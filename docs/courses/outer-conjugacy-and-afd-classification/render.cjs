/* Original selection renderer, CC0. Retains the existing reader layout. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const MarkdownIt=require('markdown-it'),katex=require('katex');
const dir=__dirname, selection=JSON.parse(fs.readFileSync(path.join(dir,'selection.json'),'utf8')).lessons;
const course=JSON.parse(fs.readFileSync(path.join(dir,'course.json'),'utf8'));
const renderables=[...selection,...(course.companions||[])];
const isDraft=course.status==='draft';
const draftNotice=`<aside class="draft-notice" aria-label="Course scope"><p>This course selection contains ${selection.length} lessons. <a href="source-review.html">Mathematical scope and prerequisites</a>.</p></aside>`;
const requested=process.argv[2]||selection[0].id;
if(!renderables.some(item=>item.id===requested))throw Error('Unknown selected lesson');
const item=renderables.find(item=>item.id===requested), sourcePath=path.join(dir,item.editable_source);
const escape=s=>s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const md=new MarkdownIt({html:false,linkify:false,typographer:false});
const ids=[];
md.renderer.rules.heading_open=(tokens,i,o,e,self)=>{let id=tokens[i+1].content.replace(/@@INLINE(\d+)@@/g,(_,n)=>math[Number(n)].tex).replace(/[^a-zA-Z0-9\s-]/g,'').trim().toLowerCase().replace(/\s+/g,'-');if(ids.includes(id))throw Error('Duplicate heading');ids.push(id);tokens[i].attrSet('id',id);return self.renderToken(tokens,i,o);};
const mathJaxConfig=JSON.stringify({tex:{inlineMath:[[String.fromCharCode(92)+'(',String.fromCharCode(92)+')']],displayMath:[[String.fromCharCode(92)+'[',String.fromCharCode(92)+']']],processEscapes:true},options:{ignoreHtmlClass:'no-math',processHtmlClass:'math'}});
const source=fs.readFileSync(sourcePath,'utf8'),math=[];const title=source.split('\n')[0].replace(/^# /,'').trim();
const solutions=(source.match(/\*Solution\.\*/g)||[]).length;
if(solutions!==item.solved_exercises)throw Error('Solution count does not match selection');
const courseNavigation=selection.map(entry=>`<a href="${entry.reader}">${escape(entry.navigation_label||entry.title)}</a>`).join(' · ');
let text=source.replace(/\\\[([\s\S]*?)\\\]/g,(_,tex)=>{let i=math.length;math.push({tex,display:true});return `\n\n@@BLOCK${i}@@\n\n`;}).replace(/\\\(([\s\S]*?)\\\)/g,(_,tex)=>{let i=math.length;math.push({tex,display:false});return `@@INLINE${i}@@`;});
let body=md.render(text);
// Permit explicit mathematical anchors while keeping other raw HTML escaped.
body=body.replace(/&lt;a id=&quot;([A-Za-z0-9_.:-]+)&quot;&gt;&lt;\/a&gt;/g,'<a id="$1"></a>');
for(let i=0;i<math.length;i++){
 const {tex,display}=math[i];katex.renderToString(tex,{displayMode:display,throwOnError:true,strict:'error',trust:false});
 if(display){const tag=tex.match(/\\tag\{([^}]+)\}/);const expression=tex.replace(/\\tag\{[^}]+\}/,'');body=body.replace(new RegExp(`<p>@@BLOCK${i}@@</p>\\n?`),`<div class="equation"><div class="math math-display">\\[${escape(expression)}\\]</div>${tag?`<span class="equation-tag">(${escape(tag[1])})</span>`:''}</div>\n`);}
 else body=body.replace(`@@INLINE${i}@@`,`<span class="math">\\(${escape(tex)}\\)</span>`);
}
if(/@@(?:BLOCK|INLINE)/.test(body))throw Error('Unresolved math');
// Markdown source links use source-directory coordinates. Correct both image
// and download paths, then send selected lesson links to their HTML readers.
body=body.replace(/(href|src)="([^"#]+)(#[^"]*)?"/g,(_,attribute,url,fragment)=>{
 if(/^(?:[a-z][a-z0-9+.-]*:|\/\/|\/)/i.test(url))return `${attribute}="${url}${fragment||''}"`;
 let target=path.posix.normalize(path.posix.join(path.posix.dirname(item.editable_source),url));
 if(attribute==='href'){
  let sourceName=path.posix.basename(target);
  const linked=renderables.find(entry=>target===entry.editable_source);
  if(linked)target=linked.reader;
 }
 return `${attribute}="${target}${fragment||''}"`;
});
// A partial draft edition must not offer broken links as supplied proofs.
const unbundled=new Set(item.unbundled_programme_links||[]);
body=body.replace(/<a href="([^"]+)">([\s\S]*?)<\/a>/g,(all,url,label)=>{
 const target=url.split('#')[0];
 return (unbundled.has(target)||unbundled.has(path.posix.basename(target)))?`<span class="unbundled-lesson">${label} <small>(lesson outside this selection)</small></span>`:all;
});
const prerequisiteNotice=item.prerequisite_notice?`<aside class="draft-notice" aria-label="Prerequisite scope"><p>${escape(item.prerequisite_notice)}</p></aside>`:'';
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(title)} · Open Mathematics Courses</title><meta name="description" content="${escape(title)}: ${item.numbered_lesson===false?'programme proof companion':(isDraft?'lesson draft':'mathematical lesson')+' with '+solutions+' solved exercises'}."><link rel="stylesheet" href="../../assets/site.css"><style>.draft-notice{max-width:880px;margin:1rem auto;padding:.5rem 1rem;border-left:4px solid #856000;background:#fff8df;color:#342b17}.equation{position:relative;margin:1.25rem 0;padding:0 3.8rem}.equation-tag{position:absolute;right:0;top:50%;transform:translateY(-50%);font-family:serif}.math-display{overflow-x:auto;padding:.4rem 0}.lesson{max-width:880px}mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden}@media(max-width:600px){.lesson{padding:1rem}.equation{padding:0}.equation-tag{position:static;display:block;transform:none;text-align:right;margin-top:.25rem}}</style><script>window.MathJax=${mathJaxConfig};</script><script defer src="../../assets/mathjax/tex-chtml-full.js"></script></head><body class="no-math"><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="header-inner"><a class="brand" href="../../">Open Mathematics Courses</a><nav class="primary-nav" aria-label="Main"><a href="../../">Courses</a><a href="../../licensing.html">Licensing</a></nav><p class="lang-note">English</p></div></header><main id="main"><nav class="crumbs" aria-label="Breadcrumb"><a href="../../">All courses</a> › Operator algebras</nav><nav class="lesson-nav" aria-label="Course lessons">${courseNavigation}</nav>${draftNotice}${prerequisiteNotice}<article class="lesson">${body}</article><nav class="lesson-nav" aria-label="Sources"><a href="${item.editable_source}">Editable Markdown</a> · <a href="${item.provenance||'provenance.json'}">Sources and authorship</a> · <a href="LICENSE.txt">Licences and component notices</a></nav></main></body></html>\n`;
fs.writeFileSync(path.join(dir,item.reader),html);
console.log(JSON.stringify({pass:true,lesson:item.id,solutions,math_expressions:math.length,displays:math.filter(x=>x.display).length,source_sha256:crypto.createHash('sha256').update(source).digest('hex'),html_sha256:crypto.createHash('sha256').update(html).digest('hex'),heading_ids:ids}));

(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory();else root.ProgrammeSearch=factory();})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const fieldWeights=[[1,30],[2,18],[4,18],[8,12],[16,2],[32,6],[64,8],[128,12],[256,1],[512,1],[1024,2]];
 const scaffolding=new Set(['how','can','i','find','prove','show','the','a','an','to','of','and','for','in']);
 const normalize=text=>String(text??'').normalize('NFKD').toLowerCase().replace(/\p{M}/gu,'');
 const tokens=text=>normalize(text).match(/[\p{L}\p{N}]+/gu)||[];
 const phrase=text=>tokens(text).join(' ');
 const weight=mask=>fieldWeights.reduce((best,[bit,score])=>mask&bit?Math.max(best,score):best,0);
 function create(index){
  const vocabulary=Object.keys(index.postings).sort();
  const names=index.documents.map(d=>({id:phrase(d.id),name:phrase(d.name),aliases:d.aliases.map(phrase)}));
  function lowerBound(word){let lo=0,hi=vocabulary.length;while(lo<hi){const mid=(lo+hi)>>1;if(vocabulary[mid]<word)lo=mid+1;else hi=mid;}return lo;}
  function variants(word){
   const found=new Set(index.postings[word]?[word]:[]);const bases=[word];
   if(word.length>5&&word.endsWith('ies'))bases.push(word.slice(0,-3)+'y');
   else if(word.length>5&&word.endsWith('es'))bases.push(word.slice(0,-2));
   if(word.length>4&&word.endsWith('s')&&!word.endsWith('ss'))bases.push(word.slice(0,-1));
   for(const base of bases)if(base.length>=4){for(let i=lowerBound(base);i<vocabulary.length&&vocabulary[i].startsWith(base);i++)found.add(vocabulary[i]);}
   return [...found];
  }
  function search(query,filters={}){
   const raw=[...new Set(tokens(query))];let words=raw.filter(w=>!scaffolding.has(w));if(!words.length)words=raw;
   const selected=d=>Object.entries(filters).every(([key,value])=>{
    if(!value)return true;
    if(key==='coverage')return value==='anchor'?d.exact_anchor:value==='unresolved_anchor'?!d.exact_anchor:value==='statement'?d.statement_excerpt:value==='passage'?d.registered_passage:false;
    return d[key]===value;
   });
   if(!words.length)return {query,words:[],matches:[],empty:true};
   const maps=words.map(word=>{
    const matches=new Map();
    for(const term of variants(word)){
     const list=index.postings[term];const multiplier=term===word?1:.65;
     for(let i=0;i<list.length;i+=2){const number=list[i],mask=list[i+1],score=weight(mask)*multiplier;const previous=matches.get(number);matches.set(number,{score:Math.max(previous?.score||0,score),mask:(previous?.mask||0)|mask});}
    }
    return matches;
   }).sort((a,b)=>a.size-b.size);
   const matches=[];const exact=phrase(query);
   for(const [number,first] of maps[0]){
    if(!selected(index.documents[number]))continue;
    let score=first.score,mask=first.mask,all=true;
    for(const map of maps.slice(1)){const item=map.get(number);if(!item){all=false;break;}score+=item.score;mask|=item.mask;}
    if(!all)continue;
    const name=names[number];
    if(name.id===exact)score+=10000;
    else if(name.name===exact||name.aliases.includes(exact))score+=1000;
    else if(name.name.includes(exact)||name.aliases.some(x=>x.includes(exact)))score+=150;
    matches.push({number,score,mask});
   }
   matches.sort((a,b)=>b.score-a.score||index.documents[a.number].name.localeCompare(index.documents[b.number].name)||index.documents[a.number].id.localeCompare(index.documents[b.number].id));
   return {query,words,matches,empty:false};
  }
  return {search,documents:index.documents};
 }
 return {create,normalize,tokens};
});

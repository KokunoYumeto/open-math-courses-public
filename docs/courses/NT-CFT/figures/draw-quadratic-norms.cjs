/* Original exact norm-subgroup diagram. OpenAI GPT-6.1 Sol, Codex, Ultra. CC0. */
const fs=require('fs'),path=require('path');
const sharp=require(process.env.NT_CFT_NODE_MODULES ? process.env.NT_CFT_NODE_MODULES+'/sharp' : 'sharp');
const out=path.resolve(__dirname,'../assets');fs.mkdirSync(out,{recursive:true});
const width=720,height=1010;
const pieces=['<svg xmlns="http://www.w3.org/2000/svg" width="'+width+'" height="'+height+'" viewBox="0 0 '+width+' '+height+'"><rect width="720" height="1010" fill="#ffffff"/><g font-family="DejaVu Sans, sans-serif" fill="#173d45">'];
function text(x,y,s,size=26,anchor='middle'){pieces.push('<text x="'+x+'" y="'+y+'" font-size="'+size+'" text-anchor="'+anchor+'">'+s+'</text>');}
text(360,48,'Quadratic norm subgroups of Q₂',32);
function panel(top,title,subtitle,predicate){
 text(360,top,title,29);text(360,top+40,subtitle,23);
 text(60,top+142,'k',27);
 text(455,top+100,'Odd unit u modulo 4',24);
 const xs=[350,555],ys=Array.from({length:5},(_,i)=>top+140+i*48);
 text(xs[0],top+132,'1',26);text(xs[1],top+132,'3',26);
 for(let i=0;i<5;i++){
  const k=i-2,y=ys[i]+24;text(95,y+7,String(k),25);
  for(let j=0;j<2;j++){
   const ok=predicate(k,j===0?1:3),x=xs[j];
   pieces.push('<rect x="'+(x-85)+'" y="'+(y-19)+'" width="170" height="38" rx="6" fill="'+(ok?'#d9edf2':'#f2f3f4')+'" stroke="'+(ok?'#17708a':'#c8ced0')+'" stroke-width="1.5"/>');
   text(x,y+7,ok?'norm':'non-norm',23);
  }
 }
 text(360,top+420,'Each cell: all a = 2ᵏu in that unit class.',23);
}
panel(105,'Unramified quadratic extension','Norm condition: k is even',(k,u)=>k%2===0);
panel(555,'Ramified extension Q₂(i) / Q₂','Norm condition: u ≡ 1 modulo 4',(k,u)=>u===1);
pieces.push('</g></svg>');
const svg=pieces.join('\n');fs.writeFileSync(path.join(out,'quadratic-norms.svg'),svg);
sharp(Buffer.from(svg)).resize(width*2,height*2).png().toFile(path.join(out,'quadratic-norms.png')).then(()=>console.log('rendered quadratic norm comparison')).catch(e=>{console.error(e);process.exitCode=1;});

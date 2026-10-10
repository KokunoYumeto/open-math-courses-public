#!/usr/bin/env node
/* Original wrapper expression CC0-1.0. External software retains its terms. */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'data.json'),'utf8'));
const svg=path.join(__dirname,data.slug+'.svg');
const png=path.join(__dirname,data.slug+'.png');
const checkOnly=process.argv.includes('--check-only');
(async()=>{
  const options={headless:true,args:['--disable-gpu']};
  if(process.env.CHROME_EXECUTABLE) options.executablePath=process.env.CHROME_EXECUTABLE;
  const browser=await chromium.launch(options);
  try {
    const page=await browser.newPage({viewport:data.dimensions_px,deviceScaleFactor:1});
    await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#fff">'+fs.readFileSync(svg,'utf8')+'</body></html>');
    await page.evaluate(()=>document.fonts.ready);
    const check=await page.evaluate(()=>{
      const box=document.querySelector('svg').viewBox.baseVal;
      const labels=Array.from(document.querySelectorAll('text')).map((el,index)=>{
        const b=el.getBBox();return {index,text:el.textContent,x:b.x,y:b.y,width:b.width,height:b.height};
      });
      const clipped=labels.filter(b=>b.x<0||b.y<0||b.x+b.width>box.width||b.y+b.height>box.height);
      const overlaps=[];
      for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
        const a=labels[i],b=labels[j],dx=Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x),dy=Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y);
        if(dx>1&&dy>1)overlaps.push({a:a.text,b:b.text,overlap:[dx,dy]});
      }
      return {clipped,overlaps,labelCount:labels.length,dimensions:[box.width,box.height]};
    });
    if(check.clipped.length||check.overlaps.length)throw new Error('Native SVG label checks failed: '+JSON.stringify(check));
    if(!checkOnly) await page.screenshot({path:png,fullPage:false,omitBackground:false,timeout:30000});
    console.log(JSON.stringify({output:path.basename(png),checkOnly,labelCheck:check}));
  } finally {await browser.close();}
})().catch(error=>{console.error(error.stack||String(error));process.exitCode=1;});

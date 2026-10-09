// Original CC0 rendering wrapper. Installed software and fonts retain their terms.
const fs=require('fs');const path=require('path');const {pathToFileURL}=require('url');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const dir=path.resolve(process.argv[2]||'generated');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_EXECUTABLE||undefined});
 try{
  const page=await browser.newPage({viewport:{width:760,height:1000},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(dir,'joint-graph-dirac.svg')).href,{waitUntil:'load'});
  await page.screenshot({path:path.join(dir,'joint-graph-dirac.png')});
  const bad=await page.evaluate(()=>[...document.querySelectorAll('text')].filter(e=>{const b=e.getBBox();return b.x<0||b.y<0||b.x+b.width>760||b.y+b.height>1000;}).map(e=>e.textContent));
  if(bad.length)throw Error('Clipped figure labels: '+JSON.stringify(bad));
  process.stdout.write(JSON.stringify({rendered:true,width:760,height:1000,clippedLabels:bad})+'\n');
 }finally{await browser.close();}
})().catch(e=>{process.stderr.write(String(e)+'\n');process.exitCode=1;});

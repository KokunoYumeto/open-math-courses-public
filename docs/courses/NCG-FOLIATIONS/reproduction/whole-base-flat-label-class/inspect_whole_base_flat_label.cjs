// CC0. Render and inspect the generated SVG with locally installed Playwright.
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
(async()=>{
 const dir=process.argv[2]||__dirname;
 const options={headless:true};
 if(process.env.CHROME_EXECUTABLE)options.executablePath=process.env.CHROME_EXECUTABLE;
 const browser=await chromium.launch(options);
 try {
  const page=await browser.newPage({viewport:{width:1220,height:930}});
  await page.goto(pathToFileURL(path.join(dir,'whole-base-flat-label-class.svg')).href);
  await page.evaluate(async()=>{await document.fonts.ready;});
  const result=await page.evaluate(()=>{
   const svg=document.querySelector('svg');
   return {svg:!!svg,external_images:svg.querySelectorAll('image').length,
    overflow_text:[...svg.querySelectorAll('text')].filter(e=>{
     const b=e.getBBox();return b.x<0||b.y<0||b.x+b.width>1200||b.y+b.height>900;
    }).map(e=>e.textContent)};
  });
  if(!result.svg||result.external_images||result.overflow_text.length)throw Error(JSON.stringify(result));
  await page.locator('svg').screenshot({path:path.join(dir,'whole-base-flat-label-class.png')});
  fs.writeFileSync(path.join(dir,'WHOLE-BASE-FLAT-LABEL-RENDER.json'),JSON.stringify(result,null,2)+'\n');
  process.stdout.write(JSON.stringify(result)+'\n');
 }finally{await browser.close();}
})().catch(e=>{process.stderr.write(String(e)+'\n');process.exitCode=1;});

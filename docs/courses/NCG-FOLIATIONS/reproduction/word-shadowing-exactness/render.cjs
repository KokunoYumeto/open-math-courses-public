#!/usr/bin/env node
/* Original wrapper expression: CC0-1.0. External software keeps its terms. */
'use strict';

const fs = require('node:fs');
const path = require('node:path');

const moduleChoice = process.env.PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(moduleChoice);
const directory = __dirname;
const svgPath = path.join(directory, 'word-shadowing-exactness.svg');
const pngPath = path.join(directory, 'word-shadowing-exactness.png');
const data = JSON.parse(fs.readFileSync(path.join(directory, 'data.json'), 'utf8'));

(async () => {
  const options = { headless: true, args: ['--disable-gpu'] };
  if (process.env.CHROME_EXECUTABLE) options.executablePath = process.env.CHROME_EXECUTABLE;
  const browser = await chromium.launch(options);
  try {
    const page = await browser.newPage({
      viewport: { width: data.dimensions_px.width, height: data.dimensions_px.height },
      deviceScaleFactor: 1,
    });
    const source = fs.readFileSync(svgPath, 'utf8');
    await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#fff">'+source+'</body></html>');
    await page.evaluate(() => document.fonts.ready);
    const check = await page.evaluate(() => {
      const root = document.querySelector('svg');
      const box = root.viewBox.baseVal;
      const texts = Array.from(document.querySelectorAll('text'));
      const bounds = texts.map((element, index) => {
        const b = element.getBBox();
        return { index, text: element.textContent, x: b.x, y: b.y, width: b.width, height: b.height };
      });
      const clipped = bounds.filter(b => b.x < 0 || b.y < 0 || b.x+b.width > box.width || b.y+b.height > box.height);
      const overlaps = [];
      for (let i=0; i<bounds.length; i++) {
        for (let j=i+1; j<bounds.length; j++) {
          const a=bounds[i], b=bounds[j];
          const dx=Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x);
          const dy=Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y);
          if (dx>1 && dy>1) overlaps.push({ a:a.text, b:b.text, overlap:[dx,dy] });
        }
      }
      return { clipped, overlaps, labelCount:bounds.length, dimensions:[box.width,box.height] };
    });
    if (check.clipped.length || check.overlaps.length) {
      throw new Error('Label geometry failed: '+JSON.stringify(check));
    }
    await page.screenshot({ path:pngPath, fullPage:false, omitBackground:false, timeout:30000 });
    console.log(JSON.stringify({ output:path.basename(pngPath), labelCheck:check }));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error.stack || String(error)); process.exitCode=1; });

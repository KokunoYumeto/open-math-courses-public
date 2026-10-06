/* Original figure and code: GPT-6.1 Sol (OpenAI), Codex, Ultra. CC0 1.0.
   Run with Node.js and the sharp package. No external figure is reused. */
const fs = require('fs');
const path = require('path');
let sharp;
try { sharp = require('sharp'); }
catch (_) { sharp = require(process.env.NT_CFT_NODE_MODULES + '/sharp'); }
const output = path.resolve(__dirname, '../assets');
fs.mkdirSync(output, { recursive: true });
const levels = [
  {modulus: 2, y: 125, residues: [0, 1], x: [200, 600]},
  {modulus: 4, y: 345, residues: [0, 2, 1, 3], x: [100, 300, 500, 700]},
  {modulus: 8, y: 565, residues: [0, 4, 2, 6, 1, 5, 3, 7], x: [50, 150, 250, 350, 450, 550, 650, 750]}
];
let svg = '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="680" viewBox="0 0 800 680"><rect width="800" height="680" fill="white"/><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke"/></marker></defs><g font-family="DejaVu Sans,sans-serif" text-anchor="middle">';
for (let k = 1; k < levels.length; k++) {
  const upper = levels[k - 1], lower = levels[k];
  lower.residues.forEach((residue, j) => {
    const i = upper.residues.indexOf(residue % upper.modulus);
    const blue = residue === 3 % lower.modulus;
    svg += `<line x1="${lower.x[j]}" y1="${lower.y-35}" x2="${upper.x[i]}" y2="${upper.y+43}" stroke="${blue ? '#005a9c' : '#b0b8c0'}" stroke-width="${blue ? 7 : 3}" marker-end="url(#arrow)"/>`;
  });
}
for (const row of levels) {
  svg += `<text x="400" y="${row.y+85}" font-size="34" fill="#283747">mod ${row.modulus}</text>`;
  row.residues.forEach((residue, j) => {
    const blue = residue === 3 % row.modulus;
    svg += `<circle cx="${row.x[j]}" cy="${row.y}" r="34" fill="${blue ? '#005a9c' : '#ffffff'}" stroke="${blue ? '#005a9c' : '#687787'}" stroke-width="3"/><text x="${row.x[j]}" y="${row.y+15}" font-size="43" fill="${blue ? '#ffffff' : '#162534'}">${residue}</text>`;
  });
}
svg += '</g></svg>';
fs.writeFileSync(path.join(output, 'compatible-residues.svg'), svg);
sharp(Buffer.from(svg)).resize(1600,1360).png().toFile(path.join(output, 'compatible-residues.png'));

"""Corrected word reflection and the actual modified weighted-spin cup."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="850" viewBox="0 0 740 850"><rect width="740" height="850" fill="white"/>']
def text(x,y,s,size=17,bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb'):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')
text(26,40,'Complement the finite words before reflection',24,True)
text(26,74,'p = 1/4, q = 3/4; d = 16/3; λ = 3/16. Exact proof: 62.6.',18)
rect(18,94,704,255)
text(36,128,'C₃ blocks: sizes 1, 3, 3, 1. Values below are minimal weights.',17,True)
cols=[42,176,307,437,572]
for x,s in zip(cols,['ones ℓ','0','1','2','3']):text(x,169,s,18,True)
for y,label,vals in [
 (212,'inherited',['1/64','3/64','9/64','27/64']),
 (254,'specified θ',['27/64','9/64','3/64','1/64']),
 (297,'β = θσ',['1/64','3/64','9/64','27/64'])]:
 text(cols[0],y,label,17,True)
 for x,s in zip(cols[1:],vals):text(x,y,s,18)
text(36,333,'σ complements every letter: ℓ ↦ 3−ℓ. β is trace preserving.',17)
rect(18,369,704,198,'#eef8f4')
text(36,403,'The same correction changes the lower cup',20,True)
text(42,439,'Original f: 01,10 block',17,True);text(402,439,'Modified g: 01,10 block',17,True)
text(55,478,'[ 3/4     √3/4 ]',20);text(417,478,'[ 1/4     √3/4 ]',20)
text(55,516,'[ √3/4    1/4  ]',20);text(417,516,'[ √3/4    3/4  ]',20)
text(36,551,'σ(gⱼ) = fⱼ;  θ(fⱼ) = eⱼ;  therefore β(gⱼ) = eⱼ.',18)
rect(18,587,704,155,'#fff7ea')
text(36,623,'E_(first-site diagonal)(g) = (3/16)1.',19,True)
text(36,661,'E_N(g) = (9/16)P₀ + (1/16)P₁, on the second site.',18)
text(36,700,'g implements F with first-tail-site weights (3/4,1/4).',18)
text(36,730,'F preserves the inherited trace only at p = q.',16)
text(26,781,'β extends normally from M to M′ ∩ T and sends each tail to Bⱼ.',17)
text(26,812,'The modified cup supplies all shifted scalar identities; C₀ = M follows.',17)
text(26,843,'Sources: course 47 balanced-spin construction; Pimsner–Popa, pp. 83–85.',15)
out.append('</svg>')
(R/'modified-spin-reflection.svg').write_text('\n'.join(out),encoding='utf-8')

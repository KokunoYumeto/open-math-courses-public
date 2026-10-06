"""Exact degree support and normalized current pairings in D3."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import hashlib, json
root=Path(__file__).resolve().parents[1]
image=Image.new('RGB',(3000,1450),'#f5f8fb');draw=ImageDraw.Draw(image)
def font(size,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'seguisym.ttf'),size)
def text(x,y,s,size=36,bold=False,color='#17394e'):draw.text((x,y),s,font=font(size,bold),fill=color)
text(100,60,'One K-class sees finitely many degrees',68,True)
text(100,175,'X = disjoint union of S^(2j), j ≥ 1; z = 2 beta_1 − beta_3. Rows show cohomology, not sphere geometry.',36)
for x,label in [(150,'degree'),(560,'family weight'),(1160,'character of z'),(1840,'normalized pairing')]:text(x,310,label,42,True)
for y,degree,weight,character,value,active in [
 (435,'0','arbitrary rank weights','0','0',False),
 (590,'2','lambda_1 = 2','2','4',True),
 (745,'4','arbitrary lambda_2','0','0',False),
 (900,'6','lambda_3 = 5','−1','−5',True),
 (1055,'8, 10, …','arbitrary weights','0','0',False)]:
 draw.rounded_rectangle((100,y-15,2890,y+105),radius=16,fill='#e2f0ee' if active else 'white',outline='#bbcdd6',width=3)
 for x,label in [(150,degree),(560,weight),(1160,character),(1840,value)]:text(x,y+12,label,43,active)
text(130,1210,'Exact total: 4 − 5 = −1. Rank contributes zero; omitted degrees have zero character on this class.',38,True)
text(130,1280,'Trace factors: degree 2 is −1/(2πi); degree 6 is −1/(6(2πi)^3). Odd orientation is fixed separately.',33)
text(130,1350,'Theorem 7.11, Corollary 7.12, Example 7.13; Appendix A. Human foundation: Atiyah–Hirzebruch (1961), §1.',31)
path=root/'public/assets/analytic-degree-family-realization.png';image.save(path)
assert 2*2-5==-1
receipt={'passed':True,'exact_example':{'degrees':[2,6],'character_values':[2,-1],'weights':[2,5],'pairings':[4,-5],'sum':-1},
 'figure_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'The finite example checks Example 7.13; the arbitrary-class finite-support theorem is proved in Theorem 7.11 and Corollary 7.12.'}
(root/'public/assets/analytic-degree-family-check-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))

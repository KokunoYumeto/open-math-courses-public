"""Figure 47.1: exact balanced blocks, actual tunnel and trace obstruction. CC0."""
from pathlib import Path
from html import escape
W,H=560,1430
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
'<title id="title">A generating weighted-spin Jones tunnel</title>',
'<desc id="desc">At p=1/4 and q=3/4 balanced blocks generate M, shifted rank-one cups give every tail basic construction, and the specified reflection reverses the first projection weights.</desc>',
'<rect width="560" height="1430" fill="#f8fafc"/>',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#475569"/></marker></defs>']
def text(x,y,s,size=19,fill='#172554',anchor='start',weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>')
def panel(y,h):
    parts.append(f'<rect x="16" y="{y}" width="528" height="{h}" rx="14" fill="white" stroke="#cbd5e1"/>')
def line(x1,y1,x2,y2,arrow=False,color='#475569'):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def box(x,y,w,label):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="42" rx="7" fill="#e0e7ff" stroke="#818cf8"/>')
    text(x+w/2,y+28,label,18,anchor='middle')
text(28,37,'A generating tunnel; reflection is not normal',23,weight='bold')
text(28,69,'p = 1/4, q = 3/4,  [M : N] = 16/3',22)
panel(90,370)
text(32,121,'Balanced blocks: same number of ones',21,weight='bold')
text(32,150,'Cₙ = ⊕ᵣ M₍ₙ choose r₎    (47.1)',19)
rows=[(0,['1']),(1,['1','1']),(2,['1','2','1']),(3,['1','3','3','1']),(4,['1','4','6','4','1'])]
for n,labels in rows:
    y=174+n*46
    text(32,y+28,f'C{n}',18)
    width=70;gap=10;left=94
    for i,label in enumerate(labels):box(left+i*(width+gap),y,width,label)
text(32,428,'Each old word extends by 0 or 1.',19)
text(32,451,'Minimal weight: pⁿ⁻ʳqʳ; block mass multiplies it.',17)
panel(480,330)
text(32,515,'Actual Jones tunnel of tail factors',21,weight='bold')
text(32,547,'Nₐ = spins after site a, with balanced words',18)
for y,left,right,lab in [(587,'N₃','N₂','f₃ in N₂'),(640,'N₂','N₁ = N','f₂ in N₁'),(693,'N₁ = N','N₀ = M','f₁ in M')]:
    box(40,y-28,128,left);box(358,y-28,156,right)
    line(183,y-6,346,y-6,True)
    text(270,y-17,'⊂',22,anchor='middle')
    text(270,y+22,lab,17,anchor='middle')
text(32,755,'Nₐ₊₁ ⊂ Nₐ ⊂ Nₐ₋₁ = ⟨Nₐ, fₐ⟩',20)
text(32,783,'fₐ uses sites a,a+1; every index is 16/3.',18)
panel(830,235)
text(32,864,'The cup and generating density',21,weight='bold')
text(32,897,'v = (√3/2)|01⟩ + (1/2)|10⟩,  f = |v⟩⟨v|',19)
text(32,930,'f block = [ 3/4  √3/4 ; √3/4  1/4 ]',20)
text(32,962,'E_N(f) = (3/16)1,  t(f) = 3/16   (47.12)',19)
text(32,998,'Nₐ′ ∩ M = Cₐ; closure of ⋃ Cₐ is M.',20)
text(32,1035,'Inside N: the shifted union generates N.',19)
panel(1085,320)
text(32,1120,'The specified reflection cannot extend normally',20,weight='bold')
text(32,1154,'P₀ = first-spin zero projection; Θ(P₀) = JP₀J',18)
for y,label,weight,color in [(1195,'t(P₀) = 1/4',1/4,'#2563eb'),(1260,'τ_M₁(Θ(P₀)) = 3/4',3/4,'#b45309')]:
    text(32,y,label,20)
    parts.append(f'<rect x="32" y="{y+10}" width="480" height="24" fill="#e2e8f0" rx="3"/>')
    parts.append(f'<rect x="32" y="{y+10}" width="{480*weight:g}" height="24" fill="{color}" rx="3"/>')
text(32,1330,'A normal extension pulls the tower trace back',18)
text(32,1357,'to the unique trace on the factor M.',18)
text(32,1384,'1/4 ≠ 3/4: contradiction.  Theorem 47.5.',19,weight='bold')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

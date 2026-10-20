"""Plot the cusp and exact descent identities of Example 4.37.

GPT-6.1 Sol (OpenAI), CC0 1.0.
"""
from pathlib import Path
from html import escape

parts=[]
def text(x,y,value,size=19,**attrs):
    extra=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {extra}>{escape(value)}</text>')
def box(x,y,w,h,color='white'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{color}" stroke="#c4cfdd"/>')
def xy(a,b):return 88+470*(a+.1)/1.55,195+470*(1.7-b)/3.4
points=[]
for i in range(601):
    t=-1.15+2.3*i/600
    x,y=xy(t*t,t*t*t)
    points.append(f'{x:.6f},{y:.6f}')
parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900" role="img" aria-labelledby="title desc">
<title id="title">The cusp point quotient and its geometric restriction</title>
<desc id="desc">The curve b squared equals a cubed is plotted from 601 samples of a=t squared,b=t cubed for t from -1.15 to1.15. Marked exact points are (1,-1),(0,0),(1,1). The map has one-point geometric fibres and equal rational fields. At0 both coordinate differentials vanish, and t is not in k[t squared,t cubed]. On the fibre pair epsilon=t-s is nonzero with epsilon squared=-2s epsilon and epsilon cubed=0. On a nonzero the inverse t=b/a makes the map an isomorphism.</desc>
<rect width="1200" height="900" fill="#f6f8fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
''')
text(30,39,'The cusp point quotient and its geometric restriction',26,font_weight=650)
text(30,75,'p: A¹ → Spec k[t²,t³],   t ↦ (a,b)=(t²,t³),   b²=a³;   characteristic zero.',21)
box(25,105,560,685)
box(615,105,560,685)
text(47,145,'The exact parametrization',23,font_weight=600)
ox,oy=xy(0,0)
parts.append(f'<path d="M{ox} 181V676M75 {oy}H558" stroke="#738299" stroke-width="1.5"/>')
text(564,oy+7,'a',21)
text(ox-6,178,'b',21)
for a in [.5,1]:
    x,y=xy(a,0)
    parts.append(f'<path d="M{x} {y-5}V{y+5}" stroke="#738299"/>')
    text(x,y+27,str(a).removesuffix('.0'),16,text_anchor='middle')
for b in [-1,1]:
    x,y=xy(0,b)
    parts.append(f'<path d="M{x-5} {y}H{x+5}" stroke="#738299"/>')
    text(x-15,y+6,str(b),16,text_anchor='end')
parts.append('<polyline points="'+' '.join(points)+'" fill="none" stroke="#265ba8" stroke-width="3"/>')
for t,label,dx,dy in [(-1,'(1,−1), t=−1',-120,31),(0,'(0,0), t=0',18,-23),(1,'(1,1), t=1',-110,-19)]:
    x,y=xy(t*t,t**3)
    parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="'+('#a34224' if t==0 else '#265ba8')+'"/>')
    text(x+dx,y+dy,label,18,fill='#a34224' if t==0 else '#174880')
text(48,710,'a=t², b=t³;  −1.15 ≤ t ≤ 1.15.',20)
text(48,745,'601 samples of the exact parametrization.',19)
text(640,145,'Equal point fibres and rational fields',22,font_weight=600)
text(640,188,'k(t²,t³) = k(t),   t = t³/t² in the field.',22)
text(640,230,'t ∉ k[t²,t³]',25,fill='#a34224')
text(640,272,'d(t²)|₀ = d(t³)|₀ = 0',24,fill='#a34224')
box(638,308,513,226,'#edf2fc')
text(659,344,'On the fibre pair X ×_Y X',22,font_weight=600)
text(659,385,'R=k[t,s]/(t²−s²,t³−s³)',23)
text(659,426,'ε=t−s ≠ 0;   ε²=−2sε',24)
text(659,467,'s²ε=0  ⇒  ε³=0',24)
text(659,507,'Pointwise equality leaves nilpotents.',20)
box(638,560,513,196,'#eaf4ed')
text(659,599,'On the target open a ≠ 0',23,font_weight=600)
text(659,644,'t=b/a',30,fill='#2c6547')
text(659,687,'p is an isomorphism:',22)
text(659,726,'flatness, differential rank and descent.',20)
box(25,810,1150,72)
text(47,852,'Theorems 4.35–4.36: differential rank and the invariant sheaf need their own arguments.',22)
parts.append('</g></svg>')
svg='\n'.join(parts)+'\n'

if __name__=='__main__':
    Path(__file__).with_suffix('.svg').write_text(svg,encoding='utf-8',newline='\n')

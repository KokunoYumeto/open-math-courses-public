"""Reproduce the exact projection, original burst schedule and detector margins."""
from pathlib import Path
import math, html
P=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1760" viewBox="0 0 1400 1760">',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#244664"/></marker></defs>',
'<rect width="1400" height="1760" fill="#f4f7fb"/>']
def text(x,y,s,size=25,color='#18344f',weight='normal',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,DejaVu Sans,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(s)}</text>')
def rect(x,y,w,h,fill='#fff'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="#c9d5e3" stroke-width="2"/>')
def line(x,y,x2,y2,arrow=False,color='#244664'):
 parts.append(f'<path d="M{x},{y} L{x2},{y2}" stroke="{color}" stroke-width="2.5" fill="none"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
text(65,65,'One halting test, two fluid constructions',40,weight='bold')
text(65,107,'Exact source correspondence · VC1–VC7',25)
rect(45,140,1310,420)
text(75,187,'The history projection preserves every machine step',29,weight='bold')
rect(95,225,440,90,'#e8f1fa');rect(860,225,430,90,'#e8f1fa')
rect(95,405,440,90,'#e8f5ee');rect(860,405,430,90,'#e8f5ee')
text(315,281,'(c, h)',31,anchor='middle')
text(1075,281,'(T(c), sbh + τ(c))',29,anchor='middle')
text(315,461,'c = (q, x, y)',29,anchor='middle')
text(1075,461,'T(c)',31,anchor='middle')
line(545,270,845,270,True);text(695,248,'history transition',22,anchor='middle')
line(545,450,845,450,True);text(695,428,'original transition',22,anchor='middle')
line(315,325,315,392,True);text(345,368,'π',27)
line(1075,325,1075,392,True);text(1105,368,'π',27)
text(75,535,'τ(c) = bq + (y mod b)     ·     π T̂ = T π     ·     injective on active configurations',24)
rect(45,585,1310,555)
text(75,632,'One burst: injection, forward transport, reverse transport, withdrawal',27,weight='bold')
text(75,670,'r = [t − (k + 1)] / δₖ        δₖ = εₖ / [3(1 + νLₖ)]        εₖ = 2⁻ᵏ / 16',24)
def E(t):return math.exp(-1/t) if t>0 else 0.
def S(t):
 if t<=0:return 0.
 if t>=1:return 1.
 return E(t)/(E(t)+E(1-t))
def panel(x0,y0,width,height,func,ymax,label,color):
 line(x0,y0+height,x0+width,y0+height)
 line(x0,y0+height,x0,y0)
 for v in [0,1/8,1/4,1/2,5/8,3/4,7/8,1]:
  xx=x0+width*v
  line(xx,y0+height,xx,y0+height+7,color='#899cad')
 for v,lab in [(0,'0'),(1/4,'1/4'),(1/2,'1/2'),(3/4,'3/4'),(1,'1')]:
  text(x0+width*v,y0+height+32,lab,21,anchor='middle')
 for v in range(ymax+1):
  yy=y0+height-height*v/ymax
  text(x0-15,yy+7,str(v),21,anchor='end')
  if v:line(x0,yy,x0+width,yy,color='#e3eaf2')
 points=[]
 for j in range(601):
  r=j/600
  points.append((x0+width*r,y0+height-height*func(r)/ymax))
 parts.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(points))+'" stroke="'+color+'" stroke-width="4" fill="none"/>')
 text(x0+width/2,y0-20,label,25,weight='bold',anchor='middle')
 text(x0+width+18,y0+height+32,'r',24)
panel(115,755,510,220,lambda r:S(8*r)-S(8*r-7),1,'Packet amplitude ωₖ(t)','#167c5a')
panel(790,755,480,220,lambda r:3*(S(8*r-1)-S(8*r-5)),3,'Clock λₖ(t), example k + 1 = 3','#2667a7')
text(75,1050,'ω′ₖ ≠ 0 only while λₖ = 0: both injection and withdrawal occur at the initial position.',23)
text(75,1090,'These curves display the stated smooth formulas; the estimates are proved analytically.',22,color='#49647a')
rect(45,1165,1310,260)
text(75,1212,'Exact mass for every input, including after halting',29,weight='bold')
text(90,1270,'∫[0,1]² w(t,X) dX = ∑ₖ Mₖ ωₖ(t)       Mₖ = R²ₖ₊₁ (∫ℝ φ)²',32)
text(90,1320,'The mean is zero for k + 1 + δₖ ≤ t ≤ k + 2.',27)
text(90,1370,'Zero mean permits a remaining field with both signs. It does not imply w = 0.',24)
rect(45,1450,1310,250)
text(75,1497,'The same detector event remains exact',29,weight='bold')
text(90,1550,'Never halts:  w ≤ 1/8 on 1/32 < X₂ < 1/8, at every t ≥ 0.',27,color='#167c5a')
text(90,1600,'First halt:  w ≥ 7/8 at height X₂ = 1/16 and t = k + 1 + δₖ/2.',27,color='#2667a7')
text(90,1650,'The event threshold is 1/2.  Both outcomes retain a strict proved margin.',24)
text(65,1735,'Source: OpenAI, VelocityDetection Lean sources, adc7f1241b42e322a6451854ab7e4b4c146bf78a.',20)
parts.append('</svg>')
out=P/'torus-computation-correspondence.svg'
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(out.name)


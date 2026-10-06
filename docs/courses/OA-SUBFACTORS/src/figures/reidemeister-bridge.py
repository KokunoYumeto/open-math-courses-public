"""Original exact-coordinate figure for the full smooth Reidemeister proof. CC0 1.0."""
from pathlib import Path
from html import escape
from fractions import Fraction as F

R=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="2010" viewBox="0 0 740 2010">',
       '<rect width="740" height="2010" fill="#fff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#152b3d} .title{font-size:25px;font-weight:bold}.h{font-size:21px;font-weight:bold}.t{font-size:17px}.small{font-size:15px}</style>']
def text(x,y,s,cls='t',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def line(points,color='#52687b',width=2,dash=None,halo=False):
    xy=' '.join(f'{float(x):.4f},{float(y):.4f}' for x,y in points)
    if halo:parts.append(f'<polyline points="{xy}" fill="none" stroke="white" stroke-width="{width+5}" stroke-linejoin="round"/>')
    parts.append(f'<polyline points="{xy}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def poly(points,fill):
    xy=' '.join(f'{float(x):.4f},{float(y):.4f}' for x,y in points)
    parts.append(f'<polygon points="{xy}" fill="{fill}" fill-opacity=".35" stroke="{fill}" stroke-width="1.2"/>')
def dot(p,color='#152b3d'):
    parts.append(f'<circle cx="{float(p[0])}" cy="{float(p[1])}" r="4" fill="{color}"/>')
def separator(y):line([(24,y),(716,y)],'#d2dbe4',1)
text(28,42,'A finite bridge from spatial motion to diagram moves','title')
text(28,73,'Exact coordinate models for Lemma 45.0b and Theorem 45.0.','small')

text(28,122,'1. One vertex change uses two empty triangles','h')
coords={'a':(-1,0,0),'u':(0,0,0),'v':(3,0,0),'z':(3,3,0),'b':(3,4,0),'c':(-1,4,0),'w':(3,F(1,4),F(1,4))}
def iso(q):x,y,z=map(float,q);return (165+85*(x+.45*y),325-85*(.35*y+1.2*z))
q={k:iso(v) for k,v in coords.items()}
poly([q[x] for x in ['u','v','w']],'#e37b58')
poly([q[x] for x in ['v','w','z']],'#47a1c3')
line([q[x] for x in ['a','u','v','z','b','c','a']],'#7f8c97',2)
line([q[x] for x in ['u','w','z']],'#11659b',3)
line([q['w'],q['v']],'#d0633f',2,'5 4')
for k in coords:dot(q[k])
text(40,358,'a=(−1,0,0)','small')
text(130,355,'u=(0,0,0)','small')
text(390,359,'v=(3,0,0)','small')
text(547,260,'z=(3,3,0)','small')
text(582,199,'b=(3,4,0)','small')
text(158,193,'c=(−1,4,0)','small')
line([q['w'],(485,385)],'#11659b',1)
text(485,407,'w=(3,¼,¼)','small')
text(28,441,'u—v—z   →   u—w—v—z   →   u—w—z')
text(28,470,'Full link: a,u,v,z,b,c,a. Nonincident edge clearance d=1.')
text(28,499,'‖w−v‖²=⅛ < d²/4. Barycentric sheet distance is at most ‖w−v‖.')
text(28,526,'Affine 3D view; metric bound uses the displayed exact spatial coordinates.','small')
separator(550)

text(28,588,'2. The swept strand may have the middle height','h')
text(28,616,'T: A=(0,0), B=(8,0), C=(4,6); sheet height 0.','small')
text(28,643,'Fixed E: y=x−1, height +1. Fixed F: y=−x+7, height −1.','small')
def sweep(ox,t):
    def p(x,y):return (ox+33*float(x),914-33*float(y))
    A,B,C=p(0,0),p(8,0),p(4,6)
    poly([A,B,C],'#d7e9f4')
    line([p(7,0),p(F(14,5),F(21,5))],'#617686',2.5)
    moving=[p(0,0),p(4*t,6*t),p(8-4*t,6*t),p(8,0)]
    line(moving,'#1675af',3,halo=True)
    line([p(1,0),p(F(26,5),F(21,5))],'#bb493b',3,halo=True)
    text(C[0],C[1]-10,'C','small','middle')
    text(A[0]-6,A[1]+23,'A','small')
    text(B[0]-3,B[1]+23,'B','small')
    text(ox+132,687,'t='+str(t),'t','middle')
    text(ox+132,963,'xE='+str(6*t+1)+'; xF='+str(7-6*t),'small','middle')
sweep(43,F(9,20));sweep(419,F(11,20))
text(370,816,'III','h','middle')
text(28,1001,'At t=½, both intersections reach X=(4,3). E > sheet > F.')
text(28,1029,'Before: xE=37/10 < xF=43/10. After: xE=43/10 > xF=37/10.','small')
text(28,1056,'Each strand keeps its height order. Local arcs continue outside this face.','small')
separator(1081)

text(28,1119,'3. Explicit smooth local lifts of all three moves','h')
text(212,1152,'t=−¼','t','middle');text(550,1152,'t=+¼','t','middle')
def plotcurve(ox,oy,fn,color='#1675af',a=-.9,b=.9,scale=100,halo=False):
    points=[(ox+scale*fn(a+(b-a)*i/160)[0],oy-scale*fn(a+(b-a)*i/160)[1]) for i in range(161)]
    line(points,color,2.5,halo=halo)
for ox,t in [(160,-.25),(498,.25)]:
    plotcurve(ox,1278,lambda s:(s*s,s*s*s-t*s),a=-.8,b=.8,scale=100)
    if t>0:
        plotcurve(ox,1278,lambda s:(s*s,s*s*s-t*s),a=.44,b=.56,scale=100,halo=True)
text(31,1235,'I','h')
text(28,1361,'(s²,s³−ts,hs). Shown h>0; at t>0, s=±√t have different heights.','small')
text(28,1386,'At the projected cusp the spatial derivative still has third component h.','small')
separator(1403)
for ox,t in [(210,-.25),(548,.25)]:
    line([(ox-95,1540),(ox+95,1540)],'#617686',2.5)
    plotcurve(ox,1540,lambda s:(s,s*s-t),a=-.85,b=.85,scale=95,halo=True)
text(31,1505,'II','h')
text(28,1600,'(s,0,h₁) and (s,s²−t,h₂). Two crossings; shown h₂>h₁.','small')
text(28,1625,'At t=0 the plane arcs are tangent; the spatial arcs remain disjoint.','small')
separator(1644)
for ox,t in [(210,-.25),(548,.25)]:
    line([(ox,1784-78),(ox,1784+78)],'#617686',2.5)
    plotcurve(ox,1784,lambda s:(s,s+t),a=-.77,b=.77,scale=85,halo=True)
    line([(ox-82,1784),(ox+82,1784)],'#bb493b',2.5,halo=True)
text(31,1745,'III','h')
text(28,1896,'(s,0,h₁), (0,s,h₂), (s,s+t,h₃); h₁,h₂,h₃ pairwise different.','small')
text(28,1921,'Crossings: (0,0), (−t,0), (0,t). Shown h₁>h₃>h₂; all orders/orientations allowed.','small')
text(28,1953,'Models shown where cutoff χ=1; endpoint collars stay fixed.','small')
text(28,1978,'Proof: Lemmas 45.0b–45.0d and Theorem 45.0.','small')
parts.append('</svg>')
out=R/'reidemeister-bridge.svg'
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(out.name)

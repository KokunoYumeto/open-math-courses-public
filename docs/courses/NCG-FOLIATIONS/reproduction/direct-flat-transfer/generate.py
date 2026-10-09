"""Original CC0 exact coordinate/type diagram; no third-party assets."""
from pathlib import Path
from fractions import Fraction
import argparse, json
from html import escape

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path('generated'));a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="1000" viewBox="0 0 760 1000"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#2563eb"/></marker></defs><rect width="760" height="1000" fill="#f8fafc"/><g font-family="Arial,sans-serif" fill="#172554">']
    def text(x,y,s,size=16,color='#172554',anchor='start'):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
    def line(x1,y1,x2,y2,color='#94a3b8',width=2,dash='',arrow=False):
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    def box(x,y,w,h):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#cbd5e1"/>')
    def dot(x,y):parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#2563eb"/>')
    text(30,38,'Incomplete flat holonomy: actual domains and direct transfer',24)
    text(30,65,'Theorem 11BN.1 · IHT.8–IHT.26 · Exercises 294–296',16,'#475569')
    box(26,88,708,326);text(45,117,'A. Two deleted points; three separate leaves at height zero',19)
    X=lambda x:255+95*x
    Y=lambda y:320-240*y
    for x,label in [(-1,'T_L: x = −1'),(1,'T_M: x = 1'),(3,'T_R: x = 3')]:
        line(X(x),158,X(x),353,dash='4 5');text(X(x),150,label,15,anchor='middle')
    for y,label in [(Fraction(1,2),'y = 1/2'),(Fraction(1,4),'y = 1/4')]:
        yy=float(Y(y));line(X(-1.55),yy,X(3.55),yy,color='#cbd5e1');text(52,yy+5,label,14)
        for x in [-1,1,3]:dot(X(x),yy)
    line(X(-1)+8,Y(Fraction(1,2)),X(1)-9,Y(Fraction(1,2)),color='#2563eb',arrow=True)
    line(X(1)+8,Y(Fraction(1,2)),X(3)-9,Y(Fraction(1,2)),color='#2563eb',arrow=True)
    text(255,184,'h',18,anchor='middle');text(445,184,'g',18,anchor='middle')
    line(X(-1.55),320,X(0)-10,320,color='#334155',width=3)
    line(X(0)+10,320,X(2)-10,320,color='#334155',width=3)
    line(X(2)+10,320,X(3.55),320,color='#334155',width=3)
    text(52,325,'y = 0',14)
    for x in [0,2]:
        xx=X(x);line(xx-6,314,xx+6,326,color='#dc2626',width=3);line(xx-6,326,xx+6,314,color='#dc2626',width=3);text(xx,350,f'({x},0) removed',14,'#b91c1c',anchor='middle')
    text(45,385,'Only positive-height cross arrows are shown. There is no zero-height cross arrow.',15)
    box(26,434,708,180);text(45,465,'B. A radius feature is shadowed; the relative cost detects the increment',18)
    text(45,496,'ρ(h) = ρ(gh) = |y|       ⇒       kρ(gh,h) = 0',20)
    text(45,530,'k(gh,h) = 1 + y⁻² for every nonunit g, independently of h',18,'#1d4ed8')
    text(45,562,'y = 1/2: cost 5        y = 1/4: cost 17        y → 0: cost → ∞',17)
    text(45,593,'Low cost ≤ R forces |y| ≥ (R−1)⁻¹ᐟ² when R > 1.',16)
    box(26,635,708,314);text(45,666,'C. The even auxiliary leaves the original disk and normal degree intact',18)
    for x,w,label in [(52,100,'A_r(G)'),(222,210,'A_m(G) ⊗ B'),(500,108,'A_m(G)')]:
        box(x,711,w,52);text(x+w/2,743,label,18,anchor='middle')
    line(153,737,214,737,color='#2563eb',arrow=True);text(183,704,'Δ_r',19,anchor='middle')
    line(433,737,492,737,color='#2563eb',arrow=True);text(465,704,'1 ⊠ κ',17,anchor='middle')
    text(52,793,'Δ_r(f) = Σδ fδ ⊗ λδ',18)
    text(52,821,'fδ retains its actual domain; B = C*r(Γ), and κ has unit index +1.',16)
    text(52,853,'Original disk: b_U[j_U][i_r] Θ = b_U[j_U][i_m]',19,'#1d4ed8')
    text(52,883,'Then x_r = Θ ⊗ x_N has degree q and original Bott pairing +1.',17)
    text(52,914,'Full inverse Spin-c coefficient and ordered right Clifford block are retained.',15)
    text(30,979,'Exact coordinate/type schematic · original CC0 expression · no global action asserted',14,'#475569')
    parts.append('</g></svg>');(a.output_dir/'direct-flat-transfer.svg').write_text(''.join(parts),encoding='utf-8')
    samples=[{'y':str(y),'radius_cost':0,'relative_cost':str(1+1/y**2)} for y in [Fraction(1,2),Fraction(1,4)]]
    data={'theorem':'11BN.1','proofs':['IHT.8–IHT.26'],'removed_points':[[0,0],[2,0]],'transversal_x':[-1,1,3],'samples':samples,'actual_positive_height_arrows':{'h':'L to M','g':'M to R','gh':'L to R'},'zero_height_cross_arrows':[],'coordinate_map':{'X':'255+95*x','Y':'320-240*y'},'scope':'exact coordinate and type schematic; not a global action','license':'CC0-1.0'}
    (a.output_dir/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(data))
if __name__=='__main__':main()

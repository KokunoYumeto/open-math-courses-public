"""Original CC0 exact metric and operator diagram; no external assets."""
from pathlib import Path
from fractions import Fraction
from html import escape
import argparse,json,math


def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path('generated'));a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="1000" viewBox="0 0 760 1000"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#2563eb"/></marker></defs><rect width="760" height="1000" fill="#f8fafc"/><g font-family="Arial,sans-serif" fill="#172554">']
    def text(x,y,s,size=16,color='#172554',anchor='start'):parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
    def box(x,y,w,h):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#cbd5e1"/>')
    def line(x1,y1,x2,y2,color='#94a3b8',dash='',arrow=False):parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    text(30,38,'Curved incomplete geometry and its graph class',24)
    text(30,65,'Theorem 11BP.1 · NK.3–NK.16 · Exercises 300–302',16,'#475569')
    box(26,88,708,214);text(45,119,'A. Actual compact words, uniform radius, polynomial count',19)
    text(45,155,'Fixed compact arrow test C → one radius ε at every word endpoint.',16)
    text(45,188,'Compact normal frames → buffered central plaques → finite states.',16)
    text(45,224,'B_n = M(2n+2)^E       ||fⁿ||I ≤ √B_n ||f||rⁿ',22,'#1d4ed8')
    text(45,258,'Nth roots: the entire neutral full norm equals the reduced norm.',16)
    text(45,283,'Distinct original arrows and isotropy remain distinct frame endpoints.',15)
    box(26,321,708,363);text(45,353,'B. A curved, incomplete periodic coordinate strip',19)
    text(45,386,'g = dt² + exp(2t²) dθ²    K = −2−4t²    shift θ by 2π/√2',18)
    X=lambda u:160+410*u;Y=lambda t:594-160*t
    line(X(0),Y(0),X(1),Y(0),color='#dc2626',dash='5 5');line(X(0),Y(1),X(1),Y(1),color='#dc2626',dash='5 5')
    line(X(0),Y(0),X(0),Y(1));line(X(1),Y(0),X(1),Y(1))
    text(90,Y(1)+5,'t = 1',15);text(90,Y(0)+5,'t = 0',15)
    for t,k in [(Fraction(3,4),'-17/4'),(Fraction(1,2),'-3'),(Fraction(1,4),'-9/4')]:
        yy=Y(float(t));line(X(0),yy,X(1),yy,color='#cbd5e1');line(X(.08),yy,X(.08+1/math.sqrt(2)),yy,color='#2563eb',arrow=True);text(52,yy+5,'t = '+str(t),14);text(589,yy+5,'K = '+k,16)
    text(X(0),621,'0',15,anchor='middle');text(X(1),621,'1',15,anchor='middle');text(365,621,'θ / (2π); angular edges identified',15,anchor='middle')
    text(45,650,'Both red t-ends are omitted and have finite radial distance.',16)
    text(45,674,'Killing rank j = 1 (∂θ); original normal degree q = 2.',17,'#1d4ed8')
    box(26,704,708,243);text(45,737,'C. The labels supply the actual reduced graph construction',18)
    text(45,778,'(M_g, i−l) → discrete diagonal → actual Čech multiplication',18)
    text(45,815,'Joint q-normal Dirac → full graph P(1 ⊗ F_A₀)P',21,'#1d4ed8')
    text(45,851,'Finite orthogonal rank blocks retain all scalar compact defects.',16)
    text(45,887,'Original disk: b_U = b_V[j_VU]; original Bott pairing +1.',18)
    text(45,922,'The full inverse Spin-c line and final right Cl_q remain unchanged.',15)
    text(30,978,'Exact coordinates and type schematic; strip is not a Euclidean metric embedding. CC0.',13,'#475569')
    parts.append('</g></svg>');(a.output_dir/'killing-rank-graph.svg').write_text(''.join(parts),encoding='utf-8',newline='\n')
    samples=[{'t':str(t),'curvature':str(-2-4*t*t)} for t in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]]
    data={'theorem':'11BP.1','equations':'NK.3–NK.16','word_count':'M(2n+2)^E','metric':'dt^2+exp(2t^2)dtheta^2','domain':'theta modulo 2pi; t in (0,1)','curvature':'-2-4t^2','samples':samples,'angular_shift':'2pi/sqrt(2)','arrow_source_theta_over_2pi':'2/25','arrow_target_theta_over_2pi':'2/25+1/sqrt(2)','coordinate_map':{'X':'160+410*theta/(2pi)','Y':'594-160*t'},'killing_rank':1,'normal_degree':2,'original_bott_pairing':1,'scope':'Whole locally constant Killing-rank transversal; no variable-rank claim','license':'CC0-1.0'}
    (a.output_dir/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({'generated':True,'samples':samples}))


if __name__=='__main__':main()

"""Boundary-controlled actual source-essential joint core: original CC0 diagram."""
from pathlib import Path
from fractions import Fraction
import argparse,base64,html,io,json,math
from PIL import Image,ImageDraw,ImageFont
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--output-dir",type=Path,required=True)
p.add_argument("--resources",type=Path,default=Path(__file__).resolve().parent.parent/"labelled-geometric-kernel")
a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
font=(a.resources/"fonts/DejaVuSans.ttf").read_bytes()
notice=(a.resources/"FONT-NOTICE.txt").read_text(encoding="utf-8")
W,H=1800,1430
im=Image.new("RGB",(W,H),"#f7fafc");d=ImageDraw.Draw(im);fonts={};overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 "<title>Boundary-controlled source-essential joint core and transported normal-domain test</title>",
 "<desc>OJC.1–10. Whole-vector boundary estimates survive compact convex selections. The actual nondegenerate inverse retains its class and full joint core after ordinary stabilization. Actual irrational-rotation transport shows that this chosen connection is not automatically holonomy covariant.</desc>",
 "<metadata>"+html.escape(notice)+"</metadata>",
 '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font).decode()+')}text{font-family:LocalSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f7fafc"/>']
def text(x,y,s,size=27,col="#183047"):
 if size not in fonts:fonts[size]=ImageFont.truetype(io.BytesIO(font),size,layout_engine=ImageFont.Layout.BASIC)
 b=d.textbbox((x,y),s,font=fonts[size],anchor="lt")
 if b[0]<0 or b[1]<0 or b[2]>W or b[3]>H:overflow.append([s,list(b)])
 d.text((x,y),s,font=fonts[size],fill=col,anchor="lt")
 svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def box(x,y,w,h):
 d.rectangle((x,y,x+w,y+h),fill="white",outline="#c4d6e5",width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#c4d6e5" stroke-width="3"/>')
def line(points,col="#176b96",width=4):
 d.line(points,fill=col,width=width)
 svg.append('<polyline points="'+" ".join(f"{x:.3f},{y:.3f}" for x,y in points)+f'" stroke="{col}" stroke-width="{width}" fill="none"/>')
def arrow(x,y,xx,yy):
 line([(x,y),(xx,yy)]);ang=math.atan2(yy-y,xx-x)
 pts=[(xx,yy)]+[(xx-16*math.cos(ang+u),yy-16*math.sin(ang+u)) for u in (-.45,.45)]
 d.polygon(pts,fill="#176b96");svg.append('<polygon points="'+" ".join(f"{x:.3f},{y:.3f}" for x,y in pts)+'" fill="#176b96"/>')
text(35,25,"A full joint core for the ACTUAL source-essential inverse",36)
text(35,85,"OJC.1–10. Proper probability base; finite buffered unit boxes; genuine transported arrows.",25)
box(35,145,825,480);box(895,145,870,480)
text(65,175,"Whole-vector control at a coordinate face",29)
line([(100,350),(790,350)],"#183047",3)
text(95,380,"0: face",23);text(720,380,"1: face",23)
d.ellipse((232,342,248,358),fill="#176b96")
svg.append('<circle cx="240" cy="350" r="8" fill="#176b96"/>')
arrow(240,325,100,325)
text(135,270,"shortest straight path: length d(x)",24)
text(65,440,"Lift the WHOLE coordinate vector along one path.",24)
text(65,485,"||ξ(μ)|| ≤ CT d(x) sup[d≤d(x)] ||∇0ξ||",26,col="#246b43")
text(65,530,"||δEk ξ|| ≤ C0 bξ(2εk) → 0; εk=4⁻k.",26,col="#246b43")
text(65,575,"Ek=χk(a(μ))Qk is compact; all fibres are retained.",23)
text(925,175,"Source, phase and full closed graph",29)
text(925,235,"Ordinary A-linear carrier map V; Φ and U move with V.",23)
text(925,285,"Copied phase F and first-copy projection P stay exact.",23)
text(925,335,"vn: common convex tails; source/arrow/adaptive tests.",24)
text(925,385,"The uniform normal GRAPH bound survives convexity.",23,col="#246b43")
text(925,435,"r*=1+Σ(1−vn); r=(r*+Fr*F)/2; S=closure(PFrP)",23)
text(925,485,"[M,Φ,FS]=dX; Φ is NONDEGENERATE.",26,col="#246b43")
text(925,535,"wmξ, Swmξ and ∇0wmξ converge on the full domain.",23,col="#246b43")
text(925,575,"span(wm C) is a core for all three completed graphs.",23)
box(35,685,825,520);box(895,685,870,520)
text(65,715,"An ACTUAL irrational-rotation arrow",29)
text(65,775,"G=Z⋉S1; α=2π(√5−1)/2; arrow label m stays.",24)
text(65,825,"V(x)e[m,n]=exp(i n sin x)e[m,n]",26)
text(65,875,"U1(x)e[m,n]=exp(i n ψ(x))e[m+1,n]",25)
text(65,925,"ψ(x)=sin x−sin(x−α); ψ′(0)=1−cos α >0",24)
text(65,975,"ξ=Σ n⁻¹ e[0,n] belongs to Dom ∇0; ∇0ξ=0.",25)
text(65,1035,"Partial derivative norm² = N |ψ′(0)|².",28,col="#b24d34")
text(65,1095,"As N→∞ the full image has no norm derivative.",25,col="#b24d34")
text(65,1145,"Genuine U does not imply U Dom ∇0 = Dom ∇0.",23,col="#b24d34")
text(925,715,"Normalized partial derivative energy",29)
line([(1025,1090),(1660,1090)],"#183047",2)
line([(1025,1090),(1025,790)],"#183047",2)
pts=[(1025+55*n,1090-23*n) for n in range(0,11)]
line(pts,"#b24d34",5)
text(965,1120,"N:",23)
for n in range(0,11,2):text(1018+55*n,1120,str(n),23)
text(1060,800,"Norm² / |ψ′(0)|² = N",26,col="#b24d34")
text(925,1170,"Finite sums illustrate the infinite lower-bound proof.",23)
box(35,1260,1730,115)
text(65,1280,"Proved: actual inverse, nondegenerate source, full joint core and transported operator graph.",25,col="#246b43")
text(65,1325,"Still needed: normal covariance/source stability, original physical sum and original Bott +1.",25,col="#b24d34")
text(35,1390,"Original CC0 diagram. Infinite proofs: OJC.1–10 and Exercises285–286; font/software terms retained.",23)
assert not overflow,overflow
partial=[dict(N=n,vector_norm_squared=str(sum((Fraction(1,j*j) for j in range(1,n+1)),Fraction())),
              normalized_derivative_norm_squared=n) for n in range(1,11)]
plateaus=[]
for k in range(1,5):
 ek=Fraction(1,4**k);later=Fraction(1,4**(k+1))
 assert 2*later<ek
 plateaus.append(dict(k=k,epsilon=str(ek),next_epsilon=str(later),strict_next_plateau_on_previous_support=True))
checks=dict(schema="ordinary-joint-core-checks/v1",field="Q with symbolic positive psi-prime factor",
 partial_coordinate_sums=partial,nested_cutoff_supports=plateaus,
 compact_probability_fibres_retained=True,whole_vector_boundary_estimate_proved_in_text=True,
 source_essential_full_joint_core_proved_in_text=True,actual_entire_inverse_class_retained=True,
 transported_operator_graph_domains_retained=True,canonical_normal_covariance_proved=False,
 full_normal_source_domain_preservation_proved=False,original_physical_sum_proved=False,
 original_Bott_comparison_proved=False,finite_samples_prove_infinite_domain_claim=False,
 canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(a.output_dir/"ordinary-joint-core.png",format="PNG",compress_level=9)
(a.output_dir/"ordinary-joint-core.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(a.output_dir/"ORDINARY-JOINT-CORE-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(exact_partial_sums=10,nested_plateau_checks=4,overflows=overflow)))

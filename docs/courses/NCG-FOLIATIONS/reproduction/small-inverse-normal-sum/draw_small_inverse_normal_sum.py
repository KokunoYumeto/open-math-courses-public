"""Small inverse commutator and completed normal sum: original CC0 diagram."""
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
 "<title>Small inverse commutator, full joint graph and adjoint-domain argument</title>",
 "<desc>SNC.1–10. The quadratic mixed estimate controls the full joint graph; a small bounded inverse commutator forces both deficiency spaces to vanish. The circle model retains a normalized source-domain obstruction. Original graph, source and Bott identifications remain separate.</desc>",
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

text(35,25,"A small INVERSE commutator closes the normal sum",36)
text(35,85,"SNC.1–10. N is self-adjoint; J anticommutes with N; H>0 has dense range and commutes with J.",24)
box(35,145,825,480);box(895,145,870,480)
text(65,175,"Two completed operators; one joint domain",29)
text(65,240,"T=J H⁻¹; Dom T=Ran H.  K=[N,H].",27)
text(65,300,"a=||H||; κ=||K||; a+κ < √(1−κ).",27)
text(65,360,"D=N+T on Dom N ∩ Dom T.",29)
text(65,425,"NT+TN = H⁻¹ J K H⁻¹ on the mixed core.",24)
text(65,490,"||Dξ||² ≥ ||Nξ||²+(1−κ)||Tξ||²",27,col="#246b43")
text(65,550,"The sum graph equals the FULL joint graph.",25,col="#246b43")
text(925,175,"The resolvent sign matters",29)
text(925,240,"Rλ=(T+iλ)⁻¹=H(J+iλH)⁻¹",27)
text(925,300,"N Rλ = −R−λ N + Cλ",29)
text(925,360,"Cλ=J B−λ⁻¹ K Bλ⁻¹; Bλ=J+iλH",25)
text(925,420,"βλ=||B−λ⁻¹ K|| → 0",27,col="#246b43")
text(925,480,"||iλ Cλ ξ|| ≤ βλ ||Tξ||",27,col="#246b43")
text(925,540,"uλξ, Tuλξ, Nuλξ → ξ, Tξ, Nξ",25)
text(925,585,"Rμ C is a core for all three graphs.",23)
box(35,685,825,520);box(895,685,870,520)
text(65,715,"Every adjoint vector is tested legally",29)
text(65,775,"H Dom D* ⊂ Dom D",29,col="#246b43")
text(65,835,"D Hξ = H D*ξ + Kξ",29)
text(65,900,"If D*ξ=±iξ:",27)
text(65,950,"√(1−κ)||ξ|| ≤ ||D Hξ||",28,col="#246b43")
text(65,1005,"||D Hξ|| ≤ (a+κ)||ξ||",28,col="#b24d34")
text(65,1065,"Strict inequality forces ξ=0 in BOTH spaces.",24)
text(65,1120,"D is SELF-ADJOINT on the full joint domain.",24,col="#246b43")
text(65,1165,"||D⁻¹|| ≤ a / √(1−κ)",25)
text(925,715,"Infinite circle check; source still matters",29)
text(925,775,"H[n]=(16n)⁻¹; N=Γ(−i∂x); K=0.",25)
text(925,835,"D[n,k] = [ [k,16n], [16n,−k] ]",26)
text(925,890,"Eigenvalues: ±√(k²+256n²); gap=16.",24)
text(925,950,"α(x)=√|sin(x/2)|; first even source only.",23)
text(925,1005,"Φ(z)ξ=e^{iα(x)}ξ is NOT in H¹.",26,col="#b24d34")
text(925,1065,"|α′(x)|² ~ 1/(8|x|): the integral diverges.",23,col="#b24d34")
text(925,1125,"Self-adjointness does not supply the source rule.",23)
text(925,1170,"This model is not the original Bott source.",23)
box(35,1260,1730,115)
text(65,1280,"Canonical coefficient inverse: all-jet local floors, small commutator and weighted limit are available.",24,col="#246b43")
text(65,1325,"Still required: original normal realization, source, spatial compacts, R-balance and original Bott +1.",24,col="#b24d34")
text(35,1390,"Original CC0 diagram. Full proofs: SNC.1–10 and Exercises287–288; font/software terms retained.",23)
assert not overflow,overflow
bounds=[]
for numerator in range(1,5):
 a0=Fraction(1,32);k0=Fraction(numerator,64)
 assert (a0+k0)**2<1-k0
 bounds.append(dict(a=str(a0),kappa=str(k0),upper_squared=str((a0+k0)**2),lower_squared=str(1-k0),strict=True))
blocks=[]
for n in range(1,5):
 for k in [-3,0,5]:
  matrix=[[k,16*n],[16*n,-k]]
  square=[[sum(matrix[i][l]*matrix[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
  energy=k*k+256*n*n
  assert square==[[energy,0],[0,energy]]
  blocks.append(dict(n=n,k=k,matrix=matrix,square=square,eigenvalue_squared=energy))
h0=Fraction(1,32);dh=Fraction(1,128);mass_squared=2/(h0*h0);mixed=-2*dh/(h0*h0)
assert abs(mixed)==dh*mass_squared
checks=dict(schema="small-inverse-normal-sum-checks/v1",field="Q",strict_deficiency_bounds=bounds,
 circle_blocks=blocks,nonzero_mixed_form=dict(h=str(h0),h_prime=str(dh),vector="(1,i)",mass_norm_squared=str(mass_squared),mixed_form=str(mixed),bound_attained=True),
 smallest_circle_gap=16,normal_realization_assumed_in_general_application=True,
 original_physical_graph_class_proved=False,original_Bott_comparison_proved=False,
 finite_samples_prove_infinite_domain_claim=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(a.output_dir/"small-inverse-normal-sum.png",format="PNG",compress_level=9)
(a.output_dir/"small-inverse-normal-sum.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(a.output_dir/"SMALL-INVERSE-NORMAL-SUM-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(exact_circle_blocks=12,strict_bounds=4,overflows=overflow)))

"""Reproducible exact proof map, HF.1–HF.7 and RR.6–RR.8."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import html, base64
out = Path(__file__).resolve().parent.parent / 'figures'
W,H=2100,1460
im=Image.new('RGB',(W,H),'#f8fafc');d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<rect width="100%" height="100%" fill="#f8fafc"/>']

# Cross-platform SVG font binding; retain the complete embedded-font licence.
fontcss=[]
for fontname,weight in [('DejaVuSansCondensed.ttf','400'),('DejaVuSansCondensed-Bold.ttf','700')]:
    fontdata=base64.b64encode((Path(__file__).resolve().parent/'fonts'/fontname).read_bytes()).decode('ascii')
    fontcss.append("@font-face{font-family:'NCG-DejaVu-Condensed';font-style:normal;font-weight:"+weight+";src:url(data:font/ttf;base64,"+fontdata+") format('truetype')}")
svg.insert(1,'<defs><style>'+''.join(fontcss)+'</style></defs>')
svg.insert(1,'<metadata>'+html.escape((Path(__file__).resolve().parent/'fonts/LICENSE_DEJAVU.txt').read_text(encoding='utf-8'))+'</metadata>')

navy='#173f59';green='#236743';red='#a53c3c'
def txt(x,y,s,size=29,color=navy,bold=False):
    f=ImageFont.truetype(str(Path(__file__).resolve().parent/'fonts'/('DejaVuSansCondensed'+('-Bold' if bold else '')+'.ttf')),size)
    d.text((x,y),s,font=f,fill=color,anchor='mm')
    svg.append(f'<text x="{x}" y="{y+size*.3}" text-anchor="middle" font-family="NCG-DejaVu-Condensed" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{html.escape(s)}</text>')
def box(x,y,w,h,title,lines,color=navy):
    d.rounded_rectangle((x,y,x+w,y+h),radius=16,fill='white',outline=color,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="white" stroke="{color}" stroke-width="3"/>')
    txt(x+w/2,y+41,title,32,color,True)
    spacing=(h-115)/max(1,len(lines)-1)
    for i,line in enumerate(lines):txt(x+w/2,y+90+i*spacing,line,27,color)
def arrow(x,y,X,Y):
    d.line((x,y,X,Y),fill=navy,width=4)
    import math
    a=math.atan2(Y-y,X-x);p=[(X,Y),(X-20*math.cos(a-.4),Y-20*math.sin(a-.4)),(X-20*math.cos(a+.4),Y-20*math.sin(a+.4))]
    d.polygon(p,fill=navy)
    svg.append(f'<path d="M{x},{y} L{X},{Y}" stroke="{navy}" stroke-width="4" fill="none"/><polygon points="{" ".join(f"{a},{b}" for a,b in p)}" fill="{navy}"/>')
txt(1050,60,'The exact native difference factors through the boundary',46,bold=True)
txt(1050,120,'B = C(closed disk),  I = C₀(open disk),  Q = C(circle);  G̃ = SU(1,1)',30)
box(55,190,625,235,'Actual lifted difference',[
    'z = [x̄] − [ȳ] ∈ KK_G̃(B, ℂ)',
    'Full form copies and all H_b retained',
    'Exact K̃ contraction gives r z = 0',
    'CL.1–27; original frame cocycle'],navy)
box(737,190,625,235,'Interior operator cancellation',[
    'M_h(F_Q − F_H),  M_hBT are compact',
    'Fixed I and group representations',
    'W_s = exp(iπs(1−Γ_H)/2); then cancellation',
    'F_θ = cos θ diag(F_H, −F_H) + sin θ J',
    'F₁ is exactly I-degenerate; HF.2–3'],navy)
box(1420,190,625,235,'Equivariant path lift',[
    'D_B / K(E) → D_I / J_I is onto',
    'Actual B-cycle path G_t, G₀ = F₀',
    '(G₁ − F₁)I is compact on both sides',
    'Whole C([0,1], E) module; HF.4'],navy)
arrow(680,310,728,310);arrow(1362,310,1410,310)
arrow(1730,425,1730,500)
box(1080,510,965,265,'The full Stinespring interval',[
    'ψ_t = (1 − t) id_B + t s q  is equivariant unital c.p.',
    'N_[0,1] = completion of B ⊙ C([0,1], B)',
    'Operator G₁ ⊕ (1 ⊗ F₁|E_I); exact diagonal group action',
    'All compact defects lie in the whole interval ideal',
    'Endpoints: z and q*w; hence z = q*w.  HF.5–6'],green)
box(55,510,965,265,'Boundary projector identity',[
    'P̃ = {±1} × (ℝ ⋉ ℝ); exact group contraction to {±1}',
    'Induction of the scalar unit is the full Q unit',
    'σ_Q(γ) = 1_Q, so γ z = q*(γ w) = q*w = z',
    'rγ = 1 by the complete negative Witten K-product',
    'Repaired projector: rL = 1,  Lr = γ·(−)',
    'Therefore z = L(rz) = 0.  RR.2–3; RP.0–8; HF.7'],green)
arrow(1080,635,1030,635)
arrow(535,775,535,855)
box(55,865,1990,255,'Finite-center descent and actual holonomy-module transport',[
    'Q_Z = (1 + U(−1))/2 extracts the center-trivial whole homotopy; G = PSU(1,1)',
    'E_A = Γ(V, P_frames ×_K E) ⊗_{C(V)⊗C([0,1])} C([0,1], A),   A = C*_r(Hol(V,F))',
    'Exact cocycle c(p,γ,q), genuine convolution representation, K-averaged bounded operator',
    'Compact arrow kernels are uniformly approximated by whole-interval rank-one fields',
    'Native p = J(x) = J(y) = 1_A.  RR.6–8 and BC.19–26'],green)
box(55,1170,1275,195,'Calibrated inverse products',[
    'δ_inv ⊗_{C(V)} T = 1_A,   T ⊗_A δ_inv = 1_{C(V)}',
    'Exact KK equalities imply both integral K-degree inverses',
    'Complete prescribed spin-c module and coefficient order'],green)
box(1370,1170,675,195,'Literal historical class retained',[
    'δ_S = −δ_inv[D]',
    'T δ_S = −[D],  D = det S = LH²',
    'The literal positive same-spin identity is refuted'],red)
txt(1050,1420,'Section 11B proof map: HF.1–HF.7, RR.2–3 and RR.6–8, RP.0–8, CL.1–27.  No numerical test supplies a proof.',24,'#444444')
im.save(out/'kt-hyperbolic-boundary-factorization.png')
svg.append('</svg>');(out/'kt-hyperbolic-boundary-factorization.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
print('Rendered exact proof diagram: kt-hyperbolic-boundary-factorization.png and .svg')

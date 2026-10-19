"""Editable diagram for the countable canonical-field construction. CC0-1.0."""
from pathlib import Path
import json
from html import escape
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"countable-cone-transport.svg"
DATA=ROOT/"countable-cone-transport.json"
data={
 "title":"Canonical transport from countable cone tests",
 "license":"CC0-1.0",
 "proof":"../../OA-FLOW-MSF.html#oa-flow.msf.constructive",
 "parameter":"A fixed x; all data and index choices are measurable in x.",
 "types":{"W_x":"H_x -> K_x","p_j":"P_x subset H_x","q_k":"Q_x subset K_x"},
 "residual":"D_jk = sup_l |<theta(b_l) q_k,q_k> - <b_l p_j,p_j>|",
 "residual_identity":"D_jk = ||omega_q_k - omega_W_x_p_j||",
 "cone_error":"D_jk < epsilon^2 implies ||q_k-W_x p_j|| < epsilon",
 "frame_choice":"a_t = sum_j r_tj p_j; ||a_t-e_i|| < 2^(-m)",
 "coefficient_sum":"R_t = sum_j |r_tj|",
 "cone_tolerance":"epsilon = 2^(-m)/(1+R_t)",
 "frame_image":"h_i,m = sum_j r_tj q_k_j",
 "frame_error":"||h_i,m-W_x e_i|| < R_t epsilon + 2^(-m) < 2^(1-m)",
 "scope":"Countable exact norm tests; no finite decision procedure is asserted.",
 "sample":{"m":3,"R_t":3,"epsilon":"1/32","cone_contribution":"3/32","source_contribution":"1/8","sum":"7/32","strict_bound":"1/4"}
}
assert Fraction(3)*Fraction(1,32)+Fraction(1,8)==Fraction(7,32)<Fraction(1,4)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900">',
 '<rect width="1440" height="900" fill="#f7f9fc"/>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#516379"/></marker></defs>']
def text(x,y,s,size=22,weight="normal",fill="#152a43"):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(s)}</text>')
def box(x,y,w,h,title,lines):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#b6c7da" stroke-width="2"/>')
 text(x+20,y+36,title,23,"bold")
 for i,line in enumerate(lines):text(x+20,y+72+i*30,line,20)
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#516379" stroke-width="2.5" fill="none"/>')
 points=f'{x2},{y2} {x2-8},{y2-5} {x2-8},{y2+5}' if y1==y2 else f'{x2},{y2} {x2-5},{y2-8} {x2+5},{y2-8}'
 parts.append(f'<polygon points="{points}" fill="#516379"/>')
text(44,53,"Canonical transport from countable cone tests",35,"bold")
text(44,91,"At each x: Wₓ : Hₓ → Kₓ.  The construction makes every frame image measurable.",23)
box(44,125,425,188,"1  Supplied measurable sections",[
 "bℓ ∈ (Mₓ)₁,  dℓ = θₓ(bℓ) ∈ (Nₓ)₁",
 "pⱼ ∈ Pₓ,  qₖ ∈ Qₓ,  both cone lists dense",
 "Wₓ exists pointwise by canonical comparison",
 "Its measurability is to be proved."])
box(507,125,425,188,"2  Countable coefficient residual",[
 "Dⱼₖ = supℓ |⟨dℓqₖ,qₖ⟩ − ⟨bℓpⱼ,pⱼ⟩|",
 "Dⱼₖ = ‖ω(qₖ) − ω(Wₓpⱼ)‖",
 "Each coefficient, then Dⱼₖ, is measurable.",
 "The full norm uses a countable dense ball."])
box(970,125,425,188,"3  Least index and cone error",[
 "Choose the least k with Dⱼₖ < ε².",
 "The level sets of this choice are measurable.",
 "CR6:  ‖qₖ − Wₓpⱼ‖² ≤ Dⱼₖ < ε²",
 "Let ε ↓ 0 to obtain measurable Wₓpⱼ."])
arrow(473,218,502,218);arrow(936,218,965,218)
box(44,366,650,182,"4  Approximate a source Hilbert-frame vector",[
 "aₜ = Σⱼ rₜⱼ pⱼ,  with rational complex coefficients",
 "Choose the least t with ‖aₜ − eᵢ‖ < 2⁻ᵐ.",
 "CR1 makes these finite combinations dense in Hₓ.",
 "Put Rₜ = Σⱼ |rₜⱼ|  and  ε = 2⁻ᵐ / (1 + Rₜ)."])
box(745,366,650,182,"5  Assemble a target frame approximation",[
 "For each term j, choose q(kⱼ) with D(j,kⱼ) < ε².",
 "hᵢ,ₘ = Σⱼ rₜⱼ q(kⱼ), pasted over the t-levels.",
 "‖hᵢ,ₘ − Wₓeᵢ‖ < Rₜ ε + 2⁻ᵐ < 2¹⁻ᵐ.",
 "Limits on the frame give measurable Wₓ and Wₓ*."])
arrow(1165,319,1165,360);arrow(700,454,739,454)
text(44,609,"The two error contributions",27,"bold")
text(44,643,"Example: m = 3, Rₜ = 3, ε = 1/32.  The triangle bound is 7/32, strictly below 1/4.",23)
parts.append('<rect x="150" y="679" width="360" height="42" fill="#1b8a83"/><rect x="510" y="679" width="480" height="42" fill="#487bc0"/>')
parts.append('<line x1="1110" y1="669" x2="1110" y2="731" stroke="#b04031" stroke-width="3" stroke-dasharray="7,5"/>')
text(206,707,"cone: 3/32",22,"bold","white");text(656,707,"source: 1/8",22,"bold","white")
text(959,757,"7/32",22,"bold");text(1085,757,"1/4",22,"bold","#b04031")
text(44,816,"Exact proof: OA-FLOW-MSF, (MSF.D1)–(MSF.D11).  Bars show bounds, not measured errors.",21)
text(44,851,"The supremum is countable; finite coefficient tests alone need not decide a least-index inequality.",21)
parts.append('</svg>')
OUT.write_text("\n".join(parts)+"\n",encoding="utf-8")
DATA.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"svg":OUT.name,"data":DATA.name,"exact_sample":"7/32 < 1/4"}))


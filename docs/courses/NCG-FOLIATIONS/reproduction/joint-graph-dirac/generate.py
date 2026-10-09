"""Original CC0 mathematical diagram; no external assets or font bytes."""
from pathlib import Path
from html import escape
import argparse, json


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output-dir', type=Path, default=Path('generated'))
    a = p.parse_args()
    a.output_dir.mkdir(parents=True, exist_ok=True)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="1000" viewBox="0 0 760 1000"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#2563eb"/></marker></defs><rect width="760" height="1000" fill="#f8fafc"/><g font-family="Arial,sans-serif" fill="#172554">']

    def text(x, y, s, size=16, color='#172554', anchor='start'):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')

    def box(x, y, w, h, fill='white'):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#cbd5e1"/>')

    def arrow(x1, y1, x2, y2):
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>')

    text(30, 38, 'Joint Dirac and its actual graph phase', 25)
    text(30, 66, 'Theorem 11BO.1 · DJ.1–DJ.33 · Exercises 297–299', 16, '#475569')
    box(26, 88, 708, 202)
    text(45, 119, 'A. One positive speed weights both leading operators', 19)
    text(45, 157, 'A = α¹ᐟ² (Dκ ⊗ 1 + Γκ ⊗ Ninv) α¹ᐟ²', 23, '#1d4ed8')
    text(45, 188, 'Dκ: compact resolvent; index +1; every label preserves its domain.', 16)
    text(45, 220, 'Local graph norm controls H¹ in all q normal directions and Dκ.', 16)
    text(45, 251, 'Finite Dκ² windows + Rellich give ordinary scalar local compacts.', 16)
    text(45, 274, 'The full inverse Spin-c line and final right Clq factor remain.', 15)
    box(26, 308, 708, 238)
    text(45, 340, 'B. Actual multiplication, agreeing domains, full graph carrier', 18)
    for x, w, label in [(45, 175, 'Transfer tensor'), (295, 170, 'Original T'), (540, 172, 'Graph E_Z')]:
        box(x, 364, w, 47, '#eff6ff')
        text(x+w/2, 394, label, 17, anchor='middle')
    arrow(225, 388, 288, 388)
    arrow(470, 388, 533, 388)
    text(249, 434, 'Ω', 20, anchor='middle')
    text(503, 434, 'W', 20, anchor='middle')
    text(45, 466, 'D_i = Σj φj V_ij Dκ V_ij⁻¹ = Dκ + K_i', 20)
    text(45, 498, 'D_i = V_il D_l V_il⁻¹, including the complete graph domains.', 16)
    text(45, 527, 'Fgraph = P (1 ⊗ F_A₀) P on the entire induced range.', 18, '#1d4ed8')
    box(26, 564, 708, 187)
    text(45, 596, 'C. The physical normal phase is tested on actual columns', 18)
    text(45, 633, 'e⁻ⁱᵗᶠ F_A₀ eⁱᵗᶠ v → Γκ i C(df) / |df| · v', 21, '#1d4ed8')
    text(45, 665, 'First prove this on the compact joint core; extend by L² density.', 16)
    text(45, 694, 'Compact creation errors vanish on the oscillating packets.', 16)
    text(45, 726, 'Original positive disk: b_U = b_V[j_VU]; scalar Bott pairing +1.', 17)
    box(26, 769, 708, 177)
    text(45, 801, 'D. Bounded compression does not imply domain preservation', 18)
    text(45, 833, 'Two copies of (0,1): α₁ = x²(1−x)², α₂ = x(1−x).', 18)
    text(45, 864, 'x_n = λ_n⁻¹ᐟ³; coefficient x_n²; bump width comparable to x_n.', 16)
    text(45, 895, 'Auxiliary norm: copy 1 ≍ x_n; copy 2 ≍ 1 (not square summable).', 16)
    text(45, 925, 'P(u₁,0) = (u₁/2,u₁/2) fails the second completed domain.', 16)
    text(30, 976, 'Exact operator/type schematic; ≍ denotes uniform two-sided estimates. CC0.', 14, '#475569')
    parts.append('</g></svg>')
    (a.output_dir/'joint-graph-dirac.svg').write_text(''.join(parts), encoding='utf-8', newline='\n')
    data = {'theorem':'11BO.1', 'proofs':['DJ.1–DJ.33'], 'weighted_expression':'alpha^(1/2)(D_kappa tensor 1 + Gamma_kappa tensor N_inv)alpha^(1/2)', 'graph_phase':'P(1 tensor F_A0)P', 'normal_phase':'Gamma_kappa i C(df)/|df|', 'auxiliary_index':1, 'original_disk_pairing':1, 'counterexample':{'domain':'(0,1)', 'alpha_1':'x^2(1-x)^2', 'alpha_2':'x(1-x)', 'x_n':'lambda_n^(-1/3)', 'coefficient':'x_n^2', 'bump_width':'comparable to x_n', 'auxiliary_norm_1':'comparable to x_n', 'auxiliary_norm_2':'comparable to 1'}, 'scope':'discrete-cocycle transfer; actual bounded physical graph phase', 'license':'CC0-1.0'}
    (a.output_dir/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'generated':True,'width':760,'height':1000}))


if __name__ == '__main__':
    main()

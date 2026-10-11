"""Reproduce the exact explanatory vector figure for OA-FLOW-EOR. CC0-1.0."""
from pathlib import Path
from html import escape

def render():
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1140" viewBox="0 0 1600 1140" role="img" aria-labelledby="title desc">', '<title id="title">A normal orbit functional forces one homogeneous space</title>', '<desc id="desc">The top chain proves that each orbit map is proper, its stabilizer compact and its orbit closed. The middle chain extends a dominated orbit functional normally and annihilates the ideal off the orbit. Ergodicity forces the ideal to vanish. The lower chain extends multiplication normally and identifies the full Haar multiplier algebra without countability assumptions.</desc>', '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#247e94"/></marker></defs>', '<rect width="1600" height="1140" fill="#f5f8fc"/>']
    def text(x,y,s,size=26,weight='normal',anchor='middle',color='#173650'):
        out.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>')
    def box(x,y,w,h,title,lines,color='#e8f2f7'):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{color}" stroke="#9bb2c6" stroke-width="2"/>')
        text(x+w/2,y+40,title,23 if w<500 else 26,'bold')
        for j,s in enumerate(lines):text(x+w/2,y+80+34*j,s,21 if w<500 else 23)
    def arrow(x,y,u,v):out.append(f'<path d="M{x},{y} L{u},{v}" fill="none" stroke="#247e94" stroke-width="3" marker-end="url(#arrow)"/>')
    text(800,56,'One proper orbit, then the complete normal algebra',36,'bold')
    text(800,96,'Arbitrary locally compact G; arbitrary nonzero abelian M; ergodic and integrable',24,color='#536e88')
    box(45,145,450,180,'Finite orbit integrals',['u(s) = h(s⁻¹y), h ≥ 0 compact','∫ u(s) ds ≤ τ(h) < ∞','Right uniform continuity ⇒ u ∈ C₀(G)'])
    box(575,145,440,180,'Proper orbit map',['pᵧ : G → X, s ↦ sy','pᵧ⁻¹(K) is compact for compact K','EO13–EO15'])
    box(1095,145,460,180,'Compact stabilizer; closed orbit',['Hᵧ = pᵧ⁻¹({y}) is compact','Gy is closed in X','No countable covering is used'])
    arrow(501,233,567,233);arrow(1022,233,1087,233)
    box(45,390,690,195,'A finite normal witness',['ρᵧ,ₕ(a) = ∫ h(s⁻¹y) a(s⁻¹y) ds','0 ≤ ρᵧ,ₕ ≤ μₕ,     μₕ(x) = τ(hx)','Domination ⇒ a nonzero normal extension to M','EO16–EO17'], '#e5f2ed')
    box(830,390,725,195,'The ideal off the closed orbit',['J = {a ∈ C₀(X) : a|Gy = 0};  I = closureᵘʷ(J) = eM','I is invariant and the normal witness annihilates I','Ergodicity: e = 0 or 1; nonzero witness excludes 1','Hence J = 0 and X = Gy ≅ G/Hᵧ'], '#e5f2ed')
    arrow(743,482,822,482)
    box(45,665,450,225,'Every multiplication coefficient',['On L²(X,ν): a ↦ multiplication by a','|f|² gives ρᵧ,|f|² for f ∈ C꜀(X)','L² approximation + polarization','give normal coefficients for all vectors','EO20–EO21'])
    box(575,665,440,225,'The faithful normal extension',['T : M → B(L²(X,ν))','T is multiplicative and equivariant','Its invariant kernel is zero','T(M) = C₀(X)″','EO21–EO24'])
    box(1095,665,460,225,'The full Haar algebra',['ν = Δ⁻¹ mG/H; identical local null sets','C₀(G/H)″ = ∏ⱼ L∞(Xⱼ)','Xⱼ are open σ-compact pieces','The bounded product may be uncountable','EO25–EO26'])
    arrow(501,776,567,776);arrow(1022,776,1087,776)
    text(800,956,'Why a global probability cannot be assumed',28,'bold')
    text(800,998,'Uncountable discrete G acting on ℓ∞(G): integrable and ergodic, H = {e}.',25)
    text(800,1034,'Every normal state has countable support, so none is faithful. The proof still applies.',24)
    text(800,1094,'Proof locators: OA-FLOW-EOR, EO13–EO26. This is a proof diagram, not a geometric embedding.',20,color='#536e88')
    out.append('</svg>')
    return '\n'.join(out)+'\n'

if __name__=='__main__':
    Path(__file__).with_name('ergodic-orbit.svg').write_text(render(),encoding='utf-8',newline='\n')

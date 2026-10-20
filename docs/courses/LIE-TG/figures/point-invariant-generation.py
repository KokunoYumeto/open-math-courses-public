"""Exact all-order invariant coordinates of Example 4.39.

GPT-6.1 Sol (OpenAI), CC0 1.0.
"""
from pathlib import Path
from html import escape
parts=[]
def text(x,y,value,size=21,**attrs):
    attrs=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {attrs}>{escape(value)}</text>')
def box(x,y,w,h,color='white'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{color}" stroke="#c4cfdd"/>')
parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1080" viewBox="0 0 1200 1080" role="img" aria-labelledby="title desc">
<title id="title">Nonlinear invariant generation with one low coefficient ring</title>
<desc id="desc">For the translation action on (1+p squared)u_xx=u_xy, p=u_x,r=u_y,q=u_xy,s=u_yy, f=1+p squared and delta=qs/f-q squared. Both f and delta are inverted in the order-two ring. The two horizontal forms have determinant delta. At order three Q1=a/q-2psq squared/(f squared delta),S1=(sa-qb)/delta with a=u_xyy,b=u_yyy, and the exact affine inverse is displayed. At every order h+2 the symbol rows of Q_h=nabla1^h q and S_h=nabla1^h s have triangular matrix with diagonal q^-h and(-q/delta)^h, determinant(-1/delta)^h. Every next quotient adds the affine plane with coordinates Q_h,S_h.</desc>
<rect width="1200" height="1080" fill="#f6f8fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
''')
text(30,39,'Nonlinear invariant generation with one low coefficient ring',26,font_weight=650)
text(30,76,'p=uₓ, r=uᵧ, q=uₓᵧ, s=uᵧᵧ;   f=1+p²,   δ=qs/f−q²;   f ≠ 0 and δ ≠ 0.',21)
box(25,104,1150,177)
text(47,143,'Order two: B = K[p,r,q,s,f⁻¹,δ⁻¹] and F₂ = K(p,r,q,s)',24,font_weight=600)
text(48,186,'dₕp=(q/f)dx+q dy;    dₕr=q dx+s dy.    Their determinant is δ.',23)
text(48,229,'∇₁=(sDₓ−qDᵧ)/δ;    ∇₂=(−qDₓ+(q/f)Dᵧ)/δ;    [∇₁,∇₂]=0.',23)
text(48,263,'The two inverses f⁻¹ and δ⁻¹ remain in the low ring throughout.',20,fill='#174880')
box(25,302,560,247,'#edf2fc');box(615,302,560,247,'#eaf4ed')
text(47,341,'Order three: (a,b) → (Q₁,S₁)',23,font_weight=600)
text(47,380,'a=uₓᵧᵧ,   b=uᵧᵧᵧ',22)
text(47,424,'Q₁=a/q−2psq²/(f²δ)',23)
text(47,467,'S₁=(sa−qb)/δ',23)
text(47,516,'det = −1/δ; every pair is allowed.',21)
text(637,341,'The exact affine inverse',23,font_weight=600)
text(637,400,'a=qQ₁+2psq³/(f²δ)',23)
text(637,447,'b=sQ₁−(δ/q)S₁+2ps²q²/(f²δ)',22)
text(637,501,'No inverse of a higher coordinate occurs.',20)
box(25,570,1150,276)
text(47,609,'Every order h+2: Qₕ=∇₁ʰq,  Sₕ=∇₁ʰs,  h ≥ 0',24,font_weight=600)
text(48,653,'Standard symbol basis: (tₓtᵧʰ⁺¹, tᵧʰ⁺²).  The two rows are triangular:',22)
parts.append('<path d="M170 677H155V770H170M530 677H545V770H530" fill="none" stroke="#17283d" stroke-width="2"/>')
text(235,709,'q⁻ʰ',29,text_anchor='middle');text(420,709,'0',29,text_anchor='middle')
text(235,752,'Cₕ',29,text_anchor='middle');text(420,752,'(−q/δ)ʰ',29,text_anchor='middle')
text(672,723,'det = (−1/δ)ʰ ≠ 0',31,fill='#2c6547')
text(48,797,'Cₕ = f[(s/f−q)ʰ−(−q)ʰ]/δʰ.  The binomial proof gives all h, not a finite sample.',21)
text(48,829,'Actual inverse affine changes give independent polynomial coordinates in every degree.',20)
box(25,868,1150,187)
text(47,906,'The geometric quotient tower',24,font_weight=600)
text(48,950,'X₂ ← X₃ ← X₄ ← ⋯ ;  each step forgets its newest pair (Qₕ,Sₕ).',25)
text(48,993,'O(Xⱼ)=B[Q₁,S₁,…,Qⱼ₋₂,Sⱼ₋₂];  invariant algebra: F₂[Qₕ,Sₕ : h≥1].',23)
text(48,1031,'Translation isotropy is {id}; each fixed-basic-point Xⱼ is its own geometric quotient.',20)
parts.append('</g></svg>')
svg='\n'.join(parts)+'\n'
if __name__=='__main__':
    Path(__file__).with_suffix('.svg').write_text(svg,encoding='utf-8',newline='\n')

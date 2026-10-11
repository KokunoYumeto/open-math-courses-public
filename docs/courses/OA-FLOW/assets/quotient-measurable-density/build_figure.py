"""Exact step densities for translation by one in the affine quotient."""
from pathlib import Path
from html import escape


def build_svg():
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="700" viewBox="0 0 1160 700" role="img" aria-labelledby="title desc">',
           '<title id="title">Discontinuous density and inverse translation conventions</title>',
           '<desc id="desc">Beta is one on the negative half line and two otherwise. For translation by one, the pullback density is two on minus one inclusive to zero exclusive. The pushforward density is one half on zero inclusive to one exclusive. Both are one elsewhere.</desc>',
           '<rect width="1160" height="700" fill="#f8fafc"/>']
    def text(x,y,s,size=19,weight=400,anchor="start"):
        out.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="#172033">{escape(s)}</text>')
    text(32,43,"A jump in the quotient density",28,700)
    text(32,77,"Exact model: G/H = ℝ,   dμ(t) = β(t) dt,   T(t) = t + 1",21)
    def panel(top,title,pieces,endpoints,color,notes):
        out.append(f'<rect x="24" y="{top}" width="1112" height="168" rx="12" fill="white" stroke="#cbd5e1"/>')
        text(42,top+28,title,21,700)
        def x(t): return 335+123*t
        def y(v): return top+129-35*v
        out.append(f'<path d="M{ x(-2.15) },{ y(0) } H{ x(2.15) } M{ x(0) },{ y(0) } V{ y(2.25) }" fill="none" stroke="#64748b"/>')
        for tick in [-2,-1,0,1,2]:
            out.append(f'<path d="M{x(tick)},{y(0)-4} V{y(0)+4}" stroke="#64748b"/>')
            text(x(tick),y(0)+22,str(tick),16,anchor="middle")
        text(x(2.25),y(0)+5,"t",17)
        for v in [0.5,1,2]:
            text(x(-2.33),y(v)+5,str(v).replace("0.5","½"),15,anchor="end")
        for left,right,value in pieces:
            out.append(f'<path d="M{x(left)},{y(value)} H{x(right)}" fill="none" stroke="{color}" stroke-width="4"/>')
        for t,v,closed in endpoints:
            fill=color if closed else "white"
            out.append(f'<circle cx="{x(t)}" cy="{y(v)}" r="5" fill="{fill}" stroke="{color}" stroke-width="2"/>')
        for j,note in enumerate(notes):text(678,top+51+j*32,note,19)
    panel(101,"The quotient density β",[(-2,0,1),(0,2,2)],[(0,1,False),(0,2,True)],"#0f766e",
          ["β(t) = 1 for t < 0;  β(t) = 2 for t ≥ 0", "Upstairs: φ(a,t) = a β(t)", "Downstairs: dμ(t) = β(t) dt"])
    panel(280,"Pullback on sets: E ↦ μ(T E)",[(-2,-1,1),(-1,0,2),(0,2,1)],[(-1,1,False),(-1,2,True),(0,2,False),(0,1,True)],"#b45309",
          ["d(μ ∘ T) / dμ (t) = β(t + 1) / β(t)", "Value 2 on [−1, 0)", "Value 1 everywhere else"])
    panel(459,"Pushforward: E ↦ μ(T⁻¹ E)",[(-2,0,1),(0,1,0.5),(1,2,1)],[(0,1,False),(0,0.5,True),(1,0.5,False),(1,1,True)],"#7c3aed",
          ["d(T* μ) / dμ (t) = β(t − 1) / β(t)", "Value ½ on [0, 1)", "Value 1 everywhere else"])
    text(32,657,"Filled endpoints are included. Horizontal pieces continue beyond the displayed window.",18)
    text(32,682,"Proof: OA-FLOW-L43, QM2–QM10. Translation changes both the argument and the density ratio.",17)
    out.append('</svg>')
    return '\n'.join(out)+'\n'


if __name__ == '__main__':
    Path(__file__).with_name('quotient-measurable-density.svg').write_text(build_svg(),encoding='utf-8',newline='\n')

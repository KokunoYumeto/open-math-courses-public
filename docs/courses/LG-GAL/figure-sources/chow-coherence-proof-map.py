"""Reproduce the Chow geometry proof map with Python 3, Pillow and fontTools.

All arrows are sheaf/module maps or proof implications; no geometric scale
is represented. The full argument and assumptions are in CG1--CG10 and CS8.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 2600, 3330
OUT = Path(__file__).resolve().parents[1] / 'assets/chow-coherence-proof-map.png'
REGULAR = (Path('C:/Windows/Fonts/seguisym.ttf'),
           Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
BOLD = (Path('C:/Windows/Fonts/segoeuib.ttf'),
        Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
INK, MUTED = '#192c45', '#40536c'
BLUE, TEAL, PURPLE, ORANGE = '#225c95', '#076b6c', '#674392', '#97531e'


def render():
    reg = next((p for p in REGULAR if p.is_file()), None)
    bold = next((p for p in BOLD if p.is_file()), None)
    if reg is None or bold is None:
        raise RuntimeError('Segoe UI Symbol/Segoe UI Bold or DejaVu Sans required.')
    image = Image.new('RGB', (W, H), '#f5f8fc')
    draw = ImageDraw.Draw(image)
    seen = []

    def font(size, strong=False):
        return ImageFont.truetype(str(bold if strong else reg), size)

    def text(x, y, value, size=40, color=INK, strong=False):
        seen.append((value, strong))
        draw.text((x,y), value, font=font(size,strong), fill=color)

    def lines(values, x, y, right, bottom, size=40, step=56, color=INK):
        f = font(size)
        for value in values:
            words = value.split(' ')
            current = ''
            for word in words:
                candidate = word if not current else current+' '+word
                if current and draw.textlength(candidate,font=f)>right-x:
                    assert y+size<=bottom, ('panel overflow',value)
                    text(x,y,current,size,color); y+=step; current=word
                else: current=candidate
            assert draw.textlength(current,font=f)<=right-x, ('unbreakable line',value)
            assert y+size<=bottom, ('panel overflow',value)
            text(x,y,current,size,color);y+=step
        return y

    def panel(y,height,title,locator,color):
        draw.rounded_rectangle((95,y,2505,y+height),radius=22,fill='white',outline='#cad6e4',width=3)
        draw.rounded_rectangle((95,y,117,y+height),radius=10,fill=color)
        text(150,y+23,title,48,color,True)
        assert draw.textlength(title,font=font(48,True))<2200
        text(150,y+85,locator,34,MUTED)
        return 150,y+137,2450,y+height-20

    def arrow(x1,y1,x2,y2,color=BLUE,width=5):
        import math
        draw.line((x1,y1,x2,y2),fill=color,width=width)
        a=math.atan2(y2-y1,x2-x1);length=19;half=10
        points=[(x2,y2),(x2-length*math.cos(a)+half*math.sin(a),y2-length*math.sin(a)-half*math.cos(a)),
                (x2-length*math.cos(a)-half*math.sin(a),y2-length*math.sin(a)+half*math.cos(a))]
        draw.polygon(points,fill=color)

    text(95,52,'Chow modification: the actual graphs and the common twist',59,BLUE,True)
    text(95,140,'R Noetherian; X/R separated and of finite type. Properness is added in panels 4–6.',38)
    text(95,200,'Module generators, quotient ideals and pullback frames retain the stated scheme structure.',35,MUTED)

    box=panel(265,390,'1. An affine cover with explicit algebra generators','CG1; CG1a–CG1b',BLUE)
    lines(['Start with a finite affine cover V_l = Spec C_l and finite R-generators.',
           'For a missing generic point η, take η ∈ D(f) ⊆ V_k \\ closure(V).',
           'Its ring (C_k)_f adds the generator f^(-1); adjoin this disjoint piece.',
           'For B_i = ∏ E_t, use factor idempotents e_t and embedded generators.',
           '(b_1,…,b_s) = Σ e_t p_t(embedded generators of E_t).',
           'Each U_i = Spec B_i contains all generics; U = ∩ U_i is dense.'],*box,size=39,step=38)

    box=panel(675,375,'2. Close the graph with the projection to X already present','CG2–CG4; CG2–CG4',TEAL)
    lines(['j_i: U_i ↪ A_i = D_+(T_i0) ⊆ P_i;  P = ∏ P_i.',
           "X′ = schematic closure of {(u,j(u)) : u ∈ U} in X ×_R P.",
           "π = pr_X|X′;  q = pr_P|X′.  π^(-1)U → U is an isomorphism.",
           'The closure is defined by ker(O → j_*O_U) on finite affine charts.',
           'It retains every nilpotent over U; boundary structure need not survive.',
           'The proper projection π has closed image containing dense U, hence is onto.'],*box,size=39,step=35)

    box=panel(1070,420,'3. TWO ideal containments identify the open subschemes','CG4; CG5–CG6',PURPLE)
    lines(['T_i = A_i ×_R ∏_(k≠i) P_k.',
           'On X ×_R T_i: the closed graph of U_i → X uses separated X/R,',
           'then j_i is closed; the closure kernel contains its defining ideal.',
           'Thus q^(-1)T_i ⊆ π^(-1)U_i, with the actual scheme factorization.',
           'On U_i ×_R P: the graph of U_i → P_i uses separated P_i/R.',
           'The closure kernel contains this graph ideal, giving the reverse inclusion.',
           'Hence q^(-1)T_i = π^(-1)U_i as open subschemes.'],*box,size=39,step=35)

    box=panel(1510,540,'4. Proper X gives both closed projective maps and one L','CG3–CG5; CG6–CG7',BLUE)
    lines(['The two local closed immersions of CG6 make q closed into ∪ T_i.',
           'If X/R is proper, q is proper by its closed graph; q(X′) is closed.',
           'The opens ∪ T_i and P \\ q(X′) make q globally closed. Segre gives h.'],*box,size=39,step=39)
    y=1786
    text(310,y,"X′",45,BLUE);text(1800,y,'P_R^N',45,BLUE)
    arrow(520,y+29,1690,y+29,BLUE);text(1080,y-20,'h closed',35,MUTED)
    arrow(350,y+63,350,y+125,BLUE);text(410,y+66,'π proper, onto',34,MUTED)
    text(310,y+143,'X',45,BLUE);text(1710,y+143,'Spec R',45,BLUE)
    arrow(520,y+173,1610,y+173,BLUE)
    text(150,1990,"Also (π,h): X′ ↪ P_X^N is closed, with L = h*O(1) ≅ (π,h)*O(1).",37)

    box=panel(2070,430,'5. Projective finiteness supplies a common exponent','PF8–PF9; CG6–CG8; CG8–CG12',TEAL)
    lines(['Apply the construction to integral closed Z ⊆ X. Then Z′ is integral.',
           "Both π: Z′ → Z and g′: Z′ → Spec R are projective with the same L.",
           'Their hyperplane frames are identical pullbacks of the Segre frames.',
           'Choose a ≥ 0 past both projective higher-image vanishing thresholds.',
           'R^q π_*L^a = 0 and R^q g′_*L^a = 0 for q>0.',
           'G_Z = π_*L^a is coherent, with full support Z and generic rank one.',
           'SC15 gives H^p(Z,G_Z) ≅ H^p(Z′,L^a), finite over R.'],*box,size=39,step=35)

    box=panel(2520,480,'6. The witness fits CS8; proper coherent finiteness follows','CG8–CG10; CS8; CG11–CG14',ORANGE)
    lines(['For i: Z ↪ X put W_Z = i_*G_Z. Its generic maximal ideal acts by zero.',
           'Its cohomology equals that on Z by exact closed-immersion pushforward.',
           'Let P(F) mean: every H^q(X,F) is finite over R.',
           'P(0) holds. The positive long exact sequence proves two out of three,',
           'including the left-sheaf degree-zero injection into H^0(X,F_middle).',
           'CS8, with both ideal comparisons and all nilpotent layers, proves P(F).',
           'For proper f: X → S with S locally Noetherian, apply this on each affine.',
           'SC14 identifies R^q f_*F on every affine target with the associated',
           'finite cohomology module; AS7 makes each higher image coherent.'],*box,size=39,step=35)

    text(95,3053,'Diagram arrows are the stated morphisms, not a model of scheme dimensions.',36,MUTED)
    text(95,3108,'Proofs: CG1–CG10, PF1–PF9, SC14–SC15 and CS0–CS8.',36,MUTED)
    text(95,3163,'Free comparisons: Stacks 0200, 0201, 01R8, 01RG, 01W6 and 01WD.',36,MUTED)
    text(95,3218,'Universal finiteness is the conclusion; it is not used to produce its projective witness.',35,MUTED)
    from fontTools.ttLib import TTFont
    cmaps={False:TTFont(reg).getBestCmap(),True:TTFont(bold).getBestCmap()}
    absent={(ch,strong) for value,strong in seen for ch in value if ord(ch)>127 and ord(ch) not in cmaps[strong]}
    assert not absent, ('missing mathematical glyphs',absent)
    image.save(OUT)
    print(f'{OUT.name}: {W} x {H} RGB')


if __name__ == '__main__':
    render()

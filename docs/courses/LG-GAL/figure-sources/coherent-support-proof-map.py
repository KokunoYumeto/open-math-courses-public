"""Reproduce the coherent-support proof map with Python 3, Pillow and fontTools.

All arrows are sheaf/module maps or proof implications; no geometric scale
is represented. The full argument and assumptions are in CS0--CS8.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 2600, 3780
OUT = Path(__file__).resolve().parents[1] / 'assets/coherent-support-proof-map.png'
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

    text(95,52,'Coherent support: keep the actual source and every layer',61,BLUE,True)
    text(95,139,'X Noetherian; J a coherent ideal; E and F coherent; U = X \\ V(J).',41)
    text(95,199,'Local proof map for Sections 0.C.4.0–0.C.4.8 (CS0–CS8).',36,MUTED)

    box=panel(265,325,'1. Uniform support powers and Artin–Rees','CS0–CS2; CSFR1–CSFR4',BLUE)
    lines(['Supp M ⊆ V(J)  ⇒  J^a M = 0 for some a ≥ 1.',
           'For a finite submodule N ⊆ M, the Rees submodule is finite.',
           'J^n M ∩ N = J^(n−c)(J^c M ∩ N),  n ≥ c.',
           'A finite affine cover supplies a common exponent and index.'],*box,size=40,step=42)

    box=panel(608,388,'2. Clean torsion, then take an ideal preimage','CS3; CSFR5–CSFR6',TEAL)
    lines(['T = F[J^a] stabilized; choose c by Artin–Rees.',
           'F_clean = J^(a+c) F;  F_clean ∩ T = 0.',
           'F_clean ↪ j_*(F_clean|U),  j: U ↪ X.',
           's defines h: O_X → j_*(F_clean|U).',
           'L = ker(O_X → j_*(F_clean|U) / F_clean).',
           'L|U = O_U ⇒ J^b ⊆ L; hence J^b → F extends s.'],*box,size=40,step=38)

    box=panel(1014,350,'3. The ordinary tensor product has a real kernel','CS4; CSFR7',PURPLE)
    lines(['A = J^b ⊗ E;   v: A → F by evaluation in Hom(E,F).',
           'μ: A ↠ J^b E;   ker μ need not be zero.',
           'If k = Σ a_i ⊗ e_i and Σ a_i e_i = 0, then for r ∈ J^b:',
           'r k = Σ r ⊗ a_i e_i = r ⊗ (Σ a_i e_i) = 0.',
           'Thus J^b ker μ = 0. Coherence is used; flatness is not.'],*box,size=40,step=38)

    box=panel(1382,505,'4. Remove the kernel before returning to the source','CS4; CSFR8–CSFR10',PURPLE)
    lines(['For an Artin–Rees index d, set m = b+d.',
           'J^m A ∩ ker μ ⊆ J^b ker μ = 0.'],*box,size=40,step=43)
    y=1628
    text(290,y,'J^m A',45,PURPLE);text(1845,y,'F',45,PURPLE)
    arrow(640,y+31,1760,y+31,PURPLE);text(1040,y-18,'v restricted',35,MUTED)
    arrow(426,y+62,426,y+129,PURPLE);text(490,y+72,'μ isomorphism',34,MUTED)
    text(250,y+141,'J^(m+b) E',45,PURPLE);text(1845,y+141,'F',45,PURPLE)
    arrow(670,y+172,1760,y+172,PURPLE);text(1030,y+116,'transported map',35,MUTED)
    arrow(1870,y+62,1870,y+129,PURPLE);text(1920,y+70,'identity',34,MUTED)
    text(150,1825,'Both routes agree. On U the lower map is ψ: E|U → F|U.',37)

    box=panel(1905,350,'5. Quotient-ring descent and an injective generic lattice','CS5; CSFR11',TEAL)
    lines(['Z integral closed; η generic; m_(X,η) F_η = 0.',
           'B = F[J_Z] = i_*G, with the actual O_Z = O_X/J_Z action.',
           'A basis over κ(η), then CS4, gives i_*(I^⊕r) ↪ F.',
           'The map is an isomorphism near η; domain fractions prove injection.',
           'I is a nonzero coherent ideal. If r=0, the source is zero.'],*box,size=39,step=38)

    box=panel(2273,375,'6. Split supports; retain the complete nilpotent filtration','CS6–CS7; CSFR12–CSFR13',ORANGE)
    lines(['Supp F = W1 ∪ W2:  0 → J^e F → F → F/J^e F → 0.',
           'For J = J_W1, the two end supports lie in W2 and W1.',
           'Irreducible W:  0 = J^e F ⊆ J^(e−1) F ⊆ ··· ⊆ J F ⊆ F.',
           'Every layer J^q F / J^(q+1) F is killed by J_W.',
           'Generic lattices and closed-support induction give a finite',
           'filtration by i_*I. No layer is discarded and no dimension bound is used.'],*box,size=39,step=35)

    box=panel(2666,495,'7. One rank-one witness and BOTH ideal comparisons','CS8; CSFR14–CSFR17',BLUE)
    lines(['P is invariant under isomorphism, holds for zero, and has two out of three.',
           'For every integral closed Z, the coherent witness W_Z has full support,',
           'm_(X,η)(W_Z)_η = 0, generic rank one, and P(W_Z).',
           'At a minimal counterexample support W:',
           '0 → i_*I0 → W_Z → C0 → 0,   Supp C0 ⊊ W.',
           'K = I ∩ I0 ≠ 0; both quotient supports below are proper in W.',
           '0 → i_*K → i_*I0 → i_*(I0/K) → 0.',
           '0 → i_*K → i_*I   → i_*(I/K)   → 0.',
           'P(i_*I0) ⇒ P(i_*K) ⇒ P(i_*I); CS7 then proves P(F).'],*box,size=39,step=37)

    box=panel(3179,330,'8. Check the two distinctions on explicit rings','Exercise 6.20; full solution follows the section',ORANGE)
    lines(['A = k[x], J=(x), E=A/(x):  J ⊗ E ≅ E, but J E = 0.',
           'Its multiplication kernel is all of E; J kills that kernel.',
           'B = k[x,ε]/(ε²):  0 ⊂ εk[x] ⊂ B.',
           'Both factors are k[x] over B/(ε), while ε·1 remains nonzero in B.'],*box,size=40,step=43)

    text(95,3553,'Solid arrows show the stated module maps; boxes display the proved mechanisms.',35,MUTED)
    text(95,3605,'Free comparisons: Stacks 01Y8–01YI. Exact statements and proofs: CS0–CS8.',35,MUTED)
    text(95,3657,'Witness existence comes from the projective construction; CS8 states its hypotheses.',35,MUTED)
    # Verify every rendered non-ASCII glyph against the selected native font.
    # This guards the arrows/signs themselves, rather than replacing visual QA.
    from fontTools.ttLib import TTFont
    cmaps={False:TTFont(reg).getBestCmap(),True:TTFont(bold).getBestCmap()}
    absent={(ch,strong) for value,strong in seen for ch in value if ord(ch)>127 and ord(ch) not in cmaps[strong]}
    assert not absent, ('missing mathematical glyphs',absent)
    image.save(OUT)
    print(f'{OUT.name}: {W} x {H} RGB')


if __name__ == '__main__':
    render()

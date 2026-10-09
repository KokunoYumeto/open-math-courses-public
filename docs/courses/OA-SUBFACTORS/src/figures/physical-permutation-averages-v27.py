"""CC0: exact finite checks and a reproducible schematic for PU.1--PU.20.

The finite checks reproduce the physical product probabilities and conditional
matrix calculations. They supplement the written proof; they do not verify the
unrestricted strongly amenable subfactor theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def bits(n):
    return list(product((0, 1), repeat=n))

def probability(word, p, q):
    return p ** (len(word)-sum(word)) * q ** sum(word)

def raw_monomial(word, positions, q):
    out = F(1)
    for i in positions:
        out *= word[i]-q
    return out

def compressed_count_matrix(l, m, p, q):
    words = bits(l)
    matrix = []
    for target in words:
        row = []
        for source in words:
            value = F(0)
            for k in range(m-l+1):
                total = sum(target)+k
                tail_mass = F(choose(m-l, k))*q**k*p**(m-l-k)
                fiber_mass = F(choose(m-l, total-sum(source)), choose(m, total))
                value += tail_mass * fiber_mass
            row.append(value)
        matrix.append(row)
    return words, matrix

def act(matrix, vector):
    return [sum((a*b for a,b in zip(row, vector)), F(0)) for row in matrix]

def exact_checks():
    checked = []
    p, q = F(1,4), F(3,4)
    lam = p*q
    for l in range(1,5):
        for m in range(l,7):
            words, k = compressed_count_matrix(l,m,p,q)
            assert all(sum(row, F(0)) == 1 for row in k)
            weights = [probability(w,p,q) for w in words]
            for i in range(len(words)):
                for j in range(len(words)):
                    assert weights[i]*k[i][j] == weights[j]*k[j][i]
            for r in range(l+1):
                level = list(combinations(range(l), r))
                symmetric = [sum((raw_monomial(w,J,q) for J in level), F(0)) for w in words]
                eigenvalue = F(choose(l,r), choose(m,r))
                assert act(k, symmetric) == [eigenvalue*x for x in symmetric]
                for I in level:
                    monomial = [raw_monomial(w,I,q) for w in words]
                    expected = [x/F(choose(m,r)) for x in symmetric]
                    assert act(k, monomial) == expected
            checked.append({"l":l,"m":m,"norm_on_centered_space":str(F(l,m)),
                "gap":str(1-F(l,m)),"symmetric_eigenvalues":[str(F(choose(l,r),choose(m,r))) for r in range(l+1)]})

    cup = []
    for m in range(1,7):
        variance = F(0)
        for site0 in (0,1):
            left_mass = p if site0 == 0 else q
            z = p if site0 == 0 else -q
            for w in bits(m):
                delta = z * F(sum(w)-m*q, m)
                variance += left_mass*probability(w,p,q)*delta*delta
        assert variance == lam*(1-3*lam)/m
        cup.append({"m":m,"physical_cup_variance":str(variance)})

    h_norm2 = lam*(1-3*lam)
    assert h_norm2 == F(21,256)
    commutator_norm2 = h_norm2/F(4)
    assert commutator_norm2 == F(21,1024)
    _, k12 = compressed_count_matrix(1,2,p,q)
    zvec = [-q, p]
    assert act(k12,zvec) == [x/F(2) for x in zvec]
    assert act(k12,act(k12,zvec)) == [x/F(4) for x in zvec]
    # Intended negative control: finite compression is not an expectation.
    nonprojection_detected = act(k12,act(k12,zvec)) != act(k12,zvec)
    assert nonprojection_detected
    result = {"scope":"Exact finite checks for the existing weighted-spin inclusion; no arbitrary-inclusion conclusion.",
        "parameter":{"p":str(p),"q":str(q),"lambda":str(lam),"index":str(1/lam)},
        "compressed_count_checks":checked,"cup_variances":cup,
        "finite_noncommutation":{"l":1,"m":2,"eigenvalue":"1/2","h_norm_squared":str(h_norm2),
            "commutator_norm_squared":str(commutator_norm2),"intended_nonprojection_control_detected":nonprojection_detected},
        "proof_locators":["PU.10--PU.14","PU.16--PU.20"],"license":"CC0-1.0"}
    (HERE/'physical-permutation-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

def figure():
    from PIL import Image, ImageDraw, ImageFont
    width,height = 1440,1130
    white,navy,blue,green,red,grey = '#ffffff','#17324a','#255bb1','#1a6a48','#a34434','#526271'
    im=Image.new('RGB',(width,height),white)
    dr=ImageDraw.Draw(im)
    fontroot=Path('C:/Windows/Fonts')
    def font(size,bold=False):
        return ImageFont.truetype(str(fontroot/('arialbd.ttf' if bold else 'seguisym.ttf')),size)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<title>Exact physical permutation averaging in the weighted-spin tower</title>',
        '<desc>Schematic physical algebra maps and exact compressed eigenvalues; finite expectations have a nonzero commutator, while all fixed-depth limits give the original bicommutant in this model.</desc>',
        f'<rect width="{width}" height="{height}" fill="white"/>']
    import html
    def text(x,y,value,size=25,color=navy,bold=False):
        dr.text((x,y),value,fill=color,font=font(size,bold))
        svg.append(f'<text x="{x}" y="{y+size}" font-family="Segoe UI Symbol,Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{html.escape(value)}</text>')
    def rect(x,y,w,h,fill,stroke=blue):
        dr.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=fill,outline=stroke,width=2)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    def line(x1,y1,x2,y2,color=grey,width=3):
        dr.line((x1,y1,x2,y2),fill=color,width=width)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
    text(42,27,'Physical count averaging: exact depth control and a finite obstruction',33,bold=True)
    text(42,74,'Same weighted-spin inclusion, normalized tower trace, ordinary Jones cups. Proofs PU.1–PU.20.',23)
    rect(42,124,1356,229,'#eef5ff')
    text(65,143,'Actual right coordinates and their containing algebras',27,bold=True)
    text(65,189,'M ⊂ M_l ⊂ M_m ⊂ T       B_m = M′ ∩ M_m = equal-count matrix blocks',26)
    text(65,231,'Y_1, …, Y_m independent Bernoulli(q);   S_m = Y_1 + … + Y_m',26)
    text(65,273,'Q_m(a f) = a E(f | S_m),   a ∈ M;   diagonal averaging first removes off-diagonal words.',23)
    text(65,311,'The permutation matrices lie in the actual B_m; all averages preserve the physical trace.',22,color=grey)
    rect(42,381,654,319,'#effaf3',green)
    text(65,400,'Entire depth-l stage: exact compressed spectrum',25,color=green,bold=True)
    text(65,447,'K_l,m = E_M_l Q_m on L²(M_l)',27)
    text(65,490,'Degree r:  α_r = binom(l,r) / binom(m,r)',25)
    text(65,533,'Largest centered eigenvalue = l/m',28,bold=True)
    text(65,578,'Gap = 1 − l/m;   m ≥ 2l gives gap ≥ 1/2.',26)
    text(65,623,'For fixed l, m → ∞: K_l,m → E_M.',25)
    text(65,664,'Consequently (M′ ∩ T)′ ∩ T = M in this model.',23,color=green)
    rect(730,381,668,319,'#fff3ec',red)
    text(753,400,'Actual finite expectations do not commute',25,color=red,bold=True)
    text(753,447,'p = 1/4, q = 3/4;  d = 16/3, λ = 3/16',26)
    text(753,490,'h = (p P_0 − q P_1)(Y_1 − q)',25)
    text(753,533,'K_1,2 h = h/2,   K_1,2² h = h/4',28,bold=True)
    text(753,578,'‖[E_M_1, Q_2] h‖₂² = 21/1024 > 0',27,color=red)
    text(753,623,'Finite compression is not a projection.',25)
    text(753,664,'This does not contradict the scalar limit.',23,color=grey)
    rect(42,730,1356,147,'#f3f7fb')
    text(65,751,'Ordinary cup, exact original trace',26,bold=True)
    text(65,793,'Q_m(e_0) = λ1 + (pP_0 − qP_1) m⁻¹ Σ_i(Y_i − q)',27)
    text(65,839,'v_0,m = λ(1 − 3λ)/m = 21/(256m) at p = 1/4.  Every fixed cup has variance → 0.',24)
    rect(42,904,1356,146,'#fff8e8','#9c702e')
    text(65,925,'Unrestricted boundary retained',27,color='#885d21',bold=True)
    text(65,970,'General strong amenability / generating tunnels have not supplied these physical site permutations.',24)
    text(65,1010,'No general bicommutant proof or original-theorem counterexample is claimed by this calculation.',23)
    text(42,1077,'All boxes are schematic; all displayed constants are proved. CC0 source: physical-permutation-checks-and-figure.py.',20,color=grey)
    svg.append('</svg>')
    (HERE/'physical-permutation-averages-v27.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
    im.save(HERE/'physical-permutation-averages-v27.png')

if __name__=='__main__':
    result=exact_checks()
    figure()
    print(json.dumps({"finite_pairs_checked":len(result['compressed_count_checks']),
        "cup_depths_checked":len(result['cup_variances']),"negative_control_detected":True,
        "scope":result['scope']}))

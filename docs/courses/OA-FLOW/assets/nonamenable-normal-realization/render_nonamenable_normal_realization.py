"""Deterministic explanatory SVG and exact integer phase checks.

Only --write writes the one adjacent SVG. --check is read-only.
No imports beyond the Python standard library; no raster, cache or network.
The finite arithmetic checks are diagnostics, not proofs of the theorem.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
if sys.flags.optimize:
    raise RuntimeError("Optimized execution would omit required checks")
import argparse
from fractions import Fraction
import hashlib
from html import escape
import json
import itertools
import xml.etree.ElementTree as ET

HERE=Path(__file__).resolve().parent
TARGET=HERE/"nonamenable-normal-realization.svg"
IDENTITY=(1,0,0,1)
E=((0,0),IDENTITY)


def mv(matrix,vector):
    a,b,c,d=matrix;x,y=vector
    return (a*x+b*y,c*x+d*y)


def mm(first,second):
    a,b,c,d=first;e,f,g,h=second
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)


def inv_matrix(matrix):
    a,b,c,d=matrix
    assert a*d-b*c==1
    return (d,-b,-c,a)


def mul(first,second):
    v,A=first;w,B=second
    Aw=mv(A,w)
    return ((v[0]+Aw[0],v[1]+Aw[1]),mm(A,B))


def inv(element):
    v,A=element;Ai=inv_matrix(A);w=mv(Ai,v)
    return ((-w[0],-w[1]),Ai)


def conjugate_inverse(n,g):
    return mul(mul(inv(g),n),g)


def wedge(v,w):
    return v[0]*w[1]-v[1]*w[0]


def mu_exponent(n,m):
    return wedge(n[0],mv(n[1],m[0]))


def lambda_exponent(n,g):
    return mu_exponent(g,conjugate_inverse(n,g))-mu_exponent(n,g)


def finite_matrix_model():
    # Actual unital F=M2 tensor I3 + M3 tensor I4 inside M18.
    # H=L2(M18,Tr/18) has dimension324; its F subspace has dimension13.
    size=18
    X=[[Fraction((3*i+5*j)%17-8,11) for j in range(size)] for i in range(size)]
    def product(A,B):
        columns=list(zip(*B))
        return [[sum((a*b for a,b in zip(row,col) if a and b),Fraction(0)) for col in columns] for row in A]
    def norm2(A):
        return sum((v*v for row in A for v in row),Fraction(0))/size
    def weighted_left_norm2(A):
        result=Fraction(0)
        for dimension,multiplicity,offset in [(2,3,0),(3,4,6)]:
            trace_weight=Fraction(dimension*multiplicity,size)
            eigenvalue_squared=trace_weight/(dimension**2)
            basis_normalization_squared=dimension/trace_weight
            for r in range(dimension):
                for s in range(dimension):
                    unit=[[Fraction(0) for _ in range(size)] for _ in range(size)]
                    for t in range(multiplicity):
                        unit[offset+r*multiplicity+t][offset+s*multiplicity+t]=Fraction(1)
                    result+=eigenvalue_squared*basis_normalization_squared*norm2(product(A,unit))
        return result
    left=weighted_left_norm2(X)
    right=weighted_left_norm2(list(map(list,zip(*X))))
    expected=norm2(X)
    assert left==right==expected
    p1=[[Fraction(int(i==j and i<6)) for j in range(size)] for i in range(size)]
    assert weighted_left_norm2(p1)==Fraction(1,3)
    # A normalized but unweighted projection gets this same p1 test wrong.
    wrong=Fraction(4,13)
    assert wrong!=norm2(p1)==Fraction(1,3)
    return {"ambient_matrix_dimension":size,"trace_Hilbert_dimension":324,"finite_algebra_dimension":13,
            "blocks_and_multiplicities":[[2,3],[3,4]],"trace_weights":["1/3","2/3"],
            "actual_dense_matrix_tau_XstarX":str(expected),"actual_weighted_left_HS_norm_squared":str(left),
            "actual_weighted_right_HS_norm_squared":str(right),"normalized_unweighted_projection_wrong_p1_value":str(wrong),
            "correct_p1_value":"1/3","arithmetic":"exact Fraction matrix multiplication, no rounded square roots"}


def arithmetic_checks():
    matrices=[IDENTITY,(1,1,0,1),(1,0,1,1),(1,-1,0,1),(1,0,-1,1),
              (1,2,0,1),(1,0,2,1)]
    vectors=[(0,0),(1,0),(0,1),(1,1),(-1,2)]
    elements=list(itertools.product(vectors,matrices))
    assert len(elements)==35
    cocycle=action=compatibility=0
    for n,m,g in itertools.product(elements,repeat=3):
        assert mul(mul(n,m),g)==mul(n,mul(m,g))
        assert mu_exponent(n,m)+mu_exponent(mul(n,m),g)==mu_exponent(n,mul(m,g))+mu_exponent(m,g)
        cocycle+=1
        assert lambda_exponent(n,mul(m,g))==lambda_exponent(n,m)+lambda_exponent(conjugate_inverse(n,m),g)
        action+=1
        assert lambda_exponent(n,g)+lambda_exponent(m,g)-lambda_exponent(mul(n,m),g)==mu_exponent(conjugate_inverse(n,g),conjugate_inverse(m,g))-mu_exponent(n,m)
        compatibility+=1
    for n,m in itertools.product(elements,repeat=2):
        assert lambda_exponent(n,m)==mu_exponent(m,conjugate_inverse(n,m))-mu_exponent(n,m)
    for n in elements:
        assert mul(n,inv(n))==mul(inv(n),n)==E
        assert mu_exponent(n,E)==mu_exponent(E,n)==lambda_exponent(n,E)==lambda_exponent(E,n)==0
    a=((1,0),IDENTITY);b=((0,1),IDENTITY)
    assert mul(a,b)==mul(b,a)
    assert mu_exponent(a,b)==1 and mu_exponent(b,a)==-1
    # The irrational constant is kept symbolic; no rounded phase is used.
    assert mu_exponent(a,b)-mu_exponent(b,a)==2
    gauges=[lambda n:0,lambda n:n[0][0]**2+3*n[0][1]+n[1][1],lambda n:sum(n[1])+n[0][0]*n[0][1]-2]
    for f in gauges:
        left=mu_exponent(a,b)+f(a)+f(b)-f(mul(a,b))
        right=mu_exponent(b,a)+f(b)+f(a)-f(mul(b,a))
        assert left-right==2
    weighted_mass=4*Fraction(1,12)+9*Fraction(2,27)
    assert weighted_mass==1
    T=(1,1,0,1);L=(1,0,1,1)
    assert mv(T,(1,0))==(1,0)
    assert mv(L,(1,0))==(1,1)
    assert mv(L,(0,1))==(0,1)
    assert mv(T,(0,1))==(1,1)
    # Independent samples of the actual free-subgroup domains, with fractions.
    for k in [-4,-3,-2,-1,1,2,3,4]:
        for r in [Fraction(-4,5),Fraction(-1,2),Fraction(0),Fraction(3,4)]:
            assert abs(r+2*k)>1
        for r in [Fraction(-5),Fraction(-3,2),Fraction(3,2),Fraction(7)]:
            assert abs(r/(2*k*r+1))<1
    return {
        "sampled_semidirect_associativity_triples":cocycle,
        "exact_integer_multiplier_triples":cocycle,
        "exact_integer_lambda_action_triples":action,
        "exact_integer_compatibility_triples":compatibility,
        "exact_integer_inner_action_pairs":len(elements)**2,
        "normalizations_and_inverses":len(elements),
        "commuting_pair_exponent_difference":2,
        "commuting_pair_gauge_exponent_checks":len(gauges),
        "weighted_HS_mass":{"first":str(Fraction(1,3)),"second":str(Fraction(2,3)),"sum":str(weighted_mass)},
        "projective_parabolic_fixed_and_moved_lines":"exact integer vectors checked",
        "sampled_free_subgroup_domain_tests":64,
        "theta":"sqrt(2), retained symbolically",
        "independent_finite_matrix_HS_model":finite_matrix_model(),
        "infinite_group_nonrealization_and_rigidity":"proved in the accompanying lesson, not inferred from samples",
    }


def svg_bytes():
    out=['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1440" viewBox="0 0 1440 1440" role="img" aria-labelledby="title desc">',
         '<title id="title">An irrational compatible pair obstructs every AFD II1 realization</title>',
         '<desc id="desc">Exact integer translation area, weighted finite-algebra Hilbert-Schmidt vectors, parabolic dynamics on the real projective line, and a finite-dimensional determinant contradiction. The ambient group is Gamma times C2 and the proper normal subgroup is Gamma. Positive amenable and arbitrary-subgroup trivial-class boundaries are preserved.</desc>',
         '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#243b53"/></marker></defs>',
         '<rect width="1440" height="1440" fill="#ffffff"/>',
         '<style>text{font-family:Arial,"DejaVu Sans",sans-serif;fill:#172b4d}.title{font-size:32px;font-weight:700}.section{font-size:23px;font-weight:700}.body{font-size:19px}.small{font-size:16px}.formula{font-size:20px;font-weight:600}.red{fill:#a52835}.blue{fill:#1765a5}.green{fill:#176348}</style>']

    def text(x,y,value,klass="body",anchor="start"):
        out.append(f'<text x="{x}" y="{y}" class="{klass}" text-anchor="{anchor}">{escape(value)}</text>')

    def rect(x,y,w,h,fill="#f6f8fb",stroke="#b8c7d6",radius=12):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

    def line(x1,y1,x2,y2,arrow=False,color="#243b53",width=2.2):
        end=' marker-end="url(#arrow)"' if arrow else ''
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{end}/>')

    def circle(x,y,r=5,fill="#243b53"):
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')

    text(30,50,"A compatible pair with no AFD II₁ realization","title")
    text(30,84,"Γ = ℤ² ⋊ SL₂(ℤ),   G = Γ × C₂,   N = Γ × {e};   θ = √2.","formula")

    rect(30,110,675,400);rect(735,110,675,400)
    text(50,149,"1. The exact multiplier and translation phase","section")
    text(50,181,"μ((v,A),(w,B)) = exp(πi√2 · ω(v,Aw))","formula")
    text(50,208,"ω(v,w) = v₁w₂ − v₂w₁.   Proof: NNR1–8.")
    text(50,240,"λ(n,(g,c)) = μ(g,g⁻¹ng)/μ(n,g).","formula")
    ox,oy,step=95,432,115
    out.append(f'<polygon points="{ox},{oy} {ox+step},{oy} {ox+step},{oy-step} {ox},{oy-step}" fill="#daeaf7" stroke="#8aa8c1"/>')
    for i in range(2):
        for j in range(2):circle(ox+i*step,oy-j*step)
    line(ox,oy,ox+step,oy,True,"#1765a5",3)
    line(ox,oy,ox,oy-step,True,"#176348",3)
    text(ox-16,oy+29,"(0,0)","small")
    text(ox+step-10,oy+29,"(1,0)","small")
    text(ox-38,oy-step-14,"(0,1)","small")
    text(ox+step-20,oy-step-14,"(1,1)","small")
    text(147,416,"a = e₁","small blue")
    text(115,376,"b = e₂","small green")
    text(300,285,"ω(e₁,e₂) = 1","formula")
    text(300,327,"UV = qVU","formula red")
    text(300,360,"q = exp(2πi√2)","formula red")
    text(300,403,"qᵈ ≠ 1 for every integer d ≥ 1.","body red")
    text(300,437,"The ratio survives every gauge.")
    text(50,489,"The shaded unit square records the actual lattice area; no numerical phase approximation.","small")

    text(755,149,"2. AFD gives weighted HS unit vectors","section")
    text(755,181,"Example: F = M₂ ⊕ M₃,   (t₁,t₂) = (1/3,2/3).","body")
    text(755,208,"Pⱼ projects onto L²(Fpⱼ), of dimension dⱼ².","small")
    for r in range(2):
        for s in range(2):
            rect(775+45*s,232+45*r,43,43,"#dcecf7","#8fb4d0",2)
    for r in range(3):
        for s in range(3):
            rect(1035+32*s,232+32*r,30,30,"#dcefe2","#9abbab",2)
    text(755,351,"rank P₁ = 4","body blue")
    text(1008,351,"rank P₂ = 9","body green")
    text(755,384,"D_F = √(1/12) P₁ + √(2/27) P₂","formula")
    text(755,417,"‖D_F‖²_HS = 4/12 + 18/27 = 1","formula")
    text(755,450,"‖LᵤD_F − D_FLᵤ‖_HS ≤ 2‖u − y_F‖₂ → 0","formula")
    text(755,489,"General weights: √tⱼ/dⱼ. The displayed two-block model is an example, not every F.","small")

    rect(30,530,675,460);rect(735,530,675,460)
    text(50,569,"3. Relative rigidity proved on the dual torus","section")
    text(50,602,"Assume no nonzero T-fixed vector. Then νₙ({0}) = 0.")
    text(50,632,"Almost invariance ⇒ mass near 0 tends to 1.")
    text(50,661,"Directions ⇒ an SL₂(ℤ)-invariant probability η on RP¹.")
    text(50,689,"That probability is impossible.   Proof: NNR14–21.","formula")
    line(90,768,557,768)
    for x,r in [(140,"0"),(275,"1"),(410,"2")]:
        line(x,761,x,775);text(x,800,r,"body","middle")
    line(150,742,261,742,True)
    line(285,742,396,742,True)
    text(260,713,"T₀: r ↦ r+1","formula","middle")
    circle(588,835,6)
    text(588,867,"∞ = ℝ(1,0)","body","middle")
    out.append('<path d="M 598 833 C 644 795 646 875 597 847" fill="none" stroke="#1765a5" stroke-width="2.2" marker-end="url(#arrow)"/>')
    text(534,905,"T₀ fixes ∞","small blue")
    out.append('<path d="M 580 829 C 511 846 401 844 279 780" fill="none" stroke="#176348" stroke-width="2.2" marker-end="url(#arrow)"/>')
    text(300,837,"L₀ sends ∞ to 1","body green")
    text(50,936,"T₀-invariance forces η = δ∞, which is not L₀-invariant.","formula red")
    text(50,969,"Chart r=x/y; ∞ is the omitted line. T₀=[1 1;0 1], L₀=[1 0;1 1].","small")

    text(755,569,"4. Rigidity forces the forbidden finite dimension","section")
    rect(765,598,615,57,"#edf3fb")
    text(785,635,"Πg(S) = Lᵤg S Lᵤg*; scalar phases cancel.","formula")
    line(1070,659,1070,683,True)
    rect(765,690,615,58,"#edf3fb")
    text(785,727,"D_F almost invariant ⇒ S ≠ 0 fixed by T = ℤ².","formula")
    line(1070,751,1070,775,True)
    rect(765,782,615,58,"#edf3fb")
    text(785,819,"S*S compact ⇒ T-invariant eigenspace E, 0 < d < ∞.","formula")
    line(1070,843,1070,867,True)
    rect(765,874,615,72,"#fff1f1","#d29da4")
    text(785,904,"U_E V_E = q V_E U_E ⇒ qᵈ = 1 by determinants.","formula red")
    text(785,932,"But qᵈ = exp(2πid√2) ≠ 1. Contradiction.","formula red")
    text(755,973,"No faithful group representation or regular trace on N is assumed. NNR10–23.","small")

    rect(30,1010,1380,332,"#ffffff")
    text(50,1049,"What is disproved, and what survives","section")
    line(480,1074,480,1315,False,"#c4ced8",1.5)
    line(944,1074,944,1315,False,"#c4ced8",1.5)
    text(50,1102,"This explicit irrational class","formula red")
    for y,s in [(1140,"Proper nonamenable N is allowed."),
                (1173,"Every AFD II₁ realization fails."),
                (1206,"This excludes all possible recipes,"),
                (1239,"not only the regular product."),
                (1297,"Theorem 3; no type-III claim.")]:text(50,y,s,"body red" if y==1173 else "body")
    text(505,1102,"Amenable N: every compatible pair","formula green")
    for y,s in [(1140,"G may be any countable group."),
                (1173,"Finite N: TRP Section 9."),
                (1206,"Infinite amenable N: ARP."),
                (1239,"Same regular product, exact kernel"),
                (1272,"and original characteristic phases.")]:text(505,y,s,"body")
    text(970,1102,"Arbitrary N: the trivial class","formula green")
    for y,s in [(1140,"Q = G/N; outer Bernoulli β on R."),
                (1173,"αg = βgN;  N(α) = N."),
                (1206,"Implementers uₙ = 1 ⇒ λ = μ = 1."),
                (1239,"Thus nonamenability alone is"),
                (1272,"not an obstruction. Section 7.")]:text(970,y,s,"body")
    text(30,1375,"Question: Takesaki III, XVII.3 Exercise 5, pp.293–294. Relative-rigidity background: Cornulier, Theorem 3.2; Breuillard, III.","small")
    text(30,1404,"Complete argument: accompanying lesson. This theorem does not characterize all nonamenable classes.","small")
    out.append("</svg>")
    data=("\n".join(out)+"\n").encode("utf8")
    root=ET.fromstring(data)
    assert root.attrib["viewBox"]=="0 0 1440 1440"
    assert not any(e.tag.endswith("image") for e in root.iter())
    assert b"<script" not in data and b"href=" not in data
    return data


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument("--write",action="store_true")
    group.add_argument("--stdout",action="store_true")
    group.add_argument("--check",action="store_true")
    args=parser.parse_args()
    checks=arithmetic_checks();data=svg_bytes()
    if args.write:
        TARGET.write_bytes(data)
    elif args.stdout:
        sys.stdout.buffer.write(data)
        raise SystemExit(0)
    else:
        assert TARGET.read_bytes()==data,"Complete SVG byte comparison failed"
    print(json.dumps({"checks":checks,"SVG_bytes":len(data),"SVG_sha256":hashlib.sha256(data).hexdigest(),"physical_generated_paths":[str(TARGET)] if args.write else []}))

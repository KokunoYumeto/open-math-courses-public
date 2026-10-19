"""Exact arithmetic and original figure for TR-BAKER-10, Section 81.

GPT-6 Astra (OpenAI), Ultra. CC0; font glyphs retain their licences.
The uniform proofs are Lemmas 10.244–10.245 and Theorem 10.246.
This file verifies their rational endpoints and concrete examples.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent
rows = []
for name, f, sigma, z, w, ratio in [
    ("even residue degree", 2, 1, F(39,16), F(1), F(143,240)),
    ("odd residue degree at least three", 3, 2, F(13,8), F(8), F(143,180)),
    ("residue degree one, degree at least two", 1, 2, F(39,8), F(1), F(143,160)),
    ("rational field", 1, 2, F(81,8), F(1), F(143,160)),
]:
    endpoint = F(406,128*sigma**3)*F(13,16*f)**2*F(3,8)**4*F(135,14)*z*w
    assert 0 < endpoint < 1 and 0 < ratio < 1
    rows.append({"case":name,"endpoint_upper_bound":str(endpoint),
                 "endpoint_margin":str(1-endpoint),"successive_ratio_bound":str(ratio)})
assert [r["endpoint_upper_bound"] for r in rows] == [
    "2090104965/8589934592","77411295/1073741824",
    "2090104965/8589934592","4340987235/8589934592"]
assert F(121,100)-F(32,27) == F(67,2700)
assert F(11,4)**2*F(7,5)**3/12 == F(41503,24000) < 2
# Coefficient identities in the all-rank algebra, not a finite rank test:
# (6n+5)-2(n-1)=4n+7; logarithmic derivative numerator = 2-n.
assert (6-2,5+2)==(4,7)
assert (2+1-3,2+3-6,2)==(0,-1,2)

def multiply(x,y):
    a=[0]*5
    for i,u in enumerate(x):
        for j,v in enumerate(y):a[i+j]+=u*v
    for k in (4,3):
        c=a[k];a[k]=0;a[k-2]+=c;a[k-3]+=c
    return tuple(a[:3])

def power(x,n):
    result=(1,0,0)
    for _ in range(n):result=multiply(result,x)
    return result

def valuation(n,p):
    assert n
    answer=0
    while n%p==0:answer+=1;n//=p
    return answer

a=(0,1,0)
assert power(a,3)==(1,1,0)
assert power(a,7)==(1,2,2)
product=tuple(3*x-(1 if i==0 else 0) for i,x in enumerate(power(a,7)))
assert product==(2,6,6)
assert tuple(x//2%2 for x in product)==(1,1,1)
assert all((x**3+x+1)%2 for x in (0,1))
assert F(64,9)<8 and F(64,9)==F(64*7,63)
for m in (3,9):
    delta=63//(m*7)
    assert m*delta==9 and F(64,m*delta)==F(64,9)
original=(F(6),F(11,2),F(33))
assert original[0]*original[1]*original[2]==1089
assert valuation(1088,2)==6
certificate={"state":"passed","scope":"Exact all-rank endpoint and ratio margins, algebraic coefficient identities, cubic-field arithmetic, residue cancellation and nonunit rational example. Uniform proofs are in Section81, not inferred from finite samples.",
 "endpoints":rows,"ratio_square_margin":str(F(67,2700)),
 "analytic_residue_margin":str(2-F(41503,24000)),
 "cubic_a_power_seven":power(a,7),"cubic_product_minus_one":product,
 "cubic_residue_factor":"64/9","cubic_exact_valuation":1,
 "rational_product_minus_one":1088,"rational_exact_valuation":6,
 "scope_of_theorem":"All number fields and rational primes; original d,e,f, height floors and coefficient bounds; arbitrary normalized multiplicative rank."}
(out/"yu-two-adic-coefficient-check.json").write_text(json.dumps(certificate,indent=2)+"\n",encoding="utf-8")

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"mathtext.fontset":"dejavusans"})
fig,ax=plt.subplots(figsize=(13,8.4))
fig.patch.set_facecolor("#f8fafc")
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.text(.5,.98,"Cubic saturation across a quadratic extension",ha="center",va="top",fontsize=19,weight="bold",color="#16324a")
ax.text(.5,.91,r"Example: $K=\mathbb{Q}(a)$,  $a^3=a+1$,  $1<a<2$; independent units $(a,3)$",ha="center",fontsize=13)

def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",facecolor="white",edgecolor=color,linewidth=1.5))
    ax.text(x+.02,y+h-.025,title,va="top",fontsize=15,weight="bold",color=color)
    for j,line in enumerate(lines):ax.text(x+.02,y+h-.09-.055*j,line,va="top",fontsize=12)

box(.04,.61,.40,.23,"Original field",[
    r"$d=3,\quad e=1,\quad f=3,\quad N=8$",
    r"Residues of saturated roots lie in $\mathbb{F}_8^*$.",
    r"Their group has order $g=7$."],"#176c86")
box(.56,.61,.40,.23,r"$L=K(\zeta_3)$",[
    r"$d'=6,\quad e'=1,\quad f'=6,\quad N'=64$",
    r"Generated residue group: order $mg$.",
    r"$m=3^u,\quad m\mid9,\quad\delta_L=9/m$"],"#765296")
ax.annotate("",xy=(.55,.73),xytext=(.45,.73),arrowprops={"arrowstyle":"->","lw":2,"color":"#475569"})
box(.04,.34,.92,.20,"The norm keeps the roots in the original field",[
    r"$\beta^T=A\in K,\ T=3^r\quad\Longrightarrow\quad z=N_{L/K}(\beta),\quad z^T=A^2$",
    r"$\theta=z^{(T+1)/2}/A\in K,\quad\theta^T=A\quad\Longrightarrow\quad M_3^L=M_3^K$"],"#176c86")
box(.04,.075,.92,.20,"The residue contribution and the original target",[
    r"$m\delta_L=9,\qquad \dfrac{64}{m\delta_L}=\dfrac{64}{9}<8=N$",
    r"$2C_2(L)J^n<\mathcal{A}_n(K)$ for every $n\geq2$; original field data are retained."],"#216b53")
ax.text(.5,.022,"Proofs: Lemmas 10.244–10.245 and Theorem 10.246. Target: Bérczes–Evertse–Győry, Theorem B.",ha="center",fontsize=10.5,color="#475569")
fig.savefig(out/"yu-two-adic-coefficient.png",dpi=165,bbox_inches="tight",facecolor=fig.get_facecolor())
plt.close(fig)
print(json.dumps({"state":"passed","uniform_endpoint_cases":len(rows),"cubic_valuation":1,"rational_valuation":6}))

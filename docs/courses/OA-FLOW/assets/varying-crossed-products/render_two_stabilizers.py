"""Original exact operator-block illustration and rational checks. CC0-1.0.

The squares represent full B(L2(R)) operator corners. The finite rational
checks concern the C2 coordinate of the proved infinite-dimensional example.
DejaVu font terms are retained in FONT-LICENSE.txt.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-varying-crossed-products-two-stabilizers-20261009-v1"
from matplotlib.patches import FancyBboxPatch, Rectangle

D = Path(__file__).resolve().parent
I = [[F(1),F(0)],[F(0),F(1)]]
flip = [[F(0),F(1)],[F(1),F(0)]]
S = [[F(1),F(1)],[F(1),F(-1)]]
def scale(a,c):
    return [[c*x for x in row] for row in a]
def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def sub(a,b):
    return add(a,scale(b,F(-1)))
def flatten(a):
    return [a[i][j] for i in range(2) for j in range(2)]
def rank(rows):
    a=[list(row) for row in rows]
    if not a:return 0
    lead=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(lead,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[lead],a[pivot]=a[pivot],a[lead]
        divisor=a[lead][col]
        a[lead]=[x/divisor for x in a[lead]]
        for i in range(len(a)):
            if i!=lead and a[i][col]:
                factor=a[i][col]
                a[i]=[x-factor*y for x,y in zip(a[i],a[lead])]
        lead+=1
        if lead==len(a):break
    return lead

basis=[]
for i in range(2):
    for j in range(2):
        a=[[F(0),F(0)],[F(0),F(0)]]
        a[i][j]=F(1)
        basis.append(a)
Sinv=scale(S,F(1,2))
assert mul(Sinv,S)==I
assert mul(mul(Sinv,flip),S)==[[F(1),F(0)],[F(0),F(-1)]]
def average(a):
    return scale(add(a,mul(mul(flip,a),flip)),F(1,2))
for a in basis:
    transformed=mul(mul(Sinv,a),S)
    averaged=mul(mul(Sinv,average(a)),S)
    assert averaged==[[transformed[0][0],F(0)],[F(0),transformed[1][1]]]
    assert average(average(a))==average(a)
pplus=scale(add(I,flip),F(1,2))
pminus=scale(sub(I,flip),F(1,2))
assert mul(pplus,pplus)==pplus and mul(pminus,pminus)==pminus
assert mul(pplus,pminus)==[[F(0),F(0)],[F(0),F(0)]]
assert add(pplus,pminus)==I
rank_A=rank([flatten(average(a)) for a in basis])
rank_B=rank([flatten(a) for a in basis])
assert rank_A==2 and rank_B==4
comm_constraints=[]
for a in basis:
    columns=[flatten(sub(mul(x,a),mul(a,x))) for x in basis]
    comm_constraints.extend([[columns[j][i] for j in range(4)] for i in range(4)])
assert 4-rank(comm_constraints)==1
assert F(1,3)+F(2,3)==1
def serial(a):
    return [[str(x) for x in row] for row in a]
data={
    "group":"R x C2, with addition in both coordinates",
    "haar_measure":"dt times (delta_0 + delta_1)/2",
    "base_weights":{"A":"1/3","B":"2/3"},
    "stabilizers":{"A":"{0} x C2","B":"{(0,0)}"},
    "quotients":{"A":"R with dt","B":"R x C2 with dt times normalized counting measure"},
    "conditional_probability_density":"p(t)=exp(-abs(t))/2; integral 1 on R",
    "common_H0":"H tensor C^2, H=L2(R,dt)",
    "flip_matrix":serial(flip),
    "sign_change":"U=S/sqrt(2), with S="+str(serial(S)),
    "positive_sign_projection":serial(pplus),
    "negative_sign_projection":serial(pminus),
    "rational_checks":{"sign_diagonalization":True,"average_keeps_exactly_sign_diagonal":True,
        "average_idempotent":True,"orthogonal_sign_projections":True,
        "rank_of_C2_corner_average_A":rank_A,"rank_of_identity_on_two_by_two_corners_B":rank_B,
        "center_dimension_of_full_two_by_two_scalar_matrix_algebra":1},
    "proved_algebras":{"A":"B(H) direct sum B(H)","B":"B(H tensor C^2)",
        "whole":"B(H) direct sum B(H) direct sum B(H tensor C^2)"},
    "proved_centers":{"A":"C^2","B":"C","whole":"C^3"},
    "base_into_center":"(a,b) maps to (a,a,b)",
    "proof":"OA-FLOW-L74.md#oa-flow.field.example, (B17)-(B26)",
    "diagram_scope":"Real lines depict entire orbits. Matrix squares are full B(H) operator corners.",
    "licence":"CC0-1.0 original diagram, code and data; DejaVu font terms retained",
}
(D/"two-stabilizers-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")

plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(15,10),dpi=180,facecolor="#f8fafc")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis("off")
ink="#182e43";muted="#53687c";blue="#26689e";teal="#087f83";orange="#c87327";pale="#e7edf2"
ax.text(.55,9.55,"Same group, two stabilizers, different fiber centers",fontsize=23,weight="bold",color=ink)
ax.text(.55,9.13,r"$G=\mathbb{R}\times C_2$,  $H=L^2(\mathbb{R},dt)$",fontsize=15,color=muted)
for x in [.55,7.8]:
    ax.add_patch(FancyBboxPatch((x,1.93),6.65,6.87,boxstyle="round,pad=0.04,rounding_size=.12",
        facecolor="white",edgecolor="#ccd7e0",linewidth=1.2))
ax.text(3.875,8.43,r"Orbit A:  $H_A=C_2$,  $\nu(A)=1/3$",ha="center",fontsize=17,weight="bold",color=blue)
ax.text(11.125,8.43,r"Orbit B:  $H_B=\{e\}$,  $\nu(B)=2/3$",ha="center",fontsize=17,weight="bold",color=teal)
ax.text(3.875,8.05,r"$G/H_A\cong\mathbb{R}$",ha="center",fontsize=15,color=ink)
ax.text(11.125,8.05,r"$G/H_B\cong\mathbb{R}\times C_2$",ha="center",fontsize=15,color=ink)
def real_line(x1,x2,y,color):
    ax.annotate("",(x2,y),(x1,y),arrowprops=dict(arrowstyle="<->",lw=2.1,color=color))
real_line(1.22,6.53,7.47,blue)
ax.text(3.875,7.08,r"$t\mapsto t+s$; $C_2$ fixes this line",ha="center",fontsize=13,color=muted)
real_line(8.65,13.76,7.60,teal)
real_line(8.65,13.76,7.23,teal)
ax.text(8.30,7.60,"0",va="center",fontsize=12,color=muted)
ax.text(8.30,7.23,"1",va="center",fontsize=12,color=muted)
ax.annotate("",(13.94,7.62),(13.94,7.21),arrowprops=dict(arrowstyle="<->",lw=1.6,color=orange))
ax.text(11.125,6.83,r"$(t,\delta)\mapsto(t+s,\delta+\epsilon)$",ha="center",fontsize=13,color=muted)
ax.text(3.875,6.48,r"$\mathcal{E}_A(T)=\frac{1}{2}(T+UTU^*)$",ha="center",fontsize=16,color=blue)
ax.text(11.125,6.48,r"$\mathcal{E}_B(T)=T$",ha="center",fontsize=16,color=teal)
def matrix(x,y,labels,colors,basislabels):
    cell=1.48
    for i in range(2):
        for j in range(2):
            xx=x+j*cell; yy=y+(1-i)*cell
            ax.add_patch(Rectangle((xx,yy),cell,cell,facecolor=colors[i][j],edgecolor="white",linewidth=3))
            ax.text(xx+cell/2,yy+cell/2,labels[i][j],ha="center",va="center",fontsize=19,
                color=ink if colors[i][j]==pale else "white",weight="bold")
    for j,label in enumerate(basislabels):
        ax.text(x+(j+.5)*cell,y+2*cell+.12,label,ha="center",va="bottom",fontsize=13,color=muted)
    for i,label in enumerate(basislabels):
        ax.text(x-.15,y+(1.5-i)*cell,label,ha="right",va="center",fontsize=13,color=muted)
matrix(2.395,3.02,[[r"$B(H)$","0"],["0",r"$B(H)$"]],[[blue,pale],[pale,teal]],["+","−"])
matrix(9.645,3.02,[[r"$B(H)$",r"$B(H)$"],[r"$B(H)$",r"$B(H)$"]],[[blue,orange],[orange,teal]],["0","1"])
ax.text(3.875,2.56,r"$P_A=B(H)\oplus B(H)$",ha="center",fontsize=16,color=ink)
ax.text(11.125,2.56,r"$P_B=B(H\otimes\mathbb{C}^2)$",ha="center",fontsize=16,color=ink)
ax.text(3.875,2.17,r"$Z(P_A)=\mathbb{C}^2$",ha="center",fontsize=16,color=blue)
ax.text(11.125,2.17,r"$Z(P_B)=\mathbb{C}$",ha="center",fontsize=16,color=teal)
ax.text(7.5,1.43,r"$P\cong B(H)\oplus B(H)\oplus B(H\otimes\mathbb{C}^2)$",
        ha="center",fontsize=20,color=ink)
ax.text(7.5,.86,r"$Z(P)\cong\mathbb{C}^3,\qquad L^\infty(\{A,B\},\nu)\longrightarrow Z(P):\ (a,b)\longmapsto(a,a,b)$",
        ha="center",fontsize=16,color=ink)
ax.text(7.5,.31,"Each operator square is a full B(H) corner. The two base weights change the Hilbert norms, while the displayed algebras stay the same.",
        ha="center",fontsize=11.5,color=muted)
fig.savefig(D/"two-stabilizers.png",dpi=180)
fig.savefig(D/"two-stabilizers.svg", metadata={"Date": None})
plt.close(fig)
print(json.dumps(data["rational_checks"]))

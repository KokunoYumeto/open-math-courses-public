"""Exact compact-group examples for OA-FLOW-L52 and OA-FLOW-L53.

Original code and diagram composition: CC0-1.0.
Matplotlib uses the DejaVu font; retain FONT-LICENSE.txt.
Run with Python, NumPy and Matplotlib. No external data or network required.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    "savefig.facecolor": "white",
})

# a^i b^j, with a^3=b^2=e and b a b=a^-1.
elements = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
labels = ["e", "a", r"$a^2$", "b", "ab", r"$a^2b$"]
index = {x:i for i,x in enumerate(elements)}
def mul(x,y):
    return ((x[0]+(-1)**x[1]*y[0])%3,(x[1]+y[1])%2)
def inv(x):
    return ((-(-1)**x[1]*x[0])%3,x[1])
def left(h):
    out=np.zeros((6,6),dtype=int)
    for col,x in enumerate(elements): out[index[mul(h,x)],col]=1
    return out
def right(h):
    out=np.zeros((6,6),dtype=int)
    for col,x in enumerate(elements): out[index[mul(x,inv(h))],col]=1
    return out

e=(0,0); a=(1,0); b=(0,1)
Q=np.zeros((6,6),dtype=int); Q[index[e],index[a]]=1
orbit=[right(r)@Q@right(r).T for r in elements]
sum_orbit=sum(orbit)
assert np.array_equal(sum_orbit,left(inv(a)))
assert all(np.array_equal(right(r)@sum_orbit@right(r).T,sum_orbit) for r in elements)
coefficient=np.zeros(6,dtype=int); coefficient[index[inv(a)]]=1
assert np.array_equal(sum(coefficient[i]*left(h) for i,h in enumerate(elements)),sum_orbit)
displacements=[]
wrong_displacements=[]
for r in elements:
    s=inv(r); t=mul(a,inv(r))
    displacements.append(mul(s,inv(t)))
    wrong_displacements.append(mul(inv(t),s))
assert set(displacements)=={inv(a)}
assert set(wrong_displacements)=={a,inv(a)}

blue="#28649d"; ink="#17314a"; teal="#137d80"; orange="#c7752b"
def exact_matrix(ax, pattern, entry, title):
    ax.imshow(pattern, cmap=ListedColormap(["#f3f6f9",blue]),vmin=0,vmax=1)
    ax.set_xticks(range(6),labels); ax.set_yticks(range(6),labels)
    ax.tick_params(length=0,labelsize=13)
    ax.set_xticks(np.arange(-.5,6,1),minor=True)
    ax.set_yticks(np.arange(-.5,6,1),minor=True)
    ax.grid(which="minor",color="white",linewidth=1.6)
    ax.tick_params(which="minor",length=0)
    ax.set_title(title,fontsize=15,fontweight="bold",pad=18,color=ink)
    ax.set_xlabel("input t",labelpad=10); ax.set_ylabel("output s",labelpad=8)
    for i,j in zip(*np.nonzero(pattern)):
        ax.text(j,i,entry,ha="center",va="center",color="white",fontsize=15,fontweight="bold")
    for sp in ax.spines.values(): sp.set_visible(False)

fig=plt.figure(figsize=(13.8,5.45))
gs=fig.add_gridspec(1,3,width_ratios=[1,1,1.05],left=.055,right=.975,top=.81,bottom=.30,wspace=.40)
ax0=fig.add_subplot(gs[0]); ax1=fig.add_subplot(gs[1]); ax2=fig.add_subplot(gs[2])
exact_matrix(ax0,Q,"1",r"$Q=|e_e\rangle\langle e_a|$")
exact_matrix(ax1,sum_orbit,r"$\frac{1}{6}$",r"$\mathcal{E}(Q)=\frac{1}{6}L_{a^{-1}}$")
ax2.bar(range(6),coefficient,color=[orange if v else "#e6edf2" for v in coefficient],width=.68)
ax2.set_xticks(range(6),labels); ax2.set_ylim(0,1.12)
ax2.set_yticks([0,1]); ax2.set_ylabel(r"$a_h$")
ax2.set_xlabel("group element h",labelpad=10)
ax2.set_title("Integrated coefficient",fontsize=15,fontweight="bold",pad=18,color=ink)
ax2.spines[["top","right"]].set_visible(False)
ax2.grid(axis="y",color="#e3e8ed"); ax2.set_axisbelow(True)
fig.suptitle("A right orbit keeps the displacement  s t⁻¹  fixed",fontsize=19,fontweight="bold",color=ink,y=.98)
fig.text(.5,.105,r"$H=S_3,\quad e_x=\sqrt{6}\,1_{\{x\}},\quad dh(\{x\})=\frac{1}{6},\quad"
         r"\int_H a_hL_h\,dh=\frac{1}{6}L_{a^{-1}}$",
         ha="center",fontsize=16,color=ink)
fig.text(.5,.035,"All displayed matrix entries are exact.  The conjugacy-dependent quantity t⁻¹s is not constant along this orbit.",
         ha="center",fontsize=11.5,color="#4c6071")
for ext in ["svg","png"]:
    fig.savefig(OUT/f"compact-kernel-averaging.{ext}",dpi=170)
plt.close(fig)

# G=S3, H={e,b}: right b has three + and three - eigenvectors.
Rb=right(b)
S=np.zeros((6,6))
for j in range(3):
    S[index[(j,0)],j]=1/np.sqrt(2)
    S[index[(j,1)],j]=1/np.sqrt(2)
    S[index[(j,0)],j+3]=1/np.sqrt(2)
    S[index[(j,1)],j+3]=-1/np.sqrt(2)
signature=np.diag([1]*3+[-1]*3)
assert np.allclose(S.T@S,np.eye(6))
assert np.allclose(S.T@Rb@S,signature)
T=np.arange(1,37,dtype=float).reshape(6,6)
averaged=(T+signature@T@signature)/2
assert np.array_equal(averaged[:3,3:],np.zeros((3,3)))
assert np.array_equal(averaged[3:,:3],np.zeros((3,3)))
assert np.array_equal(averaged[:3,:3],T[:3,:3])
assert np.array_equal(averaged[3:,3:],T[3:,3:])
generators=[]
for j in range(3):
    proj=np.diag([int(x[0]==j) for x in elements])
    for g in elements: generators.append((proj@left(g)).reshape(-1))
assert np.linalg.matrix_rank(np.stack(generators))==18
assert all(np.array_equal(v.reshape(6,6)@Rb,Rb@v.reshape(6,6)) for v in generators)

fig=plt.figure(figsize=(13.8,5.25))
gs=fig.add_gridspec(1,3,width_ratios=[1.25,1,1],left=.035,right=.98,top=.80,bottom=.21,wspace=.32)
ax0=fig.add_subplot(gs[0]); ax0.axis("off")
ax0.text(.5,1.04,"Three cosets, two signs",ha="center",fontsize=15,fontweight="bold",color=ink)
for j,y in enumerate([.79,.51,.23]):
    rep=["e","a",r"$a^2$"][j]
    ax0.add_patch(Rectangle((.035,y-.125),.93,.22,facecolor="#edf2f6",edgecolor="none"))
    ax0.text(.11,y,rep+"H",ha="left",va="center",fontsize=15,fontweight="bold",color=ink)
    ax0.text(.58,y,rf"$v_{j}^+$"+"       "+rf"$v_{j}^-$",ha="center",va="center",fontsize=17,color=ink)
ax0.text(.5,-.05,r"$v_j^\pm=(e_{a^j}\pm e_{a^jb})/\sqrt{2}$",ha="center",fontsize=14,color=ink)
def blocks(ax,averaged,title):
    ax.set_xlim(0,6); ax.set_ylim(6,0); ax.set_aspect("equal")
    configs=[(0,0,"A",blue),(3,3,"B",teal),(3,0,"0" if averaged else "C","#e9eef2" if averaged else orange),(0,3,"0" if averaged else "D","#e9eef2" if averaged else orange)]
    for x,y,label,color in configs:
        ax.add_patch(Rectangle((x,y),3,3,facecolor=color,edgecolor="white",linewidth=2))
        ax.text(x+1.5,y+1.5,label,ha="center",va="center",fontsize=28,fontweight="bold",
                color="#758591" if label=="0" else "white")
    for n in range(1,6):
        if n!=3:
            ax.plot([n,n],[0,6],color="white",lw=.45,alpha=.45)
            ax.plot([0,6],[n,n],color="white",lw=.45,alpha=.45)
    ax.set_xticks([1.5,4.5],["plus","minus"]); ax.set_yticks([1.5,4.5],["plus","minus"])
    ax.tick_params(length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_title(title,fontsize=15,fontweight="bold",pad=18,color=ink)
blocks(fig.add_subplot(gs[1]),False,"An arbitrary operator T")
blocks(fig.add_subplot(gs[2]),True,"The compact average")
fig.suptitle("Compact stabilization: each subgroup character retains the quotient factor",
             fontsize=18,fontweight="bold",color=ink,y=.98)
fig.text(.5,.105,r"$R_b=\operatorname{diag}(I_3,-I_3),\qquad "
         r"E_H(T)=\frac{1}{2}(T+R_bTR_b),\qquad "
         r"\mathbb{C}^3\rtimes S_3\cong M_3(\mathbb{C})\oplus M_3(\mathbb{C})$",
         ha="center",fontsize=15,color=ink)
fig.text(.5,.028,"G = S₃,  H = {e,b},  N = ℂ.  Each square block is 3 × 3; averaging removes exactly the two mixed-sign blocks.",
         ha="center",fontsize=11.5,color="#4c6071")
for ext in ["svg","png"]:
    fig.savefig(OUT/f"compact-stabilization.{ext}",dpi=170)
plt.close(fig)

data={
    "licence":"CC0-1.0 original data and figure composition",
    "group":"S3=<a,b | a^3=b^2=e, bab=a^-1>",
    "order":["e","a","a^2","b","ab","a^2b"],
    "normalized_Haar_weight": "1/6",
    "kernel_example":{"Q":Q.tolist(),"six_times_E_Q":sum_orbit.tolist(),"a_h":coefficient.tolist(),
        "proof_locator":"OA-FLOW-L52.md#oa-flow.compactcomm.example; C6-C10 and C12"},
    "stabilization_example":{"subgroup":["e","b"],"quotient_representatives":["e","a","a^2"],
        "subgroup_Haar_weight":"1/2","quotient_measure_per_coset":"1/3",
        "right_b_matrix":Rb.tolist(),"plus_minus_signature":[1,1,1,-1,-1,-1],
        "crossed_product_linear_dimension":18,
        "proof_locator":"OA-FLOW-L53.md#oa-flow.compactstab.example; T16-T18"},
    "checks":{"kernel_identity":True,"right_fixed":True,"noncommutative_displacement":True,
        "quotient_eigenbasis":True,"expectation_block_identity":True,"generator_span_dimension":18}}
(OUT/"figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font_dir=Path(matplotlib.get_data_path())/"fonts"/"ttf"
shutil.copyfile(font_dir/"LICENSE_DEJAVU",OUT/"FONT-LICENSE.txt")
print(json.dumps(data["checks"]))

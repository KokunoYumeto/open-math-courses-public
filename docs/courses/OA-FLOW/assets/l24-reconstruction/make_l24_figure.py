"""CC0 original L24 figure. Every displayed value is specified by its proof."""
from pathlib import Path
import json
import math
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OWN=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "svg.fonttype":"none","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(16,5.5),constrained_layout=True)
grid=fig.add_gridspec(1,3,width_ratios=[1,1,1.5])
ax=fig.add_subplot(grid[0])
theta=2*np.pi*np.arange(5)/5
circle=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(circle),np.sin(circle),color="#acb5c0",lw=1)
colors=["#214e78","#c66a21","#388165","#388165","#c66a21"]
for j in range(5):
    xx,yy=np.cos(theta[j]),np.sin(theta[j])
    ax.plot([0,xx],[0,yy],color=colors[j],lw=1.1,alpha=.45)
    ax.scatter([xx],[yy],s=70,color=colors[j],zorder=3)
    ax.text(1.28*xx,1.28*yy,r"$\zeta^{%d}$"%j,ha="center",va="center",color=colors[j])
ax.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65),aspect="equal")
ax.axis("off")
ax.set_title(r"$C_5$: five orthogonal coordinates",pad=18)
ax.text(0,-1.57,r"$P_j=\frac{1}{5}\sum_{k=0}^4\zeta^{-jk}V^k$",
        ha="center",va="top",fontsize=12)
ax.text(0,1.6,r"$\zeta=e^{2\pi i/5},\quad VP_j=\zeta^jP_j$",
        ha="center",fontsize=11)

ax=fig.add_subplot(grid[1])
points={"v":(0,0),"p":(0,1.1),"c1":(-.95,-1.1),"c2":(0,-1.1),"c3":(.95,-1.1)}
for child,parent in [("v","p"),("c1","v"),("c2","v"),("c3","v")]:
    ax.annotate("",xy=points[parent],xytext=points[child],
                arrowprops={"arrowstyle":"->","color":"#214e78","lw":1.8,
                            "shrinkA":10,"shrinkB":10})
for label,point in points.items():
    ax.scatter(*point,s=80,color="#214e78",zorder=3)
    ax.text(point[0]+.1,point[1]+.08,
            {"v":r"$v$","p":"parent","c1":r"$c_1$","c2":r"$c_2$","c3":r"$c_3$"}[label],
            fontsize=11,ha="left")
for xx in [-.95,0,.95]:
    ax.plot([xx,xx],[-1.27,-1.5],color="#acb5c0",ls=":")
ax.text(0,1.57,"toward one fixed end",ha="center",fontsize=10)
ax.text(0,-1.78,r"$(R\xi)(v)=\xi(c_1)+\xi(c_2)+\xi(c_3)$",ha="center",fontsize=11)
ax.text(0,-2.1,r"$RR^*=3I,\quad A=R+R^*$",ha="center",fontsize=12)
ax.text(0,-2.42,r"$\|A\|\leq 2\sqrt{3}$",ha="center",fontsize=13,color="#214e78")
ax.set(xlim=(-1.5,1.55),ylim=(-2.7,1.8))
ax.axis("off")
ax.set_title(r"$F_2$: one parent, three children",pad=18)

ax=fig.add_subplot(grid[2])
n=np.arange(1,41)
rayleigh=2*np.sqrt(3)/(1+3/(4*n))
ax.plot(n,rayleigh,color="#388165",lw=2,label="proved radial Rayleigh lower bound")
ax.scatter(n[[0,1,4,9,19,39]],rayleigh[[0,1,4,9,19,39]],color="#388165",s=25)
ax.axhline(2*np.sqrt(3),color="#214e78",lw=1.5,
           label=r"reduced norm $2\sqrt{3}$")
ax.axhline(4,color="#c66a21",lw=1.5,label="full norm 4")
ax.fill_between(n,2*np.sqrt(3),4,color="#c66a21",alpha=.08)
ax.set(xlabel=r"radial cutoff level $n$",ylabel="norm / Rayleigh quotient",
       xlim=(1,40),ylim=(1.75,4.28))
ax.grid(alpha=.15)
ax.legend(loc="lower right",fontsize=9,frameon=False)
ax.set_title(r"$x=\delta_a+\delta_{a^{-1}}+\delta_b+\delta_{b^{-1}}$",pad=18)
ax.text(.35,.52,r"$\xi_n(v)=3^{-d(e,v)/2}\,1_{\{d(e,v)\leq n\}}$",
        transform=ax.transAxes,fontsize=11)
ax.text(.35,.40,r"$\|\xi_n\|^2=1+4n/3$",
        transform=ax.transAxes,fontsize=11)
ax.text(.35,.28,r"$\langle A\xi_n,\xi_n\rangle=8n/\sqrt{3}$",
        transform=ax.transAxes,fontsize=11)
fig.suptitle("Exact finite Fourier coordinates and an infinite-tree norm gap",
             fontsize=16)
for suffix in ["png","svg"]:
    fig.savefig(OWN/("L24-original-completions."+suffix),dpi=160,
                metadata={"Description":"CC0 original mathematical illustration; L24 Propositions 12.1 and 13.1"})
plt.close(fig)

inverse={"a":"A","A":"a","b":"B","B":"b"}
letters=tuple(inverse)
def left(letter,word):
    return word[1:] if word and word[0]==inverse[letter] else letter+word
levels=[{""}]
for k in range(7):
    levels.append({left(c,w) for w in levels[-1] for c in letters
                   if not w or w[0]!=inverse[c]})
assert [len(x) for x in levels]==[1]+[4*3**(k-1) for k in range(1,8)]
checks=[]
for n0 in range(1,8):
    vectors={w:3**(-k/2) for k in range(n0+1) for w in levels[k]}
    norm=sum(v*v for v in vectors.values())
    quadratic=sum(v*vectors.get(left(c,w),0) for w,v in vectors.items() for c in letters)
    assert abs(norm-(1+4*n0/3))<1e-10
    assert abs(quadratic-8*n0/math.sqrt(3))<1e-10
    checks.append({"n":n0,"vertices":len(vectors),"norm_squared":norm,
                   "adjacency_quadratic":quadratic,
                   "rayleigh":quadratic/norm})
target="a"*12
def distance(x,y):
    # Reduced length of y*x^-1 in the left Cayley graph.
    word="".join(inverse[c] for c in x[::-1])
    for c in y[::-1]:
        word=left(c,word)
    return len(word)
for word in set.union(*levels[:4]):
    neighbours=[left(c,word) for c in letters]
    parent=min(neighbours,key=lambda w:distance(w,target))
    assert sum(distance(w,target)<distance(word,target) for w in neighbours)==1
    assert sum(distance(w,target)>distance(word,target) for w in neighbours)==3
    for child in neighbours:
        if child!=parent:
            assert min([left(c,child) for c in letters],
                       key=lambda w:distance(w,target))==word

rng=np.random.default_rng(24)
V=np.roll(np.eye(5),1,axis=0)
zeta=np.exp(2j*np.pi/5)
Ps=[sum(zeta**(-j*k)*np.linalg.matrix_power(V,k) for k in range(5))/5
    for j in range(5)]
assert np.linalg.norm(sum(Ps)-np.eye(5))<1e-12
for i in range(5):
    assert np.linalg.norm(Ps[i].conj().T-Ps[i])<1e-12
    for j in range(5):
        assert np.linalg.norm(Ps[i]@Ps[j]-(Ps[j] if i==j else 0))<1e-12
for _ in range(50):
    f=rng.normal(size=5)+1j*rng.normal(size=5)
    coordinates=np.array([sum(f[k]*zeta**(j*k) for k in range(5)) for j in range(5)])
    operator=sum(f[k]*np.linalg.matrix_power(V,k) for k in range(5))
    assert abs(np.linalg.norm(operator,2)-max(abs(coordinates)))<1e-11
    recovered=np.array([sum(coordinates[j]*zeta**(-j*k) for j in range(5))/5
                        for k in range(5)])
    assert np.linalg.norm(recovered-f)<1e-11
receipt={"status":"passed","purpose":"finite arithmetic and figure consistency, not proof substitution",
         "radial_samples":checks,"tree_end_orientation_vertices":len(set.union(*levels[:4])),
         "fourier_random_samples":50,"seed":24,
         "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OWN/"FIGURE_AND_ARITHMETIC_CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n",
                                                  encoding="utf-8")
print(json.dumps({"status":"passed","figure":str(OWN/"L24-original-completions.png"),
                  "radial_samples":len(checks),"fourier_samples":50}))

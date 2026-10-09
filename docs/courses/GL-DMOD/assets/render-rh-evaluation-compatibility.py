"""Reproduce leaf V's exact normalization and functor diagrams.

Run from any directory with Python and matplotlib. Outputs remain beside this
script. Geometry in the first panel is schematic; its circle is exactly
z = epsilon exp(i theta), with epsilon = 1 solely for plotting.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "none"})
INK, BLUE, GREEN, BG = "#17324d", "#146899", "#177563", "#f6f8fb"

def box(ax, x, y, w, h, text, color=BLUE, size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.015",
                              linewidth=1.4,edgecolor=color,facecolor="white"))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=INK,fontsize=size)

def arrow(ax, start, end, label="", dy=0.015):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=15,
                               color=INK,lw=1.4))
    if label:
        ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+dy,label,
                ha="center",va="bottom",fontsize=12,color=INK)

fig = plt.figure(figsize=(15,10),facecolor=BG)
fig.suptitle("The normal residue and the ambient evaluation use the same trace",
             fontsize=21,color=INK,y=.97)
grid=fig.add_gridspec(2,2,left=.045,right=.96,bottom=.085,top=.90,
                     width_ratios=(.85,1.5),height_ratios=(1.1,1),hspace=.18,wspace=.10)
ax=fig.add_subplot(grid[0,0]); ax.set_aspect("equal"); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.45,1.5)
ax.axhline(0,color="#8999a7",lw=.8);ax.axvline(0,color="#8999a7",lw=.8)
t=np.linspace(0,2*np.pi,400);ax.plot(np.cos(t),np.sin(t),lw=2.8,color=BLUE)
for theta in [.35,2.45,4.55]:
    arrow(ax,(np.cos(theta),np.sin(theta)),(np.cos(theta+.18),np.sin(theta+.18)))
ax.plot(0,0,"o",color=INK,ms=6)
ax.text(.08,.12,"z = 0",color=INK)
ax.text(1.30,-.10,"Re z",fontsize=11,ha="right");ax.text(.06,1.30,"Im z",fontsize=11)
ax.text(0,-1.26,r"$z=\epsilon e^{i\theta},\quad 0\leq\theta\leq2\pi$",ha="center",fontsize=12)
ax.set_xticks([]);ax.set_yticks([])
ax.set_title("Positive circle in one normal disc",color=INK,fontsize=14,pad=12)
ax.text(0,1.05,r"$\int_{|z|=\epsilon}^{+} dz/z=2\pi i$",ha="center",fontsize=15)
for sp in ax.spines.values():sp.set_visible(False)

ax=fig.add_subplot(grid[0,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
box(ax,.025,.74,.94,.20,
    "Point-module resolution:  D e₁ → D e₀, right multiplication by z\n"
    "degrees [−1, 0]; Hom differential −z; shifted evaluation sign +1",size=12)
box(ax,.025,.41,.94,.22,
    "c ordered normal directions; normal top form contracts the transfer determinant\n"
    r"untwisted top frame: $\varepsilon_c(2\pi i)^c$; closed dual map: $\varepsilon_c H_z$"+"\n"
    r"ordered tensor--Hom frame: positive residue period $(2\pi i)^c$",size=12)
arrow(ax,(.50,.74),(.50,.64),"",dy=0)
box(ax,.025,.035,.94,.26,
    r"$i:Z\hookrightarrow X,\quad c=d_X-d_Z,\quad q_X=(2\pi i)^{-d_X}$"+"\n"
    r"$q_X(2\pi i)^c=q_Z$"+"\n"
    "trace-calibrated evaluation commutes with the actual closed-support counit",
    color=GREEN,size=14)
arrow(ax,(.50,.41),(.50,.30),"",dy=0)

ax=fig.add_subplot(grid[1,:]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.text(.5,.97,"Projective trace: ordered Čech/form density, with base coefficients retained",
        ha="center",fontsize=16,color=INK)
box(ax,.02,.42,.42,.38,
    r"$p:\mathbf{P}^{r}\times Y\longrightarrow Y$"+"\n"
    r"$\eta=[dz_1\wedge\cdots\wedge dz_r/(z_1\cdots z_r)]$"+"\n"
    r"operator trace $\mathrm{res}(\eta)=1$",size=15)
box(ax,.57,.42,.41,.38,
    "actual forms comparison and positive orientation\n"
    r"period of $\eta$: $(2\pi i)^r$"+"\n"
    r"$q_{\mathbf{P}^{r}\times Y}(2\pi i)^r=q_Y$",color=GREEN,size=14)
arrow(ax,(.44,.61),(.57,.61),"1.vk–1.vl",dy=.03)
ax.text(.5,.26,
    r"For $r=1$: $[dz/z]\mapsto d\rho_\infty\wedge dz/z=i\rho_\infty'(r)dr\wedge d\theta$."+"\n"
    r"$\rho_\infty:0\to1$ gives positive complex-oriented integral $2\pi i$.",
    ha="center",va="center",fontsize=14,color=INK)
ax.text(.5,.06,"The schematic fixes no preferred splitting of cohomology. The trace and evaluation are the actual maps.",
        ha="center",fontsize=11,color=INK)
fig.text(.045,.025,"Proof locators: Theorem 1.18 (1.vb), (1.vf)–(1.vi); Theorem 1.19 (1.vk)–(1.vl); Signed chain calculations (1.vah)–(1.val). Human reading: Ginzburg, III.4 and IV.3 (free author notes).",
         fontsize=10,color=INK)
for ext in ("png","svg"):
    fig.savefig(OUT/f"rh-trace-calibration.{ext}",dpi=160,facecolor=BG)
plt.close(fig)

fig,ax=plt.subplots(figsize=(15,11),facecolor=BG)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.text(.5,.967,"Every compatibility is built from an actual map",ha="center",fontsize=23,color=INK)
box(ax,.04,.77,.29,.14,"Regular connection pair E, H\nflat-frame product map is the identity\n1.vt on connection loci",size=13)
box(ax,.37,.77,.29,.14,"a_*E, b_*H standards\noperator exterior direct comparison\nactual sheaf exterior counits",size=13)
box(ax,.70,.77,.26,.14,"Every bounded regular pair\nfinite generation in each variable\nall attaching maps retained",size=13,color=GREEN)
arrow(ax,(.33,.84),(.37,.84));arrow(ax,(.66,.84),(.70,.84))
ax.text(.5,.723,"The exterior de Rham map k is multiplication of coefficient germs and ordered wedge of forms (1.vt–1.vu-a).",
        ha="center",fontsize=12,color=INK)

rows=[
    ("Duality",r"$F_X D_XM\ \longrightarrow\ \mathbf{D}_XF_XM$", "v: finite evaluation, then q_X (1.vc)"),
    ("Shriek direct",r"$F_Y f_!M\ \longrightarrow\ Rf_!F_XM$", "ξ: dualize the actual direct comparison (1.vm)"),
    ("Extraordinary inverse",r"$F_X f^!N\ \longrightarrow\ f^!F_YN$", "β: dualize the actual ordinary inverse (1.vn)"),
]
ys=[.64,.56,.48]
for (label,formula,description),y in zip(rows,ys):
    ax.text(.045,y,label,fontsize=13,color=INK,va="center")
    ax.text(.255,y,formula,fontsize=17,color=BLUE,va="center")
    ax.text(.665,y,description,fontsize=11.5,color=INK,va="center")
box(ax,.04,.345,.92,.095,
    "Actual unit and counit equations (1.vo–1.vo-a), composition (1.vo-b), and bidual equation (1.vd)\n"
    "Proper β: residue-one trace; smooth r-dimensional orientation factor (2πi)⁻ʳ; closed c-normal factor (2πi)ᶜ",
    size=13,color=GREEN)

ax.text(.05,.286,"Diagonal and currying retain the tensor convention and its shift",fontsize=16,color=INK)
ax.text(.065,.23,"Operator object",fontsize=12,color=INK,weight="bold")
ax.text(.44,.23,"Sheaf object after F_X",fontsize=12,color=INK,weight="bold")
table=[
    (r"$M\otimes^!N=(M\otimes^L_{\mathcal{O}_X}N)[-d_X]$",r"$\Delta_X^!(F_XM\boxtimes F_XN)$"),
    (r"$M\otimes^*N=D_X(D_XM\otimes^!D_XN)$",r"$F_XM\otimes^L F_XN$"),
    (r"$\mathcal{H}_X(M,N)=D_X(M\otimes^*D_XN)$",r"$R\mathcal{H}om(F_XM,F_XN)$"),
]
for y,(left,right) in zip([.18,.125,.070],table):
    ax.text(.065,y,left,fontsize=15,color=BLUE,va="center")
    ax.text(.44,y,right,fontsize=15,color=BLUE,va="center")
    ax.text(.88,y,["1.vv–1.vx","1.vw–1.vx","1.vy–1.vaa"][list([.18,.125,.070]).index(y)],fontsize=11,color=INK,va="center")
fig.text(.05,.015,"F_X = DR_X. Full scope: smooth separated finite-type complex varieties; arbitrary singular supports; all bounded regular complexes. Schematic of proved maps.",
         fontsize=10,color=INK)
for ext in ("png","svg"):
    fig.savefig(OUT/f"rh-functor-compatibility.{ext}",dpi=160,facecolor=BG)
plt.close(fig)
print("Wrote two reproducible PNG/SVG pairs.")

fig,ax=plt.subplots(figsize=(15,10),facecolor=BG)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.956,'The raw augmentation retains its signs',ha='center',fontsize=23,color=INK)
box(ax,.035,.72,.93,.17,
    r'$P_\partial=[D e_1\ \longrightarrow\ D e_0],\quad DP_\partial=[D f_0\ \longrightarrow\ D f_1]$; differentials $\partial$, $-\partial$'+'\n'
    r'horizontal lift $f_1-dz\,f_0$; Spencer augmentation sends it to $-f_0$'+'\n'
    r'$v_{\mathcal{O}}=-(2\pi i)^{-1}$ in the positive untwisted connection frame',size=15)
box(ax,.035,.49,.45,.17,
    r'$\sigma_d=(-1)^{d(d+1)/2}$'+'\n'
    'd = 0, 1, 2, 3, 4:  +1, −1, −1, +1, +1\n'
    r'$v_{E[k]}=\sigma_d(-1)^{dk}q_X$',size=14)
box(ax,.52,.49,.445,.17,
    r'$\varepsilon_d=(-1)^{d(d-1)/2}$'+'\n'
    'd = 0, 1, 2, 3, 4:  +1, +1, −1, −1, +1\n'
    r'actual bidual frame: $(-1)^d$',color=GREEN,size=14)
box(ax,.035,.245,.93,.19,
    'Two normal variables, ordered untwisted Hom basis\n'
    r'$T:(f_\varnothing,f_1,f_2,f_{12})\mapsto(e_{12},-e_2,e_1,e_\varnothing)$'+'\n'
    r'$H_z:(e_\varnothing,e_1,e_2,e_{12})\mapsto(f_{12},f_2,-f_1,f_\varnothing)$'+'\n'
    r'closed proper dual map: $\rho_i^{\mathrm{normal}}=\varepsilon_2 H_z=-H_z$',size=14)
box(ax,.035,.035,.93,.15,
    r'$K_N^\bullet[N-1]\longrightarrow P_N\longrightarrow M\longrightarrow K_N^\bullet[N]$'+'\n'
    'entire bounded complex; fixed-width coherent kernel complexes\n'
    r'$\delta_M$ factors through $B(K_N^\bullet)[-N]$; $a+N>t$ forces the factor to vanish',color=GREEN,size=14)
fig.text(.04,.015,'Proof locators: 1.vab–1.vam. Determinants are retained. Finite matrix checks are reproducible and supplement the full proof.',fontsize=10,color=INK)
for ext in ['png','svg']:fig.savefig(OUT/f'rh-signed-spencer.{ext}',dpi=160,facecolor=BG)
plt.close(fig)

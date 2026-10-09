from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12})
fig,axs=plt.subplots(2,2,figsize=(16,11.5))
blue="#155a86"; red="#a8432e"; green="#22654e"

def setup(ax,title):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
    ax.text(0,1.02,title,transform=ax.transAxes,fontsize=16,
            weight="bold",va="bottom")

def box(ax,y,text,color=blue,size=13):
    ax.text(.5,y,text,ha="center",va="center",fontsize=size,color=color,
            bbox=dict(boxstyle="round,pad=.6",facecolor="#f4f8fa",
                      edgecolor=color,linewidth=1.3))

def down(ax,start,end,label=None):
    ax.annotate("",(.5,end),(.5,start),
                arrowprops=dict(arrowstyle="->",color=blue,lw=1.6))
    if label: ax.text(.54,(start+end)/2,label,fontsize=10.5,va="center")

ax=axs[0,0]; setup(ax,"1. Actual central lifts (HC.1–HC.4)")
box(ax,.84,r"$m_{\mu,d}=\sum_{\nu\in W\mu}\ell_\nu^d$"
    "\nDistinct-orbit moments span invariant degree d.")
box(ax,.57,r"$a_{\mu,d}(\zeta)=\mathrm{tr}_{F_\mu}"
    r"\,r_\mu(\kappa^{-1}\zeta)^d$"
    "\nRestriction = leading orbit moment + lower-norm moments.")
down(ax,.71,.67)
box(ax,.29,"Finite norm descent lifts every invariant polynomial.\n"
    r"$\sigma(a)\in Z(U\mathfrak{g})$; correct lower degrees recursively.")
down(ax,.47,.39)
ax.text(.5,.06,r"$q:Z(U\mathfrak{g})\simeq\mathbf{C}[\mathfrak{h}^*]^W$",
        ha="center",fontsize=18,color=green)

ax=axs[0,1]; setup(ax,"2. The actual scalar and its sign (T.1–T.4)")
box(ax,.89,r"Operators on $\mathcal{L}(-\lambda)$"
    "\n" r"Base fiber action: $h\mapsto-\lambda(h)$")
box(ax,.62,"Evaluation is a right module.\n"
    r"Via antipode $S$, its highest weight is $\lambda$.")
down(ax,.80,.73)
box(ax,.35,r"$q_{S(z)}(\xi)=q_z(-\xi)$"
    "\n" r"$u_\lambda(z)=q_z(-\lambda-\rho)\,1$")
down(ax,.52,.45)
ax.text(.5,.10,"Actual integral characters are polynomially dense.\n"
        "The finite operator identity extends to every complex λ.",
        ha="center",fontsize=12.5,color=green)

ax=axs[1,0]; setup(ax,"3. Uniform highest splitting (T.5; E.4; S.1)")
box(ax,.88,r"$\mu=N\,2\rho,\quad A^N=\mathcal{L}(-\mu)$"
    "\n" r"$i_M:M\longrightarrow(M\otimes A^N)\otimes F_\mu$")
ax.text(.5,.65,r"Factor labels: $\chi_{\tau-\mu+\nu}$"
        "\n" r"Endpoint $\nu=\mu$ has label $\chi_\tau$ and occurs once.",
        ha="center",fontsize=13)
box(ax,.40,"Finite central CRT projector gives a C-linear retraction.\n"
    "The fixed bundle injection is natural for every O-linear map.",
    color=green,size=12.5)
ax.text(.5,.14,r"$\tau(h_\alpha)\notin\mathbf{Z}_{>0}$ for every positive root."
        "\nNo reality condition on the other root pairings.",
        ha="center",fontsize=12.5)

ax=axs[1,1]; setup(ax,"4. Uniform lowest splitting (E.5; S.2–S.4)")
box(ax,.88,r"$p_M:M\otimes F'\longrightarrow M\otimes A^N$"
    "\n" r"$F'$ has lowest weight $-\mu$.")
ax.text(.5,.65,r"Factor labels: $\chi_{\tau+\nu'}$"
        "\n" r"Endpoint $\nu'=-\mu$ has label $\chi_{\tau-\mu}$ and occurs once.",
        ha="center",fontsize=13)
box(ax,.40,"Regular antidominant τ supplies the C-linear section.\n"
    "All quasi-coherent modules have nonzero sections when nonzero.",
    color=green,size=12.5)
ax.text(.5,.14,"Antidominance gives all higher-cohomology vanishing.\n"
        "Ring isomorphism, §5A.10: " r"$U(\mathfrak{g})_\chi"
        r"\ \overset{\sim}{\longrightarrow}\ \Gamma(\mathscr{D}_\lambda)$",
        ha="center",fontsize=12.5,color=red)

fig.suptitle("Center action and translation splittings at full flag scope",
             fontsize=22,weight="bold",y=.995)
fig.text(.5,.012,"τ = −λ − ρ throughout. Actual group characters, arbitrary rank and central quotients. "
         "Proofs: HC.1–HC.5, T.1–T.6, E.1–E.5, BC.1–BC.4, S.1–S.4.",
         ha="center",fontsize=10.5,color="#47535c")
fig.subplots_adjust(left=.065,right=.97,bottom=.075,top=.915,hspace=.26,wspace=.18)
fig.savefig(ROOT/"center-and-splitting-mechanisms.png",dpi=155)
fig.savefig(ROOT/"center-and-splitting-mechanisms.svg")
print("Rendered center-and-splitting-mechanisms PNG/SVG")

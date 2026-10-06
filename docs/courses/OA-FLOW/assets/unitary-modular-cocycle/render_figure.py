"""Original exact finite model and proof-map illustration for UR0–6."""
from pathlib import Path
from fractions import Fraction
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=ROOT / "assets")
args = parser.parse_args()
out = args.output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "svg.hashsalt": "OA-FLOW-UR-20261005-fixed",
    "axes.unicode_minus": False,
})
Q = np.diag([1.0, 4.0])
R = np.array([[5.0, 4.0], [4.0, 5.0]])
def power(a, z):
    values, vectors = np.linalg.eigh(a)
    return (vectors * np.exp(z * np.log(values))) @ vectors.T.conj()
def u(t):
    return power(R, 1j*t) @ power(Q, -1j*t)
def sigma(t, x):
    return power(Q, 1j*t) @ x @ power(Q, -1j*t)
x = np.array([[1+2j, 2-1j], [3j, -2+.5j]])
y = np.array([[2-1j, -.5j], [1+1j, 3-2j]])
checks = {}
checks["cocycle_residual"] = float(np.linalg.norm(u(.37-.61)-u(.37) @ sigma(.37,u(-.61))))
checks["eta_residual"] = float(np.linalg.norm(
    x @ (power(R,.5) @ y).T.conj() - x @ y.T.conj() @ power(R,.5)))
t = .43
delta_x = power(Q,1j*t) @ x @ power(Q,-1j*t)
v_x = u(t) @ delta_x
u_x = u(t) @ delta_x @ u(t).T.conj()
checks["V_action_residual"] = float(np.linalg.norm(v_x-power(R,1j*t) @ x @ power(Q,-1j*t)))
checks["U_action_residual"] = float(np.linalg.norm(u_x-power(R,1j*t) @ x @ power(R,-1j*t)))
checks["normalization_phi"] = float(np.trace(Q))
checks["normalization_psi"] = float(np.trace(R))
er = np.array([[1,1],[1,-1]],dtype=float)/np.sqrt(2)
eigen_residuals = []
for i, rv in enumerate((9.,1.)):
    for j, qv in enumerate((1.,4.)):
        basis = np.outer(er[:,i], np.eye(2)[:,j])
        eigen_residuals.append(np.linalg.norm(power(R,.5)@basis@power(Q,-.5)-np.sqrt(rv/qv)*basis))
    for j, sv in enumerate((9.,1.)):
        basis = np.outer(er[:,i],er[:,j])
        eigen_residuals.append(np.linalg.norm(R@basis@np.linalg.inv(R)-(rv/sv)*basis))
checks["displayed_eigenvalue_residual"] = float(max(eigen_residuals))
v = np.array([[0,1],[-1,0]],dtype=complex)
base_gns = (v.T.conj()@x@v)@power(Q,.5)
cone_aligned = v@base_gns@v.T.conj()
checks["coboundary_standard_factor_residual"] = float(np.linalg.norm(cone_aligned-x@v@power(Q,.5)@v.T.conj()))
assert max(v for k,v in checks.items() if k.endswith("residual")) < 1e-12
relative = [[Fraction(3), Fraction(3,2)], [Fraction(1), Fraction(1,2)]]
modular = [[Fraction(1), Fraction(9)], [Fraction(1,9), Fraction(1)]]
data = {
    "proof": "UNITARY_MODULAR_COCYCLE_REALIZATION.md, UR0–6; UR3–5, UR18, UR26–42",
    "Q": [[1,0],[0,4]], "R": [[5,4],[4,5]],
    "T_basis": "row eigenvectors of R (9,1); column eigenvectors of Q (1,4)",
    "D_basis": "row and column eigenvectors of R (9,1)",
    "T_exact": [[str(v) for v in row] for row in relative],
    "D_exact": [[str(v) for v in row] for row in modular],
    "checks": checks, "scope": "Exact M2 model; general proof retains arbitrary Hilbert spaces and full spectral domains.",
}
(out/"figure-data.json").write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")

fig = plt.figure(figsize=(14,11),dpi=200,facecolor="#f5f7fb")
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ink="#16324f"; blue="#2364aa"; teal="#087e8b"
ax.text(.05,.958,"Two generators, one recovered weight",fontsize=26,weight="bold",color=ink,va="top")
ax.text(.05,.909,"Arbitrary faithful n.s.f. reference weight • full domains • exact cocycle normalization",
        fontsize=14,color="#45566b",va="top")
def box(x0,y0,w,h,title,body,color=blue):
    ax.add_patch(FancyBboxPatch((x0,y0),w,h,boxstyle="round,pad=0.012,rounding_size=0.012",
                  facecolor="white",edgecolor=color,linewidth=1.6))
    ax.text(x0+.014,y0+h-.017,title,color=color,fontsize=14,weight="bold",va="top")
    ax.text(x0+.014,y0+h-.050,body,color=ink,fontsize=14,va="top",linespacing=1.6)
def arrow(start,end):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=16,linewidth=1.5,color="#59758f"))
box(.05,.731,.26,.132,"Given cocycle  ·  UR1–3",
    r"$u_{t+r}=u_t\sigma_t^\varphi(u_r)$"+"\n"+r"$\rho_t(x)=u_t\sigma_t^\varphi(x)$")
box(.37,.754,.25,.11,"Relative generator  ·  UR5",
    r"$V_t=u_t\Delta_\varphi^{it}=e^{itH}$"+"\n"+r"$T=e^{H/2}$")
box(.68,.754,.27,.11,"Recovered finite algebra",
    r"$\eta(xy^*)=xJT\Lambda_\varphi(y)$"+"\n"+r"$x,y\in\mathcal{C}$  ·  UR18–29")
box(.37,.598,.25,.108,"Modular generator  ·  UR5",
    r"$U_t=u_tJu_tJ\Delta_\varphi^{it}$"+"\n"+r"$D=e^K,\quad S_\psi=JD^{1/2}$",teal)
box(.68,.598,.27,.108,"Cone alignment  ·  UR32–38",
    r"$P_\psi=P_\varphi$"+"\n"+r"$T=\Delta_{\psi,\varphi}^{1/2}$",teal)
arrow((.322,.816),(.355,.816))
arrow((.635,.816),(.665,.816))
arrow((.307,.744),(.358,.659))
arrow((.635,.650),(.665,.650))
arrow((.815,.741),(.815,.721))
ax.text(.055,.661,"Gaussian graph cores",fontsize=14,weight="bold",color=ink)
ax.text(.055,.634,r"$\Lambda_\varphi(\mathcal{C})$ is a core for $T$",fontsize=13,color=ink)
ax.text(.055,.611,r"Full $D(T)$ is proved, not assumed.",fontsize=12,color="#45566b")
ax.text(.5,.548,r"Exact conclusion:  $(D\psi:D\varphi)_t=u_t$",ha="center",fontsize=21,color=ink,weight="bold")
ax.plot([.05,.95],[.524,.524],color="#cad5e2",lw=1)
ax.text(.05,.484,"Exact M₂ model",fontsize=19,weight="bold",color=ink)
ax.text(.32,.484,r"$Q=\mathrm{diag}(1,4),\quad R=$",
        fontsize=17,color=ink)
for row, vals in enumerate(((5,4),(4,5))):
    for col, value in enumerate(vals):
        ax.text(.52+.027*col,.498-.022*row,str(value),fontsize=14,color=ink,ha="center",va="center")
ax.plot([.503,.497,.497,.503],[.51,.51,.464,.464],color=ink,lw=1.3)
ax.plot([.565,.571,.571,.565],[.51,.51,.464,.464],color=ink,lw=1.3)
def grid(x0,title,formula,rows,cols,values,foot):
    ax.text(x0,.439,title,fontsize=16,weight="bold",color=ink)
    ax.text(x0,.408,formula,fontsize=15,color=ink)
    gx=x0+.095; gy=.207; cw=.128; ch=.066
    for j,c in enumerate(cols):
        ax.text(gx+(j+.5)*cw,gy+2*ch+.016,c,ha="center",va="bottom",fontsize=12,color="#45566b")
    for i,r in enumerate(rows):
        ax.text(gx-.016,gy+(1.5-i)*ch,r,ha="right",va="center",fontsize=12,color="#45566b")
        for j in range(2):
            v=values[i][j]
            fill="#cce6f4" if v>1 else "#f1dcc5" if v<1 else "#e3e9ef"
            ax.add_patch(Rectangle((gx+j*cw,gy+(1-i)*ch),cw,ch,facecolor=fill,edgecolor="white",linewidth=2))
            ax.text(gx+(j+.5)*cw,gy+(1.5-i)*ch,str(v),ha="center",va="center",fontsize=21,color=ink,weight="bold")
    ax.text(x0,.174,foot,fontsize=11.5,color="#45566b",va="top",linespacing=1.45)
grid(.05,r"Relative half-power $T$",r"$T\xi=R^{1/2}\xi Q^{-1/2}$",
     [r"$r_i=9$",r"$r_i=1$"],[r"$q_j=1$",r"$q_j=4$"],relative,
     "Rows: R eigenvectors. Columns: Q eigenvectors.\nEach cell is the eigenvalue "+r"$\sqrt{r_i/q_j}$"+".")
grid(.54,r"Modular operator $D$",r"$D\xi=R\xi R^{-1}$",
     [r"$r_i=9$",r"$r_i=1$"],[r"$r_j=9$",r"$r_j=1$"],modular,
     "Rows and columns: R eigenvectors.\nEach cell is the eigenvalue "+r"$r_i/r_j$"+".")
ax.text(.05,.087,r"$\varphi(x)=\mathrm{Tr}(Qx),\quad \psi(x)=\mathrm{Tr}(Rx),\quad \varphi(1)=5,\quad \psi(1)=10$",
        fontsize=16,color=ink)
ax.text(.05,.048,"The two panels use different rank-one bases. Exact rational values; colors only distinguish < 1, = 1, > 1.",
        fontsize=11.5,color="#45566b")
ax.text(.05,.025,"Proof: UR0–6, especially UR32–42. Source: Takesaki II, VIII.3.8, pp.115–121; earlier local WF/NC/MC/BC proofs.",
        fontsize=10.2,color="#596b7c")
fig.savefig(out/"cocycle-realization.png",dpi=200,metadata={"Software":"OA-FLOW original UR renderer"})
fig.savefig(out/"cocycle-realization.svg",metadata={"Date":None,"Creator":"OA-FLOW original UR renderer"})
(out/"cocycle-realization.svg").write_text(
    (out/"cocycle-realization.svg").read_text(encoding="utf-8"),
    encoding="utf-8",newline="\n")
plt.close(fig)
print(json.dumps({"outputs":str(out),"checks":checks},indent=2))

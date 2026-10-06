"""Exact OA-FLOW L41 matrix-swap illustration. Original code/data: CC0-1.0.
Requires numpy and matplotlib; retain FONT_LICENSE_DEJAVU.txt with outputs.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
weights = [F(1,3), F(2,3)]
rho = [[F(2,3), F(1,3)], [F(1,4), F(3,4)]]
source = [1,0]
j = [weights[source[y]]/weights[y] for y in range(2)]
h = j.copy()
squares = [[h[y]*r for r in rho[source[y]]] for y in range(2)]
normalized = [[r/h[y] for r in squares[y]] for y in range(2)]
masses = [weights[y]*h[y] for y in range(2)]
assert sum(weights)==1 and all(sum(row)==1 for row in rho)
assert j==[F(2),F(1,2)] and j[0]*j[1]==1
assert all(weights[y]*j[y]==weights[source[y]] for y in range(2))
assert list(map(sum,squares))==h
assert normalized==[rho[1],rho[0]]
assert masses==[F(2,3),F(1,3)] and sum(masses)==1

def U(v): return [np.sqrt(float(j[y]))*v[source[y]] for y in range(2)]
def J(v): return [b.conj().T for b in v]
def L(a,v): return [a[y]@v[y] for y in range(2)]
def norm2(v): return sum(float(weights[y])*np.vdot(v[y],v[y]).real for y in range(2))
def same(v,w): return all(np.allclose(b,c,rtol=0,atol=1e-12) for b,c in zip(v,w))
eta=[np.array([[1+2j,3],[-1j,2-1j]]),np.array([[0,1-1j],[4,2j]])]
a=[np.array([[1,2+1j],[0,-1]]),np.array([[2j,-3],[1+1j,2]])]
assert np.isclose(norm2(U(eta)),norm2(eta),rtol=0,atol=1e-12)
assert same(U(U(eta)),eta) and same(U(J(eta)),J(U(eta)))
assert same(U(L(a,U(eta))),L([a[1],a[0]],eta))
assert all(np.linalg.eigvalsh(b).min()>-1e-12 for b in U([b.conj().T@b for b in eta]))

data={
 "license":"CC0-1.0",
 "proof_locator":"OA-FLOW-L41.md#oa-flow.cstd.example; E1-E13",
 "group":"C2={e,s}, s^2=e",
 "base_action":"T_s(0)=1, T_s(1)=0",
 "base_masses":list(map(str,weights)),
 "density_matrix_diagonals":[list(map(str,row)) for row in rho],
 "target_columns":[0,1],"source_for_each_target":source,
 "fibre_arrows":"u(s,x)b=b between the labelled Hilbert-Schmidt copies",
 "pushforward_density_at_target":list(map(str,j)),
 "global_unitary":"U_s(eta_0,eta_1)=(sqrt(2)*eta_1,eta_0/sqrt(2))",
 "transported_vector_squared_diagonal_entries":[list(map(str,row)) for row in squares],
 "transported_conditional_masses_h":list(map(str,h)),
 "transported_central_masses":list(map(str,masses)),
 "normalized_vector_squared_diagonal_entries":[list(map(str,row)) for row in normalized],
 "exact_checks":["mu(y)*j_s(y)=mu(T_s^-1 y)","j_s(0)*j_s(1)=1",
                 "sum diagonal squares=h_nu","sum_y mu(y)*h_nu(y)=1",
                 "normalized squared diagonal entries=rho_source"],
 "numerical_checks":["weighted norm preservation","U_s^2=1","U_s J=J U_s",
                     "U_s L_a U_s*=L_alpha_s(a)","positive-cone preservation"],
 "numerical_absolute_tolerance":1e-12,
}
(OUT/"exact-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
 "mathtext.fontset":"dejavusans","svg.fonttype":"path",
 "svg.hashsalt":"oa-flow-l41-moving-standard-fields"})
fig=plt.figure(figsize=(15,12),facecolor="#f7fafc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ink="#193141"; muted="#536b7a"; blue="#196a9a"; orange="#b35420"; green="#177b62"
def fraction(q):
 return str(q.numerator) if q.denominator==1 else r"\frac{"+str(q.numerator)+"}{"+str(q.denominator)+"}"
ax.text(.045,.967,"Identity fibre maps; unequal global vector weights",
 fontsize=25,weight="bold",color=ink,va="top")
ax.text(.045,.914,r"$M=M_2\oplus M_2,\quad\rho_0=\mathrm{diag}(2/3,1/3),\quad"
 r"\rho_1=\mathrm{diag}(1/4,3/4)$",fontsize=21,color=ink)
ax.text(.045,.868,r"$U_s(\eta_0,\eta_1)=(\sqrt{2}\,\eta_1,\eta_0/\sqrt{2})$"
 "     |     Columns are indexed by the target point.",fontsize=18,color=muted)
for y,x0 in enumerate([.045,.535]):
 cx=x0+.21;x=source[y]
 ax.add_patch(FancyBboxPatch((x0,.29),.42,.53,boxstyle="round,pad=.012",
                            fc="#edf4f7",ec="#b8cad4",lw=1.2))
 ax.text(x0+.016,.781,rf"Target $y={y}$:  $\mu(\{{{y}\}})={fraction(weights[y])}$",
         fontsize=21,weight="bold",color=blue)
 ax.text(cx,.735,rf"Incoming unit vector from source $x={x}$",
         fontsize=16,color=muted,ha="center")
 ax.text(cx,.688,rf"$u(s,{x})\xi_\varphi({x})=\rho_{x}^{{1/2}}$",
         fontsize=24,color=ink,ha="center")
 ax.text(cx,.653,"Identity fibre map; Hilbert–Schmidt norm = 1",
         fontsize=14,color=muted,ha="center")
 ax.add_patch(FancyArrowPatch((cx,.633),(cx,.592),arrowstyle="-|>",
                             mutation_scale=17,lw=2,color=orange))
 factor=r"\sqrt{2}" if y==0 else r"1/\sqrt{2}"
 ax.text(cx+.028,.608,rf"$\times\,({factor})$",fontsize=19,color=orange,va="center")
 vector=r"\sqrt{2}\,\rho_1^{1/2}" if y==0 else r"\rho_0^{1/2}/\sqrt{2}"
 ax.text(cx,.562,rf"$\xi_\nu({y})={vector}$",fontsize=24,color=orange,ha="center")
 ax.text(cx,.522,rf"$\|\xi_\nu({y})\|_{{\rm HS}}^2=h_\nu({y})={fraction(h[y])}$",
         fontsize=19,color=orange,ha="center")
 ax.add_patch(FancyArrowPatch((cx,.493),(cx,.450),arrowstyle="-|>",
                             mutation_scale=17,lw=2,color=green))
 ax.text(cx+.028,.469,rf"$\div\,({factor})$",fontsize=19,color=green,va="center")
 ax.text(cx,.416,rf"$\zeta_\nu({y})=\rho_{x}^{{1/2}}$",
         fontsize=24,color=green,ha="center")
 ax.text(cx,.375,"Normalized conditional state vector",fontsize=16,color=green,ha="center")
 ax.text(cx,.335,r"$\|\zeta_\nu(y)\|_{\rm HS}=1$",fontsize=19,color=green,ha="center")
ax.text(.045,.245,r"Central masses: reference $\varphi$ (blue), transported "
 r"$\nu=\varphi\circ\alpha_s$ (orange)",fontsize=19,color=ink)
for y,x0 in enumerate([.045,.535]):
 bx=x0+.11; bw=.255
 for name,mass,height,col in [
  (r"$\varphi$",weights[y],.185,blue),(r"$\nu$",masses[y],.139,orange)]:
  ax.text(x0+.016,height,name,fontsize=20,color=col,va="center")
  ax.barh(height,bw*float(mass),height=.018,left=bx,color=col,alpha=.85)
  ax.plot([bx,bx+bw],[height-.016,height-.016],color="#bdccd5",lw=1)
  ax.text(bx+bw+.017,height,"$"+fraction(mass)+"$",fontsize=22,color=col,va="center")
ax.text(.045,.077,r"$\mu(\{y\})h_\nu(y)=\mu(\{T_s^{-1}y\})$:"
 " central masses swap; base coordinates retain their weights.",fontsize=16,color=ink)
ax.text(.045,.032,"Exact matrix example · OA-FLOW L41 · (E1)–(E13) · "
 "Bars show probabilities, not fibre dimensions.",fontsize=12,color=muted)
fig.savefig(OUT/"moving-standard-fields.png",dpi=180,facecolor=fig.get_facecolor())
fig.savefig(OUT/"moving-standard-fields.svg",facecolor=fig.get_facecolor(),metadata={"Date":None})
plt.close(fig)
print("Exact fraction and matrix checks passed; PNG, SVG and exact data written.")

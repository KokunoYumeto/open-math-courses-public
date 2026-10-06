"""Reproduce the exact proof map; no numerical approximation is used."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
D=Path(__file__).resolve().parent;out=D/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'oa-flow-faithful-recognition-v1'})
fig=plt.figure(figsize=(14,9),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,14);ax.set_ylim(0,9);ax.axis('off')
navy='#15374A';teal='#087E82';pale='#EDF6F7';gold='#875600';grey='#49616F'
ax.text(.65,8.45,'Recovering the coefficient weight',fontsize=23,weight='bold',color=navy)
ax.text(.65,8.02,'Arbitrary LCA group and von Neumann algebra • faithful normal semifinite weights',fontsize=12,color=grey)
ax.text(.65,7.57,r'Fix $\varphi$ on $M$ using FR1.  Write $N=M\rtimes_\alpha G$ and $N^\theta=\pi(M)$.',fontsize=14,color=navy)

def box(x,y,w,h,title,formula,detail):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.08',facecolor=pale,edgecolor=teal,lw=1.5))
 ax.text(x+w/2,y+h-.31,title,ha='center',va='center',weight='bold',color=navy,fontsize=13)
 ax.text(x+w/2,y+h-.8,formula,ha='center',va='center',fontsize=17,color=navy)
 ax.text(x+w/2,y+.34,detail,ha='center',va='center',fontsize=11,color=grey)

def arrow(a,b,label='',labelpos=None):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.8,color=teal))
 if label:ax.text(*(labelpos or ((a[0]+b[0])/2,(a[1]+b[1])/2+.18)),label,ha='center',va='bottom',fontsize=11,color=teal)
box(.8,5.35,5.4,1.6,'Start with a dual-invariant target',r'$\Omega\circ\theta_\chi=\Omega$',r'$\Omega$ is a faithful n.s.f. weight on $N$')
box(7.75,5.35,5.4,1.6,'Form its normalized cocycle',r'$z_t=(D\Omega:D\widetilde\varphi)_t$',r'BC4: a unitary $\sigma^{\widetilde\varphi}$-cocycle')
arrow((6.35,6.15),(7.55,6.15),'BC4',(6.97,6.33))
box(7.75,2.7,5.4,1.6,'Pull back to the coefficient algebra',r'$v_t=\pi^{-1}(z_t)$',r'$v_{t+r}=v_t\sigma_t^\varphi(v_r)$')
arrow((10.45,5.2),(10.45,4.45),'',None)
ax.text(10.75,4.83,'BC5 + fixed algebra',fontsize=11,color=teal,va='center')
ax.text(10.75,4.53,r'$\theta_\chi(z_t)=z_t$',fontsize=13,color=teal,va='center')
box(.8,2.7,5.4,1.6,'Realize the unique input weight',r'$(D\psi:D\varphi)_t=v_t$',r'UR: $\psi$ is faithful n.s.f. on $M$')
arrow((7.55,3.5),(6.35,3.5),'UR',(6.97,3.7))
arrow((3.5,4.45),(3.5,5.2))
ax.text(.82,4.89,r'$\widetilde\psi=\Omega$',fontsize=17,color=teal)
ax.text(.82,4.56,'GDA9 + whole-cone uniqueness',fontsize=10.5,color=teal)
ax.text(.8,2.04,r'The closing identity: $(D\widetilde\psi:D\widetilde\varphi)_t=\pi(v_t)=z_t$',fontsize=16,color=navy)
ax.text(.8,1.64,'Equality holds on all positive elements, including infinite weight values. The reference choice cancels.',fontsize=11.5,color=grey)
ax.plot([.8,13.15],[1.31,1.31],color='#C4D8DC',lw=1)
ax.text(.8,.91,r'Scalar normalization: $c\Omega\longleftrightarrow c\psi$  $(c>0)$',fontsize=14,color=gold)
ax.text(.8,.5,r'Haar rescaling: $ds\mapsto a\,ds$, $T_\alpha\mapsto a^{-1}T_\alpha$; fixed $\Omega$ has input $a\psi$.',fontsize=13,color=gold)
ax.text(.8,.15,'Proof: FR1–3. Human antecedent: Haagerup, Dual weights I, Theorem 3.7 (116–117). Original proof map.',fontsize=9,color=grey)
fig.savefig(out/'faithful-dual-weight-recognition.png',dpi=160,metadata={'Software':'OA-FLOW original proof map'})
fig.savefig(out/'faithful-dual-weight-recognition.svg',metadata={'Date':None,'Creator':'OA-FLOW original proof map'})
plt.close(fig)
data={'kind':'exact proof diagram, not a sampled approximation','hypotheses':['arbitrary LCA group','arbitrary von Neumann algebra','point-ultraweakly continuous action','faithful normal semifinite weights'],'vertices':['dual-invariant Omega on N','z_t = (D Omega : D tilde(phi))_t','v_t = pi^-1(z_t)','unique psi with (D psi : D phi)_t = v_t'],'arrows':['BC4 normalized derivative','BC5 invariance + DA fixed algebra + ST2 topology + modular restriction','UR realization','GDA9 comparison + GDA7 whole-cone uniqueness'],'scalar_factor':'c Omega <-> c psi, c>0','haar_factor':'ds -> a ds; T -> a^-1 T; fixed target Omega -> input a psi','proof_locators':['FR1','FR2','FR3'],'nonclaims':['nonfaithful or nonsemifinite recognition','recognition of arbitrary covariant systems']}
(out/'faithful-dual-weight-recognition-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')

"""Original reproducible diagram; no source-paper pixels or geometry are reused."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

D=Path(__file__).resolve().parent
OUT=D/'assets';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans','svg.hashsalt':'GDW-original-20261005'})
blue='#175a91';green='#16725b';purple='#74489c';orange='#aa5e0f';ink='#172938';gray='#566573'
fig=plt.figure(figsize=(16,11),dpi=200,facecolor='white')
fig.suptitle('A general dual weight from compact coefficient graphs',fontsize=23,color=ink,y=.975)
fig.text(.5,.935,'Arbitrary LCH group; faithful n.s.f. input weight; no invariance or countability assumption',ha='center',fontsize=14,color=gray)
axes=[fig.add_axes([.045,.515,.44,.38]),fig.add_axes([.535,.515,.42,.38]),fig.add_axes([.045,.07,.44,.37]),fig.add_axes([.535,.07,.42,.37])]
for ax in axes:ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def title(ax,s):ax.text(0,1,s,fontsize=18,fontweight='bold',color=ink,va='top')
def box(ax,xy,wh,label,color=blue,fs=14):
 ax.add_patch(FancyBboxPatch(xy,*wh,boxstyle='round,pad=.012',facecolor=color+'10',edgecolor=color,linewidth=1.5))
 ax.text(xy[0]+wh[0]/2,xy[1]+wh[1]/2,label,ha='center',va='center',fontsize=fs,color=color)
def arrow(ax,p,q,color=gray):ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=15,linewidth=1.5,color=color))

a=axes[0];title(a,'1  Full graphs retain the Haar factors')
a.text(.02,.855,r'$\psi_t=\varphi\circ\alpha_{t^{-1}},\quad A_t=V_tS_{\psi_t,\varphi}$',fontsize=17,color=blue)
box(a,(.03,.58),(.91,.17),'Continuous graph pair at each t\n'+r'$(\alpha_t(b^*)\Lambda(a),\;\alpha_{t^{-1}}(a^*)\Lambda(b))$',blue,15)
a.text(.485,.525,r'$a,b\in N_\varphi$; compact scalar multiples give the whole graph core',ha='center',fontsize=12,color=gray)
arrow(a,(.485,.49),(.485,.40),green)
box(a,(.03,.12),(.91,.265),r'$(S\xi)(t)=\delta(t)^{-1}A_t\xi(t^{-1})$'+'\n'+r'$(F\zeta)(t)=A_{t^{-1}}^*\zeta(t^{-1})$'+'\n'+r'$(\widehat\Delta\xi)(t)=K_t\xi(t),\quad K_t=\delta(t)A_{t^{-1}}^*A_{t^{-1}}$',green,15)
a.text(.485,.035,'Each domain requires pointwise membership and an L² output.\nThe F domain retains its '+r'$\delta(t)^{-1/2}$'+' integrability factor.',ha='center',va='center',fontsize=12,color=ink)

b=axes[1];title(b,'2  A noninvariant eight-dimensional check')
b.text(.02,.855,r'$G=\mathbb{Z}/2,\quad d=\mathrm{diag}(1,3),\quad v:e_1\leftrightarrow e_2$',fontsize=16,color=ink)
b.text(.02,.78,r'$\varphi(E_{11})=1,\quad \varphi(\alpha_1(E_{11}))=3$',fontsize=16,color=orange)
grids=[np.array([[1,1/3],[3,1]]),np.array([[3,1],[1,1/3]])]
labels=[r'$K_0=L_dR_{d^{-1}}$',r'$K_1=L_{vdv^*}R_{d^{-1}}$']
for k,(arr,label) in enumerate(zip(grids,labels)):
 x=.07+.49*k;y=.37
 b.text(x+.17,.69,label,ha='center',fontsize=16,color=blue if k==0 else purple)
 for i in range(2):
  for j in range(2):
   val=arr[i,j];cell_color={1:green,3:orange,1/3:purple}[val]
   b.add_patch(Rectangle((x+.17*j,y+.12*(1-i)),.17,.12,facecolor=cell_color+'14',edgecolor=cell_color))
   b.text(x+.17*j+.085,y+.12*(1-i)+.06,'1/3' if val==1/3 else str(int(val)),ha='center',va='center',fontsize=18,color=cell_color)
 b.text(x+.17,.30,'Entry (i,j): eigenvalue on '+r'$E_{ij}$',ha='center',fontsize=11,color=gray)
b.text(.50,.195,r'$u(1,r)=\mathrm{diag}(3^{ir},3^{-ir})$',ha='center',fontsize=18,color=purple)
b.text(.50,.095,r'$\sigma_r^{\widehat\varphi}(\lambda_1)=\lambda_1\pi(u(1,r))$',ha='center',fontsize=18,color=blue)
b.text(.50,.025,'A unit cocycle would erase the genuine change of weight.',ha='center',fontsize=12,color=gray)

c=axes[2];title(c,'3  Compact localization gives a common adjoint test')
c.text(.02,.855,'A schematic finite cover; the group itself need not be metric.',fontsize=12,color=gray)
c.plot([.09,.88],[.61,.61],color=ink,lw=5,solid_capstyle='round')
for x,w,col in [(.07,.32,blue),(.29,.34,green),(.55,.35,purple)]:
 c.add_patch(FancyBboxPatch((x,.52),w,.18,boxstyle='round,pad=.015',facecolor=col+'12',edgecolor=col,linewidth=1.5))
c.text(.485,.765,r'$K\subset O,\quad \mu(O\setminus K)\ \mathrm{small}$',ha='center',fontsize=17,color=ink)
c.text(.485,.455,'On K: Lusin continuity + finitely many graph approximants.',ha='center',fontsize=13,color=gray)
c.text(.485,.375,r'$\|v-v_{\rm app}\|_2^2\leq\varepsilon^2\mu(K)+B^2\mu(O\setminus K)+\mathrm{tail}$',ha='center',fontsize=16,color=green)
arrow(c,(.485,.315),(.485,.245),purple)
box(c,(.04,.065),(.9,.165),'On the support of '+r'$\mu|_K$'+': every continuous pairing vanishes.\nOne common conull set tests the entire point graph.',purple,13)

dax=axes[3];title(dax,'4  Continuity follows after the weight exists')
steps=[('Compact graph core\n'+r'$\mathcal{A}=\eta(\mathscr{D})$',blue),('Closed S, full '+r'$\widehat\Delta$'+'\nBorel domains via the resolvent',green),('Whole faithful n.s.f. weight\n'+r'$\widehat\varphi$'+' from the full multiplier ideal',orange),('Modular generator formula\n'+r'$\sigma_r^{\widehat\varphi}(\lambda_g)=\delta(g)^{ir}\lambda_g\pi(u(g,r))$',purple),('Joint strong* continuity\n'+r'$(g,r)\longmapsto u(g,r)$',blue)]
for k,(label,col) in enumerate(steps):
 y=.73-.16*k
 box(dax,(.04,y),(.91,.115),label,col,13)
 if k<4:arrow(dax,(.495,y-.012),(.495,y-.045),gray)

fig.text(.5,.015,'Exact proofs: GDW1–7. Matrix sample: GDW8. Local graph construction is general; the matrix example is finite only.',ha='center',fontsize=12,color=gray)
png=OUT/'general-dual-weight.png';svg=OUT/'general-dual-weight.svg'
fig.savefig(png,dpi=200,metadata={'Software':'Original GDW proof diagram'})
fig.savefig(svg,metadata={'Date':None,'Creator':'Original GDW proof diagram'})
plt.close(fig)
data={'native_dimensions':[3200,2200],'group_example':'Z/2 with counting Haar measure','matrix_density':[[1,0],[0,3]],'flip_unitary':[[0,1],[1,0]],'basis_order':['E11','E12','E21','E22'],'K0_eigenvalues':['1','1/3','3','1'],'K1_eigenvalues':['3','1','1','1/3'],'cocycle_diagonal':['3^(i r)','3^(-i r)'],'haar_convention':'mu(E s)=delta(s) mu(E)','graph_factors':{'S':'delta(t)^-1 A_t xi(t^-1)','F_action':'A_(t^-1)^* zeta(t^-1)','F_domain_output':'delta(t)^-1/2 A_t^* zeta(t)','positive':'K_t=delta(t) A_(t^-1)^* A_(t^-1)'},'localization_bound':'epsilon^2 mu(K)+B^2 mu(O minus K)+tail','cover_is_schematic':True,'scope':'General proofs GDW1-7; finite example GDW8; no asserted metric or finite cover of the entire group','license':'CC0-1.0 to the extent of rights held'}
(OUT/'general-dual-weight-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'png':png.name,'svg':svg.name,'native_dimensions':data['native_dimensions']}))

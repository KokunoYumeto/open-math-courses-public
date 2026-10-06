from pathlib import Path
import json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
from matplotlib import font_manager
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(13,9));fig.patch.set_facecolor('#f8fafc');ax.set(xlim=(0,13),ylim=(0,9));ax.axis('off')
def box(x,y,w,h,txt,c):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.14',facecolor=c,edgecolor='#a9bbc9',linewidth=1.2));ax.text(x+w/2,y+h/2,txt,ha='center',va='center',linespacing=1.6,color='#172d43')
def arrow(p,q,label=None):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=20,linewidth=2,color='#45697a'))
 if label:ax.text((p[0]+q[0])/2,(p[1]+q[1])/2+.12,label,ha='center',fontsize=13,color='#244b64')
ax.text(.3,8.55,'Reconstruction through two commuting algebras',fontsize=25,weight='bold',color='#142b43')
ax.text(.3,8.12,r'$P=\pi(C_0(G/H))^{\prime},\quad D=L^\infty(G),\quad \gamma_h=\mathrm{Ad}(V_h)\otimes\rho_h$',fontsize=18,color='#354c61')
box(.45,5.93,4.45,1.55,'The whole quotient commutant\n'+r'$P$', '#e1ebf7')
box(7.6,5.93,4.9,1.55,'The whole fixed tensor algebra\n'+r'$(B(K)\,\bar{\otimes}\,D)^\gamma$', '#e1ebf7')
arrow((5.1,6.7),(7.4,6.7),'normal isomorphism')
ax.text(6.23,6.12,r'$a\longmapsto\widehat a$',ha='center',fontsize=18)
ax.text(.48,5.51,'Hilbert pullback: '+r'$\Lambda(f\otimes\xi)(s)=f(s)\xi(s)$',fontsize=18,color='#233d56')
box(.45,3.10,5.55,1.55,'Norm-continuous part of M\n'+r'$A=M_c,\quad a\longmapsto F_a(e)$'+'\n'+r'$N=\{F_a(e):a\in A\}^{\prime\prime}$','#dceef0')
box(6.55,3.10,5.95,1.55,'Norm-continuous part of M′\n'+r'$B=(M^{\prime})_c,\quad b\longmapsto F_b(e)$'+'\n'+r'$F_b(s)\in N^{\prime}\quad(s\in G)$','#f9e9d8')
ax.text(6.26,4.99,'continuous fields commute at every point',ha='center',fontsize=13,color='#39536b')
arrow((3.23,2.91),(3.23,2.5));arrow((9.5,2.91),(9.5,2.5))
box(.45,.64,12.05,1.66,r'$T\in(N\,\bar{\otimes}\,D)^\gamma\ \Longrightarrow\ [T,\widehat{M^{\prime}}]=0$'+'\n'+r'$T=\widehat c\ (c\in P)\ \Longrightarrow\ c\in M^{\prime\prime}=M$', '#e7efdf')
ax.text(.45,.1,'Surjectivity supplies c; faithfulness transfers commutation; the bicommutant gives equality.',fontsize=14,color='#354c61')
fig.tight_layout(pad=1);fig.savefig(P/'pullback-commutants.png',dpi=210,facecolor=fig.get_facecolor());fig.savefig(P/'pullback-commutants.svg',facecolor=fig.get_facecolor());plt.close(fig)
data={'diagram':'Arbitrary-LCH central-quotient reconstruction','hilbert_map':'Lambda(f tensor xi)(s)=f(s)xi(s)','normal_map':'P -> (B(K) bar-tensor L-infinity(G))^gamma, a -> hat(a)','evaluation_domain':'Only norm-action-continuous elements; not arbitrary measurable fields','proof_locators':['iw-3','iw-4','iw-5'],'conclusion':'hat(M)=(N bar-tensor L-infinity(G))^gamma'}
(P/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
font=Path(font_manager.findfont('DejaVu Sans'));candidates=[font.parent/'LICENSE_DEJAVU',font.parent.parent/'LICENSE_DEJAVU',Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU']
for f in candidates:
 if f.exists():shutil.copyfile(f,P/'FONT-LICENSE.txt');break
else:raise RuntimeError('Font license not found')
print(str(P/'pullback-commutants.png'))

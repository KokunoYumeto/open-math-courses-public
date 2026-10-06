"""Original exact FS4 matrix model and FS2 proof schematic. CC0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
D=Path(__file__).resolve().parent;O=D/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'OA-FLOW-fixed-supports-v1'})
w=np.array([0,0,1]);labels=(w[None,:]-w[:,None])%3
p=np.diag([1,1,0]);q=np.diag([0,0,1]);e13=np.zeros((3,3),int);e13[0,2]=1
assert np.array_equal(p@e13,e13) and not np.any(e13@p)
selectors=[]
for n in range(3):
 for i in range(3):
  for j in range(3):
   z=np.exp(2j*np.pi/3);value=sum(z**(n*s)*z**((int(w[i])-int(w[j]))*s)/3 for s in range(3))
   exact=int(labels[i,j]==n);assert abs(value-exact)<1e-13
   selectors.append({'label':n,'matrix_unit':[i+1,j+1],'exact_coefficient':exact})
blue='#176cac';orange='#ce6a1b';green='#268453';dark='#18354f';light='#e9eff4';purple='#8055a3'
fig=plt.figure(figsize=(14,10),dpi=200);fig.patch.set_facecolor('white')
fig.text(.035,.957,'Spectral support joins live in the fixed center',fontsize=26,weight='bold',color=dark)
fig.text(.035,.919,r'Exact model: $G=\mathbb{Z}/3\mathbb{Z}$, $U_s=\mathrm{diag}(1,1,\omega^s)$, $\omega=e^{2\pi i/3}$',fontsize=19,color=dark)
def matrix(ax,data,colors,title,fs=23):
 ax.set_xlim(0,3);ax.set_ylim(3,0);ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontsize=19,color=dark,pad=15)
 for i in range(3):
  for j in range(3):
   c=colors[i][j];ax.add_patch(Rectangle((j,i),1,1,facecolor=c,edgecolor='white',lw=2));ax.text(j+.5,i+.5,str(data[i][j]),ha='center',va='center',fontsize=fs,color='white' if c in [blue,orange,green,purple] else dark)
 ax.add_patch(Rectangle((0,0),3,3,fill=False,edgecolor=dark,lw=1.2))
ax=fig.add_axes([.04,.58,.22,.27]);cols=[[light if n==0 else blue if n==1 else orange for n in row] for row in labels];matrix(ax,labels,cols,'A. Negative-Fourier labels')
fig.text(.037,.533,r'$\alpha_s(e_{ij})=\overline{\gamma_{w_j-w_i}(s)}e_{ij}$',fontsize=17,color=dark)
fig.text(.037,.497,'Blue: span{e13, e23}; orange: adjoints.',fontsize=14,color=dark)
ax=fig.add_axes([.375,.58,.22,.27]);matrix(ax,p,[[green if p[i,j] else light for j in range(3)] for i in range(3)],r'B. Left join $p_{\{1\}}$')
fig.text(.36,.533,'Ranges of e13 and e23 span axes 1 and 2.',fontsize=14,color=dark)
fig.text(.386,.494,r'$p_{\{1\}}=\mathrm{diag}(1,1,0)$',fontsize=18,color=dark)
ax=fig.add_axes([.71,.58,.22,.27]);matrix(ax,q,[[purple if q[i,j] else light for j in range(3)] for i in range(3)],r'C. Right join $q_{\{1\}}$')
fig.text(.705,.533,'Both initial ranges are axis 3.',fontsize=14,color=dark)
fig.text(.721,.494,r'$q_{\{1\}}=\mathrm{diag}(0,0,1)$',fontsize=18,color=dark)
fig.text(.10,.436,r'$F=M^\alpha=M_2\oplus\mathbb{C},\qquad p_{\{1\}},q_{\{1\}}\in Z(F),\qquad p_{\{1\}}\ne q_{\{1\}}$',fontsize=21,color=dark)
fig.text(.18,.391,r'$p_{\{1\}}e_{13}=e_{13},\quad e_{13}p_{\{1\}}=0:$ the join is not central in $M_3$.',fontsize=18,color=dark)
fig.text(.04,.33,'D. General proof mechanism — arbitrary joins, arbitrary Hilbert spaces',fontsize=20,color=dark)
ax=fig.add_axes([.035,.055,.93,.245]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
boxes=[(.01,blue,r'$\alpha_s(M(E))=M(E)$'+'\n'+r'$\alpha_s(\ell(x))=\ell(\alpha_s x)$'+'\n'+'Joins are preserved.'+'\n'+r'$p_E\in F$'),(.355,green,r'$uM(E)=M(E)\quad (u\in\mathcal{U}(F))$'+'\n'+r'$\ell(ux)=u\ell(x)u^*$'+'\n'+r'$up_Eu^*=p_E$'),(.70,purple,'Commutes with all unitaries of F'+'\n'+'and hence all of F.'+'\n'+r'$p_E\in Z(F),\quad q_E=p_{-E}$')]
for x,c,t in boxes:
 ax.add_patch(FancyBboxPatch((x,.15),.285,.70,boxstyle='round,pad=.01',fc='#f5f7fa',ec=c,lw=2));ax.text(x+.1425,.5,t,ha='center',va='center',fontsize=15,color=dark,linespacing=1.6)
for a,b in [(.30,.345),(.645,.69)]:ax.annotate('',xy=(b,.5),xytext=(a,.5),arrowprops={'arrowstyle':'->','color':dark,'lw':2})
fig.text(.04,.028,'FS1–FS4 and complete caption. A–C are exact matrices; D is a proof schematic. Original CC0 figure.',fontsize=12,color=dark)
fig.savefig(O/'fixed-supports.png',metadata={'Software':'OA-FLOW FS original CC0'});fig.savefig(O/'fixed-supports.svg',metadata={'Date':None,'Creator':'OA-FLOW FS original CC0'});plt.close(fig)
data={'group':'Z/3Z','Haar':'counting','dual_point_mass':'1/3','weights':w.tolist(),'negative_Fourier_labels':labels.tolist(),'left_support_join':p.tolist(),'right_support_join':q.tolist(),'exact_selector_coefficients':selectors,'noncentrality':{'p_e13':e13.tolist(),'e13_p':(e13@p).tolist()},'general_panel':'schematic of actual FS2 proof, not a finite-model premise'}
(O/'fixed-supports-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'dimensions':[2800,2000],'exact_selectors':len(selectors)}))

from pathlib import Path
import argparse,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch,Rectangle
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=P/'assets');args=parser.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'oa-flow-l116-factor-criterion-20261005','mathtext.fontset':'dejavusans'})
blue='#22577a'; teal='#24817a'; red='#a44a3f'; grey='#52606d';bg='#f8fafc'
fig=plt.figure(figsize=(16,11),dpi=200,facecolor=bg)
fig.text(.04,.966,'A fixed center, an exact shear, and two surviving components',fontsize=22,weight='bold',color=blue)
fig.text(.04,.928,'The top row proves the general mechanism; the bottom row is the exact counting-Haar model G = Z/3Z.',fontsize=12,color=grey)
def box(ax,x,y,w,h,text,color=blue,size=15):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor='white',edgecolor=color,linewidth=1.6))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=color,fontsize=size)
def arrow(ax,p,q,color=blue): ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=15,color=color,linewidth=1.5))
ax=fig.add_axes([.04,.58,.53,.29]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(0,1,'1  Direct generator test (arbitrary LCA G, arbitrary M ≠ 0)',weight='bold',fontsize=14,color=blue)
box(ax,.03,.68,.88,.17,r'$z\in Z(N)^\theta\ \Longrightarrow\ z=i(c)$',size=18)
box(ax,.03,.35,.39,.19,r'$[z,i(a)]=0$'+'\n'+r'$i([c,a])=0\ \Rightarrow\ c\in Z(M)$',size=14)
box(ax,.52,.35,.39,.19,r'$\lambda_s z\lambda_s^*=z$'+'\n'+r'$i(\alpha_s(c))=i(c)\ \Rightarrow\ \alpha_s(c)=c$',size=13)
arrow(ax,(.24,.68),(.24,.55));arrow(ax,(.72,.68),(.72,.55))
box(ax,.03,.02,.88,.17,r'$Z(N)^\theta=i(Z(M)^\alpha)$'+'     (F5, FC1–FC2)',color=teal,size=17)
arrow(ax,(.24,.35),(.36,.2),teal);arrow(ax,(.72,.35),(.6,.2),teal)
ax=fig.add_axes([.62,.58,.34,.29]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(0,1,'2  What full spectrum leaves',weight='bold',fontsize=14,color=blue)
box(ax,.03,.69,.91,.17,r'$\Gamma(\alpha)=\widehat{G}\ \Rightarrow\ Z(N)=Z(N)^\theta$',size=16)
arrow(ax,(.48,.69),(.48,.54))
box(ax,.03,.32,.91,.21,r'$Z(M)^\alpha=\mathbb{C}1\ \Rightarrow\ Z(N)=\mathbb{C}1$'+'\n'+'central ergodicity gives a factor (F16–F17)',color=teal,size=13)
ax.text(.49,.07,'Without central ergodicity:\nfixed center can retain two components.',ha='center',va='center',fontsize=13,color=red)
ax=fig.add_axes([.04,.095,.54,.38]);ax.set(xlim=(-.35,4.1),ylim=(-.55,3.45));ax.axis('off')
ax.text(-.35,3.48,'3  S is a permutation of all nine coordinates (TR2–TR4)',weight='bold',fontsize=14,color=blue)
ax.text(.65,3.0,'input (r,t)',ha='center',weight='bold');ax.text(3.15,3.0,'output (u,v)',ha='center',weight='bold')
colors=[blue,teal,red];perm=[]
for r in range(3):
 for t in range(3):
  u=(r+t)%3;v=r;perm.append({'r':r,'t':t,'u':u,'v':v})
  # Coordinate-label positions are a drawing layout, not group distances.
  xp=t*.62;yp=2.25-r*.85;xq=2.5+u*.62;yq=2.25-v*.85
  ax.plot(xp,yp,'o',color=colors[r],ms=7);ax.plot(xq,yq,'o',color=colors[r],ms=7)
  ax.text(xp,yp+.15,f'({r},{t})',ha='center',fontsize=10,color=colors[r]);ax.text(xq,yq+.15,f'({u},{v})',ha='center',fontsize=10,color=colors[r])
  ax.add_patch(FancyArrowPatch((xp+.07,yp-.02),(xq-.07,yq-.02),arrowstyle='->',connectionstyle=f'arc3,rad={.06+.025*t}',linewidth=.8,alpha=.62,color=colors[r],mutation_scale=9))
ax.text(1.87,-.05,r'$(u,v)=(r+t,r),\quad(r,t)=(v,u-v)$',ha='center',fontsize=16,color=blue)
ax.text(1.87,-.48,r'$Si_0(f)S^*=M_f\otimes1,\quad S\lambda_sS^*=L_s\otimes1$',ha='center',fontsize=16,color=teal)
ax=fig.add_axes([.64,.095,.32,.38]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(0,1.0,'4  Two full matrix blocks (F20–F22)',weight='bold',fontsize=14,color=blue)
for j,y in enumerate([.64,.36]):
 ax.add_patch(Rectangle((.04,y),.30,.22,facecolor=colors[j],alpha=.13,edgecolor=colors[j],linewidth=2))
 for k in range(1,3):
  ax.plot([.04+k*.1,.04+k*.1],[y,y+.22],color=colors[j],lw=.5);ax.plot([.04,.34],[y+k*.22/3,y+k*.22/3],color=colors[j],lw=.5)
 ax.text(.19,y+.11,r'$M_3$',ha='center',va='center',fontsize=20,color=colors[j])
 ax.text(.41,y+.12,r'$P_1=I_3\oplus0$' if j==0 else r'$P_2=0\oplus I_3$',fontsize=16,color=colors[j])
ax.text(.04,.20,r'$\theta_k=\operatorname{Ad}(Q_k\oplus Q_k)$',fontsize=16,color=blue)
ax.text(.04,.08,r'$Z(N)=\mathbb{C}P_1\oplus\mathbb{C}P_2$',fontsize=16,color=red)
ax.text(.04,-.02,'The dual fixes both central blocks; N is not a factor.',fontsize=11,color=grey)
fig.text(.04,.025,'Exact finite example: Qₖ = diag(1, ω⁻ᵏ, ω⁻²ᵏ),  ω = exp(2πi/3);   QₖLₛQₖ* = ω⁻ᵏˢLₛ.  Abstract proof locators: F5, F16–F22, TR1–TR6.',fontsize=11,color=grey)
fig.savefig(out/'factor-criterion.png',dpi=200,metadata={'Software':'OA-FLOW original L116 renderer'})
fig.savefig(out/'factor-criterion.svg',metadata={'Date':None,'Creator':'OA-FLOW original L116 renderer'})
plt.close(fig)
omega=np.exp(2j*np.pi/3); L=[];Q=[];checks=[]
for s in range(3):
 l=np.zeros((3,3),complex)
 for r in range(3): l[r,(r-s)%3]=1
 L.append(l)
for k in range(3): Q.append(np.diag([omega**(-k*r) for r in range(3)]))
for k in range(3):
 for s in range(3):
  err=float(np.max(np.abs(Q[k]@L[s]@Q[k].conj().T-omega**(-k*s)*L[s])))
  assert err<1e-14;checks.append({'k':k,'s':s,'max_numerical_error':err})
assert len({(x['u'],x['v']) for x in perm})==9
for x in perm: assert ((x['v'],(x['u']-x['v'])%3))==(x['r'],x['t'])
data={'scope':'G=Z/3Z only for the finite coordinate and matrix drawings; upper proof schematic is arbitrary LCA','haar':'counting measure','K_dimension':3,'regular_tensor_dimension':9,'doubled_algebra':'M3 direct sum M3','ambient_matrix_dimension':6,'center_dimension':2,'coordinate_permutation':perm,'shear_inverse_verified':True,'unitary_permutation_matrix_exact':True,'weyl_checks':checks,'dual_character_sign':'negative','P1_diagonal':[1,1,1,0,0,0],'P2_diagonal':[0,0,0,1,1,1],'native_dimensions':[3200,2200],'licence':'original programme CC0-1.0; DejaVu font separate terms'}
(out/'factor-criterion-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'output_dir':str(out),'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.glob('factor-criterion*'))}},indent=2))

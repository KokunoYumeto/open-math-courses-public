"""Original exact M3 model; source CC0, DejaVu components retain their terms."""
from pathlib import Path
import argparse,json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
import sympy as s
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output;out.mkdir(parents=True,exist_ok=True)
W=s.diag(1,s.I,-1);u=-s.I*W;e=s.diag(0,1,0);assert u*e==e and u.adjoint()*u==s.eye(3)
rows=[]
for i in range(3):
 for j in range(3):
  x=s.zeros(3);x[i,j]=1;assert u*x*u.adjoint()==W*x*W.adjoint();rows.append({'i':i+1,'j':j+1,'frequency':i-j,'eigenvalue':str((W*x*W.adjoint())[i,j])})
assert {r['frequency'] for r in rows}=={-2,-1,0,1,2}
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-L126-small-corner-lift','font.size':13})
fig=plt.figure(figsize=(15,10),facecolor='#f5f8fc');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis('off')
navy='#19344e';blue='#176c9a';green='#16765b';orange='#a7511f'
def txt(x,y,t,size=13,**kw):return ax.text(x,y,t,fontsize=size,color=navy,**kw)
def arrow(x,y,X,Y):ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=20,lw=2,color=orange))
txt(7.5,9.6,'A small fixed corner determines a central fixed implementer',22,weight='bold',ha='center')
txt(7.5,9.14,r'$M=M_3(\mathbb{C}),\quad W_s=\mathrm{diag}(1,e^{is},e^{2is}),\quad\alpha_s=\mathrm{Ad}(W_s)$',17,ha='center')
ax.add_patch(Rectangle((.6,6.45),13.8,2.15,facecolor='white',edgecolor='#c6d4df'))
txt(.9,8.22,'Compact spectral image in a noncompact quotient',16,weight='bold')
txt(.9,7.81,r'$\Gamma=\{0\},\quad H/\Gamma=\mathbb{R},\quad S=\{-2,-1,0,1,2\}$',15)
ax.plot([3.4,11.8],[7.14,7.14],color=navy,lw=1.4)
for k in range(-2,3):
 x=7.6+1.6*k;ax.plot(x,7.14,'o',ms=9,color=green if k==0 else blue);txt(x,6.8,str(k),13,ha='center')
ax.plot([7.12,8.08],[7.14,7.14],lw=9,color=green,alpha=.2)
txt(12.0,7.05,'frequency',12)
txt(.9,6.53,'A rank-one fixed corner retains only 0.',12)
txt(.8,5.96,r'Select $e=E_{22}$ in the diagonal fixed algebra $F=Z(F)$',16,weight='bold')
for i in range(3):
 for j in range(3):
  x=1.2+j*.77;y=3.01+(2-i)*.77;sel=(i,j)==(1,1)
  ax.add_patch(Rectangle((x,y),.77,.77,facecolor='#c3e5d8' if sel else 'white',edgecolor=orange if sel else '#b3c4d2',lw=2.5 if sel else 1))
  txt(x+.385,y+.385,'1' if sel else '0',17,ha='center',va='center')
txt(2.35,2.58,r'$eMe=\mathbb{C}e$',15,ha='center')
txt(4.25,5.11,r'$t=\pi/2$',18)
txt(4.25,4.57,r'$\alpha_t^e=\mathrm{id}$',18)
txt(4.25,4.01,r'$\mathrm{Sp}(\alpha_t^e)=\{1\}\subset V(r)$',16)
txt(4.25,3.47,r'Choose the corner unitary $v=e$.',13)
arrow(7.53,4.4,8.6,4.4)
ax.add_patch(Rectangle((8.9,2.86),5.3,2.95,facecolor='white',edgecolor='#c6d4df'))
txt(11.55,5.32,'Unique prescribed lift',16,weight='bold',ha='center')
txt(11.55,4.78,r'$u=\mathrm{diag}(-i,1,i)$',20,ha='center')
txt(11.55,4.22,r'$ue=e,\qquad\mathrm{Ad}(u)=\alpha_t$',16,ha='center')
txt(11.55,3.66,r'$u\in\mathcal{U}(Z(F))$',18,ha='center')
txt(11.55,3.15,'The middle value fixes the global phase.',12,ha='center')
txt(.85,1.94,r'Full spectrum at this time: $\mathrm{Sp}(\alpha_t)=\{1,i,-1,-i\}$',17)
txt(.85,1.44,'The small-spectrum hypothesis concerns one corner. The full action need not be close to the identity.',13)
txt(.85,.94,'Proof: LC0 (full support), LC1 (corner recognition and lifting), LC2–LC3 (compact selection), LC4 (this model).',11.5)
txt(.85,.47,'All nine matrix-unit identities are checked exactly. The finite example does not replace the arbitrary-algebra proof.',11.5)
fig.savefig(out/'corner-lift.png',dpi=200,metadata={'Software':'Original reproducible OA-FLOW figure'});fig.savefig(out/'corner-lift.svg',metadata={'Date':None,'Creator':'Original OA-FLOW illustration'});plt.close(fig)
(out/'corner-lift-data.json').write_text(json.dumps({'frequencies':[-2,-1,0,1,2],'time':'pi/2','corner':[0,1,0],'global_lift':['-i','1','i'],'matrix_unit_checks':rows,'small_spectrum_domain':'operator on eMe','full_spectrum':['1','i','-1','-i'],'all_checks_passed':True},indent=2)+'\n',encoding='utf-8')
font=Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU';shutil.copyfile(font,out/'FONT-LICENSE.txt');print(json.dumps({'passed':True,'pixels':[3000,2000],'matrix_unit_checks':len(rows)}))

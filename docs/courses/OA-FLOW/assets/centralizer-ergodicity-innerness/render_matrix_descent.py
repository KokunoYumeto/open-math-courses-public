"""Exact M2 model and an explicitly cropped bilateral matrix; original CC0 expression."""
from pathlib import Path
import argparse,json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
import sympy as s

p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args();out=args.output;out.mkdir(parents=True,exist_ok=True)
u=s.diag(1,s.I);a=u.adjoint();assert a.adjoint()*a==s.eye(2)
checks=[]
for i in range(2):
 for j in range(2):
  x=s.zeros(2);x[i,j]=1;sigma=u*x*u.adjoint();assert a*sigma==x*a
  for k in range(-3,4):assert a*(u**(-(k-1))*x*u**(k-1))==(u**(-k)*x*u**k)*a
  checks.append({'matrix_unit':[i+1,j+1],'eigenvalue':str(s.simplify(sigma[i,j]))})
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-L124-matrix-descent','font.size':12})
fig=plt.figure(figsize=(15,10),facecolor='#f5f8fc');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis('off')
navy='#17344e';blue='#12628c';green='#18765e';orange='#b34c20'
def text(x,y,t,size=12,**kw):return ax.text(x,y,t,fontsize=size,color=navy,**kw)
def arrow(x1,y1,x2,y2,color=navy):ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=17,lw=1.8,color=color))
text(7.5,9.6,'Read the original implementer from one matrix entry',24,ha='center',weight='bold')
text(7.5,9.16,'Circle eigenunitaries first; exact bilateral matrix extraction second',15,ha='center')
ax.add_patch(Rectangle((.6,7.65),13.8,1.05,facecolor='white',edgecolor='#ced8e4'))
text(.9,8.32,'Faithful circle action on an abelian algebra',14,weight='bold')
text(.9,7.96,'Commuting ergodic automorphisms',13)
arrow(6.0,8.15,7.0,8.15)
text(7.35,8.31,r'$c_n=1$ for every $n\in\mathbb{Z}$',15)
text(7.35,7.96,r'Orthogonal polar sums give a unitary $w\in D_1$',13)
text(.85,7.15,r'$M=M_2(\mathbb{C}),\quad u=\mathrm{diag}(1,i),\quad\sigma=\mathrm{Ad}(u)$',17)
text(.85,6.74,r'$a=u^*=\mathrm{diag}(1,-i),\qquad w=a\otimes U^*$',16)
text(.85,6.3,'Finite window of the infinite bilateral matrix of w',14,weight='bold')
left,bottom,cell=1.25,1.95,.73
indices=list(range(-2,3));marked=None
for ri,k in enumerate(indices):
 for ci,m in enumerate(indices):
  xx=left+ci*cell;yy=bottom+(4-ri)*cell;active=k-m==1
  ax.add_patch(Rectangle((xx,yy),cell,cell,facecolor='#d3eee7' if active else 'white',edgecolor='#aebdcc',lw=1))
  text(xx+cell/2,yy+cell/2,'a' if active else '0',17,ha='center',va='center',weight='bold' if active else 'normal')
  if k==0 and m==-1:marked=(xx,yy)
 for _ in [0]:text(left-.3,bottom+(4-ri+.5)*cell,str(k),13,ha='right',va='center')
for ci,m in enumerate(indices):text(left+(ci+.5)*cell,bottom+5*cell+.19,str(m),13,ha='center')
text(left+2.5*cell,bottom+5*cell+.4,'column m',13,ha='center')
text(.58,bottom+2.5*cell,'row k',13,ha='center',va='center',rotation=90)
mx,my=marked;ax.add_patch(Rectangle((mx,my),cell,cell,fill=False,edgecolor=orange,lw=3))
text(1.15,1.55,'Rows and columns continue in both directions.',11)
text(1.15,1.28,'This crop is not asserted to be a finite unitary.',11)
arrow(left+5*cell+.1,my+cell/2,6.7,4.72,color=orange)
ax.add_patch(Rectangle((6.9,3.2),7.15,2.75,facecolor='white',edgecolor='#ced8e4'))
text(7.2,5.55,r'$w_{km}=0\quad\mathrm{unless}\quad k-m=1$',17)
text(7.2,5.05,r'$wS=Sw\quad\Longrightarrow\quad w_{k,k-1}=a$',16)
text(7.2,4.55,r'$a=w_{0,-1},\qquad a^*a=aa^*=1$',17)
text(7.2,4.04,r'$wD_x=D_xw\quad\Longrightarrow\quad a\sigma(x)=xa$',16)
text(7.2,3.54,r'$\sigma(x)=a^*xa$',19,weight='bold')
text(7.25,2.65,'Exact matrix-unit check',14,weight='bold')
text(7.25,2.19,r'$\sigma(E_{11})=E_{11},\qquad\sigma(E_{22})=E_{22}$',16)
text(7.25,1.73,r'$\sigma(E_{12})=-iE_{12},\qquad\sigma(E_{21})=iE_{21}$',16)
text(7.5,.72,'The carrier argument uses arbitrary projection families; the displayed matrix uses the chosen ℓ²(ℤ) stabilization.',11,ha='center')
text(7.5,.34,'Proof: CE0–CE2 (eigenunitaries), CE3–CE5 (matrix extraction and innerness). Original illustration; no source-book image.',10.5,ha='center')
fig.savefig(out/'matrix-descent.png',dpi=200);fig.savefig(out/'matrix-descent.svg',metadata={'Date':None});plt.close(fig)
data={'original_model':True,'algebra':'M2(C)','u':['1','i'],'a':['1','-i'],'sigma_matrix_units':checks,'infinite_matrix_rule':'w[k,m]=a if k-m=1, otherwise zero','displayed_rows_and_columns':indices,'highlighted_coefficient':[0,-1],'crop_is_not_a_finite_unitary':True,'all4_matrix_unit_intertwining_and_7integer_recurrences_verified':True}
(out/'matrix-descent-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
shutil.copyfile(Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU',out/'FONT-LICENSE.txt')
print(json.dumps({'passed':True,'pixels':[3000,2000],'matrix_unit_checks':4,'integer_recurrences_per_unit':7}))

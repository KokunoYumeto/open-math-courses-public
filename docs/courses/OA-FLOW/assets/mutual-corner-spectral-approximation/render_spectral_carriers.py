"""Original CC0 two-dimensional exact illustration of SC1–SC7; no source image."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sympy as s
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figure');a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
t=s.symbols('t',real=True);z0,z1,c=s.symbols('z0 z1 c',complex=True)
e11=s.Matrix([[1,0],[0,0]]);e22=s.eye(2)-e11;e12=s.Matrix([[0,1],[0,0]]);e21=e12.H;u=s.diag(1,s.exp(s.I*t))
assert s.simplify(u*e12*u.H-s.exp(-s.I*t)*e12)==s.zeros(2)
assert s.simplify(u*e21*u.H-s.exp(s.I*t)*e21)==s.zeros(2)
assert (z0*e12).H*(c*e11)*(z1*e12)==s.conjugate(z0)*c*z1*e22
assert e12*e12.H==e11 and e12.H*e12==e22 and e11*e22==s.zeros(2)
r1,r2=s.Rational(3),s.Rational(2);r0=min(r1,r2)/3;assert 2*r0<min(r1,r2)
model={'action':'alpha_t=Ad diag(1,exp(it)) on M2(C)','positive_vector_frequencies':{'E11':0,'E22':0,'E12':-1,'E21':1},'fixed_algebra':'diagonal M2','ambient_center':'scalar','family':'C E12','left_carrier':'E11','right_carrier':'E22','orthogonal_carriers':True,'both_corner_spectra':[0],'K':[-1],'K_minus_K':[0],'sandwich':'(z0 E12)* (c E11) (z1 E12)=conj(z0)c z1 E22','radii':{'r1':str(r1),'r2':str(r2),'r0':str(r0)},'two_r0_less_than_both':True,'scope':'Exact finite illustration; SC0–SC4 contain the arbitrary-group proof.'}
(a.output/'spectral-carriers-data.json').write_text(json.dumps(model,indent=2)+'\n',encoding='utf8',newline='\n')
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-spectral-carriers-20261005','mathtext.fontset':'dejavusans'})
blue='#245D7E';teal='#208A86';red='#BB503B';gray='#52636D';bg='#F7FAFC'
fig=plt.figure(figsize=(14,9),dpi=200,facecolor=bg);ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,9));ax.axis('off')
ax.text(.5,8.5,'A spectral bridge compares disjoint corners',fontsize=23,color=blue,weight='bold')
ax.text(.5,8.12,'Exact model: '+r'$\alpha_t=\operatorname{Ad}\mathrm{diag}(1,e^{it})$ on $M_2(\mathbb{C})$; positive frequency labels.',fontsize=13,color=gray)
def box(x,y,w,hh,text,color=blue,fs=16):
 ax.add_patch(FancyBboxPatch((x,y),w,hh,boxstyle='round,pad=0.08',linewidth=1.4,edgecolor=color,facecolor='white'))
 ax.text(x+w/2,y+hh/2,text,ha='center',va='center',fontsize=fs,color=color)
def arrow(xy0,xy1,label,yshift=.2,color=teal):
 ax.annotate('',xy=xy1,xytext=xy0,arrowprops={'arrowstyle':'-|>','lw':2,'color':color})
 ax.text((xy0[0]+xy1[0])/2,(xy0[1]+xy1[1])/2+yshift,label,ha='center',fontsize=13,color=color)
ax.text(.5,7.5,'1  The bridge runs from the right carrier to the left carrier',fontsize=15,weight='bold',color=blue)
box(.6,6.15,3.4,.85,r'$p=E_{11}$'+'\nleft carrier; '+r'$p\mathbb{C}^2=\mathbb{C}e_1$',fs=14)
box(9.7,6.15,3.5,.85,r'$q=E_{22}$'+'\nright carrier; '+r'$q\mathbb{C}^2=\mathbb{C}e_2$',fs=14)
arrow((9.5,6.6),(4.2,6.6),r'$y=E_{12}: e_2\mapsto e_1$'+'\nfrequency '+r'$-1$',.24)
ax.text(7,5.85,r'$yy^*=p,\qquad y^*y=q,\qquad pq=0$',ha='center',fontsize=17,color=blue)
ax.text(.5,5.3,'2  A nonzero sandwich transports the zero-frequency corner',fontsize=15,weight='bold',color=blue)
box(.6,4.1,3,.8,r'$x=cE_{11}\ne0$'+'\nfrequency 0',fs=14)
box(9.2,4.1,4,.8,r'$y^*xy=cE_{22}\ne0$'+'\nfrequency 0',color=teal,fs=14)
arrow((3.9,4.5),(8.9,4.5),r'$E_{21}(cE_{11})E_{12}$'+'\n'+r'$+1+0-1=0$',.22)
ax.text(7,3.67,r'$\operatorname{Sp}(\alpha^p)=\{0\}=\operatorname{Sp}(\alpha^q),\quad K-K=\{0\}$',ha='center',fontsize=16,color=teal)
ax.text(.5,3.06,'3  One spectral neighborhood refines both targets',fontsize=15,weight='bold',color=blue)
center=8.1;scale=1.25
for yy,r,label,color in [(2.35,3,r'$A_1=(-3,3)$',blue),(1.72,2,r'$A_2=(-2,2)$',gray),(1.09,2/3,r'$B=(-2/3,2/3)$',teal)]:
 ax.text(.7,yy,label,fontsize=15,color=color,va='center');ax.plot([center-scale*r,center+scale*r],[yy,yy],color=color,lw=4)
 ax.scatter([center-scale*r,center+scale*r],[yy,yy],s=65,facecolor=bg,edgecolor=color,lw=2,zorder=3)
ax.plot([center,center],[.87,2.58],ls=':',color=gray,lw=1)
ax.text(center,.62,'0',fontsize=12,ha='center',color=gray)
ax.text(11.05,1.25,r'$2r_0=4/3<2<3$',ha='center',fontsize=12,color=teal)
ax.text(.5,.28,'Proof locators: SC1–SC4 for arbitrary groups; SC5 / SC6–SC7 for this model. Open circles are excluded endpoints.',fontsize=10.5,color=gray)
fig.savefig(a.output/'spectral-carriers.png',dpi=200,facecolor=bg)
fig.savefig(a.output/'spectral-carriers.svg',metadata={'Date':None},facecolor=bg)
plt.close(fig)
print(json.dumps({'passed_exact_model':True,'output':str(a.output),'pixels':[2800,1800]}))

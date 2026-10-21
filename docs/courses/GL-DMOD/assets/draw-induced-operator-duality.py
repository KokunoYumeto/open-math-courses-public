"""The exact induced comparison square, density calibration and nilpotent residue layers."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sympy as sp
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-ID-20261021','mathtext.fontset':'dejavusans'})
ink='#19384e';blue='#285f97';teal='#008b91';bg='#f4f7fb'
fig=plt.figure(figsize=(16,11),dpi=180,facecolor=bg);ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,16),ylim=(0,11));ax.axis('off')
def box(x,y,w,h,title,formula):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',ec=blue,fc='white',lw=1.5))
 ax.text(x+w/2,y+h-.14,title,ha='center',va='top',fontsize=12.5,color=ink)
 ax.text(x+w/2,y+.33,formula,ha='center',va='center',fontsize=19,color=blue)
def arrow(a,b,label='',dy=.12):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':teal,'lw':2})
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',fontsize=16,color=teal)
ax.text(8,10.57,'Induced coefficients: the actual proper-duality map',ha='center',fontsize=22,weight='bold',color=ink)
box(.7,8.55,5.3,1.05,'Induced ordinary source',r'$I_Y(Rf_*D_XF)$')
box(10,8.55,5.3,1.05,'Induced ordinary target',r'$I_Y(D_YRf_*F)$')
box(.7,6.3,5.3,1.05,'Actual operator source',r'$f_+\mathbb{D}^{\mathrm{r}}_X I_X(F)$')
box(10,6.3,5.3,1.05,'Actual operator target',r'$\mathbb{D}^{\mathrm{r}}_Y f_+ I_X(F)$')
arrow((6.2,9.04),(9.8,9.04),r'$I_Y(\alpha_f(F))$')
arrow((6.2,6.79),(9.8,6.79),r'$\beta_f(I_X(F))$')
arrow((3.35,8.3),(3.35,7.55));ax.text(3.65,7.9,r'$\chi_L^{-1}$',ha='left',fontsize=17,color=teal)
arrow((12.65,8.3),(12.65,7.55));ax.text(12.95,7.9,r'$\chi_R^{-1}$',ha='left',fontsize=17,color=teal)
ax.text(8,7.85,'ID.8–ID.9',ha='center',fontsize=16,color=ink)
ax.text(8,5.85,'Source transpose cancels in transfer; target transpose cancels in the induced dual.',ha='center',fontsize=14,color=ink)
ax.plot([.7,15.3],[5.53,5.53],color='#bccbd8',lw=1)
ax.text(8,5.13,'The density calibration in every current degree, ID.13–ID.14',ha='center',fontsize=17,color=ink)
ax.text(8,4.6,r'$(-1)^{nq}\ [(-1)^r(2\pi i)^{-r}]\ (-1)^{m(q-r)} f_*u$',ha='center',fontsize=22,color=blue)
ax.text(8,3.85,r'$=\ (-1)^{r(q-n)}(2\pi i)^{-r}f_*u\ =\ \tau_f^q(u),\qquad r=n-m$',ha='center',fontsize=21,color=teal)
ax.plot([.7,15.3],[3.46,3.46],color='#bccbd8',lw=1)
ax.text(4.2,3.04,'A nonflat coefficient with four layers, ID.19–ID.20',ha='center',fontsize=15,color=ink)
ax.text(4.2,2.55,r'$F=\mathcal{O}_{\mathbf{C}}/(z^4),\quad f:\mathbf{C}\longrightarrow\{*\}$',ha='center',fontsize=19,color=blue)
ax.text(4.2,1.91,r'$\langle z^i dz,z^j\rangle=\mathrm{Res}_0\,z^{i+j-4}dz$',ha='center',fontsize=19,color=blue)
ax.text(4.2,1.32,r'$=1\ \mathrm{if}\ i+j=3,\quad 0\ \mathrm{otherwise}$',ha='center',fontsize=18,color=teal)
ax.text(4.2,.73,'Proper support is the point {0}; all nilpotent layers remain.',ha='center',fontsize=12.5,color=ink)
# Four rows and columns, with the complete residue value in each cell.
x0,y0,cell=10.1,.72,.48
for i in range(4):
 ax.text(x0-.3,y0+(3-i+.5)*cell,rf'$z^{i}dz$',ha='right',va='center',fontsize=13,color=ink)
 ax.text(x0+(i+.5)*cell,y0+4*cell+.22,rf'$z^{i}$',ha='center',fontsize=13,color=ink)
 for j in range(4):
  val=int(i+j==3);x=x0+j*cell;y=y0+(3-i)*cell
  ax.add_patch(plt.Rectangle((x,y),cell,cell,facecolor='#d7f0ec'if val else'white',edgecolor='#a8becb'))
  ax.text(x+cell/2,y+cell/2,str(val),ha='center',va='center',fontsize=15,color=teal if val else ink)
ax.text(13.8,1.63,r'$\det=1$',ha='center',fontsize=19,color=blue)
ax.text(8,.25,'The diagram represents the proved canonical map; the finite data illustrate the general identities.',ha='center',fontsize=12.5,color=ink)
fig.savefig(r/'induced-operator-duality.png',facecolor=bg);fig.savefig(r/'induced-operator-duality.svg',facecolor=bg,metadata={'Date':None});plt.close(fig)
sgn=lambda k:1 if k%2==0 else -1
edges=[];degrees=[]
for n in range(5):
 for m in range(5):
  rel=n-m
  for q in range(n+1):
   ss,raw,ta=sgn(n*q),sgn(rel),sgn(m*(q-rel));expected=sgn(rel*(q-n));assert ss*raw*ta==expected
   edges.append({'n':n,'m':m,'q':q,'r':rel,'target_type_exists':0<=q-rel<=m,'source_edge':ss,'raw_trace_dimension_sign':raw,'target_augmentation':ta,'composite':ss*raw*ta,'coherent_trace':expected})
   for b in range(-4,5):
    before,after=q-n,(q-rel)-m;assert before==after
    degrees.append({'n':n,'m':m,'q':q,'input_cochain_degree':b,'source_density_degree':before,'target_density_degree':after,'source_evaluation_sign':sgn(before*b),'target_evaluation_sign':sgn(after*b)})
residues=[]
for ell in range(1,13):
 mat=[[int(i+j==ell-1)for j in range(ell)]for i in range(ell)];det=int(sp.Matrix(mat).det());assert det==sgn(ell*(ell-1)//2)
 residues.append({'nilpotent_length':ell,'rows':['z^'+str(i)+' dz'for i in range(ell)],'columns':['z^'+str(j)for j in range(ell)],'residue_matrix':mat,'determinant':det,'all_layers_nonzero_in_pairing':True})
data={'proof':'ID.A--ID.D','finite_samples_are_general_proof':False,'coherent_edge_calibrations':edges,'cochain_evaluation_signs':degrees,'nilpotent_residue_pairings':residues,'figure_nilpotent_length':4,'generator_hypothesis':'coherent ordinary generators near each proper fibre','proper_regularity_or_RH_is_an_additional_assertion':True}
(r/'induced-operator-duality-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

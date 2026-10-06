"""Exact central order correction on two M2 blocks; original CC0 expression."""
from pathlib import Path
import argparse,json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from fractions import Fraction
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);out=p.parse_args().output;out.mkdir(parents=True,exist_ok=True)
b=[[3,1],[-1,-3]];hs=[[b[1-i][j]-b[i][j] for j in range(2)] for i in range(2)];k=[[max(0,-hs[i][j]) for j in range(2)] for i in range(2)];d=[[b[i][j]-k[i][j] for j in range(2)] for i in range(2)]
assert hs==[[-4,-4],[4,4]] and k==[[4,4],[0,0]] and d==[[-1,-3],[-1,-3]]
assert max(abs(x) for row in d for x in row)==max(abs(x) for row in b for x in row)==3
for i in range(2):
 for j in range(2):
  for l in range(2):assert b[i][j]-b[i][l]==d[i][j]-d[i][l]
data={'angle_unit':'pi/32','b':b,'h_swap':hs,'k':k,'d':d,'operator_spectrum_angle_units':[-2,0,2],'epsilon_angle_units':4,'bound_B_angle_units':3,'all_eight_matrix_unit_phase_differences_preserved':True,'model_only_not_general_proof':True}
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-L125-central-order','font.size':12})
fig=plt.figure(figsize=(15,10),facecolor='#f5f8fc');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis('off')
navy='#17344e';blue='#12628c';green='#18765e';orange='#b34c20'
def text(x,y,t,size=12,**kw):return ax.text(x,y,t,fontsize=size,color=navy,**kw)
def arrow(x1,y1,x2,y2):ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=17,lw=1.8,color=navy))
text(7.5,9.55,'Correct in the center; keep the small logarithm',24,ha='center',weight='bold')
text(7.5,9.10,r'$M=M_2(\mathbb{C})\oplus M_2(\mathbb{C})$; the action exchanges the two blocks',15,ha='center')
text(7.5,8.72,r'All displayed eigenvalues are in units of $\pi/32$',13,ha='center')
for i,(x,title,color) in enumerate([(0.7,'Initial logarithm b',blue),(5.4,'Central correction k',orange),(10.1,'Fixed logarithm d',green)]):
 ax.add_patch(Rectangle((x,5.78),4.15,2.50,facecolor='white',edgecolor=color,lw=1.5))
 text(x+2.075,7.93,title,16,ha='center',weight='bold')
 vals=[b,k,d][i]
 for j,label in enumerate(['Block 1','Block 2']):
  yy=7.30-j*.68;text(x+.25,yy,label,12);text(x+1.65,yy,rf'$\mathrm{{diag}}({vals[j][0]},\ {vals[j][1]})$',18)
 if i==1:text(x+2.075,5.96,r'$k=\sup(0,-h_s)$',14,ha='center')
 elif i==2:text(x+2.075,5.96,'The two blocks now agree',12,ha='center')
 else:text(x+2.075,5.96,r'$h_s=(-4I_2,\ 4I_2)$',14,ha='center')
arrow(4.86,6.99,5.3,6.99);arrow(9.57,6.99,10.0,6.99)
text(7.5,5.3,r'$d=b-k,\qquad \alpha_s(d)=d,\qquad \|d\|=\|b\|=3\pi/32$',19,ha='center')
text(.9,4.62,'Exact phase differences on matrix units',17,weight='bold')
text(.9,4.19,r'$\mathrm{Ad}(e^{ib})=\mathrm{Ad}(e^{id}),\qquad \mathrm{Sp}(\mathrm{Ad}(e^{ib}))=\{1,e^{i\pi/16},e^{-i\pi/16}\}$',17)
# Horizontal angular coordinate, not a circular distance distortion.
x0,y0,scale=7.5,3.08,.75
ax.plot([x0-4.6*scale,x0+4.6*scale],[y0,y0],color=navy,lw=1)
ax.plot([x0-4*scale,x0+4*scale],[y0,y0],color='#b3cce3',lw=11,solid_capstyle='butt')
for value in [-4,-2,0,2,4]:
 xx=x0+value*scale;ax.plot([xx,xx],[y0-.13,y0+.13],color=navy,lw=1);text(xx,y0-.46,str(value),12,ha='center')
for value in [-2,0,2]:ax.plot(x0+value*scale,y0,'o',color=green,markersize=11)
for value in [-4,4]:ax.plot(x0+value*scale,y0,'o',markerfacecolor='#f5f8fc',markeredgecolor=blue,markersize=10,mew=2)
text(7.5,3.62,r'$V(\varepsilon)$ with $\varepsilon=\pi/8$: the endpoints are excluded',13,ha='center')
text(7.5,2.23,r'Argument coordinate in units of $\pi/32$; green points are the exact automorphism spectrum',12,ha='center')
ax.add_patch(Rectangle((.7,.65),13.55,1.1,facecolor='white',edgecolor='#ced8e4'))
text(.95,1.32,r'General mechanism: $h_t=\alpha_t(b)-b\in Z(M)_{\mathrm{sa}},\quad k=\sup_t(-h_t)$',16)
text(.95,.91,r'$\alpha_s(k)=h_s+k$ and $-B1\leq b-k\leq B1$ give a fixed implementer $e^{i(b-k)}$',15)
text(7.5,.28,'Exact finite model: CO6. General proof: CO0–CO2. Phase localization: CO3–CO4. Original diagram, CC0.',11,ha='center')
fig.savefig(out/'central-order.png',dpi=200,metadata={'Software':'OA-FLOW original exact model'})
fig.savefig(out/'central-order.svg',metadata={'Date':None,'Creator':'OA-FLOW original exact model'})
(out/'central-order-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
font=Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU';assert font.exists();shutil.copyfile(font,out/'FONT-LICENSE.txt');plt.close(fig)

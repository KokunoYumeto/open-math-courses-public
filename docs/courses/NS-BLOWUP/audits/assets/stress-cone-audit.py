"""Reproduce the schematic for C1–C3; this drawing supplies no proof data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(12,6.2),layout='constrained')
ax,tx=fig.subplots(1,2,gridspec_kw={'width_ratios':[1,1.2]})
ax.set_aspect('equal');ax.set_xlim(-3.8,1.1);ax.set_ylim(-3.3,3.3)
ax.add_patch(Polygon([[0,0],[-3.6,3.0],[-3.6,-3.0]],color='#e5f1fa'))
ax.annotate('',xy=(.9,0),xytext=(-3.7,0),arrowprops={'arrowstyle':'->','color':'#7a8490'})
ax.annotate('',xy=(0,3.1),xytext=(0,-3.1),arrowprops={'arrowstyle':'->','color':'#7a8490'})
ax.text(.55,.18,r'$N$');ax.text(.15,2.9,r'$K$')
for end,label,offset in [((-3,2.5),r'$c_-=-A_cN+u_*K$',(.03,.23)),((-3,-2.5),r'$c_+=-A_cN-u_*K$',(.03,-.45))]:
 ax.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#17659b','lw':2.5})
 ax.text(end[0]+offset[0],end[1]+offset[1],label,color='#174567')
ax.annotate('',xy=(-2.5,.35),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#ab5420','lw':2.5})
ax.text(-3,.65,r'$T=h_+y_+c_++h_-y_-c_-$',color='#934214')
ax.text(-3.4,-.75,r'$h_+,h_-,y_+,y_->0$',fontsize=12)
ax.set_xticks([]);ax.set_yticks([]);ax.set_frame_on(False)
ax.set_title('Reference directions and positive coefficients',fontsize=13,pad=12)
tx.axis('off');tx.set_title('Actual columns retain both errors',fontsize=13,pad=12)
lines=[
 (r'$H_\sigma=h_\sigma(-A_cN-\sigma u_*K+e_\sigma)$',.92,15),
 (r'$|e_\sigma|\leq C_e S_*^{-1/2},\qquad h_\sigma\asymp S_*^{-1/2}$',.80,13),
 ('The original target has a strict margin:',.65,12),
 (r'$T_N<0,\quad |T_K|/u_*\leq(1-\eta_c)(-T_N/A_c)$',.55,12),
 ('C3 controls the full matrix perturbation and proves',.40,12),
 (r'$y_\sigma=(H^{-1}T)_\sigma\geq c\sqrt{S_*}\,|T|>0.$',.30,14),
 ('Both stress components, orientation and Haar factors',.12,11),
 ('are retained in the proof. No profile values are inferred.',.05,11)
]
for s,y,size in lines:tx.text(.02,y,s,fontsize=size,va='center')
fig.suptitle('Two-pulse covariance: the positive representation',fontsize=17)
fig.supxlabel('Schematic reference cone (errors set to zero only in the left drawing).\nArrow lengths are illustrative; C1–C3 give the actual vectors, measures and bounds.',fontsize=10)
for ext in ('png','svg'):fig.savefig(out/f'stress-cone-audit.{ext}',dpi=170,facecolor='white')
plt.close(fig)
print('Wrote stress-cone-audit.png and stress-cone-audit.svg')

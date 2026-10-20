"""Reproduce the exact trace, cubic ramification and residue diagram."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams['svg.hashsalt']='snc-cover-trace-descent'
parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent);args=parser.parse_args()
out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
blue='#2466a3';green='#147e6b';ink='#203d55';muted='#536b83';orange='#bc6828';bg='#f5f8fd'
fig=plt.figure(figsize=(18,14),facecolor=bg)
fig.text(.5,.965,'Finite-cover trace and the actual D-type summand',ha='center',fontsize=25,color=ink)
fig.text(.5,.938,'A. Supplied proper locally projective SNC cover; TC.4–TC.25',ha='center',fontsize=15,color=muted)
box=fig.add_axes([.035,.69,.93,.22]);box.set_axis_off()
box.add_patch(FancyBboxPatch((.01,.02),.98,.95,boxstyle='round,pad=.01',linewidth=1,edgecolor='#adc4da',facecolor='white',transform=box.transAxes))
for x,y,txt in [
 (.19,.74,r'$L$'),(.80,.74,r'$K=h_*h^{-1}L$'),
 (.19,.25,r'$Q_L=\operatorname{im}\epsilon$'),(.80,.25,r'$N=f_*E_\Sigma(*D)$')]:
 box.text(x,y,txt,ha='center',va='center',fontsize=22,color=blue)
for y,lab in [(.78,r'$\iota$'),(.60,r'$r=d^{-1}\operatorname{Tr}$')]:
 if y>.7:
  box.annotate('',(.65,y),(.32,y),arrowprops={'arrowstyle':'->','color':green,'lw':2})
 else:
  box.annotate('',(.32,y),(.65,y),arrowprops={'arrowstyle':'->','color':green,'lw':2})
 box.text(.48,y+.035,lab,ha='center',fontsize=18,color=green)
box.text(.50,.41,r'$r\iota=1,\quad e=\iota r,\quad \epsilon^2=\epsilon$',ha='center',fontsize=19,color=green)
box.plot([.19,.19],[.43,.59],ls=':',color=muted,transform=box.transAxes)
box.plot([.80,.80],[.43,.59],ls=':',color=muted,transform=box.transAxes)
box.text(.12,.49,'DT lift',ha='center',fontsize=11,color=muted)
box.text(.88,.49,'DT lift',ha='center',fontsize=11,color=muted)
for y,left,right,lab in [(.30,.32,.65,'inclusion'),(.12,.65,.32,'projection')]:
 box.annotate('',(right,y),(left,y),arrowprops={'arrowstyle':'->','color':green,'lw':1.5})
 box.text(.48,y+.025,lab,ha='center',fontsize=11,color=green)
fig.text(.5,.66,r'$B_X\otimes_{\mathcal{D}_X}Q_L \simeq j_*(Q_L|_U)$'+'   (TC.21)',ha='center',fontsize=22,color=green)
fig.text(.26,.61,'B. Cubic ramification: a real slice',ha='center',fontsize=16,color=muted)
ax=fig.add_axes([.085,.335,.33,.25],facecolor='white')
x=np.linspace(-1,1,501);ax.plot(x,x**3,color=green,lw=2.5)
ax.axhline(0,color=muted,lw=.5);ax.axvline(0,color=muted,lw=.5);ax.grid(alpha=.14)
ax.set_xlim(-1.05,1.05);ax.set_ylim(-1.05,1.05);ax.set_aspect('equal')
ax.set_xlabel(r'$\operatorname{Re}w$',fontsize=12);ax.set_ylabel(r'$\operatorname{Re}t$',fontsize=12)
ax.text(-.90,.70,r'$t=w^3$',color=green,fontsize=17)
ax.plot([0],[0],'o',markerfacecolor='white',markeredgecolor=orange,markersize=7)
fig.text(.25,.295,'Im w = Im t = 0; equal axes, −1 ≤ w ≤ 1.',ha='center',fontsize=12,color=muted)
fig.text(.25,.274,'The complex punctured-disc covering has degree 3.',ha='center',fontsize=12,color=muted)
fig.text(.70,.61,'C. Exact residues and the index-one projector',ha='center',fontsize=16,color=muted)
for y,txt in [
 (.575,r'$A=\frac{2}{5} I_2+N$'),
 (.520,r'$B=3A-I_2=\frac{1}{5} I_2+3N$'),
 (.470,r'$R_0=\frac{1}{15}I_2+N$'),
 (.425,r'$R_1=\frac{2}{5} I_2+N\quad\longleftarrow\quad a\mapsto wv$'),
 (.380,r'$R_2=\frac{11}{15}I_2+N$'),
 (.325,r'$\epsilon=\operatorname{diag}(0_2,I_2,0_2)$')]:
 fig.text(.70,y,txt,ha='center',fontsize=19,color=green if y in(.425,.325)else blue)
fig.text(.70,.545,'N = [[0, 1], [0, 0]]',ha='center',fontsize=16,color=blue)
fig.text(.5,.225,'Density and normalized trace: TC.40–TC.45',ha='center',fontsize=16,color=muted)
fig.text(.5,.180,r'$J=3w^2,\qquad v=w^{-1}f^*a,\qquad \eta=dw\otimes f^*(dt)^{-1}$',ha='center',fontsize=22,color=blue)
fig.text(.5,.125,r'$\eta\otimes1\otimes3w^3v\ \mapsto\ wv=f^*a\ \mapsto\ a\quad(r)$',ha='center',fontsize=23,color=green)
box.set_xlim(0,1);box.set_ylim(0,1)
fig.text(.5,.065,'All nilpotent entries and the transfer density are retained. Algebraic panels have no metric scale.',ha='center',fontsize=13,color=muted)
fig.savefig(out/'snc-cover-trace-descent.png',dpi=150,metadata={'Software':'Matplotlib'})
fig.savefig(out/'snc-cover-trace-descent.svg',metadata={'Date':None})
plt.close(fig)
data={'equations':['TC.4–TC.9','TC.21–TC.25','TC.40–TC.45'],
 'cover_hypothesis':'Supplied proper locally projective equal-dimensional map, positive finite unramified cover off S, SNC inverse boundary',
 'real_slice':{'w_min':-1,'w_max':1,'t':'w^3','imaginary_coordinates':0,'equal_axes':True,'complex_cover_degree':3},
 'nilpotent':[[0,1],[0,0]],'target_residue_eigenvalue':'2/5','source_residue_eigenvalue':'1/5','source_nilpotent_factor':3,
 'target_image_blocks':['1/15 I2+N','2/5 I2+N','11/15 I2+N'],'projector_blocks':[0,1,0],
 'jacobian':'3 w^2','source_frame':'v=w^-1 f^*a','transfer_unit':'eta tensor 1 tensor 3 w^3 v','normalized_trace_of_unit':'a'}
(out/'snc-cover-trace-descent-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

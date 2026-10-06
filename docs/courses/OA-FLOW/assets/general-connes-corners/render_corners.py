"""Original exact M2 support-orbit model and spectral sandwich; CC0-1.0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.hashsalt':'gcc-corners-20261005'})
OUT=Path(__file__).resolve().parent/'assets';OUT.mkdir(exist_ok=True)
fig=plt.figure(figsize=(15,10),dpi=200,facecolor='#f2f5f8')
fig.text(.055,.952,'A nonfixed support becomes an admissible fixed corner',size=23,weight='bold',color='#17344d')
fig.text(.055,.916,r'Exact $M_2$ model of the orbit-support step; negative labels and arbitrary-group proof kept distinct',size=13,color='#435b70')
def frame(pos,title):
 ax=fig.add_axes(pos);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.add_patch(FancyBboxPatch((.005,.005),.99,.99,boxstyle='round,pad=0.001,rounding_size=0.018',facecolor='white',edgecolor='#bccbd8',lw=1))
 ax.text(.045,.90,title,size=15,weight='bold',color='#17344d');return ax
a=frame([.05,.51,.44,.35],'1  A filtered row has two frequencies')
a.text(.06,.75,r'$\alpha_t=\mathrm{Ad}\,\mathrm{diag}(1,e^{it})$',size=15)
a.text(.06,.61,r'$x=2^{-1/2}(e_{11}+e_{12})$',size=15)
a.text(.06,.46,r'$\alpha_t(x)=2^{-1/2}(e_{11}+e^{-it}e_{12})$',size=14)
a.text(.06,.31,r'$\mathrm{Sp}_\alpha(x)=\{0,1\}$',size=15,color='#116e8d')
a.text(.06,.17,r'$s_r(x)\ \mathrm{is\ not\ fixed}$',size=15,color='#ac402b')
b=frame([.515,.51,.435,.35],'2  The orbit join is fixed')
b.text(.055,.745,r'$r_t=s_r(\alpha_t(x))$',size=15)
b.text(.055,.66,'rₜ = ½ [ [1, exp(−it)],\n             [exp(it), 1] ]',size=13,linespacing=1.4,va='top')
b.text(.055,.47,r'$r_0+r_\pi=I,\qquad e_1=\bigvee_t r_t=I$',size=15)
b.text(.055,.30,'A single support cannot index the Connes intersection.',size=11.5)
b.text(.055,.18,'The complete orbit join can (C24–C25).',size=12)
c=frame([.05,.09,.44,.38],'3  Exact coordinates of the projection matrices')
circle=fig.add_axes([.065,.14,.235,.255]);circle.set_aspect('equal');tt=np.linspace(0,2*np.pi,721);circle.plot(np.cos(tt),np.sin(tt),color='#1985a5',lw=2.4);circle.axhline(0,color='#afbdc9',lw=.7);circle.axvline(0,color='#afbdc9',lw=.7)
circle.scatter([1,-1],[0,0],s=55,color=['#166886','#aa452e'],zorder=3)
circle.annotate(r'$r_0$',(1,0),xytext=(6,8),textcoords='offset points',size=12);circle.annotate(r'$r_\pi$',(-1,0),xytext=(-17,8),textcoords='offset points',size=12)
circle.set_xlim(-1.3,1.3);circle.set_ylim(-1.3,1.3);circle.set_xticks([-1,0,1]);circle.set_yticks([-1,0,1]);circle.tick_params(labelsize=10);circle.set_xlabel(r'$\cos t$',size=12);circle.set_ylabel(r'$\sin t$',size=12);circle.spines[['top','right']].set_visible(False)
c.text(.59,.70,'Each plotted point labels',size=11.5);c.text(.59,.60,'the displayed projection.',size=11.5)
c.text(.59,.44,'Opposite points at 0 and π',size=11.5);c.text(.59,.34,'give orthogonal supports.',size=11.5)
c.text(.59,.17,'Circle line is sampled;\nmatrices and marked\nidentities are exact.',size=10.5,linespacing=1.35,color='#4e6377')
d=frame([.515,.09,.435,.38],'4  The sandwich returns a nonzero witness')
d.text(.055,.73,r'$y=e_{22},\quad z=xyx^*=\frac{1}{2} e_{11}\ne0$',size=15)
d.text(.055,.59,r'$\mathrm{Sp}_\alpha(y)=\mathrm{Sp}_\alpha(z)=\{0\}$',size=14)
d.text(.055,.45,'Product bound: {0,1} + {0} − {0,1}',size=12.5)
d.text(.055,.34,r'$\qquad=\{-1,0,1\}$',size=15,color='#617588')
d.text(.055,.20,'Actual output: {0}, inside the required open O.',size=12,color='#116e8d')
fig.text(.055,.04,'Exact example GCC3–5; general transport C20–C28. Circle coordinates label matrices, not real lines in the complex Hilbert space.',size=10.5,color='#435b70')
fig.savefig(OUT/'fixed-corners.png',metadata={'Software':'Original GCC renderer'})
fig.savefig(OUT/'fixed-corners.svg',metadata={'Date':None,'Creator':'Original GCC renderer'});plt.close(fig)
p=OUT/'fixed-corners.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines())+'\n',encoding='utf-8')
data={'scope':'exact M2 model, not a general-group countability reduction','action':'Ad diag(1,exp(i t))','negative_frequency_labels':{'e11':[0],'e12':[1],'x':[0,1],'y':[0],'z':[0]},'x':'(e11+e12)/sqrt(2)','y':'e22','z':'e11/2','right_support_matrix':'[[1,exp(-it)],[exp(it),1]]/2','r0_plus_rpi':'I','orbit_join':'I','coordinate_map':['cos(t)','sin(t)'],'circle_samples':721,'neighbourhoods':{'U1':['-1/10','11/10'],'V':['-1/10','1/10'],'W':['-13/10','13/10'],'O':['-3/2','3/2'],'closureU1_minus_closureU1':['-6/5','6/5'],'closureV_plus_W':['-7/5','7/5']},'product_bound':[-1,0,1],'actual_output':[0],'native_dimensions':[3000,2000],'proof_locators':['C20','C21','C24','C25','C27','C28','GCC3','GCC4','GCC5'],'all_model_identities_exact':True,'circle_outline_numerically_sampled':True}
(OUT/'fixed-corners-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Original GCC PNG, SVG and exact semantic data rendered.')

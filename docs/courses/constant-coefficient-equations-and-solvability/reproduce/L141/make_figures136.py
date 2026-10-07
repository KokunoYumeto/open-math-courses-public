"""Reproducible exact examples for directional PSH averages; original CC0 art."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OWN=Path(__file__).resolve().parent;OUT=OWN/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':14,'axes.labelsize':12,'svg.fonttype':'none'})
teal='#00838b';navy='#354e68';rose='#b6336a';gold='#ac6a00'
def finish(fig,name):
 for ax in fig.axes:
  ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.14)
 fig.savefig(OUT/(name+'.png'),dpi=160,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig,axes=plt.subplots(1,3,figsize=(18,5.7),gridspec_kw={'width_ratios':[1,1,1.35]})
fig.subplots_adjust(left=.05,right=.985,top=.74,bottom=.23,wspace=.32)
fig.suptitle('Directional limits allow exceptional complex fibers',fontsize=20,y=.97)
fig.text(.5,.895,'Examples A and C: exact fibers of log|sin z₁|; exact envelopes of log|sin z| + log|cos z|',ha='center',fontsize=12)
ax=axes[0];ax.set_title('Projection to the first complex coordinate',pad=15)
ax.axhline(0,color=navy,alpha=.4);ax.axvline(0,color=navy,alpha=.3)
ax.scatter([-math.pi,0,math.pi],[0,0,0],s=80,color=rose,zorder=4)
for x,lab in [(-math.pi,'−π'),(0,'0'),(math.pi,'π')]:ax.annotate(lab,(x,0),xytext=(0,-21),textcoords='offset points',ha='center',color=rose)
ax.scatter([math.pi/6,math.pi/2],[0,0],s=54,color=teal,zorder=5)
ax.annotate('π/6',(math.pi/6,0),xytext=(-20,37),textcoords='offset points',color=teal,arrowprops={'arrowstyle':'-','color':teal})
ax.annotate('π/2',(math.pi/2,0),xytext=(10,20),textcoords='offset points',color=teal,arrowprops={'arrowstyle':'-','color':teal})
ax.set_xlim(-4,4);ax.set_ylim(-1.4,1.4);ax.set_aspect('equal',adjustable='box');ax.set_xlabel('Re ζ₁');ax.set_ylabel('Im ζ₁')
fig.text(.178,.10,'Each red point represents the whole complex z₂ fiber.\nEqual Euclidean coordinate scales; direction y=(0,1).',ha='center',fontsize=11,color=navy)
ax=axes[1];t=np.geomspace(1,100,301)
ax.plot(t,-math.log(2)/t,color=teal,lw=2.5,label='ζ₁=π/6: −log(2)/t')
ax.plot(t,np.zeros_like(t),color=navy,lw=2,label='ζ₁=π/2: 0')
ax.set_xscale('log');ax.set_xlabel('dilation t');ax.set_ylabel('normalized fiber value');ax.set_title('Finite fibers converge to the profile 0',pad=15)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.21),frameon=False,fontsize=11)
ax.text(.06,.10,'ζ₁=kπ: value remains −∞\n(no finite plotted ordinate)',transform=ax.transAxes,color=rose,fontsize=11)
ax=axes[2];s=np.linspace(-2,2,501)
msum=2*np.log(np.cosh(s));m3=np.log(np.cosh(2*s))-math.log(2)
ax.plot(s,msum,color=navy,lw=2,label='M₁(s)+M₂(s)')
ax.plot(s,m3,color=teal,lw=2.4,label='M₃(s)')
ax.plot(s,2*np.abs(s),color=gold,lw=1.8,ls='--',label='H₃(s)=H₁(s)+H₂(s)=2|s|')
ax.scatter([0],[ -math.log(2)],color=teal,zorder=6)
ax.annotate('M₃(0)=−log 2',(0,-math.log(2)),xytext=(.25,-.34),fontsize=11,color=teal,arrowprops={'arrowstyle':'-','color':teal})
ax.set_ylim(-.88,4.18);ax.set_xlabel('imaginary height s');ax.set_ylabel('envelope / indicator');ax.set_title('Indicators add; finite-height maxima differ',pad=15)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.21),frameon=False,fontsize=11)
finish(fig,'fibers-and-indicators')
fig,ax=plt.subplots(figsize=(10.6,6.2));fig.subplots_adjust(left=.11,right=.95,bottom=.21,top=.78)
fig.suptitle('A linearly growing observation ball can retain positive error',fontsize=18,y=.96)
fig.text(.5,.885,'Example B: v(z)=|Im z₁| on C², y=(0,1), ball in R⁴, parameter-window area m(K)=2',ha='center',fontsize=11)
factor=32/(15*math.pi)
ax.plot(t,factor/t,color=teal,lw=2.5,label='radius r(t)=1')
ax.plot(t,factor/np.sqrt(t),color=navy,lw=2.5,label='radius r(t)=√t')
ax.plot(t,np.full_like(t,factor),color=rose,lw=2.5,label='radius r(t)=t')
ax.set_xscale('log');ax.set_xlabel('dilation t (logarithmic scale)');ax.set_ylabel('normalized signed = absolute error')
ax.set_ylim(0,factor*1.12)
ax.text(2,factor*.94,'exact positive limit 32/(15π)',color=rose,fontsize=12)
ax.text(7,factor*.62,'Exact formula: (32/(15π)) r(t)/t\nThe four-dimensional slicing constant is proved in (D34).',color=navy,fontsize=12)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.16),ncol=3,frameon=False,fontsize=11)
finish(fig,'moving-ball-errors')
geometry={'authorship':'GPT-6.1 Sol (OpenAI),Ultra;CC0 1.0','euclidean_metric':True,
 'complex_dimension':2,'observation_ball_real_dimension':4,'direction':[0,1],
 'fibers':{'function':'log|sin z1|','exceptional_set':'z1 in pi Z,all z2 in C','projection':'z1 complex plane; equal real/imaginary scales',
 'visible_exceptional_first_coordinates':['-pi','0','pi'],'finite_first_coordinates':['pi/6','pi/2'],
 'normalized_values':['-log(2)/t','0'],'singular_value':'-infinity,no finite plot value'},
 'indicator_example':{'M1+M2':'2 log cosh s','M3':'log cosh(2s)-log2','H3':'2|s|','height_window':[-2,2]},
 'moving_ball':{'v':'|Im z1|','profile':'0','parameter_window_area':2,'unit_ball_mean_absolute_coordinate':'16/(15pi)',
 'normalized_error':'(32/(15pi))r(t)/t','radii':['1','sqrt(t)','t'],'dilation_range':[1,100],
 'linear_radius_limit':'32/(15pi)','sampling':'301 logarithmically spaced exact formula evaluations'},
 'proof_locators':['Theorem D1;Example A','Theorem D4;Example C','Theorem D3;(D34)–(D35);Example B']}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Two exact-example PNG/SVG pairs and geometry written')

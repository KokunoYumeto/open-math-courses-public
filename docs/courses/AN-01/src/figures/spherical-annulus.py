"""Reproduce Figure 1 in 'Spherical convolution and support control'.

Original figure: GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.
CC0-1.0. Requires numpy and matplotlib; no TeX installation.
Theorem 1.1 gives the exact support 2 <= |x| <= 4 for radii 3 and 1.
The upper panel is the central planar section, not a projection or a
two-dimensional density. Corollary 1.2 gives the probability radius
density r/6 on 2 < r < 4; its integral is exactly one.
Background: John K. Hunter, Notes on Partial Differential Equations
(2014), sections 2.5-2.8. The accompanying lesson gives the full proof.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,
                     'text.usetex':False,'axes.spines.top':False,
                     'axes.spines.right':False})
fig,(geometry,radial)=plt.subplots(2,1,figsize=(5.5,8),facecolor='#faf9f5',
                                 gridspec_kw={'height_ratios':[1.4,1]})
for ax in [geometry,radial]:ax.set_facecolor('#faf9f5')
geometry.add_patch(Circle((0,0),4,facecolor='#b8d8d5',edgecolor='#17656d',linewidth=2))
geometry.add_patch(Circle((0,0),2,facecolor='#faf9f5',edgecolor='#17656d',linewidth=2))
geometry.plot(0,0,'o',color='#173b3e',markersize=4)
geometry.annotate('',xy=(4,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#173b3e','linewidth':1.5})
geometry.text(2.7,.3,'r = 4',fontsize=14,ha='center')
geometry.text(0,-1,'r < 2',ha='center',fontsize=14)
geometry.text(0,2.9,'support',ha='center',fontsize=15,color='#173b3e')
geometry.set(xlim=(-4.6,4.6),ylim=(-4.6,4.6),aspect='equal',
             xlabel='x',ylabel='y',title='Central plane section')
geometry.set_xticks([-4,-2,0,2,4]);geometry.set_yticks([-4,-2,0,2,4])
geometry.tick_params(labelsize=12)
radial.plot([0,2],[0,0],color='#17656d',linewidth=2)
radial.plot([2,4],[1/3,2/3],color='#17656d',linewidth=2.5)
radial.plot([4,4.6],[0,0],color='#17656d',linewidth=2)
radial.fill_between([2,4],[1/3,2/3],color='#b8d8d5',alpha=.85)
radial.scatter([2,4],[1/3,2/3],facecolors='#faf9f5',edgecolors='#17656d',s=65,zorder=4)
radial.text(3,.16,'area = 1',ha='center',fontsize=15,color='#173b3e')
radial.text(3.35,.61,'r / 6',ha='center',fontsize=14,color='#173b3e')
radial.set(xlim=(0,4.6),ylim=(-.03,.79),xlabel='radius r',
           ylabel='radius density',title='Probability normalization')
radial.set_xticks([0,1,2,3,4]);radial.set_yticks([0,1/3,2/3])
radial.set_yticklabels(['0','1/3','2/3'])
radial.tick_params(labelsize=12)
fig.subplots_adjust(left=.17,right=.96,top=.95,bottom=.08,hspace=.46)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180,
            facecolor=fig.get_facecolor(),metadata={'Software':'Matplotlib'})
plt.close(fig)

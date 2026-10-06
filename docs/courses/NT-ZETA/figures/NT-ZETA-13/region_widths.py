"""Original comparison of zero-free-region shapes; CC0 1.0.

The common a=0.02 is illustrative, not a certified zero-free constant.
The RH width is conditional and its boundary line is not zero-free.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
t=np.geomspace(10,1_000_000,700)
l=np.log(t+4)
a=0.02
classical=a/l
vk=a/(l**(2/3)*np.log(l)**(1/3))
plt.rcParams.update({'font.size':16,'axes.spines.top':False,
                     'axes.spines.right':False,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(10.8,5.6))
ax.loglog(t,classical,color='#1f77b4',lw=2.7,label='Classical logarithmic shape')
ax.loglog(t,vk,color='#d65f19',lw=2.7,
          label='Vinogradov–Korobov shape')
ax.loglog(t,np.full_like(t,0.5),color='#4b6f37',lw=2.5,ls='--',
          label='Under RH: open strip 1/2 < σ < 1 (width 1/2)')
ax.set_xlim(10,1_000_000)
ax.set_ylim(0.001,0.85)
ax.set_xlabel('Height t')
ax.set_ylabel('Width to the left of the line σ = 1')
ax.set_title('Comparing zero-free-region widths')
ax.grid(which='major',alpha=0.21)
ax.text(0.035,0.62,'Common coefficient a = 0.02 for the two shapes\nIllustrative normalization; not a numerical zero-exclusion certificate',
        transform=ax.transAxes,fontsize=12.4,va='top',
        bbox={'facecolor':'white','edgecolor':'#d2d2d2','alpha':0.95,'pad':8})
handles,labels=ax.get_legend_handles_labels()
fig.legend(handles,labels,loc='lower left',bbox_to_anchor=(0.07,0.004),
           frameon=False,fontsize=14)
fig.subplots_adjust(left=0.11,right=0.975,top=0.89,bottom=0.265)
fig.savefig(here/'region_widths.png',dpi=180,facecolor='white')
plt.close(fig)
values={'coefficient':a,'height_interval':[10,1_000_000],
        'classical_at_million':float(classical[-1]),
        'vk_at_million':float(vk[-1]),
        'ratio_at_million':float(vk[-1]/classical[-1]),
        'rh_width':0.5,'status':'Illustrative shapes, RH conditional; not certified numerical constants.'}
(here/'region_widths.json').write_text(json.dumps(values,indent=2)+'\n',encoding='utf-8')
print(json.dumps(values))

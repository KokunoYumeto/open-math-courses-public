"""Reproduce the exact profiles, form cancellation and weak trace norms."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':11})
root=Path(__file__).resolve().parents[1]
fig,axes=plt.subplots(1,3,figsize=(16,5.2),gridspec_kw={'width_ratios':[1,1.18,1]})
ax=axes[0];x=np.linspace(0,2,401)
ax.plot(x,np.exp(-x),label='lift w = exp(−x)',lw=2,color='#087f8c')
ax.plot(x,-x,label='local u = −x',lw=2,color='#87929c')
ax.plot(x,-x-np.exp(-x),label='v = u − w',lw=2,color='#ad4265')
ax.scatter([0],[ -1],color='#ad4265',zorder=4)
ax.annotate('v′(0) = 0',xy=(0,-1),xytext=(.55,-.8),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='normal coordinate x',ylabel='exact profile',title='Boundary source removed (SL22)')
ax.legend(loc='lower left',fontsize=9);ax.grid(alpha=.2)
ax=axes[1];ax.axis('off');ax.set_title('The actual form difference (SL12)')
rows=[['Normal principal','0'],['All lower terms','0'],['Tangential principal','δ − h'],['Added mass','μ']]
tab=ax.table(cellText=rows,colLabels=['a − q','remaining coefficient'],loc='center',cellLoc='center',colWidths=[.53,.47])
tab.auto_set_font_size(False);tab.set_fontsize(10);tab.scale(1,2.25)
for (r,c),cell in tab.get_celld().items():
    cell.set_edgecolor('#c8d5da')
    if r==0:cell.set_facecolor('#dbeef0')
ax.text(.5,.12,'The complete mₓ pairing cancels.\nNo boundary functional is discarded.',ha='center',va='center',transform=ax.transAxes,fontsize=10)
ax=axes[2];k=np.arange(1,17)
ax.plot(k,k,'o-',label='L² trace: k',color='#ad4265',ms=4)
ax.plot(k,k/np.sqrt(1+k*k),'s-',label='H⁻¹ᐟ² trace = bound',color='#087f8c',ms=4)
ax.set(xlabel='integer tangential frequency k',ylabel='squared norm',title='Sharp graph trace (SL24)',ylim=(0,17))
ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.2)
fig.subplots_adjust(left=.055,right=.99,bottom=.15,top=.86,wspace=.3)
fig.suptitle('Exact source lifting and the retained weak normal flux',fontsize=16,y=.99)
p=root/'figures/source-lift-and-flux.svg';fig.savefig(p);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps({'svg':'figures/'+p.name,'svg_sha256':sha(p),
 'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'scope':'Exact local profiles SL22, full form cancellation SL12, and integer samples of squared trace norms SL24. No physical-ray claim.'},indent=2)+'\n',encoding='utf-8')
print(p.name, p.stat().st_size)

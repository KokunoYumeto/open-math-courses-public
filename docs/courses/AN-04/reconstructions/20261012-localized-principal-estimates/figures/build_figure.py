"""Reproducible exact formulas for the two independent scales and log margin."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','svg.hashsalt':'an04-localized-principal-estimates','font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,3,figsize=(11,4.5),constrained_layout=True)
d=np.geomspace(.001,1,401)
for values,label,color in [(d*d,'α = δ²','#247248'),(2*d,'{γ, α} = 2δ','#236b94'),(np.full_like(d,2),'Second bracket = 2','#a36521')]:axes[0].loglog(d,values,lw=2.3,label=label,color=color)
axes[0].set(title='Local symbol values',xlabel='Geometric width δ',ylabel='Magnitude',xlim=(.001,1));axes[0].legend(fontsize=8)
lam=np.geomspace(.0001,1,501)
axes[1].loglog(lam,1/np.sqrt(lam),lw=2.3,label='Unnormalized loss λ⁻¹ᐟ²',color='#a36521')
axes[1].loglog(lam,np.sqrt(lam),lw=2.3,label='Normalized gain λ¹ᐟ²',color='#247248')
axes[1].set(title='Derivative normalization',xlabel='Frequency parameter λ',ylabel='Factor',xlim=(.0001,1));axes[1].legend(fontsize=8)
l=np.linspace(.000001,1,601);values=np.sqrt(l)*np.abs(np.log(l));peak=np.exp(-2)
axes[2].plot(l,values,lw=2.3,color='#673a87');axes[2].plot([peak],[2/np.e],'o',color='#673a87')
axes[2].annotate('λ = e⁻²\nmaximum 2/e',(peak,2/np.e),xytext=(.37,.69),arrowprops={'arrowstyle':'->'},fontsize=9)
axes[2].set(title='A strict logarithmic margin',xlabel='Frequency parameter λ',ylabel='λ¹ᐟ² |log λ|',xlim=(0,1),ylim=(0,.83))
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Fix the geometric width first; then decrease the frequency parameter',fontsize=13)
out=HERE/'localized-scales-and-logarithmic-margin.svg';fig.savefig(out,metadata={'Date':None,'Creator':'AN-04 original reproducible figure'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/localized-scales-and-logarithmic-margin.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'actual_formulas':['local α=δ², first bracket=2δ, second bracket=2','unnormalized derivative loss λ^(-1/2), normalized gain λ^(1/2)','λ^(1/2)|log λ| has maximum 2/e at exp(-2)'],'scope':'Exact formulas sampled for illustration; local symbol values are not global operator norms. The independent order of choosing width and frequency is retained.'                           },indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(out),'sha256':sha(out)}))

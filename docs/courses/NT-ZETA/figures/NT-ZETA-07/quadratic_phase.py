"""Original finite quadratic-phase samples; CC0. No claim of a numerical proof."""
from pathlib import Path
import json
from fractions import Fraction as F
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[2]
mp.mp.dps=60;alpha=mp.sqrt(2)
partial=[mp.mpc(0)]
for n in range(1,401):partial.append(partial[-1]+mp.exp(2j*mp.pi*alpha*n*n))
u=[float(mp.frac(alpha*n*n)) for n in range(1,8001)]
counts,edges=np.histogram(u,bins=20,range=(0,1))
plt.rcParams.update({'font.size':13,'axes.titlesize':16,'axes.labelsize':14})
fig,ax=plt.subplots(1,2,figsize=(11.4,5))
ax[0].plot([float(z.real) for z in partial],[float(z.imag) for z in partial],lw=.85,color='#236c66')
ax[0].scatter([0,float(partial[-1].real)],[0,float(partial[-1].imag)],c=['#333333','#9c5833'],s=42,zorder=4)
ax[0].annotate('Start: 0',(0,0),xytext=(3,-16),textcoords='offset points',fontsize=11)
ax[0].annotate('End: N = 400',(float(partial[-1].real),float(partial[-1].imag)),xytext=(-103,-27),textcoords='offset points',fontsize=11,arrowprops={'arrowstyle':'->','color':'#9c5833'},bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax[0].set_aspect('equal',adjustable='datalim');ax[0].margins(.2)
ax[0].set_title(r'Partial sums of $e(\sqrt{2}\,n^2)$')
ax[0].set_xlabel('Real part');ax[0].set_ylabel('Imaginary part');ax[0].grid(alpha=.17)
ax[1].bar((edges[:-1]+edges[1:])/2,counts/8000,width=.046,color='#236c66',alpha=.8)
ax[1].axhline(.05,color='#9c5833',ls='--',lw=1.6,label='Limiting mass per bin: 0.05')
ax[1].set_xlim(0,1);ax[1].set_ylim(0,.08)
ax[1].set_title(r'Fractional parts of $\sqrt{2}\,n^2$; N = 8000')
ax[1].set_xlabel('Twenty equal bins in [0, 1)');ax[1].set_ylabel('Fraction of the sample')
ax[1].legend(fontsize=10,loc='upper center');ax[1].spines[['top','right']].set_visible(False)
fig.tight_layout(pad=1.2);fig.savefig(Path(__file__).with_suffix('.png'),dpi=160)
pair=(F(0),F(1));pairs=[pair]
for operation in 'BAAABA':
    k,l=pair
    pair=(l-F(1,2),k+F(1,2)) if operation=='B' else (k/(2*k+2),(k+l+1)/(2*k+2))
    pairs.append(pair)
assert pair==(F(11,82),F(57,82))
eta=sum(pair)/2-F(1,4);assert eta==F(27,164)<F(1,6)
checks=[]
for x in [1000,10000,100000,1000000]:
    m=int(mp.sqrt(x));D=2*sum(x//n for n in range(1,m+1))-m*m
    delta=mp.mpf(D)-x*mp.log(x)-(2*mp.euler-1)*x
    saw=mp.fsum(mp.frac(mp.mpf(x)/n)-mp.mpf('.5') for n in range(1,m+1))
    checks.append({'x':x,'D':D,'error':mp.nstr(delta,24),'error_plus_twice_sawtooth':mp.nstr(delta+2*saw,24),'normalized_error':mp.nstr(delta/(x**(mp.mpf(1)/3)*mp.log(x)),24)})
receipt={'precision':60,'quadratic_alpha':'sqrt(2)','partial_sum_N':400,'partial_sum_real':mp.nstr(partial[-1].real,30),'partial_sum_imag':mp.nstr(partial[-1].imag,30),'partial_sum_modulus':mp.nstr(abs(partial[-1]),30),'histogram_N':8000,'histogram_counts':counts.tolist(),'exponent_pair_operations':'B, A, A, A, B, A','pairs':[[str(k),str(l)] for k,l in pairs],'zeta_exponent':str(eta),'divisor_examples':checks}
(root/'lesson07_numeric.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))

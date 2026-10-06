"""Original CC0 graph and Gram-point calculations for Hardy's function.

OpenAI GPT-6.1 Sol, Codex, Ultra. The plotted curve is sampled floating-point
data. Gram signs and zero ordinates are separately enclosed with FLINT balls.
No third-party figure, source code or numerical table is redistributed.
"""
from pathlib import Path
import json,hashlib,time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp
import flint
from flint import arb,acb,ctx

root=Path(__file__).resolve().parent
started=time.perf_counter()
ctx.dps=80
mp.mp.dps=50
grid=np.linspace(0,50,2501)
values=np.array([mp.fp.siegelz(float(t)) for t in grid])
assert np.isfinite(values).all()
sample_checks=[]
for t in [0,5,14,25,40,50]:
    exact=mp.siegelz(t)
    err=abs(mp.mpf(mp.fp.siegelz(float(t)))-exact)
    assert err<mp.mpf('1e-11')
    sample_checks.append({'t':t,'value_50_digits':str(exact),'float_error':str(err)})
zeros=[]
for j in range(1,11):
    z=acb.zeta_zero(j)
    assert z.real.contains(arb('0.5'))
    zeros.append({'index':j,'ordinate_ball':str(z.imag),'plotted_ordinate':float(z.imag.mid())})
grams=[]
for n in range(-1,127):
    g=arb.gram_point(n)
    z=acb(arb('0.5'),g).zeta()
    assert z.imag.contains(0)
    # At a Gram point exp(i theta)=(-1)^n, so (-1)^n Z(g_n)=Re zeta.
    sign=1 if z.real>0 else -1 if z.real<0 else 0
    assert sign!=0
    if n<126: assert sign==1
    else: assert sign==-1
    grams.append({'index':n,'gram_point_ball':str(g),
                  'alternating_hardy_value_ball':str(z.real),
                  'gram_sign':sign,'plotted_gram_point':float(g.mid()),
                  'hardy_value_midpoint':((-1)**n)*float(z.real.mid())})

plt.rcParams.update({'font.size':23,'axes.titlesize':25,'axes.labelsize':25})
fig,ax=plt.subplots(figsize=(12,5.4),layout='constrained')
ax.plot(grid,values,color='#1e5675',linewidth=2.3,label=r'$Z(t)$, sampled curve')
ax.axhline(0,color='#333',linewidth=1)
ax.scatter([z['plotted_ordinate'] for z in zeros],[0]*len(zeros),
           s=53,color='#a43e32',zorder=4,label='First ten zero ordinates')
small=[g for g in grams if g['index']<=8]
ax.scatter([g['plotted_gram_point'] for g in small],
           [g['hardy_value_midpoint'] for g in small],
           marker='s',s=55,color='#668530',zorder=4,label='Gram points, indices −1 to 8')
ax.set(xlim=(0,50),xlabel=r'Height $t$',ylabel=r'Hardy’s function $Z(t)$',
       title='Real values and sign changes on the critical line')
ax.grid(alpha=.17)
ax.legend(fontsize=14,loc='lower left',framealpha=.96)
fig.savefig(root/'hardy_z.png',dpi=180)
plt.close(fig)
record={'definition':'Z(t)=exp(i theta(t))*zeta(1/2+it); theta(0)=0, continuous gamma phase',
        'curve':{'interval':[0,50],'samples':2501,'method':'mpmath FP siegelz; six values compared at 50 decimal digits','sample_checks':sample_checks},
        'ball_calculations':{'library':'python-flint','version':flint.__version__,'decimal_precision':80,
                             'zeros':zeros,'gram_points':grams,
                             'gram_law_check':'All indices -1 through 125 have positive alternating value; index 126 has a strictly negative ball.'},
        'licence':'CC0-1.0','authorship':'OpenAI GPT-6.1 Sol, Codex, Ultra',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'figure_sha256':hashlib.sha256((root/'hardy_z.png').read_bytes()).hexdigest(),
        'elapsed_seconds':time.perf_counter()-started}
(root/'hardy_z_calculation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'zeros':zeros,'small_gram_points':grams[:5],'gram_failure':grams[-1],
                  'figure_sha256':record['figure_sha256'],'elapsed_seconds':record['elapsed_seconds']},indent=2))

"""Exact algebraic examples DS36–DS37; no simulated PDE trajectories."""
from pathlib import Path
import hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig, axes = plt.subplots(1,3,figsize=(15,4.7),layout='constrained')
t = np.linspace(-1,1,1001)
beta = np.exp(-4)
gap = beta*(5*(t-.1)**2+.2)
ax = axes[0]
ax.plot(t,gap,color='#146575',lw=2.5,label=r'$e^{-4}[5(t-1/10)^2+1/5]$')
ax.scatter([.1],[beta/5],color='#ac4f20',zorder=5)
ax.annotate(r'minimum $e^{-4}/5$',xy=(.1,beta/5),xytext=(-.8,.04),
            arrowprops={'arrowstyle':'->','color':'#ac4f20'})
ax.set(title='Exact nonnegative gap (DS36)',xlabel=r'normal polynomial variable $t$',
       ylabel='upper bound minus completed expression',ylim=(0,.13))
ax.legend(loc='upper center',fontsize=9)
ax = axes[1]
completed = t*t+.25+beta*(1+t)
upper = (1+5*beta)*(t*t+.25)
ax.plot(t,upper,color='#146575',lw=2.5,label=r'$g(t^2-r)$')
ax.plot(t,completed,color='#ac4f20',lw=2,label=r'$A+(1+t)^2$')
ax.fill_between(t,completed,upper,color='#d8e8e6')
ax.set(title=r'No real roots: $r=-1/4$',xlabel=r'normal polynomial variable $t$',
       ylabel='quadratic value')
ax.legend(fontsize=9)
ax = axes[2]
r1,r2 = 528/31,2080/63
for value,color,label in [(r1,'#146575',r'$\delta=1/32$: $(1,528/31)$'),
                          (r2,'#ac4f20',r'$\delta=1/64$: $(1,2080/63)$')]:
    ax.annotate('',xy=(1,value),xytext=(0,0),
                arrowprops={'arrowstyle':'->','color':color,'lw':2.5})
    ax.scatter([1],[value],color=color,label=label)
ax.set(title='Independent coefficient rows (DS37)',xlabel=r'coefficient of $\Psi$ (normalized)',
       ylabel=r'coefficient of $\partial_\xi\Psi$',
       xlim=(-.08,1.2),ylim=(-1,37))
ax.legend(loc='upper left',fontsize=9)
for ax in axes:
    ax.grid(alpha=.22);ax.set_axisbelow(True)
fig.suptitle('Characteristic completion and commutant independence — exact algebra, not physical rays',fontsize=14)
out = HERE/'characteristic-squares.svg'
fig.savefig(out,metadata={'Date':None,'Creator':'AN-04 original proof illustration'})
plt.close(fig)
check = {'svg':'figures/'+out.name,'svg_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_locators':['DS36','DS37'],'r':-0.25,'gap_minimum':'exp(-4)/5',
    'rows':[['1','528/31'],['1','2080/63']],'determinant':'31216/1953',
    'actually_inspected':False,'depicts_PDE_solution':False}
(HERE.parent/'figure-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':out.name,'bytes':out.stat().st_size}))

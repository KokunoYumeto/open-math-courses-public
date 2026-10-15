"""Reproduce the exact endpoint cap and its retained zero interval."""
from pathlib import Path
import hashlib,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'AN04-ERS-cap'})
E=lambda z:math.exp(-1/z) if z>0 else 0.
ts=[-2.95+i*4.9/980 for i in range(981)]
h=[E(t) for t in ts];rho=[E(t+3)*E(-1.75-t) for t in ts]
fig,axes=plt.subplots(2,1,figsize=(11,6.8),gridspec_kw={'height_ratios':[1.6,1]})
ax=axes[0]
ax.plot(ts,h,color='#17697b',label='old coefficient h(t) = E(t)')
ax.plot(ts,[v+w for v,w in zip(h,rho)],color='#c06b20',linestyle='--',label='new coefficient h(t) + rho(t)')
ax.fill_between(ts,rho,color='#c06b20',alpha=.25,label='nonnegative cap rho(t)')
ax.axvspan(-1.5,1.5,color='#67824b',alpha=.12)
ax.axvline(-1.75,color='#536677',linestyle=':',alpha=.7)
ax.axvline(0,color='#536677',linestyle=':',alpha=.7)
ax.set(xlim=(-2.95,1.95),ylim=(-.02,.65),ylabel='coefficient',title='Exact cap outside the support: positive faces bound the new zero class')
ax.grid(alpha=.15)
ax.legend(loc='upper left',fontsize=9)
ax=axes[1]
ax.axvspan(-1.5,1.5,color='#67824b',alpha=.12)
ax.plot([-2.95,0],[1,1],color='#17697b',lw=5,solid_capstyle='butt')
ax.annotate('',xy=(-2.92,1),xytext=(-2.65,1),arrowprops={'arrowstyle':'->','color':'#17697b','lw':2})
ax.plot([-1.75,0],[0,0],color='#c06b20',lw=5)
ax.plot([-2],[0],'o',color='#283a4c')
ax.annotate('new rank-two endpoint t = -2',xy=(-2,0),xytext=(-2.8,-.52),arrowprops={'arrowstyle':'->','color':'#283a4c'},fontsize=10)
ax.text(-.85,1.16,'old zero interval: t <= 0',ha='center',fontsize=10)
ax.text(-.875,.16,'new retained zero class: [-7/4, 0]',ha='center',fontsize=10)
ax.text(.62,-.58,'shaded: time projection of K',ha='center',color='#526d3b',fontsize=10)
ax.set(xlim=(-2.95,1.95),ylim=(-.8,1.4),yticks=[],xlabel='time t')
ax.set_xticks([-2.75,-2,-1.75,-1.5,0,1.5],labels=['-11/4','-2','-7/4','-3/2','0','3/2'])
ax.grid(axis='x',alpha=.15)
fig.tight_layout(pad=1.4)
out=root/'escape-cap-and-active-fiber.svg'
fig.savefig(out,metadata={'Date':None,'Title':'Endpoint cap outside a compact support','Creator':'Independent CC0 programme figure'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root.parent/'figure-check.json').write_text(json.dumps({
 'svg':'figures/escape-cap-and-active-fiber.svg','svg_sha256':sha(out),
 'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'exact_formulas':{'h':'E(t)','rho':'E(t+3)E(-7/4-t)','cap_positive_interval':['-3','-7/4'],'retained_zero_class':['-7/4','0'],'support_time_projection':['-3/2','3/2'],'rank_two_mark':'-2'},
 'plot_scope':'Samples of exact smooth formulas and exact interval endpoints within the retained work strip; no active-fiber assertion outside that strip.',
 'independent_expression_licence':'CC0-1.0'},indent=2)+'\n',encoding='utf-8')
print('Wrote exact cap/zero-class SVG and reproducible formula record.')

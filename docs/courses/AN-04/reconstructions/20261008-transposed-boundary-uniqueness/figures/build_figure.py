"""Exact support envelope for the terminal adjoint test. Original figure, CC0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-terminal-test-support',
                            'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
P=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,5.1),gridspec_kw={'width_ratios':[1.3,1]})
ts=np.linspace(-.6,2,300)
ax.axhspan(-.6,0,color='#edf0f3')
ax.fill_betweenx(ts,0,2.4-ts,color='#c6e6e7',alpha=.82)
ax.plot(2.4-ts,ts,color='#176879',lw=2)
ax.axhspan(-.5,-.25,color='#9572b3',alpha=.34)
ax.add_patch(Rectangle((0,1.6),.4,.3,facecolor='#d88837',edgecolor='#9b501c',lw=1.5))
ax.axhline(0,color='#6e7b86',ls='--',lw=1)
ax.axhline(2,color='#6e7b86',ls=':',lw=1)
ax.axvline(0,color='#172d3e',lw=2)
ax.text(1.08,1.8,r'$\mathrm{supp}\,\psi$',color='#944812')
ax.text(.83,.65,r'$\mathrm{supp}\,v$ lies inside'+'\n'+r'$q\leq 12/5-t$',color='#135562',ha='center')
ax.text(2.12,-.36,r"$\mathrm{supp}\,\chi'$",color='#482762',ha='center')
ax.text(1.65,-.12,r'$u=0$ for $t<0$',color='#3a4954')
ax.text(.6,2.06,r'$T=2$',color='#3a4954')
ax.set(xlim=(-.08,3.08),ylim=(-.64,2.24),xlabel=r'$q$ (normal space)',ylabel=r'$t$ (time)')
ax.set_xticks([0,.4,1,2,3]);ax.set_yticks([-.5,-.25,0,1,1.6,2])
ax.set_title('A terminal test has compact backward support',fontsize=12)
bx.axis('off')
blocks=[
 (.89,r'$L^*v=\psi$'+'\nSmooth terminal solution; exact adjoint boundary data.'),
 (.62,r'$L^*(\chi v)=\psi+[L^*,\chi]v$'+'\nEvery cutoff error lies below $t=0$.'),
 (.34,r'$(u,[L^*,\chi]v)=0$'+'\nThe given solution vanishes on that earlier band.'),
 (.07,r'$(u,\psi)=0$'+'\nArbitrary target tests prove causal uniqueness.')]
for yy,label in blocks:bx.text(.02,yy,label,va='center',transform=bx.transAxes,fontsize=12,linespacing=1.7,wrap=True)
for y1,y2 in [(.79,.72),(.50,.44),(.23,.17)]:
 bx.annotate('',xy=(.44,y2),xytext=(.44,y1),xycoords='axes fraction',arrowprops={'arrowstyle':'->','color':'#176879','lw':1.5})
fig.suptitle('Transposition compares a distribution with smooth terminal tests',fontsize=15)
fig.tight_layout(rect=(0,0,1,.93),w_pad=2.5)
out=P/'terminal-test-support.svg';fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinates':{'terminal_time':2,'speed_bound':1,'source_q':[0,'2/5'],'source_t':['8/5','19/10'],
 'display_t':['-3/5',2],'envelope':'q <= 12/5 - t','cutoff_derivative_t':['-1/2','-1/4'],'zero_past':'t<0'},
 'depicts_support_bound_not_solution_values':True,'proof_locator':'**F0. Exact coordinates of the figure.**',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'svg_sha256':sha(out)}))

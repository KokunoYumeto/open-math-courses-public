"""Exact functions from Exercises 2–3. Independent illustration, CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-cauchy-extensions-and-jets','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
P=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.8))
q=np.linspace(-1.5,1.5,501)
ax.plot(q,np.exp(-np.abs(q)),color='#16677a',lw=2.6,label=r'even: $e^{-|q|}\in H^1$')
ax.plot([-1.5,0],[0,0],color='#a25630',lw=2.2,ls='--',label=r'zero: $H(q)e^{-q}\notin H^1$')
qpos=np.linspace(0,1.5,251);ax.plot(qpos,np.exp(-qpos),color='#a25630',ls='--',lw=2.2)
ax.scatter([0],[0],s=55,facecolors='white',edgecolors='#a25630',zorder=5)
ax.scatter([0],[1],s=30,color='#a25630',zorder=5)
ax.axvline(0,color='#9caab1',lw=.8)
ax.set(xlim=(-1.5,1.5),ylim=(-.1,1.14),xlabel=r'$q$',ylabel='initial position')
ax.set_title('An energy extension must avoid a jump');ax.legend(loc='lower left',frameon=False,fontsize=10)
t=np.linspace(-1,1,501);tp=np.maximum(t,0)
bx.plot(t,tp,color='#a25630',lw=2.5,label=r'$t_+$: $\partial_t^2t_+=\delta_0$')
bx.plot(t,tp**2,color='#16677a',lw=2.5,ls='--',label=r'$t_+^2$: $\partial_t^2t_+^2=2H$')
bx.axvline(0,color='#9caab1',lw=.8)
bx.set(xlim=(-1,1),ylim=(-.1,1.14),xlabel=r'$t-r$ (here $r=0$)',ylabel='time profile')
bx.set_title('Matching velocity removes the delta');bx.legend(loc='upper left',frameon=False,fontsize=10)
bx.text(-.92,.46,'Labels are exact distribution identities.\nThe delta is not drawn as a function.',fontsize=10,color='#415664')
fig.tight_layout(w_pad=3)
out=P/'cauchy-extensions-and-jets.svg';fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinates':{'q_range':['-3/2','3/2'],'even':'exp(-abs(q))','zero':'H(q) exp(-q)','t_range':[-1,1],'profiles':['max(t,0)','max(t,0)^2']},
 'exact_functions':True,'delta_is_a_distribution_label_not_a_numeric_plot':True,'proof_locator':'**F0. Exact coordinates of the figure.**',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'licence':'CC0-1.0'}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'svg_sha256':sha(out)}))

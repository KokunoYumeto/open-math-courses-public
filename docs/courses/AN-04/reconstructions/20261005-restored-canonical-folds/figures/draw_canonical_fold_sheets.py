"""Exact two-sheet normal slice of the canonical fold relation."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
here=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'svg.fonttype':'path','font.family':'DejaVu Sans'})
fig,axs=plt.subplots(2,1,figsize=(5.8,7.5));blue='#176f91';red='#b14a35'
sm=np.linspace(-1,0,401);sp=np.linspace(0,1,401)
for ax in axs:
    ax.axvline(0,color='#757575',lw=.7);ax.axhline(0,color='#757575',lw=.7)
    ax.grid(alpha=.12);ax.set_xlim(-1.08,1.08);ax.spines[['top','right']].set_visible(False)
    ax.set_xticks([-1,0,1])
axs[0].plot(sm,sm**2,color=red,lw=2.5);axs[0].plot(sp,sp**2,color=blue,lw=2.5)
axs[0].set_ylim(-.06,1.16);axs[0].set_yticks([0,9/16,1]);axs[0].set_yticklabels(['0',r'$9/16$','1'])
axs[0].set_title('Two sheets share the output momentum',fontsize=13,pad=14)
axs[0].set_xlabel(r'Sheet coordinate $s$');axs[0].set_ylabel(r'$p=\xi_1/\rho=s^2$')
axs[0].hlines(9/16,-.75,.75,color='#707070',ls='--',lw=1)
for ss,colour,tx in [(-.75,red,-.94),(.75,blue,.3)]:
    axs[0].plot([ss],[9/16],'o',color=colour,ms=6)
    label=r'$s=-3/4$' if ss<0 else r'$s=3/4$'
    axs[0].annotate(label,(ss,9/16),xytext=(tx,.83),fontsize=12,
                    arrowprops={'arrowstyle':'-','color':colour})
axs[1].plot(sm,-sm**3/3,color=red,lw=2.5);axs[1].plot(sp,-sp**3/3,color=blue,lw=2.5)
axs[1].set_ylim(-.5,.5);axs[1].set_yticks([-1/3,0,1/3]);axs[1].set_yticklabels([r'$-1/3$','0',r'$1/3$'])
axs[1].set_xlabel(r'Input first position $y_1=s$');axs[1].set_ylabel(r'Input last position $y_n=-s^3/3$')
axs[1].set_title('Their input positions are distinct',fontsize=13,pad=14)
axs[1].plot([-.75,.75],[9/64,-9/64],'o',color='#334655',ms=6)
axs[1].annotate(r'$(-3/4,9/64)$',(-.75,9/64),xytext=(-1.02,.38),fontsize=11,
                arrowprops={'arrowstyle':'-','color':red})
axs[1].annotate(r'$(3/4,-9/64)$',(.75,-9/64),xytext=(.05,-.4),fontsize=11,
                arrowprops={'arrowstyle':'-','color':blue})
fig.subplots_adjust(left=.2,right=.98,top=.95,bottom=.085,hspace=.63)
dest=here/'canonical-fold-sheets.svg'
fig.savefig(dest,metadata={'Title':'Two exact input sheets over one canonical fold output',
 'Description':'Normal slice x=0,rho=1, p=s^2, (y1,yn)=(s,-s^3/3), marked s=plus/minus 3/4.',
 'Creator':'AN-04 course author'})
qa=here/'canonical-fold-sheets-qa.png';fig.savefig(qa,dpi=170)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'figure':'figures/'+dest.name,'sha256':sha(dest),'script':Path(__file__).name,
 'script_sha256':sha(Path(__file__)),'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'visual_inspection':'pending','exact_geometry':'s in [-1,1], rho=1, p=s^2; input coordinates (s,-s^3/3); s=plus/minus 3/4 share p=9/16 and give (plus/minus 3/4,minus/plus 9/64).',
 'mathematical_scope':'Fixed-output/spectator normal slice, not bicharacteristic trajectories; formulas (4.1),(6.3)-(6.6), full proof sections 1,4,6.',
 'rendering_guard':'Vector text outlines preserve exact mathematical labels across readers.',
 'license':'CC0 original diagram'}
(here/'figure-record.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':dest.name,'sha256':sha(dest)}))


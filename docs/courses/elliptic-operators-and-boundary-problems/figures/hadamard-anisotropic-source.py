"""Reproduce two exact coordinate sections of the original U020 metric sphere."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
                     'svg.hashsalt':'AN03-U020-anisotropic-source-264'})
fig,axes=plt.subplots(1,2,figsize=(12,8.4))
fig.patch.set_facecolor('#fafaf7')
theta=np.linspace(0,2*np.pi,801)
for ax,second,axis,coordinates in [(axes[0],1,2,(2*np.cos(theta),np.sin(theta))),
                                   (axes[1],3,3,(2*np.cos(theta),3*np.sin(theta)))]:
    ax.set_facecolor('#fafaf7')
    ax.plot(*coordinates,color='#215b78',linewidth=2.7)
    ax.axhline(0,color='#8a8a8a',linewidth=.7);ax.axvline(0,color='#8a8a8a',linewidth=.7)
    ax.scatter([0],[0],color='#9e3131',s=30,zorder=4)
    ax.text(.08,.14,r'$x=y$',fontsize=12,color='#9e3131')
    ax.set_xlabel(r'$x_1-y_1$',fontsize=14)
    ax.set_ylabel(rf'$x_{axis}-y_{axis}$',fontsize=14)
    ax.set_aspect('equal');ax.grid(alpha=.2)
    ax.set_title(r'$x_3=y_3$' if axis==2 else r'$x_2=y_2$',fontsize=15,pad=13)
    ax.set_xticks([-2,0,2]);ax.set_yticks([-second,0,second])
    ax.set_xlim(-2.6,2.6);ax.set_ylim(-second-.45,second+.45)
fig.suptitle('Two exact sections of the metric sphere $r=1$',fontsize=20,fontweight='bold',y=.97)
fig.text(.5,.88,r'$G=\mathrm{diag}(4,1,9),\quad r^2=\frac{(x_1-y_1)^2}{4}+(x_2-y_2)^2+\frac{(x_3-y_3)^2}{9}$',ha='center',fontsize=17)
fig.subplots_adjust(left=.09,right=.96,top=.78,bottom=.40,wspace=.4)
fig.text(.30,.285,r'$(2\cos\theta,\sin\theta,0)$',ha='center',fontsize=13)
fig.text(.77,.285,r'$(2\cos\theta,0,3\sin\theta)$',ha='center',fontsize=13)
fig.text(.5,.19,r'$d\mu(y)=\frac{dy}{6},\quad F_0(r,-1)=\frac{e^{-r}}{4\pi r},\quad(P+1)F_0(r,-1)=6\delta_y$',ha='center',fontsize=17)
fig.text(.5,.105,'The unchanged kernel integrates against dy/6; its coefficient against dy is F₀/6.',ha='center',fontsize=13)
fig.text(.5,.04,'Coordinate sections, not a replacement metric. Exact proof: U020, RK32–RK35 and HE1–HE2.',ha='center',fontsize=10,color='#414141')
stem=OUT/'hadamard-anisotropic-source'
fig.savefig(stem.with_suffix('.png'),dpi=200,metadata={'Software':'U020 exact reproducible diagram'})
fig.savefig(stem.with_suffix('.svg'),metadata={'Date':None,'Creator':'U020 exact reproducible diagram'})
plt.close(fig)
params={'schema_version':1,'kind':'two exact coordinate sections, metric radius one',
        'source_lesson':'elliptic-hadamard-parametrices.md','proof_locators':'RK32–RK35; HE1–HE2',
        'G_diagonal':[4,1,9],'H_diagonal':['1/4','1','1/9'],'metric_radius':1,
        'sections':['(2 cos theta,sin theta,0)','(2 cos theta,0,3 sin theta)'],
        'theta_interval':['0','2pi'],'theta_samples':801,'density':'dy/6','z':-1,
        'original_kernel':'exp(-r)/(4pi r)','identity_mass':'6 delta_y',
        'Lebesgue_coefficient':'F0/6','figure_size_inches':[12,8.4],'dpi':200}
stem.with_suffix('.parameters.json').write_text(json.dumps(params,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

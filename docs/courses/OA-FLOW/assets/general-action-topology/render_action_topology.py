"""Original exact proof diagram and M2 example; deterministic PNG/SVG/data."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'OA-FLOW-AT-original-20261004','axes.spines.top':False,'axes.spines.right':False})

def box(ax,xy,w,h,title,body,color='#eef4fb'):
    x,y=xy
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.018',facecolor=color,edgecolor='#506480',linewidth=1.4))
    ax.text(x+w/2,y+h-.055,title,ha='center',va='top',fontsize=17,fontweight='bold',color='#172d47')
    ax.text(x+w/2,y+h-.13,body,ha='center',va='top',fontsize=14,linespacing=1.5)

def arrow(ax,start,end):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=20,linewidth=1.8,color='#38577a'))

def main(out):
    out.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(16,11),dpi=200,facecolor='white')
    fig.text(.04,.969,'From scalar orbit continuity to the predual and integrated action',fontsize=23,fontweight='bold',color='#172d47')
    fig.text(.04,.929,'AT1–6: arbitrary LCH group and arbitrary W* algebra. The plotted example uses only M₂ and G = ℝ.',fontsize=15,color='#46556a')
    chain=fig.add_axes([.035,.58,.93,.31]);chain.set(xlim=(0,1),ylim=(0,1));chain.axis('off')
    box(chain,(.012,.19),.28,.75,'1. Positive compact averages',r'$F_{f,\omega}(x)=\int f(t)\omega(\alpha_{t^{-1}}x)\,dt$'+'\nContinuous decreasing differences\non one compact support.\nFinite cover + directed upper index\ngive uniform convergence (AT2).')
    box(chain,(.359,.19),.28,.75,'2. Normality before Bochner',r'$F_{f,\omega}\in M_*$'+'\nNF1–4 applies to the proved\nbounded order-normal functional.\n'+r'$\|\rho_sF_f-F_f\|\leq\|L_sf-f\|_1\|\omega\|$'+'\nSo every smoothed vector is in $E_c$.')
    box(chain,(.706,.19),.28,.75,'3. Density gives all vectors',r'$F_{a_V,\omega}\to\omega$ weakly'+'\n$E_c$ is norm closed and linear.\nHahn–Banach makes it weakly closed.\nFour positive vector-series terms\ncover every predual functional.\n'+r'Thus $g\mapsto\omega\circ\alpha_g$ is norm continuous.')
    arrow(chain,(.303,.57),(.348,.57));arrow(chain,(.650,.57),(.695,.57))
    chain.text(.5,.045,'The integral in $M_*$ is justified after order normality; arbitrary directed nets are retained.',ha='center',fontsize=14,color='#172d47')
    ax=fig.add_axes([.08,.20,.40,.28]);t=np.linspace(-1,1,401);nvals=[1,4,16]
    for n,col in zip(nvals,['#2563a0','#008875','#b35725']):
        ax.plot(t,np.cos(t)**2/n,color=col,linewidth=2.5,label=rf'$d_{{{n}}}(t)=\cos^2(t)/{n}$')
        ax.axhline(1/n,color=col,alpha=.55,linewidth=1.2,linestyle='--')
    ax.set(xlim=(-1,1),ylim=(0,1.06),xlabel=r'$t\in C=[-1,1]$',ylabel=r'$d_n(t)$')
    ax.set_title('Exact compact coefficient differences',loc='left',fontsize=18,fontweight='bold',pad=35)
    ax.grid(alpha=.17);ax.legend(loc='upper left',bbox_to_anchor=(-.055,-.27),ncol=3,fontsize=12,frameon=False,columnspacing=1)
    ax.text(.98,1.045,'Dashed lines: exact uniform bounds $1/n$',ha='right',va='bottom',transform=ax.transAxes,fontsize=12)
    eq=fig.add_axes([.545,.13,.405,.36]);eq.set(xlim=(0,1),ylim=(0,1));eq.axis('off')
    eq.text(0,1,'After NR0: bounded-set topology\nand full L¹ maps',va='top',fontsize=17,fontweight='bold',color='#172d47',linespacing=1.3)
    eq.text(0,.77,r'$\omega\alpha_{g_i}(z_i^*z_i)$'+'\n'+r'$\leq\omega\alpha_g(z_i^*z_i)+4C^2\|\omega\alpha_{g_i}-\omega\alpha_g\|$'+'\n\nJoint strong* continuity on each norm ball (AT4).',va='top',fontsize=15,linespacing=1.5)
    eq.text(0,.40,r'$T_fT_h=T_{f*h},\qquad S_fS_h=S_{h*f}$'+'\n'+r'$T_f\alpha_s=T_{R_sf},\quad R_sf(t)=\Delta(s)^{-1}f(ts^{-1})$'+'\n\n'+r'$S_{a_V}\omega\to\omega$ in norm; $T_{a_V}x\to x$ strong*.'+'\nNormal maps and ultraweakly closed kernels (AT5–6).',va='top',fontsize=15,linespacing=1.5)
    fig.text(.08,.054,r'$q=e_{11},\ x_n=I-q/n,\ \omega(x)=\langle xe_1,e_1\rangle,\ \alpha_t=\mathrm{Ad}(R_t),\ R_t=\begin{pmatrix}\cos t&-\sin t\\\sin t&\cos t\end{pmatrix}$',fontsize=15)
    fig.text(.08,.019,'Original illustration · exact plotted formulas, not a reduction of the arbitrary-group theorem · CC0-1.0',fontsize=12,color='#46556a')
    # Matplotlib mathtext does not implement pmatrix: use an equivalent inline entry notation in the figure only.
    fig.texts[-2].set_text(r'$q=e_{11},\ x_n=I-q/n,\ \omega(x)=\langle xe_1,e_1\rangle,\ \alpha_t=\mathrm{Ad}(R_t)$'+';  Rₜ has rows (cos t, −sin t) and (sin t, cos t).')
    fig.savefig(out/'action-topology.png',dpi=200,metadata={'Software':'OA-FLOW original deterministic action-topology renderer'})
    fig.savefig(out/'action-topology.svg',metadata={'Date':None,'Creator':'OA-FLOW original deterministic action-topology renderer'})
    plt.close(fig)
    data={'native_dimensions':[3200,2200],'numeric_example_scope':'M2; real rotation action only. Diagram theorem scope: arbitrary LCH G and arbitrary W* M.','t_interval':[-1,1],'sample_count':len(t),'indices':nvals,'samples':[{'t':float(v),'d_n':{str(n):float(np.cos(v)**2/n) for n in nvals}} for v in t],'exact_uniform_bounds':{str(n):'1/'+str(n) for n in nvals},'compact_kernel':'f(t)=(3/4)(1-t^2) for |t|<=1; f(t)=0 otherwise','mathematical_locators':['AT2 equations AT4–8','AT3 equations AT9–13','AT4 equation AT14','AT5 equations AT16–19','AT6 equations AT20–22'],'terms':'CC0-1.0 to the extent of rights held'}
    (out/'action-topology-data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'figures');main(p.parse_args().output_dir)

"""Exact receiving-map diagram for PD.8-PD.24; no field is numerically sampled."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent.parent/'figures'
HERE.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-GAUGE-F09-potential_difference'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                    'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(19,13),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,19); ax.set_ylim(0,13); ax.axis('off')
ax.text(.65,12.35,'Two actual connections: the potential-wave difference receiver',
        fontsize=25,weight='bold',color='#132b43')
ax.text(.65,11.78,r'$\eta=a-a^{\prime},\quad Z=G-G^{\prime},\quad'
        r'\delta B(s)=\eta(s)-\eta(S),\quad I=[t_-,t_+],\quad s\in[0,S],\quad c>0$',
        fontsize=19,color='#334155')

def box(x,y,w,h,title,lines,color='#e6f0fa',fs=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.16,rounding_size=.13',
                              linewidth=1.2,edgecolor='#87a4c0',facecolor=color))
    ax.text(x+.22,y+h-.42,title,fontsize=18,weight='bold',color='#163654',va='top')
    for i,line in enumerate(lines):
        ax.text(x+.22,y+h-.98-i*.47,line,fontsize=fs,color='#152536',va='top')
def arrow(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,
                                 linewidth=2,color='#56758f'))

box(.7,7.45,8.15,3.55,'PD.8–PD.12 · Every finite heat weight',[
 r'$P_2[\eta]=S^{1/2}W_2(\eta;S)+2\mathcal{F}_2^{\delta,2}$',
 r'$P_1[\eta]=2S^{1/8}W_1(\eta;S)+8S^{1/8}\mathcal{F}_1^{\delta,2}$',
 r'$P_{3/2}[\eta]=\sqrt{2}S^{1/4}W_{3/2}(\eta;S)+4\mathcal{F}_{3/2}^{\delta,2}$',
 r'$P_{5/2}[\eta]=\sqrt{2/3}S^{3/4}W_{5/2}(\eta;S)+(4/3)\mathcal{F}_{5/2}^{\delta,2}$',
 r'Output weights: $1/2,\ 1/8,\ 1/4,\ 3/4$ in $L^2(ds/s)$.'],fs=16)
box(9.65,7.45,8.65,3.55,'PD.3–PD.16 · All five ordered products',[
 r'$N_\delta=\mathcal{B}(\eta,a)+\mathcal{B}(a^{\prime},\eta)$',
 r'$\quad+\mathcal{C}(\eta,a,a)+\mathcal{C}(a^{\prime},\eta,a)$',
 r'$\quad+\mathcal{C}(a^{\prime},a^{\prime},\eta)$',
 r'$\int_0^S W_1(N_\delta;s)\,ds\leq J_\delta$',
 r'$J_\delta$: minimum of the two complete integrated expansions.'],fs=16)
arrow((4.75,7.2),(4.75,6.68)); arrow((13.8,7.2),(13.8,6.68))
box(.7,3.82,8.15,2.7,'PD.18–PD.20 · Full potential difference',[
 r'$U_\delta=W_1(\eta;S)+2P_2[\eta]+2J_\delta$',
 r'$\sup_s W_1(\eta;s)\leq U_\delta$',
 r'$D_\delta=2W_1(\eta;S)+2P_2[\eta]+2J_\delta$',
 r'$\sup_s\|\delta B(s)\|_{\mathsf{S}_c^1}\leq D_\delta$'],color='#e8f5ee',fs=17)
box(9.65,3.82,8.65,2.7,'PD.21a · Projection and the zero heat endpoint',[
 r'$D_{\rm df}^{(1)}=2w_1^{\rm df}+2P_{2,\rm df}^{\delta}+2J_\delta$',
 r'$D_{\rm df}^{(0)}=2(P_{2,\rm df}^{\delta}+S^{1/2}w_2^{\rm df})$',
 r'$\qquad+2(J_\delta+Sw_3^{\rm df})$',
 r'$\sup_s\|P_{\rm df}\delta B(s)\|_{\mathsf{S}_c^1}'
 r'\leq D_{{\rm df},\delta}=\min(D_\delta,D_{\rm df}^{(1)},D_{\rm df}^{(0)})$'],
 color='#e8f5ee',fs=16)
arrow((13.8,3.6),(13.8,3.07))
box(.7,.75,17.6,2.2,'PD.22–PD.24 · Both exact null-product placements',[
 r'$\left\|s\left\|[P_{\rm df}B,\partial u]-[P_{\rm df}B^{\prime},\partial u^{\prime}]'
 r'\right\|_{L^2_{t,x}}\right\|_{L^p(ds/s)}$',
 r'$\quad\leq 2\sqrt{3}\sqrt{2/(\pi c)}\,'
 r'\min\{D_{{\rm df},\delta}Q_p(u)+D_{a^{\prime}}Q_p(\delta u),'
 r'\ D_aQ_p(\delta u)+D_{{\rm df},\delta}Q_p(u^{\prime})\}$',
 r'$u=s^{(m-1)/2}\partial_x^{(m-1)}G,\quad Q_p(u)=\mathcal{F}_m^p,'
 r'\quad Q_p(\delta u)=\mathcal{F}_m^{\delta,p},\quad p=2,\infty.$'],
 color='#fff3dc',fs=17)
ax.text(.75,.25,'Exact proof map; every bracket contraction is over all three spatial labels. '
        'All wave norms include their original Box forcing.',fontsize=13,color='#475569')
fig.savefig(HERE/'f09-potential-difference.png',dpi=160)
fig.savefig(HERE/'f09-potential-difference.svg',metadata={'Date':None})
plt.close(fig)
print('Saved f09-potential-difference.png and .svg')

def build():
    return None

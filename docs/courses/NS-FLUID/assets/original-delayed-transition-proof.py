"""Reproducible diagram of proved original five-mode transfer bounds."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(19,11),facecolor='#f5f7fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.05,.955,'The original delayed transfer: the corrected proof closes',fontsize=23,weight='bold',color='#16283e')
ax.text(.05,.908,r'$K\geq10^{10},\quad 0<\epsilon\leq K^{-100}e^{-10K^{10}}$'
        '\nOriginal coordinates, original clock, all five gates retained. DA1–DA37.',fontsize=15,linespacing=1.65,color='#344e67',va='top')

def box(x,y,w,h,title,lines,fc='#e9f0fa'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.013',fc=fc,ec='#a0b3cb',lw=1.2))
    ax.text(x+.012,y+h-.035,title,fontsize=16,weight='bold',color='#16283e',va='top')
    ax.text(x+.012,y+h-.09,'\n'.join(lines),fontsize=15,color='#203850',va='top',linespacing=1.65)

box(.05,.55,.205,.27,'1. Delay and threshold',[
    r'$0\leq t\leq t_c$',
    r'$c(t_c)=\epsilon^2K^{-10}$',
    r'$0\leq1-a\leq5K^{-20}$',
    r'$\sqrt{d^2+\widetilde a^2}\leq2K^{-10}$',
    'DA12–DA18'])
box(.285,.55,.20,.27,'2. Proved activation',[
    r'$s_0=t_c+K^{-9}$',
    r'$b\geq\epsilon/2$',
    r'$c\geq\epsilon^2K^{100}$',
    r'$\omega=\epsilon^{-2}c\geq K^{100}$',
    'DA19–DA22'])
box(.515,.55,.20,.27,'3. Output begins',[
    r'$t_1=t_c+K^{-1}$',
    r'$\widetilde a(t_1)>1/10$',
    r'$\widetilde a^{\prime}=Kd^2\geq0$',
    'Average only after '+r'$s_0$.',
    'DA23–DA28'])
box(.745,.55,.205,.27,'4. Complete transfer',[
    r'$t_2=t_c+K^{-1/2}$',
    r'$1-\widetilde a\leq4K^{-80}$',
    r'$a^2+b^2+c^2+d^2\leq4K^{-80}$',
    r'All $t\geq t_2$.',
    'DA29–DA37'],fc='#e6f4ed')
for x in [.269,.499,.729]:
    ax.annotate('',xy=(x+.012,.692),xytext=(x-.012,.692),arrowprops=dict(arrowstyle='->',lw=2,color='#476d95'))

box(.05,.205,.435,.275,'The repaired product and energy',[
    r'$M=ad\epsilon^2/c,\quad Z=\widetilde a$',
    r'$M^{\prime}=a^2-d^2-(\epsilon b+\epsilon^2e^{-K^{10}}c+KZ+c^{\prime}/c)M$',
    r'$E=\frac{1}{2}(a^2+b^2+c^2+d^2),\quad E_{\rm corr}=E-\frac{K}{2}MZ$',
    r'$E_{\rm corr}^{\prime}=-KZE_{\rm corr}+\mathcal{R}$',
    'The positive product sign requires the minus energy correction.'],fc='#fff2df')
box(.515,.205,.435,.275,'Every remainder and interval is bounded',[
    r'$|\mathcal{R}|\leq2K^{-89},\quad |E_{\rm corr}-E|\leq\frac{1}{4}K^{-99}$',
    r'On $[s_0,2]$, using the complete DA31 remainder.',
    r'$E(t)\leq e^{-K(t-t_1)/10}+5K^{-89}\quad(t_1\leq t\leq2)$',
    r'$\left|\int_{t_c}^{s_0}(a^2-d^2)\,dt\right|\leq K^{-9}$',
    'The activation gap is estimated separately.'],fc='#e6f4ed')

ax.text(.05,.138,r'$0<\sqrt{2}-t_c\leq(10\log K+2)/K^{10}$'+'  (DA17–DA18)',fontsize=16,color='#16283e')
ax.text(.05,.092,'Human source: Terence Tao, arXiv:1402.0290v3, original equations a-eq–ta-eq and Theorem daet.',fontsize=13,color='#40516a')
ax.text(.05,.058,'This diagram shows proved estimates, not sampled trajectories; box spacing is schematic. The infinite cascade remains a separate calculation.',fontsize=13,color='#40516a')
for suffix in ['png','svg']:
    fig.savefig(R/('original-delayed-transition-proof.'+suffix),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)

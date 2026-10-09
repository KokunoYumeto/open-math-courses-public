"""Exact dependency diagram for VC1–VC10; no numerical proof substitution."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
R=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,11));ax.set_xlim(0,13);ax.set_ylim(0,11);ax.axis('off');fig.subplots_adjust(left=.025,right=.975,bottom=.025,top=.96)
ax.text(6.5,10.65,'The complete principal-velocity estimate',ha='center',fontsize=23,color='#163f51')
ax.text(6.5,10.20,'The original amplitudes, interaction counts and physical frequency gaps all enter the bound.',ha='center',fontsize=12)
def box(x,y,w,h,title,lines,color='#e9f3f7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',lw=1.2,edgecolor='#496878',facecolor=color))
    ax.text(x+w/2,y+h-.24,title,ha='center',va='top',fontsize=14,weight='bold',color='#163f51')
    for j,line in enumerate(lines):ax.text(x+w/2,y+h-.64-.36*j,line,ha='center',va='top',fontsize=14)
def arrow(x1,y1,x2,y2):ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=16,color='#496878',lw=1.4))
box(.2,8.45,6.05,1.35,'Actual amplitudes and label counts — VC2–VC4',[
    r'$\|D(a_Ia_J)\|_\infty\leq B_1\lambda_q^{25},\qquad i_*\leq C_I\lambda_q$',
    r'$6i_*\ \mathrm{positive\ pairs};\quad 432i_*\ \mathrm{ordered\ interactions}$'])
box(6.75,8.45,6.05,1.35,'Original physical gaps — VC1 and VC8',[
    r'$\beta=\alpha N_\Lambda\lambda_q^{b/16}$',
    r'$K_{I,J}>\alpha c_\Lambda\lambda_q^b,\qquad \alpha=2\pi/L$'])
arrow(3.2,8.35,3.2,8.0);arrow(9.75,8.35,9.75,8.0)
box(.2,6.4,6.05,1.5,'Centered opposite-pair error — VC7–VC9',[
    r'$\frac{48\mathcal{T}_1VC_IB_1}{\alpha N_\Lambda}\lambda_q^{26-b/16}$',
    r'$26-b/16\leq-6\quad (b\geq512)$'])
box(6.75,6.4,6.05,1.5,'Full nonopposite-pair error — VC7–VC9',[
    r'$\frac{864\mathcal{T}_1VC_IB_1}{\alpha c_\Lambda}\lambda_q^{26-b}$',
    r'$26-b\leq-486\quad (b\geq512)$'])
arrow(3.2,6.3,5,5.98);arrow(9.75,6.3,8,5.98)
box(.7,4.35,11.6,1.5,'Both original mean errors enter the same full bound — VC9',[
    r'$\mathcal{E}_1\leq C_{\rm vel}\lambda_q^{-6},\qquad C_{\rm vel}=\mathcal{T}_1VC_IB_1[48/(\alpha N_\Lambda)+864/(\alpha c_\Lambda)]$',
    r'$\mathcal{E}_1/\delta\leq C_{\rm vel}\lambda_1^{-3\beta_{\rm reg}}\lambda_q^{-6+2\beta_{\rm reg}b}\leq C_{\rm vel}\lambda_q^{-119/20}$'])
arrow(6.5,4.25,9.75,4.05)
box(.2,2.5,6.05,1.45,'Complete principal mean — AB10 and AB13',[
    r'$3R_{\rm av}=3\rho_0I_0+H\leq2\delta+\delta/800$',
    r'$R_{\rm av}=\sum_i\rho_i\int\chi_i^2$'])
box(6.75,2.5,6.05,1.45,'Constructed finite threshold — VC9',[
    r'$a\geq C_{\rm vel}^{20/119}\quad\Longrightarrow\quad\mathcal{E}_1\leq\delta$',
    'Retain AB12 and the rational separation threshold.'])
arrow(3.2,2.4,5,.0+2.05);arrow(9.75,2.4,8,2.05)
box(.7,.75,11.6,1.18,'Actual principal velocity — VC10',[
    r'$\|w^{(p)}\|_2^2\leq3R_{\rm av}+\mathcal{E}_1\leq(2401/800)\delta,\qquad \|w^{(p)}\|_2\leq49\sqrt{\delta}/\sqrt{800}<2\sqrt{\delta}$'],color='#eaf3df')
ax.text(6.5,.25,'Complete proof: VC1–VC10. Human comparison: Buckmaster–Vicol, arXiv:1709.10033v4, original velocity proposition.\nThe original volume V=L³ and amplitude prefactor remain. This diagram asserts the principal estimate only.',ha='center',va='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(R/f'original-principal-velocity-bound.{ext}',dpi=155,facecolor='white')

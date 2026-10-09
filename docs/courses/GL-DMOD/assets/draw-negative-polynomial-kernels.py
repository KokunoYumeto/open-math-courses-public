from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,FancyBboxPatch
HERE=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,9),facecolor='white')
gs=fig.add_gridspec(1,2,width_ratios=[1,1.35],wspace=.15)
ax=fig.add_subplot(gs[0,0]);bx=fig.add_subplot(gs[0,1])
ax.add_patch(Polygon([[0,0],[0,1],[1,1]],fc='#dfeefa',ec='#457da2',lw=1.8))
ax.plot([.35,.35],[.35,1],color='#cc792d',lw=3)
ax.scatter([.35,.35],[.35,1],color='#cc792d',s=45)
ax.text(.385,.70,'Inner integral: s from v to t',rotation=90,ha='left',va='center',fontsize=11)
ax.text(.24,.89,'0 ≤ r ≤ q ≤ 1',ha='center',fontsize=14)
ax.set_xlim(-.05,1.05);ax.set_ylim(-.05,1.05);ax.set_aspect('equal')
ax.set_xticks([0,.35,1]);ax.set_xticklabels(['0','r(v)','1'])
ax.set_yticks([0,.35,1]);ax.set_yticklabels(['0','q=v parameter','1 (t)'])
ax.set_xlabel('r: v=a+r(t−a)',fontsize=12);ax.set_ylabel('q: s=a+q(t−a)',fontsize=12)
ax.set_title('Exact ordered triangle on a complex segment\nThe parameters r,q are real; t,a may be complex.',fontsize=12)
ax.text(.5,-.23,'Fubini uses the convergent triangle 0≤r≤q≤1.\n'
        'For h ∘ (t h): ∫ᵥᵗ s ds = (t²−v²)/2\n'
        '= t(t−v) − (t−v)²/2, giving t h² − h³.',transform=ax.transAxes,ha='center',va='top',fontsize=11,linespacing=1.5)
bx.axis('off');bx.set_xlim(0,1);bx.set_ylim(0,1)
def box(y,h,txt,c,fs=12):
    bx.add_patch(FancyBboxPatch((.015,y),.97,h,boxstyle='round,pad=.008',fc=c,ec='#466076',lw=1.3))
    bx.text(.5,y+h/2,txt,ha='center',va='center',fontsize=fs,linespacing=1.4)
box(.78,.16,'Exact negative rescaling, K.1\nQⱼ=hʲ Pⱼ h⁻⁽ʲ⁻¹⁾ = σʲ(Pⱼ)h\nAll matrix orders ≤ −1; QⱼQⱼ₋₁=0','#e9f1fc')
box(.50,.19,'Actual analytic kernels, K.2–K.4\nKβ=Σₙ≥0 aβ,n(t,x)(t−s)^(n+|β|)/(n+|β|)!\n'
    '|Kβ| ≤ Bβ |t−s|^|β| / (1−Cβ|t−s|)\n'
    'One η: Cβη<1/2 for the finite matrix list','#edf6e6',11)
box(.25,.17,'Exact convolution, K.6–K.8\n'
    '(−1)ᵏ binom(m+k−1,k)=binom(−m,k)\n'
    'All τ/t and finite ξ/x contractions are retained.\n'
    'V_P V_Q = V_(P∘Q) on a common convex product','#e6f5ec',11)
box(.035,.13,'OPEN: canonical residue/cohomology operator classes,\n'
    'proper-cone action, propagation and singular separation;\n'
    'finite D-type, finite poles, microlocal order and C1','#fff0dc',10.5)
for top,bot in [(.765,.705),(.485,.435),(.235,.18)]:
    bx.annotate('',xy=(.5,bot),xytext=(.5,top),arrowprops=dict(arrowstyle='->',lw=1.7,color='#4e6d82'))
fig.suptitle('Convergent negative-order polynomial kernels with exact convolution signs',fontsize=16,y=.99)
fig.subplots_adjust(bottom=.20,top=.88)
fig.text(.055,.03,'Exact proof: K.1–K.3; ordinary Volterra orientation a→t. No residue normalization or (2πi) factor is assigned at this stage.\n'
         'Free human proof target: Kashiwara–Kawai, HolIII, III.1–III.3 and IV.3–IV.4. The proper-cone/cohomology interface remains explicit.',fontsize=10,color='#435b6d')
fig.savefig(HERE/'negative-polynomial-kernels.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'negative-polynomial-kernels.svg',bbox_inches='tight')
print('Rendered negative-polynomial-kernels.png and .svg')

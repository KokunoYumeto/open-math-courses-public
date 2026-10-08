"""Proof dependency diagram for the independent finite-link argument."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
root = Path(__file__).parent
fig, ax = plt.subplots(figsize=(14, 7.4))
fig.patch.set_facecolor('#fbfcff')
ax.set_facecolor('#fbfcff')
ax.set_xlim(-.45, 12.65)
ax.set_ylim(-1.1, 5.4)
positions = [(0,3.1),(3.2,3.1),(6.4,3.1),(9.6,3.1),
             (9.6,.5),(6.4,.5),(3.2,.5),(0,.5)]
texts = [
    'Original stratum $S$\nTube functions $g_R$\nJoint differential rank (F5)',
    'Compact corner core $P_S$\nAll $g_R\\geq1$\nEvery joint face checked',
    'Rounded smooth core $Q_S$\n$S\\simeq Q_S$ by actual flow\nCoefficient transport (F9)',
    'Smooth compact double $D_S$\n$u:Q_S\\to D_S$, $p:D_S\\to Q_S$\n$pu=\\mathrm{id}$ (F10)',
    'Finite convex cover of $D_S$\nFinite ordered Čech cochains\nActual restrictions (F11)',
    'Ordinary sections on $S$\n$R\\Gamma(S;A^\\vee\\otimes o_S)$\nFinite via core and folding',
    'Compact sections on $S$\n$D_KR\\Gamma_c(S;A)$\n$\\simeq R\\Gamma(S;A^\\vee\\otimes o_S)[d]$',
    'Original compact Whitney link\n$R\\Gamma(L;F)$ is finite\nActual skeleton arrows (F13)']
for k, ((x,y), label) in enumerate(zip(positions,texts)):
    ax.add_patch(FancyBboxPatch((x,y),2.7,1.5,boxstyle='round,pad=.10',
        facecolor='#e8effb' if k<4 else '#f4ebd9', edgecolor='#46688e' if k<4 else '#93743c',lw=1.4))
    ax.text(x+1.35,y+.75,label,ha='center',va='center',fontsize=11,color='#17283c',linespacing=1.8)
for k in range(7):
    x,y=positions[k]; x2,y2=positions[k+1]
    if y==y2:
        start=(x+2.83,y+.75) if x2>x else (x-.13,y+.75)
        end=(x2-.15,y2+.75) if x2>x else (x2+2.85,y2+.75)
    else:
        start=(x+1.35,y-.15); end=(x2+1.35,y2+1.65)
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',lw=1.8,color='#526c88'))
ax.text(6.15,5.05,'Finite link coefficients from Whitney controls and finite smooth cochains',
    ha='center',fontsize=17,color='#17283c')
ax.text(6.15,2.5,'Arrows show proof dependencies. Original strata remain fixed; no subanalytic refinement is imposed.',
    ha='center',fontsize=11,color='#5a6678')
ax.text(6.15,-.38,r'Actual normal map: $F_\nu\ \longrightarrow\ R\Gamma(L;F|_L)$; its fibre remains perfect (F14).',
    ha='center',fontsize=14,color='#17283c')
ax.text(6.15,-.84,'The orientation line $o_S$ is retained; the finite assertion is for field coefficients with finite local ranks.',
    ha='center',fontsize=11,color='#5a6678')
ax.axis('off')
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
fig.savefig(root/'finite-whitney-link-cochains.png',dpi=180)
fig.savefig(root/'finite-whitney-link-cochains.svg')

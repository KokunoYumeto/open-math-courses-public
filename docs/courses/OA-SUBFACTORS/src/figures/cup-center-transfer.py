"""Original cup-center transfer and finite-depth profile ranges. CC0-1.0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path'})
fig=plt.figure(figsize=(6.4,16),dpi=150,facecolor='#f6f8fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def panel(y,h,title,lines,color):
 ax.add_patch(FancyBboxPatch((.055,y),.89,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#8295af'))
 ax.text(.08,y+h-.018,title,fontsize=17,weight='bold',va='top',color='#183956')
 for k,line in enumerate(lines):ax.text(.08,y+h-.053-.032*k,line,fontsize=16,va='top',color='#23384d')
ax.text(.055,.981,'Cup centers and tail profiles',fontsize=23,weight='bold',va='top',color='#183956')
ax.text(.055,.951,'The same ordinary tunnel at every finite depth',fontsize=13.5,color='#52667c')
panel(.746,.174,'The original cup — 68.6',[
 r'$d\,E_{D_0}(c_0)=\kappa$',
 r'$\beta_0:Z(R)\ \longrightarrow\ Z(\mathcal{C}_2)$',
 r'$T_S(\beta_0(r))=Q_\kappa(r)$'],'#e7effa')
panel(.524,.174,'Joint trace transport — 68.7–68.8',[
 r'$\tau(\beta_j(r)\beta_{j+1}(s))=\tau(rs)$',
 r'$B_{j+2}\beta_{j+1}=\beta_j B_j$',
 r'$B_1B_2\beta_1=\mathsf{T}=Q_\kappa P_0$'],'#e6f3eb')
for hi,lo in [(.733,.711),(.510,.488)]:
 ax.annotate('',xy=(.5,lo),xytext=(.5,hi),arrowprops=dict(arrowstyle='->',lw=2,color='#285b86'))
panel(.077,.390,'Exact tail-profile ranges — TP.5–TP.6',[
 r'$l=0:\quad[0,1]_{Z(S)}$',
 r'$l=1:\quad Q_\kappa[0,1]_{Z(R)}$',
 r'$l=2:\quad\mathsf{T}[0,1]_{Z(S)}$',
 r'$l=3:\quad\mathsf{T}Q_\kappa[0,1]_{Z(R)}$',
 r'$l=4:\quad\mathsf{T}^{\,2}[0,1]_{Z(S)}$',
 'Every finite partition includes its full residual.',
 r'$\mathrm{profile\ error}\ \leq\lceil l/2\rceil\delta+2e_b/c$',
 r'$\tau(q_{l,b})\leq c/b$',
 'Physical target control is a separate selection.'],'#fff0e0')
ax.text(.055,.040,'Exact maps and bounds; boxes have no trace-area scale.',fontsize=10.5,color='#52667c')
ax.text(.055,.022,'Proofs: 17.14; 68.6–68.8; TP.5–TP.6. Popa (1994), pp. 213–214.',fontsize=9.2,color='#52667c')
stem='cup-center-transfer';fig.savefig(out/(stem+'.png'),dpi=150);fig.savefig(out/(stem+'.svg'))
p=out/(stem+'.svg');p.write_text(re.sub(r'[ \t]+(?=\r?$)','',p.read_text(),flags=re.M),encoding='utf-8')

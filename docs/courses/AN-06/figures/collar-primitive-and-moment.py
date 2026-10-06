from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN06-collar-primitive-v1'})
fig=plt.figure(figsize=(11,12),facecolor='white')
fig.suptitle('The reflected mass and its next frozen-model coefficient',fontsize=18,y=.98)
ax=fig.add_axes([.06,.50,.88,.42]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.add_patch(FancyBboxPatch((.01,.55),.98,.43,boxstyle='round,pad=.008',fc='#eaf2f8',ec='#a7bdd0'))
ax.text(.5,.92,r'$T_n(s)=\int_s^\infty W_n(2u)\,du,\quad T_n^\prime(s)=-W_n(2s)$',ha='center',fontsize=16)
ax.text(.5,.79,r'$|T_n(s)|\leq C_n(1+s)^{-(n+1)/2},\quad n\geq2$',ha='center',fontsize=16)
ax.text(.5,.66,r'$T_n(0)=\kappa_{n-1},\quad \int_0^\infty T_n(s)\,ds=M_n=\frac{n}{4}(2\pi)^{-n}\omega_n$',ha='center',fontsize=16)
ax.text(.5,.46,r'$b(y,d)=\psi(y,d)a(y,d),\quad d\ \mathrm{points\ inward}$',ha='center',fontsize=14)
ax.text(.5,.35,r'$\int_0^\infty b(y,s/k)W_n(2s)\,ds$',ha='center',fontsize=17)
ax.text(.5,.25,r'$=\ \kappa_{n-1}b(y,0)+k^{-1}\int_0^\infty \partial_d b(y,s/k)T_n(s)\,ds$',ha='center',fontsize=16)
ax.text(.5,.10,r'Fixed $C^1$ weight: normalized error $O(k^{-1})$ in every $n\geq2$',ha='center',fontsize=15)
ax2=fig.add_axes([.12,.15,.48,.28])
k=np.linspace(1,30,500)
M2=1/(8*np.pi)
remainder=M2*(1-1/(np.sqrt(1+4*k*k)+2*k))
assert np.all((remainder>0)&(remainder<M2))
ax2.plot(k,remainder,color='#24678d',lw=2.5,label='Exact exponential model, $a=G=1$')
ax2.axhline(M2,color='#a0452c',ls='--',label=r'$M_2=1/(8\pi)$')
ax2.set_xlabel(r'Spectral radius $k$');ax2.set_ylabel('Remainder after bulk and wall terms')
ax2.set_ylim(.027,.042);ax2.grid(alpha=.2);ax2.legend(loc='lower right',fontsize=10)
ax2.set_title('Exact flat two-dimensional consistency check',fontsize=12,pad=12)
ax3=fig.add_axes([.64,.14,.31,.29]);ax3.axis('off')
ax3.text(.5,.95,'Exact constants',ha='center',fontsize=15)
tbl=ax3.table(cellText=[['2',r'$1/(4\pi)$',r'$1/(8\pi)$'],['3',r'$1/(16\pi)$',r'$1/(8\pi^2)$'],['4',r'$1/(24\pi^2)$',r'$1/(32\pi^2)$']],
 colLabels=[r'$n$',r'$\kappa_{n-1}$',r'$M_n$'],cellLoc='center',bbox=[0,.42,1,.45])
tbl.auto_set_font_size(False);tbl.set_fontsize(12)
for (row,col),cell in tbl.get_celld().items():
 cell.set_edgecolor('white');cell.set_facecolor('#eaf2f8' if row==0 else '#f3f6f8')
ax3.text(.5,.30,'Next model contribution:',ha='center',fontsize=13)
ax3.text(.5,.16,r'$-M_nk^{n-2}\int_{\partial X}\partial_d(\psi a)\,dS_g$',ha='center',fontsize=13)
fig.text(.5,.055,'U029 Lemma 3.2 and Corollary 3.3; exponential check in Section 5. CC0.',ha='center',fontsize=11)
fig.text(.5,.027,'The frozen model does not supply the next coefficient of an arbitrary curved spectral density.',ha='center',fontsize=11)
fig.savefig(OUT/'collar-primitive-and-moment.png',dpi=170,metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 mathematical figure'})
fig.savefig(OUT/'collar-primitive-and-moment.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Description':'Exact primitive identity and next frozen-model coefficient; independently authored CC0. Plot samples the exact fixed-window two-dimensional formula.'})
plt.close(fig)

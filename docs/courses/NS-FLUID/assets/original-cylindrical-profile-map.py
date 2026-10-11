"""Original cylinder coordinates and their exact vorticity dictionary."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':13})
fig=plt.figure(figsize=(15,12),facecolor='#f6f8fb');blue='#173b59';teal='#087f8c';orange='#a45423'
fig.text(.05,.955,'The full cylindrical field determines two different vorticity profiles',fontsize=21,weight='bold',color=blue)
for left,native in [(.08,True),(.60,False)]:
 ax=fig.add_axes([left,.64,.32,.22]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.axvspan(.17,.98,facecolor='#e3f2f5')
 ax.plot([.17,.17],[.08,.95],color=teal,lw=3)
 ax.annotate('',xy=(.98,.17),xytext=(.03,.17),arrowprops={'arrowstyle':'->','color':blue})
 ax.annotate('',xy=(.17,.96),xytext=(.17,.05),arrowprops={'arrowstyle':'->','color':blue})
 ax.plot(.67,.67,'o',color=orange,ms=8)
 ax.plot([.17,.67],[.67,.67],'--',color=orange);ax.plot([.67,.67],[.17,.67],'--',color=orange)
 ax.text(.97,.02,r'$r$' if native else r'$y_2$',ha='right',fontsize=18)
 ax.text(.05,.94,r'$z$' if native else r'$y_1$',fontsize=18)
 ax.text(.17,.02,r'$1$' if native else r'$0$',ha='center',fontsize=15)
 ax.text(.69,.70,r'$(r,z)=(1+\delta b,\delta a)$' if native else r'$(y_1,y_2)=(a,b)$',fontsize=14,ha='center')
 ax.text(.5,1.12,'Original cylinder exterior' if native else 'Original profile half-plane',ha='center',fontsize=17,weight='bold',color=blue)
fig.text(.50,.77,r'$\longrightarrow$',fontsize=35,ha='center',color=teal)
fig.text(.50,.67,r'$\delta=(1-t)^{1+\lambda}>0$',fontsize=17,ha='center',color=blue)
ax=fig.add_axes([.06,.30,.88,.25]);ax.axis('off')
ax.text(0,1.05,'The exact product rule carries one equation into the other',fontsize=18,weight='bold',color=blue)
ax.text(.02,.79,r'$R=1+\delta y_2,\quad \mathcal{D}R=\delta U_2,\quad \Omega=(1-t)\omega_\theta=RQ$',fontsize=21,color=teal)
ax.text(.02,.49,r'$\mathcal{D}\Omega+\Omega=R^{-3}\Phi+\delta U_2\Omega/R$',fontsize=24)
ax.text(.02,.19,r'$\mathcal{D}Q+Q=R^{-4}\Phi,\qquad \partial_{y_1}U_2-\partial_{y_2}U_1=RQ$',fontsize=24)
ax=fig.add_axes([.06,.06,.88,.17]);ax.axis('off')
ax.text(0,1.10,'The full field map retains signed swirl and cylindrical volume',fontsize=18,weight='bold',color=blue)
ax.text(.02,.70,r'$u_\theta=(1-t)^{(\lambda-1)/2}W/R,\quad \Theta=W^2,\quad dV=2\pi R\delta^2\,dy_1dy_2$',fontsize=20,color=teal)
ax.text(.02,.28,r'$\frac{1}{2}\int |u|^2\,dV=\pi(1-t)^{2+4\lambda}\int R|U|^2\,dy+\pi(1-t)^{1+3\lambda}\int W^2/R\,dy$',fontsize=20)
fig.text(.05,.016,'Schematic coordinate spacing; a,b>0. Exact maps: CP1–CP20. Source: Wang, Lai, Gómez-Serrano, Buckmaster, arXiv:2201.06780v3.',fontsize=10.5,color='#546979')
for ext in ['png','svg']:fig.savefig(R/('original-cylindrical-profile-map.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)


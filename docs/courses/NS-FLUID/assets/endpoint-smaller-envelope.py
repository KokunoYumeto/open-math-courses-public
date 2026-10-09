"""Render the exact smaller-envelope and heat-threshold mechanisms."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(13,8.2))
ax.set_xlim(0,13);ax.set_ylim(0,8.2);ax.axis('off')
ax.text(.4,7.75,'A smaller event bound, with the heat threshold retained',fontsize=20,weight='bold')
ax.text(.4,7.24,'Original radial envelopes divided by the displayed factor '+r'$\ell_a$'+'; schematic spacing, inner endpoints may coincide',fontsize=12)
positions=[1,2,3.3,8.2,9.4,11.4]
labels=[r'$A_0-d$',r'$A_0-s_0$',r'$A_0$',r'$B_0$',r'$B_0+s_0$',r'$B_0+\bar d$']
for x,label in zip(positions,labels):
    ax.plot([x,x],[5.35,6.8],ls=':',color='#8993a0',lw=.8)
    ax.text(x,5.1,label,ha='center',fontsize=14)
ax.plot([positions[0],positions[-1]],[6.5,6.5],color='#a4abb4',lw=11,solid_capstyle='butt')
ax.plot([positions[1],positions[-2]],[5.9,5.9],color='#267b6c',lw=11,solid_capstyle='butt')
ax.text(6.2,6.72,'Earlier enclosing shell',ha='center',fontsize=12)
ax.text(6.2,6.1,'Envelope of the actual bump ball',ha='center',fontsize=12)
ax.text(.8,4.6,r'$s_0=r_c^*\leq d<\bar d=\Lambda^{-2}\overline{R}_c/4$',fontsize=17)
ax.text(.8,4.15,r'$L_{s_0}=L_c^*,\qquad q_{s_0}<q_{\rm shell}\quad\Longrightarrow\quad\mathcal{Q}_{\rm opt}<\mathcal{Q}$',fontsize=17)
ax.text(.4,3.47,'The physical frequency cutoff keeps both requirements',fontsize=17,weight='bold')
ax.text(.8,2.95,r'$\mathcal{N}_{\rm opt}^2=\max\{2\mathcal{Q}_{\rm opt},H_0\},\qquad\mathcal{N}^2=\max\{2\mathcal{Q},H_0\}$',fontsize=20)
ax.text(.8,2.27,r'$H_0\geq2\mathcal{Q}$',fontsize=18,color='#82562d')
ax.text(5.2,2.27,'Both cutoffs equal '+r'$H_0$'+'.',fontsize=15)
ax.text(.8,1.66,r'$H_0<2\mathcal{Q}$',fontsize=18,color='#267b6c')
ax.text(5.2,1.66,r'$\mathcal{N}_{\rm opt}^2<\mathcal{N}^2$',fontsize=19)
ax.text(.8,1.03,'Then the complete enstrophy, dissipation and original velocity bounds improve strictly.',fontsize=13)
ax.text(.4,.35,'Proof: 10.1–12.2. Original viscosity, heat contribution and all mixed squares remain in the formulas.',fontsize=11,color='#405066')
out=Path(__file__).with_suffix('')
fig.tight_layout()
fig.savefig(out.with_suffix('.png'),dpi=160)
fig.savefig(out.with_suffix('.svg'))
plt.close(fig)


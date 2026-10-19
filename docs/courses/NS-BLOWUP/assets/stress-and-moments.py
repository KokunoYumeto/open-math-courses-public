"""Recreate the exact section and correction diagram; requires numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none'})
fig=plt.figure(figsize=(14,6.5),facecolor='#f6f8fb')
ax=fig.add_axes([.07,.18,.40,.64],facecolor='white')
x=np.linspace(3,6,250);upper=np.sqrt(2)*(x-3)
ax.fill_between(x,-upper,upper,color='#d2eee9')
ax.plot(x,upper,'--',color='#087f77',linewidth=2)
ax.plot(x,-upper,'--',color='#087f77',linewidth=2)
ax.plot(3,0,'o',mfc='white',mec='#087f77',markersize=8,zorder=3)
ax.axhline(0,color='#8293a5',linewidth=.8);ax.axvline(0,color='#8293a5',linewidth=.8)
ax.set_xlim(1.8,6.1);ax.set_ylim(-4.6,4.6)
ax.set_xticks([2,3,4,5,6]);ax.set_yticks([-4,-2,0,2,4])
ax.set_xlabel(r'Original integrated contribution $p_{s,1}$')
ax.set_ylabel(r'$p_{s,2}$')
ax.set_title(r'Exact cone section: $a=3,\ b_s=0$',pad=14)
ax.text(5,0,'admissible',ha='center',va='center',color='#075b55')
fig.text(.07,.07,r'$p_{s,1}>3,\quad |p_{s,2}|<\sqrt{2}(p_{s,1}-3)$',fontsize=16)
fig.text(.53,.82,'Restore all five original moments',fontsize=20,weight='bold',color='#16263b')
rows=[
    r'$M=\int_0^X U\,dx,\quad I=\int_0^X H\,dx,\quad J=\int_0^X UH\,dx$',
    r'$S=\int_0^X(U^2-E^2/2)\,dx,\quad C_p=\int_0^X E^2/(2x)\,dx$',
    r'Integrands evaluated at $(x,\eta)$.',
    'Two axial bumps + three angular bumps',
    r'$\delta\mathbf{m}(c)\ \longleftrightarrow\ Bc+\mathscr{Q}_\eta(c,c)=d$',
    r'Exact inverse row map: P5.2–P5.3',
    r'Keep $\rho,\ \rho^{3/2},\ e_*f_*,\ \sqrt{2}$ and every quadratic term.',
    'Same exterior profiles, moments and axis pressure',
    'give the same exterior velocity, pressure and stress.'
]
for i,t in enumerate(rows):
    fig.text(.53,.73-.075*i,t,fontsize=14 if i in [0,1,2,6,8] else 16,color='#16263b')
fig.text(.07,.93,'A stress direction and an exact correction map',fontsize=24,weight='bold',color='#16263b')
fig.text(.53,.07,'Dashed cone boundary and its vertex are excluded. P6 and Exercise 5.',fontsize=11,color='#36536b')
fig.savefig(Path(__file__).with_suffix('.svg'),metadata={'Creator':'GPT-6 Astra (OpenAI)','Description':'Exact stress-cone section and five-moment correction map from NS-BLOWUP N2.1.'})
plt.close(fig)

p=Path(__file__).with_suffix(".svg")
t=p.read_text(encoding="utf8")
p.write_text(t.replace('width="1008pt" height="468pt"','width="1400" height="650"'),encoding="utf8")

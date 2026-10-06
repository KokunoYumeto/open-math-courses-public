"""Exact n=1 linear pullbacks of MI1, and their LI1--LI3 receiving maps."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,8),facecolor='#f8fafc')
fig.text(.055,.95,'Linear index transport retains the full original symbol',fontsize=21,weight='bold',color='#0f172a')
fig.text(.055,.90,r'$a(z)=(x+i\xi)/\sqrt{1+x^2+\xi^2},\quad L_+=\mathrm{diag}(2,1/2),\quad L_-=\mathrm{diag}(-2,1/2)$',fontsize=17,color='#334155')
theta=np.linspace(0,2*np.pi,1601)
den=np.sqrt(1+4*np.cos(theta)**2+.25*np.sin(theta)**2)
for j,sign in enumerate((1,-1)):
    ax=fig.add_axes([.08+j*.48,.36,.35,.45],facecolor='white')
    x=sign*2*np.cos(theta)/den
    y=.5*np.sin(theta)/den
    ax.plot(x,y,lw=2.5,color=('#2563eb' if sign==1 else '#7c3aed'))
    for t in (np.pi/4,5*np.pi/4):
        i=int(t/(2*np.pi)*1600)
        ax.annotate('',xy=(x[i+30],y[i+30]),xytext=(x[i],y[i]),
                    arrowprops={'arrowstyle':'-|>','color':('#2563eb' if sign==1 else '#7c3aed'),'lw':2})
    ax.axhline(0,color='#cbd5e1',lw=.8);ax.axvline(0,color='#cbd5e1',lw=.8)
    ax.plot([0],[0],'o',color='#334155',ms=4)
    ax.set_aspect('equal');ax.set_xlim(-1,1);ax.set_ylim(-.65,.65)
    ax.set_xlabel(r'$\mathrm{Re}\,a(L_\pm z)$');ax.set_ylabel(r'$\mathrm{Im}\,a(L_\pm z)$')
    ax.set_title(('det '+('L₊ = +1' if sign==1 else 'L₋ = −1')+'; index '+('+1' if sign==1 else '−1')),fontsize=16,weight='bold')
    ax.grid(alpha=.18)
fig.text(.055,.27,r'$z=(\cos\vartheta,\sin\vartheta),\quad a(L_\pm z)=\frac{\pm2\cos\vartheta+(i/2)\sin\vartheta}{\sqrt{1+4\cos^2\vartheta+(1/4)\sin^2\vartheta}}$',fontsize=18,color='#0f172a')
fig.text(.055,.205,r'$J_L=LJL^T:\quad J_{L_+}=J,\quad J_{L_-}=-J;\qquad \lambda\mapsto\lambda\ \mathrm{or}\ -\lambda$',fontsize=16,color='#334155')
fig.text(.055,.15,'LI2 proves the full product morphism; LI3 retains every term of its defect in the original product.',fontsize=12,color='#475569')
fig.text(.055,.105,'LI1 proves the index sign for every invertible real L by the actual norm-continuous Fredholm paths.',fontsize=12,color='#475569')
fig.text(.055,.06,'Exact 2D symbol-image samples of the original positively oriented unit circle. Arrows follow increasing ϑ.',fontsize=11,color='#475569')
fig.text(.055,.025,'Complete proofs: LP3–LP12, LI1–LI3 and MI1–MI2. Reproducible programme calculation; no novelty claim.',fontsize=10.5,color='#64748b')
for ext in ('png','svg'):
    fig.savefig(OUT/f'matrix-index-linear-maps.{ext}',dpi=180,facecolor=fig.get_facecolor(),
                metadata={'Creator':'Matplotlib programme figure'} if ext=='svg' else {})
plt.close(fig)

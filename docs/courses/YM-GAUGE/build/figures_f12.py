"""Reproducible exact finite-system diagrams for quantum gauge symmetry."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures'
INK='#173f4a';TEAL='#187c78';BLUE='#445fa6';OCHRE='#a75c18';RED='#a24363'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor=fig.get_facecolor())
    fig.savefig(OUT/(name+'.png'),dpi=145,metadata={'Software':'YM-GAUGE reproducible figure'},facecolor=fig.get_facecolor())
    plt.close(fig)
def build():
    OUT.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,
      'axes.labelcolor':INK,'axes.edgecolor':INK,'xtick.color':INK,'ytick.color':INK,
      'svg.hashsalt':'YM-F12-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
    fig=plt.figure(figsize=(11.4,7.8));ax=fig.add_axes((0,0,1,1));ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.text(.04,.95,'Three links, exact constraints, surviving quantum states',fontsize=18,weight='bold')
    vertices=[(.1,.53),(.39,.53),(.245,.81)]
    for idx,((x,y),(lx,ly)) in enumerate(zip(vertices,[(.07,.515),(.402,.515),(.255,.833)]),1):
        ax.plot(x,y,'o',color=INK,ms=9);ax.text(lx,ly,str(idx),fontsize=15,weight='bold')
    for a,b in [(0,1),(1,2),(2,0)]:
        p=np.array(vertices[a]);q=np.array(vertices[b]);delta=q-p
        ax.add_patch(FancyArrowPatch(p+.07*delta,q-.07*delta,arrowstyle='->',mutation_scale=18,lw=2,color=TEAL))
    ax.text(.24,.49,r'$1:1\to2,\ n_1$',ha='center',fontsize=14)
    ax.text(.36,.69,r'$2:2\to3$',fontsize=12);ax.text(.36,.65,r'$n_2$',fontsize=14)
    ax.text(.055,.69,r'$3:3\to1$',fontsize=12);ax.text(.085,.65,r'$n_3$',fontsize=14)
    ax.text(.5,.80,r'$C_1=\hbar(n_3-n_1)$',fontsize=17)
    ax.text(.5,.72,r'$C_2=\hbar(n_1-n_2)$',fontsize=17)
    ax.text(.5,.64,r'$C_3=\hbar(n_2-n_3)$',fontsize=17)
    ax.text(.5,.54,r'$C_1+C_2+C_3=0$',fontsize=16,color=OCHRE)
    ax.text(.05,.405,r'$P_Ne_{(n_1,n_2,n_3)}=e_{(n,n,n)}$ if $n_1=n_2=n_3=n$; otherwise zero.',fontsize=15)
    ax.text(.05,.34,r'Full dimension: $(2N+1)^3$.  Physical dimension: $2N+1$.',fontsize=15)
    ax.text(.05,.255,'For N = 1, the compressed loop moves along the physical basis:',fontsize=13)
    for x,lab in [(.22,r'$|-1\rangle$'),(.48,r'$|0\rangle$'),(.74,r'$|1\rangle$')]:ax.text(x,.17,lab,fontsize=20,ha='center')
    for start,end in [(.29,.41),(.55,.67),(.81,.89)]:
        ax.add_patch(FancyArrowPatch((start,.183),(end,.183),arrowstyle='->',mutation_scale=15,color=BLUE,lw=2))
        ax.text((start+end)/2,.22,r'$W_1$',fontsize=12,ha='center',color=BLUE)
    ax.text(.92,.17,'0',fontsize=20)
    ax.text(.05,.07,r'$H_{N,\rm phys}|n\rangle=3\hbar^2n^2/(2I)|n\rangle$. Proof: Q.9–Q.14; F12.2–F12.3 and F12.8–F12.11.',fontsize=11)
    save(fig,'f12-triangle-constraints')
    fig=plt.figure(figsize=(11.4,8.0));ax=fig.add_axes((.08,.22,.53,.63))
    fig.suptitle('A complete rotation slice and its two signed intersections',fontsize=18,y=.97,weight='bold')
    theta=np.linspace(0,2*np.pi,1001);ax.plot(5*np.cos(theta),5*np.sin(theta),color=BLUE,lw=2)
    ax.axhline(0,color=INK,lw=1);ax.axvline(0,color=INK,lw=1)
    ax.plot([0,6],[0,0],color=TEAL,lw=4);ax.plot([-6,0],[0,0],color=OCHRE,lw=2,ls='--')
    ax.plot([0,3],[0,4],color=BLUE,lw=1,ls=':');ax.plot(3,4,'o',color=BLUE,ms=8)
    ax.annotate(r'$z=(3\ell,4\ell)$',xy=(3,4),xytext=(1.2,5.5),fontsize=12,arrowprops={'arrowstyle':'-','color':BLUE})
    ax.plot([5,-5],[0,0],'o',color=TEAL,ms=7)
    ax.annotate('',xy=(5,2),xytext=(5,.12),arrowprops={'arrowstyle':'->','lw':2,'color':TEAL})
    ax.annotate('',xy=(-5,-2),xytext=(-5,-.12),arrowprops={'arrowstyle':'->','lw':2,'color':OCHRE})
    ax.text(3.4,2.3,r'$\Delta=+5\ell$',color=TEAL,fontsize=12)
    ax.text(-6.25,-2.7,r'$\Delta=-5\ell$',color=OCHRE,fontsize=12)
    ax.plot(0,0,'x',color=RED,ms=9,mew=2);ax.text(.35,-.85,r'$r=0$',color=RED)
    ax.set_xlim(-6.6,6.6);ax.set_ylim(-6.1,6.4);ax.set_aspect('equal');ax.set_xlabel(r'$x/\ell$');ax.set_ylabel(r'$y/\ell$');ax.grid(alpha=.15)
    fig.text(.66,.79,'Positive slice: x > 0, y = 0',fontsize=14,color=TEAL,weight='bold')
    fig.text(.66,.735,'One representative per nonzero orbit.',fontsize=11)
    fig.text(.66,.65,'Unrestricted horizontal slice',fontsize=14,weight='bold')
    fig.text(.66,.595,'Two intersections; signed sum 1 − 1 = 0.',fontsize=11)
    fig.text(.66,.54,'Absolute determinant counts both.',fontsize=11)
    fig.text(.66,.455,'The origin is a fixed orbit.',fontsize=13,color=RED)
    fig.text(.66,.40,'Its slice derivative is zero.',fontsize=11)
    fig.text(.08,.13,r'$dx\,dy=r\,dr\,d\theta$; Haar probability $d\theta/(2\pi)$; invariant integral $2\pi\int_0^\infty rF(r,0)\,dr$.',fontsize=13)
    fig.text(.08,.065,'Exact display coordinates x/ℓ, y/ℓ with the retained length ℓ > 0. Proof: Q.16–Q.20; Solution 4.',fontsize=11)
    fig.text(.08,.025,'Arrows indicate increasing angle; their lengths are schematic.',fontsize=11)
    save(fig,'f12-rotation-slice')
    fig,axs=plt.subplots(1,2,figsize=(11.4,7.6));fig.subplots_adjust(left=.09,right=.96,bottom=.29,top=.71,wspace=.30)
    fig.suptitle('Finite BRST Ward identities: exact coefficient cancellations',fontsize=18,y=.965,weight='bold')
    fig.text(.08,.875,r'Left: $(2/g_{\rm YM}^2)\langle s(\bar c t)\rangle$.  Right: $(2\xi/g_{\rm YM}^2)\langle s(\bar c B)\rangle/i$.',fontsize=13)
    labels=[[r'$i\langle Bt\rangle$',r'$-\langle t^2\rangle/\xi$',r'$-\langle\bar c c\rangle$'],
            [r'$\langle B^2\rangle$',r'$i\langle tB\rangle/\xi$',r'$\langle\bar c c\rangle/\xi$']]
    for ax,vals,labs in zip(axs,[[0,-1,1],[1,0,-1]],labels):
        ax.bar(range(3),vals,color=[BLUE,OCHRE,TEAL],width=.58)
        ax.set_xticks(range(3),labs,fontsize=11);ax.axhline(0,color=INK,lw=1)
        ax.set_ylim(-1.3,1.3);ax.set_yticks([-1,0,1]);ax.set_ylabel('With the stated display multiplier')
        ax.grid(axis='y',alpha=.2)
        for idx,val in enumerate(vals):ax.text(idx,val+(.1 if val>=0 else -.19),str(val),ha='center',fontsize=14)
    fig.text(.08,.195,r'$\langle t^2\rangle=\xi g_{\rm YM}^2/2$,  $\langle B^2\rangle=g_{\rm YM}^2/(2\xi)$,  $\langle\bar c c\rangle=-g_{\rm YM}^2/2$,  $\langle Bt\rangle=0$.',fontsize=13)
    fig.text(.08,.12,'Each sum is zero for every ξ > 0 and real nonzero coupling. No moment factor is discarded.',fontsize=12)
    fig.text(.08,.055,'Exact finite integrals and full boundary proof: B.18–B.21. Second identity: F12.6–F12.7.',fontsize=11)
    save(fig,'f12-ward-cancellation')
    (OUT/'f12-figure-data.json').write_text(json.dumps({'triangle':{'vertices':[1,2,3],'oriented_edges':[[1,2],[2,3],[3,1]],'charges_divided_by_hbar':['n3-n1','n1-n2','n2-n3'],'physical_labels':'(n,n,n), -N<=n<=N'},
      'rotation':{'display_map':'x/ell,y/ell; ell>0 retained','point':[3,4],'radius':5,'theta':theta.tolist(),'x_over_ell':(5*np.cos(theta)).tolist(),'y_over_ell':(5*np.sin(theta)).tolist()},
      'ward':{'exact_display_values':[[0,-1,1],[1,0,-1]],'multipliers':['2/gYM²','2xi/(i gYM²)'],'proof_locators':['B.18–B.21','F12.6–F12.7']}},separators=(',',':'))+'\n',encoding='utf8')
if __name__=='__main__':build()

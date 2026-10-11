"""Exact relative quotient and central return diagram; no sampled geometry."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw(output):
    fig = plt.figure(figsize=(9, 22), dpi=100, facecolor='#f6f8fb')
    ax = fig.add_axes([0,0,1,1])
    ax.set(xlim=(0,900), ylim=(2200,0)); ax.axis('off')
    ink,edge = '#193750','#527c9f'
    ax.text(450,55,'The relative cyclic quotient',ha='center',fontsize=24,weight='bold',color=ink)
    ax.text(450,93,'Every Noetherian Q-base, including nilpotents; every N ≥ 1',ha='center',fontsize=14,color=ink)
    ax.text(450,126,'A construction for a supplied elliptic family, with its recorded foundations.',ha='center',fontsize=12.5,color=ink)
    def panel(y,h,title,rows,fill='#e8f1fa'):
        ax.add_patch(FancyBboxPatch((45,y),810,h,boxstyle='round,pad=0,rounding_size=12',facecolor=fill,edgecolor=edge,lw=1.5))
        ax.text(65,y+34,title,fontsize=16,weight='bold',color=ink)
        for dy,txt,size in rows:ax.text(65,y+dy,txt,fontsize=size,color=ink)
    panel(160,260,'1. The marking must be a torsion section — §1.0Q.2.3 and §1.0Q.2.3A',[
        (80,r'$P\in E[N](S),\quad [N]P=O$ as sections, with exact fibre order $N$.',16),
        (124,r'$C=\langle P\rangle\cong(\mathbf{Z}/N\mathbf{Z})_S\subset E[N]$',18),
        (166,'The disjoint finite étale sections iP define the schematic cyclic subgroup.',13.5),
        (207,r'$x+iP=x$ on any test scheme $\Longrightarrow iP=O$.',16),
        (241,'The translation action is schematically free.',14),
    ])
    panel(455,345,'2. The actual invariant charts glue the quotient — (Q4)–(Q11)',[
        (82,r'$U=\operatorname{Spec}A,\quad D=A^C,\quad Y_U=\operatorname{Spec}D$',18),
        (127,r'$A\otimes_D A\cong\prod_{g\in C}A$',20),
        (171,'The written trace dual bases prove finite projectivity and rank N.',14),
        (214,'Reynolds splitting commutes with every base change.',14),
        (259,r"$q:E\longrightarrow E'=E/C$ is finite étale of degree $N$.",18),
        (301,r"$C\times_S E\cong E\times_{E'}E$; stable opens give actual scheme gluing.",16),
    ])
    panel(835,380,'3. The quotient, its dual and the selected point — (Q12)–(Q21)',[
        (82,r"Marking over $S_\zeta=S\times_{\mathbf{Q}}\operatorname{Spec}\mathbf{Q}(\zeta_N)$; primitive $\zeta_N$.",15),
        (126,r"Over S: $\widehat{q}:E'\longrightarrow E,\quad\widehat{q}q=[N]_E,\quad q\widehat{q}=[N]_{E'}$",17),
        (171,r"$e_N(P,Q)=\zeta_N,\quad P'_\zeta=q(Q),\quad\ker\widehat{q}=\langle P'_\zeta\rangle$",18),
        (214,r"$Q\in E[N]$ on a finite étale cover of $S_\zeta$; the quotient point descends.",14),
        (258,r"$[N]P'_\zeta=O$ is a section identity; its exact fibre order is $N$.",16),
        (302,r"$P'_{\zeta^u}=uP'_\zeta,\quad\mathcal{F}_\zeta D_d=D_{d^{-1}}\mathcal{F}_\zeta$",18),
        (345,r"$u,d\in(\mathbf{Z}/N\mathbf{Z})^\times$; these scheme identities survive all pullbacks.",14),
    ])
    panel(1250,420,'4. Two return identifications have different composites — (Q22)–(Q24)',[
        (81,r"Over $S_\zeta$: $E\longrightarrow E'\longrightarrow E''$ via q, then q₂",18),
        (122,r"$R\in E[N^2]$ on a finite étale cover of $S_\zeta$, with $[N]R=P$.",16),
        (164,r"$P''=q_2(-qR),\quad v:E''\longrightarrow E$ (isomorphism)",18),
        (206,r"$v q_2=\widehat{q},\quad v q_2q=[N],\quad v(P'')=-P$",19),
        (248,r"$j=[-1]\circ v,\quad j q_2q=[-N],\quad j(P'')=P$",19),
        (282,'The negative return is chosen explicitly, including its central action.',14),
        (315,'At N = 1 or 2, P = −P: the marking does not select between v and j.',14),
        (348,r'Coefficient square $w^2=(-N)^m$ still requires actual modular descent.',16),
        (386,'A point marking alone cannot replace that coefficient construction.',14),
    ],'#fff3dc')
    panel(1705,290,'5. Why geometric-fibre order alone fails — §1.0Q.2.3A',[
        (81,r'$S=\operatorname{Spec}(F[\epsilon]/(\epsilon^2)),\quad\operatorname{char}F=0$',18),
        (125,r'$P=P_0+\delta_v,\quad [N]P_0=O,\quad v\ne0\in T_OE_0$',18),
        (170,r'$d[N]_O(v)=Nv,\quad [N]P=\delta_{Nv}\ne O$',20),
        (212,'Every geometric fibre sees P₀, of exact order N.',15),
        (253,'Nilpotent parameters cannot be discarded when defining the cyclic action.',14),
    ],'#fff3dc')
    ax.text(450,2050,'Exact proof: §§1.0Q.2–1.0Q.8 and (Q1)–(Q24), including the torsion-section condition.',ha='center',fontsize=12,color=ink)
    ax.text(450,2087,'Free human pairing conventions: Milne, Abelian Varieties, I §13, pp.57–58.',ha='center',fontsize=12,color=ink)
    ax.text(450,2124,'Coefficient descent, cusp/integral models and every good-prime specialization remain required.',ha='center',fontsize=11.8,color=ink)
    fig.canvas.draw(); renderer=fig.canvas.get_renderer()
    for text in ax.texts:
        bounds=text.get_window_extent(renderer=renderer);limit=760 if text.get_ha()=='left' else 810
        if bounds.width>limit:text.set_fontsize(text.get_fontsize()*limit/bounds.width)
    p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(p,dpi=100,facecolor=fig.get_facecolor(),metadata={'Software':'Reproducible relative elliptic quotient diagram'})
    plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default=str(Path(__file__).resolve().parents[1]/'assets/relative-cyclic-quotient-proof-map.png'))
    draw(parser.parse_args().output)

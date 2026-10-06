"""Original CC0 Dynkin diagrams for RT-LIE-09.

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra, October 2026.
Run: python rt_lie_09_figures.py OUTPUT_DIR
Requires Matplotlib and NumPy. Diagrams are schematics of the numbered
Cartan data proved in Sections 1-4 and Exercise 8.1; no source image copied.
"""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

INK = '#26384b'
SHORT = '#d5eee7'


def edge(ax, a, b, multiplicity=1, short_end=None):
    """short_end is the index 0 or 1 of the shorter endpoint."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    direction = (b-a)/np.linalg.norm(b-a)
    normal = np.array([-direction[1], direction[0]])
    start, end = a+.12*direction, b-.12*direction
    for offset in np.linspace(-.048*(multiplicity-1), .048*(multiplicity-1), multiplicity):
        p, q = start+offset*normal, end+offset*normal
        ax.plot([p[0], q[0]], [p[1], q[1]], color=INK, lw=1.8, zorder=1)
    if multiplicity > 1:
        assert short_end in (0, 1)
        toward = direction if short_end == 1 else -direction
        tip = (a+b)/2+.12*toward
        back = tip-.26*toward
        p, q = back+.15*normal, back-.15*normal
        ax.plot([p[0], tip[0], q[0]], [p[1], tip[1], q[1]], color=INK, lw=2.2, zorder=3)
    else:
        assert short_end is None


def vertex(ax, xy, label, short=False, above=False):
    ax.add_patch(Circle(xy, .12, edgecolor=INK, facecolor=SHORT if short else 'white', lw=1.8, zorder=4))
    ax.text(xy[0], xy[1]+(.25 if above else -.27), label,
            ha='center', va='center', fontsize=17, color=INK)


def setup(title, height):
    fig, ax = plt.subplots(figsize=(10, height))
    fig.subplots_adjust(left=.035, right=.985, top=.91, bottom=.075)
    ax.set_xlim(-1.6, 7.45)
    ax.set_ylim(-.55, height-.8)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle(title, fontsize=21, color=INK, y=.975)
    fig.text(.5, .022, 'Numbers label simple roots. Arrows point toward the shorter root.',
             ha='center', fontsize=12, color=INK)
    return fig, ax


def family_chain(ax, y, name, multiple=False, short_end=None):
    ax.text(-1.45, y, name, fontsize=22, va='center', color=INK)
    points = [(0,y), (1.2,y), (3.6,y), (4.8,y)]
    edge(ax, points[0], points[1])
    ax.plot([1.32, 2.1], [y,y], color=INK, lw=1.8)
    ax.text(2.4, y, r'$\cdots$', fontsize=21, ha='center', va='center', color=INK)
    ax.plot([2.7, 3.48], [y,y], color=INK, lw=1.8)
    edge(ax, points[2], points[3], 2 if multiple else 1, short_end)
    labels = [r'$1$', r'$2$', r'$n-1$', r'$n$']
    short = set()
    if multiple:
        short = {3} if short_end == 1 else {0,1,2}
    for i, (xy, label) in enumerate(zip(points, labels)):
        vertex(ax, xy, label, i in short)


def classical():
    fig, ax = setup('Classical Dynkin diagrams — Bourbaki numbering', 8)
    family_chain(ax, 6.6, r'$A_n$')
    family_chain(ax, 5.2, r'$B_n$', True, 1)
    family_chain(ax, 3.8, r'$C_n$', True, 0)
    y = 2.4
    ax.text(-1.45, y, r'$D_n$', fontsize=22, va='center', color=INK)
    points = [(0,y),(1.2,y),(3.6,y),(4.8,y+.45),(4.8,y-.45)]
    edge(ax, points[0], points[1])
    ax.plot([1.32,2.1],[y,y],color=INK,lw=1.8)
    ax.text(2.4,y,r'$\cdots$',fontsize=21,ha='center',va='center',color=INK)
    ax.plot([2.7,3.48],[y,y],color=INK,lw=1.8)
    edge(ax,points[2],points[3]); edge(ax,points[2],points[4])
    for i, (xy,label) in enumerate(zip(points,[r'$1$',r'$2$',r'$n-2$',r'$n-1$',r'$n$'])):
        vertex(ax,xy,label,above=i==3)
    ax.text(6.05, y, 'fork at\n'+r'$n-2$', fontsize=14, va='center', ha='center', color=INK)
    y = .8
    ax.text(-1.45,y,r'$D_4$',fontsize=22,va='center',color=INK)
    points = [(0,y),(1.2,y),(2.4,y+.45),(2.4,y-.45)]
    for i in [0,2,3]: edge(ax,points[1],points[i])
    for i,xy in enumerate(points): vertex(ax,xy,f'${i+1}$',above=i==2)
    ax.text(5.1,y,'Triality permutes 1, 3, 4\nand fixes 2.',ha='center',va='center',fontsize=15,color=INK)
    return fig


def exceptional():
    fig, ax = setup('Exceptional Dynkin diagrams — Bourbaki numbering', 9)
    for r,y in [(6,7.1),(7,5.55),(8,4.0)]:
        ax.text(-1.45,y,rf'$E_{r}$',fontsize=22,va='center',color=INK)
        ids=[1,3,4]+list(range(5,r+1))
        xy={i:(j*1.0,y) for j,i in enumerate(ids)}
        xy[2]=(2.0,y+.62)
        for a,b in zip(ids,ids[1:]): edge(ax,xy[a],xy[b])
        edge(ax,xy[2],xy[4])
        for i in range(1,r+1): vertex(ax,xy[i],f'${i}$',above=i==2)
    y=2.4
    ax.text(-1.45,y,r'$F_4$',fontsize=22,va='center',color=INK)
    xy=[(i*1.2,y) for i in range(4)]
    edge(ax,xy[0],xy[1]); edge(ax,xy[1],xy[2],2,1); edge(ax,xy[2],xy[3])
    for i,p in enumerate(xy): vertex(ax,p,f'${i+1}$',short=i>=2)
    y=.8
    ax.text(-1.45,y,r'$G_2$',fontsize=22,va='center',color=INK)
    xy=[(0,y),(1.8,y)]
    edge(ax,xy[0],xy[1],3,0)
    vertex(ax,xy[0],'$1$',short=True); vertex(ax,xy[1],'$2$')
    return fig


def rank_two():
    fig, ax = setup('All rank-two Dynkin diagrams', 7)
    for name,y,k,short in [(r'$A_1\times A_1$',5.5,0,None),(r'$A_2$',4.35,1,None),
                            (r'$B_2$',3.2,2,1),(r'$C_2$',2.05,2,0),(r'$G_2$',.9,3,0)]:
        ax.text(-1.45,y,name,fontsize=22,va='center',color=INK)
        xy=[(1.3,y),(3.5,y)]
        if k: edge(ax,xy[0],xy[1],k,short)
        for i,p in enumerate(xy): vertex(ax,p,f'${i+1}$',short=i==short)
    return fig


def render(output):
    output.mkdir(parents=True,exist_ok=True)
    receipts=[]
    for name,make in [('dynkin-classical',classical),('dynkin-exceptional',exceptional),('dynkin-rank2',rank_two)]:
        fig=make()
        path=output/(name+'.png')
        fig.savefig(path,dpi=180,metadata={'Software':'Matplotlib; original RT-LIE-09 CC0 diagrams'})
        plt.close(fig)
        receipts.append({'id':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size})
    return receipts


if __name__=='__main__':
    destination=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'assets/RT-LIE-09'
    print(json.dumps(render(destination),indent=2))

"""Original schematic dual graphs for AG-GS-07, Lemma 8.6 and Proposition 8.7.

Run this file with Python, Matplotlib and Pillow. Outputs are written beside it.
Vertices denote irreducible special-fibre components; edges denote nodes.
The drawing positions are schematic, not coordinates on the elliptic curve.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Circle
from PIL import Image

OUT=Path(__file__).resolve().parent
INK="#193a45"; GREEN="#087f6c"; PAPER="#fffef9"; MUTED="#48606a"
plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(5.6,10.2),dpi=150,facecolor=PAPER)
fig.text(.5,.973,"Tate special fibre: dual graphs",ha="center",color=INK,size=19,weight="bold")
fig.text(.5,.943,"Vertices = components; edges = nodes",ha="center",color=MUTED,size=15)
fig.text(.5,.917,r"Green vertex = $C_0$, containing the origin $O$",ha="center",color=GREEN,size=14)

def bezier(ax,points):
    ax.add_patch(PathPatch(MPath(points,[MPath.MOVETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4]),
                           facecolor="none",edgecolor=INK,lw=2.5,zorder=1))

def node(ax,x,y,j):
    ax.add_patch(Circle((x,y),.027,facecolor=GREEN if j==0 else PAPER,
                        edgecolor=GREEN if j==0 else INK,lw=2.5,zorder=3))

for m,bottom in [(1,.626),(2,.338),(5,.050)]:
    ax=fig.add_axes([.04,bottom,.92,.265])
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.text(.5,.94,rf"$v_R(q)={m}$",ha="center",color=INK,size=19,weight="bold")
    if m==1:
        # One vertex and one loop: the two branches lie on the same component.
        bezier(ax,[(.477,.40),(.12,.88),(.88,.88),(.523,.40)])
        node(ax,.5,.40,0)
        ax.text(.5,.26,r"$C_0$",ha="center",color=GREEN,size=20)
        group=r"$\Phi=0$"
        statement="One node, two branches on one component"
        vertices=[0];edges=[(0,0)]
    elif m==2:
        # Two distinct nodes between the same two components.
        bezier(ax,[(.28,.52),(.40,.90),(.60,.90),(.72,.52)])
        bezier(ax,[(.28,.52),(.40,.14),(.60,.14),(.72,.52)])
        node(ax,.28,.52,0);node(ax,.72,.52,1)
        ax.text(.13,.51,r"$C_0$",ha="center",color=GREEN,size=20)
        ax.text(.87,.51,r"$C_1$",ha="center",color=INK,size=20)
        group=r"$\Phi=\mathbf{Z}/2\mathbf{Z}$"
        statement="Two nodes joining the same two components"
        vertices=[0,1];edges=[(0,1),(0,1)]
    else:
        # Cyclic indexing, with C0 at the top and positive indices clockwise.
        points=[(.5+.28*math.sin(2*math.pi*j/m),.51+.25*math.cos(2*math.pi*j/m)) for j in range(m)]
        for j in range(m):
            a,b=points[j],points[(j+1)%m]
            ax.plot([a[0],b[0]],[a[1],b[1]],color=INK,lw=2.5,zorder=1)
        for j,(x,y) in enumerate(points):
            node(ax,x,y,j)
            lx=.5+1.40*(x-.5);ly=.51+1.40*(y-.51)
            ax.text(lx,ly,rf"$C_{j}$",ha="center",va="center",color=GREEN if j==0 else INK,size=18)
        group=r"$\Phi=\mathbf{Z}/5\mathbf{Z}$"
        statement="Five nodes in cyclic order"
        vertices=list(range(m));edges=[(j,(j+1)%m) for j in range(m)]
    # These checks bind the displayed graph to the proved cycle, including loops.
    assert len(vertices)==m and len(edges)==m
    assert all(sum(j==a for a,b in edges)+sum(j==b for a,b in edges)==2 for j in vertices)
    ax.text(.5,.12,statement,ha="center",color=MUTED,size=14)
    ax.text(.5,.018,group+r"$\qquad \mathcal{E}_{q,\kappa}^{\,0}\simeq\mathbf{G}_m$",ha="center",color=INK,size=16)

png=OUT/"tate-dual-graphs.png"
fig.savefig(png,dpi=150,facecolor=PAPER)
fig.savefig(OUT/"tate-dual-graphs.svg",facecolor=PAPER,
            metadata={"Creator":"GPT-6.1 Sol (OpenAI), independently authored course diagram","Date":None})
plt.close(fig)
# Retain only image pixels and standard PNG framing, without source-path metadata.
with Image.open(png) as im:
    clean=im.convert("RGB")
clean.save(png,optimize=False)
print(png)

"""Exact sectional-curvature illustration for the Kähler-curvature lesson.

Mathematics: Theorem D.2, K = c/4 * (1 + 3*cos(theta)**2).
Coordinates in the real orthonormal basis (X, JX, E):
X=(1,0,0), JX=(0,1,0), E=(0,0,1),
Y_theta=(0,cos(theta),sin(theta)); the depicted angle is pi/4.
The left panel applies the stated linear projection, not a manifold embedding.
The right panel samples the exact proved function for c=4,0,-4.
For complex dimension one, only theta=0 is possible.

Reproduce with Python 3, NumPy and Matplotlib:
    python kahler_sectional_range.py
Optional: --output figure.svg --preview figure.png
New figure and code: OpenAI, October 2026. CC0 1.0.
"""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def project(v):
    """Exact linear projection P(x,y,z)=(x-11*y/20, 8*y/25+z)."""
    v=np.asarray(v)
    return np.stack((v[...,0]-11*v[...,1]/20,
                     8*v[...,1]/25+v[...,2]),axis=-1)


def build(output, preview=None):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                         "svg.fonttype":"none","svg.hashsalt":"kahler-sectional-range-v1"})
    fig=plt.figure(figsize=(12.4,6.6),facecolor="white")
    left=fig.add_axes((.035,.20,.43,.61))
    right=fig.add_axes((.565,.27,.35,.53))
    ink="#173c42"; blue="#247b9a"; orange="#c26328"; gray="#617176"
    X=np.array([1.,0,0]); JX=np.array([0.,1,0]); E=np.array([0.,0,1])
    Y=(JX+E)/np.sqrt(2)
    for vec,color,alpha in [(JX,blue,.11),(Y,orange,.21)]:
        corners=project(np.array([np.zeros(3),X,X+vec,vec]))
        left.add_patch(Polygon(corners,facecolor=color,edgecolor=color,lw=1.6,alpha=alpha))
    for v,label,color,offset in [
        (X,r"$X$",ink,(.04,-.11)),
        (JX,r"$JX$",blue,(-.10,.00)),
        (E,r"$E$",gray,(.02,.06)),
        (Y,r"$Y_{\pi/4}=(JX+E)/\sqrt{2}$",orange,(-.30,.36))]:
        end=project(v)
        left.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"-|>","color":color,"lw":2})
        left.text(*(end+offset),label,color=color,fontsize=12)
    for v in [JX,Y]:
        a,b=project(X),project(X+v)
        left.plot([a[0],b[0]],[a[1],b[1]],ls="--",lw=1,color=gray,alpha=.65)
    phi=np.linspace(0,np.pi/4,80)
    arc=project(np.stack((np.zeros_like(phi),.40*np.cos(phi),.40*np.sin(phi)),axis=-1))
    left.plot(arc[:,0],arc[:,1],color=orange,lw=1.5)
    left.text(-.34,.47,r"$\theta=\pi/4$",color=orange,fontsize=11)
    left.scatter([0],[0],s=16,color=ink,zorder=5)
    left.text(.015,-.12,"0",color=ink)
    left.text(.48,.14,r"$\mathrm{span}(X,JX)$",color=blue,fontsize=10)
    left.text(.40,.74,r"$\mathrm{span}(X,Y_{\pi/4})$",color=orange,fontsize=10)
    left.set(xlim=(-.8,1.28),ylim=(-.23,1.42),aspect="equal")
    left.axis("off")
    left.set_title("A real plane moving between two extremes",loc="left",color=ink,pad=10,fontsize=12)

    theta=np.linspace(0,np.pi/2,401)
    for c,color,label in [(4,blue,r"$c=4$"),(0,gray,r"$c=0$"),(-4,orange,r"$c=-4$")]:
        values=c/4*(1+3*np.cos(theta)**2)
        right.plot(theta,values,color=color,lw=2.2,label=label)
        right.scatter([0,np.pi/2],[c,c/4],s=25,color=color,zorder=4)
        right.annotate(label,xy=(np.pi/2,c/4),xytext=(9,0),
                       textcoords="offset points",color=color,fontsize=10,va="center")
        if c:
            right.scatter([np.pi/4],[5*c/8],s=30,color=color,zorder=5)
            right.annotate(r"$5/2$" if c>0 else r"$-5/2$",
                           xy=(np.pi/4,5*c/8),xytext=(8,9 if c>0 else -18),
                           textcoords="offset points",color=color,fontsize=11)
    right.axvline(np.pi/4,color=gray,ls=":",lw=1)
    right.set_xlim(-.025,np.pi/2+.025);right.set_ylim(-4.5,4.5)
    right.set_xticks([0,np.pi/4,np.pi/2],["0",r"$\pi/4$",r"$\pi/2$"])
    right.set_yticks([-4,-1,0,1,4])
    right.set_xlabel(r"$\theta$  (radians)")
    right.set_ylabel(r"$K(X,Y_\theta)$")
    right.grid(axis="y",color="#dfe6e6",lw=.6)
    right.spines[["top","right"]].set_visible(False)
    right.spines[["left","bottom"]].set_color(gray)
    right.set_title(r"$K=\frac{c}{4}(1+3\cos^2\theta)$",color=ink,pad=18,fontsize=14)
    fig.text(.035,.945,"Sectional curvature in a complex space form",color=ink,fontsize=19,weight="bold")
    fig.text(.035,.895,r"$X,JX,E$ orthonormal;  $E\perp\mathrm{span}(X,JX)$;  "
             r"$Y_\theta=\cos\theta\,JX+\sin\theta\,E$.",color=ink,fontsize=12)
    fig.text(.04,.105,"Left: linear projection of a tangent subspace.\n"
             "The shaded planes are tangent planes, not surfaces in the manifold.",
             color=gray,fontsize=10,linespacing=1.45)
    fig.text(.56,.08,r"$\theta=0$: complex plane, $K=c$."+"\n"+
             r"$\theta=\pi/2$: totally real plane, $K=c/4$."+"\n"+
             r"Complex dimension $n\geq2$: full interval; $n=1$: only $\theta=0$.",
             color=ink,fontsize=10,linespacing=1.45)
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"OpenAI",
      "Title":"Sectional curvature in a complex space form",
      "Description":"Exact Theorem D.2 curves and the projected orthonormal tangent-plane construction. The plane at pi/4 has curvature plus or minus 5/2 for c=plus or minus 4; in complex dimension one only theta=0 occurs."})
    if preview:
        preview=Path(preview);preview.parent.mkdir(parents=True,exist_ok=True)
        fig.savefig(preview,dpi=150)
    plt.close(fig)
    checks={"X_dot_Y":float(X@Y),"Y_norm_squared":float(Y@Y),
            "XJX_dot_E":float(JX@E),"theta_midpoint":float(np.pi/4),
            "midpoint_curvatures":[2.5,0.,-2.5]}
    assert np.isclose(Y@Y,1) and X@Y==0 and JX@E==0
    print(checks)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("kahler-sectional-range.svg"))
    parser.add_argument("--preview",type=Path)
    args=parser.parse_args()
    build(args.output,args.preview)

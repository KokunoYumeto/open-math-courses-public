"""Exact terminal-force and comparison maps; schematic, no numerical samples."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).with_suffix("")
BG = "#faf9f5"
INK = "#172c3d"

def box(ax, x, y, w, h, title, lines, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                               facecolor=color, edgecolor="#a9b2b7", lw=1.1))
    ax.text(x+.018, y+h-.035, title, va="top", fontsize=13, weight="bold", color=INK)
    for k, line in enumerate(lines):
        ax.text(x+.018, y+h-.085-k*(h-.125)/max(1,len(lines)-1), line, va="top", fontsize=12, color=INK)

def arrow(ax, x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0,y0), (x1,y1), arrowstyle="-|>",
                                mutation_scale=15, color="#667987", lw=1.5))

def main():
    fig, ax = plt.subplots(figsize=(15.5,10.5))
    fig.patch.set_facecolor(BG)
    ax.set(xlim=(0,1), ylim=(0,1))
    ax.axis("off")
    ax.text(.5,.985,"Smooth compact force and the blowup conclusion",ha="center",
            va="top",fontsize=21,weight="bold",color=INK)
    ax.text(.5,.938,"Exact implications for the actual local fields I0–I7",ha="center",
            fontsize=12,color="#53616a")
    box(ax,.025,.655,.285,.23,"At the origin — F2",[
        r"$c=1,\quad f^-=\mathscr{R}(v,p^{\rm loc})$",
        r"$|\partial_x^\alpha\partial_t^j f^-|$",
        r"$\quad\leq C_{\alpha,j,N}(\tau+|z|^{1/D})^N$"
    ],"#e7f0ef")
    box(ax,.357,.655,.285,.23,"Away, positive q — F2",[
        r"$0<c_1\leq q\leq c_2<q_*$",
        "All field derivatives bounded",
        "One more time derivative",
        r"$\Rightarrow$ uniform terminal limits"
    ],"#e9eef7")
    box(ax,.689,.655,.285,.23,"Away, positive r — F2",[
        r"$\mathcal{A}=0,\quad v=K(r,\tau)e_\theta$",
        r"$p^{\rm loc}=-\int_r^\infty K(\rho,\tau)^2\,d\rho/\rho$",
        "Exact heat integral controls",
        "every terminal derivative"
    ],"#f1ebf7")
    for x in [.168,.5,.831]:arrow(ax,x,.642,.5,.578)
    box(ax,.16,.367,.68,.20,"Compatible jets and their compact extension — F2–F3",[
        r"$F_j=\lim_{t\uparrow1}\partial_t^j f^-\in C_c^\infty(\mathbb{R}^3)$",
        r"$f^+(x,1+\sigma)=\sum_{j\geq0}\chi_0(b_j\sigma)\,\sigma^j F_j(x)/j!$",
        r"$\mathrm{supp}\,f\subset\mathcal{K}\times[1-\tau_0,2]$"
    ],"#f4eedf")
    arrow(ax,.37,.354,.26,.31);arrow(ax,.63,.354,.74,.31)
    box(ax,.025,.095,.45,.205,"Energy and comparison — F4–F5",[
        r"$\|u(t)\|_2^2+2\int_0^t\|\nabla u\|_2^2\leq\mathcal{F}(t)^2$",
        r"$\mathcal{F}(t)=\int_0^t\|f(s)\|_2\,ds$",
        r"$E_R(t)\leq C_T R^{-4/3}\ \Rightarrow\ v_c=u\ (t<1)$"
    ],"#e7f0ef")
    box(ax,.525,.095,.45,.205,"Original inner path — F6–F8",[
        r"$x_\tau=(\sqrt{2X_{\rm in}\tau},0,0)$",
        r"$u_\theta(x_\tau,1-\tau)\geq(e_0/2)\tau^{-A}\to\infty$",
        r"$u_\nu=\sqrt{\nu}\,u(x/\sqrt{\nu},t)$"
    ],"#f4e8e3")
    ax.text(.5,.052,"A smooth global competitor would be bounded near (0, 1), contradicting this same path.",
            ha="center",fontsize=12,color=INK)
    ax.text(.5,.014,"Source: OpenAI, Theorem 1.1 and §10, pp. 117–126. Proof: terminal-force-and-blowup-audit.md, F0–F8.",
            ha="center",fontsize=10,color="#53616a")
    fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.99)
    for ext in [".png",".svg"]:
        fig.savefig(OUT.with_suffix(ext),dpi=150,facecolor=BG,bbox_inches="tight")
    print(OUT.name)

if __name__ == "__main__":
    main()

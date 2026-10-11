"""Reproducible course diagrams for I.6–I.9, I.25–I.37 and I.48."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"figures"
INK="#173f4a"; TEAL="#187c78"; OCHRE="#a75c18"; BLUE="#445fa6"

def setup():
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
        "text.color":INK,"axes.labelcolor":INK,"axes.edgecolor":INK,
        "xtick.color":INK,"ytick.color":INK,"svg.hashsalt":"YM-F10-20261010",
        "figure.facecolor":"#fffef9","axes.facecolor":"#fffef9"})

def save(fig,name):
    fig.savefig(OUT/(name+".svg"),metadata={"Date":None},facecolor=fig.get_facecolor())
    fig.savefig(OUT/(name+".png"),dpi=145,metadata={"Software":"YM-GAUGE reproducible figure"},
                facecolor=fig.get_facecolor())
    plt.close(fig)

def build():
    setup();OUT.mkdir(exist_ok=True)
    fig=plt.figure(figsize=(11.4,7.0));ax=fig.add_axes((0,0,1,1));ax.axis("off")
    ax.text(.04,.94,"The Hodge star pairs the six coordinate two-forms",fontsize=19,weight="bold")
    ax.text(.04,.885,r"Metric $\sum_{\mu=0}^3(dx^\mu)^2$; orientation $dx^0\wedge dx^1\wedge dx^2\wedge dx^3$.",fontsize=14)
    rows=[(r"dx^0\wedge dx^1",r"dx^2\wedge dx^3","+"),
          (r"dx^0\wedge dx^2",r"dx^1\wedge dx^3","−"),
          (r"dx^0\wedge dx^3",r"dx^1\wedge dx^2","+")]
    for y,(left,right,sign) in zip([.73,.53,.33],rows):
        ax.text(.09,y,"$"+left+"$",fontsize=23,va="center")
        ax.text(.43,y,"$"+right+"$",fontsize=23,va="center")
        ax.add_patch(FancyArrowPatch((.275,y),(.402,y),arrowstyle="<->",mutation_scale=17,
                                    color=TEAL,lw=2))
        ax.text(.315,y+.045,sign+" star",fontsize=13,color=TEAL)
        ax.text(.67,y+.03,"self-dual: left "+sign+" right",fontsize=14)
        ax.text(.67,y-.035,"anti-self-dual: left "+("−" if sign=="+" else "+")+" right",fontsize=14)
    ax.text(.04,.15,"Applying star twice gives +1 on every two-form.",fontsize=15,weight="bold")
    ax.text(.04,.095,"Each paired sum and difference is written with its exact orientation sign.",fontsize=13)
    ax.text(.04,.04,"Proof: Unit 10, I.6–I.9; complete component table: Solution 1, F10.5.",fontsize=12)
    save(fig,"f10-hodge-pairs")

    fig,axs=plt.subplots(1,2,figsize=(11.4,6.4))
    fig.subplots_adjust(left=.08,right=.97,bottom=.26,top=.81,wspace=.28)
    fig.suptitle("The instanton charge changes scale while its total stays one",fontsize=17,y=.97,weight="bold")
    fig.text(.08,.88,r"Display map: $s=R/\ell$, with an arbitrary retained length $\ell>0$.",fontsize=13)
    samples=[]
    s=np.linspace(0,5,1001)
    for ratio,color,label in [(.5,TEAL,r"$\rho=\ell/2$"),(1,BLUE,r"$\rho=\ell$"),(2,OCHRE,r"$\rho=2\ell$")]:
        # These are the exact physical formulas evaluated at R=ell*s, rho=ell*ratio.
        # The left ordinate is ell*dQ/dR; no field scale is replaced.
        shell=12*ratio**4*s**3/(s*s+ratio*ratio)**4
        mass=s**4*(s*s+3*ratio*ratio)/(s*s+ratio*ratio)**3
        axs[0].plot(s,shell,color=color,lw=2,label=label)
        axs[1].plot(s,mass,color=color,lw=2,label=label)
        axs[1].plot([ratio],[.5],"o",color=color,ms=6)
        samples.append({"rho_over_ell":ratio,"R_over_ell":s.tolist(),
                        "ell_times_dQ_dR":shell.tolist(),"Q_R":mass.tolist()})
    for ax in axs:
        ax.set_xlabel(r"$R/\ell$");ax.grid(alpha=.2);ax.set_xlim(0,5)
    axs[0].set_ylabel(r"$\ell\,dQ_R/dR$");axs[1].set_ylabel(r"$Q_R$")
    axs[1].set_ylim(0,1.04);axs[0].legend(frameon=False,fontsize=11)
    axs[1].axhline(.5,color=INK,ls=":",lw=1)
    fig.text(.08,.15,r"$dQ_R/dR=12\rho^4R^3/(R^2+\rho^2)^4$     $Q_R=R^4(R^2+3\rho^2)/(R^2+\rho^2)^3$",fontsize=13)
    fig.text(.08,.10,r"Dots: $Q_\rho=1/2$.  Full action $S_E=8\pi^2\hbar/g_{\rm YM}^2$; inside radius $R$: $S_E Q_R$.",fontsize=12)
    fig.text(.08,.045,"Exact curves and sampled points. Proof: I.25–I.28, I.48 and Solution 3. These are four-dimensional radii.",fontsize=11)
    save(fig,"f10-charge-concentration")
    (OUT/"f10-charge-samples.json").write_text(json.dumps({
        "display_map":"R=ell*s, rho=ell*ratio; ell>0; plotted ordinate ell*dQ_R/dR",
        "original_formula":"12*rho^4*R^3/(R^2+rho^2)^4",
        "proof_locators":["I.25–I.28","I.48","F10.8–F10.9"],"samples":samples},
        separators=(",",":"))+"\n",encoding="utf8")

    fig=plt.figure(figsize=(11.4,7.5))
    fig.text(.04,.945,"Two smooth connection charts on the four-sphere",fontsize=19,weight="bold")
    fig.text(.04,.89,r"The drawing is the exact section $Y^1=Y^2=Y^3=0$; the bundle lives over all of $S_L^4$.",fontsize=13)
    ax=fig.add_axes((.06,.36,.42,.45));theta=np.linspace(0,2*np.pi,601)
    ax.plot(np.sin(theta),np.cos(theta),color=TEAL,lw=2)
    ax.axhline(0,color=INK,lw=.6);ax.axvline(0,color=INK,lw=.6)
    ax.plot([0,0],[1,-1],"o",color=INK)
    ax.text(.06,1.04,"N: y chart omits this point",fontsize=10)
    ax.text(.06,-1.16,"S: z chart omits this point",fontsize=10)
    ax.plot([.8],[.6],"o",color=OCHRE);ax.text(.83,.61,"P",color=OCHRE,fontsize=14)
    ax.set(xlim=(-1.2,1.3),ylim=(-1.24,1.2),aspect="equal",xlabel=r"$Y^0/L$",ylabel=r"$Y^4/L$")
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    fig.text(.54,.77,r"Finite chart: $y\in\mathbb{R}^4$",fontsize=16,weight="bold")
    fig.text(.54,.72,r"$Y^\mu=\dfrac{2L^2y^\mu}{L^2+|y|^2}$",fontsize=15)
    fig.text(.54,.615,r"$Y^4=\dfrac{L(|y|^2-L^2)}{|y|^2+L^2}$",fontsize=15)
    fig.text(.54,.525,r"Overlap: $z=L^2y/|y|^2$",fontsize=16)
    fig.text(.54,.46,r"$\det(Dz/Dy)=-L^8/|y|^8$",fontsize=15)
    fig.text(.54,.395,r"Frame transition: $h=q/|y|$",fontsize=15)
    fig.text(.54,.33,r"$A_\infty=h^{-1}A_Rh+h^{-1}dh$",fontsize=15)
    fig.text(.06,.235,r"$P=(4L/5,0,0,0,3L/5)$:  $y=(2L,0,0,0)$;  $z=(L/2,0,0,0)$.",fontsize=14)
    fig.text(.06,.175,"The negative coordinate determinant reverses the coordinate orientation.",fontsize=13)
    fig.text(.06,.12,"The global Hodge star uses the same chosen sphere orientation in both charts.",fontsize=13)
    fig.text(.06,.055,"Proof: I.29–I.37; worked chart comparison: F10.4. Circle coordinates display Y/L; L is retained.",fontsize=11)
    save(fig,"f10-sphere-charts")

if __name__=="__main__":build()

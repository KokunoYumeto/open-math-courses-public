"""Original null-section figure and symbolic/numerical self-checks.

Run with Python + matplotlib, numpy, sympy, scipy. Does not run TeX.
Only writes beneath this script's directory. Source scans are never used.
"""
from pathlib import Path
import json
import math
import sys
import hashlib
from datetime import datetime, timezone
import numpy as np
import sympy as sp
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "none", "text.usetex": False})


def symbolic_checks():
    # At any sphere point rotate omega to e3 and use an orthonormal
    # covariantly geodesic frame e1,e2. The independent slope and Hessian
    # symbols below represent arbitrary two-jets of w, not a special profile.
    r,c=sp.symbols("r c", positive=True, real=True)
    a1,a2,h11,h12,h22=sp.symbols("a1 a2 h11 h12 h22", real=True)
    a=[a1,a2]
    hs=[[h11,h12],[h12,h22]]
    n=sp.Matrix([-1/c,0,0,1])
    om=sp.Matrix([0,0,0,1])
    es=[sp.Matrix([0,1,0,0]),sp.Matrix([0,0,1,0])]
    aa=a1*a1+a2*a2
    F=r*n
    L=sp.Matrix([(1+aa)/(2*c*r),-a1/r,-a2/r,(1-aa)/(2*r)])
    E=[r*(a[j]*n+es[j]) for j in range(2)]
    # These are ambient covariant second derivatives after subtracting
    # the sphere-connection term; that tangent term pairs to zero with L.
    second=[[r*((hs[i][j]+a[i]*a[j])*n+a[i]*es[j]+a[j]*es[i]
                -(1 if i==j else 0)*om) for j in range(2)] for i in range(2)]
    def G(v, z):
        return c*c*v[0]*z[0] - (v[1:, :].T*z[1:, :])[0]
    def simp(q):
        return sp.factor(sp.cancel(q))
    checks = {
        "radial_null": simp(G(F,F)),
        "reflected_null": simp(G(L,L)),
        "normal_scale_G_N_L_minus1": simp(G(F,L)+1),
        "normal_e1": simp(G(E[0],L)),
        "normal_e2": simp(G(E[1],L)),
        "metric_e1": simp(-G(E[0],E[0])-r*r),
        "metric_cross": simp(-G(E[0],E[1])),
        "metric_e2": simp(-G(E[1],E[1])-r*r),
    }
    btt = G(second[0][0],L)
    btp = G(second[0][1],L)
    bpp = G(second[1][1],L)
    expected_tt = -h11+a1*a1+(1-aa)/2
    expected_tp = -h12+a1*a2
    expected_pp = -h22+a2*a2+(1-aa)/2
    checks.update({
        "ambient_second_form_theta": simp(btt-expected_tt),
        "ambient_second_form_cross": simp(btp-expected_tp),
        "ambient_second_form_phi": simp(bpp-expected_pp),
        "ambient_trace_equals_intrinsic_K": simp((btt+bpp)/r**2-(1-h11-h22)/r**2),
    })
    b11,b22,b12 = sp.symbols("b11 b22 b12", real=True)
    # Null normal coefficient pairs are (coefficient of N, coefficient of L).
    def NG(v,z):
        return -v[0]*z[1]-v[1]*z[0]
    ii11,ii22,ii12=(-b11,-1),(-b22,-1),(-b12,0)
    K=b11+b22
    H=(-K/2,-1)
    checks.update({
        "null_gauss_trace": sp.expand(-NG(ii11,ii22)+NG(ii12,ii12)-K),
        "mean_vector_norm": sp.expand(NG(H,H)+K),
        "riesz_directional_mean": sp.expand(-NG(H,(0,-sp.Rational(1,2)))-K/4),
    })
    output = {name: str(value) for name,value in checks.items()}
    assert all(value == 0 for value in checks.values()), output
    return output


def polynomial_checks():
    results=[]
    for eps in [0,1/6,1/3,0.5]:
        def values(z):
            P=(3*z*z-1)/2
            w=eps*P
            r=math.exp(w)
            a2=9*eps*eps*z*z*(1-z*z)
            delta=-6*eps*P
            density=1-delta
            # L spatial z component: ((1-a2)z - 2a_z)/(2r),
            # where a_z=3eps*z*(1-z*z).
            Lz=((1-a2)*z-6*eps*z*(1-z*z))/(2*r)
            Lt=(1+a2)/(2*r)
            return r,a2,density,Lz,Lt
        fields={
            "constant": lambda r,a2,d,Lz,Lt: (1.0,0.0,0.0),
            "time": lambda r,a2,d,Lz,Lt: (-r,Lt,0.0),
            "x3": lambda r,a2,d,Lz,Lt: (None,Lz,0.0),
            "homogeneous_quadratic": lambda r,a2,d,Lz,Lt:
                (4*r*r/3, -2/3-4*a2/3,0.0),
            "spatial_square_forced": lambda r,a2,d,Lz,Lt:
                (r*r,1-a2,-3*r*r),
            "time_square_forced": lambda r,a2,d,Lz,Lt:
                (r*r,-(1+a2),r*r),
        }
        for field,fn in fields.items():
            def terms(z):
                r,a2,d,Lz,Lt=values(z)
                u,Lu,force=fn(r,a2,d,Lz,Lt)
                if u is None:
                    u=r*z
                intrinsic=(d*u+2*Lu*r*r)/2
                # Riesz mu=d/(4r²) and nu=-L/2, azimuthal integral 2pi.
                ambient=2*(d*u/4+Lu*r*r/2)
                return intrinsic,ambient,force/2
            bi=quad(lambda z: terms(z)[0],-1,1,epsabs=2e-12)[0]
            ba=quad(lambda z: terms(z)[1],-1,1,epsabs=2e-12)[0]
            ff=quad(lambda z: terms(z)[2],-1,1,epsabs=2e-12)[0]
            expected=1.0 if field=="constant" else 0.0
            error=max(abs(bi+ff-expected),abs(ba+ff-expected),abs(bi-ba))
            assert error < 2e-10,(eps,field,error)
            results.append({"epsilon":eps,"field":field,"intrinsic_boundary":bi,
                            "riesz_boundary":ba,"radial_source":ff,
                            "expected_vertex_value":expected,"maximum_error":error})
    return results


def build_figure(comparison_only=False):
    epsvals=[0,1/6,1/3,0.5]
    colors=["#708090","#1b9e77","#d95f02","#7570b3"]
    fig,axs=plt.subplots(1,3,figsize=(15.8,5.4),layout="constrained")
    theta=np.linspace(0,2*np.pi,1000)
    z=np.cos(theta)
    for eps,col in zip(epsvals,colors):
        r=np.exp(eps*(3*z*z-1)/2)
        label={0:"0",1/6:"1/6",1/3:"1/3",0.5:"1/2"}[eps]
        axs[0].plot(r*np.sin(theta),r*z,color=col,lw=2,label=rf"$\epsilon={label}$")
    axs[0].set_aspect("equal")
    axs[0].set(xlabel=r"$x_1-X_1$",ylabel=r"$x_3-X_3$",
               title="Spatial meridian projection")
    axs[0].text(0.03,0.98,r"$t-T=-r/c$"+"\n"+r"$g=r^2g_{S^2}$",
                transform=axs[0].transAxes,va="top",bbox={"facecolor":"white","alpha":0.85,"edgecolor":"none"})
    axs[0].legend(loc="lower left",fontsize=10)
    zs=np.linspace(-1,1,601)
    for eps,col in zip(epsvals,colors):
        density=1+6*eps*(3*zs*zs-1)/2
        axs[1].plot(zs,density,color=col,lw=2)
    axs[1].axhline(0,color="#444444",ls="--",lw=1)
    axs[1].scatter([0],[0],color=colors[2],zorder=5)
    axs[1].annotate(r"$K=0$ at $\epsilon=1/3$",xy=(0,0),xytext=(-0.9,1.8),
                    arrowprops={"arrowstyle":"->","color":colors[2]},color=colors[2])
    axs[1].set(xlabel=r"$z=\omega_3$",ylabel=r"$Kr^2=1+6\epsilon P_2(z)$",
               title="Exact curvature density")
    axs[1].text(0.04,0.96,r"$\int_\Sigma K\,d\sigma=4\pi$",transform=axs[1].transAxes,va="top",
                bbox={"facecolor":"white","edgecolor":"none","alpha":1.0,"pad":3})
    r=math.exp(-1/6)
    Rs=np.linspace(-5.7*r*r,5.7*r*r,400)
    xs=r-Rs/(4*r)
    cts=-r-Rs/(4*r)
    axs[2].plot(xs/r,cts/r,color=colors[2],lw=2)
    pts=[(1,-1,r"$Q:(x_1,ct)=(r,-r)$"),
         (2,0,r"$R_\theta=-4r^2$"+"\n"+r"$(2r,0)$"),
         (0,-2,r"$R_\phi=+4r^2$"+"\n"+r"$(0,-2r)$")]
    for x,t,lab in pts:
        axs[2].scatter([x],[t],color="#222222",s=38,zorder=5)
        if x==1: xytext=(1.06,-1.45)
        elif x==2: xytext=(1.35,0.25)
        else: xytext=(0.05,-2.62)
        axs[2].annotate(lab,xy=(x,t),xytext=xytext,fontsize=10,
                        arrowprops={"arrowstyle":"-","color":"#555555"})
    axs[2].annotate("increasing R (past)",xy=(0.3,-1.7),xytext=(1.8,-2.4),fontsize=10,
                    arrowprops={"arrowstyle":"->","color":"#444444"})
    axs[2].scatter([0],[0],marker="*",s=90,color="#1f78b4")
    axs[2].annotate("vertex q",xy=(0,0),xytext=(-0.45,0.22),fontsize=10,color="#1f78b4")
    axs[2].set(xlabel=r"$x_1/r$",ylabel=r"$ct/r$",xlim=(-0.6,2.6),ylim=(-2.85,0.8),
               title=r"Two foci where $K=0$ ($\epsilon=1/3$)")
    axs[2].set_aspect("equal")
    for ax in axs:
        ax.grid(alpha=0.2)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Null Gauss identity: radial form = metric, reflected mean = K/4",fontsize=15)
    fig.savefig(FIG/"null-gauss-comparison.png",dpi=190)
    fig.savefig(FIG/"null-gauss-comparison.svg")
    plt.close(fig)
    geom={"figure":"null-gauss-comparison","original":True,"geometry":"Lorentz G=c²dt²-|dx|²; q=0",
          "panels":[{"type":"spatial meridian projection, not induced metric",
                     "r":"exp(epsilon*(3*omega3²-1)/2)","time":"-r/c","epsilon":epsvals},
                    {"type":"exact analytic density","ordinate":"K*r²=1+6epsilon*P2(z)","abscissa":"z=omega3"},
                    {"type":"exact two-dimensional ambient slice","epsilon":"1/3","omega":[1,0,0],
                     "r":"exp(-1/6)","line":"(ct,x1)=(-r-R/(4r),r-R/(4r))",
                     "Q":"(ct,x1)=(-r,r)","theta_focus":{"R":"-4r²","ct":"0","x1":"2r"},
                     "phi_focus":{"R":"+4r²","ct":"-2r","x1":"0"}}],
          "proof_locators":["manuscript.md M2–M5,M7","learner eq(11),(16),(23)"],
          "human_source":"Riesz1949 §68 pp138–141; exact Gaussian comparison derived here",
          "Blender":"Not used: exact planar projections, a scalar plot and a null-line diagram are clearest as vector scientific plots."}
    (FIG/"geometry.json").write_text(json.dumps(geom,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    if comparison_only:
        return
    fig2, axes=plt.subplots(1,2,figsize=(12.8,5.2),gridspec_kw={"width_ratios":[1,1.8]},layout="constrained")
    ax=axes[0]
    ax.axline((0,0),slope=1,color="#cccccc",ls="--")
    ax.axline((0,0),slope=-1,color="#cccccc",ls="--")
    arrows=[(1,-1,r"$N=(-1,1)$","#1b9e77",(0.4,-1.28)),
            (0.5,0.5,r"$L=(1/2,1/2)$","#d95f02",(0.25,0.76)),
            (-0.25,-0.25,r"$\nu=(-1/4,-1/4)$","#7570b3",(-1.36,-0.57)),
            (-1,0,r"$H=(0,-1)$","#1f78b4",(-1.2,0.17))]
    for x,t,label,color,position in arrows:
        ax.annotate("",xy=(x,t),xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.2})
        ax.text(*position,label,color=color,fontsize=10)
    ax.set_aspect("equal")
    ax.set(xlabel="spatial normal coordinate",ylabel="time coordinate",xlim=(-1.5,1.4),ylim=(-1.5,1.15),
           title="Exact normal plane: time sphere, c = r = 1")
    ax.text(0.04,0.96,r"$G(N,L)=-1$"+"\n"+r"$H=-L-N/2$",transform=ax.transAxes,va="top")
    ax.grid(alpha=.18)
    ax.spines[["top","right"]].set_visible(False)
    axes[1].axis("off")
    axes[1].set_title("Trace and focal parameters in every degeneracy type",pad=15)
    rows=[["time sphere","1/4","1/4","1","4, 4"],
          ["equator, ε = 1/6","0","1/4","1/2","∞, 4"],
          ["equator, ε = 1/3","-1/4","1/4","0","-4, 4"],
          ["north, w = (1-z)/2","0","0","0","∞, ∞"]]
    table=axes[1].table(cellText=rows,colLabels=["section / point",r"$\kappa_1r^2$",r"$\kappa_2r^2$",r"$Kr^2$",r"$R_1/r^2, R_2/r^2$"],
                        cellLoc="center",colWidths=[.36,.14,.14,.12,.24],bbox=[0,.32,1,.52])
    table.auto_set_font_size(False)
    table.set_fontsize(10.5)
    for (row,col),cell in table.get_celld().items():
        cell.set_edgecolor("#dddddd")
        cell.set_facecolor("#eaf0f4" if row==0 else ("#fafafa" if row%2 else "white"))
    axes[1].text(.02,.23,r"$K=2(\kappa_1+\kappa_2),\quad\mu_R=K/4$",fontsize=13)
    axes[1].text(.02,.13,"∞ means no finite focal parameter in that direction.\nAt K = 0, the vector H = -L remains nonzero and null.",fontsize=11)
    fig2.savefig(FIG/"null-frame-and-degeneracies.png",dpi=190)
    fig2.savefig(FIG/"null-frame-and-degeneracies.svg")
    plt.close(fig2)
    framegeom={"original":True,"figure":"null-frame-and-degeneracies",
        "normal_plane":{"metric":"G=dt²-dx_normal²","c":1,"r":1,"coordinate_label_order":"(t,x_normal)",
                        "N":[-1,1],"L":[0.5,0.5],"nu":[-0.25,-0.25],"H":[0,-1]},
        "table_columns":["section/point","kappa1*r²","kappa2*r²","K*r²","R1/r²,R2/r²"],
        "table_exact_rows":rows,"infinite_focal_semantics":"no finite focal parameter",
        "proof_locators":["manuscript M2–M5,M7","learner Theorem2, eq(13)–(17), examples, Exercise6"],
        "human_source":"Riesz1949 §68 pp138–141; degeneracy extension and Gaussian identity derived here"}
    (FIG/"normal-frame-geometry.json").write_text(json.dumps(framegeom,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")


if __name__=="__main__":
    sym=symbolic_checks()
    num=polynomial_checks()
    build_figure()
    data={"schema":"an02.riesz-null-gauss-selfcheck.v1",
          "recorded_utc":datetime.now(timezone.utc).isoformat(),"python":sys.executable,
          "symbolic_residuals":sym,"numerical_polynomial_checks":num,
          "numerical_maximum_error":max(item["maximum_error"] for item in num),
          "source_geometry_scope":"Checks on radial sections; polynomial source uses the explicit cone radial-shell integral, not an asserted global graph extension.",
          "independent_review":False,"figure_visual_inspection":"pending"}
    (ROOT/"computational-checks.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"symbolic_checks":len(sym),"quadrature_checks":len(num),
                      "maximum_error":data["numerical_maximum_error"],"figure":str(FIG/"null-gauss-comparison.png")}))

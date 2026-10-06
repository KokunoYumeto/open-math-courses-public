"""Exact analytic equation24 contours, sampled for rendering. Original sources: CC0."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT=Path(__file__).resolve().parent
STEM=OUT/"oblique-wave-point-source-outer-front-023"
a0=2.;b=math.sqrt(3)/2;c=.5
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
    "mathtext.fontset":"dejavusans","svg.fonttype":"none",
    "svg.hashsalt":"AN02-GF-point-source-outer-front-023"})
fig,axes=plt.subplots(1,2,figsize=(15.6,7.2),gridspec_kw={"width_ratios":[1.65,1]})
fig.subplots_adjust(left=.055,right=.98,bottom=.235,top=.735,wspace=.30)
fig.suptitle("A faster boundary pulse reaches the exact outer front",fontsize=21,y=.965)
fig.text(.5,.885,r"$a_0=2,\quad b=\sqrt{3}/2,\quad c=1/2,\quad"
    r"(\partial_t^2-\partial_a^2-\partial_z^2)G=\delta_{(2,0,0)},\quad"
    r"(\partial_a+b\partial_t)G|_{a=0}=0$",ha="center",fontsize=14)
ax=axes[0];levels=[];errors=[]
def tb(av,zv):
    rho=abs(zv);A=av+a0
    return math.hypot(A,rho) if rho<=c*A/b else b*A+c*rho
def check_points(aa,zz,time):
    for av,zv in zip(aa,zz):
        assert av>=-1e-12
        error=abs(min(math.hypot(av-a0,zv),tb(av,zv))-time)
        errors.append(error);assert error<2e-12
for time in range(1,9):
    if time<=a0/b:
        angle=math.pi if time<=a0 else math.acos(-a0/time)
        theta=np.linspace(-angle,angle,1601)
        aa=a0+time*np.cos(theta);zz=time*np.sin(theta)
        if time==a0:aa[np.abs(aa)<1e-14]=0
        join=None
    else:
        aj=b*time+(1-2*b*b)*a0-2*c*math.sqrt(b*a0*(time-b*a0))
        zj=(time-b*(aj+a0))/c
        angle=math.acos((aj-a0)/time)
        theta=np.linspace(-angle,angle,1601)
        aa=a0+time*np.cos(theta);zz=time*np.sin(theta)
        assert abs(math.hypot(aj-a0,zj)-time)<1e-12
        assert zj>=c*(aj+a0)/b and aj>=0
        line_a=np.linspace(0,aj,401)
        line_z=(time-b*(line_a+a0))/c
        check_points(line_a,line_z,time)
        check_points(line_a,-line_z,time)
        ax.plot(line_z,line_a,color="#c25d1d",linewidth=1.65)
        ax.plot(-line_z,line_a,color="#c25d1d",linewidth=1.65)
        join={"a":aj,"positive_z":zj,"boundary_z":(time-b*a0)/c,
            "analytic_formula":"a_join=b*t+(1-2*b^2)*a0-2*c*sqrt(b*a0*(t-b*a0)); z_join=(t-b*(a_join+a0))/c"}
    check_points(aa,zz,time)
    ax.plot(zz,aa,color="#22699b",linewidth=1.65)
    ax.text(.26,a0+time-.12,str(time),fontsize=10,color="#174e78",
        bbox={"facecolor":"white","alpha":.9,"edgecolor":"none","pad":.2})
    levels.append({"integer_time":time,"direct_circle_angle_interval":[-angle,angle],
        "circle_samples":len(aa),"fast_straight_branch":join,
        "line_samples_per_side":401 if join else 0})
ax.axhline(0,color="#303841",linewidth=1.5)
ax.scatter([0],[a0],marker="*",s=95,color="#1d2630",zorder=5)
ax.annotate(r"source $(a,z)=(2,0)$",xy=(0,a0),xytext=(-10.5,1.1),fontsize=11,
    arrowprops={"arrowstyle":"->","color":"#303841"},color="#303841",
    bbox={"facecolor":"white","alpha":.94,"edgecolor":"none","pad":.3})
ax.set(xlim=(-13.1,13.1),ylim=(-.15,10.65),xlabel="tangent spatial coordinate z",
    ylabel="normal spatial coordinate a")
ax.set_xticks([-12,-8,-4,0,4,8,12]);ax.set_yticks([0,2,4,6,8,10])
ax.set_aspect("equal",adjustable="box")
ax.spines[["right","top"]].set_visible(False)
ax.set_title("Outer fronts at integer times 1–8",fontsize=14,pad=15)
ax.legend(handles=[
    Line2D([0],[0],color="#22699b",lw=2,label="direct circle arc"),
    Line2D([0],[0],color="#c25d1d",lw=2,label="faster boundary pulse")],
    loc="upper left",frameon=False,fontsize=11)

ax=axes[1]
TB=math.sqrt(3)+1;T0=2*math.sqrt(2)
tt=np.linspace(T0+1e-8,3.015,1001)
D=(tt-b*a0)**2-c*c*4
tail=np.arccos((a0-b*tt)/np.sqrt(D))/(2*math.pi*c)
ax.axvspan(TB,T0,color="#e3edf6",zorder=0)
ax.plot([2.58,TB],[0,0],color="#22699b",linewidth=2.3)
ax.plot([TB,T0],[1,1],color="#22699b",linewidth=2.7)
ax.plot(tt,tail,color="#22699b",linewidth=2.3)
ax.plot([TB,TB],[0,1],linestyle=":",color="#c25d1d",linewidth=2)
ax.scatter([TB,TB],[0,1],facecolors="white",edgecolors="#c25d1d",s=34,zorder=5)
ax.axvline(T0,color="#66717d",linestyle="--",linewidth=1)
ax.annotate(r"$\Delta I=1\ \Longrightarrow\ \sqrt{3}\,\delta(t-T_B)$",
    xy=(TB,.52),xytext=(2.595,1.26),fontsize=13,
    arrowprops={"arrowstyle":"->","color":"#c25d1d"},color="#a44a15")
ax.annotate(r"$G=0$ between arrivals",xy=((TB+T0)/2,.08),xytext=(2.82,.32),fontsize=12,
    arrowprops={"arrowstyle":"->","color":"#315b80"},color="#315b80")
ax.text((TB+T0)/2,1.055,r"$I=1$",ha="center",fontsize=12,color="#174e78")
ax.text(2.989,.60,"I after the\nimage arrival",ha="right",fontsize=10,color="#22699b")
ax.set(xlim=(2.58,3.015),ylim=(-.08,1.42),xlabel="time t",ylabel="retarded integral I")
ax.set_xticks([2.6,TB,T0,3.0]);ax.set_xticklabels(["2.6",r"$T_B$",r"$T_0$","3.0"])
ax.set_yticks([0,.5,1])
ax.spines[["right","top"]].set_visible(False)
ax.set_title(r"A jump and an open gap at $(a,z)=(0,2)$",fontsize=13,pad=15)
fig.text(.5,.145,r"$T_B=\sqrt{3}+1<2\sqrt{2}=T_0,\qquad"
    r"G(0,2,t)=0\quad\mathrm{for}\ \sqrt{3}+1<t<2\sqrt{2}$",ha="center",fontsize=14)
fig.text(.5,.079,"Left: analytic outer fronts, with sampled circle arcs and exact straight branches; no filled-support shading.",
    ha="center",fontsize=11,color="#3b4551")
fig.text(.5,.038,"Right: the jump in the regular integral creates a Dirac pulse in G. A Dirac mass has no function height.",
    ha="center",fontsize=11,color="#3b4551")
fig.savefig(STEM.with_suffix(".svg"),metadata={"Date":"2026-10-02",
    "Creator":"GPT-6.1 Sol (OpenAI)","Title":"Exact oblique-wave point-source outer fronts",
    "Description":"Analytic integer-time front geometry and a nonzero faster pulse followed by an open zero region. Original CC0."})
fig.savefig(STEM.with_suffix(".png"),dpi=160,metadata={"Author":"GPT-6.1 Sol (OpenAI)",
    "Title":"Exact oblique-wave point-source outer fronts"})
plt.close(fig)
STEM.with_suffix(".json").write_text(json.dumps({"schema":"oblique-wave-front-geometry/v1",
    "a0_exact":"2","b_exact":"sqrt(3)/2","c_exact":"1/2","source_coordinates":["2","0","0"],
    "normal_coordinate":"a","tangent_spatial_coordinate":"z","time_coordinate":"t",
    "outer_front_proof_locator":"Equations22-25","pulse_gap_proof_locator":"Equations20-21 and Exercises2-3",
    "circle_parametrization":"a=a0+t*cos(theta), z=t*sin(theta)",
    "fast_branch":"b*(a+a0)+c*abs(z)=t, rho>=c*(a+a0)/b, TD>=t",
    "branch_join_derivation":"Intersect the circle (a-a0)^2+z^2=t^2 with b*(a+a0)+c*z=t on z>=0 and the admitted fast branch; choose the lower normal root.",
    "levels":levels,"rendering_samples_only":True,"analytic_geometry_proved_separately":True,
    "sampled_point_count":len(errors),"maximum_sampled_front_residual":max(errors),
    "boundary_example":{"a":0,"z":2,"fast_time_exact":"sqrt(3)+1","image_time_exact":"2*sqrt(2)",
        "I_jump_exact":"1","Green_pulse_coefficient_exact":"sqrt(3)",
        "open_Green_zero_interval":"(sqrt(3)+1,2*sqrt(2))"},
    "entire_filled_envelope_support_claimed":False,"license":"CC0-1.0"},
    ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(str(STEM.with_suffix(".png")))

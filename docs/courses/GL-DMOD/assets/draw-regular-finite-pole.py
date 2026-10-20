"""Original diagrams and a rigorously bounded finite-order Nilsson example."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":18,
                           "svg.hashsalt":"regular-finite-pole"})
blue,red,grey="#145da0","#a12b3a","#687587"
fig,axes=plt.subplots(3,1,figsize=(7.6,20.0),
                     gridspec_kw={"height_ratios":[1.0,1.22,1.04]})
fig.subplots_adjust(left=.10,right=.92,top=.955,bottom=.052,hspace=.82)
def line(a,y,t,color="black",size=20):
    a.text(.5,y,t,ha="center",va="center",fontsize=size,color=color,
           transform=a.transAxes)
a=axes[0];a.axis("off")
a.set_title("A. Actual finite flatness",fontsize=23,pad=18)
line(a,.91,r"$\operatorname{gr}\widehat E\ \mathrm{flat\ over}\ \operatorname{gr}D$",blue,23)
line(a,.71,"Leading-order corrections in the formal ring",grey,17)
line(a,.54,r"$\widehat E\otimes_D-\quad\mathrm{exact}$",blue,24)
line(a,.35,r"$\downarrow\quad\widehat E/E\ \mathrm{exact\ and\ faithful}$",size=20)
line(a,.15,r"$E\otimes_D-\quad\mathrm{exact}$",red,24)
line(a,-.035,"RF.7–RF.9: finite modules and actual normal completion",size=15)

a=axes[1]
box=a.get_position();a.set_position([.18,box.y0,.74,box.height])
t=np.linspace(.0005,.75,420);lam=Fraction(2,5)
coef=Fraction(1);value=np.zeros_like(t)
exact=[]
for n in range(200):
    if n:coef*=Fraction(5*n,5*n+2)
    value+=float(coef)*t**(n+float(lam))
    if n<=24:exact.append({"n":n,"numerator":str(coef.numerator),
                           "denominator":str(coef.denominator)})
bound=t**float(lam)/(1-t)
a.plot(t,value,color=blue,lw=2.5,label="200-term sum")
a.plot(t,bound,color=grey,lw=2,ls="--",label=r"$t^{2/5}/(1-t)$")
a.set_title("B. Every negative coefficient is retained",fontsize=21,pad=22)
a.set_xlim(0,.75);a.set_ylim(0,3.7)
a.set_xlabel(r"Positive real $t$  ($0<t\leq3/4$)")
a.set_ylabel("Value and proved bound")
a.grid(alpha=.18);a.legend(loc="upper left",fontsize=15,frameon=False)
a.text(.5,-.25,r"$P=\sum_{n\geq0}n!D_t^{-n},\qquad f=t^{2/5}$",
       ha="center",va="center",transform=a.transAxes,fontsize=21)
a.text(.5,-.40,r"$0\leq Pf-S_N\leq t^{2/5}\,\frac{t^{N+1}}{1-t}$",
       ha="center",va="center",transform=a.transAxes,fontsize=20,color=red)

a=axes[2];a.axis("off")
a.set_title("C. The finite tensor reconstruction",fontsize=21,pad=22)
a.text(.17,.88,r"$E\otimes_D M_p$",ha="center",va="center",fontsize=22,
       color=blue,transform=a.transAxes)
a.text(.82,.88,r"$E\otimes_D K_0$",ha="center",va="center",fontsize=22,
       color=blue,transform=a.transAxes)
a.annotate("",xy=(.66,.88),xytext=(.34,.88),xycoords="axes fraction",
           arrowprops={"arrowstyle":"->","lw":1.8,"color":blue})
a.text(.5,.98,r"$E\otimes e'$",ha="center",fontsize=20,transform=a.transAxes)
a.text(.53,.76,"injective by finite flatness",ha="center",fontsize=16,
       color=blue,transform=a.transAxes)
a.annotate("",xy=(.17,.38),xytext=(.17,.76),xycoords="axes fraction",
           arrowprops={"arrowstyle":"->","lw":1.8})
a.text(.095,.57,r"$\mu$",ha="center",fontsize=22,transform=a.transAxes)
a.text(.17,.27,r"$M_p$",ha="center",va="center",fontsize=24,
       color=blue,transform=a.transAxes)
a.annotate("",xy=(.76,.77),xytext=(.25,.36),xycoords="axes fraction",
           arrowprops={"arrowstyle":"->","lw":1.8})
a.text(.51,.46,r"$\phi$",ha="center",fontsize=23,transform=a.transAxes)
line(a,.045,r"$\phi\mu=E\otimes e',\qquad\mu\ \mathrm{is\ an\ isomorphism}$",red,20)
line(a,-.12,"RF.28–RF.33: finite poles and the whole characteristic fibre",size=15)

stem="regular-finite-pole"
fig.savefig(r/(stem+".png"),dpi=190,facecolor="white",metadata={"Software":"matplotlib"})
fig.savefig(r/(stem+".svg"),facecolor="white",metadata={"Date":None,"Creator":"matplotlib"})
plt.close(fig)
data={
 "kind":"original mathematical diagram and rigorously bounded real sample",
 "panels":{
  "A":{"proof":"RF.A; RF.7--RF.9","rings":["D","E","Ehat"],
       "formal_correcting_series_declared_actual":False,
       "descent":"exact faithful normal completion on finite actual E-modules"},
  "B":{"proof":"RF.C; RF.17--RF.20","lambda":{"numerator":2,"denominator":5},
       "operator":"sum_{n>=0} n! D_t^{-n}","input":"t^(2/5)",
       "coefficient":"a_n=n! / product_{s=1}^n(s+2/5)",
       "recurrence":"a_0=1; a_n=a_(n-1)*5*n/(5*n+2)",
       "exact_coefficients":exact,"plotted_terms":200,"largest_plotted_index":199,
       "domain":{"real_min_exclusive":0,"real_max_numerator":3,"real_max_denominator":4},
       "coefficient_bound":"0<a_n<=1",
       "tail_bound":"0<=P f-S_N<=t^(2/5)*t^(N+1)/(1-t), 0<t<1",
       "plotted_sum_tail_bound":"t^(2/5)*t^200/(1-t)",
       "plot_is_a_real_sample_of_a_complex_multivalued_function":True},
  "C":{"proof":"RF.H; RF.28--RF.33",
       "identity":"phi*mu=E tensor_D e_prime",
       "mu":"P tensor u maps to P*u","finite_flatness_used":True,
       "mixed_E_infinity_over_D_infinity_flatness_used":False}},
 "geometry_scale":"panels A and C are algebraic diagrams with no geometric scale",
 "sources":["https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf"]}
(r/(stem+"-exact-data.json")).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"generated":3,"terms":200,"exact_coefficients":len(exact)}))

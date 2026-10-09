"""Draw single Gaussian modes and their proved complex-time growth scales."""
from pathlib import Path
import json,os,tempfile
import mpmath as mp
mp.mp.dps=90
OWN=Path(__file__).resolve().parent;OUT=OWN/"figures";OUT.mkdir(exist_ok=True)
q=mp.mpf(32)
def scaled_W(y,h):
    a=mp.sqrt(q)*(y-h);c=mp.sqrt(q)/2
    return -mp.sqrt(mp.pi/q)/(4*q)*mp.exp(q/4)*(
        mp.exp(q*(y-h))*mp.erfc(a+c)+mp.exp(-q*(y-h))*mp.erfc(-a+c))
ys=[-1+mp.mpf(j)/50 for j in range(301)]
curves=[]
for h in [1,3]:
    forcing=[-(y-h)**2-1 for y in ys]
    particular=[-1+mp.log(abs(scaled_W(y,h)))/q for y in ys]
    curves.append(dict(h=h,forcing_rate=[mp.nstr(x,80) for x in forcing],
                       particular_rate=[mp.nstr(x,80) for x in particular]))
scales=[dict(h=h,forcing_threshold_exact=f"({h}^2+1)/{h}^2",
             forcing_threshold=mp.nstr((mp.mpf(h)**2+1)/h**2,80),
             tail_threshold_exact=f"({h}+3/4)/{h}^2",
             tail_threshold=mp.nstr((mp.mpf(h)+mp.mpf(3)/4)/h**2,80)) for h in range(1,9)]
with tempfile.TemporaryDirectory(prefix="an02-own260-mpl-") as cfg:
    os.environ["MPLCONFIGDIR"]=cfg
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig,(ax,bx)=plt.subplots(1,2,figsize=(13,4.8),gridspec_kw={"width_ratios":[1.35,1]})
    colors=["#256e98","#b35225"]
    for row,color in zip(curves,colors):
        h=row["h"]
        ax.plot([float(y) for y in ys],[float(v) for v in row["forcing_rate"]],
                ls="--",lw=1.7,color=color,label=f"Gaussian forcing, h={h}")
        ax.plot([float(y) for y in ys],[float(v) for v in row["particular_rate"]],
                lw=2,color=color,label=f"Particular solution, h={h}")
        ax.axvline(h,color=color,alpha=.15)
    ax.set(xlim=(-1,5),ylim=(-18,.1),xlabel="Spatial coordinate y",
           ylabel="log of absolute mode value / q",
           title="Gaussian sources have longer resolvent tails (q=32)")
    ax.legend(loc="lower center",fontsize=9,ncol=2);ax.grid(alpha=.2)
    hs=[v["h"] for v in scales]
    bx.plot(hs,[float(v["forcing_threshold"]) for v in scales],marker="o",color="#256e98",
            label="Forcing: (h²+1)/h²")
    bx.plot(hs,[float(v["tail_threshold"]) for v in scales],marker="s",color="#b35225",
            label="Tail: (h+3/4)/h²")
    bx.axhline(1,color="#256e98",ls=":",alpha=.5)
    bx.set(xlim=(.7,8.3),ylim=(0,2.15),xticks=hs,xlabel="Gaussian centre h",
           ylabel="Complex-time height σ at t=−iσ",
           title="Where each mode's leading exponential changes sign")
    bx.legend(loc="upper right",fontsize=9);bx.grid(alpha=.2)
    fig.tight_layout(w_pad=2.3)
    fig.savefig(OUT/"gaussian-sources-and-distant-tails.png",dpi=165,
                metadata={"Author":"GPT-6.1 Sol (OpenAI)"})
    fig.savefig(OUT/"gaussian-sources-and-distant-tails.svg",
                metadata={"Creator":"GPT-6.1 Sol (OpenAI)"})
    plt.close(fig)
geometry=dict(precision_decimal_digits=90,q="32",
    operator="Two-variable Laplacian with an additional analytic parameter;epsilon=0",
    x=0,t=0,y_samples=[mp.nstr(y,80) for y in ys],curves=curves,
    left_modes_are_finite_parameter_examples_not_the_actual_lacunary_sum=True,
    per_mode_complex_time_scales=scales,
    tail_scales_are_proved_q_to_infinity_leading_exponential_rates=True,
    individual_mode_growth_does_not_replace_the_global_solution_exclusion_argument=True,
    formal_proof_locators=["Lemma3.2","Lemma4.1","Lemmas5.1–5.4","Theorem1.1"])
(OUT/"geometry260.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(samples=len(ys)*4,figure_directory=str(OUT),
    temporary_font_cache_removed=not Path(cfg).exists())))

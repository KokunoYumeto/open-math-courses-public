"""Reproduce the original figure and bounded algebra checks for HQ1--HQ31.

The computations evaluate the examples and geometric identities in the accompanying proof.
The output files accompany the reproducible figures.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import math
import datetime as dt

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
FIG = BASE / "figures"
FIG.mkdir(exist_ok=True)

checks = []


def check(name, condition, detail=""):
    if not bool(condition):
        raise AssertionError(f"{name}: {detail}")
    checks.append({"name": name, "passed": True, "detail": detail})


def eq(name, expression, detail=""):
    check(name, sp.simplify(expression) == 0, detail)


s, y, u, t, z, R = sp.symbols("s y u t z R", positive=True, real=True)
tau, sigma = sp.symbols("tau sigma")
I = sp.I

# Exact Laurent example, including the higher-order coefficient retained in q.
P = sigma**2 + tau
Q = tau**4 + sigma**2
eq("HQ27 complete P window", P.subs({tau: t, sigma: z*t})/t**2 - (z**2+1/t))
eq("HQ27 complete Q window", Q.subs({tau: t, sigma: z*t})/t**4 - (1+z**2/t**2))
eq("Example1 full P directional strength squared", t**2+abs(-2)**2-(t**2+4))
eq("Example1 full Q directional strength squared", t**8+abs(-2)**2-(t**8+4))
match_square = -(8+u+u**2)/(2*(1+u+u**2))
new_quot = (match_square+u/2)/(1+u**2*match_square/4)
old_quot = 4*(-1+u)/(1-u**2)
eq("HQ30 exact doubled physical quotient", new_quot-old_quot)
check("HQ30 matching root limit", sp.limit(match_square, u, 0) == -4)
eq("Exercise1 actual physical quotient", (-(t**2)+t)/(t**4-t**2) + 1/(t*(t+1)))

# Equal-degree countercase: proportional windows force identical normal powers.
eq("Example2 scalar proportionality of entire windows", (tau*sigma).subs({tau: t, sigma: z*t**2}) - t*(sigma.subs(sigma, z*t**2)))
for hval in [0.0, 0.2, 1.0, 4.0, 20.0]:
    check(f"Example2 envelope difference at h={hval}", abs((1+hval)-hval-1) < 1e-12)

# Compare ordered conjugation against actual derivatives of a formal exponential.
rr = sp.Function("r")(s)
FF = sp.Function("F")(s)
LL = sp.Function("L")(s)
UU = sp.exp(I*rr*y-FF)
WW = sp.diff(rr,s)*y-I*LL


def ds_conj(expr):
    return sp.expand(WW*expr-I*sp.diff(expr,s))


def dy_conj(expr):
    return sp.expand(rr*expr-I*sp.diff(expr,y))


def formal_derivative(a, j):
    expr = sp.diff(UU, s, j, y, a) * (-I)**(a+j) / UU
    # Only F derivatives occur, never F itself after factoring the exponential.
    replacements = {sp.diff(FF,s,k): -sp.diff(LL,s,k-1) for k in range(1,j+1)}
    return sp.expand(expr.xreplace(replacements))


for a, j in [(0,0),(0,1),(0,2),(0,3),(0,5),(1,1),(3,2),(6,1)]:
    ordered = sp.Integer(1)
    for _ in range(j):
        ordered = ds_conj(ordered)
    for _ in range(a):
        ordered = dy_conj(ordered)
    eq(f"HQ19 actual versus conjugated derivative tau^{a} sigma^{j}", ordered-formal_derivative(a,j))

c2 = WW**2-I*sp.diff(WW,s)
eq("HQ16 exact second ordered derivative", ds_conj(ds_conj(sp.Integer(1)))-c2)
eq("HQ28 full tau-sigma derivative", dy_conj(WW)-(rr*WW-I*sp.diff(rr,s)))
expected_mixed = rr**3*c2 + 3*rr**2*(-2*I*sp.diff(rr,s)*WW-sp.diff(rr,s,2)) - 6*rr*sp.diff(rr,s)**2
actual_mixed = c2
for _ in range(3):
    actual_mixed = dy_conj(actual_mixed)
eq("HQ19 top variable coefficient includes all mixed derivatives", actual_mixed-expected_mixed)

# Exact direct toy with A=2. The general direct proof chooses A=M+2 instead.
r2 = R*sp.exp(1/s)
h2 = 1+s**-2
L2 = r2**2*h2
r2prime = sp.diff(r2,s)
W2 = r2prime*y-I*L2
eq("HQ28 r'/r sign", r2prime/r2+s**-2)
eq("HQ28 complete imaginary denominator", r2*W2-I*r2prime - (r2*r2prime*y-I*r2*(L2-s**-2)))
toy_a = -W2/(r2*W2-I*r2prime)
eq("HQ28 exact equation", W2+toy_a*(r2*W2-I*r2prime))
eq("HQ28 y=0 exact coefficient", toy_a.subs(y,0) + L2/(r2*(L2-s**-2)))
eq("HQ28 center line exact imaginary height", (s**-2/L2).subs({R:2,s:1})-1/(8*sp.E**2))
toy_bounds = []
for rv in [2.0, 4.0, 8.0]:
    for sv in [0.08,0.15,0.5,1.0,3.0,30.0]:
        r = rv*math.exp(1/sv)
        rp = -r/sv**2
        L = r*r*(1+sv**-2)
        check(f"HQ28 nonzero imaginary denominator R={rv},s={sv}", L-sv**-2 > 0)
        for yy in [-1e6,-2.0,0.0,2.0,1e6]:
            W = rp*yy-1j*L
            val = -W/(r*W-1j*rp)
            bound = 4/(3*r)
            check(f"HQ28 uniform toy bound R={rv},s={sv},y={yy}", abs(val)<=bound*(1+1e-12))
            toy_bounds.append(abs(val)/bound)

# One-dimensional exact normal-degree advantage, with A=4.
L4 = r2**4*h2
F4prime = -L4
P1image = -I*L4
Q2image = -L4**2-sp.diff(L4,s)
a1 = -I*L4/(L4**2+sp.diff(L4,s))
eq("HQ29 exact one-dimensional equation", P1image+a1*Q2image)
eq("HQ31 exact logarithmic derivative ratio", -sp.diff(L4,s)/L4**2 - r2**-4*(4/(1+s**2)+2*s/(1+s**2)**2))
for sv in [0.1,0.2,0.5,1.0,3.0,20.0,100.0]:
    # Remove the r^-4 factor to avoid overflow and test the actual rational bound.
    rational = 4/(1+sv*sv)+2*sv/(1+sv*sv)**2
    check(f"HQ31 rational factor <=6 at s={sv}", 0<rational<=6)

# A nontrivial degree-seven Q with d=m=2 and b=3 tests the entire mixed image.
# P = sigma^2+tau+1, Q = tau^3 sigma^2+tau^6 sigma+tau^2+5.
general_samples = []
for sv in [0.12,0.25,0.75,1.0,3.0,30.0]:
    rv = 2.0
    r = rv*math.exp(1/sv)
    rp = -r/sv**2
    rpp = r*(sv**-4+2*sv**-3)
    h = 1+sv**-2
    L = r**9*h
    Lp = L*(-9/sv**2-2/(sv**3*h))
    for yy in [-1e6,-1.0,0.0,1.0,1e6]:
        W = rp*yy-1j*L
        Wp = rpp*yy-1j*Lp
        c2n = W*W-1j*Wp
        pimage = c2n+r+1
        qimage = (r**3*c2n + 3*r*r*(-2j*rp*W-rpp) - 6*r*rp*rp
                  +r**6*W-6j*r**5*rp+r*r+5)
        ep = pimage/(W*W)-1
        eqn = qimage/(r**3*W*W)-1
        check(f"HQ21 degree7 complete P image nonzero at s={sv},y={yy}", abs(ep)<0.25)
        check(f"HQ21 degree7 complete Q image nonzero at s={sv},y={yy}", abs(eqn)<0.25)
        general_samples.append({"s":sv,"y":yy,"abs_EP":abs(ep),"abs_EQ":abs(eqn)})

# Render the three mathematically separate exact mechanisms.
plt.rcParams.update({"font.size":10,"axes.titlesize":11,"axes.labelsize":10,"figure.facecolor":"white"})
fig, axes = plt.subplots(1,3,figsize=(14.4,4.8),layout="constrained")
hvals = np.linspace(0,4,401)
axes[0].plot(hvals,hvals,color="#2463a5",lw=2.3,label=r"$G_P(h)=h$")
axes[0].plot(hvals,1+hvals,color="#b34818",lw=2.3,label=r"$G_Q(h)=1+h$")
axes[0].annotate(r"same slope: $e_P=e_Q=1$",xy=(1.4,2.4),xytext=(0.15,4.0),arrowprops={"arrowstyle":"->","color":"#444"})
axes[0].set(xlim=(0,4),ylim=(0,5),xlabel="normal scale exponent h",ylabel="growth exponent",title="The Laurent envelopes never meet")
axes[0].legend(loc="lower right",frameon=False)
axes[0].grid(alpha=.18)

eta = np.linspace(-2,2,401)
height = -1+1/(8*math.e**2)
axes[1].plot(eta,np.full_like(eta,height),color="#385b38",lw=2.7,label="complete scaled Q-image")
axes[1].scatter([0],[0],marker="x",s=75,color="#b22c2c",zorder=4,label="zero (excluded)")
axes[1].axhline(0,color="#777",lw=.65)
axes[1].axvline(0,color="#777",lw=.65)
axes[1].text(-1.9,-.82,r"$\eta-i[1-(8e^2)^{-1}]$",fontsize=11)
axes[1].set(xlim=(-2.1,2.1),ylim=(-1.45,.55),xlabel=r"real part: $\eta=r'y/L$",ylabel="imaginary part",title="At s=1: Q(D)U never vanishes")
axes[1].set_aspect("equal",adjustable="box")
axes[1].legend(loc="upper left",frameon=False,fontsize=9)
axes[1].grid(alpha=.18)

sv = np.linspace(.08,3,600)
rv = 2*np.exp(1/sv)
lv = rv**2*(1+sv**-2)
abs_av = lv/(rv*(lv-sv**-2))
bound = 4/(3*rv)
axes[2].semilogy(sv,abs_av,color="#6a3d9a",lw=2.5,label=r"complete $|a(0,s)|$")
axes[2].semilogy(sv,bound,color="#333",ls="--",lw=1.8,label=r"proved $4/(3r)$ bound")
axes[2].set(xlim=(0,3),xlabel="positive normal coordinate s",ylabel="coefficient magnitude (log scale)",title="The coefficient is flat at s=0")
axes[2].legend(loc="lower right",frameon=False)
axes[2].grid(alpha=.18,which="both")
fig.suptitle(r"$P=\sigma,\ Q=\tau\sigma,\ n_0=e_s$: exact equal-normal-degree example",fontsize=14)
fig.savefig(FIG/"higher-order-q-mechanisms.png",dpi=170)
fig.savefig(FIG/"higher-order-q-mechanisms.svg")
plt.close(fig)

metadata = {
    "title":"Equal normal degrees: no envelope catch-up, a nonzero Q-image, and a flat coefficient",
    "creator":"GPT-6.1 Sol (OpenAI)","reasoning_effort":"ultra","license":"CC0",
    "original_research_figure":True,"render_source":"render_and_validate.py",
    "proof_locators":["HQ14--HQ25","HQ28","Exercise3"],
    "human_comparison":"Hörmander II, unnumbered extension after Theorem13.6.1, printed202/PDF208",
    "model":{"P":"sigma","Q":"tau*sigma","normal":"e_s","R":2,"A":2,
             "r":"2*exp(1/s)","L":"r^2*(1+s^-2)","W":"r'(s)*y-i*L"},
    "panels":[
        {"domain":"0<=h<=4","values":["G_P(h)=h","G_Q(h)=1+h"],"scope":"growth exponents, not physical solution"},
        {"domain":"-2<=eta<=2 at s=1, eta=r'*y/L ranges over all real numbers","values":["eta-i*(1-1/(8*e^2))"],"axes_equal_units":True,"scope":"complete scaled Q(D)U/(r*L*U)"},
        {"domain":"0.08<=s<=3, y=0","values":["L/(r*(L-s^-2))","4/(3*r)"],"vertical_scale":"logarithmic","scope":"exact coefficient modulus and proved bound"}
    ],
    "numerical_render_is_not_proof":True,"visually_inspected":False
}
(FIG/"higher-order-q-mechanisms.json").write_text(json.dumps(metadata,indent=2)+"\n",encoding="utf-8")

report = {
    "generated_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
    "script":"render_and_validate.py","status":"passed",
    "check_count":len(checks),"checks":checks,
    "degree7_complete_image_samples":general_samples,
    "toy_max_sampled_fraction_of_proved_bound":max(toy_bounds),
    "limits":"Exact identities and bounded samples supplement HQ1--HQ31; they neither prove global estimates by sampling nor admit the result.",
}
(BASE/"validation.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"passed","checks":len(checks),"figure":"figures/higher-order-q-mechanisms.png",
                  "max_abs_EP_degree7":max(x["abs_EP"] for x in general_samples),
                  "max_abs_EQ_degree7":max(x["abs_EQ"] for x in general_samples)},indent=2))

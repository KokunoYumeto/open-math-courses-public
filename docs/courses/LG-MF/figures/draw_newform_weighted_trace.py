"""Reproducible diagram of the finite trace and common-level coefficient extraction."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(13, 11), dpi=170)
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.axis('off')

def text(x, y, label, size=15, **kw):
    return ax.text(x, y, label, ha='center', va='center', fontsize=size,
                   color='#16304c', **kw)

def box(cx, cy, w, h, label, size=15, color='#e7effb'):
    ax.add_patch(FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                 boxstyle='round,pad=0.012', linewidth=1.3,
                 edgecolor='#366089', facecolor=color))
    text(cx, cy, label, size)

def arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '->', 'lw': 1.7, 'color': '#366089'})

text(.5, .966, 'Finite weighted trace and removal of one support prime', 22, weight='bold')
text(.5, .923, r'$N=qL,\quad q\nmid L,\quad \chi_N\ \mathrm{descends\ to}\ \chi_L$', 18)
box(.18, .835, .24, .092, r'$f\in S_k(N,\chi_N)$', 18)
box(.58, .835, .40, .092, r'$F=f\Vert_k A_q,\quad H=\Gamma_0(L)\cap\Gamma^0(q)$', 17)
arrow((.315, .835), (.367, .835))
text(.343, .865, r'$A_q=\mathrm{diag}(1,q)$', 12)
text(.58, .758, r'$H\backslash\Gamma_0(L):\ T^t\ (0\leq t<q),\ R=A_q^{-1}W$', 17)
text(.58, .719, r'$\chi_L((T^t)_{22})^{-1}=\chi_L(R_{22})^{-1}=1$', 15)
box(.29, .607, .36, .11, r'$\sum_t F\Vert_kT^t=q^{1-k/2}U_qf$', 18)
box(.74, .607, .30, .11, r'$F\Vert_kR=f\Vert_kW$', 18)
text(.29, .573, 'level N', 11)
text(.74, .573, 'level N', 11)
arrow((.29, .697), (.29, .675))
arrow((.74, .695), (.74, .675))
box(.50, .44, .80, .105,
    r'$\Psi_q^N f=U_qf+q^{k/2-1}(f\Vert_k W)\ \in S_k(L,\chi_L)$', 21, '#e6f5ec')
arrow((.29, .539), (.34, .505))
arrow((.74, .539), (.66, .505))
text(.84, .464, 'Proposition 3.4', 9)
ax.plot([.06, .94], [.364, .364], color='#a7b8ce', lw=1)
text(.50, .329, r'$M=N\prod_i r_i^2,\quad r_i\ne q:\ \mathrm{one\ compatible}\ W\ \mathrm{works\ at}\ N\ \mathrm{and}\ M$', 17)
text(.50, .280,
     r'$\Psi_q^Nf=\sum_i V_{r_i}\Psi_i+(1+q^{-1})\Phi_t$', 22)
text(.50, .231,
     r'$\gcd(m,\prod_i r_i)=1\quad\Longrightarrow\quad a_m(V_{r_i}\Psi_i)=0$', 18)
arrow((.50, .211), (.50, .196))
box(.50, .149, .81, .074,
    r'$\phi=(1+q^{-1})^{-1}\Psi_q^Nf:\quad a_m(\phi)=a_{qm}(f)$', 22, '#e6f5ec')
text(.50, .077,
     r'$f-V_q\phi\in S_k(N,\chi_N),\quad\mathrm{support\ only\ at\ multiples\ of\ the}\ r_i$', 18)
text(.50, .035, 'The coefficient equality holds when the index is prime to every other support prime.', 11)
text(.50, .009, 'Proof: Lemma 3.3, Proposition 3.4 and Lemma 3.6. Source: Li, Newforms and functional equations.', 10)
fig.subplots_adjust(left=.025, right=.975, top=.99, bottom=.01)
fig.savefig(base/'newform-weighted-trace.png')
fig.savefig(base/'newform-weighted-trace.svg')
plt.close(fig)

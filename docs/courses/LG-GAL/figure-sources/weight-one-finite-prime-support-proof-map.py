"""Reproducible exact two-dimensional map of Theorem S, not a numerical model."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

PACKAGE = Path(__file__).resolve().parents[1]
fig = plt.figure(figsize=(9, 19), dpi=100, facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 900)
ax.set_ylim(0, 1900)
ax.axis('off')

ax.text(450, 1836, 'Finite-prime Fourier support', ha='center',
        fontsize=24, fontweight='bold', color='#12304b')
ax.text(450, 1795, 'Fixed character, arbitrary level and finite prime set',
        ha='center', fontsize=14, color='#334155')
ax.text(450, 1762, r'$f\in S_k(N,\chi),\quad C=\operatorname{cond}(\chi)\mid N$',
        ha='center', fontsize=16, color='#12304b')

def panel(top, height, title, lines, color='#e7f1fa'):
    ax.add_patch(FancyBboxPatch((38, top-height), 824, height,
                 boxstyle='round,pad=0,rounding_size=14',
                 facecolor=color, edgecolor='#57748d', linewidth=1.5))
    ax.text(64, top-38, title, fontsize=17, fontweight='bold', color='#12304b')
    for i, line in enumerate(lines):
        ax.text(64, top-79-i*34, line, fontsize=14, color='#172b40')

panel(1723, 226, '1. Filter the other primes — (S1), (S12)', [
    r'$P_r=B_rU_r$ keeps multiples of $r$; $A_r=1-P_r$ removes them.',
    r'Other primes $r_1,\ldots,r_t$: $F_p=A_{r_1}\cdots A_{r_t}f$.',
    r'$F_p\in S_k(M,\chi),\quad M=Nr_1^2\cdots r_t^2$; support only on $p$.',
    'The exponent of p in M is exactly its exponent in N.'
])
panel(1467, 224, '2. Ineligible primes disappear — Lemma S.2', [
    r'$p\nmid N:\quad F_p=0$ by descent and finite dimensionality.',
    r'$p\mid N,\ C\nmid N/p:\quad F_p=0$ by the character obstruction.',
    r'In either case: $f$ is already supported on $\mathcal{S}\setminus\{p\}$.',
    r'Remaining primes satisfy $p\mid N$ and $C\mid N/p$.'
], color='#fff2d6')
panel(1213, 190, '3A. Exponent at least two — Lemma S.3', [
    r'$p^2\mid N:\quad U_p f\in S_k(N/p,\chi).$',
    r'$f-B_pU_pf=A_pf\in S_k(N,\chi).$',
    'Its coefficients are supported on the other primes. Induct.'
])
panel(993, 292, '3B. Exponent one — (S8)–(S11)', [
    r'$p\parallel N:\quad H=\Gamma_0(N/p)\cap\Gamma^0(p).$',
    r'$H\backslash\Gamma_0(N/p):\ [1:j]\ (0\leq j<p),\ [0:1].$',
    r'$Q=U_p+p^{k/2-1}(|_kV),\quad \det V=p.$',
    r'$Qf\in S_k(N/p,\chi),\quad QB_ph=(1+p^{-1})h.$',
    r'$Q^M B_r=B_r Q^{M/r}\quad(r\ne p)$ with compatible matrices.',
    'All coset representatives have descended character value one.'
])
panel(671, 224, '4. Return to N in case 3B — (S13)–(S15)', [
    r'$g_p=Qf/(1+p^{-1})\in S_k(N/p,\chi).$',
    r'$f-B_pg_p\in S_k(N,\chi)$ is supported on the other primes.',
    r'$M=Nr_1^2\cdots r_t^2$ is used to prove this support identity.',
    'The induction itself runs at N, never at the inflated level M.'
], color='#fff2d6')
panel(417, 223, 'Conclusion — Theorem S and Corollary S.4', [
    r'$f=B_{p_1}g_{p_1}+\cdots+B_{p_s}g_{p_s},\quad g_{p_i}\in S_k(N/p_i,\chi).$',
    r'Eligible indices: $p_i\in\mathcal{S},\ p_i\mid N,\ C\mid N/p_i$.',
    r'For a new good eigenvector, $a_1=0$ forces $f=0$.',
    'Hence each simultaneous good eigenspace in the new space is a line.'
])
for upper, lower in [(1497,1467),(1243,1213),(701,671),(447,417)]:
    ax.annotate('', xy=(450, lower+5), xytext=(450, upper-5),
                arrowprops={'arrowstyle':'->', 'color':'#466780', 'lw':2})
# Case 3B branches from panel 2; case 3A goes directly to the induction result.
ax.plot([862, 885, 885], [1310, 1310, 890], color='#466780', lw=2)
ax.annotate('', xy=(862, 890), xytext=(885, 890),
            arrowprops={'arrowstyle':'->', 'color':'#466780', 'lw':2})
ax.plot([38, 15, 15], [1090, 1090, 310], color='#466780', lw=2)
ax.annotate('', xy=(38, 310), xytext=(15, 310),
            arrowprops={'arrowstyle':'->', 'color':'#466780', 'lw':2})

ax.text(450, 137, 'Exact proof locators: Lesson 13 §3.2B, Lemmas S.1–S.3 and (S1)–(S16).',
        ha='center', fontsize=12, color='#334155')
ax.text(450, 108, 'Free source: W. Li, Newforms and functional equations (1975), pp. 287–293.',
        ha='center', fontsize=12, color='#334155')
ax.text(450, 79, 'Schematic of the maps with the hypotheses displayed above.',
        ha='center', fontsize=11, color='#475569')
fig.savefig(PACKAGE/'assets/weight-one-finite-prime-support-proof-map.png', dpi=100,
            metadata={'Software':'Matplotlib', 'Title':'Finite-prime Fourier-support proof map'})
plt.close(fig)


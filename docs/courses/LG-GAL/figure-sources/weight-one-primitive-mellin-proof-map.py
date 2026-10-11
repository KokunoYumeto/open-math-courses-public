"""Reproducible exact proof map for the primitive Mellin companion."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

PACKAGE = Path(__file__).resolve().parents[1]
fig, ax = plt.subplots(figsize=(9, 21), dpi=100)
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0, 900), ylim=(0, 2100))
ax.axis('off')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.text(450, 2050, 'Primitive Mellin continuation', ha='center', fontsize=22,
        weight='bold', color='#17324d')
ax.text(450, 2011, r'Every $k\geq1$, every level $N$, every fixed character $\chi$',
        ha='center', fontsize=13, color='#394b63')


fig.canvas.draw()
renderer = fig.canvas.get_renderer()
current_top = 1960
panel_extents = []


def panel(title, lines, colour='#e8f1fa'):
    global current_top
    top = current_top
    ax.text(72, top-30, title, fontsize=16, weight='bold', color='#17324d', va='top')
    cursor = top-76
    for line in lines:
        text = ax.text(72, cursor, line, fontsize=12.5, color='#17324d', va='top')
        bounds = text.get_window_extent(renderer=renderer)
        assert bounds.x1 <= 830, 'Body line exceeds the panel width.'
        cursor -= bounds.height+12
    bottom = cursor-12
    assert bottom >= 270, 'Body panels encroach on the provenance footer.'
    ax.add_patch(FancyBboxPatch((50, bottom), 800, top-bottom,
                              boxstyle='round,pad=0,rounding_size=14',
                              facecolor=colour, edgecolor='#597f9f', linewidth=1.5))
    panel_extents.append((top, bottom))
    current_top = bottom-35


panel('1. Coefficients give all Euler factors — F.9', [
    r'$|a_n|\leq Be^{2\pi}n^{k/2}$: the series is absolute for $\operatorname{Re}s>k/2+1$.',
    r'$p\nmid N:\ a_{pn}=a_pa_n-\chi(p)p^{k-1}a_{n/p}$; $p\mid N:\ a_{pn}=a_pa_n$.',
    r'Prime-power induction gives $a_n=\prod_{p^r\parallel n}a_{p^r}$.',
    r'Good factor: $(1-a_pp^{-s}+\chi(p)p^{k-1-2s})^{-1}$; bad: $(1-a_pp^{-s})^{-1}$.',
])
panel('2. Both cusp ends give an entire integral — F35', [
    r'$f(iy)=O(e^{-2\pi y})$ as $y\to\infty$.',
    r'Fricke gives $f(iy)=O(y^{-k}e^{-2\pi/(Ny)})$ as $y\to0^+$.',
    r'$\Lambda(s,f)=N^{s/2}\int_0^{\infty}f(iy)y^{s-1}\,dy$ for every complex $s$.',
    r'Each parameter derivative adds $(\log y)^r$; both tails still converge.',
])
panel('3. The reciprocal Gamma factor is proved locally — F32–F34', [
    r'$G_m(s)=s\,m^{-s}\prod_{j=1}^{m}(1+s/j)$; $\gamma=\lim(H_m-\log m)$.',
    r'$G(s)=s e^{\gamma s}\prod_{j=1}^{\infty}(1+s/j)e^{-s/j}$ is entire.',
    r'For $|s|\leq R$, $j>2R$: $|\log(1+s/j)-s/j|\leq2R^2/j^2$.',
    r'The beta integral proves $G(s)\Gamma(s)=1$ for $\operatorname{Re}s>0$.',
    r'The simple zeros of $G$ are $0,-1,-2,\ldots$; the tail product is nonzero.',
], '#fff2d9')
panel('4. The exact phase and reflection — F.10', [
    r'$f|_kW_N=\omega_fJf$, $|\omega_f|=1$, gives',
    r'$f(i/(Ny))=i^k\omega_f N^{k/2}y^kJf(iy)$.',
    r'The substitution $y=1/(Nt)$ gives $\Lambda(s,f)=i^k\omega_f\Lambda(k-s,Jf)$.',
    r'$\varepsilon_f=i^k\omega_f$, $|\varepsilon_f|=1$, $\varepsilon_{Jf}=\overline{\varepsilon_f}$.',
    r'$L(s,f)=(2\pi)^sN^{-s/2}G(s)\Lambda(s,f)$ is entire.',
    r'Initially $\Lambda=N^{s/2}(2\pi)^{-s}\Gamma(s)L(s,f)$; all constants are retained.',
])
panel('5. The weight-one modular premises are all supplied', [
    r'At $k=1$: the primitive Fricke equation has phase $i\omega_f$.',
    r'Every bad factor is $(1-a_pp^{-s})^{-1}$, with $|a_p|\leq1$ by F.5–F.6.',
    r'Exercise 7.9: $Jf=f$, $\omega_f=-i$ gives $\varepsilon_f=1$.',
    'Residual-representation existence and the Artin equation remain separate proofs.',
], '#e5f4e9')
for (_, upper), (lower, _) in zip(panel_extents, panel_extents[1:]):
    ax.annotate('', xy=(450, lower+5), xytext=(450, upper-5),
                arrowprops={'arrowstyle': '->', 'color': '#446983', 'lw': 2})
ax.text(450, 211, 'Complete written proof: Lemma F.9, Theorem F.10 and F27–F39; Exercise 7.9.',
        ha='center', fontsize=10.5, color='#394b63')
ax.text(450, 177, 'Fricke input: local F.3; free human source Li (1975), printed294–297.',
        ha='center', fontsize=10.5, color='#394b63')
ax.text(450, 128, 'Lesson 13 §3.2D proves the Euler factors, Gamma continuation and exact phase.',
        ha='center', fontsize=11.5, color='#754820')
fig.savefig(PACKAGE / 'assets/weight-one-primitive-mellin-proof-map.png', dpi=100,
            facecolor=fig.get_facecolor())
plt.close(fig)

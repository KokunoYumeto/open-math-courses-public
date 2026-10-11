"""Exact uniform full-ring proof map, accompanying public 6.0AQ.1–6.0AQ.8.

Page coordinates are layout coordinates. No plot is a numerical sample of
the valuation parameter range. Labels preserve actual fields, rings, inverse
maps, normalized valuations, full determinants and both parity classes.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.text import Text

work = Path(__file__).resolve().parent.parent / 'assets'
assert len(sys.argv) <= 3
out = Path(sys.argv[1]) if len(sys.argv) >= 2 else work / 'uniform-first-interval-odd-second-equality-proof-map.png'
prefix = sys.argv[2] if len(sys.argv) == 3 else '6.0AQ'
assert prefix in {'AW', '6.0AQ'}
ink, blue, green, red = '#172b40', '#245c91', '#16705a', '#a23a3a'
fig = plt.figure(figsize=(9, 46), dpi=100, facecolor='#f5f8fc')
fig.text(.055, .983, 'One construction covers the whole first interval', fontsize=20, weight='bold', color=ink, va='top')
fig.text(.055, .971, 'Entire integer rings, finite scalar lifting and original indices', fontsize=13, color=blue, va='top')
fig.text(.055, .96, f'Proof {prefix}.1–8 • all integer parameters • arbitrary allowed units and higher coefficients', fontsize=10, color=ink, va='top')
panels = []


def panel(n, title, locator):
    top = .945 - (n-1)*.123
    ax = fig.add_axes([.045, top-.114, .91, .114])
    panels.append(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.add_patch(FancyBboxPatch((.005, .01), .99, .98, boxstyle='round,pad=.004,rounding_size=.018', facecolor='white', edgecolor='#cbd8e8', linewidth=1.1))
    ax.text(.025, .94, f'{n}. {title}', fontsize=15, weight='bold', color=ink, va='top')
    ax.text(.025, .871, locator, fontsize=10, color=blue, va='top')
    return ax


def line(ax, y, text, size=14, color=ink, x=.035):
    ax.text(x, y, text, fontsize=size, color=color, va='top')


def box(ax, xy, width, height, text, size=16):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle='round,pad=.008,rounding_size=.014', facecolor='#f4f8fc', edgecolor=green, linewidth=1.1))
    ax.text(xy[0]+width/2, xy[1]+height/2, text, fontsize=size, color=ink, ha='center', va='center')


def arrow(ax, start, end, text=''):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=14, color=blue, linewidth=1.5))
    if text:
        ax.text((start[0]+end[0])/2, (start[1]+end[1])/2+.022, text, fontsize=10, color=blue, ha='center', va='bottom')


ax = panel(1, 'The exact domain and original invariants', f'{prefix}.1–2; M = 9 comes from the earlier model, minimality and Euler proofs')
line(ax, .79, r'$k=v(a_2)\geq3\ \mathrm{odd},\quad 2e=3k-5,\quad e=v(2)$', 16)
line(ax, .683, r'$k\leq h=v(a_1)\leq2k-3,\quad q=2k-h,\quad 3\leq q\leq k$', 15)
line(ax, .575, r'$v(a_3)\geq(3k+1)/2,\quad v(a_4)\geq2k,\quad v(a_6)=5$', 15)
line(ax, .474, 'First, second and sixth units are arbitrary; third or fourth may be zero.', 11)
line(ax, .389, r'$m=2q-5>0\ \mathrm{odd},\quad v(b_2)=2h,\quad v(b_8)=4k-m$', 15)
line(ax, .284, r'$d=v(\Delta)=6k=4e+10,\quad v(c_4)=4h,\quad M=9$', 16, green)
line(ax, .174, r'$v(j)=12h-6k\geq6k>0$; both parities of $q$ are included.', 13)
line(ax, .082, 'For k = 3 the interval is a single point. Section 6.0AO supplies h ≥ 2k − 2.', 10)

ax = panel(2, 'Both entire quartic bases and the original determinant', f'{prefix}.3; e(F/K) = 4, residue degree 1; the determinant uses the first C-basis')
line(ax, .79, r'$\theta=\pi^k/x,\quad x=\pi^k/\theta,\quad P(T)=uT^4+r_1T^3+r_2T^2+r_3T+3\pi^m$', 12)
line(ax, .693, r'$v(u)=0,\quad v(r_1)=m,\quad v(r_2)\geq e+q-2,\quad v(r_3)=2e$', 13)
line(ax, .6, r'$C=R\oplus R\theta/\pi^{n_1}\oplus R\theta^2/\pi^{n_2}\oplus R\theta^3/\pi^{n_3},\quad n_j=\lfloor jm/4\rfloor$', 13, green)
line(ax, .493, r'$m=4r+1:\ (a,b)=(1,r);\qquad m=4r+3:\ (a,b)=(3,3r+2)$', 13)
line(ax, .4, r'$\varpi=\theta^a/\pi^b,\quad v_F(\varpi)=1,\quad C=R\oplus R\varpi\oplus R\varpi^2\oplus R\varpi^3,\quad v_F=4v$', 12)
line(ax, .303, r'$J=n_1+n_2+n_3=3(m-1)/2,\quad D_4=6m-2J=6q-12$', 15)
line(ax, .195, r'$N(\theta)=3\pi^m/u,\quad\det(1,x,x^2,x^3)=\pi^{6k+J}/N(\theta)^3$', 13)
line(ax, .095, r'$i_4=6k+J-3m=3h+6$; order discriminant $6m$, full different $D_4$.', 13, green)

ax = panel(3, 'An unbounded finite induction leaves one odd error', f'{prefix}.4; every competing square in the entire field F is exhausted')
line(ax, .8, r'$A=a_1x+a_3,\quad Y=y+A/2,\quad U=x^3+a_2x^2+a_4x+a_6+(A/2)^2$', 12)
line(ax, .732, r'$V=U/\varpi^{20},\quad S=A/(2\varpi^{10}),\quad v_F(S)\geq2$', 13)
line(ax, .664, r'$X=\theta^4/\pi^m,\quad \pi/\varpi^4=X^{-a},\quad\theta/\varpi^m=X^{-b}$', 13)
line(ax, .596, r'$X=\alpha+\gamma\theta^3+O(\varpi^{t+1}),\quad t=3m=6q-15$', 13)
line(ax, .528, r'$\alpha=-3/u,\quad\gamma=-r_1/(\pi^m u),\quad\eta=a_6/\pi^5$', 13)
line(ax, .46, r'$V-S^2=\mu+\lambda\varpi^t+O(\varpi^{t+1}),\quad\mu=\eta\alpha^{-5a}$', 13)
line(ax, .392, r'$\lambda=-5a\eta\gamma\alpha^{-5a-1-3b}\in R^{\times},\quad4e-t=6(k-q)+5>0$', 12)
line(ax, .324, r'$N=\lfloor t/4\rfloor:\quad N=3r\ (m=4r+1),\quad N=3r+2\ (m=4r+3)$', 12)
line(ax, .256, r'At step $j$, lift a residue square root of $(\mu-\sum c_i^2\alpha^{ai}\pi^i\ (i<j))\pi^{-j}\alpha^{-aj}$.', 11)
line(ax, .188, r'$c_* =\sum c_j\varpi^{2j}\ (0\leq j\leq N),\quad v_F(\mu-c_*^2)>t,\quad g=S+c_*$', 13)
line(ax, .12, r'For every $s\in F$: $v_F(V-s^2)\leq t=v_F(V-g^2)$; $t$ is odd.', 13, green)
line(ax, .052, 'A further correction has an even square value; its cross term is above t.', 10)

ax = panel(4, 'The full point ring recovers the same original point', f'{prefix}.5; all shifts and inverse maps retain the actual original y-coordinate')
line(ax, .79, r'$j_0=(t-1)/2=3q-8,\quad w=(Y/\varpi^{10}-g)/\varpi^{j_0}$', 16, green)
line(ax, .682, r'$w^2+(2g/\varpi^{j_0})w+(g^2-V)/\varpi^{2j_0}=0$', 16)
line(ax, .575, r'$v_F(2g/\varpi^{j_0})=4e-j_0\geq7,\quad v_F((g^2-V)/\varpi^{2j_0})=1$', 13)
line(ax, .475, r'Eisenstein: entire $B=C[w]$, $[L:F]=2$, residue degree $1$, $v_L=2v_F$.', 12)
box(ax, (.035, .3), .92, .115, r'$y=\varpi^{10+j_0}w+c_*\varpi^{10}$', 20)
line(ax, .268, r'Basis columns in $(1,w)$: $(1,0)$ and $(c_*\varpi^{10},\varpi^{10+j_0})$.', 13)
line(ax, .169, r'$\ell=10+j_0=3q+2,\quad d_{L/F}=8e-2j_0=8e-6q+16$', 15, green)
line(ax, .073, r'Derivative values $8e+1$ and $8e-2j_0$ differ by the exact positive value $t$.', 12)

ax = panel(5, 'Full rings prove the original-index identity first', f'{prefix}.6; residue degrees are one, so every displayed length has its actual weight')
box(ax, (.035, .65), .22, .125, r'$R\subset K$', 17)
box(ax, (.39, .65), .22, .125, r'$C\subset F$', 17)
box(ax, (.745, .65), .22, .125, r'$B\subset L$', 17)
arrow(ax, (.264, .712), (.378, .712), 'degree 4')
arrow(ax, (.619, .712), (.733, .712), 'degree 2')
line(ax, .577, r'$i_4=6k-3q+6,\quad\ell=3q+2,\quad i_8=2i_4+\ell=12k-3q+14$', 14)
line(ax, .462, r'$D_4=6q-12,\quad D_8=2D_4+d_{L/F}=8e+6q-8$', 17)
line(ax, .348, r'$2d-2i_4=D_4,\quad6d-2i_8=D_8,\quad\nu=0$', 17)
box(ax, (.035, .145), .92, .125, r'$i_4+\ell=6k+8=d+M-1$', 22)
line(ax, .065, 'Both entire rings and original determinants have been proved before Swan use.', 11)

ax = panel(6, 'Wild scalar −I acts on the whole Tate module', f'{prefix}.6; the labels below are nonzero torsion-basis vectors, not curve coordinates')
for i, label in enumerate(['(1,0)', '(0,1)', '(1,1)', '(1,2)']):
    xx = .135+i*.235
    ax.text(xx, .79, label, fontsize=11, color=ink, ha='center')
    for yy in [.695, .5]:
        ax.add_patch(Circle((xx, yy), .025, facecolor=green, edgecolor='none'))
    ax.text(xx+.043, .695, f'$P_{i+1}$', fontsize=12, color=ink, va='center')
    ax.text(xx+.043, .5, f'$-P_{i+1}$', fontsize=12, color=ink, va='center')
    ax.add_patch(FancyArrowPatch((xx, .655), (xx, .54), arrowstyle='<->', mutation_scale=11, color=red, linewidth=1.2))
line(ax, .407, 'The pro-two wild kernel in the pro-three congruence kernel is trivial.', 11)
line(ax, .329, r'Wild image injects into $\mathrm{SL}_2(\mathbf{F}_3)$; its involution lifts exactly to $-I$.', 11)
line(ax, .249, r'Inertia-fixed vectors vanish: tame conductor $2$; $\epsilon_4=3$, $\epsilon_8=7$.', 12)
line(ax, .163, r'$\delta=(D_8-D_4-4)/2=4e,\quad f(E/K)=4e+2=d-8$', 16, green)
line(ax, .065, r'$M-1+f(E/K)=d$; the full different calculation supplies the Swan comparison.', 12)

ax = panel(7, 'An endpoint family requires arbitrarily many lifts', f'{prefix}.7–8; the full twelve-point exercise and complete solution accompany this map')
line(ax, .79, r'$n\geq0,\quad K=\mathbf{Q}_2(\pi),\quad\pi^{3n+2}=2\quad\mathrm{(Eisenstein)}$', 15)
line(ax, .68, r'$k=q=h=2n+3,\quad e=3n+2,\quad a_1=a_2=\pi^{2n+3}$', 15)
line(ax, .571, r'$a_3=\pi^{3n+5},\quad a_4=\pi^{4n+6},\quad a_6=\pi^5$', 15)
line(ax, .468, r'$m=4n+1,\quad a=1,\quad b=n,\quad t=12n+3,\quad N=3n$', 16, green)
line(ax, .36, r'$d=12n+18,\quad i_4=6n+15,\quad\ell=6n+11$', 16)
line(ax, .258, r'$D_4=12n+6,\quad d_{L/F}=12n+14,\quad D_8=36n+26$', 15)
line(ax, .153, r'$i_8=18n+41,\quad\delta=12n+8,\quad f(E/K)=12n+10$', 15)
line(ax, .057, 'Every n is proved by the uniform argument; a finite list of cases is not used.', 11)

fig.text(.055, .067, 'Human writing material: J. S. Milne, freely accessible Algebraic Number Theory notes,', fontsize=10, color=ink, va='top')
fig.text(.055, .057, 'Proposition 2.43; Proposition 7.55 and Remark 7.56. www.jmilne.org/math/CourseNotes/ANT.pdf', fontsize=9, color=ink, va='top')
fig.text(.055, .047, f'Every specialized assertion is proved in {prefix}.1–8 or in its exact earlier programme providers.', fontsize=9, color=ink, va='top')
fig.text(.055, .037, 'Together with Section 6.0AO, this covers h ≥ k, including infinity, under the remaining domain bounds.', fontsize=9, color=ink, va='top')
fig.text(.055, .027, 'Lower first/third/fourth values, other preparations and universal NF24 remain; full-course review is pending.', fontsize=9, color=ink, va='top')
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
text_bounds = []
for artist in fig.findobj(match=Text):
    if not artist.get_text():
        continue
    b = artist.get_window_extent(renderer)
    assert b.x0 >= 0 and b.y0 >= 0 and b.x1 <= 900 and b.y1 <= 4600, (artist.get_text(), b.bounds)
    if artist.axes in panels:
        ab = artist.axes.get_window_extent(renderer)
        assert b.x0 >= ab.x0 and b.x1 <= ab.x1 and b.y0 >= ab.y0 and b.y1 <= ab.y1, (artist.get_text(), b.bounds)
    text_bounds.append({'text':artist.get_text(), 'bounds_pixels':[b.x0,b.y0,b.x1,b.y1]})
for ax in panels:
    labels = [artist for artist in ax.findobj(match=Text) if artist.get_text()]
    for i, first in enumerate(labels):
        for second in labels[i+1:]:
            assert not first.get_window_extent(renderer).overlaps(second.get_window_extent(renderer)), (first.get_text(), second.get_text())
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor())
plt.close(fig)
record = {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'source':str(Path(__file__).resolve()),
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'output':str(out.resolve()),
          'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(), 'pixel_size':[900,4600],
          'proof_prefix':prefix, 'panels':7, 'text_bounds':text_bounds,
          'all_text_inside_canvas_and_own_panel':True, 'no_text_label_overlaps':True, 'actual_render_inspection_pending':True,
          'coordinate_boundary':'Page coordinates are schematic layout coordinates, never curve or valuation parameters.'}
print(json.dumps(record))

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent
fig = plt.figure(figsize=(15, 9), dpi=160, facecolor='#faf9f4')
grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.52], height_ratios=[1.2, .92],
                        left=.055, right=.975, bottom=.05, top=.86,
                        wspace=.12, hspace=.25)
fig.suptitle('A smooth target boundary can pull back to singular cusps',
             fontsize=21, color='#203e3b', fontweight='bold', y=.965)
fig.text(.055, .902,
         r'$f(x,y)=(u,v)=(x^2-y^3,\ x^2+y^3)$ in a chart of $(\mathbf{P}^1)^2$; target boundary $uv=0$',
         fontsize=14, color='#203e3b')

ax = fig.add_subplot(grid[0, 0], facecolor='#faf9f4')
t = np.linspace(-1.05, 1.05, 401)
ax.plot(t**3, t**2, color='#ba4e2e', lw=3,
        label=r'$h_1=0$: $C_0(t)=(t^3,t^2)$')
ax.plot(t**3, -t**2, color='#346b98', lw=2.6,
        label=r'$h_2=0$: $(t^3,-t^2)$')
ax.plot(t, t, color='#648232', lw=2, linestyle='--',
        label=r'$C_1(t)=(t,t)$')
ax.axhline(0, color='#a2a9a7', lw=.7)
ax.axvline(0, color='#a2a9a7', lw=.7)
ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), xlabel='$x$', ylabel='$y$')
ax.set_aspect('equal')
ax.set_title('Actual real slice of the pulled-back divisor', fontsize=13)
ax.legend(fontsize=10, loc='upper left', framealpha=.94)
ax.grid(alpha=.13)

txt = fig.add_subplot(grid[0, 1]); txt.axis('off')
lines = [
 ('Exact inverse module — no higher Tor', 16, True),
 (r'$N_f=f^*\overline{E}\,[1/(h_1h_2)]$, where $h_1=x^2-y^3$, $h_2=x^2+y^3$', 14, False),
 (r'$f^!M=N_f[2-2]=N_f$   (5.14a)–(5.14c)', 14, False),
 ('Boundary-contained curve', 15, True),
 (r'$h_1(C_0(t))=0$: localization inverts zero, so $C_0^!N_f=0$.', 13.5, False),
 ('Curve through the singular intersection', 15, True),
 (r'$h_1(C_1(t))=t^2(1-t)$, $h_2(C_1(t))=t^2(1+t)$', 14, False),
 (r'Both multiplicities are $2$; residue $=2A_1+2A_2$   (5.14d).', 14, False),
 (r'$A_1=\frac15I+J$, $A_2=\frac3{10}I+J$, $J=\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]$', 14, False),
 (r'Residue $=I+4J$: logarithmic and retains the nilpotent part.', 14, False),
]
y = .98
for s, size, bold in lines:
    if r'begin{smallmatrix}' in s:
        s = r'$A_1=\frac{1}{5}I+J$, $A_2=\frac{3}{10}I+J$; $J^2=0$, $J\ne0$'
    txt.text(0, y, s, fontsize=size, fontweight='bold' if bold else 'normal',
             color='#203e3b', va='top')
    y -= .106 if bold else .087

low = fig.add_subplot(grid[1, :]); low.axis('off')
low.text(0, .98, 'Singular fiber product: keep it inside the smooth product',
         fontsize=17, fontweight='bold', color='#203e3b', va='top')
low.text(0, .72, r'$T=Y^\prime\times X$ is smooth; $W=X\times_Y Y^\prime\subset T$ may be singular or nonreduced.',
         fontsize=15, color='#203e3b')
low.text(0, .47, r'$g^!f_*K\;\simeq\;s_*R\Gamma_W(t^!K)$   (5.14j)',
         fontsize=19, color='#344f81')
low.text(0, .20,
         'Local cohomology retains the supported operator directions. No smooth transfer on W is used.',
         fontsize=15, color='#203e3b')
fig.savefig(out/'arbitrary-inverse-transfer.png', facecolor=fig.get_facecolor())
fig.savefig(out/'arbitrary-inverse-transfer.svg', facecolor=fig.get_facecolor())

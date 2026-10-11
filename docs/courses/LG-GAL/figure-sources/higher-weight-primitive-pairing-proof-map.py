"""Reproduce the exact conditional pairing diagram; no numerical evidence."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw(output):
    fig = plt.figure(figsize=(9, 27), dpi=100, facecolor='#f6f8fb')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 900), ylim=(2700, 0))
    ax.axis('off')
    ink, line = '#193750', '#527c9f'
    ax.text(450, 57, 'The primitive determinant pairing', ha='center', va='center', fontsize=23, weight='bold', color=ink)
    ax.text(450, 98, r'Every $k\geq2$, level $N$, admissible $\chi$ and coefficient place $\lambda$', ha='center', fontsize=13, color=ink)
    ax.text(450, 124, 'Arithmetic objects and compatible comparison are explicit premises A1–A3.', ha='center', fontsize=12, color=ink)

    def panel(y, h, title, rows, fill='#e8f1fa'):
        ax.add_patch(FancyBboxPatch((45, y), 810, h, boxstyle='round,pad=0,rounding_size=12', facecolor=fill, edgecolor=line, linewidth=1.5))
        ax.text(68, y+31, title, fontsize=15.5, weight='bold', color=ink, va='center')
        for dy, content, size in rows:
            ax.text(68, y+dy, content, fontsize=size, color=ink, va='center')

    def arrow(y):
        ax.annotate('', xy=(450, y+22), xytext=(450, y), arrowprops={'arrowstyle':'->', 'color':line, 'lw':2})

    panel(160, 250, '1. The primitive complex constituent — local S.4 and F.2–F.4', [
        (77, r'$W_{f,K}\otimes_K\mathbf{C}=\mathbf{C} H(f)\oplus\mathbf{C} A(f^*)$', 17),
        (119, r'$f^*(z)=\overline{f(-\bar z)},\quad A(g)=[\overline{g(z)}(X-\bar zY)^m d\bar z]$', 14),
        (160, r'$m=k-2$. $A$ is antilinear; the second line has the full $f$-packet.', 14),
        (202, 'The complete local support and Fricke proofs precede the pairing.', 14),
    ])
    arrow(416)
    panel(445, 285, '2. The Fricke pullback and nonzero mixed value — equations (A5)–(A9)', [
        (76, r'$wA(f^*)=N^{m/2}\overline{\omega_{f^*}}A(f),\quad |\omega_{f^*}|=1$', 17),
        (121, r'$\alpha=\Psi(H(f),A(f^*))=-N^{m/2}\overline{\omega_{f^*}}(2i)^{m+1}\nu$', 15),
        (163, r'$\nu=\int_{\Gamma_1(N)\backslash\mathfrak{H}}|f(z)|^2y^m\,dx\,dy>0$', 16),
        (205, 'Cusp decay makes the integral finite; a nonzero disk makes it positive.', 13),
        (247, 'The analytic phase is not assumed algebraic. This basis is complex.', 13),
    ])
    arrow(736)
    panel(765, 245, '3. Nondegeneracy reaches every coefficient place — Theorem 3.3', [
        (76, r'Complex Gram rows: $(0,\alpha)$ and $(-\alpha,0)$; $\alpha\ne0$.', 16),
        (122, 'In a K-basis, cup and Fricke define a rational matrix P.', 14),
        (164, r'$\det P\ne0$ after $K\hookrightarrow\mathbf{C}\;\Longrightarrow\;\det P\ne0$ in every $K_\lambda$.', 15),
        (205, r'Compare the same $K$-matrix; no identification of $\mathbf{C}$ and $K_\lambda$.', 14),
    ])
    arrow(1016)
    panel(1045, 225, '4. Covariance proves the global determinant — equations (A10)–(A11)', [
        (75, r'$\Psi(\sigma x,\sigma y)=\chi_G(\sigma)^{-1}\chi_\ell(\sigma)^{1-k}\Psi(x,y)$', 16),
        (120, r'$\det W_{f,\lambda}=\chi_G^{-1}\chi_\ell^{1-k}$', 18),
        (164, r'$V=W^\vee:\qquad\det V_{f,\lambda}=\chi_G\chi_\ell^{k-1}$', 18),
        (201, 'A nonzero alternating basis value transforms by the determinant.', 13),
    ], '#e8f5ef')
    arrow(1276)
    panel(1305, 245, '5. Every stable rank-two lattice can be normalized — Proposition 3.4', [
        (74, r'$T=\mathcal{O} t_1\oplus\mathcal{O} t_2,\quad D_T=\mathcal{O}(t_1\wedge t_2)$', 18),
        (119, r'$a_T=\Psi_V(t_1,t_2)\ne0$: $a_T^{-1}\Psi_V$ has Gram matrix $J$.', 16),
        (162, r'$J$ has rows $(0,1)$ and $(-1,0)$; $\det J=1$.', 18),
        (207, 'The target determinant line carries the same Galois character.', 14),
    ])
    arrow(1556)
    panel(1585, 225, '6. Reduction is perfect and actually alternating, including at 2', [
        (76, r'$\overline{T}=T/\varpi T:\quad\det\overline{J}=1,\quad\overline{J}((s,t),(s,t))=st-ts=0$', 16),
        (122, r'$\det\overline{\rho}^{\mathrm{ss}}=\overline{\chi_G}\,\overline{\chi_\ell}^{k-1}$', 18),
        (164, 'Continuity and finite residue field give a finite residual image.', 14),
        (201, 'No irreducibility or integral Hecke projector is needed here.', 13),
    ], '#e8f5ef')
    arrow(1816)
    panel(1845, 265, '7. The natural coefficient lattice obstruction — equation (A13)', [
        (75, r'$\operatorname{Sym}^2\mathbf{Z}_2^2$: invariant anti-diagonal $(c,-c/2,c)$.', 17),
        (120, r'Integral $\Longrightarrow c=2u;\quad\det=c^3/2=4u^3\notin\mathbf{Z}_2^\times$.', 17),
        (165, 'This natural rank-three lattice has no perfect invariant self-pairing.', 14),
        (207, 'Rank-two scalar normalization does not assert natural integral perfectness.', 13),
        (243, 'Exercise 8.6 also shows a saturated restriction can be nonperfect.', 12.5),
    ], '#fff3dc')
    arrow(2116)
    panel(2145, 270, '8. The residual polynomial still needs geometric premises A4–A5', [
        (75, 'A4: good specialization and unramifiedness outside Nℓ.', 15),
        (120, 'A5: the full supersingular correspondence and coefficient trace.', 14),
        (165, r'$\det(X-\overline{\rho}^{\mathrm{ss}}(\operatorname{Fr}_p))=X^2-\overline{a_p}X+\overline{\chi(p)}p^{k-1}$', 15),
        (207, r'Good $p\nmid N\ell$. The determinant also handles scalar Frobenius.', 14),
        (243, 'The diagram does not construct arithmetic moduli or prove A4–A5.', 13),
    ], '#fff3dc')
    ax.text(450, 2490, 'Exact written proof: local §2.5/2.5A and §3.3, Theorem 3.3–Corollary 3.6.', ha='center', fontsize=12, color=ink)
    ax.text(450, 2525, 'Exercises 8.5–8.6 retain the phase, determinant, characteristic two and lattice distinction.', ha='center', fontsize=11.5, color=ink)
    ax.text(450, 2570, 'Free human sources: Li, printed 287–297; Deligne, original exposé 355, §3.20.', ha='center', fontsize=11.5, color=ink)
    ax.text(450, 2605, 'Their statements and geometry are inputs for the complete local argument, not proofs in its place.', ha='center', fontsize=11, color=ink)
    # Measure rendered labels at their final size; fit long formulas inside panels.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for label in ax.texts:
        bounds = label.get_window_extent(renderer=renderer)
        limit = 760 if label.get_ha() == 'left' else 810
        if bounds.width > limit:
            label.set_fontsize(label.get_fontsize() * limit / bounds.width)
    p = Path(output)
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=100, facecolor=fig.get_facecolor(), metadata={'Software':'Reproducible Galois representations proof diagram'})
    plt.close(fig)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(Path(__file__).resolve().parent.parent / 'assets/higher-weight-primitive-pairing-proof-map.png'))
    draw(parser.parse_args().output)

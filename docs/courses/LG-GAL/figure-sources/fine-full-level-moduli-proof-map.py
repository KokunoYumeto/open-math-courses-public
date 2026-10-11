"""Exact characteristic-zero fine-level construction; no sampled geometry."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def draw(output):
    fig = plt.figure(figsize=(9, 28), dpi=100, facecolor='#f6f8fb')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 900), ylim=(2800, 0))
    ax.axis('off')
    ink, edge = '#193750', '#527c9f'
    ax.text(450, 55, 'An actual fine full-level family', ha='center',
            fontsize=24, weight='bold', color=ink)
    ax.text(450, 94, 'Every M ≥ 3; every Noetherian Q-base, including nilpotents',
            ha='center', fontsize=14, color=ink)
    ax.text(450, 128, 'Exact affine slices, universal maps and the central sign',
            ha='center', fontsize=14, color=ink)

    def panel(y, height, title, rows, fill='#e8f1fa'):
        ax.add_patch(FancyBboxPatch((45, y), 810, height,
                    boxstyle='round,pad=0,rounding_size=12',
                    facecolor=fill, edgecolor=edge, lw=1.5))
        ax.text(65, y + 34, title, fontsize=16, weight='bold', color=ink)
        for offset, label, size in rows:
            ax.text(65, y + offset, label, fontsize=size, color=ink)

    panel(165, 345, '1. Actual torsion frames give a finite parameter scheme — (F1)–(F4)', [
        (82, r'$B=\mathbf{Q}[a,b,\Delta^{-1}],\quad\Delta=4a^3+27b^2$', 19),
        (125, r'$\mathscr{E}_B:\ y^2=x^3+ax+b,\quad O=[0:1:0]$', 19),
        (167, r'$\alpha:(\mathbf{Z}/M\mathbf{Z})^2_{F_M}\cong(\mathscr{E}_B[M])_{F_M},\quad P=\alpha(1,0),\ Q=\alpha(0,1)$', 17),
        (208, r'$F_M=\operatorname{Spec}R_M\longrightarrow\operatorname{Spec}B$ is finite étale.', 17),
        (249, r'$[M]P=[M]Q=O$ are section identities, not just fibre conditions.', 15),
        (291, r'$d=x(P)-x(Q)$ and $y(P)$ are units: a full frame excludes $Q=\pm P$, $2P=O$.', 14),
    ])
    panel(545, 385, '2. A unit of weight one removes every scaling — (F5)–(F8)', [
        (82, r'$R_u:(a,b,x,y)\longmapsto(u^4a,u^6b,u^2x,u^3y)$', 19),
        (126, r'$w=y(P)/d,\qquad w(R_u z)=u\,w(z)$', 21),
        (170, r'$W_M=\operatorname{Spec}C_M,\qquad C_M=R_M/(w-1)$', 19),
        (214, r'$F_M\cong W_M\times\mathbf{G}_m,\quad z\longmapsto(R_{w(z)^{-1}}z,w(z))$', 18),
        (258, r'$a_*=a/w^4,\quad b_*=b/w^6,\quad x_*=x/w^2,\quad y_*=y/w^3$', 18),
        (300, r'$R_M^{\mathbf{G}_m}=C_M$ by Laurent coefficients, also over rings with nilpotents.', 15),
        (342, 'The primary normalization uses a supplied unit and extracts no root.', 15),
    ])
    panel(965, 425, '3. The optional sign slice has an explicit descended cubic — (F9)–(F16)', [
        (82, r'$A=R_M/(d-1),\quad c=y(P),\quad\tau=R_{-1},\quad D=A^\tau$', 18),
        (125, r'$A=D\oplus Dc\cong D[T]/(T^2-v),\quad v=c^2\in D^\times$', 20),
        (168, r'$A\otimes_D A\cong A\times A$; the two roots $c,-c$ differ by the unit $2c$.', 15),
        (211, r'$\operatorname{Spec}D\cong W_M$; the sign action fixes $D$ and sends $c$ to $-c$.', 16),
        (254, r'$vY^2Z=X^3+aXZ^2+bZ^3,\quad P_D=(p,1),\quad Q_D=(p-1,r)$', 17),
        (297, r'$p=x(P),\quad r=y(Q)/c,\quad O=[0:1:0]$', 18),
        (340, r'Over $A$: $[X:Y:Z]\longmapsto[X:cY:Z]$ identifies the entire marked cubic.', 15),
        (383, 'The zero, group maps and full frame descend as scheme maps.', 15),
    ])
    panel(1425, 330, '4. Normalization glues on arbitrary test bases — (F17)–(F18)', [
        (82, r'$Y_M=W_M\cong\operatorname{Spec}D$ carries the universal elliptic family.', 17),
        (126, r'$\operatorname{Hom}_{\mathbf{Q}}(S,Y_M)\cong\{(E/S,\alpha)\}/\text{marked isomorphism}$', 18),
        (170, 'Local short coordinates normalize by w; their ring maps agree on overlaps.', 14.5),
        (212, 'A pointed scaling of normalized frames has u = 1; the marked isomorphism is unique.', 14),
        (255, 'The constructions commute with pullback; nilpotent units are retained.', 15),
        (295, 'Yₘ is a smooth affine curve over Q; all levels M ≥ 3 are included.', 15),
    ])
    panel(1790, 390, '5. Matrix maps retain an invisible base sign in the family — (F19)–(F24)', [
        (82, r'$g\in\operatorname{GL}_2(\mathbf{Z}/M),\quad r_g:\alpha\longmapsto\alpha g$', 19),
        (125, r'$w_g=w(r_g z),\quad T_g=R_{w_g^{-1}}r_g,\quad T_hT_g=T_{gh}$', 19),
        (168, r'$L_g:(z,x,y)\longmapsto(T_gz,x/w_g^2,y/w_g^3)$', 19),
        (211, r'$L_g\alpha_z=\alpha_{T_gz}g^{-1},\qquad L_hL_g=L_{gh}$', 19),
        (254, r'$T_{-I}=\operatorname{id}_{Y_M},\qquad L_{-I}=[-1]$', 22),
        (297, 'The two frames α and −α are isomorphic; −1 does not fix the same frame.', 14.5),
        (340, 'The universal family action must be retained in later coefficient descent.', 15),
    ], '#fff3dc')
    panel(2215, 385, '6. Pairing values label the actual geometric components — (F25)–(F26)', [
        (82, r'$h_M:Y_M\longrightarrow\operatorname{Spec}\mathbf{Q}(\zeta_M),\quad\epsilon_M=e_M(P,Q)$', 18),
        (125, r'$\epsilon_M$ is primitive; $h_MT_g=[\det g]h_M$.', 20),
        (168, r'Over $\overline{\mathbf{Q}}$: $\epsilon_M=\zeta_M^r$, $r\in(\mathbf{Z}/M)^\times$.', 18),
        (211, 'Each locus is a connected smooth curve; hence an irreducible component.', 15),
        (254, 'The written lattice uniformization proves this connectedness.', 15),
        (297, r'$\sigma(\zeta_M)=\zeta_M^u:\ r\longmapsto ur$; $T_{\operatorname{diag}(u^{-1},1)}$ returns the label.', 17),
        (340, 'Arithmetic transport uses the family lifts and keeps the central sign.', 15),
    ])
    ax.text(450, 2660, 'Exact proof: fine full-level §§1.0F.1–1.0F.10; (F1)–(F26), including components.',
            ha='center', fontsize=12, color=ink)
    ax.text(450, 2697, 'Free human comparison: Deligne–Rapoport, IV §5.1–5.4 (IAS original).',
            ha='center', fontsize=12, color=ink)
    ax.text(450, 2734, 'Foundations, coefficient descent, cusp/integral models, good primes and supersingular geometry remain open.',
            ha='center', fontsize=11.5, color=ink)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for label in ax.texts:
        bounds = label.get_window_extent(renderer=renderer)
        limit = 760 if label.get_ha() == 'left' else 810
        if bounds.width > limit:
            label.set_fontsize(label.get_fontsize() * limit / bounds.width)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for label in ax.texts:
        bounds = label.get_window_extent(renderer=renderer)
        assert bounds.x0 >= 35 and bounds.x1 <= 865, label.get_text()
    p = Path(output)
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=100, facecolor=fig.get_facecolor(),
                metadata={'Software': 'Reproducible fine full-level moduli construction'})
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(Path(__file__).resolve().parents[1] / 'assets/fine-full-level-moduli-proof-map.png'))
    draw(parser.parse_args().output)

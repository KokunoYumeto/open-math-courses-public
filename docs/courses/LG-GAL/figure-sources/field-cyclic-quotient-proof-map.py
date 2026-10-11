"""Reproducible field quotient, rigidity and Weil-alternation proof map."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def render(output):
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
    fig = plt.figure(figsize=(6, 14), dpi=150, facecolor='#f5f7fb')
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    ink = '#173650'
    def text(x, y, value, size=9.3, weight='normal', center=False):
        ax.text(x, y, value, color=ink, fontsize=size, fontweight=weight,
                ha='center' if center else 'left', va='top')
    def panel(top, bottom, title, lines, warm=False):
        ax.add_patch(FancyBboxPatch((.055, bottom), .89, top-bottom,
            boxstyle='round,pad=.008', linewidth=1, edgecolor='#517ca3',
            facecolor='#fff3dc' if warm else '#e8f1fa'))
        text(.077, top-.009, title, 10, 'bold')
        for y, value, size in lines: text(.077, y, value, size)
    text(.5, .983, 'A cyclic quotient explains alternation', 15, 'bold', True)
    text(.5, .959, 'Elliptic curves over an algebraically closed field k', 10, center=True)
    text(.5, .941, r'$m\geq1,\quad m\in k^\times,\quad P\in E[m],\quad s=\mathrm{ord}(P)\mid m$', 11, center=True)
    panel(.910, .663, '1. Invariant rings construct the scheme — §1.4A.1', [
        (.884, r'$H=\langle P\rangle,\quad U=\mathrm{Spec}\,A\subset E,\quad D=A^H$', 11),
        (.860, 'A finite orbit has a stable affine neighbourhood.', 9.6),
        (.839, 'Disjoint translation graphs give Chinese remaindering:', 9.6),
        (.818, r'$\Phi:A\otimes_D A\;\simeq\;\prod_{h\in H}A$  (W3)', 13),
        (.789, r'$\sum_i a_i h(b_i)=\delta_{h,1},\quad T(c)=\sum_h h(c)$', 11),
        (.763, r'$c=\sum_i a_i T(b_i c)$  (W4)–(W5)', 12),
        (.736, 'Finite projective, faithful and rank s; finite étale.', 9.6),
        (.713, r'$\beta:E\longrightarrow B,\quad H\times E\simeq E\times_B E$', 12),
        (.686, 'Stable opens glue; invariant scheme maps descend.', 9.6),
    ])
    panel(.640, .415, '2. Constants force the pointed laws to agree — §1.4A.2', [
        (.614, r'$\Gamma(C_R,\mathcal{O}_{C_R})=R$  (W8)', 13),
        (.583, 'C proper geometrically integral; every k-algebra R,', 9.6),
        (.563, 'including rings with nilpotents. A finite affine-cover', 9.6),
        (.543, 'kernel stays exact because k-modules are flat.', 9.6),
        (.516, r'$F(x,y)=f(x+y)-f(x)-f(y),\quad f(O_C)=O_D$', 11),
        (.490, 'On C × U its affine coordinate functions lie in R.', 9.6),
        (.470, 'The origin slice gives F = O; density and separatedness', 9.4),
        (.450, 'extend the scheme identity over C × C: f is a homomorphism.', 9.2),
        (.430, r'$g_B=1$; quotient law = pointed cubic law', 10.4),
    ])
    panel(.391, .105, '3. A principal divisor proves alternation — Lemma1.4 / 6.5', [
        (.365, r'$E\;\longrightarrow\;B\;\longrightarrow\;E,\quad v\beta=[m]$  (maps β, v)', 12),
        (.336, r'$\deg\beta=s,\qquad d=\deg v=m^2/s$', 12),
        (.309, r'$[m]R=P,\qquad D_P=v^*((P)-(O))$', 11.5),
        (.282, r'$\deg D_P=0,\qquad\sum D_P=d\beta R$', 12),
        (.253, r'$d\beta R=\beta([m/s]P)=O_B$  (W10)', 12),
        (.224, r'$D_P=\mathrm{div}\,h,\qquad g_P=\lambda(h\circ\beta),\quad\lambda\in k^\times$', 11),
        (.196, r'$g_P(X+P)=g_P(X),\qquad e_m(P,P)=1$', 12),
        (.166, 'This proves actual alternation for even and composite m;', 9.4),
        (.145, 's = 1 and m = 1 are included. No division by 2 is used.', 9.4),
        (.124, 'The reciprocal convention is e(A,Q) = gQ(X) / gQ(X+A).', 9.1),
    ], True)
    text(.5, .081, 'Exact proof: §§1.4A.1–1.4A.2; (W2)–(W8); Lemma1.4; Exercise6.5.', 8, center=True)
    text(.5, .062, 'Human source: Milne, free author notes, Abelian Varieties I §13, pp.57–58.', 8, center=True)
    text(.5, .043, 'The field construction supplies the pairing proof; general relative families', 8, center=True)
    text(.5, .026, 'require their own construction. Curve, étale and sheaf prerequisites are retained.', 8, center=True)
    fig.savefig(output, dpi=150, facecolor=fig.get_facecolor(), metadata={'Title': 'Field cyclic quotient, rigidity and actual Weil alternation'})
    plt.close(fig)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(Path(__file__).resolve().parents[1] / 'assets/field-cyclic-quotient-proof-map.png'))
    render(Path(parser.parse_args().output))

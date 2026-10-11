"""Original CC0 diagrams for Sections 11CA--11CC. No external artwork."""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matplotlib.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 12,
    'svg.fonttype': 'none', 'svg.hashsalt': 'ncg-general-reduced-graph-v1',
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.titleweight': 'bold', 'savefig.facecolor': 'white',
})
BLUE, RED, GREEN, GRAY = '#175a9b', '#aa3d32', '#26725a', '#4a5568'

def save(fig, out, slug):
    fig.savefig(out / (slug + '.png'), dpi=150,
                metadata={'Title': slug, 'Author': 'Original CC0 mathematical diagram'})
    fig.savefig(out / (slug + '.svg'),
                metadata={'Date': None, 'Creator': 'Original CC0 mathematical diagram'})
    plt.close(fig)

def metric(out):
    fig = plt.figure(figsize=(12, 7.2), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 3])
    title = fig.add_subplot(gs[0, :]); title.axis('off')
    title.text(.01, .88, 'Metric fibre: actual shear and a decaying phase error',
               fontsize=19, weight='bold')
    title.text(.01, .49, r'$q=2,\ d=3,\quad h(x_1,x_2)=(x_1+x_2^2/2,x_2)$', fontsize=16)
    title.text(.01, .13, r'At $x=0,\ g=I$: $D(h\!\cdot\!g)(v,B)=(v,B-v_2S)$, '
               r'$(S_{11},S_{12},S_{21},S_{22})=(0,1,1,0)$', fontsize=14)
    left = fig.add_subplot(gs[1, 0]); left.axis('off')
    left.text(.03, .94, 'Cotangent pullback on this retained fibre', weight='bold')
    left.text(.03, .78, r'$\xi_2\mapsto\xi_2-\langle\eta,S\rangle$' '\n'
              r'$L\eta=-\sqrt{2}\,\eta_S e_2,\quad\|L\|=\sqrt{2}$', fontsize=16)
    left.text(.03, .53, r'$R=(1+|\xi|^2+|\eta|^2)^{1/2}$' '\n'
              r'$b=(R^{-1/4}\xi,\eta),\quad f=b/\sqrt{1+|b|^2}$', fontsize=15)
    left.text(.03, .30, 'Positive vertical Bott + full total inverse\n'
              r'$z^q\,z^{-(q+1)}=z^{-1}$' '\n'
              'Full graded cancellation retains the original\n'
              r'positive $q$-disk and final right $\mathrm{Cl}_q$.', fontsize=13)
    left.text(.03, .06, 'Proofs: MB.12–MB.17; calibration MB.21.\n'
              'Transfer target: reduced metric-bundle algebra.', color=GRAY, fontsize=11)
    right = fig.add_subplot(gs[1, 1])
    radii = np.geomspace(2, 1e8, 420)
    sample_error = []
    for radius in radii:
        eta = radius**.75
        xi = np.sqrt(radius**2 - 1 - eta**2)
        radius2 = np.sqrt(1 + (xi - np.sqrt(2)*eta)**2 + eta**2)
        u = np.array([radius**(-.25)*xi, eta])
        v = np.array([radius2**(-.25)*(xi-np.sqrt(2)*eta), eta])
        sample_error.append(np.linalg.norm(v/np.sqrt(1+v@v)-u/np.sqrt(1+u@u)))
    constant = 1.25*np.sqrt(2)*(1+np.sqrt(2))**.25
    right.loglog(radii, sample_error, color=BLUE, lw=2.2,
                 label=r'Sampled ray: $\eta_S=R^{3/4}$')
    right.loglog(radii, constant*radii**(-.25), '--', color=RED, lw=2,
                 label=r'Uniform proof bound $C_LR^{-1/4}$')
    right.set(xlabel=r'Original cotangent radius $R$', ylabel='Coefficient-vector phase difference',
              title='The sample lies below the proved uniform bound')
    right.legend(fontsize=10, loc='lower left'); right.grid(alpha=.2, which='both')
    assert np.all(np.asarray(sample_error) <= constant*radii**(-.25))
    save(fig, out, 'metric-fibre-shear')

def classes(out):
    fig, ax = plt.subplots(figsize=(12, 7.2), layout='constrained'); ax.axis('off')
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.text(.02, .96, 'Specified descent and every attainable original-disk pairing',
            fontsize=19, weight='bold', va='top')
    boxes = [(.03, .65, 'Full class $x$\n' + r'Fixed final right $\mathrm{Cl}_q$'),
             (.39, .65, r'$\Omega(x)=p^*x$' '\nCone obstruction'),
             (.75, .65, r'$\Omega(x)=0$' '\nExactly: specified descent')]
    for x, y, text in boxes:
        ax.text(x, y, text, fontsize=13, va='center',
                bbox={'boxstyle': 'round,pad=.6', 'fc': '#edf4fa', 'ec': BLUE})
    for start, end in [(.29, .37), (.66, .73)]:
        ax.annotate('', (end, .65), (start, .65), arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2})
    ax.text(.03, .47, r'Fix $\beta_A(x_0)=1$.  $L=\ker\beta_A$, '
            r'$\epsilon=[\Omega(x_0)]\in O/\Omega(L)$.', fontsize=16)
    ax.text(.03, .34, r'All reduced pairings $=\{n\in\mathbb{Z}:n\epsilon=0\}$',
            fontsize=17, color=GREEN, weight='bold')
    ax.text(.03, .19, 'Actual commutative mapping-cylinder tests (OFD.1–OFD.4):', weight='bold')
    ax.text(.03, .09, r'$f_d(z)=z^d$   $\Longrightarrow$   cone group $\mathbb{Z}/d\mathbb{Z}$'
            '\n' r'$d=0$: infinite order, pairing $0$;  $d\geq1$: order $d$, pairings $d\mathbb{Z}$.', fontsize=14)
    ax.text(.03, -.015, 'Proofs: FCD.8–FCD.14. These algebraic tests do not assert a foliation identification.',
            fontsize=11, color=GRAY)
    save(fig, out, 'normalized-cone-pairings')

def joint(out):
    fig = plt.figure(figsize=(12, 7.2), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[.75, 3])
    title = fig.add_subplot(gs[0, :]); title.axis('off')
    title.text(.01, .83, 'Original rank seams: exact averaging and joint transport control',
               fontsize=18, weight='bold')
    title.text(.01, .28, r'$T=(\mathbb{R}/\mathbb{Z})^2\times(-2,2),\ q=3,$ '
               r'$\tau(x,y,t)=(x+1/2,y,t)$; every seam is retained.', fontsize=13)
    left = fig.add_subplot(gs[1, 0]); left.axis('off')
    left.text(.01, .94, 'Whole jet module: rank 3 in the closed middle,\nrank 6 on both open flat ends.', weight='bold')
    left.plot([.07,.93], [.68,.68], color=GRAY, lw=2)
    for x, label in [(.07,'−2'),(.28,'−1'),(.72,'1'),(.93,'2')]:
        left.plot(x,.68,'o',mfc='white' if abs(float(label.replace('−','-')))==2 else BLUE,
                  mec=BLUE,ms=8)
        left.text(x,.61,label,ha='center')
    left.text(.16,.75,'rank 6',ha='center'); left.text(.5,.75,'rank 3',ha='center'); left.text(.83,.75,'rank 6',ha='center')
    left.text(.01,.47, r'$a(x)=(2+\cos2\pi x)/3$' '\n'
              r'$a(x)+a(x+1/2)=4/3$' '\n'
              r'$\bar h=\lambda P_L+\lambda[\frac{2}{3}\rho(t-1)+\rho(-t-1)]P_W$', fontsize=13)
    left.text(.01,.23, 'Finite averaging is exactly covariant here.\nThe whole positive sum is one reduced nullhomotopy:\n'
              r'$H_u^2\geq(1-u)^2+u^2\geq1/2.$', fontsize=12)
    left.text(.01,.06, 'Full physical carrier and coherent inverse retained;\noriginal positive 3-disk pairing +1.\nProofs: JCN.25–JCN.29.', fontsize=11, color=GRAY)
    left.set(xlim=(0,1), ylim=(0,1))
    right = fig.add_subplot(gs[1, 1]); s=np.geomspace(.001, 1, 300)
    for r, color in [(1,BLUE),(4,RED),(16,GREEN),(64,'#8657a5')]:
        # Original points x=0 and tau(x)=1/2, highest W degree m=r.
        a0=1.; a1=1/3; m=r
        u=np.sqrt(1+m*(s**-2-np.log(a0)))
        v=np.sqrt(1+m*(s**-2-np.log(a1)))
        gap=np.abs(m*np.log(a1/a0)/(r*r*(u+v)))
        bound=np.minimum(np.log(3)/(2*r),np.sqrt(m)*s*np.log(3)/(2*r*r))
        assert np.all(gap<=bound*(1+1e-13))
        right.loglog(s,gap,color=color,lw=2,label=f'r=m={r}')
        right.loglog(s,bound,color=color,lw=1,ls='--')
    right.set(xlabel=r'Original distance $s=t-1>0$ to the upper seam', ylabel=r'$|\log c_{r,m}|$',
              title='Transport ratio: sample and proved bound')
    right.legend(fontsize=10); right.grid(alpha=.2, which='both')
    right.text(.03,.035, 'Completed sign comparison: JCR.1–JCR.7.\nJoint cutoff error: JCN.22.',
               transform=right.transAxes, fontsize=10, color=GRAY,
               bbox={'facecolor':'white','alpha':.9,'edgecolor':'none','pad':3})
    save(fig,out,'joint-covariant-rank-seam')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output', type=Path,
                         default=Path(__file__).resolve().parents[2]/'figures')
    out=parser.parse_args().output.resolve(); out.mkdir(parents=True, exist_ok=True)
    metric(out); classes(out); joint(out)
    print('Generated and numerically checked three original PNG/SVG pairs.')

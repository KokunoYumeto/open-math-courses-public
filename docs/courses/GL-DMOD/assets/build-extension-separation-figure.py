"""Draw the exact maps in EE.11--EE.28; no numerical proof claim."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', type=Path, default=Path(__file__).parent)
args = parser.parse_args()
args.output_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15,
                     'svg.hashsalt': 'GL-DMOD-EE-exact-diagram-v1'})
fig = plt.figure(figsize=(16, 10), dpi=150, facecolor='#f7f9fc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 16), ylim=(0, 10))
ax.axis('off')
ink, blue, green, muted = '#14223b', '#155ca5', '#17765d', '#52627a'

def txt(x, y, s, size=16, color=ink, **kw):
    return ax.text(x, y, s, fontsize=size, color=color, ha='center',
                   va='center', **kw)

def box(x, y, w, h, s, size=16, color=blue):
    patch = FancyBboxPatch((x-w/2, y-h/2), w, h,
                          boxstyle='round,pad=0.10,rounding_size=0.10',
                          facecolor='white', edgecolor=color, linewidth=1.5)
    ax.add_patch(patch)
    txt(x, y, s, size=size, color=ink)
    return patch

def arrow(a, b, label=None, label_pos=None, color=blue):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=15,
                                color=color, linewidth=1.7))
    if label:
        p = label_pos or ((a[0]+b[0])/2, (a[1]+b[1])/2 + .23)
        txt(*p, label, size=14, color=color)

txt(8, 9.48, 'Halfspace solutions separate every finite Euler extension', 24)
txt(8, 9.04, r'$E\subset B=\mathscr{E}^{\infty}_p\subset C=\mathscr{E}^{\mathbb{R}}_p$'
    '    |    ' r'$S=\underset{D}{\mathrm{colim}}\,\mathcal{O}(D\cap\{\mathrm{Re}\,t<0\})/\mathcal{O}(D)$',
    17, muted)
ax.plot([8, 8], [2.55, 8.55], color='#d7dfea', lw=1.2)
txt(4, 8.35, 'Finite resolution and actual contractions', 19, blue)
box(4, 7.63, 6.6, .78,
    r'$F_k=K_k\oplus K_{k-1},\quad\mathrm{rank}\,F_k=q\binom{d+1}{k}$', 20)
txt(4, 6.94, r'$d_F(a,b)=(d_Ka+f(b),-d_Kb)$', 18)
txt(4, 6.58, r'$f(Q)=Q(\theta I-A),\quad\theta=tD_t$' + '   [EE.11–EE.12]', 16, muted)
box(4, 5.85, 6.6, .82,
    r'$\mathrm{Hom}_E(F_\bullet,S)$' + '\n'
    r'Koszul complex of $\theta I-A,D_{x_1},\ldots,D_{x_d}$', 16)
arrow((4, 5.32), (4, 4.66), r'$H_x$ preserves both domains', (5.53, 4.99))
box(4, 4.17, 5.25, .76, r'$S_0^q\ \overset{\theta I-A}{\longrightarrow}\ S_0^q$', 23)
txt(4, 3.53, 'Surjective by a holomorphic primitive on the left half-disc', 15, muted)
txt(4, 3.09, r'$\mathrm{Ext}^{j>0}_E(N_A,S)=0,\quad\dim\mathrm{Hom}_E(N_A,S)=q$', 18, green)

txt(12, 8.35, 'Arbitrary finite extensions over the full ring', 19, blue)
txt(12, 7.75, r'$0\longrightarrow L\ \overset{i}{\longrightarrow}\ T\ \overset{\pi}{\longrightarrow}\ N\longrightarrow0$', 21)
txt(12, 7.24, r'$L,N\in\mathcal{F},\quad T\in\mathcal{F}$' + '   [EE.23]', 17, muted)
box(12, 6.37, 6.6, 1.02,
    r'$0\to\mathrm{Hom}_B(N,S)\to\mathrm{Hom}_B(T,S)$' + '\n'
    r'$\to\mathrm{Hom}_B(L,S)\to0$', 19, green)
txt(12, 5.52, r'$\mathrm{Ext}_B^1(N,S)=0$' + ': every functional on L extends to T', 16, green)
box(12, 4.57, 6.6, 1.12,
    'If all functionals kill v:\n'
    r'$g(\pi v)=0\ \ \forall g\quad\Rightarrow\quad\pi v=0,\ v=i(w)$' + '\n'
    r'$u(w)=0\ \ \forall u\quad\Rightarrow\quad w=0,\ v=0$', 17)
txt(12, 3.53, r'$\mathrm{ev}_T:T\hookrightarrow S^{r(T)}$', 24, green)
txt(12, 3.09, r'$r(T)=\sum_a q_a=\dim_{\mathbb{C}}\mathrm{Hom}_B(T,S)$', 18, muted)

ax.plot([.65, 15.35], [2.56, 2.56], color='#d7dfea', lw=1.2)
txt(8, 2.12, r'$T\longrightarrow C\otimes_BT\longrightarrow S^{r(T)}$', 27, green)
txt(8, 1.57, r'$v\mapsto1\otimes v,\qquad c\otimes v\mapsto(c\,f_j(v))_j$', 20)
txt(8, 1.08, 'The composite is the injective evaluation map.  '
    'No flatness of C over B is assumed.', 16, muted)
txt(8, .55, 'EE.1–EE.4: exact maps and proof locators.  '
    'Membership of arbitrary holonomic germs remains a separate theorem.', 14, muted)

fig.savefig(args.output_dir / 'euler-extension-separation.png', dpi=150)
fig.savefig(args.output_dir / 'euler-extension-separation.svg', metadata={'Date': None})
plt.close(fig)
data = {
    'kind': 'exact proof diagram; no numerical samples',
    'rings': ['E', 'B=E-infinity', 'C=E-real'],
    'target': 'S=colim O(left half-polydisc)/O(full polydisc)',
    'resolution': {'F_k': 'K_k direct-sum K_(k-1)',
                   'd_F(a,b)': '(d_K a+f b,-d_K b)',
                   'f(Q)': 'Q(theta I-A)', 'rank_F_k': 'q*binomial(d+1,k)',
                   'proof': ['EE.5', 'EE.6', 'EE.7', 'EE.8', 'EE.9', 'EE.10', 'EE.11', 'EE.12']},
    'solution_contraction': {'operators': ['theta I-A', 'D_x1', '...', 'D_xd'],
                            'homotopy_on_alpha_plus_e0_beta': 'H_x alpha-e0 wedge H_x beta',
                            'last_complex': 'S_0^q --theta I-A--> S_0^q',
                            'last_arrow': 'surjective by EE.17',
                            'positive_ext': 'zero', 'hom_dimension': 'q'},
    'extension': {'sequence': '0 -> L -> T -> N -> 0',
                  'membership': 'finite filtration by arbitrary T_A=B tensor_E N_A',
                  'functional_sequence': '0 -> Hom_B(N,S) -> Hom_B(T,S) -> Hom_B(L,S) -> 0',
                  'restriction_surjective_reason': 'Ext_B^1(N,S)=0; EE.24',
                  'separation_steps': ['all g(pi v)=0 -> pi v=0 -> v=i(w)',
                                       'all u(w)=0 -> w=0 -> v=0']},
    'comparison': {'arrows': ['T -> C tensor_B T', 'C tensor_B T -> S^r(T)'],
                   'formulas': ['v -> 1 tensor v', 'c tensor v -> (c f_j(v))_j'],
                   'composite': 'injective evaluation; EE.25--EE.27',
                   'C_flatness_assumed': False},
    'boundary': 'No arbitrary holonomic membership or contact theorem is asserted.'}
(args.output_dir / 'euler-extension-separation-exact-data.json').write_text(
    json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'outputs': [p.name for p in args.output_dir.iterdir() if p.is_file()]}, indent=2))

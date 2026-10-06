"""Exact conormal model and dyadic endpoint; no numerical theorem inference."""
from pathlib import Path
import datetime, hashlib, json, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'courses/AN-04/public/src').is_dir())
DEST = ROOT / 'courses/AN-04/revisions/20261004-open-oscillatory-distributions/figures'
DEST.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'AN04-U003-conormal-endpoint-v1',
                     'axes.spines.top': False, 'axes.spines.right': False})
blue, orange, ink, muted = '#156288', '#ad4f19', '#172c39', '#526875'
fig, axes = plt.subplots(2, 2, figsize=(13, 8.2), dpi=140)
fig.patch.set_facecolor('white')
fig.subplots_adjust(left=.075, right=.96, bottom=.15, top=.79, hspace=.76, wspace=.30)
fig.text(.075, .957, 'A conormal line and an exact regularity endpoint', fontsize=21,
         weight='bold', color=ink)
fig.text(.075, .905, 'X = ℝ²,  Y = {x₁ = 0},  φ(x, θ) = x₁θ,  u = δ(x₁)', fontsize=15, color=ink)
fig.text(.075, .861, 'N*Y ∖ 0 = {(0, x₂; θ, 0) : x₂ ∈ ℝ, θ ≠ 0}       m = k/2 − n/4 = 0  (k = 1, n = 2)',
         fontsize=13, color=ink)

a = axes[0, 0]
a.set_title('A. Base plane: the support Y', loc='left', weight='bold', pad=13, fontsize=13)
a.set_xlim(-2.2, 2.2); a.set_ylim(-2.2, 2.2)
a.axhline(0, color='#b0bcc4', linewidth=1); a.axvline(0, color=blue, linewidth=4)
a.scatter([0], [0], color=ink, s=40, zorder=5)
a.text(.14, .19, 'x₀ = (0, 0)', color=ink, fontsize=11)
a.text(.14, 1.45, 'Y', color=blue, fontsize=14, weight='bold')
a.set_xlabel('base coordinate x₁'); a.set_ylabel('base coordinate x₂')
a.set_xticks([-2, -1, 0, 1, 2]); a.set_yticks([-2, -1, 0, 1, 2])
a.text(0, -.34, 'Only a bounded coordinate window is drawn; Y continues.',
       transform=a.transAxes, color=muted, fontsize=10)

a = axes[0, 1]
a.set_title('B. Fixed-base fiber projected to (ξ₁, ξ₂)', loc='left', weight='bold', pad=13, fontsize=13)
a.set_xlim(-3.2, 3.2); a.set_ylim(-1.55, 1.55)
a.axvline(0, color='#b0bcc4', linewidth=1)
a.plot([-3.2, 3.2], [0, 0], color=blue, linewidth=4)
a.scatter([0], [0], facecolors='white', edgecolors=blue, linewidths=2, s=90, zorder=5)
a.text(.09, .73, 'ξ₂ = 0,  ξ₁ = θ ≠ 0', transform=a.transAxes, color=blue, fontsize=13)
a.annotate('zero covector excluded', xy=(0, 0), xytext=(.35, -.95), fontsize=10,
           color=muted, arrowprops={'arrowstyle': '-', 'color': muted})
a.set_xlabel('covector coordinate ξ₁'); a.set_ylabel('covector coordinate ξ₂')
a.set_xticks([-3, -2, -1, 0, 1, 2, 3]); a.set_yticks([-1, 0, 1])
a.text(0, -.34, 'This is one fiber over x₀; both punctured rays continue.',
       transform=a.transAxes, color=muted, fontsize=10)

j = np.arange(1, 9)
a = axes[1, 0]
a.set_title('C. Normal model δ₀ in ℝ: the endpoint supremum', loc='left',
            weight='bold', pad=13, fontsize=13)
a.plot(j, np.ones_like(j), color=blue, marker='o', linewidth=2)
a.set_xlim(.65, 8.35); a.set_ylim(0, 1.6)
a.set_xticks(j); a.set_yticks([0, 1]); a.set_xlabel('dyadic index j ≥ 1')
a.set_ylabel('2⁻ʲᐟ² ‖Πⱼδ₀‖₂ / C', fontsize=13)
a.text(.08, .81, 'Each exact normalized value is 1.', transform=a.transAxes,
       fontsize=11, color=blue)
a.grid(axis='y', alpha=.18)

a = axes[1, 1]
a.set_title('D. Sobolev square sum: exact partial sums', loc='left',
            weight='bold', pad=13, fontsize=13)
a.plot(j, j, color=orange, marker='o', linewidth=2)
a.set_xlim(.65, 8.35); a.set_ylim(0, 9)
a.set_xticks(j); a.set_yticks([0, 2, 4, 6, 8]); a.set_xlabel('last dyadic index J')
a.set_ylabel('Σⱼ₌₁ᴶ (2⁻ʲᐟ² ‖Πⱼδ₀‖₂ / C)²', fontsize=12)
a.text(.09, .81, 'Partial sum = J; it diverges as J → ∞.', transform=a.transAxes,
       fontsize=11, color=orange)
a.grid(axis='y', alpha=.18)

fig.text(.075, .066, 'C = (2π)⁻¹ᐟ² ‖p‖₂ > 0, with p the smooth dyadic multiplier of (6.2).',
         fontsize=12, color=ink)
fig.text(.075, .030, 'Panels C–D use the one-dimensional normal delta, not a global L² norm of δ(x₁) on ℝ².',
         fontsize=11, color=muted)

png, svg = DEST / 'conormal-fiber-and-endpoint.png', DEST / 'conormal-fiber-and-endpoint.svg'
fig.savefig(png, dpi=140, metadata={'Software': 'Matplotlib; independently authored AN04-U003 teaching figure'})
fig.savefig(svg, metadata={'Date': None, 'Creator': 'Matplotlib; independently authored AN04-U003 teaching figure',
                          'Description': 'Fixed-base covector projection and exact normal delta dyadic endpoint.'})
font = Path(fm.findfont('DejaVu Sans'))
notice = ROOT / 'courses/AN-04/public/src/figures/notices/LICENSE_DEJAVU.txt'
(DEST / 'notices').mkdir(exist_ok=True)
shutil.copyfile(notice, DEST / 'notices/LICENSE_DEJAVU.txt')
shutil.copyfile(Path(__file__), DEST / 'conormal-fiber-and-endpoint.py')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
labels = [t.get_text() for t in fig.findobj(matplotlib.text.Text) if t.get_text()]
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
font_files = sorted({str(Path(fm.findfont(t.get_fontproperties())))
                     for t in fig.findobj(matplotlib.text.Text) if t.get_text()})
text_boxes = []
for t in fig.findobj(matplotlib.text.Text):
    if not t.get_text(): continue
    b = t.get_window_extent(renderer)
    text_boxes.append({'text':t.get_text(), 'x':b.x0, 'y':b.y0, 'width':b.width, 'height':b.height})
canvas = {'width':fig.bbox.width, 'height':fig.bbox.height}
assert all(b['x']>=0 and b['y']>=0 and b['x']+b['width']<=canvas['width'] and b['y']+b['height']<=canvas['height'] for b in text_boxes), 'Label extends outside figure'
record = {'schema': 'an04-u003-conormal-endpoint-figure/v1',
          'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'matplotlib_version': matplotlib.__version__,
          'source_sha256': sha(Path(__file__)), 'svg_sha256': sha(svg), 'png_sha256': sha(png),
          'labels': labels, 'labels_sha256': hashlib.sha256(json.dumps(labels, ensure_ascii=False).encode()).hexdigest(),
          'canvas':canvas, 'label_boxes':text_boxes, 'all_labels_inside_canvas':True,
          'font': {'family': 'DejaVu Sans', 'actual_font_path': str(font).replace('\\', '/'),
                   'actual_font_sha256': sha(font), 'full_notice_sha256': sha(notice),
                   'actually_used_font_files':[{'path':p.replace('\\','/'),'sha256':sha(p)} for p in font_files],
                   'svg_glyph_policy': 'DejaVu outlines embedded as SVG paths; no remote fonts.'},
          'mathematical_scope': {'base': 'R^2', 'submanifold': 'x1=0', 'phase': 'x1 theta',
             'nonzero_conormal': '(0,x2;theta,0), theta!=0', 'scalar_order': '1/2-2/4=0',
             'fiber_panel': 'Projection to covector coordinates of the fiber over x0=(0,0).',
             'dyadic_model': 'delta_0 on R, k=1, s=-1/2',
             'normalizing_constant': '(2pi)^(-1/2)||p||_2>0',
             'plotted_exact_sequence': [1]*8, 'plotted_exact_square_partial_sums': list(range(1,9)),
             'finite_plot_meaning': 'Exact initial values of proved sequences; the proof establishes all j and divergence.'},
          'proof_locators': ['AN04-U002 §5, Theorem 5.1; §8 conormal model',
                             'AN04-U003 §6, (6.1)–(6.4); Exercises 7.1 and 7.2'],
          'actual_visual_inspection_pending': True}
(ROOT / 'work/oscillatory-native-reader/figure.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print(json.dumps({k:record[k] for k in ['svg_sha256','png_sha256','labels_sha256']}))

"""Original CC0 1.0 diagram of TO.1-TO.26; no numerical proof replacement."""
from pathlib import Path
import os
HERE = Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR'] = str(HERE / 'runtime-cache')
import hashlib
import html
import json
import platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
import PIL

OUTPUT = HERE.parent.parent/'figures'
OUTPUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = HERE/'fonts'
families = {'DejaVu Sans', 'DejaVu Sans Display', 'DejaVu Sans Mono',
            'STIXGeneral', 'STIXNonUnicode', 'STIXSizeOneSym', 'STIXSizeTwoSym',
            'STIXSizeThreeSym', 'STIXSizeFourSym', 'STIXSizeFiveSym'}
font_manager.fontManager.ttflist[:] = [f for f in font_manager.fontManager.ttflist
                                     if f.name not in families]
for p in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(p))
actual_fonts = set()
original_get_font = font_manager._get_font
def checked_get_font(paths, *args, **kwargs):
    for item in ([paths] if isinstance(paths, (str, Path)) else paths):
        p = Path(item).resolve()
        assert p.parent == FONT_DIR.resolve(), ('unbundled actual font', str(p))
        actual_fonts.add(p.name)
    return original_get_font(paths, *args, **kwargs)
font_manager._get_font = checked_get_font
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'mathtext.fontset': 'stix', 'svg.fonttype': 'path',
                     'svg.hashsalt': 'translation-oscillator-20261005'})
fig = plt.figure(figsize=(20, 13), facecolor='#f7f9fc')
grid = fig.add_gridspec(2, 3, left=.045, right=.98, top=.81, bottom=.16,
                       hspace=.45, wspace=.28)
blue, orange, green, gray = '#286fa3', '#b56332', '#24745c', '#52647a'

a = fig.add_subplot(grid[0, 0]); a.set_facecolor('white')
x = np.linspace(-2.7, 2.7, 151)
xx, yy = np.meshgrid(x, x)
rho = np.exp(-(xx*xx+yy*yy))/np.pi
a.imshow(rho, extent=[x[0], x[-1], x[0], x[-1]], origin='lower',
         cmap='Blues', vmin=0, vmax=1/np.pi, aspect='equal')
a.contour(xx, yy, xx*xx+yy*yy, levels=[1, 4], colors=[orange], linewidths=1.5)
a.plot([0], [0], 'o', color=green, ms=5)
a.set_title('1. The unique positive Gaussian line (d=2)',
            loc='left', fontsize=14, fontweight='bold', pad=12)
a.set_xlabel(r'$x_1$'); a.set_ylabel(r'$x_2$')
a.text(.02, .02, r'$|\phi_0(x)|^2=\pi^{-1}e^{-|x|^2}$'+'\n'
       'Empty wedge: even; all annihilators vanish.', transform=a.transAxes,
       fontsize=11, color=gray,
       bbox={'facecolor':'white', 'alpha':.94, 'edgecolor':'none'})

b = fig.add_subplot(grid[0, 1]); b.set_facecolor('white')
ks = np.arange(6)
even = np.array([1]+[2*k for k in ks[1:]])
odd = np.array([0]+[2*k for k in ks[1:]])
b.bar(ks-.17, even, width=.32, color=blue, label='Even dimension')
b.bar(ks+.17, odd, width=.32, color=orange, label='Odd dimension')
b.set_xticks(ks); b.set_xlabel(r'Exact energy level $D^2=2k$')
b.set_ylabel('Dimension (d=2)'); b.set_ylim(0, 13.6)
b.set_title('2. Entire-space pairing; a finite display',
            loc='left', fontsize=14, fontweight='bold', pad=12)
b.legend(fontsize=10, loc='upper left'); b.grid(axis='y', alpha=.16)
b.text(.97,.96, r'$k>0:\ \dim H_k=4k$'+'\n'
       r'$\lambda=\pm\sqrt{2k}$'+'\n'
       r'$\operatorname{Index}D^+=1$', transform=b.transAxes,
       ha='right', va='top', fontsize=12, color=green)
b.text(.03,.53,'All k occur.\nFinite energy windows\nare finite-dimensional.',
       transform=b.transAxes, fontsize=10, color=gray)
b.spines[['top','right']].set_visible(False)

c = fig.add_subplot(grid[0, 2]); c.set_facecolor('white')
for n in range(-1, 4): c.axvline(n, color='#c8d1dc', lw=.8)
for n in range(-1, 3): c.axhline(n, color='#c8d1dc', lw=.8)
from matplotlib.patches import Rectangle
c.add_patch(Rectangle((0,0),1,1,facecolor=blue,alpha=.18,edgecolor=blue,lw=2))
c.add_patch(Rectangle((2,1),1,1,facecolor=orange,alpha=.18,edgecolor=orange,lw=2))
c.annotate('',xy=(2.5,1.5),xytext=(.5,.5),
           arrowprops={'arrowstyle':'->','color':green,'lw':2.5})
c.text(.5,.18,r'$C$',ha='center',fontsize=17,color=blue)
c.text(2.5,1.15,r'$m+C$',ha='center',fontsize=16,color=orange)
c.text(1.25,.95,r'$m=(2,1)$',fontsize=11,color=green)
c.set_xlim(-.25,3.35); c.set_ylim(-.25,2.5); c.set_aspect('equal')
c.set_title('3. A literal regular amplification',
            loc='left', fontsize=14, fontweight='bold', pad=12)
c.set_xlabel(r'$x_1=n_1+y_1$'); c.set_ylabel(r'$x_2=n_2+y_2$')
c.text(.03,.92,r'$(J\psi)_n(y)=\psi(n+y)$',transform=c.transAxes,fontsize=12,
       bbox={'facecolor':'white','alpha':.95,'edgecolor':'none'})
c.text(.01,-.27,r'$JT_mJ^{-1}=\lambda_m\otimes1$'+'\n'
       r'$\|\sum a_mT_m\|=\|\sum a_m\lambda_m\|_r$',
       transform=c.transAxes, fontsize=12, color=green)

d = fig.add_subplot(grid[1, 0]); d.set_facecolor('white')
z=np.linspace(-3,4,351)
d.plot(z,np.pi**(-.25)*np.exp(-z*z/2),color=blue,lw=2.3,label=r'$\phi_0(x)$')
d.plot(z,np.pi**(-.25)*np.exp(-(z-1)**2/2),color=orange,lw=2.3,
       label=r'$T_1\phi_0(x)=\phi_0(x-1)$')
d.annotate('',xy=(1,.84),xytext=(0,.84),
           arrowprops={'arrowstyle':'->','color':green,'lw':2})
d.set_xlim(-3,4);d.set_ylim(0,1.04);d.set_xlabel('One coordinate; translation by +1')
d.set_ylabel('Gaussian amplitude');d.legend(fontsize=10,loc='upper left')
d.set_title('4. A bounded return difference',loc='left',fontsize=14,
            fontweight='bold',pad=12)
d.text(.98,.97,r'$[D,T_m]=c_+(m)T_m$'+'\n'+r'$\|[D,T_m]\|=|m|$',
       transform=d.transAxes,fontsize=12,color=green,ha='right',va='top')
d.text(.02,-.23,'The Gaussian is not translation invariant.\n'
       'The phase return defect is compact.',transform=d.transAxes,
       fontsize=10,color=gray)
d.grid(alpha=.16);d.spines[['top','right']].set_visible(False)

e = fig.add_subplot(grid[1, 1]); e.set_facecolor('white')
r=np.linspace(-2,3,251);t=np.linspace(0,1,121)
rr,tt=np.meshgrid(r,t)
e.imshow(np.pi**(-.5)*np.exp(-(rr-tt)**2),extent=[-2,3,0,1],origin='lower',
         cmap='Blues',aspect='auto',vmin=0,vmax=np.pi**(-.5))
e.plot([0,1],[0,1],color=orange,lw=2,label=r'Centre $r=t$')
e.legend(loc='upper left',fontsize=10)
e.annotate('',xy=(1.5,.25),xytext=(1.5,.75),
           arrowprops={'arrowstyle':'->','color':green,'lw':2.4})
e.scatter([1.5,1.5],[.25,.75],s=28,color=green)
e.text(1.65,.27,r'$t=1/4$',fontsize=11,color=green)
e.text(1.65,.73,r"$t'=3/4$",fontsize=11,color=green)
e.text(-1.85,.68,r'$\partial_{r}$',fontsize=14,color=blue)
e.annotate('',xy=(-.8,.61),xytext=(-1.8,.61),
           arrowprops={'arrowstyle':'->','color':blue,'lw':1.8})
e.set_xlim(-2,3);e.set_ylim(0,1)
e.set_xlabel(r'Actual source coordinate $r$ (one coordinate shown)')
e.set_ylabel(r'Range lift $t$ over the torus')
e.set_title('5. Actual graph: fixed source, varying range',loc='left',
            fontsize=14,fontweight='bold',pad=12)
e.text(.02,-.23,'Source r=3/2 stays fixed under convolution.\n'
       'Potential difference t\u2032-t=1/2; no t derivative.',
       transform=e.transAxes,fontsize=10,color=gray)

f = fig.add_subplot(grid[1, 2]); f.axis('off')
f.set_title('6. Closed domain and localized compactness',
            loc='left',fontsize=12,fontweight='bold',pad=12)
f.text(.01,.90,r'$D^2=-\Delta+|x|^2+2N_E-d$',fontsize=15,color=blue)
f.text(.01,.73,r'$Q=H^1\cap\{|x|\psi\in L^2\}$',fontsize=15,color=blue)
f.text(.01,.55,'Graph domain: r and normal derivatives,\n'
       'weighted (r-t)\u03c8 in L\u00b2; no range derivative.',
       fontsize=12,color=gray,linespacing=1.6)
f.text(.01,.30,r'$a(\mathcal{D}-z)^{-1}\in\mathcal{K}$',fontsize=17,color=green)
f.text(.01,.08,'Compact fibre resolvent + compact range kernel.\n'
       'The graph resolvent alone is not globally compact.',
       fontsize=11,color=gray,linespacing=1.6)

fig.suptitle('Translation oscillators: exact reduced norm and a smooth source graph',
             x=.045,y=.965,ha='left',fontsize=24,fontweight='bold',color='#263953')
fig.text(.045,.895,'Auxiliary: every d \u2265 1. Actual graph: (R\u1d48 \u00d7 R\u1d48 \u00d7 N)/Z\u1d48 for the germ-effective torus suspension.',
         fontsize=16,color=gray)
fig.text(.045,.86,'Normal metric, full inverse spin-c module and coherent lift are supplied; compatible normal connections may be noninvariant.',
         fontsize=13,color=gray)
fig.text(.045,.075,'TO.1-TO.26. Exact Gaussian profiles and finite energy multiplicities are shown; the complete all-level proofs are in Section 11E.',
         fontsize=12,color=gray)
fig.text(.045,.045,'Only one coordinate is shown in panel 5. The operator is degenerate in range directions; the general holonomy-groupoid problem remains open.',
         fontsize=12,color=gray)
fig.canvas.draw(); renderer=fig.canvas.get_renderer(); outside=[]; count=0
hidden={id(text) for ax in fig.axes if not ax.axison for text in ax.get_xticklabels()+ax.get_yticklabels()}
for obj in fig.findobj(match=matplotlib.text.Text):
    if not obj.get_visible() or not obj.get_text() or id(obj) in hidden: continue
    count+=1; bounds=obj.get_window_extent(renderer)
    if bounds.x0 < -1 or bounds.y0 < -1 or bounds.x1 > fig.bbox.x1+1 or bounds.y1 > fig.bbox.y1+1:
        outside.append(obj.get_text())
assert not outside, outside
fig.savefig(OUTPUT/'kt-translation-oscillator-graph.png',dpi=125,facecolor=fig.get_facecolor(),
            metadata={'Software':'Original reproducible mathematical diagram'})
fig.savefig(OUTPUT/'kt-translation-oscillator-graph.svg',facecolor=fig.get_facecolor(),
            metadata={'Date':None,'Creator':'Original reproducible mathematical diagram'})
plt.close(fig)
notice=(HERE/'FONT-NOTICE.txt').read_text(encoding='utf8')
svg_path=OUTPUT/'kt-translation-oscillator-graph.svg';svg=svg_path.read_text(encoding='utf8')
svg=svg.replace('</metadata>','</metadata>\n<desc id="font-notices">'+html.escape(notice)+'</desc>',1)
svg_path.write_text(svg,encoding='utf8',newline='\n')
fonts=[{'path':'fonts/'+name,'sha256':hashlib.sha256((FONT_DIR/name).read_bytes()).hexdigest().upper()}
       for name in sorted(actual_fonts)]
report={'schema':'translation-oscillator-figure-inspection-data/v1','checked_texts':count,
        'outside_figure':outside,'actual_loaded_fonts':fonts,'bundled_fonts_unmodified':True,
        'exact_d2_energy_dimensions':[{'k':int(k),'even':int(even[k]),'odd':int(odd[k])} for k in ks],
        'source_range_sample':{'r':1.5,'t':.25,'t_prime':.75,'y':1.25,'y_prime':.75,
                               'potential_difference':.5,'coordinate_projection_only':True},
        'global_graph_resolvent_claimed_compact':False,'arbitrary_groupoid_target_closed':False,
        'font_notice_sha256':hashlib.sha256((HERE/'FONT-NOTICE.txt').read_bytes()).hexdigest().upper(),
        'runtime':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,
                   'numpy':np.__version__,'pillow':PIL.__version__},
        'original_expression_terms':'CC0-1.0'}
(HERE/'FIGURE-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figures':2,'checked_texts':count,'outside_figure':outside,
                  'actual_font_load_count':len(fonts),'runtime':report['runtime']}))

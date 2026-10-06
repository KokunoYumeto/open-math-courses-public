"""Proposition 6.8h / Figure 6.8e / QB.1–QB.15: original CC0 diagram expression.
Run with this directory and its exact bundled DejaVu/STIX fonts and complete notice.
"""
from pathlib import Path
import hashlib, html, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

SOURCE_DIR=Path(__file__).resolve().parent
HERE=SOURCE_DIR.parent.parent/'figures'
HERE.mkdir(parents=True,exist_ok=True)
FONT_DIR=SOURCE_DIR/'fonts'
families={'DejaVu Sans','DejaVu Sans Display','DejaVu Sans Mono','STIXGeneral',
          'STIXNonUnicode','STIXSizeOneSym','STIXSizeTwoSym','STIXSizeThreeSym',
          'STIXSizeFourSym','STIXSizeFiveSym'}
font_manager.fontManager.ttflist[:]=[f for f in font_manager.fontManager.ttflist if f.name not in families]
for p in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(p))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path',
                    'mathtext.fontset':'dejavusans','svg.hashsalt':'qb-boundary-20261005'})
fig=plt.figure(figsize=(18,11),facecolor='#f7f9fc')
grid=fig.add_gridspec(2,2,left=.065,right=.96,bottom=.16,top=.82,
                     hspace=.44,wspace=.27,height_ratios=[1,1])
a=fig.add_subplot(grid[0,0]);a.axis('off')
a.set_title('Exact completed quotient and Dirichlet dual',loc='left',fontsize=17,fontweight='bold',pad=16)
a.text(.02,.86,r'$J:H_0^1(I)\longrightarrow L\subset H^1(M)$',fontsize=19)
a.text(.02,.68,r'$K=\{g:F_g|_L=0\},\qquad L\ \mathrm{closed}$',fontsize=17)
a.text(.02,.47,r'$H^{-1}(M)/K\ \cong\ (H_0^1(I))^*_{\mathrm{anti}}$',fontsize=20,color='#1e6a55')
a.text(.02,.27,r'$\widetilde f(w)=f(J^{-1}P_Lw),\qquad\|\widetilde f\|=\|f\|$',fontsize=17)
a.text(.02,.05,'Zero extension is isometric. Projection attains the quotient norm.\n'
       'This does not equate the inherited supported norm or the regional dual.',
       fontsize=12,color='#51647d',linespacing=1.6)

b=fig.add_subplot(grid[0,1]);b.set_facecolor('white')
b.set_title('One fixed ordinary interval; each row is a separate operator',loc='left',fontsize=15,fontweight='bold',pad=16)
b.set_xlim(-.035,1.035);b.set_ylim(-.42,2.56)
b.set_xticks([0,.25,.5,.75,1],['0','1/4','1/2','3/4','1'])
b.set_yticks([2,1,0],[r'$\varepsilon=1/5$',r'$\varepsilon=2/25$',r'$\varepsilon=3/100$'])
b.set_xlabel(r'Physical $x$ on the same plaque $I=(0,1)$',labelpad=10)
t=np.linspace(.25,.75,501);bump=np.zeros_like(t)
mask=(t>.25)&(t<.75)
bump[mask]=np.exp(-1/((t[mask]-.25)*(.75-t[mask])))
profile=bump/bump.max()
for epsilon,y in [(.2,2),(.08,1),(.03,0)]:
    b.plot([0,1],[y,y],color='#b0bccd',lw=1.5)
    b.plot([epsilon,2*epsilon],[y,y],color='#236da6',lw=4)
    b.plot(epsilon+epsilon*t,y+.27*profile,color='#236da6',lw=2)
    b.scatter([0,1],[y,y],s=28,facecolor='white',edgecolor='#677c94',zorder=3)
    b.text(.47,y+.13,r'$\operatorname{supp}g_\varepsilon\subset(\varepsilon,2\varepsilon)$',
           fontsize=12,color='#30445c')
b.axvline(0,color='#af5432',lw=1.4,ls='--')
b.text(.43,-.35,'Physical widths are exact; profile heights are normalized schematics.',
       fontsize=10,color='#51647d',ha='center')
b.spines[['top','right']].set_visible(False)

c=fig.add_subplot(grid[1,0]);c.set_facecolor('white')
epsilon=np.geomspace(1e-4,.249,300)
upper=np.sqrt(2*epsilon)
c.semilogx(epsilon,upper,color='#ab5631',lw=2.6,
           label=r'Local quotient/Dirichlet-dual norm $\leq\sqrt{2\varepsilon}$')
c.semilogx(epsilon,np.full_like(epsilon,.5),color='#236da6',lw=2.6,
           label=r'Global $L^2\to H^{-1}(M)$ norm $\geq1/2$')
c.fill_between(epsilon,0,upper,color='#ab5631',alpha=.08)
c.set_xlim(.25,1e-4);c.set_ylim(0,.82)
c.set_xticks([.1,.01,.001,.0001],['0.1','0.01','0.001','0.0001']);c.minorticks_off()
c.set_xlabel(r'$\varepsilon$ decreases toward the boundary',labelpad=10)
c.set_ylabel('Proved operator norm bounds')
c.set_title('Local tests vanish; the global constant mode remains',loc='left',fontsize=15,fontweight='bold',pad=16)
c.grid(alpha=.17);c.legend(loc='upper right',fontsize=11,framealpha=.95)
c.text(.0006,.18,r'$A_\varepsilon h_\varepsilon=g_\varepsilon,\quad\|h_\varepsilon\|_2=1,\quad\int g_\varepsilon=1$',
       fontsize=13,ha='right')
c.spines[['top','right']].set_visible(False)

d=fig.add_subplot(grid[1,1]);d.set_facecolor('white')
ratio=1/(2*np.sqrt(2*epsilon))
d.semilogx(epsilon,ratio,color='#1e795b',lw=2.8)
d.set_xlim(.25,1e-4);d.set_ylim(0,38)
d.set_xticks([.1,.01,.001,.0001],['0.1','0.01','0.001','0.0001']);d.minorticks_off()
d.set_xlabel(r'$\varepsilon$ decreases toward zero',labelpad=10)
d.set_ylabel('Proved global / local norm ratio lower bound')
d.set_title('An unbounded ratio with one plaque per leaf',loc='left',fontsize=15,fontweight='bold',pad=16)
d.text(.03,28,r'$\mathrm{ratio}\geq 1/(2\sqrt{2\varepsilon})$',fontsize=18)
d.text(.04,17,'Actual smooth convolution squares:\n'
       r'$B_{\varepsilon,u}=C_{\varepsilon,u}^*C_{\varepsilon,u}$',
       fontsize=14,linespacing=1.8)
d.grid(alpha=.17);d.spines[['top','right']].set_visible(False)

fig.suptitle('Negative restriction duality and a positive boundary test',x=.065,y=.96,
             ha='left',fontsize=24,fontweight='bold',color='#263953')
fig.text(.065,.89,r'Fixed $M=\mathbb{R}/(4\mathbb{Z})$, fixed ordinary chart $I\times U$, physical $L^2$ input; $0<\varepsilon<1/4$.',
         fontsize=17,color='#51647d')
fig.text(.065,.083,'The curves are proved bounds, not exact norms or spectra. Each support is compact, but no common interior support buffer exists.',
         fontsize=13,color='#51647d')
fig.text(.065,.045,'Supported ambient output retains the global norm here. The unrestricted regional dual is excluded. The historical plaque norm remains open.',
         fontsize=13,color='#51647d')
fig.canvas.draw();renderer=fig.canvas.get_renderer();outside=[];checked=0
hidden={id(t) for axis in fig.axes if not axis.axison for t in axis.get_xticklabels()+axis.get_yticklabels()}
for t in fig.findobj(match=matplotlib.text.Text):
    if not t.get_visible() or not t.get_text() or id(t) in hidden: continue
    checked+=1;bounds=t.get_window_extent(renderer)
    if bounds.x0 < -1 or bounds.y0 < -1 or bounds.x1 > fig.bbox.x1+1 or bounds.y1 > fig.bbox.y1+1:
        outside.append(t.get_text())
assert not outside,outside
fig.savefig(HERE/'kt-plaque-negative-output-boundary.png',dpi=125,facecolor=fig.get_facecolor(),
            metadata={'Software':'Original reproducible mathematical diagram'})
fig.savefig(HERE/'kt-plaque-negative-output-boundary.svg',facecolor=fig.get_facecolor(),
            metadata={'Date':None,'Creator':'Original reproducible mathematical diagram'})
plt.close(fig)
notice=(SOURCE_DIR/'FONT-NOTICE.txt').read_text(encoding='utf-8')
p=HERE/'kt-plaque-negative-output-boundary.svg';svg=p.read_text(encoding='utf-8')
svg=svg.replace('</metadata>','</metadata>\n<desc id="font-notices">'+html.escape(notice)+'</desc>',1)
p.write_text(svg,encoding='utf-8',newline='\n')
report={'schema':'exact-negative-output-boundary-figure/v1','proof_locators':'Proposition 6.8h, (QB.1)–(QB.15), Figure 6.8e',
        'checked_texts':checked,'outside_figure':outside,
        'support_samples':[{'epsilon':e,'outer_interval':[e,2*e],
                           'actual_bump_support_inside':[1.25*e,1.75*e]}
                          for e in [.2,.08,.03]],
        'coordinate_profiles_not_scaled_output_amplitudes':True,
        'all_epsilon_proof_not_replaced_by_samples':True,
        'exact_bound_formulas':{'local_upper':'sqrt(2epsilon)','global_lower':'1/2',
                               'ratio_lower':'1/(2sqrt(2epsilon))'},
        'font_notice_sha256':hashlib.sha256((SOURCE_DIR/'FONT-NOTICE.txt').read_bytes()).hexdigest().upper(),
        'original_expression_terms':'CC0-1.0'}
(SOURCE_DIR/'figure-and-bounds.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':2,'checked_texts':checked,'outside_figure':outside}))

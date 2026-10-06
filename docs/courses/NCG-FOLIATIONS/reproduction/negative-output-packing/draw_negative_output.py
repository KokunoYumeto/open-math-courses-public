"""Original CC0 positive-kernel plaque-bound diagram; full DejaVu/STIX terms retained.
Run from this reproduction directory with its bundled exact fonts and notice.
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
font_names=set(['DejaVu Sans', 'DejaVu Sans Display', 'STIXGeneral', 'STIXNonUnicode', 'STIXSizeFiveSym', 'STIXSizeFourSym', 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym'])
font_manager.fontManager.ttflist[:]=[f for f in font_manager.fontManager.ttflist if f.name not in font_names]
for font_path in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(font_path))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'negative-output-packing-20261005','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(18,11),facecolor='#f6f8fb')
grid=fig.add_gridspec(1,2,left=.07,right=.97,bottom=.20,top=.79,width_ratios=[1.06,1],wspace=.28)
ax=fig.add_subplot(grid[0,0]);ax.set_facecolor('white')
ax.set_title('One leaf; disjoint physical plaques',loc='left',fontsize=17,fontweight='bold',pad=20)
ax.set_xlim(-.04,1.04);ax.set_ylim(-.4,4.75)
ax.set_xticks([0,.25,.5,.75,1],['0','1/4','1/2','3/4','1'])
ax.set_yticks(range(5),[f'j = {4-j}' for j in range(5)])
ax.set_xlabel(r'Local coordinate $t=(x-u_j)/\delta_j$; each row is enlarged',labelpad=12)
t=np.linspace(.25,.75,401);eta=np.zeros_like(t)
middle=(t>.25)&(t<.75);eta[middle]=np.exp(-1/((t[middle]-.25)*(.75-t[middle])))
shape=eta/eta.max()
for j in range(5):
    y=4-j
    ax.plot([0,1],[y,y],color='#9aabc0',lw=2)
    ax.plot(t,y+.32*shape,color='#2269a4',lw=2)
    ax.fill_between(t,y,y+.32*shape,color='#2269a4',alpha=.16)
    ax.scatter([0,1],[y,y],facecolors='white',edgecolors='#63778e',s=35,zorder=4)
    ax.text(.99,y+.39,rf'$u_{j}=e^{{-{2+4*j}}},\quad\delta_{j}=u_{j}/16$',ha='right',fontsize=12)
ax.text(.02,4.5,'Blue: normalized η / max(η); each interval is enlarged',fontsize=11,color='#52647c')
ax.text(.02,-.35,r'$dx=\delta_j\,dt,\quad\int g_j\,dx=1,\quad\|h_j\|_2=1$',fontsize=14,color='#253751')
ax.spines[['top','right']].set_visible(False)

bx=fig.add_subplot(grid[0,1]);bx.set_facecolor('white')
bx.set_title('Proved bounds for every integer N',loc='left',fontsize=17,fontweight='bold',pad=20)
n=np.arange(1,37);lower=np.sqrt(n)/2;upper=np.full_like(n,np.sqrt(3)/2,dtype=float)
bx.plot(n,lower,color='#2269a4',lw=2.8,label=r'Global $L^2\to H^{-1}(M)$ norm $\geq\sqrt{N}/2$')
bx.scatter(n[::3],lower[::3],color='#2269a4',s=24)
bx.plot(n,upper,color='#a44d29',lw=2.4,label=r'Every local norm $\leq\sqrt{3}/2$')
bx.fill_between(n,0,upper,color='#a44d29',alpha=.08)
bx.set_xlim(1,36);bx.set_ylim(0,3.65);bx.set_xlabel('Number of selected plaques N',labelpad=12);bx.set_ylabel('Operator norm: exact upper and lower bounds')
bx.grid(alpha=.15);bx.legend(loc='upper left',fontsize=11,framealpha=.95)
bx.text(17,1.5,r'$f_N=N^{-1/2}\sum_{j<N}h_j,\quad\|f_N\|_2=1$',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
bx.text(17,1.14,r'$A_Nf_N=N^{-1/2}\sum_{j<N}g_j$',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
bx.text(4,.4,r'Constant Fourier component: $\int A_Nf_N=\sqrt{N}$',fontsize=12)
bx.spines[['top','right']].set_visible(False)
fig.suptitle('Positive smoothing kernels: local negative output misses shared mass',x=.07,y=.96,ha='left',fontsize=23,fontweight='bold',color='#253751')
fig.text(.07,.90,r'Fixed chart $\mathcal{F}(t,u)=(u(1+t/16),-\log u\ \mathrm{mod}\ 4)$ on a flat torus; fixed physical $L^2$ input.',fontsize=16,color='#52647c')
fig.text(.07,.85,r'$g_u=\delta^{-1}\eta(t),\quad h_u=\delta^{-1/2}\eta(t)/\|\eta\|_2,\quad A_N=Q_N^*Q_N\geq0$',fontsize=16,color='#253751')
fig.text(.07,.095,'Local output: supported ambient H⁻¹, restriction quotient H⁻¹, or the dual of H₀¹. Each is bounded by the ambient norm.',fontsize=13,color='#52647c')
fig.text(.07,.062,'Each row is a coordinate schematic; physical lengths shrink. The plotted integer bounds are proved for all N in NP.1–NP.12.',fontsize=12,color='#52647c')
fig.text(.07,.030,'The unrestricted regional H¹ dual is excluded. The historically unspecified plaque norm remains open. Original CC0 diagram expression.',fontsize=12,color='#52647c')
fig.savefig(HERE/'kt-plaque-negative-output.png',dpi=125,facecolor=fig.get_facecolor(),metadata={'Software':'Original reproducible mathematical diagram'})
fig.savefig(HERE/'kt-plaque-negative-output.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Original reproducible mathematical diagram'})
plt.close(fig)
notice=(SOURCE_DIR/'FONT-NOTICE.txt').read_text(encoding='utf-8')
svg=HERE/'kt-plaque-negative-output.svg';text=svg.read_text(encoding='utf-8')
text=text.replace('</metadata>','</metadata>\n<desc id="font-notices">'+html.escape(notice)+'</desc>',1)
svg.write_text(text,encoding='utf-8',newline='\n')
rows=[]
for p in [HERE/'kt-plaque-negative-output.png',HERE/'kt-plaque-negative-output.svg',SOURCE_DIR/'draw_negative_output.py',SOURCE_DIR/'FONT-NOTICE.txt']:
    rows.append({'path':p.relative_to(SOURCE_DIR.parent.parent).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper()})
(SOURCE_DIR/'figure-and-bounds.json').write_text(json.dumps({'schema':'negative-output-packing-figure/v1','assets':rows,'proof_locators':'NP.1–NP.12','geometry':'Coordinate schematic of five exact physical plaques; common normalized bump shape, no physical metric change','plotted_bounds':'Exact proven upper sqrt3/2 and lower sqrtN/2 at integer N; samples illustrate all-N proof','fonts':'DejaVu families plus actual STIXSizeOneSym-Regular and STIXNonUnicode-Italic SVG glyphs; full installed DejaVu and STIX notices retained','original_expression_terms':'CC0-1.0'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':2,'all_N_proof_not_replaced_by_sampling':True}))

"""Original graph Dirac constraint diagram and exact finite checks; CC0-1.0.
Bundled DejaVu/STIX fonts and external libraries retain their separate terms.
Run this complete source from the reproduction directory; no private files needed.
"""
from pathlib import Path
import json, hashlib, html
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

SOURCE_DIR = Path(__file__).resolve().parent
HERE = SOURCE_DIR.parent.parent / 'figures'
HERE.mkdir(parents=True, exist_ok=True)
FONT_DIR = SOURCE_DIR / 'fonts'
# Replace family entries with exact bundled typefaces. The SVG is outlined.
font_names = {'DejaVu Sans', 'DejaVu Sans Display', 'STIXGeneral'}
font_manager.fontManager.ttflist[:] = [f for f in font_manager.fontManager.ttflist if f.name not in font_names]
for font_path in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(font_path))
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'dejavusans'})
font_notices = '\n\n'.join((FONT_DIR/n).read_text(encoding='utf-8') for n in ['LICENSE_DEJAVU.txt','LICENSE_STIX.txt'])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'graph-dirac-interface-55-20261005'})
fig = plt.figure(figsize=(16,9), facecolor='#f7f9fc')
gs = fig.add_gridspec(2,2,width_ratios=[1.45,1],height_ratios=[1.12,1],left=.055,right=.96,bottom=.085,top=.88,wspace=.23,hspace=.3)
ax = fig.add_subplot(gs[0,0]); ax.set_facecolor('white')
ax.set_title('Actual holonomy graph of one circle leaf',loc='left',fontweight='bold',fontsize=16,pad=13)
ax.set_xlim(0,2*np.pi);ax.set_ylim(0,2*np.pi)
ax.set_xticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$'])
ax.set_yticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$'])
ax.set_xlabel(r'Range endpoint $x$ (periodic)');ax.set_ylabel(r'Source endpoint $y$ (periodic)')
for y in [1.1,3.1,5.1]:
    ax.plot([.25,6.03],[y,y],color='#a1b9d8',lw=2)
    ax.annotate('',xy=(5.75,y),xytext=(.55,y),arrowprops={'arrowstyle':'->','color':'#195c99','lw':2})
ax.text(.45,5.5,r'$\pi(k)\psi(x,y)=\int k(x,z)\psi(z,y)\,dz/(2\pi)$',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','alpha':.94})
ax.text(.45,.25,'Convolution integrates the range variable.\nEvery source mode remains in the full graph space.',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','alpha':.94})

sp=fig.add_subplot(gs[1,0]);sp.axis('off');sp.set_xlim(-3.7,3.7);sp.set_ylim(-.85,1.95)
sp.set_title('Point-transversal corner: exact flat circle blocks',loc='left',fontweight='bold',fontsize=16,pad=10)
for n in range(-3,4):
    color='#af442b' if n==0 else '#195c99'
    sp.scatter([n,n],[1.1,.1],s=105,color=color,zorder=3)
    if n:
        sp.annotate('',xy=(n,.23),xytext=(n,.95),arrowprops={'arrowstyle':'->','lw':1.7,'color':color})
        sp.text(n+.11,.58,f'i({n})',fontsize=11)
    else:
        sp.plot([0,0],[.25,.95],ls=':',color=color,lw=1.5)
        sp.text(.15,.59,'0',color=color,fontweight='bold')
    sp.text(n,-.3,str(n),ha='center',fontsize=11)
sp.text(-3.65,1.1,r'$H^+$',fontsize=13,va='center');sp.text(-3.65,.1,r'$H^-$',fontsize=13,va='center')
sp.text(0,-.63,r'$D_p=\sigma_2(-i\partial_y),\quad n\in\mathbb{Z}:\quad\ker D_p^+=\mathbb{C},\;\operatorname{coker}D_p^+=\mathbb{C}$',ha='center',fontsize=12)
sp.text(0,1.62,'All nonzero modes pair; constant kernel − constant cokernel = 1 − 1 = 0.',ha='center',fontsize=12,color='#953b26')

ob=fig.add_subplot(gs[:,1]);ob.axis('off');ob.set_xlim(0,1);ob.set_ylim(0,1)
ob.set_title('A separate determinant-line obstruction',loc='left',fontweight='bold',fontsize=16,pad=13)
for y,label in [(.76,'Projective fibre at t = 0'),(.50,'Projective fibre at t = 1')]:
    ob.add_patch(FancyBboxPatch((.07,y-.065),.82,.14,boxstyle='round,pad=.02',facecolor='white',edgecolor='#9fb5cf',lw=1.5))
    ob.text(.48,y+.025,label,ha='center',fontsize=12)
    ob.text(.48,y-.025,r'$\mathbb{CP}^2,\quad c_1(\ell|_{\mathrm{fibre}})=kh$',ha='center',fontsize=14)
ob.annotate('',xy=(.48,.595),xytext=(.48,.675),arrowprops={'arrowstyle':'->','lw':2,'color':'#195c99'})
ob.text(.52,.635,'interval transport',fontsize=11,va='center')
ob.annotate('',xy=(.95,.78),xytext=(.95,.49),arrowprops={'arrowstyle':'->','lw':2,'color':'#af442b','connectionstyle':'arc3,rad=.3'})
ob.text(.05,.89,'Conjugation mapping torus (real dimension 5)\nNormal bundle: rank 0, with its trivial spin-c structure.',fontsize=12)
ob.text(.03,.37,r'Conjugation $c(z)=\overline{z}$: $c^*h=-h$',fontsize=14)
ob.text(.03,.29,r'Any global line: $kh=-kh\;\Longrightarrow\; k=0$',fontsize=14,color='#195c99')
ob.text(.03,.20,'Tangent spin-c line would require k odd.',fontsize=14,color='#953b26')
ob.text(.03,.105,'No full tangent spin-c lift on L or on L × L.\nLarger Clifford modules remain possible.',fontsize=12)

fig.suptitle('Graph Dirac locality, scalar normalization, and the missing line',x=.055,y=.982,ha='left',va='top',fontsize=21,fontweight='bold',color='#253751')
fig.text(.055,.94,'Proved interfaces GD.1–GD.12. The SU(2)/F2 graph-column cycle of Section 11A remains intact.',fontsize=13,color='#52647c')
fig.text(.055,.025,'Section 11C.2–11C.6 and 11C.8. Exact schematic; no numerical approximation. Source question: Connes, Survey.',fontsize=11,color='#52647c')
fig.savefig(HERE/'kt-graph-dirac-constraints.png',dpi=125,facecolor=fig.get_facecolor(),metadata={'Software':'Original mathematical schematic; reproducible local Python source'})
fig.savefig(HERE/'kt-graph-dirac-constraints.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Original reproducible local mathematical schematic'})
plt.close(fig)
# Retain the full licences of the actual outlined typefaces with the SVG.
svg_path = HERE / 'kt-graph-dirac-constraints.svg'
svg_text = svg_path.read_text(encoding='utf-8')
svg_text = svg_text.replace('</metadata>', '</metadata>\n <desc id="font-notices">'+html.escape(font_notices)+'</desc>', 1)
svg_path.write_text(svg_text, encoding='utf-8', newline='\n')

# Finite arithmetic verifies the displayed formula; it does not replace the
# all-mode Fourier proof, the convolution rigidity proof or the line argument.
s1=np.array([[0,1],[1,0]],dtype=complex);s2=np.array([[0,-1j],[1j,0]],dtype=complex);s3=np.diag([1,-1])
blocks=[]
for m in range(-8,9):
    for n in range(-8,9):
        d=m*s1+n*s2
        assert np.array_equal(d@d,(m*m+n*n)*np.eye(2))
        assert np.array_equal(s3@d+d@s3,np.zeros((2,2)))
        blocks.append({'m':m,'n':n,'square':m*m+n*n})
report={'schema':'graph-dirac-interface-finite-arithmetic/v1','checked_fourier_blocks':len(blocks),'exact_matrix_square':True,'exact_grading':True,'corner_constant_kernel_dimension':1,'corner_constant_cokernel_dimension':1,'corner_index':0,'proof_scope':'finite checks support illustration only; all integers and all candidate coefficients are handled analytically in Section 11C','assets':[]}
for name in ['kt-graph-dirac-constraints.png','kt-graph-dirac-constraints.svg','draw_graph_dirac.py']:
    p=(SOURCE_DIR/name if name=='draw_graph_dirac.py' else HERE/name);b=p.read_bytes();report['assets'].append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest().upper()})
(SOURCE_DIR/'arithmetic-and-figure.json').write_bytes((json.dumps(report,indent=2)+'\n').encode())
print(json.dumps(report,indent=2))

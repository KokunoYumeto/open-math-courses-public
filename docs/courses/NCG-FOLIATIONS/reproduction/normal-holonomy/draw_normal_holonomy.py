"""Exact affine/return figure. Original expression dedicated to CC0-1.0."""
from pathlib import Path
import os, math, argparse, tempfile
HERE = Path(__file__).resolve().parent
CACHE = tempfile.TemporaryDirectory(prefix='normal-holonomy-')
os.environ['MPLCONFIGDIR'] = CACHE.name
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=HERE.parents[1]/'figures')
OUT = parser.parse_args().output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle, FancyArrowPatch

REG = FontProperties(fname=str(HERE/'fonts/DejaVuSans.ttf'))
BOLD = FontProperties(fname=str(HERE/'fonts/DejaVuSans-Bold.ttf'))
plt.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'normal-holonomy-20261006'})
BLUE, RED, INK, GREEN = '#2364aa', '#b33b46', '#233244', '#287b61'
fig, ax = plt.subplots(1,3,figsize=(16,6.8),gridspec_kw={'width_ratios':[1,1.04,1.1]})
fig.patch.set_facecolor('white')
def text(a,x,y,s,size=11,bold=False,color=INK,ha='center'):
    return a.text(x,y,s,fontsize=size,fontproperties=BOLD if bold else REG,color=color,
                  ha=ha,va='center',transform=a.transAxes,linespacing=1.30,zorder=10)
def arrow(a,start,end,color=INK):
    a.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,
                              linewidth=2,color=color,transform=a.transAxes))
for a in ax:
    a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off')
a=ax[0]
text(a,.5,.96,'A. Nonabelian affine cover',13,True)
text(a,.5,.86,'a(x,y) = (x+1,y)\nb(x,y) = (−x,y+1)',11)
a.add_patch(Rectangle((.22,.34),.56,.38,facecolor='#eef4fa',edgecolor=INK,linewidth=1.8,transform=a.transAxes))
for x in [.22,.78]: arrow(a,(x,.40),(x,.65),BLUE)
arrow(a,(.28,.34),(.68,.34),GREEN)
arrow(a,(.70,.72),(.30,.72),GREEN)
text(a,.11,.53,'a',12,True,BLUE)
text(a,.90,.53,'a',12,True,BLUE)
text(a,.5,.53,'Q = [0,1)²',12,True)
text(a,.5,.28,'Horizontal identification: x ↦ 1−x',10,color=GREEN)
text(a,.5,.18,'b a b⁻¹ = a⁻¹\n⟨a,b²⟩ = Z², index 2',11)
text(a,.5,.06,'Proper free cover of the Klein bottle.\nThis group fails the finite-tree condition.',10)
a=ax[1]
text(a,.5,.96,'B. Actual source oscillator',13,True)
text(a,.5,.86,'y = r−t ∈ R²; no range t derivative\nPositive auxiliary kernel: dimension 1',10)
grid=[-2.7+5.4*k/100 for k in range(101)]
values=[[math.pi**(-.5)*math.exp(-(x*x+y*y)/2) for x in grid] for y in grid]
heat=a.inset_axes([.16,.34,.68,.41])
heat.imshow(values,extent=(-2.7,2.7,-2.7,2.7),origin='lower',cmap='Blues',interpolation='bilinear',aspect='equal')
heat.axis('off')
text(a,.5,.54,'π⁻¹ᐟ² exp(−|y|²/2)',12,True,color=INK)
text(a,.5,.30,'Full normal action on the flat T³:',10)
text(a,.5,.22,'a: (θ₁,θ₂,θ₃) ↦ (θ₁+√2,θ₂,θ₃)\nb: (θ₁,θ₂,θ₃) ↦ (−θ₁,θ₂+√3,−θ₃)',9.5)
text(a,.5,.10,'s_b² = −1; det χ_g = exp(2πi n/5)\nOriginal local transverse Bott pairing +1',10,True)
a=ax[2]
text(a,.5,.96,'C. Hyperbolic return boundary',13,True)
text(a,.5,.86,'f(x) = x + sin(2πx)/(4π) mod 1\np = 0; f′(p) = λ = 3/2',10)
ns=list(range(9));ders=[1.5**n for n in ns]
xx=[.17+.70*n/8 for n in ns]
yy=[.36+.34*math.log(v)/math.log(ders[-1]) for v in ders]
lo=[.36+.34*math.log(v/2)/math.log(ders[-1]) for v in ders]
a.plot(xx,yy,color=RED,linewidth=2,marker='o',markersize=4,transform=a.transAxes)
a.plot(xx,lo,color=BLUE,linewidth=1.7,linestyle='--',transform=a.transAxes)
a.plot([.14,.90],[.28,.28],color=INK,linewidth=.9,transform=a.transAxes)
a.plot([.14,.14],[.28,.71],color=INK,linewidth=.9,transform=a.transAxes)
for value in [.5,1,4,16]:
    pos=.36+.34*math.log(value)/math.log(ders[-1])
    a.plot([.13,.15],[pos,pos],color=INK,linewidth=.8,transform=a.transAxes)
    text(a,.10,pos,str(value).rstrip('0').rstrip('.') if value != .5 else '1/2',8)
for n in [0,4,8]:text(a,.17+.70*n/8,.255,str(n),9)
text(a,.94,.28,'n',10)
text(a,.49,.735,'λⁿ  (log vertical scale)',10,color=RED)
text(a,.59,.41,'λⁿ/2 = proved bound / c',9,color=BLUE)
text(a,.5,.18,'One fixed kernel; unit compact inputs.\n‖T ψ_n‖ ≥ c λⁿ/2 → ∞',10,True)
text(a,.5,.06,'No invariant positive normal metric.\nNot a counterexample under that premise.',10,color=RED)
fig.subplots_adjust(left=.025,right=.987,bottom=.08,top=.90,wspace=.15)
fig.text(.5,.982,'A genuine affine graph construction and a distinct return obstruction',ha='center',va='top',fontsize=16,fontproperties=BOLD,color=INK)
fig.text(.5,.018,'NH.1–NH.25. Exact square/edge gluing, Gaussian and return derivatives; torus coordinates are formulas. Original diagram CC0-1.0; separate font terms.',ha='center',va='bottom',fontsize=9,fontproperties=REG,color=INK)
notice=(HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
png=OUT/'affine-oscillator-and-return-holonomy.png';svg=OUT/'affine-oscillator-and-return-holonomy.svg'
fig.savefig(png,dpi=160,metadata={'Title':'Affine oscillator and return holonomy','Description':notice})
fig.savefig(svg,metadata={'Date':'2026-10-06','Title':'Affine oscillator and return holonomy','Description':notice,'Creator':'Original CC0 mathematical diagram'})
plt.close(fig)
print('Rendered affine-oscillator-and-return-holonomy.png and affine-oscillator-and-return-holonomy.svg')
CACHE.cleanup()

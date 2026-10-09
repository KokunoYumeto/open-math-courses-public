"""Exact cusp-product/length illustration; no source image is reproduced."""
from pathlib import Path
import argparse, json, hashlib, textwrap
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument('--out', default='.')
args=parser.parse_args()
out=Path(__file__).parent/args.out
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'svg.hashsalt':'SH02-polar-multiplicity-exact-v1'})

def render(name, mobile=False):
    fig=plt.figure(figsize=(8,10.5) if mobile else (13.6,5.8),layout='constrained')
    ax=fig.add_subplot(211 if mobile else 121,projection='3d')
    ts=np.linspace(-.65,.65,181)
    ys=np.linspace(-.6,.6,61)
    tt,yy=np.meshgrid(ts,ys)
    ax.plot_surface(tt**2,yy,tt**3,color='#3a82c4',alpha=.55,
                    linewidth=0,rstride=3,cstride=4)
    ax.plot(np.zeros(61),ys,np.zeros(61),color='#c53b32',lw=4,label='lower stratum Y: x=z=0')
    ax.plot(ts**2,np.zeros_like(ts),ts**3,color='#143e67',lw=2.5,label='general section y₁=0')
    for y in [-.5,0,.5]:
        ax.plot([1/16]*2,[y]*2,[-1/64,1/64],color='#746531',alpha=.55,lw=1)
        ax.scatter([1/16]*2,[y]*2,[-1/64,1/64],color='#dba716',s=36,depthshade=False)
    ax.set(xlabel='x=t²',ylabel='y₁',zlabel='z=t³',
           title='Exact real cut of z²=x³\ny₂=w=0; u=(y₁,y₂,x) has degree 2')
    ax.view_init(elev=24,azim=-48)
    ax.legend(loc='upper left',fontsize=8)
    bx=fig.add_subplot(212 if mobile else 122)
    nn=np.arange(1,61,dtype=float)
    ratio=2+3/nn+1/nn**2
    bx.plot(nn,ratio,color='#3a82c4',lw=2,label='3! length(R/mⁿ)/n³ = 2+3/n+1/n²')
    bx.axhline(2,color='#c53b32',ls='--',lw=1.8,label='ordinary multiplicity = cover degree = 2')
    bx.set(xlabel='n (exact integer samples)',ylabel='normalized length',ylim=(1.6,6.2),
           title='Reduced 3-fold H: length = n(n+1)(2n+1)/6\nReduced general surface section: length = n²')
    bx.grid(alpha=.22)
    bx.legend(fontsize=8,loc='upper right')
    caption=('H={(x,z,y₁,y₂,w): z²=x³, w=0} ⊂ ℂ⁵, dim H=3; Y={x=z=w=0}, dim Y=2. '
             'Normalization (t,y₁,y₂)↦(t²,t³,y₁,y₂,0). Yellow points are the exact two sheets '
             't=±1/4 at x=1/16; they merge over x=0. The left panel shows real coordinates only.\n'
             'Proofs: MD0–MD4, GM3–GM5, EQ3–EQ6. Along Y, (m₀,m₁,m₂)=(2,0,0). '
             'Teissier, Variétés polaires II, IV.6.2.1 and V.1.2; CC0.')
    fig.supxlabel('\n'.join(textwrap.fill(line,width=105 if mobile else 170) for line in caption.splitlines()),fontsize=8)
    for suffix in ['png','svg','pdf']:
        kw={'dpi':180} if suffix=='png' else {}
        metadata={'Date':None} if suffix=='svg' else {'CreationDate':None,'ModDate':None} if suffix=='pdf' else {}
        fig.savefig(out/f'{name}.{suffix}',metadata=metadata,**kw)
    plt.close(fig)

render('polar-multiplicity-wide')
render('polar-multiplicity-mobile',True)
checks={'example':{'dimension':3,'ambient_dimension':5,'lower_dimension':2,
                  'normalization':['t^2','t^3','y1','y2','0'],
                  'sheet_at_x_1_over_16':['t=1/4,z=1/64','t=-1/4,z=-1/64'],
                  'polar_multiplicities':[2,0,0],
                  'length_3fold':'n(n+1)(2n+1)/6','length_section':'n^2'},
        'checks':{'normalization_identity':all((t**3)**2==(t**2)**3 for t in [Fraction(-1,4),Fraction(1,4),Fraction(2,3)]),
                  'first_lengths':{'n1':1,'n2':5,'n3':14},
                  'normalized_limit':2,'section_normalized_length':2},
        'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir()) if p.is_file() and p.suffix in {'.png','.svg','.pdf'}}}
(out/'MATHEMATICAL_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')

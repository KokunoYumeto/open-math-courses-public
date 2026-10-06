"""Original CC0 figure of an actual locally finite partition on the real line."""
from pathlib import Path
import argparse, hashlib, json, platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as fm
import numpy as np
import PIL

HERE = Path(__file__).resolve().parent
FP = FontProperties(fname=str(HERE/'fonts/DejaVuSans.ttf'))
FB = FontProperties(fname=str(HERE/'fonts/DejaVuSans-Bold.ttf'))
loaded_fonts = set()
original_get_font = fm._get_font
def record_font_load(font_filepaths, *args, **kwargs):
    loaded_fonts.update(str(x) for x in font_filepaths)
    return original_get_font(font_filepaths, *args, **kwargs)
fm._get_font = record_font_load

def plateau(t, delta=.6, beta=.9):
    """The exact eta quotient, evaluated stably in the transition interval.

    Numerical sampling clips a log ratio at +/-700 to avoid float overflow.
    The plateau and support regions are assigned their exact values 1 and 0.
    The proof and figure coordinates are not changed by this floating-point aid.
    """
    t = np.asarray(t, dtype=float)
    radius = np.abs(t)
    answer = np.zeros_like(radius)
    answer[radius <= delta] = 1.
    transition = (radius > delta) & (radius < beta)
    D = beta**2-delta**2
    a = (beta**2-radius[transition]**2)/D
    b = (radius[transition]**2-delta**2)/D
    log_ratio = 1/a**2-1/b**2
    answer[transition] = 1/(1+np.exp(np.clip(log_ratio, -700, 700)))
    return answer

def draw(output):
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':12,
        'svg.fonttype':'path', 'svg.hashsalt':'original-locally-finite-partition-v1',
        'axes.unicode_minus':False, 'savefig.facecolor':'white'})
    colors = ['#6b54a0', '#287f91', '#bf692f', '#3259a7', '#27816a']
    ink = '#233346'
    x = np.linspace(-2, 2, 2401)
    js = np.arange(-2,3)
    weights = np.stack([plateau(x-j) for j in js])
    S = weights.sum(axis=0)
    normalized = weights/S
    fig, axes = plt.subplots(3,1,figsize=(11,10),
        gridspec_kw={'height_ratios':[1.12,1,1]})
    fig.subplots_adjust(left=.095,right=.96,bottom=.10,top=.865,hspace=.40)
    a,b,c = axes
    a.set_xlim(-2,2);a.set_ylim(-3.6,3.6)
    for j in range(-3,4):
        color = colors[(j+2)%5]
        a.plot([j-1.1,j+1.1],[j,j],color='#cbd1da',lw=11,solid_capstyle='butt')
        a.plot([j-.9,j+.9],[j,j],color=color,alpha=.30,lw=8,solid_capstyle='butt')
        a.plot([j-.6,j+.6],[j,j],color=color,lw=3.2,solid_capstyle='butt')
        a.scatter([j-.9,j+.9],[j,j],s=24,color=color,zorder=3)
        a.scatter([j-1.1,j+1.1],[j,j],s=35,facecolors='white',edgecolors='#748093',zorder=4)
    a.set_yticks(range(-3,4))
    a.set_yticklabels([f'j = {j}' for j in range(-3,4)],fontproperties=FP)
    a.set_xticks([-2,-1,0,1,2])
    a.set_title('A  Locally finite coordinate intervals on the whole line',loc='left',fontproperties=FB,color=ink,fontsize=14,pad=13)
    a.text(0,-.19,'Grey: Uⱼ (radius 11/10)     Shaded: closed support (radius 9/10)     Dark: plateau (radius 3/5)',
        transform=a.transAxes,fontproperties=FP,fontsize=10,color=ink)
    for j,color,w,h in zip(js,colors,weights,normalized):
        b.plot(x,w,color=color,lw=2,label=f'j = {j}')
        c.plot(x,h,color=color,lw=2,label=f'j = {j}')
    b.plot(x,S,color=ink,lw=2.2,ls='--',label='S = sum of weights')
    b.set_ylim(-.04,2.17)
    b.set_yticks([0,.5,1,1.5,2])
    b.set_ylabel('wⱼ and S',fontproperties=FP)
    b.set_title('B  Smooth plateau bumps: 1 ≤ S ≤ 2 everywhere',loc='left',fontproperties=FB,color=ink,fontsize=14,pad=13)
    b.legend(loc='upper left',ncol=3,prop=FontProperties(fname=str(HERE/'fonts/DejaVuSans.ttf'),size=9),framealpha=.95)
    c.axhline(1,color=ink,ls='--',lw=1.4,label='sum hⱼ = 1')
    c.scatter([0,.5],[1,.5],s=32,color=ink,zorder=5)
    c.annotate('h₀(0) = 1',xy=(0,1),xytext=(.13,1.04),fontproperties=FP,fontsize=11,color=ink)
    c.annotate('h₀(1/2) = h₁(1/2) = 1/2',xy=(.5,.5),xytext=(.65,.35),
        fontproperties=FP,fontsize=11,color=ink,arrowprops={'arrowstyle':'->','color':ink})
    c.set_ylim(-.04,1.2);c.set_yticks([0,.5,1])
    c.set_ylabel('hⱼ = wⱼ / S',fontproperties=FP)
    c.set_xlabel('x  (only the window [−2, 2] is shown)',fontproperties=FP)
    c.set_title('C  Normalization preserves compact support and gives sum one',loc='left',fontproperties=FB,color=ink,fontsize=14,pad=13)
    for ax in axes:
        ax.set_xlim(-2,2)
        ax.grid(axis='x',alpha=.16)
        for label in [*ax.get_xticklabels(),*ax.get_yticklabels()]:
            label.set_fontproperties(FP)
        for spine in ['top','right']:
            ax.spines[spine].set_visible(False)
    fig.text(.095,.97,'From a locally finite cover to a smooth partition of unity',
        fontproperties=FB,fontsize=18,color=ink,va='top')
    fig.text(.095,.932,'Actual functions from Theorem 3.E.  Integer indices run through ℤ; inner balls cover ℝ.',
        fontproperties=FP,fontsize=11.5,color=ink,va='top')
    fig.text(.095,.029,'Lemmas 3.A–3.B, Theorems 3.E–3.1, and Exercise 6.5.  Smooth curves are numerical samples of the proved formula.',
        fontproperties=FP,fontsize=10.5,color=ink)
    base = output/'local-tools-partition-of-unity'
    fig.savefig(base.with_suffix('.png'),dpi=200,metadata={'Software':'Original CC0 partition-of-unity illustration'})
    fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'Original CC0 partition-of-unity illustration'})
    plt.close(fig)
    assert {Path(p).name for p in loaded_fonts} == {'DejaVuSans.ttf','DejaVuSans-Bold.ttf'}, loaded_fonts
    data = {'chart_radius':'11/10','delta':'3/5','beta':'9/10','epsilon':'1',
        'D':'9/20','whole_index_set':'all integers','sample_window':[-2,2],
        'sample_count':len(x),'numerical_scope':'Actual plateau quotient sampled in double precision; transition log ratios clipped at +/-700.',
        'versions':{'Python':platform.python_version(),'Matplotlib':matplotlib.__version__,
            'NumPy':np.__version__,'Pillow':PIL.__version__},
        'actual_loaded_fonts':[{'filename':Path(p).name,
            'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest()} for p in sorted(loaded_fonts)]}
    (output/'figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(data))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=HERE.parents[1]/'figures')
    draw(parser.parse_args().output)

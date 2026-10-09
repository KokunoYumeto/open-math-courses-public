"""Exact multiplier zero formulas and proved carrier inclusions."""
from pathlib import Path
import json, os, tempfile
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90
A=mp.mpf(1)/16
beta=mp.mpf(7)/8
R=A*mp.zeta(1/beta)
records=[]
for j in range(1,100):
    a=A*mp.power(j,-1/beta)
    if mp.pi/a>300:break
    for m in range(1,100):
        x=mp.pi*m/a
        if x>300:break
        for sign in [-1,1]:
            records.append(dict(j=j,m=sign*m,
                                exact_x_formula='16*pi*m*j^(8/7)',
                                x_decimal=mp.nstr(sign*x,85),
                                Q1_imaginary=0,Q2_imaginary=-1))

out=ROOT/'figures'
out.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='an02-own256-mpl-') as cfg:
    os.environ['MPLCONFIGDIR']=cfg
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    fig,(ax,bx)=plt.subplots(1,2,figsize=(13.4,4.8),gridspec_kw={'width_ratios':[1.7,1]})
    xs=[float(v['x_decimal']) for v in records]
    ax.axhline(0,color='#326ea0',lw=1.2,alpha=.4)
    ax.axhline(-1,color='#aa4c23',lw=1.2,alpha=.4)
    ax.scatter(xs,[0]*len(xs),s=20,color='#326ea0',label='Zeros of Q₁')
    ax.scatter(xs,[-1]*len(xs),s=20,marker='s',color='#aa4c23',label='Zeros of Q₂(z)=Q₁(z+i)')
    ax.set(xlim=(-300,300),ylim=(-1.55,.7),xlabel='Real part of z',ylabel='Imaginary part of z',
           title='Disjoint zero sets: an exact visible window')
    ax.set_yticks([-1,0])
    ax.legend(loc='upper center',fontsize=9,frameon=True)
    ax.grid(alpha=.2)
    bx.add_patch(Rectangle((-1,-1),2,2,fill=False,edgecolor='#747c83',lw=2))
    bx.plot([-1,1],[0,0],color='#704a9b',lw=5,label='Carriers of μ₁, μ₂ are within this line')
    bx.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),xlabel='x₁ / R',ylabel='x₂ / R',
           title='Proved carrier bounds for six kernels')
    bx.set_aspect('equal')
    bx.set_xticks([-1,0,1]);bx.set_yticks([-1,0,1]);bx.grid(alpha=.15)
    bx.text(0,1.13,'Four smooth kernels lie within the square',ha='center',fontsize=9)
    bx.text(0,-1.25,'Two kernels have order at most one',ha='center',fontsize=9)
    fig.tight_layout(w_pad=2.3)
    fig.savefig(out/'multiplier-zeros-and-kernel-carriers.png',dpi=165,
                metadata={'Author':'GPT-6.1 Sol (OpenAI)'})
    fig.savefig(out/'multiplier-zeros-and-kernel-carriers.svg',
                metadata={'Creator':'GPT-6.1 Sol (OpenAI)'})
    plt.close(fig)

geometry=dict(beta='7/8',A='1/16',d=1,R_exact='zeta(8/7)/16',R_decimal=mp.nstr(R,85),
              R_upper_bound='1/2',c_exact='log(4)*64^(-7/8)',
              frequency_window=[-300,300],zero_records=records,
              all_zeros_in_the_shown_window_included=True,
              carrier_coordinates_normalized_by_R=True,
              first_two_carrier_bound=[[-1,1],[0,0]],
              last_four_carrier_bound=[[-1,1],[-1,1]],
              exact_support_equality_not_claimed=True,
              nonzero_system_solution_requires_the_separate_proper_ideal_hypothesis=True)
(out/'geometry256.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'positive_zero_count':len(records)//2,'figure_directory':str(out),'temporary_font_cache_removed':not Path(cfg).exists()}))

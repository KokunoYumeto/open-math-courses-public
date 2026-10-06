"""Original CC0 figure: exact leading density powers and interval thresholds."""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                    'axes.labelsize':13,'axes.titlesize':15})
fig,axs=plt.subplots(1,2,figsize=(14.4,7.2),dpi=150,
                     gridspec_kw={'width_ratios':[1.15,1]})
fig.subplots_adjust(left=.075,right=.965,bottom=.19,top=.85,wspace=.33)
s=np.linspace(.5,1,1001)
ax=axs[0]
ax.plot(s,3*(1-s)/(2-s),color='#254f87',lw=2.7,label='Ingham')
ax.plot(s,12/5*(1-s),color='#167d78',lw=2.2,ls='--',label='Uniform Huxley bound')
ax.plot(s,2*(1-s),color='#777777',lw=2,ls=':',label='Density hypothesis (conjectural)')
sm=np.linspace(.7,.8,301)
ax.plot(sm,15*(1-sm)/(3+5*sm),color='#b94b21',lw=4,label='Guth–Maynard, middle range')
ax.scatter([.75,.75],[3/5,5/9],color=['#254f87','#b94b21'],s=38,zorder=5)
ax.annotate('3/5',(.75,3/5),xytext=(.8,.74),arrowprops={'arrowstyle':'-','color':'#254f87'},color='#254f87')
ax.annotate('5/9',(.75,5/9),xytext=(.66,.40),arrowprops={'arrowstyle':'-','color':'#b94b21'},color='#b94b21')
ax.set(xlim=(.5,1),ylim=(0,1.26),xlabel=r'Real-part cutoff $\sigma$',
       ylabel=r'Leading power of $T$',title='Counting zeros to the right')
ax.set_xticks([.5,.6,.7,.75,.8,.9,1])
ax.grid(alpha=.18)
ax.legend(loc='upper right',fontsize=9.5,framealpha=.97)

ax=axs[1]
rows=[('Ingham',Fraction(2,3),'2/3','#254f87'),
      ('Historical Weyl input',Fraction(5,8),'5/8','#7864a4'),
      ('Huxley',Fraction(7,12),'7/12','#167d78'),
      ('Guth–Maynard',Fraction(17,30),'17/30','#b94b21'),
      ('Density hypothesis',Fraction(1,2),'1/2','#777777')]
for i,(name,value,label,color) in enumerate(rows):
    y=len(rows)-1-i
    x=float(value)
    ax.plot([x,.73],[y,y],color=color,lw=2,
            ls=':' if name=='Density hypothesis' else '-')
    ax.scatter([x],[y],facecolors='white',edgecolors=color,s=65,lw=2,zorder=5)
    ax.annotate('',xy=(.735,y),xytext=(.72,y),arrowprops={'arrowstyle':'->','color':color,'lw':2})
    ax.text(x+.002,y+.19,label,color=color,fontsize=11)
ax.set_yticks(range(5),[r[0] for r in rows[::-1]])
ax.tick_params(axis='y',length=0,labelsize=10.5)
ax.set(xlim=(.485,.745),ylim=(-.6,4.65),
       xlabel=r'Interval exponent $\theta$',title='Asymptotics for every interval')
ax.set_xticks([.5,.55,.6,.65,.7])
ax.grid(axis='x',alpha=.18)
ax.text(.50,-.49,'Open circles: strict thresholds',fontsize=10)
fig.suptitle('Density estimates and prime intervals',fontsize=20,y=.95)
fig.text(.075,.072,'Leading exponents only: logarithmic factors and arbitrary epsilon losses are omitted.',
         fontsize=11,color='#444444')
fig.text(.075,.037,'Interval arrows mean theta is strictly above the threshold. The last row assumes the density hypothesis.',
         fontsize=11,color='#444444')
out=base/'density_intervals.png'
fig.savefig(out,metadata={'Software':'Matplotlib; original CC0 course figure'})
plt.close(fig)
checks={
 'density_at_three_quarters':{'Ingham':str(Fraction(3,5)),
                             'Guth-Maynard':str(Fraction(5,9))},
 'interval_thresholds':{name:str(value) for name,value,_,_ in rows},
 'formula_checks':{'Ingham_factor_at_three_quarters':str(Fraction(12,5)),
                   'global_Guth_Maynard_factor':str(Fraction(30,13))},
 'licence':'CC0-1.0','figure_pixels':[2160,1080]}
(base/'density_intervals_checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,indent=2))

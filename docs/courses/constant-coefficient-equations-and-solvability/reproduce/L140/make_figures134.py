"""Exact scalar sections and exact integral profiles for original L140."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OWN=Path(__file__).resolve().parent
OUT=OWN/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':14,
                    'axes.labelsize':12,'legend.fontsize':10,'svg.fonttype':'none',
                    'svg.hashsalt':'AN02-L140-original134','text.usetex':False})
COLORS=['#1b6ca8','#cc5a18','#327a47','#8056a2']
PARAMS=[1,2,4,8]

def average(s,t):
    c=np.asarray(s,dtype=float)/t
    return np.where(c>=0,1+2*c,np.where(c<=-1,-1-2*c,1+2*c+2*c*c))

def save(fig,stem):
    fig.savefig(OUT/f'{stem}.png',dpi=160,metadata={'Software':'Original L140 scientific figure; CC0 1.0'})
    fig.savefig(OUT/f'{stem}.svg',metadata={'Date':'2026-10','Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0 1.0'})
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(13.4,5.5))
fig.subplots_adjust(left=.07,right=.98,bottom=.18,top=.84,wspace=.30)
r=np.geomspace(1e-3,3,1200)
for j,color in zip(PARAMS,COLORS):
    axes[0].semilogx(r,np.log(r)/j,color=color,lw=2,label=rf'$j={j}$')
axes[0].axhline(0,color='#333333',lw=1,ls=':')
axes[0].axvline(1,color='#777777',lw=1,ls=':')
axes[0].set(xlim=(1e-3,3),ylim=(-7.3,1.35),xlabel='Radius r (logarithmic axis)',
            ylabel=r'$v_j(r)=\log(r)/j$',title='Original logarithmic functions')
axes[0].legend(title='Sequence index',loc='lower right')
axes[0].grid(alpha=.22)
r2=np.linspace(0,3,1000)
tail=np.zeros_like(r2)
tail[r2>1]=np.log(r2[r2>1])
for k,color in zip(PARAMS,COLORS):
    axes[1].plot(r2,tail/k,color=color,lw=2,label=rf'$k={k}$')
axes[1].scatter([0],[0],s=80,facecolors='white',edgecolors='#222222',lw=2,zorder=6,clip_on=False)
axes[1].annotate('At the center:\nregularized value 0;\nraw tail value −∞',xy=(0,0),xytext=(.20,.45),
                 textcoords='data',arrowprops={'arrowstyle':'->','color':'#222222'},fontsize=11,
                 bbox={'boxstyle':'round,pad=.35','fc':'white','ec':'#bbbbbb'})
axes[1].axvline(1,color='#777777',lw=1,ls=':')
axes[1].set(xlim=(0,3),ylim=(-.10,1.22),xlabel='Radius r (linear axis)',
            ylabel=r'$U_k(r)=\max(0,\log r)/k$',title='Regularized tail envelopes')
axes[1].legend(title='Tail starts at',loc='upper left')
axes[1].grid(alpha=.22)
fig.suptitle('A permanent logarithmic hole and its upper envelope',fontsize=17,y=.97)
fig.text(.5,.055,'Exact radial sections in the complex plane. The point r = 0 is omitted from the logarithmic samples; each original value there is −∞.',
         ha='center',va='center',fontsize=10)
save(fig,'logarithmic-tail-envelopes')

fig,axes=plt.subplots(1,3,figsize=(18,5.8),gridspec_kw={'width_ratios':[.95,1.15,1.5]})
fig.subplots_adjust(left=.05,right=.98,bottom=.20,top=.83,wspace=.36)
axes[0].add_patch(Rectangle((-1,0),2,1,facecolor='#e5f1f8',edgecolor='#1b6ca8',lw=2))
axes[0].axhline(0,color='#333333',lw=1);axes[0].axvline(0,color='#333333',lw=1)
axes[0].text(0,.52,'K\nArea = 2',ha='center',va='center',fontsize=16,color='#175578')
axes[0].set(xlim=(-1.4,1.4),ylim=(-.22,1.22),xticks=[-1,0,1],yticks=[0,1],
            xlabel='u = Re w',ylabel='b = Im w',title='The translation set')
axes[0].set_aspect('equal',adjustable='box')
axes[0].grid(alpha=.16)
b=np.linspace(0,1,1001)
for t,color in zip(PARAMS,COLORS):
    axes[1].plot(b,np.abs(b-1/t),color=color,lw=2,label=rf'$t={t}$')
axes[1].set(xlim=(0,1),ylim=(-.03,1.08),xlabel='b = Im w',ylabel=r'$|b-1/t|$',
            title='Normalized profiles at s = −1')
axes[1].legend(loc='upper center',ncol=2)
axes[1].grid(alpha=.22)
s=np.linspace(-2,2,1601)
for t,color in zip(PARAMS,COLORS):
    axes[2].plot(s,average(s,t),color=color,lw=2,label=rf'$t={t}$')
axes[2].axhline(1,color='#333333',lw=1.5,ls='--',label='Fixed-center limit L = 1')
axes[2].axvline(-1,color='#777777',lw=1,ls=':')
axes[2].set(xlim=(-2,2),ylim=(.35,5.2),xlabel='Center height s = Im ζ',
            ylabel=r'$a_t(\zeta)=2\int_0^1|b+s/t|\,db$',title='Exact scaled averages')
axes[2].legend(loc='upper left',ncol=2)
axes[2].grid(alpha=.22)
fig.suptitle('Complex-line translations and a computable scaling limit',fontsize=18,y=.97)
fig.text(.5,.095,'Input q(ζ) = |Im ζ|, direction y = 1. Twice the middle-panel area is the average at s = −1.',ha='center',fontsize=12)
fig.text(.5,.047,'Exact values at s = −1: t = 1 → 1; t = 2 → 1/2; t = 4 → 5/8; t = 8 → 25/32. The fixed center is held still as t increases.',
         ha='center',fontsize=11)
save(fig,'scaled-translation-averages')

geometry={'schema':'AN02-L140-original-geometry134/v1','dimension':'Figures use one complex dimension, with its ordinary Euclidean metric.',
          'logarithmic-tail-envelopes':{
              'proof_locators':['UE3','UE5','UE8','UE26','UE27'],
              'original_formula':'v_j(r)=log(r)/j, v_j(0)=-infinity',
              'tail_formula':'f_k(0)=-infinity; f_k(r)=0 for0<r<=1; f_k(r)=log(r)/k forr>1',
              'regularized_formula':'U_k(r)=max(0,log(r))/k forr>0; U_k(0)=0',
              'indices':PARAMS,'original_sample_radius':[.001,3],'original_sample_points':1200,
              'regularized_sample_radius':[0,3],'regularized_sample_points':1000,
              'singularity_policy':'The original singular value is stated as minus infinity; it is never replaced by a finite plotted value.'},
          'scaled-translation-averages':{
              'proof_locators':['UE7','UE8','UE23','UE28','UE29'],
              'input':'q(zeta)=abs(Im zeta)','direction_y':1,
              'K':{'real_interval':[-1,1],'imaginary_interval':[0,1],'area':2},
              'support_function':'H(b)=abs(b)','target_L':1,
              'average_formula':'a_t(s)=2*integral_0^1 abs(b+s/t) db',
              'piecewise_variable':'c=s/t',
              'piecewise_branches':{'c>=0':'1+2c','-1<=c<=0':'1+2c+2c^2','c<=-1':'-1-2c'},
              'parameters_t':PARAMS,'profile_fixed_s':-1,'profile_b_interval':[0,1],
              'center_sample_s_interval':[-2,2],'center_sample_points':1601,
              'values_at_s_minus_one':{'1':1,'2':.5,'4':.625,'8':.78125},
              'proved_upper_bound':'a_t(s)<=1+2*abs(s)/t','limit':'For each fixed s, a_t(s)->1.'},
          'rendering':{'PNG_dpi':160,'SVG_text':'Editable text with DejaVu Sans font notice.'}}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':['logarithmic-tail-envelopes','scaled-translation-averages'],
                  'exact_average_values':{str(t):float(average(-1,t)) for t in PARAMS}},indent=2))

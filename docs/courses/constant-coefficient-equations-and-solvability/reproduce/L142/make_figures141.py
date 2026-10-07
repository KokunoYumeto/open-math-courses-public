"""Original L142 exact support geometry and Fourier-growth illustrations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

OWN=Path(__file__).resolve().parent
OUT=OWN/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':14,
                    'axes.labelsize':12,'legend.fontsize':10,'svg.fonttype':'none',
                    'svg.hashsalt':'AN02-L142-original141','text.usetex':False})
BLUE='#176ba4';ORANGE='#c65b19';GREEN='#278150'
MASS=2+np.sqrt(2)
def save(fig,name):
    fig.savefig(OUT/f'{name}.png',dpi=160,metadata={'Software':'Original L142 scientific figure; CC0 1.0'})
    fig.savefig(OUT/f'{name}.svg',metadata={'Date':'2026-10','Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0 1.0'})
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(13.4,5.8),gridspec_kw={'width_ratios':[1,1.5]})
fig.subplots_adjust(left=.06,right=.98,bottom=.19,top=.83,wspace=.32)
triangle=np.array([[-1,0],[1,0],[0,2]])
axes[0].add_patch(Polygon(triangle,closed=True,facecolor='#e6f1f7',edgecolor=BLUE,lw=2))
axes[0].scatter(triangle[:,0],triangle[:,1],color=BLUE,s=70,zorder=5)
axes[0].text(-1,-.23,'coefficient 1',ha='center',va='top',fontsize=11)
axes[0].text(1,-.23,'coefficient i',ha='center',va='top',fontsize=11)
axes[0].text(.55,2.45,'coefficient −1 − i',ha='center',fontsize=11)
xx=np.linspace(-1.7,1.7,400)
axes[0].plot(xx,2-xx,color=GREEN,lw=1.8,ls='--')
axes[0].text(.72,1.53,r'$s_1+s_2=2$',rotation=-45,ha='left',fontsize=11,
             bbox={'fc':'white','ec':'none','alpha':.92,'pad':2})
axes[0].annotate('',xy=(-.5,1.55),xytext=(-1.25,.80),
                 arrowprops={'arrowstyle':'->','color':GREEN,'lw':2})
axes[0].text(-1.55,1.86,'η = (1, 1)',color=GREEN,fontsize=11)
axes[0].axhline(0,color='#555555',lw=.7)
axes[0].set(xlim=(-1.7,1.7),ylim=(-.55,2.7),xticks=[-1,0,1],yticks=[0,1,2],
            xlabel='Support coordinate s₁',ylabel='Support coordinate s₂',title='Support and complex coefficients')
axes[0].set_aspect('equal',adjustable='box');axes[0].grid(alpha=.18)
t=np.linspace(-3,3,1601)
profile=np.maximum.reduce([-t,t,2*t])
envelope=np.log(np.exp(-t)+np.exp(t)+np.sqrt(2)*np.exp(2*t))
axes[1].fill_between(t,profile,profile+np.log(MASS),color='#dae8ee',alpha=.7,label=r'Proved strip: $h_K\leq M\leq h_K+\log m$')
axes[1].plot(t,envelope,color=BLUE,lw=2.4,label='Exact horizontal envelope M(tη)')
axes[1].plot(t,profile,color=GREEN,lw=2,ls='--',label='Hull profile hK(tη) = max(−t, t, 2t)')
axes[1].scatter([0],[np.log(MASS)],color=BLUE,s=55,zorder=5)
axes[1].annotate('F(0) = 0 through cancellation;\nM(0) = log(2 + √2) is finite',
                 xy=(0,np.log(MASS)),xytext=(-2.8,4.6),fontsize=11,
                 arrowprops={'arrowstyle':'->','lw':1,'color':'#444444'},
                 bbox={'boxstyle':'round,pad=.35','fc':'white','ec':'#bbbbbb'})
axes[1].set(xlim=(-3,3),ylim=(-.15,7.55),xlabel='Imaginary-height parameter t, with y = t(1, 1)',
            ylabel='Log modulus envelope / support profile',title='Exact envelope and support function')
axes[1].legend(loc='upper left',fontsize=9.5);axes[1].grid(alpha=.20)
fig.suptitle('Complex cancellation preserves the exact convex support indicator',fontsize=17,y=.97)
fig.text(.5,.067,'The envelope supremum is attained here at real frequency (π/4, −π/2), which aligns the three phases. The general proof uses growth-to-support uniqueness.',
         ha='center',fontsize=10)
save(fig,'complex-triangle-envelope')

fig,axes=plt.subplots(1,2,figsize=(13.4,5.5),gridspec_kw={'width_ratios':[1,1.4]})
fig.subplots_adjust(left=.07,right=.98,bottom=.19,top=.84,wspace=.30)
axes[0].fill_between([-1,0],0,1,color='#dcebf5',alpha=.9)
axes[0].fill_between([0,1],0,-1,color='#f8e3d5',alpha=.9)
axes[0].plot([-1,0],[1,1],color=BLUE,lw=3)
axes[0].plot([0,1],[-1,-1],color=ORANGE,lw=3)
axes[0].plot([-1.4,-1],[0,0],color='#555555',lw=1.5)
axes[0].plot([1,1.4],[0,0],color='#555555',lw=1.5)
axes[0].axhline(0,color='#555555',lw=.7);axes[0].axvline(0,color='#555555',lw=.7,ls=':')
axes[0].text(-.5,.5,'+1 ds',ha='center',color=BLUE,fontsize=17)
axes[0].text(.5,-.55,'−1 ds',ha='center',color=ORANGE,fontsize=17)
axes[0].set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xticks=[-1,0,1],yticks=[-1,0,1],
            xlabel='Carrier coordinate s',ylabel='Signed Lebesgue density',title='Support [−1, 1]; no endpoint atoms')
axes[0].grid(alpha=.18)
t2=np.geomspace(.5,32,1400)
quotient=1-np.log(t2)/t2+2*np.log(-np.expm1(-t2))/t2
axes[1].semilogx(t2,quotient,color=BLUE,lw=2.5,label=r'Exact $\log|F(it)|/t$')
axes[1].semilogx(t2,1+np.log(2)/t2,color=ORANGE,lw=1.8,ls=':',label=r'Variation bound $1+\log2/t$')
axes[1].axhline(1,color=GREEN,lw=1.8,ls='--',label='Exact hull slope H(1) = 1')
axes[1].set(xlim=(.5,32),ylim=(-1.55,2.55),xlabel='Height t (logarithmic axis)',
            ylabel='Normalized logarithmic growth',title='Canceled mass, full endpoint growth')
axes[1].set_xticks([.5,1,2,4,8,16,32]);axes[1].set_xticklabels(['1/2','1','2','4','8','16','32'])
axes[1].legend(loc='upper right');axes[1].grid(alpha=.2)
fig.suptitle('A signed density with zero total mass still sees both support endpoints',fontsize=16,y=.97)
fig.text(.5,.065,'Total complex mass = 0; total variation = 2. Every endpoint neighborhood has positive variation, although each endpoint itself has zero mass.',
         ha='center',fontsize=10.5)
save(fig,'signed-density-growth')

geometry={'schema':'AN02-L142-original-geometry141/v1','Fourier_convention':'F(z)=integral exp(-i*s dot z) du(s)',
          'complex-triangle-envelope':{
              'proof_locators':['MI4','MI5','MI7','MI22–MI24'],
              'support_points':[[-1,0],[1,0],[0,2]],
              'complex_coefficients':[{'real':1,'imaginary':0},{'real':0,'imaginary':1},{'real':-1,'imaginary':-1}],
              'total_complex_mass':{'real':0,'imaginary':0},'total_variation':'2+sqrt(2)',
              'direction_eta':[1,1],'support_line':'s1+s2=2','support_value':2,
              'real_alignment_frequency':['pi/4','-pi/2'],'common_phase':'exp(i*pi/4)',
              'exact_envelope':'M(y)=log(exp(-y1)+exp(y1)+sqrt(2)*exp(2*y2))',
              'support_function':'h_K(y)=max(-y1,y1,2*y2)',
              'slice_y':'t*(1,1)','sample_t_interval':[-3,3],'sample_points':1601,
              'proved_gap':'0<=M(y)-h_K(y)<=log(2+sqrt(2))',
              'metric':'Ordinary Euclidean metric, with equal coordinate scale in the support panel.'},
          'signed-density-growth':{
              'proof_locators':['MI2','MI5','MI7','MI25–MI27'],
              'density':'1_[-1,0](s)-1_[0,1](s) relative to ds; point values have no effect on the measure.',
              'support':[-1,1],'total_mass':0,'total_variation':2,'endpoint_atomic_masses':[0,0],
              'transform':'F(z)=2*(cos(z)-1)/(i*z), entire extension F(0)=0',
              'first_moment':-1,'transform_derivative_at_zero':'i',
              'exact_ray_modulus':'abs(F(i*t))=exp(t)*(1-exp(-t))^2/t for t>0',
              'exact_quotient':'1-log(t)/t+2*log(1-exp(-t))/t',
              'variation_upper_bound':'1+log(2)/t','target_slope':1,
              'sample_t_interval':[.5,32],'sample_points':1400,'horizontal_axis':'Logarithmic t axis.'},
          'rendering':{'PNG_dpi':160,'SVG_text':'Editable labels using DejaVu Sans; the font notice accompanies the original sources.'}}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':['complex-triangle-envelope','signed-density-growth'],
                  'triangle_gap_range_sampled':[float(np.min(envelope-profile)),float(np.max(envelope-profile))],
                  'variation':float(MASS),'density_quotient_at_32':float(quotient[-1])},indent=2))

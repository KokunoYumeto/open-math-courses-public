"""Exact seed geometry, actual closed error, polynomial zeros and integral rate."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Wedge
import numpy as np
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
 'svg.hashsalt':'AN02-entire-logarithm-density154','axes.spines.top':False,'axes.spines.right':False})
INNER=1/12;OUTER=1/6
def derivative(r):
 if not INNER<r<OUTER:return 0.0
 t=(r-INNER)/(OUTER-INNER);s=-1/t+1/(1-t)
 c=math.exp(-s)/(1+math.exp(-s)) if s>0 else 1/(1+math.exp(s))
 return -c*(1-c)*(1/t**2+1/(1-t)**2)/(OUTER-INNER)
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=170,facecolor='white')
 fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Open Mathematics Courses'},facecolor='white');plt.close(fig)

fig,(left,right)=plt.subplots(1,2,figsize=(12,6.5))
fig.subplots_adjust(left=.07,right=.97,top=.80,bottom=.33,wspace=.27)
fig.suptitle('Quadratic seeds confine the closed error to disjoint annuli',y=.96,fontsize=17)
fig.text(.5,.88,r'$\phi(z)=|z|^2,\quad a=\pm1/2,\quad P_a(z)=2\overline{a}z-|a|^2$',ha='center',fontsize=13)
for a in [-.5,.5]:
 left.add_patch(Circle((a,0),.25,fill=False,ls='--',ec='#8098a8',lw=1.5))
 left.add_patch(Wedge((a,0),OUTER,0,360,width=OUTER-INNER,facecolor='#e7b767',alpha=.7))
 left.add_patch(Circle((a,0),INNER,fill=False,ec='#366886',lw=1.7))
 left.add_patch(Circle((a,0),OUTER,fill=False,ec='#c1802c',lw=1.5))
 left.scatter([a],[0],s=30,color='#172d40',zorder=6)
 left.text(a,-.31,fr'$a={a:g}$',ha='center',fontsize=11)
left.axhline(0,color='#738491',lw=.7,zorder=0);left.axvline(0,color='#738491',lw=.7,zorder=0)
left.text(0,.28,'Disjoint supports',ha='center',fontsize=11)
left.set(xlim=(-.95,.95),ylim=(-.43,.43),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
left.set_aspect('equal',adjustable='box');left.set_xticks([-.75,-.5,0,.5,.75]);left.set_yticks([-.25,0,.25])
left.set_title('Exact centers and cutoff derivative supports',fontsize=12,pad=13)
r=np.linspace(0,.25,1800)
for N,color in [(128,'#347858'),(512,'#9566a1'),(2048,'#2775a0')]:
 error=np.array([.5*abs(derivative(float(s)))*math.exp(-N*s*s) for s in r])
 right.semilogy(r,np.where(error>=1e-12,error,np.nan),color=color,lw=2,label=fr'$N={N}$')
right.axvspan(INNER,OUTER,color='#e7b767',alpha=.18)
right.axvline(INNER,color='#a77940',ls=':',lw=1);right.axvline(OUTER,color='#a77940',ls=':',lw=1)
right.set(xlim=(0,.25),ylim=(1e-12,30),xlabel=r'distance $s=|z-a|$',ylabel=r'actual $|g|e^{-N\phi}$')
right.set_xticks([0,INNER,OUTER,.25],['0','1/12','1/6','1/4']);right.grid(alpha=.13);right.legend(frameon=False)
right.set_title('Actual weighted error: |χ′(s)| exp(−Ns²) / 2',fontsize=12,pad=13)
fig.text(.06,.19,r'Exact gap: $\phi-\operatorname{Re}P_a=|z-a|^2$. Inner radius $1/12$; outer radius $1/6$.',fontsize=11)
fig.text(.06,.135,'Smooth cutoff is flat at both joins; the closed error is zero outside the annuli.',fontsize=11)
fig.text(.06,.09,r'The curves are the cutoff error, not a returned correction. The point estimate is still required for interpolation.',fontsize=10.5)
fig.text(.06,.035,'Original proof GD7–GD9; learner example 4. Human source: Hörmander II, Theorem 15.1.6 and Lemma 15.1.8, pp. 277–278.',fontsize=9.4,color='#384a57')
save(fig,'quadratic-seeds-and-closed-error')

fig,(left,right)=plt.subplots(1,2,figsize=(12,6.5))
fig.subplots_adjust(left=.07,right=.97,top=.80,bottom=.33,wspace=.32)
fig.suptitle('Entire logarithms converge in integral norm despite fixed-point holes',y=.96,fontsize=16)
fig.text(.5,.88,r'$w_N(z)=N^{-1}\log|(1+z^N)/2|,\qquad\phi(z)=\max(0,\log|z|)$',ha='center',fontsize=13)
N=13;t=np.linspace(0,2*np.pi,500)
left.fill(np.cos(t),np.sin(t),color='#e4edf3',alpha=.8)
left.plot(np.cos(t),np.sin(t),color='#678da6',ls='--',lw=1.4)
angles=(2*np.arange(N)+1)*np.pi/N;zeros=np.exp(1j*angles)
left.scatter(zeros.real,zeros.imag,s=33,color='#274f6c',label='13 simple zeros',zorder=4)
left.scatter([-1],[0],s=66,color='#b54249',zorder=5)
left.annotate('Fixed point −1:\nodd N gives −∞',xy=(-1,0),xytext=(-1.30,-1.33),ha='left',fontsize=10,
               color='#92373e',arrowprops={'arrowstyle':'->','color':'#92373e'})
left.axhline(0,color='#83929b',lw=.6,zorder=0);left.axvline(0,color='#83929b',lw=.6,zorder=0)
left.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$');left.set_aspect('equal')
left.set_title(r'Actual zeros for $N=13$: $e^{(2k+1)\pi i/13}$',fontsize=12,pad=13)
left.legend(loc='upper right',frameon=False,fontsize=9)
degrees=np.arange(1,65);errors=4*np.pi*np.log(2)/degrees
right.loglog(degrees,errors,color='#347858',lw=2,label=r'exact disk error $4\pi\log2/N$')
check=json.loads((HERE/'independent-example-checks154.json').read_bytes());assert check['status']=='PASS'
samples=check['disk_error_samples']
right.scatter([x['N'] for x in samples],[x['actual_error'] for x in samples],color='#172d40',s=30,
              label='independent physical polar quadratures',zorder=5)
right.set(xlim=(.9,70),ylim=(.09,11),xlabel=r'positive integer $N$',ylabel=r'$\int_{|z|<2}|w_N-\phi|\,dA$')
right.set_xticks([1,2,4,8,16,32,64],['1','2','4','8','16','32','64']);right.grid(which='both',alpha=.16)
right.set_title('Exact volume integral, not pointwise error',fontsize=12,pad=13);right.legend(loc='upper right',frameon=False,fontsize=9)
fig.text(.06,.19,r'$w_N\leq\phi$ everywhere. Circle-averaged gap is $\log2/N$ for every radius except the single radius 1.',fontsize=11)
fig.text(.06,.13,r'For every $R>0$: $\int_{|z|<R}|w_N-\phi|\,dA=\pi R^2\log2/N$.',fontsize=11)
fig.text(.06,.085,'At −1 the odd subsequence has a zero; the even subsequence has normalized logarithm 0.',fontsize=11)
fig.text(.06,.035,'Original proof GD11; learner example 2. Human source: Hörmander II, Theorem 15.1.6 and Lemma 15.1.7, pp. 277–278.',fontsize=9.4,color='#384a57')
save(fig,'circle-zeros-and-integral-convergence')
geometry={'schema':'AN02-entire-logarithm-geometry154/v1','quadratic_example':{'complex_dimension':1,
 'weight':'|z|^2','centers':[-.5,.5],'center_ball_radius':.25,'cutoff_inner_radius':'1/12',
 'cutoff_outer_radius':'1/6','cutoff_definition':'h(1-t)/(h(1-t)+h(t)), t=(s-1/12)/(1/6-1/12), h(t)=exp(-1/t) if t>0 else 0',
 'exact_gap':'|z-a|^2','actual_error_modulus':'0.5*abs(chi_prime(s))*exp(-N*s^2)',
 'plotted_N':[128,512,2048],'positive_log_plot_floor':1e-12,'returned_correction_plotted':False},
 'polynomial_example':{'f_N':'(1+z^N)/2','target':'max(0,log|z|)','zero_plot_degree':13,
 'exact_zero_angles':'(2k+1)*pi/13, k=0,...,12','highlighted_fixed_zero':[-1,0],
 'error_plot_disk_radius':2,'exact_L1_error':'pi*R^2*log(2)/N','N_degrees':[1,64],
 'quadrature_points':[x['N'] for x in samples],'pointwise_convergence_claimed_at_minus_one':False},
 'proof_locators':['GD7–GD9','GD11'],'human_source':'Hörmander II, Theorem 15.1.6 and Lemmas 15.1.7–15.1.8, pp. 277–278'}
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))

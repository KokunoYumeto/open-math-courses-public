"""Reproduce the exact one-dimensional whole-positive-head Legendre sample."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'GL-DMOD-LN-full-Legendre-v1'})
c=F(1,4);inputs=list(range(13));outputs=list(range(-6,7));rows=[]
values=np.full((len(outputs),len(inputs)),np.nan)
for row,j in enumerate(outputs):
    for col,m in enumerate(inputs):
        K=m-j
        exact=c**K*factorial(K)/factorial(m)**2 if K>=0 else None
        if exact is not None:values[row,col]=float(exact)
        rows.append({'input_degree':m,'output_degree':j,'loss':K,'contribution':str(exact) if exact is not None else None})
enclosures=[]
for j in range(-5,6):
    R=40
    lower=sum((c**K*factorial(K)/factorial(j+K)**2 for K in range(max(0,-j),R+1)),F(0))
    nextterm=c**(R+1)*factorial(R+1)/factorial(j+R+1)**2
    enclosures.append({'j':j,'cutoff':R,'lower':str(lower),'upper':str(lower+2*nextterm),'next_term':str(nextterm)})

ink,blue,green,muted='#152640','#155ca5','#17765d','#52627a'
fig=plt.figure(figsize=(16,10),facecolor='#f5f8fc')
fig.text(.5,.967,'The full Legendre map reaches every negative output degree',ha='center',va='top',fontsize=25,color=ink)
fig.text(.5,.909,r'Exact example: $p_m=[(m!)^2(1-y/2)(1+w/2)]^{-1}$ for every $m\geq0$; no negative input',ha='center',fontsize=17,color=muted)
left=fig.add_axes([.07,.345,.43,.49])
cmap=plt.get_cmap('viridis').copy();cmap.set_bad('#dde2ea')
finite=values[np.isfinite(values)]
im=left.imshow(values,origin='lower',aspect='auto',extent=[-.5,12.5,-6.5,6.5],cmap=cmap,
               norm=LogNorm(vmin=finite.min(),vmax=finite.max()),interpolation='nearest')
left.set_xticks(range(0,13,2));left.set_yticks(range(-6,7,2))
left.set_xlabel(r'Input degree $m$ (the whole input continues to infinity)',labelpad=8)
left.set_ylabel(r'Output degree $j$')
left.axhline(-.5,color='white',lw=1.6)
left.set_title(r'Individual exact contributions: loss $K=m-j\geq0$',fontsize=15,pad=12)
bar=fig.colorbar(im,cax=fig.add_axes([.515,.345,.015,.49]))
bar.ax.tick_params(labelsize=11);bar.set_label('Positive contribution (logarithmic scale)',fontsize=12,labelpad=8)
right=fig.add_axes([.665,.345,.29,.49])
for data in enclosures:
    low=float(F(data['lower']));high=float(F(data['upper']))
    right.errorbar(data['j'],low,yerr=[[0],[max(0,high-low)]],fmt='o',ms=7,
                   color=green if data['j']<0 else blue,capsize=5,elinewidth=1.5)
right.set_yscale('log');right.set_xticks(range(-5,6));right.set_xlabel(r'Output degree $j$',labelpad=8)
right.set_ylabel(r'Complete coefficient $q_j(0)$')
right.set_title(r'Exact rational enclosures, $R=40$',fontsize=15,pad=12)
right.grid(True,alpha=.2)
right.text(.04,.12,'Green: negative output degrees.\nEvery coefficient is strictly positive.\nIntervals are smaller than the markers.',transform=right.transAxes,fontsize=11.5,color=green,linespacing=1.5)
fig.text(.07,.244,r'$q_j(0)=\sum_{K\geq\max(0,-j)}\frac{(1/4)^K K!}{((j+K)!)^2}$',fontsize=23,color=blue)
fig.text(.07,.178,r'$S_{j,R}<q_j(0)\leq S_{j,R}+2b_{j,R+1}$',fontsize=21,color=green)
fig.text(.60,.200,'The whole analytic map has one common domain and',fontsize=14,color=ink)
fig.text(.60,.151,r'$\|A_Kp_m\|\leq L^K K!\,\|p_m\|$',fontsize=23,color=blue)
fig.text(.60,.103,'with a constant independent of the input degree m.',fontsize=14,color=ink)
fig.text(.07,.103,r'Ordered inverse: $t\mapsto s+(E_y+d-a)\sigma^{-1}$',fontsize=18,color=ink)
fig.text(.5,.036,'Bounds and tails: LN.14–LN.18. Algebra, inverse and exact sample: LN.24 and LN.30–LN.36. The real-kernel extension is separate.',ha='center',fontsize=10.5,color=muted)
stem='full-legendre-normal-transport'
fig.savefig(out/(stem+'.png'),dpi=150,metadata={'Software':'Open mathematics course figures'})
fig.savefig(out/(stem+'.svg'),metadata={'Date':None,'Creator':'Open mathematics course figures'})
plt.close(fig)
data={'scope':'One-dimensional full positive input LN.32, at t=x=z=0; no negative input coefficients.',
      'c':str(c),'input_degrees_shown':inputs,'output_degrees_shown':outputs,
      'whole_input_has_no_upper_degree_cutoff':True,'matrix_exact_contributions':rows,
      'coefficient_enclosures':enclosures,'proof_locators':['LN.14–LN.18','LN.24','LN.30–LN.36'],
      'only_logarithms_and_plotting_coordinates_numerical':True,'whole_real_kernel_transform_asserted':False}
(out/(stem+'-exact-data.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':3,'matrix_contributions':len(rows),'exact_coefficient_enclosures':len(enclosures),'png_size':[2400,1500]}))

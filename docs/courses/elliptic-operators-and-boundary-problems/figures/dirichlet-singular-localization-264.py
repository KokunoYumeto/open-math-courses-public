"""Numerical sections of the fully proved S26-19--S26-25, with actual domains."""
from pathlib import Path
import math
import argparse
import numpy as np
from scipy.special import sici
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
T=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description='Render the exact S26 singular localization figure.')
parser.add_argument('--output-dir',type=Path,default=T)
args=parser.parse_args()
out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'text.usetex':False,'font.family':'DejaVu Sans','font.size':11,
                     'svg.hashsalt':'AN03-U026-S26-264'})
def density(x,cutoff):
    x=np.asarray(x,dtype=float);a=math.sqrt(cutoff);t=2*a*x
    if a==0:return np.zeros_like(x)
    f=np.zeros_like(t);small=np.abs(t)<.02
    for k in range(1,9):f[small]+=(-1)**(k+1)*t[small]**(2*k-2)/math.factorial(2*k+1)
    f[~small]=(1-np.sinc(t[~small]/np.pi))/t[~small]**2
    return 4*a**3*f/np.pi
def window(length,cutoff):
    length=np.asarray(length,dtype=float);a=math.sqrt(cutoff);t=2*a*length
    if a==0:return np.zeros_like(length)
    val=np.zeros_like(t);small=np.abs(t)<.02
    for k in range(1,9):val[small]+=(-1)**(k+1)*t[small]**(2*k-1)/(math.factorial(2*k+1)*(2*k-1))
    u=t[~small]
    val[~small]=sici(u)[0]/2+(np.cos(u)-2)/(2*u)+np.sin(u)/(2*u**2)
    return 2*a*a*val/np.pi
fig=plt.figure(figsize=(14,9),facecolor='#fffdf8')
gs=fig.add_gridspec(2,2,left=.08,right=.96,bottom=.15,top=.78,hspace=.40,wspace=.27,
                       height_ratios=[.52,1])
maps=fig.add_subplot(gs[0,:]);maps.axis('off')
box={'facecolor':'#edf3f3','edgecolor':'#7195a4','boxstyle':'round,pad=.7'}
maps.text(.02,.68,'Original H = L²((0, ∞), 2 dx)\nχ(x) = 1/x; Eλ retains the closed cutoff',
          va='center',fontsize=12,bbox=box)
maps.text(.52,.68,'Rχ = Mχ Eλ is defined on all H\nHilbert–Schmidt: ||Rχ||₂² = λ/2',
          va='center',fontsize=12,bbox=box)
maps.annotate('',xy=(.49,.68),xytext=(.43,.68),arrowprops={'arrowstyle':'->','lw':2,'color':'#225e7b'})
maps.text(.02,.02,'Initial Mχ Eλ Mχ: domain D(Mχ)\nD(Mχ) = {f : ∫ |f(x)|² 2 dx / x² < ∞}',
          va='center',fontsize=12,bbox=box)
maps.text(.52,.02,'Its closure is Rχ Rχ* on all H\nPositive trace and trace norm = λ/2',
          va='center',fontsize=12,bbox=box)
maps.annotate('exact graph closure',xy=(.49,.02),xytext=(.43,.02),
              arrowprops={'arrowstyle':'->','lw':2,'color':'#225e7b'},fontsize=9,ha='center',va='bottom')
axq=fig.add_subplot(gs[1,0]);axt=fig.add_subplot(gs[1,1]);x=np.linspace(0,8,2401)
for lam,color in [(1,'#225e7b'),(4,'#ab5732')]:
    axq.plot(x,density(x,lam),color=color,lw=2.2,label=f'λ = {lam}; q(0) = 2 λ^(3/2) / (3π)')
    axt.plot(x,window(x,lam),color=color,lw=2.2,label=f'λ = {lam}')
    axt.axhline(lam/2,color=color,lw=1.2,ls='--',label=f'exact whole trace = {lam}/2')
for ax in (axq,axt):
    ax.set_facecolor('#fffdf8');ax.spines[['top','right']].set_visible(False);ax.set_xlim(0,8)
    ax.legend(frameon=False,fontsize=9,loc='best')
axq.set_title('The full reflected diagonal cancels the wall singularity',fontsize=12)
axq.set_xlabel('original physical coordinate x')
axq.set_ylabel('qλ(x) = |χ(x)|² e(x,x,λ) × 2')
axt.set_title('Finite singular trace on an infinite-rank projector',fontsize=12)
axt.set_xlabel('original physical window length L')
axt.set_ylabel('∫ from 0 to L of qλ(x) dx')
fig.text(.5,.94,'A singular physical weight has an exact spectral localization space',ha='center',
         fontsize=20,weight='bold',color='#173750')
fig.text(.5,.875,'Original A = −d²/dx², x > 0; domain H² ∩ H₀¹; density r₀ = 2; a = √λ',
         ha='center',fontsize=13,color='#315f78')
fig.text(.5,.825,'e(x,x,λ) = [a − sin(2ax)/(2x)] / (2π); qλ(x) = [a − sin(2ax)/(2x)] / (πx²)',
         ha='center',fontsize=12,color='#315f78')
fig.text(.5,.085,'S26-1–S26-25: exact maps and numerical samples of the proved one-dimensional formulas.',
         ha='center',fontsize=11,color='#405163')
fig.text(.5,.045,'The original kernel factor 1/2 multiplies the original measure 2 dx. λ = 0 gives zero; all wall limits are retained.',
         ha='center',fontsize=10.4,color='#405163')
for suffix in ('png','svg'):
    meta={'Software':'AN03-U026-S26-264'} if suffix=='png' else {'Date':None}
    fig.savefig(out/f'dirichlet-singular-localization-264.{suffix}',dpi=170,metadata=meta,facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered the exact singular localization section.')

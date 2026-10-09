"""Exact radial geometry and cutoff functions for NS-FLUID-13."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
LAMBDA=2.;M=4;R=16.;A=LAMBDA**(-M+2)*R;B=LAMBDA**(M-2)*R
H=1.;D0=2.;D=A/8;RMINUS=2*A+D0+H;RPLUS=B/2-D0-H
assert A==4 and B==64 and (RMINUS,RPLUS,D)==(11,29,.5)
assert B>=16*A and max(H,D0)<=A and 6*D<RPLUS-RMINUS

def bump(s):
    s=np.asarray(s,dtype=float);out=np.zeros_like(s);mask=s>0
    out[mask]=np.exp(-1/s[mask]);return out

def theta(s):
    q=np.asarray(s)**2;a=bump(1-q);b=bump(q-.25)
    return a/(a+b)

def transition(s):
    s=np.asarray(s);out=np.zeros_like(s,dtype=float)
    mask=(s>0)&(s<1);out[mask]=1-theta((s[mask]+1)/2)
    out[s>=1]=1;return out

def cutoff(r,k):
    return transition((r-RMINUS-2*k*D)/D)*transition((RPLUS-2*k*D-r)/D)

plt.rcParams.update({'font.size':11,'axes.titlesize':13,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(2,1,figsize=(12,7.8),layout='constrained',gridspec_kw={'height_ratios':[1,1.3]})
colors=['#cce4f6','#82b7dc','#246794']
ax=axs[0]
for k,(lo,hi,label) in enumerate([(1,256,'Initial shell S₀'),(2,128,'Heat-data shell S₁'),(4,64,'Receiving shell S₂')]):
    y=3-k
    ax.plot([lo,hi],[y,y],lw=14,color=colors[k],solid_capstyle='butt')
    ax.text(lo,y+.22,f'{lo:g}',ha='center');ax.text(hi,y+.22,f'{hi:g}',ha='center')
    ax.text(np.sqrt(lo*hi),y,label,ha='center',va='center',color='white' if k==2 else '#16394e')
ax.set_xscale('log',base=2);ax.set_xlim(.8,320);ax.set_ylim(.55,3.65)
ax.set_yticks([]);ax.set_xticks([1,2,4,8,16,32,64,128,256],labels=['1','2','4','8','16','32','64','128','256'])
ax.set_xlabel('Original radius r = |x| (logarithmic axis)')
ax.set_title('Nested original shells: Λ = 2, m = 4, R = 16',loc='left')
ax.grid(axis='x',alpha=.15)

ax=axs[1];r=np.linspace(10,30,6001)
ax.axvspan(RMINUS,RPLUS,color='#e9f3ec',label='Fixed common plateau Ω₀')
ax.axvspan(RMINUS+3*D,RPLUS-3*D,color='#cee6d3',label='Velocity region Ω₂')
ax.plot(r,cutoff(r,0),lw=2.6,color='#175b90',label='ζ₀')
ax.plot(r,cutoff(r,1),lw=2.4,color='#b04a23',label='ζ₁')
for x,label in [(RMINUS,'r₋ = 11'),(RMINUS+3*D,'12.5'),(RPLUS-3*D,'27.5'),(RPLUS,'r₊ = 29')]:
    ax.axvline(x,color='#666666',ls=':',lw=.8);ax.text(x,1.09,label,ha='center',fontsize=10)
ax.set_ylim(-.04,1.23);ax.set_xlim(10,30);ax.set_yticks([0,.5,1])
ax.set_xlabel('Original radius r = |x| (linear axis)');ax.set_ylabel('Cutoff value')
ax.set_title('Exact cutoffs: h = 1, D₀ = 2, d = A/8 = 0.5',loc='left')
ax.legend(loc='lower center',ncol=4,fontsize=10,framealpha=.95)
fig.suptitle('A selected annulus and the fixed region receiving its energy',fontsize=16)
for suffix in ['png','svg']:fig.savefig(ROOT/f'annulus-selection-and-local-cutoffs.{suffix}',dpi=170)
print({'parameters':{'Lambda':LAMBDA,'m':M,'R':R,'A':A,'B':B,'h':H,'D0':D0,'d':D},'figure':'annulus-selection-and-local-cutoffs.png'})

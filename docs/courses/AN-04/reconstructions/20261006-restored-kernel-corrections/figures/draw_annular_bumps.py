"""Reproduce the explicit four-piece frequency illustration in KCA2."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
def eta(v):
 a=np.asarray(v,dtype=float);out=np.zeros_like(a);mask=a>0
 out[mask]=np.exp(-1/a[mask]);return out
def step(v):
 return eta(v)/(eta(v)+eta(1-np.asarray(v)))
def bump(v):
 v=np.asarray(v)
 return step(8*(v-9/8))*step(8*(15/8-v))
if __name__=='__main__':
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path'})
 fig,ax=plt.subplots(figsize=(8.6,4.6))
 colors=['#17698c','#147d67','#9b592e','#6b52a3']
 for j,color in zip(range(1,5),colors):
  v=np.linspace(1,2,1501);x=j+np.log(v)/np.log(4)
  ax.plot(x,bump(v),color=color,lw=2.1,label=f'j = {j}')
  center=j+np.log(1.5)/np.log(4)
  ax.scatter([center],[1],c=[color],s=34,zorder=5)
  ax.annotate(f'j = {j}',(center,1),xytext=(0,13),textcoords='offset points',ha='center',color=color)
  for end in [9/8,15/8]:
   ax.scatter([j+np.log(end)/np.log(4)],[0],s=19,facecolors=color,edgecolors=color,zorder=4)
 ax.set_xlim(.92,4.65);ax.set_ylim(-.09,1.3)
 ax.set_yticks([0,.5,1]);ax.set_xticks([1,2,3,4])
 ax.set_xlabel('Logarithmic frequency  log₄ ξ   (ξ > 0)')
 ax.set_ylabel('Symbol value  bⱼ(ξ)')
 ax.set_title('Smooth pieces with height-one frequencies escaping to infinity',pad=22,fontsize=13)
 ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
 fig.text(.5,.045,'Marked points: ξⱼ = (3/2)4ʲ,  b(ξⱼ) = 1.  The infinite sequence continues.\nSampled curves; exact support endpoints and values. Proof: Exercise 2, (KC16)–(KC17), (KCA2).',
  ha='center',va='bottom',fontsize=10)
 fig.subplots_adjust(left=.095,right=.98,top=.81,bottom=.25)
 fig.savefig(HERE/'annular-bumps.svg',metadata={'Date':None})
 fig.savefig(HERE/'annular-bumps.png',dpi=160)
 print('Wrote explicit annular-bump SVG and PNG.')

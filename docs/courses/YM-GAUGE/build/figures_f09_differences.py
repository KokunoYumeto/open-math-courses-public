"""Exact heat-datum and energy-root examples, with original physical units."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
C=Path(__file__).resolve().parents[1]
def save(fig,stem):
 for ext in ('svg','png'):
  fig.savefig(C/'figures'/(stem+'.'+ext),dpi=170,
   metadata={'Date':None} if ext=='svg' else {'Software':'YM-GAUGE reproducible figure'})
 plt.close(fig)
def build():
 plt.rcParams.update({'svg.hashsalt':'YM-GAUGE-F09-differences','svg.fonttype':'none','font.size':11,
  'axes.spines.top':False,'axes.spines.right':False})
 ell=2.;kappa=1.;x=np.linspace(-6,6,601)
 fig,ax=plt.subplots(1,2,figsize=(12.5,5.6),layout='constrained')
 for heat,color in [(0.,'#153e60'),(.5,'#32759a'),(2.,'#978236'),(4.,'#ac4c32')]:
  val=kappa*(ell**2/(ell**2+4*heat))**2.5*x*np.exp(-x*x/(ell**2+4*heat))
  ax[0].plot(x,val,color=color,label=f's = {heat:g} m²')
 ax[0].set(xlabel='Original coordinate x₁ (m); x₂ = x₃ = 0',
  ylabel='Coefficient of T (m⁻¹ s⁻¹)',title='The original odd matrix datum')
 ax[0].axhline(0,color='#adb6bf',lw=.7);ax[0].legend()
 heat=np.linspace(0,4,601)
 mag=2*np.sqrt(2)*kappa*ell**4*np.sqrt(heat)/(np.sqrt(np.pi)*(ell**2+4*heat)**2)
 ax[1].plot(heat,mag,color='#ac4c32',label='Heat convolution of |f| at x = 0')
 ax[1].plot(heat,np.zeros_like(heat),color='#153e60',label='|Heat convolution of f| at x = 0')
 ax[1].set(xlabel='Original heat time s (m²)',ylabel='Full matrix magnitude (m⁻¹ s⁻¹)',
  title='Taking the magnitude loses cancellation')
 ax[1].legend(fontsize=9,loc='upper right')
 fig.suptitle('Electric difference datum: ℓ = 2 m, κ = 1 m⁻² s⁻¹, T = diag(i, −i)',fontsize=14)
 for a in ax:a.grid(alpha=.16)
 save(fig,'f09-electric-difference')
 fig,ax=plt.subplots(figsize=(10,5.8),layout='constrained')
 remainder=np.linspace(0,4,500)
 for flux,color in [(0.,'#153e60'),(1.,'#978236'),(2.,'#ac4c32')]:
  ax.plot(remainder,remainder+np.sqrt(remainder**2+flux**2),color=color,lw=2,
   label=f'F* = {flux:g} u')
 ax.scatter([1],[1+np.sqrt(5)],color='#ac4c32',zorder=4)
 ax.annotate('(R*, Y) = (u, (1 + √5)u)',xy=(1,1+np.sqrt(5)),xytext=(1.55,2.0),
  arrowprops={'arrowstyle':'->','color':'#526779'})
 ax.set(xlabel='Remainder norm R* (u)',ylabel='Upper energy root Y (u)',
  title='TD.18: Y² ≤ F*² + 2R*Y gives Y ≤ R* + √(R*² + F*²)')
 ax.legend();ax.grid(alpha=.17)
 fig.suptitle('u = 1 m⁻¹ᐟ² s⁻¹ᐟ²; exact scalar bounds, with no sampled connection',fontsize=12)
 save(fig,'f09-temporal-difference')
if __name__=='__main__':build()

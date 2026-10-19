"""Actual physical return density and bounded-increment diagnostic. CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
P=Path(__file__).resolve().with_suffix('')
fig=plt.figure(figsize=(12,9.4),facecolor='#fafcff')
ax=fig.add_axes([.04,.47,.92,.49]);ax.set_xlim(0,12);ax.set_ylim(0,6);ax.axis('off')
ink='#182a3a';blue='#164b7a';green='#126856'
ax.text(6,5.75,'Physical return densities and the central limit',ha='center',fontsize=19,weight='bold',color=ink)
ax.text(6,5.24,'Actual finite-index tower: PH.12–PH.14',ha='center',fontsize=12,color=ink)
for x,label in zip([1.4,4.4,7.4,10.4],['U = D₋₁','D₀','D₁','Dₗ']):
 ax.add_patch(FancyBboxPatch((x-.95,4.1),1.9,.65,boxstyle='round,pad=.08',facecolor='white',edgecolor=blue,lw=1.5));ax.text(x,4.42,label,ha='center',va='center',fontsize=15,color=blue)
for x,y in [(2.47,3.35),(5.47,6.35),(8.47,9.35)]:
 ax.annotate('',xy=(x,4.43),xytext=(y,4.43),arrowprops=dict(arrowstyle='->',lw=1.6,color=blue))
ax.text(6,3.66,'Φₗ : Dₗ → U normal;    τ(Φₗ(x)) = τ(Kₗ x)',ha='center',fontsize=13,color=ink)
ax.text(6,3.15,'Kₗ = k₀ ··· kₗ,    τ(Kₗ) = 1,    Eᴰₗ₋₁τ(Kₗ) = Kₗ₋₁',ha='center',fontsize=13,color=ink)
ax.text(6,2.63,'Kₗ → h almost everywhere,    h ∈ Z(U),    0 ≤ h ≤ 1',ha='center',fontsize=13,color=green)
ax.text(6,2.12,'Normal minorant:    h Eᵁτ(x) ≤ Eᴺτ(x)   for x ≥ 0',ha='center',fontsize=13,color=green)
ax.text(6,1.61,'On an atom zᵢ:    pᵢ = τ(zᵢ),    hzᵢ = aᵢzᵢ,    0 < aᵢ ≤ pᵢ',ha='center',fontsize=12,color=ink)
ax.text(6,1.09,'[Uzᵢ : Nzᵢ] ≤ pᵢ/aᵢ,    τ(h) ≤ Σᵢ pᵢ²',ha='center',fontsize=13,color=ink)
ax.text(6,.57,'Exact distance:    lim ‖Kₗ − 1‖₁ = 2(1 − τ(h))',ha='center',fontsize=13,color=blue)
b=fig.add_axes([.11,.10,.78,.27],facecolor='white')
n=np.arange(1,81);q=(np.sqrt(.5)+np.sqrt(1.5))/2
b.plot(n,np.ones_like(n),label=r'$E L_l=1$',color=blue,lw=2)
b.plot(n,q**n,label=r'$E\sqrt{L_l}=q^{l+1}$',color='#b23c41',lw=2)
b.set_xlim(1,80);b.set_ylim(0,1.1);b.set_xlabel('Number of independent increments l + 1');b.set_ylabel('Exact scalar moment');b.grid(alpha=.2);b.legend(loc='upper right',frameon=True,facecolor='white',framealpha=.95)
fig.text(.5,.415,'Probability-algebra diagnostic: equiprobable increments 1/2 and 3/2',ha='center',fontsize=12,color=ink,weight='bold')
fig.text(.5,.035,r'$q=(\sqrt{1/2}+\sqrt{3/2})/2<1$;  Exercise PH.7 proves mass loss.  This is not a Jones-tower counterexample.',ha='center',fontsize=11,color=ink)
fig.savefig(P.with_suffix('.png'),dpi=160,facecolor=fig.get_facecolor())
fig.savefig(P.with_suffix('.svg'),facecolor=fig.get_facecolor());plt.close(fig)
svg=P.with_suffix('.svg');svg.write_bytes(b'\n'.join(x.rstrip() for x in svg.read_bytes().splitlines())+b'\n')

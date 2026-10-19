"""Actual commutant expected tower, PH.26--PH.35. CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().with_suffix('')
fig,ax=plt.subplots(figsize=(12,7.7));fig.patch.set_facecolor('#fafcff');ax.set_facecolor('#fafcff')
ax.set_xlim(0,12);ax.set_ylim(0,8);ax.axis('off')
blue='#164b7a';green='#126856';ink='#182a3a'
ax.text(6,7.65,'One physical algebra T, two actual towers',ha='center',fontsize=20,color=ink,weight='bold')
ax.text(6,7.17,'Finite index; arbitrary centers; original cup e = eⱼ',ha='center',fontsize=12,color=ink)
xs=[2,6,10]
def box(x,y,title,sub,color):
 ax.add_patch(FancyBboxPatch((x-1.65,y-.43),3.3,.86,boxstyle='round,pad=0.08',facecolor='white',edgecolor=color,lw=1.5))
 ax.text(x,y+.11,title,ha='center',va='center',fontsize=15,color=color)
 ax.text(x,y-.20,sub,ha='center',va='center',fontsize=10,color=ink)
for x,title,sub in zip(xs,['C = Bⱼ₊₁','B = Bⱼ','A = Bⱼ₋₁'],['Mⱼ₊₁′ ∩ T','Mⱼ′ ∩ T','Mⱼ₋₁′ ∩ T']):box(x,6.25,title,sub,blue)
for x,title,sub in zip(xs,['W = Dⱼ₊₁','V = Dⱼ','U = Dⱼ₋₁'],['C′ ∩ T','B′ ∩ T','A′ ∩ T']):box(x,4.45,title,sub,green)
for y,col,reverse in [(6.25,blue,False),(4.45,green,True)]:
 for a,b in zip(xs[:-1],xs[1:]):
  start,end=(a+1.78,b-1.78) if not reverse else (b-1.78,a+1.78)
  ax.annotate('',xy=(end,y),xytext=(start,y),arrowprops=dict(arrowstyle='->',color=col,lw=1.8))
for x in xs:
 ax.annotate('',xy=(x,4.98),xytext=(x,5.74),arrowprops=dict(arrowstyle='->',color='#68798a',lw=1.2))
 ax.text(x+.17,5.35,'commutant in T',fontsize=9,color='#46586b',va='center')
ax.text(6,3.73,'Mⱼ₊₁ ⊂ W       Mⱼ ⊂ V       Mⱼ₋₁ ⊂ U',ha='center',fontsize=12,color=green)
ax.text(6,3.23,'Full corner:  eAe = Ce,   Σᵣ vᵣ e vᵣ* = 1,   vᵣ ∈ B',ha='center',fontsize=13,color=ink)
ax.text(6,2.75,'θ : U → (Ce)′ ∩ eTe,    θ(u) = ue,    θ⁻¹(y) = Σᵣ vᵣ y vᵣ*',ha='center',fontsize=12,color=ink)
ax.text(6,2.28,'Normal faithful expectation  ℰⱼ : V → U,    exe = ℰⱼ(x)e',ha='center',fontsize=13,color=green)
ax.text(6,1.80,'Original supported basis:  x = Σᵢ aᵢ ℰⱼ(aᵢ*x),    Σᵢ aᵢaᵢ* = d1',ha='center',fontsize=12,color=ink)
ax.add_patch(FancyBboxPatch((.65,.32),10.7,1.04,boxstyle='round,pad=0.08',facecolor='#edf5ff',edgecolor=blue,lw=1))
ax.text(6,1.08,'Physical trace correction (PH.33–PH.35)',ha='center',fontsize=12,color=blue,weight='bold')
ax.text(6,.70,'c = Eᵁτ(e),   t = Eⱽτ(e),   k = c⁻¹t,   L⁻¹1 ≤ k ≤ L1',ha='center',fontsize=12,color=ink)
ax.text(6,.36,'Eᵁτ(x) = ℰⱼ(k⁻¹ᐟ² x k⁻¹ᐟ²),    L = Σᵣ ‖vᵣ‖²',ha='center',fontsize=12,color=ink)
fig.subplots_adjust(left=.01,right=.99,bottom=.02,top=.99)
fig.savefig(P.with_suffix('.png'),dpi=160,facecolor=fig.get_facecolor())
fig.savefig(P.with_suffix('.svg'),facecolor=fig.get_facecolor())
plt.close(fig)

# SVG path whitespace has no geometric meaning; keep the editable output tidy.
svg=P.with_suffix('.svg')
svg.write_bytes(b'\n'.join(line.rstrip() for line in svg.read_bytes().splitlines())+b'\n')

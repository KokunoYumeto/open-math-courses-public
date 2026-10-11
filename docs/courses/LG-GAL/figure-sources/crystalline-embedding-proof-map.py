"""Reproduce the two completion mechanisms and the separate Frobenius proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root = Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14})
fig,ax = plt.subplots(figsize=(5,12),dpi=180)
ax.set(xlim=(0,5),ylim=(0,12)); ax.axis('off')
ax.text(2.5,11.65,'Crystalline embedding',ha='center',fontsize=21,weight='bold')
ax.text(2.5,11.25,'Every prime p, including p = 2',ha='center',fontsize=12)
boxes = [
 (10.25,'Restricted divided-power series P',r'$a_n\in A_{\rm inf},\quad a_n\to0$ p-adically','Presentation and exact completion; CE4–CE10','#edf4ff'),
 (8.62,r'$S=P/(T-\xi)P=A_{\rm cris}$','Uniform coefficient p-adic topology','No unique series coefficients assumed','#edf4ff'),
 (6.99,r'$E_m=(A_{\rm inf}/\xi^m)[1/p]$',r'Complete lattices $p^r(A_{\rm inf}/\xi^m)$','Fixed quotient bound CE12','#edf8ef'),
 (5.36,r'$B_{\rm dR}^{+}=\lim_{\leftarrow m} E_m$','Compatible maps into each quotient','Series and logarithm compatibility; CE13, CE17–CE20','#edf8ef'),
 (3.35,'Injectivity of j: S to '+r'$B_{\rm dR}^{+}$','Normalize coefficients; detect first nonzero residue','Factorial bound CE16 keeps coefficients restricted','#fff4dc'),
 (1.42,'Injectivity of Frobenius on S','Recover the original zero-series relation','Separate factorial reset at '+r'$p^N$'+'; CE22–CE27','#fff4dc'),
]
for y,title,body,locator,colour in boxes:
 ax.add_patch(FancyBboxPatch((.22,y-.62),4.56,1.24,boxstyle='round,pad=.09',facecolor=colour,edgecolor='#27445f',linewidth=1.3))
 ax.text(2.5,y+.33,title,ha='center',va='center',fontsize=14)
 ax.text(2.5,y-.03,body,ha='center',va='center',fontsize=12)
 ax.text(2.5,y-.43,locator,ha='center',fontsize=9,color='#37516a')
for upper,lower in zip([10.25,8.62,6.99],[8.62,6.99,5.36]):
 ax.add_patch(FancyArrowPatch((2.5,upper-.74),(2.5,lower+.74),arrowstyle='-|>',mutation_scale=17,color='#27445f',linewidth=1.4))
ax.text(2.5,4.3,'Two separate proofs from the series presentation',ha='center',fontsize=11,weight='bold')
ax.text(2.5,.36,'No Frobenius on the de Rham ring is asserted.\nRestriction of the equivariant maps gives every finite K.',ha='center',fontsize=10)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
target=root/'assets/crystalline-embedding-proof-map.png'
fig.savefig(target,facecolor='white',metadata={'Software':'Matplotlib'}); plt.close(fig)
with Image.open(target) as im: im.copy().save(target)

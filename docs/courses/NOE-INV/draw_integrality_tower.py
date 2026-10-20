"""Original schematic of the finite-group finiteness proof; requires matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out=Path(__file__).resolve().parent/'figures'
out.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(8.6,3.7),layout='constrained')
ax.set(xlim=(-.3,8.4),ylim=(-.8,3.1))
ax.axis('off')
for x,title,description in [
 (0,r'$C$','Orbit coefficients\nand the base ring'),
 (3,r'$B=A^G$','All invariants'),
 (6,r'$A$','The given algebra')]:
 ax.add_patch(FancyBboxPatch((x,1),2,1.0,boxstyle='round,pad=.12',
                            facecolor='#f1f6f8',edgecolor='#356277',lw=1.5))
 ax.text(x+1,1.74,title,ha='center',va='center',fontsize=17,color='#173c4d')
 ax.text(x+1,1.28,description,ha='center',va='center',fontsize=10)
for x in [2.15,5.15]:
 ax.annotate('',xy=(x+.7,1.52),xytext=(x,1.52),
             arrowprops={'arrowstyle':'->','lw':1.5,'color':'#356277'})
 ax.text(x+.35,1.87,'inclusion',ha='center',fontsize=9)
ax.add_patch(FancyArrowPatch((7,2.16),(1,2.16),connectionstyle='arc3,rad=.19',
             arrowstyle='->',mutation_scale=14,color='#ad401f',lw=1.8))
ax.text(4,2.86,r'$A$ is a finite $C$-module: monic orbit equations',
        ha='center',fontsize=11,color='#ad401f')
ax.add_patch(FancyArrowPatch((4,.84),(1,.84),connectionstyle='arc3,rad=-.25',
             arrowstyle='->',mutation_scale=14,color='#11794b',lw=1.8))
ax.text(2.5,.08,r'$B$ is a finite $C$-module: $C$ is Noetherian',
        ha='center',fontsize=11,color='#11794b')
ax.text(4,-.55,'All rings are over the Noetherian base R. Curved arrows indicate finiteness.',
        ha='center',fontsize=10,color='#4c565d')
fig.savefig(out/'integrality-tower.png',dpi=170,metadata={'Software':None})
fig.savefig(out/'integrality-tower.svg',metadata={'Date':None,'Creator':None})
plt.close(fig)

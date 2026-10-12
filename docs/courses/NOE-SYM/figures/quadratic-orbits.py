from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
root=Path(__file__).resolve().parent.parent
out=root/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':15,'svg.fonttype':'none','svg.hashsalt':'NOE-SYM-quadratic-orbits-v1'})
x=np.linspace(-1.7,1.7,401);X,Y=np.meshgrid(x,x)
fig,axes=plt.subplots(2,1,figsize=(4.8,8.5))
for ax,U,title,levels in [
 (axes[0],(X*X+Y*Y)/2,'Elliptic: det H = 1',[.25,.5,1,1.5,2]),
 (axes[1],(X*X-Y*Y)/2,'Hyperbolic: det H = −1',[-1,-.5,-.25,.25,.5,1])]:
 colors=['#24649a' if level<0 or ax is axes[0] else '#ad4434' for level in levels]
 contours=ax.contour(X,Y,U,levels=levels,colors=colors,linewidths=1.8)
 points=[]
 for level in levels:
  if ax is axes[0]:point=(np.sqrt(level),-np.sqrt(level))
  elif level>0:point=(np.sqrt(2*level+.25**2),.25)
  else:point=(.25,np.sqrt(-2*level+.25**2))
  points.append(point)
 ax.clabel(contours,inline=True,fontsize=11,fmt='%g',manual=points)
 ax.set_title(title);ax.set_aspect('equal');ax.set_xlabel('x₁');ax.set_ylabel('x₂');ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(out/'quadratic-orbits.svg',bbox_inches='tight',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Codex, Ultra; original CC0','Date':None})
fig.savefig(out/'quadratic-orbits.png',dpi=170,bbox_inches='tight',metadata={})
p=out/'quadratic-orbits.png';im=Image.open(p);im.save(p)


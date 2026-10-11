"""Original two-point geometry and the proved sharp angular ratio, HP6–HP8."""
from pathlib import Path
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt,json
R=Path(__file__).resolve().parent
radius=3.;eps=np.pi/12
z=radius*np.array([np.cos(eps),np.sin(eps)])
x=radius*np.sin(2*eps)*np.array([np.sin(eps),np.cos(eps)])
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
ax=axes[0];ax.plot([0,x[0]],[0,x[1]],color='#147968',label=r'$x_\varepsilon=R_0\sin(2\varepsilon)(\sin\varepsilon,\cos\varepsilon)$')
ax.plot([0,z[0]],[0,z[1]],color='#bc6224',label=r'$z_\varepsilon=R_0(\cos\varepsilon,\sin\varepsilon)$')
ax.plot([x[0],z[0]],[x[1],z[1]],color='#324f85',label=r'$|x_\varepsilon-z_\varepsilon|=R_0\cos(2\varepsilon)$')
ax.scatter([x[0],z[0]],[x[1],z[1]],color=['#147968','#bc6224']);ax.annotate(r'$x_\varepsilon$',x,xytext=(8,9),textcoords='offset points');ax.annotate(r'$z_\varepsilon$',z,xytext=(-15,-22),textcoords='offset points')
ax.set(xlim=(0,3.25),ylim=(0,2),xlabel='Original first coordinate',ylabel='Original second coordinate',title=r'Actual pair: $R_0=3$, $\varepsilon=\pi/12$');ax.set_aspect('equal');ax.grid(alpha=.2);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),fontsize=9,frameon=False)
angles=np.linspace(.0001,np.pi/4-.0001,500)
ax=axes[1]
for alpha,color in [(0.25,'#bc6224'),(.5,'#147968'),(1.,'#324f85')]:
 ax.plot(angles,np.cos(2*angles)**(1-alpha),label=rf'$\alpha={alpha:g}$',color=color)
ax.set(xlabel=r'Original angle $\varepsilon$',ylabel=r'$|q(x_\varepsilon)-q(z_\varepsilon)|\,|z_\varepsilon|^\alpha/|x_\varepsilon-z_\varepsilon|^\alpha$',title=r'Exact ratio $\cos(2\varepsilon)^{1-\alpha}$; proved upper bound $1$',ylim=(0,1.07),xlim=(0,np.pi/4));ax.set_xticks([0,np.pi/8,np.pi/4],['0',r'$\pi/8$',r'$\pi/4$']);ax.legend(frameon=False);ax.grid(alpha=.2)
fig.suptitle('Complete original two-point geometry; proofs HP5–HP8; Chen–Hou Part I v4, main2384–2499',fontsize=11)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-exact-two-point-weight.'+ext),dpi=180,bbox_inches='tight')
(R/'chen-hou-two-point-samples.json').write_text(json.dumps(dict(radius=radius,epsilon=eps,x=x.tolist(),z=z.tolist(),distance=float(np.linalg.norm(x-z)),scope='Numerical samples of exact HP8 formulas; the supremum is proved analytically'),indent=2)+'\n',encoding='utf-8')
plt.close(fig)

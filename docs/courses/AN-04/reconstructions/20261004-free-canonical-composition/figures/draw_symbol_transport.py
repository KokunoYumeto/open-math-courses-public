from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(12,8.4),facecolor='#f4f8fb')
grid=fig.add_gridspec(2,2,height_ratios=[1,.7],hspace=.37,wspace=.30)
ax=fig.add_subplot(grid[0,0]);ax.axis('off')
ax.text(0,1.08,'How a derivative changes order',fontsize=17,weight='bold',color='#172b3c')
rows=[(r'$\partial_x\;\to\;\partial_y a$',r'$\delta$'),
      (r'$\partial_x\;\to\;\partial_\eta a$',r'$1-\rho$'),
      (r'$\partial_\theta\;\to\;\partial_y a$',r'$\delta-1$'),
      (r'$\partial_\theta\;\to\;\partial_\eta a$',r'$-\rho$')]
for i,(label,cost) in enumerate(rows):
    y=.85-.17*i
    ax.text(.02,y,label,fontsize=18,color='#14546b')
    ax.text(.80,y,cost,fontsize=19,color='#a64d25')
ax.text(.02,.06,'Base budget: δ.  Frequency budget: −ρ.\nHigher derivatives obey the full count (H7).',fontsize=11,color='#425c6d')
bx=fig.add_subplot(grid[0,1]);bx.set_facecolor('white')
r=np.linspace(0,1,300)
bx.fill_between(r,1-r,1,color='#b9dfe3',alpha=.8,label='Fiber-preserving: ρ + δ ≥ 1')
bx.plot(r,1-r,color='#a64d25',lw=3,label='Arbitrary homogeneous map: ρ + δ = 1')
bx.set(xlim=(0,1),ylim=(0,1),xlabel='ρ',ylabel='δ',title='Guaranteed invariance ranges (H2)')
bx.text(.05,.10,'Below the line: Example H1 fails.\nAbove it: general mixing fails (H2 exercise).',fontsize=10,color='#425c6d')
bx.legend(loc='upper right',fontsize=9)
bx.spines[['top','right']].set_visible(False)
cx=fig.add_subplot(grid[1,:]);cx.axis('off')
cx.text(0,1.02,'Properness is a statement about the ray map',fontsize=17,weight='bold',color='#172b3c')
cx.text(.08,.67,r'$(r,s)\in(0,\infty)\times\Sigma_1$',fontsize=18,color='#14546b')
cx.text(.61,.67,r'$(r h(s),\psi(s))\in(0,\infty)\times\Sigma_2$',fontsize=18,color='#14546b')
cx.annotate('',xy=(.59,.70),xytext=(.48,.70),arrowprops={'arrowstyle':'->','lw':2,'color':'#a64d25'})
cx.text(.50,.79,r'$F$',fontsize=17,color='#a64d25')
cx.text(.08,.39,r'$F^{-1}(\{1\}\times K)=\{(1/h(s),s):\psi(s)\in K\}$',fontsize=19,color='#14546b')
cx.text(.08,.12,'F proper ⇔ ψ proper.  Compact normalized supports then have compact inverse images.\nFor submersions, homogeneous local sections give the left inverse R in (H11).',fontsize=12,color='#425c6d')
fig.text(.07,.018,'Exact statements: H2–H5. The diagram specifies map formulas, not an injectivity assumption.',fontsize=10,color='#425c6d')
fig.savefig(out/'symbol-transport.svg',bbox_inches='tight')
fig.savefig(out/'symbol-transport.png',dpi=130,bbox_inches='tight')
plt.close(fig)

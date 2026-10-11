"""Reproduce EX31–EX34 without identifying a scalar extremizer as a network."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13})
fig,ax=plt.subplots(1,2,figsize=(13.6,5.4),constrained_layout=True)
x=np.linspace(-2,1,301);y=np.linspace(0,2,201);X,Y=np.meshgrid(x,y)
F=3*(X+2)*(1-X)/2+2*Y*(2-Y)/2
c=ax[0].contourf(X,Y,F,levels=np.linspace(0,35/8,15),cmap='viridis')
fig.colorbar(c,ax=ax[0],label='Exact scalar value $F(z_1,z_2)$',shrink=.87)
ax[0].scatter([-2,-2,1,1],[0,2,0,2],s=38,c='white',edgecolors='black',zorder=4)
ax[0].scatter([-.5],[1],s=40,c='white',edgecolors='black',zorder=4)
ax[0].annotate('$F=35/8$ at the center',(-.5,1),xytext=(-1.65,1.5),color='white',arrowprops={'arrowstyle':'->','color':'white'})
ax[0].set(xlabel='$z_1$',ylabel='$z_2$',title='Scalar sharpness: all four corner values are zero',xticks=[-2,-.5,1],yticks=[0,1,2])
ax[0].text(.5,-.19,r'$F=\frac{3}{2}(z_1+2)(1-z_1)+(z_2)(2-z_2)$'+'\n'+r'$|F_{11}|=3$, $|F_{22}|=2$: error $(3\cdot3^2+2\cdot2^2)/8$',ha='center',va='top',transform=ax[0].transAxes)
lam=.5;L=1.;p=1+lam;B=8/np.sqrt(3);H=1+p*(1-np.tanh(L)**2+B*np.tanh(L))
Ks=B+p*(4/(3*np.sqrt(3))+16/np.sqrt(3)+(116/3)*np.tanh(L))
gap=np.linspace(0,1,501);cross=4*H/Ks
ax[1].plot(gap,H*gap/2,label=r'First derivative: $H\Delta_1/2$',lw=2.3,color='#286496')
ax[1].plot(gap,Ks*gap**2/8,label=r'Second derivative: $K_*\Delta_1^2/8$',lw=2.3,color='#b55620')
ax[1].axvline(cross,ls=':',color='#444444')
ax[1].annotate(r'$\Delta_1=4H/K_*$',(cross,H*cross/2),xytext=(.04,4.6),arrowprops={'arrowstyle':'->','color':'#444444'})
ax[1].set(xlabel=r'Actual first-coordinate gap $\Delta_1$',ylabel='Term added to the largest node residual',title=r'Specified six-layer network: $\lambda=1/2$, $L_1=1$',xlim=(0,1),ylim=(0,8.5))
ax[1].legend(loc='upper left',bbox_to_anchor=(0,.99));ax[1].grid(alpha=.18)
ax[1].text(.5,-.19,'EX19–EX23 and EX33–EX34; no trained weights used.\nCurves are proved upper bounds, not measured interpolation errors.',ha='center',va='top',transform=ax[1].transAxes)
for suffix in ['png','svg']:fig.savefig(R/('profile-grid-error.'+suffix),dpi=170,bbox_inches='tight')
plt.close(fig)
print({'figure':'profile-grid-error','lambda':lam,'L1':L,'H':H,'K_star':Ks,'crossing':cross,'scalar_center':'35/8'})

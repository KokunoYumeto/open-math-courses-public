from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
x=np.linspace(-.6,.6,1601)
for j,col in [(2,'#176b9e'),(4,'#c65a19'),(8,'#7541a1')]:
 s=j*x;y=np.zeros_like(s);inside=np.abs(s)<1
 y[inside]=np.exp(1-1/(1-s[inside]**2))
 axes[0].plot(x,y,label=fr'$j={j}$',color=col,lw=2)
axes[0].set(xlabel='$x$',ylabel='Unit-height spatial envelope',title=r'Radius $1/j$; coefficient $j^{-3r-2}$',ylim=(-.025,1.1))
axes[0].legend(loc='upper left');axes[0].grid(alpha=.15)
for j in range(2,7):
 center=j**3
 axes[1].plot([center-j,center+j],[j,j],color='#176b9e',lw=5,solid_capstyle='butt')
 axes[1].scatter([center],[j],color='#143750',s=28,zorder=3)
 axes[1].annotate(str(center),(center,j),xytext=(0,9),textcoords='offset points',ha='center',fontsize=10)
axes[1].set(xlabel=r'Frequency $\xi$',ylabel='Packet index $j$',title=r'Carrier $j^3$; frequency scale $j$',xlim=(-8,232),ylim=(1.5,6.7),yticks=range(2,7))
axes[1].text(.04,.92,'Bars mark a scale, not Fourier support.',transform=axes[1].transAxes,fontsize=10)
axes[1].grid(alpha=.15)
for ext in ['png','svg']:
 fig.savefig(out/('finite-regularity-wavefront-packets.'+ext),dpi=180)
p=out/'finite-regularity-wavefront-packets.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines()).rstrip()+'\n',encoding='utf-8')

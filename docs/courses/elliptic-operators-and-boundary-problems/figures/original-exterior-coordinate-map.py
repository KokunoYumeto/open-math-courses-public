"""Reproduce the full original exterior coordinate contours and measure."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
Ainf=np.array([[4.,2.],[0.,2.]])
As=(Ainf+Ainf.T)/2
Aa=(Ainf-Ainf.T)/2
eigen,axes=np.linalg.eigh(As)
M=(axes*np.sqrt(eigen))@axes.T
Minv=np.linalg.inv(M)
K=Minv@Aa@Minv.T
assert np.allclose(M@M,As)
assert np.allclose(Minv@Ainf@Minv.T,np.eye(2)+K)
assert np.allclose(np.linalg.det(M),np.sqrt(7))
assert np.allclose(K,np.array([[0,1/np.sqrt(7)],[-1/np.sqrt(7),0]]))
theta=np.linspace(0,2*np.pi,801)
circle=np.stack([np.cos(theta),np.sin(theta)])
fig,panels=plt.subplots(1,2,figsize=(12.2,8.6))
fig.subplots_adjust(top=.81,bottom=.35,wspace=.28)
colors=['#326b96','#ac4d28']
for ax in panels:
    ax.set_aspect('equal')
    ax.axhline(0,color='#999999',lw=.7)
    ax.axvline(0,color='#999999',lw=.7)
    ax.grid(alpha=.2)
for r,color in zip([1,2],colors):
    xy=r*circle
    original=M@xy
    panels[0].plot(xy[0],xy[1],color=color,lw=2.2,label=f'r = {r}')
    panels[1].plot(original[0],original[1],color=color,lw=2.2,label=f'r = {r}')
panels[0].set(xlim=(-2.65,2.65),ylim=(-2.65,2.65),xlabel=r'$y_1$',ylabel=r'$y_2$',title=r'Auxiliary coordinates: $r=|y|$')
panels[1].set(xlim=(-4.65,4.65),ylim=(-4.65,4.65),xlabel=r'$x_1$',ylabel=r'$x_2$',title=r'Original coordinates: $r=|M^{-1}x|$')
for ax in panels: ax.legend(loc='upper left',fontsize=10)
fig.suptitle('The exterior estimate returns to the full original operator',fontsize=19,y=.97)
fig.text(.5,.865,r'$x=My,\quad M=(A_\infty^s)^{1/2},\quad |\det M|=\sqrt{7},\quad \sigma=1$',ha='center',fontsize=16)
fig.text(.5,.29,'A∞ = [[4, 2], [0, 2]];   A∞ˢ = [[4, 1], [1, 2]]',ha='center',fontsize=15)
fig.text(.5,.235,r'$\widetilde a(\infty)=I+K_\infty,\quad (K_\infty)_{12}=1/\sqrt{7},\quad (K_\infty)_{21}=-1/\sqrt{7}$',ha='center',fontsize=14)
fig.text(.5,.175,r'$t=T-e^{-\eta T},\quad h=1+\eta e^{-\eta T},\quad dx=|\det M|\,h\,e^{nt}\,dT\,d\omega$',ha='center',fontsize=15)
fig.text(.5,.115,r'$QW=-\sigma h^2r^2(p-\lambda)w,\qquad \widetilde\lambda=\sigma\lambda>0$',ha='center',fontsize=16)
fig.text(.5,.045,'E2a and E8a prove the skew operator is zero. E3b–E3f and E77–E80 retain all maps and factors.\nThe contours are coordinate ellipsoids.',ha='center',fontsize=10.5)
fig.savefig(P/'original-exterior-coordinate-map.svg')
fig.savefig(P/'original-exterior-coordinate-map.png',dpi=160)

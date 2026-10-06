"""Reproduce the exact coordinate ellipsoid and retained skew matrix."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
A0=np.array([[4.,2.],[0.,2.]])
As=(A0+A0.T)/2
eigen,axes=np.linalg.eigh(As)
M=(axes*np.sqrt(eigen))@axes.T
theta=np.linspace(0,2*np.pi,601)
circle=np.stack([np.cos(theta),np.sin(theta)])
ellipse=M@circle
K=np.linalg.inv(M)@(A0-As)@np.linalg.inv(M).T
assert np.allclose(np.linalg.det(M),np.sqrt(7))
assert np.allclose(K,np.array([[0,1/np.sqrt(7)],[-1/np.sqrt(7),0]]))
fig,panels=plt.subplots(1,2,figsize=(11.8,7.8))
fig.subplots_adjust(top=.80,bottom=.31,wspace=.34)
for ax in panels:
 ax.set_aspect('equal');ax.axhline(0,color='#999999',lw=.7);ax.axvline(0,color='#999999',lw=.7)
 ax.grid(alpha=.2)
panels[0].plot(circle[0],circle[1],color='#2b6f89',lw=2.2)
panels[0].set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),xlabel=r'$y_1$',ylabel=r'$y_2$',title=r'Auxiliary sphere: $|y|=1$')
panels[1].plot(ellipse[0],ellipse[1],color='#934521',lw=2.2)
panels[1].set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),xlabel=r'$x_1$',ylabel=r'$x_2$',title=r'Original coordinates: $|M^{-1}x|=1$')
for j in range(2):
 panels[0].annotate('',xy=circle[:,150*j],xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#2b6f89',lw=1.5))
 panels[1].annotate('',xy=M[:,j],xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#934521',lw=1.5))
 panels[1].text(*(M[:,j]*1.07),r'$Me_'+str(j+1)+'$',fontsize=12)
fig.suptitle('The original matrix and every coordinate factor remain explicit',fontsize=19,y=.96)
fig.text(.50,.84,r'$x=My,\quad M=(A_0^s)^{1/2},\quad |\det M|=\sqrt{7}$',ha='center',fontsize=16)
fig.text(.50,.25,'A₀ = [[4, 2], [0, 2]];   A₀ˢ = [[4, 1], [1, 2]]',ha='center',fontsize=15)
fig.text(.50,.19,r'$\widetilde A(0)=I+K_0,\quad (K_0)_{12}=1/\sqrt{7},\quad (K_0)_{21}=-1/\sqrt{7}$',ha='center',fontsize=15)
fig.text(.50,.13,r'$dx=|\det M|\,s(T)\,e^{nt(T)}\,dT\,d\omega$',ha='center',fontsize=16)
fig.text(.50,.062,'PC1a proves the skew operator is zero; PC6 and PC52–PC55 retain all original data.\nThe drawing is a coordinate ellipsoid.',ha='center',fontsize=11)
fig.savefig(P/'original-point-coordinate-map.svg')
fig.savefig(P/'original-point-coordinate-map.png',dpi=160)

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OWN=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(15,8),layout='constrained')
grid=fig.add_gridspec(1,2,width_ratios=[1.12,1])
ax=fig.add_subplot(grid[0]);ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
blue='#155a86';red='#9d2736';green='#176d55'
ax.text(.03,.96,'The literal native class retains parity and line',fontsize=16,weight='bold',color=blue)
ax.text(.05,.86,r'$S=H_{\rm even}\oplus (LH)_{\rm odd}$',fontsize=19)
ax.text(.05,.77,r'$W=H^*_{\rm even}\oplus (L^*H^*)_{\rm odd}$',fontsize=19)
ax.text(.05,.67,r'$D=\det S=LH^2$',fontsize=19,color=green)
ax.text(.05,.57,r'$\Pi(W\otimes D)\ \rightarrow\ S\quad (J)$',fontsize=23,color=blue)
ax.text(.05,.485,r'$J(w_1\otimes d)=s_0,\qquad J(w_0\otimes d)=-i s_1$',fontsize=16)
ax.text(.05,.41,r'$J(-b_{W,1})=\varepsilon_1J,\qquad J(-b_{W,2})=\varepsilon_2J$',fontsize=16)
ax.text(.05,.345,'J is odd before the displayed parity reversal.',fontsize=13,color=red)
ax.text(.05,.245,r'$\delta_S=-\delta_{\rm inv}[D]$',fontsize=25,color=red)
ax.text(.05,.16,r'$T\delta_S=-[D]\quad\longrightarrow\quad -1\ {\rm at\ a\ point}$',fontsize=21,color=red)
ax.text(.05,.055,'Proof: Proposition 11.8. The analytical isomorphism\nquestion still requires the represented reverse product.',fontsize=12)

right=fig.add_subplot(grid[1]);right.set_aspect('equal');right.set_axis_off();right.set_xlim(-1.18,1.18);right.set_ylim(-1.63,1.45)
right.text(0,1.35,'A compact example with actual disk leaves',ha='center',fontsize=16,weight='bold',color=blue)
theta=np.linspace(0,2*np.pi,601);right.plot(np.cos(theta),np.sin(theta),color='#bbb',lw=1.5)
radius=2**(-.25);angles=np.arange(8)*np.pi/4;vertices=radius*np.exp(1j*angles)
labels=['a','b',r'$a^{-1}$',r'$b^{-1}$','c','d',r'$c^{-1}$',r'$d^{-1}$']
for i in range(8):
    t0=angles[i];t1=t0+np.pi/4;mid=(t0+t1)/2
    center=(1+radius**2)/(2*radius*np.cos(np.pi/8))*np.exp(1j*mid)
    cr=np.sqrt(abs(center)**2-1)
    p0=radius*np.exp(1j*t0);p1=radius*np.exp(1j*t1)
    phase0=np.angle(p0-center);phase1=np.angle(p1-center)
    delta=(phase1-phase0+np.pi)%(2*np.pi)-np.pi
    arc=center+cr*np.exp(1j*np.linspace(phase0,phase0+delta,90))
    right.plot(arc.real,arc.imag,color=blue,lw=2)
    label=.70*np.exp(1j*mid);right.text(label.real,label.imag,labels[i],ha='center',va='center',fontsize=15)
right.scatter(vertices.real,vertices.imag,color=blue,s=17)
right.text(0,.12,r'$[a,b][c,d]=1$',ha='center',fontsize=18)
right.text(0,-.09,r'$r_{\rm disk}=2^{-1/4}$',ha='center',fontsize=16)
right.text(0,-.28,r'Vertex angle $\pi/4$',ha='center',fontsize=14)
right.text(0,-1.12,r'$V=(\mathbb{H}^2\times SU(2))/\Gamma$',ha='center',fontsize=17,color=green)
right.text(0,-1.33,r'$\gamma(z,k)=(\gamma z,\rho(\gamma)k)$',ha='center',fontsize=16,color=green)
right.text(0,-1.53,'Faithful ρ ⇒ trivial leaf stabilizers. Proof: Lemma 11.9.',ha='center',fontsize=12)
fig.suptitle('Native radial / calibrated inverse: an exact graded comparison',fontsize=20,color=blue)
for ext in ['png','svg']:fig.savefig(OWN/f'kt-native-delta-interface.{ext}',dpi=170,metadata={'Creator':'NCG-FOLIATIONS mathematical research workflow',**({'Date':'2026-10-04'} if ext=='svg' else {})})
plt.close(fig)

"""Plot proved envelopes for original endpoint residues and critical norms."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R=Path(__file__).resolve().parent
lam=2.;alpha=.25;delta=.5;nu=1.;a0=1.;n0=11
r=1/math.sqrt(2);q=r;H=2*math.log(1+math.sqrt(2))
eta_s=1/24;rho0=1/32
assert rho0<eta_s and eta_s<(1-r*r)/(4*H)
Dstar=nu*H/a0*lam**(-(1-2*alpha)*n0)*q/(1-q)
Cstar=math.sqrt((1-r*r)/2)*math.exp(-Dstar)
L0=r/(a0*lam**n0*(1-q));U0=H/(a0*lam**n0*(1-q))
j=np.arange(0,37);n=n0+j;A=a0*lam**(-delta*j)
factor=a0*lam**(delta*n0)
lo=Cstar*factor*np.sqrt(j);hi=factor*np.sqrt(j+2)

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig,axes=plt.subplots(1,2,figsize=(18,10),facecolor='#f7f9fc')
fig.subplots_adjust(left=.075,right=.965,bottom=.38,top=.75,wspace=.27)
fig.suptitle('Finite energy and an exact critical regularity threshold',x=.075,y=.96,ha='left',fontsize=23,weight='bold',color='#152d43')
fig.text(.075,.895,r'$\lambda=2,\ \alpha=1/4,\ \delta=1/2,\ \nu=a_0=1,\ n_0=11;\quad r=q=1/\sqrt{2},\ H=2\log(1+\sqrt{2})$',fontsize=15)
fig.text(.075,.842,r'$k=2^n,\quad d_1=2^{n/2},\quad d_2=2^{(n+1)/2},\quad A_j=2^{-j/2},\quad \rho_j=1/32<\eta_{\rm s}=1/24$',fontsize=15)

ax=axes[0];ax.set_facecolor('white')
ax.fill_between(n,Cstar*A,A,color='#d9e9ee',alpha=.9)
ax.semilogy(n,A,color='#235e83',lw=2,label=r'$X_n^*\leq A_j$')
ax.semilogy(n,Cstar*A,color='#a95d21',lw=2,label=r'$X_n^*\geq C_* A_j$')
ax.set_title('Every original terminal residue remains positive',pad=16,fontsize=15)
ax.set_xlabel(r'Original scale $n=11+j$');ax.set_ylabel(r'Original terminal amplitude $X_n^*$')
ax.grid(alpha=.25);ax.legend(loc='upper right',fontsize=12)

ax=axes[1];ax.set_facecolor('white')
ax.fill_between(n,lo,hi,color='#dfeadb',alpha=.85)
ax.plot(n,hi,color='#235e83',lw=2,label=r'$32\sqrt{2}\sqrt{j+2}$')
ax.plot(n,lo,color='#a95d21',lw=2,label=r'$32\sqrt{2} C_*\sqrt{j}$')
ax.set_title('Critical square-sum norm diverges on every late stage',pad=16,fontsize=15)
ax.set_xlabel(r'Active original scale $n=11+j$');ax.set_ylabel(r'$\|X(t)\|_{\ell^2_{1/2}}$ for $t\in[t_n,t_{n+1})$')
ax.grid(alpha=.25);ax.legend(loc='upper left',fontsize=12)

fig.text(.075,.255,r'$C_*=\frac{1}{2}e^{-D_*},\quad D_*=\frac{\log(1+\sqrt{2})(1+\sqrt{2})}{16\sqrt{2}}$'
         +f'   (here {Cstar:.6f} and {Dstar:.6f}).',fontsize=15)
fig.text(.075,.202,r'$X^*\in\ell^2_\sigma\ \Longleftrightarrow\ \sigma<1/2;\qquad X^*\in\ell^\infty_\sigma\ \Longleftrightarrow\ \sigma\leq1/2.$',fontsize=16)
fig.text(.075,.151,r'$\|X(t)-X^*\|_{\ell^2}\longrightarrow0,\quad \|X(t)\|_{\ell^2}\leq1;\qquad L_0q^{j+1}\leq T_*-t\leq U_0q^j.$',fontsize=15)
fig.text(.075,.106,r'$L_0=r/[2^{11}(1-q)],\quad U_0=H/[2^{11}(1-q)]$'+' retain the original physical clock.',fontsize=13)
fig.text(.075,.065,'EX23–EX32 prove these bounds and exact spaces. Curves join integer-scale envelope samples, not numerical solution trajectories.',fontsize=13,color='#405268')
fig.text(.075,.031,'Human comparison: Terence Tao, arXiv:1402.0290v3, original truncated dyadic model. No claim about the full averaged-equation blowup follows.',fontsize=12,color='#405268')
for ext in ['png','svg']:fig.savefig(R/('original-scheduled-cascade-endpoint.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
data=dict(parameters=dict(lambda_=lam,alpha=alpha,delta=delta,nu=nu,a0=a0,n0=n0),
          original_coefficients='k=2^n;d1=2^(n/2);d2=2^((n+1)/2);A_j=2^(-j/2)',
          r=r,q=q,H=H,eta_s=eta_s,rho0=rho0,Dstar=Dstar,Cstar=Cstar,L0=L0,U0=U0,
          proof='Exercises5, EX23–EX32',interpretation='Samples of proved upper and lower envelopes; no ODE trajectory is sampled.',
          samples=[dict(n=int(nn),j=int(jj),terminal_lower=float(low),terminal_upper=float(up),critical_norm_lower=float(cl),critical_norm_upper=float(cu))
                   for nn,jj,low,up,cl,cu in zip(n,j,Cstar*A,A,lo,hi)])
(R/'original-scheduled-cascade-endpoint-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')

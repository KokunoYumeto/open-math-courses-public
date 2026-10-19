"""Exact receiving maps and support consequences of I0–I7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(18,10),facecolor='#fafcfb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,18);ax.set_ylim(0,10);ax.axis('off')
ink='#193b35';muted='#557168'
ax.text(.35,9.62,'The actual fields satisfy the local construction theorem',fontsize=23,color=ink,weight='bold')
ax.text(.35,9.16,'Theorem 3.1 · I0–I7    Original coordinates, one fixed domain and the preserved inner and exterior fields.',fontsize=12,color=muted)
def box(x,y,w,h,title,lines):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=.08',facecolor='#eaf2ee',edgecolor='#91aba0'))
 ax.text(x+.18,y+h-.4,title,fontsize=15,color=ink,weight='bold')
 for j,s in enumerate(lines):ax.text(x+.18,y+h-.9-j*.42,s,fontsize=12.5,color=ink)
box(.35,5.75,8.45,2.95,'The supplied base enters the original chart',[
 r'$\xi=q/Q,\quad \varepsilon=Q^h,\quad X=R^2/(2\xi),\quad \eta=Z\xi^{-D}$',
 r'$b=\varepsilon\xi^{-1/2}[V_0/\sqrt{2X}+O(q^{2h})]$',
 r'$V=\xi^{-A}[E_0+O(q^{2h})],\quad G=\xi^{-A}[U_0+O(q^{2h})]$',
 r'$\Sigma^B-\Sigma^{(0)}=O_I(\varepsilon^3\zeta\delta^{-N_I})$',
 'Full cutoff curls and both stress components remain; I1.'])
box(9.15,5.75,8.45,2.95,'Every finite correction uses the same domain',[
 r'$\lambda_0^2=2a(F^{(0)})^2(1-2/v_s)>0$',
 r'$q_{\rm big}=\min\{1/2,2^{-\ell_*-1}\},\quad q_*=q_{\rm big}/2$',
 r'$\sigma_j=1/5+j/10,\quad g_j=hj/10\longrightarrow\infty$',
 'The fixed inverses act on every finite source; I2–I3.',
 'One potential sum gives all residual derivative bounds; I4.'])
ax.text(.4,5.27,'Exact support consequences after summation',fontsize=16,color=ink,weight='bold')
pos=[1.0,3.2,6.0,11.8,15.8]
labels=[r'$0$',r'$X_{\rm in}=X_a/2$',r'$X_a$',r'$X_b$',r'$X_{\rm ext}=X_b+1$']
ax.plot([.8,17.1],[4.45,4.45],color=muted,lw=1)
for x,l in zip(pos,labels):
 ax.plot([x,x],[4.34,4.57],color=muted,lw=1);ax.text(x,4.77,l,ha='center',fontsize=13,color=ink)
ax.plot([pos[2],pos[3]],[4.05,4.05],lw=7,color='#2a6d9c',solid_capstyle='round')
ax.text(8.9,3.65,'All later wave and mean corrections',ha='center',fontsize=13,color=ink)
ax.text(3.0,3.03,'Inner path: corrections vanish',ha='center',fontsize=13,color=ink,weight='bold')
ax.text(3.0,2.57,r'$q=\tau,\quad \eta=0,\quad r=\sqrt{2X_{\rm in}\tau}$',ha='center',fontsize=13,color=ink)
ax.text(3.0,2.1,r'$u_\theta=\tau^{-A}[e_0+O(\tau^{2h})],\quad e_0>0$',ha='center',fontsize=13,color=ink)
ax.text(12.6,3.03,'Exterior: exact heat swirl and its pressure',ha='center',fontsize=13,color=ink,weight='bold')
ax.text(12.6,2.57,r'$\mathcal{A}=0,\quad \mathcal{B}=K,\quad p=-\int_r^\infty K(\rho,\tau)^2\,d\rho/\rho$',ha='center',fontsize=13,color=ink)
ax.text(12.6,2.1,r'$-\partial_\tau K=\partial_r^2K+r^{-1}\partial_rK-r^{-2}K$',ha='center',fontsize=13,color=ink)
ax.text(.4,1.46,r'Everywhere on $\Omega_*$: exact divergence zero, compatible terminal derivatives for $q\geq c>0$, and residual flat to every order.',fontsize=12,color=ink)
ax.text(.4,.93,'Radial positions show ordering only. I7 retains every viscosity factor. The full forced blowup theorem remains under audit.',fontsize=11,color=muted)
ax.text(.4,.49,'Proof: local-construction-assembly-audit.md, I0–I7. Source: OpenAI, Finite Time Blowup for Navier–Stokes, pp. 15–16, 114–116.',fontsize=10,color=muted)
ax.text(.4,.18,'Exact construction schematic; no numerical flow data.',fontsize=10,color=muted)
fig.savefig(out/'local-construction-assembly.png',dpi=140,facecolor=fig.get_facecolor())
fig.savefig(out/'local-construction-assembly.svg',facecolor=fig.get_facecolor())
plt.close(fig)

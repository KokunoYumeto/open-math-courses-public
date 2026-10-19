"""Reproducible exact support and moment schematic for Y0–Y7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(18,10),facecolor='#fafcfb');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,18);ax.set_ylim(0,10);ax.axis('off')
ink='#193b35';muted='#557168';green='#267965';blue='#315c91'
ax.text(.35,9.65,'How the positive-order coefficients become global',fontsize=23,color=ink,weight='bold')
ax.text(.35,9.18,'Original Lemma 5.2 · Y0–Y7    Exact moment equations, exterior cancellation and stress support.',fontsize=12,color=muted)
def box(x,y,w,h,title,lines,face='#eaf2ee'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=.08',facecolor=face,edgecolor='#91aba0'))
 ax.text(x+.2,y+h-.42,title,fontsize=15,color=ink,weight='bold')
 for j,s in enumerate(lines):ax.text(x+.2,y+h-.93-j*.40,s,fontsize=13,color=ink)
box(.35,6.05,8.45,2.65,'Two fixed matrix inverses restore five moments',[
 r'$B_U\alpha_n=-\left(m^0_{n,1},\ m^0_{n,4}/(e_*f)\right)^T$',
 r'$B_E\beta_n=-\left(m^0_{n,2},\ m^0_{n,3}/(2e_*f),\ -m^0_{n,5}/(e_*f)\right)^T$',
 r'$p=(1,1-2\lambda),\qquad s=(2,-2-2\lambda,-2\lambda)$',
 r'$m_{n,1}=m_{n,2}=m_{n,3}=m_{n,4}=m_{n,5}=0$'])
box(9.15,6.05,8.45,2.65,'Each moment has a specific receiving equation',[
 r'$m_{n,1}=0\ \Longrightarrow\ F_n=V_n=0\quad(X\geq X_+)$',
 r'$m_{n,3}=0\ \Longrightarrow\ \Pi_n=0\quad(X\geq X_+)$',
 r'$m_{n,2}=m_{n,4}=0:\ \int_0^\infty R^2\mathfrak{r}_{\theta,n}\,dR=0$',
 r'$m_{n,1}=m_{n,5}=0:\ \int_0^\infty R\mathfrak{r}_{z,n}\,dR=0$'])
ax.text(9.35,6.18,'The residual integrals also use completed lower moments and Y4.5.',fontsize=10,color=muted)
ax.text(.35,5.65,'One fixed radial arrangement at every order',fontsize=16,color=ink,weight='bold')
ax.text(11.5,5.65,'Positions show order, not distances.',fontsize=11,color=muted)
xs=[3.8,5.0,6.1,7.5,9.25,11.0,12.55,14.0,16.6]
labels=[r'$0$',r'$X_a$',r'$X_-$',r'$a^2$',r'$\mathcal{I}_{\rm pos}$',r'$\mathcal{I}_{\rm mean}$',r'$X_v$',r'$X_+$',r'$X_b$']
ax.plot([xs[0],17.2],[5.0,5.0],color=muted,lw=1)
for x,lab in zip(xs,labels):
 ax.plot([x,x],[4.9,5.1],color=muted,lw=1);ax.text(x,5.20,lab,ha='center',fontsize=12,color=ink)
for title,y,left,right,col in [
 ('Inner equality',4.55,xs[0],xs[2],green),
 ('Analytic parameter domain',4.05,xs[0],xs[3],green),
 (r'$\mathbf{P}_n\quad(n\geq1)$',3.55,xs[0],xs[7],blue),
 (r'$\mathcal{T}_n\quad(n\geq2)$',3.05,xs[2],xs[7],blue),
 (r'$\mathcal{T}_1$',2.55,xs[2],xs[8],'#946630')]:
 ax.text(.45,y,title,va='center',fontsize=13,color=ink)
 ax.plot([left,right],[y,y],lw=6,color=col,solid_capstyle='butt')
 ax.scatter([left,right],[y,y],s=25,color=col,zorder=3)
ax.text(3.8,2.05,r'On $\mathcal{I}_{\rm mean}$: $E_n=U_n=F_n=V_n=0$; pressure support closes later at $X_+$.',fontsize=12,color=ink)
ax.text(.4,1.50,r'Outer endpoint: $\mathcal{T}_{1,\theta}=e^{-4/\delta_b^2}\delta_b^{-3}B_1(\delta_b,\eta)$, with $B_1$ smooth and $\delta_b=\log(X_b/X)$.',fontsize=13,color=ink)
ax.text(.4,1.02,r'All fixed derivatives obey $|\partial_X^k\partial_\eta^\ell\mathcal{T}_n|\leq C_{n,k,\ell}\zeta\delta^{-N_{n,k,\ell}}$; $N_{n,k,\ell}=0$ for $n\geq2$.',fontsize=13,color=ink)
ax.text(.4,.55,'Proof: positive-order-extension-audit.md, Y0–Y7. Base summation is proved in Z0–Z8; the full blowup theorem remains unverified.',fontsize=11,color=muted)
ax.text(.4,.22,'Source: OpenAI, Finite Time Blowup for Navier–Stokes, pp. 49–54. Schematic only; no numerical data.',fontsize=10,color=muted)
fig.savefig(out/'positive-order-extension.png',dpi=140,facecolor=fig.get_facecolor())
fig.savefig(out/'positive-order-extension.svg',facecolor=fig.get_facecolor())
plt.close(fig)

"""Exact five-profile correction and its full receiving maps, MM1–MM9."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,16),dpi=100,facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,16));ax.axis('off')
ink,blue,orange='#172a42','#1b638f','#a24c16'
def text(x,y,s,size=20,color=ink):ax.text(x,y,s,va='top',fontsize=size,color=color,linespacing=1.4)
def panel(y,h,title):
    ax.add_patch(FancyBboxPatch((.45,y),13.1,h,boxstyle='round,pad=.12',linewidth=1,edgecolor='#b9cadb',facecolor='white'))
    text(.75,y+h-.2,title,20,blue)
text(.65,15.73,'Five compact profiles and three exact defect equations',25)
text(.65,15.14,r'Original base: $G_q=0$, $V_q=a(\eta)x^{-1-2\lambda}$, $\lambda>0$, $a(\eta)>0$.',19)
panel(11.05,3.45,'1  The complete five-row linear map · MM1–MM3')
text(.85,13.74,r'$\int R^2\Delta v\,dR=0,\qquad\int R\gamma_d\,dR=0$',22)
text(.85,12.99,r'$\int (2V/R)\Delta v\,dR=-\mathcal{P}$',22)
text(.85,12.29,r'$\int R^2(G\Delta v+V\gamma_d)\,dR=-\mathcal{J}_\theta$',22)
text(.85,11.59,r'$\int(2RG\gamma_d-RV\Delta v)\,dR=-\mathcal{J}_z$',22)
panel(7.95,2.7,'2  Invert the actual matrices and take the compact curl · MM3–MM4')
text(.85,9.88,r'$A_\theta u=(0,-\mathcal{P}_q,-\mathcal{J}_{z,q})^T,\qquad A_zs=(0,-\mathcal{J}_{\theta,q})^T$',21)
text(.85,9.12,r'$\Psi_{\mathrm{phys}}=q^{1/2-A}H(x)/x,\quad\Delta\beta_{\mathrm{phys}}=-\partial_z\Psi_{\mathrm{phys}},\quad\Delta\gamma_{\mathrm{phys}}=\gamma_{d,\mathrm{phys}}$',19)
text(.85,8.38,'Both moments are zero; the full potential stays in the reserved patch.',17)
panel(4.05,3.5,'3  Recompute the pressure and every quadratic defect · MM5–MM7, MM9')
text(.85,6.82,r'$g_{r,\mathrm{new}}-g_r=(2V/R)\Delta v+\mathcal{R}_g$',22)
text(.85,6.09,r'$\mathcal{P}_{\mathrm{new}}=\int\langle\mathcal{R}_g\rangle_Y\,dR$',22)
text(.85,5.34,r'$\mathcal{D}(U+d(t))=\mathcal{D}(U)-t+K(t)+B(t,t)$',22)
text(.85,4.60,r'$t=\mathcal{D}(U)\quad\Longrightarrow\quad\mathcal{D}_{\mathrm{new}}=K(t)+B(t,t)$',22)
panel(.65,3.0,'4  The full receiving bounds · MM6–MM8')
text(.85,2.92,r'$\mathcal{R}_g\in\mathsf{M}_{\alpha+0.9},\quad\mathcal{D}_{\mathrm{new}}\in\mathsf{S}_{\alpha+0.9}$',23)
text(.85,2.15,r'$\Delta E_\theta,\Delta E_z\in\mathsf{M}_{\alpha+1},\quad\mathsf{P}_{\ne0}\delta\mathscr{R}\in\mathsf{W}_\alpha$',23)
text(.85,1.39,r'Original inputs: $v,\gamma\in\mathsf{M}_{0.9}$, $\beta\in\mathsf{M}_{1.9}$, $\alpha\geq0.9$, $w\in\mathsf{W}_{1/2}$.',17)
text(.85,.91,'Every cutoff and pressure term remains. Full viscosity factors: MM2, MM9.4–MM9.7.',16,orange)
text(.65,.29,'Source: OpenAI, Lemmas 8.7–8.8, sections 8.6–8.7, pages 96–100; Step 4, page 111.  Proofs: MM1–MM9.',12.5)
for ext in ['svg','png']:fig.savefig(out/('five-profile-moment-correction.'+ext),dpi=100)
p=out/'five-profile-moment-correction.svg'
p.write_text(re.sub(r'width="1008pt" height="1152pt"','width="1400" height="1600"',p.read_text(encoding='utf8')),encoding='utf8')
plt.close(fig)

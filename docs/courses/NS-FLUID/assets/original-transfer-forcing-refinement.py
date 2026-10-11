"""Exact transfer-bound diagram; all time spacing is schematic."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,10),facecolor='#f6f8fb');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#153047';blue='#176d9a';orange='#b65c26'
ax.text(.045,.945,'Keep the decay when the forcing enters',fontsize=27,fontweight='bold',color=ink)
ax.text(.045,.9,'The actual first transfer: original physical time, viscosity and every forcing term retained',fontsize=15,color=ink)
ax.plot([.10,.86],[.79,.79],color=ink,lw=2)
for x,label,sub in [(.10,r'$s_0$',r'$t_c+\kappa^{-1}K^{-9}$'),(.42,r'$t_1$',r'$t_c+\kappa^{-1}K^{-1}$'),(.86,r'$t_2$',r'$t_c+\kappa^{-1}K^{-1/2}$')]:
 ax.plot([x,x],[.778,.802],color=ink,lw=2);ax.text(x,.835,label,ha='center',fontsize=20,color=ink);ax.text(x,.745,sub,ha='center',fontsize=15,color=ink)
ax.text(.26,.797,r'$z\geq-2K^{-100}$',ha='center',fontsize=16,color=blue)
ax.text(.64,.797,r'$z\geq1/20$',ha='center',fontsize=16,color=orange)
ax.add_patch(FancyBboxPatch((.045,.474),.91,.2,boxstyle='round,pad=.012',fc='white',ec='#c8d8e1'))
ax.text(.06,.631,r'$G(t_2,r)=\exp\left(-\lambda\int_r^{t_2}z(v)\,dv\right),\qquad\lambda=\kappa q^{5/2}K,\quad\kappa=q^{5n_0/2}$',fontsize=19,color=ink)
ax.text(.06,.568,r'$\int_{s_0}^{t_2}G(t_2,r)\,dr\ \leq\ e^{-\Theta}\frac{e^{2\lambda\eta h}-1}{2\lambda\eta}+\frac{20}{\lambda}(1-e^{-\Theta})$',fontsize=24,color=blue)
ax.text(.06,.495,r'$h=t_1-s_0,\quad\eta=K^{-100},\quad\Theta=\lambda(t_2-t_1)/20=q^{5/2}(\sqrt{K}-1)/20$',fontsize=16,color=ink)
ax.text(.055,.423,'The complete scalar forcing obeys',fontsize=16,color=ink)
ax.text(.39,.423,r'$|\mathcal{Q}|\leq10\kappa K^{-89}$',fontsize=20,color=ink)
ax.text(.055,.35,r'$E(t_2)\leq201K^{-90}$',fontsize=25,color=blue)
ax.text(.44,.35,r'$\|u(t_2)-e_1\psi_{1,n_0+1}\|_2^2\leq403K^{-90}$',fontsize=22,color=blue)
ax.text(.055,.28,r'$e_1=a_{n_0+1}(t_2),\qquad \|u(t_2)-\psi_{1,n_0+1}\|_2\leq21K^{-45}$',fontsize=23,color=orange)
ax.text(.055,.207,'Every orthogonal diffusion component and every higher scale is included.',fontsize=17,color=ink)
ax.text(.055,.154,'EX14–EX18 retain the full q-to-power20 tail and the original Sobolev factor',fontsize=15,color=ink)
ax.text(.70,.108,r'$(1+\chi q^{2n_0})^\sigma$',fontsize=23,color=ink)
ax.text(.055,.108,r'$\chi=4\pi^2(1+\epsilon_0/2)^2,\qquad0\leq\sigma\leq10$',fontsize=20,color=ink)
ax.text(.045,.052,'Exact bounds from lesson44, Exercises2–4, EX6–EX18, under the full original FT1–FT3 parameter restrictions.',fontsize=11.5,color='#456376')
ax.text(.045,.023,'Time spacing is schematic. Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex2196–2550.',fontsize=11,color='#456376')
for ext in ['png','svg']:fig.savefig(P/f'original-transfer-forcing-refinement.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)


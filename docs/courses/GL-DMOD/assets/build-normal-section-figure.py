"""Reproducible real normal-plane and cone sections for FIM.43–FIM.51."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
root=Path(__file__).resolve().parent
out=root if root.name=='assets' else root/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'FIM-normal-section'})
fig,axes=plt.subplots(1,3,figsize=(15,5.4))
fig.suptitle('The two normal sections inside one proper outer cone',fontsize=17,y=.98)
ax=axes[0]
for radius,color,style in [(1,'#26678a','-'),(.75,'#8c9fab','--'),(.25,'#8c9fab',':')]:
 ax.add_patch(Circle((0,0),radius,fill=False,edgecolor=color,linestyle=style))
ax.scatter([0,1/16],[0,0],c=['#14506a','#bd5d22'],s=32,zorder=4)
ax.annotate(r'zero section $\zeta=0$',(0,0),(-.85,-.5),arrowprops={'arrowstyle':'-'})
ax.annotate(r'input section $d=1/16$',(1/16,0),(.05,.52),arrowprops={'arrowstyle':'-'})
ax.text(0,-1.3,r'$\rho=1,\quad |\widetilde d|\leq1/8$'+'\n'+r'$\Phi_t(\zeta)=\zeta+t\widetilde d\,\chi(|\zeta|)$',ha='center')
ax.set(xlim=(-1.45,1.45),ylim=(-1.55,1.35),xlabel=r'$\Re\zeta$',ylabel=r'$\Im\zeta$')
ax.set_aspect('equal');ax.set_title('1. Actual normal plane (m = 2)',fontsize=12,pad=12)
ax.spines[['top','right']].set_visible(False)
ax=axes[1]
r=np.linspace(0,1.1,800)
chi=np.where(r<=.25,1,np.where(r<.75,1.5-2*r,0))
ax.plot(r,chi,c='#26678a',lw=2.5)
ax.scatter([.25,.75],[1,0],c='#26678a',s=25)
ax.axvline(.25,c='#8c9fab',ls=':',lw=1);ax.axvline(.75,c='#8c9fab',ls=':',lw=1)
ax.text(.04,.5,r'$\operatorname{Lip}(\chi)=2$'+'\n'+r'$\operatorname{Lip}(\Phi_t-\mathrm{id})\leq1/4$',fontsize=11)
ax.text(.55,.7,'Identity outside\n'+r'$|\zeta|\geq3\rho/4$',ha='center',fontsize=11)
ax.set(xlim=(0,1.1),ylim=(-.1,1.15),xlabel=r'$r=|\zeta|/\rho$',ylabel=r'$\chi(r)$')
ax.set_xticks([0,.25,.75,1]);ax.set_title('2. Uniform inverse and complement',fontsize=12,pad=12)
ax.spines[['top','right']].set_visible(False)
ax=axes[2]
a=np.linspace(0,1,400);radius=math.sqrt(258)*a
ax.fill_between(a,-radius,radius,color='#e4eff3')
ax.plot(a,radius,c='#26678a');ax.plot(a,-radius,c='#26678a')
ax.plot(a,a,c='#bd5d22',lw=2,label=r'$d=a$')
ax.plot(a,0*a,c='#14506a',lw=2,label=r'$\zeta=0$')
for t in [0,.25,.5,.75,1]:ax.plot(a,t*a,c='#bd5d22',lw=.7,alpha=.5)
ax.scatter([0],[0],c='#14506a',s=28,zorder=5)
ax.annotate('Collapsed fibre: both sections coincide',(0,0),(.14,-9),fontsize=10,
 arrowprops={'arrowstyle':'-'})
ax.text(.12,11,r'$\rho=\sqrt{258}\,a$'+'\n'+r'$A=L=1,\quad b=0$',fontsize=11)
ax.text(.45,-15,r'$|d|\leq\rho/16$',fontsize=11)
ax.set(xlim=(-.05,1.05),ylim=(-17,17),xlabel=r'$a=\Re f_u$',ylabel=r'one real section of $\zeta$')
ax.legend(loc='center right',fontsize=10)
ax.set_title('3. Entire collapsing family',fontsize=12,pad=12)
ax.spines[['top','right']].set_visible(False)
fig.text(.5,.025,'FIM.43–FIM.49: exact constants and supports. FIM.50–FIM.51: proper trace and even normal blocks.\n'
 'Panel 3 is a real section of the normal ball; it depicts the continuous support family, not an isolated-fibre argument.',
 ha='center',fontsize=10)
fig.tight_layout(rect=(0,.12,1,.92))
fig.savefig(out/'normal-section-comparison.png',dpi=170,facecolor='white')
fig.savefig(out/'normal-section-comparison.svg',facecolor='white',metadata={'Date':None})
(out/'normal-section-exact-data.json').write_text(json.dumps({
 'normal_complex_dimension':1,'real_normal_dimension':2,'rho_for_disk':1,
 'd_for_disk':'1/16','clipping_ratio':'1/8','chi_breakpoints':['1/4','3/4'],
 'chi_Lipschitz':2,'perturbation_Lipschitz':'1/4','inverse_lower_bound':'3/4',
 'cone_real_section':{'A':1,'L':1,'Lstar_squared':258,'b':0,'d':'a','rho':'sqrt(258)*a'},
 'proof_locators':['FIM.43–FIM.49','FIM.50–FIM.51'],
 'free_human_context':'https://arxiv.org/abs/2102.08861v2',
 'mathematical_argument':'Local HI.1/HI.A and FIM.5; the context citation is not a substitute for these proofs.'
 },indent=2)+'\n',encoding='utf-8')
print('normal-section-comparison: 2550x918 PNG, SVG and exact data')

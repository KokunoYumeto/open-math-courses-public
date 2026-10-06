"""Reproducible exact density-change diagram for Propositions 1.1 and 2.1."""
import hashlib,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
here=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(6,9.5));fig.patch.set_facecolor('#fcfcfa')
ax.set(xlim=(0,6),ylim=(0,10));ax.axis('off')
def box(x,y,width,height,text,color='#e8eef7',size=15):
    ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.08',facecolor=color,edgecolor='#244564',linewidth=1.3))
    ax.text(x+width/2,y+height/2,text,ha='center',va='center',fontsize=size,color='#16304a',linespacing=1.45)
def arrow(x1,y1,x2,y2,label,offset=.16):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','lw':1.6,'color':'#244564'})
    ax.text((x1+x2)/2,(y1+y2)/2+offset,label,ha='center',va='bottom',fontsize=13,color='#16304a')
ax.text(3,9.55,'Two radial factors in\none critical density',ha='center',va='center',fontsize=21,color='#16304a',linespacing=1.4)
box(.3,7.8,5.4,1.05,'Cubic variables and constraints\n'+r'$(\xi,s),\quad F=(\Phi_\xi,\Phi_s)$',size=19)
box(.3,5.6,5.4,1.55,'Ambient measure: factor '+r'$\rho$'+'\n'+r'$\tau=\rho s,\quad \rho=\xi_n>0$'+'\n'+r'$|d\xi\,d\tau|=\rho\,|d\xi\,ds|$',size=19)
box(.3,3.3,5.4,1.65,'Delta density: factor '+r'$\rho$'+'\n'+r'$F_h=AF,\quad \det A=\rho^{-1}$'+'\n'+r'$\delta(F_h)=\rho\,\delta(F)$',size=19)
box(.3,.45,5.4,2.3,r'$d_{C_\phi}=\rho^2\,|dx\,d\xi^{\prime}\,ds|$'+'\n'+r'$\widetilde a=a/\rho$'+'\n'+r'$\widetilde a\,d_{C_\phi}^{1/2}$'+'\n'+r'$=a\,|dx\,d\xi^{\prime}\,ds|^{1/2}$',color='#e7f2eb',size=18)
for top,bottom in [(7.7,7.25),(5.5,5.05),(3.2,2.85)]:
    ax.annotate('',xy=(3,bottom),xytext=(3,top),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#244564'})
ax.text(3,.08,'Propositions 1.1 and 2.1 • exact through s = 0',ha='center',fontsize=13,color='#244564')
fig.tight_layout(pad=.7)
dest=here/'fold-critical-density.svg';fig.savefig(dest,facecolor=fig.get_facecolor())
qa=here/'fold-critical-density-qa.png';fig.savefig(qa,dpi=140,facecolor=fig.get_facecolor());plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'figure':'figures/fold-critical-density.svg','sha256':sha(dest),
 'script':Path(__file__).name,'script_sha256':sha(Path(__file__)),
 'qa_image':qa.name,'qa_image_sha256':sha(qa),
 'visual_inspection':'pending','proof_locators':'U019 Propositions 1.1 and 2.1',
 'exact_objects':'ambient radial Jacobian rho, constraint determinant rho^-1, critical density rho^2 and amplitude/half-density cancellation',
 'source':'Original diagram; mathematical convention contextualized by H4 (25.3.7)–(25.3.8).'}
(here/'figure-record.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'figure':dest.name,'sha256':sha(dest),'qa_image':qa.name}))

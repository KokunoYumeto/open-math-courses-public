"""Whole positive form, exact damping curves and normalized evaluation growth."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path','svg.hashsalt':'AN04-complex-fio-models-v1','axes.titlesize':14,'axes.labelsize':14})
fig,ax=plt.subplots(3,1,figsize=(6.5,12))
fig.subplots_adjust(top=.90,bottom=.12,hspace=1.18,left=.17,right=.95)
fig.suptitle('Complex FIOs: positivity, damping and a real obstruction',fontsize=14,y=.98)
C=np.array([[1,0,-1,0],[0,1,0,0],[-1,0,1,0],[0,0,0,1]])
ax[0].imshow(C,cmap='RdBu',vmin=-1,vmax=1)
labels=[r'$\xi_1$',r'$\xi_2$',r'$\eta_1$',r'$\eta_2$']
ax[0].set_xticks(range(4),labels);ax[0].set_yticks(range(4),labels)
for i in range(4):
 for j in range(4):ax[0].text(j,i,str(C[i,j]),ha='center',va='center',color='white' if C[i,j] else '#222222',fontsize=15)
ax[0].set_title('A. Full matrix C of the positive Hermitian form\n'+r'$i\Omega(\overline{V},V)=2\overline{q}^{\,t}Cq$')
ax[0].text(.5,-.45,'Real radical: span (1, 0, 1, 0)\nBoth endpoint momenta are present.',transform=ax[0].transAxes,ha='center',fontsize=12)
z=np.linspace(-1,1,2001);sample_rows=[]
for r,col in [(16,'#176b8d'),(64,'#b6592c')]:
 ax[1].plot(z,np.exp(-r*z*z/2),color=col,lw=2,label=f'Gaussian, eta = {r}')
 ax[1].plot(z,np.exp(-r*z**4),color=col,lw=2,ls='--',label=f'Quartic, eta = {r}')
 sample_rows.append({'eta':r,'sample_count_each_profile':len(z),'gaussian_e_inverse_half_width':float(np.sqrt(2/r)),'quartic_e_inverse_half_width':r**(-.25)})
ax[1].axhline(np.exp(-1),color='#555555',ls=':',lw=1)
ax[1].set(xlabel='Real base coordinate z',ylabel='Exponential modulus',ylim=(-.02,1.04),xlim=(-1,1))
ax[1].set_title('B. Exact positive-phase damping\n'+r'$e^{-\eta z^2/2}$'+' (solid), '+r'$e^{-\eta z^4}$'+' (dashed)')
ax[1].legend(loc='upper center',bbox_to_anchor=(.5,-.32),ncol=2,fontsize=9.5,frameon=False)
ax[1].grid(alpha=.18)
t=np.array([1.,4.,16.,64.]);ax[2].plot(t,np.sqrt(t),'o-',color='#b6592c',lw=2,label='Output growth after removing damping')
ax[2].plot(t,np.ones_like(t),'s--',color='#176b8d',lw=2,label='Fixed input norm')
ax[2].set_xscale('log',base=4);ax[2].set_xticks(t,[str(int(x)) for x in t]);ax[2].set_ylim(0,8.7)
ax[2].set(xlabel='Packet concentration t',ylabel='Input norm; output norm / c_f')
ax[2].set_title('C. A real input-only tangent gives evaluation\n'+r'$u_t=f(y_1)t^{1/2}h(ty_2),\quad\|A_{bad}u_t\|=c_f\sqrt{t}$')
ax[2].legend(loc='upper left',fontsize=10,frameon=False);ax[2].grid(alpha=.18)
fig.text(.12,.044,'Exact models: U029 Section 12 and Exercises 11, 12, 15.\nPanel B curves are numerical samples; full proofs accompany the figure.',fontsize=10)
p=root/'complex-fio-models.svg';fig.savefig(p,metadata={'Date':None,'Creator':'Original AN-04 mathematical figure'})
qa=root/'complex-fio-models.png';fig.savefig(qa,dpi=150);plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'exact-complex-fio-model-figure/v1','figure':'figures/'+p.name,'sha256':sha(p),'script':Path(__file__).name,'script_sha256':sha(Path(__file__)),'qa_image':qa.relative_to(root).as_posix(),'qa_image_sha256':sha(qa),'proof_locators':'U029 Section12 and Exercises11,12,15','exact_objects':'Full4x4 C and real radical; Gaussian and quartic damping at eta16,64; normalized packet output sqrt(t) versus fixed input norm at t1,4,16,64. The output constant c_f is divided out, not asserted to equal one. Quadratic tangent models are distinguished from the actual conic H.','profiles':sample_rows,'evaluation_samples':[{'t':float(v),'growth_divided_by_c_f':float(np.sqrt(v)),'input_norm':1.} for v in t],'visual_inspection':'Pending complete author inspection of rendered figure.','source':'Original reproducible drawing; outlined DejaVu/STIX glyph licences retained; no source images copied.'}
(root/'complex-fio-model-figure.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'figure':p.name,'sha256':sha(p),'profile_samples':4*len(z)}))

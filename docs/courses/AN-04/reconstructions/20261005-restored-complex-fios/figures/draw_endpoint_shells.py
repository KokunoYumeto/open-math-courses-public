"""Exact frozen scale and the proved shell-interaction majorant."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
 'svg.fonttype':'path','svg.hashsalt':'AN04-endpoint-shells-v1'})
fig,axs=plt.subplots(2,1,figsize=(8,12.5))
fig.subplots_adjust(left=.15,right=.88,top=.89,bottom=.22,hspace=.72)
fig.suptitle('The half-order endpoint: scale and summation',fontsize=19,y=.98)
R=16;t=np.linspace(0,2*np.pi,801)
axs[0].plot(np.cos(t)/np.sqrt(R),np.sqrt(R)*np.sin(t),color='#176b8d',lw=2.5)
axs[0].axhline(0,color='#999999',lw=.7);axs[0].axvline(0,color='#999999',lw=.7)
axs[0].scatter([.25,0],[0,4],color='#b6592c',zorder=4)
axs[0].annotate(r'$R^{-1/2}=1/4$',(.25,0),xytext=(.28,1.2),fontsize=12,
 arrowprops={'arrowstyle':'->','color':'#b6592c'})
axs[0].annotate(r'$R^{1/2}=4$',(0,4),xytext=(-.42,4.7),fontsize=12,
 arrowprops={'arrowstyle':'->','color':'#b6592c'})
axs[0].set(xlim=(-.5,.5),ylim=(-5.5,5.8),xlabel=r'Base displacement $\Delta x$',
 ylabel=r'Frequency displacement $\Delta\eta$')
axs[0].set_title('A. One exact frozen shell scale, R = 16\n'+r'$16(\Delta x)^2+(\Delta\eta)^2/16=1$',pad=12)
axs[0].grid(alpha=.2)
axs[0].text(.5,-.30,'The unitary change x → x/√R, η → √R η\n'
 'cancels both half-order derivative factors (E5–E6).',
 transform=axs[0].transAxes,ha='center',fontsize=12)
j,k=np.meshgrid(np.arange(11),np.arange(11))
near=np.abs(k-j)<=3
majorant=np.where(near,1.,2.**(-j-k))
im=axs[1].imshow(np.log2(majorant),origin='lower',cmap='Blues_r',vmin=-20,vmax=0,
 extent=(-.5,10.5,-.5,10.5),interpolation='nearest',aspect='auto')
axs[1].set(xticks=range(0,11,2),yticks=range(0,11,2),
 xlabel='Input shell j, frequency size 2ʲ',ylabel='Output shell k, frequency size 2ᵏ')
axs[1].set_title('B. Proved upper-bound factors, j,k = 0,…,10\n'
 '1 for |k−j| ≤ 3; 2⁻ʲ⁻ᵏ for |k−j| ≥ 4',pad=12)
cb=fig.colorbar(im,ax=axs[1],fraction=.045,pad=.035)
cb.set_label('log₂ of the displayed majorant',fontsize=11)
fig.text(.13,.052,'The matrix shows bounds, not measured operator norms.\n'
 'A common constant × finite symbol seminorm is suppressed.\n'
 'Neighboring shells use bounded overlap; distant shells are norm-summable.\n'
 'Complete proof: endpoint companion E0–E4; earlier AN-03 packet estimate E23.',
 fontsize=11,linespacing=1.5)
p=ROOT/'endpoint-shells.svg';fig.savefig(p,metadata={'Date':None,'Creator':'Original AN-04 mathematical figure'})
png=ROOT/'endpoint-shells.png';fig.savefig(png,dpi=130);plt.close(fig)
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
report={'passed':True,'frozen_scale':R,'ellipse_equation':'16 dx^2 + deta^2/16 = 1',
 'grid_shape':[11,11],'matrix_meaning':'proved majorant after suppressing one common constant and the finite symbol seminorm',
 'near_factor':1,'near_band':'abs(k-j)<=3','far_factor':'2^(-j-k)',
 'figure_sha256':sha(p),'script_sha256':sha(Path(__file__)),'png_sha256':sha(png),
 'proof':'endpoint-half-order-bound.md E0-E4','finite_grid_is_general_proof':False,
 'visual_inspection':'pending'}
(ROOT/'endpoint-shells-data.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'figure':p.name,'sha256':sha(p)}))

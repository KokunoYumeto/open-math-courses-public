"""Reproduce the graph-domain diagram and original-coefficient mode samples."""
from pathlib import Path
import hashlib,json
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT=Path(__file__).resolve().parent
mp.mp.dps=80
lam=mp.findroot(lambda t:t**3-51*t**2+85*t-16,(mp.mpf('49.2'),mp.mpf('49.3')))
assert mp.mpf('49.28181370')<lam<mp.mpf('49.28181372')
a=mp.sqrt((mp.sqrt(2)-1)/2)
K=41472*lam*mp.sqrt(33)*mp.exp(2)
epsilon=2/(K*a)
assert 0<epsilon<1
plt.rcParams.update({'font.size':14,'axes.titlesize':17,'axes.labelsize':15,'savefig.facecolor':'white'})

def box(ax,xy,w,h,label,color):
    x,y=xy
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.014',facecolor=color,edgecolor='#31465a',linewidth=1.4))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',linespacing=1.5)

def arrow(ax,start,end,label,offset=(0,0)):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',linewidth=1.7,color='#24475c'))
    ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],label,ha='center',va='center',color='#203c50')

fig,ax=plt.subplots(figsize=(14,9));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.96,'The original operator: minimal domain, full graph domain and both defects',ha='center',fontsize=20,weight='bold')
box(ax,(.035,.71),.34,.15,r'$\mathcal{H}_p^0(U)=\overline{C_c^\infty(U)}^{\|\cdot\|_{\mathcal{H}_p}}$'+'\nThe actual graph-norm closure','#f1f5e8')
box(ax,(.625,.71),.34,.15,r'$R=P_U\mathcal{H}_p^0(U)\subset L^2(U)$'+'\nClosed range of the minimal operator','#f1f5e8')
arrow(ax,(.39,.80),(.61,.80),r'$P_U$'+': bounded bijection',(0,.035))
arrow(ax,(.61,.74),(.39,.74),r'$E|_R$'+': its actual inverse',(0,-.035))
box(ax,(.035,.44),.34,.16,r'$\mathcal{H}_p(U)$'+'\nAll original weaker-polynomial\nderivatives belong to '+r'$L^2(U)$','#eaf3fa')
box(ax,(.625,.44),.34,.16,r'$L^2(U)$'+'\n'+r'$P_UE=I$'+' on every input','#eaf3fa')
arrow(ax,(.39,.55),(.61,.55),r'$P_U$',(0,.035))
arrow(ax,(.61,.48),(.39,.48),r'$E=S_U(I+B_U)^{-1}$',(0,-.035))
arrow(ax,(.205,.69),(.205,.62),'inclusion',(.075,0))
arrow(ax,(.795,.69),(.795,.62),'inclusion',(.075,0))
ax.text(.5,.375,r'$Q=I-EP_U,\quad Q^2=Q,\quad\operatorname{Ran}Q=\ker P_U,\quad Q\mathcal{H}_p^0(U)=0$',ha='center',fontsize=17)
box(ax,(.07,.15),.86,.16,r'$\mathcal{H}_p(U)/\mathcal{H}_p^0(U)\ \cong\ \ker P_U\ \oplus\ (L^2(U)/R)$'+'\n'+r'$[u]\longmapsto(Qu,[P_Uu]),\qquad (k,[f])\longmapsto[k+Ef]$','#fff3de')
ax.text(.5,.075,'The direct sum is bounded; its summands need not be orthogonal.\nEvery domain and the original coefficient family remain present.',ha='center',fontsize=14)
diagram=OUT/'graph_domain_defect_maps.png';fig.savefig(diagram,dpi=150);plt.close(fig)

N=30
x=[mp.mpf(-1)/4+mp.mpf(j)/400 for j in range(201)]
def mode(z,adjoint):
    term=mp.mpc(1);total=term
    for k in range(1,N):
        h=k-1
        numerator=-(1+mp.j*epsilon*(2*h+1)) if adjoint else 1-2*mp.j*epsilon*h
        term*=numerator*z*z/((2*k)*(2*k-1))
        total+=term
    return total
v=np.array([complex(mode(z,False)) for z in x]);w=np.array([complex(mode(z,True)) for z in x])
ex=np.array([float(mp.exp(z)) for z in x]);uu=ex[:,None]*v[None,:];gg=ex[:,None]*w[None,:]
fig,axs=plt.subplots(2,2,figsize=(15,10.5),layout='constrained')
fig.suptitle('Independent kernel and adjoint-kernel modes for the unchanged example',fontsize=21,weight='bold')
for ax,data,label in zip(axs.ravel(),[uu.real,uu.imag,gg.real,gg.imag],['Real part of '+r'$u_1$','Imaginary part of '+r'$u_1$','Real part of '+r'$g_1$','Imaginary part of '+r'$g_1$']):
    image=ax.imshow(data,origin='lower',extent=(-.25,.25,-.25,.25),interpolation='nearest',cmap='viridis',aspect='equal')
    ax.set_title(label);ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$');bar=fig.colorbar(image,ax=ax,shrink=.86);bar.formatter.set_powerlimits((-3,3));bar.update_ticks()
fig.supxlabel(r'$U=(-1/4,1/4)^2,\quad P=-\partial_1^2+\partial_2-i\varepsilon x_1\partial_1,\quad \varepsilon=2/(Ka)$'+'\n'+r'$K=41472\lambda_*\sqrt{33}\,e^2,\quad a=\sqrt{(\sqrt{2}-1)/2}$'+'\nSamples include the boundary of the square; the proved modes restrict to the open domain.',fontsize=15)
samples=OUT/'original_coefficient_kernel_modes.png';fig.savefig(samples,dpi=150);plt.close(fig)

def rec(path):
    z=path.read_bytes()
    return dict(path=path.name,bytes=len(z),sha256=hashlib.sha256(z).hexdigest())
receipt=dict(original_polynomial='xi1^2+i xi2',original_operator='D1^2+i D2+epsilon x1 D1',D_convention='D=-i partial',domain='U=(-1/4,1/4)^2',full_strength_squared='xi1^4+xi2^2+4 xi1^2+1+4',lambda_star_definition='Largest real root of lambda^3-51lambda^2+85lambda-16',lambda_star_sample=str(lam),a=str(a),K=str(K),epsilon=str(epsilon),sampled_parameter=1,retained_even_terms=N,kernel_series='exp(x2) sum_{k>=0} prod_{h=0}^{k-1}(1-2 i epsilon h) x1^(2k)/(2k)!',adjoint_series='exp(x2) sum_{k>=0} prod_{h=0}^{k-1}(-(1+i epsilon(2h+1))) x1^(2k)/(2k)!',kernel_truncation_bound='exp(9/32)*(1/32)^30/30!',adjoint_truncation_bound='exp(3/8)*(1/8)^30/30!',kernel_truncation_bound_sample=str(mp.exp(mp.mpf(9)/32)*(mp.mpf(1)/32)**30/mp.factorial(30)),adjoint_truncation_bound_sample=str(mp.exp(mp.mpf(3)/8)*(mp.mpf(1)/8)**30/mp.factorial(30)),floating_samples='Coefficients evaluated with80decimal digits, then converted to display samples; these are numerical illustrations and do not prove the mathematical identities or certify a floating-point error bound.',sampled_original_coordinates=dict(x1=[str(z) for z in x],x2=[str(z) for z in x]),figure_files=[rec(diagram),rec(samples)],reproducible_source=rec(Path(__file__)),license='CC0-1.0')
(OUT/'FIGURE_FORMULAS_AND_REPRODUCTION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=receipt['figure_files'],epsilon_sample=str(epsilon),numerical_samples_only=True)))

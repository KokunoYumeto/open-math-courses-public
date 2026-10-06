"""Original exact map diagrams and a local oriented normal fibre for RC047."""
from pathlib import Path
import argparse,json,os
OWN=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(OWN/'qa/mpl-config')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'AN02-RC047-original-v1','mathtext.fontset':'dejavusans'})
BLUE='#155e91';GREEN='#197649';INK='#192d3d';ORANGE='#ad521a'
def arrow(ax,a,b,label=None,above=.22):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,lw=2,color=INK))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+above,label,ha='center',va='bottom',fontsize=17,color=INK)
def text(ax,x,y,s,size=18,color=INK):ax.text(x,y,s,ha='center',va='center',fontsize=size,color=color)
def save(fig,out,name):
    fig.savefig(out/(name+'.png'),dpi=160,facecolor='white',metadata={'Software':'Open Mathematics Courses'})
    fig.savefig(out/(name+'.svg'),facecolor='white',metadata={'Date':None,'Creator':'Open Mathematics Courses'})
    plt.close(fig)
def main():
    arg=argparse.ArgumentParser();arg.add_argument('--output',type=Path,default=OWN/'figures');out=arg.parse_args().output;out.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(14,8));fig.subplots_adjust(left=.035,right=.965,bottom=.035,top=.965);ax.set(xlim=(0,14),ylim=(0,8));ax.axis('off')
    text(ax,7,7.5,'The actual coefficient map is fixed by its right-cap square',25)
    text(ax,3.3,5.9,r'$H_c^p(M;\mathbb{Q})\otimes_{\mathbb{Q}}\mathbb{R}$',22,BLUE)
    text(ax,10.7,5.9,r'$H_c^p(M;\mathbb{R})$',22,BLUE)
    text(ax,3.3,3.7,r'$H_{m-p}(M;\mathbb{Q})\otimes_{\mathbb{Q}}\mathbb{R}$',22,GREEN)
    text(ax,10.7,3.7,r'$H_{m-p}(M;\mathbb{R})$',22,GREEN)
    arrow(ax,(5.4,5.9),(8.9,5.9),r'$B_{M,p}$')
    arrow(ax,(5.4,3.7),(8.9,3.7),r'$E_{M,m-p}$')
    arrow(ax,(3.3,5.42),(3.3,4.18));text(ax,1.48,4.8,r'$D_{M,\mathbb{Q}}^p\otimes 1$',18)
    arrow(ax,(10.7,5.42),(10.7,4.18));text(ax,12.32,4.8,r'$D_{M,\mathbb{R}}^p$',18)
    text(ax,7,2.62,r'$D_{M,\mathbb{R}}^p B_{M,p}=E_{M,m-p}(D_{M,\mathbb{Q}}^p\otimes 1)$',21)
    text(ax,7,1.8,'Same positive integer orientation class; same tail evaluation and front face.',17)
    text(ax,7,1.12,'Bottom and vertical maps are isomorphisms at their stated entries.',18,GREEN)
    text(ax,7,.52,'Finite tensor sums and finite chains. No tensor identity for an infinite cochain dual.  RC5–RC14',15)
    save(fig,out,'coefficient-and-right-cap-square')
    fig,ax=plt.subplots(figsize=(14,8));fig.subplots_adjust(left=.035,right=.965,bottom=.035,top=.965);ax.set(xlim=(0,14),ylim=(0,8));ax.axis('off')
    text(ax,7,7.55,'A rational connecting map with the normal-first normalization',25)
    center=np.array([3.,5.52]);radius=1.
    ax.add_patch(Circle(center,radius,facecolor='#e7f2fa',edgecolor=BLUE,lw=2.5))
    arrow(ax,(1.55,5.52),(4.55,5.52));arrow(ax,(3.,4.13),(3.,6.92))
    text(ax,4.65,5.27,'x',17);text(ax,3.25,6.87,'y',17)
    theta=np.linspace(.25,.95,40);points=center+np.c_[np.cos(theta),np.sin(theta)]*radius
    ax.plot(points[:,0],points[:,1],color=GREEN,lw=3)
    ax.add_patch(FancyArrowPatch(points[-2],points[-1],arrowstyle='-|>',mutation_scale=23,color=GREEN,lw=2))
    text(ax,1.4,6.7,r'$dx\wedge dy$',18,BLUE)
    text(ax,3.,3.94,'One normal fibre: unit disc.',14)
    text(ax,3.,3.66,'Positive boundary circle.',14)
    text(ax,9.15,6.86,'Example degree ledger: N=8, dim Y=6',18)
    rows=[(p,6-p,(-1)**p)for p in range(4)]
    labels=[['p','q = N − 2 − p','coefficient (−1)^p']]+[[str(p),str(q),'+'+'1' if sign>0 else '−1']for p,q,sign in rows]
    table=ax.table(cellText=labels,cellLoc='center',bbox=[.49,.51,.45,.25]);table.auto_set_font_size(False);table.set_fontsize(14)
    for (r,c),cell in table.get_celld().items():cell.set_edgecolor('#c8d7e0');cell.set_facecolor('#e7f2fa'if r==0 else 'white')
    text(ax,9.25,3.94,'Circle before base; positive normal orientation.',14)
    text(ax,9.25,3.66,'Placing the two-disc first gives sign +1.',14)
    nodes=[(1.65,r'$H_c^p(Y;\mathbb{Q})$'),(5.05,r'$H_q(Y;\mathbb{Q})$'),(8.5,r'$H_{q+1}(V;\mathbb{Q})$'),(12.05,r'$H_c^{p+1}(V;\mathbb{Q})$')]
    for x,label in nodes:text(ax,x,2.62,label,17)
    arrow(ax,(2.82,2.62),(3.82,2.62),r'$D_{Y,\mathbb{Q}}^p$',.3)
    arrow(ax,(6.17,2.62),(7.27,2.62),r'$\tau_{\mathbb{Q}}$',.3)
    arrow(ax,(9.82,2.62),(10.77,2.62),r'$(-1)^p(D_{V,\mathbb{Q}}^{p+1})^{-1}$',.3)
    text(ax,7,1.7,r'$B_V(\delta_{\mathbb{Q}}\otimes 1)=\delta_{\mathbb{R}}B_Y$',21,GREEN)
    text(ax,7,.98,'Exactness descends through the actual coefficient squares and faithful field extension.',17)
    text(ax,7,.4,'Relative to the exact real CO/FC entries. Local fibre picture; global Thom gluing is required.  RC17–RC24',14)
    save(fig,out,'rational-normal-circle-and-descent')
    geometry={'schema':'AN02-RC047-original-figure-geometry/v1','coefficient_square':{'dimension':'m','degree':'p','top_arrow':'B_M,p actual coefficient map','bottom_arrow':'E_M,m-p actual finite-chain extension','vertical_arrows':'unshifted D_Q tensor1 and D_R','same_integral_orientation_class':True,'infinite_dual_tensor_identity_claimed':False},'normal_fibre':{'local_picture_only':True,'coordinate_center':[0,0],'radius':1,'orientation':'dx then dy','boundary':'counterclockwise circle before base','disc_first_swap_sign':'(-1)^(2q)=1','global_nontrivial_bundle_requires_actual_Thom':True},'degree_table':{'N':8,'dim_Y':6,'rows':[{'p':p,'q':q,'coefficient':sign}for p,q,sign in rows]},'connecting':'delta_Q^p=(-1)^p (D_V,Q^(p+1))^-1 tau_Q D_Y,Q^p','real_CO_FC_receipt_status':'see exact private entry ledger','integral_descent_claimed':False,'affine_cycle_depicted':False,'numerical_samples_used_as_proof':False}
    (out/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()

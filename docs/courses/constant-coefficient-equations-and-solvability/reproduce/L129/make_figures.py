"""Original exact two-dimensional support slice and map diagram. No external art."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'AN02-CC048-original','mathtext.fontset':'dejavusans'})
def save(fig,folder,name):
    fig.savefig(folder/(name+'.png'),dpi=160,metadata={'Software':'Original CC048 mathematical renderer'})
    fig.savefig(folder/(name+'.svg'),metadata={'Date':None,'Creator':'Original CC048 mathematical renderer'})
    plt.close(fig)
def panel(ax,x,y,w,h,text,fill='#edf5fa',size=17):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',fc=fill,ec='#31566f',lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color='#17394d')
def arrow(ax,x1,y1,x2,y2,label='',offset=.025,size=15):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=20,lw=2,color='#31566f'))
    if label:ax.text((x1+x2)/2,(y1+y2)/2+offset,label,ha='center',va='center',fontsize=size,color='#17394d')
def main(output):
    folder=Path(output);folder.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(14,8),facecolor='white');fig.suptitle('A proper normal collapse with compact support witnesses',fontsize=23,x=.51,y=.96)
    ax=fig.add_axes([.07,.34,.56,.53]);s=np.linspace(-3,3,1201);rho=1/(8*np.sqrt(1+s*s))
    ax.fill_between(s,0,rho,color='#a9d7d1',alpha=.9,label=r'$r<\rho(s)$: collapsed at $t=1$')
    ax.fill_between(s,rho,2*rho,color='#cfe1ef',alpha=.9,label=r'$r\leq2\rho(s)$: possible motion')
    ax.plot(s,rho,color='#087e75',lw=2.6);ax.plot(s,2*rho,color='#26628d',lw=2.6)
    ax.plot(s,3*rho,color='#986525',lw=2.4,ls='--',label=r'$r=3\rho(s)$: certified bound')
    ax.axhline(0,color='#17394d',lw=2);ax.set_xlim(-3,3);ax.set_ylim(0,.43);ax.set_xlabel(r'Base slice $y=(s,0)$');ax.set_ylabel(r'Normal radius $r=\|v\|$');ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=12)
    ax.text(-2.91,.403,r'$\rho(s)=1/(8\sqrt{1+s^2})$',fontsize=18)
    ax.text(-2.9,.018,r'$Y$: $r=0$',fontsize=13,color='#17394d')
    ax2=fig.add_axes([.67,.34,.29,.53]);ax2.set_xlim(-.035,1.035);ax2.set_ylim(-.035,1.02);ax2.axis('off')
    panel(ax2,.02,.68,.95,.25,'Exact height control\n'+r'$h(y,v)=\|y\|^2+\|v\|^2$'+'\n'+r'$r\leq3\rho(y):\quad\Delta h\leq9/64<1/2$',size=16)
    panel(ax2,.02,.34,.95,.25,'Joint properness\n'+r'$|h(H_t x)-h(x)|\leq1/16$'+'\nCompact target: its full inverse\ntrack is compact.',size=15)
    panel(ax2,.02,.00,.95,.25,'Protected compact set\n'+r'$C=\{y=0,\ \|v\|=1\}$'+'\n'+r'$2\rho(y)\leq1/4$'+'; the band avoids '+r'$C$.',size=16)
    bottom=fig.add_axes([.06,.06,.90,.20]);bottom.set_xlim(-.035,1.035);bottom.set_ylim(-.04,1.02);bottom.axis('off')
    panel(bottom,.005,.32,.23,.49,r'$a\in J$, support $K$',size=19)
    panel(bottom,.36,.32,.29,.49,r'$f^*a$, support $L=f^{-1}K$',size=18)
    panel(bottom,.765,.32,.23,.49,r'$R^*f^*a\in S$'+'\n'+r'$C^{\prime}=L\setminus W_0$',size=18)
    arrow(bottom,.24,.565,.355,.565,r'$f^*$',offset=.25);arrow(bottom,.65,.565,.76,.565,r'$R^*$',offset=.25)
    bottom.text(.5,.065,'CC6–CC16: collapse first, then face-compatible subdivision; a slice in four dimensions.',ha='center',fontsize=16)
    save(fig,folder,'proper-collapse-and-support')
    fig=plt.figure(figsize=(14,8),facecolor='white');fig.suptitle('The specified canonical map and its two actual comparisons',fontsize=22,y=.965)
    ax=fig.add_axes([.035,.06,.93,.83]);ax.set_xlim(-.025,1.025);ax.set_ylim(0,1.015);ax.axis('off')
    panel(ax,.01,.80,.22,.14,r'$J_F^*$',size=23);panel(ax,.38,.80,.24,.14,r'$C_c^*(U;F)$',size=23);panel(ax,.77,.80,.22,.14,r'$C_c^*(Y;F)$',size=23)
    arrow(ax,.235,.87,.375,.87,'inclusion',offset=.055);arrow(ax,.625,.87,.765,.87,r'$i^*$',offset=.055)
    ax.text(.5,.76,'CC3: degreewise onto; zero-value section is not a cochain map.',ha='center',fontsize=17)
    panel(ax,.025,.56,.32,.125,r'$[d\ell]\in H^{p+1}(J_F)$',size=22);panel(ax,.67,.56,.31,.125,r'$c_F[a]\in H_c^{p+1}(V;F)$',size=21)
    ax.plot([.88,.88,.185],[.795,.712,.712],color='#31566f',lw=2)
    arrow(ax,.185,.712,.185,.69)
    ax.text(.51,.724,r'$\Delta_F[a]=[d\ell]$: compact lift, then differential',ha='center',fontsize=14,color='#17394d')
    arrow(ax,.35,.622,.665,.622,r'$\kappa_F=r_F H(\iota_F)^{-1}$',offset=.05,size=20)
    ax.text(.5,.515,'CC18–CC19: unique inverse of an actual inclusion, followed by actual excision.',ha='center',fontsize=16)
    panel(ax,.025,.305,.95,.145,'Real comparison through smooth singular cochains\n'+r'$c_{\mathrm{sm}} I_Y=I_V\delta_{\mathrm{dR}},\qquad q_Vc_{\mathrm{ct}}=c_{\mathrm{sm}}q_Y$'+'\n'+r'$c_{\mathbb{R}}=I_{c,V}\delta_{\mathrm{dR}}I_{c,Y}^{-1}$'+'  (CO17; CC22–CC25)',size=19)
    panel(ax,.025,.06,.95,.15,'Coefficient square and the rational conclusion\n'+r'$b_Vc_{\mathbb{Q}}=c_{\mathbb{R}}b_Y=b_V\delta_{\mathbb{Q}},\qquad b_V\ \mathrm{injective}$'+'\n'+r'$c_{\mathbb{Q}}^p=(-1)^p(D_{V,\mathbb{Q}}^{p+1})^{-1}\tau_{\mathbb{Q}}D_{Y,\mathbb{Q}}^p$'+'  (CC27)',size=20)
    save(fig,folder,'canonical-maps-and-comparison')
    geometry={'schema':'AN02-CC048-original-exact-geometry/v1','native_pixels':[2240,1280],
       'support_slice':{'ambient':'R^2_y x R^2_v','base_slice':'y=(s,0)','s_interval':[-3,3],'radius':'1/(8*sqrt(1+s^2))','sample_count':1201,
         'bands':[1,2,3],'certified_height_bound':'9/64 < 1/2','actual_joint_height_change_bound':'1/16','protected_compact':'y=0, ||v||=1','slice_not_whole_tube':True},
       'map_diagram':{'actual_equations':['CC3','CC18','CC19','CC21','CC22','CC23','CC24','CC25','CC26','CC27'],'inverse_in_cohomology_only':True},
       'Blender_used':False,'Blender_reason':'Two-dimensional exact radius slices and map domains are clearer as plotted vector diagrams; no three-dimensional geometric assertion is made.',
       'integral_descent_claimed':False,'affine_C8_depicted':False}
    (folder/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).resolve().parent/'figures'));a=p.parse_args();main(a.output)

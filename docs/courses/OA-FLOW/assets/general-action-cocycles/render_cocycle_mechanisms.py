"""Reproduce the exact cocycle examples; no source images are used."""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.hashsalt':'OA-FLOW-GENERAL-COCYCLE-20261004','axes.titlesize':20,'axes.labelsize':16})
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'figures');a=parser.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
    fig,axs=plt.subplots(2,2,figsize=(16,10.5),dpi=200)
    blue='#256481';red='#ad4e2e';green='#32744e';purple='#725293'
    fig.suptitle('Cocycle order, affine averaging and the two small branches',fontsize=25,y=.965)
    ax=axs[0,0];ax.set_title('Ordered composition: arbitrary group',pad=14);ax.set_xlim(0,10);ax.set_ylim(0,5);ax.axis('off')
    for x,label in [(1.6,r'$(M,\alpha)$'),(5,r'$(M,\beta)$'),(8.4,r'$(M,\gamma)$')]:
        ax.add_patch(FancyBboxPatch((x-1.1,2.6),2.2,.85,boxstyle='round,pad=.12',fc='#edf4f7',ec=blue,lw=1.5));ax.text(x,3.02,label,ha='center',va='center',fontsize=20)
    for x,y,label in [(2.8,3.8,r'$u_g$'),(6.2,7.2,r'$v_g$')]:
        ax.annotate('',xy=(y,3),xytext=(x,3),arrowprops={'arrowstyle':'-|>','lw':2,'color':blue});ax.text((x+y)/2,3.4,label,ha='center',fontsize=20)
    ax.text(5,1.92,r'$\beta_g=\mathrm{Ad}(u_g)\alpha_g$',ha='center',fontsize=19)
    ax.text(5,1.27,r'$\gamma_g=\mathrm{Ad}(v_g u_g)\alpha_g$',ha='center',fontsize=19)
    ax.text(5,.53,'The second cocycle is for the perturbed action.',ha='center',fontsize=14)
    ax=axs[0,1];ax.set_title('Additive orbit: fixed midpoint',pad=14);ax.set_xlim(-.28,2.28);ax.set_ylim(-.8,1.4);ax.axis('off')
    ax.plot([0,2],[0,0],color=blue,lw=5,alpha=.5);ax.scatter([0,2],[0,0],s=110,color=blue,zorder=4);ax.scatter([1],[0],s=160,color=red,zorder=5)
    for x,label in [(0,r'$0$'),(1,r'$a=Z$'),(2,r'$2a$')]:ax.text(x,-.22,label,ha='center',fontsize=19)
    ax.annotate('',xy=(.08,.35),xytext=(1.92,.35),arrowprops={'arrowstyle':'<->','connectionstyle':'arc3,rad=.25','lw':1.8,'color':green});ax.text(1,.85,r'$T_1(ta)=(2-t)a$',ha='center',fontsize=19)
    ax.text(1,-.57,r'$A_{2m}=a,\quad A_{2m+1}=(1-\frac{1}{2m+1})a$',ha='center',fontsize=17)
    ax.text(1,1.19,r'$\alpha_n=\mathrm{Ad}(X^n),\quad b_n=a-\alpha_n(a)$',ha='center',fontsize=17)
    s=1/20;theta=np.linspace(-.01,.13,250);cx=np.cos(theta);cy=np.sin(theta)
    ax=axs[1,0];ax.set_title('Noncentral small cocycle: take the polar part',pad=14)
    ax.plot(cx,cy,color='#87949c',lw=1.5);u=np.array([math.cos(2*s),math.sin(2*s)]);w=np.array([math.cos(s),math.sin(s)]);b=(np.array([1,0])+u)/2
    ax.plot([1,u[0]],[0,u[1]],color=blue,lw=3);ax.scatter([1,u[0]],[0,u[1]],color=blue,s=85);ax.scatter(*b,color=red,s=95,zorder=5);ax.scatter(*w,color=purple,s=95,zorder=5)
    ax.annotate(r'$1$',(1,0),xytext=(.993,-.007),fontsize=18)
    ax.annotate(r'$e^{2is}$',u,xytext=(.983,.109),fontsize=18,color=blue)
    ax.annotate(r'$a_+=\cos(s)e^{is}$',b,xytext=(.957,.037),fontsize=17,color=red,arrowprops={'arrowstyle':'->','color':red})
    ax.annotate(r'$w_+=e^{is}$',w,xytext=(.975,.073),fontsize=17,color=purple,arrowprops={'arrowstyle':'->','color':purple})
    ax.set_xlim(.95,1.007);ax.set_ylim(-.018,.127);ax.set_xlabel('real part');ax.set_ylabel('imaginary part');ax.grid(alpha=.12)
    ax.text(.951,.119,r'$s=1/20$',fontsize=15)
    ax.text(.5,-.27,'One eigenvalue coordinate in the X basis; the other is its conjugate.',transform=ax.transAxes,ha='center',fontsize=13)
    ax=axs[1,1];ax.set_title('Central logarithm: exact additive lift',pad=14)
    ts=np.linspace(-.12,.12,300);ax.plot(np.cos(ts),np.sin(ts),color='#87949c',lw=1.5)
    for t,c,label,dy in [(.1,blue,r'$u_{\rm odd,1}=e^{i/10}$',.015),(-.1,blue,r'$u_{\rm odd,2}=e^{-i/10}$',-.024),(.05,green,r'$e^{ik_1}=e^{i/20}$',.003),(-.05,green,r'$e^{ik_2}=e^{-i/20}$',-.009)]:
        x,y=math.cos(t),math.sin(t);ax.scatter([x],[y],s=75,color=c,zorder=4);ax.annotate(label,(x,y),xytext=(.958,y+dy),fontsize=15,color=c,arrowprops={'arrowstyle':'->','color':c,'lw':1})
    ax.scatter([1],[0],color=red,s=70);ax.annotate(r'$u_{\rm even}=(1,1)$',(1,0),xytext=(.958,.003),fontsize=15,color=red)
    ax.set_xlim(.95,1.008);ax.set_ylim(-.148,.146);ax.set_xlabel('real part');ax.set_ylabel('imaginary part');ax.grid(alpha=.12)
    ax.text(.5,-.27,r'$M=\mathbb{C}^2,\quad \alpha_1(z_1,z_2)=(z_2,z_1),\quad h_n=k-\alpha_n(k)$',transform=ax.transAxes,ha='center',fontsize=16)
    fig.text(.5,.015,'Panels 2–4 are exact finite-dimensional examples; the proofs apply to arbitrary von Neumann algebras.',ha='center',fontsize=15)
    fig.subplots_adjust(left=.065,right=.97,top=.86,bottom=.13,hspace=.62,wspace=.29)
    fig.savefig(a.output_dir/'cocycle-mechanisms.png',dpi=200,metadata={'Software':'OA-FLOW original cocycle reproduction'})
    fig.savefig(a.output_dir/'cocycle-mechanisms.svg',metadata={'Date':None,'Creator':'OA-FLOW original cocycle reproduction'})
    data={'native_dimensions':[3200,2100],'ordered_composition':{'first':'u_g','second':'v_g for Ad(u)alpha','result':'v_g u_g'},'additive':{'M':'M2(C)','alpha':'Ad(X^n)','a':'Z','orbit':['0','2Z'],'fixed':'Z','averages_even':'Z','averages_odd':'(1-1/n)Z'},'noncentral_unitary':{'s':'1/20','alpha':'Ad(Z^n)','w':'exp(i s X)','u_even':'I','u_odd':'exp(2 i s X)','fixed_hull_point':'cos(s) w','polar_modulus':'cos(s) I','plotted_coordinate':'positive eigenvalue in X basis; negative eigenvalue is conjugate','u1_plus':[float(u[0]),float(u[1])],'a_plus':[float(b[0]),float(b[1])],'w_plus':[float(w[0]),float(w[1])]},'central':{'M':'C^2','alpha_generator':'coordinate swap','k':['1/20','-1/20'],'h_even':['0','0'],'h_odd':['1/10','-1/10'],'u_odd':['exp(i/10)','exp(-i/10)'],'uniform_distance':'2 sin(1/20) < 1/10 < 1/4'},'numerical_scope':'The coordinate samples used to draw arcs are numerical; all objects and rational parameters are exact as stated.'}
    (a.output_dir/'cocycle-mechanisms-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    plt.close(fig)
if __name__=='__main__':main()

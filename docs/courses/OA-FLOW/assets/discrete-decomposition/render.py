"""Exact suspension and cardinal comparison. Original drawing: CC0-1.0."""
from pathlib import Path
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

def render():
    with plt.rc_context({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
                         'font.size':14,'svg.fonttype':'none','svg.hashsalt':'oa-flow-ddp-v1'}):
        fig=plt.figure(figsize=(14,8.2),facecolor='#f7f9fb')
        ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
        ink='#182c3a';blue='#285e91';green='#20776a';orange='#aa531d'
        def text(x,y,s,size=14,color=ink,ha='left',weight='normal'):
            ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center',weight=weight)
        def box(x,y,w,h,color):
            ax.add_patch(Rectangle((x,y),w,h,facecolor=color,edgecolor='none'))
        def arrow(x,y,X,Y):
            ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=16,lw=1.7,color=blue))
        text(.04,.947,'Discrete stability and cardinal comparison',24,weight='bold')
        text(.04,.899,r'$0<\lambda<1,\quad L=-\log\lambda,\quad P=2\pi/L$',17)
        box(.03,.515,.94,.328,'white')
        text(.05,.806,'A. The exact suspension at time s = L/3',18,blue,weight='bold')
        x0=.075;x1=.915;width=x1-x0;cut=x0+2*width/3
        box(x0,.693,2*width/3,.064,'#d6eafc');box(cut,.693,width/3,.064,'#fee7cc')
        text((x0+cut)/2,.725,r'$n=0,\quad u=r+L/3$',16,blue,ha='center')
        text((cut+x1)/2,.725,r'$n=1,\quad u=r-2L/3$',16,orange,ha='center')
        ax.plot([x0,x1],[.681,.681],color=ink,lw=1.3)
        for x,label in [(x0,'0'),(cut,r'$2L/3$'),(x1,r'$L$')]:
            ax.plot([x,x],[.672,.690],color=ink,lw=1.3);text(x,.650,label,15,ha='center')
        text(.075,.607,r'$r\in[0,L),\qquad \Theta_s F(r)=\alpha^{n_s(r)}(F(u_s(r))),\qquad C_s(r)=c_{n_s(r)}$',16)
        text(.075,.552,r'$e^r\lambda^{n_s(r)}=e^{-s}e^{u_s(r)}\quad\Longrightarrow\quad\mathcal{T}\Theta_s=e^{-s}\mathcal{T}$',17,green)
        box(.03,.303,.94,.184,'white')
        text(.05,.452,'B. Continuous stability returns a constant tensor',18,blue,weight='bold')
        text(.06,.398,r'$C_s=B^*\Theta_s(B)$',18);arrow(.255,.398,.31,.398)
        text(.34,.398,r'$B=z\otimes1$',18);arrow(.53,.398,.59,.398)
        text(.62,.398,r'$c_1=z^*\alpha(z)$',18,green)
        text(.06,.344,'Normal slices prove constancy on the suspension interval.  Proof: Section 6.',13)
        box(.03,.069,.94,.204,'white')
        text(.05,.238,'C. Compare the cover cardinals before the projections',18,blue,weight='bold')
        boxes=[(.055,.265,'#d6eafc',r'$\kappa_A(p_1)=\kappa_A(p_2)$',blue),
               (.371,.265,'#d3f1e8',r'$\kappa_F(p_1)=\kappa_F(p_2)$',green),
               (.686,.255,'#fee7cc',r'$p_1\sim p_2\ \mathrm{in}\ F$',orange)]
        for x,w,c,label,color in boxes:
            box(x,.145,w,.058,c);text(x+w/2,.174,label,16,color,ha='center')
        arrow(.327,.174,.363,.174);arrow(.644,.174,.678,.174)
        text(.187,.113,'Ambient corners are M.',12,ha='center')
        text(.503,.113,'Compact saturation preserves κ.',12,ha='center')
        text(.813,.113,'Match σ-finite summands.',12,ha='center')
        text(.04,.035,'Exact half-open intervals and normal maps; no finite-dimensional approximation.  Proofs: Sections 3 and 6.',11)
        svg=io.BytesIO();png=io.BytesIO()
        fig.savefig(svg,format='svg',metadata={'Date':None,'Creator':'Original OA-FLOW mathematical figure, CC0'})
        fig.savefig(png,format='png',dpi=150,metadata={'Software':'Matplotlib; exact suspension and cardinal comparison'})
        plt.close(fig)
        return svg.getvalue(),png.getvalue()

if __name__=='__main__':
    folder=Path(__file__).resolve().parent
    svg,png=render()
    (folder/'ddp-mechanisms.svg').write_bytes(svg)
    (folder/'ddp-mechanisms.png').write_bytes(png)

"""Reproduce exact matrix support bands and the general spectral-proof maps."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'oa-flow-connes-spectrum-original-20261004'})

def box(ax,x,y,w,h,title,body,face='#f5f9fc',size=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008',edgecolor='#6f8ca4',facecolor=face,linewidth=1.3))
    ax.text(x+w/2,y+h-.055,title,ha='center',va='top',fontsize=size+1,color='#18364b')
    ax.text(x+w/2,y+h-.16,body,ha='center',va='top',fontsize=size,linespacing=1.4,color='#294b61')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'assets');args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(15,11.5),facecolor='#f7fafc')
    fig.text(.5,.975,'Connes spectrum: the support sandwich, fixed corners and full weight domains',ha='center',fontsize=17,color='#18364b')
    fig.text(.5,.945,'A/B/D: exact M3 example. C/E: the proved general maps and their stated scope.',ha='center',fontsize=11,color='#526b7f')

    ax=fig.add_axes([.07,.66,.40,.23]);ax.set_facecolor('white')
    rows=[(3,'y: I',Fraction(-21,4),Fraction(-19,4),-5,'#4382ac'),(2,'y*: -I',Fraction(19,4),Fraction(21,4),5,'#ad6543'),(1,'z: J',Fraction(-1,8),Fraction(1,8),0,'#7c69a4'),(0,'y* z y: J+(I-I)',Fraction(-5,8),Fraction(5,8),0,'#3a8c72')]
    for y,label,l,r,c,color in rows:
        ax.plot([float(l),float(r)],[y,y],color=color,linewidth=10,alpha=.35,solid_capstyle='butt');ax.scatter([c],[y],marker='D',s=45,color=color,zorder=3)
        ax.text(-6.1,y+.20,label,fontsize=10,color=color)
    ax.set_xlim(-6.25,6.25);ax.set_ylim(-.65,3.6);ax.set_xticks(range(-6,7));ax.set_yticks([]);ax.set_xlabel('Real frequency: the diamond is the exact singleton support',fontsize=10)
    ax.grid(axis='x',alpha=.16);ax.spines[['top','right','left']].set_visible(False)
    ax.set_title('A. The center cancels; only the width transfers',loc='left',fontsize=12,pad=15)
    ax.text(.5,-.24,r'$I-I=[-1/2,1/2],\quad J+(I-I)=[-5/8,5/8]$',transform=ax.transAxes,ha='center',fontsize=11,color='#294b61')

    b=fig.add_axes([.54,.65,.43,.25]);b.set_axis_off();b.text(0,1,'B. A nonzero support sandwich (acting right to left)',fontsize=12,color='#18364b',va='top')
    xs=[.015,.28,.545,.81];titles=[r'$bH=\mathbb{C} e_3$',r'$aH=\mathbb{C} e_1$',r'$aH=\mathbb{C} e_1$',r'$bH=\mathbb{C} e_3$']
    for x,title in zip(xs,titles):box(b,x,.51,.17,.24,title,'one dimension',size=9.5)
    for i,label in enumerate([r'$y=e_{13}$',r'$z=e_{11}$',r'$y^*=e_{31}$']):
        b.add_patch(FancyArrowPatch((xs[i]+.18,.64),(xs[i+1]-.01,.64),arrowstyle='->',mutation_scale=14,color='#497b9c',linewidth=1.4));b.text((xs[i]+.18+xs[i+1]-.01)/2,.83,label,ha='center',fontsize=11,color='#294b61')
    b.text(.5,.40,r'$a=s(yy^*)=e_{11},\quad b=s(y^*y)=e_{33}$',ha='center',fontsize=12,color='#294b61')
    b.text(.5,.25,r'$v=y^*zy=e_{33}\ne0$',ha='center',fontsize=14,color='#26725e')
    b.text(.5,.10,'General proof: orbit joins replace these rank-one supports.\nTwo nonvanishing steps, not a fixed polar-isometry assertion.',ha='center',fontsize=10.5,color='#526b7f',linespacing=1.4)

    c=fig.add_axes([.055,.36,.47,.24]);c.set_axis_off();c.text(0,1,'C. The actual balanced 2 x 2 action',va='top',fontsize=12,color='#18364b')
    for x,y,w,ht,title,body in [(0.02,.44,.44,.37,r'$p_1Np_1$',r'$W_t(xe_{11})=\alpha_t(x)e_{11}$'),(.52,.44,.44,.37,r'$p_2Np_2$',r'$W_t(xe_{22})=\beta_t(x)e_{22}$')]:box(c,x,y,w,ht,title,body,size=11)
    c.text(.49,.65,r'$\Gamma$',ha='center',fontsize=14,color='#526b7f')
    c.text(.5,.31,r'$\Gamma(\alpha)=\Gamma(W)=\Gamma(\beta)$',ha='center',fontsize=14,color='#26725e')
    c.text(.5,.17,r'$v_t=\mathrm{diag}(1,u_t),\quad W_t=\mathrm{Ad}(v_t)(\alpha_t\otimes\mathrm{id})$',ha='center',fontsize=11,color='#294b61')
    c.text(.5,.045,'Both diagonal projections are fixed; N=M2(M) is a factor.\nFor modular weights, BC constructs the actual balanced weight.',ha='center',fontsize=10.5,color='#526b7f',linespacing=1.4)

    d=fig.add_axes([.62,.39,.34,.16]);d.set_facecolor('white')
    spectrum=[-5,-3,-2,0,2,3,5]
    for y,values,label,color in [(3,spectrum,'action = log modular operator','#4382ac'),(2,[-2,0,2],'corner e11+e22','#ad6543'),(1,[0],'rank-one corner e33','#7c69a4'),(0,[0],'Connes spectrum','#3a8c72')]:
        d.scatter(values,[y]*len(values),s=48,color=color);d.text(-5.8,y+.17,label,fontsize=9.5,color=color)
    d.set_xlim(-6,6);d.set_ylim(-.55,3.65);d.set_xticks(range(-5,6));d.set_yticks([]);d.grid(axis='x',alpha=.13);d.spines[['top','right','left']].set_visible(False)
    d.set_title('D. One action spectrum is larger than Gamma',loc='left',fontsize=12,pad=22)
    d.text(.5,-.28,r'$h=\mathrm{diag}(0,2,5),\quad S_+(M_3)=\{1\}$',ha='center',transform=d.transAxes,fontsize=11,color='#294b61')

    e=fig.add_axes([.055,.045,.91,.24]);e.set_axis_off();e.text(0,1,'E. Full n.s.f. GNS filters and the exact comparison boundary',va='top',fontsize=12,color='#18364b')
    box(e,.02,.34,.25,.47,r'$x\in N_\varphi$',r'$T_fx\in N_\varphi$'+'\n'+r'$\|T_fx\|\leq\|f\|_1\|x\|$',size=11)
    box(e,.36,.34,.35,.47,r'$\Lambda(T_fx)=\widehat f(L)\Lambda(x)$',r'$L=\log\Delta_\varphi,\quad f\in L^1(\mathbb{R})$'+'\n'+'EW3 closes the bounded tagged-sum graph.',size=11)
    box(e,.80,.34,.18,.47,'Exact hulls',r'$\mathrm{Sp}(\sigma^\varphi)$'+'\n'+r'$=\mathrm{Sp}(L)$',size=11)
    for a,b in [(.28,.35),(.72,.79)]:e.add_patch(FancyArrowPatch((a,.57),(b,.57),arrowstyle='->',mutation_scale=16,color='#497b9c',linewidth=1.5))
    e.text(.5,.20,r'$\exp\Gamma(\sigma^\varphi)\subseteq S_+(M)$ for every factor with a faithful n.s.f. weight.',ha='center',fontsize=12,color='#294b61')
    e.text(.5,.065,'Equality proved here: separable-predual type III factors, or factors with a supplied faithful n.s.f. trace.\nNo zero-part, realization, periodic-weight existence or classification conclusion.',ha='center',fontsize=10.5,color='#526b7f',linespacing=1.4)
    prefix=args.output_dir/'connes-spectrum';fig.savefig(prefix.with_suffix('.png'),dpi=200,metadata={'Software':'OA-FLOW original deterministic mathematical illustration'});fig.savefig(prefix.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-FLOW original mathematical illustration'});plt.close(fig)
    data={'native_pixels':[3000,2300],'actual_matrix_example':{'h':[0,2,5],'y':'e13','z':'e11','a':'e11','b':'e33','v':'e33','action_and_log_modular_spectrum':spectrum,'connes_spectrum':[0],'positive_S_intersection':['1']},'enclosing_bounds':{'I':['-21/4','-19/4'],'minus_I':['19/4','21/4'],'J':['-1/8','1/8'],'I_minus_I':['-1/2','1/2'],'J_plus_difference':['-5/8','5/8'],'actual_supports':{'y':[-5],'y_star':[5],'z':[0],'v':[0]}},'scope':'Exact finite M3 sample and diagrams of proved general maps; no finite sample is a model of a typeIII factor or numerical proof of an infinite spectral intersection.'}
    (args.output_dir/'connes-spectrum-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':main()

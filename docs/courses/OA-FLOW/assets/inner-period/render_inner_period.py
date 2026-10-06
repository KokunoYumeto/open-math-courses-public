"""Original exact-coordinate illustration of the inner-period proof."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'oa-flow-inner-period-original-20261004'})

def box(ax,x,y,w,h,title,body,size=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008',edgecolor='#68849a',facecolor='#f3f8fc',linewidth=1.3))
    ax.text(x+w/2,y+h-.04,title,ha='center',va='top',fontsize=size+1,color='#19394e')
    ax.text(x+w/2,y+h-.21,body,ha='center',va='top',fontsize=size,color='#365c72',linespacing=1.45)

def cutoff(s):
    # Exact formula: q(t)=exp(-1/t) for t>0, zero otherwise.
    def q(t):
        out=np.zeros_like(t,dtype=float);mask=t>0;out[mask]=np.exp(-1/t[mask]);return out
    n=q(4-s*s);d=n+q(s*s-1);return n/d

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'assets');args=p.parse_args();args.output_dir.mkdir(exist_ok=True,parents=True)
    delta=Fraction(1,16);theta=Fraction(1,64);P=2*np.pi;eta=float(delta)/(2*P)
    fig=plt.figure(figsize=(16,12.5),facecolor='#f7fafc')
    fig.text(.5,.975,'An actual inner modular period from a discrete spectral invariant',ha='center',fontsize=20,color='#19394e')
    fig.text(.5,.946,'A: schematic theorem input. B: analytic cutoff formula. C/D: proved maps. E: exact finite matrix check.',ha='center',fontsize=12,color='#587084')

    a=fig.add_axes([.065,.76,.41,.11]);a.set_facecolor('white')
    for k in [-1,0,1]:
        a.add_patch(Rectangle((k-eta,-.22),2*eta,.44,facecolor='#4384ac',alpha=.55))
        a.scatter([k],[0],marker='D',s=50,color='#267456')
        a.text(k,.32,str(k),ha='center',color='#267456',fontsize=12)
    a.set_xlim(-1.5,1.5);a.set_ylim(-.55,.6);a.set_yticks([]);a.set_xticks([-1.5,-1,-.5,0,.5,1,1.5]);a.grid(axis='x',alpha=.16);a.spines[['top','right','left']].set_visible(False)
    a.set_title('A. A fixed corner with a narrow periodic spectrum',loc='left',fontsize=13,pad=28)
    a.set_xlabel(r'$a=1,\quad P=2\pi,\quad \delta=1/16,\quad \eta=1/(64\pi)$',fontsize=12)
    fig.text(.275,.68,r'$\mathrm{Sp}(\alpha^e)\subseteq\bigcup_{k\in\mathbb{Z}}(k-\eta,k+\eta)$',ha='center',fontsize=14,color='#365c72')
    fig.text(.275,.637,'Diamonds: the assumed group Z. Bands: enclosing intervals, not computed spectra.\nCompactness of one period and directed neighborhoods give the actual corner.',ha='center',fontsize=10.5,color='#587084',linespacing=1.4)

    b=fig.add_axes([.58,.745,.36,.13]);s=np.linspace(-2.4,2.4,1201);chi=cutoff(s);h=(np.exp(1j*float(delta)*s)-1)*chi
    b.axvspan(-.5,.5,color='#4384ac',alpha=.14,label='the spectral band')
    b.axvspan(-1,1,color='#3a8c72',alpha=.10)
    b.plot(s,h.imag/float(delta),color='#4384ac',linewidth=2,label=r'$\mathrm{Im}(h_\delta)/\delta$')
    b.plot(s,h.real/float(delta),color='#ae6848',linewidth=2,label=r'$\mathrm{Re}(h_\delta)/\delta$')
    b.axhline(0,color='#879bac',linewidth=.6);b.set_xlim(-2.4,2.4);b.grid(alpha=.15);b.spines[['top','right']].set_visible(False)
    b.set_title('B. A local symbol, with a global summable filter',loc='left',fontsize=13,pad=26)
    b.set_xlabel(r'$s=\vartheta/\delta;\quad h_\delta(\vartheta)=(e^{i\vartheta}-1)\chi(s)$',fontsize=12)
    b.legend(loc='upper left',fontsize=10,framealpha=.9)
    fig.text(.76,.671,r'$\chi=1\ (|s|\leq1),\quad \sum_n|c_n|\leq Q\delta$',ha='center',fontsize=13,color='#365c72')
    fig.text(.76,.636,'The displayed delta illustrates the formula; the theorem chooses Q delta < 1/10.\nNeither this graph nor sampled coefficients prove that norm inequality.',ha='center',fontsize=10.5,color='#587084',linespacing=1.4)

    c=fig.add_axes([.04,.385,.92,.20]);c.set_axis_off();c.text(.02,1.02,'C. The complete corner: the norm logarithm proves Leibniz before innerness is used',fontsize=13,color='#19394e')
    xs=[.025,.275,.525,.775]
    specs=[(r'$\beta-I=\sum_n c_n\alpha_{nP}^e$',r'$\epsilon\leq Q\delta<1/10$'+'\n'+'normal, norm-convergent maps'),(r'$D=\log\beta$',r'$\|D\|\leq-\log(1-\epsilon)$'+'\n'+r'$D(xy)=D(x)y+xD(y)$'),(r'$D=i[h,\,\cdot\,]$',r'$h=h^*\in eMe$'+'\n'+r'$\|h\|\leq\|D\|/2$'),(r'$u=\exp_{eMe}(ih)$',r'$u^*u=uu^*=e$'+'\n'+r'$\beta(x)=uxu^*$')]
    for x,(title,body) in zip(xs,specs):box(c,x,.30,.205,.56,title,body,size=10.5)
    for i in range(3):
        c.add_patch(FancyArrowPatch((xs[i]+.218,.58),(xs[i+1]-.015,.58),arrowstyle='->',mutation_scale=16,color='#4b7791',linewidth=1.5))
    c.text(.5,.13,r'$\log O\,m=(\log L+\log R)m:\quad O F=\beta F,\ L F(x,y)=F(\beta x,y),\ R F(x,y)=F(x,\beta y)$',ha='center',fontsize=12,color='#365c72')
    c.text(.5,.025,'Commuting bounded operators on the Banach space of bilinear maps supply the actual derivation identity. L35 then constructs h.',ha='center',fontsize=10.5,color='#587084')

    d=fig.add_axes([.045,.075,.46,.24]);d.set_axis_off();d.text(.02,1.02,'D. The whole-factor unitary, with every support',fontsize=13,color='#19394e')
    ds=[.03,.36,.69];titles=[r'$H$',r'$eH$',r'$eH$',r'$H$']
    for x,title in zip([.015,.265,.515,.765],titles):box(d,x,.57,.17,.22,title,'',size=12)
    for i,label in enumerate([r'$v$',r'$u$',r'$\alpha_P(v^*)$']):
        x=.015+.25*i
        d.add_patch(FancyArrowPatch((x+.18,.67),(x+.24,.67),arrowstyle='->',mutation_scale=16,color='#4b7791',linewidth=1.5))
        d.text(x+.21,.86,label,ha='center',fontsize=12,color='#365c72')
    d.text(.5,.42,r'$v^*v=1,\quad vv^*=e,\quad b=\alpha_P(v^*)uv$',ha='center',fontsize=13,color='#365c72')
    d.text(.5,.28,r'$b^*b=bb^*=1,\qquad \alpha_P(x)=bxb^*\quad(x\in M)$',ha='center',fontsize=13,color='#267456')
    d.text(.5,.09,'CT/PC supply e equivalent to 1 in the stated type III factor.\nThe corner exponential has unit e. The final implementer has unit 1.',ha='center',fontsize=11,color='#587084',linespacing=1.45)

    e=fig.add_axes([.56,.078,.40,.235]);e.set_axis_off();e.text(0,1.035,'E. Exact M2 check; all domains are the full algebra',fontsize=13,color='#19394e')
    labels=[['matrix unit','beta multiplier','log beta multiplier'],['e11, e22','1','0'],['e12',r'$e^{-i/64}$',r'$-i/64$'],['e21',r'$e^{i/64}$',r'$i/64$']]
    table=e.table(cellText=labels,cellLoc='center',bbox=[0,.43,1,.45],colWidths=[.33,.33,.34]);table.auto_set_font_size(False);table.set_fontsize(11.5)
    for (row,col),cell in table.get_celld().items():
        cell.set_edgecolor('#a8bbc9');cell.set_facecolor('#e7f0f5' if row==0 else '#fbfdfe')
    e.text(.5,.31,r'$\|\beta-I\|=2\sin(1/128)<1/64<1/10$',ha='center',fontsize=13,color='#365c72')
    e.text(.5,.22,r'$h-\frac{1}{128}I=\mathrm{diag}(-1/128,1/128),\quad \|D\|=1/64$',ha='center',fontsize=12,color='#267456')
    e.text(.5,.025,'Dimension 4 over C. This checks the analytic logarithm step;\nit is not an example of the type III / Gamma=Z hypothesis.',ha='center',fontsize=10.5,color='#587084',linespacing=1.45)
    prefix=args.output_dir/'inner-period';fig.savefig(prefix.with_suffix('.png'),dpi=200,metadata={'Software':'OA-FLOW original deterministic mathematical illustration'});fig.savefig(prefix.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-FLOW original mathematical illustration'});plt.close(fig)
    data={'native_pixels':[3200,2500],'schematic_periodic_band':{'a':'1','P':'2*pi','delta':'1/16','eta':'1/(64*pi)','group':'Z','displayed_centers':[-1,0,1],'bands':'open enclosing intervals; not claimed actual spectral sets'},'cutoff':{'q':'exp(-1/t) if t>0, else0','chi':'q(4-s^2)/(q(4-s^2)+q(s^2-1))','h':'(exp(i*delta*s)-1)*chi(s)','plot_horizontal':'s=theta/delta','plot_vertical':'h/delta','samples':[{'s':float(x),'chi':float(c),'Re_h_over_delta':float(v.real/float(delta)),'Im_h_over_delta':float(v.imag/float(delta))} for x,c,v in zip(s,chi,h)],'formal_bound':'Q*delta with Q=5*C0/pi+(C0+2*C1+2*C2)/pi; theorem separately chooses Q*delta<1/10','no_numerical_admission_claim':True},'exact_matrix_example':{'theta':'1/64','h':['0','1/64'],'centered_h':['-1/128','1/128'],'norm_beta_minus_I':'2*sin(1/128)','norm_D':'1/64','centered_implementer_norm':'1/128','complex_dimension':4,'typeIII':False},'whole_factor_map':{'v':'H->eH, v*v=1,vv*=e','u':'eH->eH,u*u=uu*=e','alphaP_vstar':'eH->H','b':'alpha_P(v*) u v','result':'alpha_P(x)=b x b*'}}
    (args.output_dir/'inner-period-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()

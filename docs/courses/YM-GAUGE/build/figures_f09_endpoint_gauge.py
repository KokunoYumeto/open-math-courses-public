"""Exact symbol, heat-interval and unitary-gauge illustrations. CC0-1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
C=Path(__file__).resolve().parents[1]
def build():
    out=C/'figures';out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
                        'svg.hashsalt':'ym-f09-endpoint-electric-gauge-v1'})
    ink='#18334e';blue='#267b9d';gold='#ae6515'
    data={}
    fig,axes=plt.subplots(1,2,figsize=(12,5.2),gridspec_kw={'width_ratios':[1,1.3]})
    ax=axes[0];ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-.8,1.8);ax.set_ylim(-.8,1.8)
    for dx,dy,label,color in [(1.3,0,r'$\xi=\kappa e_1$',ink),(0,1.3,r'$z=e_2T$',blue),(-.6,-.6,r'$\xi\times z=\kappa e_3T$',gold)]:
        ax.annotate('',xy=(dx,dy),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':3,'color':color})
        ax.text(.2 if dy<0 else dx,-.85 if dy<0 else dy+.14,label,ha='center',color=color)
    ax.set_title('Coordinate directions of the exact symbol',fontsize=15)
    ax.text(.5,-.5,'The Fourier derivative includes i.\nThe displayed axes are a projection.',transform=ax.transAxes,ha='center',fontsize=12)
    ax=axes[1];ax.axis('off')
    ax.text(.02,.93,'All ordered antisymmetric entries',fontsize=17,color=ink)
    table=ax.table(cellText=[['0',r'$i\kappa T$','0'],[r'$-i\kappa T$','0','0'],['0','0','0']],
                   rowLabels=['i = 1','i = 2','i = 3'],colLabels=['j = 1','j = 2','j = 3'],
                   cellLoc='center',bbox=[.15,.43,.8,.4])
    table.auto_set_font_size(False);table.set_fontsize(14)
    for (r,c),cell in table.get_celld().items():
        cell.set_edgecolor('#bacbd5')
        if (r,c) in [(1,1),(2,0)]:cell.set_facecolor('#e3f1f4')
    ax.text(.02,.26,r'$|\xi\times z|^2=\kappa^2m^2$',fontsize=18,color=blue)
    ax.text(.02,.12,r'$\sum_{i,j}|X_{ij}|^2=2\kappa^2m^2$',fontsize=18,color=gold)
    fig.suptitle('EW.5–EW.6: vector curl and the full tensor',color=ink,fontsize=19)
    fig.subplots_adjust(top=.8,bottom=.28,wspace=.25)
    save(fig,out,'f09-endpoint-wave')
    data['endpoint_wave']={'frequency':['kappa',0,0],'amplitude':[0,'T',0],
       'tensor_12':'i*kappa*T','tensor_21':'-i*kappa*T','T_HS_norm':'m','kind':'exact Fourier-symbol diagram; projected coordinate axes'}
    fig,ax=plt.subplots(figsize=(12,4.6));ax.set_xlim(0,3);ax.set_ylim(-.45,1.3);ax.axis('off')
    for i in range(3):
        ax.plot([i,i+1],[.35,.35],lw=8,color=[blue,gold,ink][i],solid_capstyle='butt')
        ax.annotate('',xy=(i+.87,.77),xytext=(i+.13,.77),arrowprops={'arrowstyle':'->','lw':2,'color':[blue,gold,ink][i]})
        ax.text(i+.5,.97,rf'$J_{i}\ \longrightarrow\ J_{i+1}$',ha='center',fontsize=18)
        ax.text(i+.5,-.07,r'gain factor $K\sqrt{6}$',ha='center',fontsize=14)
    for i,label in enumerate([r'$s/2$',r'$2s/3$',r'$5s/6$',r'$s$']):
        ax.plot([i,i],[.25,.45],color=ink,lw=2);ax.text(i,.15,label,ha='center',va='top',fontsize=17)
    ax.text(1.5,-.36,r'$h=s/6,\quad K=2(1+2/\sqrt{\pi}),\quad S_3=K^3(\sqrt{6})^3$',ha='center',fontsize=17)
    fig.suptitle('ES.19–ES.22: three gains on the original heat interval',fontsize=19,color=ink)
    ax.set_title(r'$q=N_q=3,\quad b=c_m=0$ — the zero-coefficient example',fontsize=14,pad=3)
    fig.subplots_adjust(left=.07,right=.93,bottom=.1,top=.77)
    save(fig,out,'f09-electric-smoothing')
    data['electric_smoothing']={'q':3,'N':3,'b':0,'c_m':0,'endpoints':['s/2','2s/3','5s/6','s'],
        'step':'s/6','gain':'K*sqrt(6)','K':'2*(1+2/sqrt(pi))'}
    fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.3),gridspec_kw={'width_ratios':[1,1.2]})
    u=np.linspace(0,2*np.pi,721);theta=np.pi/3
    ax.plot(np.cos(u),np.sin(u),color='#bbc9d2');ax.axhline(0,color='#d9e2e8');ax.axvline(0,color='#d9e2e8')
    for sign,color in [(1,blue),(-1,gold)]:
        v=np.linspace(0,sign*theta,101);ax.plot(np.cos(v),np.sin(v),color=color,lw=3)
        ax.plot([0,np.cos(theta)],[0,sign*np.sin(theta)],color=color,lw=1.5)
        ax.scatter([np.cos(theta)],[sign*np.sin(theta)],color=color)
        ax.text(.64,sign*.98,r'$e^{i\theta}$' if sign==1 else r'$e^{-i\theta}$',color=color,fontsize=18)
    ax.scatter([1],[0],color=ink);ax.text(1.04,.05,'anchor: 1',fontsize=12)
    ax.set_aspect('equal');ax.set_xlim(-1.2,1.65);ax.set_ylim(-1.2,1.2);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part');ax.set_title(r'$\theta=(t-t_*)f(x)$')
    bx.axis('off')
    for y,text in [(.85,r'$f(x)=\omega e^{-|x|^2/L^2},\quad T=\mathrm{diag}(i,-i)$'),
      (.65,r'$a_t=fT,\quad a_i=(t-t_*)\partial_i f\,T$'),(.45,r'$Y_t=fT,\quad Y_i=(t-t_*)\partial_i f\,T$'),
      (.23,r'$A_\mu=Ua_\mu U^{-1}-Y_\mu=0$'),(.06,'Exact flat connection; curvature is zero.')]:
        bx.text(0,y,text,fontsize=16 if y!=.06 else 13,color=ink)
    fig.suptitle('GO.26–GO.31: the anchored gauge in a commuting example',fontsize=19,color=ink)
    fig.subplots_adjust(left=.08,right=.97,bottom=.18,top=.82,wspace=.3)
    save(fig,out,'f09-physical-gauge')
    data['physical_gauge']={'T':'diag(i,-i)','f':'omega*exp(-|x|^2/L^2)','sample_theta':'pi/3','sample_x':[0,0,0],
      'sample_time':'(t-t*)*omega=pi/3','connection':'exact flat physical connection; separate from upper heat boundary construction'}
    (out/'f09-endpoint-gauge-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def save(fig,out,name):
    fig.savefig(out/(name+'.svg'),metadata={'Date':None},bbox_inches='tight',pad_inches=.2)
    fig.savefig(out/(name+'.png'),dpi=140,metadata={'Software':'YM-GAUGE reproducible figure builder'},bbox_inches='tight',pad_inches=.2)
    plt.close(fig)
if __name__=='__main__':build()

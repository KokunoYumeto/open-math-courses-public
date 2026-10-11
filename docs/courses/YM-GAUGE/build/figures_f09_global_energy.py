"""Reproducible finite-cover diagram for GE.11–GE.15."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def build():
    root=Path(__file__).resolve().parents[1];out=root/'figures'
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'ym-f09-ge'})
    fig,(top,ax)=plt.subplots(2,1,figsize=(13,9),gridspec_kw={'height_ratios':[1,2.3]})
    fig.patch.set_facecolor('#f7f9fc')
    top.set_axis_off();top.set_xlim(0,1);top.set_ylim(0,1)
    top.text(.03,.92,'One original sequence, compatible limits',fontsize=20,weight='bold',color='#173350')
    for x,head,body in [
        (.03,'Original constrained data',r'$U_{*,n}\longrightarrow U_*$'),
        (.36,'Global regular curves',r'$(A_n^0,E_n^0)$ on every $I_H$'),
        (.69,'One global energy solution',r'$(A^0,E^0)$; the same limit on overlaps')]:
        top.add_patch(Rectangle((x,.21),.28,.49,facecolor='#e6eef8',edgecolor='#40739c',lw=1.5))
        top.text(x+.14,.56,head,ha='center',fontsize=11,weight='bold')
        top.text(x+.14,.34,body,ha='center',fontsize=11)
    for x in [.315,.645]:top.annotate('',xy=(x+.035,.45),xytext=(x,.45),arrowprops={'arrowstyle':'->','lw':2})
    ax.set_title('Exact sample cover: '+r'$H=3\ell/c,\ \tau_H=2\ell/(3c),\ N_H=9,\ \delta_H=\ell/(3c)$',pad=15)
    rows=[]
    H=3.;d=1/3
    for k in range(9):
        for eps in [-1,1]:
            a=eps*k*d;z=eps*(k+1)*d
            left=max(-H,min(a,z)-d/2);right=min(H,max(a,z)+d/2)
            colour='#cb6d35' if eps<0 else '#277c79'
            ax.plot([left,right],[k,k],lw=12,alpha=.65,color=colour,solid_capstyle='butt')
            ax.plot(a,k,'o',color='#173350',ms=5)
            rows.append({'direction':eps,'k':k,'left_display':left,'right_display':right,'anchor_display':a})
    ax.axvline(0,color='#697989',lw=1)
    ax.set_xlim(-3.2,3.2);ax.set_ylim(8.65,-.65)
    ax.set_yticks(range(9),[str(k) for k in range(9)])
    ax.set_ylabel(r'Cell index $k$ in each direction')
    ax.set_xlabel(r'Display coordinate $c(t-t_*)/\ell$; dot = actual anchor',labelpad=12)
    ax.grid(axis='x',alpha=.2)
    fig.text(.07,.035,r'GE.15: separate global suprema are bounded by  $2\max(1,C_H^{\rm loc})^{N_H}e_{nm}$.'
             '\nThe bars are comparison intervals, not computed field trajectories.',fontsize=11)
    fig.subplots_adjust(left=.08,right=.97,top=.97,bottom=.18,hspace=.24)
    fig.savefig(out/'f09-global-energy-data.svg',metadata={'Date':None})
    fig.savefig(out/'f09-global-energy-data.png',dpi=150)
    plt.close(fig)
    (out/'f09-global-energy-cover.json').write_text(json.dumps({'proof':'GE.11–GE.15','display_coordinate':'c(t-t*)/ell','H':'3 ell/c','tau':'2 ell/(3c)','N':9,'intervals':rows},indent=2)+'\n',encoding='utf8')

if __name__=='__main__':build()

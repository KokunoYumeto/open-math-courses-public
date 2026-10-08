"""Original illustration of the terminal nested integer comparison. CC0."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import terminal_integer_endpoints as cert

def draw(output):
    table=cert.certificate()['table']
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,(nodes,margins)=plt.subplots(1,2,figsize=(15.2,6.2),gridspec_kw={'width_ratios':[1.15,1]},layout='constrained')
    fig.suptitle('Terminal integer zeros: retain the full interval and trim its extra jets',fontsize=17,fontweight='bold')
    rb=25;r0=24;x=np.arange(-rb,rb+1)
    blue='#2478a8';orange='#d57822';ink='#243449'
    for level in [2,1]:
        nodes.plot([-rb,rb],[level,level],color='#bbc5d0',linewidth=2,zorder=1)
    nodes.scatter(x,np.full(x.shape,2),s=22,c=orange,zorder=3)
    nodes.scatter(x,np.full(x.shape,1),s=np.where(np.abs(x)<=r0,22,50),
                  c=np.where(np.abs(x)<=r0,orange,blue),zorder=3)
    nodes.text(0,2.24,'Uniform multiplicity 2: 51 nodes, 102 conditions',ha='center',color=ink)
    nodes.text(0,1.24,'49 inner nodes of multiplicity 2; two outer nodes of multiplicity 1',ha='center',color=ink,fontsize=10)
    nodes.annotate(r'$R_0=24$',xy=(24,1),xytext=(15,.48),arrowprops={'arrowstyle':'->','color':ink},ha='center')
    nodes.annotate(r'$-R_0=-24$',xy=(-24,1),xytext=(-15,.48),arrowprops={'arrowstyle':'->','color':ink},ha='center')
    nodes.text(0,-.12,r'$N_*=2R_b+2R_0+2=100$',ha='center',fontsize=14,color=ink)
    nodes.text(0,-.44,r'$(98/25)R_b<N_*\leq(98/25)R_b+2$',ha='center',fontsize=13,color=ink)
    nodes.text(0,-.74,'Outer cardinal loss: one separation factor, included in the input budget',ha='center',fontsize=10,color=ink)
    nodes.set(ylim=(-1.05,2.6),xlim=(-27,27),xticks=[-25,-12,0,12,25],yticks=[],xlabel='Integer node s (illustration: radius 25; actual stages have radius >231)')
    nodes.set_title('Exact nested Hermite conditions',fontweight='bold',pad=14)
    for spine in ['left','right','top']:nodes.spines[spine].set_visible(False)
    labels=['I.1','I.2','II','III.1','III.2','IV, first prime','IV, larger prime','V']
    y=np.arange(len(table))
    inputs=[row['input_lower_per_1000']/1000 for row in table]
    masses=[row['mass_lower_per_1000']/1000 for row in table]
    margins.scatter(inputs,y-.12,color=blue,s=60,label=r'Input margin $c_1-P_r$',zorder=4)
    margins.scatter(masses,y+.12,color=orange,s=60,marker='s',label=r'Arithmetic margin $G_r-C_r$',zorder=4)
    for k,(im,mm) in enumerate(zip(inputs,masses)):
        margins.text(im+.018,k-.12,f'{int(round(im*1000))}/1000',va='center',fontsize=9,color=blue)
        margins.text(mm+.018,k+.12,f'{int(round(mm*1000))}/1000',va='center',fontsize=9,color=orange)
    margins.axvline(0,color=ink,linewidth=1)
    margins.set(xlim=(-.015,1.03),yticks=y,yticklabels=labels,xlabel='Proved strict lower bound, including every precision cost')
    margins.invert_yaxis();margins.grid(axis='x',alpha=.22)
    margins.set_title('Every original case and every rank',fontweight='bold',pad=14)
    margins.legend(loc='lower center',bbox_to_anchor=(.5,-.28),ncol=1,frameon=False,fontsize=11)
    for spine in ['right','top']:margins.spines[spine].set_visible(False)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,dpi=175,facecolor='white');plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('terminal-integer-profile.png'))
    draw(p.parse_args().output)

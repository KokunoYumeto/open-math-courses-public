"""Reproduce the coordinate cancellation for the l1 left-shift equation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'AN02-L205-shift-cancellation','font.family':'DejaVu Sans'})

def main():
    fig,ax=plt.subplots(figsize=(11,5.6),dpi=170)
    fig.patch.set_facecolor('white')
    ax.set_xlim(-2.15,6.6);ax.set_ylim(-.85,4.9);ax.axis('off')
    labels=[r'$f(z)$',r'$Lf(z)$',r'$zf(z)$',r'$(L-zI)f(z)$']
    rows=[[r'$0$',r'$1$',r'$z$',r'$z^2$',r'$z^3$',r'$\cdots$'],
          [r'$1$',r'$z$',r'$z^2$',r'$z^3$',r'$z^4$',r'$\cdots$'],
          [r'$0$',r'$z$',r'$z^2$',r'$z^3$',r'$z^4$',r'$\cdots$'],
          [r'$1$',r'$0$',r'$0$',r'$0$',r'$0$',r'$\cdots$']]
    colors=['#dfeefb','#e6f1e4','#fff0d6','#e8e5f5']
    for j in range(5):
        ax.text(j+.42,4.3,str(j),ha='center',fontsize=12,color='#4b5563')
    ax.text(5.42,4.3,r'$\cdots$',ha='center',fontsize=14,color='#4b5563')
    ax.text(-1.4,4.3,'coordinate',ha='center',fontsize=12,color='#4b5563')
    for k,(label,row,color) in enumerate(zip(labels,rows,colors)):
        y=3.3-k
        ax.text(-.2,y+.35,label,ha='right',va='center',fontsize=17)
        for j,item in enumerate(row):
            ax.add_patch(Rectangle((j,y),.84,.72,facecolor=color,edgecolor='#a3acb8',linewidth=.8))
            ax.text(j+.42,y+.35,item,ha='center',va='center',fontsize=18)
    ax.plot([-.05,5.9],[1.12,1.12],color='#4b5563',lw=1.2)
    ax.text(-1.42,1.63,'subtract',ha='center',va='center',fontsize=11,color='#7c5200')
    ax.text(2.8,-.68,r'$|z|<1:\quad \|f(z)\|_1=\sum_{n=0}^{\infty}|z|^n=(1-|z|)^{-1}$',ha='center',fontsize=17)
    fig.suptitle('An analytic lift for the left-shift equation',fontsize=19,y=.965)
    fig.subplots_adjust(left=.035,right=.98,bottom=.09,top=.87)
    out=HERE/'figures';out.mkdir(exist_ok=True)
    fig.savefig(out/'shift-and-geometric-lift.png',dpi=170,metadata={'Software':'Matplotlib; GPT-6.1 Sol (OpenAI)'})
    fig.savefig(out/'shift-and-geometric-lift.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI); Matplotlib'})
    svg=out/'shift-and-geometric-lift.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

if __name__=='__main__':main()

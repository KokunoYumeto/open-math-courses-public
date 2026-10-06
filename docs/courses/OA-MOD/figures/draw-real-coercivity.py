"""Reproduce the exact two-dimensional compression in RC.6–7. CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def draw(destination):
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    fig,axes=plt.subplots(2,1,figsize=(4.5,7.8),layout='constrained')
    plt.rcParams['svg.fonttype']='path'
    plt.rcParams['svg.hashsalt']='oa-mod-real-coercivity-v1'
    for ax,base,result,title,signed in [
        (axes[0],(1,0),(1,1/3),r'$Ae=e+\frac{1}{3}f$',r'$(Ae,f)_{\mathbb{R}}=+\frac{1}{3}$'),
        (axes[1],(0,1),(-1/3,1),r'$Af=f-\frac{1}{3}e$',r'$(Af,e)_{\mathbb{R}}=-\frac{1}{3}$')]:
        ax.set_aspect('equal');ax.set_xlim(-.65,1.45);ax.set_ylim(-.32,1.48)
        ax.axhline(0,color='#ced7dc',lw=1);ax.axvline(0,color='#ced7dc',lw=1)
        for end,label,offset in [((1,0),'e',(.04,-.1)),((0,1),'f',(.05,.04))]:
            ax.add_patch(FancyArrowPatch((0,0),end,arrowstyle='-|>',mutation_scale=14,color='#7c8792',lw=1.5))
            ax.text(end[0]+offset[0],end[1]+offset[1],label,color='#526171',fontsize=12)
        ax.add_patch(FancyArrowPatch((0,0),result,arrowstyle='-|>',mutation_scale=17,color='#075c89',lw=2.5))
        ax.add_patch(FancyArrowPatch(base,result,arrowstyle='-|>',mutation_scale=13,color='#bf5b26',lw=1.8,linestyle='--'))
        ax.text(result[0]+.05,result[1]+.03,'Ae' if ax is axes[0] else 'Af',fontsize=13,color='#075c89')
        ax.set_title(title,fontsize=17,pad=10)
        ax.text(.5,-.1,signed,transform=ax.transAxes,ha='center',fontsize=14)
        ax.set_xticks([]);ax.set_yticks([])
        for spine in ax.spines.values():spine.set_visible(False)
    for extension in ['svg','png']:
        fig.savefig(destination/f'real-coercivity.{extension}',dpi=180,facecolor='white',metadata={'Creator':'OpenAI Codex; reproducible exact-coordinate illustration','Date':None} if extension=='svg' else None)
    plt.close(fig)

if __name__=='__main__':draw(Path(__file__).resolve().parent)

from pathlib import Path
import hashlib, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'svg.hashsalt':'borel-functor-obstruction-20261005'})
fig=plt.figure(figsize=(16,11),dpi=125,facecolor='#fbfcfe')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.055,.945,'A lost measure scale prevents an unrestricted functor',fontsize=27,weight='bold',color='#13243b')
ax.text(.055,.895,'Exact categorical schematic for BO.1–BO.13; no quotient geometry is implied.',fontsize=16,color='#45566d')

def box(x,y,w,h,text,color='#e9f0fb',edge='#315885',fontsize=20):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.016',
                               facecolor=color,edgecolor=edge,linewidth=2))
    ax.text(x,y,text,ha='center',va='center',fontsize=fontsize,color='#14273e',linespacing=1.5)
def arrow(start,end,color='#315885',style='-'):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=22,
                                color=color,linewidth=2.6,linestyle=style))

box(.155,.72,.22,.12,'S with λ\nλ(S) = 1')
box(.155,.49,.22,.12,'S with 2λ\n(2λ)(S) = 2')
box(.52,.605,.265,.18,'Q = S / E\nSame Λ∞ for both inputs',fontsize=18)
box(.865,.605,.17,.18,'Point *\nOne output mass?',color='#fff0ee',edge='#b64336',fontsize=18)
arrow((.28,.715),(.365,.65));arrow((.28,.495),(.365,.565))
ax.text(.325,.745,'q',fontsize=24,ha='center',color='#315885')
ax.text(.325,.455,'q',fontsize=24,ha='center',color='#315885')
ax.text(.325,.603,'proper\npushforward',fontsize=15,ha='center',va='center',color='#315885')
arrow((.67,.605),(.758,.605),color='#b64336',style='--')
ax.text(.72,.695,'c',fontsize=24,ha='center',color='#b64336')
ax.text(.72,.78,'weakly Borel\nextension sought',fontsize=15,ha='center',va='center',color='#b64336')

ax.text(.055,.355,'Why the two middle measures are exactly equal',fontsize=21,weight='bold',color='#13243b')
ax.text(.065,.30,'For every Borel B ⊂ S and every a > 0:',fontsize=18,color='#13243b')
ax.text(.065,.245,'(q∗(aλ))(B, q) = 0 if λ(B) = 0;  ∞ if λ(B) > 0.',fontsize=21,color='#315885')
ax.text(.065,.196,'BO.3 proves the ergodic integral; BO.4 extends equality to every countable presentation.',fontsize=16,color='#45566d')

ax.plot([.055,.945],[.158,.158],color='#c5d1de',lw=1.5)
ax.text(.055,.105,'Functoriality would force the same mass to equal both 1 and 2.',fontsize=22,weight='bold',color='#a3352b')
ax.text(.055,.052,'The ordinary composite c q has mass 1 on λ and mass 2 on 2λ.  No extension of c can satisfy both.',fontsize=16,color='#45566d')
for ext in ['png','svg']:
    fig.savefig(HERE/('borel-functor-obstruction.'+ext),dpi=125,
                metadata={'Creator':'GPT-6.1 Sol (OpenAI)', **({'Date':None} if ext=='svg' else {})})
plt.close(fig)
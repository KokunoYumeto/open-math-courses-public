"""Original-period cancellation slice and exact original velocity margins."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
R=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,2,figsize=(14,7));fig.subplots_adjust(left=.04,right=.98,bottom=.21,top=.86,wspace=.22)
fig.suptitle('Cancellation in the original periodic projection',fontsize=21,color='#163f51')
ax=axs[0];ax.set_aspect('equal');ax.set_xlim(0,12);ax.set_ylim(0,12)
ax.add_patch(Rectangle((0,0),12,12,fill=False,lw=1.5))
ax.add_patch(Circle((6,6),2*np.sqrt(3),color='#e8f3f7',ec='#32738c'))
ax.add_patch(Rectangle((5.5,5.5),1,1,color='#ddac4c',alpha=.7))
ax.plot([6,11],[6,6],color='#874048',lw=1.3)
ax.scatter([6,6.5,11],[6,6.5,6],c=['#163f51','#996012','#874048'],s=36,zorder=5)
ax.text(5.1,5,'B',fontsize=13);ax.text(5.6,6.9,r'$c_B$',fontsize=13)
ax.text(6.8,6.7,'y',fontsize=13);ax.text(11,6.6,'x',fontsize=13)
ax.text(8.2,5.4,r'$r=5$',fontsize=13)
ax.text(6,2.05,r'$B^*: R=2\sqrt{3}\ell_B$',ha='center',fontsize=13)
ax.set_xlabel('Original spatial coordinate x₁');ax.set_ylabel('Original spatial coordinate x₂')
ax.set_title('Central slice x₃=6; L=12, ℓB=1',fontsize=13)
ax=axs[1];ax.axis('off')
lines=[
 ('The original three-dimensional geometry',15),
 (r'$|y-c_B|\leq\sqrt{3}\ell_B/2<r/4$',18),
 (r'$d(x-y,0)\geq 3r/4$',18),
 ('Zero integral of the actual local remainder',15),
 (r'$\int_B b_B=0$',18),
 (r'$Qb_B(x)=\int_B[K(x-y)-K(x-c_B)]b_B(y)\,dy$',12),
 ('The proved kernel gradient retains the distance',15),
 (r'$|DK(x)|\leq H_1d(x,0)^{-4}$',18),
 (r'$\int_{(B^*)^c}|Qb_B|\leq \pi H_1(4/3)^4\|b_B\|_1$',16)]
for i,(txt,fs) in enumerate(lines):ax.text(.5,.97-i*.108,txt,ha='center',va='top',fontsize=fs,transform=ax.transAxes)
fig.text(.5,.065,'PL7–PL16 give the complete periodic kernel and cancellation proof. The left image is a central slice of the stated 3D cube and ball.\nHuman receiver: Buckmaster–Vicol, arXiv:1709.10033v4, temporal velocity correction. No unproved endpoint projection bound is used.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-periodic-projection-cancellation.{ext}',dpi=150,facecolor='white')
plt.close(fig)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.34,right=.96,bottom=.22,top=.86)
ns=np.arange(4);b=512
offsets=[(3/8,6),(11/8,21),(9/16,6),(3/8,11),(3/2,26)]
labels=['Principal field','Curl: amplitude gradient','Curl: intermittent gradient','Temporal: main input','Temporal: extra spatial derivative']
values=np.array([b*(const+7*ns/16)-power for const,power in offsets])
ax.imshow(values,cmap='Blues',vmin=0,vmax=1900,aspect='auto')
for i in range(5):
    for j in range(4):ax.text(j,i,str(int(values[i,j])),ha='center',va='center',fontsize=20,color='white' if values[i,j]>1100 else '#102e3d')
ax.set_xticks(ns);ax.set_xticklabels(['N=0','N=1','N=2','N=3'],fontsize=13)
ax.set_yticks(np.arange(5));ax.set_yticklabels(labels,fontsize=12)
ax.set_xlabel('Full space-time derivative order',fontsize=12,labelpad=10)
fig.suptitle('Exact positive exponents for all five velocity costs',fontsize=21,color='#163f51')
fig.text(.5,.065,'Every entry is the exact dₙ,ₛ of VD21 at the source b=512. Each complete term is Uₙ,ₛ λq⁻ᵈ.\nVD22 constructs one finite base so the five contributions sum to at most 1/2 for every stated derivative order.\nHuman source: Buckmaster–Vicol, arXiv:1709.10033v4, original velocity proposition.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-velocity-derivative-margins.{ext}',dpi=150,facecolor='white')

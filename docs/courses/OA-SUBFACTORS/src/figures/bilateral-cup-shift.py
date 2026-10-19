"""Physical two-step shift and its exact cup-error mechanism. CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(8,12.5));fig.subplots_adjust(0,0,1,1);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ink='#15344a';blue='#edf5fc';green='#eaf5ee';orange='#fff2dd'
def box(x,y,w,h,fc):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',fc=fc,ec=ink,lw=1.2))
def label(x,y,t,size=12,weight='normal',ha='center'):
 ax.text(x,y,t,ha=ha,va='center',fontsize=size,color=ink,weight=weight,linespacing=1.6)
def arrow(a,b):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.5,color=ink))
label(.5,.969,'A forward shift with the physical trace',17,'bold')
label(.5,.94,r'$e_k\in M_{k+1},\quad d=[M:N]>1,\quad\lambda=d^{-1}$',13)
box(.045,.615,.91,.285,blue)
label(.5,.873,'1. Retain the full supported matrix corner',14,'bold')
label(.5,.834,r'$\Phi_{ij}:f\operatorname{Mat}_q(M_j)f\ \longrightarrow\ M_{j+2}$',14)
label(.5,.799,r'$\tau(\Phi_{ij}(x))=\lambda\sum_r\tau(x_{rr}),\quad\sum_r\tau(p_r)=d$',13)
label(.23,.738,r'$A_{ij}$',16);label(.76,.738,r'$A_{i+2,j+2}$',16)
label(.23,.656,r'$A_{i-1,j+1}$',16);label(.76,.656,r'$A_{i+1,j+3}$',16)
arrow((.35,.738),(.63,.738));arrow((.35,.656),(.63,.656))
arrow((.23,.719),(.23,.678));arrow((.76,.719),(.76,.678))
label(.495,.76,r'$\theta$',14);label(.495,.679,r'$\theta$',14)
label(.5,.704,'both index inclusions commute',11)
box(.045,.265,.91,.31,green)
label(.5,.548,'2. The same cup preserves the error',14,'bold')
label(.5,.512,r'$x\in R_j,\quad[x,e_k]=0\ (k\leq j-1)$',13)
label(.5,.477,r'$\theta(x)e_{j+1}=x e_{j+1}$',16)
label(.5,.441,r'$z\in\{e_k:k\in\mathbb{Z}\}^{\prime}\cap\mathcal{R}$',13)
label(.5,.402,r'$\|(z-x)e_{j+1}\|_2^2=\lambda\|z-x\|_2^2$',13)
label(.5,.37,r'$\|(z-\theta(x))e_{j+1}\|_2^2=\lambda\|z-\theta(x)\|_2^2$',13)
label(.5,.326,'right half-cup factor       left half-cup factor',11)
label(.5,.287,r'$\|z-\theta^n(x)\|_2=\|z-x\|_2$',15)
box(.045,.063,.91,.16,orange)
label(.5,.199,'3. Mix, approximate, and specialize',14,'bold')
label(.5,.164,r'$2\|E_{R_j}(z)\|_2^2\leq4\|z-E_{R_j}(z)\|_2^2\ \longrightarrow\ 0$',13)
label(.5,.128,r'$\tau(z)=0\ \Longrightarrow\ z=0$',14)
label(.5,.09,r'$R_0=M\ \Longrightarrow\ \mathcal{R}=T,\quad\theta(M_j)=M_{j+2}$',13)
label(.5,.029,'PH.25–PH.28 • No extremality assumption • Zero return remains unresolved',10)
p=Path(__file__).with_suffix('');fig.savefig(p.with_suffix('.svg'));fig.savefig(p.with_suffix('.png'),dpi=200);plt.close(fig)
svg=p.with_suffix('.svg');svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')

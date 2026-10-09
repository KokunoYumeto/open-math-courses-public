from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans', 'mathtext.fontset':'dejavusans'})
fig, ax = plt.subplots(figsize=(15,12), dpi=150)
ax.set(xlim=(0,15),ylim=(0,12))
ax.axis('off')
ink='#17324d'
blue='#e7f0f8'
orange='#b66519'
def box(x,y,w,h,label,face=blue,edge=ink,size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.13',
                              facecolor=face,edgecolor=edge,linewidth=1.4))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size,color=ink)
def arrow(a,b,label='',dash=False,above=0.14,size=12):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,
                               linewidth=1.5,color=orange if dash else ink,
                               linestyle='--' if dash else '-'))
    ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+above,label,ha='center',va='bottom',
            fontsize=size,color=orange if dash else ink)
ax.text(.2,11.7,'From a Lie module to the two actual flag-bundle maps',
        fontsize=21,weight='bold',color=ink)
ax.text(.2,11.23,r'All ranks; actual torus characters. Solid arrows are proved at G.0 root hypotheses.',
        fontsize=12,color=ink)

ax.text(.2,10.63,'1  Integration: torus loops control the descent',fontsize=16,weight='bold',color=ink)
box(.3,8.95,3.7,1.3,r'$F_\mu$ from H.5'+'\n'+r'$\mu\in X^*(T),\ \mu(h_i)\geq0$')
box(5.1,8.95,4.3,1.3,r'$\Omega=U_-\times T\times U_+$'+'\n'+r'$\pi_1(\Omega)\twoheadrightarrow\pi_1(G)$')
box(10.5,8.95,4.0,1.3,r'$R:G\longrightarrow\mathrm{GL}(F_\mu)$'+'\nactual algebraic representation')
arrow((4.15,9.6),(4.93,9.6),'G.1–G.3',above=.22,size=11)
arrow((9.55,9.6),(10.35,9.6),'G.4',above=.22,size=11)
ax.text(7.2,8.40,'Integral characters kill torus monodromy; root exponentials are finite polynomials.',
        ha='center',fontsize=12,color=ink)

ax.plot([.2,14.7],[7.99,7.99],color='#bacbda',linewidth=1)
ax.text(.2,7.59,'2  Geometry: the regular highest line embeds the whole flag',fontsize=16,weight='bold',color=ink)
box(.3,6.10,4.1,1.03,r'$\mu_0=2\rho\in\mathbb{Z}\Phi$'+'\n'+r'$\mu_0(h_i)=2$ for every simple root')
box(5.45,6.10,3.8,1.03,r'$X=G/B\hookrightarrow\mathbb{P}(F_{\mu_0})$'+'\nclosed highest-line orbit',size=13)
box(10.3,6.10,4.2,1.03,r'$A=\mathcal{L}(-2\rho)$'+'\npullback of '+r'$\mathcal{O}(1)$'+': very ample')
arrow((4.55,6.61),(5.30,6.61),'G.8',above=.21,size=11)
arrow((9.40,6.61),(10.15,6.61),'G.9',above=.21,size=11)
ax.text(7.2,5.61,r'Principal charts: $G|_{X_0}\simeq U_-\times B$; root curve degree is $\mu(h_i)$.',
        ha='center',fontsize=12,color=ink)

ax.plot([.2,14.7],[5.22,5.22],color='#bacbda',linewidth=1)
ax.text(.2,4.80,'3  G.10: both maps tensor naturally with every ordinary coefficient sheaf E',
        fontsize=15,weight='bold',color=ink)
box(.3,3.45,6.6,.9,r'$\mathcal{O}_X\hookrightarrow A^N\otimes F_{N\mu_0}$',
    face='#edf5e7',size=17)
box(7.9,3.45,6.6,.9,r'$\mathcal{O}_X\otimes F_{-w_0N\mu_0}\twoheadrightarrow A^N$',
    face='#edf5e7',size=16)
box(.3,1.84,6.6,.95,r'$E\hookrightarrow(E\otimes A^N)\otimes F_{N\mu_0}$',
    face='#edf5e7',size=16)
box(7.9,1.84,6.6,.95,r'$E\otimes F_{-w_0N\mu_0}\twoheadrightarrow E\otimes A^N$',
    face='#edf5e7',size=15)
arrow((3.6,3.30),(3.6,2.94),'tensor E',above=.0,size=11)
arrow((11.2,3.30),(11.2,2.94),'tensor E',above=.0,size=11)
ax.text(.35,1.31,'Locally free quotients make these maps exact even for nonflat E.',
        fontsize=12,color=ink)
ax.text(.35,.91,'Naturality holds for every O-linear coefficient map; global O-linear splitting is not claimed.',
        fontsize=12,color=ink)
ax.text(7.4,.41,'For TDO coefficients: central-character uniqueness + scalar action are still pending (§G.11).',
        ha='center',fontsize=12,color=orange,weight='bold')
fig.savefig(OUT/'bb-integration-and-two-bundle-maps.png',bbox_inches='tight',facecolor='white')
fig.savefig(OUT/'bb-integration-and-two-bundle-maps.svg',bbox_inches='tight',facecolor='white')
plt.close(fig)
print(str(OUT/'bb-integration-and-two-bundle-maps.png'))

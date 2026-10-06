"""Reproduce the exact dual-map square, DT1--DT8. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,6.3))
fig.patch.set_facecolor('#fbfcfe');ax.set_facecolor('#fbfcfe')
ax.set_xlim(0,12);ax.set_ylim(0,6.3);ax.axis('off')
ink='#17324d'; blue='#17658b'; amber='#a75d10'
ax.text(6,5.98,'One operator, two exact test evaluations',ha='center',va='center',fontsize=18,color=ink,weight='bold')
def box(x,y,title,formula):
    ax.add_patch(FancyBboxPatch((x,y),3.5,1.05,boxstyle='round,pad=0.12',facecolor='#eaf3f9',edgecolor=blue,lw=1.6))
    ax.text(x+1.75,y+.73,title,ha='center',va='center',fontsize=12,color=ink)
    ax.text(x+1.75,y+.30,formula,ha='center',va='center',fontsize=15,color=ink)
box(.65,4.13,'Vector tests',r'$v\in F$')
box(7.85,4.13,'Vector tests',r'$B^*v\in E$')
box(.65,1.84,'Linear dual-density tests',r'$\phi\in F^*\otimes\Omega_X$')
box(7.85,1.84,'Linear dual-density tests',r'$B^{\mathrm{t}}\phi\in E^*\otimes\Omega_X$')
def arrow(start,end):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',lw=2.2,color=blue,shrinkA=4,shrinkB=4))
arrow((4.3,4.66),(7.7,4.66));ax.text(6,4.9,r'$B^*$',ha='center',fontsize=17,color=ink)
arrow((4.3,2.36),(7.7,2.36));ax.text(6,2.60,r'$B^{\mathrm{t}}=\iota_E B^*\iota_F^{-1}$',ha='center',fontsize=16,color=ink)
arrow((2.4,4),(2.4,3.02));arrow((9.6,4),(9.6,3.02))
ax.text(2.14,3.52,r'$\iota_F$',ha='right',va='center',fontsize=18,color=amber)
ax.text(9.34,3.52,r'$\iota_E$',ha='right',va='center',fontsize=18,color=amber)
ax.text(6,3.52,r'$\iota_E(w)(z)=h_E(z,w)\mu$',ha='center',va='center',fontsize=16,color=ink)
ax.text(6,1.25,r'$B_\mu=\mu^{-1/2}\mathbf{B}\mu^{1/2}$'
        '     '+r'$B_\mu^*=\mu^{-1/2}\mathbf{B}^*\mu^{1/2}$',ha='center',fontsize=14,color=ink)
ax.text(6,.70,r'$B=iI:\quad B^{\mathrm{t}}=iI,\quad B^*=-iI$'
        '     '+r'$U_{\mathrm{H}}(v)=U_{\mathrm{L}}(\iota_Ev)$',ha='center',fontsize=15,color=ink)
ax.text(6,.23,'DT1–DT8: both vertical maps are conjugate-linear; their composite transpose is linear.',ha='center',fontsize=11,color=ink)
fig.subplots_adjust(left=.015,right=.985,bottom=.015,top=.985)
for suffix in ['png','svg']:
    fig.savefig(root/('linear-and-hermitian-duals.'+suffix),dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)

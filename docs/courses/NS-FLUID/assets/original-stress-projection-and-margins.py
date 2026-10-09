"""Exact original stress example and all five original parameter margins."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(14,6.2))
fig.subplots_adjust(left=.05,right=.95,bottom=.27,top=.77,wspace=.3)
M=np.array([[2,1,3],[1,-1,4],[3,4,-1]])
TM=np.array([[0,0,3],[0,0,4],[3,4,0]])
assert np.sum(M*M)==58 and np.sum(TM*TM)==50 and np.sum((M-TM)**2)==8
for ax,A,title,norm in zip(axs,[M,TM,M-TM],
 ['Original coefficient M','Selected coefficient T M','Removed coefficient M − T M'],
 [r'$\|\widetilde{S}\|_2^2=29V$',r'$\|\mathcal{T}\widetilde{S}\|_2^2=25V$',r'$\|(I-\mathcal{T})\widetilde{S}\|_2^2=4V$']):
    ax.imshow(A,cmap='RdBu_r',vmin=-4,vmax=4)
    for i in range(3):
        for j in range(3):
            ax.text(j,i,str(A[i,j]),ha='center',va='center',fontsize=25,
                    color='white' if abs(A[i,j])>=3 else '#153745')
    ax.set_xticks([0,1,2],['1','2','3']);ax.set_yticks([0,1,2],['1','2','3'])
    ax.set_xlabel(norm,fontsize=16,labelpad=15);ax.set_title(title,fontsize=13,pad=13)
fig.suptitle('The exact stress projection and its pressure correction',fontsize=21,color='#163f51',y=.96)
fig.text(.5,.845,r'$\widetilde{S}(x)=M\cos(x_3),\quad L=2\pi,\quad V=(2\pi)^3,\quad k=e_3,\quad \chi_{\widetilde{S}}=-\cos(x_3)$',
 ha='center',fontsize=16)
fig.text(.5,.125,r'$\operatorname{div}\widetilde{S}=-(3,4,-1)\sin(x_3),\quad'
 r'\operatorname{div}\mathcal{T}\widetilde{S}=-(3,4,0)\sin(x_3),\quad'
 r'\nabla\chi_{\widetilde{S}}=(0,0,1)\sin(x_3)$',ha='center',fontsize=13)
fig.text(.5,.055,'SM1–SM6 and EX1–EX3 prove the full map, pressure identity and orthogonal square-norm decomposition.\nHuman comparison: Buckmaster–Vicol, arXiv:1709.10033v4, original stress corollary.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-stress-projection.{ext}',dpi=150,facecolor='white')
plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1.2,1]})
fig.subplots_adjust(left=.07,right=.97,bottom=.25,top=.84,wspace=.36)
bs=np.arange(512,1249,16,dtype=float);d3=bs/16-60-41/512;d5=159/16
ax=axs[0]
ax.plot(bs,d3,color='#3b86a4',lw=1.5,label=r'$d_3=b/16-60-41/512$')
ax.axhline(d5,color='#ab7745',lw=1.5,label=r'$d_5=159/16$')
ax.plot(bs,np.minimum(d3,d5),'o',ms=3,color='#163f51',label=r'$d(b)=\min_j d_j$')
ax.axhline(0,color='#808080',lw=1);ax.axvline(960,color='#aaa',lw=.8,ls='--')
for xx,yy,txt,xytext in [(512,512/16-60-41/512,'512: negative margin',(565,-26)),
 (976,471/512,r'$976:\ 471/512$',(610,-3)),
 (1024,2007/512,r'$1024:\ 2007/512$',(875,14))]:
    ax.scatter([xx],[yy],s=40,color='#a24348',zorder=5)
    ax.annotate(txt,(xx,yy),xytext=xytext,fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#7d5258'})
ax.set_xlim(490,1270);ax.set_ylim(-33,20);ax.set_xticks([512,768,960,1024,1248])
ax.set_xlabel('Original exponent b (multiples of 16)',fontsize=11)
ax.set_ylabel('Exact receiving exponent d(b)',fontsize=11)
ax.legend(loc='lower right',fontsize=10,framealpha=.95)
ax=axs[1];ax.axis('off')
rows=[['1',r'$12247/512$'],['2',r'$3536101/32768$'],
      ['3',r'$2007/512$'],['4',r'$67543/512$'],['5',r'$159/16$']]
tab=ax.table(cellText=rows,colLabels=['Original term j',r'$d_j$ at $b=1024$'],
             cellLoc='center',colLoc='center',bbox=[0,.12,1,.75])
tab.auto_set_font_size(False);tab.set_fontsize(15)
for (i,j),cell in tab.get_celld().items():
    cell.set_edgecolor('#d1dfe4')
    if i==0:cell.set_facecolor('#163f51');cell.set_text_props(color='white')
    elif i==3:cell.set_facecolor('#d3edf4')
ax.text(.5,.99,'All five original terms retained',ha='center',fontsize=14,transform=ax.transAxes)
fig.suptitle('Exact margins for the complete stress estimate',fontsize=21,color='#163f51')
fig.text(.5,.16,r'$\theta=1/(64b^2),\quad\varepsilon_R=1/(64b),\quad p=128b/(128b-1),\quad'
 r'T_j/(\Lambda^{-2\varepsilon_R}\delta_{q+2})=\lambda_1^{-3\theta}X^{-d_j}$',
 ha='center',fontsize=15)
fig.text(.5,.055,'The plotted choice is SP6 throughout; the printed source example fails separately by SP4–SP5.\nSP1–SP9, ST23–ST30 and EX6–EX10 prove the numerical powers and the actual finite stress bounds.\nHuman source: Buckmaster–Vicol, arXiv:1709.10033v4, original eq:parameters. Energy induction remains subsequent work.',
 ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-stress-parameter-margins.{ext}',dpi=150,facecolor='white')
plt.close(fig)

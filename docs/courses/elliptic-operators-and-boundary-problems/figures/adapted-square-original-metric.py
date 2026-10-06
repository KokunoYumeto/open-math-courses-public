"""Exact original and adapted metrics in the scalar square-root proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,5.4));ax.set(xlim=(0,12),ylim=(0,5.4));ax.axis('off')
def txt(x,y,s,size=16):ax.text(x,y,s,ha='center',va='center',fontsize=size)
txt(6,5.07,'A square-root proof retaining the original metric',20)
txt(6,4.42,r'$a\geq0,\quad a\in S(h^{-1},g),\quad m=a+1$',18)
txt(6,3.69,r'$G=g/(hm),\quad \mu=(hm)^{-1}\geq (1+p_0(a;h^{-1},g))^{-1}>0$',17)
txt(6,2.94,r'$h_G=1/m,\quad b=\sqrt{m},\quad b\# b=m+r$',19)
txt(6,2.19,r'$r\in S(mh_G^2,G)=S(m^{-1},G)\subset S(1,G)$',18)
txt(6,1.43,r'$\langle a^wu,u\rangle=\|b^wu\|^2-\|u\|^2-\langle r^wu,u\rangle$',18)
txt(6,.65,'The bounded remainder gives the lower bound; the original g is retained.',14)
fig.text(.5,.02,'F7, F11a and F13 prove the displayed identities. A56–A58 prove temperateness for every fixed positive lower bound.\nThis diagram records a complete proof, not a changed symbol.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.13)
fig.savefig(p/'adapted-square-original-metric.svg');fig.savefig(p/'adapted-square-original-metric.png',dpi=165);plt.close(fig)

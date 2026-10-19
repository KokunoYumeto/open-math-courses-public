"""The structural zero-one law of the actual physical return. CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=Path(__file__).resolve().with_suffix('');ink='#182a3a';blue='#164b7a';green='#126856'
fig=plt.figure(figsize=(12,10.5),facecolor='#fafcff')
a=fig.add_axes([.035,.30,.93,.67]);a.axis('off')
a.text(.5,.965,'Actual physical return: zero mass or unit mass',ha='center',fontsize=21,weight='bold',color=ink)
a.text(.5,.88,r'$H_{j-1}=k_jH_j,\qquad \mathrm{supp}(H_j)=p\in Z(T)=\mathbb{C}1$',ha='center',fontsize=16,color=blue)
a.text(.18,.775,r'$p=0$',ha='center',fontsize=17,color='#8b3d32');a.text(.70,.775,r'$p=1$ (faithful; no spectral lower bound)',ha='center',fontsize=14,color=green)
a.annotate('',xy=(.18,.80),xytext=(.38,.845),arrowprops=dict(arrowstyle='->',color='#778899'))
a.annotate('',xy=(.70,.80),xytext=(.62,.845),arrowprops=dict(arrowstyle='->',color='#778899'))
a.text(.18,.68,r'$H_j=0$ for every shift',ha='center',fontsize=13,color='#8b3d32')
rows=[(r'$\Theta_j=\tau(H_j^{-1}\,\cdot)$','Compatible normal semifinite traces; total mass may be infinite'),
 ('Actual full-corner center map',r'Preserves $\tau$ and $\Theta$: $m_{j+1}=m_{j-1}$'),
 ('Exact positive increment',r'$m_j-m_{j-1}=\tau(H_{j-1}(k_j-1)^2k_j^{-1})\geq0$'),
 ('Nondecreasing and two-periodic masses',r'$k_j=1$ for every step; $H_j=1$')]
for n,(title,detail) in enumerate(rows):
 y=.68-.15*n
 a.text(.70,y,title,ha='center',fontsize=13,color=green,weight='bold')
 a.text(.70,y-.055,detail,ha='center',fontsize=11,color=ink)
 if n<3:a.annotate('',xy=(.70,y-.115),xytext=(.70,y-.075),arrowprops=dict(arrowstyle='->',color='#778899'))
a.text(.5,.04,'PH.22–PH.24 use the whole shifted tower and original cups; no amenability is assumed.',ha='center',fontsize=12,color=ink)
b=fig.add_axes([.10,.12,.80,.13],facecolor='white');b.set_xlim(-.05,1.05);b.set_ylim(0,1);b.set_yticks([])
b.axvspan(0,1,color='#f0dedd',alpha=.8);b.plot([0,1],[.5,.5],color='#8797a5',lw=1)
b.scatter([0,1],[.5,.5],s=110,c=['#8b3d32',green],zorder=3)
b.set_xticks([0,.25,.5,.75,1]);b.set_xlabel(r'Actual limiting mass $\tau(h)$')
b.text(.5,.82,'Every intermediate mass is excluded',ha='center',fontsize=13,color=ink)
b.text(.015,.16,'h = 0',ha='left',fontsize=12,color='#8b3d32');b.text(.985,.16,'h = 1; physical bicommutant',ha='right',fontsize=12,color=green)
fig.text(.5,.035,'The original strongly amenable case still requires exclusion of h = 0.',ha='center',fontsize=13,color='#8b3d32')
for ext in ['.svg','.png']:
 fig.savefig(str(P)+ext,dpi=160,facecolor=fig.get_facecolor())
 if ext=='.svg':
  f=P.with_suffix('.svg');f.write_text('\n'.join(line.rstrip() for line in f.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)

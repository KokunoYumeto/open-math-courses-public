"""Figure10.12: exact row fields and initial kernel heights. Original work, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,axes=plt.subplots(1,2,figsize=(14,8.3))
fig.subplots_adjust(top=.82,bottom=.10,wspace=.10,left=.035,right=.965)
fig.suptitle('The initial rows determine the coefficient field',fontsize=19,y=.965,weight='bold')
fig.text(.5,.89,r'Rows: $0,\ (1,1,1,1),\ 2(1,t,t^2,t^3)$     Kernel: $(-t,\ t^2+t+1,\ -t^2-t-1,\ t)$',ha='center',fontsize=14)
for i,ax in enumerate(axes):
 ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
 color='#2563eb' if i==0 else '#7c3aed'
 for y,hh in [(.70,.20),(.42,.21),(.10,.25)]:
  ax.add_patch(FancyBboxPatch((.025,y),.95,hh,boxstyle='round,pad=.012',facecolor='#eff6ff' if i==0 else '#f5f3ff',edgecolor=color,lw=1.5))
 if i==0:
  ax.text(.5,.945,r'Rational columns: $t=6$',ha='center',fontsize=15,weight='bold')
  ax.text(.5,.835,r'Ambient $K=\mathbb{Q}(\sqrt{5})$: degree 2',ha='center',fontsize=13)
  ax.text(.5,.765,r'Exact row field $E_0=\mathbb{Q}$: degree 1',ha='center',fontsize=14,color=color)
  ax.text(.5,.565,r'$c=(-6,43,-43,6)$',ha='center',fontsize=15)
  ax.text(.5,.490,r'$43-7\cdot6=1$: primitive integer vector',ha='center',fontsize=12)
  ax.text(.5,.305,r'$h_\infty(c)=\ln43$',ha='center',fontsize=14)
  ax.text(.5,.230,r'$h_2(c)=\frac{1}{2}\ln3770$',ha='center',fontsize=14)
  ax.text(.5,.155,r'Discriminant cost: $0$; removes $\frac{1}{4}\ln5$',ha='center',fontsize=12,color=color)
 else:
  ax.text(.5,.945,r'Algebraic columns: $t=\sqrt{6}$',ha='center',fontsize=15,weight='bold')
  ax.text(.5,.835,r'The row entry $2t$ recovers $\sqrt{6}$',ha='center',fontsize=13)
  ax.text(.5,.765,r'Exact row field $E_0=\mathbb{Q}(\sqrt{6})$: degree 2',ha='center',fontsize=13,color=color)
  ax.text(.5,.565,r'$c=(-t,7+t,-7-t,t)$',ha='center',fontsize=15)
  ax.text(.5,.490,r'$(7+t)-(1+t)t=1$: unit ideal',ha='center',fontsize=12)
  ax.text(.5,.305,r'$h_\infty(c)=\frac{1}{2}\ln43$',ha='center',fontsize=14)
  ax.text(.5,.230,r'$h_2(c)=\frac{1}{4}\ln10180$',ha='center',fontsize=14)
  ax.text(.5,.155,r'Discriminant cost: $\frac{1}{4}\ln24\leq\frac{1}{2}\ln12$',ha='center',fontsize=13,color=color)
 ax.annotate('',xy=(.5,.64),xytext=(.5,.695),arrowprops={'arrowstyle':'->','lw':1.5,'color':color})
fig.text(.5,.047,'Theorem10.63; equations(10.169)–(10.176); Solution32. All displayed fields, rows, vectors and heights are exact.',ha='center',fontsize=11,color='#475569')
fig.savefig(Path(__file__).with_name('initial-coefficient-field.png'),dpi=150,facecolor='white')
plt.close(fig)

"""Original CC0 cocycle transport-order and negative-crossing illustration."""
from pathlib import Path
from fractions import Fraction as Q
import math,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'mathtext.fontset':'dejavusans','svg.fonttype':'path','svg.hashsalt':'oa-flow-l37-transports-v1'})
navy='#17334d';blue='#2563a6';purple='#7450a3';orange='#b45118';teal='#147a70';gray='#718294';light='#f1f5f9'
u=Q(1,4);t=Q(-3,2);q=u+t;n=math.floor(q);v=q-n
assert (q,n,v)==(Q(-5,4),-2,Q(3,4)) and n+v-u==t and 0<=v<1
up=Q(3,4);tp=Q(7,4);np=math.floor(up+tp);vp=up+tp-np
assert (np,vp)==(2,Q(1,2)) and np+vp-up==tp
checks={'negative':{'u':str(u),'t':str(t),'u+t':str(q),'n':n,'v':str(v),'h+f_target-f_source':str(Q(n)+v-u)},'positive':{'u':str(up),'t':str(tp),'n':np,'v':str(vp)},'chronological_order':['down: a_i(z,u)^-1','return: c_i(y,z)','up: a_i(y,v)'],'product':'a_i(y,v) c_i(y,z) a_i(z,u)^-1','top_panel':'Transport diagram; vertical lengths schematic, return arrow may be signed.','lower_panel':'Exact local orbit segment in a unit-roof suspension; no finite-base assumption.','all_exact_assertions_pass':True}
OUT.joinpath('exact_checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(16,11),facecolor='white')
fig.text(.06,.945,'Three transports, one ordered product',fontsize=26,weight='bold',color=navy)
fig.text(.06,.90,'Traverse the arrows down → return → up. Each new cocycle factor multiplies on the left.',fontsize=17,color=gray)
ax=fig.add_axes([.08,.585,.84,.25]);ax.set_xlim(-.9,6.9);ax.set_ylim(-.45,2.65);ax.axis('off')
ax.plot([0,0],[0,2],color=blue,alpha=.2,lw=9);ax.plot([6,6],[0,1.45],color=orange,alpha=.2,lw=9)
ax.scatter([0,0,6,6],[2,0,0,1.45],s=70,c=[blue,blue,orange,orange],zorder=4)
ax.annotate('',xy=(0,.14),xytext=(0,1.86),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':blue,'mutation_scale':20})
ax.annotate('',xy=(5.84,0),xytext=(.16,0),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':purple,'mutation_scale':20})
ax.annotate('',xy=(6,1.31),xytext=(6,.14),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':orange,'mutation_scale':20})
ax.text(0,2.21,r'$x=(z,u)$',fontsize=21,ha='center',color=blue)
ax.text(6,1.66,r'$F_tx=(y,v)$',fontsize=21,ha='center',color=orange,bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(-.16,-.25,r'$(z,0)$',fontsize=19,ha='center',color=navy)
ax.text(6.16,-.25,r'$(y,0)$',fontsize=19,ha='center',color=navy)
ax.text(.25,1.02,r'1. down: $a_i(z,u)^{-1}$',fontsize=19,ha='left',color=blue)
ax.text(3,-.29,r'2. return: $c_i(y,z)$',fontsize=19,ha='center',color=purple)
ax.text(5.7,.72,r'3. up: $a_i(y,v)$',fontsize=19,ha='right',color=orange)
ax.annotate('',xy=(5.87,1.5),xytext=(.13,2.05),arrowprops={'arrowstyle':'->','lw':1.5,'ls':'--','color':gray,'connectionstyle':'arc3,rad=-.12','mutation_scale':15})
ax.text(3.2,2.47,r'$\sigma_i(t,x)$',fontsize=23,ha='center',color=navy,bbox={'facecolor':'white','edgecolor':'none','pad':2})
fig.text(.50,.532,r'$\sigma_i(t,(z,u))=a_i(y,v)\;c_i(y,z)\;a_i(z,u)^{-1}$',fontsize=25,ha='center',color=navy)
fig.text(.50,.491,'Product order:  up × return × down.  Vertical lengths above are schematic.',fontsize=15,ha='center',color=gray)
fig.text(.06,.437,'An exact negative crossing under a unit roof',fontsize=21,weight='bold',color=navy)
ax2=fig.add_axes([.08,.205,.84,.20]);ax2.set_xlim(-2.4,1.25);ax2.set_ylim(-.63,1.65);ax2.axis('off')
for k,label,col in [(-2,r'$S^{-2}z$',teal),(-1,r'$S^{-1}z$',purple),(0,r'$z$',blue)]:
 ax2.add_patch(Rectangle((k,0),1,.60,facecolor=col,alpha=.10,edgecolor='none'))
 ax2.plot([k,k],[-.06,.61],color=gray,lw=1)
 ax2.text(k,-.13,str(k),ha='center',va='top',fontsize=15,color=gray)
 ax2.text(k+.5,-.42,label,ha='center',va='top',fontsize=19,color=col)
ax2.plot([1,1],[-.06,.61],color=gray,lw=1);ax2.text(1,-.13,'1',ha='center',va='top',fontsize=15,color=gray)
ax2.plot([-2.18,1.08],[0,0],color=gray,lw=1)
ax2.scatter([float(q),float(u)],[.34,.34],s=100,c=[teal,blue],zorder=5)
ax2.text(float(q),.67,r'$v=\frac{3}{4}$',ha='center',va='center',fontsize=19,color=teal,bbox={'facecolor':'white','edgecolor':'none','pad':1})
ax2.text(float(u),.67,r'$u=\frac{1}{4}$',ha='center',va='center',fontsize=19,color=blue,bbox={'facecolor':'white','edgecolor':'none','pad':1})
ax2.plot([float(q),float(q)],[.42,.88],color=teal,lw=1,ls=':');ax2.plot([float(u),float(u)],[.42,.88],color=blue,lw=1,ls=':')
ax2.annotate('',xy=(float(q),.99),xytext=(float(u),.99),arrowprops={'arrowstyle':'-|>','lw':2.5,'color':orange,'mutation_scale':18})
ax2.text(-.50,1.22,r'$t=-\frac{3}{2}$',ha='center',fontsize=20,color=orange)
ax2.text(-1.8,.93,r'$u+t=-\frac{5}{4}$',ha='center',fontsize=17,color=teal)
ax2.text(.67,1.05,'two roofs\nbackward',ha='center',va='center',fontsize=15,color=gray)
box=FancyBboxPatch((.06,.065),.88,.091,transform=fig.transFigure,boxstyle='round,pad=0.012',facecolor=light,edgecolor='#d9e2eb');fig.patches.append(box)
fig.text(.50,.104,r'$n=-2,\quad h+f(F_tx)-f(x)=-2+\frac{3}{4}-\frac{1}{4}=-\frac{3}{2}$',ha='center',fontsize=24,color=navy)
fig.text(.06,.025,'Local orbit segment only; the three displayed base labels do not form a finite system. Proofs: L37 (E1)–(E6).',fontsize=12,color=gray)
fig.savefig(OUT/'three-transports-crossings.png',dpi=200,facecolor='white')
fig.savefig(OUT/'three-transports-crossings.svg',metadata={'Date':None},facecolor='white')
plt.close(fig)
print(json.dumps({'png':'three-transports-crossings.png','pixels':[3200,2200],'exact_checks':True}))

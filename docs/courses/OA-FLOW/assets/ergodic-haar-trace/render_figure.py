"""Reproduce the exact Klein-four Haar-average illustration; no sampled theorem proof."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch

P=Path(__file__).resolve().parent
OUT=P/'assets';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-ergodic-haar-exact-v1','font.size':12})
U=((1,0),(0,-1));V=((0,1),(1,0));I=((1,0),(0,1));X=((5,2),(2,1))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def adj(a):return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))
G=[(0,0),(1,0),(0,1),(1,1)]
conjugations=[]
for a,b in G:
    w=mul(U if a else I,V if b else I)
    conjugations.append(mul(mul(w,X),adj(w)))
mean=tuple(tuple(sum(Fraction(m[i][j],4) for m in conjugations) for j in range(2)) for i in range(2))
assert mean==((3,0),(0,3))
chars=[[1]*4,[(-1)**b for a,b in G],[(-1)**a for a,b in G],[(-1)**(a+b) for a,b in G]]
assert [sum(r) for r in chars]==[4,0,0,0]
data={'group':'(Z/2Z)^2','group_order':G,'haar_mass_per_element':'1/4','U':U,'V':V,'UV':mul(U,V),'X':X,'conjugations':conjugations,'character_rows':['I','U','V','UV'],'character_values':chars,'character_means':['1','0','0','0'],'average':[[str(x) for x in r] for r in mean],'tau_X':'3','source_proof':'ET1-3; equations H22-H25','scope':'Exact finite illustration; arbitrary compact-group proof remains in full lesson.'}
(OUT/'ergodic-haar-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(12.8,9.6),dpi=175,facecolor='#ffffff')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,12.8),ylim=(0,9.6));ax.axis('off')
ink='#15384b';teal='#087f89';muted='#4e6875';gold='#946000'
ax.text(.5,9.03,'Four symmetries reveal the trace',fontsize=25,fontweight='bold',color=ink)
ax.text(.52,8.61,'Exact noncommutative model:  G = (Z/2Z)² acts on M₂ by conjugation',fontsize=14,color=muted)
ax.text(.52,8.18,'U = diag(1, −1),   V swaps the two coordinates,   UV = −VU',fontsize=17,color=ink)
ax.text(.52,7.70,'The scalar sign cancels in conjugation, so the two automorphisms commute.',fontsize=12,color=muted)
ax.text(.52,7.13,'Character values on the four group elements',fontsize=16,fontweight='bold',color=ink)
xs=[1.0,3.0,4.7,6.4,8.1,10.55]
headers=['basis','(0,0)','(1,0)','(0,1)','(1,1)','Haar mean']
for x,s in zip(xs,headers):ax.text(x,6.61,s,ha='center',color=muted,fontweight='bold')
for i,(name,vals) in enumerate(zip(['I','U','V','UV'],chars)):
    y=6.08-.52*i
    ax.add_patch(FancyBboxPatch((.5,y-.2),11.55,.43,boxstyle='round,pad=.02',facecolor='#e8f4f3' if i==0 else '#f3f6f8',edgecolor='none'))
    for x,s in zip(xs,[name]+[str(q) if q<0 else '+1' for q in vals]+['1' if i==0 else '0']):ax.text(x,y,s,ha='center',va='center',color=teal if i==0 else ink,fontsize=16)
ax.text(.53,3.96,r'$X=c_0I+c_1U+c_2V+c_3UV\quad\longmapsto\quad E(X)=c_0I=\frac{\mathrm{Tr}(X)}{2}I$',fontsize=20,color=teal)
ax.text(.53,3.40,'A concrete positive matrix: average its four conjugates entry by entry',fontsize=15,fontweight='bold',color=ink)
def matrix(x,y,m):
    ax.plot([x-.42,x-.5,x-.5,x-.42],[y+.32,y+.32,y-.32,y-.32],color=ink,lw=1.5)
    ax.plot([x+.42,x+.5,x+.5,x+.42],[y+.32,y+.32,y-.32,y-.32],color=ink,lw=1.5)
    for i in range(2):
        for j in range(2):ax.text(x+(-.23 if j==0 else .23),y+(.16 if i==0 else -.16),str(m[i][j]),ha='center',va='center',fontsize=20,color=ink)
for k,(g,m) in enumerate(zip(G,conjugations)):
    x=1.45+2.25*k
    ax.text(x,2.82,str(g),ha='center',color=muted)
    matrix(x,2.23,m)
    if k<3:ax.text(x+1.1,2.23,'+',ha='center',va='center',fontsize=22,color=ink)
ax.text(.33,2.23,'¼',ha='center',va='center',fontsize=24,color=gold)
ax.plot([.8,.7,.7,.8],[2.70,2.70,1.76,1.76],color=ink,lw=1.5)
ax.plot([8.82,8.92,8.92,8.82],[2.70,2.70,1.76,1.76],color=ink,lw=1.5)
ax.add_patch(FancyArrowPatch((9.1,2.23),(10.0,2.23),arrowstyle='->',mutation_scale=18,color=teal,lw=2))
matrix(10.8,2.23,((3,0),(0,3)))
ax.text(10.8,1.65,r'$E(X)=3I$',ha='center',fontsize=17,color=teal)
ax.text(.53,1.15,'Only the scalar character survives. The algebra is still noncommutative.',fontsize=14,color=ink)
ax.text(.53,.75,'General proof: normal Haar average → faithful state → opposite fibers → ultraweak density.',fontsize=11,color=muted)
ax.text(.53,.37,'Proof: ET1–3, H22–H25. Target: Takesaki II, Exercise XI.1.6, p.331. Original exact illustration.',fontsize=9,color=muted)
fig.savefig(OUT/'ergodic-haar.png',dpi=175,metadata={'Software':'OA-FLOW original exact illustration'})
fig.savefig(OUT/'ergodic-haar.svg',metadata={'Date':None,'Creator':'OA-FLOW original exact illustration'})
plt.close(fig)
print(json.dumps({'exact_matrix_checks':True,'exact_character_average_checks':True,'png':str(OUT/'ergodic-haar.png')}))

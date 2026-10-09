"""Exact normalization/contact diagram for RC2. Independently authored CC0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import sys
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','svg.hashsalt':'sh02-relative-conormal-v1','mathtext.fontset':'dejavuserif'})
blue='#284f75';ink='#182e41';green='#237c61'
def render(portrait):
 fig,ax=plt.subplots(figsize=(5.8,9.5) if portrait else (12.8,7.4))
 ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 def box(x,y,w,h,lines):
  ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',fc='#f2f6fa',ec=blue,lw=1.3))
  for j,line in enumerate(lines):ax.text(x+w/2,y+h*(.72-j*.4),line,ha='center',va='center',fontsize=13,color=ink)
 def arrow(a,b,label,dx=0,dy=.035):
  ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,color=blue,lw=1.5))
  ax.text((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy,label,ha='center',va='center',fontsize=12,color=ink)
 ax.text(.5,.965,'Vanishing on the zero divisor',ha='center',fontsize=19,color=ink)
 ax.text(.5,.925,'Finite normalization and the actual tangent lift',ha='center',fontsize=11,color=ink)
 if portrait:
  box(.07,.74,.33,.12,[r'$C^\nu$',r'$H=h\circ\pi\circ\nu$'])
  box(.61,.74,.32,.12,[r'$C\subset T^*M$',r'$\alpha=\sum_j\xi_j\,dz_j$'])
  box(.07,.50,.33,.12,[r'$E=\{t=0\}$',r'$w\in T E$'])
  box(.61,.50,.32,.12,[r'$D\subset C_0$',r'$v=d\nu(w)\in T D$'])
  arrow((.42,.80),(.59,.80),r'$\nu$ finite',dy=.045)
  arrow((.42,.56),(.59,.56),r'$\nu|_E$',dy=.055)
  arrow((.235,.64),(.235,.72),'inclusion',dx=.12,dy=0)
  arrow((.77,.64),(.77,.72),'inclusion',dx=-.12,dy=0)
  ax.text(.5,.44,'At a generic regular divisor point:',ha='center',fontsize=12,color=ink)
  ax.text(.5,.395,r'$H=t^m,\qquad m\geq1$',ha='center',fontsize=16,color=ink)
  ax.text(.5,.345,r'$\nu^*\alpha=m\lambda t^{m-1}\,dt$',ha='center',fontsize=16,color=ink)
  ax.text(.5,.295,r'$dt(w)=0\ \Longrightarrow\ \alpha(v)=0$',ha='center',fontsize=15,color=green)
  ax.text(.5,.22,'A pole of the multiplier is allowed:',ha='center',fontsize=12,color=ink)
  ax.text(.5,.175,r'$H=t^3,\quad\lambda=t^{-2}$',ha='center',fontsize=15,color=ink)
  ax.text(.5,.13,r'$\nu^*\alpha=3\,dt,\quad(\nu^*\alpha)|_E=0$',ha='center',fontsize=15,color=green)
  ax.text(.5,.055,'The bottom finite map has full rank generically.\nDensity and analytic pullback give all of RC2.\nDiagram of maps; no geometric scale. Proof: RC2.',ha='center',fontsize=9,color=ink)
 else:
  box(.055,.61,.32,.20,[r'$C^\nu$',r'$H=h\circ\pi\circ\nu$'])
  box(.625,.61,.32,.20,[r'$C\subset T^*M$',r'$\alpha=\sum_j\xi_j\,dz_j$'])
  box(.055,.30,.32,.18,[r'$E=\{t=0\}$',r'$w\in T E$'])
  box(.625,.30,.32,.18,[r'$D\subset C_0$',r'$v=d\nu(w)\in T D$'])
  arrow((.39,.71),(.61,.71),r'$\nu$ finite',dy=.045)
  arrow((.39,.39),(.61,.39),r'$\nu|_E$ finite; generic full rank',dy=.055)
  arrow((.215,.50),(.215,.59),'inclusion',dx=.08,dy=0)
  arrow((.785,.50),(.785,.59),'inclusion',dx=-.08,dy=0)
  ax.text(.5,.235,r'$H=t^m,\quad m\geq1,\qquad \nu^*\alpha=m\lambda t^{m-1}\,dt$',ha='center',fontsize=15,color=ink)
  ax.text(.5,.18,r'$dt(w)=0\quad\Longrightarrow\quad\alpha(v)=(\nu^*\alpha)(w)=0$',ha='center',fontsize=15,color=green)
  ax.text(.5,.105,r'Example with a pole: $H=t^3,\ \lambda=t^{-2},\ \nu^*\alpha=3\,dt,\ (\nu^*\alpha)|_E=0$.',ha='center',fontsize=12,color=ink)
  ax.text(.5,.045,'At generic regular points; density and analytic pullback extend the conclusion. Diagram of maps, with no geometric scale. Proof: RC2.',ha='center',fontsize=9,color=ink)
 fig.subplots_adjust(left=.03,right=.97,top=.98,bottom=.015)
 stem='relative-conormal-normalization-stacked' if portrait else 'relative-conormal-normalization'
 fig.savefig(out/(stem+'.svg'),metadata={'Date':None})
 fig.savefig(out/(stem+'.png'),dpi=160)
 fig.savefig(out/(stem+'.pdf'),metadata={'CreationDate':None,'ModDate':None})
 plt.close(fig)
render(False);render(True)
(out/'FIGURE_MATH.json').write_text(json.dumps({'proof':'RC2','kind':'Exact finite-normalization and tangent-lift diagram, not a geometric sample','hypotheses':'C relative conormal closure; E divisor over a component D of C0; generic regular normalization point; H=t^m after analytic unit absorption; m>=1','maps':['nu:C^nu->C finite normalization','nu|E:E->D finite with generic full rank','w in TE lifts v=dnu(w) in TD'],'one_form':'nu*alpha=m lambda t^(m-1)dt; dt(w)=0 implies alpha(v)=0','pole_example':'H=t^3, lambda=t^-2, nu*alpha=3dt, restriction to E=0','source_license':'CC0-1.0','wide_and_portrait':'Same exact objects, maps, coefficients and example.'},indent=2)+'\n',encoding='utf-8')

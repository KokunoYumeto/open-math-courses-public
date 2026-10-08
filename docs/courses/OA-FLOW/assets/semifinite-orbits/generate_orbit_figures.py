"""Original CC0 semifinite-orbit figures. Run with python -B; NumPy + Matplotlib."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE=Path(__file__).resolve().parent
BG,INK,MUTED='#fcfbf7','#172d3c','#536575'
BLUE,TEAL,RED,GOLD='#236c9c','#087e80','#b4443f','#b88024'
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':13,'text.color':INK,
 'axes.labelcolor':INK,'axes.edgecolor':'#9ba9b1','xtick.color':MUTED,'ytick.color':MUTED,
 'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'svg.fonttype':'path',
 'svg.hashsalt':'oa-flow-semifinite-orbits-20261007','axes.spines.top':False,'axes.spines.right':False})
def canvas(title,sub):
 f=plt.figure(figsize=(15,8.8));f.text(.05,.95,title,fontsize=24,weight='bold',va='top');f.text(.05,.895,sub,fontsize=13,color=MUTED,va='top');return f
def save(f,name):
 f.savefig(HERE/(name+'.png'),dpi=160);f.savefig(HERE/(name+'.svg'),metadata={'Date':None,'Creator':'Original OA-FLOW mathematical illustration','Rights':'CC0-1.0'});plt.close(f)
def foot(f,s):f.text(.05,.035,s,fontsize=10.5,color=MUTED)

def matching():
 f=canvas('Trace-matched bands realize the exact orbit distance',r'A type II step model: both densities have trace one; the padded support has trace $3$.')
 ax=f.add_axes([.075,.39,.39,.39]);s=np.array([0,1,1.5,3]);aa=np.array([.6,.2,.2,.2]);bb=np.array([.5,.5,1/6,1/6])
 ax.step(s,aa,where='post',color=BLUE,lw=2.5,label=r'$\mu_a$: $3/5$, then $1/5$');ax.step(s,bb,where='post',color=TEAL,lw=2.5,label=r'$\mu_b$: $1/2$, then $1/6$');ax.fill_between(s,aa,bb,step='post',color=GOLD,alpha=.23)
 ax.set(xlim=(0,3),ylim=(0,.76),xticks=[0,1,1.5,3],yticks=[0,.2,.5,.6],yticklabels=['0','1/5','1/2','3/5'],xlabel=r'trace coordinate $s$',ylabel='decreasing coefficient',title='A. One common refinement');ax.legend(frameon=False,fontsize=11,loc='upper right');ax.grid(alpha=.13)
 bx=f.add_axes([.575,.39,.37,.39]);t=np.array([0,1/6,.2,.5,.6,.7]);fa=np.array([3,3,1,1,0,0]);fb=np.array([3,1.5,1.5,0,0,0]);bx.step(t,fa,where='post',color=BLUE,lw=2.5,label=r'$f_a$');bx.step(t,fb,where='post',color=TEAL,lw=2.5,label=r'$f_b$');bx.fill_between(t,fa,fb,step='post',color=GOLD,alpha=.23)
 bx.set(xlim=(0,.7),ylim=(0,3.4),xticks=[0,1/6,.2,.5,.6],xticklabels=['0','1/6','1/5','1/2','3/5'],yticks=[0,1,1.5,3],xlabel=r'threshold $t$',ylabel='tail trace',title='B. The same area in tail coordinates');bx.tick_params(axis='x',labelrotation=45,labelsize=11);bx.legend(frameon=False,fontsize=11);bx.grid(alpha=.13)
 cx=f.add_axes([.075,.12,.40,.14]);cx.set(xlim=(-.55,3.1),ylim=(-.1,1.1));cx.axis('off')
 for row,y,label in [(0,.71,r'$p_j$'),(1,.05,r'$q_j$')]:
  cx.text(-.22,y+.12,label,ha='right',va='center',fontsize=16)
  for j,(left,right) in enumerate(zip(s[:-1],s[1:])):
   cx.add_patch(Rectangle((left,y),right-left,.23,facecolor=['#d3e5ef','#d8ede6','#f0e4ca'][j],edgecolor=INK,lw=1))
   cx.text((left+right)/2,y+.115,['1','1/2','3/2'][j],ha='center',va='center',fontsize=12)
 for j,(left,right) in enumerate(zip(s[:-1],s[1:])):cx.annotate('',((left+right)/2,.30),((left+right)/2,.68),arrowprops={'arrowstyle':'-|>','color':INK,'lw':1.3})
 f.text(.075,.082,r'Matched traces: $1$, $1/2$, $3/2$; each arrow is a partial isometry.',fontsize=12)
 f.text(.575,.21,r'$\delta(\phi_a,\phi_b)=\frac{3}{10}$',fontsize=25,color=TEAL)
 f.text(.575,.135,r'$\int|\mu_a-\mu_b|=\int|f_a-f_b|$',fontsize=20,color=TEAL)
 foot(f,'Proof: Spectral distributions and closed unitary orbits, #orbit-step-matching, (SO10)–(SO12); completion in #orbit-projections, (SO8). Every drawn step and trace mass is exact.')
 save(f,'orbit-trace-band-matching')

def rangefigure():
 f=canvas('The tail range remembers discrete or continuous trace dimension',r'Each panel represents a normal state: $\int_0^\infty f(t)\,dt=1$. The type II example uses $\tau(1)=1$.')
 ax=f.add_axes([.075,.36,.39,.43]);ax.step([0,.25,.75,1.0],[2,1,0,0],where='post',lw=2.8,color=BLUE);ax.fill_between([0,.25,.75,1.0],[2,1,0,0],step='post',alpha=.13,color=BLUE)
 ax.set(xlim=(0,1),ylim=(0,2.35),xlabel=r'threshold $t$',ylabel='tail trace',xticks=[0,.25,.75,1],xticklabels=['0','1/4','3/4','1'],yticks=[0,1,2],title=r'Type I: eigenvalues $3/4$, $1/4$');ax.grid(alpha=.13)
 ax.text(.5,-.23,r'$f(t)\in\mathbb{N}_0$ for the standard trace',transform=ax.transAxes,ha='center',fontsize=15,color=BLUE)
 bx=f.add_axes([.575,.36,.37,.43]);t=np.linspace(.001,4,800);v=np.minimum(1,1/(4*t*t));bx.plot(t,v,lw=2.8,color=TEAL);bx.fill_between(t,0,v,alpha=.13,color=TEAL)
 bx.set(xlim=(0,4),ylim=(0,1.15),xlabel=r'threshold $t$',ylabel='tail trace',xticks=[0,.5,1,2,3,4],yticks=[0,.25,.5,1],title=r'Type II: $\mu(s)=1/(2\sqrt{s})$, $0<s<1$');bx.grid(alpha=.13)
 bx.text(.37,.66,r'$f(t)=\min\{1,1/(4t^2)\}$',transform=bx.transAxes,fontsize=15,color=TEAL)
 bx.text(.5,-.23,r'Exact mass beyond the frame: $\int_4^\infty f(t)\,dt=1/16$',transform=bx.transAxes,ha='center',fontsize=14,color=TEAL)
 f.text(.075,.16,r'Continuous trace flag: $\tau(P_s)=s$; construct $B$ with Lebesgue spectral trace, then $h=\mu(B)$.',fontsize=16)
 f.text(.075,.087,r'$D(h)=\{\xi:\int\mu(s)^2\,d\mu^B_\xi(s)<\infty\}$; the type II example is integrable and unbounded.',fontsize=16)
 foot(f,'Proof: #orbit-range, (SO17)–(SO27). The left steps are exact. The right curve samples the displayed exact formula; its entire tail is included in the stated mass.')
 save(f,'orbit-tail-range')

def diameters():
 f=canvas('Nested finite projections give the sharp semifinite diameters',r'$0<e\leq f$, $a=\tau(e)$, $b=\tau(f)<\infty$: the states have densities $e/a$ and $f/b$.')
 ax=f.add_axes([.08,.31,.45,.47]);r=np.linspace(0,1,501);ax.plot(r,2*(1-r),lw=2.8,color=TEAL,label=r'exact distance $2(1-a/b)$');ax.scatter([1,1/2,1/3,1/4,1/8],[0,1,4/3,1.5,1.75],s=50,color=BLUE,zorder=4)
 ax.scatter([0],[2],s=85,facecolor=BG,edgecolor=RED,lw=2,zorder=5);ax.set(xlim=(-.03,1.02),ylim=(-.06,2.18),xlabel=r'trace ratio $a/b$',ylabel='orbit distance',xticks=[0,.25,.5,1],xticklabels=['0','1/4','1/2','1'],yticks=[0,1,1.5,2],title='Exact distances, with the limiting endpoint open');ax.grid(alpha=.13)
 ax.text(.06,2.025,'supremum 2',fontsize=13,color=RED);ax.legend(frameon=False,fontsize=12,loc='lower left')
 bx=f.add_axes([.62,.26,.33,.52]);bx.axis('off')
 bx.text(0,.90,r'$M_n(\mathbb{C})$',fontsize=22,color=BLUE);bx.text(0,.77,r'$D=2(1-1/n)$',fontsize=25,color=BLUE);bx.text(0,.63,'Pure state versus tracial state;\nattained, including n = 1.',fontsize=14)
 bx.text(0,.42,r'Type $\mathrm{I}_\infty$ and type II',fontsize=21,color=TEAL);bx.text(0,.29,r'$D=2$',fontsize=25,color=TEAL);bx.text(0,.13,'Rank ratios, or diffuse finite-corner\ntrace ratios, tend to zero.',fontsize=14)
 f.text(.08,.16,'Blue points show the finite-matrix values at ratios 1/n. Type II permits every positive ratio up to one.',fontsize=14)
 f.text(.08,.09,'The upper bound 2 follows from the norm of states; no infinite trace appears in a denominator.',fontsize=13)
 foot(f,'Proof: #orbit-diameters, (SO28)–(SO32). The line samples an exact formula; plotted matrix values are exact. The value 2 is a supremum, with no attainment claim here.')
 save(f,'orbit-semifinite-diameters')

def main():
 matching();rangefigure();diameters()
 sizes=np.array([1,.5,1.5]);aa=np.array([.6,.2,.2]);bb=np.array([.5,.5,1/6])
 data={'matching':{'trace_band_sizes':['1','1/2','3/2'],'a_coefficients':['3/5','1/5','1/5'],'b_coefficients':['1/2','1/2','1/6'],'mass_a':float(sizes@aa),'mass_b':float(sizes@bb),'distance':float(sizes@abs(aa-bb)),'exact_distance':'3/10'},'range':{'type_I_eigenvalues':['3/4','1/4'],'type_II_quantile':'1/(2*sqrt(s)), 0<s<1','type_II_tail':'min(1, 1/(4*t*t))','type_II_total_mass':1,'type_II_tail_mass_beyond_4':'1/16','type_II_density_unbounded':True},'diameters':{'finite_matrix':'2*(1-1/n)','I_infinity_and_II':2,'nested_projection_distance':'2*(1-a/b)'},'license':'CC0-1.0','font':'Installed DejaVu Sans, no copied fonts','figures':['orbit-trace-band-matching','orbit-tail-range','orbit-semifinite-diameters']}
 assert abs(data['matching']['mass_a']-1)<1e-12;assert abs(data['matching']['mass_b']-1)<1e-12;assert abs(data['matching']['distance']-.3)<1e-12
 (HERE/'diagnostics.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print('Three orbit figures rendered; exact band-matching diagnostics passed.')
if __name__=='__main__':main()

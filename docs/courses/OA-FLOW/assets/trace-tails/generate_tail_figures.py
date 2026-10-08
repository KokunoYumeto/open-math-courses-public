"""Original CC0 trace-tail figures. Run with python -B; NumPy + Matplotlib only."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
BG,INK,MUTED='#fcfbf7','#172d3c','#536575'
BLUE,TEAL,RED,GOLD='#236c9c','#087e80','#b4443f','#b88024'
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':13,'text.color':INK,
 'axes.labelcolor':INK,'axes.edgecolor':'#9ba9b1','xtick.color':MUTED,'ytick.color':MUTED,
 'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'svg.fonttype':'path',
 'svg.hashsalt':'oa-flow-trace-tails-20261007','axes.spines.top':False,'axes.spines.right':False})

def canvas(title,sub):
 f=plt.figure(figsize=(15,8.2));f.text(.05,.95,title,fontsize=24,weight='bold',va='top');f.text(.05,.89,sub,fontsize=13,color=MUTED,va='top');return f
def save(f,name):
 f.savefig(HERE/(name+'.png'),dpi=160);f.savefig(HERE/(name+'.svg'),metadata={'Date':None,'Creator':'Original OA-FLOW mathematical illustration','Rights':'CC0-1.0'});plt.close(f)
def foot(f,s):f.text(.05,.04,s,fontsize=10.5,color=MUTED)
def matrix(ax,x,y,a,label,color=INK,scale=.10):
 ax.text(x-.03,y,label,ha='right',va='center',fontsize=18,color=color)
 for i,row in enumerate(a):
  for j,v in enumerate(row):ax.text(x+(j+.5)*scale,y+(0.5-i)*scale,str(v),ha='center',va='center',fontsize=17,color=color)
 for xx,d in [(x-.014,1),(x+2*scale+.014,-1)]:ax.plot([xx+d*.012,xx,xx,xx+d*.012],[y+scale+.012,y+scale+.012,y-scale-.012,y-scale-.012],color=color,lw=1.5)

def contraction():
 f=canvas('Spectral tails can be closer than the original densities',r'Ordinary trace on $M_2(\mathbb{C})$; strict tails $f_h(t)=\mathrm{Tr}(1_{(t,\infty)}(h))$, $t>0$.')
 ax=f.add_axes([.075,.30,.40,.46]);ts=np.array([0,.5,1,2,3,3.4]);fh=np.array([2,2,1,1,0,0]);fk=np.array([2,1,1,0,0,0])
 ax.step(ts,fh,where='post',lw=2.8,color=BLUE,label=r'$h$: eigenvalues $(3,1)$');ax.step(ts,fk,where='post',lw=2.5,color=TEAL,label=r'$k$: eigenvalues $(2,1/2)$')
 ax.fill_between(ts,fh,fk,step='post',color=GOLD,alpha=.23)
 ax.set(xlim=(0,3.4),ylim=(-.05,2.35),xlabel=r'threshold $t$',ylabel='trace of strict tail',yticks=[0,1,2],xticks=[0,.5,1,2,3],title='Exact step functions')
 ax.legend(frameon=False,loc='upper right',fontsize=11);ax.grid(alpha=.13)
 ax.text(.72,1.46,r'$1/2$',ha='center',color=GOLD,fontsize=18);ax.text(2.5,.48,r'$1$',ha='center',color=GOLD,fontsize=18)
 ax.text(.5,-.25,r'$\int_0^\infty|f_h-f_k|\,dt=\frac{3}{2}$',transform=ax.transAxes,ha='center',fontsize=22,color=GOLD)
 bx=f.add_axes([.58,.23,.36,.55]);bx.set(xlim=(0,1),ylim=(0,1));bx.axis('off')
 matrix(bx,.14,.80,[[3,0],[0,1]],r'$h=$',BLUE)
 matrix(bx,.67,.80,[['5/4','3/4'],['3/4','5/4']],r'$k=$',TEAL,.12)
 bx.text(0,.54,r'$\operatorname{spec}(h-k)=\{2,-1/2\}$',fontsize=19)
 bx.text(0,.40,r'$\|h-k\|_1=5/2\ >\ 3/2$',fontsize=23,color=RED)
 bx.text(0,.24,'Optimal common-majorant trace:',fontsize=15)
 bx.text(0,.08,r'$\min\mathrm{Tr}(a)=\frac{1}{2}(4+5/2+5/2)=9/2$',fontsize=19,color=TEAL)
 f.text(.075,.12,'The shaded areas add to 3/2. The exact original norm is 5/2; aligning the eigenvectors reduces it to 3/2.',fontsize=13)
 foot(f,'Proof: Trace tails and the smallest common majorant, #tail-majorant and #tail-example, (TT14), (TT18)–(TT19). Step curves are exact; no spectral truncation is used.')
 save(f,'tail-contraction-majorant')

def equaltraces():
 f=canvas('Equal tail traces do not identify the spectral projections',r'$h=2P_{e_1}$, $k=2P_{(1,1)}$ on $\mathbb{C}^2$; $P_{(1,1)}$ is the orthogonal projection onto $\mathbb{C}(1,1)$.')
 ax=f.add_axes([.075,.30,.40,.46]);ax.step([0,2,2.7],[1,0,0],where='post',color=BLUE,lw=4,label=r'$f_h=f_k$')
 ax.set(xlim=(0,2.7),ylim=(-.05,1.3),xticks=[0,1,2],yticks=[0,1],xlabel=r'threshold $t$',ylabel='trace',title='The same scalar invariant');ax.legend(frameon=False);ax.grid(alpha=.13)
 ax.text(.5,-.24,r'$D(f_h,f_k)=0$',transform=ax.transAxes,ha='center',fontsize=23,color=TEAL)
 bx=f.add_axes([.62,.28,.30,.49]);bx.set_aspect('equal');bx.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),xticks=[-1,0,1],yticks=[-1,0,1],xlabel='first real coordinate',ylabel='second real coordinate',title=r'Spectral ranges for $0<t<2$')
 bx.axhline(0,lw=2.7,color=BLUE);bx.plot([-1.1,1.1],[-1.1,1.1],lw=2.7,color=TEAL);bx.scatter([1],[0],color=BLUE,s=55,zorder=3);bx.text(.7,.13,r'$e_1$',color=BLUE,fontsize=17);bx.text(-1.05,-.87,r'$(1,1)$ line',color=TEAL,fontsize=13);bx.grid(alpha=.13)
 f.text(.075,.145,r'$\|h-k\|_1=2\sqrt{2}$, but $\delta(\phi_h,\phi_k)=0$: a unitary rotation matches the two densities.',fontsize=20)
 f.text(.075,.092,'The right panel is an exact real slice of two complex spectral lines; neither projection is below the other.',fontsize=13)
 foot(f,'Proof: #tail-trace-order and #tail-example, (TT6), (TT20). This equal-trace example distinguishes scalar trace comparison from operator projection order.')
 save(f,'tail-projection-traces')

def main():
 contraction();equaltraces()
 h=np.diag([3.,1.]);k=np.array([[1.25,.75],[.75,1.25]]);a=np.array([[61.,3.],[3.,29.]])/20
 d={'strict_example':{'h':h.tolist(),'k':k.tolist(),'eigenvalues_difference':np.linalg.eigvalsh(h-k).tolist(),'original_norm':float(np.abs(np.linalg.eigvalsh(h-k)).sum()),'exact_tail_distance':'3/2','a0':a.tolist(),'a0_trace':float(np.trace(a)),'eigenvalues_a0_minus_h':np.linalg.eigvalsh(a-h).tolist(),'eigenvalues_a0_minus_k':np.linalg.eigvalsh(a-k).tolist()},'equal_tails':{'exact_original_distance':'2*sqrt(2)','exact_orbit_distance':0,'tail':'1 for 0<t<2, 0 for t>=2'},'license':'CC0-1.0','font':'Installed DejaVu Sans, no copied fonts','figures':['tail-contraction-majorant','tail-projection-traces']}
 assert np.allclose(np.linalg.eigvalsh(h-k),[-.5,2]);assert np.all(np.linalg.eigvalsh(a-h)>-1e-12);assert np.all(np.linalg.eigvalsh(a-k)>-1e-12)
 (HERE/'diagnostics.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
 print('Two tail figures rendered; exact matrix diagnostics passed.')
if __name__=='__main__':main()

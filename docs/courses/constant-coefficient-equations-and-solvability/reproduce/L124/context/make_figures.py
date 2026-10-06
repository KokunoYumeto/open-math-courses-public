"""Portable exact-coordinate diagrams; independently written CC0-1.0."""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN02-TP041-fixed','axes.spines.top':False,'axes.spines.right':False})
def write(fig,p):
 fig.savefig(p.with_suffix('.png'),dpi=150,metadata={'Software':'AN02 TP041 portable CC0 renderer'})
 fig.savefig(p.with_suffix('.svg'),metadata={'Date':None,'Creator':'AN02 TP041 portable CC0 renderer'})
 plt.close(fig)
def main(out):
 out.mkdir(parents=True,exist_ok=True)
 fig,ax=plt.subplots(figsize=(10,5.5),layout='constrained');t=np.linspace(-2.3,2.3,601);rho=2*np.log(2*np.cosh(t));ax.plot(t,rho,color='#155e86',lw=2.5,label=r'$\rho=2\log(2\cosh t)$')
 c=math.log(25/4);a=math.log(2);ax.axhline(c,color='#ac4c23',ls='--',label=r'$c=\log(25/4)$');ax.fill_between(t,math.log(4),c,where=(abs(t)<=a),alpha=.12,color='#328267')
 for x,label in [(-a,'r=1/2'),(0,'r=1'),(a,'r=2')]:
  y=2*math.log(2*math.cosh(x));ax.plot(x,y,'o',color='#155e86');ax.annotate(label,(x,y),xytext=(0,13),textcoords='offset points',ha='center')
 ax.set(xlabel=r'$t=\log r$ (real radial section)',ylabel=r'$\rho$',title=r'$U=\mathbb{P}^1\setminus\{z_0z_1=0\}=\mathbb{C}^*$');ax.text(.025,.93,r'Levi coefficient $2/(1+r^2)^2>0$',transform=ax.transAxes,va='top');ax.legend(loc='lower right');ax.set_ylim(1.1,5.1);write(fig,out/'projective-exhaustion')
 fig=plt.figure(figsize=(11,9),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1.35,1]);ax=fig.add_subplot(gs[0,0]);side=2*math.pi
 ax.plot([0,side,side,0,0],[0,0,side,side,0],color='#155e86',lw=2);ax.plot([0,side],[0,side],color='#71848e',ls=':');ax.fill_between([0,side],0,side,color='#d8ebee',alpha=.5)
 for y in [0,side]:ax.annotate('',(side*.68,y),(side*.32,y),arrowprops={'arrowstyle':'->','color':'#155e86','lw':2})
 for x in [0,side]:ax.annotate('',(x,side*.68),(x,side*.32),arrowprops={'arrowstyle':'->','color':'#ac4c23','lw':2})
 ax.set(xlim=(-.3,side+.3),ylim=(-.3,side+.3),xticks=[0,side],yticks=[0,side],xticklabels=['0',r'$2\pi$'],yticklabels=['0',r'$2\pi$'],xlabel=r'normal phase $\phi$',ylabel=r'base phase $\theta$',title='Normal circle first');ax.set_aspect('equal');ax.spines[['left','bottom']].set_visible(False)
 ax.text(side*.5,side*.57,r'$d\phi\wedge d\theta$',ha='center',bbox={'facecolor':'#edf5f6','edgecolor':'none','pad':3});ax.text(side*.5,side*.42,'opposite edges identified',ha='center',fontsize=10,bbox={'facecolor':'#edf5f6','edgecolor':'none','pad':3})
 text=fig.add_subplot(gs[0,1]);text.axis('off');text.text(0,.98,'Actual product example (TP18–TP19)',va='top',weight='bold');lines=[r'$U=\mathbb{C}^*\times\mathbb{C}$',r'$Y=\mathbb{C}^*\times\{0\}$',r'$V=(\mathbb{C}^*)^2$',r'$b=\epsilon e^{i\phi},\quad a=e^{i\theta}$',r'$\Omega=(2\pi i)^{-2}(db/b)\wedge(da/a)$',r'$\int_{\tau S^1}\Omega=1$',r'$U\simeq S^1:\ H_3(U;\mathbb{Q})=0$']
 for i,line in enumerate(lines):text.text(0,.84-i*.115,line,va='top',fontsize=13)
 bottom=fig.add_subplot(gs[1,:]);bottom.axis('off');bottom.text(.02,.93,'General receiver at d=2: proof interfaces stay explicit',weight='bold');bottom.text(.02,.71,r'$H_3(U)\longrightarrow H_3(U,V)\longrightarrow H_2(V)$',fontsize=19);bottom.text(.02,.53,r'$H_3(U,V)\ \cong\ H_1(Y)$  requires the oriented normal Thom comparison',fontsize=13);bottom.text(.02,.32,r'$H_c^1(U)\longrightarrow H_c^1(Y)\longrightarrow H_c^2(V)$',fontsize=19);bottom.text(.02,.14,'PD dimensions 4 / 2 / 4; closed–open and tube compatibility required.',fontsize=13);write(fig,out/'normal-first-tube-and-degrees')
 geometry={'schema':'AN02-TP041-figure-geometry/v1','projective_exhaustion':{'F':'z0*z1','d':1,'m':2,'rho_t':'2*log(2*cosh(t))','c':'log(25/4)','exact_sublevel_r':['1/2','2'],'Levi_coefficient':'2/(1+r*r)^2','Levi_at_markers':['32/25','1/2','2/25'],'sample_t':[-2.3+4.6*i/600 for i in range(601)],'section_not_whole_manifold':True},'tube':{'d':2,'F':'z0*z1','L':'z2','normal_first_coordinates':['phi','theta'],'both_ranges':['0','2*pi'],'actual_point':['a=exp(i*theta)','b=epsilon*exp(i*phi), epsilon>0'],'orientation':'dphi wedge dtheta','period':1,'opposite_edges_identified':True,'general_interfaces_proved_by_diagram':False}}
 (out/'geometry.json').write_bytes((json.dumps(geometry,indent=2)+'\n').encode())
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent/'figures');main(parser.parse_args().out)

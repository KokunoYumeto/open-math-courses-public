"""Reproduce the exact finite quotient, lattice subdivision and two charts."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Polygon
matplotlib.rcParams['svg.hashsalt']='finite-toroidal-cover'
pa=argparse.ArgumentParser()
pa.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
args=pa.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
bg='#f5f8fd';blue='#2466a3';green='#147e6b';orange='#bc6828';ink='#203d55';muted='#536b83'
fig=plt.figure(figsize=(10,20),facecolor=bg)
fig.text(.5,.976,'A finite cover and its whole SNC modification',ha='center',fontsize=24,color=ink)
fig.text(.5,.952,'A. Actual global maps, TF.1–TF.4',ha='center',fontsize=20,color=muted)
ax=fig.add_axes([.045,.844,.91,.098]);ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.add_patch(FancyBboxPatch((.01,.02),.98,.95,boxstyle='round,pad=.007',facecolor='white',edgecolor='#adc4da'))
for x,label in [(.13,r'$Z$'),(.5,r'$N$'),(.88,r'$Y$')]:ax.text(x,.72,label,ha='center',fontsize=28,color=blue)
for a,b,label in [(.21,.42,r'$\mu$'),(.59,.80,r'$f$')]:
 ax.annotate('',(b,.76),(a,.76),arrowprops={'arrowstyle':'->','lw':2,'color':green})
 ax.text((a+b)/2,.86,label,ha='center',fontsize=22,color=green)
ax.text(.5,.43,r'$Z\setminus D=V\ \longrightarrow\ U=Y\setminus E$',ha='center',fontsize=21,color=blue)
ax.text(.5,.18,'Finite degree n off E; D is SNC.',ha='center',fontsize=18,color=muted)
fig.text(.5,.814,'B. The quotient w² = xy: lattice star, TF.40–TF.44',ha='center',fontsize=19,color=muted)
fan=fig.add_axes([.24,.58,.52,.22],facecolor='white')
fan.add_patch(Polygon([(0,0),(1,0),(.5,.5)],facecolor=blue,alpha=.13))
fan.add_patch(Polygon([(0,0),(.5,.5),(0,1)],facecolor=green,alpha=.13))
points=[(i/2,j/2)for i in range(3)for j in range(3)if (i-j)%2==0]
fan.scatter([a for a,b in points],[b for a,b in points],c=ink,s=30,zorder=5)
for end,c in [((1,0),blue),((0,1),blue),((1.03,1.03),green)]:
 fan.annotate('',end,(0,0),arrowprops={'arrowstyle':'->','lw':2.5,'color':c})
fan.plot([0,1,1,0,0],[0,0,1,1,0],ls='--',color=muted,lw=1.2)
fan.text(.45,.25,'mult = 1',fontsize=17,color=blue)
fan.text(.06,.63,'mult = 1',fontsize=17,color=green)
fan.text(.53,.51,'v* = (½, ½)',fontsize=17,color=green)
fan.text(.88,-.08,'(1, 0)',fontsize=16,color=blue)
fan.text(-.05,1.08,'(0, 1)',fontsize=16,color=blue)
fan.set_xlim(-.08,1.20);fan.set_ylim(-.12,1.20);fan.set_aspect('equal')
fan.set_xticks([0,.5,1]);fan.set_yticks([0,.5,1]);fan.tick_params(labelsize=15)
fan.grid(alpha=.15);fan.set_xlabel('first lattice coordinate',fontsize=16);fan.set_ylabel('second coordinate',fontsize=16)
fig.text(.5,.526,r'$N_M=\mathbb{Z}^2+\mathbb{Z}(\frac{1}{2},\frac{1}{2}),\quad \operatorname{mult}(\sigma)=2$',ha='center',fontsize=22,color=blue)
fig.text(.5,.506,'Equal coordinate scales; dots are lattice points. Covolume = ½.',ha='center',fontsize=15,color=muted)
fig.text(.5,.473,'C. Normalized blowup of (x, y), TF.41–TF.43',ha='center',fontsize=20,color=muted)
fig.text(.5,.442,r'$(x,s)\ \longmapsto\ (x,\ xs^2,\ xs)$',ha='center',fontsize=24,color=green)
fig.text(.5,.418,r'$(y,t)\ \longmapsto\ (yt^2,\ y,\ yt)$',ha='center',fontsize=24,color=blue)
fig.text(.5,.389,r'$t=s^{-1},\quad y=xs^2\qquad(s\ne0)$',ha='center',fontsize=22,color=ink)
fig.text(.5,.368,r'$\{x=0\}\simeq\mathbb{C}_s\quad\cup_{\,t=1/s}\quad\{y=0\}\simeq\mathbb{C}_t$',ha='center',fontsize=20,color=green)
fig.text(.5,.346,r'Entire exceptional fibre: $\mathbb{P}^1$, including $s=0$ and $t=0$.',ha='center',fontsize=17,color=muted)
fig.text(.5,.308,'D. Real slices of the two smooth charts, TF.45',ha='center',fontsize=20,color=muted)
for left,labels in [(.09,('x','s')),(.58,('y','t'))]:
 a=fig.add_axes([left,.135,.33,.165],facecolor='white')
 a.axvline(0,color=orange,lw=2.4);a.axhline(0,color=green,lw=2.4)
 a.set_xlim(-1.1,1.1);a.set_ylim(-1.1,1.1);a.set_aspect('equal');a.grid(alpha=.16)
 a.set_xlabel('Re '+labels[0],fontsize=17);a.set_ylabel('Re '+labels[1],fontsize=17)
 a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1]);a.tick_params(labelsize=15)
 a.text(.13,.12,labels[1]+' = 0',fontsize=14,color=green)
 a.text(.08,.82,labels[0]+' = 0',fontsize=14,color=orange)
fig.text(.255,.094,r'$xy=x^2s^2,\quad J_{(x,s)}=2xs$',ha='center',fontsize=18,color=green)
fig.text(.745,.094,r'$xy=y^2t^2,\quad J_{(y,t)}=-2yt$',ha='center',fontsize=18,color=blue)
fig.text(.5,.061,'Im x = Im s = 0, or Im y = Im t = 0; equal axes.',ha='center',fontsize=16,color=muted)
fig.text(.5,.039,'The complex charts have dimension two. Map and gluing panels have no metric scale.',ha='center',fontsize=13,color=muted)
fig.savefig(out/'finite-toroidal-cover.png',dpi=180,metadata={'Software':'Matplotlib'})
fig.savefig(out/'finite-toroidal-cover.svg',metadata={'Date':None})
plt.close(fig)
data={'proofs':['TF.1–TF.4','TF.38–TF.45'],'finite_cover_degree':'n',
 'quotient':{'group':'(u,v)~(-u,-v)','x':'u^2','y':'v^2','w':'uv','equation':'w^2=xy','basis_over_base':['1','w']},
 'lattice':{'basis':[[1,0],['1/2','1/2']],'primitive_rays':[[1,0],[0,1]],'inserted_ray':['1/2','1/2'],'old_multiplicity':2,'new_multiplicities':[1,1],'equal_axes':True,'covolume':'1/2'},
 'normalized_blowup_ideal':['x','y'],
 'x_chart':{'coordinates':['x','s'],'map':['x','x*s^2','x*s'],'boundary':'x^2*s^2','jacobian':'2*x*s'},
 'y_chart':{'coordinates':['y','t'],'map':['y*t^2','y','y*t'],'boundary':'y^2*t^2','jacobian':'-2*y*t'},
 'overlap':{'t':'1/s','y':'x*s^2','domain':'s!=0'},'exceptional_fibre':'P^1= C_s union_(t=1/s) C_t',
 'real_slices':{'all_imaginary_coordinates':0,'each_axis_bounds':['-11/10','11/10'],'equal_axes':True}}
(out/'finite-toroidal-cover-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

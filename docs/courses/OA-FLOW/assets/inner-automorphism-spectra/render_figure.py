from pathlib import Path
from fractions import Fraction as Q
import json,sys,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
import numpy as np
E=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else E/'assets';out.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'L122-exact-inner-spectra-20261005'})
z=(Q(15,17),Q(8,17));one=(Q(1),Q(0));minus=(-Q(1),Q(0))
def conj(a):return (a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ds(a,b):return (a[0]-b[0])**2+(a[1]-b[1])**2
values=[one,z,minus];support=[ds(w,one)<Q(1,4) for w in values]
assert support==[True,True,False] and mul(z,conj(z))==one
assert ds(z,one)==Q(4,17)<Q(1,4)
corner=[[mul(a,conj(b)) for b in values[:2]] for a in values[:2]]
assert set(sum(corner,[]))=={one,z,conj(z)}
factor=[[mul(a,conj(b)) for b in [one,minus]] for a in [one,minus]]
assert factor==[[one,minus],[minus,one]]
assert all(ds(w,one)<=1 for row in corner for w in row)
def enc(w):return [str(w[0]),str(w[1])]
data={'exact_rational_complex_pairs_real_imag':True,'implementer_spectrum':[enc(w) for w in values],'lambda':enc(one),'delta':'1/2','distance_squared_z_to_one':'4/17','support_diagonal':[int(x) for x in support],'corner_matrix_unit_eigenvalues':[[enc(w) for w in row] for row in corner],'factor_M2_eigenvalues':[[enc(w) for w in row] for row in factor],'abelian_C2_present_cells':[[True,False],[False,True]],'abelian_operator_spectrum':[enc(one)],'norm_upper_bound':'2delta=1; exact operator norm not asserted','all_exact_checks_passed':True}
(out/'inner-spectra-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
fig=plt.figure(figsize=(14,10),dpi=180)
fig.suptitle('Small supports localize conjugation; factors supply bridges',fontsize=20,y=.966)
gs=fig.add_gridspec(2,2,left=.07,right=.95,bottom=.09,top=.88,hspace=.39,wspace=.24,height_ratios=[1.1,1])
blue='#2475b2';green='#27835a';red='#b14848';grey='#bbc0c5';texts=[]
def plane(ax,title,radius,color):
 ax.set_aspect('equal');ax.set_xlim(-1.42,2.30);ax.set_ylim(-1.40,1.40)
 ax.axhline(0,color='#d3d6d9',lw=.7);ax.axvline(0,color='#d3d6d9',lw=.7)
 ax.add_patch(Circle((0,0),1,fill=False,color=grey,lw=1.4))
 ax.add_patch(Circle((1,0),radius,color=color,alpha=.12))
 ax.add_patch(Circle((1,0),radius,fill=False,color=color,lw=1.8))
 ax.set_xticks([-1,0,1,2]);ax.set_yticks([-1,0,1]);ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part')
 ax.set_title(title,loc='left',fontsize=15,pad=16)
 texts.append(ax.text(-1.27,-1.25,'Unit circle: reference only',fontsize=10,color='#616b75'))
 for spine in ax.spines.values():spine.set_color('#d3d6d9')
def point(ax,w,color,label,offset):
 x,y=map(float,w);ax.scatter([x],[y],s=68,c=color,zorder=5)
 texts.append(ax.annotate(label,(x,y),xytext=offset,textcoords='offset points',fontsize=12,color=color))
ax=fig.add_subplot(gs[0,0]);plane(ax,'A  Support of f(u): keep 1 and z',.5,blue)
point(ax,one,blue,'1 = λ',(10,-19));point(ax,z,blue,'z = (15+8i)/17',(-118,18));point(ax,minus,red,'−1 excluded',(-15,17))
texts.append(ax.text(1.59,.56,'Radius δ = 1/2',fontsize=11,color=blue))
texts.append(ax.text(-1.23,1.08,'e = diag(1,1,0)',fontsize=12))
ax=fig.add_subplot(gs[0,1]);plane(ax,'B  Spectrum of Ad(uₑ): 1, z, z̄',1,green)
point(ax,one,green,'1',(10,-6));point(ax,z,green,'z',(-20,18));point(ax,conj(z),green,'z̄',(-20,-24))
texts.append(ax.text(1.12,1.14,'Radius 2δ = 1',fontsize=11,color=green))
texts.append(ax.text(-1.23,.79,'|z−1| = 2/√17',fontsize=11))
def grid(ax,title,present):
 ax.set_xlim(0,2);ax.set_ylim(2,0);ax.set_aspect('equal');ax.axis('off')
 ax.set_title(title,loc='left',fontsize=15,pad=23)
 for i in range(2):
  for j in range(2):
   exists=present[i][j];diag=i==j;color=green if diag else blue
   rect=Rectangle((j,i),1,1,facecolor=color if exists else '#eef0f2',edgecolor='white',linewidth=3,alpha=.18 if exists else 1,hatch=None if exists else '///')
   ax.add_patch(rect)
   label=f'e{i+1}{j+1}\n'+('+1' if diag else '−1') if exists else 'absent'
   texts.append(ax.text(j+.5,i+.5,label,ha='center',va='center',fontsize=17,color=color if exists else '#737c85'))
 for j in range(2):texts.append(ax.text(j+.5,-.1,f'column {j+1}',ha='center',fontsize=11))
 for i in range(2):texts.append(ax.text(-.09,i+.5,f'row {i+1}',va='center',ha='right',fontsize=11))
 texts.append(ax.text(1,2.21,'Sp(Ad u) = '+('{1, −1}' if all(sum(present,[])) else '{1}'),ha='center',fontsize=14))
grid(fig.add_subplot(gs[1,0]),'C  Factor M₂: off-diagonal bridges',[[True,True],[True,True]])
grid(fig.add_subplot(gs[1,1]),'C  Abelian C ⊕ C: no bridges',[[True,False],[False,True]])
texts.append(fig.text(.5,.025,'Both lower implementers have Sp(u) = {1, −1}. Hatched cells are absent spaces, never zero eigenvalues.',ha='center',fontsize=12))
fig.canvas.draw();renderer=fig.canvas.get_renderer();W,H=fig.canvas.get_width_height()
bad=[]
for i,t in enumerate(texts):
 b=t.get_window_extent(renderer)
 if b.x0<0 or b.y0<0 or b.x1>W or b.y1>H:bad.append({'text':t.get_text(),'bounds':[float(x) for x in [b.x0,b.y0,b.x1,b.y1]]})
assert not bad,bad
layout={'canvas_pixels':[W,H],'all_explicit_label_extents_within_canvas':True,'labels_checked':len(texts),'reference_circles_not_spectrum':True,'native_inspection_required':True}
(out/'inner-spectra-layout.json').write_text(json.dumps(layout,indent=2)+'\n',encoding='utf8',newline='\n')
fig.savefig(out/'inner-spectra.png',metadata={'Software':'L122 reproducible native renderer'})
fig.savefig(out/'inner-spectra.svg',metadata={'Date':'2026-10-05','Creator':'L122 reproducible native renderer'})
plt.close(fig)
print(json.dumps({'exact_checks':True,'labels':len(texts),'outputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.glob('inner-spectra*'))}}))

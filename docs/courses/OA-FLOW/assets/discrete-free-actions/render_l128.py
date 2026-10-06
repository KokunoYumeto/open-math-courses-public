from pathlib import Path
import sys,argparse,json,hashlib
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
sys.path.insert(0,str(Path(__file__).resolve().parent))
E=Path(__file__).resolve().parent
arg=argparse.ArgumentParser();arg.add_argument('--output',type=Path,default=E/'figures');a=arg.parse_args()
a.output.mkdir(exist_ok=True,parents=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'l128-discrete-columns-orbits-v1','pdf.fonttype':42,'axes.unicode_minus':False})
def finish(fig,name):
 for ext in ['png','svg','pdf']:
  meta={'Software':'Original L128 mathematical construction'} if ext=='png' else {'Date':None,'Creator':'Original L128 mathematical construction'} if ext=='svg' else {'CreationDate':None,'ModDate':None,'Creator':'Original L128 mathematical construction'}
  fig.savefig(a.output/(name+'.'+ext),dpi=160,metadata=meta,facecolor='white')
 plt.close(fig)
fig=plt.figure(figsize=(13,8));ax=fig.add_axes([.05,.12,.9,.79]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
fig.text(.05,.94,'Fourier columns and the inner-carrier obstruction',fontsize=21,weight='bold')
panels=[
 (.02,.58,.46,.36,'Free flip on C²',[
  'G = Z/2Z;  s swaps the two coordinates',
  'diag(C²) and U = [[0,1],[1,0]] generate M₂',
  'x = diag(1,2) + diag(3,4) U = [[1,3],[4,2]]',
  'E(x* x) = diag(17,13)',
  'E(x x*) = diag(10,20)']),
 (.52,.58,.46,.36,'Inner action on M₂',[
  'W = diag(1,−1);  αs = Ad W',
  'v = π(W)* us is a central involution',
  'v² = 1;  v is not scalar (its s coefficient ≠ 0)',
  'Crossed product = M₂ ⊗ C²',
  'The central projections are (1+v)/2 and (1−v)/2']),
 (.02,.04,.96,.44,'The exact positive tail',[
  'Keep F = {e}:  SF(x) = diag(1,2)',
  'E((x − SF(x))* (x − SF(x))) = αs(diag(9,16)) = diag(16,9)',
  'For φ(diag(d₁,d₂)) = (d₁+d₂)/2, squared Hilbert error = 25/2.',
  'The proved general limit is the normal Hilbert-seminorm limit (FC5–FC6).',
  'This finite computation makes no claim about raw strong* Fourier convergence.'])]
for x,y,w,h,title,lines in panels:
 ax.add_patch(plt.Rectangle((x,y),w,h,facecolor='#eef4f9',edgecolor='#284b63',lw=1.4))
 ax.text(x+.018,y+h-.025,title,weight='bold',fontsize=16,va='top')
 for i,t in enumerate(lines):ax.text(x+.018,y+h-.095-i*.055,t,fontsize=12.1,va='top')
fig.text(.05,.035,'FC0–FC4, FC6 and WK0. The 2 × 2 flip model is faithfully isomorphic to the four-dimensional regular representation.',fontsize=10.5)
finish(fig,'fourier-inner-carrier')
fig=plt.figure(figsize=(13,8));fig.text(.045,.945,'Orbit coordinates: six points, two inequivalent representations',fontsize=19,weight='bold')
ax=fig.add_axes([.04,.17,.46,.69]);ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-1.5,1.5),ylim=(-1.4,1.4))
angles=np.pi*np.arange(6)/3;pts=np.column_stack((np.cos(angles),np.sin(angles)))
for parity,col in [(0,'#126b78'),(1,'#b85c18')]:
 idx=np.arange(parity,6,2)
 for j in idx:
  k=(j+2)%6
  ax.annotate('',xy=pts[k]*.92,xytext=pts[j]*.92,arrowprops={'arrowstyle':'->','color':col,'lw':2,'connectionstyle':'arc3,rad=.12'})
 ax.scatter(pts[idx,0],pts[idx,1],s=170,color=col,zorder=3)
for j,pt in enumerate(pts):ax.text(*(pt*1.18),str(j),ha='center',va='center',fontsize=17,weight='bold')
ax.text(0,-1.35,'Exact points: exp(iπj/3),  j = 0,…,5',ha='center',fontsize=12)
tx=fig.add_axes([.54,.17,.42,.69]);tx.axis('off')
lines=[
 ('The action is h · j = j + 2h (mod 6).',True),
 ('G = Z/3Z; uniform probability on all six points.',False),
 ('It is free, with orbits {0,2,4} and {1,3,5}.',False),
 ('For ρj(f), coordinate h reads f(j + 2h).',False),
 ('Move j to j+2:  V₁ δh = δh−1  (mod 3).',True),
 ('h = 0 → 2     h = 1 → 0     h = 2 → 1',False),
 ('The right shift commutes with all left shifts.',False),
 ('Same orbit: unitarily equivalent irreducibles.',False),
 ('Different orbits: all intertwiner entries vanish.',False),
 ('The algebra is M₃ ⊕ M₃; its center is C².',True),
 ('The actual regular Hilbert space has dimension 18.',False)]
for i,(t,bold) in enumerate(lines):tx.text(0,.97-i*.080,t,fontsize=12,weight='bold' if bold else 'normal',va='top')
fig.text(.045,.075,'OS0–OS2 and WK0: all six support-point states are pure; the diagonal integral is orthogonal.',fontsize=12)
fig.text(.045,.040,'This finite model is outside the countably infinite, free ergodic type-classification hypotheses. Here every density dg equals 1.',fontsize=10.5)
finish(fig,'orbit-coordinate-shift')
font=Path(font_manager.findfont('DejaVu Sans'))
(a.output/'EXACT_MODEL.json').write_text(json.dumps({'free_flip':{'x':[[1,3],[4,2]],'E_xstar_x':[17,13],'E_x_xstar':[10,20],'positive_tail':[16,9],'squared_Hilbert_error':'25/2','regular_representation_dimension':4,'faithful_matrix_model_dimension':2},'inner_action':{'W':[[1,0],[0,-1]],'center_dimension':2,'v_formula':'pi(W)^*u_s','v_squared':1},'orbit':{'points_exact':['exp(i*pi*'+str(j)+'/3)' for j in range(6)],'action':'j+2*h mod6','orbits':[[0,2,4],[1,3,5]],'right_shift_inverse':[2,0,1],'regular_H_dimension':18,'algebra':'M3 direct_sum M3','densities':1},'font':{'family':'DejaVu Sans','license':'FONT-LICENSE.txt'}},indent=2)+'\n',encoding='utf8')
print(json.dumps({'output':str(a.output),'rendered_assets':6,'font':str(font)}))


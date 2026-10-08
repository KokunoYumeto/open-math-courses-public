"""Reproduce the original modular-gap figure from local data and fonts."""
from pathlib import Path
import argparse,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--font-dir',type=Path,default=P.parent/'typeiii-zero-decomposition')
args=parser.parse_args()
data=json.loads((P/'data.json').read_text())
for name in ['DejaVuSans.ttf','DejaVuSans-Bold.ttf']:fm.fontManager.addfont(str(args.font_dir/name))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'path','svg.hashsalt':'oa-flow-lac-20261007','axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#192d45','text.color':'#192d45','xtick.color':'#192d45','ytick.color':'#192d45'})
b=(math.sqrt(5)-1)/2;c=math.log(2);eps=1/20
assert 0<eps<min(.5,1-b)
rho=lambda x:np.where(np.mod(x,1)<.5,.25,.5)
assert rho(eps/2)==.25 and rho(b+eps/2)==.5 and rho((b+eps/2)-b)==.25
fig=plt.figure(figsize=(15,10.8),dpi=160,facecolor='#f5f8fc')
gs=fig.add_gridspec(2,2,left=.075,right=.965,bottom=.19,top=.855,wspace=.27,hspace=.57)
ax=fig.add_subplot(gs[0,0]);ax.set_title('A. The left coefficient is transported by the return',loc='left',pad=16,fontweight='bold')
xs=np.array([0,b-.5,.5,b,1]);vals=rho((xs[:-1]+xs[1:])/2)
ax.stairs(vals,xs,baseline=None,color='#2465a5',lw=2.8,label='right density ρ(ω)')
vals2=rho((xs[:-1]+xs[1:])/2-b);ax.stairs(vals2,xs,baseline=None,color='#c05a14',lw=2.4,linestyle='--',label='left density θ(ρ)(η) = ρ(T⁻¹η)')
ax.axvspan(0,eps,color='#168070',alpha=.15);ax.axvspan(b,b+eps,color='#168070',alpha=.15)
ax.set(xlim=(0,1),ylim=(.12,.68),xticks=[0,b-.5,.5,b,1],xticklabels=['0','b − 1/2','1/2','b','1'],yticks=[.25,.5],yticklabels=['1/4','1/2'],xlabel='circle coordinate;  b = (√5 − 1)/2')
ax.legend(loc='upper left',frameon=False,fontsize=10)
ax.text(eps/2,.16,'I',ha='center',color='#168070');ax.text(b+eps/2,.16,'TI',ha='center',color='#168070')
ax.text(0,-.38,'At t = π/log 2 on u1_I: correct right phase +1;\nunchanged left density gives −1.  [LACM4]',transform=ax.transAxes,fontsize=10)
ax=fig.add_subplot(gs[0,1]);ax.set_title('B. A gap in the full operator spectrum',loc='left',pad=16,fontweight='bold')
ax.set(xlim=(-3.3,3.3),ylim=(-.9,.9),yticks=[],xticks=[-3,-2,-1,0,1,2,3],xlabel='modular frequency s / log 2 = −log(a) / log 2')
ax.spines['left'].set_visible(False);ax.spines['bottom'].set_position(('data',0))
ax.plot([-3.05,-1],[0,0],lw=10,color='#a1bbd5',solid_capstyle='butt');ax.plot([1,3.05],[0,0],lw=10,color='#a1bbd5',solid_capstyle='butt')
ax.annotate('',(-3.25,0),(-2.75,0),arrowprops={'arrowstyle':'->','color':'#2465a5','lw':2});ax.annotate('',(3.25,0),(2.75,0),arrowprops={'arrowstyle':'->','color':'#2465a5','lw':2})
ax.scatter([-1,0,1],[0,0,0],s=75,c=['#2465a5','#168070','#2465a5'],zorder=5)
for x,label in [(-1,'a = 2'),(0,'a = 1'),(1,'a = 1/2')]:ax.text(x,.2,label,ha='center',fontsize=10)
ax.text(0,.6,'No spectrum between these three points',ha='center',fontsize=11)
ax.text(-2.1,-.66,'possible\nspectrum',ha='center',fontsize=10);ax.text(2.1,-.66,'possible\nspectrum',ha='center',fontsize=10)
ax.text(0,-.38,'The three marked points are attained; the rays are only bounds.\nThe modular fixed algebra is the entire coefficient N.  [LAC3, LACM3]',transform=ax.transAxes,fontsize=10)
ax=fig.add_subplot(gs[1,0]);ax.set_title('C. Equal initial carriers need not give equal final carriers',loc='left',pad=16,fontweight='bold');ax.set(xlim=(-.3,3.4),ylim=(-.6,4.9));ax.axis('off')
for n in range(5):
 y=4-n;ax.scatter([.25],[y],s=60,color='#2465a5');ax.scatter([2.65],[y],s=60,color='#b9cadb' if n==0 else '#168070')
 ax.text(-.07,y,f'e{n}',va='center',ha='right');ax.text(2.9,y,f'e{n}',va='center')
 if n<4:ax.annotate('',(2.58,y-1),(.33,y),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#168070'})
ax.scatter([2.65],[4],marker='x',s=160,lw=2.5,color='#b22e47')
ax.text(.25,4.65,'initial 1',ha='center',fontweight='bold');ax.text(2.65,4.65,'final 1 − e₀₀',ha='center',fontweight='bold')
ax.text(.25,-.48,'⋮',ha='center',fontsize=19);ax.text(2.65,-.48,'⋮',ha='center',fontsize=19)
ax.text(0,-.29,'S e_n = e_(n+1);  S*S = 1,  SS* < 1.\nOnly the first five basis vectors are drawn.  [LACM6]',transform=ax.transAxes,fontsize=10)
ax=fig.add_subplot(gs[1,1]);ax.set_title('D. Repair the two residual supports separately',loc='left',pad=16,fontweight='bold');ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text,col):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.018',facecolor=col,edgecolor='#8ca8c4',lw=1));ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=10)
box(.1,.79,.8,.13,'primitive product  a = w₁ ··· w_k','#e2ebf5')
box(.025,.45,.425,.2,'initial projection\nf = a*a ≤ 1 − e','#e2f2ed');box(.55,.45,.425,.2,"final projection\nf′ = aa* ≤ 1 − e′",'#f7e8da')
box(.025,.11,.425,.18,'restrict the last factor\nw_k f','#e2f2ed');box(.55,.11,.425,.18,"restrict the first factor\nf′ w₁",'#f7e8da')
for x,y,tox,toy in [(.37,.78,.23,.67),(.63,.78,.77,.67),(.23,.44,.23,.31),(.77,.44,.77,.31)]:ax.annotate('',(tox,toy),(x,y),arrowprops={'arrowstyle':'->','lw':1.6,'color':'#192d45'})
ax.text(0,-.29,'Each nonzero central restriction stays primitive.\nThe maximal-family argument needs both repairs.  [LAC26–27]',transform=ax.transAxes,fontsize=10)
fig.text(.075,.955,'From a modular gap to a discrete generating unitary',fontsize=23,fontweight='bold')
fig.text(.075,.913,'Exact scalar model, full-spectrum bounds and the two support corrections',fontsize=13)
fig.text(.075,.033,'Proofs: Sections 4, 5 and 7 of Recovering a discrete system from a modular spectral gap.\nThe carrier panel is a finite schematic of an infinite isometry; no human source image is used.',fontsize=10)
fig.savefig(P/'lacunary-normalizers.png',dpi=160,metadata={'Software':'OA-FLOW original reproducible renderer'})
fig.savefig(P/'lacunary-normalizers.svg',metadata={'Date':None,'Creator':'OA-FLOW original reproducible renderer'})
plt.close(fig)
print(json.dumps({'size_px':[2400,1728],'exact_order_checks':True,'files':['lacunary-normalizers.png','lacunary-normalizers.svg']}))

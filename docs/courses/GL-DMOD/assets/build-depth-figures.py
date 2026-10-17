from pathlib import Path
import os,json,math
os.environ['MPLCONFIGDIR']=str(Path(__file__).resolve().parent/'matplotlib-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path)
args=parser.parse_args()
out=args.output_dir.resolve() if args.output_dir else root
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'full-infinite-support-depth-v1'})
metadata={'Date':None,'Creator':'Reproducible mathematical proof diagram'}
fig=plt.figure(figsize=(18,12),dpi=100)
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,18);ax.set_ylim(0,12);ax.axis('off')
def box(x,y,w,h,title,body,fc='#eff5fb',fs=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.14',fc=fc,ec='#607891',lw=1.3))
    ax.text(x+.18,y+h-.30,title,fontsize=17,fontweight='bold',va='top')
    ax.text(x+.18,y+h-.85,body,fontsize=fs,va='top',linespacing=1.65)
ax.text(.55,11.62,'Full infinite coefficient support depth',fontsize=25,fontweight='bold')
ax.text(.55,11.18,'Actual auxiliary families → full Laurent primitives → singular-support induction',fontsize=15,color='#355269')
box(.6,8.2,8.1,2.45,'Every-epsilon positive head  ·  SD.A',
    r'$F_+(v,s)=\sum_{j\geq0} j!\,p_j(v)s^j$'+'\n'+
    r'$|p_j|_K\leq B_{K,\epsilon}\epsilon^j/j!\quad(\epsilon>0)$'+'\n'+
    r'$B_+=\pi_*\mathcal{O}_{V\times\mathbb{C}}$'+'  ·  entire in s, one v-domain')
box(9.2,8.2,8.1,2.45,'Factorial negative tail  ·  SD.A–B',
    r'$F_-(v,s)=\sum_{n\geq1}p_{-n}(v)s^{n-1}/n!$'+'\n'+
    r'$|p_{-n}|_K\leq B_KC_K^n n!$'+'\n'+
    r'$B_-=i^{-1}\mathcal{O}_{V\times\mathbb{C}}$'+'  ·  actual germs along s = 0')
ax.text(.6,7.66,'Smooth support S = {w₁ = w₂ = 0}  ·  c = 2  ·  SD.C',fontsize=19,fontweight='bold')
ax.text(.6,7.24,'All Laurent blocks are full auxiliary families; T_J is strictly negative exactly in coordinates J.',fontsize=13)
cols=[(.65,'J = ∅',r'$T_{\varnothing}\;\longrightarrow\;T_{\varnothing}^{\,2}\;\longrightarrow\;T_{\varnothing}$',
       'degrees 0 → 1 → 2\nd₀(a) = (a,a)\nd₁(a,b) = b − a\ncontractible: dh + hd = 1'),
      (5.0,'J = {1}',r'$T_{\{1\}}\;\longrightarrow\;T_{\{1\}}$',
       'degrees 1 → 2\nI = {1} → {1,2}\nd = −identity\ncontractible: dh + hd = 1'),
      (9.35,'J = {2}',r'$T_{\{2\}}\;\longrightarrow\;T_{\{2\}}$',
       'degrees 1 → 2\nI = {2} → {1,2}\nd = +identity\ncontractible: dh + hd = 1'),
      (13.7,'J = {1,2}',r'$T_{\{1,2\}}$',
       'degree 2 only\nI = {1,2}\nremaining support cohomology')]
for x,title,formula,body in cols:
    box(x,4.28,3.65,2.45,title,formula+'\n'+body,fc='#eef8ed' if title=='J = {1,2}' else '#f3f5f7',fs=11.5)
ax.text(.6,3.77,'Singular Z: choose closed analytic W ⊂ Z with dim W < dim Z  ·  SD.D',fontsize=18,fontweight='bold')
box(.65,1.33,16.65,1.99,'Actual supported Godement complexes',
    r'$0\ \longrightarrow\ C_W\ \longrightarrow\ C_Z\ \longrightarrow\ j_*C_{Z\setminus W}\ \longrightarrow\ 0$'+'\n'+
    r'$H^q(C_W)=0\ (q<c+1)\quad+\quad H^q(Rj_*C_{Z\setminus W})=0\ (q<c)$'+'\n'+
    r'$\Longrightarrow\ H_Z^q(B)=0\ (q<c)$'+'  ·  includes every point in W',fc='#fff6e7',fs=14)
ax.text(.65,.74,'SD.E–F: right E action on actual stalk products preserves support; finite Hom commutes termwise with Γ_Z.',fontsize=13)
ax.text(.65,.32,'All displayed maps and degrees are literal. Only degree c = 2 can survive; the proof treats every c and every closed analytic Z.',fontsize=12,color='#355269')
fig.savefig(out/'full-coefficient-depth-mechanism.png',metadata=metadata)
fig.savefig(out/'full-coefficient-depth-mechanism.svg',metadata=metadata)
plt.close(fig)

samples=[(i/250,math.exp(-1)*(1-(i/250)**2)) for i in range(-249,250)]
fig,axs=plt.subplots(1,2,figsize=(14,6),dpi=120,gridspec_kw={'width_ratios':[1.05,1]})
x=[v for v,r in samples];r=[r for v,r in samples]
axs[0].fill_between(x,[-a for a in r],r,color='#ddeefa')
axs[0].plot(x,r,color='#285a87',lw=2);axs[0].plot(x,[-a for a in r],color='#285a87',lw=2)
axs[0].axhline(0,color='#58636a',lw=1);axs[0].set_xlim(-1,1);axs[0].set_ylim(-.45,.45)
axs[0].set_xlabel('v real,  −1 < v < 1');axs[0].set_ylabel('s real')
axs[0].set_title('Exact real slice of an actual auxiliary tube',fontsize=15)
axs[0].text(0,.405,r'$|s|<e^{-1}(1-v^2)$',ha='center',fontsize=16)
axs[0].text(0,-.414,'Open boundaries; zero section lies inside every fibre',ha='center',fontsize=11)
axs[1].axis('off')
axs[1].text(0,1,'SD.B  ·  variable radius with a strict exhaustion',va='top',fontsize=16,fontweight='bold')
axs[1].text(0,.85,
    r'$U=\{|v|<1\}\subset\mathbb{C}$'+'\n\n'+
    r'$\psi_0(v)=-\log(1-|v|^2),\quad\chi(t)=1+t$'+'\n\n'+
    r'$r(v)=e^{-\chi(\psi_0(v))}=e^{-1}(1-|v|^2)$'+'\n\n'+
    r'$t(v,s)=e^{2\chi(\psi_0(v))}|s|^2<1$'+'\n\n'+
    r'$\rho=\psi_0+|s|^2-\log(1-t)$'+'\n\n'+
    'ρ is smooth, strictly plurisubharmonic and proper.\n'+
    'One holomorphic germ family retains every negative index.\n'+
    'The general proof chooses χ to fit the actual datum.',va='top',fontsize=13,linespacing=1.4)
fig.tight_layout()
fig.savefig(out/'auxiliary-variable-tube.png',metadata=metadata)
fig.savefig(out/'auxiliary-variable-tube.svg',metadata=metadata)
plt.close(fig)
data={'figure':'full-coefficient-depth-mechanism','smooth_example_codimension':2,
      'cube_blocks':[{'J':[],'degrees':[0,1,2],'multiplicities':[1,2,1],'d0':'a -> (a,a)','d1':'(a,b) -> b-a'},
                     {'J':[1],'degrees':[1,2],'differential':-1},
                     {'J':[2],'degrees':[1,2],'differential':1},
                     {'J':[1,2],'degrees':[2],'remaining':True}],
      'singular_induction':'dim W < dim Z; Z minus W smooth; H_W below c+1 zero and Rj_* support complex below c zero',
      'tube':{'complex_base_domain':'unit disc','psi0':'-log(1-|v|^2)','chi':'1+t',
              'radius':'exp(-1)*(1-|v|^2)','plotted_real_slice':'v,s real','sample_spacing':'1/250','samples':samples},
      'proved_locators':['SD.A','SD.B','SD.C','SD.D','SD.E','SD.F'],
      'human_source':'https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf I.2.2'}
(out/'full-coefficient-depth-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'media_files':5,'mechanism_px':[1800,1200],'tube_px':[1680,720]}))


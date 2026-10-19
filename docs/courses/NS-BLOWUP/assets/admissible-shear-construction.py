"""Reproduce the exact maps and support order of the finite shear construction."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path'})
fig=plt.figure(figsize=(14,11.2),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1400);ax.set_ylim(1120,0);ax.axis('off')
ink='#183047';blue='#17639b';green='#166e60';orange='#98491d'
def txt(x,y,s,size=14,color=ink,**kw):ax.text(x,y,s,va='top',fontsize=size,color=color,**kw)
def box(x,y,w,h,fill='#e5eef7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
        facecolor=fill,edgecolor='#c5d2dd'))
txt(35,24,'A finite radial modulation completes the leading profile',24)
txt(35,66,'Exact loop mean → actual field → five nonlinear moment corrections → preserved axis and exterior',14)
box(40,116,645,310)
txt(58,132,'1. THE EXACT MEAN — V1–V2',16,blue,weight='bold')
txt(58,175,r'$v=v_s+\rho,\qquad a\langle t-t_s\rangle=0,\qquad a\langle(t-t_s)^2\rangle=\rho$',16)
txt(58,230,r'$\dfrac{d\varphi}{d\theta^\prime}=\dfrac{a(1+t^2)}{2\pi v}$',22)
txt(58,295,r'$(a_L,-b_L)=\dfrac{v(1,t)}{1+t^2}$',22)
txt(58,355,r'$\int_0^1(a_L,-b_L)\,d\varphi=(a,-b_s)$',22)
box(715,116,645,300,'#e4f1ec')
txt(733,132,'2. THE ACTUAL FIELD — V3',16,green,weight='bold')
txt(733,177,r'$\partial_\varphi\mathcal{A}=-\frac{1}{2}(a_L-a)$',20)
txt(733,222,r'$\partial_\varphi\mathcal{B}=\frac{1}{2}E(b_L-b_s)$',20)
txt(733,278,r'$E_N=E\,e^{\mathcal{A}(X,\eta,N\log X)/N}$',20)
txt(733,330,r'$U_N=U+\mathcal{B}(X,\eta,N\log X)/N$',20)
txt(733,383,'Choose one finite N after all profile data are fixed.',12)
txt(40,451,'3. RADIAL ORDER AND EXACT PRESERVATION — V0, V4–V7',16,blue,weight='bold')
box(40,494,1320,247)
positions=[85,245,440,635,830,1030,1290];y=563
ax.plot([positions[0],positions[-1]],[y,y],color=ink,linewidth=2)
labels=[r'$X_a$',r'$X_{\rm an}$',r'$X_-$',r'$X_+$',r'$R_-$',r'$R_+$',r'$X_b$']
for x,label in zip(positions,labels):
    ax.plot([x,x],[y-9,y+9],color=ink);txt(x,y+16,label,18,ha='center')
ax.plot([positions[2],positions[3]],[y,y],color=green,linewidth=9)
ax.plot([positions[4],positions[5]],[y,y],color=orange,linewidth=9)
txt(100,515,'Protected axis collar',13,blue)
txt(432,515,'Modulation',13,green)
txt(810,515,'Moment correction',13,orange)
txt(1080,515,'Protected exterior',13,blue)
txt(66,630,r'$X\geq R_+:\quad\Delta(M,I,J,S,C_p)=0,\qquad\Delta(E,U,\Pi,V_0,Q_s,N_s)=0$',20)
txt(66,690,'Both stress-edge factors and the two later reserved patches remain exactly as constructed.',13)
box(40,776,1320,265,'#fff0e5')
txt(60,794,'4. THE EXACT ENDPOINT PRESSURE COEFFICIENT — V8.10–V8.18',16,orange,weight='bold')
txt(60,840,r'$\Delta C_p(X_+)=\dfrac{1}{N^2}\int_{X_-}^{X_+}\dfrac{E^2}{X}\langle\mathcal{A}^2\rangle_\varphi\,dX+O(N^{-3})$',24)
txt(60,927,r'$c_N=-N^{-2}B^{-1}\mathscr{R}\mathbf{D}+O(N^{-3}),\qquad Bc_N+\mathscr{Q}(c_N,c_N)=d_N$',20)
txt(60,982,'Every original moment weight is retained. The nonlinear correction cancels the full discrepancy exactly.',13)
txt(60,1012,'Small endpoint error controls the correction; radial derivatives of the modulation need not be small.',13)
txt(40,1061,'Radial positions show order, not scale. Periodic averages are auxiliary phase averages, not physical angular averages.',11)
txt(40,1086,'Source: OpenAI, Theorem 4.6 and Appendix C, pp.31–38,157–165. Full proofs: N2.5 V0–V8. Figure source: CC0.',11)
fig.savefig(HERE/'admissible-shear-construction.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Title':'Finite shear construction and exact moment restoration'})
fig.savefig(HERE/'admissible-shear-construction.png',dpi=100);plt.close(fig)
p=HERE/'admissible-shear-construction.svg';t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="806.4pt"' in t
p.write_text(t.replace('width="1008pt" height="806.4pt"','width="1400" height="1120"'),encoding='utf8')

"""Reproduce the exact construction and correction diagram in N2.4."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Rectangle
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path'})
fig=plt.figure(figsize=(14,12.4),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1400);ax.set_ylim(1240,0);ax.axis('off')
ink='#183047';blue='#17639b';green='#166e60';orange='#9a4a1c'
def txt(x,y,s,size=14,color=ink,**kw):ax.text(x,y,s,va='top',fontsize=size,color=color,**kw)
def box(x,y,w,h,fill='#e5eef7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
        facecolor=fill,edgecolor='#c5d2dd'))
txt(35,25,'One actual connection, five exact moment equations',24)
txt(35,68,'Inner stress activation → fixed-length transition → axial restoration → exact moment cancellation',14)
txt(40,115,'RADIAL ORDER — Q0–Q9',15,blue,weight='bold')
cards=[
    ('Analytic axis and first stress collar',r'$X_0=4/\Lambda,\quad 0<t_c<t_1,\quad X\leq X_0e^{t_c}$','Later modifications preserve this entire inner rectangle.'),
    ('Small shear, then the two final slope changes',r'$X_b^{\rm loc}=100,\quad X_i=110,\quad a=.8,\quad U_X=0$','The strict relaxed cone holds through the continuation.'),
    ('The angular transition has a fixed length',r'$X_{\rm sep}=X_i e^{T_{\rm sh}}$','Choose T_sh before the final amplitude C.'),
    ('The matching scale retains its amplitude factors',r'$X_R=X_i(\mathsf{C}P_*)^{10},\quad x=X/X_R$','The interval before X_sep is fixed while X_R grows.'),
    ('Restore the axial field',r'$-8<\log x<-7,\quad U=4\eta+\rho(x)(G_i-4\eta)$','The angular profile is already exactly the ideal one.'),
    ('Correct all five cumulative moments',r'$-6<\log x<-5$','Two axial bumps and three angular bumps have disjoint supports.'),
    ('Continue with the full actual outer field',r'$\log x=-5:\quad \Delta(M,I,J,S,C_p)=0$','Pressure, radial velocity and stress then agree exactly.')
]
for i,(a,b,c) in enumerate(cards):
    y=155+i*122;box(40,y,625,105)
    txt(57,y+12,str(i+1)+'. '+a,14,blue,weight='bold')
    txt(57,y+40,b,16);txt(57,y+77,c,11)
    if i<6:ax.annotate('',xy=(352,y+121),xytext=(352,y+106),arrowprops=dict(arrowstyle='->',color=blue))
txt(710,115,'EVERY ORIGINAL SCALE FACTOR — Q7',15,green,weight='bold')
box(710,155,645,225,'#e4f1ec')
txt(730,173,r'$M=X_R\widehat{M},\qquad S=X_R\widehat{S}$',20)
txt(730,218,r'$I=X_R^{3/2}\widehat{I},\qquad J=X_R^{3/2}\widehat{J}$',20)
txt(730,265,r'$C_p=\widehat{C}_p,\qquad \Pi=\Pi_0+\widehat{C}_p$',20)
txt(730,311,r'$p_s=\dfrac{X_Rx}{L}(Q_s,N_s/E)$',20)
txt(710,411,'DISJOINT SUPPORTS GIVE EXACT BLOCKS — EXERCISE 4',13,orange,weight='bold')
box(710,450,645,330,'#fff0e5')
txt(730,466,r'$a_0=e^{-6},\quad b_0=e^{-5},\quad \omega=(b_0-a_0)/20$',16)
txt(730,506,r'$c_j=a_0+j(b_0-a_0)/6$',16)
x0=750;length=555;y=566
ax.plot([x0,x0+length],[y,y],color=ink)
for j in range(1,6):
    center=x0+j*length/6;half=length/20
    ax.add_patch(Rectangle((center-half,y-14),2*half,28,color=blue if j<3 else orange,alpha=.65))
    txt(center,y+28,('U'+str(j)) if j<3 else ('E'+str(j-2)),12,ha='center')
txt(x0-10,y+28,r'$a_0$',12,ha='right');txt(x0+length+10,y+28,r'$b_0$',12)
txt(730,620,r'$ue=0,\qquad u^2=\sum_i a_i^2\beta_i^2,\qquad e^2=\sum_j b_j^2\beta_{j+2}^2$',14)
txt(730,674,r'$\mathbf{a}=B_U^{-1}(d_1,d_2)^T$',20)
txt(730,718,r'$B_E\mathbf{b}+q_E(\mathbf{b},\mathbf{b})=\mathbf{r}$',20)
txt(710,814,'THE ACTUAL INNER EDGE — EXERCISES 1, 2, 5',14,green,weight='bold')
box(710,853,645,139,'#e4f1ec')
txt(730,871,r'$e_a=e^{-t_1^2/y^2}g_a(y),\qquad g_a(0)>0$',18)
txt(730,916,r'$\Delta\Pi=e_a y^6B_\Pi,\qquad B_\Pi(0)=\dfrac{E_e^2p_e}{8t_1^4}>0$',18)
box(40,1043,1315,128)
txt(60,1058,'Same complete radial Taylor data; different nearby fields',17,blue,weight='bold')
txt(60,1092,r'$\log\phi-\log\phi_{\rm nat}=\frac{1}{2}\int_0^y e_a(v)p_{1,\rm r}(X_0e^v,\eta)\,dv>0$',18)
txt(60,1150,r'The activated profile is smooth and parameter analytic, but is not radially analytic at $X_0$.',12)
txt(40,1200,'Radial cards show order, not scale. Support positions follow the exact affine map x=a_0+s(b_0-a_0).',11)
txt(40,1220,'Source: OpenAI, Appendix B, pp.150–157. Complete proofs: N2.4 Q0–Q10. Editable figure: CC0.',11)
fig.savefig(HERE/'exact-inner-outer-joining.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Title':'Exact inner-outer joining and moment correction'})
fig.savefig(HERE/'exact-inner-outer-joining.png',dpi=100);plt.close(fig)
p=HERE/'exact-inner-outer-joining.svg';t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="892.8pt"' in t
p.write_text(t.replace('width="1008pt" height="892.8pt"','width="1400" height="1240"'),encoding='utf8')

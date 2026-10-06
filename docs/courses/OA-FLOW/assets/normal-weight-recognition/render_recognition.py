"""Exact support/finite-domain diagram. Original expression, CC0-1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
matplotlib.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'nwr-20261005','mathtext.fontset':'dejavusans'})
OUT=Path(__file__).resolve().parent/'assets'
OUT.mkdir(exist_ok=True)
fig=plt.figure(figsize=(15,10.5),dpi=200,facecolor='#f4f6f8')
fig.text(.055,.957,'Weight support and finite domain are different projections',size=22,weight='bold',color='#183148')
fig.text(.055,.925,'Whole-cone recognition for a normal dual-invariant weight on an arbitrary LCA crossed product',size=13,color='#405267')
colors={'finite':'#cce9e4','zero':'#e0e5eb','infinite':'#ffdcc1','faithful':'#d9e6fb'}
def panel(pos,title):
 ax=fig.add_axes(pos);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.add_patch(FancyBboxPatch((.006,.01),.988,.975,boxstyle='round,pad=0.003,rounding_size=0.02',facecolor='white',edgecolor='#c4cdd7',lw=1.1))
 ax.text(.035,.86 if pos[3]<.20 else .89 if pos[3]<.28 else .92,title,size=15,weight='bold',color='#183148');return ax
def box(ax,xy,w,h,text,fc=colors['faithful'],size=12):
 ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=0.008,rounding_size=0.02',facecolor=fc,edgecolor='#73869a',lw=1))
 ax.text(xy[0]+w/2,xy[1]+h/2,text,ha='center',va='center',size=size,color='#172d42',linespacing=1.5)
def arrow(ax,start,end):ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,color='#526b84',lw=1.4))
a=panel([.05,.565,.43,.315],'1  Three orthogonal parts (NWR1, NWR5)')
for x,w,key,label in [(.04,.39,'finite',r'$r=pq$'+'\nfaithful semifinite corner'),(.44,.23,'zero',r'$z=1-p$'+'\nzero part'),(.68,.28,'infinite',r'$d=1-q$'+'\ninfinite part')]:box(a,(x,.44),w,.32,label,colors[key],11)
a.text(.055,.31,r'$q=r+z$: join of finite-weight projections',size=12)
a.text(.055,.19,r'$p=r+d$: complement of the null-projection join',size=12)
a.text(.055,.075,r'$\Omega(X)=\Omega(qXq)+\infty\,1_{\{dXd\ne0\}}$',size=13)
b=panel([.51,.565,.44,.315],'2  Complete only a complementary corner (NWR3)')
box(b,(.04,.51),.36,.25,r'$\Omega_p$'+'\nfaithful n.s.f. on '+r'$pNp$',colors['finite'],11)
box(b,(.57,.51),.38,.25,r'$\Phi_{1-p}$'+'\nfaithful n.s.f. on '+r'$(1-p)N(1-p)$',colors['faithful'],10.5)
b.text(.48,.63,'+',ha='center',size=24,color='#183148');arrow(b,(.22,.49),(.40,.36));arrow(b,(.76,.49),(.58,.36))
box(b,(.24,.20),.55,.14,r'$\Sigma=\nu_N\circ E_p=D\psi$',colors['faithful'],13)
b.text(.04,.065,'FR applies to this faithful semifinite completion.',size=11.5)
c=panel([.05,.27,.90,.265],'3  The infinite part has its own proof (NWR5, NWR6)')
box(c,(.035,.31),.265,.38,r'$d=\pi(e_d)$'+'\n'+r'$\varphi_\infty(a)=0$'+' if '+r'$e_dae_d=0$'+'\notherwise '+r'$\varphi_\infty(a)=\infty$',colors['infinite'],12)
arrow(c,(.315,.50),(.415,.50))
box(c,(.43,.31),.255,.38,r'$dT(X)d=T(dXd)$'+'\n'+r'$T(dXd)=0\Longleftrightarrow dXd=0$',colors['faithful'],12)
arrow(c,(.70,.50),(.79,.50))
box(c,(.80,.31),.165,.38,r'$D\varphi_\infty$'+'\n'+r'$=\Omega_\infty$',colors['infinite'],13)
c.text(.04,.10,r'Compact-square recovery: $D\varphi(L_{ha}^{*}L_{ha})=\varphi(a^{*}a)$, with $\int|h|^2=1$.',size=13)
d=panel([.05,.055,.90,.185],'4  Exact matrix examples: '+r'$M_2$, $G=\mathbb{Z}/2$, $T(A,B)=(A+B)/2$')
rows=[(r'$\varphi_s(a)=3a_{11}$',r'$p=e_{11}$',r'$q=1$', 'semifinite, nonfaithful'),(r'$\varphi_m(a)=3a_{11}+\infty\,a_{22}$',r'$p=1$',r'$q=e_{11}$','faithful, nonsemifinite'),(r'$\varphi_i(a)=\infty\,a_{22}$',r'$p=e_{22}$',r'$q=e_{11}$','nonfaithful, nonsemifinite')]
for j,(f,p,q,scope) in enumerate(rows):
 y=.64-j*.21
 d.text(.035,y,f,size=12);d.text(.43,y,p,size=12);d.text(.57,y,q,size=12);d.text(.70,y,scope,size=11.5)
fig.text(.055,.018,'All diagrams are algebraic schematics; rectangle widths are not dimensions or traces. Native image: 3000 × 2100.',size=10,color='#4a5b6c')
fig.savefig(OUT/'normal-weight-recognition.png',dpi=200,metadata={'Software':'NWR original renderer'})
fig.savefig(OUT/'normal-weight-recognition.svg',metadata={'Date':None,'Creator':'NWR original renderer'})
plt.close(fig)
p=OUT/'normal-weight-recognition.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
data={'projection_definitions':{'support_p':'p=1-z, where z is the largest null projection','finite_domain_q':'q is the join of finite-weight projections'},'group':'Z/2, counting Haar','dual_point_mass':'1/2','matrix_dimension':2,'native_dimensions':[3000,2100],'weights':[{'name':'phi_s','finite_density':[3,0],'infinite_projection':[0,0],'support_p':[1,0],'finite_domain_q':[1,1]},{'name':'phi_m','finite_density':[3,0],'infinite_projection':[0,1],'support_p':[1,1],'finite_domain_q':[1,0]},{'name':'phi_i','finite_density':[0,0],'infinite_projection':[0,1],'support_p':[0,1],'finite_domain_q':[1,0]}],'normalization':'dual finite value = 3(A11+B11)/2; infinite term is zero iff A22+B22=0','schematic_widths_not_dimensions':True}
(OUT/'normal-weight-recognition-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Rendered PNG, SVG and exact data.')

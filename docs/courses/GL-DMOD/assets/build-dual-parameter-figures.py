"""Reproduce exact division, connection and resonant-frame proof diagrams."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,
                     'svg.hashsalt':'GL-DMOD-DP-exact-maps-v1'})
ink,blue,green,muted='#152640','#155ca5','#17765d','#52627a'

def canvas(title,subtitle):
 f=plt.figure(figsize=(16,10),dpi=150,facecolor='#f7f9fc')
 a=f.add_axes([0,0,1,1]);a.set(xlim=(0,16),ylim=(0,10));a.axis('off')
 a.text(8,9.48,title,ha='center',va='center',fontsize=23,color=ink)
 a.text(8,8.98,subtitle,ha='center',va='center',fontsize=17,color=muted)
 return f,a

def text(a,x,y,v,size=17,color=ink,**kw):
 a.text(x,y,v,ha='center',va='center',fontsize=size,color=color,**kw)

def box(a,x,y,w,h,v,size=17,color=blue):
 a.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.08,rounding_size=0.1',
                           facecolor='white',edgecolor=color,linewidth=1.5))
 text(a,x,y,v,size,color=ink)

def arrow(a,p,q,color=blue):
 a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=15,lw=1.7,color=color))

def matrix(a,x,y,entries,cell=.53,size=23,color=ink):
 rows,cols=len(entries),len(entries[0]);w=cols*cell;hh=rows*cell
 for i,row in enumerate(entries):
  for j,v in enumerate(row):text(a,x+(j-(cols-1)/2)*cell,y+((rows-1)/2-i)*cell,'$'+v+'$',size,color)
 left,right=x-w/2-.1,x+w/2+.1
 a.plot([left+.12,left,left,left+.12],[y+hh/2,y+hh/2,y-hh/2,y-hh/2],color=color,lw=1.5)
 a.plot([right-.12,right,right,right-.12],[y+hh/2,y+hh/2,y-hh/2,y-hh/2],color=color,lw=1.5)

f,a=canvas('Whole-module realization by actual Gevrey coefficients',
          r'$v=(t,z),\quad h=D_t^{-1},\quad R_0=\{\sum a_n(x)h^n:\ |a_n|_K\leq MC^n n!\}$')
a.plot([8,8],[1.05,8.5],color='#d7dfea',lw=1.2)
text(a,4,8.24,'Mixed normal division retains the time correction',19,blue)
box(a,4,7.43,6.9,.88,r'$h^2\circ(t^2z)=h^2t^2z-4h^3tz+6h^4z$',21)
text(a,4,6.76,'Right side: ordinary normal symbols.  [DP.9]',15,muted)
box(a,4,5.91,6.9,.87,r'$\|D\mathcal{E}\|\leq\frac{1}{4},\quad (1+D\mathcal{E})^{-1}=\sum_{k\geq0}(-D\mathcal{E})^k$',18)
text(a,4,5.12,r'$\|(Q,S)\|_*\leq\frac{4}{3}\|F\|_c$'+'   [DP.12–DP.14]',18,green)
box(a,4,4.35,6.9,.87,r'$S=\sum_{(a,\beta,j)\in\mathcal{B}}s_{a,\beta,j}(x,h)t^az^\beta e_j$',18)
text(a,4,3.62,'Finite inverse ordering uses every time derivative.  [DP.16]',15,muted)
arrow(a,(4,3.38),(4,2.90))
box(a,4,2.35,6.9,.83,r'$M_0=\sum_{(a,\beta,j)\in\mathcal{B}}R_0(t^az^\beta)m_j$',19,green)
text(a,4,1.65,'The entire module is finite over the commutative ring.  [DP.17]',15,green)

text(a,12,8.24,'Smooth support gives the finite parameter input',19,blue)
text(a,12,7.64,r'$\Lambda=\{t=z=0\},\qquad (t,z)^k(M_0/hM_0)=0$',19)
text(a,12,7.13,r'$L=M_0/hM_0\quad\mathrm{finite\ over}\ \mathcal{O}_x$',19)
arrow(a,(12,6.82),(12,6.35))
box(a,12,5.75,6.9,.91,r'$L\ \mathrm{free\ on}\ \{g\ne0\}\quad\Longrightarrow\quad M_0\simeq R_0^r$',19,green)
text(a,12,5.08,'Actual finite matrix inversion and h-injectivity.  [DP.20–DP.21]',15,muted)
box(a,12,4.12,6.9,1.05,r'$t=h^2\partial_h+T,\qquad z_i=h\partial_{x_i}+Z_i$'+'\n'
    r'$\nabla_h=\partial_h+h^{-2}T,\quad\nabla_i=\partial_{x_i}+h^{-1}Z_i$',19)
text(a,12,3.24,r'$h^2\partial_hZ_i-h\partial_iT+[T,Z_i]=hZ_i$',19)
text(a,12,2.80,r'$h(\partial_iZ_j-\partial_jZ_i)+[Z_i,Z_j]=0$',19)
text(a,12,2.18,r'$T_0^a Z_{1,0}^{\beta_1}\cdots Z_{d,0}^{\beta_d}=0\quad(a+|\beta|\geq k)$',18,green)
text(a,12,1.65,'Flat connection; joint nilpotence of the leading matrices.  [DP.23–DP.26]',14,green)
a.plot([.65,15.35],[1.06,1.06],color='#d7dfea',lw=1.2)
text(a,8,.60,'These are factorial-growth symbol coefficients.  No numerical convergence in h is assumed.',16,muted)
f.savefig(out/'actual-dual-parameter-realization.png',dpi=150)
f.savefig(out/'actual-dual-parameter-realization.svg',metadata={'Date':None});plt.close(f)

f,a=canvas('An Euler-stable lattice gives a finite-order Euler normal form',
          r'$M_0\subset M,\quad EM_0=M,\quad\theta M_0\subset M_0,\quad D_{x_i}M_0\subset M_0$')
text(a,4,8.29,'No exceptional parameter point in the stable-lattice case',18,blue)
box(a,4,7.50,6.8,.86,r'$L=M_0/hM_0\quad\mathrm{has\ an}\ \mathcal{O}_x\mathrm{\ connection}$',18)
text(a,4,6.82,'Every ideal of presentation minors is stable under all derivatives.',15,muted)
text(a,4,6.39,'A nonzero analytic differential ideal contains a unit.  [DP.35]',15,green)
arrow(a,(4,6.08),(4,5.66))
box(a,4,5.13,6.8,.79,r'$L\simeq\mathcal{O}_x^r,\qquad M_0\simeq R_0^r$',21,green)
box(a,4,3.98,6.8,.86,r'$\nabla_h=\partial_h+A(h,x)/h,\quad\nabla_i=\partial_i+B_i(h,x)$',18)
text(a,4,3.20,'Tangential iterated integrals converge in a Gevrey Banach algebra.',15,muted)
text(a,4,2.79,r'$\|a\|_\epsilon=\sum_{n\geq0}\|a_n\|\epsilon^n/n!$',20)
text(a,4,2.19,r'$U\in\mathrm{GL}_r(R_0),\qquad A(h,x)\longmapsto A(h)$',19,green)

text(a,12,8.29,'Integer shifts retain every resonance and nilpotent block',18,blue)
box(a,12,7.50,6.8,.86,r'$S=\mathrm{diag}(hI_W,I_V),\quad A\mapsto S^{-1}AS+hS^{-1}\partial_h S$',17)
# The full h derivative is displayed explicitly in the coordinate gauge.
text(a,12,6.80,r'$\mathrm{Re}\,\lambda\in(b-1,b]\quad\Longrightarrow\quad\lambda_i-\lambda_j\notin\mathbb{Z}\setminus\{0\}$',18,green)
box(a,12,5.77,6.8,1.05,r'$h\partial_hV=VH-A(h)V$'+'\n'
    r'$\mathcal{C}_n(X)=nX+HX-XH,\quad\|\mathcal{C}_n^{-1}\|\leq K/n$',18)
text(a,12,4.91,r'$\|V_n\|\leq L^n n!,\quad L=C(1+2KM)$',21,green)
text(a,12,4.43,r'$V,V^{-1}\in M_r(R_0)$'+'   [DP.39–DP.42]',18,muted)
arrow(a,(12,4.08),(12,3.65))
box(a,12,3.10,6.8,.88,r'$M\simeq N_{(H-I)^{\mathsf{T}}}\quad\mathrm{over\ the\ actual}\ E$',22,green)
text(a,12,2.28,'The transpose and minus I follow from coefficient columns and θ = tDₜ.',14,muted)

a.plot([.65,15.35],[1.76,1.76],color='#d7dfea',lw=1.2)
text(a,1.65,.99,r'$A(h)=$',22)
matrix(a,3.08,.99,[['0','h^2'],['0','2']],cell=.48,size=22)
text(a,5.35,.99,r'$S=\mathrm{diag}(h,1)\ \mathrm{twice}$',17,blue)
arrow(a,(6.96,.99),(7.64,.99))
text(a,8.18,.99,r'$H=$',22)
matrix(a,9.34,.99,[['2','1'],['0','2']],cell=.48,size=22)
arrow(a,(10.30,.99),(11.00,.99))
text(a,11.98,.99,r'$A_{\mathrm{Euler}}=$',20)
matrix(a,13.57,.99,[['1','0'],['1','1']],cell=.48,size=22,color=green)
text(a,8,.29,'Exact two-step resonant example; no classification for arbitrary non-stable lattices is asserted.',14,muted)
f.savefig(out/'euler-stable-lattice-normal-form.png',dpi=150)
f.savefig(out/'euler-stable-lattice-normal-form.svg',metadata={'Date':None});plt.close(f)

data={
 'kind':'exact proof diagrams, no numerical samples',
 'dual_parameter_realization':{'coefficient_ring':'R_0: common-domain holomorphic x coefficients with |a_n|<=M C^n n!',
  'time_head_example':{'Q':'h^2','head':'t^2 z','normal_composition':'h^2 t^2 z - 4 h^3 t z + 6 h^4 z','proof':'DP.9'},
  'division_error_norm':'at most 1/4','inverse_norm':'at most 4/3','remainder_support':'finite downward-closed normal monomial set B',
  'whole_module_generators':'(t^a z^beta)m_j over R_0','free_locus':'g != 0, for the general smooth-support input',
  'actions':{'t':'h^2 partial_h + T','z_i':'h partial_i + Z_i'},
  'curvature':['h^2 partial_h Z_i - h partial_i T + [T,Z_i] = h Z_i','h(partial_i Z_j-partial_j Z_i)+[Z_i,Z_j]=0'],
  'principal_nilpotence':'T_0^a product Z_i,0^beta_i=0 for a+|beta|>=k','proof':'DP.1--DP.6'},
 'stable_lattice':{'hypotheses':['M_0 coherent finite E_0 lattice inside M','E M_0=M','theta and all D_xi preserve M_0'],
  'residue_freeness':'at every parameter point; differential ideals of minors are zero or unit',
  'tangential_gauge':'invertible actual R_0 matrix; iterated integral bound M^k |x_i|^k/k!',
  'residue_shift':'A -> S^-1 A S + h S^-1 partial_h S; S=diag(h I_W,I_V)',
  'spectral_strip':'b-1 < Re lambda <= b','recursion':'(n I+ad H)V_n = -sum_(k=1)^n A_k V_(n-k)',
  'inverse_bound':'K/n','factorial_bound':'L^n n!, L=C(1+2 K M)',
  'Euler_matrix':'(H-I)^T','isomorphism':'actual finite-order E-module isomorphism','proof':'DP.7.1--DP.7.5',
  'resonant_example':{'initial':[['0','h^2'],['0','2']],'S':[['h','0'],['0','1']],'steps':2,
                      'H':[[2,1],[0,2]],'Euler_matrix':[[1,0],[1,1]]}},
 'not_claimed':['ordinary numerical convergence of the h series','arbitrary holonomic full-infinite regularization','full real contact transport']}
(out/'dual-parameter-and-stable-lattice-exact-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':sorted(p.name for p in out.iterdir() if p.is_file())}))

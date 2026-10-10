"""Reproducible exact algebra/coordinate illustrations of D/U/T, not numerical proofs."""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='gl-dmod-generalized-dictionary'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
OUT=Path(args.output) if args.output else Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
data={'torsor':{'chart':'q != 0, t_i=q^2*t_j','beta':'2*dq/q','horizontal_transition':'P_i=P_j-(2/q)*E',
 'parameter_transition':'P_i=P_j-(2/q)*(lambda+epsilon)','Euler':'E=t*d/dt',
 'right_action_on_functions':'r_a f(t)=f(t/a)','right_derivative':'dr=-E on coefficient functions',
 'defect':'M=E+dr=Lambda on invariant coefficients','lift_E':'E(f tensor v)=E(f) tensor v+f tensor Lambda*v',
 'inverse':'sum_k v_k -> sum_k t^(-k) tensor t^k*v_k, weak weight k',
 'status':'Exact one-chart transition model; not a global presentation of an arbitrary G/N+',
 'proof':['ND.6','ND.7','ND.8','ND.9','ND.10','ND.11']},
 'duality':{'rank':2,'N':2,'ring':'C[x,y]/(x,y)^2','basis':['1','x','y'],
 'x_matrix':[[0,0,0],[1,0,0],[0,0,0]],'y_matrix':[[0,0,0],[0,0,0],[1,0,0]],
 'dual_basis':['1*','x*','y*'],'dual_x_matrix':[[0,-1,0],[0,0,0],[0,0,0]],
 'dual_y_matrix':[[0,0,-1],[0,0,0],[0,0,0]],'socle_R_dimension':2,'socle_dual_dimension':1,
 'Hom_R_k_R_dimension':2,'true_dual_dimension':3,'true_simple_dual_dimension':1,
 'shift':'n+r','opposite_parameter':'-Lambda-2*rho','density_line':'L(-2*lambda-2*rho)',
 'final_parameter':'2*lambda-Lambda','deviation':'-epsilon transpose',
 'status':'Local parameter/torus-connection dualizing diagnostic; no global strong-B free-R object asserted',
 'proof':['NU.1','NU.2','NU.3','NU.4','NU.6','NU.7','NU.8','NU.9']},
 'projector':{'d':3,'N':2,'residue_order':[1,1,0],'epsilon_block':[[0,1],[0,0]],
 'diagonal_z_blocks':['I+3*epsilon','I+4*epsilon','2*epsilon'],
 'off_diagonal_z_blocks':'I at (1,2) and (2,3), all other off-diagonal blocks zero',
 'bound':'Q(z)=z^6*(z-1)^6=0','selected_residue':0,'selected_dimension':2,
 'selected_z':'2*epsilon != 0','endpoint_quotient':'q = projection to the last 2 coordinates',
 'endpoint_inverse':'i = e_0 times the canonical last-block insertion',
 'whole_parameter_deviation':'epsilon_W=diag(epsilon,epsilon,epsilon)',
 'identities':['q*i=I_2','i*q=e_0','z*i=i*(2*epsilon)','epsilon_W*i=i*epsilon'],
 'status':'Exact finite module/flag calibration of NT.4; not a tensor flag of a specified group',
 'proof':['NT.4','NT.7','NT.9','NT.11','NT.12']},
 'free_human_comparison':'https://arxiv.org/html/1209.0188v2 Remark1.2(4)',
 'licence':'CC0-1.0'}
(OUT/'generalized-dictionary-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def box(ax,xy,w,h,label,fc='#f0f5f8',fs=13):
 x,y=xy;ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.015',facecolor=fc,edgecolor='#42647d',lw=1.5))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=fs,linespacing=1.5)
def arrow(ax,a,b,label='',offset=.025):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#366580'})
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+offset,label,ha='center',fontsize=12)
def save(fig,stem):
 fig.savefig(OUT/(stem+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(stem+'.svg'),bbox_inches='tight',metadata={'Date':None});plt.close(fig)

fig,ax=plt.subplots(figsize=(14,8));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
ax.text(.5,.96,'Actual Cartan torsor operators and both inverse descent maps',ha='center',fontsize=20,weight='bold')
box(ax,(.035,.66),.36,.17,'Invariant coefficients F\nparameter Λ = λ + ε',fs=15)
box(ax,(.60,.66),.36,.17,'Lift O_T ⊗ F\nE(f ⊗ v) = E(f) ⊗ v + f ⊗ Λv',fs=14)
arrow(ax,(.41,.765),(.585,.765),'lift',.027)
arrow(ax,(.585,.690),(.41,.690),'T invariants',-.047)
box(ax,(.05,.36),.40,.18,'Chart transition: t_i = q² t_j\nP_i = P_j − (2/q) E\nq ≠ 0, P = ∂/∂q',fc='#e8f2ed')
box(ax,(.55,.36),.40,.18,'Weak rational right action: r_a f(t)=f(t/a)\ndr(h) = −E_h on functions\nM_h = E_h + dr(h) = Λ(h)',fc='#fff1dd',fs=12.5)
ax.text(.5,.26,'A nilpotent monodromy defect coexists with a semisimple rational torus linearization.',ha='center',fontsize=14)
box(ax,(.08,.075),.84,.12,'Inverse evaluation on a finite weak-weight sum:\nΣ v_κ  ↦  Σ t^(−κ) ⊗ t^κ v_κ;  f ⊗ v  ↦  fv',fs=14)
fig.text(.5,.015,'Exact one-chart model; proof ND.6–ND.11. The global proof constructs the actual G/N₊ for every stated central quotient.',ha='center',fontsize=11)
save(fig,'generalized-dictionary-torsor')

fig,axs=plt.subplots(1,3,figsize=(19,7));fig.suptitle('The genuine dual retains nilpotents without a Gorenstein assumption',fontsize=20,weight='bold')
for ax in axs:ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
ax=axs[0];ax.set_title('R = C[x,y]/(x,y)²; basis 1,x,y',fontsize=15,pad=12)
box(ax,(.34,.70),.30,.12,'1',fs=17)
box(ax,(.05,.36),.30,.12,'x',fs=17);box(ax,(.65,.36),.30,.12,'y',fs=17)
arrow(ax,(.43,.67),(.25,.50),'x',.015);arrow(ax,(.56,.67),(.76,.50),'y',.015)
ax.text(.5,.19,'socle(R) = Cx ⊕ Cy\nHom_R(C,R) has dimension 2',ha='center',fontsize=14)
ax.text(.5,.055,'It cannot be the dual of a simple object.',ha='center',fontsize=12,color='#9b4f3c')
ax=axs[1];ax.set_title('Genuine reflected dual R*',fontsize=15,pad=12)
box(ax,(.05,.70),.30,.12,'x*',fs=17);box(ax,(.65,.70),.30,.12,'y*',fs=17)
box(ax,(.34,.36),.30,.12,'1*',fs=17)
arrow(ax,(.25,.67),(.44,.50),'−xᵗ',.015);arrow(ax,(.76,.67),(.55,.50),'−yᵗ',.015)
ax.text(.5,.19,'x·x* = −1*;  y·y* = −1*\nsocle(R*) = C1*',ha='center',fontsize=14)
ax.text(.5,.055,'Dimension 3; nilpotent actions remain nonzero.',ha='center',fontsize=12)
ax=axs[2];ax.set_title('Full ambient dualizing calculation',fontsize=15,pad=12)
box(ax,(.03,.70),.94,.13,'Holonomic D_Y dual: shift [n+r]',fs=14)
arrow(ax,(.5,.67),(.5,.55))
box(ax,(.03,.40),.94,.14,'Bare opposite parameter −Λ−2ρ\nactual density line L(−2λ−2ρ)',fs=13.5)
arrow(ax,(.5,.37),(.5,.25))
box(ax,(.03,.08),.94,.14,'Final parameter 2λ−Λ\nε dual = −ε transpose; bidual returns ε',fs=13.5)
fig.text(.5,.02,'Local parameter/torus-connection diagnostic, not a global strong-B free-R object. Proof NU.1–NU.9; det(h) cancels the parameter-Koszul det(h*).',ha='center',fontsize=10.5)
fig.subplots_adjust(top=.78,bottom=.11,wspace=.27);save(fig,'generalized-dictionary-duality')

fig,ax=plt.subplots(figsize=(15,8));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
ax.text(.5,.96,'A selected endpoint retains its full nilpotent central action',ha='center',fontsize=20,weight='bold')
ax.text(.5,.88,'Exact finite flag calibration: d=3, N=2, ε²=0 in each two-dimensional quotient',ha='center',fontsize=13)
box(ax,(.05,.65),.25,.15,'first layer: z = 1 + 3ε',fc='#eaf0f7',fs=13)
box(ax,(.375,.65),.25,.15,'second layer: z = 1 + 4ε',fc='#eaf0f7',fs=13)
box(ax,(.70,.65),.25,.15,'endpoint: z = 2ε ≠ 0',fc='#e1f2e4',fs=13)
arrow(ax,(.32,.72),(.355,.72));arrow(ax,(.645,.72),(.68,.72))
ax.text(.5,.55,'Upper off-diagonal identity blocks give the actual nontrivial flag; Q(z)=z⁶(z−1)⁶=0.',ha='center',fontsize=13)
box(ax,(.055,.29),.36,.17,'whole six-dimensional module\nprojector e₀ = p₀(z)',fs=14)
box(ax,(.595,.29),.36,.17,'selected two-dimensional endpoint\nz = 2ε; ε remains nonzero',fc='#e1f2e4',fs=14)
arrow(ax,(.43,.405),(.58,.405),'q: endpoint quotient',.023)
arrow(ax,(.58,.33),(.43,.33),'i: e₀ × insertion',-.052)
ax.text(.5,.15,'q i = I₂;  i q = e₀;  z i = i(2ε);  ε_W i = iε',ha='center',fontsize=16)
fig.text(.5,.035,'Exact finite linear module/flag model of NT.4, not a tensor flag of a specified group. The all-rank bundle/endpoint proof is NT.5–NT.12.\nThe selected graph need not inherit the original function action; its true shifted operator structure is transported through the endpoint isomorphism.',ha='center',fontsize=11)
save(fig,'generalized-dictionary-projector')
print('Rendered three exact dictionary figures, their SVGs and joint data.')

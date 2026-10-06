"""Reproduce the exact map diagram and check finite Clifford models."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
base=Path(__file__).resolve().parent
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex);I=np.eye(2)
def kron(items):
    r=np.array([[1]],complex)
    for a in items:r=np.kron(r,a)
    return r
checks=[]
for N in (2,4,6):
    m=N//2;gs=[]
    for j in range(m):
        for a in (X,Y):gs.append(kron([Z]*j+[a]+[I]*(m-j-1)))
    d=2**m;eye=np.eye(d);big=np.eye(d*d);G=(-1j)**m*np.linalg.multi_dot(gs);epsN=(-1)**(N*(N-1)//2)
    for p in range(N+1):
        q=N-p;P=big.copy();vol=big.copy()
        for j in range(p):
            alpha=np.kron(G,gs[j]);f=-np.kron(gs[j],eye)
            vol=vol@(-1j*alpha@f)
        for a in range(p,N):
            K=-1j*np.kron(gs[a]@G,gs[a]);P=P@(big+K)/2
        err=np.linalg.norm((vol-epsN*np.kron(G,G))@P)
        assert np.linalg.norm(P@P-P)<1e-10 and abs(np.trace(P).real-2**p)<1e-9 and err<1e-10
        for j in range(p):
            assert np.linalg.norm(P@np.kron(G,gs[j])-np.kron(G,gs[j])@P)<1e-10
            assert np.linalg.norm(P@np.kron(gs[j],eye)-np.kron(gs[j],eye)@P)<1e-10
        checks.append(dict(N=N,p=p,q=q,kernel_rank=round(np.trace(P).real),volume_error=float(err)))
fig,ax=plt.subplots(figsize=(7.7,9.0))
fig.patch.set_facecolor('#f9fafb');ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.035,.985,'The embedding index and its normal Gaussian',ha='left',va='top',fontsize=16,weight='bold',color='#14243a')
def panel(y,height,title,lines):
    ax.add_patch(FancyBboxPatch((.02,y),.96,height,boxstyle='round,pad=0.008,rounding_size=0.013',facecolor='white',edgecolor='#58769a',linewidth=1.3))
    ax.text(.045,y+height-.018,title,va='top',fontsize=13,weight='bold',color='#153a65')
    for k,line in enumerate(lines):ax.text(.045,y+height-.066-.038*k,line,va='top',fontsize=11.8,color='#14243a')
panel(.727,.205,'1. Complement Thom equivalence',[
    r'$F\oplus\nu_i\cong V\times\mathbb{R}^N,\quad N$ even, $\quad\nu_i=(diF)^\perp$',
    r'$z_i:C_F\longrightarrow C_0(\nu_i),\quad v\mapsto-\gamma(e_iv)$',
    r'Grading $\epsilon_p\Gamma_N$; operator $\gamma(\eta)/\sqrt{1+|\eta|^2}$',
    r'$\Theta_i=y_Fz_i:B_F=C_0(F^*)\longrightarrow C_0(\nu_i)$'])
panel(.496,.205,'2. Transverse tube and ambient Bott inverse',[
    r'$\phi_i(x,\eta)=(x,i(x)+\eta),\quad N_i\subset\nu_i$ a small disk',
    r'$\operatorname{Hol}(\Omega_i)=\Omega_i\times_{N_i}\Omega_i\subset G\times\mathbb{R}^N$',
    r'$\kappa_i:C_0(\nu_i)\longrightarrow A\otimes C_0(\mathbb{R}^N)$',
    r'$\mathcal{T}_i=\Theta_i\kappa_i(1_A\boxtimes\eta_N)$'])
panel(.228,.242,'3. One leaf: the full Clifford source remains',[
    r'$K_a=-i\gamma_{\tau,a}\Gamma_\tau\otimes\gamma_{D,a},\quad K_aw=w$',
    r'Vacuum $\pi^{-q/4}e^{-|\eta|^2/2}$; rank $2^p$; $O^2\geq2$ off its kernel',
    r'$\alpha_j=\Gamma_\tau\otimes\gamma_{D,j},\quad f_j=-\gamma_{\tau,j}\otimes1$',
    r'$\Gamma_{0,F}=(-i\alpha_1f_1)\cdots(-i\alpha_pf_p)$',
    r'On $\ker O$: $\Gamma_{0,F}=\epsilon_N\Gamma_\tau\Gamma_D$; grading $\epsilon_p\Gamma_{0,F}$'])
panel(.041,.173,'4. Exact comparison',[
    r'Zero foliation: both index maps are identity on $K^0(V)$',
    r'One leaf: $\mathcal{T}_i=d_{V,-}$, with $J_-(v,\eta)=(g^{-1}\eta,-gv)$',
    'Lemmas 2.1–2.4; Theorems 3.1 and 4.1; equations (4.3)–(4.6)'])
ax.text(.025,.006,r'$\epsilon_r=(-1)^{r(r-1)/2}$; $p=\operatorname{rank}F$, $q=N-p$. Maps denote KK classes.',fontsize=9.8,color='#41536c')
fig.subplots_adjust(left=.02,right=.98,top=.99,bottom=.01)
for ext in ('png','svg'):fig.savefig(base/('KT-KK-23-embedding-index-gaussian.'+ext),dpi=210)
(base/'clifford-checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(clifford_cases=len(checks),figure='KT-KK-23-embedding-index-gaussian.png')))

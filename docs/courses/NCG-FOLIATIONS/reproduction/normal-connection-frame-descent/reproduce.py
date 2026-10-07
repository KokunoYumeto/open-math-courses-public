"""CC0 diagram and exact finite checks for LF/GJ/FD normal connections."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,math,os

def finite_checks():
    rows=[]
    def check(name,passed,detail):
        assert passed,name
        rows.append(dict(name=name,passed=True,detail=detail))
    # Nontrivial transition, actual affine weighted origin and identity arrow.
    tests=[]
    for t in [Q(-5),Q(3),Q(7,2)]:
        for weight in [Q(0),Q(1,3),Q(2,3),Q(1)]:
            omega_j=-weight*t;omega_i=(1-weight)*t
            tests.append(t+omega_j-omega_i==0)
    check('identity_displacement_after_affine_origin',all(tests),
          '12 rational chart-transition tests; t=3, weight=2/3 gives omega_j=-2, omega_i=1, B_1=0.')
    tests=[]
    for rho in [Q(k,8) for k in range(1,9)]:
        tau=1+100/rho**4
        for b in [Q(1,4),Q(1,2),Q(1)]:
            for lam in [Q(1),Q(2),Q(16),Q(256)]:
                tests.append(lam/(tau+b*lam)**2<=1/(4*tau*b))
    check('scalar_resolvent_derivative_inequality',all(tests),
          '96 rational spectral samples; difference reduces to (tau-b*lambda)^2>=0.')
    vals=[]
    for rho in [Q(k,8) for k in range(9)]:
        bound=(4*rho**3+(2*rho+rho**4)/4+rho**4)/100
        vals.append(0<=bound<=Q(23,400))
    check('conditional_relative_bound',all(vals),
          '9 rational samples with L=J=H=1 and K0=100; endpoint 23/400, zero endpoint 0.')
    # Two frame points, three auxiliary points; exact pinned Haar marginal.
    mu=[Q(1,6)]*6
    check('pinned_frame_marginal',sum(mu[:3])==sum(mu[3:])==Q(1,2),
          'Finite toy frame fibre with two equally weighted points; three auxiliary choices per frame.')
    values=[Q(k) for k in range(6)]
    avg=sum(m*v*v for m,v in zip(mu,values))
    check('probability_minimum_and_gram',min(v*v for v in values)<=avg and
          avg-sum(m*v for m,v in zip(mu,values))**2>=0,
          'Exact minimum<=mean and positive two-vector Gram determinant; not an infinite-field compactness test.')
    # Direct Gaussian-integer sum of four characters of the cyclic group C4.
    # This finite illustration does not establish the infinite circle theorem.
    roots=[(1,0),(0,1),(-1,0),(0,-1)]
    fourier=[]
    for m in range(4):
        row=[]
        for n in range(4):
            terms=[roots[(n-m)*k%4] for k in range(4)]
            row.append((Q(sum(v[0] for v in terms),4),Q(sum(v[1] for v in terms),4)))
        fourier.append(row)
    check('fixed_auxiliary_finite_fourier_modes',fourier==[
          [(Q(int(n==m)),Q(0)) for n in range(4)] for m in range(4)] and Q(1,2)**2==Q(1,4),
          'Four C4 characters summed directly in Gaussian integers have Haar Gram identity; inverse eigenvalue 1/2 preserves squared norm 1/4. Infinite S1 noncompactness is proved in FD.7.')
    return dict(schema='normal-connection-frame-descent-finite-checks/v1',count=len(rows),all_passed=True,checks=rows)

def draw(output,resources,description):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.patches import FancyBboxPatch
    regular=FontProperties(fname=str(resources/'fonts/DejaVuSans.ttf'))
    bold=FontProperties(fname=str(resources/'fonts/DejaVuSans-Bold.ttf'))
    blue,green,red,ink,gray='#17628f','#16745a','#b34638','#19384d','#627789'
    plt.rcParams.update({'svg.hashsalt':'normal-connection-frame-descent-lf-gj-fd-v1',
                        'svg.fonttype':'path','axes.edgecolor':ink,'axes.labelcolor':ink,
                        'xtick.color':ink,'ytick.color':ink})
    def text(ax,x,y,s,size=12,strong=False,**kw):
        return ax.text(x,y,s,fontproperties=bold if strong else regular,
                       fontsize=size,color=kw.pop('color',ink),**kw)
    def panel(rect,title):
        ax=fig.add_axes(rect);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
        text(ax,0,1,title,15,True,va='top');return ax
    def box(ax,x,y,w,h,s,color=blue):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',
                     facecolor='#edf4f8',edgecolor=color,linewidth=1.4))
        text(ax,x+w/2,y+h/2,s,12,ha='center',va='center')
    def arrow(ax,start,end,color=blue):
        ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=color,lw=1.8))
    fig=plt.figure(figsize=(17,12),facecolor='white')
    head=panel([.035,.94,.93,.05],'Normal connections survive gluing; compact inverse can fail under averaging')
    text(head,0,.23,'Actual affine labels, flat collapse, geometric graph weight and original-unit frame descent.  LF.1–FD.7',12)
    ax=panel([.04,.62,.43,.27],'A  Correct affine origins cancel the identity label')
    box(ax,.01,.59,.35,.24,'Chart j\nωj = −2');box(ax,.62,.59,.35,.24,'Chart i\nωi = 1')
    arrow(ax,(.39,.72),(.59,.72));text(ax,.49,.80,'tij = 3',11,ha='center')
    text(ax,.02,.43,'Local i-origin in j: −3; weights φi=2/3, φj=1/3',12)
    text(ax,.02,.29,'ωj=(2/3)(−3)+(1/3)0=−2;  ωi=tij+ωj=1',12,color=green)
    text(ax,.02,.14,'Identity in different charts:  B1 = 3+(−2)−1 = 0',12,True)
    text(ax,.02,.01,'Transitions are constant-normal. The flat connection agrees.  LF.4–LF.6',10)
    ax=panel([.53,.62,.43,.27],'B  A disappearing factor requires flat connection cores')
    box(ax,.02,.62,.36,.21,'ρa > 0: active Qa\n(wa, wa za)');box(ax,.63,.62,.33,.21,'ρa = 0\none vertex')
    arrow(ax,(.41,.73),(.59,.73));text(ax,.49,.84,'wa → 0',11,ha='center')
    text(ax,.02,.46,'βa = exp(−1/ρa²),  ba = βa /(Σ βc²)½,  wa = ba²',12)
    text(ax,.02,.30,'Core observable: d(x) f(za), with every jet of d zero at ρa=0',11)
    text(ax,.02,.15,'Differentiate on the potential product; every derivative descends.',11,color=green)
    text(ax,.02,.01,'No derivative of a nonexistent coordinate is assigned.  GJ.1–GJ.3',10)
    ax=fig.add_axes([.075,.285,.37,.255])
    rho=[k/200 for k in range(201)]
    inv=[r**4/100 for r in rho]
    deriv=[(4*r**3+(2*r+r**4)/4+r**4)/100 for r in rho]
    ax.plot(rho,inv,color=blue,lw=2,label='ρ⁴/100: inverse norm upper bound')
    ax.plot(rho,deriv,color=green,lw=2,label='relative derivative upper bound')
    ax.axhline(23/400,color=gray,ls='--',lw=1)
    ax.set_xlim(0,1);ax.set_ylim(0,.062);ax.grid(alpha=.18)
    ax.set_title('C  Conditional sample: L=J=H=1, K0=100',fontproperties=bold,fontsize=14,color=ink,pad=14)
    ax.set_xlabel('ρa (numerical samples)',fontproperties=regular,fontsize=11)
    ax.set_ylabel('operator norm upper bound',fontproperties=regular,fontsize=11)
    ax.legend(prop=FontProperties(fname=str(resources/'fonts/DejaVuSans.ttf'),size=9),loc='upper left')
    for label in ax.get_xticklabels()+ax.get_yticklabels():label.set_fontproperties(regular)
    text(ax,0,-.25,'Ta=(1+K0 ρa⁻⁴)I+ba Θa; defect = ba Sg.  GJ.7–GJ.11',11,transform=ax.transAxes)
    text(ax,0,-.37,'Both displayed bounds vanish at collapse; endpoint 23/400 is exact.',10,transform=ax.transAxes)
    ax=panel([.53,.285,.43,.27],'D  Pinned Haar probabilities return to original units')
    box(ax,.01,.65,.95,.19,'XH → P → T;  compact frame Px, Haar probability mx')
    text(ax,.02,.50,'XG,x = {μ ∈ Prob(XH|Px) : frame_anchor* μ = mx}',12)
    text(ax,.02,.35,'Eμ = L²(μ; EH);  Ψ(g,μ) = ∫ ‖C(g,u)(z)‖² dμ(u,z)',12,color=blue)
    text(ax,.02,.20,'δv ∫ f dμ = ∫ δv̂ f dμ;  v̂ is the horizontal normal lift.',12,color=green)
    text(ax,.02,.06,'Lift potential-product measures to prove actual relation and null independence.',10)
    text(ax,.02,-.02,'Dense closable metric connection; no generic KK representative is used.  FD.1–FD.6',10)
    ax=panel([.04,.035,.92,.14],'E  Pointwise averaging of a compact-inverse weight can lose compact inverse')
    text(ax,.01,.58,'L²(S¹) ⊗ H0;  Θ0 e1=2e1;  vn=exp(inu)⊗e1, n∈Z, orthonormal.',12)
    text(ax,.01,.25,'(1 ⊗ Θ0)⁻¹ vn = (1/2)vn.  The images stay orthogonal at norm 1/2.',12,color=red,strong=True)
    text(ax,.01,-.03,'Thus the inverse is noncompact. A confining averaged weight and closed physical sum remain required.  FD.7',11)
    output.mkdir(parents=True,exist_ok=True)
    fig.savefig(output/'normal-connection-frame-descent.png',dpi=150,
                metadata=dict(Title='Normal connection and compact-frame descent',Description=description,Software='normal-connection-frame-descent v1'))
    fig.savefig(output/'normal-connection-frame-descent.svg',
                metadata=dict(Title='Normal connection and compact-frame descent',Description=description,Date=None))
    plt.close(fig)
    return dict(schema='normal-connection-frame-descent-data/v1',
      affine_origin=dict(transition='3',weights=['2/3','1/3'],omega_j='-2',omega_i='1',identity_displacement='0'),
      collapse=dict(beta='exp(-1/rho^2)',b='beta/sqrt(sum beta_c^2)',w='b^2',core='d(x)f(z_a), all derivatives of d zero where rho_a=0'),
      exact_weight='(1+K0*rho^-4)I+b*Theta',
      conditional_sample=dict(L=1,J=1,H=1,K0=100,endpoint_bound='23/400',samples=[dict(rho=r,inverse_upper=a,relative_derivative_upper=b) for r,a,b in zip(rho,inv,deriv)]),
      frame_base='probabilities on X_H above P_x with prescribed Haar marginal m_x',
      noncompactness=dict(space='L2(S1) tensor H0',Theta0_eigenvalue='2',inverse_norm_every_Fourier_mode='1/2'),
      scope='Panel C is a numerical rendering of conditional bounds, not a chosen metric or a proved physical operator; the other panels are exact algebra or typed schematics.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'out')
    parser.add_argument('--resources',type=Path,default=Path(__file__).resolve().parent.parent/'labelled-geometric-kernel')
    parser.add_argument('--checks-only',action='store_true');args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    os.environ.setdefault('MPLCONFIGDIR',str(args.output_dir/'runtime-cache'))
    checks=finite_checks();(args.output_dir/'finite-checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    if not args.checks_only:
        terms=Path(__file__).with_name('COMPONENT-TERMS.md').read_text(encoding='utf-8')
        data=draw(args.output_dir,args.resources,'LF.4–LF.6, GJ.1–GJ.5, FD.1–FD.7. Exact algebra, typed schematics and explicitly conditional sampled bounds.\n\n'+terms)
        (args.output_dir/'figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(all_passed=checks['all_passed'],checks=checks['count'],figure_rendered=not args.checks_only)))
if __name__=='__main__':main()

"""Reproduce the original CCF field maps and specified Hilbert quadrature benchmark."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sympy as s
import mpmath as mp

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':11,'legend.fontsize':9,'figure.facecolor':'#f7f9fc','axes.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
blue='#176699';orange='#c95b20';green='#16775b';purple='#7447a7'
def save(fig,stem):
    for ext in ['png','svg']:fig.savefig(R/(stem+'.'+ext),dpi=180,bbox_inches='tight')
    plt.close(fig)
def finish(ax):
    ax.grid(alpha=.18);ax.set_xlabel('Original coordinate y');ax.axhline(0,color='#9da9b7',lw=.6)
y=s.symbols('y',real=True);p=s.Rational(8,5);lam=s.Rational(3,5);epsilon=s.Rational(3,20)
O=-2*y/(1+y*y);V=-2*s.atan(y);U=V+epsilon*y
def res(u):return -O-p*y*s.diff(O,y)+u*s.diff(O,y)+O*s.diff(u,y)
Q=V*s.diff(O,y)+O*s.diff(V,y);h0=y*s.diff(O,y);h1=O+p*y*s.diff(O,y)
grid=np.linspace(-3,3,801)
def ev(expr):return s.lambdify(y,expr,'numpy')(grid)

fig,ax=plt.subplots(1,2,figsize=(13,4.6));fig.suptitle('Signed CCF scaling retains the reflection sign',y=1.03,fontweight='bold')
ax[0].plot(grid,ev(O),color=blue,label=r'Original $\Omega(y)$')
ax[0].plot(grid,ev(O.subs(y,y/2)),color=green,lw=2,label=r'Signed maps $\kappa=2$ and $\kappa=-2$ (coincide)')
ax[0].plot(grid,ev(O.subs(y,-y/2)),color=orange,ls='--',label=r'Unsigned $\kappa=-2$: $\Omega(-y/2)$')
ax[0].set_ylabel('Original vorticity profile');ax[0].set_title('Odd benchmark: the signed negative map preserves its sign')
ax[1].plot(grid,ev(-2*Q.subs(y,-y/2)),color=purple,lw=2,label=r'$\widetilde R(y)-R(-y/2)=-2Q(-y/2)$')
ax[1].set_ylabel('Complete residual difference');ax[1].set_title('The unsigned reflection retains this entire mismatch')
for a in ax:finish(a);a.legend(loc='best')
fig.text(.5,-.015,r'$\Omega=-2y/(1+y^2),\ U=-2\arctan y,\ \sigma=-1,\ \lambda=3/5,\ Q=U\Omega^{\prime}+\Omega U^{\prime}$.  CF15–CF18; HQ35.',ha='center',fontsize=11)
fig.tight_layout();save(fig,'ccf-signed-spatial-map')

fig,ax=plt.subplots(1,3,figsize=(15.2,4.8));fig.suptitle('The complete change made by repairing the predicted velocity',y=1.03,fontweight='bold')
ax[0].plot(grid,ev(U),color=blue,label=r'Predicted $U=U_*+3y/20$')
ax[0].plot(grid,ev(V),color=green,ls='--',label=r'Repaired $U_*=-2\arctan y$')
ax[0].set_title('Both original velocity fields');ax[0].set_ylabel('Velocity profile')
ax[1].plot(grid,ev(res(U)),color=blue,label=r'Original $R[\Omega,U]$')
ax[1].plot(grid,ev(res(V)),color=green,ls='--',label=r'Repaired $R[\Omega,U_*]$')
ax[1].set_title(r'$R-R_*=(E\Omega)^{\prime}$');ax[1].set_ylabel('Full profile-equation residual')
ax[2].plot(grid,ev(s.diff(epsilon*y*h0,y)),color=orange,label=r'$(L-L_*)h_0=(Eh_0)^{\prime}$')
ax[2].plot(grid,ev(s.diff(epsilon*y*h1,y)),color=purple,label=r'$(L-L_*)h_1=(Eh_1)^{\prime}$')
ax[2].set_title('The two complete operator changes');ax[2].set_ylabel('Mode-image difference')
for a in ax:finish(a);a.legend(loc='best')
fig.text(.5,-.025,r'$\Omega=-2y/(1+y^2),\ \lambda=3/5,\ \sigma=-1,\ E=3y/20,\ \Delta=3/20$.  CM1–CM3; both displayed residuals can be nonzero.',ha='center',fontsize=11)
fig.tight_layout();save(fig,'ccf-velocity-repair')

mp.mp.dps=80
def mul(a,b):
    c=[mp.mpf(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c
def integral(poly,a,b):return sum(v*(b**(k+1)-a**(k+1))/(k+1) for k,v in enumerate(poly))
def make_quad(n,D):
    Z=mp.asinh(D);nodes=[mp.sinh(-Z+2*Z*k/n) for k in range(n+1)]
    weights=[mp.mpf(0)]*(n+1);totalJ=mp.mpf(0)
    for i in range(n):
        start=min(max(i-1,0),n-3);ids=list(range(start,start+4));a,b=nodes[i:i+2]
        for k in ids:
            poly=[mp.mpf(1)];den=mp.mpf(1)
            for r in ids:
                if r!=k:poly=mul(poly,[-nodes[r],mp.mpf(1)]);den*=nodes[k]-nodes[r]
            weights[k]+=integral(poly,a,b)/den
        W=[mp.mpf(1)]
        for k in ids:W=mul(W,[-nodes[k],mp.mpf(1)])
        cuts=sorted(set([a,b]+[nodes[k] for k in ids if a<nodes[k]<b]))
        for l,r in zip(cuts,cuts[1:]):
            midpoint=(l+r)/2;sign=mp.sign(sum(v*midpoint**k for k,v in enumerate(W)))
            totalJ+=sign*integral(W,l,r)
    assert totalJ>0
    return nodes,weights,totalJ
def f(q):return -2*q/(1+q*q)
def g(q,target):return 2*(1-q*target)/((1+q*q)*(1+target*target))
def Qvalue(nodes,weights,D,target):
    return (sum(w*g(q,target) for q,w in zip(nodes,weights))+f(target)*mp.log((D+target)/(D-target)))/mp.pi
def Hfinite(D,target):return (4*mp.atan(D)-2*target*mp.log((D+target)/(D-target)))/(mp.pi*(1+target*target))
def Tail(D,target):return (4*mp.atan(1/D)+2*target*mp.log((D+target)/(D-target)))/(mp.pi*(1+target*target))
diagnostics=[];D=mp.mpf(4);A=mp.mpf(2);N=[16,32,64,128,256]
for n in N:
    nodes,weights,J=make_quad(n,D);bound=2*J/mp.pi
    targets=[mp.mpf(-2),mp.mpf('-.5'),mp.mpf(0),mp.mpf('.5'),mp.mpf(2),nodes[n//2+1]]
    errs=[]
    for target in targets:
        e0=abs(Qvalue(nodes,weights,D,target)-Hfinite(D,target))
        e1=abs(mp.diff(lambda v:Qvalue(nodes,weights,D,v)-Hfinite(D,v),target))
        assert e0<=bound and e1<=bound
        errs.append(dict(y=str(target),value_error=str(e0),derivative_error=str(e1)))
    diagnostics.append(dict(cells=n,D=str(D),A=str(A),sum_J=str(J),proved_interpolation_bound=str(bound),values=errs))
Ds=np.geomspace(4,1024,100);C=1+mp.sqrt(2)
t0=[float(abs(Tail(mp.mpf(v),mp.mpf(0)))) for v in Ds]
t1=[float(abs(mp.diff(lambda r:Tail(mp.mpf(v),r),A))) for v in Ds]
b0=[float(2*C/(mp.pi*(1-(A/mp.mpf(v))**2)*mp.mpf(v))) for v in Ds]
b1=[float(4*A*C/(3*mp.pi*(1-(A/mp.mpf(v))**2)**2*mp.mpf(v)**3)) for v in Ds]
assert all(a<=b for a,b in zip(t0,b0)) and all(a<=b for a,b in zip(t1,b1))
fig,ax=plt.subplots(1,3,figsize=(15.2,4.9));fig.suptitle('Full-line Hilbert error: finite interpolation and both omitted tails',y=1.03,fontweight='bold')
ax[0].loglog(N,[float(v['values'][3]['value_error']) for v in diagnostics],'o-',color=blue,label=r'Actual $|Q_{+,4}f-H_{+,4}f|$ at $y=1/2$')
ax[0].loglog(N,[float(v['values'][3]['derivative_error']) for v in diagnostics],'s-',color=purple,label=r'Actual first-derivative error at $y=1/2$')
ax[0].loglog(N,[float(v['proved_interpolation_bound']) for v in diagnostics],'--',color=orange,label=r'Proved bound $(2/\pi)\sum_i J_i$ for each')
ax[0].set_xlabel('Number of original cells (uniform z grid)');ax[0].set_ylabel('Interpolation error / proved bound');ax[0].set_title(r'$D=4,\ z_k=-\operatorname{arsinh}4+2k\operatorname{arsinh}4/N$')
ax[1].loglog(Ds,t0,color=blue,label=r'Exact $|T_{+,D}f(0)|$')
ax[1].loglog(Ds,b0,'--',color=orange,label=r'HQ14 bound on $[-2,2]$')
ax[1].set_title('Value tail retains its inverse-radius size');ax[1].set_xlabel('Actual original cutoff D');ax[1].set_ylabel('Value tail / proved bound')
ax[2].loglog(Ds,t1,color=purple,label=r'Exact $|\partial_y T_{+,D}f(2)|$')
ax[2].loglog(Ds,b1,'--',color=green,label=r'Oddness bound HQ14 on $[-2,2]$')
ax[2].set_title('Oddness gains one further inverse power');ax[2].set_xlabel('Actual original cutoff D');ax[2].set_ylabel('Derivative tail / proved bound')
for a in ax:a.grid(alpha=.2,which='both');a.legend(loc='best')
fig.text(.5,-.025,r'$f=-2x/(1+x^2),\ \sigma=+1,\ \beta=1,\ C_0=1+\sqrt{2},\ M_5\leq 240,\ M_6\leq 1440$.  HQ14, HQ21–HQ28 and HQ32–HQ38.',ha='center',fontsize=11)
fig.tight_layout();save(fig,'hilbert-tails-and-cubic-quadrature')
(R/'ccf-hilbert-benchmark.json').write_text(json.dumps(dict(arithmetic_digits=80,scope='High-precision numerical diagnostics; analytic error bounds are proved in HQ1–HQ38. These evaluations are not interval-certified arithmetic or source-trained data.',stencil='Cell i uses indices start,...,start+3; start=min(max(i-1,0),N-3). All weights use HQ22 and absolute quartic integrals use HQ24.',quadrature=diagnostics),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=3,quadrature_cells=N,numerical_value_and_derivative_comparisons=60,arithmetic_digits=80)))

"""Original scientific figures and independent symbolic/integral checks.

No input or write lies outside this workflow, except read-only libraries.
"""
from pathlib import Path
import json, hashlib, platform, shutil
import numpy as np
import sympy as sp
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
SRC=ROOT/'src'; SRC.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'petrowsky-schwartz-032','axes.titlesize':14,'axes.labelsize':13})
def save(fig,name):
    fig.savefig(FIG/(name+'.png'),dpi=170,facecolor='white',metadata={'Software':'original reproducible matplotlib figure'})
    fig.savefig(FIG/(name+'.svg'),facecolor='white',metadata={'Date':None,'Creator':'original reproducible matplotlib figure'})
    plt.close(fig)

xi=np.linspace(-4,4,801)
fig,ax=plt.subplots(figsize=(10.4,6.3))
ax.plot(xi,xi**2,color='#167844',lw=2.8,label=r'Forward heat: $z=i\xi^2$')
ax.plot(xi,-np.log1p(xi**2),color='#1c61a1',lw=3,label=r'Convolution evolution: $z=-i\log(1+\xi^2)$')
ax.plot(xi,-xi**2,color='#ad3434',lw=2.6,ls='--',label=r'Backward heat: $z=-i\xi^2$')
ax.axhline(0,color='#555555',lw=.9);ax.axvline(0,color='#555555',lw=.9)
ax.set(xlim=(-4.2,4.2),ylim=(-17,17),xlabel=r'Real spatial frequency $\xi$',ylabel=r'Imaginary time root coordinate $\operatorname{Im} z$',title='Root sign determines growth in forward time')
ax.text(-3.88,11.0,r'$\operatorname{Re}\lambda=-\operatorname{Im}z$'+'\nNegative imaginary roots grow.',bbox={'facecolor':'white','edgecolor':'#999999','pad':7},fontsize=11)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.20),frameon=False,ncol=1,fontsize=11)
ax.grid(alpha=.16);fig.subplots_adjust(left=.11,right=.97,top=.90,bottom=.28)
save(fig,'time-root-growth-032')

fig,ax=plt.subplots(figsize=(9.4,6.4))
t=np.linspace(0,4.75,400)
ax.fill_betweenx(t,-t,t,color='#d7e5f4',alpha=.58)
ax.plot(-t,t,color='#6585a4',lw=1.3);ax.plot(t,t,color='#6585a4',lw=1.3)
ax.plot(np.zeros(400),t,color='#466a8a',ls=':',lw=1.4)
for k in range(5):
    ax.scatter([0],[k],s=65,c='#153e68',zorder=5)
    label=r'$k=0:\ \delta_0(t)\otimes\delta_0(x)$' if k==0 else rf'$k={k}:\ \delta_{k}(t)\otimes D_x^{{{2*k}}}\delta_0(x)$'
    ax.annotate(label,(0,k),xytext=(15,7),textcoords='offset points',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','pad':2.7},zorder=6)
ax.text(-2.1,3.8,r'$t\geq |x|$'+'\nA containing cone',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','pad':4})
ax.text(-2.13,.55,'Dots show exact support points.\nThey do not show distribution values.',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','pad':4})
ax.annotate('Further terms continue upward',(0,4.69),xytext=(-2.18,4.62),arrowprops={'arrowstyle':'->','color':'#153e68'},fontsize=10,va='center')
ax.set(xlim=(-2.45,2.45),ylim=(-.32,4.95),xlabel=r'Spatial coordinate $x$',ylabel=r'Time coordinate $t$',title='A causal delay inverse with increasing spatial derivative order')
ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks(range(5));ax.grid(alpha=.13)
fig.subplots_adjust(left=.10,right=.98,top=.89,bottom=.14)
save(fig,'delay-convolution-support-032')

geometry={'schema':'exact-original-figure-geometry/v1','figure1':{'domain':[-4,4],'sample_count':801,'coordinate_axes':['real spatial xi','imaginary time root Im z'],'exact_curves':['Im z=xi^2','Im z=-log(1+xi^2)','Im z=-xi^2'],'evolution_relation':'lambda=i z; Re lambda=-Im z','proof_locators':['(35)','(37)','(42)','Exercise1']},'figure2':{'displayed_exact_support_points':[[k,0] for k in range(5)],'coordinate_order':'(t,x)','full_exact_support':'{(k,0): k=0,1,...}','derivative_order':{str(k):2*k for k in range(5)},'containing_cone':'t>=abs(x)','full_support_equals_cone':False,'distribution_values_plotted':False,'proof_locators':['(43)','(44)','(45)','Exercise6']},'private_images_copied':False}
(FIG/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')

t,x,z,lam,s,a,b=sp.symbols('t x z lam s a b',real=True)
checks=[]
def verify(name,value):
    if isinstance(value,sp.MatrixBase): ok=all(sp.simplify(v)==0 for v in value)
    else:ok=sp.simplify(value)==0
    checks.append({'name':name,'passed':bool(ok),'residual':str(sp.simplify(value))})
    if not ok:raise AssertionError((name,value))
# Exact nilpotent and companion identities, including force sign.
J=sp.Matrix([[0,x**3],[0,0]]); MJ=sp.eye(2)+t*J
verify('nilpotent matrix ODE',sp.diff(MJ,t)-J*MJ)
verify('nilpotent initial normalization',MJ.subs(t,0)-sp.eye(2))
AP=sp.Matrix([[0,1],[-x**2,0]])
verify('wave companion characteristic determinant',AP.charpoly(lam).as_expr().subs({sp.Symbol('lam'):lam})-(lam**2+x**2))
Mw=sp.Matrix([[sp.cos(t*x),sp.sin(t*x)/x],[-x*sp.sin(t*x),sp.cos(t*x)]])
verify('wave matrix ODE',sp.diff(Mw,t)-AP*Mw)
verify('wave initial normalization',Mw.subs(t,0)-sp.eye(2))
verify('wave derivative at initial time',sp.diff(Mw,t).subs(t,0)-AP)
verify('wave forcing Green sign',sp.diff(-sp.sin((t-s)*x)/x,t,2)+x**2*(-sp.sin((t-s)*x)/x))
verify('wave forcing initial derivative is minus one',sp.diff(-sp.sin((t-s)*x)/x,t).subs(t,s)+1)
verify('heat sign lambda=i z',sp.I*(sp.I*x**2)+x**2)
verify('heat companion forcing factor',sp.I/sp.I-1)
verify('Schwartz logarithmic multiplier ODE',sp.diff((1+x**2)**t,t)-sp.log(1+x**2)*(1+x**2)**t)
verify('forward exponential spatial derivative Duhamel',sp.integrate(sp.exp(-(t-s)*x**2)*(-2*x)*sp.exp(-s*x**2),(s,0,t))-sp.diff(sp.exp(-t*x**2),x))
# Derivative formula with noncommuting matrices: exact polynomial parameter and finite nilpotence.
A=sp.Matrix([[0,x,0],[0,0,1],[0,0,0]])
assert A*sp.diff(A,x)!=sp.diff(A,x)*A
M=sp.eye(3)+t*A+t**2*A**2/2
Mtms=sp.eye(3)+(t-s)*A+(t-s)**2*A**2/2
Ms=sp.eye(3)+s*A+s**2*A**2/2
verify('noncommuting parameter derivative integral',sp.integrate(Mtms*sp.diff(A,x)*Ms,(s,0,t))-sp.diff(M,x))
# Exact higher time-order companion coefficient conversion for several degrees.
for q in range(1,6):
    coeff=sp.symbols('a0:'+str(q))
    C=sp.zeros(q)
    for j in range(q-1):C[j,j+1]=1
    for j in range(q):C[q-1,j]=-sp.I**(q-j)*coeff[j]
    det=(lam*sp.eye(q)-C).det()
    target=lam**q+sum(sp.I**(q-j)*coeff[j]*lam**j for j in range(q))
    verify(f'companion characteristic q={q}',det-target)
# Delay symbol at its claimed exact roots, positive frequency suffices by xi^2 symmetry.
rho=sp.symbols('rho',positive=True);ell=sp.symbols('ell',integer=True)
verify('delay logarithmic zero coordinates',1-rho**2*sp.exp(-sp.I*(2*sp.pi*ell-2*sp.I*sp.log(rho))))
verify('delay finite telescoping identity',sum(z**k for k in range(7))*(1-z)-(1-z**7))

# Independent Fourier integrals check the actual nonunitary heat factor and semigroup convolution.
integrals=[]
for tau in [.2,.7,1.5]:
    for xx in [-1.2,0.,.6,2.]:
        val=quad(lambda eta:np.cos(xx*eta)*np.exp(-tau*eta*eta),-np.inf,np.inf,epsabs=2e-11)[0]/(2*np.pi)
        exact=np.exp(-xx*xx/(4*tau))/np.sqrt(4*np.pi*tau)
        integrals.append({'kind':'inverse Fourier heat kernel','t':tau,'x':xx,'observed':val,'exact':exact,'abs_error':abs(val-exact)})
for ta,tb in [(.2,.3),(.7,1.1)]:
    for xx in [-.8,0.,1.3]:
        H=lambda tau,yy:np.exp(-yy*yy/(4*tau))/np.sqrt(4*np.pi*tau)
        val=quad(lambda yy:H(ta,xx-yy)*H(tb,yy),-np.inf,np.inf,epsabs=2e-11)[0]
        exact=H(ta+tb,xx)
        integrals.append({'kind':'heat convolution semigroup','t':ta,'s':tb,'x':xx,'observed':val,'exact':exact,'abs_error':abs(val-exact)})
# Numerical bound for nonnormal matrices with repeated roots / highly skew offdiagonal sizes.
bounds=[]
for size in [2,3,4]:
    for skew in [.3,3.,20.]:
        B=np.diag([-1.]*size).astype(complex)
        for j in range(size-1):B[j,j+1]=skew*(j+1)
        for tau in [0.,.2,1.1]:
            observed=float(np.linalg.norm(expm(tau*B),2))
            bound=float(np.exp(-tau)*sum((2*tau*np.linalg.norm(B,2))**k/float(sp.factorial(k)) for k in range(size)))
            assert observed<=bound*(1+1e-12)
            bounds.append({'r':size,'skew':skew,'t':tau,'norm':observed,'proved_bound':bound})
result={'schema':'mathematical-reproduction/v1','runtime':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},'symbolic_checks':checks,'integral_checks':integrals,'max_integral_abs_error':max(x['abs_error'] for x in integrals),'matrix_bound_checks':bounds,'no_unproved_general_theorem_inferred_from_samples':True}
assert result['max_integral_abs_error']<1e-9
(ROOT/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if (ROOT/'manuscript.md').exists():
    shutil.copyfile(ROOT/'manuscript.md',SRC/'root-growth-and-cauchy-evolution-in-schwartz-spaces.md')
print(json.dumps({'symbolic_checks':len(checks),'integral_checks':len(integrals),'matrix_checks':len(bounds),'max_integral_abs_error':result['max_integral_abs_error']}))

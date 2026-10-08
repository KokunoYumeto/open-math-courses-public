"""Exact quadratic motion and explicitly numerical flat-profile coordinate sections."""
from pathlib import Path
import hashlib,json,math,xml.etree.ElementTree as ET
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
r=Path(__file__).resolve().parents[1];dest=r/'figures';dest.mkdir(parents=True,exist_ok=True)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
x=lambda t:95+315*(t+1)
checks=[];paths=[]
colors={0:'#bd4d3e',.25:'#72a4bd',.5:'#236985'}
def curve(lo,hi,f,df,base,scale,color):
    dt=hi-lo;y=lambda a:base-scale*a
    control=f(lo)+df(lo)*dt/2
    for j in range(21):
        u=j/20;t=lo+dt*u;value=(1-u)**2*f(lo)+2*(1-u)*u*control+u*u*f(hi)
        assert abs(value-f(t))<1e-12;checks.append({'t':t,'value':f(t),'bezier':value})
    return f'<path d="M{x(lo):g},{y(f(lo)):g} Q{x((lo+hi)/2):g},{y(control):g} {x(hi):g},{y(f(hi)):g}" fill="none" stroke="{color}" stroke-width="3.3"/>'
for c in [0,.25,.5]:
    paths.append(curve(-1,0,lambda t:t*t-2*c*t,lambda t:2*t-2*c,330,95,colors[c]))
    paths.append(curve(0,1,lambda t:t*t+2*c*t,lambda t:2*t+2*c,330,95,colors[c]))
for c in [.5,.25]:
    for k in range(int(1/c)):
        lo=-1+2*c*k;hi=lo+2*c
        paths.append(curve(lo,hi,lambda t,lo=lo,c=c:2*c*(t-lo)-(t-lo)**2,
          lambda t,lo=lo,c=c:2*c-2*(t-lo),680,430,colors[c]))
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="770" viewBox="0 0 840 770" role="img" aria-labelledby="title desc">
<title id="title">Diffractive and gliding characteristic motion</title><desc id="desc">Exact parabolic normal radii for the two canonical symbols. Red is c equals zero, light blue c equals one quarter, and dark blue c equals one half. Tangential coordinate y is Hamilton time. The upper red limit is an interior tangent parabola. The lower red limit is boundary gliding.</desc>
<rect x="14" y="14" width="812" height="365" rx="14" fill="#f6f8fa"/><rect x="14" y="397" width="812" height="359" rx="14" fill="#f6f8fa"/>
<g font-family="Arial,sans-serif" fill="#263c48">
<text x="34" y="47" font-size="22" font-weight="700">Diffractive contact: p = ρ² − r + η</text>
<text x="34" y="79" font-size="17">r = y² + 2c|y|,   ρ = y + c sign(y),   η = −c²</text>
<text x="100" y="111" font-size="16" fill="#bd4d3e">c = 0</text><text x="250" y="111" font-size="16" fill="#72a4bd">c = 1/4</text><text x="405" y="111" font-size="16" fill="#236985">c = 1/2</text>
<path d="M78 124 V330 H754" fill="none" stroke="#88989f" stroke-width="1.4"/>
<path d="M95 330 H727 M95 235 H727 M95 140 H727" fill="none" stroke="#c8d1d5"/>
<text x="53" y="130" font-size="18">r</text><text x="55" y="336" font-size="16">0</text><text x="55" y="241" font-size="16">1</text><text x="55" y="146" font-size="16">2</text>
<text x="85" y="356" font-size="16">−1</text><text x="404" y="356" font-size="16">0</text><text x="718" y="356" font-size="16">1</text><text x="763" y="336" font-size="18">y</text>
<text x="34" y="430" font-size="22" font-weight="700">Gliding contact: p = ρ² + r + η</text>
<text x="34" y="462" font-size="17">r = 2cu − u²,  ρ = c − u,  0 ≤ u ≤ 2c;  reflect and repeat</text>
<text x="100" y="494" font-size="16" fill="#bd4d3e">c = 0: r = ρ = η = 0</text>
<text x="407" y="494" font-size="16" fill="#236985">height c², spacing 2c</text>
<path d="M78 523 V680 H754" fill="none" stroke="#88989f" stroke-width="1.4"/>
<path d="M95 680 H727 M95 572.5 H727" fill="none" stroke="#c8d1d5"/>
<text x="52" y="530" font-size="18">r</text><text x="52" y="686" font-size="16">0</text><text x="37" y="578" font-size="16">1/4</text>
<text x="85" y="706" font-size="16">−1</text><text x="404" y="706" font-size="16">0</text><text x="718" y="706" font-size="16">1</text><text x="763" y="686" font-size="18">y</text>
''' + ''.join(paths)+'''<path d="M95 680 H725" stroke="#bd4d3e" stroke-width="3.3"/>
<text x="34" y="738" font-size="16">GF16–GF19 and Exercise 1: Hamilton time increases to the right.</text>
</g></svg>'''
ET.fromstring(svg);first=dest/'diffractive-and-gliding-motion.svg';first.write_text(svg,encoding='utf8')
# The following figure is a numerical illustration with the exact rescalings stated.
def raw(z):return math.exp(-1/(1-4*z*z)) if abs(z)<.5 else 0.0
integral,error=quad(raw,-.5,.5,epsabs=1e-14,epsrel=1e-14);norm=1/integral
kap=lambda z:norm*raw(z)
assert abs(quad(kap,-.5,.5,epsabs=1e-12)[0]-1)<1e-11
assert abs(quad(lambda z:z*kap(z),-.5,.5,epsabs=1e-12)[0])<1e-13
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'an04-u053-flat-contact','text.usetex':False})
fig,axes=plt.subplots(3,2,figsize=(11.3,8.8),gridspec_kw={'width_ratios':[1.35,1]})
samples=[]
for row,j in enumerate([2,3,4]):
    ratio=1/(1+math.exp(2*j-1));delta=2**(-j)
    us=np.unique(np.concatenate([np.linspace(0,1,300),1-ratio+ratio*np.linspace(-.5,.5,151)]))
    profile=[]
    for u in us:
        z=(u-1+ratio)/ratio
        if z<=-.5:value=u
        elif z>=.5:value=(1/ratio-1)*(1-u)
        else:
            f0=quad(kap,-.5,z,epsabs=1e-13)[0];f1=quad(lambda zz:zz*kap(zz),-.5,z,epsabs=1e-13)[0]
            value=u-((u-1+ratio)*f0-ratio*f1)/ratio
        assert value>=-1e-10 and value<=1+1e-10;profile.append(max(0,value))
    assert abs(profile[0])<1e-12 and abs(profile[-1])<1e-12
    ax=axes[row,0];ax.plot(us,profile,color='#236985',linewidth=2);ax.axhline(0,color='#bd4d3e',linewidth=1)
    ax.set(xlim=(0,1),ylim=(-.06,1.08),ylabel=r'$r/(\Delta_j v_j)$',xlabel=r'$u=(t-t_j)/\Delta_j$')
    ax.set_title(rf'$j={j}:\ \Delta_j=2^{{-{j}}},\ v_j=e^{{-{j*j}}}$',fontsize=13)
    ax.grid(alpha=.2)
    zz=np.linspace(-.5,.5,301);force=[-kap(z) for z in zz]
    ax=axes[row,1];ax.plot(zz,force,color='#925a31',linewidth=2)
    ax.set(xlim=(-.5,.5),ylabel=r'$2\mu_j a/(v_j+v_{j-1})$',xlabel=r'$z=(t-t_{j-1}+\mu_j)/\mu_j$')
    ax.set_title(rf'$\mu_j=\Delta_j/(1+e^{{{2*j-1}}})$',fontsize=13);ax.grid(alpha=.2)
    samples.append({'j':j,'delta':delta,'v':math.exp(-j*j),'mu':delta*ratio,'profile_samples':len(us),'profile_min':min(profile),'profile_max':max(profile),'scaling':'u=(t-t_j)/Delta_j; radius=r/(Delta_j*v_j); force=2mu_j*a/(v_j+v_{j-1})=-kappa'})
fig.suptitle('Flat contact: tiny late pulses close each reflected excursion',fontsize=17,y=.99)
fig.text(.5,.013,'Numerical samples of GF35–GF39. The red line is the alternative gliding radius r = 0.\nEach row uses its stated rescaling; physical radii shrink faster than every power of t.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.06,1,.955))
second=dest/'flat-contact-reflection-mechanism.svg'
fig.savefig(second,metadata={'Date':None,'Title':'Flat contact reflection mechanism','Creator':'GPT-6.1 Sol (OpenAI), Ultra','Description':'Numerical samples with exact coordinate rescalings of the smooth flat-force example GF35-GF41; not a proof certificate.'});plt.close(fig)
ET.fromstring(second.read_text(encoding='utf8'))
third=dest/'compressed-volume-and-clock-slices.svg'
volume_svg='''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="510" viewBox="0 0 960 510" role="img" aria-labelledby="title desc">
<title id="title">Normal compression changes coordinate area, not Liouville mass</title>
<desc id="desc">In normalized coordinates the rectangle 0 less than x less than 1 and absolute y less than 1 maps by z equals x y to the triangle absolute z less than x. Its Euclidean area changes from 2 epsilon cubed to epsilon to the fifth. The density d r d kappa divided by r retains mass 2 epsilon cubed. The normal boundary segment collapses to the vertex.</desc>
<rect width="960" height="510" fill="#fff"/>
<g font-family="Arial,sans-serif" fill="#263c48">
<text x="28" y="36" font-size="23" font-weight="700">Normal compression: κ = rρ</text>
<text x="28" y="65" font-size="16">GF30, GFA1 and Exercise 4 · independently normalized axes</text>
<text x="60" y="110" font-size="19" font-weight="700">Ordinary normal coordinates</text>
<text x="535" y="110" font-size="19" font-weight="700">Compressed normal coordinates</text>
<path d="M100 155 H400 V375 H100 Z" fill="#d9edf3" stroke="#236985" stroke-width="2"/>
<path d="M570 265 L870 155 V375 Z" fill="#d9edf3" stroke="#236985" stroke-width="2"/>
<g stroke="#859ca8" stroke-width="1.4" fill="none"><path d="M82 265 H420 M100 390 V138 M552 265 H891 M570 390 V138"/></g>
<g stroke="#75a5b8" stroke-width="1.5" stroke-dasharray="5 4"><path d="M250 155 V375 M720 210 V320"/></g>
<path d="M100 155 V375" stroke="#bd4d3e" stroke-width="4"/><circle cx="570" cy="265" r="4.5" fill="#bd4d3e"/>
<path d="M447 265 H509 L500 259 M509 265 L500 271" fill="none" stroke="#263c48" stroke-width="2"/>
<text x="450" y="245" font-size="17">z = xy</text>
<text x="66" y="153" font-size="16">1</text><text x="59" y="381" font-size="16">−1</text>
<text x="536" y="153" font-size="16">1</text><text x="529" y="381" font-size="16">−1</text>
<text x="81" y="287" font-size="16">0</text><text x="398" y="288" font-size="16">1</text>
<text x="549" y="287" font-size="16">0</text><text x="868" y="288" font-size="16">1</text>
<text x="115" y="143" font-size="16">y = ρ/ε</text><text x="586" y="143" font-size="16">z = κ/ε³</text>
<text x="278" y="404" font-size="16">x = r/ε²</text><text x="748" y="404" font-size="16">x = r/ε²</text>
<text x="60" y="438" font-size="18">Euclidean area: 2ε³</text>
<text x="535" y="438" font-size="18">Euclidean area: ε⁵</text>
<text x="535" y="468" font-size="18" font-weight="700">Mass with dr dκ/r: 2ε³</text>
<text x="60" y="489" font-size="15" fill="#a44135">Boundary segment → vertex; r = 0 has measure zero.</text>
</g></svg>'''
ET.fromstring(volume_svg);third.write_text(volume_svg,encoding='utf-8')
volume_checks=[]
for xx in [.125,.25,.5,.75,1.]:
 for yy in [-1.,-.5,0.,.5,1.]:
  zz=xx*yy
  assert abs(zz)<=xx and abs(zz/xx-yy)<1e-15
  volume_checks.append({'x':xx,'y':yy,'z':zz})
record={'schema':'an04-generalized-glancing-figures/v1','source_sha256':sha(r/'generalized-glancing-flow-preparation.md'),
 'figures':[{'asset':str(first.relative_to(r)).replace('\\','/'),'sha256':sha(first),'kind':'Exact quadratic coordinate sections','proof_locators':['GF16-GF19','GF43-GF44'],'base_map':'y->95+315(y+1); diffractive r->330-95r; gliding r->680-430r','exact_bezier_checks':checks,'schematic':False,'numerical_sample':False},
 {'asset':str(second.relative_to(r)).replace('\\','/'),'sha256':sha(second),'kind':'Explicitly numerical smooth bump/profile samples with exact rescalings','proof_locators':['GF35-GF41'],'bump':'C exp(-1/(1-4z^2)) for abs(z)<1/2; C reciprocal of exact defining integral','computed_normalization':norm,'quadrature_absolute_error_estimate':error,'samples':samples,'schematic':False,'numerical_sample':True}],
 'actual_images_inspected':False,'original_licence':'CC0-1.0','script_sha256':sha(Path(__file__))}
record['figures'].append({'asset':'figures/'+third.name,'sha256':sha(third),'kind':'Exact normal compression and Liouville density','proof_locators':['GF30','GFA1','GF48'],'coordinates':'x=r/epsilon^2, y=rho/epsilon, z=kappa/epsilon^3=x*y','uncompressed_area':'2epsilon^3','compressed_coordinate_area':'epsilon^5','compressed_density':'dr d kappa/r','weighted_mass':'2epsilon^3','exact_coordinate_checks':volume_checks,'schematic':False,'numerical_sample':False})
(r/'figure-check.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print({'figures':3,'exact_quadratic_points_checked':len(checks),'numerical_profile_rows':len(samples),'actual_visual_inspection_pending':True})

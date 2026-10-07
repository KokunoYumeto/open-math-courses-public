"""Reproducible sampled flow diagram and exact finite-model identities."""
from pathlib import Path
import datetime,hashlib,json,math,html
import sympy as sp
MOD=Path(__file__).resolve().parent;r=MOD.parents[3];p=MOD/'figures';a=MOD;p.mkdir(exist_ok=True)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
d,x,y,eta=sp.symbols('d x y eta',real=True)
Rp=sp.sqrt(1+sp.exp(2*d)*sp.sinh(y)**2)
Rm=sp.sqrt(1+sp.exp(-2*d)*sp.sinh(x)**2)
X=sp.asinh(sp.exp(d)*sp.sinh(y));Y=sp.asinh(sp.exp(-d)*sp.sinh(x))
J=sp.exp(d)*sp.cosh(y)/Rp;xi=sp.exp(-d)*Rp/sp.cosh(y)
checks=[]
def zero(name,*exprs):
    reduced=[sp.simplify(z) for z in exprs];assert all(z==0 for z in reduced),(name,reduced)
    checks.append({'name':name,'exact_reduced_residuals':[str(z) for z in reduced],'passed':True})
zero('Hamilton base equation and full base derivative',sp.diff(X,d)-sp.exp(d)*sp.sinh(y)/Rp,sp.diff(X,y)-J)
zero('Jacobian growth and covector equation',sp.diff(J,d)-J/Rp**2,sp.diff(xi,d)+xi/Rp**2,J*xi-1)
zero('Forward Hamilton-Jacobi and backward initial parameter',sp.diff(Y*eta,d)+sp.tanh(x)*sp.diff(Y*eta,x),-sp.diff(Y*eta,d)-eta*sp.exp(-d)*sp.sinh(x)/Rm)
zero('Density derivative and reduced-symbol factor',sp.diff(J**sp.Rational(-1,2),d)+J**sp.Rational(-1,2)/(2*Rp**2),J**sp.Rational(-1,2)*J**sp.Rational(1,2)-1)
zero('Initial phase, initial position and Jacobian',Y.subs(d,0)-sp.asinh(sp.sinh(x)),X.subs(d,0)-sp.asinh(sp.sinh(y)),J.subs(d,0)-1)
ca,cb=sp.symbols('a b',real=True);N1=sp.Matrix([[0,1],[0,0]]);N2=sp.Matrix([[0,0],[1,0]]);I=sp.eye(2)
U=(I-cb*N2)*(I-ca*N1);Ui=(I+ca*N1)*(I+cb*N2)
zero('Ordered pulse product and both inverses',*(U-sp.Matrix([[1,-ca],[-cb,1+ca*cb]])),*(Ui*U-I),*(U*Ui-I))
zero('Initial and final derivative factor order',*(-U.diff(ca)-U*N1),*(U.diff(cb)+N2*U))
zero('Explicit noncommuting right and left products',*(U*N1-sp.Matrix([[0,1],[0,-cb]])),*(N1*U-sp.Matrix([[-cb,1+ca*cb],[0,0]])))
source=MOD/'oscillatory-cauchy-kernels-and-exact-evolution.md';assert source.read_text(encoding='utf8').count('**Solution.**')==3
W,H=1100,840
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
'<title id="title">Variable-speed Cauchy fronts and transported covectors</title>',
'<desc id="desc">Base positions X=arsinh(exp(t) sinh(y)) and covectors xi=exp(-t) cosh(X)/cosh(y), for y=-1,0,1 and initial eta=1. Curves are piecewise linear samples at121 equally spaced times, from0 to2. Exact formulas and delta weight are proved in Section7.3.</desc>',
'<rect width="1100" height="840" fill="#fffdf7"/>',
'<g font-family="Arial,sans-serif" font-size="17" fill="#253e4b">']
def text(xp,yp,t,size=17,color='#253e4b',anchor='start'):
    parts.append(f'<text x="{xp}" y="{yp}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#deded4',width=1,dash=None):
    extra=f' stroke-dasharray="{dash}"' if dash else ''
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>')
text(55,40,'Variable speed preserves the flow graph and changes the delta weight',25)
text(110,78,'Base flow: X(t,0,y)=arsinh(exp(t) sinh(y))',20)
for tv in [0,0.5,1,1.5,2]:
    xp=110+340*tv;line(xp,110,xp,410);text(xp,437,str(tv),15,anchor='middle')
for xv in [-3,-2,-1,0,1,2,3]:
    yp=260-50*xv;line(110,yp,790,yp);text(95,yp+5,str(xv),15,anchor='end')
line(110,110,110,410,'#253e4b',1.5);line(110,410,790,410,'#253e4b',1.5)
text(87,97,'x',18);text(812,437,'t',18)
colors={-1:'#a44444',0:'#596951',1:'#126879'}
samples=[];geometry=[]
for y0 in [-1,0,1]:
    rows=[]
    for j in range(121):
        tv=j/60;xx=math.asinh(math.exp(tv)*math.sinh(y0));jj=math.exp(tv)*math.cosh(y0)/math.cosh(xx);cv=1/jj
        assert -3<xx<3 and math.exp(-tv)-1e-13<=cv<=1+1e-13
        rows.append({'t':tv,'X':xx,'J_X':jj,'xi':cv})
    samples.append({'initial_y':y0,'initial_eta':1,'points':rows})
    coords=' '.join(f'{110+340*z["t"]:.7f},{260-50*z["X"]:.7f}' for z in rows)
    parts.append(f'<polyline points="{coords}" fill="none" stroke="{colors[y0]}" stroke-width="3"/>')
    text(815,260-50*rows[-1]['X']+6,f'y={y0}',18,colors[y0])
    geometry.append({'initial_y':y0,'all_base_plot_points_inside':True,'all_covectors_positive':True,'sharp_lower_bound_exp_minus_t_verified_on_samples':True})
text(815,189,'Initial data at y',17)
text(815,216,'travels to X(t,0,y).',17)
text(815,320,'Delta weight:',17)
text(815,347,'J_X W_C e',20)
text(815,374,'It need not be one.',16)
text(110,513,'Cotangent section: eta=1, xi=1/J_X >0',20)
for tv in [0,0.5,1,1.5,2]:
    xp=110+340*tv;line(xp,550,xp,750);text(xp,778,str(tv),15,anchor='middle')
for cv in [0,0.25,0.5,0.75,1]:
    yp=750-190*cv;line(110,yp,790,yp);text(95,yp+5,str(cv),15,anchor='end')
line(110,550,110,750,'#253e4b',1.5);line(110,750,790,750,'#253e4b',1.5)
text(76,535,'xi',18);text(812,778,'t',18)
for yi,col in [(1,'#76508a'),(0,colors[0])]:
    rows=next(z['points'] for z in samples if z['initial_y']==yi)
    coords=' '.join(f'{110+340*z["t"]:.7f},{750-190*z["xi"]:.7f}' for z in rows)
    parts.append(f'<polyline points="{coords}" fill="none" stroke="{col}" stroke-width="3"/>')
    text(815,750-190*rows[-1]['xi']+6,'y=+1 and y=-1' if yi else 'y=0: xi=exp(-t)',17,col)
text(815,566,'Kernel input covector:',16)
text(815,592,'-eta=-1',19)
text(55,817,'Proof: Section7.3, (CE38)-(CE40). Curves sampled at121 times; exact identities and bounds remain in the text.',15)
parts.append('</g></svg>\n')
svg=p/'fio-cauchy-variable-speed.svg';svg.write_text('\n'.join(parts),encoding='utf8')
samplefile=MOD/'figure-samples.json';samplefile.write_text(json.dumps(samples,indent=2)+'\n',encoding='utf8')
report={'schema':'an04-fio-cauchy-exact-model-checks/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'passed':True,'finite_groups':len(checks),'checks':checks,'svg_sha256':sha(svg),'sampling_record':str(samplefile.relative_to(r)),'sampling_sha256':sha(samplefile),'geometry':geometry,'coordinate_maps':{'base':'screenX=110+340t, screenY=260-50X; 0<=t<=2, -3<=X<=3','cotangent':'screenX=110+340t, screenY=750-190xi; 0<=t<=2, 0<=xi<=1'},'curve_representation':'Piecewise linear rendering of121 exact-formula numerical samples per curve. Two outer covector curves coincide by symmetry. No samples are a proof substitute.','source_hashes':{source.name:sha(source),'figures/'+svg.name:sha(svg)},'full_figure_visually_inspected':False,'Blender_used':False,'Blender_decision':'The exact two-dimensional base and cotangent panels show this construction directly; no three-dimensional scene improves the required identities.'}
(a/'model-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'exact_model_groups':len(checks),'passed':True,'original_svg_created':True,'figure_visual_inspection_pending':True}))

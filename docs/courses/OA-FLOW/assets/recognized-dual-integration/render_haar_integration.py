"""Original four-block Haar-average diagram. CC0-1.0 to the extent of rights held.

Reproduce with Python, Matplotlib 3.10.9 and NumPy 2.4.4:
    python render_haar_integration.py --output OUTPUT_DIRECTORY

No TeX, external art or network access. Typography terms are in ASSET_TERMS.md.
Private build/layout receipts are emitted separately from the mathematical data.
"""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json,os,re

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,required=True)
out=parser.parse_args().output.resolve()
out.mkdir(parents=True,exist_ok=True)
os.environ['MPLCONFIGDIR']=str(out/'runtime-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
from matplotlib.text import Text

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
    'text.usetex':False,'svg.fonttype':'path','svg.hashsalt':'OA-FLOW-L31-four-block-original-20261006'})

def save_json(name,value):
    (out/name).write_bytes((json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))

c=Fraction(3)
d=Fraction(1,12)
assert 4*d*c*c==c
assert 4*d==Fraction(1,3)
root_pairs=[(1,0),(0,1),(-1,0),(0,-1)]
exact_projections=[]
for j in range(4):
    row=[]
    for ell in range(4):
        terms=[root_pairs[((ell-j)*s)%4] for s in range(4)]
        pair=[sum(t[q] for t in terms) for q in (0,1)]
        assert pair==([4,0] if ell==j else [0,0])
        row.append(pair[0]//4)
    exact_projections.append(row)
assert all(((j-k)*s-j*s+k*s)%4==0 for j in range(4) for k in range(4) for s in range(4))

vectors=[np.array([1,0]),np.array([1,1]),np.array([0,1]),np.array([1,1j])]
coefficients=[2,3,5,7]
X=[a*np.outer(v,v.conj()) for a,v in zip(coefficients,vectors)]
expected=np.array([[12,3-7j],[3+7j,15]],complex)
assert np.array_equal(sum(X),expected)
f=[1,0,2,4]
assert sum(f)*d==Fraction(7,12)
I2=np.eye(2)
checks={}

def check(name,actual,target):
    error=float(np.max(np.abs(np.asarray(actual)-np.asarray(target))))
    assert error<1e-12,(name,error)
    checks[name]=error

for j,block in enumerate(X):
    check(f'positive_factorization_X{j}',block,coefficients[j]*np.outer(vectors[j],vectors[j].conj()))
    assert np.linalg.eigvalsh(block).min()>=-1e-12
    check(f'selfadjoint_X{j}',block,block.conj().T)
for ell in range(4):
    average=sum((X[(ell-k)%4] for k in range(4)),start=np.zeros((2,2),complex))/12
    check(f'general_average_output_block_{ell}',average,expected/12)
    spectral=sum((f[(ell-k)%4]*I2 for k in range(4)),start=np.zeros((2,2),complex))/12
    check(f'spectral_average_output_block_{ell}',spectral,Fraction(7,12)*I2)
for k in range(4):
    for s in range(4):
        actual=np.array([(1j)**(((j-k)%4)*s) for j in range(4)])
        target=(1j)**(-k*s)*np.array([(1j)**(j*s) for j in range(4)])
        check(f'eigencharacter_k{k}_s{s}',actual,target)
test=np.array([[2,1+2j],[1-2j,4]])
check('constant_coefficient_normalized_average',3*sum([test]*4)/12,test)
check('identity_average',sum([I2]*4)/12,I2/3)
check('normalized_expectation_identity',3*sum([I2]*4)/12,I2)
eigenvalues=np.linalg.eigvalsh(expected/12)
assert eigenvalues.min()>0

def pairmatrix(a):
    return [[[int(z.real),int(z.imag)] for z in row] for row in a]

save_json('haar-integration-data.json',{
    'license':'CC0-1.0 to the extent of rights held; numerical facts are not claimed as exclusive property.',
    'model':{'G':'Z/4Z','H':'Z/4Z','pairing':'chi_j(s)=i^(j*s)',
        'beta':'beta_k(X)_j=X_(j-k)','eigenunitaries':'u_s|block_j=i^(j*s) I2',
        'coefficient_algebra':'constant M2 tuples','recovered_action':'trivial',
        'spectral_algebra':'scalar-block tuples','J':'J(f)_j=f_j I2'},
    'Haar':{'original_singleton_mass':'3','dual_singleton_mass':'1/12','dual_total_mass':'1/3',
        'Plancherel_identity_indicator_squared_norm':'3=4*(1/12)*3^2'},
    'exact_projection_values':exact_projections,
    'exact_phase_covariance_checked_for_all_64_triples':True,
    'matrix_entries_format':'Each scalar is [real integer, imaginary integer].',
    'positive_input_blocks':[pairmatrix(a) for a in X],
    'rank_one_coefficients':coefficients,
    'rank_one_vectors':[[[int(z.real),int(z.imag)] for z in v] for v in vectors],
    'sum_numerator':pairmatrix(expected),'average_denominator':12,
    'spectral_input_values':f,'spectral_average':'7/12 I2',
    'identity_average':'1/3 I2','unital_expectation':'3 E_beta',
    'average_eigenvalue_samples':eigenvalues.tolist(),
    'numeric_residuals':checks,'numeric_tolerance':1e-12,
    'scope':'Exact finite example with bounded output in M_2+. The general extended-positive target is proved in OA-FLOW-L31, Sections 4–6.'})

ink,blue,green,purple,orange='#173341','#155f8d','#127158','#735096','#a56327'
muted,border='#4a606b','#c7d2d9'
colors=[blue,green,purple,orange]
fig=plt.figure(figsize=(16,14),dpi=160,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')

def text(x,y,s,size=18,color=ink,weight='normal',ha='left'):
    return ax.text(x,y,s,fontsize=size,color=color,fontweight=weight,ha=ha,va='center',transform=ax.transAxes)

def line(x1,y1,x2,y2,color=border,lw=1.2):
    ax.plot([x1,x2],[y1,y2],color=color,lw=lw,transform=ax.transAxes)

def box(x,y,w,h,color=border,face='#f7f9fb'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.007,rounding_size=0.007',
        linewidth=1.5,edgecolor=color,facecolor=face,transform=ax.transAxes))

def arrow(x,y1,y2,color=blue):
    ax.add_patch(FancyArrowPatch((x,y1),(x,y2),arrowstyle='-|>',mutation_scale=21,
        linewidth=2,color=color,transform=ax.transAxes))

def matrix(cx,cy,entries,width=.115,height=.063,size=21,color=ink):
    # Four separately positioned entries avoid relying on a TeX matrix environment.
    for r in range(2):
        for q in range(2):
            text(cx+(q-.5)*width*.65,cy+(.5-r)*height*.65,
                 '$'+entries[r][q]+'$',size,color=color,ha='center')
    for side in (-1,1):
        x=cx+side*width*.60
        line(x,cy-height*.65,x,cy+height*.65,color,1.6)
        line(x,cy+height*.65,x-side*.009,cy+height*.65,color,1.6)
        line(x,cy-height*.65,x-side*.009,cy-height*.65,color,1.6)

text(.05,.967,'One Haar factor; two different kinds of positive input',27,weight='bold')
text(.05,.926,r'$N=M_2\oplus M_2\oplus M_2\oplus M_2,\qquad M=\{(a,a,a,a):a\in M_2\}$',22)
text(.05,.891,r'$G=\mathbb{Z}/4:\ c=3;\qquad H=\widehat G:\ d=\frac{1}{4c}=\frac{1}{12},\quad |H|=4d=\frac{1}{3}$',20,color=muted)
line(.5,.245,.5,.855,color=border)
text(.06,.846,'Arbitrary positive matrix blocks',20,color=blue,weight='bold')
text(.545,.846,'Positive spectral input J(f)',20,color=green,weight='bold')
text(.545,.816,r'$f=(1,0,2,4),\qquad J(f)_j=f_jI_2$',17,color=muted)

left_centers=[.155,.365,.155,.365]
right_centers=[.640,.850,.640,.850]
ys=[.660,.660,.480,.480]
entries=[[['2','0'],['0','0']],[['3','3'],['3','3']],
         [['0','0'],['0','5']],[['7','-7i'],['7i','7']]]
for j,y in enumerate(ys):
    for cx in (left_centers[j],right_centers[j]):
        box(cx-.087,y,.174,.133,color=colors[j])
    text(left_centers[j],y+.109,rf'$X_{j}$',18,color=colors[j],weight='bold',ha='center')
    matrix(left_centers[j],y+.052,entries[j],color=colors[j])
    text(right_centers[j],y+.109,rf'$J(f)_{j}$',18,color=colors[j],weight='bold',ha='center')
    text(right_centers[j],y+.052,rf'${f[j]}I_2$',28,color=colors[j],ha='center')

text(.26,.446,r'$\frac{1}{12}(X_0+X_1+X_2+X_3)$',22,ha='center')
text(.745,.446,r'$\frac{1}{12}(1+0+2+4)I_2$',22,ha='center')
arrow(.26,.421,.386,blue)
arrow(.745,.421,.386,green)
box(.065,.235,.39,.140,color=blue,face='#f1f7fb')
box(.550,.235,.39,.140,color=green,face='#eff8f3')
text(.26,.349,'Repeated output block',17,color=blue,weight='bold',ha='center')
text(.745,.349,'Repeated output block',17,color=green,weight='bold',ha='center')
text(.135,.287,r'$\frac{1}{12}$',27,ha='center')
matrix(.307,.287,[['12','3-7i'],['3+7i','15']],width=.195,height=.061,size=24,color=blue)
text(.745,.287,r'$\frac{7}{12}I_2$',33,color=green,ha='center')
text(.05,.202,'Each output is constant across all four blocks and lies in the same coefficient algebra M.',17)
text(.05,.163,r'$E_\beta(1_N)=\frac{1}{3}1_M.\qquad 3E_\beta\ \mathrm{is\ the\ unital\ expectation\ onto}\ M.$',22)
text(.05,.121,r'Full theorem: $E_\beta:N_+\to\widehat M_+$. Infinite outputs are allowed; this finite model has bounded outputs.',15,color=muted)
line(.05,.088,.95,.088)
text(.05,.066,'Proof: OA-FLOW-L31, l31-8-matrices, (L31.8.a)–(L31.8.f); full average l31-5; spectral formula l31-6.',12.3,color=muted)
text(.05,.042,'Antecedent: M. Takesaki, Theory of Operator Algebras II, Proposition X.2.6, pp.263–265.',12.3,color=muted)
text(.05,.018,'Original course illustration. Matrix coefficients 2, 3, 5, 7 are input data; they do not change either Haar measure.',12.3,color=muted)

fig.canvas.draw()
renderer=fig.canvas.get_renderer()
layout=[]
for t in fig.findobj(Text):
    if not t.get_visible() or not t.get_text():continue
    bounds=t.get_window_extent(renderer).bounds
    x,y,w,h=bounds
    inside=bool(x>=0 and y>=0 and x+w<=fig.bbox.width and y+h<=fig.bbox.height)
    layout.append({'text':t.get_text(),'bbox_px':[round(v,3) for v in bounds],'inside_canvas':inside})
assert all(t['inside_canvas'] for t in layout),[t for t in layout if not t['inside_canvas']]
manifest=[]
for ext in ('png','svg'):
    file=out/('haar-integration.'+ext)
    metadata={'Software':'OA-FLOW original mathematical illustration'} if ext=='png' else {'Date':None,'Creator':'OA-FLOW original mathematical illustration'}
    fig.savefig(file,dpi=160,format=ext,facecolor='white',metadata=metadata)
    if ext=='svg':file.write_bytes(re.sub(br'<!DOCTYPE svg PUBLIC[^>]*>\r?\n',b'',file.read_bytes(),count=1))
    manifest.append({'path':file.name,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'bytes':file.stat().st_size})
save_json('LAYOUT_CHECKS.json',{'canvas_px':list(fig.canvas.get_width_height()),'text_checks':layout})
save_json('BUILD_RECEIPT.json',{'runtime':{'matplotlib':matplotlib.__version__,'numpy':np.__version__,'tex_used':False},
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'outputs':manifest,
    'numeric_checks':len(checks),'maximum_residual':max(checks.values())})
print(json.dumps({'figures':1,'artifacts':2,'numeric_checks':len(checks),'maximum_residual':max(checks.values()),
    'exact_projection_values':exact_projections,'all_text_inside_canvas':True}))

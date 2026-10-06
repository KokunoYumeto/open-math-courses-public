"""Exact finite illustrations and checks; numerical examples do not prove K.2-K.4."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json, hashlib
import os
_LOCAL_HOME = Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR'] = str(_LOCAL_HOME / '.matplotlib-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent

# Local unmodified typeface; reject every unbound glyph font instead of silently substituting.
from matplotlib import font_manager as _fm
_FONT_ROOT = HERE / 'fonts'
_FONT = _FONT_ROOT / 'DejaVuSans.ttf'
if not _FONT.is_file():
    raise RuntimeError('Missing bound local DejaVu Sans typeface')
_fm.fontManager.addfont(str(_FONT))
_original_findfont = _fm.fontManager.findfont
def _local_findfont(*args, **kwargs):
    selected = Path(_original_findfont(*args, **kwargs))
    local = _FONT_ROOT / selected.name
    if not local.is_file():
        raise RuntimeError('Unbound selected font: ' + selected.name)
    return str(local)
_fm.fontManager.findfont = _local_findfont
_fm.findfont = _local_findfont
_actual_font_loads = []
_original_get_font = _fm.get_font
def _record_font_load(paths, *args, **kwargs):
    requested = [paths] if isinstance(paths, (str, bytes, Path)) else list(paths)
    for value in requested:
        path = Path(value).resolve()
        if path.parent != _FONT_ROOT.resolve():
            raise RuntimeError('Glyph load escaped bound local fonts')
        data = path.read_bytes()
        _actual_font_loads.append({'file': 'fonts/' + path.name, 'sha256': hashlib.sha256(data).hexdigest().upper(), 'bytes': len(data)})
    return _original_get_font(paths, *args, **kwargs)
_fm.get_font = _record_font_load

OUT = HERE / 'figures'
OUT.mkdir(exist_ok=True)
PARTITIONS = [[[0,1,2,3]], [[0,1],[2,3]], [[0],[1],[2],[3]]]

def expectation(f, w, cells):
    result = [Q(0)] * len(f)
    for cell in cells:
        mass = sum((w[i] for i in cell), Q(0))
        value = sum((w[i]*f[i] for i in cell), Q(0))/mass if mass else Q(0)
        for i in cell: result[i] = value
    return result

def norm(f,w):
    return sum((w[i]*abs(f[i]) for i in range(len(f))), Q(0))

checks = {'finite_maximal_inequalities':0,'finite_tower_identities':0,
          'density_parameter_checks':0,'finite_weighted_interchanges':0}
weights = [Q(1),Q(2),Q(3),Q(4)]
for values in product(range(-2,3), repeat=4):
    f=list(map(Q,values))
    e=[expectation(f,weights,p) for p in PARTITIONS]
    for i in range(3):
        for j in range(i,3):
            assert expectation(e[j],weights,PARTITIONS[i])==e[i]
            checks['finite_tower_identities']+=1
    for level in [Q(1,2),Q(1),Q(3,2),Q(2),Q(3)]:
        bad=[i for i in range(4) if max(abs(row[i]) for row in e)>level]
        assert level*sum((weights[i] for i in bad),Q(0))<=norm(f,weights)
        checks['finite_maximal_inequalities']+=1

uniform=[Q(1,4)]*4
for numerator in range(15):
    y=Q(numerator,14)
    f=[y+Q(k) for k in [0,2,4,6]]
    actual=[expectation(f,uniform,p) for p in PARTITIONS]
    expected=[[y+3]*4,[y+1,y+1,y+5,y+5],f]
    assert actual==expected
    assert [norm([a-b for a,b in zip(row,f)],uniform) for row in actual]==[Q(2),Q(1),Q(0)]
    assert sum((uniform[i]*f[i] for i in range(4)),Q(0))==y+3
    checks['density_parameter_checks']+=1

# Include zero measures and infinite positive entries explicitly.
def positive_product(a,b):
    if a==0 or b==0:return Q(0)
    if a==float('inf') or b==float('inf'):return float('inf')
    return a*b

for wy in [[Q(1),Q(2)],[Q(0),Q(2)],[Q(0),Q(0)]]:
    for wz in [[Q(1),Q(1,2)],[Q(0),Q(1,2)],[Q(0),Q(0)]]:
        for f in [[[Q(2),Q(0)],[Q(1),Q(4)]],
                  [[float('inf'),Q(0)],[Q(1),Q(4)]]]:
            row=sum((positive_product(wy[i],sum((positive_product(wz[j],f[i][j]) for j in range(2)),Q(0))) for i in range(2)),Q(0))
            col=sum((positive_product(wz[j],sum((positive_product(wy[i],f[i][j]) for i in range(2)),Q(0))) for j in range(2)),Q(0))
            assert row==col
            checks['finite_weighted_interchanges']+=1

plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.hashsalt':'finite-kernel-K3-K4-20261006'})
y=Q(1,2);f=[y+Q(k) for k in [0,2,4,6]]
fig,axes=plt.subplots(1,3,figsize=(13.2,5.2),sharey=True)
formulas=['D₀ = y + 3','D₁ = y + (1, 1, 5, 5)','D₂ = fᵧ = y + (0, 2, 4, 6)']
for n,(ax,p) in enumerate(zip(axes,PARTITIONS)):
    d=expectation(f,uniform,p)
    x=np.arange(4)
    ax.bar(x,[float(v) for v in d],width=.76,color='#397db3',alpha=.72,label='partition density Dₙ')
    ax.plot(x,[float(v) for v in f],color='#b44338',marker='o',linewidth=1.8,label='cell values of fᵧ')
    for i,v in enumerate(d):
        ax.text(i,float(v)+.13,str(v),ha='center',fontsize=10,color='#164365')
    ax.set_xticks(x,['cell 1','cell 2','cell 3','cell 4'])
    ax.set_ylim(0,8.1);ax.grid(axis='y',alpha=.18)
    ax.set_title(['One cell','Two cells','Four cells'][n])
    ax.set_xlabel(formulas[n]+'\nL¹ error = '+str([2,1,0][n]),labelpad=12)
axes[0].set_ylabel('Density relative to Lebesgue measure')
axes[0].legend(loc='upper left',fontsize=9)
fig.suptitle('K.3: measurable finite-partition averages — plotted parameter y = 1/2',fontsize=14)
fig.text(.5,.025,'Each original cell has mass 1/4. Formulas hold for every y ∈ [0, 1]; integral mass = y + 3.',ha='center',fontsize=11)
fig.subplots_adjust(left=.07,right=.99,bottom=.23,top=.83,wspace=.12)
for ext in ['png','svg']:
    fig.savefig(OUT/('density-refinement.'+ext),dpi=160,metadata={'Date':None} if ext=='svg' else None)
plt.close(fig)

fig,ax=plt.subplots(figsize=(10.5,5.9))
ax.axis('off')
table=ax.table(cellText=[['y₀: weight 1','2 × 1 × 1 = 2','0 × 1 × 1/2 = 0','2'],
                        ['y₁: weight 2','1 × 2 × 1 = 2','4 × 2 × 1/2 = 4','6'],
                        ['column totals','4','4','8']],
               colLabels=['Y fibre','z₀: weight 1','z₁: weight 1/2','row totals'],
               colWidths=[.22,.29,.31,.18],
               cellLoc='center',bbox=[.025,.25,.95,.5])
table.auto_set_font_size(False);table.set_fontsize(12)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor('#577089')
    cell.set_facecolor('#e9f2fa' if r==0 or c==0 else '#f8fafc')
ax.set_title('K.4: weighted nonnegative integration has the same total',fontsize=14,pad=18)
ax.text(.55,.16,'Row route: 1 · 2 + 2 · 3 = 8     |     Column route: 1 · 4 + (1/2) · 8 = 8',ha='center',transform=ax.transAxes,fontsize=12)
ax.text(.55,.075,'F has rows (2, 0), (1, 4). Interior cells show F × Y-weight × Z-weight.\nFinite illustration; the positive s-finite theorem also allows an infinite answer.',ha='center',transform=ax.transAxes,fontsize=11)
fig.subplots_adjust(left=.09,right=.98,bottom=.05,top=.90)
for ext in ['png','svg']:
    fig.savefig(OUT/('positive-interchange.'+ext),dpi=160,metadata={'Date':None} if ext=='svg' else None)
plt.close(fig)
bind=lambda p:{'path':p.relative_to(HERE).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper(),'bytes':p.stat().st_size}
report={'schema':'finite-kernel-exact-example-and-figure-checks/v1','pass':True,
        'checks':checks,'total':sum(checks.values()),'figures':[bind(p) for p in sorted(OUT.iterdir())],
        'exact_data':'Fractions for all finite examples; extended nonnegative checks use explicit 0 times infinity = 0.',
        'scope':'Finite illustrations and checks of consequences; complete general arguments remain in READING.md.',
        'figure_original_expression':'CC0-1.0','actual_owner_image_inspection':False}
(HERE/'EXACT-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pass':True,'checks':checks,'total':report['total'],'figures':len(report['figures'])}))

assert _actual_font_loads, 'No actual glyph load was instrumented'
_fonts = {r['file']:r for r in _actual_font_loads}
(HERE/'FONT-LOAD-CHECKS.json').write_text(json.dumps({'schema':'actual-bound-local-glyph-font-loads/v1','pass':True,'actual_font_load_calls':len(_actual_font_loads),'loaded_fonts':list(_fonts.values()),'all_loads_from_bound_local_fonts':True},indent=2)+'\n',encoding='utf-8')

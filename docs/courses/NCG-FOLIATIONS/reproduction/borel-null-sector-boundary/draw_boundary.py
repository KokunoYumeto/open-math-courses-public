"""Figures 5.21–5.22: independently written CC0 categorical schematics.
Run with the two exact unmodified bundled DejaVu fonts and full notices.
"""
from pathlib import Path
import os,hashlib,json,platform,importlib.metadata as im
SOURCE_DIR=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(SOURCE_DIR/'runtime-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
from matplotlib.font_manager import FontProperties
from matplotlib import font_manager
from PIL import Image
import xml.etree.ElementTree as ET
HERE=SOURCE_DIR.parent.parent/'figures'
HERE.mkdir(parents=True,exist_ok=True)
FONT_DIR=SOURCE_DIR/'fonts'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
regular=FONT_DIR/'DejaVuSans.ttf'
bold=FONT_DIR/'DejaVuSans-Bold.ttf'
font_notice=SOURCE_DIR/'FONT-NOTICE.txt'
assert sha(regular)=='3FDF69CABF06049EA70A00B5919340E2CE1E6D02B0CC3C4B44FB6801BD1E0D22'
assert sha(bold)=='B184B89E3C1075F22F6B71575B6FC20D4972B3CFD3B23322CA6FD596DCAEF167'
assert sha(font_notice)=='D75938DEC098F06F0AC3C00853065D94F020BE1C3C62EF1DC2975BA15B4D9B0E'
font_manager.fontManager.ttflist[:]=[f for f in font_manager.fontManager.ttflist if f.name!='DejaVu Sans']
for p in [regular,bold]:font_manager.fontManager.addfont(str(p))
actual_fonts=set()
original_get_font=font_manager._get_font
def checked_get_font(paths,*args,**kwargs):
    for item in ([paths] if isinstance(paths,(str,Path)) else paths):
        p=Path(item).resolve()
        assert p.parent==FONT_DIR.resolve(),('unbundled actual font',str(p))
        actual_fonts.add(p.name)
    return original_get_font(paths,*args,**kwargs)
font_manager._get_font=checked_get_font
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'borel-boundary-20261005','savefig.facecolor':'white'})
GREEN='#11624f';RED='#9a343b';INK='#203546';GREY='#62747d'
font=FontProperties(fname=str(regular));bfont=FontProperties(fname=str(bold))
def text(ax,x,y,s,size=12,color=INK,boldface=False,ha='left',va='center'):
    return ax.text(x,y,s,fontproperties=bfont if boldface else font,fontsize=size,color=color,ha=ha,va=va,linespacing=1.4)
def box(ax,x,y,w,h,fc,ec=INK):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.018,rounding_size=0.02',linewidth=1.2,facecolor=fc,edgecolor=ec))
def arrow(ax,a,b,color=GREEN,style='-'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,color=color,linewidth=1.8,linestyle=style))
def save(fig,name,desc):
    png=HERE/(name+'.png');svg=HERE/(name+'.svg')
    fig.savefig(png,dpi=180,metadata={'Description':desc,'Software':'Original BP generator with Matplotlib '+matplotlib.__version__})
    fig.savefig(svg,metadata={'Date':'2026-10-05','Title':name,'Description':desc+'\n\nComplete installed DejaVu notice:\n'+font_notice.read_text(encoding='utf-8')})
    plt.close(fig)
    root=ET.parse(svg).getroot();ids=[n.attrib.get('id','') for n in root.iter()]
    glyphs=[v for v in ids if 'Sans-' in v]
    assert glyphs and all(v.startswith(('DejaVuSans-','DejaVuSans-Bold-')) for v in glyphs)
    assert font_notice.read_text(encoding='utf-8') in svg.read_text(encoding='utf-8')
    with Image.open(png) as pic:shape=list(pic.size)
    return {'name':name,'png':{'path':png.name,'sha256':sha(png),'bytes':png.stat().st_size,'pixels':shape},'svg':{'path':svg.name,'sha256':sha(svg),'bytes':svg.stat().st_size,'glyph_ids':sorted(set(glyphs))},'caption':desc,'mathematical_status':'Exact categorical/measure-domain schematic; no nonsmooth quotient is parametrized or geometrically approximated.'}

fig,ax=plt.subplots(figsize=(13.5,6.5));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');fig.subplots_adjust(left=.035,right=.97,top=.97,bottom=.04)
text(ax,.0,.94,'Deleting an invariant null sector preserves the whole image and composition',18,boldface=True)
for x,label in [(.025,'Source Q'),(.43,'Middle Q′')]:
    box(ax,x,.26,.265,.49,'#f7fafb')
    text(ax,x+.1325,.71,label,15,boldface=True,ha='center')
    box(ax,x+.018,.49,.23,.12,'#e0f4ec',GREEN)
    text(ax,x+.13,.55,'Good circle: λ, mass 1',11,color=GREEN,ha='center')
    box(ax,x+.018,.315,.23,.12,'#f8e9ea',RED)
    text(ax,x+.13,.375,'Irrational leaf sector: mass 0',10.4,color=RED,ha='center')
box(ax,.82,.42,.15,.23,'#e0f4ec',GREEN)
text(ax,.895,.565,'Point {*}',14,boldface=True,ha='center')
text(ax,.895,.48,'mass 1',13,color=GREEN,ha='center')
arrow(ax,(.29,.55),(.43,.55));text(ax,.36,.64,'u: identity',11,color=GREEN,ha='center')
arrow(ax,(.29,.375),(.43,.375),RED,'--');text(ax,.36,.28,'u: fixed bad leaf',10,color=RED,ha='center')
arrow(ax,(.695,.55),(.82,.55));text(ax,.757,.69,'v: collapse',11,color=GREEN,ha='center')
arrow(ax,(.695,.375),(.82,.45),RED,'--');text(ax,.76,.29,'null bad sector',10,color=RED,ha='center')
text(ax,.49,.19,'Both global maps are nonproper; their good-sector restrictions are proper.',12,ha='center')
text(ax,.49,.12,'Composite pushforward = successive pushforwards: every finite m-label presentation has value m;',11.5,ha='center')
text(ax,.49,.065,'the empty presentation has value 0; every infinite countable presentation has value ∞.',11.5,ha='center')
caption1='Figure 5.21. Exact schematic of Sections 5.21.4 and 5.21.6, equations BP.9–BP.10 and BP.13. Green blocks are full conull circle leaf sectors with equality transversal relation and normalized Lebesgue measure; red blocks are full irrational suspension leaf sectors assigned zero measure. u is identity on the good circles and constant to one fixed bad leaf on the bad sector; v is constant to a point. Both global weak Borel maps are nonproper. Their essentially proper images agree on every presentation and compose to point mass one. Rectangles depict specified sectors, not charts or a Borel model of an irrational quotient. Human context: Connes 1982 Section 2 p9; Connes 1979 III.3.7 and III.3.10–11.'
items=[save(fig,'borel-null-sector-composition',caption1)]

fig,ax=plt.subplots(figsize=(12.5,6.2));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');fig.subplots_adjust(left=.04,right=.97,top=.97,bottom=.045)
text(ax,.01,.945,'The finite Radon boundary: any positive irrational-sector mass excludes collapse',16,boldface=True)
box(ax,.035,.41,.40,.39,'#f7fafb')
text(ax,.235,.74,'ε = 0',18,boldface=True,ha='center')
text(ax,.235,.65,'μ₀ = λgood ⊕ 0',17,ha='center')
text(ax,.235,.55,'Allowed on the conull good sector',13,color=GREEN,ha='center')
text(ax,.235,.465,'Point image: mass 1',13,color=GREEN,ha='center')
box(ax,.55,.41,.40,.39,'#f8e9ea',RED)
text(ax,.75,.74,'Every ε > 0',18,boldface=True,color=RED,ha='center')
text(ax,.75,.65,'με = λgood ⊕ ε λirrational',16,ha='center')
text(ax,.75,.55,'Excluded: finite invariant aperiodic sector',11.8,color=RED,ha='center')
text(ax,.75,.465,'No conull normalized collapse cutoff',12,color=RED,ha='center')
arrow(ax,(.445,.60),(.54,.60),GREY);text(ax,.493,.345,'Total variation norm ‖με − μ₀‖ = ε',16,ha='center')
text(ax,.493,.245,'Mass transport on a hypothetical aperiodic conull domain M:',13,ha='center')
text(ax,.493,.17,'0 < μ(M) = ∫ Σ[a′ E a] c(a′) dμ(a) = ∫ Σ[a′ E a] c(a) dμ(a) = ∞',15,ha='center')
text(ax,.493,.08,'Admissibility boundary only: no output is asserted for ε > 0; the historical map interface remains open.',11.7,ha='center')
caption2='Figure 5.22. Exact measure-domain boundary of Section 5.21.6, BP.12 and Exercise 19. The same compact disjoint union of two foliated tori carries μ₀=λgood⊕0 or με=λgood⊕ελirrational; all these source transverse measures are finite Radon. Total variation norm of their positive difference is exactly ε. At ε=0 collapse is essentially presentation Borel and its point image has mass one. At every ε>0 the positive finite invariant aperiodic component prevents any conull normalized cutoff by Theorem 5.24. This is a categorical admissibility boundary, not a numeric output plot or an obstruction to all imaginable finite-Radon output rules. Human context: Connes 1982 Section 2 p9; Connes 1979 III.3.7 and III.3.10–11.'
items.append(save(fig,'borel-finite-radon-boundary',caption2))
assert actual_fonts=={'DejaVuSans.ttf','DejaVuSans-Bold.ttf'},actual_fonts
report={'schema':'public-borel-null-sector-figure-bindings/v1','proof_locators':'Sections 5.21.1–5.21.7, Theorems 5.21–5.24, BP.1–BP.13, Exercises 16–19',
        'generator_sha256':sha(Path(__file__)),'python_version':platform.python_version(),
        'runtime_versions':{n:im.version(n) for n in ['matplotlib','numpy','pillow']},
        'actual_fonts':[{'path':'fonts/'+n,'sha256':sha(FONT_DIR/n),'bytes':(FONT_DIR/n).stat().st_size} for n in sorted(actual_fonts)],
        'figures':items,'svg_font_notice_complete':True,'glyph_families_only_dejavu':True,
        'figure_meaning':'Exact categorical schematics; sector boxes are not charts or Borel models of the irrational quotient. The epsilon boundary asserts admissibility only, not undefined numerical outputs.',
        'visual_inspection':'Generation is not inspection; inspect both PNGs and native SVGs separately.'}
(SOURCE_DIR/'figure-bindings.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'generated':[x['name'] for x in items],'actual_font_files':sorted(actual_fonts)}))

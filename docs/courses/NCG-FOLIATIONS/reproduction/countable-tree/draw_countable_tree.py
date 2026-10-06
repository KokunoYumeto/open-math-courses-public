"""Exact infinite-valence proper-weight schematic CT.5; original CC0 1.0."""
from pathlib import Path
import json
import html
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

SOURCE_DIR = Path(__file__).resolve().parent
OUT = SOURCE_DIR.parent.parent / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = SOURCE_DIR / 'fonts'
font_names = {'DejaVu Sans','DejaVu Sans Display','DejaVu Sans Mono','STIXGeneral','STIXNonUnicode','STIXSizeOneSym','STIXSizeTwoSym','STIXSizeThreeSym','STIXSizeFourSym','STIXSizeFiveSym'}
font_manager.fontManager.ttflist[:] = [f for f in font_manager.fontManager.ttflist if f.name not in font_names]
for font_path in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(font_path))
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'dejavusans'})
font_notices = '\n\n'.join((FONT_DIR/n).read_text(encoding='utf-8') for n in ['LICENSE_DEJAVU.txt','LICENSE_STIX.txt'])
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
                     "svg.hashsalt":"countable-tree-proper-weight-20261005"})
fig,axes=plt.subplots(1,3,figsize=(14,5.7),layout="constrained",facecolor="#f7f8fb")
at,ar,ac=axes
at.axis("off")
at.set_title("Infinitely many leaves at each base vertex",fontsize=11,loc="left")
at.set_xlim(-.8,2.3); at.set_ylim(-.85,1.35)
base=[(0,1),(1.5,1)]
at.plot([0,1.5],[1,1],color="#718197",lw=1.3)
at.scatter(.75,1,s=40,marker="s",color="#d8954e")
at.annotate("",xy=(.75,1),xytext=(1.13,1),
            arrowprops={"arrowstyle":"->","color":"#247955","lw":1.1})
for g,(x,y) in enumerate(base):
    at.scatter(x,y,s=80,color="#b64069" if g==0 else "#336da5",zorder=3)
    at.text(x,y+.13,"o = 1, w = 0" if g==0 else "a, w = 1",ha="center",fontsize=10)
    for j in range(1,4):
        xy=(x+(j-2)*.5,.1)
        at.plot([x,xy[0]],[y,xy[1]],color="#718197",lw=1.1)
        mid=((x+xy[0])/2,(y+xy[1])/2)
        at.scatter(*mid,s=30,marker="s",color="#d8954e",zorder=2)
        at.annotate("",xy=mid,xytext=((3*xy[0]+x)/4,(3*xy[1]+y)/4),
                    arrowprops={"arrowstyle":"->","color":"#247955","lw":1.1})
        at.scatter(*xy,s=45,color="#336da5",zorder=3)
        at.text(xy[0],xy[1]-.13,f"j={j}\nw={g+j}",ha="center",va="top",fontsize=9)
    at.text(x,-.38,"⋯  all j ≥ 1",ha="center",fontsize=11)
at.text(.7,-.65,"Q pairs every attached leaf with its edge.\nOnly the base root is unmatched.",
        ha="center",fontsize=9,linespacing=1.6)

j=np.arange(1,10)
ar.plot(j,.5*np.ones_like(j),"s--",color="#bb4068",label="graph distance: w = 1")
ar.plot(j,1/(1+j*j),"o-",color="#346ba4",label="proper weight: w = j")
ar.set_title("Exact resolvent values on root-attached blocks",fontsize=11,loc="left")
ar.set_xlabel("Attached leaf label j")
ar.set_ylabel(r"Square resolvent norm $1/(1+w^2)$")
ar.set_ylim(-.02,.64)
ar.set_yticks(np.arange(0,.61,.1))
ar.grid(alpha=.2)
ar.legend(fontsize=8,frameon=False,loc="upper right")
ar.text(.16,.47,"Distance leaves infinitely many equal blocks.\n"
        "Proper weights make their tail norms tend to zero.",
        transform=ar.transAxes,fontsize=8,linespacing=1.6)

ac.axis("off")
ac.set_title("Every proper-weight window is finite",fontsize=11,loc="left")
ac.text(.02,.87,r"$w(g)=|g|,\qquad w(g,j)=|g|+j$",fontsize=13)
ac.text(.02,.71,r"$\#\{w\leq R\}=B(R)+\sum_{j=1}^{R}B(R-j)$",fontsize=12)
ac.text(.02,.57,"R            0      1      2       3       4\n"
        "vertices   1      6     23     76    237",fontsize=11,fontfamily="DejaVu Sans Mono",linespacing=1.8)
ac.text(.02,.36,"For each return h the parent mismatch lies on\n"
        "the finite base segment [o, ho]. All added leaf\n"
        "pairs transport exactly, with bounded weight change.",
        fontsize=10,linespacing=1.8)
ac.text(.02,.10,r"$\mathrm{Index}\,Q=+1$"+"\nNormal inverse, central phase and Bott pairing stay intact.",
        fontsize=10,linespacing=1.8,color="#2f6b50")
fig.suptitle("A proper tree weight controls countably infinite valence",fontsize=16,x=.025,ha="left")
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
hidden={id(t) for a in axes if not a.axison for t in a.get_xticklabels()+a.get_yticklabels()}
checked=0; outside=[]
for t in fig.findobj(match=matplotlib.text.Text):
    if not t.get_visible() or not t.get_text() or id(t) in hidden: continue
    checked+=1
    b=t.get_window_extent(renderer)
    if b.x0 < -1 or b.y0 < -1 or b.x1 > fig.bbox.x1+1 or b.y1 > fig.bbox.y1+1:
        outside.append(t.get_text())
fig.savefig(OUT/"kt-countable-tree-proper-weight.png",dpi=150,metadata={"Software":"Original programme diagram; CC0 1.0"})
fig.savefig(OUT/"kt-countable-tree-proper-weight.svg",metadata={"Date":None,"Creator":"Original programme diagram; CC0 1.0"})
(SOURCE_DIR/"COUNTABLE-FIGURE-BOUNDS.json").write_text(json.dumps({"checked_texts":checked,"outside_figure":outside,"mathematical_scope":"Exact attached-leaf infinite-valence schematic, exact resolvent formula and finite weight-window counts; finite displayed labels do not prove infinite tail"},indent=2)+"\n",encoding="utf-8")
assert not outside,outside

# Exact actual glyph licences accompany the outlined SVG.
svg_path = OUT / 'kt-countable-tree-proper-weight.svg'
svg_text = svg_path.read_text(encoding='utf-8')
svg_text = svg_text.replace('</metadata>', '</metadata>\n <desc id="font-notices">'+html.escape(font_notices)+'</desc>', 1)
svg_path.write_text(svg_text, encoding='utf-8', newline='\n')
plt.close(fig)

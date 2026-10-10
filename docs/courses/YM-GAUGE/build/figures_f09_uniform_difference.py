from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parent.parent/'figures'
ROOT.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-F09-uniform_difference'
fig,ax=plt.subplots(figsize=(13.5,8.2))
fig.patch.set_facecolor("#f4f6f8");ax.set_facecolor("#f4f6f8")
ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
def box(x,y,w,h,title,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
                  facecolor=color,edgecolor="#32485c",linewidth=1.2))
    ax.text(x+w/2,y+h-.035,title,ha="center",va="top",fontsize=12,fontweight="bold",color="#152b40")
    ax.text(x+w/2,y+h-.085,text,ha="center",va="top",fontsize=10.5,color="#152b40",linespacing=1.4)
def arrow(start,end,label):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=14,color="#35566f",linewidth=1.6))
    ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+.017,label,ha="center",fontsize=9,color="#35566f",bbox={'facecolor':'#f4f6f8','edgecolor':'none','pad':2})
ax.text(.5,.98,"Original c, S, physical interval and gauge anchors retained",
        ha="center",va="top",fontsize=17,fontweight="bold",color="#152b40")
box(.025,.68,.275,.21,"Physical-curve differences",
    "FI heat map with original anchor\nUD.4a restores the physical gauge\nEvery coefficient comes from FC/HT", "#d9e8f4")
box(.365,.68,.27,.21,"Temporal tension V = δFₛₜ",
    "L¹ start → L² gain → derivatives\nDegree one in actual differences\nUD.11–UD.19", "#d8eee4")
box(.705,.68,.27,.21,"Electric heat receiver",
    "Both p = 2 and p = ∞\nActual differences retained\nUD.21–UD.22", "#d8eee4")
arrow((.305,.77),(.355,.77),"")
arrow((.64,.77),(.695,.77),"")
box(.025,.32,.275,.22,"Spatial tension z = δw",
    "Original zero heat datum\nLz, Bz and integrated δQ\nUD.24–UD.27", "#d9e8f4")
box(.365,.32,.27,.22,"Signed heat cancellation",
    "Pcf [z(S) − z(0) − ∫ δNw]\nAll temporal products integrable\nUD.25–UD.30", "#d8eee4")
box(.705,.32,.27,.22,"Boundary time increments",
    "∇δb in L²x and δb in L³x\nGain √|J|; retain value at tj\nUD.31", "#d8eee4")
arrow((.305,.42),(.355,.42),"")
arrow((.64,.42),(.695,.42),"")
arrow((.505,.675),(.505,.553),"TD products")
box(.14,.055,.72,.155,"Complete initial-data composition remains",
    "Both PD null placements: UD.35.  Direct PD/FI composition retains jρ ρ: UD.33–34.\nThe electric bound vanishes with its inputs. Initial-data stability still requires the full paired system.",
    "#f5e8cc")
arrow((.83,.31),(.73,.225),"")
ax.text(.025,.008,"Figure UD-A • proved receiving maps, not sampled Yang–Mills solutions • source: this script",
        ha="left",fontsize=9,color="#526777")
fig.savefig(ROOT/"f09-uniform-difference.png",dpi=180,bbox_inches="tight")
fig.savefig(ROOT/"f09-uniform-difference.svg",bbox_inches="tight",metadata={'Date':None})


def build():
    return None

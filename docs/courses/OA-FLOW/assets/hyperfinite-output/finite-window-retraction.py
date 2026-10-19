"""Draw the exact seven-coordinate compression for a degree-two Fourier word.

Run this file to regenerate the SVG and exact JSON beside it.
Pass --preview PATH to also write a PNG for visual inspection.
The drawing uses installed DejaVu Sans; no font file is distributed.
Original exposition and drawing code: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import argparse,json
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch

def main():
 parser=argparse.ArgumentParser();parser.add_argument("--preview",type=Path);args=parser.parse_args()
 root=Path(__file__).resolve().parent
 n,r=3,2;indices=list(range(-n,n+1));N=len(indices)
 pairs=[(s,t)for s in indices for t in indices if s-t==r]
 assert pairs==[(-1,-3),(0,-2),(1,-1),(2,0),(3,1)]
 q=Fraction(len(pairs),N);assert q==Fraction(5,7)
 data={"n":n,"F_n":indices,"matrix_indices":"row s, column t","degree":r,"surviving_pairs":pairs,"entry_weight":{"numerator":1,"denominator":N},"multiplier":{"numerator":q.numerator,"denominator":q.denominator},"coefficient_formula":"q_n(r)=max(1-|r|/(2n+1),0)","proof_locators":["HAFR2","HAFR3","HAFR5","HAFR6"],"scope":"One exact finite Fourier coefficient; whole-algebra convergence is proved in the lesson."}
 (root/"finite-window-retraction.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none","svg.hashsalt":"oa-flow-finite-window-retraction-v1"})
 fig,ax=plt.subplots(figsize=(12,6.6),dpi=150);fig.patch.set_facecolor("#f7f9fc");ax.set_facecolor("#f7f9fc")
 ax.set_xlim(0,1000);ax.set_ylim(0,550);ax.axis("off")
 blue="#173b57";red="#b84732";muted="#41596c"
 def text(x,y,s,size=14,**kw):ax.text(x,y,s,fontsize=size,color=blue,va="center",**kw)
 text(40,520,"A finite window keeps five of the seven degree-two entries",20,fontweight="bold")
 text(60,477,"Rows s and columns t in F₃ = {−3,…,3}",13)
 cell=37;x0=75;y0=425
 for j,t in enumerate(indices):text(x0+(j+.5)*cell,y0+17,str(t),12,ha="center")
 text(45,y0+17,"s \\ t",11,ha="center")
 for i,s in enumerate(indices):
  cy=y0-(i+1)*cell;text(48,cy+cell/2,str(s),12,ha="center")
  for j,t in enumerate(indices):
   cx=x0+j*cell;active=(s,t)in pairs
   ax.add_patch(Rectangle((cx,cy),cell,cell,facecolor="#fbe5df"if active else"#ffffff",edgecolor="#afbcc8",linewidth=.8))
   if active:ax.text(cx+cell/2,cy+cell/2,"1/7",fontsize=11,ha="center",va="center",color=red)
 text(75,132,"Marked entries satisfy s − t = 2.",13)
 text(75,105,"Five contributions of weight 1/7 give 5/7.",13,fontweight="bold")
 def box(x,y,w,h,title):
  ax.add_patch(Rectangle((x,y),w,h,facecolor="#e8f0f8",edgecolor="#6d8ca5",linewidth=1.3));text(x+w/2,y+h/2,title,18,ha="center")
 box(430,355,130,75,"B(H)");box(695,355,210,75,"M₇(D)");box(695,205,210,75,"A = D ⋊ Z")
 ax.add_patch(FancyArrowPatch((570,392),(685,392),arrowstyle="-|>",mutation_scale=15,color=blue,linewidth=1.7))
 text(627,420,"C₃",17,ha="center");text(627,365,"entrywise P",12,ha="center")
 ax.add_patch(FancyArrowPatch((800,345),(800,290),arrowstyle="-|>",mutation_scale=15,color=blue,linewidth=1.7))
 text(840,319,"Γ₃",17)
 text(440,323,"Γ₃ uses the row [u^s] / √7.",14)
 text(440,158,"R₃(π(f)u²) = (5/7) π(f)u²",17,fontweight="bold")
 text(440,125,"Rₙ preserves τ on all of A.",15)
 text(440,97,"A cluster retraction fixes every X in A.",13)
 ax.plot([40,960],[65,65],color="#bcc8d2",linewidth=1)
 text(40,39,"Finite formula: qₙ(r) = max(1 − |r|/(2n+1), 0).  Whole-algebra convergence: HAFR5–HAFR6.",12)
 fig.subplots_adjust(left=.01,right=.99,bottom=.01,top=.99)
 fig.savefig(root/"finite-window-retraction.svg",metadata={"Date":None,"Creator":"Original OA-FLOW finite-window retraction diagram"},facecolor=fig.get_facecolor())
 if args.preview:fig.savefig(args.preview,facecolor=fig.get_facecolor())
 plt.close(fig)
if __name__=="__main__":main()


"""Render exact cone-support geometry; plotted sets are bounds, not solution values."""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
STEM="constant-strength-causal-support-024"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
    "svg.fonttype":"none","svg.hashsalt":"AN02-SC-support-024",
    "axes.titleweight":"bold","axes.spines.top":False,"axes.spines.right":False})
fig,(left,right)=plt.subplots(1,2,figsize=(20,10),dpi=120)
fig.subplots_adjust(left=.065,right=.965,bottom=.15,top=.77,wspace=.27)
fig.suptitle("A local inverse can retain the frozen causal support",fontsize=27,x=.5,y=.965,weight="bold")
fig.text(.5,.913,"The wave cone and its sums are exact. Shading shows a support bound, not a nonzero solution.",ha="center",fontsize=17)
z=np.linspace(-1.6,1.6,1601)
front=-.3+np.maximum(0,np.abs(z)-.2)
left.fill_between(z,front,1.65,color="#dfedf8",label="C + S: upper bound on support")
left.plot(z,front,color="#135d85",lw=2.8)
left.add_patch(Rectangle((-.2,-.3),.4,.2,facecolor="#f4bc74",edgecolor="#93591d",lw=2.2,zorder=5))
left.add_patch(Circle((0,0),1,fill=False,ls=(0,(5,4)),lw=1.7,color="#5f6470",zorder=4))
left.text(-1.41,-.82,"X: the chosen local ball\n(normalized radius 1)",fontsize=14,color="#444b56",
    bbox={"facecolor":"white","edgecolor":"none","alpha":.95},zorder=10)
left.annotate("S: |z/r| <= 1/5\n-3/10 <= t/r <= -1/10",xy=(-.16,-.23),xytext=(-1.49,.31),
    arrowprops={"arrowstyle":"-","color":"#93591d"},fontsize=14,color="#704016",
    bbox={"facecolor":"white","edgecolor":"none","alpha":.95},zorder=10)
left.text(-1.46,1.40,"C = {t >= |z|}",fontsize=16,color="#135d85")
left.text(-1.46,1.12,"C + S:  t/r >= -3/10\n                 + max(0, |z/r| - 1/5)",fontsize=14,color="#135d85")
points=np.array([[0,-.2],[-.35,.25],[0,.65]])
for a,b in zip(points[:-1],points[1:]):
    left.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"-|>","lw":2.8,"color":"#196d48"},zorder=7)
left.scatter(points[:,0],points[:,1],color="#196d48",s=38,zorder=8)
left.text(.48,1.05,"two allowed\nforward shifts",fontsize=14,color="#196d48")
left.text(.46,-.58,"Outside the blue set, Ef = 0.\nInside it, no nonvanishing is claimed.",fontsize=14,
    bbox={"facecolor":"white","edgecolor":"#c9d3df","boxstyle":"round,pad=.6"},zorder=10)
left.set(xlim=(-1.6,1.6),ylim=(-1.08,1.65),xlabel="z / r",ylabel="t / r")
left.set_aspect("equal",adjustable="box")
left.set_title("Input support plus the forward cone",pad=18,fontsize=18)
left.grid(alpha=.16)

zz=np.linspace(-1.15,1.15,801)
right.fill_between(zz,np.abs(zz),1.17,where=np.abs(zz)<=1.17,color="#eef2f4")
right.plot(zz,np.abs(zz),color="#929ca4",lw=1.5)
d1=np.array([-.35,.45]);d2=np.array([.35,.4]);total=d1+d2
def arrow(start,end,color,style="-|>"):
    right.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":style,"lw":3.0,"color":color},zorder=7)
arrow([0,0],d1,"#216b9a")
arrow(d1,total,"#bb6e25")
arrow([0,0],total,"#23764f")
right.scatter([0,d1[0],total[0]],[0,d1[1],total[1]],s=42,color="#33414c",zorder=8)
right.text(-.75,1.02,"C",fontsize=27,color="#71808b")
right.text(-.09,.015,"0",fontsize=13,color="#33414c")
right.text(-.99,.26,"d1 = (-7/20, 9/20)",fontsize=14,color="#216b9a",rotation=0,
    bbox={"facecolor":"white","edgecolor":"none","alpha":.9})
right.text(.35,.60,"d2 = (7/20, 2/5)",fontsize=14,color="#a35919",
    bbox={"facecolor":"white","edgecolor":"none","alpha":.95},zorder=10)
right.text(.15,.98,"d1 + d2 = (0, 17/20)\nis still in C",fontsize=14,color="#23764f")
right.text(-.96,-.26,"SC13: every K term adds a displacement in C.\nSC14: C + C = C, and the distributional\nlimit retains the closed support bound.",fontsize=14,
    bbox={"facecolor":"white","edgecolor":"#c9d3df","boxstyle":"round,pad=.65"})
right.set(xlim=(-1.08,1.12),ylim=(-.35,1.18),xlabel="displacement in z / r",ylabel="displacement in t / r")
right.set_aspect("equal",adjustable="box")
right.set_title("Adding causal displacements stays causal",pad=18,fontsize=18)
right.grid(alpha=.16)
fig.text(.5,.068,"Proof: SC13-SC14. Rectangle bound: SC19.  The radius r is the validated small radius from SC8, not a universal numeric radius.",
    ha="center",fontsize=14,color="#354555")
fig.savefig(OUT/(STEM+".png"),dpi=120,metadata={"Software":"AN02 original reproducible mathematical figure"})
fig.savefig(OUT/(STEM+".svg"),metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI)",
    "Title":"Constant-strength inverse causal support inclusion"})
plt.close(fig)
geometry={"schema":"exact-constant-strength-support-geometry/v1",
    "coordinates":"z/r,t/r; r is the chosen positive contraction radius",
    "input_rectangle":{"z":[-.2,.2],"t":[-.3,-.1]},
    "cone":"t>=abs(z)","closed_sum_front":"t=-3/10+max(0,abs(z)-1/5)",
    "displacements":[[-7/20,9/20],[7/20,2/5]],"sum":[0,17/20],
    "cone_margins":[float(d1[1]-abs(d1[0])),float(d2[1]-abs(d2[0])),float(total[1]-abs(total[0]))],
    "support_inclusion_not_equality":True,"plotted_solution_values":False,"proof_locators":["SC13","SC14","SC19"],
    "editable_SVG_text":True,"external_assets":False}
(OUT/(STEM+".json")).write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"png":str(OUT/(STEM+".png")),"svg":str(OUT/(STEM+".svg")),"geometry":geometry}))

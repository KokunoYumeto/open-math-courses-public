from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-classify-finite-orbit-class-towers'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.1,15.5),dpi=160)
fig.subplots_adjust(left=.035,right=.985,bottom=.015,top=.99)
ax.set_xlim(0,10);ax.set_ylim(0,26);ax.axis('off')
ink='#183b53';blue='#246d97';red='#a74b43'
def text(y,t,size=20,color=ink):ax.text(.5,y,t,fontsize=size,color=color,va='top')
def box(y,h,label):
 ax.add_patch(FancyBboxPatch((.2,y),9.5,h,boxstyle='round,pad=.12',linewidth=1.2,edgecolor=blue,facecolor='#eef5f9'))
 text(y+h-.35,label,23)
text(25.6,'Finite orbit classes\nand tower boundaries',25)
text(24.0,r'$Q=\mathbb{Z}/100\mathbb{Z},\quad \mu(\{x\})=1/100$',18)
box(17.6,5.45,'Three classes on the orbit')
classes=[(0,4),(4,48),(52,48)]
for j,(root,length) in enumerate(classes):
 y=21.25-j*1.15
 for k in range(length):
  # Equal unit widths; a short class remains visibly short.
  ax.add_patch(Rectangle((.58+k*.166,y),.166,.32,facecolor='#d87f74' if length==4 else '#69a9c5',edgecolor='white',linewidth=.28))
 text(y-.12,f'Root {root}; {length} points',17)
text(17.08,'Within each class, +1 leaves at\nits last point; −1 leaves at its first.',18)
box(10.8,4.9,'Group equal root shapes')
text(14.65,r'$R_4=\{0,\ldots,3\}$',21)
text(13.95,r'$B_{R_4}=\{0\},\quad \mu(B_{R_4})=1/100$',18)
text(13.02,r'$R_{48}=\{0,\ldots,47\}$',21)
text(12.28,r'$B_{R_{48}}=\{4,52\}$',20)
text(11.55,r'$\mu(B_{R_{48}})=2/100$',20)
box(5.65,4.65,'Count edges, then whole classes')
text(9.33,r'$d_{+1}(R)=d_{-1}(R)=1$',21)
text(8.53,r'$\mu(D_{+1})=\mu(D_{-1})=3/100$',19)
text(7.63,r'$\kappa=1/4:\quad R_4\ \mathrm{is\ bad}$',21,red)
text(6.82,r'$1/48<1/4:\quad R_{48}\ \mathrm{is\ good}$',19)
box(.35,4.75,'The actual mass and its bound')
text(4.08,r'$\mu(\mathrm{bad\ classes})=4/100$',21,red)
text(3.40,r'$\kappa^{-1}\sum_{g=\pm1}\mu(D_g)=24/100$',19)
text(2.10,r'$\mu(\mathrm{retained\ towers})=96/100$',19)
text(1.30,'Proposition 6A.1, (6A.6)–(6A.8)\nand Exercise 9.9.',16)
for ext in ['svg','png']:
 fig.savefig(out/('finite-relation-towers.'+ext),metadata={'Date':None} if ext=='svg' else {'Software':'OA-CLASSIFY reproducible mathematical figure'})
plt.close(fig)


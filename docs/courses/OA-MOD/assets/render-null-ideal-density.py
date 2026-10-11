"""Original exact matrix diagram for QW01–05; no sampled operator claims."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'savefig.facecolor':'white'})
INK='#183345';BLUE='#176990';RED='#ad421b';GREEN='#1c6d5d'

def box(fig,xywh,title,lines,color):
 x,y,w,h=xywh
 fig.add_artist(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008',transform=fig.transFigure,facecolor='#f3f7fa',edgecolor=color,lw=1.5))
 fig.text(x+.02,y+h-.035,title,size=17,weight='bold',color=color)
 fig.text(x+.02,y+h-.078,lines,size=15,va='top',color=INK,linespacing=1.3)

def matrix(fig,x,y,entries,color):
 ax=fig.add_axes([x,y,.18,.135]);ax.set_xlim(0,2);ax.set_ylim(0,2);ax.axis('off')
 for i in range(2):
  for j in range(2):
   value=entries[i][j]
   ax.add_patch(plt.Rectangle((j,1-i),1,1,facecolor=color if value else '#edf1f4',edgecolor='white',lw=2))
   ax.text(j+.5,1.5-i,str(value),ha='center',va='center',size=25,color='white' if value else INK)

def render(out):
 out.mkdir(parents=True,exist_ok=True);fig=plt.figure(figsize=(9,11),dpi=100)
 fig.text(.07,.952,'Why finite-domain density matters',size=25,weight='bold',color=INK)
 box(fig,(.07,.725,.86,.18),'QW01–04 · The faithful quotient theorem',
  'C*-algebra; lower-semicontinuous weight; modular condition\n'
  '+ a norm-dense finite domain\n'
  '⇒ closed two-sided null ideal and a faithful quotient;\ncanonical GNS spaces are unitarily equivalent.',GREEN)
 fig.text(.07,.693,r'QW05 · Remove density: $A=M_2(\mathbb{C})$, identity dynamics',size=17,weight='bold',color=RED)
 fig.text(.07,.647,r'$p=E_{11};\quad\omega(a)=0$ for $a=pap\geq0$, and $\omega(a)=\infty$ otherwise.',size=15,color=INK)
 matrix(fig,.17,.425,[[1,0],[0,0]],BLUE)
 matrix(fig,.65,.425,[[0,1],[0,0]],RED)
 fig.text(.26,.579,r'$E_{11}\in Ap$',ha='center',size=18,color=BLUE)
 fig.text(.74,.579,r'$E_{12}\notin Ap$',ha='center',size=18,color=RED)
 fig.text(.50,.514,r'$\times E_{12}$',ha='center',size=18,color=INK)
 fig.text(.50,.470,'→',ha='center',size=32,color=INK)
 fig.text(.26,.384,r'$\omega(E_{11}^*E_{11})=0$',ha='center',size=16,color=BLUE)
 fig.text(.74,.384,r'$\omega(E_{12}^*E_{12})=\infty$',ha='center',size=16,color=RED)
 fig.text(.07,.330,r'Null ideal $Ap$: exactly the matrices with zero second column.',size=16,color=INK)
 fig.text(.07,.298,'It is a left ideal, but right multiplication above leaves it.',size=16,color=INK)
 box(fig,(.07,.085,.86,.15),'Two distinct support reductions',
  r'Finite-domain projection $e=p$; largest null projection $f=p$.'+'\n'
  r'The null complement $1-f=E_{22}$ retains an infinite weight.'+'\n'
  r'The faithful semifinite corner $e-f=0$ loses the infinite-part data.',BLUE)
 fig.text(.07,.027,'Proofs: QW01–05, especially QW.11–13; full normal-weight reconstruction: WS06.\nSource remarks: Takesaki, Theory of Operator Algebras II, VIII.4 (pp.134,137–138). Original figure.',size=10,color=INK)
 fig.savefig(out/'null-ideal-density.png');plt.close(fig)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
 render(parser.parse_args().output_dir)

"""Reproduce the precise additive-layer normalization mechanism and results."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(5,16),dpi=180)
ax.set(xlim=(0,5),ylim=(0,16));ax.axis('off')
ax.text(2.5,15.65,'Further additive families',ha='center',fontsize=21,weight='bold')
ax.text(2.5,15.22,'Residue characteristic two; every finite K/Q₂',ha='center',fontsize=12)
ax.text(2.5,14.88,'Unrestricted e = v(2) ≥ 1 and all allowed higher coefficients',ha='center',fontsize=9.5)
boxes=[
 (13.65,'Actual torsion orders A₄ and A₈\nFull B₄ by distinct valuation classes\nor finite unramified simple-root splitting',
  'D₄ = 2d − 2i₄; explicit bases: AL10, AL29, AL32, AL37', '#edf4ff'),
 (11.55,'Actual point quadratic over each quartic factor\nShifted constant valuation 1; trace ≥ 1\nFull Eisenstein ring; relative different 2 or 4',
  'All shifts and retained errors: 6.0O.2–6; AL17–AL40', '#edf4ff'),
 (9.45,'Trace-dual tower + inertia orbits\nD₈ = 6d − 2i₈\ni₈ − i₄ = d + M + 1 − (ε₈ − ε₄)/2',
  'Both indices and orbit terms computed; AL3, AL28–AL40', '#fff4dc'),
 (7.35,'δ = 2d − i₈ + i₄ − (ε₈ − ε₄)/2\nd = M + 1 + δ = −Art(X/R)',
  'AL2 and the earlier proved Euler identity, Lemma6.0H', '#edf8ef'),
]
for y,body,locator,colour in boxes:
 ax.add_patch(FancyBboxPatch((.27,y-.72),4.46,1.44,boxstyle='round,pad=.10',facecolor=colour,edgecolor='#27445f',linewidth=1.3))
 ax.text(2.5,y+.12,body,ha='center',va='center',fontsize=11.9,linespacing=1.5)
 ax.text(2.5,y-.60,locator,ha='center',fontsize=8.4,color='#37516a')
for top,bottom in [(13.65,11.55),(11.55,9.45),(9.45,7.35)]:
 ax.add_patch(FancyArrowPatch((2.5,top-.88),(2.5,bottom+.88),arrowstyle='-|>',mutation_scale=17,color='#27445f',linewidth=1.4))
ax.text(2.5,6.10,'Precisely the proved preparations',ha='center',fontsize=13,weight='bold')
rows=[
 ['II: v(a₃)=v(a₄)=1','4','1','4','12','2','6','2','4'],
 ['II: v(a₃)=1, v(a₄)≥2','4','1','2','10','3','7','2','4'],
 ['III: v(a₃)=1','4','2','4','10','2','7','1','3'],
 ['III*: v(a₁)=1','10','8','4','10','8','25','1','3'],
 ['II*: v(a₁)=1','11','9','4','10','9','28','1','3'],
 ['II*: v(a₁)≥2, v(a₃)=3','12','9','0','8','12','32','2','4'],
]
table=ax.table(cellText=rows,colLabels=['family / condition','d','M','D₄','D₈','i₄','i₈','δ','f'],
               colWidths=[.44]+[.07]*8,cellLoc='center',bbox=[.05,.11,.90,.245])
table.auto_set_font_size(False);table.set_fontsize(10.3)
for (row,column),cell in table.get_celld().items():
 cell.set_edgecolor('#7890a6');cell.set_linewidth(.55)
 cell.set_facecolor('#e7eff8' if row==0 else ('#f6f8fb' if row%2 else '#ffffff'))
 if row==0:cell.set_text_props(weight='bold')
 if column==0:cell.set_text_props(ha='left');cell.PAD=.025
ax.text(2.5,1.25,'Dⱼ: K-normalized discriminant exponents; iⱼ: R-lengths\nQuadratic errors: the quartic-factor valuation; different: upper field\nSplit product decompositions are after finite unramified extension.',
        ha='center',fontsize=8.2,linespacing=1.55)
ax.text(2.5,.43,'The table includes every coefficient allowed by each preparation.\nLower bounds include coefficient zero. All residual cases remain open.',
        ha='center',fontsize=8.1,linespacing=1.5)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
target=root/'assets/additive-layers-proof-map.png'
fig.savefig(target,facecolor='white',metadata={'Software':'Matplotlib'});plt.close(fig)
with Image.open(target) as picture:picture.copy().save(target)

"""Exact finite-cycle construction, from CS1–CS5 and FC0–FC9. CC0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(14,16),dpi=100)
fig.patch.set_facecolor('#f6f8fb');ax.set_facecolor('#f6f8fb')
ax.set_xlim(0,14);ax.set_ylim(0,16);ax.axis('off')
ink='#142c44';blue='#dcebf8';green='#e0eee6';orange='#f7ebd9'
ax.text(7,15.55,'One complete correction cycle',ha='center',fontsize=27,color=ink,weight='bold')
ax.text(7,15.14,'Original operators, full fields, and exact receiving bounds',ha='center',fontsize=15,color=ink)
def box(y,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((.4,y),13.2,h,boxstyle='round,pad=0.12,rounding_size=0.15',facecolor=color,edgecolor='#8aa2b5'))
    ax.text(.72,y+h-.35,title,fontsize=17,color=ink,weight='bold')
    for k,line in enumerate(lines):ax.text(.75,y+h-.78-k*.38,line,fontsize=16,color=ink)
def arrow(y):ax.annotate('',xy=(7,y-.31),xytext=(7,y+.08),arrowprops=dict(arrowstyle='->',color='#335c7b',lw=2))
box(13.25,1.43,'Incoming state  |  FC0',[
    r'$B=0.7+j/10,\quad C_*=B+1/2,\quad \kappa_s=10^{-5}$',
    r'$w\in\mathsf{W}_{1/2},\ w-w_0^{\rm tan}\in\mathsf{W}_{0.68};\quad v,\gamma,p_m\in\mathsf{M}_{0.9},\ \beta\in\mathsf{M}_{1.9}$'],blue)
arrow(13.12)
box(11.23,1.58,'1. Cancel supported nonzero harmonics  |  FC3',[
    'Solve the inhomogeneous pulse equation; add its full curl and pressure.',
    r'Wave residual: $\mathsf{W}_{B+0.4}$; means and defects: order $C_*-\kappa_s$.',
    r'Weighted residual moments: $\mathsf{S}_{C_*+1-\kappa_s}$.'],green)
arrow(11.1)
box(9.2,1.58,'2. Correct the auxiliary-averaged stress  |  FC4',[
    'Use the compact signed stress and the fixed primary amplitude inverse.',
    r'Keep the entire covariance square; set $H=C_*-2\kappa_s$.',
    r'Averaged tangential residual: $\mathsf{M}_{C_*+0.18-\kappa_s}$.'],green)
arrow(9.07)
box(7.17,1.58,'3. Cancel nonconstant auxiliary means  |  FC5',[
    'Apply the torus inverse; retain the actual compact curl and axial remainder.',
    r'Full tangential residual: $\mathsf{M}_{C_*+0.18-\kappa_s}$.',
    r'Defects remain in $\mathsf{S}_H$; added wave source belongs to $\mathsf{W}_H$.'],green)
arrow(7.04)
box(5.14,1.58,'4. Correct the three current defects  |  FC6',[
    'Solve all five profile rows; preserve the two exact velocity moments.',
    r'New defects: $\mathsf{S}_{H+0.9}$; tangential change: $\mathsf{M}_{H+1}$.',
    r'Added wave source: $\mathsf{W}_H$. Recompute the complete pressure.'],green)
arrow(5.01)
box(2.81,1.88,'End of cycle  |  FC7',[
    r'Wave: $B+39999/100000$; full tangential: $C_*+17999/100000$.',
    r'Defects: $C_*+89998/100000$. Each gain exceeds the original $1/10$.',
    'The accumulated velocity bounds and both zero moments are preserved.',
    'Every next input uses the full updated velocity, pressure, and defects.'],orange)
box(.58,1.7,'Repeat on one positive domain  |  CS1–CS5, FC8',[
    r'$0<q<q_{\rm big}$: fixed base, phases, supports, denominators and inverse maps.',
    'Every finite stage has finitely many angular harmonics and finite derivative counts.',
    'Constants may grow with the stage. Actual infinite summation is a further construction.'],blue)
ax.text(7,.13,'Source: OpenAI, section 9, original pages 100–112. Complete proofs: CS1–CS5, FC0–FC9.',ha='center',fontsize=11,color=ink)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(P/'finite-correction-cycle.svg');fig.savefig(P/'finite-correction-cycle.png');plt.close(fig)
p=P/'finite-correction-cycle.svg'
p.write_text(re.sub(r'width="1008pt" height="1152pt"','width="1400" height="1600"',p.read_text(encoding='utf8')),encoding='utf8')

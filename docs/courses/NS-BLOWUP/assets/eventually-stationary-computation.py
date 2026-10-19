"""Exact detector, corridor and clock maps for ST0–ST8. CC0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

P = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'path', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(14, 14), dpi=100, facecolor='#f6f8fb')
fig.text(.5, .96, 'A fixed detector and an exact spatial clock', ha='center', fontsize=25, weight='bold', color='#142c44')
ax = fig.add_axes([.07, .52, .44, .39])
ax.set_aspect('equal'); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.add_patch(Rectangle((0, 1/32), 1, 1/8-1/32, facecolor='#f6dfbd', edgecolor='none'))
ax.axhline(1/32, color='#a66820', linestyle='--'); ax.axhline(1/8, color='#a66820', linestyle='--')
ax.add_patch(Rectangle((1/8, 1/32), 7/8-1/8, 7/8-1/32, facecolor='#dfeaf4', alpha=.45, edgecolor='#275d8c', linewidth=2))
ax.plot([1/4], [1/4], 'o', color='#152e48', markersize=8)
ax.annotate(r'$p=(1/4,1/4)$', (1/4, 1/4), xytext=(.33, .30), arrowprops={'arrowstyle':'->'}, fontsize=14)
ax.text(.5, .59, r'$J_*=[1/8,7/8]\times[1/32,7/8]$', ha='center', fontsize=13)
ax.text(.5, .51, r'$g=1$ on a neighborhood of $J_*$', ha='center', fontsize=12)
ax.text(.5, .078, r'$H:\quad 1/32<Y<1/8$', ha='center', fontsize=13)
ax.set_xlabel('X', fontsize=14); ax.set_ylabel('Y', fontsize=14)
ax.set_xticks([0,1/8,1/4,7/8,1], ['0','1/8','1/4','7/8','1'])
ax.set_yticks([0,1/8,1/4,7/8,1], ['0','1/8','1/4','7/8','1'])
ax.set_title('Exact fixed sets in the unit torus chart', fontsize=15, pad=15)
fig.text(.56,.86,'Whole rectangles implement every rule',fontsize=18,weight='bold',color='#142c44')
for y,t in [(.81,r'$F_r(w)=h_r+A_r(w-d_r)$'),(.77,r'$A_r=\mathrm{diag}(B^{-d},B^d),\quad d\in\{-1,0,1\}$'),(.72,'Sources and targets are separately disjoint.'),(.68,'Ordered extraction, scaling and insertion'),(.65,'realize all branches in one phase period.'),(.60,'Nonhalting paths satisfy Y > 3/16.'),(.56,'A halting phase enters H with margin 1/32.'),(.51,'Proof: ST2–ST5; no trajectory sample is shown.')]:
    fig.text(.56,y,t,fontsize=14,color='#142c44')
canvas=fig.add_axes([0,0,1,1]);canvas.axis('off');canvas.set_zorder(-1)
def box(y,h,title,lines,color):
    canvas.add_patch(FancyBboxPatch((.055,y),.89,h,boxstyle='round,pad=0.009',facecolor=color,edgecolor='#96abbc'))
    fig.text(.075,y+h-.030,title,fontsize=17,weight='bold',color='#142c44')
    for j,t in enumerate(lines):fig.text(.077,y+h-.066-j*.030,t,fontsize=14,color='#142c44')
box(.31,.145,'ST6  |  Mean-zero suspension and the original force',[
    r'$g=\partial_X(X\chi_*),\quad W=(V_1(Z,X,Y),V_2(Z,X,Y),g(X,Y)),\quad \nabla\!\cdot W=0,\quad\int W=0$',
    r'$\alpha(t)=\beta(2t-1),\quad U=\alpha W,\quad f=\alpha^{\prime}W+\alpha^2(W\!\cdot\!\nabla)W-\nu\alpha\Delta W$',
    r'$s(1)=1/4,\quad s(t)=t-3/4\ (t\geq1):\quad\mathrm{phase}\ n\ \mathrm{occurs\ at}\ t=n+3/4.$'], '#dfeaf4')
box(.13,.145,'ST8  |  Exact distinction between stationary work and a slow clock',[
    r'$F_\infty=(W\!\cdot\!\nabla)W-\nu\Delta W,\qquad\int F_\infty\!\cdot W=\nu\|\nabla W\|_2^2>0$',
    r'$a_\sigma(t)=\beta(2t-1)(1+t)^{-\sigma},\quad 0<\sigma\leq1,\qquad\int_0^\infty a_\sigma(t)\,dt=\infty$',
    r'$U_\sigma=a_\sigma W,\quad F_\sigma=a_\sigma^{\prime}W+a_\sigma^2(W\!\cdot\!\nabla)W-\nu a_\sigma\Delta W$'], '#e0eee6')
fig.text(.5,.075,'ST8 retains every derivative coefficient and proves the time-integrability range.',ha='center',fontsize=14,color='#142c44')
fig.text(.5,.037,'Source: OpenAI, Eventually Stationary Navier–Stokes Forcing (2026); independent proof ST0–ST8.',ha='center',fontsize=11,color='#142c44')
fig.savefig(P/'eventually-stationary-computation.svg')
fig.savefig(P/'eventually-stationary-computation.png')
plt.close(fig)
p=P/'eventually-stationary-computation.svg'
p.write_text(re.sub(r'width="1008pt" height="1008pt"','width="1400" height="1400"',p.read_text(encoding='utf8')),encoding='utf8')

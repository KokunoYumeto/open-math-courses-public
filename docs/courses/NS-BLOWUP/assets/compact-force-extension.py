"""Exact localization and terminal-force construction, LF0–LF5. CC0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(14,16),dpi=100)
fig.patch.set_facecolor('#f6f8fb');ax.set_xlim(0,14);ax.set_ylim(0,16);ax.axis('off')
ink='#142c44';blue='#dcebf8';green='#e0eee6';gold='#f7ebd9'
ax.text(7,15.55,'A compact field and a smooth force',ha='center',fontsize=27,color=ink,weight='bold')
ax.text(7,15.12,'The force extends through time one; the singular velocity is used only before it',ha='center',fontsize=14,color=ink)
def box(x,y,w,h,title,lines,color,size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.15',facecolor=color,edgecolor='#8aa2b5'))
    ax.text(x+.25,y+h-.35,title,fontsize=17,color=ink,weight='bold')
    step=.35 if len(lines)==5 else .42
    for k,line in enumerate(lines):ax.text(x+.27,y+h-.82-k*step,line,fontsize=size,color=ink)
def arrow(y):ax.annotate('',xy=(7,y-.30),xytext=(7,y+.08),arrowprops=dict(arrowstyle='->',color='#335c7b',lw=2))
box(.4,12.55,13.2,1.97,'Localize the potentials and retain the full curl  |  LF0–LF1',[
    r'$u=\operatorname{curl}(c\mathcal{A})+c\mathcal{B}e_\theta=cv+\nabla c\times\mathcal{A},\qquad p=cp^{\rm loc}$',
    r'$\operatorname{div}u=0,\qquad f^-=\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p$',
    r'Support: $\mathcal{K}\times[1-\tau_0,1)$; the full residual includes all cutoff derivatives.'],blue)
arrow(12.4)
box(.4,9.7,4.16,2.4,'Positive q  |  LF2',[
    r'$0<c_0\leq q<q_*$',
    'Actual field derivatives',
    'remain uniformly bounded.',
    'One more time derivative',
    'gives uniform limits.'],green,size=13)
box(4.92,9.7,4.16,2.4,'Heat exterior  |  LF2',[
    r'$r>0,\quad X\geq X_{\rm ext}$',
    r'$v=K(r,1-t)e_\theta$',
    'The heat integral controls',
    'velocity and pressure jets.',
    'Cutoff force terms remain.'],green,size=13)
box(9.44,9.7,4.16,2.4,'Near the origin  |  LF2',[
    r'$c=1,\quad f^-=\mathscr{R}(v,p^{\rm loc})$',
    'Every mixed derivative is',
    r'$O((1-t+|z|^{1/D})^N)$',
    'for every fixed power N.',
    'The exterior residual is zero.'],green,size=12)
arrow(9.55)
box(.4,7.48,13.2,1.78,'Compatible terminal data on the whole spatial domain  |  LF2',[
    r'$F_j(x)=\lim_{t\uparrow1}\partial_t^j f^-(x,t),\quad F_j\in C_c^\infty,\quad \operatorname{supp}F_j\subset\mathcal{K}$',
    r'$\partial_x^\alpha F_j(0)=0,\qquad\partial_x^\alpha\partial_t^j f^-\longrightarrow\partial_x^\alpha F_j$',
    'Uniform limits and the fundamental theorem of calculus give every matching derivative.'],blue)
arrow(7.33)
box(.4,4.75,13.2,2.28,'One actual compact extension  |  LF3',[
    r'$f^+(x,1+s)=\sum_{j=0}^\infty\chi_0(b_js)\,s^jF_j(x)/j!,\qquad s\geq0$',
    r'$b_j>b_{j-1},\quad C_{j,m}b_j^{m-j}\|F_j\|_{C^a}\leq2^{-j}\quad(a+m\leq\lfloor j/2\rfloor)$',
    r'$\partial_t^m f^+(x,1)=F_m(x),\quad\operatorname{supp}f\subset\mathcal{K}\times[1-\tau_0,2]$',
    'Finite constraints select each integer; every differentiated tail converges uniformly.'],gold)
box(.4,2.3,13.2,2.0,'Every original viscosity factor  |  LF4',[
    r'$y=x_\nu/\sqrt{\nu},\quad u_\nu=\sqrt{\nu}u(y,t),\quad p_\nu=\nu p(y,t),\quad f_\nu=\sqrt{\nu}f(y,t)$',
    r'$\mathscr{R}_\nu(u_\nu,p_\nu)=f_\nu,\qquad\mathcal{K}_\nu=\sqrt{\nu}\mathcal{K}$',
    r'$\partial_{x_\nu}^\alpha\partial_t^m f_\nu=\nu^{(1-|\alpha|)/2}(\partial_y^\alpha\partial_t^m f)(y,t)$'],green)
box(.4,.6,13.2,1.4,'What is preserved  |  LF5',[
    'Exact equation before time one, zero initial velocity, all terminal jets, compact support.',
    'Future extensions differ by a smooth compact term supported at times one through two.'],blue,size=14)
ax.text(7,.18,'Source: OpenAI, Proposition 10.1, Lemmas 10.2–10.3 and (10.22). Proof: LF0–LF5.',ha='center',fontsize=11,color=ink)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(P/'compact-force-extension.svg');fig.savefig(P/'compact-force-extension.png');plt.close(fig)
p=P/'compact-force-extension.svg';p.write_text(re.sub(r'width="1008pt" height="1152pt"','width="1400" height="1600"',p.read_text(encoding='utf8')),encoding='utf8')

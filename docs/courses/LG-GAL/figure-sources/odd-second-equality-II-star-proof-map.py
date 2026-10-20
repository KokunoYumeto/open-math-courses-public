"""Reproducible, schematic proof diagram for Lesson 08, Section 6.0AN.

Run with Python and Matplotlib; an optional single argument is the PNG path.
The coordinates below are schematic layout coordinates, not curve coordinates.
All exponents and maps are exact. No TeX installation or network is needed.
"""
from pathlib import Path
import sys
# The public scene keeps validation records outside the artifact.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

out = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parent.parent / 'assets/odd-second-equality-II-star-proof-map.png'
assert len(sys.argv) <= 2
ink, blue, green, red = '#172b40', '#245c91', '#16705a', '#a23a3a'
fig = plt.figure(figsize=(9, 36), dpi=100, facecolor='#f5f8fc')
fig.text(.055,.982,'Odd second valuation: the equality boundary',fontsize=20,weight='bold',color=ink,va='top')
fig.text(.055,.968,'Exact full rings, the original orders, and the wild action',fontsize=13,color=blue,va='top')
fig.text(.055,.956,'Proof 6.0AN.1–6.0AN.6 • schematic algebra maps • every permitted residue factorization',fontsize=10,color=ink,va='top')


def panel(number, title, locator):
    top = .943 - (number-1)*.147
    ax = fig.add_axes([.045,top-.137,.91,.137])
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(FancyBboxPatch((.005,.01),.99,.98,boxstyle='round,pad=0.004,rounding_size=.018',
                              facecolor='white',edgecolor='#cbd8e8',linewidth=1.1))
    ax.text(.025,.94,f'{number}. {title}',fontsize=15,weight='bold',color=ink,va='top')
    ax.text(.025,.872,locator,fontsize=10,color=blue,va='top')
    return ax


def line(ax, y, text, size=14, color=ink, x=.035):
    ax.text(x,y,text,fontsize=size,color=color,va='top')


def box(ax, xy, width, height, text, color=blue, size=12):
    ax.add_patch(FancyBboxPatch(xy,width,height,boxstyle='round,pad=0.009,rounding_size=.014',
                              facecolor='#f4f8fc',edgecolor=color,linewidth=1.1))
    ax.text(xy[0]+width/2,xy[1]+height/2,text,fontsize=size,color=ink,ha='center',va='center')


def arrow(ax, start, end, text='', yoffset=.015):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,color=blue,linewidth=1.5))
    if text:
        ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+yoffset,text,fontsize=11,color=blue,ha='center',va='bottom')


ax = panel(1,'The complete coefficient range','HP1–HP5; nine-component geometry: earlier Lemmas 6.0E and 6.0H')
line(ax,.785,r'$k=v(a_2)\geq 3\ \mathrm{odd},\quad e=v(2),\quad 2e=3k-5$',17)
line(ax,.67,r'$v(a_1)>e+k/2,\quad v(a_3)>e+5/2$',15)
line(ax,.565,r'$v(a_4)>e+(k+5)/2,\quad v(a_6)=5$',15)
line(ax,.455,'Arbitrary second and sixth units; the other coefficients may vanish.',11)
line(ax,.375,'All finite values are allowed above the strict bounds.',11)
line(ax,.275,r'$d=v(\Delta)=4e+10=6k,\quad M=9$',17,color=green)
line(ax,.155,r'$v(c_4)=4e+2k,\quad v(j)=8e+6k-10>0$',14)

ax = panel(2,'Every quartic factor is unramified and full','HP6–HP7; earlier unramified lifting and full trace-dual proofs')
line(ax,.79,r'$Z=x/\pi^k,\quad \overline{Q}(T)=T^4+\overline{C}_1T+\overline{C}_0$',16)
line(ax,.67,r'$\overline{C}_1\ne0\quad\Longrightarrow\quad\overline{Q}^{\prime}(T)=\overline{C}_1$',15,color=green)
line(ax,.565,'Four distinct roots lift in a finite unramified splitting extension.',11)
box(ax,(.035,.31),.33,.16,r'$A_4=R[x]/q$',size=16)
box(ax,(.57,.31),.39,.16,r'$B_4=R[Z]=\prod_j C_j$',size=15)
arrow(ax,(.375,.39),(.557,.39),r'$x=\pi^k Z$')
line(ax,.23,r'$E_j=1,\quad d_j=0,\quad\sum_j f_j=4,\quad D_4=0$',14)
line(ax,.12,r'$\det(1,x,x^2,x^3\ \mathrm{in}\ 1,Z,Z^2,Z^3)=\pi^{6k}$',12)
line(ax,.07,r'$i_4=6k=d$; unit trace determinant proves the entire ring.',11,color=green)

ax = panel(3,'The exact identity fixes the radical value','HP8–HP9; complete Weierstrass coefficients are retained')
line(ax,.79,r'$B_0=3x+b_2/4,\quad N=3x^2+(b_2/2)x+b_4/2$',14)
line(ax,.68,r'$U=x^3+a_2x^2+a_4x+a_6+(a_1x+a_3)^2/4$',13)
box(ax,(.035,.405),.92,.17,r'$N^2-4UB_0=-3q(x)$',size=22,color=red)
line(ax,.33,r'$q(x)=0,\quad v(U)=5,\quad v(N)=2k$',16)
line(ax,.215,r'$v(B_0)=4k-2e-5=k$',19,color=green)
line(ax,.105,r'Both summands of $B_0$ have value $k$.',12)
line(ax,.065,'The displayed identity proves the sum’s value at every actual root.',11,color=red)

ax = panel(4,'The same point algebra and its full integral ring','HP10; entire point-ring and determinant proof: 6.0AN.5')
line(ax,.79,r'$s=\pi^{(k-1)/2},\quad Y=y+(a_1x+a_3)/2$',15)
line(ax,.675,r'$B=B_0/s^2=\pi(3Z+u_0),\quad v(B)=1$',15)
line(ax,.6,r'$u_0=b_2/(4\pi^k)\in R^{\times}$',12)
line(ax,.52,r'$\zeta=N/(2sY),\quad\zeta^2=B$',17)
line(ax,.415,r'$D=N/(2sB),\quad y=D\zeta-(a_1x+a_3)/2$',14)
line(ax,.32,r'$v(D)=2,\quad v((a_1x+a_3)/2)\geq3$',14)
box(ax,(.035,.105),.92,.15,'Each entire point ring: '+r'$C_j[\zeta_j],\quad T^2-B_j$'+' Eisenstein',size=13,color=green)
line(ax,.07,r'$\ell_j=2,\quad d_{\mathrm{point}/F_j}=2e+1$ (upper normalized valuation).',11)

ax = panel(5,'Residue weights give the original-order equality','HP11; full rings and both indices are computed before the conductor')
line(ax,.79,r'$\ell=\sum_j f_j\ell_j=2\sum_j f_j=8$',19,color=green)
line(ax,.66,r'$i_4=d,\quad i_8=2i_4+\ell=2d+8$',18)
box(ax,(.035,.37),.92,.16,r'$i_4+\ell=d+8$',size=24,color=green)
line(ax,.285,r'$D_8=\sum_j f_j(2e+1)=8e+4$',17)
line(ax,.17,r'$6d-2i_8=D_8$',19)
line(ax,.07,'Each local length is weighted by its residue degree '+r'$f_j$'+'.',11)

ax = panel(6,'One wild scalar swaps all four geometric pairs','HP12 and 6.0AN.6; pairs shown over a separable splitting field')
for i, vector in enumerate(['(1,0)','(0,1)','(1,1)','(1,2)']):
    xx = .13+i*.24
    for yy, label in [(.665,r'$P_'+str(i+1)+'$'),(.465,r'$-P_'+str(i+1)+'$')]:
        ax.add_patch(Circle((xx,yy),.026,facecolor=green,edgecolor='white',linewidth=.7))
        ax.text(xx+.045,yy,label,fontsize=12,color=ink,va='center')
    ax.add_patch(FancyArrowPatch((xx,.627),(xx,.503),arrowstyle='<->',mutation_scale=12,color=red,linewidth=1.5))
    ax.text(xx,.75,vector,ha='center',fontsize=11,color=ink)
line(ax,.365,'The labels above are torsion-basis representatives in '+r'$\mathbf{F}_3^2$'+'.',10)
line(ax,.295,r'Wild image on $T_3E$: $\{I,-I\}$; every inertia-fixed vector is zero.',11)
line(ax,.218,r'$\epsilon_4=0,\quad\epsilon_8=4,\quad\delta=(D_8-4)/2=4e$',14)
line(ax,.12,r'$f(E/K)=4e+2=d-8,\quad M-1+f(E/K)=d$',15,color=green)
line(ax,.065,'Scope is HP1; other preparations are outside these hypotheses. General NF24: JM30–JM32.',10,color=red)

fig.text(.055,.047,'Source: J. S. Milne, free Algebraic Number Theory notes,',fontsize=10,color=ink,va='top')
fig.text(.055,.037,'Proposition 2.43; Proposition 7.55 and Remark 7.56. www.jmilne.org/math/CourseNotes/ANT.pdf',fontsize=9,color=ink,va='top')
fig.text(.055,.027,'Every specialized assertion is proved in 6.0AN.1–6.0AN.6 or the exact earlier lesson providers named there.',fontsize=9,color=ink,va='top')
fig.text(.055,.017,'The diagram accompanies the proof and graded solution under the stated hypotheses.',fontsize=9,color=ink,va='top')
out.parent.mkdir(parents=True, exist_ok=True)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
texts = list(fig.texts) + [text for axes in fig.axes for text in axes.texts]
text_bounds = []
for text in texts:
    bounds = text.get_window_extent(renderer)
    assert 8 <= bounds.x0 and bounds.x1 <= 892 and 8 <= bounds.y0 and bounds.y1 <= 3592, (text.get_text(), bounds)
    text_bounds.append({'text':text.get_text(),'bounds_pixels':[float(v) for v in bounds.extents]})
for axes in fig.axes:
    for text in axes.texts:
        bounds = text.get_window_extent(renderer)
        assert axes.bbox.x0+10 <= bounds.x0 and bounds.x1 <= axes.bbox.x1-10, text.get_text()
        assert axes.bbox.y0+8 <= bounds.y0 and bounds.y1 <= axes.bbox.y1-8, text.get_text()
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor(), metadata={'Description':'Exact schematic algebra maps for the Lesson 08 Section 6.0AN equality-case proof; original point algebra and residue weights retained.'})
plt.close(fig)
# The public scene writes only the figure; author validation records remain private.
print(out.name)

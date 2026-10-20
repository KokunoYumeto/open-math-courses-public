"""Reproducible exact algebra maps for the missing first boundary, 6.0AP.1–7.

Page coordinates are schematic layout coordinates, never curve coordinates.
All valuations, maps, bases, different exponents and residue weights are exact.
The whole written argument accompanies this original diagram. No TeX is used.
"""
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch,Circle
from matplotlib.text import Text

w=Path(__file__).resolve().parent.parent/'assets'
assert len(sys.argv)<=2
out=Path(sys.argv[1]) if len(sys.argv)==2 else w/'first-boundary-odd-second-equality-proof-map.png'
ink,blue,green,red='#172b40','#245c91','#16705a','#a23a3a'
fig=plt.figure(figsize=(9,36),dpi=100,facecolor='#f5f8fc')
fig.text(.055,.982,'One lower first coefficient changes both full rings',fontsize=20,weight='bold',color=ink,va='top')
fig.text(.055,.968,'Reciprocal quartic, exact square error, original-order lengths',fontsize=13,color=blue,va='top')
fig.text(.055,.956,'Proof 6.0AP.1–7 • exact algebra maps • arbitrary allowed units and higher coefficients',fontsize=10,color=ink,va='top')
panels=[]

def panel(n,title,locator):
    top=.943-(n-1)*.147
    ax=fig.add_axes([.045,top-.137,.91,.137]);panels.append(ax)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.add_patch(FancyBboxPatch((.005,.01),.99,.98,boxstyle='round,pad=.004,rounding_size=.018',facecolor='white',edgecolor='#cbd8e8',linewidth=1.1))
    ax.text(.025,.94,f'{n}. {title}',fontsize=15,weight='bold',color=ink,va='top')
    ax.text(.025,.872,locator,fontsize=10,color=blue,va='top')
    return ax

def line(ax,y,text,size=14,color=ink,x=.035):
    ax.text(x,y,text,fontsize=size,color=color,va='top')

def box(ax,xy,width,height,text,color=blue,size=14):
    ax.add_patch(FancyBboxPatch(xy,width,height,boxstyle='round,pad=.009,rounding_size=.014',facecolor='#f4f8fc',edgecolor=color,linewidth=1.1))
    ax.text(xy[0]+width/2,xy[1]+height/2,text,fontsize=size,color=ink,ha='center',va='center')

def arrow(ax,start,end,text=''):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,color=blue,linewidth=1.5))
    if text:ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+.02,text,fontsize=10,color=blue,ha='center',va='bottom')

ax=panel(1,'The missing integer first boundary','6.0AP.1–6.0AP.2; component count and minimality come from earlier written proofs')
line(ax,.79,r'$k=v(a_2)\geq3\ \mathrm{odd},\quad e=v(2),\quad2e=3k-5$',16)
line(ax,.685,r'$v(a_1)=2k-3,\quad v(a_3)\geq(3k+1)/2$',16)
line(ax,.58,r'$v(a_4)\geq2k,\quad v(a_6)=5$',16,color=green)
line(ax,.475,'First, second and sixth units arbitrary; third or fourth may vanish.',11)
line(ax,.39,r'$v(b_8)=4k-1,\quad v(c_4)=8k-12$',15)
line(ax,.275,r'$d=v(\Delta)=6k=4e+10,\quad M=9$',18,color=green)
line(ax,.16,r'$v(j)=18k-36>0$; no upper coefficient bounds.',13)
line(ax,.07,'Higher first values are already proved in Section 6.0AO.',11)

ax=panel(2,'The reciprocal coordinate gives the full quartic ring','6.0AP.3; full Eisenstein ring, whole basis determinant and derivative different')
line(ax,.79,r'$\theta=\pi^k/x,\quad P(T)=uT^4+r_1T^3+r_2T^2+r_3T+3\pi$',14)
line(ax,.685,r'$v(u)=0,\quad v(r_1)=1,\quad v(r_2)\geq e+1,\quad v(r_3)=2e$',14)
line(ax,.575,r'$P/u$ is Eisenstein; $v_F(\theta)=1$, $v_F=4v$.',15,color=green)
box(ax,(.035,.31),.32,.16,r'$A_4=R[x]/q$',size=16)
box(ax,(.59,.31),.365,.16,r'$C=R[\theta]$',size=17)
arrow(ax,(.366,.39),(.578,.39),'normalization')
line(ax,.255,r'$x=\pi^k/\theta,\quad v(x)=k-1/4$; full basis $1,\theta,\theta^2,\theta^3$.',13)
line(ax,.155,r'Derivative values: $8e+3,\ 6,\ \geq8e+5,\ 8e$.',14)
line(ax,.07,r'$[F:K]=4$, residue degree $1$, entire different $D_4=6$.',14,color=green)

ax=panel(3,'A value-three error survives every square','6.0AP.4; normalized valuations on the entire quartic field are used')
line(ax,.79,r'$A=a_1x+a_3,\quad Y=y+A/2,\quad Y^2=U$',15)
line(ax,.69,r'$U=x^3+a_2x^2+a_4x+a_6+(A/2)^2$',15)
line(ax,.59,r'$v_F(A/2)\geq12,\quad v_F(U)=20,\quad V=U/\theta^{20}$',15)
line(ax,.48,r'$V=c_0+c_3\theta^3+O(\theta^4),\quad c_0,c_3\in R^\times$',17,color=green)
line(ax,.37,r'Choose $c\in R^\times$ with $\overline{c}^{\,2}=\overline{c}_0$.',14)
line(ax,.255,r'$v_F(V-c^2)=3,\qquad\max_{s\in F}v_F(V-s^2)=3$',17,color=green)
line(ax,.135,r'For $s=c+r$: $v_F(r)=1$ gives error $2$; $v_F(r)\geq2$ gives $3$.',12)
line(ax,.05,'Other residues or nonunit roots give error at most zero; all roots are covered.',10)

ax=panel(4,'The shifted generator recovers the original point','6.0AP.5; both maps, integral shift and complete point basis are explicit')
line(ax,.79,r'$w=(Y/\theta^{10}-c)/\theta$',19,color=green)
line(ax,.68,r'$w^2+(2c/\theta)w+(c^2-V)/\theta^2=0$',17)
line(ax,.56,r'$v_F(2c/\theta)=4e-1,\quad v_F((c^2-V)/\theta^2)=1$',15)
line(ax,.45,r'Eisenstein: full ring $B=C[w]$, $[L:F]=2$, residue degree $1$.',13)
box(ax,(.035,.26),.92,.12,r'$y=\theta^{11}w+c\theta^{10}-A/2$',size=19,color=green)
line(ax,.235,r'Basis columns: $(1,0)$ and $(c\theta^{10}-A/2,\theta^{11})$.',13)
line(ax,.135,r'Original relative length $\ell=v_F(\theta^{11})=11$.',15)
line(ax,.065,r'Entire relative different $d_{L/F}=8e-2$; $v_L=2v_F$.',14,color=green)

ax=panel(5,'Original-order lengths come before conductors','6.0AP.3 and 6.0AP.5; every length has its actual residue weight')
line(ax,.79,r'$N_{F/K}(\theta)=3\pi/u,\quad v(N(\theta))=1$',16)
line(ax,.68,r'Whole quartic basis determinant $=\pi^{6k}/N(\theta)^3$.',15)
line(ax,.56,r'$i_4=6k-3,\quad\ell=11,\quad i_8=2i_4+\ell=12k+5$',17)
line(ax,.445,r'$D_4=6,\quad D_8=2D_4+d_{L/F}=8e+10$',17)
line(ax,.335,r'$6d-2i_8=D_8$; both whole integer rings have been constructed.',13)
box(ax,(.035,.135),.92,.12,r'$i_4+\ell=d+8=d+M-1$',size=22,color=green)
line(ax,.055,'Both residue degrees are one: C-length eleven is R-length eleven.',11)

ax=panel(6,'The scalar involution pairs all eight points','6.0AP.6; labels are torsion-basis vectors, never coordinates on the curve')
for i,label in enumerate(['(1,0)','(0,1)','(1,1)','(1,2)']):
    xx=.14+i*.235
    ax.text(xx,.76,label,fontsize=11,color=ink,ha='center')
    for yy in [.655,.46]:ax.add_patch(Circle((xx,yy),.025,facecolor=green,edgecolor='none'))
    ax.text(xx+.045,.655,f'$P_{i+1}$',fontsize=12,color=ink,va='center')
    ax.text(xx+.045,.46,f'$-P_{i+1}$',fontsize=12,color=ink,va='center')
    ax.add_patch(FancyArrowPatch((xx,.615),(xx,.5),arrowstyle='<->',mutation_scale=10,color=red,linewidth=1.2))
line(ax,.355,'Red arrows: wild scalar −I. Inertia has one orbit on pairs and on points.',11)
line(ax,.245,r'$\epsilon_4=3,\quad\epsilon_8=7,\quad\nu=0,\quad\delta=4e$',17)
line(ax,.13,r'$f(E/K)=4e+2=d-8,\quad M-1+f(E/K)=d$',18,color=green)
line(ax,.045,'The tame conductor is two; the full different calculation precedes Swan use.',10)

fig.text(.055,.048,'Source: J. S. Milne, free Algebraic Number Theory notes,',fontsize=10,color=ink,va='top')
fig.text(.055,.038,'Proposition 2.43; Proposition 7.55 and Remark 7.56. www.jmilne.org/math/CourseNotes/ANT.pdf',fontsize=9,color=ink,va='top')
fig.text(.055,.028,'All specialized assertions are proved in 6.0AP.1–7 or the exact earlier lesson providers named there.',fontsize=9,color=ink,va='top')
fig.text(.055,.018,'Full proof and eight-point solution accompany this map. Other preparations are outside these hypotheses; general NF24 is JM30–JM32.',fontsize=9,color=ink,va='top')
fig.canvas.draw();renderer=fig.canvas.get_renderer();text_bounds=[]
for artist in fig.findobj(match=Text):
    if not artist.get_text():continue
    b=artist.get_window_extent(renderer)
    assert b.x0>=0 and b.y0>=0 and b.x1<=900 and b.y1<=3600,(artist.get_text(),b.bounds)
    if artist.axes in panels:
        ab=artist.axes.get_window_extent(renderer)
        assert b.x0>=ab.x0 and b.x1<=ab.x1 and b.y0>=ab.y0 and b.y1<=ab.y1,(artist.get_text(),b.bounds)
    text_bounds.append({'text':artist.get_text(),'bounds_pixels':[b.x0,b.y0,b.x1,b.y1]})
fig.savefig(out,dpi=100,facecolor=fig.get_facecolor());plt.close(fig)
print(str(out.resolve()))

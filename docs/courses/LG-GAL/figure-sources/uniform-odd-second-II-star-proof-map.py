"""Reproducible proof map of HO1–HO33; coordinates are schematic.

The valuation panel labels an illustrative lemma pattern explicitly. It fixes
no curve coefficients. All statements retain their hypotheses and proof links.
"""
from pathlib import Path
import hashlib
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig = plt.figure(figsize=(9,48),dpi=100,facecolor='#f4f7fb')
ink = '#172b43'; blue = '#1d638d'; green = '#176b4b'; red = '#a23d38'
texts = []


def panel(index,title,locator):
    bottom = .837-index*.113
    ax = fig.add_axes([.055,bottom,.89,.101])
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle='round,pad=0.012',
                              facecolor='white',edgecolor='#cad6e4',linewidth=1,
                              transform=ax.transAxes,clip_on=False))
    put(ax,.04,.925,title,14,blue,weight='bold')
    put(ax,.04,.06,'Proof: '+locator,10,'#526377')
    return ax


def put(ax,x,y,text,size=12,color=ink,weight='normal',ha='left'):
    artist=ax.text(x,y,text,fontsize=size,color=color,fontweight=weight,
                   ha=ha,va='top',transform=ax.transAxes,linespacing=1.5)
    texts.append(artist)
    return artist


fig.text(.055,.982,'Every high odd-second preparation',fontsize=22,color=ink,weight='bold',va='top')
fig.text(.055,.972,'Full factor rings → maximal square error → original point order',fontsize=13,color=blue,va='top')
fig.text(.055,.963,'Proof map. The complete argument and graded solution remain in 6.0AM.1–6.0AM.8.',fontsize=10,color=ink,va='top')

ax=panel(0,'1. The whole preparation and the exact point radical','HO1–HO8')
put(ax,.04,.79,r'$k=v(a_2)\geq3\ \mathrm{odd},\quad n=2e-3k+5\geq2,\quad \mu=k+n/4$')
put(ax,.04,.68,r'$h>e+\mu/2,\quad z>e+(\mu+5-k)/2$')
put(ax,.04,.57,r'$l>e+(\mu+5)/2,\quad v(a_6)=5,\quad e=v(2)$')
put(ax,.04,.46,r'$B=\pi u_0+3\pi^{1-k}x,\quad \zeta^2=B,\quad v(B)=1$')
put(ax,.04,.35,r'$y=D\zeta-A/2,\quad v(D)=2,\quad v(A/2)\geq3$')
put(ax,.04,.23,'Arbitrary units; vanishing higher coefficients allowed. No upper bound on n.',11)
put(ax,.04,.15,'Every actual quartic decomposition is retained; d = 4e + 10 and M = 9.',11)

ax=panel(1,'2. Bound the different of every full quartic factor','HO9–HO18')
put(ax,.04,.80,r'$B_4=\prod_j C_j,\quad E_j=e(F_j/K),\quad f_j=[\kappa_j:\kappa],\quad \sum_jE_jf_j=4$')
put(ax,.04,.69,'For E odd: d_j = E_j − 1. For E even: d_j is even and at least E_j.',11)
put(ax,.07,.55,'n',12,blue,weight='bold');put(ax,.39,.55,'E = 2',12,blue,weight='bold');put(ax,.69,.55,'E = 4',12,blue,weight='bold')
put(ax,.07,.45,'4r, r ≥ 1');put(ax,.39,.45,r'$d_j\leq2r$');put(ax,.69,.45,r'$d_j\leq4r$')
put(ax,.07,.35,'4r + 2, r ≥ 1');put(ax,.39,.35,r'$d_j\leq2r$');put(ax,.69,.35,r'$d_j\leq4r+2$')
put(ax,.07,.25,'2');put(ax,.39,.25,'cannot occur');put(ax,.69,.25,r'$d_j=4$')
put(ax,.04,.14,r'$d_j+1<E_je,\qquad E_j(1+\mu-k)-1>d_j$',12,green)

ax=panel(2,'3. Construct series in the full ring, then differentiate','HO19–HO21')
put(ax,.04,.80,r'$S/2S=\kappa_j,\quad R^\prime\subset C_j,\quad C_j=R^\prime[\alpha],\quad v_C(\alpha)=1$')
put(ax,.04,.68,'Residue lifting over Q₂ constructs S inside R′. Completeness gives digits.',11)
put(ax,.04,.57,r'$G(P,A)=A^E+\sum_{i<E}g_i(P)A^i,\quad G_P(0,0)\in S^\times$')
put(ax,.04,.46,r'$G(F(A),A)=0,\quad F(A)=A^E\cdot\mathrm{unit},\quad F(\alpha)=\pi$')
put(ax,.04,.35,'Coefficient recursion constructs F. A unit difference quotient proves equality.',11)
put(ax,.04,.24,r"$F'(\alpha)=-G_A(\pi,\alpha)/G_P(\pi,\alpha)$")
put(ax,.04,.14,r"$v_C(F'(\alpha))=d_C,\qquad T=v_C(2)=Ee$",12,green)

ax=panel(3,'4. The derivative belongs to the exact radical','HO24–HO26')
put(ax,.04,.80,r'$H(A)=F(A)u_0(F(A))+3F(A)^{1-k}X(A),\quad H(\alpha)=B$')
put(ax,.04,.69,r'$X(A)\in A^{E\mu}S[[A]],\quad E\mu>E(k-1)$')
put(ax,.04,.59,'The apparent negative power cancels. Keep all three derivative terms:',11)
put(ax,.04,.48,r"$[u_0(\pi)+\pi u_0'(\pi)]F'(\alpha)$",12,green)
put(ax,.04,.37,r"$+\ 3\pi^{1-k}X'(\alpha)+3(1-k)\pi^{-k}xF'(\alpha)$")
put(ax,.04,.25,r'$v_C(\mathrm{second})\geq E(1+\mu-k)-1>d_C$')
put(ax,.04,.15,r"$v_C(\mathrm{third})\geq E(\mu-k)+d_C>d_C\ \Longrightarrow\ v_C(H')=d_C$",11,green)

ax=panel(4,'5. The first odd degree is the maximal square obstruction','HO22–HO23')
put(ax,.04,.80,r'$d_C\ \mathrm{even},\quad d_C+1<T:\quad\mathrm{first\ odd\ unit\ degree}=d_C+1$')
put(ax,.04,.69,r'$w=\sum_{2a<d_C+1}b_a\alpha^a,\quad v_C(w)=E/2$')
put(ax,.04,.58,r'$v_C(w^2-B)=d_C+1\quad\mathrm{and\ no\ square\ improves\ this}$',12,green)
put(ax,.04,.47,'Illustrative lemma pattern: E = 4, d_C = 6, T = 20; no curve coefficients fixed.',10)
line_y=.31
ax.plot([.07,.93],[line_y,line_y],color='#607487',lw=1,transform=ax.transAxes)
for value,label,color in [(4,'4: even',blue),(6,'6: even',blue),(7,'7: first odd',red),(20,'20: two threshold',ink)]:
    xx=.07+.86*value/20
    ax.plot([xx,xx],[line_y-.02,line_y+.025],color=color,transform=ax.transAxes)
    ax.scatter([xx],[line_y+.04],s=45,color=color,transform=ax.transAxes)
    yy=.25 if value!=6 else .19
    put(ax,xx,yy,label,9,color,ha='center')
put(ax,.04,.13,'Match earlier even coefficients by residue square roots; the odd error survives.',10)

ax=panel(5,'6. Entire point rings and the determinant of the original order','HO27–HO31')
put(ax,.04,.80,r'$E\ \mathrm{even}:\quad\eta=(\zeta-w)/\alpha^{d_C/2}$')
put(ax,.04,.68,r'$\eta^2+(2w/\alpha^{d_C/2})\eta+(w^2-B)/\alpha^{d_C}=0$')
put(ax,.04,.56,'Constant value 1; trace value Ee + E/2 − d_C/2 > 0. Entire ring C[η].',11)
put(ax,.04,.44,r'$E\ \mathrm{odd}:\quad\eta=\zeta/\alpha^{(E-1)/2},\quad\eta^2=B/\alpha^{E-1}$')
put(ax,.04,.32,r'$d_{8,j/4,j}=2E_je+E_j-d_j\quad\mathrm{in\ every\ factor}$',12,green)
put(ax,.04,.21,r'$y=(Dw-A/2)+D\alpha^{d_C/2}\eta\quad(E\ \mathrm{even})$')
put(ax,.04,.12,r'$\ell_j=\operatorname{length}_{C_j}(C_j[\eta]/C_j[y])=2E_j+d_j/2$',12,green)

ax=panel(6,'7. Residue weights give the index equality before the conductor','HO32–HO33')
put(ax,.04,.80,r'$D_4=\sum_j f_jd_j=2d-2i_4$')
put(ax,.04,.69,r'$\ell=\sum_j f_j\ell_j=8+D_4/2\quad\Longrightarrow\quad i_4+\ell=d+8$',12,green)
put(ax,.04,.57,r'$D_8=D_4+8e+4=6d-2i_8,\quad i_8=2i_4+\ell$')
put(ax,.04,.45,'Every point quadratic ramifies: ν = 0. Wild torsion acts with central −1.',11)
put(ax,.04,.34,'The proved quaternion comparison gives no inertia invariants and tame part 2.',11)
put(ax,.04,.23,r'$\delta=2d-i_4-\ell-2=4e,\quad f(E/K)=4e+2$')
put(ax,.04,.12,r'$M-1+f(E/K)=d,\quad M=9,\quad d=4e+10$',12,green)

ax=panel(7,'8. Exact scope, earlier proofs and free human context','6.0AM.1 and 6.0AM.7–6.0AM.8')
put(ax,.04,.80,'Covers every HO1 preparation, including all deeper even n ≥ 8.',12,green)
put(ax,.04,.69,'Lower coefficient bounds and other preparations lie outside these hypotheses.',11)
put(ax,.04,.58,'Earlier written providers: Lesson 01, 0F.2 and 0G.2–0G.3;',11)
put(ax,.04,.49,'this lesson, 6.0E/H/I, 6.0K.2/K.6 and 6.0P.2/P.5.',11)
put(ax,.04,.37,'Free human context: J. S. Milne, Algebraic Number Theory,',11)
put(ax,.04,.29,'Proposition 2.43; Proposition 7.55 and Remark 7.56.',11)
put(ax,.04,.21,'https://www.jmilne.org/math/CourseNotes/ANT.pdf',10,blue)
put(ax,.04,.12,'Ten-point exercise and complete solution accompany these formulas.',10)

fig.text(.055,.020,'Coordinates are schematic; the valuation panel is a labelled lemma illustration.',fontsize=10,color=ink)
fig.text(.055,.014,'This map explains the proof. It does not replace the complete argument or its hypotheses.',fontsize=10,color=ink)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
for artist in texts:
    box=artist.get_window_extent(renderer)
    axis_box=artist.axes.get_window_extent(renderer)
    assert box.x0>=axis_box.x0-1 and box.x1<=axis_box.x1+1,(artist.get_text(),'horizontal text exceeds panel')
    assert box.y0>=axis_box.y0 and box.y1<=axis_box.y1,(artist.get_text(),'vertical text exceeds panel')
out=base.parent/'assets/uniform-odd-second-II-star-proof-map.png'
fig.savefig(out,dpi=100,facecolor=fig.get_facecolor())
plt.close(fig)
digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
print(json.dumps({'image':out.name,'image_sha256':digest(out),'panels':8}))

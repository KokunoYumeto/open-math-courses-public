"""Two exact coordinate examples for PS and BI, independent CC0 diagram."""
from pathlib import Path
import sys,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'svg.hashsalt':'SH02-stronger-analytic-20261009'})
blue='#2167a2';purple='#7143a0';red='#b5263a';grey='#52606b'

def polar(ax):
    g=np.linspace(-.7,.7,31);xx,yy=np.meshgrid(g,g)
    ax.plot_surface(xx,yy,0*xx,color='#b8cddc',alpha=.5,edgecolor='none')
    t=np.linspace(-.85,.85,100)
    ax.plot(0*t,0*t,t,color=blue,lw=4)
    ax.scatter([0],[0],[0],color=red,s=55,depthshade=False)
    ax.text(.07,.07,.05,'[0:0:1:0]',color=red,fontsize=9)
    ax.text(.33,-.6,.04,'L₂: ξ₄ = 0',color=grey,fontsize=10)
    ax.text(.05,.05,.7,'F: ξ₁ = ξ₂ = 0',color=blue,fontsize=9)
    ax.set_xlim(-.8,.8);ax.set_ylim(-.8,.8);ax.set_zlim(-.9,.9)
    ax.set_xlabel('Re(ξ₁/ξ₃)',labelpad=7)
    ax.set_ylabel('Re(ξ₂/ξ₃)',labelpad=7)
    ax.set_zlabel('Re(ξ₄/ξ₃)',labelpad=7)
    ax.view_init(elev=22,azim=-52)
    ax.set_title('Conormal fibre in one projective chart',fontweight='bold',pad=17)
    ax.text2D(.5,-.19,'H = {z₃ = z₄ = 0} ⊂ ℂ⁴; d = 2; dim F = 1.\n'
      'k = 0: ℓ = 1, L₂ meets F ⇒ P₀ = H.\n'
      'k = 1: ℓ = 2, L₁ = {ξ₃ = ξ₄ = 0} misses F ⇒ P₁ is empty.',
      transform=ax.transAxes,ha='center',va='top',fontsize=9,color=grey)

def integral(ax):
    theta=np.linspace(0,np.pi,150)
    rr=np.linspace(-1,1,100)
    r,t=np.meshgrid(rr,theta)
    u1=r*np.cos(t)**2;u2=r*np.sin(t)**2;w=r*np.cos(t)*np.sin(t)
    ax.plot_surface(u1,u2,w,color=purple,alpha=.58,edgecolor='none')
    z=np.linspace(-.9,.9,100)
    ax.plot(0*z,0*z,z,color=red,lw=2,ls='--')
    ax.scatter([0],[0],[0],color=grey,s=24,depthshade=False)
    ax.text(.06,.06,.77,'vertical direction\n[0:0:1] is excluded',color=red,fontsize=9)
    ax.set_xlim(-1,1);ax.set_ylim(-1,1);ax.set_zlim(-1,1)
    ax.set_xlabel('u₁',labelpad=7);ax.set_ylabel('u₂',labelpad=7);ax.set_zlabel('w',labelpad=7)
    ax.view_init(elev=23,azim=-48)
    ax.set_title('Cone over the exceptional fibre',fontweight='bold',pad=17)
    ax.text2D(.5,-.19,'g₁ = x², g₂ = y², F = xy; |F| ≤ max(|g₁|, |g₂|).\n'
      'Cone: w² − u₁u₂ = 0.  The coefficient of w² is 1.\n'
      'Substitution: F² − g₁g₂ = 0, with −g₁g₂ ∈ (g₁,g₂)².',
      transform=ax.transAxes,ha='center',va='top',fontsize=9,color=grey)

def draw(mobile):
    fig=plt.figure(figsize=(7.8,13.6) if mobile else (15.8,8.1))
    if mobile:
        a1=fig.add_subplot(211,projection='3d');a2=fig.add_subplot(212,projection='3d')
        fig.subplots_adjust(left=.02,right=.98,top=.79,bottom=.20,hspace=.65)
    else:
        a1=fig.add_subplot(121,projection='3d');a2=fig.add_subplot(122,projection='3d')
        fig.subplots_adjust(left=.03,right=.97,top=.75,bottom=.32,wspace=.12)
    polar(a1);integral(a2)
    title='Exact projective sections and integral equations'
    fig.suptitle(title if not mobile else 'Exact projective sections\nand integral equations',
                 y=.975,fontweight='bold',fontsize=16 if not mobile else 15)
    fig.text(.5,.89 if mobile else .88,
      'Left: real section of the chart ξ₃ = 1 in ℙ³; L₁ lies outside this chart.\n'
      'Right: real section over (x,y) = 0 of w² = u₁u₂.\n'
      'The plotted extents are display windows, not mathematical bounds.',
      ha='center',va='top',fontsize=10,color=grey)
    foot=('PS: dim R = d−k, dim bad ≤ d−k−1 ⇒ dense regular part ⇒ κ(R) = Pₖ.\n'
          'Pₖ is empty exactly when dim C₀ < N−1−d+k.\n'
          'BI: missing vertical vertex ⇒ a homogeneous equation\nwith unit pure-F coefficient ⇒ an actual integral equation.\n'
          'Proof: PS0–PS4 and BI1–BI3. Independent CC0 diagram.') if mobile else (
          'PS: dim R = d−k, dim bad ≤ d−k−1 ⇒ dense regular part ⇒ κ(R) = Pₖ; Pₖ is empty exactly when dim C₀ < N−1−d+k.\n'
          'BI: missing vertical vertex ⇒ homogeneous equation with unit pure-F coefficient ⇒ actual integral equation. Proof: PS0–PS4 and BI1–BI3.')
    fig.text(.5,.035 if mobile else .06,foot,ha='center',va='bottom',fontsize=9,color=grey)
    stem=OUT/('stronger-analytic-mobile' if mobile else 'stronger-analytic-wide')
    fig.savefig(stem.with_suffix('.svg'),metadata={'Date':None,'Creator':'Independent CC0 mathematical diagram'})
    fig.savefig(stem.with_suffix('.png'),dpi=180,metadata={'Software':'Independent CC0 mathematical diagram'})
    fig.savefig(stem.with_suffix('.pdf'),metadata={'CreationDate':None,'ModDate':None,'Creator':'Independent CC0 mathematical diagram'})
    plt.close(fig)

draw(False);draw(True)
(OUT/'stronger-analytic-math.md').write_text('''# Exact mathematical coordinates

Independent CC0 diagrams for [the polar-section and integral-equation proofs](../polar-sections-and-lipschitz-algebras.html). The pictures show exact examples of the general mechanisms; the full proofs remain alongside them.

Left: H={z3=z4=0} in C4 is reduced pure of complex dimension d=2 in N=4, meeting the original N>=d+2 requirement. Its conormal fibre F={xi1=xi2=0} is P1 in P3. In the chart xi3=1, the displayed real section has Im xi1=Im xi2=Im xi4=0; F is (0,0,xi4), and L2={xi4=0} is the displayed plane. Their entire complex intersection is [0:0:1:0]. The extra point of F at infinity is not displayed. For k=0, ell=N-1-d+k=1, p0(z)=(z1,z2,z3), rank(p0|TH)=2<3, so P0=H. For k=1, L1={xi3=xi4=0} lies outside this affine chart and is disjoint from F: combining its equations with F would make all four homogeneous coordinates zero. The projection p1(z)=(z1,z2) has full rank 2 on H, so P1 is empty. dim F=1 is respectively >=ell and <ell. This is the exact fibre threshold, not a Euclidean intersection estimate for arbitrary planes.

Right: I=(x^2,y^2), F=xy, with C=1 in |F|<=max(|x|^2,|y|^2). The actual projective graph [x^2:y^2:xy] has exceptional image the conic v3^2=v1 v2 in P2. Its tautological affine cone is w^2=u1u2. The plotted real section is parametrized by (u1,u2,w)=(r cos^2 theta,r sin^2 theta,r cos theta sin theta), theta in [0,pi], r in [-1,1]. The finite r interval is a display window, not a bound on the full cone. The vertical projective point [0:0:1] violates its equation and is excluded; its zero vector remains the cone vertex. The homogeneous equation has unit coefficient 1 on w^2. Substituting (u1,u2,w)=(x^2,y^2,xy) gives F^2-g1g2=0, with a1=0 in I and a2=-g1g2 in I^2. It is an actual ideal integral equation, not merely an equation with arbitrary coefficients.

General proof locators: PS1/PS2 actual compact-fibre generic flag and jump-image density; PS3 proper polar image; PS4 full fibre threshold. BI1 missing projective vertex; BI2 proper tautological-cone image; BI3 homogeneous Taylor extraction with the exact I^j coefficient powers. Human antecedents retained in those proof bodies: Teissier, Varietes polaires II, IV.4.1.1 and IV.6.1.1(a), pp.432–433 and 451; Demailly, Complex Analytic and Differential Geometry, II.5.4/II.5.9, II.6.2 and II.8.8, for actual closures, compact affine finiteness, one-equation purity and general proper analytic images. No protected source prose or figure is copied.
''',encoding='utf-8')
print('Rendered seven reproducible outputs for the exact projective/cone examples.')

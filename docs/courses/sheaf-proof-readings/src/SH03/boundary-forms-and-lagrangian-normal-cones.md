# Boundary forms and Lagrangian normal cones

The normal cone records how a set approaches a submanifold after its transverse displacement is rescaled. Along a positive-conic analytic Lagrangian submanifold, the symplectic form identifies that normal bundle with a cotangent bundle. An isotropic set then has an isotropic normal cone. The proof rests on an analytic boundary calculation: a form of the shape \(t a+b\,dt\) that vanishes on an approaching subanalytic set forces both the tangential part of \(a\) and the scalar \(b\) to vanish at the boundary.

All manifolds and maps in this lesson are real analytic, finite dimensional, Hausdorff and countable at infinity. Let \(X\) have dimension \(n\), put \(P=T^*X\), and use

\[
\alpha=\sum_i\xi_i dx_i,\qquad \omega=d\alpha.
\tag{1}
\]

The proof uses the following programme results.

- The [analytic deformation construction](../SH02/normal-geometry.md#sh02-ng-construction--the-deformation-manifold-and-its-maps) and [signed normal-cone convention](subanalytic-sets-and-limiting-tangent-directions.md#the-signed-normal-cone-prerequisite) identify the central cone with the closure of the positive lift, including zero normal vectors.
- [Proper analytic uniformization](subanalytic-sets-and-limiting-tangent-directions.md#a-locally-finite-assembly-with-a-fixed-source-dimension) maps a smooth analytic manifold properly onto each closed subanalytic set. Its locally finite construction covers the countable-at-infinity, possibly noncompact case used here.
- The [singular one-form criterion](subanalytic-sets-and-limiting-tangent-directions.md#one-forms-on-a-singular-set) and [pullback, closure and surjective-detection rules](subanalytic-sets-and-limiting-tangent-directions.md#analytic-maps-and-locally-finite-unions) interpret vanishing on all limiting tangent vectors. Their set-theoretic inputs are the [local subanalytic calculus](subanalytic-sets-and-limiting-tangent-directions.md#the-local-calculus-with-the-precise-properness-hypothesis), [intrinsic regular-locus theorem](subanalytic-sets-and-limiting-tangent-directions.md#every-intrinsic-regular-point-in-each-dimension) and [analytic curve-selection construction](subanalytic-sets-and-limiting-tangent-directions.md#from-a-local-analytic-presentation-to-analytic-curve-selection).
- The optional second boundary proof also uses [proper function resolution](subanalytic-sets-and-limiting-tangent-directions.md#from-finite-local-towers-to-the-global-function-resolution), with a signed monomial expression near the resolved zero set.

The main boundary calculation uses analytic Taylor expansion on the uniformizing smooth source. No coefficient ring occurs here. We prove the normal-cone theorem in adapted analytic coordinates along a general **positive-conic** analytic Lagrangian; no contact normal-form reduction is required.

Kashiwara and Schapira, [*Micro-hyperbolic systems*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/Microhyp.pdf), Acta Mathematica 142 (1979), §§10.2–10.5, printed pp. 49–52, supply the classical boundary-form and first-normal-form methods. Proposition 10.4.1 gives boundary vanishing, Proposition 10.5.1 gives the canonical-form identity, and Theorem 10.5.2 states the homogeneous Lagrangian-input application. The proof below treats the stated positive-conic subanalytic isotropic input and includes the possible zeroes of the Euler field.

<a id="boundary-vanishing"></a>
<a id="vanishing-at-a-boundary-approached-from-its-complement-boundary-vanishing"></a>

## Vanishing at a boundary approached from its complement

Work locally on an analytic product with coordinates \((x,t)\), and let \(Y=\{t=0\}\). Suppose \(Z\) is subanalytic and

\[
Z\subset\overline{Z\setminus Y}.
\tag{2}
\]

Let \(a\) be an analytic one-form and \(b\) an analytic function. Set

\[
\theta=t a+b\,dt.
\tag{3}
\]

If \(\theta|_Z=0\), then

\[
a|_{Z\cap Y}=0,\qquad b|_{Z\cap Y}=0.
\tag{4}
\]

The first equality is tangential one-form vanishing; the second is pointwise function vanishing. No regularity of \(Z\cap Y\) is assumed.

**Proof.** We can replace \(Z\) by its closure. Vanishing of \(\theta\) passes to that closure by the one-form cone criterion, and (2) implies that this closed set is still the closure of its part off \(Y\). A conclusion on its boundary implies (4) for the original set.

By uniformization choose a proper analytic \(f:M\to X\) with image this closed \(Z\). Put \(h=t\circ f\). Discard the connected components on which \(h\) is identically zero. The remaining union \(M_1\) is open and closed in \(M\), so the restricted map is still proper. Its image is closed and contains \(Z\setminus Y\), because a preimage of a point with nonzero \(t\) cannot be on a discarded component. Density in (2) therefore makes its image all of \(Z\). This argument explains why a whole boundary component upstairs can be discarded without losing the boundary downstairs.

<a id="analytic-boundary-without-function-resolution"></a>
<a id="the-smooth-source-calculation-analytic-boundary-without-function-resolution"></a>

### The smooth-source calculation

Retain the proper analytic uniformization \(f:M_1\to X\) onto the closed set \(Z\), after discarding components on which \(t\circ f\) is identically zero. Put

\[
h=t\circ f,\qquad A=f^*a,\qquad B=b\circ f,\qquad
D=\{h=0\}.
\quad
hA+B\,dh=0.
\tag{BF1}
\]

The last equality is an equality of analytic one-forms on the smooth manifold \(M_1\), by the singular one-form pullback rule. The analytic function \(h\) has a nonzero germ at every point of \(M_1\): otherwise the analytic identity theorem would make it identically zero on that point's connected component.

We first prove \(B=0\) at every point of \(D\). Fix \(p\in D\), choose analytic coordinates centred at \(p\), and let \(m\ge1\) be the degree of the first nonzero homogeneous Taylor term of \(h\) at \(p\). Choose a real vector \(v\) on which this nonzero homogeneous polynomial does not vanish. Along the analytic line \(c(s)=p+sv\), write \(c^*A=\alpha(s)\,ds\). Then

\[
h(c(s))=s^m u(s),\qquad u(0)\ne0,\qquad
s\,u(s)\alpha(s)
+B(c(s))\bigl(m u(s)+s u'(s)\bigr)=0.
\tag{BF2}
\]

The second equality follows from (BF1) by division by \(s^{m-1}\) for \(s\ne0\), followed by analytic continuation to zero. Evaluation at zero gives \(m u(0)B(p)=0\). Hence \(B(p)=0\).

We now prove tangential vanishing of \(A\) on every analytic submanifold \(N\) contained in \(D\). This stronger intermediate statement includes submanifolds inside the singular locus. Work in a connected coordinate product with coordinates \((x,y)\) in which \(N=\{y=0\}\). A zero-dimensional \(N\) makes no tangential demand. If the normal coordinate group were empty, \(h\) would vanish on an ambient open set, contrary to the nonzero-germ assertion.

Expand in the normal coordinates:

\[
h(x,y)=\sum_{\nu\in\mathbb N^q}h_\nu(x)y^\nu,\qquad
r=\min\{|\nu|:h_\nu\text{ is not identically zero}\}\ge1,
\qquad
h_r(x,y)=\sum_{|\nu|=r}h_\nu(x)y^\nu .
\tag{BF3}
\]

These coefficients are analytic on the connected \(x\)-coordinate neighborhood, after shrinking the coordinate product if necessary. The minimum exists because \(h\) is not identically zero. It is a minimum for coefficient functions on this neighborhood, not a claim that the pointwise normal order is constant.

Let \(I=(y_1,\ldots,y_q)\). Taylor expansion and termwise differentiation give

\[
h\in I^r,\qquad \partial_{x_i}h\in I^r,\qquad B\in I,
\qquad
hA_i=-B\,\partial_{x_i}h\in I^{r+1},
\tag{BF4}
\]

where \(A_i\) is the coefficient of \(dx_i\) in \(A\). Here \(B\in I\) follows from the already proved equality \(B(x,0)=0\), by analytic Taylor expansion. Taking the homogeneous part of normal degree \(r\) yields

\[
h_r(x,y)A_i(x,0)=0,
\qquad\text{hence}\qquad
A_i(x,0)=0.
\tag{BF5}
\]

Indeed some coefficient \(h_\nu(x)\), with \(|\nu|=r\), is not identically zero. Its nonzero set is dense by the analytic identity theorem. The corresponding coefficient equation \(h_\nu(x)A_i(x,0)=0\) gives vanishing on that dense set, and continuity gives vanishing everywhere. This also covers points where the normal order jumps.

Thus \(A|_N=0\). Apply this to the local analytic submanifolds constituting \(D_{\mathrm{reg}}\). By the definition of singular one-form vanishing, \(A|_D=0\); the already proved one-form cone criterion then includes every point of \(D\), with its actual limiting tangent vectors. No assertion that the ambient covector \(A_p\) vanishes is made.

The map \(f\) is onto \(Z\), so \(f(D)=Z\cap Y\). The pointwise equality \(B=0\) on \(D\) gives \(b=0\) on \(Z\cap Y\). Surjective one-form detection, applied to the analytic map \(f\) and the exact subanalytic sets \(D\) and \(Z\cap Y\), gives \(a|_{Z\cap Y}=0\). This proves both conclusions of the boundary lemma.

For the identity theorem used here, the set where an analytic function has zero germ is open. It is also closed: at a limit of such points every derivative vanishes by continuity, so the convergent Taylor series is zero near the limit. On a connected component this set is therefore empty or the whole component. This proves both the nonzero-germ assertion and density of the nonzero set of a non-identically-zero analytic coefficient.

This calculation uses analytic coordinates, convergent Taylor expansion, the identity theorem proved above, and the linked singular one-form calculus. It requires no further resolution of the uniformizing source. The construction of proper uniformization in the programme uses function resolution; the direct calculation therefore does not assert resolution independence of the full prerequisite chain.

<a id="boundary-monomial-alternative"></a>
<a id="an-alternative-through-monomial-resolution-boundary-monomial-alternative"></a>

### An alternative through monomial resolution

The direct argument above has proved the boundary lemma. The following useful alternative records precisely what the additional normal-crossing resolution input supplies.

On every component of \(M_1\), \(h\) is not identically zero. Resolve it by the stated monomial-resolution prerequisite. At a regular zero the analytic inverse-function theorem gives the same local coordinate description. After composing with the proper resolution map, we have a proper analytic map \(g:\widetilde M\to X\), still onto \(Z\), such that near every point of \(D=g^{-1}Y\),

\[
t\circ g=\varepsilon\prod_{j=1}^{r}u_j^{m_j},
\qquad \varepsilon\in\{1,-1\},\quad m_j>0.
\tag{5}
\]

Coordinates with exponent zero are omitted from the product. The resolution map is onto: its proper image is closed and contains the dense open set on which it is an isomorphism. The zero set \(D\) in these coordinates is \(\bigcup_{j=1}^r\{u_j=0\}\).

Write \(A=g^*a\) and \(B=b\circ g\). Analytic pullback gives

\[
(t\circ g)A+B\,d(t\circ g)=0.
\tag{6}
\]

Off \(D\), divide by the nonzero monomial:

\[
A=-B\sum_{j=1}^r\frac{m_j}{u_j}\,du_j.
\tag{7}
\]

If \(A=\sum_j A_jdu_j\), comparison and analytic continuation give

\[
u_j A_j+m_j B=0\quad(j\le r),
\qquad A_j=0\quad(j>r).
\tag{8}
\]

Each \(u_j\) divides \(B\) in the analytic local ring. Equivalently, in its convergent power series every nonzero term has positive exponent in every one of \(u_1,\ldots,u_r\). Thus

\[
B=\left(\prod_{j=1}^r u_j\right)C,
\qquad
A_j=-m_j\left(\prod_{k\ne j,\ k\le r}u_k\right)C
\quad(j\le r),
\tag{9}
\]

for an analytic \(C\). In particular \(B\) is zero on \(D\). On the hyperplane \(u_i=0\), all tangential coefficients \(A_j\), \(j\ne i\), vanish. Hence \(A\) restricts to zero on every such hyperplane, and therefore on their finite subanalytic union \(D\). This includes its intersections through the singular one-form calculus.

Since \(g(D)=Z\cap Y\), pointwise vanishing of \(B\) proves pointwise vanishing of \(b\) there. Surjective one-form detection on this exact subanalytic source and target turns \(g^*a|_D=0\) into \(a|_{Z\cap Y}=0\). This proves both assertions. \(\square\)

The factors in (9) establish tangential vanishing. They do not assert that the ambient one-form \(a\) itself is the zero covector at every boundary point.

## The cotangent identification and its sign

Let \(L\subset P\) be a smooth embedded real analytic positive-conic Lagrangian submanifold, locally closed. Since \(\dim L=n\) and \(\omega|_{TL}=0\), the normal bundle

\[
N_LP=(TP|_L)/TL
\tag{10}
\]

has the intrinsic analytic identification

\[
K:N_LP\longrightarrow T^*L,\qquad
K([w])(v)=\omega(w,v)\quad(v\in TL).
\tag{11}
\]

Adding a vector of \(TL\) to \(w\) leaves this value unchanged. The kernel on \(TP|_L\) is \((TL)^\omega=TL\), so (11) is an isomorphism.

Retain the Hamiltonian convention

\[
H(a\,dx+b\,d\xi)=b\partial_x-a\partial_\xi,
\qquad\iota_{H\theta}\omega=-\theta.
\tag{12}
\]

The inverse of (11) is the map induced by \(-H\): extend \(\beta\in T^*L\) to \(\theta\in T^*P|_L\), and send it to \([-H\theta]\). Two extensions differ by the conormal of \(L\); \(H\) takes that conormal to \(TL\), so the quotient class is independent of the extension. Also \(\omega(-H\theta,v)=\theta(v)=\beta(v)\), proving the sign.

The Euler field \(R=\sum_i\xi_i\partial_{\xi_i}\) is tangent to \(L\), by positive conicity. Since \(\iota_R\omega=\alpha\), isotropy of \(TL\) gives \(\alpha|_{TL}=0\). Thus \(\alpha\) defines a fibrewise linear function

\[
\ell([w])=\alpha(w)\quad\text{on }N_LP.
\tag{13}
\]

Under (11),

\[
\ell([w])=-K([w])(R|_L).
\tag{14}
\]

Consequently its zero set is the set of covectors on \(L\) annihilating its Euler vector. At a zero of the Euler field this kernel is the whole cotangent fibre; a codimension-one assertion there is not intended.

## First order of the canonical form on the deformation

Choose adapted analytic coordinates \((y,z)\) on \(P\), with \(L=\{z=0\}\); both groups have \(n\) coordinates. Write

\[
\alpha=\sum_i A_i(y,z)dy_i+\sum_j B_j(y,z)dz_j,
\qquad A_i(y,0)=0.
\tag{15}
\]

In its normal-deformation chart \((y,v,t)\), the map to \(P\) is \(q(y,v,t)=(y,tv)\). Direct substitution gives

\[
q^*\alpha=t a+b\,dt,
\tag{16}
\]

where

\[
a=\sum_i\frac{A_i(y,tv)}{t}dy_i+
\sum_j B_j(y,tv)dv_j,
\qquad
b=\sum_j B_j(y,tv)v_j.
\tag{17}
\]

The quotient in (17) extends analytically at \(t=0\), because its analytic numerator vanishes identically when \(t=0\). Denote the restrictions to the central fibre by \(a_0,b_0\). The scalar is exactly \(b_0=\ell\). The coefficients of (11) in these coordinates are

\[
\beta_i=
\sum_j v_j\left(\partial_{z_j}A_i(y,0)-\partial_{y_i}B_j(y,0)\right).
\tag{18}
\]

Indeed evaluate \(d\alpha\) on the normal representative \(\sum_jv_j\partial_{z_j}\) and the tangent vector \(\partial_{y_i}\). If \(\lambda_L\) is the canonical one-form on \(T^*L\), then \(K^*\lambda_L=\sum_i\beta_i dy_i\). Differentiating \(\ell=\sum_jB_j(y,0)v_j\) and using (18) yields the crucial identity

\[
a_0=K^*\lambda_L+d\ell.
\tag{19}
\]

Both the minus sign in (18) and the exact differential in (19) matter. The first-order form \(a_0\) need not itself be the canonical form on the cotangent normal bundle.

<a id="lagrangian-normal-cone-isotropy"></a>
<a id="the-full-lagrangian-normal-cone-theorem-lagrangian-normal-cone-isotropy"></a>

## The full Lagrangian normal-cone theorem

Let \(S\subset T^*X\) be a positive-conic subanalytic isotropic set, and let \(L\) be as above. Under (11),

\[
K\bigl(C_L(S)\bigr)\subset T^*L
\text{ is subanalytic, positive-conic and isotropic},
\tag{20}
\]

and

\[
C_L(S)\subset\{\ell=0\}.
\tag{21}
\]

**Proof.** Everything is local along \(L\); choose an ambient open set where it is closed. In its analytic deformation, put

\[
Z=\overline{q^{-1}(S)\cap\{t>0\}}.
\tag{22}
\]

The normal-deformation prerequisite gives

\[
C_L(S)=Z\cap\{t=0\}.
\tag{23}
\]

The lifted set and its closure are subanalytic, so the cone is subanalytic. It is positive-conic in its normal fibres by the deformation action \((y,v,t)\mapsto(y,cv,t/c)\), \(c>0\). The analytic linear bundle isomorphism \(K\) preserves these properties.

Analytic pullback of \(\alpha|_S=0\) gives \(q^*\alpha=0\) on the lifted positive set. Closure preserves this one-form vanishing, so \(q^*\alpha|_Z=0\). Moreover \(Z\) is the closure of its part with \(t\ne0\), because its defining positive lift is contained in that part and dense in \(Z\). Apply the boundary theorem to (16). It gives

\[
a_0|_{C_L(S)}=0,\qquad
\ell|_{C_L(S)}=0.
\tag{24}
\]

The second statement proves (21). Because \(\ell\) is identically zero as a function on this subanalytic set, its differential restricts to zero on its regular locus. Equation (19) now gives

\[
K^*\lambda_L|_{C_L(S)}=0.
\tag{25}
\]

Transport through the analytic isomorphism \(K\) proves canonical-form isotropy on its image, which is (20). All points of the cone, including zero normal vectors and those over limits of \(S\), are included. \(\square\)

The proof applies to a general positive-conic analytic Lagrangian. It keeps both normal-fibre positive scaling and the original cotangent Euler constraint; these are different operations. Its closure in (22) is the closure of the positive lift, rather than a literal inverse image on the central fibre.

## The fibre model makes the sign visible

Take \(L=T_0^*\mathbb R^n=\{x=0\}\). A normal vector has coordinates \((\xi;v)\), where \(v\) is the normal \(x\)-displacement. Formula (11) becomes

\[
K(\xi;v)=(\xi;-v\,d\xi),\qquad
\ell(\xi;v)=\langle\xi,v\rangle.
\tag{26}
\]

The canonical form after transport is \(-\sum_i v_i d\xi_i\). In the deformation \(x=tv\),

\[
q^*\alpha=t\sum_i\xi_i dv_i+\langle\xi,v\rangle dt,
\qquad
\sum_i\xi_i dv_i
=-\sum_i v_i d\xi_i+d\langle\xi,v\rangle.
\tag{27}
\]

This is (19) in the model used for many cotangent computations. The boundary calculation first gives the two vanishings in (24); subtracting the exact differential then produces the correctly signed canonical form.

## Exercises with complete solutions

### The off-boundary density hypothesis is essential

*Difficulty: Introductory.*

On \(\mathbb R_x\times\mathbb R_t\), take \(Z=Y=\{t=0\}\), \(a=dx\) and \(b=1\). Test the conclusion (4) for \(\theta=t\,dx+dt\). Explain which hypothesis fails.

**Solution.** On the smooth \(Z\), both \(t\) and the tangential pullback of \(dt\) vanish, so \(\theta|_Z=0\). But \(a|_Z=dx\ne0\), and \(b|_Z=1\ne0\). Here \(Z\setminus Y=\varnothing\), whose closure does not contain \(Z\); hypothesis (2) fails. One-form vanishing on a set wholly in the boundary cannot detect either the lost factor of \(t\) or the coefficient of its normal differential.

### A boundary one-form may retain a normal covector

*Difficulty: Introductory.*

Let \(Z=\mathbb R^{m}_x\times\mathbb R_t\), \(a=dt\), \(b=-t\). Verify the boundary theorem and compare tangential with ambient vanishing of \(a\).

**Solution.** Equation (3) gives \(\theta=t\,dt-t\,dt=0\) identically. The complement of \(t=0\) is dense in \(Z\), so (2) holds. At the boundary, \(b=0\), and the pullback of \(a=dt\) to \(\{t=0\}\) is zero. Its ambient covector \(dt\) remains nonzero. Thus both conclusions of (4) hold with precisely their different meanings.

### A positive support ray becomes a negative cotangent ray

*Difficulty: Intermediate.*

In \(T^*\mathbb R\), take \(L=T_0^*\mathbb R\) and \(S=\{(x;0):x\ge0\}\). Compute the normal cone and its image under \(K\). Verify (20)–(21).

**Solution.** The deformation is \(q(v,\xi,t)=(tv;\xi)\). In the positive chamber the inverse image of \(S\) is \(\{v\ge0,\xi=0,t>0\}\). Its central closure is

\[
C_L(S)=\{(\xi;v):\xi=0,v\ge0\}.
\tag{28}
\]

Formula (26) sends it to \(\{(0;\eta\,d\xi):\eta\le0\}\subset T^*L\). This is subanalytic and positive-conic in the new cotangent fibres. Its regular part is a vertical ray, where \(\eta\,d\xi\) restricts to zero; hence it is isotropic. Also \(\ell=\xi v=0\). The sign is detectable because the normal cone is a single ray, not a sign-symmetric vector subspace. Involutivity of \(S\) is not needed for this theorem.

### A literal central inverse image gives the wrong cone

*Difficulty: Intermediate.*

For \(L=T_0^*\mathbb R\) and \(S=\{(0;\xi):\xi>0\}\), compare \(C_L(S)\) with the literal inverse image of \(S\) under \(q|_{t=0}\).

**Solution.** For \(t>0\), membership \((tv;\xi)\in S\) means \(v=0\) and \(\xi>0\). Its closure on the central fibre gives

\[
C_L(S)=\{v=0,\xi\ge0\}.
\tag{29}
\]

The literal central map is \(q(v,\xi,0)=(0;\xi)\), so its inverse image of \(S\) is \(\{\xi>0,\ v\text{ arbitrary}\}\). It both omits the zero-base limit in (29) and adds unwanted normal vectors. The transported actual cone is the zero section of \(T^*L\) over \(\xi\ge0\), isotropic and with \(\ell=0\). The definition must therefore retain the positive lift and its closure.

### The normal cone of a curved conormal at a fibre

*Difficulty: Advanced.*

Let \(N=\{(u,u^2):u\in\mathbb R\}\subset\mathbb R^2\), \(S=T_N^*\mathbb R^2\), and \(L=T_{(0,0)}^*\mathbb R^2\). Compute \(C_L(S)\) and identify its transported image as a conormal in \(T^*L\).

**Solution.** Write covectors \((\xi_1,\xi_2)=(-2ub,b)\). In the deformation \(x=t v\), the positive lift satisfies

\[
u=tv_1,\qquad v_2=t v_1^2,\qquad
\xi_1=-2t v_1 b,\qquad \xi_2=b.
\tag{30}
\]

Any convergent tuple as \(t\downarrow0\) has bounded \(v_1\) and \(b\), giving \(v_2=0\) and \(\xi_1=0\) in the limit. Conversely, each finite pair \((v_1,b)\) is realized by (30). Thus the cone is exactly \(\{v_2=0,\xi_1=0\}\), with \(v_1,\xi_2\) arbitrary. Under \(K\), \(\eta_i=-v_i\), so it becomes \(\{\xi_1=0,\eta_2=0\}\). This is the conormal of the line \(\{\xi_1=0\}\subset L\): the covector is a multiple of \(d\xi_1\). Also \(\ell=\xi_1v_1+\xi_2v_2=0\). The curved relation in (30) has the same finite first-order normal limit as its tangent line, while retaining the limiting cotangent base condition \(\xi_1=0\).

### Recover the general first-order identity

*Difficulty: Advanced.*

Starting from (15), compute \(a_0\), \(d\ell\) and \(K^*\lambda_L\), and verify (19). Explain why \(a_0|_C=0\) alone would not prove isotropy of a subanalytic \(C\subset N_LP\).

**Solution.** Analytic differentiation at zero gives

\[
a_0=\sum_{i,j}\partial_{z_j}A_i(y,0)v_jdy_i+\sum_jB_j(y,0)dv_j.
\tag{31}
\]

The differential of \(\ell=\sum_jB_j(y,0)v_j\) is

\[
d\ell=\sum_{i,j}\partial_{y_i}B_j(y,0)v_jdy_i+\sum_jB_j(y,0)dv_j.
\tag{32}
\]

Subtracting (32) from (31) leaves the coefficients in (18), hence \(a_0-d\ell=K^*\lambda_L\). Merely knowing \(a_0|_C=0\) would give \(K^*\lambda_L|_C=-d\ell|_C\), which need not be zero. The boundary theorem supplies \(\ell|_C=0\) as a function, so its differential also restricts to zero. This is why both boundary conclusions, rather than just the form conclusion, enter the normal-cone theorem.

<a id="boundary-normal-order-jump"></a>
<a id="a-normal-order-that-jumps-boundary-normal-order-jump"></a>

### A normal order that jumps

*Difficulty: Advanced.*

On \(\mathbb R^2_{x,y}\), put

\[
h=y^2(x^2+y^2),\qquad B=y(x^2+y^2),\qquad
A=-2xy\,dx-(2x^2+4y^2)\,dy.
\tag{BF6}
\]

Verify \(hA+B\,dh=0\). Determine the zero set of \(h\), the normal order of \(h\) along that set, and the tangential and ambient restrictions of \(A\). Explain why the direct proof handles the order jump.

**Solution.** Differentiation gives \(dh=2xy^2\,dx+(2x^2y+4y^3)\,dy\). The coefficient of \(dx\) in \(hA\) is \(-2xy^3(x^2+y^2)\), while its coefficient in \(B\,dh\) is \(2xy^3(x^2+y^2)\). The coefficients of \(dy\) are respectively \(-2y^2(x^2+y^2)(x^2+2y^2)\) and \(2y^2(x^2+y^2)(x^2+2y^2)\). Both pairs cancel.

Since \(x^2+y^2\) is positive except at the origin, the real zero set is exactly \(D=\{y=0\}\). The expansion \(h=x^2y^2+y^4\) has normal order two at every point \((x,0)\) with \(x\ne0\), and order four at the origin. On any connected \(x\)-interval containing zero, however, the smallest normal degree with a non-identically-zero coefficient function is two: that coefficient is \(x^2\). Thus (BF3) takes \(r=2\), without falsely requiring the pointwise order to be constant.

On \(D\), \(B=0\) and the ambient covector \(A\) is \(-2x^2\,dy\). It need not be zero away from the origin, but it annihilates the tangent line spanned by \(\partial_x\); therefore \(A|_D=0\) in the required tangential sense. The coefficient argument first proves the tangential equality where \(x^2\ne0\), and continuity supplies the origin. Also \(B/h=1/y\) off \(D\), so dividing \(B\) by the entire function \(h\) would not be an analytic operation.

<a id="boundary-source-and-foundations"></a>
<a id="source-methods-and-proof-inputs-boundary-source-and-foundations"></a>
<a id="source-comparison-and-exact-foundation-boundary"></a>
<a id="source-comparison-and-exact-foundation-boundary-boundary-source-and-foundations"></a>

## Source methods and proof inputs

Proposition 10.4.1 of the cited paper uses proper uniformization followed by a generic-power calculation. Here the least nonzero normal degree is taken over analytic coefficient functions on each connected coordinate chart. It proves tangential vanishing on every analytic submanifold of the zero set, and continuity includes points where that normal degree jumps. The monomial calculation gives a second proof after resolving the function on the smooth source.

The paper uses its Hamiltonian map to identify the normal bundle with a cotangent bundle. With convention (12), the inverse of (11) is induced by minus that map. The adapted-coordinate calculation (18)–(19) retains the exact differential; the fibre model and sixth solved check verify its sign. Subtracting that differential after both boundary vanishings proves the isotropic-input statement here.

The boundary lemma uses proper uniformization and singular one-form detection with their stated hypotheses. In the latter proof, the full smooth Sard theorem and dense regular lifts apply to the induced surjection between manifolds with countable atlases; they require neither compactness nor properness of that surjection. The exact subanalytic set, regularity and curve-selection inputs, and the extra resolution input of the alternative, are supplied by the programme sections linked at the beginning.

<span id="the-limiting-operation-consequence-to-develop"></span>

## Limiting-operation consequences

The normal-cone theorem supplies the cotangent isotropy needed for limiting fibre sums and characteristic inverse images. Their exact diagonal and graph slices are proved in [Limiting cotangent sums and characteristic inverse images](limiting-cotangent-sums-and-characteristic-inverse-images.md#isotropy-of-the-full-limiting-sum-limiting-sum-isotropy). The theorem here retains the intrinsic \(-H\) identification, the canonical-form kernel constraint and the full general positive-conic analytic Lagrangian before those applications.

# Kernels, adjoints and clean composition

A Fourier-integral operator carries a singularity from an input covector to an output covector along a canonical relation. Composing two operators matches their middle covectors. Clean matching can leave a family of possible middle points; its dimension raises the order by half that dimension, and the principal symbol is an integral over that family.

The prerequisites are the clean phase and relation geometry in [Phase space and generating families](phase-space-and-generating-families.md), the estimates and normalization in [Oscillatory distributions and their order](oscillatory-distributions-and-order.md), the intrinsic phase converse in [Recognizing a Lagrangian distribution intrinsically](intrinsic-lagrangian-regularity.md), the invariant symbol and conjugation theorem in [Gaussian lines, densities and invariant symbols](gaussian-lines-and-invariant-symbols.md), and the linear symbol product in [Reducing Gaussian symbols and composing linear relations](reduction-and-linear-symbol-composition.md).

We import the bundle/half-density kernel correspondence and anti-dual convention from §13 of Detecting regularity without choosing coordinates. Its scalar Schwartz kernel theorem is an explicit entry prerequisite there; we use that same contract. Its Fourier wavefront test and compact-distribution polynomial bound are also used below. We prove the FIO-specific mapping and composition assertions. The authority is [Hörmander IV, §25.2], through Theorem 25.2.3. Symbols here are ordinary \(S_{1,0}\) symbols; the \(\rho\)-loss variants require their own estimates.

All manifolds are smooth, Hausdorff, second countable and without boundary. All vector bundles are smooth, complex and of finite rank. We write \(D=-i\partial\), use Fourier phase \(-x\cdot\xi\), and use inverse Fourier factor \((2\pi)^{-n}\). Orders and estimates on a noncompact manifold are local over compact base sets.

## 1. A kernel has a reflected input covector

Let \(E\to X\) and \(F\to Y\). A distribution kernel
\[
K\in\mathcal D'(X\times Y;
\Omega_{X\times Y}^{1/2}\otimes\operatorname{Hom}(F_y,E_x))
\tag{1.1}
\]
defines a continuous map
\[
A:C_c^\infty(Y;\Omega_Y^{1/2}\otimes F)
\longrightarrow\mathcal D'(X;\Omega_X^{1/2}\otimes E).
\tag{1.2}
\]
Conversely every such continuous map has a unique kernel. This is the exact imported kernel correspondence. In local frames it reads
\[
(Af)(x)=\int K(x,y)f(y)\,dy;
\tag{1.3}
\]
the displayed coefficients are relative to the half-density frames. The two input half densities supply the density integrated in \(y\), leaving an output half density. For a distribution kernel, (1.3) initially means its pairing with a product of input and output tests.

A homogeneous canonical relation from \(T^*Y\setminus0\) to \(T^*X\setminus0\) is a conic Lagrangian
\[
C\subset (T^*X\setminus0)\times(T^*Y\setminus0)
\]
for \(\omega_X-\omega_Y\). Its kernel Lagrangian is the twist
\[
C'=\{(x,\xi;y,-\eta):(x,\xi;y,\eta)\in C\}
\subset T^*(X\times Y)\setminus0.
\tag{1.4}
\]
The twist is a symplectic identification from the signed product to the usual product cotangent, and preserves the distinguished vertical tangent plane.

We require \(C'\) to be closed in the full punctured cotangent \(T^*(X\times Y)\setminus0\). Closure just inside the set where both covectors are nonzero is weaker: it would permit limit directions with one covector zero. Such limits matter for mapping estimates.

**Definition 1.1.** An FIO of order \(m\) associated with \(C\) is the operator whose kernel belongs to
\[
I^m(X\times Y,C';
\Omega_{X\times Y}^{1/2}\otimes\operatorname{Hom}(F,E)).
\tag{1.5}
\]
Its principal symbol is transported from \(C'\) to \(C\), and has degree
\[
\nu=m+\frac{\dim X+\dim Y}{4}
\tag{1.6}
\]
in \(M_C\otimes\Omega_C^{1/2}\otimes\operatorname{Hom}(F,E)\), modulo one lower symbol order. This is a half-density symbol, not a scalar amplitude of order \(m\).

The kernel is **properly supported** when both projections of its support to \(X\) and \(Y\) are proper. Above a compact set in either variable, the other variable then lies in a compact set. This is a condition on base support, distinct from the proper cotangent matching projection in Section 4.

## 2. Nonzero covectors give mapping and wavefront control

**Theorem 2.1.** An FIO with the preceding nonzero-covector and closure hypotheses has continuous maps
\[
A:C_c^\infty(Y)\longrightarrow C^\infty(X),
\qquad
A:\mathcal E'(Y)\longrightarrow\mathcal D'(X),
\tag{2.1}
\]
with the displayed bundle and half-density coefficients understood. The second extends the first uniquely, and
\[
\operatorname{WF}(Au)\subset C(\operatorname{WF}(u)),
\qquad u\in\mathcal E'(Y).
\tag{2.2}
\]
If \(A\) is properly supported, it also maps \(C_c^\infty\) to \(C_c^\infty\), \(\mathcal E'\) to \(\mathcal E'\), \(C^\infty\) to \(C^\infty\), and \(\mathcal D'\) to \(\mathcal D'\), continuously. Formula (2.2) then holds locally for arbitrary \(u\in\mathcal D'\).

**Proof.** It is enough to prove a kernel assertion with \(\operatorname{WF}(K)\subset C'\); the earlier intrinsic theorem gives that inclusion. Localize to compact coordinate products and finitely many bundle components. Choose cutoffs in both variables, with the input cutoff equal to one near the compact input support relevant to the output cutoff. Write \(k\) for the resulting compact scalar kernel. Its Fourier transform has a global polynomial bound.

The closed wavefront set of this compact kernel contains no direction \((\xi,0)\) and no direction \((0,\eta)\). Compactness of its unit covector slice and the Fourier wavefront test therefore give a number \(0<\delta<1\) for which
\[
|\widehat k(\xi,\eta)|
\leq C_N\langle(\xi,\eta)\rangle^{-N}
\quad\text{if }|\xi|\leq\delta|\eta|
\text{ or }|\eta|\leq\delta|\xi|,
\tag{2.3}
\]
for every \(N\). The same estimates hold after fixed Fourier derivatives, since they correspond to multiplication of the kernel by smooth coordinate polynomials. Spatial partitions make this use of the Fourier wavefront test valid on each compact product; there are finitely many pieces.

For a compact distribution \(u\), the localized Fourier formula is
\[
\widehat{Au}(\xi)
=(2\pi)^{-\dim Y}
\int\widehat k(\xi,-\eta)\widehat u(\eta)\,d\eta.
\tag{2.4}
\]
For each fixed \(\xi\), the tail \(|\eta|\gg|\xi|\) is absolutely integrable by (2.3) and the polynomial bound for \(\widehat u\). The other part is bounded by a polynomial in \(\xi\). Thus (2.4) defines a compactly localized distribution. For smooth \(u\), Fourier inversion and the kernel pairing prove the formula first; compact smooth mollifications of a compact distribution have a common polynomial Fourier bound and converge pointwise in Fourier space. The same tail estimate passes (2.4) to their limit.

For compact smooth \(u\), (2.4) decreases rapidly in \(\xi\): on \(|\eta|\leq\delta|\xi|\), use the rapid bound for \(\widehat k\); on its complement, use rapid decrease of \(\widehat u\), the polynomial bound for the kernel, and also (2.3) on the unbounded tail. Choosing arbitrarily high decay proves every output smooth seminorm, with only finitely many input seminorms. This proves \(C_c^\infty\to C^\infty\) continuity.

Interchanging the variables gives the same smooth mapping for the transposed kernel. Transposition therefore defines the continuous strong-dual map \(\mathcal E'\to\mathcal D'\): a bounded family of output tests maps to a bounded family of smooth input functions. Formula (2.4) agrees with this definition. Compact smooth approximation converges in \(\mathcal E'\): a finite-order estimate, applied to the Taylor remainder of a test under mollification, is uniform on each bounded family of smooth tests. Hence the extension is unique.

To prove (2.2), take an output covector \((x_0,\xi_0)\) outside \(C(\operatorname{WF}(u))\). Work over the compact input support and shrink the output spatial and angular neighborhoods. In the comparable region
\[
\delta|\xi|<|\eta|<\delta^{-1}|\xi|,
\tag{2.5}
\]
the normalized frequencies, their ratios, and the relevant base sets form a compact set. At every point of this set, either the input direction is outside \(\operatorname{WF}(u)\), or the kernel direction \((\xi,-\eta)\) is outside \(\operatorname{WF}(K)\). Otherwise that point would give a member of \(C(\operatorname{WF}(u))\) in the chosen output neighborhood. The separation can be made uniform: failure for every shrinking neighborhood would give, by compactness, a limiting point contradicting the choice of \((x_0,\xi_0)\).

Cover this compact set by finitely many spatial/angular neighborhoods with one of those two alternatives. Choose spatial cutoffs with slightly larger supports for the Fourier wavefront tests. On pieces of the first kind, \(\widehat u\) is rapidly decreasing in the selected input cone. On pieces of the second kind, the localized \(\widehat k\) is rapidly decreasing in the selected joint cone. A bounded angular partition in (2.4), together with spatial localization, estimates each piece by those bounds; the remaining factor is polynomial. Comparability makes arbitrary joint or input decay into arbitrary output decay, and the integration volume costs only a fixed power of \(|\xi|\). The noncomparable pieces are already rapidly decreasing by (2.3). Thus the localized Fourier transform of \(Au\) decreases rapidly in a cone about \(\xi_0\), proving (2.2).

For clarity, in the first alternative an input cutoff is chosen equal to one on the corresponding kernel's input support; localization of \(u\) there gives the asserted rapid cone estimate. In the second alternative the same choice leaves a compact distribution with a polynomial Fourier bound. This avoids treating a global wavefront test as an estimate valid after an arbitrary unlocalized pairing.

Finally properness gives compact output support for compact input, and compact input support relevant to every compact output set. Insert a cutoff equal to one on that latter set to act on a noncompact smooth function or distribution. The result is independent of the cutoff because the kernel has no support in its difference. These local definitions agree, with the already proved estimates, and prove the remaining maps and their continuity. ∎

## 3. The adjoint has the inverse relation

Let \(E^*\) mean the anti-dual: its elements are conjugate-linear functionals on \(E\). The canonical pairing is \(\langle v,\mu\rangle=\overline{\mu(v)}\), linear in \(v\). For \(T:F_y\to E_x\), define
\[
T^*:E_x^*\to F_y^*,\qquad T^*\mu=\mu\circ T.
\tag{3.1}
\]
This is linear in \(\mu\) and conjugate-linear in \(T\). In paired local frames it is conjugate transpose; no Hermitian metric identifying a bundle with its anti-dual is required.

The formal adjoint is characterized on compact smooth half densities by
\[
\int_X\langle Af,g\rangle
=\int_Y\langle f,A^*g\rangle.
\tag{3.2}
\]
Its kernel is \(K^*(y,x)=K(x,y)^*\), with the variables interchanged.

**Theorem 3.1 (adjoint).** If \(A\) has order \(m\) and relation \(C\), then
\[
A^*\in I^m\bigl(Y\times X,(C^{-1})';
\Omega_{Y\times X}^{1/2}\otimes\operatorname{Hom}(E^*,F^*)\bigr),
\tag{3.3}
\]
where \(C^{-1}\) interchanges the two members of the relation. Its principal symbol is the transported fiberwise adjoint of the original symbol, with the conjugated Maslov factor. Proper support is preserved.

**Proof.** Let \(s:Y\times X\to X\times Y\) interchange the variables. Pullback by \(s\) preserves the Lagrangian order and its half-density symbol by coordinate invariance. The bundle map taking adjoints is antilinear. The conjugation theorem of the invariant-symbol lesson then reflects both kernel covectors and conjugates its Maslov factor. For \((x,\xi;y,\eta)\in C\), the kernel covectors are \((\xi,-\eta)\). Interchange and reflection give \((\eta,-\xi)\) on \(Y\times X\), precisely the twist of \((y,\eta;x,\xi)\in C^{-1}\). The symbol transformation is the same interchange followed by the antilinear bundle adjoint and the proved conjugated Maslov identification. The pairing (3.2) follows from the kernel pairing on products of tests, and identifies this kernel as the formal adjoint. Interchanging two proper kernel projections preserves properness. ∎

## 4. Clean matching becomes a global relation under properness and connectedness

Let \(C_1\) go from \(T^*Y\setminus0\) to \(T^*X\setminus0\), and \(C_2\) from \(T^*Z\setminus0\) to \(T^*Y\setminus0\). Write
\[
\mathcal F=(C_1\times C_2)\cap
\bigl(T^*X\times\operatorname{diag}(T^*Y)\times T^*Z\bigr),
\]
\[
p:\mathcal F\longrightarrow T^*(X\times Z)\setminus0,
\qquad (x,\xi;y,\eta;y,\eta;z,\zeta)
\longmapsto(x,\xi;z,-\zeta).
\tag{4.1}
\]
Assume the intersection is clean and has fixed excess \(e\). The earlier geometry theorem proves that \(p\) has rank \(\dim X+\dim Z\), with \(e\)-dimensional fibers and local Lagrangian images. We call the composition **proper** if \(p\) is proper, and **connected** if every nonempty fiber is connected.

**Lemma 4.1.** Under these hypotheses the image \(C'\) is a closed embedded conic Lagrangian, with both its covectors nonzero. Every fiber \(\mathcal F_\gamma\), \(\gamma\in C'\), is a compact connected manifold of dimension \(e\).

**Proof.** The clean geometry already gives constant rank, local Lagrangian images and the fiber dimension. Properness gives compact fibers and a closed image. To verify the latter directly near any target point, a sequence of image points converging there has preimages in the preimage of a compact target neighborhood; a convergent subsequence supplies a preimage of the limit.

Embeddedness requires an additional argument. Cover the compact fiber over a point \(\gamma\) by finitely many constant-rank coordinate neighborhoods. Two neighborhoods intersecting at a point of this fiber have the same local image germ at \(\gamma\): a smaller constant-rank neighborhood in their intersection maps onto a neighborhood of \(\gamma\) in either image. Connectedness of the fiber makes the adjacency graph of the finite covering connected, so all these image germs coincide. Choose a small target neighborhood where their finitely many germs are one embedded submanifold.

Shrink it so that its whole inverse image lies in the chosen coordinate neighborhoods. Such a shrink exists by properness: otherwise preimages outside their union could be chosen over a sequence tending to \(\gamma\); compactness would give a limiting preimage in the fiber outside that open union, a contradiction. The entire image in the shrunken neighborhood is therefore the single constant-rank image, and is embedded. Its tangent plane is Lagrangian by the local theorem. Homogeneity and the nonzero external covectors are inherited from the matching relations. ∎

These two properness conditions play different roles. Proper kernel support makes the operator product act on distributions and gives base support control. Properness of (4.1) makes its middle cotangent fibers compact and its symbol integral finite.

If \(Y\) is compact, (4.1) is automatically proper under the stated full-cotangent closure and nonzero-covector hypotheses. Indeed, over a compact external cotangent set, all base variables are compact. If a sequence of middle covectors were unbounded, divide all covectors by their middle norms. A subsequence would converge in \(C_1'\) to a covector with zero \(X\) component and nonzero middle component, contradicting its full-cotangent closure and exclusion of such covectors. A middle norm tending to zero would, without rescaling, give an analogous forbidden limit with one external component nonzero. Thus the middle covectors remain in a compact annulus. Closure of both relations then makes the inverse image compact.

## 5. The clean composition theorem

Let \(n_X=\dim X\), \(n_Y=\dim Y\), \(n_Z=\dim Z\), and let \(G\to Z\) be the third bundle. Suppose
\[
A_1\in I^{m_1}(X\times Y,C_1';
\Omega^{1/2}\otimes\operatorname{Hom}(F,E)),
\]
\[
A_2\in I^{m_2}(Y\times Z,C_2';
\Omega^{1/2}\otimes\operatorname{Hom}(G,F))
\tag{5.1}
\]
are properly supported, and their relations have proper connected clean composition of excess \(e\), as in Section 4.

At each matching point, the tangent relations are linear canonical relations. Their symbol product from the preceding lesson, followed by ordinary bundle-map composition \(F\to E\) after \(G\to F\), defines
\[
\sigma_1\times\sigma_2
\in p^*(M_C\otimes\Omega_C^{1/2}\otimes\operatorname{Hom}(G,E))
\otimes\Omega(\ker dp).
\tag{5.2}
\]
It is a density along the fiber with values in the indicated output symbol line. Our product convention includes the factor \((2\pi)^{-e/2}\) proved in the linear lesson.

**Theorem 5.1 (clean FIO composition).** The product has properly supported kernel and
\[
A_1A_2\in I^{m_1+m_2+e/2}
(X\times Z,C';\Omega^{1/2}\otimes\operatorname{Hom}(G,E)).
\tag{5.3}
\]
Its principal symbol is
\[
\sigma(A_1A_2)(\gamma)
=\int_{\mathcal F_\gamma}\sigma_1\times\sigma_2,
\tag{5.4}
\]
modulo one lower symbol order, of degree
\[
m_1+m_2+\frac e2+\frac{n_X+n_Z}{4}.
\tag{5.5}
\]
The local construction is continuous in ordinary amplitude symbol seminorms, with fixed phase/support data. Microlocal interior-cone versions follow by localization. The remaining sections prove each analytic and normalization assertion.

## 6. Discard the unequal-frequency part by a full smoothing estimate

Choose local nondegenerate phase representations
\[
K_1(x,y)=(2\pi)^{-(n_X+n_Y+2N_1)/4}
\int e^{i\phi(x,y,\theta)}a_1(x,y,\theta)\,d\theta,
\]
\[
K_2(y,z)=(2\pi)^{-(n_Y+n_Z+2N_2)/4}
\int e^{i\psi(y,z,\tau)}a_2(y,z,\tau)\,d\tau,
\tag{6.1}
\]
where
\[
a_1\in S^{\alpha_1},\quad
\alpha_1=m_1+(n_X+n_Y-2N_1)/4,
\]
\[
a_2\in S^{\alpha_2},\quad
\alpha_2=m_2+(n_Y+n_Z-2N_2)/4.
\tag{6.2}
\]
Bundle coefficients multiply in the order \(a_1a_2\). Compactly localize the base variables and angular supports near critical points, and remove bounded frequencies into smooth kernels. Since both middle covectors are nonzero, shrink the conic supports so
\[
c_1|\theta|\leq|\phi_y|\leq C_1|\theta|,
\qquad c_2|\tau|\leq|\psi_y|\leq C_2|\tau|
\tag{6.3}
\]
throughout them. The external covectors are nonzero as well. Shrink these same supports so that \(|\phi_x|\geq c_X|\theta|\) and \(|\psi_z|\geq c_Z|\tau|\), for positive constants \(c_X,c_Z\). These estimates will also control the smooth-input limits in Section 8. Pieces away from their phase-critical sets are smooth by the earlier full-gradient nonstationary argument.

The formal product phase and amplitude are
\[
\Phi=\phi(x,y,\theta)+\psi(y,z,\tau),\qquad
a=a_1(x,y,\theta)a_2(y,z,\tau).
\tag{6.4}
\]
If \(\Phi_y=0\), (6.3) implies
\[
\frac{c_2}{C_1}|\tau|\leq|\theta|
\leq\frac{C_2}{c_1}|\tau|.
\tag{6.5}
\]
Choose a smooth degree-zero ratio cutoff \(\chi(\theta,\tau)\), equal to one on a neighborhood of a somewhat larger comparable region containing (6.5), supported where the two radii remain comparable. Choose its transition thresholds far enough apart that, on \(\operatorname{supp}(1-\chi)a\),
\[
|\Phi_y|\geq c(|\theta|+|\tau|).
\tag{6.6}
\]
For example, in \(C_1|\theta|\leq c_2|\tau|/2\), the triangle inequality gives \(|\Phi_y|\geq c_2|\tau|/2\); the reversed case is identical. A cutoff equal to one between these two separated regimes gives the assertion. Low joint frequencies can be treated separately and smoothly.

Put \(b=\chi a\), \(r=(1-\chi)a\). Consider the remainder kernel
\[
R(x,z)=c_0\iint\left(\int e^{i\Phi}r\,dy\right)d\theta\,d\tau,
\qquad c_0=(2\pi)^{-(n_X+n_Z+2(n_Y+N_1+N_2))/4}.
\tag{6.7}
\]
The complete transposed integration field in \(y\) is
\[
L=\frac{\Phi_y\cdot\partial_y}{i|\Phi_y|^2},
\qquad Le^{i\Phi}=e^{i\Phi},
\qquad L^t r=-\operatorname{div}_y
\left(\frac{\Phi_y}{i|\Phi_y|^2}r\right).
\tag{6.8}
\]
On the compact base supports, every fixed \(y\)-derivative of the vector coefficient is \(O((|\theta|+|\tau|)^{-1})\), by homogeneity and (6.6). Repeating (6.8) costs one inverse joint radius each time. The product amplitude and its base derivatives are bounded by
\[
C\langle|\theta|+|\tau|\rangle^P,
\qquad P=\max(\alpha_1,0)+\max(\alpha_2,0),
\tag{6.9}
\]
also when either order is negative and its own frequency is much smaller than the other. Fixed output derivatives of \(e^{i\Phi}\) cost only additional fixed powers of the joint radius. Thus, for every output derivative and every \(M\), enough repetitions give
\[
\left|\partial_{x,z}^{\beta}
\int e^{i\Phi}r\,dy\right|
\leq C_{\beta,M}\langle|\theta|+|\tau|\rangle^{-M}.
\tag{6.10}
\]
All integrations have compact \(y\) support. Taking \(M>N_1+N_2+1\) gives absolute frequency integrability, and arbitrarily many output derivatives give \(R\in C^\infty\). The constants use finitely many amplitude seminorms, proving continuity of this smoothing remainder.

## 7. Make the middle base variable into a homogeneous phase variable

On \(\operatorname{supp}b\), both frequencies are comparable to
\[
q=(|\theta|^2+|\tau|^2)^{1/2}.
\]
Leibniz's rule and (6.2) show that \(b\) is an ordinary joint symbol of order
\[
\mu=m_1+m_2+
\frac{n_X+n_Z+2n_Y-2N_1-2N_2}{4}.
\tag{7.1}
\]
Every derivative in either frequency costs one inverse \(q\), including derivatives of \(\chi\). This conclusion would fail for the uncut product when one frequency is small.

Set
\[
v=q y,\qquad w=(v,\theta,\tau),\qquad N=n_Y+N_1+N_2.
\tag{7.2}
\]
This is an invertible change for \(q>0\), with
\[
dy\,d\theta\,d\tau=q^{-n_Y}\,dv\,d\theta\,d\tau.
\tag{7.3}
\]
In the new variables the phase is
\[
\widetilde\Phi(x,z,w)
=\phi(x,v/q,\theta)+\psi(v/q,z,\tau).
\tag{7.4}
\]
All components of \(w\) dilate together, so it is homogeneous of degree one. The amplitude is
\[
\widetilde b(x,z,w)=q^{-n_Y}b(x,z,v/q,\theta,\tau)
\in S^{\mu-n_Y}.
\tag{7.5}
\]
To verify every derivative in (7.5), note that on its support \(|w|\asymp q\), because \(y\) is compactly supported. Every \(w\)-derivative of \(v/q\) of positive order costs the corresponding inverse power of \(q\); derivatives of the original frequencies and of \(q^{-n_Y}\) obey the same scaling. Apply the chain rule and the joint symbol estimates from (7.1). Base derivatives preserve the order. Compact \(y\) and compact angular supports give compactly generated support in the new phase cone, so extension by zero inside a slightly larger cone preserves these estimates.

The phase-critical equations before this change are
\[
\phi_\theta=0,\quad\psi_\tau=0,\quad
\phi_y+\psi_y=0.
\tag{7.6}
\]
They identify the critical manifold with the clean matching space \(\mathcal F\); its critical map is \(p\). The previously proved phase-addition proposition shows that \(\widetilde\Phi\) is a clean phase of excess \(e\) parametrizing \(C'\) locally. The full differential is nonzero near the selected critical cone because its external covectors are nonzero. The invertible change (7.2) preserves its clean rank.

The comparable kernel is
\[
B(x,z)=c_0\int e^{i\widetilde\Phi(x,z,w)}
\widetilde b(x,z,w)\,dw.
\tag{7.7}
\]
Put \(n=n_X+n_Z\) and \(M=m_1+m_2+e/2\). The order computation is
\[
\mu-n_Y=M+\frac{n-2N-2e}{4}.
\tag{7.8}
\]
Also the original constant and the normalized clean-phase constant satisfy
\[
c_0=(2\pi)^{-e/2}(2\pi)^{-(n+2N-2e)/4}.
\tag{7.9}
\]
The clean phase converse therefore gives \(B\in I^M(X\times Z,C')\). Its oscillatory-integral seminorm estimates and the proved clean stationary-phase reduction give continuous dependence on the original amplitudes. These are ordinary-symbol estimates; no assertion about a different remainder scale has been inferred from them.

## 8. Identify the constructed kernel with the operator product and assemble it

So far (6.7) and (7.7) define kernels from the original amplitudes. To identify \(A_1A_2=B+R\), one must justify the formal integrations when the individual kernels are singular.

Take a smooth compact frequency cutoff \(h\), equal to one near zero, and replace \(a_i\) by \(h(\theta_i/T)a_i\). The resulting local kernels are smooth, and compact base supports make ordinary Fubini valid. Their product equals the comparable part plus the remainder just constructed.

The truncated amplitudes are uniformly bounded in their original symbol orders and converge in every slightly higher order:
\[
h(\theta/T)a\longrightarrow a
\quad\text{in }S^{\alpha+\varepsilon},
\qquad\varepsilon>0.
\tag{8.1}
\]
Indeed the error is supported where \(|\theta|\geq cT\); every fixed derivative has the \(S^\alpha\) bound, and the additional \(\varepsilon\) in the seminorm gives \(O(T^{-\varepsilon})\). Derivatives of the cutoff have the same bound on their transition annulus. This argument does not assert density of smoothing symbols in the same-order topology.

Oscillatory-integral continuity, applied at those slightly higher orders, gives distributional convergence of both constructed pieces to (6.7) and (7.7). Their actual orders remain the original orders already proved directly in Sections 6–7.

There is also convergence of the operator products on compact smooth inputs. On these phase supports the input phase gradient never vanishes, by (6.3), or by its input analogue for the second operator. Integration by parts in that input variable, with the full transposed field, makes the frequency tail decrease faster than every power of \(T\) after any fixed output derivatives. The estimate uses finitely many input smooth seminorms, uniformly for the truncated amplitudes. Thus the local truncated operators \(A_{i,T}\) are uniformly continuous \(C_c^\infty\to C^\infty\) on fixed supports and converge there in every smooth seminorm.

Properness, or the fixed compact base supports of the current local pieces, puts \(A_{2,T}f\) and \(A_2f\) in a common compact input support for \(A_1\). Consequently
\[
A_{1,T}A_{2,T}f-A_1A_2f
=A_{1,T}(A_{2,T}f-A_2f)
+(A_{1,T}-A_1)A_2f\longrightarrow0
\tag{8.2}
\]
in local smooth output seminorms. Equality on all compact input/output tests now identifies the limiting kernel with \(A_1A_2\), by uniqueness of the kernel correspondence. This proves \(A_1A_2=B+R\) locally and hence its order assertion.

For global assembly, first localize external base supports. Proper support of both kernels confines the relevant middle base points to a compact set. Local phase partitions on the unit cospheres and smooth residual kernels reduce to finitely many pieces on each such compact product. Properness of \(p\) makes the matching cotangent preimage of a compact normalized external cone compact, so finitely many matched phase patches cover it. Pieces not meeting that preimage are microlocally smoothing at the external cone, by full-gradient nonstationarity in the product phase. Thus the local class statements assemble at every output covector. The remaining smooth kernels cause no difficulty: composed with a properly supported FIO they are smooth, by the smooth-input mapping of Theorem 2.1 and its adjoint version, with differentiation under a smooth compact test family.

The product is properly supported as well. Above a compact output base set, the first kernel permits middle points only in a compact set, and the second then permits input points only in a compact set. The reversed reasoning controls the other projection. More explicitly, possible support points of the product lie in the projection of the two kernel supports with matching middle base. This projection is closed on every such compact region: its middle points have a convergent subsequence. Both external projections of the resulting closed support relation are therefore proper. This completes (5.3).

## 9. The principal symbol is the compact fiber integral

Fix a matching point and split the clean phase variables into a normal group and \(e\) local fiber coordinates. The clean symbol theorem says that the principal symbol of (7.7) is the integral, over those fiber coordinates, of the normal stationary-phase symbol. Its exact Fresnel factor and normal determinant are already part of that theorem.

At the fixed critical point, the Hessians of \(\phi\) and \(\psi\) parametrize the tangent kernel Lagrangians. To make the identification explicit, their quadratic critical equations are the linearizations of \(\phi_\theta=0\) and \(\psi_\tau=0\). Restricting to the middle diagonal identifies the two base variations \(\delta y\); stationarity in that shared variation adds \(\delta\phi_y+\delta\psi_y=0\). After reflecting each input covector, these are exactly the tangent matching equations in \(T C_1\times T C_2\). Forgetting the shared middle variation is their reduction map. Its kernel is \(\ker dp\), of dimension \(e\), and its output is the tangent plane to \(C'\). Thus the summed quadratic phase, restricted and integrated in the shared middle variable, is precisely the quadratic reduction of the preceding lesson.

The critical-map density identifies its radical with \(\ker dp\). The proved Gaussian reduction theorem therefore identifies the normal symbol multiplied by the density of the \(e\) fiber coordinates with \(\sigma_1\times\sigma_2\) in (5.2), including its Maslov map, positive Jacobian and bundle-map order. The amplitude change (7.3) contributes its density Jacobian and is already covered by the invariant clean-phase symbol formula.

There is no extra factor of \(2\pi\) to insert in (5.4). In our conventions the product integral originally has the unadjusted constant \(c_0\); (7.9) compares it with the clean normalized constant. That comparison is the same \((2\pi)^{-e/2}\) which the linear symbol product already includes. Both descriptions evaluate the same quadratic integral; multiplying by that factor a second time would change the kernel's leading coefficient.

The fiber is compact by Lemma 4.1. A density with values in the fixed output symbol line integrates without a choice of orientation. It may have complex coefficients, and cancellation is possible. To see smoothness and symbol estimates, work over a compact normalized external cone. Its preimage under \(p\) is compact. Cover it by finitely many submersion charts, use a smooth partition with compact support in those charts, and express \(p\) as \((\gamma,s)\mapsto\gamma\). Each piece integrates a smooth density in \(s\) on a common compact support. Differentiating under that integral proves every local seminorm estimate. Local trivializations of the pulled-back output line make these formulas scalar; their transition maps commute with the integral. Thus they define (5.4) globally.

Here is also an intrinsic check of the symbol degree (5.5). Let
\[
\nu_1=m_1+(n_X+n_Y)/4,
\qquad\nu_2=m_2+(n_Y+n_Z)/4.
\]
Cotangent dilation pulls the symplectic form back to \(t\omega\), not to \(\omega\). In the tangent reduction density map the perfect pairing is between quotients of dimension \(2n_Y-e\). Scaling that pairing by \(t\) multiplies the positive dual-density map by \(t^{-(2n_Y-e)/2}\): in bases its coefficient is the inverse square root of the absolute pairing determinant. Trivialization of the inverse constraint half density by the middle symplectic half volume contributes \(t^{n_Y/2}\). Their product is \(t^{(e-n_Y)/2}\). Therefore the fiber-density symbol has total degree
\[
\nu_1+\nu_2+\frac{e-n_Y}{2}
=m_1+m_2+\frac e2+\frac{n_X+n_Z}{4}.
\tag{9.1}
\]
The Maslov phase is unchanged by a positive conformal scaling. Fiber integration commutes with pullback by dilation, including its fiber-density Jacobian, so it has the same degree. The finite submersion-chart argument supplies all derivative bounds for ordinary, not necessarily homogeneous, symbols.

Changing either input symbol by one lower order changes the integral by one lower output order, using the same bounds and (9.1). The normal stationary-phase remainder is also one lower order. Thus (5.4) is an identity of principal-symbol quotient classes, and completes the proof of Theorem 5.1. If its integral vanishes, the invariant-symbol isomorphism puts the product in \(I^{m_1+m_2+e/2-1}\). Computing its new leading symbol requires the next term, rather than reusing the vanished integral.

## 10. A compact fiber model checks the excess and the constant

Let \(X=Z=\mathbb R\), \(Y=\mathbb R\times M\), where \(M\) is a compact connected smooth manifold of dimension \(k\), with positive density \(\rho\). For smooth scalar functions \(v_1,v_2\) on \(M\), define
\[
A_1f(x)=\int_M v_1(t)f(x,t)\,\rho(t),
\qquad A_2g(s,t)=v_2(t)g(s).
\tag{10.1}
\]
The coefficient frames are \(|dx|^{1/2}\) on \(X,Z\) and \(|ds|^{1/2}\rho^{1/2}\) on \(Y\). Their kernels are \(v_1(t)\delta(x-s)\) and \(v_2(t)\delta(s-z)\) in the corresponding product half-density frames. Both kernels are properly supported because \(M\) is compact.

The relations match \(x=s=z\), with the same nonzero covector in that variable and zero covector in the \(M\) direction. Their middle points form \(M\), so the composition is the identity relation with excess \(e=k\). It is proper and connected. Each delta kernel is conormal of codimension one in base dimension \(2+k\), hence has order
\[
m_1=m_2=\frac12-\frac{2+k}{4}=-\frac k4.
\tag{10.2}
\]
The theorem predicts product order zero, and indeed
\[
A_1A_2g=\left(\int_Mv_1v_2\,\rho\right)g.
\tag{10.3}
\]

The normalized one-variable phase amplitudes for these exact delta kernels are \((2\pi)^{k/4}v_i\), relative to the specified product half-density frames, because their kernel normalization is \((2\pi)^{-(4+k)/4}\int e^{i(x-s)\theta}a_i\,d\theta\). In a coordinate half-density frame using \(|dt|^{1/2}\), each amplitude also contains \((\rho/|dt|)^{1/2}\). Multiplying the two middle half densities therefore supplies exactly \(\rho\). The two amplitudes contribute \((2\pi)^{k/2}\), canceled by the linear symbol factor \((2\pi)^{-e/2}\). Formula (5.4) gives exactly \(\int_Mv_1v_2\rho\) times the identity symbol. This analytic compact-fiber example satisfies the global hypotheses.

## 11. Exercises with complete solutions

**Exercise 11.1 (translation and adjoint; introductory).** On \(\mathbb R\), let \(A_af(x)=f(x+a)\), \(a\in\mathbb R\), acting on half densities. Determine its kernel, canonical relation, order and formal adjoint.

**Solution.** Its kernel is \(\delta(y-x-a)|dx\,dy|^{1/2}\), represented by the phase \((x+a-y)\theta\) with prefactor \((2\pi)^{-1}\). The relation is
\[
C_a=\{(x,\xi;y=x+a,\eta=\xi):\xi\ne0\}.
\]
It is the graph of a symplectic translation and is closed in the full punctured product cotangent. A codimension-one delta kernel in base dimension two has order \(1/2-2/4=0\). Its graph support is proper. Changing variables in the half-density pairing gives \(A_a^*g(y)=g(y-a)\). Its relation is \(C_a^{-1}\), its order is zero, and its unit symbol is transported unchanged by the adjoint law.

**Exercise 11.2 (why two scales must be comparable; intermediate).** For phases \(\phi=(x-y)\theta\), \(\psi=(y-z)\tau\), show that if \(|\theta|\leq c|\tau|\), \(0<c<1\), then
\[
|\Phi_y|\geq\frac{1-c}{1+c}(|\theta|+|\tau|).
\]
Explain why arbitrary amplitude orders are allowed in the smoothing estimate on this region.

**Solution.** Here \(\Phi_y=\tau-\theta\). The reverse triangle inequality gives \(|\tau-\theta|\geq(1-c)|\tau|\), while \(|\theta|+|\tau|\leq(1+c)|\tau|\). This proves the bound, for either sign of the real frequencies. With compact middle support, each integration by parts in \(y\) gives one inverse joint radius; the phase coefficient is constant in \(y\) in this example. The amplitude and every fixed output derivative have some fixed polynomial growth, even when one individual frequency is small. Repeating more times than that growth plus the frequency integration dimension proves a smooth remainder. The general case retains the divergence term in (6.8).

**Exercise 11.3 (the order of compact fiber averaging; intermediate).** In Section 10, take \(\dim M=3\). Give the two kernel orders, the composition order, and the exact normalized phase amplitudes. Verify the cancellation of the \(2\pi\) factors in the symbol.

**Solution.** The kernel base dimension is five and its delta codimension is one, so each order is \(-3/4\). The excess is three, hence the composition order is \(-3/4-3/4+3/2=0\). Each normalized amplitude is \((2\pi)^{3/4}v_i\). Their product has factor \((2\pi)^{3/2}\), and the linear symbol map has factor \((2\pi)^{-3/2}\). The symbol is therefore \((\int_Mv_1v_2\rho)\) times the identity symbol, with neither a missing nor a doubled constant.

**Exercise 11.4 (bundle-map order; intermediate).** Compose two identity-relation FIOs with constant matrix coefficients
\[
B_1=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad B_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]
Compute the product symbol and its adjoint. Explain why exchanging the factors gives a different symbol.

**Solution.** The excess is zero and the identity Maslov unit and graph half density are preserved. The ordered bundle composition is
\[
B_1B_2=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Its adjoint is \(B_2^*B_1^*=(B_1B_2)^*\), acting between the anti-dual bundles. Here the displayed real product is symmetric, so it is its own conjugate transpose. The reversed product is \(B_2B_1=\begin{pmatrix}1&1\\1&2\end{pmatrix}\), which differs. The density and Maslov factors cannot turn noncommuting bundle maps into commuting coefficients.

**Exercise 11.5 (a vanished fiber integral with a nonzero lower term; advanced).** In Section 10 take \(M=S^1\), with normalized density \(dt/(2\pi)\), and \(A_1\) the unweighted average. Let \(P\) be a properly supported ordinary pseudodifferential operator of order \(-1\) on \(\mathbb R\), with nonzero principal symbol. Define
\[
A_2g(s,t)=e^{it}g(s)+(Pg)(s).
\]
Determine the leading clean-composition symbol and the actual product.

**Solution.** The first term of \(A_2\) is the lift model of order \(-1/4\). The second is the lift composed with \(P\); the already proved theorem applies with a graph factor and excess zero, and gives order \(-1/4-1=-5/4\). Thus it is one lower order. The leading fiber symbol integrates \(e^{it}\) over the circle and is zero. The clean theorem places the product in order zero, and the vanished symbol improves it to order \(-1\). Directly,
\[
A_1A_2g=
\left(\int_{S^1}e^{it}\frac{dt}{2\pi}\right)g
+\left(\int_{S^1}\frac{dt}{2\pi}\right)Pg=Pg.
\]
Its nonzero order-\(-1\) symbol is that of \(P\). This shows why pointwise nonzero input symbols can yield a zero fiber integral and why the next coefficient must then be computed. Proper support of \(P\) and compactness of the circle preserve both kernel support requirements.

**Exercise 11.6 (remove the compact-fiber hypothesis; advanced).** Replace \(M\) in the unweighted scalar model (10.1) by \(\mathbb R\). Determine which hypotheses fail and whether the formal product on a nonzero compact smooth \(g\) is defined by the displayed integrals.

**Solution.** The matching fiber over any identity covector is \(\mathbb R\), so the cotangent projection is not proper. The lifting kernel is not properly supported: over a compact input base set its output contains that set times the entire line. The averaging kernel also fails the corresponding projection condition. Although the average is defined on compact smooth functions on \(Y\), the lift of a nonzero \(g\) is constant in the middle real variable and is not compactly supported there. Its unweighted average would require \(g(x)\int_{\mathbb R}dt\), which diverges wherever \(g\ne0\). Clean matching alone does not define this product. Adding suitable integrable weights can yield a different well-defined problem, but does not prove the stated properly supported compact-fiber theorem without its hypotheses.

## References

- [Hörmander IV, §25.2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, 1985, §25.2, Definition 25.2.1 and Theorems 25.2.2–25.2.3.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*

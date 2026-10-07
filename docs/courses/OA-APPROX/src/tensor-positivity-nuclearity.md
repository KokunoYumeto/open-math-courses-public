# Tensor positivity and nuclearity

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

The minimal tensor product describes two algebras acting on separate Hilbert spaces. The maximal tensor product allows any two commuting actions on one Hilbert space. Nuclearity says that these two ways of coupling systems give the same norm. We will show that this condition is equivalent to approximation by finite-dimensional completely positive models.

The difficult direction is to turn information about all commuting actions into maps with values in the algebra itself. We do this by first encoding operators as normal functionals, then correcting one distinguished functional, and finally using separation to bring the reconstruction maps back into the algebra.

Prerequisites are [Completely positive finite models](completely-positive-finite-models.md), [Completely positive maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/completely-positive-maps.html), and [the enveloping von Neumann algebra \(A^{**}\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). The density step is proved in [Operator density from finite vector tests](../components/operator-density-foundations.md#odf06): its positive matrix approximants have the same norm bound and converge ultraweakly. Its bicommutant and entire contraction-ball arguments also supply the density inputs in the enveloping-algebra construction.

[Standard-cone geometry](../components/standard-cone-geometry.md) supplies the support, corner, orthogonal-decomposition and norm-estimate arguments used here. Every normal positive functional \(\psi\) has a unique cone representative \(\xi_\psi\), and
\[
\|\xi_\psi-\xi_\chi\|^2\le\|\psi-\chi\|.
\]
Its commutant support is obtained from its algebra support by the standard conjugation. No faithful normal state on the whole algebra is assumed. The freely accessible primary constructions are [Araki, Theorems 4 and 6](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf) and [Haagerup, Lemmas 2.6 and 2.10](https://journals.msp.org/mscand/article/download/2067/2066/2098). The [natural-cone construction](../components/natural-cone-construction.md#nc03) proves endpoint duality and self-duality from bounded multiplication. The [cyclic realization proof](../components/cyclic-cone-realization.md#cr07) constructs each positive functional by a convergent modular correction. The geometry component then gives the arbitrary-algebra reduction. We also use Hahn–Banach separation. The dilation and dominated-functional arguments use the freely readable primary papers specified in the references.

Inner products in this lesson are linear in the second variable. Unital algebras in unital assertions are nonzero.

## 1. Positive bilinear forms and the dual order

The Banach dual \(B^*\) has a matrix order: a matrix \([f_{ij}]\) is positive when
\[
[b_{ij}]\longmapsto\sum_{i,j}f_{ij}(b_{ij})
\]
is a positive functional on \(M_n(B)\). The transpose in the corresponding matrix pairing is important.

**Lemma 1.1.** A positive functional \(\omega\) on \(A\otimes_{\max}B\) determines a completely positive map
\[
\theta_\omega:A\to B^*,\qquad
\theta_\omega(a)(b)=\omega(a\otimes b).
\]
Conversely, every bounded completely positive map \(\theta:A\to B^*\) determines a positive functional on \(A\otimes_{\max}B\). The two constructions are inverse and preserve norms.

**Proof.** Suppose first that \(\omega\ge0\). If \([a_{ij}]\ge0\) and \([b_{ij}]\ge0\), write
\(a_{ij}=\sum_kx_{ki}^*x_{kj}\) and \(b_{ij}=\sum_ly_{li}^*y_{lj}\). Then
\[
\sum_{i,j}a_{ij}\otimes b_{ij}
=\sum_{k,l}\left(\sum_i x_{ki}\otimes y_{li}\right)^*
              \left(\sum_j x_{kj}\otimes y_{lj}\right)\ge0.
\]
Evaluating \(\omega\) gives positivity of \([\theta_\omega(a_{ij})]\) in the dual order. Also \(\|\theta_\omega\|\le\|\omega\|\) by the tensor cross norm.

Conversely define \(\omega(a\otimes b)=\theta(a)(b)\) algebraically. For \(z=\sum_i a_i\otimes b_i\), complete positivity applied to \([a_i^*a_j]\) and \([b_i^*b_j]\) gives \(\omega(z^*z)\ge0\).

The GNS construction for this positive algebraic functional has commuting left actions of \(A\) and \(B\). They are bounded: for \(a\in A\), the difference \(\|a\|^2z^*z-z^*(a^*a\otimes1)z\) has nonnegative \(\omega\)-value by the same matrix test, and likewise for \(b\in B\). The expressions with \(1\) denote left multiplier actions when an algebra is nonunital; their differences are finite algebraic tensors and the positive matrix test still applies. Thus the actions extend to commuting representations, giving a representation \(\pi\) of the maximal tensor product.

For unital algebras the GNS vector is \([1\otimes1]\), and the functional has norm \(\omega(1\otimes1)=\theta(1)(1)\). Its vector formula gives \(|\theta(a)(b)|\le\theta(1)(1)\|a\|\|b\|\), while testing the two units gives the reverse bound. Hence this norm is \(\|\theta\|\).

For completeness, the cyclic vector in the nonunital case can be constructed without assuming the boundedness of \(\omega\) on the tensor completion. Take positive contractive approximate identities \((e_i)\) in \(A\), \((f_j)\) in \(B\). In the algebraic GNS space,
\[
\|[e_i\otimes f_j]\|^2
=\theta(e_i^2)(f_j^2)\le\|\theta\|.
\]
Choose a weakly convergent subnet of these bounded vectors, with limit \(\xi\). For each finite algebraic tensor \(z\),
\[
\pi(z)[e_i\otimes f_j]=[z(e_i\otimes f_j)]\longrightarrow[z]
\]
in the GNS norm. Indeed, expand the squared norm of the difference into finitely many values \(\theta(a)(b)\); multiplication by the approximate identities makes their coefficients converge in the original C*-norms, and \(|\theta(a)(b)|\le\|\theta\|\|a\|\|b\|\). Hence \(\pi(z)\xi=[z]\). The same coefficient convergence gives
\[
\omega(z)=\lim_{i,j}\omega(z(e_i\otimes f_j))
=\langle[z^*],\xi\rangle
=\langle\xi,\pi(z)\xi\rangle.
\]
This vector functional is bounded on the maximal completion with norm at most \(\|\xi\|^2\le\|\theta\|\). The opposite norm inequality follows from the tensor cross norm, as in the first paragraph of the proof. Thus the constructions preserve norms in the nonunital case as well. \(\square\)

The finite-rank vector forms in a spatial representation have an especially useful factorization.

**Lemma 1.2.** Let \(A\) act on \(L\), let \(B\) act on \(H\), and take
\(\zeta=\sum_{i=1}^n u_i\otimes v_i\).
For \(\omega_\zeta(a\otimes b)=\langle\zeta,(a\otimes b)\zeta\rangle\), the associated map factors completely positively through \(M_n\).

**Proof.** Define
\[
S(a)_{ij}=\langle u_i,a u_j\rangle,\qquad
T(x)(b)=\sum_{i,j}x_{ij}\langle v_i,b v_j\rangle.
\]
The first map is compression by the operator \(e_i\mapsto u_i\), hence is completely positive. The matrix of functionals \([\langle v_i,(\,\cdot\,)v_j\rangle]\) is positive in the dual order: on a positive matrix \([b_{ij}]\), its value is \(\sum_{i,j}\langle v_i,b_{ij}v_j\rangle\ge0\).

Here is the dual matrix criterion used to conclude that \(T\) is completely positive. If \(F=[T(E_{ij})]\) is positive, take \(X=[x_{pq}]\in M_m(M_n)_+\) and \(Y=[b_{pq}]\in M_m(B)_+\). Write the positive scalar matrix \(X\), indexed by \((p,i),(q,j)\), as a sum of rank-one matrices \(\overline{u_{pi}}u_{qj}\). For each term, the pairing of \([T(x_{pq})]\) with \(Y\) is the pairing of \(F\) with the positive scalar compression \(U^*YU\). It is nonnegative. Thus \(T\) is completely positive. Necessity follows by applying \(T\) to the positive matrix \([E_{ij}]\).

Expanding the vector functional gives \(\theta_{\omega_\zeta}=TS\). If \(B\) is a concretely represented von Neumann algebra, \(T\) takes values in its predual. \(\square\)

Finite sums of these factorizations still factor through one matrix algebra, by diagonal blocks. For a positive functional \(\omega\) of norm at most \(c\), the composite map has norm at most \(c\), even when the separate maps in a chosen vector decomposition do not have norm at most one.

**Lemma 1.3.** In any faithful representation of a C*-algebra \(D\), the convex hull of its vector states is weak* dense in its state space. For a spatial representation \(D=A\otimes_{\min}B\), vectors that are finite sums of elementary tensors suffice.

**Proof.** If \(D=0\), its state space is empty and the assertion is vacuous. For a faithful representation \(\pi:D\to B(K)\), first restrict to the essential subspace \(K_{\mathrm{ess}}=\overline{\pi(D)K}\). The representation is zero on its orthogonal complement, so this restriction remains faithful and is nondegenerate. A contractive approximate identity acts strongly as the identity there; hence every unit vector in \(K_{\mathrm{ess}}\) defines a functional of norm one, and therefore a state. All unit vectors and spectral suprema below are taken in this essential representation.

If a state were outside the weak* closed convex hull, Hahn–Banach would separate it by a self-adjoint \(d\in D\). But the supremum of \(\langle\xi,d\xi\rangle\), over unit vectors, is the largest point of the spectrum of \(d\) in a faithful representation. No state can take a larger value. Applying this to \(-d\) also rules out separation on the other side.

For the spatial representation, restrict the two coefficient representations to \(L_{\mathrm{ess}}=\overline{A L}\) and \(H_{\mathrm{ess}}=\overline{B H}\). The essential subspace of their tensor representation is \(L_{\mathrm{ess}}\otimes H_{\mathrm{ess}}\); the other tensor summands carry the zero representation. Finite sums of elementary tensors from these essential spaces are norm-dense there. Normalizing a nearby nonzero vector approximates its vector state in norm, so does not change the weak* closed convex hull. \(\square\)

**Proposition 1.4.** A positive functional \(\Omega\) on \(A\otimes_{\max}B\), of norm at most one, is minimal-norm bounded if and only if its associated map \(A\to B^*\) is in the pointwise weak* closure of the finite-rank completely positive contractions.

The same equivalence holds with completely positive matrix factorizations whose composites have norm at most one in place of all finite-rank completely positive contractions.

**Proof.** If \(\Omega\) is minimal-norm bounded, Lemmas 1.2 and 1.3 approximate it by positive finite-rank vector forms, with norms at most one. Their maps are finite-rank completely positive contractions and converge pointwise weak*.

Conversely, a finite-rank bounded map \(A\to B^*\) corresponds to an algebraic sum \(\sum_k f_k\otimes g_k\), with \(f_k\in A^*\), \(g_k\in B^*\). Each such product functional is bounded on the minimal tensor product: realize the two functionals as vector coefficients of their universal representations and take their tensor product. Therefore the sum is minimal-norm bounded. If its associated map is completely positive, Lemma 1.1 gives positivity on all algebraic squares. Continuity then gives positivity on the minimal completion. Its positive-functional norm equals the norm of the associated map, so is at most one.

The weak* closed unit ball of the minimal dual, pulled back to the maximal tensor product, is closed under convergence on elementary tensors when the norms are uniformly bounded. Hence the limit functional is also minimal-norm bounded. \(\square\)

For the additional statement, the forward approximations from Lemma 1.2 already have completely positive matrix factorizations. The reverse implication holds because every such composite is a finite-rank completely positive map.

**Proposition 1.5 (Convexity of matrix factorizations).** For a target \(D\) that is a C*-algebra or a dual \(B^*\), the completely positive maps \(A\to D\) factoring through matrices form a convex cone. Their intersection with the unit ball is convex, even when only the composite norms are bounded.

**Proof.** For finitely many factorizations \(T_jS_j\) and coefficients \(t_j\ge0\), use the recording map \(S(a)=\bigoplus_j S_j(a)\) and reconstruction map \(T((x_j)_j)=\sum_jt_jT_j(x_j)\). Both are completely positive in the inherited matrix orders. Block diagonal inclusion and block compression replace the middle direct sum by one full matrix algebra. Their composite is \(\sum_jt_jT_jS_j\). If the \(t_j\)'s sum to one and the original composites have norms at most one, the triangle inequality bounds the new composite norm by one. No bounds on the separate arrows are needed for this assertion. \(\square\)

**Proposition 1.6 (Normal-valued approximation).** Let \(N\) be a von Neumann algebra. Suppose \(\Omega\) is a positive functional of norm at most one on \(A\otimes_{\min}N\) and its associated map \(\theta:A\to N^*\) has range in \(N_*\). Then \(\theta\) is in the pointwise norm closure of completely positive matrix factorizations \(A\to M_n\to N_*\) whose composites have norm at most one.

**Proof.** Use a faithful spatial representation with \(N\) normally represented. Lemmas 1.2 and 1.3 give finite-tensor vector approximations with reconstruction values in \(N_*\); their convex combinations also factor through matrices by Proposition 1.5. Their composite norms are at most one by Lemma 1.1. Their convergence against every element of \(N\) is precisely weak convergence in \(N_*\), since both the approximants and the limit take values in that predual. For each finite list from \(A\), apply Hahn–Banach to the convex image in the finite product of copies of \(N_*\). Its weak and norm closures agree, giving the assertion. A positive functional of norm less than one is handled by scaling the state approximations; the zero case is immediate. No unit or separability of \(A\) is required. \(\square\)

## 2. Keep a marginal exactly fixed

Choose a weight-constructed standard representation \(N\subset B(H)\). The marginal-correction statement concerns the abstract algebra and its predual, so this choice adds no hypothesis on \(N\). The commutant standard representation uses the opposite right Hilbert algebra and has the same cone. In translating the programme construction’s first-variable inner product to the second-variable convention here, put \([u,v]=\langle v,u\rangle\); the norm, conjugation, cone and support projections are unchanged.

Let \(N\subset B(H)\) be a von Neumann algebra in standard form. For \(\psi\in N_*^+\), write \(\xi_\psi\) for its cone vector and \(q_\psi\in N'\) for the projection onto \(\overline{N\xi_\psi}\).

We recall an elementary consequence of the GNS dominated-functional theorem. The map
\[
R_\psi:q_\psi N'q_\psi\to N_*,
\qquad
R_\psi(z)(y)=\langle\xi_\psi,yz\xi_\psi\rangle
\]
is a complete order isomorphism onto the linear span of the positive normal functionals bounded above by a scalar multiple of \(\psi\). Its inverse is not claimed bounded on an arbitrary normed subspace. On positive functionals \(f\le c\psi\), the inverse satisfies \(0\le R_\psi^{-1}(f)\le cq_\psi\).

Here is the complete order argument, including a possibly nonfaithful \(\psi\). If \(\psi=0\), both spaces are zero. Otherwise abbreviate \(q=q_\psi\) and \(\xi=\xi_\psi\). For \(0\le f\le c\psi\), Cauchy–Schwarz for \(f\) gives
\[
|f(x^*y)|^2\le f(x^*x)f(y^*y)
\le c^2\|x\xi\|^2\|y\xi\|^2.
\]
Thus the form \(f(x^*y)\) is well defined and bounded on the dense subspace \(N\xi\subset qH\). Its representing operator satisfies
\[
\langle x\xi,z_fy\xi\rangle=f(x^*y),\qquad
0\le z_f\le cq.
\]
For \(a,x,y\in N\), the form identity gives
\[
\langle x\xi,z_fay\xi\rangle=f(x^*ay)
=\langle a^*x\xi,z_fy\xi\rangle
=\langle x\xi,az_fy\xi\rangle.
\]
Density shows that \(z_f\) commutes with the restricted \(N\)-action. Extending it by zero on \((1-q)H\) gives an element of \(qN'q\). Taking \(x=1\) shows \(R_\psi(z_f)=f\).

Conversely, if \(0\le z\le cq\) in \(qN'q\), then
\[
R_\psi(z)(y)=\langle z^{1/2}\xi,yz^{1/2}\xi\rangle
\]
is normal and positive, and is at most \(c\psi\). Any element of the corner is a linear combination of four positive elements bounded by scalar multiples of \(q\). This proves the claimed range. If \(R_\psi(z)=0\), commutation gives
\[
\langle x\xi,zy\xi\rangle=R_\psi(z)(x^*y)=0
\quad(x,y\in N).
\]
Density proves injectivity, and hence also uniqueness of each \(z_f\).

To check every matrix level, take \(Z=[z_{ij}]\in M_m(qN'q)_+\) and \(Y=[y_{ij}]\in M_m(N)_+\). On \(qH\), factor the two matrices as \(Z=U^*U\) and \(qYq=V^*V\). Their entries commute across the two algebras, so
\[
\sum_{i,j}(qy_{ij}q)z_{ij}
=\sum_{k,l}\left(\sum_i v_{ki}u_{li}\right)^*
                  \left(\sum_j v_{kj}u_{lj}\right)\ge0.
\]
Its value at \(\xi\) is \(\sum_{i,j}R_\psi(z_{ij})(y_{ij})\). Thus \(R_\psi\) is completely positive in the stated dual matrix order.

For the inverse, let \([f_{ij}]\) be positive in that inherited dual order and put \(z_{ij}=R_\psi^{-1}(f_{ij})\). For arbitrary \(a_1,\ldots,a_m\in N\),
\[
\sum_{i,j}\langle a_i\xi,z_{ij}a_j\xi\rangle
=\sum_{i,j}f_{ij}(a_i^*a_j)\ge0,
\]
because \([a_i^*a_j]\) is positive. The tuples \((a_i\xi)_i\) are dense in \((qH)^m\), so \([z_{ij}]\ge0\). This proves complete positivity of the inverse without asserting any uniform inverse norm bound. It also explains why restricting to the actual support, rather than assuming a faithful state, is sufficient.

The exact norm-additive decomposition of a self-adjoint normal functional used below is [Corollary 2.8 and its polar-decomposition proof](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03). Its normal positive summands remain in the predual. The decomposition of a vector in a real self-dual cone is a separate statement.

**Lemma 2.1 (Marginal correction).** Let \(A\) be unital, and suppose a completely positive map \(\theta:A\to N_*\) is in the pointwise norm closure of completely positive matrix factorizations. Put \(\psi=\theta(1)\). For every finite \(F\subset A\) and \(\varepsilon>0\), there is a completely positive factorization \(\theta_3=TS\) through a matrix algebra such that
\[
\|\theta_3(a)-\theta(a)\|<\varepsilon\quad(a\in F),
\qquad \theta_3(1)=\psi.
\]
The recording map \(S\) may be taken unital, and \(\|\theta_3\|=\|\theta\|\).

**Proof.** The case \(\psi=0\) gives \(\theta=0\); take a state as the recording map to \(\mathbb C\) and zero as the reconstruction map. Otherwise choose a factorization \(\theta_1\) with errors less than \(\delta\) on \(F\cup\{1\}\), where \(\delta\) will tend to zero. Put \(\psi_1=\theta_1(1)\), and take the Jordan decomposition
\[
\psi-\psi_1=f-g,\qquad f,g\in N_*^+,\qquad
\|f\|+\|g\|=\|\psi-\psi_1\|<\delta.
\]
For a state \(\omega\) on \(A\), set
\(\theta_2(a)=\theta_1(a)+\omega(a)f\).
This still factors through matrices: add a scalar block to the previous factorization. Its marginal
\(\chi=\theta_2(1)=\psi_1+f\)
satisfies \(\chi\ge\psi\) and \(\|\chi-\psi\|=\|g\|<\delta\). Also
\[
\|\theta_2(a)-\theta(a)\|
<\delta+\delta\|a\|\quad(a\in F).
\]

Normalize its recording map to be unital. Explicitly, if \(\theta_2=T_0S_0\) and \(h=S_0(1)\), invert \(h^{1/2}\) on its finite-dimensional support and add a state times the complementary projection. This gives a ucp \(S\) with
\(S_0(a)=h^{1/2}S(a)h^{1/2}\).
Replace \(T_0\) by \(T_2(x)=T_0(h^{1/2}xh^{1/2})\). Then \(T_2(1)=\chi\).

By the dominated-functional theorem,
\[
B=R_\chi^{-1}T_2:M_n\to q_\chi N'q_\chi
\]
is ucp. Since \(\psi\le\chi\), its support in \(N\) is below the support of \(\chi\). Standard conjugation gives \(q_\psi\le q_\chi\), so \(q_\chi\xi_\psi=\xi_\psi\).

Define
\[
T(x)(y)=\langle\xi_\psi,yB(x)\xi_\psi\rangle.
\]
This is completely positive and normal-functional-valued, and \(T(1)=\psi\). Put \(\theta_3=TS\).

For \(z=B(S(a))\), contractivity gives \(\|z\|\le\|a\|\). Comparing its vector functionals at \(\xi_\chi\) and \(\xi_\psi\) gives
\[
\|\theta_2(a)-\theta_3(a)\|
\le\|a\|(\|\xi_\chi\|+\|\xi_\psi\|)
              \|\xi_\chi-\xi_\psi\|.
\]
The cone estimate bounds the last factor by \(\sqrt\delta\), and
\(\|\xi_\chi\|^2=\|\chi\|\le\|\psi\|+\delta\).
The right side tends to zero uniformly on the finite \(F\). Choose \(\delta\) small enough. Finally, for completely positive maps from the unital \(A\) into \(N_*\), Lemma 1.1 gives the norm as the norm of the unit value. Both maps have unit value \(\psi\), so their norms agree. In particular contractivity of the composite is retained when \(\theta\) is contractive. \(\square\)

Only finitely many normal functionals are involved at each approximation. The argument needs no countable decomposition of \(N\).

## 3. Nuclearity produces finite models

**Theorem 3.1 (Choi–Effros–Kirchberg).** For every C*-algebra \(A\), the following are equivalent:

1. \(A\) is nuclear.
2. The identity of \(A\) has cpc factorizations through matrix algebras converging pointwise in norm.

If \(A\) is unital, both factor maps may be chosen unital. If \(A\) is separable, the approximations may be a sequence; in general they are a net.

**Proof.** The implication from 2 to 1, and the assertions about unital maps and sequences, were proved in **Completely positive finite models**. We prove 1 to 2 first for unital \(A\).

**Encode finitely many tests.** Let \(a_1,\ldots,a_r\in A\) and let \(f_1,\ldots,f_s\) be positive functionals on \(A\). Put \(w=\sum_j f_j\), viewed as a normal functional on \(M=A^{**}\). Represent \(M\) in standard form, and write \(\xi=\xi_w\). Set \(N=M'\). The formula
\[
\Omega(a\otimes y)=\langle\xi,ay\xi\rangle
\quad(a\in A,\ y\in N)
\]
defines a positive functional on \(A\otimes_{\max}N\), because the two actions commute. Nuclearity makes it a positive functional on \(A\otimes_{\min}N\).

**Approximate the functional by matrix factorizations.** Represent \(A\) faithfully on a Hilbert space \(L\), keeping the given normal representation of \(N\) on \(H\). Lemmas 1.2 and 1.3 approximate \(\Omega\) weak* by positive finite-tensor vector forms and their convex combinations. Their associated maps \(A\to N_*\) factor completely positively through matrices. The limit is
\[
\theta(a)(y)=\langle\xi,ay\xi\rangle.
\]
The convergence is pointwise weak in \(N_*\), since testing against every \(y\in N\) is precisely its weak topology. Convexity and Hahn–Banach, applied in \((N_*)^r\) for each finite set, turn this into pointwise norm approximation.

**Recover an operator approximation.** Apply Lemma 2.1, with exact marginal \(\theta(1)=\psi=\omega_\xi|_N\). Take \(S:A\to M_n\) ucp and \(T:M_n\to N_*\) completely positive with \(T(1)=\psi\) and \(TS\) close to \(\theta\) on the chosen elements.

Let \(e\in M\) project onto \(\overline{N\xi}\). The dominated-functional inverse turns \(T\) into a ucp map \(T':M_n\to eMe\), where the unit of the corner is \(e\). Viewed in \(M\), \(T'\) is cpc. Each \(f_j\le w\) has a GNS Radon–Nikodym contraction \(b_j\in M'=N\) with
\[
f_j(a)=\langle b_j\xi,a b_j\xi\rangle.
\]
Thus
\[
|f_j(a-T'S(a))|
=|(\theta(a)-TS(a))(b_j^*b_j)|
\le\|\theta(a)-TS(a)\|.
\]
All positive functional tests can therefore be met. General functionals are linear combinations of four positive ones. The inclusion \(A\to M\) is consequently in the pointwise ultraweak closure of cpc matrix factorizations \(A\to M_n\to M\).

**Bring the range back into \(A\).** For a reconstruction map \(T':M_n\to M\), its positive matrix
\(C=[T'(E_{ij})]\in M_n(M)_+\)
can be approximated ultraweakly by positive matrices from \(M_n(A)\), by Kaplansky density. Their corresponding maps \(M_n\to A\) are completely positive. At this intermediate step their norms need not be one.

It follows that \(\operatorname{id}_A\) lies in the pointwise weak closure of the convex set of composites \(\beta\alpha\), with \(\alpha:A\to M_n\) ucp and \(\beta:M_n\to A\) completely positive. The set is convex by the diagonal-block construction. Hahn–Banach changes weak closure into pointwise norm closure. Include \(1\) among the finite tests. Since
\(\alpha(1)=1_n\), we then have
\[
\|\beta\|=\|\beta(1_n)\|\longrightarrow1.
\]
Dividing \(\beta\) by its norm gives cpc reconstruction maps with the same limiting identity. This proves 2 in the unital case.

**Remove the unit hypothesis.** Let \(A^\dagger=A+\mathbb C1\) have a newly adjoined unit. If \(A\) is nuclear, then \(A^\dagger\) is nuclear. Here are the tensor details. For either tensor norm \(\nu\), the maps induced by the character \(\chi:A^\dagger\to\mathbb C\) give an exact sequence
\[
0\longrightarrow A\otimes_\nu B
\longrightarrow A^\dagger\otimes_\nu B
\xrightarrow{\chi\otimes\operatorname{id}}B
\longrightarrow0.
\]
The restriction norm on the ideal is unchanged. For the maximal norm, extend any commuting representation of \(A,B\) to \(A^\dagger\) by sending its new unit to the identity; for the minimal norm use spatial functoriality. Exactness follows directly: subtract the splitting \(b\mapsto1\otimes b\) from an approximating algebraic tensor to approximate every kernel element by \(A\odot B\).

The canonical maximal-to-minimal quotient for \(A^\dagger\) is injective on this ideal by nuclearity of \(A\), and induces the identity on the quotient \(B\). Its kernel is therefore zero. This proves nuclearity of \(A^\dagger\).

Apply the unital case to \(A^\dagger\). For a positive contraction \(e\) in an approximate identity of \(A\), restrict the recording map to \(A\) and replace the reconstruction map \(\beta\) by
\(\beta_e(x)=e\beta(x)e\).
It is cpc and takes values in \(A\). For a finite \(F\subset A\), first make \(\|eae-a\|\) small and then make the approximation to \(a\) in \(A^\dagger\) small. The inequality
\[
\|e\beta\alpha(a)e-a\|
\le\|\beta\alpha(a)-a\|+\|eae-a\|
\]
finishes the proof. The zero algebra is immediate. \(\square\)

This proof explains why finite-dimensional models need not be subalgebras. Positivity first gives approximating maps in a much larger space. Convexity, the unit test and the matrix criterion put their values back into the original algebra.

## 4. Two other forms of approximation

**Corollary 4.1.** A C*-algebra \(A\) is nuclear if and only if, for every C*-algebra \(B\) and every completely positive contraction \(\theta:A\to B^*\), \(\theta\) is a pointwise weak* limit of completely positive factorizations through matrices whose composites have norm at most one. If \(A\) is nuclear, pointwise norm approximation is possible.

**Proof.** Nuclearity gives cpc \(\beta_i\alpha_i\to\operatorname{id}_A\). Compose \(\beta_i\) with \(\theta\). Since \(\theta\) is contractive, the errors still tend to zero in norm, and all composite norms are at most one.

Conversely, let \(\Omega\) be a positive functional of norm at most one on \(A\otimes_{\max}B\), and apply the hypothesized approximation to its map \(\theta_\Omega\) from Lemma 1.1. A factorization \(TS\) gives a positive functional on the minimal tensor product: use the completely positive tensor map \(S\otimes\operatorname{id}\) and the positive functional on \(M_n\otimes B\) associated with \(T\). The norm of this positive functional is the norm of \(TS\), hence at most one.

Pointwise weak* convergence of \(TS\) is convergence of these functionals on all elementary tensors. Their norm bound extends convergence to all algebraic finite sums and ensures that the limit is minimal-norm bounded. Every positive unit-ball functional on the maximal tensor product is therefore minimal-norm bounded. Such functionals determine the C*-norm by evaluating positive elements, so the two norms agree. \(\square\)

In the dual formulation, the middle space must carry the dual norm. Section 7 proves the [coefficient complete-order identification](#coefficient-dual-order) and [adjoint positivity](#adjoint-dual-order); it also makes [matrix-level positivity of CP tensoring](#cp-tensor-positivity) explicit.

**Corollary 4.2.** \(A\) is nuclear if and only if \(\operatorname{id}_{A^*}\) is a pointwise weak* limit of completely positive contractions factoring as
\[
A^*\longrightarrow M_n^*\longrightarrow A^*,
\]
with both arrows contractive in their Banach norms and completely positive in the dual matrix orders.

**Proof.** Adjoint the cpc primal factorizations from Theorem 3.1. Adjoint maps preserve norms and complete positivity in the dual orders. For \(f\in A^*\), \(a\in A\), the resulting composite satisfies
\[
(\alpha_i^*\beta_i^*f)(a)=f(\beta_i\alpha_i(a))\longrightarrow f(a).
\]

Conversely, let \(\gamma_i:A^*\to M_{n_i}^*\), \(\delta_i:M_{n_i}^*\to A^*\) be the proposed maps. For any positive maximal-tensor functional \(\Omega\) of norm at most one, view its associated map instead as \(\theta_\Omega:B\to A^*\). Lemma 1.1 gives \(\|\theta_\Omega\|=\|\Omega\|\le1\). The finite-rank completely positive maps \(\delta_i\gamma_i\theta_\Omega\) have norm at most one and converge pointwise weak* to \(\theta_\Omega\).

The coefficient pairing \(x\mapsto[y\mapsto\operatorname{Tr}(x^{\mathsf T}y)]\) is a complete order isomorphism \(M_n\to M_n^*\). Using it converts each factorization to one through \(M_n\); the separate norms can change, but the composite norm remains at most one. The reverse argument of Corollary 4.1 applies, with the tensor factors interchanged. Hence \(A\) is nuclear. \(\square\)

Here \(M_n^*\) is the trace-class matrix space, with its Banach dual norm. It is not the operator-norm matrix space. A complete order identification alone does not preserve a contractivity assertion.

## 5. Type I algebras

The [spatial type I factor construction](#type-i-spatial-form) and [irreducible norm detection](#irreducible-norm-detection) used in the next proof are given in Section 7.

**Theorem 5.1.** Every type I C*-algebra is nuclear.

**Proof.** Recall that type I means every generated von Neumann algebra \(\pi(A)''\) is type I. Let \(\rho\) be an irreducible representation of \(A\otimes_{\max}B\), and let \(\pi_A,\pi_B\) be its commuting coefficient representations. Put \(M=\pi_A(A)''\). A central element of \(M\) commutes with \(M\) and with \(\pi_B(B)\), hence with the irreducible joint representation. It is scalar, so \(M\) is a type I factor.

Thus the Hilbert space splits as \(K\otimes L\), with \(M=B(K)\otimes1\). The \(B\)-action lies in \(M'=1\otimes B(L)\). Consequently the joint representation is spatial, so
\(\|\rho(z)\|\le\|z\|_{\min}\) for \(z\in A\odot B\).
Irreducible representations detect the C*-norm of \(A\otimes_{\max}B\). Taking their supremum proves \(\|z\|_{\max}\le\|z\|_{\min}\). \(\square\)

The commutative and finite-dimensional examples in **Completely positive finite models** also fit this theorem, but their explicit sampling and compression maps give more information than the abstract type I argument.

## 6. Exercises with solutions

**Exercise 1 (Check the tensor positivity; intermediate).** For positive matrices \([a_{ij}]\in M_n(A)\) and \([b_{ij}]\in M_n(B)\), verify directly that \(\sum_{i,j}a_{ij}\otimes b_{ij}\) is positive in the maximal tensor product.

*Solution.* Factor the two matrices as \(X^*X\) and \(Y^*Y\), and expand as in Lemma 1.1. The sum becomes
\(\sum_{k,l}z_{kl}^*z_{kl}\), where \(z_{kl}=\sum_i x_{ki}\otimes y_{li}\). Each summand is positive.

**Exercise 2 (The transpose in the pairing; introductory).** Show that \(\sum_{ij}x_{ij}y_{ij}=\operatorname{Tr}(x^{\mathsf T}y)\), and that this generally differs from \(\operatorname{Tr}(xy)\).

*Solution.* Expanding the trace gives \(\sum_{i,j}x_{ji}y_{ji}\), which is the required sum after renaming indices. With \(x=y=E_{12}\), the coefficient sum is one, while \(xy=0\) and its trace is zero.

**Exercise 3 (Norms distinguish a space from its dual; introductory).** Let \(F_n\in M_n^*\) be \(F_n(x)=\operatorname{Tr}(x)\). Compute \(\|F_n\|\), and compare it with the operator norm of the matrix \(1_n\).

*Solution.* For \(\|x\|\le1\), \(|\operatorname{Tr}(x)|\le n\). Equality holds at \(1_n\), so \(\|F_n\|=n\). The matrix \(1_n\) has operator norm one. The transpose trace pairing sends \(1_n\) to \(F_n\), so is not a Banach-space isometry for \(n>1\).

**Exercise 4 (An impossible dual approximation; advanced).** Put \(E=\ell^1(\{1,2\})\), with its coordinate positive cone. If \(S:E\to M_n\) and \(T:M_n\to E\) are positive contractions, prove that \(TS\) cannot have error less than \(1/2\) on both coordinate unit vectors.

*Solution.* Each \(S(e_j)\) is a positive contraction, so \(0\le S(e_j)\le1_n\). Therefore \(0\le TS(e_j)\le T(1_n)\), coordinatewise. If \(\|TS(e_1)-e_1\|_1<1/2\), the first coordinate of \(T(1_n)\) is greater than \(1/2\). Error less than \(1/2\) on \(e_2\) forces the same for its second coordinate. Then \(\|T(1_n)\|_1>1\), contradicting contractivity. This is why the middle space in Corollary 4.2 uses the dual matrix norm.

**Exercise 5 (Exact marginal, small error; intermediate).** In Lemma 2.1, estimate \(\|\chi-\psi\|\) when \(\|\psi_1-\psi\|<\delta\), and give the resulting vector estimate.

*Solution.* With \(\psi-\psi_1=f-g\), the corrected marginal is \(\chi=\psi_1+f=\psi+g\). Thus \(\|\chi-\psi\|=\|g\|<\delta\), and the standard-cone estimate gives \(\|\xi_\chi-\xi_\psi\|<\sqrt\delta\).

**Exercise 6 (The unit test controls the outgoing norm; intermediate).** Suppose \(\alpha:A\to M_n\) is ucp, \(\beta:M_n\to A\) is completely positive, and \(\|\beta\alpha(1)-1\|<\delta<1\). Show that \(|\|\beta\|-1|<\delta\) and estimate the extra error from replacing \(\beta\) by \(\beta/\|\beta\|\).

*Solution.* Since \(\alpha(1)=1_n\), \(\|\beta\|=\|\beta(1_n)\|\), and the reverse triangle inequality gives the first bound. For \(a\in A\),
\[
\|(\beta/\|\beta\|)\alpha(a)-\beta\alpha(a)\|
\le|1-\|\beta\||\,\|a\|<\delta\|a\|.
\]
The equality for the map norm holds because its domain is unital and the map is completely positive.

**Exercise 7 (Ideal permanence; intermediate).** Use Theorem 3.1 and the ideal approximation argument in **Completely positive finite models** to prove that a closed ideal of a nuclear C*-algebra is nuclear.

*Solution.* Nuclearity of \(A\) gives the completely positive approximation property by Theorem 3.1. Restrict the recording maps to the ideal and compress the reconstruction maps by a positive contraction from its approximate identity. This gives the same property for the ideal. The tensor-norm implication then gives nuclearity.

## 7. Operator and matrix-order details

The following proofs supply the representation and dual-order facts used above.

<a id="type-i-spatial-form"></a>
### Type I factors in their given representation

Use the [Hilbert-space and kernel constructions H00–H02](regular-group-operator-foundations.md#h00), [bounded polar decomposition T04a](regular-group-operator-foundations.md#t04a), C*-functional calculus F01–F08, and the [projection lattice C02](projection-comparison-and-finite-traces.md#c02) and [central contact C04](projection-comparison-and-finite-traces.md#c04).

Let \(M\subset B(H)\) be a nonzero type I factor. The defining condition for type I, applied to the nonzero central projection \(1\), supplies \(p\ne0\) with \(pMp\) commutative. A nonzero projection in a factor has central support one, because its central support is a nonzero central projection.

If \(0<q<p\) were a projection, then \(qM(p-q)=q(pMp)(p-q)=0\), since \(pMp\) is commutative. The central-contact proof C04 gives \(c(q)c(p-q)=0\), contradicting both central supports being one. Thus \(p\) is minimal. Moreover \(pMp=\mathbb Cp\). Indeed, a self-adjoint \(a\in pMp\) with two distinct spectral values admits two disjoint nonnegative continuous functions, nonzero at the respective values. Their calculi are nonzero positive elements with orthogonal supports in \(pMp\), by H02. One of those supports is a nonzero proper subprojection of \(p\), impossible. Therefore every self-adjoint \(a\) has singleton spectrum and is scalar by the normal spectral-radius formula; splitting real and imaginary parts proves the assertion.

By Zorn choose a maximal orthogonal family \((p_i)_{i\in I}\) of projections equivalent to \(p\), containing \(p\). Chain unions are admissible; all families lie in the fixed projection set of \(M\). Its join \(P\) belongs to \(M\) by the projection-lattice proof C02. If \(q=1-P\ne0\), then \(c(p)=c(q)=1\), so the central-contact proof C04 gives a nonzero element in \(qMp\). Its polar partial isometry has nonzero initial support below \(p\), hence initial support \(p\), and final support below \(q\). This supplies another orthogonal copy of \(p\), contradicting maximality. Consequently \(\sum_i p_i=1\), with arbitrary sums meaning strong limits of finite partial sums.

Put \(L=pH\), \(K=\ell^2(I)\), and choose \(u_i\in M\) with \(u_i^*u_i=p\), \(u_i u_i^*=p_i\). The map
\[
W:L\otimes K\longrightarrow H,\qquad W(\zeta\otimes\delta_i)=u_i\zeta
\]
is isometric on finite-support vectors: the cross terms vanish since \(u_i^*u_j=0\) for \(i\ne j\). Its range contains every \(p_iH\), whose span is dense; hence it is unitary.

For \(x\in M\), each matrix entry of \(W^*xW\) is \(u_i^*xu_j|_L\in pMp=\mathbb Cp\). Thus it is \(\lambda_{ij}1_L\). Choose a unit vector \(\zeta_0\in L\). Compression to \(\mathbb C\zeta_0\otimes K\) shows that \((\lambda_{ij})\) defines a bounded operator \(a\in B(K)\) with \(\|a\|\le\|x\|\). Equality of entries on finite tensors gives \(W^*xW=1_L\otimes a\).

Conversely, for \(a\in B(K)\) and a finite subset \(F\subset I\), its coordinate compression \(a_F=P_FaP_F\) satisfies
\[
W(1_L\otimes a_F)W^*=\sum_{i,j\in F} a_{ij}u_i u_j^*\in M.
\]
The coordinate projections \(P_F\) tend strongly to \(1_K\), and the \(a_F\) are uniformly bounded by \(\|a\|\). Bounded strong multiplication gives \(a_F\to a\) strongly, and therefore \(1_L\otimes a_F\to1_L\otimes a\) strongly, first on finite elementary tensors and then on all vectors. Strong closedness yields \(W(1_L\otimes a)W^*\in M\). Thus \(W^*MW=1_L\otimes B(K)\).

An operator commuting with all \(1_L\otimes E_{ij}\) has off-diagonal entries zero and equal diagonal entries, by multiplying the matrix units. It consequently has the form \(b\otimes1_K\) for a bounded \(b\in B(L)\). Conversely every such operator commutes with \(1_L\otimes B(K)\), first on entries and then by finite-coordinate density. Hence \(W^*M'W=B(L)\otimes1_K\). Flipping the two Hilbert factors gives the exact spatial form used by tensor Theorem 5.1. This proof includes every nonzero finite or infinite cardinal \(I\); no countability assumption is used.

<a id="irreducible-norm-detection"></a>
### Irreducible representations detect the C*-norm

Use positive scalar Cauchy–Schwarz, C*-functional calculus, the [positive norm-preserving scalar extension](completely-positive-finite-models.md#lemma-2-2), and the GNS, separation and compactness proofs in [Hypertraces and finite injective algebras, Section 1](hypertraces-finite-injectivity.md). The compact-face argument below supplies the needed extreme point directly.

For a possibly nonunital nonzero C*-algebra \(D\), let \(Q=\{f\in D^*:f\ge0,\ \|f\|\le1\}\). This is weak* compact: positivity is closed on every positive element, and COMPACT gives the compact dual unit ball. It is convex. A faithful representation supplies vector functionals in \(Q\), and the quadratic-form characterization and order calculus give
\(\sup_{f\in Q}f(h)=\|h\|\) for \(h\ge0\).
For \(x\ne0\), set \(h=x^*x\); then
\[
F=\{f\in Q:f(h)=\|h\|\}
\]
is a nonempty compact face. Nonemptiness follows by compactness and the displayed supremum. The face property follows because both values in any convex decomposition are at most \(\|h\|\).

Every nonempty compact convex subset of a Hausdorff locally convex space has an extreme point: order its nonempty compact faces by reverse inclusion; a nested chain has nonempty intersection by compactness and that intersection is a face. Zorn gives a minimal compact face. If it had two distinct points, a continuous real linear functional separating them would attain its maximum on a proper nonempty compact face, a contradiction. Thus the minimal face is a singleton. Applied to \(F\), this gives an extreme point \(\varphi\) of \(F\), which is also extreme in \(Q\). It is nonzero.

Its norm is one, since otherwise \(\varphi=\|\varphi\|(\varphi/\|\varphi\|)+(1-\|\varphi\|)0\) is a nontrivial convex decomposition in \(Q\). For positive functionals, the norm is the limit of their values on a positive contractive approximate identity \((e_i)\). One direct proof is
\[
|f(ae_i)|^2\le f(e_i^2)f(aa^*)
\le f(e_i)\|f\|\|a\|^2.
\]
Take the limit on the left for each \(a\), then take a norming supremum. Together with \(f(e_i)\le\|f\|\), this proves \(f(e_i)\to\|f\|\). Therefore, if \(0\le g\le\varphi\), then
\(\|g\|+\|\varphi-g\|=1\). Normalize the two nonzero summands. Extremality gives \(g=\lambda\varphi\). Thus \(\varphi\) is pure.

In its cyclic GNS representation \((\pi,H,\xi)\), a positive contraction \(T\in\pi(D)'\) defines \(g(a)=\langle\xi,\pi(a)T\xi\rangle\), with \(0\le g\le\varphi\). Purity gives \(g=\lambda\varphi\). Evaluating at \(b^*a\) and using density of \(\pi(D)\xi\) gives \(T=\lambda1\). Every commutant element is a linear combination of positive contractions, so \(\pi(D)'=\mathbb C1\), equivalently \(\pi\) is irreducible. Finally
\[
\|\pi(x)\|\ge\|\pi(x)\xi\|=\varphi(x^*x)^{1/2}=\|x\|,
\]
and contractivity gives equality. For \(x=0\) no detection is needed. The zero algebra has no nonzero irreducible representation and all relevant norms are zero.

For completeness, the nonunital cyclic-vector construction follows from positive extension and the unital GNS proof. Extend \(f\) by Hahn–Banach to a functional \(F\) on its forced unitization with \(\|F\|=r=\|f\|\). Since \(\|1-2e_i\|\le1\), we have \(|F(1)|\le r\) and \(|F(1)-2f(e_i)|\le r\). Letting \(f(e_i)\to r\), the two discs \(|z|\le r\), \(|z-2r|\le r\) meet only at \(z=r\); hence \(F(1)=r\). The norming-positivity lemma gives \(F\ge0\). Its unital GNS vector satisfies
\(\|\xi-\pi(e_i)\xi\|^2\le\|f\|-f(e_i)\to0\).
Consequently \(\xi\) belongs to the essential subspace of the restricted representation; its restriction is cyclic and nondegenerate. This uses no bidual.

<a id="coefficient-dual-order"></a>
### Complete order of the coefficient matrix dual

Let \(I_n:M_n\to M_n^*\) be \(I_n(x)(y)=\operatorname{Tr}(x^{\mathsf T}y)=\sum_{a,b}x_{ab}y_{ab}\). It is a linear bijection by entry recovery. At level \(m\), identify \(X=[x_{ij}]\) and \(Y=[y_{ij}]\) with scalar matrices on the index set \(\{1,\ldots,m\}\times\{1,\ldots,n\}\). Their dual pairing is
\[
\sum_{i,j}I_n(x_{ij})(y_{ij})
=\sum_{i,j,a,b}X_{(i,a),(j,b)}Y_{(i,a),(j,b)}
=\operatorname{Tr}(X^{\mathsf T}Y).
\]
If \(X,Y\ge0\), then \(X^{\mathsf T}\ge0\) and
\(\operatorname{Tr}(X^{\mathsf T}Y)
=\operatorname{Tr}(Y^{1/2}X^{\mathsf T}Y^{1/2})\ge0\).
Conversely, if this expression is nonnegative for every \(Y\ge0\), test rank-one \(Y=vv^*\). Then \(v^*X^{\mathsf T}v\ge0\) for every \(v\), forcing \(X^{\mathsf T}\), and hence \(X\), to be positive by finite polarization. Thus \(I_n\) and its inverse preserve positivity at every matrix level. This proves the exact complete-order assertion in Corollary 4.2 without asserting a Banach-norm isometry.

<a id="adjoint-dual-order"></a>
### Adjoint maps preserve the stated dual complete order

If \(\phi:C\to D\) is completely positive, then \(\phi^*:D^*\to C^*\) is completely positive: for a positive functional matrix \(F=[f_{ij}]\) and \(X=[x_{ij}]\in M_m(C)_+\),
\(\sum f_{ij}(\phi(x_{ij}))\ge0\), because \(\phi_m(X)\ge0\). Conversely, if \(\phi^*\) is completely positive, positive matrices in \(M_m(D)\) are separated from the complement of their closed convex cone by scalar positive functionals, so the same test forces \(\phi_m(X)\ge0\). Only the forward implication is consumed in Corollary 4.2. Norm equality of an adjoint follows from Hahn–Banach norming functionals, already provided in F01.

<a id="cp-tensor-positivity"></a>
### CP tensoring in the precise finite-model reverse route

The [finite-model tensor lemma](completely-positive-finite-models.md#lemma-4-1) states contractivity; its written compression proof also proves complete positivity. In the minimal case its formula is compression of the tensor *-representation. At every matrix level, compressions of a positive operator matrix are positive. In the maximal case, the fully written commuting-action dilation in that same proof gives, for every commuting target representation, compression of a *-representation of the maximal source product. Testing positive elements in faithful representations gives positivity, and applying the identical construction to finite matrix amplifications gives complete positivity. Rescaling handles a bounded CP map whose norm is not one; the zero map is immediate.

For a nonunital domain, the later approximate-identity paragraph of the same full Lemma 4.1 constructs its dilation operator by a bounded form and weak limit. That construction, with no second commuting action, also supplies the minimal-case dilation. The exact finite-model body and the unital dilation are public; the same formulas give the required positive compressions at every matrix level.

## References

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorems 1.1.1 and 1.3.1 provide the dilation and commuting-action methods used in the preceding finite-model lesson. Lemma 1.4.1 and Theorem 1.4.2 prove the order correspondence between dominated completely positive maps and operators in the dilation commutant. Section 2 above supplies the cyclic scalar case and both matrix-order directions explicitly. The tensor-duality, convexity and nuclearity consequences are proved in this lesson.

Huzihiro Araki, [Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf), *Pacific Journal of Mathematics* 50 (1974), 309–354. Theorem 4(6)–(8), printed pp.326–332, proves orthogonal positive decomposition, orthogonality of supports and the cone-vector norm estimate. Theorem 6, pp.335–339, constructs the cone vector of each normal positive functional in the cyclic and separating setting. These are the cone ingredients needed in the marginal correction, rather than an assumption that two density operators commute.

Uffe Haagerup, [The standard form of von Neumann algebras](https://doi.org/10.7146/math.scand.a-11606), *Mathematica Scandinavica* 37 (1975), 271–283. Lemmas 2.6 and 2.10 treat standard-form corners and normal positive functionals. Lemma 2.10 uses Araki's cyclic-case result and reduces arbitrary von Neumann algebras to the appropriate support corner. This retains the general scope of Lemma 2.1 and Theorem 3.1.

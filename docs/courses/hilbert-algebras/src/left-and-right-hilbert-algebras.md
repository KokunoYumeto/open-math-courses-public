# Left and right Hilbert algebras

*Written by Claude Opus 5.5 (Anthropic), September 2026, extended October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October additions (Lemma 3.5, Theorem 3.6 and the revision of the references) are self-checked by the writing AI. Example 6.7 and Proposition 6.8 were drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

A left Hilbert algebra is an algebra with an involution that sits densely in a Hilbert space and acts on it by bounded left multiplication. Every faithful normal semifinite weight on a von Neumann algebra produces a left Hilbert algebra. Conversely, every left Hilbert algebra produces a von Neumann algebra together with a faithful normal semifinite weight, a modular operator and a modular conjugation. Left Hilbert algebras therefore give a concrete way to handle weights.

This lesson works out the basic examples and the basic structure. Sections 3–5 treat three families of examples: the commutative algebras \(L^2\cap L^\infty\) of a measure space, the convolution algebra \(C_c(G)\) of a locally compact group with its left and right structures, and algebras of finite-rank operators that realize every weight \(\operatorname{Tr}(h^2\,\cdot\,)\) on \(B(\mathcal K)\). Sections 6–9 prove four structural results. Vectors in the domain of the closed involution give closed multipliers affiliated with the von Neumann algebra, and this hypothesis cannot be dropped; the closed multipliers of such a vector and of its image under the involution are adjoint to each other for commutative algebras, but not in general. Two left Hilbert algebras are equivalent exactly when there is a weight-preserving isomorphism of their von Neumann algebras. The full completion is a Banach algebra for a natural norm, and fullness can be read off the unit ball. A left Hilbert algebra that fills its whole Hilbert space generates a direct sum of type I factors. Section 10 has further exercises with solutions.

We assume the general theory of left Hilbert algebras from the course *Modular theory and weights*: the lessons *Closing an involution and recovering its modular data*, *Building the two multiplication actions of a Hilbert algebra*, *Right Hilbert algebra density and commutants*, *Weights and the Hilbert spaces of multiplication* and *Approximating multiplication without losing its bound*, and, for the group algebra, *The Plancherel weight and Fourier coefficients of a locally compact group*. From this course we use Haar measure on locally compact groups and Spatial tensor products of von Neumann algebras. Section 2 states the outside results that we use; facts about Haar measure and Hilbert–Schmidt operators are recalled where they are needed.

In the early 1950s, Hilbert algebras with an isometric involution were used to prove the commutation theorem for the regular representation of a unimodular group, and [Dixmier 1952] extended the theory to quasi-unitary algebras in order to handle groups that are not unimodular. Left Hilbert algebras in the present generality come from Tomita's modular theory, as presented by Takesaki, and [Combes 1971] constructed the weight associated with a left Hilbert algebra.

## 1. Setting and notation

Hilbert spaces are complex and of any dimension, and the zero space is allowed. Inner products are linear in the first variable. For a set \(\mathcal S\subseteq B(H)\), \(\mathcal S'\) is its commutant. Nothing in this lesson assumes separability, countability, a unit or a faithful state. Sequences are used only to test closedness in metrizable spaces; global approximations use nets.

**Definition 1.1.** Let \(H\) be a Hilbert space, and let \(\mathcal A\subseteq H\) be a dense subspace that is also a complex associative algebra with a conjugate-linear involution \(a\mapsto a^\sharp\), so that \((ab)^\sharp=b^\sharp a^\sharp\) and \((a^\sharp)^\sharp=a\). We call \(\mathcal A\) a *left Hilbert algebra* in \(H\) if it satisfies the following four axioms.

1. For each \(a\in\mathcal A\), the map \(b\mapsto ab\) is bounded on \(\mathcal A\) for the norm of \(H\).
2. \(\langle ab,c\rangle=\langle b,a^\sharp c\rangle\) for all \(a,b,c\in\mathcal A\).
3. The involution, viewed as a conjugate-linear operator in \(H\) with domain \(\mathcal A\), is closable.
4. The span \(\mathcal A^2\) of all products \(ab\) is dense in \(H\).

A *right Hilbert algebra* is defined in the same way, with the involution written \(\flat\): right multiplication \(a\mapsto ab\) by each fixed \(b\) is bounded, \(\langle ab,c\rangle=\langle a,cb^\flat\rangle\), the involution is closable, and the products are dense. A left Hilbert algebra whose involution is isometric, \(\|a^\sharp\|=\|a\|\), is called a *unimodular Hilbert algebra*.

Fix a left Hilbert algebra \(\mathcal A\subseteq H\). The following objects are attached to it, and we use this notation throughout.

- For \(a\in\mathcal A\), \(L_a\in B(H)\) is the bounded extension of \(b\mapsto ab\). The von Neumann algebra \(M=L(\mathcal A)''\) is the *left von Neumann algebra* of \(\mathcal A\).
- \(S\) is the closure of the involution, with domain \(D(S)\), and \(F=S^*\) is its adjoint, with domain \(D(F)\). The *modular operator* is \(\Delta=FS\). The *modular conjugation* \(J\) is the antiunitary in the polar decomposition \(S=J\Delta^{1/2}\) (Fact 2.4).
- A vector \(\eta\in H\) is *right bounded* if there is a constant \(c\) with \(\|L_a\eta\|\leq c\|a\|\) for all \(a\in\mathcal A\). These vectors form the space \(\mathcal B_r\). For \(\eta\in\mathcal B_r\), \(R_\eta\in B(H)\) is the bounded extension of \(a\mapsto L_a\eta\), and \(\mathfrak n_r=R(\mathcal B_r)\).
- The *right algebra* is \(\mathcal A_r=\mathcal B_r\cap D(F)\). Its product is \(\eta\zeta=R_\zeta\eta\) and its involution is \(F\); we also write \(\eta^\flat=F\eta\).
- A vector \(\xi\in H\) is *left bounded* if there is a constant \(c\) with \(\|R_\eta\xi\|\leq c\|\eta\|\) for all \(\eta\in\mathcal A_r\). These vectors form the space \(\mathcal B_l\). For \(\xi\in\mathcal B_l\), \(\lambda_\xi\in B(H)\) is the bounded operator with \(\lambda_\xi\eta=R_\eta\xi\) for \(\eta\in\mathcal A_r\), and \(\mathfrak n_l=\lambda(\mathcal B_l)\).
- The *full completion* of \(\mathcal A\) is \(\mathcal A_l=\mathcal B_l\cap D(S)\), with product \(\xi\zeta=\lambda_\xi\zeta\) and involution \(S\). We call \(\mathcal A\) *full* when \(\mathcal A=\mathcal A_l\).
- The *weight* of \(\mathcal A\) is the map \(\psi\) on \(M_+\) with \(\psi(a)=\|\xi\|^2\) if \(a^{1/2}=\lambda_\xi\) for some \(\xi\in\mathcal B_l\), and \(\psi(a)=+\infty\) otherwise. It is a faithful normal semifinite weight on \(M\) (Fact 2.10).
- A *projection* of a left Hilbert algebra is a vector \(e\neq0\) with \(ee=e=e^\sharp\).
- A closed operator \(T\) is *affiliated* with a von Neumann algebra \(N\) if \(uD(T)=D(T)\) and \(Tu\xi=uT\xi\) for every unitary \(u\in N'\) and every \(\xi\in D(T)\).

When several algebras occur, we add an index or the name of the algebra: \(\mathcal A_{1,l}\), \(\psi_2\), \(\mathcal B_r(\mathcal C)\), \(\mathcal C_r\), and so on.

## 2. Results used from other lessons

Facts 2.1–2.12 are proved in the course *Modular theory and weights*; after each one we name the lesson that proves it. Facts 2.13 and 2.14 are standard; for them we name the lessons of the course *Foundations of von Neumann algebras* that prove them, and one textbook. Throughout, \(\mathcal A\subseteq H\) is a left Hilbert algebra with the notation of Section 1.

**Fact 2.1** (left multiplication). The map \(a\mapsto L_a\) is linear, multiplicative and injective, and \(L_{a^\sharp}=L_a^*\). (Building the two multiplication actions of a Hilbert algebra)

**Fact 2.2** (adjoints of conjugate-linear operators). Let \(A\) be a conjugate-linear operator with dense domain in \(H\). Its adjoint \(A^*\) is defined as follows: \(y\in D(A^*)\) and \(A^*y=z\) exactly when \(\langle Ax,y\rangle=\langle z,x\rangle\) for all \(x\in D(A)\). A vector \(y\) lies in \(D(A^*)\) exactly when \(x\mapsto\langle Ax,y\rangle\) is bounded on \(D(A)\). The adjoint is closed. The operator \(A\) is closable exactly when \(D(A^*)\) is dense, and then \((\overline A)^*=A^*\) and \(A^{**}=\overline A\). The same statements hold for linear operators and their usual adjoints. The canonical map \(C_H\) from \(H\) onto the conjugate Hilbert space \(\overline H\) is a conjugate-linear isometry, so \(C_HA\) is linear whenever \(A\) is conjugate-linear. (Closing an involution and recovering its modular data)

**Fact 2.3** (the two involutions). The operator \(S\) is closed and densely defined, it maps \(D(S)\) onto itself, and \(S^2x=x\) for \(x\in D(S)\). The same holds for \(F\) on \(D(F)\). The two involutions satisfy the *adjoint relation*
\[
\langle Sx,y\rangle=\langle Fy,x\rangle\qquad(x\in D(S),\ y\in D(F)).
\]
(Building the two multiplication actions of a Hilbert algebra)

**Fact 2.4** (polar decomposition). Let \(S\) be a closed, densely defined, conjugate-linear operator that maps its domain onto itself with \(S^2=I\) there, and let \(F=S^*\). There is exactly one pair consisting of an antiunitary \(J\) and a positive self-adjoint operator \(A\) with \(S=JA\) and \(D(S)=D(A)\). For this pair, \(A=\Delta^{1/2}\) with \(\Delta=FS\), \(A\) is injective, \(J^2=I\), and
\[
S=J\Delta^{1/2}=\Delta^{-1/2}J,\qquad F=J\Delta^{-1/2}=\Delta^{1/2}J,\qquad D(F)=D(\Delta^{-1/2}).
\]
(Closing an involution and recovering its modular data)

**Fact 2.5** (right-bounded vectors and the right algebra). The space \(\mathcal B_r\) is a vector space, the map \(\eta\mapsto R_\eta\) is linear and injective, and \(R_\eta\in M'\). If \(\eta\in\mathcal A_r\), then \(F\eta\in\mathcal A_r\) and \(R_{F\eta}=R_\eta^*\). For \(\eta,\zeta\in\mathcal A_r\),
\[
R_{\eta\zeta}=R_\zeta R_\eta,\qquad(\eta\zeta)^\flat=\zeta^\flat\eta^\flat .
\]
(Building the two multiplication actions of a Hilbert algebra)

**Fact 2.6** (density of the right algebra). The right algebra \(\mathcal A_r\) is a right Hilbert algebra. Both \(\mathcal A_r\) and the span \(\mathcal A_r^2\) of its products are graph cores for \(F\), and \(R(\mathcal A_r)''=M'\). The product span \(\mathcal A^2\) is a graph core for \(S\); equivalently, for \(v,w\in H\), the identities \(\langle a^\sharp b,v\rangle=\langle w,b^\sharp a\rangle\) for all \(a,b\in\mathcal A\) hold exactly when \(v\in D(F)\) and \(Fv=w\). Finally, if \(\eta,\zeta\in\mathcal B_r\) and \(R_\eta^*=R_\zeta\), then \(\eta\in D(F)\) and \(F\eta=\zeta\). (Right Hilbert algebra density and commutants)

**Fact 2.7** (closed right multipliers and affiliation). (a) Let \(\mathcal C\subseteq B(H)\) be a \(*\)-algebra, and let \(T\) be a closed operator with \(cD(T)\subseteq D(T)\) and \(Tc\xi=cT\xi\) for all \(c\in\mathcal C\) and \(\xi\in D(T)\). If \(\mathcal C''=N'\) for a von Neumann algebra \(N\), then \(T\) is affiliated with \(N\). (b) For \(\eta\in D(F)\), the operator \(a\mapsto L_a\eta\) with domain \(\mathcal A\) is closable, and its closure is affiliated with \(M'\). (Building the two multiplication actions of a Hilbert algebra)

**Fact 2.8** (left-bounded vectors and the full completion). The map \(\xi\mapsto\lambda_\xi\) is linear and injective from \(\mathcal B_l\) into \(M\). It is *covariant*: for \(x\in M\) and \(\xi\in\mathcal B_l\), we have \(x\xi\in\mathcal B_l\) and \(\lambda_{x\xi}=x\lambda_\xi\). So \(\mathfrak n_l\) is a left ideal of \(M\). Moreover \(\mathcal A\subseteq\mathcal A_l\), and \(\lambda_a=L_a\) for \(a\in\mathcal A\). The full completion \(\mathcal A_l\) is a left Hilbert algebra, the closure of the restriction of \(S\) to \(\mathcal A_l\) is \(S\), \(\lambda_{S\xi}=\lambda_\xi^*\) for \(\xi\in\mathcal A_l\), \(\lambda(\mathcal A_l)''=M\), and \(\lambda(\mathcal A_l)=\mathfrak n_l\cap\mathfrak n_l^*\). The two multiplications are compatible: \(\lambda_\xi\eta=R_\eta\xi\) for all \(\xi\in\mathcal B_l\) and \(\eta\in\mathcal B_r\). (Weights and the Hilbert spaces of multiplication)

In particular, the product \(\xi\eta=\lambda_\xi\eta\) of \(\xi\in\mathcal B_l\) with any \(\eta\in H\) is consistent with the earlier products. For \(\xi=a\in\mathcal A\) it is the left product \(L_a\eta\), because \(\lambda_a=L_a\). For \(\eta\in\mathcal B_r\) it is the right product \(R_\eta\xi\), by the compatibility just stated.

**Fact 2.9** (the full completion is full). The right algebra of \(\mathcal A_l\) is \(\mathcal A_r\), with the same products, involution and right operators. Consequently \(\mathcal A\) and \(\mathcal A_l\) have the same \(S\), \(F\), \(\Delta\), \(J\), \(M\), \(\mathcal B_r\), \(R\), \(\mathcal A_r\), \(\mathcal B_l\), \(\lambda\) and \(\psi\). Dualizing \(\mathcal A_l\) gives back \(\mathcal A_r\), and dualizing once more gives back \(\mathcal A_l\): the full completion of \(\mathcal A_l\) is \(\mathcal A_l\) itself, so \(\mathcal A_l\) is full. (Weights and the Hilbert spaces of multiplication)

**Fact 2.10** (the weight). The weight \(\psi\) of \(\mathcal A\) is a faithful normal semifinite weight on \(M\). Its left ideal of elements of finite weight is \(\mathfrak n_\psi=\lambda(\mathcal B_l)\), and \(\psi(\lambda_\xi^*\lambda_\xi)=\|\xi\|^2\) for \(\xi\in\mathcal B_l\). Conversely, let \(\varphi\) be a faithful normal semifinite weight on a von Neumann algebra \(N\), with GNS map \(\Lambda_\varphi\colon\mathfrak n_\varphi\to H_\varphi\). Then \(\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)\), with the product \(\Lambda_\varphi(x)\Lambda_\varphi(y)=\Lambda_\varphi(xy)\) and the involution \(\Lambda_\varphi(x)^\sharp=\Lambda_\varphi(x^*)\), is a full left Hilbert algebra in \(H_\varphi\). Its left von Neumann algebra is the image of \(N\) in the GNS representation, and its weight is \(\varphi\), transported by that representation. (Weights and the Hilbert spaces of multiplication)

**Fact 2.11** (bounded approximation). (a) If \((\xi_i)\) is a net in \(\mathcal B_l\) with \(\xi_i\to\xi\) in \(H\) and \(\lambda_{\xi_i}\to x\) strongly for some \(x\in M\), then \(\xi\in\mathcal B_l\) and \(\lambda_\xi=x\). (b) For every \(\xi\in\mathcal A_l\) there are \(a_n\in\mathcal A\) with \(a_n\to\xi\), \(a_n^\sharp\to S\xi\) and \(\|L_{a_n}\|\leq\|\lambda_\xi\|\). (c) For every \(\xi\in\mathcal B_l\) there are \(a_n\in\mathcal A\) with \(a_n\to\xi\) and \(\|L_{a_n}\|\leq\|\lambda_\xi\|\). (Approximating multiplication without losing its bound)

**Fact 2.12** (examples from the prerequisite lessons).

- (a) If the involution of \(\mathcal A\) is isometric, then \(\mathcal A\) is also a right Hilbert algebra with the same involution. (Building the two multiplication actions of a Hilbert algebra)
- (b) If \(\mathcal A\) has a unit \(e\), then \(\mathcal B_r=M'e\) and \(R_{xe}=x\) for \(x\in M'\). Moreover \(e\in\mathcal A_r\), and \(e\) is a two-sided unit of \(\mathcal A_r\). (Building the two multiplication actions of a Hilbert algebra)
- (c) Let \(N\) be a von Neumann algebra on \(H\) with a cyclic and separating vector \(\Omega\). Then \(N\Omega\), with the product \((a\Omega)(c\Omega)=(ac)\Omega\) and the involution \((a\Omega)^\sharp=a^*\Omega\), is a left Hilbert algebra with unit \(\Omega\), and its left von Neumann algebra is \(N\). For example, let \(B(\ell^2(\mathbb N))\) act by left multiplication on the Hilbert–Schmidt operators on \(\ell^2(\mathbb N)\); then \(\rho^{1/2}\), with \(\rho=\operatorname{diag}(2^{-n})\), is a cyclic and separating vector. (Closing an involution and recovering its modular data)
- (d) Let \(I\) be a set and \(\mu_i>0\) for \(i\in I\). The finitely supported functions \(c_{00}(I)\), with pointwise product and complex conjugation, form a left Hilbert algebra in \(\ell^2(I,\mu)\). For it, \(\mathcal B_r=\mathcal A_r=\ell^2(I,\mu)\cap\ell^\infty(I)\), \(R_\eta\) is multiplication by \(\eta\), and \(M=M'\) is the algebra of bounded multiplication operators. (Right Hilbert algebra density and commutants)
- (e) Let \(I\) be a set, and let \(t_i>0\) and \(D_i=\operatorname{diag}(1,t_i)\) for \(i\in I\). The finitely supported families \(a=(a_i)\) of \(2\times2\) matrices, with blockwise product and the matrix adjoint as involution, form a left Hilbert algebra for the inner product \(\langle a,b\rangle=\sum_i\operatorname{Tr}(D_ib_i^*a_i)\). Its Hilbert space consists of the families \(\eta=(\eta_i)\) with \(\sum_i\operatorname{Tr}(D_i\eta_i^*\eta_i)<\infty\), and \(D(S)=\{\eta\in H:(\eta_i^*)_i\in H\}\) with \((S\eta)_i=\eta_i^*\). (Building the two multiplication actions of a Hilbert algebra)
- (f) For a probability space \((X,\mu)\), the multiplication operators by functions in \(L^\infty(X,\mu)\) form a von Neumann algebra on \(L^2(X,\mu)\) that equals its own commutant. (Closing an involution and recovering its modular data)

**Fact 2.13** (analysis). We use the closed graph theorem; the spectral theorem and the Borel functional calculus for self-adjoint operators, bounded or not, including positive square roots and the inverse of an injective positive operator; Chebyshev's inequality; the dominated convergence theorem; and the fact that every \(L^2\)-convergent sequence has an almost everywhere convergent subsequence. The closed graph theorem is in
Hahn–Banach, Baire and the basic theorems on Banach spaces, Section 5;
the bounded spectral theorem and Borel calculus in The spectral theorem for bounded self-adjoint
operators; the unbounded case in Spectral calculus
with its domains retained, §§SK-04–SK-07; the measure-theoretic facts in Measure
and Hilbert space tools for Haar integration.

**Fact 2.14** (von Neumann algebras). Let \(N\) be a von Neumann algebra, \(x\in N\) self-adjoint, and \(g\) a bounded Borel function on the spectrum of \(x\). Then \(g(x)\in N\). In particular every spectral projection \(1_\Omega(x)\) lies in \(N\), and it is nonzero when \(\Omega\) is open and meets the spectrum of \(x\). A projection \(p\in N\) is *abelian* if \(pNp\) is abelian, and a factor is of *type I* if it has a nonzero abelian projection. The function \(g(x)\) commutes with every operator
commuting with \(x\) (The spectral theorem for bounded self-adjoint operators, Theorem
3.1(5)), so it lies in \(N''=N\); if \(\Omega\) is open
and meets the spectrum, take a continuous function \(f\) supported in \(\Omega\) with \(f(\lambda)\ne0\) at a point
\(\lambda\) of the spectrum; then \(f(x)\ne0\), because the continuous functional calculus is isometric (C\*-algebras:
continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients, Section
5), and
\(f(x)=f(x)1_\Omega(x)\) by Theorem 3.1(1) and (2) of the spectral lesson, so \(1_\Omega(x)\ne0\). The types are those of Projections and types of von Neumann algebras,
Definition 7.1.

## 3. Commutative left Hilbert algebras and measure spaces

The model example of a left Hilbert algebra is \(L^2\cap L^\infty\) of a measure space, and one can think of measure theory as the study of commutative left Hilbert algebras. This section makes part of that picture precise. Proposition 3.1 goes from measure spaces to algebras, for an arbitrary measure space. Proposition 3.2 proves one necessary condition for the way back: a commutative left Hilbert algebra is automatically unimodular. The converse, that every full commutative left Hilbert algebra is \(L^2\cap L^\infty\) of a measure space, is Theorem 3.6; it rests on the representation of an abelian von Neumann algebra with a faithful normal semifinite trace as an \(L^\infty\) space (Lemma 3.5). Example 3.3 shows that the algebra forgets the parts of a measure space that square-integrable functions cannot reach, and Example 3.4 gives a commutative algebra that is not full.

**Proposition 3.1.** Let \((X,\Sigma,\mu)\) be any measure space. Let \(\mathcal A=L^2(\mu)\cap L^\infty(\mu)\): classes of square-integrable functions \(f\) with \(|f|\leq c\) almost everywhere for some \(c\), with \(\|f\|_\infty\) the least such \(c\). Use pointwise products, complex conjugation, and the inner product of \(H=L^2(\mu)\).

1. \(\mathcal A\) is a left Hilbert algebra. Its closed involution is complex conjugation \(C\) on \(H\), and \(F=S=J=C\), \(\Delta=I\).
2. \(\mathcal B_r=\mathcal B_l=\mathcal A\), and \(R_\eta=\lambda_\eta=m_\eta\), multiplication by \(\eta\), with \(\|m_\eta\|=\|\eta\|_\infty\).
3. \(\mathcal A\) is full.

No \(\sigma\)-finiteness or semifiniteness of \(\mu\) is assumed.

**Proof.** (1) For \(f\in\mathcal A\) and \(g\in H\), \(|fg|\leq\|f\|_\infty|g|\) almost everywhere, so \(\|fg\|_2\leq\|f\|_\infty\|g\|_2\): left multiplication is bounded and \(L_f=m_f\). The identity \(\langle fg,k\rangle=\int fg\bar k\,d\mu=\langle g,\bar fk\rangle\) is the adjoint axiom. The space \(\mathcal A\) is dense in \(H\): for \(g\in H\), the truncations \(g1_{\{|g|\leq n\}}\) lie in \(\mathcal A\) and converge to \(g\) by dominated convergence. Conjugation is isometric on \(\mathcal A\), so it is closable, and its closure is the antiunitary \(C\) of \(H\). For products, let \(f\in\mathcal A\) and \(E_n=\{|f|>1/n\}\). Chebyshev's inequality gives \(\mu(E_n)\leq n^2\|f\|_2^2<\infty\), so \(1_{E_n}\in\mathcal A\) and \(f1_{E_n}=f\cdot1_{E_n}\in\mathcal A^2\). As \(f=0\) off \(\bigcup_nE_n\), dominated convergence gives \(f1_{E_n}\to f\). So \(\mathcal A^2\) is dense. An antiunitary involution \(C\) satisfies \(\langle Cx,y\rangle=\langle Cx,C(Cy)\rangle=\langle Cy,x\rangle\). By the definition of the adjoint (Fact 2.2), this says \(F=C^*=C\). Then \(\Delta=FS=C^2=I\), and \(J=C\) by the uniqueness of the polar decomposition (Fact 2.4).

(2) If \(\eta\in\mathcal A\), then \(\|L_f\eta\|=\|f\eta\|\leq\|\eta\|_\infty\|f\|\), so \(\eta\in\mathcal B_r\) with \(R_\eta=m_\eta\). Conversely let \(\eta\in\mathcal B_r\), with \(\|f\eta\|\leq c\|f\|\) for all \(f\in\mathcal A\). If \(c=0\), testing with \(f=1_{\{|\eta|>1/n\}}\), which lies in \(\mathcal A\) by Chebyshev's inequality, shows \(\eta=0\). If \(c>0\), let \(\varepsilon>0\) and \(E=\{|\eta|>c+\varepsilon\}\). Then \(\mu(E)<\infty\) by Chebyshev's inequality, so \(1_E\in\mathcal A\), and
\[
(c+\varepsilon)^2\mu(E)\leq\|1_E\eta\|^2\leq c^2\mu(E).
\]
So \(\mu(E)=0\) and \(\|\eta\|_\infty\leq c\). Taking \(c=\|R_\eta\|\) gives \(\|m_\eta\|=\|\eta\|_\infty\). Since \(D(F)=H\), \(\mathcal A_r=\mathcal A\). Left boundedness is tested against the operators \(R_\eta\) with \(\eta\in\mathcal A_r=\mathcal A\), and \(R_\eta\xi=\eta\xi\). This is the same test with the two factors exchanged, so \(\mathcal B_l=\mathcal A\) and \(\lambda_\xi=m_\xi\).

(3) \(\mathcal A_l=\mathcal B_l\cap D(S)=\mathcal A\). \(\square\)

**Proposition 3.2** (commutative means unimodular). Suppose the product of the left Hilbert algebra \(\mathcal A\) is commutative: \(ab=ba\) for all \(a,b\in\mathcal A\). Then \(\langle a^\sharp,b^\sharp\rangle=\langle b,a\rangle\) for all \(a,b\). Hence \(S\) is antiunitary, \(F=S=J\), \(\Delta=I\), and \(\mathcal A\) is a unimodular Hilbert algebra.

**Proof.** Fix \(a\in\mathcal A\). For \(b\in\mathcal A\), \(L_ba=ba=ab=L_ab\), so \(\|L_ba\|\leq\|L_a\|\|b\|\). Thus \(a\in\mathcal B_r\) with \(R_a=L_a\). The same holds for \(a^\sharp\), and \(R_{a^\sharp}=L_{a^\sharp}=L_a^*=R_a^*\) by Fact 2.1. The last criterion of Fact 2.6, applied to \(\eta=a\) and \(\zeta=a^\sharp\), gives \(a\in D(F)\) and \(Fa=a^\sharp\). Now take \(a,b\in\mathcal A\). What we just proved, applied to \(b^\sharp\), gives \(b^\sharp\in D(F)\) and \(Fb^\sharp=(b^\sharp)^\sharp=b\). So the adjoint relation (Fact 2.3) with \(x=a\) and \(y=b^\sharp\) gives
\[
\langle a^\sharp,b^\sharp\rangle=\langle Sa,b^\sharp\rangle=\langle Fb^\sharp,a\rangle=\langle b,a\rangle .
\]
So \(\sharp\) is isometric, and its closure \(S\) is an antiunitary involution. As in Proposition 3.1, \(F=S^*=S\), \(\Delta=S^2=I\) and \(J=S\). \(\square\)

**Example 3.3** (what the algebra cannot see).

- (i) Let \(X=\{p\}\) with \(\mu(\{p\})=\infty\). Then \(L^2(\mu)=\{0\}\), and \(\mathcal A\) is the zero algebra.
- (ii) Let \(X=\{p,q\}\) with \(\mu(\{p\})=1\) and \(\mu(\{q\})=\infty\). A function is square integrable exactly when it vanishes at \(q\). So \(H=\mathbb C1_{\{p\}}\), \(\mathcal A=H\) is the one-dimensional algebra with unit \(1_{\{p\}}\), and \(M=\mathbb C\). The point \(q\) has positive measure, and \(L^\infty(\mu)=\mathbb C^2\) sees it, but it leaves no trace in the Hilbert algebra. So a measure space that is not a single point can have a one-dimensional Hilbert algebra. The Hilbert algebra keeps only the part of the measure space that square-integrable functions can reach.
- (iii) Even all the function spaces can be one-dimensional. Let \(X\) be uncountable, let \(\Sigma\) consist of the countable sets and their complements, and let \(\mu\) be \(0\) on countable sets and \(1\) on the others. For a real measurable \(f\), the number \(t_0=\sup\{t:\mu(\{f>t\})=1\}\) is finite, because the sets \(\{f>-n\}\) cover \(X\) and the sets \(\{f>n\}\) have empty intersection. The set \(\{f\neq t_0\}\) is contained in the countable union of the countable sets \(\{f>t_0+1/n\}\) and \(\{f\leq t_0-1/n\}\). So every measurable function is constant almost everywhere (apply this to its real and imaginary parts), \(L^2(\mu)=L^\infty(\mu)=\mathbb C1\), and \(\mathcal A=\mathbb C1\), although every point of \(X\) is a null set.

**Example 3.4** (a commutative algebra that is not full). Let \(\mathcal C=C_c(0,1)\) in \(L^2(0,1)\), with Lebesgue measure, pointwise product and conjugation. It is a commutative left Hilbert algebra: it is a \(*\)-subalgebra of the algebra of Proposition 3.1, it is dense (density of compactly supported functions), and \(\mathcal C^2=\mathcal C\) because \(f=fg\) for any \(g\in C_c(0,1)\) equal to \(1\) on the support of \(f\). Its full completion is \(L^\infty(0,1)\). Indeed, let \(\eta\in L^2(0,1)\) satisfy \(\|f\eta\|\leq c\|f\|\) for \(f\in\mathcal C\), and let \(f\in L^\infty(0,1)\) with \(|f|\leq\beta\). Choose \(f_n\in\mathcal C\) with \(f_n\to f\) in \(L^2\) and almost everywhere (a subsequence of an \(L^2\)-convergent sequence). Let \(\tau(z)=z\) for \(|z|\leq\beta\) and \(\tau(z)=\beta z/|z|\) otherwise. Then \(g_n=\tau\circ f_n\) lies in \(\mathcal C\), \(|g_n|\leq\beta\), \(g_n\to f\) almost everywhere, and \(\|g_n-f\|\leq\|f_n-f\|\) because \(\tau\) is \(1\)-Lipschitz and fixes the values of \(f\). Dominated convergence, with bound \(4\beta^2|\eta|^2\), gives \(g_n\eta\to f\eta\) in \(L^2\). So \(\|f\eta\|\leq c\|f\|\). Hence \(\mathcal B_r(\mathcal C)\) equals \(\mathcal B_r\) of Proposition 3.1, namely \(L^\infty(0,1)\), and then \(\mathcal C_r=L^\infty(0,1)\), \(\mathcal B_l(\mathcal C)=L^\infty(0,1)\) and \(\mathcal C_l=L^\infty(0,1)\). The indicator of \((0,\tfrac12)\) lies in \(\mathcal C_l\) but not in \(\mathcal C\).

**Lemma 3.5** (abelian algebras with a trace as \(L^\infty\) spaces). Let \(N\) be an abelian von Neumann algebra and \(\tau\) a faithful normal semifinite trace on \(N\). There are pairwise disjoint compact spaces \(K_i\) (\(i\in I\)) with finite positive Radon measures \(\mu_i\) of support \(K_i\), and a \(*\)-isomorphism \(\Phi\) of \(N\) onto \(L^\infty(X,\mu)\), where \(X=\bigcup_iK_i\), the measurable sets are the \(E\subseteq X\) with every \(E\cap K_i\) Borel, and \(\mu(E)=\sum_i\mu_i(E\cap K_i)\), such that \(\tau(x)=\int_X\Phi(x)\,d\mu\) for every \(x\in N_+\).

**Proof.** By Zorn's lemma choose a maximal family \((e_i)_{i\in I}\) of mutually orthogonal nonzero projections of finite trace. Then \(\sum_ie_i=1\): otherwise \(1-\sum_ie_i\) majorizes a nonzero projection of finite trace, because \(\tau\) is semifinite (Traces on von Neumann algebras, Proposition 2.5), against maximality. Each \(e_i\) is central, so \(x\mapsto(xe_i)_i\) is a \(*\)-isomorphism of \(N\) onto the algebra of bounded families \((x_i)\) with \(x_i\in Ne_i\): a bounded family is the image of its strongly convergent sum \(\sum_ix_i\in N\), and \(x=\sum_ixe_i\) strongly.

Fix \(i\). The algebra \(Ne_i\) is an abelian von Neumann algebra on \(e_iH\) with unit \(e_i\), and \(\tau\) restricts to a faithful normal finite trace on it. Let \(K_i\) be its spectrum and \(x\mapsto\hat x\) its Gelfand isomorphism onto \(C(K_i)\) (C\*-algebras, Theorem 2.1), an isometric \(*\)-isomorphism that preserves and reflects order. By the Riesz representation theorem (Haar measure on locally compact groups) there is a finite positive Radon measure \(\mu_i\) on \(K_i\) with \(\tau(x)=\int\hat x\,d\mu_i\) for \(x\in Ne_i\). It is *normal* in the sense of Abelian operator algebras, Definition 5.1: a bounded increasing net in \(C_{\mathbb R}(K_i)\) comes from a bounded increasing net in \(Ne_i\), whose strong limit is its least upper bound (Lemma 2.4 there), and \(\tau\) is normal. The space \(K_i\) is stonean, as the spectrum of an abelian von Neumann algebra (Theorem 7.1 there), so the support of \(\mu_i\) is clopen (Corollary 5.4(3) there). If it were not \(K_i\), the indicator of its complement would be \(\hat q\) for a nonzero projection \(q\in Ne_i\) with \(\tau(q)=0\), against faithfulness. So Theorem 5.5 there makes \(x\mapsto[\hat x]\) an isometric \(*\)-isomorphism of \(Ne_i\) onto \(L^\infty(K_i,\mu_i)\).

Replacing the \(K_i\) by disjoint copies, the bounded measurable functions on \(X\) are the bounded families of Borel functions on the \(K_i\), and a set is \(\mu\)-null exactly when its trace on each \(K_i\) is null. So \(L^\infty(X,\mu)\) is the algebra of bounded families of elements of the \(L^\infty(K_i,\mu_i)\), and \(\Phi(x)=([\widehat{xe_i}])_i\) is a \(*\)-isomorphism of \(N\) onto it. For \(x\in N_+\) the finite partial sums of \(\sum_ixe_i\) increase to \(x\), so normality of \(\tau\) gives \(\tau(x)=\sum_i\tau(xe_i)=\sum_i\int_{K_i}\widehat{xe_i}\,d\mu_i=\int_X\Phi(x)\,d\mu\). \(\square\)

**Theorem 3.6** (full commutative left Hilbert algebras). Let \(\mathcal A\subseteq H\) be a full left Hilbert algebra with commutative product. Let \((X,\mu)\) and \(\Phi\) be given by Lemma 3.5 for \(N=M\) and \(\tau=\psi\), the weight of \(\mathcal A\). There is a unitary \(U:H\to L^2(X,\mu)\) such that

1. \(U\xi=\Phi(\lambda_\xi)\) for \(\xi\in\mathcal B_l\), in particular \(Ua=\Phi(L_a)\) for \(a\in\mathcal A\);
2. \(U\mathcal A=L^2(\mu)\cap L^\infty(\mu)\), \(U(ab)=U(a)\,U(b)\) and \(U(a^\sharp)=\overline{U(a)}\) for \(a,b\in\mathcal A\);
3. \(UxU^*\) is multiplication by \(\Phi(x)\), for every \(x\in M\).

So \(\mathcal A\) is isomorphic, by a unitary that carries products, involution and left von Neumann algebra, to the algebra of Proposition 3.1 for the measure space \((X,\mu)\).

**Proof.** The operators \(L_a\) commute with each other, since \(L_aL_b=L_{ab}=L_{ba}=L_bL_a\) (Fact 2.1), and \(L_a^*=L_{a^\sharp}\). So \(L(\mathcal A)\) is a commutative self-adjoint set, its commutant contains it, and \(M=L(\mathcal A)''\) is abelian. The weight \(\psi\) is faithful, normal and semifinite (Fact 2.10), and on an abelian algebra it is a trace, as \(x^*x=xx^*\). Lemma 3.5 applies.

For \(\xi\in\mathcal B_l\), \(\lambda_\xi\in\mathfrak n_\psi\) and \(\psi(\lambda_\xi^*\lambda_\xi)=\|\xi\|^2\) (Fact 2.10), so \(\int|\Phi(\lambda_\xi)|^2d\mu=\|\xi\|^2\). The map \(V\xi=\Phi(\lambda_\xi)\) is therefore a linear isometry of \(\mathcal B_l\) into \(L^2(X,\mu)\), and its range is \(\Phi(\mathfrak n_\psi)\), the set of \(f\in L^\infty(\mu)\) with \(\int|f|^2d\mu<\infty\), that is \(L^2(\mu)\cap L^\infty(\mu)\), because \(\mathfrak n_\psi=\lambda(\mathcal B_l)\) (Fact 2.10). As \(\mathcal B_l\supseteq\mathcal A\) is dense in \(H\) and \(L^2\cap L^\infty\) is dense in \(L^2\) (proof of Proposition 3.1), \(V\) extends to a unitary \(U\). This is (1), since \(\lambda_a=L_a\) (Fact 2.8). By Proposition 3.2, \(S\) is antiunitary, so \(D(S)=H\) and \(\mathcal A=\mathcal A_l=\mathcal B_l\cap D(S)=\mathcal B_l\); hence \(U\mathcal A=L^2\cap L^\infty\). Products and involution are carried over by \(\Phi(L_{ab})=\Phi(L_a)\Phi(L_b)\) and \(\Phi(L_{a^\sharp})=\Phi(L_a^*)=\overline{\Phi(L_a)}\). For (3), let \(x\in M\) and \(\xi\in\mathcal B_l\). By covariance (Fact 2.8), \(x\xi\in\mathcal B_l\) and \(\lambda_{x\xi}=x\lambda_\xi\), so \(U(x\xi)=\Phi(x)\,U\xi\). The vectors \(U\xi\) are dense, so \(UxU^*=m_{\Phi(x)}\). \(\square\)

The measure space of Theorem 3.6 is a disjoint union of finite measure spaces. It is not determined by \(\mathcal A\): by Example 3.3, different measure spaces can give the same algebra.

## 4. The group algebra of a locally compact group

Let \(G\) be a locally compact group. No countability, \(\sigma\)-compactness or unimodularity is assumed. Fix a left Haar measure \(ds\). We write \(\delta\) for its modular function and keep \(\Delta\) for the modular operator; the lesson on Haar measure writes \(\Delta\) for the modular function. Then
\[
\int f(ts)\,dt=\delta(s)^{-1}\int f(t)\,dt,\qquad \int f(t^{-1})\,dt=\int f(t)\,\delta(t)^{-1}\,dt
\tag{4.1}
\]
by the definition of the modular function and the inversion formula. Put \(H=L^2(G)\). On \(C_c(G)\) define
\[
(\xi*\eta)(s)=\int\xi(t)\,\eta(t^{-1}s)\,dt,\qquad
\xi^\sharp(s)=\delta(s)^{-1}\,\overline{\xi(s^{-1})},\qquad
\xi^\flat(s)=\overline{\xi(s^{-1})}.
\tag{4.2}
\]
Note that \(\xi^\sharp=\delta^{-1}\xi^\flat\) as functions.

The left structure is treated in the lesson *The Plancherel weight and Fourier coefficients of a locally compact group*, and we use the following facts from it. The algebra \((C_c(G),*,\sharp)\) is a left Hilbert algebra in \(H\). Its closed involution is \(S=JD^{1/2}\), where \(D\) is multiplication by \(\delta\) on its largest domain and \((J\xi)(s)=\delta(s)^{-1/2}\overline{\xi(s^{-1})}\). So its modular operator is \(\Delta=D\). Its products are dense, because \(G\) has approximate identities in \(C_c(G)\). Its left von Neumann algebra \(M=L(C_c(G))''\) is the von Neumann algebra generated by the left translations, and \(M'=R(C_c(G))''\), where \(R_\eta\) is right convolution by \(\eta\). The next theorem supplies the right structure and shows how it sits inside the constructions of Section 1.

**Theorem 4.1.** Let \(G\) be any locally compact group.

1. For \(\eta\in C_c(G)\), the map \(\xi\mapsto\xi*\eta\) sends \(C_c(G)\) into itself and extends to a bounded operator \(R_\eta\) on \(H\) with
\[
\|R_\eta\|\leq\int|\eta(t)|\,\delta(t)^{-1/2}\,dt.
\tag{4.3}
\]
2. \(\langle\xi*\eta,\zeta\rangle=\langle\xi,\zeta*\eta^\flat\rangle\) for all \(\xi,\eta,\zeta\in C_c(G)\).
3. \(\flat\) is a conjugate-linear involution of \(C_c(G)\) that reverses products.
4. Let \(F=S^*\) be the adjoint involution of the left Hilbert algebra \((C_c(G),*,\sharp)\). Then \(F\eta=\eta^\flat\) for \(\eta\in C_c(G)\), and \(C_c(G)\) is a graph core for \(F\).
5. \((C_c(G),*,\flat)\) is a right Hilbert algebra. More precisely, \(C_c(G)\subseteq\mathcal A_r\), where \(\mathcal A_r\) is the right algebra of \((C_c(G),*,\sharp)\). The product of \(\mathcal A_r\) restricts to \(*\), its involution restricts to \(\flat\), and its right operators are the \(R_\eta\) of part 1. The operators \(R_\eta\), \(\eta\in C_c(G)\), generate \(M'\).
6. The following are equivalent: (a) \(G\) is unimodular; (b) \(\sharp\) is isometric; (c) \(\flat\) is isometric; (d) \(\sharp=\flat\). In that case \(C_c(G)\) is a unimodular Hilbert algebra.

*Remark.* The standard statement is that \(C_c(G)\) with the involution \(\flat\) is a right Hilbert algebra; parts 4 and 5 add that it is a \(*\)-subalgebra of \(\mathcal A_r\) that is a graph core for \(F\) and generates \(M'\).

**Proof.** (1) The convolution of two functions in \(C_c(G)\) lies in \(C_c(G)\), and \((\xi*\eta)(s)=\int\xi(st^{-1})\eta(t)\delta(t)^{-1}\,dt\) (convolution on a locally compact group). Fix \(\xi,\zeta\in C_c(G)\). The function \((s,t)\mapsto\xi(st^{-1})\eta(t)\delta(t)^{-1}\overline{\zeta(s)}\) is continuous with compact support on \(G\times G\). So we may integrate in \(s\) first, because the two iterated integrals of such a function agree:
\[
\langle\xi*\eta,\zeta\rangle=\int\eta(t)\,\delta(t)^{-1}\,\langle\rho_t\xi,\zeta\rangle\,dt,\qquad(\rho_t\xi)(s)=\xi(st^{-1}).
\]
Right translation changes \(L^2\) norms by the modular function: \(\|\rho_t\xi\|=\delta(t^{-1})^{-1/2}\|\xi\|=\delta(t)^{1/2}\|\xi\|\). Hence \(|\langle\xi*\eta,\zeta\rangle|\leq c_\eta\|\xi\|\|\zeta\|\), where \(c_\eta\) is the right side of (4.3). Since \(C_c(G)\) is dense in \(H\), \(\|\xi*\eta\|\leq c_\eta\|\xi\|\), and the map extends. (The weak-integral formula for right convolution in the lesson on the Plancherel weight, and the convolution inequalities, give bounds of the same kind.)

(2) Let \(k(t,s)=\xi(t)\eta(t^{-1}s)\overline{\zeta(s)}\), a continuous function with compact support on \(G\times G\). The left side is \(\int(\int k(t,s)\,dt)\,ds\). For the right side, \((\zeta*\eta^\flat)(t)=\int\zeta(s)\eta^\flat(s^{-1}t)\,ds=\int\zeta(s)\overline{\eta(t^{-1}s)}\,ds\). So \(\langle\xi,\zeta*\eta^\flat\rangle=\int\xi(t)\big(\int\overline{\zeta(s)}\eta(t^{-1}s)\,ds\big)\,dt=\int(\int k(t,s)\,ds)\,dt\). The two iterated integrals agree, as in part 1. No invariance of the measure is used here.

(3) Conjugate-linearity and \((\xi^\flat)^\flat=\xi\) are clear. For products, substitute \(t=s^{-1}u\) (left invariance):
\[
(\xi*\eta)^\flat(s)=\int\overline{\xi(t)\eta(t^{-1}s^{-1})}\,dt
=\int\overline{\eta(u^{-1})}\;\overline{\xi(s^{-1}u)}\,du
=\int\eta^\flat(u)\,\xi^\flat(u^{-1}s)\,du=(\eta^\flat*\xi^\flat)(s).
\]

(4) As recalled above, \(S=JD^{1/2}\) with \(D(S)=D(D^{1/2})\). Here \(J\) is antiunitary and \(D^{1/2}\) is positive self-adjoint, so this is the polar decomposition of \(S\), and Fact 2.4 gives \(F=JD^{-1/2}\) with \(D(F)=D(D^{-1/2})\). For \(\eta\in C_c(G)\),
\[
(JD^{-1/2}\eta)(s)=\delta(s)^{-1/2}\,\overline{\delta(s^{-1})^{-1/2}\eta(s^{-1})}=\overline{\eta(s^{-1})}=\eta^\flat(s),
\]
because \(\delta(s^{-1})^{-1/2}=\delta(s)^{1/2}\). So \(F\eta=\eta^\flat\). Since \(J\) is isometric, the graph norm of \(F\) is \(\big(\int|\eta|^2(1+\delta^{-1})\,ds\big)^{1/2}\), and \(D(F)\) is exactly \(L^2((1+\delta^{-1})ds)\). The measure \((1+\delta^{-1})ds\) is Radon, because its density is continuous and positive, so \(C_c(G)\) is dense in that space (Radon measures with continuous densities, and density of \(C_c\)). This is the graph-core claim. (The same argument, for the density \(1+\delta\), appears in the lesson on Haar measure.)

(5) For \(\xi,\eta\in C_c(G)\), \(L_\xi\eta=\xi*\eta=R_\eta\xi\). By (1), \(\|L_\xi\eta\|\leq c_\eta\|\xi\|\), so \(\eta\in\mathcal B_r\) and its right operator is the \(R_\eta\) of part 1. By (4), \(\eta\in D(F)\), so \(\eta\in\mathcal A_r\) and \(F\eta=\eta^\flat\). In \(\mathcal A_r\) the product of \(\eta\) and \(\zeta\) is \(R_\zeta\eta=\eta*\zeta\). So \((C_c(G),*,\flat)\) is a \(*\)-subalgebra of \(\mathcal A_r\). It has bounded right multiplication by (1) and the adjoint identity by (2). Its involution is closable, since \(\flat\subseteq F\) and \(F\) is closed. Its products are dense, by the approximate identities already used for the left structure. So it is a right Hilbert algebra. Finally \(R(C_c(G))''=M'\) was recalled above.

(6) By (4.1), applied to \(u\mapsto\delta(u)^2|\xi(u)|^2\) and to \(|\xi|^2\),
\[
\|\xi^\sharp\|^2=\int\delta(s)^{-2}|\xi(s^{-1})|^2\,ds=\int\delta\,|\xi|^2\,ds,\qquad
\|\xi^\flat\|^2=\int|\xi(s^{-1})|^2\,ds=\int\delta^{-1}|\xi|^2\,ds.
\tag{4.4}
\]
If \(\delta\equiv1\), then (b), (c) and (d) hold. If \(\delta(s_0)\neq1\), choose an open \(U\ni s_0\) on which \(\delta-1\) has one sign, and a nonzero \(\xi\in C_c(U)\) (Urysohn's lemma). Then (4.4) gives \(\|\xi^\sharp\|\neq\|\xi\|\) and \(\|\xi^\flat\|\neq\|\xi\|\). Also \(\xi^\flat\) is nonzero somewhere on \(U^{-1}\), where \(\delta=\delta(\cdot^{-1})^{-1}\neq1\), so \(\xi^\sharp=\delta^{-1}\xi^\flat\neq\xi^\flat\). In the unimodular case \(\sharp\) is isometric, so \(C_c(G)\) is a unimodular Hilbert algebra; by Fact 2.12(a) it is then also a right Hilbert algebra with the same involution. \(\square\)

**Remark 4.2.** Part 5 says that the right structure is not a new object: it is a \(*\)-subalgebra of the right algebra \(\mathcal A_r\) that is a graph core for \(F\) and generates \(M'\). The two involutions differ by the modular function, \(\eta^\flat=\delta\,\eta^\sharp\). This matches the operator identity \(F=\Delta S\) on \(\{x\in D(S):Sx\in D(\Delta)\}\), which follows from \(S=\Delta^{-1/2}J\) and \(F=\Delta^{1/2}J\) (Fact 2.4). We do not compute the full completion of the right Hilbert algebra \((C_c(G),*,\flat)\) directly from it.

### Worked examples

**Example 4.3** (discrete groups). Let \(\Gamma\) be a discrete group with counting measure, so \(\delta\equiv1\) (discrete groups are unimodular). Then \(C_c(\Gamma)=\mathbb C[\Gamma]\), and \(\sharp=\flat\) is \(f^*(s)=\overline{f(s^{-1})}\). The point mass \(e=1_{\{1\}}\) is a unit with \(e^*=e\). The involution is isometric, so \(S=F\) is the antiunitary \(f\mapsto f^*\) of \(\ell^2(\Gamma)\), \(D(S)=\ell^2(\Gamma)\), \(\Delta=I\) and \(J=S\). By Fact 2.12(b), \(\mathcal B_r=M'e\) with \(R_{xe}=x\), and \(e\) is a two-sided unit of \(\mathcal A_r\). Now apply the same fact to the unital left Hilbert algebra \(\mathcal A_r^{\mathrm{op}}\), the right algebra with the opposite product. Its left von Neumann algebra is \(R(\mathcal A_r)''=M'\) (Fact 2.6). Its right-bounded vectors and right operators are \(\mathcal B_l\) and \(\lambda\), because the definition of left-bounded vectors for \(\mathcal A\) is the definition of right-bounded vectors for \(\mathcal A_r^{\mathrm{op}}\). So \(\mathcal B_l=M''e=Me\) with \(\lambda_{xe}=x\). As \(D(S)=\ell^2(\Gamma)\), the full completion is \(\mathcal A_l=Me\). The vector \(e\) is cyclic for \(M\) (\(Me\supseteq\mathbb C[\Gamma]\)) and separating (\(xe=0\) gives \(x=\lambda_{xe}=0\)). So the full completion of \(\mathbb C[\Gamma]\) is the vector algebra \(Me\) of Fact 2.12(c), for \(M\) and the cyclic and separating vector \(e\).

**Example 4.4** (compact groups). Let \(G\) be compact with Haar measure of total mass \(m\). Then \(\delta\equiv1\), \(S=F\) is the antiunitary \(\xi\mapsto\xi^*\), and \(D(S)=D(F)=H\). By Cauchy–Schwarz \(\|\xi\|_1\leq m^{1/2}\|\xi\|_2\), and the convolution inequalities give, for \(\xi,\eta\in L^2(G)\),
\[
\|\xi*\eta\|_2\leq\|\xi\|_1\|\eta\|_2\leq m^{1/2}\|\xi\|_2\|\eta\|_2,\qquad
\|\xi*\eta\|_2\leq\|\xi\|_2\|\eta\|_1\leq m^{1/2}\|\xi\|_2\|\eta\|_2 ,
\]
the second by unimodularity. So every \(\eta\in H\) is right bounded, with \(R_\eta\) the continuous extension of \(\xi\mapsto\xi*\eta\); thus \(\mathcal A_r=H\). In the definition of left-bounded vectors we now test against all \(\eta\in\mathcal A_r=H\). Since \(R_\eta\xi=\xi*\eta\), the first bound shows \(\mathcal B_l=H\). Hence \(\mathcal A_l=L^2(G)\): the full completion of \(C(G)\) is complete, with \(\|\xi*\eta\|\leq m^{1/2}\|\xi\|\|\eta\|\). By Theorem 9.2, \(M\) is a direct sum of type I factors. \(C(G)\) itself has no unit when \(G\) is infinite: a unit for \(C(G)\) would, by density and the \(L^1\) bound, be a unit for \(L^1(G)\), which does not exist for non-discrete \(G\). For \(G=\mathbb T\) with \(m=1\), the characters \(e_n(z)=z^n\) satisfy \(e_n*e_k=\delta_{nk}e_n\) and \(e_n^*=e_n\). They are projections of norm \(1=m^{-1/2}\), the least value that part (c) of Theorem 9.2 allows with the constant \(K=m^{1/2}\).

**Example 4.5** (the \(ax+b\) group). Let \(G=\{(a,b):a>0,\ b\in\mathbb R\}\) with \((a,b)(a',b')=(aa',b+ab')\) and \((a,b)^{-1}=(a^{-1},-a^{-1}b)\). The measure \(a^{-2}\,da\,db\) is left invariant: left translation by \((x,y)\) has Jacobian \(x^2\). Right translation by \((x,y)\) sends \((a,b)\) to \((ax,b+ay)\), with Jacobian \(x\). By (4.1) this gives \(\delta(x,y)=x^{-1}\). Hence, by (4.2),
\[
\xi^\flat(a,b)=\overline{\xi(a^{-1},-a^{-1}b)},\qquad \xi^\sharp(a,b)=a\,\overline{\xi(a^{-1},-a^{-1}b)},
\]
and by (4.4), \(\|\xi^\sharp\|^2=\int|\xi|^2a^{-3}\,da\,db\) and \(\|\xi^\flat\|^2=\int|\xi|^2a^{-1}\,da\,db\). For \(\xi\) supported where \(a\leq\varepsilon\) the ratio \(\|\xi^\sharp\|/\|\xi\|\) is at least \(\varepsilon^{-1/2}\), so \(S\) is unbounded; supports where \(a\geq R\) do the same for \(F\). The modular operator is multiplication by \(a^{-1}\), and \(\Delta^{it}\) is multiplication by \(a^{-it}\). The bound (4.3) reads \(\|R_\eta\|\leq\int|\eta(a,b)|a^{-3/2}\,da\,db\).

**Example 4.6** (no countability). For \(G=\mathbb R\times\mathbb R_d\), the reals times the discrete reals (the first worked example of the lesson on Haar measure), Haar measure is not \(\sigma\)-finite and \(L^2(G)\) is not separable. The group is abelian, so \(\delta\equiv1\). Theorem 4.1 applies word for word. Its measure-theoretic tools are the formulas (4.1), iterated integrals of compactly supported continuous functions, positivity of Haar measure on nonempty open sets, and density of \(C_c\) in \(L^2\) of a Radon measure. None of them needs countability, and the facts about the left structure recalled at the start of this section hold for every locally compact group.

## 5. The algebra of a weight on \(B(\mathcal K)\)

This section builds, from a positive operator \(h\), a left Hilbert algebra of finite-rank operators whose left von Neumann algebra is \(B(\mathcal K)\) and whose weight is \(\operatorname{Tr}(h^2\,\cdot\,)\). Section 6 uses it for a counterexample. We state the main facts as an exercise and then solve it.

**Exercise 5.1.** Let \(\mathcal K\) be a Hilbert space and \(h\) a positive self-adjoint operator on \(\mathcal K\) with zero kernel. On the algebraic tensor product \(\mathcal A=D(h)\odot\overline{D(h^{-1})}\), inside \(\mathcal K\otimes\overline{\mathcal K}\), put
\[
(\xi_1\otimes\bar\eta_1)(\xi_2\otimes\bar\eta_2)=\langle\xi_2,h^{-1}\eta_1\rangle\,\xi_1\otimes\bar\eta_2,\qquad
(\xi\otimes\bar\eta)^\sharp=h^{-1}\eta\otimes\overline{h\xi} .
\tag{5.1}
\]
Prove that these operations make \(\mathcal A\) a left Hilbert algebra in \(\mathcal K\otimes\overline{\mathcal K}\), with \(M=B(\mathcal K)\otimes\mathbb C1\), \(J(\xi\otimes\bar\eta)=\eta\otimes\bar\xi\) and \(\Delta^{1/2}(\xi\otimes\bar\eta)=h\xi\otimes\overline{h^{-1}\eta}\).

**The Hilbert–Schmidt realization.** Here \(\overline{\mathcal K}\) is the conjugate Hilbert space (Fact 2.2). We realize \(\mathcal K\otimes\overline{\mathcal K}\) as the Hilbert–Schmidt operators \(HS(\mathcal K)\), with \(\xi\otimes\bar\eta\) the rank-one operator \(\theta_{\xi,\eta}\zeta=\langle\zeta,\eta\rangle\xi\). This is the usual model of the Hilbert tensor product, and it matches the inner product of the Hilbert tensor product: \(\langle\theta_{a,b},\theta_{c,d}\rangle=\langle a,c\rangle\langle d,b\rangle=\langle a\otimes\bar b,c\otimes\bar d\rangle\). We use four facts.

- (a) For \(u,v\in B(\mathcal K)\), \(\ell(u)X=uX\) and \(r(v)X=Xv\) are bounded on \(HS(\mathcal K)\), with \(\ell(u)^*=\ell(u^*)\) and \(r(v)^*=r(v^*)\). In tensor form \(\ell(u)=u\otimes1\) and \(r(v)=1\otimes\overline{v^*}\), where \(\overline w\,\bar\zeta=\overline{w\zeta}\) (see tensor products of operators).
- (b) \(X\mapsto X^*\) is an antiunitary involution of \(HS(\mathcal K)\). In tensor form it is \(\xi\otimes\bar\eta\mapsto\eta\otimes\bar\xi\).
- (c) \(\langle X,\theta_{u,v}\rangle=\langle Xv,u\rangle\) for \(X\in HS(\mathcal K)\).
- (d) If \(D_1,D_2\subseteq\mathcal K\) are dense subspaces, the operators \(\theta_{a,b}\), \(a\in D_1\), \(b\in D_2\), span a dense subspace (elementary tensors of total sets are total).

Here \(D(h)\) and \(D(h^{-1})=\operatorname{ran}h\) are dense, \(h^{-1}\) is positive self-adjoint, and \(h^{-1}\) maps \(\operatorname{ran}h\) onto \(D(h)\), by the spectral theorem (Fact 2.13). So \(\mathcal A\) is the span of the \(\theta_{a,b}\) with \(a\in D(h)\), \(b\in D(h^{-1})\). For \(X\in\mathcal A\), the operator \(Xh^{-1}\) on \(D(h^{-1})\) is bounded, since \(\theta_{a,b}h^{-1}\zeta=\langle\zeta,h^{-1}b\rangle a\). Let \(\Phi(X)\) be its bounded extension; so \(\Phi(\theta_{a,b})=\theta_{a,h^{-1}b}\), and \(\Phi(X)\) depends only on \(X\). Similarly \(h^{-1}X^*h\) is bounded on \(D(h)\), with extension \(\sum_i\theta_{h^{-1}b_i,ha_i}\) when \(X=\sum_i\theta_{a_i,b_i}\). So (5.1) defines, in this realization,
\[
X\cdot Y=\Phi(X)Y,\qquad X^\sharp=\overline{h^{-1}X^*h}\qquad(X,Y\in\mathcal A).
\tag{5.2}
\]
Indeed \(\theta_{a_1,b_1}\cdot\theta_{a_2,b_2}=\theta_{a_1,h^{-1}b_1}\theta_{a_2,b_2}=\langle a_2,h^{-1}b_1\rangle\theta_{a_1,b_2}\) and \(\theta_{a,b}^\sharp=\theta_{h^{-1}b,ha}\). One checks on rank-one operators that
\[
\Phi(X^\sharp)=\Phi(X)^*,\qquad \Phi(X\cdot Y)=\Phi(X)\Phi(Y),\qquad X\zeta=\Phi(X)h\zeta\ \ (\zeta\in D(h)).
\tag{5.3}
\]
For example \(\Phi(\theta_{h^{-1}b,ha})=\theta_{h^{-1}b,a}=\theta_{a,h^{-1}b}^*\). The last identity shows that \(\Phi\) is injective.

**Theorem 5.2** (solution of Exercise 5.1).

1. The operations (5.2) satisfy the four axioms of a left Hilbert algebra; \(L_X=\ell(\Phi(X))\), and \(\mathcal A^2=\mathcal A\).
2. \(M=\ell(B(\mathcal K))\), that is, \(B(\mathcal K)\otimes\mathbb C1\).
3. Let \(A_0X=\overline{hXh^{-1}}\) on \(\mathcal A\), so \(A_0\theta_{a,b}=\theta_{ha,h^{-1}b}\). Its closure \(A\) is positive and self-adjoint, \(S=JA\) with \(J(X)=X^*\), and therefore \(\Delta^{1/2}=A\) and the modular conjugation is \(X\mapsto X^*\). In tensor form, \(\Delta^{1/2}(\xi\otimes\bar\eta)=h\xi\otimes\overline{h^{-1}\eta}\) and \(J(\xi\otimes\bar\eta)=\eta\otimes\bar\xi\).

**Proof.** (1) By (5.2) and (5.3), \((X\cdot Y)\cdot Z=\Phi(X)\Phi(Y)Z=X\cdot(Y\cdot Z)\). Also \((X^\sharp)^\sharp=X\), and \(\Phi((X\cdot Y)^\sharp)=\Phi(Y)^*\Phi(X)^*=\Phi(Y^\sharp\cdot X^\sharp)\), so \((X\cdot Y)^\sharp=Y^\sharp\cdot X^\sharp\) by injectivity. The left multiplication \(Y\mapsto\Phi(X)Y\) is \(\ell(\Phi(X))\), bounded by fact (a). The adjoint axiom is \(\langle\Phi(X)Y,Z\rangle=\langle Y,\Phi(X)^*Z\rangle=\langle Y,X^\sharp\cdot Z\rangle\). For closability, let \(X_n\to0\) and \(X_n^\sharp\to Y\) in \(HS(\mathcal K)\). For \(u\in D(h^{-1})\) and \(v\in D(h)\), fact (c) gives
\[
\langle X_n^\sharp,\theta_{u,v}\rangle=\langle h^{-1}X_n^*hv,u\rangle=\langle hv,X_nh^{-1}u\rangle\longrightarrow0 ,
\]
since Hilbert–Schmidt convergence implies norm convergence. So \(\langle Y,\theta_{u,v}\rangle=0\), and \(Y=0\) by fact (d). Finally, if \(\mathcal K\neq0\), pick \(0\neq c\in D(h^{-1})\) and put \(d=h^{-1}c/\|h^{-1}c\|^2\in D(h)\). Then \(\theta_{a,c}\cdot\theta_{d,b}=\langle d,h^{-1}c\rangle\theta_{a,b}=\theta_{a,b}\), so \(\mathcal A^2=\mathcal A\), which is dense by fact (d).

(2) As \(b\) runs through \(D(h^{-1})\), \(h^{-1}b\) runs through \(D(h)\). So \(\{\Phi(X)\}\) is the span \(\mathcal F\) of the \(\theta_{a,c}\), \(a,c\in D(h)\), and \(M=\ell(\mathcal F)''\). Every \(\ell(u)\) commutes with every \(r(v)\). Conversely, let \(T\) commute with all \(r(v)\). If \(\mathcal K\neq0\), fix a unit vector \(e\) and define \(xu=(T\theta_{u,e})e\); then \(\|xu\|\leq\|T\|\|u\|\). Since \(\theta_{u,w}=\theta_{u,e}\theta_{e,w}=r(\theta_{e,w})\theta_{u,e}\),
\[
T\theta_{u,w}=r(\theta_{e,w})T\theta_{u,e}=(T\theta_{u,e})\theta_{e,w}=\theta_{xu,w}=\ell(x)\theta_{u,w},
\]
so \(T=\ell(x)\) by fact (d). This is the description of the commutant of \(1\otimes B(\mathcal K)\) in the present realization. Hence \(\ell(B(\mathcal K))\) is the commutant of \(r(B(\mathcal K))\), so it is a von Neumann algebra containing \(\ell(\mathcal F)\), and \(M\subseteq\ell(B(\mathcal K))\). For the reverse inclusion, let \(x\in B(\mathcal K)\). For each finite-dimensional subspace \(V\subseteq D(h)\), let \(P_V\) be its projection. The operators \(P_VxP_V\) lie in \(\mathcal F\), have norm at most \(\|x\|\), and \(\ell(P_VxP_V)\theta_{u,w}=\theta_{P_VxP_Vu,w}\to\theta_{xu,w}\) as \(V\) increases, because \(P_V\to1\) strongly (\(D(h)\) is dense). A bounded net that converges on a total set converges strongly, so \(\ell(x)\in M\).

(3) Let \(E\) be the spectral measure of \(h\), \(E_n=E([1/n,n])\), and \(P_nX=E_nXE_n\). Since \(E(\{0\})=0\), \(E_n\to1\) strongly. The \(P_n\) are orthogonal projections of \(HS(\mathcal K)\), and \(P_n\theta_{a,b}=\theta_{E_na,E_nb}\to\theta_{a,b}\); by fact (d), \(P_n\to1\) strongly. On \(\mathcal K_n=P_n\,HS(\mathcal K)\) the operators \(hE_n\), \(h^{-1}E_n\) are bounded, and \(A_nX=(hE_n)X(h^{-1}E_n)\) is bounded, invertible, and positive: \(A_n=B_n^2\) with \(B_nX=(h^{1/2}E_n)X(h^{-1/2}E_n)\) self-adjoint by fact (a). These operators agree on the increasing subspaces \(\mathcal K_n\), so they define a symmetric operator \(T_0\) on \(D_0=\bigcup_n\mathcal K_n\), with \(T_0\geq0\).

*Self-adjointness.* Let \(A=\overline{T_0}\). It is closed, symmetric and positive, and \(\operatorname{ran}(A\pm i)\supseteq\mathcal K_n\) for each \(n\), because \(A_n\pm i\) is invertible on \(\mathcal K_n\). So \(\operatorname{ran}(A\pm i)\) is dense. For a closed symmetric operator, \(\|(A\pm i)x\|^2=\|Ax\|^2+\|x\|^2\), so these ranges are closed, hence equal to the whole space. Let \(y\in D(A^*)\), and choose \(x\in D(A)\) with \((A-i)x=(A^*-i)y\). Then \((A^*-i)(y-x)=0\). But \(\langle(A^*-i)z,w\rangle=\langle z,(A+i)w\rangle\) for \(w\in D(A)\), so \(\ker(A^*-i)=\operatorname{ran}(A+i)^\perp=\{0\}\). Hence \(y=x\in D(A)\), and \(A\) is self-adjoint.

*The core.* For \(X=\theta_{a,b}\in\mathcal A\), put \(X_n=P_nX=\theta_{E_na,E_nb}\in\mathcal K_n\). Then \(X_n\to X\), and \(T_0X_n=\theta_{hE_na,h^{-1}E_nb}=\theta_{E_nha,E_nh^{-1}b}\to\theta_{ha,h^{-1}b}\). So \(X\in D(A)\) and \(AX=A_0X\): \(A\) extends \(A_0\). The rank-one operators \(\theta_{u,v}\) with \(u,v\in E_n\mathcal K\) lie in \(\mathcal A\), since \(E_n\mathcal K\subseteq D(h)\cap D(h^{-1})\). They span a dense subspace of \(\mathcal K_n\), on which \(A\) is bounded, and \(D_0\) is a core for \(A\). Hence \(\mathcal A\) is a core for \(A\), that is, \(\overline{A_0}=A\).

*The polar decomposition.* On \(\mathcal A\), \(JA_0\theta_{a,b}=\theta_{ha,h^{-1}b}^*=\theta_{h^{-1}b,ha}=\theta_{a,b}^\sharp\). As \(J\) is an isometric bijection, the closure of \(JA_0\) is \(J\overline{A_0}=JA\). So \(S=JA\) with \(D(S)=D(A)\). By the uniqueness of the polar decomposition (Fact 2.4), \(\Delta^{1/2}=A\) and the modular conjugation is \(J\). \(\square\)

The same realization identifies the bounded vectors and the weight.

**Proposition 5.3.** Keep the setting of Theorem 5.2.

1. \(\eta\in\mathcal B_r\) if and only if \(\operatorname{ran}\eta\subseteq D(h^{-1})\) and \(y=h^{-1}\eta\) is bounded; then \(R_\eta=r(y)\). In particular \(\theta_{hu,v}\in\mathcal A_r\) for \(u,v\in D(h)\), with \(F\theta_{hu,v}=\theta_{hv,u}\).
2. \(\xi\in\mathcal B_l\) if and only if there is \(x\in B(\mathcal K)\) with \(\xi\zeta=xh\zeta\) for all \(\zeta\in D(h)\); then \(\lambda_\xi=\ell(x)\). Such \(\xi\) lies in \(\mathcal A_l\) exactly when \(xh\) and \(x^*h\) both extend to Hilbert–Schmidt operators; then \(S\xi\) is the extension of \(x^*h\).
3. Identify \(M\) with \(B(\mathcal K)\). For \(b\in B(\mathcal K)_+\), \(\psi(b)=\|\overline{b^{1/2}h}\|_{HS}^2\) if \(b^{1/2}h\) extends to a Hilbert–Schmidt operator, and \(\psi(b)=+\infty\) otherwise. In particular \(\psi(\theta_{u,u})=\|hu\|^2\) for a unit vector \(u\in D(h)\), and \(\psi(1)=\|h\|_{HS}^2\). So \(\psi\) is the weight "\(\operatorname{Tr}(h^2\,\cdot\,)\)", and \(\mathcal A\) is a dense subalgebra of its left Hilbert algebra.


**Proof.** (1) If \(\eta=hy\) with \(y\) bounded and \(\operatorname{ran}y\subseteq D(h)\), then for \(X=\theta_{a,b}\), \(\Phi(X)hy\zeta=\langle hy\zeta,h^{-1}b\rangle a=\langle y\zeta,b\rangle a=Xy\zeta\). So \(L_X\eta=Xy\), with \(\|Xy\|\leq\|y\|\|X\|\): \(\eta\in\mathcal B_r\) and \(R_\eta=r(y)\). Conversely, let \(\|\Phi(X)\eta\|\leq c\|X\|\) for all \(X\in\mathcal A\). With \(X=\theta_{a,b}\), \(\|a\|=1\), this says \(\|\eta^*h^{-1}b\|\leq c\|b\|\) for \(b\in D(h^{-1})\). For \(\zeta\in\mathcal K\), the functional \(b\mapsto\langle h^{-1}b,\eta\zeta\rangle=\langle\eta^*h^{-1}b,\zeta\rangle\) is then bounded on \(D(h^{-1})\), so \(\eta\zeta\in D(h^{-1})\) (self-adjointness of \(h^{-1}\)), and \(y=h^{-1}\eta\) satisfies \(\|y\zeta\|\leq c\|\zeta\|\). For the last claim, \(\theta_{hu,v}=h\theta_{u,v}\), with \(\theta_{u,v}\) bounded and of range in \(D(h)\). Also \(A\theta_{u,hv}=\theta_{hu,v}\), since \(hv\in D(h^{-1})\); so \(\theta_{hu,v}\in D(A^{-1})=D(\Delta^{-1/2})=D(F)\), and \(F\theta_{hu,v}=JA^{-1}\theta_{hu,v}=\theta_{u,hv}^*=\theta_{hv,u}\) (Fact 2.4).

(2) By (1), every \(\eta\in\mathcal A_r\) has the form \(hy\), and \(R_\eta\xi=\xi y\). If \(\xi\zeta=xh\zeta\) on \(D(h)\), then \(R_\eta\xi=\xi y=xhy=x\eta\), so \(\|R_\eta\xi\|\leq\|x\|\|\eta\|\): \(\xi\in\mathcal B_l\) with \(\lambda_\xi=\ell(x)\). Conversely, let \(\xi\in\mathcal B_l\). Then \(\lambda_\xi\in M\), so \(\lambda_\xi=\ell(x)\) for some \(x\) by Theorem 5.2. Test with \(\eta=\theta_{hu,v}\), \(u,v\in D(h)\), \(v\neq0\): \(\xi\theta_{u,v}=R_\eta\xi=\lambda_\xi\eta=x\theta_{hu,v}\), that is \(\theta_{\xi u,v}=\theta_{xhu,v}\), so \(\xi u=xhu\). For the second sentence: if \(xh\) and \(x^*h\) extend to Hilbert–Schmidt operators \(\xi\) and \(\xi'\), both lie in \(\mathcal B_l\), with \(\lambda_{\xi'}=\ell(x^*)=\lambda_\xi^*\). Then \(\lambda_\xi\in\mathfrak n_l\cap\mathfrak n_l^*\), so \(\xi\in\mathcal A_l\) and \(S\xi=\xi'\) (Fact 2.8). The converse follows from \(\lambda_{S\xi}=\lambda_\xi^*\).

(3) By the definition of \(\psi\) and part 2, \(\psi(b)<\infty\) exactly when \(\ell(b^{1/2})=\lambda_\xi\) for some \(\xi\), that is, when \(b^{1/2}h\) extends to a Hilbert–Schmidt \(\xi\); then \(\psi(b)=\|\xi\|^2\). For \(b=\theta_{u,u}\) with \(\|u\|=1\), \(b^{1/2}=b\) and \(bh\zeta=\langle\zeta,hu\rangle u\), which extends to \(\theta_{u,hu}\), of norm \(\|hu\|\). \(\square\)

**Remark 5.4.** Take \(h=\rho^{1/2}\) with \(\rho=\operatorname{diag}(2^{-n})\) on \(\ell^2(\mathbb N)\). Then \(h\) is Hilbert–Schmidt, so \(xh\) and \(x^*h\) are Hilbert–Schmidt for every bounded \(x\), and part 2 of Proposition 5.3 gives \(\mathcal A_l=\{xh:x\in B(\mathcal K)\}\). This is the vector algebra \(M\Omega\) of the cyclic and separating vector \(\Omega=\rho^{1/2}\) (Fact 2.12(c)), and \(\psi(1)=\operatorname{Tr}(\rho)=1\): the weight is a state. In general \(h\) is arbitrary: \(\psi(1)=\|h\|_{HS}^2\) may be infinite, and \(h\) may be unbounded.

## 6. Closed multipliers for vectors of the involution domain

For a vector \(\xi\in H\), right multiplication \(\theta\mapsto R_\theta\xi\) by the vectors of the right algebra is always defined, but it need not be bounded. Theorem 6.2 shows that it is closable, with a closure affiliated with \(M\), whenever \(\xi\in D(S)\). Proposition 6.4 shows that this hypothesis cannot be dropped. Example 6.7 shows that the closures for \(\xi\) and \(S\xi\) need not be adjoint to each other, and Proposition 6.8 gives two cases in which they are. We start with a test for membership in \(D(S)\) that uses only products in the right algebra.

**Proposition 6.1** (a pairing test for the domain of \(S\)). Let \(v,w\in H\). Then \(v\in D(S)\) and \(Sv=w\) if and only if
\[
\langle\theta'(F\theta),v\rangle=\langle w,\theta(F\theta')\rangle\qquad(\theta,\theta'\in\mathcal A_r),
\tag{6.1}
\]
where the products are those of \(\mathcal A_r\).

**Proof.** Put \(u=\theta(F\theta')\), a vector of \(\mathcal A_r\). By the product rule of Fact 2.5 and \(F^2=I\), \(Fu=(F\theta')^\flat\theta^\flat=\theta'(F\theta)\). So (6.1) says \(\langle Fu,v\rangle=\langle w,u\rangle\) for these \(u\).

If \(v\in D(S)\) and \(Sv=w\), then the adjoint relation (Fact 2.3) gives \(\langle Fu,v\rangle=\langle Sv,u\rangle=\langle w,u\rangle\).

Conversely, assume (6.1). As \(\theta'\) runs through \(\mathcal A_r\), so does \(F\theta'\), since \(F\) maps \(\mathcal A_r\) onto itself (Fact 2.5). So the vectors \(u\) span \(\mathcal A_r^2\), and by linearity \(\langle Fu,v\rangle=\langle w,u\rangle\) for all \(u\in\mathcal A_r^2\). Both sides are continuous in \(u\) for the graph norm of \(F\), and \(\mathcal A_r^2\) is a graph core for \(F\) (Fact 2.6). Hence the identity holds for every \(u\in D(F)\). By the definition of the adjoint of a conjugate-linear operator (Fact 2.2), this says \(v\in D(F^*)\) and \(F^*v=w\). Finally \(F^*=S^{**}=S\), because \(S\) is closed (Fact 2.2). \(\square\)

Proposition 6.1 is the mirror image of the pairing test for \(F\) in Fact 2.6: the roles of \(\mathcal A\) and \(\mathcal A_r\) are exchanged, and the product core \(\mathcal A_r^2\) of \(F\) replaces the product core \(\mathcal A^2\) of \(S\).

**Theorem 6.2.** Let \(\mathcal A\) be any left Hilbert algebra and \(\xi\in D(S)\). Define two linear operators with domain \(\mathcal A_r\):
\[
a_0\theta=R_\theta\xi,\qquad b_0\theta=R_\theta S\xi\qquad(\theta\in\mathcal A_r).
\tag{6.2}
\]
1. \(\langle a_0\theta,\theta'\rangle=\langle\theta,b_0\theta'\rangle\) for \(\theta,\theta'\in\mathcal A_r\). Hence \(a_0\subseteq b_0^*\), \(b_0\subseteq a_0^*\), and both operators are closable.
2. Write \(\bar\lambda_\xi\) and \(\bar\lambda_{S\xi}\) for the closures of \(a_0\) and \(b_0\). Then \(\bar\lambda_\xi\subseteq\bar\lambda_{S\xi}^*\) and \(\bar\lambda_{S\xi}\subseteq\bar\lambda_\xi^*\), and both closures are affiliated with \(M\).
3. \(\bar\lambda_\xi\) is bounded if and only if \(\xi\in\mathcal B_l\), and then \(\bar\lambda_\xi=\lambda_\xi\). If \(\xi\in\mathcal A_l\), then \(\bar\lambda_\xi=\lambda_\xi\) and \(\bar\lambda_{S\xi}=\lambda_\xi^*\), so both inclusions in 2 are equalities. For \(a\in\mathcal A\), \(\bar\lambda_a=L_a\).

*Remark.* Part 2 asserts only inclusions. They can be strict, even for the full left Hilbert algebra of a faithful normal state on \(B(\ell^2(\mathbb N))\) and a vector with \(S\xi=\xi\) (Example 6.7). They are equalities when \(\mathcal A\) is commutative, and in the model of Section 5 when \(h^{-1}\) is bounded (Proposition 6.8).

By Fact 2.9, \(\mathcal A\) and \(\mathcal A_l\) have the same \(\mathcal A_r\), \(S\) and \(M\), so the theorem says the same for \(\mathcal A\) and for its full completion.

**Proof.** (1) Let \(\theta,\theta'\in\mathcal A_r\). By Fact 2.5, \(R_\theta^*=R_{F\theta}\), so
\[
\langle R_\theta\xi,\theta'\rangle=\langle\xi,R_{F\theta}\theta'\rangle=\langle\xi,\theta'(F\theta)\rangle .
\]
The product rule of Fact 2.5 and \(F^2=I\) give \(\theta'(F\theta)=F\big(\theta(F\theta')\big)\). Put \(w=\theta(F\theta')=R_{F\theta'}\theta\in\mathcal A_r\). By the adjoint relation (Fact 2.3), \(\langle\xi,Fw\rangle=\overline{\langle Fw,\xi\rangle}=\overline{\langle S\xi,w\rangle}=\langle w,S\xi\rangle\). Therefore
\[
\langle R_\theta\xi,\theta'\rangle=\langle R_{F\theta'}\theta,S\xi\rangle=\langle\theta,R_{F\theta'}^*S\xi\rangle=\langle\theta,R_{\theta'}S\xi\rangle,
\]
using \(R_{F\theta'}^*=R_{F^2\theta'}=R_{\theta'}\). This is the first claim, and it gives \(b_0\subseteq a_0^*\). Apply it to \(S\xi\in D(S)\), with \(S(S\xi)=\xi\): \(\langle b_0\theta,\theta'\rangle=\langle\theta,a_0\theta'\rangle\), so \(a_0\subseteq b_0^*\). Both adjoints contain \(\mathcal A_r\) in their domains, and \(\mathcal A_r\) is dense (Fact 2.6). By the graph lemma for linear operators (Fact 2.2), both operators are closable.

(2) The adjoint of a closable operator equals the adjoint of its closure (Fact 2.2). So the inclusions pass to the closures. For affiliation, let \(\zeta\in\mathcal A_r\). Then \(R_\zeta\theta=\theta\zeta\in\mathcal A_r\) for \(\theta\in\mathcal A_r\), and
\[
a_0(R_\zeta\theta)=R_{\theta\zeta}\xi=R_\zeta R_\theta\xi=R_\zeta\,a_0\theta
\]
by Fact 2.5. Also \(R_\zeta^*=R_{F\zeta}\) with \(F\zeta\in\mathcal A_r\). So the graph of \(a_0\) is invariant under \(\operatorname{diag}(c,c)\) for every \(c\) in the \(*\)-algebra \(\mathcal C=R(\mathcal A_r)\), and so is its closure. By Fact 2.6, \(\mathcal C''=M'\). The graph criterion of Fact 2.7(a), with \(N=M\), shows that \(\bar\lambda_\xi\) is affiliated with \(M\). The same argument applies to \(b_0\).

(3) \(\bar\lambda_\xi\) is bounded exactly when \(a_0\) is bounded on \(\mathcal A_r\), which is the definition of \(\xi\in\mathcal B_l\). In that case \(a_0\) is the restriction of \(\lambda_\xi\) to \(\mathcal A_r\), by the definition of \(\lambda_\xi\), and a bounded operator is the closure of its restriction to a dense subspace. If \(\xi\in\mathcal A_l\), then \(S\xi\in\mathcal A_l\subseteq\mathcal B_l\) and \(\lambda_{S\xi}=\lambda_\xi^*\) (Fact 2.8). The last claim is \(\lambda_a=L_a\) (Fact 2.8). \(\square\)

The same argument, with the roles of \(\mathcal A\) and \(\mathcal A_r\) exchanged, gives the closed right multipliers of Fact 2.7(b). For the full algebra, the conclusions of Theorem 6.2 can also be derived from the density theory applied to the opposite of the right algebra, as in the lesson *The modular group and its analytic algebra*. The proof above is direct and does not pass through the full completion.

**Remark 6.3.** Only the inclusions in part 2 are claimed; Example 6.7 shows that equality can fail. Proposition 6.4 shows that the hypothesis \(\xi\in D(S)\) cannot be dropped.

### When the domain hypothesis fails

**Proposition 6.4.** In the model of Section 5, suppose \(\operatorname{ran}h\neq\mathcal K\), which happens exactly when \(h^{-1}\) is unbounded. Choose a unit vector \(e\), a unit vector \(e'\in D(h)\), and \(w\in\mathcal K\setminus\operatorname{ran}h\). Then \(\xi=\theta_{e,w}\) does not lie in \(D(S)\), and the operator \(a_0\theta=R_\theta\xi\) on \(\mathcal A_r\) of (6.2) is not closable. So the hypothesis \(\xi\in D(S)\) of Theorem 6.2 cannot be dropped.

**Proof.** *The functional.* The map \(u\mapsto\langle u,w\rangle\) on \(D(h)\) is not bounded for \(\|hu\|\). Otherwise \(hu\mapsto\langle u,w\rangle\) would be a bounded functional on the dense subspace \(\operatorname{ran}h\), so \(\langle u,w\rangle=\langle hu,v\rangle\) for some \(v\) and all \(u\in D(h)\). Then \(v\in D(h^*)=D(h)\) and \(hv=w\), against \(w\notin\operatorname{ran}h\). Hence there are \(u_n\in D(h)\) with \(\langle u_n,w\rangle=1\) and \(\|hu_n\|\to0\).

*Not closable.* Put \(\eta_n=\theta_{hu_n,e'}\). By Proposition 5.3(1), \(\eta_n\in\mathcal A_r\) with \(R_{\eta_n}=r(\theta_{u_n,e'})\). So
\[
\|\eta_n\|=\|hu_n\|\to0,\qquad a_0\eta_n=\xi\,\theta_{u_n,e'}=\langle u_n,w\rangle\,\theta_{e,e'}=\theta_{e,e'}\neq0 .
\]
A closable operator cannot send a null sequence to a sequence with a nonzero limit.

*Not in \(D(S)\).* Suppose \(\xi\in D(S)=D(A)\). For \(c\in D(h)\) and \(d\in D(h^{-1})\), self-adjointness of \(A\) and fact (c) of Section 5 give
\[
\langle A\xi,\theta_{c,d}\rangle=\langle\xi,\theta_{hc,h^{-1}d}\rangle=\langle\xi h^{-1}d,hc\rangle=\langle h^{-1}d,w\rangle\,\langle e,hc\rangle .
\]
Choose \(c\) with \(\langle e,hc\rangle\neq0\) (\(\operatorname{ran}h\) is dense). Then \(|\langle h^{-1}d,w\rangle|\leq C\|d\|\) for all \(d\in D(h^{-1})\), so \(w\in D(h^{-1})=\operatorname{ran}h\), a contradiction. \(\square\)

**Example 6.5.** A concrete case of Proposition 6.4: \(\mathcal K=\ell^2(\mathbb N)\), \(he_n=n^{-1}e_n\), and \(w=\sum_nn^{-1}e_n\), which is not in \(\operatorname{ran}h\) because \(\sum_n e_n\) is not square summable.

**Example 6.6** (closability without \(D(S)\)). The hypothesis \(\xi\in D(S)\) is sufficient for closability but not necessary. Take the block algebra of Fact 2.12(e) with \(I=\mathbb N\) and \(t_n=n^{-2}\). Every \(R_\theta\) acts blockwise, \((R_\theta\xi)_n=\xi_n\theta_n\), for every \(\xi\in H\) (by continuity from finite blocks). If \(\theta^{(k)}\to0\) and \(R_{\theta^{(k)}}\xi\to\zeta\), then each block of \(\zeta\) is \(\lim_k\xi_n\theta^{(k)}_n=0\), because the blocks are finite-dimensional. So \(a_0\) is closable for every \(\xi\). Yet \(\xi=(n^{-1/2}E_{12})_n\) lies in \(H\setminus D(S)\): its squared norm is \(\sum_nn^{-1}t_n<\infty\), while the adjoint family has squared norm \(\sum_nn^{-1}=\infty\), so \(\xi\notin D(S)\) by the description of \(D(S)\) in Fact 2.12(e). What Theorem 6.2 really needs \(\xi\in D(S)\) for is the operator \(b_0\) and the adjoint relation of part 1.

### The two closures need not be adjoint to each other

**Example 6.7** (strict inclusions for a faithful normal state). Let \(\mathcal K=\ell^2(\mathbb N)\) with orthonormal
basis \((e_n)_{n\geq1}\), let \(B\) be the diagonal operator \(Be_n=n^{-1}e_n\), let \(v=\sum_nn^{-1}e_n\), and let \(P\)
be the projection onto \(v^\perp\). In the model of Section 5 take
\[
h=BPB,\qquad \xi=PB .
\]
Then \(\mathcal A_l=\{xh:x\in B(\mathcal K)\}\), the weight \(\psi(b)=\operatorname{Tr}(hbh)\) is finite (a state after
\(h\) and \(\xi\) are multiplied by \(\|h\|_{HS}^{-1}\)), \(\xi\in D(S)\) with \(S\xi=\xi\), and
\[
\bar\lambda_{S\xi}\subsetneq\bar\lambda_\xi^*,\qquad \bar\lambda_\xi\subsetneq\bar\lambda_{S\xi}^* .
\]

**Proof.** *A closed symmetric operator.* Let \(N=B^{-1}\), the diagonal operator \(Ne_n=ne_n\) on
\(D(N)=\operatorname{ran}B=\{u:\sum_nn^2|u_n|^2<\infty\}\); it is positive and self-adjoint. For \(u\in D(N)\) the series
\(\sum_nu_n=\langle Nu,v\rangle\) converges absolutely, and we let \(T\) be the restriction of \(N\) to
\(D(T)=\{u\in D(N):\sum_nu_n=0\}\). Writing \(u=Bz\), we have \(\sum_nu_n=\langle z,v\rangle\), so \(D(T)=B(v^\perp)\) and
\(T(Bz)=z\) for \(z\perp v\); in particular \(\operatorname{ran}T=v^\perp\). The functional
\(u\mapsto\langle Nu,v\rangle\) is continuous for the graph norm of \(N\), so \(T\) is closed. It is symmetric, as a
restriction of \(N\), and densely defined: \(D(T)\) contains the vectors \(e_j-e_k\), and a vector orthogonal to all of
them has constant coordinates, hence is \(0\). The vector \(v\) is not in \(D(N)\supseteq D(T)\), since \(Nv\) would be
\((1,1,\dots)\).

*The density.* The operator \(h\) is Hilbert–Schmidt, as \(B\) is, and \(\langle hu,u\rangle=\|PBu\|^2\geq0\). If
\(hu=0\), then \(PBu=0\), so \(Bu=cv\) for a scalar \(c\), that is, \(u_n=c\) for all \(n\), and \(u=0\). So \(h\) is
positive with zero kernel and dense range. Since \(PBu\perp v\), we have \(hu=B(PBu)\in D(T)\) and \(T(hu)=PBu\): as
operators, \(\operatorname{ran}h\subseteq D(T)\) and \(Th=\xi\). Moreover \(\operatorname{ran}h\) is a core for \(T\).
Indeed, let \(u=Bz\in D(T)\) and let \(E_m\) be the projection onto the span of \(e_1,\dots,e_m\). The vectors
\(y_m=NE_mz\) satisfy \(hy_m=BPE_mz\to BPz=u\) and \(Thy_m=PE_mz\to z=Tu\).

*The algebra.* Since \(h\) is Hilbert–Schmidt, \(D(h)=\mathcal K\), and Proposition 5.3(2) gives, as in Remark 5.4,
\(\mathcal A_l=\{xh:x\in B(\mathcal K)\}\) with \(\lambda_{xh}=\ell(x)\) and \(S(xh)=x^*h\). Proposition 5.3(1) gives
\(\mathcal B_r=\{hy:y\in B(\mathcal K)\}\) with \(R_{hy}=r(y)\). Since \(R_{hy}^*=r(y^*)=R_{hy^*}\), the last statement of
Fact 2.6 gives \(hy\in D(F)\); so \(\mathcal A_r=\{hy:y\in B(\mathcal K)\}\). By Proposition 5.3(3),
\(\psi(b)=\|b^{1/2}h\|_{HS}^2=\operatorname{Tr}(hbh)\), and \(\psi(1)=\|h\|_{HS}^2<\infty\). Multiplying \(h\) and \(\xi\)
by \(\|h\|_{HS}^{-1}\) keeps \(Th=\xi\) and the core property, makes \(\psi\) a state, and changes nothing below.

*\(\xi\in D(S)\) and \(S\xi=\xi\).* The bounded self-adjoint operators \(N_m=NE_m\) give
\(\xi_m=N_mh=E_mNh=E_m\xi\in\mathcal A_l\) with \(S\xi_m=N_m^*h=\xi_m\). Since \(\xi\) is Hilbert–Schmidt,
\(\xi_m\to\xi\) in \(HS(\mathcal K)\), and closedness of \(S\) gives \(\xi\in D(S)\) and \(S\xi=\xi\).

*The closures.* Let \(\ell(T)\) be the operator \(X\mapsto TX\) with domain
\(\{X\in HS(\mathcal K):X\mathcal K\subseteq D(T),\ TX\in HS(\mathcal K)\}\). It is closed: if \(X_k\to X\) and
\(TX_k\to Y\) in \(HS(\mathcal K)\), then \(X_ku\to Xu\) and \(TX_ku\to Yu\) for every \(u\), so \(Xu\in D(T)\) and
\(TXu=Yu\). It is symmetric: \(\langle TX,Y\rangle=\sum_j\langle TXe_j,Ye_j\rangle=\sum_j\langle Xe_j,TYe_j\rangle=
\langle X,TY\rangle\). For \(hy\in\mathcal A_r\),
\[
a_0(hy)=R_{hy}\xi=\xi y=Thy,\qquad b_0(hy)=R_{hy}S\xi=Thy,
\]
so \(a_0=b_0\) is the restriction of \(\ell(T)\) to \(\mathcal A_r\). This restriction is a core for \(\ell(T)\). Let
\(X\) be in the domain of \(\ell(T)\). Then \(XE_m\to X\) and \(TXE_m\to TX\) in \(HS(\mathcal K)\), the errors being
tails of \(\sum_j\|Xe_j\|^2\) and \(\sum_j\|TXe_j\|^2\). For fixed \(m\), \(XE_m=\sum_{j\leq m}\theta_{Xe_j,e_j}\); choose
\(u_{j,k}\) with \(hu_{j,k}\to Xe_j\) and \(Thu_{j,k}\to TXe_j\), by the core property of \(\operatorname{ran}h\), and put
\(y_k=\sum_{j\leq m}\theta_{u_{j,k},e_j}\). Column by column, \(hy_k\to XE_m\) and \(Thy_k\to TXE_m\) in
\(HS(\mathcal K)\). Hence
\[
\bar\lambda_\xi=\bar\lambda_{S\xi}=\ell(T).
\]

*Strictness.* Let \(Z=\theta_{v,e_1}\). For \(X\) in the domain of \(\ell(T)\), fact (c) of Section 5 and
\(\operatorname{ran}T=v^\perp\) give \(\langle\ell(T)X,Z\rangle=\langle TXe_1,v\rangle=0\). So \(Z\) lies in the domain of
\(\ell(T)^*\), with \(\ell(T)^*Z=0\), but not in the domain of \(\ell(T)\), because \(Ze_1=v\notin D(T)\). As \(\ell(T)\)
is symmetric, \(\ell(T)\subsetneq\ell(T)^*\), which is the assertion. \(\square\)

**Proposition 6.8** (two cases of equality). Let \(\xi\in D(S)\).

1. If \(\mathcal A\) is commutative, then \(\bar\lambda_{S\xi}=\bar\lambda_\xi^*\) and \(\bar\lambda_\xi=\bar\lambda_{S\xi}^*\);
   here \(D(S)=H\). For the algebra of Proposition 3.1 and \(f\in L^2(\mu)\), \(\bar\lambda_f\) is multiplication by \(f\)
   on \(\{g\in L^2(\mu):fg\in L^2(\mu)\}\).
2. In the model of Section 5, if \(h^{-1}\) is bounded, then \(\mathcal B_l=H\), \(\mathcal A_l=D(S)\), and the same
   equalities hold.

**Proof.** (1) We first show: *if \(C\subseteq D\) are closed densely defined operators affiliated with an abelian von
Neumann algebra \(N\), then \(C=D\).* Let \(|D|=(D^*D)^{1/2}\), so that \(D(|D|)=D(D)\) and \(\||D|u\|=\|Du\|\)
(Normal products and closed operator graphs, polar decomposition for closed
operators),
and let \(p_m=1_{[0,m]}(|D|)\). A unitary \(u\in N'\) satisfies \(uDu^*=D\), hence \(uD^*Du^*=D^*D\), so it commutes with
the spectral projections of \(D^*D\); as every element of \(N'\) is a linear combination of unitaries,
\(p_m\in N''=N\). Since \(N\) is abelian, \(p_m\in N'\), and affiliation applied to the unitary \(2p_m-1\) shows that
\(p_m\) maps \(D(C)\) and \(D(D)\) into themselves and commutes with \(C\) and with \(D\) there. Also \(p_m\to1\)
strongly, \(p_mH\subseteq D(D)\) and \(\|Dp_m\|\leq m\). For \(u\in p_mH\), choose \(u_k\in D(C)\) with \(u_k\to u\);
then \(p_mu_k\to u\) and \(Cp_mu_k=Dp_mu_k\to Du\), so \(u\in D(C)\) by closedness. Hence, for \(u\in D(D)\),
\(p_mu\in D(C)\), \(p_mu\to u\) and \(Cp_mu=Dp_mu=p_mDu\to Du\), so \(u\in D(C)\). Thus \(C=D\).

Now let \(\mathcal A\) be commutative. Then \(L_aL_b=L_{ab}=L_{ba}=L_bL_a\) and \(L_a^*=L_{a^\sharp}\) (Fact 2.1), so \(M\)
is abelian, and \(D(S)=H\) by Proposition 3.2. By Theorem 6.2, \(\bar\lambda_{S\xi}\subseteq\bar\lambda_\xi^*\); both are
closed and densely defined; \(\bar\lambda_{S\xi}\) is affiliated with \(M\), and so is \(\bar\lambda_\xi^*\), since
\(u\bar\lambda_\xi u^*=\bar\lambda_\xi\) implies \(u\bar\lambda_\xi^*u^*=\bar\lambda_\xi^*\) for unitaries \(u\in M'\). The
statement just proved gives \(\bar\lambda_{S\xi}=\bar\lambda_\xi^*\), and taking adjoints gives
\(\bar\lambda_\xi=\bar\lambda_{S\xi}^*\). For the algebra of Proposition 3.1, \(\mathcal A_r=\mathcal A\) and
\(R_\theta=m_\theta\), so \(a_0\theta=f\theta\) for \(\theta\in L^2\cap L^\infty\). Multiplication by \(f\) on
\(\{g:fg\in L^2\}\) is closed, since on each set \(\{|f|\leq n\}\) it is bounded and \(f\) is finite almost everywhere,
and \(L^2\cap L^\infty\) is a core for it: for \(g\) in its domain, the truncations \(g1_{\{|g|\leq n\}}\) converge to
\(g\), with \(fg1_{\{|g|\leq n\}}\to fg\), by dominated convergence. So \(\bar\lambda_f\) is this operator.

(2) For \(\xi\in HS(\mathcal K)\), \(x=\xi h^{-1}\) is bounded and \(\xi\zeta=xh\zeta\) for \(\zeta\in D(h)\), so
\(\xi\in\mathcal B_l\) by Proposition 5.3(2). Thus \(\mathcal B_l=H\) and \(\mathcal A_l=D(S)\), and Theorem 6.2(3) gives
the equalities. \(\square\)

## 7. Equivalent left Hilbert algebras

Different left Hilbert algebras can have the same full completion, and then they carry the same von Neumann algebra and the same weight. This section makes this precise. Two algebras are called equivalent when their full completions are isomorphic, and Theorem 7.3 shows that equivalence is exactly a weight-preserving isomorphism of the left von Neumann algebras.

**Definition 7.1.** An *isomorphism* of left Hilbert algebras \(\Phi\colon\mathcal A_1\to\mathcal A_2\), in Hilbert spaces \(H_1,H_2\), is a linear bijection with \(\Phi(ab)=\Phi(a)\Phi(b)\), \(\Phi(a^\sharp)=\Phi(a)^\sharp\) and \(\langle\Phi a,\Phi b\rangle=\langle a,b\rangle\). For a linear map the last condition is the same as \(\|\Phi a\|=\|a\|\), by polarization. The algebras \(\mathcal A_1\) and \(\mathcal A_2\) are *equivalent*, written \(\mathcal A_1\sim\mathcal A_2\), when their full completions \(\mathcal A_{1,l}\) and \(\mathcal A_{2,l}\) are isomorphic.

**Lemma 7.2** (transport). Let \(\Phi\colon\mathcal A_1\to\mathcal A_2\) be an isomorphism. Its continuous extension \(U\colon H_1\to H_2\) is unitary, and:

1. \(UL_aU^*=L_{\Phi(a)}\) for \(a\in\mathcal A_1\); hence \(UM_1U^*=M_2\) and \(UM_1'U^*=M_2'\).
2. \(UD(S_1)=D(S_2)\) and \(US_1U^*=S_2\); likewise for \(F\); and \(U\Delta_1U^*=\Delta_2\), \(UJ_1U^*=J_2\).
3. \(U\mathcal B_{1,r}=\mathcal B_{2,r}\) with \(UR_\eta U^*=R_{U\eta}\), and \(U\mathcal A_{1,r}=\mathcal A_{2,r}\).
4. \(U\mathcal B_{1,l}=\mathcal B_{2,l}\) with \(U\lambda_\xi U^*=\lambda_{U\xi}\), and \(U\) restricts to an isomorphism \(\mathcal A_{1,l}\to\mathcal A_{2,l}\).
5. \(\psi_2(UxU^*)=\psi_1(x)\) for every \(x\in(M_1)_+\).

**Proof.** \(U\) is isometric with dense range, hence unitary.

(1) For \(a,b\in\mathcal A_1\), \(UL_ab=\Phi(ab)=\Phi(a)\Phi(b)=L_{\Phi(a)}Ub\); both sides are bounded, so \(UL_a=L_{\Phi(a)}U\). Conjugation by \(U\) maps commutants to commutants.

(2) \(U\) maps the graph of \(\sharp_1\) onto the graph of \(\sharp_2\), because \(U(a^\sharp)=\Phi(a)^\sharp\). Closures correspond, so \(US_1U^*=S_2\) with domains. For a conjugate-linear \(A\), \(\langle UAU^*x,y\rangle=\langle AU^*x,U^*y\rangle=\langle A^*U^*y,U^*x\rangle=\langle UA^*U^*y,x\rangle\), so \((UAU^*)^*=UA^*U^*\) with transported domain; hence \(UF_1U^*=F_2\) and \(U\Delta_1U^*=U F_1S_1U^*=\Delta_2\). Spectral calculus is covariant under unitaries, so \(U\Delta_1^{1/2}U^*=\Delta_2^{1/2}\). Then \(S_2=(UJ_1U^*)\Delta_2^{1/2}\) with \(UJ_1U^*\) antiunitary, and the uniqueness of the polar decomposition (Fact 2.4) gives \(J_2=UJ_1U^*\).

(3) As \(\Phi\) is an isometric bijection, \(\|L_a\eta\|\leq c\|a\|\) for all \(a\in\mathcal A_1\) is equivalent to \(\|L_{\Phi a}U\eta\|\leq c\|\Phi a\|\) for all \(\Phi a\in\mathcal A_2\). On \(\mathcal A_2\), \(R_{U\eta}\Phi(a)=L_{\Phi a}U\eta=UR_\eta a\). With (2) this gives the claims.

(4) The same argument works, with \(\mathcal A_r\) as the space of test vectors in the definition of left-bounded vectors. For \(\xi,\zeta\in\mathcal A_{1,l}\), \(U(\lambda_\xi\zeta)=\lambda_{U\xi}U\zeta\) and \(US_1\xi=S_2U\xi\).

(5) For \(x\in(M_1)_+\), \((UxU^*)^{1/2}=Ux^{1/2}U^*\). By (4), \(x^{1/2}=\lambda_\xi\) exactly when \((UxU^*)^{1/2}=\lambda_{U\xi}\), and \(\|U\xi\|=\|\xi\|\). \(\square\)

**Theorem 7.3.** For left Hilbert algebras \(\mathcal A_1\subseteq H_1\) and \(\mathcal A_2\subseteq H_2\), with left von Neumann algebras \(M_i\) and weights \(\psi_i\), the following are equivalent.

1. \(\mathcal A_1\sim\mathcal A_2\).
2. There is a unitary \(U\colon H_1\to H_2\) with \(U\mathcal A_{1,l}=\mathcal A_{2,l}\), \(U(\xi\zeta)=(U\xi)(U\zeta)\) and \(U(S_1\xi)=S_2(U\xi)\) for \(\xi,\zeta\in\mathcal A_{1,l}\).
3. There is a \(*\)-isomorphism \(\alpha\colon M_1\to M_2\) with \(\psi_2\circ\alpha=\psi_1\) on \((M_1)_+\).

Moreover, every \(\alpha\) as in 3 is implemented by a unitary \(V\) as in 2: \(\alpha(x)=VxV^*\). Every unitary as in 2 carries \(M_1'\), \(\mathcal A_{1,r}\), \(\Delta_1\) and \(J_1\) to \(M_2'\), \(\mathcal A_{2,r}\), \(\Delta_2\) and \(J_2\).

**Proof.** (1)\(\Rightarrow\)(2): extend the isomorphism of the full completions to a unitary.

(2)\(\Rightarrow\)(3) and the last sentence: \(U\) restricts to an isomorphism \(\mathcal A_{1,l}\to\mathcal A_{2,l}\). Apply Lemma 7.2 to it. By Fact 2.9, the objects attached to \(\mathcal A_{i,l}\) are those attached to \(\mathcal A_i\). Put \(\alpha(x)=UxU^*\).

(3)\(\Rightarrow\)(1): For \(x\in M_1\), \(\psi_2(\alpha(x)^*\alpha(x))=\psi_2(\alpha(x^*x))=\psi_1(x^*x)\). So \(\alpha\) maps the ideal \(\mathfrak n_{\psi_1}\) of elements of finite weight onto \(\mathfrak n_{\psi_2}\); use \(\alpha^{-1}\) for "onto". By Fact 2.10, \(\mathfrak n_{\psi_i}=\lambda(\mathcal B_{i,l})\), and \(\psi_i(\lambda_\xi^*\lambda_\xi)=\|\xi\|^2\). Define \(V\colon\mathcal B_{1,l}\to\mathcal B_{2,l}\) by \(\lambda_{V\xi}=\alpha(\lambda_\xi)\). Injectivity of \(\lambda\) makes \(V\) well defined, linear and bijective, and
\[
\|V\xi\|^2=\psi_2(\alpha(\lambda_\xi)^*\alpha(\lambda_\xi))=\psi_1(\lambda_\xi^*\lambda_\xi)=\|\xi\|^2 .
\]
Both \(\mathcal B_{i,l}\) are dense (they contain \(\mathcal A_i\)), so \(V\) extends to a unitary \(H_1\to H_2\). For \(x\in M_1\) and \(\xi\in\mathcal B_{1,l}\), covariance (Fact 2.8) gives
\[
\lambda_{V(x\xi)}=\alpha(x\lambda_\xi)=\alpha(x)\lambda_{V\xi}=\lambda_{\alpha(x)V\xi},
\]
so \(Vx\xi=\alpha(x)V\xi\), and by density \(\alpha(x)=VxV^*\). Next, \(\xi\in\mathcal A_{1,l}\) if and only if \(\lambda_\xi\in\mathfrak n_{1,l}\cap\mathfrak n_{1,l}^*\) (Fact 2.8), if and only if \(\alpha(\lambda_\xi)\in\mathfrak n_{2,l}\cap\mathfrak n_{2,l}^*\), if and only if \(V\xi\in\mathcal A_{2,l}\). For \(\xi,\zeta\in\mathcal A_{1,l}\), \(V(\lambda_\xi\zeta)=\alpha(\lambda_\xi)V\zeta=\lambda_{V\xi}V\zeta\), and \(\lambda_{VS\xi}=\alpha(\lambda_\xi^*)=\lambda_{V\xi}^*=\lambda_{SV\xi}\), so \(VS\xi=SV\xi\). Thus \(V\) restricts to an isomorphism of the full completions. \(\square\)

**Corollary 7.4.**

1. Let \(\mathcal C\) be a \(*\)-subalgebra of \(\mathcal A_l\) with \(\mathcal A\subseteq\mathcal C\). With the operations of \(\mathcal A_l\), \(\mathcal C\) satisfies the four axioms; its full completion is \(\mathcal A_l\); and \(\mathcal C\sim\mathcal A\). In particular \(\mathcal A\sim\mathcal A_l\).
2. \(\sim\) is an equivalence relation. Isomorphic left Hilbert algebras are equivalent.
3. Two full left Hilbert algebras are equivalent if and only if they are isomorphic.
4. Equivalent left Hilbert algebras have unitarily equivalent left von Neumann algebras, commutants, modular operators and modular conjugations, and their weights correspond.

**Proof.** (1) \(\mathcal C\) inherits bounded left multiplication (\(L_\xi=\lambda_\xi|_{\mathcal C}\)) and the adjoint identity from \(\mathcal A_l\). Its involution is the restriction of the closed \(S\), hence closable, and its closure lies between the closure of \(\sharp\) on \(\mathcal A\), which is \(S\), and \(S\) itself. \(\mathcal C^2\supseteq\mathcal A^2\) is dense. Its left von Neumann algebra lies between \(L(\mathcal A)''=M\) and \(\lambda(\mathcal A_l)''=M\). For right boundedness, \(\mathcal B_r(\mathcal A_l)\subseteq\mathcal B_r(\mathcal C)\subseteq\mathcal B_r(\mathcal A)\), since the tests are over nested sets, and the outer two are equal (Fact 2.9). In all three, \(R_\eta\) is the bounded extension of \(a\mapsto L_a\eta\) from \(\mathcal A\). So \(\mathcal C_r=\mathcal A_r\), then \(\mathcal B_l(\mathcal C)=\mathcal B_l\) by the definition of left-bounded vectors, and \(\mathcal C_l=\mathcal A_l\). The identity map of \(\mathcal A_l\) shows \(\mathcal C\sim\mathcal A\).

(2) Compose and invert isomorphisms of full completions. For the second claim use part 4 of Lemma 7.2.

(3) Full means \(\mathcal A_i=\mathcal A_{i,l}\).

(4) This is the last sentence of Theorem 7.3. \(\square\)

**Example 7.5** (equivalent but not isomorphic). Let \(\mathcal A_1=c_{00}(\mathbb N)\) and \(\mathcal A_2=\ell^2(\mathbb N)\cap\ell^\infty(\mathbb N)\), with pointwise operations in \(\ell^2(\mathbb N)\). Both have full completion \(\ell^2\cap\ell^\infty\): for \(\mathcal A_1\), Fact 2.12(d) gives \(\mathcal A_{1,r}=\ell^2\cap\ell^\infty\), and then Proposition 3.1 (for counting measure) gives \(\mathcal B_l\) and fullness. So \(\mathcal A_1\sim\mathcal A_2\). They are not isomorphic, not even as vector spaces. \(c_{00}(\mathbb N)\) has a countable Hamel basis. \(\ell^2\cap\ell^\infty\) contains the vectors \(x_t=(t^n)_{n\geq1}\), \(0<t<1\), and finitely many of them with distinct \(t\) are linearly independent: a vanishing combination \(\sum_jc_jt_j^n=0\) for \(n=1,\dots,k\) forces \(c=0\), because the matrix \((t_j^n)\) has determinant \(\prod_jt_j\prod_{i<j}(t_j-t_i)\neq0\).

**Example 7.6** (same modular data, not equivalent). On \(H=M_2(\mathbb C)\) with \(\langle x,y\rangle=\operatorname{Tr}(y^*x)\), fix \(c>0\) and let \(\mathcal A^{(c)}\) be \(M_2(\mathbb C)\) with the product \(x\circ y=c\,xy\), involution \(x^\sharp=x^*\), and this inner product. It is associative, \(L^{(c)}_x\) is left multiplication by \(cx\), and \(\langle x\circ y,z\rangle=\langle y,cx^*z\rangle=\langle y,x^\sharp\circ z\rangle\). The involution is isometric and \(\mathcal A^{(c)}\circ\mathcal A^{(c)}=M_2(\mathbb C)\). So each \(\mathcal A^{(c)}\) is a complete, hence full, left Hilbert algebra. All of them have the same \(H\), \(S=J=(x\mapsto x^*)\), \(\Delta=I\) and \(M=\{y\mapsto xy\}\). The weight of \(\mathcal A^{(c)}\) is \(\psi_c(a)=\|a^{1/2}/c\|^2=c^{-2}\operatorname{Tr}(a)\), since \(\lambda^{(c)}_\xi\) is left multiplication by \(c\xi\). If \(\mathcal A^{(c)}\sim\mathcal A^{(1)}\), Theorem 7.3 gives \(\alpha\) with \(\psi_1\circ\alpha=\psi_c\); at \(a=1\) this reads \(2=2c^{-2}\), so \(c=1\). Thus, for \(c\neq1\), the modular data do not determine the equivalence class; the weight does.

## 8. Fullness, completeness and the unit ball

A full left Hilbert algebra carries a natural Banach algebra norm, and fullness can be read off its unit ball. Both facts are stated first as exercises and then proved in a more general form.

### A Banach algebra norm

**Exercise 8.1.** For a full left Hilbert algebra \(\mathcal A\), put \(|||\xi|||=\max\{\|L_\xi\|,\|\xi\|,\|\xi^\sharp\|\}\). Show that \((\mathcal A,|||\cdot|||)\) is a Banach algebra with isometric involution.

**Theorem 8.2** (solution of Exercise 8.1, in a more general form). Let \(\mathcal A\) be any left Hilbert algebra, and put \(|||\xi|||=\max\{\|\lambda_\xi\|,\|\xi\|,\|S\xi\|\}\) on \(\mathcal A_l\).

1. \((\mathcal A_l,|||\cdot|||)\) is a Banach algebra, \(S\) is an isometric involution on it, and \(\xi\mapsto\lambda_\xi\) is an injective contractive \(*\)-homomorphism into \(M\).
2. \(\mathcal A\) is a \(*\)-subalgebra. It is \(|||\cdot|||\)-complete if and only if it is \(|||\cdot|||\)-closed in \(\mathcal A_l\). In particular, a full left Hilbert algebra is complete; this solves Exercise 8.1.
3. The converse of Exercise 8.1 fails: \(C_0(0,1)\) in \(L^2(0,1)\) is a \(|||\cdot|||\)-complete left Hilbert algebra that is not full.
4. \(|||\cdot|||\) need not be a C\(^*\)-norm.

*Remark.* Theorem 8.2 extends Exercise 8.1 from full left Hilbert algebras to the full completion of any left Hilbert algebra; parts 3 and 4 go beyond the exercise.

**Proof.** (1) \(|||\cdot|||\) is a norm, since it dominates the Hilbert norm. For \(\xi,\zeta\in\mathcal A_l\): \(\|\lambda_{\xi\zeta}\|=\|\lambda_\xi\lambda_\zeta\|\leq\|\lambda_\xi\|\|\lambda_\zeta\|\) (Fact 2.8); \(\|\xi\zeta\|=\|\lambda_\xi\zeta\|\leq\|\lambda_\xi\|\|\zeta\|\); and \(\|S(\xi\zeta)\|=\|(S\zeta)(S\xi)\|=\|\lambda_\zeta^*S\xi\|\leq\|\lambda_\zeta\|\|S\xi\|\). Each is at most \(|||\xi|||\,|||\zeta|||\). Since \(\|\lambda_{S\xi}\|=\|\lambda_\xi^*\|\), \(|||S\xi|||=|||\xi|||\). For completeness, let \((\xi_n)\) be \(|||\cdot|||\)-Cauchy. Then \(\xi_n\to\xi\) and \(S\xi_n\to\zeta\) in \(H\), and \(\lambda_{\xi_n}\to x\) in norm. As \(S\) is closed, \(\xi\in D(S)\) and \(S\xi=\zeta\). For \(\eta\in\mathcal A_r\), \(R_\eta\xi=\lim R_\eta\xi_n=\lim\lambda_{\xi_n}\eta=x\eta\), so \(\|R_\eta\xi\|\leq\|x\|\|\eta\|\): \(\xi\in\mathcal B_l\) and \(\lambda_\xi=x\) (as in Fact 2.11(a)). So \(\xi\in\mathcal A_l\) and \(|||\xi_n-\xi|||\to0\). The last claim follows from Fact 2.8 and \(\|\lambda_\xi\|\leq|||\xi|||\).

(2) A subspace of a Banach space is complete exactly when it is closed. If \(\mathcal A\) is full, it equals \(\mathcal A_l\).

(3) By Example 3.4, \(C_c(0,1)\) has full completion \(L^\infty(0,1)\), with \(\lambda_f=m_f\). There \(|||f|||=\max\{\|f\|_\infty,\|f\|_2\}=\|f\|_\infty\), since \((0,1)\) has measure \(1\). The algebra \(C_0(0,1)\) of continuous functions with limit \(0\) at both ends lies between \(C_c(0,1)\) and \(L^\infty(0,1)\). By Corollary 7.4(1), it satisfies the axioms and its full completion is again \(L^\infty(0,1)\). The essential supremum of a continuous function is its supremum, so \(C_0(0,1)\) is closed in \(L^\infty(0,1)\) under uniform convergence. Hence it is \(|||\cdot|||\)-complete. It is not full: \(1_{(0,1/2)}\) lies in \(L^\infty(0,1)\setminus C_0(0,1)\).

(4) In \(M_2(\mathbb C)\) with \(\langle x,y\rangle=\operatorname{Tr}(y^*x)\) (complete, hence full), \(|||1|||=\max\{1,\sqrt2,\sqrt2\}=\sqrt2\), while \(|||1^\sharp1|||=\sqrt2\neq2=|||1|||^2\). \(\square\)

### Fullness and the unit ball

**Exercise 8.3.** Prove: \(\mathcal A\) is full exactly when the set \(\{\xi\in\mathcal A:\|L_\xi\|\leq1\}\) is closed in \(D(S)\).

For a set \(\mathcal X\) of left-bounded vectors write \(\mathcal X_1=\{\xi\in\mathcal X:\|\lambda_\xi\|\leq1\}\).

**Theorem 8.4** (solution of Exercise 8.3). Let \(\mathcal A\) be any left Hilbert algebra.

1. The closure of \(\mathcal A_1\) in \(D(S)\), for the graph norm of \(S\), is \((\mathcal A_l)_1\).
2. The closure of \(\mathcal A_1\) in \(H\) is \((\mathcal B_l)_1\). Hence its closure in \(D(S)\) for the Hilbert norm is also \((\mathcal A_l)_1\).
3. The following are equivalent: (a) \(\mathcal A\) is full; (b) \(\mathcal A_1\) is closed in \(D(S)\) for the graph norm; (c) \(\mathcal A_1\) is closed in \(D(S)\) for the Hilbert norm. Then \(\mathcal A_1\) is closed for every topology on \(D(S)\) between these two.

Exercise 8.3 does not say which topology on \(D(S)\) is meant. Part 3 shows that the answer is the same for the Hilbert norm and for the graph norm.

**Proof.** First a limit fact. If \(\xi_n\in(\mathcal B_l)_1\) and \(\xi_n\to\xi\) in \(H\), then for \(\eta\in\mathcal A_r\),
\[
R_\eta\xi=\lim_nR_\eta\xi_n=\lim_n\lambda_{\xi_n}\eta,\qquad\text{so}\qquad\|R_\eta\xi\|\leq\|\eta\| .
\tag{8.1}
\]
So \(\xi\in(\mathcal B_l)_1\). Thus \((\mathcal B_l)_1\) is closed in \(H\), and \((\mathcal A_l)_1=(\mathcal B_l)_1\cap D(S)\) is closed in \(D(S)\) for both norms. Both norms are metrizable, so sequences suffice.

(1) By (8.1), the graph closure of \(\mathcal A_1\) lies in \((\mathcal A_l)_1\). Conversely, by Fact 2.11(b), each \(\xi\in(\mathcal A_l)_1\) is a graph-norm limit of vectors \(a_n\in\mathcal A\) with \(\|L_{a_n}\|\leq\|\lambda_\xi\|\leq1\).

(2) Likewise, with Fact 2.11(c) for the reverse inclusion. The closure of a subset of \(D(S)\) in the relative Hilbert topology is its closure in \(H\) intersected with \(D(S)\), which is \((\mathcal B_l)_1\cap D(S)=(\mathcal A_l)_1\).

(3) If \(\mathcal A\) is full, \(\mathcal A_1=(\mathcal A_l)_1\), which is closed for both norms. The graph topology is finer than the relative Hilbert topology, so (c) implies (b). Assume (b). By (1), \(\mathcal A_1=(\mathcal A_l)_1\). If \(0\neq\xi\in\mathcal A_l\), then \(\lambda_\xi\neq0\) (Fact 2.8), and \(\xi/\|\lambda_\xi\|\in(\mathcal A_l)_1=\mathcal A_1\subseteq\mathcal A\). So \(\mathcal A_l=\mathcal A\). A set closed for the coarser topology is closed for every finer one; this gives the last sentence. \(\square\)

## 9. Complete left Hilbert algebras are atomic

A left Hilbert algebra is *complete* if it is all of its Hilbert space. For example, every finite-dimensional left Hilbert algebra is complete, and so is the full completion of the group algebra of a compact group (Example 4.4). This section shows that complete left Hilbert algebras always generate direct sums of type I factors. We again state the result as an exercise first.

**Exercise 9.1.** Let \(\mathcal A\) be complete, that is \(\mathcal A=H\), and \(\mathcal A\neq\{0\}\). (a) Show that \(\mathcal A\) has a projection. (b) Show that \(\|ab\|\leq K\|a\|\|b\|\) for some constant \(K>0\). (c) Show \(\|e\|\geq1/K\) for every projection \(e\). (d) Let \(\lambda=\inf\{\|e\|^2:e\text{ a projection of }\mathcal A\}\); show that \(\|e\|^2<2\lambda\) forces \(L_e\) to be a minimal projection of \(M\). (e) Show that \(M\) splits as a direct sum of type I factors.

**Theorem 9.2** (solution of Exercise 9.1). Assume \(\mathcal A=H\neq\{0\}\). Everything below also applies to the full completion of any left Hilbert algebra whose full completion is all of \(H\), for example \(C(G)\) for a compact group (Example 4.4).

0. \(\mathcal A\) is full, \(\mathcal B_l=\mathcal B_r=\mathcal A_r=H\), and \(S\), \(F\) are bounded.
1. (a) \(\mathcal A\) has a projection.
2. (b) \(\|ab\|\leq K\|a\|\|b\|\) for some \(K>0\).
3. (c) \(\|e\|\geq1/K\) and \(\|e\|^2\geq1/K^2\) for every projection \(e\).
4. (d, localized) For a nonzero projection \(q\in M\), let \(\lambda_q\) be the infimum of \(\|f\|^2\) over the projections \(f\) of \(\mathcal A\) with \(L_f\leq q\). Then \(\lambda_q\geq1/K^2\). If \(L_f\leq q\) and \(\|f\|^2<2\lambda_q\), then \(L_f\) is a minimal projection of \(M\). The case \(q=1\) is part (d) of Exercise 9.1, with \(\lambda=\lambda_1\geq1/K^2\).
5. (e) Every nonzero projection of \(M\) dominates a minimal projection of \(M\), and \(M\) is a direct sum of type I factors.

*Remark.* The bound \(\lambda\geq1/K\) can fail (Example 9.3); the correct bound is \(\lambda\geq1/K^2\), and it is attained.

**Proof.** (0) \(\mathcal A=H\subseteq\mathcal A_l\subseteq H\), so \(\mathcal A\) is full, \(\mathcal B_l=H\) and \(\lambda=L\). The closure \(S\) of \(\sharp\) extends an everywhere-defined map, so \(S=\sharp\) is closed and everywhere defined. With the canonical conjugate-linear isometry \(C_H\colon H\to\overline H\) (Fact 2.2), \(C_HS\) is a closed linear map \(H\to\overline H\), bounded by the closed graph theorem. So \(S\) is bounded. Then \(x\mapsto\langle Sx,y\rangle\) is bounded for every \(y\), so \(F=S^*\) is everywhere defined (Fact 2.2), and it is bounded because \(|\langle Fy,x\rangle|=|\langle Sx,y\rangle|\leq\|S\|\|x\|\|y\|\). For \(\eta\in H=D(F)\), Fact 2.7(b) says that \(a\mapsto L_a\eta\) is closable on \(\mathcal A=H\). An everywhere-defined closable operator is closed, hence bounded. So \(\eta\in\mathcal B_r\), and \(\mathcal B_r=\mathcal A_r=H\).

(b) The linear map \(a\mapsto L_a\) from \(H\) to the Banach space \(B(H)\) has closed graph: if \(a_n\to a\) and \(L_{a_n}\to T\) in norm, then for every \(b\), \(L_{a_n}b=R_ba_n\to R_ba=L_ab\), so \(T=L_a\). By the closed graph theorem, \(\|L_a\|\leq K\|a\|\) for some \(K\), which we may take positive. Then \(\|ab\|\leq\|L_a\|\|b\|\leq K\|a\|\|b\|\).

(a) Pick \(a\neq0\). The vectors \(a+a^\sharp\) and \(i(a-a^\sharp)\) are fixed by \(\sharp\), and \(2a=(a+a^\sharp)-i\cdot i(a-a^\sharp)\), so one of them is nonzero; call it \(\xi\). Then \(x=L_\xi\) is self-adjoint and nonzero. Its spectrum contains a point \(t_0\) with \(|t_0|=\|x\|\). Let \(\Omega=\{t:|t|\geq\|x\|/2\}\) and \(g(t)=t^{-1}1_\Omega(t)\), a bounded Borel function. By Fact 2.14, \(p=1_\Omega(x)\) and \(g(x)\) lie in \(M\). And \(p\neq0\), because \(\Omega\) contains an open interval around the spectral point \(t_0\). Also \(g(x)x=p\). Put \(e=g(x)\xi\). Covariance (Fact 2.8) gives \(\lambda_e=g(x)\lambda_\xi=p\). So \(L_e=p\) is a nonzero projection. Then \(L_{ee}=L_e^2=L_e\) and \(L_{e^\sharp}=L_e^*=L_e\), and injectivity of \(L\) (Fact 2.1) gives \(ee=e=e^\sharp\).

(c) \(\|e\|=\|ee\|\leq K\|e\|^2\) and \(e\neq0\).

(d) *Splitting.* Let \(e\) be a projection of \(\mathcal A\), and let \(L_e=p_1+p_2\) with \(p_1,p_2\) orthogonal projections of \(M\). Put \(e_i=p_ie\). Covariance gives \(L_{e_i}=p_iL_e=p_i\). As in (a), \(e_ie_i=e_i=e_i^\sharp\), and \(e_i\neq0\) when \(p_i\neq0\). Also \(e_1+e_2=L_ee=ee=e\), and
\[
\langle e_1,e_2\rangle=\langle e_1e_1,e_2\rangle=\langle e_1,e_1^\sharp e_2\rangle=\langle e_1,p_1p_2e\rangle=0 ,
\tag{9.1}
\]
using the adjoint axiom and \(e_1^\sharp e_2=L_{e_1}e_2=p_1p_2e\). Hence \(\|e\|^2=\|e_1\|^2+\|e_2\|^2\).

Now let \(q\) and \(f\) be as in statement 4, and suppose \(L_f\) is not minimal. Then \(L_f\) has a subprojection \(p_1\notin\{0,L_f\}\), and \(p_2=L_f-p_1\) is a nonzero projection orthogonal to \(p_1\). Splitting gives projections \(f_1,f_2\) of \(\mathcal A\) with \(L_{f_i}=p_i\leq L_f\leq q\). So \(\|f_i\|^2\geq\lambda_q\), and by (9.1) \(\|f\|^2=\|f_1\|^2+\|f_2\|^2\geq2\lambda_q\), a contradiction. The bound \(\lambda_q\geq1/K^2\) is (c).

(e) *Step 1.* Let \(q\in M\) be a nonzero projection. Choose \(\xi_0\in H\) with \(q\xi_0\neq0\), and put \(\zeta=q\xi_0\). Then \(L_\zeta=qL_{\xi_0}\neq0\) by covariance and injectivity. The vector \(\zeta\zeta^\sharp\) is fixed by \(\sharp\), and \(x=L_{\zeta\zeta^\sharp}=L_\zeta L_\zeta^*\) is nonzero, with \(x=qxq\). Run the construction of (a) with this \(\xi=\zeta\zeta^\sharp\). It gives a projection \(e\) of \(\mathcal A\) with \(L_e=g(x)x\), and \(g(x)x(1-q)=0\) because \(x(1-q)=0\). So \(L_e\leq q\), and \(\lambda_q<\infty\). Since \(\lambda_q>0\), there is a projection \(f\) with \(L_f\leq q\) and \(\|f\|^2<2\lambda_q\). By (d), \(L_f\) is a minimal projection of \(M\) below \(q\).

*Step 2.* Let \(\mathcal N\) be a von Neumann algebra on \(H\) in which every nonzero projection dominates a minimal one. We show that \(\mathcal N\) is a direct sum of type I factors.

(i) If \(p\) is minimal, then \(p\mathcal Np=\mathbb Cp\). Indeed \(p\mathcal Np\), on \(pH\), is a von Neumann algebra (reduced algebras) whose only projections are \(0\) and \(p\). If a self-adjoint \(y\in p\mathcal Np\) had two points \(s<t\) in its spectrum, disjoint open intervals around them would give two nonzero orthogonal spectral projections in \(p\mathcal Np\) (Fact 2.14). So the spectrum of \(y\) is one point \(s\), and \(y=sp\).

(ii) For a projection \(p\in\mathcal N\), let \(z_p\) be the projection onto the closed span of \(\mathcal NpH\). This subspace is invariant under \(\mathcal N\) and under \(\mathcal N'\) (as \(x'yp\xi=ypx'\xi\)). So \(z_p\) commutes with \(\mathcal N\) and with \(\mathcal N'\): it is a central projection of \(\mathcal N=\mathcal N''\), and \(p\leq z_p\). If \(z\) is a central projection with \(p\leq z\), then \(\mathcal NpH=\mathcal NzpH\subseteq zH\), so \(z_p\leq z\).

(iii) If \(p\) is minimal, \(z_p\) is a minimal central projection. Let \(z\leq z_p\) be a central projection. Then \(zp\) is a projection in \(p\mathcal Np\), so \(zp\in\{0,p\}\) by (i). If \(zp=p\), then \(p\leq z\), so \(z_p\leq z\) and \(z=z_p\). If \(zp=0\), then \(p\leq1-z\), so \(z_p\leq1-z\) and \(z=zz_p=0\).

(iv) The algebra \(\mathcal Nz_p\), on \(z_pH\), is a factor. A central projection \(w\) of \(\mathcal Nz_p\) satisfies, for \(y\in\mathcal N\), \(yw=(yz_p)w=w(yz_p)=wy\). So \(w\) is central in \(\mathcal N\) and \(w\leq z_p\), hence \(w\in\{0,z_p\}\) by (iii). The factor contains \(p\), and \(p\mathcal Np=\mathbb Cp\) is abelian. A factor with a nonzero abelian projection is of type I (Fact 2.14).

(v) Two minimal central projections \(z,z'\) are equal or orthogonal: \(zz'\) is a central projection below both. Let \((z_k)\) be the distinct projections \(z_p\), \(p\) minimal, and \(z_0=1-\sum_kz_k\) (a strong sum of orthogonal projections), a central projection. If \(z_0\neq0\), it dominates a minimal projection \(p_0\). Then \(z_{p_0}\leq z_0\) by (ii), but \(z_{p_0}\) is one of the \(z_k\), which is orthogonal to \(z_0\). So \(z_{p_0}=0\) and \(p_0=0\), a contradiction. Hence \(\sum_kz_k=1\).

(vi) The map \(x\mapsto(xz_k)_k\) is a \(*\)-isomorphism of \(\mathcal N\) onto the algebra of bounded families \((y_k)\) with \(y_k\in\mathcal Nz_k\). It is injective because \(x=\sum_kxz_k\) strongly. It is onto because, for a bounded family, the partial sums of \(\sum_ky_k\) are bounded and converge strongly, and \(\mathcal N\) is strongly closed.

Step 1 lets us apply Step 2 to \(\mathcal N=M\). \(\square\)

**Example 9.3** (the bound in part (c) is attained). Part (c) gives \(\|e\|^2\geq1/K^2\), so \(\lambda\geq1/K^2\), and this cannot be improved to \(\lambda\geq1/K\). Take \(\mathcal A=\mathbb C\), with the usual product and conjugation, and \(\langle x,y\rangle=\gamma\,x\bar y\) for a constant \(0<\gamma<1\). This is a complete left Hilbert algebra. As \(\|xy\|=\gamma^{-1/2}\|x\|\|y\|\), the constant \(K=\gamma^{-1/2}\) is admissible, and it is the smallest one. The only projection is \(1\), with \(\|1\|^2=\gamma\). So \(\lambda=\gamma=1/K^2<1/K\), and the bound \(\lambda\geq1/K^2\) is attained. The argument of (d) needs only \(\lambda>0\).

**Remarks 9.4.**

1. By Fact 2.10, \(\psi(L_e)=\|e\|^2\) for a projection \(e\). Every minimal projection \(p\) of \(M\) dominates, by Step 1, a minimal projection \(L_f\), so \(p=L_f\). Every \(L_e\) dominates such an \(L_f\), and \(\psi(L_f)\leq\psi(L_e)\). Thus \(\lambda\) is the infimum of the weights of the minimal projections, and (c) says that this infimum is at least \(1/K^2\). It need not be attained: in Exercise 10.3, with \(n_k=1\) and \(\gamma_k=\gamma(1+1/k)\), the minimal projections have weights \(\gamma_k>\gamma=\lambda\).
2. That each type I factor in (e) is isomorphic to some \(B(\mathcal K)\) is standard and is not needed here.
3. Completeness cannot be weakened to boundedness of \(S\). In \(L^2(0,1)\cap L^\infty(0,1)=L^\infty(0,1)\) (Proposition 3.1), \(S\) is even isometric, but \(M\) is the multiplication algebra of \(L^\infty(0,1)\) (Fact 2.12(f)). A nonzero projection \(m_{1_E}\) there has the proper subprojection \(m_{1_{E'}}\) for any \(E'\subseteq E\) with \(0<|E'|<|E|\), so \(M\) has no minimal projection at all.
4. Conversely, \(M\) can be atomic without \(\mathcal A_l=H\). For \(c_{00}(\mathbb N)\) with weights \(\mu_k=k^{-2}\) (Fact 2.12(d)), \(M=\ell^\infty(\mathbb N)\) is atomic, but the full completion \(\ell^2(\mu)\cap\ell^\infty\) is not \(\ell^2(\mu)\): the vector \((k^{0.4})_k\) lies in \(\ell^2(\mu)\) and is unbounded.

## 10. Exercises

**Exercise 10.1** (scaling a weight on \(B(\mathcal K)\)). For \(c>0\) let \(\mathcal A_{ch}\) be the algebra of Section 5 built from \(ch\). (1) Show that its weight is \(c^2\psi_h\). (2) If \(h\) is Hilbert–Schmidt and \(\mathcal K\neq0\), show that \(\mathcal A_{ch}\sim\mathcal A_h\) only for \(c=1\). (3) Let \(\mathcal K=\ell^2(\mathbb Z)\) and \(he_n=2^{n/2}e_n\). Show that \(\mathcal A_{\sqrt2h}\sim\mathcal A_h\).

*Solution.* (1) By Proposition 5.3(3), \(\psi_{ch}(b)=\|\overline{b^{1/2}ch}\|^2=c^2\psi_h(b)\), with the same infinite values. (2) An equivalence gives \(\alpha\) with \(\psi_h\circ\alpha=\psi_{ch}\) (Theorem 7.3; both algebras generate \(\ell(B(\mathcal K))\)). At \(b=1\), \(\|h\|_{HS}^2=c^2\|h\|_{HS}^2\), and \(\|h\|_{HS}\neq0\), so \(c=1\). (3) Let \(ue_n=e_{n+1}\). Then \(u^*hue_n=2^{(n+1)/2}e_n\), so \(u^*hu=\sqrt2\,h\), including domains: \(uv\in D(h)\) iff \(\sum_n2^{n+1}|v_n|^2<\infty\) iff \(v\in D(h)\). Hence \(u^*h=\sqrt2\,hu^*\) on \(D(h)=uD(h)\). For \(b\geq0\) and \(\alpha(b)=ubu^*\), \((ubu^*)^{1/2}h=ub^{1/2}u^*h=\sqrt2\,u\,b^{1/2}h\,u^*\) on \(D(h)\). Unitaries do not change Hilbert–Schmidt norms or the existence of extensions, so \(\psi_h(\alpha(b))=2\psi_h(b)=\psi_{\sqrt2h}(b)\) for all \(b\geq0\), infinite values included. The implication (3)\(\Rightarrow\)(1) of Theorem 7.3 gives \(\mathcal A_{\sqrt2h}\sim\mathcal A_h\).

**Exercise 10.2** (when the model is full). Show that the algebra \(\mathcal A\) of Section 5 is full exactly when \(\dim\mathcal K<\infty\).

*Solution.* If \(\dim\mathcal K<\infty\), \(h\) is an invertible matrix, \(D(h)=D(h^{-1})=\mathcal K\), and \(\mathcal A\) is all of \(HS(\mathcal K)\): complete, hence full. If \(\dim\mathcal K=\infty\), the dense subspace \(D(h)\) contains an orthonormal sequence \((u_k)\) (Gram–Schmidt inside \(D(h)\)). Put \(c_k=2^{-k}/(1+\|hu_k\|)\) and \(x=\sum_kc_k\theta_{u_k,u_k}\), a bounded self-adjoint operator. On \(D(h)\), \(xh\zeta=\sum_kc_k\langle\zeta,hu_k\rangle u_k\), so \(xh\) extends to \(\xi=\sum_kc_k\theta_{u_k,hu_k}\), a Hilbert–Schmidt series with \(\sum_kc_k\|hu_k\|<\infty\). As \(x^*=x\), Proposition 5.3(2) gives \(\xi\in\mathcal A_l\). But \(\xi^*u_j=c_jhu_j\), and the vectors \(hu_j\) are linearly independent, so \(\xi^*\) and \(\xi\) have infinite rank. Every element of \(\mathcal A\) has finite rank, so \(\xi\notin\mathcal A\).

**Exercise 10.3** (the constants of Theorem 9.2 are sharp). Let \(n_k\geq1\) and \(\gamma_k>0\) for \(k\in\mathbb N\). Let \(H\) be the space of sequences \(a=(a_k)\), \(a_k\in M_{n_k}(\mathbb C)\), with \(\|a\|^2=\sum_k\gamma_k\operatorname{Tr}(a_k^*a_k)<\infty\), with blockwise product and adjoint. Show: if \(\gamma=\inf_k\gamma_k>0\), then \(H\) is a complete left Hilbert algebra, the best constant in part (b) of Theorem 9.2 is \(K=\gamma^{-1/2}\), and \(\lambda=\gamma=1/K^2\). If \(\gamma=0\), show by an example that \(H\) need not be closed under the product.

*Solution.* Write \(\|a_k\|_{HS}^2=\operatorname{Tr}(a_k^*a_k)\). Then \(\|a_k\|_{op}\leq\|a_k\|_{HS}\leq\gamma_k^{-1/2}\|a\|\leq\gamma^{-1/2}\|a\|\), so
\[
\|ab\|^2=\sum_k\gamma_k\|a_kb_k\|_{HS}^2\leq\sup_k\|a_k\|_{op}^2\,\|b\|^2\leq\gamma^{-1}\|a\|^2\|b\|^2 .
\]
So \(H\) is closed under the product, with \(K=\gamma^{-1/2}\) admissible. The adjoint axiom holds blockwise, the adjoint is isometric, and finite block sums, which are products with block units, are dense. So \(H\) is a complete (unimodular) left Hilbert algebra. A rank-one projection \(e\) in block \(k\) has \(\|e\|^2=\gamma_k\), and \(\|e\|=\|ee\|\leq K\|e\|^2\) forces \(K\geq\gamma_k^{-1/2}\) for every \(k\). So the best constant is \(\gamma^{-1/2}\). The blocks \(e_k\) of a projection \(e\) of \(H\) are orthogonal projections, so \(\|e\|^2=\sum_k\gamma_k\operatorname{rank}(e_k)\geq\gamma\) when \(e\neq0\), while the rank-one projections of block \(k\) give \(\gamma_k\). So \(\lambda=\gamma=1/K^2\). If \(\gamma=0\), take \(n_k=1\), \(\gamma_k=k^{-2}\) and \(a_k=k^{2/5}\): then \(\sum_kk^{-2}k^{4/5}<\infty\) but \(\sum_kk^{-2}k^{8/5}=\infty\), so \(a\in H\) and \(a^2\notin H\).

## Where this leads

- The central theorem of Tomita–Takesaki theory says that \(JMJ=M'\) and \(\Delta^{it}M\Delta^{-it}=M\) for all real \(t\). It is proved in the lesson *The modular group and its analytic algebra* of the course *Modular theory and weights*.
- The weight of the group algebra of Section 4 is the Plancherel weight of \(G\); see the lesson *The Plancherel weight and Fourier coefficients of a locally compact group*.
- Further topics include Tomita algebras, built from the vectors that are entire for the modular group, and direct integrals of left Hilbert algebras.

## References



- [Combes 1971] F. Combes, *Poids associé à une algèbre hilbertienne à gauche*, Compositio Mathematica 23 (1971), 49–77. https://www.numdam.org/item/CM_1971__23_1_49_0/
- [Dixmier 1952] J. Dixmier, *Algèbres quasi-unitaires*, Commentarii Mathematici Helvetici 26 (1952), 275–322. https://www.e-periodica.ch/digbib/view?pid=com-001:1952:26::306

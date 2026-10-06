# Square-integrable representations and random operators

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

On an ordinary measure space \((X,\mu)\), a "random Hilbert space" is a measurable field of Hilbert spaces
\((H_x)_{x\in X}\), and a "random operator" is a bounded measurable field of operators \((T_x)\), taken modulo equality
almost everywhere. The random operators on a field form the von Neumann algebra of decomposable operators on
\(\int^\oplus H_x\,d\mu(x)\). This lesson carries out the same construction on the "space of orbits" of a measured
groupoid \((G,\Lambda)\), where \(\Lambda\) is a transverse measure. That space is in general singular: it can have no
non-constant measurable functions at all. So a field of Hilbert spaces over it is replaced by a *representation* of
\(G\): a measurable field \((H_x)_{x\in G^{(0)}}\) over the units together with unitaries \(U(\gamma):H_x\to H_y\) for
every arrow \(\gamma:x\to y\). A field of operators is replaced by an *intertwiner* \((T_x)\) with
\(U(\gamma)T_x=T_yU(\gamma)\). Two such operators are identified when they differ only on a saturated set that is
negligible for \(\Lambda\).

Two new phenomena appear. First, one must restrict to *square-integrable* representations: those that sit inside a
multiple of a left regular representation \(L^\nu\) on \(L^2(G^y,\nu^y)\). Without this restriction the resulting
category does not have the right properties; for a group \(G\) it is the familiar class of representations contained
in a multiple of the regular representation. Second, the algebra of random operators \(\operatorname{End}_\Lambda(H)\)
is a von Neumann algebra, but not because it is visibly a weakly closed algebra of operators on a Hilbert space: it
acts on no canonical Hilbert space. We prove it by identifying \(\operatorname{End}_\Lambda(H)\) with the commutant of
a von Neumann algebra \(W(\nu)\), built from a left Hilbert algebra of functions on \(G\), in a representation on
\(\int^\oplus H_x\,d\Lambda_\nu(x)\).

The main results are these.

1. A representation is square integrable if and only if it has a countable total family of vectors with square
   integrable coefficients, if and only if it is contained in \(\bigoplus_1^\infty L^\nu\), if and only if it is
   contained in a representation that absorbs tensor products (Theorem 4.4). Square integrability is stable under
   subrepresentations, sums, tensor products, and pull-backs along proper homomorphisms (Section 4).
2. For a \(\sigma\)-finite transverse measure \(\Lambda\), the random operators on a square-integrable representation
   form a von Neumann algebra (Theorem 7.2); semi-finiteness of \(\Lambda\) does not suffice (Example 7.6). For each proper transverse function \(\nu\) there is a unique normal
   representation of \(W(\nu)\) on \(\nu(H)=\int^\oplus H_x\,d\Lambda_\nu(x)\) whose commutant is
   \(\operatorname{End}_\Lambda(H)\) when \(\nu\) is faithful (Theorem 7.1). The "continuous sums of rank-one
   operators" \(\theta_\nu(\xi,\eta)\) span an ideal, weakly dense when \(\nu\) is faithful (Corollary 7.3).
3. When \(G\) is a standard Borel space and the isotropy groups are trivial, the centre of \(\operatorname{End}_\Lambda(H)\) consists of the invariant
   scalar functions. If \(\Lambda\neq0\), \(\operatorname{End}_\Lambda(H)\) is a factor for every nonzero random
   Hilbert space \(H\) exactly when \(\Lambda\) is ergodic; and \(\operatorname{End}_\Lambda(H)\) is of type I for
   every \(H\), equivalently for one \(H\) whose fibres are nonzero off a negligible saturated set, exactly when the
   orbit space is "smooth" off a negligible saturated set (Section 8).

These results are used in the next lesson, "Weights on random operators and formal dimension", which attaches normal
weights on \(\operatorname{End}_\Lambda(H)\) to positive random operators of degree one.

**What is assumed.** From this course we use "Measured groupoids and transverse measures": kernels, transverse
functions, transverse measures and their negligible sets, proper \(G\)-spaces and proper homomorphisms. Section 1
restates exactly what is used. We also use measurable fields of Hilbert spaces and direct integrals, the definition of
a left Hilbert algebra, basic von Neumann algebra theory (the double commutant theorem, normal representations,
projections and types), the martingale convergence theorem, and a few facts on standard Borel spaces; these are listed
in "Results used from other lessons", with the place where each is proved.

Basic references are [Connes 1979], [Connes 1982] and [Connes 1994].

**Conventions.**

- Inner products are linear in the first variable. For vectors \(\xi,\eta\), \(\xi\eta^*\) denotes the operator
  \(\zeta\mapsto\langle\zeta,\eta\rangle\xi\). All Hilbert spaces are separable.
- For a function \(f\) on \(G\) we write \(\tilde f(\gamma)=f(\gamma^{-1})\) and
  \(f^\flat(\gamma)=\overline{f(\gamma^{-1})}\). For \(a\) on \(G^{(0)}\), \(a\circ r\) and \(a\circ s\) are
  functions on \(G\).
- \(\mathcal F^+(Z)\) is the set of measurable maps \(Z\to[0,\infty]\), and \(0\cdot\infty=0\).
- A family \(S\) of sections of a field \((H_x)\) is *total* if \(\{\xi_x:\xi\in S\}\) is total in \(H_x\) for every
  \(x\).
- "Transverse measure of modulus \(\delta\)" is what the lesson "Measured groupoids and transverse measures" calls a
  transverse measure of module \(\delta\).

## Results used from other lessons

**(B1) Measurable fields of Hilbert spaces.** Let \((Z,\mathcal Z)\) be a measurable
space. A *measurable field of Hilbert spaces* is a family \((H_z)_{z\in Z}\) of separable Hilbert spaces with a vector
space \(\mathcal M\) of sections (the *measurable sections*) such that: \(z\mapsto\langle\xi_z,\eta_z\rangle\) is
measurable for \(\xi,\eta\in\mathcal M\); a section \(\eta\) with \(z\mapsto\langle\eta_z,\xi_z\rangle\) measurable
for all \(\xi\in\mathcal M\) belongs to \(\mathcal M\); and there is a countable \(\{\xi^n\}\subset\mathcal M\) (a
*fundamental sequence*) total in every \(H_z\). Then:

(i) a section \(\eta\) is measurable iff \(\langle\eta_z,\xi^n_z\rangle\) is measurable for all \(n\);

(ii) \(z\mapsto\dim H_z\) is measurable, and there are measurable sections \(e^1,e^2,\dots\) such that
\((e^k_z)_{k<\dim H_z+1}\) is an orthonormal basis of \(H_z\) and \(e^k_z=0\) for \(k>\dim H_z\) (Gram–Schmidt applied
to a fundamental sequence); each \(e^k\) is a countable sum \(\sum_na_{kn}\xi^n\) with measurable coefficients
\(a_{kn}\), only finitely many of them nonzero at each point (on each set of a countable measurable partition of \(Z\),
\(e^k\) is a combination of finitely many \(\xi^n\));

(iii) if \((\zeta^k)\) is a countable family of sections, total in every \(H_z\), with \(\langle\zeta^k_z,\xi^n_z
\rangle\) measurable for all \(k,n\), then the \(\zeta^k\) are measurable and form a fundamental sequence;

(iv) a family \((T_z)\) of bounded operators \(T_z:H_z\to H'_z\) between measurable fields is *measurable* if it maps
measurable sections to measurable sections; this holds iff \(z\mapsto\langle T_z\xi^n_z,\xi'^m_z\rangle\) is
measurable for fundamental sequences of both fields; then \(z\mapsto\|T_z\|\) is measurable, the adjoint field is
measurable, and so is \(f(T)=(f(T_z))\) for self-adjoint \(T\) with \(\sup_z\|T_z\|<\infty\) and \(f\) continuous.

The proofs in Measurable fields of Hilbert spaces
and their direct integrals do not use a measure on \(Z\); there (i)–(iii) are Theorem 3.1(3), (1)–(2) and (4), and (iv) is
Theorem 6.2. For \(f(T)\): polynomials in \(T\) are measurable by Theorem 6.2(4), \(f\) is a uniform limit of polynomials on
\([-\sup_z\|T_z\|,\sup_z\|T_z\|]\), and pointwise limits of measurable sections are measurable (Lemma 2.2(3) there).

**(B2) Direct integrals.** Let \(\mu\) be a
\(\sigma\)-finite measure on \((Z,\mathcal Z)\), with \(\mathcal Z\) countably generated, and \((H_z)\) a measurable
field. The direct integral \(\int^\oplus H_z\,d\mu(z)\) is the separable Hilbert space of classes of measurable sections
with \(\int\|\xi_z\|^2\,d\mu<\infty\). A measurable field \((T_z)\) with \(\operatorname{ess\,sup}\|T_z\|<\infty\)
defines a *decomposable* operator \(\int^\oplus T_z\), of norm \(\operatorname{ess\,sup}_\mu\|T_z\|\); it is zero iff
\(T_z=0\) almost everywhere. For \(a\in L^\infty(\mu)\) the decomposable operator \(\int^\oplus a(z)1\) is *diagonal*.
The diagonal operators form an abelian von Neumann algebra \(\mathcal D\), and its commutant is the algebra of
decomposable operators: every operator commuting with \(\mathcal D\) is \(\int^\oplus T_z\) for a bounded measurable
field \((T_z)\), unique up to null sets. For \(H_z=\mathbb C\) this says that \(L^\infty(\mu)\) acting by
multiplication on \(L^2(\mu)\) is maximal abelian. Proved in Measurable fields of Hilbert spaces and their direct
integrals, Theorems 8.2, 9.1 and 10.1 and Decomposable operators and the diagonal algebra, Theorem
5.1.

**(B3) Left Hilbert algebras.** A *left Hilbert algebra* is a complex \(*\)-algebra
\(\mathcal A\), with involution \(\xi\mapsto\xi^\#\), carrying an inner product such that (1)
\(\langle\xi\eta,\zeta\rangle=\langle\eta,\xi^\#\zeta\rangle\); (2) each left multiplication \(\eta\mapsto\xi\eta\)
extends to a bounded operator \(\lambda(\xi)\) on the completion \(\mathfrak H\); (3) the products \(\xi\eta\) span a
dense subspace of \(\mathfrak H\); (4) \(\xi\mapsto\xi^\#\) is closable as a conjugate-linear operator in
\(\mathfrak H\). Its *left von Neumann algebra* is \(\lambda(\mathcal A)''\). This is the definition of Left and right
Hilbert algebras.

**(B4) Von Neumann algebras.** Proved in the course *Foundations of von Neumann algebras*; the providers are listed at the end
of this item.

(i) (Kaplansky density.) If \(\mathcal A\) is a nondegenerate \(*\)-algebra of operators, the unit ball of
\(\mathcal A\) is strongly dense in the unit ball of \(\mathcal A''\); in particular \(1\) is a strong limit of a bounded
net in \(\mathcal A\).

(ii) A normal representation is \(\sigma\)-weakly continuous and strongly continuous on bounded sets; it is determined
by its values on a \(\sigma\)-weakly dense \(*\)-subalgebra. A \(*\)-homomorphism between von Neumann algebras is normal
if it is completely additive on orthogonal families of projections.

(iii) If \(M\subset B(\mathfrak H)\) with \(\mathfrak H\) separable, every normal representation of \(M\) on a separable
Hilbert space is unitarily equivalent to a subrepresentation of \(x\mapsto x\otimes1\) on \(\mathfrak H\otimes\ell^2\).

(iv) A \(\sigma\)-weakly closed two-sided ideal of a von Neumann algebra \(M\) is \(zM\) for a central projection \(z\).
If \(M\) acts on \(\mathfrak H\) and the ideal acts nondegenerately, then \(z=1\).

(v) A von Neumann algebra is of type I iff it has an abelian projection with central support \(1\); then every corner
\(pMp\) is of type I. In a factor with separable predual, any two infinite projections are equivalent.

(vi) (Vigier.) In a von Neumann algebra every bounded increasing net of self-adjoint elements has a least upper bound,
its strong limit; in particular an increasing net of projections has a least upper bound that is a projection. Since a
W\(^*\)-algebra is \(*\)-isomorphic to a von Neumann algebra, and \(*\)-isomorphisms preserve order, the same
holds in every W\(^*\)-algebra.

Providers: (i) Kaplansky's density theorem and its consequences, Theorem 7.1. (ii) Normal
representations are \(\sigma\)-weakly continuous by definition; they are strongly continuous on bounded sets by
Compact and trace-class operators, Lemma 8.5 and Theorem 9.1(ii), and they are determined by a
\(\sigma\)-weakly dense \(*\)-subalgebra by Spatial tensor products of von Neumann algebras, Proposition
4.3; a \(*\)-homomorphism \(\pi\) between von Neumann algebras that is completely additive on orthogonal families
of projections is normal: for every normal functional \(\psi\) on the target, \(\psi\circ\pi\) is completely additive,
because \(\psi\) is, and so \(\psi\circ\pi\) is normal by The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras, Corollary
11.5. (iii) Spatial tensor products of von Neumann algebras,
Theorem 8.2: its proof takes \(R=\ell^2(I\times\mathbb N)\) for a maximal family \(I\) of mutually
orthogonal cyclic subspaces, which is countable on a separable space. (iv) The double commutant theorem, Theorem
8.3(4): the closure is \(Me\) with \(e\) central the projection onto \([mH]\), and \(e=1\) for a
nondegenerate ideal. (v) Projections and types of von Neumann algebras, Definition 7.1 and Lemma
7.4(1); conversely, if \(e\) is abelian with \(c(e)=1\), every nonzero central \(z\) has \(ze\ne0\)
abelian; a nonzero central projection of \(pMp\) is \(zp\) with \(z\) central (Traces on von Neumann algebras, Lemma
1.5), and \(zp\) majorizes a nonzero abelian projection by Lemma 7.4(1); the last statement is
Proposition 15.2(4) there, since a factor with separable predual is countably decomposable. (vi) The spectral theorem
for bounded self-adjoint operators, Theorem 6.1 (Vigier); every W\(^*\)-algebra is \(*\)-isomorphic to a
von Neumann algebra by The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras.

**(B5) Martingales.** If \(\sigma_1\subset\sigma_2\subset\cdots\) are \(\sigma\)-algebras on a set with a
finite measure \(\beta\), and \(\phi\in L^1(\beta)\) is measurable for \(\sigma_\infty=\sigma(\bigcup_n\sigma_n)\), then
the conditional expectations \(E(\phi\mid\sigma_n)\) converge to \(\phi\) \(\beta\)-almost everywhere. This is in the
core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): [Fremlin, Measure Theory, Volume 2, Theorem 275I](https://www1.essex.ac.uk/maths/people/fremlin/cont27.htm) (free), applied to
\(\beta/\beta(1)\) and to the real and imaginary parts of \(\phi\); since \(\phi\) is \(\sigma_\infty\)-measurable it is its own
conditional expectation on \(\sigma_\infty\).

**(B6) Standard Borel spaces.** An injective Borel map between standard Borel spaces has Borel image and is a
Borel isomorphism onto it (Souslin's theorem). Analytic sets are universally measurable. (Jankov–von Neumann
uniformization theorem.) If \(P\subset A\times B\) is Borel, \(A,B\) standard, the projection \(p_B(P)\) has a
universally measurable map \(\sigma:p_B(P)\to A\) with \((\sigma(b),b)\in P\). A universally measurable map from a
standard Borel space, with a \(\sigma\)-finite measure \(\mu\), to a standard Borel space agrees with a Borel map off a
\(\mu\)-null Borel set. The set of probability measures on a standard Borel space, with the \(\sigma\)-algebra generated
by the maps \(p\mapsto p(E)\), is standard Borel. Proved in Polish spaces and standard Borel
spaces: the first statement is Theorem 4.3(5), universal measurability is Theorem 6.2, and the
uniformization is Theorem 7.7, applied to the projection \(P\to B\) and composed with the projection onto \(A\). The last two statements follow from the isomorphism theorem (Theorem 5.2 there): every standard Borel space is isomorphic to
a compact set \(K\subseteq[0,1]\), namely to \([0,1]\) if it is uncountable, and otherwise to a finite set or to
\(\{0\}\cup\{1/n:n\geq1\}\), which have the same cardinality.

*Borel representatives.* Let \(\sigma:Y\to A\) be \(\mu\)-measurable, that is, measurable for the \(\mu\)-completion of the
Borel sets, and let \(\iota:A\to K\) be an isomorphism. For rational \(q\) the set \(\{\iota\circ\sigma<q\}\) differs from a
Borel set \(B_q\) by a subset of a \(\mu\)-null Borel set \(N_q\). Put \(N=\bigcup_qN_q\). On \(Y\setminus N\) the sets
\(\{\iota\circ\sigma<q\}\setminus N=B_q\setminus N\) are Borel, so \(\iota\circ\sigma\) is Borel there. Fix \(a\in A\), and
put \(\sigma'=\sigma\) on \(Y\setminus N\) and \(\sigma'=a\) on \(N\). Then \(\sigma'\) is Borel and agrees with \(\sigma\)
off \(N\).

*Probability measures.* Let \(\operatorname{Prob}(K)\) carry the \(\sigma\)-algebra \(\Sigma\) generated by the maps
\(p\mapsto p(E)\), \(E\) Borel. For open \(U\subseteq K\) the continuous functions \(h_{U,n}=\min(1,n\,d(\cdot,K\setminus U))\)
(with \(h_{K,n}=1\)) increase to \(1_U\). So two probability measures that agree on \(C(K)\) agree on the open sets, and
hence on all Borel sets by the Monotone Class Theorem ([Fremlin, Volume 1, Theorem
136B](https://www1.essex.ac.uk/maths/people/fremlin/cont13.htm), free). By the Riesz representation theorem (Haar measure
on locally compact groups, Theorem 2.2), every state of \(C(K)\) is
integration against a probability measure. So \(p\mapsto(f\mapsto\int f\,dp)\) is a bijection of
\(\operatorname{Prob}(K)\) onto the state space \(S\) of \(C(K)\). The set \(S\) is weak\*-closed in the unit ball of
\(C(K)^*\), hence weak\*-compact by the Banach–Alaoglu theorem (Weak topologies, Tychonoff, Banach–Alaoglu, Mazur,
bipolars, Krein–Milman and Eberlein–Šmulian, Section
3). The
restrictions to \(K\) of the polynomials with rational coefficients form a dense sequence \((f_n)\) in \(C(K)\) (The
Stone–Weierstrass theorem for functions vanishing at infinity).
On the bounded set \(S\) the evaluation at any \(f\in C(K)\) is a uniform limit of evaluations at the \(f_n\), so the
weak\* topology of \(S\) is the weakest one making the maps \(\phi\mapsto\phi(f_n)\) continuous. Thus
\(\phi\mapsto(\phi(f_n))_n\) is a continuous injection of the compact space \(S\) into \(\mathbb C^{\mathbb N}\), hence a
homeomorphism onto a compact set: \(S\) is compact metrizable, so standard, and its Borel sets are generated by the maps
\(\phi\mapsto\phi(f_n)\). On \(\operatorname{Prob}(K)\) these maps \(p\mapsto\int f_n\,dp\) are \(\Sigma\)-measurable,
because each \(f_n\) is a uniform limit of Borel simple functions. Conversely, for open \(U\) the map
\(p\mapsto p(U)=\sup_n\int h_{U,n}\,dp\) is a supremum of continuous functions on \(S\), hence Borel. The Borel sets \(E\)
for which \(p\mapsto p(E)\) is Borel on \(S\) form a Dynkin class that contains the open sets, which are closed under
finite intersections; so they are all the Borel sets. Hence \(\Sigma\) is the Borel structure of \(S\), and
\((\operatorname{Prob}(K),\Sigma)\) is standard. An isomorphism of a standard Borel space with \(K\) carries its
probability measures and this \(\sigma\)-algebra onto \(\operatorname{Prob}(K)\) and \(\Sigma\).

## 1. Measured groupoids: what we use

This section fixes the setting and restates what is used from the lesson "Measured groupoids and transverse
measures". A reference for this section is [Connes 1979].

### 1.1 Standing assumptions

A *measurable groupoid* \((G,\mathcal B)\) is a groupoid \(G\) (a small category in which every arrow is invertible)
with a \(\sigma\)-algebra \(\mathcal B\) for which range \(r\), source \(s\), inversion and the product
\(G^{(2)}=\{(\gamma_1,\gamma_2):s(\gamma_1)=r(\gamma_2)\}\to G\) are measurable. The units \(G^{(0)}\subset G\) carry
the trace \(\sigma\)-algebra \(\mathcal B_0\). We write \(\gamma:x\to y\) when \(s(\gamma)=x\), \(r(\gamma)=y\), and
\(G^y=r^{-1}(y)\), \(G_x=s^{-1}(x)\), \(G^y_x=G^y\cap G_x\). The group \(G^y_y\) is the *isotropy group* at \(y\).
Units \(x,y\) are *equivalent* (\(x\sim y\)) if \(G^y_x\neq\emptyset\); the classes are the *orbits*; a set of units is
*saturated* if it is a union of orbits.

Throughout the lesson:

- **(S)** \(\mathcal B\) is countably generated (\(G\) is *separable*), and the one-point subsets of \(G^{(0)}\) belong
  to \(\mathcal B_0\). Then \(G^y\), \(G_x\) and \(G^y_x\) are measurable, and \(\mathcal B_0\) is countably generated.
  If \(C_1,C_2,\dots\) generate \(\mathcal B_0\), they separate the points of \(G^{(0)}\) (the sets that do not separate
  two given points form a \(\sigma\)-algebra), so the diagonal
  \(\bigcap_n\big((C_n\times C_n)\cup(C_n^c\times C_n^c)\big)\) of \(G^{(0)}\times G^{(0)}\) is measurable.
- **(F)** \(G\) has a faithful proper transverse function (defined in (R2) below).

The point condition in (S) is the standing assumption of "Measured groupoids and transverse measures", and (F) is its
Hypothesis (F). In Sections 5 and 8 we assume moreover that \((G,\mathcal B)\) is a standard Borel space, and from
Section 6 on we fix a \(\sigma\)-finite transverse measure \(\Lambda\) of modulus \(\delta\); Example 7.6 shows that
semi-finiteness would not suffice. This is said again where it is used.

### 1.2 Recap

The following is taught in "Measured groupoids and transverse measures"; the numbers in parentheses refer to that
lesson.

**(R1) Kernels** (Definition 1.3, Lemma 1.4(a)). A *kernel* \(\lambda\) on \(G\) is a family \((\lambda^y)_{y\in G^{(0)}}\) of measures on \(G\), with
\(\lambda^y\) carried by \(G^y\) and \(y\mapsto\lambda^y(E)\) measurable for \(E\in\mathcal B\) (and \(\lambda\)
s-finite). We write \(\lambda(f)(y)=\lambda^y(f)\). The kernel is *bounded* if \(\sup_y\lambda^y(G)<\infty\) and
*proper* if \(G=\bigcup_nA_n\), \(A_n\) increasing, with \(\sup_{\gamma}\lambda^{s(\gamma)}(\gamma^{-1}A_n)<\infty\);
then \(\sup_y\lambda^y(A_n)<\infty\). For \(h\in\mathcal F^+(G)\), \(h\lambda\) is the kernel \(y\mapsto h\lambda^y\).
For \(f\in\mathcal F^+(G)\) the functions
\[
(\lambda*f)(\gamma)=\int f(\gamma'^{-1}\gamma)\,d\lambda^{r(\gamma)}(\gamma'),\qquad
(f*\tilde\lambda)(\gamma)=\int f(\gamma\gamma')\,d\lambda^{s(\gamma)}(\gamma')
\]
are measurable. For a measure \(m\) carried by \(G^x\) and \(\gamma:x\to y\), \(\gamma m\) is its image under
\(\gamma'\mapsto\gamma\gamma'\).

**(R2) Transverse functions** (Definition 2.1, Lemmas 2.2 and 2.4, Proposition 2.7). A *transverse function* is a kernel \(\nu\) with \(\gamma\nu^x=\nu^y\) for every
\(\gamma:x\to y\). The proper ones form the cone \(\mathcal E^+\); a transverse function is proper iff
\(G=\bigcup_nA_n\), \(A_n\) increasing, with \(\sup_y\nu^y(A_n)<\infty\). The *support* \(\{y:\nu^y\neq0\}\) is
measurable and saturated; \(\nu\) is *faithful* if its support is \(G^{(0)}\). If \(\nu,\nu'\in\mathcal E^+\) and
\(a\in\mathcal F^+(G^{(0)})\) is finite-valued, then \(\nu+\nu'\) and \((a\circ s)\nu\) belong to \(\mathcal E^+\).
*Normalizing functions:* if \(\nu\in\mathcal E^+\) has support \(A\), there is \(f\in\mathcal F^+(G)\) with
\(\nu(f)=1_A\) and \(f>0\) on \(r^{-1}(A)\). *Densities:* if \(\nu_1,\nu_2\in\mathcal E^+\) and \(\nu_1^y\) is absolutely
continuous with respect to \(\nu_2^y\) for every \(y\), then \(\nu_1=(a\circ s)\nu_2\) for a finite-valued
\(a\in\mathcal F^+(G^{(0)})\). (If \(\nu_1\le\nu_2\), then \(a\le1\) holds \(\nu_2^y\)-almost everywhere on \(G^y\) for
every \(y\), and \(\min(a,1)\) may replace \(a\).)

**(R3) Transverse measures** (Definitions 3.1 and 3.2, Lemma 3.3). A *modulus* is a measurable homomorphism \(\delta:G\to\mathbb R_+^*\). A *transverse
measure of modulus \(\delta\)* is a map \(\Lambda:\mathcal E^+\to[0,\infty]\) that is additive, positively homogeneous,
normal (\(\Lambda(\nu)=\sup\Lambda(\nu_n)\) if \(\nu_n\uparrow\nu\) in \(\mathcal E^+\)), and satisfies
\(\Lambda(\nu*\delta\rho)=\Lambda(\nu)\) whenever \(\rho\) is a kernel with \(\rho^y(G)=1\) for all \(y\) and
\(\nu,\nu*\delta\rho\in\mathcal E^+\). For \(\nu\in\mathcal E^+\), \(\Lambda_\nu(E)=\Lambda((1_E\circ s)\nu)\) is a
measure on \(G^{(0)}\), carried by the support of \(\nu\), with \(\Lambda_\nu(a)=\Lambda((a\circ s)\nu)\) and
\(\Lambda_{(a\circ s)\nu}=a\Lambda_\nu\) for finite \(a\in\mathcal F^+(G^{(0)})\), and
\(\Lambda_{\nu+\nu'}=\Lambda_\nu+\Lambda_{\nu'}\). We write \(m_\nu=\Lambda_\nu\circ\nu\) for the measure
\(h\mapsto\int\nu^y(h)\,d\Lambda_\nu(y)\) on \(G\).

**(R4) Modular symmetry** (Theorem 3.5). For \(\nu,\nu'\in\mathcal E^+\) and \(h\in\mathcal F^+(G)\),
\[
\Lambda_{\nu'}\big(\nu(\tilde h)\big)=\Lambda_\nu\big(\nu'(\delta^{-1}h)\big);\qquad\text{in particular}\qquad
m_\nu(\tilde h)=m_\nu(\delta^{-1}h). \tag{1.1}
\]

**(R5) Finiteness and uniqueness** (Proposition 3.9, Theorem 3.8). \(\Lambda\) is \(\sigma\)-finite iff \(\Lambda_\nu\) is \(\sigma\)-finite for one
faithful \(\nu\) iff \(\Lambda_{\nu'}\) is \(\sigma\)-finite for every \(\nu'\in\mathcal E^+\). If \(\nu\) is faithful,
\(\Lambda\mapsto\Lambda_\nu\) is injective on transverse measures of modulus \(\delta\).

**(R6) Negligible sets** (Definition 5.1, Proposition 5.2). A measurable saturated \(A\subset G^{(0)}\) is *\(\Lambda\)-negligible* if
\(\Lambda_\nu(A)=0\) for all \(\nu\in\mathcal E^+\); if \(\nu\) is faithful, this holds as soon as
\(\Lambda_\nu(A)=0\). For measurable \(Z\subset G^{(0)}\) and \(\nu\in\mathcal E^+\), the set
\([Z]_\nu=\{x:\nu^x(s^{-1}(Z))>0\}\) is measurable and saturated, and \(\Lambda_\nu(Z)=0\) iff \([Z]_\nu\) is
\(\Lambda\)-negligible.

**(R7) \(G\)-spaces and random variables** (Definitions 6.1, 6.2 and 6.8, Lemmas 6.7 and 6.11). A *\(G\)-space* is a measurable space \(X\) with a measurable
\(\pi:X\to G^{(0)}\) and a measurable action \((\gamma,z)\mapsto\gamma z\), defined when \(s(\gamma)=\pi(z)\), with
\(\pi(\gamma z)=r(\gamma)\), \(\pi(z)z=z\), \(\gamma_1(\gamma_2z)=(\gamma_1\gamma_2)z\). We write \(X^x=\pi^{-1}(x)\) and
\((\nu*f)(z)=\int f(\gamma^{-1}z)\,d\nu^{\pi(z)}(\gamma)\). It is *proper* if for some (equivalently every) faithful
\(\nu\in\mathcal E^+\) there is \(f\in\mathcal F^+(X)\) with \(\nu*f=1\); one can then take \(f>0\) everywhere. A
*random variable of modulus \(\rho\)* is a \(G\)-space with measures \(\alpha^x\) carried by \(X^x\), \(x\mapsto
\alpha^x(E)\) measurable, \(X=\bigcup_nX_n\) with \(X_n\) increasing and \(\sup_x\alpha^x(X_n)<\infty\), and
\(\gamma\alpha^x=\rho(\gamma)\alpha^y\) for \(\gamma:x\to y\). Its integral \(\int X\,d\Lambda\) (for \(\rho=\delta\))
satisfies: if \(X\) is proper, \(\int X\,d\Lambda=0\) iff the saturated set \(\{x:\alpha^x\neq0\}\) is
\(\Lambda\)-negligible.

**(R8) Proper homomorphisms** (Definitions 7.1 and 8.1, Corollary 7.5, Theorem 8.2). For a measurable homomorphism \(h:G\to G'\) and a \(G'\)-space \(X'\), the pull-back
\(h^*X'=\{(x,z'):\pi'(z')=h(x)\}\) is a \(G\)-space with \(\gamma(x,z')=(r(\gamma),h(\gamma)z')\). The homomorphism
\(h\) is *proper* if \(X_h=h^*G'=\{(x,\gamma'):r(\gamma')=h(x)\}\) is a proper \(G\)-space; equivalences (Definition 7.1(c)
there, recalled in Corollary 7.5(c) below) are proper. For \(\delta'\) a modulus on \(G'\) and \(\Lambda\) of modulus \(\delta'\circ h\), the
image \(h(\Lambda)\) is the transverse measure of modulus \(\delta'\) with \(h(\Lambda)(\nu')=\int h^*L^{\nu'}\,d
\Lambda\), where \(h^*L^{\nu'}\) is the random variable on \(X_h\) with measures \(\delta'^{-1}\nu'^{h(x)}\) placed on
\(\{x\}\times G'^{h(x)}\).

### 1.3 Two measure-theoretic lemmas

**Lemma 1.1 (measurability of fibre integrals).** Let \(X\) be a measurable space with a measurable map
\(\pi:X\to G^{(0)}\) and measures \(\beta^y\) carried by \(\pi^{-1}(y)\) such that \(y\mapsto\beta^y(E)\) is measurable
and \(X=\bigcup_nX_n\) with \(\sup_y\beta^y(X_n)<\infty\). Let \(p\) be \(r\) or \(s\), and let \(\Phi\ge0\) be
measurable on \(\{(\gamma,z)\in G\times X:p(\gamma)=\pi(z)\}\). Then \(\gamma\mapsto\int\Phi(\gamma,z)\,
d\beta^{p(\gamma)}(z)\) is measurable on \(G\).

*Proof.* The domain \(Y\) of \(\Phi\) is the preimage of the diagonal under \((p,\pi)\), hence measurable by (S). Fix
\(n\). The sets \(C\subset Y\), measurable, for which \(\gamma\mapsto\beta^{p(\gamma)}(\{z\in X_n:(\gamma,z)\in C\})\)
is measurable form a Dynkin system (the measures \(\beta^{p(\gamma)}(\,\cdot\cap X_n)\) are finite). It contains the
traces \((E\times F)\cap Y\), for which the function is \(1_E(\gamma)\beta^{p(\gamma)}(F\cap X_n)\), and these form a
\(\pi\)-system generating the trace \(\sigma\)-algebra. So it contains all measurable \(C\). Letting \(n\to\infty\) and
approximating \(\Phi\) by simple functions from below gives the claim by monotone convergence. \(\square\)

Applied with \(X=G\), \(\pi=r\) and \(\beta=\nu\) for a proper kernel \(\nu\), the lemma shows that integrals such as
\(\gamma\mapsto\int\phi(\gamma^{-1}\gamma')\psi(\gamma')\,d\nu^{r(\gamma)}(\gamma')\) are measurable.

Fix once and for all a countable algebra \(\mathcal C_0\) of subsets of \(G^{(0)}\) generating \(\mathcal B_0\), and a
countable algebra \(\mathcal C\) of subsets of \(G\) generating \(\mathcal B\) and containing \(r^{-1}(C)\) and
\(s^{-1}(C)\) for \(C\in\mathcal C_0\).

**Lemma 1.2 (symmetric exhaustions and total families).** Let \(\nu\in\mathcal E^+\) and let \(\delta\) be a modulus.

(a) There are measurable sets \(B_1\subset B_2\subset\cdots\) with \(\bigcup_nB_n=G\), \(B_n^{-1}=B_n\),
\(n^{-1}\le\delta\le n\) on \(B_n\), and \(\sup_y\nu^y(B_n)<\infty\) for each \(n\).

(b) Let \(w\) be a bounded measurable function on \(G\) with \(w>0\) everywhere, and let
\(\mathcal D=\{w\,1_{C\cap B_n}:C\in\mathcal C,\ n\ge1\}\). For every \(y\), \(\mathcal D\) is total in
\(L^1(G,\nu^y)\) and in \(L^2(G,\nu^y)\); in particular a function \(\phi\in L^\infty(G,\nu^y)\) with
\(\int\phi f\,d\nu^y=0\) for all \(f\in\mathcal D\) vanishes \(\nu^y\)-almost everywhere.

*Proof.* (a) Take \(A_n\) as in (R2) and put \(B_n=A_n\cap A_n^{-1}\cap\{n^{-1}\le\delta\le n\}\). These are
increasing and symmetric (\(\delta(\gamma^{-1})=\delta(\gamma)^{-1}\)), \(\nu^y(B_n)\le\nu^y(A_n)\), and every \(\gamma\)
lies in \(A_n\) and \(A_m^{-1}\) and satisfies \(n^{-1}\le\delta(\gamma)\le n\) for large \(n,m\).

(b) Let \(\phi\in L^2(G,\nu^y)\) (respectively \(L^\infty\)) with \(\int\bar\phi f\,d\nu^y=0\) for all
\(f\in\mathcal D\). For fixed \(n\), \(E\mapsto\int_{E\cap B_n}\bar\phi w\,d\nu^y\) is a finite complex measure on
\(\mathcal B\), because \(\nu^y(B_n)<\infty\) and \(w\) is bounded. It vanishes on the algebra \(\mathcal C\), so its
real and imaginary parts, which are differences of finite measures agreeing on \(\mathcal C\), vanish on
\(\sigma(\mathcal C)=\mathcal B\). Hence \(\bar\phi w=0\) almost everywhere on each \(B_n\), so \(\phi=0\)
\(\nu^y\)-almost everywhere. \(\square\)

## 2. Representations of a measurable groupoid

A reference for Sections 2 to 5 is [Connes 1979].

### 2.1 Definitions

A measurable field of Hilbert spaces over \(G^{(0)}\) is taken in the sense of (B1). A section \(\xi\) is *bounded* if
\(\|\xi\|_\infty=\sup_x\|\xi_x\|<\infty\).

**Definition 2.1.** A *representation* of \(G\) on a measurable field \(H=(H_x)_{x\in G^{(0)}}\) is a family of
unitary operators \(U(\gamma):H_x\to H_y\), one for each \(\gamma:x\to y\), such that

1. \(U(\gamma_1\gamma_2)=U(\gamma_1)U(\gamma_2)\) for \((\gamma_1,\gamma_2)\in G^{(2)}\), and \(U(x)=1\) for
   \(x\in G^{(0)}\);
2. for all measurable sections \(\xi,\eta\), the *coefficient*
   \[
   (\xi,\eta)(\gamma)=\big\langle\xi_{r(\gamma)},U(\gamma)\eta_{s(\gamma)}\big\rangle\qquad(\gamma\in G)
   \]
   is a measurable function on \(G\).

Condition 1 is equivalent to \(U(\gamma_1^{-1}\gamma_2)=U(\gamma_1)^{-1}U(\gamma_2)\) whenever \(r(\gamma_1)=
r(\gamma_2)\): take \(\gamma_1=\gamma_2\) to get \(U(s(\gamma))=1\), then \(\gamma_2=r(\gamma_1)\) to get
\(U(\gamma_1^{-1})=U(\gamma_1)^{-1}\), and then the general identity is multiplicativity. When \(G\) is a group this is a
unitary representation with measurable coefficients; when \(G=G^{(0)}\) is a space it is just a measurable field.

**Lemma 2.2.** Let \((U(\gamma))\) satisfy condition 1, and let \((\xi^n)\) be a fundamental sequence of \(H\). If
all \((\xi^n,\xi^m)\) are measurable, then \(U\) is a representation.

*Proof.* Let \((e^k)\) be the measurable orthonormal sections of (B1)(ii), with \(e^k=\sum_na_{kn}\xi^n\) as
there. Then \((e^k,e^l)(\gamma)=\sum_{n,m}a_{kn}(r(\gamma))\overline{a_{lm}(s(\gamma))}(\xi^n,\xi^m)(\gamma)\), a sum
of measurable functions with only finitely many nonzero terms at each \(\gamma\), so it is measurable. For measurable \(\xi,\eta\) and \(\gamma:x\to y\), expanding \(\eta_x=\sum_l\langle\eta_x,e^l_x\rangle
e^l_x\) and then \(\xi_y=\sum_k\langle\xi_y,e^k_y\rangle e^k_y\) (Parseval) gives the iterated series
\[
(\xi,\eta)(\gamma)=\sum_k\langle\xi_y,e^k_y\rangle\Big(\sum_l\overline{\langle\eta_x,e^l_x\rangle}\,
(e^k,e^l)(\gamma)\Big),
\]
where the inner series converges to \(\langle e^k_y,U(\gamma)\eta_x\rangle\) and the outer one to
\(\langle\xi_y,U(\gamma)\eta_x\rangle\), at every \(\gamma\). All terms are measurable functions of \(\gamma\) (the
coefficients are measurable functions of \(y=r(\gamma)\) and \(x=s(\gamma)\)), and pointwise limits of measurable
functions are measurable. \(\square\)

**Definition 2.3 (constructions).**

(a) *Direct sums.* For countably many representations \((H^i,U^i)\), \(\bigoplus_iH^i\) has fibres
\(\bigoplus_iH^i_x\), fundamental sequence the sections with a single nonzero component taken from a fundamental
sequence of some \(H^i\), and \(U=\bigoplus_iU^i\). We write \(\infty\cdot H=\bigoplus_1^\infty H\).

(b) *Tensor products.* For representations \((H,U)\), \((K,V)\), \(H\otimes K\) has fibres \(H_x\otimes K_x\),
fundamental sequence \((\xi^n\otimes\eta^m)\), and \((U\otimes V)(\gamma)=U(\gamma)\otimes V(\gamma)\). Its
coefficients \((\xi^n\otimes\eta^m,\xi^{n'}\otimes\eta^{m'})=(\xi^n,\xi^{n'})(\eta^m,\eta^{m'})\) are measurable.

(c) *Pull-backs.* For a measurable homomorphism \(h:G_1\to G\) and a representation \((H,U)\) of \(G\),
\(h^*H\) has fibres \((h^*H)_x=H_{h(x)}\), fundamental sequence \((\xi^n\circ h)\), and \((h^*U)(\gamma)=U(h(\gamma))\).
Its coefficients are \((\xi^n,\xi^m)\circ h\).

(d) *Trivial representations.* For a measurable function \(d:G^{(0)}\to\{0,1,\dots,\infty\}\) constant on orbits,
the field \(\mathbb C^{d}\) with fibres \(\mathbb C^{d(x)}\) (\(\mathbb C^\infty=\ell^2\)), the standard basis vectors as
fundamental sequence, and \(U(\gamma)\) the identity matrix, is the *trivial representation of dimension \(d\)*. For
\(d=1\) we write \(\mathbf 1\).

By Lemma 2.2 these are representations.

### 2.2 Integrated form and coefficients

Let \(\lambda\) be a kernel and \(f\) a complex measurable function on \(G\) with \(\lambda(|f|)\) bounded. For a
bounded measurable section \(\xi\) and \(\alpha\in H_y\), the function \(\gamma\mapsto\langle U(\gamma)
\xi_{s(\gamma)},\alpha\rangle\) on \(G^y\) is measurable (it is a limit of combinations of the functions
\(\overline{(\xi^n,\xi)}\) restricted to \(G^y\)) and bounded by \(\|\xi\|_\infty\|\alpha\|\). So there is a unique
vector \((U(f\lambda)\xi)_y\in H_y\) with
\[
\big\langle(U(f\lambda)\xi)_y,\alpha\big\rangle=\int f(\gamma)\big\langle U(\gamma)\xi_{s(\gamma)},\alpha\big\rangle
\,d\lambda^y(\gamma)\qquad(\alpha\in H_y), \tag{2.1}
\]
and \(\|(U(f\lambda)\xi)_y\|\le\lambda^y(|f|)\,\|\xi\|_\infty\). The section \(U(f\lambda)\xi\) is measurable, since
\(\langle(U(f\lambda)\xi)_y,\eta_y\rangle=\int f\,\overline{(\eta,\xi)}\,d\lambda^y\) is measurable in \(y\) by (R1).
We write \(\int f(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\lambda^y(\gamma)\) for this weak integral.

**Proposition 2.4.** Let \((H,U)\) be a representation.

(a) For bounded measurable sections \(\xi,\eta\) and \(\lambda(|f|)\) bounded,
\[
(\eta,\xi)=(\xi,\eta)^\flat,\qquad
\big(U(f\lambda)\xi,\eta\big)(\gamma)=\int f(\gamma')(\xi,\eta)(\gamma'^{-1}\gamma)\,d\lambda^{r(\gamma)}(\gamma'),
\]
\[
\big(\xi,U(f\lambda)\eta\big)(\gamma)=\int\overline{f(\gamma')}\,(\xi,\eta)(\gamma\gamma')\,d\lambda^{s(\gamma)}(\gamma').
\]

(b) (*Totality.*) Let \(\lambda\) be a proper kernel, \(D\) a countable set of measurable functions \(f\) with
\(\lambda(|f|)\) bounded that is total in \(L^1(G,\lambda^y)\) for every \(y\), and \(S\) a countable set of bounded
measurable sections. Fix \(y\). Suppose that for every \(\lambda^y\)-conull measurable \(E\subset G^y\) the vectors
\(U(\gamma)\xi_{s(\gamma)}\), \(\gamma\in E\), \(\xi\in S\), are total in \(H_y\). Then the vectors
\((U(f\lambda)\xi)_y\), \(f\in D\), \(\xi\in S\), are total in \(H_y\). The hypothesis holds for every \(y\) with
\(\lambda^y\neq0\) if \(S\) is total.

*Proof.* (a) \((\eta,\xi)(\gamma)=\langle U(\gamma)^{-1}\eta_y,\xi_x\rangle=\overline{\langle\xi_x,U(\gamma^{-1})
\eta_y\rangle}=\overline{(\xi,\eta)(\gamma^{-1})}\). Next, by (2.1),
\[
(U(f\lambda)\xi,\eta)(\gamma)=\int f(\gamma')\langle U(\gamma')\xi_{s(\gamma')},U(\gamma)\eta_{s(\gamma)}\rangle\,
d\lambda^{y}(\gamma')=\int f(\gamma')(\xi,\eta)(\gamma'^{-1}\gamma)\,d\lambda^y(\gamma'),
\]
using \(U(\gamma')^*U(\gamma)=U(\gamma'^{-1}\gamma)\). Similarly \(\langle\xi_y,U(\gamma)(U(f\lambda)\eta)_x\rangle=
\int\bar f(\gamma')\langle\xi_y,U(\gamma\gamma')\eta_{s(\gamma')}\rangle\,d\lambda^x(\gamma')\).

(b) Let \(\alpha\in H_y\) be orthogonal to all \((U(f\lambda)\xi)_y\). For \(\xi\in S\) the bounded function
\(\phi_\xi(\gamma)=\langle U(\gamma)\xi_{s(\gamma)},\alpha\rangle\) satisfies \(\int f\phi_\xi\,d\lambda^y=0\) for all
\(f\in D\), so \(\phi_\xi=0\) \(\lambda^y\)-almost everywhere. Hence \(E=\{\gamma\in G^y:\phi_\xi(\gamma)=0\ \forall
\xi\in S\}\) is conull, and \(\alpha\) is orthogonal to the total set \(\{U(\gamma)\xi_{s(\gamma)}:\gamma\in E,\xi\in
S\}\); so \(\alpha=0\). If \(S\) is total and \(\lambda^y\neq0\), a conull \(E\) contains some \(\gamma:x\to y\), and
\(U(\gamma)\) maps the total set \(\{\xi_x\}\) onto a total subset of \(H_y\). \(\square\)

Families \(D\) as in (b) exist for every proper kernel: take \(\mathcal D\) of Lemma 1.2(b), whose proof uses only
\(\sup_y\lambda^y(B_n)<\infty\), which holds for sets \(B_n\) built from the sets \(A_n\) of (R1).

### 2.3 Intertwiners

**Definition 2.5.** Let \((H,U)\), \((H',U')\) be representations. An *intertwiner* is a measurable field
\(T=(T_x)\) of bounded operators \(T_x:H_x\to H'_x\) with \(\|T\|=\sup_x\|T_x\|<\infty\) and
\[
U'(\gamma)T_x=T_yU(\gamma)\qquad(\gamma:x\to y).
\]
They form a Banach space \(\operatorname{Hom}_G(H,H')\), and \(\operatorname{End}_G(H)=\operatorname{Hom}_G(H,H)\).
The representations are *equivalent* if there is an intertwiner with every \(T_x\) unitary. A projection
\(P\in\operatorname{End}_G(H)\) defines the *subrepresentation* \(PH\) (fibres \(P_xH_x\), measurable sections the
measurable sections of \(H\) with values in \(PH\), and the restricted \(U\)); it is a representation by Lemma 2.2,
since the sections \(P\xi^n\) form a fundamental sequence. We write \(H\prec H'\) if \(H\) is equivalent to a
subrepresentation of \(H'\), that is, if there is an intertwiner \(V\) with every \(V_x\) isometric.

**Proposition 2.6.** Let \(H,H',H''\) be representations.

(a) If \(T_1\in\operatorname{Hom}_G(H,H')\) and \(T_2\in\operatorname{Hom}_G(H',H'')\), then \(T_2T_1=(T_{2,x}T_{1,x})
\in\operatorname{Hom}_G(H,H'')\), and \(T_1^*=(T_{1,x}^*)\in\operatorname{Hom}_G(H',H)\). So \(\operatorname{End}_G(H)\)
is a C\(^*\)-algebra.

(b) If \(T\in\operatorname{Hom}_G(H,H')\) and \(T_x=v_x|T_x|\) is the polar decomposition, then \(|T|=(|T_x|)\in
\operatorname{End}_G(H)\) and \(v=(v_x)\in\operatorname{Hom}_G(H,H')\).

(c) For \(T\in\operatorname{Hom}_G(H,H')\), \(\lambda(|f|)\) bounded and \(\xi\) bounded measurable,
\(T\,U(f\lambda)\xi=U'(f\lambda)\,T\xi\).

(d) Let \(E_x\subset H_x\) be closed subspaces with projections \(P_x\) such that \(U(\gamma)P_x=P_yU(\gamma)\). Then
\(P=(P_x)\) is measurable (so \(P\in\operatorname{End}_G(H)\)) iff there is a countable family of measurable sections
of \(H\) with values in \(E\) that is total in every \(E_x\).

(e) Let \(P_1,P_2\in\operatorname{End}_G(H)\) be projections. Then \(P_1\vee P_2=(P_{1,x}\vee P_{2,x})\) and
\(P_1\wedge P_2\) belong to \(\operatorname{End}_G(H)\), and the subrepresentations defined by \(P_1\vee P_2-P_1\) and
\(P_2-P_1\wedge P_2\) are equivalent.

*Proof.* (a) Measurability of products and adjoints is (B1)(iv), and the intertwining relations follow from
\(U(\gamma)^*=U(\gamma)^{-1}\): \(T_{1,y}^*U'(\gamma)=(U'(\gamma)^*T_{1,y})^*=(T_{1,x}U(\gamma)^{-1})^*=U(\gamma)
T_{1,x}^*\).

(b) \(|T|=(T^*T)^{1/2}\) is measurable by (B1)(iv), since \(\sup\|T_x\|<\infty\). For \(\varepsilon>0\) the field
\(T(\varepsilon+T^*T)^{-1/2}\) is measurable, and it converges strongly to \(v\) as \(\varepsilon\to0\): on
\(\ker|T_x|\) both vanish, and on the range of \(|T_x|\), \(T_x(\varepsilon+T_x^*T_x)^{-1/2}|T_x|\zeta=
v_x|T_x|^2(\varepsilon+|T_x|^2)^{-1/2}\zeta\to v_x|T_x|\zeta\). So \(v\) is measurable. Since
\(T_y=U'(\gamma)T_xU(\gamma)^{-1}\), \(T_y^*T_y=U(\gamma)T_x^*T_xU(\gamma)^{-1}\), hence \(|T_y|=U(\gamma)|T_x|
U(\gamma)^{-1}\); and \(U'(\gamma)v_xU(\gamma)^{-1}\) is a partial isometry with initial space
\(U(\gamma)\overline{\operatorname{ran}}|T_x|=\overline{\operatorname{ran}}|T_y|\) whose product with \(|T_y|\) is
\(T_y\). By uniqueness of the polar decomposition it equals \(v_y\).

(c) By (2.1), \(\langle T_y(U(f\lambda)\xi)_y,\alpha\rangle=\int f(\gamma)\langle T_yU(\gamma)\xi_{s(\gamma)},\alpha
\rangle\,d\lambda^y=\int f(\gamma)\langle U'(\gamma)T_{s(\gamma)}\xi_{s(\gamma)},\alpha\rangle\,d\lambda^y\).

(d) If \(P\) is measurable, the sections \(P\xi^n\) are measurable, have values in \(E\), and are total in each
\(E_x\). Conversely, given such a family, apply Gram–Schmidt (B1)(ii) to it inside \(H\): this gives measurable
sections \(e^k\) with values in \(E\) such that the nonzero \(e^k_x\) form an orthonormal basis of \(E_x\). Then
\(P_x\zeta=\sum_k\langle\zeta,e^k_x\rangle e^k_x\), and \(\langle P_x\xi^n_x,\xi^m_x\rangle=\sum_k\langle\xi^n_x,
e^k_x\rangle\langle e^k_x,\xi^m_x\rangle\) is measurable.

(e) \(P_1\vee P_2\) is the support projection of \(P_1+P_2\), the strong limit of \((P_1+P_2)^{1/j}\), and
\(P_1\wedge P_2=1-(1-P_1)\vee(1-P_2)\); both are measurable by (B1)(iv) and intertwine because conjugation by the
unitaries \(U(\gamma)\) respects these operations. Let \(v\) be the partial isometry in the polar decomposition of
\(T=(1-P_1)P_2\), which lies in \(\operatorname{End}_G(H)\) by (b). Fibrewise, the initial projection of \(v_x\) is
the projection onto \((\ker T_x)^\perp\); here \(\ker T_x=(1-P_{2,x})H_x\oplus(P_{1,x}\wedge P_{2,x})H_x\), so the
initial projection is \(P_{2,x}-P_{1,x}\wedge P_{2,x}\). The final projection is onto
\(\overline{\operatorname{ran}}\,T_x=(\ker T_x^*)^\perp\), with \(\ker T_x^*=\ker P_{2,x}(1-P_{1,x})=
P_{1,x}H_x\oplus((1-P_{1,x})\wedge(1-P_{2,x}))H_x\); so the final projection is \(1-P_{1,x}-(1-P_{1,x})\wedge(1-P_{2,x})
=1-P_{1,x}-\big(1-(P_{1,x}\vee P_{2,x})\big)=P_{1,x}\vee P_{2,x}-P_{1,x}\). Thus \(v\) restricts to a unitary intertwiner between the two
subrepresentations. \(\square\)

Part (e) is the parallelogram law of Kaplansky, done measurably.

### 2.4 The subrepresentation generated by a section

For a bounded measurable section \(\xi\), let \(P^\xi_y\) be the projection onto the closed span of
\(\{U(\gamma)\xi_{s(\gamma)}:\gamma\in G^y\}\). In general \(P^\xi\) need not be measurable. Averaging against a
transverse function repairs this.

For \(\nu\in\mathcal E^+\) and \(y\in G^{(0)}\) put
\[
N^{\nu,\xi}_y=\{\alpha\in H_y:\ \langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle=0\ \text{for }\nu^y\text{-almost every }
\gamma\},
\]
a closed subspace, and let \(P^{\nu,\xi}_y\) be the projection onto \((N^{\nu,\xi}_y)^\perp\).

**Proposition 2.7.** Let \((H,U)\) be a representation, \(\xi\) a bounded measurable section and \(\nu\in\mathcal E^+\).

(a) \(P^{\nu,\xi}\in\operatorname{End}_G(H)\), and the range of \(P^{\nu,\xi}_y\) is the closed span of the vectors
\((U(f\nu)\xi)_y\), \(\nu(|f|)\) bounded.

(b) Put \(\xi'=P^{\nu,\xi}\xi\). For every \(y\), \(\xi_{s(\gamma)}=\xi'_{s(\gamma)}\) for \(\nu^y\)-almost every
\(\gamma\), and \(P^{\nu,\xi}=P^{\nu,\xi'}=P^{\xi'}\). In particular \(P^{\xi'}\) is measurable.

(c) For \(B\in\operatorname{Hom}_G(H,H')\), \(N^{\nu,B\xi}_y=\{\alpha:B_y^*\alpha\in N^{\nu,\xi}_y\}\). If \(B\) is a
projection in \(\operatorname{End}_G(H)\) with \(B\le P^{\nu,\xi}\), then \(P^{\nu,B\xi}=B\).

(d) Let \((\xi^n)\) be a total sequence of bounded measurable sections and \(\nu\) faithful. There are
\(A_n\in\operatorname{End}_G(H)\) such that, with \(\eta^n=A_n\xi^n\), each \(P^{\eta^n}\) is measurable, the
\(P^{\eta^n}\) are pairwise orthogonal, and \(\sum_nP^{\eta^n}=1\).

*Proof.* (a) Let \(D\) be as in Proposition 2.4(b) for \(\lambda=\nu\). The argument there shows: if \(\alpha\perp
(U(f\nu)\xi)_y\) for all \(f\in D\), then \(\alpha\in N^{\nu,\xi}_y\); and conversely \(\alpha\in N^{\nu,\xi}_y\) is
orthogonal to every \((U(f\nu)\xi)_y\) by (2.1). So the countable family \(U(f\nu)\xi\), \(f\in D\), is total in the
range of \(P^{\nu,\xi}\), and its closed span contains all \((U(f\nu)\xi)_y\). Intertwining: for \(\gamma:x\to y\) and
\(\alpha\in H_x\), since \(\nu^y=\gamma\nu^x\),
\[
\langle U(\gamma)\alpha,U(\gamma'')\xi_{s(\gamma'')}\rangle=0\ \text{for }\nu^y\text{-a.e. }\gamma''\iff
\langle U(\gamma)\alpha,U(\gamma\gamma')\xi_{s(\gamma')}\rangle=0\ \text{for }\nu^x\text{-a.e. }\gamma',
\]
and the right side says \(\alpha\in N^{\nu,\xi}_x\). So \(U(\gamma)N^{\nu,\xi}_x=N^{\nu,\xi}_y\), and
\(P^{\nu,\xi}\) is measurable by Proposition 2.6(d).

(b) Fix \(y\) and an orthonormal basis \((\beta_j)\) of \(N^{\nu,\xi}_y\). For \(\nu^y\)-almost every \(\gamma:x\to
y\), \(\langle\beta_j,U(\gamma)\xi_x\rangle=0\) for all \(j\), that is \((1-P^{\nu,\xi}_y)U(\gamma)\xi_x=0\); since
\(P^{\nu,\xi}\) intertwines, \(U(\gamma)(1-P^{\nu,\xi}_x)\xi_x=0\), so \(\xi_x=\xi'_x\). Hence the functions
\(\gamma\mapsto\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle\) and \(\gamma\mapsto\langle\alpha,U(\gamma)
\xi'_{s(\gamma)}\rangle\) agree \(\nu^y\)-almost everywhere, and \(N^{\nu,\xi'}=N^{\nu,\xi}\). Every
\(U(\gamma)\xi'_x=P^{\nu,\xi}_yU(\gamma)\xi_x\) lies in the range of \(P^{\nu,\xi}_y\), so \(P^{\xi'}\le P^{\nu,\xi}\);
and \(N^{\nu,\xi'}_y\supset(\operatorname{ran}P^{\xi'}_y)^\perp\), so \(P^{\nu,\xi'}\le P^{\xi'}\). Hence
\(P^{\nu,\xi}=P^{\nu,\xi'}=P^{\xi'}\).

(c) \(\langle\alpha,U'(\gamma)B_x\xi_x\rangle=\langle\alpha,B_yU(\gamma)\xi_x\rangle=\langle B_y^*\alpha,U(\gamma)\xi_x
\rangle\) gives the first claim. If \(B\) is a projection with \(B\le P^{\nu,\xi}\), then \(B_y\alpha\) lies in the
range of \(P^{\nu,\xi}_y\), which meets \(N^{\nu,\xi}_y\) only in \(0\); so \(\alpha\in N^{\nu,B\xi}_y\) iff
\(B_y\alpha=0\), and \(P^{\nu,B\xi}=B\).

(d) Put \(Q_n=P^{\nu,\xi^n}\). By Proposition 2.4(b) (with \(S=\{\xi^n\}\)) and (a), \(\bigvee_nQ_{n,x}=1\) for every
\(x\). Let \(Q'_n=Q_1\vee\cdots\vee Q_n\) (\(Q'_0=0\)) and \(P_n=Q'_n-Q'_{n-1}=(Q'_{n-1}\vee Q_n)-Q'_{n-1}\); these are
orthogonal projections in \(\operatorname{End}_G(H)\) with sum \(1\). By Proposition 2.6(e) there is a partial
isometry \(v_n\in\operatorname{End}_G(H)\) with \(v_n^*v_n=P'_n=Q_n-Q_n\wedge Q'_{n-1}\) and \(v_nv_n^*=P_n\). Put
\(A_n=v_nP'_n\) and \(\eta^n=A_n\xi^n\). Since \(P'_n\le Q_n\), (c) gives \(P^{\nu,P'_n\xi^n}=P'_n\), and then by the
first part of (c), \(N^{\nu,\eta^n}_y=\{\alpha:v_{n,y}^*\alpha\in\ker P'_{n,y}\}=\ker v_{n,y}^*\), so
\(P^{\nu,\eta^n}=v_nv_n^*=P_n\). Since \(\eta^n=P_n\eta^n\), (b) gives \(P^{\eta^n}=P^{\nu,\eta^n}=P_n\). \(\square\)

## 3. Regular representations and convolution operators

### 3.1 The left regular representation of a transverse function

Let \(\nu\in\mathcal E^+\). For \(y\in G^{(0)}\) let \(L^2(G,\nu^y)\) be the Hilbert space of classes of square
integrable functions for \(\nu^y\); since \(\nu^y\) is carried by the measurable set \(G^y\), these are functions on
\(G^y\). Choose sets \(B_n\) as in Lemma 1.2(a). The functions \(1_{C\cap B_n}\) (\(C\in\mathcal C\), \(n\ge1\)) are
total in every \(L^2(G,\nu^y)\) (Lemma 1.2(b)), and their inner products \(\nu^y(C\cap C'\cap B_n\cap B_m)\) are
measurable in \(y\). By (B1) they are a fundamental sequence of a measurable field
\[
L^2(G,\nu)=\big(L^2(G,\nu^y)\big)_{y\in G^{(0)}}.
\]
If \(g\) is a measurable function on \(G\) with \(\nu^y(|g|^2)<\infty\) for all \(y\), then \(y\mapsto g|_{G^y}\) is a
measurable section, because \(\int_{C\cap B_n}g\,d\nu^y\) is measurable in \(y\) (R1). For \(\gamma:x\to y\) define
\[
(L^\nu(\gamma)g)(\gamma')=g(\gamma^{-1}\gamma')\qquad(\gamma'\in G^y,\ g\in L^2(G,\nu^x)).
\]
Since \(\gamma\nu^x=\nu^y\), \(L^\nu(\gamma)\) is a unitary from \(L^2(G,\nu^x)\) onto \(L^2(G,\nu^y)\), and
\(L^\nu(\gamma_1\gamma_2)=L^\nu(\gamma_1)L^\nu(\gamma_2)\). The coefficient of two fundamental sections,
\[
(1_E,1_{E'})(\gamma)=\int1_E(\gamma')1_{E'}(\gamma^{-1}\gamma')\,d\nu^{r(\gamma)}(\gamma'),
\]
is measurable by Lemma 1.1. By Lemma 2.2, \(L^\nu\) is a representation: the *left regular representation* of \(\nu\).
We write \(\mathcal L^2_b(\nu)\) for the set of measurable functions \(g\) on \(G\) with
\(\sup_y\nu^y(|g|^2)<\infty\); they define bounded measurable sections. For functions \(f,g\) on \(G\) put
\[
(f*_\nu g)(\gamma)=\int f(\gamma')\,g(\gamma'^{-1}\gamma)\,d\nu^{r(\gamma)}(\gamma') \tag{3.1}
\]
wherever the integral converges absolutely.

**Proposition 3.1.** Let \(\nu\in\mathcal E^+\).

(a) Every measurable section \(\zeta\) of \(L^2(G,\nu)\) is given by a measurable function: there is a measurable
\(g\) on \(G\) with \(\zeta_y=g|_{G^y}\) in \(L^2(G,\nu^y)\) for every \(y\).

(b) If \(g\in\mathcal L^2_b(\nu)\), \(\lambda\) is a kernel and \(\lambda(|f|)\) is bounded, then for every \(y\)
\[
(L^\nu(f\lambda)g)_y(\gamma)=\int f(\gamma')\,g(\gamma'^{-1}\gamma)\,d\lambda^{y}(\gamma')\qquad\text{for }
\nu^y\text{-a.e. }\gamma;
\]
in particular \(L^\nu(f\nu)g=f*_\nu g\).

(c) For \(g_1,g_2\in\mathcal L^2_b(\nu)\), the coefficient is \((g_1,g_2)=g_1*_\nu g_2^\flat\).

*Proof.* (a) Enumerate \(\mathcal C=\{C_1,C_2,\dots\}\), let \(\mathcal C_n\) be the finite algebra generated by
\(C_1,\dots,C_n\), and put \(D_k=B_k\setminus B_{k-1}\) (\(B_0=\emptyset\)). For \(\gamma\in D_k\) with \(r(\gamma)=y\), let
\(b\) be the atom of \(\mathcal C_n\) containing \(\gamma\), and put
\[
g_n(\gamma)=\frac{\langle\zeta_y,1_{b\cap D_k}\rangle}{\nu^y(b\cap D_k)}\quad\text{if }\nu^y(b\cap D_k)>0,\qquad
g_n(\gamma)=0\ \text{otherwise}.
\]
The function \(1_{b\cap D_k}\) is a finite combination of fundamental sections, so numerator and denominator are
measurable functions of \(y=r(\gamma)\) on each of the finitely many sets \(b\cap D_k\); hence \(g_n\) is measurable. For
fixed \(y\) and \(k\), on \(D_k\) with the finite measure \(\nu^y|_{D_k}\), \(g_n\) is the conditional expectation of
\(\zeta_y\) given the finite \(\sigma\)-algebra generated by the traces of the atoms of \(\mathcal C_n\). These
\(\sigma\)-algebras increase and generate the trace of \(\mathcal B\) on \(D_k\), and \(\zeta_y\in L^2\subset L^1\) there.
By (B5), \(g_n\to\zeta_y\) \(\nu^y\)-almost everywhere on \(D_k\). Let \(g=\lim g_n\) where the limit exists (a
measurable set) and \(g=0\) elsewhere.

(b) For \(\alpha\in L^2(G,\nu^y)\),
\(\iint|f(\gamma')||g(\gamma'^{-1}\gamma)||\alpha(\gamma)|\,d\nu^y(\gamma)\,d\lambda^y(\gamma')\le\int|f(\gamma')|\,
\|g|_{G^{s(\gamma')}}\|\,\|\alpha\|\,d\lambda^y(\gamma')<\infty\), using \(\|L^\nu(\gamma')g_{s(\gamma')}\|=\|g_{s(\gamma')}\|\).
So Fubini's theorem applies to \(\langle(L^\nu(f\lambda)g)_y,\alpha\rangle=\int f(\gamma')\langle L^\nu(\gamma')
g_{s(\gamma')},\alpha\rangle\,d\lambda^y(\gamma')\) and gives the formula.

(c) \((g_1,g_2)(\gamma)=\langle g_1|_{G^y},L^\nu(\gamma)g_2|_{G^x}\rangle=\int g_1(\gamma')\overline{g_2(\gamma^{-1}
\gamma')}\,d\nu^y(\gamma')=(g_1*_\nu g_2^\flat)(\gamma)\). \(\square\)

### 3.2 Convolution operators between regular representations

**Definition 3.2.** For \(\nu,\nu'\in\mathcal E^+\) and a measurable function \(f\) on \(G\) put
\[
\|f\|_{\nu',\nu}=\max\Big(\sup_y\nu^y(|f|),\ \sup_y\nu'^y(|\tilde f|)\Big)\in[0,\infty].
\]
We write \(\|f\|_\nu=\|f\|_{\nu,\nu}\).

**Proposition 3.3.** Let \(\nu,\nu',\nu''\in\mathcal E^+\) and \(\|f\|_{\nu',\nu}<\infty\).

(a) For each \(y\) the formula
\[
(R_{\nu',\nu}(f)_yq)(\gamma_1)=\int f(\gamma_1^{-1}\gamma_2)\,q(\gamma_2)\,d\nu^y(\gamma_2)\qquad(q\in L^2(G,\nu^y))
\]
defines a bounded operator \(L^2(G,\nu^y)\to L^2(G,\nu'^y)\) of norm at most \(\|f\|_{\nu',\nu}\), the integral
converging absolutely for \(\nu'^y\)-almost every \(\gamma_1\). In terms of (3.1), \(R_{\nu',\nu}(f)q=q*_\nu\tilde f\).

(b) \(R_{\nu',\nu}(f)=(R_{\nu',\nu}(f)_y)\in\operatorname{Hom}_G(L^\nu,L^{\nu'})\).

(c) \(\|f^\flat\|_{\nu,\nu'}=\|f\|_{\nu',\nu}\) and \(R_{\nu',\nu}(f)^*=R_{\nu,\nu'}(f^\flat)\). If
\(\|k\|_{\nu'',\nu'}<\infty\), then \(\|k*_{\nu'}f\|_{\nu'',\nu}\le\|k\|_{\nu'',\nu'}\|f\|_{\nu',\nu}\) and
\[
R_{\nu'',\nu'}(k)\,R_{\nu',\nu}(f)=R_{\nu'',\nu}(k*_{\nu'}f).
\]

(d) Fix \(y\). Let \(f_n\) be measurable with \(|f_n|\le h\), \(\|h\|_\nu<\infty\), and \(f_n(\gamma_1^{-1}\gamma_2)\to
f(\gamma_1^{-1}\gamma_2)\) for \(\nu^y\otimes\nu^y\)-almost every \((\gamma_1,\gamma_2)\). Then \(R_{\nu,\nu}(f_n)_y\to
R_{\nu,\nu}(f)_y\) weakly.

*Proof.* (a) This is the Schur test. Put \(K(\gamma_1,\gamma_2)=|f(\gamma_1^{-1}\gamma_2)|\) on \(G^y\times G^y\). By
left invariance (\(\gamma_1^{-1}\nu^y=\nu^{s(\gamma_1)}\)),
\[
\int K(\gamma_1,\gamma_2)\,d\nu^y(\gamma_2)=\nu^{s(\gamma_1)}(|f|)\le C_1,\qquad
\int K(\gamma_1,\gamma_2)\,d\nu'^y(\gamma_1)=\nu'^{s(\gamma_2)}(|\tilde f|)\le C_2,
\]
with \(C_1=\sup\nu(|f|)\), \(C_2=\sup\nu'(|\tilde f|)\). By Cauchy–Schwarz, \(\big(\int K|q|\,d\nu^y(\gamma_2)\big)^2\le
C_1\int K|q|^2\,d\nu^y(\gamma_2)\), and integrating in \(\gamma_1\) against \(\nu'^y\) gives
\(\int\big(\int K|q|\,d\nu^y\big)^2d\nu'^y\le C_1C_2\|q\|^2\). So the integral converges absolutely almost everywhere and
\(\|R_{\nu',\nu}(f)_yq\|\le(C_1C_2)^{1/2}\|q\|\).

(b) For \(\gamma:x\to y\) and \(q\in L^2(G,\nu^x)\), substituting \(\gamma_2=\gamma\gamma_3\) (\(\nu^y=\gamma\nu^x\)),
\[
(R_yL^\nu(\gamma)q)(\gamma_1)=\int f(\gamma_1^{-1}\gamma\gamma_3)q(\gamma_3)\,d\nu^x(\gamma_3)=(R_xq)(\gamma^{-1}\gamma_1)
=(L^{\nu'}(\gamma)R_xq)(\gamma_1).
\]
Measurability: for fundamental sections \(1_E\), \(1_{E'}\) of finite measure, \(\langle R_y1_E,1_{E'}\rangle=\iint
f(\gamma_1^{-1}\gamma_2)1_E(\gamma_2)1_{E'}(\gamma_1)\,d\nu^y(\gamma_2)\,d\nu'^y(\gamma_1)\) is measurable in \(y\) by
Lemma 1.1 (applied to the positive and negative parts of the real and imaginary parts of \(f\)), and (B1)(iv) applies.

(c) The first identity is \(\nu'(|f^\flat|)=\nu'(|\tilde f|)\) and \(\nu(|\widetilde{f^\flat}|)=\nu(|f|)\). The adjoint of
an integral operator with kernel \(f(\gamma_1^{-1}\gamma_2)\) has kernel \(\overline{f(\gamma_2^{-1}\gamma_1)}=
f^\flat(\gamma_1^{-1}\gamma_2)\), with the roles of \(\nu\) and \(\nu'\) exchanged. For the product, by absolute
convergence (part (a) applied to \(|k|\) and \(|f|\)) and Fubini,
\[
(R(k)R(f)q)(\gamma_0)=\int q(\gamma_2)\Big(\int k(\gamma_0^{-1}\gamma_1)f(\gamma_1^{-1}\gamma_2)\,d\nu'^y(\gamma_1)\Big)
d\nu^y(\gamma_2),
\]
and the substitution \(\gamma_1=\gamma_0\beta\), \(\beta\in G^{s(\gamma_0)}\), turns the inner integral into
\((k*_{\nu'}f)(\gamma_0^{-1}\gamma_2)\). For the norm, left invariance gives
\[
\nu^x(|k*_{\nu'}f|)\le\iint|k(\beta)||f(\beta^{-1}\gamma)|\,d\nu'^x(\beta)\,d\nu^x(\gamma)=\int|k(\beta)|\,
\nu^{s(\beta)}(|f|)\,d\nu'^x(\beta)\le\sup\nu'(|k|)\,\sup\nu(|f|).
\]
The same substitution shows \(\widetilde{k*_{\nu'}f}=\tilde f*_{\nu'}\tilde k\), whence
\(\nu''(|\widetilde{k*_{\nu'}f}|)\le\sup\nu'(|\tilde f|)\sup\nu''(|\tilde k|)\).

(d) For \(q,p\in L^2(G,\nu^y)\), \(\langle R(f_n)q,p\rangle=\iint f_n(\gamma_1^{-1}\gamma_2)q(\gamma_2)
\overline{p(\gamma_1)}\), and \(h(\gamma_1^{-1}\gamma_2)|q(\gamma_2)||p(\gamma_1)|\) is integrable by (a). Dominated
convergence applies. \(\square\)

### 3.3 Absorption

**Proposition 3.4.** Let \(\nu\in\mathcal E^+\), let \((K,V)\) be any representation and \(d(x)=\dim K_x\) (constant
on orbits). Then \(L^\nu\otimes K\) is equivalent to \(L^\nu\otimes\mathbb C^d\). Consequently
\(L^\nu\otimes K\prec\infty\cdot L^\nu\), and \(L^\nu\prec L^\nu\otimes K\) if \(K_x\neq0\) for all \(x\).

*Proof.* Let \((e^k)\) be the measurable orthonormal sections of \(K\) given by (B1)(ii), and \((\varepsilon_k)\) the
standard basis of \(\mathbb C^{d(y)}\). Identify \(L^2(G,\nu^y)\otimes K_y\) with the space of \(K_y\)-valued square
integrable functions on \((G^y,\nu^y)\), and \(L^2(G,\nu^y)\otimes\mathbb C^{d(y)}\) likewise. For \(\gamma\in G^y\) the
operator \(K_y\to\mathbb C^{d(y)}\), \(\beta\mapsto\sum_k\langle V(\gamma)^{-1}\beta,e^k_{s(\gamma)}\rangle\varepsilon_k\),
is unitary (note \(d(s(\gamma))=d(y)\)). So
\[
(W_yF)(\gamma)=\sum_k\big\langle V(\gamma)^{-1}F(\gamma),e^k_{s(\gamma)}\big\rangle\,\varepsilon_k
\]
is a unitary \(L^2(G,\nu^y)\otimes K_y\to L^2(G,\nu^y)\otimes\mathbb C^{d(y)}\). For \(\gamma_0:x\to y\),
\((L^\nu\otimes V)(\gamma_0)F=\big(\gamma\mapsto V(\gamma_0)F(\gamma_0^{-1}\gamma)\big)\), and
\[
\big\langle V(\gamma)^{-1}V(\gamma_0)F(\gamma_0^{-1}\gamma),e^k_{s(\gamma)}\big\rangle
=\big\langle V(\gamma_0^{-1}\gamma)^{-1}F(\gamma_0^{-1}\gamma),e^k_{s(\gamma_0^{-1}\gamma)}\big\rangle,
\]
so \(W_y(L^\nu\otimes V)(\gamma_0)=(L^\nu\otimes1)(\gamma_0)W_x\). Measurability: for a fundamental function \(g\) and a
fundamental section \(\eta^m\) of \(K\), \(W(g\otimes\eta^m)(\gamma)=g(\gamma)\sum_k(\eta^m,e^k)(\gamma)\varepsilon_k\),
whose inner product with \(g'\otimes\varepsilon_k\) is \(\int g\,\overline{g'}\,(\eta^m,e^k)\,d\nu^y\), measurable in
\(y\); (B1)(iv) applies. Finally \(L^\nu\otimes\mathbb C^d\) is the subrepresentation of
\(L^\nu\otimes\ell^2=\infty\cdot L^\nu\) given by the projections \(1\otimes Q_x\), \(Q_x\) the projection onto
\(\mathbb C^{d(x)}\subset\ell^2\); and if \(d\ge1\), \(g\mapsto g\otimes\varepsilon_1\) embeds \(L^\nu\) into
\(L^\nu\otimes\mathbb C^d\). \(\square\)

## 4. Square-integrable representations

### 4.1 Vectors with square integrable coefficients

**Definition 4.1.** Let \((H,U)\) be a representation and \(\nu\in\mathcal E^+\). Let \(D(U,\nu)\) be the space of
bounded measurable sections \(\xi\) of \(H\) for which there is \(c\ge0\) with
\[
\int\big|\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle\big|^2\,d\nu^y(\gamma)\le c^2\|\alpha\|^2\qquad
(y\in G^{(0)},\ \alpha\in H_y). \tag{4.1}
\]
For \(\xi\in D(U,\nu)\) let \(T_\nu(\xi)_y:H_y\to L^2(G,\nu^y)\), \(T_\nu(\xi)_y\alpha=\big(\gamma\mapsto
\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle\big)\). For \(\xi,\eta\in D(U,\nu)\) put
\[
\theta_\nu(\xi,\eta)=T_\nu(\xi)^*\,T_\nu(\eta).
\]

For a bounded measurable section \(\eta\), \(T_\nu(\xi)\eta\) is the coefficient \((\eta,\xi)\), a measurable function
on \(G\) in \(\mathcal L^2_b(\nu)\).

**Proposition 4.2.** Let \((H,U)\), \((H',U')\) be representations and \(\nu,\nu'\in\mathcal E^+\).

(a) For \(\xi\in D(U,\nu)\), \(T_\nu(\xi)\in\operatorname{Hom}_G(H,L^\nu)\), with \(\|T_\nu(\xi)\|\le c\).

(b) For \(\xi\in D(U,\nu)\), \(y\in G^{(0)}\) and \(g\in L^1\cap L^2(G,\nu^y)\),
\(T_\nu(\xi)_y^*g=\int g(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y(\gamma)\) (a weak integral). In particular
\(T_\nu(\xi)^*g=U(g\nu)\xi\) for \(g\in\mathcal L^2_b(\nu)\) with \(\nu(|g|)\) bounded.

(c) For \(A\in\operatorname{Hom}_G(H,H')\) and \(\xi\in D(U,\nu)\): \(A\xi\in D(U',\nu)\) and \(T_\nu(A\xi)=T_\nu(\xi)A^*\).

(d) Let \(\xi\) be a bounded measurable section and \(\varphi=(\xi,\xi)\). If \(\sup\nu(|\varphi|)\) and
\(\sup\nu'(|\varphi|)\) are finite, then \(\xi\in D(U,\nu)\cap D(U,\nu')\), (4.1) holds with
\(c^2=\sup\nu(|\varphi|)\), and \(T_{\nu'}(\xi)T_\nu(\xi)^*=R_{\nu',\nu}(\tilde\varphi)\); here
\(\|\tilde\varphi\|_{\nu',\nu}=\max(\sup\nu(|\varphi|),\sup\nu'(|\varphi|))\).

(e) If \(\xi\in D(U,\nu)\) and \(\|f\|_{\nu',\nu}<\infty\), then \(U(f\nu)\xi\in D(U,\nu')\) and
\(T_{\nu'}(U(f\nu)\xi)=R_{\nu',\nu}(\bar f)\,T_\nu(\xi)\).

(f) For \(\xi,\eta\in D(U,\nu)\), \(\theta_\nu(\xi,\eta)\in\operatorname{End}_G(H)\), and for \(\alpha,\beta\in H_y\)
\[
\langle\theta_\nu(\xi,\eta)_y\alpha,\beta\rangle=\int\langle\alpha,U(\gamma)\eta_{s(\gamma)}\rangle\,
\langle U(\gamma)\xi_{s(\gamma)},\beta\rangle\,d\nu^y(\gamma), \tag{4.2}
\]
that is, \(\theta_\nu(\xi,\eta)_y=\int(U(\gamma)\xi_{s(\gamma)})(U(\gamma)\eta_{s(\gamma)})^*\,d\nu^y(\gamma)\) weakly.
Moreover \(\theta_\nu(\xi,\eta)^*=\theta_\nu(\eta,\xi)\), \(\theta_\nu(\xi,\xi)\ge0\),
\[
\theta_\nu(A\xi,B\eta)=A\,\theta_\nu(\xi,\eta)\,B^*\quad(A,B\in\operatorname{Hom}_G(H,H')),\qquad
\theta_\nu(\xi,\eta)\theta_\nu(\xi',\eta')=\theta_\nu\big(\theta_\nu(\xi,\eta)\xi',\eta'\big), \tag{4.3}
\]
and for bounded measurable \(\xi',\eta'\) the coefficient is \((\theta_\nu(\xi,\eta)\xi',\eta')=(\xi',\eta)*_\nu
(\eta',\xi)^\flat\).

*Proof.* (a) By (4.1), \(\|T_\nu(\xi)_y\|\le c\). For bounded measurable \(\eta\), \(T_\nu(\xi)\eta=(\eta,\xi)\) is a
measurable function with \(\nu^y(|(\eta,\xi)|^2)\le c^2\|\eta\|_\infty^2\), hence a measurable section of
\(L^2(G,\nu)\); applying this to a fundamental sequence of bounded sections, (B1)(iv) gives measurability. For
\(\gamma:x\to y\), \(\alpha\in H_x\) and \(\gamma'\in G^y\),
\[
(T_\nu(\xi)_yU(\gamma)\alpha)(\gamma')=\langle\alpha,U(\gamma^{-1}\gamma')\xi_{s(\gamma')}\rangle=
(T_\nu(\xi)_x\alpha)(\gamma^{-1}\gamma')=(L^\nu(\gamma)T_\nu(\xi)_x\alpha)(\gamma').
\]
(b) For \(\alpha\in H_y\), \(\langle T_\nu(\xi)_y\alpha,g\rangle=\int\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle
\overline{g(\gamma)}\,d\nu^y=\big\langle\alpha,\int g(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y\big\rangle\).

(c) \(\langle\alpha',U'(\gamma)A_x\xi_x\rangle=\langle A_y^*\alpha',U(\gamma)\xi_x\rangle\), so
\(T_\nu(A\xi)_y=T_\nu(\xi)_yA_y^*\) and (4.1) holds with \(c\|A\|\).

(d) Fix \(y\), \(\alpha\in H_y\), put \(F(\gamma)=\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle\) on \(G^y\), and let
\(E\subset G^y\) be measurable with \(\nu^y(E)<\infty\). The function \(g=1_EF\) is bounded and in \(L^1\cap L^2\). Let
\(w=\int g(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y(\gamma)\). Then \(\langle\alpha,w\rangle=\int\bar gF\,d\nu^y=
\int_E|F|^2\,d\nu^y\), and, since \(\langle U(\gamma_2)\xi_{s(\gamma_2)},U(\gamma_1)\xi_{s(\gamma_1)}\rangle=
\varphi(\gamma_2^{-1}\gamma_1)\),
\[
\|w\|^2=\iint g(\gamma_2)\overline{g(\gamma_1)}\,\varphi(\gamma_2^{-1}\gamma_1)\,d\nu^y(\gamma_2)\,d\nu^y(\gamma_1)
\le\iint|g(\gamma_1)||g(\gamma_2)|\,|\varphi(\gamma_1^{-1}\gamma_2)|\le C\|g\|^2,
\]
where \(C=\sup\nu(|\varphi|)\), by the Schur test of Proposition 3.3(a) for the kernel \(|\varphi|\) (note
\(|\varphi(\gamma^{-1})|=|\varphi(\gamma)|\) by Proposition 2.4(a), so both Schur constants equal \(C\)). Hence
\(\|g\|^2=\langle\alpha,w\rangle\le\|\alpha\|C^{1/2}\|g\|\), so \(\int_E|F|^2\le C\|\alpha\|^2\); letting \(E\uparrow
G^y\) gives (4.1) with \(c^2=C\). The same holds for \(\nu'\). For \(g\in L^1\cap L^2(G,\nu^y)\), by (b),
\[
\big(T_{\nu'}(\xi)T_\nu(\xi)^*g\big)(\gamma_1)=\Big\langle\int g(\gamma_2)U(\gamma_2)\xi_{s(\gamma_2)}\,d\nu^y,
U(\gamma_1)\xi_{s(\gamma_1)}\Big\rangle=\int g(\gamma_2)\,\varphi(\gamma_2^{-1}\gamma_1)\,d\nu^y(\gamma_2),
\]
and \(\varphi(\gamma_2^{-1}\gamma_1)=\overline{\varphi(\gamma_1^{-1}\gamma_2)}=\tilde\varphi(\gamma_1^{-1}\gamma_2)\).
Both sides are bounded operators agreeing on a dense subspace. The norm formula follows from \(|\tilde\varphi|=
|\varphi|\).

(e) For \(\alpha\in H_y\) and \(\gamma_1:x_1\to y\), using (2.1) and \(\nu^y=\gamma_1\nu^{x_1}\),
\[
\big\langle\alpha,U(\gamma_1)(U(f\nu)\xi)_{x_1}\big\rangle=\int\overline{f(\gamma')}\langle\alpha,U(\gamma_1\gamma')
\xi_{s(\gamma')}\rangle\,d\nu^{x_1}(\gamma')=\int\bar f(\gamma_1^{-1}\gamma_2)(T_\nu(\xi)_y\alpha)(\gamma_2)\,
d\nu^y(\gamma_2).
\]
The right side is \((R_{\nu',\nu}(\bar f)T_\nu(\xi)_y\alpha)(\gamma_1)\), whose \(L^2(\nu'^y)\)-norm is at most
\(\|f\|_{\nu',\nu}c\|\alpha\|\) by Proposition 3.3(a). \(U(f\nu)\xi\) is bounded measurable since \(\nu(|f|)\) is
bounded.

(f) \(\theta_\nu(\xi,\eta)\) is a product of intertwiners (Proposition 2.6(a)). Formula (4.2) is
\(\langle T_\nu(\eta)_y\alpha,T_\nu(\xi)_y\beta\rangle\). The first identity of (4.3) follows from (c):
\(\theta_\nu(A\xi,B\eta)=(T_\nu(\xi)A^*)^*T_\nu(\eta)B^*\); the second from
\(T_\nu(\theta_\nu(\xi,\eta)\xi')=T_\nu(\xi')\theta_\nu(\xi,\eta)^*\). Finally
\[
(\theta_\nu(\xi,\eta)\xi',\eta')(\gamma)=\langle T_\nu(\eta)_y\xi'_y,\,T_\nu(\xi)_yU(\gamma)\eta'_x\rangle=
\langle(\xi',\eta)|_{G^y},L^\nu(\gamma)(\eta',\xi)|_{G^x}\rangle,
\]
which is the coefficient of \(L^\nu\) between \((\xi',\eta)\) and \((\eta',\xi)\); apply Proposition 3.1(c).
\(\square\)

**Corollary 4.3.** Let \((H,U)\) be a representation and \(\nu\in\mathcal E^+\). Let \(\mathcal J_\nu\) be the linear
span of the operators \(\theta_\nu(\xi,\eta)\), \(\xi,\eta\in D(U,\nu)\).

(a) \(\mathcal J_\nu\) is a self-adjoint two-sided ideal of \(\operatorname{End}_G(H)\).

(b) If \(\nu_1,\nu_2\in\mathcal E^+\) and \(\nu_1\le\nu_2\), then \(\mathcal J_{\nu_1}\subset\mathcal J_{\nu_2}\).

*Proof.* (a) By (4.3), \(A\theta_\nu(\xi,\eta)=\theta_\nu(A\xi,\eta)\) and \(\theta_\nu(\xi,\eta)B=\theta_\nu(\xi,
B^*\eta)\), and \(D(U,\nu)\) is stable under \(\operatorname{End}_G(H)\) by Proposition 4.2(c).

(b) By (R2), \(\nu_1=(a\circ s)\nu_2\) with \(0\le a\le1\). The operators \((M_yq)(\gamma)=a(s(\gamma))^{1/2}q(\gamma)\)
map \(L^2(G,\nu_1^y)\) isometrically into \(L^2(G,\nu_2^y)\), since \(\int|q|^2(a\circ s)\,d\nu_2^y=\int|q|^2\,d\nu_1^y\);
they commute with left translations because \(s(\gamma^{-1}\gamma')=s(\gamma')\), so \(M\in\operatorname{Hom}_G
(L^{\nu_1},L^{\nu_2})\) with \(M^*M=1\). For \(\xi\in D(U,\nu_1)\) let \(\xi'=(a^{1/2}(x)\xi_x)_x\). Then
\((T_{\nu_2}(\xi')_y\alpha)(\gamma)=a(s(\gamma))^{1/2}\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle\), so
\(\xi'\in D(U,\nu_2)\) and \(T_{\nu_2}(\xi')=MT_{\nu_1}(\xi)\). Hence \(\theta_{\nu_2}(\xi',\eta')=T_{\nu_1}(\xi)^*M^*M
T_{\nu_1}(\eta)=\theta_{\nu_1}(\xi,\eta)\). \(\square\)

### 4.2 Square integrability

**Theorem 4.4.** Let \(\nu\in\mathcal E^+\) be faithful and \((H,U)\) a representation of \(G\). The following are
equivalent, and whether they hold is independent of \(\nu\).

1. \(D(U,\nu)\) contains a countable total subset.
2. \(H\prec\infty\cdot L^\nu\).
3. There is a representation \(H'\) with \(H\prec H'\) such that \(H'\prec H'\otimes K\) for every representation
   \(K\) with \(K_x\neq0\) for all \(x\).

*Proof.* We first record two facts.

*(i) Property 1 passes to subrepresentations.* If \(V\in\operatorname{Hom}_G(H,H')\) has isometric fibres and
\(D'\subset D(U',\nu)\) is countable and total, then \(V^*D'\subset D(U,\nu)\) by Proposition 4.2(c), and it is total
because each \(V_x^*\) maps \(H'_x\) onto \(H_x\).

*(ii) Property 1 holds for \(\infty\cdot L^\nu\).* Let \(B_n\) be as in Lemma 1.2(a) and \(g=1_{C\cap B_n}\) with
\(C\in\mathcal C\). Then \(\varphi=(g,g)=g*_\nu g^\flat\) (Proposition 3.1(c)) and, as in the proof of Proposition
3.3(c), \(\sup\nu(|\varphi|)\le\sup\nu(|g|)\sup\nu(|g^\flat|)\le(\sup_y\nu^y(B_n))^2<\infty\), because \(B_n\) is
symmetric. By Proposition 4.2(d), \(g\in D(L^\nu,\nu)\). The sections of \(\infty\cdot L^\nu\) with one component of
this form and the others zero have the same coefficients, lie in \(D(\infty\cdot L^\nu,\nu)\), are countably many, and
are total by Lemma 1.2(b).

1 \(\Rightarrow\) 2. Let \(\{\xi^n\}\subset D(U,\nu)\) be total, with constants \(c_n\) in (4.1). The field
\(T_x\alpha=\big(2^{-n}(1+c_n)^{-1}T_\nu(\xi^n)_x\alpha\big)_{n\ge1}\) is an intertwiner from \(H\) to
\(\infty\cdot L^\nu\), of norm at most \(1\). It is injective in every fibre: if \(T_x\alpha=0\), then
\(\langle\alpha,U(\gamma)\xi^n_{s(\gamma)}\rangle=0\) for \(\nu^x\)-almost every \(\gamma\) and all \(n\); as
\(\nu^x\neq0\) there is \(\gamma:x'\to x\) with \(U(\gamma)^{-1}\alpha\perp\xi^n_{x'}\) for all \(n\), so \(\alpha=0\).
The partial isometry \(v\) of the polar decomposition of \(T\) is an intertwiner (Proposition 2.6(b)) with isometric
fibres.

2 \(\Rightarrow\) 3. Take \(H'=\infty\cdot L^\nu\). For \(K\) with nonzero fibres, \(L^\nu\prec L^\nu\otimes K\) by
Proposition 3.4, hence \(H'\prec\infty\cdot(L^\nu\otimes K)=H'\otimes K\).

3 \(\Rightarrow\) 1. Since \(\nu\) is faithful, \(L^\nu\) has nonzero fibres, so \(H\prec H'\prec H'\otimes L^\nu\).
The flip \(H'\otimes L^\nu\to L^\nu\otimes H'\) is a unitary intertwiner, and \(L^\nu\otimes H'\prec\infty\cdot L^\nu\)
by Proposition 3.4. So \(H\prec\infty\cdot L^\nu\), and 1 follows from (i) and (ii).

Condition 3 does not mention \(\nu\), and it is equivalent to 1 and 2 for every faithful \(\nu\). \(\square\)

**Definition 4.5.** A representation is *square integrable* if it satisfies the conditions of Theorem 4.4.

**Proposition 4.6.** (a) A representation \(H'\prec H\) with \(H\) square integrable is square integrable. (b) A
countable direct sum of square-integrable representations is square integrable. (c) If \(H\) is square integrable and
\(K\) is any representation, \(H\otimes K\) is square integrable.

*Proof.* (a) \(H'\prec H\prec\infty\cdot L^\nu\). (b) \(\bigoplus_iH^i\prec\bigoplus_i\infty\cdot L^\nu\), which is
equivalent to \(\infty\cdot L^\nu\). (c) If \(V:H\to\infty\cdot L^\nu\) has isometric fibres, so does \(V\otimes1:
H\otimes K\to\infty\cdot(L^\nu\otimes K)\), and \(L^\nu\otimes K\prec\infty\cdot L^\nu\) by Proposition 3.4. \(\square\)

### 4.3 Representations defined by proper random variables

**Lemma 4.7.** Let \((H,U)\) be a representation, \(\nu\in\mathcal E^+\), and \((B_x)\) a bounded measurable field
of positive operators \(B_x\in B(H_x)\) such that for some \(C\)
\[
\int\big\langle B_{s(\gamma)}U(\gamma)^{-1}\alpha,U(\gamma)^{-1}\alpha\big\rangle\,d\nu^y(\gamma)\le C\|\alpha\|^2
\qquad(y\in G^{(0)},\ \alpha\in H_y).
\]
Then for every bounded measurable section \(\xi\), the section \(B^{1/2}\xi=(B_x^{1/2}\xi_x)\) belongs to
\(D(U,\nu)\).

*Proof.* \(B^{1/2}\) is measurable by (B1)(iv). For \(\gamma:x\to y\) and \(\alpha\in H_y\),
\[
|\langle\alpha,U(\gamma)B_x^{1/2}\xi_x\rangle|^2=|\langle B_x^{1/2}U(\gamma)^{-1}\alpha,\xi_x\rangle|^2\le
\|\xi\|_\infty^2\langle B_xU(\gamma)^{-1}\alpha,U(\gamma)^{-1}\alpha\rangle;
\]
integrate against \(\nu^y\). \(\square\)

Let \((X,\alpha)\) be a random variable of some modulus \(\rho\) (R7), with \(X\) countably generated, and let
\(\mathcal C_X\) be a countable algebra generating its \(\sigma\)-algebra. The field \(L^2(X,\alpha)=
(L^2(X,\alpha^x))_x\), with fundamental sequence \(1_{E\cap X_n}\) (\(E\in\mathcal C_X\)), carries the representation
\[
(U(\gamma)g)(z)=\rho(\gamma)^{1/2}g(\gamma^{-1}z)\qquad(\gamma:x\to y,\ z\in X^y,\ g\in L^2(X,\alpha^x)).
\]
Indeed \(\gamma^{-1}\alpha^y=\rho(\gamma)^{-1}\alpha^x\), so \(U(\gamma)\) is unitary; the fundamental sequence is total
by the argument of Lemma 1.2(b); and the coefficients \(\rho(\gamma)^{1/2}\int1_{E\cap X_n}(z)1_{E'\cap X_m}(\gamma^{-1}z)
\,d\alpha^{r(\gamma)}(z)\) are measurable by Lemma 1.1, so Lemma 2.2 applies. The left regular representation
\(L^\nu\) is the case \(X=G\) with left translations, \(\alpha=\nu\), \(\rho=1\).

**Proposition 4.8.** If the random variable \((X,\alpha)\) is proper, the representation \(L^2(X,\alpha)\) is square
integrable.

*Proof.* Let \(\nu\) be faithful, \(f>0\) on \(X\) with \(\nu*f=1\) (R7), and \(b=\min(f,1)\), so that \(0<b\le1\)
and \(\nu*b\le1\). Let \(B_x\) be multiplication by \(b\) on \(L^2(X,\alpha^x)\). Then
\(U(\gamma)B_xU(\gamma)^{-1}\) is multiplication by \(b(\gamma^{-1}\cdot)\), and
\[
\int\langle B_xU(\gamma)^{-1}\beta,U(\gamma)^{-1}\beta\rangle\,d\nu^y(\gamma)=\int|\beta(z)|^2(\nu*b)(z)\,d\alpha^y(z)
\le\|\beta\|^2
\]
by Tonelli's theorem. By Lemma 4.7, \(B^{1/2}\xi\in D(U,\nu)\) for every bounded measurable \(\xi\). Applied to the
fundamental sequence, this gives a countable total subset of \(D(U,\nu)\): multiplication by \(b^{1/2}>0\) is injective
and self-adjoint, hence has dense range. \(\square\)

**Corollary 4.9.** Let \(h:G_1\to G\) be a proper homomorphism, where \(G_1\) also satisfies (S) and (F). If \(H\) is a
square-integrable representation of \(G\), then \(h^*H\) is a square-integrable representation of \(G_1\).

*Proof.* If \(V:H\to\infty\cdot L^\nu\) has isometric fibres, so does \(h^*V:h^*H\to\infty\cdot h^*L^\nu\); by
Proposition 4.6 it suffices to treat \(h^*L^\nu\). Its fibre at \(x\) is \(L^2(G,\nu^{h(x)})\), and
\((h^*L^\nu)(\gamma)\) is left translation by \(h(\gamma)\). This is \(L^2(X_h,\alpha)\) for the random variable of
modulus \(1\) on the \(G_1\)-space \(X_h=\{(x,\gamma'):r(\gamma')=h(x)\}\) of (R8), with \(\alpha^x=\nu^{h(x)}\) placed on
\(\{x\}\times G^{h(x)}\) (condition \(\gamma\alpha^x=\alpha^{r(\gamma)}\) is the invariance of \(\nu\), and
\(X_h=\bigcup_n(G_1^{(0)}\times B_n)\cap X_h\)). The two measurable structures agree: the pulled-back fundamental
sections \(x\mapsto1_{C\cap B_n}|_{G^{h(x)}}\) are total and have measurable inner products
\(\alpha^x(E\cap(G_1^{(0)}\times(C\cap B_n)))\) with the fundamental sections of \(L^2(X_h,\alpha)\), so (B1)(iii)
applies. Since \(h\) is proper, \(X_h\) is a proper \(G_1\)-space, and Proposition 4.8 applies. \(\square\)

**Example 4.10.**

(a) *Groups.* Let \(G\) be a locally compact second countable group (one unit), and \(\nu\) a left Haar measure. Then
\(L^\nu\) is the left regular representation, \(D(U,\nu)\) is the space of vectors \(\xi\) for which
\(\alpha\mapsto\langle\alpha,U(\cdot)\xi\rangle\) is a bounded map into \(L^2(G)\), and square integrable means
contained in a multiple of the regular representation. If \(G\) is compact and \(\nu\) is the Haar probability, (4.1)
holds with \(c=\|\xi\|\) for every \(\xi\): every representation is square integrable. If \(G=\mathbb R\) and
\(U=\mathbf 1\), then \(\int_{\mathbb R}|\alpha\bar\xi|^2\,dt=\infty\) unless \(\alpha\bar\xi=0\), so \(D(\mathbf 1,
\nu)=\{0\}\) and the trivial representation is not square integrable.

(b) *Spaces.* If \(G=G^{(0)}=X\), a transverse function is \(\nu^x=a(x)\varepsilon_x\) with \(a\) finite, and
\(L^\nu=\mathbf 1\) where \(a>0\). With \(a=1\), (4.1) holds with \(c=\|\xi\|_\infty\) for every bounded section: every
measurable field is square integrable, and random operators (Section 6) are ordinary decomposable operators.

(c) *Pair groupoids.* Let \(G=X\times X\) for a standard Borel space \(X\) with a probability measure \(\beta\), so
\(G^y=\{y\}\times X\). Then \(\nu^y=\varepsilon_y\otimes\beta\) is a faithful transverse function of total mass \(1\), and
\(\mathbf 1\) is square integrable: (4.1) holds with \(c=\|\xi\|_\infty\).

## 5. Irreducibility at points with trivial isotropy

In this section \((G,\mathcal B)\) is a standard Borel space. For an intertwiner \(A\in\operatorname{End}_G(H)\) and
\(g\in G^y_y\), \(U(g)A_y=A_yU(g)\): the fibres of random operators always commute with the isotropy group. The next
result says that, at a point with trivial isotropy, the fibres of the operators \(\theta_\nu(\xi,\eta)\) exhaust
\(B(H_y)\), and a single countable family of sections does this at all such points.

**Proposition 5.1.** Let \(G\) be standard Borel, \((H,U)\) square integrable and \(\nu\in\mathcal E^+\) faithful.
There is a countable total set \(D\subset D(U,\nu)\) such that, for every \(y\in G^{(0)}\), the linear span
\(\mathcal A_y\) of \(\{\theta_\nu(\xi,\eta)_y:\xi,\eta\in D\}\) is a \(*\)-algebra, and \(\mathcal A_y\) is weakly
dense in \(B(H_y)\) whenever \(G^y_y=\{y\}\).

*Proof.* *Step 1: \(H=L^\nu\).* Let \(B_n\) be as in Lemma 1.2(a) and \(D_0=\{1_{C\cap B_n}:C\in\mathcal C,n\ge1\}\subset
D(L^\nu,\nu)\) (proof of Theorem 4.4, fact (ii)). For \(E\in\mathcal C_0\) the multiplication \(M^E\) by
\(1_E\circ s\) belongs to \(\operatorname{End}_G(L^\nu)\) (it commutes with left translations since
\(s(\gamma^{-1}\gamma')=s(\gamma')\)), and \(M^E\) maps \(D_0\) into \(D_0\) because \(s^{-1}(E)\in\mathcal C\). Fix \(y\)
with \(G^y_y=\{y\}\), and let \(S\in B(L^2(G,\nu^y))\) commute with all \(\theta=\theta_\nu(f,g)_y\), \(f,g\in D_0\).

(i) \(S\) commutes with every \(M^E_y\). By (4.3), \(\theta_\nu(f,g)M^E=\theta_\nu(f,M^Eg)\), so \(S\) commutes with
\(\theta M^E_y\) and with \(\theta\); hence \(\theta SM^E_y=S\theta M^E_y=\theta M^E_yS\), i.e. \(\theta(SM^E_y-M^E_yS)=
0\). The common kernel of the \(\theta_\nu(f,f)_y=T_\nu(f)_y^*T_\nu(f)_y\) is \(\bigcap_f\ker T_\nu(f)_y\), which is
\(\{0\}\): if \(\langle\alpha,L^\nu(\gamma)f\rangle=0\) for \(\nu^y\)-almost every \(\gamma\) and all \(f\in D_0\), pick
such a \(\gamma:x\to y\); then \(L^\nu(\gamma)^{-1}\alpha\) is orthogonal to the total set \(D_0\) of \(L^2(G,\nu^x)\), so
\(\alpha=0\). Therefore \(SM^E_y=M^E_yS\).

(ii) \(S\) is a multiplication operator. The von Neumann algebra generated by the \(M^E_y\), \(E\in\mathcal C_0\),
contains multiplication by \(1_E\circ s\) for every Borel \(E\subset G^{(0)}\) (the sets \(E\) for which this holds form a
monotone class containing the algebra \(\mathcal C_0\)), hence multiplication by \(b\circ s\) for every bounded Borel
\(b\). Since \(G^y_y=\{y\}\), \(s\) is injective on the standard Borel space \(G^y\) (if \(s(\gamma)=s(\gamma')\) then
\(\gamma'\gamma^{-1}\in G^y_y\)), so by (B6) it is a Borel isomorphism onto a Borel set, and every bounded Borel
function on \(G^y\) is of the form \(b\circ s\). So \(S\) commutes with \(L^\infty(G,\nu^y)\), which is maximal abelian
(B2): \(S\) is multiplication by some \(\phi\in L^\infty(G,\nu^y)\).

(iii) \(\phi\) is constant. Let \(g_n=1_{B_n}\). By Proposition 4.2 and Proposition 3.1(c), \(T_\nu(g)=R_{\nu,\nu}
(\bar g)\) for \(g\in D_0\) (indeed \((T_\nu(g)\alpha)(\gamma_1)=(\alpha*_\nu g^\flat)(\gamma_1)=\int\overline{g(\gamma_1^{-1}
\gamma_2)}\alpha(\gamma_2)\,d\nu^y(\gamma_2)\)), so by Proposition 3.3(c) \(\theta_\nu(g_n,g_n)=R_{\nu,\nu}(k_n)\) with
\(k_n=\tilde g_n*_\nu g_n\). The kernel of this operator is, after the substitution \(\gamma''=\gamma_1\gamma'\),
\[
k_n(\gamma_1^{-1}\gamma_2)=\int1_{B_n}(\gamma''^{-1}\gamma_1)1_{B_n}(\gamma''^{-1}\gamma_2)\,d\nu^y(\gamma'')=
\nu^y(\gamma_1B_n\cap\gamma_2B_n),
\]
where \(\gamma_iB_n=\{\gamma''\in G^y:\gamma_i^{-1}\gamma''\in B_n\}\) (\(B_n\) is symmetric). The operator
\(M_\phi R_{\nu,\nu}(k_n)-R_{\nu,\nu}(k_n)M_\phi=0\) has the kernel \(F(\gamma_1,\gamma_2)=(\phi(\gamma_1)-
\phi(\gamma_2))k_n(\gamma_1^{-1}\gamma_2)\), bounded by \(2\|\phi\|_\infty\sup\nu(B_n)\). Testing against
\(1_{E'}\otimes1_E\) for sets of finite measure shows that the complex measure \(F\,d(\nu^y\otimes\nu^y)\) vanishes on
rectangles inside \(E'\times E\), hence \(F=0\) almost everywhere. As \(n\to\infty\), \(\gamma_iB_n\uparrow G^y\), so
\(k_n(\gamma_1^{-1}\gamma_2)\uparrow\nu^y(G^y)>0\) for every \((\gamma_1,\gamma_2)\). Hence \(\phi(\gamma_1)=
\phi(\gamma_2)\) for almost every \((\gamma_1,\gamma_2)\), and by Fubini \(\phi\) is almost everywhere constant.

So \(\{\theta_\nu(f,g)_y:f,g\in D_0\}'=\mathbb C\) at every \(y\) with trivial isotropy.

*Step 2: \(\infty\cdot L^\nu=\ell^2\otimes L^\nu\).* Let \((e_i)\) be the standard basis of \(\ell^2\) and
\(D_1=\{e_i\otimes f:f\in D_0,i\ge1\}\). The coefficients show \(T_\nu(e_i\otimes f)=e_i^*\otimes T_\nu(f)\), where
\(e_i^*\beta=\langle\beta,e_i\rangle\), so \(\theta_\nu(e_i\otimes f,e_j\otimes g)=e_ie_j^*\otimes\theta_\nu(f,g)\). Let
\(y\) have trivial isotropy and \(\mathcal X=\{\theta_\nu(f,g)_y\}\). \(\mathcal X\) is self-adjoint with commutant
\(\mathbb C\), so the algebra it generates is weakly dense in \(B(L^2(G,\nu^y))\) (double commutant theorem; it is
nondegenerate since \(\mathcal X\neq\{0\}\) and the projection onto the common kernel lies in \(\mathcal X'\)). Since
\((e_ie_j^*\otimes x)(e_je_k^*\otimes x')=e_ie_k^*\otimes xx'\), the algebra generated by
\(\{\theta_\nu(\zeta,\zeta')_y:\zeta,\zeta'\in D_1\}\) is weakly dense in \(B(\ell^2\otimes L^2(G,\nu^y))\).

*Step 3: general \(H\).* By Theorem 4.4 there is \(V\in\operatorname{Hom}_G(H,\infty\cdot L^\nu)\) with isometric
fibres; put \(P=VV^*\). Let \(D_2\) be the smallest set containing \(D_1\) and stable under \(\zeta\mapsto P\zeta\) and
\((\zeta_1,\zeta_2,\zeta_3)\mapsto\theta_\nu(\zeta_1,\zeta_2)\zeta_3\); it is countable and contained in
\(D(\infty\cdot L^\nu,\nu)\) by Proposition 4.2(c). By (4.3) the span \(\mathcal A^{(2)}_y\) of
\(\{\theta_\nu(\zeta,\zeta')_y:\zeta,\zeta'\in D_2\}\) is a \(*\)-algebra, closed under \(x\mapsto P_yx\) and
\(x\mapsto xP_y\) (since \(P\theta_\nu(\zeta,\zeta')=\theta_\nu(P\zeta,\zeta')\)), and it is weakly dense at points with
trivial isotropy by Step 2. Put \(D=V^*D_2\subset D(U,\nu)\), a countable total set (fact (i) in the proof of Theorem
4.4). By (4.3), \(\theta_\nu(V^*\zeta,V^*\zeta')=V^*\theta_\nu(\zeta,\zeta')V\), so \(\mathcal A_y=V_y^*\mathcal
A^{(2)}_yV_y\). It is a \(*\)-algebra: \(V^*xVV^*x'V=V^*(xPx')V\) with \(xPx'\in\mathcal A^{(2)}_y\). Since \(V_y\) is an
isometry, \(x\mapsto V_y^*xV_y\) is weakly continuous from \(B(\ell^2\otimes L^2(G,\nu^y))\) onto \(B(H_y)\); so
\(\mathcal A_y\) is weakly dense when \(\mathcal A^{(2)}_y\) is. \(\square\)

**Remark 5.2 (nontrivial isotropy).** For separable \(G\) (countably generated \(\mathcal B\)), [Connes 1979] states
more generally that for every \(y\) the restriction of \(U\) to \(G^y_y\) is a square-integrable representation of
this group, which carries a locally compact topology, and that the \(\theta_\nu(\xi,\eta)_y\), \(\xi,\eta\) in a suitable countable \(D\), generate
the commutant \(U(G^y_y)'\). The proof decomposes \((G^y,\nu^y)\) as a product of a Haar measure on \(G^y_y\) and a
measure on the orbit \(s(G^y)\), using a measurable cross-section of \(s\) on \(G^y\); the existence of the locally
compact topology rests on the theorem of Mackey and Weil on Borel groups with invariant measures [Mackey 1957]. We do
not reproduce this argument. The part of it used below is Proposition 5.1, which we prove only for standard \(G\): its
proof uses that every bounded measurable function on \(G^y\) is a function of \(s\) when \(G^y_y=\{y\}\), and we
derive this from standardness. The inclusion of the \(\theta_\nu(\xi,\eta)_y\)
in \(U(G^y_y)'\) always holds, by the remark at the beginning of this section.

## 6. Random operators and the algebra \(W(\nu)\)

From now on \(\Lambda\) is a \(\sigma\)-finite transverse measure of modulus \(\delta\) on \(G\). By (R5), every
\(\Lambda_\nu\), \(\nu\in\mathcal E^+\), is \(\sigma\)-finite. Example 7.6 shows that this hypothesis cannot be
weakened to semi-finiteness. A reference for Sections 6 to 8 is [Connes 1979]; see
also [Connes 1982].

### 6.1 Random operators

Let \(H_1,H_2\) be square-integrable representations and \(T\in\operatorname{Hom}_G(H_1,H_2)\). The set
\(\{x:T_x\neq0\}\) is measurable (it is the union over \(n,m\) of \(\{\langle T_x\xi^n_x,\xi'^m_x\rangle\neq0\}\)) and
saturated (\(T_y=U_2(\gamma)T_xU_1(\gamma)^{-1}\)); likewise \(x\mapsto\|T_x\|\) is measurable and constant on orbits.

**Definition 6.1.** A *random operator* from \(H_1\) to \(H_2\) is a class of intertwiners
\(T\in\operatorname{Hom}_G(H_1,H_2)\) modulo those that vanish off a \(\Lambda\)-negligible saturated set. The space
of random operators is \(\operatorname{Hom}_\Lambda(H_1,H_2)\), with norm \(\|T\|_\infty=\inf\{c:\{x:\|T_x\|>c\}\text{ is
}\Lambda\text{-negligible}\}\), and \(\operatorname{End}_\Lambda(H)=\operatorname{Hom}_\Lambda(H,H)\). Two square-integrable
representations that coincide off a \(\Lambda\)-negligible saturated set are identified; a class of such
representations is a *\(\Lambda\)-random Hilbert space*.

Given \(T\), the set \(\{x:\|T_x\|>\|T\|_\infty\}\) is saturated and negligible, and setting \(T_x=0\) there gives a
representative with \(\sup_x\|T_x\|=\|T\|_\infty\). So \(\|\cdot\|_\infty\) is the quotient norm, and
\(\operatorname{End}_\Lambda(H)\) is the quotient of the C\(^*\)-algebra \(\operatorname{End}_G(H)\) by a closed
two-sided \(*\)-ideal: it is a C\(^*\)-algebra. All the constructions below depend only on the \(\Lambda\)-random Hilbert
spaces, because negligible sets are \(\Lambda_\nu\)-null for every \(\nu\).

### 6.2 A left Hilbert algebra of functions on \(G\)

Fix \(\nu\in\mathcal E^+\), and put \(\mu=\Lambda_\nu\) and \(m=m_\nu=\mu\circ\nu\). The measure \(m\) is
\(\sigma\)-finite: \(G\) is covered by the sets \(B_n\cap r^{-1}(Z_k)\) with \(\mu(Z_k)<\infty\). Let
\(\mathfrak h_\nu=L^2(G,m)\). By Tonelli's theorem and Proposition 3.1(a), \(g\mapsto(g|_{G^y})_y\) is a unitary from
\(\mathfrak h_\nu\) onto the direct integral \(\int^\oplus L^2(G,\nu^y)\,d\mu(y)\) of the field \(L^2(G,\nu)\). By (1.1),
\[
(Jg)(\gamma)=\delta(\gamma)^{-1/2}\,\overline{g(\gamma^{-1})}=\big(\delta^{-1/2}g^\flat\big)(\gamma)
\]
is a conjugate-linear isometry of \(\mathfrak h_\nu\) with \(J^2=1\): \(m(\delta^{-1}|\tilde g|^2)=m(|g|^2)\) because
\(\widetilde{\delta^{-1}|\tilde g|^2}=\delta|g|^2\). Let \(\Delta\) be multiplication by \(\delta\), a positive
self-adjoint operator. For a measurable \(k\) with \(\|k\|_\nu<\infty\) let \(\rho(k)\) be the decomposable operator of
right convolution \(q\mapsto q*_\nu k=R_{\nu,\nu}(\tilde k)q\); by Proposition 3.3, \(\|\rho(k)\|\le\|\tilde k\|_\nu=
\|k\|_\nu\) and \(\rho(k)^*=\rho(k^\flat)\).

Let \(\mathcal K_\nu\) be the set of measurable functions \(f\) on \(G\) with \(\|\delta^tf\|_\nu<\infty\) for every
\(t\in\mathbb R\), and
\[
\mathcal A_\nu=\{f\in\mathcal K_\nu:\ f\in\mathfrak h_\nu,\ \delta^{1/2}f\in\mathfrak h_\nu\},\qquad
f^\#=\delta^{-1}f^\flat,\qquad f*_\nu g\ \text{as in (3.1)}.
\]
For \(f\in\mathcal K_\nu\) put \(\lambda_\nu(f)=J\rho(Jf)J\), a bounded operator on \(\mathfrak h_\nu\) of norm at most
\(\|Jf\|_\nu\) (note \(Jf=\delta^{-1/2}f^\flat\in\mathcal K_\nu\)).

**Proposition 6.2.** (a) \(\mathcal K_\nu\) is stable under \(*_\nu\), \(f\mapsto f^\flat\), \(f\mapsto\delta^tf\), and
multiplication by bounded measurable functions of \(r\) and of \(s\).

(b) For \(f\in\mathcal K_\nu\) and \(g\in\mathfrak h_\nu\), the integral \((f*_\nu g)(\gamma)\) converges absolutely for
\(m\)-almost every \(\gamma\), and \(\lambda_\nu(f)g=f*_\nu g\). Moreover \(\lambda_\nu(f)\) depends only on the class
of \(f\) modulo \(m\)-null functions.

(c) \(\mathcal A_\nu\) is a left Hilbert algebra in \(\mathfrak h_\nu\), with left multiplication operators
\(\lambda_\nu(f)\), and \(f^\#=J\Delta^{1/2}f\) for \(f\in\mathcal A_\nu\).

*Proof.* (a) Since \(\delta\) is multiplicative, \(\delta^t(f*_\nu g)=(\delta^tf)*_\nu(\delta^tg)\), and
\(\|a*_\nu b\|_\nu\le\|a\|_\nu\|b\|_\nu\) by Proposition 3.3(c). Next \(\delta^tf^\flat=(\delta^{-t}f)^\flat\) and
\(\|a^\flat\|_\nu=\|a\|_\nu\). Bounded multipliers do not increase \(|f|\) or \(|\tilde f|\) beyond a constant.

(b) The substitution \(\gamma'=\gamma^{-1}\gamma''\) in (3.1) shows \(\widetilde{a*_\nu b}=\tilde b*_\nu\tilde a\) at
every point where either side converges absolutely; taking complex conjugates and using
\(\delta(\gamma)^{-1/2}=\delta(\gamma'')^{-1/2}\delta(\gamma''^{-1}\gamma)^{-1/2}\) gives
\[
J(a*_\nu b)=(Jb)*_\nu(Ja). \tag{6.1}
\]
For \(g\in\mathfrak h_\nu\), \(\rho(Jf)Jg=(Jg)*_\nu(Jf)\) converges absolutely off an \(m\)-null set \(Z\) (Proposition
3.3(a), fibrewise). By (6.1), \(f*_\nu g=J((Jg)*_\nu(Jf))\) converges absolutely off \(Z^{-1}\), which is \(m\)-null by
(1.1), and equals \(J\rho(Jf)Jg\) there. Finally \(\rho(k)\) only depends on \(k|_{G^y}\) up to \(\nu^y\)-null sets for
\(\mu\)-almost all \(y\), that is on the \(m\)-class of \(k\); and \(f\mapsto Jf\) maps \(m\)-null functions to
\(m\)-null functions by (1.1).

(c) *Algebra.* If \(f,g\in\mathcal A_\nu\), then \(f*_\nu g\in\mathcal K_\nu\), \(f*_\nu g=\lambda_\nu(f)g\in
\mathfrak h_\nu\), and \(\delta^{1/2}(f*_\nu g)=\lambda_\nu(\delta^{1/2}f)(\delta^{1/2}g)\in\mathfrak h_\nu\).
Associativity follows from Fubini's theorem, the triple integrals converging absolutely almost everywhere by (b)
applied to \(|f|,|g|,|h|\). *Involution.* By (1.1), \(\|f^\#\|^2=m(\delta^{-2}|\tilde f|^2)=m(\delta|f|^2)\), so
\(f^\#\in\mathfrak h_\nu\) iff \(\delta^{1/2}f\in\mathfrak h_\nu\); and \(\delta^{1/2}f^\#=\delta^{-1/2}f^\flat=Jf\in
\mathfrak h_\nu\). With (a), \(f^\#\in\mathcal A_\nu\), \(f^{\#\#}=f\), and \((f*_\nu g)^\#=g^\#*_\nu f^\#\) (conjugate of
(6.1) without the \(\delta\)-factors, then multiply by \(\delta^{-1}\)). Also \(J\Delta^{1/2}f=\delta^{-1/2}
(\delta^{1/2}f)^\flat=\delta^{-1}f^\flat=f^\#\).

*(1) Adjoints.* \(\lambda_\nu(f)^*=J\rho(Jf)^*J=J\rho((Jf)^\flat)J\), and \((Jf)^\flat=\delta^{1/2}f\), whose image
under \(J\) is \(f^\#\). So \(\lambda_\nu(f)^*=\lambda_\nu(f^\#)\), which is condition (1) of (B3).

*(2) Boundedness* holds by construction.

*(3) Density of products.* Choose a Borel \(c>0\) on \(G^{(0)}\) with \(c\le1\) and \(\mu(c^2)<\infty\), let
\(w=(c\circ r)(c\circ s)\), and let \(D=\{w1_{C\cap B_n}\}\) with \(B_n\) as in Lemma 1.2(a) (for \(\nu\) and \(\delta\)).
Each \(f\in D\) lies in \(\mathcal A_\nu\): \(|f|\le1_{B_n}\), \(B_n\) is symmetric with \(n^{-1}\le\delta\le n\) on it, so
\(\|\delta^tf\|_\nu\le n^{|t|}\sup\nu(B_n)\), and \(m(|f|^2)\le\int c(y)^2\nu^y(B_n)\,d\mu(y)<\infty\), similarly for
\(\delta^{1/2}f\). By Lemma 1.2(b), \(D\) is total in each \(L^1(G,\nu^y)\) and in each \(L^2(G,\nu^y)\). By Proposition
2.4(b) for \(L^\nu\) and Proposition 3.1(b), the functions \(f*_\nu g\), \(f,g\in D\), are total in \(L^2(G,\nu^y)\) for
every \(y\) with \(\nu^y\neq0\). If \(h\in\mathfrak h_\nu\) is orthogonal to all \(((a\circ r)f)*_\nu g=(a\circ r)
(f*_\nu g)\), \(a\) bounded Borel on \(G^{(0)}\) (and \((a\circ r)f\in\mathcal A_\nu\)), then \(\langle h|_{G^y},
(f*_\nu g)|_{G^y}\rangle=0\) for \(\mu\)-almost every \(y\) and all \(f,g\in D\), so \(h=0\).

*(4) Closability.* \(f\mapsto f^\#\) is the restriction of the closed operator \(J\Delta^{1/2}\). \(\square\)

**Definition 6.3.** \(W(\nu)=\lambda_\nu(\mathcal A_\nu)''\), the left von Neumann algebra of \(\mathcal A_\nu\) on
\(\mathfrak h_\nu=L^2(G,m_\nu)\).

**Remark 6.4.** The closure of \(f\mapsto f^\#\) on \(\mathcal A_\nu\) is all of \(J\Delta^{1/2}\): the domain of
\(\Delta^{1/2}\) is \(L^2(G,(1+\delta)m)\) with the graph norm, and the argument of Lemma 1.2(b) (with the weight
\(w(1+\delta)\)) shows that the span of \(D\) is dense in it. So the modular conjugation and modular operator of the left
Hilbert algebra \(\mathcal A_\nu\) are \(J\) and multiplication by \(\delta\). By Left and right Hilbert algebras, Fact 2.9, \(W(\nu)\) is then also the left
von Neumann algebra of every left Hilbert algebra of functions, with the same product and involution, that lies between
\(\mathcal A_\nu\) and its full completion. Nothing below uses this remark.

**Lemma 6.5.** For every bounded Borel function \(a\) on \(G^{(0)}\), the multiplication \(M_{a\circ r}\) by \(a\circ r\)
on \(\mathfrak h_\nu\) belongs to \(W(\nu)\), and \(M_{a\circ r}\lambda_\nu(f)=\lambda_\nu((a\circ r)f)\) for
\(f\in\mathcal A_\nu\). The right convolutions \(\rho(k)\), \(\|k\|_\nu<\infty\), belong to \(W(\nu)'\).

*Proof.* \(((a\circ r)f)*_\nu g=(a\circ r)(f*_\nu g)\) because \(r(\gamma')=r(\gamma)\) in (3.1). Let \(X\in W(\nu)'\).
Then \(XM_{a\circ r}\lambda_\nu(f)=X\lambda_\nu((a\circ r)f)=\lambda_\nu((a\circ r)f)X=M_{a\circ r}X\lambda_\nu(f)\);
since the ranges of the \(\lambda_\nu(f)\) span a dense subspace (condition (3)), \(XM_{a\circ r}=M_{a\circ r}X\). So
\(M_{a\circ r}\in W(\nu)''=W(\nu)\). For the last claim, \(\lambda_\nu(f)\rho(k)g=f*_\nu(g*_\nu k)=(f*_\nu g)*_\nu k=
\rho(k)\lambda_\nu(f)g\) by Fubini's theorem. \(\square\)

## 7. The representation theorem

For \(\nu\in\mathcal E^+\) with \(\mu=\Lambda_\nu\) and a square-integrable \(H\), let
\[
\nu(H)=\int^\oplus H_x\,d\mu(x),
\]
and for \(T\in\operatorname{Hom}_\Lambda(H_1,H_2)\) let \(\nu(T)=\int^\oplus T_x\,d\mu(x)\). This is well defined,
because \(\Lambda\)-negligible saturated sets are \(\mu\)-null, and \(\|\nu(T)\|\le\|T\|_\infty\). Let \(\nu(H)_b\) be the
dense subspace of classes of bounded measurable sections \(\xi\) with \(\int\|\xi_x\|^2\,d\mu<\infty\). For
\(a\in L^\infty(\mu)\), \(\operatorname{diag}(a)\) is the diagonal operator \(\int^\oplus a(x)1\,d\mu(x)\).

**Theorem 7.1.** Let \(\nu\in\mathcal E^+\).

(a) For every square-integrable representation \((H,U)\) there is a unique normal unital representation
\(\pi^H_\nu\) of \(W(\nu)\) on \(\nu(H)\) such that, for \(f\in\mathcal A_\nu\) and \(\xi\in\nu(H)_b\), the section
\(U(f\nu)\xi\) is square integrable and
\[
\pi^H_\nu(\lambda_\nu(f))\,\xi=U(f\nu)\xi .
\]
For \(H=L^\nu\), \(\nu(L^\nu)=\mathfrak h_\nu\) and \(\pi^{L^\nu}_\nu\) is the identity representation. Moreover
\(\pi^H_\nu(M_{a\circ r})=\operatorname{diag}(a)\) for bounded Borel \(a\) on \(G^{(0)}\).

(b) For \(T\in\operatorname{Hom}_\Lambda(H_1,H_2)\), \(\nu(T)\pi^{H_1}_\nu(w)=\pi^{H_2}_\nu(w)\nu(T)\) for all
\(w\in W(\nu)\). The map \(T\mapsto\nu(T)\) is linear, multiplicative and \(*\)-preserving.

(c) Suppose \(\nu\) is faithful. Then \(T\mapsto\nu(T)\) is an isometric bijection from
\(\operatorname{Hom}_\Lambda(H_1,H_2)\) onto the space of bounded operators \(X:\nu(H_1)\to\nu(H_2)\) with
\(X\pi^{H_1}_\nu(w)=\pi^{H_2}_\nu(w)X\) for \(w\in W(\nu)\). In particular \(\nu\) is an isomorphism of
\(\operatorname{End}_\Lambda(H)\) onto the commutant \(\pi^H_\nu(W(\nu))'\). Every normal representation of \(W(\nu)\) on
a separable Hilbert space is unitarily equivalent to \(\pi^H_\nu\) for some square-integrable \(H\).

In the language of categories: for faithful \(\nu\), \(H\mapsto\nu(H)\), \(T\mapsto\nu(T)\) is an equivalence from the
category of \(\Lambda\)-random Hilbert spaces and random operators onto the category of normal \(W(\nu)\)-modules on
separable Hilbert spaces.

*Proof.* (a) *Step 1: \(H=L^\nu\).* By Section 6.2, \(\nu(L^\nu)=\mathfrak h_\nu\). For \(g\in\nu(L^\nu)_b\),
Proposition 3.1(b) and Proposition 6.2(b) give \(L^\nu(f\nu)g=f*_\nu g=\lambda_\nu(f)g\). So the identity representation
works.

*Step 2: \(H=\infty\cdot L^{\nu'}\) with \(\nu'=\nu+(1_{G^{(0)}\setminus A}\circ s)\nu_0\),* where \(A\) is the support of
\(\nu\) and \(\nu_0\) is faithful. Then \(\nu'\in\mathcal E^+\) is faithful and \(\nu'^y=\nu^y\) for \(y\in A\). Since
\(\mu\) is carried by \(A\), \(\nu(\infty\cdot L^{\nu'})=\ell^2\otimes\mathfrak h_\nu\), and on bounded sections
\(U(f\nu)\) acts componentwise as \(\lambda_\nu(f)\) (Step 1). So \(w\mapsto1\otimes w\) works.

*Step 3: general \(H\).* By Theorem 4.4 (with the faithful \(\nu'\)) there is \(V\in\operatorname{Hom}_G(H,\infty\cdot
L^{\nu'})\) with isometric fibres; \(P=VV^*\in\operatorname{End}_G(\infty\cdot L^{\nu'})\). Then \(\nu(V)\) is an isometry
with final projection \(\nu(P)\). For bounded \(\xi\), \(\nu(P)U'(f\nu)\xi=U'(f\nu)P\xi\) by Proposition 2.6(c); so
\(\nu(P)\) commutes with \(1\otimes\lambda_\nu(\mathcal A_\nu)\), hence with \(1\otimes W(\nu)\). Put
\(\pi^H_\nu(w)=\nu(V)^*(1\otimes w)\nu(V)\). This is normal and unital, and multiplicative because
\(\nu(V)\nu(V)^*=\nu(P)\) commutes with \(1\otimes w\). For \(\xi\in\nu(H)_b\), \(V\xi\) is bounded and square
integrable, and \(\pi^H_\nu(\lambda_\nu(f))\xi=V^*U'(f\nu)V\xi=V^*VU(f\nu)\xi=U(f\nu)\xi\) by Proposition 2.6(c).

*Uniqueness.* \(\lambda_\nu(\mathcal A_\nu)\) is a \(*\)-algebra (\(\lambda_\nu(f)\lambda_\nu(g)=\lambda_\nu(f*_\nu g)\),
\(\lambda_\nu(f)^*=\lambda_\nu(f^\#)\)) acting nondegenerately, so it is \(\sigma\)-weakly dense in \(W(\nu)\); a normal
representation is determined by its values there (B4)(ii), and these are determined on the dense subspace
\(\nu(H)_b\).

*Diagonal operators.* For \(f\in\mathcal A_\nu\) and bounded \(\xi\), \((U((a\circ r)f\nu)\xi)_y=a(y)(U(f\nu)\xi)_y\), so
by Lemma 6.5, \(\pi(M_{a\circ r})\pi(\lambda_\nu(f))=\pi(\lambda_\nu((a\circ r)f))=\operatorname{diag}(a)
\pi(\lambda_\nu(f))\). By (B4)(i) there is a bounded net \(\lambda_\nu(f_i)\to1\) strongly; \(\pi\) is strongly
continuous on bounded sets, so \(\pi(M_{a\circ r})=\operatorname{diag}(a)\).

(b) For bounded \(\xi\), \(\nu(T)U_1(f\nu)\xi=U_2(f\nu)T\xi\) (Proposition 2.6(c)), so \(\nu(T)\pi^{H_1}(w)=
\pi^{H_2}(w)\nu(T)\) for \(w\in\lambda_\nu(\mathcal A_\nu)\). The set of \(w\) satisfying this is a \(\sigma\)-weakly
closed subspace containing \(\lambda_\nu(\mathcal A_\nu)\), hence equal to \(W(\nu)\). The algebraic properties are those
of decomposable operators.

(c) *Isometry.* By (B2), \(\|\nu(T)\|=\operatorname{ess\,sup}_\mu\|T_x\|\). The sets \(\{x:\|T_x\|>c\}\) are saturated,
and for faithful \(\nu\) a saturated set is \(\Lambda\)-negligible iff it is \(\mu\)-null (R6). So
\(\|\nu(T)\|=\|T\|_\infty\).

*Surjectivity for \(H_1=H_2=H\).* Let \(X\in\pi^H_\nu(W(\nu))'\). By (a), \(X\) commutes with the diagonal algebra, so
\(X=\int^\oplus X_x\) for a measurable field \((X_x)\), which we may take with \(\|X_x\|\le\|X\|\) for all \(x\) (B2).
Let \(D=\{w1_{C\cap B_n}\}\subset\mathcal A_\nu\) be the countable family of the proof of Proposition 6.2(c), total in
every \(L^1(G,\nu^y)\), and let \(S\) be a countable total family of bounded measurable sections of \(H\) with
\(\int\|\xi_x\|^2\,d\mu<\infty\) (multiply a fundamental sequence, normalized to norm \(\le1\), by a function \(c>0\) with
\(\mu(c^2)<\infty\)). Let \((\eta^m)\) be a fundamental sequence. For \(h\in D\) and \(\xi\in S\),
\(X\pi(\lambda_\nu(h))\xi=\pi(\lambda_\nu(h))X\xi\) says that for \(\mu\)-almost every \(y\)
\[
\int h(\gamma)\Big(\big\langle X_yU(\gamma)\xi_{s(\gamma)},\eta^m_y\big\rangle-\big\langle U(\gamma)X_{s(\gamma)}
\xi_{s(\gamma)},\eta^m_y\big\rangle\Big)\,d\nu^y(\gamma)=0\quad\text{for all }m. \tag{7.1}
\]
The left side is measurable in \(y\): the integrand is \(\overline{(X^*\eta^m,\xi)}-\overline{(\eta^m,X\xi)}\). Let
\(A_0\) be the measurable set of \(y\) where (7.1) holds for all \(h\in D\), \(\xi\in S\), \(m\); then
\(\mu(G^{(0)}\setminus A_0)=0\). For \(y\in A_0\), Lemma 1.2(b) shows that the bounded integrands vanish
\(\nu^y\)-almost everywhere; as \(S\) is total at \(s(\gamma)\) and \((\eta^m_y)\) is total,
\[
X_yU(\gamma)=U(\gamma)X_{s(\gamma)}\qquad\text{for }\nu^y\text{-almost every }\gamma\in G^y\quad(y\in A_0). \tag{7.2}
\]
Put \(\Phi(\gamma)=U(\gamma)X_{s(\gamma)}U(\gamma)^{-1}\in B(H_{r(\gamma)})\); expanding in the orthonormal sections of
(B1)(ii) as in Lemma 2.2, \(\gamma\mapsto\langle\Phi(\gamma)\eta^k_{r(\gamma)},\eta^l_{r(\gamma)}\rangle\) is measurable.
By (7.2), \(\Phi=X_y\) \(\nu^y\)-almost everywhere on \(G^y\) for \(y\in A_0\). Let \(B\) be the complement of
\([G^{(0)}\setminus A_0]_\nu\); by (R6) \(B\) is saturated, measurable, and \(G^{(0)}\setminus B\) is
\(\Lambda\)-negligible. For \(y\in B\), \(s(\gamma)\in A_0\) for \(\nu^y\)-almost every \(\gamma\in G^y\).

*Claim: for \(y\in B\), \(\Phi\) is \(\nu^y\)-almost everywhere constant on \(G^y\).* For \(\nu^y\)-almost every \(\gamma\),
\(x'=s(\gamma)\in A_0\), so \(\Phi(\gamma'')=X_{x'}\) for \(\nu^{x'}\)-almost every \(\gamma''\in G^{x'}\), and then
\(\Phi(\gamma\gamma'')=U(\gamma)\Phi(\gamma'')U(\gamma)^{-1}=\Phi(\gamma)\). The set \(N=\{(\gamma,\gamma_3)\in G^y\times
G^y:\Phi(\gamma)\neq\Phi(\gamma_3)\}\) is measurable, and its section at \(\gamma\) is the image under left translation by
\(\gamma\) of \(\{\gamma'':\Phi(\gamma\gamma'')\neq\Phi(\gamma)\}\); since \(\gamma\nu^{s(\gamma)}=\nu^y\), it is
\(\nu^y\)-null for almost every \(\gamma\). By Tonelli's theorem \(N\) is null, so (as \(\nu^y\neq0\)) there is
\(\gamma_0\) with \(\Phi=\Phi(\gamma_0)\) almost everywhere.

Let \(f\ge0\) with \(\nu(f)=1\) (R2) and define \(X'_y=\int\Phi(\gamma)f(\gamma)\,d\nu^y(\gamma)\) (weakly) for
\(y\in B\), \(X'_y=0\) for \(y\notin B\). Then \((X'_y)\) is a bounded measurable field (Lemma 1.1), and by the claim
\(X'_y\) is the almost everywhere value of \(\Phi\) on \(G^y\) for \(y\in B\). It is an intertwiner: for
\(\gamma_1:x_1\to y_1\) in \(B\), \(U(\gamma_1)X'_{x_1}U(\gamma_1)^{-1}=\Phi(\gamma_1\gamma)\) for \(\nu^{x_1}\)-almost
every \(\gamma\), and \(\Phi(\gamma_1\gamma)=X'_{y_1}\) for \(\nu^{x_1}\)-almost every \(\gamma\) because
\(\gamma_1\nu^{x_1}=\nu^{y_1}\). For \(y\in A_0\cap B\), \(X'_y=X_y\) by (7.2), and \(A_0\cap B\) is \(\mu\)-conull. So
\(X=\nu(X')\) with \(X'\in\operatorname{End}_G(H)\).

*Surjectivity in general.* Apply the previous case to \(H_1\oplus H_2\): \(\nu(H_1\oplus H_2)=\nu(H_1)\oplus\nu(H_2)\), and
by uniqueness \(\pi^{H_1\oplus H_2}_\nu=\pi^{H_1}_\nu\oplus\pi^{H_2}_\nu\). If \(X\) intertwines \(\pi^{H_1}\) and
\(\pi^{H_2}\), the operator \(\begin{pmatrix}0&0\\X&0\end{pmatrix}\) lies in \(\pi^{H_1\oplus H_2}(W(\nu))'\), so it is
\(\nu(T')\) with \(T'\in\operatorname{End}_\Lambda(H_1\oplus H_2)\); the corner \(T=(1-P_1)T'P_1\) (\(P_1\) the projection
onto \(H_1\)) is a random operator from \(H_1\) to \(H_2\) with \(\nu(T)=X\).

*Every normal module.* Let \(\varrho\) be a normal representation of \(W(\nu)\) on a separable space. By (B4)(iii),
\(\varrho\) is equivalent to the subrepresentation of \(w\mapsto1\otimes w\) on \(\ell^2\otimes\mathfrak h_\nu\) defined
by a projection \(Q\) in its commutant. By Step 2 (with \(\nu'=\nu\)) this is \(\pi^{\infty\cdot L^\nu}_\nu\), so by the
first part \(Q=\nu(P')\) with \(P'\in\operatorname{End}_G(\infty\cdot L^\nu)\). The set where \(P'_x\) is not a
projection is saturated, measurable and \(\mu\)-null, hence negligible; setting \(P'_x=0\) there we get a projection
\(P\). Then \(H=P(\infty\cdot L^\nu)\) is square integrable (Proposition 4.6), \(\nu(H)=Q(\ell^2\otimes\mathfrak h_\nu)\),
and by uniqueness \(\pi^H_\nu\) is the restriction of \(1\otimes\mathrm{id}\), i.e. equivalent to \(\varrho\). \(\square\)

**Theorem 7.2.** For every \(\Lambda\)-random Hilbert space \(H\), the C\(^*\)-algebra \(\operatorname{End}_\Lambda(H)\)
is a von Neumann algebra (a W\(^*\)-algebra) with separable predual. For each faithful \(\nu\in\mathcal E^+\), \(\nu\) is a
\(*\)-isomorphism of \(\operatorname{End}_\Lambda(H)\) onto the von Neumann algebra \(\pi^H_\nu(W(\nu))'\) on the separable
space \(\nu(H)\).

*Proof.* A faithful \(\nu\) exists by (F), and Theorem 7.1(c) applies. \(\nu(H)\) is separable because \(\mu\) is
\(\sigma\)-finite, \(\mathcal B_0\) is countably generated and the fibres are separable. \(\square\)

The predual of a W\(^*\)-algebra is unique, so the normal functionals and the \(\sigma\)-weak topology of
\(\operatorname{End}_\Lambda(H)\) do not depend on \(\nu\). The collection of \(\Lambda\)-random Hilbert spaces, with
random operators as morphisms, is thus a W\(^*\)-category; it depends only on \((G,\mathcal B)\) and on the class of
\(\Lambda\) (its negligible sets), because square integrability does not involve \(\Lambda\) at all.

**Corollary 7.3.** Let \(H\) be a \(\Lambda\)-random Hilbert space and \(\nu\in\mathcal E^+\). The image \(J^\nu\) of
\(\mathcal J_\nu\) (Corollary 4.3) in \(\operatorname{End}_\Lambda(H)\) is a two-sided \(*\)-ideal; if \(\nu\) is faithful
it is \(\sigma\)-weakly dense.

*Proof.* The quotient map \(\operatorname{End}_G(H)\to\operatorname{End}_\Lambda(H)\) is a surjective \(*\)-homomorphism,
so it maps the ideal \(\mathcal J_\nu\) onto an ideal. Let \(\nu\) be faithful and \(\mathcal N=\nu(\operatorname{End}_
\Lambda(H))\). The \(\sigma\)-weak closure of \(\nu(J^\nu)\) is a \(\sigma\)-weakly closed ideal of \(\mathcal N\), so by
(B4)(iv) it suffices to show that \(\nu(J^\nu)\) acts nondegenerately on \(\nu(H)\). Let \(D\subset D(U,\nu)\) be countable
and total (Theorem 4.4). For \(\xi\in D\) the closed range of \(\theta_\nu(\xi,\xi)_y=T_\nu(\xi)_y^*T_\nu(\xi)_y\)
equals that of \(T_\nu(\xi)_y^*\), which contains the vectors \((U(h\nu)\xi)_y\) for \(h\) in the family \(D'=
\{1_{C\cap B_n}\}\) (Proposition 4.2(b)). By Proposition 2.4(b) these vectors, \(\xi\in D\), \(h\in D'\), are total in
\(H_y\) for every \(y\). The support projection of the decomposable operator \(\nu(\theta_\nu(\xi,\xi))\) is the
decomposable projection with fibres the supports of \(\theta_\nu(\xi,\xi)_y\) (strong limit of \(t^{1/j}\)); the supremum
over the countable set \(D\) is then \(1\). \(\square\)

**Lemma 7.4.** Let \(G_1\), \(G\) satisfy (S) and (F), \(h:G_1\to G\) a proper homomorphism, \(\delta\) a modulus on
\(G\), and \(\Lambda_1\) a transverse measure of modulus \(\delta\circ h\) on \(G_1\). A measurable saturated
\(A\subset G^{(0)}\) is \(h(\Lambda_1)\)-negligible iff the saturated set \(h^{-1}(A)\) is \(\Lambda_1\)-negligible.

*Proof.* Let \(\nu\) be faithful on \(G\). By (R6), \(A\) is \(h(\Lambda_1)\)-negligible iff
\(h(\Lambda_1)((1_A\circ s)\nu)=0\), that is (R8) iff \(\int h^*L^{(1_A\circ s)\nu}\,d\Lambda_1=0\). This random variable
lives on the proper \(G_1\)-space \(X_h\) and its measure over \(x\) is \(\delta^{-1}1_A(h(x))\nu^{h(x)}\) (as \(A\) is
saturated, \((1_A\circ s)\nu^{y}=1_A(y)\nu^y\)); it is nonzero exactly for \(x\in h^{-1}(A)\). By (R7) the integral
vanishes iff \(h^{-1}(A)\) is \(\Lambda_1\)-negligible. \(\square\)

**Corollary 7.5.** Let \(G_1,G,h,\delta,\Lambda_1\) be as in Lemma 7.4, with \(\Lambda_1\) \(\sigma\)-finite, and let
\(\Lambda\) be a \(\sigma\)-finite transverse measure on \(G\) such that every \(\Lambda\)-negligible saturated set is
\(h(\Lambda_1)\)-negligible.

(a) If \(H\) is a \(\Lambda\)-random Hilbert space, then \(h^*H\) is a well-defined \(\Lambda_1\)-random Hilbert space.

(b) \(h^*:(T_x)\mapsto(T_{h(x)})\) is a normal \(*\)-homomorphism \(\operatorname{End}_\Lambda(H)\to\operatorname{End}_{
\Lambda_1}(h^*H)\).

(c) Suppose \(h\) is an *equivalence*: there are a measurable homomorphism \(k:G\to G_1\) and measurable maps
\(\theta:G^{(0)}\to G\), \(\theta_1:G_1^{(0)}\to G_1\) with \(\theta(y):h(k(y))\to y\), \(\theta(y')h(k(\gamma))=\gamma\theta(y)\)
for \(\gamma:y\to y'\), and \(\theta_1(x):k(h(x))\to x\), \(\theta_1(x')k(h(\gamma_1))=\gamma_1\theta_1(x)\) for
\(\gamma_1:x\to x'\). If moreover \(h(\Lambda_1)\) and \(\Lambda\) have the same negligible sets, then \(h^*\) is a
\(*\)-isomorphism.

*Proof.* (a) \(h^*H\) is square integrable by Corollary 4.9. If \(H\) is changed on a negligible saturated \(A\), then
\(h^*H\) changes on \(h^{-1}(A)\), which is \(\Lambda_1\)-negligible by the hypothesis and Lemma 7.4.

(b) \(h^*T\) is measurable and intertwines: \(U(h(\gamma))T_{h(x)}=T_{h(y)}U(h(\gamma))\). By Lemma 7.4 and the
hypothesis, it is well defined on classes, and it is a \(*\)-homomorphism. *Normality.* \(\operatorname{End}_\Lambda(H)\)
has separable predual, so an orthogonal family of nonzero projections in it is countable. Given orthogonal projections
\(P_n\in\operatorname{End}_\Lambda(H)\), choose representatives; off a negligible saturated set they are orthogonal
projections, and we set them to \(0\) on it. Then \(Q_x=\sum_nP_{n,x}\) (strongly) is a projection in
\(\operatorname{End}_G(H)\), and \(\nu(Q)=\sum_n\nu(P_n)\) strongly for faithful \(\nu\) (dominated convergence in the
direct integral), so \(Q\) represents \(\sup_nP_n\) (Theorem 7.2). Likewise \(h^*Q=(Q_{h(x)})\) represents
\(\sup_nh^*P_n\). So \(h^*\) is completely additive, hence normal (B4)(ii).

(c) *\(h\) is bijective on isotropy groups.* If \(g,g'\in(G_1)^x_x\) and \(h(g)=h(g')\), then
\(g=\theta_1(x)k(h(g))\theta_1(x)^{-1}=g'\). Given \(g\in G^{h(x)}_{h(x)}\), put \(c=h(\theta_1(x))\theta(h(x))^{-1}\in
G^{h(x)}_{h(x)}\); for \(g_1=\theta_1(x)k(c^{-1}gc)\theta_1(x)^{-1}\in(G_1)^x_x\) we get, using \(h(k(g'))=
\theta(h(x))^{-1}g'\theta(h(x))\), that \(h(g_1)=c\,(c^{-1}gc)\,c^{-1}=g\).

*Injectivity.* If \(T_{h(x)}=0\) off a \(\Lambda_1\)-negligible set, then \(\{y:T_y\neq0\}\) is \(h(\Lambda_1)\)-negligible
(Lemma 7.4), hence \(\Lambda\)-negligible.

*Surjectivity.* Let \(S\in\operatorname{End}_G(h^*H)\) represent a given random operator, and define
\(T_y=U(\theta(y))S_{k(y)}U(\theta(y))^{-1}\) (note \((h^*H)_{k(y)}=H_{h(k(y))}\)). \(T\) is measurable; for
\(\gamma:y\to y'\), using \(\gamma\theta(y)=\theta(y')h(k(\gamma))\) and the intertwining of \(S\) at \(k(\gamma)\),
\[
U(\gamma)T_yU(\gamma)^{-1}=U(\theta(y'))\,U(h(k(\gamma)))S_{k(y)}U(h(k(\gamma)))^{-1}\,U(\theta(y'))^{-1}=T_{y'}.
\]
If \(S\) is changed on a \(\Lambda_1\)-negligible saturated \(N\), \(T\) changes on \(k^{-1}(N)\), and
\(h^{-1}(k^{-1}(N))=N\) because \(k(h(x))\sim x\); so \(k^{-1}(N)\) is \(h(\Lambda_1)\)-negligible (Lemma 7.4), hence
\(\Lambda\)-negligible. Finally, intertwining at \(\theta_1(x):k(h(x))\to x\) gives \(S_{k(h(x))}=U(h(\theta_1(x)))^{-1}S_x
U(h(\theta_1(x)))\), so
\[
T_{h(x)}=U(\theta(h(x)))U(h(\theta_1(x)))^{-1}S_xU(h(\theta_1(x)))U(\theta(h(x)))^{-1}=U(c)^{-1}S_xU(c)
\]
with \(c\) as above. Since \(c=h(g_1)\) with \(g_1\in(G_1)^x_x\) and \(S\) intertwines at \(g_1\), \(S_x\) commutes with
\(U(c)\), so \((h^*T)_x=S_x\) for every \(x\). \(\square\)

**Example 7.6 (semi-finiteness is not enough).** Definition 6.1 and the remarks after it use no finiteness of
\(\Lambda\): \(\operatorname{End}_\Lambda(H)\) is a C\(^*\)-algebra for every transverse measure. It need not be a
W\(^*\)-algebra. Let \(G=G^{(0)}=[0,1]\) with its Borel sets, a groupoid with only units; (S) and (F) hold. Proper
transverse functions are \(\nu^x=a(x)\varepsilon_x\) with \(a\ge0\) finite and Borel (Example 4.10(b)), and
\(\Lambda(\nu)=\sum_{x\in[0,1]}a(x)\) is a transverse measure of modulus \(1\): it is additive, homogeneous and normal
(monotone convergence for sums), and the modulus condition is empty because the only kernel \(\rho\) with
\(\rho^y(G)=1\) is \(\rho^y=\varepsilon_y\). It is semi-finite, since \(\Lambda(\nu)\) is the supremum of
\(\Lambda((1_F\circ s)\nu)=\sum_{x\in F}a(x)\) over finite \(F\), and it is not \(\sigma\)-finite, since for \(a=1\) a set
of finite \(\Lambda_\nu\)-measure is finite. For faithful \(\nu\) (\(a>0\)) a set is \(\Lambda_\nu\)-null only if it is
empty, so no nonempty set is negligible. Take \(H=\mathbf 1\), which is square integrable (Example 4.10(b)). Then
\(\operatorname{End}_\Lambda(\mathbf 1)\) is the algebra \(\mathcal B_b\) of bounded Borel functions on \([0,1]\) with the
supremum norm. Its projections are the indicators \(1_B\), \(B\) Borel. Let \(S\subset[0,1]\) be a set that is not
Borel, and consider the increasing net of projections \(1_F\), \(F\subset S\) finite. If it had a least upper bound
\(1_B\) in \(\mathcal B_b\), then \(B\supset S\); and for \(x\in B\setminus S\), \(1_{B\setminus\{x\}}\) would be a smaller
upper bound. So \(B=S\), which is not Borel. By (B4)(vi), \(\mathcal B_b\) is not a W\(^*\)-algebra.

*Reference:* [Connes 1979, Section V, Theorem 2] states that \(\operatorname{End}_\Lambda(H)\) is a von Neumann algebra
for every semi-finite transverse measure \(\Lambda\); this fails by the example above, so we assume
\(\sigma\)-finiteness.

## 8. Centre, factors and type I

In this section \((G,\mathcal B)\) is standard Borel and \(\Lambda\) is a \(\sigma\)-finite transverse measure of modulus
\(\delta\). We say that \(G\) has *trivial isotropy \(\Lambda\)-almost everywhere* if there is a \(\Lambda\)-negligible
saturated measurable set \(N\) with \(G^y_y=\{y\}\) for all \(y\notin N\). For a bounded measurable function \(a\) on
\(G^{(0)}\) that is constant on orbits, \((a(x)1_{H_x})\) is an intertwiner commuting with every intertwiner; its class
is central in \(\operatorname{End}_\Lambda(H)\). We call these the *invariant scalar* random operators. A
\(\Lambda\)-random Hilbert space is *nonzero* if \(\{x:H_x\neq0\}\) (a saturated measurable set) is not negligible.

**Corollary 8.1 (the centre).** If \(G\) has trivial isotropy \(\Lambda\)-almost everywhere, the centre of
\(\operatorname{End}_\Lambda(H)\) consists of the invariant scalar random operators, for every \(\Lambda\)-random
Hilbert space \(H\).

*Proof.* Let \(Z\) be central, with a representative in \(\operatorname{End}_G(H)\), and let \(\nu\) be faithful and
\(D\) as in Proposition 5.1. For \(\xi,\eta\in D\), \(Z\) commutes with the class of \(\theta_\nu(\xi,\eta)\), so the
fibres commute off a negligible saturated set. Off the union \(N'\) of these countably many sets and of \(N\), \(Z_x\)
commutes with the weakly dense algebra \(\mathcal A_x\) of Proposition 5.1, so \(Z_x=a(x)1\). On
\(\{x\notin N':H_x\neq0\}\) put \(a(x)=\langle Z_xe^1_x,e^1_x\rangle\) (\(e^1\) the first orthonormal section of (B1)(ii)),
and \(a=0\) elsewhere. Then \(a\) is measurable and bounded, and constant on orbits since \(Z_y=U(\gamma)Z_xU(\gamma)^{-1}\)
and \(N'\) is saturated. \(\square\)

This proof uses neither the \(\sigma\)-finiteness of \(\Lambda\) nor Section 7: Corollary 8.1 holds for every
transverse measure, \(\operatorname{End}_\Lambda(H)\) being then regarded as a C\(^*\)-algebra.

**Corollary 8.2 (factors).** Suppose \(G\) has trivial isotropy \(\Lambda\)-almost everywhere and \(\Lambda\neq0\). The
following are equivalent.

1. \(\operatorname{End}_\Lambda(H)\) is a factor for every nonzero \(\Lambda\)-random Hilbert space \(H\).
2. \(\operatorname{Hom}_\Lambda(H_1,H_2)\neq\{0\}\) whenever \(H_1,H_2\) are nonzero.
3. \(W(\nu)\) is a factor for some faithful \(\nu\in\mathcal E^+\).
4. \(\Lambda\) is *ergodic*: for every measurable saturated \(A\), either \(A\) or \(G^{(0)}\setminus A\) is
   \(\Lambda\)-negligible.
5. \(\Lambda\) is *extremal*: if \(\Lambda=\Lambda_1+\Lambda_2\) with \(\Lambda_1,\Lambda_2\) transverse measures of
   modulus \(\delta\), then \(\Lambda_1=c\Lambda\) for a constant \(c\ge0\).

The implications 2 \(\Rightarrow\) 4, 1 \(\Rightarrow\) 3 \(\Rightarrow\) 5 \(\Rightarrow\) 4 and 1 \(\Rightarrow\) 2 hold without
the isotropy hypothesis.

*Proof.* 1 \(\Rightarrow\) 2. Let \(H=H_1\oplus H_2\) and \(P_i\) the projections onto \(H_i\), nonzero in the factor
\(\operatorname{End}_\Lambda(H)\). If \(P_2\operatorname{End}_\Lambda(H)P_1=0\), the central support of \(P_1\) would be
orthogonal to \(P_2\), which is impossible in a factor. So some \(P_2TP_1\neq0\), and it defines a nonzero element of
\(\operatorname{Hom}_\Lambda(H_1,H_2)\).

2 \(\Rightarrow\) 4. If \(A\) and its complement are not negligible, let \(\nu\) be faithful and \(H_1\), \(H_2\) the
subrepresentations of \(L^\nu\) given by the projections \(1_A(x)1\) and \(1_{G^{(0)}\setminus A}(x)1\) (in
\(\operatorname{End}_G(L^\nu)\) since \(A\) is saturated). They are nonzero, and every intertwiner \(H_1\to H_2\) vanishes,
since in each fibre one of the two spaces is \(0\).

1 \(\Rightarrow\) 3. Take a faithful \(\nu\). By Theorem 7.1, \(\operatorname{End}_\Lambda(L^\nu)\cong W(\nu)'\) on
\(\mathfrak h_\nu\); it is a factor by 1 (\(L^\nu\) is nonzero because \(\Lambda\neq0\)), so \(W(\nu)\) is a factor.

3 \(\Rightarrow\) 5. Let \(\Lambda=\Lambda_1+\Lambda_2\) and \(\nu\) be as in 3, \(\mu=\Lambda_\nu\), \(m=m_\nu\). Since
\((\Lambda_1)_\nu\le\mu\) and \(\mu\) is \(\sigma\)-finite, \((\Lambda_1)_\nu=\varphi\mu\) with \(0\le\varphi\le1\) Borel,
and \((\Lambda_1)_\nu\circ\nu=(\varphi\circ r)m\). Applying (1.1) to \(\Lambda_1\) and to \(\Lambda\) (with \(h(\gamma)=
F(\gamma)\varphi(s(\gamma))\) in the latter),
\[
\int F(\gamma^{-1})\varphi(r(\gamma))\,dm=\int F\delta^{-1}\varphi\circ r\,dm,\qquad
\int F(\gamma^{-1})\varphi(r(\gamma))\,dm=\int F\delta^{-1}\varphi\circ s\,dm
\]
for \(F\ge0\). Taking \(F=\delta1_E\) with \(m(E)<\infty\) gives \(\int_E(\varphi\circ s-\varphi\circ r)\,dm=0\) for all
such \(E\); so \(\varphi\circ s=\varphi\circ r\) \(m\)-almost everywhere. Hence for \(f\in\mathcal A_\nu\) the functions
\((\varphi\circ s)f\) and \((\varphi\circ r)f\) of \(\mathcal A_\nu\) coincide \(m\)-almost everywhere, and by Proposition
6.2(b) and Lemma 6.5,
\[
\lambda_\nu(f)M_{\varphi\circ r}=\lambda_\nu((\varphi\circ s)f)=\lambda_\nu((\varphi\circ r)f)=M_{\varphi\circ r}\lambda_\nu(f),
\]
the first equality because \(((\varphi\circ s)f)*_\nu g=f*_\nu((\varphi\circ r)g)\). So \(M_{\varphi\circ r}\in W(\nu)'
\cap W(\nu)\) (Lemma 6.5), and it is scalar: \(\varphi\circ r=c\) \(m\)-almost everywhere. Since \(\nu^y\neq0\) for all
\(y\), \(\varphi=c\) \(\mu\)-almost everywhere, so \((\Lambda_1)_\nu=c\Lambda_\nu\) and \(\Lambda_1=c\Lambda\) by (R5).

5 \(\Rightarrow\) 4. If \(A\) is saturated, measurable, and neither \(A\) nor its complement is negligible, put
\(\Lambda_A(\nu')=\Lambda((1_A\circ s)\nu')\). It is additive, positively homogeneous and normal; it has modulus
\(\delta\) because \((1_A\circ s)\nu'=(1_A\circ r)\nu'\) and \(((1_A\circ r)\nu')*\delta\rho=(1_A\circ r)(\nu'*\delta\rho)\).
So \(\Lambda=\Lambda_A+\Lambda_{G^{(0)}\setminus A}\). For a faithful \(\nu\), \(\Lambda_A((1_{G^{(0)}\setminus A}\circ
s)\nu)=0<\Lambda((1_{G^{(0)}\setminus A}\circ s)\nu)\) and \(\Lambda_A(\nu)=\Lambda_\nu(A)>0\) (R6), so \(\Lambda_A\) is not
a multiple of \(\Lambda\).

4 \(\Rightarrow\) 1. By Corollary 8.1 the centre consists of invariant scalar operators \(a\). For each rational \(t\),
\(\{a>t\}\) is saturated, hence negligible or co-negligible; so \(a\) is constant off a negligible set, and the centre is
\(\mathbb C1\) (and \(\operatorname{End}_\Lambda(H)\neq0\) since \(H\) is nonzero). \(\square\)

Without the isotropy hypothesis 4 does not imply 1: for a locally compact group \(G\) (one unit), every \(\Lambda\) is
ergodic, while \(W(\nu)\) is the group von Neumann algebra, which is not a factor for \(G=\mathbb Z\).

**Corollary 8.3 (type I).** Suppose \(G\) has trivial isotropy \(\Lambda\)-almost everywhere. The following are
equivalent.

1. There is a \(\Lambda\)-random Hilbert space \(H\), with \(H_x\neq0\) for \(\Lambda\)-almost every \(x\) (that is,
   off a negligible saturated set), such that \(\operatorname{End}_\Lambda(H)\) is of type I.
2. \(\operatorname{End}_\Lambda(H)\) is of type I for every \(\Lambda\)-random Hilbert space \(H\).
3. There is a measurable saturated \(A\subset G^{(0)}\) with negligible complement such that the trivial
   representation \(\mathbf 1\) of the reduced groupoid \(G_A=r^{-1}(A)\) is square integrable.
4. There is a bounded \(\nu'\in\mathcal E^+\) (\(\sup_y\nu'^y(G)<\infty\)) whose support has negligible complement.

*Proof.* 2 \(\Rightarrow\) 1. Take \(H=L^\nu\) with \(\nu\) faithful.

1 \(\Rightarrow\) 3. Let \(P\) be an abelian projection of \(\operatorname{End}_\Lambda(H)\) with central support \(1\) (B4)(v).
The set \(E=\{x:P_x\neq0\}\) is saturated and \(P\le1_E(x)1\), a central projection; so \(1_E(x)1=1\) in
\(\operatorname{End}_\Lambda(H)\), and since \(H_x\neq0\) almost everywhere, the complement of \(E\) is negligible. Let
\(H'=PH\); then \(\operatorname{End}_\Lambda(H')\cong P\operatorname{End}_\Lambda(H)P\) is abelian, so it equals its
centre, which consists of invariant scalar operators (Corollary 8.1). Let \(\nu\) be faithful and \(D\) as in Proposition
5.1 for \(H'\). Off a negligible saturated set \(N'\supset N\), every \(\theta_\nu(\xi,\eta)_x\), \(\xi,\eta\in D\), is a
scalar, and they span a weakly dense subalgebra of \(B(H'_x)\); so \(\dim H'_x\le1\), with equality on
\(A=E\setminus N'\). On the saturated set \(A\), let \(e_x\) be a measurable unit section of \(H'\) and \(\{\xi^n\}\subset
D\) a total set; \(b_n(x)=|\langle\xi^n_x,e_x\rangle|\) are bounded measurable, for each \(x\in A\) some \(b_n(x)\neq0\),
and \(|\langle\alpha,U'(\gamma)\xi^n_{s(\gamma)}\rangle|=|\alpha|\,b_n(s(\gamma))\) for \(\alpha\in H'_y=\mathbb Ce_y\).
So (4.1) for \(\xi^n\) says exactly that \(b_n\in D(\mathbf 1,\nu|_{G_A})\), and these are total: \(\mathbf 1\) is square
integrable on \(G_A\) (the restriction of \(\nu\) to \(A\) is a faithful proper transverse function on \(G_A\)).

3 \(\Rightarrow\) 4. Let \(\nu\) be faithful and \(\{b_n\}\subset D(\mathbf 1,\nu|_{G_A})\) total, with constants \(c_n\) in
(4.1): \(\int|b_n(s(\gamma))|^2\,d\nu^y(\gamma)\le c_n^2\) for \(y\in A\), and for each \(x\in A\) some \(b_n(x)\neq0\).
Put \(\phi=\sum_n2^{-n}(1+c_n^2+\|b_n\|_\infty^2)^{-1}|b_n|^2\) on \(A\), a finite positive function, and \(\phi=0\) off \(A\). Then \(\nu'=(\phi\circ s)\nu\in\mathcal E^+\)
satisfies \(\nu'^y(G)\le1\), and \(\nu'^y\neq0\) exactly for \(y\in A\).

4 \(\Rightarrow\) 2. Write \(A\) for the support of \(\nu'\), and put \(a(x)=\nu'^x(G)^{-1}\) for \(x\in A\), \(a=0\) off
\(A\).
Since \(\nu'^x(G)\) is constant on orbits, \(\nu_1=(a\circ s)\nu'\in\mathcal E^+\) has \(\nu_1^y(G)=1\) for \(y\in A\). Let
\(\nu_0\) be faithful and \(\hat\nu=\nu_1+(1_{G^{(0)}\setminus A}\circ s)\nu_0\), a faithful element of \(\mathcal E^+\).
In \(L^{\hat\nu}\), let \(P_x\) be the projection onto the constant functions in \(L^2(G,\nu_1^x)=L^2(G,\hat\nu^x)\) for
\(x\in A\), and \(P_x=0\) for \(x\notin A\). Since left translations fix constants and \(A\) is saturated, \(P\in
\operatorname{End}_G(L^{\hat\nu})\) (measurable because \(P_xq=\langle q,1\rangle1\) and \(1_A(r(\gamma))\) is a bounded
section). The subrepresentation \(PL^{\hat\nu}\) has one-dimensional fibres on \(A\) on which \(G\) acts trivially, so
its random operators are invariant scalar functions: \(P\operatorname{End}_\Lambda(L^{\hat\nu})P\) is abelian. By
Corollary 8.1 the central support of \(P\) is some \(1_E(x)1\) with \(E\) saturated; as \(P\le1_E\), \(E\supset A\) up to a
negligible set, so the central support is \(1\). Hence \(\operatorname{End}_\Lambda(L^{\hat\nu})\) is of type I, and so is
\(\operatorname{End}_\Lambda(\infty\cdot L^{\hat\nu})\), in which \(P\otimes e_{11}\) is abelian with central support \(1\)
by the same argument. For any \(H\), Theorem 4.4 gives \(V:H\to\infty\cdot L^{\hat\nu}\) with isometric fibres, and
\(T\mapsto VTV^*\) identifies \(\operatorname{End}_\Lambda(H)\) with the corner \(Q\operatorname{End}_\Lambda(\infty\cdot
L^{\hat\nu})Q\), \(Q=VV^*\), which is of type I (B4)(v). \(\square\)

**Proposition 8.4 (smooth orbit spaces).** Suppose \(G\) has trivial isotropy \(\Lambda\)-almost everywhere. Condition
4 of Corollary 8.3 holds if and only if there are a measurable saturated \(A\) with negligible complement and a Borel set
\(T\subset A\) meeting every orbit contained in \(A\) in exactly one point.

*Proof.* *If.* Removing the negligible set \(N\), we may assume trivial isotropy on \(A\). Let \(\Gamma=\{\gamma:
r(\gamma)\in A,\ s(\gamma)\in T\}\), a Borel set. For \(y\in A\) there is exactly one \(\gamma\in\Gamma\cap G^y\): its
source is the point of \(T\) in the orbit of \(y\), and two arrows with the same source and range differ by an element of
the trivial isotropy group. So \(r|_\Gamma\) is a Borel bijection onto \(A\), and by (B6) its inverse \(\tau\) is Borel.
Put \(\nu'^y=\varepsilon_{\tau(y)}\) for \(y\in A\) and \(\nu'^y=0\) otherwise. Then \(y\mapsto\nu'^y(E)=1_E(\tau(y))1_A(y)\)
is measurable, and for \(\gamma:x\to y\) in \(A\), \(\gamma\tau(x)\in\Gamma\cap G^y\), so \(\gamma\tau(x)=\tau(y)\) and
\(\gamma\nu'^x=\nu'^y\). This \(\nu'\) is bounded (hence proper) with support \(A\).

*Only if.* As in the proof of 4 \(\Rightarrow\) 2 above, we get \(\nu_1\in\mathcal E^+\) with \(\nu_1^y(G)=1\) for \(y\) in a
saturated set \(A'\) with negligible complement, and we may assume trivial isotropy on \(A'\). For \(y\in A'\) let
\(p_y=s_*(\nu_1^y)\), a probability measure on \(G^{(0)}\). The map \(P:y\mapsto p_y\) from \(A'\) to the standard Borel
space \(\operatorname{Prob}(G^{(0)})\) (B6) is Borel, and constant on orbits since \(\gamma\nu_1^x=\nu_1^y\) and
\(s(\gamma\gamma')=s(\gamma')\). It separates orbits: the orbit \([y]=s(G^y)\) is analytic, hence universally
measurable, and \(p_y([y])\ge\nu_1^y(G^y)=1\); so \(p_x=p_y\) forces \([x]\cap[y]\neq\emptyset\). By the Jankov–von
Neumann uniformization theorem applied to the graph of \(P\), there is a universally measurable \(\sigma\) on the analytic
set \(P(A')\) with \(P(\sigma(q))=q\); extend it by a constant to a universally measurable map on
\(\operatorname{Prob}(G^{(0)})\). If \(\Lambda=0\), every saturated Borel set is negligible, and \(A''=T=\emptyset\) will do.
Otherwise let \(\mu_0\) be a probability measure on \(A'\) equivalent to the restriction of \(\Lambda_{\hat\nu}\) to
\(A'\), for a faithful \(\hat\nu\); it exists because \(\Lambda_{\hat\nu}\) is \(\sigma\)-finite and nonzero and
\(G^{(0)}\setminus A'\) is \(\Lambda_{\hat\nu}\)-null. By (B6), \(\sigma\) coincides with a Borel map \(\sigma'\) off a \(P_*\mu_0\)-null Borel set, so
\(Q_1=\{q:\sigma'(q)\in A',\ P(\sigma'(q))=q\}\) is a Borel set of full \(P_*\mu_0\)-measure. Then \(A''=P^{-1}(Q_1)\) is
saturated, Borel, and \(\mu_0(A'\setminus A'')=0\), so \(G^{(0)}\setminus A''\) is negligible (R6). The Borel set
\(T=\{y\in A'':\sigma'(P(y))=y\}\) meets the orbit of each \(y\in A''\) in the point \(\sigma'(P(y))\), and only there,
because two points of \(T\) in one orbit have the same image under \(P\). \(\square\)

**Proposition 8.5.** Suppose \(G\) has trivial isotropy \(\Lambda\)-almost everywhere, and let \(M=\operatorname{End}_
\Lambda(H)\) be a properly infinite factor. There are a normal unital injective \(*\)-endomorphism \(\sigma\) of \(M\) and a
unitary \(S\in M\) with \(S^2=1\) such that, with \(\sigma_S(x)=S\sigma(x)S^*\),
\[
\sigma_S(M)=\sigma(M)'\cap M\qquad\text{and}\qquad\sigma(M)=\sigma_S(M)'\cap M .
\]

*Proof.* *Step 1: \(H\cong H\otimes H\).* Let \(E=\{x:H_x\neq0\}\). For a saturated \(A\), \(1_A(x)1\) is a central
projection of \(M\), hence \(0\) or \(1\); so \(A\cap E\) or \(E\setminus A\) is negligible. The representation \(H\otimes H\)
is square integrable (Proposition 4.6) and nonzero exactly on \(E\). Let \(K=H\oplus(H\otimes H)\) and
\(\mathcal N=\operatorname{End}_\Lambda(K)\). By Corollary 8.1 its centre consists of invariant scalar functions, which
are constant off a negligible set on \(E\) and irrelevant off \(E\); so \(\mathcal N\) is a factor, with separable predual
(Theorem 7.2). The map \(\iota(T)=(T_x\otimes1)\) is a unital injective normal \(*\)-homomorphism from \(M\) into
\(\operatorname{End}_\Lambda(H\otimes H)\) (normality as in Corollary 7.5(b)). Let \(P_1,P_2\) be the projections of
\(\mathcal N\) onto \(H\) and \(H\otimes H\). \(P_1\mathcal NP_1\cong M\) is properly infinite, so \(P_1\) is infinite; if
\(v\in M\) is a non-unitary isometry, \(\iota(v)\) is a non-unitary isometry in \(P_2\mathcal NP_2\cong\operatorname{End}_
\Lambda(H\otimes H)\), so \(P_2\) is infinite. By (B4)(v), \(P_1\) and \(P_2\) are equivalent in \(\mathcal N\), which gives
a random operator \(W\in\operatorname{Hom}_\Lambda(H,H\otimes H)\) with \(W^*W=1\), \(WW^*=1\).

*Step 2: \(\sigma\) and \(S\).* The flip \(\Sigma_x(a\otimes b)=b\otimes a\) is a self-adjoint unitary in
\(\operatorname{End}_G(H\otimes H)\) (it maps \(\xi^n\otimes\xi^m\) to \(\xi^m\otimes\xi^n\) and commutes with
\(U(\gamma)\otimes U(\gamma)\)), and \(\Sigma(T\otimes1)\Sigma=1\otimes T\). Put \(\sigma(T)=W^*\iota(T)W\) and \(S=W^*\Sigma W\).
Then \(S=S^*\), \(S^2=1\), and \(\sigma_S(T)=W^*(1\otimes T)W\).

*Step 3: relative commutants.* It suffices to show \(\iota(M)'\cap\operatorname{End}_\Lambda(H\otimes H)=\{1\otimes T:
T\in M\}\); the other identity follows by conjugating with \(\Sigma\). Clearly \(1\otimes T\) commutes with \(\iota(M)\).
Conversely let \(Z\) commute with \(\iota(M)\), and let \(D\) be as in Proposition 5.1 for \(H\) and a faithful \(\nu\). Off
a negligible saturated set \(N'\supset N\), \(Z_x\) commutes with \(\theta_\nu(\xi,\eta)_x\otimes1\) for all
\(\xi,\eta\in D\), hence with \(B(H_x)\otimes1\); so \(Z_x=1\otimes Z'_x\) for a unique \(Z'_x\in B(H_x)\) when
\(H_x\neq0\). Put \(\langle Z'_xa,b\rangle=\langle Z_x(e^1_x\otimes a),e^1_x\otimes b\rangle\) for \(x\in E\setminus N'\)
and \(Z'_x=0\) otherwise: \(Z'\) is measurable, and conjugating \(Z_x=1\otimes Z'_x\) by \(U(\gamma)\otimes U(\gamma)\)
shows that \(Z'\) is an intertwiner. So \(Z=1\otimes Z'\) in \(\operatorname{End}_\Lambda(H\otimes H)\). Conjugating by
\(W\) gives the two identities. \(\square\)

**Remark 8.6.** Proposition 8.5 exhibits \(M\) as containing a pair of mutually commuting copies of itself, exchanged by
the symmetry \(S\), each the relative commutant of the other. [Connes 1979] states in addition that
\(\sigma(M)\) and \(\sigma_S(M)\) generate \(M\), with the proof left to the reader; that part is not proved in this
lesson. The tensor product \(H\otimes H\) of random Hilbert spaces is what makes the construction possible: as
[Connes 1979] points out, an abstract isomorphism \(M\cong M\bar\otimes M\) would not suffice, because the flip of
\(M\bar\otimes M\) is inner only when \(M\) is of type I.

## 9. Exercises

**Exercise 9.1 (the averaged cyclic projection can be smaller).** Let \(G=X\times X\) be the pair groupoid of the
two-point set \(X=\{1,2\}\) (all subsets measurable), with \(r(y,x)=y\), \(s(y,x)=x\). Let \(\nu^y=\varepsilon_{(y,1)}\),
let \(H=\mathbf 1\), and let \(\xi_1=0\), \(\xi_2=1\). Show that \(\nu\) is a faithful proper transverse function, and
compute \(P^\xi\), \(P^{\nu,\xi}\) and \(\xi'=P^{\nu,\xi}\xi\) of Section 2.4. Check Proposition 2.7(b).

*Solution.* For \(\gamma=(y,x)\), \(\gamma\nu^x=\varepsilon_{(y,x)(x,1)}=\varepsilon_{(y,1)}=\nu^y\); the masses are \(1\), so
\(\nu\) is bounded, hence proper, and faithful. \(P^\xi_y\) is the projection onto the span of \(U(y,1)\xi_1=0\) and
\(U(y,2)\xi_2=1\), so \(P^\xi=1\). Since \(\nu^y\) is the unit mass at \((y,1)\), \(N^{\nu,\xi}_y=\{\alpha:\langle\alpha,
\xi_1\rangle=0\}=\mathbb C\), so \(P^{\nu,\xi}=0\) and \(\xi'=0\). Indeed \(\xi'_{s(\gamma)}=\xi_{s(\gamma)}\) for
\(\nu^y\)-almost every \(\gamma\), because \(s(\gamma)=1\) there, and \(P^{\xi'}=0=P^{\nu,\xi}\). So \(P^{\nu,\xi}\) can be
strictly smaller than \(P^\xi\): it only sees the values of \(\xi\) on the part of each orbit charged by \(s(\nu^y)\).

**Exercise 9.2 (compact groups).** Let \(G\) be a compact second countable group with Haar probability \(\nu\), and \(U\) an
irreducible representation on \(\mathbb C^d\). Show that \(D(U,\nu)=\mathbb C^d\), that \(\theta_\nu(\xi,\xi)=
(\|\xi\|^2/d)\,1\), and that \(\mathcal J_\nu=\mathbb C1=\operatorname{End}_G(\mathbb C^d)\).

*Solution.* \(\int|\langle\alpha,U(g)\xi\rangle|^2\,dg\le\|\alpha\|^2\|\xi\|^2\), so (4.1) holds for every \(\xi\). By (4.2),
\(\theta_\nu(\xi,\xi)=\int U(g)\xi\xi^*U(g)^*\,dg\), which commutes with every \(U(h)\) by invariance of the Haar measure;
by Schur's lemma it is a scalar \(c\). Taking traces, \(cd=\int\|U(g)\xi\|^2\,dg=\|\xi\|^2\). By polarization
\(\mathcal J_\nu\) is spanned by the \(\theta_\nu(\xi,\xi)\), so \(\mathcal J_\nu=\mathbb C1\), which is all of
\(\operatorname{End}_G(\mathbb C^d)\) by Schur's lemma.

**Exercise 9.3 (the classical case).** Let \(G=G^{(0)}=X\) be a standard Borel space, viewed as a groupoid with only
units, \(\nu^x=\varepsilon_x\), and \(\Lambda\) a transverse measure with \(\Lambda_\nu=\mu\) \(\sigma\)-finite. Show that
\(\mathfrak h_\nu=L^2(X,\mu)\), that \(W(\nu)=L^\infty(X,\mu)\), and that Theorem 7.1(c) reduces to the statement of
(B2) that the commutant of the diagonal algebra is the algebra of decomposable operators.

*Solution.* Every modulus is \(1\) on units, so \(\delta=1\). Here \(G^y=\{y\}\), so \(m_\nu=\mu\), \((f*_\nu g)(x)=
f(x)g(x)\), \(f^\#=\bar f\) and \(J g=\bar g\). \(\mathcal A_\nu\) consists of the functions \(f\in L^2(\mu)\) that are
bounded (\(\|f\|_\nu=\sup|f|\)), and \(\lambda_\nu(f)\) is multiplication by \(f\). The von Neumann algebra generated by
multiplications by bounded \(L^2\) functions is \(L^\infty(\mu)\), because \(\mu\) is \(\sigma\)-finite (the indicators of
sets of finite measure increase to \(1\)). A representation of \(X\) is a measurable field \(H\), every field is square
integrable (Example 4.10(b)), intertwiners are bounded measurable fields of operators, and negligible sets are
\(\mu\)-null sets. Since \((U(f\nu)\xi)_x=f(x)\xi_x\), \(\pi^H_\nu(W(\nu))\) is the diagonal algebra of
\(\int^\oplus H_x\,d\mu\), and Theorem 7.1(c) says that its commutant consists of the decomposable operators.

**Exercise 9.4 (products of \(\theta\)'s).** Let \(\xi,\eta,\xi',\eta'\in D(U,\nu)\). Using only Definition 4.1, show that
\(\theta_\nu(\xi,\eta)\theta_\nu(\xi',\eta')=\theta_\nu(\theta_\nu(\xi,\eta)\xi',\eta')\), and deduce that the span of
\(\{\theta_\nu(\xi,\eta):\xi,\eta\in D\}\) is an algebra whenever \(D\subset D(U,\nu)\) is stable under
\((\xi,\eta,\zeta)\mapsto\theta_\nu(\xi,\eta)\zeta\).

*Solution.* For \(A=\theta_\nu(\xi,\eta)\in\operatorname{End}_G(H)\), \(A\xi'\in D(U,\nu)\) and
\(T_\nu(A\xi')=T_\nu(\xi')A^*\), both by the computation \(\langle\alpha,U(\gamma)A\xi'_{s(\gamma)}\rangle=
\langle A^*\alpha,U(\gamma)\xi'_{s(\gamma)}\rangle\). Hence \(\theta_\nu(A\xi',\eta')=(T_\nu(\xi')A^*)^*T_\nu(\eta')=
A\,\theta_\nu(\xi',\eta')\). A product of two spanning elements is therefore again a spanning element, and the span is
closed under products.

## References



- [Connes 1979] A. Connes, Sur la théorie non commutative de l'intégration, in: Algèbres d'opérateurs (Sém.,
  Les Plans-sur-Bex, 1978), Lecture Notes in Math. 725, Springer, Berlin, 1979, 19–143. Free at https://alainconnes.org/wp-content/uploads/ThNonComm.pdf
- [Connes 1982] A. Connes, A survey of foliations and operator algebras, in: Operator algebras and applications,
  Part I (Kingston, Ont., 1980), Proc. Sympos. Pure Math. 38, Amer. Math. Soc., Providence, RI, 1982, 521–628. Free at https://alainconnes.org/wp-content/uploads/foliationsfine.pdf
- [Connes 1994] A. Connes, Noncommutative geometry, Academic Press, San Diego, CA, 1994.
  https://alainconnes.org/publications/
- [Mackey 1957] G. W. Mackey, Borel structure in groups and their duals, Trans. Amer. Math. Soc. 85 (1957), 134–165.
  https://doi.org/10.1090/S0002-9947-1957-0089999-2. Free at https://www.ams.org/journals/tran/1957-085-01/S0002-9947-1957-0089999-2/

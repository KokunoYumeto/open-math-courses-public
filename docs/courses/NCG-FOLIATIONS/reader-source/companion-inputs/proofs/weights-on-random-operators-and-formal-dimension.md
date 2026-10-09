# Weights on random operators and formal dimension

*Mathematical additions by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

On a measure space, a positive function \(\rho\) turns into a measure \(\rho\,d\mu\), and integrating the constant
function \(1\) against it gives a number. This lesson does the same thing on the "space of orbits" of a measured
groupoid, where functions are replaced by random operators. The earlier lessons of this course built the pieces:
a measurable groupoid \(G\), a transverse measure \(\Lambda\) of modulus \(\delta\), square-integrable
representations (random Hilbert spaces) \(H\), and the von Neumann algebra \(\operatorname{End}_\Lambda(H)\) of
random operators. Here we attach to every positive random operator \(T\) of degree one a normal semifinite weight
\(\varphi_T\) on \(\operatorname{End}_\Lambda(H)\). Heuristically
\[
\varphi_T(A)=\int\operatorname{Trace}(T_xA_x)\,d\Lambda(x),
\]
an integral over the orbit space of a function that is only defined up to the transformation rule of \(T\). The
weight is characterized by its values on the "continuous sums of rank-one operators" \(\theta_\nu(\xi,\xi)\), and every
normal semifinite weight arises this way (Theorem 5.3).

The main results are the following.

1. The map \(T\mapsto\varphi_T\) is a bijection from positive random operators of degree one onto normal semifinite
   weights on \(\operatorname{End}_\Lambda(H)\). For nonsingular \(T\), which give the faithful weights, the modular
   group of \(\varphi_T\) is \(\operatorname{Ad}T_x^{it}\), and cocycle derivatives are quotients
   \(T_{2,x}^{it}T_{1,x}^{-it}\) (Section 5).
2. An operator-valued weight \(E_\nu\) from the direct integral of the algebras \(\mathcal L(H_x)\) onto
   \(\operatorname{End}_\Lambda(H)\) is the average along orbits, and \(\varphi_T\circ E_\nu\) is the weight
   \(\int\operatorname{Trace}(T_x\,\cdot\,)\,d\Lambda_\nu\) (Section 6).
3. When the isotropy groups are trivial and \(T\) is nonsingular, the modular spectrum of \(\varphi_T\) is read off from the spectra of the
   operators \(\log T_x\), and \(\varphi_T\) is a trace exactly when \(T_x\) is scalar (Section 7).
4. For nonsingular \(T\), the modular group of \(\varphi_T\) is integrable exactly when the \(T_x\) have absolutely continuous spectrum (for
   diagonal \(T\)); its centralizer is then an algebra of random operators on the stable kernel of \(\delta\) (Section
   8).
5. Integration formulas: \(\varphi_T(1)=\int F_T\,d\Lambda\) for an explicit random variable \(F_T\), a
   Hilbert–Schmidt formula for convolution operators, and invariance under proper homomorphisms (Section 9).
6. When \(\delta=1\), the formal dimension \(\dim_\Lambda H=\varphi_1(1)\) of a random Hilbert space: additivity,
   invariance, agreement with the formal degree and with the Murray–von Neumann dimension for unimodular groups, and
   the value \(\Lambda(\nu_T)\) for a transversal (Section 10).
7. The index \(\operatorname{Ind}_\Lambda\) of a random Fredholm operator, a real number that is additive, locally
   constant and invariant under \(\Lambda\)-compact perturbations (Section 11).

Items 6 and 7 are what make the theory useful for index theory on foliations: the \(\Lambda\)-index of a leafwise
elliptic operator is a real number of exactly this kind.

**What is assumed.** The lesson relies on three earlier lessons of this course: "The spatial derivative",
"Measured groupoids and transverse measures" and "Square-integrable representations and random operators". Section 1
restates precisely what is used from them. It also uses Tomita–Takesaki theory, normal weights and the Connes cocycle
derivative, operator-valued weights, direct integrals, and the Arveson spectrum of a one-parameter automorphism group.
These are listed in Section 2, "Results used from other lessons", with the place where each is proved; the
Arveson spectrum (B4) and the facts on unimodular groups (B9) are proved there, from the lessons on harmonic analysis.

Basic references are [Connes 1979], [Connes 1980a], [Haagerup 1979] and [Connes 1994].

**Conventions.**

- Inner products are linear in the first variable. For a vector \(\xi\), \(\xi\xi^*\) is the rank-one operator
  \(\zeta\mapsto\langle\zeta,\xi\rangle\xi\). Hilbert spaces and measurable fields of Hilbert spaces are separable.
- Let \(T\) be positive and self-adjoint. For a vector \(\zeta\) we write \(\langle T\zeta,\zeta\rangle=
  \|T^{1/2}\zeta\|^2\) if \(\zeta\in\operatorname{dom}T^{1/2}\) and \(\langle T\zeta,\zeta\rangle=+\infty\) otherwise.
  \(T^{it}\) is defined by functional calculus with \(0^{it}=0\): a partial isometry with initial and final projection
  the support \(s(T)\), the projection onto \((\ker T)^\perp\). \(T\) is *nonsingular* if \(s(T)=1\).
- Weights are additive positively homogeneous maps \(A_+\to[0,\infty]\); *normal* means \(\varphi(\sup x_i)=
  \sup\varphi(x_i)\) for bounded increasing nets; *fns* abbreviates faithful normal semifinite. \(\sigma^\varphi\) is
  the modular group, \((D\varphi_2:D\varphi_1)_t\) the Connes cocycle derivative, \(s(\varphi)\) the support. A normal
  weight extends by normality to the extended positive part \(\widehat A_+\) (increasing limits of elements of
  \(A_+\)).
- **Standing assumptions.** \(G\) is a measurable groupoid whose Borel structure is standard, and \(G\) has a faithful
  proper transverse function (hypothesis (F) of the earlier lessons). \(\delta:G\to\mathbb R_+^*\) is a Borel
  homomorphism, and \(\Lambda\) is a *\(\sigma\)-finite* transverse measure of modulus \(\delta\) ("module
  \(\delta\)" in the lesson "Measured groupoids and transverse measures"). Then every measure \(\Lambda_\nu\) is
  \(\sigma\)-finite, every algebra \(\operatorname{End}_\Lambda(H)\) is a von Neumann algebra with separable predual,
  and in particular it has a faithful normal state. The lesson "Square-integrable representations and random
  operators" constructs \(\operatorname{End}_\Lambda(H)\) only for \(\sigma\)-finite \(\Lambda\), and Example 6.13 of
  "Measured groupoids and transverse measures" shows that semi-finite transverse measures can behave differently; so
  everything below is stated for \(\sigma\)-finite \(\Lambda\).

## 1. What we use from the earlier lessons

### 1.1 Transverse functions and transverse measures

The following is taught in "Measured groupoids and transverse measures"; the numbers in parentheses after each item
refer to that lesson.

**(R1) Kernels and transverse functions.** A kernel \(\lambda\) on \(G\) assigns to every \(y\in G^{(0)}\) a positive
measure \(\lambda^y\) on \(G^y=r^{-1}(y)\), measurably in \(y\) (and s-finitely). It is *proper* if \(G\) is an
increasing union of Borel sets \(A_n\) with \(\gamma\mapsto\lambda^{s(\gamma)}(\gamma^{-1}A_n)\) bounded. A *transverse
function* is a kernel \(\nu\) with \(\gamma\nu^x=\nu^y\) for all \(\gamma:x\to y\) (left invariance); \(\mathcal E^+\)
is the cone of proper transverse functions, stable under sums. \(\nu\) is *faithful* if \(\nu^y\neq0\) for all \(y\).
For \(\nu\in\mathcal E^+\) and a finite-valued Borel \(g\ge0\) on \(G^{(0)}\), \((g\circ s)\nu\in\mathcal E^+\). For
\(f\ge0\) on \(G\) we write \(\nu(f)(y)=\int f\,d\nu^y\) and \(\tilde f(\gamma)=f(\gamma^{-1})\). If \(\nu\) is faithful
there is a Borel \(g>0\) on \(G\) with \(\nu(g)=1\). If \(\nu_1,\nu_2\in\mathcal E^+\) and \(\nu_1^y\le\nu_2^y\) for all
\(y\), then \(\nu_1=(g\circ s)\nu_2\) for a Borel \(g\) on \(G^{(0)}\) with \(0\le g\le1\). (Definitions 1.3 and 2.1,
Lemma 2.2(d),(f), Lemma 2.4 and Proposition 2.7. Proposition 2.7 gives a finite \(g\) with \(\nu_1=(g\circ s)\nu_2\);
since \(\nu_1\le\nu_2\), \(g\circ s\le1\) holds \(\nu_2^y\)-almost everywhere for every \(y\), so \(\min(g,1)\) may
replace \(g\).)

**(R2) Transverse measures.** \(\Lambda:\mathcal E^+\to[0,\infty]\) is additive, positively homogeneous, normal and of
modulus \(\delta\). For \(\nu\in\mathcal E^+\), \(\Lambda_\nu(g)=\Lambda((g\circ s)\nu)\) (\(g\ge0\) finite) defines a
measure \(\Lambda_\nu\) on \(G^{(0)}\), and \(\Lambda_{(g\circ s)\nu}=g\Lambda_\nu\). The *modular relation*: for
\(\nu,\nu'\in\mathcal E^+\) and Borel \(f\ge0\) on \(G\),
\[
\int\!\!\int f(\gamma^{-1})\,d\nu'^y(\gamma)\,d\Lambda_\nu(y)=\int\!\!\int f(\gamma)\,\delta(\gamma)^{-1}\,d\nu^y(\gamma)
\,d\Lambda_{\nu'}(y). \tag{1.1}
\]
In particular the measure \(m_\nu=\Lambda_\nu\circ\nu\), \(m_\nu(f)=\int\nu^y(f)\,d\Lambda_\nu(y)\), satisfies
\(\int f(\gamma^{-1})\,dm_\nu(\gamma)=\int f(\gamma)\delta(\gamma)^{-1}\,dm_\nu(\gamma)\). (Definitions 3.1 and 3.2, Lemma
3.3, and Theorem 3.5 with \(\nu\) and \(\nu'\) exchanged.)

**(R3) Negligible sets.** A Borel set \(A\subset G^{(0)}\) is *saturated* if it is a union of orbits. A saturated Borel
set is \(\Lambda\)-negligible if it is \(\Lambda_\nu\)-null for every \(\nu\); if \(\nu\) is faithful this holds as
soon as \(\Lambda_\nu(A)=0\). For \(\nu\in\mathcal E^+\) and a Borel set \(Z\subset G^{(0)}\) with \(\Lambda_\nu(Z)=0\),
the set \([Z]_\nu=\{y:\nu^y(s^{-1}(Z))>0\}\) is a saturated Borel \(\Lambda\)-negligible set. (Definition 5.1 and
Proposition 5.2.)

**(R4) Random variables.** A random variable of modulus \(\delta\) is a measurable functor \(F\) from \(G\) to measured
spaces: a standard Borel space \(X=\bigsqcup_xF(x)\) with a Borel projection \(\pi:X\to G^{(0)}\), a Borel action
\((\gamma,z)\mapsto\gamma z\) of \(G\) on \(X\), and measures \(\alpha^x\) on \(F(x)\), measurable in \(x\), such that
\(X\) is an increasing union of Borel sets \(X_n\) with \(\sup_x\alpha^x(X_n)<\infty\), and \(\gamma_*\alpha^x=
\delta(\gamma)\alpha^y\) for \(\gamma:x\to y\). For \(f\ge0\) on \(X\), \((\nu*f)(z)=\int f(\gamma^{-1}z)\,
d\nu^{\pi(z)}(\gamma)\); it is a \(G\)-invariant function, and \(\nu*(\varphi f)=\varphi\,(\nu*f)\) for invariant
\(\varphi\ge0\). \(F\) is *proper* if \(\nu*f=1\) for some Borel \(f\ge0\) and some (equivalently every) faithful
\(\nu\); then one can take \(f>0\), and
\[
\int F\,d\Lambda=\int\alpha^x(f)\,d\Lambda_\nu(x)\qquad(\nu\text{ faithful},\ \nu*f=1)
\]
does not depend on the choices. The functor \(L\), \(x\mapsto G^x\) with left translations, is proper; so is every
sub-functor of \(\mathbb N\times L\) (a \(G\)-invariant Borel subset \(W\) of \(\mathbb N\times G\)): if \(\nu*k=1\) on
\(G\), then \(f(n,\gamma)=k(\gamma)1_W(n,\gamma)\) has \(\nu*f=1_W\). (Definitions 6.1, 6.2 and 6.8, Lemma 6.3(b),
Theorem 6.6(b),(c), Lemma 6.7 and Example 6.9.)

**(R5) Proper homomorphisms.** For a proper homomorphism \(h:G\to G'\) and a Borel homomorphism \(\delta'\) with
\(\delta'\circ h=\delta\), there is an image transverse measure \(h(\Lambda)\) of modulus \(\delta'\), the pull-back
\(h^*F'\) of a proper random variable \(F'\) on \(G'\) is proper, and \(\int h^*F'\,d\Lambda=\int F'\,d\,h(\Lambda)\).
(Definition 7.1, Lemma 7.3 and Theorem 8.2(a),(c).)

**(R6) The stable kernel of \(\delta\).** Write \(c=\log\delta:G\to\mathbb R\). The groupoid \(G'=G\times\mathbb R\)
has unit space \(G^{(0)}\times\mathbb R\), \(r(\gamma,s)=(r(\gamma),s)\), \(s(\gamma,s)=(s(\gamma),s+c(\gamma))\) and
product \((\gamma_1,s_1)(\gamma_2,s_1+c(\gamma_1))=(\gamma_1\gamma_2,s_1)\). The map \(h(\gamma,s)=\gamma\) is a proper
homomorphism, and \(G'\) has a faithful proper transverse function. Every \(\nu\in\mathcal E^+\) lifts to
\(\nu'\in\mathcal E^+(G')\), \(\nu'^{(y,s)}\) the image of \(\nu^y\) under \(\gamma\mapsto(\gamma,s)\), faithful if
\(\nu\) is. There is a unique transverse measure \(\Lambda'\) on \(G'\), of modulus \(\delta\circ h\), with
\(\Lambda'_{\nu'}=\Lambda_\nu\times ds\) for all \(\nu\); it is \(\sigma\)-finite. (Section 9 with the homomorphism
\(\psi=c\) into the unimodular group \(\mathbb R\): Lemma 9.1 and Theorem 9.2, where \(\delta_\psi=\delta\circ h\).)

### 1.2 Random Hilbert spaces and random operators

The following is taught in "Square-integrable representations and random operators"; the numbers in parentheses
refer to that lesson.

**(Q1) Coefficients.** A representation \(U\) of \(G\) on a measurable field \(H=(H_x)\) gives unitaries
\(U(\gamma):H_x\to H_y\) for \(\gamma:x\to y\), multiplicative and measurable. For \(\nu\in\mathcal E^+\),
\(D(U,\nu)\) is the space of bounded Borel sections \(\xi\) with
\[
\int|\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle|^2\,d\nu^y(\gamma)\le c^2\|\alpha\|^2\qquad(y\in G^{(0)},\
\alpha\in H_y).
\]
For \(\xi\in D(U,\nu)\), \(T_\nu(\xi)_y\alpha=(\gamma\mapsto\langle\alpha,U(\gamma)\xi_{s(\gamma)}\rangle)\) is an
intertwiner from \(U\) to the regular representation \(L^\nu\) on \(L^2(G^y,\nu^y)\). Its adjoint is the weak integral
\(T_\nu(\xi)_y^*g=\int g(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y(\gamma)\) for \(g\in L^1\cap L^2(G^y,\nu^y)\); we write
\(U(g\nu)\xi\) for the section \(y\mapsto\int g(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y(\gamma)\) when \(\nu(|g|)\) is
bounded. For an intertwiner \(A\), \(A\xi\in D(U',\nu)\) and \(T_\nu(A\xi)=T_\nu(\xi)A^*\). We put
\(\theta_\nu(\xi,\eta)=T_\nu(\xi)^*T_\nu(\eta)\); thus
\[
\theta_\nu(\xi,\xi)_y=\int_{G^y}\big(U(\gamma)\xi_{s(\gamma)}\big)\big(U(\gamma)\xi_{s(\gamma)}\big)^*\,d\nu^y(\gamma)
\quad\text{(weakly)},\qquad \theta_\nu(A\xi,B\eta)=A\theta_\nu(\xi,\eta)B^*. \tag{1.2}
\]
If \(\nu|f|\) and \(\nu'|\tilde f|\) are bounded and \(\xi\in D(U,\nu)\), then \(U(f\nu)\xi\in D(U,\nu')\). (Definitions
2.1 and 4.1, Section 2.2, and Proposition 4.2(a),(b),(c),(e),(f).)

**(Q2) Square integrability.** \(U\) is square integrable if, for a faithful \(\nu\), \(D(U,\nu)\) contains a countable
set whose values are total in \(H_x\) for every \(x\); equivalently \(U\) is equivalent to a subrepresentation of
\(\bigoplus_1^\infty L^\nu\). Subrepresentations, countable direct sums, tensor products with arbitrary
representations, the representations \(L^2\circ F\) for proper random variables \(F\) (with \((U(\gamma)g)(z)=
\delta(\gamma)^{1/2}g(\gamma^{-1}z)\) on \(L^2(F(x),\alpha^x)\)), and pull-backs \(h^*H\) along proper
homomorphisms are square integrable. A *\(\Lambda\)-random Hilbert space* is a square-integrable representation up to
changes on \(\Lambda\)-negligible saturated sets; its pull-back along a proper \(h\) with \(h(\Lambda_1)=\Lambda\) is a
\(\Lambda_1\)-random Hilbert space. Finally, let \(\nu\) be faithful, \(S\) a countable set of bounded Borel sections and
\(y\in G^{(0)}\) such that for every \(\nu^y\)-conull Borel set \(E\subset G^y\) the vectors \(U(\gamma)\xi_{s(\gamma)}\),
\(\gamma\in E\), \(\xi\in S\), are total in \(H_y\). Then there is a countable family \(\mathcal D\) of bounded Borel
functions \(f\) on \(G\) with \(\nu|f|\) and \(\nu|\tilde f|\) bounded, not depending on \(y\), such that the vectors
\((U(f\nu)\xi)_y\), \(f\in\mathcal D\), \(\xi\in S\), are total in \(H_y\); if \(S\subset D(U,\nu)\), these sections lie
in \(D(U,\nu)\) by (Q1). (Definition 4.5, Theorem 4.4, Proposition 4.6, Proposition 4.8, Corollary 4.9, Definition 6.1,
Corollary 7.5(a), Proposition 2.4(b) with the family \(\mathcal D\) of Lemma 1.2(b).)

**(Q3) Random operators.** \(\operatorname{Hom}_\Lambda(H_1,H_2)\) is the space of bounded Borel intertwiners
\((A_x)\), modulo equality off a \(\Lambda\)-negligible saturated set; \(\operatorname{End}_\Lambda(H)\) is a von
Neumann algebra with separable predual. For \(\nu\in\mathcal E^+\), \(\nu(H)=\int^\oplus H_x\,d\Lambda_\nu(x)\), and
\(\nu(A)\) is the decomposable operator \((A_x)\). (Definition 6.1, Theorem 7.2 and the beginning of Section 7.)

**(Q4) The algebra \(W(\nu)\).** For \(\nu\in\mathcal E^+\) let \(\mathcal A_\nu\) be the set of Borel functions \(f\)
on \(G\) such that \(\nu|\delta^tf|\) and \(\nu|\delta^t\tilde f|\) are bounded for every \(t\in\mathbb R\), and \(f\)
and \(\delta^{1/2}f\) lie in \(L^2(G,m_\nu)\). With the product \(f*_\nu g(\gamma)=\int f(\gamma')g(\gamma'^{-1}\gamma)\,
d\nu^{r(\gamma)}(\gamma')\) and the involution \(f^\#=\delta^{-1}f^\flat\), \(f^\flat(\gamma)=\overline{f(\gamma^{-1})}\),
it is a left Hilbert algebra in \(L^2(G,m_\nu)\), stable under \(f\mapsto\delta^{it}f\). Its left von Neumann algebra
is \(W(\nu)\), generated by the operators \(\lambda(f)\) of left convolution; \(\psi_\nu\) denotes its canonical weight.
Its modular conjugation is \(Jg=\delta^{-1/2}g^\flat\) and its modular operator is multiplication by \(\delta\), so
\[
\sigma_t^{\psi_\nu}(\lambda(f))=\lambda(\delta^{it}f); \tag{1.3}
\]
indeed \(\delta^{it}(f*_\nu g)=(\delta^{it}f)*_\nu(\delta^{it}g)\) because \(\delta\) is multiplicative, so
\(\delta^{it}\lambda(f)\delta^{-it}=\lambda(\delta^{it}f)\). The right convolutions \(\rho(k):g\mapsto g*_\nu k\) with
\(\nu|k|\), \(\nu|\tilde k|\) bounded are bounded operators in \(W(\nu)'\). For each random Hilbert space \(H\), \(\nu(H)\)
is a normal \(W(\nu)\)-module, the action \(\pi^H_\nu\) being determined by \(\pi^H_\nu(\lambda(f))\xi=U(f\nu)\xi\) for
bounded \(\xi\in\nu(H)\); for \(H=L^\nu\) this is \(L^2(G,m_\nu)\) with its identity representation. There is an
isometry \(V:\nu(H)\to\ell^2\otimes L^2(G,m_\nu)\) with \(V\pi^H_\nu(w)=(1\otimes w)V\) for \(w\in W(\nu)\), and every
\(A\in\operatorname{Hom}_\Lambda(H_1,H_2)\) gives a \(W(\nu)\)-linear operator \(\nu(A)\), for every \(\nu\).
(Section 6.2 with Proposition 6.2, Definition 6.3, Remark 6.4 and Lemma 6.5; Theorem 7.1(a),(b) and Step 3 of its
proof.)

**(Q5) The equivalence.** If \(\nu\) is faithful, then for all random Hilbert spaces \(H_1,H_2\) the map \(A\mapsto
\nu(A)\) is an isometric bijection from \(\operatorname{Hom}_\Lambda(H_1,H_2)\) onto the space of bounded
\(W(\nu)\)-linear maps \(\nu(H_1)\to\nu(H_2)\). In particular \(\nu:\operatorname{End}_\Lambda(H)\to W(\nu)'\) is an
isomorphism of von Neumann algebras (the commutant taken in \(\nu(H)\)). (Theorem 7.1(c) and Theorem 7.2.)

**(Q6) The ideal \(\mathcal J_\nu\).** The span \(\mathcal J_\nu\) of the \(\theta_\nu(\xi,\eta)\), \(\xi,\eta\in
D(U,\nu)\), forms a two-sided ideal in \(\operatorname{End}_\Lambda(H)\), weakly dense if \(\nu\) is faithful. (Corollaries
4.3(a) and 7.3.)

**(Q7) Points with trivial isotropy.** The fibre at \(y\) of every intertwiner commutes with the isotropy group
\(U(G^y_y)\). For \(\nu\) faithful there is a countable total subset \(D\subset D(U,\nu)\) such that, for every \(y\),
the span of the operators \(\theta_\nu(\xi,\eta)_y\), \(\xi,\eta\in D\), is a \(*\)-algebra, weakly dense in
\(\mathcal L(H_y)\) whenever \(G^y_y=\{y\}\). If \(G\) has *trivial isotropy \(\Lambda\)-almost everywhere* (that is,
\(G^y_y=\{y\}\) off a \(\Lambda\)-negligible saturated Borel set), the centre of \(\operatorname{End}_\Lambda(H)\)
consists of the classes of the families \((a(x)1_{H_x})\), \(a\) bounded, Borel and constant on orbits. (Section 5 with
Proposition 5.1, and Corollary 8.1. The generation of the commutant \(U(G^y_y)'\) at points with nontrivial isotropy is
only stated there, in Remark 5.2, and is not used here.)

### 1.3 The spatial derivative

The following is taught in "The spatial derivative"; the numbers in parentheses refer to that lesson. Fix a von
Neumann algebra \(N\) with an fns weight \(\psi\) and a normal \(N\)-module \(K\), and let \(M\) be the commutant of
\(N\) in \(K\).

**(S1)** A vector \(\zeta\in K\) is \(\psi\)-bounded if \(\|y\zeta\|\le C\|\eta_\psi(y)\|\) for \(y\in\mathfrak
n_\psi\); then \(R^\psi(\zeta)\eta_\psi(y)=y\zeta\) extends to a bounded \(N\)-linear map \(K_\psi\to K\), and
\(\theta^\psi(\zeta,\zeta)=R^\psi(\zeta)R^\psi(\zeta)^*\in M_+\). The \(\psi\)-bounded vectors form a dense subspace
\(D(K,\psi)\). (Definition 1.1, Proposition 1.3 and Remark 1.6.)

**(S2)** For a normal semifinite weight \(\varphi\) on \(M\), the spatial derivative \(d\varphi/d\psi\) is positive and
self-adjoint on \(K\), and \(\varphi(\theta^\psi(\zeta,\zeta))=\langle(d\varphi/d\psi)\zeta,\zeta\rangle\)
for all \(\zeta\in D(K,\psi)\). Moreover \(\varphi_1\le\varphi_2\) iff \(d\varphi_1/d\psi\le d\varphi_2/d\psi\); so
\(\varphi\) is determined by \(d\varphi/d\psi\). The support of \(d\varphi/d\psi\) is \(s(\varphi)\). (Definition 3.2,
Propositions 3.3 and 3.4(a), Corollary 5.2.)

**(S3)** If \(\varphi\) is faithful, \(T=d\varphi/d\psi\) is nonsingular, \(T^{it}xT^{-it}=\sigma^\varphi_t(x)\) for
\(x\in M\), and \((d\varphi_2/d\psi)^{it}=(D\varphi_2:D\varphi_1)_t(d\varphi_1/d\psi)^{it}\). (Theorem 4.3 and Theorem
5.4(a).)

**(S4) Homogeneous operators.** A positive self-adjoint \(T\) on \(K\) equals \(d\varphi/d\psi\) for some normal
semifinite weight \(\varphi\) on \(M\) iff it is homogeneous of degree \(-1\):
\[
T^{it}\sigma^\psi_t(y)=yT^{it}\qquad(y\in N,\ t\in\mathbb R).
\]
The weight is then unique, and faithful iff \(T\) is nonsingular. (Definition 6.1 and the remark after it, Theorem
6.2.)

## 2. Results used from other lessons

**(B1) Operator-valued weights.** Let \(N\subset P\) be von Neumann algebras, \(\varphi\) an fns weight
on \(N\) and \(\rho\) an fns weight on \(P\). If \(\sigma^\rho_t(x)=\sigma^\varphi_t(x)\) for \(x\in N\), there is a
unique fns operator-valued weight \(E:P_+\to\widehat N_+\) with \(\rho=\varphi\circ E\). For every fns
operator-valued weight \(E\) and fns \(\varphi\), \(\sigma^{\varphi\circ E}_t\) restricts to \(\sigma^\varphi_t\) on \(N\),
\(E(a^*xa)=a^*E(x)a\) (\(a\in N\)), \(E\circ\sigma^{\varphi\circ E}_t=\sigma^\varphi_t\circ E\), and
\((D(\varphi_1\circ E):D(\varphi\circ E))_t=(D\varphi_1:D\varphi)_t\) for fns \(\varphi_1\). The composition of a
normal weight with a normal operator-valued weight is a normal weight. These are proved in the course *Modular theory and weights*:
existence and uniqueness in Compatible modular weights and the full positive cone,
§§OE-01–OE-06; the restriction of the modular group and the cocycle identity are proved in [Finite matrices and modular restriction](#finite-matrices-and-modular-restriction); normality of compositions in Finite
calculus and composition of operator-valued weights, §§OVW-02 and OVW-04;
\(E(a^*xa)=a^*E(x)a\) is part of the definition. For the covariance, \(E_t=\sigma^\varphi_{-t}\circ E\circ\sigma^{\varphi\circ
E}_t\) is again an fns operator-valued weight, and \(\varphi\circ E_t=\varphi\circ E\) because \(\varphi\circ\sigma^\varphi_{-t}=\varphi\)
and \(\varphi\circ E\) is invariant under its modular group; uniqueness gives \(E_t=E\). See also, e.g., [Haagerup 1979].

### Finite matrices and modular restriction

**Proposition 2.1.** Let \(N\subset M\), let \(T\) be a faithful normal semifinite operator-valued weight onto \(N\), and let \(\varphi,\psi\) be faithful normal semifinite weights on \(N\). Put \(\Phi=\widehat\varphi\circ T\), \(\Psi=\widehat\psi\circ T\). Then

\[
\sigma_t^\Phi(n)=\sigma_t^\varphi(n),\qquad
[D\Psi:D\Phi]_t=[D\psi:D\varphi]_t\in N
\quad(n\in N,\ t\in\mathbb R).
\]

**Proof.** We prove the finite mixed-domain transfer first, then use two independent right spectral cutoffs to obtain the full analytic graph. This order avoids assuming the modular restriction being proved.

#### 1. Types and finite ideals

Let \(N\subset M\) be von Neumann algebras and \(T:M_+\to\widehat N_+\) a faithful normal semifinite operator-valued weight. Let \(\varphi,\psi\) be faithful normal semifinite scalar weights on \(N\), with \(\Phi=\widehat\varphi\circ T\), \(\Psi=\widehat\psi\circ T\). For a scalar weight \(\omega\), write \(\mathfrak n_\omega=\{x:\omega(x^*x)<\infty\}\). Write \(\mathfrak n_T=\{x:T(x^*x)\in N_+\}\). The bounded finite-ideal extension of \(T\) is \(\dot T\), with its linear polarization and \(N\)-bimodularity as in OVW-02.

Take \(y\in\mathfrak n_\Phi\cap\mathfrak n_T\) and \(z\in\mathfrak n_\Psi\cap\mathfrak n_T\). Put

\[
A=T(y^*y),\qquad B=T(z^*z),\qquad C=\dot T(y^*z).
\]

Then \(A,B\) are bounded positive elements of \(N\), \(\varphi(A)=\Phi(y^*y)<\infty\), and \(\psi(B)=\Psi(z^*z)<\infty\).

#### 2. Matrix positivity follows from bimodularity

The ideal \(\mathfrak n_T\) is stable under right multiplication by \(N\), since \(T((ya)^*(ya))=a^*Aa\) is bounded. For every \(a,b\in N\), positivity and the finite-ideal identities give

\[
\begin{pmatrix}a\\b\end{pmatrix}^*
\begin{pmatrix}A&C\\C^*&B\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}
=T((ya+zb)^*(ya+zb))\ge0.
\]

This implies positivity of the full matrix \(Q\in M_2(N)\), rather than merely positivity in scalar tests using one vector. Here is an algebraic verification. If its negative part \(Q_-\) were nonzero, take the columns of \(Q_-^{1/2}\) as the test columns. Since \(Q_-\) is a spectral function of \(Q\),

\[
Q_-^{1/2}QQ_-^{1/2}=-Q_-^2.
\]

At least one diagonal entry of the nonzero positive matrix \(Q_-^2\) is nonzero: if all its diagonal entries vanished, every column of \(Q_-\) would have zero squared norm and \(Q_-=0\). That test column would give a negative nonzero element, a contradiction. Hence \(Q\ge0\).

#### 3. Oriented factorization

For \(\varepsilon>0\), matrix positivity and the Schur-complement test give

\[
C^*(A+\varepsilon)^{-1}C\le B.
\]

For example, apply the block quadratic form with first component \(-(A+\varepsilon)^{-1}C\eta\) and second component \(\eta\); adding \(\varepsilon\) to the first diagonal preserves positivity. Thus

\[
k_\varepsilon=(A+\varepsilon)^{-1/2}C(B+\varepsilon)^{-1/2}
\]

is a contraction in \(N\). A subnet has an ultraweak limit \(k\) in the unit ball. Since square roots converge in norm,

\[
C=(A+\varepsilon)^{1/2}k_\varepsilon(B+\varepsilon)^{1/2}
\longrightarrow A^{1/2}kB^{1/2}
\]

ultraweakly. Therefore \(C=A^{1/2}kB^{1/2}\). Set

\[
a_0=k^*A^{1/2},\qquad b_0=B^{1/2}.
\]

Then \(a_0^*a_0=A^{1/2}kk^*A^{1/2}\le A\), so \(a_0\in\mathfrak n_\varphi\). Likewise \(b_0\in\mathfrak n_\psi\). Consequently

\[
\boxed{\dot T(y^*z)=a_0^*b_0\in\mathfrak n_\varphi^*\mathfrak n_\psi.}
\]

This is the required orientation. It does not exchange the two scalar weights or require a trace. It proves one elementary product, stronger than membership merely in the finite linear span.

#### 4. The finite scalar mixed identity

Suppose \((a,b)\) belongs to the relative scalar analytic graph on \(N\), so its proved finite-domain criterion gives

\[
a\mathfrak n_\varphi^*\subset\mathfrak n_\psi^*,\qquad
\mathfrak n_\psi b\subset\mathfrak n_\varphi,\qquad
\psi(aC)=\varphi(Cb)
\quad(C\in\operatorname{span}\mathfrak n_\varphi^*\mathfrak n_\psi).
\]

These are AG.27's exact oriented domains. To obtain the required bounds without an unstated relative multiplier theorem, use its balanced matrix weight \(\Omega(X)=\psi(X_{11})+\varphi(X_{22})\). The pair \(aE_{12},bE_{12}\) has the complete bounded lower strip proved in AG.28–AG.31. Let \(H\) be its value at \(-i/2\). HS.15–HS.16 applied to \(aE_{12}\), with positive test \(QE_{22}\), gives \(\psi(aQa^*)\le\|H\|^2\varphi(Q)\). Reflect the full strip by \(F(\overline z-i)^*\); its real edge is the modular orbit of \(b^*E_{21}\) and its midpoint is \(H^*\). The same half-strip theorem, now tested against \(QE_{11}\), gives \(\varphi(b^*Qb)\le\|H\|^2\psi(Q)\). Take \(K=L=\max(1,\|H\|)\). Normal evaluation of the increasing bounded spectral truncations, including the truncations of any infinite projection, extends both inequalities to the full extended cone. Thus

\[
\widehat\psi(aQa^*)\le K^2\widehat\varphi(Q),\qquad
\widehat\varphi(b^*Qb)\le L^2\widehat\psi(Q).
\]

Bimodularity and composition give the corresponding inequalities on \(M\). In particular \(ya^*\in\mathfrak n_\Psi\) and \(zb\in\mathfrak n_\Phi\). Right \(N\)-stability also keeps them in \(\mathfrak n_T\).

Here is the finite-composition identity with its full domains. For \(\omega\in\{\varphi,\psi\}\), \(\Omega=\widehat\omega\circ T\), and \(u,v\in\mathfrak n_T\cap\mathfrak n_\Omega\), polarize \(u^*v\) into its four positive squares. Each \(u+i^kv\) remains in both ideals. Its square has bounded \(T\)-output and finite \(\Omega\)-value, so \(\Omega(w^*w)=\omega(T(w^*w))\). Polarization proves both \(\dot T(u^*v)\in\mathfrak m_\omega\) and \(\Omega(u^*v)=\omega(\dot T(u^*v))\). This is not a scalar evaluation on an undefined mixed product. Applying it to \(ya^*,z\) and \(y,zb\), bimodularity gives

\[
\Psi(ay^*z)=\psi(a\dot T(y^*z))
=\varphi(\dot T(y^*z)b)=\Phi(y^*zb).
\]

Every value is a defined finite complex weight value. The left product is \((ya^*)^*z\) in \(\mathfrak n_\Psi^*\mathfrak n_\Psi\), and the right product is \(y^*(zb)\) in \(\mathfrak n_\Phi^*\mathfrak n_\Phi\).

#### 5. Independent right spectral cuts

Now take arbitrary \(y\in\mathfrak n_\Phi\), \(z\in\mathfrak n_\Psi\). The extended positives \(A=T(y^*y)\), \(B=T(z^*z)\) may be unbounded. They have no nonzero infinite projections: a nonzero infinite projection would have positive faithful \(\varphi\)- or \(\psi\)-value, forcing the corresponding extended evaluation to be infinite. Their finite spectral parts are densely defined positive affiliated operators. Put

\[
e_n=1_{[0,n]}(A),\qquad f_n=1_{[0,n]}(B),\qquad
y_n=ye_n,\quad z_n=zf_n.
\]

These are two separate **right** cuts. Bimodularity gives \(T(y_n^*y_n)=e_nAe_n\le n1\) and \(T(z_n^*z_n)=f_nBf_n\le n1\). Because each cutoff is a spectral function of its own positive, \(e_nAe_n\le A\), \(f_nBf_n\le B\). Thus \(y_n\in\mathfrak n_\Phi\cap\mathfrak n_T\), \(z_n\in\mathfrak n_\Psi\cap\mathfrak n_T\).

The scalar tails satisfy

\[
\|\Lambda_\Phi(y-y_n)\|^2
=\widehat\varphi(A(1-e_n))\longrightarrow0,\qquad
\|\Lambda_\Psi(z-z_n)\|^2
=\widehat\psi(B(1-f_n))\longrightarrow0.
\]

Indeed the bounded spectral truncations increase to the full positive, their scalar evaluations increase to its finite scalar value by normal extended-positive evaluation, and additivity makes each tail the difference. The half-strip inequalities give

\[
\|\Lambda_\Psi((y-y_n)a^*)\|
\le K\|\Lambda_\Phi(y-y_n)\|,\qquad
\|\Lambda_\Phi((z-z_n)b)\|
\le L\|\Lambda_\Psi(z-z_n)\|.
\]

Cauchy–Schwarz in the respective GNS spaces therefore passes the finite identities to

\[
\Psi((ya^*)^*z)=\Phi(y^*(zb))
\quad(y\in\mathfrak n_\Phi,\ z\in\mathfrak n_\Psi).
\]

No common cutoff commuting with both extended positives, left cut, or equality on a merely dense unbounded-form test space has been substituted.

#### The real modular actions

The transferred ideal inclusions, their bounds, and the last full finite-domain identity are exactly AG.27 on \(M\). They give the analytic-graph inclusion OR.9. The real-action comparison needs its embedded-algebra version, since invariance of \(N\) under the \(M\)-action is a conclusion.

Let \(\alpha_t\) be the mixed group on \(N\) and \(\beta_t\) that on \(M\). Both are normal sigma-weakly continuous groups of complex-linear isometries, directly from their modular automorphisms and unitary cocycles, as AG.26 states. Suppose their lower imaginary graphs satisfy \(G(\alpha_{-i})\subset G(\beta_{-i})\) in \(M\oplus M\). Reversing graph pairs gives the corresponding positive-imaginary inclusion. Take \(x\) in AG.02's bounded exponential core in \(N\), with entire orbit bound \(Ce^{r|\operatorname{Im}z|}\), and put \(y_k=\alpha_{ik}(x)\) for every integer \(k\). These are elements of \(N\) and remain in its entire core. Both imaginary graph inclusions give \(\beta_i(y_k)=y_{k+1}\) and \(\beta_{-i}(y_{k+1})=y_k\) inside \(M\). Integer strip gluing therefore gives an entire \(M\)-orbit for \(x\) with these same imaginary integer values. On every strip between adjacent integer heights, the real isometries of \(\beta\) preserve the two edge norms. The scalar three-lines estimate bounds the glued orbit by \(Ce^{r|\operatorname{Im}z|}\).

For \(\omega\in M_*\), the scalar entire difference \(\omega(\alpha_z(x)-\beta_z(x))\) has AG.03's horizontal growth bound and vanishes at all positive imaginary integers. That proved uniqueness theorem makes it zero. Predual separation gives equality of the real orbits on this core. AG.02 supplies uniformly bounded sigma-weak core approximants to every \(n\in N\); normality of the two fixed real maps passes equality to all of \(N\). Hence \(\beta_t(n)=\alpha_t(n)\), establishing invariance rather than presupposing it. No general Kadison-isometry classification is used.

Setting the two scalar weights equal yields the forward modular restriction. Evaluating the mixed action at \(1\) yields its cocycle restriction with numerator \(\psi\) and reference \(\varphi\). The scalar inputs used above are Analytic generators and finite domains, its relative finite-domain theorem and exponential-core comparison, and Half-strip domination and endpoints. The bounded finite calculus is Finite calculus and composition of operator-valued weights. The proof uses these scalar and finite-calculus results without assuming that the larger modular group preserves the smaller algebra.


**(B2) Cocycles and traces.** Two fns weights with the same cocycle derivative relative to a third one
are equal. An fns weight with \(\sigma^\varphi=\mathrm{id}\) is a trace. The support of a normal trace is central, and
\(\varphi(x)=\varphi(exe)\) for a normal weight with support \(e\). The first statement is Reconstructing a weight from a modular cocycle,
§CX-10. If \(\sigma^\varphi=\mathrm{id}\), every element is in the centralizer, so by Fixed
elements and changes of density, §CZ-05 every \(a\in M\) multiplies
\(\mathfrak m_\varphi\) on both sides with \(\varphi(az)=\varphi(za)\); for \(x\in\mathfrak n_\varphi\) with polar decomposition
\(x=v|x|\) this gives \(\varphi(xx^*)=\varphi(v\cdot x^*xv^*)=\varphi(x^*xv^*v)=\varphi(x^*x)\), and applied to \(x^*\) it shows
that the two values are finite together. The support of a normal trace is central by Traces on von Neumann algebras,
Section 2 (null projections and the support), and \(\varphi(x)=\varphi(exe)\) is Finite domains, null
directions, and support corners, §WS-05.

**(B3) Weights given by densities.** Let \(\tau\) be an fns trace on \(P\) and \(h\) a
nonsingular positive self-adjoint operator affiliated with \(P\). The weight \(\tau_h(x)=\lim_{\varepsilon\to0}
\tau(h_\varepsilon^{1/2}xh_\varepsilon^{1/2})\), \(h_\varepsilon=h(1+\varepsilon h)^{-1}\), is fns, and
\(\sigma^{\tau_h}_t=\operatorname{Ad}h^{it}\), \((D\tau_{h_2}:D\tau_{h_1})_t=h_2^{it}h_1^{-it}\). The weight \(\tau_h\) is normal and semifinite with support \(s(h)=1\) by Fixed elements and
changes of density, §CZ-08; the modular group of \(\tau\) is trivial, so
\((D\tau_h:D\tau)_t=h^{it}\) by Recognizing a weight by its fixed density, §§PT-04 and
PT-08, and the chain rule (Changing reference for a weight cocycle,
§CH-01) gives the last formula.

**(B4) Arveson spectrum** [Arveson 1974]. Let \(X=E^*\) be a dual Banach space and \((\gamma_t)_{t\in\mathbb R}\) a
one-parameter group of weak\*-continuous linear isometries of \(X\) such that \(t\mapsto\langle\gamma_tx,a\rangle\) is
continuous for all \(x\in X\), \(a\in E\). Two cases are used: a \(\sigma\)-weakly continuous action \(\alpha\) of
\(\mathbb R\) on a von Neumann algebra \(M\) (\(X=M\), \(E=M_*\)); and \(\beta_t(x)=u_txv_t^*\) on \(X=B(K_2,K_1)\), for
strongly continuous unitary groups \(u\) on \(K_1\) and \(v\) on \(K_2\), where \(E\) is the space of trace-class
operators \(a\colon K_1\to K_2\) and \(\langle x,a\rangle=\operatorname{Tr}(xa)\). For \(f\in L^1(\mathbb R)\) let
\(\gamma(f)x\in X\) be given by \(\langle\gamma(f)x,a\rangle=\int f(t)\langle\gamma_tx,a\rangle\,dt\), and put
\(\hat f(p)=\int f(t)e^{ipt}dt\). The spectrum \(\operatorname{Sp}(\gamma)\) is the set of \(p\) with \(\hat f(p)=0\) for
every \(f\) with \(\gamma(f)=0\); \(\operatorname{Sp}_\gamma(x)\) is defined likewise with \(\gamma(f)x=0\). Then:
(i) \(\operatorname{Sp}(\gamma)\) and \(\operatorname{Sp}_\gamma(x)\) are closed, and
\(\operatorname{Sp}_\gamma(x)\subset\operatorname{Sp}(\gamma)\); (ii) \(\operatorname{Sp}_\gamma(x)=\emptyset\) iff \(x=0\);
(iii) if \(\hat f\) vanishes on a neighbourhood of \(\operatorname{Sp}_\gamma(x)\), then \(\gamma(f)x=0\); (iv) if the
spectral measures \(e_1,e_2\) of \(u,v\) (\(u_t=\int e^{ipt}de_1(p)\), \(v_t=\int e^{ipt}de_2(p)\)) are carried by closed
sets \(I_1,I_2\), then \(\operatorname{Sp}(\beta)\subset\overline{I_1-I_2}\), so
\(\operatorname{Sp}_\beta(x)\subset\overline{I_1-I_2}\) for every \(x\); (v) \(\operatorname{Sp}(\gamma)\subset\{0\}\) iff
\(\gamma\) is trivial; when \(X\ne0\), this says \(\operatorname{Sp}(\gamma)=\{0\}\). If an action \(\alpha\) on a von
Neumann algebra satisfies \(\alpha_t(x)=u_txv_t^*\) for an element \(x\), then \(\alpha(f)x=\beta(f)x\) for every \(f\),
so \(\operatorname{Sp}_\alpha(x)=\operatorname{Sp}_\beta(x)\).

*Proof.* We use three results on closed ideals of \(L^1(\mathbb R)\). In the lessons on harmonic analysis on locally
compact abelian groups the Fourier transform is \(\int f(t)\overline{\chi(t)}\,dt\) for characters \(\chi\), and
\(s\mapsto\chi_s\), \(\chi_s(t)=e^{2\pi ist}\), identifies \(\mathbb R\) with its dual group (Characters and the dual
group, Theorem 3.1). Our \(\hat f(p)\) is the transform at
\(\chi_{-p/2\pi}\), and \(p\mapsto\chi_{-p/2\pi}\) is a homeomorphism onto the dual group, so the results apply in our
normalization. For a closed ideal \(J\) let \(h(J)\) be the set of \(p\) with \(\hat f(p)=0\) for all \(f\in J\).

- (W) If \(h(J)=\emptyset\), then \(J=L^1(\mathbb R)\) ([Closed ideals of \(L^1(G)\) and Wiener's theorem, Theorem
  5.3](../../HA-LCA/src/closed-ideals-of-l1-g-and-wieners-theorem.html#section-5)).
- (S) If \(\hat f\) vanishes on a neighbourhood of \(h(J)\), then \(f\in J\); and if \(h(J)=\{0\}\), then
  \(J=\{f:\int f=0\}\), because finite sets admit spectral synthesis (Tauberian theorems and spectral synthesis,
  Corollary 3.3).
- (U) If \(K\) is compact and \(W\supset K\) open, there is \(f\in L^1(\mathbb R)\) with \(\hat f=1\) on \(K\) and
  \(\operatorname{supp}\hat f\) a compact subset of \(W\) ([Closed ideals of \(L^1(G)\) and Wiener's theorem,
  Proposition 2.1](../../HA-LCA/src/closed-ideals-of-l1-g-and-wieners-theorem.html#section-2)).

Since \(|\langle\gamma(f)x,a\rangle|\le\|f\|_1\|x\|\|a\|\), \(\gamma(f)x\) is well defined and
\(\|\gamma(f)x\|\le\|f\|_1\|x\|\). Weak\* continuity of each \(\gamma_s\) and Fubini's theorem give
\(\gamma_s\gamma(f)=\gamma(f(\cdot-s))\) and \(\gamma(f)\gamma(g)=\gamma(f*g)\). Hence \(J_x=\{f:\gamma(f)x=0\}\) and
\(J_\gamma=\{f:\gamma(f)=0\}\) are closed ideals, with hulls \(\operatorname{Sp}_\gamma(x)\) and
\(\operatorname{Sp}(\gamma)\). If \(e_n\ge0\) has integral \(1\) and support in \((-1/n,1/n)\), then
\(\gamma(e_n)x\to x\) weak\*, by continuity of the scalar orbits.

(i) Each \(\hat f\) is continuous, and \(J_\gamma\subset J_x\). (ii) For \(x=0\), \(J_x=L^1(\mathbb R)\), whose hull is
empty by (U). If \(\operatorname{Sp}_\gamma(x)=\emptyset\), then \(J_x=L^1(\mathbb R)\) by (W), so \(\gamma(e_n)x=0\) for
all \(n\), and \(x=0\). (iii) is (S).

(v) If \(X=0\), then \(\operatorname{Sp}(\gamma)=\emptyset\) and \(\gamma\) is trivial. Let \(X\ne0\). If
\(\operatorname{Sp}(\gamma)\subset\{0\}\), then \(\operatorname{Sp}(\gamma)\supset\operatorname{Sp}_\gamma(x)\ne\emptyset\)
for \(x\ne0\), so \(\operatorname{Sp}(\gamma)=\{0\}\) and \(J_\gamma=\{f:\int f=0\}\) by (S). Then
\(f(\cdot-s)-f\in J_\gamma\), so \(\gamma_s\gamma(f)x=\gamma(f)x\); with \(f=e_n\) and \(n\to\infty\), \(\gamma_sx=x\).
Conversely, if \(\gamma\) is trivial, then \(\gamma(f)=(\int f)\,1\) and \(J_\gamma=\{f:\int f=0\}\). Its hull contains
\(0\), and for \(p\ne0\), (U) with \(K=\{p\}\) and \(W=\mathbb R\setminus\{0\}\) gives \(f\in J_\gamma\) with
\(\hat f(p)=1\). So \(\operatorname{Sp}(\gamma)=\{0\}\).

(iv) The pairing identifies \(B(K_2,K_1)\) with the dual of the trace class, and \(\beta_t\) is the adjoint of
\(a\mapsto v_t^*au_t\), which is continuous in the trace norm, first for rank-one \(a\) and then by density; so
\(\beta\) is of the kind considered. Let \(F=\overline{I_1-I_2}\) and suppose that \(\hat f=0\) on \(F\). Put
\(P_n=e_1([-n,n])\) and \(Q_n=e_2([-n,n])\). Divide \([-n,n]\) into finitely many Borel intervals of length at most
\(1/m\), let \(E_i\) and \(F_j\) be the nonzero spectral projections of \(e_1\) and \(e_2\) of these intervals, and
choose \(a_i\in I_1\) and \(b_j\in I_2\) in the corresponding intervals, which is possible because \(e_1,e_2\) vanish
off \(I_1,I_2\). For \(U(t)=\sum_ie^{ita_i}E_i\) and \(V(t)=\sum_je^{itb_j}F_j\), the spectral theorem gives
\(\|U(t)-u_tP_n\|\le\min(2,|t|/m)\) and \(\|V(t)-v_tQ_n\|\le\min(2,|t|/m)\), and
\[
\int f(t)U(t)xV(t)^*\,dt=\sum_{i,j}\hat f(a_i-b_j)\,E_ixF_j=0,
\]
because \(a_i-b_j\in F\). Since \(P_n\) commutes with \(u_t\) and \(Q_n\) with \(v_t\),
\(\int f(t)u_tP_nxQ_nv_t^*\,dt=P_n\beta(f)xQ_n\), and dominated convergence as \(m\to\infty\) gives
\(P_n\beta(f)xQ_n=0\). Letting \(n\to\infty\), \(\beta(f)x=0\) for every \(x\), that is, \(\beta(f)=0\). If
\(p\notin F\), (U) with \(K=\{p\}\) and \(W=\mathbb R\setminus F\) gives such an \(f\) with \(\hat f(p)=1\), so
\(p\notin\operatorname{Sp}(\beta)\). \(\square\)

**(B5) Direct integrals.** Let \(\mu\) be a \(\sigma\)-finite measure on a standard Borel space \(Y\) and
\(\mathcal D\) the diagonal algebra of \(\int^\oplus K_y\,d\mu\). Its commutant is the algebra of decomposable
operators. A positive self-adjoint operator whose unitary group and support commute with \(\mathcal D\) is a direct
integral \(\int^\oplus T_y\,d\mu\) of a measurable field of positive self-adjoint operators. If a von Neumann algebra
\(R\supset\mathcal D\) is generated by \(\mathcal D\) and countably many decomposable operators \(b^n\), then
\(R=\int^\oplus R_y\,d\mu\) with \(R_y\) generated by the \(b^n_y\), and \(R'=\int^\oplus R_y'\,d\mu\), \(R\cap R'=
\int^\oplus(R_y\cap R_y')\,d\mu\). The commutant of the diagonal algebra is Decomposable operators and the diagonal
algebra, Theorem 5.1; the algebra generated by \(\mathcal D\) and the \(b^n\) is \(\int^\oplus R_y\,d\mu\) by
Lemma 5.1 of Direct integrals of von Neumann algebras, with commutant and centre given by Theorems
3.2(1) and 4.3 there. The statement on positive self-adjoint operators is Unbounded decomposable operators and
measurable spectral decomposition, Corollary 4.2, for an arbitrary
\(\sigma\)-finite base; there a field of self-adjoint operators is measurable when its Cayley transforms are
(Definition 3.1), and every bounded Borel function of \(\int^\oplus T_y\,d\mu\) is the direct integral of the same
function of the \(T_y\) (Theorem 3.6), in particular \(\big(\int^\oplus T_y\,d\mu\big)^{it}=\int^\oplus T_y^{it}\,d\mu\).

The measurable Hilbert fields in (B5) and (B6) have countable fundamental sequences, as in Measurable fields of Hilbert spaces and their direct integrals (Definition 2.1 and Theorem 3.1). The diagonal-commutant assertion is proved in Decomposable operators and the diagonal algebra (Theorem 5.1). The positive-operator assertion, including the support and the convention \(0^{it}=0\), is Corollary 4.2 of Unbounded decomposable operators and measurable spectral decomposition. For the countably generated algebra, Lemma 5.1 of Direct integrals of von Neumann algebras gives the stated fibre generators; Theorem 3.2 in its Direct integrals of von Neumann algebras section gives the commutant, and Theorem 4.3 in its Direct integrals of von Neumann algebras section gives the centre. The \(\sigma\)-finite and standard Borel hypotheses above remain in force.

**(B6) Measurable spectral decomposition.** Let \(\mu\) be a \(\sigma\)-finite measure on a standard
Borel space \(Y\) and \((A_y)\) a measurable field of self-adjoint operators on a measurable field \((K_y)\) whose
spectral measures are absolutely continuous. There are a measurable field \((K_{(y,s)})\) over \(Y\times\mathbb R\) and
a measurable field of unitaries \(K_y\to\int^\oplus K_{(y,s)}\,ds\) (defined for \(\mu\)-almost every \(y\)) carrying
\(A_y\) to multiplication by \(s\). If \((\tilde A_y)\) on \((\tilde K_y)\) is a second such field, decomposed in the
same way, a measurable field \((B_y)\) of bounded operators \(B_y:K_y\to\tilde K_y\) with \(B_yg(A_y)=g(\tilde A_y)B_y\)
for all bounded Borel \(g\) is carried to \((\int^\oplus B'_{(y,s)}\,ds)_y\) for a measurable field of operators
\(B'_{(y,s)}:K_{(y,s)}\to\tilde K_{(y,s)}\) over \(Y\times\mathbb R\). This is proved, with Lebesgue measure as the
dominating measure \(\kappa\) and for an arbitrary \(\sigma\)-finite base, in Unbounded decomposable operators and
measurable spectral decomposition, Theorems 8.1 and 8.3; the
measurable fields over \(Y\times\mathbb R\) and the spaces \(\int^\oplus K_{(y,s)}\,ds\) are those of Theorem 7.1 there,
and the second statement holds for any two decompositions of this kind, with \(\|B'_{(y,s)}\|\le\|B_y\|\).

Theorem 8.1 of Unbounded decomposable operators and measurable spectral decomposition proves this decomposition, and Theorem 8.3 there proves the jointly measurable intertwining field; Theorems 6.1 and 7.1 supply the countably generated multiplication representation and the iterated direct integral. Absolute continuity uses one fixed Lebesgue measure \(ds\): outside one \(\mu\)-null set, every Lebesgue-null Borel set has zero spectral projection in each fibre. The ordinary sigma-finite Radon–Nikodym input of its Fact 1.8 is proved in Measure and Hilbert space tools for Haar integration, Theorem 4.1. The product-measure and Tonelli–Fubini inputs are proved in Finite conditional expectations, measurable densities, and positive kernel integrals, Corollary K.4(c): both measures are sigma-finite, the product sigma-algebra is uncompleted, nonnegative section integrals are measurable, and signed or complex interchange requires absolute integrability. In particular the fixed Lebesgue measure on \(\mathbb R\) is sigma-finite, using the disjoint unit intervals; no topological Radon-measure hypothesis on \(Y\) is needed. Almost-everywhere representatives are taken on these given sigma-algebras.

**(B7) Almost homomorphisms** [Ramsay 1971]. Let \(\mathcal G\) be a groupoid whose Borel structure is standard,
\(\kappa\) a faithful proper transverse function on \(\mathcal G\) and \(\mu\) a \(\sigma\)-finite measure on
\(\mathcal G^{(0)}\) such that \(m=\mu\circ\kappa\) and its image under \(\gamma\mapsto\gamma^{-1}\) have the same null
sets. Let \(\pi\) be a Borel map from \(\mathcal G\) to a Polish group such that \(\pi(\gamma_1\gamma_2)=\pi(\gamma_1)
\pi(\gamma_2)\) for almost every composable pair, for the measure \(\int\!\!\int\varepsilon_{(\gamma_1,\gamma_2)}\,
d\kappa^{s(\gamma_1)}(\gamma_2)\,dm(\gamma_1)\) on \(\mathcal G^{(2)}\). Then there are a \(\mu\)-conull saturated Borel
set \(Y\subset\mathcal G^{(0)}\) and a Borel homomorphism \(\pi'\) from the reduction \(\mathcal G_Y=r^{-1}(Y)\) to the
Polish group with \(\pi'=\pi\) \(m\)-almost everywhere on \(\mathcal G_Y\). This is Almost homomorphisms of measured groupoids,
Theorem 5.1. Ramsay's theory of virtual groups works with
reductions to conull Borel sets that need not be saturated, as Connes points out [Connes 1979, Introduction]; that
lesson reaches a saturated set by joining each unit to the conull set with a Borel choice of arrows.

**(B8) Projections.** In a von Neumann algebra: the left and right supports \(l(x)\), \(r(x)\)
of an element are equivalent; \(p\vee q-q\sim p-p\wedge q\) (parallelogram law); two projections with \(\|p-q\|<1\)
are equivalent, and so are \(1-p\) and \(1-q\). For closed subspaces with projections \(P_1,P_2\), \(\|P_1-P_2\|=
\max(\|(1-P_2)P_1\|,\|(1-P_1)P_2\|)\), and \(\|(1-P_2)P_1\|\) is the supremum over unit vectors of \(P_1\) of the
distance to the range of \(P_2\). If \(b\in M\) is injective on the range of a projection \(q\in M\), then \(q\) is
equivalent to the projection onto the closure of \(bqH\) (polar decomposition of \(bq\)); if \(b\) is bounded below on
\(qH\), this range is closed. The inverse of an element of \(fMe\) mapping \(eH\) bijectively onto \(fH\) lies in
\(eMf\). The supports are equivalent through the partial isometry of the polar decomposition, which lies in \(M\) by
The double commutant theorem, Proposition 7.2; this also gives the statement on \(bq\). The
parallelogram law is Projections and types of von Neumann algebras, Proposition 4.4. If
\(\|p-q\|<1\), then \(x=qp+(1-q)(1-p)\) satisfies \(x^*x=1-(p-q)^2\), so it is invertible, and \(|x|\) commutes with \(p\);
its unitary polar part \(u\in M\) satisfies \(upu^*=xpx^{-1}=q\), which gives both equivalences. An element of \(fMe\)
mapping \(eH\) bijectively onto \(fH\) has a bounded inverse there (Hahn–Banach, Baire and the basic theorems on Banach
spaces, the open mapping theorem); extended by \(0\) on \((1-f)H\), the inverse commutes with \(M'\), so
it lies in \(M\), and in \(eMf\). The two norm formulas are elementary Hilbert-space geometry.

An additional direct verification of the support equivalence is the following. (For \(\xi\in pH\), \(\|q\xi\|=\|\xi-(p-q)\xi\|\ge(1-\|p-q\|)\|\xi\|\), and symmetrically for \(\eta\in qH\); so \(qp\) has right support \(p\) and left support \(q\), and these are equivalent [Takesaki I, Chapter V, Proposition 1.5]. The same argument applies to \(1-p\) and \(1-q\).)

**(B9) Groups.** Let \(\Gamma\) be a unimodular locally compact group with Haar measure \(dg\), also written \(m\). No
countability assumption is made in this item.

(a) Every nonzero \(\sigma\)-finite left-invariant measure on the Borel sets of \(\Gamma\) is \(c\,dg\) for a unique
\(c>0\).

(b) The right von Neumann algebra \(R(\Gamma)=\lambda(\Gamma)'\) carries the Plancherel trace \(\tau'\): call
\(\eta\in L^2(\Gamma)\) right bounded if \(a\mapsto a*\eta\) (\(a\in C_c(\Gamma)\)) extends to a bounded operator
\(\rho(\eta)\) on \(L^2(\Gamma)\); then \(\tau'(\rho(\eta)^*\rho(\eta))=\|\eta\|^2\), and \(\tau'(x^*x)=\infty\) for every
other \(x\in R(\Gamma)\). It is an fns trace.

(c) Let \(\pi\) be an irreducible strongly continuous unitary representation of \(\Gamma\) on \(K_\pi\ne0\), with
coefficients \(c_{\xi,\eta}(g)=\langle\pi(g)\xi,\eta\rangle\). The following are equivalent: some \(c_{\xi_0,\eta_0}\)
with \(\xi_0,\eta_0\ne0\) is square integrable; every \(c_{\xi,\eta}\) is square integrable; \(\pi\) is equivalent to a
subrepresentation of the left regular representation \(\lambda\). Such a \(\pi\) is called *square integrable*, and
there is a unique \(d_\pi>0\), the *formal degree*, with
\[
\int c_{\xi,\eta}(g)\overline{c_{\xi',\eta'}(g)}\,dg=d_\pi^{-1}\langle\xi,\xi'\rangle\overline{\langle\eta,\eta'\rangle},
\qquad\text{in particular}\qquad\int|c_{\xi,\eta}|^2\,dg=d_\pi^{-1}\|\xi\|^2\|\eta\|^2.
\]

For second countable \(\Gamma\), (a) is Regular representations, Fourier algebra and Fourier–Stieltjes coefficients,
§PF-39, and Section 10 uses (a) only in that case. The proofs below, of (a) in
general and of (b) and (c), use these results of *Haar measure on locally compact groups*: the Riesz representation
theorem and inner regularity on sets of finite measure (Theorem 2.2 and Proposition
2.3(1)); image
measures and density of \(C_c\) in \(L^p\) (Proposition
3.1); an open
\(\sigma\)-compact subgroup (Proposition
7.2);
positivity of Haar measure on nonempty open sets and its uniqueness (Proposition 9.1 and Theorem
9.2);
invariance of \(dg\) under right translations and under \(g\mapsto g^{-1}\), \(\Gamma\) being unimodular (Theorem
10.1 and
Theorem 11.1);
the bound \(\|\xi*k\|_2\le\|k\|_1\|\xi\|_2\) and continuity of translation in \(L^1\) (Theorem
14.2(4),(6));
and approximate identities (Theorem
15.1).

*Proof of (a).* Let \(\nu\) be such a measure. We use two facts. A \(\sigma\)-finite measure has at most countably
many pairwise disjoint measurable sets of positive measure: if sets \(E_n\) of finite measure cover the space, each
such set meets some \(E_n\) in measure at least \(1/k\), and for fixed \(n,k\) there are only finitely many. Next, by
a theorem of Ulam, there is no countably additive probability measure \(P\) on all subsets of the first uncountable
ordinal \(\omega_1\) with \(P(\{\beta\})=0\) for every \(\beta\). Indeed, choose for each countable ordinal \(\beta\ge1\)
a surjection \(e_\beta\colon\mathbb N\to\beta\), and put \(A_{\alpha,n}=\{\beta>\alpha:e_\beta(n)=\alpha\}\). For fixed
\(n\) these sets are pairwise disjoint, so \(P(A_{\alpha,n})>0\) for only countably many \(\alpha\); choose \(\alpha\)
outside all these countable sets. Then \(\bigcup_nA_{\alpha,n}=\{\beta:\beta>\alpha\}\) has probability \(0\), and so
does its countable complement, a contradiction.

*Step 1: \(\Gamma\) is \(\sigma\)-compact.* This step, which adapts the argument of [Erdős–Mauldin 1976], does not use
unimodularity. Suppose \(\Gamma\) is not \(\sigma\)-compact. Starting from an open \(\sigma\)-compact subgroup
\(H_0\), build by transfinite recursion open \(\sigma\)-compact subgroups \(H_\alpha\), \(\alpha<\omega_1\), with
\(H_\alpha\subsetneq H_{\alpha+1}\) and \(H_\lambda=\bigcup_{\alpha<\lambda}H_\alpha\) for limit \(\lambda\). For
\(H_{\alpha+1}\) take the subgroup generated by \(H_\alpha\) and some \(g_\alpha\notin H_\alpha\), which exists because
\(H_\alpha\ne\Gamma\); it is the union of the \(\sigma\)-compact sets \(W^n\), \(W=H_\alpha\cup\{g_\alpha,g_\alpha^{-1}\}\),
and it is open. An increasing countable union of open \(\sigma\)-compact subgroups is again one. Put
\(H=\bigcup_\alpha H_\alpha\). For each \(\alpha\), \(H_\alpha\) has uncountably many left cosets in \(H\): countably many
coset representatives would all lie in one \(H_\beta\), since countably many countable ordinals have a countable upper
bound, and then \(H=H_\beta\ne H_{\beta+1}\). Let \(R\) be a set of representatives of the right cosets of \(H\) in
\(\Gamma\), and \(S_\alpha=H_\alpha R\). It is a union of right cosets of the open subgroup \(H_\alpha\), and so is its
complement; so \(S_\alpha\) is clopen. If \(M_\alpha\subset H\) represents the left cosets of \(H_\alpha\) in \(H\),
the sets \(xS_\alpha\), \(x\in M_\alpha\), are pairwise disjoint: \(xhr=x'h'r'\) with \(h,h'\in H_\alpha\) gives
\(Hr=Hr'\), so \(r=r'\), and then \(xH_\alpha=x'H_\alpha\). They all have measure \(\nu(S_\alpha)\), and there are
uncountably many, so \(\nu(S_\alpha)=0\). The sets \(S_\alpha\) increase, \(S_\lambda=\bigcup_{\alpha<\lambda}S_\alpha\)
for limit \(\lambda\), and \(\bigcup_\alpha S_\alpha=HR=\Gamma\). So \(T_0=S_0\) and \(T_{\alpha+1}=S_{\alpha+1}\setminus
S_\alpha\) (\(T_\lambda=\emptyset\) for limit \(\lambda\)) partition \(\Gamma\) into clopen \(\nu\)-null sets indexed by
\(\omega_1\), and every union of them is open, hence Borel. For a Borel set \(E\) with \(0<\nu(E)<\infty\),
\(P(A)=\nu\bigl(E\cap\bigcup_{i\in A}T_i\bigr)/\nu(E)\) contradicts Ulam's theorem.

*Step 2: compact zero sets.* A *zero set* is a set \(q^{-1}(0)\) with \(q\colon\Gamma\to[0,\infty)\) continuous. For
every Borel \(E\) with \(m(E)<\infty\), \(m(E)=\sup\{m(C):C\subset E\text{ a compact zero set}\}\); this is a theorem of
Halmos, in the form of [Fremlin, 443M]. Given \(r<m(E)\), choose a compact \(K\subset E\) with \(m(K)>r\), and let \(C\)
be the set of points of \(K\) all of whose neighbourhoods \(O\) satisfy \(m(K\cap O)>0\); it is compact. Every compact
subset of \(K\setminus C\) is covered by finitely many open sets \(O\) with \(m(K\cap O)=0\), so \(m(K\setminus C)=0\) by
inner regularity, and \(m(C)=m(K)>r\). The function \(\varphi(s)=m(C\,\triangle\,sC)=\|1_C-1_{sC}\|_1\) is continuous;
choose open neighbourhoods \(U_n\) of the identity with \(\varphi<2^{-n}\) on \(U_n\). Then \(C=\bigcap_nU_nC\). Indeed,
let \(x=u_nz_n\) with \(u_n\in U_n\), \(z_n\in C\), and suppose \(x\notin C\). A subnet of \((z_n)\) converges to some
\(z\in C\); along it \(u_n\to u=xz^{-1}\), and \(\varphi(u)=0\), so \(m(C\setminus u^{-1}C)=0\) by left invariance. But
\(z\in C\setminus u^{-1}C\), and the open set \(\Gamma\setminus u^{-1}C\) contains \(z\), so
\(m(C\setminus u^{-1}C)=m(K\setminus u^{-1}C)>0\), a contradiction. Choose \(\chi_n\in C_c(\Gamma)\) with
\(0\le\chi_n\le1\), \(\chi_n=1\) on \(C\) and support in the open set \(U_nC\). Then \(q=\sum_n2^{-n}(1-\chi_n)\) is
continuous with zero set exactly \(C\).

*Step 3: \(\nu\) is finite on compact sets.* By Step 1, \(\Gamma\) is the union of an increasing sequence of compact
sets \(K_n\). Every continuous function on \(\Gamma\times\Gamma\) is then measurable for the product of the Borel
\(\sigma\)-algebras, since on each \(K_n\times K_n\) it is a uniform limit of finite sums of products \(a(s)b(t)\) of
continuous functions (Stone–Weierstrass). Since \(\nu\) is \(\sigma\)-finite, some Borel set \(E\) with
\(\nu(E)<\infty\) and some \(K_n\) satisfy \(m(K_n\cap E)>0\); Step 2 gives a compact zero set \(C=q^{-1}(0)\subset K_n\cap E\) with \(m(C)>0\) and
\(\nu(C)<\infty\). Let \(b\in C_c(\Gamma)\) be nonnegative and nonzero, and \(h(x)=\int b(t)1_C(tx)\,dm(t)\). The
integrand is product measurable, since \((t,x)\mapsto q(tx)\) is continuous, and Tonelli's theorem for the
\(\sigma\)-finite measures \(m\) and \(\nu\), with left invariance, gives
\[
\int h\,dm=m(C)\int b\,dm>0,\qquad\int h\,d\nu=\nu(C)\int b\,dm<\infty.
\]
By right invariance of \(m\), \(h(x)=\int_Cb(yx^{-1})\,dm(y)\); it is continuous, because \(b(yx^{-1})\to
b(yx_0^{-1})\) uniformly in \(y\in C\) as \(x\to x_0\). So \(h\ge\varepsilon\) on a nonempty open set \(U\) for some
\(\varepsilon>0\), and \(\nu(U)\le\varepsilon^{-1}\int h\,d\nu<\infty\). Every compact set is covered by finitely many
left translates of \(U\), so it has finite \(\nu\)-measure.

*Step 4: \(\nu=c\,m\).* By Step 3, \(f\mapsto\int f\,d\nu\) is a positive linear functional on \(C_c(\Gamma)\); let
\(\mu\) be the Radon measure representing it. For \(s\in\Gamma\), \(E\mapsto\mu(sE)\) is a Radon measure representing
the same functional, by left invariance of \(\nu\), so \(\mu\) is left invariant by the uniqueness in the Riesz
theorem. It is nonzero: some \(K_n\) has \(\nu(K_n)>0\), and a function of \(C_c(\Gamma)\) that is \(\ge1_{K_n}\) has
positive \(\nu\)-integral. By uniqueness of Haar measure, \(\mu=c\,m\) with \(c>0\). For a compact zero set
\(C=q^{-1}(0)\) and \(\chi\in C_c(\Gamma)\) with \(0\le\chi\le1\) and \(\chi=1\) on \(C\), the functions
\(\chi\max(0,1-nq)\) decrease to \(1_C\), and dominated convergence gives \(\nu(C)=c\,m(C)\). For a relatively compact
Borel set \(A\), Step 2 gives \(\nu(A)\ge c\,m(A)\). Choose \(\psi\in C_c(\Gamma)\) with \(0\le\psi\le1\) and \(\psi=1\)
on \(\bar A\); then \(Z=\{\psi\ge1/2\}\) is a compact zero set containing \(A\), and
\(\nu(A)=\nu(Z)-\nu(Z\setminus A)\le c\,m(Z)-c\,m(Z\setminus A)=c\,m(A)\). So \(\nu=c\,m\) on relatively compact Borel
sets, and on all Borel sets by intersecting with the \(K_n\). Since \(m\ne0\), \(c\) is unique. \(\square\)

*Proof of (b).* By Haar convolution from both sides, §§HG-01–HG-03,
\(C_c(\Gamma)\) with convolution and the involution \(a^*(g)=\overline{a(g^{-1})}\) is a left Hilbert algebra in
\(L^2(\Gamma)\). Its left von Neumann algebra is \(\lambda(\Gamma)''\): the operator \(a*\cdot\) is the weak integral
\(\int a(g)\lambda(g)\,dg\), so it lies in \(\lambda(\Gamma)''\), and for an approximate identity \((a_U)\),
\((a_U(s^{-1}\cdot))*\cdot=\lambda(s)(a_U*\cdot)\to\lambda(s)\) strongly. So its commutant is \(R(\Gamma)\), and
Weights and the Hilbert spaces of multiplication, §WH-12 gives an fns weight
\(\tau'\) on \(R(\Gamma)\) whose finite ideal consists of the \(\rho(\eta)\), \(\eta\) right bounded for the original
algebra \(C_c(\Gamma)\), with \(\tau'(\rho(\eta)^*\rho(\eta))=\|\eta\|^2\). It is a trace. Let \(J\) be the antiunitary
\((J\eta)(g)=\overline{\eta(g^{-1})}\). For \(a,b\in C_c(\Gamma)\) and \(\eta\in L^2(\Gamma)\), Fubini's theorem gives
\(\langle a*\eta,b\rangle=\langle a,b*J\eta\rangle\). If \(\eta\) is right bounded, then
\(|\langle a,b*J\eta\rangle|\le\|\rho(\eta)\|\|a\|\|b\|\), so \(J\eta\) is right bounded and
\(\rho(\eta)^*=\rho(J\eta)\). Hence the finite ideal is closed under adjoints, and for \(x=\rho(\eta)\),
\(\tau'(xx^*)=\|J\eta\|^2=\|\eta\|^2=\tau'(x^*x)\); for every other \(x\) both values are infinite. For a unitary
\(u\in R(\Gamma)\) and \(b\in R(\Gamma)_+\), \(x=ub^{1/2}\) gives \(\tau'(ubu^*)=\tau'(b)\). \(\square\)

*Proof of (c).* Since \(\Gamma\) is unimodular, \(dg\) is invariant under \(g\mapsto gs\) and \(g\mapsto g^{-1}\), so
these maps preserve square integrability. An operator commuting with \(\pi(\Gamma)\) is scalar (Schur's lemma): the
spectral projections of its real and imaginary parts have invariant ranges. Fix \(\eta\ne0\), let \(D_\eta\) be the set
of \(\xi\in K_\pi\) for which \(T_\eta\xi\colon g\mapsto\langle\xi,\pi(g)\eta\rangle=c_{\xi,\eta}(g^{-1})\) is square
integrable, and regard \(T_\eta\) as an operator from \(D_\eta\) to \(L^2(\Gamma)\).

(1) *If \(D_\eta\ne0\), then \(D_\eta=K_\pi\) and \(\|T_\eta\xi\|_2^2=c_\eta\|\xi\|^2\) with \(c_\eta>0\).* From
\(T_\eta\pi(s)\xi=\lambda(s)T_\eta\xi\), \(D_\eta\) is invariant under \(\pi\), hence dense by irreducibility. \(T_\eta\) is closed: if
\(\xi_n\to\xi\) and \(T_\eta\xi_n\to F\) in \(L^2\), the coefficients converge uniformly to \(T_\eta\xi\), and a
subsequence with \(\sum_k\|T_\eta\xi_{n_k}-F\|_2^2<\infty\) converges to \(F\) almost everywhere, so \(F=T_\eta\xi\). By
Normal products and closed operator graphs, §3,
\(A=T_\eta^*T_\eta\) is a positive self-adjoint operator with \(D(A^{1/2})=D_\eta\) and
\(\|A^{1/2}\xi\|=\|T_\eta\xi\|\). The relation \(T_\eta\pi(s)=\lambda(s)T_\eta\), with equal domains, gives
\(\pi(s)^*A\pi(s)=A\), so \((1+A)^{-1}\) commutes with \(\pi\) and is a scalar \(a\in(0,1]\). Hence \(A=(a^{-1}-1)1\)
is bounded, \(D_\eta=K_\pi\), and \(c_\eta=a^{-1}-1\). Finally \(c_\eta>0\): \(T_\eta\eta\) is continuous with value
\(\|\eta\|^2\) at the identity, and a nonzero continuous function does not vanish almost everywhere, Haar measure being
positive on nonempty open sets.

(2) *Then \(c_\eta^{-1/2}T_\eta\) is an isometry \(K_\pi\to L^2(\Gamma)\) intertwining \(\pi\) and \(\lambda\)*, so
\(\pi\) is equivalent to a subrepresentation of \(\lambda\).

(3) *One square-integrable coefficient makes all of them square integrable.* If \(c_{\xi_0,\eta_0}\) is square
integrable, then \(\xi_0\in D_{\eta_0}\), so \(T_{\eta_0}\) is everywhere defined by (1). For \(\xi\ne0\),
\(T_\xi\eta_0(g)=\overline{T_{\eta_0}\xi(g^{-1})}\) is square integrable, so \(\eta_0\in D_\xi\) and \(D_\xi=K_\pi\).
So every coefficient is square integrable, and \(\pi\) is a subrepresentation of \(\lambda\) by (2).

(4) *Subrepresentations of \(\lambda\).* Let \(\pi\) be the restriction of \(\lambda\) to a closed invariant subspace
\(H\subset L^2(\Gamma)\) with projection \(P\), which commutes with \(\lambda\). By density of \(C_c(\Gamma)\) choose
\(h\in C_c(\Gamma)\) with \(\eta=Ph\ne0\). For \(\xi\in H\),
\(\langle\xi,\lambda(g)\eta\rangle=\langle\xi,\lambda(g)h\rangle=(\xi*h^*)(g)\) with \(h^*(s)=\overline{h(s^{-1})}\), and
\(\|\xi*h^*\|_2\le\|h\|_1\|\xi\|_2\). So \(D_\eta=H\), and the coefficient \(c_{\eta,\eta}\), which is nonzero, is
square integrable; by (3) all coefficients are.

(5) *The formal degree.* For \(\xi,\eta\ne0\), \(\|T_\eta\xi\|_2=\|T_\xi\eta\|_2\), by the identity in (3) and
invariance under inversion; so \(c_\eta\|\xi\|^2=c_\xi\|\eta\|^2\). With a unit vector \(e\) and \(c=c_e>0\), this gives
\(c_\eta=c\|\eta\|^2\), that is, \(\int|c_{\xi,\eta}|^2\,dg=c\|\xi\|^2\|\eta\|^2\). Put \(d_\pi=c^{-1}\). Polarization in
\(\xi\) for fixed \(\eta\), and then in \(\eta\), gives the formula for four vectors, and evaluation at unit vectors gives
uniqueness of \(d_\pi\). \(\square\)

Square-integrable representations and the formal degree are treated for every locally compact group in
[Duflo–Moore 1976].

**(B10) Left Hilbert algebras.** Let \(\mathcal A\) be a left Hilbert algebra in a Hilbert space
\(\mathfrak h\), with left von Neumann algebra \(L=\lambda(\mathcal A)''\) and canonical weight \(\psi\), an fns weight
on \(L\). (i) The GNS space of \(\psi\) is \(\mathfrak h\), with \(\eta_\psi(\lambda(a))=a\) for \(a\in\mathcal A\).
(ii) Call \(\zeta\in\mathfrak h\) *right bounded* if \(a\mapsto\lambda(a)\zeta\) (\(a\in\mathcal A\)) extends to a
bounded operator \(\pi_r(\zeta)\) on \(\mathfrak h\). Then \(y\zeta=\pi_r(\zeta)\eta_\psi(y)\) for every
\(y\in\mathfrak n_\psi\).

## 3. Random operators of degree \(\alpha\)

A closed densely defined operator \(T\) is determined by the pair of bounded operators \((u,(1+T^*T)^{-1})\), where
\(T=u|T|\) is the polar decomposition. A family \((T_x)_{x\in G^{(0)}}\) of closed densely defined operators
\(T_x:H_x\to H'_x\) between measurable fields is *measurable* if both bounded families \((u_x)\) and
\(((1+T_x^*T_x)^{-1})\) are measurable. For positive self-adjoint \(T_x\) this is the same as measurability of
\(x\mapsto T_x^{it}\) for every \(t\), because \(T^{it}\) and \((1+T)^{-1}\) are obtained from each other by Borel
functional calculus, and a Borel function of a measurable field is measurable.

The ordinary spectral calculus, with its maximal domains, is proved in Self-adjoint spectral calculus with the original domain from A spectral measure for a unitary operator. Spectral products, transport and inverse domains (Proposition 3), Spectral products, transport and inverse domains (Proposition 4) and Spectral products, transport and inverse domains (Proposition 5 and Corollary 6) give the changes of variable, unitary transport, support restrictions and inverse domains used here. Field measurability of the bounded Borel functions and equality of the unbounded direct-integral domains are Proposition 3.2 and Theorem 3.6 of Unbounded decomposable operators and measurable spectral decomposition. In Lemmas 3.2 and 3.5, reconstructing a positive operator from its group on the support uses Theorem 4.3 and Corollary 4.5 of Holomorphy in Banach spaces, Stone's theorem and resolvent convergence.

**Definition 3.1.** Let \((H,U)\) and \((H',U')\) be square-integrable representations and \(\alpha\in\mathbb R\). A
measurable family \(T=(T_x)\) of closed densely defined operators \(T_x:H_x\to H'_x\) has *degree \(\alpha\)* if for
every \(\gamma:x\to y\)
\[
U'(\gamma)T_x=\delta(\gamma)^{\alpha}\,T_y\,U(\gamma) \tag{3.1}
\]
as closed operators; in particular \(U(\gamma)\operatorname{dom}T_x=\operatorname{dom}T_y\). A *random operator of
degree \(\alpha\)* is a class of such families modulo equality off a \(\Lambda\)-negligible saturated Borel set (the
relation (3.1) is only required off such a set). It is *positive* if \(H=H'\) and every \(T_x\) is positive
self-adjoint.

Random operators of degree \(0\) that are bounded are exactly the elements of \(\operatorname{Hom}_\Lambda(H,H')\).
For each \(t\in\mathbb R\) let \(H^{(t)}\) denote the field \(H\) with the representation \(U^{(t)}(\gamma)=
\delta(\gamma)^{it}U(\gamma)\). It is square integrable, since \(|\langle\alpha,U^{(t)}(\gamma)\xi_x\rangle|=
|\langle\alpha,U(\gamma)\xi_x\rangle|\) gives \(D(U^{(t)},\nu)=D(U,\nu)\).

**Lemma 3.2.** Let \(T=(T_x)\) be a measurable family of positive self-adjoint operators on \(H\). The following are
equivalent.

(a) \(T\) has degree \(1\).

(b) For every \(t\in\mathbb R\) and \(\gamma:x\to y\), \(U(\gamma)T_x^{it}U(\gamma)^*=\delta(\gamma)^{it}T_y^{it}\).

(c) For every \(t\), the family \((T_x^{it})\) is an intertwiner from \(U^{(t)}\) to \(U\):
\(T_y^{it}\,\delta(\gamma)^{it}U(\gamma)=U(\gamma)T_x^{it}\).

In this case the support family \(s(T)=(s(T_x))\) is a projection of degree \(0\), that is, an element of
\(\operatorname{End}_G(H)\).

*Proof.* (a) says \(U(\gamma)T_xU(\gamma)^*=\delta(\gamma)T_y\). Conjugation by a unitary commutes with the functional
calculus, and \((cS)^{it}=c^{it}S^{it}\) for \(c>0\) (with \(0^{it}=0\) on the kernel), so (a) implies (b). Conversely,
two positive self-adjoint operators \(S_1,S_2\) with \(S_1^{it}=S_2^{it}\) for all \(t\) have the same support
(\(t=0\)) and the same unitary group on it, hence are equal by the uniqueness in Stone's theorem; applied to
\(S_1=U(\gamma)T_xU(\gamma)^*\), \(S_2=\delta(\gamma)T_y\), (b) implies (a). (b) and (c) are the same equation
multiplied on the right by \(U(\gamma)\). At \(t=0\), (b) reads \(U(\gamma)s(T_x)U(\gamma)^*=s(T_y)\). \(\square\)

**Examples 3.3.** (a) If \(\delta=1\), the identity family \(1=(1_{H_x})\) is a positive random operator of degree
\(1\). This is the case of Section 10.

(b) Let \(F\) be a proper random variable and \(H=L^2\circ F\) (see (Q2)). Let \(\rho>0\) be a Borel function on
\(X=\bigsqcup F(x)\) with \(\rho(\gamma^{-1}z)=\delta(\gamma)\rho(z)\) for \(z\in F(y)\), \(\gamma:x\to y\), and let
\(M(\rho)_x\) be multiplication by \(\rho\) on \(L^2(F(x),\alpha^x)\). Since \(U(\gamma)M(g)_xU(\gamma)^*\) is
multiplication by \(z\mapsto g(\gamma^{-1}z)\) on \(F(y)\) for every Borel \(g\),
\[
U(\gamma)M(\rho)_xU(\gamma)^*=M(\rho\circ\gamma^{-1})_y=\delta(\gamma)M(\rho)_y,
\]
so \(M(\rho)\) is a positive random operator of degree \(1\). We call such operators *diagonal*.

(c) In particular, for \(\nu\in\mathcal E^+\) the regular representation \(L^\nu\) is \(L^2\circ F\) for the random
variable \(x\mapsto(G^x,\delta^{-1}\nu^x)\): indeed \(\gamma_*(\delta^{-1}\nu^x)=\delta(\gamma)\delta^{-1}\nu^y\) by
left invariance and multiplicativity, and \(g\mapsto\delta^{1/2}g\) is a unitary from \(L^2(G^x,\nu^x)\) onto
\(L^2(G^x,\delta^{-1}\nu^x)\) that carries \(L^\nu(\gamma)\) to \(g\mapsto\delta(\gamma)^{1/2}g(\gamma^{-1}\,\cdot)\).
On \(L^\nu\) itself, multiplication by \(\delta^{-1}\) has degree \(1\): \(\delta(\gamma^{-1}\gamma')^{-1}=
\delta(\gamma)\delta(\gamma')^{-1}\).

**Lemma 3.4 (rigidity).** Let \(\nu\in\mathcal E^+\) be faithful and let \(T_1,T_2\) be families of degree \(\alpha\)
between \(H\) and \(H'\), each satisfying (3.1) on a saturated Borel set \(Y\) with \(\Lambda\)-negligible complement.
If \(T_{1,x}=T_{2,x}\) for \(\Lambda_\nu\)-almost every \(x\), then \(T_1=T_2\) as random operators.

*Proof.* Let \(Z\subset Y\) be the set where \(T_{1,x}\neq T_{2,x}\). Using the bounded pairs \((u,(1+T^*T)^{-1})\)
and a countable family of Borel sections whose values are dense in every fibre, \(Z\) is Borel. By (3.1), for
\(\gamma:x\to y\) in \(Y\) we have \(T_{j,y}=\delta(\gamma)^{-\alpha}U'(\gamma)T_{j,x}U(\gamma)^*\), so \(x\in Z\) iff
\(y\in Z\): \(Z\) is saturated. Since \(\Lambda_\nu(Z)=0\) and \(\nu\) is faithful, \(Z\) is \(\Lambda\)-negligible by
(R3). \(\square\)

The next lemma turns an operator on the direct integral \(\nu(H)\) into a random operator of degree \(1\). Recall
from (Q4) that \(\nu(H^{(t)})\) is the Hilbert space \(\nu(H)\) on which \(\lambda(f)\) acts by \(U^{(t)}(f\nu)=
U(\delta^{it}f\nu)\).

**Lemma 3.5.** Let \(\nu\in\mathcal E^+\) be faithful, and let \(S\) be positive and self-adjoint on \(\nu(H)\),
such that, for every \(t\), \(S^{it}\) is a \(W(\nu)\)-linear map from \(\nu(H^{(t)})\) to \(\nu(H)\). Then
there is a unique positive random operator \(T\) of degree \(1\) with \(\nu(T)=S\), where \(\nu(T)=\int^\oplus
T_x\,d\Lambda_\nu(x)\).

*Proof.* Uniqueness follows from Lemma 3.4. For each rational \(t\), (Q5) applied to \(H^{(t)}\) and \(H\) gives
\(W^{(t)}\in\operatorname{Hom}_\Lambda(H^{(t)},H)\) with \(\nu(W^{(t)})=S^{it}\). Choose Borel representatives which
are genuine intertwiners off a \(\Lambda\)-negligible saturated set; discarding countably many such sets we may assume
they are intertwiners everywhere.

Twisting both sides by \(\delta^{is}\), \(W^{(t)}\) is also an intertwiner from \(H^{(s+t)}\) to \(H^{(s)}\). Hence
\(W^{(s)}W^{(t)}\) and \(W^{(s+t)}\) are both intertwiners from \(H^{(s+t)}\) to \(H\), and \(W^{(t)*}\), \(W^{(-t)}\)
are both intertwiners from \(H\) to \(H^{(t)}\). Since \(S^{is}S^{it}=S^{i(s+t)}\) and \((S^{it})^*=S^{-it}\), these
pairs agree \(\Lambda_\nu\)-almost everywhere, hence off a \(\Lambda\)-negligible saturated set by Lemma 3.4 (which
applies to bounded intertwiners of any twisted representations, with the same proof). Discarding countably many sets,
for every \(x\) the map \(t\mapsto W^{(t)}_x\) on \(\mathbb Q\) is a group homomorphism into partial isometries with
\(W^{(t)*}_x=W^{(-t)}_x\); so \(e_x=W^{(0)}_x\) is a projection and \(t\mapsto W^{(t)}_x\) is a unitary group of
\(e_xH_x\).

Let \(C\) be the set of \(x\) where \(t\mapsto W^{(t)}_x\) is strongly continuous on \(\mathbb Q\) (uniformly on
bounded sets). Since the \(W^{(t)}_x\) are contractions, it suffices to test on a countable family of sections dense
in every fibre, so \(C\) is Borel. From \(W^{(t)}_y=\delta(\gamma)^{-it}U(\gamma)W^{(t)}_xU(\gamma)^*\) we see that
\(C\) is saturated. The operators \(S^{it}=\nu(W^{(t)})\), \(t\in\mathbb Q\), are decomposable, hence so are their
strong limits \(S^{it}\), \(t\in\mathbb R\); by (B5), \(S=\int^\oplus S_x\,d\Lambda_\nu(x)\) for a measurable field of
positive self-adjoint operators \(S_x\), and \(W^{(t)}_x=S_x^{it}\) for all rational \(t\) and \(\Lambda_\nu\)-almost
every \(x\). Such \(x\) lie in \(C\). So \(C\) has \(\Lambda\)-negligible complement (R3), and we discard it.

For \(x\in C\), the group extends by continuity to a strongly continuous unitary group of \(e_xH_x\); by Stone's
theorem it is \(A_x^{it}\) for a unique nonsingular positive self-adjoint operator \(A_x\) on \(e_xH_x\). Put
\(T_x=A_x\oplus0\) on \(e_xH_x\oplus(1-e_x)H_x\), so that \(T_x^{it}=W^{(t)}_x\). Measurability: the self-adjoint
operators \(L_x=\log A_x\oplus0\) have \(e^{itL_x}=W^{(t)}_x+1-e_x\), a measurable field for rational \(t\), so
\((L_x)\) is a measurable field by Unbounded decomposable operators and measurable spectral decomposition, Proposition
3.2(d); hence so is \((T_x)\), whose Cayley transform is
\((c\circ\exp)(L_x)\,e_x-(1-e_x)\) with \(c(\lambda)=(\lambda-i)(\lambda+i)^{-1}\). The intertwining relation of Lemma 3.2(c) holds for rational \(t\),
hence for all \(t\) by continuity, so \(T\) has degree \(1\). Finally \(\nu(T)^{it}=S^{it}\) for rational \(t\), hence
for all \(t\), so \(\nu(T)=S\) by Stone's theorem. \(\square\)

## 4. Normal weights determined by a generating cone

The weight \(\varphi_T\) will be defined by its values on the operators \(\theta_\nu(\xi,\xi)\). The following
general principle shows that such values determine a normal weight.

**Lemma 4.1.** Fix a von Neumann algebra \(M\) and a set \(\mathcal S\subset M_+\) with (i) \(x+y\in\mathcal S\)
for \(x,y\in\mathcal S\), (ii) \(axa^*\in\mathcal S\) for \(x\in\mathcal S\), \(a\in M\), and (iii) the linear span
of \(\mathcal S\) weakly dense in \(M\). Then \(\mathcal S_1=\{x\in\mathcal S:\|x\|<1\}\) is upward directed, and as
an increasing net it converges strongly to \(1\).

*Proof.* By (ii) with \(a=\sqrt c\), \(\mathcal S\) is stable under multiplication by \(c>0\). For \(x\in\mathcal S_1\)
put \(x'=x(1-x)^{-1}=(1-x)^{-1/2}x(1-x)^{-1/2}\in\mathcal S\) by (ii). Note that \(1+x'=(1-x)^{-1}\), so
\(x'(1+x')^{-1}=x\). Given \(a,b\in\mathcal S_1\), let \(c=(a'+b')(1+a'+b')^{-1}=(1+a'+b')^{-1/2}(a'+b')
(1+a'+b')^{-1/2}\). It lies in \(\mathcal S\) by (i) and (ii), and \(\|c\|<1\). The function \(t\mapsto t(1+t)^{-1}=
1-(1+t)^{-1}\) is operator monotone on \([0,\infty)\), because \(u\mapsto u^{-1}\) reverses order on positive invertible
operators. Hence \(c\ge a'(1+a')^{-1}=a\) and likewise \(c\ge b\). So \(\mathcal S_1\) is upward directed; let \(e\le1\)
be the strong limit of the increasing net.

For \(x\in\mathcal S\) and \(n\ge1\), \(nx(1+nx)^{-1}\in\mathcal S_1\), and these operators increase strongly to the
support projection \(s(x)\). Hence \(e\ge s(x)\) for every \(x\in\mathcal S\). Let \(p=1-\bigvee_{x\in\mathcal S}s(x)\).
Then \(xp=0\) for all \(x\in\mathcal S\), hence \(yp=0\) for all \(y\) in the span of \(\mathcal S\), and by weak
density \(p=0\). So \(e\ge1\). \(\square\)

**Proposition 4.2.** Let \(\mathcal S\) be as in Lemma 4.1 and \(\varphi_1,\varphi_2\) normal weights on \(M\). If
\(\varphi_1(x)\le\varphi_2(x)\) for all \(x\in\mathcal S\), then \(\varphi_1\le\varphi_2\). In particular normal
weights that agree on \(\mathcal S\) are equal.

*Proof.* Let \(x\in M_+\) and let \((s_i)\) be the increasing net \(\mathcal S_1\). Then \(x^{1/2}s_ix^{1/2}\in
\mathcal S\) by (ii), and it increases strongly to \(x\). By normality \(\varphi_1(x)=\sup_i\varphi_1(x^{1/2}s_i
x^{1/2})\le\sup_i\varphi_2(x^{1/2}s_ix^{1/2})=\varphi_2(x)\). \(\square\)

**Corollary 4.3.** Let \(H\) be a \(\Lambda\)-random Hilbert space and \(\nu\in\mathcal E^+\) faithful. The set
\(\mathcal S_\nu\) of finite sums \(\sum_i\theta_\nu(\xi_i,\xi_i)\), \(\xi_i\in D(U,\nu)\), satisfies the hypotheses of
Lemma 4.1 in \(M=\operatorname{End}_\Lambda(H)\). Hence a normal weight on \(\operatorname{End}_\Lambda(H)\) is
determined by its values on the operators \(\theta_\nu(\xi,\xi)\), \(\xi\in D(U,\nu)\).

*Proof.* (i) is clear. (ii): \(a\theta_\nu(\xi,\xi)a^*=\theta_\nu(a\xi,a\xi)\) with \(a\xi\in D(U,\nu)\) by (1.2) and
(Q1). (iii): by polarization, \(\theta_\nu(\xi,\eta)=\frac14\sum_{k=0}^3i^k\theta_\nu(\xi+i^k\eta,\xi+i^k\eta)\), so
the span of \(\mathcal S_\nu\) is \(\mathcal J_\nu\), which is weakly dense by (Q6). \(\square\)

## 5. The weight of a positive operator of degree one

Throughout this section \(H\) is a \(\Lambda\)-random Hilbert space and \(T\) a positive random operator of degree
\(1\) on \(H\).

**Lemma 5.1.** Let \(\nu\in\mathcal E^+\), \(\psi=\psi_\nu\), and \(\xi\in D(U,\nu)\) with \(\int\|\xi_x\|^2
d\Lambda_\nu(x)<\infty\), and let \(\xi'\) be its class in \(\nu(H)\). Then \(\xi'\) is \(\psi\)-bounded in the
\(W(\nu)\)-module \(\nu(H)\), \(R^\psi(\xi')=\nu(T_\nu(\xi)^*)\), and
\[
\theta^\psi(\xi',\xi')=\nu\big(\theta_\nu(\xi,\xi)\big).
\]

*Proof.* By (Q4) and (B10)(i), \(\nu(L^\nu)=L^2(G,m_\nu)\) is the GNS space of \(\psi\), with
\(\eta_\psi(\lambda(f))=f\) for \(f\in\mathcal A_\nu\). The operator \(R=\nu(T_\nu(\xi)^*)\) from \(L^2(G,m_\nu)\) to
\(\nu(H)\) is bounded (by \(\sup_y\|T_\nu(\xi)_y\|\)) and \(W(\nu)\)-linear, because \(T_\nu(\xi)^*\) is an intertwiner
(Q4). For \(f\in\mathcal A_\nu\) and almost every \(y\), \(f|_{G^y}\) lies in \(L^1\cap L^2(G^y,\nu^y)\), so
\(T_\nu(\xi)_y^*f=\int f(\gamma)U(\gamma)\xi_{s(\gamma)}\,d\nu^y(\gamma)\) (Q1). Since \(\xi'\) is bounded and square
integrable, the description of the action in (Q4) gives
\[
R\,\eta_\psi(\lambda(f))=Rf=\big(U(f\nu)\xi\big)'=\lambda(f)\xi'\qquad(f\in\mathcal A_\nu).
\]
We show \(y\xi'=R\eta_\psi(y)\) for every \(y\in\mathfrak n_\psi\). Proved in Weights and the Hilbert spaces of multiplication, §§WH-04–WH-08 and
WH-11: the canonical weight and its GNS space in WH-05–WH-08, the left-bounded vectors
\(\eta_\psi(\mathfrak n_\psi)\) in WH-11, and \(\lambda_\xi\zeta=\pi_r(\zeta)\xi\) in WH-04. Let \(V:\nu(H)\to\ell^2\otimes L^2(G,m_\nu)\) be an
isometry with \(V\lambda(f)=(1\otimes\lambda(f))V\) (Q4), and write \(V\xi'=(\zeta_k)_k\) and \(VR=(R_k)_k\), with
\(\zeta_k\in L^2(G,m_\nu)\) and bounded operators \(R_k\) on \(L^2(G,m_\nu)\). Applying \(V\) to this identity and taking the
\(k\)-th component, \(\lambda(a)\zeta_k=R_ka\) for \(a\in\mathcal A_\nu\). So \(\zeta_k\) is right bounded in the sense of
(B10)(ii), with \(\pi_r(\zeta_k)=R_k\), and \(y\zeta_k=R_k\eta_\psi(y)\) for \(y\in\mathfrak n_\psi\). Hence
\(Vy\xi'=(1\otimes y)V\xi'=VR\eta_\psi(y)\), and \(y\xi'=R\eta_\psi(y)\) because \(V\) is isometric. Thus
\(\|y\xi'\|\le\|R\|\|\eta_\psi(y)\|\), \(\xi'\) is \(\psi\)-bounded, and \(R^\psi(\xi')=R\). Finally
\(\theta^\psi(\xi',\xi')=RR^*=\nu(T_\nu(\xi)^*T_\nu(\xi))=\nu(\theta_\nu(\xi,\xi))\). \(\square\)

**Lemma 5.2.** For every \(\nu\in\mathcal E^+\), the positive self-adjoint operator \(\nu(T)=\int^\oplus T_x\,
d\Lambda_\nu(x)\) on \(\nu(H)\) is homogeneous of degree \(-1\) with respect to \(\psi_\nu\):
\(\nu(T)^{it}\sigma^{\psi_\nu}_t(y)=y\,\nu(T)^{it}\) for \(y\in W(\nu)\), \(t\in\mathbb R\). Equivalently,
\(\nu(T)^{it}\) is \(W(\nu)\)-linear from \(\nu(H^{(t)})\) to \(\nu(H)\).

*Proof.* Both sides are \(\sigma\)-weakly continuous and linear in \(y\), and \(\lambda(\mathcal A_\nu)\) is a
\(*\)-algebra generating \(W(\nu)\), so it suffices to take \(y=\lambda(f)\), \(f\in\mathcal A_\nu\). By (1.3),
\(\sigma_t(\lambda(f))=\lambda(\delta^{it}f)\), which acts on \(\nu(H)\) as \(U(\delta^{it}f\nu)\). For a section
\(\zeta\) of \(\nu(H)\), Lemma 3.2(c) gives
\[
\big(\nu(T)^{it}U(\delta^{it}f\nu)\zeta\big)_y=\int f(\gamma)\,T_y^{it}\delta(\gamma)^{it}U(\gamma)\zeta_{s(\gamma)}\,
d\nu^y(\gamma)=\int f(\gamma)\,U(\gamma)T^{it}_{s(\gamma)}\zeta_{s(\gamma)}\,d\nu^y(\gamma)=\big(U(f\nu)\nu(T)^{it}
\zeta\big)_y,
\]
where the bounded operator \(T^{it}_y\) passes through the weak integral. The second statement is the first one
rewritten with the description of \(\nu(H^{(t)})\) before Lemma 3.5, because two normal representations of
\(W(\nu)\) that agree on \(\lambda(\mathcal A_\nu)\) agree. \(\square\)

**Theorem 5.3.** Let \(H\) be a \(\Lambda\)-random Hilbert space.

(a) For every positive random operator \(T\) of degree \(1\) on \(H\) there is a unique normal semifinite weight
\(\varphi_T\) on \(\operatorname{End}_\Lambda(H)\) satisfying
\[
\varphi_T\big(\theta_\nu(\xi,\xi)\big)=\int\langle T_x\xi_x,\xi_x\rangle\,d\Lambda_\nu(x)\qquad(\nu\in\mathcal E^+,\
\xi\in D(U,\nu)). \tag{5.1}
\]
For every faithful \(\nu\), \(\nu(T)\) is the spatial derivative of the weight \(\varphi_T\circ\nu^{-1}\) on
\(W(\nu)'\) with respect to \(\psi_\nu\).

(b) The map \(T\mapsto\varphi_T\) is a bijection from positive random operators of degree \(1\) onto normal semifinite
weights on \(\operatorname{End}_\Lambda(H)\). The weight \(\varphi_T\) is faithful iff \(T_x\) is nonsingular for
\(\Lambda\)-almost every \(x\).

*Proof.* *Step 1: one faithful \(\nu\).* Fix \(\nu\) faithful. By Lemma 5.2 and (S4) there is a unique normal
semifinite weight \(\varphi^\nu\) on \(W(\nu)'\) with \(d\varphi^\nu/d\psi_\nu=\nu(T)\). Put \(\Phi_\nu=\varphi^\nu
\circ\nu\), a normal semifinite weight on \(\operatorname{End}_\Lambda(H)\) by (Q5). If \(\xi\in D(U,\nu)\) and
\(\int\|\xi_x\|^2d\Lambda_\nu<\infty\), then by Lemma 5.1 and (S2)
\[
\Phi_\nu(\theta_\nu(\xi,\xi))=\varphi^\nu(\theta^\psi(\xi',\xi'))=\langle\nu(T)\xi',\xi'\rangle=\int\langle T_x\xi_x,
\xi_x\rangle\,d\Lambda_\nu(x);
\]
the last equality is the description of the form of a direct integral: \(\xi'\in\operatorname{dom}\nu(T)^{1/2}\)
iff \(\xi_x\in\operatorname{dom}T_x^{1/2}\) almost everywhere and \(\int\|T_x^{1/2}\xi_x\|^2<\infty\).

This domain identity is Theorem 3.6(3)–(4) of Unbounded decomposable operators and measurable spectral decomposition applied to the square-root multiplier, together with Corollary 6 of Spectral products, transport and inverse domains. It retains both the almost-everywhere fibre-domain condition and the integrability of the squared fibre norms.

For general \(\xi\in D(U,\nu)\), choose Borel sets \(Z_n\uparrow G^{(0)}\) with \(\Lambda_\nu(Z_n)<\infty\) (standing
assumption) and put \(\xi^n=1_{Z_n}\xi\). Then \(\xi^n\in D(U,\nu)\) with the same constant, and by (1.2)
\(\theta_\nu(\xi^n,\xi^n)_y=\int1_{Z_n}(s(\gamma))(U(\gamma)\xi_{s(\gamma)})(U(\gamma)\xi_{s(\gamma)})^*d\nu^y(\gamma)\)
increases to \(\theta_\nu(\xi,\xi)_y\) for every \(y\). So \(\theta_\nu(\xi^n,\xi^n)\uparrow\theta_\nu(\xi,\xi)\) in
\(\operatorname{End}_\Lambda(H)\), and normality and monotone convergence give (5.1) for \(\xi\) and \(\nu\).

*Step 2: a comparison.* Let \(\nu_1\) be faithful and \(\nu_2=(g\circ s)\nu_1\) with \(0\le g\le1\). For \(\xi\in
D(U,\nu_2)\), the section \(g^{1/2}\xi\) lies in \(D(U,\nu_1)\), since
\(\int|\langle\alpha,U(\gamma)g(s(\gamma))^{1/2}\xi_{s(\gamma)}\rangle|^2d\nu_1^y=\int|\langle\alpha,U(\gamma)
\xi_{s(\gamma)}\rangle|^2d\nu_2^y\), and (1.2) gives \(\theta_{\nu_1}(g^{1/2}\xi,g^{1/2}\xi)=\theta_{\nu_2}(\xi,\xi)\).
Using \(\Lambda_{\nu_2}=g\Lambda_{\nu_1}\) (R2) and Step 1 for \(\nu_1\),
\[
\Phi_{\nu_1}(\theta_{\nu_2}(\xi,\xi))=\int g(x)\langle T_x\xi_x,\xi_x\rangle\,d\Lambda_{\nu_1}(x)=\int\langle
T_x\xi_x,\xi_x\rangle\,d\Lambda_{\nu_2}(x).
\]

*Step 3: independence.* Let \(\nu\) be faithful and \(\nu'\in\mathcal E^+\) arbitrary. Then \(\nu_1=\nu+\nu'\) is
faithful and \(\nu=(g\circ s)\nu_1\), \(\nu'=(g'\circ s)\nu_1\) with \(0\le g,g'\le1\) by (R1). By Step 2,
\(\Phi_{\nu_1}\) satisfies (5.1) on the operators \(\theta_\nu(\xi,\xi)\); so does \(\Phi_\nu\), by Step 1. By
Corollary 4.3, \(\Phi_{\nu_1}=\Phi_\nu\). By Step 2 again, \(\Phi_{\nu_1}\) satisfies (5.1) on the operators
\(\theta_{\nu'}(\xi,\xi)\). Hence \(\varphi_T:=\Phi_\nu\) does not depend on the faithful \(\nu\) and satisfies (5.1)
for all \(\nu'\). Uniqueness follows from Corollary 4.3, and the last assertion of (a) holds by construction.

*Step 4: (b).* Fix \(\nu\) faithful. If \(\varphi_{T_1}=\varphi_{T_2}\), then by (a) and (S2) \(\nu(T_1)=\nu(T_2)\),
so \(T_{1,x}=T_{2,x}\) for \(\Lambda_\nu\)-almost every \(x\), and \(T_1=T_2\) by Lemma 3.4. Let \(\varphi\) be a
normal semifinite weight on \(\operatorname{End}_\Lambda(H)\) and \(S=d(\varphi\circ\nu^{-1})/d\psi_\nu\). By (S4),
\(S\) is homogeneous of degree \(-1\), which by the argument of Lemma 5.2 means that \(S^{it}\) is \(W(\nu)\)-linear
from \(\nu(H^{(t)})\) to \(\nu(H)\). Lemma 3.5 gives a positive random operator \(T\) of degree \(1\) with
\(\nu(T)=S\); then \(\varphi_T\circ\nu^{-1}\) and \(\varphi\circ\nu^{-1}\) have the same spatial derivative, so
\(\varphi_T=\varphi\) by (S2). Finally, by (S4) \(\varphi_T\) is faithful iff \(\nu(T)\) is nonsingular, that is, iff
\(T_x\) is nonsingular for \(\Lambda_\nu\)-almost every \(x\); the set where \(T_x\) is singular is saturated by Lemma
3.2, so this is the same as \(\Lambda\)-almost everywhere. \(\square\)

*Reference:* [Connes 1979, Section VI, Lemma 3] asserts that every \(\xi\in D(U,\nu)\) defines a vector \(\xi'\) of
\(\nu(H)\) with \(\theta^\psi(\xi',\xi')=\nu(\theta_\nu(\xi,\xi))\), and derives (5.1) from it. Such a vector exists only
when \(\int\|\xi_x\|^2d\Lambda_\nu<\infty\) (for \(G=\mathbb R\) with only units, \(\nu^x=\varepsilon_x\), \(\Lambda_\nu\)
Lebesgue measure, \(H_x=\mathbb C\) and \(\xi=1\), it does not), so Lemma 5.1 assumes this and Step 1 reaches every
\(\xi\) by truncation.

Heuristically, (5.1) says \(\varphi_T(A)=\int\operatorname{Trace}(T_xA_x)\,d\Lambda(x)\): for \(A=\theta_\nu(\xi,\xi)\)
the "integrand" is \(\operatorname{Trace}(T_yA_y)=\int\langle T_yU(\gamma)\xi_x,U(\gamma)\xi_x\rangle
d\nu^y(\gamma)=\int\delta(\gamma)^{-1}\langle T_x\xi_x,\xi_x\rangle d\nu^y(\gamma)\) (with \(x=s(\gamma)\)), a sum
over the orbit of \(y\), and (5.1) is what the modular relation (1.1) makes of "integrating it over the orbit
space". We write
\(\varphi_T(A)=\int\operatorname{Trace}(T_xA_x)\,d\Lambda(x)\) as a notation for \(\varphi_T(A)\), and
\(\int\operatorname{Trace}(T_x)\,d\Lambda(x)\) for \(\varphi_T(1)\).

**Corollary 5.4.** Let \(T\), \(T_1\), \(T_2\) be positive random operators of degree \(1\), nonsingular almost
everywhere, so that the weights \(\varphi_T\), \(\varphi_{T_j}\) are faithful. Then:

(a) \(\sigma^{\varphi_T}_t(A)=\big(T_x^{it}A_xT_x^{-it}\big)_x\) for \(A\in\operatorname{End}_\Lambda(H)\);

(b) \((D\varphi_{T_2}:D\varphi_{T_1})_t=\big(T_{2,x}^{it}T_{1,x}^{-it}\big)_x\).

*Proof.* The families on the right have degree \(0\) by Lemma 3.2(b), since the factors \(\delta(\gamma)^{\pm it}\)
cancel; they are bounded, so they are elements of \(\operatorname{End}_\Lambda(H)\). Fix \(\nu\) faithful. By Theorem
5.3(a), \(\nu(T)=d(\varphi_T\circ\nu^{-1})/d\psi_\nu\), and (S3) gives \(\nu(\sigma_t^{\varphi_T}(A))=\nu(T)^{it}\nu(A)
\nu(T)^{-it}\), which is the image under \(\nu\) of the family in (a). Likewise (S3) gives \(\nu((D\varphi_{T_2}:
D\varphi_{T_1})_t)=\nu(T_2)^{it}\nu(T_1)^{-it}\). Since \(\nu\) is injective (Q5), (a) and (b) follow. \(\square\)

**Proposition 5.5 (transport).** (a) Let \(V\in\operatorname{Hom}_\Lambda(H_1,H_2)\) be an isometry and \(T_1\) a
positive random operator of degree \(1\) on \(H_1\). Then \(T_2=VT_1V^*\), which is \(T_1\) transported to
\(VV^*H_2\) and \(0\) on \((1-VV^*)H_2\), is a positive random operator of degree \(1\) on \(H_2\), and
\(\varphi_{T_2}(X)=\varphi_{T_1}(V^*XV)\) for \(X\in\operatorname{End}_\Lambda(H_2)_+\).

(b) Let \(H=\bigoplus_iH_i\) (countable sum), \(V_i\) the inclusions and \(T=\bigoplus_iT_i\). Then
\(\varphi_T(X)=\sum_i\varphi_{T_i}(V_i^*XV_i)\) for \(X\in\operatorname{End}_\Lambda(H)_+\).

*Proof.* (a) Degree \(1\) is clear from (3.1) since \(V\) has degree \(0\). Both sides are normal weights in \(X\).
For \(\xi\in D(U_2,\nu)\), \(V^*\theta_\nu(\xi,\xi)V=\theta_\nu(V^*\xi,V^*\xi)\) by (1.2), and \(\langle T_2\xi,\xi
\rangle=\|T_1^{1/2}V^*\xi\|^2=\langle T_1V^*\xi,V^*\xi\rangle\) fibrewise. So both weights take the value
\(\int\langle T_{1,x}V_x^*\xi_x,V_x^*\xi_x\rangle d\Lambda_\nu\) on \(\theta_\nu(\xi,\xi)\), and Corollary 4.3 gives
equality. (b) Both sides are normal weights, and on \(\theta_\nu(\xi,\xi)\) both equal \(\sum_i\int\langle
T_{i,x}V_{i,x}^*\xi_x,V_{i,x}^*\xi_x\rangle d\Lambda_\nu\), because the quadratic form of a direct sum is the sum of
the quadratic forms. \(\square\)

**Example 5.6 (one orbit).** Let \(X\) be a standard Borel space with a \(\sigma\)-finite measure \(\beta\neq0\) and
\(G=X\times X\) the pair groupoid, \(r(y,x)=y\), \(s(y,x)=x\), \(\delta=1\). A transverse function is
\(\nu_\beta^y=\varepsilon_y\times\beta\) (the measure \(\beta\) placed on \(G^y=\{y\}\times X\)); every proper
transverse function has this form. Transverse measures are \(\Lambda(\nu_\beta)=c\,\beta(X)\), \(c\ge0\): indeed,
\(\Lambda_{\nu_\beta}\) must be a multiple \(c_\beta\beta\) for \(m_{\nu_\beta}=\Lambda_{\nu_\beta}\times\beta\) to be
invariant under the flip, and (1.1), applied to the indicator function of a rectangle \(A\times A'\) with
\(0<\beta(A')<\infty\) and \(0<\beta'(A)<\infty\), gives \(c_\beta\beta(A')\beta'(A)=c_{\beta'}\beta'(A)\beta(A')\), so
\(c_\beta=c_{\beta'}\).
Using \(U(x_0,x)\) to identify every \(H_x\) with \(K=H_{x_0}\), a section is a function \(\xi:X\to K\) and
\(\theta_{\nu_\beta}(\xi,\xi)=\int_X\xi(x)\xi(x)^*d\beta(x)\) in \(\operatorname{End}_\Lambda(H)=\mathcal L(K)\) (we take
\(c>0\); intertwiners are constant families under this identification). A
positive operator of degree \(1\) is a single positive operator \(T_0\) on \(K\), and (5.1) reads
\[
\varphi_T\Big(\int\xi(x)\xi(x)^*d\beta(x)\Big)=c\int\langle T_0\xi(x),\xi(x)\rangle d\beta(x),
\]
so \(\varphi_T=c\operatorname{Tr}(T_0^{1/2}\,\cdot\,T_0^{1/2})\). The orbit space is one point carrying mass \(c\).

## 6. Averaging along orbits and the operator-valued weight \(E_\nu\)

For a Hilbert space \(K\) and a positive self-adjoint \(S\) on \(K\), put \(S_\varepsilon=S(1+\varepsilon S)^{-1}\)
(bounded) and
\[
\omega_S(B)=\sup_{\varepsilon>0}\operatorname{Tr}\big(S_\varepsilon^{1/2}BS_\varepsilon^{1/2}\big)\qquad(B\in
\mathcal L(K)_+).
\]
This is the usual weight "\(\operatorname{Trace}(S\,\cdot\,)\)".

**Lemma 6.1.** \(\omega_S\) is a normal weight on \(\mathcal L(K)\), and for every strongly convergent sum
\(B=\sum_j\eta_j\eta_j^*\),
\[
\omega_S(B)=\sum_j\langle S\eta_j,\eta_j\rangle .
\]
In particular \(\omega_S(X^*X)=\sum_k\langle SX^*e_k,X^*e_k\rangle\) for an orthonormal basis \((e_k)\), which is
\(\|XS^{1/2}\|_{HS}^2\) when \(S\) is bounded.

*Proof.* The function \(t\mapsto t(1+\varepsilon t)^{-1}\) increases as \(\varepsilon\downarrow0\), so \(S_\varepsilon\)
increases, and \(\operatorname{Tr}(S_\varepsilon^{1/2}\eta\eta^*S_\varepsilon^{1/2})=\langle S_\varepsilon\eta,\eta
\rangle=\int t(1+\varepsilon t)^{-1}\,d\mu_\eta(t)\) increases to \(\int t\,d\mu_\eta(t)=\langle S\eta,\eta\rangle\) by
monotone convergence (\(\mu_\eta\) the spectral measure of \(\eta\)). Each \(B\mapsto\operatorname{Tr}(S_\varepsilon^{1/2}
BS_\varepsilon^{1/2})\) is a normal weight, and an increasing limit of normal weights is a normal weight (two suprema
commute). By normality \(\operatorname{Tr}(S_\varepsilon^{1/2}BS_\varepsilon^{1/2})=\sum_j\langle S_\varepsilon\eta_j,
\eta_j\rangle\), and taking the supremum over \(\varepsilon\) (monotone in both indices) gives the formula. For
\(B=X^*X=\sum_k(X^*e_k)(X^*e_k)^*\) we get the second statement. \(\square\)

Let \(\nu\in\mathcal E^+\). Let \(P_\nu=\int^\oplus\mathcal L(H_x)\,d\Lambda_\nu(x)\), the von Neumann algebra of
decomposable operators on \(\nu(H)\); it is of type I, and \(\nu\) maps \(\operatorname{End}_\Lambda(H)\) into it. For
a positive random operator \(T\) of degree \(1\) put
\[
\rho^\nu_T(B)=\int\omega_{T_x}(B_x)\,d\Lambda_\nu(x)\qquad(B\in(P_\nu)_+). \tag{6.1}
\]
The integrand is Borel: with a measurable orthonormal frame \((\xi^k)\) it is \(\sup_n\sum_k\langle B_xT_{1/n,x}^{1/2}
\xi^k_x,T_{1/n,x}^{1/2}\xi^k_x\rangle\). Each functional \(B\mapsto\int_Z\langle B_xa_x,a_x\rangle d\Lambda_\nu\) with
\(\Lambda_\nu(Z)<\infty\) and \(a\) bounded is a normal vector functional, and \(\rho^\nu_T\) is an increasing limit of
countable sums of such functionals; so \(\rho^\nu_T\) is a normal weight. If \(\tau_\nu=\int\operatorname{Tr}\,
d\Lambda_\nu\) denotes the canonical fns trace of \(P_\nu\) and \(T\) is nonsingular, then \(\rho^\nu_T\) is the weight
\(\tau_h\) of (B3) with \(h=\nu(T)\); hence it is fns, \(\sigma^{\rho^\nu_T}_t=\operatorname{Ad}\nu(T)^{it}\), and
\((D\rho^\nu_{T_2}:D\rho^\nu_{T_1})_t=\nu(T_2)^{it}\nu(T_1)^{-it}\).

**Proposition 6.2 (averaging formula).** Let \(\nu\in\mathcal E^+\) and let \(B=(B_x)\) be a bounded Borel family of
positive operators such that the family
\[
C_y=\int_{G^y}U(\gamma)B_{s(\gamma)}U(\gamma)^*\,d\nu^y(\gamma)\qquad(\text{weak integral}) \tag{6.2}
\]
is bounded. Then:

(a) \(C\) is an intertwiner, \(C\in\operatorname{End}_G(H)\);

(b) for every bounded Borel section \(\xi\), the section \(B^{1/2}\xi\) lies in \(D(U,\nu)\);

(c) \(C=\sum_j\theta_\nu(B^{1/2}\xi^j,B^{1/2}\xi^j)\) for every measurable orthonormal frame \((\xi^j)\) of \(H\);

(d) \(\rho^\nu_T(B)=\varphi_T(C)\) for every positive random operator \(T\) of degree \(1\).

*Proof.* (a) For \(\gamma_0:x\to y\), left invariance \(\gamma_0\nu^x=\nu^y\) gives \(U(\gamma_0)C_xU(\gamma_0)^*=
\int U(\gamma_0\gamma)B_{s(\gamma)}U(\gamma_0\gamma)^*d\nu^x(\gamma)=C_y\). Measurability is clear.

(b) For \(\alpha\in H_y\), by the Cauchy–Schwarz inequality \(|\langle\alpha,U(\gamma)B_x^{1/2}\xi_x\rangle|^2=
|\langle B_x^{1/2}U(\gamma)^*\alpha,\xi_x\rangle|^2\le\|\xi\|_\infty^2\langle U(\gamma)B_xU(\gamma)^*\alpha,\alpha\rangle\).
Integrating over \(\nu^y\) gives the bound \(\|\xi\|_\infty^2\|C\|\|\alpha\|^2\).

(c) With \(\eta^j=B^{1/2}\xi^j\) we have \(\sum_j\eta^j_x\eta^{j*}_x=B_x^{1/2}\big(\sum_j\xi^j_x\xi^{j*}_x\big)
B_x^{1/2}=B_x\), so by (1.2) and monotone convergence, \(\sum_j\theta_\nu(\eta^j,\eta^j)_y=\int U(\gamma)
\big(\sum_j\eta^j\eta^{j*}\big)_{s(\gamma)}U(\gamma)^*d\nu^y(\gamma)=C_y\).

(d) By (c), normality, (5.1), monotone convergence and Lemma 6.1,
\[
\varphi_T(C)=\sum_j\int\langle T_x\eta^j_x,\eta^j_x\rangle\,d\Lambda_\nu(x)=\int\sum_j\langle T_x\eta^j_x,\eta^j_x\rangle
\,d\Lambda_\nu(x)=\int\omega_{T_x}(B_x)\,d\Lambda_\nu(x).\qquad\square
\]

**Theorem 6.3.** Let \(\nu\in\mathcal E^+\) be faithful, and identify \(\operatorname{End}_\Lambda(H)\) with its image
under \(\nu\) in \(P_\nu\). There is a unique operator-valued weight \(E_\nu\) from \(P_\nu\) to
\(\operatorname{End}_\Lambda(H)\) with \(\varphi_T\circ E_\nu=\rho^\nu_T\) for one (equivalently, for every)
nonsingular positive random operator \(T\) of degree \(1\). It is faithful, normal and semifinite, and:

(a) \(\varphi_T\circ E_\nu=\rho^\nu_T\) for every positive random operator \(T\) of degree \(1\), singular or not;

(b) \(E_\nu(B)=C\) whenever \(B\in(P_\nu)_+\) and the average \(C\) of (6.2) is bounded; in particular
\(E_\nu(\eta\eta^*)=\theta_\nu(\eta,\eta)\) for \(\eta\in D(U,\nu)\).

*Proof.* *Existence.* \(\operatorname{End}_\Lambda(H)\) has a faithful normal state, which is \(\varphi_{T_0}\) for some
nonsingular \(T_0\) by Theorem 5.3(b). The fns weight \(\rho^\nu_{T_0}\) has modular group \(\operatorname{Ad}
\nu(T_0)^{it}\), whose restriction to \(\operatorname{End}_\Lambda(H)\) is \(\sigma^{\varphi_{T_0}}\) (Corollary 5.4).
By (B1) there is a unique fns operator-valued weight \(E_\nu\) with \(\varphi_{T_0}\circ E_\nu=\rho^\nu_{T_0}\). For
another nonsingular \(T_1\), (B3), Corollary 5.4(b) and (B1) give
\[
(D\rho^\nu_{T_1}:D\rho^\nu_{T_0})_t=\nu(T_1)^{it}\nu(T_0)^{-it}=(D\varphi_{T_1}:D\varphi_{T_0})_t=
(D(\varphi_{T_1}\circ E_\nu):D(\varphi_{T_0}\circ E_\nu))_t,
\]
so \(\varphi_{T_1}\circ E_\nu=\rho^\nu_{T_1}\) by (B2). Uniqueness is part of (B1).

*(b), rank one.* Let \(\eta\in D(U,\nu)\). For nonsingular \(T\), \(\varphi_T(E_\nu(\eta\eta^*))=\rho^\nu_T(\eta\eta^*)=
\int\langle T_x\eta_x,\eta_x\rangle d\Lambda_\nu=\varphi_T(\theta_\nu(\eta,\eta))\) by (5.1). Let \(\omega\) be a normal
positive functional on \(\operatorname{End}_\Lambda(H)\) and \(\omega_0\) a faithful normal state. The faithful normal
positive functionals \(\omega_0\) and \(\omega+\omega_0\) are of the form \(\varphi_T\) with \(T\) nonsingular. Since
\(\omega_0(E_\nu(\eta\eta^*))=\omega_0(\theta_\nu(\eta,\eta))<\infty\), subtraction gives \(\omega(E_\nu(\eta\eta^*))=
\omega(\theta_\nu(\eta,\eta))\). An element of the extended positive part is determined by its values on normal
positive functionals, so \(E_\nu(\eta\eta^*)=\theta_\nu(\eta,\eta)\).

*(b), general.* With \(\eta^j=B^{1/2}\xi^j\in D(U,\nu)\) as in Proposition 6.2, \(B=\sum_j\eta^j\eta^{j*}\), and
normality of \(E_\nu\) and Proposition 6.2(c) give \(E_\nu(B)=\sum_j\theta_\nu(\eta^j,\eta^j)=C\).

*(a).* Let \(T\) be arbitrary and \(e=s(T)\in\operatorname{End}_\Lambda(H)\) (Lemma 3.2). The random Hilbert space
\((1-e)H\) carries a nonsingular positive random operator \(R\) of degree \(1\) (Theorem 5.3(b) applied to a faithful
normal state of \(\operatorname{End}_\Lambda((1-e)H)\)). Then \(T_1=T|_{eH}\oplus R\) is nonsingular of degree \(1\).
By Proposition 5.5, \(\varphi_{T_1}(eXe)=\varphi_{T|_{eH}}(eXe|_{eH})=\varphi_T(X)\) for \(X\ge0\), and by normality
this extends to the extended positive part. Fibrewise, \(\omega_{T_{1,x}}(e_xB_xe_x)=\omega_{T_x}(B_x)\): write
\(B_x=\sum\eta_j\eta_j^*\) and use \(\langle T_{1}e\eta,e\eta\rangle=\langle T\eta,\eta\rangle\) (Lemma 6.1), so
\(\rho^\nu_{T_1}(eBe)=\rho^\nu_T(B)\). Since \(E_\nu(eBe)=eE_\nu(B)e\) (B1),
\[
\varphi_T(E_\nu(B))=\varphi_{T_1}(eE_\nu(B)e)=\varphi_{T_1}(E_\nu(eBe))=\rho^\nu_{T_1}(eBe)=\rho^\nu_T(B).\qquad\square
\]

**Example 6.4.** \(E_\nu(1)\) is the average of the constant family \(1\), namely the family of scalars
\((\nu^y(1)\,1_{H_y})_y\) (a function constant on orbits), provided it is bounded. So if \(\nu^y(1)=1\) for all \(y\),
\(E_\nu\) is a faithful normal conditional expectation of \(P_\nu\) onto \(\operatorname{End}_\Lambda(H)\), given by
\(E_\nu(B)_y=\int U(\gamma)B_{s(\gamma)}U(\gamma)^*d\nu^y(\gamma)\). In that case \(\operatorname{End}_\Lambda(H)\) is the
range of a conditional expectation from a type I algebra.

**Proposition 6.5.** Let \(F\) be a proper random variable, \(H=L^2\circ F\), and for a Borel \(f\ge0\) on
\(X=\bigsqcup F(x)\) let \(M(f)\) be the family of multiplications by \(f\). For every faithful \(\nu\) and bounded
\(f\ge0\),
\[
E_\nu(M(f))=M(\nu*f),
\]
where the right side is the element \(\sup_kM(\min(\nu*f,k))\) of the extended positive part; it is bounded iff
\(\nu*f\) is essentially bounded for the measure \(\int\alpha^x\,d\Lambda_\nu(x)\) on \(X\), in particular when
\(\nu*f\) is bounded.

*Proof.* The function \(\nu*f\) is \(G\)-invariant (R4), so \(M(\min(\nu*f,k))\in\operatorname{End}_\Lambda(H)\). As
in Example 3.3(b), \(U(\gamma)M(f)_xU(\gamma)^*\) is multiplication by \(z\mapsto f(\gamma^{-1}z)\) on \(F(y)\), and by
Fubini the weak integral over \(\nu^y\) is multiplication by \((\nu*f)(z)=\int f(\gamma^{-1}z)d\nu^y(\gamma)\). If
\(\nu*f\) is bounded, Theorem 6.3(b) applies. In general, take \(f_1>0\) with \(\nu*f_1=1\) and \(g_k=
\min(f,kf_1)\uparrow f\); then \(\nu*g_k\le k\), \(E_\nu(M(g_k))=M(\nu*g_k)\uparrow M(\nu*f)\), and normality of
\(E_\nu\) concludes. For a bounded invariant \(g\ge0\), \(\nu(M(g))\) is multiplication by \(g\) on
\(\nu(H)=\int^\oplus L^2(F(x),\alpha^x)\,d\Lambda_\nu(x)\), whose norm is the essential supremum of \(g\) for
\(\int\alpha^x\,d\Lambda_\nu(x)\), and \(A\mapsto\nu(A)\) is isometric (Q3). So the increasing family
\(M(\min(\nu*f,k))\) is bounded exactly when \(\nu*f\) is essentially bounded. \(\square\)

## 7. The modular spectrum and traces

A reference for the spectral theory used here is [Arveson 1974]. For a self-adjoint operator \(A\) write
\(\operatorname{Sp}A\) for its spectrum.

**Proposition 7.1.** Let \(\mu\) be a \(\sigma\)-finite measure on a standard Borel space \(Y\), \((A_y)\) a
measurable field of self-adjoint operators on \((K_y)\), \(A=\int^\oplus A_y\,d\mu\), \(P=\int^\oplus\mathcal L(K_y)
\,d\mu\), and \(\alpha_t=\operatorname{Ad}e^{itA}\) on \(P\). For \(p\in\mathbb R\) and \(\varepsilon>0\) let
\[
Y_\varepsilon(p)=\{y\in Y:(\operatorname{Sp}A_y-\operatorname{Sp}A_y)\cap(p-\varepsilon,p+\varepsilon)\neq\emptyset\}.
\]
Then \(Y_\varepsilon(p)\) is Borel, and \(p\in\operatorname{Sp}(\alpha)\) iff \(\mu(Y_\varepsilon(p))>0\) for every
\(\varepsilon>0\).

*Proof.* Let \(e_y\) be the spectral measure of \(A_y\). For rationals \(a,b,r\) with \(r>0\) and \([a-b-2r,a-b+2r]
\subset(p-\varepsilon,p+\varepsilon)\), let \(Y_{a,b,r}=\{y:e_y((a-r,a+r))\neq0\neq e_y((b-r,b+r))\}\), a Borel set.
If \(y\in Y_{a,b,r}\), there are \(\lambda_1\in\operatorname{Sp}A_y\cap[a-r,a+r]\) and \(\lambda_2\in
\operatorname{Sp}A_y\cap[b-r,b+r]\), so \(y\in Y_\varepsilon(p)\). Conversely, if \(\lambda_1-\lambda_2\in
(p-\varepsilon,p+\varepsilon)\) with \(\lambda_j\) in the spectrum, choose a small rational \(r>0\) and rationals \(a,b\) within
\(r\) of \(\lambda_1,\lambda_2\); then \(y\in Y_{a,b,r}\). So \(Y_\varepsilon(p)\) is the countable union of the
\(Y_{a,b,r}\).

Suppose \(\mu(Y_\varepsilon(p))>0\) for all \(\varepsilon\). Fix \(\varepsilon\) and \((a,b,r)\) as above with
\(\mu(Y_{a,b,r})>0\). Choosing, for \(y\in Y_{a,b,r}\), the first section \(\xi^n\) of a fixed countable dense family
with \(e_y((a-r,a+r))\xi^n_y\neq0\), and normalizing, we get a Borel unit section \(u\) with \(u_y\in e_y((a-r,a+r))K_y\);
likewise \(v\) for \((b-r,b+r)\). Let \(B_y=u_yv_y^*\) on \(Y_{a,b,r}\) and \(B_y=0\) elsewhere. Then \(B\neq0\), and
with \(E_1=\int^\oplus e_y((a-r,a+r))\), \(E_2=\int^\oplus e_y((b-r,b+r))\), we have \(B=E_1BE_2\) and \(\alpha_t(B)=
u_tBv_t^*\) where \(u_t=e^{itA}E_1\), \(v_t=e^{itA}E_2\) are unitary groups on the ranges of \(E_1\), \(E_2\), with spectra in
\([a-r,a+r]\), \([b-r,b+r]\). By (B4)(iv), \(\operatorname{Sp}_\alpha(B)\subset[a-b-2r,a-b+2r]\subset
(p-\varepsilon,p+\varepsilon)\); by (B4)(ii),(i) it is a nonempty subset of \(\operatorname{Sp}(\alpha)\). As
\(\varepsilon\) is arbitrary and \(\operatorname{Sp}(\alpha)\) is closed, \(p\in\operatorname{Sp}(\alpha)\).

Suppose \(\mu(Y_\varepsilon(p))=0\) for some \(\varepsilon\). Choose \(f\in L^1(\mathbb R)\) (a Schwartz function) with
\(\hat f(p)=1\) and \(\hat f\) supported in \([p-\varepsilon/2,p+\varepsilon/2]\). For \(B\in P\),
\((\alpha(f)B)_y=\int f(t)e^{itA_y}B_ye^{-itA_y}dt\) for almost every \(y\). For \(y\notin Y_\varepsilon(p)\) the fibre
action \(\alpha^y=\operatorname{Ad}e^{itA_y}\) has spectrum in the closure of \(\operatorname{Sp}A_y-\operatorname{Sp}
A_y\) (B4)(iv), which does not meet the open interval \((p-\varepsilon,p+\varepsilon)\). So \(\hat f\) vanishes on a
neighbourhood of \(\operatorname{Sp}_{\alpha^y}(B_y)\), and \(\alpha^y(f)B_y=0\) by (B4)(iii). Hence \(\alpha(f)=0\)
while \(\hat f(p)\neq0\): \(p\notin\operatorname{Sp}(\alpha)\). \(\square\)

**Theorem 7.2.** Assume that \(G\) has trivial isotropy \(\Lambda\)-almost everywhere (Q7). Let \(T\) be a
nonsingular positive random operator of degree \(1\) and \(\varphi=\varphi_T\). For \(p\in\mathbb R\) and \(\varepsilon>0\) the set
\[
X_\varepsilon(p)=\{x\in G^{(0)}:(\operatorname{Sp}\log T_x-\operatorname{Sp}\log T_x)\cap(p-\varepsilon,p+\varepsilon)
\neq\emptyset\}
\]
is saturated and Borel, and
\[
p\in\operatorname{Sp}(\sigma^\varphi)\iff X_\varepsilon(p)\text{ is not }\Lambda\text{-negligible for any }
\varepsilon>0.
\]
In multiplicative notation: \(e^p\) belongs to the modular spectrum of \(\varphi\) iff for every \(\varepsilon\) a
non-negligible set of \(x\) has two spectral values of \(T_x\) with ratio in \((e^{p-\varepsilon},e^{p+\varepsilon})\).

*Proof.* By Lemma 3.2, \(\log T_y=U(\gamma)(\log T_x)U(\gamma)^*-\log\delta(\gamma)\), so \(\operatorname{Sp}\log T_y\)
is a translate of \(\operatorname{Sp}\log T_x\) and \(X_\varepsilon(p)\) is saturated; it is Borel by Proposition 7.1.
Fix a faithful \(\nu\) and put \(P=P_\nu\), \(\rho=\rho^\nu_T\), \(\mathcal M=\nu(\operatorname{End}_\Lambda(H))\subset
P\). By Section 6, \(\sigma^\rho_t=\operatorname{Ad}\nu(T)^{it}\), and Proposition 7.1 with \(A_x=\log T_x\) and
\(\mu=\Lambda_\nu\) (together with (R3)) shows that \(\operatorname{Sp}(\sigma^\rho)\) is the right-hand set. It
remains to show \(\operatorname{Sp}(\sigma^\varphi)=\operatorname{Sp}(\sigma^\rho)\). By Corollary 5.4,
\(\sigma^\rho|_{\mathcal M}=\sigma^\varphi\).

Let \(\mathcal D\) be the diagonal algebra of \(\nu(H)\). It commutes with every decomposable operator, in particular
with \(\mathcal M\) and with \(\nu(T)^{it}\); so \(\sigma^\rho\) is trivial on \(\mathcal D\).

*\(\mathcal M\) and \(\mathcal D\) generate \(P\).* Let \(D\) be the countable set of (Q7) and \(b^{\xi,\eta}=
\nu(\theta_\nu(\xi,\eta))\in\mathcal M\) for \(\xi,\eta\in D\). The points with nontrivial isotropy lie in a
\(\Lambda\)-negligible set, so for \(\Lambda_\nu\)-almost every \(y\) the fibres \(b^{\xi,\eta}_y\) span a weakly dense
\(*\)-subalgebra of \(\mathcal L(H_y)\). By (B5), the von Neumann algebra generated by \(\mathcal D\) and the
\(b^{\xi,\eta}\) is \(\int^\oplus\mathcal L(H_y)\,d\Lambda_\nu(y)=P\). A fortiori \(\mathcal M\) and \(\mathcal D\)
generate \(P\).

*Equality of spectra.* If \(\sigma^\rho(f)=0\) then \(\sigma^\varphi(f)=0\) by restriction. Conversely let
\(\sigma^\varphi(f)=0\). For \(a\in\mathcal M\), \(b\in\mathcal D\), \(\sigma^\rho_t(ab)=\sigma^\varphi_t(a)b\), so
\(\sigma^\rho(f)(ab)=(\sigma^\varphi(f)a)b=0\). The span of such products is a unital \(*\)-algebra (\(\mathcal M\) and
\(\mathcal D\) commute), which is \(\sigma\)-weakly dense in \(P\) by the double commutant theorem, and
\(\sigma^\rho(f)\) is \(\sigma\)-weakly continuous, so \(\sigma^\rho(f)=0\). The two actions have the same annihilating
functions, hence the same spectrum. \(\square\)

The same argument works when the isotropy is nontrivial, provided that \(\delta=1\) on \(G^y_y\), that
\(U(G^y_y)''\) is a factor, and that the fibres \(\theta_\nu(\xi,\eta)_y\) generate the commutant \(U(G^y_y)'\) for
\(\Lambda\)-almost every \(y\): then the relative commutant \(\mathcal M'\cap P=\int^\oplus U(G^y_y)''\,d\Lambda_\nu\)
replaces \(\mathcal D\). [Connes 1979, Section VI, Corollary 6] states the result under the first two conditions and
obtains the third from its general generation statement for the isotropy commutant, which is not proved in this course
(Remark 5.2 of "Square-integrable representations and random operators").

**Corollary 7.3.** Assume that \(G\) has trivial isotropy \(\Lambda\)-almost everywhere. A positive random operator
\(T\) of degree \(1\) gives a trace \(\varphi_T\) iff \(T_x\) is a scalar \(\lambda_x1_{H_x}\) for \(\Lambda\)-almost
every \(x\). The implication "scalar \(\Rightarrow\) trace" holds without the assumption on the isotropy.

*Proof.* Suppose \(T_x=\lambda_x1\). The set \(Y=\{\lambda_x>0\}\) is saturated (\(\lambda_y=\delta(\gamma)^{-1}
\lambda_x\)) and \(e=s(T)=(1_Y(x)1)\) is central in \(\operatorname{End}_\Lambda(H)\), since scalar families commute
with intertwiners. By (S2) and Theorem 5.3(a), \(s(\varphi_T)=e\), so \(\varphi_T(X)=\varphi_T(eXe)\) (B2). On
\(e\operatorname{End}_\Lambda(H)e=\operatorname{End}_\Lambda(eH)\), \(\varphi_T\) is \(\varphi_{T|eH}\) (Proposition
5.5), which is faithful with modular group \(\operatorname{Ad}\lambda_x^{it}=\mathrm{id}\) (Corollary 5.4), hence a
trace (B2). For \(A\in\operatorname{End}_\Lambda(H)\), \(eA=eAe\) and
\(\varphi_T(AA^*)=\varphi_T(eAA^*e)=\varphi_T((eA)(eA)^*)=\varphi_T((eA)^*(eA))=\varphi_T(A^*A)\).

Conversely let \(\varphi_T\) be a trace. Its support \(e=s(T)\) is central (B2). By (Q7) the central elements are
the invariant scalar families, so \(e=(1_Y(x)1)\) for a saturated Borel \(Y\), and \(T_x=0\) for almost every
\(x\notin Y\). The restriction of \(\varphi_T\) to \(\operatorname{End}_\Lambda(eH)\) is a
faithful trace, so its modular group is trivial and its spectrum is contained in \(\{0\}\) (B4)(v). Theorem 7.2, applied to \(eH\)
(the zero fibres off \(Y\) play no role), shows that for each \(p\neq0\) some \(X_\varepsilon(p)\) is negligible. Covering
\(\mathbb R\setminus\{0\}\) by countably many such intervals, we find that for almost every \(x\in Y\) the set
\(\operatorname{Sp}\log T_x-\operatorname{Sp}\log T_x\) is \(\{0\}\), so \(\operatorname{Sp}\log T_x\) is one point and
\(T_x\) is scalar. \(\square\)

**Example 7.4.** Some hypothesis on the isotropy is needed in Theorem 7.2 and Corollary 7.3. If \(G\) is a single
compact group \(\Gamma\neq\{e\}\) (unit
space a point, \(\delta=1\)) and \(H=L^2(\Gamma)\), the isotropy representation is the regular representation, which is
not factorial, and \(\operatorname{End}_\Lambda(H)=R(\Gamma)\) is a direct sum of matrix algebras. A positive operator of
degree \(1\) is a positive \(T\) commuting with \(\lambda(\Gamma)\), that is, \(T\in R(\Gamma)\) affiliated; taking
\(T\) a non-scalar central projection plus \(1\) gives a non-scalar \(T\) for which \(\varphi_T\) is still a trace,
since \(T\) is central in \(R(\Gamma)\) and \(\sigma^{\varphi_T}=\operatorname{Ad}T^{it}=\mathrm{id}\).

## 8. Integrable modular groups and the centralizer

A reference for integrable actions is [Connes–Takesaki 1977]. Let \(\alpha\) be a \(\sigma\)-weakly continuous action of
\(\mathbb R\) on a von Neumann algebra \(M\). For \(x\in M_+\), \(E^\alpha(x)=\int_{\mathbb R}
\alpha_t(x)\,dt\) is the element of the extended positive part of the fixed-point algebra \(M^\alpha\) given by
\(\omega(E^\alpha(x))=\int\omega(\alpha_t(x))dt\). We call \(x\) *integrable* if \(E^\alpha(x)\) is bounded; the
integrable elements form a hereditary cone \(\mathcal I_\alpha\) (if \(0\le y\le x\in\mathcal I_\alpha\) then
\(y\in\mathcal I_\alpha\)).

**Lemma 8.1.** The following are equivalent; when they hold, \(\alpha\) is called *integrable*.

(1) \(\mathfrak n_\alpha=\{x\in M:x^*x\in\mathcal I_\alpha\}\) is \(\sigma\)-weakly dense in \(M\).

(2) \(\bigvee_{x\in\mathcal I_\alpha}s(x)=1\).

(3) There is an increasing net in \(\mathcal I_\alpha\) with supremum \(1\) (if \(M\) has separable predual, one can
take a sequence).

*Proof.* (1)\(\Rightarrow\)(2): the \(\sigma\)-weak closure of the left ideal \(\mathfrak n_\alpha\) is \(Mq\) with \(q\)
the join of the right supports \(r(x)=s(x^*x)\), \(x\in\mathfrak n_\alpha\); density forces \(q=1\).
(2)\(\Rightarrow\)(3): the proof of Lemma 4.1 applies to \(\mathcal S=\mathcal I_\alpha\) with (ii) replaced by
heredity, because \(x(1-x)^{-1}\le(1-\|x\|)^{-1}x\), \((a'+b')(1+a'+b')^{-1}\le a'+b'\) and \(nx(1+nx)^{-1}\le nx\),
and with (iii) replaced by (2). If \(M\) has separable predual, it has a faithful normal state \(\omega\); choosing
elements \(x_n\ge x_{n-1}\) of the net with \(\omega(1-x_n)<1/n\) gives a sequence with supremum \(1\). (3)\(\Rightarrow\)(1): if \(y_i\uparrow1\)
in \(\mathcal I_\alpha\) and \(a\in M\), then \(ay_i^{1/2}\in\mathfrak n_\alpha\) because \(y_i^{1/2}a^*ay_i^{1/2}\le
\|a\|^2y_i\), and \(ay_i^{1/2}\to a\) strongly. \(\square\)

For an fns weight \(\varphi\), the fixed-point algebra of \(\sigma^\varphi\) is the centralizer \(M_\varphi\), and we write
\(E^\varphi=E^{\sigma^\varphi}\).

**Lemma 8.2.** Let \(N\subset M\) be von Neumann algebras, \(E\) an fns operator-valued weight
from \(M\) to \(N\), \(\varphi\) an fns weight on \(N\) and \(\psi=\varphi\circ E\).

(a) If \(\sigma^\varphi\) is integrable, so is \(\sigma^\psi\).

(b) Suppose there is an increasing net \((x_i)\) in \(M_\psi\cap M_+\) with \(E(x_i)\) bounded and \(\sup_ix_i=1\). If
\(\sigma^\psi\) is integrable, so is \(\sigma^\varphi\).

*Proof.* Recall from (B1) that \(\sigma^\psi_t|_N=\sigma^\varphi_t\) and \(E\circ\sigma^\psi_t=\sigma^\varphi_t\circ
E\).

(a) Let \(y_j\uparrow1\) in \(\mathcal I_{\sigma^\varphi}\). Viewed in \(M\), \(E^\psi(y_j)=\int\sigma^\psi_t(y_j)dt=
\int\sigma^\varphi_t(y_j)dt\) is bounded, so Lemma 8.1(3) holds for \(\sigma^\psi\).

(b) Let \(y\in\mathcal I_{\sigma^\psi}\), \(Y=E^\psi(y)\), and \(z_i=E(x_i^{1/2}yx_i^{1/2})\le\|y\|E(x_i)\), a bounded
element of \(N_+\). Since \(x_i\) lies in the centralizer, \(\sigma^\psi_t(x_i^{1/2})=x_i^{1/2}\), and
\[
\sigma^\varphi_t(z_i)=E(\sigma^\psi_t(x_i^{1/2}yx_i^{1/2}))=E(x_i^{1/2}\sigma^\psi_t(y)x_i^{1/2}).
\]
For \(\omega\in N_*^+\), \(\omega\circ E\) is a normal weight, hence a sum of normal positive functionals, and Tonelli's
theorem gives
\[
\int\omega(\sigma^\varphi_t(z_i))\,dt=(\omega\circ E)\Big(x_i^{1/2}\Big(\int\sigma^\psi_t(y)dt\Big)x_i^{1/2}\Big)\le
\|Y\|\,\omega(E(x_i)).
\]
So \(E^\varphi(z_i)\le\|Y\|E(x_i)\) is bounded: \(z_i\in\mathcal I_{\sigma^\varphi}\). Now take \(y=y_j\) from an increasing
net \(y_j\uparrow1\) in \(\mathcal I_{\sigma^\psi}\), and let \(p\in N\) be a projection orthogonal to all supports
\(s(z_{i,j})\). Then \(pz_{i,j}p=0\); since \(x_i^{1/2}y_jx_i^{1/2}\uparrow x_i\), normality of \(E\) gives
\(pE(x_i)p=\sup_jpz_{i,j}p=0\), so \(E(px_ip)=0\) and \(px_ip=0\) because \(E\) is faithful. Taking the supremum over
\(i\), \(p=0\). Lemma 8.1(2) holds for \(\sigma^\varphi\). \(\square\)

*Reference:* [Connes 1979, Section VI, Lemma 13] states Lemma 8.2(b) for any increasing net in the domain of \(E\)
inside the centralizer, without requiring \(\sup_ix_i=1\). This fails: take \(N=\mathbb C\subset M=B(L^2(\mathbb R))\),
\(\varphi(\lambda)=\lambda\) and \(E=\omega_{e^Q}\) (Section 6), \(Q\) multiplication by the variable; then \(\psi=E\), the
only such net is \(0\), \(\sigma^\psi\) is integrable (Proposition 8.3), and \(\sigma^\varphi\) is trivial, hence not
integrable. So we assume \(\sup_ix_i=1\), which is what the applications provide.

We need the fibrewise criterion. Recall that for a vector \(a\) and a self-adjoint \(A\) with spectral measure \(e\),
\(\mu_a(I)=\langle e(I)a,a\rangle\) and \(\mu_{a,\zeta}(I)=\langle e(I)a,\zeta\rangle\); then
\(|\mu_{a,\zeta}(I)|^2\le\mu_a(I)\mu_\zeta(I)\). We use the following fact of harmonic analysis: a finite
complex Borel measure \(\mu\) on \(\mathbb R\) has \(\hat\mu(t)=\int e^{it\lambda}d\mu(\lambda)\) square integrable iff
\(\mu=g\,d\lambda\) with \(g\in L^2\), and then \(\int|\hat\mu|^2dt=2\pi\int|g|^2d\lambda\).

*Proof of this fact.* Write \(\check f(t)=\int f(\lambda)e^{it\lambda}\,d\lambda\) for \(f\in L^1(\mathbb R)\). For the
pairing \(e^{it\lambda}\), the dual Haar measure of \(d\lambda\) is \(dt/2\pi\) (put \(t=2\pi\xi\) in The Fourier
inversion theorem and the dual Haar measure, Proposition 3.2),
and \(\check f\) differs from the Fourier transform there by the reflection \(t\mapsto-t\). So, by The Plancherel theorem,
Theorem 1.1, \(f\mapsto\check f\) on \(L^1\cap L^2\) extends to a unitary operator
\(\mathcal F\) of \(L^2(d\lambda)\) onto \(L^2(dt/2\pi)\). If \(\mu=g\,d\lambda\) with \(g\in L^2\), then \(g\in L^1\),
because \(\mu\) is finite; so \(\hat\mu=\check g=\mathcal Fg\) and \(\int|\hat\mu|^2dt=2\pi\int|g|^2d\lambda\).
Conversely, let \(\hat\mu\in L^2\) and put \(g=\mathcal F^{-1}\hat\mu\). For \(\varepsilon>0\) let
\(G_\varepsilon(\lambda)=(4\pi\varepsilon)^{-1/2}e^{-\lambda^2/4\varepsilon}\), an even function with
\(\check G_\varepsilon(t)=e^{-\varepsilon t^2}\). The function \((\mu*G_\varepsilon)(\lambda)=\int
G_\varepsilon(\lambda-\kappa)\,d\mu(\kappa)\) lies in \(L^1\cap L^2\), with norms at most \(|\mu|(\mathbb R)\) times those
of \(G_\varepsilon\), and Fubini's theorem gives \(\mathcal F(\mu*G_\varepsilon)=\hat\mu\,e^{-\varepsilon t^2}\). Also
\(\mathcal F(g*G_\varepsilon)=(\mathcal Fg)\,e^{-\varepsilon t^2}\): this is Fubini's theorem when \(g\in L^1\cap L^2\),
and both sides are continuous in \(g\in L^2\). As \(\mathcal F\) is injective, \(\mu*G_\varepsilon=g*G_\varepsilon\)
almost everywhere. Let \(\phi\in C_c(\mathbb R)\). By Fubini's theorem and evenness, \(\int\phi\,(\mu*G_\varepsilon)\,d\lambda
=\int(\phi*G_\varepsilon)\,d\mu\), which tends to \(\int\phi\,d\mu\), because \(\phi*G_\varepsilon\to\phi\) uniformly with
\(|\phi*G_\varepsilon|\le\sup|\phi|\). And \(\int\phi\,(g*G_\varepsilon)\,d\lambda\to\int\phi g\,d\lambda\), because
\(\|g*G_\varepsilon-g\|_2\le\int G_\varepsilon(s)\|g(\cdot-s)-g\|_2\,ds\to0\) by the continuity of translation in \(L^2\).
So \(\int\phi\,d\mu=\int\phi g\,d\lambda\) for every \(\phi\in C_c(\mathbb R)\). For a bounded open interval \(I\), take
\(\phi_n\in C_c(\mathbb R)\) with \(0\le\phi_n\uparrow1_I\); dominated convergence gives \(\mu(I)=\int_Ig\,d\lambda\). On a
bounded interval \(J\), the Borel sets \(E\subseteq J\) with \(\mu(E)=\int_Eg\,d\lambda\) form a Dynkin class that contains
the open subintervals, a family closed under finite intersections; so \(\mu(E)=\int_Eg\,d\lambda\) for every bounded Borel
set \(E\), and then for every Borel set. Hence \(\mu=g\,d\lambda\), and
\(\int|\hat\mu|^2dt=\int|\mathcal Fg|^2dt=2\pi\int|g|^2d\lambda\). \(\square\)

**Proposition 8.3.** Let \(Y,\mu,(A_y),P,\alpha\) be as in Proposition 7.1. Then \(\alpha\) is integrable iff the
spectral measure of \(A_y\) is absolutely continuous (with respect to Lebesgue measure) for \(\mu\)-almost every \(y\).

*Proof.* *One fibre.* Let \(A\) act on \(K\) and \(a,\zeta\in K\). Then \(\langle e^{itA}aa^*e^{-itA}\zeta,\zeta\rangle=
|\langle e^{itA}a,\zeta\rangle|^2=|\hat\mu_{a,\zeta}(t)|^2\), so
\[
\langle E^\alpha(aa^*)\zeta,\zeta\rangle=\int|\hat\mu_{a,\zeta}(t)|^2\,dt. \tag{8.1}
\]
If \(\mu_a=w_a\,d\lambda\) with \(w_a\le N\), then \(\mu_{a,\zeta}\ll d\lambda\) and its density \(g\) satisfies
\(|g|^2\le w_aw_\zeta\) almost everywhere (differentiate the inequality \(|\mu_{a,\zeta}(I)|^2\le\mu_a(I)\mu_\zeta(I)\)
on intervals shrinking to a point; here \(\mu_{a,\zeta}=\mu_{a,P\zeta}\) with \(P\) the projection on the absolutely
continuous subspace, so only the density of \(\mu_{P\zeta}\) enters). Hence \(\int|g|^2\le N\|\zeta\|^2\) and
\(E^\alpha(aa^*)\le2\pi N\). If instead \(a\) has a nonzero component \(a_s\) in the singular subspace, take
\(\zeta=a_s\): the singular subspace reduces \(A\), so \(\mu_{a,\zeta}=\mu_{a_s}\) is a nonzero singular measure, its
Fourier transform is not square integrable, and (8.1) is infinite. Consequently, if \(b\in\mathcal L(K)_+\) is integrable,
writing \(b=\sum_ja_ja_j^*\) we get \(E^\alpha(a_ja_j^*)\le E^\alpha(b)\) bounded, so every \(a_j\) is absolutely
continuous and \(s(b)\) is below the projection on the absolutely continuous subspace.

*Only if.* By Lemma 8.1(2) and separability there are integrable \(B^n\in P_+\) with \(\bigvee s(B^n)=1\). Since
\(\langle E^\alpha(B)\zeta,\zeta\rangle=\int\!\!\int\langle\alpha^y_t(B_y)\zeta_y,\zeta_y\rangle\,dt\,d\mu(y)\) by
Tonelli, a bounded \(E^\alpha(B^n)\) forces \(E^{\alpha^y}(B^n_y)\) to be bounded for almost every \(y\) (test on a
countable family of sections dense in every fibre). By the one-fibre result, for almost every \(y\) every \(s(B^n_y)\)
lies below the absolutely continuous projection of \(A_y\); and \(\bigvee_ns(B^n_y)=1\) almost everywhere, so \(A_y\) is
absolutely continuous.

*If.* Let \((\xi^m)\) be a countable family of Borel sections with \(\|\xi^m_y\|\le1\) for all \(y\), dense in the
unit ball of every fibre, and \(\mu^m_y=\mu_{\xi^m_y}\). To obtain such a family, take all finite Gaussian-rational combinations of the Borel orthonormal fundamental sequence supplied by Measurable fields of Hilbert spaces and their direct integrals, Theorem 3.1, and divide each section pointwise by \(\max(1,\|\cdot\|)\). Each resulting section is Borel and bounded by one. The combinations are dense in each fibre, and the continuous map \(v\mapsto v/\max(1,\|v\|)\), which fixes the unit ball, shows that their normalized images are dense in that unit ball. The
function \(w^m(y,\lambda)=\limsup_k2^k\mu^m_y(D_k(\lambda))\), with \(D_k(\lambda)\) the dyadic interval of length
\(2^{-k}\) containing \(\lambda\), is Borel in \((y,\lambda)\) and is a density of \(\mu^m_y\) when \(\mu^m_y\) is
absolutely continuous (differentiation theorem). Put \(a^{m,N}_y=1_{\{w^m(y,\cdot)\le N\}}(A_y)\xi^m_y\), a Borel section
of norm at most \(1\), and \(B^{m,N}=a^{m,N}a^{m,N*}\in P_+\). Indeed, the cutoff depends jointly on \(y\) and the spectral variable, so its measurability is Lemma 8.2 of Unbounded decomposable operators and measurable spectral decomposition. Its fibre operators are projections, hence the sections \(a^{m,N}\) have norm at most one. Their rank-one fields are measurable and essentially bounded, and therefore define elements of \(P_+\) by Theorems 6.2 and 10.1 of Measurable fields of Hilbert spaces and their direct integrals. For almost every \(y\), \(\mu_{a^{m,N}_y}\) has density \(\le N\), so
\(E^\alpha(B^{m,N})\le2\pi N\) by the one-fibre estimate and Tonelli. As \(N\to\infty\), \(a^{m,N}_y\to
1_{\{w^m<\infty\}}(A_y)\xi^m_y=\xi^m_y\), because \(\{w^m=\infty\}\) is Lebesgue null, hence \(\mu^m_y\)-null. So the
supports of the \(B^{m,N}\) have join \(1\), and \(\alpha\) is integrable by Lemma 8.1. \(\square\)

**Theorem 8.4.** Let \(T\) be a nonsingular positive random operator of degree \(1\) and \(\varphi=\varphi_T\).

(a) If \(\sigma^\varphi\) is integrable, then the spectral measure of \(T_x\) is absolutely continuous for
\(\Lambda\)-almost every \(x\).

(b) If \(T\) is diagonal (Example 3.3(b): \(H=L^2\circ F\) and \(T=M(\rho)\), \(\rho>0\)), the converse holds:
\(\sigma^\varphi\) is integrable iff the spectral measure of \(T_x\) is absolutely continuous for \(\Lambda\)-almost
every \(x\).

*Proof.* Fix a faithful \(\nu\) and let \(\psi=\rho^\nu_T=\varphi\circ E_\nu\) (Theorem 6.3), an fns weight on \(P_\nu\)
with \(\sigma^\psi_t=\operatorname{Ad}\nu(T)^{it}\). By Proposition 8.3 with \(A_x=\log T_x\), \(\sigma^\psi\) is
integrable iff \(\log T_x\) (equivalently \(T_x\), as \(\log\) is a diffeomorphism of \((0,\infty)\) onto \(\mathbb R\))
is absolutely continuous for \(\Lambda_\nu\)-almost every \(x\). The set \(S\) of \(x\) where this fails is saturated,
since \(\log T_y\) is unitarily equivalent to a translate of \(\log T_x\). If \(S\) is contained in a Borel
\(\Lambda_\nu\)-null set \(Z\), then \(S\subset[Z]_\nu\): for \(y\in S\), \(s_*(\nu^y)\) is a nonzero measure carried by
the orbit of \(y\), which lies in \(S\subset Z\). By (R3), \(S\) is then \(\Lambda\)-negligible. So "\(\Lambda_\nu\)-almost
every" may be replaced by "\(\Lambda\)-almost every".

(a) follows from Lemma 8.2(a) applied to \(E_\nu\).

(b) Take \(f_1>0\) with \(\nu*f_1=1\) (R4) and \(f_k=\min(kf_1,1)\). Then \(f_k\uparrow1\), \(\nu*f_k\le k\), so
\(x_k=M(f_k)\) increases to \(1\) and \(E_\nu(x_k)=M(\nu*f_k)\le k\) (Proposition 6.5). As multiplication operators,
\(x_k\) commutes with \(\nu(T)=M(\rho)\), hence lies in the centralizer of \(\psi\). Lemma 8.2(b) shows that
\(\sigma^\varphi\) is integrable when \(\sigma^\psi\) is. \(\square\)

**Example 8.5.** On \(L^\nu\) take \(T=M(\delta^{-1})\) (Example 3.3(c)). The spectral measure of \(T_x\) is
equivalent to the image of \(\nu^x\) under \(\gamma\mapsto\delta(\gamma)^{-1}\). If \(\delta=1\) this is a point mass,
and \(\sigma^{\varphi_T}\) is trivial and not integrable (unless \(H=0\)). If the image measures are absolutely continuous, \(\sigma^{\varphi_T}\) is integrable
by Theorem 8.4(b). This happens, for instance, for the groupoid \(X\rtimes\mathbb R\) of a flow, with
\(\delta(x,t)=e^t\) and \(\nu^x\) Lebesgue measure in the parameter \(t\): the image of Lebesgue measure under
\(t\mapsto e^{-t}\) is equivalent to Lebesgue measure on \((0,\infty)\).

Now suppose that \(\sigma^\varphi\) is integrable, \(\varphi=\varphi_T\) faithful. Discarding a negligible saturated set,
\(A_x=\log T_x\) is absolutely continuous for every \(x\). By (B6) we may write \(H_x=\int^\oplus_{\mathbb R}
H'_{(x,s)}\,ds\), with \(A_x\) acting as multiplication by \(s\), measurably in \(x\). For \(\gamma:x\to y\), Lemma 3.2
gives \(U(\gamma)g(A_x)U(\gamma)^*=g(A_y+c(\gamma))\) for bounded Borel \(g\) (\(c=\log\delta\)): \(U(\gamma)\) carries
multiplication by \(g(s)\) to multiplication by \(g(s+c(\gamma))\). Composing with the shift by \(c(\gamma)\) we obtain an
operator commuting with the diagonal algebra, hence decomposable (B5): there are unitaries
\[
U'(\gamma,s):H'_{(x,s+c(\gamma))}\to H'_{(y,s)},\qquad (U(\gamma)\zeta)(s)=U'(\gamma,s)\,\zeta(s+c(\gamma)),
\]
for almost every \(s\). A Borel choice in \((\gamma,s)\) exists: apply the last clause of (B6) over \(Y=G\) (with the
measure \(m_\nu\), \(\nu\) faithful) to the field \(\gamma\mapsto U(\gamma)\), which intertwines \(\log T_{s(\gamma)}-
c(\gamma)\) with \(\log T_{r(\gamma)}\). In the stable kernel \(G'\) of (R6), \((\gamma,s)\) is an arrow from
\((x,s+c(\gamma))\) to \((y,s)\), so \(U'\) is a Borel family of unitaries along the arrows of \(G'\); since \(U\) is
multiplicative, for each composable pair \((\gamma_1,\gamma_2)\) the relation \(U'(\gamma_1\gamma_2,s)=U'(\gamma_1,s)
U'(\gamma_2,s+c(\gamma_1))\) holds for almost every \(s\), hence (Fubini) for almost every composable pair of \(G'\). Let
\(\mu=\Lambda_\nu\times ds=\Lambda'_{\nu'}\) and \(m'=\mu\circ\nu'\). Since \(U'(\gamma')\) is a unitary from
\(H'_{s(\gamma')}\) onto \(H'_{r(\gamma')}\) for \(m'\)-almost every arrow \(\gamma'\), the Borel function
\(d=\dim H'_{(\cdot)}\) with values in \(\{0,1,\dots,\infty\}\) satisfies \(d\circ r=d\circ s\) \(m'\)-almost
everywhere. This does not make the sets \(\{d=n\}\) saturated after removal of a negligible set, because a field can be
changed on a null set that meets every orbit. Put instead
\[
Y_n=\{y\in G'^{(0)}:\nu'^y(s^{-1}(\{d\neq n\}))=0\}.
\]
These sets are Borel, by the measurability of the kernel \(\nu'\) (R1). They are saturated: for an arrow
\(\gamma'_0:y\to z\), left invariance gives \(\nu'^z=\gamma'_0\nu'^y\), and \(s(\gamma'_0\gamma')=s(\gamma')\). They are
disjoint, because \(\nu'^y\neq0\) for every \(y\). Since \(d(s(\gamma'))=d(y)\) for \(\nu'^y\)-almost every \(\gamma'\),
for \(\mu\)-almost every \(y\), almost every \(y\) lies in \(Y_{d(y)}\). So the complement of \(\bigcup_nY_n\) is a
saturated \(\mu\)-null Borel set, \(\Lambda'\)-negligible by (R3), and \(d=n\) almost everywhere on \(Y_n\). On \(Y_n\)
replace \(H'\) by the constant field \(\ell^2_n\) (\(\mathbb C^n\), or \(\ell^2(\mathbb N)\) for \(n=\infty\)),
identified with \(H'\) on the Borel set \(Y_n\cap\{d=n\}\) by a measurable field of unitaries \(W\)
(Measurable fields of Hilbert spaces and their direct integrals, Theorem 5.1). Replace \(U'(\gamma')\) by
\(W_{r(\gamma')}U'(\gamma')W_{s(\gamma')}^{-1}\) when both ends of \(\gamma'\) lie in \(Y_n\cap\{d=n\}\), and by \(1\)
otherwise. The arrows with an end in the null set \(Y_n\setminus\{d=n\}\) form an \(m'\)-null set, because \(m'\) and
its image under \(\gamma'\mapsto\gamma'^{-1}\) have the same null sets (the modular relation (1.1) for \(\Lambda'\)).
So the new family is still multiplicative for almost every composable pair, and on the reduction of \(G'\) to each
\(Y_n\) it is a Borel map into the unitary group of \(\ell^2_n\), a Polish group. For \(\Lambda_\nu\)-almost every
\(x\) only a null set of \(s\) is affected, so the decomposition \(H_x=\int^\oplus H'_{(x,s)}\,ds\) is unchanged. We
keep the notation \(H'\) and \(U'\). The measure \(\mu\) and the faithful lift \(\nu'\) satisfy the hypothesis of (B7),
by the modular relation (1.1) for \(\Lambda'\). So (B7), applied to the reduction of \(G'\) to each \(Y_n\), yields a
genuine representation, still denoted \(U'\), of \(G'\) on \(H'\), equal to the family above almost everywhere, off a
\(\mu\)-null saturated set, which is \(\Lambda'\)-negligible by (R3). For a section
\(\xi\) of \(H\) we write \(\xi'_{(x,s)}=\xi_x(s)\).

**Lemma 8.6.** With these notations, let \(\nu\in\mathcal E^+\), \(\nu'\) its lift to \(G'\) (R6), and \(\xi\in D(U,\nu)\).
For almost every \(y\) and every \(\alpha\in H_y=\int^\oplus H'_{(y,s)}ds\),
\[
\big\langle E^\varphi(\theta_\nu(\xi,\xi))_y\alpha,\alpha\big\rangle=2\pi\int ds\int\big|\langle\alpha(s),U'(\gamma,s)
\xi'_{s(\gamma,s)}\rangle\big|^2\,d\nu'^{(y,s)}(\gamma,s). \tag{8.2}
\]
In particular, if \(E^\varphi(\theta_\nu(\xi,\xi))\le c\), then for almost every \((y,s)\) (for \(\Lambda'_{\nu'}\)),
\(\int|\langle\beta,U'(\gamma')\xi'_{s(\gamma')}\rangle|^2\,d\nu'^{(y,s)}(\gamma')\le(c/2\pi)\|\beta\|^2\) for all
\(\beta\in H'_{(y,s)}\). If moreover \(\nu\) is faithful, then after removal of a \(\Lambda'\)-negligible saturated set,
\(g\xi'\in D(U',\nu')\) for every Borel \(g\) on \(G'^{(0)}\) with \(0\le g\le1\) and \(g\xi'\) bounded.

*Proof.* By Corollary 5.4(a), \((\sigma^\varphi_t(X))_y=T_y^{it}X_yT_y^{-it}\), and by (1.2),
\[
\langle E^\varphi(\theta_\nu(\xi,\xi))_y\alpha,\alpha\rangle=\int dt\int|\langle T_y^{-it}\alpha,U(\gamma)
\xi_{s(\gamma)}\rangle|^2d\nu^y(\gamma)=\int d\nu^y(\gamma)\int|\langle T_y^{-it}\alpha,\beta_\gamma\rangle|^2dt,
\]
with \(\beta_\gamma=U(\gamma)\xi_{s(\gamma)}\). In the decomposition of \(H_y\), \(T_y^{-it}\alpha=(e^{-its}\alpha(s))\),
so \(\langle T_y^{-it}\alpha,\beta_\gamma\rangle=\int e^{-its}\langle\alpha(s),\beta_\gamma(s)\rangle ds\) is the Fourier
transform of the integrable function \(s\mapsto\langle\alpha(s),\beta_\gamma(s)\rangle\). By Plancherel (valid in
\([0,\infty]\) for integrable functions), \(\int|\cdot|^2dt=2\pi\int|\langle\alpha(s),\beta_\gamma(s)\rangle|^2ds\), and
\(\beta_\gamma(s)=U'(\gamma,s)\xi'_{(x,s+c(\gamma))}=U'(\gamma,s)\xi'_{s(\gamma,s)}\). Exchanging the integrals and using
that \(\nu'^{(y,s)}\) is the image of \(\nu^y\) under \(\gamma\mapsto(\gamma,s)\) gives (8.2). If the left side is at
most \(c\|\alpha\|^2\), the decomposable quadratic form on the right is bounded by \(c\), so its fibres are bounded by
\(c/2\pi\) almost everywhere (test on a countable dense family of sections). The set of points of \(G'^{(0)}\) where
this bound holds is saturated: for \(\gamma'_0:(y_0,s_0)\to(y,s)\), left invariance of \(\nu'\) and unitarity of
\(U'(\gamma'_0)\) turn the integral at \((y,s)\) with the vector \(\beta\) into the integral at \((y_0,s_0)\) with
\(U'(\gamma'_0)^*\beta\). So its complement is a saturated \(\Lambda'_{\nu'}\)-null set, \(\Lambda'\)-negligible by (R3)
when \(\nu'\) is faithful; off it the bound holds everywhere, which is the condition defining \(D(U',\nu')\). Finally,
multiplying by \(g\) only decreases the integrals. \(\square\)

The constant \(2\pi\) comes from the normalizations \(E^\varphi=\int\sigma_t\,dt\) and \(ds\) on \(\mathbb R=\log
\mathbb R_+^*\).

**Theorem 8.7.** Let \(\varphi=\varphi_T\) be faithful with \(\sigma^\varphi\) integrable, and let \(H'\), \(U'\) be as
above.

(a) After removal of a \(\Lambda'\)-negligible saturated set, \((H',U')\) is square integrable: it is a
\(\Lambda'\)-random Hilbert space on the stable kernel \((G',\Lambda')\) of \(\delta\).

(b) The map \(A'\mapsto A\), \(A_x=\int^\oplus A'_{(x,s)}ds\), is an isomorphism of \(\operatorname{End}_{\Lambda'}(H')\)
onto the centralizer \(\operatorname{End}_\Lambda(H)_\varphi\).

*Proof.* (a) By Lemma 8.1(3) there are \(y_n\uparrow1\) in \(\operatorname{End}_\Lambda(H)\) with \(E^\varphi(y_n)\)
bounded; let \(A_n=y_n^{1/2}\), so \(A_n\to1\) strongly and \(E^\varphi(A_nA_n^*)\) is bounded. Let \(\nu\) be faithful and
\(D\) a countable subset of \(D(U,\nu)\) with values total in every fibre (Q2). For \(\xi\in D\), \(A_n\xi\in D(U,\nu)\)
and \(\theta_\nu(A_n\xi,A_n\xi)=A_n\theta_\nu(\xi,\xi)A_n^*\le\|\theta_\nu(\xi,\xi)\|A_nA_n^*\), so
\(E^\varphi(\theta_\nu(A_n\xi,A_n\xi))\) is bounded. By Lemma 8.6, the truncations \(g_k(A_n\xi)'\), \(g_k=
1_{\{\|(A_n\xi)'\|\le k\}}\), lie in \(D(U',\nu')\). Since \(\nu(A_n)\to1\) strongly, a subsequence satisfies
\(A_{n,x}\xi_x\to\xi_x\) for all \(\xi\in D\) and almost every \(x\); so for almost every \(x\) the vectors \(A_{n,x}\xi_x\)
are total in \(H_x\), and then their components \((A_n\xi)'_{(x,s)}\) are total in \(H'_{(x,s)}\) for almost every
\(s\) (a family of sections whose values span a proper subfield at a non-null set of \(s\) cannot be total in the direct
integral). So the countable family of truncations has values total at \(\Lambda'_{\nu'}\)-almost every point of
\(G'^{(0)}\). Let \(Z\) be the null set where this fails. For \(y\notin[Z]_{\nu'}\), \(s(\gamma')\notin Z\) for
\(\nu'^y\)-almost every \(\gamma'\), and a single such \(\gamma'\) already makes \(\{U'(\gamma')\eta_{s(\gamma')}\}\) total.
By the last clause of (Q2), applied on \(G'\) with the faithful \(\nu'\) and the countable family of truncations, the
sections \(U'(f\nu')\eta\) form a countable subset of \(D(U',\nu')\) whose values are total at every point off
\([Z]_{\nu'}\). By (R3), \([Z]_{\nu'}\) is \(\Lambda'\)-negligible, and \(U'\) is square integrable off it.

(b) Let \(A'\in\operatorname{End}_{\Lambda'}(H')\) (a bounded Borel intertwiner). Then \(A_x=\int^\oplus A'_{(x,s)}ds\)
is bounded and Borel. The unitary \(U(\gamma)\) is the direct integral of the unitaries that decompose it, and these
agree with the \(U'(\gamma,s)\) for almost every \(s\), for \(m_\nu\)-almost every \(\gamma\), since the genuine
representation \(U'\) agrees with the family constructed above almost everywhere. So \(U(\gamma)A_x=A_yU(\gamma)\) for
\(m_\nu\)-almost every \(\gamma\). By (Q5), as in the proof of surjectivity below, this almost-everywhere intertwiner
defines an element of \(\operatorname{End}_\Lambda(H)\), equal to \((A_x)\) almost everywhere, which we still denote
\(A\);
\(A_x\) commutes with multiplication by bounded functions of \(s\), in particular with \(T_x^{it}\), which is
multiplication by \(e^{its}\); so \(\sigma^\varphi_t(A)=A\) by Corollary 5.4(a). The map is a normal \(*\)-homomorphism. It is
injective: if \(A=0\) as a random operator, then \(A'_{(x,s)}=0\) for \(\Lambda_\nu\times ds\)-almost every \((x,s)\),
and the set where \(A'\neq0\) is saturated in \(G'^{(0)}\), hence \(\Lambda'\)-negligible (R3). It is surjective: if
\(A\in\operatorname{End}_\Lambda(H)_\varphi\), then \(T_x^{it}A_xT_x^{-it}=A_x\) for all rational \(t\) and, by Lemma
3.4 and continuity, for all \(t\) and almost every \(x\); so \(A_x\) commutes with the unitary group of \(\log T_x\),
hence with its spectral measure, and is decomposable, \(A_x=\int^\oplus A'_{(x,s)}ds\) (B6). The family \(A'\) is an
intertwiner for \(U'\) almost everywhere, because \(A\) is one for \(U\), and it is a genuine element of
\(\operatorname{End}_{\Lambda'}(H')\) by (Q5) applied on \(G'\) (the equivalence with \(W(\nu')\)-modules turns an
almost-everywhere intertwiner, which gives a \(W(\nu')\)-linear operator, into a random operator). \(\square\)

The assembly of \(A'\) into \(A\) uses Theorem 7.1(4) of Unbounded decomposable operators and measurable spectral decomposition; its decomposition over the product field uses Theorem 8.3 of Unbounded decomposable operators and measurable spectral decomposition. These field results do not replace the saturated-null-set reductions (R3), the representation correspondence (Q5), or the almost-homomorphism theorem (B7) used to obtain a genuine groupoid representation.

Theorem 8.7 identifies the centralizer of an integrable weight on \(\operatorname{End}_\Lambda(H)\) with an algebra of
random operators on the stable kernel of \(\delta\), whose transverse measure \(\Lambda'\) has modulus \(\delta\circ h\).
This is the groupoid form of the continuous decomposition of [Connes–Takesaki 1977]: the centralizer of an integrable
weight is semifinite, and its centre carries the flow of weights.

## 9. Integration formulas

In this section \(F\) is a proper random variable, \(X=\bigsqcup F(x)\), \(H=L^2\circ F\) with \((U(\gamma)g)(z)=
\delta(\gamma)^{1/2}g(\gamma^{-1}z)\), and \(M(f)\) denotes multiplication by a Borel function \(f\ge0\) on \(X\).
Every random Hilbert space is isomorphic to a subspace of such an \(H\) (Q2 and Example 3.3(c)), so the formulas below,
combined with Proposition 5.5, compute \(\varphi_T\) in general.

**Proposition 9.1.** Let \(\nu_i\in\mathcal E^+\) and Borel \(f_i\ge0\) on \(X\) (\(i\) in a countable set) with
\(\sum_i\nu_i*f_i=1\). For every positive random operator \(T\) of degree \(1\) and every \(A\in\operatorname{End}
_\Lambda(H)_+\),
\[
\varphi_T(A)=\sum_i\int\omega_{T_x}\big(A_x^{1/2}M(f_i)_xA_x^{1/2}\big)\,d\Lambda_{\nu_i}(x), \tag{9.1}
\]
where for unbounded \(f_i\) the integrand means \(\sup_k\omega_{T_x}(A_x^{1/2}M(\min(f_i,k))_xA_x^{1/2})\). Formally,
\(\varphi_T(A)=\sum_i\int\operatorname{Trace}(A_x^{1/2}M(f_i)A_x^{1/2}T_x)\,d\Lambda_{\nu_i}(x)\).

*Proof.* Put \(f_{i,k}=\min(f_i,k)\). The family \(B_x=A_x^{1/2}M(f_{i,k})_xA_x^{1/2}\) is bounded, and since \(A\) is an
intertwiner, its average (6.2) for \(\nu_i\) is \(A_y^{1/2}\big(\int U(\gamma)M(f_{i,k})U(\gamma)^*d\nu_i^y\big)A_y^{1/2}=
A_y^{1/2}M(\nu_i*f_{i,k})_yA_y^{1/2}\) (by the computation in the proof of Proposition 6.5, which does not use
faithfulness), and it is bounded by \(\|A\|\). By Proposition 6.2(d),
\[
\varphi_T\big(A^{1/2}M(\nu_i*f_{i,k})A^{1/2}\big)=\int\omega_{T_x}\big(A_x^{1/2}M(f_{i,k})_xA_x^{1/2}\big)\,
d\Lambda_{\nu_i}(x).
\]
As \(k\to\infty\), \(\sum_iA^{1/2}M(\nu_i*f_{i,k})A^{1/2}\) increases to \(A^{1/2}M(\sum_i\nu_i*f_i)A^{1/2}=A\). Normality of
\(\varphi_T\) and monotone convergence give (9.1). \(\square\)

**Lemma 9.2 (the local trace).** For every positive random operator \(T\) of degree \(1\) on \(H=L^2\circ F\) there is
a \(G\)-invariant Borel function \(w_T:X\to[0,\infty]\) such that, for every \(x\) and every Borel \(g\ge0\),
\[
\alpha_T^x(g):=\sup_k\omega_{T_x}\big(M(\min(g,k))_x\big)=\int g\,w_T\,d\alpha^x .
\]
The measures \(\alpha^x_T\) satisfy \(\gamma_*\alpha^x_T=\delta(\gamma)\alpha^y_T\) for \(\gamma:x\to y\).

*Proof.* Let \((e^j)\) be a measurable orthonormal frame of \(H\) and \(T_{n,x}=T_x(1+T_x/n)^{-1}\). For bounded
\(g\), \(\operatorname{Tr}(T_n^{1/2}M(g)T_n^{1/2})=\sum_j\langle M(g)T_n^{1/2}e^j,T_n^{1/2}e^j\rangle=\int g\,w_n\,
d\alpha^x\) with \(w_n=\sum_j|T_n^{1/2}e^j|^2\), a Borel function on \(X\). These integrals increase with \(n\) for every
\(g\ge0\), so \(w_n\le w_{n+1}\) \(\alpha^x\)-almost everywhere, and \(w=\sup_nw_n\) satisfies \(\omega_{T_x}(M(g))=\int
gw\,d\alpha^x\) by monotone convergence; the case of unbounded \(g\) follows. For \(\gamma:x\to y\), \(U(\gamma)^*T_y
U(\gamma)=\delta(\gamma)^{-1}T_x\) and \(U(\gamma)^*M(g)_yU(\gamma)=M(g\circ\gamma)_x\) give \(\alpha_T^y(g)=
\delta(\gamma)^{-1}\alpha_T^x(g\circ\gamma)\), which is the transformation rule; the same rule for \(\alpha\) then
shows \(w(\gamma^{-1}z)=w(z)\) for \(\alpha^y\)-almost every \(z\in F(y)\), for each \(\gamma\in G^y\). Now fix
\(f_1>0\) with \(\nu*f_1=1\) (\(\nu\) faithful) and put \(w_T(z)=\int f_1(\gamma^{-1}z)w(\gamma^{-1}z)\,
d\nu^{\pi(z)}(\gamma)\). It is \(G\)-invariant, like every function \(\nu*h\). By Tonelli on \(\nu^y\times\alpha^y\),
for \(\alpha^y\)-almost every \(z\) we have \(w(\gamma^{-1}z)=w(z)\) for \(\nu^y\)-almost every \(\gamma\), hence
\(w_T(z)=w(z)(\nu*f_1)(z)=w(z)\). So \(w_T\,\alpha^x=w\,\alpha^x=\alpha^x_T\). \(\square\)

We call \(F_T:x\mapsto(F(x),\alpha^x_T)\) the *local trace* of \(T\). The measures \(\alpha^x_T\) need not be
\(\sigma\)-finite (for instance \(\alpha_T^x(g)=\operatorname{Trace}M(g)=\infty\) when \(T=1\) and \(\alpha^x\) has no
atoms). But the truncations \(F_{T,n}:x\mapsto(F(x),\min(w_T,n)\alpha^x)\) are proper random variables of modulus
\(\delta\) in the sense of (R4), increasing to \(F_T\), and we define \(\int F_T\,d\Lambda=\sup_n\int F_{T,n}\,d\Lambda\).
By monotone convergence \(\int F_T\,d\Lambda=\int\alpha^x_T(f)\,d\Lambda_\nu(x)\) whenever \(\nu\) is faithful and
\(\nu*f=1\).

**Corollary 9.3.** \(\varphi_T(1)=\int F_T\,d\Lambda\).

*Proof.* Take a faithful \(\nu\) and \(f\ge0\) with \(\nu*f=1\), and apply (9.1) with one term and \(A=1\):
\(\varphi_T(1)=\int\alpha^x_T(f)\,d\Lambda_\nu(x)\). \(\square\)

So \(\varphi_T(1)=\int\operatorname{Trace}(T_x)\,d\Lambda(x)\) is the integral over the orbit space of the random
variable "local trace of \(T\)", which is how the notation should be read.

**Corollary 9.4 (convolution operators).** Let \(\nu\in\mathcal E^+\) be faithful, \(E=(E_x)\) a measurable field of
Hilbert spaces on \(G^{(0)}\), and \(H_x=L^2(G^x,\nu^x;s^*E)\), the square-integrable sections \(\xi\) with
\(\xi(\gamma)\in E_{s(\gamma)}\), with \((U(\gamma)\xi)(\gamma')=\xi(\gamma^{-1}\gamma')\). Let \(\Delta^{-1}\) be the
family of multiplications by \(\delta^{-1}\), a nonsingular positive random operator of degree \(1\). Let \(k\) be a
Borel field with \(k(\eta)\in\mathcal L(E_{s(\eta)},E_{r(\eta)})\), and \(T\in\operatorname{End}_\Lambda(H)\) given by
\[
(T_x\xi)(\gamma)=\int k(\gamma^{-1}\gamma')\xi(\gamma')\,d\nu^x(\gamma')
\]
for bounded sections \(\xi\) with \(\nu^x\)-finite support (the integral converging absolutely). Then
\[
\varphi_{\Delta^{-1}}(T^*T)=\int_G\|k(\eta)\|_{HS}^2\,\delta(\eta)^{-1}\,dm_\nu(\eta),\qquad m_\nu=\Lambda_\nu\circ\nu .
\]
In the notation above, \(\int\operatorname{Trace}(\delta_x^{-1}|T_x|^2)\,d\Lambda(x)=\int\|k\|_{HS}^2\,\delta^{-1}
\,d(\Lambda_\nu\circ\nu)\).

*Proof.* \(H\) is square integrable: with a measurable orthonormal frame of \(E\), \(H\) is a direct sum of regular
representations \(L^{(1_{Y_j}\circ s)\nu}\), \(Y_j=\{\dim E\ge j\}\). The operator \(\Delta^{-1}\) has degree \(1\) by
Example 3.3(c). Choose \(g>0\) with \(\nu(g)=1\) and put \(f=\tilde g\), \(f_k=\min(f,k)\). Multiplication by \(f\) on
\(H_x\) averages to multiplication by \((\nu*f)(\gamma)=\int f(\gamma'^{-1}\gamma)d\nu^{r(\gamma)}(\gamma')=
\nu(g)(s(\gamma))=1\) (substitute \(\gamma'=\gamma\eta\) and use left invariance). As in Proposition 9.1, with
\(B_x=T_x^*M(f_k)T_x\) (average \(T^*M(\nu*f_k)T\)) and normality,
\[
\varphi_{\Delta^{-1}}(T^*T)=\sup_k\int\omega_{\delta^{-1}}\big(T_x^*M(f_k)T_x\big)\,d\Lambda_\nu(x).
\]
With \(S_\varepsilon\) the multiplication by \(s_\varepsilon=\delta^{-1}(1+\varepsilon\delta^{-1})^{-1}\) and
\(Y=M(f_k)^{1/2}T_x\), Lemma 6.1 gives \(\omega_{\delta^{-1}}(Y^*Y)=\sup_\varepsilon\|YS_\varepsilon^{1/2}\|_{HS}^2\).
The operator \(YS_\varepsilon^{1/2}\) agrees on a dense subspace with the integral operator of kernel
\(f_k(\gamma)^{1/2}k(\gamma^{-1}\gamma')s_\varepsilon(\gamma')^{1/2}\); a bounded operator of this kind has Hilbert–Schmidt
norm equal to the \(L^2\) norm of its kernel, both sides possibly infinite (if it is Hilbert–Schmidt it has an \(L^2\)
kernel, which must agree almost everywhere with the given one; if the kernel is \(L^2\), the associated Hilbert–Schmidt
operator agrees with it on a dense subspace). Letting \(\varepsilon\to0\) and \(k\to\infty\) (monotone convergence), and
substituting \(\gamma'=\gamma\eta\),
\[
\varphi_{\Delta^{-1}}(T^*T)=\int d\Lambda_\nu(x)\int d\nu^x(\gamma)\,f(\gamma)\delta(\gamma)^{-1}h(s(\gamma)),\qquad
h(z)=\int\|k(\eta)\|_{HS}^2\delta(\eta)^{-1}d\nu^z(\eta).
\]
The right side is \(\int\Phi\,\delta^{-1}dm_\nu\) with \(\Phi(\gamma)=f(\gamma)h(s(\gamma))\). By the modular relation
(R2), \(\int\Phi\delta^{-1}dm_\nu=\int\Phi(\gamma^{-1})dm_\nu(\gamma)=\int h(y)\big(\int g\,d\nu^y\big)d\Lambda_\nu(y)=
\int h\,d\Lambda_\nu\), which is the claimed integral. \(\square\)

**Proposition 9.5 (invariance under proper homomorphisms).** Let \(\Lambda\), \(\Lambda'\) be \(\sigma\)-finite
transverse measures of moduli \(\delta\), \(\delta'\) on \(G\), \(G'\), and \(h:G\to G'\) a proper homomorphism with
\(h(\Lambda)=\Lambda'\) and \(\delta=\delta'\circ h\). Let \(H'\) be a \(\Lambda'\)-random Hilbert space, \(H=h^*H'\), \(T'\)
a positive random operator of degree \(1\) on \(H'\) and \(T=h^*T'=(T'_{h(x)})\). Then \(T\) is a positive random
operator of degree \(1\) on \(H\), and
\[
\int\operatorname{Trace}(T_x)\,d\Lambda(x)=\int\operatorname{Trace}(T'_{x'})\,d\Lambda'(x'),\quad\text{that is,}\quad
\varphi_T(1)=\varphi_{T'}(1).
\]

*Proof.* \(H\) is \(\Lambda\)-random by (Q2). For \(\gamma:x\to y\), \(U(\gamma)T_x=U'(h(\gamma))T'_{h(x)}=
\delta'(h(\gamma))T'_{h(y)}U'(h(\gamma))=\delta(\gamma)T_yU(\gamma)\).

*Reduction.* By (Q2) and Example 3.3(c) there are a proper random variable \(F'\) on \(G'\) and an isometry
\(V\in\operatorname{Hom}_{\Lambda'}(H',L^2\circ F')\) (take \(F'=\mathbb N\times(x\mapsto(G'^x,\delta'^{-1}\nu'^x))\)).
By Proposition 5.5(a), \(\varphi_{VT'V^*}(1)=\varphi_{T'}(V^*V)=\varphi_{T'}(1)\). Likewise \(h^*V\) is an isometry from
\(H\) into \(h^*(L^2\circ F')=L^2\circ h^*F'\), with \(h^*(VT'V^*)=(h^*V)T(h^*V)^*\), so the value at \(1\) is unchanged
on the left too. So we may assume \(H'=L^2\circ F'\) and \(H=L^2\circ h^*F'\); \(h^*F'\) is proper (R5).

*Computation.* Since \(F(x)=F'(h(x))\) and \(T_x=T'_{h(x)}\), the local traces satisfy \(\alpha^x_T=\alpha'^{h(x)}_{T'}\),
and with \(w_T=w_{T'}\) (on \(F(x)=F'(h(x))\)) the truncations satisfy \(F_{T,n}=h^*F'_{T',n}\). By (R5),
\(\int F_{T,n}\,d\Lambda=\int F'_{T',n}\,d\Lambda'\) for every \(n\). Taking suprema and using Corollary 9.3 on both sides
gives the result. Here \(w_{T'}\), read on \(F(x)=F'(h(x))\), is \(G\)-invariant because \(G\) acts on
\(\bigsqcup_xF'(h(x))\) through \(h\); so it is an admissible choice of \(w_T\), and the truncations are random variables
on \(G\). \(\square\)

## 10. Formal dimension

In this section \(\delta=1\). Then the identity family \(1\) is a positive random operator of degree \(1\) on every
random Hilbert space.

**Definition 10.1.** The *formal dimension* of a \(\Lambda\)-random Hilbert space \(H\) is
\[
\dim_\Lambda(H)=\varphi_1(1)=\int\operatorname{Trace}(1_{H_x})\,d\Lambda(x)\in[0,\infty].
\]
The weight \(\operatorname{Tr}_\Lambda=\varphi_1\) on \(\operatorname{End}_\Lambda(H)\) is characterized by
\(\operatorname{Tr}_\Lambda(\theta_\nu(\xi,\xi))=\int\|\xi_x\|^2\,d\Lambda_\nu(x)\).

**Proposition 10.2.** (a) \(\operatorname{Tr}_\Lambda\) is a faithful normal semifinite trace on
\(\operatorname{End}_\Lambda(H)\), and \(\operatorname{Tr}_\Lambda(p)=\dim_\Lambda(pH)\) for every projection \(p\).

(b) If \(\operatorname{Hom}_\Lambda(H_1,H_2)\) contains an invertible element, then \(\dim_\Lambda H_1=\dim_\Lambda H_2\).

(c) \(\dim_\Lambda\big(\bigoplus_iH_i\big)=\sum_i\dim_\Lambda H_i\) for countable direct sums.

(d) If \(\Lambda=\sum_i\Lambda_i\) is a countable sum of transverse measures (of modulus \(1\)), then
\(\dim_\Lambda(H)=\sum_i\dim_{\Lambda_i}(H)\).

(e) If \(h:G\to G'\) is a proper homomorphism, \(\delta'=1\) and \(h(\Lambda)=\Lambda'\), then
\(\dim_\Lambda(h^*H)=\dim_{\Lambda'}(H)\) for every \(\Lambda'\)-random Hilbert space \(H\).

*Proof.* (a) \(\varphi_1\) is normal, semifinite and faithful (Theorem 5.3), with \(\sigma_t^{\varphi_1}=
\operatorname{Ad}1^{it}=\mathrm{id}\) (Corollary 5.4), so it is a trace (B2). Write \(H=pH\oplus(1-p)H\); by Proposition
5.5(b) with \(T=1\oplus1\), \(\varphi_1(p)=\varphi^{pH}_1(1)+\varphi^{(1-p)H}_1(0)=\dim_\Lambda(pH)\).

(b) Let \(A\) be invertible, \(A_x=u_x|A_x|\) the polar decompositions. The \(u_x\) are unitary, measurable (\(u_x=A_x
|A_x|^{-1}\)), and intertwine, by uniqueness of the polar decomposition of \(U_2(\gamma)A_xU_1(\gamma)^*=A_y\). By
Proposition 5.5(a) with \(V=u\), \(\varphi^{H_2}_{u1u^*}(1)=\varphi^{H_1}_1(u^*u)\), and \(u1u^*=1\).

(c) Proposition 5.5(b) with \(T=\bigoplus1\) and \(X=1\).

(d) \(H\) is \(\Lambda_i\)-random, and \(\pi_i:\operatorname{End}_\Lambda(H)\to\operatorname{End}_{\Lambda_i}(H)\),
which keeps the family and forgets more null sets, is a normal \(*\)-homomorphism. The normal weight
\(\sum_i\varphi_1^{\Lambda_i}\circ\pi_i\) takes the value \(\sum_i\int\|\xi\|^2d\Lambda_{i,\nu}=\int\|\xi\|^2d\Lambda_\nu\)
on \(\theta_\nu(\xi,\xi)\), so it equals \(\varphi^\Lambda_1\) by Corollary 4.3. Evaluate at \(1\).

(e) Proposition 9.5 with \(T'=1\). \(\square\)

**Example 10.3.** In Example 5.6 (one orbit with mass \(c\)), \(\dim_\Lambda(H)=c\dim K\). For the trivial groupoid
\(G=G^{(0)}=Y\) (only units), a transverse measure is a measure \(\mu\) on \(Y\), a random Hilbert space is a measurable
field, and \(\dim_\Lambda(H)=\int\dim H_y\,d\mu(y)\). The formal dimension interpolates between these: it is an
integral of dimensions over the orbit space, normalized by \(\Lambda\), and it takes all values in \([0,\infty]\).

**Theorem 10.4 (unimodular groups).** Let \(\Gamma\) be a unimodular locally compact second countable group, viewed as a
groupoid with one unit, with \(\delta=1\). Fix a Haar measure \(dg\); the transverse functions are the multiples of
\(dg\) (B9)(a), and \(\Lambda(c\,dg)=c\) defines a transverse measure. The \(\Lambda\)-random Hilbert spaces are the
representations \(\pi\) of \(\Gamma\) contained in a multiple of the regular representation, and
\(\operatorname{End}_\Lambda(\pi)=\pi(\Gamma)'\).

(a) If \(\pi\) is irreducible and square integrable with formal degree \(d_\pi\) (relative to \(dg\)), then
\(\dim_\Lambda(\pi)=d_\pi\).

(b) On \(L^2(\Gamma)\), \(\operatorname{Tr}_\Lambda\) is the Plancherel trace \(\tau'\) of \(R(\Gamma)\); on
\(L^2(\Gamma)\otimes\ell^2\), it is \(\tau'\otimes\operatorname{Tr}\). Hence, if \(\pi\) is realized as
\(p(L^2(\Gamma)\otimes\ell^2)\) with \(p\in R(\Gamma)\otimes\mathcal L(\ell^2)\), then \(\dim_\Lambda(\pi)=
(\tau'\otimes\operatorname{Tr})(p)\), the Murray–von Neumann dimension of \(\pi\) as a module over the group von Neumann
algebra with its Plancherel trace.

*Proof.* (a) Let \(\xi\in K_\pi\) be a unit vector. By (B9)(c), \(\int|\langle\alpha,\pi(g)\xi\rangle|^2dg=
d_\pi^{-1}\|\alpha\|^2\), so \(\xi\in D(\pi,dg)\) and \(\langle\theta_{dg}(\xi,\xi)\alpha,\alpha\rangle=
d_\pi^{-1}\|\alpha\|^2\), that is \(\theta_{dg}(\xi,\xi)=d_\pi^{-1}1\). Hence \(\dim_\Lambda(\pi)=d_\pi\varphi_1
(\theta_{dg}(\xi,\xi))=d_\pi\|\xi\|^2\Lambda(dg)=d_\pi\).

(b) For \(\xi\in L^2(\Gamma)\) put \(\xi^*(u)=\overline{\xi(u^{-1})}\). Then \((T_{dg}(\xi)\alpha)(g)=\langle\alpha,
\lambda(g)\xi\rangle=\int\alpha(u)\overline{\xi(g^{-1}u)}du=(\alpha*\xi^*)(g)\), so \(\xi\in D(\lambda,dg)\) iff right
convolution \(\rho(\xi^*)\) is bounded, and then \(\theta_{dg}(\xi,\xi)=\rho(\xi^*)^*\rho(\xi^*)\) and
\(\tau'(\theta_{dg}(\xi,\xi))=\|\xi^*\|^2=\|\xi\|^2\) (unimodularity). Also \(\operatorname{Tr}_\Lambda(\theta_{dg}(\xi,\xi))
=\|\xi\|^2\Lambda(dg)=\|\xi\|^2\). Both are normal weights on \(\operatorname{End}_\Lambda(\lambda)=R(\Gamma)\), so they
agree (Corollary 4.3). Proposition 5.5(b) gives \(\operatorname{Tr}_\Lambda=\tau'\otimes\operatorname{Tr}\) on the
multiple, and Proposition 10.2(a) gives \(\dim_\Lambda(pH)=(\tau'\otimes\operatorname{Tr})(p)\). \(\square\)

For a discrete group with counting measure, \(\dim_\Lambda(\ell^2\Gamma)=\tau'(1)=1\), and for a finite group
\(\dim_\Lambda(\pi)=\dim\pi/|\Gamma|\) (Exercise 12.3).

**Proposition 10.5 (transversals).** Let \(Z\subset G^{(0)}\) be a transversal, that is, a Borel set whose
characteristic transverse function \(\nu_Z\), \(\nu_Z(f)(y)=\sum_{\gamma\in G^y,\,s(\gamma)\in Z}f(\gamma)\), is proper.
Let \(H_x=\ell^2(G^x\cap s^{-1}(Z))\) with left translations. Then \(\dim_\Lambda(H)=\Lambda(\nu_Z)\).

*Proof.* \(H=L^2\circ F\) for the random variable \(F(x)=G^x\cap s^{-1}(Z)\) with counting measure (of modulus \(1\)), a
sub-functor of \(L\), hence proper (R4). For \(T=1\), \(\omega_1(M(g))=\operatorname{Trace}M(g)=\sum_{z\in F(x)}g(z)\),
so \(F_1=F\), a \(\sigma\)-finite random variable, and \(\dim_\Lambda(H)=\int F\,d\Lambda\) by Corollary 9.3. Now \(F\) is
the functor \(x\mapsto(G^x,\nu_Z^x)\). Take \(\nu\) faithful, \(g>0\) with \(\nu(g)=1\), and \(f=\tilde g\) on \(G\), so
that \(\nu*f=1\) as in the proof of Corollary 9.4. Then, by the modular relation (1.1) with \(\delta=1\),
\[
\int F\,d\Lambda=\int\nu_Z^x(\tilde g)\,d\Lambda_\nu(x)=\int\nu(g)\,d\Lambda_{\nu_Z}=\Lambda_{\nu_Z}(1)=\Lambda(\nu_Z).
\qquad\square
\]

For a countable measured equivalence relation \(R\) on \((Y,\mu)\) with invariant \(\mu\), the unit space itself is a
transversal, \(\Lambda(\nu_Y)=\mu(Y)\), and \(\dim_\Lambda\) of \(\ell^2\) of the classes is the total mass \(\mu(Y)\):
the formal dimension of \(\ell^2(\text{orbit})\) is the "number of points" of the orbit space, measured by \(\Lambda\).

## 11. \(\Lambda\)-compact operators and the \(\Lambda\)-index

In this section \(\delta=1\). The Fredholm theory relative to a trace goes back to Breuer; we give complete
proofs, and Remark 11.8 notes that they give it for every semifinite von Neumann algebra. It is the framework in which the index theorem for measured foliations is stated
[Connes 1982].

Fix \(\Lambda\)-random Hilbert spaces \(H_1,H_2,H_3\) and let \(M=\operatorname{End}_\Lambda(H_1\oplus H_2\oplus H_3)\)
with the fns trace \(\tau=\operatorname{Tr}_\Lambda\) (Proposition 10.2). Let \(p_j\) be the projection onto \(H_j\), so
that \(\operatorname{Hom}_\Lambda(H_j,H_k)=p_kMp_j\). By Proposition 5.5(b), the restriction of \(\tau\) to
\(p_jMp_j=\operatorname{End}_\Lambda(H_j)\) is \(\operatorname{Tr}_\Lambda\) of \(H_j\), and by Proposition 10.2(a)
\(\tau(q)=\dim_\Lambda(qH)\) for projections \(q\). For \(x\in M\), \(l(x)\) and \(r(x)\) are its left and right
supports. For \(x\in p_kMp_j\) the *kernel projection* is \(N(x)=p_j-r(x)\), the projection onto \(\ker x\cap H_j\);
thus \(\dim_\Lambda\operatorname{Ker}x=\tau(N(x))\), and \(N(x^*)=p_k-l(x)\). For \(a>0\), \(e_a(|x|)\) is the
spectral projection of \(|x|\) for \([a,\infty)\).

**Lemma 11.1.** (a) \(\mathcal F=\{x\in M:\tau(l(x))<\infty\}\) is a two-sided \(*\)-ideal, and \(\tau(l(x))=
\tau(r(x))\).

(b) Let \(\mathcal K\) be the norm closure of \(\mathcal F\). If \(x\in\mathcal K\) and \(e\) is a projection with
\(\|x\xi\|\ge c\|\xi\|\) for \(\xi\in eH\) (some \(c>0\)), then \(\tau(e)<\infty\).

(c) \(\mathcal K=\{x\in M:\tau(e_a(|x|))<\infty\text{ for all }a>0\}\), and \(\mathcal K\) is also the norm closure of
the ideal of definition \(\mathfrak m_\tau\) of \(\tau\).

*Proof.* (a) \(l(x)\sim r(x)\) (B8) and \(\tau\) is a trace. Since \(l(x^*)=r(x)\), \(\mathcal F\) is self-adjoint. For
\(a\in M\), \(l(xa)\le l(x)\) and \(\tau(l(ax))=\tau(r(ax))\le\tau(r(x))\). Finally \(l(x+y)\le l(x)\vee l(y)\) and
\(\tau(p\vee q)\le\tau(p)+\tau(q)\), since \(p\vee q-q\sim p-p\wedge q\le p\) (B8).

(b) Choose \(y\in\mathcal F\) with \(\|x-y\|<c\). For \(0\neq\xi\in eH\), \(\|y\xi\|\ge(c-\|x-y\|)\|\xi\|>0\), so \(ye\)
is injective on \(eH\) and \(r(ye)=e\). Then \(\tau(e)=\tau(l(ye))\le\tau(l(y))<\infty\).

(c) If \(x\in\mathcal K\), then \(\||x|\xi\|\ge a\|\xi\|\) on the range of \(e_a(|x|)\), and \(\|x\xi\|=\||x|\xi\|\); apply
(b). Conversely, if all \(\tau(e_a(|x|))\) are finite, then \(x_a=xe_a(|x|)\) has \(r(x_a)\le e_a(|x|)\), so \(x_a\in
\mathcal F\), and \(\|x-x_a\|=\|x(1-e_a(|x|))\|\le a\). For the last statement: \(\mathfrak m_\tau\) is a two-sided ideal
containing the projections of finite trace, and \(y=l(y)y\) for \(y\in\mathcal F\), so \(\mathcal F\subset
\mathfrak m_\tau\); conversely, for \(x\ge0\) with \(\tau(x)<\infty\), \(a\,e_a(x)\le x\) gives \(\tau(e_a(x))\le\tau(x)/a\),
so \(\mathfrak m_\tau\subset\mathcal K\). \(\square\)

**Definition 11.2.** An operator \(x\in\operatorname{Hom}_\Lambda(H_j,H_k)\) is *\(\Lambda\)-compact* if \(x\in
\mathcal K\), that is, \(\dim_\Lambda e_a(|x|)H_j<\infty\) for every \(a>0\). It is a *\(\Lambda\)-Fredholm operator* if
there is \(y\in\operatorname{Hom}_\Lambda(H_k,H_j)\) (a parametrix) with \(yx-p_j\in\mathcal K\) and \(xy-p_k\in
\mathcal K\). Its *\(\Lambda\)-index* is
\[
\operatorname{Ind}_\Lambda(x)=\dim_\Lambda\operatorname{Ker}x-\dim_\Lambda\operatorname{Ker}x^*=\tau(N(x))-\tau(N(x^*)).
\]

**Lemma 11.3.** Let \(x\in p_kMp_j\) be \(\Lambda\)-Fredholm with parametrix \(y\).

(a) \(\tau(N(x))\) and \(\tau(N(x^*))\) are finite, so \(\operatorname{Ind}_\Lambda(x)\in\mathbb R\) is well defined.

(b) There are a projection \(e\le p_j\) with \(\tau(p_j-e)<\infty\) and \(c>0\) such that \(\|x\xi\|\ge c\|\xi\|\) for
\(\xi\in eH\).

*Proof.* Let \(k=p_j-yx\in\mathcal K\). (a) On \(N(x)H\), \(k\xi=\xi\); apply Lemma 11.1(b) with \(c=1\). The same
argument for \(x^*\), whose parametrix is \(y^*\), gives \(\tau(N(x^*))<\infty\). (b) Choose \(z\in\mathcal F\) with
\(\|k-z\|\le1/2\) and let \(e=p_j\wedge(1-r(z))\), the projection onto \(p_jH\cap\ker z\). For \(\xi\in eH\),
\(\xi=yx\xi+(k-z)\xi\), so \(\|\xi\|\le\|y\|\|x\xi\|+\|\xi\|/2\) and \(\|x\xi\|\ge\|\xi\|/(2\|y\|+1)\). By (B8),
\(p_j-e\sim p_j\vee(1-r(z))-(1-r(z))\le r(z)\), which has finite trace. \(\square\)

**Proposition 11.4 (index formula).** Let \(x\in p_kMp_j\) be \(\Lambda\)-Fredholm, \(e\le p_j\) a projection with
\(\tau(p_j-e)<\infty\) such that \(x\) is bounded below on \(eH\), and \(f=l(xe)\), the projection onto the closed
subspace \(x(eH)\). Then \(\tau(p_k-f)<\infty\) and
\[
\operatorname{Ind}_\Lambda(x)=\tau(p_j-e)-\tau(p_k-f).
\]

*Proof.* Let \(e'=p_j-e\), \(q'=p_k-f\), \(a=fxe\) and \(d=q'xe'\). Then \(q'xe=0\), and \(a\) maps \(eH\) bijectively onto
\(fH\), with inverse \(a^{-1}\in eMf\) (B8). *Finiteness:* \(f\le l(x)\le f\vee l(xe')\), so \(q'=(p_k-l(x))+(l(x)-f)\) with
\(\tau(p_k-l(x))=\tau(N(x^*))<\infty\) and \(l(x)-f\le f\vee l(xe')-f\sim l(xe')-f\wedge l(xe')\le l(xe')\sim r(xe')\le e'\).

*Reduction to a diagonal operator.* Let \(n=a^{-1}fxe'\), which maps \(e'H\) into \(eH\) and vanishes on \(eH\); hence
\(n^2=0\) and \(g=p_j+n\) is invertible in \(p_jMp_j\) with inverse \(p_j-n\). With \(x_0=a+d\) we get
\(x_0g=a+d+an+dn=fxe+q'xe'+fxe'=x\), because \(an=fxe'\) and \(dn=0\). Since \(\ker x=g^{-1}(\ker x_0)\), \(N(x)\sim
N(x_0)\) (B8); since \(g^*\) is invertible, \(\ker x^*=\ker(g^*x_0^*)=\ker x_0^*\). Relative to \(p_j=e+e'\) and
\(p_k=f+q'\), \(x_0=a\oplus d\) with \(a\) invertible, so \(N(x_0)=e'-r(d)\) and \(N(x_0^*)=q'-l(d)\). Therefore
\[
\operatorname{Ind}_\Lambda(x)=\tau(e')-\tau(r(d))-\tau(q')+\tau(l(d))=\tau(e')-\tau(q'),
\]
using \(r(d)\sim l(d)\), both of finite trace. \(\square\)

**Lemma 11.5.** Let \(e\le p_j\) be a projection, \(x,w\in p_kMp_j\), and suppose \(\|x\xi\|\ge c\|\xi\|\) on \(eH\) and
\(\|w\|<c/2\). Then \(\|(x+w)\xi\|\ge(c/2)\|\xi\|\) on \(eH\), and the projections \(f=l(xe)\), \(f_w=l((x+w)e)\) satisfy
\(p_k-f\sim p_k-f_w\).

*Proof.* The lower bound is clear. For \(\xi\in eH\), the unit vector \(\eta=(x+w)\xi/\|(x+w)\xi\|\) is at distance at most
\(\|w\xi\|/\|(x+w)\xi\|\le\|w\|/(c-\|w\|)<1\) from \(fH\), and \(x\xi/\|x\xi\|\) is at distance at most \(\|w\|/c<1\) from
\(f_wH\). By (B8), \(\|f-f_w\|<1\), and \(p_k-f\), \(p_k-f_w\) are projections of \(p_kMp_k\) at distance \(<1\), hence
equivalent. \(\square\)

**Theorem 11.6.** (a) If \(x_1\in\operatorname{Hom}_\Lambda(H_1,H_2)\) and \(x_2\in\operatorname{Hom}_\Lambda(H_2,H_3)\)
are \(\Lambda\)-Fredholm, then so is \(x_2x_1\), and \(\operatorname{Ind}_\Lambda(x_2x_1)=\operatorname{Ind}_\Lambda(x_1)
+\operatorname{Ind}_\Lambda(x_2)\).

(b) The \(\Lambda\)-Fredholm operators form a norm-open subset of \(\operatorname{Hom}_\Lambda(H_1,H_2)\), on which
\(\operatorname{Ind}_\Lambda\) is locally constant (continuous for the discrete topology of \(\mathbb R\)).

(c) If \(x\) is \(\Lambda\)-Fredholm and \(k\) is \(\Lambda\)-compact, then \(x+k\) is \(\Lambda\)-Fredholm and
\(\operatorname{Ind}_\Lambda(x+k)=\operatorname{Ind}_\Lambda(x)\).

*Proof.* (b) Let \(x\) have parametrix \(y\), \(k_1=p_1-yx\), \(k_2=p_2-xy\), and let \(e,c\) be as in Lemma 11.3(b).
Let \(\|w\|<\min(c/2,1/\|y\|)\). Then \(g=p_1+yw\) and \(h=p_2+wy\) are invertible in \(p_1Mp_1\), \(p_2Mp_2\), and
\(g^{-1}y(x+w)=p_1-g^{-1}k_1\), \((x+w)yh^{-1}=p_2-k_2h^{-1}\). So \(x+w\) has a left parametrix \(y_L\) and a right
parametrix \(y_R\) modulo \(\mathcal K\); then \(y_L\equiv y_L(x+w)y_R\equiv y_R\) modulo \(\mathcal K\), and \(y_L\) is a
parametrix. By Lemma 11.5, \(x+w\) is bounded below on \(eH\) and \(\tau(p_2-l((x+w)e))=\tau(p_2-l(xe))\); by Proposition
11.4 applied to \(x\) and to \(x+w\) with the same \(e\), the indices agree.

(c) \(y\) is also a parametrix of \(x+k\). Choose \(z\in\mathcal F\) with \(\|k-z\|<c/2\); replacing \(z\) by
\(p_2zp_1\in\mathcal F\) we may assume \(z\in p_2Mp_1\). Let \(e_2=e\wedge(p_1-r(z))\). By (B8), \(e-e_2\sim e\vee(p_1-r(z))-
(p_1-r(z))\le r(z)\), so \(\tau(p_1-e_2)<\infty\). On \(e_2H\), \(z\) vanishes, so \((x+k)\xi=(x+w)\xi\) with \(w=(k-z)e_2\),
\(\|w\|<c/2\), and \(x\) is bounded below by \(c\) there. Lemma 11.5 and Proposition 11.4 (for \(x\) and for \(x+k\), with
\(e_2\)) give equal indices.

(a) Parametrices \(y_1,y_2\) give \(y_1y_2x_2x_1=y_1(p_2-k)x_1\in p_1+\mathcal K\) and similarly on the other side, so
\(x_2x_1\) is \(\Lambda\)-Fredholm. Choose \(e_1\le p_1\) for \(x_1\) and \(e_2\le p_2\) for \(x_2\) as in Lemma 11.3(b),
and let \(f_1=l(x_1e_1)\), \(a_1=f_1x_1e_1\). Put \(g=f_1\wedge e_2\); then \(f_1-g\sim f_1\vee e_2-e_2\le p_2-e_2\), so
\(\tau(f_1-g)<\infty\). Let \(e\le e_1\) be the projection onto \(a_1^{-1}(gH)\). Since \(e_1H\ominus a_1^{-1}(gH)=
a_1^*(f_1H\ominus gH)\) and \(a_1^*\) is injective and bounded below on \(f_1H\), (B8) gives \(e_1-e\sim f_1-g\). So
\(\tau(p_1-e)=\tau(p_1-e_1)+\tau(f_1-g)<\infty\). The operator \(x_1\) maps \(eH\) bijectively onto \(gH\), bounded below,
and \(x_2\) is bounded below on \(gH\subset e_2H\); so \(x_2x_1\) is bounded below on \(eH\), with \(l(x_2x_1e)=l(x_2g)=:h\).
Proposition 11.4 gives
\[
\operatorname{Ind}(x_2x_1)=\tau(p_1-e_1)+\tau(f_1-g)-\tau(p_3-h),\quad\operatorname{Ind}(x_1)=\tau(p_1-e_1)-\tau(p_2-f_1),
\quad\operatorname{Ind}(x_2)=\tau(p_2-g)-\tau(p_3-h),
\]
the last one using \(g\le e_2\) (so \(x_2\) is bounded below on \(gH\)) and \(\tau(p_2-g)=\tau(p_2-f_1)+\tau(f_1-g)<
\infty\). Adding the last two gives the first. \(\square\)

Clearly \(\operatorname{Ind}_\Lambda(x^*)=-\operatorname{Ind}_\Lambda(x)\).

**Remark 11.8 (Breuer's theory in general).** The proofs of Lemma 11.1 to Theorem 11.6 use only that \(M\) is a
von Neumann algebra with a faithful normal semifinite trace \(\tau\), that \(p_1,p_2,p_3\) are projections of \(M\)
with sum \(1\), and the facts (B8), which hold in every von Neumann algebra. So they prove the same statements in
that generality. For a von Neumann algebra \(N\) with a faithful normal semifinite trace \(\tau_N\), apply them to
the algebra \(M_3(N)\) of \(3\times3\) matrices over \(N\), with the trace \(\tau_N\otimes\operatorname{Tr}\) and the
diagonal matrix units \(p_j\): each corner \(p_kM_3(N)p_j\) is a copy of \(N\), and one obtains Breuer's Fredholm theory
for operators in \(N\) relative to \(\tau_N\).

**Example 11.7 (non-integral index).** Let \(G=Y=[0,1]\) (only units) with Lebesgue measure as \(\Lambda\), \(H_y=
\ell^2(\mathbb N)\) for all \(y\), and \(S\) the unilateral shift. Fix \(t\in[0,1]\) and let \(x_y=S^*\) for \(y\le t\),
\(x_y=1\) for \(y>t\). A parametrix is \(y_y=S\) for \(y\le t\), \(1\) otherwise: \(yx-1\) and \(xy-1\) are the families
\(-1_{[0,t]}(y)e_0e_0^*\) and \(0\), of finite trace. \(\operatorname{Ker}x_y=\mathbb Ce_0\) for \(y\le t\), and
\(\operatorname{Ker}x_y^*=0\). So \(\operatorname{Ind}_\Lambda(x)=t\). In Example 5.6 (one orbit of mass \(c\)),
\(\mathcal K\) is the ideal of compact operators on \(K\) and \(\operatorname{Ind}_\Lambda=c\cdot\operatorname{ind}\), the
ordinary Fredholm index scaled by the mass of the orbit.

## 12. Exercises

**Exercise 12.1.** Let \(G=Y\) be a standard Borel space with only units, \(\Lambda=\mu\) a \(\sigma\)-finite measure,
and \(H=(H_y)\) a measurable field. Show that \(\operatorname{End}_\Lambda(H)\) is the algebra of decomposable
operators on \(\int^\oplus H_y\,d\mu\), that \(\varphi_T(A)=\int\omega_{T_y}(A_y)\,d\mu(y)\), and that
\(\dim_\Lambda(H)=\int\dim H_y\,d\mu(y)\). Compute \(E_\nu\) for \(\nu^y=g(y)\varepsilon_y\), \(g>0\).

*Solution.* Here \(G^y=\{y\}\), every representation is square integrable, intertwiners are arbitrary bounded Borel
families, and negligible sets are \(\mu\)-null sets; so \(\operatorname{End}_\Lambda(H)\) is the decomposable algebra.
A transverse function is \(\nu^y=g(y)\varepsilon_y\) with \(g\ge0\) Borel, \(\Lambda_\nu=g\mu\), and
\(\theta_\nu(\xi,\xi)_y=g(y)\xi_y\xi_y^*\). The weight \(A\mapsto\int\omega_{T_y}(A_y)d\mu\) is normal and takes the value
\(\int g\langle T\xi,\xi\rangle d\mu=\int\langle T\xi,\xi\rangle d\Lambda_\nu\) on \(\theta_\nu(\xi,\xi)\), so it is
\(\varphi_T\) by Corollary 4.3. With \(T=1\) and \(A=1\): \(\dim_\Lambda H=\int\operatorname{Tr}(1_{H_y})d\mu\). Here
\(P_\nu=\operatorname{End}_\Lambda(H)\) and the average (6.2) of \(B\) is \(gB\); so \(E_\nu(B)=gB\), and \(\varphi_T(gB)=
\int\omega_{T_y}(B_y)\,g\,d\mu=\rho^\nu_T(B)\), as Theorem 6.3 requires.

**Exercise 12.2.** In Example 5.6 (pair groupoid on \((X,\beta)\), \(\beta\) a probability measure, \(\Lambda(\nu_\beta)=c\)),
identify every \(H_x\) with \(K\). Show that \(E_{\nu_\beta}\) is the conditional expectation \((B_x)\mapsto
\int_XB_x\,d\beta(x)\) of \(P_{\nu_\beta}=L^\infty(X,\beta)\bar\otimes\mathcal L(K)\) onto \(\mathcal L(K)\), and that
\(\rho^{\nu_\beta}_T=c\operatorname{Tr}(T_0^{1/2}E_{\nu_\beta}(\cdot)T_0^{1/2})\).

*Solution.* Under the identification, \(U(y,x)\) becomes the identity of \(K\), so the average (6.2) is
\(C=\int B_x\,d\beta(x)\), constant in \(y\), bounded by \(\|B\|\) because \(\beta(X)=1\). By Theorem 6.3(b),
\(E_{\nu_\beta}(B)=\int B_xd\beta\), and \(E(1)=1\). Then \(\rho_T(B)=\int\omega_{T_0}(B_x)\,c\,d\beta(x)=
c\,\omega_{T_0}(\int B_xd\beta)\). Indeed, with \(S=T_0\) and \(S_\varepsilon\) as in Section 6, and an orthonormal
basis \((e_i)\) of \(K\), \(\operatorname{Tr}(S_\varepsilon^{1/2}B_xS_\varepsilon^{1/2})=\sum_i\langle
B_xS_\varepsilon^{1/2}e_i,S_\varepsilon^{1/2}e_i\rangle\); Tonelli's theorem for these nonnegative terms and the
definition of the weak integral give \(\int\operatorname{Tr}(S_\varepsilon^{1/2}B_xS_\varepsilon^{1/2})\,d\beta(x)=
\operatorname{Tr}(S_\varepsilon^{1/2}(\int B_xd\beta)S_\varepsilon^{1/2})\). Both sides increase as
\(\varepsilon\downarrow0\), and monotone convergence along \(\varepsilon=1/n\) gives the claim. This is
\(\varphi_T(E(B))\) by Example 5.6.

**Exercise 12.3.** Let \(\Gamma\) be a finite group with counting measure as Haar measure and \(\Lambda\) as in Theorem
10.4. Show that \(\dim_\Lambda(\pi)=\dim\pi/|\Gamma|\) for every irreducible \(\pi\), and check Proposition 10.2(c) on the
regular representation.

*Solution.* Every representation is square integrable. Schur orthogonality for finite groups gives
\(\sum_g|\langle\pi(g)\xi,\eta\rangle|^2=\frac{|\Gamma|}{\dim\pi}\|\xi\|^2\|\eta\|^2\), so \(d_\pi=\dim\pi/|\Gamma|\) and
Theorem 10.4(a) gives \(\dim_\Lambda(\pi)=\dim\pi/|\Gamma|\). The regular representation is \(\bigoplus_\pi(\dim\pi)\,\pi\),
so Proposition 10.2(c) gives \(\dim_\Lambda(\ell^2\Gamma)=\sum_\pi(\dim\pi)^2/|\Gamma|=1\), in agreement with
\(\tau'(1)=\|\delta_e\|^2=1\) from Theorem 10.4(b).

**Exercise 12.4.** In Example 5.6 with \(\delta=1\), let \(T_0\) be a nonsingular positive operator on \(K\). Use Theorem
7.2 to show that \(\operatorname{Sp}(\sigma^{\varphi_T})\) is the closure of \(\operatorname{Sp}\log T_0-
\operatorname{Sp}\log T_0\), and deduce the familiar fact that \(\operatorname{Tr}(T_0\,\cdot\,)\) is a trace iff
\(T_0\) is scalar.

*Solution.* The isotropy groups of the pair groupoid are trivial, so Theorem 7.2 applies. \(T_x\) is unitarily equivalent to \(T_0\), so
\(X_\varepsilon(p)\) is either empty or all of \(X\), and it is not negligible iff \((\operatorname{Sp}\log T_0-
\operatorname{Sp}\log T_0)\cap(p-\varepsilon,p+\varepsilon)\neq\emptyset\). So \(p\in\operatorname{Sp}(\sigma^\varphi)\)
iff \(p\) is in the closure of the difference set. By Corollary 7.3, \(\varphi_T=c\operatorname{Tr}(T_0^{1/2}\cdot
T_0^{1/2})\) is a trace iff \(T_0\) is scalar.

**Exercise 12.5.** Let \(\delta=1\) and \(x\in\operatorname{End}_\Lambda(H)\) be \(\Lambda\)-Fredholm. Show that
\(\operatorname{Ind}_\Lambda(x)=0\) when \(\operatorname{Tr}_\Lambda(1)<\infty\), whereas Example 11.7 gives every value in
\([0,1]\) for \(\operatorname{Tr}_\Lambda(1)=\infty\).

*Solution.* Take \(H_1=H_2=H\), so \(p_1=p_2=1\), and let \(e\), \(f=l(xe)\) be as in Proposition 11.4 (they exist by
Lemma 11.3(b)). If \(\tau(1)<\infty\), then \(\operatorname{Ind}_\Lambda(x)=\tau(1-e)-\tau(1-f)=\tau(f)-\tau(e)\), and
\(e\sim f\) by (B8), because \(x\) is injective on \(eH\) with closed range \(fH\). So the index vanishes. In Example
11.7, \(H_y=\ell^2(\mathbb N)\) is infinite-dimensional, so \(\operatorname{Tr}_\Lambda(1)=\infty\), and the index is
\(t\).

**Exercise 12.6 (12 points).** For the finite mixed transfer in Proposition 2.1, prove directly that \(C=A^{1/2}kB^{1/2}\) implies \(C\in\mathfrak n_\varphi^*\mathfrak n_\psi\). Then explain why the separate right cuts \(y_n=ye_n\), \(z_n=zf_n\) converge in the required mixed scalar identity even when neither \(e_n\) nor \(f_n\) commutes with \(a^*\) or \(b\).

**Solution.** Set \(a_0=k^*A^{1/2}\), \(b_0=B^{1/2}\). Contractivity gives \(a_0^*a_0\le A\), so \(\varphi(a_0^*a_0)<\infty\); likewise \(\psi(b_0^*b_0)<\infty\). Thus \(C=a_0^*b_0\) has the stated orientation (4 points). Normal evaluation gives \(\Lambda_\Phi(y_n)\to\Lambda_\Phi(y)\), \(\Lambda_\Psi(z_n)\to\Lambda_\Psi(z)\). The two transferred half-strip bounds give convergence of \(\Lambda_\Psi(y_na^*)\) and \(\Lambda_\Phi(z_nb)\), without commuting a cutoff through either multiplier (4 points). Apply Cauchy–Schwarz to the identity \(\langle\Lambda_\Psi(z_n),\Lambda_\Psi(y_na^*)\rangle=\langle\Lambda_\Phi(z_nb),\Lambda_\Phi(y_n)\rangle\), using the first-slot-linear convention. Both sides converge to their full mixed scalar values. No common finite ideal or common spectral cutoff is required (4 points). Total: 12 points.

## References



- [Arveson 1974] W. Arveson, On groups of automorphisms of operator algebras, J. Functional Analysis 15 (1974),
  217–243. https://doi.org/10.1016/0022-1236(74)90034-2. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123674900342
- [Connes 1979] A. Connes, Sur la théorie non commutative de l'intégration, in: Algèbres d'opérateurs (Sém.,
  Les Plans-sur-Bex, 1978), Lecture Notes in Math. 725, Springer, Berlin, 1979, 19–143. Free at https://alainconnes.org/wp-content/uploads/ThNonComm.pdf
- [Connes 1980a] A. Connes, On the spatial theory of von Neumann algebras, J. Functional Analysis 35 (1980), no. 2,
  153–164. Free at https://doi.org/10.1016/0022-1236(80)90002-6
- [Connes 1982] A. Connes, A survey of foliations and operator algebras, in: Operator algebras and applications,
  Part I (Kingston, Ont., 1980), Proc. Sympos. Pure Math. 38, Amer. Math. Soc., Providence, RI, 1982, 521–628. Free at https://alainconnes.org/wp-content/uploads/foliationsfine.pdf
- [Connes 1994] A. Connes, Noncommutative geometry, Academic Press, San Diego, CA, 1994.
  https://alainconnes.org/publications/
- [Connes–Takesaki 1977] A. Connes and M. Takesaki, The flow of weights on factors of type III, Tôhoku Math. J. (2) 29
  (1977), no. 4, 473–575. https://doi.org/10.2748/tmj/1178240493
- [Haagerup 1979] U. Haagerup, Operator valued weights in von Neumann algebras. I, J. Functional Analysis 32 (1979),
  no. 2, 175–206; II, J. Functional Analysis 33 (1979), no. 3, 339–361. https://doi.org/10.1016/0022-1236(79)90053-3,
  https://doi.org/10.1016/0022-1236(79)90072-7. Free at https://doi.org/10.1016/0022-1236(79)90053-3
- [Ramsay 1971] A. Ramsay, Virtual groups and group actions, Advances in Math. 6 (1971), 253–322.
  https://doi.org/10.1016/0001-8708(71)90018-1. Free at https://doi.org/10.1016/0001-8708(71)90018-1
- [Duflo–Moore 1976] M. Duflo and C. C. Moore, On the regular representation of a nonunimodular locally compact group,
  J. Functional Analysis 21 (1976), 209–243. https://doi.org/10.1016/0022-1236(76)90079-3. Free at
  https://linkinghub.elsevier.com/retrieve/pii/0022123676900793
- [Erdős–Mauldin 1976] P. Erdős and R. D. Mauldin, The nonexistence of certain invariant measures, Proc. Amer. Math.
  Soc. 59 (1976), 321–322. Free at https://www.renyi.hu/~p_erdos/1976-47.pdf
- [Fremlin] D. H. Fremlin, *Measure theory*, Volume 4, *Topological measure spaces*, Chapter 44, *Topological groups*,
  author's version. Free at https://www1.essex.ac.uk/maths/people/fremlin/chap44.pdf

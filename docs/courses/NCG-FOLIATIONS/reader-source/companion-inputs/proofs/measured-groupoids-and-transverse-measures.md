# Measured groupoids and transverse measures

*Public domain (CC0).*

## Introduction

Many spaces that geometry produces are quotients \(\Omega=X/\!\sim\) of a good measurable space \(X\) by an equivalence
relation whose classes are small and dense: the orbits of an ergodic transformation, the leaves of a foliation, the
geodesics of a compact manifold with ergodic geodesic flow. Such a quotient has almost no measurable functions. If
\(T\) is an ergodic transformation of a probability space \((X,\mu)\), every measurable function on \(X\) that is
constant on the orbits of \(T\) is almost everywhere constant. Classical integration, which integrates functions on
\(\Omega\), sees nothing of \(\Omega\).

The remedy is to change the notion of *function*, not the notion of measure. A function \(f: \Omega\to\{0,1,2,\dots,
\infty\}\) can be thought of as a countable set over \(\Omega\): a set \(Y\) with a map \(p:Y\to\Omega\) whose fibre over
\(\omega\) has \(f(\omega)\) elements. Two sets over \(\Omega\) define the same ordinary function exactly when there is a
fibrewise bijection between them. If one insists that the bijection be *measurable*, sets over \(\Omega\) with the same
finite fibre cardinalities are still identified, but sets with infinite fibres are no longer all alike: an infinite
fibre can be "large" or "small" in a way that measurable maps detect. A generalized measure on \(\Omega\) integrates
these generalized functions, is countably additive, and gives the same value to measurably equivalent ones. On a
singular \(\Omega\) it can give a finite nonzero integral to generalized functions that are infinite everywhere.

To make this precise, one replaces \(\Omega\) by a *measurable groupoid* \(G\) whose isomorphism classes of objects
are the points of \(\Omega\): for \(\Omega=X/\!\sim\) take the graph of the relation, with composition
\((x_1,x_2)(x_2,x_3)=(x_1,x_3)\). The generalized functions become *transverse functions*: families
\((\nu^y)_{y}\) of measures on the sets \(G^y\) of arrows ending at \(y\), compatible with left translation. A
*transverse measure of module \(\delta\)* is a normal additive functional on transverse functions, invariant under
right translation up to the homomorphism \(\delta:G\to\,]0,\infty[\). The case \(\delta\neq1\) is needed to handle
quotients on which no invariant measure exists.

This lesson develops that theory.

1. Kernels and their convolution on a measurable groupoid (Section 1), and transverse functions (Section 2).
2. Transverse measures of module \(\delta\) (Section 3). The main result, Theorem 3.8, is a disintegration theorem:
   once a proper transverse function \(\nu\) is fixed, transverse measures correspond exactly to measures \(\mu\) on the
   unit space whose "conditional measures along the classes" have the prescribed modular behaviour. It is expressed by
   the single identity \(\widetilde{\mu\circ\nu}=\delta^{-1}(\mu\circ\nu)\) for the measure \(\mu\circ\nu\) on \(G\).
3. Consequences (Section 4): reduction to a subset meeting every class, transversals, and actions of locally compact
   groups. Negligible sets (Section 5): only *saturated* sets have a meaning for a transverse measure.
4. Random variables and their integrals (Section 6). A random variable is a measurable functor from \(G\) to measure
   spaces; its integral against a transverse measure is well defined and invariant under isomorphism. This gives the
   *image* of a transverse measure under a *proper* homomorphism (Sections 7 and 8), which is functorial and invariant
   under equivalence of groupoids.
5. Homomorphisms into a locally compact group (Section 9): the stable kernel, and the identification of its
   semidirect product with a product groupoid.

The later lessons "Square-integrable representations and random operators", "Weights on random operators and formal
dimension" and "Transverse measures of foliations" build on the definitions of this lesson: kernels, transverse
functions, the cone \(\mathcal E^+\), transverse measures of module \(\delta\), the measures \(\Lambda_\nu\),
negligible sets, proper functors and homomorphisms, and image measures.

**What is assumed.** Measure theory on abstract measurable spaces, and the basic facts on standard Borel spaces and
on Haar measure, taught in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin's *Measure Theory*) and in the lessons Polish
spaces and standard Borel spaces and Haar measure on locally compact groups. The facts used are listed
below in "Results used from other lessons", with the place where each is proved.

Basic references are [Connes 1979], [Connes 1982] and [Connes 1994]. The idea of treating a quotient space as a
groupoid goes back to Mackey's theory of virtual groups; see also [Ramsay].

**Conventions.** A measure on a measurable space \((Z,\mathcal Z)\) is a countably additive map
\(\mathcal Z\to[0,\infty]\). We write \(\mathcal F^+(Z)\) for the set of measurable maps \(Z\to[0,\infty]\), and
\(m(f)=\int f\,dm\) for \(f\in\mathcal F^+(Z)\); we use \(0\cdot\infty=0\). A measure is *s-finite* if it is a countable
sum of finite measures; every \(\sigma\)-finite measure is s-finite. A measure \(m\) is *carried by* a measurable set
\(E\) if \(m(Z\setminus E)=0\). For a measurable map \(\varphi\), \(\varphi_*m\) is the image measure, and
\(\varepsilon_z\) is the unit mass at \(z\). A subset \(S\subset Z\) carries the *trace* \(\sigma\)-algebra
\(\{E\cap S:E\in\mathcal Z\}\). "Increasing" means "non-decreasing".

## Results used from other lessons

**(B1) Kernels and the Tonelli theorem.** Let \((Y,\mathcal Y)\) and \((Z,\mathcal Z)\) be measurable spaces. A
*kernel* from \(Y\) to \(Z\) is a family \((\kappa_y)_{y\in Y}\) of measures on \(Z\) such that \(y\mapsto\kappa_y(E)\) is
measurable for every \(E\in\mathcal Z\). It is *bounded* if \(\sup_y\kappa_y(Z)<\infty\), and *s-finite* if it is a
countable sum of bounded kernels. For an s-finite kernel \(\kappa\) and \(F\in\mathcal F^+(Y\times Z)\) (product
\(\sigma\)-algebra), the function \(y\mapsto\int F(y,z)\,d\kappa_y(z)\) is measurable. If \(\rho\) and \(\rho'\) are
s-finite measures on \(Y\) and \(Z\), then \(\int\!\!\int F\,d\rho'\,d\rho=\int\!\!\int F\,d\rho\,d\rho'\) (the Tonelli
theorem for s-finite measures). Both statements are proved in Finite conditional expectations, measurable densities, and positive kernel integrals, K.0 and K.4, using the ordinary measure-theory inputs stated in K.0. The proof uses a generating-class argument and nonnegative countable sums, so it also permits infinite values; it does not assert signed interchange or a uniqueness theorem for arbitrary s-finite product measures.

For \(\sigma\)-finite, in particular finite, measures this is in the core course
[Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): [Fremlin, Measure Theory, Volume 2, Theorem 252B and Corollary 252H](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm) (free). An s-finite
measure is a countable sum of finite ones, and both iterated integrals are countably additive in each measure by monotone
convergence, which gives the s-finite case. For the measurability of \(y\mapsto\int F(y,z)\,d\kappa_y(z)\) with \(\kappa\)
bounded: for \(F=1_{A\times B}\) it is \(1_A(y)\kappa_y(B)\); the product-measurable sets with the property form a Dynkin
class containing the measurable rectangles, so the Monotone Class Theorem ([Fremlin, Volume 1, Theorem 136B](https://www1.essex.ac.uk/maths/people/fremlin/cont13.htm))
gives all of them; simple functions and increasing limits give \(\mathcal F^+(Y\times Z)\), and sums of bounded kernels
give s-finite ones.

**(B2) Extension of measurable functions.** If \(S\subset Z\) carries the trace \(\sigma\)-algebra, every
\(f\in\mathcal F^+(S)\) is the restriction of some \(F\in\mathcal F^+(Z)\). (For an indicator \(1_{E\cap S}\) take
\(1_E\); pass to simple functions, and to increasing limits by taking the supremum of the extensions.)

**(B3) Measurable Radon–Nikodym derivatives.** Let \(\mathcal Z\) be countably generated and let \(\kappa,\kappa'\) be
bounded kernels from \(Y\) to \(Z\) with \(\kappa_y\) absolutely continuous with respect to \(\kappa'_y\) for every
\(y\). Then there is \(D\in\mathcal F^+(Y\times Z)\) with \(\kappa_y=D(y,\cdot)\,\kappa'_y\) for every \(y\in Y\). This is proved in Finite conditional expectations, measurable densities, and positive kernel integrals, Theorem K.3. Finite partition quotients are jointly measurable; Theorem K.2 gives convergence separately for each fibre. Taking the finite limit where it exists and zero otherwise yields the stated density for every parameter, without assuming one null set common to all fibres.

*Proof.* Let \(Z_1,Z_2,\ldots\) generate \(\mathcal Z\), and let \(\mathcal P_n\) be the finite partition of \(Z\) into the
nonempty sets of the form \(Z_1^{\pm}\cap\cdots\cap Z_n^{\pm}\), where \(Z_k^+=Z_k\) and \(Z_k^-=Z\setminus Z_k\). For
\(z\in P\in\mathcal P_n\) put \(D_n(y,z)=\kappa_y(P)/\kappa'_y(P)\) if \(\kappa'_y(P)>0\) and \(D_n(y,z)=0\) otherwise.
Each \(D_n\) is measurable on \(Y\times Z\), because \(\mathcal P_n\) is finite and its coefficients are measurable in
\(y\). Let \(D\) be the finite limit of \(D_n\) where that limit exists, and zero otherwise. Fix \(y\) with \(\kappa'_y\neq0\), let \(\mathbb P_y=\kappa'_y/\kappa'_y(Z)\), and let \(f\)
be a density of \(\kappa_y\) with respect to \(\kappa'_y\) (the Radon–Nikodym theorem, Decomposable operators and the
diagonal algebra, Results used from other lessons). Since
\(\int_Pf\,d\kappa'_y=\kappa_y(P)\), \(D_n(y,\cdot)\) is a conditional expectation of \(f\) for \(\mathbb P_y\) on the
finite \(\sigma\)-algebra generated by \(\mathcal P_n\). These \(\sigma\)-algebras increase and generate \(\mathcal Z\).
By Lévy's martingale convergence theorem ([Fremlin, Measure Theory, Volume 2, Theorem
275I](https://www1.essex.ac.uk/maths/people/fremlin/cont27.htm), free, in the core course [Measure and
Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)), \(D_n(y,\cdot)\) converges
\(\kappa'_y\)-almost everywhere to a conditional expectation of \(f\) on \(\mathcal Z\), which is \(f\) itself. So
\(D(y,\cdot)=f\) \(\kappa'_y\)-almost everywhere, and \(\kappa_y=D(y,\cdot)\,\kappa'_y\). If \(\kappa'_y=0\), then
\(\kappa_y=0\) and there is nothing to prove.

**(B4) Haar measure.** A locally compact, second countable group \(H\) has a left Haar measure \(dt\), unique up to a
positive factor, \(\sigma\)-finite, positive on nonempty open sets and finite on compact sets. The modular function
\(\Delta_H:H\to\,]0,\infty[\) is the continuous homomorphism with
\[
\int_H f(ts)\,dt=\Delta_H(s)^{-1}\int_H f(t)\,dt,\qquad \int_H f(t^{-1})\,dt=\int_H f(t)\,\Delta_H(t)^{-1}\,dt
\tag{0.1}
\]
for \(f\in\mathcal F^+(H)\) and \(s\in H\). Proved in Haar measure on locally compact groups:
existence is Theorem 8.3, positivity on open sets and uniqueness are Proposition 9.1 and Theorem 9.2, the modular
function and the first formula are Theorem 10.1, and the second formula is Theorem 11.1. Haar measure is Radon, hence
finite on compact sets, and a second countable locally compact group is a countable union of compact sets, so the
measure is \(\sigma\)-finite.

**(B5) Countable sections.** Let \(Y,Z\) be standard Borel spaces, \(E\subset Y\times Z\) a Borel set all of whose
sections \(E_y=\{z:(y,z)\in E\}\) are countable. Then \(E\) is the union of the graphs of countably many Borel partial
maps \(f_i\) from Borel subsets of \(Y\) to \(Z\) (the Lusin–Novikov theorem), and \(y\mapsto\#E_y\) is Borel. These are Borel sets with countable sections, Theorem 3.1 and Corollary
3.2.

## 1. Measurable groupoids and kernels

A reference for this section and the next is [Connes 1979].

**Definition 1.1.** A *groupoid* is a small category \(G\) in which every arrow is invertible. We identify the set of
objects with the set \(G^{(0)}\subset G\) of identity arrows (the *units*). For \(\gamma\in G\) we write
\(\gamma:x\to y\) when \(x=s(\gamma)=\gamma^{-1}\gamma\) and \(y=r(\gamma)=\gamma\gamma^{-1}\); these define the maps \(r\)
(range) and \(s\) (source) from \(G\) onto \(G^{(0)}\). The product \(\gamma_1\gamma_2\) is defined on
\[
G^{(2)}=\{(\gamma_1,\gamma_2)\in G\times G\ :\ s(\gamma_1)=r(\gamma_2)\}.
\]
For \(x,y\in G^{(0)}\) put \(G^y=r^{-1}(y)\), \(G_x=s^{-1}(x)\) and \(G^y_x=G^y\cap G_x\); the set \(G^y_y\) is a group,
the *isotropy group* at \(y\). Units \(x,y\) are *equivalent*, \(x\sim y\), if \(G^y_x\neq\emptyset\). The classes
are the *orbits*. The *saturation* of \(A\subset G^{(0)}\) is \([A]=\{x:\, x\sim y\text{ for some }y\in A\}\), and
\(A\) is *saturated* if \([A]=A\). The *reduction* of \(G\) to \(A\subset G^{(0)}\) is the groupoid
\(G_A=r^{-1}(A)\cap s^{-1}(A)\).

A *measurable groupoid* is a pair \((G,\mathcal B)\) of a groupoid and a \(\sigma\)-algebra \(\mathcal B\) on \(G\) such
that \(r\), \(s\), \(\gamma\mapsto\gamma^{-1}\) (as maps \(G\to G\)) and the product \(G^{(2)}\to G\) are measurable,
\(G^{(2)}\) carrying the trace of \(\mathcal B\otimes\mathcal B\). The unit space carries the trace
\(\sigma\)-algebra \(\mathcal B_0\). It is *separable* if \(\mathcal B\) is countably generated. A *measurable
homomorphism* \(h:(G,\mathcal B)\to(G',\mathcal B')\) is a measurable map with \(h(\gamma_1\gamma_2)=h(\gamma_1)
h(\gamma_2)\) on \(G^{(2)}\); it maps units to units and inverses to inverses.

**Standing assumption.** Throughout, the one-point subsets of \(G^{(0)}\) belong to \(\mathcal B_0\). Then \(G^y\),
\(G_x\) and \(G_x^y\) belong to \(\mathcal B\): if \(\{y\}=E\cap G^{(0)}\) with \(E\in\mathcal B\), then
\(G^y=r^{-1}(E)\). This holds whenever \(\mathcal B_0\) separates points and is countably generated, in particular for
groupoids whose underlying measurable space is standard Borel. Note also that a function \(a\in\mathcal F^+(G^{(0)})\)
gives measurable functions \(a\circ r\) and \(a\circ s\) on \(G\), and that for \(A\in\mathcal B_0\) the reduction
\(G_A\) belongs to \(\mathcal B\) and is a measurable groupoid for the trace \(\sigma\)-algebra.

**Example 1.2.**

(a) A measurable space \(X\) is a groupoid with \(G=G^{(0)}=X\): every arrow is a unit.

(b) A group with a \(\sigma\)-algebra making product and inverse measurable, for instance a locally compact second
countable group \(H\) with its Borel sets, is a measurable groupoid with one unit \(e\).

(c) If \(R\subset X\times X\) is a measurable equivalence relation on a measurable space \(X\), then \(R\) is a
measurable groupoid with \(R^{(0)}=\{(x,x)\}\cong X\), \(r(x,y)=x\), \(s(x,y)=y\), \((x,y)(y,z)=(x,z)\) and
\((x,y)^{-1}=(y,x)\). The case \(R=X\times X\) is the *pair groupoid* of \(X\). The orbits of \(R\) are its
equivalence classes, and the "space of orbits" is the quotient \(X/R\).

(d) Let a locally compact second countable group \(H\) act measurably on the right on a measurable space \(X\),
\((x,h)\mapsto xh\). The *action groupoid* \(X\rtimes H\) is \(X\times H\) with units \(X\times\{e\}\cong X\) and
\[
r(x,h)=x,\quad s(x,h)=xh,\quad (x,h)(xh,k)=(x,hk),\quad (x,h)^{-1}=(xh,h^{-1}).
\]
Its orbits are the \(H\)-orbits in \(X\).

(e) The product \(G\times K\) of measurable groupoids, with componentwise operations, is a measurable groupoid with unit
space \(G^{(0)}\times K^{(0)}\).

For a measure \(m\) on \(G\) carried by \(G^x\) and \(\gamma:x\to y\) we write \(\gamma m\) for the image of \(m\) under
the left translation \(G^x\to G^y\), \(\gamma'\mapsto\gamma\gamma'\):
\[
(\gamma m)(f)=\int f(\gamma\gamma')\,dm(\gamma').
\]
For \(f\) on \(G\) put \(\tilde f(\gamma)=f(\gamma^{-1})\), and for a measure \(m\) on \(G\) let \(\tilde m\) be its
image under \(\gamma\mapsto\gamma^{-1}\), so that \(\tilde m(f)=m(\tilde f)\).

**Definition 1.3.** A *kernel* on \(G\) is a family \(\lambda=(\lambda^y)_{y\in G^{(0)}}\) of measures on
\((G,\mathcal B)\) such that

1. \(\lambda^y\) is carried by \(G^y\) for every \(y\);
2. \(\lambda\) is an s-finite kernel from \(G^{(0)}\) to \(G\) in the sense of (B1).

For \(f\in\mathcal F^+(G)\) we write \(\lambda(f)\) for the function \(y\mapsto\lambda^y(f)\) on \(G^{(0)}\); it is
measurable by (B1). We write \(\lambda\le\lambda'\) if \(\lambda^y(E)\le\lambda'^y(E)\) for all \(y\) and \(E\). For
\(h\in\mathcal F^+(G)\) the kernel \(h\lambda\) is \(y\mapsto h\,\lambda^y\). For \(a\in\mathcal F^+(G^{(0)})\) the
*diagonal kernel* \(\iota_a\) is \(\iota_a^y=a(y)\,\varepsilon_y\). The kernel \(\lambda\) is *bounded* if
\(\sup_y\lambda^y(G)<\infty\), and *proper* if there is an increasing sequence \((A_n)\) in \(\mathcal B\) with
\(\bigcup_nA_n=G\) and
\[
\sup_{\gamma\in G}\ \lambda^{s(\gamma)}(\gamma^{-1}A_n)<\infty\quad\text{for every }n,\qquad
\gamma^{-1}A=\{\gamma'\in G^{s(\gamma)}:\, \gamma\gamma'\in A\}.
\tag{1.1}
\]
We write \(\mathcal C^+\) for the set of proper kernels on \(G\).

Taking \(\gamma=y\) a unit in (1.1) gives \(\lambda^y(A_n)\le C_n\) for all \(y\); so the restrictions of \(\lambda\) to
\(A_n\setminus A_{n-1}\) are bounded kernels with sum \(\lambda\). Thus a family satisfying condition 1, measurable in
\(y\), and satisfying (1.1) is automatically s-finite. A kernel dominated by a proper kernel is proper (use the same
sets \(A_n\)).

**Lemma 1.4 (convolution).** Let \(\lambda,\lambda_1,\lambda_2,\lambda_3\) be kernels on \(G\) and
\(f\in\mathcal F^+(G)\).

(a) The functions
\[
(f*\tilde\lambda)(\gamma)=\int f(\gamma\gamma')\,d\lambda^{s(\gamma)}(\gamma'),\qquad
(\lambda*f)(\gamma)=\int f(\gamma'^{-1}\gamma)\,d\lambda^{r(\gamma)}(\gamma')
\]
belong to \(\mathcal F^+(G)\), and \((\lambda*f)^\sim=\tilde f*\tilde\lambda\).

(b) The formula \((\lambda_1*\lambda_2)^y(f)=\lambda_1^y(f*\tilde\lambda_2)\) defines a kernel \(\lambda_1*\lambda_2\),
the *convolution*; equivalently \((\lambda_1*\lambda_2)^y=\int\gamma\lambda_2^{s(\gamma)}\,d\lambda_1^y(\gamma)\).

(c) \((\lambda_1*\lambda_2)*\lambda_3=\lambda_1*(\lambda_2*\lambda_3)\),
\(\ (f*\tilde\lambda_3)*\tilde\lambda_2=f*(\lambda_2*\lambda_3)^\sim\) and
\(\ \lambda_1*(\lambda_2*f)=(\lambda_1*\lambda_2)*f\).

(d) For \(a\in\mathcal F^+(G^{(0)})\) put \(s(\lambda)a=\lambda(a\circ s)\). Then \(s(\lambda)\) maps
\(\mathcal F^+(G^{(0)})\) to itself, and \(s(\lambda_1*\lambda_2)=s(\lambda_1)\circ s(\lambda_2)\). We call \(s(\lambda)\)
the *diffusion* of \(\lambda\).

*Proof.* (a) The map \((\gamma,\gamma')\mapsto f(\gamma\gamma')\) is measurable on \(G^{(2)}\); by (B2) it is the
restriction of some \(F\in\mathcal F^+(G\times G)\). The family \(\gamma\mapsto\lambda^{s(\gamma)}\) is an s-finite
kernel from \(G\) to \(G\), and \(\lambda^{s(\gamma)}\) is carried by \(G^{s(\gamma)}=\{\gamma':(\gamma,\gamma')\in
G^{(2)}\}\), so \(\int F(\gamma,\gamma')\,d\lambda^{s(\gamma)}(\gamma')=(f*\tilde\lambda)(\gamma)\) for every choice of
\(F\), and this is measurable by (B1). The same argument applies to \(\lambda*f\), using the measurable map
\((\gamma,\gamma')\mapsto\gamma'^{-1}\gamma\) on \(\{r(\gamma')=r(\gamma)\}\). Finally
\((\lambda*f)(\gamma^{-1})=\int f(\gamma'^{-1}\gamma^{-1})\,d\lambda^{s(\gamma)}(\gamma')=\int\tilde
f(\gamma\gamma')\,d\lambda^{s(\gamma)}(\gamma')\).

(b) By (a) and (B1), \(y\mapsto\lambda_1^y(f*\tilde\lambda_2)\) is measurable, and \(f\mapsto\lambda_1^y(f*\tilde
\lambda_2)\) is a measure by monotone convergence, carried by \(G^y\) because \(\gamma\gamma'\in G^y\) when
\(\gamma\in G^y\). If \(\lambda_1=\sum_i\kappa_i\) and \(\lambda_2=\sum_j\kappa'_j\) with bounded \(\kappa_i,\kappa'_j\),
then \(\lambda_1*\lambda_2=\sum_{i,j}\kappa_i*\kappa'_j\) and \((\kappa_i*\kappa_j')^y(G)\le\sup\kappa_i(G)
\cdot\sup\kappa'_j(G)\); so the convolution is s-finite.

(c) Unwinding the definitions, each side of the second identity at \(\gamma\) equals
\(\int\!\int f(\gamma\gamma'\gamma'')\,d\lambda_3^{s(\gamma')}(\gamma'')\,d\lambda_2^{s(\gamma)}(\gamma')\). The first
identity follows: both sides at \(y\) and \(f\) equal \(\lambda_1^y((f*\tilde\lambda_3)*\tilde\lambda_2)\). For the
third, both sides at \(\gamma\) equal \(\int\!\int f(\gamma''^{-1}\gamma'^{-1}\gamma)\,d\lambda_2^{s(\gamma')}
(\gamma'')\,d\lambda_1^{r(\gamma)}(\gamma')\).

(d) Measurability is (B1). Since \(s(\gamma\gamma')=s(\gamma')\), we have \(((a\circ s)*\tilde\lambda_2)(\gamma)=
\lambda_2^{s(\gamma)}(a\circ s)=(s(\lambda_2)a)(s(\gamma))\), hence \(s(\lambda_1*\lambda_2)a=
\lambda_1((s(\lambda_2)a)\circ s)=s(\lambda_1)(s(\lambda_2)a)\). \(\square\)

**Lemma 1.5.** Let \(\lambda\) be a proper kernel.

(a) If \(h\in\mathcal F^+(G)\) is bounded, \(h\lambda\) is proper.

(b) If \(a\in\mathcal F^+(G^{(0)})\) is finite-valued, \((a\circ s)\lambda\) is proper.

(c) If \(a\in\mathcal F^+(G^{(0)})\) is finite-valued, the diagonal kernel \(\iota_a\) is proper.

*Proof.* (a) is clear. (b) Let \((A_n)\) be as in (1.1) with bounds \(C_n\), and put \(A'_n=A_n\cap
s^{-1}(\{a\le n\})\), an increasing sequence with union \(G\). Since \(s(\gamma\gamma')=s(\gamma')\),
\[
((a\circ s)\lambda)^{s(\gamma)}(\gamma^{-1}A'_n)=\int1_{A'_n}(\gamma\gamma')\,a(s(\gamma\gamma'))\,
d\lambda^{s(\gamma)}(\gamma')\le n\,C_n .
\]
(c) \(\iota_a^{s(\gamma)}(\gamma^{-1}E)=a(s(\gamma))1_E(\gamma)\), which is at most \(n\) on
\(E=s^{-1}(\{a\le n\})\). \(\square\)

**Example 1.6.** Boundedness in (a) cannot be dropped. Let \(G=\mathbb Z\) with all subsets measurable, written
additively, \(\lambda\) counting measure and \(h(k)=|k|\). Then \(\lambda\) is proper (take \(A_n=[-n,n]\)). For any
increasing sequence \((A_n)\) with union \(\mathbb Z\) choose \(n\) with \(A_n\) nonempty and \(a\in A_n\); then
\((h\lambda)(\gamma^{-1}A_n)=\sum_{k\in A_n-\gamma}|k|\ge|a-\gamma|\), which is unbounded in \(\gamma\). So \(h\lambda\)
is not proper. In contrast, (b) allows unbounded factors that are functions of \(s(\gamma)\) alone.

The convolution of two proper kernels need not be proper. Two sufficient conditions follow.

**Lemma 1.7.** Let \(\lambda_1,\lambda_2\) be kernels on \(G\).

(a) If \(\lambda_1\) is bounded and \(\lambda_2\) is proper, then \(\lambda_1*\lambda_2\) is proper.

(b) Suppose \(\lambda_2^y(G)\le c\) for all \(y\) and that every \(\lambda_2^y\) is carried by a fixed \(B\in\mathcal B\).
Suppose there are an increasing sequence \((A_n)\) in \(\mathcal B\) with union \(G\) and sets \(E_n\in\mathcal B\)
containing \(A_nB^{-1}=\{\alpha\beta^{-1}:\alpha\in A_n,\ \beta\in B,\ s(\alpha)=s(\beta)\}\) such that
\(\sup_\gamma\lambda_1^{s(\gamma)}(\gamma^{-1}E_n)<\infty\) for each \(n\). Then \(\lambda_1*\lambda_2\) is proper.

*Proof.* For \(\gamma\in G\), \(x=s(\gamma)\) and \(A\in\mathcal B\), Lemma 1.4(b) gives
\[
(\lambda_1*\lambda_2)^{x}(\gamma^{-1}A)=\int\lambda_2^{s(\gamma')}\big((\gamma\gamma')^{-1}A\big)\,
d\lambda_1^{x}(\gamma').
\]
(a) With \((A_n)\) and \(C_n\) as in (1.1) for \(\lambda_2\), the integrand is at most \(C_n\) for \(A=A_n\), so the
integral is at most \(C_n\sup_x\lambda_1^x(G)\).

(b) If \(\lambda_2^{s(\gamma')}((\gamma\gamma')^{-1}A_n)\neq0\), there is \(\beta\in B\cap G^{s(\gamma')}\) with
\(\gamma\gamma'\beta\in A_n\), so \(\gamma\gamma'=(\gamma\gamma'\beta)\beta^{-1}\in E_n\). Hence the integrand is at most
\(c\,1_{E_n}(\gamma\gamma')\) and the integral is at most \(c\,\lambda_1^x(\gamma^{-1}E_n)\), which is bounded. \(\square\)

## 2. Transverse functions

**Definition 2.1.** A *transverse function* on \(G\) is a kernel \(\nu\) such that
\[
\gamma\,\nu^{x}=\nu^{y}\qquad\text{for every }\gamma:x\to y.
\tag{2.1}
\]
We write \(\bar{\mathcal E}^+=\bar{\mathcal E}^+(G)\) for the set of transverse functions and
\(\mathcal E^+=\mathcal E^+(G)\) for the set of *proper* ones. The *support* of \(\nu\) is
\(\operatorname{supp}\nu=\{y\in G^{(0)}:\nu^y\neq0\}\), and \(\nu\) is *faithful* if its support is \(G^{(0)}\).

On the groupoid of an equivalence relation (Example 1.2(c)), \(G^y\) is the class of \(y\), and (2.1) says that
\(\nu^y\) depends only on the class of \(y\): a transverse function is a measure on each class, i.e. a
\([0,\infty]\)-valued generalized function on the quotient in the sense of the introduction. On a group it is a left
invariant measure.

**Lemma 2.2.** Let \(\nu\in\bar{\mathcal E}^+\).

(a) \(\operatorname{supp}\nu\) is measurable and saturated.

(b) \(\nu\) is proper if and only if there is an increasing sequence \((A_n)\) in \(\mathcal B\) with union \(G\)
and \(\sup_{y\in G^{(0)}}\nu^y(A_n)<\infty\) for each \(n\).

(c) If \(\nu_n\in\bar{\mathcal E}^+\) is an increasing sequence with \(\nu_n\le\nu'\) for some \(\nu'\in\mathcal E^+\),
then \(\sup_n\nu_n\), defined by \((\sup_n\nu_n)^y(E)=\sup_n\nu_n^y(E)\), belongs to \(\mathcal E^+\). We then write
\(\nu_n\uparrow\sup_n\nu_n\).

(d) If \(\nu\in\mathcal E^+\) and \(a\in\mathcal F^+(G^{(0)})\) is finite-valued, then \((a\circ s)\nu\in\mathcal
E^+\).

(e) If \(\lambda\) is any kernel, \(\nu*\lambda\in\bar{\mathcal E}^+\).

(f) \(\mathcal E^+\) is stable under sums and multiplication by numbers in \([0,\infty[\).

*Proof.* (a) \(\operatorname{supp}\nu=\{y:\nu^y(G)>0\}\) is measurable, and \(\gamma\nu^x=\nu^y\) has the same total
mass as \(\nu^x\).

(b) By (2.1), \(\nu^{s(\gamma)}(\gamma^{-1}A)=(\gamma\nu^{s(\gamma)})(A)=\nu^{r(\gamma)}(A)\); as \(\gamma\) runs over
\(G\), \(r(\gamma)\) runs over \(G^{(0)}\).

(c) An increasing limit of measures is a measure, and measurability in \(y\) passes to the limit. The limit is
dominated by \(\nu'\), so it satisfies (1.1) and is s-finite. Relation (2.1) passes to the limit.

(d) Since \(s(\gamma\gamma')=s(\gamma')\), \(\gamma((a\circ s)\nu^x)=(a\circ s)\,\gamma\nu^x=(a\circ s)\nu^y\).
Properness is Lemma 1.5(b).

(e) For \(\gamma:x\to y\), using (2.1) with \(\gamma''=\gamma\gamma'\) (so \(s(\gamma'')=s(\gamma')\)):
\[
\gamma(\nu*\lambda)^x=\int\gamma\gamma'\lambda^{s(\gamma')}\,d\nu^x(\gamma')=
\int\gamma''\lambda^{s(\gamma'')}\,d(\gamma\nu^x)(\gamma'')=(\nu*\lambda)^y .
\]
(f) is clear, taking \(A_n\cap A'_n\) for a sum. \(\square\)

**Example 2.3.**

(a) *Spaces.* If \(G=G^{(0)}=X\), a kernel is \(\nu^x=a(x)\varepsilon_x\) with \(a\in\mathcal F^+(X)\), and (2.1) is
empty. It is proper if and only if \(a\) is finite-valued: if \(a(x_0)=\infty\), every \(A_n\) containing \(x_0\) has
\(\nu^{x_0}(A_n)=\infty\); if \(a\) is finite, take \(A_n=\{a\le n\}\). So \(\mathcal E^+(X)\) is the set of finite
measurable functions: transverse functions generalize functions.

(b) *Groups.* If \(G=H\) is a locally compact second countable group, a transverse function is a left invariant
s-finite measure on \(H\). Left Haar measure \(dt\) is in \(\mathcal E^+\): take \(A_n\) compact with union \(H\).

(c) *Pair groupoid of a countable set.* Let \(S\) be countable with all subsets measurable and \(G=S\times S\). Then
\(G^t=\{t\}\times S\), and \((t,t')\) maps \((t',u)\) to \((t,u)\). So transverse functions are the families
\(\nu^t=\varepsilon_t\otimes\rho\) for one measure \(\rho\) on \(S\). Such a \(\nu\) is proper if and only if
\(\rho(\{u\})<\infty\) for all \(u\): if \(\rho(\{u\})=\infty\), every \(A_n\) containing some \((t,u)\) has
\(\nu^t(A_n)=\infty\); otherwise take \(A_n=S\times F_n\) with finite \(F_n\uparrow S\).

(d) *Action groupoids.* For \(G=X\rtimes H\) as in Example 1.2(d), let \(\nu_H^x\) be the image of left Haar measure
under \(h\mapsto(x,h)\). For \(\gamma=(x,h):xh\to x\), left translation sends \((xh,k)\) to \((x,hk)\), so
\(\gamma\nu_H^{xh}=\nu_H^x\) by left invariance. Measurability in \(x\) follows from (B1), and \(\nu_H\) is proper with
\(A_n=X\times K_n\), \(K_n\) compact. It is faithful.

**Lemma 2.4 (normalizing functions).** Let \(\nu\in\mathcal E^+\), \(A=\operatorname{supp}\nu\), and let
\(w:G\to\,]0,\infty[\) be measurable. There is \(g\in\mathcal F^+(G)\) with \(0<g\le w\) everywhere and
\(\nu(g)\le1\). Put \(b=1_A/\nu(g)\) (with \(b=0\) off \(A\)), a finite measurable function on \(G^{(0)}\), and
\(f=(b\circ r)\,g\). Then
\[
\nu(f)=1_A,\qquad f>0\ \text{on}\ G_A=r^{-1}(A),\qquad f=0\ \text{off}\ G_A .
\]
*Proof.* Take \((A_n)\) as in Lemma 2.2(b) with \(\nu^y(A_n)\le C_n\), \(C_n\ge1\), and put
\(g=\min(1,w)\sum_n2^{-n}C_n^{-1}1_{A_n}\). Then \(0<g\le w\) because every \(\gamma\) lies in some \(A_n\), and
\(\nu^y(g)\le\sum_n2^{-n}=1\). For \(y\in A\), \(\nu^y\neq0\) and \(g>0\), so \(\nu^y(g)>0\) and \(b(y)<\infty\). Since
\(\nu^y\) is carried by \(G^y\), \(\nu^y(f)=b(y)\nu^y(g)=1_A(y)\). As \(A\) is saturated, \(r^{-1}(A)=s^{-1}(A)=G_A\).
\(\square\)

**Proposition 2.5.** Let \(\nu\) be a kernel on \(G\).

(a) \(\nu\) is a transverse function if and only if \(f*\tilde\nu=\nu(f)\circ r\) for all \(f\in\mathcal F^+(G)\).
In that case \(\nu*f=\nu(\tilde f)\circ s\) for all \(f\).

(b) If \(\nu\in\bar{\mathcal E}^+\) and \(\lambda\) is a kernel, then \(\nu(\lambda*f)=\lambda(\nu(f)\circ s)=
s(\lambda)(\nu(f))\) for all \(f\in\mathcal F^+(G)\).

(c) If \(\nu\in\bar{\mathcal E}^+\), \(\lambda\) is a kernel and \(f\in\mathcal F^+(G)\), then
\[
\lambda*(f\nu)=(\lambda*f)\,\nu,\qquad \lambda*\nu=(\lambda(1)\circ r)\,\nu .
\]
*Proof.* (a) For \(\gamma:x\to y\), \((f*\tilde\nu)(\gamma)=(\gamma\nu^x)(f)\) while \(\nu(f)(r(\gamma))=\nu^y(f)\). These
agree for all \(f\) exactly when \(\gamma\nu^x=\nu^y\). Then, by Lemma 1.4(a), \((\nu*f)(\gamma)=(\tilde
f*\tilde\nu)(\gamma^{-1})=\nu(\tilde f)(r(\gamma^{-1}))=\nu(\tilde f)(s(\gamma))\).

(b) Fix \(y\). Both \(\nu^y\) and \(\lambda^y\) are s-finite measures carried by \(G^y\), so by (B1)
\[
\nu^y(\lambda*f)=\int\!\!\int f(\gamma'^{-1}\gamma)\,d\lambda^y(\gamma')\,d\nu^y(\gamma)
=\int\Big(\int f(\gamma'^{-1}\gamma)\,d\nu^y(\gamma)\Big)d\lambda^y(\gamma').
\]
For \(\gamma'\in G^y\), \(\gamma'^{-1}:y\to s(\gamma')\) carries \(\nu^y\) to \(\nu^{s(\gamma')}\) by (2.1), so the inner
integral is \(\nu(f)(s(\gamma'))\).

(c) For \(k\in\mathcal F^+(G)\), by definition and (2.1) (with \(x=s(\gamma)\)),
\[
(\lambda*(f\nu))^y(k)=\int\Big(\int k(\gamma\gamma')f(\gamma')\,d\nu^{x}(\gamma')\Big)d\lambda^y(\gamma)
=\int\Big(\int k(\eta)f(\gamma^{-1}\eta)\,d\nu^{y}(\eta)\Big)d\lambda^y(\gamma).
\]
Exchanging the two integrals over \(G^y\) (B1) gives \(\int k(\eta)(\lambda*f)(\eta)\,d\nu^y(\eta)\), since
\(r(\eta)=y\). For \(f=1\), \((\lambda*1)(\eta)=\lambda^{r(\eta)}(1)\). \(\square\)

**Proposition 2.6.** Let \(\nu,\nu'\in\mathcal E^+\) with \(\operatorname{supp}\nu'\subset\operatorname{supp}\nu=A\),
let \(f\) be as in Lemma 2.4 for \(\nu\), and put \(k=\tilde f\). Then \(\lambda=k\nu'\) is a proper kernel and
\(\nu*\lambda=\nu'\).

*Proof.* By Propositions 2.5(c) and 2.5(a), \(\nu*(k\nu')=(\nu*k)\nu'=(\nu(f)\circ s)\nu'=(1_A\circ s)\nu'\). For
\(y\in A\), \(\nu'^y\) is carried by \(G^y\subset s^{-1}(A)\) since \(A\) is saturated; for \(y\notin A\),
\(\nu'^y=0\). So \((1_A\circ s)\nu'=\nu'\). For properness, \(k=\tilde f=(b\circ s)\tilde g\) with \(\tilde g\le1\); so
\(\tilde g\nu'\) is proper by Lemma 1.5(a), and \(k\nu'=(b\circ s)(\tilde g\nu')\) by Lemma 1.5(b). \(\square\)

The factorization \(k=(b\circ s)\tilde g\) matters: \(k\) itself is usually unbounded, and Example 1.6 shows that
multiplying a proper kernel by an unbounded function can destroy properness.

**Proposition 2.7.** Let \(G\) be separable, and let \(\nu_1,\nu_2\in\mathcal E^+\) be such that \(\nu_1^y\) is
absolutely continuous with respect to \(\nu_2^y\) for every \(y\). Then there is a finite-valued
\(a\in\mathcal F^+(G^{(0)})\) with \(\nu_1=(a\circ s)\nu_2\).

*Proof.* *Step 1: a measurable density.* Take exhausting sequences \((A_n)\), \((A'_n)\) for \(\nu_2\), \(\nu_1\) as in
Lemma 2.2(b), with bounds \(C_n\), \(C'_n\), and put \(w=\sum_n2^{-n}(1+C_n+C'_n)^{-1}1_{A_n\cap A'_n}\), a strictly
positive function. Then \(w\nu_1\) and \(w\nu_2\) are bounded kernels from \(G^{(0)}\) to \(G\), and \(w\nu_1^y\) is
absolutely continuous with respect to \(w\nu_2^y\). By (B3) there is a measurable \(D\) on \(G^{(0)}\times G\) with
\(w\nu_1^y=D(y,\cdot)\,w\nu_2^y\). Put \(h(\gamma)=D(r(\gamma),\gamma)\), a measurable function on \(G\). Since
\(\nu_i^y\) is carried by \(G^y\) and \(w>0\), \(\nu_1^y=h\,\nu_2^y\) for every \(y\).

*Step 2: almost invariance.* Fix \(y\) and \(\gamma_1\in G^y\), \(x_1=s(\gamma_1)\). By (2.1), \(h\nu_2^y=\nu_1^y=
\gamma_1\nu_1^{x_1}=\gamma_1(h\nu_2^{x_1})=(h\circ L_{\gamma_1}^{-1})\,\nu_2^y\), where \(L_{\gamma_1}\) is left
translation by \(\gamma_1\). Densities with respect to the \(\sigma\)-finite measure \(\nu_2^y\) are unique almost
everywhere, so \(h(\gamma_1^{-1}\eta)=h(\eta)\) for \(\nu_2^y\)-almost every \(\eta\in G^y\). The set
\(N=\{(\gamma_1,\eta)\in G^y\times G^y:h(\gamma_1^{-1}\eta)\ne h(\eta)\}\) is measurable and each of its sections
\(N_{\gamma_1}\) is \(\nu_2^y\)-null. By the Tonelli theorem, for \(\nu_2^y\)-almost every \(\eta\), the section
\(\{\gamma_1:(\gamma_1,\eta)\in N\}\) is \(\nu_2^y\)-null.

*Step 3: the function \(a\).* Let \(f\) be as in Lemma 2.4 for \(\nu_2\) (so \(\nu_2(f)=1_A\),
\(A=\operatorname{supp}\nu_2\)) and put \(a_0(x)=\nu_2^x(\tilde h f)\), a measurable function on \(G^{(0)}\). Let
\(y\in A\) and let \(\eta\in G^y\) be as at the end of Step 2, with \(x=s(\eta)\in A\). Then, substituting
\(\gamma_1=\eta\zeta\) with \(\zeta\in G^x\) (the translation by \(\eta\) carries \(\nu_2^x\) to \(\nu_2^y\)),
\[
\int h(\gamma_1^{-1}\eta)\,f(\eta^{-1}\gamma_1)\,d\nu_2^y(\gamma_1)=\int h(\zeta^{-1})f(\zeta)\,d\nu_2^x(\zeta)=a_0(x),
\]
while by the choice of \(\eta\) the left side is \(h(\eta)\int f(\eta^{-1}\gamma_1)\,d\nu_2^y(\gamma_1)=h(\eta)\,
\nu_2^x(f)=h(\eta)\). Hence \(h=a_0\circ s\) \(\nu_2^y\)-almost everywhere, and \(\nu_1^y=(a_0\circ s)\nu_2^y\), for every
\(y\in A\). For \(y\notin A\) both sides vanish.

*Step 4: finiteness.* Let \(Z=s^{-1}(\{a_0=\infty\})\). Since \(\nu_1^y(A'_n\cap Z)\le C'_n<\infty\) and
\(\nu_1^y=\infty\cdot\nu_2^y\) on \(Z\), we get \(\nu_2^y(A'_n\cap Z)=0\) for all \(n\), so \(\nu_2^y(Z)=0\). Replacing
\(a_0\) by \(a=a_0 1_{\{a_0<\infty\}}\) does not change \((a\circ s)\nu_2\). \(\square\)

**Definition 2.8 (transversals and discrete groupoids).** Let \(T\in\mathcal B_0\). For \(y\in G^{(0)}\) and \(E\in\mathcal B\) put
\[
\nu_T^y(E)=\#\big(E\cap G^y\cap s^{-1}(T)\big).
\]
Left translation by \(\gamma:x\to y\) is a bijection of \(G^x\cap s^{-1}(T)\) onto \(G^y\cap s^{-1}(T)\), so
\(\gamma\nu_T^x=\nu_T^y\). We call \(T\) a *transversal* if \(y\mapsto\nu_T^y(E)\) is measurable for every \(E\) and the
resulting transverse function \(\nu_T\) is proper. Then each \(G^y\cap s^{-1}(T)\) is countable, since a counting
measure that is \(\sigma\)-finite lives on a countable set. The support of \(\nu_T\) is the saturation \([T]\); we call
\(T\) a *complete* transversal if \([T]=G^{(0)}\), that is, if \(\nu_T\) is faithful. We call \(G\) *discrete* if
\(G^{(0)}\) is a transversal, that is, if the counting measures on the sets \(G^y\) form a proper transverse function.
If \(T\) is a transversal, the reduction \(G_T\) is discrete: for \(y\in T\), the counting measure on \(G_T^y=G^y\cap
s^{-1}(T)\) is \(\nu_T^y\).

When \(G\) is a standard Borel space and each \(G^y\cap s^{-1}(T)\) is countable, the measurability of \(\nu_T\) is
automatic by (B5), applied to \(\{(y,\gamma):\gamma\in E\cap s^{-1}(T),\ r(\gamma)=y\}\).

**Example 2.9.**

(a) A locally compact second countable group \(H\) is discrete in the sense of Definition 2.8 if and only if it is countable, if
and only if its topology is discrete. Indeed, if counting measure is proper there are \(A_n\uparrow H\) with \(\#A_n<
\infty\), so \(H\) is countable; a countable locally compact group is a countable union of closed points, so by the
Baire category theorem some point, hence every point, is open. Conversely, on a countable group take finite
\(A_n\uparrow H\).

(b) A countable Borel equivalence relation \(R\) on a standard Borel space \(X\) (Example 1.2(c) with countable
classes and \(R\) Borel) is discrete. Measurability comes from (B5). By (B5), \(R\) is the union of the graphs of
countably many Borel partial maps \(f_i\) on \(X\), viewed as sets of arrows \((y,f_i(y))\in R^y\); with
\(A_n=\bigcup_{i\le n}\operatorname{graph}(f_i)\) we get \(\#(A_n\cap R^y)\le n\).

## 3. Transverse measures

**Modules.** A *module* on \(G\) is a measurable map \(\delta:G\to\,]0,\infty[\) with
\(\delta(\gamma_1\gamma_2)=\delta(\gamma_1)\delta(\gamma_2)\) on \(G^{(2)}\). Then \(\delta=1\) on \(G^{(0)}\) (since
\(\delta(y)=\delta(y)^2\)) and \(\tilde\delta=\delta^{-1}\). For a kernel \(\lambda\), \(\delta\lambda\) and
\(\delta^{-1}\lambda\) are kernels (write \(\delta=\sum_n\delta1_{\{n-1<\delta\le n\}}\) to see s-finiteness).

**Definition 3.1.** Let \(\delta\) be a module on \(G\). A *transverse measure of module \(\delta\)* on \(G\) is a map
\(\Lambda:\mathcal E^+\to[0,\infty]\) such that

1. \(\Lambda\) is *additive and positively homogeneous*: \(\Lambda(\nu+\nu')=\Lambda(\nu)+\Lambda(\nu')\) and
   \(\Lambda(c\nu)=c\Lambda(\nu)\) for \(c\in[0,\infty[\);
2. \(\Lambda\) is *normal*: \(\Lambda(\nu)=\sup_n\Lambda(\nu_n)\) whenever \(\nu_n\uparrow\nu\) in \(\mathcal E^+\);
3. \(\Lambda\) has *module \(\delta\)*: if \(\nu,\nu'\in\mathcal E^+\) and \(\rho\) is a kernel with \(\rho^y(G)=1\) for
   all \(y\) and \(\nu'=\nu*\delta\rho\), then \(\Lambda(\nu')=\Lambda(\nu)\).

\(\Lambda\) is *semi-finite* if \(\Lambda(\nu)=\sup\{\Lambda(\nu'):\nu'\in\mathcal E^+,\ \nu'\le\nu,\
\Lambda(\nu')<\infty\}\) for all \(\nu\), and *\(\sigma\)-finite* if there are \(\nu_n\in\mathcal E^+\) with
\(\Lambda(\nu_n)<\infty\) and \(\nu_n\uparrow\nu\) for a faithful \(\nu\).

When \(\delta=1\), condition 3 is invariance under right translation. For instance, if \(\theta:G^{(0)}\to G\) is
measurable with \(r(\theta(y))=y\) and \(\rho^y=\varepsilon_{\theta(y)}\), then \((\nu*\rho)^y\) is the image of \(\nu^y\)
under \(\gamma\mapsto\gamma\,\theta(s(\gamma))\); condition 3 says that moving each fibre measure to the right in this
way does not change \(\Lambda\). In the picture of the introduction, it says that measurably equivalent generalized
functions have the same integral, while normality expresses countable additivity.

**Definition 3.2.** For a transverse measure \(\Lambda\) and \(\nu\in\mathcal E^+\), put
\(\Lambda_\nu(E)=\Lambda((1_E\circ s)\nu)\) for \(E\in\mathcal B_0\).

**Lemma 3.3.** \(\Lambda_\nu\) is a measure on \(G^{(0)}\), and \(\Lambda_\nu(a)=\Lambda((a\circ s)\nu)\) for every
finite-valued \(a\in\mathcal F^+(G^{(0)})\). Moreover \(\Lambda(\nu)=\Lambda_\nu(1)\),
\(\Lambda_{(a\circ s)\nu}=a\,\Lambda_\nu\) for finite \(a\), \(\Lambda_{\nu+\nu'}=\Lambda_\nu+\Lambda_{\nu'}\), and
\(\Lambda_\nu\) is carried by \(\operatorname{supp}\nu\).

*Proof.* By Lemma 2.2(d), \((1_E\circ s)\nu\in\mathcal E^+\). Finite additivity is condition 1. If \(E_n\uparrow E\),
then \((1_{E_n}\circ s)\nu\uparrow(1_E\circ s)\nu\) with all terms below \(\nu\), so normality gives countable
additivity. For a simple finite \(a\) the formula is linearity; for finite \(a\) choose simple \(a_n\uparrow a\) and use
normality on the left and monotone convergence on the right. Then \(\Lambda_{(a\circ s)\nu}(E)=\Lambda((1_Ea\circ
s)\nu)=\Lambda_\nu(1_Ea)\). Finally, for \(y\in A=\operatorname{supp}\nu\), \(\nu^y\) is carried by \(s^{-1}(A)\), and
\(\nu^y=0\) otherwise; so \((1_{G^{(0)}\setminus A}\circ s)\nu=0\). \(\square\)

We use the measure \(\Lambda_\nu\) on all of \(\mathcal F^+(G^{(0)})\), including functions with infinite values.

**Proposition 3.4.** Let \(\Lambda\) be a transverse measure of module \(\delta\), \(\nu\in\mathcal E^+\) and
\(\lambda\) a kernel with \(\nu*\lambda\in\mathcal E^+\). Then
\[
\Lambda(\nu*\lambda)=\Lambda_\nu\big(\lambda(\delta^{-1})\big).
\tag{3.1}
\]
*Proof.* *Case 1: \(a=\lambda(\delta^{-1})\) is finite-valued.* Put \(\rho^y=a(y)^{-1}\delta^{-1}\lambda^y\) if
\(a(y)>0\) and \(\rho^y=\varepsilon_y\) if \(a(y)=0\). Then \(\rho\) is a kernel with \(\rho^y(G)=1\), and
\(\lambda=(a\circ r)\,\delta\rho\): where \(a(y)=0\) both sides vanish at \(y\), because \(\delta^{-1}>0\) forces
\(\lambda^y=0\). For any kernel \(\kappa\) and finite \(a\), \(\nu*((a\circ r)\kappa)=((a\circ s)\nu)*\kappa\), because
\(((a\circ r)\kappa)^{s(\gamma)}=a(s(\gamma))\kappa^{s(\gamma)}\) in Lemma 1.4(b). Hence
\(\nu*\lambda=((a\circ s)\nu)*\delta\rho\) with \((a\circ s)\nu\in\mathcal E^+\) (Lemma 2.2(d)), and condition 3 of
Definition 3.1 gives \(\Lambda(\nu*\lambda)=\Lambda((a\circ s)\nu)=\Lambda_\nu(a)\).

*General case.* Write \(\lambda=\sum_i\kappa_i\) with bounded \(\kappa_i\) and put
\(\lambda_N=\sum_{i\le N}1_{\{\delta^{-1}\le N\}}\kappa_i\). Then \(\lambda_N(\delta^{-1})\) is bounded,
\(\lambda_N\uparrow\lambda\), and \(\nu*\lambda_N\uparrow\nu*\lambda\) (monotone convergence in Lemma 1.4(b)). Each
\(\nu*\lambda_N\) is transverse (Lemma 2.2(e)) and dominated by \(\nu*\lambda\in\mathcal E^+\), hence in \(\mathcal E^+\).
By Case 1 and normality, \(\Lambda(\nu*\lambda)=\sup_N\Lambda_\nu(\lambda_N(\delta^{-1}))=\Lambda_\nu(\lambda(\delta^{-1}))\).
\(\square\)

For \(\nu\in\bar{\mathcal E}^+\) and a measure \(\mu\) on \(G^{(0)}\) we write \(\mu\circ\nu\) for the measure
\(f\mapsto\int\nu^y(f)\,d\mu(y)\) on \(G\). The next theorem is the basic identity of the theory.

**Theorem 3.5 (modular symmetry).** Let \(\Lambda\) be a transverse measure of module \(\delta\) and
\(\nu,\nu'\in\mathcal E^+\). For every \(h\in\mathcal F^+(G)\),
\[
\Lambda_{\nu'}\big(\nu(\tilde h)\big)=\Lambda_\nu\big(\nu'(\delta^{-1}h)\big).
\tag{3.2}
\]
In particular the measure \(m=\Lambda_\nu\circ\nu\) on \(G\) satisfies \(\tilde m=\delta^{-1}m\), that is
\(m(\tilde h)=m(\delta^{-1}h)\) for all \(h\).

*Proof.* Suppose first that \(\nu(\tilde h)\) is finite-valued. By Propositions 2.5(c) and 2.5(a),
\(\nu*(h\nu')=(\nu*h)\nu'=(\nu(\tilde h)\circ s)\nu'\), which lies in \(\mathcal E^+\) by Lemma 2.2(d). Proposition 3.4
with \(\lambda=h\nu'\) gives \(\Lambda(\nu*(h\nu'))=\Lambda_\nu((h\nu')(\delta^{-1}))=\Lambda_\nu(\nu'(\delta^{-1}h))\), and
Lemma 3.3 gives \(\Lambda((\nu(\tilde h)\circ s)\nu')=\Lambda_{\nu'}(\nu(\tilde h))\). For general \(h\), let \((A_n)\)
be as in Lemma 2.2(b) for \(\nu\), with bounds \(C_n\), and put \(h_n=\min(h,n)\,\widetilde{1_{A_n}}\). Then
\(\nu(\tilde h_n)\le nC_n\) and \(h_n\uparrow h\); apply monotone convergence on both sides. The last statement is the
case \(\nu'=\nu\). \(\square\)

**Corollary 3.6 (change of transverse function).** Let \(\nu\in\mathcal E^+\) be faithful and let
\(k\in\mathcal F^+(G)\) satisfy \(\nu*k=1\), that is \(\nu(\tilde k)=1\) (Proposition 2.5(a)); for instance \(k=\tilde f\)
with \(f\) as in Lemma 2.4. For every
\(\nu'\in\mathcal E^+\) and \(a\in\mathcal F^+(G^{(0)})\),
\[
\Lambda_{\nu'}(a)=\int\nu'^y\big(\delta^{-1}k\,(a\circ s)\big)\,d\Lambda_\nu(y).
\tag{3.3}
\]
*Proof.* Apply (3.2) with \(h=k\,(a\circ s)\). Then \(\tilde h=\tilde k\,(a\circ r)\), so \(\nu(\tilde h)(y)=a(y)\nu^y(\tilde k)=a(y)\).
\(\square\)

**Proposition 3.7.** Let \(\Lambda\) be a transverse measure of module \(\delta\), \(\nu,\nu'\in\mathcal E^+\), and
\(\lambda\) a kernel with \(\nu'=\nu*\delta\lambda\). Let \(D=s(\lambda)\) be its diffusion. Then
\[
\Lambda_{\nu'}=\Lambda_\nu\circ D,\qquad\text{and}\qquad
\Lambda_{\nu'}\big(\nu'(f)\big)=\Lambda_\nu\Big(\nu\big(\lambda*f*(\delta\lambda)^\sim\big)\Big)\quad(f\in\mathcal F^+(G)).
\]
*Proof.* For finite \(a\), \((a\circ s)\nu'=\nu*((a\circ s)\delta\lambda)\) because \(s(\gamma\gamma')=s(\gamma')\) in
Lemma 1.4(b). By Proposition 3.4, \(\Lambda_{\nu'}(a)=\Lambda_\nu(((a\circ s)\delta\lambda)(\delta^{-1}))=
\Lambda_\nu(\lambda(a\circ s))=\Lambda_\nu(Da)\); monotone convergence extends this to all \(a\). Next,
\(\nu'(f)=\nu(f*(\delta\lambda)^\sim)\) by definition of the convolution, and \(D(\nu(g))=\lambda(\nu(g)\circ s)=
\nu(\lambda*g)\) by Proposition 2.5(b). So \(\Lambda_{\nu'}(\nu'(f))=\Lambda_\nu(D\nu(f*(\delta\lambda)^\sim))=
\Lambda_\nu(\nu(\lambda*(f*(\delta\lambda)^\sim)))\). \(\square\)

The following theorem characterizes the measures on \(G^{(0)}\) of the form \(\Lambda_\nu\). It is an analogue of the
disintegration of measures: condition (1) says that the measure \(\mu\circ\nu\) on \(G\), which disintegrates over
\(r\) with conditional measures \(\nu^y\), behaves under inversion as prescribed by \(\delta\).

**Theorem 3.8 (transverse measures and measures on the units).** Let \(\nu\in\mathcal E^+\) with support \(A\). The
map \(\Lambda\mapsto\Lambda_\nu\) is a bijection from the set of transverse measures of module \(\delta\) on \(G_A\)
onto the set of measures \(\mu\) on \(G^{(0)}\) carried by \(A\) that satisfy the following equivalent conditions:

1. \(\widetilde{\mu\circ\nu}=\delta^{-1}(\mu\circ\nu)\), that is, \(\int\nu^y(\tilde h)\,d\mu(y)=\int\nu^y(\delta^{-1}h)
   \,d\mu(y)\) for all \(h\in\mathcal F^+(G)\);
2. if \(\lambda,\lambda'\in\mathcal C^+\) and \(\nu*\lambda=\nu*\lambda'\in\mathcal E^+\), then
   \(\mu(\lambda(\delta^{-1}))=\mu(\lambda'(\delta^{-1}))\).

(Here \(\nu\) is regarded as a faithful proper transverse function on \(G_A\), and \(\Lambda_\nu\), a measure on \(A\),
as a measure on \(G^{(0)}\) carried by \(A\).) The inverse map is \(\mu\mapsto\Lambda\) with
\[
\Lambda(\nu')=\int\nu'^y(\delta^{-1}k)\,d\mu(y)\qquad(\nu'\in\mathcal E^+(G_A)),
\tag{3.4}
\]
for any \(k\in\mathcal F^+(G_A)\) with \(\nu*k=1\) on \(G_A\), and for every kernel \(\lambda\) on \(G_A\) with
\(\nu*\lambda\in\mathcal E^+\) one has \(\Lambda(\nu*\lambda)=\mu(\lambda(\delta^{-1}))\).

*Proof.* For \(y\in A\), \(\nu^y\) is carried by \(G^y\subset G_A\) (as \(A\) is saturated), and for \(y\notin A\),
\(\nu^y=0\). So condition (1) only involves the restriction of \(h\) to \(G_A\) and the restriction of \(\mu\) to \(A\).
Replacing \(G\) by \(G_A\), we may and do assume that \(\nu\) is faithful. Fix \(k\) with \(\nu*k=1\) (Lemma 2.4 and
Proposition 2.5(a) give one).

*The image satisfies (1), and the map is injective.* Theorem 3.5 says that \(\Lambda_\nu\) satisfies (1). If
\(\nu'\in\mathcal E^+\), Proposition 2.6 writes \(\nu'=\nu*\lambda\) with a kernel \(\lambda\), and then
\(\Lambda(\nu')=\Lambda_\nu(\lambda(\delta^{-1}))\) by (3.1). So \(\Lambda\) is determined by \(\Lambda_\nu\).

*A key identity.* Let \(\mu\) satisfy (1) and put \(m=\mu\circ\nu\). We claim that for every kernel \(\lambda\),
\[
\mu\big(\lambda(\delta^{-1})\big)=\mu\big((\nu*\lambda)(\delta^{-1}k)\big).
\tag{3.5}
\]
Since \(\nu*k=1\), \(\lambda^y(\delta^{-1})=\int\!\int\delta(\gamma)^{-1}k(\eta^{-1}\gamma)\,d\nu^y(\eta)\,
d\lambda^y(\gamma)\). Exchanging the integrals over \(G^y\) (B1) gives \(\lambda^y(\delta^{-1})=\nu^y(\Phi)\) with
\(\Phi(\eta)=\int\delta(\gamma)^{-1}k(\eta^{-1}\gamma)\,d\lambda^{r(\eta)}(\gamma)\). Hence
\(\mu(\lambda(\delta^{-1}))=m(\Phi)\). Condition (1), applied to \(\tilde\Phi\), gives \(m(\Phi)=m(\delta^{-1}\tilde\Phi)\),
and
\[
\delta(\eta)^{-1}\tilde\Phi(\eta)=\int\delta(\eta)^{-1}\delta(\gamma)^{-1}k(\eta\gamma)\,d\lambda^{s(\eta)}(\gamma)
=\big((\delta^{-1}k)*\tilde\lambda\big)(\eta).
\]
So \(m(\Phi)=\int\nu^y((\delta^{-1}k)*\tilde\lambda)\,d\mu(y)=\int(\nu*\lambda)^y(\delta^{-1}k)\,d\mu(y)\), which is
(3.5).

*(1) implies (2).* By (3.5), \(\mu(\lambda(\delta^{-1}))\) depends only on \(\nu*\lambda\).

*(2) implies (1).* Let \(h\in\mathcal F^+(G)\) be bounded with \(\nu(\tilde h)\) bounded. The kernel \(\lambda_1=h\nu\) is
proper (Lemma 1.5(a)) and so is the diagonal kernel \(\lambda_2=\iota_{\nu(\tilde h)}\) (Lemma 1.5(c)). By
Propositions 2.5(c) and 2.5(a), \(\nu*\lambda_1=(\nu(\tilde h)\circ s)\nu\), and by Lemma 1.4(b),
\(\nu*\lambda_2=(\nu(\tilde h)\circ s)\nu\) as well; this lies in \(\mathcal E^+\). Condition (2) gives
\(\mu(\nu(\delta^{-1}h))=\mu(\lambda_1(\delta^{-1}))=\mu(\lambda_2(\delta^{-1}))=\mu(\nu(\tilde h))\), using
\(\delta=1\) on units. A general \(h\) is the increasing limit of \(h_n=\min(h,n)\widetilde{1_{A_n}}\) as in the proof of
Theorem 3.5, and monotone convergence gives (1).

*Surjectivity.* Let \(\mu\) satisfy (1) and define \(\Lambda\) by (3.4). It is additive and positively homogeneous,
and it is normal by monotone convergence, since \(\nu'_n\uparrow\nu'\) implies \(\nu_n'^y(\delta^{-1}k)\uparrow
\nu'^y(\delta^{-1}k)\). By (3.5), \(\Lambda(\nu*\lambda)=\mu(\lambda(\delta^{-1}))\) for every kernel \(\lambda\) with
\(\nu*\lambda\in\mathcal E^+\). For module \(\delta\), let \(\nu',\nu''\in\mathcal E^+\) and \(\rho\) a kernel with
\(\rho^y(G)=1\) and \(\nu''=\nu'*\delta\rho\). Write \(\nu'=\nu*\lambda'\) (Proposition 2.6). Then
\(\nu''=\nu*(\lambda'*\delta\rho)\) by Lemma 1.4(c), and
\[
(\lambda'*\delta\rho)^y(\delta^{-1})=\int\!\!\int\delta(\gamma\gamma')^{-1}\delta(\gamma')\,d\rho^{s(\gamma)}(\gamma')\,
d\lambda'^y(\gamma)=\int\delta(\gamma)^{-1}\rho^{s(\gamma)}(G)\,d\lambda'^y(\gamma)=\lambda'^y(\delta^{-1}).
\]
Hence \(\Lambda(\nu'')=\mu((\lambda'*\delta\rho)(\delta^{-1}))=\mu(\lambda'(\delta^{-1}))=\Lambda(\nu')\). Finally, for
finite \(a\), \((a\circ s)\nu=\nu*\iota_a\) and \(\iota_a(\delta^{-1})=a\), so \(\Lambda_\nu(a)=\Lambda(\nu*\iota_a)=
\mu(a)\), and \(\Lambda_\nu=\mu\). The value (3.4) does not depend on \(k\), since \(\Lambda\) is determined by
\(\Lambda_\nu=\mu\). \(\square\)

**Proposition 3.9 (\(\sigma\)-finiteness).** Let \(\Lambda\) be a transverse measure and \(\nu\in\mathcal E^+\) faithful.
The following are equivalent: (i) \(\Lambda\) is \(\sigma\)-finite; (ii) \(\Lambda_\nu\) is \(\sigma\)-finite;
(iii) \(\Lambda_{\nu'}\) is \(\sigma\)-finite for every \(\nu'\in\mathcal E^+\).

*Proof.* (iii) implies (ii) trivially. (ii) implies (i): if \(E_n\uparrow G^{(0)}\) with \(\Lambda_\nu(E_n)<\infty\),
then \(\nu_n=(1_{E_n}\circ s)\nu\uparrow\nu\) and \(\Lambda(\nu_n)=\Lambda_\nu(E_n)<\infty\). (i) implies (iii): let
\(\rho_n\uparrow\rho\) with \(\rho\) faithful and \(\Lambda(\rho_n)<\infty\), and let \(\nu'\in\mathcal E^+\). By Lemma 2.4
choose \(g>0\) with \(\nu'(g)\le1\), and put \(h=\delta g\), so that \(\nu'(\delta^{-1}h)\le1\). By (3.2), \(\Lambda_{\nu'}(\rho_n(\tilde h))=\Lambda_{\rho_n}(\nu'(\delta^{-1}h))\le
\Lambda_{\rho_n}(1)=\Lambda(\rho_n)<\infty\). Since \(\tilde h>0\) and \(\rho\) is faithful,
\(\rho_n(\tilde h)\uparrow\rho(\tilde h)>0\) everywhere; so the sets \(\{\rho_n(\tilde h)>1/j\}\), \(n,j\ge1\), have
finite \(\Lambda_{\nu'}\)-measure and cover \(G^{(0)}\). \(\square\)

**Example 3.10.**

(a) *Spaces.* On \(G=X\) every module is \(1\). With \(\nu=1\) (that is \(\nu^x=\varepsilon_x\)), \(\mu\circ\nu=\mu\) and
inversion is the identity, so condition (1) always holds. Transverse measures on \(X\) are the measures \(\mu\) on \(X\),
acting by \(\Lambda(a)=\int a\,d\mu\) on finite functions \(a\in\mathcal E^+(X)\).

(b) *Groups.* Let \(G=H\) be locally compact second countable, \(\nu=dt\) left Haar measure and \(\mu=c\,\varepsilon_e\)
with \(c\in[0,\infty]\). Then \(\mu\circ\nu=c\,dt\), and by (0.1) \(\widetilde{dt}=\Delta_H^{-1}dt\). Condition (1)
reads \(c\,\Delta_H^{-1}dt=c\,\delta^{-1}dt\). So if \(\delta=\Delta_H\), transverse measures of module \(\delta\) are
exactly the maps with \(\Lambda(dt)=c\), \(c\in[0,\infty]\). If \(\delta\ne\Delta_H\), then \(\delta\) and \(\Delta_H\)
differ on a set of positive Haar measure (the set where two homomorphisms agree is a measurable subgroup, and a
subgroup of full Haar measure is \(H\), as at the end of the proof of Remark 4.4), and only \(c=0\) and \(c=\infty\)
remain. Thus the modular function of \(H\) is
the only module of an interesting transverse measure on \(H\); a unimodular group needs \(\delta=1\). For \(\delta=
\Delta_H\) and \(c=1\), (3.4) gives \(\Lambda(\nu')=\nu'(\Delta_H^{-1}k)\) for any \(k\) with \(\int k(t^{-1})\,dt=1\).

(c) *Pair groupoid of a countable set*: see Exercise 10.1.

## 4. Reduction, transversals and group actions

**Corollary 4.1 (reduction).** Let \(\nu\in\mathcal E^+\) be faithful and \(B\in\mathcal B_0\) such that every
\(\nu^x\) is carried by \(s^{-1}(B)\). For \(y\in B\) let \(\nu_B^y\) be \(\nu^y\) regarded as a measure on \(G_B\) (it is
carried by \(G^y\cap s^{-1}(B)=G_B^y\)), and write \(\delta_B\) for the restriction of \(\delta\) to \(G_B\). Then
\(\nu_B\) is a faithful element of \(\mathcal E^+(G_B)\), and:

(a) for every transverse measure \(\Lambda\) of module \(\delta\) on \(G\) there is a unique transverse measure
\(\Lambda_B\) of module \(\delta_B\) on \(G_B\) with \((\Lambda_B)_{\nu_B}=(\Lambda_\nu)|_B\);

(b) \(\Lambda\mapsto\Lambda_B\) is a bijection between transverse measures of module \(\delta\) on \(G\) and of
module \(\delta_B\) on \(G_B\);

(c) \(\Lambda_B\) is the same for every faithful \(\nu\in\mathcal E^+\) carried by \(s^{-1}(B)\); precisely,
\((\Lambda_B)_{\nu'_B}=(\Lambda_{\nu'})|_B\) for every such \(\nu'\).

Note that \(B\) meets every orbit: each \(\nu^x\neq0\) is carried by \(G^x\cap s^{-1}(B)\), so this set is nonempty.

*Proof.* \(\nu_B\) is a transverse function on \(G_B\) (restrict (2.1) to arrows of \(G_B\)), proper with the sets
\(A_n\cap G_B\), and faithful since \(\nu_B^y=\nu^y\ne0\). By Lemma 3.3 and the hypothesis, \(\Lambda_\nu\) is carried
by \(B\): \((1_{G^{(0)}\setminus B}\circ s)\nu=0\).

For a measure \(\mu\) on \(G^{(0)}\) carried by \(B\) and \(h\in\mathcal F^+(G)\), \(\int\nu^y(h)\,d\mu(y)=
\int_B\nu_B^y(h|_{G_B})\,d\mu(y)\), since for \(y\in B\) the measure \(\nu^y\) is carried by \(G_B\). As inversion preserves
\(G_B\), \(\mu\) satisfies condition (1) of Theorem 3.8 for \((G,\nu,\delta)\) if and only if \(\mu|_B\) satisfies it
for \((G_B,\nu_B,\delta_B)\). Thus \(\mu\mapsto\mu|_B\) is a bijection between the two sets of measures described by
Theorem 3.8, and composing the bijections \(\Lambda\mapsto\Lambda_\nu\), \(\mu\mapsto\mu|_B\) and the inverse of
\(\Lambda'\mapsto\Lambda'_{\nu_B}\) gives (a) and (b).

(c) Let \(k\) with \(\nu*k=1\) on \(G\) (Corollary 3.6). For \(y\in B\), \(\nu_B^y(\tilde k|_{G_B})=\nu^y(\tilde k)=1\),
so \(k|_{G_B}\) serves for \(\nu_B\) in (3.3). Let \(a\in\mathcal F^+(B)\) and let \(\bar a\) be its extension by \(0\).
Applying (3.3) on \(G_B\), then using that \(\nu'^y\) is carried by \(G_B\) for \(y\in B\) and that \(\Lambda_\nu\) is
carried by \(B\), and then (3.3) on \(G\):
\[
(\Lambda_B)_{\nu'_B}(a)=\int_B\nu_B'^y\big(\delta_B^{-1}k\,(a\circ s)\big)\,d\Lambda_\nu(y)
=\int\nu'^y\big(\delta^{-1}k\,(\bar a\circ s)\big)\,d\Lambda_\nu(y)=\Lambda_{\nu'}(\bar a).
\]
So \(\Lambda_B\) satisfies the defining property of (a) relative to \(\nu'\), and by uniqueness the two constructions
agree. \(\square\)

**Corollary 4.2 (transversals).** Let \(T\subset G^{(0)}\) be a complete transversal and \(\nu=\nu_T\). Then
\(\Lambda\mapsto\Lambda_{\nu_T}\) is a bijection between transverse measures of module \(\delta\) on \(G\) and measures
\(\mu\) on \(T\) such that, on the discrete groupoid \(G_T\),
\[
\int_T\sum_{\gamma\in G_T^y}f(\gamma)\,d\mu(y)=\int_T\sum_{\gamma\in(G_T)_x}\delta(\gamma)f(\gamma)\,d\mu(x)
\qquad(f\in\mathcal F^+(G_T)),
\tag{4.1}
\]
that is, \(d\mu(r(\gamma))=\delta(\gamma)\,d\mu(s(\gamma))\) in the sense of counting measures along the fibres of
\(r\) and \(s\).

*Proof.* \(\nu_T\) is faithful and \(\Lambda_{\nu_T}\) is carried by \(T\) (Lemma 3.3, as \(\nu_T^y\) is carried by
\(s^{-1}(T)\)). By Theorem 3.8, the measures \(\Lambda_{\nu_T}\) are the measures \(\mu\) carried by \(T\) with
\(m(\tilde h)=m(\delta^{-1}h)\), where \(m(h)=\int\nu_T^y(h)\,d\mu(y)\). Put \(M_r(f)=\int_T\sum_{\gamma\in G_T^y}
f(\gamma)\,d\mu(y)\) and \(M_s(f)=\int_T\sum_{\gamma\in(G_T)_x}f(\gamma)\,d\mu(x)\). For \(y\in T\),
\(\nu_T^y(h)=\sum_{\gamma\in G_T^y}h(\gamma)\), so \(m(h)=M_r(h|_{G_T})\), and \(m(\tilde h)=M_s(h|_{G_T})\) because
\(\gamma\mapsto\gamma^{-1}\) maps \(G_T^y\) onto \((G_T)_y\). The condition reads \(M_s=\delta^{-1}M_r\), which is (4.1)
(replace \(f\) by \(\delta f\)). \(\square\)

For \(\delta=1\), (4.1) says that \(\mu\) is an *invariant measure* of the discrete groupoid \(G_T\): for a countable
equivalence relation it means that every partial Borel bijection whose graph lies in the relation preserves \(\mu\).
So a transverse measure of module \(1\) is the same thing as an invariant measure on a complete transversal.

**Corollary 4.3 (group actions).** Let \(G=X\rtimes H\) be the action groupoid of a measurable right action of a locally
compact second countable group \(H\) on \(X\) (Example 1.2(d)), \(\delta\) a module on \(G\), and \(\nu_H\) the
transverse function of Example 2.3(d). Then \(\Lambda\mapsto\Lambda_{\nu_H}\) is a bijection between transverse
measures of module \(\delta\) on \(G\) and measures \(\mu\) on \(X\) with
\[
\int_X\!\int_Hf(xh,h^{-1})\,dh\,d\mu(x)=\int_X\!\int_H\delta(x,h)^{-1}f(x,h)\,dh\,d\mu(x)\qquad(f\in\mathcal F^+(X\times H)).
\tag{4.2}
\]
*Proof.* Here \(\nu_H^x(f)=\int_Hf(x,h)\,dh\) and \((x,h)^{-1}=(xh,h^{-1})\), so (4.2) is condition (1) of Theorem 3.8.
\(\square\)

**Remark 4.4.** Suppose \(X\) is countably generated and \(\mu\) is \(\sigma\)-finite. For \(k\in H\) let \(\mu_k\) be the
image of \(\mu\) under \(x\mapsto xk\), and \(c_k(x)=\Delta_H(k)\,\delta(x,k)^{-1}\). Then (4.2) holds if and only if
\[
\mu_{k^{-1}}=c_k\,\mu\qquad\text{for every }k\in H.
\tag{4.3}
\]
For \(\delta=1\) and \(H\) unimodular this says that \(\mu\) is \(H\)-invariant; in general it prescribes the
Radon–Nikodym derivatives of the translates of \(\mu\).

*Proof.* Since \(\mu\) and \(dh\) are \(\sigma\)-finite, the Tonelli theorem, the substitution \(k=h^{-1}\) and (0.1) turn the
left side of (4.2) into \(\int_H\Delta_H(k)^{-1}\int_Xf(y,k)\,d\mu_{k^{-1}}(y)\,dk\), and the right side is
\(\int_H\int_X\delta(y,k)^{-1}f(y,k)\,d\mu(y)\,dk\). So (4.3) implies (4.2). Conversely assume (4.2). Choose
\(w\in\mathcal F^+(X)\), \(w>0\), with \(\mu(w)<\infty\). For \(E\) measurable and \(\varphi\in\mathcal F^+(H)\), take
\(f(y,k)=1_E(y)w(y)\delta(y,k)\varphi(k)\): we get \(\int a_E(k)\varphi(k)\,dk=\int\mu(1_Ew)\varphi(k)\,dk\), where
\(a_E(k)=\Delta_H(k)^{-1}\int1_Ew\,\delta(\cdot,k)\,d\mu_{k^{-1}}\) is measurable in \(k\). So \(a_E(k)=\mu(1_Ew)\) for
almost every \(k\). Let \(\mathcal A\) be a countable algebra generating the \(\sigma\)-algebra of \(X\). Off a Haar-null set
\(N\), the finite measures \(E\mapsto a_E(k)\) and \(E\mapsto\mu(1_Ew)\) agree on \(\mathcal A\), hence everywhere;
dividing by the positive finite function \(w\,\delta(\cdot,k)\) gives (4.3) for \(k\notin N\). Finally the set \(S\) of
\(k\) satisfying (4.3) is a subgroup. Indeed the cocycle identity \(\delta(x,k_1k_2)=\delta(x,k_1)\delta(xk_1,k_2)\)
(from \((x,k_1)(xk_1,k_2)=(x,k_1k_2)\)) gives \(c_{k_1k_2}(x)=c_{k_1}(x)c_{k_2}(xk_1)\), and the image of \(\varphi\mu\)
under \(x\mapsto xg\) is \((\varphi(\cdot\,g^{-1}))\,\mu_g\). So for \(k_1,k_2\in S\),
\(\mu_{(k_1k_2)^{-1}}=(c_{k_2}\mu)_{k_1^{-1}}=c_{k_2}(\cdot\,k_1)\,c_{k_1}\mu=c_{k_1k_2}\mu\); and for \(k\in S\),
pushing (4.3) forward by \(x\mapsto xk\) and using \(c_k(xk^{-1})\,c_{k^{-1}}(x)=c_e(x)=1\) gives \(\mu_k=c_{k^{-1}}\mu\).
A subgroup \(S\) containing a Borel set \(S_0\) of full Haar measure is \(H\): for \(g\in H\), \(gS_0\cap S_0\ne\emptyset\), so
\(g\in S_0S_0^{-1}\subset S\). \(\square\)

## 5. Negligible sets

Let \(\Lambda\) be a transverse measure of module \(\delta\).

**Definition 5.1.** A measurable saturated set \(A\subset G^{(0)}\) is *\(\Lambda\)-negligible* if \(\Lambda_\nu(A)=0\)
for every \(\nu\in\mathcal E^+\).

Only saturated sets are considered: a transverse measure does not see individual points of an orbit. The next results
show how an arbitrary set of units is measured through its saturation. For \(\nu\in\mathcal E^+\) and \(x\in G^{(0)}\),
call a measurable \(A\subset G^{(0)}\) *\(s(\nu^x)\)-negligible* if \(\nu^x(s^{-1}(A))=0\). If \(f\) is as in Lemma 2.4,
then \(f>0\) on \(G^x\) for \(x\in\operatorname{supp}\nu\), so this is the same as negligibility for the finite measure
\(s_*(f\nu^x)\), whose class therefore does not depend on \(f\). It does not change if \(x\) is replaced by an equivalent
\(y\): for \(\gamma:x\to y\), \(\nu^y(s^{-1}(A))=\nu^x(\gamma^{-1}s^{-1}(A))=\nu^x(s^{-1}(A))\) since \(s(\gamma\gamma')=
s(\gamma')\).

**Proposition 5.2.** Let \(\nu\in\mathcal E^+\) and \(B=\operatorname{supp}\nu\).

(a) If \(A\subset B\) is measurable and saturated, then \(A\) is \(\Lambda\)-negligible if and only if
\(\Lambda_\nu(A)=0\). In particular, if \(\nu\) is faithful, the \(\Lambda\)-negligible sets are the saturated
\(\Lambda_\nu\)-null sets.

(b) For measurable \(A\subset G^{(0)}\) put \([A]_\nu=\{x\in G^{(0)}:A\text{ is not }s(\nu^x)\text{-negligible}\}=
\{x:\nu^x(s^{-1}(A))>0\}\). Then \([A]_\nu\) is measurable, saturated, contained in \([A]\cap B\), and
\[
\Lambda_\nu(A)=0\iff[A]_\nu\ \text{is }\Lambda\text{-negligible}.
\]
*Proof.* (a) One direction is the definition. Suppose \(\Lambda_\nu(A)=0\) and let \(\nu'\in\mathcal E^+\). The
transverse function \((1_A\circ s)\nu'\) has support in \(A\subset B\), so by Proposition 2.6 it equals \(\nu*\lambda\)
with \(\lambda=k(1_A\circ s)\nu'\). For \(y\notin A\), \(\nu'^y\) is carried by \(G^y\subset s^{-1}(G^{(0)}\setminus A)\)
(saturation), so \(\lambda^y=0\). By (3.1), \(\Lambda_{\nu'}(A)=\Lambda_\nu(\lambda(\delta^{-1}))=
\Lambda_\nu(1_A\lambda(\delta^{-1}))=0\).

(b) The function \(x\mapsto\nu^x(s^{-1}(A))\) is measurable, and invariant along orbits by the remark before the
proposition; so \([A]_\nu\) is measurable and saturated. It lies in \(B\), and in \([A]\) because \(\nu^x\) is carried by
\(G^x\) and \(s(G^x)\subset[x]\). By (a), \([A]_\nu\) is \(\Lambda\)-negligible if and only if \(\Lambda_\nu([A]_\nu)=0\),
that is, if and only if \(m(1_A\circ s)=0\) where \(m=\Lambda_\nu\circ\nu\) (a positive function has zero integral exactly
when it vanishes almost everywhere). By Theorem 3.5 applied to \(1_A\circ r\), whose inverse is \(1_A\circ s\),
\[
m(1_A\circ s)=m\big(\delta^{-1}(1_A\circ r)\big)=\int_A\nu^y(\delta^{-1})\,d\Lambda_\nu(y).
\]
Since \(\nu^y(\delta^{-1})>0\) exactly on \(B\) and \(\Lambda_\nu\) is carried by \(B\), this vanishes if and only if
\(\Lambda_\nu(A)=0\). \(\square\)

So \(\Lambda_\nu(A)=0\) means that almost every orbit, for \(\Lambda\), meets \(A\) only in a set that is negligible for the
measures \(s(\nu^x)\) along the orbit. Two transverse measures have the same negligible sets if and only if, for one
faithful \(\nu\), the measures \(\Lambda_\nu\) and \(\Lambda'_\nu\) have the same saturated null sets.

## 6. Random variables and their integrals

A transverse measure has been defined on transverse functions. We now integrate more general objects: measurable
functors from \(G\) to measure spaces, which play the role of random variables on the "space" \(G^{(0)}/\!\sim\). A
reference for Sections 6 to 9 is [Connes 1979].

**Hypothesis (F).** From now on every measurable groupoid considered has a faithful proper transverse function:
\(\mathcal E^+(G)\) contains a faithful element. This holds for spaces, locally compact second countable groups,
discrete groupoids, action groupoids (Example 2.3(d)) and products of such. Without (F) the theory below degenerates:
for instance, the identity homomorphism of \(G\) is proper exactly when (F) holds (Example 6.9).

**Definition 6.1.** A *\(G\)-space* is a measurable space \((X,\mathcal X)\) with a measurable map \(\pi:X\to G^{(0)}\)
and a measurable map \((\gamma,z)\mapsto\gamma z\) from \(G*X=\{(\gamma,z)\in G\times X:s(\gamma)=\pi(z)\}\) (trace
\(\sigma\)-algebra) to \(X\) such that \(\pi(\gamma z)=r(\gamma)\), \(\pi(z)z=z\) and \(\gamma_1(\gamma_2z)=
(\gamma_1\gamma_2)z\). Equivalently, \(x\mapsto X^x=\pi^{-1}(x)\) and \(\gamma\mapsto(z\mapsto\gamma z)\) is a functor
from \(G\) to measurable spaces with a measurable total space. A measurable function \(\varphi\) on \(X\) is *invariant*
if \(\varphi(\gamma z)=\varphi(z)\), and a measurable set is invariant if its indicator is. An *isomorphism* of
\(G\)-spaces is a bijection \(\phi\) with \(\phi\) and \(\phi^{-1}\) measurable, \(\pi'\circ\phi=\pi\) and
\(\phi(\gamma z)=\gamma\phi(z)\).

For a measure \(m\) on \(X\) carried by \(X^x\) and \(\gamma:x\to y\), let \(\gamma m\) be its image under
\(X^x\to X^y\), \(z\mapsto\gamma z\).

**Definition 6.2.** Let \(\delta\) be a module on \(G\). A *random variable of module \(\delta\)* on \(G\) is a
\(G\)-space \(X\) with a family \(\alpha=(\alpha^x)_{x\in G^{(0)}}\) of measures on \(X\) such that

1. \(\alpha^x\) is carried by \(X^x\), and \(x\mapsto\alpha^x(E)\) is measurable for each measurable \(E\subset X\);
2. \(X\) is the union of an increasing sequence of measurable sets \(X_n\) with \(\sup_x\alpha^x(X_n)<\infty\);
3. \(\gamma\alpha^{x}=\delta(\gamma)\,\alpha^{y}\) for every \(\gamma:x\to y\).

We write \(\alpha(f)(x)=\alpha^x(f)\) for \(f\in\mathcal F^+(X)\). The *direct sum* of two random variables is the
disjoint union of the \(G\)-spaces, with the sums of the measures. The *restriction* to an invariant measurable
\(W\subset X\) is \((W,\alpha|_W)\). An *isomorphism* of random variables is an isomorphism \(\phi\) of \(G\)-spaces with
\(\phi_*\alpha^x=\alpha'^x\) for all \(x\).

In the picture of the introduction, \(\alpha^x\) is a measure on the fibre over the point \([x]\) of the quotient, and
condition 3 with \(\delta=1\) says that it depends only on \([x]\) up to the identifications \(\gamma\). A random
variable is a "generalized \([0,\infty]\)-valued function" whose values are measure spaces rather than numbers.

**Lemma 6.3.** Let \(X\) be a \(G\)-space, \(\lambda,\lambda_1,\lambda_2\) kernels on \(G\) and \(f\in\mathcal F^+(X)\).

(a) \((\lambda*f)(z)=\int f(\gamma^{-1}z)\,d\lambda^{\pi(z)}(\gamma)\) defines \(\lambda*f\in\mathcal F^+(X)\), and
\(\lambda_1*(\lambda_2*f)=(\lambda_1*\lambda_2)*f\).

(b) If \(\nu\in\bar{\mathcal E}^+\), then \(\nu*f\) is invariant, \(\nu*1=\nu(1)\circ\pi\), and
\(\nu*(\varphi f)=\varphi\,(\nu*f)\) for every invariant \(\varphi\in\mathcal F^+(X)\).

*Proof.* (a) The map \((z,\gamma)\mapsto f(\gamma^{-1}z)\) is measurable on \(\{(z,\gamma):r(\gamma)=\pi(z)\}\);
extend it by (B2) and use (B1) with the s-finite kernel \(z\mapsto\lambda^{\pi(z)}\), which is carried by the set where
the formula makes sense. Associativity is the computation of Lemma 1.4(c), with \(\gamma''^{-1}\gamma'^{-1}z\) in place of
\(\gamma''^{-1}\gamma'^{-1}\gamma\).

(b) For \(\gamma:x\to y\) and \(z\in X^x\), the substitution \(\eta=\gamma\eta'\) and (2.1) give
\((\nu*f)(\gamma z)=\int f(\eta^{-1}\gamma z)\,d\nu^y(\eta)=\int f(\eta'^{-1}z)\,d\nu^x(\eta')=(\nu*f)(z)\). The other two
statements are immediate, since \(\varphi(\eta^{-1}z)=\varphi(z)\). \(\square\)

**Example 6.4.**

(a) *The left regular random variable.* For \(\nu_0\in\mathcal E^+\), let \(L^{\nu_0}\) be the \(G\)-space \(G\), with
\(\pi=r\) and \(\gamma\cdot\gamma'=\gamma\gamma'\), and with \(\alpha^y=\delta^{-1}\nu_0^y\). Condition 3 holds: for
\(\gamma:x\to y\),
\[
\gamma(\delta^{-1}\nu_0^x)(\varphi)=\int\varphi(\gamma\gamma')\delta(\gamma')^{-1}\,d\nu_0^x(\gamma')=
\int\varphi(\eta)\delta(\gamma^{-1}\eta)^{-1}\,d\nu_0^y(\eta)=\delta(\gamma)\,(\delta^{-1}\nu_0^y)(\varphi).
\]
Condition 2 holds with \(X_n=A_n\cap\{\delta^{-1}\le n\}\). The convolution \(\nu*f\) of Lemma 6.3 is the convolution of
Lemma 1.4.

(b) *Ordinary functions.* Let \(X=G^{(0)}\), \(\pi=\mathrm{id}\), \(\gamma\cdot s(\gamma)=r(\gamma)\), and
\(\alpha^x=a(x)\varepsilon_x\) with a finite-valued \(a\in\mathcal F^+(G^{(0)})\) such that
\(a(s(\gamma))=\delta(\gamma)a(r(\gamma))\) (condition 2 holds with \(X_n=\{a\le n\}\)). For \(\delta=1\) this is an
invariant function, that is, an ordinary function on the quotient. Here \((\nu*f)(x)=\nu^x(f\circ s)\).

**Lemma 6.5 (symmetry on random variables).** Let \(\Lambda\) be a transverse measure of module \(\delta\),
\((X,\alpha)\) a random variable of module \(\delta\) and \(\nu\in\mathcal E^+\). For all \(f,g\in\mathcal F^+(X)\),
\[
\Lambda_\nu\big(\alpha(f\,(\nu*g))\big)=\Lambda_\nu\big(\alpha(g\,(\nu*f))\big).
\tag{6.1}
\]
In particular \(\Lambda_\nu\big(\nu(1)\,\alpha(f)\big)=\Lambda_\nu\big(\alpha(\nu*f)\big)\).

*Proof.* Let \(m=\Lambda_\nu\circ\nu\). Exchanging the integrals over \(\alpha^y\) and \(\nu^y\) (B1),
\[
\Lambda_\nu(\alpha(f(\nu*g)))=\int\!\!\int\!\!\int f(z)g(\gamma^{-1}z)\,d\nu^y(\gamma)\,d\alpha^y(z)\,d\Lambda_\nu(y)=m(\Psi),
\qquad \Psi(\gamma)=\int f(z)g(\gamma^{-1}z)\,d\alpha^{r(\gamma)}(z),
\]
where \(\Psi\) is measurable by (B1) and (B2). By Theorem 3.5 applied to \(\tilde\Psi\), \(m(\Psi)=m(\delta^{-1}\tilde\Psi)\).
Now \(\tilde\Psi(\gamma)=\int f(z)g(\gamma z)\,d\alpha^{s(\gamma)}(z)\), and condition 3 of Definition 6.2 turns this into
\(\delta(\gamma)\int f(\gamma^{-1}w)g(w)\,d\alpha^{r(\gamma)}(w)\). Hence
\[
m(\delta^{-1}\tilde\Psi)=\int\!\!\int\!\!\int f(\gamma^{-1}w)g(w)\,d\alpha^y(w)\,d\nu^y(\gamma)\,d\Lambda_\nu(y)
=\Lambda_\nu(\alpha(g\,(\nu*f))).
\]
For the last statement take \(g=1\) and use \(\nu*1=\nu(1)\circ\pi\). \(\square\)

**Theorem 6.6 (the integral of a random variable).** Let \(\Lambda\) be a transverse measure of module \(\delta\),
\((X,\alpha)\) a random variable of module \(\delta\), and \(\nu\in\mathcal E^+\) faithful. Put
\[
I_\nu=\sup\big\{\Lambda_\nu(\alpha(f)):\, f\in\mathcal F^+(X),\ \nu*f\le1\big\}.
\]
(a) If \(W\subset X\) is invariant and \(\nu*f=0\) on \(W\), then \(\Lambda_\nu(\alpha(f1_W))=0\).

(b) If \(f,f'\in\mathcal F^+(X)\) and \(\nu*f\le\nu*f'\le1\), then \(\Lambda_\nu(\alpha(f))\le\Lambda_\nu(\alpha(f'))\).
Hence \(\Lambda_\nu(\alpha(f))\) depends only on \(\nu*f\) when \(\nu*f\le1\), and if \(\nu*f_0=1\) then
\(I_\nu=\Lambda_\nu(\alpha(f_0))\).

(c) \(I_\nu\) does not depend on the faithful \(\nu\in\mathcal E^+\). We write it \(\int X\,d\Lambda\), or
\(\int F\,d\Lambda\) when the random variable is called \(F\).

(d) \(\int(X_1\oplus X_2)\,d\Lambda=\int X_1\,d\Lambda+\int X_2\,d\Lambda\).

(e) Suppose that \(\Lambda\) is \(\sigma\)-finite. Then \(X=X_1\sqcup X_2\) with \(X_1,X_2\) invariant and measurable,
\(\int X_1\,d\Lambda=0\), and some \(g_2\in\mathcal F^+(X)\) with \(\nu*g_2=1_{X_2}\). In particular
\(\int X\,d\Lambda=\Lambda_\nu(\alpha(g_2))\).

*Proof.* (a) By Lemma 6.3(b), \(\nu*(f1_W)=1_W(\nu*f)=0\), so by Lemma 6.5, \(\Lambda_\nu(\nu(1)\alpha(f1_W))=0\). Since
\(\nu\) is faithful, \(\nu(1)>0\) everywhere, and \(\Lambda_\nu(\alpha(f1_W))=0\).

(b) Let \(Y=\{\nu*f'>0\}\), an invariant set, and \(g=1_Y f'/(\nu*f')\). By Lemma 6.3(b), \(\nu*g=1_Y\). On
\(W=X\setminus Y\) we have \(\nu*f\le\nu*f'=0\), so \(\Lambda_\nu(\alpha(f1_W))=0\) by (a). By Lemma 6.5,
\[
\Lambda_\nu(\alpha(f))=\Lambda_\nu(\alpha(f(\nu*g)))=\Lambda_\nu(\alpha(g(\nu*f)))\le\Lambda_\nu(\alpha(g(\nu*f')))
=\Lambda_\nu(\alpha(f'(\nu*g)))\le\Lambda_\nu(\alpha(f')).
\]
(c) Let \(\nu'\in\mathcal E^+\) be faithful. Choose \(g\in\mathcal F^+(G)\) with \(\nu'*g=1\) (Lemma 2.4 and
Proposition 2.5(a)) and put \(\lambda=g\nu\); then \(\nu'*\lambda=(\nu'*g)\nu=\nu\) (Proposition 2.5(c)). Let
\(f\in\mathcal F^+(X)\) with \(\nu*f\le1\). Then \(\nu'*(\lambda*f)=\nu*f\le1\) by Lemma 6.3(a). Moreover, for
\(\gamma\in G^y\) with \(x=s(\gamma)\), condition 3 gives \(\int f(\gamma^{-1}z)\,d\alpha^y(z)=\delta(\gamma)^{-1}
\alpha^x(f)\), so
\[
\alpha^y(\lambda*f)=\int g(\gamma)\int f(\gamma^{-1}z)\,d\alpha^y(z)\,d\nu^y(\gamma)=\nu^y\big(\delta^{-1}h\big),\qquad
h=g\,(\alpha(f)\circ s).
\]
By (3.2) with the roles of \(\nu,\nu'\) exchanged, \(\Lambda_{\nu'}(\nu(\delta^{-1}h))=\Lambda_\nu(\nu'(\tilde h))\), and
\(\nu'^y(\tilde h)=\alpha^y(f)\,\nu'^y(\tilde g)=\alpha^y(f)\). Hence \(\Lambda_{\nu'}(\alpha(\lambda*f))=
\Lambda_\nu(\alpha(f))\), and \(I_{\nu'}\ge I_\nu\). By symmetry the two are equal.

(d) A function \(f\) on \(X_1\sqcup X_2\) satisfies \(\nu*f\le1\) if and only if both restrictions do, and
\(\Lambda_\nu(\alpha(f))\) splits into the two contributions.

(e) By Proposition 3.9, \(\Lambda_\nu\) is \(\sigma\)-finite; with condition 2 of Definition 6.2, the measure
\(\kappa=\Lambda_\nu\circ\alpha\) on \(X\) is \(\sigma\)-finite. Let \(\kappa'\) be a finite measure with the same null sets
(if \(\kappa\ne0\), \(\kappa'=w\kappa\) with \(w>0\) and \(\kappa(w)<\infty\); if \(\kappa=0\) there is nothing to prove).
Let \(\mathcal Y\) be the family of invariant measurable \(Y\subset X\) with \(1_Y=\nu*g_Y\) for some \(g_Y\in\mathcal
F^+(X)\). It is stable under countable unions: if \(Y_n\in\mathcal Y\), put \(Y'_n=Y_n\setminus\bigcup_{m<n}Y_m\) and
\(g=\sum_ng_{Y_n}1_{Y'_n}\); then \(\nu*g=\sum_n1_{Y'_n}=1_{\bigcup Y_n}\) by Lemma 6.3(b). Choose \(Y_n\in\mathcal Y\)
with \(\kappa'(Y_n)\to\sup_{Y\in\mathcal Y}\kappa'(Y)\), and let \(X_2=\bigcup_nY_n\in\mathcal Y\) and \(X_1=X\setminus
X_2\). Then \(\kappa'(Y\setminus X_2)=0\) for all \(Y\in\mathcal Y\). Let \(f\) be supported in \(X_1\) with
\(\nu*f\le1\), and \(Y=\{\nu*f>0\}\); as in (b), \(Y\in\mathcal Y\). The part of \(f\) on \(Y\) lies in
\(Y\setminus X_2\), a \(\kappa\)-null set, and contributes \(\kappa(f1_{Y\setminus X_2})=0\); the part on \(X\setminus Y\)
contributes \(0\) by (a). So \(\int X_1\,d\Lambda=0\), and the last statement follows from (b) and (d). \(\square\)

**Lemma 6.7 (proper \(G\)-spaces).** For a \(G\)-space \(X\) the following are equivalent.

(a) There are \(\nu\in\mathcal E^+\) and \(f\in\mathcal F^+(X)\) with \(\nu*f=1\).

(b) For every faithful \(\nu\in\mathcal E^+\) there is \(f\in\mathcal F^+(X)\) with \(\nu*f=1\).

(b') For every faithful \(\nu\in\mathcal E^+\) there is \(f\in\mathcal F^+(X)\) with \(f>0\) everywhere and
\(\nu*f=1\).

(c) For some faithful \(\nu\in\mathcal E^+\), the kernel \(z\mapsto\rho^z\), \(\rho^z(\varphi)=(\nu*\varphi)(z)\), from
\(X\) to \(X\) is proper: \(X=\bigcup_nX_n\) with \(X_n\) measurable, increasing, and \(\sup_z(\nu*1_{X_n})(z)<\infty\).

(c') The same holds for every faithful \(\nu\in\mathcal E^+\).

*Proof.* (a) implies (b): if \(\nu_0*f_0=1\) and \(\nu\) is faithful, write \(\nu_0=\nu*\lambda\) (Proposition 2.6);
then \(\nu*(\lambda*f_0)=\nu_0*f_0=1\) by Lemma 6.3(a).

(b) implies (b'): choose \(k\in\mathcal F^+(G)\) with \(k>0\) and \(\nu*k=1\) (Lemma 2.4 gives \(\tilde k>0\) on \(G_A=G\)),
and put \(f_1(z)=\int f(\gamma^{-1}z)k(\gamma)\,d\nu^{\pi(z)}(\gamma)\). Since \(\int f(\gamma^{-1}z)\,d\nu^{\pi(z)}
(\gamma)=1\), the integrand \(f(\gamma^{-1}z)\) is positive on a set of positive \(\nu^{\pi(z)}\)-measure, and \(k>0\), so
\(f_1(z)>0\). With \(y=\pi(z)\), the substitution \(\eta=\gamma'\gamma\) and (2.1) give
\(f_1(\gamma'^{-1}z)=\int f(\eta^{-1}z)k(\gamma'^{-1}\eta)\,d\nu^y(\eta)\) for \(\gamma'\in G^y\), hence
\[
(\nu*f_1)(z)=\int\!\!\int f(\eta^{-1}z)k(\gamma'^{-1}\eta)\,d\nu^y(\eta)\,d\nu^y(\gamma')
=\int f(\eta^{-1}z)(\nu*k)(\eta)\,d\nu^y(\eta)=(\nu*f)(z)=1 .
\]
(b') implies (c'): take \(X_n=\{f\ge1/n\}\); then \(\nu*1_{X_n}\le n\,\nu*f=n\). (c') implies (c) trivially.

(c) implies (a): with \(\nu*1_{X_n}\le c_n\), \(c_n\ge1\), put \(f_2=\sum_n2^{-n}c_n^{-1}1_{X_n}\). Then \(f_2>0\),
\(\nu*f_2\le1\), and \(\nu*f_2>0\) because \(\nu^{\pi(z)}\ne0\). The function \(f=f_2/(\nu*f_2)\) satisfies \(\nu*f=1\) by
Lemma 6.3(b). \(\square\)

**Definition 6.8.** A \(G\)-space is *proper* (one also says that the action of \(G\) on it is proper) if it satisfies
the conditions of Lemma 6.7. A random variable is proper if its \(G\)-space is.

By Theorem 6.6(b), for a proper random variable \(\int X\,d\Lambda=\Lambda_\nu(\alpha(f))\) for any \(f\) with
\(\nu*f=1\). Theorem 6.6(e) says that, for \(\sigma\)-finite \(\Lambda\), every random variable is the sum of a proper one
and one of integral zero; so for integration purposes proper random variables suffice. Example 6.13 shows that
\(\sigma\)-finiteness cannot be weakened to semi-finiteness here.

**Example 6.9.** The \(G\)-space of Example 6.4(a), \(G\) acting on itself by left translation, is proper: with \(\nu\)
faithful and \(k\) as in Corollary 3.6, \(\nu*k=1\). Conversely, a function \(f\) on \(G\) with \(\nu*f=1\) forces
\(\nu^{y}\ne0\) for all \(y\); so this \(G\)-space is proper if and only if Hypothesis (F) holds.

In Example 6.4(b), with \(G\) the equivalence relation of an ergodic transformation, the \(G\)-space \(G^{(0)}\) is in
general not proper; Exercise 10.3 shows that the constant function \(1\) then has integral \(0\), in accordance with the
introduction.

**Proposition 6.10 (equivariant Markov maps).** Let \(X,X'\) be \(G\)-spaces and \(z\mapsto\lambda^z\) a kernel from
\(X\) to \(X'\) of probability measures, with \(\lambda^z\) carried by \(X'^{\pi(z)}\) and \(\lambda^{\gamma z}=
\gamma\lambda^z\) whenever \(s(\gamma)=\pi(z)\).

(a) If \(X'\) is proper, so is \(X\).

(b) Let \((X,\alpha)\) and \((X',\alpha')\) be random variables of module \(\delta\) with \(\alpha'^x=\int\lambda^z\,
d\alpha^x(z)\) for all \(x\). Then \(\int X'\,d\Lambda\le\int X\,d\Lambda\), with equality if \(X'\) is proper.

(c) Isomorphic random variables have the same integral, and a \(G\)-space isomorphic to a proper one is proper.

*Proof.* For \(f\in\mathcal F^+(X')\) put \((Pf)(z)=\lambda^z(f)\), a measurable function on \(X\). For \(y=\pi(z)\),
\[
(\nu*Pf)(z)=\int\lambda^{\gamma^{-1}z}(f)\,d\nu^y(\gamma)=\int\!\!\int f(\gamma^{-1}z')\,d\lambda^z(z')\,d\nu^y(\gamma)
=\big(P(\nu*f)\big)(z),
\]
exchanging the integrals by (B1). (a) If \(\nu*f=1\) then \(\nu*Pf=P1=1\). (b) \(\alpha'(f)=\alpha(Pf)\), and \(\nu*f\le1\)
implies \(\nu*Pf\le1\); so every value in the supremum defining \(\int X'\,d\Lambda\) is a value for \(\int X\,d\Lambda\). If
\(X'\) is proper and \(\nu*f_0=1\), then \(\nu*Pf_0=1\) and Theorem 6.6(b) gives \(\int X'\,d\Lambda=
\Lambda_\nu(\alpha'(f_0))=\Lambda_\nu(\alpha(Pf_0))=\int X\,d\Lambda\). (c) Apply (a) and (b) to \(\lambda^z=
\varepsilon_{\phi(z)}\) and to \(\lambda'^{z'}=\varepsilon_{\phi^{-1}(z')}\). \(\square\)

**Lemma 6.11 (random variables of integral zero).** Let \((X,\alpha)\) be a random variable of module \(\delta\) and
\(S=\{x:\alpha^x\ne0\}\). Then \(S\) is measurable and saturated, and if \(S\) is \(\Lambda\)-negligible then
\(\int X\,d\Lambda=0\). If \(X\) is proper, \(\int X\,d\Lambda=0\) if and only if \(S\) is \(\Lambda\)-negligible.

*Proof.* \(S=\{x:\alpha^x(X)>0\}\) is measurable, and saturation follows from \(\gamma\alpha^x=\delta(\gamma)\alpha^y\). If \(\Lambda_\nu(S)=0\), then
\(\Lambda_\nu(\alpha(f))=\int_S\alpha^x(f)\,d\Lambda_\nu(x)=0\) for all \(f\). If \(X\) is proper, choose \(f_1>0\) with
\(\nu*f_1=1\) (Lemma 6.7(b')). Then \(S=\{\alpha(f_1)>0\}\), and \(\int X\,d\Lambda=\Lambda_\nu(\alpha(f_1))\)
vanishes if and only if \(\Lambda_\nu(S)=0\), that is (Proposition 5.2(a), \(\nu\) faithful) if and only if \(S\) is
\(\Lambda\)-negligible. \(\square\)

**Proposition 6.12.** For every \(\nu_0\in\mathcal E^+\), \(\int L^{\nu_0}\,d\Lambda=\Lambda(\nu_0)\).

*Proof.* Let \(\nu\) be faithful and \(k\) with \(\nu*k=1\) on \(G\) (Corollary 3.6), so \(\nu(\tilde k)=1\). The random
variable \(L^{\nu_0}\) is proper (Example 6.9), so by Theorem 6.6(b) and then (3.2),
\[
\int L^{\nu_0}\,d\Lambda=\Lambda_\nu\big(\nu_0(\delta^{-1}k)\big)=\Lambda_{\nu_0}\big(\nu(\tilde k)\big)=
\Lambda_{\nu_0}(1)=\Lambda(\nu_0).\qquad\square
\]

**Example 6.13 (semi-finiteness does not suffice in Theorem 6.6(e)).** Let \(Z=\{0,1\}^{\mathbb N}\) with its Borel
sets, and let \(x\sim y\) mean that \(x\) and \(y\) differ in finitely many coordinates. The classes are the orbits of
the countable group \(\Gamma=\bigoplus_{\mathbb N}\mathbb Z/2\), acting freely by changing finitely many coordinates, so
this is a countable Borel equivalence relation; let \(G\) be its groupoid, which is discrete (Example 2.9(b)), and
\(\nu\) its counting transverse function, which is faithful. Counting measure \(\mu\) on \(Z\) satisfies (4.1) with
\(T=Z\) and \(\delta=1\), since both sides equal \(\sum_{\gamma\in G}f(\gamma)\). By Corollary 4.2 there is a transverse
measure \(\Lambda\) of module \(1\) with \(\Lambda_\nu=\mu\).

*\(\Lambda\) is semi-finite.* The function \(k=1_{G^{(0)}}\) satisfies \(\nu(\tilde k)=1\), so by (3.4)
\(\Lambda(\nu')=\sum_{y\in Z}c(y)\) with \(c(y)=\nu'^y(\{y\})\), and likewise
\(\Lambda((1_E\circ s)\nu')=\sum_{y\in E}c(y)\). Each \(c(y)\) is finite by Lemma 2.2(b), since the unit \(y\) lies in
one of the sets \(A_n\) there. The transverse functions \((1_E\circ s)\nu'\le\nu'\) with \(E\) finite lie in
\(\mathcal E^+\) (Lemma 2.2(d)) and have finite values whose supremum is \(\Lambda(\nu')\). (\(\Lambda\) is not
\(\sigma\)-finite, by Proposition 3.9.)

*The random variable.* Let \(X=Z\times[0,1]\), \(\pi(x,u)=x\), \(\gamma\cdot(s(\gamma),u)=(r(\gamma),u)\) and
\(\alpha^x=\varepsilon_x\otimes du\). This is a random variable of module \(1\) with atomless fibres: \(\alpha^x(E)\) is
the Lebesgue measure of the section \(\{u:(x,u)\in E\}\), a Borel function of \(x\) by the Fubini theorem;
\(\alpha^x(X)=1\), so condition 2 of Definition 6.2 holds with \(X_n=X\); and \(\gamma\alpha^x=\alpha^y\) for
\(\gamma:x\to y\). Moreover \((\nu*f)(x,u)=\sum_{y\sim x}f(y,u)\) and \(\Lambda_\nu(\alpha(f))=\sum_{x\in Z}\int_0^1
f(x,u)\,du\).

*No decomposition as in Theorem 6.6(e) exists.* It suffices to treat the counting transverse function \(\nu\): by
Theorem 6.6(c) the integral of \(X_1\) does not depend on the faithful transverse function, and by Lemma 6.7, applied
to the \(G\)-space \(X_2\), neither does the existence of \(g_2\). Suppose \(X=X_1\sqcup X_2\) with \(X_1,X_2\)
invariant and measurable, \(\nu*g_2=1_{X_2}\) and \(\int X_1\,d\Lambda=0\). For \(x\in Z\) let \(U_x=\{u:(x,u)\in X_1\}\). By invariance
\(X_1\cap([x]\times[0,1])=[x]\times U_x\), so \(f=1_{\{x\}\times U_x}\) is supported in \(X_1\), has
\(\nu*f=1_{[x]\times U_x}\le1\), and gives \(\Lambda_\nu(\alpha(f))=|U_x|\), the Lebesgue measure of \(U_x\). Hence
\(|U_x|=0\) for every \(x\). Let \(m_0\) be the product of the measures \(\frac12(\varepsilon_0+\varepsilon_1)\) on
\(Z\), a probability measure preserved by \(\Gamma\). By the Fubini theorem, \((m_0\otimes du)(X_2)=\int(1-|U_x|)\,dm_0(x)=1\), so for some \(u\) the Borel set
\(Z_u=\{x:(x,u)\in X_2\}\) has \(m_0(Z_u)>0\). It is \(\Gamma\)-invariant, and \(\varphi=g_2(\cdot,u)\) satisfies
\(\sum_{g\in\Gamma}\varphi(gx)=1\) for \(x\in Z_u\). Integrating over \(Z_u\) and using the invariance of \(m_0\) and
\(Z_u\),
\[
m_0(Z_u)=\sum_{g\in\Gamma}\int_{Z_u}\varphi(gx)\,dm_0(x)=\sum_{g\in\Gamma}\int_{Z_u}\varphi\,dm_0 ,
\]
an infinite sum of equal terms, which is \(0\) or \(\infty\). This contradicts \(0<m_0(Z_u)\le1\).

The proof of Theorem 6.6(e) used only that the measure \(\Lambda_\nu\circ\alpha\) on \(X\) is \(\sigma\)-finite; here it
is \(\mu\otimes du\), which is not.

*Reference:* Part 2 of [Connes 1979, Section III, Lemma 1] states the decomposition of Theorem 6.6(e) for
semi-finite transverse measures; this example shows that it fails for them, so we prove it for \(\sigma\)-finite ones.

## 7. Proper homomorphisms

**Definition 7.1.** Let \(h:G\to G'\) be a measurable homomorphism.

(a) For a \(G'\)-space \(X'\) (with map \(\pi'\)), the *pull-back* \(h^*X'\) is the \(G\)-space
\(\{(x,z')\in G^{(0)}\times X':\pi'(z')=h(x)\}\) (trace \(\sigma\)-algebra) with \(\pi(x,z')=x\) and
\(\gamma(x,z')=(r(\gamma),h(\gamma)z')\) for \(\gamma:x\to y\). If \((X',\alpha')\) is a random variable of module
\(\delta'\) on \(G'\), then \(h^*X'\) with the measures \(\alpha^x\) equal to \(\alpha'^{h(x)}\) placed on
\(\{x\}\times X'^{h(x)}\) is a random variable of module \(\delta'\circ h\) on \(G\), written \(h^*(X',\alpha')\).

(b) The *\(G\)-space of \(h\)* is \(X_h=h^*G'=\{(x,\gamma')\in G^{(0)}\times G':r(\gamma')=h(x)\}\), the pull-back of
\(G'\) acting on itself by left translation: \(\gamma(x,\gamma')=(r(\gamma),h(\gamma)\gamma')\). We say that \(h\) is
*proper* if \(X_h\) is a proper \(G\)-space.

(c) Two measurable homomorphisms \(h,h':G\to G'\) are *similar*, \(h'\sim h\), if there is a measurable
\(\theta:G^{(0)}\to G'\) with \(\theta(x):h(x)\to h'(x)\) for all \(x\) and \(\theta(y)h(\gamma)=h'(\gamma)\theta(x)\) for
every \(\gamma:x\to y\). We then write \(h'=h^\theta\). A measurable homomorphism \(h:G\to G'\) is an *equivalence* if
there is a measurable homomorphism \(h':G'\to G\) with \(h'\circ h\sim\mathrm{id}_G\) and \(h\circ h'\sim\mathrm{id}_{G'}\).

The measurability and module claims in (a) are routine: the action is measurable because the product of \(G'\) and the
action on \(X'\) are, and condition 3 of Definition 6.2 for \(h^*X'\) is condition 3 for \(X'\) applied to \(h(\gamma)\).

**Example 7.2 (groups).** Let \(h:H\to H'\) be a continuous homomorphism of locally compact second countable groups
such that \(h^{-1}(C)\) is compact for every compact \(C\subset H'\). Then \(h\) is proper. Indeed \(X_h\cong H'\) with \(t\cdot g=h(t)g\). Take \(\nu=dt\) and
compact sets \(K_n\uparrow H'\). If \(\{t:h(t)^{-1}g\in K_n\}\) contains \(t_0\), then for every \(t\) in it
\(h(t_0^{-1}t)=h(t_0)^{-1}g\,(h(t)^{-1}g)^{-1}\in K_nK_n^{-1}\); so this set lies in \(t_0h^{-1}(K_nK_n^{-1})\), and
\((\nu*1_{K_n})(g)\le\int1_{h^{-1}(K_nK_n^{-1})}\,dt<\infty\). Lemma 6.7(c) applies. In particular the inclusion of a
closed subgroup is proper. By Exercise 10.2, the homomorphism \(H\to\{e\}\) is proper only when \(H\) is compact.

**Lemma 7.3 (pull-backs of proper spaces).** If \(h:G\to G'\) is proper and \(X'\) is a proper \(G'\)-space, then
\(h^*X'\) is a proper \(G\)-space. More precisely, let \(\nu\in\mathcal E^+(G)\) be faithful and \(g\in\mathcal
F^+(X_h)\) with \(\nu*g=1\), and let \(\nu'\in\mathcal E^+(G')\) and \(f\in\mathcal F^+(X')\) with \(\nu'*f=1\). Then
\[
k(x,z')=\int f(\gamma'^{-1}z')\,g(x,\gamma')\,d\nu'^{h(x)}(\gamma')
\tag{7.1}
\]
defines \(k\in\mathcal F^+(h^*X')\) with \(\nu*k=1\).

*Proof.* Measurability follows from (B1) and (B2). Let \(\gamma_1:x_1\to x\). Then
\(\gamma_1^{-1}(x,z')=(x_1,h(\gamma_1)^{-1}z')\), and the substitution \(\eta=h(\gamma_1)\gamma'\) (the translation by
\(h(\gamma_1):h(x_1)\to h(x)\) carries \(\nu'^{h(x_1)}\) to \(\nu'^{h(x)}\)) gives
\[
k(\gamma_1^{-1}(x,z'))=\int f(\eta^{-1}z')\,g(x_1,h(\gamma_1)^{-1}\eta)\,d\nu'^{h(x)}(\eta).
\]
Integrating over \(\gamma_1\) with respect to \(\nu^x\) and exchanging the integrals,
\((\nu*k)(x,z')=\int f(\eta^{-1}z')\,(\nu*g)(x,\eta)\,d\nu'^{h(x)}(\eta)=(\nu'*f)(z')=1\). \(\square\)

**Proposition 7.4.** Let \(h:G\to G'\), \(h':G'\to G''\) be measurable homomorphisms.

(a) If \(h\) is proper and \(h'\sim h\) (with \(h,h':G\to G'\)), then \(h'\) is proper.

(b) If \(h\) and \(h'\) are proper, so is \(h'\circ h\).

(c) If \(h'\circ h\) is proper, so is \(h\).

*Proof.* (a) Let \(h'=h^\theta\). The map \(\phi(x,\gamma')=(x,\theta(x)\gamma')\) from \(X_h\) to \(X_{h'}\) is measurable,
bijective with inverse \((x,\gamma')\mapsto(x,\theta(x)^{-1}\gamma')\), and equivariant:
\(\phi(\gamma(x,\gamma'))=(y,\theta(y)h(\gamma)\gamma')=(y,h'(\gamma)\theta(x)\gamma')=\gamma\phi(x,\gamma')\). Apply
Proposition 6.10(c).

(b) The map \((x,\gamma'')\mapsto(x,(h(x),\gamma''))\) is an isomorphism of \(X_{h'\circ h}\) onto \(h^*(X_{h'})\), and
Lemma 7.3 applies.

(c) The map \(\Psi(x,\gamma')=(x,h'(\gamma'))\) from \(X_h\) to \(X_{h'\circ h}\) is equivariant, since
\(\Psi(\gamma(x,\gamma'))=(y,h'(h(\gamma))h'(\gamma'))=\gamma\Psi(x,\gamma')\). Apply Proposition 6.10(a) with
\(\lambda^z=\varepsilon_{\Psi(z)}\). \(\square\)

**Corollary 7.5.** An equivalence \(h:G\to G'\) is proper, and so is any \(h'\) as in Definition 7.1(c).

*Proof.* \(\mathrm{id}_G\) is proper: \(X_{\mathrm{id}}\) is the \(G\)-space of Example 6.9, and (F) holds. Since
\(h'\circ h\sim\mathrm{id}_G\), \(h'\circ h\) is proper by Proposition 7.4(a), hence \(h\) is proper by Proposition
7.4(c). The same argument with \(G'\) gives \(h'\). \(\square\)

**Example 7.6.**

(a) *Subgroupoids of a discrete groupoid.* Let \(G\) be discrete and \(G_1\in\mathcal B\) a subgroupoid (stable under
products and inverses). Then \(G_1\) is discrete and the inclusion \(i:G_1\to G\) is proper. Let \(C_n\uparrow G\) with
\(\#(C_n\cap G^y)\le c_n\), and \(D_n=C_n\cap\tilde C_n\); then \(D_n\uparrow G\), \(D_n=\tilde D_n\), and both
\(\#(D_n\cap G^y)\) and \(\#(D_n\cap G_x)=\#(D_n\cap G^x)\) are at most \(c_n\). The counting measures on
\(G_1^y=G^y\cap G_1\) are measurable in \(y\) (they are \(\nu_{G^{(0)}}^y(\cdot\cap G_1)\)) and proper with the sets
\(D_n\cap G_1\). In \(X_i=\{(x,\gamma):x\in G_1^{(0)},\gamma\in G^x\}\) put \(A_n=\{(x,\gamma):\gamma\in D_n\}\). With \(\nu\)
the counting transverse function of \(G_1\), \((\nu*1_{A_n})(x,\gamma)=\#\{\gamma_1\in G_1^x:\gamma_1^{-1}\gamma\in D_n\}\le
\#(D_n\cap G_{s(\gamma)})\le c_n\), because \(\gamma_1\mapsto\gamma_1^{-1}\gamma\) is injective with values in
\(G_{s(\gamma)}\). Lemma 6.7(c) applies.

(b) *Projection of an action groupoid.* Let \(p:X\rtimes H\to H\), \(p(x,h)=h\). Here \(X_p=X\times H\) with
\((x,h)\cdot(xh,k)=(x,hk)\). Choose \(\beta\in\mathcal F^+(H)\) with \(\int\beta(u)\Delta_H(u)^{-1}\,du=1\), and put
\(g(x,k)=\beta(k)\). Using (0.1) twice,
\[
(\nu_H*g)(x,k)=\int_H\beta(h^{-1}k)\,dh=\int_H\beta(hk)\Delta_H(h)^{-1}\,dh=\int_H\beta(u)\Delta_H(u)^{-1}\,du=1 .
\]
So \(p\) is proper.

## 8. The image of a transverse measure

Let \(h:G\to G'\) be a proper homomorphism, \(\delta'\) a module on \(G'\), and \(\delta=\delta'\circ h\). For
\(\nu'\in\mathcal E^+(G')\), the left regular random variable \(L^{\nu'}\) of module \(\delta'\) on \(G'\) (Example
6.4(a)) pulls back to the random variable \(h^*L^{\nu'}\) of module \(\delta\) on \(G\): its \(G\)-space is \(X_h\), and
its measure over \(x\) is \(\delta'^{-1}\nu'^{h(x)}\) placed on \(\{x\}\times G'^{h(x)}\).

**Definition 8.1.** For a transverse measure \(\Lambda\) of module \(\delta=\delta'\circ h\) on \(G\), the *image*
\(h(\Lambda)\) is the map \(\mathcal E^+(G')\to[0,\infty]\) given by
\[
h(\Lambda)(\nu')=\int h^*L^{\nu'}\,d\Lambda .
\]
**Theorem 8.2.** Let \(h:G\to G'\) be proper, \(\delta'\) a module on \(G'\) and \(\Lambda\) a transverse measure of module
\(\delta'\circ h\) on \(G\).

(a) \(h(\Lambda)\) is a transverse measure of module \(\delta'\) on \(G'\). If \(\nu\in\mathcal E^+(G)\) is faithful and
\(g\in\mathcal F^+(X_h)\) satisfies \(\nu*g=1\), then
\[
h(\Lambda)(\nu')=\int\!\!\int g(x,\gamma')\,\delta'(\gamma')^{-1}\,d\nu'^{h(x)}(\gamma')\,d\Lambda_\nu(x).
\tag{8.1}
\]
(b) If \(h'=h^\theta\) with \(\delta'\circ\theta=1\), then \(\delta'\circ h'=\delta'\circ h\), \(h'\) is proper, and
\(h'(\Lambda)=h(\Lambda)\).

(c) For every proper random variable \(X'\) of module \(\delta'\) on \(G'\),
\(\int h^*X'\,d\Lambda=\int X'\,d\big(h(\Lambda)\big)\).

(d) \(h(\Lambda)=0\) if and only if \(\Lambda=0\).

*Proof.* (a) The random variable \(h^*L^{\nu'}\) is proper, since its \(G\)-space is \(X_h\); so Theorem 6.6(b) gives
(8.1). From (8.1), \(h(\Lambda)\) is additive, positively homogeneous and, by monotone convergence, normal. For the
module, let \(\nu',\nu''\in\mathcal E^+(G')\) and \(\rho\) a kernel on \(G'\) with \(\rho^{x'}(G')=1\) and
\(\nu''=\nu'*\delta'\rho\). For \(z=(x,\gamma')\in X_h\) let \(\lambda^z\) be the image of \(\rho^{s(\gamma')}\) under
\(\eta\mapsto(x,\gamma'\eta)\). This is a kernel of probability measures from \(X_h\) to \(X_h\), carried by the fibre over
\(x\), and equivariant: \(\lambda^{\gamma z}\), for \(\gamma z=(y,h(\gamma)\gamma')\), is the image of
\(\rho^{s(\gamma')}\) under \(\eta\mapsto(y,h(\gamma)\gamma'\eta)\), which is \(\gamma\lambda^z\). For
\(\varphi\in\mathcal F^+(X_h)\),
\[
\int\lambda^z(\varphi)\,d\alpha'^x(z)=\int\!\!\int\varphi(x,\gamma'\eta)\,d\rho^{s(\gamma')}(\eta)\,
\delta'(\gamma')^{-1}\,d\nu'^{h(x)}(\gamma')=\int\varphi(x,\zeta)\,\delta'(\zeta)^{-1}\,d\nu''^{h(x)}(\zeta),
\]
where \(\alpha'\) is the measure of \(h^*L^{\nu'}\): indeed, by definition of \(\nu''=\nu'*\delta'\rho\), the right side is
\(\int\!\int\varphi(x,\gamma'\eta)\delta'(\gamma'\eta)^{-1}\delta'(\eta)\,d\rho^{s(\gamma')}(\eta)\,d\nu'^{h(x)}(\gamma')\).
So the measure of \(h^*L^{\nu''}\) is \(\int\lambda^z\,d\alpha'^x(z)\), and Proposition 6.10(b) (both random variables live
on the proper \(G\)-space \(X_h\)) gives \(h(\Lambda)(\nu'')=h(\Lambda)(\nu')\).

(b) For \(\gamma:x\to y\), \(\delta'(h'(\gamma))=\delta'(\theta(y)h(\gamma)\theta(x)^{-1})=\delta'(h(\gamma))\), and \(h'\) is
proper by Proposition 7.4(a). The isomorphism \(\phi(x,\gamma')=(x,\theta(x)\gamma')\) of \(X_h\) onto \(X_{h'}\) carries
\(\delta'^{-1}\nu'^{h(x)}\) to \(\delta'(\theta(x))\,\delta'^{-1}\nu'^{h'(x)}=\delta'^{-1}\nu'^{h'(x)}\) (the computation of
Example 6.4(a) with \(\gamma=\theta(x)\)). So \(h^*L^{\nu'}\) and \(h'^*L^{\nu'}\) are isomorphic random variables and
Proposition 6.10(c) applies.

(c) Let \(\nu'\in\mathcal E^+(G')\) be faithful and \(f\in\mathcal F^+(X')\) with \(\nu'*f=1\) (Lemma 6.7(b)). With
\(\nu,g\) as in (a), define \(k\) by (7.1); then \(\nu*k=1\) on \(h^*X'\) (Lemma 7.3) and
\(\int h^*X'\,d\Lambda=\Lambda_\nu(\alpha(k))\), where \(\alpha^x=\alpha'^{h(x)}\). By condition 3 of Definition 6.2 for
\(X'\), \(\int f(\gamma'^{-1}z')\,d\alpha'^{h(x)}(z')=\delta'(\gamma')^{-1}\alpha'(f)(s(\gamma'))\) for \(\gamma'\in
G'^{h(x)}\), so
\[
\alpha^x(k)=\int g(x,\gamma')\,\delta'(\gamma')^{-1}\,\alpha'(f)(s(\gamma'))\,d\nu'^{h(x)}(\gamma').
\]
Suppose first that \(\alpha'(f)\) is finite-valued. Then \(\nu''=(\alpha'(f)\circ s)\nu'\in\mathcal E^+(G')\), and by
(8.1) and Lemma 3.3, \(\Lambda_\nu(\alpha(k))=h(\Lambda)(\nu'')=h(\Lambda)_{\nu'}(\alpha'(f))\), which is
\(\int X'\,d(h(\Lambda))\) by Theorem 6.6(b). In general, with \(X'_n\) as in condition 2 of Definition 6.2, the
functions \(f_n=\min(f,n)1_{X'_n}\) increase to \(f\) and have \(\alpha'(f_n)\le n\sup_x\alpha'^x(X'_n)\); the
corresponding \(k_n\) increase to \(k\), and the identity \(\Lambda_\nu(\alpha(k_n))=h(\Lambda)_{\nu'}(\alpha'(f_n))\) passes
to the limit by monotone convergence.

(d) If \(\Lambda=0\) all integrals vanish. Conversely let \(\nu'\in\mathcal E^+(G')\) be faithful. If
\(h(\Lambda)(\nu')=\int h^*L^{\nu'}\,d\Lambda=0\), Lemma 6.11 says that \(\{x:\delta'^{-1}\nu'^{h(x)}\ne0\}=G^{(0)}\) is
\(\Lambda\)-negligible; so \(\Lambda(\nu)=\Lambda_\nu(1)=0\) for all \(\nu\in\mathcal E^+(G)\). \(\square\)

For an isomorphism \(k:G\to K\) of measurable groupoids (a bijective measurable homomorphism with measurable inverse)
and \(\nu\in\mathcal E^+(G)\), let \(k_*\nu\in\mathcal E^+(K)\) be given by \((k_*\nu)^{k(y)}=k_*(\nu^y)\).

**Corollary 8.3.**

(a) \(\mathrm{id}_G(\Lambda)=\Lambda\).

(b) (*Functoriality.*) Let \(h:G\to G'\) and \(h':G'\to G''\) be proper, \(\delta''\) a module on \(G''\), and
\(\Lambda\) a transverse measure of module \(\delta''\circ h'\circ h\) on \(G\). Then \((h'\circ h)(\Lambda)=
h'\big(h(\Lambda)\big)\).

(c) (*Isomorphisms.*) If \(k:G\to K\) is an isomorphism and \(\delta\) is a module on \(K\), then \(k\) is proper and, for a
transverse measure \(\Lambda\) of module \(\delta\circ k\) on \(G\), \(k(\Lambda)(k_*\nu)=\Lambda(\nu)\) for all
\(\nu\in\mathcal E^+(G)\). Consequently \(k(\Lambda)_{k_*\nu}(a)=\Lambda_\nu(a\circ k)\) for \(a\in\mathcal
F^+(K^{(0)})\).

*Proof.* (a) The map \((x,\gamma)\mapsto\gamma\) is an isomorphism of \(\mathrm{id}_G^*L^{\nu_0}\) onto \(L^{\nu_0}\);
apply Proposition 6.10(c) and Proposition 6.12.

(b) The isomorphism \(X_{h'\circ h}\cong h^*(X_{h'})\) of Proposition 7.4(b) carries the measures of
\((h'\circ h)^*L^{\nu''}\) to those of \(h^*(h'^*L^{\nu''})\), both being \(\delta''^{-1}\nu''^{h'(h(x))}\). The random
variable \(h'^*L^{\nu''}\) on \(G'\) is proper, of module \(\delta''\circ h'\). By Theorem 8.2(c) for \(h\),
\((h'\circ h)(\Lambda)(\nu'')=\int h^*(h'^*L^{\nu''})\,d\Lambda=\int h'^*L^{\nu''}\,d(h(\Lambda))=h'(h(\Lambda))(\nu'')\).

(c) The map \((x,\eta)\mapsto k^{-1}(\eta)\) is an isomorphism of \(X_k\) onto \(G\) with left translation, so \(k\) is
proper (Example 6.9, Proposition 6.10(c)). It carries \(\delta^{-1}\nu'^{k(x)}\) to \((\delta\circ
k)^{-1}(k^{-1}_*\nu')^x\), so \(k^*L^{\nu'}\) is isomorphic to \(L^{k^{-1}_*\nu'}\) and \(k(\Lambda)(\nu')=\Lambda(k^{-1}_*\nu')\)
by Proposition 6.12. For the last formula note \((a\circ s)k_*\nu=k_*((a\circ k\circ s)\nu)\). \(\square\)

**Corollary 8.4 (invariance under equivalence).** Let \(h:G\to G'\) and \(h':G'\to G\) be measurable homomorphisms with
\(h'\circ h=\mathrm{id}_G^{\,\theta}\) and \(h\circ h'=\mathrm{id}_{G'}^{\,\theta'}\). Let \(\delta'\) be a module on \(G'\)
with \(\delta'\circ\theta'=1\), and put \(\delta=\delta'\circ h\); assume \(\delta\circ\theta=1\). Then
\(\delta\circ h'=\delta'\), and \(\Lambda\mapsto h(\Lambda)\) is a bijection from transverse measures of module \(\delta\)
on \(G\) onto transverse measures of module \(\delta'\) on \(G'\), with inverse \(\Lambda'\mapsto h'(\Lambda')\). In
particular transverse measures of module \(1\) are invariant under equivalence of measurable groupoids.

*Proof.* \(h\) and \(h'\) are proper (Corollary 7.5). For \(\gamma':x'\to y'\), \(h(h'(\gamma'))=\theta'(y')\gamma'
\theta'(x')^{-1}\), so \(\delta(h'(\gamma'))=\delta'(\gamma')\). By Corollary 8.3(b), Theorem 8.2(b) and Corollary
8.3(a), \(h'(h(\Lambda))=(h'\circ h)(\Lambda)=\mathrm{id}_G(\Lambda)=\Lambda\); symmetrically \(h(h'(\Lambda'))=\Lambda'\).
\(\square\)

This is the precise sense in which a transverse measure is attached to the "space of orbits" rather than to the
groupoid chosen to describe it: equivalent groupoids describe the same singular space.

**Example 8.5.**

(a) *Covolume of a discrete subgroup.* Let \(\Gamma\) be a discrete subgroup of a locally compact second countable group
\(H\) with \(\Delta_H=1\) on \(\Gamma\). Let \(\Lambda_\Gamma\) be the transverse measure of module \(1\) on \(\Gamma\) with
value \(1\) on counting measure (Example 3.10(b); \(\Gamma\) is countable and discrete). The inclusion \(i:\Gamma\to H\) is
proper (Example 7.2: \(\Gamma\) is closed, and compact subsets of \(\Gamma\) are finite), and \(\Delta_H\circ i=1\). Then
\(i(\Lambda_\Gamma)\) is the transverse measure of module \(\Delta_H\) on \(H\) with
\[
i(\Lambda_\Gamma)(dt)=\int_D\Delta_H(t)^{-1}\,dt ,
\]
where \(D\) is any Borel set meeting every coset \(\Gamma t\) in exactly one point. This is the volume of \(\Gamma\backslash
H\) for the right Haar measure \(\Delta_H(t)^{-1}dt\) (the *covolume* of \(\Gamma\)), possibly infinite.

Such \(D\) exists: choose an open \(U\ni e\) with \(UU^{-1}\cap\Gamma=\{e\}\) and \(t_n\) with \(\bigcup_nUt_n=H\); then
\(Ut_n\) meets each coset in at most one point (if \(u_1t_n=\gamma u_2t_n\) then \(\gamma\in UU^{-1}\)), and
\(D=\bigcup_n\big(Ut_n\setminus\Gamma\bigcup_{m<n}Ut_m\big)\) works. With \(g=1_D\) on \(X_i\cong H\) and \(\nu\) counting
measure on \(\Gamma\), \((\nu*g)(t)=\#(\Gamma t\cap D)=1\), and (8.1) gives the formula, since \((\Lambda_\Gamma)_\nu\) is the
unit mass. By Theorem 8.2(a), the value does not depend on \(D\).

(b) *Invariant measures and total mass.* Let \(G=X\rtimes H\) with \(X\) countably generated and consider the module
\(\delta(x,h)=\Delta_H(h)\), so that \(\delta=\Delta_H\circ p\) for the proper projection \(p\) of Example 7.6(b). By
Corollary 4.3 and Remark 4.4, the transverse measures \(\Lambda\) of module \(\delta\) with \(\Lambda_{\nu_H}\)
\(\sigma\)-finite are given by the \(H\)-invariant \(\sigma\)-finite measures \(\mu=\Lambda_{\nu_H}\) on \(X\) (here
\(c_k=1\) in (4.3)). With \(g\) as in Example 7.6(b), (8.1) gives
\[
p(\Lambda)(dt)=\int_X\int_H\beta(k)\Delta_H(k)^{-1}\,dk\,d\mu(x)=\mu(X).
\]
So the image of \(\Lambda\) on \(H\) is the transverse measure of Example 3.10(b) with value the total mass of \(\mu\).

## 9. Homomorphisms into a locally compact group

Let \(\psi:G\to H\) be a measurable homomorphism into a locally compact second countable group \(H\) with left Haar
measure \(dt\) and modular function \(\Delta=\Delta_H\) normalized by (0.1).

**The stable kernel.** Let \(G_\psi\) be the set \(G\times H\) with unit space \(G^{(0)}\times H\) and
\[
r(\gamma,t)=(r(\gamma),t),\quad s(\gamma,t)=(s(\gamma),t\psi(\gamma)),\quad (\gamma,t)(\gamma',t\psi(\gamma))=(\gamma\gamma',t),
\quad(\gamma,t)^{-1}=(\gamma^{-1},t\psi(\gamma)).
\]
It is a measurable groupoid, the *stable kernel* of \(\psi\). The projection \(p(\gamma,t)=\gamma\) is a homomorphism
\(G_\psi\to G\), and \(\theta_u(\gamma,t)=(\gamma,ut)\), \(u\in H\), are automorphisms of \(G_\psi\). When \(G=H\) and
\(\psi=\mathrm{id}\), \(G_\psi\) is the pair groupoid of \(H\) (Exercise 10.5).

**Lemma 9.1.** For \(\nu\in\mathcal E^+(G)\) let \(\nu_\psi^{(y,t)}\) be the image of \(\nu^y\) under \(\gamma\mapsto
(\gamma,t)\). Then \(\nu_\psi\in\mathcal E^+(G_\psi)\), it is faithful if \(\nu\) is, and \((\theta_u)_*\nu_\psi=\nu_\psi\).
The projection \(p\) is proper, and \(G_\psi\) satisfies (F).

*Proof.* \(G_\psi^{(y,t)}=G^y\times\{t\}\). For \((\gamma_1,t):(x,t\psi(\gamma_1))\to(y,t)\), left translation sends
\((\gamma,t\psi(\gamma_1))\) to \((\gamma_1\gamma,t)\), hence \(\nu_\psi^{(x,t\psi(\gamma_1))}\) to \(\nu_\psi^{(y,t)}\) by
(2.1). Properness holds with the sets \(A_n\times H\), and \(\theta\)-invariance is clear. The \(G_\psi\)-space of \(p\) is
\(X_p=\{((x,t),\gamma):\gamma\in G^x\}\), with \((\gamma_1,t)^{-1}\big((x,t),\gamma\big)=\big((s(\gamma_1),t\psi(\gamma_1)),
\gamma_1^{-1}\gamma\big)\). If \(\nu\) is faithful and \(\nu*k=1\), the function \(f((x,t),\gamma)=k(\gamma)\) satisfies
\((\nu_\psi*f)((x,t),\gamma)=\int k(\gamma_1^{-1}\gamma)\,d\nu^x(\gamma_1)=(\nu*k)(\gamma)=1\). \(\square\)

For a measure \(\mu\) on \(G^{(0)}\) we write \(\mu\otimes dt\) for the measure \(a\mapsto\int\!\int a(y,t)\,dt\,d\mu(y)\) on
\(G^{(0)}\times H\) (the \(t\)-integral is taken first; \(\mu\) need not be \(\sigma\)-finite).

**Theorem 9.2.** Let \(\Lambda\) be a transverse measure of module \(\delta\) on \(G\), and define
\[
\delta_\psi(\gamma,t)=\delta(\gamma)\,\Delta\big(\psi(\gamma)\big)^{-1}.
\]
Then \(\delta_\psi\) is a module on \(G_\psi\), and there is a unique transverse measure \(\Lambda_\psi\) of module
\(\delta_\psi\) on \(G_\psi\) such that \((\Lambda_\psi)_{\nu_\psi}=\Lambda_\nu\otimes dt\) for every
\(\nu\in\mathcal E^+(G)\). It is invariant under the automorphisms \(\theta_u\): \(\Lambda_\psi((\theta_u)_*\nu'')=
\Lambda_\psi(\nu'')\).

*Proof.* \(\delta_\psi\) is multiplicative because \(\delta\) and \(\Delta\circ\psi\) are. Fix a faithful \(\nu\), put
\(\mu=\Lambda_\nu\), \(m=\mu\circ\nu\) and \(m_\psi=(\mu\otimes dt)\circ\nu_\psi\). For \(f\in\mathcal F^+(G_\psi)\), exchanging
the integrals over \(G^y\) and \(H\) (B1),
\[
m_\psi(f)=\int\!\!\int\!\!\int f(\gamma,t)\,dt\,d\nu^y(\gamma)\,d\mu(y)=m(F),\qquad F(\gamma)=\int_Hf(\gamma,t)\,dt .
\]
Since \((\gamma,t)^{-1}=(\gamma^{-1},t\psi(\gamma))\), (0.1) gives \(\int_Hf(\gamma^{-1},t\psi(\gamma))\,dt=
\Delta(\psi(\gamma))^{-1}F(\gamma^{-1})=F_1(\gamma^{-1})\) with \(F_1(\gamma)=\Delta(\psi(\gamma))F(\gamma)\). Hence, by
Theorem 3.5 for \(\Lambda\),
\[
m_\psi(\tilde f)=m(\tilde F_1)=m(\delta^{-1}F_1)=\int\!\!\int\!\!\int\delta(\gamma)^{-1}\Delta(\psi(\gamma))f(\gamma,t)\,dt\,
d\nu^y(\gamma)\,d\mu(y)=m_\psi(\delta_\psi^{-1}f).
\]
So \(\mu\otimes dt\) satisfies condition (1) of Theorem 3.8 for the faithful \(\nu_\psi\), which gives existence and
uniqueness of \(\Lambda_\psi\) with \((\Lambda_\psi)_{\nu_\psi}=\Lambda_\nu\otimes dt\).

For another \(\nu_2\in\mathcal E^+(G)\), let \(k\) satisfy \(\nu*k=1\) and put \(k_\psi(\gamma,t)=k(\gamma)\). Since
\((\gamma_1,t)^{-1}(\gamma,t)=(\gamma_1^{-1}\gamma,t\psi(\gamma_1))\), we get \(\nu_\psi*k_\psi=1\). By (3.3) on
\(G_\psi\), exchanging the integrals over \(H\) and \(G^y\), and (0.1):
\[
(\Lambda_\psi)_{\nu_{2,\psi}}(a)=\int\!\!\int\!\!\int\frac{\Delta(\psi(\gamma))\,k(\gamma)}{\delta(\gamma)}\,
a\big(s(\gamma),t\psi(\gamma)\big)\,dt\,d\nu_2^y(\gamma)\,d\mu(y)
=\int\nu_2^y\big(\delta^{-1}k\,(b\circ s)\big)\,d\mu(y),
\]
with \(b(x)=\int_Ha(x,t)\,dt\). By (3.3) on \(G\) this is \(\Lambda_{\nu_2}(b)=(\Lambda_{\nu_2}\otimes dt)(a)\).

Finally \(\Lambda^u(\nu'')=\Lambda_\psi((\theta_u)_*\nu'')\) is a transverse measure of module
\(\delta_\psi\circ\theta_u=\delta_\psi\), and since \((\theta_u)_*((a\circ s)\nu_\psi)=((a\circ\theta_u^{-1})\circ s)\nu_\psi\),
\((\Lambda^u)_{\nu_\psi}(a)=(\Lambda_\nu\otimes dt)(a\circ\theta_u^{-1})=(\Lambda_\nu\otimes dt)(a)\) by left invariance of
\(dt\). By uniqueness, \(\Lambda^u=\Lambda_\psi\). \(\square\)

*Reference:* [Connes 1979, Section III] writes the moduli of the stable kernel, of its semidirect product and, in its
Proposition 10, of the pair groupoid of \(H\) with \(\Delta_H\) and \(\Delta_H^{-1}\) interchanged, while its own treatment
of action groupoids uses the normalization (0.1). Under (0.1) those formulas fail when \(H\) is not unimodular: for
\(G=H\) and \(\psi=\mathrm{id}\) they give the stable kernel the module \(\Delta_H^2\), whereas Exercise 10.5 shows that
the module is \(1\). So we prove the formulas stated here.

**Products.** For measurable groupoids \(G,K\) and \(\nu\in\mathcal E^+(G)\), \(\kappa\in\mathcal E^+(K)\), the
kernel \((\nu\otimes\kappa)^{(y,z)}=\nu^y\otimes\kappa^z\) on \(G\times K\) is a proper transverse function (use (B1) for
measurability and the sets \(A_n\times A'_n\) for properness), faithful if \(\nu\) and \(\kappa\) are. For modules
\(\delta,\delta_K\), put \((\delta\times\delta_K)(\gamma,\eta)=\delta(\gamma)\delta_K(\eta)\). For a measure \(\mu\) on
\(G^{(0)}\) and a \(\sigma\)-finite measure \(\rho\) on \(K^{(0)}\), \(\mu\otimes\rho\) denotes
\(a\mapsto\int\!\int a(y,z)\,d\rho(z)\,d\mu(y)\).

**Proposition 9.3.** Let \(\Lambda\) and \(\Lambda_K\) be transverse measures of modules \(\delta\) on \(G\) and
\(\delta_K\) on \(K\), with \(\Lambda_K\) \(\sigma\)-finite. There is a unique transverse measure \(\Lambda\times\Lambda_K\) of
module \(\delta\times\delta_K\) on \(G\times K\) with \((\Lambda\times\Lambda_K)_{\nu\otimes\kappa}=\Lambda_\nu\otimes
(\Lambda_K)_\kappa\) for all \(\nu\in\mathcal E^+(G)\) and \(\kappa\in\mathcal E^+(K)\).

*Proof.* Fix faithful \(\nu_0,\kappa_0\), and put \(\mu_0=\Lambda_{\nu_0}\), \(\rho_0=(\Lambda_K)_{\kappa_0}\) (which is
\(\sigma\)-finite by Proposition 3.9), \(m=\mu_0\circ\nu_0\), \(m_K=\rho_0\circ\kappa_0\) (\(\sigma\)-finite). For
\(F\in\mathcal F^+(G\times K)\), exchanging the integrals over \(K^{(0)}\) and \(G^y\) (B1),
\[
M(F)=\big((\mu_0\otimes\rho_0)\circ(\nu_0\otimes\kappa_0)\big)(F)=m(\Psi_F),\qquad\Psi_F(\gamma)=m_K\big(F(\gamma,\cdot)\big).
\]
Theorem 3.5 for \(\Lambda_K\) gives \(\Psi_{\tilde F}(\gamma)=m_K(\delta_K^{-1}F(\gamma^{-1},\cdot))=\Xi(\gamma^{-1})\) with
\(\Xi(\gamma)=m_K(\delta_K^{-1}F(\gamma,\cdot))\); Theorem 3.5 for \(\Lambda\) gives \(m(\tilde\Xi)=m(\delta^{-1}\Xi)\). Thus
\(M(\tilde F)=M((\delta\times\delta_K)^{-1}F)\), and Theorem 3.8 gives a unique \(\Lambda\times\Lambda_K\) with value
\(\mu_0\otimes\rho_0\) at \(\nu_0\otimes\kappa_0\). For arbitrary \(\nu,\kappa\), let \(k,k'\) satisfy \(\nu_0*k=1\),
\(\kappa_0*k'=1\); then \((\nu_0\otimes\kappa_0)*(k\otimes k')=1\). Formula (3.3) on \(G\times K\), an exchange of the
integrals over \(K^{(0)}\) and \(G^y\), and (3.3) on \(K\) and then on \(G\) give
\[
(\Lambda\times\Lambda_K)_{\nu\otimes\kappa}(a)=\int\nu^y\big(\delta^{-1}k\,(b\circ s)\big)\,d\mu_0(y)=\Lambda_\nu(b),\qquad
b(x)=(\Lambda_K)_\kappa\big(a(x,\cdot)\big),
\]
which is \((\Lambda_\nu\otimes(\Lambda_K)_\kappa)(a)\). \(\square\)

**The pair groupoid of \(H\).** Let \(I=H\times H\) be the pair groupoid of \(H\) (Example 1.2(c)): units \(H\),
\(r(t_1,t_2)=t_1\), \(s(t_1,t_2)=t_2\). Its transverse functions are \(\kappa^t=\varepsilon_t\otimes\rho\) for one measure
\(\rho\) on \(H\) (as in Example 2.3(c)); let \(\nu_I\) be the one with \(\rho=dt\). Consider the module
\(\delta_I(t_1,t_2)=\Delta(t_1)\Delta(t_2)^{-1}\), and let \(\Lambda_I=j(\Lambda_e)\), where \(\Lambda_e\) is the transverse
measure on the one-point groupoid \(\{e\}\) with \(\Lambda_e(c\,\varepsilon_e)=c\) and \(j(e)=(e,e)\). The homomorphism \(j\)
is proper (its space \(X_j=\{e\}\times H\) has trivial action, and \(f=1\) works), and \(\delta_I\circ j=1\). By (8.1) with
\(g=1\),
\[
\Lambda_I(\varepsilon\otimes\rho)=\int_H\delta_I(e,u)^{-1}\,d\rho(u)=\int_H\Delta(u)\,d\rho(u),\qquad
(\Lambda_I)_{\nu_I}=\Delta(u)\,du .
\]
In particular \(\Lambda_I\) is \(\sigma\)-finite. (The pair groupoid \(I\) is equivalent to the one-point groupoid.)

**The semidirect product of the stable kernel.** The group \(H\) acts on \(G_\psi\) by the automorphisms
\(\theta_u\). The semidirect product \(G_1=G_\psi\rtimes_\theta H\) is \(G_\psi\times H\) with units \(G^{(0)}\times H\) and
\[
r(\gamma',t_1)=r(\gamma'),\quad s(\gamma',t_1)=\theta_{t_1}^{-1}(s(\gamma')),\quad
(\gamma'_1,t_1)(\gamma'_2,t_2)=(\gamma'_1\,\theta_{t_1}(\gamma'_2),\,t_1t_2)
\]
when \(s(\gamma'_1)=\theta_{t_1}(r(\gamma'_2))\). Thus for \(\gamma'=(\gamma,t)\),
\(s(\gamma',t_1)=(s(\gamma),t_1^{-1}t\psi(\gamma))\). For \(\nu\in\mathcal E^+(G)\) let \(\nu_1^{(y,t)}\) be the image of
\(\nu^y\otimes dt_1\) under \((\gamma,t_1)\mapsto((\gamma,t),t_1)\), and put \(\delta_1(\gamma',t_1)=\Delta(t_1)\,
\delta_\psi(\gamma')\).

**Proposition 9.4.** The map
\[
k:G_1\to G\times I,\qquad k\big((\gamma,t),t_1\big)=\big(\gamma,\,(t,\ t_1^{-1}t\psi(\gamma))\big)
\]
is an isomorphism of measurable groupoids with \((\delta\times\delta_I)\circ k=\delta_1\), which is therefore a module on
\(G_1\). For every \(\nu\in\mathcal E^+(G)\), \(\nu_1\in\mathcal E^+(G_1)\), and \(\nu_1\) is faithful if \(\nu\) is. For every
transverse measure \(\Lambda\) of module \(\delta\) on \(G\) there is a unique transverse measure \(\Lambda_1\) of module
\(\delta_1\) on \(G_1\) with \((\Lambda_1)_{\nu_1}=\Lambda_\nu\otimes dt\) for every \(\nu\in\mathcal E^+(G)\), and
\[
k(\Lambda_1)=\Lambda\times\Lambda_I .
\]
Since \((\Lambda_\psi)_{\nu_\psi}=\Lambda_\nu\otimes dt\) as well, \(\Lambda_1\) is the transverse measure of the semidirect
product attached to the \(\theta\)-invariant \(\Lambda_\psi\) and the Haar measure of \(H\): it has the same measures on the
common unit space \(G^{(0)}\times H\) for the transverse functions \(\nu_1=\nu_\psi\otimes dt_1\).

*Proof.* On units, \(k((y,t),e)=(y,(t,t))\): \(k\) is the identity of \(G^{(0)}\times H\). It maps \(r\) and \(s\) of \(G_1\)
to those of \(G\times I\): \(r=(r(\gamma),t)\) and \(s=(s(\gamma),t_1^{-1}t\psi(\gamma))\) on both sides. It is bijective,
with inverse \((\gamma,(t,u))\mapsto((\gamma,t),t\psi(\gamma)u^{-1})\), and both maps are measurable. For products, let
\(\gamma'_1=(\gamma_1,a)\) and \(\gamma'_2=(\gamma_2,b)\) with \(((\gamma'_1,t_1),(\gamma'_2,t_2))\) composable, that is
\(t_1b=a\psi(\gamma_1)\) and \(s(\gamma_1)=r(\gamma_2)\). The product is \(((\gamma_1\gamma_2,a),t_1t_2)\), with image
\((\gamma_1\gamma_2,(a,(t_1t_2)^{-1}a\psi(\gamma_1\gamma_2)))\). The product of the images is
\((\gamma_1,(a,t_1^{-1}a\psi(\gamma_1)))\,(\gamma_2,(b,t_2^{-1}b\psi(\gamma_2)))=(\gamma_1\gamma_2,(a,t_2^{-1}b\psi(\gamma_2)))\),
composable because \(t_1^{-1}a\psi(\gamma_1)=b\), and \(t_2^{-1}b\psi(\gamma_2)=t_2^{-1}t_1^{-1}a\psi(\gamma_1)\psi(\gamma_2)\).
So \(k\) is multiplicative. For the modules,
\[
(\delta\times\delta_I)(k(\gamma',t_1))=\delta(\gamma)\,\frac{\Delta(t)}{\Delta(t_1^{-1}t\psi(\gamma))}=
\delta(\gamma)\,\Delta(t_1)\,\Delta(\psi(\gamma))^{-1}=\delta_1(\gamma',t_1).
\]
Next we compute \(k_*\nu_1\). For fixed \(\gamma\) and \(t\), put \(c=t\psi(\gamma)\). The image of \(dt_1\) under
\(t_1\mapsto t_1^{-1}c\) is \(\Delta(u)^{-1}du\): by (0.1), \(\int\varphi(t_1^{-1}c)\,dt_1=\int\varphi(t_1c)
\Delta(t_1)^{-1}\,dt_1=\int\varphi(u)\Delta(u)^{-1}\,du\). Hence
\[
(k_*\nu_1)^{(y,t)}=\nu^y\otimes\varepsilon_t\otimes\Delta(u)^{-1}du,\qquad\text{that is}\qquad
k_*\nu_1=(b\circ s)(\nu\otimes\nu_I),\quad b(y,u)=\Delta(u)^{-1}.
\]
This lies in \(\mathcal E^+(G\times I)\) (Lemma 2.2(d)) and is faithful when \(\nu\) is; as \(k\) is an isomorphism,
\(\nu_1=k^{-1}_*(k_*\nu_1)\in\mathcal E^+(G_1)\).

Define \(\Lambda_1(\nu'')=(\Lambda\times\Lambda_I)(k_*\nu'')\) for \(\nu''\in\mathcal E^+(G_1)\); it is a transverse measure
of module \((\delta\times\delta_I)\circ k=\delta_1\), and \(k(\Lambda_1)=\Lambda\times\Lambda_I\) by Corollary 8.3(c). Since
\(k\) is the identity on units, Lemma 3.3 and Proposition 9.3 give
\[
(\Lambda_1)_{\nu_1}(a)=(\Lambda\times\Lambda_I)_{(b\circ s)(\nu\otimes\nu_I)}(a)=
\big(\Lambda_\nu\otimes\Delta(u)\,du\big)\big(\Delta(u)^{-1}a\big)=(\Lambda_\nu\otimes dt)(a).
\]
Uniqueness follows from Theorem 3.8 with a faithful \(\nu_1\). Any transverse measure with the stated property is this
\(\Lambda_1\), so its image under \(k\) is \(\Lambda\times\Lambda_I\). \(\square\)

So, measure-theoretically, forming the stable kernel of \(\psi\) and then the semidirect product by \(H\) gives back
\(G\) up to the factor \(I\), which is equivalent to a point. This is the measured version of the decomposition of a
homomorphism into a locally compact group, used in the classification of ergodic actions.

## 10. Exercises

**Exercise 10.1.** Let \(S\) be a countable set and \(G=S\times S\) its pair groupoid, all subsets measurable.

(a) Show that every module has the form \(\delta(a,b)=c(a)/c(b)\) with \(c:S\to\,]0,\infty[\).

(b) For a measure \(\rho\) on \(S\) finite on points, let \(\nu^\rho\) be the transverse function \(\varepsilon\otimes\rho\)
(Example 2.3(c)). Show that the transverse measures of module \(\delta\) are exactly the maps
\(\Lambda(\nu^\rho)=\kappa\sum_{u\in S}c(u)\rho(\{u\})\) with \(\kappa\in[0,\infty]\). For \(\delta=1\), \(\Lambda(\nu^\rho)\) is
a multiple of the total mass of \(\rho\), which can be infinite: the quotient is one point, and a transverse function is a
measure on the single orbit.

*Solution.* (a) Fix \(u_0\) and put \(c(u)=\delta(u,u_0)\). Then \(\delta(a,b)=\delta(a,u_0)\delta(u_0,b)=
c(a)\,c(b)^{-1}\), since \(\delta(u_0,b)=\delta(b,u_0)^{-1}\).

(b) Let \(\nu=\nu^{\rho_0}\) with \(\rho_0\) counting measure, which is faithful. For \(\mu\) on \(S\),
\((\mu\circ\nu)(f)=\sum_{a,b}\mu(\{a\})f(a,b)\), and condition (1) of Theorem 3.8 reads
\(\sum_{a,b}f(a,b)\mu(\{b\})=\sum_{a,b}f(a,b)\mu(\{a\})c(b)/c(a)\) for all \(f\), that is
\(\mu(\{b\})c(a)=\mu(\{a\})c(b)\) for all \(a,b\). So \(\mu=\kappa c\) with \(\kappa\in[0,\infty]\) (if one value of \(\mu\) is
infinite, all are). The function \(k(a,b)=1_{\{a=u_0\}}\) satisfies \(\nu(\tilde k)(y)=\sum_uk(u,y)=1\), so \(\nu*k=1\).
Formula (3.4) gives \(\Lambda(\nu^\rho)=\sum_t\mu(\{t\})\sum_u\rho(\{u\})\delta(t,u)^{-1}k(t,u)=\kappa\,c(u_0)\sum_u
\rho(\{u\})c(u)/c(u_0)\), as claimed. By Theorem 3.8 every \(\kappa\) occurs.

**Exercise 10.2.** Let \(H\) be a locally compact second countable group. Show that the homomorphism \(H\to\{e\}\) is
proper if and only if \(H\) is compact.

*Solution.* The space of the homomorphism is one point on which \(H\) acts trivially. With \(\nu=dt\),
\(\nu*f=f(\mathrm{pt})\int_Hdt\), which can equal \(1\) if and only if \(H\) has finite Haar measure. A compact group has
finite Haar measure. Conversely, if \(\int_Hdt<\infty\), let \(U\) be a compact neighbourhood of \(e\), of measure
\(|U|>0\). A family of pairwise disjoint translates \(t_iU\) has at most \(\int_Hdt/|U|\) members; take a maximal one. For
every \(t\), \(tU\) meets some \(t_iU\), so \(t\in t_iUU^{-1}\). Hence \(H=\bigcup_it_iUU^{-1}\) is compact.

**Exercise 10.3.** Let \(R\) be a countable Borel equivalence relation on a standard Borel space \(X\) (Example 2.9(b)),
\(\nu\) its counting transverse function, and \(\mu\) a finite measure on \(X\) satisfying (4.1) with \(T=X\) and
\(\delta=1\) (an invariant measure). Let \(\Lambda\) be the transverse measure of module \(1\) with \(\Lambda_\nu=\mu\), and
let \(F\) be the random variable of Example 6.4(b) with \(a=1\) (the constant function \(1\) on the quotient). Assume that
\(\mu\)-almost every class is infinite. Show that \(\int F\,d\Lambda=0\), while \(\Lambda(\nu)=\mu(X)\).

*Solution.* Here \((\nu*f)(x)=\nu^x(f\circ s)=\sum_{y\sim x}f(y)\) and \(\Lambda_\nu(\alpha(f))=\int f\,d\mu\). Let
\(f\in\mathcal F^+(X)\) with \(\sum_{y\sim x}f(y)\le1\) for all \(x\). Apply condition (1) of Theorem 3.8 (with \(\delta=1\))
to \(h(x,y)=f(y)\) on \(R\): \(m(h)=\int\sum_{y\sim x}f(y)\,d\mu(x)\le\mu(X)<\infty\), and \(m(\tilde h)=
\int\sum_{y\sim x}f(x)\,d\mu(x)=\int f(x)\,\#[x]\,d\mu(x)\). These are equal, so \(f=0\) \(\mu\)-almost everywhere on the
measurable set \(\{\#[x]=\infty\}=\{\nu^x(G)=\infty\}\), which has full measure. Hence \(\int f\,d\mu=0\) and
\(\int F\,d\Lambda=0\). On the other hand \(\Lambda(\nu)=\Lambda_\nu(1)=\mu(X)\): the transverse function "counting measure
on each orbit", which is infinite at every point of the quotient, has finite nonzero integral.

**Exercise 10.4.** Let \(\nu\in\mathcal E^+\) be faithful. Show that a transverse measure \(\Lambda\) is zero as soon as
\(\Lambda(\nu)=0\).

*Solution.* \(\Lambda_\nu(G^{(0)})=\Lambda(\nu)=0\), so by Proposition 5.2(a) the saturated set \(G^{(0)}\) is
\(\Lambda\)-negligible. Hence \(\Lambda(\nu')=\Lambda_{\nu'}(G^{(0)})=0\) for all \(\nu'\in\mathcal E^+\).

**Exercise 10.5.** Let \(G=H\) be a locally compact second countable group, \(\Lambda\) the transverse measure of module
\(\Delta_H\) with \(\Lambda(dt)=1\) (Example 3.10(b)), and \(\psi=\mathrm{id}\). Show that \((\gamma,t)\mapsto(t,t\gamma)\) is
an isomorphism of the stable kernel \(G_\psi\) onto the pair groupoid \(I\) of \(H\) carrying \(\nu_\psi\) (for \(\nu=dt\)) to
\(\nu_I\), that \(\delta_\psi=1\), and that the image of \(\Lambda_\psi\) is the transverse measure of module \(1\) on \(I\)
whose measure at \(\nu_I\) is \(du\). Check this against Theorem 3.8 on \(I\).

*Solution.* The units of \(G_\psi\) are \(\{e\}\times H\cong H\), with \(r(\gamma,t)=t\) and \(s(\gamma,t)=t\gamma\); the map
sends \((\gamma,t)\) to the pair \((r,s)\), and \((\gamma,t)(\gamma',t\gamma)=(\gamma\gamma',t)\) goes to
\((t,t\gamma)(t\gamma,t\gamma\gamma')=(t,t\gamma\gamma')\). It is bijective and bimeasurable. The measure
\(\nu_\psi^{t}\) is the image of \(d\gamma\) under \(\gamma\mapsto(\gamma,t)\), which the map sends to the image of
\(d\gamma\) under \(\gamma\mapsto(t,t\gamma)\), namely \(\varepsilon_t\otimes du\) by left invariance: this is \(\nu_I^t\).
Next \(\delta_\psi(\gamma,t)=\Delta_H(\gamma)\Delta_H(\gamma)^{-1}=1\), and \((\Lambda_\psi)_{\nu_\psi}=\Lambda_{dt}\otimes dt=du\)
on \(H\) (Corollary 8.3(c) transports this to \(I\)). On \(I\), for \(\mu=c(u)\,du\) with \(c>0\) and \(m=\mu\circ\nu_I\), we have
\(m(f)=\int\!\int f(a,b)\,db\,c(a)\,da\), hence \(m(\tilde f)=\int\!\int f(a,b)\,c(b)\,da\,db\) and
\(m(\delta^{-1}f)=\int\!\int f(a,b)\,\delta(a,b)^{-1}c(a)\,da\,db\). So condition (1) of Theorem 3.8 holds exactly when
\(\delta(a,b)=c(a)/c(b)\) for almost all \((a,b)\), and \(\mu=du\) (\(c=1\)) requires module \(1\), as found. The module
\(\Delta_H(\gamma)^2\), which the opposite convention for \(\Delta_H\) would produce, corresponds to
\(\mu=\Delta_H(u)^{-2}du\) instead.

## References



- [Connes 1979] A. Connes, Sur la théorie non commutative de l'intégration, in: Algèbres d'opérateurs (Sém.,
  Les Plans-sur-Bex, 1978), Lecture Notes in Math. 725, Springer, Berlin, 1979, 19–143. Free at https://alainconnes.org/wp-content/uploads/ThNonComm.pdf
- [Connes 1982] A. Connes, A survey of foliations and operator algebras, in: Operator algebras and applications,
  Part I (Kingston, Ont., 1980), Proc. Sympos. Pure Math. 38, Amer. Math. Soc., Providence, RI, 1982, 521–628. Free at https://alainconnes.org/wp-content/uploads/foliationsfine.pdf
- [Connes 1994] A. Connes, Noncommutative geometry, Academic Press, San Diego, CA, 1994.
  https://alainconnes.org/publications/
- [Ramsay] A. Ramsay, Virtual groups and group actions, Advances in Math. 6 (1971), 253–322.
  https://doi.org/10.1016/0001-8708(71)90018-1. Free at https://doi.org/10.1016/0001-8708(71)90018-1

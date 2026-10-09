# The scaling site

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions (AI Integrated Stacks Project citations; the points of a topos of sheaves, Lebesgue's covering theorem, three elementary facts and one implication of Weil's criterion proved) are self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

The arithmetic site is the topos of sets with an action of the monoid \(\mathbb{N}^{\times}\) of positive integers,
together with the structure sheaf \(\mathbb{Z}_{\max}\). It is an object over the Boolean semifield \(\mathbb{B}\).
Its points over the tropical semifield \(\mathbb{R}_{\max}\) form the quotient
\(\mathbb{Q}^{\times}\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb{Z}}^{\times}\) of the adèle class space of
\(\mathbb{Q}\). This is proved in *The arithmetic site*.

For a curve \(C\) over a finite field \(\mathbb{F}_q\), Weil's proof of the Riemann hypothesis does not take place on
\(C\). It takes place on the square of the curve. The lesson *Weil's proof for curves and what is missing over the
integers* carries it out on the surface \(C\times C\) over \(\mathbb{F}_q\). In the form recalled in
[Connes 2015, Section 2.3], one first extends scalars to \(\bar C=C\otimes_{\mathbb{F}_q}\bar{\mathbb{F}}_q\) and
then works on the surface \(\bar C\times\bar C\). The scaling site of [Connes–Consani 2017] plays the role of
\(\bar C\) for the arithmetic site. It is the arithmetic site after extension of scalars from \(\mathbb{B}\) to
\(\mathbb{R}_{\max}\).

The lesson has four parts.

1. **Extension of scalars (Section 2).** We compute the semiring \(\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}\)
   and its largest multiplicatively cancellative quotient. The quotient is a semiring of convex piecewise affine
   functions on the half-line \([0,\infty)\) with integral slopes. The Frobenius maps of \(\mathbb{Z}_{\max}\) become
   the maps \(f(\lambda)\mapsto f(n\lambda)\).
2. **The site and its points (Sections 3 to 5).** The scaling site is the topos \([0,\infty)\rtimes\mathbb{N}^{\times}\)
   of \(\mathbb{N}^{\times}\)-equivariant sheaves on the half-line, with the sheaf \(\mathcal{O}\) of convex piecewise
   affine functions with integral slopes. We classify its points with full proofs, identify them with
   \(\mathbb{Q}^{\times}\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb{Z}}^{\times}\), and compute the stalks of
   \(\mathcal{O}\).
3. **Periodic orbits as curves (Section 6).** For each prime \(p\) the scaling flow has a periodic orbit \(C_p\) of
   length \(\log p\). It carries functions, divisors with real degree, theta functions and a Riemann–Roch theorem with
   real-valued dimensions. All of this is proved here; the one classical theorem of dimension theory it needs,
   Lebesgue's covering theorem, is proved in two lessons of the course on index theory of elliptic operators.
4. **The Riemann hypothesis (Section 7).** We state exactly which theorems the scaling site provides, which inequality
   would have to be proved, and which constructions are missing.

**What the lesson assumes.** Sheaves on a topological space; the definition of a Grothendieck topology and of a point
of a topos, to the extent recalled in Sections 3.1 and 4.1, with the lessons
Sites and sheaves and Topoi, morphisms and points of the course on étale cohomology; convex functions of one real variable and convex subsets
of \(\mathbb{R}^{m}\); the finite adèles of \(\mathbb{Q}\) as used in *The arithmetic site*. Prerequisite lessons are
*The arithmetic site* and *Characteristic one and hyperrings*. Section 7 refers to *Weil's proof for curves and what
is missing over the integers*. Section 6.6 uses the lessons
Covering dimension and finite trivializing covers and
Lebesgue's covering theorem and the dimension of cubes.

Basic references are [Connes–Consani 2017] and [Connes–Consani 2016b].

## 1. Conventions and two lemmas

**Semirings.** As in *Characteristic one and hyperrings*, a semiring is commutative, has elements 0 and 1, and 0 is
absorbing. It has *characteristic one* when \(1+1=1\). Then \(a\le b\iff a+b=b\) defines an order, and \(a+b\) is the
least upper bound of \(a\) and \(b\). A semiring is *multiplicatively cancellative* when \(ac=bc\) and \(c\neq 0\)
imply \(a=b\).

The semifield \(\mathbb{R}_{\max}\) is the set \(\mathbb{R}\cup\{-\infty\}\). Its semiring sum is
\(x\vee y=\max(x,y)\). Its semiring product is the ordinary sum \(x+y\). So the zero of \(\mathbb{R}_{\max}\) is
\(-\infty\) and its one is the number \(0\). This lesson always uses this additive writing: the symbol \(\vee\) is the
semiring sum and the symbol \(+\) is the semiring product. The same rules define \(H_{\max}=H\cup\{-\infty\}\) for
every subgroup \(H\subseteq\mathbb{R}\) and for every totally ordered abelian group \(H\). Examples are
\(\mathbb{Z}_{\max}\) and the Boolean semifield \(\mathbb{B}=\{-\infty,0\}\).

We write \(\mathbb{N}^{\times}=\{1,2,3,\dots\}\) for the positive integers under multiplication. This monoid has no
zero element; in this lesson a monoid is not required to have one.

For \(n\in\mathbb{N}^{\times}\) the map \(\mathrm{Fr}_n(x)=nx\) is an injective endomorphism of
\(\mathbb{Z}_{\max}\). In multiplicative writing it is \(x\mapsto x^{n}\). For every real number \(\mu>0\) the map
\(\mathrm{Fr}_\mu(x)=\mu x\) is an automorphism of \(\mathbb{R}_{\max}\). We write \(\mathbb{R}_{>0}\) for the
multiplicative group of positive real numbers.

An *\(\mathbb{R}_{\max}\)-algebra* is a semiring \(R\) with a morphism of semirings \(\mathbb{R}_{\max}\to R\). For
\(c\in\mathbb{R}_{\max}\) and \(r\in R\) we write \(c+r\) for the product of \(r\) with the image of \(c\). A morphism
of \(\mathbb{R}_{\max}\)-algebras is a morphism of semirings \(\varphi\) with \(\varphi(c+r)=c+\varphi(r)\).

**Rank one.** A *rank one subgroup of \(\mathbb{R}\)* is a subgroup \(H\neq\{0\}\) of \(\mathbb{R}\) such that
\(h/h'\in\mathbb{Q}\) for all \(h,h'\in H\) with \(h'\neq 0\). We write \(H_+=H\cap(0,\infty)\). A *rank one ordered
group* is a totally ordered abelian group that is isomorphic, as an ordered group, to a non-zero subgroup of
\(\mathbb{Q}\). For a prime \(p\) we write \(H_p=\mathbb{Z}[1/p]\subset\mathbb{Q}\).

**Lemma 1.1.** Let \(H\) be a rank one subgroup of \(\mathbb{R}\).

1. Any finitely many elements \(h_1,\dots,h_k\) of \(H_+\) are positive integer multiples of one element \(g\in H_+\).
2. If \(H'\) is a rank one subgroup of \(\mathbb{R}\) and \(\varphi\colon H\to H'\) is a group homomorphism, then there
   is a real number \(c\) with \(\varphi(h)=ch\) for all \(h\in H\).

*Proof.* (1) Fix \(h_0\in H_+\). Then \(h_0^{-1}H\) is a subgroup of \(\mathbb{Q}\). It contains the positive
rational numbers \(r_i=h_i/h_0\). A finitely generated subgroup of \(\mathbb{Q}\) lies in \(\tfrac1N\mathbb{Z}\) for
some \(N\), so it is cyclic. Let \(r>0\) generate the group spanned by \(r_1,\dots,r_k\). Then \(r\in h_0^{-1}H\) and
\(r_i=n_ir\) with \(n_i\in\mathbb{N}^{\times}\). Put \(g=h_0r\).

(2) Fix \(h_0\in H\), \(h_0\ne0\), and put \(c=\varphi(h_0)/h_0\). For \(h\in H\) there are integers \(n\neq0\) and
\(m\) with \(nh=mh_0\). Then \(n\varphi(h)=m\varphi(h_0)=mch_0=nch\), so \(\varphi(h)=ch\). \(\blacksquare\)

**Piecewise affine functions.** Let \(U\) be an open subset of the half-line \([0,\infty)\) and let \(G\) be a subgroup
of \(\mathbb{R}\). We write \(\mathrm{PA}_G(U)\) for the set of continuous functions \(f\colon U\to\mathbb{R}\) with
the following property. For each \(\lambda_0\in U\) there are \(\varepsilon>0\) and \(a_-,a_+\in G\) such that

\[
f(\lambda)=f(\lambda_0)+a_+(\lambda-\lambda_0)\ \text{ for }\lambda_0\le\lambda<\lambda_0+\varepsilon,\qquad
f(\lambda)=f(\lambda_0)+a_-(\lambda-\lambda_0)\ \text{ for }\lambda_0-\varepsilon<\lambda\le\lambda_0 .
\]

For \(\lambda_0=0\) only the first condition is imposed. We write \(a_\pm=f'_\pm(\lambda_0)\) and call these numbers
the *slopes* of \(f\) at \(\lambda_0\). The *jump* of \(f\) at \(\lambda_0>0\) is
\(j_f(\lambda_0)=f'_+(\lambda_0)-f'_-(\lambda_0)\in G\). A *breakpoint* is a point with non-zero jump. The breakpoints
form a closed discrete subset of \(U\). We write \(\mathrm{CPA}_G(U)\) for the set of those \(f\in\mathrm{PA}_G(U)\)
with \(j_f(\lambda_0)\ge0\) for all \(\lambda_0\in U\), \(\lambda_0>0\).

**Lemma 1.2.** Let \(U\subseteq[0,\infty)\) be open and \(G\subseteq\mathbb{R}\) a subgroup.

1. \(\mathrm{PA}_G(U)\) is a group under pointwise addition, and it is closed under pointwise maximum.
   \(\mathrm{CPA}_G(U)\) is closed under pointwise addition and pointwise maximum.
2. Let \(f,g\in\mathrm{PA}_G(U)\) and \(\lambda>0\) in \(U\). Then \(j_{f+g}(\lambda)=j_f(\lambda)+j_g(\lambda)\). If
   \(f(\lambda)>g(\lambda)\), then \(j_{f\vee g}(\lambda)=j_f(\lambda)\). If \(f(\lambda)=g(\lambda)\), then
   \(j_{f\vee g}(\lambda)\ge\max(j_f(\lambda),j_g(\lambda))\).
3. If \(U\) is an interval, then \(f\in\mathrm{PA}_G(U)\) is a convex function if and only if
   \(f\in\mathrm{CPA}_G(U)\).

*Proof.* Sums and differences are clear. Let \(f,g\in\mathrm{PA}_G(U)\) and \(\lambda_0\in U\). If
\(f(\lambda_0)>g(\lambda_0)\), then \(f\vee g=f\) near \(\lambda_0\) by continuity. If \(f(\lambda_0)=g(\lambda_0)\),
then near \(\lambda_0\)

\[
(f\vee g)(\lambda)=f(\lambda_0)+\max\bigl(f'_+(\lambda_0),g'_+(\lambda_0)\bigr)(\lambda-\lambda_0)\quad(\lambda\ge\lambda_0),
\]
\[
(f\vee g)(\lambda)=f(\lambda_0)+\min\bigl(f'_-(\lambda_0),g'_-(\lambda_0)\bigr)(\lambda-\lambda_0)\quad(\lambda\le\lambda_0),
\]

because \(\lambda-\lambda_0\le0\) in the second line. So \(f\vee g\in\mathrm{PA}_G(U)\), and its jump at \(\lambda_0\)
is \(\max(f'_+,g'_+)-\min(f'_-,g'_-)\), which is at least \(j_f(\lambda_0)\) and at least \(j_g(\lambda_0)\). This
proves (1) and (2). For (3): on an interval, \(f\) is affine between consecutive breakpoints. If all jumps are
\(\ge0\), the slope is a non-decreasing function of \(\lambda\), so \(f\) is convex. Conversely a convex function has
\(f'_-\le f'_+\) at every interior point. \(\blacksquare\)

## 2. Extension of scalars: from \(\mathbb{Z}_{\max}\) to functions on the half-line

The arithmetic site has the structure sheaf \(\mathbb{Z}_{\max}\) with the Frobenius maps \(\mathrm{Fr}_n\). To
extend scalars from \(\mathbb{B}\) to \(\mathbb{R}_{\max}\) we form the tensor product
\(\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}\) and the maps \(\mathrm{Fr}_n\otimes\mathrm{id}\). This
section computes them. A reference for this section is [Connes–Consani 2017, Section 2.1].

### 2.1 The tensor product of two totally ordered \(\mathbb{B}\)-modules

A *\(\mathbb{B}\)-module* is a commutative monoid \((M,\vee,0)\) with \(x\vee x=x\) for all \(x\). It is ordered by
\(x\le y\iff x\vee y=y\), and \(0\) is its least element. Every semiring of characteristic one is a
\(\mathbb{B}\)-module under its sum. A map \(\varphi\colon M\times N\to P\) between \(\mathbb{B}\)-modules is
*bilinear* when

\[
\varphi(x\vee x',y)=\varphi(x,y)\vee\varphi(x',y),\qquad \varphi(x,y\vee y')=\varphi(x,y)\vee\varphi(x,y'),\qquad
\varphi(0,y)=\varphi(x,0)=0 .
\]

A *tensor product* \(M\otimes_{\mathbb{B}}N\) is a \(\mathbb{B}\)-module with a bilinear map
\(\tau\colon M\times N\to M\otimes_{\mathbb{B}}N\) such that every bilinear map \(M\times N\to P\) factors uniquely as
\(\Phi\circ\tau\) with \(\Phi\) a morphism of \(\mathbb{B}\)-modules.

**Proposition 2.1.** Let \(M\) and \(N\) be \(\mathbb{B}\)-modules whose orders are total. Put
\(M^{*}=M\smallsetminus\{0\}\), \(N^{*}=N\smallsetminus\{0\}\), and order \(M^{*}\times N^{*}\) by
\((x',y')\le(x,y)\iff x'\le x\) and \(y'\le y\). For \((x,y)\in M^{*}\times N^{*}\) let

\[
Q(x,y)=\{(x',y')\in M^{*}\times N^{*} : (x',y')\le(x,y)\}.
\]

Let \(T(M,N)\) be the set of all finite unions of sets \(Q(x,y)\), the empty union included, with the operation
\(\cup\). Define \(\tau(x,y)=Q(x,y)\) for \(x\ne0\), \(y\ne0\), and \(\tau(x,y)=\emptyset\) otherwise. Then
\((T(M,N),\tau)\) is a tensor product of \(M\) and \(N\).

*Proof.* \(T(M,N)\) is a \(\mathbb{B}\)-module with zero \(\emptyset\). The map \(\tau\) is bilinear: if \(x\le x'\)
in \(M^{*}\), then \(x\vee x'=x'\) and \(Q(x,y)\cup Q(x',y)=Q(x',y)\). The other identities are checked in the same
way.

Let \(\varphi\colon M\times N\to P\) be bilinear. Since the order of \(M\) is total, \(x\le x'\) gives
\(\varphi(x',y)=\varphi(x\vee x',y)=\varphi(x,y)\vee\varphi(x',y)\), that is
\(\varphi(x,y)\le\varphi(x',y)\). So \(\varphi\) is non-decreasing in each variable. Define

\[
\Phi\Bigl(\,\bigcup_i Q(x_i,y_i)\Bigr)=\bigvee_i\varphi(x_i,y_i).
\]

This does not depend on the way the set is written. Indeed, if \(\bigcup_iQ(x_i,y_i)=\bigcup_jQ(x'_j,y'_j)\), then
each \((x_i,y_i)\) lies in some \(Q(x'_j,y'_j)\), so \(\varphi(x_i,y_i)\le\varphi(x'_j,y'_j)\). Hence
\(\bigvee_i\varphi(x_i,y_i)\le\bigvee_j\varphi(x'_j,y'_j)\), and the reverse inequality holds by symmetry. The map
\(\Phi\) is a morphism of \(\mathbb{B}\)-modules with \(\Phi\circ\tau=\varphi\). It is unique because the sets
\(Q(x,y)\) generate \(T(M,N)\). \(\blacksquare\)

*Reference:* [Connes–Consani 2016b, Proposition 6.6] for \(M=N=\mathbb{Z}_{\min}\).

### 2.2 The semiring \(\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}\)

Take \(M=\mathbb{Z}_{\max}\) and \(N=\mathbb{R}_{\max}\). Then \(M^{*}=\mathbb{Z}\) and \(N^{*}=\mathbb{R}\). For a
point \(P=(x,y)\in\mathbb{Z}\times\mathbb{R}\) the set \(Q(P)\) is the quadrant
\(\{(x',y')\in\mathbb{Z}\times\mathbb{R}:x'\le x,\ y'\le y\}\). We write

\[
T=\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}=\{\text{finite unions of quadrants }Q(P)\}.
\]

For \(E,E'\in T\) put \(E\cdot E'=\{P+P':P\in E,\ P'\in E'\}\). Since \(Q(P)\cdot Q(P')=Q(P+P')\), the product of two
elements of \(T\) is in \(T\). The product is associative and commutative, it distributes over \(\cup\), and
\(Q(0,0)\) is neutral. So \(T\) is a semiring of characteristic one with zero \(\emptyset\) and one \(Q(0,0)\). The
maps \(x\mapsto Q(x,0)\) and \(y\mapsto Q(0,y)\), with \(-\infty\mapsto\emptyset\), are morphisms of semirings from
\(\mathbb{Z}_{\max}\) and from \(\mathbb{R}_{\max}\) to \(T\), and \(Q(x,y)=Q(x,0)\cdot Q(0,y)\). The second map makes
\(T\) an \(\mathbb{R}_{\max}\)-algebra. If \(E\ne\emptyset\) and \(E'\ne\emptyset\), then
\(E\cdot E'\neq\emptyset\).

For \(n\in\mathbb{N}^{\times}\) the map \((x,y)\mapsto Q(nx,y)\) is bilinear. By Proposition 2.1 it gives a map

\[
\mathrm{Fr}_n\otimes\mathrm{id}\colon T\to T,\qquad \bigcup_iQ(x_i,y_i)\mapsto\bigcup_iQ(nx_i,y_i).
\]

It is an endomorphism of the \(\mathbb{R}_{\max}\)-algebra \(T\), and
\((\mathrm{Fr}_n\otimes\mathrm{id})(\mathrm{Fr}_m\otimes\mathrm{id})=\mathrm{Fr}_{nm}\otimes\mathrm{id}\).

**Example 2.2 (\(T\) is not multiplicatively cancellative).** Let \(a=Q(0,0)\cup Q(2,-2)\) and
\(b=a\cup Q(1,-1)\). The point \((1,-1)\) lies in neither \(Q(0,0)\) nor \(Q(2,-2)\), so \(a\neq b\). Both products
\(a\cdot b\) and \(b\cdot b\) are equal to

\[
Q(0,0)\cup Q(1,-1)\cup Q(2,-2)\cup Q(3,-3)\cup Q(4,-4).
\]

So \(a\cdot b=b\cdot b\) with \(b\neq\emptyset\) and \(a\neq b\). Also \(a\cdot a=Q(0,0)\cup Q(2,-2)\cup Q(4,-4)\) is
not equal to \(Q(0,0)\cup Q(4,-4)\). So squaring is not additive on \(T\). In *Characteristic one and hyperrings*
the power maps are shown to be endomorphisms of every multiplicatively cancellative semiring of characteristic one.
The semiring \(T\) is not of this kind.

### 2.3 The cancellative quotient is a semiring of convex functions

**Definition.** \(\mathcal{R}(\mathbb{Z})\) is the set consisting of the constant function \(-\infty\) and of all
functions \(f\colon[0,\infty)\to\mathbb{R}\) of the form

\[
f(\lambda)=\max_{1\le i\le m}(x_i\lambda+y_i),\qquad m\ge1,\ x_i\in\mathbb{Z},\ y_i\in\mathbb{R}.
\]

With pointwise maximum as sum and pointwise addition as product, \(\mathcal{R}(\mathbb{Z})\) is a semiring of
characteristic one. The constants make it an \(\mathbb{R}_{\max}\)-algebra. It is multiplicatively cancellative: if
\(f+h=g+h\) and \(h\neq-\infty\), then \(h\) is finite everywhere and \(f=g\).

**Lemma 2.3.** The finite elements of \(\mathcal{R}(\mathbb{Z})\) are exactly the functions in
\(\mathrm{CPA}_{\mathbb{Z}}([0,\infty))\) with finitely many breakpoints.

*Proof.* A maximum of finitely many affine functions with integral slopes is in \(\mathrm{CPA}_{\mathbb{Z}}\) by
Lemma 1.2, and it has finitely many breakpoints because two distinct affine functions agree in at most one point.
Conversely let \(f\in\mathrm{CPA}_{\mathbb{Z}}([0,\infty))\) have finitely many breakpoints. Let
\(\ell_0,\dots,\ell_k\) be the affine functions that agree with \(f\) on the intervals between consecutive
breakpoints. By Lemma 1.2 (3) the function \(f\) is convex, so \(f\ge\ell_i\) on \([0,\infty)\) for each \(i\). Hence
\(f=\max_i\ell_i\). \(\blacksquare\)

For \(E\in T\) define a function \(L(E)\) on \([0,\infty)\) by \(L(\emptyset)=-\infty\) and

\[
L(E)(\lambda)=\sup\{x\lambda+y:(x,y)\in E\}=\max_i(x_i\lambda+y_i)\qquad\text{for }E=\bigcup_iQ(x_i,y_i).
\]

The two expressions agree because \(\lambda\ge0\): on a quadrant \(Q(x_i,y_i)\) the function
\((x,y)\mapsto x\lambda+y\) is largest at the corner. The function \(L(E)\) is a form of the Legendre transform of
\(E\).

**Lemma 2.4.** Let \(E\in T\), \(E\neq\emptyset\), and let \(P=(k,y)\in\mathbb{Z}\times\mathbb{R}\) be a point with
\(k\lambda+y\le L(E)(\lambda)\) for all \(\lambda\ge0\). Then there is \(C\in T\), \(C\neq\emptyset\), with
\((E\cup Q(P))\cdot C=E\cdot C\).

*Proof.* Write \(E=\bigcup_iQ(x_i,y_i)\), \(f=L(E)\) and \(g(\lambda)=f(\lambda)-k\lambda-y\). The function \(g\) is
convex, piecewise affine with finitely many breakpoints, and \(g\ge0\) on \([0,\infty)\). Call the index \(i\)
*active* at \(\lambda\) when \(x_i\lambda+y_i=f(\lambda)\).

*Step 1: there are indices \(i_1,i_2\) and integers \(d\ge1\), \(0\le e\le d\) with
\(dP\le(d-e)(x_{i_1},y_{i_1})+e(x_{i_2},y_{i_2})\) in the product order.*
The slope of \(g\) for large \(\lambda\) is \(\max_ix_i-k\). It is \(\ge0\), since otherwise \(g\) would take negative
values. The slope of \(g\) at \(0\) is \(s_0=\max\{x_i-k:i\text{ active at }0\}\).

If \(s_0\ge0\), there is an index \(i\) active at \(0\) with \(x_i\ge k\). Then \(y_i=f(0)=g(0)+y\ge y\). So
\(P\le(x_i,y_i)\), and we take \(i_1=i_2=i\), \(d=1\), \(e=0\).

If \(s_0<0\), the convex function \(g\) first decreases and finally does not decrease. So it has a minimum at some
\(\lambda_0>0\) with \(g'_-(\lambda_0)\le0\le g'_+(\lambda_0)\). The two slopes are the smallest and the largest of
the numbers \(x_i-k\) over the indices active at \(\lambda_0\). So there are active indices \(i_1,i_2\) with
\(x_{i_1}\le k\le x_{i_2}\). For an active index, \(y_i=f(\lambda_0)-x_i\lambda_0\). If \(x_{i_1}=k\), then
\(y_{i_1}=g(\lambda_0)+y\ge y\) and \(P\le(x_{i_1},y_{i_1})\). The case \(x_{i_2}=k\) is the same. Otherwise put
\(d=x_{i_2}-x_{i_1}\) and \(e=k-x_{i_1}\), so \(0<e<d\). Then \((d-e)x_{i_1}+ex_{i_2}=dk\) and

\[
(d-e)y_{i_1}+ey_{i_2}=d\,f(\lambda_0)-\lambda_0\,dk=d\,(g(\lambda_0)+y)\ \ge\ dy .
\]

*Step 2.* Put \(a=Q(x_{i_1},y_{i_1})\), \(b=Q(x_{i_2},y_{i_2})\), \(q=Q(P)\), and let \(r\) be the union of the other
quadrants of \(E\), so \(E=a\cup b\cup r\). Step 1 says \(q^{d}\subseteq a^{d-e}b^{e}\), where powers are taken in
\(T\). In a semiring of characteristic one, \((u\vee v)^{d}=\bigvee_{j=0}^{d}u^{j}v^{d-j}\). With \(u=q\) and
\(v=a\cup b\) this gives

\[
(a\cup b\cup q)^{d}=\bigcup_{j=0}^{d}q^{j}(a\cup b)^{d-j}=\bigcup_{j=0}^{d-1}q^{j}(a\cup b)^{d-j}
=(a\cup b)\cdot(a\cup b\cup q)^{d-1}.
\]

The middle equality holds because the term \(q^{d}\) is contained in \(a^{d-e}b^{e}\subseteq(a\cup b)^{d}\), which is
the term \(j=0\). Let \(C=(a\cup b\cup q)^{d-1}\), a non-empty element of \(T\). Then
\((a\cup b\cup q)\cdot C=(a\cup b)\cdot C\). Adding \(r\cdot C\) to both sides gives
\((E\cup q)\cdot C=E\cdot C\). \(\blacksquare\)

**Theorem 2.5 (the reduction).**

1. The map \(L\colon T\to\mathcal{R}(\mathbb{Z})\) is a surjective morphism of \(\mathbb{R}_{\max}\)-algebras, and
   \(L(E)=-\infty\) only for \(E=\emptyset\).
2. For \(E,E'\in T\): \(L(E)=L(E')\) if and only if there is \(C\in T\), \(C\neq\emptyset\), with
   \(E\cdot C=E'\cdot C\).
3. Let \(R\) be a multiplicatively cancellative semiring and \(\rho\colon T\to R\) a morphism of semirings with
   \(\rho(E)\ne0\) for \(E\neq\emptyset\). Then \(\rho=\bar\rho\circ L\) for a unique morphism of semirings
   \(\bar\rho\colon\mathcal{R}(\mathbb{Z})\to R\).
4. For \(n\in\mathbb{N}^{\times}\) and \(E\in T\): \(L\bigl((\mathrm{Fr}_n\otimes\mathrm{id})E\bigr)(\lambda)=L(E)(n\lambda)\).

So \(\mathcal{R}(\mathbb{Z})\) is the largest multiplicatively cancellative quotient of
\(\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}\) in the sense of (3). It is written
\(\mathbb{Z}_{\max}\widehat\otimes_{\mathbb{B}}\mathbb{R}_{\max}\). The Frobenius \(\mathrm{Fr}_n\otimes\mathrm{id}\)
becomes the substitution \(f(\lambda)\mapsto f(n\lambda)\).

*Proof.* (1) \(L(E\cup E')=L(E)\vee L(E')\) is clear. For non-empty \(E,E'\) the supremum of \(x\lambda+y\) over
\(E\cdot E'\) is the sum of the suprema over \(E\) and over \(E'\), so \(L(E\cdot E')=L(E)+L(E')\). Also
\(L(Q(0,y))\) is the constant \(y\). Surjectivity holds by the definition of \(\mathcal{R}(\mathbb{Z})\).

(2) If \(E\cdot C=E'\cdot C\) with \(C\ne\emptyset\), then \(L(E)+L(C)=L(E')+L(C)\) and \(L(C)\) is finite, so
\(L(E)=L(E')\). Conversely let \(L(E)=L(E')\). If this function is \(-\infty\), then \(E=E'=\emptyset\). Otherwise
write \(E'=Q(P_1)\cup\dots\cup Q(P_m)\) and \(E_j=E\cup Q(P_1)\cup\dots\cup Q(P_j)\). Then \(L(E_j)=L(E)\) for all
\(j\), and \(L(Q(P_{j+1}))\le L(E')=L(E_j)\). Lemma 2.4 gives non-empty \(C_j\) with
\(E_{j+1}\cdot C_j=E_j\cdot C_j\). With \(C'=C_0\cdots C_{m-1}\neq\emptyset\) we get
\(E\cdot C'=(E\cup E')\cdot C'\). In the same way \(E'\cdot C''=(E\cup E')\cdot C''\) for some \(C''\neq\emptyset\).
So \(E\cdot C'C''=E'\cdot C'C''\).

(3) If \(E\cdot C=E'\cdot C\) with \(C\neq\emptyset\), then \(\rho(E)\rho(C)=\rho(E')\rho(C)\) and
\(\rho(C)\neq0\), so \(\rho(E)=\rho(E')\). By (2), \(\rho\) is constant on the fibres of \(L\). Since \(L\) is a
surjective morphism, \(\bar\rho(L(E))=\rho(E)\) defines the unique morphism with \(\rho=\bar\rho\circ L\).

(4) \(\max_i(nx_i\lambda+y_i)=L(E)(n\lambda)\). \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Lemma 2.1 and Proposition 2.2]; for
\(\mathbb{Z}_{\min}\otimes_{\mathbb{B}}\mathbb{Z}_{\min}\), [Connes–Consani 2016b, Proposition 6.21].

In Example 2.2, \(L(a)=L(b)=\max(0,2\lambda-2)\), in agreement with part (2).

### 2.4 The half-line as the space of characters

**Proposition 2.6.** For \(\lambda\ge0\) the evaluation \(\mathrm{ev}_\lambda(f)=f(\lambda)\) is a morphism of
\(\mathbb{R}_{\max}\)-algebras \(\mathcal{R}(\mathbb{Z})\to\mathbb{R}_{\max}\). Every morphism of
\(\mathbb{R}_{\max}\)-algebras \(\chi\colon\mathcal{R}(\mathbb{Z})\to\mathbb{R}_{\max}\) is \(\mathrm{ev}_\lambda\) for
exactly one \(\lambda\in[0,\infty)\). Composition with the Frobenius \(f(\cdot)\mapsto f(n\,\cdot)\) sends
\(\mathrm{ev}_\lambda\) to \(\mathrm{ev}_{n\lambda}\).

*Proof.* The first and last statements are clear. Let \(\chi\) be a morphism of \(\mathbb{R}_{\max}\)-algebras, and
let \(\iota\in\mathcal{R}(\mathbb{Z})\) be the function \(\iota(\lambda)=\lambda\). The function \(-\iota\) also
belongs to \(\mathcal{R}(\mathbb{Z})\), and \(\iota+(-\iota)=0\) is the one of the semiring. So
\(\chi(\iota)+\chi(-\iota)=0\) and \(\lambda_0=\chi(\iota)\) is a real number. On \([0,\infty)\) we have
\(0\vee\iota=\iota\). Applying \(\chi\) gives \(\max(0,\lambda_0)=\lambda_0\), so \(\lambda_0\ge0\). Since \(\chi\) is
multiplicative and \(\mathbb{R}_{\max}\)-linear, \(\chi(x\iota+y)=x\lambda_0+y\) for \(x\in\mathbb{Z}\),
\(y\in\mathbb{R}\). Since \(\chi\) is additive,
\(\chi(\max_i(x_i\iota+y_i))=\max_i(x_i\lambda_0+y_i)\). So \(\chi=\mathrm{ev}_{\lambda_0}\). Finally
\(\lambda=\mathrm{ev}_\lambda(\iota)\) shows uniqueness. \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Proposition 2.2].

The restriction of \(\mathrm{ev}_\lambda\) to the image of \(\mathbb{Z}_{\max}\) is the morphism
\(x\mapsto\lambda x\) from \(\mathbb{Z}_{\max}\) to \(\mathbb{R}_{\max}\). For \(\lambda=0\) it takes its values in
\(\mathbb{B}\).

**Conclusion of Section 2.** Extension of scalars turns the pair \((\mathbb{Z}_{\max},\mathrm{Fr}_n)\) into a
semiring of functions on the half-line \([0,\infty)\), on which \(n\in\mathbb{N}^{\times}\) acts through
multiplication of the variable by \(n\). The geometric object behind this algebra is the half-line with the action of
\(\mathbb{N}^{\times}\), and functions that are convex, piecewise affine, with integral slopes. The next section
turns this into a topos with a sheaf of semirings.

## 3. The scaling site

### 3.1 The topos \([0,\infty)\rtimes\mathbb{N}^{\times}\)

**Definition 3.1.** An *object* is a bounded open interval of \([0,\infty)\) or the empty set. So the non-empty
objects are the sets \((\alpha,\beta)\) with \(0\le\alpha<\beta<\infty\) and the sets \([0,\beta)\) with
\(0<\beta<\infty\). The category \(\mathcal{C}\) has these objects. For \(\Omega\ne\emptyset\),

\[
\mathrm{Hom}_{\mathcal{C}}(\Omega,\Omega')=\{n\in\mathbb{N}^{\times}:n\Omega\subseteq\Omega'\},
\]

and \(\mathrm{Hom}_{\mathcal{C}}(\emptyset,\Omega')\) has one element. Composition is multiplication of integers. We
write \(n\colon\Omega\to\Omega'\). An inclusion \(\Omega\subseteq\Omega'\) is the morphism \(1\).

Note that \(n\Omega\) and \(n^{-1}\Omega=\{\lambda:n\lambda\in\Omega\}\) are objects when \(\Omega\) is, and that the
intersection of two objects is an object.

**Lemma 3.2 (fibre products).** Let \(n_j\colon\Omega_j\to\Omega\), \(j=1,2\), be morphisms between non-empty objects.
Let \(n=\mathrm{lcm}(n_1,n_2)=a_1n_1=a_2n_2\) and \(\Omega'=a_1^{-1}\Omega_1\cap a_2^{-1}\Omega_2\). Then
\(\Omega'\), with the morphisms \(a_j\colon\Omega'\to\Omega_j\), is the fibre product
\(\Omega_1\times_\Omega\Omega_2\) in \(\mathcal{C}\). In particular, for an inclusion \(\Omega_1\subseteq\Omega\) and
a morphism \(n\colon\Omega_2\to\Omega\), the fibre product is \(n^{-1}\Omega_1\cap\Omega_2\) with its inclusion into
\(\Omega_2\).

*Proof.* \(\Omega'\) is an object and \(n_1a_1=n_2a_2\). Let \(k_j\colon W\to\Omega_j\) be morphisms with
\(n_1k_1=n_2k_2\). If \(W=\emptyset\) there is nothing to prove. Otherwise \(n_1k_1=n_2k_2\) is a common multiple of
\(n_1\) and \(n_2\), so it equals \(mn\) with \(m\in\mathbb{N}^{\times}\), and \(k_j=ma_j\). For \(\lambda\in W\) we
have \(a_jm\lambda=k_j\lambda\in\Omega_j\), so \(mW\subseteq\Omega'\). Thus \(m\colon W\to\Omega'\) is a morphism with
\(a_jm=k_j\), and it is the only one. If \(\Omega'=\emptyset\), this shows that only \(W=\emptyset\) maps to both
\(\Omega_j\) compatibly, so the fibre product is the initial object \(\emptyset\). \(\blacksquare\)

**Definition 3.3.** A *covering family* of an object \(\Omega\) is a family of objects \(\Omega_i\subseteq\Omega\),
\(i\in I\), with \(\bigcup_i\Omega_i=\Omega\). The empty family covers the object \(\emptyset\). A *sheaf* on
\(\mathcal{C}\) is a functor \(\mathcal{G}\colon\mathcal{C}^{\mathrm{op}}\to\mathrm{Set}\) such that for every
covering family

\[
\mathcal{G}(\Omega)\longrightarrow\prod_i\mathcal{G}(\Omega_i)\rightrightarrows\prod_{i,j}\mathcal{G}(\Omega_i\cap\Omega_j)
\]

is an equalizer. In particular \(\mathcal{G}(\emptyset)\) has one element. The category of sheaves on
\(\mathcal{C}\) is written \([0,\infty)\rtimes\mathbb{N}^{\times}\). A *global section* of a sheaf \(\mathcal{G}\) is
a family \(s_\Omega\in\mathcal{G}(\Omega)\), one for each object, with \(\mathcal{G}(u)(s_{\Omega'})=s_\Omega\) for
every morphism \(u\colon\Omega\to\Omega'\).

The covering families satisfy the three conditions of a basis for a Grothendieck topology on \(\mathcal{C}\). These
conditions are those of [Connes–Consani 2017, Section 2.3]; they are also the axioms of a site in [Stacks, Tag [00VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-site)]. Indeed, the only
isomorphisms of \(\mathcal{C}\) are identities; by Lemma 3.2 the pullback of a covering family
\(\{\Omega_i\subseteq\Omega\}\) along \(n\colon\Omega'\to\Omega\) is the covering family
\(\{n^{-1}\Omega_i\cap\Omega'\subseteq\Omega'\}\); and a covering family of covering families is a covering family.
By Lemma 3.2 the fibre product of two members \(\Omega_i\), \(\Omega_j\) of a covering family of \(\Omega\) over
\(\Omega\) is \(\Omega_i\cap\Omega_j\). So the sheaves on this site in the sense of [Stacks, Tag [00VM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-sheaf-sets)] are the
functors described above, and \([0,\infty)\rtimes\mathbb{N}^{\times}\), being the category of sheaves on a site, is a
Grothendieck topos [Stacks, Tag [00XA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-topos)].

The name of the topos is explained by the next statement. An *\(\mathbb{N}^{\times}\)-equivariant sheaf* on the space
\([0,\infty)\) is a sheaf of sets \(\mathcal{F}\) on this space with maps
\(\alpha_n^{W}\colon\mathcal{F}(W)\to\mathcal{F}(n^{-1}W)\), for \(n\in\mathbb{N}^{\times}\) and \(W\) open, which
commute with restrictions and satisfy \(\alpha_1^{W}=\mathrm{id}\) and
\(\alpha_m^{\,n^{-1}W}\circ\alpha_n^{W}=\alpha_{nm}^{W}\). Morphisms are morphisms of sheaves that commute with the
maps \(\alpha\).

**Proposition 3.4.** The category \([0,\infty)\rtimes\mathbb{N}^{\times}\) is equivalent to the category of
\(\mathbb{N}^{\times}\)-equivariant sheaves on the space \([0,\infty)\).

*Proof.* Let \((\mathcal{F},\alpha)\) be an equivariant sheaf. Put \(\mathcal{G}(\Omega)=\mathcal{F}(\Omega)\), and
for \(n\colon\Omega\to\Omega'\) let \(\mathcal{G}(n)\) be \(\alpha_n^{\Omega'}\) followed by the restriction from
\(n^{-1}\Omega'\) to \(\Omega\). The identities for \(\alpha\) show that \(\mathcal{G}\) is a functor, and the sheaf
condition of Definition 3.3 is the sheaf condition of \(\mathcal{F}\) for covers of an interval by intervals.

Conversely let \(\mathcal{G}\) be a sheaf on \(\mathcal{C}\). The objects form a basis of the topology of
\([0,\infty)\) that is closed under finite intersections. The restriction of \(\mathcal{G}\) to inclusions is a sheaf
on this basis, so it extends to a sheaf \(\mathcal{F}\) on \([0,\infty)\), uniquely up to unique isomorphism
[Stacks, Tag [009H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-bases)]. For an object \(\Omega'\) the morphism \(n\colon n^{-1}\Omega'\to\Omega'\) gives a map
\(\mathcal{F}(\Omega')\to\mathcal{F}(n^{-1}\Omega')\). These maps commute with restrictions between objects, because
\(\mathcal{G}\) is a functor. So they define a morphism from \(\mathcal{F}\) to the sheaf
\(W\mapsto\mathcal{F}(n^{-1}W)\) on the basis, hence on all open sets. This gives the maps \(\alpha_n^{W}\). The two
identities hold on the basis, hence everywhere. Both constructions send morphisms to morphisms. They are inverse
to each other up to natural isomorphism, because \(n\colon\Omega\to\Omega'\) is the composite of the inclusion
\(\Omega\subseteq n^{-1}\Omega'\) and \(n\colon n^{-1}\Omega'\to\Omega'\). \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Proposition 2.5].

### 3.2 The structure sheaf

**Definition 3.5.** For an object \(\Omega\) let \(\mathcal{O}(\Omega)\) be the set of functions
\(f\colon\Omega\to\mathbb{R}_{\max}\) that are either constant equal to \(-\infty\) or belong to
\(\mathrm{CPA}_{\mathbb{Z}}(\Omega)\). For a morphism \(n\colon\Omega\to\Omega'\) let

\[
\mathcal{O}(n)\colon\mathcal{O}(\Omega')\to\mathcal{O}(\Omega),\qquad \mathcal{O}(n)(f)(\lambda)=f(n\lambda).
\]

With pointwise maximum as sum and pointwise addition as product, \(\mathcal{O}\) is a sheaf of semirings of
characteristic one on \(\mathcal{C}\), and the constants make it a sheaf of \(\mathbb{R}_{\max}\)-algebras. The
*scaling site* is the pair

\[
\mathscr{S}=\bigl([0,\infty)\rtimes\mathbb{N}^{\times},\ \mathcal{O}\bigr).
\]

We check the claims. By Lemma 1.2 each \(\mathcal{O}(\Omega)\) is closed under maximum and addition, so it is a
semiring with zero \(-\infty\) and one \(0\). If \(f\) has integral slopes and is convex, then
\(\lambda\mapsto f(n\lambda)\) has slopes in \(n\mathbb{Z}\subseteq\mathbb{Z}\) and is convex. So \(\mathcal{O}(n)\) is
well defined. It preserves maxima, sums and constants. Functoriality is clear. For the sheaf condition let
\(\Omega=\bigcup_i\Omega_i\) and let \(f_i\in\mathcal{O}(\Omega_i)\) agree on the intersections. The \(f_i\) glue to a
function \(f\) on \(\Omega\). The set where \(f=-\infty\) and the set where \(f\) is finite are open and disjoint.
Since \(\Omega\) is connected, \(f\) is constant \(-\infty\) or finite everywhere. In the second case
\(f\in\mathrm{CPA}_{\mathbb{Z}}(\Omega)\), because this is a local condition.

In the language of Proposition 3.4, \(\mathcal{O}\) is the sheaf on \([0,\infty)\) of convex piecewise affine
functions with integral slopes, and \(n\) acts by \(f(\lambda)\mapsto f(n\lambda)\).

**Proposition 3.6 (\(\mathcal{O}\) is generated by \(\mathcal{R}(\mathbb{Z})\)).** For every object \(\Omega\),
restriction of functions is a morphism of \(\mathbb{R}_{\max}\)-algebras
\(\mathcal{R}(\mathbb{Z})\to\mathcal{O}(\Omega)\), and it carries the Frobenius \(f(\cdot)\mapsto f(n\,\cdot)\) of
\(\mathcal{R}(\mathbb{Z})\) to the maps \(\mathcal{O}(n)\). A function \(f\colon\Omega\to\mathbb{R}\) belongs to
\(\mathcal{O}(\Omega)\) if and only if every point of \(\Omega\) has a neighbourhood in \(\Omega\) on which \(f\)
agrees with an element of \(\mathcal{R}(\mathbb{Z})\).

*Proof.* The first sentence follows from Lemma 2.3. If \(f\) agrees locally with elements of
\(\mathcal{R}(\mathbb{Z})\), then \(f\in\mathrm{CPA}_{\mathbb{Z}}(\Omega)\), since this is a local condition.
Conversely let \(f\in\mathrm{CPA}_{\mathbb{Z}}(\Omega)\) and \(\lambda_0\in\Omega\). Near \(\lambda_0>0\),

\[
f(\lambda)=\max\bigl(f(\lambda_0)+f'_-(\lambda_0)(\lambda-\lambda_0),\ f(\lambda_0)+f'_+(\lambda_0)(\lambda-\lambda_0)\bigr),
\]

because \(f'_-(\lambda_0)\le f'_+(\lambda_0)\). The right side is an element of \(\mathcal{R}(\mathbb{Z})\). Near
\(\lambda_0=0\) the function \(f\) is affine with integral slope. \(\blacksquare\)

**Example 3.7 (a section that is not the restriction of a global element).** On \(\Omega=[0,1)\) let
\(f(\lambda)=\sum_{k\ge1}\max(0,\lambda-1+2^{-k})\). Near each point of \(\Omega\) only finitely many terms are
non-zero, so \(f\in\mathcal{O}(\Omega)\). Its slopes are unbounded near \(1\). So \(f\) is not the restriction of an
element of \(\mathcal{R}(\mathbb{Z})\). The sheaf \(\mathcal{O}\) has sections that agree with elements of
\(\mathcal{R}(\mathbb{Z})\) only locally.

**Proposition 3.8 (global sections).** The global sections of \(\mathcal{O}\) are the constants. So the semiring of
global sections of \(\mathcal{O}\) is \(\mathbb{R}_{\max}\).

*Proof.* Let \((s_\Omega)\) be a global section. Compatibility with inclusions shows that the \(s_\Omega\) are the
restrictions of one function \(s\colon[0,\infty)\to\mathbb{R}_{\max}\). As in the check after Definition 3.5, \(s\) is
constant \(-\infty\) or finite and continuous. Compatibility with the morphisms \(n\colon[0,\beta)\to[0,n\beta)\)
gives \(s(n\lambda)=s(\lambda)\) for all \(\lambda\ge0\) and all \(n\). Hence \(s(\lambda)=s(\lambda/n)\) for all
\(n\), and \(s(\lambda/n)\to s(0)\) as \(n\to\infty\) by continuity at \(0\). So \(s\) is constant. Conversely every
constant is a global section. \(\blacksquare\)

For the arithmetic site the global sections of the structure sheaf \(\mathbb{Z}_{\max}\) form the semifield
\(\mathbb{B}\) (*The arithmetic site*, Proposition 3.3; [Connes–Consani 2016b, Proposition 3.5]). After extension of scalars the constants are
\(\mathbb{R}_{\max}\).

### 3.3 The scaling automorphisms

For \(\mu\in\mathbb{R}_{>0}\) let \(\tau_\mu\colon\mathcal{C}\to\mathcal{C}\) be the functor
\(\Omega\mapsto\mu\Omega\), which is the identity on morphisms. It is an automorphism of \(\mathcal{C}\) with inverse
\(\tau_{1/\mu}\), and it maps covering families to covering families. So \(\mathcal{G}\mapsto\mathcal{G}\circ\tau_\mu\)
is an automorphism of the category of sheaves.

**Proposition 3.9.** For \(\mu\in\mathbb{R}_{>0}\) the maps

\[
A_\mu\colon\mathcal{O}(\mu\Omega)\to\mathcal{O}(\Omega),\qquad A_\mu(f)(\lambda)=\mu^{-1}f(\mu\lambda)
\]

form an isomorphism of sheaves of semirings \(\mathcal{O}\circ\tau_\mu\to\mathcal{O}\). On constants it is
\(c\mapsto\mu^{-1}c\), the Frobenius automorphism \(\mathrm{Fr}_{1/\mu}\) of \(\mathbb{R}_{\max}\).

*Proof.* If \(f\in\mathrm{CPA}_{\mathbb{Z}}(\mu\Omega)\), then \(A_\mu(f)\) is convex and its slopes at \(\lambda\)
are the slopes of \(f\) at \(\mu\lambda\). So \(A_\mu(f)\in\mathrm{CPA}_{\mathbb{Z}}(\Omega)\). Since \(\mu^{-1}>0\),
\(A_\mu\) respects maximum and addition. It commutes with the maps \(\mathcal{O}(n)\), and
\(f\mapsto\mu f(\mu^{-1}\,\cdot)\) is its inverse. \(\blacksquare\)

So the group \(\mathbb{R}_{>0}\) acts on the scaling site by automorphisms that are semilinear over the Frobenius
automorphisms of \(\mathbb{R}_{\max}\). Without the factor \(\mu^{-1}\) the slopes would not stay integral. This is
the analogue of the action of the Galois group of \(\bar{\mathbb{F}}_q\) over \(\mathbb{F}_q\) on
\(\bar C=C\otimes_{\mathbb{F}_q}\bar{\mathbb{F}}_q\). We call it the *scaling action*.

## 4. The points of the topos

### 4.1 Points and flat functors

A *point* of a topos \(\mathcal{E}\) is a geometric morphism from the topos of sets to \(\mathcal{E}\). It is
determined by its inverse image functor \(p^{*}\colon\mathcal{E}\to\mathrm{Set}\), which preserves colimits and
finite limits. A morphism of points is a natural transformation between the inverse image functors. For a topos of
sheaves there is the following description.

**Theorem 4.1 (points of a topos of sheaves).** Let \(\mathcal{D}\) be a small category with a basis of a
Grothendieck topology. For a functor \(F\colon\mathcal{D}\to\mathrm{Set}\) consider the conditions:

- (F1) \(F(C)\neq\emptyset\) for some object \(C\).
- (F2) For \(a_1\in F(C_1)\) and \(a_2\in F(C_2)\) there are an object \(C\), an element \(a\in F(C)\) and morphisms
  \(u_j\colon C\to C_j\) with \(F(u_j)(a)=a_j\) for \(j=1,2\).
- (F3) For morphisms \(u,v\colon C\to D\) and \(a\in F(C)\) with \(F(u)(a)=F(v)(a)\) there are a morphism
  \(w\colon B\to C\) and \(b\in F(B)\) with \(u\circ w=v\circ w\) and \(F(w)(b)=a\).
- (F4) For every covering family \(\{C_i\to C\}\) of the basis, \(F(C)\) is the union of the images of the sets
  \(F(C_i)\).

Call \(F\) *flat* when (F1), (F2), (F3) hold and *continuous* when (F4) holds. Then:

1. The category of points of the topos of sheaves on \(\mathcal{D}\) is equivalent to the category of flat continuous
   functors \(\mathcal{D}\to\mathrm{Set}\) and their natural transformations.
2. Let the point \(p\) correspond to \(F\), and let \(\mathcal{G}\) be a sheaf. The set \(p^{*}\mathcal{G}\), called
   the *stalk* of \(\mathcal{G}\) at \(p\), is the set of triples \((C,a,s)\) with \(a\in F(C)\) and
   \(s\in\mathcal{G}(C)\), modulo the following equivalence relation: \((C_1,a_1,s_1)\sim(C_2,a_2,s_2)\) when there
   are an object \(C\), an element \(a\in F(C)\) and morphisms \(u_j\colon C\to C_j\) with \(F(u_j)(a)=a_j\) and
   \(\mathcal{G}(u_1)(s_1)=\mathcal{G}(u_2)(s_2)\).

Part (1) is stated in [Connes–Consani 2017, Section 3.1]; Lemma 3.2 of that work compares condition (F4) for the covering families
of a basis with continuity for the topology which the basis generates. For (2) see [Stacks, Tag [00Y3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-section-points)].
We derive the theorem from the description of the points of a site in the lesson
Topoi, morphisms and points of the course on étale cohomology.
A basis of a Grothendieck topology is a site in the sense of its prerequisite
Sites and sheaves: single isomorphisms are covering families, covering
families of covering families are covering families, and covering families pull back along every arrow, with fibre
products. Sheaves are taken for the covering families of the basis, as in Section 3.1. We need one fact about sets.

**Lemma on filtered colimits.** Let \(I\) be a *filtered* category: it is non-empty, for objects \(i,j\) there are
arrows \(i\to k\) and \(j\to k\) to some object \(k\), and for arrows \(f,g\colon i\to j\) there is \(h\colon j\to k\)
with \(hf=hg\).

1. For a functor \(X\colon I\to\mathrm{Set}\), two elements \(x\in X(i)\) and \(y\in X(j)\) have the same image in
   \(\varinjlim X\) if and only if \(X(f)x=X(g)y\) for some arrows \(f\colon i\to k\), \(g\colon j\to k\).
2. Colimits over \(I\) commute with finite limits: the canonical maps
   \(\varinjlim(X\times Y)\to\varinjlim X\times\varinjlim Y\) and, for natural maps \(a,b\colon X\to Y\),
   \(\varinjlim\mathrm{Eq}(a,b)\to\mathrm{Eq}(\varinjlim a,\varinjlim b)\) are bijective, and the colimit of the
   constant functor with value a point is a point.

*Proof.* (1) Write \((i,x)\sim(j,y)\) for the condition. It is reflexive and symmetric. If \((i,x)\sim(j,y)\) through
\(i\to k\leftarrow j\) and \((j,y)\sim(l,z)\) through \(j\to m\leftarrow l\), choose arrows \(k\to n\) and \(m\to n\),
then an arrow \(n\to n'\) that equalizes the two composite arrows \(j\to n\); the composites \(i\to n'\) and
\(l\to n'\) show \((i,x)\sim(l,z)\). The colimit is the quotient of \(\coprod_iX(i)\) by the equivalence relation
generated by \((i,x)\approx(j,X(f)x)\) for \(f\colon i\to j\). The relation \(\sim\) contains these pairs, and it is
contained in the generated relation, because \(X(f)x=X(g)y\) gives \((i,x)\approx(k,X(f)x)=(k,X(g)y)\approx(j,y)\).
Being an equivalence relation, \(\sim\) is the generated one.

(2) The category \(I\) is non-empty and any two objects are joined by arrows to a common object, so the colimit of a
point is a point. Products: two elements of \(\varinjlim X\) and \(\varinjlim Y\) are represented at a common object,
so the map is surjective. If \((x,y)\in X(i)\times Y(i)\) and \((x',y')\in X(j)\times Y(j)\) have the same image, (1)
gives \(f_1\colon i\to k_1\), \(g_1\colon j\to k_1\) with \(X(f_1)x=X(g_1)x'\) and \(f_2\colon i\to k_2\),
\(g_2\colon j\to k_2\) with \(Y(f_2)y=Y(g_2)y'\). Map \(k_1\) and \(k_2\) to a common \(k\), and follow with an arrow
that equalizes the two resulting arrows \(i\to k\) and then with one that equalizes the two resulting arrows
\(j\to k\). The final arrows \(i\to k''\) and \(j\to k''\) identify \((x,y)\) with \((x',y')\). Equalizers:
\(\mathrm{Eq}(a,b)(i)\subseteq X(i)\), and by (1) two of its elements that agree in \(\varinjlim X\) already agree
in \(\varinjlim\mathrm{Eq}(a,b)\), since the images of an element of \(\mathrm{Eq}(a,b)(i)\) stay in
\(\mathrm{Eq}(a,b)\); so the map is injective. If \(x\in X(i)\) has \(a(x)\) and \(b(x)\) equal in \(\varinjlim Y\),
then by (1) \(Y(f)a(x)=Y(g)b(x)\) for some \(f,g\colon i\to k\); an arrow \(h\colon k\to k'\) with \(hf=hg\) gives
\(a(X(hf)x)=b(X(hf)x)\), so the class of \(x\) comes from \(\mathrm{Eq}(a,b)(k')\). Finite limits are built from a
terminal object, binary products and equalizers. \(\blacksquare\)

*Proof of Theorem 4.1.* For a functor \(F\colon\mathcal{D}\to\mathrm{Set}\), let \(N_F\) be the category of pairs
\((C,a)\) with \(a\in F(C)\), an arrow \((B,b)\to(C,a)\) being a morphism \(w\colon B\to C\) with \(F(w)b=a\). For a
presheaf \(\mathcal{G}\) put \(\mathcal{G}_F=\varinjlim\mathcal{G}(C)\), the colimit over the opposite category
\(N_F^{\mathrm{op}}\). Conditions (F1), (F2) and (F3) say exactly that \(N_F^{\mathrm{op}}\) is filtered. In the lesson
on topoi, \(F\) is a *point of the site* if (i) it takes covering families to jointly surjective families, (ii) the
map \(F(C_i\times_CB)\to F(C_i)\times_{F(C)}F(B)\) is bijective for every member \(C_i\to C\) of a covering family and
every arrow \(B\to C\), and (iii) \(\mathcal{G}\mapsto\mathcal{G}_F\) preserves finite limits of sheaves. Its
Theorem 4.1 shows that such an \(F\) defines a point \(p_F\) with \(p_F^{*}\mathcal{G}=\mathcal{G}_F\), that every
point \(p\) arises from the point of the site \(C\mapsto p^{*}(h_C^{\#})\), where \(h_C^{\#}\) is the sheaf associated
with the presheaf represented by \(C\), and that the two constructions are inverse to each other up to natural
isomorphism. Its proof also shows that \((h_C)_F=F(C)\), naturally in \(C\), and that sheafification does not change
\(\mathcal{G}_F\) when \(F\) is a point of the site.

*Flat continuous functors are points of the site.* Let \(F\) be flat and continuous. Condition (i) is (F4). By the
lemma on filtered colimits, \(\mathcal{G}\mapsto\mathcal{G}_F\) preserves finite limits of presheaves; limits of
sheaves are computed on sections (Sites and sheaves, Theorem 4.2), so
(iii) holds. The presheaf represented by \(C_i\times_CB\) is the fibre product of those represented by \(C_i\) and
\(B\) over the one represented by \(C\). Applying \(\mathcal{G}\mapsto\mathcal{G}_F\), which preserves fibre products,
gives (ii). Moreover \(p_F^{*}(h_C^{\#})=(h_C)_F=F(C)\).

*The functor of a point is flat and continuous.* Let \(p\) be a point and \(F(C)=p^{*}(h_C^{\#})\). By Theorem 4.1 of
the lesson on topoi, \(F\) is a point of the site, so (F4) holds. Sheafification preserves finite limits
(Sites and sheaves, Theorem 3.3), and \(p^{*}\) does by definition; both
preserve colimits and epimorphisms, being left adjoints. A map of presheaves that is surjective on every set of
sections is an epimorphism. Hence such a map becomes a surjection of sets after sheafification and \(p^{*}\).
(F1): the map \(\coprod_Ch_C\to1\) to the terminal presheaf is surjective on sections, so \(\coprod_CF(C)\to p^{*}(1)\),
a map to a point, is surjective, and some \(F(C)\) is non-empty. (F2): the map \(\coprod h_B\to h_{C_1}\times h_{C_2}\),
over the triples \((B,u_1,u_2)\) with \(u_j\colon B\to C_j\), is surjective on sections. It becomes a surjection
\(\coprod F(B)\to F(C_1)\times F(C_2)\) with components \((F(u_1),F(u_2))\), which is (F2). (F3): for
\(u,v\colon C\to D\) the equalizer \(E\) of the represented maps consists of the arrows \(w\colon B\to C\) with
\(uw=vw\), and \(\coprod h_B\to E\), over these \(w\), is surjective on sections. Since \(p^{*}\) and sheafification
preserve the equalizer, it becomes a surjection \(\coprod F(B)\to\{a\in F(C):F(u)a=F(v)a\}\) with components \(F(w)\),
which is (F3).

*Morphisms.* A morphism of points \(\theta\colon p^{*}\to q^{*}\) restricts to a natural transformation between the
functors \(C\mapsto p^{*}(h_C^{\#})\) and \(C\mapsto q^{*}(h_C^{\#})\). Every sheaf is, naturally, a colimit of sheaves
\(h_C^{\#}\) (presentation (1.1) of the lesson on topoi), and \(p^{*}\), \(q^{*}\) preserve colimits; so every natural
transformation between the restricted functors extends uniquely to a morphism of points. So
\(p\mapsto(C\mapsto p^{*}(h_C^{\#}))\) is fully faithful, and by the two preceding steps every flat continuous functor
is isomorphic to a functor in its image. This proves (1).

(2) By (1), \(p^{*}\mathcal{G}=\mathcal{G}_F\) is a colimit over the filtered category \(N_F^{\mathrm{op}}\), and
part (1) of the lemma on filtered colimits describes when two triples \((C,a,s)\) define the same element. Arrows
\(u_j\colon(C,a)\to(C_j,a_j)\) of \(N_F\) with \(\mathcal{G}(u_1)(s_1)=\mathcal{G}(u_2)(s_2)\) are exactly the
relation of (2). \(\blacksquare\)

The stalk functor preserves finite products. So the stalk of a sheaf of semirings is a semiring: two elements of the
stalk can be written over the same pair \((C,a)\) by (F2), and they are added and multiplied there.

We apply this to the category \(\mathcal{C}\) of Definition 3.1. "Flat" and "continuous" now refer to
\(\mathcal{C}\).

### 4.2 Two families of points

**Definition 4.2.**

1. Let \(H\) be a rank one subgroup of \(\mathbb{R}\). Define \(F_H\colon\mathcal{C}\to\mathrm{Set}\) by
   \(F_H(\Omega)=\Omega\cap H_+\) and \(F_H(n)(h)=nh\).
2. Let \(H\) be a rank one ordered group and \(H_{>0}\) its set of positive elements. Define
   \(F'_H\colon\mathcal{C}\to\mathrm{Set}\) by \(F'_H(\Omega)=H_{>0}\) if \(0\in\Omega\) and
   \(F'_H(\Omega)=\emptyset\) otherwise, and \(F'_H(n)(h)=nh\).

Both are functors: if \(n\Omega\subseteq\Omega'\), then multiplication by \(n\) maps \(\Omega\cap H_+\) into
\(\Omega'\cap H_+\), and \(0\in\Omega\) implies \(0\in\Omega'\).

**Proposition 4.3.** The functors \(F_H\) and \(F'_H\) are flat and continuous. We write \(\mathfrak{p}_H\) and
\(\mathfrak{q}_H\) for the corresponding points of \([0,\infty)\rtimes\mathbb{N}^{\times}\).

*Proof.* *The functor \(F_H\).* (F1): \(H_+\neq\emptyset\), and every element of \(H_+\) lies in some object.
(F2): let \(h_j\in\Omega_j\cap H_+\). By Lemma 1.1 there are \(g\in H_+\) and \(n_j\in\mathbb{N}^{\times}\) with
\(h_j=n_jg\). The set \(W=n_1^{-1}\Omega_1\cap n_2^{-1}\Omega_2\cap(g/2,2g)\) is an object containing \(g\), and
\(n_j\colon W\to\Omega_j\) sends \(g\) to \(h_j\). (F3): if \(F_H(n)(h)=F_H(m)(h)\), then \(nh=mh\) with \(h>0\),
so \(n=m\) and we can take \(w\) to be the identity. (F4): if \(\Omega=\bigcup_i\Omega_i\), then
\(\Omega\cap H_+=\bigcup_i(\Omega_i\cap H_+)\); for \(\Omega=\emptyset\) both sides are empty.

*The functor \(F'_H\).* We may take \(H\subseteq\mathbb{Q}\). (F1) is clear. (F2): let \(h_j\in F'_H(\Omega_j)\),
so \(0\in\Omega_j\). Write \(h_j=n_jg\) as before. For small \(\beta>0\) the object \(W=[0,\beta)\) satisfies
\(n_jW\subseteq\Omega_j\), and \(n_j\colon W\to\Omega_j\) sends \(g\in F'_H(W)\) to \(h_j\). (F3) is proved as for
\(F_H\). (F4): if \(0\in\Omega=\bigcup_i\Omega_i\), then \(0\in\Omega_i\) for some \(i\), and
\(F'_H(\Omega_i)\to F'_H(\Omega)\) is the identity of \(H_{>0}\). If \(0\notin\Omega\), then
\(F'_H(\Omega)=\emptyset\). \(\blacksquare\)

Here is how to picture these points. The point \(\mathfrak{p}_H\) sees the half-line through the multiples in
\(H\): the set \(F_H(\Omega)\) consists of the elements of \(H\) in \(\Omega\), and the morphism \(n\) multiplies
them by \(n\). The point \(\mathfrak{q}_H\) sits over \(0\in[0,\infty)\).

### 4.3 The classification

In this subsection \(F\colon\mathcal{C}\to\mathrm{Set}\) is a flat continuous functor.

**Lemma 4.4.**

1. \(F(\emptyset)=\emptyset\).
2. If \(n,m\colon W\to V\) are morphisms and \(c\in F(W)\) satisfies \(F(n)(c)=F(m)(c)\), then \(n=m\).

*Proof.* (1) Apply (F4) to the empty covering family of \(\emptyset\). (2) By (F3) there are \(w\colon B\to W\) and
\(b\in F(B)\) with \(n\circ w=m\circ w\) and \(F(w)(b)=c\). By (1), \(B\neq\emptyset\). So \(w\) is a positive
integer and \(nw=mw\) as integers. Hence \(n=m\). \(\blacksquare\)

Let \(V\) be an object and \(x\in F(V)\). We say that an object \(U\subseteq V\) *carries* \(x\) when \(x\) lies in
the image of \(F(U)\to F(V)\).

**Lemma 4.5 (the position of an element).**

1. If \(U\) and \(U'\) carry \(x\), then \(U\cap U'\) carries \(x\). In particular \(U\cap U'\neq\emptyset\).
2. There is exactly one point \(\lambda_V(x)\in V\) such that every object \(U\) with
   \(\lambda_V(x)\in U\subseteq V\) carries \(x\).

*Proof.* (1) Let \(x\) be the image of \(y\in F(U)\) and of \(y'\in F(U')\). By (F2) there are an object \(W\),
an element \(c\in F(W)\) and morphisms \(n\colon W\to U\), \(n'\colon W\to U'\) with \(F(n)(c)=y\) and
\(F(n')(c)=y'\). The composites \(n,n'\colon W\to V\) both send \(c\) to \(x\). By Lemma 4.4, \(n=n'\). So
\(nW\subseteq U\cap U'\), and \(x\) is the image of \(F(n\colon W\to U\cap U')(c)\). Since
\(F(\emptyset)=\emptyset\), the object \(U\cap U'\) is not empty.

(2) *Existence.* Suppose that every \(\lambda\in V\) lies in an object \(U_\lambda\subseteq V\) that does not carry
\(x\). The \(U_\lambda\) form a covering family of \(V\). By (F4) one of them carries \(x\), a contradiction.
*Uniqueness.* If \(\lambda\neq\lambda'\) both have the property, choose disjoint objects \(U\ni\lambda\) and
\(U'\ni\lambda'\) inside \(V\). Both carry \(x\), which contradicts (1). \(\blacksquare\)

**Lemma 4.6 (naturality of the position).**

1. For a morphism \(n\colon U\to V\) and \(x\in F(U)\): \(\lambda_V(F(n)(x))=n\,\lambda_U(x)\).
2. Let \(\theta\colon F\to F'\) be a natural transformation between flat continuous functors, with position maps
   \(\lambda\) and \(\lambda'\). Then \(\lambda'_V(\theta_V(x))=\lambda_V(x)\).

*Proof.* (1) Put \(\lambda=\lambda_U(x)\) and \(y=F(n)(x)\). Let \(A\) be an object with \(n\lambda\in A\subseteq V\).
The object \(W=U\cap n^{-1}A\) contains \(\lambda\), so \(x=F(W\subseteq U)(w)\) for some \(w\in F(W)\). Then
\(y=F(n\colon W\to V)(w)\) is the image of \(F(n\colon W\to A)(w)\in F(A)\). So \(A\) carries \(y\). This holds for
every such \(A\), so \(\lambda_V(y)=n\lambda\) by the uniqueness in Lemma 4.5.

(2) If \(U\) carries \(x\), say \(x=F(U\subseteq V)(y)\), then
\(\theta_V(x)=F'(U\subseteq V)(\theta_U(y))\), so \(U\) carries \(\theta_V(x)\). Hence every object \(U\) with
\(\lambda_V(x)\in U\subseteq V\) carries \(\theta_V(x)\), and uniqueness gives the claim. \(\blacksquare\)

**Lemma 4.7 (two cases).** Either \(\lambda_V(x)>0\) for all objects \(V\) and all \(x\in F(V)\), or
\(\lambda_V(x)=0\) for all \(V\) and all \(x\in F(V)\).

*Proof.* Let \(x_1\in F(V_1)\) and \(x_2\in F(V_2)\). By (F2) there are \(W\), \(c\in F(W)\) and
\(n_j\colon W\to V_j\) with \(F(n_j)(c)=x_j\). By Lemma 4.6, \(\lambda_{V_j}(x_j)=n_j\lambda_W(c)\). Both numbers are
zero or both are positive. \(\blacksquare\)

**Lemma 4.8 (the first case).** Suppose \(\lambda_V(x)>0\) for all \(V\) and \(x\). Let \(E\subseteq(0,\infty)\) be
the set of all values \(\lambda_V(x)\). Then \(H=E\cup\{0\}\cup(-E)\) is a rank one subgroup of \(\mathbb{R}\) with
\(H_+=E\), and the maps \(\lambda_V\) form an isomorphism of functors \(F\to F_H\).

*Proof.* *Each \(\lambda_V\) is injective.* Let \(\lambda_V(x_1)=\lambda_V(x_2)\). Take \(W\), \(c\), \(n_j\) as in
(F2) for \(x_1,x_2\). Then \(n_1\lambda_W(c)=n_2\lambda_W(c)\) and \(\lambda_W(c)>0\), so \(n_1=n_2\) and
\(x_1=x_2\).

*The image of \(\lambda_V\) is \(V\cap E\).* Let \(\mu\in V\cap E\), say \(\mu=\lambda_{V'}(x')\). The object
\(U=V\cap V'\) contains \(\mu\), so \(x'=F(U\subseteq V')(z)\) with \(z\in F(U)\). By Lemma 4.6,
\(\lambda_U(z)=\mu\) and \(\lambda_V(F(U\subseteq V)(z))=\mu\).

*\(H\) is a rank one subgroup.* \(E\neq\emptyset\) by (F1). If \(\mu=\lambda_V(x)\in E\) and
\(n\in\mathbb{N}^{\times}\), then \(n\mu=\lambda_{nV}(F(n\colon V\to nV)(x))\in E\). Let \(\mu_1,\mu_2\in E\). Choose
an object \(V\) containing both and \(x_j\in F(V)\) with \(\lambda_V(x_j)=\mu_j\). Take \(W\), \(c\), \(n_j\) as in
(F2). Then \(\mu_j=n_j\nu\) with \(\nu=\lambda_W(c)\in E\). So \(\mu_1+\mu_2=(n_1+n_2)\nu\in E\), and
\(\mu_1-\mu_2=(n_1-n_2)\nu\) lies in \(E\), in \(-E\) or is \(0\). Hence \(H\) is a subgroup, any two of its non-zero
elements have a rational ratio, and \(H_+=E\).

So \(\lambda_V\colon F(V)\to V\cap H_+=F_H(V)\) is a bijection for every \(V\). These bijections are natural by
Lemma 4.6. \(\blacksquare\)

For the second case we recall a result of *The arithmetic site*. A set \(X\) with an action of
\(\mathbb{N}^{\times}\) is *flat* when \(X\neq\emptyset\), any two elements of \(X\) are of the form
\(n_1\cdot c\), \(n_2\cdot c\) for one \(c\in X\), and \(n\cdot x=m\cdot x\) implies \(n=m\). Every flat
\(\mathbb{N}^{\times}\)-set is isomorphic to \(H_{>0}\) for a non-zero subgroup \(H\subseteq\mathbb{Q}\), with \(n\)
acting by multiplication. Every \(\mathbb{N}^{\times}\)-equivariant map \(H_{>0}\to H'_{>0}\) is the multiplication
by a positive rational number \(r\) with \(rH\subseteq H'\) (*The arithmetic site*, Theorem 2.2; [Connes–Consani 2016b, Theorem 2.1]). In particular
\(H_{>0}\) and \(H'_{>0}\) are isomorphic \(\mathbb{N}^{\times}\)-sets exactly when \(H\) and \(H'\) are isomorphic
ordered groups.

**Lemma 4.9 (the second case).** Suppose \(\lambda_V(x)=0\) for all \(V\) and \(x\). Then \(F\) is isomorphic to
\(F'_H\) for a rank one ordered group \(H\).

*Proof.* *Step 1.* If \(0\notin V\), then \(F(V)=\emptyset\), because \(\lambda_V(x)\in V\). Let
\(0\in U\subseteq V\). The map \(F(U)\to F(V)\) is surjective, because \(U\) contains \(0=\lambda_V(x)\) and so
carries every \(x\in F(V)\). It is injective: if \(y_1,y_2\in F(U)\) have the same image \(x\), take \(W\), \(c\),
\(n_j\colon W\to U\) as in (F2) for \(y_1,y_2\). Then \(n_1,n_2\colon W\to V\) both send \(c\) to \(x\), so
\(n_1=n_2\) by Lemma 4.4 and \(y_1=y_2\).

*Step 2.* Put \(X=F([0,1))\). For an object \(V\ni0\) let \(U=V\cap[0,1)\) and let \(\beta_V\colon X\to F(V)\) be
the bijection \(F(U\subseteq V)\circ F(U\subseteq[0,1))^{-1}\). For \(0\in V\subseteq V'\) one has
\(F(V\subseteq V')\circ\beta_V=\beta_{V'}\). This follows from the functoriality of \(F\) on the inclusions
\(V\cap[0,1)\subseteq V'\cap[0,1)\subseteq[0,1)\) and \(V\cap[0,1)\subseteq V\subseteq V'\).

Let \(n\colon U\to V\) be a morphism between objects containing \(0\). The map
\(\beta_V^{-1}\circ F(n)\circ\beta_U\colon X\to X\) depends only on \(n\). Indeed, for a second such morphism
\(n\colon U'\to V'\), the set \(V\cup V'\) is an object and \(n\colon U\cap U'\to V\cup V'\) is the composite of
\(U\cap U'\subseteq U\), \(n\colon U\to V\) and \(V\subseteq V\cup V'\). With the compatibility of \(\beta\) with
inclusions this gives

\[
\beta_{V\cup V'}^{-1}\circ F(n\colon U\cap U'\to V\cup V')\circ\beta_{U\cap U'}=\beta_V^{-1}\circ F(n\colon U\to V)\circ\beta_U ,
\]

and the same with \((U',V')\) in place of \((U,V)\). Write \(x\mapsto n\cdot x\) for this map. Composing morphisms
shows \((nm)\cdot x=n\cdot(m\cdot x)\) and \(1\cdot x=x\). So \(X\) is an \(\mathbb{N}^{\times}\)-set. Let \(F'_X\)
be the functor with \(F'_X(V)=X\) if \(0\in V\), \(F'_X(V)=\emptyset\) otherwise, and \(F'_X(n)(x)=n\cdot x\). By
construction the maps \(\beta_V\) form an isomorphism \(F'_X\to F\).

*Step 3.* The \(\mathbb{N}^{\times}\)-set \(X\) is flat. It is not empty by (F1) and Step 1. Two elements of \(X\)
are of the form \(n_1\cdot c\), \(n_2\cdot c\) by (F2) for \(F'_X\cong F\). If \(n\cdot x=m\cdot x\), then
\(n,m\colon[0,1)\to[0,n+m)\) send the same element of \(F([0,1))\) to the same element, so \(n=m\) by Lemma 4.4.
By the recalled result, \(X\cong H_{>0}\) for a rank one ordered group \(H\), and then
\(F\cong F'_X\cong F'_H\). \(\blacksquare\)

**Theorem 4.10 (the points of \([0,\infty)\rtimes\mathbb{N}^{\times}\)).**

1. Every flat continuous functor on \(\mathcal{C}\) is isomorphic to \(F_H\) for exactly one rank one subgroup
   \(H\subseteq\mathbb{R}\), or to \(F'_H\) for a rank one ordered group \(H\) that is unique up to isomorphism. The
   two cases exclude each other.
2. There is a natural transformation \(F_H\to F_{H'}\) if and only if \(H\subseteq H'\); it is then unique and is
   the inclusion. The natural transformations \(F'_H\to F'_{H'}\) are the \(\mathbb{N}^{\times}\)-equivariant maps
   \(H_{>0}\to H'_{>0}\). There is no natural transformation between a functor \(F_H\) and a functor \(F'_{H'}\),
   in either direction.

So the set of isomorphism classes of points of \([0,\infty)\rtimes\mathbb{N}^{\times}\) is the disjoint union of the
set of rank one subgroups of \(\mathbb{R}\) and the set of isomorphism classes of rank one ordered groups. The second
set is the set of isomorphism classes of points of the topos of \(\mathbb{N}^{\times}\)-sets.

*Proof.* (2) For \(F_H\) the position map is \(\lambda_V(h)=h\): every object \(U\) with \(h\in U\subseteq V\) has
\(h\in F_H(U)\). For \(F'_H\) the position map is \(\lambda_V(h)=0\). Let \(\theta\colon F_H\to F_{H'}\) be natural.
By Lemma 4.6, \(\theta_V(h)=h\). So \(V\cap H_+\subseteq V\cap H'_+\) for all \(V\), that is \(H\subseteq H'\), and
\(\theta\) is the inclusion. Conversely the inclusion is natural. A natural transformation
\(\theta\colon F'_H\to F'_{H'}\) consists of maps \(\theta_V\colon H_{>0}\to H'_{>0}\) for \(V\ni0\). Naturality for
inclusions says that they are all equal, and naturality for the morphisms \(n\) says that the common map is
equivariant. A natural transformation between \(F_H\) and \(F'_{H'}\) would map an element with position \(>0\) to
an element with position \(0\), or conversely. This contradicts Lemma 4.6.

(1) Existence is Lemmas 4.7, 4.8 and 4.9. Uniqueness follows from (2): if \(F_H\cong F_{H'}\), then \(H\subseteq H'\)
and \(H'\subseteq H\); if \(F'_H\cong F'_{H'}\), then \(H_{>0}\cong H'_{>0}\) as \(\mathbb{N}^{\times}\)-sets, so
\(H\cong H'\). \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 3.9].

### 4.4 The adèle class space

We recall from *The arithmetic site* the adelic description of the subgroups of \(\mathbb{Q}\). Let
\(\mathbb{A}^{f}\) be the ring of finite adèles of \(\mathbb{Q}\), let
\(\widehat{\mathbb{Z}}=\prod_\ell\mathbb{Z}_\ell\subset\mathbb{A}^{f}\), and let \(\widehat{\mathbb{Z}}^{\times}\) be
its group of invertible elements. The field \(\mathbb{Q}\) is embedded diagonally in \(\mathbb{A}^{f}\). For
\(a\in\mathbb{A}^{f}\) put

\[
H_a=\{q\in\mathbb{Q}:qa\in\widehat{\mathbb{Z}}\}.
\]

Then \(a\mapsto H_a\) induces a bijection from \(\mathbb{A}^{f}/\widehat{\mathbb{Z}}^{\times}\) onto the set of
non-zero subgroups of \(\mathbb{Q}\) (*The arithmetic site*, Proposition 2.4; [Connes–Consani 2016b, Proposition 2.5]). For \(q\in\mathbb{Q}^{\times}\) the
definition gives \(H_{qa}=q^{-1}H_a\). In terms of the components \(a_\ell\in\mathbb{Q}_\ell\) and the valuations
\(v_\ell\), one has \(H_a=\{q:v_\ell(q)+v_\ell(a_\ell)\ge0\text{ for all primes }\ell\}\), with
\(v_\ell(0)=+\infty\).

The ring of adèles is \(\mathbb{A}_{\mathbb{Q}}=\mathbb{A}^{f}\times\mathbb{R}\). The group \(\mathbb{Q}^{\times}\)
acts on it diagonally, and \(\widehat{\mathbb{Z}}^{\times}\) acts on the first factor. Let

\[
X_{\mathbb{Q}}=\mathbb{Q}^{\times}\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb{Z}}^{\times}.
\]

The group \(\mathbb{R}_{>0}\) acts on \(X_{\mathbb{Q}}\) by \(\mu\cdot[a,x]=[a,\mu x]\). On the other side,
\(\mathbb{R}_{>0}\) acts on the points of the topos through the automorphisms \(\tau_\mu\) of Section 3.3: the point
with functor \(F\) is sent to the point with functor \(F\circ\tau_{1/\mu}\). Since
\(\mu^{-1}\Omega\cap H_+\) is identified with \(\Omega\cap\mu H_+\) by \(h\mapsto\mu h\), this sends
\(\mathfrak{p}_H\) to \(\mathfrak{p}_{\mu H}\). It fixes \(\mathfrak{q}_H\), because \(0\in\mu^{-1}\Omega\) exactly
when \(0\in\Omega\).

**Theorem 4.11 (points and adèle classes).** Define \(\Phi(a,x)=\mathfrak{p}_{|x|H_a}\) for \(x\neq0\) and
\(\Phi(a,0)=\mathfrak{q}_{H_a}\). Then \(\Phi\) induces a bijection from \(X_{\mathbb{Q}}\) onto the set of
isomorphism classes of points of \([0,\infty)\rtimes\mathbb{N}^{\times}\). It carries the action of
\(\mathbb{R}_{>0}\) on \(X_{\mathbb{Q}}\) to the scaling action on points. The fixed points of the scaling action are
the points \(\mathfrak{q}_H\); they are the classes of the adèles with archimedean component \(0\).

*Proof.* *\(\Phi\) is constant on classes.* Let \(q\in\mathbb{Q}^{\times}\) and
\(u\in\widehat{\mathbb{Z}}^{\times}\). Then \(H_{qau}=q^{-1}H_a=|q|^{-1}H_a\), because \(H_a=-H_a\). For
\(x\neq0\) this gives \(|qx|H_{qau}=|x|H_a\). For \(x=0\), multiplication by \(|q|\) is an isomorphism of ordered
groups from \(H_{qau}\) to \(H_a\), so \(\mathfrak{q}_{H_{qau}}\cong\mathfrak{q}_{H_a}\).

*Surjective.* Let \(H\) be a rank one subgroup of \(\mathbb{R}\) and \(h_0\in H_+\). Then \(h_0^{-1}H\) is a
non-zero subgroup of \(\mathbb{Q}\), so it equals \(H_a\) for some \(a\), and \(H=h_0H_a\) gives
\(\mathfrak{p}_H=\Phi(a,h_0)\). A rank one ordered group is isomorphic to some \(H_a\), so
\(\mathfrak{q}_H\cong\Phi(a,0)\). By Theorem 4.10 these are all the points.

*Injective.* Let \(\Phi(a,x)\cong\Phi(b,y)\). By Theorem 4.10 either \(x,y\neq0\) and \(|x|H_a=|y|H_b\), or
\(x=y=0\) and \(H_a\cong H_b\) as ordered groups. In the first case choose \(h\in H_a\), \(h\neq0\). Then
\(|x|h=|y|h'\) for some \(h'\in H_b\), so \(r=|x|/|y|=h'/h\) lies in \(\mathbb{Q}_{>0}\). Then
\(H_b=rH_a=H_{r^{-1}a}\), so \(b=r^{-1}au\) with
\(u\in\widehat{\mathbb{Z}}^{\times}\). Choose the sign \(\epsilon=\pm1\) with \(\epsilon r^{-1}x=y\). Then
\((b,y)=(\epsilon r^{-1})\cdot(a,x)\cdot(\epsilon u)\), and \(\epsilon u\in\widehat{\mathbb{Z}}^{\times}\). In the
second case an isomorphism \(H_a\to H_b\) of ordered groups is the multiplication by a rational number \(r>0\) by
Lemma 1.1. So \(H_b=rH_a\), and \((b,0)=r^{-1}\cdot(a,0)\cdot u\) as before.

*The actions.* \(\Phi(a,\mu x)=\mathfrak{p}_{\mu|x|H_a}\) for \(x\neq0\), and \(\Phi(a,0)\) does not change.
No point \(\mathfrak{p}_H\) is fixed by all \(\mu\), since \(\mu H=H\) forces \(\mu\in\mathbb{Q}\).
\(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 3.9]; [Connes–Consani 2016b, Lemma 3.7 and Theorem 3.8].

**Example 4.12.** (a) Let \(a=1\). Then \(H_1=\mathbb{Z}\), and the classes \([1,x]\) with \(x>0\) give the points
\(\mathfrak{p}_{x\mathbb{Z}}\). Here \(F_{x\mathbb{Z}}(\Omega)\) is the set of positive multiples of \(x\) in
\(\Omega\). The scaling action is free on these points, because \(\mu x\mathbb{Z}=x\mathbb{Z}\) with \(\mu>0\) forces
\(\mu=1\).

(b) Let \(a=0\). Then \(H_0=\mathbb{Q}\), and the classes \([0,x]\) give the points \(\mathfrak{p}_{x\mathbb{Q}}\).
Here \(\mu x\mathbb{Q}=x\mathbb{Q}\) for all \(\mu\in\mathbb{Q}_{>0}\).

(c) The class \([1,0]\) gives \(\mathfrak{q}_{\mathbb{Z}}\), and the class \([0,0]\) gives
\(\mathfrak{q}_{\mathbb{Q}}\). Both are fixed by the scaling action.

(d) A subgroup such as \(\mathbb{Z}+\mathbb{Z}\sqrt2\) gives no point: see Exercise 2.

## 5. Stalks, points over \(\mathbb{R}_{\max}\), and the order of a function

### 5.1 The stalks of the structure sheaf

Let \(H\) be a rank one subgroup of \(\mathbb{R}\). A *germ at \(1\) with slopes in \(H\)* is the germ at \(t=1\) of
a function in \(\mathrm{PA}_H(U)\), for an open interval \(U\ni1\). Such a germ is given by a triple
\((x,a_-,a_+)\in\mathbb{R}\times H\times H\): the function is \(x+a_+(t-1)\) for \(t\ge1\) and \(x+a_-(t-1)\) for
\(t\le1\), near \(1\). Let

\[
\mathcal{R}_H=\{-\infty\}\cup\{\text{germs at }1\text{ with slopes in }H\text{ and }a_-\le a_+\},
\]

with maximum as sum and addition as product. It is an \(\mathbb{R}_{\max}\)-algebra.

Let \(H\) be a rank one ordered group. Order \(\mathbb{R}\times H\) lexicographically: \((x,h)<(x',h')\) when
\(x<x'\), or \(x=x'\) and \(h<h'\). This is a totally ordered abelian group. Let
\(\mathcal{Z}_H=(\mathbb{R}\times H)_{\max}\). It is a semifield, and \(c\mapsto(c,0)\) makes it an
\(\mathbb{R}_{\max}\)-algebra.

**Theorem 5.1 (stalks of \(\mathcal{O}\)).**

1. Let \(H\) be a rank one subgroup of \(\mathbb{R}\). Sending a triple \((\Omega,h,f)\), with
   \(h\in\Omega\cap H_+\) and \(f\in\mathcal{O}(\Omega)\) finite, to the germ at \(t=1\) of \(t\mapsto f(th)\), and
   \((\Omega,h,-\infty)\) to \(-\infty\), defines an isomorphism of \(\mathbb{R}_{\max}\)-algebras from the stalk
   \(\mathcal{O}_{\mathfrak{p}_H}\) onto \(\mathcal{R}_H\).
2. Let \(H\) be a rank one ordered group. Sending a triple \((\Omega,h,f)\), with \(0\in\Omega\), \(h\in H_{>0}\)
   and \(f\in\mathcal{O}(\Omega)\) finite, to the pair \((f(0),f'_+(0)\,h)\), and \((\Omega,h,-\infty)\) to
   \(-\infty\), defines an isomorphism of \(\mathbb{R}_{\max}\)-algebras from the stalk
   \(\mathcal{O}_{\mathfrak{q}_H}\) onto \(\mathcal{Z}_H\).

*Proof.* We use Theorem 4.1 (2). (1) The function \(t\mapsto f(th)\) is defined near \(t=1\), it is convex, and its
slopes at \(1\) are \(h f'_\pm(h)\in h\mathbb{Z}\subseteq H\). So we get an element \(\rho(\Omega,h,f)\) of
\(\mathcal{R}_H\). If \(n\colon\Omega\to\Omega'\), \(h\in\Omega\cap H_+\) and \(f'\in\mathcal{O}(\Omega')\), then
\(\rho(\Omega,h,\mathcal{O}(n)f')\) is the germ of \(t\mapsto f'(nth)\), which is \(\rho(\Omega',nh,f')\). Hence
equivalent triples have the same image, and \(\rho\) is defined on the stalk. It preserves maxima, sums and
constants.

*Injective.* Let \(\rho(\Omega_1,h_1,f_1)=\rho(\Omega_2,h_2,f_2)\). By (F2) for \(F_H\) there are an object \(W\),
\(g\in W\cap H_+\) and \(n_j\colon W\to\Omega_j\) with \(n_jg=h_j\). The functions
\(\mathcal{O}(n_j)f_j=f_j(n_j\,\cdot)\) on \(W\) have the same germ at \(g\), because
\(f_1(n_1tg)=f_1(th_1)\) and \(f_2(n_2tg)=f_2(th_2)\) agree for \(t\) near \(1\). So they agree on a smaller object
\(W'\ni g\). The morphisms \(n_j\colon W'\to\Omega_j\) then show that the two triples are equivalent. If one of the
two sections is \(-\infty\), so is the other.

*Surjective.* Let \((x,a_-,a_+)\) be a germ with \(a_\pm\in H\), \(a_-\le a_+\). By Lemma 1.1 there are
\(g\in H_+\) and integers \(k_-\le k_+\) with \(a_\pm=k_\pm g\). Let
\(f(\lambda)=x+\max\bigl(k_-(\lambda-g),k_+(\lambda-g)\bigr)\) on the object \(\Omega=(g/2,2g)\). Then
\(f\in\mathcal{O}(\Omega)\) and \(f(tg)=x+\max(a_-(t-1),a_+(t-1))\). So \(\rho(\Omega,g,f)\) is the given germ.

(2) Near \(0\) a finite section \(f\) is affine: \(f(\lambda)=f(0)+k\lambda\) with \(k=f'_+(0)\in\mathbb{Z}\). Put
\(\rho(\Omega,h,f)=(f(0),kh)\). If \(n\colon\Omega\to\Omega'\) and \(f'\in\mathcal{O}(\Omega')\) has slope \(k'\) at
\(0\), then \(\mathcal{O}(n)f'\) has slope \(nk'\) at \(0\), and
\(\rho(\Omega,h,\mathcal{O}(n)f')=(f'(0),nk'h)=\rho(\Omega',nh,f')\). So \(\rho\) is defined on the stalk.

*Injective.* Let \(\rho(\Omega_1,h_1,f_1)=\rho(\Omega_2,h_2,f_2)\), with slopes \(k_1,k_2\) at \(0\). Take \(W\ni0\),
\(g\in H_{>0}\), \(n_j\colon W\to\Omega_j\) with \(n_jg=h_j\). The sections \(f_j(n_j\,\cdot)\) have the same value
at \(0\) and the slopes \(n_jk_j\) at \(0\). From \(k_1h_1=k_2h_2\) we get \(n_1k_1g=n_2k_2g\), so
\(n_1k_1=n_2k_2\). So the two sections agree on a smaller object \(W'\ni0\), and the triples are equivalent.

*Surjective.* The pair \((x,h)\) with \(h>0\) is \(\rho([0,1),h,x+\lambda)\). The pair \((x,-h)\) with \(h>0\) is
\(\rho([0,1),h,x-\lambda)\). The pair \((x,0)\) is the image of a constant.

*Operations.* Two elements of the stalk can be written as \((W,g,f_1)\) and \((W,g,f_2)\). Near \(0\) the maximum
of \(f_1\) and \(f_2\) is the one with the larger value at \(0\), and for equal values the one with the larger slope.
This is the maximum of \((f_1(0),k_1g)\) and \((f_2(0),k_2g)\) in the lexicographic order. Sums correspond to sums.
\(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 4.2].

**Remark 5.2.** On the arithmetic site, the stalk of \(\mathbb{Z}_{\max}\) at the point given by the ordered group
\(H\) is \(H_{\max}\) (*The arithmetic site*, Theorem 3.2; [Connes–Consani 2016b, Theorem 3.2]). At the corresponding point \(\mathfrak{q}_H\) of the
scaling site the stalk is the semifield \((\mathbb{R}\times H)_{\max}\), which contains \(\mathbb{R}_{\max}\) as the
elements \((c,0)\) and \(H_{\max}\) as the elements \((0,h)\). At the points \(\mathfrak{p}_H\) the stalk
\(\mathcal{R}_H\) is not a semifield: for an element \(h>0\) of \(H\), the germ of
\(\max(0,h(t-1))\) is not invertible. The invertible elements of \(\mathcal{R}_H\) are the germs with \(a_-=a_+\).

### 5.2 Points over \(\mathbb{R}_{\max}\)

**Definition.** A *point of the scaling site over \(\mathbb{R}_{\max}\)* is a pair \((p,\varphi)\), where \(p\) is a
point of \([0,\infty)\rtimes\mathbb{N}^{\times}\) and \(\varphi\colon\mathcal{O}_p\to\mathbb{R}_{\max}\) is a
morphism of \(\mathbb{R}_{\max}\)-algebras. Two such pairs are identified when an isomorphism of points carries one
morphism to the other. The set of classes is written \(\mathscr{S}(\mathbb{R}_{\max})\).

The condition of \(\mathbb{R}_{\max}\)-linearity expresses that the scaling site is defined over
\(\mathbb{R}_{\max}\).

**Theorem 5.3.** For every point \(p\) of \([0,\infty)\rtimes\mathbb{N}^{\times}\) there is exactly one morphism of
\(\mathbb{R}_{\max}\)-algebras \(\mathcal{O}_p\to\mathbb{R}_{\max}\). On \(\mathcal{R}_H\) it is the value of the
germ at \(t=1\). On \(\mathcal{Z}_H\) it is \((x,h)\mapsto x\). Hence the map from
\(\mathscr{S}(\mathbb{R}_{\max})\) to the set of isomorphism classes of points of the topos is bijective, and
\(\mathscr{S}(\mathbb{R}_{\max})\cong X_{\mathbb{Q}}\) by Theorem 4.11.

*Proof.* The two maps named in the statement preserve maxima, sums and constants. Let \(\varphi\) be any morphism of
\(\mathbb{R}_{\max}\)-algebras from the stalk to \(\mathbb{R}_{\max}\). It is additive, so \(s\vee s'=s'\) implies
\(\varphi(s)\le\varphi(s')\). It sends the constant \(c\) to \(c\). Let \(s\) be a finite element of the stalk with
value \(x\), and let \(\varepsilon>0\). In \(\mathcal{R}_H\), a germ with value \(x\) at \(1\) lies between the
constants \(x-\varepsilon\) and \(x+\varepsilon\) near \(1\). In \(\mathcal{Z}_H\),
\((x-\varepsilon,0)<(x,h)<(x+\varepsilon,0)\). So \(x-\varepsilon\le\varphi(s)\le x+\varepsilon\) for all
\(\varepsilon\), and \(\varphi(s)=x\). An isomorphism of points carries the unique morphism to the unique morphism.
\(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 4.3].

**Corollary 5.4 (extension of scalars does not change the points over \(\mathbb{R}_{\max}\)).** By *The arithmetic
site*, Theorem 4.3, Corollary 4.4 and Theorem 4.6, the points of the arithmetic site \(\mathscr{A}\) over \(\mathbb{R}_{\max}\) are of two kinds
[Connes–Consani 2016b, Theorem 3.8]. There is one for each isomorphism class of rank one ordered groups \(H\); its
morphism \(H_{\max}\to\mathbb{R}_{\max}\) has values in \(\mathbb{B}\). And there is one for each rank one subgroup
\(H'\) of \(\mathbb{R}\); its morphism is an isomorphism of the stalk onto \(H'_{\max}\). The first kind corresponds
to the points \(\mathfrak{q}_H\) and the second to the points \(\mathfrak{p}_{H'}\). So

\[
\mathscr{S}(\mathbb{R}_{\max})=\mathscr{A}(\mathbb{R}_{\max})=X_{\mathbb{Q}} .
\]

The action of \(\mathrm{Fr}_\mu\in\mathrm{Aut}(\mathbb{R}_{\max})\) on \(\mathscr{A}(\mathbb{R}_{\max})\) sends
\(H'\) to \(\mu H'\) and fixes the first kind. So it corresponds to the scaling action of Theorem 4.11. This is the
analogue of \(\bar C(\bar{\mathbb{F}}_q)=C(\bar{\mathbb{F}}_q)\) with its Frobenius action.

### 5.3 Rational functions and the order at a point

**Definition 5.5.** For an object \(\Omega\) let \(\mathcal{K}(\Omega)\) be the set of functions on \(\Omega\) that
are constant \(-\infty\) or belong to \(\mathrm{PA}_{\mathbb{Z}}(\Omega)\), with \(\mathcal{K}(n)(f)=f(n\,\cdot)\).
This is a sheaf of semirings containing \(\mathcal{O}\), and every finite section \(f\) has the inverse \(-f\). The
proof of Theorem 5.1 (1), without the convexity condition, identifies the stalk of \(\mathcal{K}\) at
\(\mathfrak{p}_H\) with

\[
\mathcal{K}_H=\{-\infty\}\cup\{\text{germs at }1\text{ with slopes in }H\}.
\]

\(\mathcal{K}_H\) is a semifield. Every finite element \((x,a_-,a_+)\) of \(\mathcal{K}_H\) is a difference of two
elements of \(\mathcal{R}_H\): if \(a_->a_+\), it is \((x,a_-,a_-)-(0,0,a_--a_+)\). So \(\mathcal{K}_H\) is the
semifield of fractions of \(\mathcal{R}_H\).

The *order* of a finite element \(f=(x,a_-,a_+)\in\mathcal{K}_H\) is \(\mathrm{ord}(f)=a_+-a_-\in H\).

**Proposition 5.6.** Let \(f,g\in\mathcal{K}_H\) be finite.

1. \(\mathrm{ord}(f+g)=\mathrm{ord}(f)+\mathrm{ord}(g)\) and \(\mathrm{ord}(-f)=-\mathrm{ord}(f)\).
2. \(\mathrm{ord}(f\vee g)\ge\min(\mathrm{ord}(f),\mathrm{ord}(g))\).
3. \(f\in\mathcal{R}_H\) if and only if \(\mathrm{ord}(f)\ge0\), and \(f\) is invertible in \(\mathcal{R}_H\) if and
   only if \(\mathrm{ord}(f)=0\).
4. If \(f\) is represented by the triple \((\Omega,h,s)\) with \(s\in\mathrm{PA}_{\mathbb{Z}}(\Omega)\), then
   \(\mathrm{ord}(f)=h\,j_s(h)\).

*Proof.* (1) and (2) are Lemma 1.2 (2) for germs. (3) holds by the definition of \(\mathcal{R}_H\). (4) The slopes
of \(t\mapsto s(th)\) at \(t=1\) are \(h\,s'_\pm(h)\). \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Definition 4.6 and Proposition 4.7].

So an element of \(\mathcal{K}_H\) has a zero of order \(\mathrm{ord}(f)>0\), or a pole of order
\(-\mathrm{ord}(f)>0\), exactly where it has a breakpoint. The order is an element of the group \(H\) attached to
the point. It is a real number, not an integer.

## 6. The periodic orbits as curves

### 6.1 Stabilizers and the orbit \(C_p\)

**Proposition 6.1 (stabilizers of the scaling action).** Let \(H\) be a rank one subgroup of \(\mathbb{R}\). The
group \(\{\mu\in\mathbb{R}_{>0}:\mu H=H\}\) is the subgroup of \(\mathbb{Q}_{>0}\) generated by the primes \(p\)
with \(pH=H\).

*Proof.* If \(\mu H=H\) and \(h\in H_+\), then \(\mu h\in H\), so \(\mu\in\mathbb{Q}\). Write \(\mu=m/n\) in lowest
terms. Then \(mH=nH\). Let \(p\) be a prime dividing \(m\), so \(p\nmid n\). For \(h\in H\) we have
\(nh\in mH\subseteq pH\) and \(ph\in pH\). Since \(n\) and \(p\) are coprime, \(h\in pH\). So \(pH=H\). The same
argument applies to the primes dividing \(n\). Conversely, if \(pH=H\) for every prime \(p\) occurring in \(\mu\),
then \(\mu H=H\). \(\blacksquare\)

So the orbit of \(\mathfrak{p}_H\) under the scaling action is of one of three kinds. If \(pH\neq H\) for all
primes \(p\), the action on the orbit is free. If \(pH=H\) for exactly one prime \(p\), the stabilizer is
\(p^{\mathbb{Z}}\) and the orbit is a circle \(\mathbb{R}_{>0}/p^{\mathbb{Z}}\), of length \(\log p\) in the variable
\(\log\mu\). We call it a *periodic orbit of period \(\log p\)*. If \(pH=H\) for at least two primes, the stabilizer
is dense in \(\mathbb{R}_{>0}\). In adelic terms, for \(H=xH_a\) one has \(pH=H\) exactly when \(a_p=0\): indeed
\(pH_a=H_{p^{-1}a}\), and \(p^{-1}a\) and \(a\) have the same class modulo \(\widehat{\mathbb{Z}}^{\times}\) exactly
when \(v_p(a_p)-1=v_p(a_p)\), that is when \(v_p(a_p)=+\infty\).

The subgroup \(H_p=\mathbb{Z}[1/p]\) satisfies \(pH_p=H_p\) and \(\ell H_p\ne H_p\) for every prime \(\ell\neq p\).
It is \(H_a\) for the finite adèle \(a\) with \(a_p=0\) and \(a_\ell=1\) for \(\ell\neq p\). This is the adèle
attached to the prime \(p\) of \(\operatorname{Spec}\mathbb{Z}\) in [Connes–Consani 2016b, Remark 2.9].

**Definition 6.2.** Let \(p\) be a prime. The *periodic orbit* \(C_p\) is the orbit of \(\mathfrak{p}_{H_p}\):

\[
C_p=\{\mathfrak{p}_{\lambda H_p}:\lambda\in\mathbb{R}_{>0}\}.
\]

By Proposition 6.1 the map \(\lambda\mapsto\lambda H_p\) induces a bijection
\(\mathbb{R}_{>0}/p^{\mathbb{Z}}\to C_p\). We give \(C_p\) the topology of the circle
\(\mathbb{R}_{>0}/p^{\mathbb{Z}}\) and write \(\pi\colon\mathbb{R}_{>0}\to C_p\) for the quotient map. We write
\(H\) for the point \(\mathfrak{p}_H\) of \(C_p\).

For an open set \(U\subseteq C_p\) let \(\mathcal{K}_p(U)\) be the set of functions
\(f\colon\pi^{-1}(U)\to\mathbb{R}_{\max}\) with \(f(p\lambda)=f(\lambda)\) which, on each connected component of
\(\pi^{-1}(U)\), are constant \(-\infty\) or belong to \(\mathrm{PA}_{H_p}\). Let
\(\mathcal{O}_p(U)\subseteq\mathcal{K}_p(U)\) be the subset where \(\mathrm{PA}_{H_p}\) is replaced by
\(\mathrm{CPA}_{H_p}\). These are sheaves of semirings on \(C_p\). The semifield of *rational functions* on \(C_p\)
is

\[
\mathcal{K}(C_p)=\mathcal{K}_p(C_p)=\{-\infty\}\cup\{f\in\mathrm{PA}_{H_p}(\mathbb{R}_{>0}):f(p\lambda)=f(\lambda)\}.
\]

If \(f(p\lambda)=f(\lambda)\), then \(f'_\pm(p\lambda)=p^{-1}f'_\pm(\lambda)\). So the substitution
\(\lambda\mapsto p\lambda\) turns a function with slopes in a group \(G\) into a function with slopes in \(pG\), and
the condition "slopes in \(G\)" is invariant under this substitution exactly when \(pG=G\). The group \(H_p\) has
this property and \(\mathbb{Z}\) does not: a function with integral slopes and \(f(p\lambda)=f(\lambda)\) is
constant, because a slope \(a\) at \(\lambda\) gives the slope \(p^{-k}a\) at \(p^{k}\lambda\), and \(p^{-k}a\) is
an integer for all \(k\ge0\) only if \(a=0\).

**Proposition 6.3.**

1. Let \(\lambda>0\). Sending the germ of \(g\) at \(\lambda\) to the germ at \(t=1\) of \(t\mapsto g(\lambda t)\)
   is an isomorphism of \(\mathbb{R}_{\max}\)-algebras from the stalk of \(\mathcal{O}_p\) at \(\pi(\lambda)\) onto
   \(\mathcal{R}_{\lambda H_p}\), and from the stalk of \(\mathcal{K}_p\) onto \(\mathcal{K}_{\lambda H_p}\). It is
   the same for \(\lambda\) and for \(p\lambda\).
2. For a finite germ \(g\) of \(\mathcal{K}_p\) at the point \(H=\lambda H_p\), the order of the corresponding
   element of \(\mathcal{K}_H\) is \(\mathrm{ord}_H(g)=\lambda\,j_g(\lambda)\in H\).
3. The global sections of \(\mathcal{O}_p\) are the constants: \(\mathcal{O}_p(C_p)=\mathbb{R}_{\max}\).

*Proof.* (1) The slopes of \(t\mapsto g(\lambda t)\) at \(t=1\) are \(\lambda g'_\pm(\lambda)\in\lambda H_p\).
Conversely the germ \((x,a_-,a_+)\) with \(a_\pm\in\lambda H_p\) comes from the function
\(x+\lambda^{-1}a_\pm(\mu-\lambda)\) for \(\pm(\mu-\lambda)\ge0\). Convexity is the condition \(a_-\le a_+\) on both
sides. Since \(g(p\lambda t)=g(\lambda t)\), the representative \(p\lambda\) gives the same germ. (2) follows from
the formula for the slopes. (3) A finite global section is a convex continuous function \(f\) on
\(\mathbb{R}_{>0}\) with \(f(p\lambda)=f(\lambda)\). It is bounded. A convex function on \((0,\infty)\) that is
bounded above is non-increasing. With \(f(p\lambda)=f(\lambda)\) this gives that \(f\) is constant.
\(\blacksquare\)

By Theorem 5.1 and Definition 5.5, the stalks of \(\mathcal{O}_p\) and \(\mathcal{K}_p\) at the point \(H\) of
\(C_p\) are the stalks of \(\mathcal{O}\) and \(\mathcal{K}\) at the point \(\mathfrak{p}_H\) of the scaling site.
In this sense \((C_p,\mathcal{O}_p)\) is the restriction of the scaling site to the periodic orbit.

*Reference:* [Connes–Consani 2017, Lemma 5.1].

### 6.2 Divisors, degree, and the invariant \(\chi\)

**Definition 6.4.** A *divisor* on \(C_p\) is a map \(D\) that assigns to each point \(H\in C_p\) an element
\(D(H)\in H\), with \(D(H)=0\) for all but finitely many \(H\). Divisors form a group \(\mathrm{Div}(C_p)\) under
pointwise addition. We write \(D\ge0\), and call \(D\) *effective*, when \(D(H)\ge0\) for all \(H\). We write
\([H]\cdot d\) for the divisor with value \(d\in H\) at \(H\) and \(0\) elsewhere. The *degree* is

\[
\deg D=\sum_{H\in C_p}D(H)\in\mathbb{R}.
\]

Let \(\chi\colon H_p\to\mathbb{Z}/(p-1)\mathbb{Z}\) be the ring homomorphism with
\(\chi(a/p^{k})=a\bmod(p-1)\). It is well defined because \(p\equiv1\) modulo \(p-1\), and its kernel is
\((p-1)H_p\). For a point \(H=\lambda H_p\) put \(\chi_H(h)=\chi(h/\lambda)\) for \(h\in H\). This does not depend
on the choice of \(\lambda\), because \(\chi(p^{k}x)=\chi(x)\). Put

\[
\chi(D)=\sum_{H\in C_p}\chi_H(D(H))\in\mathbb{Z}/(p-1)\mathbb{Z}.
\]

The *divisor of a finite function* \(f\in\mathcal{K}(C_p)\) is
\((f)=\sum_H[H]\cdot\mathrm{ord}_H(f)\), with \(\mathrm{ord}_H(f)=\lambda j_f(\lambda)\) for \(H=\lambda H_p\). The
sum is finite, because \(f\) has finitely many breakpoints in \([1,p]\). Divisors of the form \((f)\) are called
*principal*. They form a subgroup \(\mathcal{P}\), because \((f+g)=(f)+(g)\) and \((-f)=-(f)\) by Lemma 1.2.

The degree of a divisor is a real number. Both \(\deg\) and \(\chi\) are group homomorphisms. If \((f)=0\), then
\(f\) has no breakpoint, so it is affine on \(\mathbb{R}_{>0}\) and periodic, hence constant.

Every divisor is locally principal: near \(\lambda_0\), the function \((d/\lambda_0)\max(0,\lambda-\lambda_0)\) has
the divisor \([\lambda_0H_p]\cdot d\). A local section of \(\mathcal{K}_p\) has divisor \(0\) exactly when it is an
invertible section of \(\mathcal{O}_p\). So divisors are the global sections of the quotient of the sheaf of finite
sections of \(\mathcal{K}_p\) by the sheaf of invertible sections of \(\mathcal{O}_p\). They are Cartier divisors
[Connes–Consani 2017, Proposition 5.2].

**Proposition 6.5.** For every finite \(f\in\mathcal{K}(C_p)\): \(\deg(f)=0\) and \(\chi((f))=0\).

*Proof.* Let \(a(\lambda)=f'_+(\lambda)\) be the slope and \(b(\lambda)=f(\lambda)-\lambda f'_+(\lambda)\) the
intercept of the affine piece of \(f\) to the right of \(\lambda\). Both are right-continuous step functions on
\(\mathbb{R}_{>0}\) with finitely many jumps in each compact interval. Since \(f\) is continuous, the jump of \(b\)
at \(\lambda\) is \(-\lambda j_f(\lambda)=-\mathrm{ord}_{\lambda H_p}(f)\). From \(f(p\lambda)=f(\lambda)\) and
\(a(p\lambda)=a(\lambda)/p\) we get \(b(p\lambda)=b(\lambda)\). Fix \(\lambda_0>0\). The points of
\((\lambda_0,p\lambda_0]\) represent each point of \(C_p\) once. The sum of the jumps of \(b\) over this interval is
\(b(p\lambda_0)-b(\lambda_0)=0\). So \(\deg(f)=0\).

The function \(c(\lambda)=\chi(a(\lambda))\) satisfies \(c(p\lambda)=\chi(a(\lambda)/p)=c(\lambda)\). Its jump at
\(\lambda\) is \(\chi(j_f(\lambda))=\chi_{\lambda H_p}(\mathrm{ord}_{\lambda H_p}(f))\). The sum of its jumps over
\((\lambda_0,p\lambda_0]\) is \(c(p\lambda_0)-c(\lambda_0)=0\). So \(\chi((f))=0\). \(\blacksquare\)

**Theorem 6.6 (divisor classes on \(C_p\)).** The map

\[
(\deg,\chi)\colon\mathrm{Div}(C_p)/\mathcal{P}\longrightarrow\mathbb{R}\times\mathbb{Z}/(p-1)\mathbb{Z}
\]

is an isomorphism of groups. In particular a divisor is principal if and only if its degree is \(0\) and its
invariant \(\chi\) is \(0\), and the group of classes of divisors of degree \(0\) is cyclic of order \(p-1\).

*Proof.* The map is defined on classes by Proposition 6.5.

*Injective.* Let \(\deg D=0\) and \(\chi(D)=0\). Choose points \(\lambda_0<\lambda_1<\dots<\lambda_{k-1}<p\lambda_0\)
such that the support of \(D\) lies in \(\{\lambda_jH_p\}\), and put \(\lambda_k=p\lambda_0\). Write
\(D(\lambda_jH_p)=\lambda_ja_j\) with \(a_j\in H_p\). Then \(\sum_{j<k}\lambda_ja_j=\deg D=0\), and
\(\sigma=\sum_{j<k}a_j\) satisfies \(\chi(\sigma)=\chi(D)=0\), so \(\sigma\in(p-1)H_p\).

We look for a function \(f\in\mathcal{K}(C_p)\) that is affine with slope \(h_j\in H_p\) on
\([\lambda_{j-1},\lambda_j]\) for \(1\le j\le k\). By periodicity its slope on \([\lambda_{k-1}/p,\lambda_0]\) is
\(ph_k\). So \((f)=D\) means

\[
h_{j+1}-h_j=a_j\quad(1\le j\le k-1),\qquad h_1-ph_k=a_0 .
\]

Adding these equations gives \((1-p)h_k=\sigma\). So we put \(h_k=-\sigma/(p-1)\in H_p\) and
\(h_j=h_k-(a_j+\dots+a_{k-1})\). Define \(f\) on \([\lambda_0,p\lambda_0]\) by \(f(\lambda_0)=0\) and these slopes.
Then, by summation by parts,

\[
f(p\lambda_0)=\sum_{j=1}^{k}h_j(\lambda_j-\lambda_{j-1})
=h_k\lambda_k-h_1\lambda_0-\sum_{j=1}^{k-1}\lambda_j(h_{j+1}-h_j)
=-\lambda_0a_0-\sum_{j=1}^{k-1}\lambda_ja_j=0 .
\]

So \(f\) extends to a continuous function on \(\mathbb{R}_{>0}\) with \(f(p\lambda)=f(\lambda)\). Its slope on
\(p^{i}[\lambda_{j-1},\lambda_j]\) is \(p^{-i}h_j\in H_p\). So \(f\in\mathcal{K}(C_p)\), and \((f)=D\).

*Surjective.* Let \(\delta\in\mathbb{R}\), \(\delta\neq0\), and \(c\in\mathbb{Z}/(p-1)\mathbb{Z}\). Choose a
non-zero integer \(a\) with the sign of \(\delta\) and with \(a\equiv c\) modulo \(p-1\). The divisor
\(D=[(\delta/a)H_p]\cdot\delta\) is defined, since \(\delta=(\delta/a)a\). It has \(\deg D=\delta\) and
\(\chi(D)=\chi(a)=c\). So the image contains all pairs \((\delta,c)\) with \(\delta\neq0\). It is a subgroup, so it
is everything. \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 5.6].

**Example 6.7 (a principal divisor, \(p=3\)).** Let \(f(\lambda)=1-|\lambda-2|\) on \([1,3]\), extended by
\(f(3\lambda)=f(\lambda)\). Its slopes on \([1,2]\) and \([2,3]\) are \(1\) and \(-1\). At \(\lambda=2\) the jump is
\(-2\), so \(\mathrm{ord}_{2H_3}(f)=-4\). At \(\lambda=1\) the slope to the left is \(3\cdot(-1)=-3\), the jump is
\(4\), and \(\mathrm{ord}_{H_3}(f)=4\). So \((f)=[H_3]\cdot4-[2H_3]\cdot4\). The degree is \(0\), and
\(\chi((f))=\chi(4)+\chi(-2)=0\) in \(\mathbb{Z}/2\mathbb{Z}\).

**Example 6.8 (edge cases).** (a) For \(p=2\) the group \(\mathbb{Z}/(p-1)\mathbb{Z}\) is trivial. Two divisors on
\(C_2\) are equivalent modulo \(\mathcal{P}\) exactly when they have the same degree.

(b) Let \(p=3\) and \(D=[H_3]\cdot1-[\tfrac32H_3]\cdot1\). This is a divisor, since
\(1=\tfrac32\cdot\tfrac23\) and \(\tfrac23\in H_3\). Its degree is \(0\). But
\(\chi(D)=\chi(1)-\chi(\tfrac23)=1-0=1\) in \(\mathbb{Z}/2\mathbb{Z}\). So \(D\) is not principal, while \(2D\) is.

(c) The class of a divisor of degree \(0\) depends only on \(\chi\). For \(p=3\), all divisors
\([H]\cdot1-[H']\cdot1\) with \(\chi_H(1)\neq\chi_{H'}(1)\) are equivalent to the divisor in (b), wherever the two
points lie on the circle. Compare Exercise 6: on a tropical circle of length \(L\) the class of \([u]-[u']\) is
\(u-u'\) modulo \(L\).

### 6.3 Theta functions

The rational functions on \(C_p\) can be written with theta functions, as for the curve
\(k^{\times}/t^{\mathbb{Z}}\) over a non-archimedean field \(k\). There the basic theta function is, up to a
constant factor, the product \((1-w)\prod_{m\ge1}(1-t^{m}w)(1-t^{m}w^{-1})\); see [Connes–Consani 2017,
Section 5.3]. Here products become sums. For \(\lambda>0\) put

\[
\theta(\lambda)=\sum_{m\ge0}\max(0,\,1-p^{m}\lambda)+\sum_{m\ge1}\max(0,\,p^{-m}\lambda-1).
\]

For \(h\in H_p\) with \(h>0\) and a real number \(\mu>0\) put
\(\Theta_{h,\mu}(\lambda)=\mu\,\theta(h\lambda/\mu)\).

**Lemma 6.9.**

1. On each compact subset of \(\mathbb{R}_{>0}\) only finitely many terms of \(\theta\) are non-zero. The function
   \(\theta\) belongs to \(\mathrm{CPA}_{H_p}(\mathbb{R}_{>0})\), and \(\theta=0\) on \([1,p]\).
2. \(\theta(p\lambda)=\theta(\lambda)+\lambda-1\) for all \(\lambda>0\).
3. The breakpoints of \(\theta\) are the points \(p^{k}\), \(k\in\mathbb{Z}\), and \(p^{k}j_\theta(p^{k})=1\).
4. \(\Theta_{h,\mu}\in\mathrm{CPA}_{H_p}(\mathbb{R}_{>0})\), and
   \(\Theta_{h,\mu}(p\lambda)=\Theta_{h,\mu}(\lambda)+h\lambda-\mu\). Its breakpoints are the points of
   \((\mu/h)p^{\mathbb{Z}}\), and \(\lambda j_{\Theta_{h,\mu}}(\lambda)=\mu\) at each of them.

*Proof.* (1) The term \(\max(0,1-p^{m}\lambda)\) vanishes for \(\lambda\ge p^{-m}\), and
\(\max(0,p^{-m}\lambda-1)\) vanishes for \(\lambda\le p^{m}\). Each term is convex and piecewise affine with slopes
in \(H_p\). On \([1,p]\) all terms vanish. (2) Replacing \(\lambda\) by \(p\lambda\) shifts the index \(m\) by one
in both sums. The first sum loses the term \(\max(0,1-\lambda)\) and the second gains the term
\(\max(0,\lambda-1)\). So \(\theta(p\lambda)-\theta(\lambda)=\max(0,\lambda-1)-\max(0,1-\lambda)=\lambda-1\).
(3) The term \(\max(0,1-p^{m}\lambda)\) has one
breakpoint, at \(p^{-m}\), with jump \(p^{m}\). The term \(\max(0,p^{-m}\lambda-1)\) has one breakpoint, at
\(p^{m}\), with jump \(p^{-m}\). (4) The slopes of \(\Theta_{h,\mu}\) are \(h\) times slopes of \(\theta\). By (2),
\(\Theta_{h,\mu}(p\lambda)=\mu\theta(h\lambda/\mu)+\mu(h\lambda/\mu-1)\). By (3) the breakpoints are the
\(\lambda\) with \(h\lambda/\mu=p^{k}\), and there \(\lambda j(\lambda)=(\mu p^{k}/h)\cdot h\,p^{-k}=\mu\).
\(\blacksquare\)

So \(\Theta_{h,\mu}\) is not periodic, but it has a divisor in the evident sense: the one-point divisor
\([(\mu/h)H_p]\cdot\mu\). Every effective one-point divisor \([H]\cdot\mu\), \(\mu\in H_+\), arises in this way: if
\(H=\lambda H_p\), take \(h=\mu/\lambda\).

**Theorem 6.10 (functions with a given divisor).** Let \(D\) be a divisor on \(C_p\). Write

\[
D=\sum_i[\lambda_iH_p]\cdot\mu_i-\sum_j[\lambda'_jH_p]\cdot\mu'_j,\qquad \mu_i,\mu'_j>0,
\]

and put \(h_i=\mu_i/\lambda_i\) and \(h'_j=\mu'_j/\lambda'_j\), elements of \(H_p\). Let

\[
\Theta_D(\lambda)=\sum_i\Theta_{h_i,\mu_i}(\lambda)-\sum_j\Theta_{h'_j,\mu'_j}(\lambda).
\]

1. \(\deg D=\sum_i\mu_i-\sum_j\mu'_j\) and \(\chi(D)=\chi\bigl(\sum_ih_i-\sum_jh'_j\bigr)\).
2. Suppose \(\deg D=0\) and \(\sum_ih_i-\sum_jh'_j=(p-1)k\) with \(k\in H_p\). Then the function
   \(f(\lambda)=\Theta_D(\lambda)-k\lambda\) belongs to \(\mathcal{K}(C_p)\) and \((f)=D\).
3. Every finite \(g\in\mathcal{K}(C_p)\) is of the form \(g=f+c\), where \(f\) is the function of (2) for the
   divisor \(D=(g)\) and \(c\in\mathbb{R}\).

*Proof.* (1) holds by the definitions, since \(\chi_{\lambda_iH_p}(\mu_i)=\chi(h_i)\). (2) The function \(f\) is
in \(\mathrm{PA}_{H_p}(\mathbb{R}_{>0})\). By Lemma 6.9 (4),

\[
f(p\lambda)-f(\lambda)=\sum_i(h_i\lambda-\mu_i)-\sum_j(h'_j\lambda-\mu'_j)-(p-1)k\lambda=-\deg D=0 .
\]

So \(f\in\mathcal{K}(C_p)\). At a point \(\lambda\), the number \(\lambda j_f(\lambda)\) is the sum of the
\(\mu_i\) with \(\lambda\in\lambda_ip^{\mathbb{Z}}\) minus the sum of the \(\mu'_j\) with
\(\lambda\in\lambda'_jp^{\mathbb{Z}}\). This is \(D(\lambda H_p)\). (3) By Proposition 6.5 the divisor \((g)\)
satisfies the hypotheses of (2). Then \(g-f\) has divisor \(0\), so it is constant. \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Proposition 5.11 and Theorem 5.12].

Part (2) gives a second proof that a divisor with \(\deg D=0\) and \(\chi(D)=0\) is principal.

### 6.4 The Riemann–Roch problem

**Definition 6.11.** For a divisor \(D\) on \(C_p\) let

\[
H^{0}(D)=\{-\infty\}\cup\{f\in\mathcal{K}(C_p)\text{ finite}: D+(f)\ge0\}.
\]

**Lemma 6.12.**

1. \(H^{0}(D)\) is closed under \(\vee\) and under addition of constants. So it is a module over
   \(\mathbb{R}_{\max}\).
2. For a finite \(g\in\mathcal{K}(C_p)\): \(H^{0}(D+(g))=\{f-g:f\in H^{0}(D)\}\).
3. If \(\deg D<0\), then \(H^{0}(D)=\{-\infty\}\).
4. If \(\deg D=0\), then \(H^{0}(D)\ne\{-\infty\}\) if and only if \(D\) is principal. If \(D=(g)\), then
   \(H^{0}(D)=\{-\infty\}\cup\{c-g:c\in\mathbb{R}\}\).
5. If \(\deg D>0\), then \(H^{0}(D)\) contains a finite function.

*Proof.* (1) For finite \(f,g\in H^{0}(D)\) and a point \(H\), Proposition 5.6 gives
\(D(H)+\mathrm{ord}_H(f\vee g)\ge D(H)+\min(\mathrm{ord}_H(f),\mathrm{ord}_H(g))\ge0\). (2) holds because
\(D+(g)+(f-g)=D+(f)\). (3) If \(f\) is finite and \(D+(f)\ge0\), then \(\deg D=\deg(D+(f))\ge0\) by
Proposition 6.5. (4) If \(D+(f)\ge0\) and \(\deg D=0\), the effective divisor \(D+(f)\) has degree \(0\), so it is
\(0\) and \(D=(-f)\). If \(D=(g)\), then \(D+(f)=0\) means \((f+g)=0\), so \(f+g\) is constant. (5) Let
\(\delta=\deg D>0\). Choose a positive integer \(a\) with \(\chi(a)=\chi(D)\) and put
\(E=[(\delta/a)H_p]\cdot\delta\). Then \(E\ge0\), \(\deg E=\delta\) and \(\chi(E)=\chi(D)\). By Theorem 6.6,
\(E-D=(f)\) for a finite \(f\), and \(D+(f)=E\ge0\). \(\blacksquare\)

By (4) and (5) the \(\mathbb{R}_{\max}\)-module \(H^{0}(D)\) is a "line" when \(D\) is principal and is much
larger when \(\deg D>0\). The slopes of its elements lie in \(H_p\), which is dense in \(\mathbb{R}\), and there is
no bound on their denominators. To measure \(H^{0}(D)\) one filters it by the denominators of the slopes.

### 6.5 The filtration and the real-valued dimension

Let \(|\cdot|_p\) be the \(p\)-adic absolute value on \(\mathbb{Q}\), with \(|p|_p=1/p\).

**Definition 6.13.** For a finite \(f\in\mathcal{K}(C_p)\) put

\[
\|f\|_p=\sup_{\lambda>0}\frac{|f'_+(\lambda)|_p}{\lambda}.
\]

**Lemma 6.14.**

1. The function \(\lambda\mapsto|f'_+(\lambda)|_p/\lambda\) takes the same value at \(\lambda\) and \(p\lambda\),
   and the supremum is a maximum.
2. For \(n\in\mathbb{Z}\): \(\|f\|_p\le p^{n}\) if and only if \(f'_+(\lambda)\in p^{-n}\mathbb{Z}\) for all
   \(\lambda\in[1,p)\).
3. \(\|f+g\|_p\le\max(\|f\|_p,\|g\|_p)\), \(\|f\vee g\|_p\le\max(\|f\|_p,\|g\|_p)\), \(\|-f\|_p=\|f\|_p\),
   \(\|c\|_p=0\) for constants, and \(\|p^{m}f\|_p=p^{-m}\|f\|_p\) for \(m\in\mathbb{Z}\).

*Proof.* (1) \(f'_+(p\lambda)=f'_+(\lambda)/p\) and \(|x/p|_p=p|x|_p\). On \([1,p)\) the function \(f'_+\) takes
finitely many values, each on an interval \([u,v)\), and \(|h|_p/\lambda\) is largest at \(\lambda=u\). (2) If
the slopes on \([1,p)\) lie in \(p^{-n}\mathbb{Z}\), then \(|f'_+(\lambda)|_p\le p^{n}\) and \(\lambda\ge1\) there,
so \(\|f\|_p\le p^{n}\) by (1). Conversely, if \(\|f\|_p\le p^{n}\), then for \(\lambda\in[1,p)\) we get
\(|f'_+(\lambda)|_p\le p^{n}\lambda<p^{n+1}\). The values of \(|\cdot|_p\) are \(0\) and powers of \(p\), so
\(|f'_+(\lambda)|_p\le p^{n}\). An element \(h\) of \(H_p\) with \(|h|_p\le p^{n}\) lies in \(p^{-n}\mathbb{Z}\).
(3) \((f+g)'_+=f'_++g'_+\), and \(|\cdot|_p\) is ultrametric. At each \(\lambda\), \((f\vee g)'_+(\lambda)\) is
\(f'_+(\lambda)\) or \(g'_+(\lambda)\), by the proof of Lemma 1.2. The rest is clear. \(\blacksquare\)

**Definition 6.15.** Let \(D\) be a divisor on \(C_p\) and \(n\in\mathbb{Z}\). Put

\[
X_n(D)=\{f\in\mathcal{K}(C_p)\text{ finite}:D+(f)\ge0,\ \|f\|_p\le p^{n}\},
\]

a metric space for the distance \(d(f,g)=\max_{\lambda\in[1,p]}|f(\lambda)-g(\lambda)|\). Let \(d_n(D)\) be the
topological dimension of \(X_n(D)\) (Definition 6.16 below) if \(X_n(D)\neq\emptyset\), and \(d_n(D)=0\) if
\(X_n(D)=\emptyset\). The *real dimension* of \(H^{0}(D)\) is

\[
\operatorname{Dim}_{\mathbb{R}}H^{0}(D)=\lim_{n\to\infty}p^{-n}\,d_n(D),
\]

when the limit exists.

The sets \(X_n(D)\) increase with \(n\), and their union is the set of finite elements of \(H^{0}(D)\). By
Lemma 6.14 each set \(X_n(D)\cup\{-\infty\}\) is a submodule of \(H^{0}(D)\). The element \(-\infty\) is left out
of \(X_n(D)\). Keeping it as an isolated point would give the same numbers \(d_n(D)\).

### 6.6 What is needed from dimension theory

**Definition 6.16.** Let \(X\) be a topological space and \(m\ge-1\) an integer. We write \(\mathrm{tdim}\,X\le m\)
when every open cover of \(X\) has a refinement by an open cover of \(X\) in which each point of \(X\) lies in at
most \(m+1\) members. The *topological dimension* \(\mathrm{tdim}\,X\) is the least such \(m\), or \(\infty\) if
there is none. It is invariant under homeomorphisms.

**Lemma 6.17.** Let \(X\) be a topological space and \(m\ge0\).

1. If \(Y\subseteq X\) is closed, then \(\mathrm{tdim}\,Y\le\mathrm{tdim}\,X\).
2. If \(X=Y\cup Z\) with \(Y,Z\) closed, \(\mathrm{tdim}\,Y\le m\) and \(\mathrm{tdim}\,Z\le m\), then
   \(\mathrm{tdim}\,X\le m\).
3. If \(X\) is the union of pairwise disjoint open subsets \(X_i\) with \(\mathrm{tdim}\,X_i\le m\), then
   \(\mathrm{tdim}\,X\le m\).

*Proof.* (1) Let \(\mathrm{tdim}\,X\le m\) and let \(\{Y\cap A_i\}\) be an open cover of \(Y\), with \(A_i\) open in
\(X\). The sets \(A_i\) and \(X\smallsetminus Y\) cover \(X\). Take a refinement \(\mathcal{V}\) as in the
definition. The sets \(V\cap Y\), \(V\in\mathcal{V}\), form an open cover of \(Y\) that refines \(\{Y\cap A_i\}\),
and each point of \(Y\) lies in at most \(m+1\) of them.

(2) *Step 1.* Let \(\mathcal{A}\) be an open cover of \(X\). We construct an open cover \(\mathcal{B}\) of \(X\)
that refines \(\mathcal{A}\) such that each point of \(Y\) lies in at most \(m+1\) members of \(\mathcal{B}\). The
sets \(A\cap Y\) cover \(Y\). Let \(\mathcal{W}\) be an open cover of \(Y\) refining them in which each point lies
in at most \(m+1\) members. For \(W\in\mathcal{W}\) choose an open set \(W'\) of \(X\) with \(W'\cap Y=W\) and a
set \(A_W\in\mathcal{A}\) containing \(W\). Let \(\mathcal{B}\) consist of the sets \(W'\cap A_W\) and the sets
\(A\smallsetminus Y\), \(A\in\mathcal{A}\). A point of \(Y\) lies in no set \(A\smallsetminus Y\), and it lies in
\(W'\cap A_W\) only if it lies in \(W\).

*Step 2.* Let \(\mathcal{A}\) be an open cover of \(X\). Apply Step 1 to get \(\mathcal{B}\). Apply Step 1 to
\(\mathcal{B}\) with \(Z\) in place of \(Y\) to get an open cover \(\mathcal{E}\) refining \(\mathcal{B}\) in
which each point of \(Z\) lies in at most \(m+1\) members. Choose a map
\(\varphi\colon\mathcal{E}\to\mathcal{B}\) with \(E\subseteq\varphi(E)\). For \(B\in\mathcal{B}\) let \(D(B)\) be
the union of the \(E\) with \(\varphi(E)=B\). The sets \(D(B)\) are open, \(D(B)\subseteq B\), and they cover
\(X\). Suppose a point \(x\) lies in \(D(B_1),\dots,D(B_r)\) with the \(B_i\) distinct. Then \(x\in E_i\) for some
\(E_i\) with \(\varphi(E_i)=B_i\); the \(E_i\) are distinct, and \(x\in B_i\). If \(x\in Y\), then \(r\le m+1\)
because of \(\mathcal{B}\). If \(x\in Z\), then \(r\le m+1\) because of \(\mathcal{E}\).

(3) Refine the cover on each \(X_i\) separately and take the union of the refinements. \(\blacksquare\)

**Theorem 6.18 (Lebesgue's covering theorem).** For every integer \(m\ge0\),
\(\mathrm{tdim}\,[0,1]^{m}=m\).

*Proof.* Let \(X\) be a compact Hausdorff space and \(k\ge-1\). Then \(\mathrm{tdim}\,X\le k\) holds exactly when
every finite open cover of \(X\) has an open refinement in which each point lies in at most \(k+1\) members, which
is the condition \(\dim X\le k\) of Covering dimension and finite trivializing covers, Definition 2.1.
One direction is clear. Conversely, given any open cover of \(X\), refine a finite subcover; the refinement also
refines the given cover. By Lebesgue's covering theorem and the dimension of cubes,
Theorem 4.3, \(\dim[0,1]^{m}=m\). \(\blacksquare\)

Covering dimension is treated in Covering dimension and finite trivializing covers.

**Corollary 6.19.** Let \(\Pi\subseteq\mathbb{R}^{M}\) be a non-empty compact convex set whose affine hull has
dimension \(d\). Then \(\mathrm{tdim}(\mathbb{R}\times\Pi)=d+1\).

*Proof.* Identify the affine hull of \(\Pi\) with \(\mathbb{R}^{d}\). Then \(S=\mathbb{R}\times\Pi\) is a closed
subset of \(\mathbb{R}^{d+1}\). A convex set has non-empty interior in its affine hull: a maximal affinely
independent subset \(\{c_0,\dots,c_d\}\) of \(\Pi\) spans the affine hull, the barycentric coordinates with
respect to it are continuous on the affine hull, and they are all positive near the barycentre of the \(c_i\); so a
neighbourhood of that point in the affine hull lies in \(\operatorname{conv}\{c_i\}\subseteq\Pi\). So \(S\) contains a closed
cube, which is a closed subset of \(S\) homeomorphic to \([0,1]^{d+1}\). By Lemma 6.17 (1) and Theorem 6.18,
\(\mathrm{tdim}\,S\ge d+1\).

For \(j\in\mathbb{Z}\) the set \(S_j=[j,j+1]\times\Pi\) is compact. It is a closed subset of a closed cube of
\(\mathbb{R}^{d+1}\), so \(\mathrm{tdim}\,S_j\le d+1\) by Lemma 6.17 (1) and Theorem 6.18. Let \(Y\) be the union
of the \(S_j\) with \(j\) even and \(Z\) the union of the \(S_j\) with \(j\) odd. Both are closed in \(S\). In
\(Y\) the sets \(S_j\) are pairwise disjoint, and each is open in \(Y\). So \(\mathrm{tdim}\,Y\le d+1\) by
Lemma 6.17 (3), and likewise for \(Z\). By Lemma 6.17 (2), \(\mathrm{tdim}\,S\le d+1\). \(\blacksquare\)

### 6.7 The model space

In this subsection a *convex integral function* is a convex continuous function \(g\colon[1,p]\to\mathbb{R}\)
which is affine with integral slope on each of finitely many intervals covering \([1,p]\). We write \(g'_+(1)\)
for its first slope and \(g'_-(p)\) for its last slope. For an integer \(N\) let \(E_N\) be the set of convex
integral functions \(g\) with

\[
g(1)=g(p)\qquad\text{and}\qquad-g'_+(1)+p\,g'_-(p)\le N,
\]

with the distance \(\max_{x\in[1,p]}|g_1(x)-g_2(x)|\) between two such functions \(g_1,g_2\).

**Lemma 6.20.** For every integer \(N\), restriction to \([1,p]\) is an isometry from \(X_0([H_p]\cdot N)\) onto
\(E_N\).

*Proof.* Let \(f\in\mathcal{K}(C_p)\) be finite and \(D=[H_p]\cdot N\). By Lemma 6.14, \(\|f\|_p\le1\) means that
the slopes of \(f\) on \([1,p)\) are integers. The condition \(D+(f)\ge0\) means \(j_f(\lambda)\ge0\) for
\(1<\lambda<p\), so that \(f\) is convex on \([1,p]\), and \(N+j_f(1)\ge0\). Since
\(f'_-(1)=p\,f'_-(p)\), we have \(j_f(1)=f'_+(1)-p\,f'_-(p)\). So the restriction of \(f\) lies in \(E_N\).
Conversely \(g\in E_N\) extends to the periodic function \(f(\lambda)=g(\lambda/p^{i})\) for
\(\lambda\in[p^{i},p^{i+1}]\), which is continuous because \(g(1)=g(p)\), has slopes in \(H_p\), and lies in
\(X_0(D)\). \(\blacksquare\)

For integers \(A,B\ge1\) let \(S(A,B)\) be the set of convex integral functions \(g\) with \(g(1)=g(p)\),
\(g'_+(1)\ge-A\) and \(g'_-(p)\le B\).

**Lemma 6.21.** Let \(A,B\ge1\) and \(m=A+B\). Let

\[
\Pi(A,B)=\Bigl\{u\in\mathbb{R}^{m}:1\le u_1\le u_2\le\dots\le u_m\le p,\ \ \sum_{i=1}^{m}(p-u_i)=A(p-1)\Bigr\}.
\]

For \(c\in\mathbb{R}\) and \(u\in\Pi(A,B)\) put
\(g_{c,u}(x)=c-A(x-1)+\sum_{i=1}^{m}\max(0,x-u_i)\). Then \((c,u)\mapsto g_{c,u}\) is a homeomorphism from
\(\mathbb{R}\times\Pi(A,B)\) onto \(S(A,B)\). The set \(\Pi(A,B)\) is compact and convex, and its affine hull has
dimension \(m-1\). Hence \(\mathrm{tdim}\,S(A,B)=A+B\).

*Proof.* *\(g_{c,u}\in S(A,B)\).* The function is convex with integral slopes. Its slope at \(x\) is \(-A\) plus
the number of \(i\) with \(u_i<x\), a number between \(-A\) and \(B\). Also \(g_{c,u}(1)=c\) and
\(g_{c,u}(p)=c-A(p-1)+\sum_i(p-u_i)=c\).

*Bijective.* Let \(g\in S(A,B)\). Its right slope \(g'_+\) on \([1,p)\) is a non-decreasing, right-continuous step
function with integral values between \(-A\) and \(B\). For \(1\le i\le m\) put

\[
u_i=\inf\bigl(\{x\in[1,p):g'_+(x)\ge-A+i\}\cup\{p\}\bigr).
\]

Then \(1\le u_1\le\dots\le u_m\le p\), and for \(x\in[1,p)\) we have \(g'_+(x)\ge-A+i\) exactly when \(x\ge u_i\).
So \(g'_+(x)=-A+\#\{i:u_i\le x\}\). Integrating from \(1\) to \(x\) gives \(g=g_{c,u}\) with \(c=g(1)\). The
condition \(g(p)=g(1)\) gives \(\sum_i(p-u_i)=A(p-1)\), so \(u\in\Pi(A,B)\). The pair \((c,u)\) is determined by
\(g\): \(c=g(1)\), and \(u\) is recovered from \(g'_+\) by the displayed formula.

*Homeomorphism.* We have \(|g_{c,u}-g_{c',u'}|\le|c-c'|+\sum_i|u_i-u'_i|\) on \([1,p]\), so the map is continuous.
The map \(u\mapsto g_{0,u}\) is a continuous bijection from the compact set \(\Pi(A,B)\) onto
\(\{g\in S(A,B):g(1)=0\}\), hence a homeomorphism: it maps closed subsets of \(\Pi(A,B)\), which are compact,
to compact and hence closed subsets of the metric space \(S(A,B)\). And \(g\mapsto(g(1),g-g(1))\) is a homeomorphism from
\(S(A,B)\) onto the product of \(\mathbb{R}\) with that set.

*The set \(\Pi(A,B)\).* It is closed, bounded and defined by linear conditions, so it is compact and convex. It
lies in the hyperplane \(\sum_iu_i=A+Bp\). Let \(\bar u=(A+Bp)/(A+B)\). Since \(A,B\ge1\), the number \(\bar u\)
lies strictly between \(1\) and \(p\). For a small positive \(\eta\), the point with
\(u_i=\bar u+(i-\tfrac{m+1}{2})\eta\) lies in the hyperplane, and its coordinates are strictly increasing and lie
strictly between \(1\) and \(p\). All points of the hyperplane near it lie in \(\Pi(A,B)\). So the affine hull
of \(\Pi(A,B)\) is the hyperplane, of dimension \(m-1\). Corollary 6.19 gives
\(\mathrm{tdim}\,S(A,B)=m\). \(\blacksquare\)

**Proposition 6.22 (dimension of the model space).** Let \(N\ge1\) be an integer. Then

\[
\mathrm{tdim}\,X_0([H_p]\cdot N)=\mathrm{tdim}\,E_N=\max(N-p+1,\,1).
\]

In particular it is \(N-p+1\) for \(N\ge p\).

*Proof.* The first equality is Lemma 6.20. Let \(g\in E_N\) be non-constant. The slopes of the convex function
\(g\) are non-decreasing, and \(g(1)=g(p)\). If the first slope were \(\ge0\), all slopes would be \(\ge0\) and
\(g(p)=g(1)\) would force them to be \(0\). So \(\alpha=-g'_+(1)\ge1\), and in the same way
\(\beta=g'_-(p)\ge1\). These are integers with \(\alpha+p\beta\le N\), and \(g\in S(\alpha,\beta)\). Conversely
\(S(A,B)\subseteq E_N\) when \(A+pB\le N\). Let \(P_N\) be the finite set of pairs of integers \(A,B\ge1\) with
\(A+pB\le N\). Then

\[
E_N=\{\text{constants}\}\ \cup\bigcup_{(A,B)\in P_N}S(A,B).
\]

The set of constants is closed in \(E_N\) and isometric to \(\mathbb{R}\), so its dimension is \(1\) by
Corollary 6.19. Each \(S(A,B)\) is closed in \(E_N\): for a convex function \(g\) on \([1,p]\), the condition
\(g'_+(1)\ge-A\) is equivalent to \(g(x)\ge g(1)-A(x-1)\) for all \(x\), and \(g'_-(p)\le B\) is equivalent to
\(g(x)\ge g(p)+B(x-p)\) for all \(x\); both pass to uniform limits. By Lemma 6.21,
\(\mathrm{tdim}\,S(A,B)=A+B\). For \((A,B)\in P_N\),

\[
A+B=(A+pB)-(p-1)B\le N-(p-1),
\]

with equality for \((A,B)=(N-p,1)\), which lies in \(P_N\) when \(N\ge p+1\). By Lemma 6.17 (1) and (2),
\(\mathrm{tdim}\,E_N\) is the largest of the dimensions of these closed pieces. For \(N\ge p+1\) this is
\(N-p+1\). For \(N\le p\) the set \(P_N\) is empty, \(E_N\) consists of the constants, and the dimension is \(1\).
\(\blacksquare\)

*Reference:* [Connes–Consani 2017, Lemma 5.19 (iv)] states the value \(N-p+1\) for every integer \(N>0\); for
\(N<p\) the space consists of the constants and has dimension \(1\), so we prove the value \(\max(N-p+1,1)\).

### 6.8 The Riemann–Roch theorem on \(C_p\)

**Lemma 6.23.** Let \(D\) be a divisor on \(C_p\) and \(n\in\mathbb{Z}\).

1. For \(m\in\mathbb{Z}\), \(f\mapsto p^{m}f\) is a bijection \(X_n(D)\to X_{n-m}(p^{m}D)\) that multiplies
   distances by \(p^{m}\). So \(d_n(D)=d_0(p^{n}D)\).
2. If \(g\in\mathcal{K}(C_p)\) is finite and \(\|g\|_p\le p^{n}\), then \(f\mapsto f-g\) is an isometry
   \(X_n(D)\to X_n(D+(g))\). So \(d_n(D)=d_n(D+(g))\).
3. If \(D'\le D\), then \(X_n(D')\) is a closed subset of \(X_n(D)\). So \(d_n(D')\le d_n(D)\).

*Proof.* (1) The function \(p^{m}f\) has slopes in \(H_p\), \((p^{m}f)=p^{m}(f)\) and
\(\|p^{m}f\|_p=p^{-m}\|f\|_p\). (2) \(D+(g)+(f-g)=D+(f)\) and
\(\|f-g\|_p\le\max(\|f\|_p,\|g\|_p)\le p^{n}\); the inverse map is \(f\mapsto f+g\). (3) The inclusion is clear.
Let \(f_k\in X_n(D')\) converge uniformly to \(f\in X_n(D)\), and let \(\lambda_0>0\). Put
\(c=D'(\lambda_0H_p)/\lambda_0\). Choose an open interval \(I\ni\lambda_0\) such that \(D'(\lambda H_p)=0\) for
all \(\lambda\in I\), \(\lambda\neq\lambda_0\). On \(I\) the function
\(f_k(\lambda)+c\max(0,\lambda-\lambda_0)\) is piecewise affine, and all its jumps are \(\ge0\): at
\(\lambda\ne\lambda_0\) because \(D'+(f_k)\ge0\), and at \(\lambda_0\) because
\(j_{f_k}(\lambda_0)+c\ge0\). So it is convex on \(I\). A uniform limit of convex functions is convex, because the
inequality \(h(tx+(1-t)y)\le th(x)+(1-t)h(y)\) passes to pointwise limits. So
\(f(\lambda)+c\max(0,\lambda-\lambda_0)\) is convex on \(I\), which gives \(j_f(\lambda_0)+c\ge0\). This is
\(D'(\lambda_0H_p)+\mathrm{ord}_{\lambda_0H_p}(f)\ge0\). Hence \(f\in X_n(D')\). The inequality for \(d_n\)
follows from Lemma 6.17 (1); it is trivial when \(X_n(D')\) is empty. \(\blacksquare\)

**Theorem 6.24 (Riemann–Roch on the periodic orbit).** For every divisor \(D\) on \(C_p\) the limit
\(\operatorname{Dim}_{\mathbb{R}}H^{0}(D)\) exists, and

\[
\operatorname{Dim}_{\mathbb{R}}H^{0}(D)=\max(\deg D,\,0).
\]

Consequently, for every divisor \(D\),

\[
\operatorname{Dim}_{\mathbb{R}}H^{0}(D)-\operatorname{Dim}_{\mathbb{R}}H^{0}(-D)=\deg D .
\]

*Proof.* If \(\deg D<0\), all \(X_n(D)\) are empty by Lemma 6.12, and the limit is \(0\). If \(\deg D=0\), then
by Lemma 6.12 each \(X_n(D)\) is empty or is a set \(\{c-g:c\in\mathbb{R}\}\), isometric to \(\mathbb{R}\). So
\(d_n(D)\le1\) and the limit is \(0\).

Let \(\delta=\deg D>0\) and \(0<\varepsilon<\delta\). The set of \(\alpha\in H_p\) with \(\chi(\alpha)=\chi(D)\)
is a coset of \((p-1)H_p\), so it is dense in \(\mathbb{R}\). Choose such \(\alpha_1,\alpha_2\) with
\(\delta-\varepsilon<\alpha_1<\delta<\alpha_2<\delta+\varepsilon\). For a real number \(e>0\) the divisor
\(P(e)=[\tfrac{e}{p-1}H_p]\cdot e\) is effective, of degree \(e\), with \(\chi(P(e))=\chi(p-1)=0\). Put

\[
D_1=[H_p]\cdot\alpha_1+P(\delta-\alpha_1),\qquad D_2=[H_p]\cdot\alpha_2-P(\alpha_2-\delta).
\]

Both have degree \(\delta\) and invariant \(\chi(\alpha_j)=\chi(D)\). By Theorem 6.6 there are finite
\(g_1,g_2\in\mathcal{K}(C_p)\) with \(D_j=D+(g_j)\). Let \(n\) be so large that \(\|g_j\|_p\le p^{n}\), that
\(p^{n}\alpha_j\in\mathbb{Z}\) and that \(p^{n}\alpha_1\ge p\). By Lemma 6.23 and Proposition 6.22,

\[
d_n(D)=d_n(D_1)\ \ge\ d_n([H_p]\cdot\alpha_1)=d_0([H_p]\cdot p^{n}\alpha_1)=p^{n}\alpha_1-p+1 ,
\]
\[
d_n(D)=d_n(D_2)\ \le\ d_n([H_p]\cdot\alpha_2)=d_0([H_p]\cdot p^{n}\alpha_2)=p^{n}\alpha_2-p+1 .
\]

Hence \(\alpha_1-(p-1)p^{-n}\le p^{-n}d_n(D)\le\alpha_2-(p-1)p^{-n}\) for all large \(n\). So the lower and upper
limits of \(p^{-n}d_n(D)\) lie between \(\delta-\varepsilon\) and \(\delta+\varepsilon\). Since \(\varepsilon\) is
arbitrary, the limit exists and equals \(\delta\). The last formula follows:
\(\max(\delta,0)-\max(-\delta,0)=\delta\). \(\blacksquare\)

*Reference:* [Connes–Consani 2017, Theorem 5.17].

**Remarks.** (a) For a smooth projective curve of genus one the Riemann–Roch theorem reads
\(\ell(D)-\ell(-D)=\deg D\). Theorem 6.24 has the same form, with real-valued dimensions and real-valued degrees.
Putting \(\operatorname{Dim}_{\mathbb{R}}H^{1}(D)=\operatorname{Dim}_{\mathbb{R}}H^{0}(-D)\) turns Serre duality
into a definition; no independent definition of \(H^{1}\) is used.

(b) The real numbers come from the density of \(H_p\) in \(\mathbb{R}\). At level \(n\) the slopes lie in the
discrete group \(p^{-n}\mathbb{Z}\) and the dimension is an integer, of size about \(p^{n}\deg D\). Dividing by
\(p^{n}\) gives a real limit.

(c) The proof uses only the divisor class group (Theorem 6.6), the model space (Proposition 6.22) and the three
operations of Lemma 6.23. It uses nothing about other primes.

**Example 6.25 (\(p=3\)).** Let \(D=[H_3]\cdot4\). Then \(P_4=\{(1,1)\}\) and \(X_0(D)\cong E_4=S(1,1)\). The set
\(\Pi(1,1)\) consists of the pairs \((u,4-u)\) with \(1\le u\le2\), and

\[
g_{c,u}(x)=c+\max(1-x,\ 1-u,\ x-3)\qquad(1\le x\le3).
\]

So \(X_0(D)\) is homeomorphic to \(\mathbb{R}\times[1,2]\), of dimension \(2=4-3+1\). For \(u=1\) the function is
the constant \(c\). At level \(n\ge0\), \(d_n(D)=d_0([H_3]\cdot4\cdot3^{n})=4\cdot3^{n}-2\), and
\(3^{-n}d_n(D)\to4=\deg D\).

For \(D=[H_3]\cdot2\) we have \(N=2<p\). Then \(X_0(D)\) consists of the constants and has dimension \(1\), while
\(N-p+1=0\). Still \(d_n(D)=2\cdot3^{n}-2\) for \(n\ge1\), and
\(\operatorname{Dim}_{\mathbb{R}}H^{0}(D)=2\).

## 7. The scaling site and the Riemann hypothesis

This section says what the scaling site contributes to the plan of carrying Weil's proof over to the Riemann zeta
function, and what is missing. Each statement below is proved in this lesson, or cited with a locator, or
formulated as an open problem.

### 7.1 The three ingredients of Weil's proof

For a curve \(C\) over \(\mathbb{F}_q\), the proof of the Riemann hypothesis, in the form recalled in
[Connes 2015, Section 2.3], uses three ingredients. The lesson *Weil's proof for curves and what is missing over
the integers* carries out the same proof on the surface \(C\times C\) over \(\mathbb{F}_q\), without extension of
scalars, and obtains the inequality of (W3) from the Hodge index theorem.

- (W1) The curve \(\bar C=C\otimes_{\mathbb{F}_q}\bar{\mathbb{F}}_q\), its points
  \(\bar C(\bar{\mathbb{F}}_q)=C(\bar{\mathbb{F}}_q)\) and the Frobenius acting on them. The numbers \(N(q^{r})\)
  of fixed points of the powers of the Frobenius determine the zeta function:
  \(-\tfrac{d}{ds}\log\zeta_C(s)=\sum_{r\ge1}N(q^{r})\,(\log q)\,q^{-rs}\).
- (W2) The surface \(\bar C\times\bar C\), and the graphs of the powers of the Frobenius as divisors on it.
- (W3) Intersection theory on this surface, and an inequality for the self-intersection numbers of these divisors.
  The inequality follows from the Hodge index theorem or, in the proof of Mattuck–Tate and Grothendieck, from the
  Riemann–Roch theorem on the surface [Connes 2015, Sections 2.2 and 2.3]. It implies the Riemann hypothesis for
  \(C\).

**Ingredient (W1) exists for \(\mathbb{Q}\).** The structure sheaf of the scaling site \(\mathscr{S}\) is a sheaf of
\(\mathbb{R}_{\max}\)-algebras whose global sections are the constants (Definition 3.5 and Proposition 3.8), and it
is obtained from the structure sheaf of the arithmetic site by extension of scalars (Theorem 2.5 and
Proposition 3.6). The points of \(\mathscr{S}\) over \(\mathbb{R}_{\max}\) are those of the arithmetic site, they
form the space \(X_{\mathbb{Q}}=\mathbb{Q}^{\times}\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb{Z}}^{\times}\),
and the group \(\mathrm{Aut}(\mathbb{R}_{\max})=\mathbb{R}_{>0}\) acts on them by the scaling action (Theorem 4.11
and Corollary 5.4). The stabilizers are known (Proposition 6.1): a number \(\mu\neq1\) fixes the class \([a,x]\)
with \(x\ne0\) exactly when \(\mu\) is a product of powers of primes \(p\) with \(a_p=0\), and every \(\mu\)
fixes the classes \([a,0]\).

The analogue of the formula in (W1) is the following statement. Let \(\Lambda\) be the von Mangoldt function,
\(\gamma\) Euler's constant and \(c=\tfrac12(\log\pi+\gamma)\). For a function \(h\) on \([1,\infty)\) put

\[
N(h)=\sum_{n\ge1}\Lambda(n)\,h(n)+\int_1^{\infty}\frac{u^{2}h(u)-h(1)}{u^{2}-1}\,\frac{du}{u}+c\,h(1),
\]

when the sum and the integral converge absolutely.

**Proposition 7.1 (the counting distribution).** For every complex number \(s\) with \(\mathrm{Re}(s)>1\),

\[
N(u^{-s})=-\frac{d}{ds}\log\zeta_{\mathbb{Q}}(s),\qquad \zeta_{\mathbb{Q}}(s)=\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s).
\]

*Proof.* For \(\mathrm{Re}(s)>1\) we have \(\sum_n\Lambda(n)n^{-s}=-\zeta'(s)/\zeta(s)\)
(Dirichlet series and Euler products, Section 3). In the integral
substitute \(t=u^{-2}\):

\[
\int_1^{\infty}\frac{u^{2-s}-1}{u^{2}-1}\,\frac{du}{u}=\frac12\int_0^{1}\frac{t^{s/2-1}-1}{1-t}\,dt
=-\frac12\Bigl(\frac{\Gamma'}{\Gamma}\Bigl(\frac s2\Bigr)+\gamma\Bigr).
\]

The last equality is Gauss's formula
\(\frac{\Gamma'}{\Gamma}(z)=-\gamma+\int_0^{1}\frac{1-t^{z-1}}{1-t}\,dt\) for \(\mathrm{Re}(z)>0\)
(The Gamma function and Stirling's formula, Proposition 5.1). So

\[
N(u^{-s})=-\frac{\zeta'(s)}{\zeta(s)}-\frac12\frac{\Gamma'}{\Gamma}\Bigl(\frac s2\Bigr)+\frac12\log\pi
=-\frac{d}{ds}\log\bigl(\pi^{-s/2}\Gamma(s/2)\zeta(s)\bigr).\qquad\blacksquare
\]

*Reference:* [Connes–Consani 2016b, Theorem 4.2].

So \(N\) plays the role of the measure \(\sum_rN(q^{r})(\log q)\,\delta_{q^{r}}\) of a curve. Its first term is
\(\sum_p\sum_{m\ge1}(\log p)\,h(p^{m})\). In [Connes–Consani 2016b, Section 4] the functional \(N\) is obtained as
the distribution that counts the fixed points of the scaling action on \(X_{\mathbb{Q}}\). The term
\((\log p)\,h(p^{m})\) is the contribution of the classes \([a,x]\) with \(a_p=0\), which are fixed by
\(\mu=p^{m}\). Its coefficient \(\log p\) equals the length of the periodic orbits of period \(\log p\). The other
two terms are the contribution of the classes \([a,0]\), which are fixed by all \(\mu\). This derivation uses a
trace formula for the scaling action and is not proved in this lesson.

Among the points \([a,x]\) with \(a_p=0\), those with \(x\neq0\) and \(a_q\neq0\) for every prime \(q\neq p\) lie
on periodic orbits of period \(\log p\) (Proposition 6.1). A point with \(x=0\) is fixed by every scaling, and a
point with \(x\neq0\) and \(a_q=0\) for a second prime \(q\) has a dense stabilizer: for example \(a_2=a_3=0\), all
other finite components equal to \(1\), and \(x=1\) give \(H=\mathbb{Z}[1/6]\). On the orbit \(C_p\) through the point of
the prime \(p\), the structure sheaf defines a curve: rational functions, divisors with real degrees, the divisor
class group \(\mathbb{R}\times\mathbb{Z}/(p-1)\mathbb{Z}\), theta functions and a Riemann–Roch theorem
(Theorems 6.6, 6.10 and 6.24).

**Ingredient (W2) exists over \(\mathbb{B}\).** The square of the arithmetic site and the Frobenius
correspondences \(\Psi(\lambda)\), \(\lambda\in\mathbb{R}_{>0}\), are constructed in [Connes–Consani 2016b,
Sections 6 and 7], with the composition law [Connes–Consani 2016b, Theorem 7.7]; *The arithmetic site* constructs
them in Section 5 and proves the composition law in Section 6 (Theorem 6.8).

**Ingredient (W3) is missing.** The next two subsections make this precise.

### 7.2 The inequality that has to be proved

For real functions \(f,g\) with compact support in \(\mathbb{R}_{>0}\) put

\[
(f\star g)(u)=\int_0^{\infty}f(v)\,g(u/v)\,\frac{dv}{v},\qquad \tilde g(u)=u^{-1}g(u^{-1}),\qquad
\mathfrak{s}(f,g)=N(f\star\tilde g),
\]

with \(N\) as in Section 7.1.

**Theorem 7.2 (Weil's positivity criterion).** The Riemann hypothesis holds if and only
if

\[
\mathfrak{s}(f,f)\le0\qquad\text{for all }f\text{ with }\int_0^{\infty}f(u)\,\frac{du}{u}=0\text{ and }\int_0^{\infty}f(u)\,du=0 .
\]

Here \(f\) runs over the real smooth functions with compact support in \(\mathbb{R}_{>0}\). For them
\(f\star\tilde f\) is smooth with compact support, and \(\mathfrak{s}(f,f)=N(f\star\tilde f)\) is defined.

*Reference:* [Connes 2015, Section 3.1] and [Connes–Consani 2018, Section 3.1] state the criterion in this form for
real functions with compact support, without a condition of regularity, and the latter refers to
[Bombieri–Lagarias 1999] for it. Without regularity the integral in \(N(f\star\tilde f)\) need not converge, so we
state the criterion for smooth \(f\).

*Proof of the implication from the Riemann hypothesis.* Put \(\widehat f(z)=\int_0^{\infty}f(u)\,u^{z}\,\frac{du}{u}\).
The two conditions in Theorem 7.2 are \(\widehat f(0)=0\) and \(\widehat f(1)=0\). Let \(h=f\star\tilde f\). Then
\(\widehat h(z)=\widehat f(z)\,\widehat f(1-z)\), \(h\) is smooth with compact support, and \(x^{-1}h(x^{-1})=h(x)\),
because \(\tilde f(u)=u^{-1}f(u^{-1})\) and the convolution is commutative. The explicit formula
(The explicit formula with general test functions, Theorem 2.1), applied to \(h\), reads

\[
\widehat h(0)-\lim_{T\to\infty}\sum_{|\mathrm{Im}\,\rho|<T}\widehat h(\rho)+\widehat h(1)
=2\sum_{n\ge1}\Lambda(n)h(n)+(\log4\pi+\gamma)\,h(1)+2\int_1^{\infty}\frac{xh(x)-h(1)}{x^{2}-1}\,dx ,
\]

where \(\rho\) runs over the non-trivial zeros of \(\zeta\), counted with multiplicity. Since
\(\frac{xh(x)-h(1)}{x^{2}-1}-\frac{x^{2}h(x)-h(1)}{x(x^{2}-1)}=-\frac{h(1)}{x(x+1)}\) and
\(\int_1^{\infty}\frac{dx}{x(x+1)}=\log2\), the right side is \(2N(h)\). The two conditions give
\(\widehat h(0)=\widehat h(1)=0\), so

\[
\mathfrak{s}(f,f)=N(h)=-\frac12\lim_{T\to\infty}\sum_{|\mathrm{Im}\,\rho|<T}\widehat f(\rho)\,\widehat f(1-\rho).
\]

If the Riemann hypothesis holds, then \(1-\rho=\bar\rho\) for every zero. Since \(f\) is real,
\(\widehat f(\bar\rho)=\overline{\widehat f(\rho)}\), so each term is \(|\widehat f(\rho)|^{2}\), and
\(\mathfrak{s}(f,f)\le0\). \(\blacksquare\)

*Proof of the converse.* Suppose that \(\mathfrak{s}(f,f)\le0\) for all \(f\) as in the theorem. Let \(g=a+ib\) be a
complex smooth function with compact support in \(\mathbb{R}_{>0}\), with \(a,b\) real, and let \(G,A,B\) be the
transforms of \(g,a,b\) defined as \(\widehat f\) above. Suppose \(G(0)=G(1)=0\). The numbers \(A(0),A(1),B(0),B(1)\)
are real, so all four vanish, and \(a\) and \(b\) satisfy the two conditions of the theorem. For a real function
\(a\) one has \(\overline{A(\bar z)}=A(z)\). In the notation of Weil's positivity criterion, (1.1)–(1.6),
with \(\mathcal{W}(g)\) the sum over the places of the explicit formula for \(g*\bar g^\sharp\), this gives

\[
\mathcal{W}(g)=-\sum_\rho G(\rho)\,\overline{G(1-\bar\rho)}
=-\sum_\rho\bigl(A(\rho)+iB(\rho)\bigr)\bigl(A(1-\rho)-iB(1-\rho)\bigr),
\]

a sum that converges absolutely by the Mellin bound of Weil's positivity criterion, Lemma 2.2.
The nontrivial zeros, with their multiplicities, are the zeros of the completed zeta function \(\xi\), and
\(\xi(s)=\xi(1-s)\) (Poisson summation, theta, and the functional equation, Theorem 3.1). So the
multiset of zeros is invariant under \(\rho\mapsto1-\rho\), the sums \(\sum_\rho B(\rho)A(1-\rho)\) and
\(\sum_\rho A(\rho)B(1-\rho)\) are equal, and the cross terms cancel: \(\mathcal{W}(g)=\mathcal{W}(a)+\mathcal{W}(b)\).
For real \(a\), \(\mathcal{W}(a)\) is the right side of the explicit formula for \(a\star\tilde a\), which is
\(2N(a\star\tilde a)=2\,\mathfrak{s}(a,a)\) by the computation in the first part of the proof. Hence
\(\mathcal{W}(g)=2\,\mathfrak{s}(a,a)+2\,\mathfrak{s}(b,b)\le0\). By Weil's positivity criterion, Theorem 4.1,
applied with the set \(F=\{0,1\}\), which contains no nontrivial zero, the Riemann hypothesis holds. \(\blacksquare\)

For the larger class \(\mathcal G\) of test functions of
Weil's proof for curves and what is missing over the integers, Theorem 6.4,
positivity on all of \(\mathcal G\) implies the Riemann hypothesis as well; Theorem 7.2 shows that the compactly
supported smooth functions with the two vanishing conditions already suffice.

So the Riemann hypothesis is a statement about the counting distribution of Proposition 7.1: it is non-positive
on the functions \(f\star\tilde f\) with the two vanishing conditions. For a curve over \(\mathbb{F}_q\) the
corresponding inequality is the one obtained in (W3).

### 7.3 Open problems

The works cited in this lesson describe the following steps as not carried out. We formulate them as problems.

**Problem A (divisors and intersection numbers on the square).** Construct a square of the scaling site over
\(\mathbb{R}_{\max}\), a notion of divisor on it for which

\[
D(f)=\int_0^{\infty}f(\lambda)\,\Psi(\lambda)\,\frac{d\lambda}{\lambda}
\]

is a divisor for every \(f\) as in Theorem 7.2, and a symmetric intersection pairing such that the
self-intersection number of \(D(f)\) is a fixed positive multiple of \(\mathfrak{s}(f,f)\). In
[Connes 2015, Section 4.3] the expected relation is \(\tfrac12D(f).D(f)=\mathfrak{s}(f,f)\). In
[Connes–Consani 2018, Section 3.1] the pairing is written down by a formula that uses the distribution \(N\), with
the normalization \(D(f)\bullet D(f)=\mathfrak{s}(f,f)\). The two normalizations differ by the factor \(2\), which
does not change the sign of the self-intersection number. No intersection theory is developed in either work;
[Connes–Consani 2018, Section 3.4] lists it as a step to be carried out.

**Problem B (cohomology).** Define the cohomology \(H^{1}\) of the relevant sheaves of modules over semirings of
characteristic one on the square. According to [Connes–Consani 2018, Introduction], the definition of \(H^{0}\) is
straightforward, \(H^{2}\) can be defined by turning Serre duality into a definition, and the definition of
\(H^{1}\) is open.

**Problem C (a Riemann–Roch inequality on the square).** Prove, for the divisors \(D=D(f)\), an inequality of the
form

\[
\operatorname{Dim}H^{0}(D)+\operatorname{Dim}H^{0}(-D)\ \ge\ \tfrac12\,D.D ,
\]

with a real-valued dimension as in Section 6.5. This is the form proposed in [Connes 2015, Section 4.3]. In the
normalization of that work the right side is \(\mathfrak{s}(f,f)\).

**Problem D (from existence to a contradiction).** Show that if \(\operatorname{Dim}H^{0}(D(f))>0\) or
\(\operatorname{Dim}H^{0}(-D(f))>0\), then \(D(f)\) or \(-D(f)\) is equivalent to an effective divisor that is not
zero, and that a non-zero effective divisor cannot have degree and codegree \(0\). In
[Connes–Consani 2018, Section 3.1] the two vanishing conditions of Theorem 7.2 are read as the vanishing of the
degree and the codegree of \(D(f)\). For a surface \(\bar C\times\bar C\) the corresponding facts are stated in
[Connes 2015, Section 2.3]: a divisor \(D\) with \(\dim H^{0}(D)>1\) is equivalent to a strictly positive divisor,
and the sum of the two degrees of a strictly positive divisor is positive. The hypothesis has to be a positive
dimension, not only \(H^{0}\neq\{-\infty\}\): on \(C_p\) a principal divisor \(D\) has \(H^{0}(D)\neq\{-\infty\}\)
and degree \(0\) (Lemma 6.12), while \(\operatorname{Dim}_{\mathbb{R}}H^{0}(D)>0\) forces \(\deg D>0\)
(Theorem 6.24).

If Problems A, C and D were solved, a function \(f\) as in Theorem 7.2 with \(\mathfrak{s}(f,f)>0\) would lead to a
contradiction: by A and C one of the two dimensions would be positive, and D would exclude this. Theorem 7.2
would then give the Riemann hypothesis. Problem B enters through Problem C. For a surface over a field the
inequality is obtained from a Riemann–Roch equality that contains the term \(\dim H^{1}\), by leaving this term
out [Connes 2015, Section 2.3]. None of the four problems is solved in the works cited here. A second route
is proposed in [Connes–Consani 2018, Section 3.4]: construct a complex lift of the scaling site, prove a
Riemann–Roch formula of Hirzebruch type on its square, and descend to characteristic one by tropicalization. That
reference lists five steps and singles out the Riemann–Roch formula on the square as the most problematic one.

### 7.4 What the Riemann–Roch theorem on \(C_p\) shows

Theorem 6.24 is a test of the definitions in dimension one. It shows that a module \(H^{0}(D)\) over
\(\mathbb{R}_{\max}\), which is far from finitely generated, has a well-defined real dimension, and that this
dimension satisfies the Riemann–Roch formula of a curve of genus one. The dimension is not defined from the
\(\mathbb{R}_{\max}\)-module structure alone: its definition uses the filtration by the \(p\)-adic size of the
slopes.

Theorem 6.24 does not give information about the zeros of \(\zeta\). Its statement and its proof involve one prime
at a time, no square, and no correspondence. The orbits \(C_p\) for different primes are disjoint subsets of
\(X_{\mathbb{Q}}\), and the works cited here contain no Riemann–Roch theorem for the scaling site as a whole.

## 8. Exercises

**Exercise 1 (cancellation in \(T\)).** In \(T=\mathbb{Z}_{\max}\otimes_{\mathbb{B}}\mathbb{R}_{\max}\) let
\(a=Q(0,0)\cup Q(3,-1)\) and \(q=Q(1,-\tfrac12)\).

- (a) Show that \(q\not\subseteq a\) and that \(L(a\cup q)=L(a)\).
- (b) Find integers \(d,e\) as in Step 1 of the proof of Lemma 2.4.
- (c) Verify directly that \((a\cup q)\cdot C=a\cdot C\) for \(C=(a\cup q)^{2}\).

*Solution.* (a) The point \((1,-\tfrac12)\) is not \(\le(0,0)\), since \(1>0\), and not \(\le(3,-1)\), since
\(-\tfrac12>-1\). Next \(L(a)(\lambda)=\max(0,3\lambda-1)\) and \(L(q)(\lambda)=\lambda-\tfrac12\). For
\(\lambda\le\tfrac12\) we have \(\lambda-\tfrac12\le0\). For \(\lambda\ge\tfrac12\) we have
\(3\lambda-1-(\lambda-\tfrac12)=2\lambda-\tfrac12>0\). So \(L(q)\le L(a)\) and \(L(a\cup q)=L(a)\).

(b) The function \(g=L(a)-L(q)\) has slope \(-1\) on \([0,\tfrac13]\) and slope \(2\) after \(\tfrac13\). Its
minimum is at \(\lambda_0=\tfrac13\), where both quadrants of \(a\) are active. With \(A=(0,0)\), \(B=(3,-1)\),
\(P=(1,-\tfrac12)\) we get \(d=3\), \(e=1\), and \(3P=(3,-\tfrac32)\le2A+B=(3,-1)\).

(c) The corners of \(C=(a\cup q)^{2}\) are the sums of two of \(A,B,P\). The corners of \((a\cup q)\cdot C\) are the
sums of three of \(A,B,P\). The corners of \(a\cdot C\) are the sums of three of \(A,B,P\) in which \(A\) or \(B\)
occurs. The only sum of three not of this kind is \(3P=(3,-\tfrac32)\), and \(Q(3P)\subseteq Q(2A+B)\). So both
products are the union of the same quadrants.

**Exercise 2 (why the subgroups have rank one).** Let \(H=\mathbb{Z}+\mathbb{Z}\sqrt2\) and define
\(F(\Omega)=\Omega\cap H\cap(0,\infty)\), \(F(n)(h)=nh\). Show that \(F\) is a functor on \(\mathcal{C}\) that
satisfies (F1), (F3) and (F4) but not (F2).

*Solution.* Multiplication by \(n\) maps \(\Omega\cap H\cap(0,\infty)\) into \(\Omega'\cap H\cap(0,\infty)\) when
\(n\Omega\subseteq\Omega'\), so \(F\) is a functor. (F1) and (F4) hold as for \(F_H\) in Proposition 4.3. (F3):
\(nh=mh\) with \(h>0\) gives \(n=m\). For (F2) take \(a_1=1\) and \(a_2=\sqrt2\) in \(F((0,2))\). If there were an
object \(W\), an element \(a\in F(W)\) and morphisms \(n_1,n_2\) with \(n_1a=1\) and \(n_2a=\sqrt2\), then
\(\sqrt2=n_2/n_1\) would be rational. So \(F\) is not flat and defines no point. By Lemma 4.8, condition (F2) is
what forces the elements of a point over \((0,\infty)\) to have rational ratios.

**Exercise 3 (the scaling action on the curve \(C_p\)).** Let \(\mu\in\mathbb{R}_{>0}\). For
\(f\in\mathcal{K}(C_p)\) finite put \((S_\mu f)(\lambda)=\mu f(\lambda/\mu)\). For a divisor \(D\) let \(\mu_*D\) be
the divisor with \((\mu_*D)(\mu H)=\mu D(H)\).

- (a) Show that \(S_\mu\) is an automorphism of the semifield \(\mathcal{K}(C_p)\) which acts on the constants by
  \(\mathrm{Fr}_\mu\), and that \((S_\mu f)=\mu_*(f)\).
- (b) Show that \(\deg(\mu_*D)=\mu\deg D\) and \(\chi(\mu_*D)=\chi(D)\).
- (c) What is \(p_*D\)?

*Solution.* (a) The function \(S_\mu f\) is continuous, \(p\)-periodic, and its slopes at \(\lambda\) are the
slopes of \(f\) at \(\lambda/\mu\), so they lie in \(H_p\). The map \(S_\mu\) preserves maxima and sums, sends the
constant \(c\) to \(\mu c\), and has the inverse \(S_{1/\mu}\). The jump of \(S_\mu f\) at \(\mu\lambda_0\) is
\(j_f(\lambda_0)\). So
\(\mathrm{ord}_{\mu\lambda_0H_p}(S_\mu f)=\mu\lambda_0j_f(\lambda_0)=\mu\,\mathrm{ord}_{\lambda_0H_p}(f)\).
(b) The degree is multiplied by \(\mu\) by definition. For \(H=\lambda H_p\) and \(d\in H\),
\(\chi_{\mu H}(\mu d)=\chi(\mu d/(\mu\lambda))=\chi_H(d)\). So the scaling action maps principal divisors to
principal divisors and acts on
\(\mathrm{Div}(C_p)/\mathcal{P}\cong\mathbb{R}\times\mathbb{Z}/(p-1)\mathbb{Z}\) by
\((\delta,c)\mapsto(\mu\delta,c)\). (c) Since \(pH=H\), we get \(p_*D=pD\). The
element \(p\) fixes every point of \(C_p\) but multiplies every divisor by \(p\). This agrees with Theorem 6.24:
\(\operatorname{Dim}_{\mathbb{R}}H^{0}(pD)=p\operatorname{Dim}_{\mathbb{R}}H^{0}(D)\).

**Exercise 4 (a principal divisor on \(C_5\)).** Let \(p=5\) and
\(D=[H_5]\cdot1-[2H_5]\cdot4+[3H_5]\cdot3\).

- (a) Compute \(\deg D\) and \(\chi(D)\).
- (b) Find a function \(f\in\mathcal{K}(C_5)\) with \((f)=D\) by the method of Theorem 6.6.
- (c) Find it again with theta functions.

*Solution.* (a) \(\deg D=1-4+3=0\). With \(\lambda_0=1,\lambda_1=2,\lambda_2=3\) the coefficients are
\(\lambda_ja_j\) with \(a_0=1\), \(a_1=-2\), \(a_2=1\). So \(\chi(D)=\chi(1-2+1)=0\) in
\(\mathbb{Z}/4\mathbb{Z}\). (b) Here \(\sigma=0\), so \(h_3=0\), \(h_2=h_3-a_2=-1\), \(h_1=h_2-a_1=1\), and
\(h_1-5h_3=1=a_0\). The function has slope \(1\) on \([1,2]\), slope \(-1\) on \([2,3]\), slope \(0\) on \([3,5]\)
and \(f(1)=0\). So \(f(\lambda)=\max(0,1-|\lambda-2|)\) on \([1,5]\), extended by \(f(5\lambda)=f(\lambda)\).

(c) In Theorem 6.10 we have \((h,\mu)=(1,1)\) and \((1,3)\) for the positive part and \((h',\mu')=(2,4)\) for the
negative part. So \(\sum h_i-\sum h'_j=0\), \(k=0\), and \(f=\Theta_{1,1}+\Theta_{1,3}-\Theta_{2,4}+c\). On
\([1,5]\): \(\Theta_{1,1}=\theta=0\). For \(\tfrac15\le x\le1\) we have \(\theta(x)=1-x\). So
\(\Theta_{1,3}(\lambda)=3\theta(\lambda/3)\) equals \(3-\lambda\) on \([1,3]\) and \(0\) on \([3,5]\), and
\(\Theta_{2,4}(\lambda)=4\theta(\lambda/2)\) equals \(4-2\lambda\) on \([1,2]\) and \(0\) on \([2,5]\). The sum is
\(\lambda-1\) on \([1,2]\), \(3-\lambda\) on \([2,3]\) and \(0\) on \([3,5]\). This is the function of (b), with
\(c=0\).

**Exercise 5 (size of the theta function).**

- (a) Show that for \(k\ge0\), \(\theta(\lambda)=\sum_{m=1}^{k}(p^{-m}\lambda-1)\) on \([p^{k},p^{k+1}]\) and
  \(\theta(\lambda)=\sum_{m=0}^{k}(1-p^{m}\lambda)\) on \([p^{-k-1},p^{-k}]\).
- (b) Let \(g(\lambda)=\frac{\lambda}{p-1}-\frac{\log\lambda}{\log p}\). Show that
  \(|\theta(\lambda)-g(\lambda)|\le1\) for all \(\lambda>0\).

*Solution.* (a) On \([p^{k},p^{k+1}]\) with \(k\ge0\) we have \(\lambda\ge1\), so the first sum in the definition
of \(\theta\) vanishes, and \(p^{-m}\lambda-1\ge0\) exactly for \(p^{m}\le\lambda\); the term \(m=k+1\) is
non-zero only beyond \(p^{k+1}\). On \([p^{-k-1},p^{-k}]\) we have \(\lambda\le1\), so the second sum vanishes, and
\(1-p^{m}\lambda\ge0\) exactly for \(p^{m}\le1/\lambda\).

(b) \(g(p\lambda)-g(\lambda)=\lambda-1\). By Lemma 6.9 the function \(\theta-g\) takes the same value at
\(\lambda\) and \(p\lambda\). So it suffices to bound it on \([1,p]\), where \(\theta=0\). The function \(g\) is
convex with \(g(1)=g(p)=\tfrac{1}{p-1}\le1\). Its minimum is at \(\lambda^{*}=\tfrac{p-1}{\log p}\), which lies in
\([1,p]\), and

\[
g(\lambda^{*})=\frac{1+\log\log p-\log(p-1)}{\log p}.
\]

The inequality \(g(\lambda^{*})\ge-1\) is equivalent to \(1+\log\log p+\log\tfrac{p}{p-1}\ge0\). This holds
because \(\log\log p\ge\log\log2>-0.37\). So \(-1\le g\le1\) on \([1,p]\).

*Reference:* [Connes–Consani 2017, Lemma 5.10].

**Exercise 6 (comparison with a tropical circle).** Let \(L>0\). On the circle \(\mathbb{R}/L\mathbb{Z}\) take as
rational functions the functions \(f\in\mathrm{PA}_{\mathbb{Z}}(\mathbb{R})\) with \(f(u+L)=f(u)\), as divisors
the finite sums \(D=\sum_in_i[u_i]\) with \(n_i\in\mathbb{Z}\), and \((f)=\sum_uj_f(u)[u]\). Show that
\(D\mapsto\bigl(\sum_in_i,\ \sum_in_iu_i\bmod L\bigr)\) induces an isomorphism from the group of divisors modulo
principal divisors onto \(\mathbb{Z}\times\mathbb{R}/L\mathbb{Z}\). Compare with Theorem 6.6.

*Solution.* The second component is well defined: replacing a representative \(u_i\) by \(u_i+L\) changes the sum
by \(n_iL\). Let \(f\) have breakpoints among \(u_0<u_1<\dots<u_{k-1}<u_0+L=u_k\) and slope \(s_j\in\mathbb{Z}\)
on \([u_{j-1},u_j]\). The jumps are \(n_j=s_{j+1}-s_j\) for \(1\le j\le k-1\) and \(n_0=s_1-s_k\). Their sum is
\(0\). Summation by parts gives

\[
0=f(u_k)-f(u_0)=\sum_{j=1}^{k}s_j(u_j-u_{j-1})=s_k(u_0+L)-s_1u_0-\sum_{j=1}^{k-1}n_ju_j=s_kL-\sum_{j=0}^{k-1}n_ju_j .
\]

So principal divisors are in the kernel. Conversely, given integers \(n_j\) with \(\sum n_j=0\) and
\(\sum n_ju_j=tL\), \(t\in\mathbb{Z}\), put \(s_k=t\) and \(s_j=s_k-(n_j+\dots+n_{k-1})\). Then
\(s_1-s_k=n_0\), and the identity above shows that the function with these slopes is periodic. So the kernel is
the group of principal divisors. The map is surjective, since \([u]\mapsto(1,u)\).

In the variable \(u=\log\lambda\) the orbit \(C_p\) is the circle of length \(L=\log p\). Its sheaf consists of
functions that are piecewise affine in \(\lambda=e^{u}\), not in \(u\). The result is different: on \(C_p\) the
degree is any real number and the classes of degree \(0\) form the finite group \(\mathbb{Z}/(p-1)\mathbb{Z}\); on
the tropical circle the degree is an integer and the classes of degree \(0\) form the circle
\(\mathbb{R}/L\mathbb{Z}\).

**Exercise 7 (the other periodic orbits of period \(\log p\)).** Let \(G\subseteq\mathbb{Q}\) be a subgroup with
\(pG=G\) and \(\ell G\neq G\) for all primes \(\ell\neq p\). On the orbit of \(\mathfrak{p}_G\), identified with
\(\mathbb{R}_{>0}/p^{\mathbb{Z}}\), define rational functions as the \(p\)-periodic functions in
\(\mathrm{PA}_G(\mathbb{R}_{>0})\), divisors as finitely supported maps \(D\) with \(D(\lambda G)\in\lambda G\),
and \((f)(\lambda G)=\lambda j_f(\lambda)\).

- (a) Show that the group of divisors modulo principal divisors is isomorphic to
  \(\mathbb{R}\times G/(p-1)G\).
- (b) Show that \(G/(p-1)G\) is cyclic of order \(p-1\).

*Solution.* (a) Let \(\chi\colon G\to G/(p-1)G\) be the quotient map. Then \(\chi(px)=\chi(x)\), because
\(px-x\in(p-1)G\). So \(\chi_{\lambda G}(h)=\chi(h/\lambda)\) is well defined, and the proofs of Proposition 6.5
and Theorem 6.6 apply word for word with \(H_p\) replaced by \(G\): the slopes \(h_j\) lie in \(G\) exactly when
\(\sigma\in(p-1)G\), and for surjectivity one uses that every class of \(G/(p-1)G\) contains non-zero elements of
both signs.

(b) Put \(n=p-1\). The group \(G\) is countable. So, by Lemma 1.1, it is the union of an increasing sequence of
infinite cyclic groups
\(\mathbb{Z}g_1\subseteq\mathbb{Z}g_2\subseteq\dots\) with \(g_i=m_ig_{i+1}\), \(m_i\in\mathbb{N}^{\times}\). Let
\(\ell\) be a prime dividing \(n\), so \(\ell\neq p\). If \(\ell\) divided infinitely many \(m_i\), every \(g_i\)
would lie in \(\ell G\), and then \(\ell G=G\). So there is \(i_0\) such that \(m_i\) is prime to \(n\) for
\(i\ge i_0\). The group \(G/nG\) is the direct limit of the groups
\(\mathbb{Z}g_i/n\mathbb{Z}g_i\cong\mathbb{Z}/n\mathbb{Z}\), with transition maps given by multiplication by
\(m_i\). For \(i\ge i_0\) these maps are isomorphisms. So \(G/nG\cong\mathbb{Z}/n\mathbb{Z}\).

So every periodic orbit of period \(\log p\) has the divisor class group
\(\mathbb{R}\times\mathbb{Z}/(p-1)\mathbb{Z}\). The Riemann–Roch theorem of Section 6.8 uses in addition that the
slopes of \(p\)-adic absolute value at most \(p^{n}\) form the discrete group \(p^{-n}\mathbb{Z}\). For \(G\) the
corresponding group is \(G_n=\{x\in G:|x|_p\le p^{n}\}\). A subgroup of \(\mathbb{Q}\) is discrete in
\(\mathbb{R}\) only if it is cyclic. If \(G_0=\mathbb{Z}g\), then \(G=\bigcup_np^{-n}G_0=gH_p\). So the groups
\(G_n\) are discrete only on the orbit \(C_p\).

## 9. What this lesson does not prove

- **Sites, sheaves and points.** Section 4.1 uses the description of the points of a site, Theorem 4.1 of
  Topoi, morphisms and points, with sheafification and the limits
  and colimits of sheaves from Sites and sheaves; Section 3.1 uses the extension of sheaves from a basis of
  a topological space [Stacks, Tag [009H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-bases)]. These are proved there.
- **Analysis.** Proposition 7.1 uses the Dirichlet series of \(-\zeta'/\zeta\) and Gauss's formula for
  \(\Gamma'/\Gamma\), and Theorem 7.2 the explicit formula and Weil's compact-support criterion; they are proved in
  the lessons cited there. Not proved in the programme: the interpretation of \(N\) as a count of fixed points of the
  scaling action by a trace formula [Connes–Consani 2016b, Section 4.2].
- **The problems of Section 7.3.** They are open in the works cited.

## References

- [Connes–Consani 2017] A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191. Free at https://alainconnes.org/wp-content/uploads/scalingsite.pdf
- [Connes–Consani 2016b] A. Connes, C. Consani, *Geometry of the arithmetic site*, arXiv:1502.05580. Free at https://alainconnes.org/wp-content/uploads/arithmeticsite.pdf
- [Connes–Consani 2018] A. Connes, C. Consani, *The Riemann–Roch strategy, complex lift of the scaling site*,
  [arXiv:1805.10501](https://arxiv.org/pdf/1805.10501).
- [Connes 2015] A. Connes, *An essay on the Riemann hypothesis*, [arXiv:1509.05576](https://arxiv.org/pdf/1509.05576).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 009H and 00Y3 carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Bombieri–Lagarias 1999] E. Bombieri, J. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*,
  J. Number Theory 77 (1999), 274–287, [doi:10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392) (free in the publisher's open archive).

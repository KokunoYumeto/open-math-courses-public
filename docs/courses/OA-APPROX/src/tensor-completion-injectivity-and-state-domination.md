# Tensor completion, injectivity and state domination

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

A completed tensor has two descriptions here: a Cauchy sequence for the projective norm \(\pi\), and a Cauchy sequence for the symmetric norm \(\sigma\). Because \(\sigma\le\pi\), the algebraic identity gives a map from the first completion to the second. The [random lift construction](symmetric-tensor-norms-and-rademacher-truncation.md#5-surjectivity-at-the-completion-level) supplies a projective preimage of every self-adjoint target vector, with cost at most \((81/16)\|v\|_\sigma+\varepsilon\). Different choices of \(\varepsilon\) could still give different preimages. Their difference lies in the kernel of the completion map.

We prove that this kernel is zero. A normalized functional detects a kernel vector only through its real part; the bilinear exponential test makes that real part \(\sigma\)-continuous. A Gaussian then turns the resulting two numerical-reality conditions into a norm bound tending to zero. Once the lift is unique, its approximate costs become an exact norm comparison. That comparison makes every bounded real bilinear form eligible for the final compact affine argument, which chooses one pair of states for all inputs.

Write
\[
q(x)=\frac{x^*x+xx^*}{2}.
\]
The two algebraic tensor norms are
\[
\|u\|_\pi=\inf_{u=\sum_jx_j\otimes y_j}\sum_j\|x_j\|\|y_j\|,
\qquad
\|u\|_\sigma=\inf_{u=\sum_jx_j\otimes y_j}
\Big\|\sum_jq(x_j)\Big\|^{1/2}\Big\|\sum_jq(y_j)\Big\|^{1/2}.
\]
Both infima use finite decompositions. The real projective norm uses self-adjoint factors and real scalars. A bounded form acts on these completions when its value on an algebraic tensor is bounded by the corresponding norm; its dual norm is the least such bound.

[Section 8.1](#8-1-the-precise-norming-functional-input) proves real and complex functional extension. [Section 8.2](#8-2-completion-and-the-projective-algebra) constructs the completion maps and the projective algebra. [Section 8.3](#8-3-positive-functionals-and-norming-states) constructs the states, using the scalar spectrum, continuous calculus and order proved in ITP F01–F13. The scalar foundations and continuous norm integrals are in [Elementary calculus for infinite products](elementary-calculus-for-infinite-products.md). [Section 9](#9-weak-star-compactness-for-arbitrary-normed-spaces) proves compactness and convergent subnets for arbitrary dual balls. None of these constructions assumes separability. A unital algebra in the state assertions has a nonzero identity of norm one; the injectivity assertion also includes zero and nonunital algebras.

<a id="3-injectivity-of-the-canonical-map"></a>

## Can a tensor disappear in the completion?

**Theorem 3.1.** For any C*-algebras \(A,B\), the canonical map
\[
I:A\widehat\otimes_\pi B\longrightarrow A\widehat\otimes_\sigma B
\tag{7}
\]
is injective.

The algebraic identity is contractive and therefore extends to \(I\) on Cauchy representatives. Injectivity asks whether \(\sigma\)-convergence to zero can hide a nonzero projective limit.

**Proof.** If either factor is zero, both tensor spaces are zero. First take nonzero unital \(A,B\), and put \(C=A\widehat\otimes_\pi B\). Section 8.2 proves its completeness, submultiplicative norm, isometric involution and norm-one identity \(1\otimes1\). Multiplication and involution also extend to the \(\sigma\)-completion by the preceding lesson's product estimate. The algebraic identities consequently pass to the completions: \(I(uv)=I(u)I(v)\) and \(I(u^*)=I(u)^*\). Thus \(K=\ker I\) is closed, is invariant under involution, and is an ideal.

Norm-preserving extension at the identity supplies \(\mathcal S_C\). For \(F\in\mathcal S_C\), put \(G=(F+F^*)/2\), where \(F^*(u)=\overline{F(u^*)}\). Adjoint isometry gives \(\|G\|\le1\), while \(G(1)=1\) gives the reverse inequality. The bilinear form \(V_G(x,y)=G(x\otimes y)\) therefore has norm one and value one at \((1,1)\): its norm is at most \(\|G\|\), and its value on that pair is one. It is self-adjoint. Lemma 1.1 and (3) below bound its value on every tensor decomposition by its \(\sigma\)-cost. It extends continuously to the \(\sigma\)-completion. The extension composed with \(I\) agrees with \(G\) on the algebraic tensors and hence on \(C\). Consequently \(G\) vanishes on \(K\). If \(v=v^*\in K\), this says \(\operatorname{Re}F(v)=0\) for every normalized \(F\). Consequently \(h=iv\) is numerical-real. Since \(v^2\in K\) is self-adjoint, \(ih^2=-iv^2\) is also numerical-real. Lemma 2.1 gives \(v=0\). For general \(u\in K\), apply this to \(u+u^*\) and \(i(u-u^*)\); both are self-adjoint elements of \(K\). Thus \(u=0\).

For nonunital algebras, use forced C*-unitizations \(\widetilde A,\widetilde B\). ITP F02 constructs these unitizations with isometric copies of the original algebras and a contractive scalar quotient. Thus
\(\|P_A(a+\lambda1)\|=\|a\|\le\|a+\lambda1\|+|\lambda|\le2\|a+\lambda1\|\);
the same holds for \(P_B\). On each finite decomposition, \(P_A\otimes P_B\) has projective bound at most \(4\), so Section 8.2 extends it to a bounded left inverse of the projective inclusion. That inclusion is therefore injective. The algebraic inclusion is \(\sigma\)-contractive, since all square-sum norms are preserved. The commuting square of the two canonical maps shows that an element in the kernel of (7) maps to the kernel for the unitizations. The unital result and projective injectivity of the inclusion make it zero. \(\square\)

<a id="1-normalized-bilinear-forms"></a>

## Normalized functionals control the kernel

Suppose initially that \(A,B\) are unital and \(V:A\times B\to\mathbb C\) is bilinear, with \(\|V\|=V(1,1)=1\). Each marginal has norm at most one and value one at the identity, so its norm is exactly one. Section 8.3's positivity criterion therefore makes \(\varphi(x)=V(x,1)\) and \(\psi(y)=V(1,y)\) states. For self-adjoint \(a\), the exponential series and adjoint give \((e^{ita})^*=e^{-ita}\) and \(e^{-ita}e^{ita}=1\). The C*-identity yields \(\|e^{ita}\|=1\), which permits the following bilinear test.

**Lemma 1.1.** For self-adjoint \(a,b\),
\[
|\operatorname{Re}V(a,b)|\le\varphi(a^2)^{1/2}\psi(b^2)^{1/2}.
\tag{1}
\]

**Proof.** Expand the two exponential series through order two and apply \(V\). If \(M=\|a\|+\|b\|\) and \(|t|\le1\), the terms of total degree at least three have absolute sum at most \(e^M M^3|t|^3/6\); this follows from \(n!\ge6(n-3)!\). The marginal values on \(a,b\) are real, so the first-order term has zero real part. Thus
\[
\operatorname{Re}V(e^{ita},e^{itb})
=1-t^2\big[\tfrac12\varphi(a^2)+\tfrac12\psi(b^2)
+\operatorname{Re}V(a,b)\big]+O(|t|^3).
\tag{2}
\]
The left side is at most \(1\), so the bracket is nonnegative. Replace \(a\) by \(-a\) to get \(|\operatorname{Re}V(a,b)|\le[\varphi(a^2)+\psi(b^2)]/2\). Replace \(a,b\) by \(t a,t^{-1}b\) and minimize over \(t>0\). If either quadratic value is zero, take the corresponding limit; otherwise the minimizing bound is their geometric mean. \(\square\)

Write \(V^*(x,y)=\overline{V(x^*,y^*)}\). If also \(V=V^*\), its values on self-adjoint pairs are real. For arbitrary \(x=a+ic,y=b+id\), rotate \(x\) by a scalar phase so that \(V(x,y)\) is real. Then
\[
|V(x,y)|=|V(a,b)-V(c,d)|
\le\varphi(a^2+c^2)^{1/2}\psi(b^2+d^2)^{1/2}
=\varphi(q(x))^{1/2}\psi(q(y))^{1/2}.
\tag{3}
\]
The phase does not change \(q(x)\). Summing (3) and applying scalar Cauchy–Schwarz proves that this normalized self-adjoint functional on \(A\widehat\otimes_\pi B\) is \(\sigma\)-continuous, with dual norm at most \(1\).

<a id="2-a-banach-algebra-kernel-test"></a>

<a id="8-an-elementary-gaussian-proof"></a>

## A Gaussian test for an invisible element

For a unital complex Banach algebra \(C\), assume \(\|1\|=1\). Its normalized functionals are
\[
\mathcal S_C=\{F\in C^*: \|F\|=F(1)=1\}.
\]
They need not be positive on any involution. Call \(h\) numerical-real if every \(F\in\mathcal S_C\) takes a real value at \(h\).

**Lemma 2.1.** If \(h\) and \(ih^2\) are numerical-real, then \(h=0\).

**Proof.** We build the norm derivative, the isometric exponential group and the integral estimate in turn. The norm derivative only needs restrictions to \(\operatorname{span}_{\mathbb C}\{1,a\}\). Section 8 proves the functional extension used in that step.

<a id="8-2-directional-norm-derivative-using-only-two-dimensional-compactness"></a>

### Directional norm derivative using only two-dimensional compactness

Let \(C\) be a unital complex Banach algebra with \(\|1\|=1\), and define

\[
\mathcal S_C=\{F\in C^*: \|F\|=F(1)=1\}.
\]

The norming-functional assertion at \(1\) makes this set nonempty. For \(a\in C\), set

\[
D_s=\frac{\|1+s a\|-1}{s},\qquad s>0.
\]

The map \(s\mapsto\|1+s a\|\) is convex, so \(D_s\le D_t\) for \(0<s<t\). Also \(|D_s|\le\|a\|\). Thus \(D=\lim_{s\downarrow0}D_s\) exists and is finite. Evaluating a member of \(\mathcal S_C\) gives

\[
D_s\ge\operatorname{Re}F(a),
\quad\hbox{so}\quad
D\ge\sup_{F\in\mathcal S_C}\operatorname{Re}F(a).
\tag{B1}
\]

Choose \(s_j\downarrow0\), small enough that \(1+s_j a\ne0\), and a norm-one \(F_j\in C^*\) with \(F_j(1+s_j a)=\|1+s_j a\|\). This is the norming consequence proved in Section 8.1. Restrict these functionals to \(E=\operatorname{span}_{\mathbb C}\{1,a\}\). Their values at a fixed basis of \(E\) are bounded, because \(|F_j(x)|\le\|x\|\). A subsequence converges coordinatewise: repeatedly bisect a bounded interval containing each of their finitely many real and imaginary coordinates, retain a subinterval containing infinitely many indices, and then take a diagonal increasing subsequence. The nested lengths tend to zero, so real completeness gives convergence in every coordinate. This is the only compactness argument needed.

The limiting functional \(f:E\to\mathbb C\) is linear and satisfies \(|f(x)|\le\|x\|\) for every fixed \(x\in E\). Moreover,

\[
F_j(1)=\|1+s_j a\|-s_j F_j(a)\longrightarrow1,
\]

so \(f(1)=1\). Apply Section 8.1 to extend \(f\) to \(F\in C^*\) with norm at most one; its value at \(1\) forces its norm to be exactly one. Hence \(F\in\mathcal S_C\). Finally,

\[
D_{s_j}
=\frac{\operatorname{Re}F_j(1)-1}{s_j}
 +\operatorname{Re}F_j(a)
\le\operatorname{Re}F_j(a).
\]

Passing along the coordinate-convergent subsequence gives \(D\le\operatorname{Re}F(a)\). Together with (B1), this proves

\[
\lim_{s\downarrow0}\frac{\|1+s a\|-1}{s}
=\sup_{F\in\mathcal S_C}\operatorname{Re}F(a).
\tag{4}
\]

This proof applies even when \(C\) is nonseparable. It uses finite-dimensional scalar subsequence compactness and Hahn-Banach, without the weak-* compactness of the full dual ball.

<a id="8-3-numerical-reality-gives-an-isometric-exponential-group"></a>

### Numerical reality gives an isometric exponential group

Call \(k\in C\) numerical-real if \(F(k)\in\mathbb R\) for all \(F\in\mathcal S_C\). Formula (4), applied to \(a=\pm ik\), gives

\[
\|1+s(\pm ik)\|=1+o(s),\qquad s\downarrow0.
\tag{C1}
\]

The exponential \(e^a=\sum_{m\ge0}a^m/m!\) converges in norm, since \(\|a^m\|\le\|a\|^m\) and the scalar exponential series converges. Also

\[
(1+a/n)^n\longrightarrow e^a.
\tag{C2}
\]

To see this directly, the coefficient of \(a^m\), for \(m\le n\), is \(\binom nm/n^m\), which tends to \(1/m!\) and is at most \(1/m!\). The norm of the tail above any fixed \(m_0\), uniformly in \(n\), is bounded by \(\sum_{m>m_0}\|a\|^m/m!\), which tends to zero. The finite initial segment converges coefficientwise.

Fix \(t\in\mathbb R\). With \(a=itk\), (C1) and submultiplicativity give

\[
\|e^{itk}\|
\le\limsup_n\|1+itk/n\|^n=1.
\]

For the last bound, fix \(\varepsilon>0\). Formula (C1) gives
\(\|1+itk/n\|\le1+\varepsilon|t|/n\) for all sufficiently large \(n\), using the appropriate sign when \(t\ne0\). The scalar exponential series gives \(1+r\le e^r\) for \(r\ge0\), and hence
\[
\|1+itk/n\|^n\le(1+\varepsilon|t|/n)^n\le e^{\varepsilon|t|}.
\]
Take the limit in (C2) and then let \(\varepsilon\downarrow0\). For \(t=0\) the norm is already one. For any \(F\in\mathcal S_C\), reality of \(F(k)\) gives
\(\|1+itk/n\|\ge|1+itF(k)/n|\ge1\).
Thus the Euler norms are also bounded below by one, proving their limit is exactly one. Absolute convergence of the exponential series permits their Cauchy product; the binomial identity then gives \(e^{itk}e^{-itk}=1\). Both factors are contractions and \(\|1\|=1\), so both have norm one. For every \(x\in C\),

\[
\|x\|=\|e^{-itk}(e^{itk}x)\|\le\|e^{itk}x\|\le\|x\|,
\]

and therefore left multiplication by \(e^{itk}\) is an isometry. The analogous right assertion follows by the same calculation.

<a id="8-4-the-scalar-gaussian-facts-and-the-vector-integral"></a>

### The scalar Gaussian facts and the vector integral

The scalar improper integral \(I=\int_{\mathbb R}e^{-u^2}\,du\) exists: outside \([-1,1]\), \(e^{-u^2}\le e^{-|u|}\). Its normalization can be checked using only compact Riemann integrals. If \(I_R=\int_{-R}^R e^{-u^2}\,du\), the double Riemann integral over the square equals \(I_R^2\), by rectangular product sums. That square contains the disk of radius \(R\) and lies inside the disk of radius \(\sqrt2 R\). For a continuous radial function on a disk, upper and lower sums on concentric annuli, whose areas are \(\pi(r_j^2-r_{j-1}^2)\), give the radial integral \(\int_0^R2\pi r f(r)\,dr\). Uniform continuity makes the difference of the two sums tend to zero. Applying this to \(f(r)=e^{-r^2}\) gives

\[
\pi(1-e^{-R^2})\le I_R^2\le\pi(1-e^{-2R^2}).
\]

Hence \(I^2=\pi\), and positivity gives \(I=\sqrt\pi\). Scalar substitution now shows that for \(t>0\),

\[
g_t(s)=(4\pi t)^{-1/2}e^{-s^2/(4t)}
\quad\hbox{satisfies}\quad
\int_{\mathbb R}g_t(s)\,ds=1.
\tag{D1}
\]

[Section 8.4](#8-4-disk-area-and-the-quarter-phase) constructs the disk and annulus areas from rectangular sums, and identifies the same \(\pi\) in the scalar quarter-phase example of Exercise 6. For the vector integral, let \(v:[a,b]\to E\) be norm continuous in a real or complex Banach space. Scalar compactness makes it uniformly continuous. If
\(\omega(\delta)=\sup_{|s-r|\le\delta}\|v(s)-v(r)\|\), comparison of two tagged sums through their common refinement gives
\[
\|S_P(v)-S_Q(v)\|\le(b-a)[\omega(\operatorname{mesh}P)+\omega(\operatorname{mesh}Q)].
\]
Dyadic sums are Cauchy and have a limit by completeness. The same estimate proves that every choice of tags converges to that limit as its mesh tends to zero. The scalar norm function is continuous, and the triangle inequality applied to each tagged sum yields

\[
\left\|\int_a^b v(s)\,ds\right\|\le\int_a^b\|v(s)\|\,ds.
\tag{D2}
\]

If a continuous scalar integrable envelope \(b(s)\ge\|v(s)\|\) has vanishing tails on \(\mathbb R\), (D2) makes the integrals over \([-R,R]\) Cauchy as \(R\to\infty\). Their limit is the improper norm integral, and (D2) holds on the line. Bounded linear maps, including multiplication by a fixed algebra element, commute with these integrals by passage from Riemann sums. The continuous fundamental theorem proved in [R04](elementary-calculus-for-infinite-products.md#r04) applies to any real or complex Banach space: the integral primitive has derivative \(v\), and subtracting it from a function with continuous derivative leaves a constant function. With the bilinear product estimate in [R07](elementary-calculus-for-infinite-products.md#r07), this gives
\[
\int_a^b u'(s)v(s)\,ds=[u(s)v(s)]_a^b-\int_a^b u(s)v'(s)\,ds
\]
for scalar \(u\) and Banach-valued \(v\) with continuous derivatives. Thus integration by parts is a norm identity. Only continuous functions with the specified integrable envelopes enter the full-line argument.

<a id="8-5-the-heat-identity-with-all-exchanges-justified"></a>

### The heat identity, with all exchanges justified

Let \(h\in C\). The series for \(e^{ish}\) converges uniformly on every compact \(s\)-interval, so it may be integrated there termwise. For the full-line integral, its absolute series has scalar envelope

\[
g_t(s)\sum_{m\ge0}\frac{|s|^m\|h\|^m}{m!}
=g_t(s)e^{|s|\|h\|}.
\]

This is integrable, since with \(A=\|h\|\),

\[
-s^2/(4t)+A|s|\le -s^2/(8t)+2t A^2.
\]

Fix a large compact interval; uniform convergence gives termwise integration there. Outside the interval, the same integrable envelope controls every partial sum and the full sum. Its tail tends to zero. These two observations justify interchange of the series and the improper norm integral, without appealing to an unproved general Bochner dominated-convergence theorem.

Odd Gaussian moments vanish by symmetry. Integration by parts for the even moments uses \(g_t'=-s g_t/(2t)\); polynomial times \(g_t\) tends to zero at both endpoints. Indeed \(e^u\ge u^N/N!\) for \(u\ge0\); choosing \(2N\) larger than a given polynomial degree shows that \(|s|^m e^{-s^2/(8t)}\to0\). Keeping the other factor \(e^{-s^2/(8t)}\) bounds each polynomial Gaussian tail by an integrable Gaussian, and eventually by a constant times \(e^{-|s|}\). For \(m\ge1\),

\[
\int s^{2m}g_t(s)\,ds
=2t(2m-1)\int s^{2m-2}g_t(s)\,ds
=\frac{(2m)!}{m!}t^m.
\tag{E1}
\]

The last equality follows inductively from (D1). Consequently,

\[
\int_{\mathbb R}g_t(s)e^{ish}\,ds
=\sum_{m\ge0}\frac{(-1)^m h^{2m}}{(2m)!}
   \frac{(2m)!}{m!}t^m
=e^{-t h^2}.
\tag{5}
\]

<a id="8-6-derivative-estimate-and-the-kernel-conclusion"></a>

### Derivative estimate and the kernel conclusion

Now assume \(h\) and \(ih^2\) are numerical-real. The isometric exponential argument gives \(\|e^{ish}\|=1\). Uniform differentiation of the exponential series on compact intervals gives \((e^{ish})'=ih e^{ish}\). Integration by parts on \([-R,R]\), and then passage to the limit, gives

\[
\int_{\mathbb R}g_t'(s)e^{ish}\,ds
=-ih\int_{\mathbb R}g_t(s)e^{ish}\,ds.
\]

The endpoint terms vanish because \(g_t(\pm R)\to0\) and \(\|e^{\pm iRh}\|=1\); both integrals have scalar integrable envelopes. Thus (5) yields

\[
h e^{-t h^2}=i\int_{\mathbb R}g_t'(s)e^{ish}\,ds,
\qquad
\|h e^{-t h^2}\|\le\int_{\mathbb R}|g_t'(s)|\,ds.
\tag{6}
\]

The Gaussian is even and decreasing on the positive half-line, so scalar integration gives

\[
\int_{\mathbb R}|g_t'|=2g_t(0)=\frac1{\sqrt{\pi t}}.
\tag{F2}
\]

Numerical reality of \(ih^2\) and the isometric exponential argument make both \(e^{t h^2}\) and \(e^{-t h^2}\) contractions: these are \(e^{ir(ih^2)}\) for the two real values \(r=-t,t\). Hence right multiplication by \(e^{-t h^2}\) is an isometry. Equations (6) and (F2) give

\[
\|h\|=\|h e^{-t h^2}\|\le\frac1{\sqrt{\pi t}}
\qquad(t>0).
\]

Letting \(t\to\infty\) gives \(h=0\), as required. The first hypothesis bounds the Gaussian integrand; the second allows the inverse damping operator without increasing the norm. These operations give \(\|h\|\le1/\sqrt{\pi t}\) for every \(t>0\), and therefore prove the lemma. \(\square\)

<a id="4-the-real-norm-comparison"></a>

## From small lifts to the real tensor bound

The kernel theorem makes a small preimage unique. Before transferring its cost, we identify the real completion inside the complex one. The real projective space embeds in the complex projective space. To see this without assuming a tensor-inclusion theorem, expand any complex decomposition of a self-adjoint tensor as in (6) of the [preceding lesson](symmetric-tensor-norms-and-rademacher-truncation.md#proposition-1-1). It costs at most twice the original projective cost, since
\(\|\operatorname{Re}x\|^2+\|\operatorname{Im}x\|^2\le2\|x\|^2\). Thus
\[
\|u\|_\pi\le\|u\|_{\pi_{\mathbb R}}\le2\|u\|_\pi
\tag{8}
\]
on the algebraic real tensor space, and the inclusion of its completion is injective. Its image is the self-adjoint part of the complex completion: symmetrized algebraic approximants are Cauchy by (8).

**Theorem 4.1.** On the completed real self-adjoint tensor space,
\[
\|u\|_\sigma\le\|u\|_{\pi_{\mathbb R}}
\le\frac{81}{16}\|u\|_\sigma.
\tag{9}
\]
Every bounded real bilinear form \(W\) on \(A_{\rm sa}\times B_{\rm sa}\) therefore has \(\sigma\)-dual norm at most \((81/16)\|W\|\).

**Proof.** Let \(v\) be in the completed real \(\sigma\)-space. For every \(\varepsilon>0\), the preceding random-lift lesson supplies a real projective vector \(u_\varepsilon\) with

\[
I(u_\varepsilon)=v,\qquad
\|u_\varepsilon\|_{\pi_{\mathbb R}}\le(81/16)\|v\|_\sigma+\varepsilon.
\]

Theorem 3.1 above and (8) show that the real canonical map is injective. All these \(u_\varepsilon\) are therefore one vector \(u\). Taking the infimum of its bounds gives \(\|u\|_{\pi_{\mathbb R}}\le(81/16)\|v\|_\sigma\). The reverse inequality follows from the contractive canonical map. This identifies the two completed real spaces and proves (9). Evaluation of a bounded real bilinear form on projective decompositions gives \(|W(u)|\le\|W\|\|u\|_{\pi_{\mathbb R}}\); (9) gives the dual norm bound and extension to the completion. \(\square\)

<a id="5-fixed-states-from-compact-affine-inequalities"></a>

## One pair of states for all tests

A finite list of affine inequalities can be encoded by a subset of Euclidean space. Let \(Q\) be a nonempty compact convex set and let \(F_1,\ldots,F_m\) be continuous real affine functions. Their joint image \(K\subset\mathbb R^m\) is compact and convex. Write \(y_+\) for the coordinatewise positive part and \(y_-=(-y)_+\). If \(K\) misses the positive orthant, the continuous function \(\|y_-\|^2\) has a strictly positive minimum at \(y_0\in K\). Put \(z_0=(y_0)_+\) and \(w=z_0-y_0=(y_0)_-\). For every \(y\in K\), \(z_0\) is a possible orthant point, so

\[
\|y_0-z_0\|^2\le\|y_0+t(y-y_0)-z_0\|^2,\qquad 0\le t\le1.
\]

The right derivative at zero gives \((y_0-z_0)\cdot(y-y_0)\ge0\). Hence

\[
w\ge0,\quad w\ne0,\qquad
w\cdot y\le w\cdot y_0=-\|w\|^2<0\quad(y\in K).
\tag{S1}
\]

The nonnegative coefficients \(w_j\) therefore give a strictly negative maximum of \(\sum_jw_jF_j\). If every finite nonnegative combination of functions in a family \(\mathcal F\) has nonnegative maximum, this contradiction proves that each finite list of its closed nonnegative sets has a common point. Compactness of \(Q\) gives one point satisfying the entire family. The finite-dimensional minimum uses scalar compactness; the last step uses arbitrary compactness, without a countability or metrizability assumption.

![An exact two-dimensional instance of the orthant separation calculation.](../assets/grothendieck-random-lift-and-sharp-constant.svg)

Here \(K=\{(-2+t,1-2t):0\le t\le1\}\). Its nearest point to the positive orthant is \(y_0=(-6/5,-3/5)\), with \(z_0=(0,0)\) and \(w=(6/5,3/5)\). The line \(w\cdot y=-9/5\) contains the entire segment, while \(w\cdot z\ge0\) on the orthant. These are the signs and strict gap in (S1). The picture illustrates one finite test family; it does not represent an infinite-dimensional state space.

Section 8.3 constructs states norming every positive element, including the zero element, on a nonzero unital algebra. It also proves that the state space is a closed subset of the weak-* compact dual ball from Section 9. The product \(S(A)\times S(B)\) is compact by the same disk-product construction with the coordinates of both algebras together. The two states norming a finite test's two square sums may depend on that test. The orthant argument will replace those separate choices by one pair that passes every test.

**Lemma 5.1.** For a real \(\sigma\)-continuous bilinear form \(W\) on self-adjoint pairs in unital \(A,B\), there are states \(\varphi,\psi\) with
\[
|W(a,b)|\le c\varphi(a^2)^{1/2}\psi(b^2)^{1/2},
\qquad c=\|W\|_{\sigma^*}.
\tag{10}
\]

**Proof.** If \(c=0\), the form is zero and any pair of states works. Suppose \(c>0\). On \(Q=S(A)\times S(B)\), test every self-adjoint pair with

\[
F_{a,b}(\varphi,\psi)=\tfrac c2[\varphi(a^2)+\psi(b^2)]-W(a,b).
\tag{11}
\]

For a finite sum \(\sum_j\lambda_jF_{a_j,b_j}\), \(\lambda_j\ge0\), replace \(a_j,b_j\) by \(\sqrt{\lambda_j}a_j,\sqrt{\lambda_j}b_j\). Set \(S_A=\|\sum_j a_j^2\|\), \(S_B=\|\sum_j b_j^2\|\), and choose states separately norming these two positive sums. The definition of the \(\sigma\)-dual norm gives \(\sum_jW(a_j,b_j)\le c\sqrt{S_A S_B}\). The combined test at those states has value at least \(c(S_A+S_B)/2-c\sqrt{S_A S_B}\ge0\).

The finite-orthant minimum and compactness argument therefore give one pair \((\varphi,\psi)\) passing every test. Testing \((a,b)\) and \((-a,b)\) gives

\[
|W(a,b)|\le\tfrac c2[\varphi(a^2)+\psi(b^2)].
\]

Apply this to \((ta,t^{-1}b)\). If both quadratic values are positive, take \(t^4=\psi(b^2)/\varphi(a^2)\). If either value is zero, send \(t\) to the corresponding endpoint. This proves (10), with the same states for all pairs. \(\square\)

<a id="6-an-initial-complex-domination-bound"></a>

## The complex form and its two common states

**Theorem 6.1.** For unital C*-algebras and any bounded complex bilinear form \(V\), there are states \(\varphi,\psi\) such that
\[
|V(x,y)|\le\frac{81}{16}\|V\|
\varphi(x^*x+xx^*)^{1/2}\psi(y^*y+yy^*)^{1/2}.
\tag{12}
\]

**Proof.** Put \(V_1=(V+V^*)/2\), \(V_2=(V-V^*)/(2i)\). Each is self-adjoint and has norm at most \(\|V\|\). Its real restriction is \(\sigma\)-continuous by Theorem 4.1. Lemma 5.1 gives states \(\varphi_i,\psi_i\) with constant \(K\|V\|\), where \(K=81/16\). Expanding \(x=a+ic,y=b+id\) and taking real parts gives the same two-term estimate as (3). Rotating \(x\) then gives
\[
|V_i(x,y)|\le K\|V\|\varphi_i(q(x))^{1/2}\psi_i(q(y))^{1/2}.
\]
Sum the bounds for \(V_1,V_2\), apply Cauchy–Schwarz to this two-term sum, and set \(\varphi=(\varphi_1+\varphi_2)/2\), \(\psi=(\psi_1+\psi_2)/2\). The result is \(2K\|V\|\sqrt{\varphi(q(x))\psi(q(y))}\), which equals the right side of (12). \(\square\)

This finite universal constant is the input to the [sharp inequality](sharp-noncommutative-bilinear-inequality.md). Its existence, rather than its preliminary numerical size, is what the improvement argument needs.

## 7. Exercises with complete solutions

The first three checks build the functional that tests a kernel vector. Exercises 4–6 examine the compactness and Gaussian estimates that make the test decisive. Exercises 7–8 transfer a completed lift's cost. Exercises 9–10 turn those norm estimates into common-state bounds.

**Exercise 1.** Let \(V\) be the normalized bilinear form used in Lemma 1.1, with marginal states \(\varphi,\psi\), and let \(a,b\) be self-adjoint. Test \(V\) on \((e^{ita},e^{itb})\). Determine the sign of the second-order bracket in (2), and determine what changes when the first input is replaced by its negative.

*Solution.* Put \(M=\|a\|+\|b\|\). Multiplying the two norm-convergent exponential series through \(V\) gives
\[
V(e^{ita},e^{itb})=
1+it[\varphi(a)+\psi(b)]
-t^2\left[\frac{\varphi(a^2)+\psi(b^2)}2+V(a,b)\right]+R(t).
\]
For \(|t|\le1\), group the absolute terms by their total degree \(n\). The binomial identity bounds them by \(|t|^nM^n/n!\). Since \(n!\ge6(n-3)!\) for \(n\ge3\),
\[
|R(t)|\le \frac{M^3e^M}{6}|t|^3.
\]
The first-order coefficient is real before multiplication by \(i\), because the marginals are states. For
\(B=[\varphi(a^2)+\psi(b^2)]/2+\operatorname{Re}V(a,b)\)
we therefore have \(\operatorname{Re}V(e^{ita},e^{itb})=1-t^2B+\operatorname{Re}R(t)\). Both exponentials have norm one, so their bilinear value has real part at most one. Subtract one and divide by \(t^2>0\):
\[
-B+\frac{\operatorname{Re}R(t)}{t^2}\le0.
\]
The last quotient tends to zero, proving \(B\ge0\). Thus
\(\operatorname{Re}V(a,b)\ge-[\varphi(a^2)+\psi(b^2)]/2\).
For \((-a,b)\), the square terms remain the same and the cross term changes sign. The resulting bracket inequality gives the opposite bound, and hence the absolute-value estimate that reciprocal scaling will sharpen.

**Exercise 2.** The bilinear test gives an additive quadratic bound, while the desired state bound is multiplicative. For \(\alpha,\beta\ge0\), compute the infimum over \(t>0\) of
\[
H(t)=\frac{t^2\alpha+t^{-2}\beta}{2}.
\]
Specify its minimizer when both values are positive and handle every case \(\alpha\beta=0\), including whether the infimum is attained.

*Solution.* The identity
\[
2[H(t)-\sqrt{\alpha\beta}]
=(t\sqrt{\alpha}-t^{-1}\sqrt{\beta})^2
\]
proves \(H(t)\ge\sqrt{\alpha\beta}\) for all \(t>0\). When \(\alpha,\beta>0\), equality occurs precisely at \(t^4=\beta/\alpha\), so the positive minimizer is \(t=(\beta/\alpha)^{1/4}\) and the minimum is \(\sqrt{\alpha\beta}\).

When \(\alpha=0<\beta\), \(H(t)=\beta/(2t^2)>0\) at each finite positive \(t\), but it tends to zero as \(t\to\infty\). When \(\beta=0<\alpha\), \(H(t)=\alpha t^2/2>0\), tending to zero as \(t\downarrow0\). Both infima are zero and neither is attained. If \(\alpha=\beta=0\), every value of \(H\) is zero. Applying these cases to \(\alpha=\varphi(a^2)\), \(\beta=\psi(b^2)\) proves that a zero quadratic value forces the tested bilinear value to vanish; no division by a zero value is needed.

**Exercise 3.** A kernel vector is tested by the self-adjoint part of a normalized functional. Let \(C\) be an involutive complex Banach algebra whose involution is isometric and whose identity has norm one. If \(F\in\mathcal S_C\), verify that
\[
G=(F+F^*)/2,\qquad F^*(x)=\overline{F(x^*)},
\]
is normalized and self-adjoint.

*Solution.* The adjoint is complex linear, since
\[
F^*(\lambda x+\mu y)
=\overline{\bar\lambda F(x^*)+\bar\mu F(y^*)}
=\lambda F^*(x)+\mu F^*(y).
\]
The involution carries the unit ball onto itself. Substituting \(z=x^*\) in the functional norm supremum therefore gives
\(\|F^*\|=\sup_{\|z\|\le1}|F(z)|=\|F\|=1\).
The triangle inequality gives \(\|G\|\le1\). Since \(1^*=1\) and \(F(1)=1\),
\[
G(1)=\tfrac12[1+\overline1]=1.
\]
Evaluation at the norm-one identity gives \(1=|G(1)|\le\|G\|\), proving equality. Finally \((F^*)^*=F\), and conjugate linearity of the functional adjoint on scalar coefficients gives \(G^*=G\). This is normalization in the Banach-algebra sense; positivity requires the additional C*-order criterion in Section 8.3.

**Exercise 4.** The directional formula (4) must hold for an arbitrary, possibly nonseparable, unital Banach algebra \(C\). For \(a\in C\), put \(q(s)=(\|1+sa\|-1)/s\). Explain how compactness of the entire dual unit ball supplies the limiting normalized functional, and how its subnet preserves the scalar limsup. Also identify why a convergent functional subsequence cannot be assumed.

*Solution.* Section 9 uses one disk of radius \(\|x\|\) for every \(x\in C\). In their product, impose all equations
\(f(x+\lambda y)=f(x)+\lambda f(y)\).
Each equation is closed in the coordinate topology. Their intersection consists exactly of linear functionals of norm at most one, so it is the weak-* dual ball. The ultrafilter proof of product compactness works for the full index set \(C\); it imposes no countability condition.

The triangle inequality gives \(|q(s)|\le\|a\|\), so its scalar limsup \(L\) is finite. Choose a strictly decreasing sequence \(s_n\downarrow0\) with \(q(s_n)\to L\), by taking \(s_n\) below the previous half-step and below a threshold on which \(q<L+1/n\), while ensuring \(q(s_n)>L-1/n\). For all sufficiently large \(n\), \(1+s_na\ne0\). Section 8.1 supplies \(\|F_n\|=1\) with
\(F_n(1+s_na)=\|1+s_na\|\).

Compactness gives a cluster point \(F\) in the full dual ball. More explicitly, intersect the closures of all tails of \((F_n)\). They have the finite intersection property, so that intersection is nonempty. Direct the triples \((n,U,m)\) with \(m\ge n\) and \(F_m\in U\), where \(U\) is a neighborhood of \(F\), by increasing both indices and decreasing the neighborhood. The cluster property gives a common upper triple for any two. The selected index \(m\) is order preserving and eventually exceeds every integer. The selected functionals therefore form a subnet converging weak-* to \(F\), as constructed for general nets in Section 9.5. Along it \(s_m\to0\) and \(q(s_m)\to L\).

The norming equality gives
\[
|F_n(1)-1|
\le|\|1+s_na\|-1|+s_n|F_n(a)|
\le2s_n\|a\|.
\]
Thus \(F(1)=1\). Its dual-ball bound and \(\|1\|=1\) then give \(\|F\|=1\). Taking real parts of the same norming equality, and using \(\operatorname{Re}F_n(1)\le1\), gives
\[
q(s_n)\le\operatorname{Re}F_n(a).
\]
On the chosen subnet this implies
\(L\le\operatorname{Re}F(a)\le\sup_{G\in\mathcal S_C}\operatorname{Re}G(a)\).
For each normalized \(G\), evaluating \(1+sa\) gives
\(q(s)\ge\operatorname{Re}G(a)\); hence the liminf is at least that same supremum. The two bounds prove the limit in (4).

Arbitrary compactness supplies subnets, and does not assert sequential compactness of this dual ball. The main proof can instead restrict the functionals to the at most two-dimensional span of \(1,a\), take a convergent coordinate subsequence there, and extend that restricted limit by Hahn–Banach. Neither route assumes separability of \(C\).

**Exercise 5.** In the heat estimate (6), the scalar envelope is the absolute derivative of the normalized kernel
\(g_t(s)=(4\pi t)^{-1/2}e^{-s^2/(4t)}\), \(t>0\).
Compute \(\int_{\mathbb R}|g_t'(s)|\,ds\) exactly. Check the value both by substitution and by the variation on the two half-lines.

*Solution.* Differentiation gives \(g_t'(s)=-s g_t(s)/(2t)\). Because \(g_t\) is even, its absolute derivative is even, and hence
\[
\int_{\mathbb R}|g_t'|
=\frac1t(4\pi t)^{-1/2}
  \int_0^\infty s e^{-s^2/(4t)}\,ds.
\]
For the last integral set \(v=s^2/(4t)\), so \(s\,ds=2t\,dv\). The scalar integral of \(e^{-v}\) on \([0,\infty)\) is one, by its antiderivative and its vanishing endpoint. Thus the last integral is \(2t\), and
\[
\int_{\mathbb R}|g_t'|
=2(4\pi t)^{-1/2}=\frac1{\sqrt{\pi t}}.
\]
On \([0,\infty)\), \(g_t\) decreases from \(g_t(0)\) to zero, so its variation is \(g_t(0)\). On the negative half-line it increases from zero to \(g_t(0)\). Adding these variations gives \(2g_t(0)\), the same value. This is valid for every positive \(t\), and is the precise constant bounding the norm integral in (6).

**Exercise 6.** Trace the two hypotheses of Lemma 2.1 through the heat estimate. Explain why numerical reality of \(h\) and of \(ih^2\) are both needed to conclude \(h=0\), rather than merely decay of \(he^{-th^2}\). Test the distinction on the nonzero self-adjoint matrix \(\operatorname{diag}(1,0)\) and on the scalar multiple \(e^{-i\pi/4}1\).

*Solution.* If \(h\) is numerical-real, (4) and the Euler construction show that \(e^{ish}\) and \(e^{-ish}\) are inverse contractions for real \(s\). Therefore their norms are one, and (6) gives
\[
\|he^{-th^2}\|
\le\int_{\mathbb R}|g_t'(s)|\,ds=\frac1{\sqrt{\pi t}}.
\]
This controls the damped vector.

The second hypothesis applies the same exponential construction to \(k=ih^2\):
\[
e^{itk}=e^{-th^2},\qquad e^{-itk}=e^{th^2}.
\]
Both have norm at most one and are inverses. Consequently
\[
\|h\|=\|(he^{-th^2})e^{th^2}\|
\le\|he^{-th^2}\|\le\|h\|.
\]
The heat bound is therefore a bound on \(\|h\|\) for every \(t>0\). Sending \(t\) to infinity gives zero.

For the matrix projection \(h=\operatorname{diag}(1,0)\), normalized functionals are states by Section 8.3, so \(h\) is numerical-real. Direct exponentiation gives
\[
he^{-th^2}=\operatorname{diag}(e^{-t},0),\qquad
\|he^{-th^2}\|=e^{-t},\quad
\|h\|=1,\quad \|e^{th^2}\|=e^t.
\]
Evaluation at the first diagonal entry is a normalized functional and takes \(ih^2\) to \(i\), so the second hypothesis fails. Decay of the damped element alone cannot yield \(h=0\). Conversely, for \(h=e^{-i\pi/4}1=(1-i)1/\sqrt2\), squaring its scalar coefficient gives \(h^2=-i1\), so \(ih^2=1\), which is numerical-real, while every normalized functional takes \(h\) to the nonreal scalar \(e^{-i\pi/4}\). Thus the second condition alone does not supply the first.

**Exercise 7.** To place a real projective lift inside the complex completion, let \(u=u^*\) be an algebraic tensor and start with an arbitrary complex decomposition \(u=\sum_jx_j\otimes y_j\). Construct a real decomposition and prove
\[
\|u\|_\pi\le\|u\|_{\pi_{\mathbb R}}\le2\|u\|_\pi.
\]
Explain how its upper factor \(2\) controls the inclusion of the completed real space.

*Solution.* Write \(x_j=a_j+ic_j\), \(y_j=b_j+id_j\) with self-adjoint parts. Average the decomposition of \(u\) with its adjoint:
\[
u=\frac{u+u^*}{2}
=\sum_j(a_j\otimes b_j-c_j\otimes d_j).
\]
This is a real decomposition, with cost at most
\(\sum_j(\|a_j\|\|b_j\|+\|c_j\|\|d_j\|)\).
For each \(j\), scalar Cauchy–Schwarz bounds its summand by
\[
(\|a_j\|^2+\|c_j\|^2)^{1/2}
(\|b_j\|^2+\|d_j\|^2)^{1/2}.
\]
Adjoint isometry in
\(a_j=(x_j+x_j^*)/2\), \(c_j=(x_j-x_j^*)/(2i)\)
gives \(\|a_j\|,\|c_j\|\le\|x_j\|\), and likewise
\(\|b_j\|,\|d_j\|\le\|y_j\|\). The product is at most \(2\|x_j\|\|y_j\|\). Taking the infimum over the original complex decompositions proves the upper bound. Every real decomposition is also an allowed complex decomposition, proving the lower bound.

The inequalities apply to differences of real tensors. A Cauchy sequence for the real norm is therefore Cauchy for the complex norm, and if its complex limit is zero the upper inequality forces its real limit to be zero. This proves injectivity of the inclusion of completions. For a self-adjoint complex projective limit, symmetrize finite approximants. They converge to it in the complex norm, and the upper inequality makes the symmetrized sequence Cauchy in the real norm. Thus its image is exactly the self-adjoint part of the complex completion, as used in (8).

**Exercise 8.** Let \(v\) be any vector of the completed real \(\sigma\)-space. Suppose that for every \(\varepsilon>0\) the random lift construction supplies \(u_\varepsilon\) with
\[
I(u_\varepsilon)=v,\qquad
\|u_\varepsilon\|_{\pi_{\mathbb R}}\le(81/16)\|v\|_\sigma+\varepsilon.
\]
Use injectivity to obtain an exact norm bound, including \(v=0\). Explain whether a convergent family of different lifts or an attaining algebraic decomposition is needed.

*Solution.* For any two positive tolerances,
\(I(u_\varepsilon-u_\delta)=0\).
Injectivity, using the real inclusion from Exercise 7, gives \(u_\varepsilon=u_\delta\). Thus every supplied lift is one fixed vector \(u\). Put \(K=81/16\). If \(d=\|u\|_{\pi_{\mathbb R}}-K\|v\|_\sigma\) were positive, the lift bound with \(\varepsilon=d/2\) would say \(d\le d/2\), a contradiction. Hence
\[
\|u\|_{\pi_{\mathbb R}}\le K\|v\|_\sigma.
\]
When \(v=0\), injectivity also gives \(u=0\), and the same bound is exact.

The approximate statements concern the costs of preimages. Uniqueness identifies their vectors before any limit argument, so no compactness of a projective ball and no convergence of distinct lifts enter. The projective norm remains an infimum of decomposition costs; the bound does not assert that one finite decomposition realizes that infimum.

**Exercise 9.** Let \(Q\) be a nonempty compact convex set and \(F_1,\ldots,F_m\) continuous real affine tests, with joint image \(K\subset\mathbb R^m\). When \(K\) misses the positive orthant, explain why the separating combination uses nonnegative coefficients and has strictly negative maximum on \(K\). Relate the orientation to positive coordinate rays and to the fact that the orthant contains zero.

*Solution.* The image \(K\) is nonempty, compact and convex. The continuous distance-squared function \(\|y_-\|^2\) attains a positive minimum at some \(y_0\): a zero minimum would put \(y_0\) in the orthant. Set
\(z_0=(y_0)_+\), \(w=z_0-y_0=(y_0)_-\).
Then \(w\ge0\), \(w\ne0\), and disjoint positive and negative coordinates give
\(w\cdot y_0=-\|w\|^2\).

For \(y\in K\) and \(0<t\le1\), \(y_0+t(y-y_0)\in K\). Its distance to the orthant is at most its distance to \(z_0\), while minimality bounds that distance below by the one at \(y_0\). Expanding the squared norm gives
\[
0\le-2t\,w\cdot(y-y_0)+t^2\|y-y_0\|^2.
\]
Divide by \(t\) and let \(t\downarrow0\). We obtain
\[
w\cdot y\le w\cdot y_0=-\|w\|^2<0.
\]
Thus \(\sum_jw_jF_j\) has strictly negative maximum on \(Q\), and every coefficient \(w_j\) is nonnegative. This is exactly the kind of combination permitted in the finite-test hypothesis.

The orientation can also be read from any strict separator that bounds its values below on the orthant and above on \(K\). A negative \(j\)-th coefficient would send its value on the ray \(re_j\), \(r\to\infty\), to \(-\infty\), violating that lower bound. Therefore every coefficient is nonnegative. Because zero belongs to the orthant, its infimum under such a functional is zero. Strict separation consequently puts the compact-set maximum below zero. Applying this contradiction to every finite test list yields the finite intersection property for the closed sets \(\{F\ge0\}\). Compactness of \(Q\) supplies one point satisfying the whole, possibly uncountable, family.

**Exercise 10.** Let \(V=V_1+iV_2\), where \(V_1,V_2\) are the self-adjoint parts in Theorem 6.1, and put \(K=81/16\). Each part has the bound
\[
|V_i(x,y)|\le K\|V\|
\sqrt{\varphi_i(q(x))\psi_i(q(y))}.
\]
Compute the bound for \(V\) using the mean states. Check that converting \(q(x)\) and \(q(y)\) to the two sums in (12) does not introduce another factor of two.

*Solution.* The triangle inequality first gives a sum of two nonnegative scalar bounds. Apply scalar Cauchy–Schwarz to that sum:
\[
\begin{aligned}
|V(x,y)|
&\le K\|V\|\sum_{i=1}^2
        \sqrt{\varphi_i(q(x))}\sqrt{\psi_i(q(y))}\\
&\le K\|V\|
 \sqrt{(\varphi_1+\varphi_2)(q(x))}
 \sqrt{(\psi_1+\psi_2)(q(y))}.
\end{aligned}
\]
Both sums are twice the mean states
\(\varphi=(\varphi_1+\varphi_2)/2\) and
\(\psi=(\psi_1+\psi_2)/2\).
The two square roots therefore multiply their factors \(\sqrt2\) into \(2\), giving
\(2K\|V\|\sqrt{\varphi(q(x))\psi(q(y))}\).
By the definition of \(q\),
\[
\sqrt{\varphi(q(x))\psi(q(y))}
=\tfrac12
 \sqrt{\varphi(x^*x+xx^*)\psi(y^*y+yy^*)}.
\]
That factor \(1/2\) cancels the \(2\) from the means. The coefficient in (12) is exactly \(K=81/16\). Convexity makes the means states, and the original two pairs worked for all inputs; hence the mean pair also works for every \(x,y\), including inputs whose quadratic values vanish.

## 8. Norm-preserving functional extension

We use extension in three places: to norm a vector in the projective algebra, to extend a limit on \(\operatorname{span}_{\mathbb C}\{1,a\}\), and to extend a spectral evaluation to a state. The construction below works on arbitrary subspaces of arbitrary normed spaces, whether or not they are closed or complete.

### 8.1. The precise norming-functional input

For the general real extension principle, let \(p:E\to\mathbb R\) be finite-valued and sublinear: \(p(x+y)\le p(x)+p(y)\) and \(p(tx)=tp(x)\) for \(t\ge0\). Let \(g:D\to\mathbb R\) be real linear with \(g\le p\). At \(z\notin D\), prescribe \(g_1(z)=c\) between
\[
\sup_{y\in D}[g(y)-p(y-z)]
\quad\text{and}\quad
\inf_{w\in D}[p(w+z)-g(w)].
\]
Each lower candidate is at most each upper candidate, since
\(g(y)+g(w)\le p(y+w)\le p(y-z)+p(w+z)\).
The choices \(y=0\) and \(w=0\) give finite bounds, so scalar completeness supplies \(c\). For \(t>0\), the upper inequality at \(y/t\) gives \(g(y)+tc\le p(y+tz)\). For \(t=-b<0\), the lower inequality at \(y/b\) gives \(g(y)-bc\le p(y-bz)\). Thus \(g_1(y+tz)=g(y)+tc\) is dominated everywhere on its enlarged domain. A chain's union is a linear dominated extension, because any finite list of vectors belongs to one domain in the chain. The original extension bounds the empty chain. Zorn supplies a maximal extension, and the one-vector construction shows that its domain is all of \(E\).

For a complex seminorm \(p\), satisfying \(p(\lambda x)=|\lambda|p(x)\), a complex linear \(f\) with \(|f|\le p\) has the same extension property. Extend its real part by the real principle and set \(F(x)=U(x)-iU(ix)\). Complex linearity and agreement on the original domain follow from \(U(ix)=-\operatorname{Im}f(x)\) there. Rotating \(x\) to make \(F(x)\) real nonnegative gives \(|F(x)|\le p(x)\). In particular this applies to \(p(x)=L\|x\|\). The norm-bounded construction, including its two signs and zero bound, is detailed next.

Let \(E\) be a real normed vector space, let \(D\subset E\) be a linear subspace, let \(f:D\to\mathbb R\) be linear, and let \(L\ge0\) satisfy \(|f(y)|\le L\|y\|\) on \(D\). If \(L=0\), the zero functional is an extension. Otherwise divide \(f\) by \(L\), so that \(L=1\). For \(z\notin D\), a real number \(c\) can be chosen between

\[
\sup_{y\in D}\{f(y)-\|y-z\|\}
\quad\hbox{and}\quad
\inf_{y\in D}\{\|y+z\|-f(y)\}.
\tag{A1}
\]

Indeed for \(y,w\in D\),

\[
f(y)+f(w)=f(y+w)\le\|y+w\|
\le\|y-z\|+\|w+z\|.
\]

Every member of the set in the supremum is therefore at most every member of the set in the infimum. Taking \(y=w=0\) in the comparison also supplies finite upper and lower bounds. Real completeness supplies \(c\). Define

\[
f_1(y+a z)=f(y)+a c,\qquad a\in\mathbb R.
\]

The representation is unique because \(z\notin D\), so \(f_1\) is linear. If \(a>0\), the upper inequality in (A1), applied to \(y/a\), gives \(f_1(y+a z)\le\|y+a z\|\). If \(a<0\), put \(b=-a>0\) and apply the lower inequality in (A1) to \(y/b\); it gives \(f(y)-b c\le\|y-b z\|\). The case \(a=0\) is the old bound. Applying the same upper bound to the negative vector gives \(|f_1(x)|\le\|x\|\). Thus extension by one real dimension preserves the bound.

Partially order all such extensions by extension of both domain and functional. In a chain, the union of the domains is a vector subspace: any two vectors lie together in one of the comparable domains. The union functional is unambiguous and linear for the same reason, extends \(f\), and obeys the same bound at each vector. Thus every chain has an upper bound. Zorn's lemma gives a maximal extension; if its domain were not \(E\), the one-dimensional construction would enlarge it. The domain is therefore \(E\). Rescaling gives the assertion for any \(L\).

For a complex normed space \(E\), let \(D\subset E\) be a complex linear subspace and let \(f:D\to\mathbb C\) be complex linear with \(|f(y)|\le L\|y\|\), \(L\ge0\). Apply the real assertion to \(u=\operatorname{Re}f\) on the underlying real space and obtain a real-linear \(U\) with \(|U(x)|\le L\|x\|\). Set

\[
F(x)=U(x)-iU(ix).
\tag{A2}
\]

Then \(F(ix)=iF(x)\), so \(F\) is complex linear. On the original complex subspace, \(u(ix)=-\operatorname{Im}f(x)\), hence \(F=f\). If \(F(x)\ne0\), choose \(|\lambda|=1\) with \(\lambda F(x)=|F(x)|\). It follows that

\[
|F(x)|=\operatorname{Re}F(\lambda x)=U(\lambda x)
\le L\|\lambda x\|=L\|x\|.
\]

For \(F(x)=0\) the inequality is immediate. This proves exactly the complex Hahn-Banach input used below. In particular, for \(x\ne0\), extend the functional \(\alpha x\mapsto\alpha\|x\|\) on \(\mathbb Cx\). The extension has norm one and takes the real positive value \(\|x\|\) at \(x\).

<a id="8-2-completion-and-the-projective-algebra"></a>

### 8.2. Completion and the projective algebra

For a real or complex normed space \(E\), use equivalence classes of Cauchy sequences, identifying \((x_n)\) and \((y_n)\) when \(\|x_n-y_n\|\to0\). The reverse triangle inequality makes \(\|[(x_n)]\|=\lim_n\|x_n\|\) well-defined. If this limit is zero, the sequence is equivalent to zero; the triangle inequality and homogeneity pass to classes. Constant sequences embed \(E\) isometrically. A class represented by \((x_n)\) lies within arbitrarily small distance of the constant class of a sufficiently late \(x_N\), proving density.

If classes \(z_n\) are Cauchy, choose \(x_n\in E\) within \(2^{-n}\) of \(z_n\). Then
\(\|x_n-x_m\|\le2^{-n}+\|z_n-z_m\|+2^{-m}\),
so \((x_n)\) is Cauchy. Its class is the limit of \(z_n\). This proves completeness, also for the zero space. A bounded linear \(T:E\to F\) into a Banach space extends by \(T[(x_n)]=\lim_n Tx_n\); its bound, independence of representative and uniqueness follow from this formula and density.

For a bilinear product of bound \(D\), Cauchy sequences are bounded and
\[
\|x_ny_n-x_my_m\|
\le D[\|x_n\|\|y_n-y_m\|+\|x_n-x_m\|\|y_m\|].
\]
The products therefore define classes independent of representatives, with the same bound. An isometric involution extends by applying it to each term. Every algebra identity follows on the dense subspace and passes to limits by these bounds.

For \(\pi\), the elementary upper bound is \(\|x\otimes y\|_\pi\le\|x\|\|y\|\). If both factors are nonzero, Section 8.1 gives unit-norm functionals \(f,g\) with \(f(x)=\|x\|\), \(g(y)=\|y\|\). Every finite decomposition satisfies
\[
|(f\otimes g)(u)|\le\sum_j\|x_j\|\|y_j\|.
\]
This proves equality for an elementary tensor. More generally, a nonzero finite tensor is detected by a pair of coordinate functionals on its finite factor spans. Those functionals are bounded: on a fixed finite basis the norm has a positive minimum on the Euclidean unit sphere, by scalar compactness. Extend them to the full factors by Section 8.1. Their tensor evaluation gives a positive lower bound for \(\|u\|_\pi\). Concatenating decompositions and scaling one leg give the norm's triangle inequality and homogeneity. The same construction over the real field gives \(\pi_{\mathbb R}\).

For two finite decompositions, tensor multiplication obeys
\[
\sum_{i,j}\|x_i z_j\|\|y_i w_j\|
\le\Big(\sum_i\|x_i\|\|y_i\|\Big)
   \Big(\sum_j\|z_j\|\|w_j\|\Big).
\]
Taking arbitrarily close costs proves \(\|uv\|_\pi\le\|u\|_\pi\|v\|_\pi\). Adjoint isometry on the factors and reversal of the decompositions give \(\|u^*\|_\pi=\|u\|_\pi\). Thus the completion is an involutive Banach algebra. For nonzero unital factors, the elementary tensor equality gives \(\|1\otimes1\|_\pi=1\); it is the identity first on finite tensors and then on their completion.

The preceding lesson proves \(\sigma\le\pi\), adjoint isometry and \(\|uv\|_\sigma\le4\|u\|_\sigma\|v\|_\sigma\). The completion construction therefore extends its product and involution. It also extends the algebraic identity to a contraction \(I\). Approximate two projective vectors by finite tensors; the two product estimates show that \(I\) preserves multiplication. The involution passes to limits in the same way. No injectivity of \(I\) is presupposed in constructing it.

<a id="8-3-positive-functionals-and-norming-states"></a>

### 8.3. Positive functionals and norming states

Let \(A\) be a nonzero unital C*-algebra. The scalar calculus and order facts in ITP F02–F08 give real self-adjoint spectra, positive square roots, \(x^*x\ge0\), and \(0\le p\le\|p\|1\) for positive \(p\). These statements concern every algebra, rather than a particular representation.

If \(f\in A^*\) has \(\|f\|=f(1)=1\), then for \(h=h^*\) and real \(t\),
\[
|1+itf(h)|^2\le\|1+ith\|^2
=\|1+t^2h^2\|\le1+t^2\|h\|^2.
\]
Writing \(f(h)=u+iv\), the inequality reads
\(-2tv+t^2|f(h)|^2\le t^2\|h\|^2\).
The two signs of \(t\), followed by \(t\to0\), force \(v=0\). For \(0\le h\le1\), scalar calculus gives \(\|1-h\|\le1\), and hence \(|1-f(h)|\le1\). Since \(f(h)\) is real, it is nonnegative. Dividing any nonzero positive element by its norm proves positivity on the entire cone; zero is automatic.

Conversely, a positive complex linear functional \(\varphi\) with \(\varphi(1)=1\) is bounded of norm one. Positivity makes its values on self-adjoint elements real, using their positive and negative parts, and gives \(\varphi(x^*)=\overline{\varphi(x)}\). Expanding \(\varphi((x-\lambda y)^*(x-\lambda y))\ge0\) and minimizing over \(\lambda\) proves
\[
|\varphi(y^*x)|^2\le\varphi(x^*x)\varphi(y^*y).
\]
If \(\varphi(y^*y)=0\), varying the phase and size of \(\lambda\) instead forces the cross term to be zero, proving that case too. Taking \(y=1\) and using \(x^*x\le\|x\|^21\) yields \(|\varphi(x)|\le\|x\|\). Its value at the identity makes the norm exactly one.

Extend \(\lambda1\mapsto\lambda\) by Section 8.1. The extension has norm one and is positive by the criterion, so states exist. For \(p\ge0\), \(p\ne0\), its scalar spectrum contains \(\|p\|\). The isometric calculus \(C(\sigma(p))\to C^*(1,p)\) from ITP F06 makes evaluation at \(\|p\|\) a norm-one functional with value one at the unit and value \(\|p\|\) at \(p\). Extend it to \(A\); the criterion gives a state \(\varphi\) with \(\varphi(p)=\|p\|\). If \(p=0\), any of the states just constructed norms it.

The closed dual ball is weak-* compact by Section 9. Inside it impose \(f(1)=1\) and, for every \(p\ge0\), the closed coordinate condition \(f(p)\in[0,\infty)\). Their intersection is exactly the state space, hence compact. It is convex by the two defining conditions. For two algebras, put both sets of coordinates into a single disk product and impose both sets of closed linearity and state conditions. This proves compactness of \(S(A)\times S(B)\) without a countable coordinate restriction.

<a id="8-4-disk-area-and-the-quarter-phase"></a>

### 8.4. Disk area and the quarter phase

The Gaussian normalization uses the disk area \(\pi R^2\). We can obtain it within scalar Riemann integration. For \(R>0\), put \(f_R(x)=\sqrt{R^2-x^2}\) on \([-R,R]\); scalar square-root continuity makes \(f_R\) uniformly continuous. In each narrow vertical strip, inscribed and circumscribed rectangles for the region between the graphs \(f_R\) and \(-f_R\) differ in total area by at most the strip's width times twice the oscillation of \(f_R\) there. The sum of these differences is at most \(4R\omega_{f_R}(\delta)\) for strip mesh at most \(\delta\), and tends to zero. Thus the disk has area
\[
\int_{-R}^{R}2\sqrt{R^2-x^2}\,dx.
\]
Define \(\pi=\int_{-1}^{1}2\sqrt{1-x^2}\,dx>0\). The substitution \(x=Ru\), justified on tagged sums, makes the displayed area \(\pi R^2\); the radius-zero disk has area zero.

The same rectangular construction permits continuous weights on a disk. On a square grid of side \(\delta\le1\), the cells meeting either boundary graph have total area at most
\[
4(R+1)\omega_{f_R}(\delta)+8(R+1)\delta,
\]
which tends to zero: in each column, cells meeting one graph have total height at most its oscillation plus \(2\delta\), and there are at most \(2R/\delta+2\) columns. Away from these boundary cells, upper and lower sums for a continuous weight differ by at most the bounding-box area times its modulus of continuity at \(\sqrt2\delta\). On the boundary cells their difference is bounded by twice a bound for the weight times the displayed area. Consequently the weighted sums converge. Subtracting two disk indicators gives annulus area \(\pi(r_2^2-r_1^2)\); disjoint finite sums and order inequalities pass from rectangular sums to their limits.

For a continuous radial weight \(w(|z|)\) on a disk of radius \(R\), partition \([0,R]\) into radial intervals. Its integral on each annulus is between the minimum and maximum of \(w\) there times that annulus's area. The difference of the two resulting sums is at most \(\pi R^2\omega_w(\delta)\). Because
\(r_j^2-r_{j-1}^2=2r_j^*\Delta r_j\) with \(r_j^*=(r_j+r_{j-1})/2\), their common limit is
\[
\int_0^R2\pi r\,w(r)\,dr.
\]
This proves the radial calculation used for \(I_R^2\), through finite area comparisons and continuous compact integrals.

It also identifies the quarter phase without an additional trigonometric assertion. Let
\[
I=\int_0^1\sqrt{1-u^2}\,du=\pi/4,\qquad
T(y)=\int_0^y(1-u^2)^{-1/2}\,du\quad(0\le y<1).
\]
The integrand is at most \((1-u)^{-1/2}\), whose integral from \(R\) to \(1\) is \(2\sqrt{1-R}\). Hence \(T(y)\) increases to a finite positive \(Q\). On \([0,R]\), differentiation of the square root and integration by parts give
\[
2\int_0^R\sqrt{1-u^2}\,du
=R\sqrt{1-R^2}+\int_0^R(1-u^2)^{-1/2}\,du.
\]
Letting \(R\uparrow1\) gives \(Q=2I=\pi/2\). The square-root derivative here follows directly by rationalizing its difference quotient; the integrands on every such compact interval have continuous derivatives.

For \(0\le t<Q\), the continuous strictly increasing function \(T\) has a unique inverse value \(y(t)\in[0,1)\), by the intermediate-value property. Its inverse is continuous: the images of two sufficiently close points on either side of \(y(t)\) bracket \(t\), so nearby inputs have inverse values between those points. Dividing the identity \(T(y(t+h))-T(y(t))=h\) by \(y(t+h)-y(t)\) therefore proves
\(y'(t)=\sqrt{1-y(t)^2}\) in the interior. Put \(x(t)=\sqrt{1-y(t)^2}\). Then \(x'=-y\), \(y'=x\), so \(z=x+iy\) satisfies \(z'=iz\), \(z(0)=1\). The scalar exponential series satisfies the same equation, and
\((z(t)e^{-it})'=0\); the continuous fundamental theorem makes this product constant. Thus \(z(t)=e^{it}\). As \(t\uparrow Q\), \(y(t)\uparrow1\): a smaller limit would have \(T(y)<Q\), contradicting the inverse identity and continuity. Therefore \(e^{iQ}=i\).

At \(t=Q/2\), both coordinates of \(e^{it}\) are positive and its square is \(i\). Writing them as \(x,y\) gives \(x^2-y^2=0\), \(2xy=1\), hence \(x=y=1/\sqrt2\). Conjugation of the exponential series now proves
\[
e^{-i\pi/4}=\frac{1-i}{\sqrt2},\qquad
i(e^{-i\pi/4})^2=1.
\]
This is the scalar identity used in the second counterexample of Exercise 6.

## 9. Weak-star compactness for arbitrary normed spaces

This supplies compactness of the state spaces and the alternative Banach–Alaoglu argument in Exercise 4. The closed unit dual ball is compact in the weak-star topology for every real or complex normed space; separability and completeness of the original space are unnecessary. The foundation boundary is ZFC, including Zorn’s lemma, scalar completeness and topology, and the definitions of a norm, a product topology and a weak-star topology. The needed arbitrary product step is proved here.

### 9.1. Proper filters and maximal extensions

A proper filter on a nonempty set \(S\) is a family of subsets containing \(S\), excluding the empty set, closed under finite intersections and upward inclusion. A family with the finite intersection property generates a proper filter by taking all supersets of its finite intersections. Order proper filters extending a fixed proper filter by inclusion. For a nonempty chain of proper filters extending the fixed filter, their union again contains the fixed filter and excludes the empty set. Any finite list of members of the union lies in a single filter of the chain: choose a filter containing each member and use the total ordering by inclusion to take the largest of the finitely many selected filters. Their intersection therefore belongs to the union and is nonempty. Upward closure also passes to the union. The fixed filter itself is an upper bound for the empty chain. Thus every chain has an upper bound in the ordered family, and Zorn's lemma gives a maximal proper extension. The maximal extension is denoted \(\mathcal U\).

For any \(A\subset S\), either \(A\in\mathcal U\) or \(S\setminus A\in\mathcal U\). Indeed, if adjoining \(A\) produced a proper filter, maximality would put \(A\) in \(\mathcal U\). Otherwise some \(F\in\mathcal U\) has \(F\cap A=\varnothing\), so \(F\subset S\setminus A\), and upward inclusion puts the complement in \(\mathcal U\). Such a maximal filter is an ultrafilter. If finitely many subsets cover a member of \(\mathcal U\), one of them is in \(\mathcal U\): otherwise all their complements would be in it, contradicting the nonempty-intersection requirement.

### 9.2. Every ultrafilter on a closed scalar disk converges

Let \(D_r=\{z\in\mathbb C:|z|\le r\}\), where \(r\ge0\), and let \(\mathcal U\) be an ultrafilter on \(D_r\). For \(r=0\), the disk is a singleton. For \(r>0\), begin with the closed square \([-r,r]^2\) and divide both coordinate intervals into halves. Its four closed subsquares cover the disk, so the preceding finite-cover argument selects a subsquare \(Q_1\) for which \(D_r\cap Q_1\in\mathcal U\). Continue within that square. This gives nested closed squares \(Q_n\), with \(D_r\cap Q_n\in\mathcal U\), and diameters tending to zero.

Write either coordinate interval of \(Q_n\) as \([a_n,b_n]\). The left endpoints increase, the right endpoints decrease, and \(b_n-a_n\to0\). By real completeness, \(c=\sup_n a_n\) exists. Nestedness gives \(a_n\le c\le b_n\) for every \(n\); the vanishing lengths make \(c\) the only point in every interval. Applying this to both coordinates gives a unique point \(z\) in every square. The proper-filter condition makes every \(D_r\cap Q_n\) nonempty. Choose \(w_n\) there; then \(|w_n-z|\le\operatorname{diam}(Q_n)\to0\), so the reverse triangle inequality gives \(|z|\le r\). Every disk neighborhood of \(z\) contains \(D_r\cap Q_n\) for all sufficiently large \(n\), hence belongs to the ultrafilter. This proves convergence. In the real case there is only one coordinate interval.

### 9.3. Arbitrary products of these disks are compact

Let \(P=\prod_{i\in I}D_{r_i}\), with its product topology; the point whose every coordinate is zero shows \(P\ne\varnothing\). If \(\mathcal U\) is an ultrafilter on \(P\), its image under a coordinate projection is an ultrafilter on the corresponding disk: a subset belongs to that image filter precisely when its inverse image belongs to \(\mathcal U\). The filter and complement rules pass through inverse images. Each image ultrafilter converges to a coordinate \(z_i\). These coordinates define \(z\in P\).

A basic neighborhood of \(z\) restricts only finitely many coordinates. Each inverse image of a restricted-coordinate neighborhood belongs to \(\mathcal U\); their finite intersection does as well. Every neighborhood contains such a basic neighborhood, so \(\mathcal U\) converges to \(z\).

Now suppose an open cover of \(P\) had no finite subcover. The complements of its members would have the finite intersection property. Extend their generated proper filter to an ultrafilter and let it converge to \(z\). A cover member containing \(z\) is a neighborhood and therefore belongs to the ultrafilter. Its complement belongs to it by construction, a contradiction. Thus every open cover has a finite subcover. This proves the precise arbitrary-product compactness needed here.

### 9.4. The dual ball is a closed subspace of the product

Let \(X\) be a complex normed space and set

\[
P_X=\prod_{x\in X}\{z\in\mathbb C:|z|\le\|x\|\}.
\]

An element \(b\in P_X\) is a scalar-valued function on \(X\) with \(|b(x)|\le\|x\|\). For each \(x,y\in X\) and \(\lambda\in\mathbb C\), the function

\[
b\longmapsto b(x+\lambda y)-b(x)-\lambda b(y)
\]

is continuous, since coordinate evaluations and finite scalar linear combinations are continuous. Its zero set is closed. Intersect all these zero sets. The intersection consists exactly of complex-linear functions satisfying the displayed bound: taking \(x=y=0\) first gives \(b(0)=0\), and the equations then give additivity and homogeneity. Such a function is continuous, because \(|b(x)-b(y)|\le\|x-y\|\), and has functional norm at most one. Conversely every functional of norm at most one belongs to this intersection.

Thus the closed unit ball of \(X^*\) is a closed subset of the compact space \(P_X\). A closed subset of a compact space is compact: extend any relative open cover to an ambient open cover by adding its open complement, take a finite subcover, then discard the complement. The restricted product topology is exactly the weak-star topology, because both are the topology generated by the evaluations \(f\mapsto f(x)\). This proves the required compactness. For real \(X\), use real intervals and real coefficients.

<a id="9-5-cluster-points-for-the-preserved-gaussian-proof"></a>

### 9.5. A convergent subnet of an arbitrary compact net

Let \((x_a)_{a\in A}\) be a net in a compact space \(K\), where \(A\) is directed and nonempty. For each \(a\), let \(T_a=\{x_b:b\ge a\}\). The closed sets \(\overline{T_a}\) have the finite intersection property: an index dominating a finite list of indices has its entire nonempty tail in all those tails. Their total intersection is nonempty, since otherwise their open complements would cover \(K\), and a finite subcover would contradict the finite intersection property. Fix \(p\) in that intersection. For every neighborhood \(U\) of \(p\) and every \(a\in A\), there is \(b\ge a\) with \(x_b\in U\).

To obtain an actual subnet, form the directed set

\[
B=\{(a,U,b):a,b\in A,\ U\text{ is a neighborhood of }p,
                  \ b\ge a,\ x_b\in U\}.
\]

Order it by

\[
(a,U,b)\preceq(a',U',b')
\quad\Longleftrightarrow\quad
a\le a',\quad U'\subseteq U,\quad b\le b'.
\]

For two triples choose \(c\) dominating their two tail indices and their two selected indices. The cluster property supplies \(b\ge c\) with \(x_b\in U\cap U'\); the triple \((c,U\cap U',b)\) dominates both. The map \(\phi:B\to A\), \(\phi(a,U,b)=b\), is order preserving. For any \(a_0\in A\), the triple \((a_0,K,a_0)\) belongs to \(B\), and every later triple has \(\phi\ge a_0\). Thus \(\phi\) is cofinal in the eventual sense required for a subnet. Finally, given a neighborhood \(V\) of \(p\), choose a triple whose neighborhood is \(V\). Every later triple has neighborhood contained in \(V\), so its selected term lies in \(V\). Hence \((x_{\phi(d)})_{d\in B}\) is a convergent subnet. This applies to the weak-star compact dual ball without separability or metrizability.

<a id="9-6-the-directional-limit-for-the-original-route"></a>

### 9.6. The directional limit using a dual-ball subnet

For the application in formula (4), set

\[
q(s)=\frac{\|1+sa\|-1}{s},\qquad s>0.
\]

The triangle inequality and its reverse give \(|q(s)|\le\|a\|\). Thus the finite real number \(L=\limsup_{s\downarrow0}q(s)\) exists by scalar completeness. Choose strictly decreasing \(s_n\downarrow0\) such that \(q(s_n)\to L\). Explicitly, for each \(n\) choose \(\delta_n>0\) with \(\sup_{0<s<\delta_n}q(s)<L+1/n\), and then choose \(s_n<\min\{\delta_n,1/n,s_{n-1}/2\}\) with \(q(s_n)>L-1/n\), omitting the final constraint for \(n=1\). Such a choice exists because the supremum on every interval \((0,\delta)\) is at least \(L\).

After discarding finitely many terms, \(1+s_na\ne0\). Use the norming-functional input already proved in Section 8.1 to choose \(F_n\in C^*\) with \(\|F_n\|=1\) and \(F_n(1+s_na)=\|1+s_na\|\). The dual-ball result and the preceding construction give a weak-star convergent subnet, with limit \(F\). For all \(n\),

\[
|F_n(1)-1|\le |\|1+s_na\|-1|+s_n|F_n(a)|
             \le2s_n\|a\|.
\]

Consequently \(F(1)=1\). The limit is still in the unit dual ball, so \(\|F\|\le1\); since \(\|1\|=1\), its value at \(1\) also gives \(\|F\|\ge1\). Thus \(F\) is normalized. Further,

\[
q(s_n)\le\operatorname{Re}F_n(a),
\]

because \(\operatorname{Re}F_n(1)\le1\). Passage along the convergent subnet gives

\[
L\le\operatorname{Re}F(a)
\le M:=\sup_{G\in\mathcal S_C}\operatorname{Re}G(a).
\]

For every normalized \(G\), evaluating \(1+sa\) gives \(q(s)\ge\operatorname{Re}G(a)\), hence \(\liminf_{s\downarrow0}q(s)\ge M\). Therefore

\[
M\le\liminf q\le\limsup q=L\le M,
\]

which proves the limit in (4) and the precise limsup assertion in Exercise 4. Compactness was used to take a subnet of the bounded functional sequence; no convergent functional subsequence was asserted.

The limiting functional argument and the two-dimensional restriction argument prove the same directional formula. Section 8.3 combines this arbitrary dual-ball compactness with the closed positivity conditions needed for the common-state selection.

## References

Gilles Pisier, [*Grothendieck's Theorem, past and present*, expanded UNCUT author version, 21 August 2013](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.UNCUT.pdf), Appendix 23, Lemma 23.1 and Proposition 23.2, printed pp.78–80 (PDF pp.80–82): compact affine separation, common-state selection and reciprocal rescaling. The corresponding appendix is in [arXiv:1101.4195v3](https://arxiv.org/pdf/1101.4195v3), printed pp.73–75 (PDF pp.75–77). Section 9 of the UNCUT version, printed pp.29–31 (PDF pp.31–33), treats the real truncation method of the preceding lesson.

Jacob Shapiro, [*Functional Analysis, Princeton University MAT520 Lecture Notes*, last typeset 10 December 2025](https://web.math.princeton.edu/~shapiro/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf#page=36), Theorems 4.4–4.5, printed/PDF pp.36–37: norm-preserving functional extension. Theorem 5.18, printed/PDF pp.44–45: weak-* compactness of the dual ball.

ITP F01–F13 prove completion, forced unitization, scalar spectrum, continuous calculus and order. [Elementary calculus for infinite products](elementary-calculus-for-infinite-products.md) proves their scalar and continuous norm-integral foundations. Real dominated functional extension and convex gauge separation are also given in CAR 19.1 and CAR 19.4.

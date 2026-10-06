# Lebesgue duality and the functionals on Fourier spaces

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Hölder's inequality turns an \(L^{p'}\) density into a functional on \(L^p\). To prove that these are all the functionals, we construct the density from the functional itself. The proof includes \(p=1\), keeps the exact norm, and then identifies the reciprocal and reflected weights in Fourier space.

[Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Sections 15.0–15.3, proves the integration and completeness results used here. Its generic measure-space proofs apply to the finite auxiliary measure we construct. Read [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md) for the moderate-weight isometry.

Grubb provides distribution background. The integration and completeness input used here is supplied by the linked internal Lebesgue foundation. The density construction below proves finite-exponent duality before applying it to the weighted Fourier spaces.

## A representing vector in Hilbert space

**Lemma 1.1.** In a complex Hilbert space \(H\) with inner product linear in its first argument, every continuous complex-linear \(L\) has a unique \(g\in H\) with \(L(v)=\langle v,g\rangle\), and \(\|L\|=\|g\|\).

**Proof.** If \(L=0\), take \(g=0\); uniqueness follows by testing the difference of two representing vectors against itself. Otherwise choose \(x\) with \(L(x)=1\). The subspace \(M=\ker L\) is closed by continuity. Let \(d=\inf_{m\in M}\|x-m\|\), and choose \(m_j\in M\) with \(\|x-m_j\|\to d\). The parallelogram identity gives

\[
\begin{gathered}
\|m_j-m_k\|^2
 \\
=2\|x-m_j\|^2+2\|x-m_k\|^2
      \\
-4\left\|x-\frac{m_j+m_k}{2}\right\|^2
 \\
\le 2\|x-m_j\|^2+2\|x-m_k\|^2-4d^2.
\end{gathered}
\tag{1}
\]

The right side tends to zero as \(j,k\to\infty\). Completeness and closedness give \(m_j\to m\in M\). Put \(y=x-m\). It minimizes the distance, has \(L(y)=1\), and hence is nonzero. For any \(h\in M\), \(\|y-th\|^2\ge\|y\|^2\) for every complex \(t\). Expanding the square, first with real \(t\) and then with purely imaginary \(t\), gives \(\langle y,h\rangle=0\). Every \(v\) has \(v-L(v)y\in M\), so

\[
 \langle v,y\rangle=L(v)\|y\|^2,\qquad
          g=\frac{y}{\|y\|^2}.
 \tag{2}
\]

The denominator is real and positive; therefore \(\langle v,g\rangle=L(v)\). The Hilbert Cauchy–Schwarz bound follows directly by expanding \(\|u-tv\|^2\ge0\) and taking \(t=\langle u,v\rangle/\|v\|^2\) when \(v\ne0\); its zero case is immediate. It gives \(\|L\|\le\|g\|\). Testing at \(g/\|g\|\) gives equality when \(g\ne0\). This proves all assertions without an orthonormal basis or separability. \(\square\)

For any positive measure \(\lambda\), \(L^2(\lambda)\) is such a Hilbert space. Its completeness is the general measure-space proof in [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section 15.3. The inner product \(\int u\bar v\,d\lambda\) is defined by Hölder and has the parallelogram identity by pointwise algebra and integral linearity. This identifies precisely the Hilbert space used below.

## Constructing a density on a finite set

Let \(Q\) be a Lebesgue measurable set of finite measure, let \(1\le p<\infty\), and let \(L:L^p(Q)\to\mathbb C\) be continuous with \(C=\|L\|\). Null sets are always factored out.

**Lemma 2.1.** There is \(g\in L^1(Q)\) such that \(L(a)=\int_Q a\bar g\,d\mu\) for every bounded measurable \(a\).

**Proof.** Define \(\nu(E)=L(1_E)\) for measurable \(E\subset Q\). It is finitely additive by linearity. If \(E_j\) are disjoint with union \(E\), the indicators of their finite unions tend to \(1_E\) in \(L^p\), since the measure of the omitted tail tends to zero by countable additivity and \(\mu(Q)<\infty\). Continuity gives countable additivity of \(\nu\).

Define its variation by finite measurable partitions:

\[
 \eta(E)=\sup_{E=\bigsqcup_{\ell=1}^r E_\ell}
                      \sum_{\ell=1}^r|\nu(E_\ell)|.
 \tag{3}
\]

For any such partition, choose unit scalars \(c_\ell\) with \(c_\ell\nu(E_\ell)=|\nu(E_\ell)|\); when the value is zero choose \(c_\ell=1\). The simple function \(a=\sum c_\ell1_{E_\ell}\) has modulus \(1_E\). Hence

\[
\begin{gathered}
\sum_\ell|\nu(E_\ell)|=L(a)
          \le C\mu(E)^{1/p},\\
\qquad
             0\le\eta(E)\le C\mu(E)^{1/p}.
\end{gathered}
\tag{4}
\]

Here \(L(a)\) is the nonnegative real displayed sum, so the norm inequality applies to its modulus. In particular \(\eta(Q)<\infty\), and \(\eta\) vanishes on every Lebesgue null set.

We verify countable additivity, rather than assuming a variation theorem. For disjoint \(A_j\) with union \(A\), partitions approximating \(\eta(A_j)\) for any finite list can be combined and supplemented by its remaining complement in \(A\). Taking the suprema gives \(\eta(A)\ge\sum_{j=1}^N\eta(A_j)\) for every \(N\). Conversely take any finite partition \(A=\bigsqcup_\ell B_\ell\). Countable additivity gives \(\nu(B_\ell)=\sum_j\nu(B_\ell\cap A_j)\). These sums are absolutely convergent: all finite partial sums of their absolute values are bounded by \(\eta(B_\ell)\), using the partition by those finitely many intersections and the remaining set. Thus

\[
\begin{gathered}
\sum_\ell|\nu(B_\ell)|
 \\
\le\sum_j\sum_\ell|\nu(B_\ell\cap A_j)|
 \\
\le\sum_j\eta(A_j).
\end{gathered}
\tag{5}
\]

Take the supremum over the finite partitions. The two inequalities prove countable additivity of \(\eta\). Set \(\lambda=\mu|_Q+\eta\), a finite positive measure on the same measurable sets.

For measurable simple \(a=\sum a_\ell1_{E_\ell}\) on a disjoint partition, the preceding variation definition gives

\[
\begin{gathered}
|L(a)|\le\sum_\ell|a_\ell|\eta(E_\ell)
       \\
=\int_Q|a|\,d\eta
       \\
\le\lambda(Q)^{1/2}\|a\|_{L^2(\lambda)}.
\end{gathered}
\tag{6}
\]

This is independent of representatives modulo \(\lambda\)-null sets because both \(\mu\) and \(\eta\) then vanish on the altered sets. Simple functions are dense in \(L^2(\lambda)\): truncate a function's modulus, then round its bounded real and imaginary parts on a finite grid; dominated convergence gives the truncation limit, and the grid error is bounded by its mesh times \(\lambda(Q)^{1/2}\). Therefore (6) extends uniquely to a continuous functional on \(L^2(\lambda)\). Lemma 1.1 supplies \(v\in L^2(\lambda)\) with

\[
 \nu(E)=\int_E\bar v\,d\lambda.
 \tag{7}
\]

Likewise \(a\mapsto\int_Q a\,d\mu\) on simple functions has bound \(\lambda(Q)^{1/2}\|a\|_{L^2(\lambda)}\), since \(\mu\le\lambda\). It extends and is represented by a \(w\in L^2(\lambda)\). Indicators give \(\mu(E)=\int_E\bar w\,d\lambda\). The imaginary part of \(w\) has integral zero over every measurable set; taking its positive and negative level sets shows it vanishes almost everywhere. Positivity and \(\mu(E)\le\lambda(E)\), again tested on level sets, give

\[
\begin{gathered}
\mu(E)=\int_E w\,d\lambda,\\
\qquad
              0\le w\le1\quad\lambda\text{-almost everywhere}.
\end{gathered}
\tag{8}
\]

All these level-set integrals exist because \(v,w\in L^1(\lambda)\) by finite-measure Hölder. For example, a set where \(w<-\varepsilon\) would have a negative integral if its measure were positive, contradicting \(\mu(E)\ge0\); use a countable union over positive rational \(\varepsilon\) to obtain \(w\ge0\). The other two assertions have the same explicit argument.

Let \(Z=\{w=0\}\). Equation (8) gives \(\mu(Z)=0\), and (4) gives \(\eta(Z)=0\). Thus \(\lambda(Z)=0\). Define \(g=v/w\) on \(\{w>0\}\), and \(g=0\) on \(Z\). The identity \(\int b\,d\mu=\int bw\,d\lambda\) for nonnegative measurable \(b\) follows first for simple functions from (8), then by increasing simple approximation and monotone convergence. Consequently

\[
\begin{gathered}
\int_Q|g|\,d\mu=\int_{\{w>0\}}|v|\,d\lambda<\infty,\\
\qquad
 \nu(E)=\int_E\bar g\,d\mu.
\end{gathered}
\tag{9}
\]

The equality for indicators extends by finite linear combinations to simple \(a\). Every bounded measurable \(a\) has uniformly convergent finite-grid simple approximants. Their \(L^p(\mu)\) differences tend to zero, while their representing integrals converge by the finite \(L^1\) bound in (9). This proves the stated representation for all bounded \(a\). If \(\mu(Q)=0\), \(L^p(Q)\) is the zero space, (4) gives \(\lambda(Q)=0\), and take \(g=0\) directly. \(\square\)

**Lemma 2.2.** The density in 2.1 belongs to \(L^{p'}(Q)\) and has \(\|g\|_{p'}\le C\), including \(p'=\infty\) when \(p=1\).

**Proof.** Suppose first \(1<p<\infty\). Define the bounded measurable test

\[
\begin{gathered}
a_M=1_{\{|g|\le M\}}\,g|g|^{p'-2},\\
\qquad
 A_M=\int_{\{|g|\le M\}}|g|^{p'}\,d\mu,
\end{gathered}
\tag{10}
\]

assigning value zero when \(g=0\). Its modulus is \(|g|^{p'-1}\) on the indicated set, so it is bounded even when the displayed exponent \(p'-2\) is negative. The identity \((p'-1)p=p'\) gives \(\|a_M\|_p=A_M^{1/p}\). 2.1 and the functional bound yield \(A_M\le C A_M^{1/p}\). If \(A_M=0\) the conclusion is immediate; otherwise division gives \(A_M^{1/p'}\le C\). Monotone convergence as \(M\to\infty\) proves \(\|g\|_{p'}\le C\).

For \(p=1\), use \(a=1_E g/|g|\), assigning zero on \(g=0\), for any measurable \(E\subset Q\). 2.1 gives \(\int_E|g|\,d\mu=L(a)\le C\mu(E)\). If \(E=\{|g|>C+\varepsilon\}\) had positive measure, the left side would exceed the right side. Hence all such sets are null, and \(\|g\|_\infty\le C\). This proof establishes the density bound, rather than inferring representation from Hölder. \(\square\)

## The full domain, exact norm and uniqueness

**Theorem 3.1.** For \(1\le p<\infty\), every continuous complex-linear \(L:L^p(\mathbb R^n)\to\mathbb C\) has a unique \(g\in L^{p'}(\mathbb R^n)\) with

\[
 L(f)=\int_{\mathbb R^n}f\bar g\,d\mu,\qquad
                       \|L\|=\|g\|_{p'}.
 \tag{11}
\]

For a bilinear integral convention, write \(h=\bar g\); then \(L(f)=\int fh\) with the same norm.

**Proof.** For \(n\ge1\), let \(Q_j=[-j,j]^n\). Restrict \(L\) by extending \(L^p(Q_j)\) functions by zero; the extension is isometric, so each restricted norm is at most \(C=\|L\|\). The preceding lemmas give \(g_j\in L^{p'}(Q_j)\) with norm at most \(C\).

Two such densities agree almost everywhere on their common box. Their difference \(b\) is integrable there and has \(\int_E\bar b=0\) for every measurable \(E\) in the common box, by testing indicators. Real and imaginary level sets show \(b=0\) almost everywhere. Removing the countable union of these pairwise exceptional null sets gives a measurable global \(g\) with \(g|_{Q_j}=g_j\) almost everywhere. For finite \(p'\), monotone convergence of the integrals over the boxes gives \(\|g\|_{p'}\le C\). For \(p'=\infty\), remove the countably many exceptional sets for \(|g_j|\le C\); their boxes cover space, giving the same global bound.

Bounded measurable functions with support in some \(Q_j\) are dense in \(L^p(\mathbb R^n)\): truncate the spatial support and then the modulus; dominated convergence applied to \(|f|^p\) proves the norm limit. On these bounded functions the representation is already proved. Hölder with the global \(g\) and continuity of \(L\) extend it to every \(f\). They also give \(\|L\|\le\|g\|_{p'}\). Together with the previous bound this proves equality; no separate attainment argument is necessary. Uniqueness follows on every \(Q_j\) from the indicator test just given, and hence on their union. In dimension zero, the Lebesgue convention is unit mass on the one-point space: every function is a scalar, \(L(z)=az\), and \(g=\bar a\) proves (11) for every displayed exponent. \(\square\)

The theorem covers the zero functional, a density vanishing on any subset, and \(p=1\). It makes no assertion that every functional on \(L^\infty\) has an \(L^1\) density.

## The weighted Fourier map

Use [the weighted Fourier lesson](weighted-fourier-spaces.md) Fourier convention \(\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx\), with inverse factor \((2\pi)^{-n}\). Its already proved weighted-space isomorphism is

\[
\begin{gathered}
J_{p,k}u=(2\pi)^{-n/p}k\widehat u,\\
\qquad
      \|J_{p,k}u\|_p=\|u\|_{p,k}.
\end{gathered}
\tag{12}
\]

The moderate weight and its reciprocal have polynomial bounds, so the inverse of this map defines the same tempered-distribution space proved in that lesson. Apply Theorem 3.1 to a functional composed with \(J_{p,k}^{-1}\). For its unique representing \(g\), define \(v\) by

\[
\begin{gathered}
\widehat v=(2\pi)^{n/p'}k g,\\
\qquad
 L_v(u)=(2\pi)^{-n}\int\widehat u\,\overline{\widehat v}.
\end{gathered}
\tag{13}
\]

When \(p'=\infty\), interpret \(n/p'=0\). Substitution into (13) gives exactly \(\int J_{p,k}u\,\bar g\), because \(n/p+n/p'=n\). Moreover

\[
\begin{gathered}
\|v\|_{p',1/k}
 =(2\pi)^{-n/p'}\|\widehat v/k\|_{p'}\\
=\|g\|_{p'}=\|L_v\|.
\end{gathered}
\tag{14}
\]

Polynomial bounds make the displayed \(\widehat v\) a tempered function, including the \(L^\infty\) endpoint. Thus every functional has the full claimed \(v\), with uniqueness and the exact norm. For the complex-linear distribution pairing set \(\widehat w(-\xi)=\overline{\widehat v(\xi)}\). If \(k^\vee(\xi)=k(-\xi)\), the density transformation gives

\[
\begin{gathered}
L_v(u)=\langle w,u\rangle,\\
\qquad
                  \|w\|_{p',1/k^\vee}=\|v\|_{p',1/k}.
\end{gathered}
\tag{15}
\]

These are the precise normalization, conjugation and reflection in [the weighted Fourier lesson](weighted-fourier-spaces.md) Theorem 5.1. No symmetric-weight hypothesis is added.

## Exercises with complete solutions

**Exercise 1 (intermediate).** In the finite-set proof, can one divide the density \(v\) by \(w\) merely because \(\mu\) is absolutely continuous with respect to \(\lambda\)? Identify the extra argument actually used.

**Solution 1.** Absolute continuity alone permits \(w=0\) on a set of positive \(\lambda\)-measure. Here (4) gives \(\eta(E)=0\) whenever \(\mu(E)=0\). For \(Z=\{w=0\}\), (8) gives \(\mu(Z)=0\), so \(\eta(Z)=0\) too. Since \(\lambda=\mu+\eta\), \(\lambda(Z)=0\). Hence \(w>0\) almost everywhere for the very measure used in the Hilbert representations, and \(g=v/w\) is valid after its explicit zero definition on \(Z\). Its \(L^1(\mu)\) bound is the full change-of-density identity (9).

**Exercise 2 (advanced).** Take \(p=1\) and a moderate nonsymmetric weight \(k\). State the unique representing weighted-space norm and the weight in the bilinear distribution form.

**Solution 2.** Here \(p'=\infty\), and \(\widehat v=kg\) with \(g\in L^\infty\). The norm is \(\|v\|_{\infty,1/k}=\|\widehat v/k\|_\infty=\|g\|_\infty\); the factors with \(n/p'\) are one. The bilinear density has \(\widehat w(\eta)=\overline{\widehat v(-\eta)}\), so its reciprocal weight is \(1/k^\vee(\eta)=1/k(-\eta)\). Reflection preserves the essential supremum and gives \(\|w\|_{\infty,1/k^\vee}=\|v\|_{\infty,1/k}\). Replacing \(k^\vee\) by \(k\) would require a symmetry hypothesis absent from the theorem.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Internal norm inequalities: [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html#section-15-2), Section 15.2, including finite-measure Hölder.
- Internal completeness: [the same foundation](../prerequisites/banach-foundation-bridges.html#section-15-3), Section 15.3, proves completeness on a general measure space, including the finite auxiliary measure used here.
- The representing-vector, finite-set density and global finite-exponent duality proofs are in this lesson, Lemmas 1.1 and 2.1–2.2 and Theorem 3.1; the final section applies the weighted isometry proved in the weighted Fourier lesson.

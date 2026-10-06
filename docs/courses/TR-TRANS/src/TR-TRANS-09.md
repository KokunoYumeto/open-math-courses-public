# Quasi-periods, complex multiplication and the modular invariant

*Written and mathematically self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra setting, October 2026. Original exposition and proofs are CC0. Linked open proofs retain their own licences. Prerequisites are identified below; no human or independent review is claimed.*

A period returns an elliptic function to the same value. A quasi-period records the additive change in its antiderivative. The two kinds of numbers are linked by an exact determinant, the Legendre relation. Together with the Schneider–Lang criterion, that determinant will rule out every algebraic linear combination of a primitive period and its associated quasi-period.

The functions, quotient growth bounds, cubic equation and period lattice are constructed in [Weierstrass functions, elliptic values and periods](TR-TRANS-08.md). We keep its normalization

\[
 L=\mathbb Z\omega_1+\mathbb Z\omega_2,
 \quad\operatorname{Im}(\omega_1/\omega_2)>0,
 \quad\wp'^2=4\wp^3-g_2\wp-g_3,
 \quad\zeta'=-\wp.
\]

The exact analytic inputs are the linked open proofs in Jiří Lebl's [*Guide to Cultivating Complex Analysis*](https://www.jirka.org/ca/ca.pdf), version 1.9, July 11, 2026: Theorem 3.3.4 for the Cauchy formula, Theorem 3.3.10 for Liouville's theorem and Theorem 5.3.2 for residues. The original author proofs are linked under the actual [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) licence option.

## 1. The determinant of periods and quasi-periods

Recall from (8.13)–(8.15) that

\[
 \zeta=\sigma'/\sigma,\qquad
 \zeta(z+\omega)=\zeta(z)+\eta(\omega),\qquad
 \eta:L\longrightarrow\mathbb C
\]

is additive. Write \(\eta_i=\eta(\omega_i)\). The zeta function is odd, with simple poles of residue one exactly at \(L\). It is a quotient of entire functions of strict order at most two. These properties were proved from the convergent sigma product, rather than assumed as properties of an unnamed antiderivative.

### Lemma 9.1. The Legendre relation

With the orientation above,

\[
 \omega_1\eta_2-\omega_2\eta_1=2\pi i.
 \tag{9.1}
\]

**Proof.** Choose a translated fundamental parallelogram whose boundary misses \(L\). Its positive basis is \(\lambda_1=\omega_2,\lambda_2=\omega_1\); put \(\theta_1=\eta_2,\theta_2=\eta_1\). There is exactly one lattice point in its interior, with zeta residue one. The positively oriented boundary integral is therefore \(2\pi i\).

Combine the bottom \(\lambda_1\)-side with the reversed top side. Quasi-periodicity replaces the top integrand by the bottom integrand plus \(\theta_2\), so their sum is \(-\lambda_1\theta_2\). The right \(\lambda_2\)-side and reversed left side similarly give \(\lambda_2\theta_1\). Thus the integral is \(\lambda_2\theta_1-\lambda_1\theta_2=\omega_1\eta_2-\omega_2\eta_1\), proving (9.1). \(\square\)

If \(\omega\) is primitive, then \(\omega/2\notin L\). Oddness at \(-\omega/2\) in the translation identity gives

\[
 \eta(\omega)=2\zeta(\omega/2).
 \tag{9.2}
\]

This formula is used only for primitive periods, or more generally periods whose halves are not poles. Additivity defines \(\eta(\omega)\) for every lattice element, whether or not its half is a pole.

### Lemma 9.2. Independence from a quasi-periodic coordinate

For complex constants \(a,b\) not both zero, the functions

\[
 \wp(z),\qquad h(z)=az+b\zeta(z)
\]

are algebraically independent over \(\mathbb C\).

**Proof.** At least one of \(c_i=a\omega_i+b\eta_i\) is nonzero. Otherwise the two equations \(c_1=c_2=0\), whose coefficient determinant is (9.1), would imply \(a=b=0\). Choose that period \(\omega_i\). Translation gives

\[
 h(z+n\omega_i)=h(z)+nc_i\qquad(n\in\mathbb Z).
\]

Suppose a nonzero polynomial relation were written \(\sum_j p_j(\wp)h^j=0\). Choose \(z_0\notin L\) for which at least one \(p_j(\wp(z_0))\ne0\). Such a choice exists because a nonzero polynomial has finitely many roots, while \(\wp\) takes every complex value. At \(z_0+n\omega_i\) the coefficients are unchanged and finite, but the distinct values \(h(z_0)+nc_i\) would all be roots of the same nonzero polynomial. This is impossible. \(\square\)

### Theorem 9.3. A period and its quasi-period

Suppose \(g_2,g_3\) are algebraic. If \(\omega\ne0\) belongs to \(L\), then for algebraic \(a,b\) not both zero,

\[
 a\omega+b\eta(\omega)
 \quad\hbox{is transcendental}.
 \tag{9.3}
\]

In particular every nonzero period and every quasi-period associated to a nonzero lattice element is transcendental; those quasi-periods are themselves nonzero.

**Proof.** First let \(\omega\) be primitive. Suppose \(c=a\omega+b\eta(\omega)\) were algebraic, including the possibility \(c=0\). Put \(e=\wp(\omega/2)\), a root of the cubic with algebraic coefficients, and

\[
 K=\mathbb Q(g_2,g_3,a,b,c,e).
\]

Use the three functions \(\wp,\wp',h=az+b\zeta\). They are quotients of entire functions of strict order at most two; sums and multiplication by \(z\) preserve that representation and bound. Their derivatives lie in their \(K\)-ring:

\[
 \wp'=\wp',\quad (\wp')'=6\wp^2-g_2/2,\quad h'=a-b\wp.
\]

The first and third functions are independent by Lemma 9.2. At each distinct nonpole point \(w_n=(n+1/2)\omega\), their values are

\[
 e,\qquad0,\qquad(n+1/2)c,
\]

using (9.2). All belong to \(K\), contradicting Theorem 7.2 for arbitrarily many points.

For an arbitrary nonzero \(\omega\), divide its integer basis coordinates by their gcd \(d\) to write \(\omega=d\lambda\) with \(\lambda\) primitive. Additivity gives \(\eta(\omega)=d\eta(\lambda)\). Thus its combination is \(d(a\lambda+b\eta(\lambda))\), transcendental by the proved case. Taking \((a,b)=(0,1)\) also excludes a zero quasi-period, since zero would be algebraic. \(\square\)

The conclusion is stronger than saying that the period and quasi-period cannot both be algebraic. It says that \(1,\omega,\eta(\omega)\) are linearly independent over the algebraic numbers: a relation with a nonzero period or quasi-period coefficient would make their combination algebraic.

### Proposition 9.4. Addition for zeta

As a meromorphic identity,

\[
 \zeta(u+v)=\zeta(u)+\zeta(v)+\frac12
 \frac{\wp'(u)-\wp'(v)}{\wp(u)-\wp(v)}.
 \tag{9.4}
\]

In particular, when \(u,2u\notin L\),

\[
 \zeta(2u)=2\zeta(u)+\frac{\wp''(u)}{2\wp'(u)}.
 \tag{9.5}
\]

**Proof.** Fix a generic \(v\), and denote the quotient in (9.4) by \(Q(u)\). Write \(X=\wp(u),Y=\wp(v),p=\wp'(u),q=\wp'(v)\). Direct differentiation and the cubic equation give

\[
 Q'=\frac{(6X^2-g_2/2)(X-Y)-(p-q)p}{(X-Y)^2},
 \qquad \frac12Q'+\frac14Q^2=2X+Y.
\]

For the second equality, multiply by \(4(X-Y)^2\) and substitute \(p^2=4X^3-g_2X-g_3\), \(q^2=4Y^3-g_2Y-g_3\); all terms cancel. The addition formula (8.10) now implies that the derivative with respect to \(u\) of the difference of the two sides of (9.4) is zero. Near zero,

\[
 \zeta(u)=u^{-1}+O(u^3),\qquad
 Q(u)=-2u^{-1}-2\wp(v)u+O(u^2).
\]

These expansions show that the constant difference is zero. The identity extends to all pairs meromorphically. Letting \(v\to u\) gives (9.5), with nonzero denominator because \(2u\notin L\). \(\square\)

## 2. When two lattices give dependent functions

Two lattices are **commensurable** if their intersection has finite index in each. Equivalently they span the same two-dimensional vector space over \(\mathbb Q\). For lattices \(L,M\), this is also equivalent to \(mM\subseteq L\) for some positive integer \(m\). Indeed, such an inclusion makes each basis vector of \(M\) a rational combination of a basis of \(L\); their real independence then shows that the rational spans coincide. Conversely equality of rational spans allows a common integer to clear both basis denominators, in both directions, so the intersection has finite index.

### Lemma 9.5. Even elliptic functions are rational in Weierstrass

Every even meromorphic function elliptic under \(L\) is a rational function of \(\wp_L\).

**Proof.** A fundamental cell contains finitely many poles, counted modulo \(L\). Let \(h\) be even. Consider a pole class \(v\ne0\) that is not a half-period, and set \(c=\wp(v)\). Then \(x=\wp(z)-c\) is a local coordinate at \(v\), since \(\wp'(v)\ne0\). The elementary inverse argument from section 6 of Lesson 8 supplies its convergent local inverse. The principal part of \(h\) in this coordinate is therefore a finite sum \(\sum_{k\geq1}a_kx^{-k}\). Subtracting \(\sum a_k(\wp-c)^{-k}\) cancels its pole at \(v\) and, by evenness, its pole at \(-v\). These are the only possible poles of that rational expression by the exact fibre count.

At a nonzero half-period \(v\), evenness and \(2v\in L\) give \(h(v+t)=h(v-t)\). Its Laurent series contains only even powers of \(t\). Also \(\wp(v+t)-c\) is even, with leading term \(dt^2\), \(d\ne0\), because its fibre is exactly double. Regard the two series as series in \(s=t^2\); the latter has nonzero derivative and hence a local inverse in \(s\). Again the principal part of \(h\) is a finite sum of negative powers of \(\wp-c\), which cancels the entire pole class.

At zero, the even Laurent series has leading polar power \(z^{-2k}\). Successively subtract multiples of \(\wp^k\), whose leading term is \(z^{-2k}\), until its principal part is removed. No new pole classes are introduced by these operations. The remainder is an entire elliptic function and is constant. Reassembling the subtractions expresses \(h\) as a rational function of \(\wp\). \(\square\)

### Theorem 9.6. Algebraic dependence and commensurability

The functions \(\wp_L(z),\wp_M(z)\) are algebraically dependent over \(\mathbb C\) if and only if their lattices are commensurable, equivalently

\[
 mM\subseteq L\quad\hbox{for some integer }m>0.
 \tag{9.6}
\]

**Proof.** Suppose first that the functions are dependent. Since \(\wp_M\) is nonconstant, it is transcendental over the constant field: a nonzero constant-coefficient polynomial has only finitely many roots, whereas \(\wp_M\) takes all complex values. We can therefore make a polynomial relation monic over \(\mathbb C(\wp_M)\):

\[
 \wp_L^n+a_{n-1}(\wp_M)\wp_L^{n-1}
 +\cdots+a_0(\wp_M)=0,\qquad n\geq1,
 \tag{9.7}
\]

where the \(a_j\) are rational functions.

Fix a basis period \(\nu\) of \(M\). Choose \(z_0\) so that all coefficients in (9.7) are finite there, all \(z_0+k\nu\) are nonpoles of \(\wp_L\), and

\[
 2z_0\notin L+\mathbb Z\nu.
 \tag{9.8}
\]

Only countably many points are forbidden: lattice translates, their halves, and the discrete fibres of finitely many rational coefficient poles. A complex point outside that countable union exists. Translation by \(k\nu\) leaves \(\wp_M\), and thus the coefficients of (9.7), unchanged. Its infinitely many values \(\wp_L(z_0+k\nu)\) lie among the finitely many roots of one monic polynomial. Some two values, with \(k\ne\ell\), agree. The fibre identity (8.8) gives either

\[
 (k-\ell)\nu\in L,
 \quad\hbox{or}\quad
 2z_0+(k+\ell)\nu\in L.
\]

The second alternative is excluded by (9.8). Thus a positive integer multiple of \(\nu\) is in \(L\). Apply this argument separately to both basis vectors of \(M\), and take a common multiple of the resulting positive integers. This proves (9.6).

Conversely suppose \(mM\subseteq L\). The function \(\wp_L(mz)\) is even and \(M\)-elliptic, so Lemma 9.5 expresses it as \(R(\wp_M(z))\). It is also even and \(L\)-elliptic, giving \(S(\wp_L(z))\). Both \(R,S\) are nonconstant, since \(\wp_L(mz)\) has poles and is nonconstant. Clearing denominators in \(R(Y)-S(X)\) yields a nonzero polynomial relation. It is nonzero because two nonconstant rational functions of independent formal variables cannot be identical: fixing a regular value of one variable would otherwise make the other function constant. Hence the two Weierstrass functions are algebraically dependent. \(\square\)

The exclusion (9.8) accounts for the second sign in a Weierstrass fibre. Repeated values alone do not automatically give a period difference without checking that alternative.

### Lemma 9.7. Simultaneous algebraic values

Suppose \(L,M\) both have algebraic invariants. If at a common nonpole \(w\) both \(\wp_L(w),\wp_M(w)\) are algebraic, then the two functions are algebraically dependent.

**Proof.** Their derivatives at \(w\) are algebraic by their cubic equations. Let \(K\) contain these four values and all four invariants. The \(K\)-ring generated by \(\wp_L,\wp'_L,\wp_M,\wp'_M\) is stable under differentiation, and all generators have strict order at most two. If the two Weierstrass functions were independent, Theorem 7.2 would permit only finitely many points with all four values in \(K\).

For each lattice, classify the class of \(w\) in its torus. If it has infinite order, the duplication and addition induction in Theorem 8.9 shows that both coordinates at every positive multiple \(nw\) lie in \(K\). That induction uses infinite order to exclude poles and every zero addition denominator; it does not require the argument itself to be algebraic. If its class has finite order \(r\), then \(r\geq2\), since \(w\) is a nonpole. At each \(n\equiv1\pmod r\), its two values equal those at \(w\), and are finite and in \(K\).

Choose \(N\) to be the least common multiple of the finite orders that occur, or \(N=1\) if neither occurs. At every point \((1+kN)w\), \(k\geq0\), both cases give all four values in \(K\), with no poles. These points are distinct because \(w\ne0\). This contradicts the criterion and proves dependence. \(\square\)

## 3. Schneider's theorem for the modular invariant

Recall the invariant and homothety criterion proved in Theorem 8.11:

\[
 j(\tau)=1728\frac{g_2(L_\tau)^3}
 {g_2(L_\tau)^3-27g_3(L_\tau)^2},
 \qquad L_\tau=\mathbb Z\tau+\mathbb Z,
 \quad\tau\in\mathfrak H.
 \tag{9.9}
\]

Scaling does not change \(j\), and two lattices have the same invariant exactly when they are homothetic. For the normalized lattices, homothety is equivalent to the action of \(\mathrm{SL}_2(\mathbb Z)\). To check the converse of the basis-change formula (8.21), write a homothety's images of \(\tau,1\) as an integer basis of \(L_{\tau'}\). Its matrix has determinant \(\pm1\); complex multiplication by a nonzero scale preserves real orientation, so the determinant is \(+1\). Taking the ratio gives the required fractional linear transformation. Thus \(j\) classifies complex tori up to their origin-preserving analytic isomorphisms induced by lattice homothety.

### Theorem 9.8. Schneider's modular invariant theorem

If \(\tau\in\mathfrak H\) is algebraic and is not imaginary quadratic, then \(j(\tau)\) is transcendental.

**Proof.** Suppose \(j(\tau)\) were algebraic. Scale \(L_\tau\) so that its new invariants are algebraic. Explicitly, if \(j\ne0\), choose a fourth-root scale making \(g_2=1\); then

\[
 g_3^2=\frac{1-1728/j}{27}
\]

makes \(g_3\) algebraic. If \(j=0\), then \(g_2=0\) and a sixth-root scale makes \(g_3=1\). Let the resulting basis be \(\omega_1,\omega_2\), still with \(\omega_1/\omega_2=\tau\), and put \(M=\tau L\). Its invariants are \(\tau^{-4}g_2,\tau^{-6}g_3\), hence algebraic. The scaling identity gives

\[
 \wp_M(\tau z)=\tau^{-2}\wp_L(z).
\]

At \(w=\omega_1/2\), both functions are finite: it is a nonzero half-period of \(L\), and \(w/\tau=\omega_2/2\) is a nonzero half-period of \(L\), so \(w\) is also a nonzero half-period of \(M\). Their values are algebraic cubic roots, with the second value equal to \(\tau^{-2}\wp_L(\omega_2/2)\). Lemma 9.7 and Theorem 9.6 give \(m\tau L\subseteq L\) for some positive integer \(m\).

Multiplication by \(m\tau\) consequently has an integer matrix on the basis of \(L\). Its characteristic polynomial has degree two and rational coefficients, and vanishes at \(m\tau\). One can see this directly by applying the matrix to the nonzero complex row of its two basis vectors, which is an eigenvector for the transpose with eigenvalue \(m\tau\). Hence \(\tau\) has degree at most two over \(\mathbb Q\). It is nonreal, so its degree is exactly two, and its field is imaginary quadratic. This contradicts the hypothesis. \(\square\)

For example, \(j(i\sqrt[3]{2})\) is transcendental. Indeed, if \(i\sqrt[3]{2}\) had degree at most two, its square \(-\sqrt[3]{4}\) would lie in a field of degree at most two. But \(\sqrt[3]{4}\) has degree three: the cubic \(X^3-4\) has no rational root, and a reducible cubic over \(\mathbb Q\) would have a linear factor. This is impossible by the tower formula.

## 4. An ellipse and a quasi-period

Let an ellipse have real algebraic semiaxes \(a>b>0\), and put \(k^2=1-b^2/a^2\), so \(0<k^2<1\). Its perimeter is

\[
 C=4aE(k),\qquad
 E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2\theta}\,d\theta.
 \tag{9.10}
\]

To prove the formula, parametrize it by \((a\cos\theta,b\sin\theta)\). Its speed is \(a\sqrt{1-k^2\cos^2\theta}\); four quadrant integrals and the change \(\theta\mapsto\pi/2-\theta\) give (9.10).

Consider the cubic with roots

\[
 e_1=(2-k^2)/3,\qquad e_2=(2k^2-1)/3,
 \qquad e_3=-(1+k^2)/3.
\]

They are distinct, real and algebraic, sum to zero, and satisfy \(e_1-e_3=1\), \(e_2-e_3=k^2\). The invariants determined by \(4\prod(X-e_i)=4X^3-g_2X-g_3\) are algebraic and nonsingular, so Theorem 8.11 supplies its lattice. The positive real half-period is

\[
 K=\int_{e_1}^\infty\frac{dx}{\sqrt{4\prod(x-e_i)}}
 =\int_0^1\frac{dt}{\sqrt{(1-t^2)(1-k^2t^2)}},
 \tag{9.11}
\]

by \(x=e_3+t^{-2}\). Section 6 of Lesson 8 proves that \(\omega=2K\) is the least positive real period. It is primitive in the lattice: a common integer factor in its basis coordinates would give a smaller positive real period. Put \(\eta=\eta(\omega)=2\zeta(K)\).

### Proposition 9.9. The exact perimeter combination

For this normalization,

\[
 E(k)=\zeta(K)+e_1K=\frac{\eta+e_1\omega}{2},
 \qquad C=2a(\eta+e_1\omega).
 \tag{9.12}
\]

In particular the perimeter of every ellipse with real algebraic semiaxes \(a>b>0\) is transcendental.

**Proof.** On \(0<z\leq K\), set \(t=(\wp(z)-e_3)^{-1/2}\), taking the positive real branch. Then \(t\) increases from zero to one, and (9.11) gives

\[
 dz=\frac{dt}{\sqrt{D(t)}},\qquad
 D(t)=(1-t^2)(1-k^2t^2).
\]

Differentiate \(H(t)=\sqrt{D(t)}/t\) to obtain

\[
 H'(t)=\frac{k^2t^4-1}{t^2\sqrt{D(t)}},\qquad
 \frac1{t^2\sqrt{D(t)}}=-H'(t)+\frac{k^2t^2}{\sqrt{D(t)}}.
\]

Since \(\zeta'=-\wp\), integration from \(\varepsilon\) to \(K\), with \(t_\varepsilon=(\wp(\varepsilon)-e_3)^{-1/2}\), gives

\[
 \zeta(K)=\zeta(\varepsilon)-e_3(K-\varepsilon)
 -H(t_\varepsilon)-k^2\int_{t_\varepsilon}^1\frac{t^2\,dt}{\sqrt{D(t)}}.
\]

The local expansions \(\wp(\varepsilon)=\varepsilon^{-2}+O(\varepsilon^2)\) and \(\zeta(\varepsilon)=\varepsilon^{-1}+O(\varepsilon^3)\) imply \(t_\varepsilon=\varepsilon+O(\varepsilon^3)\) and \(H(t_\varepsilon)=\varepsilon^{-1}+O(\varepsilon)\). Their divergent terms cancel. Taking the limit gives

\[
 \zeta(K)=-e_3K-k^2\int_0^1\frac{t^2\,dt}{\sqrt{D(t)}}.
\]

On substituting \(t=\sin\theta\) in (9.10),

\[
 E(k)=\int_0^1\frac{1-k^2t^2}{\sqrt{D(t)}}\,dt
 =K-k^2\int_0^1\frac{t^2\,dt}{\sqrt{D(t)}}.
\]

As \(1+e_3=e_1\), subtraction proves (9.12). Its coefficients \(2a,2ae_1\) are algebraic and the quasi-period coefficient \(2a\) is nonzero. Theorem 9.3 therefore makes the perimeter transcendental. \(\square\)

Waldschmidt's *Transcendence Methods*, Corollary 7.1.2, states that the nonzero periods of elliptic integrals of the first and second kinds defined over \(\overline{\mathbb Q}\) are transcendental; this contains the ellipse consequence. The calculation above supplies the precise curve, coefficients, path and normalization needed to apply that corollary here.

## 5. Algebraic invariants at imaginary quadratic points

The preceding theorem excludes algebraic \(j\)-values at algebraic points of degree greater than two. We now prove the complementary assertion: at imaginary quadratic points the invariant is an algebraic integer. The proof needs an arithmetic polynomial relating the invariants of a lattice and its finite-index sublattices. We construct that polynomial before using it.

### Proposition 9.10. The Fourier expansion and its integral coefficients

Put \(q=e^{2\pi i\tau}\), \(|q|<1\), and \(\sigma_r(n)=\sum_{d\mid n}d^r\). Then

\[
 \begin{aligned}
 E_4(q)&=1+240\sum_{n\geq1}\sigma_3(n)q^n,
 &g_2(L_\tau)&=\frac{4\pi^4}{3}E_4(q),\\
 E_6(q)&=1-504\sum_{n\geq1}\sigma_5(n)q^n,
 &g_3(L_\tau)&=\frac{8\pi^6}{27}E_6(q).
 \end{aligned}
 \tag{9.13}
\]

Moreover

\[
 j(\tau)=\frac{1728E_4(q)^3}{E_4(q)^3-E_6(q)^2}
 =q^{-1}+744+196884q+21493760q^2+\cdots,
 \tag{9.14}
\]

and all Laurent coefficients are integers.

**Proof.** For \(\operatorname{Im}z>0\), the partial fraction formula (8.18) and the geometric series give

\[
 S_2(z):=\sum_{n\in\mathbb Z}(z-n)^{-2}
 =-4\pi^2\sum_{r\geq1}r e^{2\pi i r z}.
\]

Indeed \(\sin^{-2}(\pi z)=-4w/(1-w)^2\), \(w=e^{2\pi iz}\). Differentiate \(2k-2\) times, using locally uniform convergence on closed subregions of the upper half-plane:

\[
 S_{2k}(z)=\frac{-4\pi^2(2\pi i)^{2k-2}}{(2k-1)!}
 \sum_{r\geq1}r^{2k-1}e^{2\pi i r z}.
\]

The row with zero \(\tau\)-coordinate in \(G_4,G_6\) was computed in Lemma 8.10. Pairing the other rows \(m\) and \(-m\), we get

\[
 \begin{aligned}
 G_4&=\frac{\pi^4}{45}+\frac{16\pi^4}{3}
       \sum_{m,r\geq1}r^3q^{mr},\\
 G_6&=\frac{2\pi^6}{945}-\frac{16\pi^6}{15}
       \sum_{m,r\geq1}r^5q^{mr}.
 \end{aligned}
\]

Absolute convergence justifies collecting the coefficient of \(q^n\), which is the corresponding divisor sum. This proves (9.13) and the quotient in (9.14).

For integrality set \(A=\sum\sigma_3(n)q^n\), \(B=\sum\sigma_5(n)q^n\). Expansion gives

\[
 \frac{E_4^3-E_6^2}{1728}
 =\frac{5A+7B}{12}+100A^2+8000A^3-147B^2
 =q+O(q^2).
 \tag{9.15}
\]

Each coefficient of \((5A+7B)/12\) is an integer. For every integer \(d\), \(5d^3+7d^5\) is divisible by three because \(d^3\equiv d^5\equiv d\pmod3\); it is divisible by four because even \(d\) gives multiples of eight, while odd \(d\) gives \(d^3\equiv d^5\equiv d\pmod4\). Sum this over divisors of \(n\). Thus the right side of (9.15) is \(q\) times a power series in \(\mathbb Z[[q]]\) with constant term one. Its reciprocal also has integer coefficients, recursively: if \(1+\sum d_nq^n\) has inverse \(1+\sum c_nq^n\), then \(c_n=-\sum_{r=1}^n d_rc_{n-r}\). Multiplication by \(E_4^3\) proves the integral Laurent expansion. Its displayed initial coefficients follow by the same finite series division. \(\square\)

This argument proves integrality without requiring a product formula for the discriminant. The series converge analytically for \(|q|<1\); formal division gives their analytic Laurent coefficients near zero, and the nonvanishing lattice discriminant continues the quotient throughout the punctured disc.

### Lemma 9.11. A holomorphic modular function with a finite cusp limit

Let \(f\) be holomorphic on \(\mathfrak H\), invariant under \(\mathrm{SL}_2(\mathbb Z)\), and have a convergent Laurent series in \(q\) with only finitely many negative powers. Then \(f\) is a polynomial in \(j\). If its Laurent coefficients are integers, that polynomial has integer coefficients.

**Proof.** First suppose no negative powers occur. Reduction to \(\mathcal F\), proved in Theorem 8.11, shows that the image together with the finite cusp value \(f(\infty)\) is compact: a sequence of reduced arguments either has bounded imaginary parts, giving a subsequence in a compact subset of \(\mathfrak H\), or has a subsequence tending to the cusp, giving that finite limit. The modulus consequently attains its maximum in this enlarged image. If it is attained at a point in \(\mathfrak H\), the maximum modulus principle makes \(f\) constant. If it is attained only at the cusp, its holomorphic \(q\)-series on a disc around zero attains that maximum at the interior point zero, again making it constant. Equality on that disc extends by the identity theorem.

For general \(f\), the leading term \(j=q^{-1}+O(1)\) lets us cancel its finite principal part successively by a polynomial in \(j\). The remainder is constant by the preceding case. When the Laurent coefficients are integers, each cancellation coefficient is an integer because the leading coefficient of every \(j^r\) is one; the final constant is an integer as well. \(\square\)

### Proposition 9.12. The sublattice polynomial

For every positive integer \(m\), there is a polynomial \(\Psi_m(X,Y)\in\mathbb Z[X,Y]\), monic in \(X\), such that

\[
 \Psi_m(X,j(\tau))=
 \prod_{\substack{a,d>0,\ ad=m\\0\leq b<d}}
 \left(X-j\left(\frac{a\tau+b}{d}\right)\right).
 \tag{9.16}
\]

The factors are precisely the invariants of all index-\(m\) sublattices of \(L_\tau\), with multiplicities retained. If \(m\) is not a square, \(\Psi_m(X,X)\) is a nonconstant polynomial with leading coefficient \(1\) or \(-1\).

**Proof.** Each index-\(m\) sublattice has a unique basis \(a\tau+b,d\) with \(a,d>0\), \(ad=m\), \(0\leq b<d\). To see this, project its integer coordinates onto the \(\tau\)-coordinate. The image is \(a\mathbb Z\); its intersection with the integer direction is \(d\mathbb Z\). Choose a vector with first coordinate \(a\), reduce its second coordinate modulo \(d\), and subtract its multiples from every vector of the sublattice. This proves the basis assertion. Its index is \(ad\), as representatives for the two coordinates give \(ad\) cosets. Scaling by \(d\) gives the invariant appearing in (9.16).

An integer change of basis of the ambient lattice permutes its index-\(m\) sublattices. The homothety formula (8.21) therefore makes each coefficient of the product a holomorphic modular invariant function. Each factor has Laurent expansion

\[
 j\left(\frac{a\tau+b}{d}\right)
 =\zeta_d^{-b}q^{-a/d}+744+
 \sum_{n\geq1}c_n\zeta_d^{bn}q^{an/d},
 \qquad\zeta_d=e^{2\pi i/d},\quad c_n\in\mathbb Z.
\]

For the finite product its coefficients lie in the Laurent series ring in \(q^{1/m}\) with coefficients in \(\mathbb Z[\zeta_m]\), and have only finitely many negative powers. Invariance under \(\tau\mapsto\tau+1\) removes all fractional exponents. Every automorphism of \(\mathbb Q(\zeta_m)/\mathbb Q\) sends \(\zeta_m\) to another root of exact order \(m\), hence to \(\zeta_m^k\) with \(k\) coprime to \(m\), and permutes the factors by \(b\mapsto kb\pmod d\). Thus each Laurent coefficient is fixed by every such automorphism. This field is the splitting field of \(X^m-1\); the embedding extension argument supplied in Lemma 2.9 implies that a fixed coefficient has only itself as a conjugate, so is rational. It is also an algebraic integer, being in \(\mathbb Z[\zeta_m]\), so is an ordinary integer. The integral-ring and rational-integrality prerequisites are exactly those specified in [Heights of algebraic numbers](TR-TRANS-02.md). No assertion that every unit \(k\) occurs as an automorphism is needed here. Lemma 9.11 now expresses every coefficient as an integer polynomial in \(j\), proving (9.16).

For \(m\) nonsquare, every pair \(ad=m\) has \(a/d\ne1\). Consequently each diagonal factor \(j(\tau)-j((a\tau+b)/d)\) has a nonzero leading term at \(q=0\), of negative exponent \(-\max(1,a/d)\) and leading coefficient either one or a negative root of unity. Their product therefore has a pole at zero and a root of unity as its leading coefficient. On the other hand it is \(\Psi_m(j,j)\), so it has integral powers of \(q\) and integer leading coefficient. A rational root of unity is \(1\) or \(-1\). Since \(j\) has leading term \(q^{-1}\), this is also the leading coefficient of the nonconstant diagonal polynomial. \(\square\)

The polynomial here uses all sublattices. The usual modular polynomial \(\Phi_m\) keeps only sublattices with cyclic quotient. For prime \(m\) the two definitions agree, so \(\Psi_2=\Phi_2\). Keeping all sublattices avoids an unnecessary cyclicity assumption in the existence proof below.

### Theorem 9.13. Complex multiplication gives algebraic integers

For every imaginary quadratic \(\tau\in\mathfrak H\), \(j(\tau)\) is an algebraic integer.

**Proof.** Write \(a\tau^2+b\tau+c=0\) with integers \(a>0,b,c\). Then multiplication by \(\alpha=a\tau\) preserves \(L_\tau\): it sends \(1\) to \(a\tau\) and \(\tau\) to \(-b\tau-c\). Its matrix on the lattice has integer trace \(t\) and determinant \(u\), with \(t^2-4u<0\), because its eigenvalues are the nonreal conjugate numbers \(\alpha,\overline\alpha\). Multiplication by \(n+\alpha\) also preserves the lattice and has index

\[
 m=n^2+tn+u=|n+\alpha|^2.
\]

For sufficiently large positive \(n\), this integer is not a square. If \(t=2s\), it is \((n+s)^2+(u-s^2)\), strictly between \((n+s)^2\) and \((n+s+1)^2\) once \(n\) is large, since \(u-s^2>0\). If \(t=2s+1\), it is \((n+s)^2+(n+s)+(u-s(s+1))\), again strictly between those consecutive squares for large \(n\). This time \(u-s(s+1)\) is a positive integer, because the negative discriminant implies it exceeds \(1/4\).

The index-\(m\) sublattice \((n+\alpha)L_\tau\) is homothetic to \(L_\tau\). Thus (9.16) gives \(\Psi_m(j(\tau),j(\tau))=0\). The diagonal polynomial has integer coefficients and leading coefficient \(\pm1\) by Proposition 9.12. Its root \(j(\tau)\) is therefore an algebraic integer. \(\square\)

Here **complex multiplication** means that the lattice has a nonreal multiplier \(\alpha\) with \(\alpha L\subseteq L\). Conversely such a multiplier has a degree-two integer characteristic polynomial, and its two lattice equations make the period ratio imaginary quadratic. This proves the usual equivalence with the imaginary quadratic condition, without treating the name as a hypothesis about transcendence.

## 6. Exact singular invariants and a near-integer

For the square lattice, \(g_3=0\), so \(j(i)=1728\). For the triangular lattice, \(g_2=0\), so \(j(e^{2\pi i/3})=0\). Both follow from the rotational symmetries proved in Lesson 8.

For a third exact value the index-two polynomial is

\[
 \begin{aligned}
 \Phi_2(X,Y)={}&X^3+Y^3-X^2Y^2+1488XY(X+Y)\\
 &-162000(X^2+Y^2)+40773375XY\\
 &+8748000000(X+Y)-157464000000000.
 \end{aligned}
 \tag{9.17}
\]

Here is a finite way to verify this formula from the proved construction. The three factors in (9.16) involve \(j(2\tau),j(\tau/2),j((\tau+1)/2)\). Their first, second and third elementary symmetric functions have pole orders at most two, two and three in \(q\). For the second function, the potential half-power leading terms cancel because the latter two series are obtained by opposite square roots of \(q\); their sum has a finite constant term. Lemma 9.11 says that the three coefficients are polynomials in \(j\) of those degree bounds. Their principal parts and constants determine the polynomials uniquely. Series division in (9.14), followed by those three products, gives exactly (9.17). Only finitely many coefficients are needed for this determination; the accompanying exact source calculation compares every nonpositive Laurent coefficient, rather than checking a numerical value of an asserted identity.

Multiplication by \(\sqrt{-2}\) is an index-two endomorphism of \(\mathbb Z\sqrt{-2}+\mathbb Z\). The diagonal specialization factors as

\[
 \Phi_2(X,X)=-(X-8000)(X-1728)(X+3375)^2.
\]

For \(\tau=i\sqrt2\), the positive real parameter \(q=e^{-2\pi\sqrt2}\), the convergent expressions (9.13)–(9.14) place \(j(\tau)\) between 7999 and 8001. Thus the only possible root is

\[
 j(i\sqrt2)=8000.
 \tag{9.18}
\]

We give reproducible rigorous error bounds for this and the following example below; approximate equality alone would not prove either exact value.

### Lemma 9.14. Conjugation and a unique reduced complex multiplication lattice

Let \(\tau_0=(1+i\sqrt{163})/2\). Then \(j(\tau_0)\) is an ordinary integer.

**Proof.** It is an algebraic integer by Theorem 9.13. We show that all its algebraic conjugates are equal by keeping track of the endomorphism ring, rather than assuming a class-number formula.

First consider a normalized lattice \(\mathbb Z\tau+\mathbb Z\) with \(\tau\) imaginary quadratic. Choose its primitive quadratic equation \(a\tau^2+b\tau+c=0\), with \(a>0\) and \(\gcd(a,b,c)=1\). Every lattice multiplier must have the form \(r+s\tau\), \(r,s\in\mathbb Z\), because it sends 1 into the lattice. Its product with \(\tau\) is in the lattice precisely when \(a\mid sb\) and \(a\mid sc\). Bézout applied to \(a,b,c\) shows that this is equivalent to \(a\mid s\). Thus

\[
 \operatorname{End}(L):=\{\alpha\in\mathbb C:\alpha L\subseteq L\}
 =\mathbb Z+\mathbb Z(a\tau),
 \qquad\operatorname{disc}(\operatorname{End})=b^2-4ac.
 \tag{9.19}
\]

The discriminant here is the determinant of the trace pairing on that two-element integer basis; expansion gives \(b^2-4ac\). A ring isomorphism preserves this pairing and its discriminant.

We need to know that algebraic conjugation of the invariants preserves this ring. Scale the lattice to have algebraic invariants \(A,B\), as in Theorem 9.8; scaling does not change its multiplier ring. Its Laurent coefficients at zero are algebraic by (8.22). A multiplier \(\alpha\) has an integer matrix on the lattice, whose degree-two characteristic polynomial vanishes at \(\alpha\); hence every multiplier is algebraic.

For \(\alpha\ne0\), the function \(\wp(\alpha z)\) is even and elliptic under \(L\), so Lemma 9.5 gives a rational presentation \(P(\wp(z))/Q(\wp(z))\). Its coefficients can be chosen algebraic. Indeed both Laurent series \(\wp(z),\wp(\alpha z)\) have algebraic coefficients, and the identity after clearing \(Q\) is a linear system in the finitely many coefficients of \(P,Q\) of the chosen degree bounds. Its row space has a finite basis, all with algebraic entries. A nonzero complex solution therefore gives a nonzero algebraic solution to that finite system, and it satisfies every row of the original system. Its denominator cannot vanish identically: that would force its numerator to vanish as well, since \(\wp\) is transcendental over the constant field. Thus the algebraic solution supplies the rational identity as a Laurent identity and hence as a meromorphic identity.

Apply an automorphism \(\sigma\) of the algebraic closure of \(\mathbb Q\) coefficientwise to this formal identity. Theorem 8.11 supplies the unique lattice \(L^\sigma\) with invariants \(\sigma(A),\sigma(B)\); its Laurent recurrence (8.22) is obtained by applying \(\sigma\) to that of \(L\). Consequently the transported identity says

\[
 \wp_{L^\sigma}(\sigma(\alpha)z)
 =\frac{P^\sigma(\wp_{L^\sigma}(z))}
 {Q^\sigma(\wp_{L^\sigma}(z))}.
\]

Its right side is periodic under \(L^\sigma\). The period group of its left side is exactly \(\sigma(\alpha)^{-1}L^\sigma\): a period preserves its pole set, which is that lattice, and every element of that lattice is a period. Therefore \(\sigma(\alpha)L^\sigma\subseteq L^\sigma\). This gives an injective ring map on multiplier rings, including zero. Applying the same argument to \(L^\sigma\) and \(\sigma^{-1}\), and using uniqueness to recover \(L\), proves surjectivity. Thus the rings are isomorphic and have the same discriminant. The invariant of \(L^\sigma\) is \(\sigma(j(L))\) by its rational coefficient formula. This is a coefficientwise argument in formal Laurent series; it never assumes that a field automorphism is continuous on \(\mathbb C\).

For \(\tau_0\), equation (9.19) gives discriminant \(-163\). Reduce the period ratio of any conjugated model to \(\mathcal F\). Its primitive equation then satisfies

\[
 |b|\leq a\leq c,\qquad 4ac-b^2=163,
 \qquad a\leq\sqrt{163/3}<8.
\]

The first inequalities follow from \(\operatorname{Re}\tau=-b/(2a)\), \(|\tau|^2=c/a\) and the defining inequalities of \(\mathcal F\). Check \(a=1,\ldots,7\), \(|b|\leq a\), requiring \(c=(b^2+163)/(4a)\) to be an integer at least \(a\). The only possibilities are \((a,b,c)=(1,1,41),(1,-1,41)\). Their upper half-plane roots differ by an integer, so have the same \(j\)-value. Consequently every algebraic conjugate of \(j(\tau_0)\) equals itself. Its minimal polynomial over \(\mathbb Q\) is separable in characteristic zero, so has degree one; the invariant is rational. A rational algebraic integer is an integer. \(\square\)

Every conjugate used in this argument is induced by an automorphism of the algebraic closure. For completeness, start with the embedding of the simple field that sends an algebraic number to the chosen conjugate. Enumerate the countable set of algebraic numbers and successively extend the embedding by choosing a root of each transported minimal polynomial. The union is an embedding of the algebraic closure. Its image is algebraically closed: a polynomial in the image has preimage coefficients, a root in the original algebraic closure, and hence a root in the image. Since the whole algebraic closure is algebraic over that image, the image must be the whole field. Thus the embedding is an automorphism. This supplies the extension fact needed for the minimal-polynomial argument.

The standard language calls this the class-number-one case. The proof above includes the small reduced-form enumeration and the needed conjugation argument; it does not infer rationality from an unexplained reference to class field theory.

For \(\tau_0\), \(q=-e^{-\pi\sqrt{163}}\). Evaluation of the convergent Fourier quotient with the bounds below places its invariant within \(1/2\) of \(-640320^3\). Lemma 9.14 therefore determines the integer exactly:

\[
 j\left(\frac{1+i\sqrt{163}}2\right)=-640320^3.
 \tag{9.20}
\]

The nearby positive real number is

\[
 \begin{aligned}
 e^{\pi\sqrt{163}}&=640320^3+744-\delta,\\
 0.0000000000007499274028018
 &<\delta<0.0000000000007499274028019.
 \end{aligned}
 \tag{9.21}
\]

Thus its distance from that integer to three significant digits is \(7.50\times10^{-13}\). It is transcendental: choose \(\log(-1)=i\pi\), and the algebraic irrational exponent \(-i\sqrt{163}\). The fixed-branch Gelfond–Schneider theorem gives \((-1)^{-i\sqrt{163}}=e^{\pi\sqrt{163}}\) transcendental.

**Rigorous bounds for the numerical examples.** These small intervals are obtained with exact rational arithmetic. The identity

\[
 \pi=16\arctan(1/5)-4\arctan(1/239)
\]

follows by the tangent addition formula: its quarter has tangent one and lies in \((0,\pi/2)\). The series \(\arctan t=\sum_{r\geq0}(-1)^rt^{2r+1}/(2r+1)\) follows by integrating the geometric series for \((1+t^2)^{-1}\); truncation has the sign and modulus of at most its first omitted term. Using 150 terms for \(1/5\) and 45 for \(1/239\) gives rational bounds for \(\pi\). Bounds for \(\sqrt2,\sqrt{163}\) are obtained by checking the squares of consecutive rational numbers with denominator \(10^{100}\).

For a positive rational \(x\), truncate \(e^x=\sum x^r/r!\) after \(N\) terms. If \(N+2>x\), its remaining positive tail is at most

\[
 \frac{x^{N+1}}{(N+1)!}\frac1{1-x/(N+2)},
\]

because successive ratios are at most \(x/(N+2)\). The calculation uses \(N=300\), with each intermediate term rounded outwards to denominator \(10^{110}\); inclusion in the resulting rational interval is preserved at every operation. Taking reciprocals bounds each \(q\), with its indicated sign. For the Fourier series, \(\sigma_r(n)\leq n^{r+1}\). If \(s=|q|\), the tail after \(n=N_0\) is at most

\[
 \frac{(N_0+1)^{r+1}s^{N_0+1}}
 {1-s((N_0+2)/(N_0+1))^{r+1}}
\]

when the denominator is positive; this follows by bounding the successive term ratios. Eight Fourier terms suffice here. Rational interval evaluation of (9.14) gives

\[
 \begin{aligned}
 7999.999999999999&<j(i\sqrt2)<8000.000000000001,\\
 -262537412640768000.000000000001
 &<j(\tau_0)<-262537412640767999.999999999999.
 \end{aligned}
\]

These enclosures certify the root selection and integer selection above. They also yield (9.21) directly from the exponential interval. The finite arithmetic supports the stated exact theorems; it does not replace their algebraicity proofs.

## 7. The differential system of the three Eisenstein series

The deeper independence result involves one more series,

\[
 E_2(q)=1-24\sum_{n\geq1}\sigma_1(n)q^n,
 \qquad D=q\frac{d}{dq}=\frac1{2\pi i}\frac{d}{d\tau}.
 \tag{9.22}
\]

We first establish its relation to quasi-periods and the differential system. This also distinguishes an independence assertion about functions from one about their values at a specified argument.

### Proposition 9.15. A quasi-period and the weight-two series

For \(L_\tau=\mathbb Z\tau+\mathbb Z\), with the period-one quasi-period denoted by \(\eta_2\),

\[
 \eta_2(\tau)=\frac{\pi^2}{3}E_2(q).
 \tag{9.23}
\]

For \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbb Z)\),

\[
 E_2(\gamma\tau)=(c\tau+d)^2E_2(\tau)
 +\frac{12}{2\pi i}c(c\tau+d).
 \tag{9.24}
\]

Here \(E_2(\tau)\) denotes the same series evaluated at \(q=e^{2\pi i\tau}\).

**Proof.** Subtract the two absolutely convergent zeta series (8.13) at \(z+1\) and \(z\), and collect lattice terms by their \(\tau\)-coordinate. In each row the reciprocal differences telescope:

\[
 \sum_{n\in\mathbb Z}\left(
 \frac1{z+1-m\tau-n}-\frac1{z-m\tau-n}\right)=0.
\]

The summands in this difference are absolutely summable in the integer direction; the symmetric finite sums telescope to endpoint terms tending to zero. The remaining row term is \(\sum_n(m\tau+n)^{-2}\), with the zero term excluded when \(m=0\). The original combined zeta difference is absolutely summable over the lattice, with tail of order \(|\omega|^{-3}\), so collecting these rows is legitimate. It gives

\[
 \eta_2=\frac{\pi^2}{3}+2\sum_{m\geq1}S_2(m\tau)
 =\frac{\pi^2}{3}-8\pi^2\sum_{m,r\geq1}r q^{mr}.
\]

The exponential row series is absolutely convergent. Collect its divisor coefficients to obtain (9.23).

Scaling gives \(\zeta_{sL}(sz)=s^{-1}\zeta_L(z)\). One may check this directly in the absolutely convergent zeta series; all its terms scale by \(s^{-1}\). Thus \(\eta_{sL}(s\omega)=s^{-1}\eta_L(\omega)\). The period 1 in \(L_{\gamma\tau}=(c\tau+d)^{-1}L_\tau\) corresponds to \(c\tau+d\) in \(L_\tau\). Therefore

\[
 \eta_2(\gamma\tau)=(c\tau+d)(c\eta_1(\tau)+d\eta_2(\tau)).
\]

The Legendre relation is \(\tau\eta_2-\eta_1=2\pi i\), so this becomes \((c\tau+d)^2\eta_2-2\pi i c(c\tau+d)\). Multiply by \(3/\pi^2\) to obtain (9.24). \(\square\)

### Lemma 9.16. The small-weight valence estimate

Suppose \(f\ne0\) is holomorphic on \(\mathfrak H\), holomorphic at \(q=0\), and satisfies

\[
 f(\gamma\tau)=(c\tau+d)^k f(\tau)
\]

for an even nonnegative integer \(k\). If \(n\) is its order at \(q=0\), then \(n\leq k/12\). In particular, for \(k<12\) its constant Fourier coefficient determines the function uniquely within this vector space.

**Proof.** Truncate the reduced region \(\mathcal F\) at imaginary height \(T\), choosing \(T\) large enough that the leading cusp term \(Cq^n\), \(C\ne0\), ensures no zeros above it. Integrate \(f'/f\) on the positively oriented boundary. The vertical sides cancel because \(f(\tau+1)=f(\tau)\). The top, directed from right to left, contributes a limit \(-2\pi i n\) as \(T\to\infty\).

On the unit-circle bottom split at \(i\). Its left half runs clockwise from \(\rho=e^{2\pi i/3}\) to \(i\), and the inversion \(S\tau=-1/\tau\) maps it to the right half with reversed direction. Differentiating \(f(-1/\tau)=\tau^kf(\tau)\) gives

\[
 \frac{f'}f(-1/\tau)\frac1{\tau^2}
 =\frac{k}{\tau}+\frac{f'}f(\tau).
\]

Pair the two arc integrals. Their sum is minus \(k\int_\rho^i d\tau/\tau\), namely \(k\pi i/6\), since the left arc's argument decreases from \(2\pi/3\) to \(\pi/2\). If there are no boundary zeros, the residue theorem now gives the total interior zero multiplicity as \(k/12-n\), a nonnegative number.

Boundary zeros give the same estimate with nonnegative fractional contributions. To see the precise accounting, remove small discs at those zeros, choosing paired pieces under translation and inversion, and integrate on the remaining boundary. For a zero of order \(r\), \(f'/f=r/(\tau-\tau_0)+O(1)\); a removed circular indentation of interior angle \(\theta\), traversed clockwise, contributes \(-ir\theta+o(1)\). The paired modular integrals are unchanged in the limit, since the missing integrals of \(k/\tau\) tend to zero. A zero on an ordinary paired boundary contributes total angle \(2\pi\); the zero at \(i\) has angle \(\pi\); the two identified corners \(\rho,\rho+1\) have total angle \(2\pi/3\). Thus the limiting residue formula is

\[
 n+\frac12\operatorname{ord}_i(f)
 +\frac13\operatorname{ord}_\rho(f)
 +\sum_{\text{other zero classes}}\operatorname{ord}(f)=\frac{k}{12}.
\]

Every term is nonnegative, proving the estimate. If two forms of weight \(k<12\) have the same constant coefficient, their difference has \(n\geq1\), impossible for a nonzero form. Thus their difference is zero. \(\square\)

This proof uses the actual arc orientation and boundary angles. A full cell count without the factors at \(i\) and \(\rho\) would give the wrong bound.

### Theorem 9.17. Ramanujan's differential identities

The convergent series satisfy

\[
 DE_2=\frac{E_2^2-E_4}{12},\qquad
 DE_4=\frac{E_2E_4-E_6}{3},\qquad
 DE_6=\frac{E_2E_6-E_4^2}{2}.
 \tag{9.25}
\]

**Proof.** The lattice scaling law makes \(E_4,E_6\) holomorphic modular forms of weights four and six, respectively, with constant coefficients one. Their product \(E_4^2\) is one of weight eight with constant coefficient one. For a weight-\(k\) form \(f\), differentiating its transformation law and using (9.24) shows that

\[
 Df-\frac{k}{12}E_2f
\]

is a holomorphic form of weight \(k+2\). Indeed the extra derivative term is \(k c(c\tau+d)^{k+1}f/(2\pi i)\), exactly cancelled by the extra term from \(E_2\). Its Fourier expansion has no negative powers. For \(f=E_4\), its constant term is \(-1/3\); by Lemma 9.16 the unique such weight-six form is \(-E_6/3\). For \(f=E_6\), the weight-eight constant is \(-1/2\), giving \(-E_4^2/2\). These are the last two identities.

For the first, differentiate (9.24). If \(t=c\tau+d\) and \(\kappa=12/(2\pi i)\), that identity is \(E_2(\gamma\tau)=t^2E_2+\kappa ct\). Its derivative, multiplied by the chain factor \(t^2\), gives

\[
 (DE_2)(\gamma\tau)=t^4DE_2
 +\frac{2ct^3}{2\pi i}E_2
 +\frac{\kappa c^2t^2}{2\pi i}.
\]

Expanding \(E_2(\gamma\tau)^2\) shows that the extra terms cancel in \(E_2^2-12DE_2\). It is thus a holomorphic form of weight four, with constant term one. Lemma 9.16 makes it \(E_4\), completing the proof. \(\square\)

### Proposition 9.18. Independence of the functions

The functions \(E_2,E_4,E_6\) are algebraically independent over \(\mathbb C\).

**Proof.** First \(E_4,E_6\) are independent. If a polynomial relation between them existed, apply the matrices \(\left(\begin{smallmatrix}1&0\\N&1\end{smallmatrix}\right)\), \(N\in\mathbb Z\). At any fixed \(\tau\), their modular transformations make the relation a polynomial in \(N\tau+1\). Infinitely many distinct such numbers imply that every coefficient, corresponding to a fixed weight \(4b+6c\), is zero. Within such a weight the exponent pairs differ by \((3,-2)\). Away from the discrete zeros of \(E_4E_6\), the weighted relation is a nonzero monomial times a polynomial in \(E_4^3/E_6^2\). This ratio is nonconstant, by (9.14) and the already proved nonconstancy of \(j\). It cannot satisfy a nonzero constant polynomial. Thus all original coefficients are zero.

Now suppose \(P(E_2,E_4,E_6)=0\). At fixed \(\tau\), transformation by every matrix with bottom row \((c,d)\) coprime gives

\[
 P\bigl(t^2E_2+\kappa ct,t^4E_4,t^6E_6\bigr)=0,
 \qquad t=c\tau+d.
\]

This is a polynomial in the formal variables \(c,d\), vanishing for every coprime integer pair. Such pairs are Zariski dense: for each fixed nonzero integer \(c\), infinitely many integers \(d\) are coprime to it, forcing all coefficients as a polynomial in \(d\) to vanish; doing this for infinitely many \(c\) forces the coefficient polynomials in \(c\) to vanish. Thus the displayed polynomial is identically zero for complex \(c,d\).

The invertible linear change \((c,d)\mapsto(c,t)\) permits arbitrary complex \(c\) and \(t\). For \(t\ne0\), the value \(s=E_2+\kappa c/t\) can be any complex number. Hence

\[
 P(t^2s,t^4E_4,t^6E_6)=0\qquad(s\in\mathbb C,\ t\ne0).
\]

The coefficient of each power of \(s\) and each power of \(t\) is a polynomial relation between \(E_4,E_6\), holding for all \(\tau\). Their proved independence forces every coefficient of \(P\) to be zero. This proves the assertion. \(\square\)

### Proposition 9.19. Including the argument as a function

The four functions \(q,E_2(q),E_4(q),E_6(q)\) are algebraically independent over \(\mathbb C\).

**Proof.** Suppose a polynomial relation existed, and write its polynomial as

\[
 A(Z,X_1,X_2,X_3)=\sum_{j=0}^s Z^j A_j(X_1,X_2,X_3).
\]

Fix \(\tau\in\mathfrak H\). Apply the relation at \(\gamma_N\tau=\tau/(N\tau+1)\), where \(\gamma_N=\left(\begin{smallmatrix}1&0\\N&1\end{smallmatrix}\right)\) and \(N\) ranges over positive integers. Put \(u=(N\tau+1)^{-1}\). The transformed relation is

\[
 \sum_j e^{2\pi i j\tau u}
 A_j\left(u^{-2}\left(E_2+\frac\kappa\tau\right)
                 -\frac\kappa\tau u^{-1},
                 u^{-4}E_4,u^{-6}E_6\right)=0,
 \qquad \kappa=\frac{12}{2\pi i}.
 \tag{9.26}
\]

Here the untransformed series values are fixed at \(\tau\). Multiply by a sufficiently large power of \(u\). The left side becomes an entire function of \(u\), a finite sum of polynomials times exponentials. The infinitely many distinct \(u=(N\tau+1)^{-1}\) tend to zero, so its Taylor expansion, or the identity theorem following from that expansion, makes it identically zero.

For any nonzero complex \(a\), the functions \(e^{ja u}\), for distinct nonnegative integers \(j\), are independent over \(\mathbb C(u)\). Indeed, clear denominators in a proposed relation to get \(\sum p_j(u)e^{ja u}=0\). On the ray \(u=t/a\), \(t>0\), divide by the exponential with largest index. Every other term tends to zero exponentially times a polynomial. The remaining polynomial \(p_s(t/a)\) could tend to zero only if it were zero. Descending on the largest index proves all \(p_j=0\).

Use this with \(a=2\pi i\tau\ne0\) in (9.26). Each Laurent-polynomial coefficient must vanish. Evaluating it at \(u=1\) gives

\[
 A_j(E_2(\tau),E_4(\tau),E_6(\tau))=0.
\]

This holds for every \(\tau\), so Proposition 9.18 makes each \(A_j\) zero. The proposed relation was therefore zero, proving the assertion. \(\square\)

Function independence ensures that a nonzero polynomial in these four functions has a finite order of vanishing. Independence of their values at one fixed argument is a further arithmetic statement. We next construct the integer polynomials and prove both bounds on their nonzero values; the multiplicity estimate will control their remaining parameter.

## 8. Integer auxiliary functions and a nonzero derivative

Fix \(q\) with \(0<|q|<1\), and choose a real \(r\) with \(|q|<r<1\). Throughout this section constants may depend on \(q,r\), but not on the positive integer \(N\). The norm \(H(A)\) is the maximum absolute value of a polynomial's coefficients; \(\|A\|_1\) is their sum. For a holomorphic function, \(|F|_r=\max_{|z|=r}|F(z)|\).

### Lemma 9.20. Interpolation with one repeated point

Let \(F\) be holomorphic in a neighbourhood of \(|z|\leq r\), with a zero of exact order \(M\) at zero, and write \(F(z)=f_Mz^M+\cdots\). For every integer \(L\geq1\),

\[
 r^M|f_M|\leq
 \left(\frac{|q|}{r}\right)^L|F|_r
 +2^{M+L}\left(\frac r{|q|}\right)^M
 \sum_{\ell=0}^{L-1}\left(\frac{|q|}{2}\right)^\ell
                         \frac{|F^{(\ell)}(q)|}{\ell!}.
 \tag{9.27}
\]

**Proof.** The factor

\[
 B(z)=\frac{r(z-q)}{r^2-\overline qz}
\]

has modulus one on \(|z|=r\), because \(|r^2-\overline qz|=r|z-q|\) there. Integrate \(F(z)B(z)^{-L}z^{-M-1}\) on that circle. Its residue at zero is \(f_MB(0)^{-L}\), of modulus \(|f_M|(r/|q|)^L\); the contour integral divided by \(2\pi i\) has modulus at most \(|F|_r/r^M\). The only other pole is at \(q\). Its residue is

\[
 \sum_{\ell<L}\frac{F^{(\ell)}(q)}{\ell!}
 [t^{L-1-\ell}]\,
 \frac{(r^2-\overline q(q+t))^L}{r^L(q+t)^{M+1}},
\]

where \([t^j]\) denotes the Taylor coefficient. On \(|t|=|q|/2\), the numerator's base has modulus at most \(r^2-|q|^2/2\leq r^2\), while \(|q+t|\geq|q|/2\). Cauchy's coefficient bound therefore bounds the coefficient in this sum by

\[
 r^L\left(\frac2{|q|}\right)^{M+L-\ell}.
\]

The residue theorem and triangle inequality, multiplied by \(r^M(|q|/r)^L\), give exactly (9.27). The coefficient estimate uses only the displayed rational function, which is analytic on \(|t|\leq|q|/2\); that circle need not lie in the disc on which \(F\) is being estimated. \(\square\)

### Proposition 9.21. Many initial zeros with small integer coefficients

For every sufficiently large \(N\) there is a nonzero
\(A_N\in\mathbb Z[Z,X_1,X_2,X_3]\), of degree at most \(N\) in each variable, such that

\[
 \log H(A_N)\leq C N\log N,
 \qquad F_N(z)=A_N(z,E_2(z),E_4(z),E_6(z))
\]

has an exact, finite order \(M=M_N\) at zero satisfying

\[
 M\geq \left\lfloor\frac{(N+1)^4}{2}\right\rfloor
 \geq\frac{N^4}{2},\qquad
 |F_N|_r\leq r^M M^{C_rN}.
 \tag{9.28}
\]

**Proof.** All three series have integer coefficients. Since a positive integer \(n\) has at most \(n\) divisors,
\(\sigma_k(n)\leq n^{k+1}\). Thus every coefficient of any one of the three series is bounded in absolute value by \(504(n+1)^6\), including its constant term. In a product of at most \(3N\) factors, each coefficient of degree \(n\) is consequently bounded by

\[
 U_n=504^{3N}(n+1)^{21N}.
 \tag{9.29}
\]

For a product with \(s\geq1\) factors, there are at most \((n+1)^{s-1}\) compositions of \(n\) into their nonnegative degrees, and each product of coefficients is at most \(504^s(n+1)^{6s}\). This proves (9.29); the empty product also satisfies it. Multiplication by \(z^a\), \(a\geq0\), cannot increase the bound.

There are \(D_N=(N+1)^4\) unknown coefficients of \(A_N\). Impose vanishing of the first \(\nu=\lfloor D_N/2\rfloor\) Taylor coefficients of \(F_N\). This is an integer homogeneous system with \(\nu\) rows. Each entry has absolute value at most
\(U=504^{3N}(\nu+1)^{21N}\). The box proof of Siegel's lemma, Lemma 5.1, gives a nonzero integer vector with

\[
 H(A_N)\leq(D_NU)^{\nu/(D_N-\nu)}\leq D_NU.
\]

The exponent is at most one. Since \(\nu+1\leq (N+1)^4\) for \(N\geq1\), the logarithm of this bound is \(O(N\log N)\). Proposition 9.19 proves that the resulting \(F_N\) is not identically zero, so \(M\) is finite and at least \(\nu\). Its leading coefficient \(f_M\) is a nonzero integer, hence \(|f_M|\geq1\).

For every \(n\), its Taylor coefficient satisfies

\[
 |f_n|\leq D_N H(A_N)504^{3N}(n+1)^{21N}.
\]

Let \(s=(1+r)/2<1\). For all sufficiently large \(N\) and every \(n\geq M\),

\[
 r\left(\frac{n+2}{n+1}\right)^{21N}
 \leq r\exp\left(\frac{21N}{M+1}\right)\leq s,
\]

because \(M\geq N^4/2\). The tail of the absolute Taylor series on the circle is therefore at most

\[
 \frac{D_NH(A_N)504^{3N}}{1-s}
 (M+1)^{21N}r^M.
\]

Taking logarithms, using \(\log N=O(\log M)\) and \(M+1\leq2M\), absorbs every factor before \(r^M\) into \(M^{C_rN}\). This proves (9.28). \(\square\)

### Proposition 9.22. Two bounds at the chosen argument

For the same \(M=M_N\), there is an integer polynomial \(B_N\) such that

\[
 \deg B_N\leq C N\log M,\qquad
 \log H(B_N)\leq C N(\log M)^2,
\]

and, for fixed positive \(c_1,c_2\),

\[
 e^{-c_2M}\leq
 |B_N(q,E_2(q),E_4(q),E_6(q))|
 \leq e^{-c_1M}.
 \tag{9.30}
\]

**Proof.** Take

\[
 L=1+\left\lceil
 \frac{C_rN\log M+\log2}{\log(r/|q|)}
 \right\rceil.
\]

The first term on the right of (9.27), with \(F=F_N\), is at most \(r^M/2\). Since \(|f_M|\geq1\), at least one \(T<L\) satisfies

\[
 \left(\frac{|q|}{2}\right)^T
 \frac{|F_N^{(T)}(q)|}{T!}
 \geq\frac{|q|^M}{L2^{M+L+1}}.
 \tag{9.31}
\]

In particular that derivative is nonzero. We have \(L=O(N\log M)\) and, by \(N\leq(2M)^{1/4}\), both \(L\) and \(N(\log M)^2\) are \(o(M)\). As \(T!(2/|q|)^T\geq1\), (9.31) gives
\(\log|F_N^{(T)}(q)|\geq-CM\).

For the upper bound take \(\delta=(r-|q|)/2>0\). The circle of radius \(\delta\) about \(q\) lies inside \(|z|<r\). Cauchy's derivative bound and (9.28) give

\[
 \log|F_N^{(T)}(q)|
 \leq M\log r+C_rN\log M+\log(T!)+T\log(1/\delta)
 \leq M\log r+O(N(\log M)^2).
\]

Here \(\log(T!)\leq T\log\max(1,T)\), and
\(\log\max(1,T)=O(\log M)\). Since \(\log r<0\), the bound is at most \(\tfrac12M\log r\) for all sufficiently large \(N\).

Introduce the polynomial derivation

\[
 \mathcal D=Z\partial_Z
 +\frac{X_1^2-X_2}{12}\partial_{X_1}
 +\frac{X_1X_2-X_3}{3}\partial_{X_2}
 +\frac{X_1X_3-X_2^2}{2}\partial_{X_3}.
\]

Theorem 9.17 and the chain rule identify its evaluation on the four functions with \(z\,d/dz\). For an integer \(T\geq0\), induction gives

\[
 z^T F_N^{(T)}(z)
 =\left[\prod_{k=0}^{T-1}(\mathcal D-k)A_N\right]
 (z,E_2(z),E_4(z),E_6(z)).
\]

For the induction, \((z\,d/dz-T)(z^TF^{(T)})=z^{T+1}F^{(T+1)}\). Define

\[
 B_N=\prod_{k=0}^{T-1}12(\mathcal D-k)A_N;
\]

the empty product means \(B_N=A_N\) when \(T=0\). Each factor has integer polynomial coefficients, so \(B_N\) is an integer polynomial. Its evaluated value is \(12^Tq^TF_N^{(T)}(q)\). The logarithm of the prefactor's modulus is \(O(T)=o(M)\); it preserves the two bounds (9.30), after adjusting fixed positive constants.

For completeness, each application of \(\mathcal D-k\) increases total degree by at most one, and does not increase degree in \(Z\). Thus \(\deg B_N\leq4N+T\). If \(U\) has total degree \(d\), the displayed derivation gives

\[
 \|12(\mathcal D-k)U\|_1\leq12(d+k)\|U\|_1.
\]

Indeed on a monomial with exponents \((a,b,c,d')\), the coefficient sum from \(12\mathcal D\) is at most \(12a+2b+8c+12d'\leq12d\), and the constant term adds \(12k\). Consequently

\[
 \log H(B_N)\leq\log\|A_N\|_1
 +T\log\bigl(12(4N+2T)\bigr)
 =O(N(\log M)^2).
\]

The polynomial is nonzero because its value is nonzero. This proves all assertions. \(\square\)

These estimates explain the need for a multiplicity bound of order \(N^4\). With \(M_N\leq C N^4\), (9.30) gives small nonzero values on the scale \(N^4\), while polynomial degree and log height cost only \(O(N(\log N)^2)\). To prove that bound, we first study the invariant algebraic sets of the displayed derivation. An ideal is **stable under a derivation** if applying the derivation to any of its elements gives another element of the ideal.

## 9. Invariant prime ideals of the modular differential system

Write \(P=X_1,Q=X_2,R=X_3\) in this section, and assign them weights \(1,2,3\), respectively; give \(Z\) weight zero. These are half the usual modular weights. The discriminant polynomial

\[
 \Delta=Q^3-R^2
\]

satisfies \(\mathcal D\Delta=P\Delta\). Its value on the series begins \(1728z+O(z^2)\) and never vanishes when \(0<|z|<1\), by the nonsingularity of the lattice cubic proved in Lesson 8. The derivation on \(\mathbb C[P,Q,R]\), obtained by omitting \(Z\partial_Z\), will be denoted by \(\delta\).

### Lemma 9.23. The irreducible stable hypersurfaces

If a nonconstant irreducible \(A\in\mathbb C[Z,P,Q,R]\) has
\(\mathcal DA\in(A)\), then \(A\) is a nonzero constant multiple of either \(Z\) or \(\Delta\).

**Proof.** Write \(\mathcal DA=BA\). Degree in \(Z\) cannot increase under \(\mathcal D\), and weight can increase by at most one. Degrees and maximum weights add under multiplication of nonzero polynomials. If \(\mathcal DA\ne0\), these observations make \(B=aP+b\) for constants \(a,b\). If \(\mathcal DA=0\), take \(a=b=0\); the same argument below also deals with that case.

By Proposition 9.19,
\(F(z)=A(z,E_2(z),E_4(z),E_6(z))\) is not identically zero. Its differential equation is

\[
 zF'(z)=(aE_2(z)+b)F(z).
\]

If its exact order at zero is \(m\), comparison of the leading coefficients gives \(m=a+b\in\mathbb Z_{\geq0}\). On the interval \(0<z<1\), the discriminant value is positive: it is real, has positive leading term, and has no zero. Comparing logarithmic derivatives, using \(z\Delta'(z)=E_2(z)\Delta(z)\), therefore gives

\[
 F(z)=C z^b\Delta(z)^a,
 \qquad C\ne0,
 \tag{9.32}
\]

where the powers on this real interval use real logarithms. This comparison also proves that \(F\) has no zero on the interval.

We determine \(a\) at the other cusp. Put \(z=e^{-2\pi t}\), \(u=e^{-2\pi/t}\), with \(t>0\). The transformation laws proved above give

\[
 E_2(z)=-t^{-2}E_2(u)+\frac6{\pi t},\qquad
 E_4(z)=t^{-4}E_4(u),\qquad E_6(z)=-t^{-6}E_6(u),
\]

and
\(\Delta(z)=t^{-12}\Delta(u)=1728t^{-12}u(1+O(u))\).
After multiplying \(F(e^{-2\pi t})\) by some integer power \(t^K\), the polynomial expression for \(F\) has an expansion

\[
 t^KF(e^{-2\pi t})=\sum_{n\geq0}h_n(t)u^n.
\]

Each \(h_n\) is holomorphic near \(t=0\): it is a finite linear combination of powers of \(t\) and \(e^{-2\pi t}\). On a fixed small complex disc its modulus is at most \(C(n+1)^C\). This last bound follows by the coefficient convolution estimate (9.29), with the number of factors now fixed by \(A\). Some \(h_n\) is not identically zero, since otherwise \(F\) would vanish for all small positive \(t\). Let \(n_0\) be the least such index and let its zero order at \(t=0\) be \(s\). The uniform polynomial coefficient bound makes the later terms exponentially smaller, so

\[
 F(e^{-2\pi t})=C_0t^{s-K}e^{-2\pi n_0/t}(1+o(1)),
 \qquad C_0\ne0.
\]

On the other hand (9.32) makes this
\(C_1t^{-12a}e^{-2\pi a/t}(1+o(1))\), with \(C_1\ne0\). Comparison of absolute values first gives \(\operatorname{Re}a=n_0\), since exponential decay cannot be balanced by a power of \(t\); it then gives \(s-K=-12n_0\). If \(\operatorname{Im}a\ne0\), the quotient of the two leading expressions has phase
\(12\operatorname{Im}a\log t+2\pi\operatorname{Im}a/t\), up to a fixed constant. This phase is monotone and unbounded for all sufficiently small \(t>0\), and hence has sequences approaching zero on which its exponential is respectively \(1\) and \(-1\). It cannot have the required nonzero limit. Thus \(a=n_0\) is a nonnegative integer, and \(b=m-a\) is an integer.

The rational function \(S=A/(Z^b\Delta^a)\) now satisfies \(\mathcal DS=0\). Its value on the four functions is constant on a real interval. After clearing denominators, the identity theorem and Proposition 9.19 make \(S\) constant as a rational function. Therefore
\(A=CZ^b\Delta^a\). Since \(A\) is a polynomial and \(Z\) does not divide \(\Delta\), we must have \(b\geq0\). Finally \(\Delta=Q^3-R^2\) is irreducible: over \(\mathbb C(Q)\) the element \(Q^3\) is not a square, its order at \(Q=0\) being odd, so the quadratic in \(R\) is irreducible; its primitive coefficients preserve irreducibility on adjoining \(P,Z\). Irreducibility of \(A\) therefore leaves exactly \(A=CZ\) or \(A=C\Delta\). \(\square\)

### Lemma 9.24. A homogeneous polynomial in a nonprincipal prime

If a nonzero prime ideal \(\mathfrak q\subset\mathbb C[P,Q,R]\) is not principal, then it contains a nonzero weighted homogeneous polynomial. The ideal \(\widetilde{\mathfrak q}\) generated by all its weighted homogeneous elements is prime. If \(\mathfrak q\) is \(\delta\)-stable, so is \(\widetilde{\mathfrak q}\).

**Proof.** Choose an irreducible polynomial \(A\in\mathfrak q\), by factoring a nonzero element and using primality. Since \(\mathfrak q\ne(A)\), choose \(B\in\mathfrak q\) not divisible by \(A\). They are relatively prime. If either is weighted homogeneous, the first assertion is immediate. Otherwise consider

\[
 a(T)=T^{-\mu}A(TP,T^2Q,T^3R),\qquad
 b(T)=T^{-\nu}B(TP,T^2Q,T^3R),
\]

where \(\mu,\nu\) are their minimum weights. These are nonconstant polynomials in \(T\) with nonzero constant coefficients in \(\mathbb C[P,Q,R]\). They are relatively prime over \(\mathbb C(P,Q,R)[T]\). To verify this, a common nonconstant factor there would, on clearing primitive coefficients, give a common factor in \(\mathbb C[P,Q,R,T]\) other than \(T\). Localize at \(T\). The substitution \((P,Q,R)\mapsto(TP,T^2Q,T^3R)\) is an automorphism of that Laurent polynomial ring and preserves the relatively prime pair \(A,B\), a contradiction.

Their Sylvester resultant \(H(P,Q,R)=\operatorname{Res}_T(a,b)\) is consequently nonzero. The determinant criterion used here follows directly from the map
\((U,V)\mapsto Ua+Vb\), with \(\deg U<\deg b\), \(\deg V<\deg a\): it has zero determinant precisely when a nonzero such pair gives \(Ua+Vb=0\), which is equivalent to a common factor over the coefficient field. Modulo \(\mathfrak q\), both \(a,b\) vanish at \(T=1\). Their resultant is therefore zero in that domain, so \(H\in\mathfrak q\). This also follows by specializing the Sylvester determinant, whose rows then have the common evaluation functional at 1 in their kernel.

Let \(p=\deg_Ta\), \(q'=\deg_Tb\). Weighted scaling by a nonzero \(\lambda\) changes \(a(T)\) to \(\lambda^\mu a(\lambda T)\), and \(b(T)\) to \(\lambda^\nu b(\lambda T)\). The determinant, or its product over roots, makes their resultant scale by
\(\lambda^{\mu q'+\nu p+pq'}\). Thus \(H\) is weighted homogeneous, proving the first assertion.

The homogeneous elements of \(\mathfrak q\) are exactly the homogeneous elements of \(\widetilde{\mathfrak q}\): one inclusion follows from its definition, the other from \(\widetilde{\mathfrak q}\subseteq\mathfrak q\). For homogeneous \(U,V\), a product \(UV\) in this ideal forces one factor into \(\mathfrak q\), hence into \(\widetilde{\mathfrak q}\). This homogeneous test proves primality for arbitrary polynomials too: modulo the homogeneous ideal, take the largest-weight nonzero component of each factor. Their product is the largest-weight component of the product and is nonzero by the homogeneous test. Finally \(\delta\) increases weight by one; the derivative of every homogeneous generator is again a homogeneous element of \(\mathfrak q\). The Leibniz rule proves stability of the generated ideal. \(\square\)

### Theorem 9.25. The discriminant in every invariant prime

Every nonzero \(\mathcal D\)-stable prime ideal
\(\mathfrak p\subset\mathbb C[Z,P,Q,R]\) with
\(\mathfrak p\cap\mathbb C[Z]=(0)\) contains \(\Delta\).

**Proof.** First consider a nonzero \(\delta\)-stable prime
\(\mathfrak q\subset\mathbb C[P,Q,R]\). If it is principal, its irreducible generator also generates a prime ideal in the larger ring. Lemma 9.23 makes that generator \(\Delta\), since it cannot be \(Z\). If it is not principal, Lemma 9.24 gives a nonzero homogeneous stable prime
\(\mathfrak h=\widetilde{\mathfrak q}\subseteq\mathfrak q\). We show that \(\Delta\in\mathfrak h\).

If \(\mathfrak h\cap\mathbb C[Q]\ne0\), homogeneity and primality imply \(Q\in\mathfrak h\); then \(\delta Q=(PQ-R)/3\) gives \(R\in\mathfrak h\), and hence \(\Delta\in\mathfrak h\). Suppose this intersection is zero but \(\mathfrak h\cap\mathbb C[Q,R]\ne0\). Choose a nonzero homogeneous \(A(Q,R)\) in the intersection with the least possible degree in \(R\), and let its weight be \(w\). That degree is positive, since there is no polynomial in \(Q\) alone. The weighted Euler identity is

\[
 2Q A_Q+3R A_R=wA.
\]

It gives the following polynomial identity by substitution of \(\delta Q,\delta R\):

\[
 wA\,\delta Q-2Q\,\delta A=(Q^3-R^2)A_R=\Delta A_R.
 \tag{9.33}
\]

The left side belongs to \(\mathfrak h\). The nonzero derivative \(A_R\), which has smaller \(R\)-degree, does not belong to \(\mathfrak h\), by minimality. Primality forces \(\Delta\in\mathfrak h\).

The remaining possibility, \(\mathfrak h\cap\mathbb C[Q,R]=0\), is impossible. Localize at the nonzero polynomials in \(Q,R\). The extension of \(\mathfrak h\) is a nonzero prime in the one-variable polynomial ring \(\mathbb C(Q,R)[P]\), and is generated by an irreducible polynomial. Clear its primitive denominators to get an irreducible \(A\in\mathbb C[Q,R][P]\). Its contraction is exactly \((A)\): if a polynomial is divisible by \(A\) after localization, multiply by a denominator in \(\mathbb C[Q,R]\); since the irreducible \(A\) has positive \(P\)-degree, it divides the original polynomial already. Thus \(\mathfrak h=(A)\), and Lemma 9.23 forces \(A\) to be \(\Delta\). This contradicts the assumed zero intersection with \(\mathbb C[Q,R]\). We have proved that every nonzero stable \(\mathfrak q\) contains \(\Delta\).

Now put \(\mathfrak q=\mathfrak p\cap\mathbb C[P,Q,R]\). It is prime and \(\delta\)-stable. If nonzero, the result just proved gives \(\Delta\in\mathfrak p\). If zero, localize at the nonzero elements of \(\mathbb C[P,Q,R]\). As in the preceding paragraph, the nonzero extended prime in \(\mathbb C(P,Q,R)[Z]\) has principal contraction \(\mathfrak p=(A)\) with \(A\) irreducible. Lemma 9.23 then makes \(\mathfrak p=(Z)\) or \((\Delta)\). The first violates \(\mathfrak p\cap\mathbb C[Z]=0\); the second violates \(\mathfrak q=0\). This rules out the last case and proves the theorem. \(\square\)

Consequently every prime in Theorem 9.25 contains a polynomial whose value on the four functions has order exactly one at zero. This is the **D-property** needed for the multiplicity argument, with constant one: no nonzero invariant prime disjoint from \(\mathbb C[Z]\) can have all its polynomial values vanish to arbitrarily high order. The preceding proof fills the stable-hypersurface and homogeneous-ideal steps, rather than treating either as a classification quoted from a source. The use of homogeneous ideals follows Pellarin's simplification described in Bosser, Remark 4.30.

The remaining geometric task is to turn this property into a bound for every polynomial, including polynomials whose zero sets are not invariant. We do this by successive proper intersections.

## 10. Bounding the order of an auxiliary function

We give the degree argument in an affine space \(\mathbb C^n\). A positive **cycle** is a finite sum \(\sum m_i[V_i]\), with \(m_i\) positive integers and \(V_i\) irreducible subvarieties of a common dimension. Its degree is \(\sum m_i\deg V_i\), where the degree of a variety is the number of points, with intersection multiplicities, in a general complementary linear section of its projective closure. Proper intersection with a degree-\(d\) polynomial, followed by discarding components at infinity, has degree at most \(d\) times the original degree. Local multiplicities at a point are nonnegative and at most this degree.

The exact open geometric inputs are the Stacks Project's [degrees and numerical intersections](https://stacks.math.columbia.edu/tag/0BFI), [additivity of the first Chern class](https://stacks.math.columbia.edu/tag/02SP), and [the cycle of an effective Cartier divisor](https://stacks.math.columbia.edu/tag/02SQ). They supply the stated degree rule for \(\mathcal O(d)\). Its [local complete-intersection formula](https://stacks.math.columbia.edu/tag/0B04) and [hypersurface length formula](https://stacks.math.columbia.edu/tag/0B05) give the multiplicities of the proper intersections. We use the linked author proofs, available under the GNU Free Documentation License 1.2 or later, rather than reproduce their text. The local formulas are formulas in regular local rings and apply to the formal neighbourhoods used below, by the same Koszul complexes.

### Lemma 9.26. Degree and polynomials of small degree

For a reduced affine variety \(V\subseteq\mathbb C^n\) of pure dimension \(k\), the vector space of restrictions to \(V\) of polynomials of degree at most \(t\) has dimension at most

\[
 \deg(V)(t+1)^k.
 \tag{9.34}
\]

In particular, if a prime ideal of codimension \(i\) contains no nonzero polynomial of degree less than \(d\), its variety has degree at least \(d^i/n!\).

**Proof.** We construct an injective evaluation map on at most \(\deg(V)(t+1)^k\) points. For \(k=0\), use all its \(\deg(V)\) points. For \(k>0\), choose \(t+1\) distinct general parallel affine hyperplanes. Their projective sections have degree \(\deg(V)\) and have reduced top-dimensional components; none of those components lies at infinity. Such choices exist: on each irreducible component the smooth locus is dense, the singular locus has smaller dimension, and a general hyperplane meets that smooth locus smoothly. The exact latter input is the open [Bertini lemma](https://stacks.math.columbia.edu/tag/0FD6), applied to the smooth locus with its projective immersion. A general hyperplane also meets the singular locus and the hyperplane at infinity properly, so neither can contain a top-dimensional section component. Finitely many choices preserve these properties. Distinct members of the parallel family have no common section component of dimension \(k-1\).

Apply induction to each reduced section, and take the union of its evaluation points. The number of points is at most \((t+1)\deg(V)(t+1)^{k-1}\). If a polynomial of degree at most \(t\) vanishes at all these points, induction makes it vanish on every section component. Suppose it did not vanish on an irreducible component \(W\) of \(V\). Its effective divisor on \(W\) would then contain the \(t+1\) disjoint sets of hyperplane section components, of total degree \((t+1)\deg(W)\). But the degree rule bounds that divisor's degree by \(t\deg(W)\). This is impossible. It must vanish on every \(W\), proving injectivity and (9.34).

For the last assertion, restriction of polynomials of degree at most \(d-1\) is injective. Their dimension is \(\binom{d-1+n}{n}\geq d^n/n!\), whereas (9.34) bounds it by \(\deg(V)d^{n-i}\). Rearranging gives the assertion. \(\square\)

### Lemma 9.27. Leaving a noninvariant variety

Let \(\xi\) be a polynomial derivation whose coefficient degrees are at most \(\delta\), and put \(s=\max(0,\delta-1)\). There is a constant \(K=K(n,\delta)\) with the following property. If an irreducible variety \(V\) is not contained in any proper \(\xi\)-invariant variety, and \(E\) has the least positive degree \(d\) among its nonzero vanishing polynomials, then for some \(N\leq K\),

\[
 E,\xi E,\ldots,\xi^{N-1}E\in I(V),
 \qquad \xi^NE\notin I(V),
 \qquad \deg(\xi^NE)\leq d+sK.
 \tag{9.35}
\]

**Proof.** First some iterate leaves \(\mathfrak p=I(V)\). Otherwise the nonzero ideal generated by all iterates is stable and contained in \(\mathfrak p\). Every minimal prime of a stable ideal in characteristic zero is stable. To verify this, take a primary decomposition and a minimal prime \(\mathfrak q\). For \(a\in\mathfrak q\), choose an exponent \(e\) and an element \(b\notin\mathfrak q\), belonging to every other primary component, so that \(a^eb\) belongs to the ideal. The Leibniz rule gives
\(\xi^e(a^eb)=e!(\xi a)^eb+ab'\). Stability puts this expression in \(\mathfrak q\), so primality makes \(\xi a\in\mathfrak q\). A minimal prime contained in \(\mathfrak p\) would thus define a proper invariant variety containing \(V\), a contradiction.

Let \(N\) be the first escaping index. Work in the regular local ring \(\mathcal R=\mathbb C[x_1,\ldots,x_n]_{\mathfrak p}\), and put
\(J_j=(E,\xi E,\ldots,\xi^jE)\mathcal R\).
The ideals before \(J_N=\mathcal R\) are proper. Their heights begin at one and increase by at most one per step. Adjoining one element of the maximal ideal decreases the quotient dimension by at most one, by the open [one-equation dimension lemma](https://stacks.math.columbia.edu/tag/00KW); the [dimension and height formula](https://stacks.math.columbia.edu/tag/00OR), after localization at \(\mathfrak p\), converts this into the height assertion. For each height \(i\) attained, let \(n_i\) be its first index and let \(n_{i+1}\) be the first next-height index, or \(N\) at the final height. Put \(a_i=n_{i+1}-n_i\geq1\); in particular \(n_1=0\). There are at most \(n\) such heights.

Choose successively polynomials \(E_i\) in the span of \(E,\ldots,\xi^{n_i}E\), with \(E_1=E\), such that \((E_1,\ldots,E_i)\mathcal R\) has height \(i\). At a step, the previous complete intersection has finitely many minimal primes in \(\mathcal R\); the height of \(J_{n_i}\) ensures its generators are not all in any of them. A general complex linear combination avoids their finite union. We have \(\deg E_i\leq d+sn_i\).

These are regular sequences in \(\mathcal R\). The exact algebraic facts used are that a regular local ring is [Cohen–Macaulay](https://stacks.math.columbia.edu/tag/00NQ), that a [sequence giving the full dimension drop is regular](https://stacks.math.columbia.edu/tag/00N6), and that a Cohen–Macaulay module has [only minimal associated primes of its dimension](https://stacks.math.columbia.edu/tag/0BUS). For this sequence, avoidance of those minimal associated primes makes each next element a nonzerodivisor; quotienting decreases both dimension and depth by one. Contract the resulting complete-intersection ideals to the polynomial ring, calling them \(A_i\). Their associated primes all have codimension \(i\) and are contained in \(\mathfrak p\). The degree rule and the local hypersurface length formula give

\[
 \deg Z(A_i)\leq\prod_{j=1}^i(d+sn_j).
 \tag{9.36}
\]

Indeed, intersect the preceding cycle properly with \(E_i\), then discard the primary components whose primes are not contained in \(\mathfrak p\). Localization and contraction preserve the lengths of the retained components, so discarding can only decrease degree.

Choose a minimal prime \(\mathfrak q\subseteq\mathfrak p\) of \(J_{n_{i+1}-1}\) of height \(i\). It is also a minimal prime of \(A_i\). In the local ring at \(\mathfrak q\), the ideals from \(A_i\) through \(J_{n_i},\ldots,J_{n_{i+1}-1}\) give at least \(a_i\) units of length. Each intermediate inclusion \(J_j\subsetneq J_{j+1}\) after localization is strict: equality would make that localized ideal stable under \(\xi\), by the quotient rule on denominators and the consecutive derivative generators. Its contraction, contained in \(\mathfrak q\subseteq\mathfrak p\), would contain every iterate of \(E\), contradicting escape. The final quotient by the maximal ideal has length at least one. Thus the primary multiplicity \(\ell\) of \(\mathfrak q\) in \(A_i\) is at least \(a_i\).

Every polynomial in \(\mathfrak q\) belongs to \(\mathfrak p\), so Lemma 9.26 makes \(\deg Z(\mathfrak q)\geq d^i/n!\). Combining this with (9.36) gives

\[
 a_i\leq\ell\leq n!\prod_{j=1}^i(1+sn_j/d)
                    \leq n!\prod_{j=1}^i(1+sn_j).
\]

Define integers \(b_1=0\) and
\(b_{i+1}=b_i+n!\prod_{j=1}^i(1+sb_j)\).
Induction gives \(n_i\leq b_i\) and hence \(N\leq b_{n+1}\). Take \(K=b_{n+1}\), depending only on \(n,\delta\). Iteration increases degree by at most \(s\) each time, proving the final degree bound. \(\square\)

### Lemma 9.28. Local intersections along a trajectory

Let \(\gamma\) be a smooth formal curve through \(p\), invariant under a regular derivation \(\xi\). Choose formal coordinates \((t,y_2,\ldots,y_n)\) making it the axis \(y=0\). If \(V\) is an irreducible germ not containing \(\gamma\), define \(m_\gamma(V)\) as its intersection multiplicity with general complementary linear sections containing that axis, in these coordinates. For \(\dim V=k\), use \(k\) such hyperplanes. Write \(m_p(V)\) for its ordinary multiplicity, obtained with unrestricted general complementary sections. Extend both functions to cycles by addition.

If \(f\) vanishes on \(V\) but \(g=\xi f\) does not, then

\[
 m_\gamma(V)\leq m_p(V)+m_\gamma(V\cdot Z(g)).
 \tag{9.37}
\]

When \(\xi(p)=0\), the \(m_p(V)\) term can be omitted. Also, if \(f\) vanishes on \(V\) and has order \(c\) on \(\gamma\), then \(m_\gamma(V)\leq c\,m_p(V)\). For a hypersurface defined by \(F\), its multiplicity along \(\gamma\) is exactly the order of \(F|_\gamma\).

**Proof.** Intersect \(V\) with \(k-1\) general hyperplanes containing the axis, obtaining a curve cycle \(C\). The open [associativity formula for proper intersections](https://stacks.math.columbia.edu/tag/0B1L) lets us compute either side by further intersection of \(C\): all pairwise and total intersections have the expected dimensions, and the local Tor calculation applies in the completed regular local ring. Choose a general coordinate \(t\), transverse to its tangent cone and nonzero on the axis tangent. The branch calculation is formal: the normalization of a one-dimensional complete reduced local ring is finite, by the open [complete local Nagata theorem](https://stacks.math.columbia.edu/tag/032W); its local normal factors are [discrete valuation rings](https://stacks.math.columbia.edu/tag/00PD), and their completions with residue field \(\mathbb C\) are [power series rings \(\mathbb C[[s]]\)](https://stacks.math.columbia.edu/tag/0C0S). On a branch \(t=s^e v(s)\), with \(v(0)\ne0\), take the formal \(e\)-th root of the unit and change its parameter to make \(t=s^e\). Its \(e\) Puiseux determinations express the other coordinates as \(y_j=\phi_j(t)\) with rational orders at least one. Include these determinations with the curve cycle's assigned multiplicities. Their total number is \(\mu=m_p(C)=m_p(V)\).

The local length formula gives the order of intersection of \(C\) with a function \(h\) as the sum of \(\operatorname{ord}_t h(t,\phi(t))\) over these determinations. One may compute this after finite normalization: the quotient between the curve ring and its normalization has finite length, and multiplication by a nonzero \(h\) has equal kernel and cokernel lengths on that finite-length quotient, so the intersection length is unchanged. In a branch, taking the norm from \(\mathbb C((s))\) to \(\mathbb C((t))\) sums precisely the orders of its Puiseux determinations. A general linear combination of the \(y_j\) on a branch has order
\(v=\min_j\operatorname{ord}_t\phi_j\), avoiding cancellation of its first terms. Thus \(m_\gamma(V)\) is the sum of these \(v\)'s.

Since \(f(t,\phi(t))=0\), substitution in its formal series gives \(\operatorname{ord}_t f(t,0)\geq v\). On the invariant axis, \(\xi\) acts as \(a(t)\,d/dt\). Hence \(g(t,0)\) has order at least \(v-1\), or at least \(v\) if \(a(0)=0\). Substitution back to the branch changes a formal function by terms of order at least \(v\). Therefore \(g(t,\phi(t))\) has order at least \(v-1\), or \(v\) in the singular case. Summing proves (9.37) and its stronger version.

For the second assertion, if any \(v>c\), substitution from \(f(t,\phi(t))=0\) would make the axis order exceed \(c\). Every \(v\leq c\), so their sum is at most \(c\mu\). For a hypersurface the complementary section containing the axis is the axis itself; its one-function local length is the order of \(F\) on that axis. The use of general sections here is legitimate because the base locus is the axis and its intersection with each germ is only \(p\). All intermediate intersections are proper. The final unrestricted section used to compute \(\mu\) is general: every general plane transverse to the axis can be enlarged by that axis to obtain the preceding section. No convergence of the formal Puiseux series is required. \(\square\)

### Theorem 9.29. The multiplicity bound for the four modular functions

There is an absolute constant \(C\) such that every nonzero polynomial
\(A\in\mathbb C[Z,X_1,X_2,X_3]\) of total degree at most \(d\), \(d\geq1\), satisfies

\[
 \operatorname{ord}_0 A(z,E_2(z),E_4(z),E_6(z))\leq C d^4.
 \tag{9.38}
\]

**Proof.** The graph \(\gamma=(z,E_2(z),E_4(z),E_6(z))\) is a smooth invariant curve for \(\mathcal D\), by its first coordinate and Theorem 9.17. Its base point is \(p=(0,1,1,1)\), where all coefficients of \(\mathcal D\) vanish. Proposition 9.19 ensures that it is contained in no proper algebraic variety.

Every nonzero stable prime in the four-variable ring contains a polynomial of axis order one. If its intersection with \(\mathbb C[Z]\) is zero, Theorem 9.25 supplies \(\Delta\). Otherwise that intersection is \((Z-a)\) for a constant \(a\). Stability gives \(Z=\mathcal D(Z-a)\) in the prime, so \(a=0\), and \(Z\) has order one. Thus the D-property holds with constant one for every proper invariant variety, including those contained in \(Z=0\).

Factor \(A\), taking its irreducible hypersurfaces as the roots of a forest with their polynomial multiplicities. At a node \(V\), stop if it is a point or is contained in a proper invariant variety. Otherwise apply Lemma 9.27 to a least-degree polynomial \(E\) in \(I(V)\). The original \(A\) vanishes on \(V\), so \(\deg E\leq d\). For the first escaping index \(N\), the polynomial \(\mathcal D^{N-1}E\) vanishes on \(V\), but its derivative \(G=\mathcal D^NE\) does not. Make the proper intersection \(V\cdot Z(G)\) its children, retaining their intersection multiplicities. Their dimensions are one less than that of \(V\). Lemma 9.27, with \(n=4,\delta=2\), bounds \(\deg G\leq d+K\), with an absolute \(K\).

The sum of node degrees at codimension \(j\) is at most \(d(d+K)^{j-1}\), by the degree rule. At any internal node through \(p\), the singular version of Lemma 9.28 bounds its multiplicity along \(\gamma\) by the sum of its children's multiplicities. At a positive-dimensional leaf, a polynomial from its containing invariant prime has order one on \(\gamma\); the second part of that lemma bounds its multiplicity along \(\gamma\) by its ordinary multiplicity at \(p\), at most its degree. An isolated point at \(p\) has multiplicity along the smooth axis one; points away from \(p\) contribute zero. Sum from leaves to roots. The hypersurface assertion of Lemma 9.28 gives

\[
 \operatorname{ord}_0 A|_\gamma
 \leq\sum_{j=1}^4d(d+K)^{j-1}
 \leq4(d+K)^4\leq C d^4.
\]

This proves (9.38). \(\square\)

For Proposition 9.21, total degree is at most \(4N\). We now have \(N^4/2\leq M_N\leq C'N^4\), so Proposition 9.22 supplies integer polynomials with degree and log height \(O(N(\log N)^2)\) and nonzero values between \(e^{-c_2N^4}\) and \(e^{-c_1N^4}\). The next section starts the arithmetic criterion that turns these small values into algebraic independence.

## 11. Why small integer polynomial values force independence

An auxiliary value can be tiny because the point is close to a zero of its polynomial. One such value proves little. A value for every sufficiently large size parameter is much more restrictive: integer resultants prevent unrelated irreducible polynomials from remaining small at the same point. We first prove this mechanism in one variable, and then explain the finite-extension reduction. These are the first arithmetic steps towards the full criterion required for the four modular values.

For a nonzero polynomial with integer coefficients, write \(\|A\|_1\) for the sum of their absolute values and set

\[
 t(A)=\max\{1,\deg A,\log\|A\|_1\}.
\]

This is a convenient size, equivalent up to fixed constants to degree plus log height when the number of variables is fixed. Indeed, a degree-\(d\) polynomial in \(m\) variables has at most \((d+1)^m\) monomials.

### Lemma 9.30. A resultant evaluated near one point

Fix \(\theta\in\mathbb C\). There is a constant \(C_\theta\) such that, for relatively prime nonconstant \(f,g\in\mathbb Z[X]\), with \(t(f),t(g)\leq U\) and \(U\geq1\),

\[
 1\leq|\operatorname{Res}(f,g)|
 \leq e^{C_\theta U\min\{t(f),t(g)\}}
                 \bigl(|f(\theta)|+|g(\theta)|\bigr).
 \tag{9.39}
\]

**Proof.** Put \(d=\deg f\), \(e=\deg g\). Take the transpose of the coefficient matrix representing
\((a,b)\mapsto af+bg\), with \(\deg a<e\), \(\deg b<d\), in the coefficient basis \(1,X,\ldots,X^{d+e-1}\). Its rows are the shifted coefficient rows of \(f\) and \(g\). It has integer determinant and is nonsingular: a relation \(af+bg=0\) would make \(f\mid b\), forcing \(b=0\), and then \(a=0\). Thus the absolute determinant is at least one.

Replace its constant-coordinate column by the linear combination of all columns with coefficients \(1,\theta,\ldots,\theta^{d+e-1}\). The determinant is unchanged, since the coefficient of that original column is one and all other terms have repeated columns. The new entries are \(\theta^j f(\theta)\) and \(\theta^j g(\theta)\), for the appropriate row shifts. Expand along this column. Each minor has at most \(e\) rows with Euclidean norm at most \(\|f\|_1\), and at most \(d\) rows with norm at most \(\|g\|_1\). Hadamard's determinant inequality therefore gives

\[
 |\operatorname{Res}(f,g)|
 \leq(d+e)\max(1,|\theta|)^{d+e}
       \|f\|_1^e\|g\|_1^d
       \bigl(|f(\theta)|+|g(\theta)|\bigr).
\]

For completeness, that determinant inequality follows by successively subtracting the orthogonal projections of each row on the preceding rows. The resulting perpendicular row lengths multiply to the determinant's modulus and are each no larger than the original row lengths.

Both \(e\log\|f\|_1\) and \(d\log\|g\|_1\) are at most \(t(f)t(g)\leq U\min\{t(f),t(g)\}\). Also \(d+e\leq2U\), while the minimum size is at least one. Absorbing the remaining factors proves (9.39). \(\square\)

### Theorem 9.31. The uniform one-variable criterion

Let \(U_N,V_N\geq1\) be increasing sequences, with

\[
 U_N\longrightarrow\infty,\qquad
 \sup_{N\text{ large}}\frac{U_{N+1}}{U_N}<\infty,
 \qquad \frac{V_N}{U_N^2}\longrightarrow\infty.
 \tag{9.40}
\]

There is no complex number \(\theta\) and sequence of nonzero polynomials \(A_N\in\mathbb Z[X]\), for every sufficiently large \(N\), such that
\(t(A_N)\leq U_N\) and \(0<|A_N(\theta)|\leq e^{-V_N}\).

**Proof.** Factor \(A_N\) into an integer content and nonconstant primitive irreducible factors \(f\), repeated with their multiplicities. For large \(N\) it is not a constant, since a nonzero integer has modulus at least one. The polynomial Mahler measure and coefficient bounds proved in Proposition 2.2 of [Heights, house and Mahler measure](TR-TRANS-02.md) show that

\[
 \sum_f t(f)\leq C U_N.
\]

Here are the details of the sum. Each factor has degree at least one, and \(t(f)\leq\deg f+\log\|f\|_1\). If its degree is \(a\), then \(\|f\|_1\leq(a+1)2^aM(f)\). Multiplicativity of \(M\), \(M(f)\geq1\) for integer factors, \(\sum a=\deg A_N\), and \(\log(a+1)\leq a\) give the displayed bound. The integer content cannot decrease the measure. Finally \(M(A_N)\leq\|A_N\|_1\).

Since the absolute integer content is at least one, the sum of the logarithms of the evaluated factors is at most \(-V_N\). A weighted average therefore selects an irreducible factor \(f_N\) with

\[
 t(f_N)\leq C U_N,
 \qquad \log|f_N(\theta)|
           \leq-\frac{V_N}{C U_N}\,t(f_N).
\]

Normalize each factor to have positive leading coefficient. If \(f_N\ne f_{N+1}\), they are relatively prime. Apply Lemma 9.30 with \(U=C\max(U_N,U_{N+1})\). The ratio bound in (9.40) and monotonicity of \(V_N\) give

\[
 \begin{aligned}
 1&\leq|\operatorname{Res}(f_N,f_{N+1})|\\
  &\leq2\exp\left[
       \left(C' U_N-\frac{V_N}{C' U_N}\right)
                 \min\{t(f_N),t(f_{N+1})\}\right].
 \end{aligned}
\]

For all large \(N\) this is less than one, a contradiction. Thus \(f_N=f_{N+1}\) eventually, and all these normalized factors are one fixed \(f\). Its value is nonzero because it divides an \(A_N\) with nonzero value. But the selected bound tends to \(-\infty\), forcing \(f(\theta)=0\). This final contradiction proves the theorem. \(\square\)

### Lemma 9.32. A controlled field norm

Let \(L=\mathbb Q(\theta_1,\ldots,\theta_m)\subset\mathbb C\) have transcendence degree \(k\). Choose a transcendence basis \(u=(u_1,\ldots,u_k)\) from these generators, so \(L\) is finite over \(K=\mathbb Q(u)\). There is a constant \(C\), depending on these fixed generators, such that every integer polynomial \(A\) with \(t(A)\leq U\), \(U\geq1\), and \(A(\theta)\ne0\), gives an integer polynomial \(B\) in \(k\) variables satisfying

\[
 B(u)\ne0,\qquad t(B)\leq C U,
 \qquad |B(u)|\leq e^{CU}|A(\theta)|.
 \tag{9.41}
\]

For \(k=0\), \(B\) is a nonzero integer.

**Proof.** Take a \(K\)-basis of \(L\), of size \(s\). Multiplication by each fixed \(\theta_j\) is an \(s\)-by-\(s\) matrix over \(K\). There is one nonzero polynomial \(W\in\mathbb Z[T_1,\ldots,T_k]\) clearing all denominators, including their rational numerical coefficients. Thus those matrices are \(W(u)^{-1}M_j(u)\), with \(M_j\) fixed integer polynomial matrices. Algebraic independence of the \(u_i\) ensures \(W(u)\ne0\). When \(k=0\), choose a nonzero integer \(W\).

Put \(d=\deg A\). Multiply the evaluated multiplication matrix by \(W(u)^d\). Its entries are the evaluations of the integer polynomial matrix

\[
 M_A(T)=\sum_{|\alpha|\leq d}
          a_\alpha W(T)^{d-|\alpha|}
                         M_1(T)^{\alpha_1}\cdots M_m(T)^{\alpha_m}.
\]

Set \(B(T)=\det M_A(T)\). Every entry has degree at most \(C d\) and coefficient sum at most \(\|A\|_1 C^d\), after enlarging the fixed \(C\) to bound matrix multiplication and the fixed coefficient sums. The determinant has fixed size \(s\), so \(\deg B\leq C d\) and \(\log\|B\|_1\leq C(d+\log\|A\|_1)\). This proves its size bound. Its evaluated determinant is
\(W(u)^{sd}N_{L/K}(A(\theta))\), nonzero because multiplication by a nonzero field element is invertible.

In characteristic zero, the norm is the product of the \(s\) embeddings of \(L\) into an algebraic closure of \(K\), counted once each. To see the determinant formula directly, adjoining algebraic elements one at a time yields all embeddings by choosing a root of each transported minimal polynomial. The roots are distinct in characteristic zero. Their number is the product of the extension degrees, namely \(s\). Over an algebraic closure these evaluation maps diagonalize the multiplication operators: for a simple extension this is the nonsingular Vandermonde matrix on its distinct roots, and a tower gives the same assertion by successive diagonalization. We may take the algebraic closure inside \(\mathbb C\), so the chosen original embedding is one factor.

The other finitely many images \(\sigma(\theta_j)\) are fixed complex numbers. Consequently
\(|A(\sigma\theta)|\leq\|A\|_1\max(1,|\sigma\theta_1|,\ldots,|\sigma\theta_m|)^d\leq e^{CU}\).
The factor \(|W(u)|^{sd}\) also has logarithm bounded above by \(CU\). Retaining the original factor \(|A(\theta)|\) in the product proves (9.41). \(\square\)

### Proposition 9.33. The first independence consequence

For \(0<|q|<1\), the field
\(\mathbb Q(q,E_2(q),E_4(q),E_6(q))\) has transcendence degree at least two.

**Proof.** Propositions 9.21–9.22 and Theorem 9.29 provide integer polynomials \(B_N\) with
\(t(B_N)\leq C N(\log N)^2\) and
\(0<|B_N(q,E_2(q),E_4(q),E_6(q))|\leq e^{-cN^4}\).
If the field had transcendence degree zero, the norm lemma would produce a nonzero integer of modulus at most \(\exp(C'N(\log N)^2-cN^4)<1\). If it had transcendence degree one, that lemma would produce nonzero integer polynomials in one fixed transcendental basis element, with size at most \(U_N=C'N(\log N)^2\) and nonzero values at most \(e^{-cN^4/2}\) for large \(N\). Since \(U_{N+1}/U_N\to1\) and \(N^4/U_N^2\to\infty\), Theorem 9.31 forbids this sequence. Both cases are impossible. \(\square\)

To reach the full lower bound three, we must also rule out transcendence degree two. The one-variable resultant proof does not do that: two plane curves can intersect, so their simultaneous small values need not produce a nonzero integer. The following criterion controls successive intersections on the fixed surface of algebraic relations, retaining both degree and height and the two-sided bounds for the auxiliary values.

### Theorem 9.34. An arithmetic criterion with two bounds

Let \(\theta=(\theta_1,\ldots,\theta_m)\in\mathbb C^m\). Suppose that for every sufficiently large integer \(N\) there is an integer polynomial \(P_N\) such that
\[
 \deg P_N+\log\|P_N\|_1\le C N(\log N)^2,
 \qquad e^{-c_2N^4}\le |P_N(\theta)|\le e^{-c_1N^4},
 \tag{9.42}
\]
where \(C,c_1,c_2>0\) are fixed. Then
\(\operatorname{trdeg}_{\mathbb Q}\mathbb Q(\theta)\ge3\).

The lower value bound is essential. It supplies a neighbourhood without zeros, which prevents an auxiliary hypersurface from containing every variety close to the chosen point. We prove the criterion, including the height and proximity estimates needed for this step.

**Polynomial measure.** For a complex polynomial \(f\), let
\[
 M(f)=\exp\int_{[0,1]^a}\log|f(e^{2\pi it_1},\ldots,e^{2\pi it_a})|\,dt,
\]
with \(M(0)=0\). The logarithm is integrable for \(f\ne0\): factor in the last variable, use the one-variable Jensen formula, and induct on the number of variables; the exceptional zero coefficients occur on sets of measure zero. The formula gives \(M(fg)=M(f)M(g)\). For integer \(f\ne0\), \(M(f)\ge1\), by successively taking a leading coefficient in one variable and ending with a nonzero integer.

We record the coefficient estimate used below. If \(f\) has total degree \(a\), the coefficient of \(T_1^{j_1}\cdots T_b^{j_b}\), considered as a polynomial in the remaining variables, has measure at most
\(a!M(f)/[(a-\sum j_i)!\prod j_i!]\). For one selected variable, factor its polynomial and bound the elementary symmetric functions by \(\binom a j\) times the Jensen product of \(\max(1,|\alpha|)\). Integrate over the other unit circles. Repeat for the next selected variable; the binomial factors telescope to the stated multinomial coefficient. In particular
\[
 M(f)\le\|f\|_1\le(a_0+1)^aM(f)
 \tag{9.43}
\]
for a polynomial in \(a_0\) variables. Expansion also gives the following useful substitution rule: substituting polynomials of coefficient sum at most \(H\ge1\) increases measure by at most \([(a_0+1)H]^a\), regardless of their degrees. Indeed their monomial expansions have coefficient sum at most \(H^a\|f\|_1\), and measure is at most coefficient sum. In particular this applies to both the linear and quadratic substitutions below. To compare two linear substitutions, subtract their monomial expansions. Each difference contains one coefficient difference and at most \(a-1\) bounded factors. With at most \(b\) output variables, the difference therefore has measure at most its largest coefficient difference times \([C(a_0+1)(b+1)H]^aM(f)\). The measure of a sum is bounded by the sum of its measures times the corresponding factors from (9.43). These observations justify the perturbations used below, even though measure itself is not a norm.

**Forms recording an intersection.** Let \(Y\subset\mathbb P^m\) be an integral variety over \(\mathbb Q\), of dimension \(r-1\), and let \(\delta\ge1\). For each of \(r\) blocks of independent coefficients introduce a general degree-\(\delta\) form
\(U_j(X)=\sum_{|a|=\delta}u_{j,a}X^a\).
There is a primitive integer polynomial \(F_{Y,\delta}(u)\), unique up to sign, that vanishes exactly when these \(r\) forms have a common zero on \(Y\). Its degree in each coefficient block is
\(b=\delta^{r-1}\deg Y\); its total degree is \(d_\delta(Y)=rb\).

Here is the construction and the degree assertion. The incidence variety over \(Y\) imposes \(r\) independent linear conditions on the coefficient blocks, hence has dimension one less than their space. Fixing \(r-1\) general forms cuts \(Y\) into \(\delta^{r-1}\deg Y\) points counted with multiplicity, by the proper-intersection rule of Section 10. The condition on the last form is the product of its values at those points. Thus the image is a hypersurface, with the stated block degree. It is closed by projective elimination: after homogenization the finite degree-piece matrix used below has deficient rank precisely when the ideal has a projective zero. This also constructs its defining polynomial as a factor of every maximal minor. The coefficient ring is a unique factorization domain, so an irreducible hypersurface has a single primitive equation. If \(Y\) splits over \(\mathbb C\), multiply the conjugate equations; their product is the equation over \(\mathbb Q\). All the assertions then hold with the sum of the geometric degrees.

Denote \(h_\delta(Y)=\log M(F_{Y,\delta})\ge0\). For a positive cycle, multiply its component forms to their cycle multiplicities, and extend \(h_\delta,d_\delta\) additively. For a zero-dimensional variety the form is, up to a constant,
\(\prod_{y\in Y}U_1(y)\), counted with multiplicities.

Replacing the last general form by a degree-\(\delta\) integer form \(Q\) not vanishing identically on \(Y\) gives a nonzero polynomial \(F_{Y,\delta}(U_1,\ldots,U_{r-1},Q)\). It factors into the forms of the components of the proper cycle \(Y\cdot Z(Q)\), with positive multiplicities, and an integer constant. To check the multiplicities, fix another \(r-2\) general forms. The resulting curve meets \(Q=0\) in a finite scheme, and the last remaining general form contributes its value at each point to the length of that scheme. The local length and divisor formulas of Section 10 give exactly the proper-intersection multiplicities. There are no other factors, because their vanishing would describe a common projective zero outside that intersection. Consequently
\[
 d_\delta(Y\cdot Z(Q))\le d_\delta(Y),\qquad
 h_\delta(Y\cdot Z(Q))\le h_\delta(Y)+C\tau d_\delta(Y)
 \tag{9.44}
\]
if \(\log\|Q\|_1\le\tau\) and \(\tau\ge\delta\). Indeed the substitution rule just proved bounds the measure of the substituted form; the number of coefficient variables is polynomial in \(\delta\), so its logarithm is absorbed by \(C\delta\). Integer content has nonnegative log measure and can be discarded. This proves both inequalities for the cycle, not just for a selected component.

**A measure of proximity.** We may arrange \(|\theta_i|\le1\) by a fixed rational scaling, clearing the fixed denominators in (9.42). This changes its degree and height costs by \(O(\deg P_N)\), and its value exponents by that same smaller cost. Write \(x=(1,\theta)\). Let \(L(u)=\sum u_a x^a\) and \(c_\delta=M(L)\); then \(1\le c_\delta\le(m+1)^\delta\). In each coefficient block make the normalized substitution
\[
 u_{j,a}\longmapsto c_\delta^{-1}
                  \sum_{a'}s_{j,a,a'}x^{a'},\qquad
                 s_{j,a,a'}=-s_{j,a',a}.
 \tag{9.45}
\]
Use the independent entries with \(a<a'\) as variables. This makes \(U_j(x)=0\). Let \(\mathcal D_x\) denote substitution in all blocks, and put
\[
             \Psi_\delta(Y)=
                    \frac{M(\mathcal D_x F_{Y,\delta})}
                         {M(F_{Y,\delta})}.
 \tag{9.46}
\]
It is zero precisely when \(x\in Y\): all \(r\) hypersurfaces through \(x\) then meet \(Y\); if \(x\notin Y\), general such hypersurfaces avoid \(Y\), by successive proper cuts. The definition is independent of the scalar of the form, and is multiplicative on cycles.

For a projective point \(y\), the same definition is a distance \(D_\delta(y,x)\). Its numerator is the measure of the linear form with coefficients
\(y^a x^{a'}-y^{a'}x^a\); its denominator is the product of the two linear-form measures. A linear form has measure between its largest coefficient and its coefficient sum, by the coefficient estimate above. Thus \(D_\delta\) is comparable, within factors \(e^{C\delta}\), to the largest normalized cross product of degree-\(\delta\) monomials. Those cross products compare to the degree-one cross products within the same factors. Here is an explicit lower estimate. Normalize \(\max|y_i|=1\), while \(x_0=1\) and \(\max|x_i|=1\). Put \(\Delta=\max_{i,j}|x_i y_j-x_j y_i|\). The zeroth cross products have maximum at least \(\Delta/2\), since \(x_i y_j-x_j y_i=x_i(y_j-x_jy_0)-x_j(y_i-x_i y_0)\). If \(|y_0|\ge1/2\), use the monomials \(X_iX_0^{\delta-1},X_0^\delta\); their cross product is \(y_0^{\delta-1}(x_i y_0-y_i)\), and its maximum is at least \(2^{-\delta}\Delta\). If \(|y_0|<1/2\), choose \(|y_j|=1\) and use \(X_0^\delta,X_j^\delta\); their cross product has modulus at least \(1-2^{-\delta}\ge1/2\ge\Delta/4\). For the upper estimate, pair the \(\delta\) factors of two monomials and telescope; each term contains one degree-one cross product and bounded remaining coordinates, giving at most \(\delta\Delta\). Coefficient sums of the linear forms and the number of cross products add only factors \(e^{C\delta}\). If the distance is sufficiently small, the second case is excluded, so \(|y_0|\ge1/2\); the affine distance is then at most \(2\Delta\). In particular sufficiently small \(D_\delta(y,x)\) implies
\[
                        \|y-\theta\|_\infty
                                      \le e^{C\delta}D_\delta(y,x).
 \tag{9.47}
\]

There is a point \(y\in Y(\mathbb C)\) with
\[
                D_\delta(y,x)\le
                   e^{C\delta}\Psi_\delta(Y)^{1/d_\delta(Y)}.
 \tag{9.48}
\]
We prove the assertion rather than assuming that a small resultant has a nearby zero. Substitute (9.45) in the first \(r-1\) blocks only, denoting this substitution by \(\mathcal D'_x\). Its measure is at least
\(e^{-C\delta d_\delta(Y)}M(F_{Y,\delta})\). Here is an explicit inverse identity. Let \(a_0\) denote the monomial \(X_0^\delta\), so \(x^{a_0}=1\), and write \(L_j=U_j(x)\). In \(G=\mathcal D'_xF\), substitute
\[
 s_{j,a,a_0}=c_\delta(u_{j,a}L_r-u_{r,a}L_j)
       \quad(a\ne a_0),\qquad
 s_{j,a,a'}=0\quad(a,a'\ne a_0),
\]
with the opposite entries determined by antisymmetry. Formula (9.45) then gives exactly the coefficient vector of \(L_rU_j-L_jU_r\), including its \(a_0\) coefficient. A transvection \(U_j\mapsto U_j+tU_r\) preserves the intersection hypersurface and its primitive equation: its scalar multiplier is a polynomial unit in \(t\), hence constant, and equals one at \(t=0\). Homogeneity of block degree \(b\) consequently gives the polynomial identity
\[
       G(s(u),U_r)=L_r^{b(r-1)}F(U_1,\ldots,U_r).
\]
The substituted entries are quadratic polynomials of coefficient sum at most \(e^{C\delta}\); the number of variables has logarithm \(O(\delta)\). The substitution estimate gives
\(M(G(s(u),U_r))\le e^{C\delta d_\delta(Y)}M(G)\).
On the other hand its measure is \(c_\delta^{b(r-1)}M(F)\ge M(F)\). This proves the lower bound, with all denominator and normalization factors accounted for.

For almost every choice of the first antisymmetric coefficient blocks on their unit circles, they cut \(Y\) into finitely many points \(y\), whose total multiplicity is \(b=\delta^{r-1}\deg Y\). Factoring the remaining linear form and then taking its measure shows that
\[
 \log M(\mathcal D_x F)-\log M(\mathcal D'_x F)
       =\int\sum_y m_y\log D_\delta(y,x).
\]
If \(a\) is the minimum of \(D_\delta(y,x)\) on \(Y\), the right side is at least \(b\log a\). Use the preceding lower bound and (9.46). If \(\Psi<1\), the resulting bound with exponent \(1/b\) implies the weaker (9.48); if \(\Psi\ge1\), the uniform upper bound \(D_\delta\le e^{C\delta}\) implies it directly. The case \(\Psi=0\) is the already established inclusion \(x\in Y\). This proves (9.48).

**Two intersection estimates.** Set \(A=h_\delta(Y)+\tau d_\delta(Y)\), where \(\tau\ge\delta\), and assume \(Q\) is integer, homogeneous of degree \(\delta\), with \(\log\|Q\|_1\le\tau\), and is nonzero on \(Y\). For its proper intersection cycle, write \(\Psi'\). We have
\[
 \begin{aligned}
 \log\Psi'&\le
       \log(\Psi_\delta(Y)+|Q(x)|)+CA,\\
 \log\Psi'&\le\eta\log\Psi_\delta(Y)+CA
       \quad\text{if } |Q(x)|\le
             \min\{1,\min_{y\in Y}D_\delta(y,x)^\eta\},
                \quad0<\eta\le1.
 \end{aligned}
 \tag{9.49}
\]
For \(r=1\), a proper intersection means no zero at any conjugate point, the specialized form is a nonzero integer, and \(\Psi'=1\).

Here are the estimates in detail. For the first, set
\(Q_0=Q-Q(x)X_0^\delta\). Its coefficient vector vanishes at \(x\), so it is an instance of the antisymmetric substitution in the last block. Its coefficients have size at most \(e^{C\tau}\). Substitution therefore bounds
\(M(\mathcal D'_x F(U_1,\ldots,U_{r-1},Q_0))\) by
\(M(\mathcal D_x F)e^{C\tau d_\delta(Y)}\).
Replacing \(Q_0\) by \(Q\) changes one coefficient by \(Q(x)\). The difference estimate after (9.43) bounds the measure of that difference by
\(|Q(x)|M(F)e^{C\tau d_\delta(Y)}\). The measure-of-a-sum estimate gives the first line of (9.49). The denominator, the measure of the nonzero integer specialization of \(F\), is at least one. This accounts for the \(h_\delta(Y)\) term; the normalizing factors \(c_\delta\) cost at most \(C\delta d_\delta(Y)\), already included.

For the second, fix generic first \(r-1\) antisymmetric blocks and their finite intersection points. Expanding \(Q(y)\) in the degree-\(\delta\) cross products with \(x\) gives
\[
 \frac{|Q(y)|}{M(\sum u_a y^a)}
       \le e^{C\tau}
              \big(D_\delta(y,x)+|Q(x)|/M(Q)\big).
\]
Indeed subtract \(Q(x)y_0^\delta\), telescope the coefficient sum, use the largest coefficient lower bound for the linear form, and use \(c_\delta\le e^{C\delta}\). Since \(M(Q)\ge1\), the assumed bound and \(D_\delta\le e^{C\delta}\) bound the right side by
\(e^{C\tau}D_\delta(y,x)^\eta\).
Multiply these inequalities to the intersection multiplicities, using the product-of-linear-forms description of \(F\). Integrating logarithms over the first coefficient blocks gives
\[
 \log M(\mathcal D'_x F(Q))\le
 (1-\eta)\log M(\mathcal D'_x F)
           +\eta\log M(\mathcal D_x F)+C\tau d_\delta(Y).
\]
The upper substitution bound for the first term is
\(\log M(\mathcal D'_x F)\le h_\delta(Y)+C\delta d_\delta(Y)\).
Divide by the measure of the nonzero integer specialization, which is at least one, and apply (9.46). This proves the second line of (9.49), including the zero-dimensional case. Every measure and multiplicity in these inequalities has now been specified.

**The initial height bound.** For any fixed projective surface \(V\) over \(\mathbb Q\),
\[
                 d_\delta(V)\le C\delta^2,
                 \qquad h_\delta(V)\le C\delta^3.
 \tag{9.50}
\]
The degree formula already proves the first assertion. For the height assertion, normalize the fixed homogeneous coordinate ring over three independent linear coordinates. Each extra coordinate satisfies a fixed monic homogeneous equation in that coordinate and the three base coordinates. This normalization is obtained by making a homogeneous relation monic in the last coordinate through a rational linear change, then projecting and repeating; integrality is transitive. Reduction by these equations gives at most \(C\delta^2\) monomials in a homogeneous degree piece \(M\le C\delta\): the extra exponents are bounded by the fixed monic degrees and the three base exponents sum to \(M\).

For three generic degree-\(\delta\) forms and the fixed equations of \(V\), that piece is spanned by their monomial multiples. To see the degree bound, work first in the ring defined only by the fixed monic equations. It is free over the polynomial ring in the three base coordinates, hence Cohen–Macaulay. For \(\delta\) greater than the fixed generator degrees, pad each generator with all monomials needed to reach degree \(\delta\). These padded equations and the three generic forms have no common projective zero. Three general combinations therefore form a regular sequence, by the open regular-sequence inputs in Section 10. If the monic degrees are \(\nu_i\), the quotient's Koszul Hilbert series is
\((1+\cdots+z^{\delta-1})^3\prod_i(1+\cdots+z^{\nu_i-1})\).
It vanishes in degrees above \(3(\delta-1)+\sum_i(\nu_i-1)\). Choose \(M\) one greater. Their degree-\(M\) multiples span the monic quotient, and hence so do the original padded equations and generic forms. Its reduced matrix has at most \(C\delta^2\) rows. Each entry is linear in the generic coefficients, with coefficient sum at most \(e^{C\delta}\), because a monomial reduction has at most \(C\delta\) steps using fixed equations and fixed denominators. A nonzero square maximal minor therefore has integer coefficients, after fixed-denominator clearing, with log coefficient sum at most \(C\delta^3\). The intersection equation \(F_{V,\delta}\) divides this minor: at a common projective zero the matrix cannot have full rank, so its determinant vanishes on that hypersurface. Gauss's lemma makes the primitive quotient integer. Its measure is at least one; thus the factor's measure is at most that of the minor. This proves the second assertion without importing an arithmetic Bézout theorem.

**Proof of the criterion.** Transcendence degree zero or one is already excluded by Lemma 9.32 and Theorem 9.31. Suppose that it is two, and let \(V\subset\mathbb P^m\) be the projective closure of the prime ideal of rational relations of \(x=(1,\theta)\). It is a fixed surface.

Choose increasing integers \(\delta_N\asymp N(\log N)^2\) bounding all degrees, and increasing \(\tau_N\asymp N(\log N)^2\), with \(\tau_N\ge\delta_N\), bounding the coefficient costs. Put
\(S_N=cN^4\), \(R_N=C_0N^4\), with fixed \(c>0,C_0>c\). After the fixed normalization, (9.42) still gives the upper bound \(e^{-S_N}\). Its lower bound and the derivative bound
\(\sup_{\|z-\theta\|\le1}|\nabla P_N(z)|\le e^{C\tau_N}\)
show that \(P_N\) has no zero in the closed ball
\(\|z-\theta\|_\infty\le e^{-R_N}\), for a sufficiently large \(C_0\). The derivative estimate follows directly from its coefficient sum and degree; the exponential value lower bound dominates that cost.

Set
\[
                B_N=\tau_N\delta_N^2,
                \qquad W_N=S_N/B_N.
 \tag{9.51}
\]
We can make \(W_N\) increasing after deleting finitely many indices, and \(W_N\to\infty\), since it is a positive constant times \(N/(\log N)^6\). Also \(S_M/(2R_{M+1})\) is bounded below by a fixed \(\eta_0>0\), which we may take at most one.

For \(r=3,2,1\), construct for every sufficiently large \(N\) an integral subvariety \(Y_{N,r}\subset V\) of dimension \(r-1\), defined over \(\mathbb Q\), such that, for \(\delta=\delta_N\), \(\tau=\tau_N\),
\[
 \begin{gathered}
 d_\delta(Y_{N,r})\le C_r\delta_N^2,
 \quad h_\delta(Y_{N,r})\le C_r B_N,\\
 \log\Psi_\delta(Y_{N,r})\le
   -\big(h_\delta(Y_{N,r})+\tau_N d_\delta(Y_{N,r})\big)W_N^{r/3}.
 \end{gathered}
 \tag{9.52}
\]
The initial variety \(Y_{N,3}=V\) works by (9.50), since \(x\in V\) and its proximity is zero.

Assume (9.52) at \(r\ge2\), and call the variety \(Y\), with
\(A=h_\delta(Y)+\tau_Nd_\delta(Y)\le CB_N\).
Equations (9.47)–(9.48) give affine points of \(Y\) at distances tending to zero. The minimum affine distance is attained: intersect its closed affine locus with a fixed compact ball containing one such point, and minimize the continuous distance there. Call a minimizer a closest point. If the distance is zero set \(M=N\). Otherwise choose the largest index \(M\le N\) for which that distance is strictly less than \(e^{-R_M}\). It exists for large \(N\), by (9.52). For \(M<N\), its distance is at least \(e^{-R_{M+1}}\).

The polynomial \(P_M\) is nonzero on \(Y\). A closest point in its zero-free ball proves this, and positive dimension ensures that containment would put infinitely many zeros in that ball. Homogenize \(P_M\) to degree \(\delta_N\) by powers of \(X_0\), calling the result \(Q\). The coordinate \(X_0\) does not vanish identically on \(Y\), and \(Q\) still has size at most \(C\tau_N\); absorb the fixed constant in \(\tau_N\).

If \(M=N\), the first line of (9.49) gives
\[
 \log\Psi_\delta(Y\cdot Z(Q))
       \le-\min\{AW_N^{r/3},S_N\}+CA+\log2.
\]
Because \(A\le CB_N\) and \(S_N=B_NW_N\), the negative term, divided by \(AW_N^{(r-1)/3}\), tends to infinity. If \(M<N\), let
\(a=\min_{y\in Y}D_\delta(y,x)\).
Equations (9.48) and (9.52) make \(a<e^{-K\delta_N}\) for any fixed \(K\), eventually. Equation (9.47) then bounds the closest affine distance by \(a^{1/2}\), since \(e^{C\delta_N}a\le a^{1/2}\). Hence
\(a\ge e^{-2R_{M+1}}\). We have
\(|Q(x)|\le e^{-S_M}\le\min(1,a^{\eta_0})\).
The second line of (9.49) gives
\[
 \log\Psi_\delta(Y\cdot Z(Q))
       \le-\eta_0AW_N^{r/3}+CA.
\]
This has the same stronger-than-required negative bound.

By (9.44), the sum of \(h_\delta+\tau_Nd_\delta\) over the positive intersection cycle is at most \(CA\). Log proximity is additive on that cycle. Some rational integral component therefore satisfies the last line of (9.52) with exponent \((r-1)/3\); otherwise adding all its component inequalities would contradict the just established bound for the cycle. Its degree and height satisfy the first line too. This constructs \(Y_{N,r-1}\). Both cuts are proper on a projective positive-dimensional variety and therefore give a nonempty cycle; the proper-intersection degree is positive.

We have reached a rational integral zero-dimensional variety \(Y=Y_{N,1}\). Repeat the same choice of \(M\), using its closest point. The zero-free ball makes \(P_M\) nonzero at that point. As the points of \(Y\) are algebraic conjugates and \(P_M\) is rational, it is nonzero at every point of \(Y\). The specialized intersection form is thus a nonzero integer constant and its proximity is one. For \(M=N\), the first line of (9.49) nevertheless makes its log proximity at most
\(-\min(AW_N^{1/3},S_N)+CA+\log2<0\).
For \(M<N\), the second line makes it at most
\(-\eta_0AW_N^{1/3}+CA<0\).
Both contradict log proximity zero. This excludes transcendence degree two and completes the proof. \(\square\)

The proof uses the empty zero neighbourhood supplied by the lower bound. A general criterion allowing finitely many zeros there requires an additional stabilization argument. That stronger version is not needed here. The intersection forms, the two proximity estimates and the arithmetic construction are the classical ingredients of Philippon's criterion; all the support for this particular version has been given above.

### Theorem 9.35. Nesterenko's modular-value theorem

For every complex \(q\) with \(0<|q|<1\),
\[
       \operatorname{trdeg}_{\mathbb Q}
                 \mathbb Q(q,E_2(q),E_4(q),E_6(q))\ge3.
 \tag{9.53}
\]

**Proof.** Proposition 9.21 constructs integer auxiliary polynomials for every sufficiently large \(N\). Theorem 9.29 bounds their initial multiplicities by \(CN^4\), and Proposition 9.22 converts these into nonzero value bounds
\(e^{-c_2N^4}\le|B_N(q,E_2(q),E_4(q),E_6(q))|\le e^{-c_1N^4}\),
with degree and log coefficient sum at most \(CN(\log N)^2\). The constants may depend on the fixed nonzero argument \(q\), as permitted in Theorem 9.34. Apply that theorem to the four displayed numbers. This proves (9.53) for complex arguments throughout the punctured unit disc, not just for a real argument or for the square lattice. \(\square\)

At \(q=e^{-2\pi}\), the square-lattice relations in the next section give the unconditional independence of \(\pi,e^\pi\). Lesson 15, Proposition 15.19, transfers the same three-dimensional lower bound to \(\pi,e^\pi,\Gamma(1/4)\), with the exact lemniscate normalization.

### Proposition 9.36. Torsion values and the multiplication trace

Suppose \(g_2,g_3\) are algebraic and \(\alpha\ne0\) satisfies \(\alpha L\subseteq L\). Then \(N=|\alpha|^2\) is a positive integer. For the finite set
\(T=\alpha^{-1}L/L\), containing \(N\) classes, define

\[
 c_\alpha=\frac1\alpha\sum_{v\in T\setminus\{0\}}\wp(v).
\]

It is algebraic, and for every \(\omega\in L\),

\[
 \eta(\alpha\omega)=\overline\alpha\,\eta(\omega)
                         +c_\alpha\omega.
 \tag{9.54}
\]

**Proof.** Multiplication by \(\alpha\) has an integer matrix on a lattice basis. Its determinant is positive and equals \(|\alpha|^2\), by its area scaling on the real plane. The index \([L:\alpha L]\) is that determinant: the integer basis reduction used for (9.17) computes both as the product of its two diagonal entries. Multiplication by \(\alpha\) identifies \(\alpha^{-1}L/L\) with \(L/\alpha L\), so the kernel has exactly \(N\) elements. The same integer matrix's characteristic polynomial shows \(\alpha\) algebraic. Every kernel class is killed by \(N\), since the adjugate of the integer matrix makes \(NL\subseteq\alpha L\).

Every nonzero torsion class has algebraic \(\wp\)-value. Here are the details needed for that assertion. For an integer \(n>0\), \(\wp(nz)\) is even and \(L\)-elliptic, so Lemma 9.5 expresses it as a rational function \(R_n(\wp(z))\). The algebraic Laurent coefficient argument in Lemma 9.14 applies with multiplier \(n\): the linear equations on a numerator and denominator have algebraic entries, a finite basis for their row space, and hence an algebraic solution with denominator not identically zero. Reduce that rational function to relatively prime numerator and denominator in \(\overline{\mathbb Q}[X]\). If \(v\notin L\) and \(nv\in L\), then \(\wp(v)\) is finite, whereas \(\wp(nz)\) has a pole at \(v\). The denominator of \(R_n\) must vanish at \(\wp(v)\): otherwise the composition would be holomorphic there. Its nonzero algebraic polynomial therefore makes \(\wp(v)\) algebraic. This applies to every nonzero element of \(T\), with \(n=N\), and proves algebraicity of \(c_\alpha\).

Choose representatives of all classes of \(T\), taking zero for its identity class, and form

\[
 H(z)=\zeta(\alpha z)-\frac1\alpha\sum_{v\in T}\zeta(z-v).
\]

At each point of \(\alpha^{-1}L\), the first term has a simple pole of residue \(1/\alpha\), and exactly one term in the sum has the same pole and residue. Thus \(H\) is entire. Its derivative is \(L\)-elliptic, since

\[
 H'(z)=-\alpha\wp(\alpha z)+\frac1\alpha\sum_{v\in T}\wp(z-v).
\]

The derivative is entire too, and hence constant. At zero the polar terms from the identity class cancel, and the remaining constant coefficient is exactly \(c_\alpha\), because the Laurent series of \(\wp(z)\) has no constant term. Therefore \(H(z)=c_\alpha z+d\) for a constant \(d\). Translation by \(\omega\in L\) yields

\[
 \eta(\alpha\omega)-\frac N\alpha\eta(\omega)=c_\alpha\omega.
\]

Since \(N/\alpha=\overline\alpha\), this is (9.54). Changing representatives alters only \(d\), not the quasi-period relation. \(\square\)

### Proposition 9.37. The complex multiplication span

Suppose \(L\) has algebraic invariants and a nonreal multiplier \(\alpha\). With \(\tau=\omega_1/\omega_2\), there is an algebraic \(c\) such that

\[
 \omega_1=\tau\omega_2,\qquad
 \eta_1=\overline\tau\eta_2+c\omega_2,
 \qquad
 \eta_2=\frac{2\pi i/\omega_2+c\omega_2}{\tau-\overline\tau}.
 \tag{9.55}
\]

Consequently the algebraic-number span of
\(1,\omega_1,\omega_2,\eta_1,\eta_2,2\pi i\) has dimension at most four. Every nonzero algebraic linear combination of the four periods and quasi-periods in this single complex multiplication lattice is transcendental.

**Proof.** Write \(\alpha\omega_2=r\omega_1+s\omega_2\), with integers \(r,s\). We have \(r\ne0\), since otherwise \(\alpha=s\) would be real. The ratio \(\tau\) is imaginary quadratic by Theorem 9.13's multiplier characterization, so is algebraic. Equation (9.54) gives

\[
 r\eta_1+s\eta_2=\overline\alpha\eta_2+c_\alpha\omega_2,
 \qquad \overline\alpha=r\overline\tau+s.
\]

Thus \(\eta_1=\overline\tau\eta_2+(c_\alpha/r)\omega_2\); put \(c=c_\alpha/r\), algebraic by Proposition 9.36. Substitution in the Legendre relation gives the last formula in (9.55).

The first two formulas reduce the indicated span to that of \(1,\omega_2,\eta_2,2\pi i\), so its dimension is at most four. They also express every algebraic linear combination of \(\omega_1,\omega_2,\eta_1,\eta_2\) as \(a\omega_2+b\eta_2\), with algebraic \(a,b\). If its value is nonzero, these two coefficients cannot both be zero. Theorem 9.3 makes it transcendental. \(\square\)

For later use, scaling (9.13) and (9.23) gives, for any algebraic-invariant lattice with ratio \(\tau\) and \(q=e^{2\pi i\tau}\),

\[
 E_2(q)=\frac{3\omega_2\eta_2}{\pi^2},\qquad
 E_4(q)=\frac{3g_2}{4}\left(\frac{\omega_2}{\pi}\right)^4,
 \qquad
 E_6(q)=\frac{27g_3}{8}\left(\frac{\omega_2}{\pi}\right)^6.
 \tag{9.56}
\]

Indeed \(L=\omega_2L_\tau\), the invariants scale by \(\omega_2^{-4},\omega_2^{-6}\), and quasi-periods scale by \(\omega_2^{-1}\). Formula (9.55) now places all four values \(q,E_2(q),E_4(q),E_6(q)\) in \(\overline{\mathbb Q}(q,\pi,\omega_2)\). Theorem 9.35 therefore makes \(q,\pi,\omega_2\) algebraically independent. Theorem 9.39 below establishes the linear span dimension four through the period-space theorem in Section 13. The algebraic independence conclusion uses the full modular bound, whereas the span conclusion uses the period theorem.

In the square case, \(\alpha=i\) has \(N=1\), so \(c_\alpha=0\). Choose the algebraic invariants \((g_2,g_3)=(4,0)\) from Lesson 8, with least positive real period \(\omega\) and lattice \(\omega\mathbb Z[i]\). Equations (9.54) and (9.1) give \(\eta(i\omega)=-i\eta(\omega)\) and \(\eta(\omega)=\pi/\omega\). Hence, at \(q=e^{-2\pi}\),

\[
 E_2(q)=\frac3\pi,\qquad
 E_4(q)=3\left(\frac\omega\pi\right)^4,
 \qquad E_6(q)=0.
 \tag{9.57}
\]

Theorem 9.35 makes \(q,\pi,\omega\) independent. In particular \(\pi\) and \(e^\pi\) are algebraically independent, since \(q=(e^\pi)^{-2}\). This conclusion uses the arithmetic theorem, in addition to Proposition 9.19 about functions.

## 13. Linear relations across elliptic period spaces

The Schneider–Lang proof in section 1 concerns one period and its associated quasi-period. For relations across different curves, or across all four entries of a period matrix, the natural object is the period space of an abelian variety. The prerequisite is *Elliptic logarithms, the analytic subgroup theorem and open problems*, Lesson 22 of *Linear forms in logarithms and their applications*: Section 2 treats the analytic subgroup theorem and Section 3 its period-space consequences. The full statements needed for the deductions here are specified below.

The dependency concerns the abstract subgroup and period theorems, which do not use the independence conclusions of this section. The elementary elliptic constructions in sections 1–6 can be read first; the subgroup and period proof sections then supply the following input; the present section applies it. The later elliptic applications in the logarithms course may in turn use these conclusions. This order separates the actual mathematical dependencies within the two lessons.

The precise input is the **pure period-space theorem** over \(\overline{\mathbb Q}\). For an abelian variety \(A\), let \(\mathcal P(A)\) be the \(\overline{\mathbb Q}\)-span of the entries of its comparison pairing

\[
 H^1_{\mathrm{dR}}(A/\overline{\mathbb Q})
       \times H_1(A(\mathbb C),\mathbb Q)
       \longrightarrow\mathbb C,
       \qquad(\alpha,\gamma)\longmapsto\int_\gamma\alpha.
\]

The prerequisite includes the construction of this pairing, its computation with differentials of the second kind on smooth projective curves, and the following theorem. If \(A\) is isogenous to a product of powers of pairwise nonisogenous simple abelian varieties \(B\), and
\(g(B)=\dim B\), \(e(B)=\dim_{\mathbb Q}\operatorname{End}(B)\otimes\mathbb Q\), then

\[
 \overline{\mathbb Q}\,1
 \;\oplus\;\overline{\mathbb Q}\,2\pi i
 \;\oplus\;\mathcal P(A)
\]

is a direct sum and

\[
 \dim_{\overline{\mathbb Q}}\mathcal P(A)
       =\sum_B\frac{4g(B)^2}{e(B)}.
 \tag{9.58}
\]

The sum counts each simple isogeny class once. This is the specialization to pure abelian, algebraic and Tate periods of the period theorem in that lesson. Its exact mathematical reference is Huber–Wüstholz, *Transcendence and Linear Relations of 1-Periods*, Theorem 15.3 for a product of pure constituents, Theorem 16.2 and Proposition 16.5(1)–(2).

### Theorem 9.38. Combinations from two algebraic elliptic curves

Let \(E_1,E_2\) have algebraic Weierstrass invariants, and let \(\omega_j\ne0\) be periods with associated quasi-periods \(\eta_j\). Every nonzero value of

\[
 a_1\omega_1+b_1\eta_1+a_2\omega_2+b_2\eta_2,
 \qquad a_j,b_j\in\overline{\mathbb Q},
\]

is transcendental. The curves may be equal, isogenous or nonisogenous, and the periods need not be primitive.

**Proof from the stated internal prerequisite.** In the coordinate normalization of Lesson 8, the form \(dx/y\) pulls back to \(dz\), and \(-x\,dx/y\) pulls back to \(-\wp(z)\,dz=d\zeta(z)\). The latter is of the second kind: its expansion at the point at infinity has a double pole and zero residue. Its integral along a displaced closed period path is the increment \(\eta(\omega)\). Thus both \(\omega_j\) and \(\eta_j\) are entries of the elliptic comparison pairing. Pull the forms back to \(A=E_1\times E_2\) and use the corresponding homology cycle in the relevant factor. All four numbers belong to \(\mathcal P(A)\).

By the direct sum in the internal period-space theorem,
\(\mathcal P(A)\cap\overline{\mathbb Q}=\{0\}\).
Their displayed algebraic combination can therefore be algebraic only when its value is zero. Every nonzero value is transcendental, as claimed. The argument does not require the two simple factors to be distinct, so it includes the isogenous and equal cases. \(\square\)

In particular, section 4 expresses the perimeter of each algebraic ellipse as one such period combination. The sum of two perimeters is a positive nonzero value in \(\mathcal P(E_1\times E_2)\), hence is transcendental as well.

### Theorem 9.39. The dimension is four or six

For an elliptic curve with algebraic invariants and a positive lattice basis \((\omega_1,\omega_2)\), with quasi-periods \((\eta_1,\eta_2)\),

\[
 \dim_{\overline{\mathbb Q}}
 \operatorname{span}\{1,2\pi i,\omega_1,\omega_2,\eta_1,\eta_2\}
 =
 \begin{cases}
 4,&\text{if the curve has complex multiplication},\\
 6,&\text{otherwise}.
 \end{cases}
 \tag{9.59}
\]

**Proof from the stated internal prerequisite.** For a smooth projective genus-one curve, the comparison construction in that prerequisite gives a two-dimensional de Rham space. The two forms \(dx/y\) and \(-x\,dx/y\) used above are a basis: their integrals on the two basis cycles have determinant \(\omega_1\eta_2-\omega_2\eta_1=2\pi i\ne0\), so their classes are independent. Consequently
\(\mathcal P(E)=\operatorname{span}_{\overline{\mathbb Q}}\{\omega_1,\omega_2,\eta_1,\eta_2\}\).

We identify its endomorphism degree. A holomorphic group endomorphism of \(\mathbb C/L\) lifts to an additive entire map of \(\mathbb C\), hence to \(z\mapsto\alpha z\) with \(\alpha L\subseteq L\). Indeed, the difference between the lift of a sum and the sum of the lifts is lattice-valued and continuous, so is constant and zero at the origin; differentiating additivity makes its derivative constant. Conversely such a multiplier defines a group endomorphism. For algebraic invariants these endomorphisms are defined over \(\overline{\mathbb Q}\). The multiplier is algebraic by its integral lattice matrix. The even function \(\wp(\alpha z)\) is rational in \(\wp(z)\) by Lemma 9.5; its algebraic Laurent coefficients give algebraic rational coefficients by the finite linear-system argument in Lemma 9.14. Differentiating gives the corresponding odd coordinate as an algebraic rational multiple of \(\wp'(z)\). This describes the morphism over \(\overline{\mathbb Q}\).

Writing \(\alpha\omega_2=r\omega_1+s\omega_2\) shows that every multiplier lies in \(\mathbb Q+\mathbb Q\tau\), \(\tau=\omega_1/\omega_2\). If \(\alpha\) is real, the imaginary part forces \(r=0\) and \(\alpha=s\in\mathbb Z\). Thus without a nonreal multiplier the endomorphism algebra is \(\mathbb Q\) and has degree one. With complex multiplication, Theorem 9.13 makes \(\tau\) imaginary quadratic and a nonreal multiplier generates this quadratic field. The endomorphism algebra then has degree two.

Apply (9.58) with \(g(E)=1\). It gives \(\dim\mathcal P(E)=4/e(E)\), and the direct algebraic and Tate summands add two more dimensions. This is six when \(e(E)=1\) and four when \(e(E)=2\), proving (9.59). In the CM case the relations written in Proposition 9.37 already give the upper bound explicitly; the period theorem supplies its matching lower bound. \(\square\)

The determinant relation is algebraic of degree two in the period entries, while the non-CM conclusion says that all six displayed numbers are linearly independent over the algebraic numbers. It is an explicit example of algebraic dependence coexisting with linear independence over \(\overline{\mathbb Q}\). Also \(\pi+\omega\) and \(\pi+\eta(\omega)\) are transcendental: if either were algebraic, the direct sum of the algebraic, Tate and elliptic period spaces would give a nontrivial relation between its summands.


## 14. Exercises

1. **Easy — a period and its quasi-period.** Deduce from Theorem 9.3 that no nonzero period and its quasi-period can both be algebraic. Explain why this theorem also excludes a zero quasi-period.

2. **Medium — commensurable lattices.** Prove that \(\wp_L,\wp_M\) are algebraically dependent if and only if \(mM\subseteq L\) for some positive integer \(m\). Account explicitly for both signs in a Weierstrass fibre, and prove the rational-function fact needed for the converse.

3. **Medium — a transcendental near-integer.** Prove that \(e^{\pi\sqrt{163}}\) is transcendental and compute its distance from \(640320^3+744\) to three significant digits. Give an error estimate strong enough to justify those digits, rather than subtracting rounded floating-point values.

4. **Medium — a complex multiplication multiplier.** Suppose \(\alpha\ne0\) satisfies \(\alpha L\subseteq L\). Prove that \(\wp_L(z)\) and \(\wp_L(\alpha z)\) are algebraically dependent. Explain the implication when \(\alpha\) generates an order acting on \(L\).

5. **Hard — an ellipse.** For real algebraic semiaxes \(a>b>0\), use the exact formula (9.12), whose defining integral is derived in section 4 and whose transcendence interpretation is Schneider's theorem on periods of elliptic integrals of the second kind (Waldschmidt, *Transcendence Methods*, Corollary 7.1.2), to prove that the ellipse's perimeter is transcendental. Derive that formula with its associated cubic and primitive period, including cancellation at the infinite endpoint.

## 15. Solutions

1. If both \(\omega\) and \(\eta(\omega)\) were algebraic, already the coefficient choice \((a,b)=(1,0)\) would contradict Theorem 9.3. In fact that choice proves the period is individually transcendental, while \((a,b)=(0,1)\) proves the quasi-period is individually transcendental. Zero is algebraic, so the latter choice also proves \(\eta(\omega)\ne0\) whenever \(\omega\ne0\). No assumption that the quasi-period was nonzero is needed to invoke the theorem.

2. Write a monic dependence relation for \(\wp_L\) over \(\mathbb C(\wp_M)\). For a basis period \(\nu\) of \(M\), choose \(z_0\) avoiding its coefficient poles, all \(L-k\nu\), and \(\tfrac12(L+\mathbb Z\nu)\). These are countable forbidden sets. At \(z_0+k\nu\), the coefficients are unchanged, so two \(\wp_L\)-values agree. The fibre count gives either \((k-\ell)\nu\in L\) or \(2z_0+(k+\ell)\nu\in L\); the second is excluded by the choice of \(z_0\). Apply this to both basis periods and take a common multiple to obtain \(mM\subseteq L\).

   Conversely, \(\wp_L(mz)\) is even and elliptic under both \(L\) and \(M\). To express an even elliptic function in \(\wp\), cancel its principal parts on each fibre: ordinary fibres have the two points \(\pm v\) and local coordinate \(\wp-\wp(v)\); the same negative-power principal part cancels both by evenness. A half-period fibre is exactly double, and the even Laurent series in \(t=z-v\) becomes a Laurent series in \(t^2\), with invertible coordinate \(\wp-\wp(v)\). At zero, cancel the even pole powers with powers of \(\wp\). The remaining entire elliptic function is constant. This proves rational presentations \(\wp_L(mz)=R(\wp_M)=S(\wp_L)\) with both rational functions nonconstant. Clearing denominators gives a nonzero polynomial relation, proving the converse.

3. For the logarithm \(\log(-1)=i\pi\), the algebraic irrational exponent \(-i\sqrt{163}\) gives \((-1)^{-i\sqrt{163}}=e^{\pi\sqrt{163}}\). Theorem 6.1, the fixed-branch Gelfond–Schneider theorem, makes this value transcendental. For the distance, exact rational arctangent bounds for \(\pi\), squared rational bounds for \(\sqrt{163}\), and the exponential Taylor remainder described after (9.21) give

   \[
   7.499274028018\times10^{-13}
   <640320^3+744-e^{\pi\sqrt{163}}
   <7.499274028019\times10^{-13}.
   \]

   The quantity is positive, so this is its distance from the integer. Both endpoints round to \(7.50\times10^{-13}\) to three significant digits. A subtraction of values printed to eighteen decimal digits would lose this information; the certified exponential interval retains it.

4. For \(\omega\in L\), \(\alpha\omega\in L\), so \(\wp_L(\alpha(z+\omega))=\wp_L(\alpha z)\). The function is also even. Lemma 9.5 therefore supplies a nonconstant rational function \(R\) with \(\wp_L(\alpha z)=R(\wp_L(z))\). Clear the denominator to get a polynomial relation. If the order acts on \(L\), every one of its nonzero elements has this property, in particular its generator. The result concerns dependence of the functions; it makes no automatic assertion that values at arbitrary arguments are algebraic.

5. Put \(k^2=1-b^2/a^2\), and take the three algebraic roots \(e_1=(2-k^2)/3,e_2=(2k^2-1)/3,e_3=-(1+k^2)/3\). Their distinctness gives a nonsingular algebraic cubic and a lattice by Theorem 8.11. Its real half-period \(K\) is (9.11), and \(\omega=2K\) is its least positive real period, hence primitive. For \(t=(\wp(z)-e_3)^{-1/2}\), the positive real branch gives \(dz=dt/\sqrt{(1-t^2)(1-k^2t^2)}\). The derivative of \(H(t)=\sqrt{(1-t^2)(1-k^2t^2)}/t\) is \((k^2t^4-1)/(t^2\sqrt{(1-t^2)(1-k^2t^2)})\). Integrating \(\zeta'=-\wp\), the terms \(\zeta(\varepsilon)\) and \(H(t_\varepsilon)\) both have leading term \(1/\varepsilon\) and cancel, leaving

   \[
   \zeta(K)=-e_3K-k^2\int_0^1
       \frac{t^2\,dt}{\sqrt{(1-t^2)(1-k^2t^2)}}.
   \]

   The perimeter integral satisfies \(E(k)=K-k^2\int_0^1t^2/\sqrt{(1-t^2)(1-k^2t^2)}\,dt\). As \(1+e_3=e_1\), we get \(E(k)=\zeta(K)+e_1K\). Equation (9.2) gives \(\eta=2\zeta(K)\), so the perimeter is \(4aE(k)=2a(\eta+e_1\omega)\). The coefficients are algebraic and its quasi-period coefficient is nonzero. Theorem 9.3 proves transcendence.

## References and mathematical credit

- Michel Waldschmidt, [*Elliptic Functions and Transcendence*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SurveyTrdceEllipt2006.pdf), author's version of the survey in *Surveys in Number Theory*, 2008: §2.5 for quasi-periods and the Legendre relation; §3.1, Theorems 18 and 20 and Corollary 21, for Schneider's theorems on periods, quasi-periods and the modular invariant; §4.1, Theorem 26, for Masser's theorem on periods and quasi-periods; §5.6 for Nesterenko's theorem.
- Michel Waldschmidt, [*Transcendence Methods*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/QueensPaper52.pdf), Queen's Papers in Pure and Applied Mathematics 52, Queen's University, Kingston, 1979, Lecture 7, §7.1: Schneider's theorems, Theorem 7.1.1 on the linear independence of \(1,\omega,\eta\) over \(\overline{\mathbb Q}\), Corollary 7.1.2 on periods of elliptic integrals of the first and second kinds, and the later results of Baker and of Masser (Theorem 7.1.4).
- J. S. Milne, [*Modular Functions and Modular Forms*](https://www.jmilne.org/math/CourseNotes/MF.pdf), course notes, for modular polynomials and complex multiplication for elliptic curves over \(\mathbb Q\). Sections 5–6 supply the needed modular polynomial, conjugation and integrality proofs; the all-sublattice polynomial is distinguished from the usual cyclic-sublattice polynomial.
- Jiří Lebl, [*Guide to Cultivating Complex Analysis*](https://www.jirka.org/ca/ca.pdf), version 1.9, July 11, 2026: Theorems 3.3.4, 3.3.10 and 5.3.2. Copyright © 2019–2026 Jiří Lebl; actual dual CC BY-NC-SA 4.0 / CC BY-SA 4.0, with CC BY-SA used for linked author proofs.
- Vincent Bosser, [*Indépendance algébrique de valeurs de séries d'Eisenstein (théorème de Nesterenko)*](https://bosser.users.lmno.cnrs.fr/articles/art4.pdf), Séminaires & Congrès 12 (2005), 119–178: §2 for the auxiliary-function strategy, §4 for the multiplicity problem. The construction and residue proof in section 8 are supplied here with their own coefficient bounds.
- Gal Binyamini, [*Multiplicity estimates, analytic cycles and Newton polytopes*](https://arxiv.org/abs/1407.1183v2), version 2, November 19, 2014: §2, Lemma 8 and Proposition 9, for local intersections along a trajectory; §3 for the forest of proper intersections. Section 10 supplies the degree argument and the needed bounded escape lemma, using a primary-component chain rather than importing a multiplicity estimate for nonsingular vector fields.
- The Stacks Project, linked geometric and local algebra proofs in section 10: copyright the Stacks Project authors, GNU Free Documentation License 1.2 or later. Their linked proofs retain that licence.

- Patrice Philippon, [*Critères pour l’indépendance algébrique*](https://www.numdam.org/item/PMIHES_1986__64__5_0.pdf), Publications mathématiques de l’IHES 64 (1986), 5–52: Corollary 0.1 and the general criterion in Theorem 2.11. Section 11 supplies the one-variable resultant argument, controlled finite-extension norm and the complete higher-dimensional criterion for the two-sided auxiliary bounds. The proof of Theorem 9.34 defines its intersection forms and polynomial measures, proves both proximity estimates and the fixed-surface determinant height bound, and cuts to a zero-dimensional contradiction using the empty zero neighbourhood. The original general criterion allows finitely many zeros there and needs an additional stabilization argument. Actual source locators are Part I §§2–3, printed12–26, and Part II §1, printed27–38, and §3; that stronger general theorem is credited rather than imported.

- Annette Huber and Gisbert Wüstholz, [*Transcendence and Linear Relations of 1-Periods*](https://arxiv.org/abs/1805.10104v8), Cambridge Tracts in Mathematics 227, Cambridge University Press, 2022: Theorems 6.1–6.3 and Remark 6.4 for the exact subgroup theorem; Theorem 15.3, Theorem 16.2 and Proposition 16.5(1)–(2) for the pure period-space input; §18.1–18.2 for comparison with classical elliptic periods. The author manuscript, arXiv:1805.10104v8, April 21, 2022, has the same numbered period results with different pagination; Theorem 16.2 and Proposition 16.5(1)–(2) give their proofs and dimension calculations. The subgroup and period-space prerequisites are specified in Section 13.

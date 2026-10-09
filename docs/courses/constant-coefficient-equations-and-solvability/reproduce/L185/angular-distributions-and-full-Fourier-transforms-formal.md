# Angular distributions and their full Fourier transforms

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A homogeneous distribution can have a singular angular part and a singular radial part. Its Fourier transform must retain both. In particular, negative radial exponents can produce derivatives of a delta distribution in frequency; omitting the frequency origin would lose those terms.

This chapter proves the angular Fourier formula for every integer exponent, in every dimension, with arbitrary distributional angular data. Its meaning is an exact pairing with Schwartz tests. The proof keeps the sphere measure, the factor one half from the two radial directions, and the phase of the one-dimensional Fourier transform.

Basic references are the preceding chapters [Homogeneous extensions and angular moments][H], [Finite parts of singular powers][P], [Complex powers at a boundary][B], and [Schwartz functions and Fourier inversion][F]. Theorems 1.2, 3.1 and 5.1 of [H] give the angular representation and the unique parity-preserving homogeneous extension. Proposition 5.1 of [P] fixes the symmetric finite parts. Theorem 2.1 and Corollary 3.2 of [B] give their boundary and Fourier normalization. Sections 1–5 of [F] supply Schwartz seminorms, compact-test density and the transposed Fourier identities. We reuse those exact proofs and prove the remaining Radon-transform argument here.

## 1. The radial extension already fixes the origin

We use complex-linear distributional pairings, without conjugation, and the conventions
\[
 \widehat\phi(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}\phi(x)\,dx,
 \qquad
 \langle\widehat u,\phi\rangle=\langle u,\widehat\phi\rangle.
 \tag{1}
\]
Let \(n\geq1\), \(k\in\mathbb Z\), and suppose \(u\in\mathcal S'(\mathbb R^n)\) is homogeneous of degree \(-n-k\) and has parity
\[
 u(-x)=(-1)^{k+1}u(x).
 \tag{2}
\]
The equality of distributions in (2) uses reflection of the test. For \(n=1\), the unit sphere \(S^0\) has its counting measure, with mass one at each of its two points.

The angular representation in [H], Theorem 1.2, gives a unique distribution \(T\) on \(S^{n-1}\) such that, for tests supported away from zero,
\[
 \langle u,\psi\rangle
 =T\left(\omega\longmapsto
            \int_0^\infty r^{-k-1}\psi(r\omega)\,dr\right).
 \tag{3}
\]
If \(u(r\omega)=r^{-n-k}g(\omega)\) is an ordinary function, then \(T(h)=\int_{S^{n-1}}g(\omega)h(\omega)\,dS(\omega)\). Thus \(T\) includes the usual, unnormalized Euclidean sphere measure. Reflection of (3) and uniqueness give
\[
 T(h(-\,\cdot))=(-1)^{k+1}T(h).
 \tag{4}
\]

Define the tempered distribution on the real radial line
\[
 P_k(r)=
 \begin{cases}
  \operatorname{pf}(r^{-k-1}),&k\geq0,\\
  r^{-k-1},&k<0,
 \end{cases}
 \qquad
 \operatorname{pf}(r^{-k-1})
       =\dfrac{(-1)^k}{k!}\partial_r^k
                         \operatorname{pv}\dfrac1r .
 \tag{5}
\]
The finite part in (5) is the symmetric finite part of [P], Proposition 5.1; it is not a one-sided finite part with an independently chosen contact term.

**Proposition 1.1.** On every Schwartz test,
\[
 \langle u,\psi\rangle
 =\frac12 T\left(\omega\longmapsto
                  \langle P_k(r),\psi(r\omega)\rangle\right).
 \tag{6}
\]
The right side is a continuous tempered distribution for every angular \(T\) satisfying (4).

**Proof.** Formula (6) on compact smooth tests is exactly [H], Theorem 5.1, with its integer \(\ell=-k-1\). That theorem proves both existence and uniqueness at the origin: when \(k\geq0\), opposite parity annihilates the degree-\(k\) angular moments and eliminates every order-\(k\) point jet. When \(k<0\), the degree \(-n-k\) is nonresonant, and Theorem 3.1 gives uniqueness.

We verify the passage to Schwartz tests. In any compact sphere-coordinate chart, differentiation of \(\psi(r\omega)\) with respect to \(r\) and the angular coordinates gives a finite sum of derivatives of \(\psi\), multiplied by polynomials in \(r\) whose degrees are at most the angular derivative order. Derivatives of the chart coefficients are bounded on the compact chart. Consequently, for all nonnegative integers \(M,a,b\), every line Schwartz seminorm of every angular derivative of order at most \(b\) is bounded by a finite sum of seminorms
\[
 \sup_x(1+|x|)^{M+b}|\partial^\gamma\psi(x)|,
 \qquad |\gamma|\leq a+b.
 \tag{7}
\]
A finite sphere-chart cover suffices. For \(S^0\), this is just the two restrictions \(\psi(r)\) and \(\psi(-r)\).

The tempered bound for \(P_k\) therefore makes the angular function in (6) smooth, with every sphere seminorm bounded by finitely many Schwartz seminorms of \(\psi\). To justify each angular derivative, take its difference quotient in a slightly larger compact chart. The fundamental theorem expresses the remainder as an integral of the next derivative. On a bounded \(r\)-interval that remainder tends uniformly to zero with every fixed derivative, by uniform continuity. Outside that interval, (7) with one additional Schwartz weight makes the requested weighted seminorm uniformly small as the interval grows. This proves convergence in every line Schwartz seminorm. Applying the continuous functional \(P_k\) gives the asserted derivative. Iteration covers every order.

The angular distribution \(T\) has a bound by finitely many sphere derivatives. Combining it with (7) proves continuity of the right side on \(\mathcal S\). It agrees with \(u\) on compact smooth tests. Those tests are dense in \(\mathcal S\), by [F], Section 1, so the two continuous functionals agree everywhere. \(\square\)

The factor \(1/2\) is essential. On the punctured space, substitute \(r=-s\) on the negative half-line. The parity of \(P_k\) is \((-1)^{k+1}\), and (4) supplies the same sign from the angular distribution. Their product is one, so the negative radial half contributes exactly the positive half. Formula (6) divides this double count by two.

## 2. The complete one-dimensional transform

Put
\[
 \sigma_k(t)=
 \begin{cases}
  \dfrac{\operatorname{sgn}(t)t^k}{2k!},&k\geq0,\\[4pt]
  \delta_0^{(-k-1)}(t),&k<0.
 \end{cases}
 \tag{8}
\]
For negative \(k\), the right side is a delta derivative on the entire line, not a function defined only away from zero.

**Proposition 2.1.** With the convention (1) in dimension one,
\[
 \widehat P_k=2\pi i^{-1-k}\sigma_k
                    \quad\hbox{in }\mathcal S'(\mathbb R).
 \tag{9}
\]

**Proof.** The exact boundary formulas in [B], Theorem 2.1, give
\[
 \frac12\left((r+i0)^{-1}+(r-i0)^{-1}\right)
                    =\operatorname{pv}\frac1r .
 \tag{10}
\]
Its Corollary 3.2 gives the transforms of those two boundary values as \(-2\pi iH(t)\) and \(2\pi iH(-t)\), respectively. Here \(H\) is the Heaviside distribution. Therefore
\[
 \mathcal F\left(\operatorname{pv}\frac1r\right)
  =\pi i\bigl(H(-t)-H(t)\bigr)
  =-i\pi\operatorname{sgn}(t).
 \tag{11}
\]
All these equalities hold on Schwartz tests, including tests meeting zero.

For \(k\geq0\), transform the derivative formula (5), using [F], Section 5:
\[
 \widehat P_k
 =\frac{(-1)^k}{k!}(it)^k(-i\pi\operatorname{sgn}t)
 =\frac{\pi i^{-1-k}}{k!}t^k\operatorname{sgn}t.
 \tag{12}
\]
The last phase identity follows from \((-1)^k i^k=i^{-k}\). Equations (8) and (12) give (9).

For \(k<0\), set \(j=-k-1\geq0\). The same Fourier foundation proves \(\mathcal F1=2\pi\delta_0\) and \(\mathcal F(r v)=i\partial_t\mathcal Fv\). Applying it \(j\) times gives
\[
 \mathcal F(r^j)=2\pi i^j\delta_0^{(j)}.
 \tag{13}
\]
This is again (9), with \(j=-k-1\). Every integer is covered. \(\square\)

## 3. Hyperplane averages are smooth angular tests

For a unit vector \(\omega\) and \(\phi\in\mathcal S(\mathbb R^n)\), define its hyperplane average
\[
 \mathcal R_\omega\phi(t)
 =\int_{\omega^\perp}\phi(t\omega+y)\,dy ,
 \tag{14}
\]
where \(dy\) is the Euclidean measure on \(\omega^\perp\). When \(n=1\), the zero-dimensional integral has its single-point mass one, so \(\mathcal R_\omega\phi(t)=\phi(t\omega)\).

**Lemma 3.1.** The map \(\omega\mapsto\mathcal R_\omega\phi\) is a smooth sphere-valued family of line Schwartz functions. Every seminorm of this family is bounded by finitely many Schwartz seminorms of \(\phi\). Its one-dimensional Fourier transform satisfies
\[
 \widehat{\mathcal R_\omega\phi}(r)=\widehat\phi(r\omega).
 \tag{15}
\]

**Proof.** Near any fixed unit vector, choose a smooth orthonormal frame for its perpendicular plane. One construction projects a fixed independent set of \(n-1\) vectors onto the nearby perpendicular planes and applies Gram–Schmidt. Independence persists on a smaller neighborhood, and all divisions and positive square roots are of positive smooth functions there. Appending \(\omega\) gives a smooth orthogonal matrix \(Q_\omega\). In that chart,
\[
 \mathcal R_\omega\phi(t)
    =\int_{\mathbb R^{n-1}}\phi(Q_\omega(y,t))\,dy .
 \tag{16}
\]
Orthogonality gives \(|Q_\omega(y,t)|=\sqrt{|y|^2+t^2}\). Any angular derivative of order \(b\) and \(t\)-derivative of order \(a\) of the integrand is a finite sum bounded by
\[
 C(1+|y|+|t|)^b
        \max_{|\gamma|\leq a+b}
              |\partial^\gamma\phi(Q_\omega(y,t))|,
 \tag{17}
\]
uniformly on a smaller compact chart. Choose a Schwartz weight \(M\) and use
\[
 1+\sqrt{|y|^2+t^2}\ \geq\
                  2^{-1/2}(1+|y|+|t|).
 \tag{18}
\]
For \(L=M-b>n-1\), the absolute derivative integral is bounded by a constant times a finite Schwartz seminorm of \(\phi\), multiplied by
\[
 \int_{\mathbb R^{n-1}}(1+|t|+|y|)^{-L}\,dy
       =C_L(1+|t|)^{n-1-L}.
 \tag{19}
\]
The equality follows from \(y=(1+|t|)z\); the constant is finite because \(L>n-1\). Finiteness can also be checked by shells: the region \(2^j\leq|z|<2^{j+1}\) has volume at most \(C2^{j(n-1)}\), while the integrand is at most \(2^{-jL}\), giving a convergent geometric series. Choosing \(M>b+n-1+N\) proves every requested weight \((1+|t|)^N\).

The same majorants justify differentiation under the integral. More explicitly, the fundamental-theorem remainder for each parameter difference quotient is bounded by (17) with one additional derivative and a sufficiently larger weight. On \(|t|+|y|\leq R\), uniform continuity gives uniform convergence with every fixed derivative. On its complement, one additional weight beyond the integrable bound (19) makes the weighted integral tail uniformly tend to zero as \(R\) grows. This proves convergence of the quotient in every line Schwartz seminorm. Repeating proves smoothness with values in the line Schwartz space. A finite compact chart cover proves the global assertion. The case \(n=1\) is immediate.

Finally \(\phi\) is absolutely integrable, and (16) with the orthogonal change of variables \(\xi=Q_\omega(y,t)\) gives
\[
 \int_{\mathbb R}e^{-irt}\mathcal R_\omega\phi(t)\,dt
       =\int_{\mathbb R^n}e^{-ir\omega\cdot\xi}\phi(\xi)\,d\xi .
 \tag{20}
\]
Fubini and this measure-preserving substitution are valid for the absolute integrand \(|\phi|\). This proves (15). \(\square\)

In particular, the function
\[
 J_{k,\phi}(\omega)
        =\langle\sigma_k(t),\mathcal R_\omega\phi(t)\rangle
 \tag{21}
\]
is smooth, and every sphere seminorm is bounded by finitely many Schwartz seminorms of \(\phi\). For \(k\geq0\) this uses the polynomial growth of the locally integrable function in (8); for \(k<0\) it is evaluation of a fixed derivative of (14) at zero. No multiplication of arbitrary angular distributions is used in defining (21).

## 4. The angular Fourier identity on the whole frequency space

**Theorem 4.1.** Under (2), with the angular distribution \(T\) of (3),
\[
 \langle\widehat u,\phi\rangle
       =\pi i^{-1-k}\,T(J_{k,\phi}),
          \qquad \phi\in\mathcal S(\mathbb R^n).
 \tag{22}
\]
Equivalently,
\[
 \widehat u(\xi)
  =\pi i^{-1-k}
        \int_{S^{n-1}}u(\omega)\,
                         \sigma_k(\omega\cdot\xi)\,dS(\omega).
 \tag{23}
\]
The integral in (23) means exactly the test pairing (21)–(22). It is a tempered distribution on all of \(\mathbb R^n\), including its origin.

**Proof.** Apply (6) to the Schwartz function \(\widehat\phi\), then use (15) and the one-dimensional distributional Fourier transpose:
\[
 \begin{aligned}
 \langle\widehat u,\phi\rangle
 &=\frac12 T\left(\omega\longmapsto
                    \langle P_k(r),\widehat\phi(r\omega)\rangle\right)\\
 &=\frac12 T\left(\omega\longmapsto
           \langle P_k,\widehat{\mathcal R_\omega\phi}\rangle\right)\\
 &=\frac12 T\left(\omega\longmapsto
                     \langle\widehat P_k,\mathcal R_\omega\phi\rangle\right)\\
 &=\pi i^{-1-k}T(J_{k,\phi}).
 \end{aligned}
 \tag{24}
\]
Proposition 1.1 and Lemma 3.1 show that every angular function in these lines is smooth, with the requisite finite seminorm bounds. Proposition 2.1 supplies the last equality with its exact phase. These are equalities of test pairings, so there is no unproved interchange of two singular distributions. The bounds after (21) also directly prove tempered continuity of the last line. \(\square\)

When \(T\) has a smooth density, (22) is the ordinary sphere pairing of that density with the distribution \(\sigma_k(\omega\cdot\xi)\), tested first in \(\xi\). For arbitrary \(T\), (21) is the corresponding smooth angular test and remains the definition. General wavefront estimates for sphere restriction, distribution products and projection integration are additional assertions. The identity (22) itself has been proved without assuming those estimates or analytic Euler regularity.

**Proposition 4.2 (continuity and scaling).** For fixed \(k\), the maps from angular distributions satisfying (4) to \(u\) and to \(\widehat u\) are continuous for both weak and strong distribution topologies. The Fourier transform is homogeneous of degree \(k\) and has the same reflection parity as \(u\).

**Proof.** Weak convergence is convergence after pairing with each smooth angular test. Formula (6) uses one such test for each \(\psi\), and (22) uses one for each \(\phi\), so both preserve weak convergence.

The strong dual topology uses seminorms \(\sup_{\psi\in B}|u(\psi)|\) over bounded Schwartz-test sets, and the corresponding seminorms over bounded smooth sphere-test sets. Estimates (7) and those after (21) send every bounded Schwartz set to a set bounded in every smooth sphere seminorm. Transposition therefore bounds each output strong seminorm by one input strong seminorm, proving strong continuity.

For scaling, write \(D_tu(\psi)=t^{-n}u(\psi(\,\cdot/t))\). The Fourier test substitution gives
\[
 \mathcal F(D_tu)=t^{-n}D_{1/t}\widehat u.
 \tag{25}
\]
Combine this with \(D_tu=t^{-n-k}u\); setting \(s=1/t\) gives \(D_s\widehat u=s^k\widehat u\). Reflection commutes with Fourier transformation by [F], Section 5, so (2) gives the same parity for \(\widehat u\). \(\square\)

Opposite parity is a real hypothesis. In dimension one, \(\delta_0\) is homogeneous of degree \(-1\), but its angular distribution is zero and its transform is the nonzero constant one. It has even parity, whereas \(k=0\) requires odd parity. Dropping parity from Theorem 4.1 would therefore give a false identity.

## References

[H] [Homogeneous extensions and angular moments][H], Theorems 1.2, 3.1 and 5.1, with the angular foundations linked there.

[P] [Finite parts of singular powers][P], Proposition 5.1 and its complete proof.

[B] [Complex powers at a boundary][B], Theorem 2.1 and Corollary 3.2, with the normalized boundary proof preceding them.

[F] [Schwartz functions and Fourier inversion][F], Sections 1–5, including compact-test density and all transposed identities.

The linked programme proofs retain their original provenance and CC0 notices. This chapter's Radon-transform argument and exposition are original CC0 text. General analytic-wavefront estimates remain additional mathematical prerequisites.

[H]: https://github.com/KokunoYumeto/open-math-courses-public/blob/a1dbde19825087b59ffadcbed96c2cfa65d047c3/docs/courses/AN-01/src/homogeneous-extensions-and-angular-moments.md
[P]: https://github.com/KokunoYumeto/open-math-courses-public/blob/a1dbde19825087b59ffadcbed96c2cfa65d047c3/docs/courses/AN-01/src/finite-parts-of-singular-powers.md
[B]: https://github.com/KokunoYumeto/open-math-courses-public/blob/a1dbde19825087b59ffadcbed96c2cfa65d047c3/docs/courses/AN-01/src/complex-powers-at-a-boundary.md
[F]: https://github.com/KokunoYumeto/open-math-courses-public/blob/a1dbde19825087b59ffadcbed96c2cfa65d047c3/docs/courses/AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md

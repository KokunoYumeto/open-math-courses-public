# Multiplicity one, strong multiplicity one and the converse theorem

A representation can occur only once, yet still be difficult to identify from incomplete local data. Weak multiplicity one controls the first question. Strong multiplicity one answers the second: for cuspidal representations of \(\mathrm{GL}_2\), finitely many missing local components cannot hide a different representation. The converse theorem asks a third question, whether a proposed collection of local representations comes from cusp forms at all.

We work over \(\mathbb Q\), with \(G=\mathrm{GL}_2\), \(d(a)=\operatorname{diag}(a,1)\), \(n(x)=\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)\), and
\[
w_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The character \(\psi=\prod_v\psi_v\) is trivial on \(\mathbb Q\), with \(\psi_\infty(x)=e^{2\pi ix}\) and \(\psi_p(x)=e^{-2\pi i\{x\}_p}\). Give \(\mathbb Q\backslash\mathbb A\) volume one. Finite unit groups have multiplicative volume one.

The cuspidal space \(\mathcal A_0(\omega)\) consists of smooth finite-level, \(K_\infty\)-finite, infinitesimally finite automorphic cusp forms with central character \(\omega\). Its representation structure is the \((\mathfrak g,K_\infty)\times G(\mathbb A_f)\) structure of Lesson 12. At infinity, a Whittaker model means the moderate-growth smooth realization specified in Lesson 11, §5; it does not mean that arbitrary real translations preserve the space of \(K_\infty\)-finite vectors.

Completed \(L\)-functions, contragredients and epsilon factors have the normalization of Lesson 14:
\[
\begin{gathered}
L(s,\pi)=\prod_v L(s,\pi_v),\\
\gamma(s,\pi_v,\psi_v)
 =\epsilon(s,\pi_v,\psi_v)
   \frac{L(1-s,\widetilde\pi_v)}{L(s,\pi_v)},\\
L(s,\pi)=\epsilon(s,\pi)L(1-s,\widetilde\pi).
\end{gathered}
\tag{0.1}
\]
The global epsilon factor is a finite product of nontrivial local factors. It is independent of the choice of a *coherent* character of \(\mathbb A/\mathbb Q\). This does not permit changing one local character while holding all the others fixed.

## 1. Reconstructing a cusp form from one Whittaker function

For \(\phi\in\mathcal A_0(\omega)\), put
\[
W_\phi(g)=
 \int_{\mathbb Q\backslash\mathbb A}
 \phi(n(x)g)\psi(-x)\,dx.
\tag{1.1}
\]

**Theorem 1.1 — injectivity.** The map \(\phi\mapsto W_\phi\), where \(W_\phi\) is retained as a function on \(G(\mathbb A)\), is injective.

**Proof.** For fixed \(g\), consider \(x\mapsto\phi(n(x)g)\) on the compact additive quotient. Its constant coefficient is zero by cuspidality. Its coefficient at the character \(x\mapsto\psi(\alpha x)\), \(\alpha\in\mathbb Q^\times\), is
\[
c_\alpha(g)
 =\int_{\mathbb Q\backslash\mathbb A}
     \phi(n(x)g)\psi(-\alpha x)\,dx
 =W_\phi(d(\alpha)g).
\tag{1.2}
\]
For the last equality, substitute \(t=\alpha x\), use
\(d(\alpha)n(x)=n(\alpha x)d(\alpha)\), and use left rational invariance. Multiplication by \(\alpha\) preserves the quotient measure because the adelic product of its local absolute values is one.

Lesson 14, Theorem 1.1, proves the required convergence: finite additive level reduces this Fourier expansion to a smooth circle expansion, and repeated integration by parts makes it absolutely convergent, uniformly on compact sets of \(g\). Evaluating at \(x=0\) therefore gives
\[
\phi(g)=
 \sum_{\alpha\in\mathbb Q^\times}
       W_\phi(d(\alpha)g).
\tag{1.3}
\]
If \(W_\phi\) is the zero function, every summand is zero for every \(g\), so \(\phi=0\). \(\square\)

The functional \(\phi\mapsto W_\phi(1)\) alone need not be injective. A vector can have that one coefficient zero and have other coefficients nonzero. The theorem uses the full function, including all its translates.

The map also respects the right action:
\[
W_{R(h)\phi}(g)=W_\phi(gh).
\tag{1.4}
\]
At the real place this identity is interpreted in the smooth realization; restricting to the admissible module gives the corresponding Lie algebra, compact-group and Hecke actions.

## 2. Why the same representation cannot occur twice

**Theorem 2.1 — weak multiplicity one.** For an irreducible admissible representation \(V\),
\[
\dim_{\mathbb C}
 \operatorname{Hom}_{(\mathfrak g,K_\infty)\times G(\mathbb A_f)}
       (V,\mathcal A_0(\omega))\leq1.
\tag{2.1}
\]
Consequently each irreducible cuspidal representation occurs with multiplicity one.

**Proof.** A nonzero map from \(V\) is injective, since its kernel is invariant. If there is no such map, (2.1) is immediate. Otherwise Lesson 12, Theorem 6.1, writes \(V\) as a restricted tensor product \(\bigotimes'_v V_v\).

Fix one local Whittaker model for each \(V_v\), using \(\psi_v\). At almost all finite places choose the spherical vector and normalize its Whittaker function to take value one at the identity. These choices fix a global product model on the algebraic restricted tensor product.

For an embedding \(j:V\to\mathcal A_0(\omega)\), the map
\[
T_j:V\longrightarrow \{\text{Whittaker functions}\},
\qquad T_j(\xi)=W_{j(\xi)}
\tag{2.2}
\]
is nonzero and injective by Theorem 1.1. The factorization proof in Lesson 14, Theorem 2.1, shows that it is a scalar multiple of the fixed product map. Here the scalar is attached to the embedding, not to each vector separately.

To recall why this distinction is justified, fix all tensor entries except one. Local uniqueness makes the resulting function-valued intertwining map proportional to the chosen local map. Apply this successively to the finitely many entries that differ from the reference tensor. The resulting multilinear identity uses the same scalar as its value on that reference tensor. Every vector is a finite sum of such pure tensors, so linearity preserves this scalar. At infinity this uses the analytic uniqueness input of Lesson 11, §5, exactly as in Lesson 14; it does not apply unipotent translations to an abstract Harish-Chandra module.

Thus two nonzero embeddings \(j_1,j_2\) satisfy
\[
W_{j_1(\xi)}=c\,W_{j_2(\xi)}
\quad\text{for every }\xi\in V
\tag{2.3}
\]
with one nonzero constant \(c\). Fourier reconstruction gives
\(j_1(\xi)=c\,j_2(\xi)\) for every \(\xi\). All nonzero maps lie on one line, proving (2.1). A cuspidal representation, by definition, has a nonzero occurrence, so its multiplicity is exactly one. \(\square\)

A level-fixed subspace can still have dimension greater than one. It consists of different vectors inside this one occurrence. The oldform calculation in §5.3 will exhibit this distinction.

## 3. Identifying a representation from almost all places

**Theorem 3.1 — strong multiplicity one for \(\mathrm{GL}_2/\mathbb Q\).** Let \(\pi,\pi'\) be irreducible cuspidal automorphic representations. If
\[
\pi_v\simeq\pi'_v
\quad\text{outside a finite set of places},
\tag{3.1}
\]
then \(\pi\simeq\pi'\). Their realizations in the cuspidal space then agree by Theorem 2.1.

The theorem makes no assumption that the two central characters were specified in advance. That equality follows from (3.1). Let \(\eta=\omega_\pi/\omega_{\pi'}\), and let \(S\) contain all places where the components might differ. Then \(\eta_v=1\) outside \(S\), and rational invariance says
\[
\prod_{v\in S}\eta_v(r)=1
\qquad(r\in\mathbb Q^\times).
\tag{3.2}
\]
Weak approximation makes \(\mathbb Q^\times\) dense in
\(\prod_{v\in S}\mathbb Q_v^\times\). For this density over \(\mathbb Q\), clear the denominators in the finite targets, choose an arbitrarily large auxiliary denominator coprime to the primes in \(S\), and use the Chinese remainder theorem for the required finite congruences. Adding multiples of their common modulus to the numerator gives a real arithmetic progression whose step tends to zero with the auxiliary denominator. It therefore approximates any real target while retaining the finite congruences. Choosing small neighborhoods of the nonzero targets keeps every coordinate nonzero. The continuous character in (3.2) is therefore trivial on that product. Varying just one component proves \(\eta_v=1\) for every \(v\).

Weak multiplicity one cannot finish the argument: it compares embeddings of an already known common representation. We must recover the missing local components first.

For unitary \(\pi,\pi'\), a complete argument is given in Solution 7.4. Its analytic starting point is the family of twisted functional equations from Lesson 14. The equations determine a finite product of missing local gamma-factor ratios. Distinct prime periods and the real gamma poles separate these factors; the Kirillov model fixes their remaining constants. The local converse theorem of Lesson 9, Theorem 7.1, then recovers the representations.

The usual essentially unitary version reduces to this one. A smooth idele-class quasicharacter has the form \(|\cdot|^{2a}\omega_0\), with \(a\in\mathbb R\) and \(\omega_0\) unitary. Equality of central characters gives the same \(a\) for both representations. Twisting both by \(|\det|^{-a}\) gives unitary central character; cuspidal rapid decay and the finite-vector comparison of Lessons 3–4 give their unitary cuspidal realizations. Apply the unitary theorem and undo the common twist.

## 4. When proposed local data become automorphic

### 4.1. An exact sufficient converse theorem

**Theorem 4.1 — Jacquet–Langlands converse theorem.** Let
\(\pi=\bigotimes'_v\pi_v\) be an irreducible admissible restricted tensor product for \(G(\mathbb A)\). Assume:

1. Every \(\pi_v\) is infinite-dimensional and generic. At the real place use its moderate-growth smooth realization, with a continuous Whittaker functional.
2. Its central quasicharacter \(\omega_\pi:\mathbb A^\times\to\mathbb C^\times\) is trivial on \(\mathbb Q^\times\).
3. Outside a finite set, \(\pi_p\) is an unramified principal series with Satake parameters \(\alpha_p,\beta_p\). There is one \(C\geq0\) such that
   \[
   p^{-C}\leq|\alpha_p|,|\beta_p|\leq p^C
   \tag{4.1}
   \]
   at all these primes.
4. For every unitary idele-class character \(\chi\), the completed products
   \(L(s,\pi\otimes\chi)\) and
   \(L(s,\widetilde\pi\otimes\chi^{-1})\), initially defined in a right half-plane, extend to entire functions bounded on every closed vertical strip of finite width, and satisfy
   \[
   \begin{gathered}
   L(s,\pi\otimes\chi)=
    \epsilon(s,\pi\otimes\chi)
    L(1-s,\widetilde\pi\otimes\chi^{-1}),\\
   \epsilon(s,\pi\otimes\chi)=
       \prod_v\epsilon(s,\pi_v\otimes\chi_v,\psi_v).
   \end{gathered}
   \tag{4.2}
   \]

Then the given \(\pi\) has a cuspidal automorphic realization.

This is the rational-field case of Jacquet–Langlands, §11, Theorem 11.3, printed pp. 185–186. We prove the convergence, strip estimate, Mellin uniqueness and automorphic construction below, using the exact local models and factor calculations of Lessons 7, 9 and 11.

Condition (4.1) also bounds the inverse Satake parameters of the contragredient. For a unitary \(\chi\), its good unramified values have modulus one, so both Euler products converge absolutely when \(\operatorname{Re}s>C+1\), after increasing the initial half-plane to accommodate the finitely many exceptional factors. This supplies a well-defined initial analytic object. It is not a Ramanujan hypothesis.

Jacquet–Langlands use all idele-class quasicharacters. The formulation above is equivalent: every such character is a unitary character times a real power of the norm, and that power replaces \(s\) by \(s+a\). Entire continuation, boundedness on all finite-width strips and the functional equation transfer under that replacement.

Local genericity is essential to this statement. One-dimensional determinant characters cannot be inserted as missing local factors and then be recovered by a Whittaker-series construction. Central-character compatibility is also required before any rationally invariant function can exist.


### 4.2. Convergence of the proposed Fourier expansion

Choose spherical Whittaker functions \(W_p\), normalized by \(W_p(1)=1\), outside a finite set. For a product vector \(W\), define
\[
\Phi_W(g)=
 \sum_{\alpha\in\mathbb Q^\times}W(d(\alpha)g).
\tag{4.3}
\]

**Lemma 4.2 — uniform convergence and growth.** The series and all its real right derivatives converge absolutely and uniformly on compact sets of \(g\). With finite components and real rotation components in fixed compact sets, it decreases faster than every inverse power as the real diagonal height tends to infinity. Near zero on that diagonal it has at most polynomial growth.

**Proof.** A compact subset of \(G(\mathbb A)\) lies in a finite product of compact local sets, with tail \(\prod_{p\notin S}K_p\). Enlarge \(S\) to contain all nonspherical factors of \(W\). At a good prime, Lesson 13's spherical formula is
\[
W_p(d(p^n))=
 \begin{cases}
 p^{-n/2}\displaystyle\sum_{j=0}^{n}\alpha_p^{n-j}\beta_p^j
       &n\geq0,\\
 0&n<0 .
 \end{cases}
\]
At a prime in \(S\), the Kirillov functions of Lesson 7 vanish for valuations sufficiently negative; near zero their germs are finite sums of character powers times polynomials in the valuation. They are therefore bounded by a power of \(p^{v_p(\alpha)}\), after enlarging the power to absorb the valuation polynomials. These bounds are uniform for compact local translates: smoothness makes a compact set's orbit of a fixed vector finite.

A nonzero summand consequently has \(\alpha=m/M\), \(m\in\mathbb Z\setminus\{0\}\), for one fixed positive integer \(M\). Its finite part satisfies
\[
\left|\prod_{p<\infty}W_p(d(m/M)g_p)\right|
 \leq A(1+|m|)^B .
\tag{4.5}
\]
Indeed (4.1) bounds a good-prime factor by \((n+1)p^{(C-1/2)n}\). The product of \(n+1\) is the divisor count of an integer dividing \(|m|\), up to fixed primes in \(M\). Its elementary bound by that integer gives a polynomial in \(|m|\). The finitely many bad-prime powers give another polynomial.

For the real estimate, including smooth translates, write
\(W_v(d(y))=\lambda(\pi(d(y))v)\), with \(\lambda\) continuous. Moderate growth supplies a continuous seminorm \(p\), a constant \(A_0\), and an integer \(N\) such that
\[
|W_v(d(y))|\leq A_0\max(|y|,|y|^{-1})^N p(v).
\]
Let \(X\) generate the upper unipotent group. Whittaker covariance gives
\[
W_{X^jv}(d(y))=(2\pi iy)^jW_v(d(y)).
\]
The same group-growth exponent \(N\) applies to \(X^jv\); only the seminorm of the vector changes. Choosing \(j>N+R\) therefore gives, for \(|y|\geq1\),
\[
|W_v(d(y))|\leq A_R |y|^{-R}p(X^jv).
\tag{4.6}
\]
These seminorms are uniformly bounded for \(v=\pi(g_\infty)v_0\) with \(g_\infty\) in a compact set. The same argument applies to any fixed right derivative.

Combining (4.5) and (4.6), with \(R>B+2\), gives a summable majorant for the tail in \(|m|\). The remaining finite set of terms is bounded on compact sets. This proves local uniform convergence and differentiation.

In a cusp chart \(n(x)d(t)k_\infty\), the unipotent factor contributes \(\psi_\infty(\alpha x)\), of modulus one, so the bounds are uniform in \(x\). For real height \(t\geq M\), every \(|m|t/M\geq1\), so arbitrarily large \(R\) give \(O(t^{-R})\). For \(0<t\leq1\), enlarge the small-\(y\) exponent to \(A>B+2\). The real estimates give \(|W_v(d(y))|\leq A'|y|^{-A}\) for all \(y\ne0\), since the large-\(y\) part decreases rapidly. Summing \((1+|m|)^B(|m|t/M)^{-A}\) gives \(O(t^{-A})\). All bounds are uniform on the specified compact sets. \(\square\)

For a finite sum of product vectors, add the finitely many bounds. The construction is smooth, has finite finite-place level, and commutes with the right Lie, compact-group and finite Hecke actions.

### 4.3. Mellin integrals of smooth real translates

The converse proof uses \(W(\,\cdot\,g)\), which need not be \(K_\infty\)-finite. We record the analytic extension of the real calculations before using that translate.

**Lemma 4.3 — normalized smooth Mellin integrals.** In the real smooth model used above,
\[
F_v(s)=
 \frac{\displaystyle\int_{\mathbb R^\times}
             W_v(d(y))|y|^{s-1/2}d^\times y}
      {L(s,\pi_\infty)}
\tag{4.7}
\]
extends to an entire function. The local functional equation of Lesson 11 holds for every smooth vector. On any finite-width strip and for every \(\delta>0\),
\[
|F_v(\sigma+i\tau)|
 \leq A_{\delta,v}\exp(\delta\tau^2).
\tag{4.8}
\]
The assertions hold also for a fixed character twist and its contragredient.

**Proof.** The smooth compact principal realization of Lesson 11 has Fourier expansion
\(v=\sum_n c_nv_n\), with \(c_n\) decreasing faster than every power of \(|n|\). Each seminorm of its normalized rotation vectors \(v_n\) grows at most polynomially: the compact model's seminorms use finitely many derivatives on the circle. The discrete-series submodules and quotients have the corresponding half-ladders and reflected half-ladders. For the discrete ladder, Lesson 11, equation (4.2), gives \(h_{k+2j}/h_k=j!/(k)_j\), a polynomial upper and lower bound in \(1+j\); the same product estimate applies to its equation (4.1). Changing between its compact and unit-norm bases thus multiplies coefficients by at most a fixed power of \(1+j\). Thus finite Fourier sums converge in the smooth topology, and the seminorm estimates below are polynomial in the weight.

For a rotation vector, Lessons 11, Theorems 5.1 and 6.1, show that (4.7) is a polynomial in \(s\); call it \(F_n(s)\). Choose lines \(a<b\) so far apart that the original Mellin integral converges absolutely on \(b+i\mathbb R\), and the dual integral converges absolutely at \(1-a-i\mathbb R\). The real argument of Lemma 4.2 bounds these integrals polynomially in \(|n|\), uniformly in \(\tau\). Near zero use its fixed moderate-growth exponent. At infinity use one fixed \(X\)-derivative order sufficient for the chosen line. The seminorms of \(v_n\) in these estimates remain polynomial.

The reciprocal gamma factor has at most exponential growth on either line. For a rough bound, use
\(\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)\),
\(\Gamma(z+1)=z\Gamma(z)\), and
\(|\Gamma(\sigma+i\tau)|\leq\Gamma(\sigma)\) for \(\sigma>0\).
Shift \(z\) by a fixed integer so \(\operatorname{Re}(1-z)>0\), apply reflection there, and use the recurrence. For \(|\tau|\geq1\), the recurrence denominators have modulus at least one, and the sine factor is \(O(e^{\pi|\tau|})\). For \(|\tau|\leq1\), use compactness and the fact that \(1/\Gamma\) is entire. This gives
\(|1/\Gamma(z)|\leq A e^{A'|\operatorname{Im}z|}\) on each finite-width strip, and hence the same kind of bound for \(\Gamma_{\mathbb R}\) and \(\Gamma_{\mathbb C}\).

On the left line use the finite-vector local functional equation already proved in Lesson 11. The real epsilon is constant in \(s\), and its Weyl element is a rotation, so it multiplies \(v_n\) by a scalar of modulus one. The dual integral gives the same estimate there. We have, on both lines,
\[
|F_n(s)|\leq A(1+|n|)^D e^{A'|\tau|},
\tag{4.9}
\]
with \(D,A,A'\) independent of \(n\).

Fix \(\delta>0\) and \(m=(a+b)/2\). Apply the maximum principle on rectangles to
\(F_n(s)e^{\delta(s-m)^2}\). Its horizontal edges tend to zero: for fixed \(n\), \(F_n\) is a polynomial and the multiplier contributes \(e^{-\delta\tau^2}\). On its vertical edges (4.9) is bounded by a constant times \((1+|n|)^D\), because \(e^{A'|\tau|-\delta\tau^2}\) is bounded. Therefore throughout the strip
\[
|F_n(s)|\leq A_\delta(1+|n|)^D e^{\delta\tau^2}.
\tag{4.10}
\]
The bounded real-coordinate factor has been absorbed into \(A_\delta\).

Multiply by \(c_n\) and sum. Rapid Fourier decrease gives local uniform convergence in \(s\); (4.10) gives (4.8). On the initial right half-plane, the series is the Mellin integral of \(v\), by the same seminorm bounds and dominated convergence. It is therefore its entire continuation. The dual integrals have locally uniform sums as well, so their finite-vector functional equations pass to the limit. This proves the equation for every smooth \(v\), including \(v=\pi(g_\infty)v_0\). \(\square\)

### 4.4. The global strip estimate

For an idele-class character \(\chi\), put
\[
Z_\chi(g,s)=
 \int_{\mathbb A^\times}
 W(d(a)g)\chi(a)|a|^{s-1/2}d^\times a.
\tag{4.11}
\]
In its initial right half-plane it converges absolutely, and unfolds to
\(\int_{C_{\mathbb Q}}\Phi_W(d(a)g)\chi(a)|a|^{s-1/2}d^\times a\).
Use the quotient measure compatible with this unfolding.

The local calculations give
\[
Z_\chi(g,s)=L(s,\pi\otimes\chi)
                  \prod_v F_{v,\chi}(g_v,s).
\tag{4.12}
\]
Almost all normalized factors are one. The exceptional finite factors are Laurent polynomials in \(p^{\pm s}\), by Lesson 9, hence bounded on finite-width strips. At infinity use Lemma 4.3. The expression is entire and, on each strip, satisfies the bound (4.8). The same assertions hold for its dual Weyl integral.

In fact \(Z_\chi(g,s)\) is bounded on every finite-width strip. Its absolutely convergent integral gives a uniform bound on a sufficiently far right line. The normalized local functional equations and (4.2) identify it with the dual Weyl integral at \(1-s\), giving a bound on a sufficiently far left line. In forming this identity, multiply only the finitely many nontrivial normalized integrals and epsilon factors, and then use the two completed \(L\)-functions; an infinite product of unnormalized gamma ratios is unnecessary.

Between these lines, multiply the entire function by \(e^{\delta(s-m)^2}\), where \(m=(a+b)/2\). Apply its bound (4.8) with \(\delta/2\); the horizontal edges of the rectangles tend to zero. If the two vertical bounds have maximum \(M\), their damped values are at most \(M e^{\delta(b-a)^2/4}\). The maximum principle gives this bound inside. For any fixed \(s\), let \(\delta\) decrease to zero. It follows that \(|Z_\chi(g,s)|\leq M\). Any prescribed finite-width strip can be enclosed by such lines.

### 4.5. Recovering a function from the twisted Mellin family

**Lemma 4.4 — two-sided Mellin uniqueness.** Let \(f_1,f_2\) be continuous functions on \(C_{\mathbb Q}\), with finite level in its compact factor. Suppose that for each compact-factor character \(\chi\), the Mellin integral of \(f_1\) converges absolutely in a right half-plane, while that of \(f_2\) converges absolutely in a left half-plane. Suppose their continuations are the same entire function, bounded on every finite-width strip. Then \(f_1=f_2\).

**Proof.** The rational idele-class decomposition is
\(C_{\mathbb Q}\simeq\mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}\).
At a common finite level \(H\), the second factor reduces to a finite abelian group. Finite Fourier inversion reduces the assertion to continuous functions \(h_1,h_2\) on \(x=\log t\), whose bilateral Laplace transforms converge on opposite half-planes and continue to the same entire bounded-strip function \(A(s)\). Every character of that finite quotient extends to an idele-class character by making it trivial on the positive norm factor. A constant shift of \(s\), such as \(s-\tfrac12\), makes no difference.

Take \(\rho\in C_c^\infty(\mathbb R)\), and put
\(\widehat\rho(s)=\int_{\mathbb R}\rho(u)e^{su}\,du\).
Repeated integration by parts makes this transform decrease faster than any inverse power of \(|\operatorname{Im}s|\), uniformly on finite-width strips. On a line \(b\) where the appropriate transform converges, Fourier inversion gives
\[
(\rho*h_i)(x)=
 \frac{1}{2\pi i}\int_{b-i\infty}^{b+i\infty}
       \widehat\rho(s)A(s)e^{-sx}\,ds.
\tag{4.13}
\]
For justification, the function \(e^{bx}h_i(x)\) is integrable. Apply Fourier inversion to the smooth compactly supported \(\rho\), then Fubini; the transform of \(\rho\) is integrable on the line and the weighted integral of \(h_i\) is finite.

Move the line from the right half-plane to the left half-plane. The integrand is entire. Boundedness of \(A\) and rapid decrease of \(\widehat\rho\) make the horizontal integrals tend to zero, so Cauchy's theorem gives equal values on both lines. Hence \(\rho*h_1=\rho*h_2\). A smooth compactly supported approximate identity converges to each \(h_i\), by continuity, so \(h_1=h_2\). Finite Fourier inversion recovers \(f_1=f_2\) on every compact fibre. \(\square\)

Finite level here is uniform in the norm variable. For fixed \(g\), choose an open subgroup of finite units such that \(g_f^{-1}d(h)g_f\) fixes \(W_f\). Both torus restrictions used below are fixed by it. Thus the finite Fourier reduction applies.

### 4.6. Complete the automorphic construction

**Proof of Theorem 4.1.** Lemma 4.2 defines the smooth function (4.3). Left multiplication by \(d(r)\), \(r\in\mathbb Q^\times\), reindexes the sum. Left multiplication by \(n(x)\), \(x\in\mathbb Q\), contributes \(\psi(\alpha x)=1\). Rational central matrices act trivially by the hypothesis on \(\omega_\pi\). Thus \(\Phi_W\) is invariant under the rational upper triangular subgroup.

Use \(w=-w_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), the Weyl element of the local positive-kernel equations. The two rational Weyl elements differ by a rational central matrix, on which \(\omega_\pi\) is trivial. Fix \(g\), and set
\[
f_1(a)=\Phi_W(d(a)g),\qquad
f_2(a)=\Phi_W(wd(a)g).
\tag{4.14}
\]
Both are well-defined on \(C_{\mathbb Q}\). For the second, use
\(wd(r)=rI\,d(r^{-1})w\) and upper triangular invariance. Their common compact-factor finite level was checked after Lemma 4.4.

In the right half-plane, the transform of \(f_1\) is \(Z_\chi(g,s)\). The normalized local functional equations and (4.2) identify its entire continuation with
\[
\int_{\mathbb A^\times}
 W(d(a)wg)\omega_\pi(a)^{-1}\chi(a)^{-1}
                   |a|^{1/2-s}d^\times a,
\tag{4.15}
\]
initially convergent for \(\operatorname{Re}s\) sufficiently negative. To verify the identification, divide each original local integral by \(L(s,\pi_v\otimes\chi_v)\), and each dual integral by \(L(1-s,\widetilde\pi_v\otimes\chi_v^{-1})\). Their ratio is the local epsilon factor. Almost all normalized integrals and epsilon factors are one. Multiplying the finitely many exceptions, and then using the completed functional equation (4.2), gives the claimed global identity. At the real place Lemma 4.3 supplies the equation for the smooth translate. This argument does not require convergence of an infinite product of local gamma ratios.

Unfold (4.15) to \(C_{\mathbb Q}\), then replace \(a\) by \(b^{-1}\). The identity
\(wd(b)=bI\,d(b^{-1})w\) and central covariance cancel the factor \(\omega_\pi\). The result is
\[
\int_{C_{\mathbb Q}}f_2(b)\chi(b)|b|^{s-1/2}d^\times b.
\]
Section 4.4 gives the common entire bounded-strip continuation. Lemma 4.4 proves \(f_1=f_2\), for every fixed \(g\). Taking \(a=1\) gives \(\Phi_W(g)=\Phi_W(wg)\). Bruhat decomposition now proves invariance under all of \(G(\mathbb Q)\).

The constant term is zero:
\[
\begin{gathered}
\int_{\mathbb Q\backslash\mathbb A}\Phi_W(n(x)g)\,dx\\
=\sum_{\alpha\ne0}W(d(\alpha)g)
       \int_{\mathbb Q\backslash\mathbb A}\psi(\alpha x)\,dx
=0.
\end{gathered}
\tag{4.4}
\]
The compact quotient and Lemma 4.2 justify termwise integration. The coefficient at \(\psi(x)\) is \(W(g)\), by the same orthogonality. Thus \(W\mapsto\Phi_W\) is injective and nonzero. Every rational proper parabolic of \(G\) is conjugate to the upper triangular one, so rational invariance also gives all the required constant-term vanishings.

Choose a finite finite-place level fixing \(W\). Lesson 1's double-coset description and finite-index modular reduction give finitely many classical cusp charts, with fixed finite components and compact rotation component. Lemma 4.2 gives rapid decrease at large height in each chart, including every fixed real derivative. On the remaining compact part those derivatives are bounded. Central translation contributes the specified quasicharacter, whose absolute value has a fixed real norm power. Hence the resulting function has moderate growth and is cuspidal; after removing this common norm power it is square integrable as well.

The construction commutes with right finite Hecke operators, compact rotations and Lie derivatives. Finite compact type, infinitesimal finiteness and admissibility are inherited from the given module \(\pi\). We have embedded that irreducible module in the automorphic cuspidal space. \(\square\)

### 4.7. A different partial converse

Jacquet–Langlands, Theorem 11.5 and Corollary 11.6, allow an excluded finite set \(S\), with additional partial-functional-equation hypotheses and an exclusion of an Eisenstein pair. Their conclusion identifies prescribed components **away from \(S\)**. Section 4.9 proves this separate construction and its cuspidality corollary, with coefficient covariance under all rational units at \(S\). It identifies the components outside \(S\); the Artin criterion in Lesson 20 uses further local comparisons to recover the missing components. It does not supply strong multiplicity one. The full converse proved above uses all local factors and the full twisted functional equations.

### 4.8. The converse theorem over every global field

The field restriction in the preceding proof can now be removed. We use the product formula, discreteness and compact additive quotient of a global field, and compactness of its norm-one idèle class group. For number fields these are the written adelic prerequisites NT-ADL-01, NT-ADL-03 and NT-ADL-05, used in NT-ADL-09's theta lemma; for function fields the additive residue/duality argument in NT-CFT-15 and the degree/norm-one construction in NT-CFT-16–17 supply the corresponding statements. The function-field degree is onto \(\mathbf Z\). No global automorphic theorem is used in the following reduction.

**Theorem 4.5 — the full global-field converse.** Let \(F\) be any global field, and replace \(\mathbb Q\), \(p\) and \(p^C\) in the hypotheses of Theorem 4.1 by \(F\), the finite place \(v\) and \(q_v^C\). At every infinite place use the moderate smooth generic realization of Lesson 11. Assume the complete twisted functions and their contragredient family are entire, bounded on every finite-width strip, and obey the complete functional equation (4.2) for every unitary Hecke character of \(F\). Then the prescribed tensor product has a cuspidal automorphic realization. After a positive norm twist makes its central character unitary, this realization belongs to the cuspidal Hilbert space.

We prove the new analytic and reduction steps, then give the full construction. In function fields the norm coordinate is discrete; there are no archimedean local integrals.

**Lemma 4.6 — the all-field Whittaker sum.** For a finite sum of product Whittaker vectors, the series
\[
\Phi_W(g)=\sum_{\alpha\in F^\times}W(d(\alpha)g)
\tag{4.16}
\]
converges absolutely and locally uniformly, with every fixed infinite-place right derivative. Let \(a(t)\) be a homomorphic norm section and let \(g\) range over a fixed compact set. For number fields \(\Phi_W(d(a(t))g)\) decreases faster than every power as \(t\to\infty\), and is \(O(t^{-A})\) as \(t\to0\), for some \(A\). For function fields it is zero for all sufficiently large \(t\), uniformly in \(g\), and has a polynomial bound in \(t^{-1}\) near zero.

**Proof.** All finite local Kirillov functions vanish when the argument's absolute value is sufficiently large. Their small-argument germs are character powers times valuation polynomials. At good places the spherical formula of Lesson 13 bounds a nonzero value at valuation \(n\ge0\) by \((n+1)q_v^{(C-1/2)n}\). Since \(n+1\le2^n\le q_v^n\), one fixed power absorbs this factor. Thus for every nonzero summand, and uniformly for compact local translates,
\[
|y_v|_v\le c_v,\qquad |W_v(d(y_v)g_v)|\le M_v|y_v|_v^{-\rho},
\tag{4.17}
\]
where \(c_v=M_v=1\) outside a finite set and one \(\rho\) works at all finite places. Smoothness makes the orbit of a finite-place vector under any compact set finite, so the exceptional constants can be uniform.

For a number field of degree \(d\), choose \(a(t)\) with finite components one and every ordinary infinite coordinate \(t^{1/d}\). The finite support conditions put \(\alpha\) in one fractional ideal \(I\). It is a lattice in \(F_\infty\simeq\mathbf R^d\). For \(\alpha\ne0\) its infinite norm product is bounded below: if \(mI\subseteq\mathcal O_F\), then \(|N_{F/\mathbf Q}\alpha|\ge m^{-d}\). Multiplying (4.17) and using the product formula bounds the finite part by a fixed power of \(1+\|\alpha\|\).

At an infinite place, continuity of the Whittaker functional and the explicit moderate compact model give a bound by a fixed power of the argument and its inverse, controlled by a smooth seminorm. The unipotent Lie derivatives multiply a diagonal Whittaker function by the real coordinates of that argument, with fixed nonzero constants. At a complex place use both real generators: at least one of its real coordinates has absolute value at least its ordinary radius divided by \(\sqrt2\). Arbitrarily high derivatives therefore give arbitrarily fast inverse-power decrease at large ordinary radius, with the same moderate exponent at zero.

Let \(r_v\) be the ordinary radii of the infinite arguments, with weights \(d_v=1\) or \(2\), and put \(R=\max_v r_v\). Their product satisfies \(\prod_v r_v^{d_v}\ge c t\), uniformly for compact norm-one multipliers. The small radii can be absorbed as follows: for one sufficiently large fixed \(N\),
\(\prod_{r_v<1}r_v^{-d_vN}\le (ct)^{-N}\max(1,R)^{dN}\).
Use arbitrarily high unipotent derivatives at a coordinate attaining \(R\) when \(R\ge1\); the other coordinates have fixed moderate bounds. Consequently, for every \(L\), the whole infinite product is at most
\[
C_Lt^{-A}\bigl(1+t^{1/d}\|\alpha\|\bigr)^{-L}
\tag{4.18}
\]
for one fixed small-norm exponent \(A\), increased if necessary. For \(t\ge1\), the lower norm-product bound and the same argument give an arbitrarily large inverse power of \(t^{1/d}\|\alpha\|\).

A lattice has \(O(R^d)\) points in a ball of radius \(R\), by packing disjoint small balls. Its nonzero vectors have a positive minimum length. Dyadic summation, after multiplying (4.18) by the finite polynomial bound, proves absolute local uniform convergence and every claimed large-norm estimate. For \(t\le1\), split at \(\|\alpha\|=t^{-1/d}\): the inner ball contributes a polynomial in \(t^{-1}\), and the outer dyadic tail does the same when \(L\) exceeds the finite polynomial exponent plus \(d\). Fixed right derivatives obey the identical estimates, with changed seminorm constants. Compact lifts of the norm-one class group exist by finitely many relatively compact quotient charts, so these estimates are uniform on that fibre as well.

For a function field, (4.17) at every place puts \(\alpha\) in the intersection of \(F\) with a compact additive adelic set. This intersection is finite, since \(F\) is discrete. It is uniformly finite on compact sets of \(g\). Moreover a nonzero summand would imply
\(t=|\alpha a(t)|\le\prod_v c_v\), proving eventual vanishing at large norm. Write the norm section as powers of a fixed degree-one idele. Its valuations at its finitely many nonunit places are linear in the integer exponent \(n\). The allowed additive sets can therefore be covered by at most \(Cq^{B|n|}\) cosets of one small compact open additive subgroup \(U\) satisfying \(F\cap U=\{0\}\). Each coset contains at most one element of \(F\). Multiplication of the local bounds in (4.17) gives \(C t^{-\rho}\) for each nonzero term, by the product formula. The point count supplies a polynomial in \(t^{-1}\) near zero. This proves every function-field assertion. \(\square\)

**Lemma 4.7 — smooth archimedean Mellin integrals.** Lemma 4.3 holds at each real or complex place, with that place's exact local factor and functional equation. The bound is \(A_{\delta,v}e^{\delta|\operatorname{Im}s|^2}\) on every finite-width strip, for every \(\delta>0\).

**Proof.** The real case is Lemma 4.3. In the complex compact model of Lesson 11, expand a smooth section into its \(U(2)\)-types. Their dimensions and number of weight vectors at highest weight \(\ell\) grow polynomially in \(1+\ell\). For an orthonormal compact-type basis, every fixed smooth seminorm also has polynomial growth: a matrix coefficient has supremum at most the square root of its dimension, and each compact Lie derivative has operator norm \(O(1+\ell)\). Smooth coefficients decrease faster than every power, by repeatedly applying the compact Laplacian, whose eigenvalues have quadratic growth. Thus the compact-type sums converge in every smooth seminorm.

For each finite vector, the Gaussian-polynomial computation in Lesson 11, Section 8, makes its Mellin integral divided by the prescribed product of complex gamma factors a polynomial in \(s\). On a far right line, Lemma 4.6's local derivative argument bounds the original integral polynomially in the type index. On a far left line, the exact local functional equation gives the same bound for the dual integral. The Weyl matrix is compact, so its action does not enlarge the type index. Reciprocal gamma factors have at most exponential growth on those lines, by the reflection and recurrence argument of Lemma 4.3. The epsilon monomial has bounded absolute value on each vertical line. Hence both vertical bounds are a fixed polynomial in the type index times \(e^{A|\operatorname{Im}s|}\).

Apply the rectangle maximum principle to each normalized polynomial multiplied by \(e^{\delta(s-m)^2}\). The horizontal edges tend to zero, and the vertical edges have a uniform polynomial bound in the type index after Gaussian damping. The resulting bound inside is that polynomial times \(e^{\delta|\operatorname{Im}s|^2}\). Rapid compact-type coefficients make the sums locally uniform. On the initial half-plane they equal the actual smooth Mellin integral by the seminorm bound and dominated convergence; their dual functional equations also pass to the limit. This proves the entire continuation, the equation and the estimate. Fixed character twists only change the inducing parameters and constants. Finitely many infinite places give the same estimate for their product by dividing \(\delta\) among them. \(\square\)

**Lemma 4.8 — compact-fibre Mellin uniqueness.** Lemma 4.4 holds on \(C_F\) for every global field, with the integral replaced by a two-sided sum in the discrete norm coordinate of a function field.

**Proof.** Put \(C=C_F^1\). For a number field use \(C_F=C\times\mathbf R_{>0}\); for a function field choose a degree-one idele to obtain \(C_F=C\times q^{\mathbf Z}\). Every continuous unitary character of \(C\) extends by making it trivial on that norm section. Average \(f_i\) against each such character on \(C\). Absolute convergence permits Fubini, so its norm-coordinate transforms have the assumed common entire continuation. Over a number field the compactly supported convolution and contour-shift proof (4.13) applies verbatim to these averaged continuous functions on \(\log t\).

Over a function field write their transforms as \(\sum_n a_i(n)q^{ns}\). The initial right and left half-planes give Laurent expansions in \(z=q^s\) outside and inside circles, respectively. The common entire function is periodic with period \(2\pi i/\log q\), first on an initial half-plane and then everywhere by the identity theorem. It therefore descends to a holomorphic function on \(\mathbf C^\times\). Uniqueness of its Laurent coefficients gives \(a_1(n)=a_2(n)\) for every integer \(n\). No boundary value at \(z=0\) or infinity is assumed.

For completeness the compact Fourier averages determine the original continuous function. On a compact abelian group, convolution by a continuous symmetric kernel is a compact self-adjoint operator on \(L^2(C)\). It commutes with translations. Every nonzero eigenspace is finite-dimensional, and its commuting unitary translations can be simultaneously diagonalized. A joint eigenvector is continuous, since it is a nonzero-eigenvalue convolution output; its translation rule makes it a constant multiple of a continuous character. Continuous symmetric approximate identities converge strongly to the identity, so these character eigenspaces span a dense subspace of \(L^2(C)\). A continuous function with every character average zero is therefore zero almost everywhere, and then everywhere because Haar measure has full support. Applying this at each norm value recovers \(f_1=f_2\). \(\square\)

**Lemma 4.9 — an adelic reduction and integrability bound.** Modulo \(G(F)\) and the adelic centre, every element has a representative
\[
n(x)d(a(t)h)k,\qquad x\in X,\quad h\in H,\quad k\in K,
\quad t\ge c>0,
\tag{4.19}
\]
where \(X\) and \(H\) are fixed compact lifts of \(\mathbb A_F/F\) and \(C_F^1\). Quotient integration is bounded by the corresponding Iwasawa integral with norm density \(t^{-1}dt/t\); in a function field use its discrete counterpart.

**Proof.** Normalize additive Haar measure so \(\mathbb A_F^2/F^2\) has covolume one. If a measurable subset of \(\mathbb A_F^2\) has measure greater than one, two of its points differ by a nonzero vector of \(F^2\): integrate its periodized indicator on the compact additive quotient; an average greater than one forces multiplicity at least two. This is the required adelic lattice argument.

For a number field take the finite integral box and an infinite radius-\(\rho\) box in each of its two coordinates, then pull this body back by right multiplication by \(g\). Its volume is \(A_0\rho^{2d}/|\det g|\). Choose \(\rho=A_1|\det g|^{1/(2d)}\), with \(A_1\) fixed large enough. The difference of the two points found above yields a nonzero \(v\in F^2\) whose row \(vg\) is integral at every finite place and has ordinary infinite coordinates bounded by \(2\rho\). Its product of local row lengths is at most \(A_2|\det g|^{1/2}\). For a function field use the adelic integral box scaled in both coordinates by an idele \(r\), with \(|r|\) between a fixed sufficiently large multiple of \(|\det g|^{1/2}\) and \(q\) times that value. Its pulled-back volume is \(A_0|r|^2/|\det g|>1\), and its difference stays in the same additive box. The identical row-length bound follows.

Complete \(v\) to the bottom row of a matrix \(\gamma\in\mathrm{SL}_2(F)\). Local Iwasawa decomposition writes
\(\gamma g=z(b)n(x)d(a)k\). The bottom row length is \(|b_v|\) at a finite place and its ordinary radius at an infinite place, using maximum and Euclidean norms respectively. Therefore
\[
|b|\le A_2|\det g|^{1/2},\qquad
|a|=\frac{|\det g|}{|b|^2}\ge A_2^{-2}.
\tag{4.20}
\]
Remove the central \(z(b)\). Left rational diagonal multiplication puts the class of \(a\) into \(a(t)H\), preserving its norm; rational unipotent multiplication then puts \(x\) into \(X\). Compact lifts exist by finite quotient charts. This proves (4.19).

Local Iwasawa Haar measure has the inverse upper-triangular modulus \(|a|^{-1}\); multiplying over places gives \(t^{-1}\). Unfolding the discrete upper triangular rational group puts its unipotent coordinate in \(\mathbb A_F/F\) and its diagonal coordinate in \(C_F\). Their compact fibres have finite measure. The map of this upper-triangular quotient to the full rational quotient has at least one representative in (4.19); the nonnegative quotient formula therefore bounds an invariant integral by the integral over that covering set. Compact rotation fibres only contribute a fixed finite constant. This proves the stated bound, without requiring uniqueness of representatives. \(\square\)

**Proof of Theorem 4.5.** Define (4.16) using Lemma 4.6. Reindexing proves invariance under \(d(F^\times)\); the triviality of \(\psi\) on \(F\) proves invariance under \(n(F)\); the central hypothesis gives invariance under scalar rational matrices. For fixed \(g\), the two functions
\(f_1(a)=\Phi_W(d(a)g)\) and \(f_2(a)=\Phi_W(wd(a)g)\)
are thus well-defined on \(C_F\).

Their unfolded Mellin integrals are exactly (4.11) and (4.15), now over \(\mathbb A_F^\times\). Finite normalized local integrals are Laurent polynomials in \(q_v^s\). Lemma 4.7 supplies the smooth normalized archimedean integrals. The assumed completed functions, together with those finitely many normalized factors, give entire continuations of growth at most \(A_\delta e^{\delta|\operatorname{Im}s|^2}\) on any finite-width strip. The right integral and the dual left integral are bounded on sufficiently far vertical lines. The damped maximum-principle argument in Section 4.4 therefore proves boundedness on every intervening strip. For function fields there are no archimedean factors; the finite Laurent factors are already bounded on every such strip.

The exact local functional equations, multiplied over their finitely many exceptions, and the assumed complete equation identify these two entire transforms. Replace \(a\) by \(a^{-1}\) in the dual integral; \(wd(a)=aI\,d(a^{-1})w\) cancels its central-character factor. Lemma 4.8 gives \(f_1=f_2\). Taking \(a=1\) proves left Weyl invariance. Bruhat decomposition proves full \(G(F)\)-invariance.

Integrate the locally uniformly convergent sum on the compact quotient \(\mathbb A_F/F\). Every nonzero additive character integrates to zero, so its constant term vanishes. Its coefficient at \(\psi\) is \(W(g)\), proving injectivity and nonzero realization. Rational conjugacy gives vanishing at every proper rational parabolic.

For moderate growth, local Iwasawa decomposition and compact lifts give the estimates of Lemma 4.6 for every diagonal norm, with compact unipotent, norm-one and rotation coordinates. The diagonal norm and its inverse, and the removed central norm and its inverse, are bounded by fixed powers of the product matrix-and-inverse height of \(g\). Thus the polynomial small-norm bound and rapid large-norm bound give global moderate growth, also for every fixed right derivative. Finite level, compact finiteness and infinitesimal finiteness are inherited from the given tensor module, since the construction commutes with its right actions.

Finally the absolute value of the central Hecke character is trivial on compact \(C_F^1\), hence a real power of the norm. A positive determinant twist cancels it on scalar matrices. For this unitary-central realization, (4.19), Lemma 4.6 and the integration bound give a finite square norm: the norm interval begins at \(c>0\), and the upper tail is rapidly decreasing or eventually zero. The same bounds hold for derivatives. Its zero constant term puts it in the cuspidal Hilbert space. This completes the all-field converse and the claimed Hilbert realization. \(\square\)

The historical theorem and analytic comparison are Jacquet–Langlands, Theorem 11.3 and Lemmas 11.3.1–11.3.3/11.4.3. The explicit lattice reduction, compact convolution proof of Fourier uniqueness and smooth complex compact-type estimate above supply the arguments needed here beyond the rational case.

### 4.9. The converse with an exceptional finite set

This is a separate construction from Theorem 4.5. It first gives an automorphic realization of the prescribed representations away from a finite set. The cuspidality condition is addressed after the construction. Throughout this section, a local Whittaker model at infinity means its moderate smooth realization, with the finite compact types and infinitesimal character subsequently retained.

Let \(S\) be a finite set of finite places, and choose integers \(m_v\geq0\), \(v\in S\). Put \(U_v^{(0)}=\mathcal O_v^\times\) and \(U_v^{(m)}=1+\mathfrak p_v^m\) for \(m>0\). Define
\[
H=\{a\in\mathbb A_F^\times:a_v\in\mathcal O_v^\times\ (v\in S)\},
\qquad \Gamma=F^\times\cap H,
\qquad K_{D,v}=K_0(\mathfrak p_v^{m_v}).
\tag{4.21}
\]
Here \(K_0(\mathfrak p^0)=\mathrm{GL}_2(\mathcal O)\). Write \(K_D=\prod_{v\in S}K_{D,v}\), \(G^S=\prod'_{v\notin S}G(F_v)\), and \(G_D=K_DG^S\). A subscript \(S\) or superscript \(S\) on an idèle or matrix retains respectively its components in or outside \(S\), replacing the other components by the identity. Finite weak approximation gives \(\mathbb A_F^\times=F^\times H\) and \(G(\mathbb A_F)=G(F)G_D\). Thus \(\Gamma\backslash H=C_F\) topologically.

Let \(\eta\) be a Hecke quasicharacter. For \(v\notin S\), prescribe infinite-dimensional generic \(\pi_v\) with central character \(\eta_v\), spherical almost everywhere and with the two good Satake values bounded above and below by fixed powers of \(q_v\). On \(K_D\) choose characters \(e,\widehat e\) trivial on the subgroup with both diagonal entries congruent to one modulo \(\mathfrak p_v^{m_v}\). They satisfy
\[
\widehat e\bigl(\operatorname{diag}(u,z)\bigr)
=e\bigl(\operatorname{diag}(z,u)\bigr),
\qquad e(zI)=\eta_S(z)
\tag{4.22}
\]
for unit components. For \(m_v>0\), such characters depend only on the two diagonal unit residue classes. For \(m_v=0\), the stated kernel is the whole maximal compact group, so its character is trivial; the central condition then requires \(\eta_v\) to be unramified. In particular both characters are trivial on the upper unipotent subgroup of \(K_D\).

Choose bounded coefficient functions \(a_\alpha,\widehat a_\alpha\), \(\alpha\in F^\times\), with
\[
a_{\alpha\beta}=e(d(\beta_S))a_\alpha,
\qquad \widehat a_{\alpha\beta}=\widehat e(d(\beta_S))\widehat a_\alpha
\quad(\beta\in\Gamma).
\tag{4.23}
\]
The covariance in (4.23) is required for **all rational elements unit at \(S\)**. Congruence units alone would not suffice for upper triangular invariance or for recovery of every compact unit character average. Both coefficient functions vanish unless \(\alpha\mathcal O_v\) is in the kernel of \(\psi_v\) for every \(v\in S\). Require \(a_\alpha\ne0\) for at least one \(\alpha\); this explicit condition prevents a vacuous zero realization.

For a Hecke quasicharacter \(\omega\), when \(\omega_v(u)e_v(d(u))=1\) on \(\mathcal O_v^\times\), define
\[
\Lambda(s,\omega)=
\left(\sum_{\alpha\in\Gamma\backslash F^\times}
a_\alpha\omega(\alpha_S)|\alpha_S|^{s-1/2}\right)
\prod_{v\notin S}L(s,\pi_v\otimes\omega_v).
\tag{4.24}
\]
Define \(\widehat\Lambda(s,\omega)\) by replacing \(a,e\) by \(\widehat a,\widehat e\), retaining \(\pi_v\) in this formula. Its dual argument will be \(\eta^{-1}\omega^{-1}\). This convention uses \(\widetilde\pi_v=\eta_v^{-1}\otimes\pi_v\), proved in Lesson 9, Proposition 2.1, and in the infinite-place models of Lesson 11.

These definitions are independent of the coset representatives. Indeed \(|\beta_S|=1\) for \(\beta\in\Gamma\), and the two character factors in (4.23) and (4.24) cancel. They converge in a right half-plane. The coefficient support gives a lower bound on each valuation \(v(\alpha)\), \(v\in S\). For each tuple of valuations there is at most one coset, because equality of those valuations makes the quotient lie in \(\Gamma\). Bounded coefficients reduce the first sum, for unitary \(\omega\), to products of convergent geometric series when \(\operatorname{Re}s>1/2\). A fixed norm power in a quasicharacter shifts that half-plane. The good Satake bound gives the remaining Euler convergence in a sufficiently far right half-plane.

Choose \(A\in F^\times\) with \(v(A)=m_v\) at every place of \(S\), again by finite weak approximation. Assume that both defined families in (4.24) continue to entire functions bounded on every finite-width closed strip, and that
\[
\Lambda(s,\omega)=
\omega(-A_S)|A_S|^{s-1/2}
\left(\prod_{v\notin S}\epsilon(s,\pi_v\otimes\omega_v,\psi_v)\right)
\widehat\Lambda(1-s,\eta^{-1}\omega^{-1}).
\tag{4.25}
\]
The dual family on the right is defined whenever the first is: by (4.22), its unit condition is the inverse of \(\omega_v(u)e_v(d(u))=1\). These hypotheses may equivalently be imposed for all unitary \(\omega\), together with their norm shifts.

**Theorem 4.10 — the automorphic exceptional-set construction.** Under these hypotheses, the \(G^S\)-module \(\bigotimes'_{v\notin S}\pi_v\) embeds in smooth finite-level, compact-finite, infinitesimally finite automorphic forms of moderate growth and central character \(\eta\). On \(G_D\) its image is
\[
\Phi_W(g)=e(g_S)
\sum_{\alpha\in F^\times}a_\alpha W^S(d(\alpha^S)g^S).
\tag{4.26}
\]
No component at a place in \(S\) is asserted here.

**Proof: convergence and upper triangular invariance.** The finite support condition on \(a_\alpha\) supplies the missing bounds at places of \(S\). Thus the proof of Lemma 4.6 applies to the absolute value of this weighted series: its finite-place support is still a fixed fractional lattice in a number field and a compact intersection in a function field. Bounded coefficients add only a fixed constant. The same proof gives locally uniform convergence and every fixed infinite-place derivative. For fixed compact finite and angular components it gives polynomial growth in the norm and its inverse, rapid decay in the balanced large norm coordinate in number fields, and an eventual zero tail in function fields. The same statements hold for \(\widehat\Phi_W\), defined with \(\widehat a,\widehat e\).

If \(n(x)\in G(F)\cap G_D\), then \(x\in\mathcal O_v\) for \(v\in S\). Every surviving coefficient has \(\psi_v(\alpha x)=1\) there. The outside Whittaker phase is consequently
\(\prod_{v\notin S}\psi_v(\alpha x)=\prod_v\psi_v(\alpha x)=1\).
This proves upper rational unipotent invariance. If \(\beta\in\Gamma\), replacing \(\alpha\) by \(\alpha\beta\) and using (4.23) proves invariance under \(d(\beta)\). A rational upper triangular matrix in \(G_D\) has both diagonal entries unit at \(S\), so it is a product of these matrices and a rational scalar. The scalar factors cancel by the central Hecke character and the product formula. Hence both sums are invariant under the upper triangular part of \(G(F)\cap G_D\). The same calculation proves their central covariance for scalar idèles in \(H\).

**Proof: the functional equation gives the second invariance.** Set
\[
M=\begin{pmatrix}0&1\\ A&0\end{pmatrix}\in G(F),
\qquad T(g)=MgM_S^{-1}.
\tag{4.27}
\]
At \(v\in S\), conjugation sends \(\left(\begin{smallmatrix}r&b\\c&d\end{smallmatrix}\right)\) to \(\left(\begin{smallmatrix}d&c/A\\Ab&r\end{smallmatrix}\right)\). This preserves \(K_0(\mathfrak p_v^{m_v})\) and swaps its two diagonal residue classes. Thus \(T\) preserves \(G_D\) and \(\widehat e(M_Sg_SM_S^{-1})=e(g_S)\).

For fixed \(g\in G_D\), take the Mellin integrals on \(\Gamma\backslash H\) of \(\Phi_W(d(a)g)\) and \(\widehat\Phi_W(T(d(a)g))\), with weight \(\omega(a)|a|^{s-1/2}\). The first converges far to the right and the second far to the left. If the unit condition for (4.24) fails, both integrals are zero by compact unit orthogonality. Otherwise unfolding the \(\Gamma\)-sum, and normalizing its compact unit fibres to have volume one, gives respectively
\[
e(g_S)\Lambda(s,\omega)\prod_{v\notin S}P_v(g_v;s,\omega_v),
\]
\[
e(g_S)\omega(-A_S)|A_S|^{s-1/2}
\widehat\Lambda(1-s,\eta^{-1}\omega^{-1})
\prod_{v\notin S}P_v(w_0g_v;1-s,\eta_v^{-1}\omega_v^{-1}),
\tag{4.28}
\]
where
\(P_v(g;s,\omega)=L(s,\pi_v\otimes\omega)^{-1}
\int W_v(d(y)g)\omega(y)|y|^{s-1/2}d^\times y\).
Almost all normalized factors are one. For clarity, the change of variable in the second integral uses the exact matrix identity
\[
d(\alpha)M d(a)=(-Aa)I\,d(-\alpha/(Aa))w_0.
\]
Put \(b=-\alpha/(Aa)\) in the outside integration. The factors of \(\alpha\) become \((\eta^{-1}\omega^{-1})(\alpha_S)|\alpha_S|^{1/2-s}\), because \(\eta,\omega\) are trivial on \(F^\times\). The remaining factor is \(\omega(-A_S)|A_S|^{s-1/2}\). This proves every sign, central factor and exponent in (4.28).

The local equation of Lessons 9 and 11 is
\[
P_v(w_0g_v;1-s,\eta_v^{-1}\omega_v^{-1})
=\epsilon(s,\pi_v\otimes\omega_v,\psi_v)P_v(g_v;s,\omega_v).
\]
Together with (4.25), this identifies the two continued transforms. Finite normalized factors are Laurent polynomials. Lemma 4.7 handles smooth infinite-place factors. The entire strip hypotheses, far-line bounds and the Gaussian-damped maximum principle of Section 4.4 give the required common bounded-strip continuation. Lemma 4.8, on \(\Gamma\backslash H=C_F\), now gives
\(\widehat\Phi_W(Tg)=\Phi_W(g)\).

**Proof: rational invariance and extension.** Write \(\Gamma_D=G(F)\cap G_D\). It is generated by its upper and lower triangular matrices. To prove this, let \(\left(\begin{smallmatrix}r&b\\c&d\end{smallmatrix}\right)\in\Gamma_D\). At each place in \(S\), one of \(r,c\) is a unit. By weak approximation choose \(x\in F\), integral at \(S\), which is a unit where \(r\) is not a unit and belongs to \(\mathfrak p_v\) where \(r\) is a unit. Left multiplication by \(n(x)\) makes \(r+xc\) a unit everywhere in \(S\). When its upper left entry is a unit, the matrix factors as
\[
\begin{pmatrix}r&b\\c&d\end{pmatrix}
=\begin{pmatrix}r&0\\c&d-cb/r\end{pmatrix}n(b/r).
\]
Both factors lie in \(\Gamma_D\). This proves the generation assertion, including places with \(m_v=0\).

For a lower triangular \(\ell\in\Gamma_D\), \(M\ell M^{-1}\) is upper triangular and lies in \(\Gamma_D\). The established identity and upper invariance therefore give
\[
\Phi_W(\ell g)=\widehat\Phi_W((M\ell M^{-1})Tg)
=\widehat\Phi_W(Tg)=\Phi_W(g).
\]
Thus (4.26) is \(\Gamma_D\)-invariant. The equality \(G(\mathbb A_F)=G(F)G_D\) extends it uniquely to a left \(G(F)\)-invariant function. Any compact subset of \(G(\mathbb A_F)\) meets finitely many charts \(\gamma_i^{-1}G_D\), with \(\gamma_i\in G(F)\). On overlaps the preceding invariance makes the extensions agree; consequently continuity and smoothness follow from locally uniform convergence. Central covariance extends from \(H\) to all idèles using \(\mathbb A_F^\times=F^\times H\).

**Proof: moderate growth.** It suffices to bound the extended function on \(d(a)\Omega\), where \(\Omega\) is compact and \(|a|\ge c>0\), and to include the central norm power. Concentrate the norm of \(a\), modulo a rational diagonal and a fixed compact set of idèles, at one place \(v_0\notin S\): choose an infinite place in number fields. In function fields a finite place has norm image \(q^{d_0\mathbf Z}\); its finitely many remaining degree classes are absorbed into the compact set. Compactness of \(C_F^1\) proves the asserted compact remainder in both cases.

Take a fixed chart \(\gamma_i d(a)g\in G_D\). Since \(a_S=1\), its components in \(S\) are the compact matrices \(\gamma_{i,S}g_S\); they are independent of \(a\). The other finite components are also compact except possibly at \(v_0\). Local Iwasawa decomposition outside \(S\) writes this matrix as \(n(x)z(b)d(y)k\). For fixed \(\gamma_i,\Omega\), the modules of \(b,y\) and their inverses are bounded by fixed powers of \(|a|+|a|^{-1}\): at \(v_0\) this follows directly from bounds on the entries, inverse entries and determinant, and elsewhere the components are compact. Upper unipotent translation outside \(S\) changes each summand by a phase of absolute value one. Scalar translation contributes only the fixed norm power of \(|\eta|\). Modulo rational diagonal reindexing, \(y\) is a balanced norm representative times a compact lift of \(C_F^1\); its components in \(S\) may be held in a fixed compact set by using \(\Gamma\backslash H=C_F\). The weighted version of Lemma 4.6 therefore bounds the absolute series by a fixed power of \(|a|+|a|^{-1}\). There are only finitely many charts. This proves moderate growth, also for each fixed right derivative.

Right finite-place Hecke actions outside \(S\), infinite Lie derivatives and compact actions commute with the construction. The prescribed module gives infinitesimal and compact finiteness there; the \(K_D\)-character gives finite level and compact finiteness at \(S\).

Finally the map is nonzero. Represent \(\mathbb A_F/F\) using additive idèles whose \(S\)-components lie in \(\mathcal O_S\), possible by weak approximation. On this compact quotient, the locally uniform sum (4.26) has coefficient at \(x\mapsto\psi(\alpha x)\) equal to \(a_\alpha W^S(d(\alpha^S)g^S)\). The support condition makes the missing \(S\)-phase one. A nonzero \(a_\alpha\) and a suitable right translate of a nonzero Whittaker function give a nonzero coefficient. The kernel is an invariant submodule of the irreducible prescribed \(G^S\)-module, so it is zero. This proves Theorem 4.10. \(\square\)

**Lemma 4.11 — the constant-term alternative.** Let \(U\) be the prescribed irreducible \(G^S\)-module in Theorem 4.10. If the constant-term map is nonzero on \(U\), there are global Hecke quasicharacters \(\mu,\nu\) such that \(\pi_v=I(\mu_v,\nu_v)\) for almost every \(v\). The equality here concerns the irreducible unramified principal representation, with the normalized induction convention of Lesson 6.

**Proof.** Write
\(C_f(g)=\int_{F\backslash\mathbb A_F}f(n(x)g)dx\), with additive quotient volume one. This map commutes with all right actions. Its functions are left invariant under \(N(\mathbb A_F)\) and under rational diagonal matrices, and have central character \(\eta\). Its nonzero image of \(U\) is isomorphic to that irreducible module. We first prove that every image vector has a finite-dimensional orbit under left adelic diagonal translation.

At a finite place outside \(S\), evaluation at the identity after the constant-term map is an \(N_v\)-invariant functional on \(\pi_v\). It factors through its Jacquet module. In the scalar Kirillov model this quotient is exactly the finite-dimensional germ space of Lesson 7: the compact part is spanned by the differences of upper-unipotent translates, by additive character orthogonality on its finitely many support cosets. The principal and special germ descriptions consequently give finite-dimensional torus orbits; a supercuspidal gives zero. The same statement holds with the identity replaced by any fixed right translate, since the functional and that translate commute with the left torus action.

At an infinite place this assertion follows from explicit zero-frequency equations. At a real place, remove the fixed central power and write \(h_n(y)\) for a rotation-weight-\(n\) coordinate, \(D=y\,d/dy\). The Iwasawa calculation in Lesson 11, Section 5, has unipotent frequency zero here: its raising and lowering operators are \(E_n=D+n/2\), \(F_n=D-n/2\). Since \(F_{n+2}E_n=D^2-D-n(n+2)/4\), a scalar Casimir \(\lambda\) gives
\[
(D^2-D-\lambda/4)h_n=0.
\]
On each sign component its solutions are powers with exponents \((1\pm\sqrt{1+\lambda})/2\), or a power and its logarithmic companion at the repeated root. There are finitely many rotation coordinates.

At a complex place use the radial calculation of Lesson 11, Section 8: on a compact type \(V_\ell\), put \(\phi_j(t)=C_{v_j}(\operatorname{diag}(t^{1/2},t^{-1/2}))\), \(k_j=\ell/2-j\) and \(D=t\,d/dt\). Let the two traceless Casimir scalars be \(a^2-1,b^2-1\). All terms from the two left unipotent derivatives vanish for a constant term. The same displayed calculation therefore becomes
\[
\bigl((D+k_j-1)^2-a^2\bigr)\phi_j=0,
\qquad
\bigl((D-k_j-1)^2-b^2\bigr)\phi_j=0.
\]
Each coordinate is in the intersection of two finite-dimensional Euler solution spaces, including logarithmic solutions at repeated roots. Compact diagonal angles have only the finitely many weights of \(V_\ell\). The central character determines the other diagonal radius. Thus every coordinate has a finite-dimensional orbit under the full complex diagonal group. These equations require only the fixed central scalars and compact type, so also apply to a real discrete-series submodule. No assertion about a general abstract infinite-place Jacquet functor is being substituted for this calculation.

Here is how the local assertion becomes a global one without making an assumption at \(S\). Fix an image vector and enlarge a compact open normal finite-place level fixing its finite compact orbit. Let \(U_f\) be its diagonal unit subgroup. There is a finite set \(T\), disjoint from \(S\) and containing every infinite place, such that
\(\mathbb A_F^\times=F^\times I_TU_f\), where \(I_T\) consists of idèles supported at \(T\). For number fields start with all infinite places: the quotient by their norm coordinate and \(U_f\) is discrete and compact, hence finite, by compactness of \(C_F^1\). For function fields first include one place outside \(S\); its degree image has finite index in \(\mathbb Z\), and the same compact-discrete argument applies. For each of the finitely many remaining classes, weak approximation makes its components at \(S\) belong to the prescribed diagonal unit subgroup. The remaining nonunit components have finite support outside \(S\). Add those places to \(T\), also adding the finitely many outside places at which the level is not maximal. This proves the displayed factorization.

Restrict a constant-term function to \(A(\mathbb A_F)K\), which determines it by Iwasawa decomposition. Its functions of the compact variable lie in finitely many matrix-coefficient spaces of \(K\). These finite spaces are stable under left compact translation; their finite-place normal level makes \(U_f\) act trivially on them. The idèlic factorization therefore reduces each of the two diagonal variables, modulo rational invariance, to \(I_T\). The already-proved local finite torus orbits at \(T\), and the finite compact matrix-coefficient spaces, give a finite-dimensional full left torus orbit.

A finite-dimensional continuous representation of \(C_F\times C_F\) has finitely many generalized quasicharacter weights. Indeed average an inner product over the compact norm-one factors to diagonalize their commuting unitary operators; on the continuous or discrete norm coordinates use the Jordan decomposition of the commuting generator matrices. Its coefficient functions are quasicharacters times bounded-degree polynomials in the two logarithmic norm coordinates (degree integers in a function field). The normalized torus weights can therefore be written
\[
C_f(\operatorname{diag}(a,b)g)
=|a/b|^{1/2}\sum_{\mu,\nu,r,t}
\mu(a)\nu(b)(\log|a|)^r(\log|b|)^t C_{\mu,\nu,r,t}(g).
\tag{4.29}
\]
In a function field replace logarithms by the corresponding degrees. Only finitely many terms occur. Rational diagonal invariance makes \(\mu,\nu\) Hecke quasicharacters, and central covariance gives \(\mu\nu=\eta\). Left torus translations commute with right actions, so the weight projections and their nilpotent logarithmic filtrations also commute with them. Apply a nonzero weight projection, then a highest nonzero product of nilpotent operators. Irreducibility of the image of \(U\) makes each such nonzero map injective. This gives a nonzero map from the prescribed module into functions satisfying the pure normalized induction rule for one pair \(\mu,\nu\).

At almost every place both characters, the prescribed representation and these functions are unramified. The spherical double-coset calculation of Lesson 13 in this normalized induced space has Satake values \(\mu_v(\varpi_v),\nu_v(\varpi_v)\). The nonzero intertwining map identifies these with the prescribed spherical values. If this induced representation were reducible, its spherical irreducible constituent would be one-dimensional; the special constituent has no maximal-compact fixed vector, as proved in Lessons 6 and 8. This contradicts the prescribed infinite-dimensional spherical \(\pi_v\). Thus at almost every place it is the irreducible principal representation \(I(\mu_v,\nu_v)\), as asserted. \(\square\)

We include the finite-space argument needed to choose a full cuspidal constituent. This also explains why a \(G^S\)-embedding alone is not yet a choice of the missing factors.

**Lemma 4.12 — cuspidal finite spaces and constituent selection.** With a unitary central character, a space of cusp forms at a fixed finite level and finitely many infinite compact types, with fixed infinite infinitesimal characters, is finite-dimensional. Every unitary cuspidal module with those infinitesimal characters is an orthogonal sum of irreducible admissible modules. The assertions hold over every global field; a function field has no infinite-place conditions.

**Proof in function fields.** Let \(J\) be the fixed compact open level. After retaining finitely many compact translates, there is a fixed compact open additive subgroup \(X\subset\mathbb A_F\) whose upper unipotent matrices fix the functions on the right. If \(|a|\) is sufficiently large, then
\(\mathbb A_F=F+aX\). To prove this assertion, the quotient is compact and its additive character group is
\(F\cap a^{-1}X^\perp\), by self-duality and \(F^\perp=F\). The product of the local support bounds in \(a^{-1}X^\perp\) is \(C/|a|<1\); the product formula excludes any nonzero rational point. Compact Fourier uniqueness of Lemma 4.8 makes the quotient trivial.

For a fixed-level function at \(n(x)d(a)k\), right \(n(X)\)-invariance and left \(N(F)\)-invariance consequently give invariance under all of \(N(\mathbb A_F)\) at large norm. Its value is its constant term and is zero. The reduction of Lemma 4.9 now puts its support in one fixed compact subset modulo rational matrices and the centre. A compact set meets finitely many level cosets. The functions are determined by their values on those cosets, proving finite dimension and square integrability.

**Proof in number fields: a uniform finite-space estimate.** Fix the level, compact types and infinitesimal characters. On the quotient by the centre, the sum of the real and complex Casimir equations is an elliptic equation on the corresponding finite-rank compact-type bundle; its positive Laplacian differs from that sum by fixed compact-type scalars. Thus interior elliptic estimates control every fixed derivative on a compact subset by the global square norm, with constants depending only on these fixed data. On any fixed compact set of finite components the same local estimates give
\[
|D f(g)|\le C_D H(g)^{B_D}\|f\|_2,
\tag{4.30}
\]
where \(H\) is a matrix-and-inverse height in the adjoint representation at infinity. This formulation removes the centre and is all that the reduction coordinates and the Fourier samples below require. Here is a precise injectivity estimate. Conjugating the fixed finite level by a finite component in that compact set puts every rational adjoint matrix preserving the component in a fixed fractional lattice in \(M_3(F)\). Its infinite embeddings form a discrete lattice. Thus a nonzero entry of \(\operatorname{Ad}(\gamma)-I\) has some embedded absolute value at least a fixed \(c>0\). Conjugation by \(\operatorname{Ad}(g_\infty)\) and its inverse can decrease this lower bound by at most a fixed power of \(H(g)\). A ball about the identity in the real group modulo its centre, of radius \(c'H(g)^{-B}\), consequently contains no such conjugated rational element except the identity. In the group quotient this is an injective lifted ball; compact stabilizers cause no problem because we retain the compact variable before taking its finite type. A central rational element has trivial adjoint action and has already been removed. Apply the elliptic estimate on this ball, adding the fixed compact Casimir to the noncompact Casimir to obtain an elliptic operator on the lifted group, and rescale its coordinates. Sobolev powers of that radius give (4.30), uniformly in the function.

The compact unipotent quotient gives the Fourier expansion at every rational cusp. Its zero coefficient vanishes. At the fixed finite level, upper unipotent invariance restricts its nonzero indices \(\alpha\) to one fixed fractional lattice, or finitely many such lattices for the compact reduction coordinates. The infinite-place equations give a finite-dimensional radial solution space for each such coefficient at the fixed compact types and central scalars. To verify this without presuming irreducibility of the whole cusp space, use the actual nonzero-frequency equations of Lesson 11, Sections 5 and 8. At a real place each sign coordinate solves the displayed second-order Whittaker equation. At a complex place the extremal coordinate solves the displayed second-order equation for \(u\), and its recursion determines the other coordinates of the compact type. These calculations hold for any function satisfying the central equations. Moderate growth excludes the growing solutions by the local cylinder estimate of Lesson 4; the remaining solutions and their fixed derivatives decay rapidly at the large radius. Their regular-singular Euler equations at zero give one fixed power bound, with bounded-degree logarithms, at the small radius. The solution spaces are finite-dimensional, and these bounds are uniform on a chosen finite basis. Tensoring the finitely many coordinates and sign components gives a finite basis of infinite-place Whittaker functions, independent of the cusp form and Fourier index. Equivalently the explicit models of Lesson 11 give that basis, but no spectral decomposition is assumed here.

Here is a uniform bound on the scalar coefficients in those combinations. Choose finitely many infinite-place sample matrices for which evaluation on a basis of those Whittaker vectors is injective; they exist because linearly independent Whittaker functions are linearly independent as functions. To sample the coefficient indexed by \(\alpha\), replace a sample matrix by \(d(\alpha_\infty^{-1})\) times that matrix. Its height is polynomial in \(1+\|\alpha\|\): the fractional lattice gives a lower bound on the product of the infinite absolute values of a nonzero \(\alpha\), and hence bounds each inverse embedding by a fixed power of the largest embedding. Integrate (4.30) on the compact additive quotient at these matrices, then invert the fixed finite evaluation matrix. This gives a bound
\(C\|f\|_2(1+\|\alpha\|)^B\)
for every scalar Fourier coefficient, with one exponent and constant for the whole fixed-data space.

The infinite-place Whittaker decay and fractional-lattice count of Lemma 4.6 therefore give, on the balanced norm representative and every compact reduction coordinate,
\[
|f(n(x)d(a(t))hk)|\le C_L\|f\|_2t^{-L}
\quad(t\ge1)
\tag{4.31}
\]
for every \(L\). The zero coefficient has already been removed; the proof uses the fixed small-radius exponents and arbitrarily high large-radius decay from that lemma. It is uniform in the function and in the compact coordinates. First applied with a finite moderate-growth seminorm instead of \(\|f\|_2\), the same argument proves rapid cusp decay and square integrability of any cusp form with these fixed data, so (4.30) does not presume an unproved square norm for such a form.

By the quotient integration bound of Lemma 4.9, the square norm outside a truncated compact reduction set with norm coordinate \(t\le R\) is at most \(C_L R^{-2L-1}\|f\|_2^2\). On that compact set, the elliptic equation and interior estimates give a uniform first Sobolev bound. Rellich compactness there, followed by this arbitrarily small uniform tail bound, makes the whole square-norm unit ball of the fixed-data solution space precompact. The space is closed: the fixed level and compact types are bounded orthogonal projections, and the infinitesimal equations and zero constant term persist under distributional limits. Its unit ball is therefore compact. An infinite-dimensional inner-product space has an orthonormal sequence with no convergent subsequence; hence this space is finite-dimensional.

**Proof of the decomposition.** Every compact/type idempotent corner in the cuspidal space with fixed infinitesimal characters now has finite-dimensional range. The Hecke action is a star action for the square-norm inner product. A finite-dimensional corner algebra is accordingly a sum of full matrix algebras: diagonalize its self-adjoint elements and split their invariant orthogonal complements. Choose an irreducible module \(W\) for such a corner algebra \(e\mathcal H e\) in its finite-dimensional range, and let \(V=\mathcal H W\). Then \(eV=W\). A nonzero invariant submodule \(M\subset V\) has \(eM\ne0\): if \(eM=0\), adjointness and invariance make \(M\) orthogonal to every \(\mathcal H\)-translate of \(W\), hence to itself. Irreducibility of \(W\) gives \(eM=W\), so \(M=V\). Every other compact/type corner of \(V\) is finite-dimensional by the preceding result, proving admissibility. Its Hilbert closure introduces no new vectors in a fixed corner, since that finite-dimensional corner is already closed. Thus its smooth compact-finite vectors are exactly \(V\), and its orthogonal complement is invariant as well. Repeating and taking the orthogonal complement of all the obtained summands leaves no nonzero vector, since some corner fixes every smooth compact-finite vector and such vectors are dense. This gives the asserted orthogonal sum and admissibility. The algebraic restricted-tensor argument of Lesson 12 then identifies its irreducible local components. \(\square\)

**Corollary 4.13 — the cuspidal exceptional-set converse.** If there is no global Hecke pair \(\mu,\nu\) with \(\pi_v=I(\mu_v,\nu_v)\) almost everywhere, there is a cuspidal automorphic representation \(\pi'\) with \(\pi'_v=\pi_v\) for every \(v\notin S\). The same conclusion holds if one prescribed finite-place representation outside \(S\) is supercuspidal.

**Proof.** Lemma 4.11 makes every constant term of the image \(U\) zero under the first hypothesis. Under the second, evaluation of a nonzero constant term would give a nonzero upper-unipotent invariant functional on that local supercuspidal representation; its zero Jacquet module, proved in Lesson 7, excludes this directly. Hence \(U\) consists of cusp forms in either case. Every full right translate is again cuspidal, with the same infinite infinitesimal characters. A positive determinant norm twist makes \(\eta\) unitary. The rapid-decay and square-integrability part of Lemma 4.12 puts the resulting vectors in the cuspidal Hilbert space.

Decompose the full right module generated by \(U\) as in Lemma 4.12. At least one irreducible summand has nonzero orthogonal projection of \(U\); the projection commutes with \(G^S\). Its kernel on the irreducible prescribed module is consequently zero. The restricted-tensor theorem and its fixed-idempotent formula, Lesson 12, Theorem 6.1, imply equality of every local component outside \(S\). Remove the common norm twist to obtain the stated cuspidal \(\pi'\). Its components in \(S\) have not been determined by this argument. \(\square\)


The primary comparison is Jacquet–Langlands, Theorem 11.5, Lemmas 11.4, 11.5.1 and 11.5.4, printed pp. 190–203; the separate cuspidality statement is Corollary 11.6, printed p. 203. The identities above use the local conventions of this course and give their own unfolding, chart extension and moderate-growth argument.

## 5. Classical consequences and a computed oldform warning

### 5.1. A newform line inside one cuspidal representation

Let \(f\) be a normalized primitive holomorphic newform of weight \(k\geq2\), level \(N\) and character \(\chi\). Lesson 14, Lemma 6.1, proves that its adelic lift generates an irreducible representation \(\pi_f\) and that
\[
N=\prod_p p^{c(\pi_{f,p})}.
\tag{5.1}
\]
Its real component is \(D_k\). At each finite prime, Lesson 8, Theorem 2.1, gives a one-dimensional newvector space at its minimal conductor. The restricted tensor product of those lines, tensored with the holomorphic lowest-weight line in \(D_k\), is one-dimensional.

Theorem 2.1 gives only one automorphic occurrence of that representation. Therefore two normalized primitive forms realizing the same \(\pi_f\) are proportional, and their coefficients of \(q\) make the proportionality constant one. This proves classical multiplicity one for prescribed full local data.

### 5.2. Example: equal prime coefficients at different proposed levels

Suppose \(f,g\) are normalized primitive newforms of the same weight \(k\geq2\), levels \(N,N'\), with
\[
a_p(f)=a_p(g)
\qquad(p\nmid 2NN').
\tag{5.2}
\]
Their characters need not initially be specified as equal.

For this character-recovery step only, use LG-MF-10, Lemma 4.1. Its explicitly stated arithmetic inputs are the attached Shimura–Deligne two-dimensional Galois representations and Chebotarev. The lemma proves that the two Dirichlet characters agree after pullback to a common modulus. Its argument takes equality of Frobenius traces to equality of continuous traces everywhere and uses
\[
2\det A=(\operatorname{tr}A)^2-\operatorname{tr}(A^2)
\tag{5.3}
\]
to recover the determinant character. We import this lemma, not that lesson's classical strong multiplicity-one conclusion. If the character was already fixed, these arithmetic inputs are unnecessary.

Call the common character \(\chi\). For every prime in (5.2), the normalized inverse local \(L\)-polynomial is
\[
\begin{gathered}
P_{f,p}(X)
 =1-a_p(f)p^{-(k-1)/2}X+\chi(p)X^2,\\
P_{g,p}(X)
 =1-a_p(g)p^{-(k-1)/2}X+\chi(p)X^2,\\
P_{f,p}(X)=P_{g,p}(X),\qquad X=p^{-s}.
\end{gathered}
\tag{5.4}
\]
Thus the two unordered Satake pairs agree, including both trace and determinant. Lesson 13, Theorem 3.2, identifies the corresponding spherical representations. Theorem 3.1 gives \(\pi_f\simeq\pi_g\).

All local conductors consequently agree, and (5.1) gives \(N=N'\). The holomorphic newvector line of §5.1 is then common to the two forms. Weak multiplicity one and \(a_1(f)=a_1(g)=1\) give \(f=g\), with equality of *all* Fourier coefficients, including those at the previously excluded primes.

For \(\Delta\), the good local polynomials at \(2\) and \(3\), with \(k=12\), are explicitly
\[
\begin{gathered}
P_{\Delta,2}(X)
 =1+\frac{24}{2^{11/2}}X+X^2,\\
P_{\Delta,3}(X)
 =1-\frac{252}{3^{11/2}}X+X^2.
\end{gathered}
\tag{5.5}
\]
The example (5.2) need not supply either of these two coefficients. Strong multiplicity one recovers the corresponding local representations from the remaining prime data.

### 5.3. Why this does not identify arbitrary oldform vectors

Inside level \(2\), set \(V_2\Delta(z)=\Delta(2z)\). The two vectors
\(\Delta,V_2\Delta\) are independent: the first has coefficient of \(q\) equal to one, while the second starts with \(q^2\).

For odd \(p\), the usual coefficient formula for \(T_p\) shows
\[
T_p(V_2\Delta)=V_2(T_p\Delta)=\tau(p)V_2\Delta.
\tag{5.6}
\]
Indeed the coefficient at \(q^n\) on the left is zero for odd \(n\). For \(n=2m\) it is
\(\tau(pm)+p^{11}\tau(m/p)=\tau(p)\tau(m)\), with the usual convention that a nonintegral index contributes zero. This is the coefficient on the right.

Both vectors therefore have the same good-prime eigenvalues. They are two oldvectors in the same representation, not two copies of it.

At the bad prime, the level-\(2\) operator is \(U_2\). The level-\(1\) relation \(T_2\Delta=-24\Delta\) gives
\[
\begin{gathered}
U_2\Delta=-24\Delta-2048V_2\Delta,\\
U_2(V_2\Delta)=\Delta,\\
[U_2]_{(\Delta,V_2\Delta)}
 =\begin{pmatrix}-24&1\\-2048&0\end{pmatrix},\\
\det(\lambda I-U_2)=\lambda^2+24\lambda+2048.
\end{gathered}
\tag{5.7}
\]
The coefficient \(2048=2^{11}\) is the classical weight normalization. This two-dimensional oldspace is entirely compatible with weak multiplicity one and with the one-dimensional minimal newspace.

## 6. The group matters

The unrestricted strong multiplicity-one assertion fails for \(\mathrm{SL}_2\). Different members of global packets can have the same components away from a finite set. This is a stated comparison, not a theorem proved here; see Chai–Zhang, [Introduction, §1](https://arxiv.org/html/1511.00354v1#S1), which discusses this failure and states a theorem with additional common-generic, archimedean and dyadic hypotheses.

A blanket claim of failure for inner forms would be incorrect. Strong multiplicity one holds for inner forms of \(\mathrm{GL}_n\) in characteristic zero; see the precise claim in the [Badulescu–Grbac abstract](https://arxiv.org/abs/0704.2920). For a quaternion multiplicative group, the later Jacquet–Langlands transfer lesson gives the relevant connection with \(\mathrm{GL}_2\). These comparisons are not used in the proofs above.

## 7. Exercises with complete solutions

### 7.1. Zero Whittaker function

**Exercise 7.1 — easy.** Prove that \(W_\phi=0\) implies \(\phi=0\). Explain why \(W_\phi(1)=0\) is a weaker hypothesis.

**Solution 7.1.** Equation (1.2) identifies every nonconstant Fourier coefficient of \(x\mapsto\phi(n(x)g)\) with a value of \(W_\phi\). Its constant coefficient is zero by cuspidality. Under the hypothesis all these coefficients vanish, so the convergent Fourier expansion gives \(\phi(g)=0\) for every \(g\). A condition at the identity only makes one value zero; it gives no information about \(W_\phi(d(\alpha)g)\) at other arguments. Thus it does not supply the vanishing used in this proof.

### 7.2. Classical multiplicity one

**Exercise 7.2 — medium.** Deduce uniqueness of normalized newforms from the adelic multiplicity statements. State which assertion is needed if only good-prime data are specified.

**Solution 7.2.** Prescribe one cuspidal representation with real component \(D_k\) and conductor \(N\). Its finite minimal newvector space is a tensor product of one-dimensional spaces, by Lesson 8; tensor it with the holomorphic lowest-weight line. Lesson 12's fixed-space formula makes this a one-dimensional global vector space. Theorem 2.1 places it in a unique automorphic occurrence. Any two forms realizing those data are proportional, and their coefficient of \(q\) makes the constant one.

If only the good Satake pairs are prescribed, first apply strong multiplicity one to identify all local components; then apply the argument just given. If only the numbers \(a_p\) are prescribed and the character is not, first recover the determinant character by the stated arithmetic lemma in §5.2. Neither weak multiplicity one nor equality of traces alone may silently replace that step.

### 7.3. Why twists enter the converse theorem

**Exercise 7.3 — medium.** Explain what information is missing from an untwisted functional equation. Compare the role of idele-class twists with Dirichlet twists in the classical converse problem.

**Solution 7.3.** Over \(\mathbb Q\), the idele-class quotient can be written as
\[
\mathbb Q^\times\backslash\mathbb A^\times
 \simeq \mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}.
\tag{7.1}
\]
Let \(\rho\) be a nontrivial character of a finite quotient of
\(\widehat{\mathbb Z}^{\,\times}\), and let \(H\) be a nonzero nonnegative smooth compactly supported function on \(\mathbb R_{>0}\). Put \(F(t,u)=H(t)\rho(u)\). Then
\[
\begin{gathered}
\int F(t,u)t^{s-1/2}\frac{dt}{t}\,du=0,\\
\int F(t,u)\rho(u)^{-1}t^{s-1/2}\frac{dt}{t}\,du
 =\int_0^\infty H(t)t^{s-1/2}\frac{dt}{t}.
\end{gathered}
\tag{7.2}
\]
The first equality holds because a nontrivial compact-group character has mean zero. The second transform is strictly positive at \(s=1/2\), so it is not identically zero. Thus the untwisted transform misses a whole nonzero compact-variable Fourier component.

This is an example about recovering functions, not a claim that \(F\) is the Whittaker series of a candidate representation. It identifies the gap in an argument that would infer Weyl invariance from only its averaged torus identity. All character twists recover the missing compact Fourier coefficients. Norm twists alone merely shift \(s\) and do not recover them.

A finite compact-variable character is a Dirichlet character, with its compatible parity at infinity. At level one, Hecke's Mellin inversion already recovers inversion and translation, hence both modular generators: LG-MF-12, Theorem 4.1. At general level \(N\), the untwisted equation recovers the Fricke relation; the character twists supply the missing residue-class information. That lesson's §5 states Weil's converse, retaining its separate condition for the cuspidal conclusion. Our compact Fourier calculation explains the same recovery mechanism adelically, while Theorem 4.1 also accommodates nonholomorphic real types and arbitrary generic finite components. It does not prove Weil's theorem. The full twist family in Theorem 4.1 is a sufficient hypothesis; this exercise does not assert that every member is individually necessary in every refined converse theorem.

### 7.4. Recovering every missing local component

**Exercise 7.4 — hard.** Assume the global converse theorem and the local converse theorem of Lesson 9. Prove strong multiplicity one for \(\mathrm{GL}_2/\mathbb Q\).

**Solution 7.4.** We give the proof for unitary cuspidal representations; §3 explains the common norm twist for the essentially unitary case. We use the analytic conditions supplied by Lesson 14 and the local converse theorem. The global converse is available under the exercise's assumptions, but its automorphy conclusion is not needed: the two starting representations are already automorphic.

**Step 1: compare finite products.** Choose a finite \(S\) containing infinity and every place where the components may differ. Their central characters agree by (3.2) and weak approximation.

Fix any global unitary character \(\chi\). In an initial right half-plane, Euler products give
\[
\frac{L(s,\pi\otimes\chi)}
     {L(s,\pi'\otimes\chi)}
 =\prod_{v\in S}
   \frac{L(s,\pi_v\otimes\chi_v)}
        {L(s,\pi'_v\otimes\chi_v)}.
\tag{7.3}
\]
The quotient is a meromorphic function; neither denominator is identically zero. Continue (7.3) using Lesson 14. Apply the two twisted global functional equations, and compare the analogous dual quotient. With
\[
R_v(s,\chi_v)=
 \frac{\gamma(s,\pi_v\otimes\chi_v,\psi_v)}
      {\gamma(s,\pi'_v\otimes\chi_v,\psi_v)}
\]
we obtain the meromorphic identity
\[
\prod_{v\in S}R_v(s,\chi_v)=1.
\tag{7.4}
\]
Only finite products have been used. Even if \(\chi\) is ramified outside \(S\), the two local representations there are isomorphic, so their ratios still cancel.

**Step 2: isolate zeros and poles at each finite prime.** For finite \(p\), \(R_p(s,\chi_p)\) is a nonzero rational function of \(X=p^{-s}\), by Lesson 9. A zero or pole at \(X_0\in\mathbb C^\times\) produces a full vertical progression
\[
s=s_0+\frac{2\pi i n}{\log p},
\qquad n\in\mathbb Z.
\tag{7.5}
\]
For distinct primes \(p,q\), two such progressions intersect at most once. Otherwise subtraction of two intersection equations would make \(\log p/\log q\) rational. Raising \(p,q\) to the corresponding integer powers contradicts unique prime factorization.

Each finite rational function has only finitely many such progressions. The real gamma-factor ratio has its zeros and poles on finitely many horizontal progressions, from its \(\Gamma_{\mathbb R}\) and \(\Gamma_{\mathbb C}\) factors. A vertical progression meets each of these at most once. Hence the other factors in (7.4) can cancel only finitely many points of a proposed progression (7.5), contradicting (7.4).

Thus no finite \(R_p\) has a zero or pole on \(\mathbb C^\times\) in the variable \(X\). A rational function with that property is a Laurent monomial:
\[
\begin{gathered}
R_p(s,\chi_p)=b_p(\chi_p)p^{m_p(\chi_p)s},\\
b_p(\chi_p)\ne0,\qquad m_p(\chi_p)\in\mathbb Z.
\end{gathered}
\tag{7.6}
\]
Indeed factor numerator and denominator over \(\mathbb C\); after common factors cancel, their only possible roots are zero. Equation (7.4) now says that \(R_\infty\) also has no zeros or poles.

**Step 3: use the unitary pole separation.** For a unitary generic local representation, every pole of its \(L(s)\) has real part strictly less than \(1/2\). Every pole of its dual \(L(1-s)\) consequently has real part strictly greater than \(1/2\).

Here are the inputs for that strict assertion. At a finite prime the unitary principal-series characters have real norm exponents in \((-1/2,1/2)\); the complementary endpoint is excluded for a generic irreducible principal series. Unitarily twisted Steinberg has factor
\((1-\mu(p)p^{-s-1/2})^{-1}\), and supercuspidals have factor one. Ramified principal-series characters simply omit the corresponding factors. These are Lesson 7, §7, and Lesson 9, §1; the finite unitary-dual classification is proved in Lesson 7, Theorem 7.1.

At infinity the generic unitary possibilities from Lesson 11, Proposition 4.1, have factors
\[
\begin{gathered}
\Gamma_{\mathbb R}(s+\epsilon_1+it_1)
 \Gamma_{\mathbb R}(s+\epsilon_2+it_2),\\
\Gamma_{\mathbb R}(s+\epsilon+it+r)
 \Gamma_{\mathbb R}(s+\epsilon+it-r),\\
0<r<1/2,\\
\Gamma_{\mathbb C}(s+(k-1)/2+it),
 \qquad k\geq1.
\end{gathered}
\tag{7.7}
\]
Here \(t,t_j\) are real and \(\epsilon,\epsilon_j\in\{0,1\}\); the first line is tempered principal series, the second complementary series, the third \(D_k|\det|^{it}\). Their poles have the asserted positions. Gamma factors have no zeros, and epsilon factors are nonzero exponentials.

In the half-plane \(\operatorname{Re}s<1/2\), the dual factors contribute neither zeros nor poles. Since every \(R_v\) has none, the pole divisors of
\(L(s,\pi_v\otimes\chi_v)\) and
\(L(s,\pi'_v\otimes\chi_v)\) agree there, and hence agree everywhere. For finite \(p\), these factors are inverse polynomials with constant term one, so they are equal.

For the real place, even the untwisted pole divisor determines the generic unitary representation. A tempered principal factor has two progressions of step two, starting at \(-\epsilon_j-it_j\). Their imaginary parts, starting points and multiplicities recover the unordered two character parameters. A complementary factor has two step-two progressions with the same imaginary part and distinct real starting points \(-\epsilon\pm r\); their separation \(2r<1\) recovers \(r,\epsilon,t\). A discrete or limit factor has one step-one progression starting at \(-(k-1)/2-it\), which recovers \(k,t\).

The only overlap between these descriptions is a tempered principal pair of opposite parities with the same \(t\): its two step-two progressions combine into the step-one divisor of \(\Gamma_{\mathbb C}(s+it)\). Lesson 11, Theorem 3.2, identifies that principal module with the same \(D_1|\det|^{it}\), so it causes no ambiguity. A nonzero complementary \(r<1/2\) cannot give a step-one progression; equal-parity tempered pairs have double step-two poles instead. No \(D_k\) with \(k\geq2\) is such a principal pair.

Therefore
\[
\pi_\infty\simeq\pi'_\infty.
\tag{7.8}
\]
It follows that \(R_\infty(s,\chi_\infty)=1\) for every real character twist.

**Step 4: remove the finite exponents.** For the fixed global \(\chi\), insert (7.6) and (7.8) into (7.4). Differentiating the nonzero exponential identity gives
\[
\sum_{p\in S,\ p<\infty}m_p(\chi_p)\log p=0.
\]
Equivalently \(\prod_p p^{m_p(\chi_p)}=1\). Unique prime factorization forces every \(m_p(\chi_p)=0\). Thus every finite ratio is constant in \(s\).

**Step 5: show its constant does not depend on the local twist.** Fix \(p\in S\) and any unitary smooth character \(\mu:\mathbb Q_p^\times\to\mathbb C^\times\). It extends to a global unitary character ramified only at \(p\). To see this, the restriction of \(\mu\) to \(\mathbb Z_p^\times\) factors through a finite quotient. Use that Dirichlet character on the compact idele-class factor, choosing the matching sign at infinity. Its \(p\)-uniformizer value is initially one. An imaginary norm twist adjusts this value to \(\mu(p)\), since \(p^{-it}\) runs through the unit circle. At every other finite prime the resulting local character is unramified.

An unramified character at \(q\ne p\) is \(|\cdot|_q^{it_q}\), so
\[
R_q(s,\chi_q)=R_q(s+it_q,1)=b_q(1).
\tag{7.9}
\]
The real ratio is one. Compare (7.4) for this \(\chi\) and for the trivial character. All other constants cancel, giving
\[
R_p(s,\mu)=b_p(1)=:b_p.
\tag{7.10}
\]
Every local quasicharacter is a unitary one times a real norm power. Shifting \(s\) extends (7.10) to all local quasicharacters.

**Step 6: determine \(b_p\), rather than assume it is one.** Use the two scalar Kirillov models, with their common compact part
\[
V_0=C_c^\infty(\mathbb Q_p^\times).
\]
Their central characters and their upper-triangular actions agree. Denote their Weyl operators by \(W,W'\). For a unit character \(\alpha\), take the shell-zero tests in Lesson 9, equation (7.3). Their generating functions recover every unit-Fourier coefficient of the Weyl transform. Relation (7.10) therefore gives
\[
W\xi=b_p W'\xi
\qquad(\xi\in V_0).
\tag{7.11}
\]
More explicitly, choose the twisting character whose unit restriction is
\((\alpha\,\omega|_{\mathbb Z_p^\times})^{-1}\) and whose value at \(p\) is one. The right Mellin integral of the test
\((\alpha\,\omega|_{\mathbb Z_p^\times})1_{\mathbb Z_p^\times}\)
is one. The two gamma functions are then the generating functions of the two Weyl transforms, in the same Laurent variable. Their ratio \(b_p\) multiplies every coefficient. Unique Laurent expansion and unit Fourier inversion give (7.11) for arbitrary compact \(\xi\).

The germ quotients of both Kirillov models by \(V_0\) are finite-dimensional, by Lesson 7, Proposition 6.2 and equations (3.1), (6.2). Hence the linear map
\(\xi\mapsto W'\xi\bmod V_0\), defined on the infinite-dimensional space \(V_0\), has a nonzero kernel. Choose \(0\ne\xi\in V_0\) with \(W'\xi\in V_0\). Apply (7.11) twice. The identity \(w_0^2=-I\) gives
\[
\omega(-1)\xi
 =W^2\xi=b_p^2 W'^2\xi
 =b_p^2\omega(-1)\xi,
\]
so \(b_p^2=1\).

Let \(N\) be the common operator for \(n(1)\). It preserves \(V_0\), since it multiplies a compact function by \(\psi_p(t)\). Choose another nonzero \(\xi\in V_0\) such that
\((W'N)\xi\) and \((W'N)^2\xi\) lie in \(V_0\). Such vectors form the intersection of two finite-codimension kernels, so the intersection remains infinite-dimensional. Along these three steps (7.11) applies at every Weyl operation. The exact matrix relation
\[
(w_0n(1))^3=-I
\tag{7.12}
\]
therefore gives
\[
\omega(-1)\xi
 =(WN)^3\xi=b_p^3(W'N)^3\xi
 =b_p^3\omega(-1)\xi.
\]
Thus \(b_p^3=1\). The two relations force \(b_p=1\).

**Step 7: apply local converse and tensor uniqueness.** We have proved
\[
\begin{gathered}
\gamma(s,\pi_p\otimes\mu,\psi_p)
 =\gamma(s,\pi'_p\otimes\mu,\psi_p),\\
\text{for every local quasicharacter }\mu.
\end{gathered}
\tag{7.13}
\]
The central characters agree, so Lesson 9, Theorem 7.1, gives
\(\pi_p\simeq\pi'_p\) at each missing finite prime. Equation (7.8) supplies the real place; all the other places agreed at the start. Lesson 12's tensor-product uniqueness gives \(\pi\simeq\pi'\). Theorem 2.1 identifies their cuspidal occurrences.

The proof neither replaces the unknown local constants by an unsupported value nor imports a high-ramification epsilon-stability theorem. The common compact Kirillov space and the two group relations determine those constants directly. \(\square\)

## 8. Prerequisites and source locators

The full rational-field converse theorem is proved in Sections 4.1–4.6. Theorem 4.5 and Lemmas 4.6–4.9 extend it to every global field: they supply the number-field lattice and complex smooth Mellin estimates, the function-field finite sum and Laurent uniqueness, compact Fourier recovery, an explicit adelic reduction and the cuspidal Hilbert realization. Lemma 4.2 proves convergence and cusp growth from local Kirillov germs, spherical coefficients and the real moderate-growth estimate. Lemma 4.3 extends the real normalized Mellin formulas to smooth translates. Section 4.4 supplies the strip bound, Lemma 4.4 gives two-sided Mellin uniqueness, and §4.6 proves rational Weyl invariance and the cuspidal embedding. The original theorem is Jacquet–Langlands, §11, Theorem 11.3, printed pp. 185–186; its comparison locators are Lemmas 11.3.1–11.3.3 and Lemma 11.4, printed pp. 189–197. Getz–Hahn, §11.9, Theorem 11.9.1, printed pp. 273–274 in the 2022 draft, gives modern context. Initial convergence and local genericity are retained explicitly.

The following earlier results supply the proofs: Lesson 14, Theorems 1.1, 2.1, 4.2 and 5.1, for Fourier reconstruction, product Whittaker maps and the entire twisted functional equations; Lesson 12, Theorem 6.1 and its fixed-space formula, for restricted tensors and uniqueness; Lesson 9, Theorem 7.1 and equations (7.2)–(7.3), for local converse and Weyl recovery; Lesson 7, Theorem 2.3, Proposition 6.2 and equations (3.1), (6.2), for compact Kirillov functions and finite-dimensional germs; Lesson 11, Theorem 3.2, Proposition 4.1 and Theorems 5.1–6.1, for the real classification and factors.

The finite unitary-dual classification used in Solution 7.4 is proved in Lesson 7, Theorem 7.1. Its original authority is Tadić, Theorem D and §7.5, specialized to rank two. The proof uses its strict complementary-series range, not a false claim that every unitary Satake parameter has modulus one. Lesson 11, Sections 4–5 and 8, supplies the explicit real and complex models, Hilbert admissibility, moderate Whittaker uniqueness and radial equations used here.

For the classical comparison, Lesson 14, Lemma 6.1, proves irreducible generation and minimal conductor; Lesson 8, Theorem 2.1, supplies the local newvector lines, and Lesson 13, Theorem 3.2, identifies spherical representations. Only when the characters are not initially fixed do we import LG-MF-10, Lemma 4.1. Its arithmetic inputs are Diamond–Im, §12.5, equations (12.5.1)–(12.5.3), printed p. 120, with Corollary 12.4.5, printed p. 115, and Milne, *Algebraic Number Theory*, Theorem 8.31. No Galois-representation construction is proved in this lesson.

The group comparisons in §6 are stated context from the cited Chai–Zhang introduction and Badulescu–Grbac abstract. We do not prove the packet theory of \(\mathrm{SL}_2\), the general converse theorem for \(\mathrm{GL}_n\), or the general inner-form correspondence.

Theorem 4.10, Lemmas 4.11–4.12 and Corollary 4.13 now prove the exceptional-set converse over every global field: weighted Mellin recovery and rational chart extension give automorphy; explicit zero-frequency equations and finite torus weights give the Eisenstein alternative; additive annihilators in function fields and uniform elliptic/Fourier tails in number fields give finite cuspidal spaces and constituent selection. Their primary comparison is Jacquet–Langlands, Theorem 11.5 and Corollary 11.6, printed pp. 197–203, with Lemma 11.4 for growth.

## References

- H. Jacquet and R. P. Langlands, *Automorphic Forms on GL(2)*, Lecture Notes in Mathematics 114, 1970, §11: Proposition 11.1.1; Theorem 11.3 and Lemmas 11.3.3, 11.4; Theorem 11.5 and Corollary 11.6. See the [author's text collection](https://publications.ias.edu/rpl/section/22).
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §11.9, Theorem 11.9.1, printed pp. 273–274; see the [author's text page](https://sites.duke.edu/jgetz/graduate-text/).
- D. Goldfeld and H. Jacquet, “Automorphic Representations and L-Functions for GL(n),” in J. Mueller, ed., *The Genesis of the Langlands Program*, 2021, Chapter 13, pp. 215–274. Sections 13.2–13.4 and 13.8–13.9 provide local, tensor-product and cuspidal analytic background; this chapter is not the source of Theorem 4.1.
- LG-MF-10, oldforms, newforms and the theory of Atkin–Lehner and Li, Lemma 4.1, for the separately stated arithmetic character-recovery step.
- J. Chai and Q. Zhang, [*A strong multiplicity one theorem for SL(2)*](https://arxiv.org/html/1511.00354v1#S1), 2015 preprint, Introduction, §1.
- A. I. Badulescu, with appendix by N. Grbac, [*Global Jacquet–Langlands correspondence, multiplicity one and classification of automorphic representations*](https://arxiv.org/abs/0704.2920), 2007 preprint, abstract, for the inner-form scope correction.

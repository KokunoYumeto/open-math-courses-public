# Traces on integer crossed products and their K-theory ranges

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Independently authored CC0 lesson; self-checked by the writing AI.*

An invariant trace measures the constant Fourier coefficient of an integer crossed product. Its values on projections can include new numbers. Those new numbers, modulo the old trace range, are determinants of the change made by the automorphism to a fixed K-class. We prove this assertion, including the numerical comparison that connects a mapping-torus integral to an actual crossed-product trace.

Let \(A\) be a unital complex C*-algebra, \(\alpha\in\operatorname{Aut}(A)\), and \(\tau\) an \(\alpha\)-invariant tracial state. Put

\[
\begin{gathered}
B=A\rtimes_\alpha\mathbb Z,\\
uau^*=\alpha(a),\qquad \iota:A\longrightarrow B.
\end{gathered}
\tag{0.1}
\]

Matrix traces are unnormalized. Write \(H=\tau_*(K_0(A))\subset\mathbb R\); quotients by \(H\) below are quotients of additive groups, without taking a closure. We use [Lesson 14, §§1–2](KT-OPK-14.md#1-the-logarithmic-integral-and-its-periods) for the integral \(\Gamma_\tau\), its period group \(H\), and the unitary determinant \(\Delta_\tau:U_\infty(A)_0\to\mathbb R/H\). The mapping-torus integral is that lesson's Theorem 4.1. Lesson 18 supplies the PV sequence and its actual inclusion arrows.

## 1. The dual trace and agreement of trace extensions

The gauge action \(\beta_t\), for \(t\in\mathbb R/\mathbb Z\), fixes \(A\) and sends \(u\) to \(e^{2\pi it}u\). Its average is the faithful conditional expectation

\[
\begin{gathered}
E(b)=\int_0^1\beta_t(b)\,dt,\\
E\left(\sum_n a_nu^n\right)=a_0.
\end{gathered}
\tag{1.1}
\]

The crossed product equals its reduced version by amenability of \(\mathbb Z\). The expectation and gauge facts are the Fourier construction in [KT-CP-05, Proposition 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-05.html#an-automorphism-and-its-gauge-action). Faithfulness of the average also follows directly: if \(b\geq0\) and its average is zero, then for every state \(\omega\) the nonnegative continuous function \(t\mapsto\omega(\beta_t(b))\) has integral zero, hence is zero at \(t=0\). States separate positive elements, so \(b=0\).

**Proposition 1.1.** The state \(\widehat\tau=\tau E\) is a trace extending \(\tau\). Every tracial state on \(B\) restricts to an invariant tracial state on \(A\). If \(\tau\) is faithful, so is \(\widehat\tau\).

*Proof.* Positivity and normalization follow from the average. On monomials \(au^m,bu^n\), the traces of their two products are zero unless \(m+n=0\). When \(n=-m\), invariance and cyclicity give

\[
\tau(a\alpha^m(b))=\tau(b\alpha^{-m}(a)).
\tag{1.2}
\]

Thus the trace identity holds on Laurent polynomials; density and boundedness extend it to \(B\). For a trace \(\rho\) on \(B\), cyclicity gives \(\rho(uau^*)=\rho(a)\), proving invariance of its restriction. Finally \(\widehat\tau(b^*b)=0\) implies \(E(b^*b)=0\) when \(\tau\) is faithful, and then \(b=0\) by faithfulness of \(E\). \(\square\)

**Theorem 1.2 (all extensions have the same K₀-state).** If \(\rho\) is any tracial state on \(B\) restricting to \(\tau\), then \(\rho_* =\widehat\tau_*\) on \(K_0(B)\).

*Proof.* For a projection \(p\in M_n(B)\), the path \(s\mapsto\beta_s(p)\), \(0\leq s\leq t\), consists of projections. Thus \([\beta_t(p)]=[p]\) in \(K_0(B)\). A trace pairing is constant on that class by Lesson 13, Theorem 1.1. Consequently

\[
\begin{gathered}
\rho_n(p)=\int_0^1\rho_n(\beta_t(p))\,dt\\
=\rho_n(E_n(p))=\tau_n(E_n(p))\\
=\widehat\tau_n(p).
\end{gathered}
\tag{1.3}
\]

The integral commutes with the bounded linear functional \(\rho_n\). Differences of projections generate \(K_0(B)\), proving the result. This supplies the proof omitted in Blackadar, §10.10.1; no extra hypothesis on \(A\) or the trace extension is required. \(\square\)

Equality of K-pairings is weaker than equality of traces. For the trivial action on \(A=\mathbb C\), the crossed product is \(C(S^1)\). All probability measures give trace extensions of the scalar state, and all pair with a projection by its constant rank.

## 2. A determinant on fixed K₁-classes

Put \(F=\ker(1-\alpha_*:K_1(A)\to K_1(A))\). If \(x=[v]\in F\), choose a unitary matrix representative. The stable class of \(v\alpha(v^*)\) is zero. After identity padding, it lies in the unitary identity component. Define

\[
R_\tau^\alpha(x)=\Delta_\tau(v\alpha(v^*))\in\mathbb R/H.
\tag{2.1}
\]

This is also often written \(\Delta_\tau^\alpha\).

**Lemma 2.1.** Equation (2.1) is a well-defined homomorphism on \(F\).

*Proof.* First \(\Delta_\tau(\alpha(w))=\Delta_\tau(w)\) on the identity component: apply \(\alpha\) to a path from 1 and use \(\tau\alpha=\tau\) in its logarithmic integral. Conjugating such a path by an arbitrary fixed unitary also preserves the integral, by trace cyclicity.

Suppose \(v_s\) joins two stabilized representatives of the same K-class. Replace the path by a piecewise smooth unitary path in its homotopy class, as in Lesson 14, §1. Each \(r_s=v_s\alpha(v_s^*)\) lies in the identity component. The product and inverse rules for the integral apply even to paths with nonidentity endpoints and give

\[
\begin{gathered}
\Gamma_\tau(r_s)=\Gamma_\tau(v_s)-\Gamma_\tau(\alpha(v_s))\\
=0.
\end{gathered}
\tag{2.2}
\]

Appending this path to a path from 1 to \(r_0\) shows that the determinants of \(r_0\) and \(r_1\) agree modulo \(H\). Identity stabilization adds zero, proving independence of representative and size. Finally block sum represents addition of K-classes, and its logarithmic trace is the sum of the two logarithmic traces. Applying this to \(v\oplus w\) proves additivity. \(\square\)

This proof does not apply \(\Delta_\tau\) to \(v\) unless \(v\) is in its domain. A fixed K-class makes the *relative product* in (2.1) nullhomotopic; its chosen representative can have nonzero K₁-class.

### Composition and iteration on their exact domains

The next results develop Ruy Exel's rotation and invariant-determinant constructions, Sections III–IV of [*Rotation numbers for automorphisms of C*-algebras*](https://msp.org/pjm/1987/127-1/pjm-v127-n1-p03-s.pdf), printed pp. 45–50. We give the proofs with the present additive determinant convention. Composition works for the actual period subgroup \(H\), even when \(H\) is not integral.

**Theorem 2.2 (composition of rotations).** Suppose \(\alpha\) and \(\beta\) preserve \(\tau\). On the subgroup fixed by both \(\alpha_*\) and \(\beta_*\),

\[
\begin{gathered}
R_\tau^{\alpha\beta}(x)=R_\tau^\alpha(x)+R_\tau^\beta(x).
\end{gathered}
\tag{2.3}
\]

No commutativity between the automorphisms is required. For every \(n\in\mathbb Z\),

\[
R_\tau^{\alpha^n}(x)=nR_\tau^\alpha(x)
\quad\text{if }\alpha_*x=x.
\tag{2.4}
\]

*Proof.* Choose one unitary representative \(v\) of \(x\), and pad it so that both relative products are in the identity component. The class is also fixed by \((\alpha\beta)_*\). The exact factorization is

\[
\begin{gathered}
v\alpha\beta(v^*)\\
=\bigl(v\alpha(v^*)\bigr)\,
\alpha\bigl(v\beta(v^*)\bigr).
\end{gathered}
\]

Apply additivity of \(\Delta_\tau\) on this component and its invariance under \(\alpha\), proved in Lemma 2.1. This gives (2.3). Induction gives (2.4) for positive \(n\); \(R_\tau^{\mathrm{id}}=0\). The same class is fixed by \(\alpha_*^{-1}\), so applying (2.3) to \(\alpha,\alpha^{-1}\) gives \(R_\tau^{\alpha^{-1}}=-R_\tau^\alpha\). Induction with \(\alpha^{-1}\) completes the integer assertion. \(\square\)

The fixed subgroup of \(\alpha_*^n\) can be larger than that of \(\alpha_*\). Formula (2.4) concerns the latter subgroup; it makes no assertion about the additional classes.

### An obstruction to invariant determinants

For this paragraph assume \(H\subseteq\mathbb Z\). Since \(\tau(1)=1\), this is equivalent to \(H=\mathbb Z\). [Lesson 14, Theorem 2.10](KT-OPK-14.md#2-5-extending-a-determinant-to-every-stable-unitary) gives a homomorphism \(D:U_\infty(A)\to\mathbb T\) satisfying

\[
\begin{gathered}
D(e^{ih})=e^{i\tau_n(h)},\\
h=h^*\in M_n(A).
\end{gathered}
\tag{2.5}
\]

It is defined on every component. Each choice is continuous on every finite unitary group. Different choices are precisely \(D\chi\), where \(\chi\) is a character of \(K_1(A)\). No closure of a commutator subgroup is part of this construction.

Let \(G\) be any group acting on \(A\) by trace-preserving automorphisms. Use ordinary algebraic group cohomology, with no topology imposed on \(G\). The character group
\(X=\operatorname{Hom}(K_1(A),\mathbb T)\)
has the action

\[
(g\cdot\chi)(x)=\chi(g_*^{-1}x).
\tag{2.6}
\]

Every \(D\) is \(G\)-invariant on \(U_\infty(A)_0\): factor an element there into selfadjoint exponentials, apply \(g\), and use \(\tau g=\tau\) in (2.5). Therefore

\[
\begin{gathered}
c_g([v])=\frac{D(v)}{D(g^{-1}(v))}\\
=D(g^{-1}(v^*)v)
\end{gathered}
\tag{2.7}
\]

defines a character of \(K_1(A)\). Indeed the ratio is a homomorphism on the stable unitary group, and it is trivial on its identity component. Its passage to that quotient proves independence of representative and matrix size.

**Theorem 2.3 (Exel's invariant determinant obstruction).** The family \(c\) is a one-cocycle:

\[
c_{gh}=c_g\,(g\cdot c_h).
\tag{2.8}
\]

Its class in \(H^1(G,X)\) is independent of the chosen determinant. This class vanishes exactly when a \(G\)-invariant determinant exists. If \(D_0\) is invariant, every invariant determinant is \(D_0\chi\) with \(g\cdot\chi=\chi\) for all \(g\).

*Proof.* On a representative \(v\), cancellation gives

\[
\begin{gathered}
\frac{D(v)}{D(h^{-1}g^{-1}(v))}\\
=\frac{D(v)}{D(g^{-1}(v))}
\frac{D(g^{-1}(v))}{D(h^{-1}g^{-1}(v))}.
\end{gathered}
\]

This is (2.8), with the inverse order required by \((gh)^{-1}=h^{-1}g^{-1}\). If \(D'=D\chi\), then

\[
c'_g=c_g\,\frac{\chi}{g\cdot\chi}.
\tag{2.9}
\]

To make the cohomology statement explicit, one-cocycles are the families satisfying (2.8), and coboundaries are \(g\mapsto(g\cdot\chi)/\chi\). These form a subgroup of the cocycles under pointwise multiplication: inserting \(gh\) and canceling the intermediate \(g\cdot\chi\) verifies (2.8). The quotient is \(H^1(G,X)\). Equation (2.9) proves the asserted independence.

An invariant \(D\) gives \(c_g=1\). Conversely, if \(c_g=(g\cdot\chi)/\chi\), replacing \(D\) by \(D\chi\) gives \(c'_g=1\). Equation (2.7) says precisely that this determinant is invariant under \(g^{-1}\), hence under every element of \(G\). The classification follows by applying (2.9) to two invariant choices and using Lesson 14's classification of all choices. Restricting the action to a subgroup simply restricts this cocycle. \(\square\)

**Lemma 2.4 (circle rotation versus coset rotation).** For \(x=[v]\) fixed by \(\alpha_*\), the relative product has zero stable K₁-class, and

\[
\begin{gathered}
D(\alpha(v^*)v)
=\exp\bigl(2\pi iR_\tau^\alpha(x)\bigr)\\
=c_{\alpha^{-1}}(x).
\end{gathered}
\tag{2.10}
\]

The first value is independent of the all-components determinant chosen.

*Proof.* After finite padding, \(\alpha(v^*)v\) lies in the identity component. Conjugating it by \(v\) gives the relative product in (2.1). On that component \(D=\exp(2\pi i\Delta_\tau)\), by Lesson 14, Theorem 2.10, and conjugation preserves \(\Delta_\tau\). This gives the first equality. Put \(g=\alpha^{-1}\) in (2.7) for the second. A different choice multiplies the value on the relative product by the character of its K-class, which is the character at zero and hence one. \(\square\)

This compares the two rotation conventions without applying an identity-component determinant to the representative \(v\) itself.

## 3. Why the mapping-torus integral measures the crossed-product trace

An exact K-sequence alone does not identify a numerical trace pairing. We establish that additional comparison using two precise proved prerequisites:

- [KT-CP-07, Theorem 7.4 and formulas (7.10)–(7.11), (7.45)](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html#completion-in-the-full-crossed-product-norms): Green's imprimitivity module for \(\mathbb Z\subset\mathbb R\).
- [Frequency calculus for an action of Euclidean space, §7, Theorem 7.6](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/pseudodifferential-calculus-for-actions-of-rn.html#computing-the-one-dimensional-trace): for a finite invariant trace \(\varphi\) and a smooth unitary \(w\), the index-normalized Thom map satisfies

\[
\widehat\varphi_*\Phi_\sigma^1[w]
=-\frac1{2\pi i}\varphi_n(\delta(w)w^*).
\tag{3.1}
\]

That theorem includes the semifinite dual trace normalization, its trace ideals, and its K-pairing. Its frequency convention is \(V_t=e^{itH}\) and measure \(d\xi/(2\pi)\). We use the same real group parameter and \(\Phi^1\), so (3.1)'s sign is retained. We use the complete programme proof of [*Morita invariance of K-theory and correspondence maps*, Theorem 2.4 and Corollary 2.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html). For the Green module \(X\), with left algebra \(E=C\rtimes_\sigma\mathbb R\) and right algebra \(B\), its actual map is \(\mu=(i_{B*})^{-1}i_{E*}\), where the inclusions are the two full diagonal corners of \(\mathcal K(X\oplus B)\). Both corner maps are proved invertible there without countability assumptions. Theorem 5.1 identifies this map on finite-projective-module classes; those are the Gram-projection classes in the next lemma. This exact written proof replaces the earlier literature-only prerequisite description.

Let \(C=M_{\alpha^{-1}}\). Extend \(f\in C\) to \(\mathbb R\) by \(f(r+n)=\alpha^{-n}(f(r))\), and set

\[
\begin{gathered}
(\sigma_t f)(r)=f(r-t),\\
\delta f=-f',\\
\varphi(f)=\int_0^1\tau(f(r))\,dr.
\end{gathered}
\tag{3.2}
\]

Uniform continuity on a compact interval, together with the endpoint relation and isometry of \(\alpha\), proves norm continuity of \(\sigma\). The function \(r\mapsto\tau(f(r))\) is period one. Thus \(\varphi\) is an invariant tracial state. Green's module \(X\) identifies \(C\rtimes_\sigma\mathbb R\) with \(\mathcal K_B(X)\).

**Lemma 3.1 (trace compatibility in Green's module).** Let \(\mu:K_0(C\rtimes_\sigma\mathbb R)\to K_0(B)\) be the Morita isomorphism defined by \(X\). Then

\[
\widehat\varphi_*y=\widehat\tau_*\mu(y).
\tag{3.3}
\]

*Proof.* Normalize counting measure on \(\mathbb Z\) and Lebesgue measure on \(\mathbb R\), whose quotient interval has length one. For \(x,y\in C_c(\mathbb R,A)\), put \(x_n(r)=\alpha^n(x(r+n))\) and \(y_n(r)=\alpha^n(y(r+n))\). The two Green inner products become

\[
\begin{gathered}
R(x,y)(n)\\
=\int_{\mathbb R}x(r)^*\alpha^n(y(r+n))\,dr,\\
L(x,y)(t,r)\\
=\sum_{n\in\mathbb Z}x_n(r)y_n(r-t)^*.
\end{gathered}
\tag{3.4}
\]

Their left action is \(L(x,y)=\theta_{x,y}\), where \(\theta_{x,y}z=xR(y,z)\). The dual trace on positive continuous core kernels evaluates their group-zero coefficient, with the tracial integration normalization preceding (3.1). Invariance of \(\tau\), partitioning \(\mathbb R\) into unit intervals, and cyclicity therefore give

\[
\begin{gathered}
\widehat\varphi(L(x,y))
=\int_{\mathbb R}\tau(x(r)y(r)^*)\,dr\\
=\widehat\tau(R(y,x)).
\end{gathered}
\tag{3.5}
\]

For diagonal terms these are nonnegative finite quantities; polarization gives the displayed general formula. The sums and integrals are finite on compact supports before taking the quotient interval.

Here is the completion and projection step in this trace comparison. For core vectors,
\(\widehat\varphi(\theta_{x,x})=\widehat\tau(R(x,x))\leq\|x\|_X^2\).
The positive two-by-two block \((\theta_{x_i,x_j})\), with \(x_1=x,x_2=y\), factors its off-diagonal entry as \(\theta_{x,x}^{1/2}c\theta_{y,y}^{1/2}\) for a contraction \(c\) in the tracial von Neumann completion. Applying the \(L^2\)-to-\(L^1\) inequality gives
\(\|\theta_{x,y}\|_1\leq\widehat\varphi(\theta_{x,x})^{1/2}\widehat\varphi(\theta_{y,y})^{1/2}\).
It follows, by expanding differences of rank ones, that approximating vectors in module norm also approximates these operators in trace norm. Thus (3.5) holds for all completed vectors. This uses the semifinite integration inequalities included in the exact analytic prerequisite, not boundedness of \(\widehat\varphi\) on the entire compact-operator algebra.

For a projection \(p\in M_k(\mathcal K_B(X))\), choose a positive finite-rank operator \(T=\sum_i\theta_{z_i,z_i}\) with \(\|p-pTp\|<1\) in its corner. Such operators approximate compact operators. The positive operator \(pTp\) is invertible on \(pX^k\). Put \(y_i=(pTp)^{-1/2}pz_i\); then

\[
\sum_i\theta_{y_i,y_i}=p.
\tag{3.6}
\]

The column map \(V:B^N\to pX^k\), \(V(b_i)=\sum_i y_ib_i\), satisfies \(VV^*=p\). Hence \(e=V^*V=(R(y_i,y_j))\) is a projection in \(M_N(B)\), representing \(\mu[p]\). Summing (3.5) on its diagonal gives \(\widehat\varphi_k(p)=\widehat\tau_N(e)\).

These projection classes generate the whole K₀-group here. Indeed, fullness and unitality of \(B\) give finitely many vectors \(z_i\) with \(S=\sum_iR(z_i,z_i)\) positive and invertible; normalize them by \(S^{-1/2}\). The map \(b\mapsto(z_iS^{-1/2}b)_i\) embeds \(B\) as a complemented summand of \(X^N\). Its range projection is a full projection in \(M_N(\mathcal K_B(X))\), with corner \(B\). Fullness follows because every rank one factors through this column and its adjoint. The full-corner Morita K-map therefore realizes every class, including relative classes, by differences of projections in finite matrix algebras over \(\mathcal K_B(X)\). The diagonal calculation proves (3.3) on all of K₀. \(\square\)

**Proposition 3.2 (numerical comparison).** The isomorphism

\[
\begin{gathered}
\Psi=\mu\Phi_\sigma^1:K_1(M_{\alpha^{-1}})\longrightarrow K_0(B)
\end{gathered}
\tag{3.7}
\]

satisfies \(\widehat\tau_*\Psi[w]=\Gamma_\tau(w)\).

*Proof.* Every K-class has a unitary representative smooth for \(\sigma\), by orbit convolution and matrix functional calculus, as in [Lesson 15, Theorem 4.1](KT-OPK-15.md#4-smooth-actions-and-regular-spectral-triples). Such a representative is a smooth twisted path in \(r\). Insert \(\delta w=-w'\) into (3.1), then use (3.2) and (3.3):

\[
\begin{gathered}
\widehat\tau_*\Psi[w]\\
=\frac1{2\pi i}\int_0^1\tau_n(w'(r)w(r)^*)\,dr\\
=\Gamma_\tau(w).
\end{gathered}
\tag{3.8}
\]

The two minus signs cancel: one is in the index-normalized degree-one Thom formula, and one in left translation's generator. Both sides are K-homomorphisms, the right side by Lesson 14, Theorem 4.1. Thus the identity holds for every class. Invertibility of the Thom and Morita maps proves the asserted isomorphism. \(\square\)

## 4. Pimsner's exact sequence of trace ranges

**Theorem 4.1.** Set \(G=\widehat\tau_*(K_0(B))\). Then

\[
\begin{gathered}
0\longrightarrow H\longrightarrow G\\
\xrightarrow{\pi}R_\tau^\alpha(F)\longrightarrow0
\end{gathered}
\tag{4.1}
\]

is exact. The first map is inclusion and \(\pi(g)=g+H\).

*Proof.* The actual inclusion \(\iota\) preserves the trace, so \(H\subset G\). Proposition 3.2 identifies

\[
G=\Gamma_\tau(K_1(M_{\alpha^{-1}})).
\tag{4.2}
\]

For \(q:M_{\alpha^{-1}}\to A\), evaluation at zero, the exact sequence of [Lesson 17, Corollary 3.1](KT-OPK-17.md#3-kernels-cokernels-and-the-splitting-question) says \(q_*\) maps onto \(\ker(1-\alpha_*^{-1})=F\), and its kernel is the image of the suspended ideal. Lesson 14, equation (4.2), gives \(\Gamma_\tau j_*\beta_A=\tau_*\).

Let \(w\) be a unitary representative in this mapping torus and \(v=w(0)\). The path \(w(r)v^*\) starts at 1 and ends at \(\alpha^{-1}(v)v^*\). Its integral is \(\Gamma_\tau(w)\), since \(v\) is constant in \(r\). Apply \(\alpha\) to this endpoint and use determinant invariance from Lemma 2.1. We obtain

\[
\begin{gathered}
\Gamma_\tau(w)+H
=\Delta_\tau(\alpha^{-1}(v)v^*)\\
=\Delta_\tau(v\alpha(v^*))=R_\tau^\alpha(q_*[w]).
\end{gathered}
\tag{4.3}
\]

This proves that \(\pi(G)\subset R_\tau^\alpha(F)\). Conversely, every \(x\in F\) lifts to \([w]\) by the mapping-torus exact sequence, so (4.3) puts its rotation determinant in \(\pi(G)\). Thus \(\pi\) is onto the stated target. Its kernel is exactly \(H\), by definition of the quotient. Inclusion is injective, completing the proof. \(\square\)

Equivalently, as a subgroup of \(\mathbb R\),

\[
G=\{r\in\mathbb R:r+H\in R_\tau^\alpha(F)\}.
\tag{4.4}
\]

Indeed both sides contain \(H\) and have the same image modulo \(H\). This is Blackadar's Theorem 10.10.4. The proof has supplied the trace comparison behind the source's instruction to apply the extension determinant sequence. It does not identify an abstract transported functional with the dual trace merely because both extend \(\tau_*\).

### Signed traces and the integral obstruction

Exel's source allows a normalized bounded hermitian trace rather than requiring positivity. A functional \(\tau\) is **hermitian** when \(\tau(a^*)=\overline{\tau(a)}\). This extension of the numerical range argument can be made without changing its Green–Thom map.

**Lemma 4.2 (the same range theorem for hermitian traces).** Replace the standing tracial state by a bounded hermitian trace satisfying \(\tau(1)=1\) and \(\tau\alpha=\tau\). Then \(\widehat\tau=\tau E\) is a normalized bounded hermitian trace. Define \(H\), \(F\), \(G\) and \(R_\tau^\alpha\) as before. Lemma 2.1, Theorem 2.2 and the exact range sequence (4.1) remain valid; Theorem 2.3 and Lemma 2.4 remain valid when \(H\subseteq\mathbb Z\). Every bounded hermitian trace on \(B\) restricting to \(\tau\) has the same K₀-pairing as \(\widehat\tau\).

*Proof.* The monomial calculation (1.2), boundedness, and \(\tau(a^*)=\overline{\tau(a)}\) show that \(\tau E\) is a hermitian trace; normalization is immediate. Likewise \(\tau_n(p)\) is real on every projection \(p\), so \(H\subseteq\mathbb R\). For a differentiable unitary path, \(w'w^*\) is antihermitian, so \(\tau_n(w'w^*)/(2\pi i)\) is real. Lesson 14's bounded-trace period theorem therefore gives the determinant into the actual quotient \(\mathbb R/H\). All of Lemma 2.1 and Theorem 2.2 uses only boundedness, traciality and invariance. The all-components extension in Lesson 14, Theorem 2.10, already has precisely this hermitian scope, so the algebraic proofs of Theorem 2.3 and Lemma 2.4 also apply.

Here is the numerical comparison that requires an extra step. The full norm-additive decomposition argument in Lesson 14, within the proof of Theorem 2.6, gives

\[
\begin{gathered}
\tau=\tau_+-\tau_-,\\
\|\tau\|=\|\tau_+\|+\|\tau_-\|.
\end{gathered}
\tag{4.5}
\]

with uniquely determined bounded positive traces. That decomposition and its uniqueness hold for every unital C*-algebra; separability is used later in that theorem for trace detection, and is unnecessary here. Composing the two positive parts with \(\alpha\) gives another norm-additive decomposition of \(\tau\): an automorphism preserves positivity and the functional norm, and \(\tau\alpha=\tau\). Uniqueness yields \(\tau_\pm\alpha=\tau_\pm\).

For each nonzero positive part put \(c_\pm=\tau_\pm(1)>0\) and \(\sigma_\pm=\tau_\pm/c_\pm\). A positive functional of zero value at one is zero, by Cauchy–Schwarz, so zero parts are simply omitted. The nonzero \(\sigma_\pm\) are invariant tracial states. Proposition 3.2 applies to each of them using the same isomorphism \(\Psi=\mu\Phi_\sigma^1\); its Green module, translation action and index convention depend on \(A,\alpha\), not on the chosen trace. Linear combination gives, for every mapping-torus class \([w]\),

\[
\begin{gathered}
\widehat\tau_*\Psi[w]\\
=c_+\widehat{\sigma_+}_*\Psi[w]
-c_-\widehat{\sigma_-}_*\Psi[w]\\
=\Gamma_\tau(w).
\end{gathered}
\tag{4.6}
\]

The same linear combination proves that the mapping-torus integral is a K-homomorphism for \(\tau\). Its value on positive Bott loops is \(\tau_*\), either directly or by combining the two positive formulas. Invertibility of \(\Psi\) gives (4.2) with this signed trace. Evaluation onto \(F\), the endpoint computation (4.3) and inclusion of \(H\) use no positivity. They consequently give the entire exact sequence (4.1) and the subgroup formula (4.4).

Finally the proof of Theorem 1.2 works word for word for bounded trace functionals: the K-pairing is constant on a projection path and boundedness moves the functional through the gauge integral. Neither that calculation nor its conclusion needs positivity. \(\square\)

Positivity-based conclusions about faithfulness, projectionlessness and invariant probability measures in §§5–6 retain their stated tracial-state hypotheses.

**Theorem 4.3 (Exel's integral crossed-product criterion).** Under either the standing tracial-state hypotheses or the hermitian hypotheses of Lemma 4.2, assume \(H\subseteq\mathbb Z\), equivalently \(H=\mathbb Z\). The following conditions are equivalent:

1. The rotation \(R_\tau^\alpha\) vanishes on \(F=\ker(1-\alpha_*)\).
2. \(\widehat\tau_*(K_0(A\rtimes_\alpha\mathbb Z))\subseteq\mathbb Z\).
3. There is an \(\alpha\)-invariant determinant \(D:U_\infty(A)\to\mathbb T\) satisfying (2.5).
4. The class of Theorem 2.3 vanishes for the cyclic action of \(\langle\alpha\rangle\).

*Proof.* The exact sequence (4.1) identifies \(G/H\) with the image of the rotation map. Since \(H=\mathbb Z\subseteq G\), condition 1 says exactly that \(G=\mathbb Z\), which is condition 2.

Under condition 2, apply Lesson 14, Theorem 2.10, to the unital crossed product \(B\) and its normalized hermitian trace \(\widehat\tau\). It gives a determinant \(D_B\) on every stable unitary of \(B\). Restrict it to \(A\). For \(v\in U_n(A)\), covariance and multiplicativity in the abelian circle yield

\[
\begin{gathered}
D_B(\alpha_n(v))\\
=D_B((u\otimes1_n)v(u\otimes1_n)^*)\\
=D_B(v).
\end{gathered}
\tag{4.7}
\]

The restriction has normalization (2.5) because \(\widehat\tau|_A=\tau\), proving condition 3. Conversely an invariant determinant satisfies \(D(\alpha(v^*)v)=1\) on every fixed K-class. Lemma 2.4 then gives \(\exp(2\pi iR_\tau^\alpha(x))=1\). With \(H=\mathbb Z\), the exponential identifies \(\mathbb R/H\) with \(\mathbb T\), so that rotation coset is zero. This proves condition 1. Finally, invariance under \(\alpha\) gives invariance under every positive and negative power, and Theorem 2.3 gives equivalence with condition 4. \(\square\)

This is the integral criterion of Exel, Theorem V.13, printed p. 63. It also identifies exactly when an all-components determinant can be chosen compatibly with the action.

**Example 4.4 (a signed integral range).** Put \(A=C(S^1)\oplus C(S^1)\), let \(\alpha\) act by the half-turn pullback on the first component and by identity on the second, and set

\[
\tau(f,g)=2\int_{S^1}f\,d\nu-\int_{S^1}g\,d\nu,
\tag{4.8}
\]

where \(\nu\) is Haar probability measure. This is a normalized invariant bounded hermitian trace, and \(\tau(0,1)=-1\), so it is not positive. Coefficient projection traces are integers; the two central unit projections have traces 2 and \(-1\). Thus \(H=\mathbb Z\).

The crossed product splits into the crossed products of the two components: the invariant complementary central unit projections split every covariant representation, and the two component universal representations give the reverse homomorphism. The gauge expectations split in the same way. Apply Exercise 19.5 separately to the half-turn and the identity action. The two normalized dual trace ranges are \(\tfrac12\mathbb Z\) and \(\mathbb Z\). K₀ of a direct sum and its trace pairing split componentwise, hence the range for (4.8) is

\[
2\bigl(\tfrac12\mathbb Z\bigr)-\mathbb Z=\mathbb Z.
\tag{4.9}
\]

Theorem 4.3 supplies an invariant determinant for this signed trace. The normalized positive trace on the first component has the nonintegral half-integer crossed-product range. Scaling and taking a difference can therefore change the integrality obstruction; the signed theorem carries additional information.

There is a sign distinction in comparing the source's mapping-torus formula to §3. Exel, Theorem V.11, uses \(M_\alpha\) and writes \((2\pi i)^{-1}\int\tau(w'^*w)=-\Gamma_\tau(w)\). Here we use \(M_{\alpha^{-1}}\) and \(+\Gamma_\tau\). Reversal \(w(t)\mapsto w(1-t)\) changes the twist and negates the integral, so these numerical conventions agree under reversal. This numerical comparison does not identify the source's Paschke map with the particular PV boundary normalized in Lesson 18; that stronger map identity is not needed in Theorem 4.3.

## 5. Scalar determinants suffice for commutative coefficients

Let \(A=C(X)\), where \(X\) is a nonempty compact Hausdorff space, let \(\varphi:X\to X\) be a homeomorphism, and use \(\alpha(f)=f\circ\varphi^{-1}\). An invariant probability measure \(\nu\) defines \(\tau(f)=\int_X f\,d\nu\). Write \(\mathcal H^1(X)=C(X,S^1)/\exp(2\pi i C(X,\mathbb R))\), with multiplication of scalar functions giving its abelian group law. We prove the cohomological identification at the full compact Hausdorff generality used here.

### Circle maps and their cohomology classes

For a finite open cover \((U_i)\), use the nerve description of Čech cohomology. An integer one-cocycle assigns a constant integer \(n_{ij}\) whenever \(U_i\cap U_j\ne\varnothing\), with \(n_{ji}=-n_{ij}\) and \(n_{ij}+n_{jk}=n_{ik}\) whenever the triple intersection is nonempty. A coboundary has form \(n_{ij}=k_i-k_j\). Passing to refinements and then the direct limit defines \(\check H^1(X;\mathbb Z)\). Finite covers suffice by compactness.

We will use a finite partition of unity \((\rho_i)\) with \(\operatorname{supp}\rho_i\subset U_i\). Here are the needed topological details. A compact Hausdorff space is normal: separate each pair of points from two disjoint closed sets by disjoint neighborhoods, first take a finite cover of the second compact set and then a finite cover of the first. Finite intersections and unions give disjoint neighborhoods of the two whole sets. Normality consequently shrinks a neighborhood of a closed set so that its closure remains inside the original neighborhood. Shrinking neighborhoods of points in a finite cover, and taking a finite subcover, gives closed sets \(F_i\subset U_i\) that cover \(X\). Choose open \(V_i\) with \(F_i\subset V_i\) and \(\overline{V_i}\subset U_i\).

For completeness, normality gives a continuous function \(h_i:X\to[0,1]\) that is one on \(F_i\) and zero outside \(V_i\). To construct it, choose open sets \(G_r\), indexed by dyadic \(r\in[0,1]\), with \(F_i\subset G_0\), \(G_1=V_i\), and \(\overline{G_r}\subset G_s\) for \(r<s\). Insert each intermediate set between a closed set and an open neighborhood by the preceding shrinking property. Put \(a(x)=\inf\{r:x\in G_r\}\), taking the infimum of the empty set as one, and set \(h_i=1-a\). For \(0<t<1\), the sets \(\{a<t\}=\bigcup_{r<t}G_r\) and \(\{a>t\}=\bigcup_{r>t}(X\setminus\overline{G_r})\) are open; the endpoint cases follow from the same formulas. Thus \(a\) is continuous, with the required values. Since \(\operatorname{supp}h_i\subset\overline{V_i}\subset U_i\), the functions \(\rho_i=h_i/\sum_jh_j\) have the stated supports and sum to one. The denominator is positive because the \(F_i\) cover \(X\).

**Lemma (circle maps and Čech cohomology).** There is an isomorphism

\[
\begin{gathered}
\mathcal H^1(X)\cong\check H^1(X;\mathbb Z).
\end{gathered}
\]

Moreover two scalar unitaries are homotopic precisely when their quotient has a continuous real logarithm.

*Proof.* For \(u:X\to S^1\), choose a finite cover \((U_i)\) with local real logarithms \(a_i\), so \(u|_{U_i}=e^{2\pi ia_i}\), and with each \(a_i(U_i)\) contained in an interval of length less than \(1/4\). Such covers exist by taking short arcs around \(u(x)\) and then a finite subcover. On an overlap, \(n_{ij}=a_i-a_j\) is integer-valued. Its possible values lie in an interval of length less than \(1/2\), so it is a single constant integer even if the overlap is disconnected. These integers satisfy the cocycle rule. Different short-log covers have a common refinement by intersections; the two local logarithms differ there by a constant integer, so their cocycles differ by a coboundary. This defines an unambiguous class of \(u\).

Products add this class: add the local logarithms on a common refinement, shortening the cover if needed, and their transition integers add. If \(u=e^{2\pi ia}\) for a global continuous real \(a\), each \(a_i-a\) is locally constant and integer-valued. Refine the cover by neighborhoods on which it is constant, then take a finite subcover. The cocycle is a coboundary there. Conversely, if the class vanishes, some refinement has \(n_{ij}=k_i-k_j\). Restrict the original logarithms to that refinement. The functions \(a_i-k_i\) then agree on overlaps and glue to a global continuous real logarithm. Thus the kernel is precisely \(\exp(2\pi i C(X,\mathbb R))\).

To prove surjectivity, start with a cocycle on a finite cover and the partition \((\rho_k)\) just constructed. For \(x\in U_i\), put

\[
b_i(x)=\sum_k\rho_k(x)n_{ik}.
\]

Each term is interpreted as zero outside \(U_k\). It is continuous on \(U_i\): at a point outside \(U_k\), a neighborhood misses the closed support of \(\rho_k\). On \(U_i\cap U_j\), every nonzero term has a nonempty triple intersection, so the cocycle rule gives \(b_i-b_j=\sum_k\rho_k n_{ij}=n_{ij}\). The circle functions \(e^{2\pi ib_i}\) therefore glue to a global \(u\). Refine by neighborhoods inside \(U_i\) where \(b_i\) ranges over an interval shorter than \(1/4\), and take a finite subcover. These are admissible short logarithms for \(u\), and their transition cocycle is exactly the pullback of \((n_{ij})\). Hence \(u\) represents the desired class. This proves the isomorphism.

Finally a continuous real logarithm of \(u_1u_0^*\) gives the homotopy \(u_s=u_0e^{2\pi isa}\). Conversely, a norm-continuous homotopy has a finite time subdivision for which \(\|u_{s_{j+1}}u_{s_j}^*-1\|<2\). Each quotient avoids \(-1\), so the ordinary continuous logarithm on \(S^1\setminus\{-1\}\) supplies a real function \(c_j\). Multiplying the quotients gives \(u_1u_0^*=\exp(2\pi i\sum_jc_j)\). A jointly continuous homotopy on \(X\times[0,1]\) is norm continuous: compactness gives a finite neighborhood cover of each time slice and a uniform estimate. Thus the same argument proves the topological homotopy criterion. \(\square\)

The argument uses the open-cover group directly for arbitrary compact Hausdorff spaces; no singular-cohomology replacement is needed for the range theorem.

**Theorem 5.1 (commutative range formula).** In this case

\[
H=\left\{\int_X h\,d\nu:h\in C(X,\mathbb Z)\right\},
\tag{5.1}
\]

and \(G/H\) is the image under (2.1) of the \(\alpha\)-fixed components in \(\mathcal H^1(X)\). Thus scalar unitaries alone determine the additional range.

*Proof.* A matrix projection has a continuous integer-valued rank, and its trace pairing is the integral of that rank, by Lesson 13. Conversely every continuous integer-valued \(h\) has finite image and clopen level sets. The positive and negative parts are rank functions of diagonal projections formed from those clopen characteristic functions. Their difference realizes \(\int h\), proving (5.1).

For a unitary matrix path \(\xi(t,x)\), differentiation of its ordinary determinant gives pointwise

\[
\operatorname{Tr}(\xi'\xi^{-1})
=(\det\xi)'(\det\xi)^{-1}.
\tag{5.2}
\]

The path is piecewise norm smooth; integration against the probability measure and in \(t\) is legitimate for its bounded continuous derivatives. Therefore \(\Gamma_\tau(\xi)=\Gamma_\tau(\det\xi)\), and hence \(\Delta_\tau=\Delta_\tau\circ\det\) on the identity component, with the same period group (5.1).

If \([v]\in F\), a stabilized homotopy from \(v\) to \(\alpha(v)\) gives a scalar homotopy from \(\det v\) to \(\alpha(\det v)\). Thus \(\det v\) has a fixed component in \(\mathcal H^1(X)\). Also \(\det(v\alpha(v^*))=(\det v)\alpha((\det v)^*)\), so its relative determinant is exactly that of this scalar representative. Conversely, if a scalar unitary \(z\) has fixed component, the scalar homotopy from \(z\) to \(\alpha(z)\) is itself a stable unitary homotopy. It follows that \([z]\in F\). Both inclusions in the asserted determinant image follow, and Theorem 4.1 proves the range formula. \(\square\)

Scalar homotopy components are indeed the displayed logarithm quotient. A global logarithm supplies an exponential homotopy. Conversely subdivide a homotopy from 1 finely enough that each successive multiplicative increment is uniformly within distance less than one of 1. Each increment has a continuous real logarithm; in the commutative algebra their sum is a global logarithm of the endpoint.

**Corollary 5.2.** If \(\mathcal H^1(X)=0\), then \(G=H\). If \(X\) is also connected, then \(G=\mathbb Z\).

*Proof.* Every scalar unitary is \(z=\exp(2\pi i h)\), \(h\) real. Its relative product is \(\exp(2\pi i(h-\alpha(h)))\). The determinant is \(\tau(h-\alpha(h))+H=0\), by invariance. Thus Theorem 5.1 gives no additional cosets, so \(G=H\). On a connected space every continuous integer-valued rank function is constant, and all integer ranks and their differences occur. Hence (5.1) gives \(H=\mathbb Z\). \(\square\)

## 6. Minimal systems and the absence of nontrivial projections

**Lemma 6.1.** If \(X\) is infinite compact Hausdorff and \(\varphi\) is minimal, then \(C(X)\rtimes_\alpha\mathbb Z\) is simple.

*Proof.* There are no periodic points: a finite orbit would be a proper closed invariant subset of an infinite minimal space. We first prove the ideal-intersection property. Suppose a quotient map \(Q:B\to B/I\) is injective on \(C(X)\). Fix \(a\in B_+\), choose a Laurent polynomial \(c=\sum_{|n|\leq N}f_nu^n\) with \(\|a-c\|<\varepsilon\), and choose \(x_0\) where \(E(a)\) attains its maximum. The finitely many points \(\varphi^n(x_0)\), \(|n|\leq N\), are distinct. Hausdorff separation and continuity give a neighborhood \(U\) of \(x_0\) with \(U\cap\varphi^n(U)=\varnothing\) for \(0<|n|\leq N\). Choose \(h\in C(X)\), \(0\leq h\leq1\), \(h(x_0)=1\), supported in \(U\), using normality of compact Hausdorff spaces.

Covariance implies \(hch=hE(c)h\). The two approximation errors are at most \(\varepsilon\) each, so

\[
\|hah-hE(a)h\|<2\varepsilon.
\tag{6.1}
\]

Since \(Q\) is isometric on coefficients and \(\|hE(a)h\|=\|E(a)\|\), it follows that \(\|Q(a)\|\geq\|E(a)\|-2\varepsilon\). Letting \(\varepsilon\to0\) shows that if \(Q(a)=0\), then \(E(a)=0\), hence \(a=0\). Therefore \(I=0\). Any nonzero ideal consequently intersects \(C(X)\) nontrivially.

That intersection is an invariant coefficient ideal, because conjugation by \(u\) preserves it. Its corresponding open subset of \(X\) is nonempty and invariant. Minimality makes it all of \(X\), so the intersection contains 1 and \(I=B\). Thus \(B\) is simple. \(\square\)

**Theorem 6.2 (corrected projection corollary).** Suppose \(X\) is infinite, connected and compact Hausdorff, \(\varphi\) is minimal, and \(\mathcal H^1(X)=0\). Then \(B\) is simple and unital and its only projections are 0 and 1.

*Proof.* An invariant probability measure exists. Starting with a point mass, average its first \(N\) translates. The difference between such an average and its translate has norm at most \(2/N\). Weak-star compactness of the probability measures gives a cluster subnet, whose limit is invariant. Its support is nonempty, closed and invariant, hence is all of \(X\) by minimality. The coefficient trace is faithful: a nonzero positive function is positive on an open set of positive measure. Proposition 1.1 makes its dual trace faithful as well.

Lemma 6.1 proves simplicity. Corollary 5.2 gives trace range \(\mathbb Z\). If \(p\) is a projection other than 0 and 1, faithfulness on both \(p\) and \(1-p\) gives \(0<\widehat\tau(p)<1\), contradicting that integer range. Thus no such projection exists. \(\square\)

This corrects two points in Blackadar, Corollary 10.10.6. The infinite-space hypothesis is needed for simplicity: on the one-point minimal system the algebra is \(C(S^1)\), which is not simple. Also the unit is not a *minimal projection* in the standard sense \(pBp=\mathbb Cp\); here \(1B1=B\) is infinite dimensional. The proved conclusion concerns projections inside \(B\), and does not assert that matrix algebras over it have no projections.

The existence example follows from the full Fathi–Herman construction in Theorem 6.5 below, credited to [their original paper (1977), §3.4, Theorem 1 and §3.9(c)](https://www.numdam.org/item/AST_1977__49__37_0/). In particular \(S^3\subset\mathbb C^2\) has the free circle action \(z\mapsto e^{2\pi it}z\), so their existence theorem applies. Its scalar circle group vanishes directly: [Lesson 6's sphere-contraction lemma](KT-OPK-06.md#sphere-maps-and-unitary-transport) contracts every loop in \(S^3\). For a circle map on \(S^3\), lift its value along a path from a fixed basepoint, using the local-argument construction of [Lesson 2, Lemma 5.2](KT-OPK-02.md). Two paths differ by a contractible loop, whose image has winding zero, so their lifted endpoints agree. In a small coordinate ball where the circle map takes values in an arc, this lift differs from the continuous local argument by a constant integer; it is therefore continuous. This gives a global logarithm and proves \(\mathcal H^1(S^3)=0\). Theorem 6.2 consequently gives a simple unital crossed product with only the two trivial projections. Theorem 6.5 supplies the dynamical existence construction in every odd dimension and in its full locally free circle-action scope.

### The dynamical existence proof

We now supply the construction used in the odd-sphere example. The theorem is due to Fathi and Herman; its conjugation and category method follows Anosov and Katok. The proof below includes the transversal and ambient-motion steps, the finite-cover lifting, and the category argument.

**Lemma 6.3 (a finite transverse family).** Let a nonvanishing smooth vector field on a compact manifold of dimension \(d\ge2\) have its orbit foliation. There are finitely many pairwise disjoint embedded closed \((d-1)\)-disks, each with a transverse extension to a slightly larger disk, whose interiors meet every orbit.

*Proof.* Flow boxes exist directly from the inverse function theorem: choose a small disk transverse to the field at a point and map \((s,y)\) to the time-\(s\) flow of its points. The derivative is invertible at the center, so this is a coordinate chart after shrinking. Choose finitely many such charts containing closed boxes
\([-1,1]\times\overline D^{d-1}(1)\), with slightly larger flow boxes around them, so that the interiors of their smaller concentric boxes cover the manifold. The flow lines in a box are the vertical segments.

Construct the disks successively through these boxes. Start with a transverse slice in the first box covering its smaller transverse disk. Suppose a finite disjoint transverse family has already been constructed, and consider the next closed box. Let \(L\) be the intersection of the existing disks with this box, in its coordinates. It is compact. For each transverse coordinate \(y\), the fiber
\(L_y=\{s:(s,y)\in L\}\) is finite. Indeed transversality makes each intersection with a vertical segment isolated, including near a disk boundary because the disk has a transverse extension. An infinite fiber in this compact set would have an accumulation point, contradicting that isolation.

Choose a small open neighborhood \(O_y\) of this finite set in the vertical interval, leaving infinitely many points of \((-1,1)\) outside it. There is a neighborhood \(V_y\) of \(y\) such that \(L_{y'}\subset O_y\) for \(y'\in V_y\). Otherwise a sequence of points in the compact set \(L\), with transverse coordinates tending to \(y\) and vertical coordinates outside \(O_y\), would have a limit in \(L_y\setminus O_y\). This proves the needed upper semicontinuity without any regularity assumption on the boundary of the box.

Cover the smaller closed transverse disk by finitely many closed round disks \(B_i\), whose interiors cover it and which have slightly larger disks inside their respective \(V_y\)'s and the original transverse chart. For each \(B_i\), choose a vertical coordinate \(s_i\in(-1,1)\setminus O_y\), avoiding the finitely many coordinates already chosen. The slices \(\{s_i\}\times B_i\) miss \(L\), have transverse extensions, and are pairwise disjoint even when their transverse disks overlap, because their vertical coordinates differ. They also miss all earlier disks. Every orbit passing through the smaller box meets the interior of one of these slices along its vertical segment. Repeat through all finitely many boxes. Their smaller interiors cover the manifold, proving the assertion. \(\square\)

**Lemma 6.4 (moving the transverse family).** If \(M\) is connected, compact and smooth of dimension at least two, and \(U\subset M\) is nonempty and open, a finite disjoint transverse family as in Lemma 6.3 can be carried into \(U\) by a smooth diffeomorphism isotopic to identity. Consequently, for a smooth locally free circle action on \(M\), such a diffeomorphism \(H\) can be chosen with \(H^{-1}(U)\) meeting every circle orbit.

*Proof.* Each extended transverse disk has a product neighborhood: the field flow maps a slightly larger disk times a sufficiently short time interval injectively onto a neighborhood of the original disk. To justify one common time interval, local flow-box injectivity covers the compact disk by finitely many neighborhoods; pairs of points outside a common such neighborhood stay uniformly separated at time zero, so remain separated for short times. The derivative stays invertible by compactness. Shrink these product neighborhoods to make their closures pairwise disjoint. They are coordinate neighborhoods containing the entire disks, and each contains its central point.

In one such coordinate neighborhood a compactly supported radial vector field, equal to \(-x\) on a closed ball containing the disk, has a flow which shrinks that disk arbitrarily close to its center. Choose the containing ball within the product chart after rescaling the disk and time coordinates. Its flow remains in this ball, so the stated formula applies throughout the shrinking. Extend the field by zero outside the chart. Applying these disjointly supported flows shrinks all disks to arbitrarily small neighborhoods of their respective centers.

There is an ambient smooth isotopy taking these finitely many centers to distinct points of \(U\). Here are the details needed for that assertion. Removing finitely many points from a connected manifold of dimension at least two leaves it path connected: a piecewise smooth path can be altered in small coordinate balls around the forbidden points by arcs avoiding their centers, since a punctured ball in that dimension is path connected. Move the centers one at a time to distinct target points in \(U\), chosen outside the finite set of original centers. At each step choose a smooth path avoiding all other current centers. The motion along this path is the flow of a smooth time-dependent vector field with support avoiding those other centers. In coordinates around a short path segment, multiply the prescribed velocity by a bump function equal to one near the moving point; subdivide the compact time interval into finitely many such segments. This constructs the field and fixes every excluded center. Compactness gives a global flow and the reverse time-dependent flow gives its inverse. Composing these finitely many isotopies produces a diffeomorphism \(G\) carrying all centers into \(U\).

By continuity, each center has a small neighborhood which \(G\) carries into \(U\). First use the radial flows to put the original disks inside those neighborhoods, and then apply \(G\). The composite is isotopic to identity and carries every disk into \(U\). Their interiors originally meet all orbits, so its inverse image of \(U\) meets every orbit. \(\square\)

**Theorem 6.5 (Fathi–Herman existence theorem).** Every connected compact smooth manifold with a smooth locally free circle action admits a smooth minimal diffeomorphism isotopic to identity. In particular every odd sphere \(S^{2m+1}\), \(m\ge0\), admits one.

*Proof.* Write the action as \(R_t\), \(t\in\mathbb R/\mathbb Z\). Its generating vector field is nonvanishing because the stabilizers are discrete. There is a number \(\delta>0\) such that \(R_t(x)\ne x\) for all \(x\) and \(0<|t|<\delta\). To see uniformity, use the flow coordinates just constructed near each point: on a smaller neighborhood and for a common short time the vertical coordinate increases strictly with \(t\). Finitely many such smaller neighborhoods cover \(M\). Each stabilizer is a finite cyclic subgroup of the circle, hence its order is at most \(1/\delta\). Their union therefore is contained in the finite set of roots of unity of orders at most that bound.

It follows that rational rotations \(R_{p/q}\) whose generated subgroup acts freely are dense among all \(R_t\). For example take arbitrarily large prime denominators \(q\) exceeding every stabilizer order and relatively prime numerators \(p\); these fractions approximate any circle parameter. For such a subgroup \(G=\langle p/q\rangle\), the finite free quotient \(\pi:M\to M/G\) is a smooth covering. Small coordinate neighborhoods with disjoint translates give its charts; the quotient is compact and connected. The circle action descends, with nonvanishing generator, to a locally free circle action on this quotient.

Fix a nonempty open \(U\subset M\). Lemma 6.4 on \(M/G\) gives an isotopy \(\overline H_s\), starting at identity, for which \(\overline H_1^{-1}(\pi U)\) meets every quotient circle orbit. Lift this isotopy through the covering, starting at identity, to \(H_s\) on \(M\). Existence, uniqueness and smoothness follow by lifting each path in evenly covered neighborhoods and continuing through a finite time subdivision; lifting the inverse isotopy gives the inverse diffeomorphisms. For \(g\in G\), both \(H_sg\) and \(gH_s\) lift the same paths and agree at time zero, so they agree for every \(s\). In particular \(H=H_1\) commutes with \(R_{p/q}\). Its set \(H^{-1}(U)\) meets every original circle orbit: the quotient condition first puts \(H(x)\) in some translate \(gU\); replace \(x\) by \(g^{-1}x\) in that same circle orbit and use equivariance.

For irrational \(\alpha\), the positive powers of either \(R_\alpha\) or \(R_{-\alpha}\) are dense in each circle orbit, even when that orbit has a finite stabilizer. For completeness, the closure of the positive powers of an irrational circle element contains its inverse. Partition the circle into arbitrarily short arcs and apply the pigeonhole principle to finitely many successive powers; the quotient of two powers in the same arc is a positive power arbitrarily close to identity. Irrationality makes the resulting exponents unbounded as the required distance tends to zero, and the preceding powers therefore approach the inverse. The closure consequently contains the whole cyclic subgroup, whose closure is the circle by the elementary subgroup argument in Exercise 19.5. Quotienting by a finite stabilizer preserves density. Thus

\[
\bigcup_{k\ge0}(H R_\alpha H^{-1})^k(U)=M.
\tag{6.2}
\]

The sets on the left are open, and compactness supplies a finite subcover. As irrational \(\alpha\) tends to \(p/q\), the conjugate \(H R_\alpha H^{-1}\) tends in every derivative to \(R_{p/q}\), because \(H\) is fixed and commutes with that rational rotation. We have therefore approximated every freely acting rational rotation by conjugate rotations with a finite forward covering of \(U\).

We make the category step precise. Give \(\operatorname{Diff}^{\infty}(M)\) the topology of uniform convergence of every derivative of both a map and its inverse, in a finite system of charts, or after a fixed smooth embedding of \(M\) in Euclidean space. This topology has a complete metric: sum bounded versions of the successive derivative distances with weights \(2^{-r}\). A Cauchy sequence and its inverse converge in every derivative to smooth maps \(f,g\); uniform convergence in the identities \(f_ng_n=g_nf_n=1\) gives \(fg=gf=1\), so the limit is again a diffeomorphism. Derivative convergence follows in the finite charts from the usual complete spaces of smooth functions. Composition and inversion are continuous by the chain rule and compactness. Thus every closed subspace is a Baire space.

Let \(\mathcal C\) be the closure in this space of all conjugates \(hR_t h^{-1}\). For a nonempty open set \(U\), let \(\mathcal V_U\) consist of the maps \(f\in\mathcal C\) for which, for some \(N\ge0\),

\[
M=\bigcup_{k=0}^{N}f^k(U).
\tag{6.3}
\]

This is open. For any finite cover \(M=\bigcup_{k=0}^N f^k(U)\), shrink the cover to compact subsets \(K_k\subset f^k(U)\) still covering \(M\), using compactness and finitely many coordinate neighborhoods with closures inside the relevant open sets. For all sufficiently close \(g\), continuity of the finitely many inverse powers gives \(g^{-k}(K_k)\subset U\). Hence the covering property persists.

It is also dense in \(\mathcal C\). It is enough to approximate each \(hR_t h^{-1}\). Apply the preceding rational approximation to \(h^{-1}U\), then conjugate by \(h\). Freely acting rational parameters are dense, and at each such parameter the fixed commuting \(H\) gives the required approximations in \(\mathcal V_U\). This proves density for every \(t\), every conjugating diffeomorphism, and consequently their closure.

Choose a countable base \((U_i)\) of nonempty open sets. The Baire theorem gives
\(f\in\bigcap_i\mathcal V_{U_i}\). For every \(x\) and every \(U_i\), the finite covering property puts \(f^{-k}x\) in \(U_i\) for some \(k\ge0\). Every orbit is therefore dense, so \(f\) is minimal.

Finally the isotopy assertion also survives this construction. Each conjugate rotation is isotopic to identity through \(hR_{st}h^{-1}\), choosing a real lift of \(t\). The subgroup of diffeomorphisms isotopic to identity is open and closed: maps sufficiently close to identity in \(C^1\) are joined to it by their short exponential-coordinate interpolation, which remains a diffeomorphism throughout; translating this neighborhood gives open cosets and hence a closed identity subgroup. To justify that interpolation, its derivatives stay invertible for a sufficiently small \(C^1\) neighborhood; uniform local injectivity in finitely many charts and uniform closeness to identity exclude any pair of distinct preimages outside those charts. It is therefore a bijective local diffeomorphism at each interpolation time. Thus \(\mathcal C\) lies in the identity isotopy subgroup and the chosen \(f\) is isotopic to identity.

If \(\dim M=1\), a connected closed smooth manifold is a circle, and an irrational rotation proves the assertion directly. For \(S^{2m+1}\subset\mathbb C^{m+1}\), multiplication by \(e^{2\pi it}\) is a smooth free action: a nonzero coordinate forces every stabilizer element to be one. This verifies the hypotheses in every odd dimension. \(\square\)

The exact source comparison is Fathi–Herman, §4.1, Lemma 4.6, Proposition 4.8 and Corollaries 4.11–4.12, followed by §§5.4–5.6. Lemma 6.4 provides the ambient motion directly by compactly supported vector fields. The theorem is proved here in its full locally free circle-action scope; its application to the odd spheres is no longer an external existence input.

## 7. Five exercises with complete solutions

**Exercise 19.1.** Verify the dual trace, its restriction property and its faithfulness.

*Solution.* Gauge averaging is positive and preserves 1, and removes every nonzero Fourier coefficient. For \(au^m\) and \(bu^n\), the coefficient of their product at zero is zero if \(m+n\ne0\). Otherwise it is \(a\alpha^m(b)\). Applying invariance to this expression and cyclically moving the second factor gives \(\tau(b\alpha^{-m}(a))\), the zero coefficient of the reverse product. Linearity and norm density give a trace on all of \(B\). Any trace restriction satisfies \(\rho(\alpha(a))=\rho(uau^*)=\rho(a)\). If the coefficient trace is faithful, a zero dual trace on \(b^*b\) forces its nonnegative expectation to vanish, and faithfulness of the average forces \(b=0\). These prove each assertion without assuming simplicity.

**Exercise 19.2.** Prove representative independence of the rotation determinant and explain why higher matrix classes cause no difficulty in the commutative case.

*Solution.* A fixed stable class makes \(v\alpha(v^*)\) a zero stable class, so after finite stabilization a path from 1 exists. Its determinant is independent of that path modulo \(H\) by the complete period theorem of Lesson 14. If \(v_s\) joins representatives, the integral of \(v_s\alpha(v_s^*)\) is the difference of two equal integrals, because \(\tau\alpha=\tau\). Appending this relative path changes the determinant by zero. Block sums add the values, proving the K-homomorphism assertion. For commutative coefficients Jacobi's identity (5.2) makes the matrix determinant preserve the entire logarithmic integral. Taking determinants of a stable homotopy also preserves scalar component invariance. Conversely every invariant scalar component already gives a fixed stable class. Thus matrices contribute no determinant cosets beyond those of scalar unitaries, even when the full K₁-group contains additional classes.

**Exercise 19.3.** Prove the projection corollary and identify both corrections to its source formulation.

*Solution.* Vanishing Čech first cohomology makes each scalar unitary a global exponential. The relative determinant is then the trace of \(h-\alpha(h)\), hence zero. The range theorem reduces the crossed-product range to coefficient ranks, which are integers because \(X\) is connected. An invariant measure is obtained by weak-star limits of orbit averages. Minimality gives full support, and the dual trace is faithful. A proper nonzero projection would have trace strictly between 0 and 1, which an integer range excludes. For simplicity, the infinite minimal system has no periodic points, so the Fourier cutdown in Lemma 6.1 proves every nonzero ideal meets coefficients, and the invariant coefficient ideal must be the whole algebra. The one-point minimal system shows why infinitude cannot be omitted from that simplicity argument. Finally the assertion about projections does not make \(1\) minimal in the corner sense: \(1B1=B\), not \(\mathbb C\). It also leaves matrix projections available; for example \(\operatorname{diag}(1,0)\in M_2(B)\) is a nontrivial projection.

**Exercise 19.4.** Prove agreement of all trace extensions on K₀ and show that the extensions themselves can differ.

*Solution.* Gauge automorphisms are joined to identity by the gauge path. For any projection \(p\), its gauge translates have the same stable class. Thus every trace extension \(\rho\) gives them the same number \(\rho_n(p)\). Average these numbers. Boundedness of \(\rho_n\) moves it through the integral, giving \(\rho_n(E_n(p))\). This expectation lies in \(M_n(A)\), where \(\rho_n=\tau_n\), so the result is \(\widehat\tau_n(p)\). Differences give equality on all K₀. For \(A=\mathbb C\), \(\alpha=1\), evaluation at two distinct points of \(S^1\) gives two different trace states on \(C(S^1)\). Both restrict to the scalar state and both evaluate projection classes by rank. This proves the general agreement and the precise limitation on what it says about the traces.

**Exercise 19.5 (rotation range).** Let \(r_\theta(z)=e^{2\pi i\theta}z\), \(\alpha(f)=f\circ r_\theta^{-1}\), and let \(\tau\) be Haar trace on \(C(S^1)\). Compute the full dual trace range, with its sign convention explicit.

*Solution.* The coefficient range is \(H=\mathbb Z\). Scalar components are winding numbers, and rotation fixes them all. A representative of winding \(k\) is \(z^k\). Covariance and the chosen pullback give

\[
z^k\alpha(z^{-k})=e^{2\pi ik\theta}1.
\tag{7.1}
\]

The scalar exponential path has determinant \(k\theta+\mathbb Z\), as already computed in Lesson 14, Exercise 14.4. Thus the determinant image is \(\theta\mathbb Z\) modulo \(\mathbb Z\). Equation (4.4) now gives exactly \(G=\mathbb Z+\theta\mathbb Z\): every element of this subgroup occurs as the trace of a K-class, not necessarily as the trace of a projection in the unstabilized algebra. Reversing the geometric pullback convention negates the displayed determinant, but leaves the additive range subgroup unchanged. If \(\theta\) is irrational, Lemma 6.1 also proves simplicity. To see minimality, the closure of its cyclic subgroup is a closed subgroup of the circle. If a closed subgroup contains arbitrarily small positive angles, their successive multiples approximate every angle, so the subgroup is the whole circle. Otherwise its least positive angle generates a finite subgroup, which would force \(\theta\) rational. Thus the irrational subgroup is dense, and every orbit is its dense coset. This prepares the finer group and projection computations of Lesson 20.

## Sources and exact imports

- B. Blackadar, *K-Theory for Operator Algebras*, second edition (1998), complete §10.10, especially Theorem 10.10.4, Theorem 10.10.5 and Corollary 10.10.6, printed pp. 83–86. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Blackadar's introductory discussion on pp. 83–84 attributes the integer trace-range result to M. Pimsner; that is the historical attribution used in §4. The full trace-extension agreement, numerical Green–Thom comparison, determinant range sequence, commutative reduction and corrected projection corollary are proved above. The original free-group paper is not a proof prerequisite for these integer-action results.
- Green's module is imported with the exact KT-CP-07 formulas listed in §3. Its trace compatibility is proved in Lemma 3.1. The actual Morita K-map is proved in the programme Hilbert-module lesson, Theorem 2.4, Corollary 2.5 and Theorem 5.1, as specified in §3. [The checked published source](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html) contains the complete full-corner proof, including its directed-continuity passage. Rosenberg (2012), §1.2, pp. 97–98, supplies comparison and attribution.
- The numerical real-flow Thom identity and its semifinite integration framework are reused from *Frequency calculus for an action of Euclidean space*, §7, Theorem 7.6, with the signs and measures stated in §3. Theorem 7.7 there concerns real crossed products of smooth manifolds; the integer range theorem here requires the Green comparison just proved.
- Ordinary trace pairings, determinants and mapping-torus exactness are from Lessons 13, 14 and 17. Smooth representatives are from Lesson 15. The Fathi–Herman existence theorem is proved in Lemmas 6.3–6.4 and Theorem 6.5, retaining its original attribution and the Anosov–Katok conjugation method.

- Albert Fathi and Michael R. Herman, *Existence de difféomorphismes minimaux*, Astérisque 49 (1977), 37–59, §3.4 Theorem 1, §3.9(c), §4.1, §§4.6–4.12, §§5.1 and 5.4–5.6. [Original paper](https://www.numdam.org/item/AST_1977__49__37_0/). The complete required construction has been compared with this paper; the ambient motion in Lemma 6.4 is written directly with vector fields. The conjugation method retains the authors' credit to D. V. Anosov and A. B. Katok, *New examples in smooth ergodic theory. Ergodic diffeomorphisms*, Transactions of the Moscow Mathematical Society 23 (1970), 1–35.

- Ruy Exel, [*Rotation numbers for automorphisms of C*-algebras*](https://msp.org/pjm/1987/127-1/pjm-v127-n1-p03-s.pdf), Pacific Journal of Mathematics 127 (1987), 31–89, III.1–7 and IV.1–4, printed pp. 45–50, and V.3–13, printed pp. 53–63. In V.9–11 the source computes the dual trace of its mapping-torus classes explicitly; V.12–13 then treat the integral case. Theorems 2.2–2.3, Lemma 2.4 and Theorem 4.3 give complete independently written composition, cocycle, determinant-choice and integral crossed-product proofs. Lemma 4.2 retains normalized bounded hermitian traces using the full positive decomposition and the same trace-independent Green–Thom map. The circle-valued statements in V.12–13 assume the coefficient trace range is integral; the general quotient by the actual subgroup H is proved here in Theorem 4.1. Source III.3's character correction is fixed explicitly in (2.9); algebraic and closed commutator subgroups are kept distinct. Source V.11's sign/twist comparison is numerical only, as specified after Theorem 4.3, and does not identify its Paschke map with this programme's normalized PV boundary.

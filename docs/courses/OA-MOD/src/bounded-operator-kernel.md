# Bounded operators needed for comparing weights

We construct the bounded facts needed for weight comparisons: the bicommutant, order limits, supports, inverses and polar factors. The Hilbert spaces may have arbitrary dimension, and the convergence assertions allow arbitrary directed nets.

The free human source for the finite-vector commutant argument is Jacob Lurie's [*Math 261y, Lecture 5*, Theorem 4 and Proposition 5, pages 1–2](https://people.math.harvard.edu/~lurie/261ynotes/lecture5.pdf). Its topology definitions on pages 1 and 3 also motivate the coefficient tests below. The earlier written real Hilbert-space proof, first section, and bounded Bernstein-calculus proof GP0 provide the elementary constructions used here. Each further assertion is proved below; none is supplied by a citation alone.

## The bounded prerequisite boundary

Inner products are linear in the first variable. A Hilbert space is a complete complex inner-product space; scalar completeness and the inner-product axioms are entry assumptions. For a bounded self-adjoint operator \(a\), write \(a\geq0\) when \(\langle a\xi,\xi\rangle\geq0\) for all \(\xi\). All operators in this lesson have full Hilbert-space domains.

We first discharge the two bounded contracts used in later sections: Hilbert projection, representation and adjoints; and the full continuous calculus for a bounded self-adjoint element in a unital norm-closed *-algebra. The zero Hilbert space satisfies all ensuing operator statements trivially; statements about nonempty spectra below concern nonzero spaces.

**Hilbert representation and bounded operators.** The preceding real Hilbert proof constructs orthogonal projections by a minimizing sequence and the parallelogram identity, and proves the real Riesz representation theorem. Apply it to the real Hilbert space with inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\). For a complex closed subspace, testing orthogonality against \(\eta\) and \(i\eta\) makes its real projection the complex orthogonal projection. For a bounded complex-linear functional \(L\), represent \(\operatorname{Re}L(\xi)\) as \(\operatorname{Re}\langle\xi,v\rangle\). Evaluation at \(i\xi\) identifies the imaginary parts as well, so \(L(\xi)=\langle\xi,v\rangle\), with the same norm.

If a bounded form \(b(\xi,\eta)\) is linear in \(\xi\) and conjugate-linear in \(\eta\), apply this result to \(\eta\mapsto\overline{b(\xi,\eta)}\), at each fixed \(\xi\). Its representing vector \(T\xi\) satisfies
\(b(\xi,\eta)=\langle T\xi,\eta\rangle\) and \(\|T\xi\|\leq C\|\xi\|\). Uniqueness proves linearity and uniqueness of \(T\). The same argument applied to \(\langle T\xi,\eta\rangle\), for \(T:H\to K\), constructs \(T^*:K\to H\). Testing pairings proves the adjoint sum and product rules and \(\|T^*\|=\|T\|\). Also
\(\|T^*T\|=\|T\|^2\), by \(\|T\xi\|^2=\langle T^*T\xi,\xi\rangle\) and the reverse operator-norm inequality.

Bounded maps on a dense subspace extend uniquely by norm limits: the bound makes images of a Cauchy sequence Cauchy and makes the limit independent of the approximating sequence. If a pre-Hilbert space is initially given, its completion is constructed from Cauchy sequences modulo sequences tending to zero. Termwise addition and scalar multiplication descend; the inner product is the limit of the original pairings, which exists and is representative-independent by Cauchy–Schwarz. Constant sequences embed isometrically and densely. For a Cauchy sequence of classes, choose representatives within \(2^{-n}\) at the \(n\)-th step after taking a subsequence with successive class errors at most \(2^{-n}\); the chosen representative points are Cauchy and give its limit. The original Cauchy sequence converges to that limit as well. This proves completeness.

For later nets, sequential completeness also gives a limit for every Cauchy net: choose increasing indices whose subsequent pairwise errors are at most \(2^{-n}\). Their values form a Cauchy sequence with a limit, and the same tail estimates prove convergence of the original net to that limit. GP0 also proves completeness of \(B(H)\) in operator norm, by taking limits on each vector, and proves Cauchy–Schwarz for positive semidefinite forms. In particular, for bounded positive \(a\),
\(\|a\|=\sup_{\|\xi\|=1}\langle a\xi,\xi\rangle\), and

\[
\|d\xi\|^2\leq C\langle d\xi,\xi\rangle
\quad\hbox{if }0\leq d\leq CI.
\tag{BK.1}
\]

For \(C>0\), this follows from GP0 applied to \(d/C\); for \(C=0\), polarization gives \(d=0\).

**The interval calculus.** GP0 constructs the calculus for a positive contraction from Bernstein polynomials. Its polynomial norm bound, uniform approximation, positivity and commutation proofs are all given there. For self-adjoint \(T\), take \(C=\|T\|>0\) and apply that construction to \((T+CI)/(2C)\). We obtain a unital *-homomorphism
\(f\mapsto f(T)\) from \(C([-C,C])\), with
\(\|f(T)\|\leq\|f\|_\infty\), preservation of order, and polynomial approximation in operator norm. If \(C=0\), use \(f(T)=f(0)I\). Thus every resulting operator belongs to any unital norm-closed *-algebra containing \(T\), and commutes with every operator commuting with \(T\).

For completeness, we now pass from the containing interval to the actual spectrum, rather than assume its norm and inverse properties. Define \(\sigma(T)\) as the complex numbers \(\lambda\) for which \(T-\lambda I\) has no bounded two-sided inverse on \(H\). Norm completeness and the geometric series prove that the resolvent set is open: perturb an invertible operator by an error smaller than the reciprocal inverse norm. The same series excludes \(|\lambda|>C\). For \(\operatorname{Im}\lambda\ne0\), the imaginary part of the quadratic pairing gives
\(\|(T-\lambda)\xi\|\geq|\operatorname{Im}\lambda|\|\xi\|\).
Its range is closed, and its orthogonal complement is
\(\ker(T-\overline\lambda)=0\); hence it is onto and has bounded inverse. Consequently \(\sigma(T)\) is a compact subset of \([-C,C]\).

It is nonempty. Set \(B=T+CI\geq0\) and \(m=\|B\|\). If \(m=0\), \(T=-CI\), whose spectrum is \(\{-C\}\). Otherwise take unit \(\xi_n\) with \(\langle B\xi_n,\xi_n\rangle\to m\). The inequality \(B^2\leq mB\), proved in GP0, gives
\(\|(B-mI)\xi_n\|^2\leq m(m-\langle B\xi_n,\xi_n\rangle)\to0\).
A bounded inverse is therefore impossible, so \(m-C\in\sigma(T)\).
More generally, each real \(\lambda\in\sigma(T)\) has unit approximate eigenvectors. Otherwise \(T-\lambda\) is bounded below, hence injective with closed range; the range-kernel identity for its self-adjoint adjoint makes that range dense, so it would have a bounded inverse.

**Restriction to the spectrum.** If \(h\in C([-C,C])\) vanishes on \(\sigma(T)\), then \(h(T)=0\). First suppose its support is a compact subset of the complement of the spectrum. Around each point \(\lambda\) of that support choose an interval of radius \(\delta\) with
\(\delta\|(T-\lambda)^{-1}\|<1\).
A finite such cover splits \(h\) into finitely many continuous functions \(h_j\) supported in those intervals. Explicitly, choose slightly smaller intervals still covering the support, use their distance-to-complement functions, divide by their positive sum on the support, and multiply by \(h\), extending by zero elsewhere. The extension is continuous because the compact support lies inside the set where the denominator is positive.

For the center \(\lambda_j\) and radius \(\delta_j\), multiplicativity and the interval norm bound give

\[
\begin{aligned}
\|h_j(T)\|
&\leq\|(T-\lambda_j)^{-1}\|^n
       \|[(t-\lambda_j)^nh_j(t)](T)\|\\
&\leq\bigl(\delta_j\|(T-\lambda_j)^{-1}\|\bigr)^n
       \|h_j\|_\infty .
\end{aligned}
\]

Let \(n\to\infty\); each \(h_j(T)\) is zero. For a general \(h\) vanishing on the spectrum, multiply it by continuous distance cutoffs which vanish within distance \(1/n\) of the spectrum and equal one beyond distance \(2/n\). The products converge uniformly to \(h\), since \(h\) vanishes on that compact set. The preceding case and the norm bound prove \(h(T)=0\).

Every continuous complex \(f\) on \(\sigma(T)\) extends continuously to \([-C,C]\), with the same supremum norm: interpolate linearly across each complementary interval and keep the value constant beyond the extreme spectral points. To check continuity at the spectral set, small complementary intervals have both endpoints close, so uniform continuity of \(f\) controls their interpolates. For intervals longer than a fixed positive length there are only finitely many, and the interpolation is continuous at each endpoint. These two observations give continuity everywhere. Convexity of a closed complex disc gives the norm bound, and a real nonnegative \(f\) has a real nonnegative extension.

The vanishing result makes the value of \(f(T)\) independent of that extension. It yields a unital *-homomorphism on \(C(\sigma(T))\), positive and contractive. For \(\lambda\in\sigma(T)\), let \(\xi_n\) be its unit approximate eigenvectors. Factoring \(p(t)-p(\lambda)\) proves
\(\|(p(T)-p(\lambda))\xi_n\|\to0\) for polynomials. Uniform approximation on the containing interval proves the same assertion for continuous \(f\). Hence
\(\|f(T)\|\geq|f(\lambda)|\), and therefore

\[
\|f(T)\|=\max_{\lambda\in\sigma(T)}|f(\lambda)|.
\]

If \(\mu\notin f(\sigma(T))\), applying the calculus to \(1/(f-\mu)\) gives an inverse for \(f(T)-\mu I\). If \(\mu=f(\lambda)\), the approximate eigenvectors rule out such an inverse. Thus spectral mapping, including complex-valued \(f\), is proved. Inverses produced by the calculus belong to every unital norm-closed *-algebra containing \(T\).

**Positivity, square roots and lower bounds.** A bounded positive \(a\) has no negative spectral value: for \(\lambda<0\),
\(\|(a-\lambda)\xi\|\geq-\lambda\|\xi\|\), and the same closed-range and adjoint argument proves invertibility. Hence \(\sigma(a)\subset[0,\|a\|]\), and the calculus gives \(c=\sqrt a\geq0\), \(c^2=a\).
If another positive \(b\) satisfies \(b^2=a\), it commutes with \(a\), hence with \(c\) by polynomial approximation. Then \((b-c)(b+c)=0\). Positivity and (BK.1) show
\(\ker(b+c)=\ker b\cap\ker c=\ker a\).
The range of the self-adjoint \(b+c\) is dense in \((\ker a)^\perp\), so \(b-c\) vanishes there and also on \(\ker a\). Thus \(b=c\). This proves uniqueness without an unbounded spectral or polar theorem.

The identity \(\langle a\xi,\xi\rangle=\|a^{1/2}\xi\|^2\) gives
\(\ker a=\ker a^{1/2}\). If \(a\geq mI\), \(m>0\), applying the negative-value argument to \(a-mI\) gives \(\sigma(a)\subset[m,\|a\|]\); its continuous inverse and inverse square root are consequently available in the algebra. Finally, for any bounded map \(T:H\to K\),
\(\overline{\operatorname{ran}T}=(\ker T^*)^\perp\):
orthogonality to every \(T\xi\) is equivalent to \(T^*\eta=0\). This is the range-kernel identity used above and below.

![A function away from the spectrum vanishes in the calculus; the geometric curve is its proved upper bound.](../../audit/real-coercivity/figures/bounded-spectrum-restriction.svg)

**Figure.** In the displayed matrix example, \(\lambda=-1/2\), \(\delta=1/5\), and \(\|(T-\lambda I)^{-1}\|=2\). The function vanishes on \(\sigma(T)=\{0,1\}\), so its actual operator norm is zero. The right-hand curve shows the upper bounds \((2/5)^n\) from the arbitrary-dimensional argument above. The proof uses their decay to establish that vanishing result before passing to the norm on the spectrum. Reproducible figure source.

## Finite-vector approximation and the bicommutant

For \(S\subset B(H)\), let \(S'=\{r:rs=sr\ \text{for all }s\in S\}\).
Strong convergence means norm convergence on each fixed Hilbert vector; weak operator convergence means convergence of every matrix coefficient. Cauchy–Schwarz gives strong implies weak. Fixed left and right multiplication are continuous for both topologies: for strong convergence test
\(r(x_i-x)\xi\) and \((x_i-x)r\xi\); for weak convergence move \(r\) to \(r^*\eta\) in the first coefficient and to \(r\xi\) in the second. Thus a commutant is weakly closed. If \(S\) is *-closed, taking adjoints of its commutation equations also makes \(S'\) a unital *-algebra.

**Theorem.** Every unital *-subalgebra \(\mathcal B\subset B(H)\), whether or not norm closed, satisfies

\[
\overline{\mathcal B}^{\mathrm{SOT}}
=\overline{\mathcal B}^{\mathrm{WOT}}=\mathcal B''.
\tag{BK.2}
\]

Only the inclusion from right to left needs proof. Fix \(T\in\mathcal B''\), a finite list \(\xi_1,\ldots,\xi_n\), and an error \(\varepsilon>0\). On \(H^n\), let \(D(b)\) act diagonally and put

\[
\Xi=(\xi_1,\ldots,\xi_n),\qquad
L=\overline{\{D(b)\Xi:b\in\mathcal B\}}.
\]

This is a closed linear subspace invariant under \(D(\mathcal B)\) and their adjoints. Its orthogonal complement is also invariant, by the adjoint pairing; hence its orthogonal projection \(P\) commutes with every \(D(b)\). In block matrix entries this says \(P_{jk}\in\mathcal B'\).
Consequently \(D(T)P=PD(T)\). Unitality puts \(\Xi\) in \(L\), so
\(PD(T)\Xi=D(T)\Xi\). Membership of \(D(T)\Xi\) in \(L\) supplies one \(b\in\mathcal B\) with
\(\sum_j\|(b-T)\xi_j\|^2<\varepsilon^2\).
These simultaneous finite-vector conditions are exactly a neighborhood basis for the strong topology, proving \(T\) belongs to the strong closure. The other inclusions follow from weak closedness of \(\mathcal B''\).

Selecting approximants with finite sets increasing and error decreasing gives a directed net; this argument supplies no uniform norm bound and requires no countable cofinal set. We have explicitly used \(I\in\mathcal B\). Without it, the zero algebra on a nonzero space is already a counterexample to (BK.2).

A concrete von Neumann algebra is therefore equivalently a unital *-algebra \(M=M''\), a strongly closed unital *-algebra, or a weakly closed one. It is norm closed, and the calculus constructed in BK-01 stays inside it.

## The ultraweak convergence needed by finite cutoffs

The ultraweak topology is defined by the coefficient sums

\[
\omega_{\xi,\eta}(x)=\sum_{n=1}^{\infty}\langle x\xi_n,\eta_n\rangle,
\qquad
\sum_n\|\xi_n\|^2<\infty,\quad
\sum_n\|\eta_n\|^2<\infty .
\tag{BK.3}
\]

They converge absolutely by Cauchy–Schwarz, with norm bound
\(\|x\|(\sum\|\xi_n\|^2)^{1/2}(\sum\|\eta_n\|^2)^{1/2}\).
This definition permits nonseparable \(H\); the sequences belong to each individual test, not to a chosen basis.

If \(x_i\to x\) weakly and \(\sup_i\|x_i\|<\infty\), then \(x_i\to x\) ultraweakly. Indeed set \(D=\sup_i\|x_i\|+\|x\|\). The coefficient tail after \(N\), evaluated at \(x_i-x\), is bounded uniformly by

\[
D\left(\sum_{n>N}\|\xi_n\|^2\right)^{1/2}
 \left(\sum_{n>N}\|\eta_n\|^2\right)^{1/2}.
\]

Choose \(N\) for the tail, then a common directed tail for the finitely many leading coefficients. This proves convergence of the whole sum. Bounded strong convergence is a special case.

Fixed multiplication is ultraweakly continuous without a bound on the varying net: testing \(rx\) replaces \(\eta_n\) by \(r^*\eta_n\), while testing \(xr\) replaces \(\xi_n\) by \(r\xi_n\); both replacement sequences are square summable. Single-term sequences show that ultraweak convergence implies weak operator convergence. In particular a weakly closed \(M\) is ultraweakly closed. These arguments do not identify the topologies on unbounded sets or prove a general characterization of normal maps.

## Bounded increasing positive nets have strong suprema

Let \(a_i\in M_+\) be increasing on a nonempty directed set and \(a_i\leq CI\), \(C<\infty\). Then there is \(a\in M_+\) with

\[
\langle a\xi,\xi\rangle=\sup_i\langle a_i\xi,\xi\rangle,
\qquad a_i\longrightarrow a\quad\text{strongly and ultraweakly}.
\tag{BK.4}
\]

It is the least upper bound even in \(B(H)_{\rm sa}\).

Here is a construction avoiding a representation theorem for an unverified quadratic supremum. The case \(C=0\) is immediate. For \(C>0\), if \(j\geq i\), apply (BK.1) to \(a_j-a_i\):

\[
\|(a_j-a_i)\xi\|^2
 \leq C\bigl(\langle a_j\xi,\xi\rangle-\langle a_i\xi,\xi\rangle\bigr).
\]

The scalar increasing bounded net has a supremum. Given two sufficiently late indices, choose a common upper index and use the displayed estimate twice and the triangle inequality. This proves that \(a_i\xi\) is Cauchy for every \(\xi\). Completeness yields a limit \(a\xi\). Passing to limits proves linearity and \(\|a\|\leq C\); passing to adjoint pairings proves self-adjointness. Its diagonal is the stated supremum, so \(0\leq a\leq CI\) and \(a\geq a_i\). Any self-adjoint upper bound dominates this diagonal, hence dominates \(a\). Strong closedness gives \(a\in M\), and BK-03 gives ultraweak convergence.

If the original upper bound is \(b\in M_+\), use \(C=\|b\|\); leastness gives \(a\leq b\). Applying the result to \(CI-a_i\) proves the decreasing-net version. Also, for fixed \(x\in M\),

\[
a_i\uparrow a\quad\Longrightarrow\quad x^*a_ix\uparrow x^*ax.
\tag{BK.5}
\]

The congruences are positive and increasing, and fixed multiplication preserves their strong limit. The theorem then identifies that limit with their supremum. No commutation between \(x\) and the net is required.

## Inversion reverses order

If \(a,b\in M_+\) and \(mI\leq a\leq b\), \(m>0\), the calculus in BK-01 gives their inverses and inverse square roots in \(M\). We prove

\[
0\leq b^{-1}\leq a^{-1}.
\tag{BK.6}
\]

Let \(c=a^{-1/2}ba^{-1/2}\). Testing quadratic forms gives \(c\geq I\), so its one-operator calculus gives \(0\leq c^{-1}\leq I\). Direct multiplication verifies
\(b^{-1}=a^{-1/2}c^{-1}a^{-1/2}\).
Congruence of the last order inequality by \(a^{-1/2}\) proves the claim. The proof applies to noncommuting \(a,b\).

For \(0\leq a\leq b\) and \(\lambda>0\), add \(\lambda I\), apply (BK.6), and subtract the scaled inverses from \(I\):

\[
a(a+\lambda I)^{-1}
 =I-\lambda(a+\lambda I)^{-1}
 \leq I-\lambda(b+\lambda I)^{-1}
 =b(b+\lambda I)^{-1}.
\tag{BK.7}
\]

Injectivity alone supplies no positive lower bound; BK-09 gives an injective positive operator with unbounded inverse.

## Supports from bounded resolvent cutoffs

For \(a\in M_+\), let \(p\) project onto
\((\ker a)^\perp=\overline{aH}\). Then \(p\in M\), \(pa=ap=a\), and, as \(\varepsilon\downarrow0\),

\[
f_\varepsilon=a(a+\varepsilon I)^{-1}\uparrow p
\quad\text{strongly and ultraweakly}.
\tag{BK.8}
\]

Indeed the scalar functions \(t/(t+\varepsilon)\) make \(f_\varepsilon\) positive contractions, increasing as \(\varepsilon\) decreases. They vanish on \(\ker a\). On \(aH\),

\[
(I-f_\varepsilon)a\xi
=\varepsilon a(a+\varepsilon I)^{-1}\xi,\qquad
\|(I-f_\varepsilon)a\xi\|\leq\varepsilon\|\xi\|.
\tag{BK.9}
\]

This proves convergence to the identity on a dense subset of \(pH\). The contraction bound extends it to that whole space: approximate \(\zeta\in pH\) by \(a\xi\) and bound the error by \(2\|\zeta-a\xi\|+\varepsilon\|\xi\|\). On its orthogonal complement all cutoffs are zero, proving the strong limit. BK-02 gives membership \(p\in M\); BK-03 and BK-04 give the ultraweak limit and the supremum assertion.

Any projection \(q\) with \(qa=a\) has closed range containing \(aH\), hence contains \(pH\). Thus \(p\) is the smallest such projection, called \(s(a)\). The equality \(\ker a=\ker a^{1/2}\) proves \(s(a)=s(a^{1/2})\). Reparameterizing gives \(ta(I+ta)^{-1}\uparrow s(a)\).

A useful domination consequence needs no commutation assumption: if \(p\leq e\leq I\) and \(p\) is a projection, then \(ep=pe=p\). Indeed \(0\leq p(I-e)p\leq p(I-p)p=0\), so
\(\|(I-e)^{1/2}p\xi\|^2=0\) for every \(\xi\). Hence \((I-e)p=0\), and its adjoint gives the other equality.

## Polar decomposition and its regularized limit

For \(x\in M\), put \(a=|x|=(x^*x)^{1/2}\). There is a unique partial isometry \(u\in M\) with

\[
x=u|x|,\qquad\ker u=\ker x.
\tag{BK.10}
\]

A partial isometry here is zero on its kernel and isometric on its orthogonal complement. Its initial and final projections are
\(u^*u=s(|x|)\) and \(uu^*=s(|x^*|)\). Its bounded regularizations
\(u_\varepsilon=x(|x|+\varepsilon I)^{-1}\)
are contractions and converge strongly* to \(u\).

To construct it, \(\|x\xi\|=\|a\xi\|\) shows that
\(a\xi\mapsto x\xi\) is a well-defined isometry on \(aH\). Extend it to an isometry \(\overline{aH}\to\overline{xH}\), and let it vanish on \(\ker a\). This defines \(u\) on all of \(H\), with \(ua=x\). Its initial and final projections are the projections onto these two closed ranges. The range-kernel identity and \(\ker|x^*|=\ker x^*\) identify the second as \(s(|x^*|)\).

Although \(u\) was constructed as a bounded map on \(H\), it belongs to the algebra. The calculus places \(u_\varepsilon\) in \(M\), and
\(u_\varepsilon=u f_\varepsilon\), where \(f_\varepsilon\) is the cutoff of \(a\). Since \(f_\varepsilon\to p=s(a)\) strongly and \(up=u\), these contractions converge strongly to \(u\); strong closedness gives \(u\in M\). For adjoints use the separate calculation
\(u_\varepsilon^*=f_\varepsilon u^*\to pu^*=u^*\);
taking adjoints of an arbitrary strong limit would not be valid. A second partial isometry satisfying (BK.10) agrees on \(aH\), hence its closure, and is zero on the same orthogonal complement. This proves uniqueness.

For \(C:H\to K\), the identical construction gives \(C=U|C|\) between two possibly different Hilbert spaces. Here \(U\) is zero on \(\ker C\) and unitary from \((\ker C)^\perp\) onto \(\overline{\operatorname{ran}C}\). The operators \(C(|C|+\varepsilon I_H)^{-1}\) and their adjoints converge strongly to \(U\) and \(U^*\) in the respective directions. There is also the left factorization

\[
C=|C^*|U,\qquad |C^*|=(CC^*)^{1/2}.
\tag{BK.11}
\]

Indeed \(U|C|U^*\) is positive and has square \(U|C|^2U^*=CC^*\), since \(U^*U\) is the support of \(|C|\). Positive-square-root uniqueness from BK-01 gives
\(|C^*|=U|C|U^*\), and multiplication by \(U\) proves (BK.11).
If \(C\) is injective with dense range, the initial and final spaces are all of \(H,K\); thus \(U:H\to K\) is unitary.

## Testing commutation on unitaries

Every element of a unital norm-closed *-algebra is a complex linear combination of at most four unitaries. For a self-adjoint contraction \(b\), the calculus gives
\(c=(I-b^2)^{1/2}\) commuting with \(b\). Thus

\[
v=b+ic,\qquad v^*v=vv^*=I,\qquad b=(v+v^*)/2.
\]

Scale any nonzero self-adjoint element to a contraction. Then decompose a general \(z\) as
\((z+z^*)/2+i(z-z^*)/(2i)\), two self-adjoint parts, obtaining at most four unitaries. Zero parts can be omitted.

Commuting with all unitaries therefore implies commuting with every element of the algebra. In particular a bounded map commuting with every unitary in \(M'\) belongs to \(M''=M\). This proves the algebra-membership test used for contractions first constructed on closures of operator ranges.

## Problems and worked solutions

**Problem 1: nets on a nonseparable Hilbert space.** Let \(J\) be uncountable and \(P_F\) the coordinate projection for a finite \(F\subset J\) in \(\ell^2(J)\). Determine its increasing strong limit and its norm distance to that limit. Can a sequence of these projections have the same strong limit?

**Solution.** For a fixed vector, the squared norm is the supremum of its finite coordinate sums. Choosing a finite set which captures all but a prescribed error proves \(P_F\xi\to\xi\) as \(F\) increases. Thus \(P_F\uparrow I\). But \(\|I-P_F\|=1\): it is a contraction and fixes a unit coordinate outside \(F\). For any sequence \(F_n\), the union is countable; a coordinate outside that union is annihilated by every \(P_{F_n}\). Such a sequence cannot converge strongly to \(I\).

**Problem 2: a polar limit with constant norm error.** On \(\ell^2(\mathbb N)\), let \(x\delta_n=n^{-1}\delta_n\). Find its polar factor and \(\|x(x+\varepsilon I)^{-1}-u\|\).

**Solution.** Positivity and injectivity give \(|x|=x\). Its range contains every finite-support vector and is dense, so \(u=s(x)=I\). The cutoff coefficients are \(1/(1+\varepsilon n)\), giving

\[
\|x(x+\varepsilon I)^{-1}-I\|
=\sup_{n\geq1}\frac{\varepsilon n}{1+\varepsilon n}=1.
\]

Convergence on finite-support vectors and the common contraction bound still prove strong convergence. The inverse sends \(\delta_n\) to \(n\delta_n\), so it has no bounded extension; this explains the strict lower-bound hypothesis in BK-05.

**Problem 3: supports without commuting projections.** For \(a,b\in M_+\), prove
\(\ker(a+b)=\ker a\cap\ker b\) and
\(s(a+b)H=\overline{s(a)H+s(b)H}\).

**Solution.** If \((a+b)\xi=0\), its pairing with \(\xi\) is
\(\|a^{1/2}\xi\|^2+\|b^{1/2}\xi\|^2=0\).
Both vectors vanish; hence \(a\xi=b\xi=0\). The reverse inclusion is immediate. Orthogonality to a sum of two subspaces is exactly orthogonality to both, so taking orthogonal complements of this kernel identity proves the support formula. Its projection belongs to \(M\) because it is \(s(a+b)\). Products of the separate support projections need not themselves be projections.

## Exact uses and the remaining boundary

The proofs retain every bounded conclusion needed by the downstream lessons:

| Consumer | Written bounded input |
| --- | --- |
| DW-02, range contraction in \(M\) | Bicommutant BK-02 and four-unitary test BK-08 |
| DW-03, diagonal pairing for \(x^*x\) | Polar factor and initial support BK-07 |
| DW-04 and QF-03 | Rectangular and left polar factorizations BK-07 |
| DW-05 and QF-07 | Increasing and decreasing bounded nets BK-04 |
| WG-007 | Congruence preserves bounded increasing suprema, BK-04 |
| WG-008 | Inverse order BK-05, supports and projection domination BK-06 |
| WG-008, ultraweak density | Bounded weak-to-ultraweak convergence and fixed multiplication BK-03 |
| SK-08 | Algebra membership of bounded calculi, BK-02 and BK-08 |

The earlier RC Hilbert proof and GP0 Bernstein proof, together with the extensions written in BK-01, discharge this lesson's Hilbert and self-adjoint continuous-calculus contracts. The arguments construct the spectrum restriction, its exact norm, inverse and order rules, and square-root uniqueness before using them in subsequent sections. They do not require an unbounded spectral theorem.

Borel calculus, unbounded polar decomposition, normal-map characterization, weight-map closability and modular derivatives are separate theorems with separate proofs.

# Weight one: the theorem of Deligne and Serre

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

In weight one the determinant has no cyclotomic power. The representation attached to a holomorphic eigenform is a complex representation with **finite image**. Its good-prime eigenvalues are roots of unity, and its projective image is one of the finite rotation groups. The construction nevertheless passes through higher weight and reduction modulo auxiliary primes.

We keep **arithmetic Frobenius** \(\operatorname{Fr}_p\), acting on residue fields by \(x\mapsto x^p\). A Dirichlet character \(\varepsilon\) determines the finite Galois character \(\varepsilon_G\) characterized by \(\varepsilon_G(\operatorname{Fr}_p)=\varepsilon(p)\) for \(p\nmid N\). Thus \(\varepsilon_G(c)=\varepsilon(-1)\). Local reciprocity still sends a uniformizer to geometric Frobenius, the inverse of arithmetic Frobenius. The Weil–Deligne relation remains \(r(w)Nr(w)^{-1}=|w|N\); finite-image complex representations here have \(N=0\).

The prerequisites are the actual Frobenius-density and uniqueness proof in *Frobenius elements and determination by traces*, the written Fourier-lattice proofs in the modular-forms programme, and the ideal and ray-class arguments identified in §5. The higher-weight representation construction is still a required dependency: its current geometric gaps are retained explicitly in §6. The full statement below is preserved, and the portions actually closed in this edition are distinguished from that remaining proof obligation.

**Lemma 0.1 (the finite Dirichlet Galois character).** A Dirichlet character modulo \(N\) gives the continuous finite character \(\varepsilon_G\) described above; it is unramified outside \(N\), with the stated arithmetic Frobenius and complex-conjugation values.

*Proof.* Define it on \(\zeta_N\mapsto\zeta_N^a\) by \(\varepsilon(a)\). We check that every unit \(a\bmod N\) occurs. The cyclotomic polynomial \(\Phi_N\) has integer coefficients, by induction and monic division of \(X^N-1\) by the factors with proper-divisor indices. Let \(f\) be the irreducible rational polynomial of \(\zeta_N\); monic factors of integer monic polynomials are integral by Gauss's lemma. Its elementary proof is that a product of two primitive integer polynomials remains primitive, as reduction modulo any proposed common prime divisor shows, followed by clearing rational denominators. If for a prime \(r\nmid N\) the root \(\zeta_N^r\) belonged to a different irreducible factor \(g\), then \(f\mid g(X^r)\). Reduction modulo \(r\) would give a common factor of \(\bar f\) and \(\bar g\), because \(\overline{g(X^r)}=\bar g(X)^r\). But both divide \(X^N-1\), square-free modulo \(r\), whose derivative is \(NX^{N-1}\). This is impossible. Thus every such prime power sends a root of \(f\) to a root of \(f\); factoring any positive integer coprime to \(N\) into these primes shows that all primitive roots are conjugate. This proves the cyclotomic Galois group assertion.

For \(p\nmid N\), the polynomial \(X^N-1\) has simple roots in a finite residue-field extension. The unramified-extension construction and Hensel proof in Lesson 01, Lemma 0D.1 and Proposition 0F.2, lift them all in a finite unramified local extension. Arithmetic Frobenius acts there by the \(p\)-th power on these roots, by its residue action and uniqueness of the simple lifts. Complex conjugation inverts roots of unity. These give every claimed value. Restriction to the finite cyclotomic extension makes the character continuous. ∎

## 1. The exact theorem

**Theorem 1.1 (Deligne–Serre).** Let
\[
0\ne f\in M_1(\Gamma_0(N),\varepsilon),\qquad \varepsilon(-1)=-1,
\qquad T_pf=a_pf\quad(p\nmid N).
\tag{1}
\]
There is a continuous representation
\[
\rho_f:G_{\mathbf Q}\longrightarrow\operatorname{GL}_2(\mathbf C),
\tag{2}
\]
where \(\mathbf C\) has the discrete topology, unramified outside \(N\), with
\[
\det(X-\rho_f(\operatorname{Fr}_p))
=X^2-a_pX+\varepsilon(p)\quad(p\nmid N).
\tag{3}
\]
It is irreducible if and only if \(f\) is cuspidal. If \(f\) is a **normalized primitive cusp form of exact level \(N\)**, then
\[
\operatorname{cond}(\rho_f)=N,\qquad L(s,\rho_f)=L(s,f),
\tag{4}
\]
including the factors at primes dividing \(N\).

These are the complete assertions of Deligne–Serre's freely readable original article, Theorems 4.1 and 4.6. The theorem's first part does not require primitivity, normalization, or eigenvector conditions at primes dividing \(N\). In (1), \(a_p\) denotes the eigenvalue. For a normalized cusp eigenform it is also the \(p\)-th Fourier coefficient. Proposition 3.2 proves the cusp construction once the required higher-weight residual representations are supplied; Lemma 3.3 proves the exact bad-factor deduction once the primitive modular functional-equation inputs are supplied. The residual geometry, noncuspidal classification and general primitive inputs are presently unclosed, as specified in §6. The citation identifies the full result and does not substitute for those missing proofs.

Continuity makes the image finite: the compact image of the profinite group \(G_{\mathbf Q}\) in a discrete space is finite. A finite group representation over \(\mathbf C\) is semisimple. Indeed, if \(U\subset V\) is stable, average any projection \(P:V\to U\):
\[
P_G=\frac1{|G|}\sum_{g\in G}gPg^{-1}.
\tag{5}
\]
Its image is \(U\), it acts as the identity on \(U\), and its kernel is a stable complement. This also proves that (3) determines the isomorphism class: apply the characteristic-zero trace uniqueness theorem from lesson 2, or its finite-group character proof, after passing to a common finite quotient.

Primitivity in (4) matters. A form of level \(23\), viewed as an old form of level \(46\), has the same good-prime traces and the same representation. It need not become ramified at \(2\). The conclusion “ramified at every prime dividing \(N\)” follows from the **exact conductor assertion** in (4), not from the general statement (1).

## 2. Determinant, oddness, and the weight-one bound

These deductions concern any representation satisfying (2)–(3); they do not assume that the retained proof obligations in Theorem 1.1 have already been discharged.

**Theorem 2.1 (global determinant).** Under (1),
\[
\det\rho_f=\varepsilon_G.
\tag{6}
\]

**Proof.** Both characters have finite image. Their quotient \(d\) factors through a finite Galois extension. Equation (3) gives \(d(\operatorname{Fr}_p)=1\) at every \(p\nmid N\). Every conjugacy class of the finite quotient occurs as a Frobenius class at a prime outside this finite excluded set, by Chebotarev. Since \(d\) is a character, its value on that entire class is \(1\). Thus \(d=1\). ∎

**Corollary 2.2 (oddness).** If \(c\) is complex conjugation, then
\[
\rho_f(c)\sim
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{7}
\]

**Proof.** Since \(c^2=1\), the matrix is annihilated by \((X-1)(X+1)\), which has distinct roots over \(\mathbf C\). It is diagonalizable with eigenvalues in \(\{1,-1\}\). Its determinant is \(\varepsilon(-1)=-1\), so exactly one eigenvalue is \(-1\). ∎

**Corollary 2.3 (Ramanujan in weight one).** For \(p\nmid N\), the roots \(\alpha_p,\beta_p\) of (3) are roots of unity. Consequently
\[
a_p=\alpha_p+\beta_p,\qquad |a_p|\leq2.
\tag{8}
\]
The same bound holds after every complex embedding of the coefficient field.

**Proof.** An element of a finite image has finite order, say \(m\). Its matrix is annihilated by \(X^m-1\), whose roots are distinct roots of unity. The triangle inequality gives (8). A field embedding sends a root of unity to another root of unity, so it gives the same bound for the conjugate trace. ∎

There are only finitely many values of \(a_p\) at good primes, since there are only finitely many matrices in the image. This is a consequence of the finite-image theorem. The analytic estimate used in its construction gives a weaker intermediate statement, proved next.

## 3. Rankin's estimate and the construction

In this section assume \(f\) is cuspidal. The Eisenstein case is handled separately at the end of the outline.

For a set \(X\) of primes, define its upper analytic density by
\[
\overline\delta(X)=\limsup_{s\to1^+}
\frac{\sum_{p\in X}p^{-s}}{\log(1/(s-1))}.
\tag{9}
\]
The denominator agrees with \(\sum_p p^{-s}\) up to a bounded error. To see this, take the logarithm of Euler's product for \(\zeta(s)\); its prime-power terms of exponent at least two stay bounded near \(1\), and \((s-1)\zeta(s)\to1\).

We construct the coefficient field, integral lattice and conjugate cusp packets below from the actual rational Fourier-basis argument in the earlier modular-forms programme. The estimate proved next then gives, for every conjugate cusp packet,
\[
\sum_{p\nmid N}|\sigma(a_p)|^2p^{-s}
\leq\log(1/(s-1))+O_\sigma(1)\quad(s\to1^+).
\tag{10}
\]
Its use for all embeddings, and the integrality, are essential.

**Lemma 3.0 (the weight-one cusp lattice).** The good-prime eigenvalues and character values of a cusp eigenpacket in (1) are algebraic integers in a fixed number field. Every embedding of that field gives another holomorphic cusp eigenpacket. There is a full integral lattice preserved by all Hecke operators and diamonds in \(S_1(\Gamma_1(N))\).

*Proof.* Use the actually written rational Fourier bases of
\(S_5(\Gamma_1(N))\), \(S_7(\Gamma_1(N))\) and \(S_{11}(\Gamma_1(N))\) from *Modular symbols and the algebraicity of Hecke eigenvalues*, §2, equations (2.1)–(2.8), and §3, Theorems 3.1–3.2 and equation (3.5). Their proof uses integral group cohomology and its reflection involution, followed by the perfect Fourier pairing. We use this rational-basis conclusion, rather than its later stronger integral-duality assertion, which has additional arithmetic-model hypotheses. The odd-weight extension to regular principal covers is explicitly part of its §2.1. Its analytic curve and period prerequisites remain part of the earlier programme chain.

Multiplication by the full-level integral series \(E_4,E_6\) defines the linear map
\[
 S_5\oplus S_7\longrightarrow S_{11},\qquad
 (g_5,g_7)\longmapsto E_6g_5-E_4g_7.
\]
It is rational for these Fourier structures: the product coefficients of rational series are rational, and the rational Fourier structure is exactly the set of forms with rational coefficients. Its kernel is
\(\{(fE_4,fE_6):f\in S_1(\Gamma_1(N))\}\).
For the converse, divide the equality by \(E_4E_6\). The two quotients agree where both are defined. They glue holomorphically everywhere because \(E_4,E_6\) have no common zero: \(E_4^3-E_6^2=1728\Delta\), and \(\Delta\) is nowhere zero on \(\mathfrak H\), by the actual discriminant proof in the valence lesson, Theorem 2.1. At every cusp both full-level forms have constant term one in a scaling coordinate. Division preserves cusp vanishing there. Hence the quotient is precisely a weight-one cusp form. The kernel thus gives its full rational Fourier structure and commutes with complex scalar extension.

Its integral-coefficient subgroup \(S_1(\mathbf Z)\) is a full finite free lattice. To see fullness, choose a rational kernel basis and clear its finitely many denominators in the integral Fourier bases of \(S_5,S_7\). Then \(g_5\) has integer coefficients; division by \(E_4\), whose constant term is one and whose coefficients are integers, has integer formal coefficients as well. Conversely an integer-coefficient \(f\) has \(fE_4\in S_5(\mathbf Z)\). This injects the entire subgroup into that finite free lattice, proving finite generation, and the basis just obtained proves fullness.

Diamonds act rationally on this space: they commute with multiplication by the full-level \(E_4,E_6\), and their higher-weight actions are rational in the same actual Fourier-basis proof. There are finitely many diamonds. Define
\[
 L=\bigcap_{u\in(\mathbf Z/N)^\times}[u]^{-1}S_1(\mathbf Z).
\]
A finite intersection of full lattices in one rational vector space is full: clear the finitely many matrix denominators in any one rational basis. Diamond multiplication permutes the intersection, so all diamonds preserve \(L\). For \(f\in L\), the weight-one prime coefficient formula is
\(a_r(T_pf)=a_{pr}(f)+a_{r/p}([p]f)\) at a good prime, and coefficient selection at a bad prime. These are integers. Since every diamond commutes with \(T_p\), apply the same formula to each \([u]f\) to see that all diamond transforms of \(T_pf\) also have integer coefficients. Thus \(T_pL\subset L\), and the all-index Hecke recursions prove stability for every \(T_n\).

The algebra of good operators and diamonds acts faithfully on \(L\), and is a finite free subgroup of \(\operatorname{End}_{\mathbf Z}(L)\). Its eigenvalues are integral by the monic integer characteristic polynomials; its character image over \(\mathbf Q\) is a finite-dimensional rational domain, hence a number field. This applies to the given good eigenpacket even when the original form is not a bad-prime eigenvector. Its simultaneous eigenspace is defined over that number field by rational matrix equations. An embedding extends to an automorphism of \(\mathbf C\), by a transcendence basis and algebraic extension. Acting on the scalar coordinates of the finite rational cusp space produces a holomorphic cusp form with the conjugate eigenvalues and character. No discontinuous automorphism is applied term by term to an analytic limit. This proves every assertion. ∎

The same finite-intersection argument supplies the lattice in each higher cusp weight used below. More explicitly, the actual proof in *Modular symbols and the algebraicity of Hecke eigenvalues*, §3, writes \(S_k(\mathbf Z)=\operatorname{Hom}_{\mathbf Z}(A_k,\mathbf Z)\), where \(A_k=\sum_{n\ge1}\mathbf ZT_n\) is finite free and spans the rational Hecke algebra. Since an integral basis of \(A_k\) is a finite integral combination of the \(T_n\), a form with coefficients in a DVR belongs to \(S_k(\mathbf Z)\otimes\mathcal O\) exactly when all its Fourier coefficients belong to \(\mathcal O\). Intersect the finitely many diamond translates of this lattice to obtain \(L_k\). For a chosen character packet, all those translates are scalar multiples by roots of unity, so its coefficient-integrality criterion is unchanged. Finite intersections commute with localization and flat scalar extension: realize the intersection as the kernel of the map from the direct sum of the lattices to their common rational space, and tensor that exact sequence. This uses only the actually proved Fourier dual lattice, rather than a stronger canonical integral cohomology comparison. Products with the integral full-level \(E_{\ell-1}\) lie in this lattice after localization, and a coefficient congruence modulo its uniformizer is a congruence of lattice vectors. This supplies the local lattice step from the specified earlier Fourier-basis proof. Its recorded analytic dimension foundations still need their exact earlier bindings; it supplies no missing higher-weight Galois representation. ∎

**Lemma 3.0A (Rankin's inequality without normalization).** Every nonzero weight-one cusp form satisfying the good-prime eigenvector conditions in (1) satisfies (10) for its given complex embedding.

*Proof.* Write \(f=\sum_{r\geq1}c_rq^r\), and choose \(m\) with \(c_m\ne0\). Put \(H(z)=y|f(z)|^2\). Its invariance under \(\Gamma_0(N)\) follows from the weight-one transformation and \(|\varepsilon|=1\). For representatives of \(\Gamma_0(N)\backslash\operatorname{SL}_2(\mathbf Z)\), form the nonnegative invariant function
\[
 F(z)=\sum_\gamma H(\gamma z).
\]
Each summand decays exponentially at infinity, up to a factor \(y\): it is \(y|(f|_1\gamma)(z)|^2\), and the cusp expansion of a cusp form has strictly positive exponents in its cusp coordinate. There are finitely many representatives. Thus \(F(z)\le Cye^{-cy}\) on the full modular fundamental region for some \(c>0\).

Use the full-level nonholomorphic Eisenstein series \(E(z,s)\). Its actual theta-integral continuation and residue are proved in *Non-holomorphic Eisenstein series and Maass forms*, §3, Theorem 3.2 and Corollary 3.3. The integrable cusp estimate in *The Rankin–Selberg method*, §2, Lemma 2.1, applies to this \(F\) as well: its proof bounds the entire part of the theta integral by \(C_Ay^{A+3/2}\) on every compact set of parameters, which the exponential bound just proved absorbs. Consequently
\[
 I(s)=\int_{\operatorname{SL}_2(\mathbf Z)\backslash\mathfrak H}
             F(z)E(z,s)\,\frac{dx\,dy}{y^2}
       =O((s-1)^{-1})\qquad(s\downarrow1).
\]
For real \(s>1\), use first a finite partial sum of the defining Eisenstein series. Change variables in each of its finitely many terms. Their transformed domains tile a finite subset of the period strip, and their integrals sum to at most \(I(s)\), since the remaining terms are nonnegative. These subsets exhaust the strip. The integral of a nonnegative continuous function there is the supremum over compact subsets; exhaustion therefore proves that its full strip integral is at most \(I(s)\). Since \(F\ge H\), the same bound holds for \(H\). At fixed \(y>0\), the Fourier series converges uniformly in \(x\). Integrating squared finite Fourier sums, then passing to that uniform limit, gives the orthogonal coefficient sum. Retain any finite number of its nonnegative terms and integrate in \(y\). The Gamma integral gives their finite weighted sum; increasing the number of terms proves
\[
 \frac{\Gamma(s)}{(4\pi)^s}
       D_f(s)\le I(s),\qquad
 D_f(s)=\sum_{r\ge1}|c_r|^2r^{-s}.
\]
In particular \(D_f(s)\) converges for every \(s>1\) and is \(O((s-1)^{-1})\).

Exclude the finitely many primes dividing \(Nm\). The prime coefficient formula proved in *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, Theorem 2.3 and Theorem 3.1, says
\(c_{pr}=a_pc_r-\varepsilon(p)c_{r/p}\).
Induction on prime powers and then on distinct primes, since none divides \(m\), gives
\[
 c_{mn}=c_m b_n,\qquad
 b_n=\prod_{p^r\parallel n}h_r(\alpha_p,\beta_p),\qquad
 h_r(A,B)=\sum_{j=0}^r A^{r-j}B^j,
\]
for \(n\) supported on the remaining primes; here \(\alpha_p+\beta_p=a_p\), \(\alpha_p\beta_p=\varepsilon(p)\). Thus
\(D_0(s)=\sum_n|b_n|^2n^{-s}\le m^s|c_m|^{-2}D_f(s)\).
It has a convergent Euler product with nonnegative local coefficients. The four-root formal identity is proved in *The Rankin–Selberg method*, Lemma 3.1; applying it to \((A,B,C,D)=(\alpha_p,\beta_p,\bar\alpha_p,\bar\beta_p)\) gives
\[
 \sum_{r\ge0}|h_r(\alpha_p,\beta_p)|^2T^r
 =\frac{1-T^2}
 {\prod_{i,j=1}^2(1-\alpha_{p,i}\bar\alpha_{p,j}T)}.
\]
The convergence for every \(s>1\) implies
\(\max(|\alpha_p|,|\beta_p|)\le\sqrt p\).
Indeed \(|\alpha_p\beta_p|=1\). If the larger root has magnitude \(R>1\), the formula \(h_r=(\alpha_p^{r+1}-\beta_p^{r+1})/(\alpha_p-\beta_p)\) has exponential rate \(R^r\); if both magnitudes are one, its rate is at most polynomial. Convergence of \(\sum_r|h_r|^2p^{-rs}\) for all \(s>1\) consequently forces \(R^2\le p\). Therefore every geometric logarithm below converges when \(s>1\).

Multiply the local identities by the factors of \(\zeta_0(2s)\), with the same omitted primes, and take real logarithms. The coefficient of \(p^{-rs}\) in the logarithm of the resulting four-root product is
\(|\alpha_p^r+\beta_p^r|^2/r\ge0\).
For finite prime sets the term with \(r=1\) therefore gives
\[
 \sum_{p\nmid Nm}|a_p|^2p^{-s}
 \le\log\bigl(\zeta_0(2s)D_0(s)\bigr)
 \le\log(1/(s-1))+O(1).
\]
Passing to all primes is valid by monotonicity on the left and by the convergent nonnegative Euler product on the right. The finitely many primes dividing \(m\), but not \(N\), contribute \(O(1)\). This is (10). The same proof applies individually to every actually supplied conjugate cusp form. ∎

**Lemma 3.0B (an Eisenstein congruence).** For every prime \(\ell\ge5\), the normalized full-level series \(E_{\ell-1}\) has \(\ell\)-integral coefficients and is congruent to one modulo \(\ell\).

*Proof.* The Eisenstein construction in the earlier modular-forms lesson, *Modular forms, lattice functions and Eisenstein series*, §4, Proposition 4.1 and Theorem 4.2, gives
\(E_n=1-(2n/B_n)\sum_{r\ge1}\sigma_{n-1}(r)q^r\) for even \(n>2\), with \(B_j\) defined by \(t/(e^t-1)=\sum B_jt^j/j!\). Its coefficient recursion is
\(\sum_{j=0}^{r}\binom{r+1}{j}B_j=0\) for \(r>0\).
Hence \(B_j\) is \(\ell\)-integral for \(0\le j\le\ell-2\), by induction, and \(\ell B_{\ell-1}\) is integral. Multiplying the generating function by \((e^{\ell t}-1)/t\) gives the power-sum identity
\[
 \sum_{a=0}^{\ell-1}a^{\ell-1}
   =\frac1\ell\sum_{j=0}^{\ell-1}
         \binom\ell j B_j\ell^{\ell-j}.
\]
The last term is \(\ell B_{\ell-1}\); all earlier terms are divisible by \(\ell^2\), since their Bernoulli numbers are integral and, for \(1\le j<\ell\), \(\binom\ell j\) is divisible by \(\ell\). The sum on the left is \(-1\) modulo \(\ell\), because every nonzero residue has \((\ell-1)\)-st power one. Thus \(v_\ell(B_{\ell-1})=-1\). The coefficient multiplier \(-2(\ell-1)/B_{\ell-1}\) has valuation one. Every divisor sum is an integer, proving the assertion. ∎

**Lemma 3.0C (lifting an eigenpacket).** Let \(\mathcal O\) be a discrete valuation ring with characteristic-zero fraction field and uniformizer \(\pi\), let \(M\) be finite free, and let a commuting collection of endomorphisms preserve \(M\). A simultaneous eigencharacter occurring in \(M/\pi M\) lifts, after a finite extension of the fraction field and a place above \(\pi\), to a characteristic-zero eigencharacter occurring in \(M\otimes\operatorname{Frac}(\mathcal O)\).

*Proof.* The generated algebra \(T\subset\operatorname{End}_{\mathcal O}(M)\) is a finite torsion-free \(\mathcal O\)-module: submodules of a finite free module over a DVR are finite free, by Lesson 01, Lemma 0A.1. It is commutative. The residual eigencharacter has kernel a maximal ideal \(\mathfrak m\) of \(T\) containing \(\pi\). Multiplication by \(\pi\) remains injective in \(T_{\mathfrak m}\), so \(T_{\mathfrak m}[1/\pi]\ne0\). Choose a prime there and contract it to \(\mathfrak p\subset\mathfrak m\). Since \(T[1/\pi]\) is a finite-dimensional algebra over the fraction field, its prime quotients are finite fields over that field. The resulting character \(T\to E\) is integral over \(\mathcal O\). Here is the needed place construction for an arbitrary DVR. The integral closure \(B\) of \(\mathcal O\) in \(E\) is finite: choose an integral field basis; traces of products of integral elements are integral, so \(B\) is contained in the dual of its basis lattice under the nondegenerate separable trace pairing. Both lattices are finite free by Lemma 0A.1 of Lesson 01. Localize the finite extension \(T/\mathfrak p\subset B\) at \(\mathfrak m/\mathfrak p\). Its maximal ideal cannot generate the whole finite nonzero module \(B\), by the determinant proof of Nakayama given in *Discrete valuation rings and Dedekind domains*, “What one prime sees”, Nakayama’s lemma. A maximal ideal \(\mathfrak q\) above it therefore exists. Its contraction is the given maximal ideal: an integral subring of a field is a field whenever the larger ring is a field, since the monic equation of an inverse expresses that inverse in the subring. The normal one-dimensional local ring \(B_{\mathfrak q}\) is a DVR by the actual DVR characterization proved in that same section. Indeed, \(B[1/\pi]=E\) is a field, so every nonzero prime of \(B\) lies above \(\pi\); the local dimension is one. Its valuation gives the required place and reduction. The character occurs in \(M\otimes E\). For completeness, the finite-algebra decomposition needed to verify occurrence has an elementary matrix proof. Over an algebraically closed splitting field, commuting matrices can be simultaneously triangularized. Find a common eigenvector by restricting successively to eigenspaces of a finite generating set; commutation preserves each restriction. Apply the same argument to the quotient by that line and induct. The finitely many diagonal characters give distinct maximal ideals \(\mathfrak n_i\), whose intersection acts by strictly upper-triangular matrices and thus has its \(\dim M\)-th power zero. Their powers are pairwise comaximal, and their product is that same power of the intersection. The Chinese remainder decomposition follows by writing \(1=x+y\) for two comaximal ideals and expanding its sufficiently large power to prove comaximality of their powers; the standard map to the two quotients is onto by this equality and has their intersection as kernel. Induction gives the decomposition into the local factors. Faithfulness of the action makes every factor act on a nonzero summand. On the desired summand its maximal ideal is nilpotent; the last nonzero term of its powers is killed by that maximal ideal, and any nonzero vector there is an eigenvector. The simultaneous eigenvector equations for the prescribed character have coefficients in \(E\); matrix rank is unchanged by field extension, so their nonzero kernel already exists over \(E\). Reduction of eigenvalues, rather than equality of a chosen residual vector, is the conclusion. ∎

**Lemma 3.0D (two-dimensional finite-field descent).** Let \(k\) be a finite field of odd characteristic, and let a semisimple two-dimensional representation of a finite group be defined over a finite extension of \(k\). If every group element has characteristic polynomial in \(k[X]\), the representation has a two-dimensional model over \(k\).

*Proof.* We give the finite-algebra details used both here and in the next lemma. For a semisimple two-dimensional representation over any finite field \(u\) of odd characteristic, let \(A\) be the \(u\)-span of its image. If the representation is reducible, its stable complement shows that \(A\) is the scalar algebra or the diagonal algebra. If it is irreducible and contains an element with an irreducible quadratic polynomial, its span is a quadratic field \(L\). Either \(A=L\), or an element \(B\notin L\) gives the four-dimensional direct sum \(L+LB\subset A\), so \(A=M_2(u)\). If an element has two distinct eigenvalues in \(u\), its two spectral projectors belong to \(A\); irreducibility supplies both off-diagonal matrix units, so again \(A=M_2(u)\). Finally a nonscalar repeated-root matrix gives, after subtracting its scalar part, \(E_{12}\). Irreducibility supplies a matrix \(B=(b_{ij})\) with \(b_{21}\ne0\); then \(E_{12}B-b_{22}E_{12}=b_{21}E_{11}\), giving the projectors and the remaining units. These cases exhaust the possibilities. In particular extension to an algebraic closure remains semisimple.

If the representation is a sum \(\chi_1\oplus\chi_2\) over the algebraic closure, equal characters have values in \(k\), because their trace is \(2\chi_1\). Otherwise choose \(g\) with eigenvalues \(a\ne b\). They lie in a field \(L/k\) of degree at most two, and
\[
 \chi_1(h)=\frac{\operatorname{tr}(gh)-b\operatorname{tr}(h)}{a-b},\qquad
 \chi_2(h)=\frac{a\operatorname{tr}(h)-\operatorname{tr}(gh)}{a-b}.
\]
The characters are thus defined over \(L\). Its Galois automorphism either fixes both, giving a diagonal \(k\)-model, or exchanges them. In the latter case multiplication by \(\chi_1(h)\) on the two-dimensional \(k\)-space \(L\) has precisely the two required eigenvalues.

In the absolutely irreducible case choose four image matrices \(g_i\) forming a basis of the full matrix algebra over the larger field. The trace-pairing matrix \((\operatorname{tr}(g_ig_j))\) is invertible and has entries in \(k\). Pairing a product \(g_ig_j\) against the basis shows that its expansion coefficients lie in \(k\), since \(\operatorname{tr}(g_ig_jg_t)\in k\). Therefore their \(k\)-span \(A\) is a four-dimensional algebra with scalar extension \(M_2\). It is central simple: an ideal becomes an ideal of \(M_2\), and the center becomes its scalar center, by exact scalar extension of the relevant linear equations. In particular its center is \(k\).

It cannot be a division algebra. If it were, a nonscalar traceless element \(i\) would satisfy \(i^2=a\in k^\times\), with irreducible quadratic polynomial. The identities \(\operatorname{tr}(x)\in k\) and
\(\det(x)=(\operatorname{tr}(x)^2-\operatorname{tr}(x^2))/2\in k\)
hold for every \(x\in A\); the matrix characteristic identity holds after scalar extension and hence in \(A\). The centralizer of \(i\) has dimension two and is \(L=k(i)\). The solutions of \(ji=-ij\) also have dimension two, as is checked after diagonalizing \(i\). A nonzero such \(j\) is invertible under the division assumption, satisfies \(jc=\bar c j\) for \(c\in L\), and has \(j^2=b\in k^\times\). The last assertion follows because \(j^2\in L\) and commutation with \(j\) fixes it under the nontrivial automorphism of \(L/k\).

Norm \(L^\times\to k^\times\) is onto. Indeed the multiplicative group of a finite field is cyclic: its exponent is attained by combining elements of maximal prime-power orders, and its elements are roots of \(X^{\text{exponent}}-1\), so the root count makes the exponent its order. For \(|k|=q\), norm on the cyclic group of order \(q^2-1\) is the power \(q+1\) and has image of order \(q-1\). Choose \(c\) with \(c\bar c=b\). Then
\((j-c)(j+\bar c)=j^2-c\bar c=0\), with both factors nonzero, a contradiction. Thus \(A\) has a nonzero singular element \(x\). The left ideal \(Ax\) has dimension two, as it does after extension to matrices, where \(x\) has rank one. Left multiplication embeds \(A\) into \(\operatorname{End}_k(Ax)\): its kernel is an ideal and cannot be all of \(A\). Equal dimensions make this an isomorphism. Its natural module supplies the desired \(k\)-model, and scalar extension recovers the original representation. ∎

**Lemma 3.0E (the uniform image bound needed here).** Let \(G\subset\operatorname{GL}_2(k)\), for a finite field \(k\) of odd characteristic, act semisimply. Suppose more than \((1-\eta)|G|\) of its elements have characteristic polynomials in a set of at most \(M\) polynomials, where \(0<\eta<1/4\) and \(M\ge1\). Then
\[
 |G|\le\frac{M^4}{1-4\eta}.
\]

*Proof.* The image algebra described in Lemma 3.0D is scalar, diagonal, a quadratic field, or \(M_2(k)\). In each case its trace pairing is nondegenerate. For the scalar algebra this uses \(2\ne0\); for the diagonal and matrix algebras it follows from the matrix units. In the quadratic field it is the field trace pairing: if \(x\ne0\), pairing it with \(x^{-1}\) gives trace two. Choose a basis \(g_1,\ldots,g_d\) from \(G\), with \(d\le4\), and let \(S\) be the specified large subset. At least \((1-d\eta)|G|\) elements \(g\) satisfy \(g_ig\in S\) for all \(i\), by the union bound on the complements of the translates \(g_i^{-1}S\). For those elements each of the \(d\) traces \(\operatorname{tr}(g_ig)\) has at most \(M\) values. Nondegeneracy makes the map sending \(g\) to that trace tuple injective. Hence \((1-d\eta)|G|\le M^d\), which implies the displayed bound. ∎

**Lemma 3.0F (lifting a prime-to-\(\ell\) finite representation).** Let \(G\) be finite of order prime to \(\ell\), and let \(V\) be a representation of dimension two over \(\mathbf F_\ell\). It lifts to a free rank-two \(\mathbf Z_\ell\)-representation of \(G\), and hence to a finite-image complex representation after an embedding of its field of matrix entries into \(\mathbf C\).

*Proof.* Choose a surjection \(\mathbf F_\ell[G]^r\to V\). Average a linear section over \(G\), as in (5), using that \(|G|\) is invertible. It gives a \(G\)-equivariant idempotent \(e\) on the free group module whose image is \(V\). Lift its coefficients to the complete algebra
\(B=\operatorname{End}_{\mathbf Z_\ell[G]}(\mathbf Z_\ell[G]^r)\),
which is finite free over \(\mathbf Z_\ell\). If a lift \(u\) has \(u^2-u\in\ell^tB\), then \(2u-1\) is invertible: its square is \(1+4(u^2-u)\), whose inverse is its convergent geometric series. The replacement
\[
 u'=u-(2u-1)^{-1}(u^2-u)
\]
has \(u'^2-u'\in\ell^{2t}B\), by direct multiplication; all factors here are commuting polynomials or convergent series in \(u\). Iteration converges to an idempotent lifting \(e\). Its image is a direct summand of a finite free DVR module, hence free; reduction shows its rank is two. It is \(G\)-stable and has the desired reduction.

The finitely many resulting matrix entries, together with any prescribed number field already in \(\mathbf Q_\ell\), generate a finitely generated characteristic-zero field. Such a field embeds into \(\mathbf C\), extending the prescribed number-field embedding: choose complex numbers algebraically independent for a finite transcendence basis, then extend across the finite algebraic extension into the algebraically closed field \(\mathbf C\). The independent choices exist because a field generated by finitely many numbers over a number field is countable, whereas \(\mathbf C\) is uncountable. The group relations are polynomial identities, so they survive this embedding. Every eigenvalue has order dividing \(|G|\), because each group matrix is annihilated by \(X^{|G|}-1\). If the residual action is faithful, so is the lift. ∎

**Proposition 3.1 (finite coefficient set outside a small exceptional set).** Suppose \(a_p\in\mathcal O_K\), \(d=[K: \mathbf Q]\), and (10) holds for all embeddings. For every \(\eta>0\) there is a finite set \(Y\subset\mathcal O_K\) such that
\[
\overline\delta\{p\nmid N:a_p\notin Y\}\leq\eta.
\tag{11}
\]

**Proof.** For \(B>0\), let
\[
Y_B=\{a\in\mathcal O_K:|\sigma(a)|\leq B\text{ for every }\sigma\}.
\tag{12}
\]
This set is finite. Every such \(a\) has a monic minimal polynomial of degree \(e\leq d\) with integer coefficients. All its conjugates have magnitude at most \(B\); its coefficient of degree \(e-j\) has magnitude at most \(\binom ej B^j\). There are finitely many choices of these integers, finitely many such polynomials, and finitely many roots.

If \(a_p\notin Y_B\), at least one embedding has \(|\sigma(a_p)|>B\). Summing nonnegative terms gives
\[
B^2\sum_{\substack{p\nmid N\\a_p\notin Y_B}}p^{-s}
\leq\sum_\sigma\sum_{p\nmid N}|\sigma(a_p)|^2p^{-s}
\leq d\log(1/(s-1))+O(1).
\tag{13}
\]
Divide by the logarithm and take the upper limit. Choosing \(B^2\geq d/\eta\) proves (11). ∎

This is [Deligne–Serre, Proposition 5.5] with its elementary finiteness and density deductions supplied. It does **not** show that all \(a_p\) belong to a finite set. Exercise 7.4 gives an integer-valued counterexample to that inference from a prime mean-square asymptotic alone.

**Proposition 3.2 (the construction after the residual input).** Suppose the higher-weight representation construction supplies (14) for the eigenpackets lifted below, at infinitely many auxiliary primes splitting in every fixed finite enlargement of the coefficient field. Then (2)–(3) hold for this cusp eigenpacket, the representation is unramified outside \(N\), and it is irreducible. The implication is proved in the following six steps, using the lattice and conjugate packets of Lemma 3.0. Its residual premise is a required part of the full theorem, not a consequence of the currently conditional higher-weight lesson.

1. **Produce residual representations.** First choose a nonzero \(K\)-rational vector in the same good-prime and diamond eigenspace as the form in (1). Such a vector exists: Lemma 3.0 writes the eigenvector conditions as rational matrix equations over the coefficient field \(K\), and their kernel remains the same kernel after scalar extension to \(\mathbf C\). Only finitely many of these equations are needed, since intersections of subspaces in a finite-dimensional space stabilize. Clear the denominators of its coordinates in the full lattice of that lemma, and exclude the finitely many prime ideals dividing one chosen nonzero coordinate. Write \(f\) for this vector. It now has a defined nonzero reduction at every remaining \(\lambda\), with the same good-prime eigenvalues and integral unit diamond eigenvalues. For \(\ell\ge5\), put \(n=\ell-1\). Lemma 3.0B gives \(E_n\equiv1\pmod\ell\), so \(fE_n\equiv f\pmod\lambda\) in weight \(1+n\). The prime coefficient formula shows that its reduction has the required eigenpacket: its recurrence coefficient is \(\varepsilon(p)p^n\equiv\varepsilon(p)\). The product need not be a characteristic-zero eigenform. Use the higher-weight lattice described at the end of Lemma 3.0. Its coefficient criterion shows that this coefficient congruence is a congruence of vectors in the lattice. Lemma 3.0C then supplies the lifted eigenpacket. Apply the higher-weight representation construction, choose the stable lattice proved in Lesson 01, Theorem 2.1, reduce and semisimplify. Chebotarev makes the characteristic polynomial of every element belong to the residual coefficient field, since it does so for all good Frobenius elements; Lemma 3.0D then gives
   \[
   \overline\rho_\lambda:G_{\mathbf Q}\to\operatorname{GL}_2(k_f),
   \quad
   \det(X-\overline\rho_\lambda(\operatorname{Fr}_p))
   \equiv X^2-a_pX+\varepsilon(p)\pmod\lambda
   \quad(p\nmid N\ell).
   \tag{14}
   \]
   The cyclotomic exponent disappears since \(p^n\equiv1\pmod\ell\).

2. **Choose a split-prime family.** Enlarge \(K\) to a finite Galois number field containing the coefficients and character values. Use primes \(\ell\) splitting completely in \(K\), so \(k_f=\mathbf F_\ell\). These primes have positive density \(1/[K: \mathbf Q]\); they are not generally a density-one set. Infinitely many suffice. Later finite enlargements of \(K\) retain an infinite split-prime family.

3. **Bound the residual image.** Choose \(\eta=1/8\) in Proposition 3.1 and include the finitely many character values. There are at most a fixed \(M\) polynomials \(1-aT+eT^2\) with \(a\in Y\). Chebotarev converts (11) into a proportion statement in \(G_\ell=\operatorname{im}\overline\rho_\lambda\): at least \((1-\eta)|G_\ell|\) elements have characteristic polynomials in this finite set after reduction. Indeed, the complementary conjugacy-invariant set has prime density equal to its proportion in \(G_\ell\), and its primes are contained in the exceptional set of (11). Lemma 3.0E, with \(\eta=1/7\), which also handles equality at the density endpoint, proves
   \[
   |G_\ell|\leq A,\qquad A=3M^4,
   \tag{15}
   \]
   independently of \(\ell\). The trace-pairing proof supplies this bound without any finite-characteristic subgroup classification. This choice of density suffices for the full construction; no restriction has been imposed on the level or eigenpacket in (1).

4. **Recover exact finite polynomials.** Every residual eigenvalue has order at most \(A\). Enlarge \(K\) to contain all roots of unity of orders at most \(A\). Let \(\mathcal P\) be the finite set of degree-two polynomials with two such roots. For each fixed good \(p\), (14) agrees modulo infinitely many auxiliary prime ideals with a member of \(\mathcal P\). One member occurs infinitely often. A nonzero algebraic integer has only finitely many prime ideal divisors, so coefficientwise congruence at infinitely many distinct rational primes implies equality:
   \[
   X^2-a_pX+\varepsilon(p)\in\mathcal P.
   \tag{16}
   \]
   This is where a global finite set of good-prime polynomials finally emerges.

5. **Lift and remove auxiliary ramification.** Choose \(\ell>A\) and exclude the finitely many primes at which two members of \(\mathcal P\) become equal. The finite group \(G_\ell\) has order prime to \(\ell\). Lemma 3.0F gives its characteristic-zero lift. Include the prescribed enlarged number field \(K\) in the field of matrix entries and extend its chosen complex embedding as in that proof. Its finite-order eigenvalues have orders at most \(A\), so they already lie in \(K\). Their polynomial belongs to \(\mathcal P\); its reduction is (14), and the separating reduction identifies it with the exact polynomial (16). This lift is initially unramified outside \(N\ell\). Lifts made using two different auxiliary primes have the same traces outside a finite set, hence are isomorphic by finite Chebotarev in Lesson 02, Theorem 3.0c, followed by its characteristic-zero trace lemma, Lemma 4.1, on their common finite quotient. At each auxiliary prime use the other lift to conclude unramifiedness. The common representation is unramified outside \(N\).

6. **Prove cuspidal irreducibility.** A hypothetical reducible lift is \(\chi_1\oplus\chi_2\), by (5). Its determinant is \(\varepsilon_G\), by the already written proof of Theorem 2.1. Oddness makes the characters distinct. Put \(\chi=\chi_1\chi_2^{-1}\), a nontrivial character of a finite abelian quotient. Chebotarev analytic density in Lesson 02 gives
   \[
   \sum_p\chi(p)p^{-s}=o\bigl(\log(1/(s-1))\bigr).
   \]
   To see the coefficient explicitly, sum the density statement over the finitely many elements of that quotient: their character sum is zero, since multiplication by an element on which \(\chi\ne1\) preserves the sum and multiplies it by a different scalar. Omitting finitely many ramified primes has bounded effect. Consequently
   \[
   \sum_{p\nmid N}|\chi_1(p)+\chi_2(p)|^2p^{-s}
     =2\log(1/(s-1))+o\bigl(\log(1/(s-1))\bigr),
   \]
   contradicting Lemma 3.0A. A bounded cross-prime sum, stronger than this density deduction, is unnecessary. This completes the claimed implication. ∎

The noncuspidal part of Theorem 1.1 additionally needs the weight-one Eisenstein classification, yielding two finite Dirichlet characters with trace \(\chi_1(p)+\chi_2(p)\). The actually written character-Eisenstein construction in the earlier modular-forms lesson assumes weight at least two and cannot be substituted here. This remaining obligation, and the residual and arithmetic-lattice obligations in Proposition 3.2, are retained in §6.

**Lemma 3.3 (functional-equation rigidity of the bad factors).** Suppose \(f\) is a normalized primitive weight-one cusp form with completed Mellin functional equation of level \(N\), and \(\rho\) is an odd finite representation with conductor \(M\) having its good factors. Suppose the primitive bad Euler factor is \((1-a_pp^{-s})^{-1}\), with \(|a_p|\le1\), allowing \(a_p=0\). Then the completed Artin functional equation implies \(M=N\) and equality of every Euler factor.

*Proof.* At a bad prime the eigenvalues \(b_p,c_p\) of \(\rho(\operatorname{Fr}_p)\) on inertia invariants are roots of unity or absent; denote absent eigenvalues by zero. The odd archimedean representation has eigenvalues \(1,-1\), so the product of its two real Gamma factors is the weight-one complex Gamma factor, up to the same constant on both sides; the duplication identity and this normalization are proved in Lesson 09, equation (12G) in Theorem 3.3. Put
\[
 F(s)=(N/M)^{s/2}\frac{L(s,f)}{L(s,\rho)}
     =(N/M)^{s/2}\prod_{p\mid NM}
       \frac{(1-b_pp^{-s})(1-c_pp^{-s})}{1-a_pp^{-s}},
\]
where good coincident factors cancel and zero roots do nothing. Dividing the two meromorphic functional equations gives \(F^\vee(1-s)=uF(s)\), with \(|u|=1\); the dual has the conjugate local parameters. Each zero or pole of a remaining factor \(1-\alpha p^{-s}\) lies on
\(\operatorname{Re}s=\log|\alpha|/\log p\le0\).
It forms an infinite arithmetic progression with imaginary period \(2\pi/\log p\). Cancel identical same-prime factors first. Progressions for distinct primes have at most one intersection: two intersections would make \(\log p/\log q\) rational and hence \(p^r=q^t\) for positive integers, contradicting unique prime factorization. A remaining zero or pole therefore survives at infinitely many points in the half-plane \(\operatorname{Re}s\le0\). Reflection of the dual factors has all its zeros and poles in \(\operatorname{Re}s\ge1\), so the functional equation prohibits any such remaining factor. Every prime factor is one. It follows that \(F(s)=(N/M)^{s/2}\). The reflected equality is then a constant times \((N/M)^{-s/2}=(N/M)^{s/2}\) for every \(s\); logarithmic differentiation gives \(N=M\). This proves all factor and conductor conclusions. ∎

The full Artin/Hecke functional equation needed in this deduction is the actual argument of Lesson 09, Lemma 3.2 and Theorem 3.3, using the local factors and induction compatibility proved in Lesson 06. The primitive weight-one Fricke functional equation and the bound \(|a_p|\le1\) remain separate modular-form proof obligations; Lemma 3.3 proves their consequence and does not silently assume that the currently weight-two newform proof covers them.

## 4. Finite projective images

Write \(D_n\) for the dihedral group of **order \(2n\)**, with \(n\geq2\). Thus \(D_2\) is the Klein four group and \(D_3\simeq S_3\).

**Lemma 4.0 (the finite-group counting facts used below).** The order of a subgroup divides the group order. If \(|G|=p^am\), with \(p\nmid m\), there is a subgroup of order \(p^a\), and every \(p\)-subgroup is contained in a conjugate of one. For a finite complex representation, the squared character norm is the dimension of its equivariant endomorphism algebra; a semisimple representation is irreducible exactly when that norm is one.

*Proof.* Cosets partition a finite group into equal sets of size the subgroup order, proving the first assertion. Let \(G\) act by left translation on its subsets of size \(p^a\). The number of these subsets is not divisible by \(p\): the coefficient of \(X^{p^a}\) in \((1+X)^{p^am}\) is congruent modulo \(p\) to the coefficient in \((1+X^{p^a})^m\), namely \(m\). The stabilizer of any subset acts freely on its points by translation, so its order divides \(p^a\). If every stabilizer had order at most \(p^{a-1}\), every orbit size would be divisible by \(p\), contradicting the subset count. One stabilizer therefore has order \(p^a\). For any \(p\)-subgroup \(H\), its orbits on the \(m\) cosets of this subgroup have powers of \(p\) as sizes; the orbit-stabilizer identity follows by the same coset partition. Since \(p\nmid m\), some orbit is a point. Its stabilizer condition says exactly that \(H\) is contained in a conjugate. This gives the Sylow assertions needed here.

On \(\operatorname{End}(V)\), average the conjugation action as in (5). Its image is \(\operatorname{End}_G(V)\), and its trace, being the rank of an idempotent, is that dimension. The trace of conjugation by \(g\) is \(\chi(g)\chi(g^{-1})=|\chi(g)|^2\), after averaging a Hermitian metric to make the representation unitary. This proves the norm identity. On an irreducible complex module an equivariant endomorphism has an eigenvalue; its kernel after subtracting that eigenvalue is a nonzero stable space and hence the whole space, so the endomorphism is scalar. Conversely a proper invariant summand gives a nonscalar equivariant projection by (5). Thus norm one is precisely irreducibility. ∎

**Theorem 4.1 (finite subgroups of \(\operatorname{PGL}_2(\mathbf C)\)).** Every finite subgroup is isomorphic to a cyclic group, \(D_n\), \(A_4\), \(S_4\), or \(A_5\). The trivial group is included among the cyclic groups.

**Proof.** We first turn the group into a rotation group. The inverse image \(\widetilde G\) of \(G\) under \(\operatorname{SL}_2(\mathbf C)\to\operatorname{PGL}_2(\mathbf C)\) has exactly \(2|G|\) elements: every projective class has exactly two determinant-one representatives. Average a positive definite Hermitian form over \(\widetilde G\). After a change of basis \(\widetilde G\subset\operatorname{SU}_2\).

Conjugation by \(\operatorname{SU}_2\) acts on the three-dimensional real space of traceless Hermitian matrices, preserving the positive quadratic form \(\tfrac12\operatorname{tr}(H^2)\). Its kernel is \(\{\pm I\}\), since a matrix commuting with all Hermitian matrices is scalar. Its image is \(\operatorname{SO}_3\). For completeness, use the Pauli matrices
\[
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{17}
\]
They satisfy \(\sigma_j\sigma_k=\delta_{jk}I+i\sum_l\epsilon_{jkl}\sigma_l\). For a unit vector \(u\), conjugation by
\[
\cos(\theta/2)I-i\sin(\theta/2)(u\cdot\sigma)
\tag{18}
\]
gives rotation through \(\theta\) about \(u\), by direct multiplication. Every rotation has an axis and angle. Hence \(G\) is a finite subgroup of \(\operatorname{SO}_3\).

Assume \(h=|G|>1\). Every nonidentity rotation fixes exactly two points of the unit sphere. Let \(P\) be the finite set of points with nontrivial stabilizer. A stabilizer consists of rotations about one axis, hence is a finite subgroup of the circle group and is cyclic. Let its orders on the distinct \(G\)-orbits of \(P\) be \(n_1,\ldots,n_r\), each at least two. Count pairs \((g,x)\) with \(g\ne1\) and \(gx=x\):
\[
2(h-1)=\sum_{x\in P}(|G_x|-1)
=h\sum_{j=1}^r(1-1/n_j).
\tag{19}
\]
Thus \(r\leq3\), since the left-hand quotient is strictly less than \(2\). There cannot be only one orbit: its contribution is less than \(1\), whereas \(2-2/h\geq1\).

If \(r=2\), (19) gives \(1/n_1+1/n_2=2/h\). Each \(n_j\leq h\), so both equal \(h\). There are two globally fixed points, and \(G\) is cyclic about their common axis.

If \(r=3\), order \(n_1\leq n_2\leq n_3\). Equation (19) says \(\sum1/n_j>1\). Consequently \(n_1=2\); if \(n_2\geq4\) the sum is at most \(1\). The complete list is
\[
\begin{array}{c|c}
(n_1,n_2,n_3)&h\\ \hline
(2,2,n)&2n\\
(2,3,3)&12\\
(2,3,4)&24\\
(2,3,5)&60.
\end{array}
\tag{20}
\]
Here is the group identification in every case.

For \((2,2,n)\) with \(n>2\), the unique order-\(n\) pole orbit consists of the two endpoints of one axis: it has size \(2n/n=2\), and antipodes have the same stabilizer. The subgroup fixing both endpoints is the cyclic group \(C_n\), of index two. A rotation exchanging the endpoints is a half-turn about a perpendicular axis; it has order two and conjugates a rotation about the original axis to its inverse. Hence \(G=C_n\rtimes C_2=D_n\). If \(n=2\), the group has order four and every nonidentity element has order two, by the pole stabilizers. It is the Klein four group \(D_2\).

For \((2,3,3)\), one order-three pole orbit has four points. The action on these four points is faithful: a nonidentity rotation cannot fix all four, since it has only two fixed points. Thus \(G\) is an order-twelve subgroup of \(S_4\), necessarily \(A_4\). To justify the last assertion, any index-two subgroup is the kernel of a nontrivial map \(S_4\to C_2\). All transpositions are conjugate and generate \(S_4\); therefore they all map to the nonidentity element, and the map is the sign character.

For \((2,3,4)\), the six order-four poles give three axes, since the antipode of a pole has the same stabilizer and this pole orbit is unique. A quarter-turn about one axis must interchange the other two axis lines: if it fixed either distinct line, it would have a second real invariant line, impossible for a quarter-turn. Its square is a half-turn, so both other lines are perpendicular to the first. Applying this to all three axes shows they are mutually perpendicular. The group embeds into the orientation-preserving signed permutation matrices in an orthonormal basis along these axes. That group has \(3!\cdot4=24\) elements, so the embedding is onto.

These matrices permute the four lines through the body diagonals of a cube. The action is faithful. If an orthogonal matrix fixes all four such lines, its eigenvalue on each is \(1\) or \(-1\). Any two distinct body diagonal lines have nonzero inner product, forcing their signs to agree. They span \(\mathbf R^3\), so the matrix is \(I\) or \(-I\); determinant one excludes \(-I\). The group is therefore \(S_4\).

For \((2,3,5)\), there are fifteen order-two axes, ten order-three axes, and six order-five axes. Thus the nonidentity elements consist of fifteen involutions, twenty elements of order three, and twenty-four of order five. The involutions form one conjugacy class, since their pole orbit is transitive. A rotation of order three or five has centralizer equal to its cyclic axis stabilizer: a commuting rotation must preserve the oriented axis, and reversing it would invert the rotation. Its conjugacy class has size \(60/3=20\) or \(60/5=12\). The full class sizes are
\[
1,\quad15,\quad20,\quad12,\quad12.
\tag{21}
\]
A normal subgroup is a union of these classes containing the identity, and its order divides \(60\). The possible sizes of such unions are
\[
1,13,16,21,25,28,33,36,40,45,48,60.
\tag{22}
\]
Only \(1\) and \(60\) divide \(60\). Thus \(G\) is simple.

A Sylow two-subgroup has order four. There is no element of order four, so it is a Klein four group. The centralizer of an involution has order four, by its class size, and is the unique Sylow two-subgroup containing that involution. Each such subgroup contains three involutions; there are therefore five Sylow two-subgroups. Conjugation acts on this set of five. This action is nontrivial, since a trivial action would make each proper Sylow subgroup normal. Simplicity makes the action faithful. The resulting order-sixty subgroup of \(S_5\) has index two and is \(A_5\), by the transposition argument already given. This proves the list. ∎

All entries occur. Cyclic and dihedral groups are generated by rotations about one axis and, in the dihedral case, a perpendicular half-turn. The rotation groups of a regular tetrahedron, cube, and icosahedron give \(A_4,S_4,A_5\). One can check their orders by counting vertex images and vertex stabilizers: \(4\cdot3=12\), \(8\cdot3=24\), and \(12\cdot5=60\). For the last count, the vertices
\[
(0,\pm1,\pm\phi),\quad(\pm1,\pm\phi,0),\quad
(\pm\phi,0,\pm1),\qquad \phi=(1+\sqrt5)/2,
\tag{23}
\]
form the icosahedron. Cyclic coordinate permutations and even sign changes act transitively on its twelve vertices. For \(v=(0,1,\phi)\), the five vertices \(w\) with \(v\cdot w=\phi\) form a regular pentagon: their pairwise distances, computed from (23), are \(2\) and \(2\phi\), the side and diagonal lengths. The other five nonpolar vertices are their antipodes. Rotation through \(2\pi/5\) about the polar axis therefore preserves all twelve vertices. A rotation fixing \(v\) must permute that pentagon, so its stabilizer has exactly five elements. This verifies the count. The corresponding projective subgroups arise by the \(\operatorname{SU}_2/\{\pm1\}\) correspondence.

**Corollary 4.2.** A finite irreducible two-dimensional complex representation has projective image \(D_n,A_4,S_4\), or \(A_5\).

**Proof.** If the projective image were cyclic, choose a matrix lifting its generator. Every image matrix would be a scalar times a power of that matrix. Finite-order matrices are diagonalizable, so its eigenlines would be stable under the entire image. This contradicts irreducibility. Theorem 4.1 supplies the other possibilities. ∎

The converse assertion for odd irreducible representations with solvable projective image is also part of the mathematical scope: such a representation is modular of weight one. Its proof is not supplied by the rotation classification, and remains a separate required automorphic proof in §6. The \(A_5\) case is outside that solvable assertion. No paid source is used to reconstruct or cite it.

## 5. The level-23 example

The modular and arithmetic identities needed for the example are proved next.

**Lemma 5.0A (the two binary theta series).** Put
\(Q_0=x^2+xy+6y^2\), \(Q_1=2x^2+xy+3y^2\), and
\(\Theta_Q(z)=\sum_{(x,y)\in\mathbf Z^2}q^{Q(x,y)}\).
Both theta series belong to \(M_1(\Gamma_0(23),\chi_{-23})\), where \(\chi_{-23}(a)=(a/23)\). Their half-difference is a cusp form with leading coefficient one, and
\[
 \dim S_1(\Gamma_0(23),\chi_{-23})=1,\qquad
 \tfrac12(\Theta_{Q_0}-\Theta_{Q_1})=\eta(z)\eta(23z).
\]

*Proof.* The Gram matrices are
\[
 A_0=\begin{pmatrix}2&1\\1&12\end{pmatrix},\qquad
 A_1=\begin{pmatrix}4&1\\1&6\end{pmatrix},\qquad \det A_i=23.
\]
They are positive definite, so the series and all fixed derivatives converge locally normally by a positive Gaussian bound. Let \(L=\mathbf Z^2\) with its indicated Gram form, and put \(L^\vee=A^{-1}\mathbf Z^2\). The discriminant group has order 23. For \(A_0\), the class of \((-1,2)/23\) has quadratic value \(1/23\). For \(A_1\), the class of \((-1,4)/23\) has value \(2/23\); multiplying that generator by 14 changes its value to \(1/23\), since \(2\cdot14^2\equiv1\pmod{23}\). In either case label the cosets by \(r\in\mathbf F_{23}\), with quadratic value \(r^2/23\) and bilinear value \(2rs/23\). Write \(\Theta_r\) for the corresponding coset series, and \(e(t)=\exp(2\pi it)\).

Schwartz Poisson summation and its Gaussian transform are actually proved in *Theta functions and sums of squares*, Theorem 1.1, including the multivariable formula. The lattice change of variables with its covolume is proved in *Theta series of lattices*, §2, equation (2.1). Applying it to a translated positive Gaussian, then extending from the imaginary axis by the holomorphic identity theorem, gives
\[
 \Theta_r(z+1)=e(r^2/23)\Theta_r(z),\qquad
 (\Theta_r|_1 S)(z)=\frac{-i}{\sqrt{23}}
                  \sum_s e(-2rs/23)\Theta_s(z).
\]
For the second formula the rank-two Gaussian contributes \(-iz\), its covolume is \(\sqrt{23}\), and the coset translation contributes the displayed negative Fourier phase. These specify every sign.

Here are the finite Fourier calculations that turn these two formulas into the full level and character assertion. Let \(\chi\) be the quadratic character of \(\mathbf F_{23}^\times\). The sum
\(G(a)=\sum_r e(ar^2/23)\) satisfies \(G(a)=\chi(a)G(1)\) for \(a\ne0\), by counting the two square roots of a nonzero square. Also \(G(1)=\sum_x\chi(x)e(x/23)\). Its conjugate is \(-G(1)\), since \(\chi(-1)=-1\); expanding its absolute square and putting \(x=ty\) shows that its square is \(-23\). The sign is positive imaginary. For an elementary sign check, the quadratic residues are
\(1,2,3,4,6,8,9,12,13,16,18\). Hence
\[
 \operatorname{Im}G(1)=2\sum_{r=1}^{11}
                 \chi(r)\sin(2\pi r/23)>0.
\]
There are four negative terms, each of magnitude at most one. The seven positive terms at \(r=1,2,3,4,6,8,9\) are respectively greater than
\(0.25,0.49,0.68,0.82,0.99,0.76,0.59\); their sum exceeds four. These bounds follow from \(\sin u\ge u-u^3/6\) on \([0,\pi/2]\), reflection about \(\pi/2\), and \(\cos u\ge1-u^2/2\) for the term \(r=6\). The elementary bound \(3<\pi<22/7\) suffices: it follows, for example, from \(\pi=16\arctan(1/5)-4\arctan(1/239)\), checked by the tangent addition formula, and the alternating arctangent series with its first omitted term bound. Thus \(G(1)=i\sqrt{23}\).

On vectors indexed by \(\mathbf F_{23}\), assign to \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\operatorname{SL}_2(\mathbf F_{23})\) the operator
\[
 (R(\gamma)v)_r=
 \begin{cases}
 \chi(a)e(ab r^2/23)v_{ar},&c=0,\\[2pt]
 G(c)^{-1}\displaystyle\sum_s
       e\bigl((ar^2-2rs+ds^2)/(23c)\bigr)v_s,&c\ne0.
 \end{cases}
\]
Fractions in the exponents mean inverses in \(\mathbf F_{23}\), followed by their residue modulo 23. These operators multiply according to the matrices. To verify the nonzero-lower-left case, the coefficient in a composition is a sum
\(\sum_t e((At^2+Bt+C)/23)\).
If \(A\ne0\), completing the square gives
\(G(A)e((C-B^2/(4A))/23)\).
Here \(A=c_3/(c_1c_2)\), where \(c_3\) is the lower-left entry of the product, and
\(G(A)/(G(c_1)G(c_2))=1/G(c_3)\).
Substitution leaves exactly its displayed quadratic kernel. If \(A=0\), the finite geometric sum is 23 when \(B=0\) and zero otherwise; it gives the first-line permutation and phase for \(c_3=0\). If one of \(c_1,c_2\) is zero, its first-line permutation picks a single summand in that same kernel, and substitution of the product entries gives the second line; if both are zero, the first lines multiply directly. This proves the operator law in all cases. Its operators for \(S,T\) are exactly the two theta transformations above. Since Euclidean reduction proves that \(S,T\) generate \(\operatorname{SL}_2(\mathbf Z)\), the theta transformation for every integral matrix is its reduction under \(R\). For \(c\equiv0\pmod{23}\), the zero component consequently transforms by \(\chi(a)=\chi(d)\). This is the asserted weight-one character law.

The same vector formulas prove regularity at every cusp: each slash translate is a finite linear combination of the coset series, all with nonnegative exponents in \(q^{1/23}\). In particular no unproved general theta-modularity theorem is needed. The Gauss sum also identifies the character name: in \(\mathbf Q(\zeta_{23})\), its square is \(-23\) and \(\zeta_{23}\mapsto\zeta_{23}^a\) multiplies it by \(\chi(a)\). Thus it is precisely the character of \(\mathbf Q(\sqrt{-23})\), conventionally denoted \(\chi_{-23}\).

Put \(h=(\Theta_{Q_0}-\Theta_{Q_1})/2\). Its constant term vanishes and its first coefficient is one: \(Q_0\) represents one twice, whereas \(Q_1\) does not. At the other cusp use \(W=\left(\begin{smallmatrix}0&-1\\23&0\end{smallmatrix}\right)\), with the determinant-normalized weight-one slash. Poisson gives
\(\Theta_Q|_1W=-i\Theta_{23Q^\vee}\).
The dual forms are \(6x^2-xy+y^2\) and \(3x^2-xy+2y^2\), each isometric to its original form by exchanging coordinates and changing one sign. Hence \(h|_1W=-ih\), so it vanishes at zero as well.

There are exactly two cusps, of widths one and 23. Indeed left cosets of \(\Gamma_0(23)\) are the projective bottom rows in \(\mathbf P^1(\mathbf F_{23})\); right multiplication by \(T\) has one fixed row and one orbit of length 23. The integral reduction is onto because the upper and lower elementary matrices generate the finite special linear group and lift integrally. This also gives index 24. There are no elliptic stabilizers in the projective subgroup: an elliptic lift has trace zero or \(\pm1\), and its upper-triangular reduction would require \(-1\) or \(-3\) to be a square modulo 23. Neither 22 nor 20 is in the residue list above.

For a meromorphic even-weight form of trivial character on this subgroup, multiply its slash translates over the 24 cosets. The product has full level and weight 24 times its weight. At infinity, a cusp orbit of width \(w\) contributes exactly its cusp order: its \(w\) translates have leading exponents \(v/w\), so their product has exponent \(v\). Interior orders likewise add over the preimages; applying the actually proved full-level valence formula in *The valence formula and the ring of modular forms of level one*, Theorem 1.1, gives total divisor degree \(24k/12\) on this torsion-free projective curve. Apply this to \(h^2\), of weight two and trivial character. Its total degree is four, and its two cusp orders are each at least two. They must both be exactly two, with no interior zero. Therefore \(h\) has simple zeros at the two cusps and no zero on \(\mathfrak H\). Any other cusp form of the same weight and character divided by \(h\) is holomorphic on the compact curve, hence constant by the maximum principle. The cusp space has dimension one.

Finally the actual product formula \(\eta^{24}=\Delta\) is proved in that same earlier lesson, §4, Theorem 4.1, by logarithmic differentiation using \(E_2\). Thus
\[
 \frac{\Delta(z)\Delta(23z)}{h(z)^{24}}
\]
is a weight-zero function on \(X_0(23)\). The numerator has order 24 at each cusp, by the full-level transformation of \(\Delta\) and \(W\); the denominator has the same orders. Neither has an interior zero. This ratio is consequently a holomorphic nowhere-zero function on the compact curve and is constant. Its leading coefficient is one, so the constant is one. The holomorphic ratio \(\eta(z)\eta(23z)/h(z)\) on the connected half-plane has twenty-fourth power one; hence it is constant, and its leading coefficient again makes it one. This proves the eta identity. Preservation of the cusp space by the Hecke operators is proved by the double-coset cusp calculation in the earlier Hecke lesson, §2. Its one dimension therefore makes \(h\) an eigenform for every Hecke operator, including \(U_{23}\). ∎

**Lemma 5.0B (the ideal classes and their theta coefficients).** For \(K=\mathbf Q(\sqrt{-23})\), the class group is cyclic of order three. If \(\psi\) is either nontrivial character of it, then
\[
 \sum_{\mathfrak a\subset\mathcal O_K,\ \mathfrak a\ne0}
             \psi([\mathfrak a])q^{N\mathfrak a}
       =\tfrac12(\Theta_{Q_0}-\Theta_{Q_1}).
\]
In particular its Dirichlet series is \(L_K(s,\psi)\), with all ideal Euler factors included.

*Proof.* The quadratic integer-ring proof in *Algebraic integers and rings of integers*, Theorem 1.4, gives \(\mathcal O_K=\mathbf Z[\omega]\), \(\omega=(1+\sqrt{-23})/2\), with \(\omega^2-\omega+6=0\). Ideal invertibility and unique prime factorization are proved in *Discrete valuation rings and Dedekind domains*, Proposition 3.1 and Theorem 3.2; ideal norms and their principal-ideal identity are proved in *Norms of ideals, the ideal class group, and modules over Dedekind domains*, Proposition 4.1. We use those actual proofs, not a class-group assertion from a bibliography.

Here is the required small-ideal bound directly in this field. A fractional ideal \(I\) is a lattice in \(\mathbf C\), of covolume \(N(I)\sqrt{23}/2\), by taking the determinant of the basis \(1,\omega\) and the additive index. A disk of radius \(R/2\) with area greater than this covolume contains two different points congruent modulo \(I\): periodize its indicator on a fundamental parallelogram; its integral exceeds the parallelogram's area, so the integer-valued periodization exceeds one somewhere. Their difference is a nonzero \(\alpha\in I\) of magnitude less than \(R\). Choose
\(R^2>(2/\pi)\sqrt{23}\,N(I)\), arbitrarily close to that value. Then \((\alpha)I^{-1}\) is integral, represents the inverse class, and has norm less than four. Every class therefore has a representative of norm at most three. This is the imaginary-quadratic case of the actually written bound in *Finiteness of the class number*, Theorem 8.1, with the two-dimensional argument supplied here.

The primes two and three split, with ideals
\[
 P=(2,\omega),\quad\bar P=(2,\omega-1),\qquad
 Q=(3,\omega),\quad\bar Q=(3,\omega-1).
\]
Each has norm two or three, by the quotient map sending \(\omega\) to zero or one. We have \((2)=P\bar P\), \((3)=Q\bar Q\), and \((\omega)=PQ\), by membership and the norm six. Also \(N(\omega-2)=8\), and \(\omega-2\) lies in \(P\), but not \(\bar P\); unique prime factorization gives \((\omega-2)=P^3\). Consequently every possible class of an ideal of norm at most three is among \(1,[P],[P]^{-1}\), and \([P]^3=1\). The ideal \(P\) is nonprincipal: a generator would have norm two, whereas
\[
 N(a+b\omega)=a^2+ab+6b^2
            =(a+b/2)^2+23b^2/4
\]
cannot be two for integers \(a,b\). If \(b\ne0\) it is at least \(23/4\); if \(b=0\) it is a square. Thus these are three distinct classes. The same formula shows that the only units are \(\pm1\).

For an integral ideal \(A\) representing a class \(C\), an element \(0\ne\alpha\in A\) corresponds to the integral ideal \(J=(\alpha)A^{-1}\), of class \(C^{-1}\) and norm \(N\alpha/N(A)\). Conversely every integral ideal in that class has \(JA\) principal, with exactly two generators \(\alpha\), differing by the units \(\pm1\), and they lie in \(A\) because \(J\) is integral. Therefore
\[
 \Theta_A=1+2\sum_{[J]=C^{-1}}q^{NJ}.
\]
For \(A=\mathcal O_K\), its norm form is \(Q_0\). For the basis \(2,\omega\) of \(P\), its norm divided by two is \(Q_1\). Conjugating ideals exchanges the two nontrivial classes and preserves norms, so their two ideal series are equal. Since \(\psi(P)+\psi(P)^{-1}=-1\), weighting the three class series by \(\psi\) yields exactly the asserted half-difference. Unique prime factorization now gives its ideal Euler product. It converges absolutely for \(\operatorname{Re}s>1\): in a quadratic field, at a rational prime there are at most two prime factors, so the number of ideals of norm \(n\) is at most the divisor function of \(n\); its Dirichlet series is bounded by \(\zeta(\operatorname{Re}s)^2\). This also justifies grouping the series by norms. ∎

Let
\[
f(z)=\eta(z)\eta(23z)
=q\prod_{n\geq1}(1-q^n)(1-q^{23n}),\qquad
\varepsilon=\chi_{-23}.
\tag{24}
\]
The modular input is the identity
\[
f=\tfrac12(\Theta_{Q_0}-\Theta_{Q_1}),\quad
Q_0=x^2+xy+6y^2,\quad Q_1=2x^2+xy+3y^2,
\tag{25}
\]
and that this is a normalized Hecke eigenform in
\(S_1(\Gamma_0(23),\chi_{-23})\), both now proved in Lemma 5.0A. Lemma 5.0B proves the first equality below. We will prove the second, including every ramified factor, after identifying the cubic splitting field:
\[
L(s,f)=L_K(s,\psi)=\frac{\zeta_F(s)}{\zeta(s)},
\quad F=\mathbf Q(\alpha),\quad \alpha^3-\alpha-1=0.
\tag{26}
\]
No finite coefficient check is used to infer this global identity.

The form is primitive of exact level \(23\): the character \(\chi_{-23}\) has conductor \(23\), so it cannot come from the only smaller divisor level, \(1\). It therefore meets the hypotheses of the exact-level clause of Theorem 1.1. In this example the representation and its exact conductor are constructed directly below, so the example does not depend on completing the general residual construction.

The polynomial \(g(X)=X^3-X-1\) has no rational root: the only possible integral roots are \(1,-1\), and both give \(-1\). Its discriminant is
\[
-4(-1)^3-27(-1)^2=-23.
\tag{27}
\]
An irreducible cubic has transitive Galois group in \(S_3\). Its Vandermonde product is a square root of the discriminant and transforms by the sign character. Since \(-23\) is not a rational square, the group is not \(A_3\), hence is \(S_3\). Let \(L\) be its splitting field.

The standard representation is the action on
\[
V=\{(x_1,x_2,x_3)\in\mathbf C^3:x_1+x_2+x_3=0\}.
\tag{28}
\]
The permutation representation splits as the constant line plus \(V\). Thus its character is the number of fixed roots minus one:
\[
\begin{array}{c|ccc}
\text{cycle type}&1&(12)&(123)\\ \hline
\operatorname{tr}_V&2&0&-1\\
\det_V&1&-1&1.
\end{array}
\tag{29}
\]
It is irreducible: its character norm is \((2^2+3\cdot0^2+2\cdot(-1)^2)/6=1\), using the finite-group character criterion proved by averaging. Alternatively, in the basis \(e_1-e_3,e_2-e_3\), generators act by
\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
R=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\quad S^2=R^3=I,\quad SRS=R^{-1}.
\tag{30}
\]
The two distinct eigenspaces of \(R\) are exchanged by \(S\), so no line is stable under both.

The determinant character cuts out \(K\), by the discriminant calculation, and equals \(\chi_{-23,G}\). Complex conjugation fixes the one real root and swaps the nonreal pair: a real cubic of negative discriminant has one real and two nonreal roots. Thus it acts by a transposition, and this representation is odd.

The polynomial discriminant is the fundamental discriminant \(-23\). The discriminant-index formula
\(\operatorname{disc}(\mathbf Z[\alpha])=[\mathcal O_F: \mathbf Z[\alpha]]^2\operatorname{disc}(F)\)
is proved in *Discriminants and integral bases*, Theorem 2.3, equation (3); its squarefree value forces index one. The splitting field is unramified outside \(23\). One can see the latter directly at any \(p\ne23\): the reduction is square-free, its simple roots lift in a finite unramified extension, and this extension contains the local splitting field.

At \(23\),
\[
g(X)\equiv(X-10)^2(X-3)\pmod{23}.
\tag{31}
\]
The simple root \(3\) lifts over \(\mathbf Q_{23}\), leaving a quadratic factor. The discriminant of that quadratic has valuation one: the cubic discriminant is \(-23\), and the resultant of the simple linear factor with the quadratic is a unit, so it contributes only a unit square. The quadratic splitting extension is ramified of degree two. Therefore the local decomposition and inertia groups in \(S_3\) are both generated by a transposition. This ramification is tame, since \(23\nmid2\). On \(V\), inertia has a one-dimensional invariant space. The conductor exponent and local polynomial are
\[
a_{23}(V)=2-\dim V^{I_{23}}=1,\qquad
P_{23}(T)=1-T.
\tag{32}
\]
Indeed, the quotient of the decomposition group by inertia is trivial; the induced Frobenius action on that invariant line is the identity. The tame conductor formula is the specialization of (4) in Lesson 05, §2, with its tame-group proof in Lemma 1.2. Thus the Artin conductor is exactly \(23\).

The class-field identification used here has an actual earlier proof: *Hilbert and ring class fields, and quadratic prime forms*, §1, Theorem 19.1, constructs the maximal everywhere-unramified abelian field, identifies its degree with the ordinary class number, and identifies the ideal class of every prime with its arithmetic Frobenius. Its proof uses the actually written ray-class construction in *Ray class fields, conductors and ideal reciprocity*, §1, equation (4), Propositions 18.1 and 18.3 and Theorem 18.4, and the number-field existence proof in *Global existence and the idèlic class field correspondence*, §1, Theorem 17.1.

Lemma 5.0B gives \(h(K)=3\). The subgroup \(A_3\) fixes \(K\), so \(L/K\) is cyclic of degree three. At 23 its inertia is the intersection of the already computed \(C_2\) with \(A_3\), which is trivial; away from 23 it was already unramified. There are no real places of \(K\). Therefore it is an everywhere-unramified abelian degree-three extension, and the inspected Theorem 19.1 identifies it with the Hilbert class field. Choose either nontrivial character \(\psi\) under its ideal-Artin identification. Restriction of (28) to \(A_3\) is the sum of the two nontrivial characters, and
\[
V\simeq\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}\psi.
\tag{34}
\]
Indeed in (30), the two eigenspaces of \(R\) are exchanged by \(S\). Giving these two coset slots the corresponding character actions is precisely the induced representation. Choosing the inverse character exchanges the slots and changes no representation or theta series.

Induction of Euler factors can be checked in these two slots. At a split rational prime the two one-dimensional factors are \((1-\psi(P)T)(1-\psi(\bar P)T)\); at an inert prime Frobenius exchanges the slots and has wrap-around \(\psi((p))=1\), giving \(1-T^2\). At 23 the ramified prime of \(K\) is principal, since \((\sqrt{-23})\) has norm 23; its ideal character is one. The inertia-invariant line computed in (32) consequently has factor \(1-T\), exactly its Hecke ideal factor. These calculations are the explicit two-slot case of the actually proved finite-place induction identity in *Artin and Hecke L-functions; conductors and induction*, Proposition 21.1. Together with Lemma 5.0B they prove equality of all Euler factors of \(L(s,f)\), \(L_K(s,\psi)\) and \(L(s,V)\). Finally the action on the three roots is the permutation representation \(\mathbf1\oplus V\). At any rational prime its inertia orbits are the residue-field slots of the cubic field; Frobenius rotates each orbit in its residue degree. The determinant of such a cyclic block is \(1-T^d\). Thus its Euler product is \(\zeta_F(s)\), including ramified factors, and division by the constant-line factor \(\zeta(s)\) proves the second equality of (26).

The reduced-form description agrees with the direct ideal calculation. The actual ideal–form correspondence and reduction proofs in *Quadratic fields: ideal classes and binary quadratic forms*, Theorems 10.1–10.2, give the representatives. Here \(a\le\sqrt{23/3}<3\), \(|b|\le a\le c\), and \(b^2-4ac=-23\). At \(a=1\) the convention at equality gives \((1,1,6)\); at \(a=2\) it gives \((2,1,3),(2,-1,3)\). They are exactly the three classes already proved in Lemma 5.0B.

For a good prime \(p\), the Frobenius permutation on the roots has cycle lengths equal to the degrees of the irreducible factors of \(g\bmod p\). This follows because an irreducible degree-\(d\) factor has its roots in a single Frobenius orbit of length \(d\). Equations (26) and (29), or the quotient of the permutation Euler factor by the trivial factor, now give
\[
a_p=\#\{x\in\mathbf F_p:g(x)=0\}-1,\quad
P_p(T)=
\begin{cases}
(1-T)^2,&g\text{ splits completely},\\
1-T^2,&g\text{ has degrees }1+2,\\
1+T+T^2,&g\text{ is irreducible}.
\end{cases}
\tag{33}
\]
For example \(a_2=a_3=-1\) and \(a_5=0\). The table in Exercise 7.3 checks every prime through \(50\). At \(23\), use (32), not the count of distinct roots of a repeated polynomial.

The representation (28) now supplies \(\rho_f\) directly, with all good traces proved by (26)–(33). Any other semisimple attached representation is isomorphic to it by the actual trace-uniqueness proof in Lesson 02. Its projective image is still \(S_3=D_3\): the standard representation is faithful, and no nonidentity element acts as a scalar, by the eigenvalues of a transposition and a three-cycle.

## 6. Proof scopes and required remaining work

The complete assertions of Theorem 1.1 and the solvable-projective-image converse in §4 remain required mathematics. They have not been weakened, and this edition does not certify the lesson as complete while their proofs are missing.

- **Higher-weight residual representations at arbitrary level and character.** Lemmas 3.0 and 3.0B–3.0D supply the cusp lattice, Eisenstein congruence, eigenpacket lift and finite-field descent. The actual higher-weight lesson proves the period injection, rational coefficient descent, and congruence-to-polynomial deduction under stated premises. It still lacks the full arithmetic modular models and descent, the supersingular compact correspondence, the nondegenerate primitive Fricke pairing for arbitrary nebentypus, and cuspidal irreducibility. Its Theorem 1.1 therefore cannot yet discharge the residual premise of Proposition 3.2. The required higher-weight primitive decomposition of a lifted good eigenpacket must also be covered in the supplied scope.
- **The noncuspidal weight-one classification.** Prove that every noncuspidal good eigenpacket has traces equal to the sum of two finite Dirichlet characters, with product \(\varepsilon\), and then construct that sum. The written character-Eisenstein construction in the earlier Hecke lesson assumes weight at least two. It is not a proof for weight one. This is needed for the entire scope \(M_1\) of Theorem 1.1 and for its converse direction on cuspidality.
- **Primitive exact conductor and all bad factors.** Lemma 3.3 proves the functional-equation rigidity deduction from the full Artin functional equation, the primitive weight-one Fricke equation and \(|a_p|\le1\) at bad primes. The last two modular inputs require their own all-level, all-character proof. The weight-two trivial-character newform argument does not supply them. The Mellin argument below proves entireness once the Fricke relation is available; it proves the concrete level-23 case directly.
- **Solvable-projective-image converse.** The odd irreducible finite representation with solvable projective image must be shown to come from a weight-one cusp form. The local rotation and induction calculations do not prove this automorphic assertion. Its proof remains required, independently of the direction treated in Theorem 1.1.
- **Transitive earlier proof and source chains.** Lemma 3.0 binds the actual higher-weight rational Fourier-basis proofs, whose group-cohomology, analytic compact-curve and period prerequisites must remain within the inspected earlier programme chain. In particular the written compact-curve Riemann–Roch proof, *Dimension formulas for congruence subgroups*, Appendix A, explicitly retains exact proof bindings for real integration and convergence, weak derivatives and Hilbert completion as outstanding. The local lattice argument inherits that remaining foundation requirement. Lemma 5.0B binds the actual ideal-factorization and norm proofs; §5 binds the actual Hilbert/ray-class and number-field existence arguments with their reciprocity prerequisites. An inspected local proof does not by itself certify that every provider has free mathematical origin or a currently public edition.

The new local proofs are substantive. Lemma 3.0A proves Rankin's weighted prime inequality for arbitrary cusp good eigenpackets without primitivity or normalization. Proposition 3.1 gives the finite coefficient set outside an arbitrarily small exception. Lemmas 3.0D–3.0F prove finite-field descent, a uniform image bound and characteristic-zero finite-group lifting. Proposition 3.2 proves the exact-polynomial recovery, removal of auxiliary ramification and cuspidal irreducibility once the genuinely needed residual premise is supplied. Lemma 4.0 and Theorem 4.1 prove the group-theoretic classification used here. Lemmas 5.0A–5.0B and the cubic calculations supply the full concrete theta/eta, ideal-class, finite representation, all-prime Euler factors and conductor calculation, using the stated actual earlier ideal and class-field proof bindings.

For completeness, the Mellin consequence has a direct proof in weight one. If a cusp form satisfies its primitive Fricke relation with the conjugate form, both \(f(iy)\) at infinity and its transformed expansion at zero decay exponentially, up to the indicated weight factor. Thus
\[
 N^{s/2}\int_0^\infty f(iy)y^{s-1}\,dy
   =N^{s/2}(2\pi)^{-s}\Gamma(s)L(s,f)
\]
is entire, by locally uniform domination of the integral and all its parameter derivatives at both ends. The invariant function \(y^{1/2}|f|\) is bounded: its cusp expansions decay on each of the finitely many cusp regions, and continuity bounds it on the compact remainder of a fundamental domain. Fourier coefficient extraction at height \(y=1/n\) consequently gives
\[
 |c_n|=\left|e^{2\pi ny}\int_0^1 f(x+iy)e^{-2\pi inx}\,dx\right|
       \le Ce^{2\pi}\sqrt n.
\]
This bound makes the sum of the absolute values of the termwise Mellin integrals finite for \(\operatorname{Re}s>3/2\), proving the initial identity there. Substitution \(y\mapsto1/(Ny)\) gives the completed reflection at \(1-s\) with the Fricke constant. Multiplication by the entire reciprocal Gamma function proves entireness of \(L(s,f)\). For the form in §5 the actually proved relation \(f|_1W_{23}=-if\) gives
\(f(i/(23y))=\sqrt{23}\,y f(iy)\), so its completed function reflects with constant one. In particular its irreducible Artin L-function is entire by the all-factor identity (26). The corresponding general consequence, after the remaining primitive inputs are proved, is entireness for these modular weight-one representations; it supplies no proof of entireness for every irreducible Artin representation.

## 7. Exercises with complete solutions

### Exercise 7.1 — Oddness (easy)

Let \(A=\rho_f(c)\). Prove that \(A\) is conjugate to \(\operatorname{diag}(1,-1)\), and explain why its trace alone would not establish the determinant identity on all of \(G_{\mathbf Q}\).

**Solution.** We have \(A^2=I\). Its minimal polynomial divides \(X^2-1\), so it is diagonalizable. Theorem 2.1 gives \(\det A=\varepsilon(-1)=-1\). Its eigenvalues must therefore be one \(1\) and one \(-1\), which gives the required conjugacy and trace zero. Information at the single element \(c\) cannot determine a character on the entire Galois group. The global identity follows from good-prime determinants and Frobenius classes in every finite quotient, as in the proof of Theorem 2.1. ∎

### Exercise 7.2 — The projective classification (medium)

Recover the list of finite subgroups of \(\operatorname{PGL}_2(\mathbf C)\) from the stabilizer orders of poles. Explain why cyclic projective image is excluded for an irreducible two-dimensional representation.

**Solution.** Lift the finite projective group to its finite double cover in \(\operatorname{SL}_2(\mathbf C)\), average a Hermitian form, and use the explicit \(\operatorname{SU}_2/\{\pm1\}\simeq\operatorname{SO}_3\) calculation (17)–(18). For a nontrivial group of order \(h\), double counting gives (19). There are two or three pole orbits.

Two orbits force both stabilizer orders to equal \(h\), giving a common rotation axis and a cyclic group. With three orbits the reciprocal inequality gives exactly \((2,2,n),(2,3,3),(2,3,4),(2,3,5)\). Formula (19) then gives orders \(2n,12,24,60\).

For the first type, the invariant axis and a reversing half-turn give \(D_n\); the order-four case is \(D_2\). For the second, the faithful action on four poles gives the index-two subgroup \(A_4\subset S_4\). For the third, the three mutually perpendicular order-four axes give all orientation-preserving signed permutation matrices, whose faithful action on four body diagonal lines gives \(S_4\). For the last, the conjugacy class sizes (21) make the group simple, by the complete union-size list (22). Its action on the five Klein-four Sylow two-subgroups embeds it as the index-two subgroup \(A_5\subset S_5\). These identifications, including faithfulness and the Sylow count, are proved in Theorem 4.1; thus the count gives actual groups and not just a list of numerical orders.

If the projective group is cyclic, every matrix in the original image is a scalar times a power of one finite-order generator. Its eigenlines are common invariant lines. Hence the representation is reducible. ∎

### Exercise 7.3 — Coefficients and cubic splitting (medium)

Compute \(a_p\) in (24) for every prime \(p\leq50\), and factor \(X^3-X-1\) modulo those primes. Include the ramified prime separately.

**Solution.** To compute a coefficient through degree \(50\), only factors \(1-q^n\) with \(n\leq49\) and \(1-q^{23n}\) with \(23n\leq49\) can affect the product after its leading \(q\). Starting with \(c_0=1\), multiplication by \(1-q^d\) replaces \(c_j\) by \(c_j-c_{j-d}\), in decreasing order of \(j\). Thus the following finite computation is exact, with \(a_p=c_{p-1}\). Independently one can enumerate \(Q_0,Q_1\) in (25); the coefficient is \((r(Q_0,p)-r(Q_1,p))/2\).

In the table, “irreducible” refers to the displayed cubic itself; coefficients in the factorization column are read modulo the indicated prime.

| \(p\) | \(a_p\) | \(\chi_{-23}(p)\) | Factorization of \(X^3-X-1\) |
|---:|---:|---:|---|
| 2 | −1 | 1 | \(X^3+X+1\), irreducible |
| 3 | −1 | 1 | \(X^3-X-1\), irreducible |
| 5 | 0 | −1 | \((X-2)(X^2+2X-2)\) |
| 7 | 0 | −1 | \((X+2)(X^2-2X+3)\) |
| 11 | 0 | −1 | \((X+5)(X^2-5X+2)\) |
| 13 | −1 | 1 | \(X^3-X-1\), irreducible |
| 17 | 0 | −1 | \((X-5)(X^2+5X+7)\) |
| 19 | 0 | −1 | \((X-6)(X^2+6X-3)\) |
| 23 | 1 | 0 | \((X-3)(X-10)^2\), ramified |
| 29 | −1 | 1 | \(X^3-X-1\), irreducible |
| 31 | −1 | 1 | \(X^3-X-1\), irreducible |
| 37 | 0 | −1 | \((X-13)(X^2+13X-17)\) |
| 41 | −1 | 1 | \(X^3-X-1\), irreducible |
| 43 | 0 | −1 | \((X-10)(X^2+10X+13)\) |
| 47 | −1 | 1 | \(X^3-X-1\), irreducible |

For the irreducible cubic rows, checking \(g(x)\ne0\) for all \(0\leq x<p\) proves irreducibility, since a reducible cubic over a field has a root. In each \(1+2\) row the quadratic discriminant is a nonsquare. They are respectively \(12, -8,17,-3,48,237,48\) modulo \(5,7,11,17,19,37,43\); these reduce to nonsquares \(2,6,6,14,10,15,5\). Multiplication verifies each factorization.

Thus the good-prime cubic rows are three-cycles and have trace \(-1\); the \(1+2\) rows are transpositions and have trace \(0\). There happens to be no completely split prime in this range. The three-cycle polynomial on \(V\) is \(X^2+X+1\), while a transposition has \(X^2-1\). At \(23\), the invariant line has Frobenius eigenvalue \(1\), so \(a_{23}=1\) and the factor is \(1-T\). This agrees with the product coefficient and (32). ∎

### Exercise 7.4 — Repairing the mean-square inference (hard)

Does a prime mean-square asymptotic
\[
\sum_{p\leq x}|b_p|^2\sim x/\log x
\tag{35}
\]
by itself force only finitely many values of \(b_p\)? Give a counterexample with \(b_p\in\mathbf Z\). Then state and prove the valid small-exception conclusion for integral coefficients in a fixed number field, under (10).

**Solution.** Enumerate primes \(p_1<p_2<\cdots\). Set \(b_{p_j}=1\) except at \(j=2^r\), where set \(b_{p_j}=r+1\), for \(r\geq0\). There are infinitely many distinct integer values. For \(M\geq1\),
\[
\sum_{j\leq M}|b_{p_j}|^2
=M+\sum_{2^r\leq M}\bigl((r+1)^2-1\bigr)
=M+O((\log M)^3)\sim M.
\tag{36}
\]
Taking \(M=\pi(x)\) and using the actually written prime number theorem, *The prime number theorem*, Theorem 3.1 with its proofs in §§1–3, gives (35). The exceptional indices have zero natural density; their increasingly large values do not change the mean-square main term.

For the valid conclusion, take \(a_p\in\mathcal O_K\) and impose (10) for **every** embedding. Define \(Y_B\) by (12). The bounded integer coefficients of the minimal polynomials prove \(Y_B\) finite, with no analytic input. For primes with \(a_p\notin Y_B\), at least one embedding contributes more than \(B^2\). Summing over embeddings yields (13), hence exceptional upper analytic density at most \(d/B^2\). Given \(\eta>0\), choose \(B^2\geq d/\eta\); this proves (11).

This statement allows infinitely many exceptional coefficient values. In Deligne–Serre's proof, the uniform residual-image bound and the infinitely many congruences in (15)–(16) supply the additional argument that turns a small-exception statement into a global finite set. Once Theorem 1.1 is constructed, finite image gives the finite set directly. ∎

## Freely readable primary materials

- P. Deligne and J.-P. Serre, *Formes modulaires de poids 1*, Annales scientifiques de l'ÉNS (4) **7** (1974), 507–530. Actually read: Proposition 2.7, Theorems 4.1 and 4.6, Lemma 4.9, Proposition 5.1 and §§6–8, including Lemmas 6.11 and 6.13 and the finite-image construction. The citation locates the full assertions; the local proofs and remaining obligations above determine what is actually established here. [Original article and PDF](https://www.numdam.org/item/ASENS_1974_4_7_4_507_0/).
- A. V. Sutherland, *18.785 Number Theory I*, Fall 2021, Lecture 17, Theorem 17.8 and Lemma 17.9, printed page 3: the actual Poisson and Gaussian proofs, read alongside the written multivariable programme proof used in Lemma 5.0A. [Original free lecture notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec17.pdf).
- J. S. Milne, *Algebraic Number Theory*, version 3.08, Chapter 3, Proposition 3.2 and Theorem 3.7 with its lemmas, and Chapter 4, Propositions 4.1–4.2 and 4.26–4.27 and the proof of Theorem 4.3: actual ideal, norm and lattice arguments read for the independent arithmetic exposition in Lemma 5.0B. [Author's free notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).

The actual earlier programme proofs are identified by their written titles and theorem locators where used. Their source-origin and current public-edition checks are recorded separately; a bibliography, public URL or source theorem statement never replaces a proof.

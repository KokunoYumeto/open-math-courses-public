# The different and the discriminant

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

The discriminant records the failure of an integral trace pairing to be perfect. The different records that failure at each prime of the larger field. Passing between them is an ideal norm. Keeping the different upstairs also makes its ramification exponents and its behavior in towers visible.

Let \(A\) be a Dedekind domain with fraction field \(K\), let \(L/K\) be finite separable, and let \(B\) be the integral closure of \(A\) in \(L\). The finite-integral-closure theorem from *Decomposition of primes in extensions* gives that \(B\) is finite over \(A\). For a finite separable tower \(K\subseteq L\subseteq M\), let \(C\) be the integral closure in \(M\), which is finite by the same theorem. All ideals in what follows are nonzero.

We use finite projective modules and fractional ideals from [*Norms of ideals, the ideal class group, and modules over Dedekind domains*](norms-class-groups-and-modules-over-dedekind-domains.md). From [*Decomposition of primes in extensions*](decomposition-of-primes-in-extensions.md), we use the factorization of extended ideals, the formula \(\sum ef=[L:K]\), and the separability criterion for the field trace pairing [Stacks, Tag 0BIL]. That lesson also supplies the norm of a prime ideal. No completion of a field is needed here.

## The trace dual

Define the **inverse different**, or complementary module, by
\[
J_{B/A}=\mathfrak D_{B/A}^{-1}
=\{x\in L:\operatorname{Tr}_{L/K}(xB)\subseteq A\}.
\tag{1}
\]
It is stable under multiplication by \(B\). The nondegenerate field trace pairing identifies it with an ordinary module dual:
\[
J_{B/A}\xrightarrow{\sim}\operatorname{Hom}_A(B,A),
\qquad x\longmapsto\bigl(b\longmapsto\operatorname{Tr}_{L/K}(xb)\bigr).
\tag{2}
\]
To justify surjectivity, extend an \(A\)-linear functional to \(L=B\otimes_A K\). The perfect trace pairing represents the extended \(K\)-linear functional uniquely by an element \(x\in L\); its integral values on \(B\) put \(x\) in (1).

Since \(B\) is finite projective over \(A\), the dual in (2) is finite and spans the dual \(K\)-vector space. Thus \(J_{B/A}\) is a nonzero fractional ideal of the Dedekind domain \(B\). Traces of integral elements belong to \(A\), so
\[
B\subseteq J_{B/A}.
\tag{3}
\]
The **different** is its ideal inverse:
\[
\mathfrak D_{B/A}=J_{B/A}^{-1}
=\{x\in L:xJ_{B/A}\subseteq B\}.
\tag{4}
\]
Inverting ideals is legitimate here because every nonzero fractional ideal of \(B\) is invertible. The definitions agree with [Stacks, Tag 0BW0].

**Proposition 14.1.** The different is an integral ideal of \(B\). For a multiplicative set \(S\subseteq A\setminus\{0\}\),
\[
\mathfrak D_{S^{-1}B/S^{-1}A}=S^{-1}\mathfrak D_{B/A}.
\tag{5}
\]
For a finite separable tower, it satisfies
\[
\mathfrak D_{C/A}
=\mathfrak D_{C/B}\,(\mathfrak D_{B/A}C).
\tag{6}
\]

**Proof.** Inclusion (3) implies that any \(x\) in (4) satisfies \(xB\subseteq B\), hence \(x\in B\). This proves integrality. Localization of the finite module dual (2) identifies the localized complementary module with the complementary module of the localized rings. Ideal inversion commutes with localization, proving (5).

For the tower, transitivity of field trace gives
\[
J_{C/A}=\{x\in M:\operatorname{Tr}_{M/L}(xC)\subseteq J_{B/A}\}.
\tag{7}
\]
Indeed, for \(x\in J_{C/A}\), \(c\in C\), and every \(b\in B\), the product \(bc\) lies in \(C\), so
\(\operatorname{Tr}_{L/K}(b\operatorname{Tr}_{M/L}(xc))\in A\).
That is precisely membership of the inner trace in \(J_{B/A}\). Conversely, such membership, tested with \(b=1\), gives \(x\in J_{C/A}\).

The right side of (7) is represented by \(\operatorname{Hom}_B(C,J_{B/A})\) through the trace pairing for \(M/L\). Locally at each prime of \(B\), the invertible ideal \(J_{B/A}\) has a generator \(t\). There the condition in (7) becomes
\(\operatorname{Tr}_{M/L}((x/t)C)\subseteq B\), so its solution module is \(tJ_{C/B}\). The Hom identification permits this localization because \(C\) is finite projective over \(B\). Consequently, globally,
\[
J_{C/A}=J_{C/B}(J_{B/A}C).
\]
Invert these fractional ideals to obtain (6). \(\square\)

One should localize the base ring for trace arguments. The ring \(B\otimes_A A_{\mathfrak p}\) is finite over \(A_{\mathfrak p}\) and may have several maximal ideals. A single ring \(B_{\mathfrak P}\) need not be finite over \(A_{\mathfrak p}\); replacing the former by the latter inside a field trace argument needs justification. We retain the finite semilocal ring throughout.

## Euler's lemma and a power basis

Suppose \(B=A[\alpha]\), where \(\alpha\) has monic minimal polynomial
\[
f(X)=X^n+a_{n-1}X^{n-1}+\cdots+a_0.
\]
Write, in \(L[X]\),
\[
\frac{f(X)}{X-\alpha}=\sum_{i=0}^{n-1}b_iX^i.
\tag{8}
\]

**Euler's dual-basis lemma.** The trace dual of \(1,\alpha,\ldots,\alpha^{n-1}\) is
\[
\frac{b_0}{f'(\alpha)},\ldots,\frac{b_{n-1}}{f'(\alpha)}.
\tag{9}
\]

**Proof.** Let \(\alpha_1,\ldots,\alpha_n\) be the distinct roots of \(f\) in a splitting field. Lagrange interpolation, applied to \(X^j\) for \(0\leq j<n\), gives
\[
X^j=\sum_{t=1}^n
\frac{\alpha_t^j}{f'(\alpha_t)}\frac{f(X)}{X-\alpha_t}.
\tag{10}
\]
Both sides have degree at most \(n-1\), and their values agree at every \(\alpha_t\), which proves the identity. Taking the coefficient of \(X^i\) in (10) gives
\[
\operatorname{Tr}_{L/K}
\left(\alpha^j\frac{b_i}{f'(\alpha)}\right)=\delta_{ij}.
\tag{11}
\]
These are exactly the dual-basis equations. \(\square\)

**Proposition 14.2.** If the full integral closure is \(B=A[\alpha]\), then
\[
\mathfrak D_{B/A}=(f'(\alpha)).
\tag{12}
\]

**Proof.** Euler's lemma says that \(J_{B/A}\) has \(A\)-basis (9). Comparing coefficients in \((X-\alpha)\sum b_iX^i=f(X)\) gives
\[
b_{n-1}=1,\quad b_{n-2}=\alpha+a_{n-1},\quad
b_{n-3}=\alpha^2+a_{n-1}\alpha+a_{n-2},\quad\ldots.
\]
In the reversed order these elements differ from \(1,\alpha,\ldots,\alpha^{n-1}\) by a triangular matrix with diagonal entries one. They therefore form another \(A\)-basis of \(B\). Hence \(J_{B/A}=f'(\alpha)^{-1}B\), and inversion proves (12). Separability ensures \(f'(\alpha)\ne0\). \(\square\)

The hypothesis concerns the full ring \(B\). A power order of nontrivial index has its own trace dual; its polynomial derivative alone does not automatically compute the different of the larger ring of integers.

## Norm and discriminant

The **discriminant ideal** \(\mathfrak d_{B/A}\) is the ideal of \(A\) generated by
\[
\det\bigl(\operatorname{Tr}_{L/K}(x_ix_j)\bigr)_{1\leq i,j\leq n},
\qquad x_1,\ldots,x_n\in B.
\tag{13}
\]
Equivalently, at every nonzero prime \(\mathfrak p\) of \(A\), choose an \(A_{\mathfrak p}\)-basis of \(B\otimes_A A_{\mathfrak p}\) and use its trace determinant. Changes of local basis multiply it by a unit square. This local definition agrees with (13): every tuple has a basis change matrix over \(A_{\mathfrak p}\), and clearing the basis denominators by elements outside \(\mathfrak p\) gives a tuple in \(B\) with the same determinant ideal locally. No global integral basis is assumed.

For an ideal \(\mathfrak a=\prod_{\mathfrak P}\mathfrak P^{a_{\mathfrak P}}\) of \(B\), the relative ideal norm is
\[
N_{L/K}(\mathfrak a)=
\prod_{\mathfrak p}\mathfrak p^{\sum_{\mathfrak P\mid\mathfrak p}
f(\mathfrak P/\mathfrak p)a_{\mathfrak P}}.
\tag{14}
\]

**Theorem 14.3.** One has
\[
\mathfrak d_{B/A}=N_{L/K}(\mathfrak D_{B/A}).
\tag{15}
\]
For \(K\subseteq L\subseteq M\), with \(m=[M:L]\),
\[
\mathfrak d_{C/A}
=\mathfrak d_{B/A}^{\,m}\,
N_{L/K}(\mathfrak d_{C/B}).
\tag{16}
\]
For a number field over \(\mathbf Q\), (15) becomes
\[
|d_L|=N_{L/\mathbf Q}(\mathfrak D_L).
\tag{17}
\]

**Proof.** Localize \(A\) at \(\mathfrak p\), making it a DVR, and keep \(B\) finite semilocal over it. Choose a free integral basis and let \(G\) be its trace matrix. Under (2), inclusion \(B\subseteq J_{B/A}\) is represented by \(G\). Smith reduction over the DVR gives
\[
v_{\mathfrak p}(\det G)=
\operatorname{length}_A(J_{B/A}/B).
\tag{18}
\]
If \(\mathfrak D_{B/A}=\prod_{\mathfrak P\mid\mathfrak p}\mathfrak P^{d_{\mathfrak P}}\) in this semilocal ring, then
\(J_{B/A,\mathfrak P}=\mathfrak P^{-d_{\mathfrak P}}B_{\mathfrak P}\).
Its quotient by \(B_{\mathfrak P}\) has \(d_{\mathfrak P}\) composition factors, each the residue field \(\kappa(\mathfrak P)\). Their dimensions over \(\kappa(\mathfrak p)\) are \(f(\mathfrak P/\mathfrak p)\). Thus (18) equals
\[
\sum_{\mathfrak P\mid\mathfrak p}
f(\mathfrak P/\mathfrak p)d_{\mathfrak P},
\]
the exponent of the norm in (14). Equality at every \(\mathfrak p\) proves (15).

Apply ideal norms to (6), using norm transitivity and
\(N_{M/L}(\mathfrak D_{B/A}C)=\mathfrak D_{B/A}^{\,m}\).
Then (15) at each stage gives (16). For \(A=\mathbf Z\), the discriminant ideal is \((d_L)\); its positive norm is \(|d_L|\). This proves (17), including its absolute-value convention. \(\square\)

## Trace modulo a prime and the exact tame criterion

Write
\[
\mathfrak pB=\prod_{i=1}^g\mathfrak P_i^{e_i},
\qquad k=\kappa(\mathfrak p),\quad l_i=\kappa(\mathfrak P_i),
\qquad d_i=v_{\mathfrak P_i}(\mathfrak D_{B/A}).
\tag{19}
\]
A prime is **unramified** here if \(e_i=1\) and \(l_i/k\) is separable. It is **tame** if \(e_i\) is nonzero in \(k\) and \(l_i/k\) is separable. In residue characteristic \(\ell>0\), the former condition on the integer \(e_i\) means \(\ell\nmid e_i\). Number-field residue fields are finite and therefore always separable; there ramification means \(e_i>1\).

**Theorem 14.4 (Dedekind).** For every \(\mathfrak P_i\mid\mathfrak p\),
\[
d_i\geq e_i-1.
\tag{20}
\]
Equality holds exactly in the tame case. More precisely,
\[
d_i\geq e_i
\quad\Longleftrightarrow\quad
e_i=0\text{ in }k\ \text{or }l_i/k\text{ is inseparable}.
\tag{21}
\]
Consequently, \(\mathfrak P_i\) divides the different exactly when it is ramified in the above sense.

**Proof.** Localize \(A\) at \(\mathfrak p\); let \(\pi\) generate its maximal ideal. The finite torsion-free module \(B\) is now free over \(A\). Reduction of its multiplication matrices therefore reduces the field trace to the algebra trace on
\[
R=B/\pi B=\prod_{i=1}^g R_i,\qquad
R_i=B/\mathfrak P_i^{e_i}.
\tag{22}
\]
Each \(R_i\) has a filtration with quotients
\(\mathfrak P_i^j/\mathfrak P_i^{j+1}\), \(0\leq j<e_i\).
These are one-dimensional vector spaces over \(l_i\): localization identifies the quotient ring with that of the DVR \(B_{\mathfrak P_i}\), where a uniformizer gives a generator of each successive quotient. Multiplication by \(x\in R_i\) acts on every quotient by multiplication by its residue \(\bar x\in l_i\). Taking a basis adapted to the filtration makes the matrix block triangular, so
\[
\operatorname{Tr}_{R_i/k}(x)
=e_i\operatorname{Tr}_{l_i/k}(\bar x).
\tag{23}
\]
In particular, the reduced trace pairing on this component is
\[
(x,y)\longmapsto e_i\operatorname{Tr}_{l_i/k}(\bar x\bar y).
\tag{24}
\]

If \(e_i\ne0\) in \(k\) and \(l_i/k\) is separable, its field trace pairing is perfect. The radical of (24) is then exactly
\(\mathfrak P_i/\mathfrak P_i^{e_i}\), the kernel of the residue map. If \(e_i=0\), the pairing is identically zero. The same holds if \(l_i/k\) is inseparable. Indeed, the field trace pairing is then degenerate; a nonzero element \(a\) in its radical satisfies \(\operatorname{Tr}_{l_i/k}(ay)=0\) for all \(y\). Since multiplication by \(a\) is a bijection of the field, the trace functional itself vanishes identically.

It remains to translate these radicals into different exponents. The radical of the trace pairing on all of \(R\) is
\[
\frac{B\cap\pi J_{B/A}}{\pi B}.
\tag{25}
\]
For \(x\in B\), its residue lies in that radical precisely when
\(\operatorname{Tr}_{L/K}(xB)\subseteq\pi A\), or equivalently \(x/\pi\in J_{B/A}\). This proves (25).

At \(\mathfrak P_i\), the fractional ideal \(\pi J_{B/A}\) has valuation \(e_i-d_i\). Its intersection with \(B\) has valuation
\[
\max(0,e_i-d_i).
\tag{26}
\]
In the tame case, (25) on \(R_i\) is \(\mathfrak P_i/\mathfrak P_i^{e_i}\), whose preimage has exponent one. Hence \(\max(0,e_i-d_i)=1\), giving \(d_i=e_i-1\). This includes \(e_i=1\), when the radical is zero. In either other case the radical is all of \(R_i\), whose preimage has exponent zero. Thus \(e_i-d_i\leq0\), or \(d_i\geq e_i\). These alternatives prove (20)–(21). Finally, \(d_i=0\) occurs exactly for \(e_i=1\) with separable residue extension, which proves the ramification assertion. \(\square\)

Together with (15), this recovers the discriminant ramification criterion. It also refines it:
\[
v_{\mathfrak p}(\mathfrak d_{B/A})
=\sum_i f_i d_i
\geq\sum_i f_i(e_i-1),
\tag{27}
\]
with equality exactly when all primes above \(\mathfrak p\) are tame.

## Computations

### Why residue separability matters

Let \(k=\mathbf F_\ell(u)\) with \(\ell\) prime and \(u\) transcendental, and take \(A=k[t]_{(t)}\). The polynomial \(X^\ell-u\) is irreducible over \(k\), since the \(u\)-valuation of an \(\ell\)-th power is divisible by \(\ell\). Hence the monic polynomial
\[
f(X)=X^\ell-tX-u
\]
is irreducible over \(K=\operatorname{Frac}(A)\): a monic factorization would have coefficients in the integrally closed ring \(A\) and would reduce to a factorization of \(X^\ell-u\). Let \(L=K(\alpha)\), \(f(\alpha)=0\), and \(B=A[\alpha]\). This field extension is separable because \(f'=-t\ne0\).

The finite ring \(B\) is local, with maximal ideal \(tB\), because \(B/tB=k(\sqrt[\ell]{u})\) is a field. It is a Noetherian domain of dimension one with principal maximal ideal, hence a DVR by the earlier characterization. Thus it is the full integral closure of \(A\) in \(L\). Here \(e=1\), but the residue extension is inseparable. Proposition 14.2 gives \(\mathfrak D_{B/A}=(t)\), of exponent one. This example explains why \(e=1\) alone does not imply unramifiedness over an imperfect residue field.

### Quadratic fields

Let \(d\ne1\) be squarefree, and put \(F=\mathbf Q(\sqrt d)\). Its integral basis was proved in *Discriminants and integral bases*. If \(d\equiv2,3\pmod4\), the generator is \(\sqrt d\), with polynomial \(X^2-d\). If \(d\equiv1\pmod4\), it is \(\omega=(1+\sqrt d)/2\), with polynomial \(X^2-X+(1-d)/4\). Proposition 14.2 gives
\[
\mathfrak D_F=
\begin{cases}
(2\sqrt d),&d\equiv2,3\pmod4,\\
(\sqrt d),&d\equiv1\pmod4.
\end{cases}
\tag{28}
\]
Their norms are \(4|d|\) and \(|d|\), respectively, matching the absolute discriminants.

For \(F=\mathbf Q(i)\), the different is \((2i)=(2)\). If \(\mathfrak P=(1+i)\), then \((2)=\mathfrak P^2\), so \(d_{\mathfrak P}=2>e-1=1\): this is wild ramification at \(2\).

For \(\mathbf Q(\sqrt{-3})\), the different is \((\sqrt{-3})\). Its norm is \(3\), and its valuation at the unique prime above \(3\) is one. The ramification index is two, so the exponent is the tame value \(e-1\).

### A prime cyclotomic field

For odd \(p\), the full ring is \(\mathbf Z[\zeta_p]\). Differentiate
\(\Phi_p(X)=(X^p-1)/(X-1)\) at \(\zeta=\zeta_p\):
\[
\Phi_p'(\zeta)=\frac{p\zeta^{p-1}}{\zeta-1}.
\]
The root \(\zeta\) is a unit, and \((p)=(1-\zeta)^{p-1}\). Therefore
\[
\mathfrak D_{\mathbf Q(\zeta_p)}
=(1-\zeta_p)^{p-2}.
\tag{29}
\]
The exponent is \(e-1\), because \(e=p-1\) is prime to the residue characteristic \(p\). Its norm is \(p^{p-2}\), the absolute discriminant already computed in *Cyclotomic fields*.

### A wild cubic prime

Let \(\alpha=\sqrt[3]{2}\) and \(F=\mathbf Q(\alpha)\). The earlier integral-basis calculation gives \(\mathcal O_F=\mathbf Z[\alpha]\). Hence
\[
\mathfrak D_F=(3\alpha^2).
\tag{30}
\]
Both \(2\) and \(3\) are totally ramified with residue degree one:
\[
\mathfrak P_2=(2,\alpha),\quad (2)=\mathfrak P_2^3;\qquad
\mathfrak P_3=(3,\alpha+1),\quad (3)=\mathfrak P_3^3.
\]
At \(\mathfrak P_2\), the equation \(\alpha^3=2\) gives \(v_{\mathfrak P_2}(\alpha)=1\), while \(3\) is a unit. At \(\mathfrak P_3\), \(\alpha\) has nonzero residue \(-1\), while \(v_{\mathfrak P_3}(3)=3\). Thus
\[
v_{\mathfrak P_2}(\mathfrak D_F)=2,\qquad
v_{\mathfrak P_3}(\mathfrak D_F)=3,\qquad
N(\mathfrak D_F)=2^2\,3^3=108.
\tag{31}
\]
The first prime is tame and the second wild. The signed discriminant is \(-108\); equation (17) concerns its absolute value.

### A tower with unit relative different

Take \(L=\mathbf Q(\sqrt3)\) and \(M=\mathbf Q(\zeta_{12})\). The full rings satisfy
\[
\mathcal O_L=\mathbf Z[\sqrt3],\qquad
\mathcal O_M=\mathcal O_L[\zeta_{12}].
\]
Indeed, \(\sqrt3=\zeta_{12}+\zeta_{12}^{-1}\) belongs to \(\mathbf Z[\zeta_{12}]\), and the full cyclotomic ring is that ring. Over \(L\), the root has polynomial
\[
f(X)=X^2-\sqrt3X+1.
\]
Since \(2\zeta_{12}-\sqrt3=i\), its derivative value is a unit in \(\mathcal O_M\). Thus \(\mathfrak D_{M/L}=(1)\), while \(\mathfrak D_L=(2\sqrt3)\). Equations (6) and (16) give
\[
\mathfrak D_M=(2\sqrt3)\mathcal O_M,\qquad
d_M=144=12^2.
\tag{32}
\]
The discriminants here are positive, so the ideal identity also verifies these displayed numerical values. The extension \(M/L\) is unramified at all finite primes; its real embeddings become complex, a phenomenon outside the finite-prime definition used in this lesson.

## Exercises and complete solutions

**Exercise 1.** Compute the differents of \(\mathbf Q(i)\) and \(\mathbf Q(\sqrt{-3})\), their norms, and their exponents at the ramified primes.

**Solution 1.** For \(i\), the minimal polynomial \(X^2+1\) has derivative \(2i\), so the different is \((2i)\), of norm \(4\). Since \((2)=(1+i)^2\), its ramified exponent is two. For \(\omega=(1+\sqrt{-3})/2\), the minimal polynomial \(X^2-X+1\) has derivative \(2\omega-1=\sqrt{-3}\). The different therefore has norm \(3\) and exponent one at \((\sqrt{-3})\). The corresponding ramification indices are both two; the first is wild and the second tame.

**Exercise 2.** Prove Euler's dual-basis lemma for a monogenic integral closure. Explain why its \(b_i\) span the entire power basis lattice.

**Solution 2.** Identity (10) follows by evaluation at all distinct roots. Its coefficient of \(X^i\) is (11), so (9) is the unique dual basis. The recursion from (8) gives
\[
b_{n-1-j}=\alpha^j+a_{n-1}\alpha^{j-1}+\cdots+a_{n-j}
\quad(0\leq j<n),
\]
with the sum absent when \(j=0\). Each has leading term \(\alpha^j\), so their reversed transition matrix is triangular with determinant one over \(A\). They span \(B=A[\alpha]\), not just a finite-index sublattice. Dividing by \(f'(\alpha)\) therefore gives \(J_{B/A}=f'(\alpha)^{-1}B\), proving the derivative formula.

**Exercise 3.** Compute the different exponents at \(2\) and \(3\) in \(\mathbf Q(\sqrt[3]{2})\), and check its absolute discriminant.

**Solution 3.** With \(\alpha^3=2\), use the full integral basis \(1,\alpha,\alpha^2\). Formula (30) gives the different. Its two valuations are exactly those in (31), namely two and three. No other primes divide \(3\alpha^2\), because its element norm has absolute value \(3^3\cdot2^2\). As a direct discriminant check, the trace matrix is
\[
\begin{pmatrix}3&0&0\\0&0&6\\0&6&0\end{pmatrix},
\]
whose determinant is \(-108\). Thus its absolute value equals the ideal norm in (31).

**Exercise 4.** Prove the full criterion (20)–(21) by reduction of the trace pairing, including the residue-inseparable alternative.

**Solution 4.** Work over \(A_{\mathfrak p}\), so the finite integral closure is free and its multiplication trace reduces correctly. The CRT components \(R_i\) in (22) have \(e_i\) filtration quotients isomorphic to \(l_i\). Trace additivity on a filtration gives (23). The radical of (24) is the maximal ideal of \(R_i\) in the separable, \(e_i\ne0\) case, and is the whole ring in either remaining case. For inseparability, a nonzero radical element of the field trace pairing, followed by its invertible multiplication map, proves that the field trace itself is zero. Formula (25) identifies this radical with the reduction of \(B\cap\pi J\). Its local exponent is \(\max(0,e_i-d_i)\): it equals one in the first case and zero in the second. These yield exactly \(d_i=e_i-1\) and \(d_i\geq e_i\). They exhaust all cases and prove both directions, using only localization, CRT, a finite filtration, and the integral trace dual.

## What this lesson does not prove

We import the previously proved Dedekind ideal, projective-module, norm, and prime-decomposition results, the integral bases used in the examples, and the field trace separability criterion [Stacks, Tag 0BIL]. All four numbered results about the different are proved here. Comparison with the Noether and Kähler differents belongs to the lesson on three differents in the Noether course. The ramification-group formula for wild exponents belongs to the local-field course; here wild ramification is identified by the exact threshold \(d_{\mathfrak P}\geq e_{\mathfrak P}\).

## References

- J. S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 3, “The primes that ramify,” Theorem 3.35, Lemmas 3.36–3.38 and Remark 3.39, printed pp.60–62.
- Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, 1923, Chapter V §§36–39, printed pp.131–154; trace dual and norm in Satz 101–103, the tower formula in Satz 111, and ramification in Satz 114–115.
- **[Stacks]** The Stacks project, [Tag 0BW0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-section-dedekind-different), the Dedekind complementary module and different; [Tag 0BWB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-section-formula-different), general formulas for the different; and [Tag 0BIL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-separable-trace-pairing), the field trace pairing.

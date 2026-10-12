# Projections in the reduced free group algebra

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

For the rank-two free group \(\Gamma=\mathbb F(a,b)\), the norm-closed algebra \(A=C_r^*(\Gamma)\) has only the projections \(0,1\). The mechanism is an integer trace: a projection can be moved into a dense algebra where its canonical trace is the trace of a trace-class difference of two projections. All eigenvalues of that difference except \(1,-1\) cancel in equal-multiplicity pairs.

The [complete free-word, arbitrary-index Hilbert-space and faithful-trace construction](free-group-norm-averaging.md#free-word-and-operator-inputs) supplies \(A\) and its trace \(\tau\); its norm-averaging theorem is not required here. The [complete analytic module](../components/free-group-projection-analytic-inputs.md) supplies compact spectral decomposition, the Banach trace ideal and its absolute diagonal trace, and general holomorphic contour calculus, including different representation units. We develop the integer mechanism first and then construct the representation difference and its domain.

Put \(H=\ell^2(\Gamma)\), let \(P\) project onto \(\mathbb C\delta_e\), and write \(p=1-P\). Inner products are linear in the second variable.

## 0. The integer-trace target

**Theorem 5.2.** Every projection \(e\in C_r^*(\mathbb F(a,b))\) has integer canonical trace. Consequently the only projections are \(0\) and \(1\).

**Proof.** Lemma 5.1 below gives a unitary \(u\in A\) and a projection \(q\in A_0\) with \(ueu^*=q\). Lemma 4.1 identifies \(\tau(q)\) with the trace of \(\pi(q)-\rho(q)\). Both terms are projections, and their difference is trace class by the definition of \(A_0\). Lemma 4.2 makes its trace an integer. Traciality gives \(\tau(e)=\tau(q)\), while positivity and normalization place \(\tau(e)\) in \([0,1]\). If the integer is zero, faithfulness gives \(e=0\); if it is one, faithfulness applied to \(1-e\) gives \(e=1\). The lemmas are proved in full below, and the analytic inputs in the linked module. \(\square\)

This statement concerns \(A\) itself. The projection \(\operatorname{diag}(1,0)\in M_2(A)\) is nontrivial, and its unnormalized matrix trace is \(1\) even though the matrix unit has trace \(2\). Passing to the von Neumann closure is another operation; the argument here makes no projection-absence assertion there.

## 1. Move a projection into the trace-class domain

<a id="5-bringing-every-projection-into-the-dense-algebra"></a>

The dense domain \(A_0=\{x:\pi(x)-\rho(x)\in\mathcal S_1(H)\}\) will be constructed in Section 4. Its polynomials, completeness and full holomorphic closure are proved there and in Section 5. They suffice for the following local spectral-gap construction.

**Lemma 5.1.** Every projection \(e\in A\) is unitarily conjugate within \(A\) to a projection \(q\in A_0\).

**Proof.** Approximate \(e=e^*\) by a group polynomial and average that polynomial with its adjoint. We obtain a self-adjoint polynomial \(h\in A_0\) with \(\delta=\|h-e\|<1/4\). For a real \(z\) whose distance to \(\{0,1\}\) exceeds \(\delta\), the continuous calculus of \(e\) and the Neumann perturbation formula make \(z-h\) invertible. The self-adjoint spectrum is real, so
\[
\operatorname{Sp}_A(h)\subset[-\delta,\delta]\cup[1-\delta,1+\delta].
\tag{18}
\]
Choose a function \(f\) equal to zero near the first cluster and one near the second. Its domain is the disjoint union of those neighborhoods, and it is holomorphic there. The complete Theorem 3.1 below gives \(q=f(h)\in A_0\). Agreement of holomorphic and continuous calculus in [PA4](../components/free-group-projection-analytic-inputs.md#pa-holomorphic-calculus) makes \(q=q^*=q^2\).

The circle \(|z-1|=1/2\) encloses just the second cluster. Choose the constant-one neighborhood to include this circle; a disjoint smaller neighborhood of the zero cluster still contains that cluster. PA3–4 prove the exact circle Riesz formula and its length \(\pi\). On the circle \(\|(z-e)^{-1}\|\leq2\), and the Neumann perturbation bound gives \(\|(z-h)^{-1}\|\leq(1/2-\delta)^{-1}\). The resolvent difference is
\((z-h)^{-1}(h-e)(z-e)^{-1}\).
Subtracting the two Riesz integrals and using the length bound consequently gives
\[
\|q-e\|\leq\frac{\delta}{1/2-\delta}<1.
\tag{19}
\]

Define \(v=qe+(1-q)(1-e)\). Expanding the products yields
\[
ve=qv,\qquad v^*v=vv^*=1-(e-q)^2=:d.
\]
The identity \((e-q)^2e=e(e-q)^2=e-eqe\), and its version with \(q\), show that \(d\) commutes with \(e,q\), and therefore with \(v\). Its spectrum is bounded below by \(1-\|e-q\|^2>0\), so the full continuous positive calculus gives \(d^{-1/2}\in A\). Thus
\[
u=v\bigl(1-(e-q)^2\bigr)^{-1/2}\in A
\tag{20}
\]
satisfies \(u^*u=uu^*=1\) and \(ue=qu\). It is a unitary with \(ueu^*=q\), as required. This constructs an actual nearby projection and an actual unitary, rather than treating norm density as continuity of the unbounded trace. \(\square\)

## 2. Why the projection difference has an integer trace

<a id="4-recovering-the-canonical-trace"></a>

**Lemma 4.2.** If \(E,F\) are projections on any Hilbert space and \(E-F\) is trace class, then
\[
\operatorname{Tr}(E-F)
=\dim(EH\cap\ker F)-\dim(FH\cap\ker E)\in\mathbb Z.
\tag{15}
\]

**Proof.** Set \(B=E-F\), \(C=E+F-1\). Expansion using \(E^2=E,F^2=F\) gives
\[
BC=-CB,\qquad B^2+C^2=1.
\tag{16}
\]
Since \(B\) is self-adjoint trace class, [PA1–2](../components/free-group-projection-analytic-inputs.md#pa-compact-spectral) supply its complete compact eigenspace decomposition and absolutely summable eigenvalues. The order inequalities \(-1\leq B\leq1\) put all those eigenvalues in \([-1,1]\).

For \(B\xi=t\xi\) with \(0<|t|<1\), anticommutation gives \(B(C\xi)=-tC\xi\). On that eigenspace \(C^2=(1-t^2)1\), so \(C/\sqrt{1-t^2}\) is an isometry onto the opposite eigenspace, with the same map as its inverse. These finite-dimensional eigenspaces therefore have equal dimensions. Their \(t,-t\) contributions cancel in the absolutely convergent trace sum.

For the endpoint \(t=1\), the equality
\(\langle\xi,B\xi\rangle=\|E\xi\|^2-\|F\xi\|^2=\|\xi\|^2\)
forces \(E\xi=\xi,F\xi=0\), and these conditions conversely give \(B\xi=\xi\). Hence this eigenspace is \(EH\cap\ker F\). Exchanging \(E,F\) identifies the \(-1\) eigenspace. Each endpoint has finite multiplicity by compactness; the zero eigenspace contributes zero, even if it has arbitrary dimension. Only the difference of the two endpoint dimensions remains, proving the displayed formula and its integrality. \(\square\)

<a id="paired-projection-spectrum"></a>

<svg xmlns="http://www.w3.org/2000/svg" width="780" height="350" viewBox="0 0 780 350" role="img" aria-labelledby="projection-pair-title projection-pair-desc" style="display:block;min-width:780px;background:#f8fafc">
<title id="projection-pair-title">The paired spectrum and the two finite endpoint defects</title>
<desc id="projection-pair-desc">For B equal to E minus F and C equal to E plus F minus one, eigenvalues t and minus t with zero less than t less than one have equal finite multiplicities through C divided by the square root of one minus t squared. Their absolute trace sum cancels. The eigenvalue plus one is E H intersect kernel F, and minus one is F H intersect kernel E. Both dimensions are finite. The trace is their dimension difference; the arbitrary-dimensional zero eigenspace contributes zero.</desc>
<defs><marker id="projection-pair-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#334155"/></marker></defs>
<g fill="#fff" stroke="#64748b" stroke-width="1.5"><rect x="24" y="42" width="232" height="82" rx="8"/><rect x="516" y="42" width="240" height="82" rx="8"/><rect x="24" y="198" width="330" height="80" rx="8"/><rect x="426" y="198" width="330" height="80" rx="8"/></g>
<g font-family="Arial,sans-serif" font-size="19" fill="#0f172a" text-anchor="middle"><text x="140" y="74">ker(B − t), 0 &lt; t &lt; 1</text><text x="140" y="105">finite dimension m</text><text x="636" y="74">ker(B + t)</text><text x="636" y="105">same dimension m</text><text x="189" y="230">ker(B − 1) = EH ∩ ker F</text><text x="189" y="258">finite dimension n₊</text><text x="591" y="230">ker(B + 1) = FH ∩ ker E</text><text x="591" y="258">finite dimension n₋</text><text x="390" y="158">mt + m(−t) = 0; all such pairs are absolutely summable.</text><text x="390" y="319">Tr(E − F) = n₊ − n₋ ∈ ℤ; ker B contributes 0.</text></g>
<path d="M266 82H505" stroke="#334155" stroke-width="2" marker-end="url(#projection-pair-arrow)"/>
<g font-family="Arial,sans-serif" font-size="16" fill="#0f172a" text-anchor="middle"><text x="390" y="52">C / √(1 − t²)</text><text x="390" y="115">onto isometry, its own inverse</text><text x="390" y="24">B = E − F; C = E + F − 1</text></g>
</svg>

The diagram depicts the exact finite-dimensional eigenspaces in Lemma 4.2, with their multiplicities left as variables. Trace-class absolute summation justifies cancellation of all the interior pairs.

**Lemma 4.1.** For every \(x\in A_0\),
\[
\operatorname{Tr}D(x)=\tau(x).
\tag{14}
\]

**Proof.** Every diagonal coefficient of the regular representation \(\pi\) equals \(\tau(x)\). For a polynomial this follows by checking whether left multiplication fixes a basis word; uniform polynomial approximation extends it to any \(x\in A\). Section 3's unitary realizes \(\rho\) on \(pH\) as two regular copies and maps regular basis vectors to the actual basis vectors of \(pH\). Each of its diagonals away from \(e\) is therefore also \(\tau(x)\), whereas its diagonal at \(e\) is zero because \(\rho\) is supported on \(p\).

Thus \(D(x)=\pi(x)-\rho(x)\) has diagonal zero away from \(e\), and diagonal \(\tau(x)\) at \(e\). For \(x\in A_0\), PA2's complete absolute diagonal formula applies to this actual trace-class operator and gives the assertion. The argument never approximates its trace by operator-norm approximants. In particular a projection \(q\in A_0\) satisfies
\[
\tau(q)=\operatorname{Tr}\bigl(\pi(q)-\rho(q)\bigr)\in\mathbb Z.
\tag{17}
\]
Here \(\rho(q)\) is an orthogonal projection on all of \(H\), with zero action on \(PH\); a representation need not have full unit in order to preserve a projection. \(\square\)

## 3. Construct the representation with one missing basis vector

<a id="1-removing-the-identity-from-the-regular-representation"></a>

On \(H'=pH\), use
\[
T_s\delta_g=\begin{cases}
\delta_s,&g=s^{-1},\\
\delta_{sg},&g\ne s^{-1},
\end{cases}\qquad s=a,b,\quad g\ne e.
\tag{1}
\]
Ordinary left multiplication loses the step \(s^{-1}\mapsto e\) and the predecessor \(e\mapsto s\) when \(e\) is removed. Joining them into \(s^{-1}\mapsto s\) makes a basis bijection. Its inverse joins \(s\mapsto s^{-1}\) instead, which is the same formula for \(s^{-1}\). The free universal property proved in the earlier word construction gives a unitary group representation \(\lambda'\) on \(H'\).

For \(c=a,b\), let \(\Gamma_c\) be the nonempty words whose final letter is \(c\) or \(c^{-1}\). The maps
\[
\phi_c(w)=\begin{cases}
w,&w\text{ ends in }c^{-1},\\
wc,&\text{otherwise}
\end{cases}
\tag{2}
\]
are bijections from \(\Gamma\) onto \(\Gamma_c\). The second line causes no cancellation. A word ending in \(c^{-1}\) is its own inverse image; from a word ending in \(c\), remove its last letter to recover the unique inverse image.

**Lemma 1.1.** The map
\[
U:H\oplus H\longrightarrow H',
\quad U(\delta_w,0)=\delta_{\phi_a(w)},
\quad U(0,\delta_w)=\delta_{\phi_b(w)}
\tag{3}
\]
is unitary and intertwines \(\lambda\oplus\lambda\) with \(\lambda'\).

**Proof.** The two terminal-letter sets partition the nonidentity words, so the displayed map is a basis bijection and extends to a unitary. It remains to check the action for each letter \(s=a^{\pm1},b^{\pm1}\):
\[
T_s\delta_{\phi_c(w)}=\delta_{\phi_c(sw)}.
\tag{4}
\]
If \(w\) has length at least two, left multiplication can remove at most its first letter and does not change its final letter. Appending \(c\), or leaving a terminal \(c^{-1}\) unchanged, therefore commutes with that step. For a one-letter word, the only change of terminal letter occurs at \(w=s^{-1}\). If \(c\) is not the underlying generator of \(s\), the appended \(c\) remains after the cancellation and equals \(\phi_c(e)\). If \(s=c\), the modified step sends \(c^{-1}\) to \(c=\phi_c(e)\). If \(s=c^{-1}\), the ordinary step sends \(c^2\) to \(c=\phi_c(e)\).

For \(w=e\), \(\phi_c(e)=c\). If \(s=c^{-1}\), the modified step sends \(c\) to \(c^{-1}=\phi_c(c^{-1})\). Every other letter gives the ordinary word \(sc=\phi_c(s)\). These cases exhaust the possible boundary cancellations and prove the formula. Composing the letter identities proves intertwining for every group word. \(\square\)

Thus \(\lambda'\) extends isometrically to the reduced norm, since a direct sum of two regular copies has precisely the original operator norm. Extend it by zero on \(PH\), obtaining a \*-homomorphism \(\rho:A\to B(H)\) with
\[
\rho(1)=p,\qquad \rho(x)P=P\rho(x)=0.
\tag{5}
\]
Let \(\pi(x)=x\) and
\[
D(x)=\pi(x)-\rho(x),\qquad D(1)=P.
\tag{6}
\]

## 4. A dense graph algebra with a complete trace norm

<a id="2-finite-differences-and-a-dense-algebra"></a>

For each generator or inverse letter, its two changed basis columns give
\[
D(\lambda_s)=\theta_{\delta_s,\delta_e}
 +\theta_{\delta_e-\delta_s,\delta_{s^{-1}}}.
\tag{7}
\]
It has rank two. Multiplicativity and adjoints give
\[
D(xy)=\pi(x)D(y)+D(x)\rho(y),\qquad D(x^*)=D(x)^*.
\tag{8}
\]
Finite induction on word length makes every \(D(\lambda_g)\) finite rank; for \(g\ne e\), its rank is at most \(2\ell(g)\). The identity is a separate rank-one difference. Put
\[
A_0=\{x\in A:D(x)\in\mathcal S_1(H)\}.
\tag{9}
\]
The complete PA2 construction supplies
\[
\|BTC\|_1\leq\|B\|\|T\|_1\|C\|,\qquad
|\operatorname{Tr}T|\leq\|T\|_1,\qquad
\operatorname{Tr}T=\sum_g\langle\delta_g,T\delta_g\rangle
\tag{10}
\]
with an absolutely convergent final sum.

**Lemma 2.1.** The set \(A_0\) is a norm-dense unital star subalgebra of \(A\). It is complete in the graph norm
\[
\|x\|_{\mathrm{gr}}=\|x\|+\|D(x)\|_1.
\tag{11}
\]

**Proof.** The product identity and the proved ideal bound place products in \(A_0\); the adjoint isometry places adjoints there. The unit belongs because \(P\) is trace class. Every group polynomial belongs by the finite-rank induction, giving operator-norm density. The product identity also gives
\[
\|D(xy)\|_1\leq\|x\|\|D(y)\|_1+\|D(x)\|_1\|y\|,
\]
so the graph norm is submultiplicative.

For a graph-norm Cauchy sequence, completeness of \(A\) gives \(x_n\to x\) in operator norm and PA2's Banach completeness gives \(D(x_n)\to T\) in trace norm. The bound \(\|D(z)\|\leq2\|z\|\) makes its operator-norm limit \(D(x)\); domination of operator norm by trace norm makes that same limit \(T\). Thus \(D(x)=T\in\mathcal S_1\), and convergence holds in the graph norm as well. \(\square\)

## 5. Preserve the whole holomorphic domain

<a id="3-holomorphic-closure-with-the-missing-unit-retained"></a>

**Theorem 3.1.** If \(x\in A_0\) and \(f\) is holomorphic on a neighborhood of \(\operatorname{Sp}_A(x)\), then \(f(x)\in A_0\).

**Proof.** PA3–4 construct surrounding cycles inside the given neighborhood and prove holomorphic calculus for every \(x\), with no normality assumption. Use
\[
R(z)=\pi((z1-x)^{-1}),\qquad R'(z)=\rho((z1-x)^{-1}).
\]
The latter belongs to the unital corner \(pB(H)p\), and has corner unit \(p\). The actual resolvent identities imply
\[
R(z)-R'(z)=R(z)P+R(z)D(x)R'(z).
\tag{12}
\]
To check the equality, the second term is \(R(z)p-R'(z)\), since \(R(z)\pi(x)=zR(z)-1\) and \(\rho(x)R'(z)=zR'(z)-p\). Adding \(R(z)P\) gives the required difference.

The first term has finite rank and the second is trace class by PA2. PA5 proves their trace-norm continuity and convergence of the contour Riemann sums in the complete trace ideal. Naturality of the calculus into each actual unital codomain gives
\[
D(f(x))=\frac1{2\pi i}\int_{\mathcal C}
 f(z)\bigl(R(z)P+R(z)D(x)R'(z)\bigr)\,dz
\tag{13}
\]
in \(\mathcal S_1(H)\). Hence \(f(x)\in A_0\). The full given holomorphic domain is retained, including disconnected domains. The derivation introduces no \(z^{-1}\), so a contour point at zero causes no problem when it is outside the spectrum. \(\square\)

## 6. Worked checks by mechanism

<a id="6-exercises-with-complete-solutions"></a>

The original exercise numbers retain the complete tasks. Their solutions are grouped by the part of the argument they test.

### Spectral pairing and the projection boundary

**Exercise 7.** Compute (15) for two rank-one projections whose ranges make an angle \(0<\theta<\pi/2\).

*Solution.* Choose unit vectors \(e_1\) and \(\cos\theta\,e_1+\sin\theta\,e_2\). On their two-dimensional span the projection difference has trace zero and determinant \(-\sin^2\theta\), so its eigenvalues are \(\pm\sin\theta\). There is no \(1\) or \(-1\) eigenspace. The generic pair cancels, giving trace zero. Adding an orthogonal one-dimensional summand to the range of the first projection adds one unmatched \(1\) eigenvalue and changes the trace to \(1\).

**Exercise 8.** Show that compactness, or even the Hilbert–Schmidt condition, cannot replace trace class in the trace calculation for projection differences.

*Solution.* Take the direct sum of the rank-one pairs from Exercise 7 with \(\sin\theta_n=1/n\), \(n\ge2\). The difference has eigenvalues \(\pm1/n\), so is compact and Hilbert–Schmidt because \(\sum_n2/n^2<\infty\). It is not trace class because \(\sum_n2/n=\infty\). The formal paired sum zero is not an absolutely convergent trace. Thus the trace in (15) would be undefined.

**Exercise 9.** With \(\|h-e\|=0.1\), estimate the projection error and explain why (20) stays inside \(A\).

*Solution.* Formula (19) gives \(\|q-e\|\le0.1/(0.5-0.1)=0.25\). Thus \(1-(e-q)^2\) is positive with spectrum in \([1-0.25^2,1]\), so its inverse square root is obtained by the continuous functional calculus in \(A\). Multiplying it by \(v\in A\) gives \(u\in A\). The algebraic identities in the proof make this operator a unitary that aligns the projections.

**Exercise 10.** Explain why the projection \(\operatorname{diag}(1,0)\) in \(M_2(A)\) does not contradict Theorem 5.2.

*Solution.* The theorem concerns projections in \(A\). In \(M_2(A)\), the indicated matrix is a nonzero projection different from the matrix identity. Its unnormalized matrix trace composed with \(\tau\) is \(1\), an integer, while its normalized trace is \(1/2\). Matrix amplification changes the unit's unnormalized trace from \(1\) to \(2\), so integrality no longer forces a projection to be \(0\) or the unit.

### Basis comparison and finite differences

**Exercise 1.** Check that the modified generator \(T_a\) is a permutation, including its exceptional inverse step.

*Solution.* Ordinary left multiplication sends \(a^{-1}\) to the omitted \(e\), and \(e\) to \(a\). After removing \(e\), replace these two steps by \(a^{-1}\mapsto a\); every other input and output retains its ordinary predecessor. Thus the map is bijective on nonidentity words. Its inverse sends \(a\mapsto a^{-1}\) and every other word \(g\) to \(a^{-1}g\). Both preserve the orthonormal basis, giving inverse unitaries.

**Exercise 2.** Compute \(\phi_a(e),\phi_a(a^{-1}),\phi_a(a),\phi_a(b)\), and explain how the two maps in (3) fill \(H'\).

*Solution.* These values are \(a,a^{-1},a^2,ba\). The image of \(\phi_a\) consists exactly of words ending in \(a^{\pm1}\); the analogous image of \(\phi_b\) consists of those ending in \(b^{\pm1}\). Every nonidentity reduced word ends in exactly one of these two kinds, and (2) has a unique inverse on each. Thus (3) is a basis bijection and not merely an embedding.

**Exercise 3.** Compute the rank, trace and trace norm of \(D(\lambda_a)\) on its finite-dimensional support.

*Solution.* Its only nonzero columns are the inputs \(\delta_e,\delta_{a^{-1}}\), with outputs \(\delta_a,\delta_e-\delta_a\). These are linearly independent, giving rank \(2\). Every diagonal entry is zero, so its trace is zero. The Gram matrix of these columns is
\[
\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.
\]
Its eigenvalues are \((3\pm\sqrt5)/2\), with sum \(3\) and product \(1\). The two singular values therefore have squared sum \(3\) and product \(1\), so their sum, the trace norm, is \(\sqrt5\).

**Exercise 4.** Why does finite rank for the generators imply finite rank for every group word, without summing an infinite Fourier series?

*Solution.* Formula (8) expresses the difference for a product of two words as bounded operators multiplying their two differences. Finite-rank operators form a two-sided ideal, so induction on the finite word length proves the claim. The same formula bounds the rank by the sum of the generator difference ranks, hence \(2\ell(g)\) for a nonempty reduced word. The identity has difference \(P\), of rank \(1\).

### Actual units and the trace topology

**Exercise 5.** Test (12) with \(x=1\). What error would omitting the term \(R(z)P\) cause?

*Solution.* For \(z\ne1\), \(R(z)=(z-1)^{-1}1\), \(R'(z)=(z-1)^{-1}p\), and their difference is \((z-1)^{-1}P\). Since \(D(1)=P\) and \(Pp=0\), the product \(R(z)D(1)R'(z)\) is zero. The first term in (12) gives the entire difference. Omitting it would incorrectly identify the different units of the two representations.

**Exercise 6.** Does operator-norm density of group polynomials prove (14) by continuity of \(\operatorname{Tr}\)?

*Solution.* No. The trace is continuous for trace norm, and operator-norm convergence does not control that norm. Rank-\(N\) projections divided by \(N\) have operator norm \(1/N\) but trace \(1\). The proof instead computes every diagonal of the actual trace-class difference \(D(x)\), and uses its absolute diagonal sum.

## Reading and attribution

Thomas Schick, [*The trace on the K-theory of group C\*-algebras*, arXiv:math/9907121v5](https://arxiv.org/pdf/math/9907121v5), the complete Lemma 2.6 proof on pp.7–8, Lemma 2.8 on pp.8–10 and Lemma 2.9 on pp.10–11, gives freely readable comparisons for the diagonal trace and different-unit resolvent method. Its trace-ideal facts and dense holomorphic K-theory equivalence are cited there by reference. The argument here uses the complete ordinary-Hilbert analytic module, the explicit two-copy basis unitary, spectral pairing and nearby-projection unitary instead of those imported premises. It does not assert the source's general Hilbert-module relative theorem or a K-theory computation.

All original conclusions retain their stated scope: the final projection-absence assertion is in the rank-two reduced algebra itself; the projection-difference trace formula allows arbitrary Hilbert spaces; holomorphic closure allows general elements and arbitrary given neighborhoods. The human paper retains its own distribution terms, and its text and PDF are not redistributed or assigned the programme's CC0 terms.

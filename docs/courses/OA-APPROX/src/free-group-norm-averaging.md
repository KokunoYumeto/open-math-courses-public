# Norm averaging in a free group algebra

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A finite operator average can erase the nonscalar part of an element of a reduced free-group algebra in operator norm. We begin with the operator algebra and the averaging target, derive simplicity and uniqueness of trace, and then construct the word and Hilbert-space mechanisms that make the target work. The word construction uses the same two selected generators for every finite test family, even when the full generator set is uncountable.

## 0. From words to a complete operator algebra

<a id="free-word-and-operator-inputs"></a>

Let \(I\) be any set with distinct members \(a,b\). Letters are pairs consisting of a generator and a sign; the inverse changes the sign. A reduced word is a finite string without an adjacent inverse pair. The empty word is denoted by \(e\).

Here is the normal-form proof. On the set of reduced words, define \(L_s\) for a letter \(s\) by deleting a leading \(s^{-1}\), if there is one, and otherwise prefixing \(s\). Its inverse is \(L_{s^{-1}}\). For a string \(s_1\cdots s_n\), the permutation \(L_{s_1}\cdots L_{s_n}\) is unchanged by deletion of an adjacent inverse pair. Repeated deletion terminates because length decreases by two. If it ends at a reduced word \(v\), the resulting permutation sends the empty word to \(v\). Thus every terminating deletion sequence has the same reduced result: two possible results would be the same value of the original permutation at the empty word.

Write \(R(u)\) for that unique result and define \(u\cdot v=R(uv)\) on reduced words. Deletion leaves the associated permutation unchanged, so
\[
L_{R(uv)}=L_uL_v,\qquad
L_{(u\cdot v)\cdot w}=L_uL_vL_w=L_{u\cdot(v\cdot w)}.
\]
Reduced words are detected by the value of their permutation at the empty word; the last equality proves associativity. The empty word is the unit, and reversal with inverse letters gives the inverse. Any assignment of the generators to another group extends by finite multiplication and inverse letters; deleting inverse pairs does not change its value. This proves the free universal property and constructs \(\Gamma=\mathbb F(I)\), including its unique reduced words and their length \(\ell\).

For any set \(X\), define \(\ell^2(X)\) by
\(\|\xi\|^2=\sup_{F\subset X,\ F\ {\rm finite}}\sum_{x\in F}|\xi_x|^2<\infty\).
Every such vector has countable support: for each positive integer \(n\), only finitely many coordinates have modulus at least \(1/n\). Finite coordinate truncations are dense, since a finite sum can be chosen arbitrarily close to the supremum. Finite Cauchy–Schwarz gives the absolutely convergent inner product
\(\langle\xi,\eta\rangle=\sum_x\overline{\xi_x}\eta_x\).
The space is complete. For a norm-Cauchy sequence each coordinate converges; for every finite set the squared norm of the coordinate limit difference is at most the limiting Cauchy bound. Taking the supremum proves that the limit belongs to \(\ell^2(X)\) and the sequence converges to it in norm. This proves the required arbitrary-index Hilbert space directly.

On this space coordinate restriction to a subset \(E\) is an orthogonal projection \(e_E\). Permutations of \(X\) give unitaries, because they preserve all finite sums and are onto. In particular
\[
\lambda_g\delta_h=\delta_{gh},\qquad
\lambda_g\lambda_h=\lambda_{gh},\qquad \lambda_g^*=\lambda_{g^{-1}}.
\]
Define
\[
A=C_r^*(\Gamma)=\overline{\operatorname{span}}\{\lambda_g:g\in\Gamma\}
 \subset B(\ell^2(\Gamma)).
\tag{1}
\]
The span is a unital \*-algebra. Its norm closure is complete and remains closed under multiplication and adjoints. The operator identity \(\|T^*T\|=\|T\|^2\) follows from \(\|T\xi\|^2=\langle\xi,T^*T\xi\rangle\) and the product norm inequality, so this is a concrete C\*-algebra. The existence of adjoints on an arbitrary Hilbert space and the complete positive calculus, including \(z^{1/2}\in A\) for \(z\in A_+\), are the full CF1–10 arguments. Completeness of \(B(H)\) itself follows by taking the pointwise vector limits of an operator-norm Cauchy sequence; its common norm bound makes that limit bounded and the Cauchy bound gives convergence in operator norm.

The vector functional \(\tau(x)=\langle\delta_e,x\delta_e\rangle\) is positive, unital and bounded by \(\|x\|\). It extracts the identity coefficient of a polynomial. Finite multiplication gives \(\tau(xy)=\tau(yx)\) on polynomials, and approximation in operator norm extends the equality to \(A\).

Right translations \(R_h\delta_g=\delta_{gh^{-1}}\) commute with every \(\lambda_g\), hence with all of \(A\). If \(z\geq0\) and \(\tau(z)=0\), then \(z^{1/2}\delta_e=0\). The square root lies in \(A\), so it commutes with all \(R_h\) and kills every basis vector. Their finite span is dense, giving \(z^{1/2}=0\) and \(z=0\). Thus the canonical trace is faithful at every generator cardinality.

## 1. The averaging target and its extension

<a id="3-simultaneous-norm-averaging"></a>

The symbols in the finite average are
\[
t=ab,\qquad r=ba.
\tag{8}
\]
\[
q_0=b^2ab^2.
\tag{13}
\]
One first moves an entire finite support into a word partition, and then separates its range by the powers of \(r\). The precise two mechanisms are proved in Sections 3 and 4.

**Theorem 3.1.** Let \(x\in\mathbb C[\Gamma]\) have zero identity coefficient. If \(m\) exceeds the length of every word in its support, then, for every \(N\ge1\),
\[
\left\|\frac1N\sum_{j=1}^N
\lambda_{r^jq_0t^m}\,x\,\lambda_{r^jq_0t^m}^*\right\|
\le\frac{2\|x\|}{\sqrt N}.
\tag{16}
\]

**Proof.** Define \(C\) to consist of the nonempty reduced words beginning with an \(a\)-block of either sign, or with a \(b\)-block of exponent exactly \(1\); put \(D=\Gamma\setminus C\), including \(e\). Section 3 proves that \(r^jD\) are mutually disjoint and that every transformed supporting word \(q_0t^mwt^{-m}q_0^{-1}\) sends \(C\) into \(D\).

Consequently, for \(y=\lambda_{q_0t^m}x\lambda_{q_0t^m}^*\), the whole operator \(y\) sends \(\ell^2(C)\) into \(\ell^2(D)\). If \(e_D\) is coordinate projection onto \(\ell^2(D)\), this says \((1-e_D)y(1-e_D)=0\). The projections onto \(\ell^2(r^jD)\) are orthogonal, so \(e_D\lambda_{r^i}^*\lambda_{r^j}e_D=0\) for \(i\ne j\). Section 4's full Hilbert-space estimate applies to \(y\) and those unitaries. Its bound is \(2\|y\|/\sqrt N=2\|x\|/\sqrt N\), and multiplying the two successive conjugators gives exactly the displayed family. The zero polynomial is included; it needs no nonempty support. \(\square\)

**Corollary 3.2.** For every \(x\in A\), \(\tau(x)1\) is in the operator-norm closure of the convex hull of \(\{\lambda_gx\lambda_g^*:g\in\Gamma\}\).

**Proof.** Let \(x_0=x-\tau(x)1\). For a tolerance choose a polynomial \(z\) close to \(x\) and remove its identity coefficient, \(z_0=z-\tau(z)1\). Contractivity of \(\tau\) gives \(\|x_0-z_0\|\leq2\|x-z\|\). Theorem 3.1 supplies a finite conjugation average \(T_N\) with small \(T_N(z_0)\). Each conjugation is isometric, so its convex average is contractive and fixes the unit. Hence
\[
\|T_N(x)-\tau(x)1\|
\leq2\|x-z\|+\frac{2\|z_0\|}{\sqrt N}.
\tag{17}
\]
Polynomial approximation makes the first term small; for that fixed polynomial, increasing \(N\) makes the second small. This is a genuine finite convex combination at each tolerance. For a finite family, the union of the polynomial supports is finite, so one common \(m\) and then one common \(N\) give all its required estimates. \(\square\)

## 2. What the operator-norm limit forces

<a id="4-simplicity-and-the-only-trace"></a>

**Theorem 4.1.** The reduced \(C^*\)-algebra of a free group with at least two generators is simple, and its canonical trace is its unique tracial state.

**Proof.** A tracial state \(\rho\) has \(\rho(uxu^*)=\rho(x)\) for every unitary \(u\), since its trace identity moves \(u^*\) to \(u\). It is continuous: positivity of \(\rho((s1+tx)^*(s1+tx))\) for all \(s,t\in\mathbb C\) gives \(|\rho(x)|^2\leq\rho(x^*x)\); the positive operator \(\|x\|^2 1-x^*x\) then gives \(|\rho(x)|\leq\|x\|\). Applying continuity to the finite averages in Corollary 3.2 proves \(\rho(x)=\tau(x)\) for every \(x\).

For simplicity let \(J\ne0\) be a norm-closed two-sided ideal. A nonzero \(y\in J\) gives \(0\ne y^*y\in J_+\), and faithfulness of \(\tau\) gives \(\tau(y^*y)>0\). Scale to an element \(z\in J_+\) with \(\tau(z)=1\). All group conjugates of \(z\), and their finite averages, belong to \(J\). Corollary 3.2 therefore supplies \(v\in J\) with \(\|1-v\|<1\). The series
\[
\sum_{n=0}^{\infty}(1-v)^n
\]
converges in the complete normed algebra \(A\). Multiplying its finite partial sum by \(v\), on either side, gives \(1-(1-v)^{N+1}\); this converges to \(1\). The series is consequently a two-sided inverse of \(v\). Thus \(1=v^{-1}v\in J\), forcing \(J=A\). \(\square\)

The rank-one endpoint gives a useful test of the hypotheses. For \(S\delta_k=\delta_{k+1}\) on \(\ell^2(\mathbb Z)\), the generated algebra is commutative. For \(|\zeta|=1\), the vectors
\((2N+1)^{-1/2}\sum_{k=-N}^{N}\zeta^{-k}\delta_k\)
have \(\|S\xi_N-\zeta\xi_N\|^2=2/(2N+1)\). Telescoping bounds the error for each integer power by \(|k|\|S\xi_N-\zeta\xi_N\|\), using unitarity also for negative powers. Every Laurent polynomial \(p\) therefore satisfies
\(\|p(S)\xi_N-p(\zeta)\xi_N\|\to0\), and hence \(|p(\zeta)|\leq\|p(S)\|\).
Evaluation extends continuously to the norm closure. It remains multiplicative and preserves adjoints by approximating products and adjoints by polynomials; its value at the unit is \(1\). It is positive because its value at \(d^*d\) is the squared modulus of its value at \(d\). These characters are tracial states. Evaluations at \(1\) and \(-1\) differ, and the former has a proper nonzero kernel containing \(S-1\). No Fourier transform or character-classification theorem is needed.

## 3. A finite cancellation engine

<a id="2-a-word-partition-with-separated-translates"></a>

Use the partition \(C,D\) defined in the averaging proof. We now verify its two roles by inspecting the terminal letters at each possible cancellation.

**Lemma 2.2.** If \(w\ne e\) and \(m>\ell(w)\), where \(\ell\) is reduced word length, then
\[
t^mwt^{-m}
\tag{10}
\]
is either a nonzero power of \(t\), or starts with \(a\) and ends with \(a^{-1}\).

**Proof.** Delete as many complete initial \(t^{-1}=b^{-1}a^{-1}\) pairs as possible, and then as many complete terminal \(t=ab\) pairs as possible. This gives
\[
w=t^{-p}v t^q,\qquad p,q\geq0,\qquad 2(p+q)\leq\ell(w).
\tag{11}
\]
The pairs removed from opposite ends never overlap. A nonempty remainder \(v\) begins with no \(b^{-1}a^{-1}\) pair and ends with no \(ab\) pair. If the remainder is empty, the original nonidentity word is \(t^{q-p}\) with \(q-p\ne0\), and conjugation by \(t^m\) fixes it.

For a nonempty remainder the conjugate is
\[
t^{m-p}v t^{-(m-q)},
\tag{12}
\]
with both outside exponents positive. The left boundary can delete one \(b\), but deleting the next \(a\) would require the excluded leading pair of \(v\). The right boundary can delete one \(b^{-1}\), but deleting the next \(a^{-1}\) would require the excluded terminal pair. If \(v\) is a single \(b\) or \(b^{-1}\), its deletion leaves respectively an adjacent \(b,a^{-1}\) or \(a,b^{-1}\), with no further cancellation. If both boundaries delete letters of a longer remainder, that remainder cannot disappear: disappearance would require the unreduced string \(b^{-1}b\). Thus the first \(a\) and final \(a^{-1}\) of the outside powers survive. The inequality \(m>\ell(w)\) ensures an outside pair remains at each end throughout. \(\square\)

**Lemma 2.1.** For every nonzero integer \(k\),
\[
r^kD\subset C.
\tag{9}
\]
In particular the subsets \(r^jD\), \(j\in\mathbb Z\), are pairwise disjoint.

**Proof.** A member of \(D\) has no initial \(a\)-letter of either sign. If it starts with a \(b\)-block, its exponent differs from \(1\). For \(k>0\), the final letter of \((ba)^k\) is \(a\); nothing cancels against the member of \(D\), and the product begins with the single \(b\)-block required for \(C\).

For \(k<0\), the prefix is \((a^{-1}b^{-1})^{-k}\). Its last \(b^{-1}\) either remains, joins a negative \(b\)-block, or removes one letter of a positive \(b\)-block of exponent at least \(2\). In each case an intervening letter remains before any further cancellation could reach the initial \(a^{-1}\). If the input is empty or starts with a different generator, there is no cancellation. Thus the product is in \(C\). An intersection of \(r^iD\) and \(r^jD\) with \(i\ne j\) would give \(r^{i-j}D\cap D\ne\varnothing\), contradicting what we have just proved. \(\square\)

**Lemma 2.3.** For every nonidentity word \(w\) and every \(m>\ell(w)\),
\[
\bigl(q_0t^mwt^{-m}q_0^{-1}\bigr)C\subset D.
\tag{14}
\]

**Proof.** Apply Lemma 2.2 to \(v=t^mwt^{-m}\). If it starts with \(a\) and ends with \(a^{-1}\), adjoining \(q_0=b^2ab^2\) on the left and \(q_0^{-1}=b^{-2}a^{-1}b^{-2}\) on the right creates no boundary cancellations. The result begins with \(b^2\) and ends with \(b^{-2}\).

If \(v=t^k\) with \(k>0\), the right boundary removes precisely one letter from its neighbouring \(b^{-2}\). An \(a\) then meets a \(b^{-1}\), so cancellation stops. If \(k<0\), the left boundary removes precisely one letter from its neighbouring \(b^2\); an \(a^{-1}\) then meets a \(b\), and cancellation again stops. In both cases the outermost initial \(b^2\) and final \(b^{-2}\) remain.

A word of \(C\) begins with an \(a\)-block or with exactly one \(b\) before another generator or the end. Multiplying it onto the final \(b^{-2}\) therefore removes at most one \(b^{-1}\), leaving a nonzero \(b\)-letter between the rest of the product and the input. The product still begins with a \(b\)-block of exponent \(2\), so lies in \(D\). \(\square\)

The outer \(b\)-blocks have a specific job; allowing a general word in their place loses it. For example, with a third generator \(c\), replacing \(b^2\) by \(bc\), and taking \(w=a,m=2\), gives
\[
(bc\,a\,bc)(ab)^2a(ab)^{-2}(bc\,a\,bc)^{-1}a.
\tag{15}
\]
Its initial \(b^1c\) survives. It lies in \(C\), although the final input \(a\) lies in \(C\) as well. Thus merely excluding the empty word and \(b\) from the substitute does not establish the required inclusion.

## 4. The Hilbert-space estimate behind the average

<a id="1-orthogonal-ranges-give-a-norm-estimate"></a>

**Lemma 1.1.** Let \(e\) be an orthogonal projection on a Hilbert space, and \(u_1,\ldots,u_N\) unitaries such that
\[
eu_i^*u_je=0\qquad(i\ne j).
\tag{2}
\]
If \((1-e)x(1-e)=0\), then
\[
\left\|\frac1N\sum_{j=1}^N u_jxu_j^*\right\|
\le\frac{2\|x\|}{\sqrt N}.
\tag{3}
\]

**Proof.** Write \(p_j=u_jeu_j^*\). The hypothesis gives \(p_ip_j=0\) when \(i\ne j\), so the ranges \(p_jH\) are orthogonal. Whenever \(ev=v\), let \(v_j=u_jvu_j^*\). For every vector \(\xi\), these range conditions give
\[
\left\|\sum_{j=1}^N v_j\xi\right\|^2
 =\sum_{j=1}^N\|v_j\xi\|^2
 \leq N\|v\|^2\|\xi\|^2.
\tag{4}
\]
Taking the supremum over unit vectors proves \(\|\sum_jv_j\|\leq\sqrt N\|v\|\). This directly proves the range estimate without replacing a norm inequality by equality.

The zero complementary compression means
\[
x=ex+(1-e)xe=v+w^*,\qquad v=ex,\qquad w=ex^*(1-e).
\tag{5}
\]
Both \(v\) and \(w\) satisfy the required range condition, and both norms are at most \(\|x\|\). Apply the range estimate to each. Taking adjoints preserves norm, so the triangle inequality bounds the conjugate sum of \(x\) by \(2\sqrt N\|x\|\), yielding the asserted average bound. Nothing assumes \(x=x^*\). \(\square\)

For operators \(v=ev\) and \(w=(1-e)w\), the perpendicular ranges give \(v^*w=0\), but only
\[
\|v+w\|^2=\|v^*v+w^*w\|\leq\|v\|^2+\|w\|^2.
\tag{6}
\]
Take \(e=\operatorname{diag}(1,0)\) on \(\mathbb C^2\), \(u_1=1\) and \(u_2\) the coordinate flip. With \(v=e\), the conjugate sum is the identity, whereas
\[
\|v+u_2vu_2^*\|^2=1,\qquad
\|v\|^2+\|u_2vu_2^*\|^2=2.
\tag{7}
\]
Thus orthogonality does not make the final scalar norm bound an equality.

<a id="averaging-partition-mechanism"></a>

<svg xmlns="http://www.w3.org/2000/svg" width="780" height="350" viewBox="0 0 780 350" role="img" aria-labelledby="fg-mechanism-title fg-mechanism-desc" style="display:block;min-width:780px;background:#f8fafc">
<title id="fg-mechanism-title">From a finite word support to a small operator average</title>
<desc id="fg-mechanism-desc">For all nonidentity words in the selected support, the conjugator g zero equals q zero t to the m moves C into D. Powers r to j give disjoint translates of D. Their Hilbert subspaces are orthogonal. Decomposing the operator into two range terms gives the two over square root N bound. The three boxes illustrate the first three of the N separated subspaces, without specifying their dimensions.</desc>
<defs><marker id="fg-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#334155"/></marker></defs>
<g fill="#fff" stroke="#64748b" stroke-width="1.5"><rect x="25" y="25" width="220" height="80" rx="8"/><rect x="425" y="25" width="330" height="80" rx="8"/><rect x="25" y="151" width="220" height="85" rx="8"/><rect x="425" y="151" width="94" height="85" rx="8"/><rect x="539" y="151" width="94" height="85" rx="8"/><rect x="653" y="151" width="102" height="85" rx="8"/></g>
<g font-family="Arial,sans-serif" font-size="18" fill="#0f172a" text-anchor="middle"><text x="135" y="58">finite support F ⊂ Γ ∖ {e}</text><text x="135" y="86">m &gt; max ℓ(w), w ∈ F</text><text x="590" y="58">(g₀wg₀⁻¹)C ⊂ D</text><text x="590" y="86">g₀ = q₀tᵐ; q₀ = b²ab²</text><text x="135" y="182">y = λ(g₀)xλ(g₀)*</text><text x="135" y="213">(1 − eD)y(1 − eD) = 0</text><text x="472" y="186">ℓ²(rD)</text><text x="586" y="186">ℓ²(r²D)</text><text x="704" y="186">ℓ²(r³D)</text><text x="586" y="217">⊥</text><text x="390" y="278">All N subspaces ℓ²(rʲD) are mutually orthogonal.</text><text x="390" y="319">Two range terms ⇒ ‖N⁻¹ Σⱼ λ(rʲ)yλ(rʲ)*‖ ≤ 2‖x‖ / √N</text></g>
<g stroke="#334155" stroke-width="2" marker-end="url(#fg-arrow)"><path d="M254 66H415"/><path d="M254 194H411"/></g>
<g font-family="Arial,sans-serif" font-size="16" fill="#0f172a" text-anchor="middle"><text x="334" y="48">finite cancellation</text><text x="334" y="178">separated ranges</text></g>
</svg>

The diagram records the two exact inputs of Theorem 3.1 and Lemma 1.1. The three displayed subspaces are schematic members of an arbitrary finite family; no finite dimension is asserted.

## 5. Worked checks by mechanism

<a id="5-exercises-with-complete-solutions"></a>

The original exercise numbers identify the same complete tasks. We group their solutions by the mechanism they test.

### Range bounds

**Exercise 1.** Give a norm-equality counterexample with orthogonal ranges satisfying (2).

*Solution.* Take the two projections onto the coordinate axes of \(\mathbb C^2\). Their ranges are orthogonal; their sum is the identity. Its squared norm is \(1\), while the sum of their squared norms is \(2\). They are the two conjugates of \(v=e\) under \(1\) and the coordinate flip, and \(eu_1^*u_2e=0\). This verifies (7) under the full hypotheses.

**Exercise 2.** Prove the coefficient \(N^{-1/2}\) in the estimate for \(v=ev\) cannot be replaced by \(N^{-1}\).

*Solution.* On a Hilbert space with orthonormal \(e_0,e_1,\ldots,e_N\), let \(e\) project onto \(e_1\) and \(v\xi=e_1\langle e_0,\xi\rangle\). Choose \(u_j\) fixing \(e_0\) and carrying \(e_1\) to \(e_j\). Their conjugates of \(v\) send \(e_0\) to the orthogonal unit vectors \(e_j\). Thus the sum has norm \(\sqrt N\), and its average has norm \(N^{-1/2}\). The projections \(u_jeu_j^*\) are orthogonal, so (2) holds.

### Consequences and the rank boundary

**Exercise 8.** Why does the simplicity proof need a positive element and a faithful trace?

*Solution.* A nonzero element can have trace zero, so rescaling it to trace \(1\) may be impossible. If \(y\ne0\) lies in the ideal, \(y^*y\) is a nonzero positive element in it. Faithfulness then ensures \(\tau(y^*y)>0\). Rescaling and norm averaging produce an invertible ideal element and force the ideal to contain \(1\).

**Exercise 9.** Give a finite-dimensional example showing that closeness to \(1\) in normalized trace \(2\)-norm does not imply invertibility.

*Solution.* In \(M_d\), let \(p\) project onto the first coordinate and set \(x=1-p\). It is singular, but \(\|x-1\|_2=\|p\|_2=d^{-1/2}\), tending to zero as \(d\) increases. Its operator-norm distance from \(1\) is \(1\), so it never satisfies the Neumann criterion.

**Exercise 10.** For the free group on one generator, show that the conclusion of Theorem 4.1 fails.

*Solution.* Let \(S=\lambda_1\) on \(\ell^2(\mathbb Z)\). The algebra generated by \(S\) is commutative. For \(\zeta\in\{1,-1\}\), the unit vectors \((2N+1)^{-1/2}\sum_{k=-N}^N\zeta^{-k}\delta_k\) satisfy \(\|S\xi_N-\zeta\xi_N\|\to0\). Their vector states on Laurent polynomials tend to \(p(S)\mapsto p(\zeta)\), giving bounded characters of the norm closure. The character at \(1\) has a proper kernel containing the nonzero element \(S-1\); the two characters are distinct tracial states. Commutativity also makes every conjugate of \(x\) equal to \(x\), preventing scalar averaging for a nonscalar element.

### Cancellation and finite-family uniformity

**Exercise 3.** Which part of the proof of (9) requires exclusion of an initial \(b\)-block of exponent \(1\)?

*Solution.* For negative \(k\), the terminal \(b^{-1}\) of \(r^k\) can cancel against an initial positive \(b\)-block. Exponent \(1\) would remove that block completely and could expose an \(a\)-letter which cancels further into the prefix. Excluding exponent \(1\) leaves a nonzero \(b\)-block, preserving the initial \(a^{-1}\). For example \(r^{-1}(ba)=e\notin C\); the input \(ba\) is in \(C\), not in \(D\).

**Exercise 4.** Apply the stripping construction (11) to \(w=(ab)^{-2}c(ab)\), where \(c\) is a third generator.

*Solution.* Here \(p=2,q=1,v=c\), and \(\ell(w)=7\). For \(m>7\), the conjugate is \((ab)^{m-2}c(ab)^{-(m-1)}\). No join cancels, so it starts with \(a\) and ends with \(a^{-1}\), as required.

**Exercise 5.** Explain why \(q_0\) contains \(b^2\) rather than \(b\), and test the weaker printed condition with \(d=bc\).

*Solution.* The initial \(b^2\) puts the result outside \(C\); the final \(b^{-2}\) leaves one \(b^{-1}\) after multiplying by an input whose initial block is \(b^1\). Replacing \(d\) by \(bc\) satisfies \(d\ne e,b\) but begins with exponent \(1\) of \(b\). With \(w=a,m=2\), the conjugated word and its product with \(a\in C\) retain that initial block, giving (15) in \(C\). Thus the weaker condition fails in rank three.

**Exercise 6.** For \(x=\lambda_a+2\lambda_b-\lambda_{ab}\), explain how a single averaging family controls the whole polynomial.

*Solution.* The identity coefficient is zero, and the largest support length is \(2\). Choose \(m=3\), \(q_0=b^2ab^2\), and the conjugators \(r^jq_0t^3\). Every transformed supporting word sends \(C\) into \(D\), so the compression of the whole transformed polynomial to \(\ell^2(C)\) is zero. Formula (16) gives \(2\|x\|/\sqrt N\), without replacing \(\|x\|\) by a sum of coefficient magnitudes.

**Exercise 7.** Does one averaging family work for several polynomials at once?

*Solution.* Yes. Choose \(m\) exceeding the lengths in the union of their finite supports after removing identity coefficients. The sets \(C,D\), the word \(q_0\) and the powers \(r^j\) then work for every polynomial. The bound for the \(i\)-th polynomial is \(2\|x_i-\tau(x_i)1\|/\sqrt N\). Approximating a finite set of arbitrary elements by polynomials and applying (17) gives simultaneous norm approximation as well.

## Reading and attribution

Pierre de la Harpe, [*On simplicity of reduced C\*-algebras of groups*, arXiv:math/0509450v1](https://arxiv.org/pdf/math/0509450v1), Definition 9, p.7, and the complete Theorem 14 proof, pp.10–11, supplies a freely readable comparison for Powers partitions and orthogonal-range averaging. That proof treats countable groups and obtains the free-group partition through earlier boundary-action results. Here the finite cancellation engine constructs the partition for every free generator set directly. The full operator-norm extension, unique-trace argument, rank-one characters and normal-form/operator foundations are proved locally. The inverse of an element \(v\) with \(\|1-v\|<1\) is the convergent series in \(1-v\).

The complete CF1–10 component linked in Section 0 supplies the Hilbert-space adjoint and C\*-calculus input at its exact retained version. Other factor-gap, group-boundary, classification and spectral Fourier theorems are not premises of this argument. The linked human paper retains its own distribution terms; its text and PDF are not redistributed or given the programme's CC0 grant.

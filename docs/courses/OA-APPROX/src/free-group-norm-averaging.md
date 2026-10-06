# Norm averaging in a free group algebra

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

The [free group factor gap](central-sequences-and-free-group-factors.md#5-an-explicit-free-group-gap) controls distance from the scalars in the trace \(2\)-norm. Here we prove a different statement in operator norm: finite averages of group conjugates can bring any element of the reduced group \(C^*\)-algebra arbitrarily close to its scalar trace. This proves simplicity and uniqueness of the tracial state.

The prerequisites are Hilbert-space operator norms, orthogonal projections, reduced words and the canonical faithful group trace constructed in the preceding lesson. The proof uses finite words and finite operator averages. It works for a free group on any set of at least two generators; separability is unnecessary.

Fix distinct generators \(a,b\), put \(\Gamma=\mathbb F(I)\), and let
\[
A=C_r^*(\Gamma)=\overline{\operatorname{span}}\{\lambda_g:g\in\Gamma\}
\subset B(\ell^2(\Gamma)).
\tag{1}
\]
The normalized faithful trace is \(\tau(x)=\langle\delta_e,x\delta_e\rangle\). The same proof of the trace using the commuting right regular representation works for an arbitrary indexing set \(I\); finite linear combinations of basis vectors remain dense.

## 1. Orthogonal ranges give a norm estimate

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

**Proof.** If \(v=ev\), the operator \(u_jvu_j^*\) has range in \(u_jeH\). These subspaces are mutually orthogonal by (2). Writing \(v_j=u_jvu_j^*\), we therefore have \(v_i^*v_j=0\) for \(i\ne j\), and
\[
\left\|\sum_jv_j\right\|^2
=\left\|\sum_jv_j^*v_j\right\|
\le\sum_j\|v_j^*v_j\|
=N\|v\|^2.
\tag{4}
\]
Now decompose
\[
x=ex+(1-e)xe=v+w^*,
\quad v=ex,\quad w=ex^*(1-e).
\tag{5}
\]
Both \(v,w\) have range in \(eH\), and both norms are at most \(\|x\|\). Apply (4) to each and use the triangle inequality, obtaining a bound \(2\sqrt N\|x\|\) before division by \(N\). \(\square\)

The equivalent orientation uses \(u_j^*xu_j\), with \(eu_iu_j^*e=0\). Replacing each \(u_j\) by its adjoint in (2)–(3) gives exactly that version.

More generally, if \(v=ev\) and \(w=(1-e)w\), then \(v^*w=0\) and
\[
\|v+w\|^2=\|v^*v+w^*w\|\le\|v\|^2+\|w\|^2.
\tag{6}
\]
Equality in the last inequality need not hold. For example, on \(\mathbb C^2\), let \(e=\operatorname{diag}(1,0)\), \(u_1=1\), \(u_2\) be the coordinate flip and \(v=e\). Condition (2) holds, but
\[
\|v+u_2vu_2^*\|^2=1,\qquad
\|v\|^2+\|u_2vu_2^*\|^2=2.
\tag{7}
\]
Thus an equality cannot be substituted for that intermediate norm inequality. The claimed estimate (3) remains valid.

## 2. A word partition with separated translates

Let \(C\) be the nonidentity reduced words whose initial block is a nonzero power of \(a\), or whose initial \(b\)-block is exactly \(b^1\). A word starting with a different generator is outside \(C\). Let \(D=\Gamma\setminus C\), including the identity, and set
\[
t=ab,\qquad r=ba.
\tag{8}
\]

**Lemma 2.1.** For every nonzero integer \(k\),
\[
r^kD\subset C.
\tag{9}
\]
In particular the subsets \(r^jD\), \(j\in\mathbb Z\), are pairwise disjoint.

**Proof.** A word in \(D\) starts with no \(a\)-letter, and its initial \(b\)-block, if present, has exponent different from \(1\). If \(k>0\), \(r^k=(ba)^k\) ends in \(a\), so concatenation with that word has no cancellation at the join. It starts with the \(b\)-block \(b^1\), hence lies in \(C\).

If \(k<0\), \(r^k=(a^{-1}b^{-1})^{-k}\). Its final \(b^{-1}\) cannot disappear completely against an initial \(b\)-block of exponent different from \(1\): if that exponent is positive, the remaining block has exponent one less; if it is negative, the blocks join. A word starting with another generator causes no cancellation. The initial \(a^{-1}\) therefore survives, so the result lies in \(C\). This includes the empty word. If two translates intersected, multiplying on the left by the inverse of one power would contradict \(r^kD\cap D=\varnothing\). \(\square\)

**Lemma 2.2.** If \(w\ne e\) and \(m>\ell(w)\), where \(\ell\) is reduced word length, then
\[
t^mwt^{-m}
\tag{10}
\]
is either a nonzero power of \(t\), or starts with \(a\) and ends with \(a^{-1}\).

**Proof.** Strip all possible initial blocks \(t^{-1}=b^{-1}a^{-1}\) and terminal blocks \(t=ab\) from the reduced word. Thus
\[
w=t^{-p}vt^q,\qquad p,q\ge0,\qquad 2(p+q)\le\ell(w),
\tag{11}
\]
where the remaining word \(v\) is empty, or has neither the indicated initial nor terminal block. If \(v\) is empty, \(w=t^{q-p}\), with nonzero exponent, and conjugation leaves it unchanged.

Otherwise (10) is
\[
t^{m-p}v\,t^{-(m-q)}.
\tag{12}
\]
Both powers have positive length. At the left join, at most the terminal \(b\) can cancel: cancellation of the following \(a\) would require \(v\) to start with \(b^{-1}a^{-1}\), which has been excluded. At the right join, at most the initial \(b^{-1}\) can cancel, because a further cancellation would require \(v\) to end with \(ab\). If \(v\) has length one and is \(b\) or \(b^{-1}\), one join removes it; the two surviving adjacent letters at the new join are \(b,a^{-1}\) or \(a,b^{-1}\), so they do not cancel. If both joins cancel for a longer word, they cannot remove all of \(v\), since a reduced word cannot consist of \(b^{-1}b\). The first \(a\) and final \(a^{-1}\) in (12) survive. \(\square\)

Put
\[
q_0=b^2ab^2.
\tag{13}
\]

**Lemma 2.3.** For every nonidentity word \(w\) and every \(m>\ell(w)\),
\[
\bigl(q_0t^mwt^{-m}q_0^{-1}\bigr)C\subset D.
\tag{14}
\]

**Proof.** Write \(v=t^mwt^{-m}\). If \(v\) starts with \(a\) and ends with \(a^{-1}\), neither join with \(q_0\) or \(q_0^{-1}\) cancels. Thus \(q_0vq_0^{-1}\) starts with \(b^2\) and ends with \(b^{-2}\). If \(v=t^k\), \(k>0\), its last \(b\) cancels one letter of the adjacent \(b^{-2}\), leaving a \(b^{-1}\); if \(k<0\), its first \(b^{-1}\) cancels one letter of the adjacent \(b^2\), leaving a \(b\). There are no further cancellations across that join. In both cases the outer initial \(b^2\) and terminal \(b^{-2}\) survive.

Multiplying this reduced word by a word in \(C\) either causes no cancellation at its terminal \(b^{-2}\), or cancels exactly one \(b^{-1}\), since the input's initial \(b\)-block is \(b^1\). The remaining terminal \(b^{-1}\) prevents any deeper cancellation. The product still starts with \(b^2\), which puts it in \(D\). \(\square\)

A more general choice is insufficient: it allows any \(d\in\langle b,c,\ldots\rangle\setminus\{e,b\}\) in place of \(b^2\) in \(q_0=d a d\). In rank at least three choose \(d=bc\), \(w=a\), \(m=2\), and an input word \(a\in C\). The product
\[
(bc\,a\,bc)(ab)^2a(ab)^{-2}(bc\,a\,bc)^{-1}a
\tag{15}
\]
still starts with the block \(b^1c\), so belongs to \(C\), contradicting the proposed inclusion. The fixed choice (13) works in every rank at least two.

## 3. Simultaneous norm averaging

**Theorem 3.1.** Let \(x\in\mathbb C[\Gamma]\) have zero identity coefficient. If \(m\) exceeds the length of every word in its support, then, for every \(N\ge1\),
\[
\left\|\frac1N\sum_{j=1}^N
\lambda_{r^jq_0t^m}\,x\,\lambda_{r^jq_0t^m}^*\right\|
\le\frac{2\|x\|}{\sqrt N}.
\tag{16}
\]

**Proof.** Let \(e_D\) be the projection onto \(\ell^2(D)\), so \(1-e_D\) projects onto \(\ell^2(C)\). Lemma 2.1 gives
\[
e_D\lambda_{r^i}^*\lambda_{r^j}e_D=0\qquad(i\ne j).
\]
Conjugate \(x\) by \(\lambda_{q_0t^m}\). Every supporting word then maps \(C\) into \(D\) by Lemma 2.3, so the whole conjugated operator \(y\) satisfies
\[
(1-e_D)y(1-e_D)=0.
\]
Apply Lemma 1.1 to \(y\) and \(u_j=\lambda_{r^j}\). Its norm is \(\|x\|\), and this gives (16). \(\square\)

The estimate is for the whole polynomial, rather than a separate estimate summed over its coefficients. One value of \(m\) works for its entire finite support.

**Corollary 3.2.** For every \(x\in A\), \(\tau(x)1\) is in the operator-norm closure of the convex hull of \(\{\lambda_gx\lambda_g^*:g\in\Gamma\}\).

**Proof.** Given \(\eta>0\), choose a polynomial \(z\) with \(\|z-x\|<\eta\), and put \(z_0=z-\tau(z)1\). Then
\[
\|z_0-(x-\tau(x)1)\|<2\eta.
\]
The average \(T_N\) from Theorem 3.1 is a unital contraction and fixes scalars. Consequently
\[
\|T_N(x)-\tau(x)1\|
<2\eta+\frac{2\|z_0\|}{\sqrt N}.
\tag{17}
\]
First choose \(\eta\) small, then \(N\) large. Each \(T_N(x)\) is an actual finite convex combination of the required conjugates. \(\square\)

## 4. Simplicity and the only trace

For the arbitrary generator set in this lesson, here is the full trace check on \(A\). On group polynomials \(x=\sum_g x_g\lambda_g\), \(y=\sum_g y_g\lambda_g\),
\[
\tau(xy)=\sum_g x_g y_{g^{-1}}=\sum_g y_g x_{g^{-1}}=\tau(yx).
\]
Both sums are finite. Norm approximation by polynomials and continuity of the vector state extend this identity to every \(x,y\in A\). For faithfulness, the right translations \(R_h\delta_g=\delta_{gh^{-1}}\) commute with all of \(A\). If \(z\in A_+\) and \(\tau(z)=0\), then \(z^{1/2}\delta_e=0\). Commutation gives \(z^{1/2}R_h\delta_e=0\) for every \(h\). These vectors include every basis vector and have dense linear span in \(\ell^2(\Gamma)\), so \(z^{1/2}=0\) and \(z=0\). The argument requires no countability of the basis.

**Theorem 4.1.** The reduced \(C^*\)-algebra of a free group with at least two generators is simple, and its canonical trace is its unique tracial state.

**Proof.** Every tracial state \(\rho\) is invariant under conjugation by the group unitaries. It has the same value on \(x\) and every convex average in Corollary 3.2, so continuity gives
\[
\rho(x)=\rho(\tau(x)1)=\tau(x).
\]

Let \(J\) be a nonzero closed two-sided ideal. Choose \(0\ne z\in J_+\); for example take \(z=y^*y\) for nonzero \(y\in J\). Faithfulness gives \(\tau(z)>0\). After rescaling, assume \(\tau(z)=1\). Corollary 3.2 provides an element \(v\in J\) with \(\|v-1\|<1\), because every conjugate of \(z\) remains in \(J\). The Neumann series makes \(v\) invertible in \(A\), hence \(1=v^{-1}v\in J\). Therefore \(J=A\). \(\square\)

The distinction between the two norms matters. A trace \(2\)-norm approximation to \(1\) need not produce an invertible element; the argument above uses operator norm.

## 5. Exercises with complete solutions

**Exercise 1.** Give a norm-equality counterexample with orthogonal ranges satisfying (2).

*Solution.* Take the two projections onto the coordinate axes of \(\mathbb C^2\). Their ranges are orthogonal; their sum is the identity. Its squared norm is \(1\), while the sum of their squared norms is \(2\). They are the two conjugates of \(v=e\) under \(1\) and the coordinate flip, and \(eu_1^*u_2e=0\). This verifies (7) under the full hypotheses.

**Exercise 2.** Prove the coefficient \(N^{-1/2}\) in the estimate for \(v=ev\) cannot be replaced by \(N^{-1}\).

*Solution.* On a Hilbert space with orthonormal \(e_0,e_1,\ldots,e_N\), let \(e\) project onto \(e_1\) and \(v\xi=e_1\langle e_0,\xi\rangle\). Choose \(u_j\) fixing \(e_0\) and carrying \(e_1\) to \(e_j\). Their conjugates of \(v\) send \(e_0\) to the orthogonal unit vectors \(e_j\). Thus the sum has norm \(\sqrt N\), and its average has norm \(N^{-1/2}\). The projections \(u_jeu_j^*\) are orthogonal, so (2) holds.

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

**Exercise 8.** Why does the simplicity proof need a positive element and a faithful trace?

*Solution.* A nonzero element can have trace zero, so rescaling it to trace \(1\) may be impossible. If \(y\ne0\) lies in the ideal, \(y^*y\) is a nonzero positive element in it. Faithfulness then ensures \(\tau(y^*y)>0\). Rescaling and norm averaging produce an invertible ideal element and force the ideal to contain \(1\).

**Exercise 9.** Give a finite-dimensional example showing that closeness to \(1\) in normalized trace \(2\)-norm does not imply invertibility.

*Solution.* In \(M_d\), let \(p\) project onto the first coordinate and set \(x=1-p\). It is singular, but \(\|x-1\|_2=\|p\|_2=d^{-1/2}\), tending to zero as \(d\) increases. Its operator-norm distance from \(1\) is \(1\), so it never satisfies the Neumann criterion.

**Exercise 10.** For the free group on one generator, show that the conclusion of Theorem 4.1 fails.

*Solution.* Let \(S=\lambda_1\) on \(\ell^2(\mathbb Z)\). The algebra generated by \(S\) is commutative. For \(\zeta\in\{1,-1\}\), the unit vectors \((2N+1)^{-1/2}\sum_{k=-N}^N\zeta^{-k}\delta_k\) satisfy \(\|S\xi_N-\zeta\xi_N\|\to0\). Their vector states on Laurent polynomials tend to \(p(S)\mapsto p(\zeta)\), giving bounded characters of the norm closure. The character at \(1\) has a proper kernel containing the nonzero element \(S-1\); the two characters are distinct tracial states. Commutativity also makes every conjugate of \(x\) equal to \(x\), preventing scalar averaging for a nonscalar element.

## Reading and attribution

Pierre de la Harpe, [*On simplicity of reduced C\*-algebras of groups*, arXiv:math/0509450v1](https://arxiv.org/pdf/math/0509450v1), Section 3, Definition 9 and full Theorem 14 proof, pp.7 and 10–11, supplies the Powers partition and orthogonal-range averaging method. The exact \(2/\sqrt N\) estimate and invertible-ideal step were actually read. Appendix IX, p.19, discusses scalar convex averaging by reference; the complete scalar averaging and unique-trace arguments are proved here.

Sections 1–4 give the complete finite-word construction, correct range inequality, fixed \(b^2ab^2\), simultaneous finite-support estimate and ideal proof. The local two-range decomposition works for non-self-adjoint inputs, and invertibility uses the Neumann series in \(1-v\). The argument applies to every free generator set of size at least two, with no countability hypothesis or reliance on a boundary-action theorem. Exact transitive Hilbert-space, group trace and C\*-algebra foundations remain pending; no source expression was imported.

# Fullness, hypercentrality and ultrafilter corners

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

The central sequence algebra is finite, but need not be a factor. We now relate its size and commutativity to ordinary sequences. The crucial result is stronger than a single nonzero commutator: if this algebra is noncommutative, every nonzero corner is noncommutative. This gives type \(\mathrm{II}_1\), with its center retained. For the hyperfinite factor we can go further and prove that the central sequence algebra is itself a factor.

Throughout Sections 1–4, \(M\) is a factor with separable predual. We use the preceding lesson's notation \(C_\omega,J_\omega,T_\omega,M_\omega,\pi_\omega,\tau_\omega\) and the symmetric faithful-state seminorm \(\|\cdot\|_{\varphi,\#}\). The [fullness theorem](central-sequences-and-free-group-factors.md#theorem-4-1) identifies closedness of \(\operatorname{Int}(M)\) with scalar-triviality of all bounded ordinary centralizing sequences. We also use finite von Neumann algebra type decomposition: a finite algebra has no type I part exactly when it has no nonzero abelian projection. Its general halving theorem applies without a separable-predual assumption on that finite algebra. These are selected projection-type inputs, with earlier prerequisites declared.

## 1. Ordinary and ultrafilter witnesses

Let \(C(M)\) consist of bounded sequences centralizing in the ordinary sense:
\[
\|[x_n,\psi]\|\longrightarrow0,\qquad \psi\in M_*.
\tag{1}
\]
Let \(T(M)\) consist of those sequences approaching bounded scalars strong*. Define their hypercentral subspace by
\[
H(M)=\{x\in C(M):[x_n,y_n]\longrightarrow0
\text{ strong* for every }y\in C(M)\}.
\tag{2}
\]
Use the same definition with ultralimits to obtain \(H_\omega(M)\). The inclusions are
\[
T(M)\subset H(M)\subset C(M),\qquad
T_\omega(M)\subset H_\omega(M)\subset C_\omega(M).
\tag{3}
\]

There are two distinct selection operations. An ordinary nonvanishing witness can be restricted to an increasing subsequence on which it remains uniformly nonvanishing. An ultrafilter witness can be converted to an ordinary witness by choosing indices satisfying successively larger finite collections of commutator tests.

**Lemma 1.1.** Let \((\psi_j)\) be norm dense in the normal state space.

If \(x\in C_\omega(M)\) and
\[
\lim_{n\to\omega}
\|x_n-\varphi(x_n)1\|_{\varphi,\#}^2=\delta>0,
\tag{4}
\]
there is an increasing sequence \(n(k)\) such that \(x_{n(k)}\) is ordinary centralizing and its squared scalar distance is at least \(\delta/2\). If \(x,y\in C_\omega(M)\) and their commutator has positive limiting squared seminorm, the same selection makes both subsequences ordinary centralizing with a uniformly nonvanishing commutator.

**Proof.** For (4), intersect the \(\omega\)-large scalar-distance set with the finitely many sets
\[
\|[x_n,\psi_j]\|<1/k,\qquad j\le k.
\tag{5}
\]
That intersection belongs to \(\omega\), hence is infinite. Choose \(n(k)>n(k-1)\) in it. For a pair include the corresponding tests for \(y_n\) and the commutator lower bound instead. Every fixed state commutator tends to zero on the selected subsequence. Uniform boundedness and norm density extend this to all normal functionals. \(\square\)

The scalar normalization in (4) detects triviality. If \(x_n-\lambda_n1\to0\) strong*, Cauchy–Schwarz gives \(\varphi(x_n)-\lambda_n\to0\); thus \(x_n-\varphi(x_n)1\to0\) strong*. The converse is immediate.

## 2. Fullness is independent of the ultrafilter

**Theorem 2.1.** The following are equivalent:

1. \(M\) is full.
2. \(C_\omega(M)=T_\omega(M)\) for some free ultrafilter.
3. \(C_\omega(M)=T_\omega(M)\) for every free ultrafilter.
4. \(M_\omega=\mathbb C\) for some free ultrafilter.
5. \(M_\omega=\mathbb C\) for every free ultrafilter.

**Proof.** The quotient characterization \(T_\omega=\pi_\omega^{-1}(\mathbb C)\) equates the corresponding sequence and algebra statements. If \(M\) is full but an ultrafilter sequence is not trivial, its quotient has positive distance from the scalar \(\tau_\omega(X)1\); equivalently (4) is positive. Lemma 1.1 gives an ordinary nontrivial centralizing sequence, contradicting the preceding fullness theorem.

Conversely, if \(M\) is not full, that theorem gives \(x\in C(M)\setminus T(M)\). Its faithful-state scalar distance has positive limsup. Select an ordinary subsequence along which the squared distance is at least a fixed \(\delta>0\). This subsequence remains centralizing and is nontrivial along every free ultrafilter. Hence none of its central sequence algebras is scalar. \(\square\)

This criterion retains the scalar-trivial space \(T_\omega\); fullness does not mean that every centralizing sequence converges to zero.

## 3. Hypercentrality is also independent of the ultrafilter

**Theorem 3.1.** The following are equivalent:

1. \(C(M)=H(M)\).
2. \(C_\omega(M)=H_\omega(M)\) for some free ultrafilter.
3. \(C_\omega(M)=H_\omega(M)\) for every free ultrafilter.
4. \(M_\omega\) is commutative for some free ultrafilter.
5. \(M_\omega\) is commutative for every free ultrafilter.

Furthermore,
\[
H_\omega(M)=\pi_\omega^{-1}(Z(M_\omega)).
\tag{6}
\]

**Proof.** The commutator of two centralizing sequences is centralizing, and its quotient is their quotient commutator. The zero ideal characterization gives (6) and the equivalence of the respective sequence and algebra conditions.

If two ultrafilter-centralizing sequences have a nonzero quotient commutator, its limiting squared faithful-state seminorm is positive. The pair version of Lemma 1.1 makes them ordinary centralizing sequences with a nonvanishing commutator. Thus ordinary universal hypercentrality implies every ultrafilter version.

If ordinary universal hypercentrality fails, choose a pair in \(C(M)\) whose commutator does not tend strong* to zero. Along a synchronous subsequence its squared seminorm is bounded below by a positive constant. The two restricted sequences remain ordinary centralizing, so their commutator survives every free ultrafilter. Thus no ultrafilter version can be commutative. \(\square\)

Being commutative is a weaker conclusion than being scalar. Theorem 2.1 and Theorem 3.1 deliberately keep these two tests separate.

## 4. Moving a commutator into every corner

**Theorem 4.1.** If \(M_\omega\) is noncommutative, it has no nonzero abelian projection. Consequently it is type \(\mathrm{II}_1\). The conclusion describes its type and does not assert trivial center.

**Proof.** Theorem 3.1 supplies bounded ordinary centralizing sequences \(x_k,y_k\) with
\[
\liminf_{k\to\infty}\|[x_k,y_k]\|_{\varphi,\#}^2>0.
\tag{7}
\]
Put \(c_k=[x_k,y_k]\) and
\[
\kappa=\lim_{k\to\omega}\|c_k\|_{\varphi,\#}^2
=\tau_\omega(c^*c)>0.
\tag{8}
\]
Both \(c^*c\) and \(cc^*\) have scalar ultraweak limit \(\kappa1\).

Fix a nonzero projection \(F\in M_\omega\). By exact projection lifting, choose \(f=(f_n)\in C_\omega(M)\) representing it. Let
\(\beta=\tau_\omega(F)>0\). Since \(\varphi(f_n)\to_\omega\beta\), the set where \(\varphi(f_n)\ge\beta/2\) belongs to \(\omega\). Replace \(f_n\) by \(1\) outside that set, preserving its representative and centralizing property. Thus we may assume the bound holds at every coordinate.

For each fixed \(n\), ordinary centrality gives
\([f_n,x_k]\to0\) and \([f_n,y_k]\to0\) strong*. Their differences are bounded strong*-null sequences, hence belong to the zero ideal along \(\omega\). Multiplication by a centralizing sequence preserves that ideal. Fixed multiplication by \(f_n\) also preserves strong* convergence. Expanding the commutator therefore gives, as \(k\to\omega\),
\[
[f_nx_kf_n,f_ny_kf_n]-f_nc_kf_n
\longrightarrow0\quad\text{strong*}.
\tag{9}
\]
Also \([f_n,c_k]\to0\) strong*, so compressing either side of \(c_k\) gives the same limit.
Consequently
\[
\begin{aligned}
\lim_{k\to\omega}
\varphi((f_nc_kf_n)^*(f_nc_kf_n))
&=\kappa\varphi(f_n),\\
\lim_{k\to\omega}
\varphi((f_nc_kf_n)(f_nc_kf_n)^*)
&=\kappa\varphi(f_n).
\end{aligned}
\tag{10}
\]
For example, the first expression differs by a vanishing scalar from
\(\varphi(f_nc_k^*c_kf_n)\), whose limit follows by pairing the scalar ultraweak limit of \(c_k^*c_k\) with the fixed normal functional \(a\mapsto\varphi(f_naf_n)\). This also explains why both halves of the symmetric seminorm are controlled.

For each \(n\), choose \(k(n)\ge n\) so large, within the relevant \(\omega\)-large finite-test sets, that
\[
\begin{aligned}
\|[x_{k(n)},\psi_j]\|+\|[y_{k(n)},\psi_j]\|
&<1/n&& (j\le n),\\
\|[f_nx_{k(n)}f_n,f_ny_{k(n)}f_n]\|_{\varphi,\#}^2
&\ge\kappa\beta/4.
\end{aligned}
\tag{11}
\]
The second choice is possible by (9)–(10), whose limit is at least \(\kappa\beta/2\). The first is possible because \(x_k,y_k\) are ordinary centralizing.

The reindexed sequences \(x_{k(n)},y_{k(n)}\) are ordinary centralizing by the first line of (11). Multiplying them on both sides by \(f_n\) gives centralizing sequences along \(\omega\). Their images lie in \(FM_\omega F\), and their commutator has positive quotient \(2\)-norm by the second line. Thus every nonzero corner is noncommutative.

A projection is abelian precisely when its corner is commutative. There are therefore no nonzero abelian projections. The finite type decomposition eliminates the type I part; the faithful normalized trace makes the remaining type type \(\mathrm{II}_1\). \(\square\)

By the general projection-halving input, such an algebra contains a unital two-by-two matrix unit system, even if its predual is nonseparable or its center is nontrivial. The [next lesson](strong-stability-and-tensor-absorption.md) uses the exact lifts of that system.

## 5. The center of the hyperfinite central sequence algebra

Let
\[
R=\overline{\bigotimes_{j\ge1}}(M_2,\operatorname{tr}_2),
\qquad D_r=\bigotimes_{j=1}^rM_2.
\tag{12}
\]
Its normalized trace is \(\tau\), and \(N_r=D_r'\cap R\) is the remaining tensor tail, itself a \(\mathrm{II}_1\) factor.
Let \(E_r\) be the compact-unitary average onto \(N_r\). For any bounded centralizing sequence \(a_n\),
\[
\|E_r(a_n)-a_n\|_{2,\tau}\longrightarrow0
\tag{13}
\]
ordinarily or along \(\omega\), as appropriate, for each fixed \(r\). Indeed, expand tail averaging using the finitely many matrix units of \(D_r\); its difference from the identity is a finite sum of fixed multiples of commutators. Centrality and bounded strong* convergence give (13).

**Lemma 5.1.** If \(N\) is a finite factor with faithful normalized trace and \(\tau(b)=0\), there is a unitary \(u\in N\) such that
\[
\|b-ubu^*\|_2\ge\frac12\|b\|_2.
\tag{14}
\]

**Proof.** Take the ultraweakly closed convex hull \(K\) of the bounded unitary orbit of \(b\). It is compact. The \(2\)-norm is ultraweakly lower semicontinuous: it is the supremum of its scalar pairings against bounded trace vectors of \(2\)-norm at most one. Thus \(K\) has a point of least \(2\)-norm. Strict Hilbert-space convexity and trace faithfulness make it unique. Unitary conjugation preserves \(K\) and the \(2\)-norm, so this point is central, hence scalar. Every point of \(K\) has trace zero by normality, so that scalar is zero.

If (14) failed for every unitary, the entire orbit would lie in the \(2\)-ball of radius \(\|b\|_2/2\) centered at \(b\), and so would \(K\), by convexity and the same lower semicontinuity. But \(0\in K\) and its distance from \(b\) is \(\|b\|_2\). This is impossible unless \(b=0\), when every unitary works. \(\square\)

**Theorem 5.2.** Every ordinary hypercentral sequence in \(R\) is scalar-trivial. For every free ultrafilter, \(R_\omega\) is a factor of type \(\mathrm{II}_1\).

**Proof.** First suppose an ordinary centralizing sequence \(a_n\) is not scalar-trivial. Select increasing indices \(k(r)\) with
\[
\|a_{k(r)}-\tau(a_{k(r)})1\|_2\ge\delta>0,\qquad
\|E_r(a_{k(r)})-a_{k(r)}\|_2\le2^{-r}.
\tag{15}
\]
This is possible because scalar distance has positive limsup and (13) holds for each fixed \(r\).
Put \(b_r=E_r(a_{k(r)})-\tau(a_{k(r)})1\in N_r\). It is trace zero, and choose \(u_r\in\mathcal U(N_r)\) satisfying (14).
Then
\[
\|a_{k(r)}-u_ra_{k(r)}u_r^*\|_2
\ge\frac12(\delta-2^{-r})-2^{1-r}.
\tag{16}
\]
Define a unitary sequence on the original indices by putting \(v_{k(r)}=u_r\) and \(v_n=1\) elsewhere. For every fixed \(s\), these unitaries eventually commute with \(D_s\): the exceptional finitely many \(k(r)\) with \(r<s\) cause no asymptotic problem. Bounded \(2\)-norm density of the finite stages extends centrality to all of \(R\). In a finite algebra centrality and centralizing coincide. But (16) stays positive on the selected indices. Thus the original \(a_n\) is not hypercentral, proving \(H(R)=T(R)\).

Now let \(A=\pi_\omega(a_n)\) be a central quotient element that is not scalar. After subtracting the scalar representative \(\tau(a_n)1\), assume \(\tau(a_n)=0\) and
\(\delta=\|A\|_{2,\omega}>0\).
For each \(r\), choose nested \(\omega\)-large sets \(B_r\subset\{n\ge r\}\) on which
\[
\|a_n\|_2\ge\delta/2,\qquad
\|E_r(a_n)-a_n\|_2\le1/r.
\tag{17}
\]
This uses (13) and the quotient \(2\)-norm limit. Let \(r(n)\) be the largest \(r\le n\) with \(n\in B_r\), and set \(r(n)=0\) if there is none. Then \(r(n)\to_\omega\infty\).

When \(r(n)>0\), put \(b_n=E_{r(n)}(a_n)\in N_{r(n)}\) and choose \(u_n\) there by (14); otherwise put \(u_n=1\). For each fixed \(s\), \(u_n\) commutes with \(D_s\) on the \(\omega\)-large set where \(r(n)\ge s\). Finite-stage \(2\)-density gives centrality along \(\omega\), and the finite-algebra commutator estimate gives centralizing. On \(B_1\),
\[
\|a_n-u_na_nu_n^*\|_2
\ge\delta/4-\frac{5}{2r(n)}.
\tag{18}
\]
Its ultralimit is at least \(\delta/4>0\). This contradicts centrality of \(A\) in the quotient. Hence \(Z(R_\omega)=\mathbb C\).

Finally, the matrix units in the individual tensor legs of (12) are ordinary centralizing sequences: they commute with every fixed finite initial stage and are uniformly bounded. They give a unital \(M_2\) in every \(R_\omega\), so these algebras are noncommutative. Theorem 4.1 gives type \(\mathrm{II}_1\), now with the trivial center just proved. \(\square\)

## 6. Exercises with complete solutions

**Exercise 1.** In Lemma 1.1, explain why the selected indices may be increasing.

*Solution.* Each finite-test intersection belongs to a free ultrafilter, hence is infinite. Removing the finite set \(\{1,\ldots,n(k-1)\}\) leaves another member of the ultrafilter. Choose \(n(k)\) in that remainder. This also ensures no fixed original coordinate is reused indefinitely.

**Exercise 2.** For bounded scalar sequences \(\lambda_n\), compute the quotient image and decide whether they contradict fullness.

*Solution.* Their quotient image is \((\lim_\omega\lambda_n)1\). They are scalar-trivial, whether or not they converge ordinarily. Fullness requires that all centralizing sequences be equivalent to such scalar sequences, so they satisfy its criterion.

**Exercise 3.** Prove that ordinary nonhypercentrality produces noncommutative quotient algebras for every free ultrafilter.

*Solution.* Choose a centralizing pair whose commutator seminorm has positive limsup. Restrict both to the same increasing subsequence on which the squared seminorm is at least \(\delta>0\). Both remain centralizing in the ordinary sense. Along any free ultrafilter their quotient commutator has squared \(2\)-norm at least \(\delta\), so that quotient is noncommutative.

**Exercise 4.** Why is a fixed noncommuting pair insufficient by itself to prove that a finite algebra is type \(\mathrm{II}_1\)?

*Solution.* The finite algebra \(M_2(\mathbb C)\oplus\mathbb C\) has noncommuting elements in its first summand, yet the projection onto its second summand is abelian. Theorem 4.1 excludes every nonzero abelian corner by constructing a new commutator inside each chosen corner. Merely having one nonzero commutator would not exclude a type I summand.

**Exercise 5.** In (10), identify the normal functional that tests the scalar limit of \(c_k^*c_k\).

*Solution.* For fixed \(n\), it is \(\psi_n(a)=\varphi(f_naf_n)\). Fixed multiplication and normality of \(\varphi\) make it normal. Pairing \(c_k^*c_k\to_\omega\kappa1\) ultraweakly with \(\psi_n\) gives the limit \(\kappa\psi_n(1)=\kappa\varphi(f_n)\). The projection is fixed while this particular \(k\)-limit is taken.

**Exercise 6.** Explain why the positive lower bound on \(\varphi(f_n)\) may be imposed at all coordinates.

*Solution.* The set \(S=\{n:\varphi(f_n)\ge\beta/2\}\) belongs to \(\omega\). Replace \(f_n\) by \(1\) outside \(S\). The original and altered sequences agree on \(S\), so their difference has zero ultralimit in every seminorm and their quotient images agree. Every centralizing limit also agrees because the commutator sequences agree on \(S\).

**Exercise 7.** Give an example of a finite type \(\mathrm{II}_1\) algebra with nontrivial center.

*Solution.* \(L^\infty([0,1])\bar\otimes R\), with product of Lebesgue integration and the normalized trace of \(R\), is finite and has only type II fibers. Its center is \(L^\infty([0,1])\otimes1\). Thus “type \(\mathrm{II}_1\)” alone does not imply “factor.” This example illustrates the type distinction; it is not an assertion that this particular algebra occurs as a central sequence algebra.

**Exercise 8.** In Lemma 5.1, prove uniqueness of the point of least \(2\)-norm.

*Solution.* If distinct \(x,y\in K\) had equal minimum norm \(m\), the parallelogram identity would give
\(\|(x+y)/2\|_2^2=m^2-\|x-y\|_2^2/4<m^2\).
Trace faithfulness makes \(\|x-y\|_2>0\). The midpoint lies in the convex set \(K\), a contradiction.

**Exercise 9.** Verify that the sequence \(v_n\) inserted at selected indices in (16) is central.

*Solution.* Fix \(D_s\). For \(n=k(r)\) with \(r\ge s\), \(v_n\in D_r'\cap R\subset D_s'\cap R\); elsewhere \(v_n=1\). Only the finitely many selected indices with \(r<s\) are exceptions. If \(x\in R\), approximate it in \(2\)-norm by a bounded finite-stage element \(x_0\). The bound \(\|[v_n,x-x_0]\|_2\le2\|x-x_0\|_2\), together with eventual commutation with \(x_0\), proves centrality. Finite trace then gives centralizing.

**Exercise 10.** Derive the constant in (18).

*Solution.* Let \(\varepsilon=\|a_n-b_n\|_2\le1/r(n)\). Then \(\|b_n\|_2\ge\|a_n\|_2-\varepsilon\ge\delta/2-\varepsilon\). The unitary chosen by (14) moves \(b_n\) by at least \(\delta/4-\varepsilon/2\). Replacing \(b_n\) by \(a_n\) on both sides loses at most \(2\varepsilon\). The final lower bound is \(\delta/4-(5/2)\varepsilon\), as claimed.

## References

The free sources are Dusa McDuff, [*On the structure of II₁-factors*](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5426&what=fullteng), Russian Mathematical Surveys 25(6) (1970), Lemmas 1.1–1.4 and Theorem 1.1, printed pp.32–35 (PDF pp.4–7); and Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://www.numdam.org/item/ASENS_1975_4_8_3_383_0/), Theorem 2.2.1, implication (d) ⇒ (e), printed pp.400–401 (PDF pp.19–20).

McDuff works with separable finite factors and the tracial 2-norm. In Theorem 1.1 she proves part (iii), leaving parts (i) and (ii) to a similar argument. Here both ordinary and ultrafilter selections are written out, with the faithful-state seminorms needed for arbitrary factors. The corner argument follows Connes's method and keeps the center: noncommutativity gives type II₁, without asserting factoriality. The hyperfinite tensor-tail argument separately proves triviality of its central sequence algebra's center. The preceding fullness theorem, finite type decomposition and projection halving remain declared inputs whose free prerequisite closure is not yet complete.

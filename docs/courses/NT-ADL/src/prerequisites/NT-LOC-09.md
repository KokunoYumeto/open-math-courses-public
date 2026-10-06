# Ramification groups and the different of a local extension

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

*NT-ADL bundled edition, source-reconciled on 5 October 2026 by GPT-6.1 Sol (OpenAI), Ultra. This adaptation retains the provider lesson's mathematical scope and adds the source comparisons identified below. The upstream provider draft is unchanged. Original AI-written exposition is CC0; human reference works and genuinely reused human expression retain their own terms.*

The ramification index separates tame extensions from wild ones, but it does not measure how far a wild automorphism moves an integral element. The lower ramification groups make that measurement. Their successive quotients constrain the Galois group, and the sum of their sizes gives the exponent of the different.

Throughout the local discussion, \(L/K\) is a finite Galois extension of nonarchimedean local fields, in either characteristic. Write \(G=\operatorname{Gal}(L/K)\), \(\mathcal O_L\) for the valuation ring, \(\mathfrak P\) for its maximal ideal, and \(\kappa_L\) for its residue field. Normalize \(v_L(L^\times)=\mathbf Z\), put \(v_L(0)=+\infty\), and let \(p=\operatorname{char}\kappa_L\). Thus \(v_L|_K=e\,v_K\), where \(e=e(L/K)\). Every automorphism preserves \(v_L\).

We use **Unramified and totally ramified extensions** for the maximal unramified subfield, integral monogenicity and Eisenstein extensions. **Tame ramification and the tame Galois group** supplies the meaning of tame ramification. Exact additional imports are listed at the end.

## 1. Measuring an automorphism intrinsically

Choose \(\alpha\) with \(\mathcal O_L=\mathcal O_K[\alpha]\). For \(\sigma\in G\), define
\[
i_G(\sigma)=v_L(\sigma\alpha-\alpha).
\]
In particular, \(i_G(1)=+\infty\). For integral \(i\geq-1\), set
\[
G_i=\{\sigma\in G:i_G(\sigma)\geq i+1\}.
\tag{1.1}
\]

**Proposition 1.1 (intrinsic lower groups).** The number \(i_G(\sigma)\) is independent of the chosen integral generator. More precisely,
\[
i_G(\sigma)=\min_{x\in\mathcal O_L}v_L(\sigma x-x).
\tag{1.2}
\]
The groups \(G_i\) are normal in \(G\), decrease with \(i\), and are trivial for sufficiently large \(i\). We have \(G_{-1}=G\), and \(G_0\) is the inertia group. If \(H\leq G\), the lower groups of \(L/L^H\), using the same normalized valuation on \(L\), satisfy
\[
H_i=H\cap G_i.
\tag{1.3}
\]

*Proof.* For \(x=P(\alpha)\), with \(P\in\mathcal O_K[X]\), the polynomial identity \(P(Y)-P(X)=(Y-X)Q(X,Y)\) gives
\[
\sigma x-x=(\sigma\alpha-\alpha)Q(\alpha,\sigma\alpha).
\]
The second factor is integral. Hence every value in (1.2) is at least \(i_G(\sigma)\), and \(x=\alpha\) attains the bound. This proves (1.2), including the identity case, and removes dependence on \(\alpha\).

For an integer \(i\geq0\), membership in \(G_i\) says exactly that \(\sigma\) acts trivially on every element of \(\mathcal O_L/\mathfrak P^{i+1}\). Consequently it is a subgroup. Explicitly,
\[
\sigma\tau x-x=\sigma(\tau x-x)+(\sigma x-x),
\]
and preservation of valuation proves closure; replacing \(x\) by \(\sigma^{-1}x\) proves closure under inverses. Conjugation by \(\gamma\in G\) replaces the test element by \(\gamma^{-1}x\), which runs over all of \(\mathcal O_L\), and preserves its value. Thus \(G_i\) is normal. Decrease is immediate.

Every difference of integral elements is integral, so \(G_{-1}=G\). Trivial action modulo \(\mathfrak P\) is precisely the definition of inertia, so \(G_0\) is inertia. If \(\sigma\ne1\), it cannot fix the generator \(\alpha\); its value \(i_G(\sigma)\) is finite. There are finitely many such automorphisms, and taking \(i\) above all their values makes \(G_i\) trivial.

The extension \(L/L^H\) is again Galois and local. Its intrinsic test (1.2) uses the same ring \(\mathcal O_L\) and the same \(v_L\), so its condition on an element \(\sigma\in H\) is exactly the condition defining \(G_i\). This proves (1.3), without assuming \(H\) normal in \(G\). \(\square\)

For real \(u\geq-1\), our convention is
\[
G_u=G_{\lceil u\rceil}.
\tag{1.4}
\]
For instance, \(G_u=G_0\) on \((-1,0]\) and \(G_u=G_1\) on \((0,1]\). At an integer jump the value is the group on its left. This convention will determine the endpoints in the upper numbering.

## 2. The graded pieces

Let \(L_0\) be the maximal unramified subfield of \(L/K\). Its residue field is \(\kappa_L\), and \(L/L_0\) is totally ramified.

The correspondence between unramified extensions and residue extensions identifies \(\operatorname{Gal}(L_0/K)\) with \(\operatorname{Gal}(\kappa_L/\kappa_K)\). The field \(L_0\) is stable under \(G\) by its defining maximality. Restriction from \(G\) onto \(\operatorname{Gal}(L_0/K)\) is surjective: an embedding of this intermediate field extends to an embedding of the finite normal extension \(L/K\). Its kernel is exactly \(G_0\), since the unramified correspondence identifies the action on \(L_0\) with the action on its residue field. In particular,
\[
|G_0|=[L:L_0]=e.
\tag{2.1}
\]

Fix a uniformizer \(\pi\) of \(L\). Total ramification gives \(\mathcal O_L=\mathcal O_{L_0}[\pi]\). Every \(\sigma\in G_0\) fixes \(L_0\), so the same polynomial-difference argument as before now gives
\[
i_G(\sigma)=v_L(\sigma\pi-\pi)
\qquad(\sigma\in G_0).
\tag{2.2}
\]
This uniformizer formula is intended for inertia; a noninertial automorphism has \(i_G(\sigma)=0\).

Write \(U_L^0=\mathcal O_L^\times\) and \(U_L^r=1+\mathfrak P^r\) for \(r\geq1\).

**Proposition 2.1 (canonical graded injections).** There are injective homomorphisms
\[
G_0/G_1\longrightarrow\kappa_L^\times,
\qquad
\sigma G_1\longmapsto\overline{\sigma\pi/\pi},
\tag{2.3}
\]
and, for \(r\geq1\),
\[
G_r/G_{r+1}\longrightarrow U_L^r/U_L^{r+1},
\qquad
\sigma G_{r+1}\longmapsto(\sigma\pi/\pi)U_L^{r+1}.
\tag{2.4}
\]
Both maps are independent of \(\pi\). The group \(U_L^r/U_L^{r+1}\) is isomorphic to the additive group of \(\kappa_L\); that last identification uses \(\pi\).

*Proof.* Put \(c_\sigma=\sigma\pi/\pi\). For inertia,
\[
c_{\sigma\tau}=\sigma(c_\tau)c_\sigma.
\tag{2.5}
\]
Inertia acts trivially on residue units, so reduction makes (2.5) multiplicative. Equation (2.2) says that the kernel is \(G_1\), proving (2.3).

For \(r\geq1\), the map
\[
U_L^r/U_L^{r+1}\longrightarrow(\kappa_L,+),
\qquad
(1+a\pi^r)U_L^{r+1}\longmapsto\bar a
\tag{2.6}
\]
is well defined and bijective. Multiplication becomes addition because \(\mathfrak P^{2r}\subseteq\mathfrak P^{r+1}\).

Every \(\sigma\in G_1\) acts trivially on this quotient. Indeed, \(\sigma a\equiv a\pmod{\mathfrak P}\), and \(\sigma\pi/\pi\equiv1\pmod{\mathfrak P}\), so
\(\sigma(a\pi^r)\equiv a\pi^r\pmod{\mathfrak P^{r+1}}\).
For \(\sigma,\tau\in G_r\), (2.2) puts \(c_\sigma,c_\tau\) in \(U_L^r\); (2.5) is therefore a homomorphism in this quotient. Its kernel is \(G_{r+1}\), again by (2.2).

If \(\pi'=u\pi\), with \(u\in\mathcal O_L^\times\), then
\[
\frac{\sigma\pi'}{\pi'}=
\frac{\sigma u}{u}\frac{\sigma\pi}{\pi}.
\]
For \(\sigma\in G_r\), the intrinsic definition gives
\(v_L(\sigma u-u)\geq r+1\). Thus \(\sigma u/u\in U_L^{r+1}\), also for \(r=0\) with the evident interpretation. Both (2.3) and (2.4) are unchanged.

Changing \(\pi\) does change the coordinate (2.6): if \(\pi'=u\pi\), the residue coefficient changes by \(\bar u^{-r}\). The injection into the unit quotient is canonical; its residue-field coordinate need not be. \(\square\)

**Corollary 2.2 (wild inertia and solvability).** The group \(G_0/G_1\) is cyclic of order prime to \(p\). The group \(G_1\) is the unique Sylow \(p\)-subgroup of \(G_0\). Every finite Galois group of nonarchimedean local fields is solvable. Moreover,
\[
L/K\text{ is tame}\quad\Longleftrightarrow\quad G_1=1.
\]

*Proof.* The finite cyclic group \(\kappa_L^\times\) has order prime to \(p\). Equation (2.3) proves the first assertion. Each quotient \(G_r/G_{r+1}\), for \(r\geq1\), is a subgroup of the additive residue field, so it is an elementary abelian \(p\)-group. The filtration terminates; multiplying its quotient orders shows that \(G_1\) is a \(p\)-group. Its index in \(G_0\) is prime to \(p\), and its normality makes it the unique Sylow subgroup.

The same terminating filtration has abelian quotients, so \(G_1\), and then \(G_0\), are solvable. Finally \(G/G_0\) is the cyclic finite-field Galois group described above. A group with a solvable normal subgroup and solvable quotient is solvable: lift a derived series for the quotient and then append one for the normal subgroup. This proves the assertion for \(G\). By (2.1), \(p\nmid e\) exactly when \(G_1=1\); residue extensions of local fields are separable, so this is precisely tameness. \(\square\)

## 3. Hilbert's formula

For any finite separable extension of local fields, define its trace-dual lattice and different by
\[
\mathcal O_L^*=
\{x\in L : \operatorname{Tr}_{L/K}(x\mathcal O_L)\subseteq\mathcal O_K\},
\qquad
\mathfrak D_{L/K}=(\mathcal O_L^*)^{-1}.
\tag{3.1}
\]
The trace form is nondegenerate. Its dual lattice is a fractional \(\mathcal O_L\)-ideal, and inversion is fractional-ideal inversion. If \(\mathcal O_L=\mathcal O_K[\alpha]\), with monic minimal polynomial \(f\), the monogenic different theorem gives
\[
\mathfrak D_{L/K}=f'(\alpha)\mathcal O_L.
\tag{3.2}
\]
This algebraic trace-dual theorem is proved in *Number fields*, lesson 14, [**The different and the discriminant**](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ANT/the-different-and-the-discriminant.html), “The trace dual,” Euler's dual-basis lemma and Proposition 14.2. Its hypotheses are a Dedekind base ring and a finite separable extension with finite integral closure; the monogenic formula additionally requires the full integral closure to be \(\mathcal O_K[\alpha]\). Complete local integer rings satisfy these conditions by **Extensions of complete valued fields**, Theorem 3.1. The field trace pairing is nondegenerate precisely for separable extensions, as proved in [Stacks, Tag 0BIL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-separable-trace-pairing). The ramification formula that follows is proved here.

### The algebraic trace calculation and its scope

Here is a direct verification of the algebraic identities used in (3.1)–(3.2) and in Section 4. Let \(A\) be a Dedekind domain with fraction field \(F\), let \(E/F\) be finite separable, and suppose its full integral closure \(B\) is finite over \(A\). Define
\[
 B^*=\{y\in E:\operatorname{Tr}_{E/F}(yB)\subseteq A\},\qquad
 D=(B^*)^{-1}.
\]
The nondegenerate field trace pairing is the stated algebra prerequisite. Choose an \(F\)-basis \(b_1,\ldots,b_m\) from \(B\), and set \(V=\sum A b_i\subseteq B\). In this basis the trace matrix is invertible over \(F\), so \(V^*=T^{-1}A^m\) is a finite \(A\)-lattice. Since \(B^*\subseteq V^*\) and \(A\) is Noetherian, \(B^*\) is finite over \(A\). It is stable under multiplication by \(B\). Also \(B\subseteq B^*\): products of integral elements have integral field trace, and an element of \(F\) integral over the integrally closed ring \(A\) lies in \(A\). Thus \(B^*\) is a nonzero fractional \(B\)-ideal spanning \(E\); it is invertible because \(B\) is Dedekind. Its inverse \(D\) is an integral ideal, since \(B\subseteq B^*\). None of this requires a separable residue extension.

If in addition \(B=A[\alpha]\), write the monic minimal polynomial as \(f(X)\in A[X]\), of degree \(m\), and
\[
 \frac{f(X)}{X-\alpha}=\sum_{j=0}^{m-1}c_j(\alpha)X^j.
\]
The elements \(c_{m-1}(\alpha),c_{m-2}(\alpha),\ldots,c_0(\alpha)\) have leading terms \(1,\alpha,\ldots,\alpha^{m-1}\); their change of basis from these powers is unit triangular over \(A\). In a splitting field, the distinct roots \(\beta\) of \(f\) satisfy the Lagrange interpolation identity
\[
 X^r=\sum_{f(\beta)=0}\frac{\beta^r}{f'(\beta)}\frac{f(X)}{X-\beta}\qquad(0\le r<m).
\]
Comparing coefficients of \(X^j\) proves
\[
 \operatorname{Tr}_{E/F}\!\left(\alpha^r\frac{c_j(\alpha)}{f'(\alpha)}\right)=\delta_{rj}.
\]
Consequently these \(m\) elements are the trace-dual basis to \(1,\alpha,\ldots,\alpha^{m-1}\). The unit-triangular observation gives \(B^*=f'(\alpha)^{-1}B\), hence \(D=f'(\alpha)B\). Separability supplies the distinct roots and nonzero derivative; the additional ring equality \(B=A[\alpha]\) is essential.

Trace-dual formation commutes with localization: a finite set of generators of \(B\) gives finitely many trace-integrality conditions, whose denominators can be cleared by one element of the multiplicative set. Thus the localized lattice is exactly the trace dual of the localized ring.

For the discriminant, localize at a nonzero prime \(\mathfrak p\) of \(A\). Then \(B_{\mathfrak p}\) is a finite free \(A_{\mathfrak p}\)-module. In a basis with trace matrix \(T\), its trace dual is \(T^{-1}A_{\mathfrak p}^{m}\), and elementary divisors over this DVR give
\[
 \operatorname{length}_{A_{\mathfrak p}}(B^*_{\mathfrak p}/B_{\mathfrak p})
 =v_{\mathfrak p}(\det T).
\]
If \(D=\prod_{\mathfrak P}\mathfrak P^{d_{\mathfrak P}}\), the quotient on the left has \(d_{\mathfrak P}\) composition factors isomorphic to \(B/\mathfrak P\) at each \(\mathfrak P\mid\mathfrak p\). Each such factor has \(A_{\mathfrak p}\)-length \(f(\mathfrak P/\mathfrak p)\). Therefore
\[
 v_{\mathfrak p}(\mathfrak d_{B/A})
 =\sum_{\mathfrak P\mid\mathfrak p} f(\mathfrak P/\mathfrak p)d_{\mathfrak P},\qquad
 \mathfrak d_{B/A}=N_{B/A}(D),
\]
where the ideal norm sends \(\mathfrak P\) to \(\mathfrak p^{\,f(\mathfrak P/\mathfrak p)}\). This proves the norm identity without a monogenic assumption. As usual the discriminant ideal is defined locally by these determinants when the global module is projective rather than free. The hypotheses remain finite separability and finite integral closure over a Dedekind base; residue separability is not used. Sutherland, Lecture 12, Proposition 12.24 and Theorem 12.17, gives a classical comparison for a finite separable extension of a Dedekind domain; the calculation above records the general algebraic scope required by the provider lesson.

**Theorem 3.1 (Hilbert).** For the finite Galois extension \(L/K\),
\[
d(L/K):=v_L(\mathfrak D_{L/K})
=\sum_{\sigma\ne1}i_G(\sigma)
=\sum_{r\geq0}(|G_r|-1).
\tag{3.3}
\]
Consequently a tame extension has different exponent \(e-1\), and a wild extension has exponent at least \(e\).

*Proof.* Normality and separability give
\[
f(X)=\prod_{\sigma\in G}(X-\sigma\alpha),
\qquad
f'(\alpha)=\prod_{\sigma\ne1}(\alpha-\sigma\alpha).
\]
Taking valuation in (3.2) proves the first sum. For a nonidentity automorphism, \(i_G(\sigma)\) is a nonnegative integer. It belongs to exactly \(i_G(\sigma)\) of the groups indexed \(r\geq0\), since their condition is \(r+1\leq i_G(\sigma)\). Summing these finitely many indicator functions proves the second sum.

The \(r=0\) summand is \(e-1\). In the tame case all subsequent groups are trivial. In the wild case \(G_1\ne1\), so its summand contributes at least one more. \(\square\)

## 4. Passing between number fields and completions

Let \(E/F\) be a finite extension of number fields. Write \(\mathfrak D_{E/F}\) for the different defined by the global trace dual. For a finite prime \(\mathfrak p\) of \(F\) and each \(\mathfrak P\mid\mathfrak p\), let \(F_{\mathfrak p}\) and \(E_{\mathfrak P}\) be the completions.

**Proposition 4.1 (local exponents determine the global different).** Put
\[
d_{\mathfrak P}=v_{\mathfrak P}
  (\mathfrak D_{E_{\mathfrak P}/F_{\mathfrak p}}).
\]
Then
\[
\mathfrak D_{E/F}=\prod_{\mathfrak P}\mathfrak P^{d_{\mathfrak P}}.
\tag{4.1}
\]
Only finitely many factors are nontrivial. The relative discriminant ideal has exponent
\[
v_{\mathfrak p}(\mathfrak d_{E/F})
=\sum_{\mathfrak P\mid\mathfrak p}
f(\mathfrak P/\mathfrak p)d_{\mathfrak P}.
\tag{4.2}
\]

*Proof.* Set \(A=(\mathcal O_F)_{\mathfrak p}\), \(B=(\mathcal O_E)_{\mathcal O_F\setminus\mathfrak p}\), and let \(\widehat A=\mathcal O_{F_{\mathfrak p}}\). The ring \(B\) is a finite torsion-free \(A\)-module. Since \(A\) is a DVR, \(B\) is free. Ideal factorization and the Chinese remainder theorem give
\[
B/\mathfrak p^nB
\simeq
\prod_{\mathfrak P\mid\mathfrak p}
\mathcal O_E/\mathfrak P^{n e(\mathfrak P/\mathfrak p)}.
\]
Localizing the factors at \(\mathfrak P\) changes none of these quotients. Their inverse limits are the completed local integer rings: the subsequence of powers \(n e(\mathfrak P/\mathfrak p)\) is cofinal among all powers. Taking inverse limits, or completing a finite free \(A\)-basis, proves
\[
B\otimes_A\widehat A
\simeq\prod_{\mathfrak P\mid\mathfrak p}\mathcal O_{E_{\mathfrak P}}.
\tag{4.3}
\]

Here is why the trace dual commutes with this operation. Choose an \(A\)-basis \(b_1,\ldots,b_m\) of \(B\), and let \(T=(\operatorname{Tr}_{E/F}(b_jb_k))\). It is invertible over \(F\), by separability. In coordinates,
\[
B^*=T^{-1}A^m,
\qquad
B^*\otimes_A\widehat A=T^{-1}\widehat A^m.
\]
The trace of multiplication is preserved by scalar extension. The completion decomposition of **Places of number fields in extensions and the product formula** identifies it with the sum of the local traces. The dual of the product lattice (4.3) for this sum is therefore
\[
B^*\otimes_A\widehat A
\simeq
\prod_{\mathfrak P\mid\mathfrak p}
\mathcal O_{E_{\mathfrak P}}^*.
\tag{4.4}
\]
Indeed, testing elements supported in a single factor tests each local trace condition separately.

The global trace dual localizes to \(B^*\): in a finite basis its trace integrality conditions are a finite system of linear equations, and localization clears their finitely many denominators. Fractional ideals in the Dedekind ring \(B\) are invertible and become principal at each maximal ideal. Completion preserves the exponent of that principal ideal, and inversion negates its exponent. Inverting (4.4) thus shows that the exponent of the global different at \(\mathfrak P\) is exactly \(d_{\mathfrak P}\). Unique factorization of fractional ideals proves (4.1); a fractional ideal has finite support.

Finally the algebraic discriminant theorem identifies \(\mathfrak d_{E/F}\) with the ideal norm of \(\mathfrak D_{E/F}\). Since the norm of \(\mathfrak P\) is \(\mathfrak p^{f(\mathfrak P/\mathfrak p)}\), taking norms in (4.1) gives (4.2). \(\square\)

The proposition applies to extensions that are not Galois. Hilbert's formula computes each local exponent directly when that local extension is Galois; the monogenic derivative formula also applies in the separable nongalois case.

## 5. The cyclotomic filtration

Let \(n\geq1\), let \(\zeta\) be a primitive \(p^n\)-th root of unity, and put \(L=\mathbf Q_p(\zeta)\).

**Proposition 5.1.** The extension is totally ramified of degree
\[
N=(p-1)p^{n-1},
\]
with uniformizer \(\pi=\zeta-1\) and Galois group
\[
G=(\mathbf Z/p^n\mathbf Z)^\times,
\qquad
\sigma_a(\zeta)=\zeta^a.
\]
Its lower groups are \(G_0=G\), and
\[
G_i=\{a:a\equiv1\pmod{p^k}\}
\quad\text{if}\quad
p^{k-1}\leq i\leq p^k-1,\quad 1\leq k\leq n.
\tag{5.1}
\]
In particular \(G_i=1\) for \(i\geq p^{n-1}\), and
\[
d(L/\mathbf Q_p)=np^n-(n+1)p^{n-1}.
\tag{5.2}
\]

*Proof.* The cyclotomic polynomial here is
\[
\Phi_{p^n}(X)=\sum_{j=0}^{p-1}X^{j p^{n-1}}.
\]
Modulo \(p\), \(\Phi_{p^n}(1+Y)=Y^N\); its constant coefficient over \(\mathbf Z_p\) is \(p\). Thus \(\Phi_{p^n}(1+Y)\) is Eisenstein. It proves the degree, total ramification, and uniformizer assertions, with \(\mathcal O_L=\mathbf Z_p[\zeta]\). All primitive roots \(\zeta^a\) already lie in \(L\); the polynomial is separable, so the extension is Galois and all \(N\) residue-unit exponents give distinct automorphisms.

For \(a\ne1\) modulo \(p^n\), let \(k=v_p(a-1)\), so \(0\leq k<n\). The root \(\zeta^{a-1}\) has order \(p^{n-k}\). Its difference from \(1\) is a uniformizer in the corresponding smaller cyclotomic field, by the same Eisenstein argument. The ramification index from that field to \(L\) is the ratio of their degrees, namely \(p^k\). Therefore
\[
i_G(\sigma_a)
=v_L(\zeta^{a-1}-1)=p^k.
\tag{5.3}
\]
This determines every group: if \(p^{k-1}\leq i\leq p^k-1\), the condition \(p^{v_p(a-1)}\geq i+1\) is precisely \(a\equiv1\pmod{p^k}\). Identity is included throughout. For \(k=n\) the congruence subgroup is trivial.

For \(1\leq k<n\), that congruence subgroup has \(p^{n-k}\) elements and occupies \(p^k-p^{k-1}\) indices. Hence Hilbert's formula gives
\[
\begin{aligned}
d
&=N-1+
\sum_{k=1}^{n-1}(p^k-p^{k-1})(p^{n-k}-1)\\
&=N-1+(n-1)N-(p^{n-1}-1)\\
&=nN-p^{n-1},
\end{aligned}
\]
which is (5.2). An empty sum when \(n=1\) gives \(d=p-2\); for \(p=2,n=1\) the extension is the trivial field \(\mathbf Q_2\), and \(d=0\).

There is also an independent derivative check. Differentiating
\((X^{p^{n-1}}-1)\Phi_{p^n}(X)=X^{p^n}-1\) at \(\zeta\) gives
\[
\Phi_{p^n}'(\zeta)
=\frac{p^n\zeta^{p^n-1}}{\zeta^{p^{n-1}}-1}.
\]
The numerator has value \(nN\), while the denominator has value \(p^{n-1}\). Formula (3.2) again gives \(d=nN-p^{n-1}\). \(\square\)

## 6. Three quadratic examples

**Example 6.1.** In \(L=\mathbf Q_2(i)\), the element \(\pi=i-1\) satisfies the Eisenstein polynomial \(Y^2+2Y+2\). Thus \(v_L(2)=2\), and conjugation gives
\[
\sigma\pi-\pi=-2i,\qquad i_G(\sigma)=2.
\]
The only nonidentity element belongs to \(G_0,G_1\), so
\[
G_0=G_1=G,\quad G_2=1,\quad d=2.
\]
The integral basis \(1,i\) has discriminant \(-4\), whose \(2\)-adic exponent is \(2\).

**Example 6.2.** In \(L=\mathbf Q_2(\sqrt2)\), \(\pi=\sqrt2\) is an Eisenstein uniformizer. Conjugation changes it by \(-2\sqrt2\), of value \(2+1=3\). Therefore
\[
G_0=G_1=G_2=G,\quad G_3=1,\quad d=3.
\]
The integral basis \(1,\sqrt2\) has discriminant \(8\), again with the predicted exponent.

**Example 6.3.** In \(L=\mathbf Q_3(\sqrt3)\), the same difference \(-2\sqrt3\) has value \(1\), since \(2\) is a unit. Thus
\[
G_0=G,\quad G_1=1,\quad d=1=e-1.
\]
This is tame. The discriminant of \(1,\sqrt3\) is \(12\), whose \(3\)-adic exponent is \(1\).

Each residue degree is \(1\), so the local different exponent equals the base discriminant exponent, as (4.2) predicts.

## 7. Exercises

1. Compute the lower groups of \(\mathbf Q_2(i)/\mathbf Q_2\) and verify Hilbert's formula.

2. Compute them for \(\mathbf Q_2(\sqrt2)/\mathbf Q_2\) and \(\mathbf Q_3(\sqrt3)/\mathbf Q_3\), including their differents.

3. Prove the subgroup rule \(H_i=H\cap G_i\), explaining why no normality assumption on \(H\) is needed.

4. Prove the cyclotomic filtration and different formula (5.1)–(5.2), including \(p=2\) and \(n=1\).

## 8. Complete solutions

**Solution 1.** Substitute \(i=1+\pi\) into \(i^2+1=0\), obtaining \(\pi^2+2\pi+2=0\). Eisenstein gives a totally ramified quadratic extension with uniformizer \(\pi\), so \(v_L(2)=2\). Its conjugate is \(-i-1\), and the difference is \(-2i\). Since \(i\) is a unit, its value is \(2\). By (2.2), the nonidentity conjugation belongs exactly to \(G_r\) with \(r+1\leq2\). Thus \(G_{-1}=G_0=G_1=G\) and all \(G_r\), \(r\geq2\), are trivial. Hilbert's sum is \((2-1)+(2-1)=2\). Directly, \(f'(i)=2i\) generates the different and has the same value; the integral power basis discriminant is \(-4\).

**Solution 2.** The Eisenstein polynomials \(X^2-2\) and \(X^2-3\) give total quadratic extensions with uniformizers their respective square roots. For the first, \(v_L(2)=2\), so conjugation moves the uniformizer by \(-2\sqrt2\), of value \(3\). The groups through index \(2\) equal the order-two group, and those from index \(3\) onward are trivial. Hilbert gives \(d=3\), also the value of \(2\sqrt2\); the basis discriminant is \(8\).

For the second, \(2\) is a \(3\)-adic unit, so the conjugation difference \(-2\sqrt3\) has value \(1\). Only \(G_0\) among the groups indexed at least zero is nontrivial. Hilbert gives \(d=1\), also the value of the derivative \(2\sqrt3\). The basis discriminant is \(12\), of \(3\)-adic exponent \(1\). The index \(2\) is prime to the residue characteristic \(3\), consistent with the tame formula.

**Solution 3.** The fixed-field theorem makes \(L/L^H\) finite Galois with group \(H\); its upper field and normalized valuation are still \(L,v_L\). Integral monogenicity holds over the local base \(L^H\), so the polynomial-difference proof of (1.2) expresses its ramification number as the minimum of \(v_L(\sigma x-x)\) over all \(x\in\mathcal O_L\). This is exactly the same minimum used for \(L/K\). Membership in its \(i\)-th group therefore means \(\sigma\in H\) and \(i_G(\sigma)\geq i+1\), which is \(H\cap G_i\). Normality of \(H\) is relevant to whether \(L^H/K\) is Galois, and is unnecessary for \(L/L^H\). The argument also covers real indices by the ceiling convention.

**Solution 4.** Reducing \(\sum_{j=0}^{p-1}(1+Y)^{j p^{n-1}}\) modulo \(p\) gives \(Y^{(p-1)p^{n-1}}\), and its constant term is exactly \(p\). Eisenstein proves the degree \(N=(p-1)p^{n-1}\), total ramification and uniformizer \(\zeta-1\). The roots \(\zeta^a\), for unit exponents \(a\), all lie in the field, giving the stated Galois group.

If \(a\ne1\) and \(k=v_p(a-1)<n\), then \(\zeta^{a-1}\) is primitive of order \(p^{n-k}\). Its difference from \(1\) has value \(1\) in its own cyclotomic field. Multiplying by the relative ramification index \(p^k\) gives \(i_G(\sigma_a)=p^k\). For indices \(p^{k-1}\leq i\leq p^k-1\), the inequality \(i_G(\sigma_a)\geq i+1\) requires \(v_p(a-1)\geq k\), giving (5.1). At \(k=n\) only identity remains, so all indices at least \(p^{n-1}\) are trivial.

The zeroth group contributes \(N-1\). For each \(1\leq k<n\), there are \(p^k-p^{k-1}\) indices with group order \(p^{n-k}\). Their total is
\[
\sum_{k=1}^{n-1}(p^k-p^{k-1})(p^{n-k}-1)
=(n-1)N-(p^{n-1}-1).
\]
Adding \(N-1\) gives \(nN-p^{n-1}=np^n-(n+1)p^{n-1}\). The calculation includes \(p=2\). For \(n=1\) the sum is empty, giving \(p-2\); when also \(p=2\), the Galois group is trivial and the exponent is zero. Differentiating the cyclotomic quotient as in Section 5 verifies the answer directly from the different.

## Source comparison for this edition

For lower ramification groups Fesenko–Vostokov, Chapter II, (4.3)–(4.4), and Milne 7.58–7.59 give the intrinsic filtration, uniformizer criteria and graded quotients. Section 2 here proves the graded maps, including what is independent of the uniformizer and what changes with a residue coordinate. The finite-residue assumption makes the residue multiplicative group cyclic and the higher quotients \(p\)-groups; the wild Sylow and solvability conclusions keep that hypothesis. The cyclotomic filtration, its endpoint cases and its independent derivative check remain in Sections 5 and 8.

The ramification criteria in Sutherland, Lecture 12, Theorems 12.19 and 12.27, assume separable residue extensions. The abstract trace-dual, monogenic derivative and ideal-norm identities used here have the wider algebraic scope stated in the trace calculation of Section 3: a finite separable field extension and finite integral closure over a Dedekind domain, with full integral monogenicity required only for the derivative formula. That calculation proves the identities without a residue-separability assumption. Section 4 then proves the completion identity by a finite free basis, Chinese remainders and the trace matrix; it applies to nongalois number-field extensions as well. The local Galois hypotheses belong to Hilbert's sum, not to the global trace-dual comparison.

## 9. What this lesson does not prove

- Integral monogenicity for a finite separable extension of local fields, \(\mathcal O_L=\mathcal O_K[\alpha]\), is Corollary 6.2 of **Unramified and totally ramified extensions**. Its Proposition 6.1 gives the maximal unramified subfield; Theorem 5.1 gives uniformizers and integral bases in a totally ramified extension. The finite-field Galois correspondence and Frobenius description are its Corollary 3.1.
- Trace nondegeneracy is [Stacks, Tag 0BIL]. Section 3 supplies the trace-dual, monogenic derivative and ideal-norm calculations with their general algebraic hypotheses. The exact written companion provider is *Number fields*, lesson 14, **The different and the discriminant**, “The trace dual,” Euler's lemma, Proposition 14.2 and Theorem 14.3. The Dedekind-ring and finite-integral-closure prerequisites for those calculations remain the imports in the next bullet. Sutherland, Lecture 12, Definition 12.2, Proposition 12.24 and Theorem 12.17, is a classical comparison.
- The written *Number fields* proofs are lesson 2, **Discriminants and integral bases**, Theorem 2.3 for the integer lattice; lesson 3, **Discrete valuation rings and Dedekind domains**, Proposition 3.1, Theorem 3.2 and Proposition 3.3 for Dedekindness, fractional-ideal factorization and Chinese remainders; and lesson 5, **Decomposition of primes in extensions**, Theorems 5.1–5.2 for finite integral closure and prime ideal norms. Milne, Proposition 2.29, Theorems 3.7 and 3.29 and Chapter 4 are classical references for the same facts. The field-completion decomposition and base change of trace are Theorem 2.1 and Corollary 2.2 of **Places of number fields in extensions and the product formula**.
- The extension of embeddings to a finite normal extension, the fixed-field theorem, and Sylow theory are the field and finite-group background of **Graduate Algebra**. Cyclicity of finite subgroups of a field's multiplicative group follows from [Stacks, Tag 09HX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-cyclic): its torsion bound is the polynomial root bound. Milne, *Fields and Galois Theory*, Proposition 4.19 with Exercise 1-3 is another classical reference.

## References

I. B. Fesenko and S. V. Vostokov, [*Local Fields and Their Extensions*](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf), second edition, American Mathematical Society, 2002, Chapter II, §4, (4.3)–(4.4) and the corollaries of (4.4).

A. V. Sutherland, [*The different and the discriminant*](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), MIT 18.785 Number Theory I lecture notes, Fall 2021, Lecture 12, Definition 12.2, Propositions 12.4 and 12.24, and Theorems 12.17, 12.19 and 12.27.

J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08 (19 July 2020), Chapter 7, “Ramification groups,” Theorem 7.58 and Corollary 7.59.

[Stacks, Tag 09EC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-decomposition-inertia), for decomposition and inertia. The higher filtration and the different calculation are developed explicitly above.

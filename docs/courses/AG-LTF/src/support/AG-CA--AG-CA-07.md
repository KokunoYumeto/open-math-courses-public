# Tor and flat modules

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). The proof of Lazard's theorem follows the Stacks Project's argument, cited at the end.*

Tensor products preserve quotients, but can turn an injection into a map with a kernel. Flatness is the condition that this loss never occurs. Tor measures the loss, while the equational criterion describes flatness through finite lists of elements and relations. Together these viewpoints explain why flatness is local, when it gives a free module, and how it constrains prime ideals in a family.

Rings are commutative with identity. A finite module means finitely generated; finite presentation additionally requires finitely many relations. Local rings need not be Noetherian. We use localization, local detection and Nakayama from *Localization, local properties and support*, especially Theorems 2.1, 3.1, 4.2 and 5.1. The preceding required lesson *Resolutions, Tor and Ext*, Theorems 1.1 and 3.2, proves resolution comparison, balance, symmetry and the homology sequences used below. Section 6 constructs the filtered free presentations of every flat module.

## 1. What Tor measures

Choose an augmented free resolution of an \(R\)-module \(M\):

\[
\cdots\longrightarrow F_2\xrightarrow{d_2}F_1
\xrightarrow{d_1}F_0\longrightarrow M\longrightarrow0.
\]

Free ranks can be infinite. Such a resolution is obtained by successively taking free modules surjecting onto kernels. Remove the augmentation to \(M\), tensor the resulting complex with \(N\), and define

\[
\operatorname{Tor}_i^R(M,N)=H_i(F_\bullet\otimes_R N),
\qquad i\geq0.
\]

Here the differential decreases degree. Right exactness of tensor gives \(\operatorname{Tor}_0^R(M,N)=M\otimes_R N\).

The comparison and balance proofs in *Resolutions, Tor and Ext* make Tor a bifunctor independent of the chosen resolution, with natural symmetry \(\operatorname{Tor}_i^R(M,N)\simeq\operatorname{Tor}_i^R(N,M)\); it can be computed by a projective resolution of either variable. For every short exact sequence \(0\to N'\to N\to N''\to0\), its long exact sequence has segments

\[
\cdots\to\operatorname{Tor}_i^R(M,N')
\to\operatorname{Tor}_i^R(M,N)
\to\operatorname{Tor}_i^R(M,N'')
\to\operatorname{Tor}_{i-1}^R(M,N')\to\cdots
\]

and ends in

\[
\operatorname{Tor}_1^R(M,N'')\longrightarrow M\otimes_R N'
\longrightarrow M\otimes_R N
\longrightarrow M\otimes_R N''\longrightarrow0.
\tag{1}
\]

Symmetry gives the corresponding sequence in the first variable. The connecting maps are natural in maps of short exact sequences: their lift-and-differentiate construction and its exactness are proved in Section 2 of that preceding lesson. References are [Stacks, Tags 00LZ, 00M0, 00M3], with links below.

**A principal equation.** If multiplication by \(a\) is injective on \(R\), then

\[
0\longrightarrow R\xrightarrow{a}R\longrightarrow R/(a)\longrightarrow0
\]

is a free resolution. Consequently

\[
\operatorname{Tor}_i^R(R/(a),N)=
\begin{cases}
N/aN,&i=0,\\
\{n\in N:an=0\},&i=1,\\
0,&i\geq2.
\end{cases}
\tag{2}
\]

For instance, \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\) is the kernel of multiplication by \(n\) on \(\mathbb Z/m\), for positive \(n,m\). If \(d=\gcd(n,m)\), its elements are the multiples of \(m/d\) modulo \(m\); it is cyclic of order \(d\). All higher Tor groups vanish.

The injectivity hypothesis on \(a\) matters. For \(R=k[\epsilon]/(\epsilon^2)\) and \(k=R/(\epsilon)\), the two-term complex is not a resolution. Instead use

\[
\cdots\xrightarrow{\epsilon}R\xrightarrow{\epsilon}R
\xrightarrow{\epsilon}R\longrightarrow k\longrightarrow0.
\]

Its kernels and images are both \((\epsilon)\) in positive degrees, so it is exact. After tensoring with \(k\), every differential is zero. Thus \(\operatorname{Tor}_i^R(k,k)=k\) in every degree, including arbitrarily high ones.

## 2. The ideal and Tor criteria

An \(R\)-module \(M\) is **flat** if \(-\otimes_R M\) is exact. Since tensor is always right exact, this means that it preserves every injection. A ring map \(R\to S\) is flat if \(S\) is flat as an \(R\)-module.

**Theorem 2.1.** For an arbitrary \(R\)-module \(M\), the following are equivalent:

1. \(M\) is flat.
2. \(\operatorname{Tor}_i^R(M,N)=0\) for all \(N\) and all \(i>0\).
3. \(\operatorname{Tor}_1^R(M,N)=0\) for all \(N\).
4. \(\operatorname{Tor}_1^R(M,R/I)=0\) for every finitely generated ideal \(I\).
5. The multiplication map \(I\otimes_R M\to M\) is injective for every finitely generated ideal \(I\).

In conditions (4) and (5), one may equally test all ideals.

**Proof.** If \(M\) is flat, tensoring a free resolution of \(N\) with \(M\) leaves it exact in positive degrees. Balance of Tor then gives (2). The implications (2) to (3) to (4) are immediate. Applying (1) to \(0\to I\to R\to R/I\to0\), and using \(\operatorname{Tor}_1^R(M,R)=0\), identifies \(\operatorname{Tor}_1^R(M,R/I)\) with the kernel of \(I\otimes_R M\to M\). Thus (4) and (5) are equivalent. Flatness directly implies the all-ideal versions. It remains to prove (5) implies flatness.

First the injection test extends to any ideal \(I\). A tensor in \(I\otimes_R M\) is a finite sum \(\sum_j a_j\otimes m_j\), and therefore comes from \(J\otimes_R M\) for the finitely generated ideal \(J=(a_j)\subset I\). If it maps to zero in \(M\), that representing tensor is zero by (5), so the original tensor is zero.

Next prove that \(K\otimes_R M\to R^n\otimes_R M\) is injective for every submodule \(K\subset R^n\), by induction on \(n\). For \(n=1\), this is the all-ideal test; for \(n=0\) it is empty. For larger \(n\), project \(K\) onto the last coordinate, obtaining an ideal \(I\), with kernel \(K'\subset R^{n-1}\). The sequence

\[
K'\otimes_R M\longrightarrow K\otimes_R M
\longrightarrow I\otimes_R M\longrightarrow0
\]

is right exact. A tensor in \(K\otimes_R M\) whose image in \(M^n\) is zero maps to zero in \(I\otimes_R M\), since the latter embeds in the last copy of \(M\). Lift it to \(K'\otimes_R M\). Its image in \(M^{n-1}\) is zero, so induction makes the lift zero, proving the claim.

For an arbitrary free module \(F=\bigoplus_{j\in J}R\), a finite tensor from a submodule \(K\subset F\) uses only finitely many elements of \(K\), whose coordinates lie in some finite direct summand \(F_0\). It comes from \((K\cap F_0)\otimes_R M\). If its image in \(F\otimes_R M\) is zero, its image in \(F_0\otimes_R M\) is zero, since \(F_0\) is a direct summand. The finite-rank case makes the tensor zero. Thus all submodules of free modules pass the injection test.

Finally, for any inclusion \(A\subset B\), take a free surjection \(F\to B\), let \(K\) be its kernel and \(L\) the inverse image of \(A\). Then \(K\subset L\subset F\), \(A=L/K\), and \(B=F/K\). We have just proved that \(K\otimes M\) and \(L\otimes M\) embed in \(F\otimes M\), compatibly with their inclusions. Right exactness identifies the induced map \(A\otimes M\to B\otimes M\) with the injection of their respective quotients by the same submodule \(K\otimes M\). Every injection is therefore preserved, and \(M\) is flat. \(\square\)

No finiteness of \(M\), no finite presentation of \(I\), and no Noetherian hypothesis on \(R\) entered this proof.

## 3. Stability and localization

**Proposition 3.1.** Free modules, projective modules, direct sums of flat modules and direct summands of flat modules are flat. Filtered colimits of flat modules are flat.

**Proof.** Tensoring with a free module is taking a direct sum of copies of the given module, which preserves injections. Tensor commutes with direct sums, proving the sum assertion. If \(M\oplus P\) is flat, tensoring an injection with this sum gives an injective map whose \(M\)-component is injective; this proves the summand assertion. Projective modules are direct summands of free modules, so are flat.

For a filtered diagram \((M_\lambda)\), tensor commutes with its colimit by the universal property of tensor products. To see preservation of an injection \(A\to B\), represent any element of \(\varinjlim(A\otimes M_\lambda)\) at one stage. If its image in \(\varinjlim(B\otimes M_\lambda)\) is zero, that image becomes zero after a transition to a later stage. There flatness makes its preimage zero as well, so the colimit map is injective. We used the elementary filtered-colimit rule: a finite list of representatives and equalities can be brought to a common object; an equality in the colimit holds after a further transition. This rule follows directly from the finite relations defining the colimit, with filteredness also equalizing parallel transition maps. Thus the argument applies to filtered diagrams, and in particular to directed systems. \(\square\)

**Proposition 3.2 (base change and composition).** If \(M\) is flat over \(R\) and \(R\to A\) is any ring map, then \(A\otimes_R M\) is flat over \(A\). If \(A\) is flat over \(R\) and \(P\) is flat over \(A\), then \(P\) is flat over \(R\).

**Proof.** For an \(A\)-module \(N\), the natural identification

\[
N\otimes_A(A\otimes_R M)\simeq N\otimes_R M
\]

transfers exactness from \(R\)-modules to \(A\)-modules. For composition, first apply \(A\otimes_R-\) to an exact sequence, then apply \(P\otimes_A-\). The identification \(P\otimes_A(A\otimes_R N)\simeq P\otimes_R N\) proves the result. Taking \(P\) to be an algebra proves composition of flat ring maps. \(\square\)

**Theorem 3.3 (flatness is local).** For a multiplicative set \(S\subset R\), \(S^{-1}R\) is flat over \(R\). For any \(R\)-module \(M\),

\[
M\text{ is flat over }R
\quad\Longleftrightarrow\quad
M_{\mathfrak p}\text{ is flat over }R_{\mathfrak p}
\text{ for every prime }\mathfrak p.
\]

It suffices to test maximal ideals.

**Proof.** Localization is exact and equals tensoring with \(S^{-1}R\), by Theorem 2.1 and Proposition 1.3 of the localization lesson; hence this algebra is flat. If \(M\) is flat, its localizations are flat over their localized rings by base change. Conversely suppose all \(M_{\mathfrak m}\) are flat over \(R_{\mathfrak m}\). For any inclusion \(A\subset B\), let \(K\) be the kernel of \(A\otimes_R M\to B\otimes_R M\). Exactness and the tensor-localization identity identify \(K_{\mathfrak m}\) with the kernel of

\[
A_{\mathfrak m}\otimes_{R_{\mathfrak m}}M_{\mathfrak m}
\longrightarrow B_{\mathfrak m}\otimes_{R_{\mathfrak m}}M_{\mathfrak m},
\]

which is zero by the hypothesis. Local detection makes \(K=0\). Thus \(M\) is flat. Testing all primes includes testing maximal ideals, completing both equivalences. \(\square\)

A useful related fact is that an \(S^{-1}R\)-module is flat over \(R\) exactly when it is flat over \(S^{-1}R\). One direction is composition with the flat localization. For the other, a sequence of localized-ring modules is also a sequence of \(R\)-modules, and tensor over \(R\) with such a module agrees with tensor over \(S^{-1}R\), since every \(s\in S\) already acts invertibly.

The local test concerns modules over the local rings. It is not a test on residue-field fibres alone: every \(M\otimes_R\kappa(\mathfrak p)\) is a vector space and hence flat over its residue field, whatever \(M\) is. For example, this observation applies to \(\mathbb Z/2\), which is not flat over \(\mathbb Z\).

## 4. Domains where torsion is the whole obstruction

For a domain \(R\), an \(R\)-module is **torsion-free** if \(am=0\) with \(a\ne0\) implies \(m=0\).

**Theorem 4.1.** Over a principal ideal domain, a module is flat if and only if it is torsion-free. The same holds over a valuation domain, meaning a domain whose principal ideals are linearly ordered by inclusion.

**Proof.** In any domain, \(0\to R\xrightarrow{a}R\) is injective for \(a\ne0\); a flat module preserves this injection, so is torsion-free. Conversely, in a principal ideal domain every ideal is \((a)\). For \(a\ne0\), the isomorphism \(R\to(a)\), \(r\mapsto ar\), identifies \((a)\otimes_R M\to M\) with multiplication by \(a\) on \(M\), which is injective for a torsion-free module. The zero ideal presents no condition. Theorem 2.1 proves flatness.

In a valuation domain, any finitely generated ideal is principal: of the finitely many principal ideals of its generators, choose the largest. The same argument therefore verifies the finitely generated ideal test, again giving flatness. \(\square\)

For completeness, a **Dedekind domain** here means a Noetherian normal domain of dimension at most one, allowing a field. Each localization at a nonzero maximal ideal is a discrete valuation ring [Stacks, Tag 034X]. Here is the local argument, needed for the flatness conclusion.

Let \((A,\mathfrak m)\) be a one-dimensional Noetherian normal local domain. Choose \(0\ne x\in\mathfrak m\). The only prime containing \((x)\) is \(\mathfrak m\), so a power of \(\mathfrak m\) lies in \((x)\). Choose the least \(n\ge1\) with this property and \(y\in\mathfrak m^{n-1}\setminus(x)\). Then \(t=y/x\notin A\), but \(t\mathfrak m\subset A\). If \(t\mathfrak m\subset\mathfrak m\), write multiplication by \(t\) on a finite list of generators of the nonzero ideal \(\mathfrak m\) as a matrix over \(A\). The adjugate identity makes its monic characteristic polynomial annihilate that ideal, hence vanish at \(t\) in the fraction field. Normality would put \(t\) in \(A\), a contradiction. Thus \(t\mathfrak m\) contains a unit, and equals \(A\). Consequently \(\mathfrak m=t^{-1}A=(\pi)\). Krull intersection for the finite module \(A\), proved in the Noetherian lesson, gives \(\bigcap_n\mathfrak m^n=0\). Each nonzero element is therefore \(u\pi^v\), with \(u\) a unit; choosing the least valuation in a nonzero ideal shows that every ideal is a power of \((\pi)\). This is the DVR characterization and also makes \(A\) a valuation domain. Normality localizes: if a fraction is integral over \(A_s\), multiplying it by a sufficiently high power of \(s\) clears the coefficients of its monic equation and makes it integral over \(A\). The same finite-denominator argument works for an arbitrary localization. A maximal ideal equal to zero instead makes the domain a field.

**Corollary 4.2.** A module over a Dedekind domain is flat if and only if it is torsion-free.

**Proof.** Flatness implies torsion-freeness as above. If \(M\) is torsion-free, so is \(M_{\mathfrak m}\) over \(R_{\mathfrak m}\): if \((a/s)(m/t)=0\) with \(a/s\ne0\), the localization equality criterion gives \(uam=0\) for some nonzero \(u\notin\mathfrak m\); the domain property and torsion-freeness force \(m=0\). Every such localization is therefore flat by Theorem 4.1, or by the vector-space case at a field. Theorem 3.3 gives flatness over \(R\). \(\square\)

## 5. Relations and finite free bases

A relation \(\sum_{i=1}^n a_i x_i=0\), with \(a_i\in R\) and \(x_i\in M\), is called **trivial** in the equational criterion if there are finitely many \(y_j\in M\) and coefficients \(b_{ij}\in R\) such that

\[
x_i=\sum_j b_{ij}y_j\quad\text{for every }i,
\qquad
\sum_i a_i b_{ij}=0\quad\text{for every }j.
\tag{3}
\]

The word describes the origin of the relation, not whether its coefficients vanish: the columns of \(B=(b_{ij})\) are relations among the coefficients in the ring itself.

**Theorem 5.1 (equational criterion).** An \(R\)-module is flat if and only if every finite relation has a factorization (3).

**Proof.** For a relation, let \(I=(a_1,\ldots,a_n)\) and \(K=\ker(R^n\to I)\), where the map sends \(e_i\) to \(a_i\). If \(M\) is flat, \(I\otimes M\to M\) is injective, so \(\sum_i a_i\otimes x_i=0\). Right exactness applied to \(K\to R^n\to I\to0\) says that \(\sum_i e_i\otimes x_i\) comes from \(K\otimes M\). Write a preimage as \(\sum_j v_j\otimes y_j\), and write \(v_j=\sum_i b_{ij}e_i\). Membership of \(v_j\) in \(K\) gives the second equality in (3); comparison of coordinates gives the first.

Conversely, a kernel tensor in \(I\otimes M\to M\) is a finite sum \(z=\sum_i a_i\otimes x_i\) with \(\sum_i a_ix_i=0\). Applying (3) yields

\[
z=\sum_{i,j}a_i\otimes b_{ij}y_j
=\sum_j\left(\sum_i a_i b_{ij}\right)\otimes y_j=0.
\]

Thus the ideal injection test holds, and Theorem 2.1 proves flatness. \(\square\)

**Theorem 5.2 (finite flat over a local ring).** If \((R,\mathfrak m,\kappa)\) is local and \(M\) is finite and flat, then \(M\) is finite free. Finite presentation is not assumed.

**Proof.** Lift a basis \(\bar x_1,\ldots,\bar x_r\) of \(M/\mathfrak mM\) to \(M\). Nakayama makes \(x_1,\ldots,x_r\) generators. If \(r=0\), it gives \(M=0\), which is free of rank zero. Otherwise take any relation \(\sum_i a_ix_i=0\). The equational criterion provides \(x=By\), where \(x,y\) are columns, \(B\) is an \(r\)-by-\(s\) matrix and the coefficient row \(a\) satisfies \(aB=0\). Since the \(x_i\) generate, write \(y=Cx\), with \(C\) an \(s\)-by-\(r\) matrix. Hence \(x=BCx\).

The residue classes \(\bar x_i\) are a basis, so this last equality implies

\[
BC\equiv I_r\pmod{\mathfrak m}.
\]

The determinant of \(BC\) is therefore a unit of the local ring, and the adjugate formula makes \(BC\) invertible. But \(aBC=0\), so \(a=0\). Every relation is zero, and the generators form a free basis. The relation module never needed finitely many generators. \(\square\)

**Theorem 5.3 (finite presentation gives projectivity).** A finitely presented flat \(R\)-module is finite projective and is free of finite rank on an open neighborhood of each prime of \(R\).

**Proof.** Choose a finite presentation \(R^t\to F=R^n\xrightarrow{\pi}M\to0\). Let \(x_i=\pi(e_i)\), and write the chosen generators of \(\ker\pi\) as \(k_\ell=\sum_i a_{\ell i}e_i\), for \(1\leq\ell\leq t\). Thus each row of \(A=(a_{\ell i})\) is a relation on the column \(x\).

We can trivialize all these finitely many relations simultaneously:

\[
x=By,
\qquad AB=0.
\tag{4}
\]

To see this, apply Theorem 5.1 to the first row, giving \(x=B_1y^{(1)}\) with that row times \(B_1\) zero. The second row now gives a relation on \(y^{(1)}\); factor that relation through \(B_2\), and replace \(B_1\) by \(B_1B_2\). The first row remains zero, and the second becomes zero. Repeating for the finite list gives (4). If there are no rows, use \(B=I_n\) and \(y=x\).

Lift each \(y_j\) to \(z_j\in F\). Define \(h:F\to F\) by \(h(e_i)=\sum_j b_{ij}z_j\). Then \(\pi h(e_i)=x_i\), so \(\pi h=\pi\); and

\[
h(k_\ell)=\sum_j\left(\sum_i a_{\ell i}b_{ij}\right)z_j=0.
\]

Since the \(k_\ell\) generate the kernel, \(h\) induces \(\sigma:M\to F\) with \(\pi\sigma=\mathrm{id}_M\). Thus \(M\) is a direct summand of the finite free module \(F\), proving finite projectivity.

Now fix \(\mathfrak p\). By localization and Theorem 5.2, \(M_{\mathfrak p}\) is free of some finite rank \(r\). Choose \(m_1,\ldots,m_r\in M\) whose localized images are a basis: clear the denominators of a basis and multiply its members by the resulting units. The cokernel of \(R^r\to M\), \(e_i\mapsto m_i\), is finite and vanishes at \(\mathfrak p\). The localization equality criterion, applied to finitely many generators, gives \(f\notin\mathfrak p\) for which this map is surjective over \(R_f\). Since \(M_f\) is projective, the surjection splits. Its kernel is a direct summand of \(R_f^r\), so is finite. That kernel also vanishes at \(\mathfrak p\); kill its finite list of generators by another element \(g\notin\mathfrak p\). Over \(R_{fg}\) the map is an isomorphism. Therefore \(M\) has a free basis throughout \(D(fg)\), an actual open neighborhood. \(\square\)

Conversely, a finite projective module is flat by Proposition 3.1 and finitely presented: in a splitting \(R^n=M\oplus K\), the complementary summand \(K\) is finite. The finite presentation hypothesis in Theorem 5.3 is essential; Section 7 gives a finite flat counterexample. Free stalks alone also need not supply open free neighborhoods without appropriate finiteness, as the localization lesson's examples show.

## 6. Exact sequences and prime lifting

**Theorem 6.1.** In a short exact sequence \(0\to M'\to M\to M''\to0\) with \(M''\) flat, tensoring with any module \(N\) gives a short exact sequence. Moreover \(M'\) is flat if and only if \(M\) is flat.

**Proof.** The Tor long exact sequence in the first variable ends in

\[
\operatorname{Tor}_1^R(M'',N)\longrightarrow M'\otimes_R N
\longrightarrow M\otimes_R N\longrightarrow M''\otimes_R N\longrightarrow0.
\]

Its first term is zero, giving exactness also at the left. If \(M'\) is flat, the segment \(\operatorname{Tor}_1(M',N)\to\operatorname{Tor}_1(M,N)\to\operatorname{Tor}_1(M'',N)\) makes the middle term zero for every \(N\), so \(M\) is flat. Conversely, if \(M\) is flat, use \(\operatorname{Tor}_2(M'',N)\to\operatorname{Tor}_1(M',N)\to\operatorname{Tor}_1(M,N)\). Both outer terms vanish, so \(M'\) is flat. \(\square\)

A flat module or algebra is **faithfully flat** if tensoring with it sends a nonzero module to a nonzero module. For flat modules this is equivalent to reflecting exactness: flat tensoring preserves kernels, images and their quotients, hence the homology of a complex, and the stated detection property makes vanishing of that homology equivalent before and after tensoring. The next lesson develops faithful flatness systematically. We need one local case now.

**Lemma 6.2.** A flat local homomorphism \((A,\mathfrak m)\to(B,\mathfrak n)\) is faithfully flat.

**Proof.** For a nonzero \(A\)-module \(N\), choose \(u\ne0\). Its cyclic submodule is \(Au\simeq A/I\) for a proper ideal \(I\subset\mathfrak m\). Flatness embeds \((A/I)\otimes_A B=B/IB\) in \(N\otimes_A B\). Locality gives \(IB\subset\mathfrak mB\subset\mathfrak n\), so \(B/IB\ne0\). Thus the latter tensor module is nonzero. \(\square\)

**Theorem 6.3 (flat maps satisfy going down).** Let \(R\to S\) be flat, let \(\mathfrak p\subset\mathfrak p'\) be primes of \(R\), and let \(\mathfrak q'\subset S\) contract to \(\mathfrak p'\). There is a prime \(\mathfrak q\subset\mathfrak q'\) contracting to \(\mathfrak p\).

**Proof.** Put \(A=R_{\mathfrak p'}\), \(B=S_{\mathfrak q'}\). The map \(A\to B\) is local. It is flat: \(S_{\mathfrak q'}\) is flat over \(S\) and hence over \(R\) by composition, and as an \(A\)-module it is flat by the localized-ring observation after Theorem 3.3. Lemma 6.2 makes it faithfully flat.

The ideal \(\mathfrak r=\mathfrak pA\) is prime by localization correspondence. Its residue field \(\kappa_A(\mathfrak r)\) is a nonzero \(A\)-module, so

\[
B\otimes_A\kappa_A(\mathfrak r)\ne0.
\]

This nonzero ring has a maximal ideal, hence a prime. The fibre correspondence, Theorem 3.2 of the localization lesson, gives a prime of \(B\) over \(\mathfrak r\). Contract it to \(S\); the result is contained in \(\mathfrak q'\), and its contraction to \(R\) is \(\mathfrak p\), by prime correspondence for \(R_{\mathfrak p'}\). This proves going down. No integrality or Noetherianity was assumed. \(\square\)

**Theorem 6.4 (Lazard).** An \(R\)-module is flat if and only if it is a filtered colimit of finite free \(R\)-modules [Stacks, Tag 058G]. The transition maps need not be inclusions.

**Proof.** Proposition 3.1 proves one direction. Suppose \(M\) is flat. The equational criterion proved in Theorem 5.1 implies the following factorization property: if \(f:R^n\to M\) and \(x\in\ker f\), there are maps \(h:R^n\to R^r\), \(g:R^r\to M\) with \(f=gh\) and \(h(x)=0\). Indeed the coefficients of \(x\) give one relation on the images of the basis; the matrix and elements supplied by the criterion are exactly \(h,g\). Given finitely many kernel elements, kill them successively. At the next step apply the property to \(g\) and the image of the next element; composition still kills all earlier ones. Thus every map from a finitely presented module to \(M\) factors through a finite free module: apply this procedure to a finite list of relations in its presentation.

Take the free module \(R^{(I)}\) on \(I=M\times\mathbb Z\), mapping \((m,j)\) to \(m\), and write its kernel as \(K\). Consider pairs \((J,N)\), where \(J\subset I\) is finite and \(N\subset K\cap R^J\) is finitely generated. Order them by inclusion in both entries. This is a directed set: take the union of two finite sets and the sum of the two relation modules. Put \(M_{J,N}=R^J/N\). Their colimit is \(M\): every element is represented by a basis vector; every finite relation becomes zero at the pair containing its coordinates and the submodule it generates.

For each pair, factor \(M_{J,N}\to M\) through a finite free \(F\), say \(M_{J,N}\xrightarrow{h}F\xrightarrow{g}M\). If \(b_1,\ldots,b_r\) is a basis of \(F\), choose distinct indices outside \(J\) mapping to \(g(b_1),\ldots,g(b_r)\). Infinitely many copies of each element in \(I\) make this possible even when some images coincide. Enlarge \(J\) by these indices to \(J'\), and map \(R^{J'}\to F\) by \(h\) on the old coordinates and by the selected basis on the new ones. Its kernel \(N'\) lies in \(K\), contains \(N\), and is finitely generated: the surjection splits, so its kernel is the image of the finite free module under the complementary projection. Hence \((J',N')\) is a larger pair with \(M_{J',N'}\cong F\).

The pairs whose quotients are finite free are therefore cofinal. They form a directed subset, since a common upper bound in the whole directed set can be enlarged to another free pair. Restricting to a cofinal subset does not change the colimit: any finite set of representatives and relations reaches such an upper pair. This proves the theorem for arbitrary rings and modules. \(\square\)

## 7. Four worked tests

**Flat need not be projective.** The localization \(\mathbb Q\) is flat over \(\mathbb Z\). Every homomorphism \(\mathbb Q\to\mathbb Z\) is zero: the image of \(1\) is divisible by every positive integer, so is zero, and then \(b\varphi(a/b)=a\varphi(1)=0\) forces the remaining images to vanish. Thus every map from \(\mathbb Q\) to any free abelian group is zero, since all coordinate maps are zero. If \(\mathbb Q\) were projective, a free surjection onto it would split, giving a nonzero map into a free group, a contradiction. By contrast \(\mathbb Z/n\), for \(n\geq2\), is not flat: multiplication by the nonzero integer \(n\) kills its nonzero class of \(1\).

**A component trapped over a point.** In \(B=k[X,Y]/(XY)\), the class of \(Y\) is nonzero, as reduction modulo \(X\) shows, and is killed by \(X\). Therefore \(k[X]\to B\) is not flat. In \(C=k[T,X,Y]/(XY-T)\), substitution \(T=XY\) identifies \(C\) with the domain \(k[X,Y]\). The map \(k[T]\to C\) is injective, since the monomials \((XY)^i\) are linearly independent. Hence \(C\) is torsion-free, and flat over the principal ideal domain \(k[T]\). Its fibre at \(T=0\) has two axes, while its generic fibre is \(k(T)[X,X^{-1}]\), obtained by \(Y=T/X\). Reducibility of a special fibre is therefore compatible with flatness; the first example fails through torsion.

**The Koszul calculation at the origin.** Let \(R=k[X,Y]\) and \(k=R/(X,Y)\). The complex

\[
0\longrightarrow R\xrightarrow{\binom{-Y}{X}}R^2
\xrightarrow{(X\ \ Y)}R\longrightarrow k\longrightarrow0
\tag{5}
\]

is exact. The left map is injective because \(R\) is a domain. For \(Xu+Yv=0\), reduce modulo \(X\): multiplication by \(Y\) is injective in \(k[Y]\), so \(v=Xw\). Then \(u=-Yw\), giving exactly the image of the left map. The right cokernel is \(k\). Thus (5), the two-variable Koszul resolution, computes Tor. Tensor with \(k\); both differentials become zero, giving

\[
\operatorname{Tor}_i^{k[X,Y]}(k,k)=
\begin{cases}k,&i=0,2,\\k^2,&i=1,\\0,&i>2.\end{cases}
\]

**Finite flat can still fail projectivity.** Put \(R=C^\infty(\mathbb R)\), and let \(I\) consist of functions vanishing on some neighborhood of zero. This is a proper nonzero ideal. We claim the cyclic module \(M=R/I\) is flat.

For every \(a\in I\), choose \(\epsilon>0\) for which \(a=0\) on \(|x|<\epsilon\). There is a smooth function \(h\) equal to zero on \(|x|\leq\epsilon/2\) and to one on \(|x|\geq\epsilon\). Then \(h\in I\) and \(ha=a\). One explicit construction is

\[
\eta(u)=\begin{cases}e^{-1/u},&u>0,\\0,&u\leq0,\end{cases}
\qquad \theta(u)=\frac{\eta(u)}{\eta(u)+\eta(1-u)},
\qquad h(x)=\theta\left(\frac{x^2-\epsilon^2/4}{3\epsilon^2/4}\right).
\]

The denominator defining \(\theta\) is everywhere positive. Smoothness of \(\eta\) at zero follows because each one-sided derivative is an exponential times a polynomial in \(1/u\), tending to zero; it and all derivatives match the zero function on the other side. This verifies the cutoff properties.

For every ideal \(J\subset R\), an element \(a\in J\cap I\) satisfies \(a=ha\in IJ\) by this construction. The reverse inclusion is automatic, so \(J\cap I=IJ\). Since \(J\otimes_R(R/I)=J/IJ\), the kernel of its map to \(R/I\) is \((J\cap I)/IJ=0\). Theorem 2.1 proves flatness.

If the cyclic quotient \(R/I\) were projective, the surjection \(R\to R/I\) would split. Its kernel would be the image of an idempotent endomorphism of the rank-one free module \(R\), hence \(I=eR\) for an idempotent function \(e\). A continuous idempotent on the connected real line has values in \(\{0,1\}\) and is constant. This would give \(I=0\) or \(I=R\), both impossible. Thus \(M\) is finite and flat but not projective, and Theorem 5.3 shows it is not finitely presented. The quotient retains only the germ of a smooth function at zero, but this global module need not have a global splitting.

## 8. Exercises

**Exercise 8.1 (easy: a principal ideal test).** Over a principal ideal domain, prove that flatness is equivalent to torsion-freeness for arbitrary modules. Explain why the conclusion need not mean freeness when the module is not finite.

**Exercise 8.2 (easy: two localization charts).** For \(f,g\in R\), prove that \(R\to R_f\times R_g\) is flat, and is faithfully flat exactly when \(D(f)\cup D(g)=\operatorname{Spec}R\). Include the empty-spectrum case.

**Exercise 8.3 (medium: the two axes).** Let \(R=k[X,Y]\). Compute every \(\operatorname{Tor}_i^R(R/(X),R/(Y))\) and interpret the answer as an intersection of the two coordinate axes. Also derive \(\operatorname{Tor}_1^R(R/I,R/J)\simeq(I\cap J)/IJ\) for arbitrary ideals \(I,J\subset R\).

**Exercise 8.4 (medium: constructing a splitting).** Use the equational criterion to prove that a finitely presented flat module is projective. Starting with a finite presentation, specify a splitting map and show that it respects every relation, rather than only one chosen relation.

**Exercise 8.5 (medium: a monic equation and a torsion equation).** Show that \(k[X]\to k[X,Y]/(Y^2-X)\) is flat. Give an explicit module basis. Show that \(k[X]\to k[X,Y]/(XY)\) is not flat by locating a nonzero tensor obstruction.

**Exercise 8.6 (hard: no finite-presentation assumption).** Prove that a finite flat module over a local ring is free. Your proof must apply even when the kernel of an initial finite free surjection has not been shown finitely generated.

## 9. Solutions

**Solution 8.1.** For \(a\ne0\), a flat module preserves the injection \(R\xrightarrow{a}R\), so has no \(a\)-torsion. Conversely every nonzero ideal is \((a)\simeq R\). Under that isomorphism the map \((a)\otimes_R M\to M\) is multiplication by \(a\), hence injective for a torsion-free module. The zero ideal also passes the test, so Theorem 2.1 gives flatness. The module \(\mathbb Q\) over the principal ideal domain \(\mathbb Z\) is torsion-free and flat but is not even projective, as Section 7 proves, so is not free. Finite generation is not needed for the equivalence with torsion-freeness.

**Solution 8.2.** As an \(R\)-module the finite product is \(R_f\oplus R_g\). Each summand is flat, so the product is flat. For any \(N\), tensoring gives \(N_f\oplus N_g\). Suppose the two opens cover the spectrum and this tensor is zero. At every maximal ideal \(\mathfrak m\), either \(f\) or \(g\) is a unit in \(R_{\mathfrak m}\). Localizing the corresponding zero module \(N_f\) or \(N_g\) at \(\mathfrak m\) gives \(N_{\mathfrak m}=0\). Local detection gives \(N=0\), so the map is faithfully flat.

Conversely, if \(\mathfrak p\) lies outside both opens, then \(f,g\in\mathfrak p\). The nonzero module \(\kappa(\mathfrak p)\) has both localizations zero, since both elements act as zero and are made invertible. Its tensor with the product is zero, so faithful flatness fails. If \(R=0\), its spectrum is empty, the cover condition holds, and its only module is zero; the detection condition is vacuous, giving the same equivalence. Equivalently, the cover condition is \((f,g)=R\): a proper ideal would lie in a maximal ideal outside both opens.

**Solution 8.3.** Resolve \(R/(X)\) by \(0\to R\xrightarrow{X}R\to R/(X)\to0\). After tensoring with \(R/(Y)=k[X]\), multiplication by \(X\) is injective. Thus

\[
\operatorname{Tor}_0^R(R/(X),R/(Y))=k,
\qquad \operatorname{Tor}_i^R(R/(X),R/(Y))=0\quad(i>0).
\]

The ordinary tensor product is the coordinate ring of their intersection, the reduced origin. There is no higher Tor obstruction for these two independent equations.

For general ideals use \(0\to I\to R\to R/I\to0\). The long exact sequence, together with \(\operatorname{Tor}_1^R(R,R/J)=0\), identifies \(\operatorname{Tor}_1^R(R/I,R/J)\) with the kernel of \(I\otimes_R(R/J)\to R/J\). The source is \(I/JI\), and the kernel is \((I\cap J)/JI\), proving the formula. For the axes, \((X)\cap(Y)=(XY)\): if \(Xu\in(Y)\), reduction modulo \(Y\) makes \(X\bar u=0\) in the domain \(k[X]\), hence \(u\in(Y)\). Thus the intersection of their ideals equals their product, explaining the vanishing. In comparison, intersecting \((X)\) with itself gives \((X)/(X^2)\), a nonzero first Tor group.

**Solution 8.4.** Let \(F=R^n\to M\) have a kernel generated by the finite rows \(k_\ell=\sum_i a_{\ell i}e_i\), and set \(x_i\) equal to the image of \(e_i\). Successive applications of the equational criterion give a factorization \(x=By\) with every row of \(AB\) zero. At each application, replace the current column of module elements by its factorization; multiplying its coefficient matrix on the right preserves all previously zero rows. There are finitely many rows, so this process terminates. Lift the final \(y_j\) to elements \(z_j\in F\). Define \(h(e_i)=\sum_j b_{ij}z_j\). Its image in \(M\) is \(x_i\), and \(h(k_\ell)=\sum_j(\sum_i a_{\ell i}b_{ij})z_j=0\) for every kernel generator. It therefore annihilates the whole kernel and induces \(\sigma:M\to F\). The equality of images says that the composite \(M\xrightarrow{\sigma}F\to M\) is the identity. Thus \(M\) is a direct summand of a free module and is projective. Finite presentation supplies the finite list of rows; trivializing a single relation would not suffice.

**Solution 8.5.** Monic division by \(Y^2-X\) in \(k[X][Y]\) gives a representative \(a(X)+b(X)Y\) for every class. It is unique: a nonzero multiple of the monic polynomial has \(Y\)-degree at least two, so cannot equal a nonzero polynomial of \(Y\)-degree at most one. Thus \(1,Y\) are a free \(k[X]\)-module basis, proving flatness.

For \(B=k[X,Y]/(XY)\), reduce modulo \(X\) to see that the class \(\bar Y\) is nonzero. Tensor the injective map \(k[X]\xrightarrow{X}k[X]\) with \(B\). The resulting multiplication map \(B\xrightarrow{X}B\) kills \(\bar Y\), so is not injective. Equivalently, identify \((X)\otimes_{k[X]}B\) with \(B\) using \(k[X]\simeq(X)\); the nonzero tensor \(X\otimes\bar Y\) maps to \(X\bar Y=0\). This is precisely a failure of the ideal criterion.

**Solution 8.6.** Let \((R,\mathfrak m)\) be local, and lift a residue-field basis of \(M/\mathfrak mM\) to \(x_1,\ldots,x_r\). These generate by Nakayama; if \(r=0\), then \(M=0\). For any relation with coefficient row \(a\), flatness gives \(x=By\) and \(aB=0\). Express the finite list \(y\) in the generating list \(x\), giving \(y=Cx\). Then \(x=BCx\), and independence modulo \(\mathfrak m\) forces \(BC\equiv I_r\pmod{\mathfrak m}\). Its determinant is a unit, so \(BC\) is invertible. The equality \(aBC=0\) now gives \(a=0\). Every relation vanishes, so the surjection \(R^r\to M\) is an isomorphism. The proof treats each relation individually and never applies Nakayama to an unproved finite relation module.

## Proof dependencies and sources

The independence, balance and symmetry of Tor and its natural long exact sequences are proved in *Resolutions, Tor and Ext*, Sections 1–3. Section 4 here proves the local DVR fact used for Dedekind flatness, and Theorem 6.4 gives both directions of Lazard's theorem. The earlier localization and Noetherian results are used at the locators in the text.

The proof of Lazard's theorem (Theorem 6.4) follows the finite-relation and cofinal-free-presentation argument of the Stacks Project authors ([algebra chapter at the pinned AI Integrated Stacks Project revision](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L20525), `lemma-flat-factors-free`, `lemma-flat-factors-fp` and `theorem-lazard`). The factorization, finite-generation and cofinality steps are written out here and connected to this lesson's equational criterion.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra. Definition and criteria: [Tag 00HB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#definition-flat), [Tag 00HD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat), [Tag 00HK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-eq), [Tag 00M5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-characterize-flat). Stability: [Tag 00HC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-composition-flat), [Tag 00HI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-base-change), [Tag 05UT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-colimit-flat), [Tag 00HT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-localization).
- The same work, Tor and tensor exactness: [Tag 00LZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-tor-welldefined), [Tag 00M0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-long-exact-sequence-tor), [Tag 00M3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-tor-left-right), [Tag 00HL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-tor-zero), [Tag 00HM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-ses). Finiteness and prime lifting: [Tag 00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-finite-projective), [Tag 00NZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-finite-flat-local), [Tag 00NY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#remark-warning), [Tag 00HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-local-flat-ff), [Tag 00HS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-flat-going-down), [Tag 058G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#theorem-lazard).
- The same work, special domains: [Tag 034X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-characterize-Dedekind), and More on Algebra, [Tag 0539](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#lemma-valuation-ring-torsion-free-flat), [Tag 0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#lemma-dedekind-torsion-free-flat). These links use the AI Integrated Stacks Project English reader described in the course introduction.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 23.1 on Tor, Sections 24.1–24.3 on flatness and its criteria, and Section 24.4 on the Koszul complex. [Author’s public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
- Timothy J. Ford, *Commutative Algebra*, version of 23 September 2026, Chapter 3, Section 7 on flat modules, including the ideal and equational criteria and finitely presented flat modules, and Chapter 9, Section 3 on Tor groups and on Tor and torsion over an integral domain. [Author’s version](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf).

## Licence

The text of this lesson is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The Stacks Project, cited above for the arguments this lesson follows, is distributed by its authors under the GNU FDL 1.2 or later.

# Norms of ideals, the ideal class group, and modules over Dedekind domains

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

An ideal has two kinds of information: the size of its quotient and its obstruction to being principal. These become the ideal norm and the ideal class. The same ideal class also measures whether a module that has a basis at every prime has one basis over the whole ring.

## What this lesson assumes

We use the finite freeness of the ring of integers over \(\mathbf Z\), the determinant definition of the field norm, and the lattice index formula from *Discriminants and integral bases*. We use unique factorization and invertibility of nonzero fractional ideals, localization at a prime, and the Chinese remainder theorem from *Discrete valuation rings and Dedekind domains*. In particular, localization at a nonzero prime is a discrete valuation ring.

For the general module statements, \(A\) is a Dedekind domain and \(F=\operatorname{Frac}(A)\). A fractional ideal always means a nonzero finitely generated \(A\)-submodule of \(F\) with a nonzero common denominator. Our preceding lesson excludes fields from the name Dedekind domain. If that name is taken to include fields, all statements below still hold: the only fractional ideal is \(A\), the class group is trivial, and finitely generated modules are finite dimensional vector spaces. We treat rank zero explicitly.

Basic references are [Milne ANT] and [Stacks]. We give full proofs of the module results, including the torsion classification.

## Counting residue classes

Let \(K\) be a number field and \(A=\mathcal O_K\). For a nonzero integral ideal \(\mathfrak a\), its **absolute norm** is
\[
N\mathfrak a=\#(A/\mathfrak a).
\]
This is finite. Indeed, choose \(0\ne x\in\mathfrak a\). Its monic minimal polynomial over \(\mathbf Q\) has coefficients in \(\mathbf Z\) and a nonzero constant term \(c\). The equation shows that \(c\in xA\subseteq\mathfrak a\). Thus \(A/\mathfrak a\) is a quotient of the finite abelian group \(A/cA\).

The norm of the unit ideal is \(1\). For integral ideals, \(N\mathfrak a=1\) therefore holds exactly when \(\mathfrak a=A\).

**Proposition 4.1.** For nonzero integral ideals \(\mathfrak a,\mathfrak b\) of \(\mathcal O_K\),
\[
N(\mathfrak a\mathfrak b)=N\mathfrak a\,N\mathfrak b.
\]
For every \(0\ne\alpha\in\mathcal O_K\),
\[
N(\alpha\mathcal O_K)=|N_{K/\mathbf Q}(\alpha)|.
\]
There is a unique multiplicative extension of the ideal norm to all nonzero fractional ideals, with values in \(\mathbf Q_{>0}\). The principal-ideal formula then holds for every \(0\ne\alpha\in K\).

**Proof.** Fix a nonzero prime ideal \(\mathfrak p\). For \(j\geq0\), the module
\[
\mathfrak p^j/\mathfrak p^{j+1}
\]
is killed by \(\mathfrak p\), so it is an \(A/\mathfrak p\)-vector space. Every element of \(A\setminus\mathfrak p\) acts invertibly on it: its residue in \(A/\mathfrak p\) is nonzero. Hence localizing this module at \(\mathfrak p\) does not change it. In the discrete valuation ring \(R=A_{\mathfrak p}\), with a uniformizer \(\pi\), its localization is
\[
\pi^jR/\pi^{j+1}R\cong R/\pi R\cong A/\mathfrak p.
\]
Consequently each successive quotient has exactly \(N\mathfrak p\) elements. The filtration of \(A/\mathfrak p^e\) by these \(e\) quotients gives
\[
N(\mathfrak p^e)=(N\mathfrak p)^e.
\]
For \(\mathfrak a=\prod_{\mathfrak p}\mathfrak p^{e_{\mathfrak p}}\), the Chinese remainder theorem gives a product of the quotients \(A/\mathfrak p^{e_{\mathfrak p}}\). Thus
\[
N\mathfrak a=\prod_{\mathfrak p}(N\mathfrak p)^{e_{\mathfrak p}}. \tag{1}
\]
Adding prime exponents proves multiplicativity.

Choose an integral basis of \(A\) over \(\mathbf Z\). Multiplication by \(\alpha\) has an integer matrix in that basis; its image is \(\alpha A\). Since \(\alpha\ne0\), the matrix is nonsingular over \(\mathbf Q\). The lattice index formula says that its image has index equal to the absolute value of its determinant. This determinant is \(N_{K/\mathbf Q}(\alpha)\), proving the second assertion.

Every fractional ideal has a unique factorization with integer, possibly negative, exponents. Formula (1) with these exponents defines the claimed extension. Any multiplicative extension must take these values, since inverses have reciprocal norms. Alternatively, if \(0\ne d\in A\) and \(d\mathfrak a\subseteq A\), then
\[
N\mathfrak a=\frac{N(d\mathfrak a)}{|N_{K/\mathbf Q}(d)|}.
\]
For \(\alpha\in K^\times\), choose a nonzero rational integer \(d\) with \(d\alpha\in A\). Applying the integral formula to \(d\alpha\) and \(d\), and using multiplicativity of the field norm, proves the fractional principal-ideal formula. \(\square\)

If \(\mathfrak b\subseteq\mathfrak a\) are fractional ideals, then their additive index is finite and
\[
[\mathfrak a:\mathfrak b]
=\frac{N\mathfrak b}{N\mathfrak a}
=N(\mathfrak a^{-1}\mathfrak b). \tag{2}
\]
To prove this, multiply both ideals by a common nonzero integer so they are integral. Indices are unchanged by this multiplication. Now use
\([A:\mathfrak b]=[A:\mathfrak a][\mathfrak a:\mathfrak b]\) and Proposition 4.1.

In particular, if \(0\ne\alpha\in\mathfrak a\), then
\[
\mathfrak a=(\alpha)
\quad\Longleftrightarrow\quad
N\mathfrak a=|N_{K/\mathbf Q}(\alpha)|. \tag{3}
\]
Here membership is essential: the equality of two numbers alone does not identify their ideals.

Fractional ideals of norm \(1\) need not be the unit ideal. In \(K=\mathbf Q(\sqrt{-5})\), the element \((2+\sqrt{-5})/3\) has field norm \(1\) and is not integral. Its principal fractional ideal has norm \(1\), but is not \(A\).

## The class of an ideal

The nonzero fractional ideals of a Dedekind domain \(A\) form an abelian group \(\mathcal I(A)\) under multiplication. Its identity is \(A\); its inverses are the ideal inverses established in the previous lesson. The principal fractional ideals form a subgroup
\[
\mathcal P(A)=\{aA\mid a\in F^\times\}.
\]
The **ideal class group** is
\[
\operatorname{Cl}(A)=\mathcal I(A)/\mathcal P(A).
\]
We write \([I]\) for the class of \(I\), so \([I][J]=[IJ]\). For \(A=\mathcal O_K\), write \(\operatorname{Cl}_K\). Its order, when finite, is the **class number** \(h_K\). Its finiteness will be proved in *Finiteness of the class number*.

The class group is trivial exactly when every fractional ideal is principal, equivalently when \(A\) is a principal ideal domain. This follows directly from the quotient definition and from clearing denominators of fractional ideals. The preceding lesson also proves the equivalence with unique factorization of elements.

The numerical norm does not give a function on ideal classes. Multiplying \(I\) by \(aA\) keeps its class and multiplies its norm by \(|N_{K/\mathbf Q}(a)|\).

### An ideal with no generator of the required norm

Put \(s=\sqrt{-5}\) and \(A=\mathbf Z[s]\). The map
\[
A\longrightarrow\mathbf F_2,\qquad a+bs\longmapsto a+b
\]
has kernel \(\mathfrak p=(2,1+s)\), so \(N\mathfrak p=2\). A generator \(\alpha=a+bs\) would have norm \(a^2+5b^2=2\). If \(b\ne0\), that norm is at least \(5\); if \(b=0\), it is a square. No such generator exists.

We know from the previous lesson that \(\mathfrak p^2=(2)\). Thus \([\mathfrak p]\) has order exactly \(2\). This does not yet determine the order of the entire class group.

## Why ideals are projective

We will use a finiteness consequence of Noetherianity. Every submodule of \(A^m\) is finitely generated: induct on \(m\), project a submodule to the last coordinate, choose finitely many lifts of generators of the resulting ideal, and combine them with generators of the kernel, a submodule of \(A^{m-1}\). Every finitely generated module is a quotient of some \(A^m\). The inverse image of a submodule is therefore finitely generated, and its image generates the submodule. Thus submodules of finitely generated \(A\)-modules are finitely generated.

An \(A\)-module \(P\) is **projective** if a map from \(P\) to a quotient module can always be lifted to the module being quotiented. A direct summand of a free module is projective: lift the map on the free module by lifting each basis vector, and then restrict to the summand. Conversely, for a finitely generated projective module, a surjection from a finite free module splits by lifting its identity. Thus, in the finitely generated case, projective means a direct summand of a finite free module.

Every fractional ideal \(I\) is projective. To see this without a local-to-global projectivity theorem, use \(II^{-1}=A\). There are finitely many \(x_i\in I\), \(y_i\in I^{-1}\) such that
\[
\sum_{i=1}^m x_i y_i=1.
\]
Define
\[
q:A^m\longrightarrow I,\quad (a_i)\longmapsto\sum_i a_i x_i,
\qquad
j:I\longrightarrow A^m,\quad z\longmapsto(y_i z)_i.
\]
All \(y_i z\) belong to \(A\), and \(qj=\operatorname{id}_I\). Hence \(I\) is a direct summand of \(A^m\).

For a finitely generated module \(M\), its **rank** is
\[
\operatorname{rank}_A M=\dim_F(F\otimes_A M).
\]
If \(M\) is torsion-free, the map \(M\to F\otimes_A M\) is injective: an element that becomes zero is annihilated by some nonzero element of \(A\). A torsion-free module of rank zero is therefore zero.

**Lemma.** Every finitely generated torsion-free \(A\)-module of positive rank is a direct sum of fractional ideals. In particular, it is projective.

**Proof.** View \(M\) inside its finite dimensional \(F\)-vector space. Choose an \(F\)-linear functional \(\ell:F\otimes_A M\to F\) that is nonzero on \(M\). Its image \(I=\ell(M)\) is a fractional ideal: it is nonzero and finitely generated, and finitely many elements of \(F\) have a common denominator. The exact sequence
\[
0\longrightarrow M_1\longrightarrow M\overset{\ell}{\longrightarrow}I\longrightarrow0
\]
splits because \(I\) is projective. The kernel \(M_1\) is finitely generated because \(A\) is Noetherian, and is torsion-free. After tensoring with \(F\), the functional is surjective, so its kernel has rank one less than \(M\). Induction on rank, with the rank-zero case just proved, gives
\[
M\cong I_1\oplus\cdots\oplus I_r.
\]
A finite direct sum of projective modules is projective, by lifting the maps on each summand. \(\square\)

The proof uses the decreasing rank to terminate. It does not require a principal ideal domain or an assumed global basis.

## Combining two ideal summands

**Proposition 4.2.** For fractional ideals \(I,J\) of a Dedekind domain,
\[
I\oplus J\cong A\oplus IJ
\]
as \(A\)-modules.

**Proof.** First suppose \(I,J\) are integral and \(I+J=A\). Choose \(u\in I\), \(v\in J\) with \(u+v=1\). Comaximality gives \(I\cap J=IJ\). The following formulas are inverse \(A\)-linear maps:
\[
\begin{aligned}
I\oplus J&\longrightarrow A\oplus IJ,
& (x,y)&\longmapsto(x+y,vx-uy),\\
A\oplus IJ&\longrightarrow I\oplus J,
& (a,z)&\longmapsto(ua+z,va-z).
\end{aligned} \tag{4}
\]
The second coordinates and both components of the inverse lie in the stated ideals. Substitution, using \(u+v=1\), verifies both compositions.

We next reduce arbitrary \(I,J\) to this case. Multiplying \(I\) by a nonzero scalar makes it integral. Let \(S\) be its finite set of prime divisors. We can multiply \(J\) by a scalar \(t\in F^\times\) so that \(tJ\) is integral and is contained in none of the primes of \(S\). Here is the construction.

For each \(\mathfrak p\in S\), choose a nonzero class in \(J^{-1}/\mathfrak pJ^{-1}\). Such a class exists: after localization this quotient is a one dimensional \(A/\mathfrak p\)-vector space. The module version of the Chinese remainder theorem allows one \(t\in J^{-1}\) having all these prescribed classes. Indeed, the congruence idempotents used for rings also give, by multiplication, surjectivity for any module. If \(S\) is empty, choose any nonzero \(t\in J^{-1}\). Otherwise the nonzero prescribed classes ensure \(t\ne0\).

We have \(tJ\subseteq A\). Moreover,
\[
tJ\subseteq\mathfrak p
\quad\Longleftrightarrow\quad
t\in\mathfrak pJ^{-1},
\]
by multiplying either inclusion by the inverse ideal. Our choice excludes this for all \(\mathfrak p\in S\). A maximal ideal containing both \(I\) and \(tJ\) would lie in \(S\), which is impossible. Thus \(I+tJ=A\).

Apply (4) to the scaled ideals. Multiplication by any nonzero scalar gives an isomorphism from an ideal to its scaled ideal, and scales their product by the product of the scalars. Undoing these isomorphisms proves the assertion for the original \(I,J\). \(\square\)

This reduction only chooses representatives of ideal classes. It does not assert that the original \(I,J\) are comaximal.

## The Steinitz class and the complete module classification

**Theorem 4.3.** Let \(M\) be a finitely generated torsion-free module over a Dedekind domain \(A\). If its rank is zero, then \(M=0\). If its rank is \(r\geq1\), then
\[
M\cong A^{r-1}\oplus I \tag{5}
\]
for a fractional ideal \(I\). The class \([I]\in\operatorname{Cl}(A)\) depends only on the isomorphism class of \(M\). Two such modules of positive rank are isomorphic exactly when their ranks and these ideal classes agree. The module in (5) is free exactly when \([I]=1\).

**Proof.** The preceding lemma writes \(M\cong I_1\oplus\cdots\oplus I_r\). Repeated application of Proposition 4.2 gives (5) with \(I=I_1\cdots I_r\). It remains to prove invariance, rather than infer it from a chosen decomposition.

For any module \(P\), define its \(r\)-th exterior power \(\bigwedge^r_A P\) as the quotient of \(P^{\otimes r}\) imposing the alternating multilinear relations. Isomorphisms induce isomorphisms of exterior powers, and localization commutes with this construction, since it commutes with tensors and quotients.

Multiplication induces an isomorphism \(I_1\otimes_A\cdots\otimes_A I_r\to I_1\cdots I_r\). To justify injectivity as well as surjectivity, localize at every maximal ideal. Each fractional ideal is then generated by one nonzero element, so multiplication becomes an isomorphism between free modules of rank one. A module whose localizations at all maximal ideals vanish is zero: for a nonzero element \(x\), its proper annihilator lies in a maximal ideal \(\mathfrak m\), and \(x/1=0\) there would give an element outside \(\mathfrak m\) annihilating \(x\), a contradiction. Apply this observation to the kernel and cokernel.

The alternating map taking one element from each summand likewise gives
\[
\bigwedge^r_A(I_1\oplus\cdots\oplus I_r)
\cong I_1\otimes_A\cdots\otimes_A I_r
\cong I_1\cdots I_r. \tag{6}
\]
The first map is an isomorphism locally, where it is the usual determinant map for a free module of rank \(r\); the same kernel-and-cokernel argument proves it globally.

The localization argument uses exactness, which can be checked directly with fractions. If \(f(x)/s=0\), some allowed denominator \(t\) satisfies \(tf(x)=0\); then \(tx\) is in the kernel and \(x/s=(tx)/(ts)\). This identifies the localized kernel with the kernel of the localized map. The localized cokernel is the quotient by the localized image, again directly from fractions.

Finally, two fractional ideals are isomorphic as \(A\)-modules exactly when they differ by a nonzero scalar. An isomorphism \(I\to J\), after tensoring with \(F\), is an \(F\)-linear automorphism of the one dimensional vector space \(F\), hence multiplication by a scalar \(a\in F^\times\). Its restriction has image \(aI=J\). The converse is immediate.

Thus \(\bigwedge^r M\) determines the class of the product ideal in (6), and hence the class in (5). Equal rank and equal class give isomorphisms of the displayed modules; unequal ranks or classes cannot. For a free rank-\(r\) module, the exterior power is \(A\), so freeness forces \([I]=1\). Conversely a principal \(I\) is isomorphic to \(A\), making (5) free. \(\square\)

The class in this theorem is the **Steinitz class** of \(M\). For rank zero, we may assign the trivial class by the convention \(\bigwedge^0 0=A\); formula (5) is only used for positive rank.

### Torsion modules

**Torsion classification.** Every finitely generated torsion \(A\)-module is a finite direct sum of modules
\[
A/\mathfrak p^e,\qquad \mathfrak p\ne(0),\quad e\geq1.
\]
For each prime, the multiset of exponents is uniquely determined.

**Proof.** A nonzero element \(a\in A\) kills the module \(T\): take a product of annihilators of a finite generating set. Factor \((a)=\prod_{\mathfrak p\in S}\mathfrak p^{n_{\mathfrak p}}\). The Chinese remainder idempotents split
\[
T=\bigoplus_{\mathfrak p\in S}T_{\mathfrak p},
\]
where the indicated summand is killed by \(\mathfrak p^{n_{\mathfrak p}}\). This summand is unchanged by localization at \(\mathfrak p\). For \(s\notin\mathfrak p\), the ideals \((s)\) and \(\mathfrak p^{n_{\mathfrak p}}\) are comaximal, so some \(b\in A\) satisfies \(bs\equiv1\) modulo that prime power; multiplication by \(b\) is the inverse of multiplication by \(s\) on the summand.

Write \(R=A_{\mathfrak p}\), a discrete valuation ring with uniformizer \(\pi\). A finitely generated \(R\)-module has a finite presentation because \(R\) is Noetherian. Diagonalize its presentation matrix as follows. If the matrix is nonzero, move an entry of least valuation to its upper left corner. That entry divides every other entry. Elementary row operations clear its column, and elementary column operations clear its row. These operations are invertible over \(R\); the remaining submatrix is treated in the same way. Induction on the matrix dimensions leaves a diagonal matrix. Its nonzero diagonal entries, up to units, are powers of \(\pi\). Since our module is torsion, there are no free summands; unit diagonal entries contribute zero summands. Its nonzero summands are therefore \(R/\pi^eR\).

The localization isomorphism \(A/\mathfrak p^e\cong R/\pi^eR\), proved in the preceding lesson, identifies these with the required \(A\)-modules.

To see uniqueness, for each \(k\geq1\) compute
\[
d_{\mathfrak p,k}
=\dim_{A/\mathfrak p}\!
 \left(\mathfrak p^{k-1}T_{\mathfrak p}/\mathfrak p^kT_{\mathfrak p}\right).
\]
A summand \(A/\mathfrak p^e\) contributes \(1\) exactly when \(e\geq k\). Hence the number of summands with exponent exactly \(k\) is
\(d_{\mathfrak p,k}-d_{\mathfrak p,k+1}\), an invariant of \(T\). The primary summands themselves are intrinsic: they consist of the elements killed by some power of the corresponding prime. This proves uniqueness across primes as well. \(\square\)

For an arbitrary finitely generated \(M\), its torsion submodule \(T\) is finitely generated, and \(M/T\) is torsion-free. Indeed, if \(ax\in T\) with \(a\ne0\), then some nonzero \(b\) kills \(ax\), so \(x\in T\). The quotient is projective by Theorem 4.3, and the exact sequence splits:
\[
M\cong T\oplus(M/T).
\]
Thus the primary exponents of \(T\), the rank of \(M/T\), and its Steinitz class give the complete classification. The splitting need not be canonical, but the torsion submodule and the quotient are intrinsic.

### Projective without a global basis

Return to \(A=\mathbf Z[s]\), \(s^2=-5\), and \(\mathfrak p=(2,1+s)\). It is projective, but is not free. A free fractional ideal must have rank one and hence be principal.

Nevertheless,
\[
\mathfrak p\oplus\mathfrak p
\cong A\oplus\mathfrak p^2
=A\oplus(2)
\cong A^2.
\]
Here is an explicit isomorphism, making the cancellation of the two obstructions visible:
\[
\begin{aligned}
F:\mathfrak p\oplus\mathfrak p&\longrightarrow A^2,\\
(x,y)&\longmapsto
\left(x+\frac{1+s}{2}y,\frac{1-s}{2}x+y\right),\\
G:A^2&\longrightarrow\mathfrak p\oplus\mathfrak p,\\
(a,b)&\longmapsto\bigl(-2a+(1+s)b,(1-s)a-2b\bigr).
\end{aligned}
\]
The fractional coefficients in \(F\) send \(\mathfrak p\) into \(A\): it suffices to apply them to \(2\) and \(1+s\), obtaining integral elements. Both components of \(G\) lie in \(\mathfrak p\), since \(1-s=(1+s)-2s\in\mathfrak p\). The identity \((1+s)(1-s)=6\) verifies \(FG=GF=\operatorname{id}\).

## Relative integral bases

Let \(L/K\) be an extension of number fields of degree \(n\), and put \(A=\mathcal O_K\), \(B=\mathcal O_L\). A **relative integral basis** is an \(A\)-basis of \(B\).

**Corollary 4.4.** The module \(B\) is projective of rank \(n\) over \(A\), and
\[
\mathcal O_L\cong\mathcal O_K^{\,n-1}\oplus I
\]
for a fractional ideal \(I\) of \(K\). A relative integral basis exists exactly when \([I]=1\) in \(\operatorname{Cl}_K\). In particular it exists if \(h_K=1\).

**Proof.** An absolute integral basis of \(B\) generates \(B\) over \(\mathbf Z\), and therefore over \(A\): its \(A\)-span contains its \(\mathbf Z\)-span and is contained in \(B\). Thus \(B\) is finitely generated over \(A\). It is torsion-free because it lies in the field \(L\).

Localizing at all nonzero elements of \(A\) identifies \(K\otimes_A B\) with \(L\). Injectivity follows from torsion-freeness. For surjectivity, every \(x\in L\) becomes an algebraic integer after multiplication by a nonzero rational integer, as in the first lesson; this integer lies in \(A\). The rank is consequently \([L:K]=n\). Theorem 4.3 now proves all assertions. \(\square\)

The Steinitz class here is a class of the base ring \(\mathcal O_K\), not of \(\mathcal O_L\). If the base class group is nontrivial, some modules have no basis; this does not assert that every extension has a nontrivial Steinitz class. When \(K=\mathbf Q\), the result agrees with the absolute integral basis theorem.

## Exercises

1. **Easy.** In \(A=\mathbf Z[\sqrt{-5}]\), compute the norm of \(\mathfrak q=(3,1+\sqrt{-5})\). Show that \(\mathfrak q\) is not principal.
2. **Medium.** Prove that a nonzero integral ideal of \(\mathcal O_K\) whose absolute norm is a rational prime is a prime ideal. Explain why the converse need not hold.
3. **Medium.** Give a splitting from a finite free module that proves a fractional ideal is projective. Use it to prove that every finitely generated torsion-free module over a Dedekind domain is projective. For \(\mathfrak p=(2,1+\sqrt{-5})\), give the splitting with just two generators.
4. **Hard.** Starting from the surjection \(I\oplus J\to I+J\), construct Proposition 4.2 when \(I+J=A\), and justify the reduction of arbitrary fractional ideals to comaximal integral ideals. State precisely how the product ideal changes when representatives are scaled.

## Complete solutions

**1.** The map \(a+bs\mapsto a-b\) from \(A\) to \(\mathbf F_3\) is well-defined because \((-1)^2+5=6\equiv0\). If \(a-b\) is divisible by \(3\), then
\[
a+bs=3\frac{a-b}{3}+b(1+s),
\]
so its kernel is exactly \(\mathfrak q\). It is surjective, giving \(N\mathfrak q=3\). A generator would solve \(a^2+5b^2=3\), which is impossible: \(b\ne0\) gives at least \(5\), and \(b=0\) gives a square.

**2.** A quotient ring \(R=\mathcal O_K/\mathfrak a\) with \(p\) elements has additive group of order \(p\). Its identity is nonzero, since \(p>1\), so it additively generates \(R\). The map \(\mathbf Z\to R\) therefore identifies \(R\) with \(\mathbf F_p\) as a ring. Hence \(\mathfrak a\) is maximal and prime. Conversely, the residue field at a prime ideal may have \(p^f\) elements with \(f>1\). For example, \((3)\) in \(\mathbf Z[i]\) is prime: its quotient is \(\mathbf F_3[X]/(X^2+1)\), and that polynomial has no root in \(\mathbf F_3\). The quotient is a field of order \(9\).

**3.** Choose \(x_i\in I\), \(y_i\in I^{-1}\) with \(\sum x_i y_i=1\). The maps \(q(a_i)=\sum a_i x_i\) and \(j(z)=(y_i z)_i\) satisfy \(qj=1\), so \(I\) is a summand of \(A^m\). The torsion-free decomposition lemma expresses any finitely generated torsion-free module as a finite direct sum of such ideals; combining their finite free splittings proves projectivity.

For \(\mathfrak p=(2,1+s)\), take
\[
q:A^2\to\mathfrak p,\quad q(a,b)=2a+(1+s)b,
\qquad
j(z)=\left(-z,\frac{1-s}{2}z\right).
\]
The second coordinate lies in \(A\), as can be checked on \(z=2\) and \(z=1+s\). Also
\[
qj(z)=\left(-2+\frac{(1+s)(1-s)}2\right)z=z.
\]
This proves projectivity directly while the norm obstruction above proves that the ideal is not free.

**4.** The addition map has kernel \(\{(z,-z)\mid z\in I\cap J\}\). When \(I+J=A\), its target is \(A\), the kernel is \(IJ\), and a section is \(a\mapsto(ua,va)\) for \(u+v=1\), \(u\in I\), \(v\in J\). Subtracting the section from \((x,y)\) gives
\[
(x,y)-(u(x+y),v(x+y))
=(vx-uy,-(vx-uy)).
\]
This gives exactly the mutually inverse maps (4).

For the reduction, choose \(c\in F^\times\) making \(cI\) integral. At each of its finitely many prime divisors, choose a nonzero class in \(J^{-1}/\mathfrak pJ^{-1}\); module Chinese remainders give \(t\in J^{-1}\) representing them all. Then \(tJ\) is integral and comaximal with \(cI\), as shown in the proof. The scaled product is \((cI)(tJ)=ct\,IJ\). Multiplication by \(c\), \(t\), and \(ct\) gives the respective isomorphisms needed to transport the constructed map back to \(I\oplus J\) and \(A\oplus IJ\).

## What this lesson does not prove

The absolute integral basis theorem and the integer matrix index formula are imported from *Discriminants and integral bases*. Unique factorization, invertibility and the local discrete valuation description of ideals are imported from *Discrete valuation rings and Dedekind domains*. Their precise statements and proofs are in those lessons. The general algebra characterization [Stacks, Tag 034X] was stated and its conventions explained there.

The finiteness of \(\operatorname{Cl}_K\) is reserved for *Finiteness of the class number*. Relative ideal norms, including compatibility with norms of elements in extensions, are introduced in *Decomposition of primes in extensions*. No relative ideal norm is assumed in the proof of Proposition 4.1.

## References

- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Chapter 3, “Modules over Dedekind domains (sketch),” Theorem 3.31, pp. 57–58; Chapter 4, “Norms of ideals,” Proposition 4.2, pp. 69–70. [Lecture notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Stacks]** The Stacks project, [Tag 034X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-Dedekind), characterization of Dedekind domains.

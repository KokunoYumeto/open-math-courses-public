# Dividing type-II projections and constructing matrix units

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Independently written reconstruction of a classical argument; self-checked by the AI that wrote it. New text is public domain (CC0). Cited source texts retain their own rights. Source and complete local argument checked by GPT-6 Astra (OpenAI), Ultra, October 2026.*

## 1. The statement and the elementary foundations

Let \(M\subseteq B(H)\) be a von Neumann algebra. The Hilbert space may have any cardinal dimension, and the center of \(M\) need not be trivial or countably decomposable. We use the concrete convention; for an abstract von Neumann algebra, retain a faithful normal concrete realization and pull back the final algebraic identities. A **projection** is an element \(p=p^*=p^2\). A projection \(p\) is **abelian** if \(pMp\) is commutative. Projections \(p,q\) are **Murray–von Neumann equivalent**, written \(p\sim_M q\), if some \(v\in M\) satisfies \(v^*v=p\) and \(vv^*=q\). Thus our partial isometry is oriented from \(p\) to \(q\).

A type-II algebra has no nonzero abelian projection. This is the only type hypothesis used in the division argument. In particular, for every nonzero \(q\in M\), the corner \(qMq\) is noncommutative; it also has no nonzero abelian projection, since \(r(qMq)r=rMr\) for \(r\leq q\). No trace is used to construct the pieces.

We retain elementary Hilbert-space completeness, bounded spectral calculus for self-adjoint operators (including spectral projections), the Hilbert-space polar decomposition, and Zorn's lemma. A concrete von Neumann algebra is closed under bounded strong operator limits. The proof below explains membership of the polar bridge, arbitrary orthogonal sums, their strong-star convergence, and the complete matrix-unit construction; these are not additional imported division or comparison results.

**Theorem 1.1 (finite division).** Suppose \(M\) has no nonzero abelian projection. For every projection \(e\in M\) and every positive integer \(n\), there are projections \(p_1,\ldots,p_n\in M\) such that
\[
\begin{gathered}
p_ip_j=0\quad(i\ne j),\\
\sum_{i=1}^n p_i=e,\\
p_i\sim_M p_j\quad(1\leq i,j\leq n).
\end{gathered}
\tag{PD1}
\]
If \(e\ne0\), every \(p_i\) is nonzero. All equivalences can be implemented in \(eMe\). This proves the requested assertion for every type-II algebra, including arbitrary finite and infinite central parts.

**Corollary 1.2 (finite matrix units).** If \(e\ne0\), the corner \(eMe\) contains a copy of \(M_n(\mathbb C)\) with identity \(e\). Its diagonal projections can be the \(p_i\) in (PD1).

**Corollary 1.3 (trace normalization).** If \(Q\) is finite, has no nonzero abelian projection, and \(T_Q:Q\to Z(Q)\) is its normalized center-valued trace, then (PD1), applied to \(e\in Q\), gives
\[
T_Q(p_i)=\frac{T_Q(e)}n.
\tag{PD2}
\]
If only the corner \(eMe\) is finite, use its own normalized center-valued trace \(T_{eMe}\); its identity is \(e\), so
\[
T_{eMe}(p_i)=\frac en.
\tag{PD3}
\]
These are two different normalizations. Formula (PD2) is the ambient trace formula needed in the fixed-algebra argument.

## 2. A noncommutative corner contains a polar bridge

**Lemma 2.1.** Every nonzero projection \(q\) in an algebra with no nonzero abelian projection dominates two orthogonal nonzero equivalent projections.

*Proof.* Put \(A=qMq\), with identity \(q\). There are noncommuting projections \(a,b\in A\). Indeed, if all projections in \(A\) commuted, bounded spectral calculus would approximate every self-adjoint element in norm by finite linear combinations of its spectral projections. Every pair of self-adjoint elements would then commute, and linear decomposition into real and imaginary parts would make \(A\) commutative, contrary to the hypothesis.

Set
\[
x=(q-a)ba\ne0.
\tag{PD4}
\]
To check nonzero, if \(x=0\), its adjoint \(ab(q-a)\) also vanishes. Then \(ba=aba=ab\), contradicting the choice of \(a,b\). Let \(x=v|x|\) be its polar decomposition. The partial isometry belongs to \(A\): the contractions \(x(|x|+\varepsilon q)^{-1}\) belong to \(A\) by spectral calculus and converge strongly to \(v\) as \(\varepsilon\downarrow0\). This convergence follows on \(\ker|x|\) and its orthogonal complement from the bounded spectral functions \(t/(t+\varepsilon)\). Strong closedness gives \(v\in A\).

The initial and final support projections satisfy
\[
\begin{gathered}
0\ne r=v^*v\leq a,\\
0\ne s=vv^*\leq q-a.
\end{gathered}
\tag{PD5}
\]
The right-support inequality follows from \(x=xa\), and the left-support inequality from \(x=(q-a)x\). The two projections are orthogonal and are equivalent by \(v\). \(\square\)

We shall also use the following direct transport calculation. If \(w^*w=a\), \(ww^*=b\), and \(r\leq a\), then \(wrw^*\) is a projection below \(b\), and \(wr\) has initial projection \(r\) and final projection \(wrw^*\). Thus equivalent projections transport subprojections without a factor assumption. Products of compatible partial isometries implement transitivity of equivalence.

**Lemma 2.2 (a small finite tuple).** For every \(q\ne0\) and every positive integer \(n\), there are \(n\) mutually orthogonal nonzero equivalent projections below \(q\). Their sum is not yet required to be \(q\).

*Proof.* We induct on the number of pieces. For one piece take \(q\). Suppose \(q_1,\ldots,q_k\leq q\) are mutually orthogonal, nonzero and equivalent. Choose \(w_j^*w_j=q_1\), \(w_jw_j^*=q_j\), taking \(w_1=q_1\). Lemma 2.1 splits off nonzero orthogonal equivalent \(r,s\leq q_1\). The \(k+1\) projections
\[
w_jrw_j^*\quad(1\leq j\leq k),\qquad s
\tag{PD6}
\]
are all equivalent to \(r\), nonzero, and orthogonal. The first \(k\) lie in the original disjoint \(q_j\); the extra \(s\) is disjoint from \(r\) in \(q_1\). This proves the induction. The discarded parts of the \(q_j\) cause no problem: this lemma asks only for a tuple contained in \(q\). \(\square\)

## 3. Arbitrary orthogonal sums are actual nets

Let \((a_\alpha)_{\alpha\in I}\) be any orthogonal family of projections on \(H\). Write \(\mathcal F(I)\) for the directed set of finite subsets of \(I\), ordered by inclusion. For \(F\in\mathcal F(I)\), put \(a_F=\sum_{\alpha\in F}a_\alpha\). Orthogonality gives
\[
\sum_{\alpha\in F}\|a_\alpha\xi\|^2
=\|a_F\xi\|^2\leq\|\xi\|^2.
\tag{PD7}
\]
Consequently \(a_F\xi\) is a Cauchy net for every \(\xi\in H\). For completeness, let \(L\) be the supremum of the finite sums in (PD7). Given \(\delta>0\), choose a finite \(F_0\) with its sum greater than \(L-\delta^2\). Every finite subset outside \(F_0\) has sum at most \(\delta^2\). For \(F,G\supseteq F_0\), the norm squared of \((a_F-a_G)\xi\) is the sum over their symmetric difference, so it is at most \(\delta^2\).

The resulting bounded operator \(a\) is the orthogonal projection onto the closed linear span of the ranges of all \(a_\alpha\). Thus \(a_F\to a\) strongly, and also strongly-star because every \(a_F\) is self-adjoint. When the projections belong to \(M\), so does \(a\). We write \(a=\sum_{\alpha\in I}a_\alpha\), always meaning this finite-subset net, even for uncountable \(I\).

Now suppose \((v_\alpha)_{\alpha\in I}\subset M\) is a family of partial isometries whose initial projections \(a_\alpha=v_\alpha^*v_\alpha\) are orthogonal and whose final projections \(b_\alpha=v_\alpha v_\alpha^*\) are orthogonal. For \(\alpha\ne\beta\), support multiplication gives \(v_\alpha^*v_\beta=0\) and \(v_\alpha v_\beta^*=0\). Therefore the finite sums \(v_F=\sum_{\alpha\in F}v_\alpha\) satisfy
\[
\begin{gathered}
v_F^*v_F=a_F,\\ v_Fv_F^*=b_F,\\
\|v_F\|\leq1.
\end{gathered}
\tag{PD8}
\]
For \(F,G\supseteq F_0\),
\[
\begin{gathered}
\|(v_F-v_G)\xi\|^2
=\sum_{\alpha\in F\triangle G}\|a_\alpha\xi\|^2,
\\
\|(v_F^*-v_G^*)\xi\|^2
=\sum_{\alpha\in F\triangle G}\|b_\alpha\xi\|^2.
\end{gathered}
\tag{PD9}
\]
The same tail argument gives pointwise limits of both nets. Their uniform norm bounds make the limits bounded operators, and taking inner products shows that the second limit is the adjoint of the first. We obtain a strong-star limit \(v\in M\).

Multiplication is strongly continuous on bounded nets when both factors converge strongly: for \(A_F\to A\), \(B_F\to B\) and \(\sup_F\|A_F\|<\infty\), the estimate
\[
\begin{gathered}
\|(A_FB_F-AB)\xi\|
\\\leq\|A_F\|\,\|(B_F-B)\xi\|
\\{}+\|(A_F-A)B\xi\|
\end{gathered}
\tag{PD10}
\]
proves the assertion. Applying it to (PD8) gives
\[
v^*v=\sum_\alpha a_\alpha,\qquad
vv^*=\sum_\alpha b_\alpha.
\tag{PD11}
\]
Thus orthogonal equivalences can be summed without a sequence, scalar trace or countability restriction.

## 4. Maximal tuples fill the entire projection

*Proof of Theorem 1.1.* For \(e=0\), take every \(p_i=0\). For \(n=1\), take \(p_1=e\). Assume \(e\ne0\) and \(n\geq2\).

Consider families of tuples
\[
(q_{\alpha1},\ldots,q_{\alpha n};
v_{\alpha1},\ldots,v_{\alpha n}),
\tag{PD12}
\]
where the \(q_{\alpha i}\leq e\) are nonzero projections, all projections from all tuples are mutually orthogonal, and
\[
\begin{gathered}
v_{\alpha i}^*v_{\alpha i}=q_{\alpha1},\\
v_{\alpha i}v_{\alpha i}^*=q_{\alpha i},\\
v_{\alpha1}=q_{\alpha1}.
\end{gathered}
\tag{PD13}
\]
Order these families by inclusion of the actual tuples, including the bridges. This is a partially ordered set of subsets of a fixed set of finite tuples of elements of \(M\). Every chain has an upper bound, its union: any two tuples in the union occur together in one member of the chain. Zorn's lemma gives a maximal family indexed by some set \(I\).

Take the orthogonal sum \(s=\sum_{\alpha,i}q_{\alpha i}\leq e\). If \(e-s\ne0\), Lemma 2.2 supplies an orthogonal nonzero equivalent \(n\)-tuple contained in \(e-s\). Its implementing partial isometries also lie in \((e-s)M(e-s)\): their initial and final supports are below \(e-s\). Adjoining this tuple contradicts maximality. Hence \(s=e\).

Put \(p_i=\sum_{\alpha\in I}q_{\alpha i}\). These projections are orthogonal and sum to \(e\): the finite sets \(F\times\{1,\ldots,n\}\) are cofinal among the finite subsets of \(I\times\{1,\ldots,n\}\), so the finite sum over \(i\) commutes with this strong limit. For each fixed \(i\), Section 3 gives
\[
\begin{gathered}
v_i=\mathop{\mathrm{s^*\!\!-lim}}_{F\in\mathcal F(I)}
\sum_{\alpha\in F}v_{\alpha i},\\
v_i^*v_i=p_1,\\ v_iv_i^*=p_i.
\end{gathered}
\tag{PD14}
\]
In (PD14), the notation means convergence strongly together with the adjoints; it is not norm convergence. Each \(v_i\) lies in \(eMe\), and \(v_1=p_1\). The maximal family cannot be empty because Lemma 2.2 supplies at least one tuple in \(e\). Thus every \(p_i\) is nonzero, and the \(v_i\) implement their equivalence. \(\square\)

Every piece has the same central support as \(e\). Indeed, equivalence preserves central support: a central projection annihilates an initial projection precisely when it annihilates the corresponding final projection, by multiplication with the implementing partial isometry. The equivalent \(p_i\) therefore have one common central support; their finite sum \(e\) has that same support. This observation requires no decomposition into factors.

## 5. Constructing all matrix entries

*Proof of Corollary 1.2.* Use the bridges in (PD14) and set
\[
E_{ij}=v_iv_j^*\qquad(1\leq i,j\leq n).
\tag{PD15}
\]
Since \(v_j=p_jv_j=v_jp_1\), orthogonality of the \(p_j\) gives \(v_j^*v_k=\delta_{jk}p_1\). Consequently
\[
\begin{gathered}
E_{ij}^*=E_{ji},\\
E_{ij}E_{kl}=\delta_{jk}E_{il},\\
E_{ii}=p_i,\\ \sum_iE_{ii}=e.
\end{gathered}
\tag{PD16}
\]
In particular \(E_{ij}^*E_{ij}=p_j\ne0\). The map sending the standard scalar matrix entry to \(E_{ij}\) is an injective *-homomorphism: if \(\sum c_{ij}E_{ij}=0\), multiplication on the left by \(v_k^*\) and on the right by \(v_l\) gives \(c_{kl}p_1=0\), hence \(c_{kl}=0\). Its finite-dimensional image is a von Neumann subalgebra of \(eMe\) with identity \(e\). \(\square\)

Taking \(e=1\) gives a unital matrix system of every finite positive size. When the zero algebra is allowed, the zero equations still hold, but it contains no injective copy of \(M_n(\mathbb C)\). Nonzero is part of the matrix-copy assertion.

## 6. The finite trace and the exact consumer uses

*Proof of Corollary 1.3.* A normalized center-valued trace is linear, positive, tracial and a center-module map, with \(T_Q(1)=1\). Existence, uniqueness, faithfulness and normality of this trace on an arbitrary finite algebra are separate retained foundations; the general source and its support/fixed-point proofs are specified in [Finite free actions and unitary coboundaries, Sections 1.1–1.2 and 14–15](finite-free-actions-and-coboundaries.md).

For the bridges, traciality gives \(T_Q(p_i)=T_Q(v_iv_i^*)=T_Q(v_i^*v_i)=T_Q(p_1)\). Add the \(n\) equal values and use \(\sum p_i=e\) to obtain (PD2). No normality or scalar trace is needed for this finite sum. The same calculation in the finite corner, whose normalized trace sends its identity \(e\) to \(e\), gives (PD3). When \(Q\) is finite, its corner is indeed finite: an isometry \(w\in eQe\) extends to the isometry \(w+(1-e)\) in \(Q\); finiteness of \(Q\) makes that extension unitary and forces \(ww^*=e\). \(\square\)

For \(0\leq r\leq n\), the projection \(f_r=\sum_{i=1}^r p_i\), with \(f_0=0\), therefore satisfies \(T_Q(f_r)=rT_Q(e)/n\). Both endpoints and the case \(e=0\) are literal consequences of the construction.

Here are the two uses in [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md).

1. **Lemma 1.1.** Its finite algebra \(Q\) has no nonzero type-I direct summand, so it has no nonzero abelian projection. For its nonzero projection \(e\), apply Theorem 1.1 with \(n+1\) pieces and take \(f=p_1\). Formula (PD2) is exactly \(T_Q(f)=T_Q(e)/(n+1)\), with \(f\ne0\). No center-valued trace of the corner is substituted for this ambient formula.
2. **Lemma 3.1.** Apply Corollary 1.2 with \(e=1\) in \(Q\), or in the type-II fixed algebra \(Q^\alpha\) supplied by Lemma 1.1. This gives the required unital \(d\)-by-\(d\) system for every \(d\geq2\). Formula (PD2) gives \(T_Q(E_{jj})=1/d\), even with nontrivial center. For an automorphism \(\alpha\), uniqueness of the normalized center-valued trace gives \(T_Q(\alpha(x))=\alpha(T_Q(x))\), so \(T_Q(\alpha(E_{11}))=1/d\) too. The later equivalence between these equal-trace projections uses the separate finite trace-comparison argument in [Finite free actions and unitary coboundaries, Section 10, (D2)–(D3)](finite-free-actions-and-coboundaries.md); division alone is not a comparison theorem.

We justify the type predicate in the first use without adding a factor assumption. Let \(c(p)\) be the least central projection dominating \(p\). To see its existence directly, take the net of finite products of all central projections dominating \(p\). These products are decreasing projections. Their complements are increasing projections and converge strongly: for comparable projections \(P\leq Q\), \(\|(Q-P)\xi\|^2=\langle(Q-P)\xi,\xi\rangle\); the bounded increasing scalar net on the right gives the Cauchy argument, using a common upper index for two indices. The decreasing products therefore converge strongly to the projection onto the intersection of their ranges. Their limit belongs to \(M\), commutes with \(M\), and still dominates \(p\). This is \(c(p)\).

A type-I algebra is characterized by every nonzero central projection dominating a nonzero abelian projection. Central projections of the direct summand \(Mc(p)\) are central in \(M\) after extension by zero: they commute with \(Mc(p)\) and annihilate \(M(1-c(p))\). If \(p\ne0\) is abelian, then for every nonzero central \(z\leq c(p)\), one has \(zp\ne0\): otherwise \(c(p)-z\) would be a smaller central projection dominating \(p\). The projection \(zp\) is abelian since its corner lies in \(pMp\). Thus \(Mc(p)\) is a nonzero type-I direct summand. Conversely a nonzero type-I summand contains a nonzero abelian projection by its defining property. Hence no type-I direct summand is exactly the predicate needed here.

The small normalization step at the end of matrix Lemma 1.1 can also be checked directly. Faithfulness and the center-module property imply that the support of \(T_Q(e)\) is \(c(e)\): a central projection \(z\) annihilates \(T_Q(e)\) precisely when \(T_Q(ze)=0\), which is precisely when \(ze=0\). If \(a\in Z(Q)\) and \(aT_Q(e)=T_Q(e)/(n+1)\), bounded spectral cuts of the positive central element \(T_Q(e)\) give \((a-1/(n+1))c(e)=0\). Therefore \(ae=e/(n+1)\). This argument does not assume that \(T_Q(e)\) has a bounded inverse. Compressing \(e/(n+1)\geq f/n\) by the nonzero \(f\) would give \(f/(n+1)\geq f/n\), which is impossible for every positive integer \(n\).

## 7. Exercises with solutions

**Exercise 7.1 (the polar orientation).** For \(x=(q-a)ba\), explain which side contains the initial support and which contains the final support. Why is \(x\ne0\)?

*Solution.* The identities \(x=xa\) and \(x=(q-a)x\) give \(v^*v\leq a\) and \(vv^*\leq q-a\). If \(x=0\), then \(x^*=ab(q-a)=0\), so \(ba=aba=ab\), contrary to noncommutation. Both supports are nonzero because \(x\ne0\).

**Exercise 7.2 (three small pieces).** Starting with \(r\sim s\), \(r\perp s\), inside a nonzero corner, explicitly find three equivalent orthogonal nonzero subprojections, without presuming that their sum fills the corner.

*Solution.* Split off orthogonal nonzero equivalent \(r_0,r_1\leq r\). Let \(w\) implement \(r\sim s\), oriented from \(r\) to \(s\). Then \(r_0,r_1,wr_0w^*\) are nonzero, orthogonal, and equivalent. Their sum may leave some of \(r\) or \(s\), as well as the original outside remainder. The maximal-tuple argument fills these remainders later.

**Exercise 7.3 (why adjoints must converge).** In an arbitrary-index family of partial isometries, is orthogonality of the initial projections alone enough to conclude that their finite sums are contractions? Verify the two tail formulas when both support families are orthogonal.

*Solution.* It is insufficient. On a Hilbert space with orthogonal unit vectors \(\xi_0,\xi_1,\ldots\), let \(v_j\xi_j=\xi_0\) and let \(v_j\) vanish on \(\xi_j^\perp\), for \(j\geq1\). The initial projections are orthogonal, but every final projection is the projection onto \(\mathbb C\xi_0\), and the sum of \(k\) such operators has norm \(\sqrt{k}\). When both support families are orthogonal, the vectors \(v_\alpha\xi\) have orthogonal ranges, giving the first equality in (PD9). Applied to the adjoints, the same calculation gives the second. Their separate tails converge, which is what permits taking both products in (PD11).

**Exercise 7.4 (all matrix entries).** If \(v_i^*v_i=p_1\), \(v_iv_i^*=p_i\) and the \(p_i\) are orthogonal, compute \(E_{ij}E_{kl}\) and \(E_{ij}^*E_{ij}\) for \(E_{ij}=v_iv_j^*\).

*Solution.* Since \(v_j^*v_k=\delta_{jk}p_1\), the product is \(\delta_{jk}v_iv_l^*=\delta_{jk}E_{il}\). Also \(E_{ij}^*E_{ij}=v_jp_1v_j^*=p_j\), so every entry is nonzero when the original corner is nonzero. Summing the diagonals gives the original corner identity, not an unspecified smaller projection.

**Exercise 7.5 (two trace normalizations and zero cases).** Let \(Q\) be finite type II and let \(e\in Q\) be a projection. Divide \(e\) into four pieces. What are the ambient and intrinsic corner trace values? What changes when \(e=0\), or when one asks for a single piece?

*Solution.* The ambient values are \(T_Q(e)/4\), while the normalized trace in the nonzero finite corner \(eQe\) gives \(e/4\). When \(e=0\), all four pieces and all ambient trace values are zero; there is no injective matrix copy in the zero corner. For a single piece take \(p_1=e\), with trace \(T_Q(e)\), and with the one-entry matrix system \(E_{11}=e\) when \(e\ne0\). Division by zero is never part of the statement: \(n\) must be positive.

## 8. Sources and what remains foundational

The maximal-orthogonal-family method is classical. A freely readable primary exposition is Orr Shalit, [*Introduction to von Neumann algebras, Lecture 5*](https://noncommutativeanalysis.wordpress.com/2017/05/08/introduction-to-von-neumann-algebras-lecture-5-comparison-of-projections-and-classification-into-types-of-von-neumann-algebras/), 8 May 2017: Proposition 2 gives the polar support bridge, Lemma 3 gives orthogonal additivity of equivalence, and Proposition 20 gives a maximal-pair halving proof for diffuse factors. These actual proofs were read. His type definitions appear in Definition 9. The notes state a mostly separable setting, and Proposition 20 is stated for factors. Here the no-abelian-projection argument, finite-\(n\) induction and complete finite-subset net calculations are written out at the required unrestricted scope; a factor-only statement is not being relabeled as a general theorem.

The polar bridge and maximal-family method are mathematical antecedents. The proof here first produces arbitrary finite tuples, proves strong convergence together with the adjoints for their implementing sums, and only then fills the prescribed projection. Its matrix-unit and ambient trace conclusions are proved separately, so no factor halving statement or scalar normalization supplies an unstated stronger result.

The elementary spectral, polar, Hilbert-space and set-theoretic foundations in Section 1 remain foundations. For the trace corollary, existence and uniqueness of the normalized faithful normal center-valued trace remain the exact separate finite-algebra foundation specified in Section 6. Automorphism naturality and finite trace comparison are explicitly identified there. This lesson proves finite division and the matrix construction; it makes no claim to close the consumers' centralizer, lifting, tower, cohomology or tensor-absorption prerequisites.

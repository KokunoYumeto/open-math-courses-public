# Free-group averaging and the compact ideal

*Self-checked by the writing AI. Original text: CC0 1.0.*

The left and right regular actions of a free group commute. Their joint action on one Hilbert space has an ideal of compact operators, and removing that ideal gives the spatial tensor product of the two reduced group algebras. We will prove each part of this statement. The proof separates three mechanisms: an averaging argument proves simplicity of the factors; a spectral gap isolates a rank-one projection; and an average over word cuts compares the joint action with the spatial action modulo compact operators.

Prerequisites are [Tensor norms and independent systems](../reader/tensor-norms-and-independent-systems.html), [Tensor independence and ideals](../reader/tensor-independence-and-ideals.html), and the functional calculus and quotient results in [C*-algebra foundations](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Theorem 5.1, Theorem 15.1 and Corollary 15.4. We reuse Theorem 2.1 of the tensor-independence lesson, which proves that a spatial tensor product of simple C*-algebras is simple, and Proposition 4.1 of that lesson, which computes the four-regular tree adjacency norm as \(2\sqrt3\). Familiarity with reduced words and orthogonal projections on Hilbert space is sufficient for the group arguments below.

Freely readable treatments are de la Harpe’s exposition of Powers averaging and Akemann and Ostrand’s paper on the compact ideal and spatial quotient. The arguments here give a reduced-word partition, an explicit cyclic-coset comparison and a word-cut isometry with a compact intertwining error. The last construction proves the essential-norm bound in Proposition 3.2 directly. The earlier programme lessons supply the norm, tensor and simplicity prerequisites.

Throughout, \(G=F(s,t)\) is the free group on two generators, \(e\) is its identity, and \(|g|\) is the length of the reduced word for \(g\). Put
\[
H=\ell^2(G),\qquad
\lambda_g\delta_h=\delta_{gh},\qquad
\rho_g\delta_h=\delta_{hg^{-1}}.
\tag{0.1}
\]
Both \(\lambda\) and \(\rho\) are unitary representations. Their operators commute. We write
\[
L=C^*(\lambda_g:g\in G),\qquad
R=C^*(\rho_g:g\in G),\qquad
\mathcal A=C^*(L,R)\subseteq B(H).
\tag{0.2}
\]
All three algebras are unital. The linear span of the operators \(\lambda_g\rho_h\) is dense in \(\mathcal A\), since products and adjoints of these operators remain in that span.

## 1. Word partitions and norm averaging

Define the canonical state on \(L\) by
\[
\tau(a)=\langle a\delta_e,\delta_e\rangle.
\tag{1.1}
\]
For a group polynomial, this selects its identity coefficient. Multiplication of two such polynomials shows \(\tau(ab)=\tau(ba)\), because \(gh=e\) exactly when \(hg=e\). Norm density therefore makes \(\tau\) a tracial state on \(L\).

It is faithful. If \(\tau(a^*a)=0\), then \(a\delta_e=0\). Every element of \(L\) commutes with every \(\rho_g\), so \(a\rho_g\delta_e=0\) for all \(g\). These vectors are the entire standard basis of \(H\), and hence \(a=0\). In particular, a nonzero positive element of \(L\) has strictly positive trace, by applying this argument to its square root.

**Lemma 1.1 (a word partition).** For every finite set \(F\subseteq G\setminus\{e\}\) and every positive integer \(n\), there are a partition \(G=C\sqcup D\) and elements \(u_1,\ldots,u_n\in G\) such that
\[
fC\cap C=\varnothing\quad(f\in F),
\qquad u_iD\cap u_jD=\varnothing\quad(i\ne j).
\tag{1.2}
\]

**Proof.** First we make a common conjugation of \(F\). Choose \(N>\max_{f\in F}|f|\), and put \(h=t^Ns^N\). Every reduced word for \(hfh^{-1}\) begins with \(t\) and ends with \(t^{-1}\). To verify this, if \(f=s^k\ne e\), the conjugate is \(t^Ns^kt^{-N}\). Otherwise \(f\) contains a letter \(t\) or \(t^{-1}\). Reducing \(s^Nfs^{-N}\) can cancel fewer than \(N\) letters at each end, leaving a nonempty initial block of \(s\)'s and a nonempty final block of \(s^{-1}\)'s. The outer \(t^N\) and \(t^{-N}\) then survive.

For the conjugated set, let \(C_0\) consist of all reduced words beginning with \(s\) or \(s^{-1}\), and let \(D_0=G\setminus C_0\). Thus \(D_0\) contains \(e\) and precisely the nonempty words beginning with \(t\) or \(t^{-1}\). Multiplying a word of \(C_0\) on the left by \(hfh^{-1}\) causes no cancellation at the join: that join is \(t^{-1}\) followed by \(s^{\pm1}\). The product begins with \(t\), so misses \(C_0\).

The sets \(s^iD_0\), \(1\le i\le n\), are disjoint. Their words are \(s^i\) itself or words whose first block is exactly \(i\) positive \(s\)'s followed by \(t^{\pm1}\). Different values of \(i\) cannot give the same reduced word. Finally take \(C=h^{-1}C_0\), \(D=h^{-1}D_0\), and \(u_i=s^ih\). Left multiplication by \(h\) carries \(fC\cap C\) to \((hfh^{-1})C_0\cap C_0\), while \(u_iD=s^iD_0\). This proves (1.2). \(\square\)

**Lemma 1.2 (Powers averaging estimate).** If
\[
x=\sum_{f\in F}c_f\lambda_f,
\qquad e\notin F,
\]
then, for every \(n\ge1\), some \(u_1,\ldots,u_n\in G\) satisfy
\[
\left\|\frac1n\sum_{i=1}^n\lambda_{u_i}x\lambda_{u_i}^*\right\|
\le\frac{2\|x\|}{\sqrt n}.
\tag{1.3}
\]

**Proof.** Apply Lemma 1.1 to the support of \(x\). Let \(P\) be the projection onto \(\ell^2(C)\), and let \(Q=1-P\). Since each \(\lambda_f\) carries \(\ell^2(C)\) into \(\ell^2(D)\), we have \(PxP=0\). Put
\[
x_i=\lambda_{u_i}x\lambda_{u_i}^*,
\qquad Q_i=\lambda_{u_i}Q\lambda_{u_i}^*.
\]
The \(Q_i\)'s are mutually orthogonal, and \((1-Q_i)x_i(1-Q_i)=0\). Thus
\[
x_i=Q_ix_i+(1-Q_i)x_iQ_i.
\tag{1.4}
\]
For any \(\xi\in H\), orthogonality of the output ranges gives
\[
\left\|\sum_iQ_ix_i\xi\right\|^2
=\sum_i\|Q_ix_i\xi\|^2
\le n\|x\|^2\|\xi\|^2.
\]
For the other sum, the triangle inequality and Cauchy–Schwarz give
\[
\left\|\sum_i(1-Q_i)x_iQ_i\xi\right\|
\le\|x\|\sum_i\|Q_i\xi\|
\le\sqrt n\,\|x\|\,\|\xi\|.
\]
Adding the two bounds in (1.4) and dividing by \(n\) proves (1.3). No self-adjointness assumption on \(x\) is needed. \(\square\)

**Proposition 1.3.** For every \(a\in L\), the scalar \(\tau(a)1\) belongs to the norm-closed convex hull of
\[
\{\lambda_g a\lambda_g^*:g\in G\}.
\tag{1.5}
\]

**Proof.** Subtract \(\tau(a)1\), so that we may assume \(\tau(a)=0\). Given \(\varepsilon>0\), choose a group polynomial \(b\) with \(\|a-b\|<\varepsilon/4\). Put \(x=b-\tau(b)1\). This polynomial has no identity coefficient, and
\[
\|a-x\|\le\|a-b\|+|\tau(b-a)|<\varepsilon/2.
\]
Choose \(n\) so large that \(2\|x\|/\sqrt n<\varepsilon/2\), and use the same conjugations for \(a\) as for \(x\) in Lemma 1.2. Their average applied to \(a\) has norm less than \(\varepsilon\). Restoring the scalar gives (1.5). \(\square\)

**Theorem 1.4.** The algebras \(L\) and \(R\) are simple and have unique tracial states.

**Proof.** Let \(I\subseteq L\) be a nonzero closed two-sided ideal. Choose \(0\ne a\in I_+\). Faithfulness of \(\tau\) gives \(\tau(a)>0\). Every conjugate in (1.5) lies in \(I\), so norm closure gives \(\tau(a)1\in I\). Hence \(1\in I\), and \(I=L\).

If \(\sigma\) is another tracial state, it takes the same value on every conjugate of \(a\), and therefore on every average of those conjugates. Taking the norm limit in Proposition 1.3 gives \(\sigma(a)=\tau(a)\) for every \(a\in L\).

The linear unitary \(J\delta_g=\delta_{g^{-1}}\) satisfies \(J\lambda_gJ=\rho_g\). It carries \(L\) onto \(R\), transferring both assertions. \(\square\)

## 2. A spectral gap produces the compact operators

Write \(S=\{s,s^{-1},t,t^{-1}\}\). The known tree norm is
\[
\left\|\sum_{a\in S}\lambda_a\right\|=2\sqrt3.
\tag{2.1}
\]
We need to apply this bound to the action by conjugation on every nonidentity conjugacy class. The stabilizers of that action are cyclic; we include the group-theoretic and Hilbert-space details.

**Lemma 2.1.** The centralizer \(Z_G(g)=\{a\in G:ag=ga\}\) of every \(g\ne e\) is infinite cyclic.

**Proof.** Use the Cayley tree whose edges join \(x\) to \(xs^{\pm1}\) and \(xt^{\pm1}\). Its distance is \(d(x,y)=|x^{-1}y|\), so left multiplication acts by isometries, and no nonidentity left translation fixes a vertex.

Cancel matching inverse letters at the two ends of the reduced word for \(g\). This writes \(g=ava^{-1}\), where \(v\ne e\) is cyclically reduced: its final letter is not the inverse of its first letter. The word segments from \(av^k\) to \(av^{k+1}\), for \(k\in\mathbb Z\), concatenate without backtracking and form a bi-infinite geodesic \(\ell\). Left multiplication by \(g\) translates this line by \(|v|\) edges.

For a vertex \(x\), let \(p\) be its closest vertex on \(\ell\). The closest vertex is unique, since two different closest vertices would give two different paths between vertices in a tree. The closest vertex to \(gx\) is \(gp\). The path from \(x\) to \(gx\) runs from \(x\) to \(p\), along \(\ell\) from \(p\) to \(gp\), and then to \(gx\). The off-line branches at the distinct vertices \(p\) and \(gp\) cannot meet without creating a cycle. Hence
\[
d(x,gx)=|v|+2d(x,\ell).
\tag{2.2}
\]
In particular, \(\ell\) is characterized intrinsically as the vertices having the smallest displacement under \(g\).

Every element of \(Z_G(g)\) preserves this line, because it preserves the displacement function. An isometry of a discrete line is a translation or a reflection. A reflection conjugates a nonzero translation to its inverse and therefore cannot commute with \(g\). Thus restriction to \(\ell\) gives a homomorphism from \(Z_G(g)\) into the additive group \(\mathbb Z\) of signed translations. It is injective: an element in its kernel fixes a vertex of \(\ell\), and the left action on vertices is free. Its image is a nonzero subgroup of \(\mathbb Z\), since it contains the translation induced by \(g\). Every such subgroup is generated by its smallest positive integer. The centralizer is consequently infinite cyclic. \(\square\)

**Lemma 2.2.** If \(K\subseteq G\) is infinite cyclic and \(\sigma_K\) is the left action on \(\ell^2(G/K)\), then
\[
\left\|\sum_{a\in S}\sigma_K(a)\right\|\le2\sqrt3.
\tag{2.3}
\]

**Proof.** Write \(K=\langle k\rangle\), and put \(F_N=\{k^j:-N\le j\le N\}\). For every fixed \(b\in K\),
\[
\frac{|bF_N\mathbin{\triangle}F_N|}{|F_N|}\longrightarrow0.
\tag{2.4}
\]
Indeed, if \(b=k^m\), the numerator is at most \(2|m|\), while \(|F_N|=2N+1\).

Choose a representative \(r(c)\) of each left coset \(c\in G/K\), and define an isometry
\[
W_N\delta_c=\frac1{\sqrt{|F_N|}}
\sum_{b\in F_N}\delta_{r(c)b}
\quad:\ \ell^2(G/K)\longrightarrow H.
\tag{2.5}
\]
Vectors from different cosets have disjoint supports. For fixed \(a\in G\) and \(c\in G/K\), write \(ar(c)=r(ac)b(a,c)\), with \(b(a,c)\in K\). The squared norm of
\[
\lambda_aW_N\delta_c-W_N\sigma_K(a)\delta_c
\]
is the ratio in (2.4) with \(b=b(a,c)\). It tends to zero. For any finitely supported \(\xi\in\ell^2(G/K)\), only finitely many pairs \((a,c)\) occur when \(a\in S\). Therefore
\[
\left\|\Big(\sum_{a\in S}\lambda_a\Big)W_N\xi
-W_N\Big(\sum_{a\in S}\sigma_K(a)\Big)\xi\right\|
\longrightarrow0.
\]
Since \(W_N\) is isometric, (2.1) bounds the norm of the second expression by \(2\sqrt3\|\xi\|\) in the limit. Finite-support vectors are dense, proving (2.3). The coset representatives need not have any uniform bound: only finitely many of them enter each vector comparison. \(\square\)

**Proposition 2.3.** The operator
\[
C=\sum_{a\in S}\lambda_a\rho_a\in\mathcal A
\tag{2.6}
\]
has \(C\delta_e=4\delta_e\), and its restriction to \(\delta_e^\perp\) has norm at most \(2\sqrt3\). The rank-one projection \(p_e\) onto \(\mathbb C\delta_e\) belongs to \(\mathcal A\).

**Proof.** The representation \(a\mapsto\lambda_a\rho_a\) is conjugation on the basis:
\[
\lambda_a\rho_a\delta_g=\delta_{aga^{-1}}.
\]
The identity gives the one-dimensional fixed summand. Every other conjugacy class has the form \(G/Z_G(g)\), with exactly the coset action of Lemma 2.2. The complement of \(\delta_e\) is the orthogonal direct sum of these conjugacy-class spaces. Lemmas 2.1 and 2.2 bound \(C\) on every summand by \(2\sqrt3\), and the same bound holds on their direct sum.

The operator \(C\) is self-adjoint. Its spectrum consists of \(4\) and a subset of \([-2\sqrt3,2\sqrt3]\); the two pieces are disjoint. For example, the continuous function
\[
f(r)=\frac{\max\{r-2\sqrt3,0\}}{4-2\sqrt3}
\quad(-4\le r\le4)
\tag{2.7}
\]
vanishes on the second piece and has value one at \(4\). Continuous functional calculus gives \(f(C)=p_e\in\mathcal A\). \(\square\)

**Corollary 2.4.** \(\mathcal K(H)\subseteq\mathcal A\), and \(\mathcal K(H)\) is a nonzero proper closed ideal of \(\mathcal A\).

**Proof.** For \(g,h\in G\), the operator \(\lambda_gp_e\lambda_h^*\) sends \(\delta_h\) to \(\delta_g\) and annihilates all other basis vectors. These are all the basis matrix units. Their linear span is norm dense in \(\mathcal K(H)\), so all compact operators belong to \(\mathcal A\). The compact operators form a closed ideal in \(B(H)\), hence in \(\mathcal A\). They are proper because \(H\) is infinite dimensional and \(1\) is not compact. \(\square\)

## 3. Averaging cuts of a reduced word

Let \(\mathcal Q(H)=B(H)/\mathcal K(H)\), and let \(q:B(H)\to\mathcal Q(H)\) be the quotient map. We will prove that multiplication followed by \(q\) is continuous for the spatial tensor norm.

For a reduced word \(g\) of length \(\ell\), denote by \(p_j(g)\) its first \(j\) letters and by \(r_j(g)\) the remaining \(\ell-j\) letters, for \(0\le j\le\ell\). The endpoint cuts are \((e,g)\) and \((g,e)\), and every cut satisfies \(g=p_j(g)r_j(g)\) without cancellation. Define
\[
V\delta_g=\frac1{\sqrt{|g|+1}}
\sum_{j=0}^{|g|}\delta_{p_j(g)}\otimes\delta_{r_j(g)}
\quad:\ H\longrightarrow H\otimes H.
\tag{3.1}
\]

**Lemma 3.1.** The map \(V\) is an isometry. For every fixed \(a,b\in G\), the operator
\[
E_{a,b}=V\lambda_a\rho_b-(\lambda_a\otimes\rho_b)V
\quad:\ H\longrightarrow H\otimes H
\tag{3.2}
\]
is compact.

**Proof.** There are \(|g|+1\) distinct cuts of \(g\), so \(\|V\delta_g\|=1\). A pair of group elements \((u,v)\) determines the product \(uv\). Thus pairs occurring for two different words cannot coincide, and the vectors \(V\delta_g\) are orthonormal. This proves isometry.

Fix \(a,b\), and put \(m=|a|\), \(n=|b|\), \(d=m+n\). Consider a word \(g\) of length \(\ell>d\). Left multiplication by \(a\) can cancel at most \(m\) letters of the beginning of \(g\), and right multiplication by \(b^{-1}\) can cancel at most \(n\) letters at its end. These cancellations cannot meet, because \(\ell>d\).

Consequently every cut with
\[
m\le j\le\ell-n
\tag{3.3}
\]
gives a reduced cut of \(agb^{-1}\) after reducing \(ap_j(g)\) and \(r_j(g)b^{-1}\). The portion of \(g\) beyond the possible cancellations retains its original neighboring letters at the cut. At an endpoint of (3.3) a reduced factor can be empty, which is also an allowed cut. Different \(j\)'s give different cuts: the reduced prefix length increases by one as \(j\) increases through this interval.

Let \(\ell'=|agb^{-1}|\). The two unweighted sets of pairs appearing in \(V\delta_{agb^{-1}}\) and \((\lambda_a\otimes\rho_b)V\delta_g\) therefore have at least \(\ell-d+1\) common pairs. Also \(|\ell'-\ell|\le d\). Since all coefficients are positive real numbers and all pairs in each sum are distinct, their inner product is at least
\[
\frac{\ell-d+1}{\sqrt{(\ell+1)(\ell'+1)}}
\ge\frac{\ell-d+1}{\ell+d+1}.
\]
Both vectors have norm one. Hence
\[
\|E_{a,b}\delta_g\|^2
\le\frac{4d}{\ell+d+1}
\quad(\ell>d).
\tag{3.4}
\]
For \(d=0\), the two vectors agree and the bound is zero.

A bound on individual columns alone would not prove compactness. Here we have additional orthogonality. Every pair \((u,v)\) in the support of \(E_{a,b}\delta_g\) has product \(uv=agb^{-1}\). Different \(g\)'s give different such products. Thus the columns of \(E_{a,b}\) are mutually orthogonal.

Let \(P_N\) be the finite-rank projection onto words of length at most \(N\). Column orthogonality gives
\[
\|E_{a,b}(1-P_N)\|
=\sup_{|g|>N}\|E_{a,b}\delta_g\|
\longrightarrow0
\tag{3.5}
\]
by (3.4). Each \(E_{a,b}P_N\) has finite rank. The operator \(E_{a,b}\) is therefore a norm limit of finite-rank operators, as required. \(\square\)

**Proposition 3.2 (the quotient norm estimate).** For any finite family \(a_i,b_i\in G\), \(c_i\in\mathbb C\),
\[
\left\|q\Big(\sum_i c_i\lambda_{a_i}\rho_{b_i}\Big)\right\|
\le\left\|\sum_i c_i\lambda_{a_i}\otimes\rho_{b_i}\right\|.
\tag{3.6}
\]

**Proof.** Write the joint operator on the left before quotienting as \(T\), and the spatial operator on the right as \(X\). Lemma 3.1 implies that \(XV-VT\) is compact, being a finite sum of compact operators. Since \(V^*V=1\),
\[
V^*XV-T=V^*(XV-VT)
\]
is compact on \(H\). Therefore
\[
\|q(T)\|=\|q(V^*XV)\|\le\|V^*XV\|\le\|X\|.
\]
This is (3.6). \(\square\)

The two concrete inclusions of \(L\) and \(R\) into \(B(H)\) are faithful, so the norm on the right of (3.6) is exactly the spatial tensor norm. Since group polynomials are dense in both factors, (3.6) extends to all finite sums \(\sum_i x_i\otimes y_i\), with \(x_i\in L\) and \(y_i\in R\). For this extension, approximate each factor in norm by a group polynomial and use
\[
\|xy-x'y'\|\le\|x-x'\|\,\|y\|+\|x'\|\,\|y-y'\|
\]
both in the commuting action and in the spatial action.

## 4. The quotient and the ideal lattice

**Theorem 4.1 (Akemann–Ostrand).** Multiplication modulo compact operators gives an isomorphism
\[
\mu:L\otimes_{\min}R\xrightarrow{\ \cong\ }
\mathcal A/\mathcal K(H),
\qquad
\mu\Big(\sum_i x_i\otimes y_i\Big)
=\sum_i x_iy_i+\mathcal K(H).
\tag{4.1}
\]
The only closed two-sided ideals of \(\mathcal A\) are
\[
0,\qquad\mathcal K(H),\qquad\mathcal A.
\tag{4.2}
\]

**Proof.** Commutation of \(L\) and \(R\) makes the algebraic multiplication map multiplicative and *-preserving. Proposition 3.2 and its norm-density extension make its composition with \(q\) contractive for the spatial norm. It therefore extends to a *-homomorphism on \(L\otimes_{\min}R\).

Corollary 2.4 identifies \(q(\mathcal A)\) with \(\mathcal A/\mathcal K(H)\). The extended homomorphism has dense range in this algebra, because products of elements of \(L\) and \(R\) have dense span in \(\mathcal A\). The range of a C*-algebra *-homomorphism is closed, so it is surjective.

Theorem 1.4 makes \(L\) and \(R\) simple. The imported tensor-independence Theorem 2.1 consequently makes \(L\otimes_{\min}R\) simple. Our homomorphism is nonzero: it sends \(1\otimes1\) to \(q(1)\ne0\), since \(H\) is infinite dimensional. Its kernel, a proper closed ideal of a simple algebra, is zero. This proves (4.1).

For completeness, any nonzero ideal \(I\subseteq\mathcal A\) meets \(\mathcal K(H)\) nontrivially. Choose \(0\ne a\in I\). Some basis matrix entry \(\langle a\delta_h,\delta_g\rangle\) is nonzero. Sandwiching \(a\) between the basis matrix units that send \(\delta_g\) to \(\delta_e\) and \(\delta_e\) to \(\delta_h\) gives a nonzero scalar multiple of \(p_e\) in \(I\). Multiplying again by matrix units shows that \(I\) contains every basis matrix unit and hence all of \(\mathcal K(H)\).

The image of \(I\) in \(\mathcal A/\mathcal K(H)\) is a closed ideal: since \(I\) already contains the kernel of the quotient map, it is naturally \(I/\mathcal K(H)\). By (4.1) this quotient algebra is simple. Thus either \(I=\mathcal K(H)\) or its image is the full quotient, in which case \(I=\mathcal A\). This proves (4.2). \(\square\)

In the direction used to describe the quotient, the inverse of (4.1) is
\[
\sum_i x_iy_i+\mathcal K(H)\longmapsto\sum_i x_i\otimes y_i.
\tag{4.3}
\]
Theorem 4.1 proves that this correspondence is well defined and isometric; it is not merely a rule on formal expressions.

The tensor from the earlier lesson also locates the obstruction precisely. If
\[
z=\sum_{a\in S}\lambda_a\otimes\rho_a,
\]
then \(\|z\|_{\min}=2\sqrt3\), while its joint representative \(C\) in (2.6) has norm \(4\). The extra isolated spectral value belongs to the rank-one summand. The quotient removes it and satisfies
\[
\|C+\mathcal K(H)\|=2\sqrt3.
\tag{4.4}
\]
The quotient theorem supplies the ideal and isomorphism statements in the classical free-group example as well as its tensor-norm distinction.

## 5. Exercises with solutions

**Exercise 5.1 (first step).** Put \(x=\lambda_s+\lambda_{s^{-1}}\). Use the partition consisting of words beginning with \(s^{\pm1}\) and its complement to construct an explicit finite average of conjugates of \(x\) with norm strictly less than \(1/10\). Give a sufficient number of terms, without computing the norm of the average directly.

**Solution.** The two words \(tst^{-1}\) and \(ts^{-1}t^{-1}\) begin with \(t\) and end with \(t^{-1}\). Thus the explicit conjugation \(h=t\) works here. If \(C_0\) is the stated set of words and \(D_0\) is its complement, then \((t s^{\pm1}t^{-1})C_0\cap C_0=\varnothing\), and the sets \(s^iD_0\) are pairwise disjoint. The proof of Lemma 1.2 applied to \(\lambda_t x\lambda_t^*\) gives
\[
\left\|\frac1n\sum_{i=1}^n
\lambda_{s^it}x\lambda_{s^it}^*\right\|
\le\frac{2\|x\|}{\sqrt n}\le\frac4{\sqrt n}.
\]
Taking \(n=1601\) gives \(4/\sqrt{1601}<1/10\). This is a sufficient bound; it does not assert that this number of terms is optimal.

**Exercise 5.2 (application).** Replace the word-cut isometry by the endpoint isometry \(V_0\delta_g=\delta_g\otimes\delta_e\). For \(b\ne e\), show that
\[
V_0\rho_b-(1\otimes\rho_b)V_0
\]
is not compact. Explain which feature of the averaging in (3.1) fixes this failure.

**Solution.** Its value on \(\delta_g\) is
\[
\delta_{gb^{-1}}\otimes\delta_e-
\delta_g\otimes\delta_{b^{-1}}.
\]
The two basis vectors are different, so this vector has norm \(\sqrt2\) for every \(g\). For different \(g\)'s these differences are orthogonal: within each difference the product of the two coordinates is \(gb^{-1}\), and that product distinguishes the input word. Thus the squared operator absolute value is \(2\,1_H\), which is not compact on infinite-dimensional \(H\). Equivalently, images of the standard orthonormal basis fail to tend to zero in norm, whereas this is necessary for compactness.

The endpoint map has left equivariance but retains a fixed right endpoint error. In (3.1), multiplication changes only a bounded number of cuts near the ends of a long word. Most cuts remain common after multiplication. Normalizing the average makes the squared error tend to zero as in (3.4), and the product-coordinate orthogonality turns that decay into the operator-norm estimate (3.5).

**Exercise 5.3 (further step).** Prove that \(\mathcal A\) has a unique tracial state and that this state annihilates \(\mathcal K(H)\). In particular, explain why the unique trace on \(\mathcal A\) is not faithful, although the canonical traces on \(L\) and \(R\) are faithful.

**Solution.** Let \(\omega\) be a tracial state on \(\mathcal A\). The mutually orthogonal rank-one projections \(p_g=\lambda_gp_e\lambda_g^*\) all have the same value \(\omega(p_e)\). For any \(N\) distinct group elements,
\[
N\omega(p_e)=\omega\Big(\sum_{i=1}^Np_{g_i}\Big)\le1.
\]
Letting \(N\) increase gives \(\omega(p_e)=0\). Cauchy–Schwarz then makes \(\omega\) zero on every basis matrix unit; for example, a matrix unit \(e_{g,h}\) satisfies \(e_{g,h}^*e_{g,h}=p_h\). Norm continuity gives \(\omega(\mathcal K(H))=0\). The state descends to a tracial state on \(\mathcal A/\mathcal K(H)\), hence, by (4.1), to a tracial state \(\widetilde\omega\) on \(L\otimes_{\min}R\).

Write \(\tau_L,\tau_R\) for the unique traces of Theorem 1.4. The restriction of \(\widetilde\omega\) to \(1\otimes R\) is \(\tau_R\). For \(b\in R_+\), the functional
\[
a\longmapsto\widetilde\omega(a\otimes b)
\]
on \(L\) is positive and tracial, with value \(\tau_R(b)\) at \(1\). If this value is zero the functional is zero; otherwise divide by it and use uniqueness of the tracial state on \(L\). In both cases
\[
\widetilde\omega(a\otimes b)=\tau_L(a)\tau_R(b).
\]
Every element of \(R\) is a linear combination of positive elements, so this equality holds for arbitrary \(b\). Algebraic tensor density then gives \(\widetilde\omega=\tau_L\otimes\tau_R\).

Conversely the product state \(\tau_L\otimes\tau_R\) exists on the spatial product and is tracial, as is checked first on elementary products and then by norm continuity. Pull it back through the quotient isomorphism to obtain a trace on \(\mathcal A\). This proves existence and uniqueness. The resulting trace kills the nonzero projection \(p_e\), so it is not faithful. Its restrictions to \(L\) and \(R\) are precisely their faithful canonical traces.

## References

Powers proved simplicity of the reduced free-group C*-algebra; Akemann and Ostrand identified the spatial quotient by the compact ideal. The proofs here give the partition estimate, cyclic-stabilizer comparison, and word-cut compactness argument explicitly, while reusing the earlier spatial simplicity and adjacency results.

- [Powers] R. T. Powers, *Simplicity of the C\*-algebra associated with the free group on two generators*, Duke Mathematical Journal **42** (1975), 151–156. [Publisher DOI](https://doi.org/10.1215/S0012-7094-75-04213-1).
- [de la Harpe] P. de la Harpe, *On simplicity of reduced C\*-algebras of groups*, arXiv:math/0509450v1, 20 September 2005. [Free preprint](https://arxiv.org/pdf/math/0509450v1). This freely accessible exposition treats Powers’ result.
- [Akemann–Ostrand] C. A. Akemann and P. A. Ostrand, *On a tensor product C\*-algebra associated with the free group on two generators*, Journal of the Mathematical Society of Japan **27** (1975), 589–599. [Free published PDF](https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_589/_pdf) · [Publisher DOI](https://doi.org/10.2969/jmsj/02740589).

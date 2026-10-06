# Schur–Weyl duality

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Independent AI review is not yet recorded. Public domain (CC0).*

A tensor has two kinds of symmetry. We may apply the same linear transformation to every factor, or permute the factors. These operations commute. Schur–Weyl duality says something stronger: each operation generates the entire algebra commuting with the other. The resulting decomposition pairs the representations of a finite symmetric group with the polynomial representations of a general linear group.

We use Maschke's theorem and the meaning of complete reducibility from [Representations and complete reducibility](RT-FIN-01.md), Theorem 2.3 and Lemma 2.4. Finite-group character orthogonality and completeness come from [Characters and the orthogonality relations](RT-FIN-02.md), Corollary 2.2 and Theorem 4.1. The Young symmetrizers and their ranks come from [Young tableaux and Young symmetrizers](RT-FIN-13.md), Theorem 3.1, Theorem 4.3 and Corollary 4.5; standard-tableau dimensions come from [Branching, Jucys–Murphy elements and Young's seminormal form](RT-FIN-14.md), Corollary 4.3. We use the Schur polynomials and Frobenius characteristic from [Characters of symmetric groups and symmetric functions](RT-FIN-15.md), Theorem 2.1, Lemma 2.2 and Theorem 3.1, especially its identity (34). That lesson also proves the Littlewood–Richardson rule used below. Basic comparisons are [Etingof et al.] and [Gruson–Serganova].

All vector spaces and algebras in this lesson are finite-dimensional over \(\mathbb C\). An algebra of operators contains the identity operator. Put \(m=\dim V\). The main arguments concern \(m,n\geq1\). Our conventions are \(V^{\otimes0}=\mathbb C\), \(S_0=\{1\}\), and \(S_\varnothing(V)=\mathbb C\). If \(V=0\) and \(n>0\), its tensor power and every Schur module of degree \(n\) are zero. These conventions settle the degenerate cases separately.

## 1. The operators that preserve tensor symmetry

Set \(E=V^{\otimes n}\). We use left actions, with permutation composition read from right to left:

\[
\begin{aligned}
P_\sigma(v_1\otimes\cdots\otimes v_n)
 &=v_{\sigma^{-1}(1)}\otimes\cdots\otimes v_{\sigma^{-1}(n)},\\
G_g(v_1\otimes\cdots\otimes v_n)
 &=gv_1\otimes\cdots\otimes gv_n.
\end{aligned}
\tag{1}
\]

The inverse in the first formula gives \(P_\sigma P_\tau=P_{\sigma\tau}\); the second gives \(G_gG_h=G_{gh}\). Applying both formulas to a pure tensor gives \(P_\sigma G_g=G_gP_\sigma\).

Already for \(n=2\), the flip \(P(v\otimes w)=w\otimes v\) commutes with every \(g\otimes g\). Its two eigenspaces are the symmetric and alternating tensors. For larger \(n\), different Young diagrams replace these two symmetries. Before identifying the diagrams, we determine exactly which operators commute with all the permutations.

**Lemma 1.1 (polarization in a tensor space).** If \(X\) is a complex vector space and \(n\geq1\), the invariant subspace \((X^{\otimes n})^{S_n}\) is spanned by the tensors \(x^{\otimes n}\), \(x\in X\). More explicitly,

\[
\sum_{\sigma\in S_n}x_{\sigma(1)}\otimes\cdots\otimes x_{\sigma(n)}
=\sum_{J\subseteq\{1,\ldots,n\}}
 (-1)^{n-|J|}\left(\sum_{j\in J}x_j\right)^{\otimes n}.
\tag{2}
\]

**Proof.** Expand the right side by multilinearity. A term indexed by a function \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\) occurs for the subsets \(J\) containing its image. If that image has size \(r\), its coefficient is

\[
\sum_{J\supseteq\operatorname{im}f}(-1)^{n-|J|}
 =\begin{cases}0&r<n,\\1&r=n.\end{cases}
\tag{3}
\]

The zero case is the expansion of \((1-1)^{n-r}\). A function with image of size \(n\) is a permutation, so precisely the left side survives.

Average any tensor over its \(S_n\)-orbit by dividing the sum by \(n!\). This averaging operator is the identity on invariant tensors and maps every tensor to an invariant tensor. Pure tensors span the whole tensor space, so their orbit averages span its invariant subspace. Formula (2) expresses each such average as a linear combination of powers. \(\square\)

The lemma concerns an invariant subspace of the tensor power. It is canonically isomorphic, by averaging, to the usual symmetric-power quotient. Keeping the subspace description makes the next operator calculation literal.

**Lemma 1.2 (invertible shifts suffice).** For \(a\in\operatorname{End}(V)\), its tensor power \(a^{\otimes n}\) lies in the span of \(g^{\otimes n}\) with \(g\in GL(V)\). Moreover, a polynomial in the matrix entries which vanishes on all invertible matrices is the zero polynomial.

**Proof.** The polynomial \(\det(a+tI)\) is monic of degree \(m\), so it has only finitely many roots. Choose distinct \(t_0,\ldots,t_n\) avoiding them. The operator-valued polynomial \(F(t)=(a+tI)^{\otimes n}\) has degree at most \(n\). Lagrange interpolation, applied to each matrix entry, gives

\[
a^{\otimes n}=F(0)
=\sum_{k=0}^{n}
 \left(\prod_{j\ne k}\frac{-t_j}{t_k-t_j}\right)
 (a+t_kI)^{\otimes n}.
\tag{4}
\]

Every matrix inside a tensor power on the right is invertible.

Now let \(Q\) be a polynomial vanishing on every invertible matrix. For any fixed \(a\), the polynomial \(Q(a+tI)\) vanishes for every \(t\) except possibly the finitely many roots of \(\det(a+tI)\). It therefore vanishes identically, giving \(Q(a)=0\). Thus \(Q\) vanishes at every matrix. A polynomial over an infinite field vanishing at every point is zero: prove this by induction on the number of variables, regarding it as a polynomial in the last variable and using the one-variable root bound for every choice of the other variables. This proves the asserted density without an algebraic-geometric prerequisite. \(\square\)

**Proposition 1.3 (the permutation commutant).**

\[
\operatorname{End}_{S_n}(V^{\otimes n})
=\operatorname{span}_{\mathbb C}\{g^{\otimes n}:g\in GL(V)\}.
\tag{5}
\]

**Proof.** The natural map

\[
(\operatorname{End}V)^{\otimes n}\longrightarrow
 \operatorname{End}(V^{\otimes n}),\qquad
a_1\otimes\cdots\otimes a_n\longmapsto
 [v_1\otimes\cdots\otimes v_n\mapsto a_1v_1\otimes\cdots\otimes a_nv_n]
\tag{6}
\]

is an algebra isomorphism. To verify bijectivity, choose a basis of \(V\). Tensor products of its matrix units map to all the matrix units in the corresponding tensor basis of \(V^{\otimes n}\), once each. Conjugation by \(P_\sigma\) permutes the factors on the left of (6). Consequently, the operators commuting with every \(P_\sigma\) correspond exactly to \(((\operatorname{End}V)^{\otimes n})^{S_n}\).

Lemma 1.1 spans this invariant space by \(a^{\otimes n}\), and Lemma 1.2 replaces each power by powers of invertible matrices. Conversely, every \(g^{\otimes n}\) commutes with the permutations by (1). This proves both inclusions. \(\square\)

The span in (5) is an algebra: the product of two generators is \((gh)^{\otimes n}\), and it contains the identity. The argument has not assumed that the general linear group acts completely reducibly. That fact will follow from the finite symmetric group.

*Reference:* [Gruson–Serganova, Chapter 6, Lemma 2.7]; [Etingof et al., Proposition 4.58]. Formula (4) makes the invertible-shift argument explicit.

## 2. Why a commutant has simple multiplicity spaces

For an algebra \(A\subseteq\operatorname{End}(E)\), write

\[
A'=\{b\in\operatorname{End}(E):ba=ab\text{ for every }a\in A\}.
\tag{7}
\]

A finite-dimensional unital algebra is **semisimple** if its left regular module is a direct sum of simple modules. A simple module is nonzero and has no nonzero proper submodule. We need some consequences of this definition, rather than assuming a structure theorem for algebras.

**Lemma 2.1 (complements and scalar endomorphisms).** Every finite-dimensional module over a semisimple algebra is completely reducible. Its submodules have invariant complements. If \(U,U'\) are simple complex modules, then \(\operatorname{Hom}_A(U,U')=0\) unless they are isomorphic, and \(\operatorname{End}_A(U)=\mathbb C I\).

**Proof.** If a module \(M\) is a sum of finitely many simple submodules, choose a maximal subcollection whose sum is direct. Any remaining simple submodule either lies in that sum or has zero intersection with it, by simplicity. The second possibility contradicts maximality. Thus the chosen direct sum is all of \(M\).

Choose a vector-space basis \(v_1,\ldots,v_r\) of an arbitrary module \(M\). The map \(A^r\to M\), \((a_1,\ldots,a_r)\mapsto\sum a_jv_j\), is onto because \(A\) contains the identity. The regular module and hence \(A^r\) are sums of simple modules. Their images in \(M\) are simple or zero, so the preceding argument makes \(M\) completely reducible.

For completeness, if \(M=\bigoplus_j M_j\) with \(M_j\) simple and \(N\subseteq M\), choose a maximal subcollection with \(N\cap\bigoplus_{j\in J}M_j=0\). If \(N+\bigoplus_{j\in J}M_j\ne M\), some \(M_k\) is not contained in this sum. Its intersection with the sum is zero, so adding \(k\) preserves the required zero intersection, a contradiction. The chosen sum is a complement of \(N\).

A nonzero homomorphism between simple modules is an isomorphism, since its kernel and image are submodules. For an endomorphism \(f\) of a simple complex module, choose an eigenvalue \(c\). The endomorphism \(f-cI\) has nonzero kernel and hence is zero. These are the module versions of Schur's lemma. \(\square\)

**Lemma 2.2 (simultaneous finite density).** If \(U_1,\ldots,U_r\) are pairwise nonisomorphic simple modules over a semisimple complex algebra \(A\), then the action map

\[
A\longrightarrow\bigoplus_{i=1}^{r}\operatorname{End}(U_i)
\tag{8}
\]

is onto.

**Proof.** Choose a basis \(u_{i1},\ldots,u_{id_i}\) in each \(U_i\), and consider the \(A\)-linear map

\[
A\longrightarrow T=\bigoplus_i U_i^{\oplus d_i},
\qquad a\longmapsto (a u_{ij})_{i,j}.
\tag{9}
\]

Its image \(L\) is a submodule. If \(L\ne T\), Lemma 2.1 supplies a nonzero map \(F:T\to U_k\) vanishing on \(L\): take a simple summand of a complement of \(L\) and project onto it. That summand is isomorphic to some \(U_k\), since a nonzero projection to it from \(T\) is nonzero on one of the displayed simple summands.

Schur's lemma says that \(F\) is zero on all the \(U_i\) with \(i\ne k\), and on the \(d_k\) copies of \(U_k\) it has the form \((z_1,\ldots,z_{d_k})\mapsto\sum_j c_jz_j\). Applying it to the image of \(1\in A\) gives \(\sum_jc_ju_{kj}=0\). Linear independence forces every \(c_j=0\), contradicting \(F\ne0\). Thus (9) is onto. Arbitrarily prescribing the images of every basis vector in every \(U_i\) is exactly the surjectivity of (8). \(\square\)

This is the finite-dimensional form of Jacobson's density mechanism: enough independent vectors force enough operators.

**Theorem 2.3 (double centralizer).** Let \(E\ne0\), let \(A\subseteq\operatorname{End}(E)\) be semisimple and contain \(I_E\), and put \(B=A'\). Then \(B\) is semisimple and \(B'=A\). For the distinct simple \(A\)-modules \(U_i\) occurring in \(E\), put \(W_i=\operatorname{Hom}_A(U_i,E)\). Evaluation gives a canonical isomorphism

\[
\bigoplus_i U_i\otimes W_i\longrightarrow E,
\qquad u\otimes f\longmapsto f(u).
\tag{10}
\]

The \(W_i\) are a complete list of pairwise nonisomorphic simple \(B\)-modules. On this decomposition the two algebras are

\[
A=\bigoplus_i\operatorname{End}(U_i)\otimes I_{W_i},
\qquad
B=\bigoplus_i I_{U_i}\otimes\operatorname{End}(W_i).
\tag{11}
\]

**Proof.** Decompose \(E\) as an \(A\)-module by Lemma 2.1. If \(U_i\) occurs \(r_i\) times, Schur's lemma identifies \(W_i\) with \(\mathbb C^{r_i}\); evaluation identifies \(U_i\otimes W_i\) with that isotypic summand. This proves (10), independently of a chosen decomposition into individual copies.

By Lemma 2.2, \(A\) acts as an arbitrary operator on every \(U_i\), with the choices independent for different \(i\). Since \(A\) is an actual subalgebra of \(\operatorname{End}(E)\), its action is faithful. This proves the first equality of (11).

An operator commuting with \(A\) preserves its isotypic summands: the identity in a single block of \(A\) is the projection onto that summand. Between two copies of \(U_i\), an intertwiner is scalar; between different types it is zero. Thus the full commuting algebra has the second form in (11). Its action on \(W_i\) is \(b\cdot f=b\circ f\).

Here are explicit facts about matrix algebras which finish the proof. If \(M\) is a unital module over \(\operatorname{Mat}_d(\mathbb C)\), with matrix units \(e_{ab}\), then

\[
\mathbb C^d\otimes e_{11}M\longrightarrow M,
\qquad v_a\otimes h\longmapsto e_{a1}h
\tag{12}
\]

is an isomorphism, with inverse \(z\mapsto\sum_a v_a\otimes e_{1a}z\). The matrix-unit identities verify both compositions and the action. Hence every such module is a direct sum of defining modules \(\mathbb C^d\), and this defining module is simple: matrix units send any nonzero vector to spanning basis vectors. For a finite direct sum of matrix algebras, central block identities first split every module into its block components. Consequently \(B\) is semisimple, and its simples are exactly the defining modules \(W_i\), distinguished by their block identities.

Finally an operator commuting with \(B\) must again preserve these blocks. Within \(U_i\otimes W_i\), write it as a matrix of operators on \(W_i\) using a basis of \(U_i\). Each entry must commute with every matrix unit on \(W_i\), and therefore is scalar: commuting with diagonal units makes it diagonal, and commuting with off-diagonal units equates its diagonal entries. The operator is an arbitrary element of \(\operatorname{End}(U_i)\otimes I_{W_i}\). These are precisely the first blocks in (11), proving \(B'=A\). \(\square\)

The identity assumption has content. The nonunital algebra \(A=0\) on a nonzero space has \(A'=\operatorname{End}(E)\) and \(A''=\mathbb C I\), rather than \(0\). We use the identity-preserving convention throughout the theorem.

To see the two actions inside one block, take \(\dim U=2\), \(\dim W=3\):

\[
\begin{array}{c|ccc}
 &w_1&w_2&w_3\\ \hline
u_1&u_1\otimes w_1&u_1\otimes w_2&u_1\otimes w_3\\
u_2&u_2\otimes w_1&u_2\otimes w_2&u_2\otimes w_3
\end{array}
\tag{13}
\]

*Figure 1. Basis vectors in one six-dimensional block of (10). An operator in \(A\) changes the row index by the same \(2\times2\) matrix in every column. An operator in \(B\) changes the column index by the same \(3\times3\) matrix in every row. The grid displays the actual tensor factors; it does not identify the two different algebras.*

*Reference:* [Gruson–Serganova, Chapter 5, Theorem 2.9 and Corollary 2.12]; [Etingof et al., Theorem 4.54]. Lemma 2.2 and the matrix-unit calculation supply all the finite algebra facts needed here.

## 3. The Young diagram labels both sides

Let \(V_\lambda\) be the irreducible \(S_n\)-module with the Young-ideal convention \(\mathbb C[S_n]a_tb_t\). Define

\[
S_\lambda(V)=\operatorname{Hom}_{S_n}(V_\lambda,V^{\otimes n}),
\qquad (g\cdot f)(u)=g^{\otimes n}f(u).
\tag{14}
\]

This is the **Schur module** of shape \(\lambda\). Its irreducibility will be a conclusion.

**Theorem 3.1 (Schur–Weyl duality).** The two algebras generated by \(S_n\) and \(GL(V)\) on \(V^{\otimes n}\) are mutual commutants. As a representation of \(GL(V)\times S_n\), evaluation gives

\[
V^{\otimes n}\cong
\bigoplus_{\substack{\lambda\vdash n\\\ell(\lambda)\leq m}}
 S_\lambda(V)\otimes V_\lambda.
\tag{15}
\]

Every displayed Schur module is nonzero, irreducible and pairwise nonisomorphic as a \(GL(V)\)-module. For all partitions of \(n\),

\[
S_\lambda(V)=0\quad\Longleftrightarrow\quad\ell(\lambda)>m.
\tag{16}
\]

**Proof.** Write \(A\) for the image of \(\mathbb C[S_n]\) in \(\operatorname{End}(V^{\otimes n})\). It is semisimple. Indeed, every \(A\)-module is a module for \(\mathbb C[S_n]\) through the quotient map, and Maschke supplies invariant complements; in particular its regular module is completely reducible. Let \(B=A'\). Proposition 1.3 identifies \(B\) with the span of the general linear group operators. Theorem 2.3 gives \(B'=A\), the evaluation decomposition, and simple pairwise nonisomorphic multiplicity spaces. A subspace or map is stable under, or commutes with, \(GL(V)\) exactly when it is stable under, or commutes with, its linear span \(B\). Thus the \(B\)-module assertions are exactly the required group assertions.

It remains to determine which multiplicity spaces occur. For a tableau \(t\) of shape \(\lambda\), set \(c_t=a_tb_t\), with \(a_t\) the row sum and \(b_t\) the signed column sum. The earlier rank theorem says that \(c_t\) has rank one on \(V_\lambda\) and zero on the other symmetric-group irreducibles. Therefore \(c_tV^{\otimes n}\ne0\) exactly when \(S_\lambda(V)\ne0\).

If \(\ell(\lambda)>m\), the first column has more than \(m\) tensor positions. In each tensor-basis vector some two of their basis labels agree. Pair terms of that column's signed permutation sum by the transposition of those positions. The paired vectors agree and their signs are opposite. Thus its alternation is zero, \(b_tV^{\otimes n}=0\), and hence \(c_tV^{\otimes n}=0\).

If \(\ell(\lambda)\leq m\), choose a basis \(v_1,\ldots,v_m\) and a pure tensor \(z_t\) whose factor at a box in row \(i\) is \(v_i\). Every row permutation fixes \(z_t\). In \(a_tb_tz_t\), a term \(pqz_t\), with \(p\) a row permutation and \(q\) a column permutation, can equal \(z_t\) only if \(qz_t=p^{-1}z_t=z_t\). The labels within each column are distinct, so this forces \(q=1\). The coefficient of \(z_t\) is consequently

\[
|R_t|=\prod_i\lambda_i!>0.
\tag{17}
\]

Thus \(c_t\) acts nontrivially. This proves (16), finishes the list in (15), and completes the theorem. \(\square\)

With \(e_t=c_t/\nu_\lambda\), where \(\nu_\lambda=n!/\dim V_\lambda\), the decomposition also gives

\[
e_tV^{\otimes n}\cong S_\lambda(V)\otimes e_tV_\lambda
\cong S_\lambda(V).
\tag{18}
\]

The last isomorphism requires choosing a nonzero vector in the one-dimensional space \(e_tV_\lambda\). The Hom description (14) avoids that choice. The image of the unnormalized symmetrizer is the same subspace as the image of \(e_t\).

For a linear map \(f:V\to W\), the map \(f^{\otimes n}\) commutes with permutations. Postcomposition therefore defines \(S_\lambda(f):S_\lambda(V)\to S_\lambda(W)\). Identities and compositions are preserved, so this defines the Schur functor on finite-dimensional vector spaces. Moreover \(S_\lambda(tf)=t^nS_\lambda(f)\). These functors are generally not additive: for example \(\operatorname{Sym}^2(V\oplus W)\) has the additional summand \(V\otimes W\).

The algebra action of \(\mathbb C[S_n]\) is faithful exactly when \(m\geq n\): all its simple blocks occur then, whereas the sign block \((1^n)\) vanishes when \(m<n\). This is a statement about the group algebra, not just its group elements. For \(m\geq2\), the group action itself is faithful even if \(m<n\): a nonidentity permutation moves some position, and a basis tensor with one \(v_2\) in that position and \(v_1\)'s elsewhere is changed by it.

*Comparison:* [Gruson–Serganova, Chapter 6, Theorem 2.4, Lemma 2.9, Corollary 2.10 and Definition 2.11]. The finite-dimensional characteristic-zero hypotheses and row count agree. Formula (1) fixes a left action using \(\sigma^{-1}\), and (14) defines the multiplicity space intrinsically. The coefficient test in the proof verifies nonvanishing for every allowed shape, including \(m<n\); faithfulness of the symmetric-group action is claimed only for \(m\geq n\).

## 4. A cycle trace determines the character

Write \(\chi^\lambda\) for the character of \(V_\lambda\), and \(\chi_{S_\lambda}\) for that of the Schur module. Let \(\sigma\) have cycle lengths \(\mu_1,\ldots,\mu_r\). If \(g=\operatorname{diag}(x_1,\ldots,x_m)\), a tensor-basis vector contributes to \(\operatorname{Tr}(g^{\otimes n}P_\sigma)\) only when its indices are constant around every cycle. A cycle of length \(a\) then contributes \(\sum_i x_i^a=p_a(x)\). Independent cycles give

\[
\operatorname{Tr}(g^{\otimes n}P_\sigma)
 =p_{\mu_1}(x)\cdots p_{\mu_r}(x)=p_\mu(x).
\tag{19}
\]

For arbitrary \(g\), the same basis calculation sums its matrix entries around each cycle. A cycle of length \(a\) gives \(\sum_{i_1,\ldots,i_a}g_{i_1i_2}\cdots g_{i_ai_1}=\operatorname{Tr}(g^a)\). Thus more generally

\[
\operatorname{Tr}(g^{\otimes n}P_\sigma)
 =\prod_{j=1}^{r}\operatorname{Tr}(g^{\mu_j}).
\tag{20}
\]

**Theorem 4.1 (Schur characters).** For every \(\lambda\vdash n\),

\[
\chi_{S_\lambda}(\operatorname{diag}(x_1,\ldots,x_m))
 =s_\lambda(x_1,\ldots,x_m).
\tag{21}
\]

Here the left side extends polynomially to zero coordinates. For any \(g\in GL(V)\), it is the same Schur polynomial in the eigenvalues of \(g\), counted with multiplicity. In particular,

\[
\dim S_\lambda(\mathbb C^m)=s_\lambda(1,\ldots,1),
\qquad
\chi_{S_\lambda}(g)
 =\frac1{n!}\sum_{\sigma\in S_n}
 \chi^\lambda(\sigma^{-1})\prod_{c\text{ cycle of }\sigma}
 \operatorname{Tr}(g^{|c|}).
\tag{22}
\]

**Proof.** Taking the trace of the two commuting operators on (15), and including zero Schur modules for the omitted shapes, gives

\[
p_\mu(x)=\sum_{\lambda\vdash n}
 \chi^\lambda(\mu)\chi_{S_\lambda}(g).
\tag{23}
\]

The preceding symmetric-function lesson proves the identity

\[
p_\mu(x)=\sum_{\lambda\vdash n}\chi^\lambda(\mu)s_\lambda(x).
\tag{24}
\]

The irreducible characters \(\chi^\lambda\) form a basis of class functions on \(S_n\). Fixing \(x\) and comparing their coefficients in (23) and (24) proves (21). The operators \(g^{\otimes n}\), and their restrictions to the fixed multiplicity spaces, have matrix entries polynomial in those of \(g\). Therefore the identity extends from nonzero \(x_i\) to all \(x_i\), either by Lemma 1.2 or by the one-variable root argument successively in the coordinates.

The same decomposition and finite-group character orthogonality extract the coefficient of \(\chi^\lambda\) in the function \(\sigma\mapsto\operatorname{Tr}(g^{\otimes n}P_\sigma)\). Formula (20) gives exactly the last formula of (22); the inverse supplies the complex-conjugate character in the orthogonality pairing. Every complex matrix is triangularizable: choose an eigenvector, then proceed on the quotient by its line, inductively. Its powers have diagonal entries equal to the corresponding powers of its eigenvalues. Formula (20) and the coefficient calculation are consequently the same as for a diagonal matrix with those eigenvalues. This proves the assertion for every \(g\), including nondiagonalizable ones. At \(g=I\), trace is dimension. \(\square\)

There is a second interpretation of the dimension. By the tableau formula in Theorem 2.1 of the preceding lesson, it counts semistandard tableaux of shape \(\lambda\) with entries in \(\{1,\ldots,m\}\). A column longer than \(m\) is impossible. If there are at most \(m\) rows, filling row \(i\) with \(i\)'s gives such a tableau. This independently explains the nonvanishing condition (16).

**Proposition 4.2 (dimension product).** If \(\ell(\lambda)\leq m\), pad \(\lambda\) by zeros to \(m\) parts. Then

\[
\dim S_\lambda(\mathbb C^m)
 =\prod_{1\leq i<j\leq m}
 \frac{\lambda_i-\lambda_j+j-i}{j-i}.
\tag{25}
\]

**Proof.** Put \(\beta_j=\lambda_j+m-j\), \(\delta_j=m-j\), and substitute \(x_i=q^{m-i}\) into the bialternant formula for \(s_\lambda\). The numerator is the Vandermonde determinant in \(q^{\beta_1},\ldots,q^{\beta_m}\); the denominator is the same determinant with \(\beta\) replaced by \(\delta\). Therefore, as a rational identity in \(q\),

\[
s_\lambda(q^{m-1},q^{m-2},\ldots,1)
 =\prod_{i<j}\frac{q^{\beta_i}-q^{\beta_j}}
                         {q^{\delta_i}-q^{\delta_j}}.
\tag{26}
\]

For nonnegative integers \(a>b\),

\[
q^a-q^b=(q-1)q^b(1+q+\cdots+q^{a-b-1}).
\tag{27}
\]

The sequences \(\beta\) and \(\delta\) are strictly decreasing. In each quotient of (26), cancel \(q-1\) using (27) and then set \(q=1\). The quotient becomes \((\beta_i-\beta_j)/(\delta_i-\delta_j)\). The left side is a polynomial in \(q\), so this evaluation is legitimate; it is \(s_\lambda(1^m)\). Since \(\delta_i-\delta_j=j-i\), (25) follows from (22). No division by a zero numerical Vandermonde was made. \(\square\)

For \(m=1\), the product is empty and equals \(1\); the permitted shapes are single rows. For a shape longer than \(m\), use (16), not (25) with discarded positive parts. The omitted parts cannot be padded away.

*Proof route:* [the symmetric-function lesson, Theorem 2.1 and Theorem 3.1](RT-FIN-15.md#theorem-2-1) supplies the bialternant and labelled power-sum identity (24). The cycle-trace computation (20), finite-group orthogonality and cancellation of \(q-1\) in (27) prove the character and dimension formulas here. No highest-weight classification or numerical division by a vanishing Vandermonde is assumed.

## 5. Why these are all polynomial representations

A representation \(\rho:GL_m(\mathbb C)\to GL(M)\) is **polynomial** if its matrix entries are polynomials in the entries of \(g\). It is homogeneous of degree \(n\) if those polynomials are homogeneous of degree \(n\), equivalently \(\rho(tg)=t^n\rho(g)\) for nonzero scalars \(t\). These properties are independent of bases. Entries involving negative powers of \(\det g\) belong to the larger class of rational representations; that larger class is not meant by “polynomial” here.

**Theorem 5.1 (polynomial classification).** Every finite-dimensional polynomial representation of \(GL_m(\mathbb C)\) is completely reducible. Its irreducibles are exactly \(S_\lambda(\mathbb C^m)\), for partitions of any nonnegative integer with \(\ell(\lambda)\leq m\), with no repetitions. The homogeneous representations of degree \(n\) use exactly the shapes \(\lambda\vdash n\).

**Proof for one degree.** Let \(P_n\) be the vector space of homogeneous polynomials of degree \(n\) in \(m^2\) matrix entries. For \(g\in GL_m\), write \(\operatorname{ev}_g\in P_n^*\) for evaluation at \(g\). These functionals span \(P_n^*\). Otherwise a nonzero element of the dual of \(P_n^*\), identified with \(P_n\), would vanish at every invertible matrix, contradicting Lemma 1.2.

Write \(D_n=\operatorname{span}\{g^{\otimes n}:g\in GL_m\}\). The matrix entries of \(g^{\otimes n}\) are precisely products of \(n\) matrix entries, with repetitions allowed; collectively they include every degree-\(n\) monomial. Hence

\[
\sum_k c_k g_k^{\otimes n}=0
\quad\Longleftrightarrow\quad
\sum_k c_k\operatorname{ev}_{g_k}=0\text{ in }P_n^*.
\tag{28}
\]

If \(\rho\) is homogeneous of degree \(n\), each entry of \(\rho(g)\) belongs to \(P_n\). Thus the same relation forces \(\sum_k c_k\rho(g_k)=0\). The rule

\[
D_n\longrightarrow\operatorname{End}(M),
\qquad g^{\otimes n}\longmapsto\rho(g)
\tag{29}
\]

is well-defined and linear. It preserves the identity and multiplication, since it does so on the spanning generators: \(g^{\otimes n}h^{\otimes n}=(gh)^{\otimes n}\) and \(\rho(g)\rho(h)=\rho(gh)\). It therefore makes \(M\) a unital \(D_n\)-module. By Theorems 2.3 and 3.1, \(D_n\) is the direct sum of full matrix algebras on the Schur modules of degree \(n\). Calculation (12) proves directly that its modules are completely reducible with exactly these simples. This proves the homogeneous assertion, including degree zero, where \(P_0=D_0=\mathbb C\).

**Proof for all degrees.** For a general polynomial representation, expand its scalar-matrix restriction as a finite sum

\[
\rho(tI)=\sum_{d=0}^{N}t^d Q_d.
\tag{30}
\]

The identity \(\rho(sI)\rho(tI)=\rho(stI)\), for nonzero \(s,t\), is a polynomial identity. Equating coefficients of \(s^dt^e\) gives \(Q_dQ_e=0\) for \(d\ne e\), and \(Q_d^2=Q_d\). At \(t=1\) it gives \(\sum_dQ_d=I\). Each \(Q_d\) commutes with every \(\rho(g)\), by the same coefficient comparison applied to scalar commutation. Hence

\[
M=\bigoplus_d Q_dM
\tag{31}
\]

is a decomposition into invariant subspaces. On \(Q_dM\), the equation \(\rho(tg)=\rho(tI)\rho(g)\) becomes \(\rho(tg)=t^d\rho(g)\). Polynomial coefficient comparison shows that the entries there are homogeneous of degree \(d\). Apply the one-degree proof to each summand.

Within a degree the simples are pairwise distinct by Schur–Weyl duality. Across different degrees, the scalar \(tI\) acts by different powers \(t^d\), so they cannot be isomorphic. This proves every assertion. \(\square\)

The proof relates polynomial representations to a finite algebra of operator powers. It does not require the classification of Lie algebras or integration over a compact group.

**Corollary 5.2 (products and determinant shifts).** For partitions \(\alpha,\beta\),

\[
S_\alpha(V)\otimes S_\beta(V)
\cong\bigoplus_{\substack{\nu\vdash|\alpha|+|\beta|\\\ell(\nu)\leq m}}
 S_\nu(V)^{\oplus c^\nu_{\alpha\beta}},
\tag{32}
\]

where \(c^\nu_{\alpha\beta}\) is the Littlewood–Richardson coefficient proved in the preceding lesson. Zero Schur modules are permitted on either side. For \(\ell(\lambda)\leq m\), pad \(\lambda\) to \(m\) parts. For \(r\geq0\),

\[
S_{\lambda+(r^m)}(V)\cong (\det V)^{\otimes r}\otimes S_\lambda(V),
\qquad \det V=\Lambda^mV.
\tag{33}
\]

**Proof.** The tensor product in (32) is polynomial and homogeneous of the indicated degree, so Theorem 5.1 decomposes it into that degree's Schur modules. Its diagonal character is \(s_\alpha(x)s_\beta(x)\). The preceding lesson expands this product with coefficients \(c^\nu_{\alpha\beta}\); specialization kills precisely the shapes longer than \(m\). The remaining Schur polynomials are linearly independent in \(m\) variables. Indeed, their expansions into monomial symmetric polynomials are triangular with diagonal one by Lemma 2.2 of that lesson; the dominance inequalities remain valid among shapes of length at most \(m\). Thus comparison determines every multiplicity in (32).

The action on the line \(\Lambda^mV\) is \(g\mapsto\det g\), as the alternating expansion of the images of a basis shows. Twisting an irreducible by a one-dimensional character preserves irreducibility, since it preserves its invariant subspaces. Factoring \(x_i^r\) from row \(i\) of the numerator in the bialternant gives

\[
s_{\lambda+(r^m)}(x)=(x_1\cdots x_m)^r s_\lambda(x).
\tag{34}
\]

Theorem 5.1 and character independence identify the twist with the Schur module on the left of (33). \(\square\)

On restricting a Schur module of degree \(n\) to \(SL_m(\mathbb C)\), it remains irreducible. In fact, any \(g\in GL_m\) can be written \(g=th\) with \(h\in SL_m\), by choosing \(t^m=\det g\). The scalar matrix \(tI\) acts by \(t^n\). An \(SL_m\)-invariant subspace is therefore \(GL_m\)-invariant. Determinant shifts in (33) become isomorphic on \(SL_m\). In a single tensor degree the labels are still distinct: an intertwiner for \(SL_m\) also intertwines the common scalar action and hence \(GL_m\). This explains why deleting full columns is appropriate for the special linear group while retaining them matters for the general linear group.

The polynomial definition in this section means polynomials in the entries of the matrix itself. The evaluation-functional argument (28) and scalar-degree projections prove its classification directly. Representations whose entries also involve the inverse matrix belong to the broader rational class; the two definitions are not interchangeable.

## 6. Symmetric tensors, mixed tensors and the adjoint example

### Two factors

For the flip \(P\) on \(V\otimes V\), the operators

\[
p_+=\frac{I+P}{2},\qquad p_-=\frac{I-P}{2}
\tag{35}
\]

are idempotents with \(p_+p_-=0\) and \(p_++p_-=I\). They project onto \(\operatorname{Sym}^2V\) and \(\Lambda^2V\). Symmetrization identifies the symmetric quotient with the symmetric tensors: it respects the quotient relations and induces inverse maps between the quotient and the invariant subspace. Alternation similarly identifies the exterior square with the alternating tensors. Both maps commute with \(GL(V)\). Consequently

\[
V^{\otimes2}\cong
 (\operatorname{Sym}^2V\otimes\mathbf1)
 \oplus(\Lambda^2V\otimes\operatorname{sgn}).
\tag{36}
\]

The second summand is zero for \(m=1\); the first is nonzero. For \(m\geq2\), both are irreducible as general linear group modules by Theorem 3.1. Basis vectors indexed by \(i\leq j\) and by \(i<j\) give dimensions \(m(m+1)/2\) and \(m(m-1)/2\), whose sum is \(m^2\).

The same averaging argument for a single row or column proves

\[
S_{(n)}(V)=\operatorname{Sym}^nV,\qquad
S_{(1^n)}(V)=\Lambda^nV.
\tag{37}
\]

The alternating map sends a wedge to \(1/n!\) times its signed tensor sum; the increasing basis-index tensors show that it is injective and that its image is exactly the alternating subspace. The symmetric version uses weakly increasing basis indices. Their dimensions are \(\binom{m+n-1}{n}\) and \(\binom mn\), respectively, with \(\binom mn=0\) for \(n>m\). For the first count, weakly increasing indices \(i_1\leq\cdots\leq i_n\) correspond to strictly increasing \(i_1,i_2+1,\ldots,i_n+n-1\) chosen from \(\{1,\ldots,m+n-1\}\). For the second count, choose an \(n\)-element subset of the basis indices. In particular our convention assigns symmetric tensors to a row, not to a column.

### Three factors in dimension two

The three partitions of \(3\) are \((3),(2,1),(1,1,1)\). Their symmetric-group dimensions are \(1,2,1\); the middle dimension also counts its two standard tableaux. When \(\dim V=2\), the column of height three is excluded. Formula (25) gives

\[
\dim S_{(3)}(V)=4,\qquad \dim S_{(2,1)}(V)=2.
\tag{38}
\]

More precisely, (33) with \(m=2\), \(\lambda=(1,0)\) and \(r=1\) gives \(S_{(2,1)}(V)\cong\det V\otimes V\). Thus

\[
V^{\otimes3}\cong
 (\operatorname{Sym}^3V\otimes\mathbf1)
 \oplus((\det V\otimes V)\otimes V_{(2,1)}).
\tag{39}
\]

Its dimension is \(4+2\cdot2=8\). Forgetting the symmetric-group action gives two copies of \(\det V\otimes V\). Retaining that action gives the single tensor product with its two-dimensional multiplicity partner.

The row filling used in the nonvanishing proof is particularly concrete here:

\[
\begin{array}{cc}
\boxed{1}&\boxed{1}\\
\boxed{2}&
\end{array}
\qquad
c_t(v_1\otimes v_1\otimes v_2)
=2v_1\otimes v_1\otimes v_2
 -v_2\otimes v_1\otimes v_1
 -v_1\otimes v_2\otimes v_1.
\tag{40}
\]

*Figure 2. Basis labels placed in the boxes of shape \((2,1)\). The tableau's position labels are \(1,2\) in the first row and \(3\) below the first box, so \(c_t=(1+(12))(1-(13))\). The displayed tensor is its actual image, with coefficient \(2=2!1!\) on the original row filling, as in (17). The boxed numbers denote basis labels, not the position labels.*

Here \(\operatorname{End}_{GL(V)}(V^{\otimes3})\) has dimension \(1^2+2^2=5\), while \(\operatorname{End}_{S_3}(V^{\otimes3})\) has dimension \(4^2+2^2=20\), by (11). The six permutation operators span a five-dimensional algebra: their signed sum, the degree-three antisymmetrizer, is zero on a two-dimensional space.

### Three factors in dimension three

Let now \(V=\mathbb C^3\). Substituting \(\lambda=(2,1,0)\) into (25) gives

\[
\dim S_{(2,1)}(V)
 =\frac{2-1+1}{1}\,
   \frac{2-0+2}{2}\,
   \frac{1-0+1}{1}=8.
\tag{41}
\]

An explicit construction identifies the representation. Consider

\[
\omega:V\otimes\Lambda^2V\longrightarrow\Lambda^3V,
\qquad v\otimes(a\wedge b)\longmapsto v\wedge a\wedge b.
\tag{42}
\]

This map is equivariant and onto. It has the equivariant section

\[
a\wedge b\wedge c\longmapsto
\frac13\bigl(a\otimes(b\wedge c)+b\otimes(c\wedge a)+c\otimes(a\wedge b)\bigr).
\tag{43}
\]

The expression is trilinear and alternating in \(a,b,c\), so it is well-defined on \(\Lambda^3V\); applying \(\omega\) gives back the wedge. The product rule (32) says

\[
V\otimes\Lambda^2V\cong S_{(2,1)}(V)\oplus\Lambda^3V.
\tag{44}
\]

Indeed, multiplying \(s_{(1)}s_{(1,1)}\) adds one box to \((1,1)\): shapes \((2,1)\) and \((1,1,1)\) each have one allowed Littlewood–Richardson filling. Shape \((3)\) cannot contain \((1,1)\), so contributes zero. The character of \(\ker\omega\) is therefore \(s_{(2,1)}\). Polynomial complete reducibility and character independence identify \(\ker\omega\) with \(S_{(2,1)}(V)\).

There is a canonical isomorphism \(\Lambda^2V\cong\operatorname{Hom}(V,\det V)=V^*\otimes\det V\), sending \(a\wedge b\) to \([z\mapsto z\wedge a\wedge b]\). In a basis, the three elementary wedges map, up to their signs, to the three dual basis vectors times the volume form, so the map is bijective. Under the resulting identification

\[
V\otimes\Lambda^2V\cong\operatorname{End}(V)\otimes\det V,
\tag{45}
\]

the wedge map is trace times the identity on the determinant line. In fact, a rank-one operator \(z\mapsto\ell(z)v\) has trace \(\ell(v)\), which is exactly the coefficient of \(v\wedge a\wedge b\) in the chosen volume form. We obtain

\[
S_{(2,1)}(\mathbb C^3)\cong
\det V\otimes\mathfrak{sl}(V),
\qquad g\cdot(d\otimes X)=(\det g)d\otimes gXg^{-1},
\tag{46}
\]

where \(\mathfrak{sl}(V)=\{X:\operatorname{Tr}X=0\}\). On \(SL_3\), the determinant factor is trivial, and this is its adjoint representation, irreducible by the restriction argument after (34). On \(GL_3\), the factor is essential: \(tI\) acts by \(t^3\) on this Schur module, while conjugation alone acts by the identity.

## 7. Exercises and complete solutions

### Exercise 1 — A tensor cube with all three symmetries

For \(V=\mathbb C^3\), decompose \(V^{\otimes3}\) as a \(GL(V)\times S_3\)-module and as a \(GL(V)\)-module. Give the dimensions and the diagonal characters of the distinct general linear group summands. Check the trace when the permutation is a three-cycle.

**Solution.** All three shapes of size three have at most three rows. By (15),

\[
V^{\otimes3}\cong
 (\operatorname{Sym}^3V\otimes\mathbf1)
 \oplus(S_{(2,1)}(V)\otimes V_{(2,1)})
 \oplus(\det V\otimes\operatorname{sgn}).
\tag{47}
\]

Their general linear group dimensions are \(\binom53=10\), \(8\) from (41), and \(1\). Their symmetric-group dimensions are \(1,2,1\). Thus \(10+2\cdot8+1=27=3^3\). After forgetting \(S_3\), the middle representation occurs twice. Formula (46) identifies it explicitly with \(\det V\otimes\mathfrak{sl}(V)\).

The diagonal characters are \(h_3(x)=\sum_{i\leq j\leq k}x_ix_jx_k\), \(s_{(2,1)}(x)=h_2(x)h_1(x)-h_3(x)\) by Jacobi–Trudi, and \(e_3(x)=x_1x_2x_3\). At a three-cycle, the \(S_3\) characters of the three shapes are \(1,-1,1\), respectively; the middle value also follows by removing the whole \((2,1)\) border strip of height one. The mixed trace from (47) is consequently

\[
h_3-s_{(2,1)}+e_3=2h_3-h_1h_2+e_3
 =x_1^3+x_2^3+x_3^3=p_3.
\tag{48}
\]

To verify the last equality directly, a monomial \(x_i^3\) has coefficient \(2-1=1\); a monomial \(x_i^2x_j\), \(i\ne j\), has coefficient \(2-2=0\); and \(x_1x_2x_3\) has coefficient \(2-3+1=0\). These are all degree-three monomial types. This agrees with the single-cycle trace (19).

### Exercise 2 — Produce an invertible-power expression

Prove that every operator commuting with the factor permutations is a linear combination of \(g^{\otimes n}\) with \(g\) invertible, using explicit polarization and interpolation. For \(V=\mathbb C^2\), verify the construction on

\[
X=E_{11}\otimes E_{22}+E_{22}\otimes E_{11}
\tag{49}
\]

in degree two, where \(E_{ij}\) are matrix units.

**Solution.** Identify the operator space with \((\operatorname{End}V)^{\otimes n}\) by (6). Conjugation by a factor permutation permutes these operator factors. Average a tensor-product spanning set over these permutations. Every commuting operator is a linear combination of the resulting invariant tensors. In each average, expand the signed subset sum (2): terms using fewer than all \(n\) labels cancel by (3), and the surviving terms are precisely the permutation sum. Thus the operator is a linear combination of powers \(a^{\otimes n}\).

For each such \(a\), the bad shifts are the finitely many roots of the monic polynomial \(\det(a+tI)\). Select \(n+1\) distinct good shifts. Since \((a+tI)^{\otimes n}\) has degree at most \(n\) in \(t\), interpolation at zero gives exactly (4). This replaces every power by invertible powers and proves (5), including the reverse inclusion because equal operators on all factors commute with factor permutations.

For the concrete operator, write \(A=E_{11}\), \(B=E_{22}\). Polarization gives \(X=I^{\otimes2}-A^{\otimes2}-B^{\otimes2}\). Both singular powers can be interpolated at \(t=1,2,3\); the interpolation coefficients at zero are \(3,-3,1\). Hence the required expression is

\[
\begin{aligned}
X=I^{\otimes2}
 &-3(A+I)^{\otimes2}+3(A+2I)^{\otimes2}-(A+3I)^{\otimes2}\\
 &-3(B+I)^{\otimes2}+3(B+2I)^{\otimes2}-(B+3I)^{\otimes2}.
\end{aligned}
\tag{50}
\]

All seven matrices being powered are invertible. In the ordered basis \(v_1v_1,v_1v_2,v_2v_1,v_2v_2\) of tensors, \(X\) is \(\operatorname{diag}(0,1,1,0)\). For example, the three terms for \(A\) give \(3(4,2,2,1)-3(9,6,6,4)+(16,12,12,9)=(1,0,0,0)\); those for \(B\) give \((0,0,0,1)\). Subtracting both from \((1,1,1,1)\) verifies the displayed expression entry by entry.

### Exercise 3 — Evaluate a vanishing pair of determinants

Starting from the bialternant, prove the dimension formula (25) by specializing the variables along a geometric progression. Explain why direct substitution of all variables equal to one into the quotient is insufficient. Compute \(\dim S_{(3,1)}(\mathbb C^4)\).

**Solution.** Pad \(\lambda\) by zeros and set \(\beta_j=\lambda_j+m-j\), \(\delta_j=m-j\). With \(x_i=q^{m-i}\), the numerator determinant has column \(j\) equal to the descending powers of \(q^{\beta_j}\). The Vandermonde formula therefore gives \(\prod_{i<j}(q^{\beta_i}-q^{\beta_j})\). The denominator gives the analogous product with \(\delta\). The order and hence the signs are the same in both determinants, giving (26).

For each pair, factor \(q^a-q^b\) as in (27). Cancel the common factor \(q-1\) and evaluate the two remaining geometric sums at one. The factor becomes \((\beta_i-\beta_j)/(\delta_i-\delta_j)\). All differences in the denominator are positive, and \(\delta_i-\delta_j=j-i\), so the resulting product is (25). The character theorem identifies this evaluation with the dimension. Directly substituting into the two original determinants would give \(0/0\) for \(m>1\); cancellation as a polynomial identity is what justifies the evaluation.

For \(\lambda=(3,1,0,0)\), the six factors, in order \((1,2),(1,3),(1,4),(2,3),(2,4),(3,4)\), are

\[
3,\quad\frac52,\quad2,\quad2,\quad\frac32,\quad1.
\qquad \dim S_{(3,1)}(\mathbb C^4)=45.
\tag{51}
\]

### Exercise 4 — Recover the two algebras from their blocks

Prove the double-centralizer theorem for a finite-dimensional semisimple unital \(A\subseteq\operatorname{End}(E)\), using Lemmas 2.1 and 2.2 and matrix units. Apply it to

\[
E=(\mathbb C^2\otimes\mathbb C^3)\oplus\mathbb C^2,
\qquad
A=\{(a\otimes I_3)\oplus cI_2:a\in\operatorname{Mat}_2(\mathbb C),\ c\in\mathbb C\}.
\tag{52}
\]

Find \(A'\), \(A''\), the paired simple modules, and both algebra dimensions.

**Solution.** Decompose \(E\) into its simple \(A\)-types \(U_i\) using Lemma 2.1. An intertwiner \(U_i\to E\) has scalar coordinates in its copies of \(U_i\) and zero coordinates in other types. Therefore \(W_i=\operatorname{Hom}_A(U_i,E)\) has dimension the multiplicity, and evaluation \(\bigoplus_iU_i\otimes W_i\to E\) is bijective. Lemma 2.2 prescribes arbitrary operators on the distinct \(U_i\) independently. Faithfulness of the inclusion \(A\subseteq\operatorname{End}(E)\) then identifies \(A\) with \(\bigoplus_i\operatorname{End}(U_i)\otimes I\).

Commuting with its block identities first forces preservation of every block. Within each block, Schur's scalar-endomorphism assertion says that the entries between copies of \(U_i\) are arbitrary scalars. Thus \(A'=\bigoplus_i I\otimes\operatorname{End}(W_i)\). To see semisimplicity without assuming an algebra classification, for a module \(M\) over a matrix block use \(v_a\otimes h\mapsto e_{a1}h\) from \(\mathbb C^d\otimes e_{11}M\), with inverse \(z\mapsto\sum_a v_a\otimes e_{1a}z\). This exhibits every module as a sum of defining simples; the central identities split different blocks. The defining modules \(W_i\) are simple and distinguished by those identities.

Finally, commuting with these identities also makes an element of \(A''\) block diagonal. In a block, its entries on \(W_i\) commute with all matrix units. Diagonal units force them to be diagonal and off-diagonal units force equal diagonal entries. They are scalars, leaving exactly \(\operatorname{End}(U_i)\otimes I\). This proves \(A''=A\) and all assertions of the general theorem.

In the example, the first simple \(A\)-module is the defining \(\mathbb C^2\) for the matrix block, with multiplicity space \(\mathbb C^3\). The second is the scalar module \(\mathbb C\), with multiplicity space \(\mathbb C^2\). They are different \(A\)-types, even though the ambient last summand has dimension two. The answer is

\[
A'=\{(I_2\otimes b)\oplus d:
 b\in\operatorname{Mat}_3(\mathbb C),\ d\in\operatorname{Mat}_2(\mathbb C)\},
\qquad A''=A.
\tag{53}
\]

The paired dimensions \((\dim U_i,\dim W_i)\) are \((2,3)\) and \((1,2)\). Hence \(\dim E=2\cdot3+1\cdot2=8\), \(\dim A=2^2+1^2=5\), and \(\dim A'=3^2+2^2=13\). Formula (13) displays the first block of this very example.

## References

- **[Etingof et al.]** P. Etingof, O. Golberg, S. Hensel, T. Liu, A. Schwendner, D. Vaintrob and E. Yudovina, *Introduction to representation theory*, [lecture notes](https://arxiv.org/pdf/0901.0827), §§4.18–4.22, especially Theorem 4.54, Proposition 4.58, Corollary 4.59 and Theorem 4.63. A comparison of the finite algebra, interpolation and character arguments; the notation for polynomial representations is broader there.
- **[Gruson–Serganova]** C. Gruson and V. Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Springer, 2018, Chapter 5, §2, and Chapter 6, §2. Semisimple modules, density, dual pairs and Schur functors.

# The symmetric groups II: branching, Jucys–Murphy elements and Young's seminormal form

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Independent AI review is not yet recorded. Public domain (CC0).*

Deleting the largest entry of a standard tableau leaves a smaller standard tableau. The branching rule says that this elementary operation describes restriction of irreducible symmetric-group representations. We will prove the connection by constructing the representation matrices, rather than assuming a standard-tableau basis.

The prerequisite is [lesson 13](RT-FIN-13.md): its classification of the irreducibles \(V_\lambda\), its tableau separation lemma, and its fixed left-ideal convention \(V_\lambda=\mathbb C[S_n]a_tb_t\). We also use the faithful Fourier decomposition of the group algebra from [lesson 3](RT-FIN-03.md). All permutation products act from right to left.

Our route uses Coxeter generators and Jucys–Murphy elements, as in the approach of Vershik–Okounkov [VO, §§5–6]. We first construct orthogonal matrices and verify every relation. A change of basis then gives a specified rational seminormal form. The hook formula will follow from the branching recursion and an elementary partial-fraction identity; no character formula or symmetric-function theorem is imported.

## 1. Boxes, contents and adjacent swaps

Write a box of a partition diagram as \(b=(i,j)\), with row index increasing downwards and column index increasing to the right. Its **content** is

\[
c(b)=j-i.
\tag{1}
\]

For a standard tableau \(T\), let \(c_T(k)\) be the content of the box containing \(k\). Its boxes carrying \(1,\ldots,k\) form a partition diagram, denoted \(\lambda^{(k)}(T)\). Indeed, every box above or to the left of one of these boxes has a smaller entry. Thus a tableau is equivalent to a path

\[
\varnothing=\lambda^{(0)}
\subset\lambda^{(1)}\subset\cdots\subset\lambda^{(n)}=\lambda
\tag{2}
\]

which adds one box at each step. Conversely, putting \(k\) in the box added at step \(k\) gives a standard tableau.

An **addable box** can be adjoined while keeping a partition diagram; a **removable box** can be deleted while keeping one. The latter are the bottom-right corners of the diagram. Addable boxes in different rows have different contents. In rows \(i<j\) their contents are \(\mu_i+1-i\) and \(\mu_j+1-j\), with a zero part allowed for a new bottom row; the first is strictly larger.

**Lemma 1.1 (content and swap facts).** The following statements hold.

1. The full sequence \((c_T(1),\ldots,c_T(n))\) determines \(T\), even when the shape is not specified.
2. For \(s_k=(k,k+1)\), the relabeled tableau \(s_kT\) is standard exactly when \(k,k+1\) lie in different rows and different columns. In that case
   \[
   |r_T(k)|\geq2,\qquad r_T(k)=c_T(k+1)-c_T(k).
   \tag{3}
   \]
   In the same row \(r_T(k)=1\); in the same column \(r_T(k)=-1\).
3. The three contents belonging to \(k,k+1,k+2\) are pairwise distinct.
4. Any two standard tableaux of a fixed shape are connected by swaps \(T\mapsto s_kT\) which remain standard.

**Proof.** Starting with the empty diagram, the next content selects a unique addable box, by the preceding observation. This proves statement 1 inductively.

Order boxes by \((i,j)\leq(i',j')\) when both coordinate inequalities hold. A standard tableau lists this finite partially ordered set in an order respecting all its comparisons: a linear extension. Row and column increase imply all these comparisons, by a path inside the diagram.

Two consecutive entries in comparable boxes must lie in adjacent boxes of the same row or the same column. Otherwise there is a box strictly between them in the partial order, whose entry would be strictly between the two consecutive integers. Adjacent row boxes have content difference \(1\), and adjacent column boxes have difference \(-1\). Swapping comparable consecutive entries violates their comparison. Swapping incomparable consecutive entries preserves every comparison, since all other entries are either smaller than both or larger than both. If incomparable boxes are \((i,j)\), \((i',j')\) with \(i<i'\), then \(j>j'\); their contents differ in absolute value by \((i'-i)+(j-j')\geq2\). This proves statement 2.

Equal-content distinct boxes lie on the same diagonal. Say they are \((i,j)\) and \((i+d,j+d)\), \(d\geq1\). The boxes \((i,j+1)\) and \((i+1,j)\) both belong to the diagram and both have entries strictly between the entries of the two diagonal boxes. These are two distinct intervening entries. Consequently equal contents cannot occur at entry distance \(1\) or \(2\), proving statement 3.

For statement 4, compare two linear extensions. After their initial entries have been made equal, take the next box of the target extension and move it leftwards in the other extension. Every box it passes is incomparable with it: a predecessor would have to come first in the target as well, and a successor could not precede it in the current extension. Each move is an allowed adjacent swap. Repeat on the remaining boxes. The procedure terminates because each step increases the common initial segment. \(\square\)

For example, a tableau of shape \((3,2)\), together with its contents, is

\[
T=
\begin{array}{ccc}
\boxed{1}&\boxed{2}&\boxed{5}\\
\boxed{3}&\boxed{4}&
\end{array},
\qquad
\begin{array}{ccc}
\boxed{0}&\boxed{1}&\boxed{2}\\
\boxed{-1}&\boxed{0}&
\end{array}.
\tag{4}
\]

The corresponding content sequence is \((0,1,-1,0,2)\). The repeated \(0\) does not cause ambiguity: the diagram present at each step determines where its next addable box can be.

## 2. Constructing the orthogonal matrices

Let \(W_\lambda\) have basis \(u_T\), one vector for every standard tableau of shape \(\lambda\), and declare these vectors orthonormal. Define

\[
S_k u_T=
\begin{cases}
 r^{-1}u_T+\sqrt{1-r^{-2}}\,u_{s_kT},
       &s_kT\text{ standard},\\
 r^{-1}u_T,&s_kT\text{ not standard},
\end{cases}
\qquad r=r_T(k).
\tag{5}
\]

The square root in (5) is the nonnegative real root. The second case is \(+u_T\) in a row and \(-u_T\) in a column. We must prove that these operators give a representation of \(S_n\).

For completeness, the required presentation of \(S_n\) is also elementary.

**Lemma 2.1 (Coxeter presentation).** The adjacent transpositions generate \(S_n\), and their complete defining relations are

\[
s_k^2=1,\qquad s_ks_l=s_ls_k\ (|k-l|>1),
\qquad s_ks_{k+1}s_k=s_{k+1}s_ks_{k+1}.
\tag{6}
\]

**Proof.** Adjacent swaps sort any list of distinct integers, so they generate every permutation. They satisfy (6) as permutations. Let \(G_n\) be the abstract group defined by (6), and let \(H\) be the subgroup generated by \(s_1,\ldots,s_{n-2}\). Inductively \(|H|\leq(n-1)!\); it is a quotient of \(G_{n-1}\).

Put \(d_n=1\), and \(d_j=s_{n-1}s_{n-2}\cdots s_j\) for \(1\leq j<n\). Every element of \(G_n\) belongs to one of the sets \(Hd_j\). To see this, their union contains \(1\) and is stable under right multiplication by each generator. For \(j<n\), the relations give

\[
d_js_i=
\begin{cases}
s_i d_j,&i<j-1,\\
d_{j-1},&i=j-1,\\
d_{j+1},&i=j,\\
s_{i-1}d_j,&i>j.
\end{cases}
\tag{7}
\]

The last identity follows by commuting \(s_i\) left until it meets \(s_{i-1}\), using the braid relation, and commuting the resulting \(s_{i-1}\) past the factors with larger indices. Every factor on the left of \(d_j\) in (7) lies in \(H\). For \(d_n\), right multiplication by \(s_i\) stays in \(H\) if \(i<n-1\), and gives \(d_{n-1}\) otherwise. Thus \(|G_n|\leq n|H|\leq n!\). The surjection \(G_n\to S_n\) reaches \(n!\) permutations, and hence is an isomorphism. The base \(n=1\) is trivial. \(\square\)

**Theorem 2.2 (orthogonal construction).** The operators (5) satisfy (6). They therefore define a real orthogonal representation \(W_\lambda\) of \(S_n\).

**Proof.** On a standard pair \(T,T'=s_kT\), their matrix is

\[
\begin{pmatrix}
 a&b\\ b&-a
\end{pmatrix},
\qquad a=\frac1r,\quad b=\sqrt{1-\frac1{r^2}}.
\tag{8}
\]

It is symmetric and squares to the identity. On an unpaired tableau the operator is \(1\) or \(-1\). This proves \(S_k^2=I\) and orthogonality.

For \(|k-l|>1\), the two swaps involve disjoint pairs of entries. Each leaves the other's contents and standardness condition unchanged. Expanding both products on \(u_T\) therefore gives the same coefficients for the unchanged tableau, either singly swapped tableau and the doubly swapped tableau. This proves commutation.

Here is the full braid calculation, including boundary cases. Freeze all entries except \(k,k+1,k+2\), and write the contents of their three boxes as \(x,y,z\), in this order. By Lemma 1.1 they are distinct integers. Put

\[
r=y-x,\quad t=z-y,\quad q=z-x=r+t,
\qquad a=\frac1r,\quad d=\frac1t,\quad h=\frac1q,
\tag{9}
\]

and \(b_r=\sqrt{1-r^{-2}}\), \(b_t=\sqrt{1-t^{-2}}\), \(b_q=\sqrt{1-q^{-2}}\). All three radicals are real because the differences are nonzero integers.

Temporarily allow all six orders of these three boxes. Denote their formal basis vectors by their content orders \(xyz,yxz,xzy,zxy,yzx,zyx\). Define the two adjacent-swap operators on this six-dimensional space by the same diagonal coefficient and square-root coefficient as (5), using a zero square-root coefficient when the difference is \(1\) or \(-1\). Expansion gives the following coefficients on the vector \(xyz\).

| Resulting order | \(S_kS_{k+1}S_k\) | \(S_{k+1}S_kS_{k+1}\) |
| --- | --- | --- |
| \(xyz\) | \(a^2d+(1-a^2)h\) | \(d^2a+(1-d^2)h\) |
| \(yxz\) | \(a b_r(d-h)\) | \(d b_r h\) |
| \(xzy\) | \(a b_t h\) | \(d b_t(a-h)\) |
| \(zxy\) | \(a b_t b_q\) | \(a b_t b_q\) |
| \(yzx\) | \(d b_r b_q\) | \(d b_r b_q\) |
| \(zyx\) | \(b_r b_t b_q\) | \(b_r b_t b_q\) |

The middle two equalities follow from

\[
a(d-h)=dh,\qquad d(a-h)=ah.
\tag{10}
\]

For the first row, subtract \(h\) on both sides and use
\(a^2(d-h)=d^2(a-h)=1/(rtq)\). All the identities use only \(q=r+t\). The last three rows already coincide. Replacing \(xyz\) by any other order gives the same calculation with its contents renamed, so the operators satisfy the braid relation on the entire six-dimensional space.

The span of its standard orders is invariant: a swap taking a standard order to a nonstandard one has content difference \(1\) or \(-1\), by Lemma 1.1, so its square-root coefficient is zero. Entries outside the three selected labels do not change their comparisons. Restricting the six-dimensional identity proves the braid relation on \(W_\lambda\), even if only some of the six orders are standard. Lemma 2.1 now supplies the group action. \(\square\)

The vanished coefficients at \(r=\pm1\) are essential to the boundary argument. We have not treated a nonstandard tableau as an additional basis vector of \(W_\lambda\).

## 3. Jucys–Murphy operators and irreducibility

In \(A_n=\mathbb C[S_n]\), define

\[
X_1=0,\qquad X_k=\sum_{i<k}(i\,k).
\tag{11}
\]

Write \(Z_k=\sum_{1\leq i<j\leq k}(i\,j)\), with \(Z_0=Z_1=0\). The element \(Z_k\) is central in \(A_k\), since conjugation permutes its transpositions. Thus

\[
X_k=Z_k-Z_{k-1}.
\tag{12}
\]

**Proposition 3.1 (commutation and content eigenvalues).** The \(X_k\) commute in \(A_n\), and on the constructed model,

\[
X_k u_T=c_T(k)u_T.
\tag{13}
\]

**Proof.** If \(j\leq k\), the central element \(Z_k\) commutes with \(Z_j\in A_k\). Hence all the \(Z_k\), and therefore their differences, commute. This is a group-algebra proof; it does not depend on the constructed models.

The transpositions also give

\[
X_{k+1}=s_kX_ks_k+s_k.
\tag{14}
\]

Conjugation by \(s_k\) changes \((i\,k)\), \(i<k\), into \((i\,k+1)\), and the extra summand is \((k\,k+1)\).

We prove (13) by induction on \(k\). For \(k=1\), both sides are zero. Suppose it holds for \(k\), and take a standard pair \(T,T'=s_kT\). Set \(x=c_T(k)\), \(y=c_T(k+1)\), \(r=y-x\). On this pair \(X_k=\operatorname{diag}(x,y)\), and (8) gives

\[
\begin{pmatrix}a&b\\b&-a\end{pmatrix}
\begin{pmatrix}x&0\\0&y\end{pmatrix}
\begin{pmatrix}a&b\\b&-a\end{pmatrix}
+\begin{pmatrix}a&b\\b&-a\end{pmatrix}
=\begin{pmatrix}y&0\\0&x\end{pmatrix}.
\tag{15}
\]

Indeed, the off-diagonal entry is \(b(a(x-y)+1)=0\). The upper diagonal entry is \(y+a^2(x-y)+a=y\), and the lower is \(x+a^2(y-x)-a=x\). If the swap is nonstandard, \(r=\pm1\), and (14) acts on \(u_T\) as \(x+1/r=x+r=y\). This proves the induction. \(\square\)

**Theorem 3.2 (irreducible models).** The \(W_\lambda\) are irreducible and are pairwise nonisomorphic for different shapes.

**Proof.** Their joint eigenvectors for the \(X_k\) have distinct eigenvalue sequences, by Lemma 1.1. One can extract any selected vector from a linear combination by a polynomial in these operators. More explicitly, for a fixed tableau \(T\), and each different tableau \(U\) in the same shape, choose an index \(k(U)\) at which the contents differ. The operator

\[
\prod_{U\neq T}
\frac{X_{k(U)}-c_U(k(U))I}
     {c_T(k(U))-c_U(k(U))}
\tag{16}
\]

is \(1\) on \(u_T\) and zero on every other basis vector.

A nonzero invariant subspace is stable under (16), so contains some \(u_T\). If \(T'=s_kT\) is standard, (5) and its nonzero square-root coefficient imply that the subspace also contains \(u_{T'}\). Connectivity from Lemma 1.1 gives every basis vector, proving irreducibility.

An intertwining map between two models must commute with every \(X_k\). It therefore preserves joint eigenvalue sequences. Different shapes have disjoint sets of such sequences, again by Lemma 1.1. Such a map is zero, proving nonisomorphism. \(\square\)

## 4. Identifying the labels and proving branching

We must still check that \(W_\lambda\) is the already defined \(V_\lambda\), rather than another irreducible with a permuted partition label.

**Lemma 4.1 (agreement with Young symmetrizers).** There is an \(S_n\)-isomorphism \(W_\lambda\simeq V_\lambda\).

**Proof.** Theorem 3.2 gives one pairwise distinct irreducible for each partition of \(n\). Lesson 13, Theorem 4.3, gives exactly this many irreducibles. Thus
\(W_\lambda\simeq V_{\phi(\lambda)}\) for a permutation \(\phi\) of the partitions.

Let \(t\) be the tableau obtained by filling the rows of \(\lambda\) successively. All its labels in each row form an interval. Adjacent transpositions within that interval act as \(+1\) on \(u_t\) by (5); they generate the row group \(R_t\). Consequently

\[
a_tu_t=|R_t|u_t\neq0.
\tag{17}
\]

Let \(\mu=\phi(\lambda)\), and choose a tableau \(v\) of shape \(\mu\). If \(\lambda\) is not dominated by \(\mu\), lesson 13, Lemma 2.2, gives
\(a_t x b_v=0\) for every \(x\in A_n\). In particular
\(a_t x a_v b_v=0\), so \(a_t\) acts as zero on \(A_na_vb_v=V_\mu\), contradicting (17). We obtain \(\lambda\preceq\phi(\lambda)\) in the dominance order.

Following any cycle of the finite permutation \(\phi\) gives
\(\lambda\preceq\phi(\lambda)\preceq\cdots\preceq\lambda\). Antisymmetry of dominance forces equality at every step. Hence \(\phi\) is the identity. \(\square\)

**Theorem 4.2 (branching rule).** For the subgroup \(S_{n-1}\) fixing \(n\),

\[
\operatorname{Res}^{S_n}_{S_{n-1}}V_\lambda
\simeq
\bigoplus_{\substack{\mu\subset\lambda\\|\lambda/\mu|=1}}V_\mu.
\tag{18}
\]

Each summand occurs once.

**Proof.** In a standard tableau the box containing \(n\) must be removable. Group the basis of \(W_\lambda\) according to that box. The operators \(S_1,\ldots,S_{n-2}\) never move \(n\), so each of these spans is invariant under \(S_{n-1}\). Deleting the box of \(n\) identifies its basis bijectively with the standard tableaux of the resulting shape \(\mu\). The contents and all coefficients (5) for the remaining entries are unchanged. The span is therefore isomorphic to \(W_\mu\).

These spans form a direct sum because they partition a basis. Different removable boxes give different partitions: they are row ends with a strict drop to the next row, so deleting different ends changes different parts. Lemma 4.1 identifies the models with \(V_\lambda,V_\mu\). This proves (18) and multiplicity one. The case \(n=1\) uses the empty diagram and the one-dimensional representation of \(S_0=\{1\}\). \(\square\)

**Corollary 4.3 (Gelfand–Tsetlin lines and dimension).** Iterated restriction along \(S_1\subset\cdots\subset S_n\) decomposes \(V_\lambda\) into canonical one-dimensional lines indexed by standard tableaux \(T\). Choosing a nonzero vector on each line gives an adapted basis, unique up to a separate scalar on each line. In particular

\[
\dim V_\lambda=f^\lambda
=\#\{\text{standard tableaux of shape }\lambda\},
\qquad
f^\lambda=\sum_{\mu\nearrow\lambda}f^\mu,
\quad f^\varnothing=1.
\tag{19}
\]

**Proof.** At each restriction, the irreducible summands are nonisomorphic and occur with multiplicity one. Each summand is its isotypic component, so it is intrinsic, not dependent on a choice of decomposition. Iterating yields a nested sequence of intrinsic components, terminating in a one-dimensional \(S_1\)-module. The possible sequences are exactly paths (2), hence tableaux. In the model just constructed the resulting line is \(\mathbb C u_T\), because fixing successive shapes fixes each added box. Counting the lines proves the dimension statement; grouping by the last box proves the recursion. \(\square\)

The word “canonical” describes the lines. It does not select nonzero vectors on them or make arbitrary independent rescalings disappear.

## 5. The Gelfand–Tsetlin algebra and a rational seminormal form

Let \(\mathcal G_n\) be the unital subalgebra of \(A_n\) generated by the centers \(Z(A_k)\), \(1\leq k\leq n\), under the usual inclusions \(A_k\subset A_n\). Its generators commute: a central element of \(A_k\) commutes with all of \(A_j\) when \(j\leq k\).

**Theorem 5.1 (the complete diagonal algebra).** One has

\[
\mathcal G_n=\mathbb C[X_1,\ldots,X_n].
\tag{20}
\]

Under the Fourier decomposition
\(A_n\simeq\bigoplus_{\lambda\vdash n}\operatorname{End}(V_\lambda)\),
this is exactly the algebra of all diagonal matrices in the tableau bases. It is maximal commutative: its commutant in \(A_n\) equals itself.

**Proof.** Equation (12) puts every \(X_k\) in \(\mathcal G_n\). Conversely, a central element of \(A_k\) acts as a scalar on each irreducible component of \(V_\lambda|_{S_k}\), by Schur's lemma. Every tableau line belongs to such a component with shape \(\lambda^{(k)}(T)\). Thus all of \(\mathcal G_n\) acts diagonally.

All tableau content sequences are distinct across all shapes. Also \(|c_T(k)|\leq k-1\), since the box belongs to a \(k\)-box diagram. Hence the polynomial

\[
P_T=
\prod_{k=1}^n
\ \prod_{\substack{-(k-1)\leq d\leq k-1\\d\neq c_T(k)}}
\frac{X_k-d}{c_T(k)-d}
\tag{21}
\]

acts as \(1\) on the line \(u_T\), and as zero on every other tableau line in every irreducible. The inner indexed product for \(k=1\) is empty. Extra integer roots which do not occur in the spectrum cause no problem: all denominators in (21) are nonzero.

The faithful Fourier isomorphism from lesson 3 now shows that the \(P_T\) are exactly the individual diagonal matrix units. Their linear span is the full diagonal algebra, and lies in \(\mathbb C[X_1,\ldots,X_n]\). Together with the two inclusions above, this proves (20).

In one matrix block, a matrix commuting with all diagonal matrix units has every off-diagonal entry zero. Applying this to each Fourier block shows that the commutant of this diagonal algebra is itself. This proves maximal commutativity in the entire group algebra. \(\square\)

In particular the \(P_T\) are pairwise orthogonal idempotents and sum to \(1\). Here “orthogonal” includes the algebraic relation \(P_TP_U=0\) for \(T\neq U\); in the orthonormal models they are orthogonal projections as well. They are primitive idempotents of \(A_n\), since each has rank one in one full matrix block. They generally differ from the normalized Young symmetrizers of lesson 13.

A smaller projector formula follows from the path itself. The content spectrum proved in Theorem 5.1 will verify it in every Fourier block. If \(U\) has \(k\) boxes and shape \(\mu\), and \(T\) extends it by a box of content \(c\), then, in \(A_{k+1}\),

\[
P_T=P_U
\prod_{\substack{b\text{ addable to }\mu\\c(b)\neq c}}
\frac{X_{k+1}-c(b)}{c-c(b)}.
\tag{22}
\]

**Proof of (22).** Under restriction, the included element \(P_U\) selects exactly the tableau lines whose first \(k\) boxes are \(U\). The possible next contents are the distinct contents of the addable boxes of \(\mu\). The second factor in (22) is the Lagrange interpolation polynomial which selects the desired one and kills the others. Its action therefore agrees with \(P_T\) on every irreducible, and Fourier faithfulness proves equality in \(A_{k+1}\). This also proves directly that the included \(P_U\) is the sum of all its extension projectors. \(\square\)

We now choose a different normalization of the same tableau lines. Put the boxes in row-reading order: first the first row, then the second, and so on. For an incomparable pair \(p,q\) with \(p\) earlier in that order, set
\(\delta_{pq}=c(q)-c(p)\). Such a pair has \(p\) above and to the right of \(q\), so \(\delta_{pq}\leq-2\). Define positive scalars

\[
\alpha_T^2=
\prod_{\substack{p\text{ earlier than }q\text{ in row order}\\
                 T(p)>T(q)}}
\frac{\delta_{pq}-1}{\delta_{pq}+1},
\qquad v_T=\alpha_Tu_T,
\tag{23}
\]

where every inverted pair is automatically incomparable. Take the positive square root for \(\alpha_T\). The row-filled tableau has \(\alpha_T=1\).

**Theorem 5.2 (our seminormal form).** In the basis (23), with \(r=c_T(k+1)-c_T(k)\), the action is

\[
s_kv_T=
\begin{cases}
\displaystyle\frac1r v_T+
 \left(1+\frac1r\right)v_{s_kT},&s_kT\text{ standard},\\[4pt]
v_T,&k,k+1\text{ in the same row},\\
-v_T,&k,k+1\text{ in the same column}.
\end{cases}
\tag{24}
\]

Thus all the matrices in this seminormal basis have rational entries. The contents (13) and the Gelfand–Tsetlin lines are unchanged.

**Proof.** An allowed swap of consecutive entries changes the inversion status only of their two boxes. Every other entry is smaller than both or larger than both. If the swap introduces their inversion, (23) adds its factor; if it removes the inversion, it removes that factor. In both cases

\[
\frac{\alpha_{s_kT}^2}{\alpha_T^2}
=\frac{r-1}{r+1}.
\tag{25}
\]

This number is positive for \(|r|\geq2\). Scaling (5) gives off-diagonal coefficient

\[
\frac{\alpha_T}{\alpha_{s_kT}}\sqrt{1-r^{-2}}
=\sqrt{\frac{r+1}{r-1}\frac{r^2-1}{r^2}}
=\frac{|r+1|}{|r|}
=1+\frac1r.
\tag{26}
\]

The last equality holds for \(r\geq2\) and \(r\leq-2\), separately. The diagonal coefficient remains \(1/r\). In the unpaired cases the scalar remains \(1\) or \(-1\). This proves (24); it is a change of basis in the representation already fully verified in Theorem 2.2. All \(r\) are integers, so its entries are rational. Diagonal operators still act by the same eigenvalues after rescaling. \(\square\)

On a pair \(T,T'=s_kT\), formula (24) has matrix

\[
\begin{pmatrix}
 r^{-1}&1-r^{-1}\\
 1+r^{-1}&-r^{-1}
\end{pmatrix}.
\tag{27}
\]

The columns record images of \(v_T,v_{T'}\). This matrix is generally not orthogonal for the coordinate Euclidean form, because these vectors have different lengths. Formula (8) is the orthogonal form. Other seminormal normalizations, such as [VO, (6.3)–(6.4)], put \(1\) in one off-diagonal position and \(1-r^{-2}\) in the other; they describe the same representation after another diagonal change of basis.

## 6. Hooks and the dimension formula

For \(b=(i,j)\in\lambda\), its **hook** consists of \(b\), the boxes to its right in the same row, and the boxes below it in the same column. Its length is

\[
h_\lambda(i,j)=\lambda_i-j+\lambda'_j-i+1.
\tag{28}
\]

Write \(H_\lambda=\prod_{b\in\lambda}h_\lambda(b)\). The empty product is \(1\).

**Lemma 6.1 (row products).** Pad \(\lambda\) with zeros to any fixed length \(l\geq\ell(\lambda)\), and set
\(\beta_i=\lambda_i+l-i\). Then \(\beta_1>\cdots>\beta_l\geq0\), and

\[
H_\lambda=
\frac{\prod_{i=1}^l\beta_i!}
     {\prod_{i<j}(\beta_i-\beta_j)}.
\tag{29}
\]

**Proof.** Fix row \(i\). Its hook lengths are distinct integers in \(1,\ldots,\beta_i\). We claim that the integers missing from that interval are exactly
\(\beta_i-\beta_j\), \(j>i\).

To prove the claim, let \(a\) of the lower rows have length greater than a positive integer \(c\), and let the next \(q\) lower rows have length exactly \(c\). The hook in column \(c\) of row \(i\) is
\(\lambda_i-c+1+a+q\), while the next hook, if present, is \(\lambda_i-c+a\). The omitted integers between them are

\[
\lambda_i-c+a+1,\ldots,\lambda_i-c+a+q.
\tag{30}
\]

For these \(q\) rows the indices are \(j=i+a+1,\ldots,i+a+q\), so
\(\beta_i-\beta_j=\lambda_i-c+(j-i)\), precisely (30). If \(c=\lambda_i\), the same calculation describes the integers below the last hook, with the next hook taken as zero. Lower zero rows supply the omitted integers above the first actual hook: they are \(\lambda_i+(j-i)\). These observations cover all gaps, since the hook decreases by one plus the number of lower rows ending at each successive column. They also cover an empty row: then all lower parts are zero, and the excluded integers are \(1,\ldots,l-i=\beta_i\), leaving no hooks.

Consequently the product of row \(i\)'s hooks is
\(\beta_i!/\prod_{j>i}(\beta_i-\beta_j)\). Multiplying over rows proves (29). This proves the hook product identity directly with ordinary integers. \(\square\)

**Lemma 6.2 (the recursion identity).** For distinct numbers \(\beta_1,\ldots,\beta_l\),

\[
\sum_{i=1}^l\beta_i
\prod_{j\neq i}\frac{\beta_i-\beta_j-1}{\beta_i-\beta_j}
=\sum_{i=1}^l\beta_i-\frac{l(l-1)}2.
\tag{31}
\]

**Proof.** Put
\(p_i=\prod_{j\neq i}(\beta_i-\beta_j-1)/(\beta_i-\beta_j)\).
The rational function

\[
R(z)=\prod_{j=1}^l\frac{z-\beta_j-1}{z-\beta_j}
\tag{32}
\]

has coefficient \(-p_i\) at its possible simple pole \(z=\beta_i\). Subtracting \(1-\sum_i p_i/(z-\beta_i)\) removes all its poles and gives a rational function tending to zero at infinity, hence the zero function. Equivalently, after multiplying by \(\prod_j(z-\beta_j)\), the difference is a polynomial of degree less than \(l\) vanishing at all \(l\) distinct \(\beta_i\).

Expand at infinity. The product of factors \(1-1/(z-\beta_j)\) has coefficient
\(\binom l2-\sum_j\beta_j\) at \(z^{-2}\): the single-factor contributions are \(-\beta_j\), and each pair contributes \(1\). The partial-fraction expression has coefficient \(-\sum_i\beta_i p_i\). Equating these coefficients proves (31). The argument is algebraic and applies when some \(p_i=0\). \(\square\)

**Theorem 6.3 (hook length formula).** For every partition of \(n\),

\[
\boxed{\displaystyle f^\lambda=\dim V_\lambda
=\frac{n!}{\prod_{b\in\lambda}h_\lambda(b)}}.
\tag{33}
\]

**Proof.** Set \(F(\lambda)=n!/H_\lambda\). It is \(1\) at the empty diagram. We show that it satisfies the recursion (19), which then determines it by induction on \(n\).

Keep a fixed padding length \(l\). If deleting the end of row \(i\) gives a partition \(\mu\), its \(\beta\)-vector replaces \(\beta_i\) by \(\beta_i-1\). Formula (29) therefore gives

\[
\frac{F(\mu)}{F(\lambda)}
=\frac{\beta_i}{n}
\prod_{j\neq i}\frac{\beta_i-\beta_j-1}{\beta_i-\beta_j}.
\tag{34}
\]

We may sum the right-hand side over all rows, including nonremovable ones. If \(\lambda_i=\lambda_{i+1}\), then \(\beta_i-\beta_{i+1}=1\) and the product is zero. Among zero padded rows, all but the last have this same zero factor, and the last has \(\beta_l=0\). Thus precisely the genuine removable rows can contribute. Since
\(\sum_i\beta_i=n+l(l-1)/2\), Lemma 6.2 says that the sum of (34) is \(1\). Hence
\(F(\lambda)=\sum_{\mu\nearrow\lambda}F(\mu)\).

This is the same recursion and initial value as \(f^\lambda\), so induction proves (33), using Corollary 4.3 for its representation-theoretic interpretation. \(\square\)

The hook product identity and branching recursion above give the dimension formula within this course.

## 7. Worked models and dimensions

For shape \((2,1)\), order the basis by

\[
A=\begin{array}{cc}\boxed{1}&\boxed{2}\\\boxed{3}&\end{array},
\qquad
B=\begin{array}{cc}\boxed{1}&\boxed{3}\\\boxed{2}&\end{array}.
\tag{35}
\]

Their content sequences are \((0,1,-1)\) and \((0,-1,1)\). In the seminormal normalization (23),

\[
\rho(s_1)=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\rho(s_2)=
\begin{pmatrix}-\tfrac12&\tfrac32\\
                 \tfrac12&\tfrac12\end{pmatrix}.
\tag{36}
\]

For \(A\), the axial distance at \(k=2\) is \(-2\); for \(B\) it is \(2\). Here \(\alpha_A=1,\alpha_B=\sqrt3\). In the orthonormal basis, the off-diagonal entries of the second matrix would both be \(\sqrt3/2\). Restricting to \(S_2\) gives the trivial line \(v_A\) and the sign line \(v_B\), in accordance with the two removable boxes.

For shape \((2,2)\), take tableaux with rows \(1,2\,/\,3,4\) and \(1,3\,/\,2,4\), in that order. Their content sequences are respectively
\((0,1,-1,0)\) and \((0,-1,1,0)\). The matrices are

\[
\rho(s_1)=\rho(s_3)=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\rho(s_2)=
\begin{pmatrix}-\tfrac12&\tfrac32\\
                 \tfrac12&\tfrac12\end{pmatrix}.
\tag{37}
\]

The only removable box of \((2,2)\) is \((2,2)\); deletion leaves \((2,1)\). Thus its restriction to \(S_3\) is irreducible. The fourth Jucys–Murphy operator is zero on both basis lines, because the box containing \(4\) has content zero.

For \(\lambda=(3,2)\), the content array is the right-hand array in (4). Its hook lengths are

\[
\begin{array}{ccc}
\boxed{4}&\boxed{3}&\boxed{1}\\
\boxed{2}&\boxed{1}&
\end{array},
\qquad
f^{(3,2)}=\frac{120}{4\cdot3\cdot1\cdot2\cdot1}=5.
\tag{38}
\]

There are two removable boxes, yielding \((2,2)\) and \((3,1)\). The latter has hook product \(4\cdot2=8\), hence dimension \(3\). The branching dimensions give \(2+3=5\). This check involves actual restriction summands, rather than merely an equality between unrelated numbers.

For a single row, every adjacent generator is \(+1\); for a single column, every one is \(-1\). The hook product is \(n!\) in both cases, giving dimension \(1\). The empty tableau supplies the base case at \(n=0\).

## 8. Exercises with complete solutions

### Exercise 1 (easy). Contents, hooks and a three-way restriction

Compute the content and hook arrays of \((4,2,1)\), its dimension, and the dimensions of all its \(S_6\) restriction summands.

**Solution.** The two arrays, in the same box coordinates, are

\[
\begin{array}{cccc}
\boxed{0}&\boxed{1}&\boxed{2}&\boxed{3}\\
\boxed{-1}&\boxed{0}&&\\
\boxed{-2}&&&
\end{array},
\qquad
\begin{array}{cccc}
\boxed{6}&\boxed{4}&\boxed{2}&\boxed{1}\\
\boxed{3}&\boxed{1}&&\\
\boxed{1}&&&
\end{array}.
\tag{39}
\]

Their hook product is \(144\), so \(f^{(4,2,1)}=7!/144=35\). All three row ends are removable. The resulting shapes are \((3,2,1)\), \((4,1,1)\), \((4,2)\). Their hook products are \(45,72,80\), respectively: the first has row hooks \(5,3,1\,/\,3,1\,/\,1\); the second \(6,3,2,1\,/\,2\,/\,1\); the third \(5,4,2,1\,/\,2,1\). Thus their dimensions are \(720/45=16\), \(720/72=10\), \(720/80=9\), and \(16+10+9=35\). Theorem 4.2 identifies the restriction as the direct sum of these three irreducibles.

### Exercise 2 (medium). The spectrum in \(S_3\)

Using (36), compute \(X_1,X_2,X_3\) on \(V_{(2,1)}\). Check commutation, content eigenvalues, and the two corresponding projector polynomials in \(\mathbb C[S_3]\).

**Solution.** Let \(D=\rho(s_1)\), \(M=\rho(s_2)\). Then
\(X_1=0\), \(\rho(X_2)=D\), and \(\rho(X_3)=M+MDM\). Direct multiplication gives

\[
MDM=
\begin{pmatrix}-\tfrac12&-\tfrac32\\
                 -\tfrac12&\tfrac12\end{pmatrix},
\qquad
\rho(X_3)=
\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\tag{40}
\]

These diagonal matrices commute, and their eigenvalue sequences are exactly those following (35). The other irreducibles are the trivial and sign representations, with sequences \((0,1,2)\) and \((0,-1,-2)\). Therefore

\[
P_A=\frac{(1+X_2)(2-X_3)}6,\qquad
P_B=\frac{(1-X_2)(2+X_3)}6
\tag{41}
\]

act as the two selected diagonal units in \(V_{(2,1)}\), and as zero in the other irreducibles. For example, the first polynomial evaluates to \(1\) on \((1,-1)\), to \(0\) on \((-1,1)\), to \(0\) on \((1,2)\), and to \(0\) on \((-1,-2)\). Fourier faithfulness proves that they are the stated idempotents in the group algebra itself. Their product is zero, but their sum is the central projector for \(V_{(2,1)}\), rather than the full identity of \(\mathbb C[S_3]\).

### Exercise 3 (medium). Prove the hook branching recursion

Without assuming the hook length formula, prove that
\(F(\lambda)=|\lambda|!/\prod_{b\in\lambda}h_\lambda(b)\) satisfies
\(F(\lambda)=\sum_{\mu\nearrow\lambda}F(\mu)\). Account for equal row lengths and trailing zero parts.

**Solution.** Choose a fixed length \(l\), and put \(\beta_i=\lambda_i+l-i\). Lemma 6.1 expresses
\(F(\lambda)=n!\prod_{i<j}(\beta_i-\beta_j)/\prod_i\beta_i!\), as a hook product identity independent of any tableau enumeration. For a removable row \(i\), replace \(\beta_i\) by \(\beta_i-1\). Each Vandermonde factor involving that coordinate contributes
\((\beta_i-\beta_j-1)/(\beta_i-\beta_j)\); its factorial contributes \(\beta_i\), and \((n-1)!/n!=1/n\). Thus the ratio is (34).

For an equal pair of consecutive row lengths, \(\beta_i-\beta_{i+1}=1\), so this formal ratio is zero. The same holds for all but the last zero row; the last has factor \(\beta_l=0\). Hence summing the formal ratios over all rows sums exactly over removable corners.

To evaluate that sum, use (32). Removing its simple poles gives
\(R(z)=1-\sum_i p_i/(z-\beta_i)\), with \(p_i\) as in Lemma 6.2. Its product expansion has coefficient \(\binom l2-\sum_i\beta_i=-n\) at \(z^{-2}\). Its partial-fraction expansion has coefficient \(-\sum_i\beta_i p_i\). Therefore \(\sum_i\beta_i p_i=n\), and the sum of the ratios (34) is \(1\). Multiplying by \(F(\lambda)\) proves the recursion. At the empty diagram the product is empty and \(F=1\). This proof uses no assumption that \(F\) is already a representation dimension.

### Exercise 4 (hard). Recover the commuting algebra from its spectrum

Give a complete proof of the commutation of the \(X_k\), their content spectrum, and their generation of the Gelfand–Tsetlin algebra. Explain why checking one irreducible alone would be insufficient for the last assertion.

**Solution.** Let \(Z_k\) be the sum of transpositions of \(S_k\). Conjugation permutes them, so \(Z_k\) is central in \(A_k\). For \(j\leq k\), \(Z_j\in A_k\), and hence \(Z_kZ_j=Z_jZ_k\). Since \(X_k=Z_k-Z_{k-1}\), the \(X_k\) commute in \(A_n\).

For the spectrum, begin with \(X_1=0\). Suppose \(X_k\) acts by the content of \(k\). The identity \(X_{k+1}=s_kX_ks_k+s_k\) follows by conjugating the individual transpositions in \(X_k\). For a standard swap pair with contents \(x,y\), its orthogonal matrix is (8), \(a=1/(y-x)\). Multiplication in (15) has off-diagonal entry \(b(a(x-y)+1)=0\), and diagonal entries \(y,x\), so it gives the contents of \(k+1\). In an unpaired case, the scalar is \(x+1/r=x+r=y\), since \(r=\pm1\). Induction proves the content action in every \(W_\lambda\simeq V_\lambda\).

Lemma 1.1 reconstructs a tableau from its content sequence, by selecting its successive addable boxes; their contents are distinct at each step. Therefore (21) selects one tableau line across the direct sum of all irreducibles. Its factors have nonzero denominators, and any different line has some distinct content, which supplies a zero factor. The \(P_T\) thus give every diagonal unit under the faithful Fourier isomorphism. Polynomials in the \(X_k\) are precisely the full diagonal algebra.

Every center \(Z(A_k)\) acts scalarly on the \(S_k\) irreducible component specified by a tableau's first \(k\) boxes. It is therefore diagonal and belongs to that polynomial algebra. Conversely (12) puts each \(X_k\) in the algebra generated by these centers. The inclusions prove equality (20). A matrix commuting with every diagonal unit has no off-diagonal entry, in each irreducible block, so the algebra is also its own commutant.

One irreducible representation does not give a faithful map from \(A_n\); it loses all the other Fourier blocks. An equality or polynomial identity in that one block need not hold in the group algebra. The use of all irreducibles, and their globally distinct content sequences, is what closes this proof.

The next lesson computes characters by symmetric functions and develops the Murnaghan–Nakayama rule. The dimension and branching results proved here will be available there without a forward character-theory dependency.

## References

- [VO] A. M. Vershik and A. Yu. Okounkov, *A New Approach to the Representation Theory of the Symmetric Groups. II*, revised 2005 paper, Theorem 5.8 and §6, Propositions 6.1–6.2, equations (6.3)–(6.5). [Primary paper, arXiv:math/0503040](https://arxiv.org/abs/math/0503040). These distinguish the tableau spectrum and the seminormal/orthogonal normalizations; our proofs use a direct matrix construction.

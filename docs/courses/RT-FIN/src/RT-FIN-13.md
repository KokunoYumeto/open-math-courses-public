# The symmetric groups I: Young tableaux and Young symmetrizers

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A permutation can move coordinates without changing their sum. It can also act on alternating tensors by its sign. These two familiar actions are the simplest members of a much larger family. A diagram of boxes tells us which permutations to average with equal coefficients and which to average with alternating signs. Combining these operations produces every irreducible representation of a symmetric group.

The construction takes place inside the group algebra. Its main difficulty is to prove that the resulting space is irreducible. We will do this by analyzing a cancellation: two labels in the same row and the same column allow a transposition to change the sign of a sum without changing the sum itself. A counting argument determines when this cancellation is possible. The regular trace then supplies the nonzero normalization needed to turn a Young symmetrizer into an idempotent.

We use complete reducibility from Representations and complete reducibility, the equality between the numbers of irreducible characters and conjugacy classes from Characters and the orthogonality relations, and the group-algebra viewpoint from The group algebra and Fourier analysis on a finite group. The integer-value conclusion uses character integrality from Integrality of characters and Burnside's theorem. For dual characters we use Tensor products, duals and real representations. This lesson supplies the rational models promised in Character criteria and splitting fields. Basic references are [Stevens], [Purbhoo], [Gruson–Serganova], and the original paper [Frobenius].

Take \(n\geq1\). Permutations compose from right to left. All group actions are left actions. Write \(A=\mathbb C[S_n]\), and regard its elements as operators on any complex representation by linear extension. A rational model will be constructed explicitly after the complex classification.

## 1. Averaging according to a pattern of boxes

A partition of \(n\) is a finite decreasing sequence of positive integers
\[
\lambda=(\lambda_1,\ldots,\lambda_r),\qquad
\lambda_1\geq\cdots\geq\lambda_r>0,\qquad
\sum_i\lambda_i=n.
\tag{1}
\]
Its Young diagram has \(\lambda_i\) boxes in row \(i\), with all rows starting in the same column. Row numbers increase downwards. Column numbers increase to the right. The conjugate partition records column lengths:
\[
\lambda'_j=\#\{i:\lambda_i\geq j\}.
\tag{2}
\]
Transposing a diagram twice gives the original diagram, so \((\lambda')'=\lambda\).

A tableau \(t\) of shape \(\lambda\) places the labels \(1,\ldots,n\) in its boxes, each once. A tableau is standard when labels increase along each row and down each column. For example,
\[
t=
\begin{array}{cccc}
\boxed{1}&\boxed{3}&\boxed{5}&\boxed{7}\\
\boxed{2}&\boxed{6}&&\\
\boxed{4}&&&
\end{array}
\tag{3}
\]
is standard and has shape \((4,2,1)\). The diagram and its row and column sets will matter immediately; standardness will matter for bases and dimension formulas in the next lesson. Any labeling can be used for the present construction.

Let \(R_t\) be the subgroup preserving each row's set of labels, and let \(C_t\) preserve each column's set. Thus
\[
R_t\cong\prod_i S_{\lambda_i},\qquad
C_t\cong\prod_j S_{\lambda'_j}.
\]
In (3), the nontrivial row sets are \(\{1,3,5,7\}\) and \(\{2,6\}\); the nontrivial column sets are \(\{1,2,4\}\) and \(\{3,6\}\). An element preserving both rows and columns must fix each label, since a box is the unique intersection of its row and column. Consequently
\[
R_t\cap C_t=\{1\}.
\tag{4}
\]

Define the row sum, column alternating sum, and Young symmetrizer by
\[
a_t=\sum_{p\in R_t}p,\qquad
b_t=\sum_{q\in C_t}\operatorname{sgn}(q)q,\qquad
c_t=a_tb_t.
\tag{5}
\]
This product order remains fixed throughout the lesson. On a vector, the right factor \(b_t\) acts first. In particular, our product applies column alternation and then row averaging. The sums use the groups of the original tableau throughout.

Reindexing the sums gives
\[
pa_t=a_tp=a_t,\qquad
qb_t=b_tq=\operatorname{sgn}(q)b_t
\quad(p\in R_t,\ q\in C_t).
\tag{6}
\]
Therefore
\[
pc_tq=\operatorname{sgn}(q)c_t.
\tag{7}
\]
Also \(a_t^2=|R_t|a_t\) and \(b_t^2=|C_t|b_t\). It does not follow just by multiplying these two identities that \(c_t\) is a scalar multiple of an idempotent: \(a_t\) and \(b_t\) need not commute.

The products \(pq\), with \(p\in R_t,q\in C_t\), are all distinct. Indeed, \(pq=p'q'\) implies
\[
(p')^{-1}p=q'q^{-1}\in R_t\cap C_t,
\]
and (4) forces equality of both factors. In particular, the coefficient of the identity in \(c_t\) is exactly \(1\). Hence \(c_t\ne0\).

For a first example, take
\[
t=\begin{array}{cc}\boxed{1}&\boxed{2}\\\boxed{3}&\end{array}.
\]
Then
\[
c_t=(1+(12))(1-(13))
=1+(12)-(13)-(132).
\tag{8}
\]
On the natural permutation representation with basis \(e_1,e_2,e_3\), it sends
\[
e_3\longmapsto 2e_3-e_1-e_2.
\]
This is a nonzero vector in the plane of coordinate sum zero. We will prove that the left ideal \(Ac_t\) is precisely an irreducible representation of this type.

## 2. When rows and columns force cancellation

We need a comparison between shapes. Extend a partition by zero parts. Say that \(\lambda\) dominates \(\mu\), written \(\lambda\unrhd\mu\), if
\[
\sum_{i=1}^k\lambda_i\geq\sum_{i=1}^k\mu_i
\quad\text{for every }k\geq1.
\tag{9}
\]
This is a partial order. Lexicographic order compares the first unequal parts instead and is a total order. These orders differ: \((4,1,1)\) is lexicographically larger than \((3,3)\), but neither dominates the other. We will use the prefix inequalities (9), and state explicitly when lexicographic order can also be used.

**Lemma 2.1 (tableau separation).** Let \(t,u\) have shapes \(\lambda,\mu\). Suppose that no two labels in a single row of \(t\) lie in a single column of \(u\). Then
\[
\sum_{i=1}^k\lambda_i\leq\sum_{i=1}^k\mu_i
\quad\text{for every }k.
\tag{10}
\]
If also \(\lambda\unrhd\mu\), then \(\lambda=\mu\). In this equal-shape case there are \(p\in R_t,q\in C_t\) such that
\[
u=pqt.
\tag{11}
\]
Equality of shapes and (11) also follow if the additional hypothesis is that \(\lambda\) is lexicographically at least \(\mu\).

**Proof.** Consider the labels belonging to the first \(k\) rows of \(t\). A column of \(u\) of height \(\mu'_j\) contains at most one label from each of these rows, and at most \(\mu'_j\) labels altogether. Summing over columns gives
\[
\sum_{i=1}^k\lambda_i
\leq\sum_j\min(k,\mu'_j)
=\sum_{i=1}^k\mu_i.
\tag{12}
\]
The last equality counts the boxes in the first \(k\) rows of the diagram of \(\mu\), column by column. This proves (10). Under dominance the opposite inequalities also hold, so the prefix sums, and hence the individual parts, are equal. Under the lexicographic hypothesis, a first unequal part would instead make the corresponding prefix sum of \(\lambda\) greater, contradicting (10). Thus that hypothesis also forces equality.

Now assume the shapes are equal. Each inequality in (12) is an equality. Every column must attain its individual bound: a smaller count in one column cannot be compensated by a larger count elsewhere. Subtracting the counts for \(k-1\) from those for \(k\), we see that column \(j\) of \(u\) contains exactly one label from row \(k\) of \(t\) if \(k\leq\lambda'_j\), and none otherwise.

Choose \(p\in R_t\) as follows. Send the label in box \((k,j)\) of \(t\) to that unique label from row \(k\) of \(t\) occurring in column \(j\) of \(u\). This is a permutation within each row. Thus \(pt\) and \(u\) have exactly the same set of labels in each column. There is a unique permutation \(w\) of labels with \(u=wt\). Since \(p^{-1}u\) and \(t\) have the same column sets, the permutation \(q=p^{-1}w\) belongs to \(C_t\). Hence \(w=pq\), proving (11). \(\square\)

The coefficient groups in (11) belong to \(t\). Replacing them by groups of a partially rearranged tableau would change the assertion.

**Lemma 2.2 (collision cancellation).** If a row of \(t\) and a column of \(u\) contain two common labels, then
\[
a_tb_u=0.
\tag{13}
\]
Consequently, if \(\lambda\) is not dominated by \(\mu\), then
\[
a_txb_u=0\qquad(x\in A).
\tag{14}
\]

**Proof.** Let \(\tau\) transpose the two common labels. It lies in \(R_t\cap C_u\), and its sign is \(-1\). By (6),
\[
a_tb_u=a_t\tau b_u=-a_tb_u.
\]
Since the coefficient field has characteristic zero, this proves (13).

For (14), first take \(x=g\in S_n\). The column alternating sum of \(gu\) is \(b_{gu}=gb_ug^{-1}\). Its shape is still \(\mu\). If there were no collision between rows of \(t\) and columns of \(gu\), Lemma 2.1 would say that \(\lambda\) is dominated by \(\mu\). Thus there is a collision, and
\[
a_tgb_u=a_tb_{gu}g=0.
\]
Linearity proves the assertion for every \(x\in A\). \(\square\)

For equal shapes, Lemma 2.1 says that every permutation \(g\notin R_tC_t\) creates a collision between a row of \(t\) and a column of \(gt\). This fact determines an entire space of group-algebra elements.

**Lemma 2.3 (the row-column symmetry space).** The elements \(x\in A\) satisfying
\[
pxq=\operatorname{sgn}(q)x
\quad(p\in R_t,\ q\in C_t)
\tag{15}
\]
form the one-dimensional space \(\mathbb Cc_t\).

**Proof.** Write \(x=\sum_g x_g g\). If \(g\notin R_tC_t\), choose a collision transposition
\[
\tau\in R_t\cap gC_tg^{-1},\qquad q=g^{-1}\tau g\in C_t.
\]
Then \(\tau gq=g\), while \(\operatorname{sgn}(q)=-1\). Comparing the coefficient of \(g\) in \(\tau xq=-x\) gives \(x_g=-x_g\), so \(x_g=0\).

On the remaining support, comparing the coefficient of \(pq\) in (15) gives
\[
x_{pq}=\operatorname{sgn}(q)x_1.
\]
The factorization \(pq\) is unique by (4). These are exactly the coefficients of \(x_1c_t\). Conversely, (7) shows that every multiple of \(c_t\) satisfies (15). \(\square\)

*Comparison:* [Gruson–Serganova, Chapter 6, Lemma 1.13 and Exercise 1.12]. Lemma 2.1 proves the collision alternative and the factorization in the fixed groups of \(t\); Lemma 2.3 then determines each coefficient. The product order is row sum followed by column sum, as in (5). The next proof establishes the nonzero normalization by trace before forming an idempotent; this is the step needed to justify division by \(\nu_t\).

## 3. A nonzero trace gives an irreducible left ideal

Put \(V_t=Ac_t\), with \(S_n\) acting by left multiplication. It is nonzero, since it contains \(c_t\). Lemma 2.3 immediately gives
\[
c_txc_t\in\mathbb Cc_t\quad(x\in A),
\qquad
c_t^2=\nu_tc_t
\tag{16}
\]
for some scalar \(\nu_t\). Indeed, these products have the left-row and right-column symmetries (15).

We must prove that \(\nu_t\ne0\) before dividing by it.

**Theorem 3.1 (normalization and irreducibility).** The scalar in (16) is a positive integer. If \(d_t=\dim_{\mathbb C}V_t\), then
\[
\nu_t=\frac{n!}{d_t}.
\tag{17}
\]
The element \(e_t=c_t/\nu_t\) is an idempotent, and \(V_t=Ae_t\) is irreducible.

**Proof.** Let \(T:A\to A\) be right multiplication by \(c_t\). In the group basis, the coefficient of \(g\) in \(T(g)=gc_t\) is the coefficient of \(1\) in \(c_t\), namely \(1\). Therefore
\[
\operatorname{Tr}(T)=n!.
\tag{18}
\]
If \(\nu_t=0\), then \(T^2=0\). Its image would lie in its kernel. A basis of the image, extended to a basis of the kernel and then to a basis of \(A\), would give zero diagonal entries for \(T\). This would make its trace zero, contradicting (18). Thus \(\nu_t\ne0\).

Now \(e_t^2=e_t\). Right multiplication by \(e_t\) has image \(Ae_t=Ac_t=V_t\), acts as the identity there, and vanishes on its kernel. These spaces form a direct sum: every \(x\) is the sum of \(xe_t\) and \(x-xe_t\). Its trace is consequently \(d_t\). Dividing (18) by \(\nu_t\) gives (17).

The coefficients of \(c_t\) are integers, so the coefficient of \(1\) in \(c_t^2\) is an integer. In (16) that coefficient is \(\nu_t\), because the identity coefficient in \(c_t\) is \(1\). Thus \(\nu_t\) is an integer; (17) makes it positive.

For irreducibility, (16) gives
\[
e_tAe_t=\mathbb Ce_t.
\tag{19}
\]
Every \(A\)-linear endomorphism \(f\) of \(Ae_t\) is determined by \(f(e_t)\). This value lies in \(Ae_t\), and
\[
f(e_t)=f(e_t^2)=e_tf(e_t),
\]
so it lies in \(e_tAe_t\). Conversely, for \(y\in e_tAe_t\), right multiplication by \(y\) defines an \(A\)-linear endomorphism of \(Ae_t\) taking \(e_t\) to \(y\). These operations give a vector-space isomorphism
\[
\operatorname{End}_A(Ae_t)\cong e_tAe_t.
\]
Its dimension is \(1\) by (19).

If \(Ae_t\) had a nonzero proper invariant subspace, complete reducibility would give a nonzero invariant complement. Projection onto each of the two summands would be an \(A\)-linear endomorphism. These two projections are linearly independent, contradicting the dimension \(1\). Hence \(Ae_t\), and therefore \(V_t\), is irreducible. \(\square\)

This proof distinguishes left multiplication, which defines the representation, from right multiplication, which computes its dimension and its endomorphisms. The element \(e_t\) itself need not commute with all of \(A\).

**Lemma 3.2 (changing labels).** Tableaux of the same shape yield isomorphic representations. Their dimensions and normalization constants agree.

**Proof.** If \(u=wt\), relabeling gives
\[
R_u=wR_tw^{-1},\qquad C_u=wC_tw^{-1},
\qquad c_u=wc_tw^{-1}.
\tag{20}
\]
Thus \(Ac_u=Ac_tw^{-1}\). The map \(v\mapsto vw^{-1}\) is an invertible map \(Ac_t\to Ac_u\) commuting with left multiplication by every group element. Its inverse is \(v\mapsto vw\). It preserves dimension, so (17) preserves the normalization constant. \(\square\)

We can consequently write \(V_\lambda\), \(d_\lambda\), and \(\nu_\lambda\), without choosing a particular tableau in the notation.

## 4. Counting classes completes the classification

First we show that different diagrams give different representations.

**Proposition 4.1 (different shapes).** If \(\lambda\ne\mu\), then \(V_\lambda\not\cong V_\mu\).

**Proof.** At least one of the dominance relations \(\lambda\unlhd\mu\) and \(\mu\unlhd\lambda\) fails, since both together would give equal prefix sums and equal partitions. Exchange the shapes if needed so that \(\lambda\unlhd\mu\) fails. For tableaux \(t,u\) of these shapes, Lemma 2.2 says
\[
c_txc_u=a_t(b_txa_u)b_u=0\quad(x\in A).
\tag{21}
\]
Hence \(c_t\) acts by zero on \(V_u\). It acts nontrivially on \(V_t\), since \(c_t^2=\nu_\lambda c_t\ne0\). An isomorphism commuting with the group action also commutes with every group-algebra element, and cannot identify these two actions of \(c_t\). \(\square\)

**Proposition 4.2 (cycle types and class sizes).** The conjugacy classes of \(S_n\) correspond to partitions of \(n\). If a cycle type has \(m_i\) cycles of length \(i\), then its centralizer has order
\[
z_\lambda=\prod_{i\geq1}i^{m_i}m_i!,
\tag{22}
\]
and its conjugacy class has \(n!/z_\lambda\) elements.

**Proof.** Conjugating a cycle \((a_1\,\cdots\,a_i)\) by \(g\) replaces its labels by \((g(a_1)\,\cdots\,g(a_i))\). Thus conjugation preserves cycle lengths. Conversely, if two permutations have the same cycle lengths, pair their cycles of each length, choose a starting point in every paired cycle, and match the subsequent entries in cyclic order. The resulting bijection of all labels conjugates one permutation to the other. Cycle lengths, listed in decreasing order, are exactly partitions of \(n\).

Let \(\sigma\) have the indicated cycle type. A commuting permutation \(h\) must send each orbit of \(\langle\sigma\rangle\) to an orbit of the same length: the equation \(h\sigma^k=\sigma^kh\) preserves its size. For the \(m_i\) orbits of length \(i\), there are \(m_i!\) ways to permute them. Once this permutation of orbits is chosen, there are \(i\) choices for the image of one starting point in each orbit; commutation fixes all the other images. There are therefore \(i^{m_i}m_i!\) choices for this length. Choices at different lengths are independent and exhaust all commuting bijections, proving (22). The orbit-stabilizer formula for conjugation gives the class size. \(\square\)

For instance, in \(S_6\) the type \((3,2,1)\) has \(z_\lambda=3\cdot2\cdot1=6\) and a class of size \(120\). The type \((2,2,1,1)\) has \(z_\lambda=2^2\cdot2!\cdot2!=16\) and a class of size \(45\).

*Comparison:* [Gruson–Serganova, Chapter 6, Remark 1.2]. The cycle relabeling and commuting-cycle counts above prove the criterion and the centralizer order (22) explicitly.

**Theorem 4.3 (complete classification).** The representations \(V_\lambda\), one for each partition \(\lambda\) of \(n\), form a complete list of the irreducible complex representations of \(S_n\), with no repetitions.

**Proof.** Theorem 3.1 constructs a nonzero irreducible for every partition. Proposition 4.1 makes them pairwise nonisomorphic. Proposition 4.2 identifies the number of partitions with the number of conjugacy classes. The earlier character-basis theorem identifies the number of conjugacy classes with the number of irreducible complex characters. Thus the constructed list already has the full required size; an additional irreducible would exceed that size. \(\square\)

**Corollary 4.4 (rational models).** Every irreducible complex representation of \(S_n\), and every finite-dimensional complex representation of \(S_n\), has a model over \(\mathbb Q\).

**Proof.** The element \(c_t\) belongs to \(\mathbb Q[S_n]\). Put
\[
W_t=\mathbb Q[S_n]c_t.
\tag{23}
\]
The vectors \(gc_t\) have rational coordinates in the group basis. Row reduction over \(\mathbb Q\) selects a basis of their span; the same pivots and free-variable relations hold over \(\mathbb C\). Hence the natural map
\[
\mathbb C\otimes_{\mathbb Q}W_t\longrightarrow Ac_t,
\qquad z\otimes w\longmapsto zw
\tag{24}
\]
is an isomorphism, respecting the group action. The right side is \(V_\lambda\). This gives the promised rational model. It is irreducible over \(\mathbb Q\) as well: a nonzero proper rational invariant subspace would complexify to a nonzero proper invariant subspace, with the same dimension.

By Theorem 4.3 these models cover every complex irreducible. For an arbitrary complex representation, use its irreducible direct-sum decomposition and take the same direct sum of the rational models, with the same multiplicities. \(\square\)

This is stronger than merely showing that the characters have rational values. As the quaternion example in the preceding lesson shows, rational character values alone do not supply rational matrices.

**Corollary 4.5 (multiplicity from a symmetrizer).** If \(U\) is a complex representation, then the multiplicity of \(V_\lambda\) in \(U\) is
\[
\operatorname{rank}\bigl(c_t:U\to U\bigr).
\tag{25}
\]

**Proof.** On \(V_t=Ac_t\), the image \(c_tV_t=c_tAc_t\) is the line \(\mathbb Cc_t\), since it is contained in that line by (16) and contains the nonzero element \(c_t^2\). Its rank is \(1\).

If \(c_t\) acted nontrivially on an irreducible \(V_\mu\), then \(e_t\) would too. Choose a nonzero \(v\in e_tV_\mu\). The map
\[
Ae_t\longrightarrow V_\mu,\qquad xe_t\longmapsto xv
\]
is well-defined, because \(v=e_tv\). It is a nonzero homomorphism between irreducibles, so it is an isomorphism. Thus \(\mu=\lambda\) by Proposition 4.1. The rank is consequently \(0\) on every other irreducible. Taking a direct sum of the irreducibles in \(U\) adds these ranks and proves (25). \(\square\)

*Reference:* [Gruson–Serganova, Chapter 6, Theorem 1.7, Corollary 1.16 and Lemma 1.21]. The trace and endomorphism arguments above give the normalization and irreducibility explicitly.

## 5. Transposition of a diagram and the sign representation

The row and column groups switch places when the tableau is transposed. The product order also switches under the sign operation, so we first account for that change.

**Lemma 5.1 (the opposite product gives the same representation).** For a tableau with \(a=a_t,b=b_t,c=ab\), the left ideals \(Aab\) and \(Aba\) are isomorphic.

**Proof.** Define the linear anti-automorphism
\[
\left(\sum_g x_gg\right)^*=\sum_g x_gg^{-1}.
\]
It reverses products: \((xy)^*=y^*x^*\). Since both defining groups are closed under inverses and sign is unchanged by inversion, \(a^*=a,b^*=b\). Applying this operation to \((ab)^2=\nu_\lambda ab\) gives
\[
(ba)^2=\nu_\lambda ba.
\tag{26}
\]
Right multiplication by \(a\) maps \(Aab\) into \(Aba\), since \(xaba=(xa)ba\). Right multiplication by \(b\) maps \(Aba\) into \(Aab\). Both maps commute with the left action. Their composites are
\[
v\longmapsto vab=\nu_\lambda v\quad(v\in Aab),
\qquad
w\longmapsto wba=\nu_\lambda w\quad(w\in Aba).
\]
Since \(\nu_\lambda\ne0\), right multiplication by \(a\) has inverse \(1/\nu_\lambda\) times right multiplication by \(b\). \(\square\)

**Proposition 5.2 (conjugate diagrams).** For every partition,
\[
V_{\lambda'}\cong V_\lambda\otimes\operatorname{sgn}.
\tag{27}
\]

**Proof.** Let \(s=t^{\mathsf T}\) be the transposed tableau. Define an algebra automorphism
\[
\omega:A\to A,\qquad \omega(g)=\operatorname{sgn}(g)g.
\]
It preserves products because sign is multiplicative, and \(\omega^2=1\). Since \(R_s=C_t\) and \(C_s=R_t\), formula (5) gives
\[
\omega(a_t)=b_s,\qquad
\omega(b_t)=a_s,\qquad
\omega(c_t)=b_sa_s.
\tag{28}
\]
Identify \(V_\lambda\otimes\operatorname{sgn}\) with the vector space \(Ac_t\) equipped with action \(g\cdot v=\operatorname{sgn}(g)gv\). On this twisted action,
\[
\omega(g\cdot v)
=\operatorname{sgn}(g)\omega(g)\omega(v)
=g\omega(v).
\]
Thus \(\omega\) is an isomorphism from this twisted module onto \(Ab_sa_s\). Lemma 5.1 identifies the latter with \(Aa_sb_s=V_{\lambda'}\). \(\square\)

In particular, conjugate shapes have the same dimension. A self-conjugate shape gives a representation isomorphic to its sign twist.

There is also a useful concrete model using row sets. A tabloid \(\{t\}\) remembers which labels occur in each row and forgets their order within that row. Let \(M^\lambda\) be the permutation representation on tabloids of shape \(\lambda\), and form the polytabloid
\[
\epsilon_t=b_t\{t\}.
\tag{29}
\]

**Proposition 5.3 (the tabloid model).** The subspace \(S^\lambda\) spanned by all the polytabloids of shape \(\lambda\) is a representation isomorphic to \(V_\lambda\).

**Proof.** Relabeling gives \(g\epsilon_t=\epsilon_{gt}\), so their span is invariant. The left ideal \(Aa_t\) has a basis \(ga_t\) indexed by left cosets \(S_n/R_t\): different cosets have disjoint supports in the group basis. These cosets also index the tabloids \(g\{t\}\), since the stabilizer of \(\{t\}\) is exactly \(R_t\). Therefore
\[
Aa_t\longrightarrow M^\lambda,\qquad
ga_t\longmapsto g\{t\}
\tag{30}
\]
is a well-defined equivariant isomorphism. It sends \(b_ta_t\) to \(b_t\{t\}=\epsilon_t\), and hence sends \(Ab_ta_t\) onto the span of the vectors \(g\epsilon_t\). Every tableau is a relabeling of \(t\), so that span is \(S^\lambda\). Finally Lemma 5.1 gives \(Ab_ta_t\cong Aa_tb_t=V_\lambda\). \(\square\)

The names Specht module and Young-symmetrizer representation therefore describe equivalent models here. Proposition 5.3 proves the equivalence; no basis theorem for standard polytabloids is being assumed.

*Reference:* [Purbhoo, §6.4] for the polytabloid construction; [Gruson–Serganova, Chapter 6, Exercises 1.22–1.23] for the opposite product and sign twist.

## 6. Recognizing the small representations

For \((n)\), the row group is \(S_n\), the column group is trivial, and \(c_t=\sum_g g\). Left multiplication fixes this sum, so \(V_{(n)}\) is trivial and \(\nu_{(n)}=n!\).

For \((1^n)\), the roles reverse and \(c_t=\sum_g\operatorname{sgn}(g)g\). Left multiplication by \(h\) multiplies this sum by \(\operatorname{sgn}(h)\). Thus \(V_{(1^n)}\) is the sign representation, again with normalization \(n!\).

For \(n\geq2\), fill \((n-1,1)\) with \(1,\ldots,n-1\) in the first row and \(n\) below the first box. Then
\[
c_t=\left(\sum_{p\in S_{n-1}}p\right)(1-(1n)).
\]
In the permutation representation \(E=\mathbb C^n\), the coordinate-sum-zero subspace
\[
E_0=\{(x_1,\ldots,x_n):\textstyle\sum_i x_i=0\}
\]
is irreducible. To prove this, let \(W\subseteq E_0\) be a nonzero invariant subspace and choose nonzero \(v\in W\). Its coordinates cannot all agree, because their sum is zero. Choose \(i,j\) with \(v_i\ne v_j\). Then
\[
v-(ij)v=(v_i-v_j)(e_i-e_j)\in W.
\]
Permuting labels gives every coordinate difference, and those differences span \(E_0\). Hence \(W=E_0\).

Moreover,
\[
c_te_n=(n-1)!\,e_n-(n-2)!\sum_{i=1}^{n-1}e_i\ne0.
\tag{31}
\]
The vector has sum zero. The equivariant map \(Ac_t\to E_0\), \(v\mapsto ve_n\), has a nonzero image, which is all of \(E_0\). Its kernel is zero by the irreducibility of \(Ac_t\). Therefore
\[
V_{(n-1,1)}\cong E_0,\qquad
d_{(n-1,1)}=n-1,\qquad
\nu_{(n-1,1)}=\frac{n!}{n-1}.
\tag{32}
\]

For \(S_3\), (8) consequently gives its two-dimensional standard representation. Put \(s=(23)\) and take the group-algebra basis \(c_t,sc_t\). Under the isomorphism above its images are
\[
w_1=2e_3-e_1-e_2,\qquad
w_2=2e_2-e_1-e_3.
\]
These are independent. Directly permuting their coordinates gives the rational matrices
\[
\rho((12))=
\begin{pmatrix}1&-1\\0&-1\end{pmatrix},
\qquad
\rho((23))=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{33}
\]
Together with the trivial and sign representations these give all three shapes of size \(3\). Their dimensions \(1,2,1\) have squares summing to \(6\).

### The shape \((2,2)\) in \(S_4\)

Let \(S_4\) act on the three pairings
\[
M_1=12|34,\qquad M_2=13|24,\qquad M_3=14|23.
\tag{34}
\]
Here \(12|34\), for example, means the unordered set of pairs \(\{\{1,2\},\{3,4\}\}\). In the permutation representation with basis \(f_1,f_2,f_3\) for these pairings, let
\[
W=\{x_1f_1+x_2f_2+x_3f_3:x_1+x_2+x_3=0\}.
\]
The action on the three pairings is onto \(S_3\): \((12)\) fixes \(M_1\) and swaps \(M_2,M_3\), while \((23)\) swaps \(M_1,M_2\) and fixes \(M_3\). Those two transpositions generate the full permutation group of the pairings. The coordinate-difference proof just given therefore makes \(W\) irreducible and two-dimensional.

For the tableau with first row \(1,2\) and second row \(3,4\), we have
\[
a_t=(1+(12))(1+(34)),\qquad
b_t=(1-(13))(1-(24)).
\tag{35}
\]
On the pairings, \((12)\) and \((34)\) have the same action \(S\), swapping \(M_2,M_3\). The permutations \((13),(24)\) have the same action \(T\), swapping \(M_1,M_3\). Hence \(a_t=2(I+S)\) and \(b_t=2(I-T)\) on this space. In particular,
\[
c_tf_1=4(2f_1-f_2-f_3)\ne0.
\tag{36}
\]
The equivariant map \(Ac_t\to W\), \(v\mapsto vf_1\), is nonzero and thus an isomorphism between these irreducibles. Consequently
\[
d_{(2,2)}=2,\qquad \nu_{(2,2)}=24/2=12.
\]
Its character is the number of fixed pairings minus \(1\). The five cycle types give respectively \(3,1,3,0,1\) fixed pairings. A double transposition fixes all three; a \(3\)-cycle permutes them cyclically; and \((1234)\) fixes \(M_2\) while exchanging \(M_1,M_3\). This proves the \((2,2)\) row in the table below.

The standard representation has character equal to the number of fixed labels minus \(1\). Proposition 5.2 supplies its sign twist, of shape \((2,1,1)\). The resulting full character table is

| Shape | \(1^4\) | \(2\,1^2\) | \(2^2\) | \(3\,1\) | \(4\) |
|---|---:|---:|---:|---:|---:|
| Class size | \(1\) | \(6\) | \(3\) | \(8\) | \(6\) |
| \((4)\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \((3,1)\) | \(3\) | \(1\) | \(-1\) | \(0\) | \(-1\) |
| \((2,2)\) | \(2\) | \(0\) | \(2\) | \(-1\) | \(0\) |
| \((2,1,1)\) | \(3\) | \(-1\) | \(-1\) | \(0\) | \(1\) |
| \((1^4)\) | \(1\) | \(-1\) | \(1\) | \(1\) | \(-1\) |

Every entry follows from one of the concrete actions above. There are five partitions and five rows of characters. Their degree squares sum to \(1+9+4+9+1=24\), in agreement with the regular representation.

For \(S_1\), the trivial and sign constructions coincide because there is only one partition. The case \(S_0=\{1\}\) can also be included: use the empty partition, empty tableau, \(a=b=c=1\), and dimension and normalization \(1\).

## 7. Exercises with complete solutions

### Exercise 1 (easy). An unnormalized projection in \(\mathbb Q[S_3]\)

Use the tableau in (8). Expand \(c_t^2\) directly in the group basis and show that \(c_t^2=3c_t\). Determine the image and kernel of \(c_t/3\) on the natural three-dimensional permutation representation.

**Solution.** Write \(a=(12),b=(13),d=ab=(132)\), so \(c_t=1+a-b-d\). We have \(a^2=b^2=1\), \(da=aba=bab\), \(db=a\), and \(d^2=ba\). The four contributions to the square are
\[
\begin{aligned}
1c_t&=1+a-b-d,\\
ac_t&=a+1-d-b,\\
-bc_t&=-b-ba+1+bab,\\
-dc_t&=-d-aba+a+ba.
\end{aligned}
\]
The \(ba\) terms cancel, as do \(bab\) and \(aba\). The remaining sum is \(3+3a-3b-3d=3c_t\).

For \(v=x_1e_1+x_2e_2+x_3e_3\), first \(1-(13)\) gives
\[
(x_1-x_3)(e_1-e_3).
\]
Then \(1+(12)\) gives
\[
c_tv=(x_1-x_3)(e_1+e_2-2e_3).
\tag{37}
\]
Thus the image of \(c_t/3\) is the line spanned by \(e_1+e_2-2e_3\), and its kernel is the plane \(x_1=x_3\). On that spanning vector, \(x_1-x_3=3\), so \(c_t/3\) fixes it. This is an idempotent projection inside the permutation representation. Its image alone is not an \(S_3\)-invariant line: applying \((23)\) changes that line. The irreducible left ideal \(Ac_t\) includes all left translates of \(c_t\), rather than only the image of this one projection.

### Exercise 2 (medium). Transpose the pattern, including the product order

Prove (27) directly from the two averaging sums. Account for the opposite product with explicit invertible maps, and deduce that conjugate partitions have equal normalization constants.

**Solution.** For \(s=t^{\mathsf T}\), its row group is \(C_t\) and its column group is \(R_t\). The sign automorphism \(\omega(g)=\operatorname{sgn}(g)g\) therefore sends \(a_t\) to \(b_s\) and \(b_t\) to \(a_s\). It sends \(Ac_t\) onto \(Ab_sa_s\). If the domain has the sign-twisted action, then
\[
\omega(\operatorname{sgn}(g)gv)=g\omega(v),
\]
so this is an equivariant isomorphism from \(V_\lambda\otimes\operatorname{sgn}\).

Put \(a=a_s,b=b_s,\nu=\nu_{\lambda'}\). The inversion anti-automorphism fixes \(a,b\), so from \((ab)^2=\nu ab\) it gives \((ba)^2=\nu ba\). Define
\[
F:Aab\to Aba,\quad F(v)=va,\qquad
H:Aba\to Aab,\quad H(w)=wb.
\]
The formulas land in the stated ideals because \(xaba=(xa)ba\) and \(xbab=(xb)ab\). For \(v=xab\) and \(w=xba\), we have \(HF(v)=\nu v\) and \(FH(w)=\nu w\). Thus \(F^{-1}=H/\nu\), and \(Ab_sa_s\cong Aa_sb_s=V_{\lambda'}\). This proves the sign-twist formula with the fixed order \(c_t=a_tb_t\). Tensoring with a line preserves dimension. Formula (17) then gives \(\nu_{\lambda'}=\nu_\lambda\).

### Exercise 3 (medium). Rational matrices, integer traces, and duality

Construct a rational model for each \(V_\lambda\). Prove that its character takes integer values, and deduce that \(V_\lambda\) is isomorphic to its dual. Explain why a rational-valued character by itself would be insufficient for the first conclusion.

**Solution.** The span \(W_t=\mathbb Q[S_n]c_t\) is stable under left multiplication. Its spanning vectors \(gc_t\) have rational coordinates. Select a basis by rational row reduction. Its independence persists over \(\mathbb C\), and every complex linear combination of the vectors \(gc_t\) lies in its complex span. This proves the equivariant isomorphism (24). It constructs matrices over \(\mathbb Q\) for the representation, rather than only constructing values of its trace.

For any \(g\), the trace is consequently rational. It is also an algebraic integer: if \(g\) has order \(r\), its eigenvalues satisfy \(x^r=1\), and so are roots of unity. The sum of these eigenvalues is an algebraic integer, using the closure of algebraic integers under addition proved in the integrality lesson.

A rational algebraic integer is an integer. Indeed, write it as \(a/b\) in lowest terms with \(b>0\). If it satisfies a monic polynomial of degree \(m\) with integer coefficients, multiplying that equation by \(b^m\) shows that \(b\) divides \(a^m\). Coprimality forces \(b=1\). Thus \(\chi_\lambda(g)\in\mathbb Z\).

The character of the dual is \(\chi_\lambda(g^{-1})=\overline{\chi_\lambda(g)}\). Integer values are real, so this is \(\chi_\lambda(g)\). The earlier character-isomorphism criterion now gives \(V_\lambda^*\cong V_\lambda\). This duality statement is distinct from the sign twist (27). Finally, the irreducible two-dimensional quaternion representation in the preceding lesson has integer character values and no rational model. That example shows why the matrix construction above cannot be replaced by a claim about rational-valued traces.

### Exercise 4 (hard). Recover the separating permutations

Suppose no two labels in a row of \(t\) occur in a column of \(u\). Prove the prefix inequalities (10). Under \(\lambda\unrhd\mu\), construct \(p\in R_t,q\in C_t\) with \(u=pqt\), including when the two shapes have equal row lengths. Deduce that \(\lambda>_{\mathrm{lex}}\mu\) forces a collision for every pair of tableaux of those shapes.

**Solution.** Let \(B_k\) be the labels in the first \(k\) rows of \(t\). Its size is \(\sum_{i\leq k}\lambda_i\). Each column \(j\) of \(u\) meets \(B_k\) in at most \(\min(k,\mu'_j)\) labels. Summing gives (12), hence (10). If dominance gives the reverse inequalities, all prefixes agree and subtraction gives \(\lambda_i=\mu_i\) for every \(i\).

In the equal-shape case, write \(N_{k,j}\) for the number of labels of \(B_k\) in column \(j\) of \(u\). Its upper bound is \(\min(k,\lambda'_j)\), and the sum of these bounds equals \(|B_k|\). Since the actual sum is also \(|B_k|\), each bound is attained. Thus
\[
N_{k,j}-N_{k-1,j}=
\begin{cases}
1,&k\leq\lambda'_j,\\
0,&k>\lambda'_j.
\end{cases}
\tag{38}
\]
For each existing box \((k,j)\), let \(x_{k,j}\) be the unique label in column \(j\) of \(u\) that belongs to row \(k\) of \(t\). Define \(p\) by sending the label in box \((k,j)\) of \(t\) to \(x_{k,j}\). The images exhaust row \(k\)'s labels, so this defines a permutation in \(R_t\), even if several row lengths are equal. The argument uses the individually numbered rows, not a strict decrease of their lengths.

Let \(w\) be the unique label permutation taking \(t\) to \(u\). The tableaux \(pt\) and \(u\) have the same column sets by construction. Therefore \(p^{-1}wt\) has the same column sets as \(t\), so \(q=p^{-1}w\) preserves every such set and lies in \(C_t\). This gives \(w=pq\) and \(u=pqt\).

Finally, if \(\lambda>_{\mathrm{lex}}\mu\), let \(k\) be their first unequal part. The earlier parts agree, and \(\lambda_k>\mu_k\); hence their \(k\)-th prefix sums violate (10). Absence of a collision is impossible, independently of the labels in either tableau. This proves the asserted collision for every pair. It also explains why the chosen order must be named.

The next lesson develops bases indexed by standard tableaux and dimension formulas. The present classification and its rational models did not require assuming those formulas.

## References

- [Stevens] James Stevens, *Schur–Weyl duality*, University of Chicago REU paper, 2016, §2.1, Theorem 2.1 and Lemmas 2.3–2.7. [Open text](https://math.uchicago.edu/~may/REU2016/REUPapers/Stevens.pdf).
- [Purbhoo] Kevin Purbhoo, *Lecture Notes for C&O 430/630*, Fall 2010, §6.4, Lemmas 6.4.3–6.4.4 and Theorems 6.4.5–6.4.6. [Open text](https://www.math.uwaterloo.ca/~kpurbhoo/fall2011-co630/co630notes.pdf).
- [Gruson–Serganova] Caroline Gruson and Vera Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Universitext, Springer, 2018, Chapter 6, §1, especially Theorem 1.7, items 1.13–1.19, Lemma 1.21 and Exercises 1.22–1.23.
- [Frobenius] Ferdinand Georg Frobenius, “Über die charakteristischen Einheiten der symmetrischen Gruppe,” *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin* (1903), 328–358; reprinted as paper 68 in *Gesammelte Abhandlungen*, Volume III. The introduction and §§1–2 discuss rational realizations and the trace and rank of characteristic idempotents.

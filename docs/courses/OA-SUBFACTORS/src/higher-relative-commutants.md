# Reflection, commuting squares and finite depth

A finite-index inclusion has an infinite Jones tower, but each higher relative commutant is finite dimensional. The Jones projection identifies an old part at the next level by reflection. Whatever remains records new information. Finite depth means that, from some point onward, no new part appears.

We assume [Going up and down the Jones tower](towers-and-tunnels.md), [Measuring an inclusion through modules and corners](module-dimension-and-local-index.md), [Finite bases, bounded vectors and a positive-operator inequality](finite-bases-and-positive-index.md), [Matrix inclusions and the Markov trace](finite-dimensional-markov-calculus.md), and [Positivity restricts the index](positivity-and-index-rigidity.md). References are [Jones] and [Popa].

Construction and proof sources: The actual tower and expectations come from [Going up and down the Jones tower](towers-and-tunnels.md) and [Finite bases, bounded vectors and a positive-operator inequality](finite-bases-and-positive-index.md). Proposition 12.3 and Theorem 12.4 below apply Theorem 8.6 of [Matrix inclusions and the Markov trace](finite-dimensional-markov-calculus.md) to the marked Jones ideal and its reflected inclusion. Theorems 12.5–12.7 prove support persistence, graph norm and the discrete depth bound; Proposition 12.8 retains the general pointwise graph-weight equation. The explicit level corrections and Example 12.9 are the comparison with Takesaki, Chapter XIX, §4.

Throughout, \(N\subseteq M\) are II₁ factors, \(d=[M:N]<\infty\), and \(\lambda=d^{-1}\). Use

\[
M_{-1}=N,\qquad M_0=M,\qquad
M_{k+1}=\langle M_k,e_k\rangle,
\]

where \(e_k\) remembers \(M_{k-1}\subseteq M_k\). All these algebras carry compatible normalized traces. Set

\[
\begin{gathered}
A_k=N'\cap M_k\quad(k\geq-1),\\
B_k=M'\cap M_k\quad(k\geq0).
\end{gathered}
\tag{12.1}
\]

In particular \(A_{-1}=B_0=\mathbb C\).

A third row, when needed, is

\[
\begin{gathered}
C_k=M_1'\cap M_k=B_k\cap\{e_0\}',\\
k\geq1,\qquad C_1=\mathbb C.
\end{gathered}
\]

The equality follows from \(M_1=\langle M,e_0\rangle\): commuting with \(M_1\) is exactly commuting with both generators. Thus this row is determined by the marked ladder, including its first Jones projection. It is the shifted second row for the dual inclusion \(M\subset M_1\). Its finite dimensionality follows from \([M_k:M_1]=d^{k-1}\).

## What the invariant contains

Each \(A_k\) and \(B_k\) is finite dimensional: index multiplicativity gives \([M_k:N]=d^{k+1}\), and the finite-index relative-commutant bound applies. The inclusions form a ladder

\[
\begin{array}{ccccccc}
A_0&\subseteq&A_1&\subseteq&A_2&\subseteq&\cdots\\
\cup&&\cup&&\cup\\
B_0&\subseteq&B_1&\subseteq&B_2&\subseteq&\cdots.
\end{array}
\tag{12.2}
\]

The traces, inclusions and Jones projections belong to this data. Forgetting them and retaining only the sizes of the matrix blocks loses information. We call this structured ladder the **standard invariant** in its higher-relative-commutant form.

**Proposition 12.1.** An isomorphism of inclusions extends canonically up the Jones towers and gives an isomorphism of the structured ladders (12.2).

**Proof.** Let \(\alpha:M\to\widetilde M\) carry \(N\) onto \(\widetilde N\). It preserves normalized traces by uniqueness. The unitary \(\widehat x\mapsto\widehat{\alpha(x)}\) identifies the tracial Hilbert spaces, their left actions, and the projections onto the smaller Hilbert spaces. Conjugation therefore extends \(\alpha\) to the first basic constructions and carries \(e_0\) to \(\widetilde e_0\). Repeat this argument at every level. Commutation with \(N\) or \(M\) is preserved, giving the stated ladder isomorphism, including its traces and projections. \(\square\)

## Every small square commutes

A square of finite tracial algebras

\[
\begin{array}{ccc}P&\subseteq&Q\\\cup&&\cup\\R&\subseteq&S\end{array}
\]

is equipped with a specified faithful normal tracial state on \(Q\), restricted to its subalgebras. It is a **commuting square** if the trace-preserving expectations in \(Q\) onto \(P\) and \(S\) commute and their product is the expectation onto \(R\).

**Theorem 12.2.** For \(0\leq k\leq l\), the square

\[
\begin{array}{ccc}A_k&\subseteq&A_l\\\cup&&\cup\\B_k&\subseteq&B_l\end{array}
\tag{12.3}
\]

is a commuting square.

**Proof.** The expectation \(E_{M_k}:M_l\to M_k\) is \(N\)-equivariant, because \(N\subseteq M_k\). Its restriction maps \(A_l\) onto \(A_k\) and preserves the trace, so it is \(E_{A_k}\). Likewise it maps \(B_l\) onto \(B_k\).

For a direct proof of commutation, work in the ambient space \(L^2(M_l)\). Conjugation by the unitaries of \(M\) has fixed-vector space \(L^2(B_l)\). Indeed, bounded fixed vectors are exactly \(M'\cap M_l\); truncating the absolute value of a fixed affiliated operator gives the same assertion for all square-integrable vectors. The orthogonal projection onto this space is the expectation onto \(B_l\). The projection onto \(L^2(M_k)\) commutes with every such conjugation, because \(M\subseteq M_k\). It consequently commutes with the projection onto the fixed-vector space. Restrict both projections to \(L^2(A_l)\): their ranges there are \(L^2(A_k)\) and \(L^2(B_l)\), respectively. The first paragraph shows that the restriction is legitimate, and \(B_l\subseteq A_l\) gives the second restriction. Their intersection is \(L^2(B_k)\). The product of commuting orthogonal projections is the projection onto their intersection, proving (12.3). Conjugation by a general unitary of \(M\) need not preserve \(A_l\); using the ambient space is essential. \(\square\)

The same argument works for any two fixed starting levels of the Jones tower. Thus one obtains the corresponding squares for \(M_j'\cap M_k\) as well.

## The Jones corner sees two levels back

**Proposition 12.3.** For \(k\geq0\),

\[
\begin{gathered}
e_k\in A_{k+1}\cap A_{k-1}',\\
e_kA_{k+1}e_k=A_{k-1}e_k,\\
A_{k-1}e_k\cong A_{k-1}.
\end{gathered}
\tag{12.4}
\]

For \(x\in A_k\),

\[
e_kxe_k=E_{A_{k-1}}(x)e_k.
\tag{12.5}
\]

**Proof.** The Jones projection commutes with \(M_{k-1}\), which contains \(N\); this gives the first membership assertion. The full basic-construction corner is \(e_kM_{k+1}e_k=M_{k-1}e_k\), and the map \(a\mapsto ae_k\) is faithful on \(M_{k-1}\).

If \(x\in A_{k+1}\), write \(e_kxe_k=ae_k\) for its unique \(a\in M_{k-1}\). For \(u\in\mathcal U(N)\), equivariance gives \((uau^*)e_k=ae_k\). Faithfulness implies \(uau^*=a\), so \(a\in A_{k-1}\). Conversely, each \(a\in A_{k-1}\) gives an element \(ae_k\) in this corner. Finally, \(E_{M_{k-1}}\) maps \(A_k\) onto \(A_{k-1}\) by \(N\)-equivariance, and its restriction is the trace-preserving expectation. The usual compression identity gives (12.5). \(\square\)

## The reflected part is an ideal

Let \(z_k\) be the central support of \(e_k\) in \(A_{k+1}\).

**Theorem 12.4.** The span

\[
I_k=\operatorname{span}(A_ke_kA_k)
\]

is a two-sided ideal of \(A_{k+1}\), and

\[
I_k=z_kA_{k+1}\cong\langle A_k,e_{A_{k-1}}\rangle.
\tag{12.6}
\]

Multiplication by \(z_k\) is faithful on \(A_k\). If \(D_k\) is the inclusion matrix of \(A_{k-1}\subseteq A_k\), the inclusion matrix of \(z_kA_k\subseteq z_kA_{k+1}\) is \(D_k^{\mathsf T}\). The complementary summand \((1-z_k)A_{k+1}\) is the new part.

**Proof.** The pull-down map for the finite-index inclusion \(M_{k-1}\subseteq M_k\) is

\[
R_k(X)=dE_{M_k}(Xe_k),\qquad R_k(X)e_k=Xe_k.
\]

It maps \(A_{k+1}\) into \(A_k\): both the expectation and multiplication by \(e_k\) are equivariant under conjugation by \(N\). For \(X\in A_{k+1}\) and \(b,c\in A_k\),

\[
Xbe_kc=R_k(Xb)e_kc\in I_k.
\]

Taking adjoints gives the analogous right-ideal assertion. Thus \(I_k\) is a two-sided ideal. In a finite-dimensional algebra an ideal has a central identity, here exactly the central support \(z_k\) of its generating projection.

Apply Theorem 8.6 to \(A_{k-1}\subseteq A_k\), represented in \(M_{k+1}\), with projection \(e_k\). Proposition 12.3 supplies its compression and faithfulness assumptions. On its central support, the algebra generated by \(A_k\) and \(e_k\) is the usual finite-dimensional basic construction. This central-support algebra is precisely \(I_k=z_kA_{k+1}\), proving (12.6) and the transpose rule.

If \(bz_k=0\) for \(b\in A_k\), then \(be_k=0\). Compress \(b^*b\) to obtain \(E_{A_{k-1}}(b^*b)e_k=0\). Faithfulness of \(a\mapsto ae_k\) and of the expectation implies \(b=0\). Thus the reflected copy retains the whole preceding algebra. \(\square\)

The assertion concerns multiplicities as well as block sizes. Replacing an inclusion matrix by its transpose reverses every edge, including repeated edges.

In particular, the triple \(A_{k-1}\subseteq A_k\subseteq A_{k+1}\) is the full basic construction precisely when

\[
\bigvee_{u\in\mathcal U(A_k)}ue_ku^*=1.
\]

Indeed, this join is \(z_k\). It is at most \(z_k\), since that central projection contains every conjugate. Conversely, the linear span of the unitaries is \(A_k\), so the join contains the ranges of all \(ae_kb\); their ideal contains its identity \(z_k\). This proves the reverse inequality and the criterion.

## Once reflection fills a level, it keeps doing so

**Theorem 12.5.** If \(z_k=1\), then \(z_j=1\) for every \(j\geq k\).

**Proof.** The relation \(A_{k+1}=I_k\) expresses its identity as a finite sum of elements \(a e_kb\), with \(a,b\in A_k\). The same expression shows that \(e_k\) has full central support in \(A_{k+2}\). Inside that latter algebra,

\[
v=\lambda^{-1/2}e_{k+1}e_k
\]

is a partial isometry with \(v^*v=e_k\) and \(vv^*=e_{k+1}\), by the adjacent Jones relations. Equivalent projections have equal central support. Thus \(e_{k+1}\) has full central support in \(A_{k+2}\), so \(z_{k+1}=1\). Induction proves the assertion. \(\square\)

The inclusion has **finite depth** if such a \(k\) exists. We use the convention

\[
\begin{gathered}
\operatorname{depth}(N\subseteq M)\\
=\min\{k+1:z_k=1\}.
\end{gathered}
\tag{12.7}
\]

Otherwise the depth is infinite. With this convention the identity inclusion has depth one.

The **principal graph** is the rooted bipartite graph obtained from the tower of inclusion diagrams by keeping the initial root \(A_{-1}=\mathbb C\), introducing a new vertex for each matrix summand in a new part, and identifying the old summands by the basic-construction bijection in (12.6). Edges have the inclusion multiplicities. The transpose rule means that the old edges are reproduced in reverse at the next step, rather than introducing new edges or vertices.

There is a useful further restriction on the new edges. For \(k\geq1\), the projections \(e_{k-1}\) and \(e_k\) are equivalent in \(A_{k+1}\). Thus \(1-z_k\) annihilates both, and consequently annihilates the old ideal \(A_{k-1}e_{k-1}A_{k-1}\) in \(A_k\). A new block of \(A_{k+1}\) can receive edges only from the new blocks of \(A_k\). It cannot introduce an extra edge from an older vertex. This proves, inductively, that a newly introduced vertex has distance \(k+2\) from the root. The level-\(k\) summands therefore correspond to the graph vertices reachable from the root in \(k+1\) steps, and their block sizes are the numbers of such walks. The initial embedding of scalars gives the starting edge multiplicities; counting extensions gives the induction step.

Every new vertex is connected to an earlier one, because the inclusions are unital. The graph is therefore connected. Theorem 12.5 shows that finite depth is equivalent to the appearance of only finitely many vertices. In that case, after all vertices are reached, the inclusion matrices alternate between the two orientations of the full bipartite adjacency matrix. The **dual principal graph** is obtained in the same way from \(M\subseteq M_1\), whose relative-commutant tower is \(B_0\subseteq B_1\subseteq\cdots\).

## The graph norm measures the index at finite depth

**Theorem 12.6.** If the principal graph is finite, its adjacency operator has norm \(\sqrt d\). For arbitrary depth its norm is at most \(\sqrt d\).

**Proof.** Let \(s,t\) be the positive minimal-projection trace vectors on \(A_{k-1},A_k\). Then \(s=D_kt\). In the old blocks of \(A_{k+1}\), the minimal-projection weights are \(u=\lambda s\). Indeed, the rank of \(e_k\) in each old block equals the corresponding block size of \(A_{k-1}\), and

\[
\tau(ae_k)=\lambda\tau(a)\quad(a\in A_{k-1})
\]

forces these weights exactly as in Theorem 8.4. Restricting the trace of all blocks of \(A_{k+1}\) back to \(A_k\), the old contribution is \(D_k^{\mathsf T}u\) and the new contribution is nonnegative. Consequently

\[
\lambda D_k^{\mathsf T}D_kt\leq t.
\tag{12.8}
\]

Here the bound can be proved directly from the displayed positive trace vector. Put \(H=D_k^{\mathsf T}D_k\). Its entries are nonnegative and \(Ht\leq dt\). For any vector \(x\), the elementary inequality

\[
2|x_i||x_j|\leq
\frac{t_j}{t_i}|x_i|^2+
\frac{t_i}{t_j}|x_j|^2
\]

and symmetry of \(H\) give

\[
\begin{aligned}
\langle Hx,x\rangle
&\leq\sum_{i,j}H_{ij}|x_i||x_j|\\
&\leq\sum_i\frac{(Ht)_i}{t_i}|x_i|^2\\
&\leq d\|x\|^2.
\end{aligned}
\]

Since \(H\) is positive semidefinite, \(\|D_k\|^2=\|H\|\leq d\). This estimate does not require an eigenvector theorem or connectedness.

Any finite-support vector on the principal graph is supported in the vertices and edges of a sufficiently late inclusion diagram: once a vertex has appeared, the transpose rule preserves it at all subsequent levels of the same parity. The bound for those matrices therefore gives the bound for the graph adjacency operator, whose norm is the supremum of its finite-support Rayleigh quotients in absolute value.

At finite depth, choose a level with \(z_k=1\), late enough that all graph vertices have appeared. There is no new contribution, so (12.8) is equality. The matrix \(D_k\) is the full bipartite adjacency matrix, up to orientation. The equality \(D_k^{\mathsf T}D_kt=dt\) exhibits the nonzero finite vector \(t\) as an eigenvector. Combined with the preceding upper bound, it gives \(\|D_k\|^2=d\). The adjacency operator of a bipartite graph is \(\begin{pmatrix}0&D_k\\D_k^{\mathsf T}&0\end{pmatrix}\), whose norm is \(\|D_k\|\). \(\square\)

The general inequality cannot be silently promoted to equality without additional hypotheses. Finite depth gives the equality needed here.

## Index below four forces finite depth

**Theorem 12.7.** If \(d=4\cos^2(\pi/r)<4\), where \(r\geq3\), then

\[
\operatorname{depth}(N\subseteq M)\leq r-2.
\tag{12.9}
\]

**Proof.** The Jones–Wenzl projection \(f_{r-1}\) for the first \(r-2\) Jones projections \(e_0,\ldots,e_{r-3}\) has trace zero and is zero, by Theorem 7.2 and faithfulness. This projection is the largest projection annihilated by all those generators. To check maximality, induct through its recursion: any projection annihilating the preceding generators lies below \(f_n\); if it also annihilates the next generator, multiplication by the next recursion leaves it unchanged, so it lies below \(f_{n+1}\). The recursion itself annihilates each generator, giving equality with the joint-kernel projection.

Hence

\[
e_0\vee e_1\vee\cdots\vee e_{r-3}=1
\quad\text{in }A_{r-2}.
\]

Adjacent Jones projections are equivalent by the partial isometry used in Theorem 12.5. All these partial isometries lie in \(A_{r-2}\). Thus the listed projections have the same central support there; their join being one forces that support to be one. In particular \(e_{r-3}\) has full central support in \(A_{r-2}\). Definition (12.7) gives depth at most \(r-2\). For \(r=3\), the single projection is \(e_0=1\), giving depth one. \(\square\)

Finite depth controls this finite-dimensional structure. Reconstructing a hyperfinite inclusion from the full ladder requires a generating tunnel; graph norm and block multiplicities alone do not prove that classification theorem.

## The trace gives a positive function on the whole graph

The finite trace vectors also fit into one function on the principal graph. This keeps track of the root, the parity, the block sizes and the minimal-projection weights at every level.

Write \(a(v,w)\) for the number of edges between vertices \(v,w\), and let \(\Omega_q\) be the endpoints of length-\(q\) walks from the root \(*\), counting parallel edges separately. Level \(q\) means \(A_{q-1}\); in particular level zero is \(A_{-1}=\mathbb C\). Let \(k_q(v)\) be the block size and \(w_q(v)\) the trace of a minimal projection in that block. Put \(\delta=\sqrt d\).

**Proposition 12.8.** The principal graph is locally finite. There is a positive function \(\mu\) on its vertices such that

\[
\begin{gathered}
\mu(*)=1,\\
\sum_w a(v,w)\mu(w)=\delta\mu(v),\\
w_q(v)=\delta^{-q}\mu(v)
\quad(v\in\Omega_q).
\end{gathered}
\tag{12.10}
\]

For every \(q\geq1\),

\[
\begin{gathered}
k_q(v)=\sum_w a(v,w)k_{q-1}(w),\\
k_0(*)=1,\\
k_0(v)=0\quad(v\ne*),\\
\sum_{v\in\Omega_q}k_q(v)\mu(v)=\delta^q.
\end{gathered}
\tag{12.11}
\]

An absent block contributes zero to the count recurrence. The adjacency eigenfunction in (12.10) is a pointwise statement; it does not assert that \(\mu\) belongs to \(\ell^2\) when the graph is infinite.

**Proof.** The reflection and new-edge arguments after Theorem 12.5 identify the inclusion matrix at consecutive levels with \(a(v,w)\) on \(\Omega_q\times\Omega_{q+1}\). A newly introduced vertex can acquire new neighbors only at its introduction and the next level: later new blocks receive edges only from the immediately preceding new blocks. Both of these finite algebras have finitely many blocks and finite multiplicities. Every vertex therefore has finitely many neighbors, and all sums in (12.10) are finite.

A minimal projection \(p\) in the block at \(v\in\Omega_q\) lies in \(A_{q-1}\). In the reflected ideal at level \(q+2\), the projection \(pe_q\) is minimal in the corresponding block, by Theorem 8.6 and Theorem 12.4. The Markov identity consequently gives

\[
\begin{aligned}
w_{q+2}(v)&=\tau(pe_q)\\
&=\lambda\tau(p)\\
&=\delta^{-2}w_q(v).
\end{aligned}
\tag{12.12}
\]

If \(b(v)\) is the distance of \(v\) from the root, define
\(\mu(v)=\delta^{b(v)}w_{b(v)}(v)\).
The trace is faithful, so this number is positive. Every level at which \(v\) occurs has the form \(b(v)+2j\), and repeated reflection (12.12) gives the last formula of (12.10). The initial scalar trace gives \(\mu(*)=1\).

Trace restriction across an inclusion gives

\[
w_q(v)=\sum_w a(v,w)w_{q+1}(w).
\]

Every neighbor of a reachable \(v\) is reachable one step later. Insert the weight formula and multiply by \(\delta^{q+1}\) to obtain the pointwise eigenfunction equation. Each vertex is reachable at its distance level, so this proves it on the whole graph.

Finally a path ending at \(v\) is a shorter path followed by one of the \(a(v,w)\) edges from a neighbor \(w\). This proves the count recurrence and its initial conditions. Trace normalization is \(\sum_v k_q(v)w_q(v)=1\); substitution gives the last equation in (12.11). \(\square\)

These coordinates give another direct proof of the graph-norm bound. For a finitely supported function \(f\), weighted Cauchy–Schwarz gives

\[
\begin{gathered}
|(Tf)(v)|^2\leq\delta\mu(v)\\
\quad\cdot\sum_w a(v,w)\frac{|f(w)|^2}{\mu(w)},\\
\sum_v|(Tf)(v)|^2\\
\leq\delta^2\sum_w|f(w)|^2.
\end{gathered}
\tag{12.13}
\]

The second inequality uses symmetry of \(a\) and \(\sum_v a(v,w)\mu(v)=\delta\mu(w)\). Thus adjacency extends to a bounded operator of norm at most \(\delta\). On a finite graph, \(\mu\) is a nonzero square-summable eigenvector, so equality holds. On an infinite graph that last step requires square summability and cannot be inferred from the pointwise equation alone. The actual index-nine tree inclusion in [A finite-index inclusion with no generating tunnel](nongenerating-tunnels-and-boundary.md) has \(\mu=1\), while its graph norm is \(2\sqrt2<3\).

## The support criterion uses the projection inside the triple

**Example 12.9.** Let \(Q\) be a II₁ factor and \(m\geq2\). For the actual inclusion

\[
N=1\otimes Q\subset M=M_m(\mathbb C)\bar\otimes Q,
\]

the index is \(m^2\), and

\[
\begin{gathered}
A_{-1}=\mathbb C,\qquad A_0=M_m,\\
A_1=B(L^2(M_m))\cong M_{m^2}.
\end{gathered}
\tag{12.14}
\]

This triple is the full basic construction and has depth one. Nevertheless

\[
\bigvee_{u\in\mathcal U(A_0)}ue_1u^*
=e_1\ne1.
\tag{12.15}
\]

**Proof.** As a left \(N\)-module, \(L^2(M)\) is the sum of \(m^2\) standard \(Q\)-modules, giving the index. The right \(N\)-commutant is
\(B(L^2(M_m))\bar\otimes Q\), so this is \(M_1\). Intersecting with the left \(N\)-commutant removes the \(Q\) factor and gives (12.14). In these coordinates \(e_0\) is the rank-one projection onto the trace vector \(1\in L^2(M_m)\), tensored with \(1_Q\). Left multiplication by \(A_0=M_m\) and that projection generates all rank-one operators, hence the full \(A_1\).

The ranges of \(ue_0u^*\), for matrix unitaries \(u\), span \(L^2(M_m)\), because the unitaries linearly span \(M_m\). Their join is one, giving the correct support criterion and depth one. In contrast, \(e_1\) is the Jones projection for \(M\subset M_1\). It commutes with \(M\), hence with \(A_0\), so every conjugate in (12.15) equals \(e_1\). Its trace is \(m^{-2}<1\), and faithfulness shows \(e_1\ne1\). \(\square\)

This example pinpoints the indexing in Takesaki's Corollary XIX.4.6. For \(A_{k-1}\subset A_k\subset A_{k+1}\), the criterion is the join of the \(A_k\)-conjugates of \(e_k\), as proved after Theorem 12.4. The printed \(e_{k+1}\) instead commutes with \(A_k\), so the literal criterion fails in Example 12.9. The proof of Lemma XIX.4.5 uses the same shifted symbol when taking central support in \(A_{k+1}\); the projection there is \(e_k\). Its reflected diagram is the transpose of \(A_{k-1}\subset A_k\), as stated in that lemma and proved in (12.6), rather than the repeated next inclusion in its final proof sentence. These are corrections of the specified coordinates, not a failure of the reflection theorem.

The same level convention fixes the parenthetical membership in Takesaki's equation XIX.(4.6). The correct statement is

\[
e_k\in B_{k+1}\quad(k\geq1).
\tag{12.16}
\]

Indeed \(e_k\in M_{k+1}\) commutes with \(M_{k-1}\supseteq M\). At nontrivial index \(d>1\), it cannot lie in \(M_k\): the normalized expectation gives \(E_{M_k}(e_k)=\lambda1\), whereas membership would give \(E_{M_k}(e_k)=e_k\). The scalar \(0<\lambda<1\) is not a projection. Thus the printed membership in \(B_k\subseteq M_k\) is false at nontrivial index; (12.16) supplies its precise replacement. The identity inclusion has all \(e_k=1\) and is the exceptional scalar case.

The depth bound in Corollary XIX.4.9 agrees with (12.9) on writing \(r=n+1\). Our proof uses the first \(r-2\) projections \(e_0,\ldots,e_{r-3}\) inside \(A_{r-2}\). This places the full-support conclusion at the level required by the stated depth bound.

## Exercises

**Exercise 12.1 — introductory.** For the identity inclusion \(N=M\), compute \(A_k\), its principal graph, depth and graph norm.

**Solution.** Every basic construction remains \(M\), every Jones projection is one, and every \(A_k\) is scalar. The principal graph has two vertices joined by one edge. The depth is one and the adjacency norm is one, agreeing with index one.

**Exercise 12.2 — intermediate.** Suppose \(N'\cap M=\mathbb C\) and \(d>1\). Show that the depth cannot be one.

**Solution.** Here \(A_0=\mathbb C\), so \(A_0e_0A_0=\mathbb Ce_0\). But \(\tau(e_0)=d^{-1}<1\), so its identity is not the identity of \(A_1\), which contains both \(1\) and \(e_0\). Thus \(z_0\ne1\), and the depth is at least two.

**Exercise 12.3 — intermediate.** Prove that a vertex of a principal graph with norm below two has degree at most three, counting edge multiplicities appropriately.

**Solution.** If the multiplicities of edges from a vertex are \(m_1,\ldots,m_s\), the squared norm of the adjacency operator applied to the unit vector at that vertex is \(\sum_jm_j^2\). It is less than four. Hence \(\sum_jm_j^2\leq3\). Every retained edge therefore has multiplicity one, and there are at most three incident edges. This local condition is necessary; it does not classify all such graphs.

**Exercise 12.4 — advanced.** If a finite principal graph has bipartite matrix \(D=(m)\), determine the index and the initial relative commutant's matrix size.

**Solution.** Its adjacency norm is \(m\), so Theorem 12.6 gives index \(m^2\). The initial scalar root embeds in the sole opposite-parity block with multiplicity \(m\), which means that block is \(M_m\). Thus \(A_0=M_m\). There are no new vertices after this first one, so the graph has depth one. For \(m>1\) this is a reducible inclusion, consistent with Exercise 12.2.

**Exercise 12.5 — intermediate.** For the depth-one inclusion of Example 12.9, compute the positive graph function, every block size and every minimal-projection weight. Verify normalization at all levels.

**Solution.** The graph has two vertices joined by \(m\) parallel edges. Its adjacency matrix is \(\begin{pmatrix}0&m\\m&0\end{pmatrix}\), and \(\delta=m\). The root value is one; the root equation forces the other value to be one as well. There is a single endpoint at each parity, and each step has \(m\) choices. Thus

\[
k_q=m^q,\qquad w_q=m^{-q},\qquad k_qw_q=1.
\]

Equivalently \(A_{q-1}=M_{m^q}\) for every \(q\geq0\), with the scalar algebra at \(q=0\). In particular \(A_0=M_m\) and \(A_1=M_{m^2}\), consistent with (12.14). The inclusion matrix is \((m)\) at every step; it counts parallel edges, not distinct neighboring vertices.

**Exercise 12.6 — advanced.** In the actual index-nine example of Lesson 46, both principal graphs are the infinite tree of degree three. Use (12.10)–(12.11) to recover the minimal weights and the first two relative-commutant algebras. Explain why the positive graph function does not prove graph norm three.

**Solution.** Here \(\delta=3\), and the constant function \(\mu=1\) satisfies the eigenfunction equation at every vertex because each has three neighbors. The trace formula of Proposition 46.4 identifies it as the graph function coming from the inclusion. Thus every length-\(q\) path projection has weight \(3^{-q}\). There are \(3^q\) walks altogether, so the sum of block size times minimal weight is one.

At length one the three endpoints each have one path, giving \(A_0=\mathbb C^3\). At length two there are three returning paths at the root and one path to each of six new endpoints. Hence

\[
\begin{gathered}
A_1=M_3\oplus\mathbb C^6,\\
w_2(v)=1/9.
\end{gathered}
\]

and its total trace is \((3+6)/9=1\). The function \(\mu=1\) is not square summable on the infinite vertex set. It therefore supplies no eigenvector in the Hilbert space of the adjacency operator. Proposition 46.8 proves that operator's norm is \(2\sqrt2\), so its squared norm is eight while the inclusion index is nine.

## References

- Vaughan F. R. Jones, [*Index for subfactors*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0072/LOG_0007.pdf), Inventiones Mathematicae 72 (1983), 1–25.
- Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003, Chapter XIX.
- Sorin Popa, [*An axiomatization of the lattice of higher relative commutants of a subfactor*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0120/LOG_0042.pdf), Inventiones Mathematicae 120 (1995), 427–445.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026; expanded October 2026. Self-checked by the writing AI. Public domain (CC0).*

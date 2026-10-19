# The fundamental estimate

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The estimate turns a global statement about poles into an exact statement about every local Frobenius eigenvalue. Three ingredients do different jobs. Rational local characteristic polynomials make even powers of traces nonnegative. Large geometric symplectic monodromy determines the top compact-support cohomology of tensor powers. The trace formula then places the global poles on a known circle. Comparing convergence radii and taking arbitrarily high tensor powers removes the error in the exponent.

We prove the estimate and both cohomological corollaries. We prove the symplectic tensor-invariant theorem before computing the top cohomology; finite-coefficient curve duality supplies the input for the adic and middle-extension pairings proved here. For the elliptic example we prove open monodromy directly from the Tate calculations of Lesson 8. Neither the estimate under its stated hypotheses nor that example requires a Picard–Lefschetz theorem.

## 1. Weights and the exact hypotheses

Fix \(q=p^a\), \(\ell\ne p\), and a nonempty open
\(U_0\subset\mathbf P^1_{\mathbf F_q}\). Put
\(U=U_0\times_{\mathbf F_q}\overline{\mathbf F}_q\). For a closed point \(x\), write
\(d_x=[\kappa(x):\mathbf F_q]\) and \(q_x=q^{d_x}\). The operators \(F_x\) and \(F\) are geometric Frobenius, with the conventions of Lessons 3 and 8. In particular \(F_x\) acts on \(\mathbf Q_\ell(r)\) by \(q_x^{-r}\).

A lisse \(\mathbf Q_\ell\)-sheaf \(\mathcal F_0\) is **pure of weight \(\beta\)** if every eigenvalue of every \(F_x\) is algebraic over \(\mathbf Q\), and every complex conjugate has absolute value \(q_x^{\beta/2}\). Algebraic means algebraic over \(\mathbf Q\), not merely over \(\mathbf Q_\ell\). We speak of complex absolute values after embedding a number field containing the eigenvalues into \(\mathbf C\). Purity requires the assertion for every such embedding.

The Tate sheaf \(\mathbf Q_\ell(r)\) is pure of weight \(-2r\). Tensor products of pure sheaves have weights equal to the sum of their weights, and a dual has the negative weight: the eigenvalues are products and inverses respectively. These facts use the same embedding on all algebraic factors. They do not require semisimplicity.

**Theorem 1.1 (Deligne's fundamental estimate).** Suppose that \(\beta\in\mathbf Z\) and:

1. There is a nondegenerate alternating pairing of sheaves on \(U_0\),
   \[
   \psi:\mathcal F_0\otimes\mathcal F_0\longrightarrow
   \mathbf Q_\ell(-\beta).
   \tag{1.1}
   \]
2. For a geometric base point \(u\), the image of the **geometric** group
   \(\pi_1(U,u)\) is open in
   \(\operatorname{Sp}(\mathcal F_u,\psi)(\mathbf Q_\ell)\).
3. For every \(x\in|U_0|\),
   \[
   \det(1-F_xT\mid\mathcal F_{0,x})\in\mathbf Q[T].
   \tag{1.2}
   \]

Then \(\mathcal F_0\) is pure of weight \(\beta\).

This is Deligne, *Weil I*, Theorem (3.2), printed p.284. The pairing is defined over \(U_0\), so arithmetic Frobenius acts on its target by \(q^\beta\). Geometric monodromy fixes that target and lies in a symplectic group. Using the arithmetic group in condition 2 would generally give symplectic similitudes, and would change the hypothesis.

Rank zero is harmless and the conclusion is vacuous. To prove the theorem point by point, we may assume \(U_0\) affine. If necessary, remove a closed point different from the particular \(x\) being tested. Restriction preserves (1.1) and (1.2), and the map of geometric fundamental groups from this smaller open is surjective: a connected finite étale cover of the original smooth connected curve stays connected upon restricting to a dense open. Hence condition 2 is preserved. We now work on an affine open.

## 2. Rationality and even tensor powers

Let \(\alpha_{x,1},\ldots,\alpha_{x,r}\) be the eigenvalues of \(F_x\), with multiplicity. Condition (1.2) makes them algebraic over \(\mathbf Q\). Newton's identities give
\[
a_{x,m}:=\operatorname{Tr}(F_x^m\mid\mathcal F_{0,x})
=\sum_j\alpha_{x,j}^m\in\mathbf Q
\quad(m\ge1).
\tag{2.1}
\]
This implication holds even when the operator is not diagonalizable: an upper-triangular form computes both characteristic polynomial and traces of powers.

Rationality of the characteristic polynomial does not, in general, mean that the operator has a rational matrix in some basis. For example, let \(a=\sqrt2\) in \(K=\mathbf Q(\sqrt2)\) and take
\[
A=\begin{pmatrix}a&1\\0&a\end{pmatrix}\oplus(-a)\oplus(-a).
\]
Its characteristic polynomial is \((T^2-2)^2\), but its minimal polynomial is \((T-a)^2(T+a)\), which does not belong to \(\mathbf Q[T]\). A rational matrix has a rational minimal polynomial: Gaussian elimination on the rational linear relations between \(1,A,A^2,\ldots\) computes it, and extension of the field does not change those ranks. Thus this operator has no rational matrix. Nevertheless all its power traces are rational, exactly as (2.1) asserts. The fundamental estimate uses rational characteristic polynomials and these traces; it requires no descent of Jordan blocks or semisimplicity assumption. This distinguishes the necessary hypothesis from the stronger formulation in Milne, Lemma 30.2.

For \(k\ge1\), put \(\mathcal T_k=\mathcal F_0^{\otimes2k}\). Tensor-product traces multiply, so
\[
\operatorname{Tr}(F_x^m\mid\mathcal T_{k,x})=a_{x,m}^{\,2k}\ge0.
\tag{2.2}
\]
Here “nonnegative” includes zero. There is no assertion that every trace is nonzero. The tensor-power characteristic polynomial is also rational: its roots are all products of \(2k\) roots of the original rational polynomial, and their multiset is invariant under every automorphism of \(\overline{\mathbf Q}/\mathbf Q\).

Define the local factor in the global variable \(t\) by
\[
f_{x,k}(t)=
\det(1-F_xt^{d_x}\mid\mathcal T_{k,x})^{-1}.
\tag{2.3}
\]
The characteristic-zero formal logarithm gives
\[
\log f_{x,k}(t)=
\sum_{m\ge1}\frac{a_{x,m}^{\,2k}}m\,t^{md_x}.
\tag{2.4}
\]
Thus both its logarithm and its logarithmic derivative have nonnegative rational coefficients. Exponentiating proves the same for \(f_{x,k}\), whose constant term is \(1\). More explicitly, if \(\log f=\sum_{n\ge1}b_nt^n\) and \(f=\sum_{n\ge0}c_nt^n\), then
\[
c_0=1,\qquad
nc_n=\sum_{j=1}^n j b_jc_{n-j};
\tag{2.5}
\]
induction gives \(c_n\ge0\).

There are finitely many closed points of bounded degree, so
\[
L_k(t)=L(U_0,\mathcal T_k,t)=\prod_{x\in|U_0|}f_{x,k}(t)
\tag{2.6}
\]
is a well-defined formal power series with nonnegative rational coefficients. No convergence claim has yet been used. Equations (2.2)–(2.6) are the precise squaring step: a rational trace can have either sign, but its even power cannot. Squaring the eigenvalues individually would not make each of them a nonnegative real number.

## 3. The convergence comparison

**Lemma 3.1 (Deligne's form of Landau's argument).** Let \(f_i\in1+t\mathbf R[[t]]\) have nonnegative coefficients. Suppose that \(\operatorname{ord}_t(f_i-1)\to\infty\), allowing \(f_i=1\). The product \(f=\prod_i f_i\) exists formally. Every factor has radius of absolute convergence at least that of \(f\).

**Proof.** In a given degree, only finitely many nonconstant factors contribute. Write \(f_i=\sum_n c_{i,n}t^n\) and \(f=\sum_n c_nt^n\). Selecting the degree-\(n\) term from factor \(i\) and the constant terms from all other factors proves
\[
0\le c_{i,n}\le c_n.
\tag{3.1}
\]
If \(\sum_n c_nR^n\) converges for a positive \(R\), coefficient domination proves that \(\sum_n c_{i,n}R^n\) converges. Apply this at every \(R\) strictly below the radius of \(f\). The assertion also covers radius zero or infinity. \(\square\)

**Lemma 3.2.** If \(f\) and each \(f_i\) are Taylor expansions of rational functions regular at zero, then
\[
\inf\{|z|:z\text{ is a pole of }f\}
\ \le\
\inf\{|z|:z\text{ is a pole of }f_i\}.
\tag{3.2}
\]
The infimum of the empty set is infinity.

**Proof.** After cancelling common numerator and denominator factors, a rational function is holomorphic on the open disc ending at its nearest pole. Its Taylor series converges there. It cannot have a larger radius, since that would define a holomorphic continuation at a genuine pole. Hence its radius is precisely the displayed infimum. Lemma 3.1 proves (3.2). Cancellation in the global rational function can remove poles; it cannot create nearer ones. \(\square\)

These are Deligne's Lemmas (3.5)–(3.6), printed p.284. They apply also to meromorphic functions on the whole plane, with the same nearest-pole reasoning.

For comparison, the usual positive-series singularity statement has a short proof. If \(f(t)=\sum c_nt^n\), \(c_n\ge0\), has finite positive radius \(R\), suppose it were analytic near the positive real point \(R\). For every \(m\), differentiation inside the disc, passage to \(t\uparrow R\), and monotone convergence give
\[
\frac{f^{(m)}(R)}{m!}
=\sum_{n\ge m}\binom nm c_nR^{n-m}.
\]
For small \(s>0\), the Taylor expansion at \(R\) converges at \(R+s\). All the terms in the double sum are nonnegative, so exchanging the sums gives
\[
\sum_m\frac{f^{(m)}(R)}{m!}s^m
=\sum_n c_n(R+s)^n<\infty,
\]
contradicting the radius \(R\). Thus \(R\) is a singularity; for a rational function it is a pole. The proof of Theorem 1.1 needs only Lemmas 3.1–3.2, because all possible global poles already have a known modulus.

## 4. Symplectic coinvariants and their Frobenius action

Put \(V=\mathcal F_u\). Over the geometric field, choose a basis of the constant Tate line to view \(\psi\) as scalar-valued. We first justify that an open subgroup of \(\operatorname{Sp}(V,\psi)(\mathbf Q_\ell)\) is Zariski dense, including \(\ell=2\).

Write \(J\) for the pairing matrix. On the open set where the denominators are invertible, the Cayley maps
\[
A\longmapsto(1-A)^{-1}(1+A),\qquad
g\longmapsto(g-1)(g+1)^{-1}
\]
are inverse maps between \(A^{\mathsf t}J+JA=0\) and the symplectic group. Substitution proves the pairing identity; the inverse follows by multiplying the commuting factors \(1\pm A\). They give a chart around zero and the identity over \(\mathbf Q_\ell\). At \(\ell=2\), shrink the ball so that both denominators remain invertible; no assertion about an integral chart is needed.

The symplectic group is irreducible over an algebraic closure. Here is a proof of this fact used in the density argument. Its points are ordered symplectic bases. The possible first pairs \((v,w)\), with \(\psi(v,w)=1\), form an affine bundle with fibre \(\mathbf A^{2n-1}\) over \(V-\{0\}\); it is irreducible. Their orthogonal complements form a symplectic vector bundle of rank \(2n-2\). Alternating pivot elimination supplies symplectic frames on Zariski open neighbourhoods, so the choices of the remaining basis vectors form a locally trivial bundle with fibre \(\operatorname{Sp}_{2n-2}\). Induction from rank zero proves irreducibility of the total space: the base opens and their intersections are irreducible, and each inverse image is a product of irreducible varieties.

A polynomial vanishing on an open subgroup pulls back through the Cayley chart to a rational function vanishing on a small ball in the symplectic Lie algebra. Clear its denominators. A polynomial on affine space vanishing on a product of infinite balls is zero, by induction on the variables and the one-variable root bound. It therefore vanishes on the whole Cayley open and, by irreducibility, on the whole symplectic group. This proves density without a geometric monodromy theorem.

For a representation \(W\), let \(W_G\) denote its largest quotient with trivial \(G\)-action. Its dual is \((W^\vee)^G\). The condition that a linear form be invariant is a closed polynomial condition on the acting group; Zariski density therefore identifies geometric-monodromy invariants, and hence coinvariants, with those of the whole symplectic group.

### Tensor invariants and pair contractions

We first prove the algebraic statement that makes the monodromy calculation possible. The reduction from a classical group to the general linear group has a geometric treatment in [Deligne, Lehrer and Zhang, *The first fundamental theorem of invariant theory for the orthosymplectic super group*](https://publications.ias.edu/sites/default/files/2015-06-ortho.pdf). Here we give the ordinary symplectic argument over an arbitrary characteristic-zero field.

**Lemma 4.1 (general linear tensor invariants).** Let \(W\) be a finite-dimensional vector space over a field \(K\) of characteristic zero. For every \(r\geq0\), every endomorphism of \(W^{\otimes r}\) commuting with the algebraic group \(\operatorname{GL}(W)\) is a linear combination of permutations of the \(r\) tensor factors.

**Proof.** The case \(r=0\) is immediate. We can extend scalars to an algebraic closure: invariance is the kernel of linear equations obtained by comparing polynomial matrix coefficients, and the span of the permutation operators also commutes with scalar extension. A spanning assertion over the algebraic closure therefore descends to \(K\).

Write \(E=\operatorname{End}(W)\) and \(T=W^{\otimes r}\). Under the canonical identification
\[
\operatorname{End}(T)=E^{\otimes r},
\]
conjugation by a permutation operator permutes the factors of \(E^{\otimes r}\). The centralizer of the permutation operators is consequently the symmetric subspace of this tensor power. That subspace is spanned by tensors \(a^{\otimes r}\). Indeed, polarization gives
\[
\sum_{S\subseteq\{1,\ldots,r\}}(-1)^{r-|S|}
\left(\sum_{i\in S}a_i\right)^{\otimes r}
=\sum_{\sigma\in S_r}a_{\sigma(1)}\otimes\cdots\otimes a_{\sigma(r)}.
\]
The symmetrized elementary tensors span the symmetric subspace, because division by \(r!\) is possible. We may restrict \(a\) to invertible matrices: any linear functional vanishing on their tensor powers gives a polynomial in the matrix entries vanishing on the dense open set \(\det(a)\ne0\), hence vanishing everywhere.

It follows that, if \(B\) is the algebra generated by the permutation operators, its centralizer \(B'\) is the linear span of \(g^{\otimes r}\), \(g\in\operatorname{GL}(W)\).

For completeness, the double-centralizer assertion used next follows from elementary semisimple-module theory. Averaging a projection over the finite group \(S_r\) makes every invariant subspace have an invariant complement. Thus \(T\) is a direct sum of simple \(K[S_r]\)-modules. Over the algebraic closure, write it as
\[
T=\bigoplus_\alpha S_\alpha\otimes M_\alpha
\]
with the \(S_\alpha\) pairwise nonisomorphic. Schur's lemma gives \(\operatorname{End}_{S_r}(S_\alpha)=K\): a commuting endomorphism has an eigenvalue, and its corresponding eigenspace is an invariant nonzero subspace. Consequently
\[
B'=\bigoplus_\alpha
1_{S_\alpha}\otimes\operatorname{End}(M_\alpha).
\]
The image of the group algebra acts as the full matrix algebra on each \(S_\alpha\), independently for different \(\alpha\). Here is a direct justification. Choose a basis in each \(S_\alpha\), and form the vector whose components list all these basis vectors in
\(\bigoplus_\alpha S_\alpha^{\oplus\dim S_\alpha}\). If the cyclic submodule generated by that vector were proper, semisimplicity would give a nonzero map from its quotient to one of the simple modules. Such a map is a scalar linear combination of the components belonging to that same simple module, by Schur's lemma. Evaluating the resulting relation at the identity of the group algebra contradicts linear independence of its chosen basis. The cyclic submodule is therefore the whole direct sum, which is precisely simultaneous surjectivity onto the matrix blocks.

Hence
\[
B=\bigoplus_\alpha
\operatorname{End}(S_\alpha)\otimes1_{M_\alpha}=B''.
\]
An operator commuting with all \(g^{\otimes r}\) lies in \(B''\), so lies in \(B\). This proves the lemma, with no restriction comparing \(r\) and \(\dim W\). \(\square\)

**Theorem 4.2 (symplectic tensor invariants).** Let \(V\) carry a nondegenerate alternating form \(\psi\) over a characteristic-zero field \(K\). Invariant linear forms on \(V^{\otimes 2k}\) are spanned by
\[
\psi_P(v_1\otimes\cdots\otimes v_{2k})
=\prod_{\{i,j\}\in P,\ i<j}\psi(v_i,v_j),
\tag{4.1}
\]
where \(P\) runs through pair partitions of \(\{1,\ldots,2k\}\). In odd tensor degree there are no invariants. The spanning assertion holds in every dimension and every tensor degree; it does not assert that the displayed generators are independent.

**Proof.** Degree zero is \(K\); if \(V=0\), all positive-degree tensor spaces are zero. Suppose \(\dim V=2n>0\). As in the lemma, the assertion descends from an algebraic closure, so we work over an algebraically closed field.

Put \(W=V^\vee\). The form \(\psi\), viewed as an antisymmetric tensor, is
\[
\Omega=\sum_{i=1}^n(e_i\otimes f_i-f_i\otimes e_i)
\]
in a suitable basis of \(W\). The action on \(W\) identifies \(\operatorname{Sp}(V,\psi)\) with the stabilizer of \(\Omega\) in \(\operatorname{GL}(W)\). A linear form on \(V^{\otimes m}\) is an element of \(W^{\otimes m}\). Odd-degree invariants vanish because \(-1\) belongs to the group. Take \(m=2k\), and let \(v\in W^{\otimes m}\) be invariant.

Consider the affine space \(\Lambda^2W\) of alternating bivectors, using the injection
\[
x\wedge y\longmapsto x\otimes y-y\otimes x.
\]
Its nondegenerate open subset is the orbit of
\(B_0=\sum_i e_i\wedge f_i\). Let
\(\tau=e_1\wedge f_1\wedge\cdots\wedge e_n\wedge f_n\).
Define the Pfaffian by
\[
\frac{B^{\wedge n}}{n!}=\operatorname{Pf}(B)\tau.
\]
Thus \(\operatorname{Pf}(B_0)=1\) and
\(\operatorname{Pf}(gB)=\det(g)\operatorname{Pf}(B)\).

For \(B=gB_0\), set \(h(B)=g^{\otimes m}v\). This is independent of the choice of \(g\), because two choices differ by the stabilizer of \(B_0\). It is a regular map on the nondegenerate open subset. To see regularity explicitly, choose a nonzero pivot in the alternating matrix, split off its two-dimensional block, and repeat on the complementary block. The usual symplectic elimination uses only division by the chosen pivots. On the open sets where those pivots are invertible it supplies regular matrices \(g(B)\); their images \(g(B)^{\otimes m}v\) agree on overlaps. These open sets cover all nondegenerate alternating matrices.

The coordinate ring of that open subset is the polynomial ring in the alternating-matrix entries with the Pfaffian inverted. Therefore, for some integer \(s\geq0\),
\[
P(B)=\operatorname{Pf}(B)^s h(B)
\]
is a polynomial map on all of \(\Lambda^2W\). It satisfies
\[
P(gB)=\det(g)^s g^{\otimes m}P(B).
\]
Taking \(g=a\,1_W\) shows that \(P\) is homogeneous of degree
\(N=k+ns\): its degree-\(d\) part scales by \(a^{2d}\), whereas the right side scales by \(a^{m+2ns}\).

Polarization now gives an equivariant linear map
\[
p:\operatorname{Sym}^N(\Lambda^2W)
\longrightarrow
W^{\otimes m}\otimes(\Lambda^{2n}W)^{\otimes s},
\qquad
p(B_0^N)=v\otimes\tau^{\otimes s}.
\]
The determinant factors on the right are exactly those needed for the displayed equivariance.

Both sides are direct summands of \(W^{\otimes2N}\). For the source, antisymmetrize inside each consecutive pair and then average over permutations of the \(N\) pairs. These commuting idempotents have image \(\operatorname{Sym}^N(\Lambda^2W)\). For each determinant factor on the target, use the alternating projector on \(2n\) slots. Its normalized exterior embedding sends \(w_1\wedge\cdots\wedge w_{2n}\) to
\[
\frac{1}{(2n)!}\sum_\sigma
\operatorname{sgn}(\sigma)\,
w_{\sigma(1)}\otimes\cdots\otimes w_{\sigma(2n)}.
\]
Compose the source projection, \(p\), and the target embedding. This gives a \(\operatorname{GL}(W)\)-equivariant endomorphism of \(W^{\otimes2N}\). By Lemma 4.1 it is a linear combination of permutation operators. Evaluating it on \(\Omega^{\otimes N}\) therefore expresses the embedded tensor \(v\otimes\tau^{\otimes s}\) as a linear combination of permutations of \(\Omega^{\otimes N}\).

It remains to remove the determinant factors. Let \(\eta\) be the alternating form on \(W\) with
\(\eta(e_i,f_j)=\delta_{ij}\) and zero values on the pairs of \(e\)'s or pairs of \(f\)'s. The alternating functional
\[
\lambda(w_1,\ldots,w_{2n})
=\operatorname{Pf}\bigl(\eta(w_i,w_j)\bigr)
\]
is the volume functional taking \(\tau\) to \(1\). It also takes its normalized exterior embedding to \(1\), since antisymmetrization of an alternating functional leaves that functional unchanged. Expand the Pfaffian as its signed sum over pair partitions: \(\lambda\) is a sum of products of \(n\) pair contractions by \(\eta\).

Apply \(\lambda\) to each of the \(s\) determinant blocks. On the left this recovers \(v\). On the right we have finitely many contractions of permuted copies of \(\Omega\), with \(m\) uncontracted slots. Each summand has a graph consisting of alternating \(\Omega\)-edges and \(\eta\)-edges. Every internal vertex has degree two; each free slot is an endpoint. Hence each component is either a path between two free slots or a closed cycle.

In the chosen basis the two coefficient matrices are both
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}^{\oplus n},
\qquad J^2=-1.
\]
Successive contractions along a path therefore reduce to a copy of \(\Omega\), with a possible sign from its orientations. A cycle reduces to the trace of a signed identity, hence a signed scalar \(2n\). Thus every summand is a scalar multiple of a product of copies of \(\Omega\) pairing the free slots. This expresses \(v\) as a linear combination of the pair tensors. Under \(W^{\otimes2k}=\operatorname{Hom}(V^{\otimes2k},K)\), those tensors are exactly (4.1).

Finally, scalar extension does not create a failure of spanning: both the invariant space and the span of the \(K\)-defined pair tensors commute with extension, so the assertion descends to the original field. \(\square\)

### Frobenius on the coinvariants

The forms can have relations when \(\dim V\) is small. Choose a subset that is a basis of the invariant linear forms, of cardinality \(N_k\). Restoring the Tate target, these maps induce an isomorphism
\[
(V^{\otimes2k})_{\pi_1(U)}
\simeq \mathbf Q_\ell(-k\beta)^{N_k}.
\tag{4.2}
\]
Indeed the dual map is an isomorphism onto all invariant linear forms, and finite-dimensional duality gives the claim about the quotient.

Crucially, (4.2) also identifies arithmetic Frobenius. The maps \(\psi_P\) are built from the pairing (1.1) defined over \(U_0\). They are arithmetic-equivariant and take values in the *same fixed* Tate line for every \(P\). Therefore \(F\) acts on the quotient by the scalar \(q^{k\beta}\); it does not permute an arbitrarily chosen contraction basis.

**Lemma 4.3 (the adic passage in curve duality).** Let \(U\) be a smooth connected curve over an algebraically closed field of characteristic different from \(\ell\), and let \(L\) be a classical lisse \(\mathbf Q_\ell\)-sheaf. Cup product and the degree-normalized curve trace give perfect pairings
\[
H_c^i(U,L)\otimes H^{2-i}(U,L^\vee)
\longrightarrow\mathbf Q_\ell(-1).
\tag{4.3a}
\]
They are natural for extension by zero and restriction, and for automorphisms of the curve and its coefficients.

**Proof.** Choose a stable finite free \(\mathbf Z_\ell\)-lattice \(M\subset L\); compactness of the monodromy image gives one by Lesson 1. Put \(M_n=M/\ell^nM\). The finite-coefficient curve-duality theorem in *Poincaré duality for curves*, Theorem 11.1, gives the evaluation-and-trace isomorphism
\[
R\Gamma(U,M_n^\vee(1))
\simeq R\operatorname{Hom}_{\mathbf Z/\ell^n}
   (R\Gamma_c(U,M_n),\mathbf Z/\ell^n)[-2].
\tag{4.3b}
\]
Here \(M_n^\vee=\operatorname{Hom}(M_n,\mathbf Z/\ell^n)\), and finite freeness identifies it with the reduction of \(M^\vee\). This finite theorem applies to ramified local systems as well as constant ones; its local inertia calculation and its ordered evaluation pairing are part of that provider's proof.

Lesson 7, Theorem 5.1 and its proof of (5.3)–(5.5), show that the perfect complexes \(C_n=R\Gamma_c(U,M_n)\) are the compatible derived reductions of a bounded finite free \(\mathbf Z_\ell\)-complex \(C\). Its dual is also finite free, and
\[
C^\vee\otimes^{\mathbf L}\mathbf Z/\ell^n
=R\operatorname{Hom}_{\mathbf Z/\ell^n}(C_n,\mathbf Z/\ell^n).
\]
All maps in (4.3b) are defined by cup product and the trace sending a point class to \(+1\). Reduction of coefficients preserves this normalization and these maps. They therefore form compatible isomorphisms, including their homotopies, rather than unrelated isomorphisms at each level.

Taking their derived limit identifies
\(R\Gamma(U,M^\vee(1))\) with \(C^\vee[-2]\): derived global sections commute with these limits, and the finite-level cohomology groups are finite, so their towers are Mittag–Leffler. This is also the classical adic cohomology comparison of Lesson 2, (5.1). Tensoring the resulting finite free complexes with \(\mathbf Q_\ell\) gives a duality of bounded finite-dimensional complexes. Over a field dualization is exact; taking cohomology proves (4.3a) in every degree. Its maps retain the evaluation, trace and functorialities used at each finite level. \(\square\)

Lemma 4.3 and the degree-normalized trace now give
\[
H_c^0(U,\mathcal T_k)=0,\qquad
H_c^2(U,\mathcal T_k)
\simeq(V^{\otimes2k})_{\pi_1(U)}(-1)
\simeq\mathbf Q_\ell(-k\beta-1)^{N_k}.
\tag{4.3}
\]
The first assertion follows because a section of a lisse sheaf on a connected affine curve cannot have finite support. For the second, ordinary \(H^0\) is the invariant subspace; Poincaré duality exchanges it with the top compact-support coinvariant quotient and supplies the twist \((-1)\).

For example \(N_1=1\) when \(V\ne0\). If \(\dim V=2\) and \(k=2\), the three contractions satisfy
\[
\psi_{12}\psi_{34}-\psi_{13}\psi_{24}
+\psi_{14}\psi_{23}=0.
\tag{4.4}
\]
It is the vanishing of a fourfold exterior product on a two-dimensional space, or can be checked in a symplectic basis. The first two forms are independent: evaluate on \((e,e,f,f)\) and \((e,f,e,f)\), with \(\psi(e,f)=1\). Hence \(N_2=2\), not \(3\). Counting pair partitions without their relations would give a wrong pole order, although not a different pole modulus.

## 5. Proof of the fundamental estimate

Apply [Lesson 8](l-functions-rationality-and-the-functional-equation.md), Theorem 2.1, to (4.3). This is the characteristic-zero determinant formula, proved there from the trace identity. Its Theorem 2.2 supplies the stronger finite-coefficient determinant formula for every Noetherian coefficient ring killed by an integer prime to \(p\), with finite Tor amplitude; the present characteristic-zero argument does not infer that finite formula from power traces alone. We obtain
\[
L_k(t)=
\frac{P_k(t)}{(1-q^{k\beta+1}t)^{N_k}},\qquad
P_k(t)=\det(1-Ft\mid H_c^1(U,\mathcal T_k)).
\tag{5.1}
\]
The Euler product has rational coefficients by §2. Multiplying its formal expansion by the rational polynomial in the denominator shows that \(P_k\in\mathbf Q[t]\). Thus (5.1) is a rational function over \(\mathbf Q\), and we can regard it as a complex rational function without choosing an embedding for arbitrary \(\ell\)-adic coefficients.

Every possible pole of (5.1) is at \(q^{-(k\beta+1)}\). Cancellation can only enlarge its Taylor radius \(\rho_k\), so
\[
\rho_k\ge q^{-(k\beta+1)}.
\tag{5.2}
\]
The local factors (2.3) also are rational functions over \(\mathbf Q\), with nonnegative Taylor coefficients. Their nonconstant orders tend to infinity as \(d_x\to\infty\), and there are finitely many \(x\) of bounded degree. Lemma 3.1 therefore applies to their Euler product.

Fix an eigenvalue \(\alpha\) of \(F_x\), and fix any complex conjugate of it. The repeated product \(\alpha^{2k}\) is an eigenvalue of the tensor-power operator. Every solution of
\(t^{d_x}=\alpha^{-2k}\) is a genuine pole of (2.3), since its numerator is \(1\). Each has modulus
\(|\alpha|^{-2k/d_x}\). By (5.2) and the radius comparison,
\[
q^{-(k\beta+1)}
\le \rho_k
\le \operatorname{radius}(f_{x,k})
\le |\alpha|^{-2k/d_x}.
\]
Equivalently,
\[
|\alpha|^{2k}\le q_x^{k\beta+1},\qquad
|\alpha|\le q_x^{\beta/2+1/(2k)}.
\tag{5.3}
\]
Letting \(k\to\infty\) gives \( |\alpha|\le q_x^{\beta/2}\).

The pairing (1.1) says that \(F_x\) is a similitude of multiplier \(q_x^\beta\). In matrix form,
\(A^{\mathsf t}JA=q_x^\beta J\); hence \(A\) is similar to
\(q_x^\beta A^{-\mathsf t}\). Consequently \(q_x^\beta/\alpha\) is also an eigenvalue, with multiplicity. Apply the upper bound to this eigenvalue under the same complex embedding:
\[
\left|\frac{q_x^\beta}{\alpha}\right|
\le q_x^{\beta/2},\qquad
|\alpha|\ge q_x^{\beta/2}.
\tag{5.4}
\]
The two inequalities give equality. Condition (1.2) already supplied algebraicity, and every complex conjugate was allowed in the argument. This proves Theorem 1.1. \(\square\)

Only Zariski density was used in §4; the stated openness hypothesis implies it. This proof establishes a theorem about a sheaf satisfying the three explicit hypotheses. Applying it to the vanishing quotient of a higher-dimensional Lefschetz pencil additionally requires the algebraic Picard–Lefschetz and geometric monodromy inputs of Lesson 9. Such an application must verify those inputs; a calculation in a complex quadratic model alone does not supply them in arbitrary characteristic.

## 6. The two cohomological bounds

Return to the hypotheses of Theorem 1.1, with \(U_0\) affine. The standard symplectic representation \(V\ne0\) has no trivial quotient: its dual has no invariant vector, since a vector fixed by every symplectic transvection would be orthogonal to every vector. By density the same holds for geometric monodromy. Thus
\[
H_c^0(U,\mathcal F)=H_c^2(U,\mathcal F)=0,\qquad
L(U_0,\mathcal F_0,t)
=\det(1-Ft\mid H_c^1(U,\mathcal F)).
\tag{6.1}
\]
The rank-zero case again gives zero cohomology and no eigenvalues.

**Corollary 6.1 (Deligne (3.8)).** Every eigenvalue \(\gamma\) of \(F\) on \(H_c^1(U,\mathcal F)\) is algebraic over \(\mathbf Q\), and every complex conjugate satisfies
\[
|\gamma|\le q^{\beta/2+1}
=q^{(\beta+1)/2+1/2}.
\tag{6.2}
\]

**Proof.** The left side of (6.1) has rational formal coefficients by (1.2). Since the right side is a polynomial, it lies in \(\mathbf Q[t]\), proving algebraicity of its reciprocal roots.

By purity, every local eigenvalue has modulus \(q_x^{\beta/2}\). Let \(r=\operatorname{rank}\mathcal F\), and let \(M_d\) be the number of degree-\(d\) points of \(U_0\). The projective line has \(q^d+1\) rational points over \(\mathbf F_{q^d}\), so \(M_d\le q^d+1\). For \(q^{\beta/2}|t|<1\),
\[
\sum_{x,j}|\alpha_{x,j}t^{d_x}|
\le r\sum_{d\ge1}(q^d+1)
(q^{\beta/2}|t|)^d.
\tag{6.3}
\]
The right side converges when \(|t|<q^{-\beta/2-1}\). In that disc every local term has modulus less than \(1\), and the product of its reciprocal \(1-\alpha_{x,j}t^{d_x}\) factors converges locally uniformly to a nonzero holomorphic function. This follows also by expanding their logarithms; the convergent sum in (6.3) bounds the logarithmic series on any smaller disc. Therefore the polynomial in (6.1) has no zero in that disc. Its reciprocal roots satisfy (6.2), and all conjugates occur among those roots because its coefficients are rational. \(\square\)

Let \(j:U\hookrightarrow C=\mathbf P^1\). We now derive the pairing for the ordinary sheaf \(j_*L\), including its boundary terms, from Lemma 4.3.

**Proposition 6.2 (duality of the middle extension on a curve).** For a classical lisse \(\mathbf Q_\ell\)-sheaf \(L\) on \(U\), cup product and trace give perfect pairings
\[
H^i(C,j_*L)\otimes H^{2-i}(C,j_*L^\vee)
\longrightarrow\mathbf Q_\ell(-1).
\tag{6.4}
\]
The construction is equivariant for arithmetic Frobenius when \(C,U,L\) descend to a finite field.

**Proof.** The quotient \(j_*L/j_!L\) is supported on the finite boundary. It has no positive cohomology, so
\(H_c^1(U,L)\to H^1(C,j_*L)\) is onto and
\(H^2(C,j_*L)=H_c^2(U,L)\).
The first terms of the Leray spectral sequence for \(j\) give an injection
\(H^1(C,j_*L)\to H^1(U,L)\).
Consequently
\[
H^1(C,j_*L)=
\operatorname{im}\bigl(\alpha_L:H_c^1(U,L)\to H^1(U,L)\bigr).
\tag{6.4a}
\]
Both these maps are the natural maps induced by extension by zero and restriction. In degree zero, \(H^0(C,j_*L)=H^0(U,L)\).

Lemma 4.3 identifies \(H^1(U,L^\vee)\) with the dual of \(H_c^1(U,L)\), retaining the trace line. Under this identification the adjoint of \(\alpha_L\) is \(-\alpha_{L^\vee}\): the sign is the exchange of two degree-one cup factors. To check the adjunction, choose compact classes \(a,b\). The two evaluations are the trace of their cup product after the same natural map to ordinary cohomology, in the two orders; graded commutativity gives precisely the minus sign. Thus
\[
(\ker\alpha_L)^\perp=\operatorname{im}\alpha_{L^\vee}.
\tag{6.4b}
\]
This last equality is elementary linear algebra: the image of the dual of a finite-dimensional map is the annihilator of its kernel.

For \(x=\alpha_L(a)\) and \(y\in\operatorname{im}\alpha_{L^\vee}\), define their pairing by the compact–ordinary pairing of \(a\) with \(y\). Equation (6.4b) makes this independent of the lift \(a\), and makes the induced pairing between the two images perfect. By (6.4a) these are the two degree-one groups in (6.4). This is their cup-product pairing on \(C\): evaluation \(L\otimes L^\vee\to\mathbf Q_\ell\) extends to \(j_*L\otimes j_*L^\vee\to\mathbf Q_\ell\), since \(j_*\mathbf Q_\ell=\mathbf Q_\ell\) on the smooth connected curve. Naturality of cup product with the maps from \(j_!\) identifies its trace with the compact pairing just used.

For degrees zero and two, the identifications above reduce (6.4) directly to Lemma 4.3's pairing of \(H^0(U,L)\) with \(H_c^2(U,L^\vee)\), and its exchanged version. All other groups vanish by the curve cohomological-dimension bound. This proves every degree. All constructions use natural maps and the degree-normalized trace, so they commute with Frobenius; on the target line it acts by \(q\). \(\square\)

Equivalently, twist the second factor by \((1)\) to obtain a scalar-valued perfect pairing. The boundary stalks of \(j_*L\) are local-inertia invariants. Replacing them by full generic fibres would lose the kernel in (6.4b) and would not prove this theorem. Deligne states the resulting pairing in (2.12), printed p.283.

**Corollary 6.2 (Deligne (3.9)).** Every eigenvalue \(\gamma\) of \(F\) on \(H^1(\mathbf P^1,j_*\mathcal F)\) is algebraic, and every complex conjugate satisfies
\[
q^{\beta/2}\le|\gamma|\le q^{\beta/2+1}.
\tag{6.5}
\]

**Proof.** The quotient \(\mathcal B=j_*\mathcal F/j_!\mathcal F\) is supported on finitely many points, so \(H^1(\mathbf P^1,\mathcal B)=0\). Its long exact sequence gives a Frobenius-equivariant surjection
\[
H_c^1(U,\mathcal F)\twoheadrightarrow
H^1(\mathbf P^1,j_*\mathcal F).
\tag{6.6}
\]
The characteristic polynomial of a quotient divides that of the original operator over \(\mathbf Q_\ell\), so its eigenvalues are algebraic and have the upper bound of Corollary 6.1, for every conjugate.

The sheaf pairing identifies \(\mathcal F^\vee\simeq\mathcal F(\beta)\). Combining this identification with (6.4) gives a perfect pairing on \(H^1(\mathbf P^1,j_*\mathcal F)\) valued in \(\mathbf Q_\ell(-\beta-1)\). It is Frobenius-equivariant, so \(q^{\beta+1}/\gamma\) is another eigenvalue of the same operator. Applying the upper bound to that eigenvalue gives
\(q^{\beta+1}/|\gamma|\le q^{\beta/2+1}\), which is the lower bound in (6.5). \(\square\)

These are deliberately coarse bounds. Their midpoint exponent is \((\beta+1)/2\), with error \(1/2\). The lower exponent is \(\beta/2\), not \(\beta-1/2\). In Lesson 11 the fibre weight is \(\beta=d-1\), giving the interval \(q^{d/2-1/2}\) to \(q^{d/2+1/2}\) for the varying middle term. The tensor-power trick will remove that error.

The quotient argument proves algebraicity and the bounds for all conjugates. It does not by itself prove that the quotient characteristic polynomial is rational. Even a rational matrix can have a stable subspace over \(\mathbf Q_\ell\) with an irrational quotient eigenvalue: over \(\mathbf Q_7\), the matrix \(\begin{pmatrix}0&2\\1&0\end{pmatrix}\) has an eigenline and a one-dimensional quotient with eigenvalue \(\sqrt2\). The root lies in \(\mathbf Q_7\) by Hensel lifting a root of \(T^2-2\) modulo \(7\). Thus the surjection in (6.6) justifies exactly the algebraicity conclusion stated by Deligne (3.9); it supplies no general rational-matrix descent for this quotient.

### The same argument over other curves and coefficient fields

**Proposition 6.3.** Theorem 1.1 and Corollaries 6.1–6.2 remain valid with \(U_0\) any smooth separated geometrically connected finite-type curve over \(\mathbf F_q\), and with its smooth projective completion \(C_0\) replacing \(\mathbf P^1\) in the middle-extension statement. They also remain valid for a finite coefficient extension \(E/\mathbf Q_\ell\), with pairing into \(E(-\beta)\). In either version, Zariski density in the corresponding algebraic symplectic group suffices in place of openness. The local characteristic polynomials are still required to belong to \(\mathbf Q[T]\).

**Proof.** Fix a point being tested and, if necessary, remove another closed point to make the curve affine. Surjectivity of the geometric fundamental group under restriction preserves its image. All steps of §§2–5 then apply: the trace formula and curve duality hold on every smooth curve, the tensor contractions are algebraic statements over any characteristic-zero field, and the only use of openness was density. Formula (4.3) therefore has precisely the same Frobenius scalars. No geometry specific to \(\mathbf P^1\) entered the local-purity proof.

For the global bound, choose a nonconstant rational function on \(C_0\). It extends to a finite map \(C_0\to\mathbf P^1\), of some degree \(e\): on a smooth complete curve its pole divisor defines the extension, the nonconstant map is proper with finite fibres, and hence finite. Thus
\[
M_d\le\#C_0(\mathbf F_{q^d})\le e(q^d+1).
\]
This replaces the counting bound in (6.3) and gives the same convergence disc. On an affine curve, \(H_c^0=0\) as before; if the curve is complete, \(H_c^0=H^0=0\) because the standard symplectic representation has no invariants. Its top coinvariants also vanish in both cases. Hence (6.1) still holds. The proof of Proposition 6.2 uses only a smooth complete curve and a finite boundary, so it supplies the same pairing on \(C\); the quotient and similitude argument proves the same interval.

For \(E\)-coefficients, Lesson 8, Theorem 2.1, already gives the determinant formula over \(E\). Curve duality also gives its \(E\)-valued evaluation-and-trace pairing. One can verify this directly by restriction of scalars: the nondegenerate field trace \(\operatorname{Tr}_{E/\mathbf Q_\ell}\) identifies the \(\mathbf Q_\ell\)-dual of an \(E\)-space with its \(E\)-dual, and the composite of the \(E\)-valued cup pairing with field trace is the perfect pairing of Lemma 4.3. Thus the \(E\)-valued pairing is perfect as well. Rational local polynomials still give rational traces and rational tensor polynomials, so the nonnegative real-series argument is unchanged. This proves every assertion. \(\square\)

The rationality condition cannot be replaced in this proof by “coefficients in a number field” without an additional condition ensuring real nonnegative even traces under the embeddings in use. It is the precise source of positivity, independently of the choice of \(\ell\)-adic coefficient field.

The later general weight theorem gives stronger bounds. Deligne, *Weil II*, Corollary (3.3.4), applied to a pointwise pure lisse sheaf of weight \(\beta\), bounds the weights of \(H_c^1\) by \(\beta+1\), so \(|\gamma|\le q^{(\beta+1)/2}\). Corollary (3.3.5) bounds ordinary \(H^1\) from below by that weight; together they make the image of \(H_c^1\to H^1\) pure of weight \(\beta+1\), as stated in (3.3.6). Proposition 6.2 identifies this image with \(H^1(C,j_*\mathcal F)\). These sharper conclusions require the general weight theorem, beyond the estimate proved here. They are a comparison with that later theory and are not inputs to §§1–7 or to the Weil I argument in Lesson 11. Hard Lefschetz is likewise not an input.

## 7. Examples and the twisting qualification

### A family of elliptic curves

For \(q\) odd, take the Legendre family
\[
y^2=x(x-1)(x-\lambda),\qquad
U_0=\mathbf P^1-\{0,1,\infty\},\qquad
\mathcal F_0=R^1f_*\mathbf Q_\ell.
\]
It is lisse of rank \(2\), and its nonconstant function
\(j(\lambda)=256(1-\lambda+\lambda^2)^3/(\lambda^2(1-\lambda)^2)\)
makes it an explicit nonisotrivial example. Cup product gives (1.1) with \(\beta=1\), using the degree-normalized curve trace. Every smooth fibre has local polynomial
\[
1-a_xT+q_xT^2,\qquad
a_x=q_x+1-\#X_x(\mathbf F_{q_x})\in\mathbf Z,
\]
by the fixed-point formula and duality in [Lesson 5](cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves.md), and Lesson 8, (6.3). We verify the remaining monodromy hypothesis algebraically.

**Proposition 7.1.** For every odd \(q\) and every \(\ell\ne p\), including \(\ell=2\), the geometric monodromy of this family is open in \(\operatorname{SL}_2(\mathbf Q_\ell)\). In a symplectic integral basis its image has finite index in \(\operatorname{SL}_2(\mathbf Z_\ell)\).

**Proof.** Set \(k=\overline{\mathbf F}_q\), let \(V\) be the geometric fibre, and let \(G\) be the geometric image. We use the actual Tate uniformization proved in Lesson 8, Theorem 6.3. At \(0\) and \(1\), its equation (6.6) gives nontrivial unipotent inertia: the multiplicative parameter has valuation \(2\), so its image contains \(1+2\mathbf Z_\ell N\) for a nonzero rank-one nilpotent \(N\), in an appropriate integral basis. Dualizing to \(H^1\) takes inverse transposes and preserves this assertion. Wild inertia acts trivially. At \(\infty\), equation (6.7) identifies the family as a ramified quadratic twist of a multiplicative family. The inertia semisimplification is therefore the quadratic character twice; an element with quadratic character \(-1\) has both eigenvalues \(-1\). These assertions include the valuation factor \(2\); it is not a unit when \(\ell=2\).

First, \(V\) is absolutely irreducible. Otherwise a \(G\)-stable line is defined over a finite extension \(E/\mathbf Q_\ell\); write \(\chi\) for its character. On inertia at \(0,1\) its character is trivial, because a unipotent operator has only eigenvalue \(1\); at \(\infty\) it is the nontrivial quadratic character. Thus \(\chi^2\) is trivial on inertia at all three missing points. Compactness allows an \(\mathcal O_E\)-lattice on this line. Every reduction of \(\chi^2\) modulo a power of the maximal ideal is a finite character unramified at the missing points. Its cover extends étale across those points: normalize the smooth complete curve in the finite covering field, and apply the unramified criterion over each strict henselian discrete valuation ring. This is the normalization argument of *Étale fundamental groups*, §4. The extended cover of \(\mathbf P^1_k\) is trivial by that lesson's Proposition 5.1. Indeed a connected degree-\(e\) étale cover would have canonical degree \(2g-2=-2e\), forcing \(e=1\). Every reduction of \(\chi^2\) is consequently trivial, and separatedness of \(\mathcal O_E\) gives \(\chi^2=1\).

The resulting character \(\chi\) has values in \(\{1,-1\}\), and is unramified at \(0,1\), so it defines a quadratic étale cover of \(\mathbf A^1_k\). Such a cover is trivial: the Kummer sequence, valid because \(p\ne2\), gives its group of classes between \(k[t]^*/(k[t]^*)^2=0\) and \(\operatorname{Pic}(k[t])[2]=0\). Here \(k\) is algebraically closed and \(k[t]\) is a principal ideal domain. This contradicts the value \(-1\) on inertia at infinity. Notice that only quadratic covers of the affine line were used; its full fundamental group in positive characteristic need not be trivial.

Write the nilpotent of one nontrivial inertia subgroup, after a nonzero scalar adjustment, as
\(N_u(x)=\psi(x,u)u\). Absolute irreducibility gives \(g\in G\) for which \(v=gu\) is independent of \(u\). Conjugation supplies a nonzero open parameter subgroup \(1+tN_v\) in \(G\). Rescale \(v\) so that \(\psi(u,v)=1\); this merely rescales its open parameter set. Choose a nonidentity \(h=1+t_0N_u\) in the first subgroup. Then \(w=hv=v+a u\), with \(a=-t_0\ne0\), and conjugation by \(h\) supplies a third subgroup \(1+tN_w\). In the basis \((u,v)\), the three nilpotents are
\[
N_u=\begin{pmatrix}0&-1\\0&0\end{pmatrix},\qquad
N_v=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
N_w=\begin{pmatrix}a&-a^2\\1&-a\end{pmatrix}.
\]
They span \(\mathfrak{sl}_2\), since the third has nonzero diagonal and the first two span the off-diagonal subspace.

The product map
\[
(t_1,t_2,t_3)\longmapsto
(1+t_1N_u)(1+t_2N_v)(1+t_3N_w)
\]
has invertible derivative at zero, using the Cayley chart of §4 as a target chart. It therefore maps a small \(\ell\)-adic ball onto a neighbourhood of the identity. For completeness, the local inverse assertion follows by composing with the inverse derivative and shrinking the ball: the map becomes \(x\mapsto x+R(x)\), where \(R\) has Lipschitz constant strictly less than \(1\). For every sufficiently small \(y\), iteration of \(x\mapsto y-R(x)\) converges in the complete ball to its unique solution. All three parameter balls can be chosen inside the actual inertia subgroups and their conjugates, so this neighbourhood lies in \(G\). Thus \(G\) is open. The symplectic integral Tate lattice places it inside \(\operatorname{SL}_2(\mathbf Z_\ell)\); compactness of that group makes the index of an open subgroup finite. \(\square\)

All three hypotheses of Theorem 1.1 are now verified, and it gives local weight \(1\). The cohomological bounds give \(|\gamma|\le q^{3/2}\) on \(H_c^1\) and \(q^{1/2}\le|\gamma|\le q^{3/2}\) on \(H^1(\mathbf P^1,j_*\mathcal F)\). Lesson 8, (6.8) and Exercise 8.9, give a more precise check in this particular family: the two compact-support eigenvalues are \(1\) and \(\chi_q(-1)\), while the middle-extension \(H^1\) is zero. Thus the latter interval is vacuous in this example. These calculations and Proposition 7.1 use the Tate proof, not the higher-dimensional Picard–Lefschetz theorem.

This proves the example for a concrete family with nonconstant \(j\). Extending the monodromy assertion to every nonisotrivial elliptic family uses the separate modular-curve monodromy theorem; no such additional theorem is needed for this example.

### What a Frobenius-character twist actually changes

Rationality enters at two identifiable places: (2.1) makes even trace powers nonnegative real numbers, and (5.1)/(6.1) turns the global determinant into a rational polynomial whose roots are algebraic. An arbitrary \(\ell\)-adic trace cannot be ordered as a real number or silently regarded as algebraic over \(\mathbf Q\).

Here is a twist that makes that distinction concrete. Work over \(\mathbf F_5\), with \(\ell\ne5\). Choose
\(c\in1+\ell\mathbf Z_\ell\) transcendental over \(\mathbf Q\); for \(\ell=2\) one can choose it in \(1+4\mathbf Z_2\). Such choices exist because these sets are uncountable and the algebraic numbers are countable. There is a continuous rank-one constant-field character \(\chi_c\) with geometric Frobenius \(c\): the homomorphism from the integers generated by Frobenius extends to \(\widehat{\mathbf Z}\), since the closure of the cyclic subgroup of the compact unit group is profinite.

Twist the Legendre sheaf by this character. Geometric monodromy stays the same, and the local eigenvalues become \(c^{d_x}\alpha_{x,j}\). At \(\lambda=2\), direct counting gives \(a_x=-2\), so the new polynomial is
\[
1+2cT+5c^2T^2.
\tag{7.1}
\]
It is not rational, and its eigenvalues are not algebraic over \(\mathbf Q\). Thus this twist fails both condition 3 and the conclusion of purity.

There is a necessary qualification: it also changes the pairing target to
\(\mathbf Q_\ell(-1)\otimes\chi_c^{\,2}\). It does **not** preserve condition 1 with the original Tate line. In rank \(2\), the determinant at this fibre is \(5c^2\), whereas a nondegenerate alternating pairing into \(\mathbf Q_\ell(-1)\) would require determinant \(5\). A constant-field twist retaining that pairing must have \(\chi_c^2=1\); then it is a quadratic twist and preserves both rationality and weight. Consequently the arbitrary-character example demonstrates the role of rationality in this proof, but is not a counterexample obtained by dropping condition 3 alone while retaining conditions 1–2.

<a id="8-exercises-and-audited-solutions"></a>

## 8. Exercises and solutions

**Exercise 10.1 (easy).** Prove the Tate and tensor-product weight assertions, keeping all complex conjugates in the statement.

**Solution.** The only eigenvalue on \(\mathbf Q_\ell(r)\) at \(x\) is the rational number \(q_x^{-r}\), of modulus \(q_x^{(-2r)/2}\). Tensor eigenvalues are products \(\alpha\delta\); for any embedding of a number field containing both factors, their moduli multiply to \(q_x^{(\beta+\gamma)/2}\). Algebraicity is preserved under products. Every conjugate of a product arises under such an embedding, which proves the required all-conjugates assertion. Inverse eigenvalues similarly prove the dual-weight assertion.

**Exercise 10.2 (medium).** Prove the radius comparison for an infinite product of nonnegative series, and explain its rational-function version.

**Solution.** For each coefficient only finitely many nonconstant factors contribute, by the order hypothesis. The coefficient of any single factor is one nonnegative summand of the product coefficient, using constant terms from the other factors. This is (3.1); evaluating at any positive \(R\) below the product radius proves absolute convergence of the factor there. For a rational function in reduced form the Taylor radius is the modulus of the nearest genuine pole, as proved in Lemma 3.2. Applying the comparison gives (3.2), even if some global denominator factors cancel. It is unnecessary to assume every coefficient is strictly positive.

**Exercise 10.3 (medium).** Given the upper local bound and the alternating pairing, obtain equality for every conjugate.

**Solution.** If \(A\) represents local Frobenius and \(J\) the pairing, \(A^{\mathsf t}JA=q_x^\beta J\) shows \(A\) is similar to \(q_x^\beta A^{-\mathsf t}\). Thus the eigenvalue multiset is stable under \(\alpha\mapsto q_x^\beta/\alpha\). For any complex embedding, the upper bound for this partner gives \(q_x^\beta/|\alpha|\le q_x^{\beta/2}\). Together with \(|\alpha|\le q_x^{\beta/2}\), this forces equality. No diagonalizability or pairing of a chosen individual eigenvector is needed.

**Exercise 10.4 (medium).** Identify where rationality is used. Construct a Frobenius-character twist that violates it, and check the other hypotheses rather than assuming they survive.

**Solution.** Newton identities give rational traces; the even powers in (2.2) become nonnegative real numbers, enabling Lemma 3.1. Rational local factors also give rational global coefficients and the rational polynomials in (5.1) and (6.1). For the Legendre sheaf over \(\mathbf F_5\), choose the transcendental unit \(c\) of §7 and use \(\chi_c\). At \(\lambda=2\), the fibre has \(8\) rational points, so trace \(6-8=-2\). Its twisted polynomial is (7.1), which is not rational; multiplying a nonzero algebraic eigenvalue by transcendental \(c\) also destroys algebraicity. Geometric monodromy is unchanged, but the determinant becomes \(5c^2\), and the pairing target acquires \(\chi_c^2\). Thus condition 1 fails as well. If one insists on retaining it, only \(c^2=1\) is allowed for this constant-field twist, and that twist is not the requested rationality counterexample.

**Exercise 10.5 (hard).** Prove the two-sided bound for \(H^1(\mathbf P^1,j_*\mathcal F)\) from the compact-support bound and curve duality.

**Solution.** The boundary quotient \(j_*\mathcal F/j_!\mathcal F\) has finite support and no \(H^1\). Its long exact sequence gives (6.6), so all eigenvalues in question already occur on \(H_c^1\), proving algebraicity and the upper bound \(q^{\beta/2+1}\). The pairing identifies \(\mathcal F^\vee=\mathcal F(\beta)\). Duality (6.4), including the curve trace twist \((-1)\), then makes the degree-one pairing take values in \(\mathbf Q_\ell(-\beta-1)\). Hence \(q^{\beta+1}/\gamma\) also occurs. Apply the upper bound to this eigenvalue and rearrange to obtain \(|\gamma|\ge q^{\beta/2}\). The same argument applies to every conjugate because the original compact-support characteristic polynomial is rational.

**Exercise 10.6 (medium; pole-order check).** For a two-dimensional symplectic space, determine the pole denominator in (5.1) for \(k=1,2\), and distinguish a possible pole from a guaranteed one.

**Solution.** The unique contraction for two tensor factors gives \(N_1=1\), hence denominator \(1-q^{\beta+1}t\). For four factors, the first fundamental theorem gives three contractions, with relation (4.4). The evaluations after that formula prove two are independent, so \(N_2=2\); the denominator is \((1-q^{2\beta+1}t)^2\). The numerator can cancel a factor. The convergence proof only requires that there be no pole of smaller modulus. In fact, for positive rank the Euler product and Lemma 3.1 prevent all global poles from disappearing: a local reciprocal determinant has a finite radius, whereas a polynomial global series would have infinite radius. The pole order need not equal the uncancelled top-cohomology dimension.

## Scope and references

The general-linear centralizer lemma, the first fundamental theorem for symplectic tensors, and density of open symplectic subgroups are proved in §4. Lemma 4.3 proves the adic passage from finite-coefficient curve duality, and Proposition 6.2 proves the pairing for \(j_*\); their uses and twists are specified in §§4–6. Lesson 8, Theorem 2.1, supplies the characteristic-zero determinant formula, using the all-dimensional trace theorem and adic comparison of Lessons 7 and 2. Its Theorem 2.2 also proves the full finite-coefficient determinant formula, including nonreduced rings. The positivity lemmas, radius comparison, fundamental estimate, both cohomological bounds, and the extensions of Proposition 6.3 are proved here.

[Lesson 5](cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves.md), §§2.1–2.7 and Theorem 5.3, contains the full Hodge-index proof on \(C\times C\) of the Riemann hypothesis for curves; its fixed-point formula and duality give the local elliptic polynomial used here. The degree-normalized trace and its general smooth duality extension are also proved in Smooth trace and duality, §§1–2 and 8–13. Proposition 7.1 proves Legendre openness from Lesson 8's actual Tate uniformization and boundary calculations, together with normalization and the fundamental group of \(\mathbf P^1\) in [Étale fundamental groups](course:AG-DFG/AG-DFG-05), §4 and Proposition 5.1. It requires no higher-dimensional Picard–Lefschetz assertion. Curve intersection positivity and the nonnegative trace powers in this lesson are distinct arguments; the latter prove Theorem 1.1 without assuming curve purity.

Applications to higher-dimensional vanishing quotients still require the algebraic local variation, tameness, conjugacy and geometric monodromy statements of Lesson 9. Those geometric assertions are separate from Theorem 1.1's explicitly assumed open-monodromy hypothesis. The comparison with the sharper Weil II bounds in §6 requires the general weight theorem stated there.

- [Deligne, *La conjecture de Weil I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), (1.2)–(1.7) for conventions; (2.10)–(2.12), printed pp.282–283, for compact-support coinvariants and \(j_*\)-duality; §3, printed pp.283–287, especially Theorem (3.2), Lemmas (3.3)–(3.6), the invariant-theory computation (3.7), and Corollaries (3.8)–(3.9).
- The first fundamental theorem for the symplectic group is due to Hermann Weyl (1939); H. Kraft and C. Procesi, [*Classical Invariant Theory: A Primer*](https://dmi.unibas.ch/fileadmin/user_upload/dmi/Personen/Kraft_Hanspeter/Classical_Invariant_Theory.pdf), §10.3, proves it from Weyl's theorems on polarization. The tensor theorem used above is proved in this lesson.
- [P. Deligne, G. I. Lehrer and R. B. Zhang, *The first fundamental theorem of invariant theory for the orthosymplectic super group*](https://publications.ias.edu/sites/default/files/2015-06-ortho.pdf), for the geometric reduction to general linear invariant theory. The ordinary characteristic-zero symplectic argument is proved above.
- [Deligne, *La conjecture de Weil II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), (3.3.4)–(3.3.6), printed p.206, for the sharper weight comparison in §6.
- [Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day*](https://arxiv.org/abs/1509.00797), “Landau's theorem,” “Rankin's theorem,” “A remark of Langlands,” “Grothendieck's theorem,” and “The main lemma (restricted form).” Its normalization \(q^{d/2+1}\) agrees with (6.2) for \(\beta=d\). The lower exponent printed in its later completion passage must instead be read as \(d/2-1/2\), as confirmed by Deligne's (3.9) with fibre weight \(d-1\).
- [Lesson 8](l-functions-rationality-and-the-functional-equation.md), Theorems 2.1–2.2 and 6.3, (6.6)–(6.8) and Exercise 8.9; [Lesson 9](lefschetz-pencils-and-vanishing-cycles.md) for the separate higher-dimensional applications; [Poincaré duality for curves](course:ag-etale-cohomology/poincare-duality-for-curves), Theorem 11.1 and §5, for the full finite-coefficient curve proof. Lemma 4.3 and Proposition 6.2 above prove the adic passage and the middle-extension pairing used here.
- [AI Integrated Stacks, trace-formula chapter](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/trace.tex), “Cohomology of curves, revisited,” for the canonical finite-module formulation of top compact-support coinvariants and the cyclotomic twist. This lesson proves the general-linear and symplectic invariant statements, the adic passage and the middle-extension pairing. The underlying Stacks Project mathematics is credited to its human authors and retains its GNU Free Documentation License.

Linked sources retain their own rights.

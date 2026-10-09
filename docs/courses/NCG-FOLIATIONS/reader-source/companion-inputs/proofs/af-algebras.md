# AF-algebras

*Public domain (CC0).*

An AF-algebra is a C\*-algebra that contains an increasing sequence of finite-dimensional C\*-subalgebras whose union is dense. The letters stand for "approximately finite-dimensional". The compact operators on a separable Hilbert space, the infinite tensor product \(M_2\otimes M_2\otimes\cdots\), the continuous functions on the Cantor set and the group C\*-algebra of the group of finitary permutations of \(\mathbb N\) are all AF-algebras. Elliott's theorem classifies AF-algebras completely by a computable invariant [Elliott 1976], and their combinatorics reappears in the theory of subfactors.

This lesson develops the theory from the beginning. A finite-dimensional C\*-algebra is a direct sum of full matrix algebras, so it is described by a vector of sizes (Section 2). A \*-homomorphism between two such algebras is described, up to conjugation by a unitary, by a matrix of multiplicities (Section 3). An AF-algebra is therefore coded by a sequence of such matrices, drawn as a Bratteli diagram, and conjugating the connecting maps by unitaries does not change the limit (Section 4). After the first examples (Section 5) we attach to every AF-algebra an ordered abelian group with a distinguished subset, its scaled dimension group (Section 6). Many different diagrams give the same algebra, but the scaled dimension group depends only on the algebra: it is the ordered \(K_0\)-group together with the classes of the projections (Section 7). Elliott's theorem says that it classifies AF-algebras up to isomorphism, and that the ordered group alone classifies them up to stable isomorphism; Glimm's classification of UHF algebras is a special case (Section 8). We compute the invariant of the gauge-invariant CAR algebra, whose Bratteli diagram is Pascal's triangle; its group is \(\mathbb Z[t]\), ordered by strict positivity on the open unit interval (Section 9). Section 10 describes the traces of an AF-algebra as a projective limit. Section 11 shows that passing to commutants turns the diagram of a unital embedding between finite-dimensional algebras into its mirror image. Section 12 treats group algebras of locally finite groups, such as the infinite symmetric group.

The lesson assumes the elementary theory of C\*-algebras: the continuous functional calculus, the unitization, positive elements, quotients by closed ideals and faithful representations. These are developed in the lessons [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html), [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html) and [Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html). Section 1 lists exactly what we use. Exercise 1 also uses [The Stone–Weierstrass theorem for functions vanishing at infinity](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html).

Basic references are [Takesaki 2003, Chapter XIX, §1], [Blackadar 1998, Section 7] and [Blackadar 2017, II.8.2 and V.1–V.2]; a recent survey is [Blackadar 2025, Chapter I.3].

## 1. Conventions and background

### Conventions

- Zero algebras and zero-dimensional representations are allowed, but an irreducible representation is nonzero and acts on a nonzero Hilbert space. Empty sums and maxima of nonnegative rank coordinates are taken as zero; matrix amplifications \(M_N\) always have \(N\geq1\). In polynomial evaluations, the exponent-zero factor is \(1\), including at \(0\).
- All algebras are complex. A C\*-algebra need not have a unit. A *\*-homomorphism* is a linear, multiplicative map that preserves adjoints. An *embedding* is an injective \*-homomorphism and an *isomorphism* is a bijective one; we write \(A\cong B\).
- \(M_k\) is the algebra of complex \(k\times k\) matrices, with matrix units \(e_{ab}\) and unit \(1_k\). \(\operatorname{Tr}\) is the trace on \(M_k\) with \(\operatorname{Tr}e_{aa}=1\); for a projection \(p\in M_k\), \(\operatorname{Tr}p\) is the rank of \(p\). For \(x\in M_k\) and an integer \(b\geq0\), \(x^{(b)}=\operatorname{diag}(x,\dots,x)\in M_{kb}\) is the block-diagonal matrix with \(b\) copies of \(x\) (it is empty when \(b=0\)), and \(0_d\) is the zero \(d\times d\) matrix. We identify \(\mathbb C^k\otimes\mathbb C^b\) with \(\mathbb C^{kb}\) so that \(\varepsilon_a\otimes f_t\) (standard bases) is the \(a\)-th basis vector of the \(t\)-th block of length \(k\); then the operator \(x\otimes1\) is the matrix \(x^{(b)}\).
- Inner products are linear in the first variable.
- \(\mathbb Z_+=\{0,1,2,\dots\}\) and \(\mathbb N=\{1,2,\dots\}\). Elements of \(\mathbb Z^r\) and \(\mathbb R^r\) are column vectors, and matrices act on them from the left. For vectors, \(x\leq y\) means \(x_i\leq y_i\) for every \(i\); \(\mathbb Z^r_+=\{x\in\mathbb Z^r:x\geq0\}\); \(e_1,\dots,e_r\) is the standard basis; \(x^{T}\) is the transpose.
- The *unitization* \(A^+\) of a C\*-algebra \(A\) is \(A\oplus\mathbb C\) with the product \((a,\lambda)(b,\mu)=(ab+\lambda b+\mu a,\lambda\mu)\), the adjoint \((a,\lambda)^*=(a^*,\bar\lambda)\) and its C\*-norm; we write \(a+\lambda1\) for \((a,\lambda)\). We adjoin a new unit even when \(A\) has one; then \(A^+\cong A\oplus\mathbb C\). The algebra \(A\) is a closed ideal of \(A^+\). For a unitary \(u\in A^+\), \(\operatorname{Ad}u(a)=uau^*\) maps \(A\) onto \(A\) and is an automorphism of \(A\). A \*-homomorphism \(\varphi:A\to B\) has the unital extension \(\varphi^+:A^+\to B^+\), \(\varphi^+(a+\lambda1)=\varphi(a)+\lambda1\).
- The spectrum \(\sigma(x)\) of an element \(x\) of a C\*-algebra \(A\) is taken in \(A^+\). It always contains \(0\), because \(x\) lies in the proper ideal \(A\) of \(A^+\).
- For projections \(p,q\), we write \(q\leq p\) (\(q\) is a *subprojection* of \(p\)) if \(pq=q\). A nonzero projection is *minimal* if its only subprojections are \(0\) and itself. Projections \(p,q\) of a C\*-algebra \(A\) are *equivalent*, \(p\sim q\), if \(p=v^*v\) and \(q=vv^*\) for some \(v\in A\). If \(A\) is unital, \(U(A)\) is its unitary group, and \(p,q\) are *unitarily equivalent* if \(q=upu^*\) for some \(u\in U(A)\).

### Results used from other lessons

The lesson uses the following earlier full proofs, elementary linear algebra, and the completion and compactness tools in (i)–(j).

- (a) *Homomorphisms.* A \*-homomorphism between C\*-algebras is contractive. An injective one is isometric, and the image of any \*-homomorphism is closed, hence a C\*-subalgebra. Consequently a \*-algebra carries at most one norm that makes it a C\*-algebra. (Proved in [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Sections 4 and 15.)
- (b) *Neumann series.* In a unital Banach algebra, an element \(y\) with \(\|1-y\|<1\) is invertible. (Proved in [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html), Section 2.)
- (c) *Functional calculus.* Let \(x\) be a self-adjoint element of a C\*-algebra \(A\). Its spectrum is real. For every continuous function \(f\) on \(\sigma(x)\) with \(f(0)=0\) there is an element \(f(x)\) of the C\*-subalgebra generated by \(x\). The map \(f\mapsto f(x)\) is a \*-homomorphism that sends the identity function to \(x\); \(\sigma(f(x))=f(\sigma(x))\) and \(\|f(x)\|=\max_{\sigma(x)}|f|\); and \(\psi(f(x))=f(\psi(x))\) for every \*-homomorphism \(\psi\). If \(A\) is unital, the same holds for every continuous \(f\) on the spectrum of \(x\) in \(A\), with \(f(x)\) in the C\*-subalgebra generated by \(x\) and \(1_A\); if \(B\subseteq A\) is a C\*-subalgebra with \(1_A\in B\) and \(x\in B\), the spectrum of \(x\) and the element \(f(x)\) are the same whether computed in \(B\) or in \(A\). Finally, if \(x_n\to x\) are self-adjoint with spectra in a fixed compact set \(Y\) and \(f\) is continuous on \(Y\), then \(f(x_n)\to f(x)\). (Proved in the lesson on C\*-algebras just cited, Sections 3, 5 and 6.)
- (d) *Positivity.* The positive elements of a C\*-algebra form a closed convex cone; \(y^*y\geq0\) for every \(y\); and every positive element \(a\) equals \(b^*b\) for some \(b\), for instance \(b=a^{1/2}\). (Proved in the same lesson, Section 8.)
- (e) *Quotients.* If \(J\) is a closed two-sided ideal of a C\*-algebra \(A\), then \(A/J\) with the quotient norm is a C\*-algebra. (Proved in the same lesson, Section 15.)
- (f) *Unitization and matrices.* The unitization \(A^+\) is a C\*-algebra in which \(A\) is a closed ideal ([Proposition 3.4 of the Banach-algebra lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-05), including the unital case of Exercise 5). For a C\*-algebra \(A\), the matrix algebra \(M_n(A)\), with \((x^*)_{ab}=(x_{ba})^*\), is a C\*-algebra, and \(\max_{a,b}\|x_{ab}\|\leq\|x\|\leq\sum_{a,b}\|x_{ab}\|\). *Proof.* By (g), \(A\subseteq B(H)\) for some Hilbert space \(H\). Let \(J_b:H\to H^n\) be the inclusion of the \(b\)-th summand and \(P_a=J_a^*\) the \(a\)-th coordinate map. Then \(x\mapsto\sum_{a,b}J_ax_{ab}P_b\) identifies \(M_n(A)\) with a \(*\)-subalgebra of \(B(H^n)\), with \(x_{ab}=P_axJ_b\). It is closed: if these operators converge in norm, so does each entry \(P_axJ_b\), and \(A\) is closed. So \(M_n(A)\) is a C\*-algebra, and by (a) its norm does not depend on \(H\). Finally \(\|x_{ab}\|=\|P_axJ_b\|\le\|x\|\) and \(\|x\|\le\sum_{a,b}\|J_ax_{ab}P_b\|=\sum_{a,b}\|x_{ab}\|\).
- (g) *Faithful representations.* Every C\*-algebra has an injective \*-homomorphism into \(B(H)\) for some Hilbert space \(H\) [Blackadar 2017, II.6.4.10]. (Proved in [Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html), Section 7.)
- (h) *Compact operators.* Let \(H\) be a Hilbert space with orthonormal basis \((\varepsilon_i)_{i\geq1}\) and let \(P_n\) be the projection onto the span of \(\varepsilon_1,\dots,\varepsilon_n\). For every compact operator \(T\) on \(H\), \(\|T-P_nT\|\to0\); and the adjoint of a compact operator is compact. (Proved in [Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html), Theorem 5.1(2) and (5).)

- (i) *Completion, finite dimension and Hilbert tensors.* The [completion lemma in Section 1 of the Hilbert-space lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#completing-normed-and-inner-product-spaces) constructs normed-space and Hilbert completions and proves unique bounded-map extension into a complete space. Its [Theorem 8.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#oa-fnd-hs-08) constructs the Hilbert tensor product and its orthonormal bases. [Theorem 7.1 of the Hahn–Banach lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-07) proves equivalence of finite-dimensional norms, completeness, and closedness of finite-dimensional subspaces.
- (j) *Compactness.* [Lemma 5.0 and its finite-dimensional consequence](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#oa-fnd-hs-10) prove that a closed bounded subset of a finite-dimensional Euclidean space is compact and sequentially compact. A continuous real function on a compact set is bounded, since the inverse images of bounded open intervals give an open cover. If it is strictly positive, it has a positive minimum: otherwise choose points where its values tend to zero, take a convergent subsequence, and use continuity. The Cantor space in Exercise 1 is compact by the [full proof (B2) among the elementary facts in the Polish-space lesson](polish-spaces-and-standard-borel-spaces.md#background-used-without-proof).

The precise earlier proof locations for (a)–(h) are: homomorphisms in [Section 4](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-12) and [Section 15](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-25); Neumann series in [Section 2 of the Banach-algebra lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-02); spectral permanence in [Section 3](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-06), calculus in [Section 5](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-07), and continuity in [Section 6](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-11); positivity in [Section 8](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-15); quotients in [Section 15](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-25); the full unitization proof in [Proposition 3.4 of the Banach-algebra lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-05), with its unital case in Exercise 5; faithful representations in [Section 7 of the GNS lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#oa-fnd-gn-07); and compact approximation and adjoints in [Theorem 5.1 of the Hilbert-space lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#oa-fnd-hs-05). These full programme proofs provide the mathematical inputs; books are additional reading.

## 2. Finite-dimensional C\*-algebras

**Definition 2.1.** A *size vector* is \(\mathbf m=(m_1,\dots,m_r)\in\mathbb N^r\). The *multimatrix algebra* of \(\mathbf m\) is
\[
M_{\mathbf m}=M_{m_1}\oplus\cdots\oplus M_{m_r}.
\]
We write its elements as \(x=(x_1,\dots,x_r)\) and call \(M_{m_i}\) its \(i\)-th *summand*. We allow \(r=0\), and then \(M_{\mathbf m}=0\). Let \(z_i\) be the unit of the \(i\)-th summand and \(e^{(i)}_{ab}\) its matrix units. The minimal projections of \(M_{\mathbf m}\) are the rank-one projections of the single summands. The *rank vector* of a projection \(p=(p_1,\dots,p_r)\) is
\[
\begin{gathered}
\operatorname{rk}p\\
=(\operatorname{Tr}p_1,\dots,\operatorname{Tr}p_r)^T\in\mathbb Z^r_+,\\
0\\
\leq\operatorname{rk}p\\
\leq\mathbf m .
\end{gathered}
\]

The first aim is to show that every finite-dimensional C\*-algebra is isomorphic to some \(M_{\mathbf m}\). We do not assume a unit.

**Lemma 2.2.** Let \(F\) be a finite-dimensional C\*-algebra.

1. Every self-adjoint element of \(F\) is a real linear combination of mutually orthogonal projections of \(F\). In particular \(F\) is spanned by its projections.
2. Mutually orthogonal nonzero projections of \(F\) are linearly independent, so there are at most \(\dim F\) of them. Every nonzero projection of \(F\) dominates a minimal projection of \(F\).
3. \(F\) has a unit.

**Proof.** (1) Let \(x=x^*\in F\) and \(N=\dim F\). The elements \(x,x^2,\dots,x^{N+1}\) are linearly dependent, so \(Q(x)=0\) for a nonzero polynomial \(Q\) with \(Q(0)=0\). By the spectral mapping property (Section 1(c)), \(Q\) vanishes on \(\sigma(x)\), so \(\sigma(x)\) is a finite set of real numbers. Let \(\lambda_1,\dots,\lambda_k\) be its nonzero points, and let \(f_j\) be the function on \(\sigma(x)\) that equals \(1\) at \(\lambda_j\) and \(0\) elsewhere. It is continuous because \(\sigma(x)\) is finite, and \(f_j(0)=0\). So \(p_j=f_j(x)\) lies in \(F\). Since \(f_j=f_j^2=\bar f_j\) and \(f_jf_l=0\) for \(j\neq l\), the \(p_j\) are mutually orthogonal projections. Since \(t=\sum_j\lambda_jf_j(t)\) on \(\sigma(x)\), we get \(x=\sum_j\lambda_jp_j\). Every \(y\in F\) is the combination \(\frac12(y+y^*)+i\cdot\frac1{2i}(y-y^*)\) of two self-adjoint elements.

(2) If \(\sum_jc_jp_j=0\) with mutually orthogonal nonzero projections \(p_j\), multiplying by \(p_l\) gives \(c_lp_l=0\), so \(c_l=0\). For a projection \(q\) let \(\nu(q)\) be the largest number of mutually orthogonal nonzero subprojections of \(q\); so \(1\leq\nu(q)\leq\dim F\) when \(q\neq0\). If \(q'\) is a nonzero subprojection of \(q\) with \(q'\neq q\), then \(q-q'\) is a nonzero subprojection of \(q\) orthogonal to \(q'\), so \(\nu(q)\geq\nu(q')+1\). Hence, among the nonzero subprojections of a nonzero projection \(p\), one with the smallest value of \(\nu\) is minimal.

(3) We may assume \(F\neq0\). Choose a projection \(p\in F\) with \(\nu(p)\) as large as possible. Let \(q\in F\) be a projection, \(y=q-qp\) and \(x=y^*y\). Then \(yp=0\), so \(xp=0\) and \(px=(xp)^*=0\). Suppose \(x\neq0\). By (1), \(x=\sum_j\lambda_jp_j\) with nonzero \(\lambda_j\) and spectral projections \(p_j=f_j(x)\); here \(p_1\neq0\), because its spectrum \(f_1(\sigma(x))\) contains \(1\). On the finite set \(\sigma(x)\) the function \(f_1\) agrees with a polynomial without constant term, so \(p_1\) is a polynomial in \(x\) without constant term, and \(pp_1=0\). Then \(p+p_1\) is a projection with \(\nu(p+p_1)\geq\nu(p)+1\), which is impossible. So \(x=0\), hence \(y=0\) because \(\|y\|^2=\|x\|\). This means \(q=qp\), and, taking adjoints, \(q=pq\). By (1), \(pz=zp=z\) for every \(z\in F\). \(\square\)

**Lemma 2.3** (Full matrix algebras). Let \(E\) be a nonzero finite-dimensional C\*-algebra whose centre is \(\mathbb C1_E\). Let \(e\) be a minimal projection of \(E\). Then there are \(v_1=e,v_2,\dots,v_k\in E\) with \(v_a^*v_a=e\) for all \(a\) and \(\sum_av_av_a^*=1_E\). The elements \(e_{ab}=v_av_b^*\) satisfy \(e_{ab}e_{cd}=\delta_{bc}e_{ad}\) and \(e_{ab}^*=e_{ba}\), and \((\xi_{ab})\mapsto\sum_{a,b}\xi_{ab}e_{ab}\) is an isomorphism of \(M_k\) onto \(E\).

**Proof.** The corner \(eEe\) is a C\*-algebra with unit \(e\). By Lemma 2.2(1) it is spanned by its projections, and each of them is a subprojection of \(e\), hence \(0\) or \(e\). So
\[
eEe=\mathbb Ce .
\tag{2.1}
\]
Let \(J\) be the linear span of the products \(xey\) with \(x,y\in E\). It is a two-sided ideal, closed under adjoints and finite-dimensional, hence closed. So \(J\) is a nonzero C\*-algebra, and by Lemma 2.2(3) it has a unit \(c\), which is a projection. For \(x\in E\), both \(cx\) and \(xc\) lie in \(J\), so \(cx=cxc=xc\). Thus \(c\) is central and nonzero, so \(c=1_E\), and
\[
\begin{gathered}
1_E\\
=\textstyle\sum_lx_ley_l\\
\text{for some }x_l,y_l\in E .
\end{gathered}
\tag{2.2}
\]
If \(v^*v\) is a projection, then \(vv^*v=v\), because \[
\begin{gathered}
(v-vv^*v)^*(v-vv^*v)\\
=v^*v-2(v^*v)^2+(v^*v)^3\\
=0;
\end{gathered}
\] hence \((vv^*)^2=(vv^*v)v^*=vv^*\), and \(vv^*\) is a projection too. Choose \(v_1=e,v_2,\dots,v_k\) in \(E\) with \(v_a^*v_a=e\) and with the projections \(v_av_a^*\) mutually orthogonal, and with \(k\) as large as possible; \(k\leq\dim E\) by Lemma 2.2(2). Put \(f=1_E-\sum_av_av_a^*\), a projection. Suppose \(f\neq0\). By (2.2), \(f=f1_Ef=\sum_l(fx_le)(y_lf)\), so \(w=fxe\neq0\) for some \(x\in E\). By (2.1), \(w^*w=\lambda e\) with \(\lambda=\|w\|^2>0\). Then \(v=\lambda^{-1/2}w\) satisfies \(v^*v=e\) and \(fv=v\), so \(vv^*\) is a projection below \(f\), orthogonal to every \(v_av_a^*\). This contradicts the maximality of \(k\). Hence \(\sum_av_av_a^*=1_E\).

For \(a\neq b\), \(v_b^*v_a=v_b^*(v_bv_b^*)(v_av_a^*)v_a=0\), and \(v_a^*v_a=e\), \(v_ae=v_a\). So \(e_{ab}e_{cd}=v_a(v_b^*v_c)v_d^*=\delta_{bc}v_aev_d^*=\delta_{bc}e_{ad}\), and clearly \(e_{ab}^*=e_{ba}\) and \(e_{aa}=v_av_a^*\). The map in the statement is therefore a \*-homomorphism. For \(x\in E\), the element \(e_{1a}xe_{b1}\) lies in \(eEe\), so \(e_{1a}xe_{b1}=\xi_{ab}(x)e\) by (2.1), and
\[
\begin{gathered}
x\\
=\sum_{a,b}e_{aa}xe_{bb}\\
=\sum_{a,b}e_{a1}(e_{1a}xe_{b1})e_{1b}\\
=\sum_{a,b}\xi_{ab}(x)e_{ab}.
\end{gathered}
\]
So the map is onto. It is injective, because \(e_{1c}\big(\sum_{a,b}\xi_{ab}e_{ab}\big)e_{d1}=\xi_{cd}e\). \(\square\)

**Theorem 2.4** (Structure of finite-dimensional C\*-algebras). Every finite-dimensional C\*-algebra \(F\) is isomorphic to \(M_{\mathbf m}\) for some size vector \(\mathbf m\). The number \(r\) of summands is the dimension of the centre of \(F\), and the entries of \(\mathbf m\) are determined by \(F\) up to their order.

**Proof.** For \(F=0\), use the empty size vector; the centre and the number of summands both have dimension zero. Assume \(F\neq0\). Let \(Z\) be the centre of \(F\). It contains the unit \(1_F\) (Lemma 2.2(3)) and is a finite-dimensional commutative C\*-algebra. Choose mutually orthogonal minimal projections \(z_1,\dots,z_r\) of \(Z\) with \(r\) as large as possible (Lemma 2.2(2) in \(Z\)). Then \(\sum_iz_i=1_F\): otherwise \(1_F-\sum_iz_i\) is a nonzero projection of \(Z\), it dominates a minimal projection of \(Z\), and that projection is orthogonal to every \(z_i\).

Each \(z_iF\) is a C\*-subalgebra with unit \(z_i\), \(z_iF\cdot z_jF=0\) for \(i\neq j\), and \(x=\sum_iz_ix\). So \(x\mapsto(z_1x,\dots,z_rx)\) is an isomorphism of \(F\) onto \(z_1F\oplus\cdots\oplus z_rF\). If \(c\in z_iF\) commutes with \(z_iF\), it commutes with every \(x=\sum_jz_jx\), since \(cz_jx=0=z_jxc\) for \(j\neq i\). So \(c\in Z\) and \(c\in z_iZ\). By Lemma 2.2(1), \(z_iZ\) is spanned by projections below \(z_i\), which are \(0\) or \(z_i\) by minimality. So the centre of \(z_iF\) is \(\mathbb Cz_i\), and Lemma 2.3 gives \(z_iF\cong M_{m_i}\). Hence \(F\cong M_{\mathbf m}\).

The centre of \(M_k\) is \(\mathbb C1_k\), since a matrix that commutes with all \(e_{ab}\) is scalar. So the centre of \(M_{\mathbf m}\) consists of the elements \((\lambda_11_{m_1},\dots,\lambda_r1_{m_r})\); it has dimension \(r\), its minimal projections are \(z_1,\dots,z_r\), and \(z_iM_{\mathbf m}\cong M_{m_i}\) has dimension \(m_i^2\). An isomorphism carries centre to centre and minimal central projections to minimal central projections. So \(r\) and the numbers \(m_i\), up to order, are determined by \(F\). \(\square\)

**Lemma 2.5** (Projections of a multimatrix algebra). For projections \(p,q\in M_{\mathbf m}\) the following are equivalent: (i) \(\operatorname{rk}p=\operatorname{rk}q\); (ii) \(p\sim q\); (iii) \(q=upu^*\) for some \(u\in U(M_{\mathbf m})\). The rank vectors of the projections of \(M_{\mathbf m}\) are exactly the \(x\in\mathbb Z^r\) with \(0\leq x\leq\mathbf m\).

**Proof.** (i)⇒(iii). In each summand, the ranges of \(p_i\) and \(q_i\) have the same dimension, and so do their orthogonal complements. The unitary \(u_i\) of \(\mathbb C^{m_i}\) that carries an orthonormal basis of the range of \(p_i\) to one of the range of \(q_i\), and an orthonormal basis of the complement of the first range to one of the complement of the second, satisfies \(u_ip_iu_i^*=q_i\). (iii)⇒(ii). Put \(v=up\): then \(v^*v=p\) and \(vv^*=upu^*=q\). (ii)⇒(i). If \(v^*v=p\) and \(vv^*=q\), then \(v_i\) maps the range of \(p_i\) isometrically onto the range of \(q_i\), so the ranks agree. The last statement follows by looking at diagonal projections. \(\square\)

## 3. Homomorphisms between finite-dimensional C\*-algebras

A reference for this section is [Blackadar 1998, Section 7.2].

**Definition 3.1.** Let \(\mathbf m\in\mathbb N^r\), \(\mathbf n\in\mathbb N^s\), and let \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) be a \*-homomorphism. Write \(\varphi(x)=(\varphi_1(x),\dots,\varphi_s(x))\). The *multiplicity matrix* of \(\varphi\) is the \(s\times r\) matrix \(\alpha(\varphi)\) with entries
\[
\alpha(\varphi)_{ji}=\operatorname{Tr}\varphi_j\big(e^{(i)}_{11}\big),
\]
the number of times the \(i\)-th summand of \(M_{\mathbf m}\) enters the \(j\)-th summand of \(M_{\mathbf n}\). Its *defect vector* is \(d(\varphi)=\mathbf n-\alpha(\varphi)\mathbf m\).

**Theorem 3.2** (Homomorphisms between multimatrix algebras). Let \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) be a \*-homomorphism with multiplicity matrix \(\alpha=\alpha(\varphi)\).

1. For every projection \(p\in M_{\mathbf m}\),
\[
\operatorname{rk}\varphi(p)=\alpha\operatorname{rk}p .
\tag{3.1}
\]
In particular \(\alpha_{ji}=\operatorname{Tr}\varphi_j(e)\) for every minimal projection \(e\) of the \(i\)-th summand. If \(\psi:M_{\mathbf n}\to M_{\mathbf k}\) is another \*-homomorphism, then \(\alpha(\psi\circ\varphi)=\alpha(\psi)\alpha(\varphi)\).
2. \(\alpha\mathbf m\leq\mathbf n\), that is, \(d(\varphi)\geq0\), with equality if and only if \(\varphi\) is unital. The map \(\varphi\) is injective if and only if no column of \(\alpha\) is zero.
3. Conversely, let \(\alpha\) be any \(s\times r\) matrix with entries in \(\mathbb Z_+\) and \(\alpha\mathbf m\leq\mathbf n\), and put \(d=\mathbf n-\alpha\mathbf m\). The *standard homomorphism*
\[
\begin{gathered}
\varphi_\alpha(x)_j\\
=\operatorname{diag}\big(x_1^{(\alpha_{j1})},x_2^{(\alpha_{j2})},\\
\dots,x_r^{(\alpha_{jr})},0_{d_j}\big),\\
j=1,\dots,s,
\end{gathered}
\tag{3.2}
\]
is a \*-homomorphism with multiplicity matrix \(\alpha\).
4. There is \(u\in U(M_{\mathbf n})\) with \(\varphi=\operatorname{Ad}u\circ\varphi_\alpha\). Consequently two \*-homomorphisms \(M_{\mathbf m}\to M_{\mathbf n}\) are unitarily equivalent if and only if they have the same multiplicity matrix.

**Proof.** (1) Let \(e\) be a minimal projection of the \(i\)-th summand. There is a partial isometry \(w\) in that summand with \(w^*w=e^{(i)}_{11}\) and \(ww^*=e\). Then \(\varphi_j(w)\) is a partial isometry from \(\varphi_j(e^{(i)}_{11})\) onto \(\varphi_j(e)\), so these projections have the same rank (Lemma 2.5 in \(M_{n_j}\)). A projection \(p\) of \(M_{\mathbf m}\) is a sum of mutually orthogonal minimal projections, \(\operatorname{Tr}p_i\) of them in the \(i\)-th summand (diagonalize each \(p_i\)). Images of orthogonal projections are orthogonal projections, and rank is additive on orthogonal sums. So \(\operatorname{Tr}\varphi_j(p)=\sum_i\alpha_{ji}\operatorname{Tr}p_i\), which is (3.1). Applying (3.1) twice to \(p=e^{(i)}_{11}\) gives \(\operatorname{rk}\psi(\varphi(p))=\alpha(\psi)\alpha(\varphi)e_i\), the \(i\)-th column of \(\alpha(\psi)\alpha(\varphi)\).

(2) By (3.1) with \(p=1\), \(\operatorname{rk}\varphi(1)=\alpha\mathbf m\). A projection of \(M_{n_j}\) has rank at most \(n_j\), with equality only for \(1_{n_j}\). So \(\alpha\mathbf m\leq\mathbf n\), with equality exactly when \(\varphi(1)=1\). If the \(i\)-th column of \(\alpha\) is zero, then \(\varphi(e^{(i)}_{11})=0\) and \(\varphi\) is not injective. Suppose no column is zero, and let \(\varphi(x)=0\). If \(x\neq0\), some \(x_i\) has a nonzero entry \(\xi\) in position \((a,b)\). Then \(e^{(i)}_{1a}xe^{(i)}_{b1}=\xi e^{(i)}_{11}\), so \(\varphi(e^{(i)}_{11})=\xi^{-1}\varphi(e^{(i)}_{1a})\varphi(x)\varphi(e^{(i)}_{b1})=0\), and the \(i\)-th column of \(\alpha\) is zero, a contradiction.

(3) Each map \(x\mapsto x_i^{(b)}\) is a \*-homomorphism, and so is a block-diagonal combination of them. The block sizes in (3.2) add up to \(\sum_i\alpha_{ji}m_i+d_j=n_j\). The image of \(e^{(i)}_{11}\) in the \(j\)-th summand consists of \(\alpha_{ji}\) copies of a rank-one projection, so its trace is \(\alpha_{ji}\).

(4) Fix \(j\) and write \(\phi=\varphi_j:M_{\mathbf m}\to M_{n_j}=B(\mathbb C^{n_j})\). For each \(i\), choose an orthonormal basis \(\xi^{(i)}_1,\dots,\xi^{(i)}_{\alpha_{ji}}\) of the range of \(\phi(e^{(i)}_{11})\), and put
\[
\eta^{(i)}_{t,b}=\phi\big(e^{(i)}_{b1}\big)\xi^{(i)}_t,\qquad 1\leq t\leq\alpha_{ji},\ 1\leq b\leq m_i .
\]
These vectors are orthonormal: vectors with different \(i\) are orthogonal because \(e^{(i')}_{1c}e^{(i)}_{b1}=0\) for \(i\neq i'\), and
\[
\begin{gathered}
\big\langle\phi(e^{(i)}_{b1})\xi^{(i)}_t,\phi(e^{(i)}_{c1})\xi^{(i)}_u\big\rangle\\
=\big\langle\phi(e^{(i)}_{1c}e^{(i)}_{b1})\xi^{(i)}_t,\xi^{(i)}_u\big\rangle\\
=\delta_{bc}\big\langle\xi^{(i)}_t,\xi^{(i)}_u\big\rangle\\
=\delta_{bc}\delta_{tu}.
\end{gathered}
\]
The range of \(\phi(e^{(i)}_{bb})=\phi(e^{(i)}_{b1})\phi(e^{(i)}_{11})\phi(e^{(i)}_{1b})\) is the image of the range of \(\phi(e^{(i)}_{11})\) under \(\phi(e^{(i)}_{b1})\), so it is spanned by the \(\eta^{(i)}_{t,b}\) with this \(b\). Hence the \(\eta\)'s span the range of \(\phi(1)=\sum_{i,b}\phi(e^{(i)}_{bb})\). Complete them by an orthonormal basis \(\zeta_1,\dots,\zeta_{d_j}\) of the orthogonal complement of that range, where \(d_j=n_j-\sum_i\alpha_{ji}m_i\). Order the basis as follows: for \(i=1,\dots,r\) and \(t=1,\dots,\alpha_{ji}\), the block \(\eta^{(i)}_{t,1},\dots,\eta^{(i)}_{t,m_i}\); then \(\zeta_1,\dots,\zeta_{d_j}\). We have \(\phi(e^{(i)}_{bc})\eta^{(i)}_{t,c'}=\phi(e^{(i)}_{bc}e^{(i)}_{c'1})\xi^{(i)}_t=\delta_{cc'}\eta^{(i)}_{t,b}\), \(\phi(e^{(i)}_{bc})\eta^{(i')}_{t,c'}=0\) for \(i'\neq i\), and \(\phi(y)\zeta_l=\phi(y)\phi(1)\zeta_l=0\) for every \(y\). So in this basis \(\phi(x)\) is the matrix \(\varphi_\alpha(x)_j\) of (3.2). If \(U_j\) is the unitary that carries the standard basis of \(\mathbb C^{n_j}\) to this ordered basis, then \(\varphi_j=\operatorname{Ad}U_j\circ(\varphi_\alpha)_j\). Put \(u=(U_1,\dots,U_s)\).

If \(\alpha(\varphi)=\alpha(\psi)=\alpha\), then \(\varphi=\operatorname{Ad}u\circ\varphi_\alpha\) and \(\psi=\operatorname{Ad}v\circ\varphi_\alpha\), so \(\psi=\operatorname{Ad}(vu^*)\circ\varphi\). Conversely, conjugation by a unitary preserves ranks. \(\square\)

**Remark 3.3** (Representations). Take \(s=1\): a \*-homomorphism \(\pi:M_{\mathbf m}\to M_N=B(\mathbb C^N)\) is a representation of \(M_{\mathbf m}\) on \(\mathbb C^N\). Its multiplicity matrix is a row \((a_1,\dots,a_r)\), and by Theorem 3.2(4), after a unitary change of basis,
\[
\begin{gathered}
\mathbb C^N\\
=\bigoplus_i\mathbb C^{m_i}\otimes\mathbb C^{a_i}\ \oplus\ \mathbb C^{d},\\
\pi(x)\\
=\bigoplus_ix_i\otimes1\ \oplus\ 0_d ,
\end{gathered}
\]
with \(d=N-\sum_ia_im_i\). The representation is unital exactly when \(d=0\), and faithful exactly when every \(a_i\geq1\). A unital representation has no invariant subspaces other than \(0\) and \(\mathbb C^N\) exactly when one \(a_i\) equals \(1\) and the others vanish: every subspace \(\mathbb C^{m_i}\otimes f\) with \(f\in\mathbb C^{a_i}\) is invariant, and conversely \(\mathbb C^{m_i}\) with \(x\mapsto x_i\) has no nontrivial invariant subspace. This also accounts for irreducible representations on arbitrary Hilbert spaces. For a nonzero irreducible \(\pi\), the projection \(\pi(1)\) must be \(1_H\), since its range and kernel reduce \(\pi\), and the representation is nonzero. The central projections \(\pi(z_i)\) then show that exactly one summand acts. In that summand choose a nonzero \(\xi\in\pi(e_{11})H\): some \(\pi(e_{aa})\) has nonzero range, and \(\pi(e_{1a})\) carries it isometrically to \(\pi(e_{11})H\). The vectors \(\pi(e_{a1})\xi/\|\xi\|\), \(1\leq a\leq m_i\), are orthonormal by the calculation above. Their finite-dimensional span is invariant under every matrix unit and its adjoint, so irreducibility makes it all of \(H\). Thus the irreducible representations of \(M_{\mathbf m}\) are, up to unitary equivalence, the \(r\) maps \(x\mapsto x_i\) on \(\mathbb C^{m_i}\).

**Remark 3.4** (Changing the identification). If \(F\) is a finite-dimensional C\*-algebra and \(\iota,\iota':F\to M_{\mathbf m}\) are two isomorphisms, then \(\beta=\iota'\circ\iota^{-1}\) is an automorphism of \(M_{\mathbf m}\). It maps minimal projections to minimal projections, so each column of \(\alpha(\beta)\) has a single entry \(1\) and the others \(0\). By Theorem 3.2(1), \(\alpha(\beta^{-1})\alpha(\beta)=\alpha(\mathrm{id})\) is the identity matrix, so \(\alpha(\beta)\) is invertible, and it is a permutation matrix. So rank vectors and multiplicity matrices computed through \(\iota\) and \(\iota'\) differ only by a consistent relabelling of the summands. We may therefore speak of the summands, rank vectors and multiplicity matrices of finite-dimensional C\*-algebras without naming the identification.

**Definition 3.5** (Bratteli diagram of a homomorphism). The *Bratteli diagram* of \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) is the graph with \(r\) vertices on the left, labelled \(m_1,\dots,m_r\), and \(s\) vertices on the right, labelled \(n_1,\dots,n_s\), in which the \(i\)-th left vertex and the \(j\)-th right vertex are joined by \(\alpha(\varphi)_{ji}\) edges. By Theorem 3.2(4) it determines \(\varphi\) up to unitary equivalence.

**Example 3.6.** (a) Let \(\mathbf m=(1,2)\), \(\mathbf n=(5,4)\) and \(\alpha=\begin{pmatrix}3&1\\0&2\end{pmatrix}\). Then \(\alpha\mathbf m=(5,4)^T=\mathbf n\), so the standard homomorphism
\[
\begin{gathered}
\varphi_\alpha(\lambda,y)\\
=\big(\operatorname{diag}(\lambda,\lambda,\lambda,y),\ \operatorname{diag}(y,y)\big),\\
\lambda\in\mathbb C,\ y\in M_2,
\end{gathered}
\]
is unital and injective. In its diagram, the left vertex \(1\) is joined to the right vertex \(5\) by three edges, and the left vertex \(2\) is joined to \(5\) by one edge and to \(4\) by two edges.

(b) The map \(M_2\to M_5\), \(x\mapsto\operatorname{diag}(x,x,0)\), has multiplicity matrix \((2)\) and defect \((1)\): it is injective and not unital. The map \(\mathbb C^2\to\mathbb C\), \((\lambda,\mu)\mapsto\lambda\), has multiplicity matrix \((1\ \ 0)\): its second column is zero, and it is not injective.

(c) The two maps \(M_2\to M_4\) given by \(x\mapsto\operatorname{diag}(x,x)\) and by \(x\mapsto\begin{pmatrix}x_{11}1_2&x_{12}1_2\\x_{21}1_2&x_{22}1_2\end{pmatrix}\) both have multiplicity matrix \((2)\). By Theorem 3.2(4) they are unitarily equivalent; here the unitary is the permutation matrix that exchanges the second and third basis vectors.

## 4. Inductive limits and AF-algebras

A reference for inductive limits is [Blackadar 2017, II.8.2].

**Definition 4.1.** An *inductive sequence* \((A_n,\varphi_n)_{n\geq1}\) consists of C\*-algebras \(A_n\) and \*-homomorphisms \(\varphi_n:A_n\to A_{n+1}\). For \(m>n\) put \(\varphi_{m,n}=\varphi_{m-1}\circ\cdots\circ\varphi_n:A_n\to A_m\), and \(\varphi_{n,n}=\mathrm{id}\). An *inductive limit* of the sequence is a C\*-algebra \(A\) with \*-homomorphisms \(\varphi_{\infty,n}:A_n\to A\) such that

1. \(\varphi_{\infty,n+1}\circ\varphi_n=\varphi_{\infty,n}\) for all \(n\);
2. \(\bigcup_n\varphi_{\infty,n}(A_n)\) is dense in \(A\);
3. \(\|\varphi_{\infty,n}(a)\|=\lim_{m\to\infty}\|\varphi_{m,n}(a)\|\) for all \(n\) and \(a\in A_n\).

The limit in (3) exists, because \(\|\varphi_{m+1,n}(a)\|=\|\varphi_m(\varphi_{m,n}(a))\|\leq\|\varphi_{m,n}(a)\|\) by Section 1(a).

**Proposition 4.2.** Let \((A_n,\varphi_n)\) be an inductive sequence.

1. It has an inductive limit.
2. (*Universal property.*) Let \((A,\varphi_{\infty,n})\) be an inductive limit, \(B\) a C\*-algebra and \(\sigma_n:A_n\to B\) \*-homomorphisms with \(\sigma_{n+1}\circ\varphi_n=\sigma_n\). There is exactly one \*-homomorphism \(\sigma:A\to B\) with \(\sigma\circ\varphi_{\infty,n}=\sigma_n\) for all \(n\).
3. If \((A,\varphi_{\infty,n})\) and \((A',\varphi'_{\infty,n})\) are inductive limits, there is exactly one isomorphism \(\theta:A\to A'\) with \(\theta\circ\varphi_{\infty,n}=\varphi'_{\infty,n}\) for all \(n\).
4. If every \(\varphi_n\) is injective, then every \(\varphi_{\infty,n}\) is isometric, and \(A\) is the closure of the increasing union of the subalgebras \(\varphi_{\infty,n}(A_n)\cong A_n\).

**Proof.** (1) Let \(\Pi\) be the set of bounded sequences \((a_k)_{k\geq1}\) with \(a_k\in A_k\). With coordinatewise operations and the norm \(\sup_k\|a_k\|\) it is a C\*-algebra. To prove completeness, let \(a^{(n)}\) be Cauchy in this norm. Each coordinate converges in the complete algebra \(A_k\), to \(a_k\). The Cauchy estimate, passed to the limit in each coordinate, gives \(\sup_k\|a_k-a_k^{(n)}\|\leq\varepsilon\) for all sufficiently large \(n\). The limit sequence is bounded because one fixed bounded \(a^{(n)}\) is within a uniform finite distance of it. Multiplication and adjoints act coordinatewise, and
\[
\|a^*a\|=\sup_k\|a_k^*a_k\|=\sup_k\|a_k\|^2=\|a\|^2.
\]
The sequences with \(\|a_k\|\to0\) form a two-sided \(*\)-ideal \(J\): products with bounded sequences still tend to zero. It is closed, since a uniform limit of sequences tending to zero also tends to zero, by first choosing a uniformly close sequence and then its small tail. So \(Q=\Pi/J\) is a C\*-algebra (Section 1(e)). The quotient norm of the class of \((b_k)\) is \(\limsup_k\|b_k\|\): for \((c_k)\in J\), \(\sup_k\|b_k+c_k\|\geq\limsup_k\|b_k\|\), and subtracting the first \(K\) terms shows that the class has norm at most \(\sup_{k\geq K}\|b_k\|\) for every \(K\). Define \(\varphi_{\infty,n}(a)\) as the class of the sequence whose \(k\)-th term is \(0\) for \(k<n\) and \(\varphi_{k,n}(a)\) for \(k\geq n\). This is a \*-homomorphism. The sequences for \(\varphi_{\infty,n+1}(\varphi_n(a))\) and \(\varphi_{\infty,n}(a)\) differ only in the \(n\)-th term, so condition (1) holds, and the formula for the quotient norm gives (3). The images \(\varphi_{\infty,n}(A_n)\) increase with \(n\) by (1), so their union is a \*-subalgebra, and its closure \(A\) is a C\*-algebra that satisfies (2).

(2) Define \(\sigma\) on \(A_0=\bigcup_n\varphi_{\infty,n}(A_n)\) by \(\sigma(\varphi_{\infty,n}(a))=\sigma_n(a)\). For \(m\geq n\), \(\|\sigma_n(a)\|=\|\sigma_m(\varphi_{m,n}(a))\|\leq\|\varphi_{m,n}(a)\|\), so \(\|\sigma_n(a)\|\leq\|\varphi_{\infty,n}(a)\|\). If \(\varphi_{\infty,n}(a)=\varphi_{\infty,n'}(a')\), then at a stage \(m\geq n,n'\) the element \(b=\varphi_{m,n}(a)-\varphi_{m,n'}(a')\) has \(\varphi_{\infty,m}(b)=0\), hence \(\sigma_m(b)=0\), that is, \(\sigma_n(a)=\sigma_{n'}(a')\). So \(\sigma\) is well defined on \(A_0\). It is a contractive \*-homomorphism (compute at a common stage), so it extends by continuity to \(A\). Uniqueness holds because \(A_0\) is dense.

(3) Part (2) gives \*-homomorphisms \(\theta:A\to A'\) and \(\theta':A'\to A\) compatible with the maps. Then \(\theta'\theta\) and \(\theta\theta'\) are the identity on dense subsets, hence everywhere.

(4) Injective \*-homomorphisms are isometric (Section 1(a)), so \(\|\varphi_{m,n}(a)\|=\|a\|\) for all \(m\), and \(\|\varphi_{\infty,n}(a)\|=\|a\|\) by (3) of the definition. \(\square\)

We write \(\varinjlim(A_n,\varphi_n)\) for the inductive limit. If \(A_1\subseteq A_2\subseteq\cdots\) are C\*-subalgebras of a C\*-algebra \(A\) with dense union, then \(A\), with the inclusion maps, is an inductive limit of the sequence \((A_n)\) with the inclusions as connecting maps: condition (3) holds because inclusions are isometric.

**Example 4.3** (Condition (3) matters). Let \(A_n=C_0([n,\infty))\) and let \(\varphi_n\) be restriction to \([n+1,\infty)\). Every \(\varphi_n\) is onto and every \(A_n\) is nonzero. For \(a\in A_n\), \(\|\varphi_{m,n}(a)\|=\sup_{t\geq m}|a(t)|\to0\), because \(a\) vanishes at infinity. So \(\varphi_{\infty,n}=0\) for every \(n\), and the inductive limit is the zero algebra.

**Lemma 4.4** (Ladders). Let \((A_n,\varphi_n)\) and \((B_n,\psi_n)\) be inductive sequences with limits \(A\) and \(B\), and let \(\theta_n:A_n\to B_n\) be \*-homomorphisms with \(\theta_{n+1}\circ\varphi_n=\psi_n\circ\theta_n\). There is exactly one \*-homomorphism \(\theta:A\to B\) with \(\theta\circ\varphi_{\infty,n}=\psi_{\infty,n}\circ\theta_n\) for all \(n\). If every \(\theta_n\) is an isomorphism, so is \(\theta\).

**Proof.** The maps \(\sigma_n=\psi_{\infty,n}\circ\theta_n\) satisfy \(\sigma_{n+1}\varphi_n=\psi_{\infty,n+1}\psi_n\theta_n=\psi_{\infty,n}\theta_n=\sigma_n\), so Proposition 4.2(2) gives \(\theta\). If the \(\theta_n\) are isomorphisms, the relations \(\varphi_n\circ\theta_n^{-1}=\theta_{n+1}^{-1}\circ\psi_n\) give in the same way \(\eta:B\to A\) with \(\eta\circ\psi_{\infty,n}=\varphi_{\infty,n}\circ\theta_n^{-1}\). Then \(\eta\theta\) and \(\theta\eta\) are the identity on dense subsets, hence everywhere. \(\square\)

The next theorem says that conjugating the connecting maps by unitaries does not change the limit. We state it without assuming units or injectivity.

**Theorem 4.5** (Unitary perturbation of the connecting maps). Let \((A_n,\varphi_n)\) be an inductive sequence, and for each \(n\geq2\) let \(u_n\) be a unitary of \(A_n^+\). Put \(\varphi_n'=\operatorname{Ad}u_{n+1}\circ\varphi_n\). Define unitaries \(w_n\in A_n^+\) by
\[
\begin{gathered}
w_1\\
=1,\\
w_{n+1}\\
=u_{n+1}\,\varphi_n^+(w_n).
\end{gathered}
\tag{4.1}
\]
Then \(\operatorname{Ad}w_{n+1}\circ\varphi_n=\varphi_n'\circ\operatorname{Ad}w_n\) for every \(n\). Consequently there is an isomorphism \(\theta:\varinjlim(A_n,\varphi_n)\to\varinjlim(A_n,\varphi_n')\) with \(\theta\circ\varphi_{\infty,n}=\varphi'_{\infty,n}\circ\operatorname{Ad}w_n\).

**Proof.** The element \(w_{n+1}\) is a product of unitaries of \(A_{n+1}^+\), because \(\varphi_n^+\) is a unital \*-homomorphism. For \(x\in A_n\), the element \(w_nxw_n^*\) lies in the ideal \(A_n\), and
\[
\begin{gathered}
\varphi_n'(w_nxw_n^*)\\
=u_{n+1}\varphi_n^+(w_n)\varphi_n(x)\varphi_n^+(w_n)^*u_{n+1}^*\\
=w_{n+1}\varphi_n(x)w_{n+1}^* .
\end{gathered}
\]
So the automorphisms \(\theta_n=\operatorname{Ad}w_n\) of \(A_n\) satisfy \(\theta_{n+1}\circ\varphi_n=\varphi_n'\circ\theta_n\), and Lemma 4.4 gives \(\theta\). \(\square\)

**Remark 4.6** (The unital case). Suppose every \(A_n\) has a unit \(1_n\) and \(u_{n+1}\in U(A_{n+1})\); the maps \(\varphi_n\) need not be unital. A unitary \(u\) of \(A_{n+1}\) and the unitary \(u+(1-1_{n+1})\) of \(A_{n+1}^+\) induce the same automorphism of \(A_{n+1}\). Use the latter in (4.1). By induction, the unitaries of (4.1) then have the form \(w_n+(1-1_n)\), where \(w_n\in U(A_n)\) is given by
\[
\begin{gathered}
w_1\\
=1_1,\\
w_{n+1}\\
=u_{n+1}\big(\varphi_n(w_n)+1_{n+1}-\varphi_n(1_n)\big);
\end{gathered}
\]
to see this, expand \(\big(u_{n+1}+1-1_{n+1}\big)\big(\varphi_n(w_n)+1-\varphi_n(1_n)\big)\), using \(u_{n+1}(1-1_{n+1})=0\), \((1-1_{n+1})\varphi_n(w_n)=0\) and \(\varphi_n(1_n)\leq1_{n+1}\). One can also check directly that \(v=\varphi_n(w_n)+1_{n+1}-\varphi_n(1_n)\) is a unitary of \(A_{n+1}\) (the sum of a unitary of the corner \(\varphi_n(1_n)A_{n+1}\varphi_n(1_n)\) and the complementary projection) and that \(v\varphi_n(x)v^*=\varphi_n(w_nxw_n^*)\). So conjugating by \(w_n\) intertwines \(\varphi_n\) and \(\varphi_n'\) inside the unital algebras \(A_n\).

**Definition 4.7.** A C\*-algebra \(A\) is an *AF-algebra* if it contains an increasing sequence \(A_1\subseteq A_2\subseteq\cdots\) of finite-dimensional C\*-subalgebras whose union is dense. Such a sequence is a *generating sequence* of \(A\), and the \*-subalgebra \(A_\infty=\bigcup_kA_k\) is its *local algebra*.

*Reference:* [Bratteli 1972].

**Proposition 4.8.**

1. The inductive limit of any inductive sequence of finite-dimensional C\*-algebras is an AF-algebra.
2. An AF-algebra is separable.
3. If \(A\) is a unital AF-algebra with generating sequence \((A_k)\), then \(1_A\in A_k\) for all large \(k\). So every unital AF-algebra has a generating sequence of C\*-subalgebras that contain \(1_A\).

**Proof.** (1) The images \(\varphi_{\infty,n}(A_n)\) are finite-dimensional \*-subalgebras, hence closed; they increase, and their union is dense. (2) Rational combinations of bases of the \(A_k\) form a countable dense set. (3) Choose \(k\) and a self-adjoint \(a\in A_k\) with \(\|1_A-a\|<1\) (replace an approximant \(b\) by \((b+b^*)/2\)). Let \(1_k\) be the unit of \(A_k\) (Lemma 2.2(3)). Since \(a(1_A-1_k)=0\),
\[
1_A-1_k=(1_A-1_k)(1_A-a)(1_A-1_k),
\]
so \(\|1_A-1_k\|<1\). A nonzero projection has norm one, so \(1_A=1_k\in A_k\), and then \(1_A\in A_l\) for all \(l\geq k\). \(\square\)

By Theorem 2.4, each member of a generating sequence is isomorphic to a multimatrix algebra. So an AF-algebra is described by a sequence of size vectors and multiplicity matrices.

**Definition 4.9** (Bratteli diagram of a sequence). Let \((A_k)\) be a generating sequence of an AF-algebra, with \(A_k\cong M_{\mathbf m(k)}\), \(\mathbf m(k)\in\mathbb N^{r_k}\), and let \(\alpha_k\) be the multiplicity matrix of the inclusion \(A_k\subseteq A_{k+1}\) (an \(r_{k+1}\times r_k\) matrix). The *Bratteli diagram* of the sequence has, at level \(k\), one vertex for each summand of \(A_k\), labelled by its size, and \((\alpha_k)_{ji}\) edges between the \(i\)-th vertex at level \(k\) and the \(j\)-th vertex at level \(k+1\). The same definition applies to any inductive sequence of multimatrix algebras. We write \(\alpha_{l,k}=\alpha_{l-1}\cdots\alpha_k\) for \(l>k\) and \(\alpha_{k,k}=1\).

**Corollary 4.10** (The diagram determines the algebra). Let \((M_{\mathbf m(k)},\varphi_k)\) and \((M_{\mathbf m(k)},\varphi'_k)\) be inductive sequences with the same size vectors and with \(\alpha(\varphi_k)=\alpha(\varphi'_k)\) for all \(k\). Then their inductive limits are isomorphic. Conversely, for every sequence of size vectors \(\mathbf m(k)\) and matrices \(\alpha_k\) with entries in \(\mathbb Z_+\) and \(\alpha_k\mathbf m(k)\leq\mathbf m(k+1)\), the standard homomorphisms \(\varphi_{\alpha_k}\) form an inductive sequence with these multiplicity matrices; its limit is an AF-algebra, and the connecting maps are injective exactly when no \(\alpha_k\) has a zero column.

**Proof.** By Theorem 3.2(4), \(\varphi'_k=\operatorname{Ad}u_{k+1}\circ\varphi_k\) with \(u_{k+1}\in U(M_{\mathbf m(k+1)})\). By Remark 4.6 and Theorem 4.5 the limits are isomorphic. The converse follows from Theorem 3.2(2) and (3) and Proposition 4.8(1). \(\square\)

## 5. First examples

**Example 5.1** (Compact operators). Let \(H\) be a Hilbert space with a countably infinite orthonormal basis \((\varepsilon_i)_{i\geq1}\), let \(P_n\) be the projection onto the span of \(\varepsilon_1,\dots,\varepsilon_n\), and let \(\mathcal K\) be the C\*-algebra of compact operators on \(H\). The algebras \(A_n=P_nB(H)P_n\cong M_n\) increase. Their union is dense in \(\mathcal K\): for compact \(T\), Section 1(h) gives
\[
\begin{gathered}
\|T-P_nTP_n\|\\
\leq\|T-P_nT\|+\|P_n\|\,\|(T^*-P_nT^*)^*\|\to0 .
\end{gathered}
\]
So \(\mathcal K\) is an AF-algebra. The inclusion \(A_n\subseteq A_{n+1}\) is \(x\mapsto\operatorname{diag}(x,0)\): its multiplicity matrix is \((1)\) and its defect is \((1)\). The Bratteli diagram has one vertex at each level, labelled \(n\) at level \(n\), with single edges between consecutive levels.

**Example 5.2** (The unitization of the compact operators). The C\*-algebra \(\mathcal K+\mathbb C1\subseteq B(H)\) is isomorphic to \(\mathcal K^+\): the map \(k+\lambda1\mapsto k+\lambda1_H\) is an injective \*-homomorphism (\(1_H\notin\mathcal K\)), hence an isomorphism onto its image (Section 1(a)). The algebras
\[
A_n=P_nB(H)P_n+\mathbb C(1-P_n)\cong M_n\oplus\mathbb C
\]
increase and contain \(1_H\), and their union is dense in \(\mathcal K+\mathbb C1\), since \(k+\lambda1\) is the limit of \(P_nkP_n+\lambda1\in A_n\). The inclusion \(A_n\subseteq A_{n+1}\) is \((x,\lambda)\mapsto(\operatorname{diag}(x,\lambda),\lambda)\). With the summands ordered as \((M_n,\mathbb C)\), its multiplicity matrix is
\[
\alpha_n=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad \alpha_n\binom n1=\binom{n+1}1 ,
\]
so the inclusions are unital. In the Bratteli diagram, level \(n\) has two vertices, labelled \(n\) and \(1\); the vertex \(n\) is joined to the vertex \(n+1\) of the next level, and the vertex \(1\) is joined both to the vertex \(1\) and to the vertex \(n+1\) of the next level.

**Example 5.3** (UHF algebras). Let \(k_1,k_2,\dots\) be integers \(\geq2\), put \(d_1=1\) and \(d_{n+1}=k_1k_2\cdots k_n\), and let \(A_n=M_{d_n}\) with the unital connecting maps \(x\mapsto x^{(k_n)}\) of multiplicity \(k_n\). The limit is the *UHF algebra of type \((k_n)\)*; its Bratteli diagram has one vertex at each level, labelled \(d_n\), and \(k_n\) edges between levels \(n\) and \(n+1\). When every \(k_n=2\) we get the *CAR algebra*. Identify \(M_{d_n}=M_{2^{n-1}}\) with the tensor product of \(n-1\) copies of \(M_2\) (for \(n=1\), with \(\mathbb C\)). The map \(x\mapsto x\otimes1\) into the tensor product of \(n\) copies has multiplicity \(2\), so by Corollary 4.10 the CAR algebra is also the limit of the tensor powers of \(M_2\) under \(x\mapsto x\otimes1\): it is the infinite tensor product \(M_2\otimes M_2\otimes\cdots\).

For a C\*-algebra \(A\), let \(M_\infty(A)=\bigcup_nM_n(A)\), where \(M_n(A)\) sits in \(M_{n+1}(A)\) as the upper left corner, \(x\mapsto\operatorname{diag}(x,0)\). This inclusion is an injective \*-homomorphism of C\*-algebras (Section 1(f)), hence isometric, so \(M_\infty(A)\) carries a norm. The completion lemma in Section 1(i) gives its Banach completion. Products and adjoints extend to it: for Cauchy sequences \(a_n,b_n\), their boundedness and
\[
\begin{gathered}
\|a_nb_n-a_mb_m\|\\
\leq\|a_n\|\,\|b_n-b_m\|+\|a_n-a_m\|\,\|b_m\|
\end{gathered}
\]
show that \(a_nb_n\) is Cauchy and its class is independent of the approximants; adjoints are isometric. Associativity and the \(C^*\)-identity pass to the limit. Thus the completion is a \(C^*\)-algebra, called the *stable algebra* \(A\otimes\mathcal K\) [Blackadar 2017, II.6.6.11]; it is an inductive limit of the sequence \((M_n(A))\) under the corner inclusions.

**Proposition 5.4** (Matrices and stabilization). Let \(A\) be an AF-algebra with generating sequence \((A_k)\), \(A_k\cong M_{\mathbf m(k)}\), and multiplicity matrices \(\alpha_k\).

1. For each \(n\), \(M_n(A)\) is an AF-algebra with generating sequence \((M_n(A_k))_k\), \(M_n(A_k)\cong M_{n\mathbf m(k)}\), and the multiplicity matrices are again the \(\alpha_k\).
2. \(A\otimes\mathcal K\) is an AF-algebra with generating sequence \((M_k(A_k))_k\), \(M_k(A_k)\cong M_{k\mathbf m(k)}\), and the multiplicity matrices are again the \(\alpha_k\).

**Proof.** \(M_n(M_{\mathbf m})=\bigoplus_iM_n(M_{m_i})\cong M_{n\mathbf m}\), with the same summands. A minimal projection of the \(i\)-th summand of \(M_n(A_k)\) is equivalent to \(\operatorname{diag}(e,0,\dots,0)\) with \(e\) minimal in the \(i\)-th summand of \(A_k\), and the rank vector of \(\operatorname{diag}(e,0,\dots,0)\) in \(M_n(A_{k+1})\), or in \(M_{k+1}(A_{k+1})\), is the rank vector of \(e\) in \(A_{k+1}\), the \(i\)-th column of \(\alpha_k\). This gives the multiplicity matrices. Density: by the estimate in Section 1(f), every \(x\in M_n(A)\) is a limit of matrices with entries in \(A_k\), \(k\to\infty\); and \(M_n(A_k)\subseteq M_k(A_k)\) for \(k\geq n\), while \(\bigcup_nM_n(A)\) is dense in \(A\otimes\mathcal K\). \(\square\)

**Remark 5.5** (Spatial tensor products). Let \(A\subseteq B(H_A)\) be faithfully represented (Section 1(g)), and let \(\mathcal K=\mathcal K(\ell^2)\) with matrix units \(e_{ij}\) for the standard basis. On \(H_A\otimes\ell^2=\bigoplus_{i\geq1}H_A\), the operator \(a\otimes e_{ij}\) is the infinite matrix with the single entry \(a\) in position \((i,j)\). The spatial tensor product \(A\otimes_{\min}\mathcal K\) is the closed linear span of the operators \(a\otimes k\), \(a\in A\), \(k\in\mathcal K\). The direct-sum identification follows from the tensor basis in Section 1(i). Under it, \(a\otimes1\) acts by \(a\) on every coordinate, so it is bounded with norm at most \(\|a\|\). Exchanging the two factors gives a unitary, because it sends the tensor orthonormal basis to the exchanged basis; in that identification \(1\otimes k\) acts by \(k\) on every coordinate, with norm at most \(\|k\|\). On elementary tensors their product is \(a\otimes k\), so density gives the same identity everywhere. Since \(\|a\otimes k\|\leq\|a\|\,\|k\|\) and the \(e_{ij}\) span a dense subspace of \(\mathcal K\) (Example 5.1), this closed span is the closure of the span of the \(a\otimes e_{ij}\), that is, the closure of \(\bigcup_nM_n(A)\) acting on \(H_A^n\subseteq H_A\otimes\ell^2\). On \(M_n(A)\) the operator norm is its C\*-norm, the only one (Section 1(a)). So \(A\otimes_{\min}\mathcal K\) is an inductive limit of the sequence \((M_n(A))\), that is, it is \(A\otimes\mathcal K\), whatever the faithful representation. The same holds with \(\mathcal K(H)\) whenever \(H\) has a countably infinite orthonormal basis, since then \(H\cong\ell^2\).

## 6. The scaled dimension group

**Definition 6.1.** An *ordered abelian group* \((G,G^+)\) is an abelian group \(G\) with a subset \(G^+\) such that \(G^++G^+\subseteq G^+\), \(G^+\cap(-G^+)=\{0\}\) and \(G=G^+-G^+\). We write \(g\leq h\) if \(h-g\in G^+\). A *scaled ordered group* \((G,G^+,\Sigma)\) is an ordered abelian group with a subset \(\Sigma\subseteq G^+\), the *scale*. A *homomorphism* \(h:(G,G^+,\Sigma)\to(H,H^+,\Sigma')\) is a group homomorphism with \(h(G^+)\subseteq H^+\) and \(h(\Sigma)\subseteq\Sigma'\); an *isomorphism* is a bijective homomorphism whose inverse is a homomorphism, that is, \(h(G^+)=H^+\) and \(h(\Sigma)=\Sigma'\).

The multimatrix algebra \(M_{\mathbf m}\) gives the scaled ordered group \((\mathbb Z^r,\mathbb Z^r_+,\Sigma_{\mathbf m})\) with
\[
\Sigma_{\mathbf m}=\{x\in\mathbb Z^r:0\leq x\leq\mathbf m\},
\]
the set of rank vectors of projections of \(M_{\mathbf m}\) (Lemma 2.5). A \*-homomorphism \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) gives the homomorphism \(x\mapsto\alpha(\varphi)x\) of scaled ordered groups: it maps \(\mathbb Z^r_+\) into \(\mathbb Z^s_+\), and \(\Sigma_{\mathbf m}\) into \(\Sigma_{\mathbf n}\) because \(\alpha(\varphi)\mathbf m\leq\mathbf n\). By (3.1) it sends the rank vector of \(p\) to the rank vector of \(\varphi(p)\).

**Definition 6.2** (Scaled dimension group of a generating sequence). Let \(A\) be an AF-algebra with a generating sequence \((A_k)\), \(A_k\cong M_{\mathbf m(k)}\) with \(\mathbf m(k)\in\mathbb N^{r_k}\), and multiplicity matrices \(\alpha_k\). Let \(G\) be the direct limit of the groups \(\mathbb Z^{r_k}\) under the maps \(\alpha_k\): its elements are the classes \(\alpha_{\infty,k}(x)\) of pairs \((k,x)\), \(x\in\mathbb Z^{r_k}\), where \((k,x)\) and \((l,y)\) define the same class if \(\alpha_{N,k}x=\alpha_{N,l}y\) for some \(N\geq k,l\); addition is computed at a common stage. Put
\[
G^+=\bigcup_k\alpha_{\infty,k}\big(\mathbb Z^{r_k}_+\big),\qquad \Sigma=\bigcup_k\alpha_{\infty,k}\big(\Sigma_{\mathbf m(k)}\big).
\]
The triple \((G,G^+,\Sigma)\) is the *scaled dimension group* of the sequence. For a projection \(p\in A_k\) we write \([p]=\alpha_{\infty,k}(\operatorname{rk}p)\); by (3.1) this does not depend on \(k\).

By Remark 3.4, other identifications \(A_k\cong M_{\mathbf m(k)}\) change the triple only by an isomorphism. Section 7 shows that it does not depend on the generating sequence either.

**Lemma 6.3.** In the setting of Definition 6.2:

1. \((G,G^+)\) is an ordered abelian group.
2. If \(0\neq x\in\mathbb Z^{r_k}_+\), then \(\alpha_{\infty,k}(x)\neq0\).
3. \(\alpha_{\infty,k}(x)\in G^+\) if and only if \(\alpha_{l,k}x\geq0\) for some \(l\geq k\); and \(\alpha_{\infty,k}(x)\in\Sigma\) if and only if \(\alpha_{l,k}x\in\Sigma_{\mathbf m(l)}\) for some \(l\geq k\).
4. The scale is *hereditary*: if \(g\in G\), \(h\in\Sigma\) and \(0\leq g\leq h\), then \(g\in\Sigma\).
5. If \(A\) is unital and \(1_A\in A_k\) for all \(k\), then \([1_A]=\alpha_{\infty,k}(\mathbf m(k))\) for every \(k\), and \(\Sigma=\{g\in G:0\leq g\leq[1_A]\}\).
6. For the generating sequence \((M_k(A_k))\) of \(A\otimes\mathcal K\) (Proposition 5.4), the group and positive cone are those of \((A_k)\), and the scale is the whole positive cone.

**Proof.** The matrices \(\alpha_k\) have entries in \(\mathbb Z_+\), so they preserve \(\geq0\), and they map \(\Sigma_{\mathbf m(k)}\) into \(\Sigma_{\mathbf m(k+1)}\).

(3) If \(\alpha_{\infty,k}(x)=\alpha_{\infty,k'}(y)\) with \(y\geq0\) (respectively \(y\in\Sigma_{\mathbf m(k')}\)), then \(\alpha_{N,k}x=\alpha_{N,k'}y\) for some \(N\), and the right side is \(\geq0\) (respectively in \(\Sigma_{\mathbf m(N)}\)). The converse is clear.

(1) Sums of positive elements are positive (add at a common stage), and \(x=x_+-x_-\) with \(x_\pm\geq0\) at every stage, so \(G=G^+-G^+\). If \(g=\alpha_{\infty,k}(x)\) and \(-g\) are both positive, then by (3) there is a stage \(l\) with \(\alpha_{l,k}x\geq0\) and \(-\alpha_{l,k}x\geq0\); so \(\alpha_{l,k}x=0\) and \(g=0\).

(2) The inclusions are injective, so no \(\alpha_k\) has a zero column (Theorem 3.2(2)). If \(y\geq0\) and \(y_i>0\), choose \(j\) with \((\alpha_k)_{ji}>0\); then \((\alpha_ky)_j\geq(\alpha_k)_{ji}y_i>0\). By induction \(\alpha_{l,k}x\neq0\) for all \(l\geq k\), so \((k,x)\) is not equivalent to \((k,0)\).

(4) Write \(g=\alpha_{\infty,k}(x)\) and \(h=\alpha_{\infty,k}(y)\) at a common stage. By (3), after moving to a later stage \(l\), we have \(\alpha_{l,k}y\in\Sigma_{\mathbf m(l)}\), \(\alpha_{l,k}x\geq0\) and \(\alpha_{l,k}(y-x)\geq0\). Then \(0\leq\alpha_{l,k}x\leq\alpha_{l,k}y\leq\mathbf m(l)\), so \(g\in\Sigma\).

(5) \(\operatorname{rk}1_A=\mathbf m(k)\) in \(A_k\), and the inclusions are unital, so \(\alpha_k\mathbf m(k)=\mathbf m(k+1)\). Every \(x\in\Sigma_{\mathbf m(k)}\) satisfies \(0\leq x\leq\mathbf m(k)\), so \(\Sigma\) lies in the order interval \(\{g:0\leq g\leq[1_A]\}\). The reverse inclusion is (4) with \(h=[1_A]\).

(6) The multiplicity matrices are the same (Proposition 5.4), so the group and the cone are the same. Let \(x\in\mathbb Z^{r_k}_+\) and \(c=\max_ix_i\). Since \(\mathbf m(k)\geq(1,\dots,1)^T\), we have \(x\leq c\,\mathbf m(k)\), and so \(\alpha_{l,k}x\leq c\,\alpha_{l,k}\mathbf m(k)\leq c\,\mathbf m(l)\leq l\,\mathbf m(l)\) for \(l\geq\max(k,c)\). So \(\alpha_{l,k}x\) lies in the scale \(\Sigma_{l\mathbf m(l)}\) of \(M_l(A_l)\). \(\square\)

**Example 6.4** (Computations).

(a) *Compact operators* (Example 5.1). All the matrices are \((1)\), so \(G=\mathbb Z\) and \(G^+=\mathbb Z_+\). The scale of \(M_n\) is \(\{0,1,\dots,n\}\), so \(\Sigma=\mathbb Z_+\): the classes of the projections of rank \(0,1,2,\dots\) of \(\mathcal K\).

*Further reading:* [Takesaki 2003, Section XIX.1]. The finite-rank projections constructed here prove directly that the scale is all of \(\mathbb Z_+\).

(b) *Unitization of the compact operators* (Example 5.2). Define \(h_n:\mathbb Z^2\to\mathbb Z^2\) by \(h_n(x)=(x_1-nx_2,\,x_2)\). Then
\[
\begin{gathered}
h_{n+1}(\alpha_nx)\\
=\big(x_1+x_2-(n+1)x_2,\ x_2\big)\\
=h_n(x),
\end{gathered}
\]
so the \(h_n\) induce a homomorphism \(G\to\mathbb Z^2\), which is bijective because each \(h_n\) is. Under this identification,
\[
\begin{gathered}
G^+\\
=\{(a,b):b\geq1\}\cup\{(a,0):a\geq0\},\\
\Sigma\\
=\{(a,0):a\geq0\}\cup\{(a,1):a\leq0\},\\
[1]\\
=(0,1).
\end{gathered}
\]
Indeed, for \(b\geq1\) the first coordinate \(x_1-nb\) of \(h_n(x_1,b)\) runs through all integers \(\geq-nb\), and for \(b=1\) and \(0\leq x_1\leq n\) it runs through \(-n,\dots,0\). In words: \((a,0)\) is the class of a projection of rank \(a\) in \(\mathcal K\), and \((-a,1)\) is the class of \(1-p\) for a projection \(p\in\mathcal K\) of rank \(a\). The cone \(G^+\) is not finitely generated as a monoid. Suppose finitely many elements generated it. A sum of generators with second coordinate \(1\) contains exactly one generator \((a,1)\) and otherwise generators \((c,0)\) with \(c\geq0\), so the first coordinates of the elements \((a,1)\) of \(G^+\) would be bounded below; but every \((a,1)\), \(a\in\mathbb Z\), lies in \(G^+\). Since \(\mathbb Z^2_+\) is generated by two elements, \((G,G^+)\) is not isomorphic to \((\mathbb Z^2,\mathbb Z^2_+)\).

*Further reading:* [Takesaki 2003, Section XIX.1]. The explicit connecting maps and the non-finite-generation argument above distinguish this cone from \(\mathbb Z^2_+\).

(c) *UHF algebras* (Example 5.3). The maps \(\mathbb Z\to\mathbb Q\), \(x\mapsto x/d_n\), are compatible with multiplication by \(k_n\), because \(k_nx/d_{n+1}=x/d_n\). They identify \(G\) with the subgroup \(\bigcup_nd_n^{-1}\mathbb Z\) of \(\mathbb Q\), with
\[
\begin{gathered}
G^+\\
=G\cap[0,\infty),\\
\Sigma\\
=G\cap[0,1],\\
[1]\\
=1 .
\end{gathered}
\]
For the CAR algebra, \(G=\mathbb Z[\tfrac12]\), the dyadic rationals.

(d) *Stabilization.* By Lemma 6.3(6), \(A\otimes\mathcal K\) has the group and cone of \(A\) and the scale \(G^+\). For instance, \(\mathcal K\otimes\mathcal K\) has the invariant \((\mathbb Z,\mathbb Z_+,\mathbb Z_+)\), the same as \(\mathcal K\).

## 7. Projections and the dimension group as an invariant

In this section we show that the scaled dimension group is the ordered \(K_0\)-group of the algebra with the classes of its projections as scale. The main tool is that projections in the closure of an increasing union can be moved into the union.

**Lemma 7.1** (Close projections are equivalent). Let \(p,q\) be projections of a C\*-algebra \(A\) with \(\|p-q\|<1\). There is a unitary \(u\) in the C\*-subalgebra of \(A^+\) generated by \(1,p,q\) with \(upu^*=q\). In particular \(v=up\in A\) satisfies \(v^*v=p\) and \(vv^*=q\).

**Proof.** Put \(z=qp+(1-q)(1-p)\in A^+\). Expanding,
\[
\begin{gathered}
z^*z\\
=pqp+(1-p)(1-q)(1-p)\\
=1-(p-q)^2,\\
zz^*\\
=qpq+(1-q)(1-p)(1-q)\\
=1-(p-q)^2 .
\end{gathered}
\]
Since \(\|(p-q)^2\|=\|p-q\|^2<1\), both \(z^*z\) and \(zz^*\) are invertible (Section 1(b)), so \(z\) has the left inverse \((z^*z)^{-1}z^*\) and the right inverse \(z^*(zz^*)^{-1}\), and is invertible. Also \(zp=qp=qz\). Taking adjoints, \(z^*q=pz^*\), hence \(z^*zp=z^*qz=pz^*z\): the element \(p\) commutes with \(z^*z\), and hence with \(h=(z^*z)^{-1/2}\), which is a limit of polynomials in \(z^*z\) (Section 1(c)). Put \(u=zh\). Then \(u^*u=hz^*zh=1\), and \(u\) is invertible, so \(uu^*=1\) as well. Finally
\[
\begin{gathered}
upu^*\\
=zhphz^*\\
=zph^2z^*\\
=zp(z^*z)^{-1}z^*\\
=qz(z^*z)^{-1}z^*\\
=q,
\end{gathered}
\]
because \(z(z^*z)^{-1}z^*=zz^{-1}(z^*)^{-1}z^*=1\). Since \(A\) is an ideal of \(A^+\), \(v=up\in A\), and \(v^*v=pu^*up=p\), \(vv^*=upu^*=q\). \(\square\)

**Lemma 7.2** (Projections near a subalgebra). Let \(B\) be a C\*-subalgebra of a C\*-algebra \(A\), and \(p\in A\) a projection whose distance to \(B\) is less than \(\frac14\). Then there is a projection \(q\in B\) with \(\|p-q\|<\frac12\); by Lemma 7.1, \(p\) and \(q\) are equivalent in \(A\).

**Proof.** Choose \(b\in B\) with \(\|p-b\|<\frac14\) and put \(a=\frac12(b+b^*)\in B\); then \(a\) is self-adjoint and \(\|p-a\|<\frac14\). Let \(\lambda\) be real with distance at least \(\frac14\) from \(\{0,1\}\). In \(A^+\), \(p-\lambda\) is invertible, and its inverse is the function \(t\mapsto(t-\lambda)^{-1}\) of \(p\), of norm at most \(4\) because \(\sigma(p)\subseteq\{0,1\}\) (Section 1(c)). So
\[
a-\lambda=(p-\lambda)\big(1+(p-\lambda)^{-1}(a-p)\big)
\]
is invertible by Section 1(b), since \(\|(p-\lambda)^{-1}(a-p)\|<4\cdot\frac14=1\). Hence \(\sigma(a)\subseteq(-\frac14,\frac14)\cup(\frac34,\frac54)\). Let \(f=0\) on \((-\infty,\frac12]\) and \(f=1\) on \((\frac12,\infty)\). It is continuous on \(\sigma(a)\) and \(f(0)=0\), so \(q=f(a)\in B\). Since \(f=f^2=\bar f\) on \(\sigma(a)\), \(q\) is a projection, and \(\|q-a\|=\max_{t\in\sigma(a)}|f(t)-t|<\frac14\). So \(\|p-q\|<\frac12\). \(\square\)

**Proposition 7.3** (Projections in the closure of a union). Let \(A\) be a C\*-algebra and \(A_1\subseteq A_2\subseteq\cdots\) C\*-subalgebras with dense union.

1. Every projection \(p\in A\) is equivalent in \(A\) to a projection of some \(A_k\).
2. If \(p,q\in A_k\) are projections that are equivalent in \(A\), they are equivalent in \(A_l\) for some \(l\geq k\).

**Proof.** (1) The distance from \(p\) to \(A_k\) decreases to \(0\); apply Lemma 7.2 once it is below \(\frac14\).

(2) If \(p=0\), any implementing partial isometry has norm zero, so \(q=0\) and the assertion is immediate. Assume \(p\neq0\). Let \(v\in A\) with \(v^*v=p\) and \(vv^*=q\); then \(v=qvp\). Choose \(y_l\in A_l\) with \(y_l\to v\), and put \(w_l=qy_lp\in A_l\) for \(l\geq k\); then \(w_l\to qvp=v\). The elements \(x_l=w_l^*w_l\) lie in the corner \(pA_lp\), a C\*-algebra with unit \(p\), and \(x_l\to v^*v=p\). For large \(l\), \(\|x_l-p\|<\frac12\), so \(x_l\) is invertible in \(pA_lp\) with spectrum in \([\frac12,\frac32]\) (Section 1(b), applied to \(x_l-\lambda p\)). Let \(h_l=x_l^{-1/2}\), computed in \(pA_lp\); by Section 1(c) it is the same element when computed in the unital C\*-algebra \(pAp\), and \(h_l\to p^{-1/2}=p\). Put \(v_l=w_lh_l\in A_l\). Then \(v_l^*v_l=h_lx_lh_l=p\), so \(e_l=v_lv_l^*\) is a projection, and \(qe_l=e_l\) because \(qw_l=w_l\). Moreover \(v_l\to vp=v\), so \(e_l\to vv^*=q\). For large \(l\), \(q-e_l\) is a projection of norm less than one, hence zero. So \(p\sim q\) in \(A_l\). \(\square\)

**Definition 7.4.** Let \(A\) be a C\*-algebra. Two projections \(p\in M_n(A)\) and \(q\in M_{n'}(A)\) are *equivalent* if they are equivalent in \(M_N(A)\), \(N=\max(n,n')\), where both sit as upper left corners; this does not depend on \(N\), because a partial isometry \(v\) with \(v^*v=p\) and \(vv^*=q\) satisfies \(v=qvp\). Let \(V(A)\) be the set of equivalence classes \([p]\) of projections in \(M_\infty(A)\). For projections \(p,q\), view both in some \(M_N(A)\) and put
\[
\begin{gathered}
{}[p]+[q]\\
=[\operatorname{diag}(p,q)],\\
\operatorname{diag}(p,q)\in M_{2N}(A).
\end{gathered}
\]
Enlarging \(N\) changes \(\operatorname{diag}(p,q)\) by a permutation of the basis, which is implemented by a permutation matrix, so the class does not depend on \(N\). The addition is well defined and makes \(V(A)\) an abelian monoid with zero \([0]\): if \(v,w\) implement \(p\sim p'\) and \(q\sim q'\), then \(\operatorname{diag}(v,w)\) implements \(\operatorname{diag}(p,q)\sim\operatorname{diag}(p',q')\); and \(\begin{pmatrix}0&q\\p&0\end{pmatrix}\) implements \(\operatorname{diag}(p,q)\sim\operatorname{diag}(q,p)\). A \*-homomorphism \(\psi:A\to B\) induces the monoid homomorphism \(\psi_*[p]=[\psi(p)]\), where \(\psi\) acts entrywise.

For orthogonal projections \(p,q\in A\), \(p+q\sim\operatorname{diag}(p,q)\) through \(\begin{pmatrix}p&q\\0&0\end{pmatrix}\), so \([p+q]=[p]+[q]\).

**Theorem 7.5** (The dimension group is an invariant). Let \(A\) be an AF-algebra with generating sequence \((A_k)\) and scaled dimension group \((G,G^+,\Sigma)\). For a projection \(p\in M_N(A_k)\cong M_{N\mathbf m(k)}\), let \(\operatorname{rk}p\in\mathbb Z^{r_k}_+\) be its rank vector.

1. The rule \(\alpha_{\infty,k}(\operatorname{rk}p)\mapsto[p]\) is a well-defined isomorphism of monoids \(\Phi:G^+\to V(A)\). In particular \(V(A)\) has cancellation: \(a+c=b+c\) implies \(a=b\).
2. \(\Phi(\Sigma)\) is the set of classes of projections of \(A\) itself.
3. \(G\) is the Grothendieck group of \(V(A)\): every monoid homomorphism from \(V(A)\) to an abelian group extends uniquely to a group homomorphism on \(G\), through \(\Phi^{-1}\).
4. Every \*-homomorphism \(\psi:A\to B\) between AF-algebras induces a homomorphism of scaled dimension groups \(\psi_*\) with \(\psi_*[p]=[\psi(p)]\) for projections \(p\in M_\infty(A)\); \((\psi\circ\psi')_*=\psi_*\psi'_*\) and \(\mathrm{id}_*=\mathrm{id}\). Isomorphic AF-algebras have isomorphic scaled dimension groups, whatever generating sequences are used.

**Proof.** By Proposition 5.4(1), the inclusion \(M_N(A_k)\subseteq M_N(A_l)\) has multiplicity matrix \(\alpha_{l,k}\), and the corner inclusion \(M_N(A_k)\subseteq M_{N'}(A_k)\) preserves rank vectors. So by (3.1), the rank vector of \(p\) at stage \(l\) is \(\alpha_{l,k}\operatorname{rk}p\).

(1) *Well defined and injective.* Let \(p\in M_N(A_k)\) and \(p'\in M_{N'}(A_{k'})\), and view both in \(M_{N''}(A_l)\) with \(N''=\max(N,N')\) and \(l\geq k,k'\). If \(\alpha_{\infty,k}\operatorname{rk}p=\alpha_{\infty,k'}\operatorname{rk}p'\), then at some later stage the rank vectors agree, so \(p\sim p'\) there by Lemma 2.5, and \([p]=[p']\). Conversely, if \([p]=[p']\) in \(V(A)\), Proposition 7.3(2), applied in \(M_{N''}(A)\) with the subalgebras \(M_{N''}(A_l)\), gives a stage at which \(p\sim p'\); there the rank vectors agree (Lemma 2.5), so \(\alpha_{\infty,k}\operatorname{rk}p=\alpha_{\infty,k'}\operatorname{rk}p'\). Every element \(\alpha_{\infty,k}(x)\) of \(G^+\), \(x\geq0\), is of the form \(\alpha_{\infty,k}\operatorname{rk}p\) for a diagonal projection \(p\in M_N(A_k)\) with \(N\geq\max(1,\max_ix_i)\). *Onto.* The union of the \(M_N(A_k)\) is dense in \(M_N(A)\) (Section 1(f)), so by Proposition 7.3(1) every projection of \(M_N(A)\) is equivalent to one in some \(M_N(A_k)\). *Additive.* \(\operatorname{rk}\operatorname{diag}(p,q)=\operatorname{rk}p+\operatorname{rk}q\). Cancellation holds because \(G^+\) sits in the group \(G\).

(2) If \(p\in A_k\), then \(\operatorname{rk}p\in\Sigma_{\mathbf m(k)}\). Conversely, every projection of \(A\) is equivalent to a projection of some \(A_k\) (Proposition 7.3(1)), and every element of \(\Sigma_{\mathbf m(k)}\) is the rank vector of a projection of \(A_k\).

(3) \(G=G^+-G^+\). If \(\chi:V(A)\to H\) is a monoid homomorphism into an abelian group, put \(\tilde\chi(g_1-g_2)=\chi\Phi(g_1)-\chi\Phi(g_2)\) for \(g_1,g_2\in G^+\). If \(g_1-g_2=g_1'-g_2'\), then \(g_1+g_2'=g_1'+g_2\) in \(G^+\), and applying \(\chi\Phi\) shows that \(\tilde\chi\) is well defined. It is a homomorphism, and it is the only one extending \(\chi\Phi\).

(4) \(\psi\) maps equivalent projections to equivalent projections and respects \(\operatorname{diag}\), so \(\psi_*:V(A)\to V(B)\) is a monoid homomorphism. By (1) and (3) it gives a group homomorphism \(G(A)\to G(B)\), which maps \(G(A)^+\) into \(G(B)^+\) and, by (2), \(\Sigma(A)\) into \(\Sigma(B)\). Functoriality is clear, and an isomorphism has an inverse, so it induces an isomorphism. \(\square\)

**Definition 7.6.** For an AF-algebra \(A\) we write \((K_0(A),K_0(A)^+,\Sigma(A))\) for its scaled dimension group, computed from any generating sequence: \(K_0(A)\) is the Grothendieck group of \(V(A)\), \(K_0(A)^+\) the image of \(V(A)\), and \(\Sigma(A)\) the set of classes of projections of \(A\).

For unital C\*-algebras, \(K_0(A)\) is defined in K-theory as the Grothendieck group of \(V(A)\), so the two notions agree. For a nonunital C\*-algebra, K-theory defines \(K_0(A)\) as the kernel of the map \(K_0(A^+)\to K_0(\mathbb C)=\mathbb Z\) induced by the quotient map \(A^+\to\mathbb C\) that kills \(A\), with positive cone the image of \(V(A)\) [Blackadar 2017, V.1.1.15–V.1.1.17]. The next proposition shows that this also agrees with Definition 7.6.

**Proposition 7.7** (Nonunital AF-algebras). Let \(A\) be a nonunital AF-algebra. Then \(A^+\) is an AF-algebra, and the map \(V(A)\to V(A^+)\) induced by the inclusion extends to an isomorphism of \(K_0(A)\) onto the kernel of \(K_0(A^+)\to\mathbb Z\), carrying \(K_0(A)^+\) onto the image of \(V(A)\).

**Proof.** Let \((A_k)\) be a generating sequence with units \(1_k\). Since \(A\) has no unit, \(1_k\neq1\), and \[
\begin{gathered}
A_k^+:\\
=A_k+\mathbb C1\\
=A_k\oplus\mathbb C(1-1_k)\cong M_{\mathbf m(k)}\oplus\mathbb C
\end{gathered}
\] is a finite-dimensional C\*-subalgebra of \(A^+\). These algebras increase and their union is dense in \(A^+\), so \(A^+\) is an AF-algebra. In the inclusion \(A_k^+\subseteq A_{k+1}^+\), the summands of \(A_k\) enter those of \(A_{k+1}\) as before, and the minimal projection \(1-1_k\) of the extra summand splits as \((1-1_{k+1})+(1_{k+1}-1_k)\), where \(1_{k+1}-1_k\in A_{k+1}\) has rank vector \(d_k=\mathbf m(k+1)-\alpha_k\mathbf m(k)\). So the multiplicity matrix is
\[
\begin{pmatrix}\alpha_k&d_k\\0&1\end{pmatrix}.
\]
The quotient map \(A^+\to\mathbb C\) kills \(A_k\) and sends \(1-1_k\) to \(1\), so on \(\mathbb Z^{r_k}\oplus\mathbb Z\) it induces the projection \((x,t)\mapsto t\) at every stage. An element of \(K_0(A^+)\), represented by \((x,t)\) at stage \(k\), is in the kernel exactly when \(t=0\). The connecting maps send \((x,0)\) to \((\alpha_kx,0)\), so \((x,0)\) represents \(0\) in \(K_0(A^+)\) exactly when \(\alpha_{l,k}x=0\) for some \(l\). So the kernel is the direct limit of the subgroups \(\mathbb Z^{r_k}\oplus0\) under the maps \(\alpha_k\), which is \(K_0(A)\), and the element \((x,0)\) with \(x\geq0\) is the image of the class of a projection in some \(M_N(A_k)\). \(\square\)

## 8. Elliott's classification theorem

A reference for this section is [Blackadar 1998, Section 7.3]. In the two lemmas, \(B\) is any AF-algebra with generating sequence \((B_l)\), \(B_l\cong M_{\mathbf n(l)}\) with \(\mathbf n(l)\in\mathbb N^{s_l}\), and multiplicity matrices \(\beta_l\); its classes are \(\beta_{\infty,l}(y)\). In the proof of the theorem they are applied both to \(B\) and to \(A\).

**Lemma 8.1** (Existence). Let \(\mathbf m\in\mathbb N^r\), and let \(h:\mathbb Z^r\to K_0(B)\) be a group homomorphism with \(h(\mathbb Z^r_+)\subseteq K_0(B)^+\) and \(h(\mathbf m)\in\Sigma(B)\). Then there are \(l\) and a \*-homomorphism \(\varphi:M_{\mathbf m}\to B_l\) with
\[
\beta_{\infty,l}\big(\alpha(\varphi)x\big)=h(x)\qquad(x\in\mathbb Z^r),
\]
that is, \([\varphi(p)]=h(\operatorname{rk}p)\) for every projection \(p\in M_{\mathbf m}\). If \(h(e_i)\neq0\) for every \(i\), then \(\varphi\) is injective.

**Proof.** Each \(h(e_i)\) lies in \(K_0(B)^+\), so \(h(e_i)=\beta_{\infty,l}(y_i)\) with \(y_i\geq0\) at a common stage \(l\) (Lemma 6.3(3)). The element \(\sum_im_iy_i\) represents \(h(\mathbf m)\in\Sigma(B)\), so by Lemma 6.3(3) it lies in the scale at some later stage; moving there keeps the \(y_i\geq0\). So we may assume that \(\sum_im_iy_i\leq\mathbf n(l)\). Let \(\alpha\) be the \(s_l\times r\) matrix with columns \(y_1,\dots,y_r\). Its entries lie in \(\mathbb Z_+\) and \(\alpha\mathbf m=\sum_im_iy_i\leq\mathbf n(l)\), so Theorem 3.2(3) gives \(\varphi=\varphi_\alpha:M_{\mathbf m}\to M_{\mathbf n(l)}\cong B_l\) with \(\alpha(\varphi)=\alpha\), and \(\beta_{\infty,l}(\alpha x)=\sum_ix_i\beta_{\infty,l}(y_i)=h(x)\). If \(h(e_i)\neq0\), then \(y_i\neq0\), so no column of \(\alpha\) vanishes and \(\varphi\) is injective (Theorem 3.2(2)). \(\square\)

**Lemma 8.2** (Uniqueness). Let \(\varphi,\psi:M_{\mathbf m}\to B_l\) be \*-homomorphisms with \(\beta_{\infty,l}\alpha(\varphi)=\beta_{\infty,l}\alpha(\psi)\). Then there are \(l'\geq l\) and \(u\in U(B_{l'})\) with \(u\varphi(x)u^*=\psi(x)\) for all \(x\in M_{\mathbf m}\).

**Proof.** For each \(i\), the \(i\)-th columns of \(\alpha(\varphi)\) and \(\alpha(\psi)\) have the same image in \(K_0(B)\), so they become equal at some later stage. Take \(l'\) beyond all these stages. As maps into \(B_{l'}\), \(\varphi\) and \(\psi\) have the multiplicity matrices \(\beta_{l',l}\alpha(\varphi)=\beta_{l',l}\alpha(\psi)\) (Theorem 3.2(1)), and Theorem 3.2(4) gives \(u\). \(\square\)

**Theorem 8.3** (Classification of AF-algebras). Let \(A\) and \(B\) be AF-algebras with generating sequences \((A_k)\) and \((B_l)\) and local algebras \(A_\infty\) and \(B_\infty\).

1. For every homomorphism \[
\begin{gathered}
h:(K_0(A),K_0(A)^+,\Sigma(A))\\
\to(K_0(B),K_0(B)^+,\Sigma(B))
\end{gathered}
\] of scaled ordered groups there is a \*-homomorphism \(\psi:A\to B\) with \(\psi(A_\infty)\subseteq B_\infty\) and \(\psi_*=h\).
2. For every isomorphism \(\theta\) of the scaled dimension groups there is an isomorphism \(\Phi:A\to B\) with \(\Phi(A_\infty)=B_\infty\) and \(\Phi_*=\theta\).
3. The following are equivalent: (i) \(A\cong B\); (ii) \(A_\infty\) and \(B_\infty\) are isomorphic \*-algebras; (iii) the scaled dimension groups of \(A\) and \(B\) are isomorphic.

*Reference:* [Elliott 1976].

**Proof.** Write \(\alpha_k\) for the multiplicity matrices of \((A_k)\). The classes \([e]\) of minimal projections \(e\) of the \(A_k\) generate \(K_0(A)\) as a group, so two homomorphisms from \(K_0(A)\) that agree on them are equal.

(1) We build \(l_1<l_2<\cdots\) and \*-homomorphisms \(\varphi_n:A_n\to B_{l_n}\) such that \([\varphi_n(p)]=h[p]\) for projections \(p\in A_n\), and such that \(\varphi_{n+1}\) extends \(\varphi_n\) as a map into \(B_{l_{n+1}}\). The homomorphism \(h\circ\alpha_{\infty,1}:\mathbb Z^{r_1}\to K_0(B)\) is positive and maps \(\mathbf m(1)=\operatorname{rk}1_{A_1}\) to \(h[1_{A_1}]\in\Sigma(B)\); Lemma 8.1 gives \(\varphi_1\). Suppose \(\varphi_n\) is built. Lemma 8.1, applied to \(h\circ\alpha_{\infty,n+1}\) (which satisfies its hypotheses for the same reason), gives \(\varphi':A_{n+1}\to B_{l'}\) with \([\varphi'(p)]=h[p]\); we may take \(l'>l_n\). The restriction of \(\varphi'\) to \(A_n\) and the map \(\varphi_n\), viewed in \(B_{l'}\), induce the same map \(h\circ\alpha_{\infty,n}\). By Lemma 8.2 there are \(l_{n+1}\geq l'\) and \(u\in U(B_{l_{n+1}})\) with \(u\varphi'(x)u^*=\varphi_n(x)\) for \(x\in A_n\). Put \(\varphi_{n+1}=\operatorname{Ad}u\circ\varphi'\); conjugation does not change classes. The \(\varphi_n\) define a \*-homomorphism \(A_\infty\to B_\infty\), which is contractive on each \(A_n\) (Section 1(a)) and extends to \(\psi:A\to B\). By construction \(\psi_*[e]=h[e]\) for minimal projections \(e\) of the \(A_n\), so \(\psi_*=h\).

(2) We build \(k_1<k_2<\cdots\), \(l_1<l_2<\cdots\) and injective \*-homomorphisms
\[
\varphi_n:A_{k_n}\to B_{l_n},\qquad\psi_n:B_{l_n}\to A_{k_{n+1}}
\]
such that \(\psi_n\circ\varphi_n\) is the inclusion \(A_{k_n}\subseteq A_{k_{n+1}}\), \(\varphi_{n+1}\circ\psi_n\) is the inclusion \(B_{l_n}\subseteq B_{l_{n+1}}\), \([\varphi_n(p)]=\theta[p]\) and \([\psi_n(q)]=\theta^{-1}[q]\) for projections \(p\in A_{k_n}\), \(q\in B_{l_n}\).

Put \(k_1=1\). The map \(\theta\circ\alpha_{\infty,1}\) is positive, sends \(\mathbf m(1)\) into \(\theta(\Sigma(A))=\Sigma(B)\), and sends each \(e_i\) to a nonzero element (Lemma 6.3(2) and injectivity of \(\theta\)). Lemma 8.1 gives an injective \(\varphi_1:A_1\to B_{l_1}\). Suppose \(\varphi_n\) is built. Lemma 8.1, applied to \(\theta^{-1}\circ\beta_{\infty,l_n}\) in the same way, gives an injective \(\psi':B_{l_n}\to A_{k'}\) with \([\psi'(q)]=\theta^{-1}[q]\); composing with an inclusion we may take \(k'>k_n\). Then \(\psi'\circ\varphi_n\) and the inclusion \(A_{k_n}\subseteq A_{k'}\) both send \([p]\) to \([p]\). By Lemma 8.2 there are \(k_{n+1}\geq k'\) and \(u\in U(A_{k_{n+1}})\) with \(u\psi'(\varphi_n(x))u^*=x\) for \(x\in A_{k_n}\). Put \(\psi_n=\operatorname{Ad}u\circ\psi'\), as a map into \(A_{k_{n+1}}\). Exchanging the roles of \(A\) and \(B\) and of \(\theta\) and \(\theta^{-1}\), the same step produces \(\varphi_{n+1}:A_{k_{n+1}}\to B_{l_{n+1}}\) with \(\varphi_{n+1}\circ\psi_n\) equal to the inclusion \(B_{l_n}\subseteq B_{l_{n+1}}\).

On \(A_{k_n}\) we get \(\varphi_{n+1}=\varphi_{n+1}\circ\psi_n\circ\varphi_n=\varphi_n\). So the \(\varphi_n\) define a \*-homomorphism \(\Phi_0:A_\infty\to B_\infty\), and likewise the \(\psi_n\) define \(\Psi_0:B_\infty\to A_\infty\), with \(\Psi_0\Phi_0=\mathrm{id}\) and \(\Phi_0\Psi_0=\mathrm{id}\). Each \(\varphi_n\) is isometric (Section 1(a)), so \(\Phi_0\) extends to an isometric \*-homomorphism \(\Phi:A\to B\); similarly \(\Psi\), and \(\Psi\Phi=\mathrm{id}\), \(\Phi\Psi=\mathrm{id}\) by continuity. By construction \(\Phi(A_\infty)=B_\infty\) and \(\Phi_*=\theta\).

(3) (i)⇒(iii) is Theorem 7.5(4), and (iii)⇒(ii) is (2). (ii)⇒(i): let \(\Phi_0:A_\infty\to B_\infty\) be an isomorphism of \*-algebras. The finite-dimensional subspace \(\Phi_0(A_k)\) lies in some \(B_l\), and \(\Phi_0\) restricted to \(A_k\) is an injective \*-homomorphism of C\*-algebras into \(B_l\), hence isometric. So \(\Phi_0\) is isometric on \(A_\infty\) and extends to an isometric \*-homomorphism \(\Phi:A\to B\). Its range is closed and contains \(B_\infty\), so \(\Phi\) is onto. \(\square\)

**Corollary 8.4.** Let \(A\) be an AF-algebra. (1) Any two generating sequences of \(A\) have isomorphic local algebras. (2) Every automorphism of the scaled dimension group of \(A\) is induced by an automorphism of \(A\).

**Proof.** Apply Theorem 8.3(2) with \(B=A\): to the identity of \(K_0(A)\) and two generating sequences for (1), and to the given automorphism for (2). \(\square\)

**Theorem 8.5** (Stable isomorphism). For AF-algebras \(A\) and \(B\), \(A\otimes\mathcal K\cong B\otimes\mathcal K\) if and only if the ordered groups \((K_0(A),K_0(A)^+)\) and \((K_0(B),K_0(B)^+)\) are isomorphic.

**Proof.** By Proposition 5.4 and Lemma 6.3(6), \(A\otimes\mathcal K\) is an AF-algebra whose scaled dimension group is \((K_0(A),K_0(A)^+,K_0(A)^+)\), and similarly for \(B\). If \(A\otimes\mathcal K\cong B\otimes\mathcal K\), Theorem 7.5(4) gives an isomorphism of these triples, in particular of the ordered groups. Conversely, an isomorphism of ordered groups maps \(K_0(A)^+\) onto \(K_0(B)^+\), that is, scale onto scale, and Theorem 8.3(3) gives \(A\otimes\mathcal K\cong B\otimes\mathcal K\). \(\square\)

For a UHF algebra of type \((k_n)\) (Example 5.3), its *supernatural number* \(q\) records, for each prime \(p\), the exponent \(\nu_p(q)=\sum_n\nu_p(k_n)\in\{0,1,2,\dots,\infty\}\), where \(\nu_p(k)\) is the exponent of \(p\) in \(k\). Let \(\mathbb Z(q)\) be the set of rationals \(a/b\) (\(a\in\mathbb Z\), \(b\in\mathbb N\)) with \(\nu_p(b)\leq\nu_p(q)\) for every prime \(p\).

**Corollary 8.6** (Classification of UHF algebras). The UHF algebra of type \((k_n)\) has the scaled dimension group \((\mathbb Z(q),\mathbb Z(q)\cap[0,\infty),\mathbb Z(q)\cap[0,1])\). Two UHF algebras are isomorphic if and only if their supernatural numbers are equal.

*Reference:* [Glimm 1960].

**Proof.** By Example 6.4(c), the group is \(\bigcup_nd_n^{-1}\mathbb Z\). Each \(d_n\) satisfies \(\nu_p(d_n)\leq\nu_p(q)\), so this union lies in \(\mathbb Z(q)\). Conversely, let \(a/b\in\mathbb Z(q)\). Only finitely many primes divide \(b\), and \(\nu_p(d_n)\) increases to \(\nu_p(q)\geq\nu_p(b)\), so \(b\) divides \(d_n\) for large \(n\), and \(a/b\in d_n^{-1}\mathbb Z\).

If two UHF algebras have the same supernatural number, their scaled dimension groups are the same subsets of \(\mathbb Q\), and Theorem 8.3(3) shows that the algebras are isomorphic. Conversely, an isomorphism of the algebras gives an isomorphism \(\theta:\mathbb Z(q)\to\mathbb Z(q')\) of scaled ordered groups (Theorem 7.5(4)). The largest element of the scale \(\mathbb Z(q)\cap[0,1]\) is \(1\), so \(\theta(1)=1\). For \(a/b\in\mathbb Z(q)\), \(b\,\theta(a/b)=\theta(a)=a\), so \(\theta(a/b)=a/b\). Hence \(\mathbb Z(q)=\mathbb Z(q')\), and \(\nu_p(q)=\sup\{\nu_p(b):1/b\in\mathbb Z(q)\}\) shows \(q=q'\). \(\square\)

**Example 8.7** (The scale cannot be dropped). Let \(A\) be the CAR algebra. By Proposition 5.4(1), \(M_3(A)\) is an AF-algebra with the same group and cone as \(A\), namely \(\mathbb Z[\frac12]\) with the usual order, but with unit class \(3\) and scale \([0,3]\cap\mathbb Z[\frac12]\). A group homomorphism \(\theta\) of \(\mathbb Z[\frac12]\) satisfies \(2^n\theta(2^{-n})=\theta(1)\), so \(\theta(x)=\theta(1)x\). If \(\theta\) is bijective and positive, then \(\theta(1)\) is a positive unit of the ring \(\mathbb Z[\frac12]\), that is, \(\theta(1)=2^j\) for some \(j\in\mathbb Z\). Then \(\theta([0,1])=[0,2^j]\neq[0,3]\). So \(M_3(A)\not\cong A\), although \(M_3(A)\otimes\mathcal K\cong A\otimes\mathcal K\) by Theorem 8.5. This agrees with Corollary 8.6: \(M_3(A)\) is the UHF algebra of type \((3,2,2,\dots)\), with supernatural number \(3\cdot2^\infty\neq2^\infty\).

## 9. The gauge-invariant CAR algebra and Pascal's triangle

**9.1. The algebra.** For \(n\geq0\) let \(H_n=(\mathbb C^2)^{\otimes n}\) (\(H_0=\mathbb C\)), with the orthonormal basis \(\varepsilon_\xi=\varepsilon_{\xi_1}\otimes\cdots\otimes\varepsilon_{\xi_n}\), \(\xi\in\{0,1\}^n\), where \(\varepsilon_0,\varepsilon_1\) is the standard basis of \(\mathbb C^2\). Let \(|\xi|\) be the number of ones in \(\xi\). Put \(B_n=B(H_n)\cong M_{2^n}\), identify \(H_{n+1}=H_n\otimes\mathbb C^2\), and let \(B_n\to B_{n+1}\) be \(x\mapsto x\otimes1\). By Example 5.3, the limit \(B\) is the CAR algebra. For \(\lambda\) in the unit circle \(\mathbb T\), let \(U_n(\lambda)\) be the unitary of \(H_n\) with
\[
U_n(\lambda)\varepsilon_\xi=\lambda^{\,n-2|\xi|}\varepsilon_\xi ;
\]
thus \(U_n(\lambda)=u(\lambda)^{\otimes n}\) with \(u(\lambda)=\operatorname{diag}(\lambda,\bar\lambda)\), and \(U_{n+1}(\lambda)=U_n(\lambda)\otimes u(\lambda)\). Hence \(\operatorname{Ad}U_{n+1}(\lambda)(x\otimes1)=(\operatorname{Ad}U_n(\lambda)(x))\otimes1\). By Lemma 4.4 there is an automorphism \(\sigma_\lambda\) of \(B\) that equals \(\operatorname{Ad}U_n(\lambda)\) on \(B_n\), and \(\sigma_\lambda\sigma_\mu=\sigma_{\lambda\mu}\) (check on each \(B_n\) and extend by continuity). We call the fixed-point algebra
\[
A=\{x\in B\colon\sigma_\lambda(x)=x\text{ for all }\lambda\in\mathbb T\}
\]
the *gauge-invariant CAR algebra*. It is a C\*-subalgebra of \(B\) containing \(1\). Put \(A_n=A\cap B_n\).

**Lemma 9.2.** Let \(H_{n,j}\) be the span of the \(\varepsilon_\xi\) with \(|\xi|=j\), of dimension \(\binom nj\), and \(P_{n,j}\) the projection onto it. Then
\[
\begin{gathered}
A_n\\
=\{x\in B_n:xH_{n,j}\subseteq H_{n,j}\text{ for }j=0,\dots,n\}\\
=\bigoplus_{j=0}^nB(H_{n,j})\cong\bigoplus_{j=0}^nM_{\binom nj}.
\end{gathered}
\]
Moreover, for \(x\in B_n\) and every integer \(N>2n\),
\[
\sum_{j=0}^nP_{n,j}\,x\,P_{n,j}=\frac1N\sum_{\omega^N=1}\sigma_\omega(x).
\tag{9.1}
\]

**Proof.** Let \(e_{\xi\eta}\) be the operator \(\zeta\mapsto\langle\zeta,\varepsilon_\eta\rangle\varepsilon_\xi\). Since \(\bar\lambda=\lambda^{-1}\),
\[
\begin{gathered}
\sigma_\lambda(e_{\xi\eta})\\
=U_n(\lambda)e_{\xi\eta}U_n(\lambda)^*\\
=\lambda^{\,n-2|\xi|}\,\overline{\lambda^{\,n-2|\eta|}}\,e_{\xi\eta}\\
=\lambda^{\,2(|\eta|-|\xi|)}e_{\xi\eta}.
\end{gathered}
\]
Write \(x=\sum x_{\xi\eta}e_{\xi\eta}\). The exponents \(2(|\eta|-|\xi|)\) lie between \(-2n\) and \(2n\). For \(N>2n\), the average of \(\omega^k\) over the \(N\)-th roots of unity is \(1\) for \(k=0\) and \(0\) for \(0<|k|\leq2n\). So the right side of (9.1) is \(\sum_{|\xi|=|\eta|}x_{\xi\eta}e_{\xi\eta}\), which is the left side. If \(x\) is fixed by every \(\sigma_\lambda\), it equals this average, so it maps each \(H_{n,j}\) into itself. Conversely, an operator that maps each \(H_{n,j}\) into itself is a combination of the \(e_{\xi\eta}\) with \(|\xi|=|\eta|\), and these are fixed. \(\square\)

**Proposition 9.3** (Pascal's triangle). The algebras \(A_0\subseteq A_1\subseteq\cdots\) form a generating sequence of \(A\), so \(A\) is a unital AF-algebra. Index the summands of \(A_n\) by \(j=0,\dots,n\), the \(j\)-th being \(B(H_{n,j})\) of size \(\binom nj\). The inclusion \(A_n\subseteq A_{n+1}\) is unital, and the \(j\)-th summand of \(A_n\) enters the summands \(j\) and \(j+1\) of \(A_{n+1}\), each with multiplicity one. So the Bratteli diagram is Pascal's triangle:

```
level 0                         1
level 1                      1     1
level 2                   1     2     1
level 3                1     3     3     1
level 4             1     4     6     4     1
level 5          1     5    10    10     5     1
level 6       1     6    15    20    15     6     1
```

Here each vertex is joined to the two vertices just below it, and the labels are the sizes \(\binom nj\).

**Proof.** \(A_n=A\cap B_n\subseteq A\cap B_{n+1}=A_{n+1}\). Let \(x\in A\) and \(\varepsilon>0\). Choose \(n\) and \(y\in B_n\) with \(\|x-y\|<\varepsilon\), and \(N>2n\). By Lemma 9.2 the element \(E(y)=\frac1N\sum_{\omega^N=1}\sigma_\omega(y)\) lies in \(A_n\). Since \(\sigma_\omega(x)=x\) and each \(\sigma_\omega\) is isometric,
\[
\begin{gathered}
\|x-E(y)\|\\
=\Big\|\frac1N\sum_{\omega^N=1}\sigma_\omega(x-y)\Big\|\\
\leq\|x-y\|<\varepsilon .
\end{gathered}
\]
So \(\bigcup_nA_n\) is dense in \(A\). Next, \(H_{n,j}\otimes\mathbb C^2=(H_{n,j}\otimes\varepsilon_0)\oplus(H_{n,j}\otimes\varepsilon_1)\) with \(H_{n,j}\otimes\varepsilon_0\subseteq H_{n+1,j}\) and \(H_{n,j}\otimes\varepsilon_1\subseteq H_{n+1,j+1}\). A minimal projection \(e\) of \(B(H_{n,j})\), the projection onto a unit vector \(v\), goes to \(e\otimes1\), the projection onto the span of \(v\otimes\varepsilon_0\) and \(v\otimes\varepsilon_1\); its components in \(B(H_{n+1,j})\) and \(B(H_{n+1,j+1})\) have rank one, and the others vanish. Finally \(1\otimes1=1\). \(\square\)

To compute the ordered group we need a classical theorem on positive polynomials.

**Theorem 9.4** (Pólya's theorem). Let \(F(x,y)=\sum_{j=0}^dc_jx^jy^{d-j}\) be a homogeneous polynomial with real coefficients such that \(F(x,y)>0\) whenever \(x,y\geq0\) and \(x+y=1\). Then for all sufficiently large \(N\), every coefficient of \((x+y)^NF(x,y)\) is strictly positive.

*Reference:* [Pólya 1928].

**Proof.** If \(d=0\) there is nothing to prove, so let \(d\geq1\). Put \(M=N+d\) and write \((x+y)^NF(x,y)=\sum_{k=0}^Mb_kx^ky^{M-k}\). Then \(b_k=\sum_jc_j\binom N{k-j}\), where \(\binom Ni=0\) for \(i<0\) or \(i>N\). For integers \(a\geq0\) and \(i\geq0\) let \((a)_i=a(a-1)\cdots(a-i+1)\), with \((a)_0=1\); note that \((a)_i=0\) when \(0\leq a<i\). For \(0\leq j\leq d\) and \(0\leq k\leq M\),
\[
\begin{gathered}
\binom N{k-j}\\
=\binom Mk\frac{(k)_j\,(M-k)_{d-j}}{(M)_d}.
\end{gathered}
\tag{9.2}
\]
Indeed, if \(j\leq k\) and \(k-j\leq N\), then, using \(N-k+j=M-k-(d-j)\) and \(M!/N!=(M)_d\),
\[
\begin{gathered}
\binom N{k-j}\Big/\binom Mk\\
=\frac{k!}{(k-j)!}\cdot\frac{(M-k)!}{(M-k-(d-j))!}\cdot\frac{N!}{M!}\\
=\frac{(k)_j(M-k)_{d-j}}{(M)_d};
\end{gathered}
\]
if \(k<j\), both sides of (9.2) vanish because \((k)_j=0\); and if \(k-j>N\), then \(M-k<d-j\) and both sides vanish because \((M-k)_{d-j}=0\). Put \(\delta=1/M\) and \(t=k/M\in[0,1]\). Dividing the numerator and the denominator of (9.2) by \(M^d\) gives
\[
\begin{gathered}
b_k\\
=\binom Mk\frac{F_\delta(t,1-t)}{\prod_{i=0}^{d-1}(1-i\delta)},\\
F_\delta(x,y)\\
=\sum_{j=0}^dc_j\prod_{i=0}^{j-1}(x-i\delta)\prod_{i=0}^{d-j-1}(y-i\delta).
\end{gathered}
\tag{9.3}
\]
The function \((x,y,\delta)\mapsto F_\delta(x,y)\) is a polynomial, and \(F_0=F\). On the compact set \(\Delta=\{(x,y):x,y\geq0,\ x+y=1\}\), \(F\) has a positive minimum \(\mu\). Here compactness and the minimum assertion follow from Section 1(j). Expanding the finite products shows that \(F_\delta-F_0=\delta R(x,y,\delta)\) for a polynomial \(R\). On \(\Delta\times[0,1]\), all variables have absolute value at most one, so the sum \(C\) of the absolute values of the coefficients of \(R\) bounds \(|R|\). Take \(\delta_0=\min(1/d,\mu/(2(C+1)))\). Then \(|F_\delta-F|\leq C\delta\leq\mu/2\) and \(F_\delta\geq\mu/2\) for \(0\leq\delta\leq\delta_0\). If \(M\geq1/\delta_0\), then \(\delta\leq\delta_0\) and \(i\delta\leq(d-1)/M<1\) for \(i<d\), so every \(b_k\) in (9.3) is positive. \(\square\)

**Theorem 9.5** (Dimension group of the gauge-invariant CAR algebra). For a minimal projection \(e\) of the \(j\)-th summand of \(A_n\), put \(\rho[e]=t^j(1-t)^{n-j}\in\mathbb Z[t]\). This rule extends to an isomorphism of scaled ordered groups
\[
\rho:(K_0(A),K_0(A)^+,\Sigma(A))\longrightarrow(\mathbb Z[t],\mathcal P,\mathcal S),
\]
where
\[
\begin{gathered}
\mathcal P\\
=\{0\}\cup\{f\in\mathbb Z[t]:f(t)>0\\
\text{ for all }0<t<1\},\\
\mathcal S\\
=\{0,1\}\cup\{f\in\mathbb Z[t]:0<f(t)<1\\
\text{ for all }0<t<1\}.
\end{gathered}
\]
The class of the unit is the constant polynomial \(1\).

**Proof.** *The group.* Let \(\rho_n:\mathbb Z^{n+1}\to\mathbb Z[t]\), \(\rho_n(x)=\sum_{j=0}^nx_jt^j(1-t)^{n-j}\). By Proposition 9.3, \((\alpha_nx)_j=x_j+x_{j-1}\) (with \(x_{-1}=x_{n+1}=0\)), so
\[
\begin{gathered}
\rho_{n+1}(\alpha_nx)\\
=\sum_jx_j\big(t^j(1-t)^{n+1-j}+t^{j+1}(1-t)^{n-j}\big)\\
=\sum_jx_jt^j(1-t)^{n-j}\\
=\rho_n(x).
\end{gathered}
\]
So the \(\rho_n\) induce a homomorphism \(\rho:K_0(A)\to\mathbb Z[t]\). Each \(\rho_n\) is injective: under the substitution \(t=s/(1+s)\), the polynomials \(t^j(1-t)^{n-j}\) become \(s^j/(1+s)^n\), which are linearly independent. Hence \(\rho\) is injective. It is onto: a polynomial of degree at most \(n\) with integer coefficients lies in \(\rho_n(\mathbb Z^{n+1})\), because
\[
\begin{gathered}
t^i\\
=t^i\big(t+(1-t)\big)^{n-i}\\
=\sum_{l=0}^{n-i}\binom{n-i}l\,t^{i+l}(1-t)^{n-i-l}.
\end{gathered}
\]

*The cone.* \(\rho(K_0(A)^+)=\bigcup_n\rho_n(\mathbb Z^{n+1}_+)\). A nonzero \(\sum_jx_jt^j(1-t)^{n-j}\) with all \(x_j\geq0\) is positive on \((0,1)\), so this set lies in \(\mathcal P\). Conversely, let \(0\neq f\in\mathcal P\). Divide \(f\) by \(t\) as long as its value at \(0\) vanishes, and by \(t-1\) as long as its value at \(1\) vanishes; division by these monic polynomials keeps integer coefficients. This gives \(f=t^a(1-t)^bg\) with \(a,b\geq0\), \(g\in\mathbb Z[t]\), \(g(0)\neq0\) and \(g(1)\neq0\). On \((0,1)\), \(g=f/(t^a(1-t)^b)>0\); by continuity \(g(0),g(1)\geq0\), hence \(g>0\) on \([0,1]\). Let \(e=\deg g\) and write \(g=\sum_{j=0}^ec_jt^j(1-t)^{e-j}\) with \(c_j\in\mathbb Z\), as above. The form \(G(x,y)=\sum_jc_jx^jy^{e-j}\) satisfies \(G(t,1-t)=g(t)>0\) for \(t\in[0,1]\). By Theorem 9.4, for some \(N\) all coefficients \(b_k\) of \((x+y)^NG(x,y)=\sum_kb_kx^ky^{N+e-k}\) are positive; they are integers. Putting \(x=t\) and \(y=1-t\),
\[
f=\sum_kb_k\,t^{k+a}(1-t)^{N+e-k+b},
\]
which is \(\rho_{N+e+a+b}\) of a vector with entries in \(\mathbb Z_+\). So \(f\in\rho(K_0(A)^+)\).

*The unit and the scale.* The unit of \(A_n\) has rank vector \(\big(\binom n0,\dots,\binom nn\big)\), and \(\sum_j\binom njt^j(1-t)^{n-j}=1\). Since \(1\in A_n\) for all \(n\), Lemma 6.3(5) gives \(\Sigma(A)=\{g:0\leq g\leq[1]\}\), whose image is \(\{f:f\in\mathcal P,\ 1-f\in\mathcal P\}\). An element of this set is \(0\), or \(1\), or is positive on \((0,1)\) together with \(1-f\); this is \(\mathcal S\). \(\square\)

**Example 9.6** (Edge cases). (a) The polynomial \(t(1-t)\) vanishes at both ends of \([0,1]\) and lies in \(\mathcal P\): it is the class of a minimal projection of the middle summand of \(A_2\). (b) The polynomial \((2t-1)^2\) is \(\geq0\) on \([0,1]\) but vanishes at \(\frac12\), so it is not in \(\mathcal P\); neither is its negative. So the order of \(K_0(A)\) is not the pointwise order of functions on \([0,1]\), and \((2t-1)^2\) is not the class of any projection in any matrix algebra over \(A\). (c) Neither \(2t-1\) nor \(1-2t\) lies in \(\mathcal P\), so \(K_0(A)\) is not totally ordered, unlike the dimension groups of UHF algebras.

## 10. Traces

**Definition 10.1.** A *trace* on a C\*-algebra \(A\) is a bounded linear functional \(\tau\) with \(\tau(a)\geq0\) for \(a\geq0\) and \(\tau(xy)=\tau(yx)\) for all \(x,y\in A\). A *tracial state* is a trace of norm one. Let \(T(A)\) be the set of tracial states and \(T_{\leq1}(A)\) the set of traces of norm at most one, both with the weak\* topology (pointwise convergence on \(A\)).

**Lemma 10.2** (Traces on \(M_{\mathbf m}\)). For \(t\in\mathbb R^r_+\) put \(\tau_t(x)=\sum_it_i\operatorname{Tr}(x_i)\). The traces of \(M_{\mathbf m}\) are exactly the \(\tau_t\), \(t\in\mathbb R^r_+\), and \(t_i\) is the value of \(\tau_t\) on any minimal projection of the \(i\)-th summand. Moreover \(\|\tau_t\|=\tau_t(1)=\mathbf m^Tt\). So \(T(M_{\mathbf m})\) is identified with the simplex \(\Delta(\mathbf m)=\{t\in\mathbb R^r_+:\mathbf m^Tt=1\}\), whose vertices are the \(e_i/m_i\).

**Proof.** Let \(\tau\) be a trace, and \(\tau_i\) its restriction to the \(i\)-th summand. Then \(\tau_i(e_{ab})=\tau_i(e_{a1}e_{1b})=\tau_i(e_{1b}e_{a1})=\delta_{ab}\tau_i(e_{11})\), so \(\tau_i=\tau_i(e_{11})\operatorname{Tr}\), and \(t_i=\tau(e^{(i)}_{11})\geq0\) by positivity. Conversely \(\tau_t\) is linear and tracial, and positive since \(\operatorname{Tr}(y^*y)\geq0\). Since \(|\operatorname{Tr}y|\leq k\|y\|\) for \(y\in M_k\), \(|\tau_t(x)|\leq\sum_it_im_i\|x_i\|\leq(\mathbf m^Tt)\|x\|\), with equality for \(x=1\). \(\square\)

**Lemma 10.3** (Pulling back traces). If \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) has multiplicity matrix \(\alpha\), then \(\tau_y\circ\varphi=\tau_{\alpha^Ty}\) for \(y\in\mathbb R^s_+\), and \(\|\tau_y\circ\varphi\|\leq\|\tau_y\|\), with equality when \(\varphi\) is unital.

**Proof.** \(\tau_y\circ\varphi\) is a trace, and on a minimal projection \(e\) of the \(i\)-th summand it takes the value \(\sum_jy_j\operatorname{Tr}\varphi_j(e)=\sum_jy_j\alpha_{ji}=(\alpha^Ty)_i\). Its norm is \(\mathbf m^T\alpha^Ty=(\alpha\mathbf m)^Ty\leq\mathbf n^Ty=\|\tau_y\|\), with equality when \(\alpha\mathbf m=\mathbf n\). \(\square\)

**Theorem 10.4** (Traces as a projective limit). Let \(A\) be an AF-algebra with generating sequence \((A_k)\), \(A_k\cong M_{\mathbf m(k)}\), and multiplicity matrices \(\alpha_k\). For a trace \(\tau\) on \(A\), let \(t^{(k)}(\tau)\in\mathbb R^{r_k}_+\) be the vector with \(\tau|_{A_k}=\tau_{t^{(k)}(\tau)}\).

1. The map \(\tau\mapsto(t^{(k)}(\tau))_k\) is an affine bijection of \(T_{\leq1}(A)\) onto the set of sequences \((t^{(k)})\) with \(t^{(k)}\in\mathbb R^{r_k}_+\), \(\alpha_k^Tt^{(k+1)}=t^{(k)}\) and \(\mathbf m(k)^Tt^{(k)}\leq1\) for all \(k\). It is a homeomorphism for the weak\* topology and the product topology. Moreover \(\|\tau\|=\lim_k\mathbf m(k)^Tt^{(k)}(\tau)\), and the sequence \(\mathbf m(k)^Tt^{(k)}(\tau)\) is nondecreasing.
2. A trace \(\tau\) has norm one exactly when \(\lim_k\mathbf m(k)^Tt^{(k)}(\tau)=1\).
3. If \(A\) is nonzero and unital and \(1_A\in A_k\) for all \(k\), then \(\mathbf m(k)^Tt^{(k)}(\tau)=\tau(1)\) for every \(k\). So \(T(A)\) is affinely homeomorphic to the projective limit of the simplices \(\Delta(\mathbf m(k))\) under the maps \(t\mapsto\alpha_k^Tt\), and \(T(A)\) is not empty.

**Proof.** (1) The restriction of a trace \(\tau\) of norm at most one to \(A_k\) is a trace of norm at most one, so \(\mathbf m(k)^Tt^{(k)}\leq1\) (Lemma 10.2), and \(\alpha_k^Tt^{(k+1)}=t^{(k)}\) by Lemma 10.3 applied to the inclusion. A trace is determined by its values on the dense set \(A_\infty\), so the map is injective. Let \((t^{(k)})\) be a sequence as in the statement. Define \(\tau_0\) on \(A_\infty\) by \(\tau_0(x)=\tau_{t^{(k)}}(x)\) for \(x\in A_k\); by Lemma 10.3 this is consistent. It is linear and tracial, and \(|\tau_0(x)|\leq\|x\|\) by Lemma 10.2. So it extends to a bounded linear functional \(\tau\) of norm at most one on \(A\), tracial by continuity. It is positive: if \(a\geq0\), then \(a=b^*b\) (Section 1(d)); choose \(b_n\in A_\infty\) with \(b_n\to b\); then \(b_n^*b_n\to a\), and \(\tau(b_n^*b_n)\geq0\) because \(b_n^*b_n\) is positive in the finite-dimensional algebra that contains \(b_n\). The map is clearly affine. It is continuous because each coordinate \(t^{(k)}_i(\tau)\) is the value of \(\tau\) at a fixed element. Its inverse is continuous: if \(t_\lambda\to t\) coordinatewise, the corresponding traces converge at every \(x\in A_\infty\), and since all have norm at most one, an \(\varepsilon/3\) argument gives convergence at every \(x\in A\). Finally, \(\|\tau\|\) is the supremum of \(|\tau(x)|\) over the unit ball of the dense subalgebra \(A_\infty\), so \(\|\tau\|=\sup_k\|\tau|_{A_k}\|=\sup_k\mathbf m(k)^Tt^{(k)}\), and \(\|\tau|_{A_k}\|\) increases with \(k\).

(2) is (1) with \(\|\tau\|=1\).

(3) The units of the \(A_k\) all equal \(1_A\), so \(\mathbf m(k)^Tt^{(k)}=\tau(1_A)\), and \(\tau\) is a tracial state exactly when every \(t^{(k)}\) lies in \(\Delta(\mathbf m(k))\). The inclusions are unital, so \(t\mapsto\alpha_k^Tt\) maps \(\Delta(\mathbf m(k+1))\) into \(\Delta(\mathbf m(k))\) (Lemma 10.3). To see that \(T(A)\neq\varnothing\), choose for each \(N\) a point \(s_N\in\Delta(\mathbf m(N))\) (for instance \(e_1/m(N)_1\)), and define a sequence \(t^{[N]}\) by \(t^{[N],(k)}=\alpha_k^T\cdots\alpha_{N-1}^Ts_N\in\Delta(\mathbf m(k))\) for \(k\leq N\) and \(t^{[N],(k)}\) any point of \(\Delta(\mathbf m(k))\) for \(k>N\). Each simplex is compact. For clarity, the diagonal argument uses only Section 1(j): successively take infinite nested subsequences of the indices \(N\), on the \(k\)-th of which the \(k\)-th coordinate converges. Choose the \(\nu\)-th diagonal index from the \(\nu\)-th subsequence, larger than the preceding index. For every fixed \(k\), its tail lies in the \(k\)-th subsequence. Thus there are \(N_1<N_2<\cdots\) such that \(t^{[N_\nu],(k)}\) converges, to \(t^{(k)}\in\Delta(\mathbf m(k))\) say, for every \(k\). The relation \(\alpha_k^Tt^{[N_\nu],(k+1)}=t^{[N_\nu],(k)}\) holds once \(N_\nu>k\), so it passes to the limit. By (1), \((t^{(k)})\) defines a tracial state. \(\square\)

**Example 10.5.** (a) *Compact operators.* All matrices are \((1)\), so a compatible sequence is constant, \(t^{(n)}=t\), with \(nt\leq1\) for all \(n\). So \(t=0\): the only trace of norm at most one is \(0\), and \(T(\mathcal K)=\varnothing\). So a nonunital AF-algebra may have no tracial state.

(b) *Unitization of the compact operators.* With \(t^{(n)}=(a_n,b_n)\) and \(\alpha_n^T=\begin{pmatrix}1&0\\1&1\end{pmatrix}\), compatibility says \(a_n=a_{n+1}\) and \(b_n=a_{n+1}+b_{n+1}\), and normalization says \(na_n+b_n=1\). So \(a_n=a\) is constant with \(na\leq1\) for all \(n\), hence \(a=0\) and \(b_n=1\). So \(\mathcal K+\mathbb C1\) has exactly one tracial state, \(\tau(k+\lambda1)=\lambda\).

*Further reading:* [Takesaki 2003, Section XIX.1]. The explicit quotient trace and Theorem 10.4(3) prove that every nonzero unital AF-algebra has a tracial state. The zero algebra has only the zero functional and no norm-one state.

(c) *UHF algebras.* Compatibility forces \(t^{(n)}=1/d_n\): a UHF algebra has exactly one tracial state. By Exercise 3 below, the gauge-invariant CAR algebra has infinitely many.

## 11. Commutants and the reflected Bratteli diagram

In this section \(\varphi:M_{\mathbf m}\to M_{\mathbf n}\) is a \*-homomorphism with multiplicity matrix \(\alpha\) (an \(s\times r\) matrix) and defect \(d=\mathbf n-\alpha\mathbf m\), and \(\pi:M_{\mathbf n}\to B(H)\) is a unital representation on a finite-dimensional Hilbert space. By Remark 3.3, \(\pi\) has a *multiplicity vector* \(\mathbf n'\in\mathbb Z^s_+\) with \(\sum_jn_jn_j'=\dim H\), and after a unitary change of basis \(H=\bigoplus_j\mathbb C^{n_j}\otimes\mathbb C^{n_j'}\) and \(\pi(y)=\bigoplus_jy_j\otimes1\). For a set \(S\subseteq B(H)\), \(S'\) is its commutant.

**Lemma 11.1.** Let \(H=\bigoplus_i(\mathbb C^{k_i}\otimes K_i)\oplus L\) with finite-dimensional \(K_i\) and \(L\), and let \(Q\subseteq B(H)\) consist of the operators \(\bigoplus_i(y_i\otimes1_{K_i})\oplus0_L\), \(y_i\in M_{k_i}\). Then
\[
\begin{gathered}
Q'\\
=\bigoplus_i\big(1_{k_i}\otimes B(K_i)\big)\oplus B(L)\\
\cong\bigoplus_{i:K_i\neq0}B(K_i)\ \oplus\ B(L).
\end{gathered}
\]

**Proof.** An operator \(T\in Q'\) commutes with the projections onto the spaces \(\mathbb C^{k_i}\otimes K_i\), which are images of units of summands, and hence with the projection onto \(L\). So \(T=\bigoplus_iT_i\oplus T_L\). Write \(T_i\) as a \(k_i\times k_i\) block matrix \((T_{ab})\) with blocks in \(B(K_i)\), using \(\mathbb C^{k_i}\otimes K_i=\bigoplus_a\varepsilon_a\otimes K_i\). Commuting with \(e_{cd}\otimes1\) means \(\delta_{ac}T_{db}=T_{ac}\delta_{db}\) for all \(a,b,c,d\). With \(a=c\) and \(b=d\) this gives \(T_{bb}=T_{cc}\); with \(a=c\) and \(b\neq d\) it gives \(T_{db}=0\). So \(T_i=1\otimes t_i\). There is no condition on \(T_L\). The converse inclusion is clear. \(\square\)

**Theorem 11.2** (Commutants reflect the diagram). Put \(P=\pi(M_{\mathbf n})\) and \(Q=\pi(\varphi(M_{\mathbf m}))\subseteq P\), so that \(P'\subseteq Q'\). Let \(\mathbf m'=\alpha^T\mathbf n'\) (so \(m_i'=\sum_j\alpha_{ji}n_j'\)) and \(d'=\sum_jd_jn_j'\). Then:

1. \(P'\cong\bigoplus_{j:n_j'>0}M_{n_j'}\);
2. \(Q'\cong\bigoplus_{i:m_i'>0}M_{m_i'}\oplus M_{d'}\), where the last summand is present only when \(d'>0\);
3. the inclusion \(P'\subseteq Q'\) is unital, the summand \(M_{n_j'}\) of \(P'\) enters the summand \(M_{m_i'}\) of \(Q'\) with multiplicity \(\alpha_{ji}\), and it enters \(M_{d'}\) with multiplicity \(d_j\).

In particular, if \(\varphi\) is unital and injective and \(\pi\) is faithful, then \(P'\cong M_{\mathbf n'}\), \(Q'\cong M_{\alpha^T\mathbf n'}\), and the multiplicity matrix of \(P'\subseteq Q'\) is the transpose \(\alpha^T\): the Bratteli diagram of \(P'\subseteq Q'\) is the diagram of \(\varphi\) read from right to left, with the new sizes \(\mathbf n'\) and \(\alpha^T\mathbf n'\).

**Proof.** A unitary change of basis in \(H\) conjugates \(P\), \(Q\), \(P'\) and \(Q'\) simultaneously, so we may assume \(\pi\) has the form \(\bigoplus_jy_j\otimes1\). By Theorem 3.2(4), \(\varphi=\operatorname{Ad}U\circ\varphi_\alpha\) for a unitary \(U\in M_{\mathbf n}\). Replacing \(\varphi\) by \(\varphi_\alpha\) replaces \(Q\) and \(Q'\) by their conjugates under \(\pi(U)^*\); since \(\pi(U)\in P\) commutes with every element of \(P'\), this conjugation fixes \(P'\) pointwise and does not change the inclusion. So we may assume \(\varphi=\varphi_\alpha\). Then \(\mathbb C^{n_j}=\bigoplus_i\mathbb C^{m_i}\otimes\mathbb C^{\alpha_{ji}}\oplus\mathbb C^{d_j}\), with \(\varphi(x)_j=\bigoplus_ix_i\otimes1\oplus0\). Regrouping,
\[
\begin{gathered}
H\\
=\bigoplus_i\big(\mathbb C^{m_i}\otimes K_i\big)\oplus L,\\
K_i\\
=\bigoplus_j\mathbb C^{\alpha_{ji}}\otimes\mathbb C^{n_j'},\\
L\\
=\bigoplus_j\mathbb C^{d_j}\otimes\mathbb C^{n_j'},
\end{gathered}
\]
and \(\pi(\varphi(x))=\bigoplus_ix_i\otimes1_{K_i}\oplus0_L\), with \(\dim K_i=m_i'\) and \(\dim L=d'\). Lemma 11.1 gives (2), and, applied to \(P\) itself, (1): \(P'=\bigoplus_j1_{n_j}\otimes B(\mathbb C^{n_j'})\). An element \((t_j)_j\) of \(P'\) acts on \(\mathbb C^{n_j}\otimes\mathbb C^{n_j'}=\bigoplus_i\mathbb C^{m_i}\otimes\mathbb C^{\alpha_{ji}}\otimes\mathbb C^{n_j'}\oplus\mathbb C^{d_j}\otimes\mathbb C^{n_j'}\) as \(1\otimes1\otimes t_j\) on each piece. So in \(B(K_i)\) it is \(\bigoplus_j1_{\alpha_{ji}}\otimes t_j\), and in \(B(L)\) it is \(\bigoplus_j1_{d_j}\otimes t_j\). A minimal projection of \(M_{n_j'}\) therefore has rank \(\alpha_{ji}\) in \(B(K_i)\) and rank \(d_j\) in \(B(L)\), which is (3). Both algebras contain \(1_H\). If \(\varphi\) is unital, \(d=0\); if \(\pi\) is faithful, every \(n_j'\geq1\); and if \(\varphi\) is also injective, every column of \(\alpha\) is nonzero, so every \(m_i'\geq1\). \(\square\)

**Example 11.3.** (a) Take \(\varphi_\alpha:\mathbb C\oplus M_2\to M_5\oplus M_4\) from Example 3.6(a), with \(\alpha=\begin{pmatrix}3&1\\0&2\end{pmatrix}\), and the identity representation of \(M_5\oplus M_4\) on \(\mathbb C^5\oplus\mathbb C^4\), with \(\mathbf n'=(1,1)\). Then \(P'=\mathbb C\oplus\mathbb C\) is the centre of \(M_5\oplus M_4\), and \(\mathbf m'=\alpha^T\mathbf n'=(3,3)\), so \(Q'\cong M_3\oplus M_3\). Directly: \(Q\) acts on \(\mathbb C^9\) as \(\lambda\) on a three-dimensional subspace and as \(y\otimes1\) on \(\mathbb C^2\otimes\mathbb C^3\), so its commutant is \(M_3\oplus(1_2\otimes M_3)\). The pair \((t_1,t_2)\in P'\) becomes \((\operatorname{diag}(t_1,t_1,t_1),\operatorname{diag}(t_1,t_2,t_2))\), with multiplicity matrix \(\begin{pmatrix}3&0\\1&2\end{pmatrix}=\alpha^T\).

(b) *A nonunital inclusion.* Take \(\varphi:M_2\to M_5\), \(x\mapsto\operatorname{diag}(x,x,0)\), with \(\alpha=(2)\) and \(d=(1)\), and \(\pi\) the identity on \(\mathbb C^5\). Then \(P'=\mathbb C1\), and \(Q'=(1_2\otimes M_2)\oplus\mathbb C\cong M_2\oplus\mathbb C\): the defect produces the extra summand \(M_{d'}=\mathbb C\). The scalar \(t\in P'\) becomes \((t1_2,t)\), with multiplicities \(2=\alpha\) and \(1=d\). Without unitality of \(\varphi\), the commutant \(Q'\) is not \(M_{\alpha^T\mathbf n'}=M_2\).

## 12. Group algebras of locally finite groups

For a finite group \(\Gamma\), the group algebra \(\mathbb C[\Gamma]\) is the space of functions \(\Gamma\to\mathbb C\) with the convolution \(f*g(x)=\sum_yf(y)g(y^{-1}x)\) and the involution \(f^*(x)=\overline{f(x^{-1})}\). Let \(\delta_y\) be the function equal to \(1\) at \(y\) and \(0\) elsewhere; then \(\delta_y*\delta_z=\delta_{yz}\) and \(\delta_y^*=\delta_{y^{-1}}\). The *left regular representation* \(\lambda\) of \(\mathbb C[\Gamma]\) on \(\ell^2(\Gamma)\) sends \(\delta_y\) to the unitary \(\lambda_y\), \((\lambda_y\xi)(x)=\xi(y^{-1}x)\), and \(f\) to \(\sum_yf(y)\lambda_y\); since \(\lambda_y\lambda_z=\lambda_{yz}\) and \(\lambda_y^*=\lambda_{y^{-1}}\), it is a \*-homomorphism, and it is injective because \(\lambda(f)\delta_e=f\). So \(\mathbb C[\Gamma]\), with the norm \(\|\lambda(f)\|\), is a finite-dimensional C\*-algebra, and by Section 1(a) this is its only C\*-norm.

**Proposition 12.1.** Let \(\Gamma\) be a finite group.

1. The centre of \(\mathbb C[\Gamma]\) consists of the functions that are constant on conjugacy classes, so the number of summands of \(\mathbb C[\Gamma]\) is the number of conjugacy classes.
2. Unitary representations of \(\Gamma\) on finite-dimensional Hilbert spaces correspond to unital representations of \(\mathbb C[\Gamma]\) by \(\rho(f)=\sum_yf(y)\rho(y)\), with the same invariant subspaces. So the summands of \(\mathbb C[\Gamma]\) correspond to the unitary equivalence classes of irreducible representations of \(\Gamma\), and the size of a summand is the dimension of the representation.
3. If \(\Gamma_0\subseteq\Gamma\) is a subgroup, the inclusion \(\mathbb C[\Gamma_0]\subseteq\mathbb C[\Gamma]\) (extension by zero) is a unital embedding, and its multiplicity matrix has, in the row of an irreducible representation \(\rho\) of \(\Gamma\) and the column of an irreducible representation \(\sigma\) of \(\Gamma_0\), the multiplicity of \(\sigma\) in the restriction of \(\rho\) to \(\Gamma_0\).

**Proof.** (1) \(f\) is central if and only if \(\delta_y*f*\delta_{y^{-1}}=f\) for all \(y\), and \((\delta_y*f*\delta_{y^{-1}})(x)=f(y^{-1}xy)\). The centre has one basis element for each conjugacy class; apply Theorem 2.4. (2) The correspondence is inverse to \(\rho\mapsto(y\mapsto\rho(\delta_y))\), and a subspace is invariant under all \(\rho(y)\) if and only if it is invariant under all \(\rho(f)\). By Remark 3.3, the irreducible representations of \(M_{\mathbf m}\) are the maps to its summands. (3) Restricting \(\rho\) to \(\Gamma_0\) is the same as composing the corresponding representation of \(\mathbb C[\Gamma]\) with the inclusion; by Remark 3.3, the multiplicities of this composite are the multiplicities of the irreducible representations of \(\Gamma_0\) in it. \(\square\)

**Proposition 12.2** (Locally finite groups). Let \(\Gamma\) be the union of an increasing sequence \(\Gamma_1\subseteq\Gamma_2\subseteq\cdots\) of finite subgroups, and let \(\mathbb C[\Gamma]\) be the \*-algebra of finitely supported functions on \(\Gamma\), with convolution and involution as above. Then \(\mathbb C[\Gamma]\) has exactly one C\*-norm, namely \(\|\lambda(f)\|\) for the left regular representation on \(\ell^2(\Gamma)\). Its completion \(C^*(\Gamma)\) is an AF-algebra with generating sequence \((\mathbb C[\Gamma_n])\), and the multiplicities in its Bratteli diagram are the restriction multiplicities of Proposition 12.1(3).

**Proof.** \(\mathbb C[\Gamma]=\bigcup_n\mathbb C[\Gamma_n]\), and the inclusions are \*-homomorphisms. The left regular representation of \(\mathbb C[\Gamma]\) on \(\ell^2(\Gamma)\) is injective (\(\lambda(f)\delta_e=f\)), so \(\|\lambda(f)\|\) is a C\*-norm. Any C\*-norm on \(\mathbb C[\Gamma]\) restricts to a C\*-norm on each \(\mathbb C[\Gamma_n]\), which is unique; so any two C\*-norms agree on each \(\mathbb C[\Gamma_n]\), hence on \(\mathbb C[\Gamma]\). The completion is the closure of the increasing union of the finite-dimensional C\*-algebras \(\mathbb C[\Gamma_n]\). The last statement is Proposition 12.1(3). \(\square\)

**Example 12.3** (The infinite symmetric group). Let \(S_n\) be the group of permutations of \(\{1,\dots,n\}\), embedded in \(S_{n+1}\) as the permutations fixing \(n+1\). The union \(S_\infty\) is the group of permutations of \(\mathbb N\) that move only finitely many points, and \(C^*(S_\infty)\) is an AF-algebra by Proposition 12.2. We compute the first levels of its diagram.

\(\mathbb C[S_1]=\mathbb C\). The group \(S_2\) has two conjugacy classes and order \(2\), so \(\mathbb C[S_2]\cong\mathbb C\oplus\mathbb C\); the two summands are the trivial and the sign representation. The group \(S_3\) has three conjugacy classes and order \(6\), and the only way to write \(6\) as a sum of three squares of positive integers is \(1+1+4\). So \(\mathbb C[S_3]\cong\mathbb C\oplus\mathbb C\oplus M_2\): the trivial representation, the sign representation and a two-dimensional irreducible representation \(\rho\).

We identify \(\rho\). Let \(S_3\) permute the coordinates of \(V=\{v\in\mathbb C^3:v_1+v_2+v_3=0\}\), a two-dimensional unitary representation. A one-dimensional invariant subspace would be spanned by a common eigenvector \(v\) of the transpositions \((12)\) and \((23)\), which generate \(S_3\); since they are involutions, each acts on \(v\) by \(+1\) or \(-1\). If both eigenvalues are \(+1\), the coordinates of \(v\) are equal and their sum zero forces \(v=0\). If \((12)\) has eigenvalue \(-1\), then \(v=(a,-a,0)\). For \((23)\) to have eigenvalue \(+1\) requires \(-a=0\), and eigenvalue \(-1\) requires \(a=0\). In the remaining case, \((12)\) has eigenvalue \(+1\) and \((23)\) has eigenvalue \(-1\); then \(v=(0,a,-a)\) and \(v_1=v_2\) again forces \(a=0\). So \(V\) is irreducible, and since \(\mathbb C[S_3]\) has only one summand of size \(2\), \(V\) is \(\rho\). On \(V\), the transposition \((12)\) fixes \((1,1,-2)\) and negates \((1,-1,0)\), so \(\rho\) restricted to \(S_2\) is the sum of the trivial and the sign representations. The trivial and sign representations of \(S_3\) restrict to those of \(S_2\). With the summands ordered as (trivial, sign, \(\rho\)) and (trivial, sign), the multiplicity matrices of \(\mathbb C[S_1]\subseteq\mathbb C[S_2]\subseteq\mathbb C[S_3]\) are
\[
\begin{pmatrix}1\\1\end{pmatrix},\qquad\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}.
\]
*Unused extension, not proved here.* The general Young-diagram branching rule is not used in the finite-level computations, the locally finite group theorem, or any subsequent proof of this lesson. In general, the irreducible representations of \(S_n\) are indexed by the partitions of \(n\), drawn as Young diagrams, and the restriction of the representation of a diagram to \(S_{n-1}\) is the sum, with multiplicity one each, of the representations of the diagrams obtained by removing one box [Gruson–Serganova 2018, Chapter 6, Theorem 8.8]. So the Bratteli diagram of \(C^*(S_\infty)\) is the graph of Young diagrams ordered by adding one box, and all its multiplicities are \(0\) or \(1\). The case \(n\leq3\) above agrees: \((2)\) and \((1,1)\) come from \((1)\), and the diagram \((2,1)\) of \(\rho\) contains both \((2)\) and \((1,1)\).

## 13. Exercises

**Exercise 1** (medium; The Cantor set). Let \(X=\{0,1\}^{\mathbb N}\) with the product topology. For a word \(w\in\{0,1\}^n\) let \([w]\) be the set of sequences that begin with \(w\), and let \(A_n\subseteq C(X)\) be the span of the indicator functions \(\chi_{[w]}\), \(w\in\{0,1\}^n\).
(a) Show that \(C(X)\) is an AF-algebra with generating sequence \((A_n)\) and that its Bratteli diagram is the binary tree: all sizes are \(1\), and each vertex at level \(n\) is joined by one edge to each of two vertices at level \(n+1\).
(b) Show that the scaled dimension group of \(C(X)\) is isomorphic to \((C(X,\mathbb Z),C(X,\mathbb Z_+),\{\chi_U:U\subseteq X\text{ clopen}\})\).

*Solution.* (a) The \(\chi_{[w]}\), \(w\in\{0,1\}^n\), are mutually orthogonal projections with sum \(1\), so \(A_n\cong\mathbb C^{2^n}\); and \(\chi_{[w]}=\chi_{[w0]}+\chi_{[w1]}\), so \(A_n\subseteq A_{n+1}\), and the minimal projection \(\chi_{[w]}\) of \(A_n\) enters exactly the two summands of \(A_{n+1}\) indexed by \(w0\) and \(w1\), once each. The union \(\bigcup_nA_n\) is a \*-subalgebra of \(C(X)\) that contains the constants and separates points: two different sequences first differ at some place \(n\), and \(\chi_{[w]}\) for the first \(n\) terms of one of them separates them. By the Stone–Weierstrass theorem ([The Stone–Weierstrass theorem for functions vanishing at infinity](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html)), it is dense.
(b) Let \(\rho_n(x)=\sum_wx_w\chi_{[w]}\) for \(x\in\mathbb Z^{\{0,1\}^n}\). These maps are compatible with the connecting maps and injective, so they define an injective homomorphism \(\rho\) from the dimension group into \(C(X,\mathbb Z)\), whose image consists of the functions that depend on finitely many coordinates. Every continuous \(f:X\to\mathbb Z\) is of this kind: each set \(f^{-1}(c)\) is clopen, only finitely many are nonempty because \(X\) is compact, and a clopen set is a union of sets \([w]\) (it is open) and hence a finite union (it is compact); taking all words of a common length \(n\), \(f\in\rho_n(\mathbb Z^{\{0,1\}^n})\). A function in this image is \(\geq0\) exactly when its coefficients at a stage where it is defined are \(\geq0\), and it takes only the values \(0,1\) exactly when its coefficients lie in \(\{0,1\}\), that is, in the scale \(\Sigma_{\mathbf m(n)}\) with \(\mathbf m(n)=(1,\dots,1)\). The \(\{0,1\}\)-valued continuous functions are the \(\chi_U\) with \(U\) clopen.

**Exercise 2** (medium; Two diagrams, one algebra). Let \(A\) be the limit of \(A_1=\mathbb C^2\to A_2\to\cdots\), where \(A_k=M_{2^{k-1}}\oplus M_{2^{k-1}}\) and every connecting map has multiplicity matrix \(\begin{pmatrix}1&1\\1&1\end{pmatrix}\). Show that \(A\) is isomorphic to the CAR algebra, although no \(A_k\) is a full matrix algebra.

*Solution.* The sizes satisfy \(\alpha\mathbf m(k)=(2^k,2^k)^T=\mathbf m(k+1)\), so the standard maps are unital and injective (Corollary 4.10). Let \(\rho_k(x)=(x_1+x_2)/2^k\in\mathbb Z[\frac12]\). Since \(\alpha x=(x_1+x_2,x_1+x_2)^T\), we get \(\rho_{k+1}(\alpha x)=2(x_1+x_2)/2^{k+1}=\rho_k(x)\), so the \(\rho_k\) define \(\rho:K_0(A)\to\mathbb Z[\frac12]\). It is injective: if \(\rho_k(x)=0\), then \(x_1+x_2=0\), so \(\alpha x=0\) and \(\alpha_{\infty,k}(x)=\alpha_{\infty,k+1}(\alpha x)=0\). It is onto, since \(a/2^k=\rho_k(a,0)\). Nonnegative vectors go to nonnegative numbers, and \(a/2^k\geq0\) is \(\rho_k(a,0)\) with \((a,0)\geq0\). The scale of \(A_k\), the vectors with \(0\leq x_1,x_2\leq2^{k-1}\), goes onto \([0,1]\cap2^{-k}\mathbb Z\). So the scaled dimension group of \(A\) is \((\mathbb Z[\frac12],\mathbb Z[\frac12]\cap[0,\infty),\mathbb Z[\frac12]\cap[0,1])\), the same as for the CAR algebra (Example 6.4(c)). By Theorem 8.3, \(A\) is isomorphic to the CAR algebra, and by Theorem 8.3(3) their local algebras are isomorphic too.

**Exercise 3** (easy; Traces of the gauge-invariant CAR algebra). For \(s\in[0,1]\) define vectors \(t^{(n)}\in\mathbb R^{n+1}_+\) by \(t^{(n)}_j=s^j(1-s)^{n-j}\). Show that they define a tracial state \(\tau_s\) of the gauge-invariant CAR algebra \(A\), that \(\tau_s\neq\tau_{s'}\) for \(s\neq s'\), and that \(\tau_s(p)=\rho[p](s)\) for every projection \(p\in A\), with \(\rho\) as in Theorem 9.5.

*Solution.* By Proposition 9.3, \[
\begin{gathered}
(\alpha_n^Tt^{(n+1)})_j\\
=t^{(n+1)}_j+t^{(n+1)}_{j+1}\\
=s^j(1-s)^{n+1-j}+s^{j+1}(1-s)^{n-j}\\
=s^j(1-s)^{n-j}\\
=t^{(n)}_j,
\end{gathered}
\] and \(\mathbf m(n)^Tt^{(n)}=\sum_j\binom njs^j(1-s)^{n-j}=1\). By Theorem 10.4(3), these vectors define a tracial state. Its value on a minimal projection of the summand \(j=1\) of \(A_1\) is \(s\), so different \(s\) give different traces. For a projection \(p\in A_n\) with rank vector \(x\), \[
\begin{gathered}
\tau_s(p)\\
=\sum_jx_js^j(1-s)^{n-j}\\
=\rho_n(x)(s)\\
=\rho[p](s).
\end{gathered}
\] A projection \(p\in A\) is equivalent to a projection \(q\) of some \(A_n\) (Proposition 7.3(1)), say \(p=v^*v\) and \(q=vv^*\). Then \([p]=[q]\), and \(\tau_s(p)=\tau_s(v^*v)=\tau_s(vv^*)=\tau_s(q)\) because \(\tau_s\) is tracial, so the formula holds for \(p\) as well.

**Exercise 4** (medium; AF-algebras are finite). (a) Show that a projection \(q\) in an AF-algebra with \([q]=0\) in \(K_0\) is zero. (b) Deduce that in a unital AF-algebra every \(v\) with \(v^*v=1\) satisfies \(vv^*=1\). (c) Show that the C\*-subalgebra of \(B(\ell^2)\) generated by the unilateral shift is not an AF-algebra.

*Solution.* (a) By Theorem 7.5(1), \(\Phi\) is injective, so \([q]=[0]\) in \(V(A)\): \(q=w^*w\) with \(ww^*=0\). Then \(w=0\), since \(\|w\|^2=\|ww^*\|\), and \(q=0\). (b) \(vv^*\) is a projection equivalent to \(v^*v=1\). The projections \(vv^*\) and \(1-vv^*\) are orthogonal, so \([vv^*]+[1-vv^*]=[1]=[vv^*]\), and \([1-vv^*]=0\) by cancellation (Theorem 7.5(1)). By (a), \(vv^*=1\). (c) The shift \(S\) satisfies \(S^*S=1\neq SS^*\). The algebra it generates is unital, since it contains \(S^*S=1\), so by (b) it is not an AF-algebra.

**Exercise 5** (easy; Stable isomorphism of UHF algebras). Show that the CAR algebra and the UHF algebra of type \((3,3,3,\dots)\) are not stably isomorphic, while the CAR algebra and the UHF algebra of type \((4,4,4,\dots)\) are isomorphic.

*Solution.* By Theorem 8.5 we must compare \((\mathbb Z[\frac12],\geq)\) and \((\mathbb Z[\frac13],\geq)\). A homomorphism \(\theta:\mathbb Z[\frac12]\to\mathbb Z[\frac13]\) satisfies \(2^n\theta(2^{-n})=\theta(1)\), so \(\theta(x)=rx\) with \(r=\theta(1)\in\mathbb Z[\frac13]\). If \(\theta\) is an order isomorphism, then \(r>0\), and \(r/2^n\in\mathbb Z[\frac13]\) for all \(n\). Write \(r=b/3^j\) with \(b\in\mathbb N\); then \(b/(3^j2^n)\in\mathbb Z[\frac13]\) forces \(2^n\) to divide \(b\) for every \(n\), which is impossible. For the second claim, both supernatural numbers are \(2^\infty\), and Corollary 8.6 applies.

## Where this leads

The following four extension results are further directions, not proved here and unused in the proofs and solutions above.

- *Which groups occur.* The scaled ordered groups that are dimension groups of AF-algebras are exactly those that are countable, unperforated (\(ng\geq0\) with \(n\geq1\) implies \(g\geq0\)) and have the Riesz interpolation property, with a scale that generates the group and is hereditary and upward directed (the Effros–Handelman–Shen theorem); its full statement appears in [Blackadar 2017, Theorem V.2.4.20].
- *A local criterion.* A separable C\*-algebra is an AF-algebra as soon as every finite subset lies within any given distance of some finite-dimensional C\*-subalgebra [Blackadar 2025, I.3.2.5]. The proof perturbs finite-dimensional subalgebras by unitaries close to \(1\), in the spirit of Lemma 7.1.
- *Traces and states.* For a unital AF-algebra, the tracial states correspond exactly to the positive homomorphisms \(f:K_0(A)\to\mathbb R\) with \(f[1]=1\) [Blackadar 1998, Section 7.3]; Exercise 3 exhibits a family of such states for the gauge-invariant CAR algebra.
- *Subfactors.* For a subfactor \(N\) of a factor \(M\) of type II\(_1\), the index \([M:N]\) is the coupling constant of \(N\) on \(L^2(M)\), a number in \([1,\infty]\). Jones proved that the index lies in \(\{4\cos^2(\pi/n):n\geq3\}\cup[4,\infty]\) and that each of these values occurs [Jones 1983]. Subfactors are studied through the tower \(N\subseteq M\subseteq M_1\subseteq M_2\subseteq\cdots\) obtained by iterating Jones's basic construction, and through inclusions of finite-dimensional algebras and their Bratteli diagrams; Theorem 11.2 describes how such diagrams change when one passes to commutants. [Takesaki 2003, Chapter XIX] develops this theory starting from the material of this lesson.

*Further reading:* [Takesaki 2003, Chapter XIX]. The alternative expression \(4\cos^2(2\pi/n)\) would give \(0\) at \(n=4\), and therefore cannot give only values satisfying the stated lower bound \(1\).

## References

- [Blackadar 2025] B. Blackadar, [*Classification of C\*-algebras*](https://www.bruceblackadar.com/Mathematics/Class.pdf), incomplete preliminary edition, June 4, 2025.
- [Blackadar 1998] B. Blackadar, *K-Theory for Operator Algebras*, second edition (1998), corrected [author-hosted version](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- [Blackadar 2017] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- [Bratteli 1972] O. Bratteli, [Inductive limits of finite dimensional C\*-algebras](https://www.ams.org/journals/tran/1972-171-00/S0002-9947-1972-0312282-2/S0002-9947-1972-0312282-2.pdf), *Trans. Amer. Math. Soc.* 171 (1972), 195–234.
- [Elliott 1976] G. A. Elliott, On the classification of inductive limits of sequences of semisimple finite-dimensional algebras, *J. Algebra* 38 (1976), 29–44.
- [Glimm 1960] J. G. Glimm, On a certain class of operator algebras, *Trans. Amer. Math. Soc.* 95 (1960), 318–340.
- [Gruson–Serganova 2018] C. Gruson and V. Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Universitext, Springer, Cham, 2018.
- [Jones 1983] V. F. R. Jones, Index for subfactors, *Invent. Math.* 72 (1983), 1–25.
- [Pólya 1928] G. Pólya, [Über positive Darstellung von Polynomen](https://ngzh.ch/wp-content/uploads/2024/07/73_4.pdf), *Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich* 73 (1928), 141–145.
- [Takesaki 2003] M. Takesaki, *Theory of operator algebras III*, Encyclopaedia of Mathematical Sciences 127, Operator Algebras and Non-commutative Geometry 8, Springer-Verlag, Berlin, 2003.

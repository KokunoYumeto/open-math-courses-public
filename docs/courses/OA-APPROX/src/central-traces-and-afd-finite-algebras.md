# Central traces and AFD finite algebras

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

An AFD finite algebra need not be a factor. Its matrix blocks can have different dimensions on different parts of the center. We will cut those dimensions to dyadic values, align an old matrix algebra exactly, and prove that a separable AFD algebra of type II₁ is the tensor product of its center with the tracial infinite product of \(M_2\).

We use the canonical normal center-valued trace \(T:M\to Z(M)\), projection comparison by this trace, and halving in a type II algebra. These are the same exact foundations prerequisites used in [Local approximation and the hyperfinite finite factor](hyperfinite-finite-factors.md). That lesson proves the projection-rotation lemma in arbitrary finite algebras, matrix coordinates, and the bounded-ball completeness of the trace \(2\)-norm. We also retain the precise OA-MOD tracial expectation theorem: \(E_P\) onto a unital subalgebra is normal, ucp, trace preserving and the orthogonal projection in \(L^2\).

Throughout Sections 1–3, \(M\) is of type II₁ and has a faithful normal tracial state \(\tau=\rho T\), where \(\rho\) is a faithful normal state on \(Z=Z(M)\). Set \(\|x\|_2=\tau(x^*x)^{1/2}\). Factoriality and separability are not assumed in those sections. On bounded sets this norm gives sigma-strong* convergence, by the trace-density estimate in the preceding finite-factor lesson. Local AFD and finite-set \(2\)-norm approximation agree: expectations onto the finite-dimensional approximating algebra supply bounded approximants.

## 1. Cutting a projection by a central dimension

**Lemma 1.1.** If \(e\) is a projection and \(a\in Z_+\) satisfies \(a\le T(e)\), there is \(g\le e\) with \(T(g)=a\).

**Proof.** On the central support of \(e\), put \(r=a/T(e)\) by measurable functional calculus, taking zero off that support. It is a bounded central element with \(0\le r\le1\). Repeated halving gives orthogonal pieces \(p_j\le e\), \(j\ge1\), with
\[
T(p_j)=2^{-j}T(e),\qquad \sum_{j\ge1}p_j=e.
\tag{1}
\]
Indeed retain one half at each stage and halve the remaining half. The trace of the decreasing remainder tends to zero; faithfulness and normality of \(T\) make its limiting projection zero. Express the central function \(r\) in binary. Its digits are central projections \(z_j\), with \(r=\sum_{j\ge1}2^{-j}z_j\); at \(r=1\) take all digits one. The strong sum \(g=\sum_jz_jp_j\) is a subprojection of \(e\), and normality gives \(T(g)=rT(e)=a\). \(\square\)

In particular every projection can be split into a prescribed finite list of nonnegative central dimensions summing to its dimension. Apply the lemma successively to the remaining projection. Projections with equal center-valued trace are equivalent by the declared finite comparison theorem.

**Lemma 1.2.** If \(D\subset M\) is a finite-dimensional unital algebra and \(\eta>0\), there exist a unital dyadic matrix factor \(Q\cong M_{2^p}\) and a finite central partition \(z_1,\ldots,z_s\) such that, for \(P=\sum_\ell Qz_\ell\),
\[
\|x-E_P(x)\|_2\le\eta\|x\|\qquad(x\in D).
\tag{2}
\]
The exponent \(p\) can exceed any specified integer.

**Proof.** Write \(D\)'s orthogonal matrix systems as \(f_{ij}^{(k)}\), with sizes \(d_k\), and set \(t_k=T(f_{11}^{(k)})\). Put \(N=2^p\), and round each central dimension downward:
\[
\alpha_k=N^{-1}\lfloor Nt_k\rfloor,
\quad0\le t_k-\alpha_k<N^{-1}.
\tag{3}
\]
Choose \(g_k\le f_{11}^{(k)}\) with \(T(g_k)=\alpha_k\), by Lemma 1.1, and transport it through its block:
\[
\widetilde f_{ij}^{(k)}=f_{i1}^{(k)}g_kf_{1j}^{(k)},\qquad
\|f_{ij}^{(k)}-\widetilde f_{ij}^{(k)}\|_2^2
=\rho(t_k-\alpha_k)<N^{-1}.
\tag{4}
\]
The integer-valued central functions \(r_k=\lfloor Nt_k\rfloor\) take finitely many values. Their joint level sets give a finite central partition \((z_\ell)\). On one such part, split \(g_kz_\ell\) into \(r_k\) pieces of center-valued trace \(z_\ell/N\), and transport each piece through the \(d_k\)-block. When \(r_k=0\) that block contributes no piece. The complement has trace
\[
\left(N-\sum_kd_kr_k\right)z_\ell/N,
\]
and Lemma 1.1 splits it into that many further pieces. There are now exactly \(N\) equivalent diagonals on \(z_\ell\). Complete them to an \(N\)-matrix system while respecting the transported block connections: connect a reference diagonal to the first diagonal of each prescribed block, then use its existing matrix units for the other diagonals. Products of the connecting partial isometries give all the required units.

Do this on each central part, and sum corresponding matrix units over \(\ell\). Their sums form a global unital \(N\)-matrix system with factor span \(Q\). Although the ordering of the old blocks can vary with \(\ell\), every \(\widetilde f_{ij}^{(k)}\) lies in \(P=\sum Qz_\ell\). If \(x=\sum\lambda_{ij}^{(k)}f_{ij}^{(k)}\), then \(|\lambda_{ij}^{(k)}|\le\|x\|\). With \(s=\sum_kd_k^2\), its corresponding truncated sum in \(P\) differs by at most \(sN^{-1/2}\|x\|\). The nearest-point property of \(E_P\) proves (2) when \(p\) is sufficiently large. \(\square\)

The central partition in this construction is essential. The ranks \(r_k\) generally depend on the central variable; a single scalar trace does not record that dependence.

## 2. Keeping an old factor exactly

In a locally AFD \(M\), every finite-dimensional linear subspace \(V\) admits approximation of its entire operator-norm unit ball by an algebra \(P\) as in Lemma 1.2. Choose a basis of \(V\); the sum of the absolute values of its coordinates is bounded on that unit ball. Approximate the basis by a finite-dimensional algebra, then apply Lemma 1.2 to that algebra. The coordinate bound makes the approximation uniform. Expectations preserve the norm bounds.

**Lemma 2.1.** Suppose \(M\) is locally AFD, \(A\cong M_d\) is a unital subfactor with \(d=2^n\), and \(V\subset M\) is finite dimensional. Given \(\varepsilon>0\), there are a dyadic factor \(B\supset A\) and a finite central partition \((z_\ell)\) such that
\[
\|x-E_{\sum Bz_\ell}(x)\|_2\le\varepsilon\|x\|
\qquad(x\in V).
\tag{5}
\]
The size of \(B\) may be made strictly larger than that of \(A\).

**Proof.** Fix matrix units \(e_{ij}\) of \(A\), put \(e=e_{11}\), and set \(W=\mathbb Ce+\sum_{i,j}e_{1i}Ve_{j1}\). The preceding uniformity gives \(P=\sum Qz_\ell\), with \(Q\cong M_{2^p}\), \(p>n\), such that
\(\|a-E_P(a)\|_2\le\delta\|a\|\) on \(W\). Put \(h=E_P(e)\). Then
\[
0\le h\le1,\quad \|h-e\|_2\le\delta,\quad
\|h-h^2\|_2\le3\delta.
\]
For the last inequality use \(h-h^2=(h-e)+(e-h)e+h(e-h)\) and the tracial multiplication bounds. Spectral rounding at \(1/2\) gives \(f=1_{[1/2,1]}(h)\in P\) and \(\|f-e\|_2\le7\delta\): pointwise \(|t-1_{[1/2,1]}(t)|\le2t(1-t)\).

Since \(T(e)=1/d\), contraction of the center expectation gives
\[
\|T(f)-1/d\|_2\le7\delta.
\tag{6}
\]
On each \(z_\ell\), the projection \(f\) has integer matrix rank. Enlarge or shrink it inside that matrix block to a comparable projection of rank \(2^p/d\). Assembling these projections gives \(g\in P\), with \(T(g)=1/d\) and
\[
\|f-g\|_2^2=\rho(|T(f)-1/d|)\le7\delta,
\qquad \|g-e\|_2\le a(\delta):=7\delta+\sqrt{7\delta}.
\tag{7}
\]
Equal center-valued traces give \(g\sim e\). The finite projection-rotation lemma from the preceding lesson gives a unitary \(u\in M\) with \(ugu^*=e\) and \(\|u-1\|_2\le\sqrt2a(\delta)\).

In each central matrix block, split the space into \(d\) equal subspaces with first projection \(g z_\ell\). Summing their matrix units gives unital \(d\)-matrix units \(w_{ij}\in P\), with \(w_{11}=g\). Set
\[
v=\sum_{i=1}^d e_{i1}u w_{1i}.
\tag{8}
\]
Multiplication gives \(v^*v=vv^*=1\) and \(vw_{ij}v^*=e_{ij}\). Thus \(P'=vPv^*\) contains \(A\). Also \(vg=ug\). For \(a=eae\in W\), put \(a'=gE_P(a)g\). Then \(\|a'\|\le\|a\|\), and
\[
\begin{aligned}
\|a-a'\|_2&\le(\delta+2a(\delta))\|a\|,\\
\|a-va'v^*\|_2
&\le K(\delta)\|a\|,\quad
K(\delta)=\delta+(2+2\sqrt2)a(\delta).
\end{aligned}
\tag{9}
\]
The first estimate uses \(a=eae\) and tracial multiplication; the second uses \(va'v^*=ua'u^*\) and \(\|u-1\|_2\). Reconstructing \(x=\sum e_{i1}(e_{1i}xe_{j1})e_{1j}\) shows that its distance to \(P'\) is at most \(d^2K(\delta)\|x\|\).

Each central component of \(P'\) is \(M_{2^p}\), and contains the fixed \(M_d\) algebra \(A z_\ell\). Its relative commutant is \(M_{2^p/d}\). Choose matrix units in these relative commutants and sum them over \(\ell\); they generate a global factor \(C\cong M_{2^p/d}\) commuting with \(A\). Put \(B=A\vee C\cong M_{2^p}\). Matrix coordinates on each central part give \(P'=\sum Bz_\ell\), and \(A\subset B\) exactly. Choose \(\delta\) so \(d^2K(\delta)<\varepsilon\), and use the nearest-point property of its expectation. \(\square\)

Only \(u\), the unitary aligning the first projection, must be close to one. No smallness is required of the full matrix-unit aligning unitary \(v\).

## 3. The center times the tracial infinite product

**Theorem 3.1.** If \(M\) is a locally AFD type II₁ von Neumann algebra with separable predual, then
\[
M\cong Z(M)\bar\otimes R,\qquad
R=\bar\bigotimes_{j\ge1}(M_2,\operatorname{tr}_2).
\tag{10}
\]

**Proof.** Choose a faithful \(\rho\) on \(Z\), hence \(\tau=\rho T\), and a \(2\)-norm dense sequence \((x_j)\) in the unit ball. Separability also supplies a countable family of central projections generating \(Z\): take self-adjoint generators and their rational spectral projections. Start with \(A_0=\mathbb C1\). Apply Lemma 2.1 successively to the span of the first \(n\) elements, with error \(1/n\), retaining \(A_{n-1}\) exactly and increasing the matrix size. Let \(Z_n\) be the finite central algebra generated by all the partitions obtained so far and the first \(n\) chosen central projections. Then
\[
D_n=A_nZ_n
\]
are increasing finite-dimensional unital algebras, and \(\|x_j-E_{D_n}(x_j)\|_2\le1/n\) for \(j\le n\). Their bounded approximants and trace \(2\)-norm completeness imply \((\bigcup D_n)''=M\).

Put \(R_0=(\bigcup A_n)''\). It is finite. Every normalized normal trace on \(R_0\) restricts to the unique normalized trace on every \(A_n\), so all such traces agree on the union and, by normality, on \(R_0\). If its center were nontrivial, composing its center-valued trace with different normal center states would give different normal traces. Thus \(R_0\) is a factor. Its unbounded matrix sizes rule out a finite-dimensional factor, so it is type II₁. Insert the missing dyadic tensor levels between the \(A_n\)'s. Their trace is the product matrix trace; the trace GNS construction identifies \(R_0\) with \(R\), as proved in the infinite-product and finite-factor lessons.

For \(z\in Z_+\), \(\tau(z)>0\), the functional \(x\mapsto\tau(zx)/\tau(z)\) is a normalized normal trace on \(R_0\), hence equals \(\tau|_{R_0}\). By linearity, including \(z=0\),
\[
\tau(zx)=\tau(z)\tau(x)\qquad(z\in Z,\ x\in R_0).
\tag{11}
\]
Consequently multiplication \(Z\odot R_0\to M\) preserves the product trace inner product: expand the pairing of two finite tensor sums and use (11). It extends to a unitary from the product trace Hilbert space onto \(L^2(M,\tau)\), since \(Z\) and \(R_0\) generate \(M\). This unitary intertwines left multiplication by both tensor legs. Their generated von Neumann algebras are therefore normally isomorphic, proving (10). \(\square\)

## 4. AFD gives injectivity

**Theorem 4.1.** A von Neumann algebra generated by an increasing directed family of finite-dimensional unital algebras is injective. Every locally AFD algebra with separable predual has such a generating sequence, and is therefore injective.

**Proof.** For the first assertion, in standard form average over the compact unitary group of each finite algebra:
\[
F_i(b)=\int_{\mathcal U(D_i)}ubu^*\,du\qquad(b\in B(H)).
\tag{12}
\]
These are ucp maps onto \(D_i'\). Product ultraweak compactness gives a pointwise convergent subnet. For each fixed \(j\), its tail values lie in \(D_j'\), so the limit \(F\) takes values in \(\bigcap_jD_j'=M'\). It fixes \(M'\). The map \(b\mapsto JF(JbJ)J\) is a linear unital completely positive retraction onto \(M\): conjugation by \(J\) twice is linear, and at each matrix size it carries positive operator matrices through a conjugate Hilbert-space identification. It fixes \(M\) because \(JMJ=M'\). The norm-one projection criterion gives injectivity. This is also the exact directed permanence result already taught in the averaging lesson; no separability is needed here.

For the second assertion, decompose the identity into its finite type I, finite type II and properly infinite central parts. Local AFD passes to a central part by multiplying the approximating finite algebra by that central projection. The properly infinite part has a dyadic generating sequence by the preceding lesson. The finite type II part has the sequence \(D_n\) constructed in Theorem 3.1. A finite type I algebra is a countable central product of homogeneous algebras \(Z_r\bar\otimes M_r\). Each separable abelian \(Z_r\) is generated by an increasing sequence of finite projection partitions. Tensor these finite central algebras with \(M_r\), retain the first \(n\) homogeneous summands, and add the scalar identity on the remaining central tail. These are increasing finite-dimensional algebras generating the type I part. Combining the three sequences by direct sums gives a generating sequence for \(M\). Apply the first assertion. \(\square\)

There is no implication here that every injective algebra is already proved AFD: the finite injective converse is the next substantive step.

## 5. Problems with complete solutions

**Exercise 1.** Why do the binary halves in (1) sum to \(e\)?

*Solution.* After \(n\) stages the remaining projection has center-valued trace \(2^{-n}T(e)\). The remainders decrease, so their strong limit has trace zero by normality of \(T\). Faithfulness makes that limiting projection zero. Subtracting the remainders from \(e\) gives the increasing partial sums of the selected halves and hence the asserted sum.

**Exercise 2.** For \(M=L^\infty[0,1]\bar\otimes R\), explain why the cut dimension \(a\) may vary with the variable in \([0,1]\).

*Solution.* The center is \(L^\infty[0,1]\), and \(T(e)\) is a measurable dimension function. The binary digits of \(a/T(e)\) are measurable central projections, so Lemma 1.1 chooses different halves on their corresponding measurable parts. The resulting single projection has the prescribed dimension function. This requires no choice of an independently measurable family of arbitrary fibre projections.

**Exercise 3.** Check the error formula (4).

*Solution.* The difference is \(f_{i1}(f_{11}-g_k)f_{1j}\). Its adjoint times itself is \(f_{j1}(f_{11}-g_k)f_{1j}\). Traciality makes its trace \(\tau(f_{11}-g_k)=\rho(t_k-\alpha_k)\). The downward rounding error is less than \(1/N\) as a central function, so its scalar trace is less than \(1/N\).

**Exercise 4.** Why is the number of leftover diagonals in Lemma 1.2 an integer and nonnegative on every central part?

*Solution.* On that part all \(r_k\) are integers, so \(N-\sum d_kr_k\) is an integer. The original unital blocks satisfy \(\sum d_kt_k=1\), and \(r_k/N\le t_k\). Therefore \(\sum d_kr_k\le N\). The residual projection's trace is exactly this nonnegative integer times \(z/N\), which Lemma 1.1 can split into that many pieces.

**Exercise 5.** Derive (6) without replacing center-valued traces by scalar ranks.

*Solution.* The map \(T\) is the \(\tau\)-preserving expectation onto \(Z\), hence is the orthogonal projection in \(L^2\) and contractive there. Since \(T(e)=1/d\), \(\|T(f)-1/d\|_2=\|T(f-e)\|_2\le\|f-e\|_2\le7\delta\). Scalar ranks enter only after restricting to the finite central matrix blocks of \(P\).

**Exercise 6.** Explain why \(\|f-g\|_2^2=\rho(|T(f)-1/d|)\).

*Solution.* On each central block \(f\) and \(g\) are comparable. The square of their difference is their positive projection difference, whose center-valued trace is the absolute difference of their center-valued traces. Sum over the orthogonal central partition and apply \(\tau=\rho T\). Cauchy–Schwarz for the state \(\rho\) bounds the resulting \(L^1\) norm by the \(L^2\) norm in (6).

**Exercise 7.** Verify that the unitary (8) aligns the old matrix units.

*Solution.* In \(v^*v\), \(e_{1i}e_{j1}=\delta_{ij}e\), and \(u^*eu=g\), so the sum reduces to \(\sum_iw_{i1}gw_{1i}=\sum_iw_{ii}=1\). The reverse product similarly gives \(\sum_ie_{ii}=1\). Inserting \(w_{rs}\) between the sums gives \(e_{r1}u g u^*e_{1s}=e_{rs}\). Thus all the old units lie exactly in \(vPv^*\).

**Exercise 8.** Why does the new factor \(B\) in Lemma 2.1 have size \(2^p\) even when the central partition has many pieces?

*Solution.* On every central piece the old algebra acts as \(M_d\), and its relative commutant is \(M_{2^p/d}\). Summing corresponding units of these commutants gives one global matrix factor of that size. Together with the old algebra it gives \(M_d\otimes M_{2^p/d}=M_{2^p}\). The central projections remain in the larger algebra \(\sum Bz_\ell\), rather than becoming extra central projections of the factor \(B\) itself.

**Exercise 9.** Prove that (11) makes multiplication isometric on trace Hilbert spaces.

*Solution.* For a finite sum \(t=\sum_i z_i\otimes x_i\), its product satisfies \(\|\sum_i z_ix_i\|_2^2=\sum_{i,j}\tau(z_i^*z_jx_i^*x_j)=\sum_{i,j}\tau(z_i^*z_j)\tau(x_i^*x_j)\). This is exactly the squared Hilbert tensor-product norm of \(t\). The generation hypothesis makes the image dense, so the isometry extends onto the entire trace Hilbert space and intertwines the two left actions.

**Exercise 10.** Why must the averaging proof use commutants rather than just a pointwise limit of retractions onto the \(D_i\)'s?

*Solution.* A limit of retractions onto \(D_i\) fixes their union, but may be singular and therefore need not fix its ultraweak closure. Averaging instead gives ranges in the decreasing algebras \(D_i'\). For each fixed index all sufficiently late values lie in its closed commutant, so the entire limiting range lies in their intersection \(M'\). The limit fixes that intersection directly. Standard-form conjugation then supplies the retraction onto \(M\).

## References and proof scope

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft, full Proposition 4.1.6, p.61, and Propositions 9.1.6/9.1.8, p.142, supplies the actually read binary trace-cut and finite tracial comparison methods. Section 1 here proves the central-function version, with measurable binary digits and finite joint rank partitions. The source's general finite center-trace existence statement, Remark 9.1.7, is by reference; a complete proof of that unrestricted foundation is not established in these lessons.

The same draft's full Lemma 11.2.1 and Theorem 11.2.2, pp.185–188, supplies the actually read dyadic and trace-GNS methods for factors. Its corner induction invokes amenability. Sections 2–3 here instead prove exact retention and the center tensor-product decomposition from local AFD directly, retaining varying central ranks and the full bounded-ball approximation. Theorem 10.2.4, p.162, gives the actually read compact-unitary/commutant retraction method for \(R\); Section 4 retains arbitrary directed index and treats finite type I, finite type II and properly infinite central parts separately.

The exact center-valued trace, general projection halving/comparison, tracial expectation, standard-form and properly infinite sequential-construction prerequisites remain explicit and pending complete freely accessible closure. No source expression was imported.

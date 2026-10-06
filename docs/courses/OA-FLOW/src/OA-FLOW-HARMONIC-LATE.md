# Reduced Fourier norms, biduality and the returned measure

Original reviewed H2–H5 deduction bodies, placed after the independent [H1 Fourier completion](OA-FLOW-HARMONIC.md#l138-h1). The earlier [H0: compact topology and Hilbert tensor](OA-FLOW-TOPOLOGY.md#l138-h0) and [HR-02](OA-FLOW-HR.md#hr-02), [HR-03](OA-FLOW-HR.md#hr-03), [HR-05](OA-FLOW-HR.md#hr-05), [HR-06](OA-FLOW-HR.md#hr-06), [HR-07](OA-FLOW-HR.md#hr-07), [HR-08](OA-FLOW-HR.md#hr-08), [HR-09](OA-FLOW-HR.md#hr-09) now supply the complete Haar/Radon cone at its declared CF/SC inputs.

The earlier [dual Haar construction](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p2), [scalar Plancherel unitary](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) and [dense inverse-integral proof](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p4) supply the negative-character transform for every LCA group, including its dual. Their complete original proofs use only the earlier CF/SC, topology, HR, L24 and [H1](OA-FLOW-HARMONIC.md#oa-flow.xgaps.cstar.h1) bodies. The later deductions below use those exact results.

<a id="l138-h2"></a>

## H2. The reduced norm and inverse integral

Write \(\Gamma=\widehat G\). Apply the earlier [scalar Plancherel theorem](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) to obtain the onto unitary \(F_G:L^2(G,m)\to L^2(\Gamma,\widehat m)\). For \(h\in L^1(G)\), integration of the unitary translations defines \(\lambda(h)\), with norm at most \(\|h\|_1\), by [L24](OA-FLOW-L24.md#oa-flow.grp.integration). On integrable square-integrable \(f\), qualified Fubini gives
\[
 F_G\lambda(h)f=\widehat h\,F_Gf.
\tag{H2.1}
\]
One may first prove this for \(h,f\in C_c\) and extend in \(L^1\) and \(L^2\), using the common operator bounds. A multiplier by continuous \(k\in C_0(\Gamma)\) has norm \(\|k\|_\infty\): the upper bound is pointwise; for any smaller bound, the open set where its modulus exceeds it contains a nonzero compact bump, and Haar full support makes that bump an \(L^2\) norm test. Thus
\[
 \|\lambda(h)\|=\|\widehat h\|_\infty=\|h\|_u.
\tag{H2.2}
\]
The group quotient is an isometric onto isomorphism by [L24 Section 11](OA-FLOW-L24.md#oa-flow.grp.completions). This statement applies separately to \(G\) and to every other LCA group, including \(\Gamma\).

An integrable nonnegative density \(w\) against Radon Haar gives a finite Radon measure \(w\,dm\). Here are the regularity details used below. [L24's finite-exponent comparison](OA-FLOW-L24.md#oa-flow.grp.haarconventions) gives a Borel \(L^1\) representative on a sigma compact carrier. [SC's simple approximation](OA-FLOW-SC.md#sc-03) gives nonnegative finite sums \(s=\sum_jc_j1_{E_j}\), with all \(E_j\) of finite Haar measure, and \(\|w-s\|_1\) arbitrarily small. For any Borel \(E\), finite-set inner regularity supplies a compact subset of \(E\cap E_j\) of nearly that measure. It also supplies a compact subset \(C\subset E_j\setminus E\) of nearly its measure; the open set \(X\setminus C\) contains \(E\), and its excess measure for the restriction \(1_{E_j}dm\) is arbitrarily small. Thus each finite restricted measure is inner and outer regular, and so is their finite weighted sum. The bound
\[
 \left|\int_B(w-s)\,dm\right|\le\|w-s\|_1
 \quad\text{for every Borel }B
\tag{H2.3a}
\]
transfers these compact and open approximations to \(w\,dm\). This proves the assertion, including compact tail approximation for its whole finite mass. The same estimate applies to the variation density of an integrable complex function.

We will need the inverse integral with its sign fixed. For \(k\in C_c(\Gamma)\), set \(v(x)=\int_\Gamma k(\chi)\chi(x)\,d\widehat m(\chi)\). Compact-tail uniform estimates make \(v\) continuous. Testing \(f\in C_c(G)\), the earlier [finite-measure interchange](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p0) and [Plancherel inverse-domain theorem](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p4) give
\[
 \int_G f(x)\overline{v(x)}\,dm(x)
 =\langle F_Gf,k\rangle
 =\langle f,F_G^*k\rangle.
\tag{H2.3}
\]
This identifies the continuous function \(v\) locally with the \(L^2\) class \(F_G^*k\). The identification needs no global separability assumption: on each sigma compact open coset of [L24 Section 2](OA-FLOW-L24.md#oa-flow.grp.haarconventions), both functions are locally square integrable; compact cutoff approximation of finite-measure indicators shows that a locally integrable difference with zero integrals against every compact continuous test is zero almost everywhere. On a countable compact exhaustion of that coset this gives the asserted local equality. Only countably many cosets of \(F_G^*k\) have a nonzero class. On every other coset the continuous \(v\) is zero everywhere, by Haar full support. Hence \(v\) itself has a sigma compact carrier, belongs to \(L^2(G)\), and equals \(F_G^*k\) there.

The same formula holds for \(k\in L^1(\Gamma)\cap L^2(\Gamma)\): approximate simultaneously in both norms by \(C_c(\Gamma)\). Such approximation follows by truncation to finite-measure bounded functions and the cutoff proof of [L24 Lemma 3.1](OA-FLOW-L24.md#oa-flow.grp.translations). The inverse integrals converge uniformly by the \(L^1\) bound, while the inverse transforms converge in \(L^2\). On each sigma compact coset a common subsequence converges almost everywhere, so the two limits agree locally, and the preceding carrier argument gives global \(L^2\) equality. The integral has the **positive** character sign; \(F_\Gamma\) below has the negative sign.

<a id="l138-h3"></a>

<a id="oa-flow.xgaps.cstar.h3"></a>

## H3. Biduality from the scalar unitary and compact tests

Let \(P=\widehat\Gamma\), which is LCH by [H1](OA-FLOW-HARMONIC.md#l138-h1) applied to \(\Gamma\), and let \(j(x)(\chi)=\chi(x)\). Evaluation \(G\times\Gamma\to\mathbb T\) is jointly continuous: choose a compact neighbourhood of a given \(x\), restrict uniform character error on that neighbourhood, and use continuity of the fixed character in the \(x\) variable. Finite covers of any compact \(K\subset\Gamma\) consequently show
\[
 \sup_{\chi\in K}|\chi(x)-1|\longrightarrow0\quad(x\to0).
\tag{H3.1}
\]
Thus \(j:G\to P\) is a continuous homomorphism.

Given an identity neighbourhood \(U\subset G\), choose relatively compact \(V\) with \(V-V\subset U\), and \(0\ne h\in C_c(G)\) supported in \(V\), using [H0](OA-FLOW-TOPOLOGY.md#l138-h0). The normalized autocorrelation \(c=h*\widetilde h/\|h\|_2^2\), with \(\widetilde h(x)=\overline{h(-x)}\), has support in \(U\), satisfies \(c(0)=1\), and has transform \(w=|\widehat h|^2/\|h\|_2^2\in L^1(\Gamma)\cap L^2(\Gamma)\). The last membership follows from \(\widehat h\in L^2\cap L^\infty\). [H2](OA-FLOW-HARMONIC-LATE.md#l138-h2)'s inverse integral and continuity on both sides give
\[
 c(x)=\int_\Gamma w(\chi)\chi(x)\,d\widehat m(\chi),
 \qquad\int_\Gamma w=1.
\tag{H3.2}
\]
Choose compact \(K\) with \(\int_{\Gamma\setminus K}w<1/8\). If \(\sup_K|\chi(x)-1|<1/4\), then
\[
 |c(x)-1|<\tfrac14+2\cdot\tfrac18=\tfrac12.
\tag{H3.3}
\]
Hence \(x\in U\). This proves that \(j^{-1}\) is continuous on its image and that its kernel is zero: a kernel element lies in every identity neighbourhood. Therefore \(j\) is a topological embedding.

Every locally compact subgroup \(B\subset P\) is closed. Choose an identity neighbourhood in \(B\) with compact closure \(C\subset B\), and an ambient open \(O\subset P\) whose intersection with \(B\) is inside that neighbourhood. Every point of \(O\cap\overline B\) is in the ambient closure of \(O\cap B\), hence in \(C\subset B\). Thus \(B\) is open in \(\overline B\), and its cosets make its complement open there. A dense closed subgroup of its closure is the closure itself. Apply this to \(B=j(G)\).

We prove the finite-density uniqueness needed for surjectivity directly. If \(a\in L^1(\Gamma)\) and \(\int a(\chi)\chi(x)\,d\widehat m=0\) for every \(x\in G\), then \(a=0\). Put \(d\omega=|a|\,d\widehat m\), a finite Radon measure. The evaluation polynomials \(\sum_l c_l\chi(x_l)\) separate points of \(\Gamma\) and are a unital self-adjoint algebra. On compact \(K\subset\Gamma\), [CF Section 5](OA-FLOW-CF.md#oa-flow.cf.5) approximates every continuous \(q:K\to\mathbb C\), \(|q|\le1\), by such polynomials with a **global** modulus bound one. Here is the bound: first choose a polynomial \(p_0\) close on \(K\), and let \(M\ge1\) bound its modulus globally. Approximate \(T(z)=z/\max(1,|z|)\) on \(|z|\le M\) by a polynomial \(Q(z,\bar z)\), with error \(\delta\), using [CF Section 5](OA-FLOW-CF.md#oa-flow.cf.5) again. Then \(p=Q(p_0,\bar p_0)/(1+\delta)\) is still an evaluation polynomial, has global modulus at most one, and has error at most \(2\|p_0-q\|_K+2\delta\) on \(K\). The inequality used is \(|T(z)-q|\le2|z-q|\) for \(|q|\le1\).

If \(m=\|a\|_1>0\), approximate the measurable phase \(\bar a/|a|\), defined as zero at zeros, in \(L^1(\omega)\) by \(q_0\in C_c(\Gamma)\), \(|q_0|\le1\), to error \(m/8\). Finite-measure simple approximation, finite Radon regularity and [H0](OA-FLOW-TOPOLOGY.md#l138-h0) cutoffs prove this density; clipping by \(T\) preserves an arbitrarily small error. Choose compact \(K\) with \(\omega(\Gamma\setminus K)<m/8\) and an evaluation polynomial \(p\), \(|p|\le1\) globally, with \(|p-q_0|_K<1/8\). The hypothesis makes \(\int ap=0\), whereas
\[
 \left|m-\int ap\right|
 \le\left\|\bar a/|a|-q_0\right\|_{L^1(\omega)}
   +\tfrac18\omega(K)+2\omega(\Gamma\setminus K)<\tfrac12m,
\tag{H3.4}
\]
a contradiction. This uniqueness argument uses one finite measure and never an uncountable union of null exceptions.

If the closed subgroup \(B=j(G)\) were proper, choose nonzero nonnegative \(\phi,\psi\in C_c(P)\) with support product contained in an open set disjoint from \(B\). Small neighbourhoods at a point of that open set and at the identity, followed by [H0](OA-FLOW-TOPOLOGY.md#l138-h0), supply them. Their convolution is nonzero: its integral is the positive product of their integrals. Take \(u=F_\Gamma^{-1}\phi\), \(v=F_\Gamma^{-1}\psi\); they are in \(L^2(\Gamma)\), so \(a=uv\in L^1(\Gamma)\). Parseval gives
\[
 \widehat a=\phi*\psi\quad\text{pointwise on }P.
\tag{H3.5}
\]
To verify the formula, for each \(\tau\in P\) write \(\widehat{uv}(\tau)=\langle u,\tau\bar v\rangle\). The conjugation and modulation identities, checked by the integral on \(C_c(\Gamma)\) and extended by unitary density, give \(F_\Gamma(\tau\bar v)(\eta)=\overline{F_\Gamma v(\eta^{-1}\tau)}\). Parseval now gives the convolution integral. Cauchy–Schwarz proves its absolute convergence at each \(\tau\); compact continuous approximations show it is continuous. This justifies ([H3](OA-FLOW-HARMONIC-LATE.md#l138-h3).5) for the stated arbitrary \(L^2\) vectors.

Since \(\widehat a(j(-x))=0\) for every \(x\), the just-proved finite-density uniqueness forces \(a=0\), contrary to the nonzero convolution. Therefore
\[
 j:G\xrightarrow{\cong}\widehat{\widehat G}
\tag{H3.6}
\]
is a topological group isomorphism. This proof uses the earlier [scalar Plancherel theorem](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) on \(G\) and on \(\Gamma\), but imports no separate Bochner or Pontryagin theorem.

<a id="l138-h4"></a>

<a id="oa-flow.xgaps.cstar.h4"></a>

## H4. The Haar measure returns exactly

Let \(m_P\) be the Haar measure on \(P\) paired with \(\widehat m\) by [the dual Haar construction](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p2) and [scalar Plancherel](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3). Haar uniqueness and [H3](OA-FLOW-HARMONIC-LATE.md#l138-h3) give \(m_P=cj_*m\) for some \(c>0\). For \(0\ne\phi\in C_c(\Gamma)\), [H2](OA-FLOW-HARMONIC-LATE.md#l138-h2)'s inverse integral gives
\[
 F_\Gamma\phi(j(x))
 =\int_\Gamma\phi(\chi)\overline{\chi(x)}\,d\widehat m(\chi)
 =F_G^{-1}\phi(-x).
\tag{H4.1}
\]
Reflection preserves abelian Haar measure, by the inversion formula in [L24](OA-FLOW-L24.md#oa-flow.grp.haarconventions) and unimodularity. [Plancherel on both groups](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) yields
\[
 \|\phi\|_2^2=\|F_\Gamma\phi\|_{L^2(P,m_P)}^2
 =c\|F_G^{-1}\phi\|_{L^2(G,m)}^2=c\|\phi\|_2^2.
\tag{H4.2}
\]
Its norm is positive, so \(c=1\). Density and unitarity extend ([H4](OA-FLOW-HARMONIC-LATE.md#l138-h4).1) to all \(L^2(\Gamma)\). Equivalently \(F_\Gamma F_Gf(x)=f(-x)\) as an \(L^2\) equality. No arbitrary scalar is left in the returned Haar measure.

<a id="l138-h5"></a>

<a id="oa-flow.xgaps.cstar.h5"></a><a id="oa-flow.xgaps.cstar.harmonic"></a>

## H5. Free source roles and the actual earlier proofs

[Dana Williams, author draft v3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf), Proposition 3.1, printed page 82 (PDF page 94), motivates the group Fourier completion; its representation-theoretic inputs are replaced by [H1](OA-FLOW-HARMONIC.md#l138-h1)'s complete CF/L24 deduction. [Siegfried Echterhoff, arXiv:1006.4975v4](https://arxiv.org/pdf/1006.4975v4), Remark 3.4(8), pages 9–10, records the same identification with positive characters. [H1](OA-FLOW-HARMONIC.md#l138-h1) uses negative characters by indexing that representation with \(\chi^{-1}\). [H0](OA-FLOW-TOPOLOGY.md#l138-h0) and [H2](OA-FLOW-HARMONIC-LATE.md#l138-h2)–[H4](OA-FLOW-HARMONIC-LATE.md#l138-h4) are independently expressed deductions from the precise earlier inputs above. Neither source's statement of duality is used as a premise for [H3](OA-FLOW-HARMONIC-LATE.md#l138-h3).

The harmonic analytic premises are now the complete earlier [finite-measure interchange](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p0), [positive-coefficient representation](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p1), [dual Haar normalization](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p2), [onto scalar Fourier unitary](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) and [inverse-integral domain](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p4) proofs, at arbitrary LCA generality, together with [HR-01](OA-FLOW-HR.md#hr-01), [HR-02](OA-FLOW-HR.md#hr-02), [HR-03](OA-FLOW-HR.md#hr-03), [HR-04](OA-FLOW-HR.md#hr-04), [HR-05](OA-FLOW-HR.md#hr-05), [HR-06](OA-FLOW-HR.md#hr-06), [HR-07](OA-FLOW-HR.md#hr-07), [HR-08](OA-FLOW-HR.md#hr-08), [HR-09](OA-FLOW-HR.md#hr-09).

The historical harmonic prerequisite scope is now the actual earlier deductions [H0](OA-FLOW-TOPOLOGY.md#l138-h0), [H1](OA-FLOW-HARMONIC.md#l138-h1), [H2](OA-FLOW-HARMONIC-LATE.md#l138-h2), [H3](OA-FLOW-HARMONIC-LATE.md#l138-h3), [H4](OA-FLOW-HARMONIC-LATE.md#l138-h4). Their Haar/Radon premises are now supplied by the complete earlier HR proof cone. The scalar Plancherel premise is now the actual earlier [complete proof](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3), with [paired dual Haar normalization](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p2) and [inverse domain](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p4).


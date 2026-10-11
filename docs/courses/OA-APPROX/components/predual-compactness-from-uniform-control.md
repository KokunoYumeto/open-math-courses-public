# Predual compactness from positive vector control

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original exposition and diagram: public domain (CC0).*

A weakly compact family of normal functionals has one positive normal functional that controls all its values on small bounded operators. We prove that criterion by constructing positive envelopes from vector coefficients. The reverse direction uses a real Hahn–Banach extension on a graph: a functional continuous for the controlling seminorm is a norm limit of normal vector functionals.

The classical criterion is C. A. Akemann's [*The dual space of an operator algebra*, Theorem II.3 and Lemmas II.3a–II.3c, printed pages 289–291](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/). The Baire and projection-cutting mechanism is credited to that proof. The argument here constructs its own positive vector envelopes and proves the particular sequential extraction it needs; the graph-extension argument supplies the converse directly.

We use the complete programme proofs of [H00–H01, Hilbert representation and projection](../src/regular-group-operator-foundations.md#h00), [H03, the concrete predual](../src/regular-group-operator-foundations.md#h03), F01, real and complex Hahn–Banach, [CG01, positive normal supports](standard-cone-geometry.md), and the finite-functional GNS construction in [NC01b, through its normal-inverse paragraph](natural-cone-construction.md#nc01b). The latter construction includes its Banach–Alaoglu proof. Bounded spectral projections and their order inequalities are supplied by [SK](../../OA-MOD/OA-MOD-SK.html), with the scalar measure representation supplied by [RM01–RM05](compact-rmk-from-function-covers.md). These links specify earlier complete arguments; Hilbert spaces and von Neumann algebras have no countability assumption. Inner products are linear in the second variable.

<a id="pc00"></a>
## PC00. The exact criterion

Let \(M\subset B(H)\) be a von Neumann algebra, \(M_*\) its concrete predual, and \(\mathcal K\subset M_*\). The following are equivalent:

1. \(\mathcal K\) is relatively compact for \(\sigma(M_*,M)\).
2. \(\mathcal K\) is norm bounded and there is \(\rho\in M_*^+\) such that, for every \(\varepsilon>0\), some \(\delta>0\) satisfies
\[
 \|x\|\le1,\qquad \rho(x^*x+xx^*)<\delta
 \quad\Longrightarrow\quad
 \sup_{\psi\in\mathcal K}|\psi(x)|<\varepsilon.
 \tag{PC1}
\]

Relative compactness means that the weak closure is compact. Neither the set itself nor its norm closure is asserted to be weakly closed. The empty set and zero algebra satisfy the criterion with \(\rho=0\). We prove the two directions in PC05 and PC07, and derive the faithful-state version in PC08.

<a id="pc01"></a>
## PC01. Positive envelopes constructed from normal vector coefficients

H03 identifies \(M_*\) with a Banach quotient of the completed projective tensor product. Its isometric embedding in \(M^*\) is norm closed, and each \(\psi\in M_*\) has a representation
\[
 \psi(x)=\sum_j\langle u_j,xv_j\rangle,
 \qquad \sum_j\|u_j\|\|v_j\|<\infty.
 \tag{PC2}
\]
Discard zero terms. Replacing \(u_j,v_j\) by positive reciprocal scalar multiples makes their two norms equal, with their common squared norm \(\|u_j\|\|v_j\|\); the coefficient is unchanged. For one chosen such representation set
\[
 \Gamma_\psi(x)=\sum_j
 \bigl(\langle u_j,xu_j\rangle+\langle v_j,xv_j\rangle\bigr).
 \tag{PC3}
\]
This is a positive normal functional. The sums of the vector squares are finite, so H03 puts the coefficient series in \(M_*\), and its value on \(1\) is twice the sum in (PC2). Positivity holds term by term. On a bounded increasing positive net, each vector coefficient increases to its value at the strong supremum; a finite-head and uniformly bounded tail estimate passes that limit through the series. This also verifies normality directly. Choose the zero representation for \(\psi=0\). No uniform bound comparing \(\|\Gamma_\psi\|\) to \(\|\psi\|\) will be required.

Scalar Cauchy–Schwarz for the series gives both estimates
\[
 |\psi(x)|^2\le \Gamma_\psi(1)\Gamma_\psi(x^*x),
 \qquad
 |\psi(x)|^2\le \Gamma_\psi(1)\Gamma_\psi(xx^*).
 \tag{PC4}
\]
For the first use \(\sum\langle u_j,xv_j\rangle\); for the second move \(x\) to \(x^*u_j\) in the first factor. The two partial sums of vector squares are each at most the corresponding value of \(\Gamma_\psi\).

If \(e=s(\Gamma_\psi)\), then \(\Gamma_\psi(1-e)=0\). Every retained \(u_j,v_j\) therefore lies in \(eH\), since the sum of their squared \((1-e)\)-components is zero. Thus
\[
 \psi(x)=\psi(exe).
 \tag{PC5}
\]
More generally, if \(\Gamma_\psi\le c\omega\) for a finite \(c\), CG01 gives \(s(\Gamma_\psi)\le s(\omega)\), and (PC5) holds with that larger support. These envelopes are choices attached to functionals; no linearity or uniqueness of the assignment \(\psi\mapsto\Gamma_\psi\) is asserted.

<a id="pc02"></a>
## PC02. The metric and Banach compactness tools needed here

We first give the Baire argument. If a nonempty complete metric space \(X\) is covered by closed sets \(F_n\) with empty interior, choose a nonempty open ball and then recursively choose closed balls of positive radii less than \(2^{-n}\), each inside the preceding open ball and outside \(F_n\). Such a ball exists because the complement of \(F_n\) is dense and open. The centres are Cauchy. Their limit belongs to every chosen closed ball, hence avoids every \(F_n\), a contradiction. The same construction inside any initial nonempty open set proves the usual dense-open formulation.

For completeness, the uniform boundedness consequence is as follows. For a pointwise bounded family \(\mathcal T\) of bounded linear maps on a Banach space \(X\), the closed sets
\(E_m=\{x:\sup_{T\in\mathcal T}\|Tx\|\le m\}\) cover \(X\). One has interior containing a ball about \(x_0\) of radius \(r>0\). Applying its bound to \(x_0\) and \(x_0+(r/2)y\), for \(\|y\|\le1\), gives \(\|T\|\le4m/r\) uniformly. The dual of any normed space is complete: an operator-norm Cauchy sequence of scalar functionals has pointwise limits, and its Cauchy estimate passes to the limit uniformly on the unit ball. Hahn–Banach F01 gives \(\|z\|=\sup_{\|f\|\le1}|f(z)|\). Consequently every weakly compact subset \(L\) of a normed space is norm bounded: the canonical evaluation maps \(z:X^*\to\mathbb C\), \(z\in L\), are pointwise bounded by compactness, and uniform boundedness on the Banach space \(X^*\) bounds their norms.

Here is the precise sequential extraction used below. If \(L\) is weakly compact in a Banach space \(X\), every sequence \((z_n)\) in \(L\) has a weakly convergent subsequence with limit in \(L\). Put \(Y=\overline{\operatorname{span}}\{z_n:n\ge1\}\). It is separable, by finite rational complex combinations. It is weakly closed: for \(z\notin Y\), Hahn–Banach applied to
\(y+tz\mapsto t\operatorname{dist}(z,Y)\) gives a bounded functional vanishing on \(Y\) and not on \(z\). Thus \(L\cap Y\) is weakly compact and contains the sequence.

If \(Y=0\), extraction is immediate. Otherwise choose a norm-dense sequence \((y_j)\) in its unit sphere, and norm-one functionals \(f_j\in Y^*\) with \(f_j(y_j)=1\). F01 extends them to \(X^*\). They separate points of \(Y\): for a unit vector \(y\), choosing \(\|y-y_j\|<1/2\) gives \(|f_j(y)|>1/2\). Evaluation by these functionals is a continuous injection of the weakly compact set \(L\cap Y\) into \(\mathbb C^{\mathbb N}\). Its inverse on its image is continuous: the image of each closed subset of \(L\cap Y\) is compact and therefore closed in the Hausdorff product. To verify the last fact, separate an exterior point from each point of a compact set and take a finite subcover.

The product's topology on the image is metrized by
\[
 d(z,w)=\sum_{j\ge1}2^{-j}\min\{1,|f_j(z-w)|\}.
 \tag{PC6}
\]
The finite-head and small-tail bounds show that this metric gives exactly coordinate convergence and the product topology. A sequence in a compact metric space has a convergent subsequence: repeatedly cover by finitely many balls of radius \(2^{-k}\), retaining infinitely many indices in one ball at each step. A diagonal choice from the successive retained index sets is Cauchy. The closures of its tails have the finite-intersection property, so compactness supplies a cluster point, to which this Cauchy sequence converges. Applying this to (PC6) proves the claimed weak extraction. No converse sequential compactness theorem is used.

We also use the dual-ball compactness proved inside NC01b: for any normed \(X\), its dual ball is the closed set of linear evaluation families in the product of discs \(\{z:|z|\le\|x\|\}\), \(x\in X\). The complete proof there constructs product limits by coordinate ultrafilters and scalar completeness, and proves the finite-intersection criterion with choice. This is the needed Banach–Alaoglu theorem. Applied to the canonical inclusion of a Banach space in its bidual, it says that a bounded subset is relatively weakly compact whenever its weak* closure in the bidual lies in that Banach space. Indeed the closure is then compact for the restricted weak topology. The reverse assertion follows because a weakly compact subset is compact and closed in the Hausdorff weak* space.

The same filter-extension principle supplies the free ultrafilter used by the ordinary-multiplier witness. For an infinite \(S\subset\mathbb N\), the filter generated by \(S\) and all cofinite sets is proper. The union of a chain of proper filters extending it is proper: finitely many members lie in one filter in the chain. Zorn gives a maximal proper filter. If a set \(A\) is absent, adjoining it would destroy properness, so some member of the filter is disjoint from \(A\); its complement is consequently in the filter. This proves the ultrafilter alternative. The cofinite members exclude every finite set, so the ultrafilter is free and contains \(S\).

<a id="pc03"></a>
## PC03. A complete metric on a faithful normal unit ball

Let \(\omega\) be a finite faithful normal positive functional on \(N\ne0\). The one-block case of NC01b supplies a faithful normal isometric GNS representation \(\pi:N\to B(H_\omega)\), with normal inverse on its von Neumann image, a cyclic vector \(\xi\), and
\[
 \omega(x^*x)=\|\pi(x)\xi\|^2.
 \tag{PC7}
\]
The vector is separating by faithfulness. It is cyclic for \(\pi(N)'\) as well. The projection onto \(\overline{\pi(N)'\xi}\) commutes with \(\pi(N)'\), hence belongs to \(\pi(N)\); it fixes \(\xi\), so the separating property forces that projection to be one.

On \(N_1\) put \(d_\omega(x,y)=\omega((x-y)^*(x-y))^{1/2}\). This is a metric. For a bounded net, convergence in this metric is exactly strong convergence of its GNS operators. The forward implication first uses
\[
 \|\pi(x_i-x)a'\xi\|\le\|a'\|d_\omega(x_i,x)
 \qquad(a'\in\pi(N)'),
\]
and then density of those vectors with the uniform operator bound. The reverse implication tests \(\xi\). Applying the same argument to adjoints proves that
\(\omega((x-y)^*(x-y)+(x-y)(x-y)^*)^{1/2}\) gives bounded strong* convergence.

This metric on \(N_1\) is complete. A \(d_\omega\)-Cauchy sequence makes \(\pi(x_n)\xi\) Cauchy, hence also \(\pi(x_n)a'\xi\) for every \(a'\). The common contraction bound extends convergence to every Hilbert vector. The limits define a bounded linear contraction \(T\), so \(\pi(x_n)\to T\) strongly. The image is strongly closed by NC01b, so \(T=\pi(x)\) for \(x\in N_1\), and (PC7) gives \(d_\omega(x_n,x)\to0\).

Every normal functional is \(d_\omega\)-continuous on \(N_1\). Transport it through the normal inverse of \(\pi\), express it by H03's series coefficients, and use the finite-head and bounded-tail estimate under strong convergence. For a normal positive \(\tau\), bounded strong* convergence of \(\pi(x_i)\) to zero similarly gives
\[
 \tau(x_i^*x_i+x_ix_i^*)\longrightarrow0.
 \tag{PC8}
\]
Both products converge strongly to zero and remain bounded; their series-vector pairings consequently converge. In particular the bounded strong* topology is independent of which faithful normal finite functional is used. Normal positive vector functionals in any other faithful normal concrete presentation give the original strong* tests by (PC8), so the formulation is also independent of presentation.

For a nonfaithful \(\omega\), use the corner \(s(\omega)Ns(\omega)\), where CG01 gives faithfulness. The zero corner causes no exception.

<a id="pc04"></a>
## PC04. Weakly convergent functionals are uniform on a bounded strong* null sequence

Suppose \(\psi_k\to\psi_0\) weakly in \(M_*\), and \(a_n\in M_1\) tends to zero strongly*. We show
\[
 \sup_{k\ge0}|\psi_k(a_n)|\longrightarrow0.
 \tag{PC9}
\]
Uniform boundedness in PC02 gives \(c=\sup_{k\ge0}\|\psi_k\|<\infty\). With the chosen PC01 envelopes put
\[
 \omega=\Gamma_{\psi_0}
   +\sum_{k\ge1}\frac{2^{-k}}{1+\|\Gamma_{\psi_k}\|}\Gamma_{\psi_k},
 \qquad e=s(\omega).
 \tag{PC10}
\]
This is norm convergent, positive and normal. Each envelope's support lies below \(e\), so every \(\psi_k(x)=\psi_k(exe)\). Compression of the bounded strong* null sequence is strong* null in the corner. If that corner is zero the claim follows at once. Otherwise work there with the faithful restriction of \(\omega\). Put \(\theta_k=\psi_k-\psi_0\). These converge weakly to zero and have norm at most \(2c\).

Fix \(0<t<1\). The closed sets
\[
 E_m=\{x\in M_1:|\theta_k(x)|\le t\text{ for every }k\ge m\}
\]
cover the unit ball, because each fixed \(x\) has \(\theta_k(x)\to0\). They are closed for \(d_\omega\), by PC03. Baire and completeness therefore give \(x_0\in M_1\), \(r>0\), and \(m_0\) such that the relative metric ball \(d_\omega(x,x_0)<r\) lies in \(E_{m_0}\).

Set
\[
 h_n=a_n^*a_n+a_na_n^*,\qquad
 p_n=1_{[0,t^2]}(h_n),\qquad q_n=1-p_n.
 \tag{PC11}
\]
Bounded spectral calculus gives \(p_nh_np_n\le t^2p_n\) and \(q_n\le t^{-2}h_n\). Its projections belong to \(M\). Indeed every unitary in \(M'\) commutes with the continuous calculus of \(h_n\); conjugating the Borel extension by that unitary preserves its bounded pointwise sequential limits, so SK's proved uniqueness makes it commute with the Borel extension as well. Unitaries span \(M'\): a self-adjoint contraction \(b\) is the real part of \(b+i(1-b^2)^{1/2}\), and real and imaginary parts treat every element. Thus \(p_n\in M''=M\). The order inequalities yield \(\|a_np_n\|,\|p_na_n\|\le t\), and \(\omega(q_n)\le t^{-2}\omega(h_n)\to0\). PC03 gives strong convergence of \(p_n\) to one in this GNS representation.

Write \(c_n=q_na_nq_n\). The identity
\(a_n=p_na_n+q_na_np_n+c_n\) gives \(\|a_n-c_n\|\le2t\). Also \(c_n^*c_n\le q_n\), so \(d_\omega(c_n,0)^2\le\omega(q_n)\to0\). Bounded multiplication gives \(p_nx_0p_n\to x_0\) strongly, hence in \(d_\omega\). The block sum
\[
 b_n=p_nx_0p_n+c_n
 \tag{PC12}
\]
is a contraction: its two diagonal blocks have orthogonal supports and each has norm at most one. Both \(b_n\) and \(p_nx_0p_n\) eventually lie in the chosen metric ball. Thus for all sufficiently large \(n\) and every \(k\ge m_0\),
\[
 |\theta_k(c_n)|
 =|\theta_k(b_n)-\theta_k(p_nx_0p_n)|\le2t,
 \qquad |\theta_k(a_n)|\le(4c+2)t.
 \tag{PC13}
\]
For the finitely many earlier \(k\), normality and bounded strong* convergence give \(\theta_k(a_n)\to0\). Therefore the limsup of the uniform supremum is at most \((4c+2)t\) for every \(t>0\), hence zero. Finally \(\psi_0(a_n)\to0\), proving (PC9). The proof treats general complex operators; no reduction to a self-adjoint sequence is required.

<a id="pc05"></a>
## PC05. A weakly compact family has a single positive controller

Let \(\mathcal K\) be relatively weakly compact. PC02 gives its norm boundedness. For every \(\varepsilon>0\), there are a finite \(F\subset\mathcal K\) and \(\delta>0\) such that
\[
 x\in M_1,\quad \Gamma_\psi(x^*x+xx^*)<\delta\ (\psi\in F)
 \quad\Longrightarrow\quad
 \sup_{\phi\in\mathcal K}|\phi(x)|<\varepsilon.
 \tag{PC14}
\]
The empty and zero families have this property immediately. If it fails for a nonzero family at some \(2\varepsilon>0\), choose \(\phi_1\in\mathcal K\). The failed supremum is at least \(2\varepsilon\), so a member with modulus at least \(\varepsilon\) can be chosen. Its failure recursively supplies \(a_n\in M_1\) and \(\phi_{n+1}\in\mathcal K\) such that
\[
 \Gamma_{\phi_k}(a_n^*a_n+a_na_n^*)<2^{-n}\quad(k\le n),
 \qquad |\phi_{n+1}(a_n)|\ge\varepsilon.
 \tag{PC15}
\]
Put \(\alpha_k=2^{-k}/(1+\|\Gamma_{\phi_k}\|)\), \(\omega=\sum_k\alpha_k\Gamma_{\phi_k}\), and \(e=s(\omega)\). The sum is norm convergent and \(\|\omega\|\le1\). For \(h_n=a_n^*a_n+a_na_n^*\le2\), the finite-head and tail estimates give
\[
 \omega(h_n)
 \le2^{-n}\sum_{k\le n}\alpha_k
       +2\sum_{k>n}2^{-k}
 \le3\cdot2^{-n}\longrightarrow0.
 \tag{PC16}
\]
Every \(\phi_k\) is supported by \(e\). For \(b_n=ea_ne\), positivity and support compression give
\(\omega(b_n^*b_n+b_nb_n^*)\le\omega(h_n)\). By PC03, \(b_n\to0\) strongly* in \(eMe\).

Apply PC02's extraction to the weak closure of \(\mathcal K\). A subsequence \(\phi_{n_j}\) converges weakly to a normal \(\phi_0\); restriction to \(eMe\) preserves this convergence. PC04 now gives \(\sup_j|\phi_{n_j}(b_n)|\to0\). But support compression and (PC15) say
\( |\phi_{n_j}(b_{n_j-1})|\ge\varepsilon\) whenever \(n_j\ge2\). Since \(n_j-1\to\infty\), this is a contradiction, proving (PC14).

For \(m\ge1\), take \(F_m,\delta_m\) in (PC14) with \(\varepsilon=1/m\), and set
\[
 \gamma_m=\left(1+\sum_{\psi\in F_m}\|\Gamma_\psi\|\right)^{-1},
 \qquad
 \rho=\sum_{m\ge1}2^{-m}\gamma_m\sum_{\psi\in F_m}\Gamma_\psi.
 \tag{PC17}
\]
This is positive and normal, with norm at most one. Given \(\varepsilon>0\), choose \(m>1/\varepsilon\) and \(\delta=2^{-m}\gamma_m\delta_m\). Positivity shows that \(\rho(x^*x+xx^*)<\delta\) forces each envelope in \(F_m\) below \(\delta_m\), so (PC14) gives the strict uniform bound \(1/m<\varepsilon\). This proves (PC1). The controller is a sum of positive envelopes, not a sum of arbitrary complex functionals.

<a id="pc06"></a>
## PC06. Uniform seminorm continuity forces normality

Let \(f\in M^*\) be bounded, \(\rho\in M_*^+\), and suppose that for every \(\eta>0\) there is \(d>0\) such that
\[
 \begin{gathered}
 x\in M_1,\quad q_\rho(x)<d\quad\Longrightarrow\quad |f(x)|<\eta,\\
 q_\rho(x)=\rho(x^*x+xx^*)^{1/2}.
 \end{gathered}
 \tag{PC18}
\]
We prove \(f\in M_*\). The zero functional is immediate. Fix \(\eta>0\), choose \(d\) in (PC18), and put \(C=\|f\|/d\). For every \(x\), scaling to the unit ball and splitting according as \(q_\rho(x)<d\|x\|\) or the reverse gives
\[
 |f(x)|\le\eta\|x\|+Cq_\rho(x).
 \tag{PC19}
\]
Use the normal positive GNS representation \(\pi_\rho\), with cyclic vector \(\xi\), from NC01b; faithfulness is unnecessary. The real-linear map
\[
 T_\rho x=(\pi_\rho(x)\xi,\pi_\rho(x^*)\xi)
 \quad\text{has}\quad \|T_\rho x\|=q_\rho(x).
 \tag{PC20}
\]
Give the underlying real space
\(Z=M_{\mathbb R}\oplus_1(H_\rho\oplus_2H_\rho)_{\mathbb R}\)
the sum norm. On the real-linear graph subspace \(x\mapsto(\eta x,CT_\rho x)\), define a functional with value \(\operatorname{Re}f(x)\). It is well defined because \(\eta>0\), and has norm at most one by (PC19). Real Hahn–Banach F01 extends it to
\(G(z,w)=g(z)+h(w)\) on \(Z\), with \(\|g\|,\|h\|\le1\). Hence
\[
 \operatorname{Re}f(x)=\eta g(x)+Ch(T_\rho x).
 \tag{PC21}
\]
To represent \(h\) on the complex Hilbert sum, complexify it as \(w\mapsto h(w)-ih(iw)\). This is complex linear and bounded by \(2\|h\|\|w\|\). H00's Hilbert representation gives vectors \(u,v\in H_\rho\) such that
\(h(a,b)=\operatorname{Re}\langle u,a\rangle+\operatorname{Re}\langle v,b\rangle\).
Moving the adjoint in the second coefficient shows that
\[
 n_\eta(x)=C\bigl(\langle u,\pi_\rho(x)\xi\rangle
                    +\langle\xi,\pi_\rho(x)v\rangle\bigr)
 \tag{PC22}
\]
is complex linear and normal, and \(\operatorname{Re}n_\eta(x)=Ch(T_\rho x)\). Normality follows from the explicitly proved normal GNS representation; these are its vector coefficients. A complex-linear functional is recovered from its real part by \(f(x)=\operatorname{Re}f(x)-i\operatorname{Re}f(ix)\). Consequently
\[
 f(x)-n_\eta(x)=\eta\bigl(g(x)-ig(ix)\bigr),
 \qquad \|f-n_\eta\|\le2\eta.
 \tag{PC23}
\]
The predual is norm closed in \(M^*\), by H03 and the quotient-distance argument in NC01b. Letting \(\eta\downarrow0\) proves \(f\in M_*\). If \(\rho=0\), (PC18) already makes \(f=0\); its zero GNS representation also fits the estimates. This proof uses no complete-additivity converse or functional polar decomposition.

### The actual graph and error decomposition

The following schematic displays the real graph extension in (PC20)–(PC23). The boxes denote spaces and functional summands; their drawn widths are schematic. Real Hilbert representation turns the lower summand into the two normal vector coefficients in (PC22). Complexification gives the exact error bound \(2\eta\).

<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="680" viewBox="0 0 1120 680" role="img" aria-labelledby="pc-graph-title pc-graph-desc">
<title id="pc-graph-title">Graph extension that proves normality</title>
<desc id="pc-graph-desc">The underlying real algebra maps x to eta x and C T rho x in a real sum space with norm eta norm x plus C q rho x. The real Hahn Banach extension decomposes the real part of f into eta g and C h composed with T rho. Complexification gives f equal to a normal vector functional n eta plus an error of norm at most two eta.</desc>
<defs><marker id="pc-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38536f"/></marker></defs>
<rect width="1120" height="680" rx="18" fill="#f7f9fc"/>
<g font-family="Arial, sans-serif" fill="#152b44">
<text x="34" y="43" font-size="25" font-weight="bold">PC06 · A small norm error plus normal vector coefficients</text>
<rect x="30" y="85" width="265" height="170" rx="12" fill="white" stroke="#bbcbdc"/>
<text x="52" y="122" font-size="22" font-weight="bold">M as a real space</text>
<text x="52" y="161" font-size="20">x ↦ Re f(x)</text>
<text x="52" y="199" font-size="18">|f(x)| ≤ η‖x‖ + C qρ(x)</text>
<text x="52" y="229" font-size="18">η &gt; 0, C = ‖f‖/d</text>
<line x1="305" y1="160" x2="415" y2="160" stroke="#38536f" stroke-width="3" marker-end="url(#pc-arrow)"/>
<text x="316" y="137" font-size="17">graph map</text>
<rect x="430" y="85" width="660" height="170" rx="12" fill="white" stroke="#bbcbdc"/>
<text x="454" y="122" font-size="22" font-weight="bold">Z = Mℝ ⊕₁ (Hρ ⊕₂ Hρ)ℝ</text>
<text x="454" y="161" font-size="20">x ↦ (ηx, C Tρx)</text>
<text x="454" y="198" font-size="19">Tρx = (πρ(x)ξ, πρ(x*)ξ),  ‖Tρx‖ = qρ(x)</text>
<text x="454" y="230" font-size="19">‖(ηx, C Tρx)‖Z = η‖x‖ + C qρ(x)</text>
<line x1="754" y1="270" x2="754" y2="329" stroke="#38536f" stroke-width="3" marker-end="url(#pc-arrow)"/>
<text x="773" y="305" font-size="18">real Hahn–Banach</text>
<rect x="30" y="345" width="500" height="140" rx="12" fill="#fff5e7" stroke="#d9b984"/>
<text x="52" y="382" font-size="22" font-weight="bold">Norm error</text>
<text x="52" y="420" font-size="20">ηg(x),  ‖g‖ ≤ 1</text>
<text x="52" y="457" font-size="19">gc(x) = η(g(x) − i g(ix)),  ‖gc‖ ≤ 2η</text>
<rect x="550" y="345" width="540" height="140" rx="12" fill="#eaf4fb" stroke="#99bdd8"/>
<text x="574" y="382" font-size="22" font-weight="bold">Normal vector part</text>
<text x="574" y="420" font-size="20">C h(Tρx),  ‖h‖ ≤ 1</text>
<text x="574" y="457" font-size="19">Re nη(x) = C h(Tρx); nη is given by PC22</text>
<path d="M 750 330 L 750 315 L 280 315 L 280 334" fill="none" stroke="#38536f" stroke-width="2" marker-end="url(#pc-arrow)"/>
<path d="M 280 495 L 280 531 L 520 531" fill="none" stroke="#38536f" stroke-width="2" marker-end="url(#pc-arrow)"/>
<path d="M 820 495 L 820 531 L 598 531" fill="none" stroke="#38536f" stroke-width="2" marker-end="url(#pc-arrow)"/>
<circle cx="560" cy="531" r="20" fill="white" stroke="#38536f"/><text x="560" y="538" text-anchor="middle" font-size="24">+</text>
<line x1="560" y1="551" x2="560" y2="556" stroke="#38536f" stroke-width="2"/>
<rect x="30" y="556" width="1060" height="96" rx="12" fill="white" stroke="#bbcbdc"/>
<text x="54" y="595" font-size="24" font-weight="bold">f = nη + gc,     nη is normal,     ‖f − nη‖ ≤ 2η</text>
<text x="54" y="630" font-size="20">η ↓ 0 and norm closedness of M_* imply that f belongs to M_*.</text>
</g></svg>

<a id="pc07"></a>
## PC07. The controller makes the weak* closure normal

Suppose \(\mathcal K\) is bounded and satisfies (PC1). Its weak* closure \(L\) in \(M^*\) lies in a fixed dual ball and is compact by PC02. For \(f\in L\), any fixed contraction \(x\), and a bound \(\sup_{\psi\in\mathcal K}|\psi(x)|<\varepsilon/2\), scalar weak* continuity gives \(|f(x)|\le\varepsilon/2<\varepsilon\). Applying (PC1) with \(\varepsilon/2\), and replacing its quadratic threshold by the corresponding square-root threshold, shows that every \(f\in L\) satisfies (PC18). PC06 gives \(L\subset M_*\).

The restricted weak* topology is exactly \(\sigma(M_*,M)\), because H03 identifies \((M_*)^*=M\). Thus \(L\) is a weakly compact set containing \(\mathcal K\). It is also weakly closed, since a compact subset of a Hausdorff space is closed. The weak closure of \(\mathcal K\) lies in \(L\) and is compact. This proves relative weak compactness and finishes the equivalence in PC00.

<a id="pc08"></a>
## PC08. The faithful-state test used by ordinary multipliers

Suppose \(M\ne0\) has a faithful normal state \(\varphi\), and put
\[
 \|x\|_\#=\left(\frac{\varphi(x^*x)+\varphi(xx^*)}{2}\right)^{1/2}.
 \tag{PC24}
\]
For a norm-bounded \(\mathcal K\subset M_*\), PC00 is equivalent to
\[
 \forall\varepsilon>0\ \exists\delta>0:\quad
 x\in M_1,\ \|x\|_\#<\delta
 \quad\Longrightarrow\quad
 \sup_{\psi\in\mathcal K}|\psi(x)|<\varepsilon.
 \tag{PC25}
\]
If (PC25) holds, take \(\rho=\varphi\) in (PC1), with its threshold \(2\delta^2\). Conversely let \(\rho\) be the PC00 controller. On \(M_1\), sufficiently small \(\|x\|_\#\) makes \(\rho(x^*x+xx^*)\) uniformly small. Otherwise some \(a>0\) and contractions \(x_n\) would satisfy \(\|x_n\|_\#<1/n\) but \(\rho(x_n^*x_n+x_nx_n^*)\ge a\). PC03 for \(\varphi\) gives bounded strong* convergence to zero, and (PC8) for \(\rho\) contradicts the latter inequality. Compose this modulus with the one in (PC1) to obtain (PC25).

This is exactly the quadratic predual compactness criterion and faithful-state specialization required by [ordinary multipliers](../src/ordinary-multipliers-and-predual-compactness.md). It places no factor or separable-predual hypothesis on that lesson. It asserts compactness of functional families, rather than preservation of the limit of an individually moving functional.

<a id="pc09"></a>
## PC09. Constructing the Bernoulli measure and its concrete predual

The moving-functional example in that lesson uses \(\Omega=\{-1,1\}^{\mathbb N}\). Here is its probability and predual construction. Give \(\Omega\) the metric
\[
 d(s,t)=\sum_{j\ge1}2^{-j}1_{\{s_j\ne t_j\}}.
 \tag{PC26}
\]
Positivity, symmetry and the triangle inequality follow coordinatewise; zero distance forces agreement of every coordinate. For a sign word \(w\) of length \(n\), its prefix cylinder \([w]\) has diameter at most \(2^{-n}\). It is clopen: a sufficiently small metric ball fixes each of its first \(n\) coordinates, and its complement is a finite union of other prefix cylinders.

The space is compact. If an open cover has no finite subcover, at least one of the two first-coordinate cylinders has no finite subcover; recursively at least one child of each selected cylinder has the same property. The nested words specify a point \(s\). A cover member containing \(s\) contains a metric ball of some radius \(r>0\). For \(2^{-n}<r\), the selected length-\(n\) cylinder lies entirely in that member, contradicting its lack of a finite subcover. This proves compactness directly from finite splitting and countable recursion.

Functions depending on finitely many coordinates form a unital algebra \(\mathcal A\) of continuous cylinder functions. They are uniformly dense in \(C(\Omega)\): for continuous \(f\), compact-metric uniform continuity from SS2 makes the oscillation on every sufficiently long prefix cylinder small. Taking the value at its canonical representative, with all remaining signs \(+1\), supplies a cylinder function uniformly close to \(f\).

If \(f\in\mathcal A\) depends on its first \(n\) coordinates, put
\[
 I(f)=2^{-n}\sum_{w\in\{-1,1\}^n}f(w,+1,+1,\ldots).
 \tag{PC27}
\]
Refining to length \(m\ge n\) repeats each value \(2^{m-n}\) times, so the definition is independent of the stage. It is linear, positive on real nonnegative functions, unital and bounded by \(\|f\|_\infty\). For arbitrary continuous real \(f\), uniformly convergent cylinder approximants make their \(I\)-values Cauchy, independently of the approximants. Their limits define a positive real-linear extension to \(C(\Omega,\mathbb R)\): positivity follows by choosing the nonnegative canonical-value approximants when \(f\ge0\). Apply RM01–RM05 to obtain a finite regular Borel probability \(\mu\) with
\[
 \mu([w])=2^{-n}\quad(|w|=n).
 \tag{PC28}
\]
Thus any specified signs at \(r\) distinct coordinates have joint probability \(2^{-r}\). To verify this even for nonconsecutive coordinates, take a prefix length beyond them and sum the masses of the \(2^{n-r}\) compatible length-\(n\) cylinders. This proves finite independence without importing a product-measure extension theorem. One may use this Borel measure or its completion from SC02; SS4 supplies measurable representatives and the same scalar Hilbert quotient.

The diagram is a schematic of the exact clopen fibres of the first-two-coordinate projection \(\pi_2:\Omega\to\{-1,1\}^2\). Each fibre has mass \(1/4\) and diameter at most \(1/4\) for (PC26); its drawn width is schematic, with the metric bound explicitly displayed. Longer prefixes split each fibre equally and shrink its diameter bound by another factor of two.

<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="360" viewBox="0 0 1080 360" role="img" aria-labelledby="pc-cylinder-title pc-cylinder-desc">
<title id="pc-cylinder-title">Four exact Bernoulli prefix cylinders</title>
<desc id="pc-cylinder-desc">The first two coordinates partition the sign-sequence space into four clopen fibres labelled plus plus, plus minus, minus plus and minus minus. Each has probability one quarter and metric diameter at most one quarter. The two coordinate functions have the corresponding signs and their expectations and mixed expectation are zero.</desc>
<rect width="1080" height="360" rx="18" fill="#f7f9fc"/>
<g font-family="Arial, sans-serif" fill="#152b44">
<text x="32" y="42" font-size="25" font-weight="bold">PC09 · The fibres of π₂(s) = (s₁, s₂)</text>
<text x="32" y="79" font-size="19">Ω is the disjoint union of four clopen cylinders; d(s,t) = Σⱼ≥₁ 2⁻ʲ 1{sⱼ ≠ tⱼ}</text>
<rect x="28" y="110" width="242" height="165" rx="12" fill="#eaf4fb" stroke="#99bdd8"/>
<rect x="286" y="110" width="242" height="165" rx="12" fill="#fff5e7" stroke="#d9b984"/>
<rect x="544" y="110" width="242" height="165" rx="12" fill="#edf5ed" stroke="#aac9aa"/>
<rect x="802" y="110" width="250" height="165" rx="12" fill="#f3edf7" stroke="#c4afd4"/>
<g text-anchor="middle">
<text x="149" y="151" font-size="24" font-weight="bold">[+,+]</text><text x="407" y="151" font-size="24" font-weight="bold">[+,−]</text>
<text x="665" y="151" font-size="24" font-weight="bold">[−,+]</text><text x="927" y="151" font-size="24" font-weight="bold">[−,−]</text>
<g font-size="19"><text x="149" y="192">μ = 1/4, diam ≤ 1/4</text><text x="407" y="192">μ = 1/4, diam ≤ 1/4</text>
<text x="665" y="192">μ = 1/4, diam ≤ 1/4</text><text x="927" y="192">μ = 1/4, diam ≤ 1/4</text>
<text x="149" y="236">(r₁,r₂) = (1,1)</text><text x="407" y="236">(r₁,r₂) = (1,−1)</text>
<text x="665" y="236">(r₁,r₂) = (−1,1)</text><text x="927" y="236">(r₁,r₂) = (−1,−1)</text></g>
</g>
<text x="32" y="316" font-size="22" font-weight="bold">∫ r₁ dμ = ∫ r₂ dμ = 0,   ∫ r₁r₂ dμ = 0,   ∫ rⱼ² dμ = 1</text>
</g></svg>

Put \(H=L^2(\mu)\), supplied by SS1, and represent \(f\in L^\infty(\mu)\) as multiplication \(M_f\) on \(H\). Its norm is \(\|f\|_\infty\): the upper bound follows by integrating \(|f\xi|^2\), while indicators of positive-measure sets where \(|f|\) exceeds any smaller number give the lower bound. The map is a faithful unital *-representation.

Its image is a von Neumann algebra. Suppose \(T\in B(H)\) commutes with all bounded multiplication operators, and put \(g=T1\). For bounded \(f\), commutation gives \(Tf=fg\). From
\(\|1_Ag\|_2\le\|T\|\mu(A)^{1/2}\), every measurable set \(A\) has \(\int_A|g|^2\le\|T\|^2\mu(A)\). A positive-measure set where \(|g|>\|T\|+\varepsilon\) would contradict that inequality. Hence \(g\in L^\infty\). Bounded functions are dense in \(L^2\) by truncation, so \(T=M_g\). The multiplication algebra is therefore its own commutant, hence equals its bicommutant and is strongly closed by H01.

Its predual is exactly \(L^1(\mu)\), with pairing \(h\mapsto\ell_h\), \(\ell_h(M_f)=\int hf\,d\mu\). For an integrable complex \(h\), let
\[
 u=|h|^{1/2},\qquad
 v=\begin{cases}h|h|^{-1/2}&h\ne0,\\0&h=0.\end{cases}
\]
Then \(u,v\in L^2\) and \(\ell_h(M_f)=\langle u,M_fv\rangle\), so it is normal. Its norm is \(\|h\|_1\): the upper bound is the integral inequality, and the bounded function \(f=\overline h/|h|\) off the zero set, zero on that set, attains the integral of \(|h|\).

Conversely every normal functional has H03's series \(\sum_j\langle u_j,M_fv_j\rangle\), with \(\sum_j\|u_j\|_2\|v_j\|_2<\infty\). Cauchy–Schwarz puts each \(\overline u_jv_j\) in \(L^1\), and their sum converges in \(L^1\). The latter completeness follows directly from scalar integration: from an \(L^1\)-Cauchy sequence choose a subsequence whose successive difference norms are below \(2^{-j}\). Monotone convergence makes the sum of their pointwise absolute differences finite outside a measurable null set, with finite integral. The pointwise series defines an integrable limit, and the integral of its tail bounds the subsequence's \(L^1\) error. The full Cauchy sequence has that same limit. Consequently the coefficient series has density \(h=\sum_j\overline u_jv_j\) and equals \(\ell_h\). This proves the predual identification with its exact norm, using no Radon–Nikodym theorem.

Finally \(\varphi(M_f)=\int f\,d\mu=\langle1,M_f1\rangle\) is a faithful normal state, since a nonnegative integrable function of integral zero vanishes almost everywhere. The coordinates \(r_n(s)=s_n\) have mean zero, square one, and pairwise zero inner products by (PC28). Bessel's finite orthogonal-projection estimate gives
\[
 \sum_{n=1}^N\left|\int r_nf\,d\mu\right|^2\le\|f\|_2^2.
 \tag{PC29}
\]
Every bounded \(f\) lies in \(L^2\), since \(\mu(\Omega)=1\), so those integrals tend to zero. Under the just-proved predual identification, \(\ell_{r_n}\to0\) weakly. This supplies the actual probability, normality and weak-null inputs used by the lesson's Bernoulli counterexample.

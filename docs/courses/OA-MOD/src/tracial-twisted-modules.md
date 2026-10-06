# Traces on modules and full correspondences

Original exposition and solved examples: OpenAI Codex (AI), October 2026; CC0-1.0. These are classical module and standard-form calculations, including a corrected classification statement. Inner products are linear in the first variable. Sums over arbitrary index sets mean suprema of finite positive subsums.

A normal unital right action of \(N\) on \(H\) may have a kernel. Put \(L=L^2(N)\), with standard left action \(\lambda\) and right action \(\rho(b)=J\lambda(b^*)J\). Write \(X_H=\operatorname{Hom}_{N^{\mathrm{op}}}(L,H)\) and \(M=\operatorname{End}_{N^{\mathrm{op}}}(H)\). The linking algebra acts on the actual Hilbert space \(V=L\oplus H\):

\[
 R=\operatorname{End}_{N^{\mathrm{op}}}(V),\qquad
 eV=L,\quad fV=H,\quad e+f=1 .
 \tag{TM.1}
\]

Its corners are \(eRe=N\), \(fRf=M\), and \(fRe=X_H\). The identification of \(eRe\) uses \(\lambda\). The following results retain arbitrary cardinalities and zero modules.

## The trace of a rectangular operator determines the module trace

Let \(\tau\) be a faithful normal semifinite trace on \(N\), and use its GNS coordinates for \(L\). There is a unique faithful normal semifinite trace \(\tau_M\) on \(M\) satisfying, for every \(x\in X_H\),

\[
 \tau_M(xx^*)=\tau(x^*x).
 \tag{TM.2}
\]

Both sides may be infinite. There is a faithful normal semifinite trace on \(R\), extending these corner traces, with

\[
 \tau_R(a)=\tau(eae)+\tau_M(faf),\qquad a\in R_+.
 \tag{TM.3}
\]

**Proof.** DK03's cyclic decomposition writes \(H=pL^I\) as a right module, for an arbitrary index set \(I\) and a projection
\(p\in A=B(\ell^2(I))\overline\otimes N\). Adjoin a distinguished coordinate \(0\). With \(B=B(\ell^2(\{0\}\sqcup I))\overline\otimes N\), \(e\) the \(0\)-coordinate projection and \(q=e\oplus p\), the linking algebra is \(qBq\), and \(M=pBp\).

For a positive matrix \(a\in B\), define \(\Theta(a)=\sum_i\tau(a_{ii})\). This is a faithful normal weight: finite diagonal subsums preserve increasing suprema, and a positive matrix with every diagonal compression zero is zero. It is a trace, since, for every bounded matrix \(b\),

\[
 \begin{aligned}
 \Theta(b^*b)&=\sum_{i,j}\tau(b_{ji}^*b_{ji}),\\
 \Theta(bb^*)&=\sum_{i,j}\tau(b_{ij}b_{ij}^*) .
 \end{aligned}
 \tag{TM.4}
\]

Normality justifies the strong positive coefficient sums. Traciality of \(\tau\) equates the two displayed sums, including infinite values. Equality on \(b^*b\) and \(bb^*\) is the trace condition.

Finite diagonal matrices whose entries are finite-trace projections form a net of finite-trace projections \(t\) increasing strongly to \(1\): use TI01 for the entries and finite subsets for the coordinates. Therefore \(\Theta\) is semifinite. The corner restriction is also semifinite. Indeed \(qtq\) are finite-value positive contractions increasing strongly to \(q\), because

\[
 \Theta(qtq)=\Theta(tqt)\leq\Theta(t)<\infty .
 \tag{TM.5}
\]

WG008's finite-positive-contraction criterion applies in \(qBq\). The same argument applies to \(pBp\). Set \(\tau_R=\Theta|_{qBq}\) and \(\tau_M=\Theta|_{pBp}\). Their normality and faithfulness are inherited.

A column \(x\in pBe\) has entries \(x_i\in N\). Equation (TM.4) and normality give

\[
 \begin{aligned}
 \tau_M(xx^*)&=\sum_i\tau(x_ix_i^*),\\
 \tau(x^*x)&=\tau\!\left(\sum_i x_i^*x_i\right)
                  =\sum_i\tau(x_i^*x_i).
 \end{aligned}
 \tag{TM.6}
\]

This proves (TM.2). Equation (TM.3) follows by splitting the diagonal subsum into coordinate \(0\) and the other coordinates.

To prove uniqueness, let \(\sigma\) be any normal trace on \(M\) satisfying (TM.2). For \(a\in M_+\), let \(s_i:L\to L^I\) be the coordinate inclusion and \(x_i=a^{1/2}ps_i\). These are elements of \(X_H\). Finite subsums satisfy

\[
 a=\sup_{F\subseteq I\ {\rm finite}}\sum_{i\in F}x_ix_i^* .
 \tag{TM.7}
\]

Consequently normality and (TM.2) force \(\sigma(a)=\sum_i\tau(x_i^*x_i)\), which is exactly \(\tau_M(a)\). Thus the definition is independent of the chosen column realization. The same argument for \(V\) proves uniqueness of the normalized linking trace. If \(H=0\), its corner and trace are zero, while \(\tau_R=\tau\). No faithfulness of the right action on \(H\) was needed. \(\square\)

## Every module vector is an actual square-integrable column

With the normalization above, write \(E_R=L^2(R,\tau_R)\) and \(E_M=L^2(M,\tau_M)\). There are onto bimodule unitaries

\[
 \begin{gathered}
 U:H\longrightarrow fE_Re,\\
 E_M=fE_Rf .
 \end{gathered}
 \tag{TM.8}
\]

The first target consists of the actual \(\tau_R\)-measurable operators \(T\) affiliated with \(R\) such that \(T=fTe\) and \(\tau_R(T^*T)<\infty\). For a \(\tau\)-bounded vector \(\xi\), \(U\xi\) is its bounded-vector operator \(L_\tau(\xi)\), regarded as the supported block in \(fRe\). In particular

\[
 \|U\xi\|_2^2=\tau_R((U\xi)^*U\xi)=\|\xi\|^2 .
 \tag{TM.9}
\]

The left \(M\)-action and right \(N\)-action become multiplication of measurable operators, with the closed-product convention of MT09.

**Proof.** First use the full standard column space \(L^I\). The trace GNS space of \(B\), or equivalently its concrete measurable \(L^2\) by TI15, is
\(\ell^2((\{0\}\sqcup I)^2,L^2(N,\tau))\); DK03 proves the entire matrix GNS identification, not just finite matrices. Its \(I\)-by-\(0\) corner is precisely \(L^I\). Compression by \(q=e\oplus p\) turns that corner into \(pL^I=H\). To check that the compressed GNS space is the GNS space of \(qBq\), apply TI11 on the left and right to bounded finite-trace diagonal projections \(t\uparrow1\). Finite-energy \(qBq\) vectors are dense in \(qL^2(B,\Theta)q\): for any vector there, approximate it in \(L^2(B,\Theta)\) by bounded finite-energy \(b\), then compress \(qbq\); traciality bounds both compressions in \(L^2\), and \(qbq\) has finite energy. Their GNS inner products are exactly the restricted trace inner products. This proves (TM.8), including its second equality.

A \(\tau\)-bounded vector has a bounded column \(x=L_\tau(\xi)\) with finite energy, by DK02, FU03 and DK03's full column dictionary. Its GNS vector in the \(f,e\)-corner has entries exactly those of \(\xi\); hence \(U\xi=x\). The finite-energy columns have dense vectors by FU03. TI15 identifies their Hilbert completion with all the measurable \(L^2\) columns. Thus no boundedness assumption remains on a general \(U\xi\).

Here is the precise operator meaning in the original representation \(R\subseteq B(L\oplus H)\). MT08 realizes \(T=U\xi\) as a closed densely defined affiliated operator on \(V\). Since \(T=fTe\), its polar modulus is supported by \(e\); it vanishes on \(fV\), and its nonzero block is a closed operator

\[
 \begin{gathered}
 t_\xi:D(t_\xi)\longrightarrow H,\\
 D(t_\xi)\subseteq L^2(N,\tau).
 \end{gathered}
 \tag{TM.10}
\]

For every \(b\in\mathfrak n_\tau=N\cap L^2(N,\tau)\),

\[
 \Lambda_\tau(b)\in D(t_\xi),\qquad
 t_\xi\Lambda_\tau(b)=\xi b .
 \tag{TM.11}
\]

Indeed let \(r_n=1_{[0,n]}(|T|)\) in the \(e\)-corner, including the zero spectral subspace there. The bounded finite-energy columns \(Tr_n\) have vectors \(\xi_n=U^{-1}(Tr_n)\to\xi\). The bounded-column case gives
\(Tr_n\Lambda_\tau(b)=\xi_n b\to\xi b\).
The spectral theorem characterizes \(D(t_\xi)\) by boundedness of these truncated image norms; it gives (TM.11) and its limit. For the finite-energy claim, \(\tau_R(r_nT^*Tr_n)\leq\tau_R(T^*T)\); convergence in \(L^2\) is the vanishing spectral integral over \((n,\infty)\).

This initial domain is a graph core. For \(\eta\in D(t_\xi)\), \(r_n\eta\to\eta\) and \(t_\xi r_n\eta\to t_\xi\eta\). For fixed \(n\), approximate \(\eta\) in \(L\) by \(\Lambda_\tau(b_j)\), \(b_j\in\mathfrak n_\tau\); then \(r_n\Lambda_\tau(b_j)=\Lambda_\tau(r_nb_j)\) stays in that ideal, and \(t_\xi r_n\) is bounded. This approximates each truncated graph. Thus (TM.11), followed by graph closure, determines the whole \(t_\xi\). It is bounded exactly when \(\xi\in D(H,\tau)\), by the defining estimate on that dense ideal and FU03's injectivity.

Finally the represented block has spectral trace tails
\(\tau_R(1_{(a,\infty)}(|T|))\leq a^{-2}\|\xi\|^2\); these tend to zero and prove measurability in the original representation as well. The diagonal corner in (TM.8) has Hilbert space \(L^2(M)\). The nonzero column operator in (TM.10) instead has range \(H=fV\). Those are the targets fixed by the stated linking representation; there is no implicit choice of a vector in the conjugate module to turn a column into a diagonal operator. \(\square\)

## Twists compose in the stated order

For a normal automorphism \(\alpha\) of \(N\), let \(H_\alpha\) have underlying standard Hilbert space \(L\), ordinary left action and right action \(\rho(\alpha(b))\). SF12's canonical standard implementer \(u_\alpha\) commutes with \(J\), preserves the natural cone, and satisfies \(u_\alpha u_\beta=u_{\alpha\circ\beta}\). Then

\[
 H_\alpha\boxtimes_N H_\beta
        \cong H_{\alpha\circ\beta}.
 \tag{TM.12}
\]

The isomorphisms agree with the standard unit maps and associator. They give a faithful realization of \(\operatorname{Out}(N)\) as isomorphism classes of invertible correspondences.

**Proof.** The right intertwiners \(L\to H_\alpha\) are exactly
\(T_x=\lambda(x)u_\alpha\), \(x\in N\). To check this assertion directly, \(u_\alpha\rho(b)u_\alpha^*=\rho(\alpha(b))\); therefore \(Tu_\alpha^*\) commutes with \(\rho(N)\), whose commutant is \(\lambda(N)\). Their coefficients are

\[
 T_y^*T_x=\lambda(\alpha^{-1}(y^*x)).
 \tag{TM.13}
\]

In FU02's complete intertwiner construction prescribe

\[
 V_{\alpha,\beta}[T_x,\eta]=\lambda(x)u_\alpha\eta .
 \tag{TM.14}
\]

The inner product of the proposed images for \(x,\eta\) and \(y,\zeta\) is
\(\langle\lambda(\alpha^{-1}(y^*x))\eta,\zeta\rangle\), exactly the fusion coefficient. Expanding every finite-sum cross term proves preservation of the full semidefinite form and its radical. The descended isometry is onto because \(V_{\alpha,\beta}[u_\alpha,\eta]=u_\alpha\eta\) ranges over \(L\). Left multiplication sends \(T_x\) to \(T_{ax}\). On the right,

\[
 u_\alpha\rho(\beta(b))
       =\rho(\alpha(\beta(b)))u_\alpha .
 \tag{TM.15}
\]

These are precisely the target actions.

For three twists, either associative prescription on total iterated intertwiner generators gives
\(\lambda(x\alpha(y))u_{\alpha\circ\beta}\eta\).
FU08's associator maps the corresponding creation-operator generators to each other. Boundedness and density prove equality on the whole completion. For the identity automorphism, \(u_{\mathrm{id}}=1\), and (TM.14) is the ordinary fusion unit map. In particular \(H_{\alpha^{-1}}\) is a two-sided inverse.

A bimodule unitary \(F:H_\alpha\to H_\beta\) commutes with the left action and has the form \(F=\rho(v)\) for a unitary \(v\in N\). Its right intertwining equation, using reversal of multiplication by \(\rho\), says

\[
 \alpha(b)v=v\beta(b),\qquad b\in N .
 \tag{TM.16}
\]

Thus it exists exactly when \(\alpha=\operatorname{Ad}(v)\circ\beta\). Conversely that equality makes \(\rho(v)\) the required unitary. This proves the assertion about \(\operatorname{Out}(N)\). FU09 transports all these intertwiner formulas through its specified comparison for faithful reference weights; it does not keep different weighted-vector symbols unchanged. The argument, already used for the composition calculation in FU11, needs no trace or countability assumption. \(\square\)

## A concrete finite factor which is its own matrix amplification

There exists an infinite-dimensional finite factor \(Q\), with faithful normal tracial state \(\nu\), and a normal unital isomorphism satisfying the following trace identity. Put \(\nu_2=\operatorname{tr}_2\otimes\nu\).

\[
 \begin{gathered}
 \varphi:Q\longrightarrow M_2(Q),\\
 \nu_2\circ\varphi=\nu .
 \end{gathered}
 \tag{TM.17}
\]

Here \(\operatorname{tr}_2=\tfrac12\operatorname{Tr}_2\), so \(\operatorname{tr}_2(1)=1\). We use OA-APPROX's infinite-product construction and specialize its prefix/tail splitting to identical matrix factors.

**Proof.** The construction is *Infinite tensor products and their reference states*, §2, (4)–(6). Its Theorem 4.1 gives the finite-part expectations and their strong-star convergence; Theorem 5.1, Proposition 5.2 and Corollary 5.3, together with grouping (13) give factoriality, the faithful normal product trace, finiteness and the prefix/tail decomposition. All component algebras below are nonzero finite factors and all reference states are their faithful normal normalized traces, exactly as required there.

In those constructions take

\[
 \begin{gathered}
 Q=\bigotimes_{k=1}^{\infty}
       \bigl(M_2(\mathbb C),\operatorname{tr}_2\bigr),\qquad
 \nu=\bigotimes_{k=1}^{\infty}\operatorname{tr}_2,\\
 K=\bigotimes_{k=1}^{\infty}
       \bigl(L^2(M_2(\mathbb C),\operatorname{tr}_2),1\bigr).
 \end{gathered}
 \tag{TM.18}
\]

Thus \(Q\subseteq B(K)\) is a finite factor with faithful normal tracial state \(\nu\). The local algebras \(A_n=M_{2^n}(\mathbb C)\) embed faithfully and have strong-dense union, so \(Q\) is infinite dimensional and hyperfinite.

Let \(Q_{\mathrm{tail}}\), with trace \(\nu_{\mathrm{tail}}\), be the product on the indices \(k\geq2\). Grouping (4) and (13) gives the normal unital isomorphism

\[
 \begin{gathered}
 \theta:Q\longrightarrow
      M_2(\mathbb C)\overline\otimes Q_{\mathrm{tail}},\\
 (\operatorname{tr}_2\otimes\nu_{\mathrm{tail}})
       \circ\theta=\nu .
 \end{gathered}
 \tag{TM.19}
\]

On a local product, \(\theta\) splits off its first matrix factor. Relabeling \(k+1\) as \(k\) sends finite-support tail vectors to finite-support vectors of \(K\), preserves their inner products and reference vectors, and extends to a unitary. Write this unitary as \(U:K_{\mathrm{tail}}\to K\), with \(U(\bigotimes_{j\geq2}\xi_j)=\bigotimes_{k\geq1}\xi_{k+1}\) on finite-support vectors. The isomorphism \(r(y)=UyU^*\) is normal, unital and onto; it satisfies

\[
 \begin{gathered}
 r:Q_{\mathrm{tail}}\longrightarrow Q,\qquad
 \nu\circ r=\nu_{\mathrm{tail}},\\
 \varphi=(\operatorname{id}_{M_2}\otimes r)\circ\theta .
 \end{gathered}
 \tag{TM.20}
\]

The state identity follows on local products and then by normality. Identifying \(M_2(\mathbb C)\overline\otimes Q\) with \(M_2(Q)\) now gives

\[
 (\operatorname{tr}_2\otimes\nu)\circ\varphi
   =(\operatorname{tr}_2\otimes\nu_{\mathrm{tail}})\circ\theta
   =\nu .
\]

This proves (TM.17) by specialization and reindexing. \(\square\)

## Fullness does not force an automorphism twist

Call an \(N\)-\(N\) correspondence full when its faithful normal left and right actions are mutual commutants. There are full correspondences which are not automorphism twists. A correct positive statement is: a full correspondence whose right module is unitarily isomorphic to the standard right module is an automorphism twist.

**Proof of the obstruction.** Use \(Q,\nu,\varphi\) from TM04 and put \(H=L^2(Q,\nu)\oplus L^2(Q,\nu)\). Let the right action be componentwise multiplication and the left action be \(\varphi(a)\), with matrix entries acting by left multiplication. The standard-form commutant identity and matrix coordinate compression give

\[
 \begin{gathered}
 \rho_H(Q)'=M_2(Q),\\
 M_2(Q)=\lambda_H(Q),\\
 \lambda_H(Q)'=\rho_H(Q).
 \end{gathered}
 \tag{TM.21}
\]

The middle equality follows from the surjectivity of \(\varphi\); the third equality follows by taking commutants of the first. Both actions are normal, unital and faithful.

Every \(H_\alpha\) has standard underlying right module: \(u_\alpha:L^2(Q)\to H_\alpha\) is a right-module unitary. A right-module unitary \(W:L^2(Q)\to H\) would be a bounded column \((w_1,w_2)^{\mathsf T}\) with entries in \(Q\), since each coordinate intertwiner commutes with the standard right action. It would satisfy \(W^*W=1\), \(WW^*=I_2\). The unnormalized matrix trace yields

\[
 \begin{aligned}
 2&=(\operatorname{Tr}_2\otimes\nu)(WW^*)\\
  &=\nu(w_1^*w_1+w_2^*w_2)=1 .
 \end{aligned}
 \tag{TM.22}
\]

This is impossible. The obstruction measures module multiplicity, not the ordinary Hilbert dimensions; both Hilbert spaces in this example are infinite dimensional.

**Proof of the corrected positive statement.** Let \(W:L^2(N)\to H\) be a right-module unitary and transport the left action along \(W\). Its image lies in \(\lambda(N)\), and fullness makes that image all of \(\lambda(N)\). Faithfulness gives a normal unital automorphism \(\beta\) with
\(W^*\lambda_H(a)W=\lambda(\beta(a))\).
Its inverse is normal, since a bijective normal positive order isomorphism preserves increasing bounded suprema in both directions. The unitary \(u_{\beta^{-1}}W^*:H\to L^2(N)\) transports the left action to \(\lambda(a)\) and the right action to \(\rho(\beta^{-1}(b))\). Thus

\[
 H\cong H_{\beta^{-1}} .
 \tag{TM.23}
\]

TM03 identifies the ambiguity in the chosen right-module unitary with inner automorphisms. This proves the replacement at the exact extra hypothesis and leaves the full counterexample intact. \(\square\)

## Two solved tests of normalization and composition

**Problem 1.** Take \(N=M_d(\mathbb C)\), \(\tau=c\operatorname{Tr}_d\) with \(c>0\), and the right module \(H=M_{m,d}(\mathbb C)\), \(m\geq1\), with \(\|\xi\|^2=c\operatorname{Tr}_d(\xi^*\xi)\). Compute all three traces and the vector-to-operator map.

**Solution.** The standard module is \(M_d\) with that Hilbert norm. Right intertwiners to \(H\) are left multiplication by rectangular matrices \(x\). Coordinate matrix units show \(M=M_m\) and \(R=M_{d+m}\). Directly,

\[
 \begin{gathered}
 \tau_M=c\operatorname{Tr}_m,\\
 \tau_R=c\operatorname{Tr}_{d+m},\\
 t_\xi(b)=\xi b,\\
 \|t_\xi\|=\|\xi\|_{\rm op},\\
 \|U\xi\|_2^2=c\operatorname{Tr}_d(\xi^*\xi).
 \end{gathered}
 \tag{TM.24}
\]

The equality of the rectangular traces follows by summing \(|x_{ij}|^2\) in either order. The operator-norm equality follows from the upper matrix product bound and a matrix \(b\) with one column a maximizing unit vector. No \(c^{1/2}\) enters this bounded-vector map, since the Hilbert norms of its source and target carry the same scale. The column vector space has dimension \(md\); the diagonal \(L^2(M)\) has dimension \(m^2\). At \(d=1,m=2\), they have dimensions \(2\) and \(4\). This directly checks the target in (TM.10), and prevents identifying different linking corners.

**Problem 2.** On \(N=\mathbb C^3\), take the counting trace, let \(\alpha\) cycle the three coordinate idempotents, and let \(\beta\) exchange the first two. Determine the fusion and show that reversing the order changes its bimodule isomorphism class.

**Solution.** On the standard space with coordinate vectors \(\epsilon_i\), the canonical implementers permute the coordinates in the same way as the automorphisms. Formula (TM.14) sends \([u_\alpha,\epsilon_i]\) to \(u_\alpha\epsilon_i\), with right action twisted by \(\alpha\circ\beta\). Thus the answer is \(H_{\alpha\circ\beta}\). Using the cycle \(1\mapsto2\mapsto3\mapsto1\), the products \(\alpha\circ\beta\) and \(\beta\circ\alpha\) are respectively the transpositions \((1\,3)\) and \((2\,3)\). They differ. Every inner automorphism of an abelian algebra is the identity, so (TM.16) proves that the resulting correspondences are not bimodule-isomorphic. Each is full because its left and right diagonal images are mutual commutants. This example tests the order even when inner twists cannot obscure it. \(\square\)

The trace and measurable-operator inputs are TI01, TI11 and TI15, MT08–09, WG008, and DK02–03. The twist proof uses SF05 and SF12, FU02–03, FU08–09 and FU11. TM04 imports the infinite-product construction, finite-part expectations, factoriality, faithful product trace and prefix/tail splitting from OA-APPROX, §2 and §§4–5, at the exact results named there. These are explicit proof providers, with their own antecedents; this lesson does not prove them or their prerequisites.

For free primary research context on traces and matrix amplification, see Jesse Peterson, [*Notes on von Neumann algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf), complete PDF pages 75–77, particularly §4.8.1 and §4.9.1. These selected pages were actually inspected and supply context for the module-trace and amplification application. The infinite-product proof is supplied by the OA-APPROX provider explicitly imported in TM04. The module proofs, matrix-factor specialization and solved tests here are independently written.

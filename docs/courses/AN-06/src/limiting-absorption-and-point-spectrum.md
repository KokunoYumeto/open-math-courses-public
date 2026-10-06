# Limiting absorption and point spectrum

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: What obstructs taking the perturbed resolvent to real energy?** An eigenvector creates a pole, while a regular free shell creates a radiating boundary value. They are different phenomena. The Fredholm factor identifies the finite-dimensional obstruction, and the radiation estimates turn its kernel into rapidly decreasing eigenfunctions. The set of good energies must exclude both the free thresholds and this perturbed point spectrum.

The free resolvent has boundary values at a regular energy. After a symmetric short-range perturbation, the obstruction is a finite-dimensional space of rapidly decreasing eigenfunctions. Away from those exceptional energies, the perturbed resolvent has boundary values on the same endpoint spaces.

Let \(p\) be a real, simply characteristic polynomial on \(\mathbb R^n\), \(n\geq1\), with no invariant direction. Set \(P_0=p(D)\), let \(V=\sum_{|\beta|\leq m}a_\beta(x)D^\beta\), with \(a_\beta\in L^2_{\mathrm{loc}}\), be the symmetric short-range differential perturbation of the preceding lesson, and let \(H\) be the self-adjoint closure on the Schwartz domain established in [Self-adjoint short-range operators](self-adjoint-short-range-operators.md). We use the graph space \(X_p\), local bounds \(M_j\), and distribution-to-norm convergence theorem from [Short-range compactness and local tests](short-range-compactness-and-local-tests.md). Thus \(V:X_p\to B\) is compact and

\[
 \sum_{j\geq0}R_jM_j<\infty,\qquad R_j=2^j.
\tag{1}
\]

Write \(Z=Z(p)\) for the finite set of critical values, \(R_0(z)=(P_0-z)^{-1}\), and \(R_{0,\pm}(\lambda)=R_0(\lambda\pm i0)\). At a real regular energy the two signs are kept separate. Pairings are linear in their first entry.

The [compact alternative in Self-adjoint short-range operators](self-adjoint-short-range-operators.md#short-range-compact-alternative) gives closed range and index zero on the Banach space \(B\). We also use its [extended symmetry](self-adjoint-short-range-operators.md#short-range-endpoint-symmetry) and [nonreal resolvent factorization](self-adjoint-short-range-operators.md#short-range-resolvent-factorization). Proposition 4.1 proves the compact-family argument needed at real energy. The endpoint duality is established in [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md#endpoint-shell-spaces).

For further reading on the compactness and limiting-absorption method, see Kuroda [K], Sections 5.7 and 6.1.

<a id="limiting-absorption-collective"></a>

## 1. Compactness throughout a closed half-plane

**Lemma 1.1.** If \(K\) is a compact subset of either closed half-plane, avoiding \(Z\), the family

\[
 C(z)=VR_0(z):B\longrightarrow B,\qquad z\in K,
\tag{2}
\]

is strongly continuous and collectively compact. Precisely, \(C(z)f\) is norm continuous for every fixed \(f\in B\), and the union of all \(C(z)\) images of the unit ball has compact closure in \(B\).

**Proof.** [Global polynomial resolvent estimates](global-polynomial-resolvent-estimates.md), Theorem 1.1, bounds \(R_0(z):B\to X_p\) uniformly on \(K\). Compactness of \(V\) therefore proves the assertion about the union of images. If \(z_\nu\to z\) on that side, free weak-star continuity gives \(R_0(z_\nu)f\to R_0(z)f\) in distributions, while these inputs are bounded in \(X_p\). Theorem 4.1 of the compactness lesson gives \(VR_0(z_\nu)f\to VR_0(z)f\) in \(B\). Sequential continuity is continuity on the compact metric set \(K\). \(\square\)

At a regular real energy, put

\[
 N_\pm(\lambda)=\ker_B(I+VR_{0,\pm}(\lambda)).
\]

<a id="limiting-absorption-kernels"></a>

**Lemma 1.2.** \(N_+(\lambda)=N_-(\lambda)\). For \(f\) in either kernel,

\[
 u=R_{0,+}(\lambda)f=R_{0,-}(\lambda)f,\qquad
 (p(D)+V-\lambda)u=0.
\tag{3}
\]

**Proof.** Start with \(f+VR_{0,+}f=0\). The wave \(u=R_{0,+}f\) belongs to \(X_p\), solves \((p(D)-\lambda)u=f=-Vu\), and is outgoing. Extended symmetry makes \((u,Vu)\) real, so \((u,f)\) is real. The flux criterion, Corollary 5.2 of [Global radiation and flux](global-radiation-and-flux.md), says that this wave is incoming as well. Hence \(u=R_{0,-}f\), giving \(f+VR_{0,-}f=0\). Interchange the signs to obtain the reverse inclusion. \(\square\)

The same radiation lesson says that a wave which is both incoming and outgoing has zero Fourier trace of its forcing and belongs to \(B^*_0\). These facts permit the weighted estimate used next.

<a id="limiting-absorption-weighted"></a>

## 2. Rapid decay and the closed operator domain

**Lemma 2.1 (weighted local estimate).** Let \(\mu>0\) be differentiable and increasing on \([0,\infty)\), with

\[
 (1+t)\mu'(t)\leq N\mu(t).
\tag{4}
\]

Write

\[
 U_\mu(u)=\sum_\alpha\|\mu(|x|)(\partial^\alpha p)(D)u\|_{B^*}.
\]

Whenever this is finite, for all sufficiently large \(J\),

\[
 \|\mu(|x|)Vu\|_B
 \leq C_N\mu(R_{J+c})\|Vu\|_B
      +C_N U_\mu(u)\sum_{j\geq J}R_jM_j.
\tag{5}
\]

Here the fixed integer \(c\) and the constants depend on the partition used in the local test, on \(p\), and on \(N\), but not on the maximum value of \(\mu\).

**Proof.** The derivative of \(\mu(t)/(1+t)^N\) is nonpositive by (4). The scalar mean-value theorem therefore gives \(\mu(b)/\mu(a)\leq[(1+b)/(1+a)]^N\) for \(0\leq a\leq b\). Together with monotonicity, this bounds the ratio at comparable radii, with a constant depending only on \(N\). Use the lattice partition \(\phi_k\) in the [local criterion of Short-range compactness and local tests](short-range-compactness-and-local-tests.md#short-range-local-criterion). Polynomial Leibniz gives

\[
 p(D)(\phi_k u)=
 \sum_\alpha (D^\alpha\phi_k)(\partial^\alpha p)(D)u/\alpha!.
\]

On pieces whose centres have radius comparable to \(R_j\), the lower bound for \(\mu(|x|)\) on their supports and finite overlap give

\[
 \sum_{k:y_k\in A_j}\|p(D)(\phi_k u)\|_2^2
       \leq C_N R_j\mu(R_j)^{-2}U_\mu(u)^2.
\tag{6}
\]

The local definition of \(M_j\) applies to these graph-space pieces by their compact-support smooth approximation: mollify inside the slightly larger fixed support ball. Each polynomial graph component converges in \(L^2\); the local support and graph inequalities from the same criterion pass the estimate to the limit. Their differential outputs have the same supports. Finite overlap and comparison of adjacent weights therefore bound the late output shell by

\[
 \|\mu Vu\|_{L^2(A_\ell)}
 \leq C_N R_\ell^{1/2}
       (M_{\ell-1}+M_\ell+M_{\ell+1})U_\mu(u).
\]

For all output shells beyond a fixed enlargement of \(R_J\), multiply by \(R_\ell^{1/2}\) and sum. This is the second term in (5), after enlarging the constant. In the remaining ball, \(\mu(|x|)\leq\mu(R_{J+c})\), giving the first term directly from \(\|Vu\|_B\). \(\square\)

<a id="limiting-absorption-rapid"></a>

**Theorem 2.2.** Suppose \(\lambda\notin Z\), \(u\in X_p\), and

\[
 (p(D)+V-\lambda)u=0.
\tag{7}
\]

If \(u\) is both incoming and outgoing, then, for every integer \(L\geq0\) and every \(\alpha\),

\[
 (1+|x|)^L(\partial^\alpha p)(D)u\in L^2.
\tag{8}
\]

Moreover \(u\in\mathcal D(H)\) and \(Hu=\lambda u\). On compact regular energy sets, the norms in (8) are bounded by a constant times \(\|u\|_{X_p}\), uniformly for all such solutions.

**Proof.** Fix an integer \(N\geq1\), and use bounded weights

\[
 \mu_\varepsilon(t)=\left(\frac{1+t}{1+\varepsilon t}\right)^N,
 \qquad 0<\varepsilon<1.
\tag{9}
\]

They increase, and

\[
 (1+t)\frac{\mu_\varepsilon'(t)}{\mu_\varepsilon(t)}
       =\frac{N(1-\varepsilon)}{1+\varepsilon t}\leq N.
\tag{10}
\]

Thus \(U_\varepsilon=U_{\mu_\varepsilon}(u)\) is initially finite. Equation (7) gives \(u=-R_{0,\pm}Vu\); the common boundary value has \(T_\lambda Vu=0\). The [weighted zero-trace theorem in Global polynomial resolvent estimates](global-polynomial-resolvent-estimates.md#global-weighted-division), applied to every polynomial derivative of \(p\), yields

\[
 U_\varepsilon\leq C_N\|\mu_\varepsilon Vu\|_B.
\tag{11}
\]

Each derivative has weakness ratio at most one, because its strength is bounded by \(\widetilde p\). The weight is bounded for each \(\varepsilon>0\), so \(\mu_\varepsilon Vu\in B\); the zero-trace theorem applies before any limiting argument. Its constants depend on \(N\) and the compact regular energy set, and are uniform in \(\varepsilon\). Combine (5) with (11). Choose \(J\), independent of \(\varepsilon\), so that the coefficient of \(U_\varepsilon\) from the tail is at most \(1/2\), using (1). Since \(\mu_\varepsilon(R_{J+c})\leq(1+R_{J+c})^N\), absorption gives

\[
 U_\varepsilon\leq C_{N,J}\|Vu\|_B
       \leq C'_{N,J}\|u\|_{X_p}.
\tag{12}
\]

As \(\varepsilon\downarrow0\), the weights increase to \((1+t)^N\). Fatou on each shell gives the same \(B^*\) bound for every \((1+|x|)^N(\partial^\alpha p)(D)u\). To obtain (8) at exponent \(L\), use this bound at exponent \(N=L+1\). The squared weighted \(L^2\) norm on shell \(A_j\) is then at most \(C R_j^{-1}\); summing these numbers and treating the inner ball proves (8). This also proves the asserted uniformity.

<a id="limiting-absorption-domain"></a>

Here is the domain argument. If all \((\partial^\alpha p)(D)v\) are in \(L^2\), then \(v\in X_p\), and \(h=p(D)v+Vv\in L^2\). For \(\phi\in\mathcal S\), polynomial distributional integration and the extended symmetry of \(V\) give

\[
 (v,P\phi)=(h,\phi),\qquad P=p(D)+V\text{ on }\mathcal S.
\tag{13}
\]

This is the adjoint-domain criterion. Essential self-adjointness gives \(P^*=H\), so \(v\in\mathcal D(H)\) and \(Hv=h\). Apply it to (8), including the nonzero constant derivative that controls \(u\), to finish the proof. \(\square\)

The conclusion is decay of the indicated polynomial graph components. Smoothness of arbitrary order is not asserted for rough coefficients.

<a id="limiting-absorption-discrete"></a>

## 3. Isolated exceptional energies

Define the exceptional set by its endpoint kernel:

\[
 \mathcal A=\{\lambda\in\mathbb R\setminus Z:N_+(\lambda)\ne\{0\}\}.
\tag{14}
\]

**Theorem 3.1.** Each \(N_+(\lambda)\) is finite dimensional. The set \(\mathcal A\) has no accumulation point in \(\mathbb R\setminus Z\).

**Proof.** \(VR_{0,+}(\lambda)\) is compact by Lemma 1.1, so the preceding compact alternative gives a finite kernel. Equivalently, \(R_{0,+}(\lambda)V\) is compact on \(X_p\); the maps \(f\mapsto R_{0,+}f\) and \(u\mapsto -Vu\) identify the two kernels. Injectivity of the first follows by applying \(p(D)-\lambda\); the inverse identities follow from (3).

If distinct \(\lambda_\nu\in\mathcal A\) converged to a regular \(\lambda\), choose corresponding waves with
\(\|u_\nu\|_{X_p}=1\). Lemma 1.2 and Theorem 2.2 give \(Hu_\nu=\lambda_\nu u_\nu\) and uniform bounds (8) for every exponent.

For a compact cutoff \(\chi\), polynomial Leibniz bounds \(\|p(D)(\chi u_\nu)\|_2\) uniformly. Strength properness gives \(\widetilde p(\xi)\to\infty\) at frequency infinity. Proposition 5.1 of the compactness lesson, with \(Q=1\), therefore makes \(\chi u_\nu\) precompact in \(L^2\). Its compactly supported graph inputs are in the local test completion: mollification of \(\chi u_\nu\) converges in its finitely many \(L^2\) graph components, so the compactness assertion extends from smooth tests to these inputs. A countable family of nested cutoffs and a diagonal extraction gives local \(L^2\) convergence. The uniform weighted \(L^2\) bound makes the spatial tails small, giving global convergence \(u_\nu\to u\) along a subsequence.

Then \(Hu_\nu=\lambda_\nu u_\nu\to\lambda u\). Closedness of \(H\) implies \(Hu=\lambda u\). Discard the at most one index with \(\lambda_\nu=\lambda\). Self-adjointness then gives \((u_\nu,u)=0\). Passing to the limit gives \(\|u\|_2^2=0\). Thus the subsequence tends to zero in distributions while staying bounded in \(X_p\). The distribution-to-norm theorem yields \(Vu_\nu\to0\) in \(B\). Uniform free resolvent bounds now give

\[
 1=\|u_\nu\|_{X_p}
   =\|R_{0,+}(\lambda_\nu)Vu_\nu\|_{X_p}\longrightarrow0,
\]

a contradiction. \(\square\)

Consequently \(Z\cup\mathcal A\) is closed and countable. Indeed, for each positive integer \(k\), the compact set \(E_k=\{t:|t|\leq k,\ \operatorname{dist}(t,Z)\geq1/k\}\) contains only finitely many points of \(\mathcal A\); otherwise compactness would give a regular accumulation point. If \(Z\) is empty, use \(E_k=[-k,k]\). These sets exhaust \(\mathbb R\setminus Z\), proving countability; every finite accumulation point lies in the finite closed set \(Z\), proving closedness of the union. Accumulation at a threshold is allowed.

<a id="limiting-absorption-families"></a>

## 4. Inverting a strongly continuous compact family

The following proposition isolates the exact family statement needed at the boundary.

**Proposition 4.1.** Let \(K\) be compact and metrizable, and let \(C(z)\) be a strongly continuous, collectively compact family on a Banach space \(Y\). The set

\[
 K_{\mathrm{bad}}=\{z:I+C(z)\text{ is not invertible}\}
\]

is compact. On its complement the inverses are locally bounded in operator norm and strongly continuous.

**Proof.** Set \(A(z)=I+C(z)\). The collectively compact unit-ball image is bounded, so \(\sup_K\|C(z)\|<\infty\). Fix a good parameter \(z_0\). There are a neighborhood of \(z_0\) and \(c>0\) with \(\|A(z)v\|\geq c\|v\|\) throughout that neighborhood. Otherwise metrizability gives \(z_j\to z_0\) and \(\|v_j\|=1\) with \(A(z_j)v_j\to0\). Collective compactness gives a convergent subsequence of \(C(z_j)v_j\), so \(v_j=A(z_j)v_j-C(z_j)v_j\) converges to a unit vector \(v\). Uniform boundedness and strong continuity give
\[
 \|C(z_j)v_j-C(z_0)v\|
 \leq \sup_K\|C\|\,\|v_j-v\|
       +\|(C(z_j)-C(z_0))v\|\longrightarrow0.
\]
Consequently \(A(z_0)v=0\), contradicting its invertibility. The lower bound makes every nearby \(A(z)\) injective. The compact alternative already proved in the self-adjointness lesson makes it onto as well, with inverse norm at most \(1/c\). Thus the good set is open, its closed complement in \(K\) is compact, and the inverses are locally bounded.

For fixed \(f\in Y\), put \(v_\nu=A(z_\nu)^{-1}f\), where \(z_\nu\to z\) are good parameters. The local inverse bound makes this sequence bounded. Collective compactness and \(v_\nu=f-C(z_\nu)v_\nu\) make it precompact. If a subsequence tends to \(v\), the estimate
\[
 \|C(z_\nu)v_\nu-C(z)v\|
 \leq\sup_K\|C\|\|v_\nu-v\|+\|(C(z_\nu)-C(z))v\|\to0
\]
shows that \(A(z)v=f\). The uniform norm bound for \(C\) follows from its bounded collective unit-ball image. The solution at \(z\) is unique, so every cluster point equals \(A(z)^{-1}f\). Failure of convergence would supply a subsequence separated from that solution, contradicting precompactness. This proves strong continuity. \(\square\)

<a id="limiting-absorption-boundary"></a>

**Theorem 4.2 (limiting absorption).** On either closed half-plane outside \(Z\cup\mathcal A\), for every fixed \(f\in B\),

\[
 T(z)f=(I+VR_0(z))^{-1}f
\tag{15}
\]

is norm continuous in \(B\). The inverses are locally bounded in operator norm. The formula

\[
 R_H(z)f=R_0(z)T(z)f
\tag{16}
\]

extends the Hilbert resolvent to real boundary values \(R_{H,\pm}(\lambda):B\to X_p\), locally uniformly bounded, with weak-star continuous graph components.

**Proof.** Nonreal invertibility is established in the self-adjointness lesson. At real regular energies, (14) and Lemma 1.2 identify exactly the failures of injectivity on both sides. Compactness and index zero identify these with the failures of invertibility. Apply Lemma 1.1 and Proposition 4.1 on compact neighborhoods within either side to get (15) and its bounds.

In (16), the change in \(T(z)f\) is controlled in \(B\), and the free maps are uniformly bounded into \(X_p\). The change in the free map on a fixed forcing is weak-star continuous in each component. More explicitly, for \(z_\nu\to z\) on the chosen side,

\[
 \begin{aligned}
 R_H(z_\nu)f-R_H(z)f
  &=R_0(z_\nu)\bigl(T(z_\nu)f-T(z)f\bigr)\\
  &\quad+\bigl(R_0(z_\nu)-R_0(z)\bigr)T(z)f.
 \end{aligned}
\]

The first term tends to zero in \(X_p\); every graph component of the second tends weak-star to zero. This proves the claimed continuity. In the open half-plane this is the Hilbert resolvent by the previously proved factorization, so the real values are its actual limits. Distributionally,
\((p(D)+V-\lambda)R_{H,\pm}(\lambda)f=f\).
\(\square\)

Away from \(\mathcal A\), (16) is also the unique outgoing or incoming \(X_p\) solution, respectively. Indeed such a solution satisfies
\(u=R_{0,\pm}(f-Vu)\). Its free forcing \(h=f-Vu\) solves
\((I+VR_{0,\pm})h=f\), which has exactly the solution (15).

<a id="limiting-absorption-eigenfunctions"></a>

## 5. Every square-integrable eigenfunction and the range obstruction

**Theorem 5.1.** For \(\lambda\notin Z\), choose a basis \(f_1,\ldots,f_r\) of \(N_+(\lambda)\), allowing \(r=0\). Then

\[
 u_j=R_{0,+}(\lambda)f_j
\tag{17}
\]

is a basis of \(\ker_{L^2}(H-\lambda)\). Each \(u_j\) satisfies (8). For \(g\in B\),

\[
 \exists f\in B:\ (I+VR_{0,+}(\lambda))f=g
 \quad\Longleftrightarrow\quad
 (g,u_j)=0\quad(1\leq j\leq r).
\tag{18}
\]

The same statement holds with the lower boundary. In particular, outside \(Z\) the point spectrum is discrete, has finite multiplicity, and all its eigenfunctions satisfy (8).

**Proof.** Lemma 1.2 and Theorem 2.2 show that the vectors in (17) are rapidly decreasing eigenfunctions. They are independent, since \(f_j=(p(D)-\lambda)u_j\).

To include an arbitrary \(U\in\mathcal D(H)\) with \(HU=\lambda U\), first prove that it annihilates the range in (18). If \(g=(I+VR_{0,+})f\), let \(v=R_{0,+}f\in X_p\). Thus \((p(D)+V-\lambda)v=g\). Choose a real smooth \(\chi\), equal to one near zero and compactly supported, and set \(v_R=\chi(x/R)v\). Every polynomial graph component of \(v_R\) is in \(L^2\), by Leibniz and compact support. The domain argument (13) therefore puts \(v_R\) in \(\mathcal D(H)\). It gives

\[
 (H-\lambda)v_R
  =\chi_Rg+[p(D),\chi_R]v
           +Vv_R-\chi_RVv.
\tag{19}
\]

The commutator is

\[
 [p(D),\chi_R]v
  =\sum_{|\alpha|\geq1}
       R^{-|\alpha|}(D^\alpha\chi)(x/R)
                   (\partial^\alpha p)(D)v/\alpha!.
\tag{20}
\]

Its support lies in an annulus of radius comparable to \(R\). Each graph component has \(L^2\) norm at most \(C R^{1/2}\|v\|_{X_p}\) there, so (20) tends to zero in \(L^2\), at worst like \(R^{-1/2}\). The inputs \(v_R\) are uniformly bounded in \(X_p\) and converge to \(v\) distributionally. Hence \(Vv_R\to Vv\) in \(B\). Also \(\chi_RVv\to Vv\) in \(B\), by the summable shell norm and ordinary dominated convergence on finitely many shells. Finally \(\chi_Rg\to g\) in \(L^2\). Thus the right side of (19) converges to \(g\) in \(L^2\). Pairing against \(U\) gives

\[
 0=((H-\lambda)v_R,U)\longrightarrow(g,U).
\tag{21}
\]

Index zero says that the closed range in \(B\) has codimension \(r\). Its annihilator in \(B^*\) therefore has dimension \(r\): it is the dual of the finite-dimensional quotient by that range. The independent vectors \(u_1,\ldots,u_r\) lie in this annihilator by (21), so they form its basis. Every \(L^2\) eigenfunction \(U\), viewed in \(B^*\), lies there too and is their linear combination. Equality of these functionals is equality of the distributions, since compact smooth functions lie in \(B\). This proves the basis assertion and shows that the range is exactly the simultaneous kernel of their \(r\) pairings, proving (18). The sign exchange follows from Lemma 1.2 and the identical cutoff argument. The final statement follows from Theorem 3.1. \(\square\)

<a id="limiting-absorption-scalar-primitives"></a>

For the example, we need a scalar consequence of the [integrable primitive proof](../providers/analysis/hilbert-valued-integration.md#vector-primitives). If \(w,w'\in L^2_{\mathrm{loc}}(\mathbb R)\), put \(F(x)=\int_0^x w'(t)\,dt\). Local Cauchy–Schwarz makes the integrand locally integrable. That proof gives a locally absolutely continuous \(F\), and scalar Fubini gives its distributional derivative \(w'\). Thus \(h=w-F\) has zero distributional derivative. Every compact smooth test of integral zero is the derivative of its compactly supported smooth primitive. Consequently \(h\) annihilates those tests. Fix a compact smooth test \(\vartheta\) of integral one and subtract \((\int\phi)\vartheta\) from any test \(\phi\); this shows that \(h\) is the constant distribution \(c=\int h\vartheta\). Equality of locally integrable distributions is equality almost everywhere: convolution with the normalized smooth bumps gives zero, and [local mollifier convergence](../providers/analysis/euclidean-approximation-and-convolution.md#mollification) recovers the function. Hence \(w=F+c\) almost everywhere and has the required locally absolutely continuous representative. If \(w'=-a w\) with continuous \(a\), this representative makes the right side continuous; the continuous primitive theorem then makes \(w\) continuously differentiable with that equation everywhere.

<a id="limiting-absorption-example"></a>

**Example 5.2.** In one dimension take

\[
 H=-\frac{d^2}{dx^2}-2\operatorname{sech}^2x,\qquad
 u(x)=\operatorname{sech}x.
\tag{22}
\]

The potential is bounded, symmetric and short range. Since \(u''=u-2u^3\), \(Hu=-u\). The energy \(-1\) is regular for \(p(\xi)=\xi^2\), whose only threshold is zero. The forcing in its endpoint kernel is \(f=-Vu=2u^3\). Thus the obstruction at \(-1\) is already visible in the free resolvent below the free spectrum. To see its multiplicity, write \(A=\partial_x+\tanh x\). Then \(H+1=A^*A\); an eigenfunction at \(-1\) satisfies \(Au=0\), whose solutions are constant multiples of \(\operatorname{sech}x\). Here \(\mathcal D(H)=H^2\), by the bounded-potential domain result, so the integration giving \((A^*Au,u)=\|Au\|_2^2\) is valid. Equation (18) becomes \(\int g(x)\operatorname{sech}x\,dx=0\).

Here are the domain and calculation details. Define \(\cosh x=(e^x+e^{-x})/2\), \(\sinh x=(e^x-e^{-x})/2\), \(\tanh x=\sinh x/\cosh x\), and \(\operatorname{sech}x=1/\cosh x\), using the [exponential and its derivative](../providers/analysis/elementary-functions-and-cutoffs.md#scalar-exponential). Then \(\cosh' =\sinh\), \(\sinh'=\cosh\), \(\cosh^2-\sinh^2=1\), and \(\cosh x\geq e^{|x|}/2\). Quotient differentiation gives \(u'=-u\tanh x\), \(u''=u-2u^3\), and \((\tanh x)'=u^2\). Thus \(u,u',u''\) decrease at least exponentially, giving \(u\in H^2\) and \(2u^3\in B\) by direct summation of the dyadic shell bounds. The same decay makes the potential satisfy the [short-range coefficient criterion](short-range-compactness-and-local-tests.md#short-range-decaying). The polynomial \(p(\xi)=\xi^2\) has \(\widetilde p(\xi)^2=\xi^4+4\xi^2+4\), is simply characteristic, and has no invariant direction. Its only critical value is zero.

The [bounded perturbation theorem](resolvents-domains-and-spectral-density.md#u001-specified-domains) realizes \(H\) on \(H^2\). It agrees with the Schwartz closure: both are self-adjoint extensions of the same restriction, and taking adjoints reverses their inclusion. On \(H^1\), let \(A=\partial_x+\tanh x\). Distributional integration by parts identifies its adjoint as \(A^*=-\partial_x+\tanh x\), also on \(H^1\): membership in the adjoint domain forces the weak derivative to be in \(L^2\), and the converse follows by smooth approximation. Since \(\tanh\) and its derivative are bounded, multiplication by \(\tanh\) preserves \(H^1\). Hence \(U\in H^1\) and \(AU\in H^1\) hold exactly when \(U\in H^2\). This proves \(\mathcal D(A^*A)=H^2\) and the displayed operator factorization on its full domain. Alternatively, the form calculation on compact smooth tests passes to \(H^2\) by the [Sobolev approximation theorem](../providers/analysis/euclidean-approximation-and-convolution.md#integer-sobolev-density).

For an eigenfunction at \(-1\), the norm identity gives \(U'=-\tanh x\,U\). The scalar primitive argument just proved makes \(U\) continuously differentiable; therefore \((\cosh x\,U(x))'=0\) everywhere. The mean-value theorem, applied to the real and imaginary parts, gives \(U=c\operatorname{sech}x\). Finally \(P_0+1\) is the positive Fourier multiplier \(1+\xi^2\), so its inverse on \(L^2\) sends \(f=2u^3=(P_0+1)u\) to \(u\), as claimed.

### Use the conclusion

Follow one kernel vector through the weighted bootstrap before reading the continuity theorem. Distinguish strong continuity on each forcing term from operator-norm continuity, and retain the reduced boundary value at an exceptional energy.

<a id="limiting-absorption-exercises"></a>

## 6. Exercises

**Exercise 6.1 (foundation).** Verify (10), and explain why \(\mu_\varepsilon\) is bounded for each positive \(\varepsilon\) although the limiting weight is unbounded.

**Exercise 6.2 (foundation).** Suppose \(\|(1+|x|)^{L+1}w\|_{B^*}\leq C\). Prove \((1+|x|)^Lw\in L^2\) directly from the dyadic norms, including the inner shell.

**Exercise 6.3 (intermediate).** On \(Y=\ell^2(\mathbb N)\), let \(K=\{0\}\cup\{1/n:n\geq2\}\), \(C(0)=0\), and \(C(1/n)x=x_ne_1\). Prove strong continuity and collective compactness. Compute \((I+C(1/n))^{-1}\), and determine whether the family or its inverses converge in operator norm.

**Exercise 6.4 (intermediate).** Derive the leading \(R^{-1/2}\) estimate in (20). Show how it still permits pairing with any \(L^2\) eigenfunction, without an endpoint graph estimate on that eigenfunction.

**Exercise 6.5 (advanced).** For (22), verify the factorization \(H+1=A^*A\), the one-dimensional eigenspace at \(-1\), and its endpoint forcing \(f=2\operatorname{sech}^3x\). State the exact Fredholm range condition for a complex-valued \(g\in B\).

<a id="limiting-absorption-solutions"></a>

## 7. Complete solutions

**Solution 6.1.** Logarithmic differentiation of (9) gives
\(\mu_\varepsilon'/\mu_\varepsilon=N[(1+t)^{-1}-\varepsilon(1+\varepsilon t)^{-1}]\).
Subtracting the fractions gives \(N(1-\varepsilon)/[(1+t)(1+\varepsilon t)]\), which is nonnegative and gives (10). The ratio in (9) increases from \(1\) to \(1/\varepsilon\), so \(\mu_\varepsilon\leq\varepsilon^{-N}\). At every fixed \(t\), it tends increasingly to \((1+t)^N\). This bounded approximation makes the initial weighted graph norm finite and allows Fatou after the uniform estimate.

**Solution 6.2.** For \(j\geq1\), \(1+|x|\) is comparable to \(R_j\) on \(A_j\). Thus
\[
 \|(1+|x|)^Lw\|_{L^2(A_j)}^2
 \leq C_L R_j^{-2}
       \|(1+|x|)^{L+1}w\|_{L^2(A_j)}^2
 \leq C_L C^2 R_j^{-1}.
\]
The series \(\sum_{j\geq1}2^{-j}\) converges. On \(A_0\), \(1+|x|\) is bounded and at least one, and its weighted \(L^2\) norm is bounded by the \(R_0=1\) component of the given \(B^*\) norm. Adding these estimates proves the result.

**Solution 6.3.** Every fixed \(\ell^2\) vector has \(x_n\to0\), so \(C(1/n)x\to0\). The nonzero parameters are isolated, proving strong continuity on \(K\). The union of unit-ball images is the closed unit disc in the one-dimensional space \(\mathbb Ce_1\), hence compact. For \(n\geq2\), \(C(1/n)^2=0\), since the \(n\)-th coordinate of \(e_1\) is zero. Therefore
\[
 (I+C(1/n))^{-1}=I-C(1/n).
\]
Both \(\|C(1/n)\|\) and \(\|(I+C(1/n))^{-1}-I\|\) equal one, as testing on \(e_n\) shows. Neither converges in operator norm; both converge strongly. This demonstrates the precise continuity guaranteed by Proposition 4.1.

**Solution 6.4.** On the annulus supporting \(D^\alpha\chi(x/R)\), the ball comparison for \(B^*\) gives
\(\|(\partial^\alpha p)(D)v\|_2\leq C R^{1/2}\|v\|_{X_p}\).
The bounded cutoff derivative and its factor \(R^{-|\alpha|}\) therefore give
\[
 \|R^{-|\alpha|}(D^\alpha\chi)(x/R)
             (\partial^\alpha p)(D)v\|_2
       \leq C_\alpha R^{1/2-|\alpha|}\|v\|_{X_p}.
\]
The largest exponent for \(|\alpha|\geq1\) is \(-1/2\). There are finitely many terms, so their sum tends to zero in \(L^2\). Its pairing with \(U\in L^2\) is at most this norm times \(\|U\|_2\), which tends to zero. No graph derivative of \(U\) is needed.

**Solution 6.5.** On smooth compact tests \(A^*=-\partial_x+\tanh x\), and
\[
 A^*A=-\partial_x^2-(\tanh x)'+\tanh^2x
      =-\partial_x^2+1-2\operatorname{sech}^2x=H+1.
\]
The same form identity holds on \(H^2\), by Sobolev approximation or integration by parts with cutoffs. An eigenfunction \(U\) at \(-1\) has \(\|AU\|_2^2=((H+1)U,U)=0\). Hence \(U'=-\tanh x\,U\) in distributions. Since \(U\in H^2\), it has a locally absolutely continuous representative, and integrating this equation gives \(U=c\operatorname{sech}x\). This function lies in \(H^2\) and satisfies the eigen-equation. The forcing is \(f=(P_0+1)u=-Vu=2\operatorname{sech}^3x\), a member of \(B\), and \(R_0(-1)f=u\). The endpoint kernels have dimension one. Since \(u\) is real, their range condition is exactly
\(\int_{\mathbb R}g(x)\operatorname{sech}x\,dx=0\), a complex equality for complex \(g\).

## References


- [K] Shige Toshi Kuroda, *Scattering theory for differential operators, I, operator theory*, Journal of the Mathematical Society of Japan **25** (1973), 75–104, Sections 5.7 and 6.1. [Freely accessible journal PDF](https://www.jstage.jst.go.jp/article/jmath1948/25/1/25_1_75/_pdf/-char/en).
- Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014. [Author's authorized online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).

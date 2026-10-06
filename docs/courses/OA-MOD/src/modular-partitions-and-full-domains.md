# Modular partitions and the full finite domain

**Self-checked by the writing AI.**

A partition at imaginary modular time preserves the energy of every input already finite for the reference weight. For an unbounded weight, this leaves a second question: can the new weight have more finite inputs? We prove the finite-input theorem, construct a counterexample to the unrestricted assertion, and identify the exact domain condition which restores equality on the whole positive cone.

The source assertion is Takesaki, *Theory of Operator Algebras II*, Exercise VIII.3(9), printed page 133 / PDF page 153. Its faithful normal semifinite reference weight and two bounded half-strip elements remain in scope. The assertion as printed is false at this generality. MP-03 gives a counterexample satisfying the exact analytic hypothesis and endpoint partition. MP-04 gives an explicitly corrected equivalence; the false source equivalence is not credited as proved.

The exact inputs are WG's finite left ideals and finite linear extension; HS-01's full closed-operator strip criterion and HS-03's right multiplication on the whole finite left ideal; MF's faithful GNS representation and conjugation; QF-03's closed-form representation; SK's spectral domains; PT-08/CZ-08's faithful normal semifinite trace densities and their modular groups; CZ-07's all-positive bounded centralizer density formula; and VR-07's dense closed restriction of a diagonal form. Their proofs, and the foundations they rest on, are not given here. No new structural import, separability assumption on the general algebra, or countable exhaustion of that algebra is used.

## The endpoint partition determines exactly the finite-input energies

Let \(\varphi\) be faithful normal semifinite on an arbitrary von Neumann algebra \(M\). Write \(\sigma=\sigma^\varphi\), and suppose \(a_1,a_2\in D(\sigma_{-i/2})\), in the bounded closed-strip sense of HS-01. Define

\[
 c_j=\sigma_{-i/2}(a_j),\qquad
 d=c_1^*c_1+c_2^*c_2,\qquad
 \Psi(y)=\varphi(a_1ya_1^*)+\varphi(a_2ya_2^*),\quad y\in M_+.
 \tag{MP.1}
\]

Each summand is a normal weight: a bounded positive sandwich preserves increasing positive suprema, and \(\varphi\) preserves their weight values. Positive additivity and homogeneity hold even at infinity. Thus \(\Psi\) is normal. Its finite left ideal is exactly

\[
 \mathfrak n_\Psi
 =\{x\in M:xa_1^*,xa_2^*\in\mathfrak n_\varphi\}.
 \tag{MP.2}
\]

Indeed its value at \(x^*x\) is the sum of the two nonnegative finite-or-infinite squared GNS norms.

HS-03 supplies, for every \(x\in\mathfrak n_\varphi\), both finite membership and the full right multiplier formula

\[
 \Lambda_\varphi(xa_j^*)=J_\varphi c_jJ_\varphi\Lambda_\varphi(x).
 \tag{MP.3}
\]

Consequently \(\mathfrak n_\varphi\subseteq\mathfrak n_\Psi\), and

\[
 \Psi(x^*x)
 =\langle J_\varphi dJ_\varphi\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle
 \quad(x\in\mathfrak n_\varphi).
 \tag{MP.4}
\]

Here \(J_\varphi dJ_\varphi\) is a bounded positive operator in the commutant. Semifiniteness of \(\varphi\) makes its finite left ideal sigma-weakly dense; the inclusion and WG's criterion make \(\Psi\) semifinite. Faithfulness of \(\Psi\) has not been assumed or inferred.

It follows that

\[
 d=1
 \quad\Longleftrightarrow\quad
 \Psi(y)=\varphi(y)\ \text{for every }y\in M_+\text{ with }\varphi(y)<\infty.
 \tag{MP.5}
\]

For the forward implication apply (MP.4) to \(x=y^{1/2}\). Conversely finite equality at \(x^*x\) makes the bounded self-adjoint operator \(J_\varphi(d-1)J_\varphi\) have zero quadratic form on the dense GNS range. Continuity and polarization make it zero on the whole Hilbert space. Conjugation and the faithful representation give \(d=1\). Polarization also extends the equality in (MP.5) to the complete finite linear domain \(\mathfrak m_\varphi\subseteq\mathfrak m_\Psi\).

For \(C\geq0\) there is also the exact all-positive upper bound

\[
 \Psi\leq C\varphi\quad\Longleftrightarrow\quad d\leq C1.
 \tag{MP.6}
\]

For \(C>0\), finite positives follow from (MP.4), and positives of infinite \(\varphi\)-value have infinite right side. Necessity again uses all finite GNS tests and density. If \(d=0\), each \(c_j=0\); HS-01 and injectivity of the positive modular power force \(a_j=0\), so \(\Psi=0\). This treats \(C=0\) without multiplying an infinite value by zero.

In particular the endpoint partition gives \(\Psi\leq\varphi\) and equality on the whole finite cone. It does not yet prove equality on an input of infinite \(\varphi\)-value. The concrete domain enlargement in MP-03 shows why that last step cannot be supplied by density or normality.

## An explicit closed restriction and its bounded inverse

Use \(H=\ell^2(\mathbb N)\), with inner products linear in the first slot, and the positive self-adjoint diagonal operator

\[
 A\xi=(n^2\xi_n)_n,\qquad
 E=D(A^{1/2})=\{\xi:\sum_{n\geq1}n^2|\xi_n|^2<\infty\},\qquad
 q[\xi]=\sum_{n\geq1}n^2|\xi_n|^2.
 \tag{MP.7}
\]

Put

\[
 S=\sum_{n\geq1}n^{-2},\qquad
 L(\xi)=\sum_{n\geq1}\xi_n\ (\xi\in E),\qquad
 F=\ker L\subset E,\qquad
 v=S^{-1/2}(1/n)_n,\quad w=(1/n^2)_n.
 \tag{MP.8}
\]

The series defining \(S\) is finite and positive; \(1\leq S\leq2\) follows from
\(n^{-2}\leq[n(n-1)]^{-1}\) for \(n\geq2\) and telescoping. Weighted Cauchy–Schwarz gives absolute convergence of \(L\) and \(|L(\xi)|^2\leq S q[\xi]\). Hence \(F\) is closed in the energy norm, while \(q\geq\|\cdot\|^2\) makes that norm equivalent to the usual form norm.

The space \(F\) is dense in \(H\). Given a finite-support vector with coordinate sum \(s\), subtract \(s/m\) in each of \(m\) new coordinates. These finite-support zero-sum vectors have Hilbert error \(|s|/\sqrt m\). Finite-support vectors are themselves dense. Thus the restriction of \(q\) to \(F\) is a densely defined closed positive form. QF-03 supplies a positive self-adjoint \(B\geq1\) with

\[
 D(B^{1/2})=F,\qquad
 \|B^{1/2}\xi\|^2=q[\xi]\quad(\xi\in F).
 \tag{MP.9}
\]

The domain is a proper closed subspace of \(E\) in energy norm, although both \(F\) and \(E\) are dense in \(H\). These are the closed restriction and domain distinction proved in VR-07.

There is an exact bounded inverse formula, so the model does not leave \(B\) unspecified:

\[
 B^{-1}\eta=A^{-1}\eta-\frac{\langle\eta,w\rangle}{S}w
 \quad(\eta\in H).
 \tag{MP.10}
\]

To verify it, denote the right side by \(\zeta\). Both terms belong to \(E\), and
\(L(A^{-1}\eta)=\langle\eta,w\rangle\), \(L(w)=S\), so \(\zeta\in F\). For every \(\chi\in F\), the polarized form satisfies

\[
 q(\zeta,\chi)=\langle\eta,\chi\rangle.
 \tag{MP.11}
\]

Indeed the correction contributes a scalar multiple of \(\sum_n\overline{\chi_n}=0\). The variational domain characterization of the represented operator says exactly \(\zeta\in D(B)\) and \(B\zeta=\eta\). Since \(B\geq1\), this proves (MP.10) on all \(H\). It is a rank-one correction of \(A^{-1}\), with no formal vector \((1,1,\ldots)\) asserted to lie in \(H\).

## An isometric endpoint can accompany a coisometry with a kernel

The map

\[
 U=A^{1/2}B^{-1/2}:H\longrightarrow H,\qquad a=U^*
 \tag{MP.12}
\]

is bounded and isometric. The domain of the displayed product is all \(H\), because \(B^{-1/2}H=F\subset E\), and
\(\|U\eta\|^2=q[B^{-1/2}\eta]=\|\eta\|^2\).
Its range is precisely \(v^\perp\). In fact \(A^{1/2}:E\to H\) is bijective, and

\[
 L(\xi)=\sqrt S\,\langle A^{1/2}\xi,v\rangle\quad(\xi\in E);
\]

its restriction takes \(F\) bijectively onto \(v^\perp\). Therefore

\[
 U^*U=1,\qquad UU^*=1-P_v,\qquad aa^*=1,\qquad a^*a=1-P_v,\qquad av=0.
 \tag{MP.13}
\]

Here \(P_v\eta=\langle\eta,v\rangle v\), with \(\|v\|=1\). The endpoint will be the isometry \(U\); the original operator is the coisometry \(a=U^*\).

For every \(\xi\in E\), the adjoint test in (MP.12) gives the actual bounded-operator identity

\[
 a\xi=B^{-1/2}A^{1/2}\xi.
 \tag{MP.14}
\]

It follows that \(aE\subset F\). In particular for every \(\xi\in F=D(B^{1/2})\),

\[
 a\xi\in D(B^{1/2}),\qquad
 B^{1/2}a\xi=A^{1/2}\xi=UB^{1/2}\xi.
 \tag{MP.15}
\]

Thus this is a full square-root domain identity, not merely an identity on finite coordinate vectors.

On \(M=B(H)\), let \(\tau\) be the canonical faithful normal semifinite trace and let \(\varphi=\tau_B\). PT-08/CZ-08 make \(\varphi\) faithful normal semifinite and identify
\(\sigma_t^\varphi=\operatorname{Ad}(B^{it})\).
Apply HS-01 with its positive operator \(D=B\) and \(s=1/2\) to (MP.15). It proves the bounded closed half-strip continuation of \(a\) and

\[
 a\in D(\sigma_{-i/2}^\varphi),\qquad
 \sigma_{-i/2}^\varphi(a)=U,\qquad
 \sigma_{-i/2}^\varphi(a)^*\sigma_{-i/2}^\varphi(a)=1.
 \tag{MP.16}
\]

Both real and lower edge norms equal one, so the whole strip is contractive.

Choose the source's two operators to be \(a_1=a,\ a_2=0\). Their endpoints obey exactly \(c_1^*c_1+c_2^*c_2=1\). Nevertheless, for the rank-one projections \(P_1\) onto \(e_1\), and \(P_v\),

\[
 \begin{array}{c|cc}
  y&\varphi(y)&\Psi(y)=\varphi(aya^*)\\ \hline
  P_1&+\infty&1\\
  P_v&+\infty&0
 \end{array}
 \tag{MP.17}
\]

For any vector \(\eta\), the trace-density formula is
\(\tau_B(P_\eta)=\|B^{1/2}\eta\|^2\) if \(\eta\in F\), and infinity otherwise; \(P_\eta\) here denotes the rank-one positive \(\langle\cdot,\eta\rangle\eta\), even when \(\eta\) is not normalized. Bounded spectral regularizations of \(B\) prove the formula including infinite energy, as in VR-07. The vector \(e_1\) is in \(E\) but outside \(F\). Formula (MP.14) gives \(ae_1=B^{-1/2}e_1\), whose squared \(B\)-energy is one. The vector \(v\) is outside \(E\), and \(av=0\), proving the other row. Thus the purported all-positive source equality fails.

One may take both operators nonzero: \(a_1=a_2=a/\sqrt2\). Their endpoints are \(U/\sqrt2\), the endpoint partition is unchanged, and their summed weight is still \(\varphi(a\,\cdot\,a^*)\). No condition of distinctness, individual faithfulness, or invertibility is present in the source.

The new finite vector domain and energy are also exact:

\[
 \{\eta:a\eta\in F\}=E+\mathbb Cv,\qquad
 Q_\Psi(\xi+tv)=q[\xi]\quad(\xi\in E,\ t\in\mathbb C).
 \tag{MP.18}
\]

The decomposition is unique because \(v\notin E\). For one inclusion use (MP.14) and \(av=0\). Conversely if \(a\eta\in F\), put
\(\xi=A^{-1/2}B^{1/2}a\eta\in E\).
Then (MP.14) gives \(a\xi=a\eta\), so (MP.13) implies \(\eta-\xi\in\mathbb Cv\); its energy is the asserted norm. This domain is dense, and the form is closed because it is the graph energy of the closed operator \(B^{1/2}a\), on the stated maximal domain. It has null space \(\mathbb Cv\). In contrast the original form has domain \(F\) and zero null space. On every vector in \(F\), both energies equal \(q\), consistently with MP-01.

## The corrected equivalence retains the missing domain condition

At the full generality of MP-01, the exact replacement for the printed equivalence is

\[
 \Psi=\varphi\ \text{on all }M_+
 \quad\Longleftrightarrow\quad
 \begin{cases}
  c_1^*c_1+c_2^*c_2=1,\\
  \{x\in M:xa_1^*,xa_2^*\in\mathfrak n_\varphi\}
       =\mathfrak n_\varphi.
 \end{cases}
 \tag{MP.19}
\]

**Proof.** Whole-weight equality implies the endpoint partition by MP-01 and equality of finite left ideals by their definitions, giving the second clause through (MP.2). Conversely the partition gives equality whenever \(\varphi(y)<\infty\). If instead \(\varphi(y)=\infty\) but \(\Psi(y)<\infty\), then \(y^{1/2}\in\mathfrak n_\Psi=\mathfrak n_\varphi\), a contradiction. Therefore both values are infinite on every remaining positive input. This proves equality on the entire positive cone. \(\square\)

Equivalently the endpoint partition must be accompanied by

\[
 xa_1^*,xa_2^*\in\mathfrak n_\varphi
 \quad\Longrightarrow\quad x\in\mathfrak n_\varphi
 \quad(x\in M).
 \tag{MP.20}
\]

The reverse inclusion already follows from the half-strip hypotheses. In MP-03, \(P_1\) lies in \(\mathfrak n_\Psi\setminus\mathfrak n_\varphi\), so the missing clause is visible as a bounded algebra element, not merely as a Hilbert-space schematic.

Several useful cases satisfy the full condition.

If \(\varphi\) is a bounded faithful normal positive functional, then \(\mathfrak n_\varphi=M\); every positive input is finite, and (MP.5) itself proves the source equivalence in this explicitly narrower case. This does not replace the source's arbitrary semifinite weight by a functional silently.

If one \(a_j\) is invertible and both \(a_j\) and \(a_j^{-1}\) have bounded half-strip continuations, then \(xa_j^*\in\mathfrak n_\varphi\) implies
\(x=(xa_j^*)(a_j^{-1})^*\in\mathfrak n_\varphi\) by HS-03. Thus the partition proves full equality. Analytic continuation of the inverse is an explicit hypothesis, not an inferred property of an arbitrary one-sided analytic multiplier.

If \(a_1,a_2\in M_\varphi\), then \(c_j=a_j\). The all-positive bounded centralizer density formula of CZ-07 gives

\[
 \Psi=\varphi_{a_1^*a_1+a_2^*a_2};
 \tag{MP.21}
\]

hence the partition gives \(\Psi=\varphi_1=\varphi\), including infinite values. The formula uses centralizer cyclicity and positive bounded density evaluation on the whole cone, rather than a claim that an arbitrary positive compression decreases a weight.

The distinction between endpoint isometry, agreement on the finite cone, and equality of entire weights is consistent with the separate criteria recorded in [Zsidó, *On the equality of operator valued weights*, Theorem 3.10(i),(iii)](https://arxiv.org/html/2201.05681v1). That is contextual source correspondence; the counterexample and (MP.19) have the direct proofs above and do not import that theorem as a new premise.

## Exact samples distinguish Hilbert convergence from energy convergence

**Problem 1. Locate the domain defect without an abstract operator product.** Let \(x=P_1\) in MP-03. Show it has finite \(\Psi\)-norm and that \(xa_j^*\) are \(\varphi\)-finite, although \(x\) is not \(\varphi\)-finite.

**Solution.** We have \(\Psi(x^*x)=\Psi(P_1)=1\). Thus \(x\in\mathfrak n_\Psi\), and (MP.2) gives both sandwich domains. For \(a_1=a,a_2=0\) specifically,
\(xa^*=|e_1\rangle\langle ae_1|\), so
\((xa^*)^*(xa^*)=P_{ae_1}\), whose \(\varphi\)-value is one. The original \(x^*x=P_1\) has infinite \(\varphi\)-value. The same total holds for the two nonzero equal operators.

**Problem 2. Truncate the null vector exactly.** Put

\[
 H_N=\sum_{n=1}^N n^{-2},\qquad
 v_N=H_N^{-1/2}\sum_{n=1}^N\frac{e_n}{n}.
 \tag{MP.22}
\]

Compute both rank-one weights, their Hilbert limit, and the missing energy limit.

**Solution.** Each \(v_N\in E\setminus F\), because its coordinate sum is positive. By (MP.18),

\[
 \varphi(P_{v_N})=\infty,\qquad
 \Psi(P_{v_N})=\frac{N}{H_N},\qquad
 v_N\longrightarrow v,\qquad
 \|v_N-v\|^2=2-2\sqrt{H_N/S}.
 \tag{MP.23}
\]

The norm formula follows from the real inner product \(\sqrt{H_N/S}\). Since \(H_N\leq2\), the finite energies are at least \(N/2\), while the limiting vector has \(\Psi\)-energy zero. In particular \(H_4=205/144\) and the fourth sample has \(\Psi\)-energy \(576/205\). The rank-one positives converge in operator norm, using
\(\|P_\xi-P_\eta\|\leq(\|\xi\|+\|\eta\|)\|\xi-\eta\|\).
Normal lower semicontinuity only requires the limiting energy zero to be at most the lower limit infinity. These vectors do not converge in the graph norm of \(B^{1/2}a\).

**Figure specification.** The reproducible figure displays three exact mechanisms. Its domain diagram is schematic in Hilbert space: \(F=\ker L\) is closed only in the \(E\)-energy norm, and every displayed finite domain is Hilbert dense. The arrows \(U:H\to v^\perp\) and \(a=U^*:H\to H\) label the isometry and coisometry, their precise kernels and the analytic endpoint \(-i/2\). The energy panel plots the exact samples \(N/H_N\), shows the values at \(P_1\) and \(P_v\), and marks the null-vector limit separately rather than treating infinity as a finite numerical sample. Proof locators are MP-02–04 and (MP.22)–(MP.23).

The source page has been inspected as mathematical data. Its literal equivalence is refuted by MP-03. The finite-input replacement is proved in MP-01, and the full-domain corrected equivalence is proved in MP-04 at the exact existing course inputs. This resolves the author-side exercise obligation as a source-error correction; it does not close the transitive foundations or award theorem completion for the false printed assertion.

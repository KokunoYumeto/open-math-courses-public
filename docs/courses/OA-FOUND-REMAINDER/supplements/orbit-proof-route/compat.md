<span id="exact-domain-instantiation-for-the-preserved-commutant-proof"></span>
# Exact domain instantiation for the preserved commutant proof

The graph, polar and spectral results in [Closing an involution and recovering its modular data](../../../OA-MOD/OA-MOD-TC.html), [Spectral calculus with its domains retained](../../../OA-MOD/OA-MOD-SK.html) and [Recovering operators from energy forms](../../../OA-MOD/OA-MOD-QF.html) give the domain identities used below.

Let \(\mathcal C\subseteq H\) be an arbitrary left Hilbert algebra with the four HA01 axioms. It need not be unital, full or separable. Its algebraic involution \(s\) is closable by its hypothesis. TC03 and TC05 give \(S=\overline s\), \(F=S^*\), closed dense domains, \(S^{-1}=S\) on its actual range, and the graph core \(\mathcal C\). TC07–10 apply to this \(S\) without a vector-model premise. Thus every equality in MF.3–4 is available from these operator results with its exact domain:

\[
\Delta=FS,\quad S=J\Delta^{1/2},\quad F=J\Delta^{-1/2},\quad
SF=\Delta^{-1},\quad J^2=I,\quad J\Delta^zJ=\Delta^{-\bar z}.
\]

<span id="ordinary-linear-graph-identities-used-by-ha07-and-rd02"></span>
## Ordinary linear graph identities used by HA07 and RD02

TC03 proves the linear graph identity before its conjugate-linear specialization:

\[
G(T)^\perp=\{(-T^*y,y):y\in D(T^*)\}
\]

for any densely defined linear \(T:H\to K\). It proves that closability is equivalent to density of \(D(T^*)\). The ordinary adjoint is closed by its defining pairings: if \(y_n\to y\) and \(T^*y_n\to z\), then \(\langle Tx,y\rangle=\langle x,z\rangle\) for every \(x\in D(T)\). The pairings defining \(T^*\) extend to graph limits, giving \((\overline T)^*=T^*\). Finally, if \(T\) is closable, a pair \((x,z)\) is orthogonal to every \((-T^*y,y)\) precisely when

\[
\langle x,T^*y\rangle=\langle z,y\rangle
\quad(y\in D(T^*)).
\]

After conjugation this is the defining condition for \(x\in D(T^{**})\), \(T^{**}x=z\). Therefore \(G(T^{**})=\overline{G(T)}\). These are consequences of the graph identities just proved. The sequence arguments use the graph's metric, with no assumption on the dimension of \(H\) or \(K\).

QF03 and QF10 Problem 1 consequently apply to each closed dense linear multiplier \(T\) from HA07. They give

\[
D((T^*T)^{1/2})=D(T),\qquad
D(T^*T)=\{x\in D(T):Tx\in D(T^*)\}.
\]

RD02 itself proves the remaining general partial-isometry polar decomposition, including nontrivial kernels. It does not require TC08 to assert a polar theorem for arbitrary linear \(T\). QF04's unitary symmetry and SK08's reduction/transport give the affiliation and zero-complement formulas in RD.7–10.

<span id="common-spectral-cutoffs-retain-both-half-power-graph-norms"></span>
## Common spectral cutoffs retain both half-power graph norms

For positive injective self-adjoint \(A\), put \(P_n=1_{[1/n,n]}(A)\). These bands differ from SK09's written \([e^{-n},e^n]\) only in their scalar endpoints. SK05's norm identity and SK09's vectorwise dominated-convergence proof give, for

\[
V=D(A^{1/2})\cap D(A^{-1/2}),\qquad
\|x\|_V^2=\|x\|^2+\|A^{1/2}x\|^2+\|A^{-1/2}x\|^2,
\]

the exact error identity

\[
\|x-P_nx\|_V^2
=\int_{(0,\infty)\setminus[1/n,n]}(1+\lambda+\lambda^{-1})\,d\mu_x(\lambda)
\longrightarrow0.
\]

Hence the same \(P_nx\) approximates both half powers. A band may have arbitrary Hilbert dimension. This is the common cutoff used by MA07; it is not a countable dense set in the entire Hilbert space, and it does not assert that a spectral band lies in a left Hilbert algebra.

For MF03 use \(A=\Delta\). The actual-domain sum

\[
Q=\Delta^{1/2}+\Delta^{-1/2}\quad\text{on }V
\]

equals the positive spectral operator with scalar function \(\sqrt\lambda+1/\sqrt\lambda\), because its squared function is \(\lambda+\lambda^{-1}+2\). Thus its domain is exactly \(V\), with an equivalent graph norm. There is no cancellation-domain issue. SK05/07 give the bounded operators

\[
Q^{-1},\quad \Delta^{1/2}Q^{-1},\quad \Delta^{-1/2}Q^{-1},
\]

with norms at most \(1/2,1,1\), respectively. For \(\eta\in D(\Delta^{-1/2})\), the same product-domain rules give

\[
Q(1+\Delta)^{-1}\eta=\Delta^{-1/2}\eta.
\]

The resolvent maps this \(\eta\) into \(V\); both integrability conditions follow from the scalar multipliers. MF02 places it in the full left algebra. The MF03 proof then approximates every \(x\in V\) by such resolvent vectors in the same joint norm. Its use of a common algebra test domain in MF04 is therefore justified by MF03 itself and the spectral proofs. No additional joint-core axiom is required from TC or SK.

<span id="exact-limit-of-this-binding"></span>
## Boundary of the domain argument

The graph, spectral and closed-form results above do not assert the algebraic commutant identity. That higher result uses [Building the two multiplication actions of a Hilbert algebra](../../reader/orbit-proof-route/ha.html), [Recovering the commutant from right-bounded vectors](../../reader/orbit-proof-route/rd.html), [Weights and the Hilbert spaces of multiplication](../../reader/orbit-proof-route/wh.html), the analytic arguments in [Analytic kernels for unbounded modular operators](../../reader/orbit-proof-route/ma.html), and [The modular group and its analytic algebra](../../reader/orbit-proof-route/mf.html). The original-weight, relative-operator and crossed-product coefficient-domain arguments require their additional stated hypotheses and proofs.

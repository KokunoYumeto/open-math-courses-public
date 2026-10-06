<span id="the-tensor-domain-formulas-and-their-graph-core"></span>
# The tensor-domain formulas and their graph core

*Written by GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026. CC0.*

The domain and cutoff formulas below specialize Theorem TG01 and displays TG.1–2 in [Tensor products of closed operators and weights](../../reader/orbit-proof-route/tg.html). The antecedent is Takesaki, *Theory of Operator Algebras II*, VIII.4, Lemma 4.1. [Spectral calculus with its domains retained](../../../OA-MOD/OA-MOD-SK.html), Sections SK04–09, supplies the bounded and unbounded spectral calculus used here.

<span id="orbit-tensor-domain--full-positive-tensor-domain-and-its-cutoffs"></span>
## ORBIT-TENSOR-DOMAIN — Full positive tensor domain and its cutoffs

Let \(A_i\geq0\) be positive self-adjoint operators on arbitrary Hilbert spaces \(H_i\). On \(H_1\otimes H_2\), put

\[
R=(1+A_1)^{-1}\otimes I,\qquad Q=I\otimes(1+A_2)^{-1},\qquad Z=R+iQ.
\]

The bounded positive operators \(R,Q\) commute, so \(Z\) is normal. Let \(E\) be its spectral measure on the coordinate square \([0,1]^2\). Coordinate transport in SK08 identifies its real and imaginary coordinate functions with \(R,Q\). The spectral projections of each coordinate equal the lifted spectral projections of the corresponding resolvent: this follows for polynomials, continuous functions by uniform approximation, and bounded Borel functions by vectorwise spectral bounded convergence.

Both lifts are injective. Expanding along any orthonormal basis of the other factor, their kernels consist of vectors all of whose coordinates lie in the zero kernel of the corresponding resolvent. Thus \(E(\{r=0\}\cup\{q=0\})=0\). This argument uses arbitrary bases; each individual vector has at most countably many nonzero coordinates.

On \(r,q>0\) set \(a(r)=r^{-1}-1\), \(b(q)=q^{-1}-1\), and choose arbitrary finite values on the two null axes. For \(\mu_\zeta(B)=\langle E(B)\zeta,\zeta\rangle\), the full domain formula is

\[
\boxed{C=\int a(r)b(q)\,dE(r,q),\qquad
D(C)=\left\{\zeta:\int a(r)^2b(q)^2\,d\mu_\zeta(r,q)<\infty\right\}.}
\tag{TG.1}
\]

SK05 makes \(C\) positive and self-adjoint with exactly this domain. Its scalar function need not be bounded. The rectangular cutoff formula is

\[
\boxed{P_n=1_{[0,n]}(A_1),\qquad Q_n=1_{[0,n]}(A_2),\qquad
E_n=P_n\otimes Q_n
=E(\{a\leq n,\ b\leq n\}).}
\tag{TG.2}
\]

The null axes do not affect the last equality. On \(E_nH\), coordinate inversion is bounded and gives \(C=(A_1P_n)\otimes(A_2Q_n)\), of norm at most \(n^2\). The \(E_n\) increase strongly to \(I\). For \(\zeta\in D(C)\), scalar dominated convergence applied to \(1+a^2b^2\) proves \(E_n\zeta\to\zeta\) and \(CE_n\zeta\to C\zeta\). Finite sums from \(P_nH_1\odot Q_nH_2\) are Hilbert dense in \(E_nH\); the bound \(n^2\) makes their approximations converge in the graph norm too. Therefore \(D(A_1)\odot D(A_2)\) is a graph core for \(C\).

For any \(\xi\in D(A_1)\), \(\eta\in D(A_2)\), truncate both factors by \(P_n,Q_n\). The tensor vectors converge to \(\xi\otimes\eta\) and their images converge to \(A_1\xi\otimes A_2\eta\). Closedness of \(C\) proves its agreement on every such elementary vector. Hence \(C=\overline{A_1\odot A_2}\), exactly the operator used in the remaining TG01–02 proof. Its domain allows cancellation between the two positive factors and is not replaced by an intersection of the separate lifted domains. In particular a zero factor gives the zero operator on the entire tensor Hilbert space.

The corresponding closed tensor square, adjoint and support identities follow by the full TG01–02 proofs at these exact domains. This is a concrete application of the existing domain proof with all Hilbert dimensions retained.

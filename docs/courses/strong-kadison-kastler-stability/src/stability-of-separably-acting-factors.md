# Stability of separably acting factors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson assembles the previous ones into strong Kadison–Kastler stability for all factors on separable Hilbert spaces, of every type, with one modulus (Theorem 1.1). Finite factors were treated in [Stability of finite factors](stability-of-finite-factors.md). For infinite factors the steps are these. Tensor with the fixed factor \(D\) and prepare the pair; align the modular action; conjugate the two tensor products through their common crossed product; and descend twice, first undoing the preparation and then slicing off the auxiliary tensor factor. Each descent produces a completely positive map, which the completely positive criterion turns into a unitary near the identity [OpenAI-289, Section 8].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4 and 1.5); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Proposition 4.1); [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md) (Lemma 1.1); [Stability of finite factors](stability-of-finite-factors.md) (Theorem 2.1); [Preparing infinite factors](preparing-infinite-factors.md) (Lemma 2.1, Proposition 2.2 and Proposition 5.2); [A common modular action](a-common-modular-action.md) (Theorem 3.1); [Common crossed products](common-crossed-products.md) (Proposition 3.2); and [slice maps](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#9-slice-maps) of von Neumann tensor products (Theorem 9.2 of the tensor product lesson).

## 1. The theorem

**Theorem 1.1** (strong stability of separably acting factors). There are \(t_{\rm fac}>0\) and a nondecreasing function \(\eta_{\rm fac}:(0,t_{\rm fac})\to(0,\infty)\) with \(\eta_{\rm fac}(t)\to0\) as \(t\to0\), with the following property. Let \(H\) be a separable Hilbert space and \(M_0,N_0\subseteq B(H)\) unital factors with \(d(M_0,N_0)<t<t_{\rm fac}\). Then there is a unitary \(u\in B(H)\) with
\[
uM_0u^*=N_0,\qquad\|u-1\|\le\eta_{\rm fac}(t).
\]
The threshold and the function do not depend on the factors, their types or their representations.

**Proof.** *The constants.* Let \(c_{\rm mod},C_{\rm mod}\) be the constants of Theorem 3.1 of [A common modular action](a-common-modular-action.md), and \(\gamma_0,\zeta\) those of Proposition 3.2 of [Common crossed products](common-crossed-products.md). For \(t>0\) put \(\gamma(t)=7\cdot10^7t\) and
\[
\begin{aligned}
r(t)&=3\cdot10^7t+C_{\rm mod}\gamma(t)\\
&\quad +\zeta\bigl(2C_{\rm mod}\gamma(t)\bigr).
\end{aligned}
\]
Choose \(t_{\rm fac}\le t_{\rm fin}\) so small that, for \(t<t_{\rm fac}\), \(t<4\cdot10^{-9}\), \(\gamma(t)<c_{\rm mod}\), \(2C_{\rm mod}\gamma(t)<\gamma_0\) and \(2r(t)<10^{-3}\); and put \(\eta_{\rm fac}(t)=\max\{\eta_{\rm fin}(t),64r(t)\}\), which is nondecreasing and tends to \(0\).

*Finite factors.* If \(M_0\) is finite, Theorem 2.1 of the finite lesson gives the unitary. If \(N_0\) is finite, the same theorem applied to the pair \((N_0,M_0)\) gives a unitary \(u'\) with \(u'N_0u'^*=M_0\) and \(\|u'-1\|\le\eta_{\rm fin}(t)\); take \(u=u'^*\). By Lemma 1.1 of [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md), if one of the factors is finite, so is the other. So we may assume that both are infinite.

*Preparation.* Proposition 5.2 of [Preparing infinite factors](preparing-infinite-factors.md) gives unitaries \(u_0\in B(H)\) and \(v\in B(H\otimes K)\) with \(\|u_0-1\|+\|v-1\|\le3\cdot10^7t\), such that
\[
\begin{gathered}
M=M_0\bar\otimes D,\\
N=v\bigl((u_0N_0u_0^*)\bar\otimes D\bigr)v^*
\end{gathered}
\]
form a prepared pair, with \(d_{\rm cb}(M,N)\le6\cdot10^7t<\gamma(t)\).

*Alignment.* Theorem 3.1 of [A common modular action](a-common-modular-action.md) gives a unitary \(q\) with \(\|q-1\|\le C_{\rm mod}\gamma(t)\) such that \(P=qMq^*\) is normalized by the modular group \(U_s=\Delta_N^{is}\) of the vector state on \(N\), and \(d_{\rm cb}(P,N)\le C_{\rm mod}\gamma(t)<2C_{\rm mod}\gamma(t)\). The algebra \(N\) is a type III\(_1\) factor with separable predual, by Proposition 2.2 of the preparation lesson, and \(C(N,U)\) is its continuous core for the vector state; by Lemma 2.1 of that lesson it is a factor of type II\(_\infty\). Nothing is claimed about the action of \(U\) on \(P\) beyond normalization.

*The crossed products.* Proposition 3.2 of [Common crossed products](common-crossed-products.md) gives a unitary \(a\) with \(aPa^*=N\) and \(\|a-1\|\le\zeta(2C_{\rm mod}\gamma(t))\).

*Undoing the preparation.* All these operations took place on \(H\otimes K\). Put
\[
b=(u_0^*\otimes1)\,v^*aq .
\]
Then \(b(M_0\bar\otimes D)b^*\)\(=(u_0^*\otimes1)v^*Nv(u_0\otimes1)=N_0\bar\otimes D\), and by Lemma 1.5 of [Close operator algebras](close-operator-algebras.md), \(\|b-1\|\le r(t)\).

*Slicing off the tensor factor.* Fix a unit vector \(\xi\in K\), let \(\omega_\xi\) be its vector state on \(B(K)\), and put
\[
\begin{gathered}
F_0(x)=(\mathrm{id}\otimes\omega_\xi)\bigl(b(x\otimes1)b^*\bigr)\\
(x\in M_0).
\end{gathered}
\]
With \(V_\xi\eta=\eta\otimes\xi\), the slice map is \(y\mapsto V_\xi^*yV_\xi\), which is UCP, and it maps \(N_0\bar\otimes D\) into \(N_0\) (Theorem 9.2 of the tensor product lesson). So \(F_0\) is a UCP map from \(M_0\) to \(N_0\). Since \(V_\xi^*(x\otimes1)V_\xi=x\), at every matrix level
\[
\begin{aligned}
&\|F_0-\mathrm{id}_{M_0}\|_{\rm cb}\\
&\quad \le\|b(\cdot\otimes1)b^*-(\cdot\otimes1)\|_{\rm cb}\\
&\quad \le2\|b-1\|\le2r(t).
\end{aligned}
\]
The reverse ordinary gap from \(N_0\) to \(M_0\) is less than \(t\), and \(t+2r(t)<1\). Proposition 4.1 of the averaging lesson, with the inclusion of \(M_0\) as \(\rho\), gives a unitary \(u\in B(H)\) with \(uM_0u^*=N_0\) and \(\|u-1\|\le32\cdot2r(t)\le\eta_{\rm fac}(t)\). \(\square\)

## 2. Where the uniformity comes from

Every bound in the proof is a function of \(t\) alone. The finite case contributes the modulus \(\eta_{\rm fin}\), which is uniform because the common-position theorem, the boundary isomorphism and the uniform commutator estimate have absolute constants. The infinite case uses \(\eta_{\rm fin}\) once more, on a corner of a crossed product. Everything else consists of linear estimates with absolute constants: the preparation, the graph comparison, the infinitesimal estimates and the two applications of the completely positive criterion. For a single factor \(M_0\), one could hope for a tolerance \(\delta_{M_0}(\varepsilon)\) that works in every representation; Theorem 1.1 gives one tolerance for all factors at once, which is a stronger quantifier.

## 3. Exercises

**Exercise 3.1.** Show that the slice map \(y\mapsto V_\xi^*yV_\xi\) is UCP and satisfies \(V_\xi^*(x\otimes1)V_\xi=x\).

**Exercise 3.2.** Check that \(b(M_0\bar\otimes D)b^*=N_0\bar\otimes D\) for \(b=(u_0^*\otimes1)v^*aq\).

**Exercise 3.3.** Let \(M_0\) be a factor of type I\(_\infty\), that is \(M_0\cong B(L)\) with \(L\) infinite-dimensional. Which steps of the proof could be replaced by Christensen's theorem alone?

**Exercise 3.4.** Show that the conclusion of Theorem 1.1 implies \(d(M_0',N_0')\le2\eta_{\rm fac}(t)\) for factors with \(d(M_0,N_0)<t<t_{\rm fac}\).

## 4. Solutions

**Solution 3.1.** \(V_\xi\) is an isometry, so \(y\mapsto V_\xi^*yV_\xi\) is completely positive and unital. For \(\eta,\eta'\in H\), \(\langle V_\xi^*(x\otimes1)V_\xi\eta,\eta'\rangle=\langle x\eta,\eta'\rangle\langle\xi,\xi\rangle\).

**Solution 3.2.** \(aqMq^*a^*=aPa^*=N\), so \(v^*aqMq^*a^*v=(u_0N_0u_0^*)\bar\otimes D\), and conjugating by \(u_0^*\otimes1\) gives \(N_0\bar\otimes D\).

**Solution 3.3.** A type I factor is injective, so Christensen's theorem, applied to the mutual near inclusions of \(M_0\) and \(N_0\), already gives a unitary within \(150t\) of \(1\) conjugating \(M_0\) onto \(N_0\), for \(t<1/101\). The general proof is needed for infinite factors that are not injective.

**Solution 3.4.** \(N_0'=uM_0'u^*\), and Lemma 1.5 of [Close operator algebras](close-operator-algebras.md) gives \(d(M_0',uM_0'u^*)\le2\|u-1\|\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026

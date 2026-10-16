# Ultraproduct expectations and semi-lift ambiguity

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

The [multiplier construction](multiplier-ultraproducts-and-normal-embeddings.md) gives a von Neumann algebra \(M^\omega=N_\omega/I_\omega\) with a normal constant copy of \(M\). Taking the ultraweak limit of a representative recovers an element of \(M\). We construct this map, prove its normality directly, and use it to distinguish the information in a convergent automorphism family from the information in its limit.

Throughout Sections 1–2, \(M\) has a faithful normal state \(\varphi\), and \(\omega\) is free. Section 3 assumes separable predual when using \(M_\omega=C_\omega/I_\omega\). Section 4 uses the tracial hyperfinite \(\mathrm{II}_1\) factor \(R\). Inputs are the preceding quotient and normal embedding proofs, ultraweak compactness of bounded balls, and the already proved tensor model for \(R\). We construct the expectation directly from the quotient. The [complete multiplier and faithful quotient-state proofs](multiplier-ultraproducts-and-normal-embeddings.md#theorem-3-2), [normal-functional coefficient and bounded topology proofs](../components/central-sequence-foundations.md#nt2-faithful-state-topology), and order-normal positive-functional theorem NF1–4 supply their exact full prerequisites. The [tracial Hilbert-space arguments](../components/invariant-state-trace-hilbert-inputs.md) and [full dyadic tensor model](../components/strong-stability-matrix-and-product-inputs.md#ss2-whole-variable-matrix-tracial-product) supply the finite tensor example. The general centralizing algebra is constructed below without a factor assumption.

<a id="general-centralizing-algebra-inputs"></a>

## The centralizing algebra at nonfactor scope

The C* algebra and norm estimates in the first paragraphs use only a faithful normal state. The countable metric-completion argument below additionally assumes separable predual, as in Section 3. For the module convention \((x\psi)(a)=\psi(ax)\), \((\psi x)(a)=\psi(xa)\), let \(C_\omega\) be the bounded sequences whose commutators with every fixed \(\psi\in M_*\) tend to zero along \(\omega\). The identity \([ab,\psi]=a[b,\psi]+[a,\psi]b\), the corresponding adjoint identity obtained by conjugating functionals, and \(\|[a,\psi]\|\le2\|a\|\|\psi\|\) show that this is a norm-closed unital C* algebra.

Every bounded strong*-null sequence belongs to \(C_\omega\). For a vector-pair functional, its two module products are bounded by the norm of the fixed vector times the norm of the null operator or its adjoint on the other fixed vector. Every normal functional is a summable vector-pair series; a finite head and the uniform operator bound control its tail. This proves the assertion for all normal functionals, also along an ultrafilter.

For completeness \(C_\omega\subset N_\omega\). If \(\|a_n\|\le C\), \(\|b_n\|\le K\), \(a\) is centralizing and \(b\in I_\omega\), moving \(a_n^*\) past the state and then applying Cauchy–Schwarz gives
\[
 \begin{aligned}
 \varphi(a_n^*b_n^*b_na_n)
 &\le |\varphi(b_n^*b_na_na_n^*)|
        +CK^2\|[a_n^*,\varphi]\|\\
 &\le C^2K\,\varphi(b_n^*b_n)^{1/2}
        +CK^2\|[a_n^*,\varphi]\|\longrightarrow_\omega0.
 \end{aligned}
\]
Indeed \(\varphi((b_n^*b_n)^2)\le K^2\varphi(b_n^*b_n)\) and \(\varphi((a_na_n^*)^2)\le C^4\). The adjoint estimate uses \(b_nb_n^*\) and \([a_n,\varphi]\). The two other product seminorms are directly at most \(C\) times the corresponding seminorm of \(b_n\). Thus both multiplier conditions hold. Hence \(I_\omega\) is a closed two-sided ideal in \(C_\omega\), and \(C_\omega/I_\omega\) embeds isometrically into \(M^\omega\).

The restricted faithful quotient state \(\lambda=\varphi^\omega\) is a trace, since for centralizing representatives
\[
 |\varphi(a_nb_n-b_na_n)|
 \le \sup_n\|b_n\|\,\|[a_n,\varphi]\|\longrightarrow_\omega0.
\]
Its squared trace norm is exactly the ultralimit of the squared symmetric seminorm. This trace depends on the chosen center state in general; no scalar trace invariant under every automorphism of a nonfactor is asserted.

<a id="separable-centralizing-completion"></a>

Here is the full metric-completion step. Now assume separable predual. For a Cauchy sequence of quotient contractions choose a subsequence \(A_r\) with \(\|A_r-A_p\|_{2,\lambda}<2^{-p}\) for \(r>p\). Continuous radial clipping gives centralizing contraction lifts \(a_r(k)\). Choose a norm-dense countable family \(\psi_j\) in \(M_*\), and nested sets \(W_r\in\omega\), each contained in \(\{k:k\ge r\}\), on which
\[
 \begin{aligned}
 \|[a_r(k),\psi_j]\|&<1/r &&(j\le r),\\
 \|a_r(k)-a_p(k)\|_{\varphi,\#}
     &<2^{-p}+2^{-r} &&(p<r).
 \end{aligned}
\]
Each step intersects only finitely many large sets. Put \(r(k)=\max\{r\le k:k\in W_r\}\), or zero when empty, and \(a(k)=a_{r(k)}(k)\), with \(a_0=0\). For every fixed \(r\), the set \(W_r\) forces \(r(k)\ge r\), so \(r(k)\to_\omega\infty\). The commutator tests and the uniform contraction bound imply \(a\in C_\omega\) by norm density. For fixed \(p\), the second line yields \(\|\pi(a)-A_p\|_{2,\lambda}\le2^{-p}\). Thus the subsequence, and then the whole Cauchy sequence, converges in the quotient unit ball.

This metric completeness also handles an arbitrary Cauchy net in that ball: choose successively indices whose tails have diameters below \(2^{-r}\), making the indices increasing by directedness. The selected sequence is Cauchy and has a limit; its tail-diameter bounds force the original net to that same limit. No cofinal sequence of the net is asserted.

Apply bounded strong* density to the C* subalgebra \(C_\omega/I_\omega\) in the faithful normal representation of \(M^\omega\). A bounded approximating net for an element of its von Neumann closure is Cauchy for \(\|\cdot\|_{2,\lambda}\); the complete metric ball gives its limit in the quotient itself. Traciality makes both symmetric state seminorms converge. The bounded faithful-state topology then makes this the strong* limit in \(M^\omega\), so it is the original approximated element. Consequently the subalgebra is strongly closed. Its inclusion is normal because all its vector-pair coefficients, and their summable series, are restrictions of those on \(M^\omega\). The restriction of the faithful normal state is a faithful normal trace. A proper isometry would have positive range defect of zero trace, contradicting faithfulness; hence the algebra is finite. This proves all the needed structural assertions for \(M_\omega\), with arbitrary center.

## 1. The canonical ultraweak-limit map

**Theorem 1.1.** The formula
\[
E_\omega(\pi(x_n))=\operatorname*{uw-lim}_{n\to\omega}x_n
\tag{1}
\]
defines a faithful normal unital completely positive \(M\)-bimodule map \(E_\omega:M^\omega\to M\). It fixes the constant copy of \(M\), and
\[
\varphi\circ E_\omega=\varphi^\omega.
\tag{2}
\]
In particular it is an expectation onto that copy.

**Proof.** A bounded sequence has a unique ultraweak ultralimit, since a bounded closed ball of \(M\) is compact Hausdorff for that topology. A sequence in \(I_\omega\) converges strong* to zero along \(\omega\), hence ultraweakly to zero. Thus (1) is independent of the representative.

It is linear, unital and fixes constants. For \(a,b\in M\), their constant sequences are multipliers, and separate ultraweak continuity of multiplication gives
\[
E_\omega(aXb)=aE_\omega(X)b.
\tag{3}
\]
Complete positivity can be checked at every finite matrix level. A positive element of \(M_k(M^\omega)\) has a positive lift in \(M_k(N_\omega)\): lift its positive square root and multiply the lift by its adjoint. Every coordinate matrix is positive. Its entrywise ultraweak limit is positive because the positive cone of \(M_k(M)\) is ultraweakly closed. These entries are exactly the values of the matrix amplification of (1).

Equation (2) follows from the definition of the quotient state. To prove normality, let \(0\le X_i\uparrow X\) be an arbitrary bounded increasing net in \(M^\omega\), and put \(Y=\sup_i E_\omega(X_i)\) in \(M\). Positivity gives \(Y\le E_\omega(X)\). Normality of the two states and (2) give
\[
\varphi(E_\omega(X)-Y)
=\varphi^\omega(X)-\lim_i\varphi^\omega(X_i)=0.
\tag{4}
\]
The positive difference vanishes by faithfulness of \(\varphi\). Thus \(E_\omega\) preserves increasing positive suprema and is normal. If \(X\ge0\) and \(E_\omega(X)=0\), then \(\varphi^\omega(X)=0\); the faithful quotient state makes \(X=0\). This proves faithfulness as well. To verify full ultraweak continuity, compose \(E_\omega\) with each positive normal functional \(\rho\) of \(M\). Preservation of increasing positive suprema makes \(\rho E_\omega\) order-normal, so the complete theorem NF1–4 places it in \((M^\omega)_*\). Every normal functional is a linear combination of four positive normal functionals. Thus all predual coefficients pull back to actual predual coefficients, which is exactly ultraweak continuity on the whole domain. \(\square\)

The map depends on the ultrafilter but not on the state used to describe the strong*-null ideal. The state identity (2) is a convenient proof of normality, rather than an extra definition of the map. On each fixed norm ball the two faithful normal-state symmetric seminorms describe the same topology. Continuity at zero therefore supplies, for each positive tolerance in one seminorm, a positive tolerance in the other, uniformly over that ball. Applying this implication on an ultrafilter-large set proves equality of their null ideals. The multiplier algebra is the normalizer of that ideal and hence is unchanged. Formula (1) uses only ultraweak ultralimits in the original algebra, so it gives the same expectation after this identification.

## 2. Covariance of a chosen semi-lift

For a fixed normal automorphism \(\beta\), write \(\beta^\omega\) for its constant lift. If \(\beta_n\to\beta\) in the \(u\)-topology, retain the family in
\[
\Gamma_{(\beta_n)}(\pi(x_n))=\pi(\beta_n(x_n)).
\tag{5}
\]
The preceding lesson proves that this is a normal automorphism, and that its restriction to \(M\) is \(\beta\). The coordinate map and its inverse preserve the null ideal, the two-sided multiplier condition and the centralizing commutator tests. Once the induced map is a *-automorphism of the von Neumann quotient, it preserves every bounded increasing positive supremum, because it and its inverse preserve order. NF1–4 applied to each positive normal coefficient then proves its full ultraweak continuity. No state-preservation assumption is needed for this normality argument.

<a id="general-convergent-lift-inputs"></a>

Here is a direct proof of the coordinate-lift assertions at the general faithful-state scope. The coordinate map on bounded sequences is an isometric *-automorphism. If \(b=(b_n)\in I_\omega\) and \(\|b_n\|\le C\), then
\[
 \begin{aligned}
 \varphi(\beta_n(b_n)^*\beta_n(b_n))
 &\le C^2\|\varphi\circ\beta_n-\varphi\circ\beta\|
       +(\varphi\circ\beta)(b_n^*b_n)
       \longrightarrow_\omega0.
 \end{aligned}
\]
The adjoint square has the same bound with \(b_nb_n^*\). The final terms tend to zero because fixed normal positive functionals test the same bounded strong* topology as the faithful state. The inverse family also converges in the \(u\)-topology: composing with \(\beta_n\), an isometry on the predual, gives
\[
 \|\psi\circ\beta_n^{-1}-\psi\circ\beta^{-1}\|
 =\|\psi-(\psi\circ\beta^{-1})\circ\beta_n\|
 \longrightarrow0.
\]
Thus both coordinate maps preserve \(I_\omega\). Its two-sided normalizer \(N_\omega\) is consequently invariant too, by applying the coordinate automorphism to both ideal-preservation equations. This yields a *-automorphism of \(M^\omega\), normal by the order and coefficient argument just given.

For a fixed \(a\in M\), \(u\)-convergence implies \(\beta_n(a)\to\beta(a)\) strong*. To check it directly after reducing the limit to the identity, expand each square of \(\beta_n(a)-a\). The first term is tested by \(\psi\circ\beta_n\) at \(a^*a\). The two cross terms are tested at \(a,a^*\) by the fixed normal functionals \(x\mapsto\psi(a^*x)\) and \(x\mapsto\psi(xa)\). Their limits cancel the two diagonal terms. Repeat for the adjoint square and every positive normal \(\psi\). Hence the quotient restriction to constants is precisely \(\beta\).

For centralizing \((a_n)\), bounded by \(C\), the module identity gives
\[
 \|[\beta_n(a_n),\psi]\|
 \le \|[a_n,\psi\circ\beta]\|
       +2C\|\psi\circ\beta_n-\psi\circ\beta\|
       \longrightarrow_\omega0.
\]
The inverse estimate proves invariance of \(C_\omega\) in both directions. None of these arguments uses separable predual, a factor assumption, or preservation of the chosen state. Under the separable-predual hypothesis of Section 3, the restriction is an automorphism of the finite normally embedded centralizing von Neumann algebra constructed above.

**Proposition 2.1.** Every such chosen family satisfies
\[
E_\omega\Gamma_{(\beta_n)}=\beta E_\omega.
\tag{6}
\]

**Proof.** If \(\|x_n\|\le C\) and \(\psi\in M_*\), then
\[
|\psi(\beta_n(x_n))-\psi(\beta(x_n))|
\le C\|\psi\circ\beta_n-\psi\circ\beta\|\longrightarrow0.
\tag{7}
\]
The ultraweak ultralimit of \(\beta(x_n)\) is \(\beta(E_\omega(X))\), by normality of \(\beta\). Taking scalar ultralimits in (7) proves (6). \(\square\)

Consequently every convergent family with limit \(\beta\) gives the same action on the constant algebra and the same covariance with \(E_\omega\). These two conclusions do not determine its action on varying quotient elements. Nor is \(\varphi^\omega\) automatically preserved: its transformed state is \((\varphi\circ\beta)\circ E_\omega\), which equals \(\varphi^\omega\) when \(\beta\) preserves \(\varphi\).

## 3. A trace with values in the original center

Assume now that \(M\) has separable predual, without imposing a factor hypothesis. The preceding lesson embeds the finite von Neumann algebra \(M_\omega\) normally in \(M^\omega\).

**Theorem 3.1.** The restriction
\[
T_\omega=E_\omega|_{M_\omega}:M_\omega\to Z(M)
\tag{8}
\]
is a faithful normal unital positive trace with values in \(Z(M)\). It fixes the constant copy of \(Z(M)\), is a \(Z(M)\)-bimodule map, and satisfies
\[
T_\omega(XY)=T_\omega(YX),\qquad X,Y\in M_\omega.
\tag{9}
\]
Here the specified value algebra is the center of the original \(M\); no equality with \(Z(M_\omega)\) is asserted.

**Proof.** For \(X=\pi(x_n)\), centralizing means \(\|[x_n,\psi]\|\to_\omega0\) for every \(\psi\in M_*\). For fixed \(a\in M\), this gives
\[
|\psi(x_na-ax_n)|\le\|a\|\|[x_n,\psi]\|\to_\omega0.
\tag{10}
\]
Passing to the ultraweak limit shows that \(E_\omega(X)\) commutes with every \(a\), so belongs to \(Z(M)\). For centralizing representatives \(x_n,y_n\),
\[
|\psi(x_ny_n-y_nx_n)|
\le\sup_n\|y_n\|\|[x_n,\psi]\|\to_\omega0,
\tag{11}
\]
which proves (9) for every normal functional.

The positivity, faithfulness and normality are restrictions of Theorem 1.1. A constant central element is centralizing, since its functional commutators vanish exactly. Equations (1) and (3) therefore give the remaining assertions. \(\square\)

If \(M\) is a factor, the value algebra is \(\mathbb C1\). Thus \(T_\omega(X)=\tau_\omega(X)1\), and the trace on \(M_\omega\) is independent of the particular faithful normal state of \(M\). For a nonfactor, composing (8) with a faithful normal state on \(Z(M)\) gives its corresponding faithful normal scalar trace.

## 4. Two different semi-lifts with the same limit

Use the concrete tracial tensor model
\[
R=\overline{\bigotimes_{n\ge1}(M_2,\operatorname{tr}_2)}^{\,\mathrm{vN}}.
\tag{12}
\]
Let \(z_n\) and \(x_n\) be identity on every tensor leg except leg \(n\), where they equal
\[
z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{13}
\]
They are self-adjoint unitaries, with trace zero and \(zx=-xz\). Each sequence commutes eventually with every finite tensor word. Approximating any \(a\in R\) in trace \(2\)-norm by such words proves
\[
\|[z_n,a]\|_2,\ \|[x_n,a]\|_2\longrightarrow0.
\tag{14}
\]
The finite trace centralizing criterion from the preceding lessons makes these sequences centralizing. Equivalently, finite tensor densities are dense in \(L^1(R,\tau)\), so their commutation proves the required convergence against every normal functional.

The density assertion has a direct whole-predual proof. In the trace representation, every normal functional is a norm-convergent summable vector-pair series. Its finite head can be approximated by vector pairs \(a\Omega,b\Omega\) with \(a,b\) in finite tensor stages; the coefficient error is at most \(\|\xi-a\Omega\|\|\eta\|+\|a\Omega\|\|\eta-b\Omega\|\). These coefficients are \(y\mapsto\tau(b^*ya)=\tau(ab^*y)\), so finite tensor densities are norm dense in \(R_*\). [HF0's full isometric trace pairing](../components/hyperfinite-finite-algebra-and-vacuum-inputs.md#hf0) identifies the completion for \(\|h\|_1=\tau(|h|)\) with that entire predual. Alternatively its inequality \(\|h\|_1\le\|h\|_2\) for bounded \(h\), and finite-stage Hilbert density, show the same density in this completion. Thus eventual commutation with every finite tensor density, followed by the uniform commutator bound, gives centralizing against every normal functional. Adjoint conjugation is an isometry on the predual; the same dense coefficients are eventually fixed by the tail conjugations. This also proves ordinary \(u\)-convergence used in Proposition 4.1.

Put \(Z=\pi(z_n)\), \(X=\pi(x_n)\) in \(R_\omega\). They satisfy
\[
Z^2=X^2=1,\qquad Z^*=Z,\quad X^*=X,\qquad ZX=-XZ.
\tag{15}
\]
Their trace \(2\)-norms are one, so neither is zero.

**Proposition 4.1.** The families \(\beta_n=\operatorname{Ad}(z_n)\) and \(\widetilde\beta_n=\mathrm{id}\) both converge to \(\mathrm{id}\) in the \(u\)-topology, but induce different normal automorphisms of \(R^\omega\), even on \(R_\omega\).

**Proof.** The ordinary centralizing unitary criterion gives \(\operatorname{Ad}(z_n)\to\mathrm{id}\) in the \(u\)-topology. It can also be checked directly on the dense finite tensor normal functionals: they are eventually fixed, and conjugation is an isometry on the predual. The induced automorphisms are
\[
\Gamma_{(\beta_n)}=\operatorname{Ad}(Z),\qquad
\Gamma_{(\widetilde\beta_n)}=\mathrm{id}.
\tag{16}
\]
By (15), the first sends \(X\) to \(-X\), whereas the second fixes \(X\). Their difference on \(X\) has trace \(2\)-norm two. Both restrict to the identity on constant \(R\) and obey \(E_\omega\Gamma=E_\omega\). \(\square\)

A prescribed constant restriction therefore does not determine the automorphism on varying quotient elements. What is proved for each chosen family is a normal automorphism with that constant restriction and the covariance (6). The family cannot be suppressed from the notation merely because it converges.

## 5. Two limits on a fast reindexing theorem

The same example prevents fast reindexing with unrestricted semi-lift equivariance.

**Proposition 5.1.** There are separable von Neumann subalgebras \(P,Q\subset R^\omega\) and a countable group \(G\) of semi-liftable automorphisms preserving \(P\), for which no injective *-homomorphism can satisfy simultaneously
\[
\Phi(P\cap R_\omega)\subset Q'\cap R_\omega,
\qquad \gamma\Phi=\Phi\gamma\quad(\gamma\in G).
\tag{17}
\]

**Proof.** Take \(P=Q=W^*(X,Z)\), and \(G=\{\mathrm{id},\gamma\}\), with \(\gamma=\operatorname{Ad}(Z)\). Relations (15) give \(P\cong M_2\): the projections \((1\pm Z)/2\), and their off-diagonal operators obtained from \(X\), are matrix units. Both projections have trace \(1/2\), so the representation is faithful. In particular \(P\) has separable predual and lies in \(R_\omega\). The group has order two, is semi-liftable by (16), and preserves \(P\).

The first condition of (17) makes \(\Phi(X)\) commute with \(Z\), hence \(\gamma(\Phi(X))=\Phi(X)\). Equivariance and \(\gamma(X)=-X\) instead give \(\gamma(\Phi(X))=-\Phi(X)\). Thus \(\Phi(X)=0\), contradicting injectivity. \(\square\)

There is also a separate obstruction to full scalar trace independence when constants are fixed. Let \(a=x\) be a constant trace-zero self-adjoint unitary in \(M_2\subset R\), and let \(P,Q\) contain it. Then
\[
\tau^\omega(a\Phi(x))=\tau(a^2)=1,
\qquad
\tau^\omega(a)\tau^\omega(x)=0
\tag{18}
\]
for every map fixing that constant. Thus scalar factorization cannot hold for arbitrary \(x\in P,a\in Q\). In a nontracial algebra a scalar trace on all \(M^\omega\) is not part of the construction in the first place.

The [next lesson](fast-reindexing-with-liftable-actions.md) proves the corrected fast result: equivariance for a countable group of constant lifts, and the identity
\[
E_\omega(a\Phi(x))=E_\omega(a)E_\omega(x),
\qquad x\in P,\ a\in Q.
\tag{19}
\]
For a factor and a centralizing \(x\), its right side has the scalar factorization suggested by the source. The domain assignment \(x\in P,a\in Q\) is necessary because \(\Phi\) is defined on \(P\).

## 6. Exercises with complete solutions

**Exercise 1.** Why does a positive matrix in the quotient have a positive matrix lift for the complete positivity argument?

*Solution.* The quotient map \(M_k(N_\omega)\to M_k(M^\omega)\) is surjective. Lift the positive square root of the given matrix to \(B\), and use \(B^*B\). Its image is the original positive matrix. Every coordinate of \(B^*B\) is positive, so taking ultraweak limits proves positivity at that matrix level.

**Exercise 2.** Prove normality of \(E_\omega\) without interchanging an increasing supremum with an ultralimit.

*Solution.* Form the supremum \(Y\) of the increasing images in the already known von Neumann algebra \(M\). Positivity gives \(Y\le E_\omega(X)\). The normal state identity (2) gives zero value on their positive difference, as in (4), and faithfulness makes the difference zero. No interchange of two limits is used.

**Exercise 3.** What changes if \(M\) has a nontrivial center?

*Solution.* The ultraweak limit of a centralizing representative need only be central, rather than scalar. Equations (10)–(11) still prove a normal \(Z(M)\)-valued trace. A scalar trace on \(M_\omega\) is then obtained by composing with a normal state on the original center; different center states can give different scalar traces.

**Exercise 4.** Check the off-diagonal matrix units in the counterexample.

*Solution.* Put \(e=(1+Z)/2\), \(f=(1-Z)/2\), \(v=eXf\). Anticommutation gives \(Xf=eX\) and \(Xe=fX\). Hence \(vv^*=e\), \(v^*v=f\), \(v^2=0\), and \(e+f=1\). Together with \(e,f,v,v^*\), these are a unital \(M_2\) system. Since \(E_\omega(Z)=0\), both diagonal projections have trace \(1/2\).

**Exercise 5.** Compute the size of the ambiguity between the two semi-lifts on \(X\).

*Solution.* One sends \(X\) to \(-X\), and the other sends it to \(X\). The difference is \(-2X\), with squared trace \(2\)-norm \(4\tau_\omega(X^*X)=4\). In particular it is neither zero nor a strong*-null quotient element.

**Exercise 6.** Explain why covariance with \(E_\omega\) does not detect this ambiguity.

*Solution.* The element \(X\) has ultraweak limit zero, so \(E_\omega(X)=E_\omega(-X)=0\). Both families have identity limit and therefore satisfy (6) with that limit. The faithful expectation detects positive elements faithfully, but it is not an injective linear map on all elements.

**Exercise 7.** Identify the incompatible requirements in Proposition 5.1.

*Solution.* Relative commutation with \(Q\), which contains \(Z\), makes the image of \(X\) fixed by \(\operatorname{Ad}(Z)\). Equivariance makes that same image negated because \(X\) is negated in the domain. Over \(\mathbb C\) these equations force zero. This contradiction uses neither a trace-factorization requirement nor failure to fix constants.

**Exercise 8.** Recover the scalar centralizing version of (19) when \(M\) is a factor.

*Solution.* If \(x\in P\cap M_\omega\), Theorem 3.1 gives \(E_\omega(x)=\tau_\omega(x)1\). Equation (19) becomes \(E_\omega(a\Phi(x))=\tau_\omega(x)E_\omega(a)\). Applying any normal state \(\varphi\) gives \(\varphi^\omega(a\Phi(x))=\tau_\omega(x)\varphi^\omega(a)\). If \(a\) is centralizing too, this is the scalar trace factorization on \(M_\omega\). For arbitrary constant \(x\) it need not hold, as (18) shows.

## References

Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.1, printed pp.49–50 (PDF pp.63–64), constructs the canonical normal expectation and its center-valued tracial restriction. Section 5.2, printed pp.50–52 (PDF pp.64–66), constructs actions from convergent automorphism families. The local proofs give the positive matrix lift, faithful-state normality and covariance estimates explicitly. The general expectation and covariance use a faithful normal state; the centralizing algebra's stated separable-predual assumption is retained.

The two Pauli tensor-tail obstructions are proved here directly. A chosen family's limit determines its action on constants, but does not determine its action on varying ultraproduct elements. Ocneanu's fast reindexing lemma in Section 5.3, printed pp.53–54 (PDF pp.67–68), uses constant lifts and an ordered expectation identity, as does the following lesson. No freely accessible source is claimed to prove the false unrestricted semi-lift or scalar-independence assertions.

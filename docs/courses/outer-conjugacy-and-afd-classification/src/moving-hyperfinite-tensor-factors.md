# Moving hyperfinite tensor factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026; revised by GPT-6 Astra (OpenAI), Ultra, October 2026, with writing-AI self-checking. New original text is public domain (CC0).*

## Introduction

Producing a hyperfinite tensor factor inside an algebra does not identify its complementary factor. An outer-conjugacy argument needs to compare the produced factor with a chosen one, while controlling the automorphism that moves it.

We prove that two hyperfinite II₁ tensor factors whose complements are both isomorphic to the original strongly stable factor can be moved onto one another by an approximately inner automorphism. First we match infinitely many finite tensor coordinates. Their matching unitaries need not converge. Their inner automorphisms, and their inverses, do converge. An extra hyperfinite leg then turns each selected infinite subproduct into the entire prescribed factor.

The construction is due to [Connes], Proposition 2.2.3; see also [Takesaki III], Theorem XVII.2.5. We separate convergence on the predual from the coordinate matching and the final tensor expansion. The finite asymptotic centralizer and exact prescribed-support lifts are proved in Central sequence algebras and exact lifts, Theorems 3.1, 5.1 and 6.1. Every automorphism of the hyperfinite II₁ factor \(R\) is approximately inner by [Local approximation and the hyperfinite finite factor](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/hyperfinite-finite-factors.html#theorem-6-3), Theorem 6.3; that lesson also supplies its tracial tensor-product realization. Projection comparison and polar decomposition are developed in [Peterson], Sections 2.5 and 3.1–3.2. The finite quotient comparison needed here is also verified directly in Section 3.

## 1. The statement and why its complement hypothesis matters

For a unital subfactor \(A\subset M\), write \(A^c=A'\cap M\). To say that \(A\) **factorizes** \(M\) means multiplication gives a normal isomorphism
\[
A\overline\otimes A^c\longrightarrow M.
\tag{1.1}
\]
Generation by commuting subalgebras alone is not substituted for this tensor-product hypothesis.

**Theorem 1.1.** Let \(M\) be a strongly stable factor with separable predual. Suppose \(A,B\subset M\) are hyperfinite II₁ subfactors which factorize \(M\), and
\[
A^c\cong M\cong B^c.
\tag{1.2}
\]
There is an approximately inner automorphism \(\gamma\) of \(M\) such that \(\gamma(A)=B\).

Here strongly stable means \(M\cong M\overline\otimes R\). Approximately inner means membership in \(\overline{\operatorname{Inn}M}\) for the \(u\)-topology. The statement does not require \(\gamma\) itself to be conjugation by one unitary.

Condition (1.2) will supply an additional \(R\) inside each complement. In classification arguments it must be established for the extracted factor; it cannot be inferred from \(M\cong R\overline\otimes A^c\) alone.

## 2. Passing to a convergent sequence of automorphisms

We first isolate the convergence step so that the two directions of predual control remain explicit.

**Lemma 2.1 (convergence in both directions).** Suppose \(\alpha_v\in\operatorname{Aut}M\), and a norm-total family \((\psi_j)\subset M_*\) satisfies, for every fixed \(j\),
\[
\begin{gathered}
\sum_v\|\psi_j\circ\alpha_v-\psi_j\circ\alpha_{v-1}\|<\infty,\\
\sum_v\|\psi_j\circ\alpha_v^{-1}-\psi_j\circ\alpha_{v-1}^{-1}\|<\infty.
\end{gathered}
\tag{2.1}
\]
Then \(\alpha_v\) converges in the \(u\)-topology to a normal automorphism \(\alpha\). If every \(\alpha_v\) is inner, \(\alpha\) is approximately inner.

*Proof.* Define isometries on the predual by \(L_v\psi=\psi\circ\alpha_v\) and \(J_v\psi=\psi\circ\alpha_v^{-1}\). Summability gives norm limits on each listed functional. Their common norm bound \(1\) extends convergence to every \(\psi\in M_*\). The limiting maps \(L,J\) are isometries. Since \(L_vJ_v=J_vL_v=1\),
\[
\begin{aligned}
\|L_vJ_v\psi-LJ\psi\|
&\leq\|J_v\psi-J\psi\|\\
&\quad+\|(L_v-L)J\psi\|\to0,
\end{aligned}
\]
and similarly in the other order. Thus \(LJ=JL=1\).

Their adjoints \(L^*,J^*\) are mutually inverse normal unital completely positive maps on \(M\). Indeed each is a pointwise ultraweak limit of automorphisms, and positivity at every matrix level passes to that limit. For completeness, put \(T=L^*\), \(S=J^*\). Schwarz's inequality for these unital completely positive maps gives
\[
x^*x\leq S(T(x)^*T(x))
\leq S(T(x^*x))=x^*x.
\]
Since \(S\) is injective, \(T(x)^*T(x)=T(x^*x)\). Apply this identity to \(x+y\) and \(x+iy\), subtract the individual identities, and obtain \(T(x)^*T(y)=T(x^*y)\). Replacing \(x\) by \(x^*\) proves multiplicativity. Therefore \(L^*\) is a normal automorphism \(\alpha\), with inverse \(J^*\). The convergence of \(L_v\) is precisely \(u\)-convergence of \(\alpha_v\). A limit of inner automorphisms lies in their closure by definition. \(\square\)

## 3. Matching infinitely many coordinates

Choose commuting unital matrix factors \(A_k,B_k\cong M_2(\mathbb C)\) generating \(A,B\), with units \(e_{ij}^{(k)},f_{ij}^{(k)}\). Each of these coordinate sequences is strongly central in \(M\). For instance, a far-out entry in \(A\) commutes with any fixed finite tensor product in \(A\), and the tracial tensor product makes those products dense. Strong centrality in \(A\) extends to \(M=A\overline\otimes A^c\) by first testing product normal functionals and then their norm-dense span. The same argument applies to \(B\).

**Lemma 3.1 (matching subproducts).** There are increasing integers \(k_v\), subfactors
\[
A_0=\bigvee_v A_{k_v}\subset A,\qquad
B_0=\bigvee_v B_{k_v}\subset B,
\tag{3.1}
\]
and an approximately inner \(\alpha\in\operatorname{Aut}M\) with \(\alpha(A_0)=B_0\). Both subfactors in (3.1) are isomorphic to \(R\) and factorize their respective \(A,B\).

*Proof.* Choose a norm-dense sequence \((\psi_j)\) in the unit ball of \(M_*\). We inductively choose unitaries \(u_v\) and products \(V_v=u_v\cdots u_1\), with \(V_0=1\), so that
\[
\begin{aligned}
&u_v\in(B_{k_1}\vee\cdots\vee B_{k_{v-1}})'\cap M,\\
&V_ve_{ij}^{(k_s)}V_v^*=f_{ij}^{(k_s)}\quad(s\leq v),\\
&\|\psi_j\circ\operatorname{Ad}V_v-\psi_j\circ\operatorname{Ad}V_{v-1}\|<2^{-v}\\
&\qquad(j\leq v),\\
&\|\psi_j\circ\operatorname{Ad}V_v^*-\psi_j\circ\operatorname{Ad}V_{v-1}^*\|<2^{-v}\\
&\qquad(j\leq v).
\end{aligned}
\tag{3.2}
\]

At stage \(v\), let \(N=\bigvee_{s<v}B_{k_s}\), a finite matrix factor, and \(P=N'\cap M\). The finite matrix factor gives \(M=N\overline\otimes P\). To see the decomposition explicitly, take matrix units \((d_{ij})\) for \(N\). The map
\[
(y_{ij})\longmapsto\sum_{i,j}d_{i1}y_{ij}d_{1j}
\quad\bigl(y_{ij}\in d_{11}Md_{11}\bigr)
\]
is a normal isomorphism from the matrix algebra over \(d_{11}Md_{11}\) onto \(M\); its inverse sends \(x\) to \((d_{1i}xd_{j1})\). The relative commutant consists of the diagonal copies \(\sum_i d_{i1}yd_{1i}\) of that corner. Thus \(P\) is a factor with separable predual, and product normal functionals span \(M_*\) in norm.

For \(k>k_{v-1}\), both systems
\[
g_{ij,k}=V_{v-1}e_{ij}^{(k)}V_{v-1}^*,\qquad f_{ij}^{(k)}
\]
lie exactly in \(P\): the first commutes with the matched images of all earlier \(A_{k_s}\), and the second commutes with all earlier \(B_{k_s}\). They are strongly central sequences in \(P\). This follows by extending each normal functional of \(P\) to \(M=N\overline\otimes P\) with the matrix trace.

In the finite algebra \(P_\omega\), let \(G_{ij},F_{ij}\) be their classes. Each diagonal of either unital 2-by-2 system has center-valued trace \(1/2\), which gives \(G_{11}\sim F_{11}\). Here is a direct verification of that comparison using the faithful normal scalar trace \(\tau_\omega\) from the quotient theorem, so no factor assertion about \(P_\omega\) is needed.

Put \(Q=P_\omega\), \(e=G_{11}\), \(f=F_{11}\). For every central projection \(z\in Q\), the two equivalent diagonals of each system give
\[
\tau_\omega(ze)=\tfrac12\tau_\omega(z)
=\tau_\omega(zf).
\]
Choose a maximal family of partial isometries in \(Q\) with mutually orthogonal initial projections beneath \(e\) and mutually orthogonal final projections beneath \(f\). Zorn's lemma applies by taking unions of chains. Their finite sums, together with their adjoints, converge strongly to a partial isometry \(W\). Write \(e_0=e-W^*W\) and \(f_0=f-WW^*\). Maximality gives \(f_0Qe_0=0\), since the polar partial isometry of a nonzero element of this space would extend the family. The projection \(z\) onto \(\overline{Qe_0H}\) is central: this subspace reduces both \(Q\) and \(Q'\). It contains \(e_0H\), while \(f_0Qe_0=0\) gives \(zf_0=0\). Traciality and centrality now imply
\[
\begin{aligned}
\tau_\omega(ze_0)
&=\tau_\omega(ze)-\tau_\omega(zW^*W)\\
&=\tau_\omega(zf)-\tau_\omega(zWW^*)\\
&=\tau_\omega(zf_0)=0.
\end{aligned}
\]
Faithfulness gives \(e_0=0\); then \(\tau_\omega(f_0)=\tau_\omega(f)-\tau_\omega(e)=0\), so \(f_0=0\) as well. Consequently \(W^*W=G_{11}\) and \(WW^*=F_{11}\). The prescribed-support lifting theorem gives strongly central partial isometries \(w_k\in P\) with
\[
\begin{gathered}
w_k^*w_k=g_{11,k},\\
w_kw_k^*=f_{11}^{(k)},\\
[(w_k)]=W.
\end{gathered}
\]
The pointwise initial and final projections are equivalent. If \(P\) is finite, the same trace argument just given applies to its two unital matrix systems. If \(P\) is infinite, neither half can be finite: the two halves are equivalent and their sum is \(1\), whereas a finite sum of finite projections is finite. They are therefore infinite projections in a countably decomposable factor and hence equivalent. These finite-sum and infinite-projection facts are the projection inputs also used in the prescribed-support lifting theorem; see [Peterson], Proposition 3.2.7 and Corollary 3.2.10. Only the tail \(k>k_{v-1}\) is used; finitely many earlier coordinates can be filled with any fixed equivalent pair without changing a quotient class.

Set
\[
x_k=\sum_{j=1}^2 f_{j1}^{(k)}w_kg_{1j,k}.
\tag{3.3}
\]
It is unitary and \(x_kg_{ij,k}x_k^*=f_{ij}^{(k)}\). Its class is a unitary in \(P_\omega\), so \((x_k)\) is strongly central along \(\omega\). Its inner automorphisms tend to the identity on the predual of \(P\), and hence on that of \(M\), along \(\omega\). Notice that its class need not be \(1\): the claim is centrality, not strong convergence of \(x_k\) to \(1\).

The forward difference in (3.2) has norm
\[
\|\psi_j\circ\operatorname{Ad}x_k-\psi_j\|.
\]
The inverse difference has norm
\[
\|(\psi_j\circ\operatorname{Ad}V_{v-1}^*)\circ\operatorname{Ad}x_k^*
-\psi_j\circ\operatorname{Ad}V_{v-1}^*\|.
\]
Both tend to zero along \(\omega\); only finitely many functionals are tested at this stage. Choose \(k_v>k_{v-1}\) meeting those bounds and put \(u_v=x_{k_v}\). It commutes with \(N\), preserving every earlier matching identity, and (3.3) gives the new one. This completes the induction.

Lemma 2.1 gives an approximately inner limit \(\alpha=\lim_v\operatorname{Ad}V_v\). Every fixed matching identity persists for all later stages, so its ultraweak limit is \(\alpha(e_{ij}^{(k_s)})=f_{ij}^{(k_s)}\). Thus \(\alpha(A_0)=B_0\). Each chosen infinite subproduct is a tracial infinite product of \(M_2\), hence \(R\); its unused coordinates form its tensor complement inside \(A\) or \(B\). \(\square\)

## 4. Expanding a selected subproduct to the whole factor

*Proof of Theorem 1.1.* Use Lemma 3.1. By (1.2), \(A^c\) is isomorphic to the strongly stable \(M\), so it has a tensor decomposition
\[
A^c=A_1\overline\otimes D,\qquad A_1\cong R.
\]
Inside the hyperfinite II₁ factor \(A\overline\otimes A_1\), write
\[
A\overline\otimes A_1
=A_0\overline\otimes(A_0'\cap A)\overline\otimes A_1.
\tag{4.1}
\]
The first factor is \(R\), and the product of the last two is also \(R\). Indeed, the unused-coordinate algebra is a finite matrix product, an infinite hyperfinite product, or \(\mathbb C\); tensoring any of these with the extra \(R\) gives \(R\). Choose an isomorphism from \(A_0\) onto \(A\) and from the complement in (4.1) onto \(A_1\). Their tensor product is an automorphism \(\rho_A\) of \(A\overline\otimes A_1\) taking \(A_0\) onto \(A\).

Every automorphism of this hyperfinite II₁ factor is approximately inner by the cited prerequisite. Extend \(\rho_A\) by the identity on \(D\). The extension is approximately inner on \(M\): take its approximating inner unitaries in \(A\overline\otimes A_1\), test product functionals on the tensor decomposition with \(D\), and extend convergence by norm density. We use the same name for this extension. Similarly obtain an approximately inner \(\rho_B\) of \(M\) with \(\rho_B(B_0)=B\).

Then
\[
\gamma=\rho_B\circ\alpha\circ\rho_A^{-1}
\]
is approximately inner, since the closure of the inner automorphism group is a subgroup of the topological automorphism group. It maps \(A\) first to \(A_0\), then to \(B_0\), then to \(B\). This proves the theorem. \(\square\)

The additional \(R\) does two jobs. It makes the unused-coordinate complement hyperfinite and infinite even if every original coordinate was selected, and it provides a target complement for the tensor isomorphism expanding \(A_0\) to \(A\).

## 5. Exercises with solutions

**Exercise 5.1 (introductory: selected coordinates).** In \(R=\overline\bigotimes_{k\geq1}M_2\), take \(A_0\) generated by the even coordinates. Identify its commutant inside \(R\) and its tensor factorization.

*Solution.* The unused odd coordinates generate \(A_0'\cap R\). Commutation of the coordinate factors and the tracial product realization give \(R=A_0\overline\otimes(A_0'\cap R)\). Both infinite subproducts are isomorphic to \(R\).

**Exercise 5.2 (intermediate: a central sequence need not approach one).** In the same product, put \(z_k=\operatorname{diag}(1,-1)\) in coordinate \(k\). Show \(\operatorname{Ad}z_k\to\mathrm{id}\), although \(\|z_k-1\|_2\) stays positive.

*Solution.* The sequence commutes eventually with each fixed finite tensor product. Tracial density gives centrality and \(u\)-convergence of its inner automorphisms to the identity. But \(\|z_k-1\|_2^2=(0^2+(-2)^2)/2=2\) at every coordinate. This is exactly the distinction used after (3.3).

**Exercise 5.3 (intermediate: which functional controls the inverse).** Suppose \(V'=xV\). Write the forward and inverse predual differences for \(\operatorname{Ad}V'\) and \(\operatorname{Ad}V\), and identify the transported functional in the inverse difference.

*Solution.* Composition with an automorphism is isometric on the predual. The forward difference has norm \(\|\psi\circ\operatorname{Ad}x-\psi\|\). Since \((V')^*=V^*x^*\), the inverse difference is measured by \(\psi\circ\operatorname{Ad}V^*\), followed by \(\operatorname{Ad}x^*\). Thus its norm is \(\|(\psi\circ\operatorname{Ad}V^*)\circ\operatorname{Ad}x^*-\psi\circ\operatorname{Ad}V^*\|\).

**Exercise 5.4 (advanced: why the extra leg is necessary in the expansion).** If \(A_0=A\), what is \(A_0'\cap A\)? Explain why (4.1) still has two hyperfinite II₁ factors.

*Solution.* Since \(A\) is a factor, \(A'\cap A=\mathbb C1\). The complement of \(A_0\) inside \(A\) alone is therefore scalar. In (4.1), its tensor product with \(A_1\cong R\) is \(\mathbb C\overline\otimes R\cong R\), so the required second hyperfinite factor remains available.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419, Proposition 2.2.3. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003, Theorem XVII.2.5, pp.264–265. [Publisher edition](https://doi.org/10.1007/978-3-662-10453-8).

[Peterson] Jesse Peterson, *Notes on von Neumann algebras*, 2013, Corollary 2.5.8, Lemma 3.1.8, Theorem 3.1.10, Proposition 3.2.7 and Corollary 3.2.10. [Author's notes](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf).

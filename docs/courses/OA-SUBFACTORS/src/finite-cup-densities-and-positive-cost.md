# Finite cup densities and a positive-cost Følner criterion

The ambient inclusion and its core use the same finite basis. They nevertheless have different relative commutants, and their canonical dual densities must be compared on those actual algebras. We compute both densities in finite matrix representations, construct the canonically rescaled expectation of the possibly nonfactor core, and reduce the remaining joint-center discrepancy to a finite-dimensional cup density.

The weighted discrepancy in Lesson 81 is the value of one fixed positive central operator in a finite-projection state. We prove that it can be made arbitrarily small together with all prescribed Følner commutator errors exactly when a central state annihilates that operator. This gives a precise state criterion. General relative amenability alone has not yet been shown to provide an annihilating state.

We use the finite basis and matrix-module proofs of [Lessons 2–3](module-dimension-and-local-index.md); the actual common basis and full corners of [52.1–52.2](canonical-core-traces-and-integer-rounding.md); the finite canonical density and rescaling proof of [63.1–63.3](canonical-rescaling-of-jones-cups.md); the bounds and marginals of [68.1–68.2](core-central-transition-bounds.md); the complete branch identity of [72.2–72.3](finite-central-branches-and-joint-tests.md); and the norm theorem and actual branch means of [81.2–81.6](relative-norm-averaging-and-central-density.md). Normal trace duality, the tracial \(L^1\)–\(L^\infty\) pairing, projection comparison and conditional expectations retain their declared prerequisite scope. We prove the square-root inequality and spectral extraction needed here rather than importing a Følner extraction theorem.

Human-source context for the cup warning is Sorin Popa, [*W*-representations of subfactors and restrictions on the Jones index](https://ems.press/content/serial-article-files/44478), *L'Enseignement Mathématique* 69 (2023), 149–215, DOI 10.4171/LEM/1055, printed p.189: cup-tail inclusions above index four can be locally trivial and nonextremal. That identification is context, not a prerequisite of the calculations below. The original amenability target is Popa, [*Classification of amenable subfactors of type II*](https://doi.org/10.1007/BF02392646), Theorem 4.2.2, printed pp.213–214.

## Compare the actual commutants

Let \(N\subset M\) be II₁ factors of finite index \(d>1\), with actual core \(S\subset R\). Its common cup factors satisfy

\[
\begin{gathered}
K_1\subset S\subset N,\\ K\subset R\subset M,\\
[K:K_1]=[M:N]=d,\\
C=N'\cap M,\quad C_0=S'\cap R,\\
F=K_1'\cap K,\\ D_0=Z(S)\vee Z(R).
\end{gathered}
\tag{82.1}
\]

Use the unit-containing partial orthonormal common basis \(a_i\) of 68.1. Write \(a_i=a_if_i\), \(f_i\in K_1\), and \(g=\sum_i a_i^*a_i\). Thus \(1\leq g\leq b_d1\), \(\tau(g)=d\), \(\sum_i\tau(f_i)=d\), and \(\sum_i a_ia_i^*=d1\). Every finite trace and conditional expectation below is inherited from \(\tau\).

**Lemma 82.1 — commutants and finite matrix trace.** One has \(C\subset C_0\) and \(D_0\subset Z(C_0)\). The three positive operators

\[
\begin{gathered}
k=d^{-1}E_C(g),\\ k_0=d^{-1}E_{C_0}(g),\\
k_F=d^{-1}E_F^K(g).
\end{gathered}
\tag{82.2}
\]

are the central, boundedly invertible densities of the respective normalized dual traces. All lie between \(d^{-1}1\) and \(b_d d^{-1}1\), and have trace one. In particular \(C_0\) need not be finite dimensional.

**Proof.** The initial relative commutant \(C\) belongs to \(R\) and commutes with \(S\subset N\), hence is contained in \(C_0\). Every member of \(C_0\) commutes with \(Z(S)\); it also commutes with \(Z(R)\). Both centers themselves belong to \(C_0\). This proves the stated central containment.

For the core, use the right \(S\)-module coordinate map

\[
\begin{gathered}
V:L^2(R)\longrightarrow\bigoplus_i f_iL^2(S),\\
V\widehat x=\bigl(\widehat{E_S(a_i^*x)}\bigr)_i,\\
V^*(\widehat{\xi_i})_i=\sum_i\widehat{a_i\xi_i}.
\end{gathered}
\tag{82.3}
\]

Orthogonality and the basis expansion show that these are inverse isometries on bounded coordinates, hence inverse unitaries. The commutant of right \(S\) in this representation is \(pM_t(S)p\), \(p=\operatorname{diag}(f_i)\), acting by left matrix multiplication. This follows directly from the standard \(S\)-module commutant on each coordinate; the corner selects the prescribed ranges. Its finite matrix trace is \(\operatorname{Tr}_{\rm mat}(X)=\sum_i\tau(X_{ii})\), of mass \(d\) on \(p\).

For \(c\in C_0\), right multiplication \(R_c:\widehat x\mapsto\widehat{xc}\) commutes with right \(S\). Its matrix is

\[
\begin{gathered}
(VR_cV^*)_{ij}=E_S(a_i^*a_jc),\\
\rho_0(c)\\
=d^{-1}\operatorname{Tr}_{\rm mat}(VR_cV^*)\\
=d^{-1}\tau(gc).
\end{gathered}
\tag{82.4}
\]

Indeed \(\xi_jc=c\xi_j\) permits the coefficient \(\xi_j\) to move to the right of the expectation. The supports put that coefficient in \(f_iSf_j\). Right multiplication reverses products, preserves the adjoint, and is faithful; its restriction therefore pulls the normalized matrix trace back to a faithful normal tracial state on \(C_0\). Adjointness of \(E_{C_0}\) identifies its density as \(k_0\). A density representing a trace commutes with its whole algebra: trace pairings with \(ab\) and \(ba\), followed by faithfulness of the \(L^1\) pairing, prove this. Thus \(k_0\in Z(C_0)\).

The identical matrix argument over \(N\), using the same \(a_i,f_i\), proves \(\rho(c)=d^{-1}\tau(gc)\) on \(C\). Over \(K_1\) it proves the analogous assertion on \(F\). These are exactly the normalized finite dual traces used in 63.1, now also constructed for the nonfactor core. Positivity and the bounds on \(g\) give all bounds and bounded inverses. Trace preservation gives the three normalizations. \(\square\)

**Proposition 82.2 — restriction and transfer.** The ambient dual trace is the restriction of the core dual trace to \(C\). Moreover,

\[
\begin{gathered}
E_C(k_0)=k,\\
T_0(c)=\sum_i a_ica_i^*\in Z(R),\\ c\in C_0,\\
\tau(rT_0(c))=d\,\tau(rk_0c),\\ r\in Z(R).
\end{gathered}
\tag{82.5}
\]

**Proof.** Both scalar dual trace formulas on \(C\) are \(\tau(gc)/d\). The first identity follows by testing every \(c\in C\). For the transfer, expand \(ya_i=\sum_j a_jE_S(a_j^*ya_i)\) for \(y\in R\). Since \(c\) commutes with every coefficient in \(S\), moving it across the coefficients and using the adjoint basis expansion gives \(yT_0(c)=T_0(c)y\), exactly as in 63.12. Thus the transfer is central. Cyclicity, and the fact that \(r\) commutes with the \(a_i\), give \(\tau(rT_0(c))=\tau(rcg)\). Since \(rc\in C_0\), (82.4) gives the last line. \(\square\)

The identity \(E_C(k_0)=k\) does not imply \(k_0=k\). Conditional expectation restricts the trace to a smaller commutant; it need not preserve its density as a physical operator.

## Rescale the nonfactor core with its own density

**Theorem 82.3 — actual canonical core expectation.** The core density satisfies \(E_S(k_0)=1\), and

\[
\begin{gathered}
T_0(k_0^{-1})=d1,\\
F_0(x)=E_S(k_0^{1/2}xk_0^{1/2}),\\ x\in R.
\end{gathered}
\tag{82.6}
\]

is a normal unital completely positive \(S\)-bimodular expectation onto \(S\). It has the finite basis and scalar index bound

\[
\begin{gathered}
b_i=a_ik_0^{-1/2},\\
x=\sum_i b_iF_0(b_i^*x),\\
\sum_i b_ib_i^*=d1,\\
F_0(x)\geq d^{-1}x\quad(x\geq0).
\end{gathered}
\tag{82.7}
\]

Here the last line is a bound. We do not claim a new witness proving its optimality for every nonfactor core.

**Proof.** Since \(k_0\) commutes with \(S\), its \(S\)-expectation is central. The smaller-center marginal in 68.2 gives \(\tau(sg)=d\tau(s)\) for every \(s\in Z(S)\); testing this identity shows \(E_S(k_0)=1\). Alternatively that marginal follows from the common basis supports in the factor \(K_1\), as proved there.

In (82.5) put \(c=k_0^{-1}\). Its central transfer has pairings \(d\tau(r)\) with every \(r\in Z(R)\), so it is \(d1\). Sandwiching and the trace-preserving expectation are normal completely positive maps. Commutation with \(S\) makes their composite \(S\)-bimodular; \(E_S(k_0)=1\) makes it unital and the identity on \(S\).

For reconstruction, the sum in (82.7) is
\(\sum_i a_iE_S(a_i^*xk_0^{1/2})k_0^{-1/2}=x\).
Moving \(k_0^{-1/2}\) across the \(S\)-valued coefficients is legitimate; it is not moved across \(a_i\) or \(x\). The row sum is (82.6).

For completeness put \(y=\sum_i b_iF_0(b_i^*y)\). The row norm bound gives
\(y^*y\leq d\sum_i F_0(y^*b_i)F_0(b_i^*y)\).
Applying \(F_0\) to the adjoint reconstruction identity times \(y\), using bimodularity, identifies the sum as \(F_0(y^*y)\). Taking \(y=x^{1/2}\) proves the positive-operator bound. \(\square\)

The original tracial expectation \(E_S\) and this modified expectation need not agree. In fact

\[
\tau(F_0(x))=\tau(k_0x)\quad(x\in R).
\tag{82.8}
\]

**Corollary 82.4 — exact compatibility of modified expectations.** The ambient canonical expectation of 63.3, restricted to \(R\), is
\(x\mapsto E_S(k^{1/2}xk^{1/2})\).
It equals \(F_0\) on all of \(R\) exactly when \(k_0=k\).

**Proof.** The restriction formula uses \(k\in C\subset R\) and \(E_N|_R=E_S\). Equality follows immediately if the densities agree. Conversely equality of the expectations implies, after applying \(\tau\), that \(\tau((k_0-k)x)=0\) for every \(x\in R\). Take \(x=k_0-k\) to conclude equality. \(\square\)

Compatibility of these modified expectations is consequently stronger than the joint-center equality in 81.15. The tracial commuting square by itself does not identify the two canonical rescalings.

## Reduce to a finite cup density

Write the distinct spectral values and projections of the finite-dimensional density as

\[
\begin{gathered}
h=dk_F=E_F^K(g),\\
h=\sum_{\ell=1}^s\mu_\ell e_\ell,\\
e_\ell\in Z(F),\quad\mu_\ell>0,\\ \sum_\ell e_\ell=1.
\end{gathered}
\tag{82.9}
\]

**Theorem 82.5 — finite cup reduction.** For every von Neumann subalgebra \(Y\subset K_1'\cap M\),

\[
E_Y(g)=E_Y(h).
\tag{82.10}
\]

In particular \(k_0=E_{C_0}(k_F)\), \(k=E_C(k_F)\), and \(E_{D_0}(g)=E_{D_0}(h)\), with the cup density viewed as a physical element of \(K\subset M\).

**Proof.** Apply 81.2 inside the finite-index factor inclusion \(K_1\subset K\). Finite \(K_1\)-unitary averages of \(g\) converge in norm to \(E_F^K(g)=h\). For \(y\in Y\), trace cyclicity and \([y,K_1]=0\) show that every such conjugate has the same trace pairing with \(y\) as \(g\). Equivalently \(E_Y(ugu^*)=E_Y(g)\) for each \(u\in\mathcal U(K_1)\). The expectation is norm contractive; passing to the norm limit proves (82.10). The three particular algebras commute with \(K_1\), so the asserted identities follow. \(\square\)

This theorem does not identify \(F\) with \(C\) or \(C_0\). The latter can contain diffuse \(Z(S)\), whereas \(F\) is finite dimensional.

## The weighted gap is one positive central cost

Use the complete smaller-center branches \(q_j\) and \(a_j,a'_j\) from 81.12. Define

\[
\begin{gathered}
v=E_{D_0}(h-E_C(h))\\
=dE_{D_0}(k_0-k),\\
b=E_{Z(S)}(|v|)\in Z(S)_+,\\
\widehat b\in Z(A),\quad e\widehat b e=be.
\end{gathered}
\tag{82.11}
\]

where \(e=e_R^M\), \(A=\langle N,e\rangle\), \(B=\langle M,e\rangle\) have the canonical trace \(\operatorname{Tr}\) normalized by \(\operatorname{Tr}(e)=1\). The hat is the full-corner central lift of 52.2, not physical left multiplication in \(M\).

**Proposition 82.6 — exact weighted cost.** For every positive \(\zeta\in L^1(Z(S),\tau)\),

\[
\begin{gathered}
\sum_j\|(a_j-a'_j)\zeta\|_1\\
=\tau(\zeta|v|)=\tau(\zeta b),\\
\frac{1}{c}\sum_j\|(a_j-a'_j)\zeta\|_1\\
=\frac{\operatorname{Tr}(p\widehat b)}{c},\\
c=\operatorname{Tr}(p)>0,\\ \zeta=C_A(p).
\end{gathered}
\tag{82.12}
\]

The second identity holds for every finite-trace projection \(p\in B\); \(C_A(p)\) denotes the density of its restriction to \(Z(A)\), as in 70–72. It does not require \(p\in A\).

**Proof.** The complete branch norm identity applied to \(v\) gives
\(\|v\|_1=\sum_j\|E_{Z(S)}(q_jv)\|_1\).
Apply it instead to \(\zeta_n v\), where \(\zeta_n=\min(\zeta,n)\in Z(S)\). Its branch coordinates are \(\zeta_n(a_j-a'_j)\). The bounded central multiplier commutes with \(v\), so its absolute value is \(\zeta_n|v|\). Monotone convergence gives the first identity for \(\zeta\). Adjointness of \(E_{Z(S)}\) gives the second expression \(\tau(\zeta b)\). Finally the definition of the central density \(C_A(p)\), tested on \(\widehat b\), gives \(\operatorname{Tr}(p\widehat b)=\tau(\zeta b)\). \(\square\)

Also \(b=0\) exactly when \(v=0\): take the trace of the positive operator \(|v|\). Thus 81.15 is precisely the assertion that this fixed positive cost vanishes as an operator.

The finite spectral formula is

\[
\begin{gathered}
v=\sum_\ell\mu_\ell w_\ell,\\
w_\ell=E_{D_0}(e_\ell)\\
{}-E_{D_0}(E_C(e_\ell)),\\
\sum_\ell w_\ell=0.
\end{gathered}
\tag{82.13}
\]

It supplies finitely many physical cup projections. It does not assert that either expectation of each individual \(e_\ell\) is scalar.

## A state criterion with one positive test

The next theorem applies to a von Neumann algebra \(\mathcal B\) with a faithful normal semifinite trace \(T\), a unital expected subalgebra \(\mathcal A\subset\mathcal B\), and a unital von Neumann subalgebra \(\mathcal M\subset\mathcal B\). Assume \(T|_{\mathcal A}\) is semifinite and the normal expectation \(E_{\mathcal A}\) preserves \(T\). There is no requirement that \(\mathcal M\subset\mathcal A\), or any finite-index hypothesis. A state \(\varphi\) is \(\mathcal M\)-central if \(\varphi(uxu^*)=\varphi(x)\) for every \(u\in\mathcal U(\mathcal M)\), \(x\in\mathcal B\). It may be singular.

**Theorem 82.7 — positive-cost Følner criterion in the expected algebra.** For a fixed \(a\in\mathcal A_+\), the following are equivalent:

\[
\begin{gathered}
\mathcal M\text{-central state }\varphi,\\
\varphi=\varphi E_{\mathcal A},\quad\varphi(a)=0;\\
\forall\text{ finite }U\subset\mathcal U(\mathcal M),\\ \forall\varepsilon>0,\ \exists\text{ projection }p\in\mathcal A,\\
0<T(p)<\infty,\\
\max_{u\in U}\frac{\|[p,u]\|_{2,T}}{\sqrt{T(p)}}<\varepsilon,\\
\frac{T(pa)}{T(p)}<\varepsilon .
\end{gathered}
\tag{82.14}
\]

There is no assertion that a given arbitrary bounded selfadjoint test can have any prescribed projection-state value.

**Normal density approximation.** Normal states are weak-* dense in all states of \(\mathcal A\). Otherwise real Hahn–Banach separation gives a selfadjoint \(x\in\mathcal A\) whose supremum over all states exceeds its supremum over normal states. The latter already equals the top of the spectrum: a nonzero spectral projection sufficiently near the top has a normal vector state supported on it. This is a contradiction.

Approximate \(\varphi|_{\mathcal A}\) by normal states on \(\mathcal A\), with positive densities \(h_\lambda\in L^1(\mathcal A,T)\), \(T(h_\lambda)=1\), and extend each state through \(E_{\mathcal A}\). Trace adjointness identifies the extension with \(x\mapsto T(h_\lambda x)\) on \(\mathcal B\). The equality \(\varphi=\varphi E_{\mathcal A}\) makes these extensions converge weak-* to \(\varphi\) on the whole of \(\mathcal B\). For \(U=\{u_1,\ldots,u_m\}\), centrality and \(\varphi(a)=0\) imply weak convergence to zero of
\((h_\lambda-u_i h_\lambda u_i^*)_{i=1}^m\), together with the real coordinate \(T(h_\lambda a)\). This is weak convergence in \(L^1(\mathcal B,T)^m\oplus\mathbb R\), whose dual coordinates are bounded operators and scalars. Hahn–Banach separation of a convex set shows that its weak and norm closures agree. Finite convex combinations therefore give, for any \(\delta>0\), a positive \(h\in L^1(\mathcal A,T)\) with

\[
\begin{gathered}
T(h)=1,\\
\sum_i\|h-u_i h u_i^*\|_{1,T}\\
{}+T(ha)<\delta.
\end{gathered}
\tag{82.15}
\]

The cost is nonnegative, which is essential in extracting one projection.

**Square-root estimate.** For positive \(A,B\in L^1(T)\),

\[
\begin{gathered}
\|\sqrt A-\sqrt B\|_{2,T}^2\\
\leq\|A-B\|_{1,T}.
\end{gathered}
\tag{82.16}
\]

Here is a proof retaining noncommutation. Put \(X=\sqrt A-\sqrt B\), \(Y=\sqrt A+\sqrt B\), \(s=\operatorname{sign}(X)\). Products of two \(L^2\) operators are in \(L^1\). Cyclicity and \(sX=Xs=|X|\) give
\(T(s(A-B))=T(|X|Y)\).
Since \(Y-X=2\sqrt B\geq0\), \(T(X_+Y)\geq T(X_+^2)\). Since \(Y+X=2\sqrt A\geq0\), \(T(X_-Y)\geq T(X_-^2)\). The traces of the positive products are nonnegative, justified by sandwiching or \(L^2\) approximation. Adding gives
\(T(s(A-B))\geq T(X^2)\).
The trace duality bound \(|T(s(A-B))|\leq\|A-B\|_1\) proves (82.16).

**Spectral extraction.** Let \(p_t=1_{(t,\infty)}(h)\), \(t>0\), and \(c=T(h)\). Every \(p_t\) has finite trace \(T(p_t)\leq c/t\). Layer cake gives

\[
\begin{gathered}
\int_0^\infty T(p_t)\,dt=c,\\
\int_0^\infty T(p_ta)\,dt=T(ha),\\
\int_0^\infty\|[p_t,u]\|_{2,T}^2\,dt\\
\leq2\sqrt c\,\|\sqrt h-u\sqrt h\,u^*\|_{2,T}\\
\leq2\sqrt{c\|h-uhu^*\|_{1,T}}.
\end{gathered}
\tag{82.17}
\]

To prove the commutator bound first suppose \(h=\sum_i t_iP_i\) is a finite spectral step operator supported on a finite-trace projection. Include \(P_0=1-\sum_iP_i\), \(t_0=0\). Expansion of the squared projection difference and integration gives
\(\sum_{i,j}|t_i-t_j|T(P_i uP_j u^*)\).
The \((0,0)\) term is omitted; every remaining term is finite and nonnegative. Cauchy–Schwarz, using
\(|t_i-t_j|=|\sqrt{t_i}-\sqrt{t_j}|(\sqrt{t_i}+\sqrt{t_j})\), bounds this sum by
\(\|\sqrt h-u\sqrt h u^*\|_2\|\sqrt h+u\sqrt h u^*\|_2\).
The second factor is at most \(2\sqrt c\). This proves the first bound; (82.16) proves the second.

For a general positive \(h\in L^1\), approximate it by nonnegative finite spectral step functions \(h_n=f_n(h)\), supported where \(h\) is bounded away from zero, with \(\|h_n-h\|_1\to0\). Because \(h_n,h\) commute, the integrated squared \(L^2\) distance of their spectral projections is exactly \(\|h_n-h\|_1\). A subsequence thus converges in \(L^2\) for almost every threshold, as do its unitary conjugates. Fatou's lemma, (82.16), and convergence of \(T(h_n)\) pass the bound to \(h\). Monotone spectral integration, or positive trace duality after truncation, gives the two layer-cake identities. This proves every assertion of (82.17).

Apply it to the normalized \(h\) from (82.15). Its spectral projections lie in \(\mathcal A\). The total integrated sum of the squared commutator errors and positive cost is at most
\(2\sum_i\sqrt{\|h-u_i h u_i^*\|_1}+T(ha)\leq2\sqrt{m\delta}+\delta\).
Choose \(\delta\) so small that this is below \(\min(\varepsilon^2,\varepsilon)\). Since \(\int T(p_t)\,dt=1\), some threshold with positive trace has

\[
\begin{gathered}
\sum_i\frac{\|[p_t,u_i]\|_2^2}{T(p_t)}\\
{}+\frac{T(p_ta)}{T(p_t)}\\
<\min(\varepsilon^2,\varepsilon).
\end{gathered}
\tag{82.18}
\]

Otherwise integration would contradict the strict bound. Each term is nonnegative; thus this one projection satisfies (82.14). The argument also applies with \(m=0\).

**Converse.** Direct the projections in (82.14) by finite unitary sets and tolerances tending to zero. The states \(\sigma_p(x)=T(px)/T(p)\) satisfy \(\sigma_p=\sigma_p E_{\mathcal A}\), by trace adjointness and \(p\in\mathcal A\). They have a weak-* cluster state. For \(c=T(p)\),

\[
\begin{gathered}
|\sigma_p(uxu^*)-\sigma_p(x)|\\
\leq\sqrt2\,\|x\|\frac{\|[p,u]\|_2}{\sqrt c}.
\end{gathered}
\tag{82.19}
\]

Indeed \(u^*pu-p\) is supported on the join of two projections of trace \(c\), whose trace is at most \(2c\). Trace-class Cauchy–Schwarz bounds its \(L^1\) norm by \(\sqrt{2c}\) times its \(L^2\) norm, which equals \(\|[p,u]\|_2\). The cluster state is central, remains \(E_{\mathcal A}\)-invariant, and has value zero on \(a\). This proves the converse and the theorem. \(\square\)

## Apply the criterion without assuming normal density matching

**Corollary 82.8 — exact remaining state alternative.** Apply 82.7 to the actual expected algebra \(A\subset B\), the ambient \(M\subset B\), and \(a=\widehat b\) from (82.11). Arbitrarily accurate finite-projection Følner tests with \(p\in A\) and weighted gap tending to zero exist exactly when \(B\) has an \(M\)-central, \(E_A\)-invariant state annihilating \(\widehat b\).

If a compatible hypertrace expectation \(\Phi:B\to M\) is available and \(\tau\Phi(\widehat b)=0\), its state supplies this criterion. Since \(\widehat b\in Z(A)\), compatibility gives \(\Phi(\widehat b)\in N\), and \(N\)-bimodularity puts it in \(Z(N)=\mathbb C1\). Thus this extra condition is exactly \(\Phi(\widehat b)=0\).

**Proof.** Proposition 82.6 identifies the positive cost with the normalized weighted gap. The theorem therefore gives the equivalence. The state \(\tau\Phi\) is \(M\)-central by bimodularity and traciality. Compatibility and trace preservation also give \(\tau\Phi E_A=\tau E_N\Phi=\tau\Phi\). For the final assertion use \(E_N\Phi=\Phi E_A\) on \(\widehat b\), then commute with all \(n\in N\). \(\square\)

Choose the common norm average of 81.6 first and include its finitely many \(N\)-unitaries among the \(M\)-tests. Include all finitely many unitary components of the basis and other prescribed tests. If the annihilating state is supplied, (81.18) then has a controlled final term. This conclusion does not by itself give near-one cyclic integer rounding, a common-support basis, exact full partition or an unrestricted generating tunnel. The source hypotheses must still justify the remaining steps.

The normal identity \(v=0\) makes the cost vanish for every projection. An annihilating singular state is a weaker sufficient route: it only supplies selected projection states with small cost. We have proved the alternative criterion, not that general relative amenability forces either route.

## A locally trivial density calculation

Suppose a II₁ factor \(Q\) has a projection \(f\) of trace \(0<t<1\), \(t\ne1/2\), and a normal isomorphism \(\theta:fQf\to(1-f)Q(1-f)\). The diagonal inclusion \(P=\{x+\theta(x):x\in fQf\}\subset Q\) is locally trivial. Its relative commutant is \(\mathbb Cf+\mathbb C(1-f)\). The diagonal commutant scalars follow because both corners are factors. A nonzero off-diagonal intertwiner, by its polar decomposition, would have initial and final supports \(1-f\) and \(f\): its support projections commute with the two full corner factors. These supports would be equivalent in \(Q\), contradicting their unequal traces.

Both local corner indices are one. Splitting \(L^2(Q)\) by the two commuting left projections and applying the corner module-dimension calculation of Lesson 2 gives finite left \(P\)-dimensions \(1/t\) and \(1/(1-t)\). Thus the inclusion has finite index, equal to their sum. The finite relative-commutant module trace calculation of 63.1 then gives

\[
\begin{gathered}
d=\frac1t+\frac1{1-t}\\
=\frac1{t(1-t)},\\
k_{P,Q}=\frac{1-t}{t}f\\
{}+\frac{t}{1-t}(1-f).
\end{gathered}
\tag{82.20}
\]

For clarity, each corner's dual mass is its local index divided by the product of \(d\) and its physical trace; summing the two masses to one verifies the displayed \(d\), and dividing each mass by the physical trace gives the density. The two normalized traces agree only at \(t=1/2\); the case \(t\ne1/2\) has index strictly above four. This is an actual conditional construction when the stipulated corner isomorphism exists. It is not a claim that these specific physical operators are cup factors of a separately specified tunnel.

![Actual cup-density restriction and extraction of a finite projection with small positive cost](figures/finite-cup-densities-and-positive-cost.svg)

Figure 82.1. The first two panels distinguish the finite cup density, the two actual commutant densities, and the central lift of the positive cost. The third shows the exact integrated estimates of (82.17) and the selection in (82.18). Rectangles are schematic and do not encode dimensions or trace sizes. The final panel records the precise state alternative and the outstanding amenability implication. Original editable source: [finite-cup-densities-and-positive-cost.py](figures/finite-cup-densities-and-positive-cost.py). Human-source context: Popa 2023, printed p.189, and Popa 1994, Theorem 4.2.2.

## Exercises with complete solutions

### Exercise 82.1 — introductory

Why can \(k_0\) be central in \(C_0\) even though \(g\) need not commute with \(S\)? Why does \(E_C(k_0)=k\) not assert equality of the two densities?

**Solution.** Right multiplication by \(c\in C_0\), represented in the finite \(S\)-module matrix corner, pulls back its normalized trace to \(\rho_0(c)=\tau(gc)/d\). Adjointness replaces \(g/d\) by \(E_{C_0}(g)/d=k_0\) in every such pairing. Traciality then implies \(\tau((k_0c-ck_0)y)=0\) for all \(y\in C_0\), hence \(k_0c=ck_0\). This uses the trace, not commutation of the original \(g\). Restricting that trace to \(C\) replaces its density by conditional expectation \(E_C(k_0)\). A projection onto a smaller algebra can remove a nonzero orthogonal component; the restriction identity only identifies that projection.

### Exercise 82.2 — introductory

Compute the index, dual density and unnormalized density in (82.20) at \(t=1/3\). Check both trace normalizations.

**Solution.** The index is \(d=3+3/2=9/2\). The density is \(k_{P,Q}=2f+\frac12(1-f)\), so \(\tau(k_{P,Q})=2/3+(1/2)(2/3)=1\). Its unnormalized version is \(dk_{P,Q}=9f+\frac94(1-f)\), whose trace is \(3+(9/4)(2/3)=9/2\). The dual mass on \(f\) is \(2/3\), whereas its physical mass is \(1/3\). Thus the traces differ. No ambient core, or general amenable counterexample, has been specified by this numerical example.

### Exercise 82.3 — intermediate

Suppose the finite cup density \(h\) has just two spectral values \(\alpha,\beta\), with projection \(f\) for \(\alpha\). Reduce the formula for \(v\) to one projection discrepancy. State two sufficient conditions for vanishing of the cost.

**Solution.** Write \(h=\beta1+(\alpha-\beta)f\). Both expectations are unital, so the scalar term cancels and
\(v=(\alpha-\beta)(E_{D_0}(f)-E_{D_0}(E_C(f)))\).
Consequently \(b=|\alpha-\beta|E_{Z(S)}(|E_{D_0}(f)-E_{D_0}(E_C(f))|)\). If the cup density is scalar, its trace forces \(h=d1\), so \(v=0\). If \(h\in C\), then \(E_C(h)=h\), also giving \(v=0\). A further sufficient condition is \(C_0=C\), because (82.5) then gives \(k_0=k\). None of these containments or scalarity assertions is automatic for an arbitrary actual core.

### Exercise 82.4 — intermediate

Justify (82.12) for an unbounded integrable central \(\zeta\). Explain why its last expression uses a canonical central lift.

**Solution.** The truncations \(\zeta_n=\min(\zeta,n)\) are bounded and central in \(D_0\). Complete branch decomposition applied to \(\zeta_nv\) gives the sum of the \(L^1\) norms of \(\zeta_n(a_j-a'_j)\), equal to \(\tau(\zeta_n|v|)\). Since there are finitely many branches and all their coefficients are bounded, monotone convergence of the nonnegative absolute values passes to \(\zeta\). Conditional expectation adjointness gives \(\tau(\zeta|v|)=\tau(\zeta b)\). The central density of \(p\) is defined on \(Z(A)\), and \(\widehat b\) has corner label \(b\). This is why its defining pairing is \(\operatorname{Tr}(p\widehat b)=\tau(\zeta b)\). Physical left multiplication by \(b\in Z(S)\) need not be central in \(A\), so substituting it would not justify the identity.

### Exercise 82.5 — advanced

In \(M_2(\mathbb C)\) with the unnormalized matrix trace, take rank-one projections \(A,B\) whose ranges have angle \(0\leq\theta\leq\pi/2\). Check (82.16) exactly without assuming they commute.

**Solution.** Both square roots equal the projections themselves. Since \(\operatorname{Tr}(AB)=\cos^2\theta\), the squared Hilbert–Schmidt difference is \(2-2\cos^2\theta=2\sin^2\theta\). The selfadjoint difference \(A-B\) has trace zero and determinant \(-\sin^2\theta\), hence eigenvalues \(\sin\theta,-\sin\theta\). Its trace norm is \(2\sin\theta\). The required inequality is \(\sin^2\theta\leq\sin\theta\), valid throughout the specified range. Except at the endpoints the projections need not commute. For these projection densities the spectral integral of their squared projection differences is also exactly \(2\sin^2\theta\), because every threshold in \((0,1)\) selects \(A,B\) and every threshold above one selects zero.

### Exercise 82.6 — advanced

Does \(\inf\operatorname{spec}(a)=0\) suffice for the state criterion? Test this with \(\mathcal B=\mathcal M=Q\), a II₁ factor, and a projection \(a\) of trace \(1/3\).

**Solution.** It does not suffice. Every \(Q\)-central state on \(Q\) equals its normalized trace: apply 81.2 to \(Q\subset Q\), whose relative commutant is scalar, and evaluate the norm averages in the central state. Thus every such state has value \(1/3\) on \(a\), so none annihilates it. The positive operator has zero in its spectrum, but its noncentral states supported in \(1-a\) cannot supply the missing invariance. By the converse of 82.7 there cannot be a net of projections having all finite unitary Følner errors tend to zero and their normalized \(a\)-cost tend to zero. The projection \(p=1\) makes every commutator vanish but still has cost \(1/3\). This example tests the abstract criterion, not the actual core cost in (82.11).

The exact relative commutant and density of the actual cup-tail pair are now computed in [Cup-tail commutants and the remaining central comparison](cup-tail-commutants-and-central-comparison.md), (T.2)–(T.10). At index four the joint density input81.15 holds. Above four it is reduced to the displayed expectation identity for one actual tail atom. The unrestricted identity, state alternative and remaining full approximation obligations stay open.

## References and scope

The matrix formulas and finite cup reduction are proved for the actual common-basis square, including nonfactor cores and nonextremal ambient inclusions. The positive-cost criterion is proved for a faithful normal semifinite trace, a trace-preserving expected subalgebra with semifinite restricted trace, and arbitrary unital represented ambient subalgebra. Its projections stay in the expected subalgebra. Its state is permitted to be singular; no normal density identity is inferred from it. The full original assignment remains active: derive the actual annihilating state or another justified weighted-gap control, and complete unrestricted full partition, common-stage or generating construction, full finite pair/bicommutant comparisons, represented and opposite canonical traces, and every original clause, exercise, note and dependency. Previously proved finite-depth, factorial-core and conditional endpoints remain complete.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*

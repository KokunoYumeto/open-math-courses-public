# Group integration, recovery and regular faithfulness

Programme contribution adapted from *Crossed products and the flow of weights*, lessons OA-FLOW-L24 and OA-FLOW-L25, written by GPT-6 Astra and GPT-6 Sol (OpenAI), in Codex, at Ultra (maximum reasoning effort), and self-checked by those authors. This bounded adaptation and proof replay is by GPT-6.1 Sol (OpenAI), Ultra. Original programme lesson text and these adaptations are dedicated under **CC0 1.0**; works cited retain their own rights. No human-source prose or figures are reproduced here.

This support module supplies the scalar representation correspondence and the four-neighbor norm gap consumed by the foundations course. All statements below keep arbitrary locally compact Hausdorff groups and arbitrary Hilbert spaces.

<a id="OA-FLOW.GRP.SETTING"></a>
<a id="oa-flow.grp.setting"></a>

## OA-FLOW.GRP.SETTING — Haar measure and the convolution algebra

Let \(G\) be any locally compact Hausdorff group with a nonzero left Haar measure \(ds\). Fix

$$
\int_G q(rs)\,dr=\Delta(s)^{-1}\int_G q(r)\,dr.
\tag{G1}
$$

There is no countability, sigma compactness, separability or unimodularity assumption. Scalar \(L^p(G)\) spaces use the completed localizable Haar measure. For \(f,g\in L^1(G)\), put

$$
\begin{aligned}
&(f*g)(r)=\int_G f(s)g(s^{-1}r)\,ds,\\
&f^\sharp(r)=\Delta(r)^{-1}\overline{f(r^{-1})}.
\end{aligned}
\tag{G2}
$$

These are equivalence classes; the convolution formula is interpreted almost everywhere. Write \(\ell_s f(r)=f(s^{-1}r)\). A representation of \(L^1(G)\) means a complex-linear multiplicative star-preserving map into \(B(H)\). It is **nondegenerate** if the linear span of \(\pi(f)\xi\) is dense in \(H\). Continuity of such a map will be proved, not assumed.

<a id="OA-FLOW.GRP.IMPORT.FOUNDATIONS"></a>
<a id="oa-flow.grp.import.foundations"></a>

## OA-FLOW.GRP.IMPORT.FOUNDATIONS — Exact earlier foundations and vector integration

The following are the exact earlier proof providers used here. The linked statements retain their own hypotheses; the reductions below explain how they apply to arbitrary locally compact groups.

- Haar Conventions, tools T1–T3 give compact cutoffs, nonnegative identity-neighborhood test functions and finite partitions of unity. Haar Proposition 3.1(4) gives density of \(C_c\) in scalar \(L^p\), \(1\leq p<\infty\), and sigma-compact representatives. Haar Propositions 7.2–7.3 give the open sigma-compact subgroup and uniform continuity of compact continuous functions. Theorem 8.3 and Proposition 9.1 give Haar existence and full support. Theorem 10.1 supplies (G1), multiplicativity and continuity of \(\Delta\); Theorem 11.1 supplies inversion. Regularity and finiteness on compact sets are the Radon definitions and Proposition 2.3.
- Haar Theorem 5.1(4)–(7) gives scalar Tonelli and Fubini for the Radon product at the stated integrable or sigma-finite-support hypotheses. Measure-tools Theorems 2.1–2.2 give scalar convergence theorems, and Theorems 3.1–3.2 give Hölder, Minkowski, completeness and simple approximation. The vector version needed below is proved explicitly in this section.
- HB Lemma 4.1 gives completeness of bounded-operator spaces. HS's completion lemma, projection Theorem 2.2 and adjoint Corollary 3.2 give Hilbert completion, orthogonal complements, adjoints, the operator C*-identity and the self-adjoint quadratic-form norm formula.
- BA Construction 3.2 and Proposition 3.3 give the Banach unitization with sum norm. BA Proposition 4.2(3) gives spectral inclusion under algebraic unital homomorphisms, and BA Proposition 4.4 gives the spectral-radius bound. CF Theorem 1.3 identifies the norm and spectral radius of a normal, in particular positive, operator. CF Proposition 8.5(11) identifies operator positivity with nonnegative quadratic forms.

**Vector-integration lemma.** Let E be any Banach space. Define \(L^p(G,E)\), \(p=1,2\), as the completion, in \((\int\|f(s)\|^p ds)^{1/p}\), of finite-valued simple functions supported on Borel sets of finite Haar measure, modulo norm-zero functions. This agrees with the strongly measurable Bochner space on the completed localizable Haar measure. The space \(C_c(G,E)\) is dense. For p=1 the integral is a bounded map to E, of norm at most one, and bounded linear maps commute with it. The space \(L^2(G,K)\) is a Hilbert space for every Hilbert space K, and \(C_c(G)\odot K\) is dense in it. Absolutely norm-integrable strongly measurable fields on the Radon product have the two equal iterated Bochner integrals whenever their support is sigma-finite, as in the Haar Fubini theorem.

**Proof.** For a simple function on a disjoint finite partition set \(\int\sum_j1_{E_j}v_j=\sum_j\mu(E_j)v_j\). Refining two partitions proves independence from the expression; the triangle inequality gives \(\|\int f\|\leq\int\|f\|\). Thus Cauchy simple approximations have Cauchy integrals in the complete space E, and their limits define the integral uniquely. The same estimate gives independence of the approximating sequence. A bounded linear map commutes with the integral first on simple functions and then by norm limits.

To see the function interpretation of the completion, choose from any norm-Cauchy sequence a subsequence whose successive \(L^p\) distances are summable. Minkowski and scalar monotone convergence show that the sum of the pointwise norms of its successive differences is in \(L^p\). Outside a null set those differences are therefore summable in E, so the subsequence converges in E. The sum of the remaining norms bounds the \(L^p\) error and tends to zero. This gives a strongly measurable representative and proves completeness in the function interpretation. Conversely, for a strongly measurable function F of finite \(L^p\) norm put \(E_m=\{1/m\leq\|F\|\leq m\}\). Then \(\mu(E_m)\leq m^p\|F\|_p^p<\infty\), and \(F1_{E_m}\to F\) in \(L^p\) by scalar dominated convergence. On \(E_m\), the a.e. separable range is covered by countably many balls of radius epsilon, with centers of norm at most \(m+\varepsilon\). Assign each value to its first such ball. Replacing it by that center gives a countably valued measurable function with error at most epsilon. Keep only its first N values and use zero on the remaining parts. Those remaining parts decrease to a null set, and the additional norm error is bounded by \(2m+\varepsilon\), so dominated convergence on the finite-measure set makes their \(L^p\) error tend to zero. Then let epsilon tend to zero. This gives finite-valued simple approximations supported on finite-measure sets. All countable supports and exceptional sets occur inside sigma-finite pieces.

For scalar indicators of finite-measure sets, Haar Proposition 3.1(4) gives \(C_c(G)\) approximations. Consequently \(\sum_j1_{E_j}v_j\) is approximated by \(\sum_jh_jv_j\), with error at most \(\sum_j\|v_j\|\|1_{E_j}-h_j\|_p\). This proves the density of \(C_c(G)\odot E\), and hence of \(C_c(G,E)\). A compactly supported continuous E-valued function belongs to this completion: its compact norm image has a finite epsilon-net, whose first-encounter Borel partition on the compact support gives a simple approximation with error at most \(\varepsilon\mu(\operatorname{supp}f)^{1/p}\). For K Hilbert the integral inner product satisfies Cauchy–Schwarz by the scalar theorem. It extends to the completion and has precisely the defining norm, giving the asserted Hilbert space.

For the vector Fubini assertion, finite-valued simple fields with finite-measure support satisfy it component by component by scalar Haar Fubini. Approximate a general field F by such \(F_n\) with \(\sum_n\|F_n-F\|_1<\infty\). Scalar Tonelli applied to these norm errors shows, outside a null set of either outer variable, convergence in the inner \(L^1\) norm. The norm estimate for the integral then gives both the inner integral and convergence to it. Integrating the same norm-error bound gives convergence of the outer integrals. The scalar componentwise identities for \(F_n\) pass to these limits and give both iterated integrals equal to \(\int F\). Null sets in the completed measure may be represented by Borel null sets on the sigma-finite support, so scalar Haar Fubini also transfers to that completion. This proof uses no identity between the topological product Borel sigma-algebra and the tensor-product sigma-algebra. \(\square\)

Every particular function used in an \(L^p\) calculation has, after a null modification, support on a countable union of compact sets: use a sequence of the compact continuous approximants just constructed and a summable-error subsequence. Those supports, together with one relatively compact identity neighborhood and their inverses and finite products, generate an open sigma-compact subgroup. All effective supports of the convolution integrands for finitely many such functions lie in its corresponding products. Thus the specific product calculations reduce to sigma-finite Radon pieces even when G itself is not sigma compact. Continuous vector fields on a compact set have compact, hence separable, norm image; no separability of E or K is assumed.

<a id="OA-FLOW.GRP.TRANSLATIONS"></a>
<a id="oa-flow.grp.translations"></a>

## OA-FLOW.GRP.TRANSLATIONS — The continuity needed for recovery

**Lemma.** For \(p=1,2\), the operators \(\ell_s\) are isometries on \(L^p(G)\), form a group, and are strongly continuous. The operators

$$
\begin{gathered}
r_s f(t)=\Delta(s)^{-1}f(ts^{-1})\\
\quad(f\in L^1(G))
\end{gathered}
\tag{G3}
$$

are also isometries and depend continuously on \(s\) in \(L^1\)-norm for each \(f\).

**Proof.** Left invariance gives the first isometry, and substitution gives \(\ell_s\ell_t=\ell_{st}\). For \(f\in C_c(G)\) and \(s\) in a compact neighborhood of the identity, all supports of \(\ell_s f-f\) lie in one compact set. Continuity on compact sets, with a finite-cover argument, gives uniform convergence to zero as \(s\to e\). Multiplying the supremum bound by the finite measure of that common support proves convergence in both \(L^1\) and \(L^2\). Approximate an arbitrary \(L^p\) function by one \(C_c\) function; the isometry makes the two approximation errors uniform in \(s\). This proves continuity at the identity, and the group law proves it everywhere.

For (G3), (G1) gives \(\int|f(ts^{-1})|\,dt=\Delta(s)\|f\|_1\). This proves the isometry. The same common-support proof for \(C_c\), including continuity of \(\Delta\), and then density prove continuity for all \(L^1\). All continuity assertions apply to nets in \(G\). \(\square\)

<a id="OA-FLOW.GRP.ALGEBRA"></a>
<a id="oa-flow.grp.algebra"></a>

## OA-FLOW.GRP.ALGEBRA — Products, adjoints and a two-sided approximate identity

**Proposition.** Formula (G2) makes \(L^1(G)\) a Banach star algebra with

$$
\begin{aligned}
&\|f*g\|_1\leq\|f\|_1\|g\|_1,\\
&\|f^\sharp\|_1=\|f\|_1,\\
&(f*g)^\sharp=g^\sharp*f^\sharp.
\end{aligned}
\tag{G4}
$$

There is a net \((a_V)\) of nonnegative \(C_c(G)\) functions, of integral one and with supports shrinking to \(e\), such that

$$
\begin{gathered}
a_V*f\longrightarrow f,\\
f*a_V\longrightarrow f\\
\quad\text{in }L^1(G).
\end{gathered}
\tag{G5}
$$

**Proof.** Integrating the absolute value of the convolution and using left invariance proves the first inequality. Inversion proves the second. Associativity follows by evaluating both bracketings as the absolutely integrable double integral
\(\int\!\int f(s)g(t)h(t^{-1}s^{-1}r)\,dt\,ds\); its integrated absolute value is at most \(\|f\|_1\|g\|_1\|h\|_1\). For the last identity of (G4), multiplicativity of \(\Delta\) and the left change \(s=rt\) give

$$
\begin{aligned}
&(g^\sharp*f^\sharp)(r)\\
&=\Delta(r)^{-1}\int\begin{aligned}[t]
&\overline{g(s^{-1})}\,\\
&\quad\overline{f(r^{-1}s)}\,ds
\end{aligned}\\
&=\Delta(r)^{-1}\\
&\quad{}\cdot\overline{\int f(t)g(t^{-1}r^{-1})\,dt}\\
&=(f*g)^\sharp(r).
\end{aligned}
$$

The calculation first applies to \(C_c\), and the preceding norm estimates extend it to \(L^1\). Direct substitution gives \((f^\sharp)^\sharp=f\). Completeness is an input.

Choose \(a_V\geq0\) with support in each relatively compact identity neighborhood \(V\) and normalize its integral to one. Direct changes of variables give Bochner identities in \(L^1\):

$$
\begin{aligned}
&a_V*f=\int a_V(s)\ell_s f\,ds,\\
&f*a_V=\int a_V(s)r_s f\,ds.
\end{aligned}
\tag{G6}
$$

The second identity includes the factor \(\Delta(s)^{-1}\) in (G3). Subtract \(f\) in each integral and apply the preceding norm continuities uniformly for \(s\in V\). This proves (G5). The functions need not be symmetric, and the group need not be unimodular. \(\square\)

<a id="OA-FLOW.GRP.CONTRACTIVITY"></a>
<a id="oa-flow.grp.contractivity"></a>

## OA-FLOW.GRP.CONTRACTIVITY — Algebraic star representations are bounded

**Lemma.** Every star representation \(\pi:L^1(G)\to B(H)\), including a degenerate one, satisfies \(\|\pi(f)\|\leq\|f\|_1\).

**Proof.** Extend it algebraically to the unitization by \(\pi^+(f,z)=\pi(f)+zI\). A unital homomorphism sends an inverse to an inverse, so the spectrum of \(\pi(f^\sharp*f)\) is contained in the spectrum of \((f^\sharp*f,0)\) in the Banach unitization. Positivity and the spectral-radius bound give

$$
\begin{aligned}
&\|\pi(f)\|^2=\|\pi(f)^*\pi(f)\|\\
&\leq r_{L^1(G)^+}((f^\sharp*f,0))\\
&\leq\|f^\sharp*f\|_1\\
&\leq\|f\|_1^2.
\end{aligned}
\tag{G7}
$$

No continuity of \(\pi^+\) was used to preserve invertibility. \(\square\)

If \(\pi\) is nondegenerate, (G5) and contractivity show \(\pi(a_V)\to I\) strongly: convergence holds on every \(\pi(f)\xi\), and these vectors span a dense subspace, while \(\|\pi(a_V)\|\leq1\).

<a id="OA-FLOW.GRP.INTEGRATION"></a>
<a id="oa-flow.grp.integration"></a>

## OA-FLOW.GRP.INTEGRATION — From a continuous unitary group to an algebra representation

Let \(U:G\to\mathcal U(H)\) be a strongly continuous unitary representation. Define

$$\pi_U(f)\xi=\int_G f(s)U_s\xi\,ds.\tag{G8}$$

This is a Bochner integral. Indeed, approximate \(f\) in \(L^1\) by \(C_c\) functions. On each compact support the continuous vector image is compact and hence separable; the approximating vector integrals form a Cauchy sequence, with difference bounded by \(\|f-g\|_1\|\xi\|\). Equivalently the vector field has an almost-everywhere separable measurable range on the countable union of those supports. The result is independent of the approximating sequence.

**Theorem.** The map \(\pi_U\) is a nondegenerate star representation, and \(\|\pi_U(f)\|\leq\|f\|_1\).

**Proof.** The estimate follows from unitarity. Multiplication follows by integrating \(f(s)g(t)U_{st}\) and putting \(r=st\). Adjointing the scalar matrix coefficient and then using inversion gives exactly the involution in (G2). These computations first apply to compactly supported functions; the same norm estimates and (G4) extend them to all \(L^1\). Finally

$$
\begin{aligned}
&\|(\pi_U(a_V)-I)\xi\|\\
&\leq\sup_{s\in V}\|U_s\xi-\xi\|\\
&\longrightarrow0.
\end{aligned}
\tag{G9}
$$

Every vector is therefore in the closure of \(\pi_U(L^1(G))H\). \(\square\)

<a id="OA-FLOW.GRP.RECOVERY"></a>
<a id="oa-flow.grp.recovery"></a>

## OA-FLOW.GRP.RECOVERY — Construct the individual unitaries from translated functions

**Theorem.** Every nondegenerate star representation \(\pi\) of \(L^1(G)\) is \(\pi_U\) for a unique strongly continuous unitary representation \(U\) on the same Hilbert space.

**Proof.** On the dense linear subspace \(D=\operatorname{span}\pi(L^1(G))H\), prescribe

$$
\begin{aligned}
&U_s\left(\sum_j\pi(f_j)\xi_j\right)\\
&=\sum_j\pi(\ell_s f_j)\xi_j.
\end{aligned}
\tag{G10}
$$

For any \(f,g\in L^1(G)\), Haar changes of variables give

$$
(\ell_s g)^\sharp*(\ell_s f)=g^\sharp*f.
\tag{G11}
$$

For example \((g^\sharp*f)(r)=\int\overline{g(t)}f(tr)\,dt\); replacing both functions by their left translates leaves this integral unchanged by left invariance. The identity is first checked on \(C_c\), then extended using (G4).

Expand the squared norm of the right side of (G10) into its finitely many Gram terms. Each term is unchanged by (G11) and the star-representation property. Thus the proposed vector has the same norm as the original vector. In particular a zero vector has zero image, which proves independence from its chosen expression. The maps on \(D\) are linear isometries. Their products satisfy the group law by \(\ell_s\ell_t=\ell_{st}\), and the map for \(s^{-1}\) is their inverse. They extend to unitaries on \(H\).

For a vector \(\pi(f)\xi\), contractivity gives

$$
\begin{aligned}
&\|(U_s-U_t)\pi(f)\xi\|\\
&\leq\|\ell_s f-\ell_t f\|_1\|\xi\|.
\end{aligned}
\tag{G12}
$$

The translation lemma proves continuity on \(D\); the uniform unitary bound and density prove it on every vector. To recover the integrated operators, use the \(L^1\)-valued Bochner identity \(f*g=\int f(s)\ell_s g\,ds\). Equation (G10) and boundedness of \(\pi\) give

$$
\begin{aligned}
&\pi_U(f)\pi(g)\xi\\
&=\int f(s)\pi(\ell_s g)\xi\,ds\\
&=\pi(f*g)\xi\\
&=\pi(f)\pi(g)\xi.
\end{aligned}
\tag{G13}
$$

Density proves \(\pi_U(f)=\pi(f)\). Conversely, if a strongly continuous unitary representation integrates to \(\pi\), left translation in (G8) gives \(U_s\pi(f)=\pi(\ell_s f)\). It must therefore agree with (G10) on the dense subspace and is unique. \(\square\)

<a id="OA-FLOW.GRP.INTERTWINERS"></a>
<a id="oa-flow.grp.intertwiners"></a>

## OA-FLOW.GRP.INTERTWINERS — What the correspondence preserves

If \(U,V\) act on \(H,K\) and \(A:H\to K\) is bounded, then

$$
\begin{gathered}
AU_s=V_sA\ (s\in G)\\
\Longleftrightarrow\\
A\pi_U(f)=\pi_V(f)A\\
\ (f\in L^1(G)).
\end{gathered}
\tag{G14}
$$

The forward direction passes a bounded operator through (G8). In the reverse direction, on a vector \(\pi_U(f)\xi\), the recovery formula gives


$$
\begin{aligned}
&AU_s\pi_U(f)\xi=A\pi_U(\ell_s f)\xi\\
&=\pi_V(\ell_s f)A\xi\\
&=V_sA\pi_U(f)\xi
\end{aligned}
$$

.
Density gives equality everywhere. Thus unitary equivalence, commutants and reducing subspaces are preserved.

For a degenerate \(\pi\), put \(H_0=\overline{\pi(L^1(G))H}\). This subspace is reducing, and \(\pi\) vanishes on \(H_0^\perp\): a vector in that complement is orthogonal to every \(\pi(f)^*\eta\). The restriction on \(H_0\) is nondegenerate, since (G5) puts each \(\pi(f)\xi\) in the closure of products \(\pi(a_V)\pi(f)\xi\). The theorem recovers a unitary group precisely on \(H_0\). If \(H_0\ne H\), no strongly continuous unitary group on all of \(H\) can integrate to the original \(\pi\), because (G9) would force its essential space to be all of \(H\). The zero Hilbert space has the unique trivial interpretation of all assertions.

<a id="OA-FLOW.GRP.REGULAR"></a>
<a id="oa-flow.grp.regular"></a>

## OA-FLOW.GRP.REGULAR — Faithfulness before completion

The left translations on \(L^2(G)\) form a strongly continuous unitary representation by the translation lemma. Its integrated representation is

$$\lambda(f)\xi=\int f(s)\xi(s^{-1}r)\,ds.\tag{G15}$$

**Theorem.** The representation \(\lambda:L^1(G)\to B(L^2(G))\) is faithful and nondegenerate.

**Proof.** Nondegeneracy follows from (G9). Suppose \(\lambda(f)=0\). For \(g\in C_c(G)\), (G15) represents the convolution \(f*g\) in \(L^2\), with
\(\|f*g\|_2\leq\|f\|_1\|g\|_2\).
This identity follows first for compactly supported \(f\), then by \(L^1\) approximation and the vector integral bound. Hence \(f*g=0\) as an \(L^2\) class.

It also has a continuous representative. Choose \(f_n\in C_c(G)\) converging to \(f\) in \(L^1\). Their convolutions with \(g\) are continuous, by the compact-support integral argument, and
\(\|f_n*g-f_m*g\|_\infty\leq\|f_n-f_m\|_1\|g\|_\infty\).
The uniform limit is continuous and agrees almost everywhere with the \(L^1\) convolution and the \(L^2\) vector integral. A continuous function that is zero almost everywhere is zero everywhere, since Haar measure has full support. In particular \(f*a_V=0\). Equation (G5) now gives \(f=0\) in \(L^1\). \(\square\)

<a id="OA-FLOW.GRP.MODELS"></a>
<a id="oa-flow.grp.models"></a>

## OA-FLOW.GRP.MODELS — The exact four-neighbor norm gap

**The four-neighbor tree.** Let \(G\) be the free group on two generators \(a,b\), with counting Haar measure, and put

$$h=\delta_a+\delta_{a^{-1}}+\delta_b+\delta_{b^{-1}}.\tag{G20}$$

For this element define \(\|h\|_u\) to be the supremum of \(\|U_a+U_{a^{-1}}+U_b+U_{b^{-1}}\|\) over strongly continuous unitary representations of this discrete group, and \(\|h\|_r=\|\lambda(h)\|\). The values of the first expression form a bounded subset of \([0,4]\); no cardinality-restricted family of representations is needed. The trivial representation gives \(\|h\|_u\geq4\), and the triangle inequality gives the reverse inequality. Thus \(\|h\|_u=4\). We now compute \(\|h\|_r=2\sqrt3\).

The Cayley graph is a tree, rooted at the identity. Each nonroot vertex has one parent and three children; the root has four children. The operator \(A=\lambda(h)\) sums neighboring coordinates and is self-adjoint. For finitely supported \(\xi\), sum once over each oriented parent-child edge \((v,w)\). The inequality

$$
\begin{aligned}
&2|\xi(v)\xi(w)|\leq3^{-1/2}|\xi(v)|^2\\
&\quad+3^{1/2}|\xi(w)|^2
\end{aligned}
\tag{G21}
$$

gives \(|\langle A\xi,\xi\rangle|\leq2\sqrt3\|\xi\|^2\): a nonroot coefficient is \(3/\sqrt3+\sqrt3\), and the root coefficient \(4/\sqrt3\) is smaller. Density and self-adjointness yield the upper norm bound.

For the lower bound let \(\xi_R(v)=3^{-|v|/2}\) for word lengths \(0\leq|v|\leq R\), and zero otherwise. There are \(4\cdot3^{k-1}\) vertices at depth \(k\geq1\), so

$$
\begin{aligned}
&\|\xi_R\|^2=1+\frac43R,\\
&\langle A\xi_R,\xi_R\rangle=\frac8{\sqrt3}R.
\end{aligned}
\tag{G22}
$$

The second identity counts \(4\cdot3^k\) edges from depth \(k\) to depth \(k+1\), each with coordinate product \(3^{-k-1/2}\), for \(0\leq k<R\), and counts each edge twice in the quadratic form. Their ratio tends to \(2\sqrt3\). This proves the lower bound and the exact reduced norm. The two displayed norms consequently differ. The regular representation remains faithful on every nonzero \(L^1\) function, as the theorem proved.

## Programme provenance

The scalar mathematical antecedent recorded by the original programme lesson is Takesaki, *Theory of Operator Algebras I*, Chapter I, the group-representation exercise in section 9 and the convolution algebra in section 1. The complete argument reused here is the independently written programme proof, with its nondegenerate and degenerate cases explicit. The exact selected source ranges and byte hashes, source credit and dependency correspondence are recorded in the accompanying receipt.

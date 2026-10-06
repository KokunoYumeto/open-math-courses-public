# Covariant integration and recovery with nonunital coefficients

Programme contribution adapted from *Crossed products and the flow of weights*, lessons OA-FLOW-L24 and OA-FLOW-L25, written by GPT-6 Astra and GPT-6 Sol (OpenAI), in Codex, at Ultra (maximum reasoning effort), and self-checked by those authors. This bounded adaptation and proof replay is by GPT-6.1 Sol (OpenAI), Ultra. Original programme lesson text and these adaptations are dedicated under **CC0 1.0**; works cited retain their own rights. No human-source prose or figures are reproduced here.

This support module supplies the algebra laws, covariant representation correspondence, regular faithfulness and transformation models consumed by the foundations course. Coefficients may be nonunital, and the group, algebra and Hilbert spaces may be nonseparable.

<a id="OA-FLOW.CCOV.SETTING"></a>
<a id="oa-flow.ccov.setting"></a>

## OA-FLOW.CCOV.SETTING — Left coefficients and a Banach convolution algebra

Let A be a C-star algebra, let G be a locally compact Hausdorff group, and let
\(\alpha:G\to\operatorname{Aut}(A)\) be an action such that \(s\mapsto\alpha_s(a)\) is norm continuous for every \(a\in A\). The algebra and Hilbert spaces need not be separable; G need not be sigma compact or unimodular. Fix left Haar measure and the convention

$$\int q(rs)\,dr=\Delta(s)^{-1}\int q(r)\,dr.\tag{C1}$$

Write \(B=L^1(G,A)\) for Bochner-integrable A-valued functions modulo null sets, with \(\|f\|_1=\int\|f(s)\|\,ds\). Scalar and vector spaces use the completed localizable Haar interpretation of the scalar support module. Put

$$
\begin{aligned}
&(f*g)(r)\\
&=\int f(s)\alpha_s(g(s^{-1}r))\,ds,\\
&f^\sharp(r)\\
&=\Delta(r)^{-1}\alpha_r(f(r^{-1})^*).
\end{aligned}
\tag{C2}
$$

The action in the involution is \(\alpha_r\). The choice is forced by integrating coefficients on the left of group unitaries.

A representation of B is a complex-linear algebraic star homomorphism \(\Pi:B\to B(H)\); boundedness will follow. It is nondegenerate if \(\operatorname{span}\Pi(B)H\) is dense. A covariant pair \((\rho,U)\) consists of a nondegenerate star representation \(\rho:A\to B(H)\) and a strongly continuous unitary representation of G satisfying

$$U_s\rho(a)U_s^*=\rho(\alpha_s(a)).\tag{C3}$$

When \(A=0\) or \(H=0\), the nondegenerate assertions have their unique zero interpretation. There is no unit in A unless one is explicitly assumed.

<a id="OA-FLOW.CCOV.IMPORT.FOUNDATIONS"></a>
<a id="oa-flow.ccov.import.foundations"></a>

## OA-FLOW.CCOV.IMPORT.FOUNDATIONS — Exact coefficient inputs

Use the exact Haar, Banach, Hilbert and vector-integration results in the scalar support module's foundational section. Its proofs cover Banach-valued integrals and \(L^2(G,K)\) at arbitrary Hilbert dimension, and keep every product calculation on its actual sigma-finite Radon support. Its contractivity argument applies to any Banach star algebra with submultiplicative norm and isometric involution after its laws are proved.

The additional coefficient inputs are BA Proposition 3.4 and its forced-unitization construction, CF Theorem 4.2, CF Proposition 8.5(2),(10) and CF Theorem 11.4 with Corollary 11.5(1). These supply the C*-unitization of A, contractivity of star homomorphisms, the inequality \(a^*a\leq\|a\|^2 1\), its positive square root and a positive contractive two-sided approximate identity \((e_i)\). The Banach unitization of B used for automatic boundedness is distinct from this C*-unitization of A. A faithful coefficient representation is an explicit hypothesis of the regular-faithfulness theorem; existence of a faithful representation is not an extra premise needed for the correspondence proof.

For transformation spaces, compact cutoffs come from Haar Conventions T1–T3, which are stated for all LCH spaces. BA Proposition 1.2 supplies the C*-algebra \(C_0(\Omega)\). Its compact-support density is the earlier programme result cited in that proposition; it can also be checked directly: for \(a\in C_0(\Omega)\) and \(\varepsilon>0\), take a compact cutoff equal to one on \(\{|a|\geq\varepsilon\}\); then \(\|a-ha\|_\infty\leq\varepsilon\) and \(ha\in C_c(\Omega)\). BA Proposition 12.1 and the immediately following Bochner-space identification identify the completed compact transformation convolution algebra with \(L^1(G,C_0(\Omega))\). That algebra construction does not use representation recovery, so this dependency has no reverse edge to the present module.

The vector-integration lemma gives density of \(C_c(G,A)\) in B: approximate a finite-valued simple function by a finite sum of compact scalar continuous functions times its coefficient values. Point-norm continuity of the action is uniform on every compact norm subset of A: choose a finite epsilon-net and use the isometry of every automorphism to control both approximation errors uniformly in the group parameter. Compact scalar translation estimates and that finite-net argument prove the vector translation estimates used below. Neither G, A nor any Hilbert space is assumed separable.

<a id="OA-FLOW.CCOV.ALGEBRA"></a>
<a id="oa-flow.ccov.algebra"></a>

## OA-FLOW.CCOV.ALGEBRA — Norm bounds and a product approximate identity

Define bounded operations on B by

$$\begin{aligned}
L_a f(r)&=a f(r),\\
M_s f(r)&=\alpha_s(f(s^{-1}r)),\\
N_s f(r)&=\Delta(s)^{-1}f(rs^{-1}).
\end{aligned}\tag{C4}$$

The last two are isometries. The map \(s\mapsto M_s f\) is norm continuous: for \(f\in C_c(G,A)\), the moving support stays in one compact set near a fixed s, and point-norm continuity of the action is uniform on compact subsets of A. The latter follows by a finite approximation and the isometry of automorphisms. This gives a uniform integrand estimate on the common support. Density extends the result to B. The same proof, using continuity of \(\Delta\), gives continuity of \(s\mapsto N_s f\). These are assertions about nets.

**Proposition.** Equation (C2) makes B a Banach star algebra and

$$
\begin{aligned}
&\|f*g\|_1\leq\|f\|_1\|g\|_1,\\
&\|f^\sharp\|_1=\|f\|_1.
\end{aligned}
\tag{C5}
$$

It has a positive-coefficient contractive approximate identity

$$
\begin{gathered}
b_{V,i}(s)=\varphi_V(s)e_i,\\
\varphi_V\in C_c(G),\\
\varphi_V\geq0,\\
\int\varphi_V=1,\\
\operatorname{supp}\varphi_V\subset V,
\end{gathered}
\tag{C6}
$$

where identity neighborhoods V shrink and i increases, independently in the product directed set. Positivity here describes the coefficients; it does not assert that \(b_{V,i}\) is positive in every completion.

**Proof.** Haar invariance and the isometry of \(\alpha_s\) give (C5). The common iterated expression for both associative bracketings is
\(\int\!\int f(s)\alpha_s(g(t))\alpha_{st}(h(t^{-1}s^{-1}r))\,dt\,ds\), whose integrated norm is bounded by the product of the three L1 norms. For the involution law, multiplication of modular factors gives

$$
\begin{aligned}
&(g^\sharp*f^\sharp)(r)\\
&=\Delta(r)^{-1}\int\begin{aligned}[t]
&\alpha_s(g(s^{-1})^*)\\
&\quad{}\cdot\alpha_r(f(r^{-1}s)^*)\,ds
\end{aligned}\\
&=\Delta(r)^{-1}\\
&\quad{}\cdot\alpha_r\left(\int\begin{aligned}[t]
&f(t)\\
&{}\cdot\alpha_t(g(t^{-1}r^{-1}))\,dt
\end{aligned}\right)^*\\
&=(f*g)^\sharp(r).
\end{aligned}
\tag{C7}
$$

The second line uses the left change \(s=rt\). Applying the involution twice gives f. These calculations first hold on \(C_c(G,A)\), where continuity, compact supports and Bochner Fubini apply, and extend by the norm estimates. Completeness is a Banach input.

For the left approximate identity, (C2) gives

$$b_{V,i}*f=\int\varphi_V(s)L_{e_i}M_s f\,ds.$$

Consequently

$$
\begin{aligned}
&\|b_{V,i}*f-f\|_1\\
&\leq\|L_{e_i}f-f\|_1+\\
&\quad\sup_{s\in V}\|M_s f-f\|_1.
\end{aligned}
\tag{C8}
$$

For the right one put \(q_i(r)=f(r)\alpha_r(e_i)\). Inversion in the convolution variable gives

$$f*b_{V,i}=\int\varphi_V(s)N_s q_i\,ds,$$

and hence

$$
\begin{aligned}
&\|f*b_{V,i}-f\|_1\\
&\leq\|q_i-f\|_1+\\
&\quad\sup_{s\in V}\|N_s f-f\|_1.
\end{aligned}
\tag{C9}
$$

For f in \(C_c(G,A)\), its image is compact, and so is the image of \(r\mapsto\alpha_{r^{-1}}(f(r))\). A contractive approximate identity acts uniformly on each compact subset of A, by a finite-cover estimate. Thus \(L_{e_i}f\to f\) and \(q_i\to f\) in L1. Contractivity and density extend both limits to every f in B. Equations (C8)–(C9) prove convergence of the actual product net, without dominated convergence for arbitrary nets. Finally \(\|b_{V,i}\|_1\leq1\). \(\square\)

**Automatic boundedness.** Every algebraic star representation of B is contractive. Apply the unitization spectral argument of the scalar contractivity lemma to \(f^\sharp*f\); (C5) supplies precisely the required norm bound. If \(\Pi\) is nondegenerate, then \(\Pi(b_{V,i})\to I\) strongly, first on \(\Pi(B)H\) by the left approximate identity and then by the uniform bound on all of H.

<a id="OA-FLOW.CCOV.INTEGRATION"></a>
<a id="oa-flow.ccov.integration"></a>

## OA-FLOW.CCOV.INTEGRATION — From a covariant pair to convolution

For a covariant pair define

$$\Pi_{\rho,U}(f)\xi=\int\rho(f(s))U_s\xi\,ds.\tag{C10}$$

For a compactly supported continuous f the vector integrand is continuous with compact image. The norm bound \(\|f\|_1\|\xi\|\) extends the integral to B exactly as in the scalar module’s vector-integration lemma.

**Theorem.** Equation (C10) is a contractive nondegenerate star representation of B.

**Proof.** Moving a coefficient through a unitary by (C3) turns the product integrand into
\(\rho(f(s)\alpha_s(g(t)))U_{st}\). The left change \(r=st\) yields (C2). For the adjoint, inversion gives

$$
\begin{aligned}
&\Pi(f)^*\\
&=\int U_{s^{-1}}\rho(f(s)^*)\,ds\\
&=\int\rho\left(\begin{aligned}[t]
&\Delta(r)^{-1}\\
&{}\cdot\alpha_r(f(r^{-1})^*)
\end{aligned}\right)U_r\,dr\\
&=\Pi(f^\sharp).
\end{aligned}
\tag{C11}
$$

Fubini proves these identities first on compact supports and the norm estimate extends them. Nondegeneracy of \(\rho\) gives \(\rho(e_i)\to I\) strongly, by the approximate identity on represented vectors. If \(U(\varphi_V)=\int\varphi_V(s)U_s\,ds\), the scalar integration theorem gives \(U(\varphi_V)\to I\) strongly. Thus

$$\Pi(b_{V,i})=\rho(e_i)U(\varphi_V)\longrightarrow I\tag{C12}$$

strongly on the product net; the error on \(\xi\) is bounded by
\(\|(U(\varphi_V)-I)\xi\|+\|(\rho(e_i)-I)\xi\|\). \(\square\)

<a id="OA-FLOW.CCOV.COEFFICIENTRECOVERY"></a>
<a id="oa-flow.ccov.coefficientrecovery"></a>

## OA-FLOW.CCOV.COEFFICIENTRECOVERY — Recover the coefficient algebra by a norm comparison

Let \(\Pi\) be a nondegenerate representation of B and put
\(D=\operatorname{span}\Pi(B)H\). For a in A prescribe

$$
\begin{aligned}
&\rho(a)\sum_j\Pi(f_j)\xi_j\\
&=\sum_j\Pi(L_a f_j)\xi_j.
\end{aligned}
\tag{C13}
$$

The operations \(L_a\) also make sense for a in the unitization of A.

**Lemma.** Formula (C13) is well-defined and extends to a nondegenerate star representation of A with \(\|\rho(a)\|\leq\|a\|\).

**Proof.** Direct substitution in (C2) gives, for a,b in the unitization,

$$(L_a g)^\sharp*(L_b f)=g^\sharp*L_{a^*b}f.\tag{C14}$$

For a fixed a take \(c=(\|a\|^2 1-a^*a)^{1/2}\). Expanding the squared norms of the two finite sums produced by \(L_a\) and \(L_c\), equation (C14) gives

$$
\begin{aligned}
&\left\|\sum_j\Pi(L_a f_j)\xi_j\right\|^2\\
&{}+\left\|\sum_j\Pi(L_c f_j)\xi_j\right\|^2\\
&=\|a\|^2\left\|\sum_j\Pi(f_j)\xi_j\right\|^2.
\end{aligned}
\tag{C15}
$$

Therefore the first sum has norm at most \(\|a\|\) times the original vector norm; in particular a zero vector has zero image. This proves well-definedness and the bound. Linearity and multiplication follow from the corresponding laws of \(L_a\). The mixed Gram identity (C14), with one coefficient equal to 1, gives the adjoint identity on D, hence on H. Finally \(L_{e_i}f\to f\) in L1 implies \(\rho(e_i)\to I\) strongly on D and then on H. This proves nondegeneracy. \(\square\)

The square root is taken in the unitization only to prove an inequality. It does not turn the nonunital coefficient algebra into a unital hypothesis.

<a id="OA-FLOW.CCOV.GROUPRECOVERY"></a>
<a id="oa-flow.ccov.grouprecovery"></a>

## OA-FLOW.CCOV.GROUPRECOVERY — Recover the group and its covariance

On the same dense D prescribe

$$
\begin{aligned}
&U_s\sum_j\Pi(f_j)\xi_j\\
&=\sum_j\Pi(M_s f_j)\xi_j.
\end{aligned}
\tag{C16}
$$

**Theorem.** These operators extend to a strongly continuous unitary representation. Together with (C13) they form the unique covariant pair integrating to \(\Pi\).

**Proof.** The second Gram identity is

$$(M_s g)^\sharp*(M_s f)=g^\sharp*f.\tag{C17}$$

One way to check it is to write

$$(g^\sharp*f)(r)=\int\alpha_{t^{-1}}(g(t)^*f(tr))\,dt.$$

Replacing g and f by \(M_s g,M_s f\) and putting \(t=su\) returns this integral. Thus finite Gram sums show that (C16) is well-defined and isometric. The identities \(M_sM_t=M_{st}\) and \(M_{s^{-1}}=M_s^{-1}\) give unitaries after completion. The L1 continuity of \(M_s f\) gives continuity on D, and density with the unitary bound gives strong continuity on H.

On B, \(M_sL_a=L_{\alpha_s(a)}M_s\). Hence (C3) holds on D and then on H. Finally

$$(f*g)=\int L_{f(s)}M_s g\,ds\quad\text{in }B.$$

Passing the bounded map \(h\mapsto\Pi(h)\xi\) through this Bochner integral gives

$$
\begin{aligned}
&\Pi_{\rho,U}(f)\Pi(g)\xi\\
&=\int\rho(f(s))U_s\Pi(g)\xi\,ds\\
&=\Pi(f*g)\xi\\
&=\Pi(f)\Pi(g)\xi.
\end{aligned}
\tag{C18}
$$

Density identifies the integrated representation with \(\Pi\). Conversely every integrating pair satisfies
\(\rho(a)\Pi(f)=\Pi(L_a f)\) and \(U_s\Pi(f)=\Pi(M_s f)\), so (C13) and (C16) determine it uniquely. \(\square\)

Bounded intertwiners are also preserved. An intertwiner of two covariant pairs passes through (C10). An intertwiner of their integrated representations commutes with both recovery prescriptions on their dense essential spaces, and hence intertwines both recovered families. In particular unitary equivalence, commutants and reducing subspaces are preserved.

For a degenerate \(\Pi\), its essential space \(H_0=\overline{\Pi(B)H}\) reduces the representation, and the representation is zero on \(H_0^\perp\). Apply the theorem on \(H_0\). If the coefficient representation in the covariance equation is allowed to be degenerate, the pair may carry arbitrary group action on the complementary zero-coefficient summand; integration does not recover that action. This is why the correspondence specifies nondegeneracy.

<a id="OA-FLOW.CCOV.REGULAR"></a>
<a id="oa-flow.ccov.regular"></a>

## OA-FLOW.CCOV.REGULAR — Faithfulness on the convolution algebra

Let \(\rho:A\to B(K)\) be nondegenerate. On \(L^2(G,K)\) put

$$
\begin{aligned}
&\widetilde\rho(a)\xi\\
&=\rho(\alpha_{r^{-1}}(a))\xi(r),\\
&\lambda_s\xi=\xi(s^{-1}r).
\end{aligned}
\tag{C19}
$$

Point-norm continuity makes the coefficient field continuous and bounded. Thus these are bounded coefficient operators and strongly continuous unitary translations. Multiplication and adjoints are pointwise, and substitution proves covariance. Nondegeneracy of \(\widetilde\rho\) can be checked without convergence theorems for nets: for \(h\in C_c(G)\), \(a\in A\), \(\eta\in K\), the functions \(r\mapsto h(r)\rho(a)\eta\) are approximated by applying \(\widetilde\rho(e_i)\), since the compact family \(\alpha_r(a)\) satisfies \(e_i\alpha_r(a)\to\alpha_r(a)\) uniformly on \(\operatorname{supp}h\). These functions span a dense subspace, and the operators are contractions.

Denote the integrated representation by \(T_\rho\). On compact test sections,

$$
\begin{aligned}
&T_\rho(f)\xi\\
&=\int\rho(\alpha_{r^{-1}}(f(s)))\\
&\quad\xi(s^{-1}r)\,ds.
\end{aligned}
\tag{C20}
$$

This follows first on compact supports by vector testing and Fubini, and extends in L1 by the operator norm bound. It is an almost-everywhere formula, not a point-evaluation definition for arbitrary sections.

**Theorem.** If \(\rho\) is faithful, \(T_\rho\) is faithful on B.

**Proof.** Suppose \(T_\rho(f)=0\). Fix \(g\in C_c(G,A)\) and \(\eta\in K\), and use the compact continuous section

$$\xi_{g,\eta}(r)=\rho(\alpha_{r^{-1}}(g(r)))\eta.$$

Equation (C20) gives

$$
\begin{aligned}
&T_\rho(f)\xi_{g,\eta}\\
&=\rho(\alpha_{r^{-1}}((f*g)(r)))\eta.
\end{aligned}
\tag{C21}
$$

Here \(h=f*g\) has a bounded continuous representative. Indeed \(\|h\|_\infty\leq\|f\|_1\|g\|_\infty\), and right-uniform continuity of a compactly supported continuous g gives
\(\sup_t\|g(tu)-g(t)\|\to0\) as \(u\to e\). Applying this estimate inside the convolution integral proves continuity of h. Equation (C21) first holds for compactly supported f. If \(f_n\to f\) in L1 with \(f_n\in C_c(G,A)\), then \(f_n*g\to h\) uniformly, while the left sides converge in L2. On each compact set K the right sides converge in local L2 to the displayed continuous function. Because \(T_\rho(f)=0\) the global L2 norms of the left sides tend to zero. Thus the limit continuous function is zero in L2 on each compact K. This argument only uses finite-measure compact restrictions; it does not require a global pointwise identification for a general f.

The continuous function on the right of (C21) is therefore zero everywhere: a nonzero value would stay bounded away from zero on a relatively compact nonempty open set of positive Haar measure. For each r this is true for every \(\eta\), so faithfulness of \(\rho\) gives \(h(r)=0\). We have proved \(f*g=0\) for every \(g\in C_c(G,A)\). Taking \(g=b_{V,i}\) and using (C9) gives f=0 in B. \(\square\)

This theorem uses faithfulness only at the final coefficient implication. It does not claim that every covariant representation with faithful coefficient part has faithful integration.

<a id="OA-FLOW.CCOV.TRANSFORMATIONS"></a>
<a id="oa-flow.ccov.transformations"></a>

## OA-FLOW.CCOV.TRANSFORMATIONS — Right actions and two worked models

Let \(\Omega\) be locally compact Hausdorff and let \((\omega,s)\mapsto\omega s\) be a continuous right action of G. On \(A=C_0(\Omega)\) set
\(\alpha_s(a)(\omega)=a(\omega s)\). This is a point-norm continuous action. For \(a\in C_c(\Omega)\), continuity on compact parameter sets and a common compact support near the identity prove norm continuity; density extends it to \(C_0(\Omega)\). Thus the algebra, integration, recovery and regular-faithfulness theorems apply, with

$$
\begin{aligned}
&(f*g)(r)(\omega)\\
&=\int f(s)(\omega)g(s^{-1}r)(\omega s)\,ds,\\
&f^\sharp(r)(\omega)\\
&=\Delta(r)^{-1}\overline{f(r^{-1})(\omega r)}.
\end{aligned}
\tag{C27}
$$

The coefficient and group recovery operations are

$$
\begin{aligned}
&L_a f(r)(\omega)=a(\omega)f(r)(\omega),\\
&M_t f(r)(\omega)\\
&=f(t^{-1}r)(\omega t).
\end{aligned}
\tag{C28}
$$

Neither coordinate shift can be omitted or moved without changing the integrated convention. Compactly supported continuous functions on \(G\times\Omega\) map into \(C_c(G,C_0(\Omega))\). They are dense there in the L1 norm: the compact norm image of a coefficient function can be approximated uniformly by cutting off all its values outside one compact subset of \(\Omega\). Its L1 completion is therefore B, as also proved in BA Proposition 12.1, and bounded nondegenerate star representations of this compact transformation algebra extend uniquely to B and have exactly the representation correspondence proved above. Indeed, a bounded map extends to the completion, multiplication and involution persist by continuity, and approximating B elements by compact functions preserves its essential space. Conversely restriction of a contractive B-representation is bounded and has the same essential space. A claim about all algebraic representations of that uncompleted smaller algebra would require a separate boundedness hypothesis or theorem.

**Three moving points.** Take \(G=\Omega=\mathbb Z/3\mathbb Z\), counting Haar measure and right addition. On \(\mathbb C^3\), let \(\rho(a)\) be diagonal multiplication and \(U_s\xi=\xi(j+s)\). For i,j modulo 3, let \(f_{ij}\) be supported at group element \(j-i\), with coefficient the indicator of point i. Direct substitution in (C27) gives

$$
\begin{aligned}
&f_{ij}*f_{kl}=\delta_{jk}f_{il},\\
&f_{ij}^\sharp=f_{ji},\\
&\Pi_{\rho,U}(f_{ij})=E_{ij}.
\end{aligned}
\tag{C29}
$$

These nine functions span B, so B is the matrix star algebra \(M_3(\mathbb C)\). The displayed integrated representation identifies B faithfully with the matrix star algebra, since it sends a basis to the nine matrix units. This checks the direction of both coordinate shifts without a completion or norm-comparison theorem. For example, the product has coefficient at point i only when its second index j equals k, and then its group support is (j-i)+(l-k)=l-i; the involution changes that support to i-j and its coefficient point from i to j. Acting on a vector gives the coordinate at i equal to its former coordinate at j, exactly E_{ij}.

**A nonunital translation calculation.** For \(A=C_0(\mathbb R)\), \(G=\mathbb R\) and \(\alpha_s(a)(x)=a(x+s)\), use multiplication on \(L^2(\mathbb R)\) and \(U_s\xi=\xi(x+s)\). If \(\eta,\zeta\in C_c(\mathbb R)\), put
\(f(s)(x)=\eta(x)\overline{\zeta(x+s)}\). This belongs to \(C_c(\mathbb R,C_0(\mathbb R))\): its group support lies in the compact difference of the two supports, and translations of \(\zeta\) are uniformly continuous. Changing \(y=x+s\) gives

$$
\begin{aligned}
&\Pi(f)\xi\\
&=\eta(x)\int\overline{\zeta(y)}\xi(y)\,dy.
\end{aligned}
\tag{C30}
$$

Thus integrated operators include the rank-one operators formed from compact continuous vectors. Taking two orthonormal such vectors gives four explicit matrix units. Meanwhile compact coefficient cutoffs \(0\leq e_i\leq1\), equal to 1 on compact intervals increasing to cover all of the real line, give multiplication operators converging strongly to I, with \(\|\rho(e_i)-I\|=1\) for every compactly supported cutoff. Coefficient recovery therefore naturally uses strong convergence even in this elementary nonunital example. No identification of the entire completion is inferred from the rank-one calculation alone.

## Programme provenance

The transformation antecedents are Takesaki, *Theory of Operator Algebras I*, Chapter I, exercises 1.2 and 9.5, and the coefficient convolution antecedent is in *Theory of Operator Algebras II*, Chapter X, exercise 4.1. The full argument reused here is the programme’s independent exposition, whose proofs retain arbitrary coefficients, groups and Hilbert spaces.

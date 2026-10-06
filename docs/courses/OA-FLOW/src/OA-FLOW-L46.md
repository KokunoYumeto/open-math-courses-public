# Why induction preserves every intertwiner

The converse imprimitivity theorem identifies which covariant systems arise from a closed subgroup. A stronger result identifies all maps between them: a covariant-system intertwiner acts on each induced field by one fixed subgroup intertwiner. This gives a precise equivalence of the two representation categories.

*Programme exposition written in Codex (OpenAI), September 2026; foundation integration and proof restoration by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is dedicated under CC0 to the extent of rights held. No human review is asserted.*

The earlier proofs are the full quotient, induced-field and converse chapters, [QF1](OA-FLOW-QF.md#qf-1) for compact extension, [QF6–7](OA-FLOW-QF.md#qf-6) for vector integration on the finite density measure, and [CP1–6](OA-FLOW-CP.md#oa-flow.cp.1) for the actual Hilbert-tensor concrete predual, vector series, quotients and norm closure. Square roots and positive order are CF6–8. We use this proved concrete predual directly, without requiring its identification with trace-class operators.

<a id="oa-flow.iint.setting"></a>

## Intertwiner spaces and the field map

Let $G$ be a locally compact Hausdorff group, $H\subseteq G$ closed, and $Y=G/H$. For $i=1,2$, let $K_i$ be an arbitrary Hilbert space with a strongly continuous unitary representation $V_i$ of $H$. Denote its induced Hilbert space and covariant system from lesson 44 by $(\mathcal H_i,\pi_i,U_i)$. The Hilbert inner products are linear in the first variable; $\chi=\Delta_G|_H/\Delta_H$ and $k_0$ is a quotient cutoff with $Qk_0=1$.

There are two spaces of bounded intertwiners:

<a id="equation-n1"></a>

$$ \mathcal I_H(V_1,V_2)
 =\{x\in B(K_1,K_2):xV_1(h)=V_2(h)x\ (h\in H)\}, \tag{N1} $$

<a id="equation-n2"></a>

$$ \mathcal I_G((\pi_1,U_1),(\pi_2,U_2))
 =\{T\in B(\mathcal H_1,\mathcal H_2):
 T\pi_1(F)=\pi_2(F)T,\ TU_1(s)=U_2(s)T\}. \tag{N2} $$

For $x\in\mathcal I_H(V_1,V_2)$, define pointwise

<a id="equation-n3"></a>

$$ (\Phi(x)\xi)(s)=x\xi(s). \tag{N3} $$

The $H$-covariance of $\xi$ and the intertwining relation in (N1) show that (N3) is another induced field. Its quotient norm satisfies $\|\Phi(x)\xi\|\leq\|x\|\|\xi\|$. The formula commutes with multiplication by $C_0(Y)$ and left translation, so $\Phi(x)$ belongs to (N2). We will prove that it is the only possible map and that $\|\Phi(x)\|=\|x\|$.

<a id="oa-flow.iint.smooth"></a>

## Smooth fields have genuine point values

Write $U_i(f)=\int_G f(t)U_i(t)\,dt$ for $f\in C_c(G)$, and let

<a id="equation-n4"></a>

$$ \mathscr D_i=\operatorname{span}\{U_i(f)\zeta:
                    f\in C_c(G),\ \zeta\in\mathcal H_i\}. \tag{N4} $$

This is dense by the net of group approximate identities described in lesson 45. Every member has a continuous $K_i$-valued representative. Indeed, for an induced field $\zeta$ the pointwise convolution is, almost everywhere,

<a id="equation-n5"></a>

$$ (U_i(f)\zeta)(s)
 =\int_G f(sr^{-1})\zeta(r)\Delta_G(r)^{-1}\,dr. \tag{N5} $$

For $s$ in a compact set, the integrand is supported in one compact set of $r$. The local $L^1$ estimate (I7) of lesson 44 makes (N5) finite. Uniform continuity of the scalar kernel on the relevant compact set, multiplied by the finite local integral of $\|\zeta\|$, makes it continuous in $s$, including for arbitrary parameter nets. [The full smoothing proof](OA-FLOW-L44.md#oa-flow.ind.smoothing) establishes that this representative is the actual vector integral. Its induced covariance, initially almost everywhere for each $h\in H$, therefore holds pointwise for every $s$ and each fixed $h$.

The domain is stable under all left translations. If $T$ commutes with $U_i(G)$, then $TU_i(f)\zeta=U_i(f)T\zeta$; hence every operator in $U_i(G)'$ carries $\mathscr D_i$ into itself. For an intertwiner $T$ from system 1 to system 2, the same calculation gives $T\mathscr D_1\subseteq\mathscr D_2$. These facts supply the exact point values needed below, without assigning a value to an arbitrary measurable representative.

<a id="oa-flow.iint.recovery"></a>

## A covariant map is one fiber operator

Let $T$ belong to (N2). For $\xi\in\mathscr D_1$ and nonnegative $f\in C_c(G)$, covariance of $T$ with $\pi$ gives

<a id="equation-n6"></a>

$$ m_{T\xi,T\xi}(f)
 =\langle\pi_2(Qf)T\xi,T\xi\rangle
 \leq\|T\|^2\langle\pi_1(Qf)\xi,\xi\rangle
 =\|T\|^2m_{\xi,\xi}(f). \tag{N6} $$

Here $T^*T$ commutes with $\pi_1$; the inequality follows by inserting the positive square root of $\pi_1(Qf)$. The lifted measures of the continuous fields in $\mathscr D_i$ have continuous densities $\|\xi(s)\|^2$ and $\|(T\xi)(s)\|^2$. Thus (N6), first almost everywhere and then everywhere by continuity, implies

<a id="equation-n7"></a>

$$ \|(T\xi)(s)\|\leq\|T\|\,\|\xi(s)\|
                 \qquad(s\in G). \tag{N7} $$

In particular, $\xi(e)=0$ implies $(T\xi)(e)=0$. Define $y$ on the evaluation range $\{\xi(e):\xi\in\mathscr D_1\}$ by

<a id="equation-n8"></a>

$$ y\,\xi(e)=(T\xi)(e). \tag{N8} $$

It is well defined and bounded by $\|T\|$. The range of evaluation is dense in $K_1$. To see this, the elementary fields $A(f,\eta)$ of lesson 44 have

<a id="equation-n9"></a>

$$ A(f,\eta)(e)=\int_H\chi(h)^{1/2}f(h)V_1(h)\eta\,dh. \tag{N9} $$

Choose an approximate identity on $H$ and extend each compactly supported kernel by [QF1](OA-FLOW-QF.md#qf-1) to a member of $C_c(G)$; these values approach $\eta$. Convolving each elementary field with a group approximate identity puts it in $\mathscr D_1$, and continuity of the elementary field makes its value at $e$ converge to the unsmoothed value. Hence (N8) extends uniquely to a bounded $y\in B(K_1,K_2)$ with $\|y\|\leq\|T\|$.

For a smooth induced field, pointwise covariance and left translation give

<a id="equation-n10"></a>

$$ \chi(h)^{-1/2}(U_i(h)\xi)(e)=V_i(h)\xi(e).
                                                        \tag{N10} $$

Apply (N8) to $U_1(h)\xi$ and use $TU_1(h)=U_2(h)T$. Equation (N10) yields $yV_1(h)=V_2(h)y$ on the dense evaluation range, hence on all of $K_1$. Finally, for $s\in G$,

<a id="equation-n11"></a>

$$ (T\xi)(s)=(U_2(s)^*T\xi)(e)
 =y(U_1(s)^*\xi)(e)=y\xi(s). \tag{N11} $$

Density of $\mathscr D_1$ extends (N11) to $T=\Phi(y)$ on $\mathcal H_1$. The norm bound for (N3) and $\|y\|\leq\|T\|$ give $\|\Phi(y)\|=\|y\|$. Thus $\Phi$ is an isometric bijection of the two intertwiner spaces.

<a id="oa-flow.iint.normality"></a>

## Normality, adjoints and composition

The map $\Phi$ respects adjoints and composition because those operations act pointwise:

<a id="equation-n12"></a>

$$ \Phi(x^*)=\Phi(x)^*,\qquad
 \Phi(zx)=\Phi(z)\Phi(x) \tag{N12} $$

whenever the source and target representations match. It sends identity to identity.

It is also $\sigma$-weakly continuous. For $\alpha\in\mathcal H_1$ and $\beta\in\mathcal H_2$,

<a id="equation-n13"></a>

$$ \langle\Phi(x)\alpha,\beta\rangle
   =\int_G k_0(s)\langle x\alpha(s),\beta(s)\rangle\,ds. \tag{N13} $$

To justify its predual meaning without a global separable range, first observe the scalar bound

<a id="equation-n14"></a>

$$ \int_G k_0(s)\|\alpha(s)\|\|\beta(s)\|\,ds
     \leq\|\alpha\|_{\rm ind}\|\beta\|_{\rm ind}. \tag{N14} $$

Take regular representatives as in lesson 44. Define the positive measure $\nu$ by $d\nu(s)=k_0(s)\|\alpha(s)\|\|\beta(s)\|\,ds$. It is finite by (N14) and inner regular by the complete finite-density argument in [QF7](OA-FLOW-QF.md#qf-7). There are therefore compact sets $C_n$ whose countable union carries all of $\nu$.

On each $C_n$, $\alpha,\beta$ are strongly measurable with essentially separable ranges. Since $\nu$ is absolutely continuous with respect to Haar, the normalized rank-one functional

$$ x\longmapsto
 \left\langle x\,\frac{\alpha(s)}{\|\alpha(s)\|},
                  \frac{\beta(s)}{\|\beta(s)\|}\right\rangle $$

is strongly measurable for $\nu$ in the concrete projective Hilbert-tensor predual from [CP2–4](OA-FLOW-CP.md#oa-flow.cp.2), using $K_1\oplus K_2$ and its off-diagonal corner; define it as zero when either vector vanishes. Its predual norm is at most one. A countable union of the compactwise separable ranges remains separable, and the complement has $\nu$-measure zero. Its Bochner integral against the finite measure $\nu$ exists by [QF6](OA-FLOW-QF.md#qf-6) and is a normal functional by CP3–4. By the definition of $\nu$, evaluation of that integral at $x$ is exactly (N13).

For one endomorphism algebra, CP4 writes every normal functional as a norm-convergent sum of vector functionals. Their pullbacks through the bounded map $\Phi$ converge in functional norm; each is normal by (N13), and CP6 proves that the concrete predual of the commutant is norm closed. Thus the full pullback is normal, which proves ultraweak continuity of $\Phi$. For two different representations, apply this argument to $V_1\oplus V_2$. Its induced space is $\mathcal H_1\oplus\mathcal H_2$: the pointwise component maps preserve the sum of the squared quotient norms and are onto by the field definitions. The intertwiner spaces are the corresponding off-diagonal corners of the two commutants. Their inherited ultraweak topologies are exactly the restrictions of the direct-sum vector-series tests, by CP4. Restriction therefore proves the claimed normality on the original rectangular spaces.

[Lesson 45](OA-FLOW-L45.md) proves that every nondegenerate covariant representation of $(C_0(G/H),G)$ is induced by a subgroup representation, for arbitrary locally compact $G$ and Hilbert spaces. The isometric normal bijection here shows that induction is fully faithful at the same scope. Together they give an equivalence between all strongly continuous unitary representations of $H$ and all nondegenerate covariant representations of $(C_0(G/H),G)$, with their bounded intertwiners.

**Problem.** Let $V_1=V_2=V$. Why is the commutant of the induced covariant system naturally isomorphic to $V(H)'$?

**Solution.** An operator in the commutant intertwines both $\pi$ and $U$ with themselves, so (N8)–(N11) recover a unique $y\in V(H)'$. Conversely (N3) induces every such $y$. Equations (N12)–(N14) make this an isometric normal $*$-isomorphism.

The classical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem X.4.8 and Lemma X.4.9, printed pages299–301 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The proof here uses continuous fields, the pointwise measure inequality (N6), explicit compact extensions and the concrete-predual Bochner integral. Every asserted intertwiner must preserve both the group representation and the coset multiplication action. No assertion about induction of general von Neumann dynamical systems or their crossed products is included in this result.

# Faithful normal GNS representations and their topologies

Original OA-FLOW proof candidate, written for the authorized course publisher. This file proves the exact representation result below at explicitly named earlier programme inputs. Its P514 selection status is recorded separately; a source citation does not discharge an input.

All Hilbert spaces and directed sets are arbitrary. Inner products are linear in the first variable. The zero algebra and zero Hilbert space are allowed. No faithful state, cyclic vector, separability or sigma-finiteness assumption is used.

<a id="oa-flow.wh02.1"></a>

## FLOW-WH02-01 — Exact earlier inputs

We use the following results, at precisely these scopes.

1. **[CP-06](OA-FLOW-CP.md#oa-flow.cp.6):** a concrete von Neumann algebra is the dual of its concrete Banach predual; the resulting weak-star topology is its ultraweak topology. [ST-2](OA-FLOW-ST12.md#oa-flow.st.2) proves the positive-functional seminorm comparison and corner topology directly by vector-series domination; CP-07–14 are not inputs of that comparison.
2. **[NF-6](OA-FLOW-NF.md#oa-flow.nf.6):** a positive complex-linear map between arbitrary concrete von Neumann algebras preserves bounded increasing positive suprema exactly when it is ultraweakly continuous. This is the complete earlier finite-functional/positive-map proof; it does not import an extended-valued weight characterization. Ultraweak continuity of the inverse is also supplied by the earlier ST-2 compact-ball linear criterion.
3. **[WF-2, (WF5)](OA-FLOW-WF.md#oa-flow.wf.2) and [BD, (BD7)](OA-FLOW-BD.md#oa-flow.bd.5):** bounded increasing positive nets have strong suprema and converge ultraweakly to them. Bounded strong convergence implies ultraweak convergence. Both actual earlier proofs allow arbitrary Hilbert spaces and nets.
4. **[BD-4–5](OA-FLOW-BD.md#oa-flow.bd.4):** the unit ball of a concrete C\*-algebra is strongly dense in the unit ball of its generated von Neumann algebra, on an arbitrary Hilbert space. For the possibly nonunital representation below, apply this on the identity corner. The separate bounded-net-algebra theorem 7.2 in that source section is not an input.
5. **[ST-1](OA-FLOW-ST12.md#oa-flow.st.1):** the norm ball of a Banach dual is weak-star compact. This replaces the external label OA-MOD-OPEN-CONVEX-ALAOGLU by an actual earlier programme proof. The earlier [CF Section 4](OA-FLOW-CF.md#OA-FLOW.CF.4) proves product compactness using ultrafilters; the exact source ranges and hashes are in the manifest. The proof is for arbitrary normed spaces, and its separable metrizability corollary is not used.
6. **[CF Sections 6–7](OA-FLOW-CF.md#OA-FLOW.CF.6) and [GNS Section 3](OA-FLOW-GNS.md#gns-local-units):** bounded continuous functional calculus, the C\*-identity, contractivity of \*-homomorphisms, positivity and the calculus in a possibly nonunital corner. [GW-4](OA-FLOW-GW.md#oa-flow.gw.4) proves inverse order directly, and [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1) proves the support cutoffs. These are the bounded calculus results used below, including preservation of continuous functional calculus by a \*-homomorphism.

These inputs do not include the faithful-normal-image theorem being proved here. In particular, no use is made of normality of the inverse before its domain has been shown to be a von Neumann algebra. The image-closure step uses the actual earlier compact-ball and contraction-density proofs; NF-6 supplies the full positive-map normality equivalence from the complete finite-functional argument, without an extended-valued NW premise.

<a id="oa-flow.wh02.2"></a>

## FLOW-WH02-02 — The exact representation theorem

Let $M$ be a concrete von Neumann algebra and let $\pi:M\to B(H)$ be a faithful normal \*-representation. Put $p=\pi(1)$ and $A=\pi(M)$. Then $A=pAp$ is ultraweakly closed, with identity $p$, and is a von Neumann algebra on $pH$. The map $\pi$ is an ultraweak and sigma-strong* homeomorphism onto $A$. On norm-bounded sets it also transports the concrete weak, strong and strong* operator topologies between faithful concrete realizations.

**Proof.** Since $\pi(1)$ is a self-adjoint idempotent, $p$ is an orthogonal projection. Multiplicativity gives $\pi(x)=p\pi(x)p$ for every $x$. Restrict the representation to $pH$, where it is unital. If $M=0$, faithfulness makes $A=0$ and every conclusion is immediate, so assume otherwise.

First $\pi$ is isometric. Positivity and the C\*-identity give $\|\pi(x)\|\leq\|x\|$. Suppose $b\in M_+$ and $\|\pi(b)\|<\|b\|$. Choose a continuous real function $f$ on $[0,\|b\|]$ which is zero on $[0,\|\pi(b)\|]$ and nonzero at $\|b\|$. The endpoint $\|b\|$ belongs to the spectrum of $b$, so $f(b)\neq0$. Functional calculus gives $\pi(f(b))=f(\pi(b))=0$, contrary to faithfulness. Thus norms agree on positive elements. Applying this to $x^*x$ proves

$$\|\pi(x)\|^2=\|\pi(x^*x)\|=\|x^*x\|=\|x\|^2.$$

Consequently $A$ is norm complete, hence a C\*-subalgebra of $B(pH)$, and $\pi(B_M)=B_A$ for the closed unit balls.

By [CP-06](OA-FLOW-CP.md#oa-flow.cp.6) and [ST-1](OA-FLOW-ST12.md#oa-flow.st.1), $B_M$ is ultraweakly compact. Normality of $\pi$ and [NF-6](OA-FLOW-NF.md#oa-flow.nf.6) imply ultraweak continuity into $B(pH)$. Therefore $B_A=\pi(B_M)$ is ultraweakly compact, and is closed because this topology is Hausdorff. Let $N=A''$ in $B(pH)$. The proved [BD-4](OA-FLOW-BD.md#oa-flow.bd.4) contraction density provides, for each $z\in B_N$, a net $a_i\in B_A$ converging strongly to $z$. The net is explicitly norm bounded. The [BD-5](OA-FLOW-BD.md#oa-flow.bd.5) vector-series tail estimate makes it ultraweakly convergent, so closedness of $B_A$ gives $z\in B_A$. Thus $B_N=B_A$, and scaling gives $N=A$. This proves image closure. Viewing the corner inside $B(H)$ preserves ultraweak closedness: a limit of operators $pap$ is again compressed by $p$, and the corner's ultraweak functionals are exactly the restrictions of the ambient ones.

The inverse $\rho:A\to M$ is now a positive \*-isomorphism between von Neumann algebras. It is order normal directly. Indeed, if $0\leq a_i\uparrow a$ in $A$, then $\rho(a)$ is an upper bound for $\rho(a_i)$. If $b\in M_+$ is any other upper bound, $\pi(b)$ is an upper bound for $a_i$, hence $a\leq\pi(b)$ and $\rho(a)\leq b$. This identifies the supremum as $\rho(a)$. The earlier [ST-2](OA-FLOW-ST12.md#oa-flow.st.2) compact-ball linear criterion proves ultraweak continuity of $\rho$, without an order-to-ultraweak converse for the inverse. Both directions of the asserted ultraweak homeomorphism have now been established.

For a positive normal functional $\omega$ on $M$, $\omega\circ\rho$ is a positive normal functional on $A$, and

$$
((\omega\circ\rho)(\pi(x)^*\pi(x)))^{1/2}
=\omega(x^*x)^{1/2}.
$$

Conversely every positive normal functional on $A$ pulls back along $\pi$ to one on $M$. These are exactly the sigma-strong seminorms in both algebras. Applying the same argument to $x^*$ gives both halves of the sigma-strong* topology and proves the homeomorphism without a bounded-set restriction for these intrinsic topologies.

For clarity, the passage to concrete operator topologies on bounded sets uses an actual uniform bound. If $x_i\to0$ strongly and $\|x_i\|\leq C$, a sigma-strong test represented by a square-summable vector family $(\xi_n)$ satisfies

$$
\sum_n\|x_i\xi_n\|^2
\leq \sum_{n\leq m}\|x_i\xi_n\|^2
+C^2\sum_{n>m}\|\xi_n\|^2.
$$

Choose $m$ to control the tail and then $i$ to control the finite sum. This proves sigma-strong convergence. The converse uses single-vector tests. Applying this twice proves the strong* assertion. The analogous Cauchy–Schwarz tail estimate for square-summable matrix-coefficient series proves that bounded weak convergence is ultraweak convergence; its converse uses single matrix coefficients. The ultraweak homeomorphism already proved therefore gives the bounded weak-topology assertion as well. Corner compression replaces every test vector by $p\xi$, so these conclusions include the nonunital representation. $\square$

<a id="oa-flow.wh02.3"></a>

## FLOW-WH02-03 — Application to arbitrary n.s.f. weights

Let $\varphi$ be a faithful normal semifinite weight on $M$, with GNS semicyclic map $\Lambda_\varphi:\mathfrak n_\varphi\to H_\varphi$ and left representation $\pi_\varphi$. The construction uses the finite-domain algebra and its finite-valued positive extension, proved in [GW-1–3](OA-FLOW-GW.md#oa-flow.gw.1). The normality and faithfulness conclusions can be checked directly without $\Lambda_\varphi(1)$.

For $0\leq a_i\uparrow a$ and $x\in\mathfrak n_\varphi$, all $\varphi(x^*a_i x)$ and $\varphi(x^*a x)$ are finite because they are bounded by $\|a\|\varphi(x^*x)$. Normality of the weight gives

$$
\langle\pi_\varphi(a-a_i)\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle
=\varphi(x^*a x)-\varphi(x^*a_i x)\longrightarrow0.
$$

For a positive operator $D\leq\|a\|I$, the inequality $D^2\leq\|a\|D$ gives $\|D\Lambda_\varphi(x)\|^2\leq\|a\|\langle D\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle$. Apply this to $D=\pi_\varphi(a-a_i)$. It converges strongly to zero on the dense GNS range, and its fixed uniform bound extends this to all of $H_\varphi$. Thus $\pi_\varphi$ is order normal, and [NF-6](OA-FLOW-NF.md#oa-flow.nf.6) makes it ultraweakly normal. The complete earlier [NF-5](OA-FLOW-NF.md#oa-flow.nf.5) also proves this whole-domain ultraweak continuity directly from its finite positive GNS coefficients.

Here is an explicit finite-cutoff argument for faithfulness. The finite positive cone $P=\{b\in M_+:\varphi(b)<\infty\}$ is hereditary and additive, and its complex span is ultraweakly dense by semifiniteness. Order $P$ by the operator order and set $e_b=b(1+b)^{-1}$. The set is directed since $b+c$ is an upper bound, and inverse order gives $e_b\leq e_c$ whenever $b\leq c$. Also $0\leq e_b\leq1$ and $\varphi(e_b^2)\leq\varphi(e_b)\leq\varphi(b)<\infty$.

The increasing supremum of $e_b$ is $1$. To see this, for each $b\in P$ use the subfamily $e_{tb}$, $t>0$, which converges strongly to the support projection of $b$. The join of these support projections is $1$: its complementary projection annihilates every $b\in P$, hence every element of their ultraweakly dense span, hence $1$. [WF-2, (WF5)](OA-FLOW-WF.md#oa-flow.wf.2) now gives $e_b\to1$ strongly.

If $\pi_\varphi(x)=0$, then

$$0=\|\pi_\varphi(x)\Lambda_\varphi(e_b)\|^2
=\varphi((xe_b)^*(xe_b)).$$

Faithfulness of the weight gives $xe_b=0$ for all $b$, and strong convergence of the cutoffs gives $x=0$. Therefore $\pi_\varphi$ is faithful and unital, and FLOW-WH02-02 applies with $p=I$. This is the arbitrary-weight conclusion used by the Haagerup lessons. $\square$

<a id="oa-flow.wh02.4"></a>

## FLOW-WH02-04 — Scope and publication status

This proof contains the image-closure and topology-transport arguments, rather than replacing them by a reference to a free exposition. Edward Boey's freely readable thesis [*On the Modular Theory of von Neumann Algebras*](https://uwspace.uwaterloo.ca/bitstreams/245c2a41-48ee-4c8d-ad38-95a8353dc3d1/download), Proposition 3.6, printed p.19 (PDF p.25), is comparison evidence for the GNS scope; its Theorem 3.5 on that page is stated without proof and is not a proof dependency of this note.

The compactness, density, bounded calculus and topology branches use the exact earlier CP-01–06, CF, BD and ST-1–2 proofs. The general positive-map order-to-topology equivalence now has the complete earlier NF-6 proof, and the arbitrary-weight finite ideals/GNS, cutoffs, faithfulness and normal representation use GW-1–5 and NF-5. The earlier [extended-valued normality equivalence](OA-FLOW-EW.md#ew-5) covers every weight. The earlier [finite-star closability](OA-FLOW-WR.md#wr-3), [fullness](OA-FLOW-WR.md#wr-4), [reverse correspondence](OA-FLOW-WR.md#wr-5) and [canonical opposite finite-cone](OA-FLOW-WR.md#wr-6) proofs cover faithful n.s.f. weights; none is a premise of the representation theorem proved here.
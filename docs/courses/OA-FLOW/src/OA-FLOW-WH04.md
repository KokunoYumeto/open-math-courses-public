# Full left-Hilbert-algebra domains and the unchanged closed involution

Original OA-FLOW proof candidate, written for the authorized course publisher. The mixed-product and fullness proofs below retain the complete domains on an arbitrary Hilbert space. Their precise earlier inputs and P514 selection obligations are recorded separately.

<a id="oa-flow.wh04.1"></a>

## FLOW-WH04-01 — Earlier programme statements and definitions

Let $\mathcal A\subseteq H$ be a left Hilbert algebra, let $L_a$ denote left multiplication, and put $M=L(\mathcal A)''$. Its involution is closable; write $S$ for its closure and $F=S^*$ for its conjugate-linear adjoint. We use the following earlier programme proofs.

- **[CI-1](OA-FLOW-CI.md#oa-flow.ci.1):** conjugate-linear adjoints and closure of a densely defined closable involution. In particular $S$ is a closed involution and $\mathcal A$ is a graph core; $F^*=S$.
- **[HA-R1–2](OA-FLOW-HA-R.md#oa-flow.ha-r.1):** right-bounded vectors, their injective multipliers in $M'$, invariance under $M'$, and the identity $R_{R_\alpha^*\eta}=R_\alpha^*R_\eta$ for right-bounded $\alpha,\eta$, with $R_\alpha^*\eta\in D(F)$.
- **[HA-R5–6](OA-FLOW-HA-R.md#oa-flow.ha-r.5):** the first dual algebra $\mathcal D=\mathcal B_r\cap D(F)$ is a right Hilbert algebra, its closed involution is exactly $F$, and $R(\mathcal D)''=M'$. These results apply equally to the opposite of any right Hilbert algebra. **[HA-R7](OA-FLOW-HA-R.md#oa-flow.ha-r.7):** the multipliers of that dual algebra are precisely the bounded multiplication ideal intersected with its adjoint ideal.
- **[BD-3](OA-FLOW-BD.md#oa-flow.bd.3):** a net of positive contractions in the represented involutive algebra $R(\mathcal D)$ converges strongly to $I$. The proof explicitly includes algebras that are neither norm closed nor unital, with the actual support corner and nondegeneracy accounted for.

These are actual logical premises. A bibliography entry or a public statement of RD does not replace its earlier proof. The dual-algebra theorem is not the modular commutant theorem $JMJ=M'$ and uses no modular automorphism group.

Here $\mathcal B_r$ consists of all $\eta\in H$ for which $a\mapsto L_a\eta$ is bounded in the Hilbert norm of $a\in\mathcal A$; $R_\eta$ is its bounded extension. Define $\mathcal B_l$ using the complete first dual algebra:

$$
\xi\in\mathcal B_l
\quad\Longleftrightarrow\quad
\text{the map }\eta\mapsto R_\eta\xi\text{ is bounded on }\mathcal D.
$$

Its bounded extension is $\lambda_\xi$, and the second dual algebra is

$$\mathcal C=\mathcal B_l\cap D(S).$$

Every boundedness test here is on the whole specified algebra, not a compact or analytic subalgebra.

<a id="oa-flow.wh04.2"></a>

## FLOW-WH04-02 — The second dual and its full graph domain

Apply the earlier [HA-R6–7](OA-FLOW-HA-R.md#oa-flow.ha-r.6) dual-algebra theorem to the left Hilbert algebra $\mathcal D^{\mathrm{op}}$. Its left multipliers are $R_\eta$, its generated von Neumann algebra is $M'$, its closed involution is $F$, and the adjoint of that involution is $S$. Its dual bounded-vector test is exactly the definition of $\mathcal B_l$ above. Taking the opposite product back therefore shows that $\mathcal C$ is a left Hilbert algebra, with

$$
\xi\zeta=\lambda_\xi\zeta,\qquad
\xi^\sharp=S\xi,\qquad
\lambda_{S\xi}=\lambda_\xi^*,\qquad
\lambda(\mathcal C)''=(M')'=M.
$$

Its closed involution is $S$. This application has no assumption that $\mathcal A$ was already full: the first dual $\mathcal D$ is a Hilbert algebra by its own earlier theorem.

The original algebra embeds in $\mathcal C$ with unchanged multiplication. If $a\in\mathcal A$ and $\eta\in\mathcal D$, then $R_\eta a=L_a\eta$, so $a$ passes the defining boundedness test for $\mathcal B_l$ and $\lambda_a=L_a$. Since $a\in D(S)$, it belongs to $\mathcal C$.

The graph equality can also be checked independently of the second-dual theorem's wording. We have

$$S|_{\mathcal A}\ \subseteq\ S|_{\mathcal C}\ \subseteq\ S.$$

Taking graph closures and using $\overline{S|_{\mathcal A}}=S$ yields

$$\overline{S|_{\mathcal C}}=S.$$

Thus this completion preserves the entire closed involution, its domain and its action. The algebra $\mathcal A$ is a graph core for that same operator. Nothing in this argument asserts $\mathcal A=\mathcal C$.

<a id="oa-flow.wh04.3"></a>

## FLOW-WH04-03 — Mixed products on all bounded vectors

For every $\xi\in\mathcal B_l$ and every $\eta\in\mathcal B_r$,

$$\lambda_\xi\eta=R_\eta\xi.$$

**Proof.** Choose positive contractions $e_i\in R(\mathcal D)$ with $e_i\to I$ strongly. Write $e_i=R_{\alpha_i}^*$ for $\alpha_i\in\mathcal D$: the represented algebra is self-adjoint, so such a vector exists. Put $\eta_i=e_i\eta$. [HA-R2](OA-FLOW-HA-R.md#oa-flow.ha-r.2) gives $\eta_i\in\mathcal D$, and [HA-R1](OA-FLOW-HA-R.md#oa-flow.ha-r.1) gives $R_{\eta_i}=e_iR_\eta$. It follows that $\eta_i\to\eta$ and $R_{\eta_i}\xi\to R_\eta\xi$ in Hilbert norm. By definition of $\lambda_\xi$ on $\mathcal D$,

$$\lambda_\xi\eta_i=R_{\eta_i}\xi.$$

The left side converges to $\lambda_\xi\eta$ because this operator is bounded. Passing to limits proves the asserted mixed identity. This works for every right-bounded vector, including those outside $D(F)$. $\square$

<a id="oa-flow.wh04.4"></a>

## FLOW-WH04-04 — Fullness, with no implicit domain enlargement

Let $\mathcal E$ be the right algebra obtained by dualizing $\mathcal C$. Its closed-involution adjoint domain is $D(S^*)=D(F)$.

If $\eta\in\mathcal E$, its right-boundedness inequality on $\mathcal C$ restricts to $\mathcal A\subseteq\mathcal C$, where $\lambda_a=L_a$. Thus $\eta\in\mathcal B_r$. It is already in $D(F)$, hence $\eta\in\mathcal D$.

Conversely, if $\eta\in\mathcal D$, then for $\xi\in\mathcal C$ the mixed-product identity gives

$$\|\lambda_\xi\eta\|=\|R_\eta\xi\|\leq\|R_\eta\|\,\|\xi\|.$$

This is precisely right boundedness for $\mathcal C$, and $\eta\in D(F)$ supplies the involution-domain condition. Hence $\eta\in\mathcal E$. The bounded multiplier is $R_\eta$ because the two defining maps agree on the dense algebra $\mathcal C$. The involution is $F$, and the products agree through these identical multipliers. Therefore $\mathcal E=\mathcal D$ with all its data.

Dualizing once more uses the same complete testing algebra $\mathcal D$, the same closed involution $F$, and the same adjoint $S$. It returns exactly $\mathcal C$, so $\mathcal C$ is full. This proves the double-dual assertion rather than assuming it from a terse completion statement. $\square$

<a id="oa-flow.wh04.5"></a><a id="OA-FLOW.WH04.5"></a>

The unchanged FLOW-WH04-05 weight/GNS transport scope is placed in [its later application lesson](OA-FLOW-WH04-WEIGHT.md#oa-flow.wh04.5), after the forward construction WF. It is not a premise of the general completion and mixed-product proof in Sections 2–4.

<a id="oa-flow.wh04.6"></a>

## FLOW-WH04-06 — A proper core with no state vector

Let $I$ be uncountable, put $H=\ell^2(I)$ and let $\mathcal A=c_{00}(I)$ have pointwise multiplication and complex conjugation. Its closed involution is conjugation on all of $H$: finite-support truncations converge together with their conjugates. The generated left algebra is $M=\ell^\infty(I)$ acting diagonally. Indeed, coordinate projections lie in $L(\mathcal A)$. An operator commuting with every such projection sends each basis vector to a scalar multiple of itself; boundedness bounds all these scalars by its norm, so the operator is a diagonal multiplier. All diagonal multipliers commute with each other, which computes the commutant and bicommutant. The finite-subset net of diagonal truncations of any bounded function also converges strongly to its multiplier.

Every $\eta\in H$ is right bounded since

$$\|a\eta\|_2\leq\|\eta\|_\infty\|a\|_2\leq\|\eta\|_2\|a\|_2\quad(a\in c_{00}(I)).$$

Its right multiplier is coordinate multiplication by $\eta$. Thus $\mathcal B_r=\mathcal D=H$. The same estimate for $\xi\in H$ makes it left bounded against all of $\mathcal D$, so $\mathcal B_l=\mathcal C=H$. The second dual is consequently larger than the original graph core: a vector with coordinates $1/n$ on a countably infinite subset of $I$ belongs to $\mathcal C$ and not to $c_{00}(I)$. The closed involution is nevertheless exactly unchanged.

The corresponding weight on $\ell^\infty(I)_+$ is the sum of all coordinates, interpreted as the supremum of finite sums. Additivity follows by taking a finite union of the two finite subsets used to approximate two sums. Faithfulness follows from the vanishing of each nonnegative coordinate. For a bounded increasing net, interchange the supremum over finite subsets with the supremum over the net, and then use monotone convergence of a finite sum of coordinates; this proves normality. The finite-subset projections and the finite-support bounded functions lie in the finite definition algebra, and their diagonal truncations converge strongly, hence ultraweakly on bounded sets, to every element of $M$. Thus the weight is semifinite. Its value at $1$ is infinite.

No vector in $H$ is cyclic for $M$: each square-summable vector has countable support, because for each positive integer $n$ only finitely many coordinates have magnitude at least $1/n$. Multiplication leaves that support unchanged, while an uncountable $I$ has a coordinate outside it. This example verifies that the full-domain result does not rely on a cyclic separating state vector.

<a id="oa-flow.wh04.7"></a>

## FLOW-WH04-07 — Scope and publication status

The freely readable [Boey thesis](https://uwspace.uwaterloo.ca/bitstreams/245c2a41-48ee-4c8d-ad38-95a8353dc3d1/download) contains the general dual-algebra construction in Theorem 4.5 and Lemmas 4.6–4.10, printed pp.27–31 (PDF pp.33–37), and abbreviates second-dual fullness on printed p.32 (PDF p.38). It is comparison evidence, not a substitute for the programme proofs. This note supplies the exact mixed-product and fullness argument and the closed-domain bridge in original prose.

The general Hilbert-algebra proof in Sections 2–4 now has the earlier CI/BD/HA-R proof bodies at their exact stated inputs. The [later Section 5 application](OA-FLOW-WH04-WEIGHT.md#oa-flow.wh04.5) separates the faithful n.s.f. given-weight reverse route, supplied there by the later closability, fullness and recovery proofs, from the constructed-weight direction supplied by WF. Neither later application is a premise of Sections 2–4.
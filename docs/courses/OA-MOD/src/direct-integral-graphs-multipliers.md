# Recovering algebras from measurable fibres

When can a global algebra be assembled from fibres, and when can its fibres be recovered? A scalar calculation separates measurable graphs, square-integrable graph norms and bounded multiplication. We then assemble closed graphs, construct the left and right multiplier fields, and identify the resulting algebra and its von Neumann algebra.

The countable-core arguments are part of this construction: they prove product density and measurable right-multiplier graphs. Read them at the links where those mechanisms are used. The fullness question comes after assembly; its converse needs a measurable defect relation. The analytic bridge uses Tomita algebras. Central disintegration then reverses the construction, and uniqueness separates equality over a fixed diagonal from a measurable choice of fibre isomorphisms.

Fix a **standard sigma-finite measure space** \((\Gamma,\mu)\) and a measurable field of separable complex Hilbert spaces \(H_\gamma\), allowing variable dimensions and zero fibres. Every Hilbert inner product is linear in its first argument. A measurable operator field \(B_\gamma:H_\gamma\to K_\gamma\) means that \(B_\gamma h_\gamma\) is a measurable section whenever \(h_\gamma\) is one; the field need not be uniformly bounded unless a direct-integral bounded operator is asserted. A countable fundamental sequence of measurable sections determines this property, because its fibrewise rational span is dense. A bounded field has measurable adjoint: its matrix coefficients against two countable fundamental systems are measurable, and the fibrewise Riesz vectors can be recovered by finite-dimensional projection limits. Products of such fields are measurable. Operator norm is a measurable function, being the supremum of norms on a countable fibrewise dense unit-vector system.

We use one small functional-calculus fact throughout. If \(B_\gamma=B_\gamma^*\) is a measurable contraction field, then \(f(B_\gamma)\) is measurable for every bounded Borel \(f\) on \([-1,1]\). Polynomial fields are measurable by products. Uniform polynomial approximation proves the continuous case. The bounded Borel functions preserving the assertion form a bounded monotone class: a bounded pointwise sequence gives strong convergence on every fibre by the spectral theorem, and a pointwise limit of measurable sections is measurable. Continuous functions generate the Borel sigma-algebra. The same argument works for measurable bounded positive fields on any common compact spectral interval and for continuous functions of \(B_\gamma^*B_\gamma\). This argument proves precisely the bounded functional-calculus assertion just used.

### Inputs and conventions

The Hilbert-field constructions in measurable Hilbert fields supply countable coordinates, conjugates, graph subfields, maximal integral domains, localization and the diagonal commutant. Central decomposition supplies integral commutants and bicommutants, a realization over a specified central abelian subalgebra, and equality of operator fields over a fixed diagonal. Their wider measure-space statements do not enlarge the standard base assumed here.

Countably many defining identities can share one conull set. The exceptional set for membership of an arbitrary section may depend on that section. No uncountable union of exceptional sets is taken. A measurable field of bounded fibre operators need not have an essentially bounded norm.

The single-fibre inputs are the left Hilbert-algebra axioms and closed involution, right bounded vectors and polar cutoffs, bounded strong-star approximation, full completion and its uniqueness, and the spectral domains and maximal Tomita algebra. The typed graph argument below includes conjugate fields. Hilbert projections and the spectral theorem are used with their usual closed-domain statements.

## Separate the three tests in scalar and finite fields

A fibre calculation gives three different tests before any abstract construction. Use Lebesgue measure on \((0,1)\) and the constant one-dimensional field \(H_t=\mathbb C\).

First let \(T_tz=t^{-1}z\). Every fibre operator has the whole one-dimensional domain. Its graph projection is

\[
 P_t=\frac1{1+t^2}
 \begin{pmatrix}t^2&t\\t&1\end{pmatrix}.
 \tag{DI.M1}
\]

All four entries are measurable. The graph is therefore measurable, but the constant section \(u(t)=1\) is not in the global operator domain: its image has squared integral \(\int_0^1t^{-2}\,dt=\infty\). The section \(v(t)=t\) is in that domain, with image one and squared graph norm \(1/3+1=4/3\). Thus fibre-domain membership and a measurable image still leave a global integrability test.

Now give every fibre the scalar Hilbert-algebra product and conjugation. A global algebra vector must have square-integrable vector and involution, and a uniformly essentially bounded multiplier. The three scalar quantities for a section \(x\) are

\[
 \int_0^1|x(t)|^2\,dt,\qquad
 \int_0^1|\overline{x(t)}|^2\,dt,\qquad
 \operatorname*{ess\,sup}_{0<t<1}|x(t)|.
 \tag{DI.M2}
\]

For \(x(t)=t^{-1/4}\), the first two are both two and the third is infinite. Its involution graph is square integrable, but its multiplication does not define a bounded global operator. For \(x=1\), all three are one. In this model the integral algebra is precisely \(L^\infty(0,1)\subset L^2(0,1)\).

Its full completion can also be checked directly. The closed involution is conjugation on all of \(L^2\). Right multiplication by a vector \(\eta\) is bounded exactly when \(\eta\) is essentially bounded. Sufficiency is the pointwise norm estimate. For necessity, a set on which \(|\eta|>C+\varepsilon\), if it has positive measure, has a normalized indicator whose product norm exceeds a proposed bound \(C\). Hence the right algebra and its second dual are again \(L^\infty\). No converse fullness theorem is used in this calculation.

Zero and changing dimensions give a second, finite test. On three atoms of measure one take the fibres \(0,\mathbb C,\mathbb C^2\), with coordinate multiplication on the latter two. The integral Hilbert space and algebra are \(0\oplus\mathbb C\oplus\mathbb C^2\); the closed involution is coordinate conjugation. The multiplier norm is the largest absolute coordinate. A graph-fundamental family can be zero padded across these three atoms; it never requires a unit vector in the zero fibre. This is the model for the dimension strata used below.

The construction now asks how to recognize a measurable graph, how to assemble its integrable sections, and how to retain bounded multiplication. The inverse problem at the end asks which part of an assembled algebra determines its fibres.

### Specify the algebra field before assembling it

A field \(\gamma\mapsto\mathcal A_\gamma\subset H_\gamma\) of left Hilbert algebras is **measurable** when there are countably many measurable sections \(a_j(\gamma)\) such that, almost everywhere:

1. \(a_j(\gamma)\in\mathcal A_\gamma\), and the family is fundamental in \(H_\gamma\);
2. every \(a_j(\gamma)^\sharp\) is measurable;
3. the set \(\{a_j(\gamma):j\geq1\}\) is dense in \(\mathcal A_\gamma\) for the graph norm \(\|x\|_\sharp^2=\|x\|^2+\|x^\sharp\|^2\);
4. every product \(a_j(\gamma)a_k(\gamma)\) is measurable.

The sequence is called a measurable fundamental algebra family. A measurable field of right Hilbert algebras is defined by the handed analogue. The graph-density clause is stronger than Hilbert density and will be used whenever the closed involution is integrated. The source requires density of the set itself. A family whose linear span is graph dense can be enlarged by enumerating all finite \(\mathbb Q(i)\)-linear combinations, including zero. Approximating the finitely many complex coefficients also approximates the involution coordinates, so the enlarged set is graph dense. Involution and product measurability persist by finite sums. Thus this enlargement reconciles the two formulations without assuming measurable membership for the entire original algebra. This is a definition, so it supplies no theorem-proof credit.

## Recognize a measurable closed graph

The first test is a property of the graph, independent of global square integrability. The projection, bounded resolvent and polar operator give equivalent ways to recognize it.

Let \(T_\gamma\) be densely defined closed linear operators on \(H_\gamma\). Write \(G_\gamma=\{(x,T_\gamma x):x\in D(T_\gamma)\}\subset H_\gamma\oplus H_\gamma\). The following are equivalent.

1. There is a countable measurable family \(u_j(\gamma)\in D(T_\gamma)\), graph-norm dense in each domain almost everywhere, with both \(u_j\) and \(T_\gamma u_j\) measurable; moreover, any measurable section \(u(\gamma)\in D(T_\gamma)\) has measurable image \(T_\gamma u(\gamma)\).
2. The closed-subspace field \(G_\gamma\) is measurable, equivalently its orthogonal-projection field \(P_\gamma\) is measurable.
3. In \(T_\gamma=U_\gamma |T_\gamma|\), both the polar partial-isometry field \(U_\gamma\) and the positive-contraction field \(C_\gamma=(1+|T_\gamma|)^{-1}\) are measurable.

**Proof.** For 1 to 2, the pairs \((u_j,T_\gamma u_j)\) are measurable and dense in \(G_\gamma\). Fibrewise Gram–Schmidt, keeping zero outputs at dependent steps, produces a measurable orthonormal fundamental system \(g_j(\gamma)\) for \(G_\gamma\). For any measurable \(w(\gamma)\in H_\gamma\oplus H_\gamma\), the partial sums \(\sum_{j\leq n}\langle w,g_j\rangle g_j\) are measurable and converge fibrewise to \(P_\gamma w\). This proves measurability of \(P_\gamma\). Variable fibre dimensions cause no difficulty: the zero-padded Gram–Schmidt sequence changes rank measurably, and no literal identification of every \(H_\gamma\) with one fixed Hilbert space is made.

For 2 to 3 put \(R_\gamma=(1+T_\gamma^*T_\gamma)^{-1}\) and \(B_\gamma=T_\gamma R_\gamma\). Projection onto a graph, checked on pairs in the graph and its orthogonal complement and then extended as bounded blocks, has the form

\[
 P_\gamma=
 \begin{pmatrix}
 R_\gamma&B_\gamma^*\\
 B_\gamma&U_\gamma(1-R_\gamma)U_\gamma^*
 \end{pmatrix}. \tag{DI.1}
\]

Thus \(R_\gamma\) and \(B_\gamma\) are measurable bounded fields. The continuous function \(h(0)=0\) and

\[
 h(r)=\bigl(1+\sqrt{r^{-1}-1}\bigr)^{-1}\quad (0<r\leq1)
\]

satisfies \(h(R_\gamma)=C_\gamma\), including the spectral-limit point \(r=0\). Also \(B_\gamma=U_\gamma |T_\gamma|(1+|T_\gamma|^2)^{-1}\). Its positive factor vanishes exactly on \(\ker T_\gamma\), so its polar partial isometry is \(U_\gamma\). The bounded fields

\[
 B_\gamma(B_\gamma^*B_\gamma+\varepsilon)^{-1/2}
\]

are measurable by continuous functional calculus and converge strongly on every fibre to \(U_\gamma\) as \(\varepsilon\downarrow0\). Hence \(U_\gamma\) is measurable.

For 3 to 2 define on \([0,1]\)

\[
 k(c)=\frac{c^2}{c^2+(1-c)^2},\qquad
 b(c)=\frac{c(1-c)}{c^2+(1-c)^2}.
 \tag{DI.2}
\]

The denominators never vanish. Spectral calculus gives \(R_\gamma=k(C_\gamma)\) and \(B_\gamma=U_\gamma b(C_\gamma)\). Each block in (DI.1) is therefore measurable, proving graph measurability.

It remains to recover the image clause in 1 from 2. Applying \(P_\gamma\) to a fundamental sequence of \(H_\gamma\oplus H_\gamma\) supplies countably many measurable graph sections dense in \(G_\gamma\). Their first coordinates are graph-norm fundamental. For an arbitrary measurable \(u(\gamma)\in D(T_\gamma)\), set

\[
 T_{\gamma,n}=T_\gamma(1+n^{-1}T_\gamma^*T_\gamma)^{-1}
             =U_\gamma f_n(C_\gamma),\quad
 f_n(c)=\frac{n c(1-c)}{n c^2+(1-c)^2}. \tag{DI.3}
\]

Each \(f_n\) is continuous on \([0,1]\) and \(T_{\gamma,n}\) is a measurable bounded field. On \(D(T_\gamma)\), spectral dominated convergence yields \(T_{\gamma,n}u(\gamma)\to T_\gamma u(\gamma)\) fibrewise. The limit is measurable. This completes the equivalence. \(\square\)

The proof also works for densely defined closed operators \(T_\gamma:H_\gamma\to K_\gamma\) between two measurable Hilbert fields. Here \(G_\gamma\subset H_\gamma\oplus K_\gamma\); in (DI.1), \(R\) acts on \(H\), \(B:H\to K\), \(B^*:K\to H\), and \(U(1-R)U^*\) acts on \(K\). Fibrewise graph projection, the bounded functions in (DI.2)–(DI.3), and the polar strong limit have the same proofs in these typed spaces. This extension is used in DI-03 below.

## Assemble a closed operator with its exact domain

The scalar section with a nonintegrable image explains the domain in the next formula. Both coordinates of a graph must be square integrable. Proving closedness and the adjoint identity then uses actual graph assembly.

Assume the equivalent DI-01 conditions. Let \(H=\int^\oplus_\Gamma H_\gamma\,d\mu\). Define

\[
 D(T)=\left\{u\in H:\ u(\gamma)\in D(T_\gamma)\ {\rm a.e.},\
 \int_\Gamma\|T_\gamma u(\gamma)\|^2\,d\mu<\infty\right\},
 \qquad (Tu)(\gamma)=T_\gamma u(\gamma). \tag{DI.4}
\]

Then \(T\) is densely defined and closed, and

\[
 G(T)=\int_\Gamma^\oplus G_\gamma\,d\mu\quad\text{inside }H\oplus H. \tag{DI.5}
\]

**Proof.** The image in (DI.4) is measurable by DI-01 and square-integrable by hypothesis. Equation (DI.5) follows in both directions directly from the two-coordinate definition of the Hilbert direct integral: a square-integrable section of \(G_\gamma\) has exactly the fibre-domain relation and integrability in (DI.4).

For density, choose a finite-measure exhaustion \(E_k\uparrow\Gamma\) and the countable graph-norm fundamental fields \(u_j,T_\gamma u_j\) from DI-01. For each \(j,k,m\), truncate \(u_j\) to

\[
 E_k\cap\{\|u_j(\gamma)\|^2+\|T_\gamma u_j(\gamma)\|^2\leq m\}.
\]

The truncated section belongs to \(D(T)\). Multiplying it by arbitrary bounded measurable functions with finite-measure support keeps it in \(D(T)\). If \(v\in H\) is orthogonal to all these sections, localization says \(\langle v(\gamma),u_j(\gamma)\rangle=0\) almost everywhere for every \(j\). The \(u_j(\gamma)\) are dense in \(D(T_\gamma)\) for the graph norm and hence dense in \(H_\gamma\), so \(v=0\).

For closedness, suppose \((u_n,Tu_n)\to(u,v)\) in \(H\oplus H\). Extract a subsequence whose pairwise \(L^2\) errors to \((u,v)\) have summable squares. The corresponding fibre pairs converge almost everywhere. Since every \(G_\gamma\) is closed, \((u(\gamma),v(\gamma))\in G_\gamma\) almost everywhere. Equation (DI.5) then gives \(u\in D(T)\), \(Tu=v\). \(\square\)

A useful strengthening follows from the graph geometry: \(T^*=\int^\oplus T_\gamma^*\,d\mu\). Indeed the graph projection in DI-01 is decomposable, so its orthogonal complement is the integral of \(G_\gamma^\perp\). The fixed unitary \(K(x,y)=(y,-x)\) sends \(G(T)^\perp\) to \(G(T^*)\), and the same fibrewise identity gives the asserted graph equality. The two-coordinate graph identity records the exact \(L^2\) domain condition. The graph/domain/density/closedness argument also applies, with the same two-coordinate proof, to operators \(C_\gamma:\overline H_\gamma\to H_\gamma\) between different measurable fields; after composition with the canonical conjugations, it supplies the closed antilinear integral of \(S_\gamma\) used in DI-05. No uniform bound on \(\|T_\gamma\|\) is asserted.

## Recover the involution and modular operators from the graph

For the algebra involution the graph is real linear, with a conjugate-linear first-coordinate map. Passing through the conjugate Hilbert field keeps the polar factors correctly typed.

Let \(\mathcal A_\gamma\subset H_\gamma\) be a measurable field of left Hilbert algebras in the **full four-clause sense of VI.3.1**. In particular the chosen countable fundamental algebra fields \(a_j(\gamma)\) are graph-norm dense for the closure \(S_\gamma\) of the fibre involution, and \(a_j(\gamma)^\sharp\) is measurable. Then \(J_\gamma a_j(\gamma)\) is measurable for every \(j\), where \(S_\gamma=J_\gamma\Delta_\gamma^{1/2}\).

**Proof.** For each fibre form the conjugate Hilbert space \(\overline H_\gamma\). Its fundamental sections are \(\overline{h_j(\gamma)}\), so it is a measurable field. The conjugate-linear \(S_\gamma\) becomes a complex-linear closed operator

\[
 C_\gamma:\overline H_\gamma\longrightarrow H_\gamma,\qquad
 C_\gamma(\overline x)=S_\gamma x.
\]

The pairs \((\overline{a_j(\gamma)},a_j(\gamma)^\sharp)\) are measurable and graph-norm fundamental for \(C_\gamma\). The between-fields form of DI-01 makes the polar partial isometry \(W_\gamma:\overline H_\gamma\to H_\gamma\) and \(Q_\gamma=(1+|C_\gamma|)^{-1}\) measurable. On the algebra core, \((x,S_\gamma x)\) is accompanied by \((S_\gamma x,x)\) because sharp is involutive. Swapping coordinates is continuous, so closure of this graph preserves the swap. Consequently \(S_\gamma^2x=x\) on \(D(S_\gamma)\): the kernel is zero and the range equals the dense domain. Thus \(W_\gamma\) is unitary. Composing \(W_\gamma\) with the canonical antiunitary \(\kappa_\gamma:x\mapsto\overline x\) yields the polar antiunitary \(J_\gamma\). Therefore \(J_\gamma a_j(\gamma)=W_\gamma\overline{a_j(\gamma)}\) is measurable. Moreover \(k(Q_\gamma)=(1+|C_\gamma|^2)^{-1}\), with \(k\) from (DI.2); the polar part of \(|C_\gamma|^2=C_\gamma^*C_\gamma\) is the measurable identity on \(\overline H_\gamma\), since its kernel is zero. The between-fields resolvent/polar criterion DI-01 therefore makes \(C_\gamma^*C_\gamma\) a measurable closed-operator field. Conjugate transport gives the fibre modular operator \(\Delta_\gamma=\kappa_\gamma^{-1}(C_\gamma^*C_\gamma)\kappa_\gamma\) as a measurable closed-operator field on \(H_\gamma\). \(\square\)

This argument explicitly handles conjugate-linearity; it does not treat the graph of \(S_\gamma\) as a complex-linear subspace of \(H_\gamma\oplus H_\gamma\).

## Make each left multiplier measurable

Measurability of multiplication is the next separate test. Countable products determine each bounded fibre multiplier; they supply no global norm bound.

Let \(\xi(\gamma)\in\mathcal A_\gamma\) be any Hilbert-measurable section under the full VI.3.1 hypotheses. The operator field \(\pi_\gamma(\xi(\gamma))\) is measurable, even though its fibrewise bounded norms need not have a common essential bound.

**Proof.** Work on one conull set for all the countably many fundamental identities. For each fixed fundamental section \(a_j\), the bounded left multiplier \(\pi_\gamma(a_j)\) sends every fundamental \(a_k\) to the measurable section \(a_j a_k\) by VI.3.1(iv). It is therefore a measurable bounded-operator field. The measurable-adjoint lemma above and the left Hilbert-algebra adjoint identity give a measurable field

\[
 \pi_\gamma(a_j)^*=\pi_\gamma(a_j^\sharp).
\]

The graph-image clause of DI-01, applied through the conjugate-field linearization of DI-03, makes \(\xi^\sharp=S_\gamma\xi\) measurable. Hence \(\eta_j=a_j^\sharp\xi^\sharp=\pi_\gamma(a_j)^*\xi^\sharp\) is a measurable algebra section. A second application of the same graph-image clause makes

\[
 S_\gamma\eta_j=(a_j^\sharp\xi^\sharp)^\sharp=\xi a_j
\]

measurable. Thus \(\pi_\gamma(\xi)a_j\) is measurable for every fundamental \(a_j\). Because each \(\pi_\gamma(\xi)\) is bounded on its own fibre, testing on the countable fundamental system proves measurability of the whole operator field. No essential uniform norm bound is used. \(\square\)

## Construct the opposite field with a genuine multiplier core

Before taking a polar cutoff of a closed right multiplier, prove that its proposed countable pairs really are a graph core. The countable multiplier-core proof uses bounded strong-star approximation. Its worked example shows why involution graph density alone fails. Only then are the cutoffs below justified.

Let \(\mathcal A_{r,\gamma}\) be the associated right Hilbert algebra of \(\mathcal A_\gamma\), with closed right involution \(F_\gamma=S_\gamma^*\). Then \(\gamma\mapsto\mathcal A_{r,\gamma}\) is a measurable field of right Hilbert algebras.

**Proof using the closed multiplier core in Keep a closed multiplier domain under approximation.** DI-03 makes \(\Delta_\gamma\), \(J_\gamma\), and every bounded Borel function of the modular operator measurable. Hence

\[
 F_\gamma=J_\gamma\Delta_\gamma^{-1/2} \tag{DI.6}
\]

is a measurable closed-operator field by DI-01. Choose a countable measurable graph-fundamental family \(\eta_j(\gamma)\in D(F_\gamma)\).

For each \(j\), let \(T_{j,\gamma}\) be the closed right multiplier obtained by closing

\[
 a\longmapsto L_a\eta_j(\gamma),\qquad a\in\mathcal A_\gamma.
\]

Its existence, affiliation, and adjoint restriction are the single-fibre statements RD-01–03. The explicit countable core in SCF-03, using the bounded strong-star approximation of HAP-06, makes \(\{T_{j,\gamma}\}_\gamma\) a measurable closed-operator field. Write
\(T_{j,\gamma}=u_{j,\gamma}h_{j,\gamma}=k_{j,\gamma}u_{j,\gamma}\).
DI-01 makes the polar fields and their bounded spectral functions measurable.

Choose nonnegative \(f_m\in C_c(0,\infty)\), extended by zero at the origin, with \(f_m(t)\uparrow1\) for \(t>0\). RD-03–04 gives

\[
 \theta_{j,m}(\gamma):=f_m(k_{j,\gamma})\eta_j(\gamma)
      \in\mathcal A_{r,\gamma}^{\,2},
 \qquad
 F_\gamma\theta_{j,m}(\gamma)
      =f_m(h_{j,\gamma})F_\gamma\eta_j(\gamma), \tag{DI.7}
\]

and both terms converge respectively to \(\eta_j(\gamma)\) and
\(F_\gamma\eta_j(\gamma)\). Every displayed field is measurable. Thus the
\(\theta_{j,m}\), enumerated over \((j,m)\), are graph-fundamental for
\(F_\gamma\) and Hilbert-fundamental in \(H_\gamma\).

RD-03 also gives the bounded right multiplier explicitly:

\[
 R_{\theta_{j,m}(\gamma)}
   =k_{j,\gamma}f_m(k_{j,\gamma})u_{j,\gamma}.
\]

It is a measurable bounded-operator field. Hence every pairwise right product
\(\theta_{j,m}\theta_{k,n}
 =R_{\theta_{k,n}}\theta_{j,m}\) is measurable, while (DI.7) makes every right involution measurable. Enlarge this countable family by all finite \(\mathbb Q(i)\)-linear combinations and zero. Its set is dense for the right graph norm; the involution, right multiplier and pairwise product fields remain measurable by finite sums. The four handed conditions of DI-00 now hold, so the associated right algebras form a measurable field. \(\square\)

## Require vector, involution and multiplier bounds together

Return to the scalar example: its integrable involution graph passed two tests and failed the multiplier bound. The definition therefore retains three conditions, including membership in the original fibre algebra.

For a measurable left Hilbert-algebra field define

\[
 \mathcal A=\int_\Gamma^\oplus\mathcal A_\gamma\,d\mu
 :=\left\{x\in\int_\Gamma^\oplus H_\gamma\,d\mu:
 \begin{array}{l}
 x(\gamma)\in\mathcal A_\gamma\ \text{a.e.},\\
 \displaystyle\int_\Gamma\|x(\gamma)^\sharp\|^2\,d\mu<\infty,\\
 \displaystyle\mathop{\rm ess\,sup}_\gamma\|L_{x(\gamma)}\|<\infty
 \end{array}\right\}. \tag{DI.8}
\]

Membership in the ambient Hilbert direct integral already includes \(\int\|x(\gamma)\|^2d\mu<\infty\). The right-algebra integral is defined with the handed conditions. Omitting either the involution integral or the essential multiplier bound changes the object and is not allowed.

## Assemble the Hilbert algebra and identify its right dual

Two density arguments are needed. Involution graph density identifies the closed global involution; product density identifies a Hilbert algebra. For the second, form the countable rational star algebra and prove its products dense by pairing with the opposite algebra. The complete product proof does this before approximation is invoked. Enumerating factor pairs and bounding their six norms gives the actual localized products used below, as proved in the localization argument. No selector outside the original algebra enters either step.

The space \(\mathcal A\) in (DI.8), with fibrewise multiplication and involution, is a left Hilbert algebra whose Hilbert completion is \(H=\int^\oplus H_\gamma\,d\mu\). Its associated right Hilbert algebra is exactly

\[
 \mathcal A_r=\int_\Gamma^\oplus\mathcal A_{r,\gamma}\,d\mu. \tag{DI.9}
\]

**Proof of the left Hilbert-algebra assertions.** DI-04 makes all relevant products measurable. If \(x,y\in\mathcal A\), then fibrewise

\[
 \|xy\|_H\leq\|L_x\|_{\infty}\|y\|_H,
 \quad
 \|(xy)^\sharp\|_H=\|y^\sharp x^\sharp\|_H
 \leq\|L_y\|_{\infty}\|x^\sharp\|_H,
 \quad
 \|L_{xy}\|_{\infty}\leq\|L_x\|_{\infty}\|L_y\|_{\infty}. \tag{DI.10}
\]

Thus \(\mathcal A\) is an involutive algebra and every left multiplication is bounded. Integrating the fibre adjoint identity gives \(L_x^*=L_{x^\sharp}\). The involution is preclosed because it is the restriction of the closed antilinear direct integral \(S=\int^\oplus S_\gamma\,d\mu\) supplied by DI-02.

Its closure is exactly this \(S\), a fact needed before identifying the associated right involution. Localize each fundamental \(a_j\) on a finite-measure exhaustion and on level sets bounding \(\|a_j\|\), \(\|a_j^\sharp\|\), and \(\|L_{a_j}\|\). Each resulting section belongs to \(\mathcal A\). Linearize the involution as in DI-03, so its graph lies in \(\overline H\oplus H\) and has fibrewise fundamental pairs \((\overline{a_j},a_j^\sharp)\). Multiplying an algebra section by a bounded scalar function \(f\) multiplies both coordinates of its linearized graph pair by \(\overline f\). The localization and orthogonality argument of DI-02 therefore shows that these algebra graph pairs span a dense subspace of the integrated closed graph. Hence \(\mathcal A\) is a graph core for \(S\). The adjoint graph identity in DI-02, transported through conjugate fields, now gives the exact global right involution \(F=S^*=\int^\oplus F_\gamma\,d\mu\), including its square-integrability domain.

For product density, use the explicit rational-core product family in Localize explicit products and operator generators to choose measurable pairs
\(u_j(\gamma),v_j(\gamma)\in\mathcal A_\gamma\) whose products are fibrewise fundamental. Intersect a finite-measure exhaustion with level sets on which

\[
 \|u_j\|,\ \|u_j^\sharp\|,\ \|L_{u_j}\|,
 \ \|v_j\|,\ \|v_j^\sharp\|,\ \|L_{v_j}\| \tag{DI.11}
\]

are bounded. Both localized factors lie in \(\mathcal A\), and their product is the corresponding localization of \(u_jv_j\). If a vector in \(H\) is orthogonal to all these products, further scalar localization makes it fibrewise orthogonal to the chosen fundamental product family. It is zero. Hence \(\mathcal A^2\) is dense, and \(\mathcal A\) is a left Hilbert algebra with completion \(H\).

**Proof of (DI.9).** Let \(\mathcal B\) denote the right side. For \(\eta\in\mathcal B\), the direct integral of the fibre right multipliers is bounded, and DI-02 applied to \(F_\gamma\) gives the global right involution. Therefore \(\eta\) is right bounded for \(\mathcal A\) and belongs to \(D(F)\), so \(\mathcal B\subseteq\mathcal A_r\).

Conversely take \(\eta\in\mathcal A_r\), and write its bounded global right multiplier as \(R_\eta\). DI-02 gives

\[
 \eta(\gamma)\in D(F_\gamma),\qquad
 (F\eta)(\gamma)=F_\gamma\eta(\gamma)
 \quad\text{a.e.} \tag{DI.12}
\]

For every measurable \(E\), the diagonal projection \(q_E\) preserves \(\mathcal A\), and on the dense domain \(\mathcal A\)

\[
 R_\eta q_Ea=L_{q_Ea}\eta=q_E L_a\eta=q_E R_\eta a.
\]

Thus \(R_\eta\) commutes with the diagonal algebra. OA-MOD-DI-DEP-FIELD supplies a decomposable field
\(R_\eta=\int^\oplus R_\gamma\,d\mu\) with

\[
 \|R_\gamma\|\leq\|R_\eta\|\quad\text{a.e.} \tag{DI.13}
\]

Localizing the countable fundamental algebra sections and comparing fibres in
\(R_\eta a=L_a\eta\) gives
\(R_\gamma a_j(\gamma)=L_{a_j(\gamma)}\eta(\gamma)\) off one null set. To extend this identity to every \(a\in\mathcal A_\gamma\), use graph density: choose \(a_n\) in the linear span of the fundamental family with \(a_n\to a\) and \(a_n^\sharp\to a^\sharp\). For every \(b\in\mathcal A_{r,\gamma}\), its bounded right multiplier and the adjoint pairing give

\[
 \langle R_\gamma a_n,b\rangle
 =\langle L_{a_n}\eta(\gamma),b\rangle
 =\langle\eta(\gamma),R_ba_n^\sharp\rangle
 \longrightarrow\langle\eta(\gamma),R_ba^\sharp\rangle
 =\langle L_a\eta(\gamma),b\rangle.
\]

The left side also converges to \(\langle R_\gamma a,b\rangle\). Density of \(\mathcal A_{r,\gamma}\) identifies the two vectors, so \(L_a\eta(\gamma)=R_\gamma a\) on the entire fibre algebra. Thus \(\eta(\gamma)\) is right bounded and \(R_\gamma=R_{\eta(\gamma)}\). Together with (DI.12) and (DI.13), this is exactly membership in \(\mathcal B\). Hence \(\mathcal A_r=\mathcal B\). \(\square\)

## Recover the von Neumann algebra from localized generators

The same localized countable generators determine more than product density. Their supports recover the diagonal algebra, after which the integral commutant and bicommutant identify the full von Neumann algebra. This step uses the already proved rational-core and localization mechanisms, rather than an unproved generator-selection assertion.

Write \(M_\gamma=L(\mathcal A_\gamma)''\) and \(M=L(\mathcal A)''\). Then \(\gamma\mapsto M_\gamma\) is a measurable von Neumann-algebra field and

\[
 M=\int_\Gamma^\oplus M_\gamma\,d\mu. \tag{DI.15}
\]

**Proof using CENTRAL and Prove product density before completing the core through Localize explicit products and operator generators.** SCF-02 and SCF-04 supply a countable measurable algebra family \(d_j(\gamma)\) whose left multipliers generate \(M_\gamma\). DI-04 makes those multiplier fields measurable. Finite-measure and norm localization turns them into a countable family of global sections of \(\mathcal A\), without changing the generated fibre algebra on the increasing localization sets.

For a measurable set \(E\), repeat the product-density localization from DI-07 with all products supported in \(E\). Their span is dense in \(q_EH\), and every such product has the form \(L_x y\) with \(x\in\mathcal A\) supported in \(E\). Therefore

\[
 q_E=\bigvee_{x\in\mathcal A,\ \operatorname{supp}x\subseteq E}
       s(L_xL_x^*).
\]

Every support projection on the right belongs to \(M\), so \(q_E\in M\). Thus \(M\) contains the diagonal algebra.

Every \(L_x\) is decomposable with fibre \(L_{x(\gamma)}\), giving
\(M\subseteq\int^\oplus M_\gamma\,d\mu\). Conversely the localized generator family lies in \(M\), contains the diagonal projections, and generates \(M_\gamma\) almost everywhere. The decomposable-commutant and bicommutant clauses of OA-MOD-DI-DEP-CENTRAL therefore identify its global bicommutant with
\(\int^\oplus M_\gamma\,d\mu\). This gives the reverse inclusion, proves measurability of the fibre algebra field, and establishes (DI.15). \(\square\)

## Determine when fullness can be recovered from fibres

Full fibres always give a full integral. Recovering fullness of original fibres from a full integral is a different question: it requires selecting a vector outside the original algebra. Read the full-completion membership code, the qualified defect selection, and the adjacent constant-graph obstruction with this theorem. The latter shows exactly why graph data do not code all original algebra membership. The CH investigation is separately labelled and is no premise of this theorem.

If the fibres are full almost everywhere, their integral algebra is full. The converse holds with the additional hypothesis that the proper-original-algebra defect relation is analytic in the standard Borel fibre coordinates. Borel membership of the original algebra is sufficient for this hypothesis.

**The source statement.** Takesaki II, VI.3 Corollary 3.9, printed p. 33 / PDF p. 53, states the equivalence without this additional hypothesis. The countable-family definition VI.3.1 does not give analytic original algebra membership. Test the hypothesis with constant graph data gives an unconditional obstruction to defect coding. Investigate the stronger failure under CH gives a counterexample to the literal converse under the explicitly stated Continuum Hypothesis: every fibre is proper, while the integral is full. The latter is a conditional counterexample; CH is used nowhere in the corrected theorem below.

**Proof of the unconditional implication.** Apply DI-05 and DI-07 twice:

\[
 \mathcal A_{rr}
   =\int_\Gamma^\oplus(\mathcal A_\gamma)_{rr}\,d\mu. \tag{DI.14}
\]

If the fibres are full almost everywhere, the right side equals the algebra defined in (DI.8), so the integral is full.

**Proof of the qualified converse.** Code exactly the full completion proves that membership in the canonical full completion and its actual involution and left-multiplier data have Borel codes. Write

\[
 \mathscr D=\{(\gamma,\xi):\xi\in(\mathcal A_\gamma)_{rr}
                              \setminus\mathcal A_\gamma\}.
\]

Assume that this relation is analytic. Its projection is measurable after measure completion by SCF-05. If the fibres are nonfull on a set of positive measure, SCF-05 gives a completed measurable section in this defect relation. Its vector, involution and multiplier norm functions are measurable by SCF-07. A finite-measure exhaustion and countably many norm levels therefore give a positive finite-measure set on which all three norms are bounded. Extending the localized section by zero produces an element of the right side of (DI.14). If the integral were full, it would belong to \(\mathcal A\); (DI.8) would then require original fibre membership almost everywhere on that support, contradicting the selected defect. Thus the fibres are full almost everywhere. This is precisely the proof in Select a proper defect under its actual hypothesis. \(\square\)

The corrected proof does not prove the printed unrestricted converse. The CH example also explains why the exceptional set for a section’s original-algebra membership cannot be made uniform over all measurable sections.

## Specify all integer-power conditions for a Tomita integral

The analytic bridge retains every positive and negative integer power, with all three integral-algebra conditions at each power. Finite fibre calculations with a trivial modular operator cannot remove those global requirements.

A field \(\gamma\mapsto\mathcal T_\gamma\) of Tomita algebras is measurable when it is measurable as a left Hilbert-algebra field. Let \(\mathcal A=\int^\oplus\mathcal T_\gamma d\mu\) be its left Hilbert-algebra integral and \(\Delta=\int^\oplus\Delta_\gamma d\mu\). Its **Tomita direct integral** is

\[
 \mathcal T=\left\{x\in\mathcal A:
 x\in D(\Delta^n)\ \text{and}\ \Delta^n x\in\mathcal A
 \text{ for every }n\in\mathbb Z\right\}. \tag{DI.16}
\]

Thus every positive and negative integer power must again satisfy all three conditions in (DI.8), including the essential multiplier bound. Pointwise domain membership alone is insufficient.

## Keep complex powers, products and graph cores in the integral

Integer powers must also control complex powers and multiplication. The proof uses three independent norm controls and localizes a countable list of them on one increasing conull exhaustion. It proves product density as well as involution graph density.

The algebra \(\mathcal T\) in (DI.16) is a Tomita algebra and is graph-dense in \(\mathcal A\) for the closed involution. Consequently the two left Hilbert algebras are equivalent.

**Proof of complex-power invariance.** Let \(\mathcal A^{\mathrm{full}}=\mathcal A_{rr}\) be the full left completion. By Mixed bounded vectors and fullness, it has the same closed involution \(S\) and modular operator \(\Delta\) as \(\mathcal A\). Its left multiplier for an element of \(\mathcal A\) is the same bounded operator on \(H\). If \(x\in\mathcal T\), all integer powers \(\Delta^m x\) belong to \(\mathcal A\subseteq\mathcal A^{\mathrm{full}}\). Thus The maximal entire algebra puts \(x\) in the maximal entire algebra of this full completion. Write \(U_z=\Delta^{iz}\). This proves global norm-entire vector and multiplier orbits, but membership in the original fibre algebras still has to be checked.

Fix \(m\in\mathbb Z\), \(z\in\mathbb C\), and an integer \(n\) with \(a=-\operatorname{Im}z\in[n,n+1]\). The multiplier estimate (MF.35) and spectral interpolation give

\[
\begin{aligned}
\|U_z\Delta^m x\|
 &\leq\max_{j\in\{n,n+1\}}\|\Delta^{m+j}x\|,\\
\|S U_z\Delta^m x\|
 &\leq\max_{j\in\{n,n+1\}}\|S\Delta^{m+j}x\|,\\
\|L_{U_z\Delta^m x}\|
 &\leq\max_{j\in\{n,n+1\}}\|L_{\Delta^{m+j}x}\|.
\end{aligned}
\]

For the vector bound, put \(\theta=a-n\); the scalar inequality \(s^{2a}\leq(1-\theta)s^{2n}+\theta s^{2n+2}\), integrated against the spectral measure of \(\Delta^m x\), proves the claim. For the involution bound use \(S U_z=U_{\overline z}S\) and \(S\Delta^k x=\Delta^{-k}Sx\), then interpolate between the two reflected endpoint powers of \(Sx\). All these domains follow from the integer memberships and Unbounded measurable functions. The estimates are uniform when the real part of \(z\) varies in the chosen horizontal strip.

The modular operator and its bounded spectral cutoffs act fibrewise by DI-02, DI-03 and DI-07. Approximating \(s^{m+iz}\) by its bounded cutoffs on \([1/k,k]\), and using the exact closed-operator domain in DI-02, therefore identifies

\[
(U_z\Delta^m x)(\gamma)
 =\Delta_\gamma^{iz}\Delta_\gamma^m x(\gamma)
 \quad\text{almost everywhere}.
\]

The abstract automorphisms of each fibre Tomita algebra are exactly its modular powers by Recovering the modular powers from abstract analyticity. Hence this vector belongs to the original \(\mathcal T_\gamma\). Applying the same three estimates in each fibre gives square-integrable vector and involution sections, since both endpoint powers already belong to the integral \(\mathcal A\). DI-04 makes their multiplier field measurable, and its norm is bounded essentially by the maximum of the two endpoint essential bounds. These are all the conditions in (DI.8). Consequently \(U_z\Delta^m x\in\mathcal A\) for every integer \(m\), so \(U_z x\in\mathcal T\). For fixed \(x,z\), the countably many integer-power assertions hold on a common conull set; no uniform null set over all vectors and parameters is required.

Products and involution are computed fibrewise. The rules \(\Delta^n(xy)=(\Delta^n x)(\Delta^n y)\) and \(\Delta^n(x^\sharp)=(\Delta^{-n}x)^\sharp\), together with the product and involution bounds of DI-07, keep these elements in \(\mathcal T\). The group law, automorphism property and norm-entire scalar orbits restrict from MF-07. The four Tomita identities (MF.46) of The analytic algebra is a common core also restrict to \(\mathcal T\); equivalently they integrate from the fibre identities under the square-integrable bounds just proved. In particular \(U_{-z}\) is the inverse of \(U_z\) on the original integral algebra.

**Proof of graph and product density.**

Fix \(x\in\mathcal A\). Since \(x(\gamma)\in\mathcal T_\gamma\), all its fibre modular powers exist. For \(n\in\mathbb Z\), put

\[
 h_n(\gamma)=
 \max\left\{
 \|\Delta_\gamma^n x(\gamma)\|,
 \|(\Delta_\gamma^n x(\gamma))^\sharp\|,
 \|L_{\Delta_\gamma^n x(\gamma)}\|
 \right\}. \tag{DI.17}
\]

DI-01, DI-03, and DI-04 make \(h_n\) a finite Borel function. Choose an increasing finite-measure exhaustion \(\Gamma_m\uparrow\Gamma\). Recursively choose \(c_{m,n}\), increasing in \(m\) for every \(n\), so that

\[
 E_m=\Gamma_m\cap\bigcap_{n\in\mathbb Z}\{h_n\leq c_{m,n}\}
 \quad\text{is increasing and}\quad
 \mu(\Gamma_m\setminus E_m)<m^{-1}. \tag{DI.18}
\]

For example, on \(\Gamma_m\) assign the \(n\)-th exceptional set measure less than
\(2^{-|n|-2}/m\), then enlarge the bounds to dominate those chosen earlier. The increasing union of the \(E_m\) is conull.

On \(E_m\), every modular power has square-integrable vector and involution fields and an essentially bounded multiplier, so \(x_m=1_{E_m}x\in\mathcal T\). Since \(E_m\uparrow\Gamma\) almost everywhere,
\(x_m\to x\) and \(x_m^\sharp\to x^\sharp\) in \(H\) by dominated convergence. Thus \(\mathcal T\) is a graph core for the same closed involution as \(\mathcal A\).

For completeness, these same cutoffs also prove the Hilbert-algebra product-density axiom. Fibrewise multiplication gives \(L_{x_m}=q_{E_m}L_x\), so \(L_{x_m}\to L_x\) strongly as \(E_m\) increases to a conull set. The left multipliers from \(\mathcal A\) act nondegenerately, because \(\mathcal A^2\) is dense by DI-07. Therefore the left multipliers from \(\mathcal T\) also act nondegenerately. If \(v\perp\mathcal T^2\), then \(L_y^*v=0\) for every \(y\in\mathcal T\), since \(\mathcal T\) is Hilbert dense. Closure under \(\sharp\) gives \(L_yv=0\) for every such \(y\), and nondegeneracy forces \(v=0\). The remaining Hilbert-algebra axioms restrict from \(\mathcal A\). Hence \(\mathcal T\) is a Tomita algebra equivalent to \(\mathcal A\), as asserted. \(\square\)

## Commute the maximal Tomita construction with integration

For full fibres, Gaussian modular regularization supplies a measurable fundamental family in the maximal Tomita algebras. The all-integer-power definition then identifies their integral exactly.

Assume the fibre left Hilbert algebras are full. Let \(\mathcal A_{0,\gamma}\) be the maximal Tomita algebra associated with \(\mathcal A_\gamma\), and let \(\mathcal A_0\) be the maximal Tomita algebra associated with \(\mathcal A=\int^\oplus\mathcal A_\gamma\,d\mu\). Then \(\gamma\mapsto\mathcal A_{0,\gamma}\) is measurable and

\[
 \mathcal A_0=\int_\Gamma^\oplus\mathcal A_{0,\gamma}\,d\mu
 \quad\text{as a Tomita direct integral}. \tag{DI.19}
\]

**Proof.** For \(r>0\) define

\[
 q_r(\lambda)=\sqrt{\frac r\pi}\int_{\mathbb R}e^{-rt^2}\lambda^{it}\,dt
 =\exp\!\left(-\frac{(\log\lambda)^2}{4r}\right),\qquad \lambda>0. \tag{DI.20}
\]

For every integer \(n\), the function \(\lambda^nq_r(\lambda)\) is bounded. MF-07–09, in particular the Gaussian multiplier estimates, show that
\(q_r(\Delta_\gamma)a_j(\gamma)\in\mathcal A_{0,\gamma}\) and that all its modular powers again have bounded left multipliers. The fields are measurable by DI-03 and bounded Borel calculus. Moreover, as \(r\to\infty\),

\[
 q_r(\Delta_\gamma)a_j(\gamma)\longrightarrow a_j(\gamma),
 \qquad
 S_\gamma q_r(\Delta_\gamma)a_j(\gamma)
   \longrightarrow S_\gamma a_j(\gamma). \tag{DI.21}
\]

This is spectral dominated convergence for the vector and its involution graph. Enumerating \(j\) and positive integers \(r\) gives a measurable graph-fundamental family for \(\mathcal A_{0,\gamma}\); its involutions and pairwise products are measurable by the same Gaussian and multiplier formulas. Hence the maximal Tomita algebras form a measurable field.

Let \(\mathcal B\) be their Tomita direct integral. If \(x\in\mathcal B\), then every \(\Delta^n x\) belongs to \(\mathcal A\), so the maximal-domain characterization MF-07 gives \(x\in\mathcal A_0\). Conversely, if \(x\in\mathcal A_0\), then every \(\Delta^n x\in\mathcal A\). Fibre decomposition gives
\(\Delta_\gamma^{n+k}x(\gamma)\in\mathcal A_\gamma\) for all \(n,k\in\mathbb Z\), so every \(\Delta_\gamma^n x(\gamma)\) lies in \(\mathcal A_{0,\gamma}\). The global membership of \(\Delta^n x\) in \(\mathcal A\) supplies exactly the square-integrability, involution, and essential multiplier bounds required by the left integral underlying \(\mathcal B\). Thus \(x\in\mathcal B\), proving (DI.19). \(\square\)

## Reverse assembly over a specified central diagonal

We now reverse assembly. A central diagonal first decomposes the Hilbert space and von Neumann algebra. Recover the fibre multiplication and involution from localized countable left and right cores, complete the fibres, and identify the actual global closed graph and generators. This argument uses only the unconditional full-fibres implication; it does not use the disputed converse.

Let \(\mathcal A\subset H\) be a full left Hilbert algebra with separable completion, let \(M=L(\mathcal A)''\), and let \(D\subseteq Z(M)\) be an abelian von Neumann subalgebra. Then there are a standard sigma-finite measure space \((\Gamma,\mu)\) and a measurable field of full left Hilbert algebras \(\mathcal A_\gamma\subset H_\gamma\) such that

\[
 \mathcal A=\int_\Gamma^\oplus\mathcal A_\gamma\,d\mu,
 \qquad
 D=L^\infty(\Gamma,\mu)\ \text{acting diagonally}. \tag{DI.22}
\]

**Proof using CENTRAL, closed graph localization and the explicit SCF cores.** Apply the central-decomposition contract to \((M,H,D)\), obtaining
\(H=\int^\oplus H_\gamma\,d\mu\) and
\(M=\int^\oplus M_\gamma\,d\mu\), with \(D\) diagonal. Choose a countable
\(\mathbb Q(i)\)-algebra \(\mathcal A_1\subseteq\mathcal A\), invariant under
\(\sharp\), which is a graph core for \(S\) and contains the factors of a countable product-dense family. Choose likewise a countable graph core in the associated right algebra. Take measurable representatives for these countably many global vectors and operators. Central projections commute with the actual closed global involutions; hence their graph projections commute with the diagonal algebra on the appropriate conjugate direct sums. DF's decomposability theorem gives measurable closed graph fields. Scalar localization of the global graph cores shows that their pairs are fibrewise graph fundamental: an orthogonal fibre vector would, after finite-measure and norm localization, give a nonzero global vector orthogonal to the global graph core. The same argument applied to the chosen global product family makes its products fibrewise fundamental. CENTRAL's countable decomposition and Prove product density before completing the core through Localize explicit products and operator generators thus give measurable representatives
\(a_j(\gamma)\) and right-core representatives that are fibrewise fundamental.

Because \(D\subseteq Z(M)\), every \(L_a\), \(a\in\mathcal A_1\), commutes with the diagonal and decomposes. Central projections preserve the full left algebra and commute with its closed involution and left multipliers, by WH-04 and modular centrality. After deleting one null set, define on the rational algebra generated by the \(a_j(\gamma)\)

\[
 a_j(\gamma)a_k(\gamma)=(a_ja_k)(\gamma),
 \qquad
 a_j(\gamma)^\sharp=(a_j^\sharp)(\gamma). \tag{DI.23}
\]

These rules are well defined. Indeed, if a proposed linear, product, or involution relation failed on a measurable set \(E\), the diagonal projection \(q_E\in D\subseteq Z(M)\) would localize the corresponding global relation. For example,

\[
 q_E(a_j-a_k)=0
 \ \Longrightarrow\
 L_{q_E(a_j-a_k)}=q_E L_{a_j-a_k}=0,
 \qquad
 S q_E(a_j-a_k)=q_E S(a_j-a_k)=0. \tag{DI.24}
\]

The first equality rules out failures after multiplication on either side, using centrality; the second rules out failures of the involution rule. Countability removes all exceptional sets at once. The decomposed left multipliers give bounded fibre left multiplication and the adjoint pairing.

The passage from the rational algebra to its complex span also needs well-definedness for arbitrary complex relations. Include, on the same conull set, the mixed identities against every selected right-core vector \(b_k(\gamma)\):

\[
 L_{a_j(\gamma)}b_k(\gamma)=R_{b_k(\gamma)}a_j(\gamma),
 \qquad
 \langle a_j(\gamma)^\sharp,b_k(\gamma)\rangle
 =\langle F_\gamma b_k(\gamma),a_j(\gamma)\rangle.
\]

Here \(F_\gamma b_k(\gamma)\) denotes the selected right involution value; closability is established next. These are countably many localized global identities. Fix a fibre and suppose \(\sum_j c_j a_j(\gamma)=0\), with finitely many arbitrary complex coefficients. The first identity implies that the bounded operator \(\sum_j c_jL_{a_j(\gamma)}\) vanishes on the dense right core and hence on the whole fibre. The second implies that \(\sum_j\overline{c_j}a_j(\gamma)^\sharp=0\), again by right-core density. Thus multiplication and conjugate-linear involution descend to \(\mathbb C\mathcal A_1(\gamma)\); countability is used for the identities, rather than for an uncountable set of possible complex coefficients.

The right-core representatives prove closability of the fibre involution: if
\(x_m\to0\) and \(x_m^\sharp\to y\) in one fibre, the localized adjoint identities against the fibrewise dense right core give \(\langle y,\eta\rangle=0\) for every right-core vector \(\eta\), hence \(y=0\). The selected product family gives fibrewise density of product spans. Thus the complex span \(\mathcal C_\gamma=\mathbb C\mathcal A_1(\gamma)\), with Hilbert completion \(H_\gamma\), is a left Hilbert algebra, and the family \(\mathcal C_\gamma\) satisfies DI-00.

Let \(\mathcal A_\gamma=(\mathcal C_\gamma)_{rr}\), its full left completion. DI-05 and its handed version make these completions a measurable field; DI-07 integrates them. Only the unconditional full-fibres-to-full-integral implication of DI-08 is used: \(\mathcal B=\int^\oplus\mathcal A_\gamma\,d\mu\) is full. No selector outside an original algebra and no fullness converse is needed.

We must identify the actual global closed involution and represented left algebra. For every core vector \(a_j\), central projections \(q_E\) preserve the original full algebra and satisfy \(S q_Ea_j=q_E Sa_j\). These scalar localizations therefore belong to the original \(\mathcal A\). On finite-measure and norm levels they also belong to \(\mathcal B\). The localization argument of DI-07 makes their linearized graph pairs a core for the integrated fibre involution. The preceding graph decomposition identifies that graph with the actual global \(G(S)\); the full completion of each fibre has the same closed involution as its rational core by SCF-02. Thus \(\mathcal A\) and \(\mathcal B\) have exactly the same closed involution.

Apply SCF-02 to the chosen original global star core: its products are dense and its left multipliers generate \(M\). Central scalar localizations preserve those multipliers. Their decomposed fibre multipliers generate the represented fibre algebras, again by SCF-02; DI-09 identifies the left von Neumann algebra of \(\mathcal B\) with the same decomposed \(M\). The full-completion uniqueness of WH-04 now identifies \(\mathcal B=\mathcal A\) inside \(H\). The identification uses the localized graph cores and the actual operator representation, rather than assuming that an unlocalized global family is automatically a graph core for the new integral. The diagonal statement is built into the chosen central decomposition, proving (DI.22). \(\square\)

The separability hypothesis is used to choose the countable left and right graph cores and to invoke a standard-base central decomposition. It is not imposed on the earlier single-fibre theorems.

## Distinguish fixed-diagonal equality from measurable implementation

There are two uniqueness questions. Literal equality of two integrals over the same diagonal determines the full fibres almost everywhere. Fibrewise unitary isomorphisms instead need a measurable implementation. The unitary tests and their complete sufficiency proof address that second question.

Let \(\mathcal A_{1,\gamma}\) and \(\mathcal A_{2,\gamma}\) be measurable fields of full left Hilbert algebras on the same standard sigma-finite base.

1. If their integral algebras are literally equal inside the same Hilbert direct integral, then \(\mathcal A_{1,\gamma}=\mathcal A_{2,\gamma}\) almost everywhere.
2. If almost every pair of fibres is unitarily isomorphic as left Hilbert algebras, then one can choose a measurable field of such unitary isomorphisms \(V_\gamma\), and

\[
 V=\int_\Gamma^\oplus V_\gamma\,d\mu \tag{DI.25}
\]

is a unitary isomorphism of the two integral algebras.

**Proof of 1.** The common integral has one diagonal algebra and one left von Neumann algebra. OA-MOD-DI-DEP-CENTRAL identifies the Hilbert fibres and their left von Neumann algebras almost everywhere. Choose countable measurable
\(\mathbb Q(i)\)-graph algebras fundamental for the two fields. Localize the first family on finite-measure sets controlling vector, involution, and left-multiplier norms. Each localized section belongs to the common integral and hence, by definition of the second integral, belongs fibrewise to \(\mathcal A_{2,\gamma}\). Countability and exhaustion put the whole first core in the second fibre algebra off one null set. Repeating the argument in the other direction and adjoining the two countable cores produces one common \(\mathbb Q(i)\)-graph algebra; the global literal equality makes its products and involution agree, and it is a graph core for both fibre algebras. Since both fibre algebras are full, WH-04 identifies both with the full completion of this common core inside the already identified fibre representation. Hence
\(\mathcal A_{1,\gamma}=\mathcal A_{2,\gamma}\) almost everywhere.

**Proof of 2 using Choose a witness after completing the measure through Recognize and measurably implement algebra isomorphisms.** Partition the base by the common fibre dimension and trivialize both Hilbert fields on each stratum by a fixed separable Hilbert space \(H_0\), using OA-MOD-DI-DEP-FIELD. The zero-dimensional stratum has its unique zero-space unitary; unequal dimensions have no unitary and are excluded by the almost-everywhere isomorphism hypothesis. Choose countable left graph cores
\(a_j(\gamma)\) for the first field and countable right graph cores
\(b_k(\gamma)\) for the second, together with the symmetric pair of cores. In the strong-topology unitary group \(U(H_0)\), let \(\Sigma_\gamma\) consist of the unitaries \(U\) satisfying the following countable tests and their symmetric \(U^*\)-versions:

\[
 \langle Ua_j,F_{2,\gamma}b_k\rangle
   =\langle b_k,U a_j^\sharp\rangle,\qquad
 R_{b_k}Ua_j
   =U L_{a_j}U^*b_k, \tag{DI.26}
\]

and

\[
 U\Delta_{1,\gamma}^{it}U^*
   =\Delta_{2,\gamma}^{it}\qquad(t\in\mathbb Q),
\]

where the operator equalities are tested on fixed countable Hilbert-fundamental sections. DI-03–05 make every vector and operator field in these tests measurable. The explicit joint Borel coding proved in SCF-06, with a complete strong metric controlling both a unitary and its adjoint, makes
\(\Sigma=\{(\gamma,U):U\in\Sigma_\gamma\}\) a Borel relation.

Every fibre algebra isomorphism satisfies these tests, so \(\Sigma_\gamma\) is nonempty almost everywhere. Conversely, SCF-06 proves the sufficiency of these exact tests. The graph-adjoint tests put \(Ua_j\) in the second involution domain with the correct involution; the mixed-multiplier tests give
\(L_{Ua_j}=UL_{a_j}U^*\) on a dense right core; and the symmetric tests give the inverse statements. The extension first uses weak pairings against the original opposite algebra to reach its entire graph domain, then the uniformly bounded strong-star approximation HAP-06 to reach every original left-algebra vector. Fullness and the symmetric tests give an onto isomorphism preserving multiplication and involution. These steps are proved in SCF-06; mere Hilbert graph density would not control multiplication by an arbitrary vector, as SCF-03 demonstrates. Thus \(\Sigma_\gamma\) is exactly the required isomorphism set.

SCF-05 now gives a choice measurable in the measure completion, and a Borel representative off a null set
\(\gamma\mapsto V_\gamma\in\Sigma_\gamma\). Its direct integral is unitary. The fibre isomorphisms preserve the vector norm, involution norm and left-multiplier norm, so they preserve all three conditions in (DI.8) in both directions. Thus (DI.25) carries one integral algebra onto the other. \(\square\)

The first assertion requires literal equality over one fixed diagonal structure. It does not claim that an arbitrary global unitary between the Hilbert completions is decomposable.

### A finite implementation check

Use two atoms of measure one with Hilbert–Schmidt \(M_2(\mathbb C)\) at each atom, its usual product and adjoint, and the trace inner product. Let \(P\) exchange the two standard coordinate vectors. Take \(U_a\xi=\xi\) and \(U_b\xi=P\xi P\). Each map preserves vector norm, involution, products and multiplier norm; their two-block direct sum is a measurable unitary algebra isomorphism.

Those algebra tests matter. A Hilbert-space unitary carrying \(I/\sqrt2\) to \(E_{12}\) exists by extending two unit vectors to orthonormal bases. It cannot preserve the involution: the first vector is self-adjoint and the second is not. Thus a fibre Hilbert-space unitary alone supplies no algebra isomorphism, even before measurability is considered.

### Mathematical sources

Masamichi Takesaki, *Theory of Operator Algebras II*, VI.3, is the mathematical antecedent for the graph, Hilbert-algebra, Tomita-algebra and disintegration results. Volume I, IV.8 and Appendix A, supplies the direct-integral and selection antecedents. The countable-core, multiplier-domain and selection arguments linked here fill the exact interfaces used by this exposition. The unrestricted fullness converse is replaced by the explicitly qualified theorem above; the separate CH construction states its additional assumption. The new scalar and finite examples, explanatory route and implementation check are CC0-1.0 contributions by OpenAI Codex, Ultra, October 2026. Existing proof and component licences remain.

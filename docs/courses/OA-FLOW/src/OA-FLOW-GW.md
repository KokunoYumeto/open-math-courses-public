# Finite ideals and GNS spaces for arbitrary weights

*Fresh local proof, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held. No faithfulness, normality, semifiniteness or countability is imposed unless explicitly stated.*

Let \(M\subseteq B(K)\) be a von Neumann algebra acting nondegenerately on an arbitrary Hilbert space. A weight is an additive positively homogeneous map \(\varphi:M_+\to[0,\infty]\), with \(0\cdot\infty=0\). In particular \(\varphi(0)=0\). Normality here means preservation of bounded increasing positive suprema; semifiniteness initially means ultraweak density of the linear span of the finite positive cone. We prove the alternative density and cutoff characterizations below. The zero algebra and zero GNS Hilbert space are allowed.

The proof inputs are CF-1, CF-6–8, CF-10, [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0)/[SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0) with [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1), and [BD, (BD7)](OA-FLOW-BD.md#oa-flow.bd.5) for bounded strong convergence implying concrete ultraweak convergence. The purely bounded-operator proof that a bounded increasing positive net converges strongly to its supremum is [WF-2, (WF5)](OA-FLOW-WF.md#oa-flow.wf.2); it does not depend on a weight or on another WF section. No previous WG, NW, OW or NP proof is a premise.

For free human context see [Hiai, *Lectures on von Neumann algebras*, §7.1, Definition 7.1 and the GNS discussion on printed pp.63–64](https://arxiv.org/pdf/2004.02383v1#page=63). The supplied finite-weight statements and general conventions motivated the scope check; all arguments required here are written below, including the quotient for nonfaithful weights and the increasing cutoff construction. Hiai's subsequently cited normality-equivalence and modular theorems are not imported.

<a id="oa-flow.gw.1"></a>

## GW-1. The finite cone, ideal and algebra

Put
\[
P=\{a\in M_+:\varphi(a)<\infty\},\qquad
N=\{x\in M:x^*x\in P\},\qquad
\mathfrak m=\operatorname{span}_{\mathbb C}P.
\]
If \(0\leq a\leq b\), then \(b=a+(b-a)\), and additivity shows \(\varphi(a)\leq\varphi(b)\). Thus \(P\) is hereditary. It is closed under addition and nonnegative scalar multiplication.

For \(x,y\in N\), positivity of \((x-y)^*(x-y)\) gives
\[
(x+y)^*(x+y)\leq2x^*x+2y^*y.
\tag{GW1}
\]
Heredity proves \(x+y\in N\). Scalar closure is immediate. For \(a\in M\),
\[
(ax)^*(ax)=x^*a^*ax\leq\|a\|^2x^*x,
\tag{GW2}
\]
so \(N\) is a linear left ideal. Every \(p\in P\) belongs to \(N\): \(p^2\leq\|p\|p\). Since it is self-adjoint, \(p\in N\cap N^*\).

For \(x,y\in N\), direct expansion gives
\[
y^*x=\frac14\sum_{k=0}^3 i^k(x+i^k y)^*(x+i^k y).
\tag{GW3}
\]
All four square terms are in \(P\). Conversely \(p\in P\) equals \((p^{1/2})^*p^{1/2}\), where \(p^{1/2}\in N\). Therefore
\[
\mathfrak m=\operatorname{span}N^*N.
\tag{GW4}
\]
Adjoints preserve this space. Also
\((x^*y)(z^*w)=x^*((yz^*)w)\), where \((yz^*)w\in N\), so \(\mathfrak m\) is a \*-algebra. The left-ideal property gives \(x^*y\in N\), and its adjoint belongs to \(N\); hence \(\mathfrak m\subseteq N\cap N^*\). The latter intersection is also a \*-algebra: for \(u,v\) in it, \(uv\in N\) and \((uv)^*=v^*u^*\in N\).

Every self-adjoint element of \(\mathfrak m\) is \(p-q\), \(p,q\in P\). Indeed, take real parts of the coefficients in any finite representation by elements of \(P\), then collect positive and negative coefficients. If \(p-q\geq0\), it is at most \(p\), so heredity gives \(p-q\in P\). Consequently
\[
\mathfrak m\cap M_+=P.
\tag{GW5}
\]
For \(z\in N\), \(|z|\in N\cap N^*\) since \(|z|^2=z^*z\in P\). Thus \(z^*z=|z|^2\) is a product from this intersection. Using (GW3), and the reverse containment \(uv=(u^*)^*v\), proves
\[
\mathfrak m=(N\cap N^*)^2,
\tag{GW6}
\]
where the square means the linear span of products.

<a id="oa-flow.gw.2"></a>

## GW-2. The unique linear extension and its Cauchy–Schwarz inequality

On the self-adjoint part of \(\mathfrak m\) set
\(\varphi_0(p-q)=\varphi(p)-\varphi(q)\), \(p,q\in P\).
If \(p-q=r-s\), then \(p+s=r+q\); finite additivity gives the same value for both differences. Addition and real scalar multiplication follow by collecting those differences. Complexification defines the unique complex-linear extension to \(\mathfrak m\). The extension is positive by (GW5), and \(\varphi_0(a^*)=\overline{\varphi_0(a)}\), since it is real on self-adjoint elements.

For \(x,y\in N\) define
\[
[x,y]_\varphi=\varphi_0(y^*x),\qquad q_\varphi(x)=[x,x]_\varphi.
\tag{GW7}
\]
All terms are finite by (GW4). This is sesquilinear, linear in the first variable, conjugate-symmetric, and nonnegative on the diagonal. Expanding \(q_\varphi(x+t y)\geq0\) for arbitrary complex \(t\) proves
\[
|[x,y]_\varphi|^2\leq q_\varphi(x)q_\varphi(y).
\tag{GW8}
\]
Explicitly, if \(q_\varphi(y)>0\), use \(t=-[x,y]_\varphi/q_\varphi(y)\). If \(q_\varphi(y)=0\), an arbitrarily large \(t\) with the phase making the mixed term negative forces \([x,y]_\varphi=0\).

Let \(Z=\{x\in N:q_\varphi(x)=0\}\). The inequality shows that these vectors pair to zero with every vector, hence \(Z\) is a linear subspace. Equation (GW2) gives
\[
q_\varphi(ax)\leq\|a\|^2q_\varphi(x),
\tag{GW9}
\]
so \(Z\) is also a left ideal of \(M\). The inner product on \(N/Z\) is well defined and positive definite. All these statements hold for an arbitrary weight, without normality or semifiniteness.

<a id="oa-flow.gw.3"></a>

## GW-3. The GNS representation, including null and zero cases

Use CF Section 10 to complete \(N/Z\) to a Hilbert space \(H_\varphi\). Write \(\Lambda_\varphi(x)\) for the image of \(x\in N\). Thus
\[
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
=\varphi_0(y^*x),\qquad
\overline{\Lambda_\varphi(N)}=H_\varphi.
\tag{GW10}
\]
Left multiplication preserves \(N\) and \(Z\), and (GW9) makes it bounded on the quotient. It extends uniquely to an operator \(\pi_\varphi(a)\) with
\[
\pi_\varphi(a)\Lambda_\varphi(x)=\Lambda_\varphi(ax),
\qquad \|\pi_\varphi(a)\|\leq\|a\|.
\tag{GW11}
\]
Linearity, multiplicativity and \(\pi_\varphi(1)=1_{H_\varphi}\) hold first on the dense quotient and then everywhere. The adjoint follows on that quotient from
\[
\langle\Lambda_\varphi(ax),\Lambda_\varphi(y)\rangle
=\varphi_0(y^*ax)
=\langle\Lambda_\varphi(x),\Lambda_\varphi(a^*y)\rangle.
\tag{GW12}
\]
Every expression is in \(\mathfrak m\), since \(ax,a^*y\in N\). Thus \(\pi_\varphi\) is a unital \*-representation. On the zero Hilbert space the identity is the zero operator, so this statement also covers \(N=Z\). If another Hilbert completion has a dense map with (GW10) and (GW11), the map sending one \(\Lambda(x)\) to the other preserves all inner products, vanishes on exactly \(Z\), and extends to the unique unitary intertwiner.

If \(\varphi(1)<\infty\), then \(N=M\), since \(x^*x\leq\|x\|^2 1\). In this case and only when \(1\in N\), the vector \(\Omega=\Lambda_\varphi(1)\) is available. It is cyclic and implements the bounded positive functional \(\varphi_0\):
\[
\varphi_0(a)=\langle\pi_\varphi(a)\Omega,\Omega\rangle,\qquad
\|\Omega\|^2=\varphi(1).
\tag{GW13}
\]
No vector \(\Lambda_\varphi(1)\) is used for an infinite weight.

<a id="oa-flow.gw.4"></a>

## GW-4. Semifiniteness and an increasing finite positive contraction net

The following conditions are equivalent, without normality or faithfulness:

1. \(\mathfrak m\) is ultraweakly dense in \(M\).
2. \(N\) is weak-operator dense in \(M\).
3. The supremum of all projections \(p\in M\) with \(\varphi(p)<\infty\) is \(1\).
4. There is an increasing net \(e_i\in P\), \(0\leq e_i\leq1\), with supremum \(1\).

First, (1) implies (2), since \(\mathfrak m\subseteq N\) and the ultraweak topology contains the weak operator topology.

To prove (2) implies (3), let \(q\) be the projection onto the closed span of the ranges of all finite-weight projections. Each unitary of \(M'\) preserves these ranges and their orthogonal complements; it therefore commutes with \(q\). The commutant-unitary test gives \(q\in M\), and this projection is exactly their supremum. For \(a\in P\), the spectral projection
\[
p_\epsilon=1_{[\epsilon,\infty)}(a)\leq\epsilon^{-1}a
\tag{GW14}
\]
has finite weight. These projections increase, as \(\epsilon\downarrow0\), to the support \(s(a)\). Hence \(s(a)\leq q\). If \(x\in N\), apply this to \(a=x^*x\). It follows that \(x(1-q)=0\), since
\(\|x(1-q)v\|^2=\langle x^*x(1-q)v,(1-q)v\rangle=0\).
The space \(\{x\in M:x(1-q)=0\}\) is weak-operator closed, by its vector coefficients. If \(N\) is weak-operator dense it contains \(1\), so \(q=1\).

For (3) implies (4), direct the entire finite cone \(P\) by operator order. This is directed: \(a+b\in P\) is an upper bound for \(a,b\). Define
\[
e_a=a(1+a)^{-1}=1-(1+a)^{-1}\qquad(a\in P).
\tag{GW15}
\]
Functional calculus gives \(0\leq e_a\leq1\) and \(e_a\leq a\), so \(e_a\in P\).
We justify its monotonicity without an operator-monotone-function theorem. For \(0<A\leq B\) positive and invertible, put \(C=A^{-1/2}BA^{-1/2}\geq1\). Functional calculus gives \(C^{-1}\leq1\), and
\(B^{-1}=A^{-1/2}C^{-1}A^{-1/2}\leq A^{-1}\).
Taking \(A=1+a,B=1+b\) proves \(e_a\leq e_b\) whenever \(a\leq b\).

Let \(E\leq1\) be the supremum of this bounded increasing net; existence and strong convergence follow from the bounded-operator lemma cited above. If \(p\) is a finite-weight projection, then \(np\in P\) and
\(e_{np}=n(1+n)^{-1}p\).
Thus \(E\geq p\). For \(v\in pK\), \(0\leq\langle(1-E)v,v\rangle\leq0\); positivity implies \(Ev=v\). Condition (3) says these ranges span a dense subspace, so \(E=1\).

Finally suppose (4). The bounded-operator lemma gives \(e_i\to1\) strongly. For \(x\in M\), the left-ideal property and \(e_i\in P\subseteq N\) give
\[
e_i x e_i=e_i^*(xe_i)\in\mathfrak m,\qquad
\|e_i x e_i\|\leq\|x\|,\qquad
e_i x e_i\longrightarrow x\text{ strongly}.
\tag{GW16}
\]
BD7 gives ultraweak convergence, proving (1). This completes every implication. In particular a semifinite weight has the explicitly constructed increasing finite positive contractions (GW15), even if it is not normal. No increasing net of finite-weight projections is asserted.

If \(\varphi\) is faithful and semifinite, then \(\pi_\varphi\) is faithful. Indeed, \(\pi_\varphi(a)=0\) implies \(\varphi((ax)^*(ax))=0\) for every \(x\in N\), hence \(ax=0\) by faithfulness. Taking the finite contractions \(x=e_i\) above and passing to their strong limit gives \(a=0\). Normality is not required for this conclusion.

<a id="oa-flow.gw.5"></a>

## GW-5. Normality gives the required GNS density

Now assume \(\varphi\) is normal and semifinite, and use the increasing finite contractions \(e_i\uparrow1\) just constructed. For \(x\in N\), one has
\[
e_i x=(e_i^{1/2})^*(e_i^{1/2}x)\in\mathfrak m,
\tag{GW17}
\]
because \(e_i^{1/2}\in N\) and \(e_i^{1/2}x\in N\). Moreover,
\[
0\leq x^*(1-e_i)^2x\leq x^*(1-e_i)x\leq x^*x.
\]
The net \(x^*e_i x\) increases strongly to \(x^*x\), so it has that order supremum. Its weights tend to the finite number \(\varphi(x^*x)\), by normality. Finite additivity therefore gives
\[
\|\Lambda_\varphi(x)-\Lambda_\varphi(e_i x)\|^2
\leq\varphi(x^*x)-\varphi(x^*e_i x)\longrightarrow0.
\tag{GW18}
\]
No subtraction of infinities occurs. Since \(\Lambda_\varphi(N)\) is dense,
\[
\overline{\Lambda_\varphi(\mathfrak m)}
=\overline{\Lambda_\varphi(N\cap N^*)}
=H_\varphi.
\tag{GW19}
\]
This argument uses no cyclic vector for \(1\) and works with arbitrary nets.

Normality alone, without semifiniteness, also implies that the GNS representation preserves bounded increasing positive suprema. If \(0\leq a_i\uparrow a\), then for \(x\in N\) the elements \(x^*a_i x\) increase to \(x^*ax\), all with finite weight. Consequently
\[
\langle(\pi_\varphi(a)-\pi_\varphi(a_i))\Lambda_\varphi(x),
              \Lambda_\varphi(x)\rangle
=\varphi(x^*ax)-\varphi(x^*a_i x)\longrightarrow0.
\tag{GW20}
\]
The positive differences have a common bound \(\|a\|\), so the same squared-norm inequality as (WF5) yields strong convergence on \(\Lambda_\varphi(N)\); approximation extends it to all \(H_\varphi\). Thus \(\pi_\varphi(a_i)\uparrow\pi_\varphi(a)\). This is precisely an order-continuity statement. The subsequent [order-normal functional bridge](OA-FLOW-NF.md#oa-flow.nf.5) supplies an independent proof of ultraweak continuity from the finite-functional case, without importing the arbitrary-weight normality equivalence.

<a id="oa-flow.gw.6"></a>

## GW-6. The exact remaining weight-to-Hilbert-algebra step

For a faithful normal semifinite weight, \(\Lambda_\varphi\) is injective, so the dense space \(\Lambda_\varphi(N\cap N^*)\) has an unambiguous product and conjugate-linear involution
\[
\Lambda_\varphi(x)\Lambda_\varphi(y)=\Lambda_\varphi(xy),
\qquad
\Lambda_\varphi(x)^\sharp=\Lambda_\varphi(x^*).
\tag{GW21}
\]
The finite-star \*-algebra is closed under these operations by GW-1, left multiplication is bounded by (GW11), and its Hilbert adjoint identity is (GW12). Its product span is dense by (GW6) and (GW19). The additional axiom is **closability of the involution** on this whole finite-star domain. Its complete later proof is WR-3; ordinary norm continuity of multiplication or the density just established does not supply it.

After that axiom, the fresh CI/HA-R/WH04 theory applies to its fullification. The later full algebra identification, original-weight recovery and canonical opposite finite-cone proofs cover faithful n.s.f. weights; the modular opposite formula and implementing vector follows after MF-06. The later [normality equivalence and whole-cone normal-minorant formula](OA-FLOW-EW.md#ew-5) covers every extended-valued weight. These separate proofs are not premises of the present elementary finite-ideal/GNS construction. The later [general normal opposite-weight construction](OA-FLOW-NO.md#no-1) proves the extension separately for every normal input: its supported-functional bijection uses the finite-domain projection, its unrestricted value is the functional evaluated at the finite-domain projection, and its GNS range may be a proper subspace. These later results are not inputs of GW.

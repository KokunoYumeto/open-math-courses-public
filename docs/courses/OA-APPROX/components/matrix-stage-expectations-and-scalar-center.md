# Matrix-stage expectations and scalar center

*Written by GPT-6.1 Sol (OpenAI), Ultra. Course exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

An increasing family of full matrix algebras can determine the center of its von Neumann closure directly. The input is a faithful normal trace on that closure. No MASA, expected subfactor, classification theorem or pre-existing factor assertion is required.

We use the normal trace GNS representation and the [bounded-density theorem](../../OA-FLOW/OA-FLOW-BD.html#oa-flow.bd.3). The scalar Hilbert projection facts and the normal coefficient calculations below apply to every finite matrix stage.

<a id="mx1"></a>

## MX1. Finite matrix projections determine the center

**Theorem.** Let \(P\) be a von Neumann algebra with a faithful normal tracial state \(\tau\). Let
\[
F_1\subset F_2\subset\cdots\subset P,\qquad
F_n\cong M_{d_n},\qquad
P=\left(\bigcup_nF_n\right)'',
\]
where every stage has the same unit as \(P\). Choose matrix units \((e_{ij}^{(n)})_{1\le i,j\le d_n}\) in each stage. Then
\[
Q_n(x)=d_n\sum_{i,j=1}^{d_n}
            \tau(e_{ji}^{(n)}x)e_{ij}^{(n)}
\tag{MX1}
\]
is the normal trace-preserving conditional expectation onto \(F_n\). It is completely positive and contractive. For every \(x\in P\),
\[
\|Q_n(x)-x\|_{2,\tau}\longrightarrow0.
\tag{MX2}
\]
Consequently \(Z(P)=\mathbb C1\).

**Proof.** Fix a stage and suppress its superscript. Traciality and equivalence of the diagonal projections give \(\tau(e_{ii})=1/d\). For \(i\ne j\),
\(\tau(e_{ij})=\tau(e_{ij}e_{jj})=\tau(e_{jj}e_{ij})=0\).
The matrix-unit multiplication rule therefore shows that \(Q\) fixes every matrix unit and that \(Q(1)=1\). The same rule gives
\[
Q(axb)=aQ(x)b\qquad(a,b\in F,\ x\in P).
\tag{MX3}
\]

Here is positivity at every matrix size. If \(X=(x_{ab})\in M_k(P)\) is positive and \(c_{a,i}\) is any scalar array, put
\(v_a=\sum_i c_{a,i}e_{i1}\).
The scalar coefficient matrix of \(Q^{(k)}(X)\), in the ordinary representation of \(M_k(F)\cong M_{kd}\), has quadratic form
\[
d\sum_{a,b,i,j}\overline{c_{a,i}}c_{b,j}
                      \tau(e_{ji}x_{ab})
=d\,\tau\!\left(\sum_{a,b}v_a^*x_{ab}v_b\right)\ge0.
\tag{MX4}
\]
The equality uses traciality to move \(e_{j1}e_{1i}=e_{ji}\); the inequality follows by applying the positive operator matrix \(X\) to the operator column \((v_b)\). Thus \(Q\) is completely positive. In particular it is positive and order preserving, so
\[
0\le Q(x^*x)\le\|x\|^2 1.
\]
Apply positivity to \((x-Q(x))^*(x-Q(x))\) and use (MX3) and \(Q|_F=\operatorname{id}\). The result is
\[
Q(x)^*Q(x)\le Q(x^*x)\le\|x\|^2 1,
\tag{MX5}
\]
which proves contractivity.

Every coefficient \(x\mapsto\tau(e_{ji}x)\) is normal: multiplication by a fixed bounded operator is ultraweakly continuous, and \(\tau\) is normal. The finite sum (MX1) is therefore normal. Taking its trace leaves only the terms \(i=j\), and gives \(\tau(Q(x))=\tau(x)\). The same finite calculation, first for a matrix unit \(y\) and then by linearity for every \(y\in F\), gives
\[
\tau(y^*Q(x))=\tau(y^*x).
\tag{MX6}
\]
Hence on the trace GNS space, \(Q(x)\Omega_\tau\) is exactly the orthogonal projection of \(x\Omega_\tau\) onto the finite-dimensional subspace \(F\Omega_\tau\).

These subspaces increase with \(n\). Their union is dense in the trace GNS space of \(P\). Indeed the bounded-density theorem gives, for any \(x\in P\), a uniformly bounded net from \(\bigcup_nF_n\) converging strongly to \(x\) in the faithful normal GNS representation. Applying that net to \(\Omega_\tau\) puts \(x\Omega_\tau\) in the closure of the union of the subspaces. Those vectors are dense by definition of the GNS space.

For completeness, orthogonal projections onto increasing subspaces with dense union converge strongly to the identity. Given a vector \(\xi\) and a tolerance, choose a vector \(\eta\) in one of the subspaces close to \(\xi\). Every later projection \(p_n\) fixes \(\eta\), and the norm of \(1-p_n\) is at most one, so
\(\|(1-p_n)\xi\|\le\|\xi-\eta\|\).
Apply this to \(\xi=x\Omega_\tau\) and the projections identified by (MX6). This proves (MX2).

Finally let \(z\in Z(P)\). Bimodularity gives \(aQ_n(z)=Q_n(z)a\) for every \(a\in F_n\). The center of a full matrix algebra is scalar, and trace preservation thus gives
\[
Q_n(z)=\tau(z)1.
\]
Equation (MX2) forces \(\|z-\tau(z)1\|_{2,\tau}=0\). Faithfulness of \(\tau\) makes \(z=\tau(z)1\), proving the center assertion. \(\square\)

## Reading

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Section 11.2, printed pp.185–188, gives the compatible matrix and product-trace GNS framework. The finite coefficient formula and scalar-center argument above apply to a given traced von Neumann closure, before any MASA construction or factor classification.

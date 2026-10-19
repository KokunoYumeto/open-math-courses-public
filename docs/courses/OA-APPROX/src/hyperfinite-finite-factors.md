# Local approximation and the hyperfinite finite factor

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A finite-dimensional algebra that approximates a few operators need not contain a previously chosen algebra. The main construction below repairs that defect. A small change of one projection aligns the first matrix corner, and matrix units then align the whole old algebra exactly. Repeating this construction identifies every separable AFD factor of type \(\mathrm{II}_1\) with the tracial infinite product of \(M_2\).

The complete [finite-algebra and vacuum inputs HF0–5](../components/hyperfinite-finite-algebra-and-vacuum-inputs.md#hf0) supply the whole trace-preserving expectation onto any unital subalgebra, bounded trace topology, all normal-state cutoff bounds, arbitrary-center and properly infinite projection arguments, and the full vacuum/tracial direct sum. The complete [PC0–7 and FCT0–7](../components/central-finite-trace-inputs.md#retained-pc-complete-inputs) supplies center-valued trace existence, normality, faithfulness, uniqueness and comparison with arbitrary center. The [dyadic construction AF1–5](../components/central-afd-uniqueness-inputs.md#af1-finite-matrices-and-trace-projections) proves exact containment and the whole AFD trace-GNS identification. The [normal representation and matrix-corner construction NA0–6](../components/normal-representations-and-finite-trace-corners.md#na0) supplies arbitrary Hilbert multiplicity and the finite commutant application, using HF0's full tracial commutant. The [whole tracial product SS2](../components/strong-stability-matrix-and-product-inputs.md#ss2-whole-variable-matrix-tracial-product) supplies the concrete factor \(R\).

Unless stated otherwise, \(M\) is a factor of type \(\mathrm{II}_1\), with normalized faithful normal trace \(\tau\), and
\[
\|x\|_2=\tau(x^*x)^{1/2}.
\]
The inequalities \(\|axb\|_2\le\|a\|\|x\|_2\|b\|\), \(\|x^*\|_2=\|x\|_2\), and \(|\tau(x)|\le\|x\|_2\) follow from the trace and Cauchy–Schwarz. We write \(E_N\) for the trace-preserving expectation onto a unital subalgebra \(N\).

<a id="bounded-trace-topology"></a>

**Bounded trace topology (PB1–PB2).** The normal functionals
\[
\psi_b(x)=\tau(bx),\qquad b\in M,
\tag{PB1}
\]
are norm dense in \(M_*\). Indeed their span is a linear subspace of the concrete predual. If its norm closure were proper, Hahn–Banach would give a nonzero element of \((M_*)^*=M\) annihilating it, by [CP6](../../OA-FLOW/OA-FLOW-CP.html#oa-flow.cp.6). Calling that element \(x\), we would have \(\tau(bx)=0\) for every \(b\); choosing \(b=x^*\) and using faithfulness gives \(x=0\), a contradiction.

Let \(\psi\) be a normal positive functional and \(\|x\|\le C\). Choose \(b\in M\) with \(\|\psi-\psi_b\|<\eta\), by (PB1). Trace Cauchy–Schwarz, applied to \(x^*x\) through its square root, gives \(|\tau(bx^*x)|\le\|b\|\tau(x^*x)\). Thus
\[
\psi(x^*x)\le\|b\|\|x\|_2^2+\eta C^2,\qquad
\psi(xx^*)\le\|b\|\|x\|_2^2+\eta C^2.
\tag{PB2}
\]
This proves that, on every norm-bounded set, the \(2\)-norm gives the intrinsic sigma-strong* topology. The converse uses the trace itself as one of the tests. There is no cardinality restriction on the convergent net.

If a normal positive functional has already been represented as \(\tau(h\,\cdot)\), the same estimate can also be written using a bounded positive approximation \(b\) to \(h\):

\[
\tau(hx^*x)\le\|b\|\|x\|_2^2+C^2\|h-b\|_1.
\tag{1}
\]
This density notation is optional for the topology proof: (PB1)–(PB2) prove the required estimates directly in the concrete predual.

Norm-bounded \(2\)-norm Cauchy sequences have their limit in \(M\): an ultraweak cluster point of the bounded ball has the same pairings \(\tau(y^*x)\), \(y\in M\), as the Hilbert-space limit, and those pairings determine that limit.

<a id="3-replacing-an-approximant-by-a-dyadic-factor"></a>

## Replacing finite approximants by dyadic matrix factors

For any von Neumann algebra \(P\), **AFD** means that for every finite set \(x_1,\ldots,x_m\in P\) and every sigma-strong* neighborhood \(U\) of zero there is a finite-dimensional *-subalgebra \(D\subset P\) with \(x_j\in D+U\) for every \(j\). This local definition does not require a sequence or separability. A possibly nonunital \(D\) can be replaced by \(D+\mathbb C1\).

In a finite factor call this property **locally AFD** when expressed using finite-set \(2\)-norm approximation. The two formulations agree: the intrinsic topology includes the trace seminorm, while applying \(E_D\) to any \(2\)-norm approximants supplies errors no larger and bounds the approximants by the original operator norms. Equation (PB2) then gives approximation for every specified sigma-strong* neighborhood.

**Lemma 3.1.** For every finite-dimensional unital subalgebra \(D\subset M\) and \(\eta>0\), there is a unital matrix subfactor \(Q\cong M_{2^p}\) such that
\[
\|x-E_Q(x)\|_2\le\eta\|x\|\qquad(x\in D).
\tag{10}
\]
The integer \(p\) can be required to be arbitrarily large.

**Proof.** Write \(D=\bigoplus_k M_{d_k}\), with matrix units \(f_{ij}^{(k)}\), and put \(t_k=\tau(f_{11}^{(k)})\). Choose \(p\) large enough that every \(r_k=\lfloor2^p t_k\rfloor\) is positive. Cut \(f_{11}^{(k)}\) down to a projection \(g_k\) of trace \(r_k2^{-p}\), and split \(g_k\) into \(r_k\) projections of trace \(2^{-p}\). Transport these pieces by \(f_{i1}^{(k)}\). The remaining projection has trace
\[
1-\sum_k d_k r_k2^{-p},
\]
an integer multiple of \(2^{-p}\), and can also be split into pieces of trace \(2^{-p}\). All the resulting pieces are equivalent.

They form the diagonal of a full \(2^p\)-matrix system, chosen to preserve the transported connections inside each \(k\)-block. To see that compatible extension directly, choose one reference diagonal projection. Connect it to the first diagonal in each existing block by a partial isometry; connect it to that block's other diagonals by the prescribed block matrix units. If these connecting maps are \(v_a\), their initial projection is the reference and their orthogonal final projections sum to one. The operators \(v_av_b^*\) are a full matrix system extending every prescribed block.

Its algebra \(Q\) contains
\[
\widetilde f_{ij}^{(k)}
=f_{i1}^{(k)}g_kf_{1j}^{(k)},\qquad
\|f_{ij}^{(k)}-\widetilde f_{ij}^{(k)}\|_2^2
=t_k-r_k2^{-p}<2^{-p}.
\tag{11}
\]
For \(x=\sum\lambda_{ij}^{(k)}f_{ij}^{(k)}\), each coefficient has modulus at most \(\|x\|\). With \(s=\sum_k d_k^2\), the corresponding sum of the \(\widetilde f\)'s differs from \(x\) by at most \(s2^{-p/2}\|x\|\). The expectation is the nearest \(L^2\) point of \(Q\), so taking \(p\) large gives (10). \(\square\)

It follows that in a locally AFD factor every finite-dimensional linear subspace \(V\) can be approximated uniformly on its operator-norm unit ball by a dyadic matrix subfactor. Choose a basis \(v_1,\ldots,v_m\). The constant
\[
C_V=\sup\left\{\sum_j|\lambda_j|:
\left\|\sum_j\lambda_jv_j\right\|\le1\right\}
\tag{12}
\]
is finite, by equivalence of norms on \(V\). First approximate its basis by a finite-dimensional algebra, using its expectation, then apply Lemma 3.1. The sum of the basis errors times \(C_V\) controls the whole unit ball. This is the finite-dimensional uniformity needed in the next step.

<a id="4-making-containment-exact"></a>

## Making the next matrix algebra contain the old one

**Lemma 4.1.** Suppose \(M\) is locally AFD, \(N\subset M\) is a unital copy of \(M_d\) with \(d=2^n\), \(V\subset M\) is finite dimensional, and \(\varepsilon>0\). There is a unital dyadic matrix subfactor \(Q\supset N\) satisfying
\[
\|x-E_Q(x)\|_2\le\varepsilon\|x\|\qquad(x\in V).
\tag{13}
\]
Its matrix size can be made larger than \(d\).

**Proof.** Fix matrix units \(e_{ij}\) of \(N\), put \(e=e_{11}\), and let
\[
W=\mathbb Ce+\sum_{i,j}e_{1i}Ve_{j1}\subset eMe.
\]
Choose a unital \(D\cong M_{2^p}\), \(p\ge n\), with
\(\|z-E_D(z)\|_2\le\delta\|z\|\) on \(W\), where \(\delta>0\) will tend to zero. Put \(h=E_D(e)\). Then \(0\le h\le1\) and
\[
\|h-e\|_2\le\delta,\qquad
\|h-h^2\|_2\le3\delta.
\]
For the second estimate expand \(h-h^2=(h-e)+(e-h)e+h(e-h)\). Formula (5) gives \(q\in D\) with \(\|q-e\|_2\le7\delta\). Since \(|\tau(q)-1/d|\le7\delta\), enlarge or shrink \(q\) inside \(D\) to \(q_1\) of trace exactly \(1/d\). This is possible because \(p\ge n\); both traces are integral multiples of \(2^{-p}\). The two projections are comparable, so
\[
\|q-q_1\|_2^2=|\tau(q)-1/d|,\qquad
\|q_1-e\|_2\le a(\delta):=7\delta+\sqrt{7\delta}.
\tag{14}
\]
Lemma 1.1 gives a unitary \(u\) carrying \(q_1\) to \(e\), with \(\|u-1\|_2\le\sqrt2\,a(\delta)\).

Choose unital \(d\)-matrix units \(w_{ij}\) in \(D\), with \(w_{11}=q_1\): split the matrix space into \(d\) equal-dimensional blocks. The operator
\[
v=\sum_{i=1}^d e_{i1}u w_{1i}
\tag{15}
\]
is unitary. Multiplying its sums gives \(v^*v=\sum_iw_{ii}=1\), \(vv^*=\sum_ie_{ii}=1\), and \(vw_{ij}v^*=e_{ij}\). Thus \(Q=vDv^*\) contains \(N\) exactly.

Only the first corner needs a small conjugation. For \(z\in W\) let \(z'=q_1E_D(z)q_1\). Bimodularity and \(z=eze\) give
\[
\|z-z'\|_2\le\bigl(\delta+2a(\delta)\bigr)\|z\|.
\]
Moreover \(\|z'\|\le\|z\|\), and \(vz'v^*=uz'u^*\), since \(vq_1=uq_1\). Therefore
\[
\|z-vz'v^*\|_2
\le\bigl(\delta+(2+2\sqrt2)a(\delta)\bigr)\|z\|.
\tag{16}
\]
For \(x\in V\), its matrix entries \(z_{ij}=e_{1i}xe_{j1}\) lie in \(W\) and have norms at most \(\|x\|\). Reconstruct \(x=\sum_{i,j}e_{i1}z_{ij}e_{1j}\), replacing every entry by its approximant in \(eQe\). The resulting element of \(Q\) has error at most
\[
d^2\bigl(\delta+(2+2\sqrt2)a(\delta)\bigr)\|x\|.
\tag{17}
\]
This tends to zero with \(\delta\); choose it below \(\varepsilon\). The nearest-point property of \(E_Q\) gives (13). The choice of \(D\) can have \(p>n\). \(\square\)

There is no assertion that the whole aligning unitary \(v\) is close to one. Its first-corner action is the controlled unitary \(u\); reconstruction by the old matrix units supplies the required bound.

<a id="1-rotating-equivalent-projections"></a>

## The projection repair used in exact containment

**Lemma 1.1.** If \(e,f\) are equivalent projections in a finite von Neumann algebra, there is a unitary \(u\) such that
\[
ueu^*=f,\qquad (u-1)^*(u-1)\le2(e-f)^2.
\tag{2}
\]
In particular \(\|u-1\|_2\le\sqrt2\|e-f\|_2\) whenever a finite trace is specified.

**Proof.** Set \(D=e-f\) and
\[
r=fe+(1-f)(1-e).
\]
Multiplication gives \(re=fr\),
\[
r^*r=rr^*=1-D^2,\qquad r+r^*=2(1-D^2).
\tag{3}
\]
The operator \(D^2\) commutes with \(e,f,r\). Let \(k=1_{\{1\}}(D^2)\). On \(1-k\), the polar part \(u_0\) of \(r\) is unitary, carries \(e(1-k)\) to \(f(1-k)\), and has real part \((1-D^2)^{1/2}\). Hence on that support
\[
(u_0-(1-k))^*(u_0-(1-k))
=2\bigl((1-k)-(1-D^2)^{1/2}\bigr)\le2D^2(1-k).
\tag{4}
\]
The last inequality is the scalar inequality \(1-\sqrt{1-s}\le s\), \(0\le s\le1\).

The exceptional projection \(k\) splits as \(p+q\), where \(p=e\wedge(1-f)\) and \(q=(1-e)\wedge f\). Indeed \(D^2=1\) implies \(r=0\); on \(eH\) its first term forces \(fe=0\), and on \((1-e)H\) its second term forces \(f=1\). Equivalence of \(e,f\) gives equal center-valued traces. The equivalence already established on \(1-k\) then gives equal center-valued traces for \(p,q\). [FCT7](../components/central-finite-trace-inputs.md#oa-flow.fct.7), equation (FCT32), gives a partial isometry \(v\) with \(v^*v=p,vv^*=q\) from that equality of center-valued traces. The skewadjoint unitary \(w=v-v^*\) on \(k\) carries \(p\) to \(q\), and \((w-k)^*(w-k)=2k\). Thus \(u=u_0+w\) is the required unitary; (4) and \(D^2k=k\) give (2). \(\square\)

There is also a useful spectral rounding estimate. If \(0\le h\le1\), \(\varphi\) is any normal state, and \(\|h-h^2\|_\varphi\le\delta\), then
\[
q=1_{[1/2,1]}(h)
\quad\Longrightarrow\quad
\|h-q\|_\varphi\le2\delta,\qquad
\|h^{1/2}-q\|_\varphi\le\sqrt{2\delta}.
\tag{5}
\]
The two reducing interval calculations in [HF1](../components/hyperfinite-finite-algebra-and-vacuum-inputs.md#hf1) give the operator inequalities
\[
(h-q)^2\le4h^2(1-h)^2,\qquad
(h^{1/2}-q)^2\le2h(1-h).
\]
The whole cutoff projection is constructed there from continuous positive parts and support limits, including the endpoint \(1/2\). Applying \(\varphi\) to the first inequality and positive-functional Cauchy–Schwarz to the second proves (5) for every normal state, including a nonfaithful one.

A higher cutoff is useful too: for \(0<\delta<1/4\), put \(\epsilon=\sqrt\delta\) and \(q'=1_{[1-\epsilon,1]}(h)\). The complete support/order argument of HF1 gives
\[
(1-h)^2(1-q')\ge\delta(1-q'),\qquad
(1-h)^2q'\le\delta q'.
\]
The precise calculation below proves the sharper bounds (6a), which imply the following original bounds (6) since \(0<\delta<1\):
\[
\|h-q'\|_\varphi\le2\sqrt\delta,\qquad
\|h^{1/2}-q'\|_\varphi\le\sqrt3\,\delta^{1/4}.
\tag{6}
\]
The same higher cutoff actually gives the sharper estimate
\[
\|h-q'\|_\varphi\le\sqrt{2\delta},\qquad
\|h^{1/2}-q'\|_\varphi\le\sqrt{3\delta}.
\tag{6a}
\]
Indeed \((1-h)^2(1-q')\ge\delta(1-q')\), so
\[
\varphi(h^2(1-q'))
\le\delta^{-1}\varphi(h^2(1-h)^2)\le\delta.
\]
Also \(\varphi(h(1-h))\le\|h-h^2\|_\varphi\le\delta\). Adding these positive operator estimates gives \(\varphi(h(1-q'))\le2\delta\). On \(q'\), both \((1-h)^2\) and \((1-h^{1/2})^2\) are at most \(\delta q'\). Split the two squared errors over \(q'\) and \(1-q'\) to obtain (6a). This is the higher-cutoff mechanism of Connes’s Lemma 1.1.5; the lower bound for \((1-h)^2\) supplies the spectral inequality needed in its proof. The preceding bounds (6) follow as well, since \(0<\delta<1\).

Only the simpler cutoff (5) will be needed below.

<a id="2-trace-cuts-tensor-coordinates-and-averaging"></a>

## Trace cuts and first-corner coordinates

Halving means that every projection in a type II algebra is the sum of two equivalent orthogonal projections. In a \(\mathrm{II}_1\) factor this gives every scalar trace cut: for \(0\le s\le\tau(e)\), expand \(s/\tau(e)\) in binary, repeatedly halve the current remainder of \(e\), and retain the half prescribed by each digit. The selected orthogonal pieces have traces \(\tau(e)2^{-j}\). Their strong sum has trace \(s\), by normality. Equal-trace projections are equivalent by finite trace comparison.

If \((e_{ij})_{i,j=1}^d\) are unital matrix units in an arbitrary von Neumann algebra \(P\), then
\[
P\cong M_d\bar\otimes e_{11}Pe_{11},\qquad
x\longmapsto[e_{1i}xe_{j1}]_{i,j}.
\tag{7}
\]
The inverse is \([x_{ij}]\mapsto\sum_{i,j}e_{i1}x_{ij}e_{1j}\). The matrix-unit rules check the products, adjoints and inverses; finite sums and normal corners show normality. The relative commutant of the matrix algebra is the diagonal copy \(x\mapsto\sum_i e_{i1}xe_{1i}\) of the corner. Thus the matrix algebra and its relative commutant generate \(P\). Type II is preserved in this corner: an abelian projection there would be abelian in \(P\).

<a id="5-uniqueness-and-all-finite-corners"></a>

## Identifying the dyadic limit and all finite corners

Let
\[
R=\bar\bigotimes_{j\ge1}(M_2,\operatorname{tr}_2).
\]
The tracial product construction gives its faithful normal product trace and separable trace GNS space. The explicit finite-stage projections in [the matrix-stage expectation theorem](../components/matrix-stage-expectations-and-scalar-center.md#mx1) applied to its local matrix factors give scalar center: a central element has scalar projection at every stage and is their GNS limit. Their matrix sizes are unbounded, so \(R\) is of type \(\mathrm{II}_1\).

**Theorem 5.1.** For a \(\mathrm{II}_1\) factor \(M\) with separable predual, the following are equivalent:

1. \(M\cong R\).
2. \(M\) is generated by an increasing sequence of finite-dimensional *-subalgebras.
3. \(M\) is locally AFD.
4. Every nonzero corner of every finite matrix amplification of \(M\) is locally AFD.

**Proof.** The first implication gives the initial tensor factors. For the second, Kaplansky density in the increasing union supplies bounded strong* approximants, hence the third condition.

For \(3\Rightarrow1\), choose a \(2\)-norm dense sequence \((x_j)\) in the unit ball. Such a sequence exists: the ball is compact metrizable in the weak* topology; a countable weak* dense subset is weakly dense in \(L^2\), and its rational convex combinations are norm dense by convex separation. Apply Lemma 4.1 successively to \(V_k=\operatorname{span}\{x_1,\ldots,x_k\}\), keeping the previous dyadic matrix algebra exactly and making the error tend to zero. This gives increasing \(N_k\cong M_{2^{n_k}}\), with strictly increasing \(n_k\), whose union generates \(M\). Indeed \(E_{N_k}(x_j)\to x_j\) in \(2\)-norm with bounds one; the bounded-ball completeness and (PB2) put every \(x_j\), hence the entire ball, in the generated algebra.

A unital inclusion \(M_a\subset M_b\) has \(b=ar\) and relative commutant \(M_r\): its action on \(\mathbb C^b\) is a sum of \(r\) copies of the defining \(a\)-dimensional module, or equivalently use (7). Between \(N_k\) and \(N_{k+1}\) insert the successive \(M_2\) factors of this relative commutant. Insert the earlier tensor levels inside \(N_1\) too. We obtain \(A_m\cong M_{2^m}\), \(A_m\subset A_{m+1}\), with the same generated algebra. Their relative commutants \(A_m'\cap A_{m+1}\cong M_2\) commute, and their finite products equal \(A_{m+1}\), by (7). The trace on each finite product is its unique normalized trace. The trace-preserving isomorphism of the algebraic unions therefore extends to a unitary of trace GNS spaces and, by intertwining left multiplication, to a normal isomorphism \(M\cong R\).

To prove \(3\Rightarrow4\), finite amplification can be handled directly on a finite set of matrix entries. Approximate all entries by one finite-dimensional \(D\subset M\); then \(D\otimes M_n\) approximates the matrices, since the normalized squared \(2\)-norm is \(n^{-1}\) times the sum of the entries' squared norms. This argument needs no generating sequence. It suffices next to handle a nonzero \(e\in M\). Choose \(e_1\le e\) of dyadic trace \(q2^{-n}\), so close in \(2\)-norm that \(\|e-e_1\|_2<\eta\). Extend its \(q\) equal dyadic pieces to a full unital \(M_{2^n}\) system as in Lemma 3.1. Lemma 4.1 gives a finite matrix \(N\) containing that system and approximating \(e_1Ve_1\), for a prescribed finite-dimensional \(V\subset eMe\). Then \(e_1Ne_1\subset eMe\) is finite dimensional, and for \(x\in V\), \(\|x\|\le1\),
\[
\|x-e_1E_N(e_1xe_1)e_1\|_2
\le2\|e-e_1\|_2+\|e_1xe_1-E_N(e_1xe_1)\|_2.
\tag{18}
\]
Both terms can be made arbitrarily small. The normalized corner trace divides the squared norm by \(\tau(e)\), so its \(2\)-norm is \(\tau(e)^{-1/2}\) times the ambient norm. This fixed factor does not affect approximation. Adding the missing corner identity if desired preserves finite dimension. Condition 4 implies 3 by taking the identity corner. \(\square\)

**Corollary 5.2.** If one nonzero corner of \(M\bar\otimes M_n\) is locally AFD, then \(M\) is locally AFD. All separable AFD \(\mathrm{II}_1\) factors, and all their nonzero amplified finite corners, are isomorphic to \(R\).

**Proof.** First establish the local permanence statements without a separability assumption. For finite amplification of any locally AFD \(\mathrm{II}_1\) factor \(L\), approximate the finitely many entries of the desired matrices by one finite-dimensional \(D\subset L\). The identity
\[
\|[a_{ij}]\|_{2,L\otimes M_r}^2=r^{-1}\sum_{i,j}\|a_{ij}\|_{2,L}^2
\]
makes \(D\otimes M_r\) an arbitrarily good finite-dimensional approximant. Its trace expectation supplies contractions when the original matrices are contractions.

For a nonzero corner \(pLp\), cut \(p_1\le p\) with dyadic trace as close to \(\tau_L(p)\) as desired. Split \(p_1\) into equal dyadic pieces and extend them to a unital dyadic matrix system in \(L\). Apply Lemma 4.1 to that system and the finite span of the \(p_1xp_1\)'s. The resulting matrix algebra \(N\) contains \(p_1\) exactly. The algebra
\[
p_1Np_1\oplus\mathbb C(p-p_1)\subset pLp
\]
is finite dimensional and has identity \(p\). Equation (18), with \(p,p_1\) in place of \(e,e_1\), bounds the approximation error by \(2\|p-p_1\|_2\) plus the independently chosen matrix error. Divide by \(\sqrt{\tau_L(p)}\) for the normalized corner norm. Both errors can be arbitrarily small. Thus every nonzero corner and every finite amplification of \(L\) is locally AFD, using only finite-set approximation, trace cuts and Lemma 4.1.

Now write \(P=M\bar\otimes M_n\), \(Q=ePe\), and \(t=\tau_P(e)>0\). In \(P\bar\otimes M_r\), the projection \(e\otimes1\) has normalized trace \(t\), whereas \(1_M\otimes e_{11}\otimes e_{11}\) has trace \(1/(nr)\). Choose \(r\) so that \(1/(nr)\le t\). Comparison gives a subprojection of \(e\otimes1\) equivalent to the latter projection. Its corner, inside \(Q\bar\otimes M_r\), is isomorphic to \(M\). The local permanence just proved makes this corner locally AFD, proving the first assertion at its full stated generality. When the original factor has separable predual, so do its finite amplifications and corners. Theorem 5.1 then identifies each locally AFD corner with \(R\). \(\square\)

<a id="normal-finite-commutant"></a>

**Finite commutants of normal representations.** A faithful normal representation of \(R\), with the usual unital representation convention, has commutant isomorphic to \(R\) whenever that commutant is finite. Here is the full construction. [NA3–4](../normal-representations-and-finite-trace-corners.html#na3) realizes every normal positive coefficient by a bounded dominated form and embeds every cyclic summand into an amplification of the trace GNS space. Taking the whole orthogonal family gives an isometry \(V:L\to L^2(R)\otimes K\), with arbitrary \(K\), intertwining the representation and the left action. Its reducing range projection \(p=VV^*\) is nonzero. The full tracial conjugation and matrix-entry argument [NA0, NA5](../normal-representations-and-finite-trace-corners.html#na5) gives
\[
\rho(R)'\cong p(R^{\mathrm{op}}\bar\otimes B(K))p.
\]
Finiteness of this algebra means that \(p\) is finite in the containing matrix algebra. The diagonal trace \(\mathcal T(X)=\sum_i\tau(X_{ii})\) is faithful, normal and semifinite by the full [NA1](../normal-representations-and-finite-trace-corners.html#na1) proof. The countable-shift argument [NA2](../normal-representations-and-finite-trace-corners.html#na2) gives \(\mathcal T(p)<\infty\). If \(K\) is infinite dimensional, choose an integer \(n>\mathcal T(p)\). Factor comparison puts a projection equivalent to \(p\) under a rank-\(n\) matrix projection. If \(K\) is finite dimensional, the matrix corner is already finite. Thus \(\rho(R)'\) is a nonzero corner of \(R^{\mathrm{op}}\bar\otimes M_n\).

Compatible transposition on every local dyadic matrix level extends to a unitary of the full trace GNS space. Its conjugation carries the left algebra onto the right algebra, proving \(R^{\mathrm{op}}\cong R\) by [NA6](../normal-representations-and-finite-trace-corners.html#na6). Corollary 5.2 identifies the nonzero finite amplified corner with \(R\). That corollary's full AFD proof precedes this commutant application; the construction introduces no proof cycle.

If a representation is instead allowed a proper identity projection \(e=\rho(1)\), apply this statement on \(eL\). The full commutant on \(L\) splits as \(B((1-e)L)\oplus(\rho(R)|_{eL})'\), since commutation with \(e\) kills the two off-diagonal blocks. Finiteness forces \((1-e)L\) finite dimensional, and the active corner has commutant \(R\). A nonzero zero-action summand therefore gives \(M_d\oplus R\), rather than \(R\). This states the identity convention and its exact degenerate variant explicitly.

## Averaging over any subgroup

More generally, if \(N\subset M\) is a subfactor and \(M=N\vee(N'\cap M)\), multiplication identifies
\[
M\cong N\bar\otimes(N'\cap M).
\tag{8}
\]
For \(y\in N'\cap M\), bimodularity gives \(E_N(y)\in Z(N)=\mathbb C1\); trace preservation makes it \(\tau(y)1\). Hence \(\tau(xy)=\tau(x)\tau(y)\). On algebraic tensors, multiplication is therefore an isometry of the two trace Hilbert spaces, by expanding inner products. Its range is dense by the generation hypothesis and Kaplansky density. The resulting unitary intertwines left multiplication by each tensor leg with multiplication by its image. It implements the asserted normal spatial isomorphism.

**Lemma 2.1.** If \(G\) is any subgroup of \(\mathcal U(M)\) and \(B=G'\cap M\), then \(E_B(x)\) is the unique element of \(B\) in the ultraweakly closed convex hull of \(\{uxu^*:u\in G\}\).

**Proof.** Work in the faithful normal trace GNS model \(H=L^2(M,\tau)\) from [HF0](../components/hyperfinite-finite-algebra-and-vacuum-inputs.md#hf0), with \(\Omega=1\). For \(g\in G\), the rule \(U_g(a\Omega)=gag^*\Omega\) extends to a unitary, and \(U_g^*=U_{g^{-1}}\). We will construct bounded finite averages whose limits give the required expectation.

First fix a nonempty finite **set** \(F\subset G\); it need not be a subgroup. Define bounded operators on \(H\) by
\[
 T_F=\frac1{2|F|}\sum_{g\in F}(U_g+U_g^*),\qquad
 A_F=\frac{I+T_F}{2}.
\]
The operator \(T_F\) is selfadjoint of norm at most one, so \(0\le A_F\le I\). Moreover
\[
 \langle\eta,(I-A_F)\eta\rangle
 =\frac1{4|F|}\sum_{g\in F}\|U_g\eta-\eta\|^2.
\]
Consequently its fixed space is
\[
 H_F=\ker(I-A_F)=\bigcap_{g\in F}\ker(I-U_g).
\]

The powers of a positive contraction \(A\) converge strongly to the orthogonal projection onto \(\ker(I-A)\). Here is the elementary estimate needed for that assertion. The powers decrease in operator order; multiplying their commuting positive differences by \(I-A\) gives
\[
 0\le(n+1)A^n(I-A)
 \le\sum_{j=0}^n A^j(I-A)
 =I-A^{n+1}\le I.
\]
Thus \(\|A^n(I-A)\|\le1/(n+1)\), so the powers tend to zero on \(\operatorname{ran}(I-A)\). Uniform boundedness extends this limit to its closure. Since \(I-A\) is selfadjoint, that closure is the orthogonal complement of its kernel. On the kernel every power is the identity. This proves the strong convergence, without invoking a mean ergodic theorem. Apply it to \(A_F\), and denote the resulting projection by \(P_F\).

For the chosen \(x\in M\), write \(A_F^n(x\Omega)=a_{F,n}\Omega\). Each \(a_{F,n}\) is a finite convex combination of \(wxw^*\), \(w\in G\): expand the power of
\[
 x\longmapsto\frac{x}{2}
       +\frac1{4|F|}\sum_{g\in F}(gxg^*+g^*xg).
\]
All coefficients are nonnegative and sum to one. Hence \(\|a_{F,n}\|\le\|x\|\), and their vectors converge to \(P_F(x\Omega)\).

We use the bounded \(2\)-norm completeness explicitly. If \((z_i)\subset M\) is \(2\)-norm Cauchy and \(\|z_i\|\le C\), then
\[
 \|(z_i-z_j)b\|_2\le\|b\|\,\|z_i-z_j\|_2
 \qquad(b\in M).
\]
The left multiplication operators are therefore strongly Cauchy on the dense set \(M\Omega\); their common bound gives a bounded strong limit on all of \(H\). The trace model is strongly closed by HF0, so the limit is left multiplication by some \(z\in M\), with \(\|z\|\le C\). Its value at \(\Omega\) is the \(2\)-norm limit. This works for nets as well as sequences. On such bounded families, the trace topology (PB1)–(PB2) also gives ultraweak convergence.

It follows that \(P_F(x\Omega)=y_F\Omega\) for an element \(y_F\in M\), with \(\|y_F\|\le\|x\|\). If \(K\) denotes the ultraweakly closed convex hull in the statement, the finite averages and their bounded \(2\)-norm limit show \(y_F\in K\).

Now direct the nonempty finite subsets \(F\) of \(G\) by inclusion. The spaces \(H_F\) decrease. For a fixed vector \(\xi\in H\), set \(c=\inf_F\|P_F\xi\|^2\). If \(F\subset F'\), orthogonality of the nested projections gives
\[
 \|P_F\xi-P_{F'}\xi\|^2
     =\|P_F\xi\|^2-\|P_{F'}\xi\|^2.
\]
Choose \(F_0\) with \(\|P_{F_0}\xi\|^2<c+\varepsilon\). Comparing two supersets of \(F_0\) with their union bounds their vector difference by \(2\sqrt\varepsilon\). Thus \((P_F\xi)\) is Cauchy. Its limit lies in every \(H_F\), while \(\xi-P_F\xi\) is orthogonal to their intersection. The limit is exactly the projection of \(\xi\) onto
\[
 H_G=\bigcap_{g\in G}\ker(I-U_g).
\]
No enumeration of \(G\) is used.

Apply this to \(\xi=x\Omega\). The uniformly bounded \(y_F\) have a \(2\)-norm limit \(y\in M\), and ultraweak closedness gives \(y\in K\). Its vector is fixed by every \(U_g\), so \((gyg^*-y)\Omega=0\). Faithfulness of the trace implies \(y\in G'\cap M=B\). Every \(b\Omega\), \(b\in B\), belongs to \(H_G\). The projection characterization therefore gives
\[
 \tau(b^*y)=\tau(b^*x)\qquad(b\in B).
\]
HF0's full trace-preserving expectation has exactly these pairings, so \(y=E_B(x)\). This proves membership in the hull.

Finally, for \(b\in B\) and \(g\in G\), traciality gives \(\tau(b^*gxg^*)=\tau(b^*x)\). The same projection characterization makes \(E_B\) constant on the orbit. Its normality makes it constant on its ultraweakly closed convex hull. If \(z\in K\cap B\), then \(z=E_B(z)=E_B(x)\), proving uniqueness. The trivial subgroup is included: its averaging operators and fixed-space projection are the identity. \(\square\)

Applying the lemma to \(G=\mathcal U(N)\) proves the quantitative commutant estimate
\[
\|x-E_{N'\cap M}(x)\|_2
\le\sup_{\substack{y\in N\\\|y\|\le1}}\|[x,y]\|_2.
\tag{9}
\]
Every orbit point lies in the indicated \(2\)-norm ball around \(x\). For \(z\in M\), trace Cauchy–Schwarz and the test \(b=(z-x)/\|z-x\|_2\), when the denominator is nonzero, give
\[
 \|z-x\|_2
 =\sup_{\substack{b\in M\\\|b\|_2\le1}}
                         |\tau(b^*(z-x))|.
\]
Each pairing on the right is ultraweakly continuous. Hence the ball is ultraweakly closed and convex, contains the entire orbit, and contains its ultraweakly closed convex hull. The lemma puts the expectation in that ball and proves (9). The zero denominator gives the same identity with value zero. None of these statements requires separability.

## 6. Subfactors and automorphisms

**Lemma 6.1.** A finite von Neumann algebra generated by an increasing directed family of unital subfactors is a factor.

**Proof.** Let \(T:M\to Z(M)\) be the normal faithful center-valued trace constructed in [FCT0–7](../components/central-finite-trace-inputs.md#oa-flow.fct.0), with the full arbitrary-center proof. Every normal state \(\omega\) of \(Z(M)\) gives a normalized normal scalar trace \(\omega T\). Such center states exist and separate the center: vector functionals of any faithful concrete representation give positive normal tests, and a nonzero one is normalized by its value at the identity. No faithful scalar state on all of \(M\) is presumed.

Every normalized normal trace on \(M\) restricts to the unique normalized normal trace on each generating subfactor, by FCT7 in that finite factor. Thus any two agree on the directed union. This union is a unital star algebra; bounded strong density from Kaplansky and the vector-series tail estimate make it ultraweakly dense. Normality therefore makes the two traces agree everywhere.

In particular all the \(\omega T\)'s agree. Restriction back to \(Z(M)\), where \(T(z)=z\), makes all normal center states agree. A nonscalar center would have a nontrivial central projection \(z\); vector states supported on \(z\) and \(1-z\) give two normal states taking respectively values one and zero on \(z\). This is a contradiction. Hence \(Z(M)=\mathbb C1\), as required. \(\square\)

Every type \(\mathrm{II}_1\) von Neumann algebra, including a nonfactor or a nonseparable one, contains a unital copy of \(R\). Halve its identity to embed \(M_2\). Formula (7) identifies the relative commutant with a type \(\mathrm{II}_1\) corner. Halve there and repeat, obtaining commuting \(M_2\)'s. Their generated algebra is finite and is a factor by Lemma 6.1. It contains matrices of unbounded size, hence is type \(\mathrm{II}_1\). Its normal trace restricts to the product trace on the finite tensor levels; the trace GNS identification makes this algebra \(R\).

If the ambient algebra has separable predual, every such copy lies in a maximal AFD \(\mathrm{II}_1\) subfactor. For a chain of AFD subfactors, its generated algebra is a finite factor by Lemma 6.1. It is locally AFD: approximate a finite set by bounded elements of the chain union, choose one chain member containing those finitely many approximants, and approximate them by a finite-dimensional algebra in that member. The two errors add. Separability of the ambient predual passes to the subalgebra, so Theorem 5.1 identifies this upper bound with \(R\). Zorn's lemma now supplies a maximal member. No maximality assertion here identifies the ambient algebra with that member.

### Automorphisms on finite levels and a distant tensor leg

**Lemma 6.2.** If \(A\cong M_d\) is a unital subfactor of any von Neumann algebra \(P\), then for every automorphism \(\alpha\) of \(P\) there is a unitary \(u\in P\) satisfying \(\alpha|_A=\operatorname{Ad}(u)|_A\).

**Proof.** Let \(e_{ij}\) be its matrix units. The projections \(e_{ii}\) are \(d\) equivalent pieces of one, and so are \(\alpha(e_{ii})\). [PC5](../components/central-finite-trace-inputs.md#oa-flow.projection.pc5) gives the unique finite/properly infinite central split. An automorphism preserves it, since it preserves projection equivalence, finiteness, centrality and their suprema.

On the finite central part, [FCT7](../components/central-finite-trace-inputs.md#oa-flow.fct.7) gives the normal center-valued trace, its equivalence criterion. The \(d\) equivalent diagonals sum to the central identity, so all their trace values are that identity divided by \(d\). The images have the same values. Thus \(e_{11}\sim\alpha(e_{11})\) there.

On the properly infinite central part, \(e_{11}\) is properly infinite. Indeed its central support is the whole part, since its \(d\) equivalent diagonals sum to that identity. By [PC4](../components/central-finite-trace-inputs.md#oa-flow.projection.pc4), every central projection in its corner is the compression of an ambient central projection. A nonzero finite such cut would make the sum of its \(d\) equivalent diagonal cuts finite by [PC6](../components/central-finite-trace-inputs.md#oa-flow.projection.pc6), contrary to proper infiniteness of the central summand.

The full halving proof in PC5 permits finitely many orthogonal copies of \(e_{11}\) inside \(e_{11}\): iterate to \(2^k\ge d\) equivalent copies and retain \(d\). Match the \(d\) old diagonals to those copies and add the implementations. This gives the central identity subequivalent to \(e_{11}\). The reverse subequivalence is inclusion, so [PC3](../components/central-finite-trace-inputs.md#oa-flow.projection.pc3) gives \(e_{11}\sim1\) on that part. Apply the same argument to \(\alpha(e_{11})\). Adding the central implementations gives a partial isometry \(w\) with \(w^*w=e_{11}\), \(ww^*=\alpha(e_{11})\). Then
\[
u=\sum_{i=1}^d\alpha(e_{i1})w e_{1i}
\tag{19}
\]
is unitary, and multiplication gives \(ue_{ij}u^*=\alpha(e_{ij})\). \(\square\)

**Theorem 6.3.** Every automorphism of \(R\) is a limit of inner automorphisms in the point-predual norm topology, and \(R\) has outer automorphisms.

**Proof.** For \(\alpha\in\operatorname{Aut}(R)\), apply Lemma 6.2 on the initial dyadic algebra \(A_n\), obtaining \(u_n\). Uniqueness of the trace makes \(\alpha\) a \(2\)-norm isometry. Thus
\[
\|\alpha(x)-u_nxu_n^*\|_2
\le2\|x-E_{A_n}(x)\|_2\longrightarrow0.
\tag{20}
\]
The expectations converge in \(L^2\) because the finite tensor vectors are dense. The inverse automorphisms converge in \(2\)-norm too: for \(\alpha_n=\operatorname{Ad}(u_n)\),
\[
\|\alpha_n^{-1}(b)-\alpha^{-1}(b)\|_2
=\|b-\alpha_n(\alpha^{-1}(b))\|_2\to0.
\]
For \(\psi_b=\tau(b\,\cdot)\), trace preservation gives \(\psi_b\circ\alpha_n-\psi_b\circ\alpha=\tau((\alpha_n^{-1}(b)-\alpha^{-1}(b))\,\cdot)\). On the operator unit ball, Cauchy–Schwarz bounds its norm by \(\|\alpha_n^{-1}(b)-\alpha^{-1}(b)\|_2\), tending to zero. The norm density (PB1) and the automorphisms' uniform predual isometry bounds give convergence for every normal functional. This is the stated topology.

For an outer example, take \(Z=\operatorname{diag}(1,-1)\) and the product automorphism \(\bigotimes_j\operatorname{Ad}(Z)\). It preserves the product trace. Here is a direct proof of outerness. Write \(X=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), and let \(X_k\) be this unitary in tensor leg \(k\). The product automorphism sends \(X_k\) to \(-X_k\), since \(ZXZ=-X\). If it were \(\operatorname{Ad}(u)\), then \(uX_k=-X_ku\) and \(\|[u,X_k]\|_2=2\). On the other hand \(b_n=E_{A_n}(u)\) converges to \(u\) in \(2\)-norm, and for \(k>n\) it commutes with \(X_k\). Therefore
\[
2=\|[u,X_k]\|_2
 =\|[u-b_n,X_k]\|_2\le2\|u-b_n\|_2\longrightarrow0,
\tag{OA1}
\]
a contradiction. The zero overlaps \(|\operatorname{tr}_2(Z)|\) also agree with the preceding lesson's product criterion. The finite prefix implementations converge as in (20). \(\square\)

<a id="7-problems-with-complete-solutions"></a>

## Problems with complete solutions

**Exercise 1.** For two rank-one projections in \(M_2\) whose ranges make angle \(\theta\in[0,\pi/2]\), compare the \(2\)-norms of their difference and of the planar rotation minus one, using normalized trace.

*Solution.* In an orthonormal planar basis take \(e=\operatorname{diag}(1,0)\), \(f\) onto \((\cos\theta,\sin\theta)\), and \(u=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}\). Then \((e-f)^2=\sin^2\theta\,1\) and \((u-1)^*(u-1)=2(1-\cos\theta)1\). Thus \(\|e-f\|_2=\sin\theta\), \(\|u-1\|_2=2\sin(\theta/2)\), and (2) follows from \(1-\cos\theta\le\sin^2\theta\). At \(\theta=\pi/2\) its constant is attained.

**Exercise 2.** Let \(h=\operatorname{diag}(1/10,4/5)\) in \(M_2\). Calculate the nearest spectral projection and verify (5)'s first inequality.

*Solution.* The projection is \(q=\operatorname{diag}(0,1)\). One has \(\|h-q\|_2^2=(1/100+1/25)/2=1/40\), whereas \(\|h-h^2\|_2^2=((9/100)^2+(4/25)^2)/2=337/20000\). Hence \(1/40\le4(337/20000)\), as required. The cutoff is applied to the spectrum of \(h\), not to its matrix entries in an arbitrary basis.

**Exercise 3.** A unital \(M_3\subset M\) has minimal projection trace \(1/3\). Explain why it cannot be contained exactly in a unital dyadic matrix subfactor, and why Lemma 3.1 still approximates it.

*Solution.* A unital embedding \(M_3\to M_{2^p}\) would require \(2^p=3r\), by (7), which is impossible. For approximation choose \(r=\lfloor2^p/3\rfloor\), truncate each diagonal to trace \(r2^{-p}\), and retain the \(3r\) connected dyadic pieces. Each matrix-unit error has squared \(2\)-norm below \(2^{-p}\), and the unused dyadic pieces complete the full matrix algebra. Exact containment and arbitrarily good approximation have different divisibility requirements.

**Exercise 4.** Why does the proof of Lemma 4.1 approximate all the corner entries \(e_{1i}xe_{j1}\), rather than only \(x\)?

*Solution.* The aligning unitary \(v\) need not be close to one on the whole algebra. Its restriction to the first corner agrees with the controlled \(u\). The \(d^2\) corner entries have that common control, and multiplication by the old \(e_{i1},e_{1j}\), which lie exactly in the new algebra, reconstructs the approximation to \(x\). Approximating only \(x\) would supply no estimate for its conjugate by the uncontrolled \(v\).

**Exercise 5.** In a corner of trace \(1/9\), convert an ambient \(2\)-norm error \(1/300\) to the normalized corner \(2\)-norm.

*Solution.* Divide the squared norm by \(1/9\), so multiply the norm by \(3\). The answer is \(1/100\). This normalization is a square-root factor, as in (18).

**Exercise 6.** Prove that \(R\bar\otimes M_3\cong R\), although \(3\) divides no \(2^p\).

*Solution.* The increasing algebras \(M_{2^p}\otimes M_3\) generate a separable finite factor and make it locally AFD. It is infinite dimensional, hence type \(\mathrm{II}_1\). Theorem 5.1 identifies it with \(R\). The proof permits approximating those \(3\cdot2^p\)-dimensional matrix factors by different dyadic factors; it does not put them exactly into a fixed dyadic tensor level.

**Exercise 7.** Show that the finiteness hypothesis in Lemma 6.1 is necessary, using the direct sum of the CAR vacuum and tracial representations.

*Solution.* In the vacuum representation, the average \(q_n=n^{-1}\sum_{j\le n}a_j^*a_j\) converges strongly to zero on finite occupation vectors, hence everywhere by boundedness. In the tracial representation, independence gives \(\|(q_n-1/2)\Omega\|_2^2=1/(4n)\). For a fixed local polynomial \(x\), all but finitely many occupation projections commute with \(x\), so \(\|[q_n,x]\|\to0\). Thus \(q_nx\Omega\to x\Omega/2\); boundedness and local cyclic density give the strong limit \(1/2\).

On the direct sum the strong limit is \(0\oplus(1/2)1\), giving a nontrivial central projection. The local CAR algebras are still increasing full matrix subfactors. Their closure is \(B(\mathcal F(K))\oplus R\): the central projection separates the summands and each component has that closure. It is not finite because the infinite-dimensional \(B(\mathcal F(K))\) summand is properly infinite. This exhibits the source's finite-versus-infinite distinction directly.

**Exercise 8.** For \(R\bar\otimes R\), prove the isomorphism with \(R\) without an injectivity-to-AFD theorem.

*Solution.* Its initial tensor levels are \(M_{2^n}\otimes M_{2^n}\cong M_{2^{2n}}\); they form an increasing sequence whose union generates the spatial tensor product. Its product trace is faithful and normal, and it is a factor by the tensor commutation theorem. It is infinite dimensional and has separable predual. Theorem 5.1 therefore gives \(R\bar\otimes R\cong R\). Interleaving the two sequences of \(M_2\) factors gives the same trace GNS isomorphism directly.

**Exercise 9.** For the outer automorphism in Theorem 6.3, write explicit inner approximants and estimate their error on an arbitrary \(x\in R\).

*Solution.* Put \(u_n=Z^{\otimes n}\otimes1\). Its adjoint action agrees with the product automorphism on \(A_n\). Both maps preserve the trace, so their difference on \(x\) is at most \(2\|x-E_{A_n}(x)\|_2\), tending to zero. The product innerness criterion excludes a global inner implementation, since its overlap-defect sum is \(\sum_j1\).

**Exercise 10.** Prove that every factor of type \(\mathrm{II}_1\) contains a unital \(M_7\), and explain why it also contains a unital \(R\).

*Solution.* Cut its identity into seven projections of trace \(1/7\). They are equivalent, so connecting them to a common reference constructs full unital \(7\)-matrix units. For \(R\), use successive halvings in the relative commutants of the already chosen dyadic matrix factors, as in Section 6. The increasing union has factorial finite closure by Lemma 6.1, unbounded matrix sizes, and the product trace. It is the tracial GNS model of \(R\), regardless of the ambient factor's own separability or AFD status.

## References and continuation

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft. Lemma 11.2.1 and Theorem 11.2.2, printed pp.185–188, develop dyadic matrix approximation and trace-GNS identification with \(R\). Their containment induction uses amenability to obtain AFD corners. Sections 3–5 above instead give exact containment and local corner permanence directly from finite-set approximation, with no injectivity assumption and no separability needed for the local permanence argument. Separability is used only for the generating sequence and identification with \(R\).

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://numdam.org/item/ASENS_1975_4_8_3_383_0.pdf), *Annales scientifiques de l’École Normale Supérieure*, series 4, 8 (1975), 383–419, DOI [10.24033/asens.1295](https://doi.org/10.24033/asens.1295). Lemmas 1.1.4–1.1.5, printed pp.388–389, develop projection repair and spectral rounding. The finite direct rotation above supplies a unitary and the stronger operator bound (2), including its exceptional orthogonal supports, for an arbitrary finite algebra. Equations (5), (6) and (6a) give the complete state spectral estimates.

The exact foundational inputs remain center-valued trace comparison, type II halving, projection support, normal representation amplification and trace densities. The finite trace expectations onto all unital subalgebras are constructed directly in [HF0](../components/hyperfinite-finite-algebra-and-vacuum-inputs.md#hf0), and (PB1)–(PB2) prove the bounded trace topology and predual density used here. The general center-trace and arbitrary properly infinite projection arguments use the full local FCT0–7 and PC0–7 proofs linked above, including their exact scalar/spectral/predual inputs. The whole normal representation amplification and canonical semifinite finite-projection criterion are proved in [NA0–6](../normal-representations-and-finite-trace-corners.html#na0), including arbitrary multiplicity, all-net trace normality and the full finite matrix-corner reduction. The later finite outer-action and central-sequence arguments have their own prerequisites.

Jesse Peterson, [*Notes on operator algebras*, April 27, 2020](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), printed/PDF pp.83–90 and102–107. The general projection and approximate-center-trace methods are written there. PC1–7 and FCT0–7 supply full arbitrary sums, central supports, finite cancellation, central tilings and normal assemblies. FCT0 also corrects the complex norm estimate in the source’s Lemma6.4.5; FCT5 retains both factors of its distortion parameter, and FCT6 uses the intended \(xx^*/x^*x\) inequality throughout. These are full general finite proofs, beyond the tracial comparison in the Anantharaman–Popa draft.

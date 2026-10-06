# Exact trace certificates close the finite-depth residual

Lesson 76 constructs a finite commuting square whose selected whole-tunnel blocks cover trace arbitrarily close to one. Its remaining corner is retained, so all approximation and expectation identities are exact, but that corner does not yet have a whole-tunnel origin. Here we prove an exact trace criterion for giving it such an origin. We then prove that finite depth supplies the criterion automatically. The resulting partition is finite and sums exactly to one.

Throughout, \(N\subset M\) is a proper finite-index inclusion of II₁ factors, \(d=[M:N]>1\), with normalized trace \(\tau\). For the approximation results we assume the relative amenability hypothesis used in 74–76. The trace criterion itself requires no amenability or finite depth. A different finite tunnel continuation is permitted for each supported summand. This is the endpoint in Sorin Popa, [*Classification of amenable subfactors of type II*](https://doi.org/10.1007/BF02392646), Theorem 4.4.1(1), printed p.222. A common ordinary stage and a generating tunnel require additional arguments.

Our exact existing inputs are [4.2–4.5 (actual tunnel triples)](towers-and-tunnels.md), [8.1 (finite matrix decomposition and inherited traces)](finite-dimensional-markov-calculus.md), [12.1–12.3 (relative-commutant inclusion matrices)](higher-relative-commutants.md), [14.3–14.4 (finite-depth primitive tails and trace-preserving reflection)](reflected-traces-and-uniform-bounds.md), [57.3 (finite tunnel alignment)](actual-supported-local-approximation.md), and [76.4 (the entire finite square with its retained residual)](whole-relative-commutant-blocks.md). Projection comparison in a II₁ factor and the finite-dimensional Perron theorem have the precise programme scope already used in those proofs. The rank, residual-extension and positivity arguments needed here are written out below. No common-support BF or second central local form is assumed.

## The trace must occur at a finite stage

Fix one actual tunnel \(N=N_0\supset N_1\supset\cdots\), and set

\[
\begin{gathered}
B_j=N_j'\cap N,\\
A_j=N_j'\cap M,\\
B_j=\bigoplus_{\ell=1}^{s_j}\operatorname{Mat}_{n_{j\ell}}.
\end{gathered}
\tag{78.1}
\]

Let \(\omega_{j\ell}>0\) be the actual \(\tau\)-trace of a minimal projection in the \(\ell\)-th block of \(B_j\). These are not normalized block traces. The identity has trace one, so

\[
\begin{gathered}
\sum_\ell n_{j\ell}\omega_{j\ell}=1,\\
T_j=\left\{\sum_\ell\omega_{j\ell}h_\ell\right\},\\
\text{with }h_\ell\in\mathbb Z,\\
0\leq h_\ell\leq n_{j\ell},\\
T=\bigcup_{j\geq0}T_j.
\end{gathered}
\tag{78.2}
\]

**Lemma 78.1.** The set of projection traces in \(B_j\) is exactly \(T_j\). The sets \(T_j\) increase with \(j\), and are unchanged by choosing a different tunnel of the same finite length.

**Proof.** A projection in a full matrix block is unitarily diagonalizable, with an integer rank between zero and the block size. Its trace is its rank times the trace of a minimal projection. Summing the block contributions gives 78.2. Conversely, choose diagonal projections with the specified ranks to realize every listed value. The inclusion \(B_j\subset B_{j+1}\) takes projections to projections without changing their ambient trace. Thus \(T_j\subset T_{j+1}\). For another tunnel, 57.3 gives a unitary in \(N\) conjugating the entire finite segment, hence its finite smaller relative commutant. Conjugation preserves \(\tau\). This identifies the two sets of projection traces, including their actual inherited weights. \(\square\)

**Theorem 78.2 — exact placement.** For a projection \(f\in N\), the following are equivalent:

1. There is an actual finite tunnel of \(N\subset M\) with \(f\) in its smaller finite relative commutant.
2. \(\tau(f)\in T\).

More precisely, a certificate at stage \(j\) places \(f\) at that same finite length, after conjugating the fixed tunnel by a unitary in \(N\).

**Proof.** If the first condition holds, finite alignment and Lemma 78.1 put \(\tau(f)\) in the fixed \(T_j\). Conversely, choose \(g\in B_j\) with \(\tau(g)=\tau(f)\). Projection comparison supplies a partial isometry from \(g\) to \(f\), and another from \(1-g\) to \(1-f\). Their sum is a unitary \(u\in N\), with

\[
\begin{gathered}
ugu^*=f,\\
\widetilde N_i=uN_i u^*,\\
\widetilde B_j=uB_ju^*,\\
\widetilde A_j=uA_ju^*.
\end{gathered}
\tag{78.3}
\]

Conjugating all factors and defining cups preserves the actual basic-construction relations, so this is an actual finite tunnel of the original inclusion. Indeed, \(uNu^*=N\) and \(uMu^*=M\). Its smaller algebra contains \(f\). For \(f=0\) or \(1\), use the corresponding canonical projection and the identity unitary. No physical target element is conjugated. \(\square\)

The criterion concerns membership in \(\widetilde B_j\), not membership merely in a tail factor or in its commutant. Membership of a scalar in the additive group generated by \(T\) is also insufficient by itself. The integer ranks must fit the actual block sizes.

## Enlarge only the retained residual

Apply 76.4 at \(k=0\) to finite \(Y\subset M\) and \(\varepsilon>0\). Write its selected whole-stage blocks and retained residual as

\[
\begin{gathered}
r_ir_h=0\quad(i\ne h),\\
f=1-\sum_{i=1}^{q}r_i\in N,\\
P_0=\left(\bigoplus_{i=1}^{q}P_i\right)\oplus fA_0,\\
Q_0=\left(\bigoplus_{i=1}^{q}Q_i\right)\oplus\mathbb C f,\\
A_0=N'\cap M,\\
P_i=r_iA_{m_i}^{(i)}r_i,\\
Q_i=r_iB_{m_i}^{(i)}r_i,\\
r_i\in B_{m_i}^{(i)}.
\end{gathered}
\tag{78.4}
\]

The superscript records the individual actual continuation used on that piece. Zero residual summands are omitted. The finite square satisfies

\[
\begin{gathered}
A_0\subset P_0,\\
E_N(P_0)=Q_0,\\
E_NE_{P_0}=E_{Q_0},\\
\|y-E_{P_0}(y)\|_2<\varepsilon
\quad(y\in Y).
\end{gathered}
\tag{78.5}
\]

**Theorem 78.3 — residual extension.** If the physical residual in 78.4 satisfies \(\tau(f)\in T\), there are unital finite-dimensional \(Q_*\subset P_*\subset M\) with \(Q_*\subset N\), a finite full support partition, and all the properties in 78.5. Every supported summand of \(Q_*\subset P_*\) is the full supported pair of an actual whole-inclusion finite tunnel. Moreover, \(P_0\subset P_*\), \(Q_0\subset Q_*\), and every selected old block is retained exactly.

**Proof.** If \(f=0\), take the original square. Otherwise use Theorem 78.2, and set

\[
\begin{gathered}
P_f=f\widetilde A_j f,\\
Q_f=f\widetilde B_j f,\\
P_*=\left(\bigoplus_iP_i\right)\oplus P_f,\\
Q_*=\left(\bigoplus_iQ_i\right)\oplus Q_f.
\end{gathered}
\tag{78.6}
\]

Each new block has identity its indicated support. Orthogonality to all \(r_i\) therefore makes these genuine finite-dimensional direct sums, with common identity one. Because \(u\in N\), it fixes \(A_0\) pointwise. Also \(A_0\subset A_j\). Consequently \(A_0\subset\widetilde A_j\), and \(f\in N\) commutes with \(A_0\). Thus \(fA_0\subset P_f\) and \(\mathbb C f\subset Q_f\). All other summands are unchanged, proving the two containments and retention of \(A_0\).

The actual finite-stage identity \(E_N(A_j)=B_j\), equivariance under \(u\in N\), and bimodularity over \(f\in N\) give

\[
\begin{gathered}
E_N(\widetilde A_j)=\widetilde B_j,\\
E_N(P_f)=Q_f,\\
E_N(P_*)=Q_*.
\end{gathered}
\tag{78.7}
\]

Here the last equality uses the same identity on every retained block. To verify the complete commuting square, \(E_NE_{P_*}(x)\) lies in \(Q_*\); for \(b\in Q_*\subset P_*\cap N\), trace pairing gives

\[
\begin{gathered}
\tau(b^*E_NE_{P_*}(x))=\tau(b^*x),\\
E_NE_{P_*}=E_{Q_*},\\
E_{P_*}E_N=E_{Q_*}.
\end{gathered}
\tag{78.8}
\]

The first identity characterizes the tracial expectation onto \(Q_*\); taking Hilbert-space adjoints gives the final one. Since \(P_0\subset P_*\), best approximation in \(L^2(M,\tau)\) gives

\[
\begin{gathered}
\|y-E_{P_*}(y)\|_2\\
\leq\|y-E_{P_0}(y)\|_2<\varepsilon.
\end{gathered}
\tag{78.9}
\]

The supports are the finite family \(r_1,\ldots,r_q,f\), omitting zero projections, and they sum exactly to one. Only the new residual tunnel was conjugated. The old blocks and physical targets did not move. \(\square\)

This theorem retains the initial relative commutant \(A_0\) exactly. It does not assert retention of an arbitrary higher prefix by the new unitary, which so far belongs only to \(N\).

## Positive scalar trace becomes valid ranks in a primitive tail

We isolate the order argument, including its normalization. Let a stationary finite-dimensional system have an integer matrix \(C\geq0\), with rows indexed by target blocks and columns by source blocks. For block-size columns \(n_k\), unital embeddings give

\[
\begin{gathered}
F_k=\bigoplus_{\ell=1}^{s}\operatorname{Mat}_{n_{k\ell}},\\
n_k=C^kn_0,\\
C^{\mathsf T}\omega=\rho\omega,\\
\omega>0,\qquad\omega\cdot n_0=1,\\
\omega_k=\rho^{-k}\omega.
\end{gathered}
\tag{78.10}
\]

The vector \(\omega_k\) is the minimal-projection trace vector at level \(k\). Its restriction obeys \(C^{\mathsf T}\omega_{k+1}=\omega_k\), and \(\omega_k\cdot n_k=1\).

**Lemma 78.4 — primitive rank promotion.** Suppose \(C\) is primitive: some positive power has every entry strictly positive. For any signed integer vector \(v\) with

\[
0< t=\omega\cdot v<1,
\tag{78.11}
\]

there is a finite \(k\) for which \(C^kv\) is a valid projection-rank vector in \(F_k\). Its trace is exactly \(t\). In particular, the finite projection traces in this system are the intersection of their additive group with \([0,1]\).

**Proof.** Let \(a>0\) be a right Perron vector of \(C\). The finite primitive Perron theorem, in its matrix convergence form, says

\[
\begin{gathered}
\rho^{-k}C^k\longrightarrow
\frac{a\omega^{\mathsf T}}{\omega\cdot a},\\
\rho^{-k}C^kv\longrightarrow
\frac{t a}{\omega\cdot a},\\
\rho^{-k}C^k(n_0-v)\longrightarrow
\frac{(1-t)a}{\omega\cdot a}.
\end{gathered}
\tag{78.12}
\]

This is the same primitive convergence used in 14.3; linearity extends its finite-column statement to every signed vector. Both limiting vectors in the last two lines have strictly positive coordinates. There are finitely many coordinates, so both vectors on the left are coordinatewise positive for all sufficiently large \(k\). Integer matrix multiplication keeps them integral. Therefore

\[
\begin{gathered}
0\leq C^kv\leq C^kn_0=n_k,\\
\omega_k\cdot C^kv
=\rho^{-k}\omega\cdot C^kv=t.
\end{gathered}
\tag{78.13}
\]

The inequalities are coordinatewise. Diagonal projections with these ranks give the claimed finite projection and exact trace. No approximation of the trace is involved.

An element of the additive group generated by finite projection traces is a finite signed integer combination of them. Move all its projections to one common level by the actual embeddings. Their signed sum of rank vectors is an integer vector there. Apply the argument just proved, with that level as the new initial level. This realizes every group element strictly between zero and one. For the endpoints zero and one use the zero and identity projections; no positivity of the original signed vector at those endpoints is asserted. The reverse inclusion is immediate from the definition of the group. \(\square\)

**Corollary 78.5 — a residual rank certificate.** Choose finitely many canonical finite-stage projections \(g_i\), representing the traces of physically disjoint selected supports \(r_i\). Move the \(g_i\) to one common late level with block-size vector \(n\) and minimal weights \(\omega\). If their rank vectors are \(h_i\), put

\[
\begin{gathered}
v=n-\sum_i h_i,\\
\omega\cdot v=1-\sum_i\tau(r_i)=\tau(f).
\end{gathered}
\tag{78.14}
\]

If \(0\leq v\leq n\), this is already a finite certificate. Otherwise a primitive stationary continuation supplies a finite certificate whenever \(0<\tau(f)<1\). The scalar endpoints have their usual certificates.

**Proof.** Finite alignment gives the individual \(g_i\) when each selected support has a whole-stage origin. Their embeddings preserve trace. Lemma 78.1 proves the first assertion, and Lemma 78.4 proves the promoted one. The canonical \(g_i\) need not be orthogonal to each other: they represent separate traces. Only the physical \(r_i\) are known to be disjoint. Thus \(v\) can have negative coordinates even though its scalar trace is positive. Promotion is exactly the step that repairs this possible defect. \(\square\)

## Finite depth supplies the certificate

**Theorem 78.6 — exact finite-depth whole-stage partition.** Suppose the proper inclusion is relatively amenable and has finite depth. For every finite \(Y\subset M\) and \(\varepsilon>0\), there is a unital finite-dimensional commuting square \(Q_*\subset P_*\) approximating \(Y\) within \(\varepsilon\) in \(L^2\). Its finitely many supports sum to one, and each supported pair is the full pair of finite relative commutants of an actual whole tunnel, compressed by a projection in its smaller algebra. It retains \(A_0\) exactly. This proves the finite-depth case of Popa 4.4.1(1) from the general approximation in 76.4.

**Proof.** First identify the stationary system for the actual smaller algebras \(B_j\), with their actual traces. In the two-sided tower convention \(N_j=M_{-j-1}\), reflection 14.3 with \(b=1\) gives

\[
\Theta(B_j)=M_1'\cap M_{j+1}.
\tag{78.15}
\]

Theorem 14.4 proves trace preservation on this domain. Applied twice, its dual-depth assertion makes the shifted inclusion \(M_1\subset M_2\) finite depth as well. The algebras on the right of 78.15 are precisely its upward relative-commutant sequence, after shifting the level label. Thus, after the last new vertex and at either fixed parity, their two-step inclusion matrix is

\[
\begin{gathered}
C=GG^{\mathsf T}\quad\text{or}\quad G^{\mathsf T}G,\\
n_{j+2}=Cn_j,
\end{gathered}
\tag{78.16}
\]

for the finite connected bipartite graph of that shifted inclusion. The actual anti-isomorphism preserves block sizes, ranks and ambient traces. It therefore gives these same matrices for the downward smaller algebras; abstract normalized block weights have not been substituted for the inherited trace.

Every two vertices on the same parity are connected by an even path, and every vertex has positive degree. The two-step graph is connected and its matrix has positive diagonal. Extend paths by diagonal steps to one common sufficiently large length; every entry of that power is positive. Hence \(C\) is primitive.

The exact trace calculation in 14.3 says that the minimal-projection weights of this finite-depth stationary tail lie on its positive Perron ray. Normalize at one chosen late level by \(\omega\cdot n=1\). If \(\rho\) is the Perron eigenvalue, compatibility and normalization give weights \(\rho^{-k}\omega\) at the successive two-step levels. Indeed, the next weights are on the same ray, and \(C^{\mathsf T}\omega=\rho\omega\) forces the scale \(\rho^{-1}\) under restriction. This is exactly the system in 78.10.

Now take the finite square 76.4 at \(k=0\). Every selected support has a whole-stage origin, so Lemma 78.1 and finite alignment put its trace in \(T\). Represent all these traces in one fixed canonical \(B_j\), then move to a late level of one parity. This is possible because the sequence is increasing. Construct the signed vector \(v\) in 78.14. The physical residual has \(0\leq\tau(f)\leq1\), so Lemma 78.4 and the endpoint convention give

\[
\tau(f)\in T.
\tag{78.17}
\]

Theorem 78.3 now replaces its retained corner by a whole-stage block, preserves the old finite square as a subalgebra, and preserves or improves every approximation bound. The family stays finite and its identity is exactly one. \(\square\)

The conclusion permits different continuations for different pieces. It does not identify the final supports with projections in a single common ordinary stage, produce a nested sequence of these squares, or prove the unrestricted generating-tunnel endpoint. Outside finite depth, Theorem 78.3 is still valid, but automatic existence of its trace certificate has not been proved here.

## Why scalar subtraction alone does not suffice

**Example 78.7 — a reducible finite-stage diagnostic.** Put \(\alpha=\sqrt2/2\). Consider the unital system

\[
\begin{gathered}
F_k=\operatorname{Mat}_{2^k}\oplus\operatorname{Mat}_{2^k},\\
\tau_k(x,y)\\
=\alpha\operatorname{tr}_{2^k}(x)\\
\quad+(1-\alpha)\operatorname{tr}_{2^k}(y),\\
C=2I_2.
\end{gathered}
\tag{78.18}
\]

Each summand embeds into its successor by duplicating its defining representation. The traces are compatible. This system can be realized in a II₁ factor \(N\): choose orthogonal corner identities of traces \(\alpha,1-\alpha\), and recursively construct unital dyadic matrix units in each corner. Their minimal traces are the indicated corner trace divided by \(2^k\).

The canonical projection \(p=(0,1)\in F_0\) has trace \(1-\alpha\). In the ambient factor choose \(r_1=p\), and \(r_2\leq1-r_1\) of the same trace; this is possible because \(2(1-\alpha)<1\). Projection comparison makes \(r_2\) an \(N\)-unitary conjugate of \(p\). The two physical projections are disjoint, while

\[
\begin{gathered}
f=1-r_1-r_2,\\
\tau(f)=2\alpha-1\\
=\sqrt2-1\in(0,1).
\end{gathered}
\tag{78.19}
\]

There is no projection of this trace in any \(F_k\). Such a projection with ranks \(h_0,h_1\) would require

\[
\begin{gathered}
2\alpha-1
=\frac{h_1}{2^k}
+\alpha\frac{h_0-h_1}{2^k},\\
0\leq h_0,h_1\leq2^k.
\end{gathered}
\tag{78.20}
\]

Rational independence of \(1,\alpha\) would give \(h_1/2^k=-1\), contradicting nonnegativity. The signed canonical vector and all its promotions are

\[
\begin{gathered}
v=(1,-1)^{\mathsf T},\\
C^kv=(2^k,-2^k)^{\mathsf T}.
\end{gathered}
\tag{78.21}
\]

Thus each selected trace has a finite certificate, their physically disjoint sum has trace less than one, and the residual lies in their additive trace group, but it has no finite certificate. The matrix is not primitive. This is an abstract finite-dimensional-system diagnostic, not an actual Jones-core or subfactor counterexample. It isolates why the scalar arithmetic alone does not prove the general residual claim.

**Example 78.8 — one-step repair in a primitive system.** Take

\[
\begin{gathered}
C=\begin{pmatrix}2&1\\1&2\end{pmatrix},\\
n_0=(1,1)^{\mathsf T},\\
\omega=(1/2,1/2)^{\mathsf T},\\
\rho=3,\qquad v=(-1,2)^{\mathsf T}.
\end{gathered}
\tag{78.22}
\]

The signed vector has trace \(1/2\), and

\[
\begin{gathered}
Cv=(0,3)^{\mathsf T},\\
n_1=(3,3)^{\mathsf T},\\
C^2v=(3,6)^{\mathsf T},\\
n_2=(9,9)^{\mathsf T},\\
\omega_1=(1/6,1/6)^{\mathsf T},\\
\omega_2=(1/18,1/18)^{\mathsf T}.
\end{gathered}
\tag{78.23}
\]

The first promoted vector already fits its capacities. The second is strictly inside both capacities. Both traces are exactly \(1/2\). This is a worked stationary matrix system; no particular rooted subfactor realization of it is claimed.

![An exact trace certificate replaces the residual; primitive rank promotion succeeds while a reducible diagnostic fails.](figures/trace-certificates-and-exact-finite-partitions.svg)

*Figure 78.1. The first two panels retain the actual inherited minimal weights, the physical support and the old finite square in 78.2–78.9. The third gives every rank, capacity and trace in Example 78.8. The fourth gives the irrational trace and persistent negative coordinate in Example 78.7. The colored block widths in the residual panel are schematic, not trace measurements. The matrix examples are abstract diagnostics, not asserted subfactor models. [Reproducible source](figures/trace-certificates-and-exact-finite-partitions.py). Human source for the required endpoint: Sorin Popa, [*Classification of amenable subfactors of type II*](https://doi.org/10.1007/BF02392646), Theorem 4.4.1(1), printed p.222.*

## Exercises with complete solutions

**Exercise 78.1 — use the actual weights.** Let \(B=\operatorname{Mat}_2\oplus\operatorname{Mat}_3\), with minimal-projection weights \(1/8,1/4\). Verify normalization and find every rank certificate for trace \(5/8\). Explain why replacing both minimal weights by \(1/5\) changes the problem.

**Solution.** The identity has trace \(2/8+3/4=1\). Ranks must satisfy \(h_0+2h_1=5\), with \(0\leq h_0\leq2\) and \(0\leq h_1\leq3\). For \(h_1=0,1,2,3\), the corresponding \(h_0\) is \(5,3,1,-1\); only \((h_0,h_1)=(1,2)\) is valid. A projection of trace \(5/8\) in an ambient factor can therefore be placed in a conjugate of this algebra by a unitary in that factor. The substituted equal weights would give only integral multiples of \(1/5\), none equal to \(5/8\). The inherited trace, not total matrix dimension, determines the certificate.

**Exercise 78.2 — retain the old square.** Suppose 78.4 has a residual with a finite certificate. Prove that adjoining its whole-stage block keeps the approximation to each physical \(y\) and gives both orders of the commuting-square expectation identity. Which operators does the unitary fix?

**Solution.** Choose a canonical projection of exactly the residual trace, and let an \(N\)-unitary carry it onto the physical \(f\). Conjugate only its tunnel. Because \(A_0=N'\cap M\), this unitary fixes every element of \(A_0\); the conjugated larger finite algebra still contains \(A_0\). Multiplication by \(f\) therefore puts \(fA_0\) inside its supported algebra. This proves \(P_0\subset P_*\), so orthogonal projection onto \(L^2(P_*)\) has no greater error on the unchanged \(y\). On each block, bimodularity and finite-stage expectation give \(E_N(P_*)=Q_*\). Pair \(E_NE_{P_*}(x)\) with every \(b\in Q_*\); both expectations fix \(b\), so the pairing is \(\tau(b^*x)\). Uniqueness gives \(E_NE_{P_*}=E_{Q_*}\); adjoints give \(E_{P_*}E_N=E_{Q_*}\). The selected old blocks remain fixed by construction; the proof does not conjugate them or the targets, and does not assert that the new unitary fixes a higher prescribed prefix.

**Exercise 78.3 — compute promotion exactly.** For 78.22, compute \(C^kv\), \(C^kn_0\), and the trace for arbitrary \(k\). Find the first level at which both the vector and its complement are strictly positive.

**Solution.** The vectors \((1,1)^{\mathsf T}\) and \((1,-1)^{\mathsf T}\) have eigenvalues three and one. Since \(v=\tfrac12(1,1)^{\mathsf T}-\tfrac32(1,-1)^{\mathsf T}\), we have \(C^kv=((3^k-3)/2,(3^k+3)/2)^{\mathsf T}\) and \(C^kn_0=(3^k,3^k)^{\mathsf T}\). The complement is \(((3^k+3)/2,(3^k-3)/2)^{\mathsf T}\). At \(k=0\) one rank is negative; at \(k=1\) a rank and a complementary rank are zero; at \(k=2\) all four are positive. With weights \((1/(2\cdot3^k),1/(2\cdot3^k))^{\mathsf T}\), the trace of the signed vector, and of every valid promoted projection, is exactly \(1/2\).

**Exercise 78.4 — why positivity of the scalar is insufficient.** Prove all inequalities needed to choose the two physical projections in Example 78.7, and prove the residual has no canonical finite certificate. Does this example refute the actual subfactor endpoint?

**Solution.** The inequalities \(1<\sqrt2<2\) give \(1/2<\alpha<1\), hence \(0<1-\alpha<\alpha\) and \(0<2\alpha-1<1\). The complement of \(r_1\) has trace \(\alpha\), so it contains a projection \(r_2\) of trace \(1-\alpha\). Equal trace gives unitary conjugacy in the ambient factor. A finite certificate would satisfy 78.20. Since \(\alpha\) is irrational, equality of its rational and irrational coefficients forces \(h_1=-2^k\), contrary to its nonnegative rank. The formal vector has positive scalar trace but a negative second coordinate at every promoted level. The construction concerns the stated reducible finite-dimensional system, without Jones cups or a subfactor relative-commutant identification. It therefore refutes only the proposed scalar-arithmetic inference, not the actual subfactor theorem.

**Exercise 78.5 — identify the finite-depth input.** Explain why the two-step matrix in 78.16 is primitive, why the smaller downward trace has the required Perron weights, and why the separately chosen canonical rank vectors may overlap.

**Solution.** An even graph path joins any two vertices of one parity, so the two-step matrix has an entry along a path between any two of its vertices. Positive degrees give positive diagonal entries; insert diagonal steps until all finitely many paths have one common length. The corresponding power has every entry positive. Trace-preserving reflection identifies the actual smaller downward algebras with the upward relative commutants of the twice-shifted finite-depth inclusion. The finite-depth trace proof 14.3 puts their actual minimal weights on the positive Perron ray. Compatibility fixes the successive scale to \(\rho^{-1}\), rather than an arbitrarily chosen normalized matrix trace. Finite alignment supplies an individual canonical projection for each physical support trace; it gives no joint orthogonality of these representatives. Hence their rank sum may exceed a block capacity. Subtracting it from the identity gives the signed vector, and primitive promotion repairs the ranks using positivity of the physical residual's trace.

**Exercise 78.6 — the exact endpoint and its boundary.** What changes when the residual trace is zero, or one? Does the finite-depth proof need a common continuation? State exactly what remains required in the general case.

**Solution.** A zero-trace residual is zero by faithfulness, so the selected blocks already give the full finite partition. For trace one the residual is the identity and has a finite certificate; the placement argument uses the identity projection, without promoting a potentially nonpositive signed representative. The proof permits a separate actual continuation on each supported piece, as the source endpoint does. A common stage is not required for this finite conclusion. In the general nonfinite-depth case, 76.4 supplies the near-unit whole-stage blocks and retains its residual, while 78.3 proves that an exact residual trace certificate suffices. Automatic existence of that certificate, or another construction of an exact finite full partition, remains to be proved. Common-stage or prefix alignment, nesting and unrestricted generating tunnels are further obligations, not consequences of scalar trace bookkeeping.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*

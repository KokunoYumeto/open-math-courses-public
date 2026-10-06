# Local approximation and the hyperfinite finite factor

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

A finite-dimensional algebra that approximates a few operators need not contain a previously chosen algebra. The main construction below repairs that defect. A small change of one projection aligns the first matrix corner, and matrix units then align the whole old algebra exactly. Repeating this construction identifies every separable AFD factor of type \(\mathrm{II}_1\) with the tracial infinite product of \(M_2\).

We use the infinite product construction and its CAR realization. Foundational inputs are center-valued trace comparison, halving in an algebra without a type I part, finite projection joins and normal representation amplification. Trace densities identify the predual with \(L^1\). The trace-preserving expectation used here is the finite-trace case of the OA-MOD modular expectation theorem: the trace has trivial modular action, so every unital von Neumann subalgebra is invariant. Its expectation is normal, ucp, bimodular and the orthogonal projection in \(L^2\). General weight and expectation theory remains a prerequisite.

Unless stated otherwise, \(M\) is a factor of type \(\mathrm{II}_1\), with normalized faithful normal trace \(\tau\), and
\[
\|x\|_2=\tau(x^*x)^{1/2}.
\]
The inequalities \(\|axb\|_2\le\|a\|\|x\|_2\|b\|\), \(\|x^*\|_2=\|x\|_2\), and \(|\tau(x)|\le\|x\|_2\) follow from the trace and Cauchy–Schwarz. We write \(E_N\) for the trace-preserving expectation onto a unital subalgebra \(N\).

On norm-bounded sets, the \(2\)-norm gives the intrinsic sigma-strong* topology. To check this, write a normal positive functional as \(\tau(h\,\cdot)\), with \(h\in L^1_+\), and approximate \(h\) in \(L^1\) by a bounded positive \(b\). If \(\|x\|\le C\), then
\[
\tau(hx^*x)\le\|b\|\|x\|_2^2+C^2\|h-b\|_1.
\tag{1}
\]
The same estimate applies to \(xx^*\). Conversely the trace itself is one of the topology's tests. Norm-bounded \(2\)-norm Cauchy sequences have their limit in \(M\): an ultraweak cluster point of the bounded ball has the same pairings \(\tau(y^*x)\), \(y\in M\), as the Hilbert-space limit, and those pairings determine that limit.

## 1. Rotating equivalent projections

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

The exceptional projection \(k\) splits as \(p+q\), where \(p=e\wedge(1-f)\) and \(q=(1-e)\wedge f\). Indeed \(D^2=1\) implies \(r=0\); on \(eH\) its first term forces \(fe=0\), and on \((1-e)H\) its second term forces \(f=1\). Equivalence of \(e,f\) gives equal center-valued traces. The equivalence already established on \(1-k\) then gives equal center-valued traces for \(p,q\). Finite trace comparison gives a partial isometry \(v\) with \(v^*v=p,vv^*=q\). The skewadjoint unitary \(w=v-v^*\) on \(k\) carries \(p\) to \(q\), and \((w-k)^*(w-k)=2k\). Thus \(u=u_0+w\) is the required unitary; (4) and \(D^2k=k\) give (2). \(\square\)

There is also a useful spectral rounding estimate. If \(0\le h\le1\), \(\varphi\) is any normal state, and \(\|h-h^2\|_\varphi\le\delta\), then
\[
q=1_{[1/2,1]}(h)
\quad\Longrightarrow\quad
\|h-q\|_\varphi\le2\delta,\qquad
\|h^{1/2}-q\|_\varphi\le\sqrt{2\delta}.
\tag{5}
\]
Pointwise, \(|s-1_{[1/2,1]}(s)|\le2s(1-s)\), and
\((\sqrt s-1_{[1/2,1]}(s))^2\le2s(1-s)\). Integration against the state's spectral probability measure and Cauchy–Schwarz prove (5).

A higher cutoff is useful too: for \(0<\delta<1/4\), put \(\epsilon=\sqrt\delta\) and \(q'=1_{[1-\epsilon,1]}(h)\). The middle interval \([\epsilon,1-\epsilon)\) has spectral measure at most \(\delta/(1-\epsilon)^2\), because \(s(1-s)\ge\epsilon(1-\epsilon)\) there. On the lower and upper intervals the squared error for \(h-q'\) is at most \(\delta\); their combined contribution is at most \(\delta\). The middle contribution is at most \(\delta\). For \(h^{1/2}-q'\), the outside contribution is at most \(\epsilon\), and the middle contribution at most \(\delta/(1-\epsilon)\). Consequently
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
Also \(\varphi(h(1-h))\le\|h-h^2\|_\varphi\le\delta\). Adding these positive spectral integrals gives \(\varphi(h(1-q'))\le2\delta\). On \(q'\), both \((1-h)^2\) and \((1-h^{1/2})^2\) are at most \(\delta q'\). Split the two squared errors over \(q'\) and \(1-q'\) to obtain (6a). This is the higher-cutoff mechanism of Connes’s Lemma 1.1.5; the lower bound for \((1-h)^2\) supplies the spectral inequality needed in its proof. The preceding bounds (6) follow as well, since \(0<\delta<1\).

Only the simpler cutoff (5) will be needed below.

## 2. Trace cuts, tensor coordinates and averaging

Halving means that every projection in a type II algebra is the sum of two equivalent orthogonal projections. In a \(\mathrm{II}_1\) factor this gives every scalar trace cut: for \(0\le s\le\tau(e)\), expand \(s/\tau(e)\) in binary, repeatedly halve the current remainder of \(e\), and retain the half prescribed by each digit. The selected orthogonal pieces have traces \(\tau(e)2^{-j}\). Their strong sum has trace \(s\), by normality. Equal-trace projections are equivalent by finite trace comparison.

If \((e_{ij})_{i,j=1}^d\) are unital matrix units in an arbitrary von Neumann algebra \(P\), then
\[
P\cong M_d\bar\otimes e_{11}Pe_{11},\qquad
x\longmapsto[e_{1i}xe_{j1}]_{i,j}.
\tag{7}
\]
The inverse is \([x_{ij}]\mapsto\sum_{i,j}e_{i1}x_{ij}e_{1j}\). The matrix-unit rules check the products, adjoints and inverses; finite sums and normal corners show normality. The relative commutant of the matrix algebra is the diagonal copy \(x\mapsto\sum_i e_{i1}xe_{1i}\) of the corner. Thus the matrix algebra and its relative commutant generate \(P\). Type II is preserved in this corner: an abelian projection there would be abelian in \(P\).

More generally, if \(N\subset M\) is a subfactor and \(M=N\vee(N'\cap M)\), multiplication identifies
\[
M\cong N\bar\otimes(N'\cap M).
\tag{8}
\]
For \(y\in N'\cap M\), bimodularity gives \(E_N(y)\in Z(N)=\mathbb C1\); trace preservation makes it \(\tau(y)1\). Hence \(\tau(xy)=\tau(x)\tau(y)\). On algebraic tensors, multiplication is therefore an isometry of the two trace Hilbert spaces, by expanding inner products. Its range is dense by the generation hypothesis and Kaplansky density. The resulting unitary intertwines left multiplication by each tensor leg with multiplication by its image. It implements the asserted normal spatial isomorphism.

**Lemma 2.1.** If \(G\) is any subgroup of \(\mathcal U(M)\) and \(B=G'\cap M\), then \(E_B(x)\) is the unique element of \(B\) in the ultraweakly closed convex hull of \(\{uxu^*:u\in G\}\).

**Proof.** That hull \(K\) is contained in a norm-bounded ball and is ultraweakly compact. Its map into \(L^2(M)\) is weakly continuous: this is immediate on pairings with bounded \(y\in M\), and follows on general \(L^2\) vectors by approximation and the uniform norm bound. Thus \(K\) is weakly compact and convex in \(L^2\), hence norm closed. It has a unique element of least Hilbert norm. Conjugation by \(G\) preserves both the hull and this norm, so that element is in \(B\).

For \(b\in B\), traciality gives \(\tau(b^*uxu^*)=\tau(b^*x)\). The \(L^2\)-projection formula therefore makes \(E_B\) constant on the orbit, and normality makes it constant on the hull. The least-norm element is consequently \(E_B(x)\). Any other element of \(K\cap B\) would equal its own expectation and hence equal \(E_B(x)\). \(\square\)

Applying the lemma to \(G=\mathcal U(N)\) proves the quantitative commutant estimate
\[
\|x-E_{N'\cap M}(x)\|_2
\le\sup_{\substack{y\in N\\\|y\|\le1}}\|[x,y]\|_2.
\tag{9}
\]
Every orbit point lies in the indicated \(2\)-norm ball around \(x\); that ball is weakly closed and convex, so it contains the hull. None of these statements requires separability.

## 3. Replacing an approximant by a dyadic factor

For any von Neumann algebra \(P\), **AFD** means that for every finite set \(x_1,\ldots,x_m\in P\) and every sigma-strong* neighborhood \(U\) of zero there is a finite-dimensional *-subalgebra \(D\subset P\) with \(x_j\in D+U\) for every \(j\). This local definition does not require a sequence or separability. A possibly nonunital \(D\) can be replaced by \(D+\mathbb C1\).

In a finite factor call this property **locally AFD** when expressed using finite-set \(2\)-norm approximation. The two formulations agree: the intrinsic topology includes the trace seminorm, while applying \(E_D\) to any \(2\)-norm approximants supplies errors no larger and bounds the approximants by the original operator norms. Equation (1) then gives approximation for every specified sigma-strong* neighborhood.

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

## 4. Making containment exact

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

## 5. Uniqueness and all finite corners

Let
\[
R=\bar\bigotimes_{j\ge1}(M_2,\operatorname{tr}_2).
\]
The preceding product lesson proves that this is a separable factor of type \(\mathrm{II}_1\).

**Theorem 5.1.** For a \(\mathrm{II}_1\) factor \(M\) with separable predual, the following are equivalent:

1. \(M\cong R\).
2. \(M\) is generated by an increasing sequence of finite-dimensional *-subalgebras.
3. \(M\) is locally AFD.
4. Every nonzero corner of every finite matrix amplification of \(M\) is locally AFD.

**Proof.** The first implication gives the initial tensor factors. For the second, Kaplansky density in the increasing union supplies bounded strong* approximants, hence the third condition.

For \(3\Rightarrow1\), choose a \(2\)-norm dense sequence \((x_j)\) in the unit ball. Such a sequence exists: the ball is compact metrizable in the weak* topology; a countable weak* dense subset is weakly dense in \(L^2\), and its rational convex combinations are norm dense by convex separation. Apply Lemma 4.1 successively to \(V_k=\operatorname{span}\{x_1,\ldots,x_k\}\), keeping the previous dyadic matrix algebra exactly and making the error tend to zero. This gives increasing \(N_k\cong M_{2^{n_k}}\), with strictly increasing \(n_k\), whose union generates \(M\). Indeed \(E_{N_k}(x_j)\to x_j\) in \(2\)-norm with bounds one; the bounded-ball completeness and (1) put every \(x_j\), hence the entire ball, in the generated algebra.

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

For completeness, a faithful normal representation of \(R\) with finite commutant has a commutant isomorphic to \(R\). Normal representation amplification realizes it as
\(p(R^{\mathrm{op}}\bar\otimes B(K))p\). Finiteness of this corner means \(p\) is a finite projection. The semifinite factor finite-projection trace criterion gives finite \((\tau\otimes\operatorname{Tr})(p)\). In a sufficiently large finite matrix corner there is a projection of the same trace, and finite projection comparison makes it equivalent to \(p\). Thus the commutant is a nonzero corner of \(R^{\mathrm{op}}\bar\otimes M_n\). Transposition on every local matrix factor gives a compatible trace-preserving anti-isomorphism of the dyadic unions and extends in their trace GNS spaces; hence \(R^{\mathrm{op}}\cong R\). Corollary 5.2 finishes the argument. The normal representation and semifinite trace criterion are the explicit foundational inputs in this paragraph.

## 6. Subfactors and automorphisms

**Lemma 6.1.** A finite von Neumann algebra generated by an increasing directed family of unital subfactors is a factor.

**Proof.** Every normalized normal trace restricts to the unique normalized trace on each subfactor. Two such traces therefore agree on the increasing union and, by normality and density, everywhere. A finite algebra has a separating family of normal finite traces; composing its center-valued trace with normal center states shows that uniqueness of the normalized trace forces its center to be scalar. \(\square\)

Every type \(\mathrm{II}_1\) von Neumann algebra, including a nonfactor or a nonseparable one, contains a unital copy of \(R\). Halve its identity to embed \(M_2\). Formula (7) identifies the relative commutant with a type \(\mathrm{II}_1\) corner. Halve there and repeat, obtaining commuting \(M_2\)'s. Their generated algebra is finite and is a factor by Lemma 6.1. It contains matrices of unbounded size, hence is type \(\mathrm{II}_1\). Its normal trace restricts to the product trace on the finite tensor levels; the trace GNS identification makes this algebra \(R\).

If the ambient algebra has separable predual, every such copy lies in a maximal AFD \(\mathrm{II}_1\) subfactor. For a chain of AFD subfactors, its generated algebra is a finite factor by Lemma 6.1. It is locally AFD: approximate a finite set by bounded elements of the chain union, choose one chain member containing those finitely many approximants, and approximate them by a finite-dimensional algebra in that member. The two errors add. Separability of the ambient predual passes to the subalgebra, so Theorem 5.1 identifies this upper bound with \(R\). Zorn's lemma now supplies a maximal member. No maximality assertion here identifies the ambient algebra with that member.

**Lemma 6.2.** If \(A\cong M_d\) is a unital subfactor of any von Neumann algebra \(P\), then for every automorphism \(\alpha\) of \(P\) there is a unitary \(u\in P\) satisfying \(\alpha|_A=\operatorname{Ad}(u)|_A\).

**Proof.** Let \(e_{ij}\) be its matrix units. The projections \(e_{ii}\) are \(d\) equivalent pieces of one, and so are \(\alpha(e_{ii})\). On the finite central part of \(P\), their center-valued traces are all \(1/d\), giving \(e_{11}\sim\alpha(e_{11})\). On the properly infinite central part, \(e_{11}\) is properly infinite: a nonzero finite central cut of it would make the sum of its \(d\) equivalent cuts finite, contrary to proper infiniteness of that central summand. A properly infinite projection absorbs finitely many copies of itself, by halving and projection Schröder–Bernstein. Its \(d\) equivalent pieces sum to one, so \(e_{11}\sim1\) on this part, and the same holds for \(\alpha(e_{11})\). Adding the central parts gives a partial isometry \(w\) with \(w^*w=e_{11}\), \(ww^*=\alpha(e_{11})\). Then
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
For the normal functional \(\tau(b\,\cdot)\) its predual error is the \(L^1\)-norm of this difference, at most its \(2\)-norm. Such functionals with bounded \(b\) are dense in the predual; the automorphisms' uniform isometry bounds give convergence for every normal functional. This is the stated topology.

For an outer example, take \(Z=\operatorname{diag}(1,-1)\) and the product automorphism \(\bigotimes_j\operatorname{Ad}(Z)\). It preserves the product trace. Every implementing overlap \(|\operatorname{tr}_2(Z)|\) is zero, so the preceding lesson's infinite innerness criterion excludes innerness. Its finite prefix implementations nevertheless converge as in (20). \(\square\)

## 7. Problems with complete solutions

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

The exact foundational inputs remain center-valued trace comparison, type II halving, projection support, normal representation amplification and trace densities. Finite trace expectations are the declared modular-course specialization. Their transitive accessible-source verification remains separate from the complete containment and uniqueness proofs given here. The later finite outer-action and central-sequence arguments have their own prerequisites.

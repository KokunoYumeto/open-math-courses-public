# Infinite products and modular time



Infinite products remember the reference states. Their modular operators remember more than their finite tensor cores: they have maximal spectral domains. We construct the product, determine its commutant and state support, and prove the exact test for a product automorphism to be inner. This gives a semifiniteness criterion for a sequence of factors with separable preduals, including nonfaithful normal reference states.

The source antecedents are Takesaki, *Theory of Operator Algebras III*, XIV.1, Definitions 1.5–1.6 and 1.12, Lemmas 1.7–1.8, Theorem 1.9, Corollary 1.10, Proposition 1.11 and Theorems 1.13–1.14, printed pages 84–91. The absolute phase condition in Lemma 1.7 needs a correction described below. The earlier programme infinite-product lesson, Theorems 3.1–8.1, contains the corrected convergence criterion and the general product results. We give the arguments at their points of use and identify the substantial earlier proofs needed for spatial commutation and continuous internal implementation.

Throughout, inner products are linear in the first variable. A factor is nonzero and has scalar centre. Normal states need not be faithful unless expressly stated.

## Units, reference vectors and GNS kernels

For unital \(C^*\)-algebras \(A_n\), form their finite minimal tensor products \(A_{\leq n}\). The maps \(x\mapsto x\otimes1\) are isometric: faithful spatial representations identify their norms with the original operator norms. The increasing algebraic union therefore has a consistent \(C^*\)-norm. Its completion is the infinite minimal product. The units specify the embeddings; simply omitting them does not specify a canonical product of nonunital algebras.

Let \((H_n,\xi_n)\) be pointed Hilbert spaces with \(\|\xi_n\|=1\). Complete the increasing Hilbert union

\[
 H_{\leq n}\longrightarrow H_{\leq n+1},\qquad
 \eta\longmapsto\eta\otimes\xi_{n+1}.
 \tag{ITP.1}
\]

Write the completion as \(H=\bigotimes_n(H_n,\xi_n)\), its reference vector as \(\Omega\), and the projection onto the \(n\)-th stage as \(Q_n\). These projections increase strongly to one. Inserting an arbitrary finite tensor of bounded operators defines a bounded operator on \(H\), with its ordinary finite spatial norm. For concrete von Neumann algebras \(M_n\subset B(H_n)\), define

\[
 M=\left(\bigcup_n M_{\leq n}\otimes1\right)'',
 \qquad M_{\leq n}=M_1\bar\otimes\cdots\bar\otimes M_n.
 \tag{ITP.2}
\]

No cyclicity or separability is used in this concrete definition.

For abstract \(M_n\) with normal states \(\omega_n\), take their state GNS triples and use (ITP.2). The vector state of \(\Omega\) restricts to \(\prod_{j\leq n}\omega_j(x_j)\) on elementary products. Positivity and compatibility of finite product states give a state on the minimal \(C^*\)-product. The span of its local cyclic vectors is dense in \(H\), so its GNS representation is precisely the representation just constructed.

Here is the distinction needed when a state is nonfaithful. For \(p=s(\omega)\), a normal state's GNS representation \(\pi_\omega\) has kernel

\[
 \ker\pi_\omega=M(1-z(p)),
 \tag{ITP.3}
\]

where \(z(p)\) is the central support, rather than \(1-p\). Indeed, its kernel is an ultraweakly closed two-sided ideal, hence a central summand. A central projection \(z\) acts as zero exactly when
\(\omega(z)=\|\pi_\omega(z)\Omega_\omega\|^2=0\): centrality then makes it zero on every \(a\Omega_\omega\). This is equivalent to \(zp=0\). Normality of the GNS representation follows on its dense cyclic vectors by applying normality of \(\omega(b^*\,\cdot\, b)\) to bounded increasing positive nets; polarization and bounded approximation extend the conclusion to all vectors. These facts also prove the asserted closed central kernel.

In particular, the normal GNS representation of every nonzero normal state on a factor is faithful, although its cyclic vector can fail to be separating. We henceforth identify each factor with that faithful normal image. The spatial representation and GNS-kernel proofs, Sections 4–8, give the corresponding arbitrary-algebra statement and the finite spatial identifications used here.

## The exact vector convergence criterion

Let \(\eta_n\ne0\), suppose
\(b_n=\prod_{j\leq n}\|\eta_j\|\to b\in(0,\infty)\), and put

\[
 v_n=\eta_1\otimes\cdots\otimes\eta_n\otimes\xi_{n+1}\otimes\cdots,
 \quad
 a_j=\left\langle\frac{\eta_j}{\|\eta_j\|},\xi_j\right\rangle,
 \quad w_n=b_n^{-1}v_n .
\]

For \(m>n\), the defining inner product gives

\[
 \|w_m-w_n\|^2
 =2-2\operatorname{Re}\prod_{j=n+1}^{m}a_j.
 \tag{ITP.4}
\]

Because the product has modulus at most one,

\[
 |1-z|^2\leq2(1-\operatorname{Re}z)\quad (|z|\leq1).
\]

Thus \(v_n\) converges if and only if

\[
 \sup_{m>n}\left|1-\prod_{j=n+1}^{m}a_j\right|
 \longrightarrow0.
 \tag{ITP.5}
\]

The equivalence with convergence of \(w_n\) uses \(b_n\to b>0\). Its limit has norm one, so the limit of \(v_n\) has norm \(b\).

An equivalent, sometimes more useful condition is that for some \(N\), every \(a_j\) with \(j>N\) is nonzero, and

\[
 \sum_{j>N}(1-|a_j|)<\infty,
 \qquad
 \prod_{j=N+1}^{n}\frac{a_j}{|a_j|}
 \text{ converges in the unit circle.}
 \tag{ITP.6}
\]

To prove necessity, (ITP.5) makes all sufficiently late tail products have modulus at least \(1/2\). Their nonincreasing moduli then have a positive limit. The inequalities
\(1-r\leq-\log r\), and
\(-\log r\leq2(1-r)\) for \(r\geq1/2\), show that a positive product of numbers in \((0,1]\) is equivalent to summable modulus defects. Dividing the complex partial products by their convergent positive moduli gives a convergent unit-circle product; its Cauchy property follows directly from (ITP.5). Conversely, convergence of that unit-circle product and positivity of the modulus product give uniform tail convergence in both factors, which proves (ITP.5). Finitely many early zero overlaps do not affect the criterion.

Absolute summability of \(1-a_j\) is sufficient, by
\(\left|1-\prod a_j\right|\leq\sum|1-a_j|\), but is not necessary. For

\[
 \eta_j=e^{i(-1)^j/j}\xi_j
 \tag{ITP.7}
\]

the vectors \(v_n\) are scalar multiples of \(\Omega\), and their phases converge by the alternating-series estimate. Yet
\(|1-e^{i(-1)^j/j}|=2\sin(1/(2j))\geq2/(\pi j)\).
The absolute series diverges. This is the correction to the necessity assertion in the printed Lemma 1.7; the earlier programme Theorem 3.1 proves the same correction.

If instead \(b_n\to0\), then \(\|v_n\|\to0\), so \(v_n\to0\) with no overlap condition. A zero \(\eta_j\) makes all subsequent vectors zero. The positive finite norm-limit hypothesis must therefore stay attached to (ITP.5)–(ITP.6).

## Tail expectations and the full commutant

Decompose \(H=H_{\leq n}\otimes H_{>n}\). Compression against the tail reference vector, followed by amplification, gives

\[
 E_n(x)=
 \bigl[(1\otimes\langle\,\cdot\,,\Omega_{>n}\rangle)
 x(1\otimes\Omega_{>n})\bigr]\otimes1 .
 \tag{ITP.8}
\]

The notation denotes the usual vector compression and is independent of the chosen convention for writing the bra. Compression along a tensor tail proves that this is a normal unital completely positive expectation onto \(B(H_{\leq n})\otimes1\), and that
\(\|\rho E_n-\rho\|\to0\) for every normal functional \(\rho\) on \(B(H)\).

We also need strong* convergence. If \(\eta\) belongs to the \(k\)-th Hilbert stage, then, for \(n\geq k\),

\[
 E_n(x)\eta=Q_nx\eta .
 \tag{ITP.9}
\]

Both sides are the same compression in the decomposition defining (ITP.8). Hence \(E_n(x)\eta\to x\eta\). Uniform boundedness by \(\|x\|\) and density of finite-stage vectors prove strong convergence everywhere. Applying the argument to \(x^*\) proves strong* convergence.

Normality and the elementary product formula show that
\(E_n(M)\subset M_{\leq n}\otimes1\): the inverse image of this ultraweakly closed algebra under \(E_n\) is ultraweakly closed and contains every local product. It contains their generated von Neumann algebra.

Set \(N=(\bigcup_n M_1'\bar\otimes\cdots\bar\otimes M_n'\otimes1)''\).
Local commutation gives \(N\subset M'\). Conversely, if \(y\in M'\), the bimodule property of \(E_n\) makes \(E_n(y)\) commute with \(M_{\leq n}\). The finite spatial commutation theorem gives

\[
 E_n(y)\in
 (M_1'\bar\otimes\cdots\bar\otimes M_n')\otimes1\subset N.
\]

Taking the strong limit proves

\[
 M'=\bigotimes_n(M_n',H_n,\xi_n).
 \tag{ITP.10}
\]

The finite theorem at arbitrary concrete representations is proved in the earlier spatial commutation component, Sections 3–5: it first closes the tensor Hilbert-algebra graph and then passes to arbitrary normal representations by corners of amplifications. Thus no standardness assumption on the present \(H_n\) has been inserted.

If each \(M_n\) is a factor and \(z\in Z(M)\), then \(E_n(z)\) lies in the finite head and commutes with it, so it is scalar. Since \(E_n\) preserves the reference vector state, that scalar is always \(\langle z\Omega,\Omega\rangle\). Equation (ITP.9) gives \(z=\langle z\Omega,\Omega\rangle1\). Hence every such product is a factor, without a faithfulness hypothesis on the reference vector states.

We will also use

\[
 M\cap M_{\leq n}'=1\otimes M_{>n}.
 \tag{ITP.11}
\]

Indeed \(M=M_{\leq n}\bar\otimes M_{>n}\). Slicing a commuting operator on the tail gives elements of \(Z(M_{\leq n})=\mathbb C\); the normal slice maps separate operators. The slice proof and separation by matrix coefficients are in Section 6 of the same spatial component.

## Faithful states and maximal modular domains

Assume now that each \(\omega_n\) is faithful, and use its GNS space. The reference vector is cyclic for \(M\). Each \(\xi_n\) is also cyclic for \(M_n'\), since it is separating for \(M_n\); the orthogonal projection onto \(\overline{M_n'\xi_n}\) belongs to \(M_n\), and its complement annihilates \(\xi_n\). Equation (ITP.10) therefore makes \(\Omega\) cyclic for \(M'\), hence separating for \(M\). Its normal product state is faithful.

Write the component modular data as \(S_n=J_n\Delta_n^{1/2}\). Each \(J_n\) and \(\Delta_n^{it}\) fixes \(\xi_n\). Their finite tensor actions consequently define an antiunitary conjugation \(J\) and a unitary group \(U_t\) on \(H\). The group is strongly continuous on every finite-stage vector by finite tensor continuity, and hence everywhere by density and its unit norm. By Stone's theorem with the derivative domain and its exact programme Stone theorem, let \(A\) be its self-adjoint generator, with \(U_t=e^{itA}\), and set \(\Delta=e^A\).

Each \(Q_n\) reduces this group. On its range the generator is that of the finite product modular group, so \(\Delta^{1/2}\) restricts to the closed finite tensor of the \(\Delta_j^{1/2}\). The finite tensor graph and its adjoint domains are proved in Positive tensors and a graph core through Closed tensors, adjoints, and polar supports. Their rectangular spectral cutoffs show that algebraic tensors of the component Tomita cores form a graph core for the finite product. Since \(Q_n\uparrow1\) and commutes with the spectral calculus, these finite cores together form a graph core for \(J\Delta^{1/2}\).

On that core \(J\Delta^{1/2}(x\Omega)=x^*\Omega\). This proves that it is contained in the closure of the Tomita map. For the reverse inclusion take any \(x\in M\). Compression gives

\[
 E_n(x)\Omega=Q_nx\Omega,\qquad
 E_n(x)^*\Omega=Q_nx^*\Omega .
 \tag{ITP.12}
\]

The finite product Tomita map acts on these pairs, and both components converge. Closedness of \(J\Delta^{1/2}\) gives its value \(x^*\Omega\) on \(x\Omega\). Taking the closure proves

\[
 S=J\Delta^{1/2},\qquad S^*=\Delta^{1/2}J.
 \tag{ITP.13}
\]

The component identity \(J_n\Delta_nJ_n=\Delta_n^{-1}\), first on the finite graph cores and then by closure, gives \(J\Delta J=\Delta^{-1}\). Thus \(S^*S=\Delta\) and these are the actual modular data. On local products, conjugation by \(U_t\) is the product of the component modular automorphisms; normality extends the equality to \(M\).

For clarity, every complex power has its maximal domain, not just its algebraic core:

\[
 \begin{split}
 \Delta^z&=\int_{\mathbb R}e^{z\lambda}\,dE_A(\lambda),\\
 D(\Delta^z)&=
 \left\{\eta:\int_{\mathbb R}e^{2\operatorname{Re}(z)\lambda}
                   \,d\langle E_A(\lambda)\eta,\eta\rangle<\infty\right\}.
 \end{split}
 \tag{ITP.14}
\]

Also \(D(S)=D(\Delta^{1/2})\) and
\(D(S^*)=\{\eta:J\eta\in D(\Delta^{1/2})\}\).
For each fixed \(z\), truncating first by \(Q_n\), then by bounded spectral intervals of the finitely many \(\log\Delta_j\), approximates both a vector in (ITP.14) and its image. On those intervals the operators are bounded, and finite algebraic tensors are dense. This proves the asserted graph-core approximation for every complex power.

## State supports, full corners and traces

Return to arbitrary normal reference states on factors and their faithful GNS representations. Put \(p_n=s(\omega_n)\in M_n\), and regard these as commuting local projections in \(M\). Their decreasing finite products have strong limit

\[
 e=\mathop{\mathrm{s}\!-\!\lim}_{n}\prod_{j\leq n}p_j,\qquad e\Omega=\Omega.
 \tag{ITP.15}
\]

On every finite-stage tensor, this limit compresses the finitely many nonreference legs by their \(p_j\). It follows by bounded density that
\(eH=\bigotimes_n(p_nH_n,\xi_n)\).

For a vector state on a concrete von Neumann algebra, its support is the projection onto the closure of the commutant orbit of its vector: that projection is in the algebra, fixes the vector, and is below every projection in the algebra that fixes it. Here (ITP.10) makes that closed orbit the tensor product of
\(\overline{M_n'\xi_n}=p_nH_n\). Thus \(e=s(\omega)\).

Compression of bounded local approximants shows, normally and onto, that

\[
 eMe=\bigotimes_n(p_nM_np_n,\omega_n|_{p_nM_np_n}).
 \tag{ITP.16}
\]

More explicitly, compressing a local tensor gives its finite tensor of corner entries on \(eH\). Kaplansky approximation and normal compression give every \(exe\) in the strong closure of these operators, while the opposite inclusion is immediate. Each corner state is faithful. Cyclicity in \(p_nH_n\) follows by compressing the original cyclic vectors and using \(\xi_n=p_n\xi_n\); hence these are exactly their faithful state GNS representations.

Semifiniteness passes both ways between a factor and any nonzero corner. We recall the constructive earlier proof, general semifiniteness foundations, matrix traces and corner transfer. If \(pMp\) has an NSF trace, choose partial isometries \(v_j\) with \(v_j^*v_j\leq p\), mutually orthogonal \(v_jv_j^*\), and \(\sum_jv_jv_j^*=1\). A maximal such family exhausts one because any nonzero residual projection has nonzero contact with \(p\) in a factor. The map

\[
 x\longmapsto[v_i^*xv_j]_{i,j}
 \tag{ITP.17}
\]

is a normal isomorphism onto the corner with diagonal projection
\(\operatorname{diag}(v_j^*v_j)\) in \(B(\ell^2(J))\bar\otimes pMp\).
Its diagonal trace \(\sum_j\tau(X_{jj})\), interpreted as a supremum of finite sums, is faithful, normal and tracial. Finite-coordinate projections tensored with finite-trace projections increase to one and supply finite-trace sandwiches of every positive operator, proving semifiniteness. The same sandwiches prove that restriction to an arbitrary corner stays semifinite, even when its unit has infinite trace. This proves both directions of the corner assertion. The stated earlier proof includes the factor-contact argument and all arbitrary-index matrix details.

If the \(M_n\) are finite factors and the \(\omega_n\) their normalized traces, the faithful product state is tracial. Traciality holds on the local algebra; for fixed local \(a\), normality extends \(\omega(ax)=\omega(xa)\) to all \(x\), and a second bounded strong approximation extends it to all \(a\). Thus \(M\) is a finite factor.

If infinitely many \(M_n\ne\mathbb C\), choose a nonzero trace-zero vector in each of any \(k\) such factors. Tensoring either that vector or the reference vector gives \(2^k\) mutually orthogonal nonzero vectors in the GNS space. Therefore the product cannot be a finite matrix algebra. A finite factor with a minimal projection is a finite matrix algebra: a maximal orthogonal family equivalent to that projection exhausts one by factor contact, and finiteness of the trace bounds the family's cardinality; its matrix units and scalar minimal corner span the algebra. Consequently the infinite product here is of type \(\mathrm{II}_1\). If only finitely many factors are nontrivial, the conclusion is instead their ordinary finite tensor product.

## When product automorphisms are inner

Let \(\alpha_n\in\operatorname{Aut}(M_n)\) preserve \(\omega_n\), where the \(M_n\) are factors and the \(\omega_n\) arbitrary normal states. The GNS unitary \(x\xi_n\mapsto\alpha_n(x)\xi_n\) fixes \(\xi_n\). Its pointed product constructs the normal automorphism
\(\alpha=\bigotimes_n\alpha_n\) on \(M\).

We prove the exact criterion:

\[
 \alpha\text{ is inner}
 \quad\Longleftrightarrow\quad
 \begin{cases}
 \alpha_n=\operatorname{Ad}u_n\text{ for every }n,\\
 \displaystyle\sum_n(1-|\omega_n(u_n)|)<\infty .
 \end{cases}
 \tag{ITP.18}
\]

Changing a component implementer multiplies it by a scalar unitary, so the series is well defined.

Suppose first that a unitary \(U\in M\) implements \(\alpha\). Slice \(U\), viewed in \(M_n\bar\otimes M_{\ne n}\), by a normal functional on the other leg so as to obtain \(a\ne0\). Such a slice exists because normal slices separate operators. Then
\(ax=\alpha_n(x)a\) for all \(x\in M_n\). Thus \(a^*a\) and \(aa^*\) are scalar. Their equal positive norms give \(a=c\,u_n\), with \(c>0\) and \(u_n\) unitary. This proves component innerness.

Choose its phase so that \(r_n=\omega_n(u_n)=|\omega_n(u_n)|\geq0\), and put \(v_n=u_1\cdots u_n\), with the factors in their respective legs. Equation (ITP.11) gives \(v_n^*U\in M_{>n}\). Hence

\[
 E_n(U)=a_nv_n,\qquad |a_n|\leq1.
 \tag{ITP.19}
\]

By strong convergence and \(\|v_n\Omega\|=1\),
\(|a_n|=\|E_n(U)\Omega\|\to\|U\Omega\|=1\).
For \(m>n\), the tower property \(E_nE_m=E_n\) gives

\[
 a_n=a_m\prod_{j=n+1}^m r_j .
 \tag{ITP.20}
\]

Choose \(n\) with \(a_n\ne0\). Every subsequent \(r_j\) is positive, and
\(\prod_{j=n+1}^m r_j\geq|a_n|>0\).
The logarithm bounds used in (ITP.6) prove summability of the tail defects, and the finitely many early defects do not matter. This proof does not assume \(\omega(U)\ne0\).

Conversely suppose the right side of (ITP.18) holds, and use the same nonnegative phases. For every vector \(\eta\) in the \(k\)-th Hilbert stage and \(m>n\geq k\),

\[
 \|(v_m-v_n)\eta\|^2
 =2\|\eta\|^2\left(1-\prod_{j=n+1}^{m}r_j\right).
 \tag{ITP.21}
\]

The identical estimate holds for the adjoints because
\(\omega_j(u_j^*)=r_j\). The right side tends to zero uniformly in \(m>n\). Bounded density gives strong limits \(v_n\to V\), \(v_n^*\to W\), and multiplication of bounded strongly convergent sequences gives \(VW=WV=1\), \(W=V^*\). Thus \(V\) is a unitary of \(M\). For a local \(x\), \(v_nxv_n^*=\alpha(x)\) for all sufficiently large \(n\); taking limits and then normal extension proves \(\operatorname{Ad}V=\alpha\). This proves (ITP.18) with no state-faithfulness assumption.

## Every modular time and semifiniteness

Assume now that every \(M_n\) has separable predual. The product is semifinite if and only if every \(M_n\) is semifinite and, writing
\(\omega_n(x)=\tau_n(h_nx)\) for any NSF traces \(\tau_n\), one has

\[
 \sum_n\bigl(1-|\omega_n(h_n^{it})|\bigr)<\infty
 \qquad\text{for every }t\in\mathbb R .
 \tag{ITP.22}
\]

Here \(h_n\) is the positive trace-integrable affiliated density,
\(s(h_n)=p_n=s(\omega_n)\).
The symbol \(h_n^{it}\) is unitary on \(p_nH_n\); when evaluated in \(\omega_n\), it is extended by zero off that support. At \(t=0\) this extension is \(p_n\). It is not asserted to be a unitary of \(M_n\) when \(p_n\ne1\).

We specify the modular semifiniteness input precisely. For a von Neumann algebra with separable predual and a faithful normal state, innerness of each modular time implies an NSF trace. This uses two earlier proved results: the continuous internal implementation theorem, Steps 1–6, and A continuous inner modular group characterizes semifiniteness. The first constructs a strongly continuous unitary group inside the algebra from a pointwise inner continuous real action. It proves a Borel lift, removes the commutator obstruction, constructs a regular representation and its fixed algebra, and produces a covariant central spectral family whose unitaries correct the group law. No continuity of arbitrarily chosen implementers is assumed. The second proves that a continuously internally implemented modular group is equivalent to semifiniteness, by centralizer perturbation of the faithful weight, with the trace identity on the full positive cone. It also supplies the affiliated trace densities. Conversely, those densities make every modular time inner in a semifinite algebra.

The separability hypotheses required for this input hold here. A normal state GNS space of an algebra with separable predual is separable: the unit ball is weak-star compact metrizable, and a countable weak-star dense subset has cyclic-vector span dense, since a vector orthogonal to that span defines a normal coefficient functional and is then orthogonal to every cyclic vector. Countable finite products and their Hilbert union preserve separability. The represented product and all its corners consequently have separable preduals, as quotients of the separable trace-class space. These arguments apply to each component corner too.

If \(M\) is semifinite, so is \(eMe\), by (ITP.17). Its faithful product state from (ITP.16) has componentwise modular flow by (ITP.13). For any fixed \(t\), the flow on \(eMe\) is inner. Criterion (ITP.18) implies that every component corner's modular time is inner. Doing this for all \(t\), the just stated modular input shows that each corner is semifinite; corner transfer gives semifiniteness of every original \(M_n\). Choose traces \(\tau_n\) and their densities \(h_n\). On the support corner, \(h_n^{it}\) implements the component modular time. All implementations on a factor differ only by a scalar, so (ITP.18) gives (ITP.22) at this fixed time, and hence at every real time.

Conversely, assume the right side of the criterion. Restrict the traces to the support corners; they remain NSF, regardless of \(\tau_n(p_n)\). Their densities are the same \(h_n\). For each fixed \(t\), (ITP.22) and (ITP.18) make the product corner's modular time inner. The separable-predual continuous-implementation and modular tests give an NSF trace on \(eMe\). Corner transfer gives one on \(M\). This proves both implications for the original nonfaithful states.

Finally, the full factor-trace uniqueness proof shows that any other NSF trace is \(c_n\tau_n\), with \(0<c_n<\infty\). Its density is \(c_n^{-1}h_n\), and spectral calculus on the support gives

\[
 \omega_n((c_n^{-1}h_n)^{it})
 =c_n^{-it}\omega_n(h_n^{it}).
 \tag{ITP.23}
\]

Therefore the moduli and the criterion are intrinsic. The condition is tested at every individual real time; no uniform convergence in time has been added. No assertion without the stated separable-predual hypothesis is inferred from this proof.

## Examples that distinguish the hypotheses

For \(M_n=M_2(\mathbb C)\) with density
\(d_n=\operatorname{diag}(q_n,1-q_n)\), \(0<q_n<1\), use Hilbert–Schmidt GNS coordinates and reference vector \(d_n^{1/2}\). Left multiplication represents the algebra and

\[
 \Delta_n e_{ij}=\frac{(d_n)_{ii}}{(d_n)_{jj}}e_{ij},
 \qquad
 \omega_n(d_n^{it})=q_n^{1+it}+(1-q_n)^{1+it}.
 \tag{ITP.24}
\]

Both formulas follow by multiplying the matrix units on the left by \(d_n\) and on the right by \(d_n^{-1}\). Finite tensors multiply these eigenvalue ratios. Their completion has exactly (ITP.14), so growing ratios do not justify replacing the maximal domain by the algebraic finite tensors.

If \(q_n=q\ne1/2\) is constant, the modulus in (ITP.24) is one precisely when the two unit phases coincide:

\[
 t\log\frac{q}{1-q}\in2\pi\mathbb Z.
 \tag{ITP.25}
\]

Indeed the squared modulus is
\(q^2+(1-q)^2+2q(1-q)\cos(t\log(q/(1-q)))\).
At every other time the constant positive defect makes the series diverge. Thus (ITP.18) determines exactly which modular times are inner, and (ITP.22) proves that this product is not semifinite. Determining these inner times alone is not a proof of a finer type \(\mathrm{III}\) classification.

For \(q_n=1/2\), the product is the tracial type \(\mathrm{II}_1\) factor of Section 5; every modular operator is one. These two cases show why the reference states are part of the product's data.

For a different extreme, take each \(M_n=M_2(\mathbb C)\) in its usual representation on \(\mathbb C^2\), with a pure vector state. This is that state's faithful normal GNS representation. Each local commutant is scalar, so (ITP.10) gives \(M'=\mathbb C\) and \(M=B(H)\). The product state support is the rank-one projection onto \(\Omega\), by (ITP.15); the product representation is nevertheless faithful. With the counting trace, each density is its rank-one support \(p_n\), and \(\omega_n(h_n^{it})=1\) for all \(t\). Criterion (ITP.22) correctly gives a semifinite type I algebra with a nonfaithful reference state.

These examples keep three different objects separate: the kernel of a representation, the support of a state, and the domain of an unbounded modular operator.


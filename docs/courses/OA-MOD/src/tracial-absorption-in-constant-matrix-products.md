# Tracial absorption in constant matrix products

In a long tensor block, basis words with the same letter counts have the same state density. Pairing those words gives square-zero matrix units which exactly centralize the product state and occupy almost all of it. A complete matrix-unit repair turns these partial units into commuting full blocks. This proves tracial absorption and the implication from strong lambda-stability to strong stability.

## 1. The products and the conclusion

Fix \(d\ge2\) and numbers

\[
p_i>0,\qquad \sum_{i=1}^d p_i=1.
\]

Let \(h=\operatorname{diag}(p_1,\ldots,p_d)\), let
\(\rho(a)=\operatorname{Tr}(ha)\) on \(M_d(\mathbb C)\), and form the specified infinite product

\[
P_h=\bigotimes_{n=1}^{\infty}(M_d(\mathbb C),\rho).
\tag{CTA.1}
\]

Section 4 constructs its faithful product representation. Write

\[
R=\bigotimes_{n=1}^{\infty}(M_2(\mathbb C),\operatorname{tr}_2).
\]


**Constant-product absorption theorem.** There is a normal isomorphism with normal inverse

\[
P_h\cong P_h\bar\otimes R.
\tag{CTA.2}
\]

No type classification of \(P_h\) is needed for this conclusion.

More generally, for any nonzero von Neumann algebra \(B\),

\[
B\cong B\bar\otimes P_h
\quad\Longrightarrow\quad
B\cong B\bar\otimes R.
\tag{CTA.3}
\]

In particular, with

\[
h_\lambda=\frac1{1+\lambda}
 \begin{pmatrix}\lambda&0\\0&1\end{pmatrix},
\qquad 0<\lambda<1,
\]

the product \(P_{h_\lambda}\) is precisely the specified \(R_\lambda\) of definition preceding LA01. Thus strong \(\lambda\)-stability implies tracial-product absorption.

The proof first establishes the following ordinary matrix criterion.

**Approximate-halving criterion.** If \(A\ne0\) has separable predual, the following are equivalent:

1. \(A\cong A\bar\otimes R\) normally, with normal inverse.
2. \(A\) has a bounded centralizing sequence of square-zero partial isometries \(v_n\) with \(v_n^*v_n+v_nv_n^*=1\).
3. \(A\) has centralizing contractions \(x_n\) such that

   \[
   x_n^2\longrightarrow0,\qquad
   x_n^*x_n+x_nx_n^*\longrightarrow1
   \quad\hbox{strongly*}.
   \tag{CTA.4}
   \]


Here centralizing means
\(\|\varphi x_n-x_n\varphi\|\to0\) for every \(\varphi\in A_*\), with the module conventions of ECA02. All strongly* limits below concern uniformly bounded operators and the intrinsic sigma-strong* topology.

We use the previously proved estimates for centralizing sequences and homogeneous rounding, ECA02–04, the faithful-state continuity and predual density arguments, CDS02 and CDS05–06, and the complete summable tensor-splitting theorem, TS01–06. Sections 2–3 give the ordinary, non-equivariant repair in full, so the criterion does not require a circle action.

## 2. From approximate units to exact full units

Assume condition 3. The bounded centralizing sequences form a *-algebra. Strongly* null bounded sequences centralize, and they may be multiplied on either side by a bounded centralizing sequence while remaining strongly* null. These are the fully proved estimates of ECA02. Thus equality modulo such a null sequence is compatible with the algebraic operations on centralizing sequences; write it as \(\sim\).

Set \(a_n=x_n^*x_n\), \(b_n=x_nx_n^*\). From (CTA.4),

\[
a_n+b_n\sim1,\qquad a_nb_n\sim b_na_n\sim0,\qquad
a_n^2\sim a_n,\quad b_n^2\sim b_n.
\tag{CTA.5}
\]

For example \(a_nb_n=x_n^*x_n^2x_n^*\sim0\), and

\[
a_n^2=x_n^*b_nx_n
 \sim x_n^*(1-a_n)x_n
 =a_n-(x_n^*)^2x_n^2\sim a_n.
\]

Every moving multiplier here is centralizing.

Put

\[
p_n=1_{[1/2,1]}(a_n),\qquad
z_n=(1-p_n)x_np_n.
\tag{CTA.6}
\]

The scalar inequality

\[
|1_{[1/2,1]}(t)-t|\le2(t-t^2),\qquad0\le t\le1,
\]

proved in ECA03, gives \(p_n-a_n\to0\) strongly*. Hence \(p_n\) is centralizing. The relations \(a_nx_n\sim0\) and \(x_na_n\sim x_n\) give \(z_n\sim x_n\).

If \(z_n=s_n|z_n|\) is the polar decomposition, define

\[
q_n=1_{[1/2,1]}(z_n^*z_n),\qquad w_n=s_nq_n.
\tag{CTA.7}
\]

Then \(w_n^*w_n=q_n\le p_n\) and \(w_nw_n^*\le1-p_n\); thus \(w_n\) is a square-zero partial isometry. To record both error seminorms, set

\[
g(t)=
\begin{cases}
t,&0\le t<1/2,\\
(1-\sqrt t)^2,&1/2\le t\le1.
\end{cases}
\]

Polar calculus gives

\[
\begin{aligned}
(w_n-z_n)^*(w_n-z_n)&=g(z_n^*z_n),\\
(w_n-z_n)(w_n-z_n)^*&=g(z_nz_n^*).
\end{aligned}
\tag{CTA.8}
\]

The scalar bound \(0\le g(t)\le2(t-t^2)\), including \(g(0)=0\), is proved in ECA03. Since both arguments are projections modulo strongly* null sequences, (CTA.8) proves \(w_n-z_n\to0\) strongly*. Consequently

\[
w_n\sim x_n,\qquad
w_n^*w_n+w_nw_n^*\longrightarrow1.
\tag{CTA.9}
\]

The sequence \(w_n\) is centralizing.

We next prove that every nonzero projection \(f\in A\) contains a nonzero square-zero partial isometry. The contractions \(y_n=fx_nf\) centralize \(fAf\): extend \(\chi\in(fAf)_*\) normally by \(\widetilde\chi(a)=\chi(faf)\), and restrict \([x_n,\widetilde\chi]\) to the corner. This is exactly \([y_n,\chi]\). Centrality of \(x_n\) also gives \([x_n,f]\to0\) strongly*, by ECA02. Using its small-error multiplication rule,

\[
y_n^2\longrightarrow0,\qquad
y_n^*y_n+y_ny_n^*\longrightarrow f
\quad\hbox{in }fAf.
\tag{CTA.10}
\]

For example \(y_n^2-fx_n^2f=fx_n(fx_n-x_nf)f\); the other products are expanded in the same way. Applying (CTA.5)–(CTA.9) inside \(fAf\) gives partial isometries whose support sums tend to \(f\). A normal positive functional nonzero on \(f\) shows that some one of them is nonzero.

In fact \(f\) can be filled exactly. Order the square-zero partial isometries in \(fAf\), including zero, by orthogonal extension:

\[
v\preceq v+r,\qquad
r\in(f-v^*v-vv^*)A(f-v^*v-vv^*).
\]

Along a chain, initial and final projections increase. The identity

\[
\|(v_j-v_i)\eta\|^2
 =\langle(v_j^*v_j-v_i^*v_i)\eta,\eta\rangle
 \quad(v_i\preceq v_j)
\]

and its adjoint version give a bounded strong* chain limit. Products pass to that limit, so it is still a square-zero partial isometry and an upper bound. Zorn's lemma gives a maximal one. If its support sum were less than \(f\), the preceding corner construction would give a nonzero orthogonal extension. Therefore there is \(r\in fAf\) with

\[
r^2=0,\qquad r^*r+rr^*=f.
\tag{CTA.11}
\]


Apply (CTA.11) to \(f_n=1-w_n^*w_n-w_nw_n^*\), taking \(r_n=0\) when \(f_n=0\), and put \(v_n=w_n+r_n\). These are full square-zero partial isometries. Both \(r_n^*r_n\) and \(r_nr_n^*\) lie below \(f_n\to0\), so \(r_n\to0\) strongly*. Hence

\[
v_n-x_n\longrightarrow0\quad\hbox{strongly*},
\tag{CTA.12}
\]

and the predual small-error estimate in ECA02 proves that \(v_n\) is centralizing. This establishes condition 2 from condition 3. No global commutator estimate was imposed on units in an intermediate fixed corner.

## 3. Exact commutation and the absorption criterion

To turn the units into a tensor factor, they must be chosen to commute with previous blocks. Let \(D\subset A\) be a unital full matrix algebra of size \(q\), with matrix units \(e_{ij}\), and let \(C=D'\cap A\). The faithful normal tracial expectation from TS01 is

\[
E_D(a)=\frac1q\sum_{i,j=1}^q e_{ji}ae_{ij}.
\tag{CTA.13}
\]

For a centralizing sequence \(x_n\) satisfying (CTA.4),

\[
E_D(x_n)-x_n
 =\frac1q\sum_{i,j}e_{ji}[x_n,e_{ij}]
 \longrightarrow0\quad\hbox{strongly*}.
\tag{CTA.14}
\]

The equality uses \(q^{-1}\sum_{i,j}e_{ji}e_{ij}=1\). Fixed-operator commutation follows from ECA02, and the sum is finite.

Thus \(E_D(x_n)\) is centralizing on the whole of \(A_*\) and still satisfies (CTA.4). It also centralizes \(C_*\): a normal functional on \(C\) extends by composition with \(E_D\), and bimodularity identifies the restricted commutator. Apply Section 2 inside \(C\). Its spectral formulas also give the same strong* estimates in \(A\), because the original error relations and centrality hold there. The unused projections tend strongly* to zero in \(A\), so the arbitrary fillers in their corners are small there as well. Consequently \(C\) contains a sequence of full halving units which remains centralizing on all of \(A_*\).

Choose normal states \((\psi_j)\) norm dense in the state space of \(A\). Their complex linear span is norm dense in \(A_*\), by CP07's positive decomposition. If a faithful state is needed to express a bounded strong* limit by one seminorm, \(\sum_j2^{-j}\psi_j\) provides it: a positive element killed by that sum is killed by every \(\psi_j\), hence by every normal state by norm density, and is zero. Normality follows from norm completeness of the predual in CP06.

Inductively construct commuting full \(M_2\) subalgebras \(D_k\), with \(v_k=e_{12}^{(k)}\), such that

\[
\|\psi_jv_k-v_k\psi_j\|\le2^{-k}
\qquad(1\le j\le k).
\tag{CTA.15}
\]

At each step the previously chosen blocks generate a full finite matrix algebra, by TS03. Apply the preceding relative-commutant construction and choose a sufficiently late unit for the finitely many estimates. This gives exact commutation of different blocks.

For every fixed \(j\), the defects in (CTA.15) are summable; the omitted finite initial segment is finite. TS06 at parameter \(1\) gives the bound

\[
\|\psi_j-\psi_jE_{D_k}\|
 \le3\|\psi_jv_k-v_k\psi_j\|.
\tag{CTA.16}
\]

The complete tail-expectation and spatial-splitting proof of TS01–05 therefore gives

\[
A\cong R\bar\otimes Q,\qquad
Q=\left(\bigvee_kD_k\right)'\cap A,
\tag{CTA.17}
\]

by normal multiplication with normal inverse. This proves generation and the whole spatial tensor product, not just its finite matrix moments.

The interleaving unitary of ECA07 identifies \(R\bar\otimes R\) normally with \(R\). Tensor flips and (CTA.17) now give

\[
A\bar\otimes R
 \cong R\bar\otimes Q\bar\otimes R
 \cong R\bar\otimes R\bar\otimes Q
 \cong R\bar\otimes Q
 \cong A.
\tag{CTA.18}
\]

All these maps have normal inverses.

This proves 3 implies 1 in the criterion. Conversely, in \(A\bar\otimes R\) the sequence \(1\otimes e_{12}^{(n)}\) consists of full halving units and is centralizing. ECA08 proves centrality in \(R\); the normal product-functional density argument of CDS06 proves it in \(A\bar\otimes R\). Transfer by the assumed normal isomorphism gives 1 implies 2. Condition 2 immediately implies 3. The approximate-halving criterion is proved.

## 4. The faithful product representation

We now construct the particular algebra in (CTA.1). On one leg use the Hilbert space of \(d\)-by-\(d\) matrices with Hilbert–Schmidt norm and reference vector

\[
\Omega_h=h^{1/2}.
\]

Its norm is one. Left multiplication represents \(M_d\). Right multiplication is bounded as well:

\[
\|xa\|_2^2=\operatorname{Tr}(a^*x^*xa)
 \le\|a\|^2\operatorname{Tr}(x^*x).
\]

It commutes with every left multiplication. Since \(h^{1/2}\) is invertible, the vectors obtained from \(\Omega_h\) by either all left or all right multiplications span the entire finite-dimensional Hilbert space.

Form the Hilbert space completion of finite-support tensor vectors with reference \(\Omega_h\) in the omitted legs. Let \(\Omega\) be the product reference vector, and let \(P_h\) be the von Neumann algebra generated by the finite left matrix algebras. Both their cyclic vectors and the cyclic vectors of the commuting finite right algebras are dense. Thus \(\Omega\) is cyclic for \(P_h\), and is separating: if \(X\Omega=0\), then \(Xb'\Omega=0\) for every finite right operator \(b'\), and density gives \(X=0\).

It follows that

\[
\Phi(X)=\langle X\Omega,\Omega\rangle
\tag{CTA.19}
\]

is a faithful normal state. Its restriction to the first \(m\) legs is the matrix state with density \(h^{\otimes m}\). The Hilbert space is separable: in each leg choose a finite orthonormal basis containing \(\Omega_h\); the finite-support product basis is countable. CP04–06 therefore gives separable predual for \(P_h\).

If \(h=I/d\), the local states are normalized traces. Traciality extends to the entire algebra: first keep one factor in a finite head and extend the other by normality, and then extend the first factor by normality. In particular the \(d=2\) case is the faithful tracial product defining \(R\). No classification of the general \(P_h\) has entered this representation argument.

## 5. Pairing basis words of equal density

In a block of \(m\) legs, index the standard matrix basis by words

\[
a=(a_1,\ldots,a_m)\in\{1,\ldots,d\}^m.
\]

Let \(k_i(a)\) be the number of occurrences of \(i\). The density of the basis word is

\[
p(a)=\prod_{i=1}^d p_i^{\,k_i(a)}.
\tag{CTA.20}
\]

Partition the words by their count vectors \((k_1,\ldots,k_d)\). Within each class, order the words lexicographically and pair consecutive words. For a pair \((a,b)\), use the matrix unit \(E_{ab}=|a\rangle\langle b|\), always with the first word as the range and the second as the source. Put

\[
x^{(m)}=\sum_{\text{chosen pairs }(a,b)}E_{ab}.
\tag{CTA.21}
\]

All words in different pairs are disjoint, so

\[
(x^{(m)})^2=0,\qquad
(x^{(m)})^*x^{(m)}+x^{(m)}(x^{(m)})^*=1-f_m,
\tag{CTA.22}
\]

where \(f_m\) is the projection onto the unpaired words. Thus \(x^{(m)}\) is a contraction and a partial isometry; it may be zero for a small block.

For every pair, \(p(a)=p(b)\). Hence

\[
h^{\otimes m}x^{(m)}=x^{(m)}h^{\otimes m}.
\tag{CTA.23}
\]

This is exact state centrality in that block. No approximation of the density has been made.

There is at most one unpaired word in each count class. Every coordinate of a count vector lies in \(\{0,\ldots,m\}\), so there are at most \((m+1)^d\) such classes. Put

\[
r=\max_i p_i<1.
\]

Every word has density at most \(r^m\), and therefore

\[
0\le\rho^{\otimes m}(f_m)\le(m+1)^d r^m
 \longrightarrow0.
\tag{CTA.24}
\]

To see the last limit explicitly, the ratio of consecutive upper bounds is
\(r((m+2)/(m+1))^d\), which tends to \(r<1\). It is eventually bounded by a number strictly less than one, so the remaining tail decreases geometrically. For \(d=2\) there are exactly \(m+1\) possible counts, giving the sharper bound \((m+1)r^m\).

The same-density condition in (CTA.23) is the reason for partitioning by count vectors. Pairing arbitrary words would keep the square-zero relation but could destroy state centrality.

## 6. Tail units centralize the entire predual

Place \(x^{(n)}\) in legs \(n+1,\ldots,2n\) of \(P_h\), with identity in the other legs, and call the resulting operator \(x_n\). Let \(f_n\) denote its unused projection. Then

\[
x_n^2=0,\qquad
x_n^*x_n+x_nx_n^*=1-f_n,\qquad
\Phi(f_n)\le(n+1)^d r^n\longrightarrow0.
\tag{CTA.25}
\]

Since \(f_n\) is a projection and \(\Phi\) is faithful,
\(\|f_n\|_\Phi^\#=\sqrt{2\Phi(f_n)}\to0\).
CDS02's faithful-state argument makes this strong* convergence on the bounded set of projections.

Each \(x_n\) centralizes \(\Phi\) exactly. To check it on a finite local element, take a finite head containing both that element and the block carrying \(x_n\). The state is the corresponding finite product matrix state, and its density commutes with \(x_n\) by (CTA.23). The trace identity then gives
\(\Phi(x_na)=\Phi(ax_n)\).
Both sides are normal functionals of \(a\), so equality extends from all finite heads to every \(a\in P_h\).

Let \(\mathcal L\) be the union of the finite head matrix algebras. Every fixed \(a,b\in\mathcal L\) commutes with \(x_n\) once \(n\) exceeds the head containing them. The module identity

\[
[x_n,a\Phi b]
 =[x_n,a]\Phi b+a[x_n,\Phi]b+a\Phi[x_n,b]
\tag{CTA.26}
\]

then gives zero for all sufficiently large \(n\).

The span of these functionals \(a\Phi b\) is norm dense in \((P_h)_*\). Indeed \(\mathcal L\Omega\) is dense in the product GNS Hilbert space by construction. The complete coefficient-series description in CP04–06, truncation of one series, and approximation of its finitely many coefficient vectors give precisely that norm density, as in CDS05. Since \(\|x_n\|\le1\), the commutator maps on the predual have norm at most \(2\). Approximation therefore extends the eventual-zero assertion on the dense family to

\[
\|\eta x_n-x_n\eta\|\longrightarrow0
\qquad(\eta\in(P_h)_*).
\tag{CTA.27}
\]


Thus \(x_n\) satisfies condition 3 of the criterion. The algebra has separable predual by Section 4. Sections 2–3 give (CTA.2).

The original tail blocks need not commute with one another: the intervals \(\{n+1,\ldots,2n\}\) can overlap. Exact commutation of the final matrix blocks is supplied by the relative-commutant induction of Section 3.

## 7. Strong lambda-stability and dual absorption

Let \(B\cong B\bar\otimes P_h\) be a normal isomorphism with normal inverse. Tensor it with \(\mathrm{id}_R\), reassociate, use (CTA.2) on the \(P_h\) leg, and return through the original isomorphism:

\[
B\bar\otimes R
 \cong B\bar\otimes P_h\bar\otimes R
 \cong B\bar\otimes P_h
 \cong B.
\tag{CTA.28}
\]

Normality of tensor isomorphisms and their inverses follows from the explicit spatial comparison in TG03; reassociation is a Hilbert-space tensor unitary. This proves (CTA.3) for arbitrary \(B\), without a separable-predual assumption on \(B\).

Set \(d=2\) and use the two eigenvalues of \(h_\lambda\) in Section 1. Equation (CTA.1) is then the actual product defining \(R_\lambda\), so

\[
R_\lambda\cong R_\lambda\bar\otimes R,\qquad
B\cong B\bar\otimes R_\lambda
 \ \Longrightarrow\
B\cong B\bar\otimes R.
\tag{CTA.29}
\]

This is the claimed passage from strong \(\lambda\)-stability to strong stability.

There is now a direct application to the remaining dual-action step. Suppose \(B\) has separable predual, \(\varphi\) is faithful normal, \(\sigma_T^\varphi\) is approximately inner, and \(B\cong B\bar\otimes R_\lambda\) for one \(0<\lambda<1\). By (CTA.29) \(B\) absorbs \(R\). The complete state-transport and central-sequence theorem CDS01–07 therefore proves, for the positive-character dual action,

\[
\left(B\rtimes_{\sigma_T^\varphi}\mathbb Z,\gamma\right)
\cong
\left((B\rtimes_{\sigma_T^\varphi}\mathbb Z)\bar\otimes R,
      \gamma\otimes\beta\right).
\tag{CTA.30}
\]

Both directions are normal and intertwine the actions exactly.

For the AFD type III₁ uniqueness argument, this closes the passage from an established strong-\(\lambda\)-stability statement to tracial stability and then to dual absorption. The separate theorem asserting strong \(\lambda\)-stability for every such factor, and the action-classification steps, still require their own proofs.

## 8. Exact finite checks and boundary cases

**Two binary legs.** Take \(p_1=1/3\), \(p_2=2/3\). In the ordered basis \(11,12,21,22\), the block density is

\[
H=\operatorname{diag}(1/9,2/9,2/9,4/9).
\]

The only nontrivial count class has words \(12,21\), so the construction gives

\[
x=|12\rangle\langle21|,\qquad
x^2=0,\qquad Hx=xH.
\]

Its two support projections have total state mass \(4/9\); the unused mass is \(5/9\). The construction supplies approximate fullness only as the block length grows, not in every small block.

**Four binary legs.** The count-class sizes are \(1,4,6,4,1\). All but the two extreme classes can be paired completely. Therefore at the same probabilities the unused mass is exactly

\[
(1/3)^4+(2/3)^4=\frac{17}{81}.
\tag{CTA.31}
\]

These counts also give seven disjoint matrix pairs and fourteen occupied words out of sixteen.

**A wrong pairing changes the state.** In the two-leg example, pair \(11\) with \(22\) instead and set \(y=|11\rangle\langle22|\). It is still square-zero, but evaluation of its functional commutator at \(y^*\) gives

\[
\Phi(yy^*)-\Phi(y^*y)=\frac19-\frac49=-\frac13.
\tag{CTA.32}
\]

Thus its state commutator norm is at least \(1/3\). Small or square-zero matrix units alone do not guarantee the predual property in the criterion.

**One-dimensional and zero-weight boundaries.** For \(d=1\), every block has one word, all words remain unpaired, and the unused mass is one. The assumption \(d\ge2\) is substantive. If a density is concentrated on one letter, that pure word also remains unpaired with mass one at every length; moreover the reference state is no longer faithful on the full matrix algebra. The argument uses both strict positivity of the leg weights for the faithful-state topology and \(r<1\) for (CTA.24).

**Fullness versus centrality.** The estimates (CTA.25) and (CTA.27) supply different inputs. The first controls how much of the unit is missing; the second controls every normal functional. Section 2 repairs exact fullness, while Section 3 creates exact mutual commutation and proves the normal tensor decomposition. Keeping these steps separate prevents replacing a spatial absorption theorem by a finite-block approximation.

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, proof of Theorem 4.16(i), printed p.396, uses the implication from strong \(\lambda\)-stability to strong stability. The proof above establishes it directly for the specified constant product, and for all constant faithful finite matrix products, through equal-density word pairing and the complete approximate-halving criterion.

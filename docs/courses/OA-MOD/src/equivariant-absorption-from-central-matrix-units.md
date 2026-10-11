# Equivariant absorption from central matrix units

A circle action absorbs a tracial product action when it has central matrix units of the corresponding Fourier degree. The difficult point is to move those units into successive relative commutants while keeping their support equal to one. We first round approximate units, then fill their small invariant complements without imposing an unjustified global commutator estimate on a compressed corner.

## 1. The action and the absorption theorem

Let

\[
R=\bigotimes_{k=1}^{\infty}(M_2(\mathbb C),\operatorname{tr}_2)
\]

be the tracial infinite product, with its specified product representation. On one matrix leg set

\[
b_t=\operatorname{Ad}
 \begin{pmatrix}e^{it}&0\\0&1\end{pmatrix},
\qquad t\in\mathbb T=\mathbb R/2\pi\mathbb Z.
\]

Thus \(b_t(e_{12})=e^{it}e_{12}\). Let \(\beta_t=\bigotimes_{k\ge1}b_t\). Section 7 verifies this action on the whole represented product, its continuity, and its equivariant self-absorption.

For a normal functional \(\varphi\), use

\[
(\varphi x)(a)=\varphi(xa),\qquad
(x\varphi)(a)=\varphi(ax).
\]

A bounded sequence \((x_n)\) is **centralizing** when

\[
\|\varphi x_n-x_n\varphi\|\longrightarrow0
\qquad(\varphi\in M_*).
\tag{ECA.1}
\]

This is also called a strongly central sequence. It is stronger than merely requiring convergence of operator commutators in the strong topology.

**Equivariant absorption theorem.** Let \(M\ne0\) have separable predual, and let \(\theta:\mathbb T\to\operatorname{Aut}(M)\) be a continuous action. Suppose there are centralizing partial isometries \(u_n\in M\) such that

\[
u_n^2=0,\qquad
u_n^*u_n+u_nu_n^*=1,\qquad
\theta_t(u_n)=e^{it}u_n.
\tag{ECA.2}
\]

Then there is a normal isomorphism with normal inverse

\[
\Phi:M\longrightarrow M\bar\otimes R
\]

such that

\[
\Phi\theta_t=(\theta_t\otimes\beta_t)\Phi
\qquad(t\in\mathbb T).
\tag{ECA.3}
\]

The conclusion is conjugacy of actions, with no cocycle perturbation. Neither factoriality nor an a priori tensor-absorption assumption on \(M\) is necessary.

The proof uses the earlier bounded functional-to-vector equivalence, AI04, standard form and its positive representatives, SF04–07 and SF10–11, concrete predual calculations, CP04–07, and the complete summable tensor-splitting theorem, TS01–06. All circle-equivariant rounding and complement-filling arguments are proved below.

## 2. Which products preserve a small error

Write \(z_n\to0\) strongly* to mean convergence for every seminorm

\[
\|z\|_\varphi^\#=
 \bigl(\varphi(z^*z)+\varphi(zz^*)\bigr)^{1/2},
\qquad \varphi\in M_*^+,
\]

where \(\|z\|_\varphi=\sqrt{\varphi(z^*z)}\). On the bounded sets used here this is the intrinsic sigma-strong* topology. In a standard representation it agrees, on bounded sets, with strong* operator convergence: every positive functional is represented by its cone vector, so its two seminorms are the corresponding vector norms; conversely these vectors have complex linear span dense in the Hilbert space. The last density follows from self-duality and pointedness of the standard cone, as in SF04–05.

We need four elementary continuity facts.

**Small bounded sequences centralize.** If \(z_n\to0\) strongly* and \(\sup_n\|z_n\|<\infty\), Cauchy–Schwarz gives

\[
\begin{aligned}
\|\varphi z_n\|&\le
 \sqrt{\varphi(1)}\,\sqrt{\varphi(z_nz_n^*)},\\
\|z_n\varphi\|&\le
 \sqrt{\varphi(1)}\,\sqrt{\varphi(z_n^*z_n)}
\qquad(\varphi\in M_*^+).
\end{aligned}
\tag{ECA.4}
\]

The decomposition of a normal functional into four positive ones in CP07 extends this to all of \(M_*\). In particular such a sequence is centralizing. Adding it to a bounded centralizing sequence preserves centrality.

**Centralizing sequences form a unital *-algebra.** For bounded sequences \(a_n,b_n\), the commutator identity for the two bounded predual module actions gives

\[
\|[a_nb_n,\varphi]\|
 \le \|a_n\|\,\|[b_n,\varphi]\|
    +\|b_n\|\,\|[a_n,\varphi]\|.
\tag{ECA.5}
\]

Adjoints follow by applying the functional adjoint
\(\varphi^*(x)=\overline{\varphi(x^*)}\). Sums and scalar multiples are immediate. These operations preserve the uniform bounds.

**Centralizing sequences commute strongly* with fixed operators.** By AI04 with the pair \((\varphi,\varphi)\), a bounded centralizing sequence satisfies

\[
a_n\xi_\varphi-\xi_\varphi a_n\longrightarrow0
\qquad(\varphi\in M_*^+).
\tag{ECA.6}
\]

The bounded operators \(L_{a_n}-R_{a_n}\) therefore converge strongly to zero on the whole standard Hilbert space, by the cone-span density and their uniform norm bound. Since right multiplication commutes with every left multiplication,

\[
[L_{a_n},L_x]\eta
=(L_{a_n}-R_{a_n})L_x\eta
 -L_x(L_{a_n}-R_{a_n})\eta\longrightarrow0.
\]

Apply the same reasoning to \(a_n^*\) and \(x^*\). Thus

\[
[a_n,x]\longrightarrow0\quad\hbox{strongly*}
\qquad(x\in M).
\tag{ECA.7}
\]


**A small error may be multiplied by a centralizing sequence.** Suppose \(z_n\to0\) strongly*, both sequences are bounded, and \(a_n\) is centralizing. For a cone vector,

\[
\|z_na_n\xi_\varphi\|
\le \|z_n\|\,\|a_n\xi_\varphi-\xi_\varphi a_n\|
   +\|a_n\|\,\|z_n\xi_\varphi\|\longrightarrow0.
\tag{ECA.8}
\]

The adjoint product \(a_n^*z_n^*\xi_\varphi\) is bounded directly. Reversing the order, and then taking adjoints, proves that \(z_na_n\) and \(a_nz_n\) both tend to zero strongly*. Multiplication by a fixed operator is strongly* continuous on bounded sets as well.

Consequently, within bounded centralizing sequences, equality modulo a strongly* null sequence is compatible with sums, products and adjoints. We write \(a_n\sim b_n\) for this equality. We will use only these explicitly proved algebraic rules. We do not multiply a small error by an arbitrary moving bounded operator without justification.

## 3. Exact homogeneous rounding

Let \(A\ne0\) be a von Neumann algebra carrying a circle action \(\gamma\). Suppose \(x_n\in A\) are centralizing contractions such that

\[
x_n^2\longrightarrow0,\qquad
x_n^*x_n+x_nx_n^*\longrightarrow1
\quad\hbox{strongly*},
\qquad
\gamma_t(x_n)=e^{it}x_n.
\tag{ECA.9}
\]

Then there are centralizing square-zero partial isometries \(w_n\in A\) such that

\[
\gamma_t(w_n)=e^{it}w_n,\qquad
w_n-x_n\longrightarrow0,\qquad
w_n^*w_n+w_nw_n^*\longrightarrow1
\quad\hbox{strongly*}.
\tag{ECA.10}
\]

Their support need not yet be exactly one.

Here is the full rounding construction. Work with the relation \(\sim\) from Section 2, and put \(a_n=x_n^*x_n\), \(b_n=x_nx_n^*\). Equations (ECA.9) give

\[
a_n+b_n\sim1,\qquad
a_nb_n\sim b_na_n\sim0,\qquad
a_n^2\sim a_n,\quad b_n^2\sim b_n.
\tag{ECA.11}
\]

For example,

\[
a_n^2=x_n^*b_nx_n
 \sim x_n^*(1-a_n)x_n
 =a_n-(x_n^*)^2x_n^2\sim a_n.
\]

Every moving multiplier in this calculation is centralizing. The product \(a_nb_n=x_n^*x_n^2x_n^*\) is treated by the same rule.

Define the spectral projection

\[
p_n=1_{[1/2,1]}(a_n).
\]

For \(0\le s\le1\),

\[
|1_{[1/2,1]}(s)-s|\le2(s-s^2).
\tag{ECA.12}
\]

Functional calculus therefore gives
\(\|p_n-a_n\|_\varphi\le2\|a_n-a_n^2\|_\varphi\) for every normal positive \(\varphi\); both operators are self-adjoint. Thus \(p_n\sim a_n\). It follows from (ECA.4) that \(p_n\) is centralizing. Since \(a_n\) is fixed by \(\gamma\), so is \(p_n\).

Set

\[
z_n=(1-p_n)x_np_n.
\tag{ECA.13}
\]

The algebraic relations imply \(a_nx_n\sim0\) and \(x_na_n\sim x_n\). Hence \(z_n\sim x_n\), and \(z_n\) is a centralizing contraction of degree one. Its initial support lies under \(p_n\), and its final support lies under \(1-p_n\).

Let \(z_n=s_n|z_n|\) be its polar decomposition, and put

\[
q_n=1_{[1/2,1]}(z_n^*z_n),\qquad w_n=s_nq_n.
\tag{ECA.14}
\]

Thus \(w_n^*w_n=q_n\le p_n\) and \(w_nw_n^*\le1-p_n\), so \(w_n^2=0\). Equivalently,

\[
w_n=z_n g(z_n^*z_n),\qquad
g(s)=
\begin{cases}
s^{-1/2},&1/2\le s\le1,\\
0,&0\le s<1/2.
\end{cases}
\]

This bounded Borel formula proves \(\gamma_t(w_n)=e^{it}w_n\) exactly.

To verify the error on both sides, define

\[
h(s)=
\begin{cases}
(1-\sqrt s)^2,&1/2\le s\le1,\\
s,&0\le s<1/2.
\end{cases}
\qquad 0\le h(s)\le2(s-s^2).
\tag{ECA.15}
\]

For \(s<1/2\), the last bound follows from \(s\le2s(1-s)\). For \(s\ge1/2\), use \((1-\sqrt s)^2\le1-s\le2s(1-s)\). Polar calculus, including the zero kernels where \(h(0)=0\), gives

\[
\begin{aligned}
(w_n-z_n)^*(w_n-z_n)&=h(z_n^*z_n),\\
(w_n-z_n)(w_n-z_n)^*&=h(z_nz_n^*).
\end{aligned}
\tag{ECA.16}
\]

Since \(z_n\sim x_n\), both positive arguments on the right are projections modulo strongly* null sequences, by (ECA.11). Equations (ECA.15)–(ECA.16) imply \(w_n-z_n\to0\) strongly*. Thus \(w_n\) centralizes, \(w_n\sim x_n\), and the last assertion of (ECA.10) follows by the product rule. This proves the rounding assertion without discontinuous functional-calculus continuity claims.

## 4. Invariant corners and exact completion of the support

Retain (ECA.9). Every nonzero \(\gamma\)-invariant projection \(f\in A\) contains a nonzero square-zero degree-one partial isometry.

To prove this, put \(y_n=fx_nf\). These contractions centralize the corner \(fAf\). Indeed, for \(\chi\in(fAf)_*\), the extension \(\widetilde\chi(a)=\chi(faf)\) is normal, and restriction of \([x_n,\widetilde\chi]\) to \(fAf\) is precisely \([y_n,\chi]\). Its norm tends to zero.

Equation (ECA.7) gives \([x_n,f]\to0\) strongly*. The multiplication rules of Section 2 imply

\[
y_n^2\longrightarrow0,\qquad
y_n^*y_n+y_ny_n^*\longrightarrow f
\quad\hbox{strongly* in }fAf.
\tag{ECA.17}
\]

For instance
\(y_n^2-fx_n^2f=fx_n(fx_n-x_nf)f\);
the small commutator can be multiplied by centralizing \(x_n\), and the outer fixed factors cause no problem. The two support products are expanded in the same way. The degree condition survives because \(f\) is fixed. Section 3, in \(fAf\) with unit \(f\), gives partial isometries \(r_n\) whose support sums tend to \(f\). A normal positive functional with positive value on \(f\) shows that some \(r_n\ne0\). This proves the claim.

The claim permits **exact filling** of any invariant projection \(f\), with no commutator bound required during the filling. Consider all square-zero degree-one partial isometries \(v\in fAf\), including zero. Order them by orthogonal extension: \(v\preceq w\) when

\[
w=v+r,\qquad
r\in(f-v^*v-vv^*)A(f-v^*v-vv^*)
\]

is another square-zero partial isometry of degree one. The initial and final support projections both increase along a chain. If \(v_i\preceq v_j\), then

\[
\|(v_j-v_i)\eta\|^2
 =\langle(v_j^*v_j-v_i^*v_i)\eta,\eta\rangle,
\]

and the analogous formula for adjoints uses the final projections. Increasing projections have strong limits, so the chain has a strong* limit \(v\in fAf\). Its norm is at most one. Products pass to the limit on bounded strong* convergent nets, giving the required partial-isometry and square-zero relations. A normal automorphism preserves bounded strong* convergence, so \(v\) still has degree one. The orthogonal-extension equations pass to the limit as well. Thus each chain has an upper bound.

Zorn's lemma gives a maximal \(v\). Its unused projection
\(g=f-v^*v-vv^*\) is invariant. If \(g\ne0\), the preceding corner claim supplies a nonzero degree-one square-zero partial isometry in \(gAg\), contradicting maximality. Therefore

\[
v^*v+vv^*=f.
\tag{ECA.18}
\]


Now apply this completion to

\[
f_n=1-w_n^*w_n-w_nw_n^*
\]

from Section 3, choosing a filler \(r_n\in f_nAf_n\) with full support \(f_n\), or zero if \(f_n=0\). Put \(v_n=w_n+r_n\). Since \(f_n\to0\) strongly*,

\[
r_n^*r_n\le f_n,\qquad r_nr_n^*\le f_n
\]

imply \(r_n\to0\) strongly*. Consequently

\[
\begin{gathered}
v_n^2=0,\qquad v_n^*v_n+v_nv_n^*=1,\qquad
\gamma_t(v_n)=e^{it}v_n,\\
v_n-x_n\longrightarrow0\quad\hbox{strongly*}.
\end{gathered}
\tag{ECA.19}
\]

Equation (ECA.4) proves that \(v_n\) is centralizing. Centrality is recovered from the small size of the entire final complement, rather than from a global centrality assertion about each intermediate compressed corner.

## 5. Moving the units into a finite relative commutant

Let \(D\subset M\) be a unital full matrix algebra invariant under \(\theta\), and put \(A=D'\cap M\). We prove that \(A\) contains a sequence satisfying (ECA.2) which is still centralizing on the whole of \(M\).

The explicit matrix-coordinate theorem TS01 gives

\[
M\cong D\bar\otimes A
\]

by multiplication, and the normal tracial expectation

\[
E_D:M\longrightarrow A,\qquad
E_D(x)=\frac1d\sum_{i,a=1}^d e_{ai}xe_{ia}
\tag{ECA.20}
\]

for matrix units of \(D\). It is a contraction and is faithful. It is also \(\theta\)-equivariant. Indeed \(\theta_t\) preserves both \(D\) and \(A\); under the multiplication isomorphism it acts as the tensor product of its restrictions. Every automorphism of a full matrix algebra preserves its normalized trace. To check this last statement directly, a tracial state has equal values on equivalent diagonal matrix units and vanishes on off-diagonal units, so it is the normalized trace. Therefore \(\operatorname{tr}_D\otimes\mathrm{id}_A\) commutes with these tensor-product automorphisms.

For the original sequence in (ECA.2), set \(x_n=E_D(u_n)\). Because (ECA.7) applies to each fixed matrix unit, the finite formula (ECA.20) gives

\[
x_n-u_n
=\frac1d\sum_{i,a}e_{ai}(u_ne_{ia}-e_{ia}u_n)
\longrightarrow0\quad\hbox{strongly*}.
\tag{ECA.21}
\]

The constant term is \(u_n\), since
\(d^{-1}\sum_{i,a}e_{ai}e_{ia}=1\).
Thus \(x_n\) centralizes all of \(M_*\), and it has degree one. The product rules of Section 2 give

\[
x_n^2\longrightarrow0,\qquad
x_n^*x_n+x_nx_n^*\longrightarrow1
\quad\hbox{strongly* in }M.
\tag{ECA.22}
\]


The sequence also centralizes \(A_*\). For \(\chi\in A_*\), extend it by \(\chi E_D\). Bimodularity of \(E_D\) shows that its commutator with \(x_n\in A\), restricted to \(A\), is the required corner-free commutator. Normal functionals on \(A\) have these normal extensions, so the strong* convergence in (ECA.22) holds intrinsically in \(A\) too.

Apply Sections 3–4 inside \(A\). The spectral calculations in Section 3 also prove convergence in \(M\), because (ECA.22) and centrality hold there and the same formulas are used. In particular the unused supports \(f_n\) tend to zero strongly* in \(M\). The fillers from \(f_nAf_n\) consequently tend to zero strongly* in \(M\) as well. We obtain full-support degree-one square-zero partial isometries \(v_n\in A\) with

\[
v_n-u_n\longrightarrow0\quad\hbox{strongly* in }M.
\tag{ECA.23}
\]

They centralize every functional of \(M_*\), by (ECA.4). This proves the required relative-commutant construction with both the algebraic relations and the ambient functional estimates.

## 6. Commuting blocks with summable errors

Choose a norm-dense sequence \((\varphi_j)\) in the normal state space of \(M\). This is possible because \(M_*\) is separable. Its complex linear span is norm dense in \(M_*\), by the positive decomposition in CP07 and normalization of nonzero positive functionals.

We construct mutually commuting unital copies \(D_k\cong M_2\) generated by partial isometries \(v_k\), with

\[
\theta_t(v_k)=e^{it}v_k,\qquad
v_k^2=0,\qquad v_k^*v_k+v_kv_k^*=1,
\]

and

\[
\|[\varphi_j,v_k]\|\le2^{-k}
\qquad(1\le j\le k).
\tag{ECA.24}
\]

For the first step use the original centralizing sequence. Suppose the first \(k-1\) blocks have been chosen. They generate a unital full matrix algebra
\(D=D_1\vee\cdots\vee D_{k-1}\), by TS03's exact matrix-unit multiplication argument. Their eigenvector relations make \(D\) invariant. Section 5 supplies a centralizing sequence of full halving units in \(D'\cap M\), all of degree one. Choose a sufficiently late member to satisfy the finitely many estimates (ECA.24), and use it as \(v_k\).

Define

\[
e_{12}^{(k)}=v_k,\quad e_{21}^{(k)}=v_k^*,\quad
e_{11}^{(k)}=v_kv_k^*,\quad e_{22}^{(k)}=v_k^*v_k.
\]

These are full matrix units, and their circle action is exactly \(b_t\). For each fixed \(j\), the finite initial segment of the series of commutator norms is finite, and the tail is bounded by \(\sum_{k\ge j}2^{-k}\). Thus

\[
\sum_{k=1}^\infty\|[\varphi_j,v_k]\|<\infty.
\tag{ECA.25}
\]


Apply TS06 with constant parameter \(1\). Its matrix-functional estimate, followed by the complete tail-expectation and spatial-splitting construction in TS01–05, proves

\[
P=\bigvee_{k\ge1}D_k\cong
 \bigotimes_{k\ge1}(M_2,\operatorname{tr}_2)=R,
\qquad
M\cong P\bar\otimes Q,\quad Q=P'\cap M,
\tag{ECA.26}
\]

where the second isomorphism is multiplication and both it and its inverse are normal. These are whole von Neumann algebra identifications; agreement of finite matrix moments alone is not being substituted for normality or generation.

The action preserves \(P\), hence also \(Q\). Under the product identification of TS05 it restricts to \(\beta\) on \(P\), because the two normal automorphisms agree on every finite head. Write \(\theta'_t=\theta_t|_Q\). Then multiplication intertwines

\[
(M,\theta)\cong(R\bar\otimes Q,\beta\otimes\theta').
\tag{ECA.27}
\]

No factoriality of \(Q\) or \(M\) was used.

## 7. Product actions and the final conjugacy

We verify the product-action facts used above. In the GNS Hilbert space of the product trace, act on finite-support tensor vectors by

\[
B_t\left(\bigotimes_{k=1}^n a_k\Omega_k\right)
 =\bigotimes_{k=1}^n b_t(a_k)\Omega_k.
\tag{ECA.28}
\]

Trace preservation makes this an isometry, and \(B_{-t}\) is its inverse. Reference vectors are fixed, so the formula is consistent as the finite support grows. It extends to a unitary on the completed product Hilbert space. On the dense finite-support vectors it is continuous in \(t\), and the unitary bound extends continuity to all vectors. It implements the product action on each local algebra and therefore on the generated von Neumann algebra. The estimate \(\|\omega_{\xi_t,\eta_t}-\omega_{\xi,\eta}\|\le\|\xi_t-\xi\|\|\eta_t\|+\|\xi\|\|\eta_t-\eta\|\), applied to the implementing unitaries, gives norm continuity of each vector functional. The summable coefficient description of the predual in CP04–06 extends this to pointwise norm continuity on the whole predual. Thus \(\beta\) is a continuous circle action on the entire \(R\).

There is an explicit trace-preserving normal isomorphism

\[
J:R\bar\otimes R\longrightarrow R
\]

which sends the \(k\)-th leg of the first factor to leg \(2k-1\), and the \(k\)-th leg of the second factor to leg \(2k\). On the product GNS spaces, interleaving the two finite-support tensors preserves every inner product. Every finite-support tensor in the target has a preimage obtained by separating its odd and even legs. Therefore this map extends to an onto unitary. It intertwines all generating local matrix algebras, proving that \(J\) and its inverse are normal on the generated von Neumann algebras. It also proves, leg by leg and then by normality,

\[
J(\beta_t\otimes\beta_t)=\beta_tJ.
\tag{ECA.29}
\]


Let \(\Psi:R\bar\otimes Q\to M\) be the equivariant isomorphism from (ECA.27). An isomorphism from \(M\bar\otimes R\) onto \(M\) is the following composite:

\[
M\bar\otimes R
 \xrightarrow{\ \Psi^{-1}\otimes\mathrm{id}\ }
 R\bar\otimes Q\bar\otimes R
 \xrightarrow{\ \text{swap the last two factors}\ }
 R\bar\otimes R\bar\otimes Q
 \xrightarrow{\ J\otimes\mathrm{id}\ }
 R\bar\otimes Q
 \xrightarrow{\ \Psi\ } M.
\tag{ECA.30}
\]

The tensor-factor swap is implemented by the corresponding Hilbert-space tensor flip; hence it, too, is normal with normal inverse. Equations (ECA.27) and (ECA.29) show that (ECA.30) intertwines \(\theta\otimes\beta\) with \(\theta\). Its inverse is the required \(\Phi\) in (ECA.3). This proves the full theorem.

In particular it proves the classical statement for a separable strongly stable factor. The separate strong-stability assumption is redundant once the full centralizing eigenvector sequence (ECA.2) is given: the proof constructs the requisite tracial factor and the equivariant splitting from that sequence.

## 8. Why the corner and degree conditions matter

**The model realizes the hypotheses.** In \((R,\beta)\), put \(u_n=e_{12}\) in the \(n\)-th tensor leg and the identity elsewhere. These have exactly the relations and degree in (ECA.2). To see centrality in predual norm, first take functionals

\[
x\longmapsto\tau(a x b)
\]

with \(a,b\) in a fixed finite head. Every later \(u_n\) commutes with \(a,b\), and traciality gives an exactly zero functional commutator. Their span is norm dense in \(R_*\): in the faithful trace GNS representation finite-head vectors are dense, rank-one vector coefficients approximate general summable coefficients in norm, and CP04–06 identifies their restrictions with the predual. The uniform bound \(\|u_n\|=1\) extends convergence to every normal functional.

**Compression need not preserve ambient centrality.** Let \(M=M_2\bar\otimes R\), let \(u_n=1\otimes e_{12}^{(n)}\), and put \(f=e_{11}\otimes1\). This is a centralizing sequence before compression. Set

\[
\omega(x)=\langle x(1,1)/\sqrt2,(1,1)/\sqrt2\rangle,\qquad
\varphi=\omega\otimes\tau.
\]

For \(y_n=fu_nf\), test its functional commutator on the norm-one operator

\[
a_n=e_{21}\otimes(e_{12}^{(n)})^*.
\]

Since \(e_{11}e_{21}=0\), \(e_{21}e_{11}=e_{21}\), and
\(\tau((e_{12}^{(n)})^*e_{12}^{(n)})=1/2\), one gets

\[
|\varphi(y_na_n)-\varphi(a_ny_n)|=\frac14.
\tag{ECA.31}
\]

Thus \(\|[\varphi,y_n]\|\ge1/4\) for every \(n\), although \(y_n\) is centralizing in \(fMf\). This is why Section 4 fills a complement without asserting ambient commutator bounds there. Only when the entire remaining projection tends strongly* to zero do the unrestricted fillers become harmless in ambient predual norm.

**The degree is substantive.** For the trivial circle action, the identity
\(\theta_t(u)=e^{it}u\) for all \(t\) forces \(u=0\), for example at \(t=\pi\). Hence no full halving sequence can have degree one. The theorem does not incorrectly identify a trivial action with its product with the nontrivial \(\beta\).

**Centrality is substantive too.** A single copy \(M_2\), with the action \(b\), has a full degree-one halving unit \(e_{12}\). But the constant sequence \(e_{12}\) is not centralizing: for \(\omega_{11}(x)=x_{11}\), evaluation at \(e_{21}\) gives

\[
|(\omega_{11}e_{12}-e_{12}\omega_{11})(e_{21})|=1.
\tag{ECA.32}
\]

One finite matrix block cannot replace the centralizing sequence needed to build arbitrarily many commuting blocks.

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Lemma 4.22, printed pp.393–395. The proof here supplies an explicit homogeneous spectral rounding, an exact filling of invariant complements, the ambient predual estimates, and the complete equivariant tensor identification. The intermediate corner estimates are distinguished from estimates on the ambient algebra.

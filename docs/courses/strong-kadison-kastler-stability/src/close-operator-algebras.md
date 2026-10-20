# Close operator algebras

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two operator algebras acting on the same Hilbert space are close when every contraction of either one lies near a contraction of the other. Kadison and Kastler introduced this distance in 1972 and asked whether sufficiently close von Neumann algebras are conjugate by a unitary near the identity. This course proves that they are, with a tolerance that depends only on the required closeness of the unitary to the identity: Theorem 2.1 below [OpenAI-289]. The course also proves that the corresponding statement fails for separable C\*-algebras [OpenAI-289b] and for one-sided near inclusions of von Neumann algebras [OpenAI-289c]. This lesson fixes the distances, states the three theorems, and proves the elementary tools used throughout: estimates for conjugation by unitaries close to the identity, the distance from an operator to a commutant, the conjugacy of close representations, and the absorption of matrix levels by infinite families of isometries.

We use: Corollary 4.5 of [Completely bounded homomorphisms and similarity](course:kadisons-similarity-problem/completely-bounded-homomorphisms-and-similarity#4-rectangular-derivations) (Arveson's distance formula); from the foundations course, [Corollary 9.7(a)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10) (the unit ball of \(B(H)\) is weakly compact), [Proposition 12.1](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras#OA-FND-WA-19) (the kernel and image of a normal representation) and [Corollary 13.5](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-17) (a properly infinite projection is a sum of countably many mutually orthogonal projections equivalent to it); and the continuous functional calculus.

## 1. Distances between operator algebras

All Hilbert spaces are complex, and inner products are linear in the first variable. For a subset \(X\subseteq B(H)\) we write \(X_1\) for the set of its elements of norm at most \(1\). A C\*-algebra or von Neumann algebra on \(H\) is *unital* when it contains the identity \(I=I_H\). For \(x\in B(H)\) and \(Y\subseteq B(H)\), \(\operatorname{dist}(x,Y)=\inf_{y\in Y}\|x-y\|\).

**Definition 1.1** (Kadison–Kastler distance). For subsets \(X,Y\subseteq B(H)\) put
\[
\delta(X,Y)=\sup_{x\in X_1}\operatorname{dist}(x,Y_1).
\]
For C\*-algebras \(A,B\subseteq B(H)\) the *Kadison–Kastler distance* is
\[
d(A,B)=\max\{\delta(A,B),\,\delta(B,A)\},
\]
the Hausdorff distance between the two unit balls in operator norm.

**Definition 1.2** (near inclusions). Let \(\gamma>0\). We write \(A\subset_\gamma B\) if there is \(\gamma'<\gamma\) such that \(\operatorname{dist}(x,B)\le\gamma'\) for every \(x\in A_1\). The approximating element of \(B\) is not required to be a contraction. The *one-sided gap* is
\[
\gamma(A,B)=\sup_{x\in A_1}\operatorname{dist}(x,B).
\]

**Definition 1.3** (matrix levels). For \(n\ge1\), \(M_n(A)\) is the algebra of \(n\times n\) matrices over \(A\), acting on \(H^n=H\oplus\dots\oplus H\) with its operator norm. For a linear map \(T:A\to B(K)\), the map \(T_n:M_n(A)\to B(K^n)\) applies \(T\) entrywise, and \(\|T\|_{\rm cb}=\sup_n\|T_n\|\); \(T\) is *completely bounded* when this is finite. For \(x\in B(H)\) we write \(x^{(n)}\) for the diagonal matrix with entries \(x\). The *completely bounded distance* is
\[
d_{\rm cb}(A,B)=\sup_{n\ge1}d\bigl(M_n(A),M_n(B)\bigr).
\]
For \(h\in B(H)\), \(\operatorname{ad}_h(x)=[h,x]=hx-xh\).

Since \(n=1\) is allowed, \(d(A,B)\le d_{\rm cb}(A,B)\).

**Lemma 1.4** (normalizing approximants).

1. If \(\|x\|\le1\) and \(\|x-y\|\le r\), then \(y_0=y/\max\{1,\|y\|\}\) satisfies \(\|y_0\|\le1\) and \(\|x-y_0\|\le2r\).
2. If \(A\subset_\gamma B\), then \(\delta(A,B)<2\gamma\). If \(d(A,B)<\gamma\), then \(A\subset_\gamma B\) and \(B\subset_\gamma A\).
3. For C\*-algebras \(A,B,C\subseteq B(H)\), \(d(A,C)\le d(A,B)+d(B,C)\).

**Proof.** (1) If \(\|y\|\le1\) then \(y_0=y\). Otherwise \(\|y-y_0\|=\|y\|-1\)\(\le\|y-x\|+\|x\|-1\le r\), and \(\|x-y_0\|\le2r\).

(2) Let \(\gamma'<\gamma\) be as in Definition 1.2, \(x\in A_1\) and \(\eta>0\). Choose \(y\in B\) with \(\|x-y\|\le\gamma'+\eta\). Part (1) gives \(y_0\in B_1\) with \(\|x-y_0\|\le2\gamma'+2\eta\). Hence \(\delta(A,B)\le2\gamma'<2\gamma\). Conversely, if \(d(A,B)<\gamma\), take \(\gamma'=d(A,B)\): every \(x\in A_1\) has \(\operatorname{dist}(x,B)\le\operatorname{dist}(x,B_1)\le\gamma'\), and symmetrically.

(3) For \(x\in A_1\) and \(y\in B_1\), \(\operatorname{dist}(x,C_1)\)\(\le\|x-y\|+\operatorname{dist}(y,C_1)\)\(\le\|x-y\|+\delta(B,C)\). Taking the infimum over \(y\) and then the supremum over \(x\) gives \(\delta(A,C)\le\delta(A,B)+\delta(B,C)\). Exchange \(A\) and \(C\). \(\square\)

**Lemma 1.5** (conjugation by a unitary near the identity). Let \(v\in B(H)\) be unitary and \(A,B\subseteq B(H)\) C\*-algebras.

1. \(\|vxv^*-x\|\le2\|v-I\|\,\|x\|\) for every \(x\in B(H)\).
2. \(d(A,vBv^*)\le d(A,B)+2\|v-I\|\) and \(d_{\rm cb}(A,vBv^*)\)\(\le d_{\rm cb}(A,B)+2\|v-I\|\).
3. For unitaries \(v_1,\dots,v_k\), \(\|v_1\cdots v_k-I\|\le\sum_j\|v_j-I\|\).

**Proof.** (1) \(vxv^*-x=(v-I)xv^*+x(v^*-I)\), and \(\|v^*-I\|=\|v-I\|\). (2) The map \(x\mapsto vxv^*\) carries \(B_1\) onto \((vBv^*)_1\), so (1) gives \(d(B,vBv^*)\le2\|v-I\|\); apply Lemma 1.4(3). At matrix level \(n\), \(M_n(vBv^*)=v^{(n)}M_n(B)v^{(n)*}\) and \(\|v^{(n)}-I\|=\|v-I\|\). (3) Induction on \(k\), using
\[
\begin{gathered}
\begin{aligned}
v_1\cdots v_k-I&=v_1\cdots v_{k-1}(v_k-I)\\
&\quad +(v_1\cdots v_{k-1}-I).
\end{aligned}\\
\square
\end{gathered}
\]

## 2. Three theorems

**Theorem 2.1** (strong Kadison–Kastler stability [OpenAI-289]). For every \(\varepsilon>0\) there is \(\delta(\varepsilon)>0\) with the following property. Let \(H\) be a Hilbert space and \(M,N\subseteq B(H)\) unital von Neumann algebras with \(d(M,N)<\delta(\varepsilon)\). Then there is a unitary \(u\in B(H)\) with
\[
uMu^*=N,\qquad\|u-I\|<\varepsilon.
\]

The number \(\delta(\varepsilon)\) depends on \(\varepsilon\) alone: it is the same for all pairs of algebras, of every type, in every representation and on Hilbert spaces of every dimension. The converse direction is elementary.

**Proposition 2.2.** If \(M,N\subseteq B(H)\) are unital C\*-algebras and \(uMu^*=N\) for a unitary \(u\), then \(d_{\rm cb}(M,N)\le2\|u-I\|\) and \(d(M',N')\le2\|u-I\|\).

**Proof.** Lemma 1.5(2) with \(B=M\) gives \(d_{\rm cb}(M,uMu^*)\le2\|u-I\|\). Since \(N'=uM'u^*\), the same lemma applies to the commutants. \(\square\)

So Theorem 2.1 also says that a small ordinary distance forces a small completely bounded distance and a small distance between the commutants, uniformly over all algebras and representations (the corollary in the last lesson on the main theorem). The proof of Theorem 2.1 occupies most of this course. It first treats finite factors on separable Hilbert spaces (the next six lessons), then infinite factors on separable spaces, then arbitrary von Neumann algebras on separable spaces, and finally arbitrary Hilbert spaces. One feature runs through all of it: every estimate must be independent of the algebras. For a single factor \(M\) one might prove a statement with a tolerance \(\delta_M(\varepsilon)>0\) valid in every representation of \(M\); positivity of each \(\delta_M(\varepsilon)\) would not give \(\inf_M\delta_M(\varepsilon)>0\), which is what Theorem 2.1 asserts.

The next two theorems show that the hypotheses of Theorem 2.1 cannot be weakened in two natural directions.

**Theorem 2.3** (close separable C\*-algebras [OpenAI-289b]). For every \(\varepsilon>0\) there are a separable Hilbert space \(H\) and unital norm-separable C\*-algebras \(A,B\subseteq B(H)\) with
\[
d(A,B)<\varepsilon,\qquad A''=B'',
\]
such that no unitary \(u\in B(H)\) satisfies \(uAu^*=B\).

**Theorem 2.4** (one-sided near inclusions [OpenAI-289c]). There are \(\varepsilon_0>0\), separable Hilbert spaces \(H_n\) and unital von Neumann algebras \(M_n,N_n\subseteq B(H_n)\) with \(\gamma(M_n,N_n)\to0\), such that for all sufficiently large \(n\) unitaries \(u\) with \(uM_nu^*\subseteq N_n\) exist, and every such unitary satisfies \(\|u-I\|\ge\varepsilon_0\).

Theorem 2.3 is proved in the lessons [Convergent sequences and a relative tensor norm](convergent-sequences-and-a-relative-tensor-norm.md) and [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md); Theorem 2.4 in [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md) and [Almost commuting matrices and small embeddings](almost-commuting-matrices-and-small-embeddings.md). These four lessons use only the present lesson and one another.

Earlier positive results covered type I algebras, amenable algebras, close separable nuclear C\*-algebras, and particular nonamenable II\(_1\) factors; [CCSSWW, Section 1] and [CSSWW] survey this work and its connection with Kadison's similarity problem, which the course [Kadison's similarity problem](course:kadisons-similarity-problem/completely-bounded-homomorphisms-and-similarity) treats.

## 3. Commutants and close representations

**Proposition 3.1** (distance to a commutant). Let \(A\subseteq B(H)\) be a unital C\*-algebra and \(h\in B(H)\). Then
\[
\operatorname{dist}(h,A')=\tfrac12\|\operatorname{ad}_h|_A\|_{\rm cb},
\]
and the distance is attained.

**Proof.** This is Corollary 4.5 of [Completely bounded homomorphisms and similarity](course:kadisons-similarity-problem/completely-bounded-homomorphisms-and-similarity#4-rectangular-derivations). \(\square\)

**Corollary 3.2.** Let \(A,B\subseteq B(H)\) be unital C\*-algebras with \(d_{\rm cb}(A,B)\le\gamma\). For \(h\in A'\),
\[
\begin{gathered}
\|\operatorname{ad}_h|_B\|_{\rm cb}\le2\gamma\|h\|,\\
\operatorname{dist}(h,B')\le\gamma\|h\|.
\end{gathered}
\]
Consequently \(d(A',B')\le2\gamma\).

**Proof.** Let \(Y\in M_n(B)_1\) and \(\eta>0\). Choose \(X\in M_n(A)_1\) with \(\|Y-X\|\le\gamma+\eta\). Since \(h\in A'\), \(h^{(n)}\) commutes with \(X\), so
\[
\begin{aligned}
\|[h^{(n)},Y]\|&=\|[h^{(n)},Y-X]\|\\
&\le2\|h\|(\gamma+\eta).
\end{aligned}
\]
This proves the first bound, and Proposition 3.1 gives the second, with an attained distance: some \(z\in B'\) has \(\|h-z\|\le\gamma\|h\|\). For \(h\in(A')_1\), Lemma 1.4(1) turns \(z\) into an element of \((B')_1\) within \(2\gamma\) of \(h\). Hence \(\delta(A',B')\le2\gamma\), and by symmetry \(d(A',B')\le2\gamma\). \(\square\)

A *representation* of a von Neumann algebra \(P\) on \(H\) is a unital \(*\)-homomorphism \(P\to B(H)\); it is *normal* when it is continuous for the \(\sigma\)-weak topologies.

**Lemma 3.3** (close representations). Let \(P\) be a von Neumann algebra and \(\rho,\theta:P\to B(H)\) normal representations with \(\|\rho-\theta\|_{\rm cb}\le e<2\). There is a unitary \(u\in B(H)\) with
\[
\begin{gathered}
u\rho(x)u^*=\theta(x)\quad(x\in P),\\
\|u-I\|\le e.
\end{gathered}
\]

**Proof.** On \(H\oplus H\) let \(\pi(x)=\rho(x)\oplus\theta(x)\), a normal representation of \(P\), and let \(S(\xi,\eta)=(\eta,\xi)\) be the flip. By [Proposition 12.1](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras#OA-FND-WA-19), \(\ker\pi=P(1-z)\) for a central projection \(z\), \(\pi(P)\) is a von Neumann algebra, and \(\pi\) restricts to a \(*\)-isomorphism of \(Pz\) onto \(\pi(P)\). The amplifications of an injective \(*\)-homomorphism are injective \(*\)-homomorphisms, hence isometric. So every \(Y\in M_n(\pi(P))\) is \(\pi_n(X)\) for some \(X\in M_n(Pz)\) with \(\|X\|=\|Y\|\).

Identify \((H\oplus H)^n\) with \(H^n\oplus H^n\). Then \(S^{(n)}\) is the flip of the two summands, \(\pi_n(X)=\rho_n(X)\oplus\theta_n(X)\), and
\[
\begin{aligned}
[S^{(n)},\pi_n(X)]&=\begin{pmatrix}0&\theta_n(X)-\rho_n(X)\\ \rho_n(X)-\theta_n(X)&0\end{pmatrix},
\end{aligned}
\]
of norm \(\|\theta_n(X)-\rho_n(X)\|\le e\|X\|=e\|Y\|\). Hence \(\|\operatorname{ad}_S|_{\pi(P)}\|_{\rm cb}\le e\), and Proposition 3.1 gives \(D\in\pi(P)'\) with \(\|D-S\|\le e/2\).

Write \(D\) as a \(2\times2\) operator matrix and let \(T\) be its lower left entry. The lower left entry of \(D-S\) is \(T-I\), so \(r:=\|T-I\|\le e/2<1\). Comparing lower left entries in \(D\pi(x)=\pi(x)D\) gives \(T\rho(x)=\theta(x)T\) for all \(x\in P\). Applying this to \(x^*\) and taking adjoints gives \(\rho(x)T^*=T^*\theta(x)\), so
\[
\rho(x)T^*T=T^*\theta(x)T=T^*T\rho(x).
\]
Since \(\|T\xi\|\) lies between \((1-r)\|\xi\|\) and \((1+r)\|\xi\|\), the spectrum of \(|T|=(T^*T)^{1/2}\) lies in \([1-r,1+r]\). So \(T\) is invertible, \(|T|^{-1}\) commutes with \(\rho(P)\), and \(u=T|T|^{-1}\) is a unitary with
\[
\begin{aligned}
u\rho(x)&=T\rho(x)|T|^{-1}\\
&=\theta(x)T|T|^{-1}=\theta(x)u.
\end{aligned}
\]
Finally \(u-T=u(I-|T|)\), so \(\|u-I\|\le\|I-|T|\|+\|T-I\|\)\(\le2r\le e\). \(\square\)

The constant \(e\) in Lemma 3.3 comes from the factor \(\tfrac12\) in Proposition 3.1; [OpenAI-289, Lemma 2.3] states the bound \(4e\) for \(e<1/4\). Exercise 5.3 shows that Lemma 3.3 is sharp up to a factor \(2\).

## 4. Infinite families of isometries

**Definition 4.1.** An *infinite family of isometries* in a von Neumann algebra \(P\subseteq B(H)\) is a sequence \((s_i)_{i\ge1}\) in \(P\) with \(s_i^*s_j=\delta_{ij}I\) and \(\sum_is_is_i^*=I\), the sum converging strongly.

If \(P\) is properly infinite, it contains such a family: by [Corollary 13.5](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-17), \(I=\sum_ie_i\) with mutually orthogonal projections \(e_i\) equivalent to \(I\), and partial isometries \(s_i\in P\) with \(s_i^*s_i=I\) and \(s_is_i^*=e_i\) form the family.

**Lemma 4.2** (absorbing matrix levels). Let \((s_i)\) be an infinite family of isometries in \(B(H)\), and \(S\) the von Neumann algebra it generates. For every \(n\ge1\) there are \(t_1,\dots,t_n\in S\) with
\[
t_k^*t_l=\delta_{kl}I,\qquad\sum_{k=1}^nt_kt_k^*=I.
\]
The operator \(V_n:H^n\to H\), \(V_n(\xi_1,\dots,\xi_n)=\sum_kt_k\xi_k\), is unitary. For every von Neumann algebra \(P\supseteq S\) and every \(Y\in S'\),
\[
\begin{aligned}
&V_nM_n(P)V_n^*=P,\\
&V_n[x_{kl}]V_n^*=\textstyle\sum_{k,l}t_kx_{kl}t_l^*,\\
&V_nY^{(n)}V_n^*=Y.
\end{aligned}
\]

**Proof.** Put \(t_k=\sum_{i\ge1}s_{n(i-1)+k}s_i^*\). On a vector \(\xi\) the terms are mutually orthogonal, with \(\|s_{n(i-1)+k}s_i^*\xi\|^2=\langle s_is_i^*\xi,\xi\rangle\), summing to \(\|\xi\|^2\); so the series converges strongly and \(t_k\in S\). Since \(n(i-1)+k=n(j-1)+l\) with \(1\le k,l\le n\) forces \(i=j\) and \(k=l\), we get \(s_{n(i-1)+k}^*t_l\xi=\delta_{kl}s_i^*\xi\), hence
\[
\begin{aligned}
t_k^*t_l\xi&=\sum_is_is_{n(i-1)+k}^*t_l\xi\\
&=\delta_{kl}\sum_is_is_i^*\xi=\delta_{kl}\xi.
\end{aligned}
\]
Also \(t_kt_k^*=\sum_is_{n(i-1)+k}s_{n(i-1)+k}^*\), and summing over \(k\) gives \(\sum_ms_ms_m^*=I\). The adjoint of \(V_n\) is \(\xi\mapsto(t_1^*\xi,\dots,t_n^*\xi)\); the two relations say \(V_n^*V_n=I\) and \(V_nV_n^*=I\). The formula for \(V_n[x_{kl}]V_n^*\) is a direct computation; it lies in \(P\) when the \(x_{kl}\) do, and every \(x\in P\) equals \(V_n[t_k^*xt_l]V_n^*\). Finally \(V_nY^{(n)}V_n^*=\sum_kt_kYt_k^*\)\(=Y\sum_kt_kt_k^*=Y\). \(\square\)

**Corollary 4.3.** If unital von Neumann algebras \(M,N\subseteq B(H)\) contain a common infinite family of isometries, then \(d_{\rm cb}(M,N)=d(M,N)\).

**Proof.** The unitary \(V_n\) of Lemma 4.2 maps the unit balls of \(M_n(M)\) and \(M_n(N)\) onto those of \(M\) and \(N\), preserving distances, so \(d(M_n(M),M_n(N))=d(M,N)\) for every \(n\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that \(d(A,B)\le1\) for all unital C\*-algebras \(A,B\subseteq B(H)\), and that \(d(A,B)=0\) only if \(A=B\).

**Exercise 5.2.** Show that \(\gamma(A,B)\le\delta(A,B)\le2\gamma(A,B)\), and that \(\gamma(A,B)=0\) exactly when \(A\subseteq B\).

**Exercise 5.3.** Let \(\rho\) be a normal representation of a von Neumann algebra \(P\) on \(H\) and \(\theta=v\rho(\cdot)v^*\) for a unitary \(v\). Show that \(\|\rho-\theta\|_{\rm cb}\le2\|v-I\|\). Deduce that, when \(\|\rho-\theta\|_{\rm cb}<2\), the infimum \(m\) of \(\|u-I\|\) over all unitaries \(u\) with \(u\rho(\cdot)u^*=\theta\) satisfies \(m\le\|\rho-\theta\|_{\rm cb}\le2m\).

**Exercise 5.4.** Show that the sequence \(d(M_n(A),M_n(B))\), \(n\ge1\), is nondecreasing.

**Exercise 5.5.** Show that \(B(\ell^2)\) contains an infinite family of isometries and that a von Neumann algebra in which every isometry is unitary contains none.

## 6. Solutions

**Solution 5.1.** For \(x\in A_1\), \(0\in B_1\) gives \(\operatorname{dist}(x,B_1)\le\|x\|\le1\). If \(d(A,B)=0\), every \(x\in A_1\) is a norm limit of elements of \(B_1\); \(B\) is norm closed, so \(x\in B\). Hence \(A\subseteq B\), and symmetrically.

**Solution 5.2.** \(\operatorname{dist}(x,B)\le\operatorname{dist}(x,B_1)\) gives the first inequality, and Lemma 1.4(1) the second. If \(\gamma(A,B)=0\), every element of \(A_1\) is a limit of elements of \(B\), hence lies in \(B\); scaling gives \(A\subseteq B\). The converse is immediate.

**Solution 5.3.** At matrix level \(n\), \(\theta_n(X)=v^{(n)}\rho_n(X)v^{(n)*}\) and Lemma 1.5(1) gives \(\|\theta_n(X)-\rho_n(X)\|\le2\|v-I\|\|X\|\). Every unitary \(u\) with \(u\rho(\cdot)u^*=\theta\) therefore satisfies \(\|\rho-\theta\|_{\rm cb}\le2\|u-I\|\), so \(\|\rho-\theta\|_{\rm cb}\le2m\). Lemma 3.3 produces such a \(u\) with \(\|u-I\|\le\|\rho-\theta\|_{\rm cb}\), so \(m\le\|\rho-\theta\|_{\rm cb}\).

**Solution 5.4.** Let \(X\in M_n(A)_1\). Then \(X\oplus0\in M_{n+1}(A)_1\). For \(Y'\in M_{n+1}(B)_1\), the upper left \(n\times n\) corner \(Y\) of \(Y'\) lies in \(M_n(B)_1\) and \(\|X-Y\|\le\|X\oplus0-Y'\|\). Hence \(\operatorname{dist}(X,M_n(B)_1)\)\(\le\delta(M_{n+1}(A),M_{n+1}(B))\), and symmetrically.

**Solution 5.5.** Write \(\mathbb N\) as a disjoint union of infinite sets \(N_1,N_2,\dots\) and let \(s_i\) map the standard basis bijectively onto the basis vectors indexed by \(N_i\). If every isometry is unitary and \((s_i)\) were an infinite family, \(s_1s_1^*=I\) would force \(s_2s_2^*=0\), contradicting \(s_2^*s_2=I\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [OpenAI-289b] OpenAI, Close separable C\*-algebras without spatial conjugacy, preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026
- [OpenAI-289c] OpenAI, Near inclusions of von Neumann algebras without small spatial embeddings, preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026
- [CCSSWW] J. Cameron, E. Christensen, A. M. Sinclair, R. R. Smith, S. White, A. D. Wiggins, Kadison–Kastler stable factors, Duke Mathematical Journal 163 (2014), 2639–2686. https://arxiv.org/abs/1209.4116
- [CSSWW] E. Christensen, A. M. Sinclair, R. R. Smith, S. A. White, W. Winter, Perturbations of nuclear C\*-algebras, Acta Mathematica 208 (2012), 93–150. https://arxiv.org/abs/0910.4953

# Lifting completely positive maps

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

A quotient algebra identifies elements that differ by an ideal. Lifting a map out of a quotient means choosing representatives coherently. Choosing each representative separately will not preserve linearity, much less matrix positivity. Finite-dimensional completely positive models provide a way to make the choices coherent.

We prove that a completely positive map with finite-dimensional completely positive approximations lifts whenever its domain is separable. We also prove that the class of all liftable completely positive maps is closed under pointwise norm limits on such a domain. The quotient algebra and its ideal need not be separable. Finite-domain compression and spectral clipping supply bounded lifts before the sequence argument is applied.

Prerequisites are [Completely positive finite models](completely-positive-finite-models.md), continuous functional calculus and the quotient norm formula for C*-algebras, Hahn–Banach and Banach–Alaoglu, and the [GNS construction](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#oa-fnd-gn-05). Lemma 2.1 constructs the approximate identity and proves the ideal-support argument in representations. Section 4 proves the nonunital cutoffs directly at every matrix size. Section 6 uses the [full unital Stinespring proof](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/completely-positive-maps.html#oa-fnd-cm-05); the finite-matrix criterion and the full extension proof are linked where used below.

Unital algebras in the unital assertions are nonzero. Inner products are linear in the second variable.

Throughout, \(q:B\to B/J\) is the quotient map. A **lift** of \(\theta:A\to B/J\) is a map \(\Theta:A\to B\) with \(q\Theta=\theta\).

## 1. Lift a whole positive matrix

**Lemma 1.1.** Every positive element of \(M_n(B/J)\) has a positive lift in \(M_n(B)\).

**Proof.** Let \(c\ge0\). Lift \(c^{1/2}\) to some \(v\in M_n(B)\); entrywise surjectivity of \(q\) gives such a lift. Then \(v^*v\ge0\) and \(q^{(n)}(v^*v)=c\). \(\square\)

**Proposition 1.2.** Every completely positive map \(\beta:M_n\to B/J\) has a completely positive lift. If \(\beta\) is contractive, its lift can be chosen contractive.

**Proof.** The matrix \(C=[\beta(E_{ij})]\) is positive by the [matrix criterion, Exercise 3 of Completely positive finite models](completely-positive-finite-models.md#exercise-3). Lift it to a positive matrix \(D=[d_{ij}]\in M_n(B)\). The formula
\(\beta_0(x)=\sum_{i,j}x_{ij}d_{ij}\)
defines a completely positive lift.

Suppose now that \(\beta\) is contractive. Set \(h=\beta_0(1)=\sum_i d_{ii}\in B_+\). In the unitization of \(B\), use continuous functional calculus to define
\[
r=f(h),\qquad f(t)=
\begin{cases}
1,&0\le t\le1,\\
t^{-1/2},&t\ge1.
\end{cases}
\]
Since \(f(0)=1\), \(r\) lies in \(1+B\). The map
\(\beta_1(x)=r\beta_0(x)r\)
still has range in \(B\) and is completely positive. Its norm is
\[
\|\beta_1\|=\|rhr\|=\|\min(h,1)\|\le1.
\]
The quotient map extends to unitizations. There \(q(h)=\beta(1)\le1\), so \(q(r)=f(q(h))=1\). Thus \(q\beta_1=\beta\). \(\square\)

The same conclusion holds for a finite direct sum of matrix algebras. Lift the summand maps by their positive matrices first, sum them, and apply the same normalization to the total value at the unit.

If \(B\) and \(B/J\) are unital and \(\beta\) is unital, choose a cpc lift \(\beta_1\). For a state \(\tau\) on the finite-dimensional domain, the formula
\[
\beta_2(x)=\beta_1(x)+\tau(x)(1-\beta_1(1))
\]
gives a ucp lift: its value at \(1\) is \(1\), and the added term has zero image under \(q\).

**Example 1.3.** Take \(B=C([0,1],M_2)\), and let \(q\) evaluate a function at the endpoints. Its quotient is \(M_2\oplus M_2\). If \(\beta_0,\beta_1:M_n\to M_2\) are cpc, then
\[
\Theta(x)(t)=(1-t)\beta_0(x)+t\beta_1(x)
\]
is a cpc lift of \(x\mapsto(\beta_0(x),\beta_1(x))\). Positivity is checked at each \(t\), at every matrix level.

## 2. An ideal can be cut off almost centrally

A positive contractive approximate identity \((u_i)\) of \(J\) is **quasicentral in \(B\)** if \(\|u_ib-bu_i\|\to0\) for every \(b\in B\).

Convexity is useful here because a finite convex combination of positive contractions remains a positive contraction. A **convex approximate identity** is an approximate identity organized in a subset of \(J\) that is convex. For the construction below, we use convex combinations from a common late tail: if every element in that tail approximates multiplication on a finite list from \(J\) within a chosen tolerance, each such combination retains those estimates. No assertion that an arbitrary approximate identity is increasing in operator order is needed.

**Lemma 2.1.** Every closed ideal \(J\subset B\) has a quasicentral positive contractive approximate identity. No separability is needed.

**Proof.** We first construct a positive contractive approximate identity explicitly. For a finite set \(X\subset J\) and \(t>0\), put
\[
h_X=\sum_{x\in X}(x^*x+xx^*),\qquad
e_{X,t}=h_X(h_X+t1)^{-1}.
\]
The inverse is computed in the unitization of \(B\). The function \(s/(s+t)\) vanishes at zero, so \(e_{X,t}\in J\), and \(0\le e_{X,t}\le1\). For every \(x\in X\), both \(x^*x\) and \(xx^*\) are at most \(h_X\). Consequently
\[
\begin{aligned}
\|(1-e_{X,t})x\|^2
&\le\|t^2h_X(h_X+t1)^{-2}\|\le t/4,\\
\|x(1-e_{X,t})\|^2
&\le\|t^2h_X(h_X+t1)^{-2}\|\le t/4.
\end{aligned}
\]
The scalar bound is \(t^2s/(s+t)^2\le t/4\) for \(s\ge0\). Direct these pairs by enlarging \(X\) and decreasing \(t\). Every later pair still has the estimates for a previously selected \(x\). This gives an approximate identity \((e_i)\), without a countability assumption. The empty set causes no problem: its cutoff is zero.

The weak convergence argument below applies to any positive contractive approximate identity of \(J\).

We next show that every bounded linear functional on \(B\) is a linear combination of positive functionals. We give the argument because weak convergence of commutators must be tested against the whole dual. Work first in a nonzero unital C*-algebra \(C\), and let \(E=C_{\mathrm{sa}}\) be its real Banach space. States norm \(E\): for \(a=a^*\), choose a spectral value \(\lambda\) with \(|\lambda|=\|a\|\). Evaluation at \(\lambda\) on \(C^*(1,a)\), followed by the positive-functional extension in [Completely positive finite models, Lemma 2.2](completely-positive-finite-models.md#lemma-2-2), gives a state \(s\) with \(|s(a)|=\|a\|\). A positive functional has norm equal to its value at \(1\), by its Cauchy–Schwarz inequality and \(a^*a\le\|a\|^2 1\).

In the real dual of \(E\), consider
\[
K=\{s-r:s,r\ge0,\ s(1)+r(1)\le1\}.
\]
Here positive real functionals on \(E\) are identified with their complexifications on \(C\). The pairs in this formula form a weak* closed subset of the product of two dual unit balls: positivity and the condition on the unit are weak* closed, and positivity gives the norm bounds. Banach–Alaoglu makes the set of pairs compact. Thus \(K\) is weak* compact and convex. For every \(a\in E\),
\[
\sup_{k\in K}k(a)=\|a\|.
\]
The upper bound follows from \(-\|a\|1\le a\le\|a\|1\); a norming state or its negative attains the lower bound. If a real bounded functional \(f\) on \(E\), of norm \(c>0\), lay outside \(cK\), weak* Hahn–Banach separation would give an \(a\in E\) with \(f(a)>c\|a\|\), contradicting its norm. Therefore every such \(f\) is a difference of two positive functionals; the zero case is immediate. Taking the real and imaginary parts of a complex functional on \(E\), and then complexifying, expresses it as a linear combination of four positive functionals. For a possibly nonunital \(B\), extend a bounded functional to \(B^\dagger\) by Hahn–Banach and restrict these four positive parts to \(B\). If \(B=0\), the assertion is immediate.

Fix a positive functional on \(B^\dagger\). Its GNS representation has the form
\(s(b)=\langle\xi,\pi(b)\xi\rangle\). Put
\[
L=\overline{\pi(J)H},\qquad p=P_L.
\]
Since \(J\) is a two-sided ideal, \(L\) is invariant under every \(\pi(b)\) and \(\pi(b)^*\); hence it reduces \(\pi(B^\dagger)\), and \(p\) commutes with that representation. On the dense set of vectors \(\pi(j)\eta\) in \(L\),
\[
\pi(e_i)\pi(j)\eta\longrightarrow\pi(j)\eta
\]
because \(e_i j\to j\) in norm. Each \(\pi(e_i)\) has range in \(L\), is self-adjoint, and consequently vanishes on \(L^\perp\). Their uniform bound one extends convergence from the dense set to all of \(H\). Thus \(\pi(e_i)\to p\) strongly. It follows that, for every \(b\in B\),
\[
s(e_i b-b e_i)
\longrightarrow\langle\xi,(p\pi(b)-\pi(b)p)\xi\rangle=0.
\]
The preceding four-positive-functional decomposition proves this convergence for every bounded functional on \(B\).

For a finite \(F=\{b_1,\ldots,b_r\}\subset B\), the tuples
\[
([e_i,b_1],\ldots,[e_i,b_r])\in B^r
\]
therefore converge weakly to zero. Indeed, every bounded functional on the finite product is the sum of bounded functionals on its coordinates. Zero belongs to the weak closure of every tail of these tuples. A convex set has the same weak and norm closures by Hahn–Banach, so zero belongs to the norm closure of the convex hull of each tail. Choose a convex combination \(u\) of a sufficiently late tail with all the required commutator norms as small as desired. It remains a positive contraction. If the tail already has small left and right multiplication errors on a prescribed finite subset of \(J\), its convex combinations retain those errors. Direct the finite subsets of \(B\) and \(J\) and their positive tolerances. The resulting choices form a quasicentral positive contractive approximate identity. \(\square\)

**Lemma 2.2.** For a quasicentral approximate identity \((u_i)\), both \(u_i^{1/2}\) and \((1-u_i)^{1/2}\) asymptotically commute with every \(b\in B\). Moreover
\[
u_i^{1/2}bu_i^{1/2}+(1-u_i)^{1/2}b(1-u_i)^{1/2}\longrightarrow b
\]
in norm.

**Proof.** For a polynomial \(p\), expand \([p(u_i),b]\) into sums involving \([u_i,b]\). Uniform polynomial approximation on \([0,1]\) then proves \([f(u_i),b]\to0\) for every continuous \(f\) on that interval. Apply this to \(f(t)=t^{1/2}\) and \(f(t)=(1-t)^{1/2}\).

Subtract \(u_ib+(1-u_i)b=b\) from the displayed expression. The norm of the difference is at most
\(\|[b,u_i^{1/2}]\|+\|[b,(1-u_i)^{1/2}]\|\), which tends to zero. The factors involving \(1-u_i\) are computed in the unitization and still give elements of \(B\). \(\square\)

**Lemma 2.3.** For any approximate identity \((u_i)\) of \(J\) and any \(b\in B\),
\[
\lim_i\|(1-u_i)^{1/2}b(1-u_i)^{1/2}\|=\|q(b)\|.
\]

**Proof.** Applying the extended quotient map gives \(q(b)\), so every norm on the left is at least \(\|q(b)\|\).

For an upper bound, choose \(j\in J\) with \(\|b+j\|<\|q(b)\|+\varepsilon\). The approximate identity gives
\(\|(1-u_i)^{1/2}j\|\to0\). For example, its squared norm is bounded by
\(\|j^*(1-u_i)j\|\), which tends to zero. Hence compression of \(j\) tends to zero, while compression of \(b+j\) has norm at most \(\|b+j\|\). The limit superior is at most \(\|q(b)\|+\varepsilon\). \(\square\)

**Corollary 2.4.** If \(B\) is separable, \(J\) has a quasicentral positive contractive approximate identity that is a sequence.

**Proof.** Choose norm-dense sequences \((b_j)\) in the unit ball of \(B\) and \((x_j)\) in the unit ball of \(J\), which is also separable. For each \(n\), Lemma 2.1 gives a positive contraction \(u_n\in J\) such that, for \(j\le n\),
\[
\|[u_n,b_j]\|<1/n,\qquad
\|u_nx_j-x_j\|<1/n,\qquad
\|x_ju_n-x_j\|<1/n.
\]
For arbitrary \(b\) near a \(b_j\), the commutator error is bounded by \(2\|b-b_j\|+\|[u_n,b_j]\|\). The analogous two multiplication errors for \(x\in J\) have the same bound with \(x_j\). Thus the sequence meets all three requirements on the whole algebras, first in their unit balls and then by rescaling. \(\square\)

**Proposition 2.5 (Convex order tails).** The set
\[
\mathcal U=\{u\in J_+:\|u\|<1\}
\]
is a convex approximate identity when directed by operator order. Its order tails are convex. Quasicentral choices can be made inside any prescribed order tail.

**Proof.** We will use the following elementary inverse-order calculation. If positive invertible elements satisfy \(0<a\le b\) in a unital C*-algebra, put \(c=a^{-1/2}ba^{-1/2}\ge1\). The continuous calculus gives \(0<c^{-1}\le1\). Since \(b=a^{1/2}ca^{1/2}\), multiplication gives \(b^{-1}=a^{-1/2}c^{-1}a^{-1/2}\le a^{-1}\).

For \(u,v\in\mathcal U\), compute in \(B^\dagger\)
\[
D=(1-u)^{-1}+(1-v)^{-1}-1,\qquad w=1-D^{-1}.
\]
We have \(D\ge1\). Its inverse is bounded below by \(\|D\|^{-1}1\), so \(0\le w\) and \(\|w\|<1\). Also \(D\ge(1-u)^{-1}\) implies \(D^{-1}\le1-u\), hence \(w\ge u\); likewise \(w\ge v\). Finally \(D-1\in J\) and \(D^{-1}-1\in J\), so \(w\in J\). This proves directedness.

Positive contractive approximate identities, scaled by constants approaching one from below, supply elements of \(\mathcal U\) with both multiplication errors on each finite subset of \(J\) as small as desired. For any larger \(v\ge u\),
\[
\begin{aligned}
\|(1-v)x\|^2
&\le\|x^*(1-u)x\|
\le\|x\|\|(1-u)x\|,\\
\|x(1-v)\|^2
&\le\|x(1-u)x^*\|
\le\|x\|\|x(1-u)\|.
\end{aligned}
\]
Here \((1-v)^2\le1-v\le1-u\) gives the first inequalities. Thus entire sufficiently late order tails have small errors, proving that \(\mathcal U\) is an approximate identity.

Convexity follows from positivity and the strict norm bound. The tail \(\mathcal U_u=\{v\in\mathcal U:v\ge u\}\) is convex as well and is cofinal in \(\mathcal U\). For finite \(F\subset B\), the commutator tuples indexed by this tail converge weakly to zero, by the weak commutator convergence proved in Lemma 2.1. Their set is convex, so Hahn–Banach puts zero in its norm closure. Hence, for each \(\varepsilon>0\), there is \(v\in\mathcal U_u\) with
\[
\max_{b\in F}\|[v,b]\|<\varepsilon.
\]
Direct the prescribed base elements, finite sets and tolerances. The chosen elements eventually dominate every fixed element of \(\mathcal U\) and asymptotically commute with every \(b\in B\); they give a quasicentral approximate identity. The chosen net need not itself increase in operator order. \(\square\)

This constructs a particular ordered convex approximate identity and uses its convex tails. It does not impose operator-order monotonicity on an arbitrary previously chosen net.

The same tail-separation proof works for any convex subset of positive contractions that already forms an approximate identity directed by operator order: its order tails are convex and cofinal. If the starting approximate identity is increasing, its convex hull has this directedness, since one sufficiently late original element dominates every element in any prescribed finite convex combination.

## 3. Make a new lift close to an old one

**Lemma 3.1.** Suppose \(A,B\) are unital and \(\Phi,\Psi:A\to B\) are ucp. Given finite \(F\subset A\) and \(\delta>0\), there is a ucp map \(\Psi':A\to B\) with \(q\Psi'=q\Psi\) and
\[
\|\Phi(a)-\Psi'(a)\|
<\|q\Phi(a)-q\Psi(a)\|+\delta
\quad(a\in F).
\]

**Proof.** Let \((u_i)\) be a quasicentral approximate identity of \(J\), and put
\[
\Psi_i(a)=u_i^{1/2}\Phi(a)u_i^{1/2}
+(1-u_i)^{1/2}\Psi(a)(1-u_i)^{1/2}.
\]
Both terms are completely positive. At \(1\), they sum to \(u_i+(1-u_i)=1\), so \(\Psi_i\) is ucp. Since \(q(u_i)=0\), \(q\Psi_i=q\Psi\).

Define \(\Phi_i\) by the same formula with \(\Phi\) in both terms. Lemma 2.2 gives \(\Phi_i(a)\to\Phi(a)\). Also
\[
\Phi_i(a)-\Psi_i(a)
=(1-u_i)^{1/2}(\Phi(a)-\Psi(a))(1-u_i)^{1/2}.
\]
Lemma 2.3 computes its limiting norm as
\(\|q\Phi(a)-q\Psi(a)\|\). Choose one index sufficiently large for all \(a\in F\). \(\square\)

This adjustment leaves the new quotient map exactly as it was. It changes the representative mainly inside the ideal, where the old lift can be retained.

**Theorem 3.2.** Let \(A,B\) be unital, with \(A\) separable. If a ucp map \(\theta:A\to B/J\) is a pointwise norm limit of liftable ucp maps, then \(\theta\) has a ucp lift.

**Proof.** Each liftable ucp map has a ucp lift. Indeed, for any completely positive lift \(\Psi\), clip its unit image \(h=\Psi(1)\) with \(d=g(h)\) as in Proposition 1.2. Since \(q(h)=1\), \(q(d)=1\), so \(d\Psi(\,\cdot\,)d\) is a cpc lift of the same map. Its positive unit defect \(1-dhd\) lies in \(J\). Adding a state of \(A\) times that defect gives a ucp lift.

Choose a norm-dense sequence \(a_1,a_2,\ldots\) in the unit ball of \(A\). Pass to a subsequence of the quotient maps \(\theta_k\) so that
\[
\|\theta_k(a_j)-\theta(a_j)\|<2^{-k-3}\quad(j\le k).
\]
Start with a ucp lift \(\Phi_1\) of \(\theta_1\). If \(\Phi_k\) is chosen, take any ucp lift of \(\theta_{k+1}\), then adjust it using Lemma 3.1 on \(a_1,\ldots,a_k\), with tolerance \(2^{-k-3}\). This gives a ucp lift \(\Phi_{k+1}\) for which
\[
\|\Phi_{k+1}(a_j)-\Phi_k(a_j)\|<2^{-k}\quad(j\le k).
\]
For each fixed \(j\), these successive differences are summable after stage \(j\). Thus \(\Phi_k(a_j)\) is Cauchy.

All maps have norm one. For arbitrary \(a\) in the unit ball and a nearby \(a_j\),
\[
\|\Phi_k(a)-\Phi_l(a)\|
\le2\|a-a_j\|+\|\Phi_k(a_j)-\Phi_l(a_j)\|.
\]
Hence \(\Phi_k(a)\) is Cauchy for every \(a\in A\). Define \(\Phi(a)\) to be its norm limit. Linearity and unitality pass to the limit. At every matrix size, entrywise norm convergence preserves positivity, so \(\Phi\) is completely positive. Finally \(q\Phi(a)=\lim_k\theta_k(a)=\theta(a)\). \(\square\)

The uniform norm bound is essential to this argument. Convergence on a dense list alone does not ensure convergence on all of a Banach space.

## 4. Control the norm before taking limits

We record the nonunital details so that the lifting theorem does not acquire an implicit unit hypothesis.

Let \(A^\dagger\) mean that we adjoin a new unit, even if \(A\) already has an identity of its own. There is a character \(\chi:A^\dagger\to\mathbb C\) that vanishes on \(A\) and takes the new unit to one.

**Lemma 4.1.** A cpc map \(\phi:A\to D\) extends to a ucp map
\[
\phi^\dagger:A^\dagger\to D^\dagger,\qquad
\phi^\dagger(a+\lambda1)=\phi(a)+\lambda1.
\]
If \(\phi\) factors through a matrix algebra by cpc maps, then \(\phi^\dagger\) factors through a finite-dimensional C*-algebra by ucp maps.

**Proof.** We first check the effect of cutting an adjoined unit by an element of the original algebra. If \(e\in A_+\) and \(\psi:A\to D\) is completely positive, then
\[
\psi_e^\dagger(a+\lambda1)=\psi(eae)+\lambda\psi(e^2)
\]
is completely positive on \(A^\dagger\). For a positive matrix \(X=[a_{ij}+\lambda_{ij}1]\), the matrix
\[
\operatorname{diag}(e,\ldots,e)X\operatorname{diag}(e,\ldots,e)
=[ea_{ij}e+\lambda_{ij}e^2]
\]
is positive in \(M_r(A)\). Applying \(\psi\) entrywise proves the claim at every size \(r\).

Now let \(e\) run through a positive contractive approximate identity of \(A\), and take \(\psi=\phi\). The scalar matrix \(\Lambda=[\lambda_{ij}]=\chi^{(r)}(X)\) is positive, and \(1-\phi(e^2)\ge0\) in \(D^\dagger\). Thus
\[
[\phi(ea_{ij}e+\lambda_{ij}e^2)]
+[\lambda_{ij}(1-\phi(e^2))]
=[\phi(ea_{ij}e)+\lambda_{ij}1]
\]
is positive. The second matrix is positive because it is the tensor product of the positive scalar matrix \(\Lambda\) with \(1-\phi(e^2)\). As \(eae\to a\) in norm and \(\phi\) is contractive, these matrices converge in norm to \([\phi(a_{ij})+\lambda_{ij}1]\). The positive cone is norm closed, proving complete positivity of \(\phi^\dagger\). Its value at the new unit is \(1\).

For a factorization \(\phi=\beta\alpha\), extend \(\alpha:A\to M_n\) to the ucp map
\(\alpha^\dagger(a+\lambda1)=\alpha(a)+\lambda1_n\).
Use the ucp map
\[
x\longmapsto(\alpha^\dagger(x),\chi(x))
\quad\text{into }M_n\oplus\mathbb C
\]
and reconstruct by
\[
(y,t)\longmapsto\beta(y)+t(1-\beta(1_n)).
\]
The second map is ucp because its two positive contributions sum to \(1\) at the unit. Their composite is \(\phi^\dagger\). \(\square\)

For a bounded completely positive \(\theta:A\to D\), say that \(\theta\) is **approximable** if it is locally approximable in pointwise norm by completely positive factorizations through matrices, without initially placing bounds on the two maps.

**Lemma 4.2.** If a cpc map \(\theta:A\to D\) is approximable, then it has approximations with both factor maps cpc.

**Proof.** Fix finite \(F\subset A\). Choose a positive contraction \(e\in A\) so that \(\theta(eae)\) is close to \(\theta(a)\) for \(a\in F\). This is possible because \(eae\to a\) along an approximate identity.

Choose completely positive \(S:A\to M_n\), \(T:M_n\to D\) approximating \(\theta\) on every \(eae\), \(a\in F\), and on \(e^2\), within a small \(\delta>0\). The map \(S_e(a)=S(eae)\) has the completely positive extension
\[
S_e^\dagger(a+\lambda1)=S(eae)+\lambda S(e^2)
\]
with value \(h=S(e^2)\) at the unit, by the positive-matrix cutoff in the proof of Lemma 4.1.

Let \(p\) be the support of \(h\) in \(M_n\). On \(p\mathbb C^n\), its inverse square root is bounded. The formula
\[
\alpha(x)=h^{-1/2}S_e^\dagger(x)h^{-1/2}+\chi(x)(1-p)
\]
defines a ucp map \(A^\dagger\to M_n\). The first term is computed on the support and is zero on its orthogonal complement. Its value at \(1\) is \(p\). The identity
\[
S_e^\dagger(x)=h^{1/2}\alpha(x)h^{1/2}
\]
follows because the range of the positive map \(S_e^\dagger\) is supported on \(p\): positive inputs are bounded in order by a multiple of \(h\), and they linearly span the domain.

Set \(\beta(y)=T(h^{1/2}yh^{1/2})\). Its norm is
\[
\|\beta\|=\|T(h)\|=\|TS(e^2)\|\le1+\delta.
\]
Thus \(\beta/(1+\delta)\) is cpc, and \(\alpha|_A\) is cpc. On \(a\in F\), their composite is \(TS(eae)/(1+\delta)\). The error from \(\theta(a)\) tends to zero as the cutoff error and \(\delta\) tend to zero. \(\square\)

For a nonzero completely positive map of norm \(M\), apply this lemma to \(\theta/M\). It shows why uncontrolled factor norms in an initial approximation do not obstruct the lifting argument.

**Theorem 4.3 (Closure of all liftable completely positive maps).** Let \(A\) be separable, with \(B\) and \(J\subseteq B\) arbitrary. Suppose \((\theta_n)\) is a sequence of liftable completely positive maps \(A\to B/J\) that converges in norm at every \(a\in A\). Its limit \(\theta\) has a completely positive lift of norm \(\|\theta\|\).

**Proof.** Pointwise limits preserve linearity. At every matrix size, entrywise norm convergence preserves the positive cone, so \(\theta\) is completely positive. It is also bounded. To prove this without a separate uniform boundedness assumption, suppose its values on positive contractions were unbounded. Choose positive contractions \(a_k\) with \(\|\theta(a_k)\|\ge4^k\). The norm-convergent sum \(a=\sum_k2^{-k}a_k\) satisfies \(a\ge2^{-k}a_k\), hence
\[
0\le2^{-k}\theta(a_k)\le\theta(a),\qquad
\|\theta(a)\|\ge2^k
\]
for every \(k\), a contradiction. Thus the positive contraction values have a finite bound. Every element of the unit ball is a linear combination of four positive contractions, by taking the positive and negative parts of its real and imaginary parts. This bounds \(\theta\) on the whole unit ball. If its norm is zero, use the zero lift. Otherwise rescale the maps so that \(\|\theta\|=1\).

We first construct cpc liftable maps arbitrarily close to \(\theta\) on each finite subset \(F\) of the unit ball. Fix \(0<\delta<1\). Choose a positive contraction \(e\in A\) with
\[
\|eae-a\|<\delta\quad(a\in F).
\]
Choose \(n\) sufficiently large that
\[
\|\theta_n(eae)-\theta(eae)\|<\delta\quad(a\in F),
\qquad
\|\theta_n(e^2)-\theta(e^2)\|<\delta.
\]
Take any completely positive lift \(\Psi_n:A\to B\); its norm need not be controlled. Put \(h=\Psi_n(e^2)\in B_+\), and use the clipping function
\[
g(t)=
\begin{cases}1,&0\le t\le1,\\t^{-1/2},&t>1.\end{cases}
\qquad d=g(h)\in B^\dagger.
\]
The map
\[
\Gamma(a)=d\Psi_n(eae)d
\]
takes values in \(B\) and is cpc. Indeed the positive-matrix cutoff in Lemma 4.1 gives a completely positive extension
\[
\Gamma^\dagger(a+\lambda1)=d\Psi_n(eae)d+\lambda dhd.
\]
Its value at the unit is \(dhd\le1\). A completely positive map on a unital C*-algebra has norm equal to the norm of its unit image. To see the needed bound directly, for \(\|x\|\le1\) the matrix \(\begin{pmatrix}1&x\\x^*&1\end{pmatrix}\) is positive; its image has diagonal entries at most \(1\), so its off-diagonal entry has norm at most \(1\) by the positive two-by-two block inequality. Thus \(\Gamma^\dagger\), and its restriction \(\Gamma\), are contractive.
Only the bounded element \(h\in B\) is clipped; no multiplier property of \(\Psi_n^{**}(1)\) is needed.

Write \(r=g(q(h))\) in the unitization of the quotient. Since
\[
0\le q(h)=\theta_n(e^2)\le(1+\delta)1,
\]
we have \(0\le r\le1\) and
\[
\|r-1\|\le1-(1+\delta)^{-1/2}\le\delta/2.
\]
The liftable cpc map \(\eta=q\Gamma\) is
\(\eta(a)=r\theta_n(eae)r\). On \(F\), \(\|\theta_n(eae)\|\le1+\delta\), and hence
\[
\begin{aligned}
\|\eta(a)-\theta(a)\|
&\le2\|r-1\|\|\theta_n(eae)\|
 +\|\theta_n(eae)-\theta(eae)\|
 +\|\theta(eae)-\theta(a)\|\\
&<(3+\delta)\delta.
\end{aligned}
\]
Thus bounded lifts can approximate the limiting map, even when the original chosen lifts have arbitrarily large norms.

Use a dense sequence in the unit ball of \(A\), enlarging its finite initial segments and letting \(\delta\) tend to zero. The resulting cpc maps \(\eta_k\), with cpc lifts \(\Gamma_k\), converge pointwise in norm to \(\theta\): their common bound one extends convergence from the dense sequence to all of \(A\).

By Lemma 4.1 their forced unitizations \(\eta_k^\dagger:A^\dagger\to(B/J)^\dagger\) have ucp lifts \(\Gamma_k^\dagger:A^\dagger\to B^\dagger\). The quotient \(B^\dagger/J\) is \((B/J)^\dagger\), and these maps converge pointwise to \(\theta^\dagger\). Theorem 3.2 supplies a ucp lift \(\Lambda:A^\dagger\to B^\dagger\) of \(\theta^\dagger\).

For \(a\in A\), the character of \(B^\dagger\) gives
\[
\chi_B(\Lambda(a))
=\chi_{B/J}(q^\dagger\Lambda(a))
=\chi_{B/J}(\theta^\dagger(a))=0.
\]
Therefore \(\Lambda(A)\subseteq B\). Its restriction is a cpc lift of \(\theta\). Its norm equals one, since the quotient is contractive and \(\|\theta\|=1\). Rescaling proves the stated norm equality. \(\square\)

The clipping step may change the intermediate quotient map slightly. Its quantified error tends to zero; the final quotient equality is exact.

## 5. The lifting theorem

**Theorem 5.1 (Choi–Effros lifting).** Let \(A\) be a separable C*-algebra, \(B\) any C*-algebra, and \(J\subset B\) any closed ideal. Every approximable completely positive map \(\theta:A\to B/J\) has a completely positive lift \(\Theta:A\to B\) with \(\|\Theta\|=\|\theta\|\). If \(A,B\) are unital and \(\theta\) is unital, the lift can be chosen unital.

**Proof.** The zero map has the zero lift. Otherwise divide by \(\|\theta\|\) to make \(\theta\) cpc. By Lemma 4.2, it has cpc matrix factorizations. Separability and contractivity let us choose a sequence converging pointwise in norm, by the dense-set argument of **Completely positive finite models**.

Apply Lemma 4.1 to obtain ucp finite-dimensional factorizations converging to \(\theta^\dagger:A^\dagger\to(B/J)^\dagger\). The quotient map extends to
\[
q^\dagger:B^\dagger\to(B/J)^\dagger
\]
with kernel \(J\). Each finite-dimensional reconstruction map has a ucp lift by Proposition 1.2 and its unital correction. Compose with the corresponding recording map. Thus every approximating quotient map is liftable ucp.

Theorem 3.2 gives a ucp lift \(\Theta^\dagger:A^\dagger\to B^\dagger\) of \(\theta^\dagger\). For \(a\in A\), the scalar coordinate of \(q^\dagger\Theta^\dagger(a)=\theta(a)\) is zero. The scalar coordinates of \(B^\dagger\) and \((B/J)^\dagger\) agree under \(q^\dagger\), so \(\Theta^\dagger(a)\in B\). Its restriction is a cpc lift of \(\theta\).

Restore the original scale. The resulting lift has norm at most \(\|\theta\|\). Since \(q\) is contractive and \(q\Theta=\theta\), the reverse inequality holds.

For the last assertion, stay in the original unital algebras. The unit-repair exercise in **Completely positive finite models** makes the approximations ucp in both directions. Lift their finite-dimensional reconstruction maps ucp by Proposition 1.2, and apply Theorem 3.2 directly. \(\square\)

Consequently, every completely positive map from a separable C*-algebra with the completely positive approximation property to a quotient algebra lifts. The equivalence proved in [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md) gives the same conclusion for every separable nuclear C*-algebra.

The separability hypothesis belongs to the passage from approximations to an actual lift. Proposition 1.2 and the quasicentral approximate identity argument themselves have no separability hypothesis.

## 6. Complete order embeddings retain a quotient

There is another way that matrix order recognizes a quotient, without any approximate sequence.

<a id="unital-dilation"></a>
### The unital dilation

Let \(D\) be unital and \(\psi:D\to B(K)\) ucp. On the algebraic tensor space \(D\odot K\), put, with the inner product linear in the second variable,
\[
\Big\langle\sum_i a_i\otimes\xi_i,\sum_j b_j\otimes\eta_j\Big\rangle
=\sum_{i,j}\langle\xi_i,\psi(a_i^*b_j)\eta_j\rangle.
\]
The form descends through the bilinearity relations. Its positivity is complete positivity applied to the Gram matrix \([a_i^*a_j]\). Positive-form Cauchy–Schwarz makes its zero vectors a subspace orthogonal to all vectors. Divide by that subspace and complete by taking equivalence classes of Cauchy sequences. For \(d\in D\), left multiplication by \(d\) is bounded by \(\|d\|\): the difference of the two Gram matrices is
\[
[a_i^*(\|d\|^2 1-d^*d)a_j]\ge0,
\]
since it is the Gram matrix of \((\|d\|^2 1-d^*d)^{1/2}a_j\). Hence left multiplication descends and extends to a bounded representation \(\pi:D\to B(L)\). Its adjoint identity follows directly from the form, and its product and unit identities hold on the dense algebraic vectors and then everywhere.

Define \(V\xi=[1\otimes\xi]\). Then \(\langle V\xi,V\eta\rangle=\langle\xi,\eta\rangle\), so \(V\) is an isometry; direct substitution gives \(V^*\pi(d)V=\psi(d)\). This is Stinespring’s dilation for the unital map. With \(P=VV^*\), the displayed Schwarz defects in the following argument are exactly \(V^*\pi(d)^*(1-P)\pi(d)V\). Vanishing for both \(d^*d\) and \(dd^*\) is equivalent to \(P\pi(d)=\pi(d)P\). The latter elements form a closed *-subalgebra and give both multiplicative identities by inserting \(P+(1-P)\).

### Schwarz equality and products

For a ucp map \(\psi:C\to B(K)\), write \(\psi(x)=V^*\pi(x)V\) with \(V\) an isometry, and put \(P=VV^*\). Then
\[
\psi(a^*a)-\psi(a)^*\psi(a)
=V^*\pi(a)^*(1-P)\pi(a)V\ge0.
\]
Equality holds exactly when \((1-P)\pi(a)V=0\). Equality also for \(aa^*\) gives \((1-P)\pi(a^*)V=0\). Together these say that \(VK\) reduces \(\pi(a)\), or equivalently that \(P\) commutes with \(\pi(a)\). For every \(x\in C\), inserting \(P+(1-P)\) between the two representation factors now gives
\[
\psi(ax)=\psi(a)\psi(x),\qquad
\psi(xa)=\psi(x)\psi(a).
\]
The elements whose images commute with \(P\) form a norm-closed *-subalgebra of \(C\). This proves both the Schwarz inequality and the multiplicative-domain assertion used below, including closure under products and norm limits.

**Theorem 6.1.** Let \(A\) be unital. Suppose \(\theta:A\to B(H)\) is a unital completely positive injection whose inverse on \(\theta(A)\) is completely positive. Then there is a surjective *-homomorphism
\[
\rho:C^*(\theta(A))\to A,\qquad \rho(\theta(a))=a.
\]

**Proof.** The map \(\theta\) is contractive. Its inverse is unital and completely positive on the inherited operator system \(\theta(A)\); applying it to the positive two-by-two block matrix with off-diagonal entry \(\theta(a)\) gives \(\|a\|\le\|\theta(a)\|\). Thus \(\theta\) is isometric and \(\theta(A)\) is norm closed.

Represent \(A\) faithfully on \(K\). The inverse map on the operator system \(\theta(A)\), followed by this representation, extends by [Arveson's theorem, Theorem 2.3 of Completely positive finite models](completely-positive-finite-models.md#theorem-2-3), to a ucp map
\(\rho_0:C^*(\theta(A))\to B(K)\).

The Schwarz inequality applied first to \(\theta\) and then to \(\rho_0\) gives
\[
a^*a=\rho_0\theta(a^*a)
\ge\rho_0(\theta(a)^*\theta(a))
\ge\rho_0(\theta(a))^*\rho_0(\theta(a))=a^*a.
\]
Equality holds throughout. The same argument with \(aa^*\) shows that every \(\theta(a)\) belongs to the multiplicative domain of \(\rho_0\). That domain is a C*-subalgebra, so contains \(C^*(\theta(A))\). Thus \(\rho_0\) is a *-homomorphism on the entire generated algebra. Its range is the C*-algebra generated by the elements \(a\), namely \(A\). \(\square\)

## 7. Exercises with solutions

**Exercise 1 (Normalize a positive lift; introductory).** Let \(q:B\to C\) be a quotient of unital C*-algebras and let \(h\in B_+\) satisfy \(q(h)\le1\). Show that \(rhr\le1\) and \(q(r)=1\) for the function \(r=f(h)\) in Proposition 1.2.

*Solution.* Functional calculus gives \(rhr=\min(h,1)\). Because the spectrum of \(q(h)\) is contained in \([0,1]\), \(f(q(h))=1\). Functoriality of functional calculus under \(q\) gives \(q(r)=1\).

**Exercise 2 (Keep the quotient exact; introductory).** In Lemma 3.1, compute \(q(\Psi_i(a))\) and \(\Psi_i(1)\).

*Solution.* Since \(q(u_i)=0\), the first term has zero quotient and \(q((1-u_i)^{1/2})=1\). Thus \(q\Psi_i(a)=q\Psi(a)\). If both input maps are unital, the value at \(1\) is \(u_i+(1-u_i)=1\).

**Exercise 3 (Dense-set convergence needs a bound; intermediate).** On \(\ell^2(\mathbb N)\), let \(T_n(x)=n x_n\) be a functional with values in \(\mathbb C\). Show that \(T_n(x)\to0\) for every finitely supported \(x\), but not for every \(x\in\ell^2\).

*Solution.* For a finitely supported \(x\), its \(n\)-th coordinate is eventually zero. Let \(x_{2^k}=2^{-k}\) and set all other coordinates to zero. Then \(\sum_k|x_{2^k}|^2=\sum_k4^{-k}<\infty\), but \(T_{2^k}(x)=1\). Also \(\|T_n\|=n\). This is precisely the failure prevented by the uniform norm-one lifts in Theorem 3.2.

**Exercise 4 (A nonunital lift; intermediate).** Let \(A=C_0((0,1])\), let \(B=C([0,1])\), and let \(q:B\to\mathbb C\) evaluate at \(1\). Construct a cpc lift of \(\theta(f)=f(1)\).

*Solution.* Define \(\Theta(f)(t)=t f(1)\). This lies in \(B\), is linear, and evaluates to \(f(1)\) at \(1\). At each \(t\), it is a nonnegative scalar multiple of evaluation, so is completely positive. Its norm is one. This lift differs from the *-homomorphic lift obtained by extending \(f\) by zero at \(0\); both are valid.

**Exercise 5 (A quotient model from samples; intermediate).** Suppose \(\theta:C(X)\to B/J\) is ucp, with \(X\) compact Hausdorff. Explain how partitions of unity give liftable ucp maps converging to \(\theta\). State the additional hypothesis that permits Theorem 3.2 to give one exact lift.

*Solution.* Compose the ucp sample-and-interpolation approximations of \(\operatorname{id}_{C(X)}\) with \(\theta\). Their reconstruction maps from \(\mathbb C^r\) lift ucp by Proposition 1.2, so the composites lift. For Theorem 3.2, the domain \(C(X)\) must be separable; this holds, for example, when \(X\) is compact metrizable. The partition construction alone works for every compact Hausdorff \(X\).

Here is the partition construction for the sampled functions. If the finite test list is empty and X is nonempty, choose one sample point and use the constant weight one. Otherwise assume the test list is nonempty and let \(F=\{f_1,\ldots,f_m\}\subset C(X)\), with \(X\) compact Hausdorff and nonempty, and \(\varepsilon>0\). The image of \(x\mapsto(f_1(x),\ldots,f_m(x))\) is compact. Choose finitely many \(x_j\in X\) so that every \(x\) has \(\max_i|f_i(x)-f_i(x_j)|<\varepsilon/2\) for some \(j\). Define
\[
w_j(x)=\max\{0,\varepsilon-\max_i|f_i(x)-f_i(x_j)|\},\qquad
g_j(x)=w_j(x)/\sum_l w_l(x).
\]
The denominator is everywhere positive, the \(g_j\) are continuous and nonnegative, and their sum is one. If \(g_j(x)>0\), every selected function differs from its value at \(x_j\) by less than \(\varepsilon\). Sampling \(\alpha(f)=(f(x_j))_j\) is a unital *-homomorphism. Reconstruction \(\beta(z)=\sum_j z_jg_j\) is ucp: at every matrix level and point, it is a nonnegative combination of positive scalar matrices, with weights summing to one. Thus \(\|\beta\alpha(f_i)-f_i\|<\varepsilon\) for all selected functions. The zero algebra for empty \(X\) has zero approximations. Compose reconstruction with the given \(\theta\), lift from \(\mathbb C^r\) by Proposition 1.2, and obtain the exact net required by Exercise 5.

For the additional stated example, compact metrizable \(X\) has separable \(C(X)\). Choose a finite \(1/n\)-net for every \(n\); the union is countable and dense. For each finite set of these centers and positive rational \(r\) that gives a cover by the balls of radius \(r\), form the normalized weights \(\max\{0,r-d(x,x_j)\}\). There are countably many such systems. All their rational complex linear combinations form a countable set of continuous functions. They are dense: a continuous function on compact metric \(X\) is uniformly continuous (otherwise sequences \(x_n,y_n\) with distance tending to zero and a fixed value separation have a convergent subnet in the compact product \(X\times X\); the two limit points coincide, contradicting continuity). Choose a sufficiently small rational radius and finitely many centers making a finer cover; replacing the sampled function values by rational complex numbers gives arbitrarily small uniform error. This proves precisely the separability assertion consumed by Exercise 5, rather than a general Stone–Weierstrass import.

**Exercise 6 (A norm formula from an ideal; advanced).** Prove the two-sided version of Lemma 2.3 with \(1-u_i\) in place of its square root.

*Solution.* The quotient of \((1-u_i)b(1-u_i)\) is again \(q(b)\), giving the lower bound. For \(j\in J\), \((1-u_i)j\to0\), so its two-sided compression tends to zero. Choose \(j\) with \(\|b+j\|\) arbitrarily close to \(\|q(b)\|\) for the upper bound. No quasicentrality is needed.

**Exercise 7 (Why complete order matters; advanced).** In Theorem 6.1, indicate exactly where positivity at matrix size two is used.

*Solution.* Both applications of the Schwarz inequality require 2-positivity. Complete positivity of the inverse is also what permits its extension by Arveson's theorem. An order-preserving inverse at scalar size alone does not provide those properties. In particular, transposition on \(M_2\) is a positive unital bijection with positive inverse, but is not completely positive.

**Exercise 8 (Bound an arbitrary lift after compression; advanced).** Let \(\Psi:A\to B\) be completely positive and \(e\in A\) a positive contraction. Put \(h=\Psi(e^2)\) and \(d=g(h)\), with the clipping function in Theorem 4.3. Show that \(a\mapsto d\Psi(eae)d\) is cpc, regardless of \(\|\Psi\|\).

*Solution.* Extend the compressed map to the new unit by
\[
\Gamma^\dagger(a+\lambda1)=d\Psi(eae)d+\lambda d\Psi(e^2)d.
\]
The positive-matrix cutoff in Lemma 4.1, followed by conjugation with \(d\), proves complete positivity at every matrix size. Its unit image is \(dhd\), and spectral calculus gives \(0\le dhd\le1\). Applying \(\Gamma^\dagger\) to the positive block matrix \(\begin{pmatrix}1&a\\a^*&1\end{pmatrix}\) for \(\|a\|\le1\) bounds the off-diagonal image by one. Thus \(\Gamma^\dagger\) is contractive and its restriction \(a\mapsto d\Psi(eae)d\) is cpc, regardless of the original norm of \(\Psi\). Since \(d\in B^\dagger\) and \(\Psi(eae)\in B\), its values remain in the ideal \(B\) of its unitization.

**Exercise 9 (The small change to the quotient; advanced).** If \(0\le k\le(1+\delta)1\), put \(r=g(k)\). For \(\|x\|\le1+\delta\), prove \(\|rxr-x\|\le\delta(1+\delta)\). Explain the role of this bound in Theorem 4.3.

*Solution.* Spectral calculus gives \(0\le r\le1\) and \(\|r-1\|\le1-(1+\delta)^{-1/2}\le\delta/2\). Write \(rxr-x=(r-1)xr+x(r-1)\). Its norm is at most \(2\|r-1\|\|x\|\le\delta(1+\delta)\). The clipping of a large lift may slightly alter the quotient map, but this bound makes that alteration tend to zero while the new lift has a fixed norm bound.

## References

James Gabe, [Lifting theorems for completely positive maps](https://arxiv.org/pdf/1508.00389v4), accepted arXiv:1508.00389v4 (30 January 2022). Example 2.2, p.3, defines nuclear maps using initially unbounded factor maps; Lemma 2.6, pp.5–6, proves the bounded-cutoff step for pointwise limits of liftable maps and then refers to Arveson's selection argument. Sections 2–4 above supply that selection and all norm and unitization details. Theorems 5.6–5.7, pp.21–22, concern ideal-preserving lifts with additional hypotheses; those hypotheses and their stronger conclusions are distinct from the ordinary lifting theorem proved here.

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorem 1.1.1, pp.145–146, and Theorem 1.2.3, pp.149–152, provide the dilation and extension methods used for the explicit matrix-order, support-normalization and multiplicative-domain arguments here.

Kristian Knudsen Olesen, [The Connes Embedding Problem: Sofic groups and the QWEP Conjecture](https://web.math.ku.dk/~musat/thesis_final_KKO_March12.pdf), University of Copenhagen master's thesis, November 2012. Section 2.4, Lemma 2.4.7 and Theorem 2.4.8, pp.53–54, give the quasicentral gluing and summable selection; Proposition 2.4.10 and Theorem 2.4.12, pp.55–56, present finite-dimensional lifting and the lifting theorem. These arguments credit Arveson's selection method and the Choi–Effros lifting theorem. The quasicentral existence and quotient-norm inputs referred to on p.11 are proved directly in Lemmas 2.1–2.3 above. For finite sums of matrix algebras, our direct positive-matrix lifts avoid extending into an arbitrary quotient range; the extension theorem invoked in the thesis targets B(H). Our positive-matrix normalization, norm bounds and nonunital cutoffs are also explicit. The stronger conclusion that the lift itself is nuclear, discussed but not proved in the thesis, and its later lifting statements are outside the assertions proved here.

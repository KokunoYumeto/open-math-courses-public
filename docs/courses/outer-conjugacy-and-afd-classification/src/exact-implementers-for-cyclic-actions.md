# Exact implementers for cyclic actions

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026, with writing-AI self-checking. New original text is public domain (CC0). Source and proof revision by GPT-6 Astra (OpenAI), Ultra, October 2026; not reviewed by a person.*

## Introduction

Suppose an approximately inner automorphism is a genuine action of a finite cyclic group. Its approximate implementing unitaries need not be fixed by the action or have finite order. Both defects can be removed. Centralizer cohomology first makes the unitaries almost fixed. Averaging and polar completion make them exactly fixed. A spectral normalization then gives the exact finite order.

The last normalization requires a uniformly controlled spectral cut. Applying a bounded discontinuous root to a central sequence does not automatically produce a central sequence. We prove the needed estimate before taking that root.

The finite-order implementer and conjugacy targets are [Takesaki III], Lemmas XVII.3.17–3.18. The implementing-defect method and the uniformly controlled spectral-root method also occur in [Connes], Lemmas 3.1.1, 3.1.3–3.1.4 and 3.2.3. Here we separate the fixed-factor unitary completion, the matching-coordinate selection and the uniform-cut estimate. Example 4.3 explains why the varying-logarithm inference in the book's proof needs repair; the normalization uses the adjoint root.

The exact prerequisites are:

- [Central towers and unitary cocycles](central-towers-and-unitary-cocycles.md), Section 2 and Lemma 2.1, for the induced period and proper outerness on every nonzero invariant corner of \(M_\omega\).
- Central sequence algebras and exact lifts, Theorem 3.1 and Theorem 5.1 with both prescribed endpoints equal to \(1\), for the finite normal-trace quotient and exact unitary lifts. No factor or separable-predual assertion about that quotient is used.
- [Almost-invariant inner implementers](almost-invariant-inner-implementers.md), Section 1 and Lemma 1.1, for the automorphism group topology and the moving-multiplier estimate.
- [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md), Theorem 3.1 and Section 3A, for faithful-state tests, normal-inclusion transport and joint ordinary extraction. Its [proof companion](../foundations/bounded-topology-foundations.md) supplies the preceding bounded-topology proofs.
- [Cyclic finite models for outer conjugacy](cyclic-finite-models-for-outer-conjugacy.md), Lemma 2.1, for the good-cut measure argument, and [Comparing asymptotically aperiodic automorphisms](comparing-asymptotically-aperiodic-automorphisms.md), Lemma 2.1, for norm-total dominated positive tests.
- [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md), Proposition 6.3, for absorption with the original action on the right-hand side.

The general finite free-action theorem used both on \(M_\omega\) and on \(M\) is specified next. Its retained standard-form, trace and spectral foundations remain part of the prerequisite chain; [Ando–Haagerup] gives modern quotient context.

## 1. Hypotheses and the finite-action interface

Let \(M\) be a strongly stable factor with separable predual, and let
\[
\begin{gathered}
\theta\in\overline{\operatorname{Inn}}M,\qquad\\
\theta^p=\mathrm{id},\qquad p_a(\theta)=p\geq1.
\end{gathered}\tag{1.1}
\]
For \(p>1\), no power \(\theta^j\), \(0<j<p\), is inner: an inner power would act trivially on the centralizer, contradicting its period \(p\). Hence \(\theta\) is a free cyclic action, meaning that every nonidentity group element acts properly outerly. Its induced action \(\gamma\) on the finite asymptotic centralizer \(F=M_\omega\) is free: apply [Central towers and unitary cocycles, Lemma 2.1](central-towers-and-unitary-cocycles.md) to each power \(\theta^j\), \(0<j<p\), which is not centrally trivial by \(p_a(\theta)=p\).

Here is the precise finite-action prerequisite. If a finite group \(G\) acts freely on a von Neumann algebra \(Q\), then
\[
Z(Q^G)=Z(Q)^G.
\tag{1.2}
\]
Also every unitary cocycle \(c_{st}=c_s\alpha_s(c_t)\) satisfies
\[
c_s=X^*\alpha_s(X)\quad(s\in G)
\tag{1.3}
\]
for a unitary \(X\in Q\). The finite-algebra case is the fixed-corner trace argument already used in the absorption lesson. The general theorem also compares the properly infinite fixed corners; full central support alone is insufficient without the appropriate projection comparison. The complete proof of (1.2)–(1.3), for arbitrary von Neumann algebras and arbitrary cardinal size, is [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md): Section 5, (C1)–(C4), proves the fixed-center identity; Sections 4 and 10, (M1)–(M3) and (D1)–(D4), give the cocycle in the exact orientation (1.3). Sections 2, 8 and 9 supply the projection and properly infinite comparison steps. Its trace, standard-form and bounded-topology foundations are stated there. [Takesaki II] records the historical finite-action result. In particular (1.2) makes \(M^\theta\) a factor. Its predual is separable, and a faithful state of \(M\) restricts to a faithful state there.

When \(p=1\), (1.1) says \(\theta=\mathrm{id}\); the implementing sequence \(1\) suffices. We retain this endpoint in the theorems.

## 2. Repairing an almost unitary element in a factor

Averaging a unitary over an action gives an element of the fixed algebra, but not generally a unitary. We need an exact repair inside that algebra.

**Lemma 2.1.** Let \(Q\) be a countably decomposable factor. Suppose a bounded sequence \(y_k\in Q\) satisfies
\[
\begin{gathered}
y_k^*y_k-1\longrightarrow0,\qquad\\
y_ky_k^*-1\longrightarrow0\\
\quad\text{strongly-star}.
\end{gathered}\tag{2.1}
\]
There are unitaries \(w_k\in Q\) with \(w_k-y_k\to0\) strongly-star.

*Proof.* Fix a faithful normal state \(\rho\), and let \(y_k=v_k|y_k|\) be the polar decomposition, with
\[
e_k=v_k^*v_k,\qquad f_k=v_kv_k^*.
\]
The support defects tend strongly-star to zero. Indeed,
\[
\begin{gathered}
1-e_k\leq(1-y_k^*y_k)^2,\qquad\\
1-f_k\leq(1-y_ky_k^*)^2.
\end{gathered}
\]
Continuous functional calculus on bounded positive operators gives \(|y_k|\to1\) and \(|y_k^*|\to1\) strongly. The exact identities
\[
\begin{gathered}
(y_k-v_k)^*(y_k-v_k)=(|y_k|-e_k)^2,\quad\\
(y_k-v_k)(y_k-v_k)^*=(|y_k^*|-f_k)^2
\end{gathered}
\]
then imply \(y_k-v_k\to0\) strongly-star.

If \(Q\) is finite, equivalence \(e_k\sim f_k\) makes their complements equivalent, by the faithful trace of the factor. Indeed, central comparison orders the complements up to equivalence, and the residual projection has trace zero, hence is zero. Complete \(v_k\) by a partial isometry from \(1-e_k\) to \(1-f_k\). The completing isometry is strongly-star null, since both supports are, and the resulting \(w_k\) is unitary.

Suppose \(Q\) is properly infinite. If \(e_k\) is finite, so is \(f_k\); their complements are full properly infinite projections in the countably decomposable factor. They are equivalent, and the same completion works.

If \(e_k\) is infinite, choose a properly infinite projection \(t_k\leq e_k\) with
\[
\rho(t_k)+\rho(v_kt_kv_k^*)<1/k.
\tag{2.2}
\]
Such a choice exists: split the infinite factor corner \(e_kQe_k\) into infinitely many orthogonal properly infinite projections and apply the finite positive functional
\(\rho+\rho\circ\operatorname{Ad}v_k\) to them. Some arbitrarily late projection has arbitrarily small mass on both sides. Here \(\operatorname{Ad}v_k\) denotes the corner map \(z\mapsto v_kzv_k^*\).

The projections
\[
1-e_k+t_k,\qquad 1-f_k+v_kt_kv_k^*
\]
are properly infinite with central support one. Countable decomposability makes them equivalent. Choose a partial isometry \(s_k\) between them and set
\[
w_k=v_k(e_k-t_k)+s_k.
\tag{2.3}
\]
Orthogonality of the initial and final supports makes \(w_k\) unitary. Both supports of \(s_k\) have \(\rho\)-mass tending to zero, by (2.1)–(2.2); the same is true of \(v_kt_k\). Thus \(w_k-v_k\to0\) in the sharp faithful-state seminorm, hence strongly-star on this bounded sequence. This proves the lemma in every case. \(\square\)

The projection facts used here are proved in [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md): Section 2, (NP2)–(NP6), and Section 9, (K1). In a factor, an infinite corner is properly infinite. Removing a finite projection from a properly infinite unit leaves an infinite projection, since a sum of two finite projections is finite by (NP6). Formula (NP5) supplies the splitting used in (2.2), and (K1) compares the full properly infinite complements. The countable-decomposability hypothesis is used in that last comparison. We do not assert that arbitrary infinite projections of full central support are equivalent.

## 3. Fixed unitaries that still implement the action

**Theorem 3.1.** Under (1.1), there are unitaries \(w_k\in M^\theta\) such that
\[
\operatorname{Ad}w_k\longrightarrow\theta
\quad\text{in the }u\text{-topology}.
\tag{3.1}
\]

*Proof.* Assume \(p>1\), and choose \(\operatorname{Ad}a_k\to\theta\). For \(g\in\mathbb Z/p\mathbb Z\), define
\[
c_{g,k}=a_k^*\theta^g(a_k).
\tag{3.2}
\]
These are central sequences. To see this, compute
\[
\begin{aligned}
&\operatorname{Ad}c_{g,k}\\
&=\operatorname{Ad}a_k^*\circ\theta^g\circ\operatorname{Ad}a_k\circ\theta^{-g}\\
&\longrightarrow\theta^{-1}\theta^g\theta\theta^{-g}=\mathrm{id}.
\end{aligned}
\]
Norm convergence on each normal functional is exactly predual centrality of the unitary sequence. The classes \(C_g\in F\) satisfy
\[
C_{g+h}=C_g\gamma_g(C_h),\qquad C_0=1.
\]
The finite free-action coboundary theorem on \(F\) gives \(X\in\mathcal U(F)\) with \(C_g=X^*\gamma_g(X)\).

Lift \(X\) to central unitaries \(x_k\), using Theorem 5.1 of the exact-lift prerequisite with both coordinate endpoints equal to \(1\). Choose matching coordinates \(k_l\) at which all the first \(l\) predual centrality tests and all the finitely many cocycle errors are small. Reindex both \(a_{k_l}\) and \(x_{k_l}\), preserving the coordinate of the cocycle (3.2). Renaming the resulting pairs, we have ordinary convergence
\[
\begin{gathered}
c_{g,k}-x_k^*\theta^g(x_k)\longrightarrow0\\
\quad\text{strongly-star for every }g,
\end{gathered}\tag{3.3}
\]
and \((x_k)\) is central along the ordinary sequence. Explicitly, use a norm-dense sequence \((\psi_j)\) in the predual unit ball and require \(\|[x_{k_l},\psi_j]\|<1/l\) for \(j\le l\), as well as sharp faithful-state error less than \(1/l\) in (3.3) for every \(g\). Intersect those finitely many ultrafilter-large sets with \(k_l>k_{l-1}\). Theorem 3A.4 and Corollary 3A.6 of the bounded-topology prerequisite give the ordinary limits; the subsequence of \(\operatorname{Ad}a_k\) retains its original limit.

Set \(b_k=a_kx_k^*\). Its conjugations still converge to \(\theta\), since \(\operatorname{Ad}x_k\to\mathrm{id}\). Moreover
\[
\begin{aligned}
&\theta^g(b_k)-b_k\\
&=a_k\bigl(c_{g,k}-x_k^*\theta^g(x_k)\bigr)\theta^g(x_k^*)\\
&\longrightarrow0\\
&\quad\text{strongly-star}.
\end{aligned}\tag{3.4}
\]
The varying multipliers in (3.4) require control. For unitary central sequences this is the identity-limit case of Lemma 1.1 of the almost-invariant implementer prerequisite. The same is true of any unitary sequence with \(\operatorname{Ad}a_k\) convergent in the \(u\)-topology: for a null sequence \(r_k\), the difficult seminorm in \(r_ka_k\) is tested by \(\rho\circ\operatorname{Ad}(a_k^*)\), which converges in norm; the other seminorm is bounded directly by that of \(r_k^*\). Apply adjoints for \(a_kr_k\). Thus \(a_k,x_k\) and \(\theta^g(x_k)\) all normalize this ideal, justifying (3.4).

Average inside the fixed algebra:
\[
y_k=\frac1p\sum_{g=0}^{p-1}\theta^g(b_k)\in M^\theta.
\tag{3.5}
\]
By (3.4), \(y_k-b_k\to0\) strongly-star. Also \(y_k^*y_k-1\) and \(y_ky_k^*-1\) tend strongly-star to zero. Indeed \(b_k\) is unitary and normalizes the null ideal, while \(y_k-b_k\) belongs to that ideal, so expanding both products leaves only null terms.

The fixed algebra \(M^\theta\) is a countably decomposable factor by (1.2). Apply Lemma 2.1 there, with the restriction of a faithful normal state of \(M\). The restricted state seminorm is the same on its elements; Theorem 3A.4 and normal-inclusion transport therefore identify the bounded strong-star convergence in the fixed algebra with that needed in \(M\). We obtain unitaries \(w_k\) with \(w_k-y_k\to0\) strongly-star, hence \(w_k-b_k\to0\). The unitary
\[
z_k=w_kb_k^*
\]
tends strongly-star to \(1\), because \(b_k\) normalizes the null ideal. Consequently \(\operatorname{Ad}z_k\to\mathrm{id}\) in the \(u\)-topology, and
\[
\operatorname{Ad}w_k=\operatorname{Ad}z_k\circ\operatorname{Ad}b_k\longrightarrow\theta.
\]
This proves (3.1). The case \(p=1\) uses \(w_k=1\). \(\square\)

## 4. Central roots with a uniformly good cut

Use the principal Borel root \(f_p(e^{it})=e^{it/p}\), \(-\pi<t\leq\pi\), and the arcs \(J(-1,q)\) of angular radius \(2\pi4^{-q}\), \(q\geq3\).

**Lemma 4.1.** Suppose \((t_k)\) is a central sequence of unitaries and a faithful normal state \(\varphi\) satisfies
\[
\varphi(1_{J(-1,q)}(t_k))\leq2^{-q}
\quad(k\geq1,\ q\geq3).
\tag{4.1}
\]
Then \((f_p(t_k)^*)\) is central.

*Proof.* Put \(h(z)=\overline{f_p(z)}\). Fix \(q\). Keep \(h\) outside the interior of the cut arc, and interpolate linearly in its angular parameter between the two endpoint values inside the closed unit disk. This gives a continuous extension \(H\) with \(\|H\|_\infty\le1\).

Here is a fixed Laurent approximation, including the uniformity that will matter. With normalized Haar measure \(m\), put
\[
\begin{gathered}
K_N(e^{it})=\frac1N\left|\sum_{j=0}^{N-1}e^{ijt}\right|^2,
\qquad\\
g_N(z)=\int_{\mathbb T}K_N(\zeta)H(z\zeta^{-1})\,dm(\zeta).
\end{gathered}
\]
Expansion of the finite square shows that \(K_N\), and hence \(g_N\), is a Laurent polynomial. Orthogonality of the circle characters gives \(\int K_N\,dm=1\), and \(K_N\ge0\), so \(\|g_N\|_\infty\le1\). For \(0<\delta<\pi\), the geometric-sum formula gives
\[
K_N(e^{it})\le\frac{1}{N\sin^2(\delta/2)}
\quad(\delta\le|t|\le\pi).
\]
On \(|t|<\delta\), uniform continuity makes \(H(ze^{-it})-H(z)\) uniformly small for all \(z\); on the complementary arc its integral is bounded by \(2\|H\|_\infty/[N\sin^2(\delta/2)]\). First choose \(\delta\), then \(N\). This proves \(\|g_N-H\|_\infty\to0\).

Choose one such polynomial \(g\) within \(s<1\), keeping it fixed as \(k\) varies. In particular \(\|g\|_\infty\le2\). Splitting the spectral integral into the good and omitted arcs gives
\[
\varphi(|h(t_k)-g(t_k)|^2)\leq s^2+9\cdot2^{-q}.
\tag{4.2}
\]
For \(0\leq\psi\leq\varphi\), the difference is normal and Cauchy–Schwarz yields
\[
\|[h(t_k)-g(t_k),\psi]\|
\leq2(s^2+9\cdot2^{-q})^{1/2}.
\tag{4.3}
\]
Every fixed Laurent polynomial of the central \(t_k\) is central, by the commutator telescope. Let \(k\to\infty\) in (4.3), then \(s\to0\) and \(q\to\infty\). This proves centrality on all dominated positive functionals. Their linear span is norm dense in \(M_*\), by Lemma 2.1 of the comparison lesson. Uniform boundedness of \(h(t_k)\) extends the conclusion to all normal functionals. \(\square\)

**Theorem 4.2 (fixed finite-order implementers).** Under (1.1), there are unitaries \(u_k\in M^\theta\) such that
\[
\begin{gathered}
u_k^p=1,\qquad \operatorname{Ad}u_k\longrightarrow\theta\\
\quad\text{in the }u\text{-topology}.
\end{gathered}\tag{4.4}
\]

*Proof.* Take \(w_k\) from Theorem 3.1. Since \(\theta^p=\mathrm{id}\), the \(u\)-topological group law gives \(\operatorname{Ad}(w_k^p)\to\mathrm{id}\). Thus \(w_k^p\) is central.

Apply Lemma 2.1 of the finite-model prerequisite to the spectral probability measure of each \(w_k^p\). For clarity, the arcs used here have normalized Haar measure \(2\cdot4^{-q}\). Fubini gives that mean value for their spectral masses as the center varies; Markov bounds the set where the mass exceeds \(2^{-q}\) by \(2^{1-q}\). The sum over \(q\ge3\) is \(1/2\), so a simultaneous good center \(z_k\) exists, even for atomic spectral measures. Choose \(\rho_kz_k=-1\), then \(\lambda_k^p=\rho_k\). Rotation of the spectral measure supplies scalars \(\lambda_k\in\mathbb T\) such that
\[
t_k=(\lambda_kw_k)^p
\]
obeys (4.1) for the fixed faithful state \(\varphi\). Multiplying by scalars preserves centrality and does not change any inner automorphism. Lemma 4.1 makes \(r_k=f_p(t_k)^*\) central. It is fixed by \(\theta\), because the fixed von Neumann algebra contains \(w_k\) and all its bounded Borel functions, and it commutes with \(w_k\), because it is a Borel function of its power.

Set \(u_k=\lambda_kw_kr_k\). These are fixed unitaries and
\[
u_k^p=t_k f_p(t_k)^{*p}=1.
\]
Centrality of \(r_k\) gives \(\operatorname{Ad}r_k\to\mathrm{id}\). Therefore \(\operatorname{Ad}u_k\to\theta\), proving (4.4). For \(p=1\) one may again take \(u_k=1\). \(\square\)

**Example 4.3 (a central sequence with a noncentral root).** In \(M_2\overline\otimes R\), put
\[
t_k=
\begin{pmatrix}
e^{i(\pi-1/k)}&0\\0&e^{i(-\pi+1/k)}
\end{pmatrix}\otimes1.
\]
It converges in operator norm to the scalar \(-1\), so it is central. But \(f_2(t_k)\) converges to \(\operatorname{diag}(i,-i)\otimes1\), which is noncentral. Thus an index dependent continuous approximation to a discontinuous root cannot replace the uniform cut estimate. For every fixed sufficiently small cut arc, both eigenvalues eventually lie inside it, violating (4.1).

The same obstruction occurs for fixed approximate implementers satisfying all of (1.1). Take \(R=\overline{\bigotimes}_{j\ge1}M_2\), \(\theta=\sigma_2\), \(Z=c_2\otimes1\otimes\cdots\), and \(A_k=c_2^{\otimes k}\otimes1\otimes\cdots\), with \(c_2=\operatorname{diag}(1,-1)\). Then
\[
\begin{gathered}
w_k=iA_k e^{-iZ/(2k)}\in R^\theta,\qquad\\
\operatorname{Ad}w_k\longrightarrow\theta,\qquad\\
w_k^2=-e^{-iZ/k}\longrightarrow-1
\end{gathered}
\]
in the indicated automorphism and operator-norm topologies. The convergence of the inner automorphisms follows first on each fixed tensor head and then on the predual by its finite-head density. Proposition 5.1 of the absorption prerequisite gives \(p_a(\sigma_2)=2\). The principal logarithm is
\[
h_k=(\pi-1/k)Z,\qquad w_k^2=e^{ih_k}.
\]
Thus both \(h_k\) and \((1-1/k)h_k\) have the noncentral limit \(\pi Z\), although every shrunken exponential has spectrum avoiding \(-1\). Avoidance for each individual index does not provide one uniformly valid continuous logarithm along the sequence. This invalidates that step of the printed proof of [Takesaki III], Lemma XVII.3.17; it does not invalidate the lemma's conclusion, proved above. The printed positive exponential for the root correction also has the wrong orientation for cancelling \(w_k^p\); Theorem 4.2 and Exercise 6.1 use the adjoint.

## 5. Genuine conjugacy after cyclic tensor absorption

Let \(\sigma_p=\bigotimes_{v\geq1}\operatorname{Ad}c_p\) be the product model of period \(p\) on \(R\), with \(\sigma_1=\mathrm{id}_R\).

**Proposition 5.1.** Under (1.1), the actions \(\theta\) and \(\theta\otimes\sigma_p\) are conjugate.

*Proof.* The case \(p=1\) is the identity action and strong stability. Suppose \(p>1\). Proposition 6.3 of the absorption prerequisite, applied with \(p\mid p_a(\theta)\), supplies a normal isomorphism \(\pi:M\to M\overline\otimes R\) and a unitary \(v\in M\) with
\[
\pi\circ\operatorname{Ad}v\circ\theta\circ\pi^{-1}
=\theta\otimes\sigma_p.
\tag{5.1}
\]
The right-hand action here is the original \(\theta\otimes\sigma_p\). Both actions on the two sides have \(p\)-th power equal to the identity. Hence the iterated product \(v_p=v\theta(v)\cdots\theta^{p-1}(v)\) is scalar. Write \(v_p=\zeta1\), choose \(\mu\in\mathbb T\) with \(\mu^p=\overline\zeta\), and replace \(v\) by \(\mu v\). This preserves \(\operatorname{Ad}v\) and makes the new \(v_p=1\). The products \(v_g\) now form a unitary cocycle for the free cyclic action \(\theta\) on \(M\).

The ordinary finite-action coboundary theorem (1.3), with its general algebra scope, gives a unitary \(a\in M\) with \(v_g=a^*\theta^g(a)\). In particular
\[
\operatorname{Ad}v\circ\theta
=\operatorname{Ad}(a^*)\circ\theta\circ\operatorname{Ad}a.
\]
Substituting in (5.1), the isomorphism \(\pi\circ\operatorname{Ad}(a^*)\) conjugates \(\theta\) to \(\theta\otimes\sigma_p\). \(\square\)

The asymptotic-period equality in (1.1) remains part of this result. It is what permits absorption of the period-\(p\) model.

## 6. Exercises with solutions

**Exercise 6.1 (introductory: root orientation).** Let \(w=e^{i\pi/4}\) and \(p=2\). Calculate \(wf_2(w^2)^*\) and \(wf_2(w^2)\), and compare their squares.

*Solution.* The principal root of \(w^2=i\) is \(e^{i\pi/4}=w\). The first product is \(1\), whose square is \(1\); the second is \(i\), whose square is \(-1\). The adjoint on the root is essential in Theorem 4.2.

**Exercise 6.2 (intermediate: two defect conditions).** Why does \(y_k^*y_k\to1\) alone not suffice in Lemma 2.1? Use the constant unilateral shift on \(\ell^2(\mathbb N)\).

*Solution.* The unilateral shift \(S\) satisfies \(S^*S=1\), but \(SS^*=1-e_{11}\). If unitaries \(w_k\) satisfied \(w_k-S\to0\) strongly-star, bounded multiplication would imply \(SS^*=\lim w_kw_k^*=1\), a contradiction. The second defect condition prevents this.

**Exercise 6.3 (intermediate: inspect the root counterexample).** For \(t_k\) in Example 4.3, evaluate the limit of the commutator \([f_2(t_k),e_{12}\otimes1]\).

*Solution.* If the two diagonal root entries are \(a_k,b_k\), this commutator is \((a_k-b_k)e_{12}\otimes1\). Their limits are \(i,-i\), so the coefficient tends to \(2i\). Its operator norm tends to \(2\), and its tracial \(L^2\) norm tends to \(\sqrt2\). The root sequence is not central.

**Exercise 6.4 (advanced: the cocycle correction order).** With \(c_{g,k}=a_k^*\theta^g(a_k)\), suppose \(c_{g,k}\) is close to \(x_k^*\theta^g(x_k)\). Which of \(a_kx_k^*\) and \(x_k^*a_k\) has the cancellation in (3.4)? Derive it.

*Solution.* For \(b_k=a_kx_k^*\),
\[
\begin{aligned}
&\theta^g(b_k)-b_k\\
&=a_kc_{g,k}\theta^g(x_k^*)-a_kx_k^*\\
&=a_k\bigl(c_{g,k}-x_k^*\theta^g(x_k)\bigr)\theta^g(x_k^*).
\end{aligned}
\]
The two factors involving \(\theta^g(x_k)\) cancel in the indicated order. The other product generally lacks this cancellation.

**Exercise 6.5 (advanced: why asymptotic period is needed).** Suppose \(\theta^p=\mathrm{id}\) but \(p_a(\theta)=d<p\). Use a central sequence in the model factor to show that \(\theta\) cannot be conjugate to \(\theta\otimes\sigma_p\).

*Solution.* The \(d\)-th power of \(\theta\) is centrally trivial. In a far-out \(M_p\) coordinate of \(R\), let \(z_k=e_{12}\). These form a bounded central sequence, while \(\sigma_p^d(z_k)=e^{-2\pi id/p}z_k\), with a phase different from one and a fixed nonzero \(L^2\) displacement. The sequence \(1\otimes z_k\) is central in \(M\overline\otimes R\), by product functional tests and norm density, and is moved by \((\theta\otimes\sigma_p)^d\). Thus that power is not centrally trivial. Conjugacy would preserve central triviality of powers, giving a contradiction.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Propositions 1.1.1–1.1.3 and Lemma 1.1.4 supply the centralizer and lifting source; Lemma 3.1.1, pages 409–410, supplies the implementing-defect method. Lemmas 3.1.3–3.1.4 and 3.2.3, pages 412–415, supply the good-cut and fixed-polynomial root method. The finite-group cohomology input here is separate. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. Section 3.1 and Definition 4.34–Proposition 4.35 give modern quotient context. The actual finite quotient and exact lifts consumed here are proved in the programme prerequisite named in the introduction. [Open author version](https://arxiv.org/abs/1212.5457).

[Takesaki II] Masamichi Takesaki, *Theory of Operator Algebras II*, Encyclopaedia of Mathematical Sciences 125, Springer, 2003, Proposition XI.2.26, pp.347–348. Source of the finite free-action theorem and part of the actual earlier construction consultation. Its proof explicitly assumes countable decomposability while stating the general extension; the complete arbitrary-cardinal proof used here is [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md), including its unrestricted projection, standard-form, trace and topology interfaces. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10451-4).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003, Lemmas XVII.3.17–3.18. These are the finite-order implementer and genuine-conjugacy targets compared during the original construction. The fixed-factor completion and uniform-cut argument above give the detailed repairs; Example 4.3 records the exact proof issue. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).

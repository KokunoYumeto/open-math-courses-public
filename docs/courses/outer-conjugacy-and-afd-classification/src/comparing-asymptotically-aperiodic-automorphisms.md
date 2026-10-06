# Comparing asymptotically aperiodic automorphisms

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026; revised by GPT-6 Astra (OpenAI), Ultra, October 2026, with writing-AI self-checking. New original text is public domain (CC0).*

## Introduction

An approximately inner automorphism can be approximated on a finite list of normal functionals by conjugation with a unitary. For classification, we need a compatible sequence of such approximations. We arrange that successive finite matrix factors carry prescribed cyclic actions, that their averaging errors are summable, and that the remaining action disappears in the limit.

Two issues require separate arguments. The complementary tensor factor obtained by this construction need not be isomorphic to the original factor. We repair that by extracting an additional identity action on a hyperfinite factor. Also, small perturbations of two automorphisms do not automatically combine into one small perturbation in a fixed state. An approximate coboundary argument supplies precisely that last control.

The main construction is [Connes], Section III, especially Lemma 3.2.7 and the conclusion of Theorem 2. [Takesaki III], Theorem XVII.3.1, Lemma XVII.3.9 and Corollary XVII.3.10, presents the corresponding classification, finite-stage induction and hyperfinite specialization. We separate the product extraction, comparison of complements, ordinary approximate coboundary and final state transport. [Connes periodic] supplies the central-triviality comparison for \(R\); [Ando–Haagerup] supplies modern multiplier-algebra context.

The immediate prerequisites are [Cyclic finite models for outer conjugacy](cyclic-finite-models-for-outer-conjugacy.md), Lemma 1.0, Theorem 4.1 and Lemmas 5.1–5.3; [Moving hyperfinite tensor factors](moving-hyperfinite-tensor-factors.md), Theorem 1.1; and [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md), Section 1, Theorem 3.2, Lemma 4.2, Corollary 6.2 and Proposition 6.3. Section 1 of the absorption lesson states the general normal-functional tensor-splitting theorem and proves its extension from dense states to a norm-total family. For faithful-state GNS, commutant density and bounded strong-star convergence we use [Bounded ultrastrong topology and the semifinite tracial representation](bounded-topology-and-tracial-representations.md), Lemma 3A.3 and Theorem 3A.4.

The hyperfinite inputs have the following exact programme proofs: Local approximation and the hyperfinite finite factor, Theorem 6.3, proves approximate innerness of every automorphism of \(R\); Centrally trivial automorphisms and decreasing AFD factors, Lemma 4.1 and Theorem 4.2, prove \(\operatorname{Cnt}R=\operatorname{Inn}R\). The expected-subfactor argument in Section 4 uses Averaging, crossed products, and injectivity, Proposition 5.1 and Corollary 5.2, and Small corners and the second injective proof, Theorem 4.1. These retain their stated projection, trace-expectation, infinite-product and finite-approximation prerequisites.

Throughout, \(M\) is a strongly stable factor with separable predual. Thus \(M\cong M\overline\otimes R\), where \(R\) is the hyperfinite II₁ factor. The notation \(\overline{\operatorname{Inn}}M\) means closure in the \(u\)-topology, namely norm convergence of the induced maps on every normal functional. We write
\[
\|x\|_\varphi^\sharp=\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr)^{1/2}.
\]
Asymptotic aperiodicity means \(p_a(\theta)=0\): no nonzero power acts trivially on the asymptotic centralizer.

## 1. The classification statement

**Theorem 1.1.** Suppose \(\theta_1,\theta_2\in\overline{\operatorname{Inn}}M\) and
\[
p_a(\theta_1)=p_a(\theta_2)=0.
\tag{1.1}
\]
There are \(\sigma\in\overline{\operatorname{Inn}}M\) and \(u\in\mathcal U(M)\) such that
\[
\theta_2=\operatorname{Ad}u\circ\sigma\circ\theta_1\circ\sigma^{-1}.
\tag{1.2}
\]
Moreover, for every faithful normal state \(\varphi\) and every \(\varepsilon>0\), there are \(w\in\mathcal U(M)\) and \(\gamma\in\overline{\operatorname{Inn}}M\) such that
\[
\begin{gathered}
\|w-1\|_\varphi^\sharp<\varepsilon,\\
\theta_2=\gamma\circ\operatorname{Ad}w\circ\theta_1\circ\gamma^{-1}.
\end{gathered}\tag{1.3}
\]

The use of asymptotic period is essential. Ordinary outer aperiodicity does not imply the centralizer cohomology needed for the construction.

We prove (1.2) in Sections 2–4 and the stronger estimate (1.3) in Sections 5–6.

## 2. Functional tests and finite corners

**Lemma 2.1 (dominated tests suffice).** For a faithful normal state \(\varphi\), there is a sequence of positive normal functionals \((\psi_j)\) with \(0\leq\psi_j\leq\varphi\) whose complex linear span is norm dense in \(M_*\).

*Proof.* Use the faithful normal GNS representation of Lemma 3A.3 of the bounded-topology prerequisite, and let \(\xi_\varphi\) be its state vector. The commutant-density argument in Theorem 3A.4 gives \(\overline{M'\xi_\varphi}=H_\varphi\); it uses separation of the state vector and the bicommutant theorem. For every contraction \(b'\in M'\), set
\[
\psi_{b'}(x)=\langle xb'\xi_\varphi,b'\xi_\varphi\rangle.
\]
For \(x\geq0\), commutation and \(b'^*b'\leq1\) show \(0\leq\psi_{b'}(x)\leq\varphi(x)\). These functionals separate \(M\). Indeed, \(M'\xi_\varphi\) is dense; if all the quadratic forms above vanish on an element \(x\), rescaling and polarization give \(\langle x\eta,\zeta\rangle=0\) on a dense set of vectors, hence \(x=0\).

The annihilator in \(M=(M_*)^*\) of their linear span is therefore zero. Hahn–Banach implies that the span is norm dense in \(M_*\). Separability of \(M_*\) allows a countable subfamily with the same property. Enumerate it as \((\psi_j)\). \(\square\)

**Lemma 2.2 (approximate innerness in a finite complement).** Suppose
\[
\begin{gathered}
M=N\overline\otimes C,\qquad N\cong M_d(\mathbb C),\\
\theta=\operatorname{Ad}S\otimes\beta,
\end{gathered}\tag{2.1}
\]
where \(S\in\mathcal U(N)\). If \(\theta\) is approximately inner, then \(\beta\) is approximately inner on \(C\). Also \(p_a(\beta)=p_a(\theta)\).

*Proof.* Let \(\operatorname{Ad}a_k\to\theta\). The systems \(a_ke_{ij}a_k^*\) converge strongly-star to \(Se_{ij}S^*\). Exact close-matrix comparison gives \(b_k\to1\) strongly-star with
\[
b_ka_ke_{ij}a_k^*b_k^*=Se_{ij}S^*.
\]
Here is the exact comparison. Put \(E_{ij,k}=a_ke_{ij}a_k^*\) and \(G_{ij}=Se_{ij}S^*\). Their first diagonals are equivalent because both are unitarily conjugate to \(e_{11}\). Lemma 1.0 of the finite-model prerequisite gives partial isometries \(r_k\) with
\[
\begin{gathered}
r_k^*r_k=E_{11,k},\qquad r_kr_k^*=G_{11},\\
r_k-G_{11}\longrightarrow0\text{ strongly-star}.
\end{gathered}
\]
Then \(b_k=\sum_{i=1}^dG_{i1}r_kE_{1i,k}\) is unitary, by the matrix relations, and \(b_kE_{ij,k}b_k^*=G_{ij}\). Each factor in this finite sum has a strong-star limit; its limit is \(\sum_iG_{i1}G_{11}G_{1i}=1\). Thus \(b_k\to1\) strongly-star in every factor type. The initial convergence of \(E_{ij,k}\) follows from \(u\)-convergence: expand the square of a displacement in any normal positive functional; the square term tests the image of \(e_{ij}^*e_{ij}\), and the cross terms use fixed normal functionals. Apply the same expansion to adjoints.

Thus \(c_k=S^*b_ka_k\) commutes with \(N\), so \(c_k\in C\). Conjugation by \(b_k\) tends to the identity in the \(u\)-topology: for fixed \(\psi\), the Cauchy–Schwarz estimate for \(\psi\) and a positive decomposition of it gives \(\|\psi\circ\operatorname{Ad}b_k-\psi\|\to0\). Consequently
\[
\operatorname{Ad}c_k\longrightarrow
\operatorname{Ad}(S^*)\circ\theta=\mathrm{id}_N\otimes\beta.
\]
Restricting normal functional tests to \(C\) proves approximate innerness there. The equality of asymptotic periods is the finite-leg centralizer identification proved in Lemma 4.2 of the absorption lesson. \(\square\)

The finite dimension of \(N\) is used twice: in exact matrix comparison and in the finite coefficient expansions of normal functionals.

## 3. Extracting a common product action

Choose integers \(n_v\geq2\) with
\[
\sum_{v=1}^\infty\frac1{n_v}<\infty.
\tag{3.1}
\]
Let \(c_v\) be the cyclic shift on \(\mathbb C^{n_v}\). The abstract tracial product
\[
\begin{gathered}
K_{\mathrm{mod}}=\overline{\bigotimes_{v\geq1}}(M_{n_v},\operatorname{tr}_{n_v})
\cong R,\\
\alpha=\bigotimes_{v\geq1}\operatorname{Ad}c_v
\end{gathered}\tag{3.2}
\]
depends only on this chosen sequence.

**Theorem 3.1 (product extraction).** If \(\theta\in\overline{\operatorname{Inn}}M\) has \(p_a(\theta)=0\), then there are a unitary \(W\), a tensor decomposition \(M=K\overline\otimes C_\infty\), and an action preserving isomorphism \(K_{\mathrm{mod}}\to K\), such that
\[
\operatorname{Ad}W\circ\theta=\alpha\otimes\mathrm{id}_{C_\infty}.
\tag{3.3}
\]
With a prescribed faithful state, the construction satisfies
\[
\|W-1\|_\varphi^\sharp\leq8\sum_v\frac1{n_v}.
\tag{3.4}
\]

*Proof.* Choose \((\psi_j)\) from Lemma 2.1. Put
\[
\delta_v=\frac{2^{-v}}{n_v^2(n_v+1)},\qquad
\eta_v=3\eta(n_v,\delta_v/3),
\tag{3.5}
\]
where \(\eta(n,\delta)\) is the state independent constant from the normalized-cycle centrality lemma. Choose decreasing positive numbers \(\varepsilon_v\to0\) with
\[
\varepsilon_v<\min\{2^{-v},\eta_{v+1}/4\}.
\tag{3.6}
\]
They may, for example, be chosen recursively with \(\varepsilon_v<\varepsilon_{v-1}/2\).

We construct commuting factors \(K_v\cong M_{n_v}\), cyclic unitaries \(U_v\in K_v\), and correcting unitaries \(a_v\) in the preceding relative commutants. Write
\[
\begin{gathered}
N_v=K_1\vee\cdots\vee K_v,\\
S_v=U_v\cdots U_1,\\
W_v=a_v\cdots a_1,\\
\theta_v=\operatorname{Ad}W_v\circ\theta.
\end{gathered}
\]
Set \(S_0=W_0=1\). Our requirements are
\[
\begin{gathered}
\theta_v|_{N_v}=\operatorname{Ad}S_v|_{N_v},\\
\|\psi_j\circ\theta_v^{-1}-\psi_j\circ\operatorname{Ad}(S_v^*)\|<\varepsilon_v\\
(j\leq v),\\
\|[F_i^{(v)},\psi_j]\|<\delta_v\\
(j\leq v,\ 0\leq i<n_v),\\
\|[U_v,\psi_j]\|<\delta_v\qquad(j<v),\\
\|W_v-W_{v-1}\|_\varphi^\sharp<8/n_v.
\end{gathered}\tag{3.7}
\]
Here \(F_i^{(v)}\) is the projection partition rotated by \(U_v\), and \(U_v^{n_v}=1\).

Assume the construction through \(v-1\), and put \(C=N_{v-1}'\cap M\). The exact action on \(N_{v-1}\) gives
\[
\theta_{v-1}=\operatorname{Ad}S_{v-1}\otimes\beta
\quad\text{on }N_{v-1}\overline\otimes C.
\tag{3.8}
\]
Theorem 5.1 and the finite-leg identification of Lemma 4.1 in the strong-stability prerequisite make \(C\) strongly stable, as specified in Section 1 of the absorption lesson. Lemma 2.2 makes \(\beta\) approximately inner and asymptotically aperiodic.

Use the faithful state on \(M\)
\[
\chi_v=\frac13\bigl(\varphi+\varphi\circ\theta_{v-1}^{-1}
+\varphi\circ\operatorname{Ad}(W_{v-1}^*)\bigr),
\tag{3.9}
\]
and its restriction to \(C\). Expand the first \(v\) functionals into coefficients for \(N_{v-1}\overline\otimes C\). Lemma 5.3 of the finite-model lesson lets its Theorem 4.1 in \(C\) meet arbitrarily small tolerances on the original functionals. In its inverse-predual estimate take the scalar-matrix action to be \(\operatorname{Ad}(S_{v-1}^*)\), and the complementary action to be \(\beta^{-1}\). It gives a partition \(F_i\), a unitary \(u\), and a unitary \(t\in C\), with
\[
\begin{gathered}
uF_iu^*=F_{i+1},\\
\|[F_i,\psi_j]\|<\delta_v\quad(j\leq v),\\
\begin{aligned}
&\|\psi_j\circ\theta_{v-1}^{-1}\\
&\quad-\psi_j\circ\operatorname{Ad}((uS_{v-1})^*)\|
<\varepsilon_v/2
\end{aligned}\\
(j\leq v),\\
\chi_v(1_{J(-1,q)}(u^{n_v}))\leq2^{-q}\quad(q\geq3),\\
\operatorname{Ad}t\circ\beta|_{K_v}=\operatorname{Ad}U_v|_{K_v},
\end{gathered}\tag{3.10}
\]
where
\[
\begin{gathered}
b=f_{n_v}(u^{n_v})^*,\qquad U_v=ub,\\
K_v=\{U_v,F_i\}''.
\end{gathered}
\]
The root commutes with \(K_v\), and \(\|b-1\|\leq\pi/n_v\). Choose the tolerance for \(t\) so small that
\[
\begin{gathered}
\sqrt3\|t-1\|_{\chi_v}^\sharp<1/n_v,\\
2\sqrt3\|t-1\|_{\chi_v}^\sharp<\varepsilon_v/2.
\end{gathered}\tag{3.11}
\]
All the other finite tolerances can be retained while doing this.

Set \(a_v=bt\). Both factors lie in \(C\). Thus earlier block actions persist, and the new block action remains \(\operatorname{Ad}U_v\), because \(b\) commutes with \(K_v\).

We verify the inverse-predual estimate. Since \(0\leq\psi_j\leq\varphi\), unitary conjugation satisfies
\[
\|\psi_j\circ\operatorname{Ad}z-\psi_j\|
\leq2\|z-1\|_\varphi^\sharp.
\tag{3.12}
\]
For \(z=\theta_{v-1}^{-1}(t^*)\), (3.9) bounds the right side by \(2\sqrt3\|t-1\|_{\chi_v}^\sharp\). Therefore inserting \(\operatorname{Ad}t^*\) after \(\theta_{v-1}^{-1}\) changes each test by less than \(\varepsilon_v/2\). Finally compose both compared functionals with \(\operatorname{Ad}b^*\), an isometry of the predual. Since \(b\) commutes with \(u\) and \(S_{v-1}\), the approximating unitary becomes
\[
S_{v-1}^*u^*b^*=(U_vS_{v-1})^*=S_v^*.
\]
This proves the second line of (3.7).

For \(j<v\), compare the previous second line of (3.7) with the second line of (3.10). Since \(u\) commutes with \(S_{v-1}\), their difference gives
\[
\begin{aligned}
\|[u,\psi_j]\|
&=\|\psi_j\circ\operatorname{Ad}(u^*)-\psi_j\|\\
&<\varepsilon_{v-1}+\varepsilon_v/2<\eta_v.
\end{aligned}\tag{3.13}
\]
We apply the normalized-cycle lemma on \(M\), with state \(\chi_v\) and functional \(\psi_j/3\). This is legitimate because \(\psi_j\leq\varphi\leq3\chi_v\); the spectral test in (3.10) is the same test whether evaluated in \(C\) or \(M\). Equations (3.5) and (3.13) yield
\[
\|[U_v,\psi_j]\|<\delta_v.
\]
No estimate of this kind is required for the new functional \(\psi_v\) at its first stage.

The product estimate must also include the moving \(W_{v-1}\). Direct expansion gives
\[
\begin{aligned}
&\|(t-1)W_{v-1}\|_\varphi^\sharp{}^2\\
&=\varphi\circ\operatorname{Ad}(W_{v-1}^*)
((t-1)^*(t-1))\\
&\quad+\varphi((t-1)(t-1)^*)\\
&\leq3\|t-1\|_{\chi_v}^\sharp{}^2.
\end{aligned}\tag{3.14}
\]
The other term in
\[
\begin{aligned}
(bt-1)W_{v-1}
&=(b-1)tW_{v-1}\\
&\quad+(t-1)W_{v-1}
\end{aligned}
\]
has state seminorm at most \(\sqrt2\pi/n_v\), by its operator norm. Hence (3.11) gives
\[
\|W_v-W_{v-1}\|_\varphi^\sharp
<(\sqrt2\pi+1)/n_v<8/n_v.
\]
This completes the induction.

By (3.1), \(W_v\) and \(W_v^*\) are bounded strong-star Cauchy sequences. Their limits are a unitary \(W\) and its adjoint. The triangle inequality gives (3.4). Every finite block action passes to \(\theta_\infty=\operatorname{Ad}W\circ\theta\).

For fixed \(j\) and \(v>j\), the cycle-to-expectation estimate gives
\[
\|\psi_j-\psi_j\circ E_{K_v}\|
\leq n_v^2(n_v+1)\delta_v=2^{-v}.
\tag{3.15}
\]
The earlier finitely many terms cause no problem. The normal-functional summability theorem, in the norm-total form proved in Section 1, (1.2a)–(1.2b), of the absorption lesson, therefore identifies
\[
\begin{gathered}
M=K\overline\otimes C_\infty,\\
K=\bigvee_vK_v\cong K_{\mathrm{mod}},\\
C_\infty=K'\cap M.
\end{gathered}\tag{3.16}
\]
The identification \(\iota:K_{\mathrm{mod}}\to K\) sends every elementary tensor to the product of its chosen matrix coordinates. On each finite head this preserves the normalized trace and the matrix relations. TF2–TF3 of [Normal tensor tests and tracial GNS identifications](../foundations/normal-tensor-and-tracial-product-foundations.md) give the complete trace-GNS extension and normal inverse. The splitting proof supplies the required injectivity, faithful normal state and finite-head trace data; mere commutation of the blocks would not suffice. It sends \(c_v\) to \(U_v\), so it intertwines the product action with the action on \(K\); we use \(\alpha\) for this transported action.

To determine the complementary action, \(\operatorname{Ad}S_v\) converges in the \(u\)-topology to \(\alpha\otimes\mathrm{id}\). On the tracial product \(K\), TF4 supplies the finite-vector proof of this predual limit, including the approximation often expressed through \(L^1\) functionals: the partial product GNS unitaries and their inverses agree eventually with those of \(\alpha\) on each local vector. On \(K\overline\otimes C_\infty\), TF1 and TF4 prove the extension by norm-dense product normal functionals, with no trace assumption on the complementary leg.

Meanwhile, \(\theta_v^{-1}\to\theta_\infty^{-1}\) in the \(u\)-topology, since \(W_v\to W\) strongly-star. Let \(v\to\infty\) in the second line of (3.7), for each fixed \(j\). The errors \(\varepsilon_v\) tend to zero. Norm-totality of the \(\psi_j\) gives
\[
\theta_\infty^{-1}=(\alpha\otimes\mathrm{id})^{-1}
\]
on all normal functional tests, hence on \(M\). This proves (3.3), including the identity action on the complement. \(\square\)

**Example 3.2.** Taking \(n_v=2^{v+m}\), with \(m\geq1\), gives \(\sum_v1/n_v=2^{-m}\) and \(\|W-1\|_\varphi^\sharp\leq8\cdot2^{-m}\). The matrix sizes grow; the factor generated by them is still \(R\).

**Lemma 3.3.** The product automorphism \(\alpha\) in (3.2) satisfies \(p_a(\alpha)=0\).

*Proof.* Fix a nonzero integer \(q\). In the Fourier basis of the \(v\)-th cyclic shift, let \(x_v\) be the Weyl unitary shifting the basis index by \(r_v\), where \(r_v\) is an integer nearest to \(n_v/(2|q|)\). Then, with a choice of orientation,
\[
\operatorname{Ad}c_v(x_v)=e^{2\pi i r_v/n_v}x_v.
\]
As \(n_v\to\infty\), the eigenvalue for the \(q\)-th power tends to \(-1\). The \(x_v\) are unitaries of trace norm \(\|x_v\|_2=1\), and their tail embeddings form a central sequence in \(R\). Thus
\[
\|\alpha^q(x_v)-x_v\|_2
=|e^{2\pi iqr_v/n_v}-1|\longrightarrow2.
\]
No nonzero power is centrally trivial. \(\square\)

The use of a unitary at a varying frequency matters. A fixed matrix entry with phase \(e^{2\pi i/n_v}\) would have displacement tending to zero and, in growing matrix size, vanishing \(L^2\) norm.

**Lemma 3.4 (prescribed finite tests).** For any prescribed sequence \(0\leq\psi_j\leq\varphi\), the commuting finite factors, partitions and unitaries can be constructed to satisfy (3.7), with \(U_v^{n_v}=1\) and \(a_v\in N_{v-1}'\cap M\). Norm-totality of this sequence is not required for this assertion.

*Proof.* The induction proving (3.7) uses only positivity, domination by \(\varphi\), and the finitely many coefficient functionals at each stage. Equations (3.8)–(3.14) consequently apply without a totality hypothesis. Totality is used only afterward, for tensor splitting and identification of the limiting action. This proves the stated finite-test version for an arbitrary prescribed sequence. \(\square\)

## 4. Making the complements comparable

The decomposition (3.16) alone does not say \(C_\infty\cong M\). The tensor-factor placement theorem requires that hypothesis. We now obtain it for a different hyperfinite leg.

Apply Corollary 6.2 of the absorption lesson with the identity model \(\sigma_1=\mathrm{id}_R\) to the asymptotically aperiodic \(\alpha\) on \(K_{\mathrm{mod}}\cong R\). Its divisibility condition holds because \(1\) divides \(0\). There are a unitary \(t\in K_{\mathrm{mod}}\) and a decomposition
\[
\begin{gathered}
K_{\mathrm{mod}}=A\overline\otimes B,\qquad B\cong R,\\
\operatorname{Ad}t\circ\alpha=\beta\otimes\mathrm{id}_B.
\end{gathered}\tag{4.1}
\]
Both \(A\) and \(B\) are factors. The factor \(A\) is an infinite dimensional subfactor of \(R\), so \(A\cong R\). Here is the exact reasoning for the dimension and injectivity assertions. If \(A\) were a finite matrix factor, every automorphism of it would be inner, making the whole action in (4.1) inner. This contradicts Lemma 3.3, since inner perturbations preserve asymptotic period. The trace-preserving expectation \(R\to A\), composed with an injective projection onto \(R\), makes \(A\) injective. It has separable predual, and the uniqueness theorem for the injective II₁ factor gives \(A\cong R\). More explicitly, Corollary 5.2 of the averaging prerequisite gives a ucp retraction \(P:B(H)\to R\) in a faithful normal representation. The normal trace expectation \(E_A:R\to A\) makes \(E_AP:B(H)\to A\) a ucp retraction, so \(A\) is injective. Its restricted normalized trace and infinite dimension make it type II₁, and Theorem 4.1 of the small-corner prerequisite gives the normal isomorphism \(A\cong R\).

There is also a direct choice of these same objects from the original-action absorption statement, Proposition 6.3. With \(p=1\), it gives \(t\in\mathcal U(K_{\mathrm{mod}})\) and a normal isomorphism \(h:K_{\mathrm{mod}}\to K_{\mathrm{mod}}\overline\otimes R\) such that
\[
h\circ\operatorname{Ad}t\circ\alpha\circ h^{-1}
=\alpha\otimes\mathrm{id}_R.
\]
Take \(A=h^{-1}(K_{\mathrm{mod}}\otimes1)\), \(B=h^{-1}(1\otimes R)\), and \(\beta=(\operatorname{Ad}t\circ\alpha)|_A\). The two inverse images commute and factorize \(K_{\mathrm{mod}}\), both are normally isomorphic to \(R\), and the action is exactly (4.1). This gives the required hyperfinite complement directly; the preceding expected-subfactor argument remains a second justification when one starts only with Corollary 6.2.

Perform Theorem 3.1 for both \(\theta_i\), using the same \(n_v\). Transport the same \(t,A,B,\beta\) from the abstract product model to the two extracted copies \(K_i\). After the corresponding inner perturbations \(h_i\in\mathcal U(M)\), we have
\[
\begin{gathered}
\theta_i'=\operatorname{Ad}h_i\circ\theta_i
=\beta_i\otimes\mathrm{id}_{D_i}\\
\text{on }M=A_i\overline\otimes D_i,
\end{gathered}\tag{4.2}
\]
where \(A_i\cong R\), the actions \(\beta_i\) correspond to the same \(\beta\), and
\[
D_i=B_i\overline\otimes C_i
\cong K_i\overline\otimes C_i\cong M.
\tag{4.3}
\]
The middle isomorphism uses \(B_i\cong K_i\cong R\); it concerns algebras, not an identification of their actions.

Theorem 1.1 of the tensor-factor placement lesson now gives an approximately inner automorphism \(\sigma_0\) of \(M\) with \(\sigma_0(A_1)=A_2\). Its restriction need not be the chosen action preserving isomorphism \(\vartheta:A_1\to A_2\). Correct this by
\[
\kappa=\bigl(\vartheta\circ(\sigma_0|_{A_1})^{-1}\bigr)\otimes\mathrm{id}_{D_2}.
\tag{4.4}
\]
Every automorphism of \(A_2\cong R\) is approximately inner. Extending its inner approximants by the identity on \(D_2\), and testing first on product functionals, shows that \(\kappa\) is approximately inner on \(M\). Thus \(\sigma=\kappa\circ\sigma_0\) is approximately inner and
\[
\sigma\circ\theta_1'\circ\sigma^{-1}=\theta_2'.
\tag{4.5}
\]
On \(A_2\) this is the prescribed identification of \(\beta\); on \(D_2\) both actions are the identity.

Unwinding the two perturbations gives (1.2), explicitly with
\[
u=h_2^*\sigma(h_1).
\tag{4.6}
\]
This proves the outer-conjugacy part of Theorem 1.1.

## 5. Ordinary cocycles are approximately coboundaries

The following lemma controls a unitary of \(M\) itself. It asserts approximation in a state seminorm, rather than an exact ordinary coboundary.

**Lemma 5.1.** Let \(\beta\in\operatorname{Aut}M\) have \(p_a(\beta)=0\). Given \(u\in\mathcal U(M)\), a faithful normal state \(\rho\), and \(\varepsilon>0\), there is \(x\in\mathcal U(M)\) such that
\[
\|xu\beta(x^*)-1\|_\rho^\sharp<\varepsilon.
\tag{5.1}
\]
Approximate innerness of \(\beta\) is not required.

*Proof.* Fix an integer \(n\geq2\). Apply Theorem 3.2 of the absorption lesson, the exact phase-matrix theorem, with phase \(e^{2\pi i/n}\), to increasing finite norm-dense predual tests and tolerances tending to zero. Fourier diagonalization of its clock action gives central projection partitions \(f_{0,k},\ldots,f_{n-1,k}\) and unitaries \(w_k\to1\) strongly-star such that
\[
\beta_k=\operatorname{Ad}w_k\circ\beta,\qquad
\beta_k(f_{j,k})=f_{j+1,k}.
\tag{5.2}
\]
Each partition comes from a unital \(M_n\), so its projections are pairwise equivalent at every coordinate. Moreover
\[
\rho(f_{j,k})\longrightarrow1/n.
\tag{5.3}
\]
To see (5.3), the matrix units are central in predual norm. Testing the commutator of the two opposite matrix entries makes the masses of any two diagonal projections asymptotically equal. Their sum is \(1\). The same reasoning applies after the fixed Fourier change of matrix units.

Centrality gives \(u^*f_{j,k}u-f_{j,k}\to0\) strongly-star. The finite-partition conclusion of Lemma 1.0 in the finite-model lesson applies: each \(u^*f_{j,k}u\) is equivalent to \(f_{j,k}\), with no finiteness assumption on \(M\). It supplies \(b_k\to1\) strongly-star such that
\[
b_k(u^*f_{j,k}u)b_k^*=f_{j,k}.
\]
Set \(a_k=b_ku^*\). Then \(a_k\) commutes with every \(f_{j,k}\) and \(a_k-u^*\to0\) strongly-star.

Define partial unitaries recursively by
\[
\begin{gathered}
v_{0,k}=f_{0,k},\\
v_{j+1,k}=\beta_k^{-1}(a_kv_{j,k})\\
(0\leq j<n-1).
\end{gathered}\tag{5.4}
\]
Both supports of \(v_{j,k}\) are \(f_{-j,k}\). Thus \(V_k=\sum_{j=0}^{n-1}v_{j,k}\) is unitary and commutes with the partition. For \(j<n-1\), (5.4) says \(\beta_k(v_{j+1,k})=a_kv_{j,k}\). All these terms cancel in
\[
\beta_k(V_k)-a_kV_k.
\]
The remaining two terms both have left and right support \(f_{1,k}\). Consequently the unitary
\[
d_k=V_k^*a_k^*\beta_k(V_k)
\tag{5.5}
\]
equals \(1\) on \(1-f_{1,k}\), and
\[
\|d_k-1\|_\rho^\sharp
\leq2\sqrt{2\rho(f_{1,k})}.
\tag{5.6}
\]

We must justify replacing \(a_k^*\) by \(u\), and \(\beta_k(V_k)\) by \(\beta(V_k)\), although \(V_k\) varies. An arbitrary bounded sequence would not justify this replacement.

Let \(I\) be the bounded sequences tending strongly-star to zero, and let \(D\) be the bounded sequences that multiply \(I\) into itself on both sides. Then \(D\) is a unital norm-closed star algebra, \(I\subset D\) is a two-sided ideal there, and constant sequences lie in \(D\). A strongly central bounded sequence also lies in \(D\). For completeness, if \(z_k\) is central, \(\|z_k\|\leq C\), \(r_k\in I\), and \(\|r_k\|\leq L\), then
\[
\begin{aligned}
&\rho(z_k^*r_k^*r_kz_k)\\
&\leq C L^2\|[z_k^*,\rho]\|\\
&\quad+\bigl|\rho(r_k^*r_kz_kz_k^*)\bigr|\\
&\leq C L^2\|[z_k^*,\rho]\|\\
&\quad+L C^2\rho(1)^{1/2}\|r_k\|_\rho\longrightarrow0.
\end{aligned}\tag{5.7}
\]
The first line moves the left \(z_k^*\) across \(\rho\); the second is Cauchy–Schwarz. The adjoint seminorm of \(r_kz_k\) is bounded directly by \(C\|r_k^*\|_\rho\). Applying the same reasoning to adjoints proves the assertion for \(z_kr_k\). These estimates hold for every positive normal \(\rho\). This proves the central-sequence assertion. Products of two bounded strong-star null sequences are null, so \(I\subset D\); the remaining algebra properties follow from its definition.

The fixed normal automorphism \(\beta\) preserves \(I\) and \(D\). Since \(w_k-1,b_k-1\in I\), their classes in \(D/I\) equal \(1\). All \(f_{j,k}\) belong to \(D\) by centrality, and \(a_k\in D\) with class \(u^*\). The coordinatewise maps \(\beta_k=\operatorname{Ad}w_k\circ\beta\) and their inverses \(\beta^{-1}\circ\operatorname{Ad}w_k^*\) preserve \(D\) and \(I\). On \(D/I\) they induce \(\beta\) and \(\beta^{-1}\), respectively. The recursion (5.4) therefore shows \(v_{j,k}\in D\) and \(V_k\in D\). In that quotient, (5.5) and \(V_k^*u\beta(V_k)\) have the same class. Hence
\[
V_k^*u\beta(V_k)-d_k\longrightarrow0
\quad\text{strongly-star}.
\tag{5.8}
\]
This argument supplies the moving-multiplier control missing from a purely pointwise cancellation.

By (5.3), (5.6) and (5.8),
\[
\limsup_k\|V_k^*u\beta(V_k)-1\|_\rho^\sharp
\leq2\sqrt{2/n}.
\]
Choose \(n\) with \(2\sqrt{2/n}<\varepsilon\), then a sufficiently large \(k\), and set \(x=V_k^*\). This proves (5.1). \(\square\)

**Example 5.2.** If \(\beta=\mathrm{id}\) and \(u=-1\), then \(xu\beta(x^*)=-1\) for every \(x\), and its sharp state distance from \(1\) is \(2\sqrt2\). Thus the central aperiodicity hypothesis in Lemma 5.1 cannot be dropped.

## 6. A single small perturbation in the original state

We finish Theorem 1.1. Start with (1.2), and set
\[
\beta=\sigma\circ\theta_1\circ\sigma^{-1},\qquad
\rho=\varphi\circ\sigma^{-1}.
\tag{6.1}
\]
These are fixed before applying Lemma 5.1. The lemma gives \(x\in\mathcal U(M)\) with
\[
c=xu\beta(x^*),\qquad \|c-1\|_\rho^\sharp<\varepsilon.
\tag{6.2}
\]
Conjugating \(\theta_2=\operatorname{Ad}u\circ\beta\) by \(\operatorname{Ad}x\) gives
\[
\operatorname{Ad}x\circ\theta_2\circ\operatorname{Ad}(x^*)
=\operatorname{Ad}c\circ\beta.
\tag{6.3}
\]
Define
\[
w=\sigma^{-1}(c),\qquad
\gamma=\operatorname{Ad}(x^*)\circ\sigma.
\tag{6.4}
\]
The automorphism \(\gamma\) is approximately inner, and direct substitution in (6.3) yields
\[
\theta_2=\gamma\circ\operatorname{Ad}w\circ\theta_1\circ\gamma^{-1}.
\]
By the fixed choice of \(\rho\),
\[
\|w-1\|_\varphi^\sharp=\|c-1\|_{\varphi\circ\sigma^{-1}}^\sharp<\varepsilon.
\]
This proves (1.3). The state used by Lemma 5.1 depends on the already chosen \(\sigma\), and not on the subsequently chosen \(x\). That order is what makes the estimate in the original state valid. \(\square\)

## 7. Aperiodic automorphisms of the hyperfinite II₁ factor

The specialization to \(R\) uses two exact programme results. Every automorphism of \(R\) is approximately inner, by Theorem 6.3 of the hyperfinite finite-factor prerequisite. Its proof exactly implements an automorphism on each finite dyadic head, obtains pointwise \(L^2\) convergence by conditional expectations, and then proves convergence on the predual using the inverse automorphisms and bounded trace densities. Also
\[
\operatorname{Cnt}R=\operatorname{Inn}R,
\tag{7.1}
\]
by Theorem 4.2 of the central-triviality prerequisite. Its preceding Lemma 4.1 proves the uniform displacement criterion: an automorphism of a II₁ factor moving every unitary of a finite-head commutant by less than \(1\) in \(L^2\) is inner. The proof constructs a nonzero bounded convex-hull intertwiner, exactly removes the finite matrix action, and extracts an implementing unitary from a nonzero matrix coefficient. For an outer automorphism of \(R\), the contrapositive supplies unitaries in successive dyadic-head commutants with displacement at least \(1/2\). They form an ordinary central sequence, proving (7.1). This is the direct proof used here, at the precise finite-factor hypotheses; it supplies no equality of ordinary and asymptotic periods on an arbitrary factor.

**Corollary 7.1.** If \(\theta_1,\theta_2\in\operatorname{Aut}R\) have no nonzero inner powers, they are outer conjugate. For every \(\delta>0\), there are \(w\in\mathcal U(R)\) and \(\gamma\in\operatorname{Aut}R\) such that
\[
\begin{gathered}
\|w-1\|_2<\delta,\\
\theta_2=\gamma\circ\operatorname{Ad}w\circ\theta_1\circ\gamma^{-1}.
\end{gathered}\tag{7.2}
\]

*Proof.* Equation (7.1) shows that no nonzero power is centrally trivial, so both asymptotic periods are zero. Both automorphisms are approximately inner, and \(R\) is strongly stable with separable predual. Apply Theorem 1.1 with its trace state and \(\varepsilon=\sqrt2\delta\). Since \(\|z\|_\tau^\sharp=\sqrt2\|z\|_2\), (1.3) gives (7.2). \(\square\)

For instance, the product action \(\alpha\) of (3.2) is a representative of this unique outer-conjugacy class. Every nonzero power is outer by Lemma 3.3.

## 8. Exercises with solutions

**Exercise 8.1 (introductory: a product budget).** For \(n_v=2^{v+6}\), calculate the bound in (3.4).

*Solution.* The sum is \(2^{-6}=1/64\), so (3.4) gives \(\|W-1\|_\varphi^\sharp\leq1/8\). To obtain a strict bound below \(1/8\) from this estimate alone, increase the exponent.

**Exercise 8.2 (intermediate: the growing-size trap).** In \(M_n\) with normalized trace and clock diagonal \(\operatorname{diag}(1,\zeta_n,\ldots,\zeta_n^{n-1})\), compute the \(L^2\) displacement of \(e_{01}\) under the \(q\)-th power. Why does it fail to prove Lemma 3.3 when \(n\to\infty\)?

*Solution.* The entry has norm \(n^{-1/2}\) and eigenvalue \(\zeta_n^{-q}\), so the displacement is \(|\zeta_n^{-q}-1|/\sqrt n\). For fixed \(q\), both the phase displacement and the norm tend to zero. Lemma 3.3 instead uses a norm-one Weyl unitary at frequency approximately \(n/(2|q|)\); its phase displacement tends to \(2\).

**Exercise 8.3 (intermediate: why the first test may wait).** In (3.7), centrality of \(U_v\) is required only for \(j<v\). Verify that this still gives the summable tensor-splitting estimate for every \(\psi_j\).

*Solution.* For fixed \(j\), every stage \(v>j\) meets both cycle and partition centrality tests. Its averaging error is at most \(2^{-v}\), by (3.15). The stages \(v\leq j\) are finite in number, and each error is at most \(2\|\psi_j\|\). Thus their sum and the geometric tail are finite.

**Exercise 8.4 (advanced: check the ordinary seam).** In (5.4), determine the two uncancelled summands in \(\beta_k(V_k)-a_kV_k\), and verify their common support.

*Solution.* The summands are \(\beta_k(v_{0,k})\) and \(-a_kv_{n-1,k}\). The first has both supports \(\beta_k(f_{0,k})=f_{1,k}\). The second has both supports \(f_{-(n-1),k}=f_{1,k}\), since \(a_k\) commutes with the partition. All other summands cancel by the recursion. Multiplication by the block diagonal unitaries \(V_k^*\) and \(a_k^*\) preserves this support, giving (5.6).

**Exercise 8.5 (advanced: transport the state).** Suppose \(\theta_2=\operatorname{Ad}u\circ\sigma\circ\theta_1\circ\sigma^{-1}\), and \(c=xu\beta(x^*)\) with \(\beta=\sigma\theta_1\sigma^{-1}\). Find the state in which \(c\) must be small so that \(w=\sigma^{-1}(c)\) is small in a prescribed state \(\varphi\). Check the resulting conjugator.

*Solution.* Use \(\rho=\varphi\circ\sigma^{-1}\). Then \(\|w-1\|_\varphi^\sharp=\|c-1\|_\rho^\sharp\). The conjugator is \(\gamma=\operatorname{Ad}(x^*)\circ\sigma\). Its inverse is \(\sigma^{-1}\circ\operatorname{Ad}x\), and substitution gives
\[
\begin{aligned}
&\gamma\circ\operatorname{Ad}w\circ\theta_1\circ\gamma^{-1}\\
&=\operatorname{Ad}(x^*)\circ\operatorname{Ad}c\circ\beta\circ\operatorname{Ad}x\\
&=\theta_2.
\end{aligned}
\]

**Exercise 8.6 (advanced: why multiplier control is necessary).** On \(\ell^2(\mathbb N)\), let \(p_k\) project onto the \(k\)-th basis vector and let \(z_k\) interchange the first and \(k\)-th basis vectors. Show \(p_k\to0\) strongly-star but \(p_kz_k\) does not. Relate this to (5.8).

*Solution.* For every vector, its \(k\)-th coordinate tends to zero, so \(p_k\to0\) strongly; the projections are self-adjoint. But \(p_kz_ke_1=e_k\), which has norm \(1\). Thus bounded moving right factors can destroy strong convergence to zero. In (5.8), the explicitly constructed \(V_k\) lie in the multiplier algebra \(D\), which is exactly the additional property that excludes this failure.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Section III contains the cyclic induction and aperiodic classification theorem; Sections I–II supply lifting and centralizer cohomology. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. The multiplier algebra viewpoint and the modern asymptotic-centralizer correspondence clarify which varying sequences preserve the null ideal. [Open author version, v3](https://arxiv.org/abs/1212.5457v3).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003. Theorem XVII.3.1, printed page 270 and proof on pages 281–282; Lemma XVII.3.9 and its proof, pages 279–281; Corollary XVII.3.10, page 282. The source retains a strongly stable factor with separable predual, approximately inner input automorphisms and an approximately inner outer-conjugacy map. Theorem 1.1 here also writes out the state transport needed for its single arbitrarily small perturbation. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).

For the hyperfinite central-triviality input, [Connes periodic], Lemma 3.4 and Theorem 3.2(1) are the source of the displacement criterion and displaced central sequences. The exact internal proofs used in Section 7 are those specified in the introduction. In Section 5 the ordinary null-sequence multiplier argument is proved in full; the ultrafilter construction in [Ando–Haagerup], Section 3.1, supplies context and is not substituted for that ordinary-limit proof.

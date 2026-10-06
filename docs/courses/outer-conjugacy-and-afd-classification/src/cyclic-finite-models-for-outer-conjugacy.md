# Cyclic finite models for outer conjugacy

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Spot-checked by GPT-6 Astra (OpenAI) in a separate session. Original text is public domain (CC0).*

## Introduction

To compare two automorphisms, we first arrange that each acts on a finite matrix algebra by the same cyclic shift. Approximate innerness gives a unitary that nearly implements the action; a tower gives an exact cycle of projections. Two repairs reconcile those pieces: a small unitary makes the implementer cycle the projections exactly, and a Borel root removes its residual full-period unitary.

The second repair has a subtlety. The chosen root is discontinuous at a spectral cut. Almost invariance of a unitary under an automorphism does not, by itself, justify applying that discontinuous function. We first rotate the scalar phase so that the spectral measure near the cut is uniformly small, then prove the required continuity estimate.

The finite-model construction follows [Connes], Lemmas 3.1.2–3.1.4; the iteration estimates also use Lemmas 3.2.2, 3.2.3 and 3.2.6. [Connes periodic] provides later classification context. The local treatment writes out the general close-projection completion, uses a Fubini–Markov choice of spectral cut, and retains five worked exercises. Prerequisites are [Almost invariant inner implementers](almost-invariant-inner-implementers.md) and [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md), including the stated strong stability and exact lifting results. Throughout, \(M\) is a strongly stable factor with separable predual, \(\theta\) is approximately inner with \(p_a(\theta)=0\), and \(\varphi\) is a faithful normal state. We write \(\|x\|_\varphi^\sharp=(\varphi(x^*x)+\varphi(xx^*))^{1/2}\).

## 1. Repairing an approximately cyclic implementer

**Lemma 1.0 (close equivalent projections in a general factor).** Let \(P\) be a factor with separable predual, and let \(p_k,q_k\in P\) be projections such that
\[
\begin{gathered}p_k\sim q_k,\\ p_k-q_k\longrightarrow0\quad\text{strongly-star}.\end{gathered}
\]
There are partial isometries \(v_k\in P\) such that
\[
\begin{gathered}v_k^*v_k=p_k,\qquad v_kv_k^*=q_k,\\v_k-q_k\longrightarrow0\quad\text{strongly-star}.\end{gathered}\tag{PC1}
\]
Neither projection sequence is assumed centralizing. The factor may be finite, semifinite infinite, or type III.

*Proof.* Fix a faithful normal state \(\rho\) on \(P\), and write
\(\|x\|_\rho^\sharp{}^2=\rho(x^*x)+\rho(xx^*)\).
On bounded sets this seminorm detects strong* convergence. Indeed, in the faithful state GNS representation the state vector \(\Omega\) is separating and \(P'\Omega\) is dense. If a bounded sequence and its adjoint tend to zero on \(\Omega\), commuting with each fixed operator in \(P'\) gives convergence on that dense set, hence on every vector.

We use the projection comparison, splitting and finite-sum facts proved in [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md), Section 2, NP1–NP6 and the full-corner-center argument, and Section 9, (K1). In a factor every infinite projection is properly infinite, and in a countably decomposable factor any two infinite projections are equivalent. The first assertion follows from the finite/properly infinite central decomposition in the projection corner, whose center is scalar; the second follows from (K1). These assertions concern infinite projections, not all nonzero projections of an infinite factor.

For the first estimates fix \(k\) and suppress the index. Set
\[
\begin{gathered}D=(p-q)^2,\qquad x=qp,\\h=x^*x=pqp.\end{gathered}
\]
The positive operator \(D=p+q-pq-qp\) commutes with both \(p\) and \(q\). Therefore
\[
\begin{aligned}p-h&=pD\le D,\\q-xx^*&=qD\le D,\\(x-q)^*(x-q)&=(1-p)D\le D,\\(x-q)(x-q)^*&=qD\le D.\end{aligned}\tag{PC2}
\]
For example, \((1-p)D=(1-p)q(1-p)\). These positive-operator inequalities control both seminorms even though \(p\) and \(q\) vary with \(k\).

Write \(x=w^0h^{1/2}\) for its polar decomposition and put
\[
\begin{gathered}a=\mathbf1_{[1/2,1]}(h),\\w=w^0a,\qquad c=ww^*.\end{gathered}
\]
Thus \(w^*w=a\le p\), \(c\le q\), and
\(c=\mathbf1_{[1/2,1]}(xx^*)\). Spectral calculus in the respective corners gives
\[
\begin{aligned}p-a&\le2(p-h),\\q-c&\le2(q-xx^*),\\(w-x)^*(w-x)&\le2(p-h),\\(w-x)(w-x)^*&\le2(q-xx^*).\end{aligned}\tag{PC3}
\]
For the first line, use
\(1-\mathbf1_{[1/2,1]}(t)\le2(1-t)\) for \(0\le t\le1\).
For the second, use
\((\mathbf1_{[1/2,1]}(t)-\sqrt t)^2\le2(1-t)\).
These inequalities include \(t=0,1/2,1\); on the kernel of the polar part the squared error is zero. Applying \(\rho\) to (PC2)–(PC3), and restoring indices, shows that
\[
\begin{gathered}x_k-q_k,\quad w_k-x_k,\\p_k-a_k,\quad q_k-c_k\\\longrightarrow0\quad\text{strongly-star}.\end{gathered}\tag{PC4}
\]

We next arrange that the two residual projections are equivalent. This is a coordinatewise construction, so the following cases may vary with \(k\).

If \(a_k\) is finite and \(p_k,q_k\) are finite, factor comparison compares \(p_k-a_k\) and \(q_k-c_k\). Suppose first that a partial isometry \(s\) embeds the former into the latter. Then \(w_k+s\) has initial projection \(p_k\) and final projection \(c_k+ss^*\le q_k\). Because \(p_k\sim q_k\) and \(q_k\) is finite, this final projection must be \(q_k\). Thus \(p_k-a_k\sim q_k-c_k\). If comparison has the reverse orientation, apply the same argument with initial and final projections interchanged. This proves the finite cancellation used here.

If \(a_k\) is finite and \(p_k,q_k\) are infinite, both residuals are infinite. Otherwise one of these endpoints would be a sum of two finite orthogonal projections, hence finite by NP6. The residuals are therefore equivalent by (K1). In both finite-\(a_k\) cases set \(r_k=0\).

If \(a_k\) is infinite, split it into countably many orthogonal infinite projections \((a_{k,m})_{m\ge1}\) as in NP5. The final projections \(w_ka_{k,m}w_k^*\) are also orthogonal, and normality gives
\[
\begin{gathered}\sum_{m\ge1}\bigl[\rho(a_{k,m})+\rho(w_ka_{k,m}w_k^*)\bigr]\\\le\rho(a_k)+\rho(c_k)\le2.\end{gathered}
\]
Choose one summand \(r_k=a_{k,m(k)}\) for which
\[
\rho(r_k)+\rho(w_kr_kw_k^*)<k^{-2}.
\tag{PC5}
\]
Both \(r_k\) and \(a_k-r_k\) are infinite, since the latter contains another infinite summand. Define in all cases
\[
\begin{gathered}a_k'=a_k-r_k,\\w_k'=w_k(a_k-r_k),\\c_k'=c_k-w_kr_kw_k^*.\end{gathered}
\]
Then \(w_k'^*w_k'=a_k'\) and \(w_k'w_k'^*=c_k'\). In the infinite-\(a_k\) case, \(p_k-a_k'\) contains \(r_k\), while \(q_k-c_k'\) contains the equivalent infinite projection \(w_kr_kw_k^*\). They are infinite and thus equivalent. In the finite-\(a_k\) cases their equivalence was already proved.

Choose a partial isometry \(s_k\) with initial projection \(p_k-a_k'\) and final projection \(q_k-c_k'\). The initial projections of \(w_k'\) and \(s_k\) are orthogonal, as are their final projections. Consequently
\[
v_k=w_k'+s_k
\]
has exactly the two endpoints in (PC1).

To check closeness on both sides, put \(\delta_k=\rho((p_k-q_k)^2)\to0\). Equations (PC2)–(PC5) give
\[
\begin{aligned}\|x_k-q_k\|_\rho^\sharp{}^2&\le2\delta_k,\\\|w_k-x_k\|_\rho^\sharp{}^2&\le4\delta_k,\\\|w_k'-w_k\|_\rho^\sharp{}^2&=\rho(r_k)+\rho(w_kr_kw_k^*)\\&\le k^{-2},\\\|s_k\|_\rho^\sharp{}^2&=\rho(p_k-a_k')+\rho(q_k-c_k')\\&\le4\delta_k+k^{-2}.\end{aligned}\tag{PC6}
\]
In the finite cases the third expression is zero. The triangle inequality now gives, for all \(k\ge1\),
\[
\|v_k-q_k\|_\rho^\sharp
\le(4+\sqrt2)\sqrt{\delta_k}+2/k\longrightarrow0.
\]
The sequence is bounded, so the faithful-state criterion proves (PC1). If \(p_k=q_k=0\), the construction is interpreted as \(v_k=0\). \(\square\)

**Corollary 1.0.1 (matching finite partitions).** Let \(m\ge1\) be fixed, and for every \(k\) let \((p_{j,k})_{j=1}^m\) and \((q_{j,k})_{j=1}^m\) be orthogonal projection partitions of \(1\) in a separable-predual factor. Suppose, for each \(j\), that
\[
\begin{gathered}p_{j,k}\sim q_{j,k}\quad\text{for every }k,\\p_{j,k}-q_{j,k}\longrightarrow0\quad\text{strongly-star}.\end{gathered}
\]
There are unitaries \(b_k\to1\) strongly-star with
\(b_kp_{j,k}b_k^*=q_{j,k}\) for all \(j,k\).

*Proof.* Apply Lemma 1.0 separately to each fixed \(j\), obtaining \(v_{j,k}\), and set \(b_k=\sum_{j=1}^m v_{j,k}\). Since \(v_{j,k}=q_{j,k}v_{j,k}p_{j,k}\), orthogonality gives
\[
\begin{gathered}v_{i,k}^*v_{j,k}=v_{i,k}v_{j,k}^*=0\quad(i\ne j),\\b_k^*b_k=b_kb_k^*=1.\end{gathered}
\]
Moreover \(b_kp_{j,k}=v_{j,k}\), so its conjugation sends \(p_{j,k}\) to \(q_{j,k}\). Finally
\(b_k-1=\sum_{j=1}^m(v_{j,k}-q_{j,k})\to0\) strongly-star, because the sum has fixed finite length. Zero partition cells cause no exception: equivalence then makes both corresponding cells zero. \(\square\)

The general close-projection comparison is due to [Connes], Lemma 1.1.4, printed pp. 388–389. The proof above writes out the factor case needed here, with both state seminorms and the small infinite residual retained. Its cutoff and completion also appear in Central sequence algebras and exact lifts, Theorem 5.1. That theorem concerns centralizing sequences; (PC2)–(PC6) prove the present statement without that additional hypothesis.

**Proposition 1.1 (a common cycle for the automorphism and implementer).** Fix \(n\geq1\), a finite family \(\psi_1,\ldots,\psi_q\in M_*\), an integer \(k\geq1\), and \(\varepsilon>0\). There are equivalent projection partitions \(F_0,\ldots,F_{n-1}\), unitaries \(w,u\), and \(\theta'=\operatorname{Ad}w\circ\theta\), such that
\[
\begin{aligned}
&\|[F_j,\psi_l]\|<\varepsilon,\\
&\theta'(F_j)=uF_ju^*=F_{j+1},\\
&\|\psi_l\circ\theta^{-1}-\psi_l\circ\operatorname{Ad}(u^*)\|<\varepsilon,\\
&\|\varphi\circ\theta'-\varphi\circ\operatorname{Ad}u\|<\varepsilon,\\
&\|\theta'(u^r)-u^r\|_\varphi^\sharp<\varepsilon\quad(|r|\leq k),\\
&\|w-1\|_\varphi^\sharp<\varepsilon.
\end{aligned}
\tag{1.1}
\]
Indices on the partition are read modulo \(n\). The power-invariance and forward-predual tolerances can be made arbitrarily small while retaining the same \(w\) and partition.

*Proof.* If \(n=1\), take \(F_0=1\), \(w=1\), and use the almost invariant implementer theorem directly. Suppose \(n\geq2\). Choose \(w\) as small as needed that \(\theta'=\operatorname{Ad}w\circ\theta\) differs from \(\theta\) by less than \(\varepsilon/2\) on the listed inverse-predual tests. Continuity of unitary conjugation permits this. Corollary 6.2 of the absorption lesson gives a tensor decomposition in which \(\theta'=\sigma_0\otimes\beta\), with \(w\) inside that chosen neighborhood.

The model \(\sigma_0\) has infinitely many coordinates of size \(n\), each acting by the clock diagonal \(c_n\). In such a coordinate take the projections onto a Fourier basis \(\xi_j\) with \(c_n\xi_j=\xi_{j+1}\). They are equivalent rank-one projections, sum to \(1\), and rotate exactly under the model. Far enough along the size-\(n\) coordinates, their embeddings in \(M\) commute with the listed normal functionals within \(\varepsilon\). This follows first for product functionals and finite-coordinate functionals on the tracial factor, then for all normal functionals by norm density. Fix one such partition \((F_j)\).

Inner perturbation preserves approximate innerness and asymptotic period. The almost invariant implementer theorem therefore gives unitaries \(a_s\) with
\[
\begin{gathered}\operatorname{Ad}a_s\to\theta',\\\theta'(a_s^r)-a_s^r\to0\quad\text{strongly-star}\\\text{for every fixed }r.\end{gathered}\tag{1.2}
\]
In particular \(a_sF_ja_s^*-F_{j+1}\to0\) strongly-star. The two partitions have equivalent corresponding projections. Corollary 1.0.1 gives \(b_s\to1\) strongly-star for which
\[
b_sa_sF_ja_s^*b_s^*=F_{j+1}.
\]
Put \(u_s=b_sa_s\). Its conjugations still tend to \(\theta'\) in the \(u\)-topology. The moving-multiplier lemma from the implementer lesson, applied to \(b_s-1\), gives \(u_s-a_s\to0\) strongly-star. Telescoping a fixed power, with the same predual transport control, gives \(u_s^r-a_s^r\to0\) strongly-star for every fixed integer \(r\). Normality of \(\theta'\) and (1.2) yield
\[
\theta'(u_s^r)-u_s^r\to0\text{ strongly-star}.
\tag{1.3}
\]
The inverse-predual tests tend to those of \(\theta'\), which were chosen within \(\varepsilon/2\) of \(\theta\); the forward test tends to zero. Choose a sufficiently large \(s\) to satisfy every test in (1.1). Equations (1.2)–(1.3) also prove the last assertion: keep \(w,F_j\) fixed and continue along \((u_s)\). \(\square\)

## 2. Choosing a spectral cut with small measure

Parametrize \(\mathbb T\) by angles modulo \(2\pi\). For \(q\geq3\), let \(J(z,q)\) be the closed arc centered at \(z\) with angular radius \(2\pi4^{-q}\). If \(\mu\) is a probability measure on the circle, put
\[
\begin{aligned}A(\mu)=\{z\in\mathbb T:{}&\mu(J(z,q))\leq2^{-q}\\&\text{for every }q\geq3\}.\end{aligned}\tag{2.1}
\]

**Lemma 2.1 (a good cut exists).** The set \(A(\mu)\) has normalized Haar measure at least \(1/2\). In particular it is nonempty, for every probability measure \(\mu\), including purely atomic ones.

*Proof.* The Haar measure of each arc is \(2\cdot4^{-q}\). Fubini's theorem gives
\[
\int_{\mathbb T}\mu(J(z,q))\,dm(z)=2\cdot4^{-q}.
\]
Markov's inequality bounds the measure of the set where \(\mu(J(z,q))>2^{-q}\) by \(2^{1-q}\). The union of these bad sets has measure at most
\[
\sum_{q=3}^\infty2^{1-q}=1/2.
\]
Its complement is (2.1). \(\square\)

For a unitary \(t\), let \(\mu_{\varphi,t}(B)=\varphi(1_B(t))\). If \(z\in A(\mu_{\varphi,t})\) and a scalar \(\rho\) satisfies \(\rho z=-1\), then \(-1\in A(\mu_{\varphi,\rho t})\). With \(t=u^n\), choose an \(n\)-th root \(\lambda\) of \(\rho\) and replace \(u\) by \(\lambda u\). This phase change preserves its inner automorphism and every projection-cycle relation, and gives
\[
\varphi(1_{J(-1,q)}(u^n))\leq2^{-q}\quad(q\geq3).
\tag{2.2}
\]
It also leaves the magnitudes of all power-invariance errors unchanged.

## 3. A discontinuous root under control

Define the principal Borel \(n\)-th root by
\[
f_n(e^{it})=e^{it/n},\qquad -\pi<t\leq\pi.
\tag{3.1}
\]
Its discontinuity is at \(-1\). Given a unitary \(u\), set
\[
U=u f_n(u^n)^*.
\tag{3.2}
\]
All factors in (3.2) commute. Since \(f_n(z)^n=z\), we have \(U^n=1\).

**Lemma 3.1 (Borel normalization of almost invariant unitaries).** Let \(\alpha\in\operatorname{Aut}M\). Suppose unitaries \(u_s\) satisfy
\[
\begin{gathered}\operatorname{Ad}u_s\to\alpha,\\\alpha(u_s^r)-u_s^r\to0\quad\text{strongly-star}\\\text{for every fixed integer }r,\end{gathered}\tag{3.3}
\]
and (2.2) holds uniformly in \(s\). With \(U_s=u_s f_n(u_s^n)^*\), we have
\[
\begin{gathered}\alpha(U_s^r)-U_s^r\to0\quad\text{strongly-star}\\\text{for every fixed }r.\end{gathered}\tag{3.4}
\]
Moreover, if a bounded \(d_s\to0\) strongly-star, then \(d_sU_s^r\) and \(U_s^rd_s\) tend strongly-star to zero for every fixed \(r\).

*Proof.* For fixed \(r\), write \(h_r(z)=z^r\overline{f_n(z^n)}^{\,r}\); this is a bounded function of modulus \(1\), continuous off the preimage of the cut. For \(q\geq3\), extend its restriction outside the preimage of the interior of \(J(-1,q)\) continuously across the omitted arcs, with modulus at most \(1\). Approximate that extension uniformly by a Laurent polynomial \(g\), with error \(t>0\). Its norm is at most \(1+t\), and
\[
\|h_r(u_s)-g(u_s)\|_\varphi^\sharp{}^2
\leq2t^2+2(2+t)^2\,2^{-q}.
\tag{3.5}
\]
The bound follows by splitting the spectral integral into the good and omitted arcs, using (2.2).

For the functional \(\varphi\circ\alpha\), a direct bound is also available. The norm convergence
\[
\|\varphi\circ\alpha-\varphi\circ\operatorname{Ad}u_s\|\to0
\tag{3.6}
\]
and the fact that \(u_s\) commutes with its own spectral projections show that the omitted projection has \((\varphi\circ\alpha)\)-mass at most \(2^{-q}+o(1)\). Consequently the error in \(\alpha(h_r(u_s)-g(u_s))\) has the same limiting bound as (3.5). By (3.3), \(\alpha(g(u_s))-g(u_s)\to0\) strongly-star, since \(g\) has only finitely many fixed powers. The triangle inequality, followed first by \(s\to\infty\), then by \(t\to0\) and \(q\to\infty\), proves (3.4) in the faithful-state seminorm, and hence strongly-star on this bounded sequence.

For the moving-multiplier assertion, each \(d_su_s^j\to0\) strongly-star by the predual transport lemma and \(\operatorname{Ad}u_s\to\alpha\). Thus \(d_sg(u_s)\to0\). If \(\|d_s\|\leq C\), the remaining nonadjoint seminorm is bounded by
\[
\begin{gathered}\|d_s(h_r(u_s)-g(u_s))\|_\varphi\\\leq C\|h_r(u_s)-g(u_s)\|_\varphi.\end{gathered}
\]
For the adjoint seminorm of \(d_sh_r(u_s)\), left multiplication by the unitary \(h_r(u_s)^*\) gives the bound \(\|d_s^*\|_\varphi\to0\) directly. Apply the same reasoning with \(d_s^*\) and \(\overline{h_r}\) to obtain the assertion for \(h_r(u_s)d_s\). Let \(t\to0\) and \(q\to\infty\) as above. \(\square\)

In this proof the polynomial is chosen after the arc and tolerance, and before the sequence index. There is no assertion of uniform norm continuity of a discontinuous Borel function.

## 4. The exact cyclic matrix model

If \(uF_ju^*=F_{j+1}\), then \(u^n\) commutes with every \(F_j\), as does \(f_n(u^n)\). Hence \(U\) in (3.2) still rotates the partition. Define
\[
e_{ij}=U^iF_0U^{-j}\qquad(0\leq i,j<n).
\tag{4.1}
\]
Orthogonality of the partition gives \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), \(e_{ij}^*=e_{ji}\), and \(e_{jj}=F_j\). Since \(U^n=1\), the cyclic shift
\[
U=\sum_{j=0}^{n-1}e_{j+1,j}
\tag{4.2}
\]
belongs to the unital factor \(K\cong M_n(\mathbb C)\) generated by these units.

**Theorem 4.1 (a finite cyclic model with an exact action).** Given \(n\geq1\), finitely many \(\psi_l\in M_*\), and \(\varepsilon>0\), there are a partition \((F_j)\) and unitaries \(u,v\) such that:
\[
\begin{aligned}
&\|[F_j,\psi_l]\|<\varepsilon,\qquad uF_ju^*=F_{j+1},\\
&\|\psi_l\circ\theta^{-1}-\psi_l\circ\operatorname{Ad}(u^*)\|<\varepsilon,\\
&\varphi(1_{J(-1,q)}(u^n))\leq2^{-q}\quad(q\geq3),\\
&\operatorname{Ad}v\circ\theta(x)=UxU^*\quad(x\in K),\\
&\|v-1\|_\varphi^\sharp<\varepsilon,
\end{aligned}
\tag{4.3}
\]
where \(U=u f_n(u^n)^*\) and \(K=\{F_j,U:0\leq j<n\}''\cong M_n\).

*Proof.* For \(n=1\), take \(F_0=1\), choose an approximately inner implementer meeting the inverse-predual tests, and adjust its phase by Lemma 2.1. Then \(f_1(z)=z\), \(U=1\), \(K=\mathbb C1\), and \(v=1\) meet all conclusions. Suppose \(n\geq2\). In the construction of Proposition 1.1, first choose \(w\) inside a neighborhood so small that \(\|w-1\|_\varphi^\sharp<\varepsilon/2\), the inverse-predual difference from \(\theta\) is below \(\varepsilon/2\), and the extracted fixed partition meets its centrality tests. Retain \(\alpha=\operatorname{Ad}w\circ\theta\), this partition, and the full sequence \((u_s)\) of repaired implementers. It satisfies (3.3). At each coordinate adjust a scalar phase using Lemma 2.1 to impose (2.2); neither (3.3) nor the partition cycles change.

Normalize to \(U_s\) by (3.2), and let \(e_{ij,s}\) be (4.1). Lemma 3.1 yields \(\alpha(U_s^r)-U_s^r\to0\) strongly-star for every fixed \(r\). Since \(\alpha(F_0)=F_1=U_sF_0U_s^*\), it follows that
\[
\alpha(e_{ij,s})-U_se_{ij,s}U_s^*\to0\text{ strongly-star}.
\tag{4.4}
\]
For completeness, expand the difference using
\[
\begin{gathered}\alpha(e_{ij,s})=\alpha(U_s^i)F_1\alpha(U_s^{-j}),\\U_se_{ij,s}U_s^*=U_s^iF_1U_s^{-j}.\end{gathered}
\]
The resulting null differences may be multiplied on the right by powers of \(U_s\) by the last assertion of Lemma 3.1, and by the fixed \(F_1\) by normal strong-star continuity. Products of two bounded strong-star-null sequences are also null. This justifies (4.4) despite the varying unitaries.

Put \(t_{ij,s}=U_se_{ij,s}U_s^*\). The two systems \((t_{ij,s})\) and \((\alpha(e_{ij,s}))\) have the identical first diagonal \(F_1\). Hence
\[
b_s=\sum_{j=0}^{n-1}t_{j0,s}\alpha(e_{0j,s})
\tag{4.5}
\]
is unitary and satisfies \(b_s\alpha(e_{ij,s})b_s^*=t_{ij,s}\), by matrix multiplication. Subtract
\[
1=\sum_jt_{j0,s}t_{0j,s}
\]
from (4.5). Equation (4.4) and the moving-multiplier assertion of Lemma 3.1 show \(b_s-1\to0\) strongly-star: every \(t_{j0,s}\) is a fixed finite product of powers of \(U_s\) and the fixed \(F_0\), so these products preserve the required null sequences on either side.

Take \(v_s=b_sw\). Then \(\operatorname{Ad}v_s\circ\theta\) agrees exactly with \(\operatorname{Ad}U_s\) on the matrix algebra generated by \(e_{ij,s}\). Since \(w\) is fixed and \(b_s\to1\) strongly-star, \(\|v_s-w\|_\varphi^\sharp\to0\). Choose a large coordinate meeting the predual tolerances and \(\|v_s-w\|_\varphi^\sharp<\varepsilon/2\). All conclusions of (4.3) follow. \(\square\)

The approximate implementer in the predual test is \(u\). The normalized cyclic unitary \(U\) describes the action on \(K\). The root factor \(f_n(u^n)\) commutes with \(K\), so it can still carry an action on the complementary tensor factor. The theorem does not replace \(u\) by \(U\) in the predual approximation.

## 5. Predual controls for iteration

Three estimates let the finite construction be repeated inside successive matrix relative commutants.

**Lemma 5.1 (centrality of a normalized cycle).** Fix \(n\) and \(\delta>0\). There is \(\eta=\eta(n,\delta)>0\) such that, whenever \(u\) obeys (2.2) and \(0\leq\psi\leq\varphi\),
\[
\|[u,\psi]\|<\eta
\quad\Longrightarrow\quad
\|[u f_n(u^n)^*,\psi]\|<\delta.
\tag{5.1}
\]
The choice of \(\eta\) is independent of the algebra, state and dominated functional.

*Proof.* Put \(h(z)=z\overline{f_n(z^n)}\). As in Lemma 3.1, choose a Laurent polynomial \(g(z)=\sum_{j=-m}^m c_jz^j\), of norm at most \(2\), with error at most \(t\) away from the preimage of \(J(-1,q)\). Then
\[
\varphi(|h(u)-g(u)|^2)\leq t^2+9\cdot2^{-q}.
\tag{5.2}
\]
The difference is normal, because it is a function of \(u\). Cauchy–Schwarz on the two bimodule products gives
\[
\begin{aligned}&\|[h(u)-g(u),\psi]\|\\&\quad\leq2\psi(1)^{1/2}\psi(|h(u)-g(u)|^2)^{1/2}\\&\quad\leq2(t^2+9\cdot2^{-q})^{1/2}.\end{aligned}
\]
Choose \(q\) large and then \(t\) small so that this is below \(\delta/2\). Telescoping the commutator of each positive or negative power gives
\[
\begin{gathered}\|[g(u),\psi]\|\leq A\|[u,\psi]\|,\\A=\sum_{j=-m}^m |j|\,|c_j|.\end{gathered}
\]
Take \(\eta=\delta/(2(A+1))\). The triangle inequality proves (5.1). The polynomial and every choice made depend only on \(n,\delta\). \(\square\)

**Lemma 5.2 (from a cycle to a tensor expectation).** Let \(U^n=1\) and \(UF_jU^*=F_{j+1}\). If \(\|[U,\psi]\|\leq\delta\) and \(\|[F_j,\psi]\|\leq\delta\) for every \(j\), then for \(K=\{U,F_j\}''\),
\[
\|\psi-\psi\circ E_K\|\leq n^2(n+1)\delta.
\tag{5.3}
\]

*Proof.* The matrix units can also be written \(e_{ij}=U^{i-j}F_j\). Their commutators have norm at most \((|i-j|+1)\delta\leq(n+1)\delta\), by the power telescope and the product rule for bimodule commutators. Apply Lemma 4.1 of the absorption lesson. In particular \(\delta_v=2^{-v}/(n_v^2(n_v+1))\) makes the expectation errors summable along a sequence of such cycles. \(\square\)

**Lemma 5.3 (finite matrix coefficients).** If \(M=M_d(\mathbb C)\overline\otimes C\), write \(\omega_{ij}\) for the coordinate functionals dual to its standard matrix units. Every \(\psi\in M_*\) has a unique expansion
\[
\psi=\sum_{i,j=1}^d\omega_{ij}\otimes\psi_{ij},\qquad \psi_{ij}\in C_*.
\tag{5.4}
\]
For \(x\in C\), unitaries \(a\in M_d\), \(b\in C\) and \(\beta\in\operatorname{Aut}C\),
\[
\begin{gathered}\|[1\otimes x,\psi]\|\leq d^2\max_{i,j}\|[x,\psi_{ij}]\|,\\\begin{aligned}&\bigl\|\psi\circ(\operatorname{Ad}a\otimes\beta)\\&\qquad-\psi\circ\operatorname{Ad}(a\otimes b)\bigr\|\\&\quad\leq d^2\max_{i,j}\bigl\|\psi_{ij}\circ\beta\\&\qquad-\psi_{ij}\circ\operatorname{Ad}b\bigr\|.\end{aligned}\end{gathered}\tag{5.5}
\]

*Proof.* Define \(\psi_{ij}(y)=\psi(e_{ij}\otimes y)\). These functionals are normal. The finite matrix decomposition proves (5.4) and uniqueness. Each \(\omega_{ij}\) has norm \(1\). The commutator expansion is \(\sum_{i,j}\omega_{ij}\otimes[x,\psi_{ij}]\). The action difference is
\[
\sum_{i,j}(\omega_{ij}\circ\operatorname{Ad}a)\otimes
(\psi_{ij}\circ\beta-\psi_{ij}\circ\operatorname{Ad}b).
\]
Take norms, use \(\|\omega_{ij}\circ\operatorname{Ad}a\|=1\), and sum the \(d^2\) terms. \(\square\)

The root factor also satisfies
\[
\|f_n(u^n)^*-1\|\leq2\sin(\pi/(2n))\leq\pi/n.
\tag{5.6}
\]
Thus \(\sum_v1/n_v<\infty\) controls the accumulated norm cost of these factors. This bound does not supply centrality of the normalized cycles; that is the separate role of Lemma 5.1.

## 6. Examples and exercises with solutions

**Example 6.1 (normalization can move a unitary substantially).** On \(\mathbb C^n\), let \(S\) be the cyclic shift and \(u=e^{it}S\), with \(0<t<\pi/n\). Then \(u^n=e^{int}1\), \(f_n(u^n)=e^{it}1\), and \(U=S\). The operation removes the scalar phase exactly. It does not assert that \(\|u-U\|\) is arbitrarily small for a fixed \(t\).

**Exercise 6.2 (introductory: a full-period commutant).** If \(uF_ju^*=F_{j+1}\), prove \(u^n\) commutes with the partition, and explain why the root factor also does.

*Solution.* Iteration gives \(u^nF_ju^{-n}=F_j\). Each \(F_j\) therefore commutes with \(u^n\) and its adjoint, hence with every spectral projection and bounded Borel function of \(u^n\). In particular it commutes with \(f_n(u^n)\).

**Exercise 6.3 (intermediate: an atomic measure).** Let \(\mu\) be point mass at \(1\). Show \(-1\) belongs to \(A(\mu)\) and determine why it is advantageous as a root cut.

*Solution.* The arcs \(J(-1,q)\), \(q\geq3\), have radii at most \(2\pi/64<\pi\), so none contains \(1\). Their \(\mu\)-mass is zero, satisfying every bound. The root discontinuity then lies away from the entire spectrum with positive state mass; no spectral error is introduced there.

**Exercise 6.4 (intermediate: a Borel discontinuity really matters).** In \(\mathbb C\), let \(z_s=e^{i(\pi-1/s)}\) and \(z'_s=e^{i(-\pi+1/s)}\). Show \(|z_s-z'_s|\to0\) but \(|f_2(z_s)-f_2(z'_s)|\not\to0\).

*Solution.* Both original scalars tend to \(-1\). Their principal square roots tend to \(i\) and \(-i\), respectively, so the root difference tends to \(2\). Their spectral mass is concentrated at the cut; (2.2) is precisely the type of condition that prevents this behavior in the theorem.

**Exercise 6.5 (advanced: common-first-diagonal matrix alignment).** Suppose two unital matrix systems \((a_{ij})\), \((b_{ij})\), indexed from \(0\), have \(a_{00}=b_{00}\). Verify that \(v=\sum_ja_{j0}b_{0j}\) is unitary and that \(vb_{ij}v^*=a_{ij}\).

*Solution.* Using the common diagonal,
\[
\begin{aligned}vv^*&=\sum_{j,l}a_{j0}b_{0j}b_{l0}a_{0l}\\&=\sum_ja_{j0}b_{00}a_{0j}\\&=\sum_ja_{jj}=1.\end{aligned}
\]
The same computation gives \(v^*v=1\). Multiplying \(vb_{ij}v^*\) leaves only the terms with indices \(i,j\), giving \(a_{i0}b_{00}a_{0j}=a_{ij}\). This explains why (4.5) needs no separate projection comparison.

**Exercise 6.6 (advanced: the normalization's two roles).** In the tensor product \(M_n\overline\otimes C\), let \(u=S\otimes z\), where \(S\) is the cyclic shift and \(z\) is a unitary of \(C\) whose spectrum lies in the arc \(\{e^{it}:|t|<\pi/n\}\). Calculate \(U\) and compare the two inner automorphisms.

*Solution.* We have \(u^n=1\otimes z^n\), and the spectral-arc hypothesis gives \(f_n(z^n)=z\). Hence \(U=S\otimes1\). Both conjugations act by the same shift on \(M_n\otimes1\). On \(1\otimes C\), \(\operatorname{Ad}U\) is the identity while \(\operatorname{Ad}u\) is \(\operatorname{Ad}z\). They need not agree on the whole algebra.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Close-projection comparison: Lemma 1.1.4. Finite models and the Borel root: Lemmas 3.1.2–3.1.4. Iteration controls: Lemmas 3.2.2, 3.2.3 and 3.2.6. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).


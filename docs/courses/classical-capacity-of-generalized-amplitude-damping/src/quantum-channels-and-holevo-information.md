# Quantum channels and Holevo information

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A qubit in contact with an environment at a fixed temperature relaxes towards a stationary state: it loses and gains excitations, and its coherences decay. One use of such a qubit as a communication line is described by the *generalized amplitude-damping channel* \(\mathcal A_{\gamma,\nu}\), with damping strength \(\gamma\in[0,1]\) and stationary excited population \(\nu\in[0,1]\). This course proves the theorem of [OpenAI-GAD]: for all \(\gamma\) and \(\nu\), the Holevo information of \(n\) uses of the channel is \(n\) times the Holevo information of one use, and the latter is an explicit maximum over one variable. With the classical coding theorem, the classical capacity of the channel is its one-use Holevo information. The Holevo information, the minimum output entropy and the regularized Holevo information are moreover additive when the channel is used together with any finite-dimensional channel.

This lesson sets up the finite-dimensional framework and states the theorem.

- Channels and their Kraus representations (Theorem 1.2).
- Entropy: the diagonal bound and concavity (Proposition 2.1), subadditivity in a product basis (Corollary 2.2).
- Holevo information and minimum output entropy (Lemma 3.1).
- Codes, capacity and the coding theorem (Hypothesis (CT), Proposition 4.2).
- The generalized amplitude-damping channel and the theorem of the course (Theorem 5.3).

The lesson follows [OpenAI-GAD, Section 1]. The classical entropy inequalities and the continuity of entropy are taken from the lesson [Operator convex functions and the continuity of entropy](course:entropy-of-automorphisms/operator-convex-functions-and-the-continuity-of-entropy) (Proposition 4.1 and Theorem 7.1 there).

## 1. States and channels

All Hilbert spaces in this course are complex and finite dimensional. For such a space \(\mathcal H\), \(\mathcal B(\mathcal H)\) is the algebra of linear operators on \(\mathcal H\), and \(X^*\) is the adjoint of \(X\). We write \(P\ge0\) when \(P\) is positive semidefinite. A *state* is an operator \(\rho\ge0\) with \(\operatorname{Tr}\rho=1\). For a unit vector \(\psi\), the *pure state* \(\psi\psi^*\) is the orthogonal projection onto \(\mathbb C\psi\).

On \(\mathcal H_1\otimes\mathcal H_2\), the *partial trace* \(\operatorname{Tr}_1\colon\mathcal B(\mathcal H_1\otimes\mathcal H_2)\to\mathcal B(\mathcal H_2)\) is the linear map with \(\operatorname{Tr}_1(X_1\otimes X_2)=(\operatorname{Tr}X_1)X_2\), and \(\operatorname{Tr}_2\) is defined in the same way. For an orthonormal basis \((e_i)\) of \(\mathcal H_1\) and \(y\in\mathcal H_2\),
\[
\langle y,\operatorname{Tr}_1(X)\,y\rangle=\sum_i\langle e_i\otimes y,X(e_i\otimes y)\rangle ,
\]
as one checks on products \(X=X_1\otimes X_2\). Hence partial traces of states are states. For several factors, the *marginal* of a state on one factor is its partial trace over all the others.

A linear map \(\mathcal N\colon\mathcal B(\mathcal H_{\mathrm{in}})\to\mathcal B(\mathcal H_{\mathrm{out}})\) is *positive* if it maps positive semidefinite operators to positive semidefinite operators, and *completely positive* if \(\mathrm{id}_k\otimes\mathcal N\) is positive for every \(k\ge1\), where \(\mathrm{id}_k\) is the identity map of \(\mathcal B(\mathbb C^k)\). It is *trace preserving* if \(\operatorname{Tr}\mathcal N(X)=\operatorname{Tr}X\) for all \(X\). A *channel* is a completely positive trace-preserving map; it maps states to states.

**Lemma 1.1** (Kraus families give channels). Let \(V_1,\dots,V_r\colon\mathcal H_{\mathrm{in}}\to\mathcal H_{\mathrm{out}}\) be linear maps with \(\sum_\ell V_\ell^*V_\ell=I\). Then \(\mathcal N(X)=\sum_\ell V_\ell XV_\ell^*\) is a channel.

*Proof.* On products, and hence for all \(Y\), \((\mathrm{id}_k\otimes\mathcal N)(Y)=\sum_\ell(I\otimes V_\ell)Y(I\otimes V_\ell)^*\). This is positive semidefinite when \(Y\) is, because \(\langle w,ZYZ^*w\rangle=\langle Z^*w,YZ^*w\rangle\ge0\) for every operator \(Z\). Cyclicity of the trace gives \(\operatorname{Tr}\mathcal N(X)=\operatorname{Tr}\bigl(X\sum_\ell V_\ell^*V_\ell\bigr)=\operatorname{Tr}X\). \(\blacksquare\)

**Theorem 1.2** (Kraus representation). Every channel \(\mathcal N\colon\mathcal B(\mathcal H_{\mathrm{in}})\to\mathcal B(\mathcal H_{\mathrm{out}})\) has the form of Lemma 1.1, with at most \(\dim\mathcal H_{\mathrm{in}}\cdot\dim\mathcal H_{\mathrm{out}}\) operators \(V_\ell\).

*Proof.* Let \(e_1,\dots,e_m\) be an orthonormal basis of \(\mathcal H_{\mathrm{in}}\), and \(\Omega=\sum_ie_i\otimes e_i\in\mathcal H_{\mathrm{in}}\otimes\mathcal H_{\mathrm{in}}\). Identify the first factor with \(\mathbb C^m\). Complete positivity with \(k=m\) shows that the *Choi operator*
\[
\begin{aligned}
C&=(\mathrm{id}_m\otimes\mathcal N)(\Omega\Omega^*)\\
&=\sum_{i,j}e_ie_j^*\otimes\mathcal N(e_ie_j^*)
\end{aligned}
\]
is positive semidefinite. By the spectral theorem, \(C=\sum_{\ell=1}^rw_\ell w_\ell^*\) for vectors \(w_\ell\in\mathcal H_{\mathrm{in}}\otimes\mathcal H_{\mathrm{out}}\), with \(r\le m\dim\mathcal H_{\mathrm{out}}\). Each \(w_\ell\) is uniquely of the form \(\sum_ie_i\otimes x_{\ell i}\) with \(x_{\ell i}\in\mathcal H_{\mathrm{out}}\); let \(V_\ell\) be the linear map with \(V_\ell e_i=x_{\ell i}\). Since \(x_{\ell i}x_{\ell j}^*=V_\ell e_ie_j^*V_\ell^*\),
\[
C=\sum_{i,j}e_ie_j^*\otimes\sum_\ell V_\ell e_ie_j^*V_\ell^* .
\]
An operator \(\sum_{i,j}e_ie_j^*\otimes Y_{ij}\) determines its blocks \(Y_{ij}\), so \(\mathcal N(e_ie_j^*)=\sum_\ell V_\ell e_ie_j^*V_\ell^*\) for all \(i,j\), and by linearity \(\mathcal N(X)=\sum_\ell V_\ell XV_\ell^*\) for all \(X\). Trace preservation gives \(\operatorname{Tr}\bigl(X(\sum_\ell V_\ell^*V_\ell-I)\bigr)=0\) for all \(X\), hence \(\sum_\ell V_\ell^*V_\ell=I\). \(\blacksquare\)

For linear maps \(\mathcal N_i\colon\mathcal B(\mathcal H_i)\to\mathcal B(\mathcal K_i)\), the tensor product \(\mathcal N_1\otimes\mathcal N_2\) is the linear map that sends \(X_1\otimes X_2\) to \(\mathcal N_1(X_1)\otimes\mathcal N_2(X_2)\). If \((V_\ell)\) and \((W_m)\) are Kraus families of two channels, then, on products and hence everywhere,
\[
\begin{aligned}
&(\mathcal N_1\otimes\mathcal N_2)(X)\\
&\quad=\sum_{\ell,m}(V_\ell\otimes W_m)X(V_\ell\otimes W_m)^*,
\end{aligned}
\]
and \(\sum_{\ell,m}(V_\ell\otimes W_m)^*(V_\ell\otimes W_m)=I\). By Lemma 1.1, a tensor product of channels is a channel. In particular \(n\) independent uses of a channel \(\mathcal N\) form the channel \(\mathcal N^{\otimes n}\) on \(\mathcal B(\mathcal H_{\mathrm{in}}^{\otimes n})\).

**Lemma 1.3** (marginals of outputs). If \(\mathcal N_2\) is trace preserving, then \(\operatorname{Tr}_2\bigl((\mathcal N_1\otimes\mathcal N_2)(X)\bigr)=\mathcal N_1(\operatorname{Tr}_2X)\) for all \(X\). If \(\mathcal N_1\) is trace preserving, then \(\operatorname{Tr}_1\bigl((\mathcal N_1\otimes\mathcal N_2)(X)\bigr)=\mathcal N_2(\operatorname{Tr}_1X)\).

*Proof.* For \(X=X_1\otimes X_2\), both sides of the first identity equal \((\operatorname{Tr}X_2)\,\mathcal N_1(X_1)\), and both sides are linear in \(X\). The second identity is the same argument. \(\blacksquare\)

## 2. Entropy

For \(P\ge0\) let
\[
S(P)=-\operatorname{Tr}P\ln P=\sum_\lambda\eta(\lambda),
\]
the sum over the eigenvalues \(\lambda\) of \(P\) with multiplicity, where \(\eta(t)=-t\ln t\) and \(\eta(0)=0\). On states, \(S\) is the von Neumann entropy in nats. For a probability vector \(q=(q_1,\dots,q_m)\), \(H(q)=\sum_i\eta(q_i)\) is its Shannon entropy, and \(h(q)=\eta(q)+\eta(1-q)\) is the binary entropy. The following facts are read off from the eigenvalues.

1. \(S(P)\) depends only on the nonzero eigenvalues of \(P\). Hence \(S(UPU^*)=S(P)\) for every isometry \(U\), and \(S(XX^*)=S(X^*X)\) for every rectangular matrix \(X\).
2. \(S(P_1\oplus P_2)=S(P_1)+S(P_2)\).
3. \(S(cP)=cS(P)-c\ln c\,\operatorname{Tr}P\) for \(c>0\).
4. \(S(\rho_1\otimes\rho_2)=S(\rho_1)+S(\rho_2)\) for states, because the eigenvalues of \(\rho_1\otimes\rho_2\) are the products \(\lambda\mu\) of eigenvalues, and \(\eta(\lambda\mu)=\mu\,\eta(\lambda)+\lambda\,\eta(\mu)\).
5. A state on \(\mathbb C^2\) with determinant \(u\) has the eigenvalues \((1\pm\sqrt{1-4u})/2\), so its entropy is \(g(u)\), where, for \(0\le u\le\frac14\),
\[
g(u)=h\Bigl(\frac{1+\sqrt{1-4u}}2\Bigr).
\]
The function \(g\) is continuous, with \(g(0)=0\) and \(g(\frac14)=\ln2\). It is nondecreasing: as \(u\) increases, the argument of \(h\) decreases from \(1\) to \(\frac12\), and \(h\) is decreasing on \([\frac12,1]\).

On the states of a fixed space of dimension \(d\ge2\), \(S\) is continuous by the Fannes–Audenaert inequality \(|S(\rho)-S(\sigma)|\le T\ln(d-1)+h(T)\), \(T=\frac12\|\rho-\sigma\|_1\) ([Operator convex functions and the continuity of entropy](course:entropy-of-automorphisms/operator-convex-functions-and-the-continuity-of-entropy), Theorem 7.1).

**Proposition 2.1.** (1) (Diagonal bound.) If \(\rho\) is a state and \(f_1,\dots,f_m\) is an orthonormal basis, then \(S(\rho)\le H\bigl((\langle f_k,\rho f_k\rangle)_k\bigr)\). (2) (Concavity.) If \(\rho_1,\dots,\rho_N\) are states and \(w\) is a probability vector, then
\[
S\Bigl(\sum_iw_i\rho_i\Bigr)\ge\sum_iw_iS(\rho_i).
\]

*Proof.* (1) Let \(\rho=\sum_l\lambda_lg_lg_l^*\) with an orthonormal basis \((g_l)\). Then \(\langle f_k,\rho f_k\rangle=\sum_lD_{kl}\lambda_l\) with \(D_{kl}=|\langle f_k,g_l\rangle|^2\), and the rows and the columns of \(D\) sum to \(1\) because both bases are orthonormal. Concavity of \(\eta\) gives \(\eta(\sum_lD_{kl}\lambda_l)\ge\sum_lD_{kl}\eta(\lambda_l)\); summing over \(k\) and using the column sums gives \(H\ge S(\rho)\).

(2) Choose an orthonormal basis \((f_k)\) of eigenvectors of \(\bar\rho=\sum_iw_i\rho_i\). Concavity of \(\eta\) and then (1) give
\[
\begin{aligned}
S(\bar\rho)&=\sum_k\eta\Bigl(\sum_iw_i\langle f_k,\rho_if_k\rangle\Bigr)\\
&\ge\sum_iw_i\sum_k\eta(\langle f_k,\rho_if_k\rangle)\\
&\ge\sum_iw_iS(\rho_i) .\qquad\blacksquare
\end{aligned}
\]

**Corollary 2.2** (subadditivity in a product basis). Let \(\sigma\) be a state on \(\mathcal H_1\otimes\dots\otimes\mathcal H_n\) with marginals \(\sigma_j\) on \(\mathcal H_j\), and for each \(j\) let \((f^{(j)}_k)_k\) be an orthonormal basis of \(\mathcal H_j\). Then
\[
S(\sigma)\le\sum_{j=1}^nH\Bigl(\bigl(\langle f^{(j)}_k,\sigma_jf^{(j)}_k\rangle\bigr)_k\Bigr).
\]
When \((f^{(j)}_k)_k\) is an eigenbasis of \(\sigma_j\), the \(j\)-th term is \(S(\sigma_j)\).

*Proof.* By Proposition 2.1(1) in the product basis, \(S(\sigma)\) is at most the Shannon entropy of the probability distribution
\[
\begin{gathered}
P(k_1,\dots,k_n)=\langle F,\sigma F\rangle,\\
F=f^{(1)}_{k_1}\otimes\dots\otimes f^{(n)}_{k_n}.
\end{gathered}
\]
By the formula for partial traces in Section 1, the \(j\)-th marginal distribution of \(P\) is \(k\mapsto\langle f^{(j)}_k,\sigma_jf^{(j)}_k\rangle\). Subadditivity of Shannon entropy, \(H(U,V)\le H(U)+H(V)\) for random variables with finitely many values ([Operator convex functions and the continuity of entropy](course:entropy-of-automorphisms/operator-convex-functions-and-the-continuity-of-entropy), Proposition 4.1(3)), applied \(n-1\) times, gives the claim. \(\blacksquare\)

## 3. Holevo information and minimum output entropy

An *ensemble* on \(\mathcal H_{\mathrm{in}}\) is a finite family \(\{q_a,\rho_a\}\) of states \(\rho_a\) with probabilities \(q_a\ge0\), \(\sum_aq_a=1\). Its *Holevo quantity* for a channel \(\mathcal N\), in nats, is
\[
\begin{aligned}
\chi_{\mathcal N}\{q_a,\rho_a\}&=S\Bigl(\sum_aq_a\mathcal N(\rho_a)\Bigr)\\
&\quad-\sum_aq_aS\bigl(\mathcal N(\rho_a)\bigr).
\end{aligned}
\]
It is nonnegative by concavity, and at most \(\ln\dim\mathcal H_{\mathrm{out}}\), because \(0\le S(\rho)\le\ln\dim\) for states by Proposition 2.1(1). The *Holevo information* of \(\mathcal N\), in bits, is
\[
\chi(\mathcal N)=\frac1{\ln2}\sup\chi_{\mathcal N}\{q_a,\rho_a\},
\]
the supremum over all ensembles on \(\mathcal H_{\mathrm{in}}\). For a tensor product of channels, the states of an ensemble are arbitrary states on the whole input space; they may be entangled across the factors. The *minimum output entropy* of \(\mathcal N\), in nats, is
\[
S_{\min}(\mathcal N)=\min_\rho S(\mathcal N(\rho)),
\]
the minimum over the states of \(\mathcal H_{\mathrm{in}}\); it exists because the states form a compact set on which \(\rho\mapsto S(\mathcal N(\rho))\) is continuous.

**Lemma 3.1.** Let \(\mathcal N\), \(\mathcal N_1\) and \(\mathcal N_2\) be channels.

1. \(\chi(\mathcal N)\) is the supremum of the Holevo quantities of the ensembles of pure states.
2. Some pure state attains \(S_{\min}(\mathcal N)\).
3. For unitaries \(U\) on \(\mathcal H_{\mathrm{out}}\) and \(V\) on \(\mathcal H_{\mathrm{in}}\), the channel \(X\mapsto U\mathcal N(VXV^*)U^*\) has the same Holevo information and the same minimum output entropy as \(\mathcal N\).
4. \(\chi(\mathcal N_1\otimes\mathcal N_2)\ge\chi(\mathcal N_1)+\chi(\mathcal N_2)\), and \(S_{\min}(\mathcal N_1\otimes\mathcal N_2)\) is at most \(S_{\min}(\mathcal N_1)+S_{\min}(\mathcal N_2)\).

*Proof.* (1) Write each \(\rho_a\) as \(\sum_k\mu_{ak}\psi_{ak}\psi_{ak}^*\) by the spectral theorem, and replace it by the pure states \(\psi_{ak}\psi_{ak}^*\) with probabilities \(q_a\mu_{ak}\). The mean output does not change, and by concavity
\[
\begin{aligned}
&\sum_{a,k}q_a\mu_{ak}S\bigl(\mathcal N(\psi_{ak}\psi_{ak}^*)\bigr)\\
&\qquad\le\sum_aq_aS\bigl(\mathcal N(\rho_a)\bigr),
\end{aligned}
\]
so the Holevo quantity does not decrease.

(2) If \(\rho=\sum_k\mu_k\psi_k\psi_k^*\) attains the minimum, concavity gives \(S(\mathcal N(\rho))\ge\sum_k\mu_kS(\mathcal N(\psi_k\psi_k^*))\), so some \(\psi_k\psi_k^*\) attains it too.

(3) The map \(\rho\mapsto V\rho V^*\) is a bijection of the states of \(\mathcal H_{\mathrm{in}}\), and conjugation by \(U\) does not change the spectrum of any output or mean output.

(4) For ensembles \(\{q_a,\rho_a\}\) and \(\{r_b,\sigma_b\}\), the product ensemble \(\{q_ar_b,\rho_a\otimes\sigma_b\}\) has the outputs \(\mathcal N_1(\rho_a)\otimes\mathcal N_2(\sigma_b)\), and its mean output is the tensor product of the two mean outputs. By additivity of entropy on products, its Holevo quantity is the sum of the two Holevo quantities. Taking suprema gives the first inequality, and the product of two minimizing states gives the second. \(\blacksquare\)

## 4. Codes and capacity

An \((n,M)\) *code* for a channel \(\mathcal N\) consists of states \(\rho_1,\dots,\rho_M\) on \(\mathcal H_{\mathrm{in}}^{\otimes n}\) and a *measurement*: operators \(E_1,\dots,E_M\ge0\) on \(\mathcal H_{\mathrm{out}}^{\otimes n}\) with \(\sum_kE_k\le I\), where \(I-\sum_kE_k\) stands for no decision. The error probability of message \(k\) is \(\varepsilon_k=1-\operatorname{Tr}\bigl(E_k\mathcal N^{\otimes n}(\rho_k)\bigr)\), the *average error* is \(\bar\varepsilon=\frac1M\sum_k\varepsilon_k\), and the *maximal error* is \(\max_k\varepsilon_k\). The states may be entangled across the \(n\) inputs, and the measurement acts on all \(n\) outputs together; there is no entanglement shared in advance and no feedback.

A rate \(R\ge0\) is *achievable* if for every \(n\ge1\) there is an \((n,M_n)\) code, with average errors \(\bar\varepsilon_n\to0\) and \(\liminf_n\frac1n\log_2M_n\ge R\). The *classical capacity* \(C(\mathcal N)\) is the supremum of the achievable rates; codes with \(M=1\) and \(E_1=I\) show that the rate \(0\) is achievable.

**Remark 4.1** (maximal error). The maximal error gives the same capacity. A code with maximal error \(\varepsilon\) has average error at most \(\varepsilon\). Conversely, in an \((n,M)\) code with average error \(\bar\varepsilon\), fewer than \(M/2\) messages have \(\varepsilon_k>2\bar\varepsilon\); keeping \(\lceil M/2\rceil\) of the other messages, with their measurement operators, gives a code with maximal error at most \(2\bar\varepsilon\) and \(\log_2\) of its size at least \(\log_2M-1\), which does not change the rate.

**Hypothesis (CT)** (the classical coding theorem). For every channel \(\mathcal N\) between finite-dimensional spaces,
\[
C(\mathcal N)=\sup_{n\ge1}\frac1n\chi(\mathcal N^{\otimes n}).
\]

This is the theorem of Holevo and of Schumacher and Westmoreland. The inequality \(\ge\) is the coding theorem for a fixed finite ensemble [Holevo, Theorem], applied to the ensembles of states on blocks of \(n\) inputs, each block treated as one letter: random codes from an ensemble with Holevo quantity \(\chi_0\) for \(\mathcal N^{\otimes n}\) achieve every rate below \(\chi_0/(n\ln2)\). The inequality \(\le\) follows from Holevo's entropy bound and Fano's inequality: an \((n,M)\) code with average error \(\bar\varepsilon\) satisfies
\[
(1-\bar\varepsilon)\log_2M\le\chi(\mathcal N^{\otimes n})+\frac{h(\bar\varepsilon)}{\ln2} .
\]
A complete treatment of both directions, with maximal error, is [Wilde, Theorem 20.3.1 and Sections 20.3.1–20.3.2]. Neither direction is proved in this programme. The course uses (CT) only to turn its statements about Holevo information into statements about capacity; every statement about \(\chi\) and \(S_{\min}\) is proved without it.

**Proposition 4.2** (the regularization is a limit). For every channel \(\mathcal N\), the numbers \(a_n=\chi(\mathcal N^{\otimes n})\) satisfy \(a_{m+n}\ge a_m+a_n\) and \(0\le a_n\le n\log_2\dim\mathcal H_{\mathrm{out}}\). Consequently \(\lim_na_n/n\) exists and equals \(\sup_na_n/n\).

*Proof.* Since \(\mathcal N^{\otimes(m+n)}=\mathcal N^{\otimes m}\otimes\mathcal N^{\otimes n}\), Lemma 3.1(4) gives superadditivity, and the bounds hold because \(0\le S\le\ln\dim\) on states. Fix \(k\), and write \(n=qk+r\) with \(0\le r<k\). Superadditivity and \(a_r\ge0\), with \(a_0=0\), give \(a_n\ge qa_k\), so
\[
\frac{a_n}n\ge\frac{qk}n\cdot\frac{a_k}k\longrightarrow\frac{a_k}k
\]
as \(n\to\infty\). Hence \(\liminf_na_n/n\ge a_k/k\) for every \(k\), so \(\liminf_na_n/n\ge\sup_ka_k/k\); and \(\sup_ka_k/k\ge\limsup_na_n/n\) holds in any case. \(\blacksquare\)

If \(\chi(\mathcal N^{\otimes n})=n\chi(\mathcal N)\) for every \(n\), the supremum is \(\chi(\mathcal N)\); under (CT), \(C(\mathcal N)=\chi(\mathcal N)\), and the capacity is given by a single use. Holevo information is not additive for all channels [Hastings], so this needs an argument for the channel at hand.

## 5. The generalized amplitude-damping channel

Let \(|0\rangle\) and \(|1\rangle\) be the standard basis of \(\mathbb C^2\): the ground level and the excited level. For \(\gamma,\nu\in[0,1]\) put
\[
\begin{gathered}
k=\sqrt{1-\gamma},\qquad c=\gamma\nu,\\
b=\gamma(1-\nu),\\
a=1-c,\qquad d=1-b,
\end{gathered}
\]
and let \(\mathcal A=\mathcal A_{\gamma,\nu}\) be the linear map on \(\mathcal B(\mathbb C^2)\) with
\[
\begin{gathered}
\mathcal A(|0\rangle\langle0|)=\operatorname{diag}(a,c),\\
\mathcal A(|1\rangle\langle1|)=\operatorname{diag}(b,d),\\
\mathcal A(|0\rangle\langle1|)=k\,|0\rangle\langle1|,\\
\mathcal A(|1\rangle\langle0|)=k\,|1\rangle\langle0| .
\end{gathered}
\]
So \(\mathcal A\) maps a matrix \(X=(x_{ij})\) to the matrix with diagonal entries \(ax_{00}+bx_{11}\) and \(cx_{00}+dx_{11}\) and off-diagonal entries \(kx_{01}\) and \(kx_{10}\).
On a state with excited population \(q\) and coherence \(z\),
\[
\mathcal A\begin{pmatrix}1-q&z\\ \bar z&q\end{pmatrix}=\begin{pmatrix}1-t&kz\\ k\bar z&t\end{pmatrix},
\]
where \(t=(1-\gamma)q+\gamma\nu\). The populations move towards \((1-\nu,\nu)\) by the fraction \(\gamma\), and the coherence is multiplied by \(k\). The state \(\operatorname{diag}(1-\nu,\nu)\) is fixed: \(\nu\) is the stationary excited population. For \(\nu=0\) this is ordinary amplitude damping, and for \(\gamma=0\) the identity.

**Lemma 5.1** (Kraus operators). \(a+c=b+d=1\) and \(ad-bc=k^2\). The operators
\[
\begin{gathered}
L_0=\sqrt{1-\nu}\,\operatorname{diag}(1,k),\\
L_1=\sqrt b\,|0\rangle\langle1|,\\
L_2=\sqrt\nu\,\operatorname{diag}(k,1),\\
L_3=\sqrt c\,|1\rangle\langle0|
\end{gathered}
\]
satisfy \(\sum_iL_i^*L_i=I\) and \(\mathcal A(X)=\sum_iL_iXL_i^*\). In particular \(\mathcal A\) is a channel.

*Proof.* The first two identities are the definitions of \(a\) and \(d\), and
\[
\begin{aligned}
ad-bc&=(1-\gamma\nu)(1-\gamma+\gamma\nu)\\
&\quad-\gamma^2\nu(1-\nu)\\
&=1-\gamma .
\end{aligned}
\]
Next, \(L_0^*L_0+L_2^*L_2\) is diagonal with the entries \(1-\nu+\nu k^2=1-\gamma\nu=a\) and \((1-\nu)k^2+\nu=1-\gamma+\gamma\nu=d\), and \(L_1^*L_1+L_3^*L_3=\operatorname{diag}(c,b)\). The sum is \(\operatorname{diag}(a+c,b+d)=I\). In \(\sum_iL_iXL_i^*\), the entry \((0,0)\) is \((1-\nu+\nu k^2)x_{00}+bx_{11}\), that is \(ax_{00}+bx_{11}\); the entry \((1,1)\) is \(cx_{00}+((1-\nu)k^2+\nu)x_{11}\), that is \(cx_{00}+dx_{11}\); and the entry \((0,1)\) is \(((1-\nu)k+\nu k)x_{01}=kx_{01}\), and the entry \((1,0)\) likewise \(kx_{10}\). Lemma 1.1 applies. \(\blacksquare\)

**Lemma 5.2** (pure inputs). Let \(\phi=\sqrt{1-p}\,|0\rangle+e^{i\theta}\sqrt p\,|1\rangle\) with \(p\in[0,1]\); up to a phase, every unit vector of \(\mathbb C^2\) has this form. Put \(t=t(p)=(1-\gamma)p+\gamma\nu\). The output \(\mathcal A(\phi\phi^*)\) has excited population \(t\), determinant
\[
\begin{aligned}
v(p)&=t(1-t)-(1-\gamma)p(1-p)\\
&=\gamma\nu(1-\nu)\\
&\quad+\gamma(1-\gamma)(p-\nu)^2,
\end{aligned}
\]
and entropy \(e(p)=g(v(p))\). In particular \(0\le v(p)\le\frac14\), and \(v(p)\ge\gamma\nu(1-\nu)\), with equality at \(p=\nu\).

*Proof.* The input has the populations \(1-p\) and \(p\) and a coherence of modulus \(\sqrt{p(1-p)}\). By the formula for \(\mathcal A\) on states, the output has the populations \(1-t\) and \(t\) and a coherence of modulus \(k\sqrt{p(1-p)}\); this gives the first form of the determinant. Since \(t-(1-\gamma)p=\gamma\nu\),
\[
\begin{aligned}
&t(1-t)-(1-\gamma)p(1-p)\\
&\qquad=\gamma\nu-t^2+(1-\gamma)p^2 .
\end{aligned}
\]
Inserting \(t^2=(1-\gamma)^2p^2+2\gamma\nu(1-\gamma)p+\gamma^2\nu^2\) gives \(\gamma\nu-\gamma^2\nu^2+\gamma(1-\gamma)(p^2-2\nu p)\). Since \(p^2-2\nu p=(p-\nu)^2-\nu^2\) and \(\gamma\nu-\gamma^2\nu^2-\gamma(1-\gamma)\nu^2=\gamma\nu(1-\nu)\), this is the second form. The output is a state on \(\mathbb C^2\), so its determinant lies in \([0,\frac14]\) and its entropy is \(g(v(p))\) by fact 5 of Section 2. \(\blacksquare\)

If \(\gamma>0\) and \(0<\nu<1\), then \(v(p)\ge\gamma\nu(1-\nu)>0\) for all \(p\): every pure input has an invertible output, and so does every mixed input, as a mixture of such outputs. In this range the channel has no pure output. For \(\nu\in\{0,1\}\), or \(\gamma=0\), it has one: for instance \(\mathcal A_{\gamma,0}(|0\rangle\langle0|)=|0\rangle\langle0|\).

**Theorem 5.3** (the theorem of the course; [OpenAI-GAD, Theorem 1.1 and Corollary 1.2]). Let \(\gamma,\nu\in[0,1]\), \(\mathcal A=\mathcal A_{\gamma,\nu}\), \(t(p)\) and \(e\) as in Lemma 5.2, and, for \(0\le p\le1\),
\[
f(p)=h\bigl(t(p)\bigr)-e(p).
\]

1. For every \(n\ge1\),
\[
\begin{aligned}
\chi(\mathcal A^{\otimes n})&=n\,\chi(\mathcal A)\\
&=\frac n{\ln2}\max_{0\le p\le1}f(p).
\end{aligned}
\]
If \(p\) maximizes \(f\), the \(2^n\) tensor products of the states \(\phi_\pm=\sqrt{1-p}\,|0\rangle\pm\sqrt p\,|1\rangle\), with equal probabilities, form an ensemble that attains \(\chi(\mathcal A^{\otimes n})\).
2. For every channel \(\mathcal N\) between nonzero finite-dimensional spaces,
\[
\begin{aligned}
\chi(\mathcal A\otimes\mathcal N)&=\chi(\mathcal A)+\chi(\mathcal N),\\
S_{\min}(\mathcal A\otimes\mathcal N)&=S_{\min}(\mathcal A)\\
&\quad+S_{\min}(\mathcal N),
\end{aligned}
\]
and the regularized Holevo informations add:
\[
\begin{aligned}
&\sup_n\frac1n\chi\bigl((\mathcal A\otimes\mathcal N)^{\otimes n}\bigr)\\
&\qquad=\chi(\mathcal A)+\sup_n\frac1n\chi(\mathcal N^{\otimes n}).
\end{aligned}
\]
3. Under Hypothesis (CT), \(C(\mathcal A)=\chi(\mathcal A)\) and \(C(\mathcal A\otimes\mathcal N)=C(\mathcal A)+C(\mathcal N)\).

The upper bound in (1) concerns all input states of \(n\) uses, including states entangled across the uses, and all measurements on the outputs; independent uses of a two-state ensemble attain it. In (2) nothing is assumed of the partner \(\mathcal N\), whose own capacity may need the regularization.

The proof occupies the rest of the course. [Entropy differences and log-determinants](entropy-differences-and-log-determinants.md) writes entropy differences as integrals of log-determinants and proves a joint convexity and a scalar concavity. [Block entropy inequalities](block-entropy-inequalities.md) proves two entropy inequalities for block matrices. [Output entropy of damping blocks](output-entropy-of-damping-blocks.md) turns them into a lower bound for the output entropy of \(n\) uses in terms of the input populations at each site, and proves part (1). [Additivity with an arbitrary partner](additivity-with-an-arbitrary-partner.md) proves parts (2) and (3) and works out special cases.

For ordinary amplitude damping (\(\nu=0\)), the one-use maximum and the ensemble \(\phi_\pm\) are due to Giovannetti and Fazio [GF, Section III A], and the equality of the classical capacity with the Holevo information, with additivity against every finite-dimensional partner, was proved by Tang, Zhu, Bai and Wang [TZBW, Theorem 5.5], together with the same conclusions for every qubit channel with a pure output [TZBW, Corollary 6.2]. Their argument rests on a triangular block entropy inequality [TZBW, Theorem 4.2]; the second and third lessons prove the case of it needed here and extend it to the thermal case, where the channel has no pure output.

## 6. Exercises

**6.1.** Show that the transposition \(X\mapsto X^{\mathsf T}\) of \(2\times2\) matrices is positive and trace preserving, but not completely positive.

**6.2.** Show that \(\mathcal A_{\gamma',\nu}\circ\mathcal A_{\gamma,\nu}=\mathcal A_{\gamma'',\nu}\) with \(1-\gamma''=(1-\gamma)(1-\gamma')\).

**6.3.** Show that for \(\gamma>0\) the state \(\operatorname{diag}(1-\nu,\nu)\) is the only state fixed by \(\mathcal A_{\gamma,\nu}\).

**6.4.** Show that \(S_{\min}(\mathcal A_{\gamma,\nu})=g(\gamma\nu(1-\nu))\), and find the pure states that attain it.

**6.5.** Show that \(\chi(\mathcal A_{1,\nu})=0\) and \(\chi(\mathcal A_{0,\nu})=1\).

**6.6.** Let \(\mathcal N\) be a channel and \(\{q_a,\rho_a\}\) an ensemble. Show that \(\chi_{\mathcal N}\{q_a,\rho_a\}\le H(q)\) when the outputs \(\mathcal N(\rho_a)\) have mutually orthogonal supports, and that equality holds in that case.

## 7. Solutions

**6.1.** \(X^{\mathsf T}\) has the eigenvalues of \(X\) and the same trace. For \(\Omega=e_1\otimes e_1+e_2\otimes e_2\), \((\mathrm{id}_2\otimes{}^{\mathsf T})(\Omega\Omega^*)=\sum_{i,j}e_ie_j^*\otimes e_je_i^*\) is the operator that exchanges the two factors, and it maps \(e_1\otimes e_2-e_2\otimes e_1\) to its negative, so it has the eigenvalue \(-1\).

**6.2.** Both maps multiply coherences by \(\sqrt{1-\gamma}\sqrt{1-\gamma'}=\sqrt{1-\gamma''}\). On populations, the composite maps \(q\) to \((1-\gamma')t+\gamma'\nu\) with \(t=(1-\gamma)q+\gamma\nu\), which is \((1-\gamma)(1-\gamma')q+(\gamma+\gamma'-\gamma\gamma')\nu\), and \(\gamma+\gamma'-\gamma\gamma'=\gamma''\). Two linear maps that agree on the matrix entries agree.

**6.3.** A fixed state has \((1-\gamma)q+\gamma\nu=q\), that is \(\gamma(q-\nu)=0\), and \(kz=z\) with \(k<1\). So \(q=\nu\) and \(z=0\).

**6.4.** By Lemma 3.1(2) and Lemma 5.2, \(S_{\min}=\min_pg(v(p))\). Since \(g\) is nondecreasing, the minimum is \(g\) of the minimum of \(v\), which is \(\gamma\nu(1-\nu)\), at \(p=\nu\). The minimizing pure states are \(\sqrt{1-\nu}\,|0\rangle+e^{i\theta}\sqrt\nu\,|1\rangle\), for every \(\theta\) (and, when \(v\) is constant, that is \(\gamma\in\{0,1\}\), all pure states).

**6.5.** \(\mathcal A_{1,\nu}\) maps every state to \(\operatorname{diag}(1-\nu,\nu)\), so every Holevo quantity is \(0\). \(\mathcal A_{0,\nu}\) is the identity. Every Holevo quantity is at most the entropy of the mean output, hence at most \(\ln2\), and the ensemble of \(|0\rangle\langle0|\) and \(|1\rangle\langle1|\) with probabilities \(\frac12\) attains \(\ln2\). So \(\chi(\mathcal A_{0,\nu})=1\).

**6.6.** If the supports are orthogonal, the mean output \(\sum_aq_a\mathcal N(\rho_a)\) is a direct sum of the operators \(q_a\mathcal N(\rho_a)\), so by facts 2 and 3 of Section 2 its entropy is \(\sum_a\bigl(q_aS(\mathcal N(\rho_a))-q_a\ln q_a\bigr)\) (terms with \(q_a=0\) omitted). Subtracting \(\sum_aq_aS(\mathcal N(\rho_a))\) leaves \(H(q)\).

## References

- [OpenAI-GAD] OpenAI, *Classical capacity and entropy inequalities for generalized amplitude damping*, OpenAI Math Release preprint, 24 September 2026, Section 1. https://github.com/openai/math/tree/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
- [Holevo] A. S. Holevo, *The capacity of the quantum channel with general signal states*, IEEE Transactions on Information Theory 44 (1998); preprint arXiv:quant-ph/9611023, the Theorem in Section 2 and its proof in Sections 3–6. https://arxiv.org/abs/quant-ph/9611023
- [Wilde] M. M. Wilde, *From Classical to Quantum Shannon Theory*, arXiv:1106.1445v8, Chapter 20. https://arxiv.org/abs/1106.1445
- [Hastings] M. B. Hastings, *Superadditivity of communication capacity using entangled inputs*, Nature Physics 5 (2009); preprint arXiv:0809.3972. https://arxiv.org/abs/0809.3972
- [GF] V. Giovannetti and R. Fazio, *Information-capacity description of spin-chain correlations*, Physical Review A 71 (2005); preprint arXiv:quant-ph/0405110. https://arxiv.org/abs/quant-ph/0405110
- [TZBW] Z. Tang, C. Zhu, G. Bai and X. Wang, *Classical capacity and entanglement cost of the amplitude damping channel*, arXiv:2609.28592 (2026). https://arxiv.org/abs/2609.28592

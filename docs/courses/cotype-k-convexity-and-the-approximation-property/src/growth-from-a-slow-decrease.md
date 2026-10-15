# Growth from a slow decrease

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the key step of the decay theorem (Lemma 2.1): if the Walsh norms of an operator decrease slowly between the indices \(n-2m\) and \(n\), then the Walsh norm at index \(2(n-2m)\), almost twice as large, is still comparable to the one at \(n\). The proof turns a Walsh test into three bounded scalar functions to which the coefficient lemma of [A Fourier coefficient of binary rank two](a-fourier-coefficient-of-binary-rank-two.md) applies; a coefficient of binary rank \(k\ge2\) then produces a Walsh test with \(k\) independent factors. To make the scalar functions depend only on sign matrices, the vectors of the Walsh test are replaced by *frames*, linearly independent tuples, on which the general linear group over \(\mathbb F_2\) acts transitively with prescribed pairings (Lemma 1.1).

- Pairs of frames (Lemma 1.1).
- Growth from a slow decrease (Lemma 2.1), in five steps.

The lesson follows [OpenAI-CC, Section 4.1]. Notation is that of [Walsh norms and moment lifts](walsh-norms-and-moment-lifts.md): \(V_n=\mathbb F_2^n\), \(\chi(u,v)=(-1)^{u\cdot v}\), Walsh norms \(w_n\), fixed-length cotype constants \(c_m\), and the lift parameters \(a,b\) of (3.1) there. For a function \(h\) on a sign cube, \(\mathcal Oh\) is its odd part.

## 1. Pairs of frames

A *frame* in \(V_n\) is an ordered linearly independent tuple. Vectors and covectors are identified through the dot product; the group \(\mathrm{GL}(n,\mathbb F_2)\) acts on primal frames by \(U\mapsto HU=(Hu_i)\) and on covector frames by \(V\mapsto H^{-\mathrm t}V\). The pairing matrix of a primal frame \(U\) of length \(r\) and a covector frame \(V\) of length \(s\) is \((u_i\cdot v_j)\), an \(r\times s\) binary matrix; it is unchanged by \((U,V)\mapsto(HU,H^{-\mathrm t}V)\), since \(Hu\cdot H^{-\mathrm t}v=u\cdot v\).

**Lemma 1.1** (pairs of frames; [OpenAI-CC, Lemma 4.1]). The action \((U,V)\mapsto(HU,H^{-\mathrm t}V)\) of \(\mathrm{GL}(n,\mathbb F_2)\) is transitive on pairs of frames of fixed lengths \(r,s\) with a prescribed pairing matrix. If \(n\ge r+s\), every binary \(r\times s\) matrix is a pairing matrix.

*Proof.* Let \((U,V)\) and \((U',V')\) have the same pairing matrix. The maps \(\pi(x)=(x\cdot v_j)_j\) and \(\pi'(x)=(x\cdot v_j')_j\) from \(V_n\) to \(\mathbb F_2^s\) are surjective, since the \(v_j\) and the \(v_j'\) are independent. The isomorphism \(\phi_0\colon\operatorname{span}U\to\operatorname{span}U'\), \(u_i\mapsto u_i'\), satisfies \(\pi'\phi_0=\pi\) on \(\operatorname{span}U\), because the pairing matrices agree; so it maps \(\operatorname{span}U\cap\ker\pi\) onto \(\operatorname{span}U'\cap\ker\pi'\). The kernels have the same dimension \(n-s\); extend the restriction of \(\phi_0\) to an isomorphism \(\kappa\colon\ker\pi\to\ker\pi'\). Together, \(\phi_0\) and \(\kappa\) define an isomorphism \(\operatorname{span}U+\ker\pi\to\operatorname{span}U'+\ker\pi'\) with \(\pi'H=\pi\). Choose a basis \(c_1,\dots,c_t\) of a complement of \(\operatorname{span}U+\ker\pi\); the vectors \(\pi(c_l)\) are independent modulo \(\pi(\operatorname{span}U)=\pi'(\operatorname{span}U')\). Choose \(c_l'\) with \(\pi'(c_l')=\pi(c_l)\) and put \(Hc_l=c_l'\). Then \(H\) is invertible, \(HU=U'\), and \(\pi'H=\pi\), which says \((Hx)\cdot v_j'=x\cdot v_j\) for all \(x\), that is \(H^{-\mathrm t}V=V'\).

For the second assertion, given a binary \(r\times s\) matrix \(D\), take \(u_i=(e_i,0)\) and \(v_j=(D_{:,j},e_j)\) in \(\mathbb F_2^r\oplus\mathbb F_2^s\subseteq V_n\). \(\blacksquare\)

## 2. Growth from a slow decrease

**Lemma 2.1** (growth; [OpenAI-CC, Lemma 4.2]). Let \(m\ge1\) and \(D_g,D_f\ge1\), and suppose that \(m\) and the parameters \(a,b\) of (3.1) of the previous lesson satisfy the hypotheses of Lemma 2.1 of [A Fourier coefficient of binary rank two](a-fourier-coefficient-of-binary-rank-two.md), with its constant \(c_*\). Put \(c_1=\min(1/2,c_*/2)\). If
\[
\begin{gathered}
c_m(G^*)\le D_g,\qquad c_m(F)\le D_f,\\
0\ne T\colon G\to F,
\end{gathered}
\]
and \(n>4m\) satisfies
\[
w_{n-2m}(T)\le2w_n(T), \tag{2.1}
\]
then
\[
w_{2(n-2m)}(T)\ge c_1w_n(T). \tag{2.2}
\]
\(T\) need not have finite rank.

*Proof.* Put \(n'=n-2m\).

*Step 1: exact Walsh signs.* By (1.1) of the previous lesson there are \(p_u\in G\) and \(q_v\in F^*\), \(u,v\in V_n\), with \(\mathbb E_u\|p_u\|^2\le1\), \(\mathbb E_v\|q_v\|^2\le1\) and
\[
\gamma=\mathbb E_{u,v}\chi(u,v)\,q_v(Tp_u)\ge\tfrac12w_n(T)>0 .
\]
Let \(T'\) be \(T\) applied pointwise on \(L_2(V_n\times V_n;G)\), and put
\[
\begin{gathered}
x_u'(\alpha,\beta)=(-1)^{u\cdot\beta+\alpha\cdot\beta}p_{u+\alpha},\\
y_v'(\alpha,\beta)=(-1)^{\alpha\cdot v}q_{v+\beta}.
\end{gathered}
\]
By translation invariance of the uniform measure, \(\|x_u'\|\le1\) and \(\|y_v'\|\le1\). Modulo \(2\),
\[
\begin{aligned}
u\cdot\beta+\alpha\cdot\beta&+\alpha\cdot v\\
&=(u+\alpha)\cdot(v+\beta)+u\cdot v,
\end{aligned}
\]
so
\[
\begin{aligned}
y_v'(T'x_u')&=\chi(u,v)\,\mathbb E_{\alpha,\beta}\chi(u+\alpha,v+\beta)\\
&\qquad\cdot q_{v+\beta}(Tp_{u+\alpha})\\
&=\gamma\,\chi(u,v).
\end{aligned}
\]
Amplify once more over \(\mathscr G=\mathrm{GL}(n,\mathbb F_2)\): let \(\widetilde T\colon\widetilde G\to\widetilde F\) be \(T'\) applied pointwise on functions on \(\mathscr G\), and put \(x_u(R)=x_{Ru}'\), \(y_v(R)=y_{R^{-\mathrm t}v}'\). For the bilinear form \(\mathcal B(x,y)=y(\widetilde Tx)\),
\[
\begin{gathered}
x_u\in B_{\widetilde G},\qquad y_v\in B_{\widetilde F^*},\\
\mathcal B(x_u,y_v)=\gamma\,\chi(u,v),
\end{gathered} \tag{2.3}
\]
since \(Ru\cdot R^{-\mathrm t}v=u\cdot v\). The right translations \(\Lambda(H)z(R)=z(RH)\), on \(\widetilde G\) and on \(\widetilde F^*\), are isometries, satisfy \(\Lambda(H_1)\Lambda(H_2)=\Lambda(H_1H_2)\), preserve \(\mathcal B\) when applied to both arguments, and
\[
\Lambda(H)x_u=x_{Hu},\qquad\Lambda(H)y_v=y_{H^{-\mathrm t}v},
\]
because \((RH)^{-\mathrm t}=R^{-\mathrm t}H^{-\mathrm t}\). By Lemma 1.1(2) of the previous lesson, \(w_j(\widetilde T)=w_j(T)\) for all \(j\). By Section 2 there, \(c_m(\widetilde F)\le D_f\) and \(c_m(\widetilde G^*)\le D_g\), so the moment lifts of Lemma 3.2 there are available with the same \(a,b\).

*Step 2: equivariant lifts of frames.* For a primal \(m\)-frame \(U\) we want \(P_{U,\varepsilon}\in B_{\widetilde G}\), \(\varepsilon\in\{-1,1\}^m\), with
\[
\begin{gathered}
\mathbb E_\varepsilon\varepsilon_iP_{U,\varepsilon}=a\,x_{u_i}\quad(1\le i\le m),\\
\Lambda(H)P_{U,\varepsilon}=P_{HU,\varepsilon}.
\end{gathered}
\]
Fix a frame \(U_0\) and lifts \(P_{U_0,\varepsilon}\) from Lemma 3.2 of the previous lesson, and replace them by their averages over the stabilizer \(\{K:KU_0=U_0\}\) under \(\Lambda\). The averages keep the moments, since \(\Lambda(K)x_{u_i}=x_{Ku_i}=x_{u_i}\), lie in the unit ball, and are invariant under the stabilizer. For \(U=HU_0\) put \(P_{U,\varepsilon}=\Lambda(H)P_{U_0,\varepsilon}\). This is well defined, because two choices of \(H\) differ on the right by a stabilizer element, and it is equivariant and has the required moments. The action on \(m\)-frames is transitive by Lemma 1.1. In the same way, with the action \(H^{-\mathrm t}\), there are \(Z_{V,\delta}\in B_{\widetilde F^*}\) for covector \(m\)-frames \(V\), with
\[
\begin{gathered}
\mathbb E_\delta\delta_jZ_{V,\delta}=b\,y_{v_j},\\
\Lambda(H)Z_{V,\delta}=Z_{H^{-\mathrm t}V,\delta}.
\end{gathered}
\]
By equivariance, the invariance of \(\mathcal B\) and Lemma 1.1, the following numbers depend only on the displayed sign patterns and on \(\varepsilon,\delta\):
\[
\begin{aligned}
\Phi(S,\varepsilon,\delta)&=\mathcal B(P_{U,\varepsilon},Z_{V,\delta}),\\
\phi(s,\varepsilon)&=\mathcal B(P_{U,\varepsilon},y_v),\\
\psi(t,\delta)&=\mathcal B(x_u,Z_{V,\delta}),
\end{aligned}
\]
where \(S_{ij}=\chi(u_i,v_j)\), \(s_i=\chi(u_i,v)\) with \(v\ne0\), and \(t_j=\chi(u,v_j)\) with \(u\ne0\).
Every pattern occurs, since \(n>4m\ge2m\). The moment identities and (2.3) give
\[
\begin{aligned}
&\mathbb E_\varepsilon\varepsilon_i\Phi(S,\varepsilon,\delta)\\
&\quad=a\,\psi(S_{i,:},\delta),\\
&\mathbb E_\delta\delta_j\Phi(S,\varepsilon,\delta)\\
&\quad=b\,\phi(S_{:,j},\varepsilon),\\
&\mathbb E_\varepsilon\varepsilon_i\phi(s,\varepsilon)=a\gamma\,s_i,\\
&\mathbb E_\delta\delta_j\psi(t,\delta)=b\gamma\,t_j .
\end{aligned} \tag{2.4}
\]

*Step 3: odd parts on a smaller cube.* For all \(\varepsilon,\delta\), the three numbers
\[
\begin{gathered}
\|\mathcal O\Phi(\cdot,\varepsilon,\delta)\|_\infty,\\
\|\mathcal O\phi(\cdot,\varepsilon)\|_\infty,\\
\|\mathcal O\psi(\cdot,\delta)\|_\infty
\end{gathered} \tag{2.5}
\]
are at most \(w_{n'}(T)\).
Write \(V_n=V_{n'}\oplus\mathbb F_2^m\oplus\mathbb F_2^m\) and fix \(S_0=((-1)^{D_{ij}})\). For \(u,v\in V_{n'}\) take the primal frame \(U(u)_i=(u,e_i,0)\) and the covector frames \(V^\pm(v)_j\), with \(V^+(v)_j=(v,D_{:,j},e_j)\) and \(V^-(v)_j=(v,D_{:,j}+\mathbf1,e_j)\), where \(\mathbf1\) is the all-ones vector; the tags \(e_i\), \(e_j\) make them frames for every \(u,v\). Their sign matrices are \(\chi(u,v)S_0\) and \(-\chi(u,v)S_0\), so
\[
\begin{aligned}
&\mathcal B\Bigl(P_{U(u),\varepsilon},\tfrac12\bigl(Z_{V^+(v),\delta}-Z_{V^-(v),\delta}\bigr)\Bigr)\\
&\quad=\chi(u,v)\,\mathcal O\Phi(S_0,\varepsilon,\delta).
\end{aligned}
\]
The two families lie in the unit balls and depend only on \(u\) and on \(v\), respectively. Testing (1.1) of the previous lesson at \(n'\) and using \(w_{n'}(\widetilde T)=w_{n'}(T)\) gives the first bound. For \(\phi\), keep \(U(u)\) and use the nonzero covectors \((v,h,e_1)\) and \((v,h+\mathbf1,e_1)\), where \(s_i=(-1)^{h_i}\), and half the difference of the corresponding \(y\)'s. For \(\psi\), use the covector frame \((v,0,e_j)_j\) and half the difference of \(x\)'s at the nonzero vectors \((u,e_1,h)\) and \((u,e_1,h+\mathbf1)\), whose pairings with \((v,0,e_j)\) are \(\chi(u,v)(-1)^{h_j}\) and its negative.

*Step 4: a coefficient of rank at least two.* Define the odd functions
\[
\begin{aligned}
f(s)&=\gamma^{-1}\,\mathcal O_s\,\mathbb E_\varepsilon\phi(\varepsilon s,\varepsilon),\\
g(t)&=\gamma^{-1}\,\mathcal O_t\,\mathbb E_\delta\psi(\delta t,\delta),\\
\Psi(S)&=\gamma^{-1}\,\mathcal O_S\,\mathbb E_{\varepsilon,\delta}\Phi(\varepsilon S\delta,\varepsilon,\delta),
\end{aligned}
\]
where \(\varepsilon s\) and \(\delta t\) are entrywise products. Taking odd parts commutes with the averages, so by (2.5), (2.1) and \(\gamma\ge w_n(T)/2\), all three sup norms are at most \(w_{n'}(T)/\gamma\le4=M_0\). The substitution \(s'=\varepsilon s\) and (2.4) give
\[
\widehat f(e_i)=\gamma^{-1}\mathbb E_{s',\varepsilon}s_i'\varepsilon_i\,\phi(s',\varepsilon)=a,
\]
and likewise \(\widehat g(e_j)=b\). For the row identity, note that \(\mathbb E_\sigma\sigma_ih(\sigma S)\) does not change when \(h\) is replaced by its odd part, because \(\mathbb E_\sigma\sigma_ih(-\sigma S)=-\mathbb E_\sigma\sigma_ih(\sigma S)\). Substituting \(\xi=\varepsilon\sigma\), and using (2.4) and that row \(i\) of \(\xi S\delta\) is \(\xi_i\,\delta S_{i,:}\),
\[
\begin{aligned}
&\gamma\,\mathbb E_\sigma\sigma_i\Psi(\sigma S)\\
&=\mathbb E_{\xi,\varepsilon,\delta}\xi_i\varepsilon_i\,\Phi(\xi S\delta,\varepsilon,\delta)\\
&=a\,\mathbb E_{\xi,\delta}\xi_i\,\psi(\xi_i\,\delta S_{i,:},\delta)\\
&=a\,\mathbb E_\delta\tfrac12\bigl(\psi(\delta S_{i,:},\delta)-\psi(-\delta S_{i,:},\delta)\bigr)\\
&=a\gamma\,g(S_{i,:}).
\end{aligned}
\]
Exchanging rows and columns gives \(\mathbb E_\tau\tau_j\Psi(S\tau)=b\,f(S_{:,j})\). So the coefficient lemma applies: there is a binary matrix \(P\) of rank \(k\ge2\) with \(|\widehat\Psi(P)|\ge c_*\). Since \(\Psi\) is odd, \(|P|\) is odd, and the coefficient is unchanged when the odd part is removed. With \(\Phi_{\varepsilon,\delta}(S)=\Phi(S,\varepsilon,\delta)\), the substitution \(S'=\varepsilon S\delta\) gives
\[
\gamma\,\widehat\Psi(P)=\mathbb E_{\varepsilon,\delta}\Bigl[\prod_{i,j}(\varepsilon_i\delta_j)^{P_{ij}}\,\widehat{\Phi_{\varepsilon,\delta}}(P)\Bigr].
\]
So for some fixed \(\varepsilon,\delta\) the function \(h=\Phi_{\varepsilon,\delta}\) has \(|\widehat h(P)|\ge c_*\gamma\).

*Step 5: independent Walsh factors.* Keep \(P,\varepsilon,\delta\). For tuples \((u_i')_{i\le m}\) and \((v_j')_{j\le m}\) in \(V_{n'}\) put \(U_i=(u_i',e_i,0)\) and \(V(D)_j=(v_j',D_{:,j},e_j)\) for binary \(m\times m\) matrices \(D\); these are frames, even if the tuples have repetitions or zeros. Their sign matrix has entries \((-1)^{u_i'\cdot v_j'+D_{ij}}\). Translating the uniform matrix \(D\) by \((u_i'\cdot v_j')_{ij}\) in the Fourier average gives
\[
\begin{aligned}
&\mathcal B\Bigl(P_{U,\varepsilon},\mathbb E_D(-1)^{\langle P,D\rangle}Z_{V(D),\delta}\Bigr)\\
&\quad=\widehat h(P)\,(-1)^{\sum_{i,j}P_{ij}\,u_i'\cdot v_j'},
\end{aligned}
\]
with \(\langle P,D\rangle=\sum_{i,j}P_{ij}D_{ij}\) modulo \(2\). Both arguments lie in the unit balls; the first depends only on \((u_i')\), the second only on \((v_j')\). As \(P\) has rank \(k\), there are binary \(m\times k\) matrices \(I,J\) with \(I^{\mathrm t}PJ=\mathrm{Id}_k\). For \(\zeta,\eta\in(V_{n'})^k\) substitute
\[
u_i'=\sum_{l=1}^kI_{il}\zeta_l,\qquad v_j'=\sum_{l=1}^kJ_{jl}\eta_l .
\]
The exponent becomes \(\sum_l\zeta_l\cdot\eta_l\), the dot product of \(V_{kn'}=(V_{n'})^k\). This is a Walsh test on \(V_{kn'}\) with amplitude \(\widehat h(P)\) and unit-ball families on both sides, so, by (1.1) and Lemma 1.1 of the previous lesson,
\[
\begin{aligned}
w_{2n'}(T)&\ge w_{kn'}(T)=w_{kn'}(\widetilde T)\\
&\ge|\widehat h(P)|\ge\tfrac{c_*}2\,w_n(T).
\end{aligned}
\]
\(\blacksquare\)

## 3. Exercises

**3.1.** Show that for \(r=s=1\) Lemma 1.1 says: \(\mathrm{GL}(n,\mathbb F_2)\) acts transitively on pairs \((u,v)\) of nonzero vectors with \(u\cdot v\) prescribed.

**3.2.** Verify the identity of Step 1: \(u\cdot\beta+\alpha\cdot\beta+\alpha\cdot v\) equals \((u+\alpha)\cdot(v+\beta)+u\cdot v\) modulo \(2\).

**3.3.** Why are the stabilizer averages in Step 2 needed? What goes wrong if the lifts are chosen independently for each frame?

**3.4.** Find binary \(2\times2\) matrices \(I,J\) with \(I^{\mathrm t}PJ=\mathrm{Id}_2\) for \(P=\begin{pmatrix}1&1\\0&1\end{pmatrix}\).

**3.5.** In Step 3, why does the vector \((u,e_1,h)\) need the tag \(e_1\)?

## 4. Solutions

**3.1.** Primal and covector frames of length one are nonzero vectors, and the pairing matrix is the number \(u\cdot v\).

**3.2.** \((u+\alpha)\cdot(v+\beta)\) expands to \(u\cdot v+u\cdot\beta+\alpha\cdot v+\alpha\cdot\beta\); add \(u\cdot v\) and reduce modulo \(2\).

**3.3.** Without equivariance, \(\mathcal B(P_{U,\varepsilon},Z_{V,\delta})\) could depend on the pair of frames and not only on its sign matrix, and \(\Phi\) would not be a function of \(S\).

**3.4.** \(P\) is invertible over \(\mathbb F_2\) with \(P^{-1}=P\). Take \(I=\mathrm{Id}_2\) and \(J=P\): then \(PJ=P^2=\mathrm{Id}_2\).

**3.5.** If \(u=0\) and \(h=0\), the vector \((u,0,h)\) is zero, and \(x_0\) is not covered by the definition of \(\psi\), which needs a nonzero vector.

## References

- [OpenAI-CC] OpenAI, *The cotype–cotype conjecture under the approximation property*, OpenAI Math Release preprint, 23 September 2026, Section 4.1. https://github.com/openai/math/tree/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026

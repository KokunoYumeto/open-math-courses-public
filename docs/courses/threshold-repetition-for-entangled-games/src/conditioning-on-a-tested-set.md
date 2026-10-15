# Conditioning on a tested set

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix a strategy for the \(k\)-fold repetition and a set \(C\) of tested coordinates that are all won with probability \(p>0\). This lesson describes what the players' state looks like at an untested coordinate after conditioning on that event. For each untested coordinate it builds a vector, from the shared state and averaged answer operators, together with local measurements that reproduce the conditional answers exactly. The vector depends on both players' questions at that coordinate; two approximations that depend on only one of them are constructed, and an entropy telescope bounds their average squared error by \(p\tau\), where \(\tau=\tau(C)\) is the conditioning cost. A last section bounds how much conditioning changes the law of the questions.

- Flags and averaged effects (Section 1).
- The conditional vector and its measurements (Section 2).
- Local descriptions and the entropy telescope (Section 3).
- The drift of the questions (Section 4).

Notation is that of [Entangled games and threshold repetition](entangled-games-and-threshold-repetition.md) and [A common purification of effects](a-common-purification-of-effects.md). Throughout, \(\psi\), \((M_{\mathbf x}^{\mathbf a})\), \((N_{\mathbf y}^{\mathbf b})\) is a finite-dimensional strategy for the \(k\)-fold repetition of \(G\), \(C\) is a proper subset of the coordinates, \(E_C\) is the event that every coordinate of \(C\) is won, \(p=\Pr(E_C)>0\), \(m=k-|C|\),
\[
d_C=d^{|C|},\quad L=\log\frac{d_C}p,\quad\tau=\frac Lm .
\]
Expectations of operators are taken under the original question law \(\mu^{\otimes k}\), not conditioned on \(E_C\), and \(\chi(A,B)=\langle\psi,(A\otimes B)\psi\rangle\) for operators \(A\) on \(\mathcal H_A\) and \(B\) on \(\mathcal H_B\).

## 1. Flags and averaged effects

Order the untested coordinates and write their questions as \(X_1,\dots,X_m\) and \(Y_1,\dots,Y_m\); the tested questions are \(X_C,Y_C\). For \(0\le j\le m\) the *flag* is
\[
\Omega_j=(X_C,Y_C,X_{\le j},Y_{>j}) .
\]

**Lemma 1.1.** Given a value of \(\Omega_j\) of positive probability, the question strings \(\mathbf X\) and \(\mathbf Y\) are independent.

*Proof.* The coordinates are independent. Given the flag, both questions of a tested coordinate are fixed; at an untested coordinate \(l\le j\) the question \(X_l\) is fixed and \(Y_l\) has law \(\mu(\cdot\mid X_l)\); at \(l>j\) the question \(Y_l\) is fixed and \(X_l\) has law \(\mu(\cdot\mid Y_l)\). The unfixed parts of \(\mathbf X\) and of \(\mathbf Y\) lie in different coordinates, hence are independent. No independence between the two questions of one coordinate is used. \(\square\)

For tested answer strings \(\alpha\in\mathcal A^C\) and \(\gamma\in\mathcal B^C\) define the *coarse-grained effects* and the *mask*
\[
\begin{gathered}
M_{\mathbf x}^\alpha=\sum_{\mathbf a:\,a_C=\alpha}M_{\mathbf x}^{\mathbf a},\qquad N_{\mathbf y}^\gamma=\sum_{\mathbf b:\,b_C=\gamma}N_{\mathbf y}^{\mathbf b},\\
\theta(x_C,y_C,\alpha,\gamma)=\prod_{j\in C}V(x_j,y_j,\alpha_j,\gamma_j),
\end{gathered}
\]
with \(\theta=1\) if \(C=\varnothing\). Put \(F_j^\alpha=\mathbb E[M_{\mathbf X}^\alpha\mid\Omega_j]\) and \(H_j^\gamma=\mathbb E[N_{\mathbf Y}^\gamma\mid\Omega_j]\); these are effects. Given the questions, the probability of \(E_C\) is \(\sum_{\alpha,\gamma}\theta\,\chi(M_{\mathbf x}^\alpha,N_{\mathbf y}^\gamma)\). By Lemma 1.1 and bilinearity of \(\chi\), for every \(j\)
\[
\mathbb E_{\Omega_j}\sum_{\alpha,\gamma}\theta\,\chi(F_j^\alpha,H_j^\gamma)=p . \tag{1.1}
\]

A *mode* is an index \(i\in\{1,\dots,m\}\). Removing the questions of coordinate \(i\) from the flags gives
\[
\begin{aligned}
&r_0=(X_C,Y_C,X_{<i},Y_{>i}),\\
&\nu_i=\operatorname{law}(r_0) .
\end{aligned}
\]
The variable \(r_0\) is independent of the *fresh pair* \((X_i,Y_i)\sim\mu\). Alice's questions before \(i\) and Bob's questions after \(i\) are revealed; the others are not. For each value of \(r_0\) of positive probability, each \(x\) with \(\mu_X(x)>0\) and each \(y\) with \(\mu_Y(y)>0\) (the marginals of \(\mu\)), put
\[
\begin{aligned}
F_x^\alpha&=\mathbb E[M_{\mathbf X}^\alpha\mid r_0,X_i=x],\\
H_y^\gamma&=\mathbb E[N_{\mathbf Y}^\gamma\mid r_0,Y_i=y],\\
F_y^\alpha&=\sum_x\mu(x\mid y)F_x^\alpha,\\
H_x^\gamma&=\sum_y\mu(y\mid x)H_y^\gamma .
\end{aligned}
\]
They also depend on \(i\) and \(r_0\), which are suppressed. Given \((r_0,X_i=x,Y_i=y)\), the unrevealed questions \(X_{>i}\) and \(Y_{<i}\) are independent, with laws \(\prod_{j>i}\mu(\cdot\mid Y_j)\) and \(\prod_{j<i}\mu(\cdot\mid X_j)\) that do not depend on \((x,y)\). Hence Alice's average given \((r_0,X_i=x,Y_i=y)\) is \(F_x^\alpha\), and her average given \((r_0,Y_i=y)\) is \(F_y^\alpha\); likewise for Bob. Since \(\Omega_{i-1}=(r_0,Y_i)\) and \(\Omega_i=(r_0,X_i)\),
\[
\begin{aligned}
&F_{i-1}^\alpha=F_y^\alpha,\ H_{i-1}^\gamma=H_y^\gamma\\
&\qquad\text{at }Y_i=y,\\
&F_i^\alpha=F_x^\alpha,\ H_i^\gamma=H_x^\gamma\\
&\qquad\text{at }X_i=x .
\end{aligned} \tag{1.2}
\]

## 2. The conditional vector and its measurements

Apply Lemma 1.1(3) of [A common purification of effects](a-common-purification-of-effects.md) to the finitely many effects \(F_x^\alpha,F_y^\alpha\), over all modes, values of \(r_0\), answer strings and questions of positive marginal probability: the maps \(\mathcal F_T\) take values in one finite-dimensional space \(\mathcal K_A\). Do the same for the effects \(H_y^\gamma,H_x^\gamma\), with a space \(\mathcal K_B\).

A *transcript* for mode \(i\) is \(r=(r_0,\alpha,\gamma)\), with \(r_0\) of positive probability; its weight is \(w_i(r)=\nu_i(r_0)\,\theta(r)\), where \(\theta(r)\) is the mask at \((x_C,y_C)\) from \(r_0\). The weights use counting measure on answer strings, do not depend on the fresh pair, and sum to at most \(d_C\). Put
\[
\begin{aligned}
&\Psi_{xy}^r=(\mathcal F_{F_x^\alpha}\otimes\mathcal F_{H_y^\gamma})\psi\in\mathcal K_A\otimes\mathcal K_B,\\
&p_{xy}^r=\|\Psi_{xy}^r\|^2=\chi(F_x^\alpha,H_y^\gamma),
\end{aligned}
\]
the last identity by Corollary 2.2 of that lesson. For an answer \(a\) and the coordinate \(i\), let \(M_{\mathbf x}^{\alpha,a}\) be the sum of \(M_{\mathbf x}^{\mathbf a}\) over \(\mathbf a\) with \(a_C=\alpha\) and \(a_i=a\), and similarly \(N_{\mathbf y}^{\gamma,b}\). The *fine effects*
\[
\begin{aligned}
&G_x^{\alpha,a}=\mathbb E[M_{\mathbf X}^{\alpha,a}\mid r_0,X_i=x],\\
&K_y^{\gamma,b}=\mathbb E[N_{\mathbf Y}^{\gamma,b}\mid r_0,Y_i=y]
\end{aligned}
\]
are positive with \(\sum_aG_x^{\alpha,a}=F_x^\alpha\) and \(\sum_bK_y^{\gamma,b}=H_y^\gamma\). Lemma 2.1 of that lesson gives POVMs \((\widetilde M_{r,x}^a)_a\) on \(\mathcal K_A\) and \((\widetilde N_{r,y}^b)_b\) on \(\mathcal K_B\), depending on the mode, with
\[
\begin{aligned}
&\mathcal F_{F_x^\alpha}^*\widetilde M_{r,x}^a\mathcal F_{F_x^\alpha}=G_x^{\alpha,a},\\
&\mathcal F_{H_y^\gamma}^*\widetilde N_{r,y}^b\mathcal F_{H_y^\gamma}=K_y^{\gamma,b} .
\end{aligned}
\]
Alice's measurement depends only on \((i,r,x)\) and Bob's only on \((i,r,y)\). Questions of zero marginal probability never occur.

**Lemma 2.1** (exact conditional laws). For every mode \(i\), transcript \(r=(r_0,\alpha,\gamma)\), fresh pair \((x,y)\) and answers \((a,b)\),
\[
\begin{aligned}
&\Pr\bigl(E_C,r,X_i=x,Y_i=y,\\
&\qquad A_i=a,B_i=b\bigr)\\
&=w_i(r)\,\mu(x,y)\\
&\cdot\langle\Psi_{xy}^r,(\widetilde M_{r,x}^a\otimes\widetilde N_{r,y}^b)\Psi_{xy}^r\rangle
\end{aligned} \tag{2.1}
\]
Here the event \(r\) means that \(r_0\) takes this value and the tested answers are \((\alpha,\gamma)\). In particular the law of \((r,X_i,Y_i)\) given \(E_C\) is
\[
\begin{aligned}
&\lambda_i(r,x,y)\\
&\quad=\frac{w_i(r)\,\mu(x,y)\,p_{xy}^r}p,
\end{aligned} \tag{2.2}
\]
and with \(W_{i,r,x,y}=\sum_{a,b}V(x,y,a,b)\,\widetilde M_{r,x}^a\otimes\widetilde N_{r,y}^b\),
\[
\begin{aligned}
&\Pr(I_i=1\mid E_C)\\
&\ =\frac1p\sum_{r,x,y}w_i(r)\mu(x,y)\\
&\qquad\cdot\langle\Psi_{xy}^r,W_{i,r,x,y}\Psi_{xy}^r\rangle .
\end{aligned} \tag{2.3}
\]

*Proof.* Given \((r_0,X_i=x,Y_i=y)\), the strings \(\mathbf X\) and \(\mathbf Y\) are independent and Alice's conditional average does not depend on \(y\), nor Bob's on \(x\) (Section 1). So the probability that the tested answers are \((\alpha,\gamma)\) and the answers at \(i\) are \((a,b)\), given these questions, is \(\chi(G_x^{\alpha,a},K_y^{\gamma,b})\). When \(\theta(r)=1\) these tested answers win every tested coordinate, so this event lies in \(E_C\); when \(\theta(r)=0\) it is disjoint from \(E_C\). Multiplying by \(\Pr(r_0,X_i=x,Y_i=y)=\nu_i(r_0)\mu(x,y)\) and applying Corollary 2.2 of the previous lesson gives (2.1). Summing over \((a,b)\) gives (2.2), and summing \(V(x,y,a,b)\) times (2.1) gives (2.3). \(\square\)

The transcript is a tool of the analysis, not information given to the players: a one-game strategy must use a shared resource independent of the fresh questions. The next lesson builds such strategies.

## 3. Local descriptions and the entropy telescope

The vector \(\Psi_{xy}^r\) depends on both fresh questions. Replacing one player's effect by its average over the other player's question gives vectors described by one question:
\[
\begin{aligned}
&\Psi_x^r=(\mathcal F_{F_x^\alpha}\otimes\mathcal F_{H_x^\gamma})\psi,\\
&\Psi_y^r=(\mathcal F_{F_y^\alpha}\otimes\mathcal F_{H_y^\gamma})\psi .
\end{aligned}
\]
The first is determined by \((i,r,x)\), the second by \((i,r,y)\), and both lie in \(\mathcal K_A\otimes\mathcal K_B\). With \(\mathbb E_{\nu_i\mu}\) denoting \(\sum_{r_0}\nu_i(r_0)\sum_{x,y}\mu(x,y)\), the averages defining \(F_y^\alpha\) and \(H_x^\gamma\) and (2.2) give
\[
\begin{aligned}
p&=\mathbb E_{\nu_i\mu}\sum_{\alpha,\gamma}\theta\,\|\Psi_{xy}^r\|^2\\
&=\mathbb E_{\nu_i\mu}\sum_{\alpha,\gamma}\theta\,\|\Psi_x^r\|^2\\
&=\mathbb E_{\nu_i\mu}\sum_{\alpha,\gamma}\theta\,\|\Psi_y^r\|^2 .
\end{aligned} \tag{3.1}
\]
Define the errors at mode \(i\):
\[
\begin{gathered}
e_A(i)=\mathbb E_{\nu_i\mu}\sum_{\alpha,\gamma}\theta\,\|\Psi_{xy}^r-\Psi_y^r\|^2,\\
e_B(i)=\mathbb E_{\nu_i\mu}\sum_{\alpha,\gamma}\theta\,\|\Psi_{xy}^r-\Psi_x^r\|^2 .
\end{gathered}
\]
In \(e_A\) Alice's effect changes and the comparison vector \(\Psi_y^r\) is Bob's description; in \(e_B\) Bob's effect changes and \(\Psi_x^r\) is Alice's.

**Lemma 3.1** (mixed exposure; [OpenAI-TR, Lemma 4.1]). For \(i\) uniform on \(\{1,\dots,m\}\),
\[
\mathbb E_i\,e_A(i)\le p\tau,\qquad\mathbb E_i\,e_B(i)\le p\tau .
\]
The ordering of the untested coordinates is arbitrary, and \(\mu\) may have zero entries and disconnected support.

*Proof.* With \(f(t)=t\log t\) and \(h_0(t)=-t\log t\), define for \(0\le j\le m\)
\[
\begin{aligned}
U_j&=\mathbb E_{\Omega_j}\sum_{\alpha,\gamma}\theta\,\chi\bigl(f(F_j^\alpha),H_j^\gamma\bigr),\\
Z_j&=\mathbb E_{\Omega_j}\sum_{\alpha,\gamma}\theta\,\chi\bigl(F_j^\alpha,f(H_j^\gamma)\bigr).
\end{aligned}
\]

*Range.* Since \(f(T)\preceq0\) for effects and \(\chi(\cdot,H)\) is a positive functional for \(H\succeq0\), \(U_j,Z_j\le0\). For a lower bound fix a flag and \((\alpha,\gamma)\), and put \(F=F_j^\alpha\), \(H=H_j^\gamma\), \(g=\chi(I,H)\le1\) and \(h=\chi(F,H)\). Writing \(F=\sum_k\lambda_kP_k\) spectrally, the numbers \(\chi(P_k,H)\ge0\) sum to \(g\), so concavity of \(h_0\) gives
\[
\begin{aligned}
&-\chi(f(F),H)=\sum_k\chi(P_k,H)h_0(\lambda_k)\\
&\quad\le g\,h_0(h/g)=h\log\frac gh\le h_0(h),
\end{aligned}
\]
with value \(0\) when \(g=0\). Since \(\theta\in\{0,1\}\) and \(h_0(0)=0\), concavity again, applied to the average over the flag and the \(d_C\) pairs \((\alpha,\gamma)\), and (1.1) give
\[
\begin{aligned}
-U_j&\le\mathbb E\sum_{\alpha,\gamma}h_0(\theta h)\\
&\le d_C\,h_0\Bigl(\frac p{d_C}\Bigr)=pL .
\end{aligned}
\]
The same argument with the players exchanged bounds \(-Z_j\le pL\). So \(-pL\le U_j,Z_j\le0\).

*One step.* With the entropy gaps \(\Delta_y^\alpha=\sum_x\mu(x\mid y)f(F_x^\alpha)-f(F_y^\alpha)\) and \(\Delta_x^\gamma=\sum_y\mu(y\mid x)f(H_y^\gamma)-f(H_x^\gamma)\) of the averages defining \(F_y^\alpha\) and \(H_x^\gamma\), (1.2) gives
\[
\begin{aligned}
&U_i-U_{i-1}\\
&\quad=\mathbb E_{\nu_i}\sum_y\mu_Y(y)\sum_{\alpha,\gamma}\theta\,\chi(\Delta_y^\alpha,H_y^\gamma),\\
&Z_{i-1}-Z_i\\
&\quad=\mathbb E_{\nu_i}\sum_x\mu_X(x)\sum_{\alpha,\gamma}\theta\,\chi(F_x^\alpha,\Delta_x^\gamma).
\end{aligned}
\]
For the first, \(U_i\) is an average over \((r_0,X_i)\) of \(\chi(f(F_x^\alpha),H_x^\gamma)\), and linearity in the second argument with \(H_x^\gamma=\sum_y\mu(y\mid x)H_y^\gamma\) rewrites it as \(\mathbb E_{\nu_i}\sum_{x,y}\mu(x,y)\sum\theta\chi(f(F_x^\alpha),H_y^\gamma)\); \(U_{i-1}\) is the average over \((r_0,Y_i)\) of \(\chi(f(F_y^\alpha),H_y^\gamma)\). The second is analogous.

Fix \(r_0,y,\alpha,\gamma\) and apply the estimate (1.1) of the previous lesson to the effects \(F_x^\alpha\) with probabilities \(\mu(x\mid y)\) and average \(F_y^\alpha\), with vectors in \(\mathcal H_A\otimes\mathcal H_B\) and the operators acting on the first factor. Pairing with \(\mathcal F_{H_y^\gamma}^*\mathcal F_{H_y^\gamma}=H_y^\gamma\) on the second factor in the state \(\psi\),
\[
\sum_x\mu(x\mid y)\|\Psi_{xy}^r-\Psi_y^r\|^2\le\chi\bigl(\Delta_y^\alpha,H_y^\gamma\bigr).
\]
Here \(\|\Psi_{xy}^r-\Psi_y^r\|^2=\chi(D^*D,H_y^\gamma)\) with \(D=\mathcal F_{F_x^\alpha}-\mathcal F_{F_y^\alpha}\), and (1.1) there holds as an operator inequality tested against every vector, hence also against \(H_y^\gamma\) in the state \(\psi\). Averaging gives \(e_A(i)\le U_i-U_{i-1}\); in the same way \(e_B(i)\le Z_{i-1}-Z_i\).

*Telescope.* Summing over \(i\), \(\sum_ie_A(i)\le U_m-U_0\le pL\) and \(\sum_ie_B(i)\le Z_0-Z_m\le pL\). Divide by \(m\) and use \(L=m\tau\). \(\square\)

The construction follows the weighted reveal argument of Chapter 6 of [OpenAI-TA], adapted to a fixed ordering of the untested coordinates.

## 4. The drift of the questions

Conditioning on \(E_C\) changes the law of the questions at the untested coordinates; one-game strategies, however, receive questions with the law \(\mu\). The following bound is used for the components of the question support in the next lesson.

**Lemma 4.1** (drift; compare [OpenAI-TR, Lemma 4.2]). Let \(Z_1,\dots,Z_m\) be independent random variables with values in a finite set and common law \(\nu\), defined on a probability space with an event \(E\) of probability \(p>0\). Let \(P_i\) be the law of \(Z_i\) given \(E\). Then
\[
\frac1m\sum_{i=1}^m\operatorname{TV}(P_i,\nu)\le\sqrt{\frac{\log(1/p)}{2m}} .
\]

*Proof.* Let \(P\) be the law of \((Z_1,\dots,Z_m)\) given \(E\). Its density with respect to \(\nu^{\otimes m}\) is \(\Pr(E\mid Z=z)/p\le1/p\), so the relative entropy satisfies \(D(P\Vert\nu^{\otimes m})\le\log(1/p)\). Expanding the logarithm of the product,
\[
\begin{aligned}
&D(P\Vert\nu^{\otimes m})\\
&\quad=\sum_iH(P_i)-H(P)+\sum_iD(P_i\Vert\nu)\\
&\quad\ge\sum_iD(P_i\Vert\nu),
\end{aligned}
\]
because \(H(P)\le\sum_iH(P_i)\) by the chain rule and the fact that conditioning does not increase entropy ([Entropy of finite random variables](course:the-gaussian-moat-problem/entropy-of-finite-random-variables), Propositions 2.2 and 2.3). Pinsker's inequality (Theorem 5.3 there) gives \(\operatorname{TV}(P_i,\nu)\le\sqrt{D(P_i\Vert\nu)/2}\), and by the Cauchy–Schwarz inequality
\[
\begin{aligned}
&\frac1m\sum_i\operatorname{TV}(P_i,\nu)\\
&\quad\le\Bigl(\frac1{2m}\sum_iD(P_i\Vert\nu)\Bigr)^{1/2}\\
&\quad\le\sqrt{\frac{\log(1/p)}{2m}} .\qquad\square
\end{aligned}
\]

Applied to the fresh pairs \(Z_i=(X_i,Y_i)\) at the untested coordinates and \(E=E_C\), it shows that the question law at an average untested coordinate is within \(\sqrt{\tau/2}\) of \(\mu\) in total variation, since \(\log(1/p)\le L=m\tau\).

## 5. Exercises

**5.1.** In Lemma 1.1, give an example of a distribution \(\mu\) and a flag for which \(X_i\) and \(Y_i\) at a single untested coordinate are not independent given everything else revealed, and explain why Lemma 1.1 is still true.

**5.2.** Show that \(\sum_{\alpha,\gamma}w_i(r)\le d_C\sum_{r_0}\nu_i(r_0)=d_C\).

**5.3.** Prove \(d_C\,h_0(p/d_C)=pL\).

**5.4.** Let \(C=\varnothing\). Show that \(p=1\), \(L=0\), and that the vectors \(\Psi_{xy}^r\), \(\Psi_x^r\), \(\Psi_y^r\) all coincide.

**5.5.** Let \(m=1\), let \(\nu\) be uniform on \(\{0,1\}\), and let \(E\) have conditional probability \(\frac12+\eta\) given \(Z_1=1\) and \(\frac12-\eta\) given \(Z_1=0\), where \(0<\eta<\frac12\). Compute \(p\), \(\operatorname{TV}(P_1,\nu)\) and \(D(P_1\Vert\nu)\), and compare with Pinsker's inequality as \(\eta\to0\).

## 6. Solutions

**5.1.** At an untested coordinate \(l\le j\) only \(X_l\) is revealed and \(Y_l\) has law \(\mu(\cdot\mid X_l)\); if \(\mu\) is supported on the diagonal, \(Y_l\) is then determined. Lemma 1.1 concerns the unrevealed questions, which never include both questions of one coordinate, so their joint law is a product.

**5.2.** \(\theta\le1\) and there are \(|\mathcal A|^{|C|}|\mathcal B|^{|C|}=d_C\) pairs \((\alpha,\gamma)\).

**5.3.** \(d_C\cdot\frac p{d_C}\log\frac{d_C}p=p\log\frac{d_C}p\).

**5.4.** \(E_\varnothing\) is the sure event and \(d_\varnothing=1\), so \(p=1\) and \(L=0\). The coarse-grained effects are \(M_{\mathbf x}^\varnothing=\sum_{\mathbf a}M_{\mathbf x}^{\mathbf a}=I\) and \(N_{\mathbf y}^\varnothing=I\), so every averaged effect is the identity and the three vectors equal \((\mathcal F_I\otimes\mathcal F_I)\psi\).

**5.5.** \(p=\frac12(\frac12+\eta)+\frac12(\frac12-\eta)=\frac12\), \(P_1(1)=\frac12+\eta\), so \(\operatorname{TV}(P_1,\nu)=\eta\). Further
\[
\begin{aligned}
D(P_1\Vert\nu)&=(\tfrac12+\eta)\log(1+2\eta)\\
&\quad+(\tfrac12-\eta)\log(1-2\eta)\\
&=2\eta^2+O(\eta^4),
\end{aligned}
\]
so Pinsker's bound \(D\ge2\operatorname{TV}^2=2\eta^2\) is sharp in the limit. Here \(\log(1/p)=\log2\), and the bound of Lemma 4.1, \(\sqrt{\log2/2}\approx0.59\), holds with room to spare: the relative entropy \(D(P_1\Vert\nu)\) can be much smaller than \(\log(1/p)\).

## References

- [OpenAI-TR] OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, OpenAI Math Release preprint, 25 September 2026, Section 4 (Lemmas 4.1 and 4.2). https://github.com/openai/math/tree/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
- [OpenAI-TA] OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, report, updated 6 August 2026, Chapter 6, Section 4. https://cdn.openai.com/pdf/ten-proofs-oai.pdf

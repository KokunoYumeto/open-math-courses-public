# A common modular action

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson produced, for a prepared pair \(M,N\) and every time \(t\), a unitary \(n_t\) normalizing \(M\) and close to \(\Delta_N^{it}\Delta_M^{-it}\). These unitaries are chosen one time at a time: they need not be measurable in \(t\), and they need not multiply correctly. This lesson corrects their multiplication law inside the normalizer group of \(M\) (Lemma 2.1), by an averaging iteration with an invariant mean on the real numbers as a discrete group. An intertwining argument then gives a single unitary \(q\) near the identity such that the modular group of \(N\) leaves \(qMq^*\) invariant (Theorem 3.1). The modular group of \(N\) itself is unchanged, and this is what makes the crossed products of the next lesson comparable [OpenAI-289, Section 7].

We use: [Close operator algebras](close-operator-algebras.md) (Lemma 1.5); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Proposition 2.1 and Lemma 2.2, the invariant mean \(m\) on \(\mathbb R_d\) and operator means \(m_s\)); [Infinitesimal normalizers of type III factors](infinitesimal-normalizers-of-type-iii-factors.md) (Lemma 4.1 and the groups \(\mathcal G_P\subseteq\mathcal N_P\)); [Near normalizers at every time](near-normalizers-at-every-time.md) (Theorem 1.1).

## 1. Normalizers and their small corrections

For a factor \(P\subseteq B(H)\), \(\mathcal N_P\) is the group of unitaries \(v\) with \(vPv^*=P\). It is closed in operator norm (Exercise 5.1 of the lesson on infinitesimal normalizers). By Lemma 4.1 of that lesson, every \(v\in\mathcal N_P\) with \(\|v-1\|<1/6\) factors as \(v=ab'\) with \(a\in\mathcal U(P)\), \(b'\in\mathcal U(P')\) and \(\|a-1\|+\|b'-1\|\le10\|v-1\|\). This local product structure lets an average of normalizers be corrected back into the normalizer group: averages are taken separately in \(P\) and in \(P'\).

## 2. Correction of normalizer representations

**Lemma 2.1** (correction of normalizer representations). Let \(P\subseteq B(H)\) be a factor and \(v_t\in\mathcal N_P\), \(t\in\mathbb R\), any family with
\[
e:=\sup_{t,s\in\mathbb R}\|v_tv_s-v_{t+s}\|<\frac1{7208}.
\]
There is a representation \(z\) of the discrete group \(\mathbb R_d\) with values in \(\mathcal N_P\) and
\[
\sup_t\|z_t-v_t\|\le4e .
\]

**Proof.** *Averaging.* Put
\[
F_t(s)=v_{t+s}v_s^*,\qquad A_t=m_sF_t(s).
\]
Each \(F_t(s)\) is a normalizer with \(\|F_t(s)-v_t\|\le e\), hence \(\|A_t-v_t\|\le e\) by Lemma 2.2(3) of the averaging lesson. The exact factorization \(F_{t+r}(s)=F_t(r+s)F_r(s)\), translation invariance and the module property give
\[
\begin{gathered}
A_{t+r}-A_tA_r\\
=m_s\bigl[(F_t(r+s)-A_t)(F_r(s)-A_r)\bigr],
\end{gathered}
\]
as one checks by expanding the right side; the centered factors have norm at most \(2e\), so \(\|A_{t+r}-A_tA_r\|\le4e^2\). Likewise \(1-A_t^*A_t=m_s|F_t(s)-A_t|^2\) has norm at most \(4e^2\).

*Staying among normalizers.* Taking polar parts of \(A_t\) in \(B(H)\) would leave \(\mathcal N_P\). Instead, factor \(F_t(s)v_t^*=a_{t,s}b'_{t,s}\) by Lemma 4.1 of the infinitesimal lesson: \(F_t(s)v_t^*\) is a normalizer within \(e<1/6\) of \(1\), so \(a_{t,s}\in\mathcal U(P)\), \(b'_{t,s}\in\mathcal U(P')\) and \(\|a_{t,s}-1\|,\|b'_{t,s}-1\|\le10e\). These choices need not depend measurably or continuously on anything. The averages \(a_t=m_sa_{t,s}\) and \(b'_t=m_sb'_{t,s}\) lie in \(P\) and \(P'\) by Lemma 2.2(2) of the averaging lesson, and are within \(10e\) of \(1\). Expanding the centered product \((a_{t,s}-a_t)(b'_{t,s}-b'_t)\) under the mean,
\[
\begin{gathered}
\|m_s(a_{t,s}b'_{t,s})-a_tb'_t\|\le(20e)^2,\\
\|1-a_t^*a_t\|,\ \|1-b_t'^*b'_t\|\le(20e)^2 .
\end{gathered}
\]
Since \(10e<1\), \(a_t\) and \(b'_t\) are invertible, and their unitary polar parts \(\hat a_t\in P\), \(\hat b'_t\in P'\) satisfy \(\|\hat a_t-a_t\|=\|1-|a_t|\|\le400e^2\) and the same for \(b'_t\). Put
\[
w_t=\hat a_t\hat b'_tv_t\in\mathcal N_P .
\]
Since \(A_t=m_s(a_{t,s}b'_{t,s})v_t\) by the module property, \(\|w_t-A_t\|\le1200e^2\). Hence
\[
\begin{gathered}
\|w_t-v_t\|\le e+1200e^2,\\
\|w_tw_r-w_{t+r}\|\le3604e^2,
\end{gathered}
\]
the second by comparing \(w_tw_r\) with \(A_tA_r\) (using \(\|A_t\|\le1\) and \(\|w_r\|=1\)), \(A_tA_r\) with \(A_{t+r}\), and \(A_{t+r}\) with \(w_{t+r}\).

*Iteration.* Repeat with \(w\) in place of \(v\). With \(e_0=e\) and \(e_{j+1}\le3604e_j^2\), the bound \(e_j<1/7208\) gives \(e_{j+1}\le e_j/2\), and each displacement \(e_j+1200e_j^2\) is at most \(2e_j\). The families converge uniformly in \(t\), in operator norm, to unitaries \(z_t\) with \(z_tz_r=z_{t+r}\), and \(\|z_t-v_t\|\le\sum_j2e_j\le4e\). Since \(\mathcal N_P\) is norm closed, \(z_t\in\mathcal N_P\). The multiplication law gives \(z_0^2=z_0\), so \(z_0=1\), and \(z_{-t}=z_t^*\). \(\square\)

## 3. The common modular action

**Theorem 3.1** (a common modular action). There are absolute constants \(c_{\rm mod}>0\) and \(C_{\rm mod}\) with the following property. Let \(M,N\subseteq B(H)\) be a prepared pair with \(d_{\rm cb}(M,N)<\gamma<c_{\rm mod}\). There is a unitary \(q\in B(H)\) with
\[
\begin{gathered}
\|q-1\|\le C_{\rm mod}\gamma,\\
d_{\rm cb}(qMq^*,N)\le C_{\rm mod}\gamma,
\end{gathered}
\]
\[
\Delta_N^{it}(qMq^*)\Delta_N^{-it}=qMq^*\qquad(t\in\mathbb R).
\]
The algebra \(N\) and its modular group are unchanged.

**Proof.** Put \(U_t=\Delta_N^{it}\). Theorem 1.1 of the previous lesson gives normalizers \(n_t\in\mathcal N_M\) with \(\|n_t-\Delta_N^{it}\Delta_M^{-it}\|\le C\gamma\). Since \(\Delta_M^{it}\) normalizes \(M\), the unitaries \(v_t=n_t\Delta_M^{it}\) lie in \(\mathcal N_M\), and \(\|v_t-U_t\|\le C\gamma\). As \(U\) is a representation, \(\sup_{t,s}\|v_tv_s-v_{t+s}\|\le3C\gamma\). For \(\gamma\) below an absolute threshold, Lemma 2.1 gives a representation \(z\) of \(\mathbb R_d\) in \(\mathcal N_M\) with \(\|z_t-U_t\|\le C'\gamma\) for all \(t\), where \(C'=13C\).

*Intertwining.* Put \(T=m_t\,z_tU_t^*\). It is within \(C'\gamma\) of \(1\), hence invertible for small \(\gamma\). For every \(s\), translation invariance and the two multiplication laws give
\[
z_sTU_s^*=m_t\,z_{s+t}U_{s+t}^*=T,
\]
so \(z_sT=TU_s\). Taking adjoints, \(T^*z_s=U_sT^*\), so \(U_sT^*T=T^*z_sT=T^*TU_s\): the operator \(|T|\) commutes with every \(U_s\). Its polar part \(w=T|T|^{-1}\) therefore satisfies \(z_sw=wU_s\), and \(\|w-1\|\le2\|T-1\|\le2C'\gamma\). In particular \(z_s=wU_sw^*\), so \(z\) is strongly continuous, although the \(n_t\) were chosen without any regularity.

*Conclusion.* Put \(q=w^*\). Since \(z_s\) normalizes \(M\) and \(U_s=w^*z_sw\),
\[
\begin{aligned}
&U_s(qMq^*)U_s^*\\
&\quad =w^*z_s(ww^*)M(ww^*)z_s^*w\\
&\quad =w^*Mw=qMq^* .
\end{aligned}
\]
By Lemma 1.5 of [Close operator algebras](close-operator-algebras.md), \(d_{\rm cb}(qMq^*,N)\le\gamma+2\|q-1\|\). Enlarging the constant and decreasing the threshold to meet the finitely many absolute smallness conditions proves the theorem. \(\square\)

## 4. Exercises

**Exercise 4.1.** Check the factorization \(F_{t+r}(s)=F_t(r+s)F_r(s)\) and the identity for \(A_{t+r}-A_tA_r\).

**Exercise 4.2.** Show that if \(v\) is an exact representation of \(\mathbb R_d\) in \(\mathcal N_P\), then the construction in the proof of Lemma 2.1 returns \(w_t=v_t\) after one step, provided the factorizations are chosen as \(a_{t,s}=b'_{t,s}=1\).

**Exercise 4.3.** Let \(U\) be a strongly continuous unitary group and \(z_s=wU_sw^*\) with \(w\) unitary. Show that \(z\) is strongly continuous.

**Exercise 4.4.** In the proof of Theorem 3.1, show that \(T\) commutes with every operator commuting with all \(z_s\) and all \(U_s\).

**Exercise 4.5.** Why can the unitary \(w\) not be obtained by averaging \(z_tU_t^*\) over a probability measure on \(\mathbb R\) without further information on \(t\mapsto z_t\)?

## 5. Solutions

**Solution 4.1.** \(F_t(r+s)F_r(s)\)\(=v_{t+r+s}v_{r+s}^*v_{r+s}v_s^*=v_{t+r+s}v_s^*\)\(=F_{t+r}(s)\). Expanding \(m_s[(F_t(r+s)-A_t)(F_r(s)-A_r)]\) gives \(m_s[F_t(r+s)F_r(s)]-A_tA_r\)\(-A_tA_r+A_tA_r\), using \(m_sF_t(r+s)=A_t\) and the module property; the first term is \(A_{t+r}\).

**Solution 4.2.** Then \(F_t(s)=v_t\) for all \(s\), \(A_t=v_t\), and with trivial factorizations \(a_t=b'_t=1\), so \(w_t=v_t\).

**Solution 4.3.** \(\|(z_s-z_{s_0})\xi\|=\|(U_s-U_{s_0})w^*\xi\|\).

**Solution 4.4.** If \(c\) commutes with every \(z_t\) and \(U_t\), it commutes with \(z_tU_t^*\), and by the module property of the operator mean with \(T\).

**Solution 4.5.** Averaging against a measure requires the integrand \(t\mapsto z_tU_t^*\) to be measurable, and the \(z_t\) are produced by choices at each time separately. The invariant mean on \(\mathbb R_d\) needs no measurability.

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [BOT] M. Burger, N. Ozawa, A. Thom, On Ulam stability, Israel Journal of Mathematics 193 (2013), 109–129 (the averaging and polar decomposition iteration for approximate representations). https://arxiv.org/abs/1010.0565

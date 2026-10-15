# Walsh norms and moment lifts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson collects the tools for the decay theorem of [Type, cotype and K-convexity](type-cotype-and-k-convexity.md) (Theorem 2.3 there). Walsh norms of an operator are nonincreasing in the dimension, invariant under amplification, and decay like \(2^{-n/2}\) for each fixed finite-rank operator (Lemma 1.1). Cotype of a fixed length passes to finite \(L_2\) sums (Section 2). Kahane's inequality, in the form \(\|S\|_{L_2}\le24\|S\|_{L_1}\) for Rademacher sums, is proved with a stopping time (Lemma 2.1). Together with a quotient-duality principle it gives *moment lifts*: bounded families indexed by signs whose first moments are prescribed vectors (Lemma 3.2).

- Walsh norms (Lemma 1.1).
- Fixed-length cotype and Kahane's inequality (Section 2, Lemma 2.1).
- Quotient duality and moment lifts (Lemmas 3.1 and 3.2).

The lesson follows [OpenAI-CC, Section 2]. Banach spaces are real, \(B_Y\) is the closed unit ball of \(Y\), averages over finite sets are uniform, and different averaging variables are independent. For a finite probability space \(\Omega\), \(L_p(\Omega;Y)\) has the probability-normalized norm, while \(\ell_2^m(Y)\) is \(Y^m\) with the norm \((\sum_{i=1}^m\|y_i\|^2)^{1/2}\). With the expectation pairing, for finite \(\Omega\),
\[
\begin{gathered}
L_2(\Omega;Y)^*=L_2(\Omega;Y^*),\\
L_1(\Omega;Y)^*=L_\infty(\Omega;Y^*),\\
L_\infty(\Omega;Y)^*=L_1(\Omega;Y^*),
\end{gathered}
\]
isometrically, and \(\ell_2^m(Y)^*=\ell_2^m(Y^*)\) with the pairing \(\sum_i\langle y_i,y_i^*\rangle\); the proofs are those of Lemma 3.1 of the previous lesson.

## 1. Walsh norms

Recall from the previous lesson that \(V_n=\mathbb F_2^n\), \(\chi(u,v)=(-1)^{u\cdot v}\), and for \(T\colon G\to F\)
\[
\begin{gathered}
(W^T_nx)(v)=\mathbb E_{u\in V_n}\chi(u,v)\,Tx(u),\\
w_n(T)=\|W^T_n\|,
\end{gathered}
\]
the norm from \(L_2(V_n;G)\) to \(L_2(V_n;F)\). By duality,
\[
\begin{aligned}
&w_n(T)=\sup\Bigl|\mathbb E_{u,v\in V_n}\\
&\qquad\chi(u,v)\,y_v(Tx_u)\Bigr| ,
\end{aligned} \tag{1.1}
\]
the supremum over \(x_u\in G\) and \(y_v\in F^*\) with \(\mathbb E_u\|x_u\|^2\le1\) and \(\mathbb E_v\|y_v\|^2\le1\).

**Lemma 1.1** (Walsh norms; [OpenAI-CC, Lemma 2.1]). Let \(T,A,B\colon G\to F\) be bounded.

1. \(2^{-n/2}\|T\|\le w_n(T)\le\|T\|\), and \(w_n(T)\) is nonincreasing in \(n\).
2. If \(\Omega\) is finite and \(T_\Omega\colon L_2(\Omega;G)\to L_2(\Omega;F)\) applies \(T\) pointwise, then \(w_n(T_\Omega)=w_n(T)\).
3. If \(T\) has finite rank, there is \(D_T<\infty\) with \(w_n(T)\le D_T2^{-n/2}\) for all \(n\ge0\).
4. \(|w_n(A)-w_n(B)|\le\|A-B\|\).

*Proof.* (1) For every \(v\), \(\|(W^T_nx)(v)\|\le\mathbb E_u\|Tx(u)\|\le\|T\|\,\|x\|_{L_2}\), by the Cauchy–Schwarz inequality; so \(w_n(T)\le\|T\|\). For the lower bound take \(x\) supported at one point \(u_0\), with \(x(u_0)=2^{n/2}g\); then \(\|x\|_{L_2}=\|g\|\) and \((W^T_nx)(v)=2^{-n/2}\chi(u_0,v)Tg\), so \(\|W^T_nx\|_{L_2}=2^{-n/2}\|Tg\|\). For monotonicity write \(V_{n+j}=V_n\oplus V_j\). The transform \(W^T_{n+j}\) is the transform \(W^T_n\) in the first coordinate followed by the normalized Walsh transform with the identity of \(F\) in the second coordinate; the latter has norm at most \(1\) by the upper bound just proved. Averaging the squared estimates over the unused coordinate gives \(w_{n+j}(T)\le w_n(T)\).

(2) A function in \(L_2(V_n;L_2(\Omega;G))\) is a function on \(V_n\times\Omega\); for each fixed \(\omega\), \(W^{T_\Omega}_n\) acts as \(W^T_n\) on the slice. Averaging the squared estimates over \(\omega\) gives \(w_n(T_\Omega)\le w_n(T)\); inputs constant in \(\omega\) give the reverse inequality.

(3) The range \(T(G)\) is finite-dimensional; give it a Hilbert space norm \(\|\cdot\|_H\). All norms on a finite-dimensional space are equivalent, so \(T=BA\) with \(A=T\colon G\to H=(T(G),\|\cdot\|_H)\) and \(B\) the identity \(H\to F\), both bounded. The matrix \((2^{-n}\chi(u,v))_{u,v}\) is \(2^{-n/2}\) times an orthogonal matrix, so \(\|W^{\mathrm{Id}_H}_n\|=2^{-n/2}\), and \(W^T_n=BW^{\mathrm{Id}_H}_nA\) pointwise. Take \(D_T=\|A\|\|B\|\).

(4) \(W^A_n-W^B_n=W^{A-B}_n\); use the upper bound in (1) and the triangle inequality. \(\blacksquare\)

The constant \(D_T\) depends on \(T\); the point of the course is a decay bound that does not.

## 2. Fixed-length cotype and Kahane's inequality

For an integer \(m\ge1\), let \(c_m(Y)\) be the least constant with
\[
\begin{aligned}
&\Bigl(\sum_{i=1}^m\|y_i\|^2\Bigr)^{1/2}\le c_m(Y)\\
&\quad\cdot\Bigl(\mathbb E_\varepsilon\Bigl\|\sum_{i=1}^m\varepsilon_iy_i\Bigr\|^2\Bigr)^{1/2}.
\end{aligned} \tag{2.1}
\]
If \(C_q(Y)<\infty\), Hölder's inequality \(\sum_i\|y_i\|^2\le m^{1-2/q}(\sum_i\|y_i\|^q)^{2/q}\) gives
\[
c_m(Y)\le C_q(Y)\,m^{1/2-1/q}. \tag{2.2}
\]
Squaring (2.1) and averaging over \(\omega\) gives \(c_m(L_2(\Omega;Y))\le c_m(Y)\) for finite \(\Omega\).

**Lemma 2.1** (Kahane's inequality; [OpenAI-CC, Lemma 2.2]). For every finite Rademacher sum \(S=\sum_{i=1}^m\varepsilon_iz_i\) in a Banach space,
\[
(\mathbb E\|S\|^2)^{1/2}\le24\,\mathbb E\|S\| .
\]

*Proof.* Put \(M=\mathbb E\|S\|\) and \(b=\max_i\|z_i\|\). Since \(z_i=\mathbb E(\varepsilon_iS)\), \(b\le M\). If \(M=0\), then \(S=0\). Let \(S_j=\sum_{i\le j}\varepsilon_iz_i\) and \(R_j=S-S_j\).

*Two reflection estimates.* Fix \(u>0\), and let \(\tau\) be the first \(j\) with \(\|S_j\|>u\) (if any). On the event \(\{\tau=j\}\), which depends only on \(\varepsilon_1,\dots,\varepsilon_j\), at least one of \(\|S_j+R_j\|\) and \(\|S_j-R_j\|\) exceeds \(u\), because their average is at least \(\|S_j\|\). The remaining sum \(R_j\) is independent of \(\varepsilon_1,\dots,\varepsilon_j\) and has the same distribution as \(-R_j\). So \(\mathbb P(\tau=j,\ \|S\|>u)\ge\frac12\mathbb P(\tau=j)\), and summing over \(j\),
\[
\mathbb P(\tau\text{ exists})\le2\,\mathbb P(\|S\|>u).
\]
In the same way, since \(S_j\) is independent of \(R_j\) and symmetric, \(\mathbb P(\|R_j\|>v)\le2\,\mathbb P(\|S\|>v)\) for every \(j\) and \(v>0\).

*A product estimate.* If \(\|S\|>u+b+v\), then \(\tau\) exists, \(\|S_\tau\|\le u+b\) (as \(\|S_{\tau-1}\|\le u\)), and \(\|R_\tau\|>v\). Using the independence of \(\{\tau=j\}\) and \(R_j\),
\[
\begin{aligned}
&\mathbb P(\|S\|>u+b+v)\\
&\quad\le\sum_j\mathbb P(\tau=j)\,\mathbb P(\|R_j\|>v)\\
&\quad\le4\,\mathbb P(\|S\|>u)\,\mathbb P(\|S\|>v).
\end{aligned}
\]

*Tails.* Take \(u=8M\). By Markov's inequality \(\mathbb P(\|S\|>8M)\le1/8\), and with \(b\le M\),
for \(v>0\),
\[
\mathbb P(\|S\|>9M+v)\le\tfrac12\,\mathbb P(\|S\|>v).
\]
By induction \(\mathbb P(\|S\|>9jM)\le2^{-j}\) for \(j\ge0\). Hence
\[
\begin{aligned}
\mathbb E\|S\|^2&=\int_0^\infty2t\,\mathbb P(\|S\|>t)\,dt\\
&\le\sum_{j\ge0}2^{-j}\int_{9jM}^{9(j+1)M}2t\,dt\\
&=81M^2\sum_{j\ge0}(2j+1)2^{-j}\\
&=486M^2<24^2M^2 .
\end{aligned}
\]
\(\blacksquare\)

The inequality is the \(L_1\)-to-\(L_2\) case of Kahane's inequality ([Pis11, Theorem 8.1] gives the general form); the explicit constant \(24\) is all that is needed below.

## 3. Quotient duality and moment lifts

**Lemma 3.1** (quotient lifts). Let \(U\colon A\to B\) be a bounded linear surjection between Banach spaces with a bounded right inverse, and suppose \(\|U^*b^*\|\ge D^{-1}\|b^*\|\) for all \(b^*\in B^*\). Then every \(b\in B\) and every \(\theta>1\) admit \(a\in A\) with \(Ua=b\) and \(\|a\|\le\theta D\|b\|\).

*Proof.* Let \(Q\colon A\to A/\ker U\) be the quotient map and \(\hat U\colon A/\ker U\to B\) the induced bijection, \(\hat UQ=U\); its inverse is bounded, being \(Q\) composed with the right inverse. By the Hahn–Banach theorem ([Hahn–Banach, Baire and the basic theorems on Banach spaces](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces), Corollary 2.3), the quotient norm of \(\hat U^{-1}b\) is the supremum of \(|\phi(\hat U^{-1}b)|\) over functionals \(\phi\) of norm at most \(1\) on \(A/\ker U\). For such \(\phi\), put \(b^*=\phi\circ\hat U^{-1}\in B^*\). Then \(U^*b^*=\phi\circ Q\) has norm \(\|\phi\|\le1\), since \(Q\) maps the open unit ball of \(A\) onto that of the quotient; so \(\|b^*\|\le D\) and \(|\phi(\hat U^{-1}b)|=|b^*(b)|\le D\|b\|\). The coset \(\hat U^{-1}b\) therefore has a representative \(a\) with \(\|a\|\le\theta D\|b\|\), and \(Ua=b\). \(\blacksquare\)

**Lemma 3.2** (moment lifts; [OpenAI-CC, Lemma 2.3]). Suppose \(c_m(G^*)\le D_g\) and \(c_m(F)\le D_f\), with \(D_g,D_f\ge1\), and put
\[
\begin{gathered}
a=\frac1{48D_g\sqrt m},\\
b=\frac1{48D_f\sqrt m}.
\end{gathered} \tag{3.1}
\]

1. For \(x_1,\dots,x_m\in B_G\) there are \(P_\varepsilon\in B_G\), \(\varepsilon\in\{-1,1\}^m\), with \(\mathbb E_\varepsilon\varepsilon_iP_\varepsilon=ax_i\) for all \(i\).
2. For \(y_1,\dots,y_m\in B_{F^*}\) there are \(Z_\delta\in B_{F^*}\), \(\delta\in\{-1,1\}^m\), with \(\mathbb E_\delta\delta_jZ_\delta=by_j\) for all \(j\).

The same holds, with the same \(a\) and \(b\), for \(G\) and \(F\) replaced by finite \(L_2\) sums \(L_2(\Omega;G)\) and \(L_2(\Omega;F)\).

*Proof.* (1) The moment map \(U\colon L_\infty(\{-1,1\}^m;G)\to\ell_2^m(G)\), \(UP=(\mathbb E_\varepsilon\varepsilon_iP_\varepsilon)_i\), has the right inverse \((x_i)\mapsto\sum_i\varepsilon_ix_i\). Its adjoint sends \((z_i^*)\in\ell_2^m(G^*)\) to the function \(\varepsilon\mapsto\sum_i\varepsilon_iz_i^*\) in \(L_1(\{-1,1\}^m;G^*)\). By Lemma 2.1 and (2.1),
\[
\begin{aligned}
\Bigl\|\sum_i\varepsilon_iz_i^*\Bigr\|_{L_1(G^*)}&\ge\frac1{24D_g}\\
&\quad\cdot\Bigl(\sum_i\|z_i^*\|^2\Bigr)^{1/2}.
\end{aligned}
\]
By Lemma 3.1 with \(D=24D_g\) and \(\theta=2\), the tuple \((ax_i)\), of norm at most \(a\sqrt m\), has a lift \(P\) with \(\|P\|_{L_\infty}\le48D_ga\sqrt m=1\).

(2) The map \(V\colon\ell_2^m(F)\to L_1(\{-1,1\}^m;F)\), \(V(w_j)=\sum_j\delta_jw_j\), satisfies \(\|Vw\|_{L_1}\ge(24D_f)^{-1}\|w\|_{\ell_2^m(F)}\), by Lemma 2.1 and (2.1). The functional \(Vw\mapsto b\sum_jy_j(w_j)\) on the range of \(V\) is well defined and has norm at most \(b\sqrt m\cdot24D_f=1/2\). Extend it by the Hahn–Banach theorem to \(L_1(\{-1,1\}^m;F)\) with the same norm, and represent the extension by \(Z\in L_\infty(\{-1,1\}^m;F^*)\), \(\|Z\|_{L_\infty}\le1/2\). Testing on \(Vw\) with a single nonzero \(w_j\) gives \(\mathbb E_\delta\delta_jZ_\delta=by_j\).

For finite \(L_2\) sums, \(c_m(L_2(\Omega;F))\le c_m(F)\) by Section 2, and \(L_2(\Omega;G)^*=L_2(\Omega;G^*)\) with \(c_m(L_2(\Omega;G^*))\le c_m(G^*)\); the same proofs apply. \(\blacksquare\)

Only the positivity of \(a\) and \(b\), and the growth of \(ma\) and \(mb\) with \(m\) under cotype hypotheses, matter later.

## 4. Exercises

**4.1.** Show that \(w_1(\mathrm{Id}_{\ell_\infty^2})=1\), so that the upper bound of Lemma 1.1(1) is attained.

**4.2.** Show that \(c_m(\mathbb R)=1\) and \(c_m(\ell_\infty^m)\ge\sqrt m\).

**4.3.** Check the identity \(\sum_{j\ge0}(2j+1)2^{-j}=6\).

**4.4.** In Lemma 3.2(1), why is the lift taken in \(L_\infty\), not in \(L_2\)?

**4.5.** Show that the moment lift of Lemma 3.2(1) cannot exist for every \(m\) with \(a\) independent of \(m\) when \(G=\mathbb R\): compute \(\sum_i(\mathbb E_\varepsilon\varepsilon_iP_\varepsilon)^2\) for \(|P_\varepsilon|\le1\).

## 5. Solutions

**4.1.** On \(V_1=\{0,1\}\), take \(x_0=(1,1)\), \(x_1=(1,-1)\) in \(\ell_\infty^2\). Then \((Wx)(0)=\frac12(x_0+x_1)=(1,0)\) and \((Wx)(1)=\frac12(x_0-x_1)=(0,1)\), so \(\|Wx\|_{L_2}=1=\|x\|_{L_2}\).

**4.2.** For real numbers, \(\mathbb E(\sum_i\varepsilon_iy_i)^2=\sum_iy_i^2\). In \(\ell_\infty^m\), the unit vectors \(e_i\) have \(\|\sum_i\varepsilon_ie_i\|=1\) for every choice of signs, while \((\sum_i\|e_i\|^2)^{1/2}=\sqrt m\).

**4.3.** \(\sum_jj2^{-j}=2\) and \(\sum_j2^{-j}=2\), so the sum is \(4+2=6\).

**4.4.** The lifts are used as vectors of the unit ball, pointwise in \(\varepsilon\): the dual estimate is in \(L_1\), whose dual is \(L_\infty\).

**4.5.** By Bessel's inequality for the orthonormal functions \(\varepsilon_i\) in \(L_2(\{-1,1\}^m)\), \(\sum_i(\mathbb E\varepsilon_iP_\varepsilon)^2\le\mathbb EP^2\le1\). With \(x_i=1\) this forces \(ma^2\le1\), so \(a\le m^{-1/2}\).

## References

- [OpenAI-CC] OpenAI, *The cotype–cotype conjecture under the approximation property*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026
- [Pis11] G. Pisier, *Martingales in Banach spaces (in connection with type and cotype)*, IHP course notes, version of 9 February 2011, Theorem 8.1. https://webusers.imj-prg.fr/~gilles.pisier/ihp-pisier.pdf

# Type, cotype and K-convexity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Banach space is *\(K\)-convex* when the projection onto first-order Rademacher terms is bounded on vector-valued square-integrable functions on sign cubes. This course proves the theorem of [OpenAI-CC]: a nonzero real Banach space with the approximation property is \(K\)-convex if and only if both the space and its dual have finite Rademacher cotype, possibly with different exponents. Without the approximation property the statement is false.

This lesson gives the definitions, states the theorem, and proves the elementary implications. The core of the course is a decay theorem that is proved in full (Theorem 2.3): under the approximation property and the cotype hypotheses, normalized Walsh transforms of vector families decay, and the space contains no uniform copies of the spaces \(\ell_1^n\). Two classical theorems of Pisier and of Maurey and Pisier, named hypotheses of the course, connect this to \(K\)-convexity.

- Definitions: approximation property, type, cotype, \(K\)-convexity, uniform copies of \(\ell_1^n\) (Section 1).
- The theorems and the named hypotheses (Section 2).
- Elementary facts: duality of \(K\)-convexity, type and dual cotype, \(K\)-convexity excludes uniform copies of \(\ell_1^n\) (Section 3).
- Walsh transforms and uniform copies of \(\ell_1^n\); the proof of the main theorem from the decay theorem (Section 4).

The course follows [OpenAI-CC]. All Banach spaces are real, and \(X^*\) is the continuous dual of \(X\). Averages over finite sets are uniform, and different averaging variables are independent.

## 1. Definitions

A Banach space \(X\) has the *approximation property* (AP) if for every compact set \(M\subseteq X\) and every \(\delta>0\) there is a bounded linear map \(S\colon X\to X\) of finite rank with \(\sup_{x\in M}\|Sx-x\|<\delta\). The norms of these maps need not be bounded independently of \(M\) and \(\delta\); when they can be chosen with \(\|S\|\le\lambda\) for a fixed \(\lambda\), the space has the *bounded approximation property*.

Let \(\varepsilon_1,\varepsilon_2,\dots\) be independent uniform signs. For \(2\le q<\infty\), the *cotype \(q\) constant* \(C_q(Y)\) is the least constant with
\[
\begin{aligned}
&\Bigl(\sum_{i=1}^s\|y_i\|^q\Bigr)^{1/q}\\
&\quad\le C_q(Y)\Bigl(\mathbb E_\varepsilon\Bigl\|\sum_{i=1}^s\varepsilon_iy_i\Bigr\|^2\Bigr)^{1/2}
\end{aligned}
\]
for all finite families in \(Y\). The space \(Y\) has *finite cotype* if \(C_q(Y)<\infty\) for some \(q<\infty\). For \(1<p\le2\), \(Y\) has *type \(p\)* if for some \(T<\infty\) and all finite families
\[
\Bigl(\mathbb E_\varepsilon\Bigl\|\sum_i\varepsilon_iy_i\Bigr\|^2\Bigr)^{1/2}\le T\Bigl(\sum_i\|y_i\|^p\Bigr)^{1/p};
\]
the least such \(T\) is \(T_p(Y)\).

For a finite set \(\Omega\) with uniform probability, \(L_2(\Omega;X)\) is the space of functions \(\Omega\to X\) with the norm \((\mathbb E_\omega\|f(\omega)\|^2)^{1/2}\). The *Rademacher projection* on \(L_2(\{-1,1\}^s;X)\) is
\[
(\mathcal R_sf)(\varepsilon)=\sum_{i=1}^s\varepsilon_i\,\mathbb E_\eta[\eta_if(\eta)],
\]
and
\[
K(X)=\sup_{s\ge1}\|\mathcal R_s\|,
\]
where \(\|\mathcal R_s\|\) is the norm of \(\mathcal R_s\) on \(L_2(\{-1,1\}^s;X)\).
The space \(X\) is *\(K\)-convex* if \(K(X)<\infty\).

The space \(X\) *contains the spaces \(\ell_1^n\) uniformly* if there is \(\lambda\ge1\) such that for every \(n\) there are \(x_1,\dots,x_n\) in the unit ball \(B_X\) with
\[
\Bigl\|\sum_{j=1}^n\alpha_jx_j\Bigr\|\ge\lambda^{-1}\sum_{j=1}^n|\alpha_j|\qquad(\alpha\in\mathbb R^n).
\]

## 2. The theorems and the named hypotheses

**Theorem 2.1** ([OpenAI-CC, Theorem 1.1]). Let \(X\) be a nonzero real Banach space with the approximation property. Then \(X\) is \(K\)-convex if and only if
\[
C_q(X)<\infty\quad\text{and}\quad C_r(X^*)<\infty
\]
for some \(q,r\in[2,\infty)\).
The exponents \(q\) and \(r\) may differ. The implication from \(K\)-convexity to finite cotype holds for every real Banach space.

The assertion fails without an approximation hypothesis. For every space \(E\) of cotype \(2\), Pisier constructed a space \(X\) containing \(E\) isometrically such that \(X\) and \(X^*\) have cotype \(2\); this space fails the approximation property [Pis84, Theorem 7 and the end of Section 3]. With \(E=\ell_1\), \(X\) contains the spaces \(\ell_1^n\) uniformly, so it is not \(K\)-convex (Proposition 3.3). For cotype \(2\) on both sides, Pisier also proved a stronger conclusion: a space \(E\) with the approximation property such that \(E\) and \(E^*\) have cotype \(2\) is isomorphic to a Hilbert space [Pis84, Theorem 8 and its corollaries].

**Corollary 2.2** ([OpenAI-CC, Corollary 1.2], first assertion). For \(q,r\in[2,\infty)\) and \(C,D\ge1\) there is \(\kappa<\infty\) such that every nonzero real Banach space \(X\) with the approximation property, \(C_q(X)\le C\) and \(C_r(X^*)\le D\) has \(K(X)\le\kappa\).

The core of the proof is the following theorem, which needs no named hypothesis. Walsh norms \(w_N\) are defined in Section 4.

**Theorem 2.3** (decay theorem). Let \(X\) be a real Banach space with the approximation property and \(C_q(X)<\infty\), \(C_r(X^*)<\infty\) for some \(q,r\in[2,\infty)\). Then \(w_N(\mathrm{Id}_X)\to0\) as \(N\to\infty\), and \(X\) does not contain the spaces \(\ell_1^n\) uniformly.

Theorem 2.3 is proved in the last lesson, [Uniform decay and the characterization](uniform-decay-and-the-characterization.md); Section 4 below derives its second assertion from the first. Two classical theorems connect it with \(K\)-convexity; the course does not prove them.

**Hypothesis (P)** (Pisier; [Pis11, Theorem 4.49]). A Banach space that does not contain the spaces \(\ell_1^n\) uniformly is \(K\)-convex.

**Hypothesis (MP)** (Pisier, after Maurey and Pisier; [Pis11, Theorem 4.40(i)]). A Banach space that does not contain the spaces \(\ell_1^n\) uniformly has type \(p\) for some \(p>1\).

The converses of both hypotheses are proved in Section 3 (Proposition 3.3) and Exercise 5.3.

## 3. Elementary facts

**Lemma 3.1** (duality). For finite \(\Omega\), the pairing \(\langle f,g\rangle=\mathbb E_\omega\langle f(\omega),g(\omega)\rangle\) identifies \(L_2(\Omega;X^*)\) isometrically with the dual of \(L_2(\Omega;X)\), and \(\mathcal R_s\) on \(L_2(\{-1,1\}^s;X^*)\) is the adjoint of \(\mathcal R_s\) on \(L_2(\{-1,1\}^s;X)\). Hence \(K(X^*)=K(X)\).

*Proof.* Let \(n=|\Omega|\). A functional \(\Phi\) on \(L_2(\Omega;X)\) is determined by its restrictions to the functions supported at single points; write \(\Phi(f)=\mathbb E_\omega\langle f(\omega),g(\omega)\rangle\) with \(g(\omega)\in X^*\). Then \(|\Phi(f)|\le\mathbb E_\omega\|f(\omega)\|\|g(\omega)\|\le\|f\|\|g\|\), so \(\|\Phi\|\le\|g\|\). Conversely, for \(\delta>0\) choose \(x_\omega\in B_X\) with \(\langle x_\omega,g(\omega)\rangle\ge(1-\delta)\|g(\omega)\|\) and put \(f(\omega)=\|g(\omega)\|x_\omega\); then \(\|f\|\le\|g\|\) and \(\Phi(f)\ge(1-\delta)\|g\|^2\). So \(\|\Phi\|=\|g\|\). For the projection,
\[
\begin{aligned}
\langle\mathcal R_sf,g\rangle&=\sum_i\bigl\langle\mathbb E_\eta[\eta_if(\eta)],\mathbb E_\varepsilon[\varepsilon_ig(\varepsilon)]\bigr\rangle\\
&=\langle f,\mathcal R_sg\rangle .
\end{aligned}
\]
An operator and its adjoint have the same norm (Hahn–Banach, [Hahn–Banach, Baire and the basic theorems on Banach spaces](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces), Corollary 2.3). \(\blacksquare\)

**Lemma 3.2** (type and dual cotype). If \(Y\) has type \(p\in(1,2]\), then \(Y^*\) has cotype \(p'=p/(p-1)\), with \(C_{p'}(Y^*)\le T_p(Y)\).

*Proof.* For \(y_i\in Y\) and \(y_i^*\in Y^*\),
\[
\begin{aligned}
&\Bigl|\sum_iy_i^*(y_i)\Bigr|\\
&\quad=\Bigl|\mathbb E_\varepsilon\Bigl\langle\sum_i\varepsilon_iy_i,\sum_i\varepsilon_iy_i^*\Bigr\rangle\Bigr|\\
&\quad\le T_p(Y)\Bigl(\sum_i\|y_i\|^p\Bigr)^{1/p}\\
&\qquad\cdot\Bigl\|\sum_i\varepsilon_iy_i^*\Bigr\|_{L_2(Y^*)},
\end{aligned}
\]
by the Cauchy–Schwarz inequality. The supremum of the left side over \(\sum_i\|y_i\|^p\le1\) is \((\sum_i\|y_i^*\|^{p'})^{1/p'}\): choose \(y_i\) almost norming \(y_i^*\), with \(\|y_i\|\) proportional to \(\|y_i^*\|^{p'-1}\). \(\blacksquare\)

**Proposition 3.3** ([Pis11, Proposition 4.46]). A \(K\)-convex space does not contain the spaces \(\ell_1^n\) uniformly. More precisely, \(K(\ell_1^{2^n})\ge\sqrt{n/3}\), and if \(X\) contains vectors \(x_1,\dots,x_{2^n}\in B_X\) with \(\|\sum_j\alpha_jx_j\|\ge\lambda^{-1}\sum_j|\alpha_j|\), then \(K(X)\ge\lambda^{-1}\sqrt{n/3}\).

*Proof.* *A lower bound for sign sums.* For \(S=\sum_{j=1}^n\eta_j\), \(\mathbb ES^2=n\) and \(\mathbb ES^4=3n^2-2n\le3n^2\). By Hölder's inequality, \(\mathbb ES^2\le(\mathbb E|S|)^{2/3}(\mathbb ES^4)^{1/3}\), so
\[
\mathbb E|S|\ge\frac{(\mathbb ES^2)^{3/2}}{(\mathbb ES^4)^{1/2}}\ge\sqrt{n/3}.
\]

*The space \(\ell_1^{2^n}\).* Identify \(\ell_1^{2^n}\) isometrically with \(L_1(D_n)\), the functions on \(D_n=\{-1,1\}^n\) with the norm \(\mathbb E_\eta|\phi(\eta)|\). Let \(b_j(\eta)=\eta_j\) and define \(F\colon D_n\to L_1(D_n)\) by \(F(\varepsilon)=\prod_{j=1}^n(1+\varepsilon_jb_j)\). Each \(F(\varepsilon)\) is a nonnegative function with mean \(1\), so \(\|F\|_{L_2(L_1)}=1\). Expanding the product, \(\mathbb E_\varepsilon[\varepsilon_jF(\varepsilon)]=b_j\), so
\[
\begin{gathered}
(\mathcal R_nF)(\varepsilon)=\sum_j\varepsilon_jb_j,\\
\Bigl\|\sum_j\varepsilon_jb_j\Bigr\|_{L_1(D_n)}=\mathbb E_\eta\Bigl|\sum_j\varepsilon_j\eta_j\Bigr|,
\end{gathered}
\]
which is \(\mathbb E|S|\ge\sqrt{n/3}\) for every \(\varepsilon\). Hence \(K(\ell_1^{2^n})\ge\sqrt{n/3}\).

*Copies.* The map \(T\colon\ell_1^{2^n}\to X\), \(e_j\mapsto x_j\), has \(\|T\|\le1\) and \(\|T^{-1}\|\le\lambda\) on its range \(E\). Pointwise application of \(T\) commutes with \(\mathcal R_n\), and \(K\) does not increase under passage to a subspace, so \(K(\ell_1^{2^n})\le\lambda K(E)\le\lambda K(X)\). \(\blacksquare\)

*Proof of the forward implication of Theorem 2.1, assuming (MP).* Let \(K(X)<\infty\). By Lemma 3.1, \(K(X^*)<\infty\). By Proposition 3.3 neither \(X\) nor \(X^*\) contains the spaces \(\ell_1^n\) uniformly, so by (MP) both have type \(p>1\) for some \(p\). By Lemma 3.2, \(X^*\) and \(X^{**}\) have finite cotype, and the cotype inequality of \(X^{**}\) restricts to \(X\subseteq X^{**}\). No approximation property is used. \(\blacksquare\)

## 4. Walsh transforms and uniform copies of \(\ell_1^n\)

Let \(V_n=\mathbb F_2^n\), with the dot product \(u\cdot v\) computed modulo \(2\), and \(\chi(u,v)=(-1)^{u\cdot v}\). For a bounded linear map \(T\colon G\to F\) between Banach spaces, the *Walsh transform* \(W^T_n\colon L_2(V_n;G)\to L_2(V_n;F)\) is
\[
(W^T_nx)(v)=\mathbb E_{u\in V_n}\chi(u,v)\,Tx(u),
\]
and the *Walsh norm* is \(w_n(T)=\|W^T_n\|\). For \(n=0\), \(w_0(T)=\|T\|\).

**Lemma 4.1.** If \(X\) contains the spaces \(\ell_1^n\) uniformly with constant \(\lambda\), then \(w_N(\mathrm{Id}_X)\ge\lambda^{-1}\) for every \(N\).

*Proof.* Choose \(x_u\in B_X\), \(u\in V_N\), with \(\|\sum_u\alpha_ux_u\|\ge\lambda^{-1}\sum_u|\alpha_u|\). The input \(x=(x_u)\) has \(\|x\|_{L_2}\le1\), and for every \(v\)
\[
\begin{aligned}
\bigl\|(W^{\mathrm{Id}}_Nx)(v)\bigr\|&=\Bigl\|2^{-N}\sum_u\chi(u,v)x_u\Bigr\|\\
&\ge\lambda^{-1}.
\end{aligned}
\]
So \(\|W^{\mathrm{Id}}_Nx\|_{L_2}\ge\lambda^{-1}\). \(\blacksquare\)

So the second assertion of Theorem 2.3 follows from the first.

*Proof of the converse implication of Theorem 2.1, assuming (P).* By Theorem 2.3, \(X\) does not contain the spaces \(\ell_1^n\) uniformly, and (P) gives \(K(X)<\infty\). \(\blacksquare\)

*Proof of Corollary 2.2, assuming (P).* Suppose not, and choose spaces \(X_j\) with the approximation property, \(C_q(X_j)\le C\), \(C_r(X_j^*)\le D\) and \(K(X_j)\to\infty\). Let \(Z=(\bigoplus_jX_j)_{\ell_2}\). Its dual is \((\bigoplus_jX_j^*)_{\ell_2}\). For \(z_i=(z_{ij})_j\) in \(Z\), Minkowski's inequality in \(\ell_{q/2}\) gives
\[
\begin{aligned}
\Bigl(\sum_i\|z_i\|^q\Bigr)^{2/q}&\le\sum_j\Bigl(\sum_i\|z_{ij}\|^q\Bigr)^{2/q}\\
&\le C^2\,\mathbb E_\varepsilon\Bigl\|\sum_i\varepsilon_iz_i\Bigr\|^2,
\end{aligned}
\]
so \(C_q(Z)\le C\), and likewise \(C_r(Z^*)\le D\). \(Z\) has the approximation property: for compact \(M\subseteq Z\) and \(\delta>0\), the truncations to finitely many coordinates converge uniformly on \(M\), and each of the finitely many coordinate images of \(M\) is compact in \(X_j\). By Theorem 2.1, \(K(Z)<\infty\), while \(K(X_j)\le K(Z)\) for every \(j\), since \(X_j\) is a subspace. This is a contradiction. \(\blacksquare\)

## 5. Exercises

**5.1.** Show that \(C_q(\mathbb R)=1\) for every \(q\ge2\), and that Hilbert spaces have type \(2\) and cotype \(2\) with constant \(1\).

**5.2.** Show that \(K(H)=1\) for a Hilbert space \(H\).

**5.3.** Show that a space with type \(p>1\) does not contain the spaces \(\ell_1^n\) uniformly. (This is the converse of (MP).)

**5.4.** Show that \(w_n(\mathrm{Id}_H)=2^{-n/2}\) for a Hilbert space \(H\ne0\).

**5.5.** In the proof of Corollary 2.2, give the finite-rank maps on \(Z\) explicitly from finite-rank approximations on the coordinates.

## 6. Solutions

**5.1.** For real numbers, \(\mathbb E(\sum_i\varepsilon_iy_i)^2=\sum_iy_i^2\ge(\sum_i|y_i|^q)^{2/q}\). In a Hilbert space, \(\mathbb E\|\sum_i\varepsilon_iy_i\|^2=\sum_i\|y_i\|^2\), since the cross terms have mean \(0\).

**5.2.** On \(L_2(\{-1,1\}^s;H)\), \(\mathcal R_s\) is an orthogonal projection: the functions \(\varepsilon\mapsto\varepsilon_ih\) are orthogonal to the other Walsh functions. Its norm is \(1\) (for \(s\ge1\), \(H\ne0\)).

**5.3.** With \(x_j\) as in the definition, \(\lambda^{-1}n\le\mathbb E\|\sum_j\varepsilon_jx_j\|\le T_p(X)n^{1/p}\), which fails for large \(n\) when \(p>1\).

**5.4.** The matrix \((2^{-n}\chi(u,v))_{u,v}\) is \(2^{-n/2}\) times an orthogonal matrix, and on \(L_2(V_n;H)\) the transform acts as this matrix tensored with \(\mathrm{Id}_H\).

**5.5.** Given \(M\) and \(\delta\), choose \(J\) with \(\sup_{z\in M}(\sum_{j>J}\|z_j\|^2)^{1/2}<\delta/2\), and for \(j\le J\) finite-rank \(S_j\) on \(X_j\) with \(\sup_{z\in M}\|S_jz_j-z_j\|<\delta/(2\sqrt J)\). Put \(S(z)=(S_1z_1,\dots,S_Jz_J,0,\dots)\).

## References

- [OpenAI-CC] OpenAI, *The cotype–cotype conjecture under the approximation property*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1, Corollary 1.2. https://github.com/openai/math/tree/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026
- [Pis11] G. Pisier, *Martingales in Banach spaces (in connection with type and cotype)*, IHP course notes, version of 9 February 2011, Theorems 4.40 and 4.49, Proposition 4.46. https://webusers.imj-prg.fr/~gilles.pisier/ihp-pisier.pdf
- [Pis84] G. Pisier, *Finite rank projections on Banach spaces and a conjecture of Grothendieck*, Proceedings of the International Congress of Mathematicians (Warsaw, 1983), Vol. 2, 1027–1039, Theorems 5, 7 and 8. https://www.imj-prg.fr/wp-content/uploads/2020/prix/pisier1983.pdf

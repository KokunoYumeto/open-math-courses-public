# Bilinear sums and the sharp cutoff

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson assembles the proof of the first moment. The sharp condition \(X<N(\pi)\le2X\) is replaced by a smooth envelope times a Fourier integral over heights \(|t|\le X^{1/6+\rho}\), at a cost of \(X^{5/6-\rho+\epsilon}\). At low heights, \(|t|\le L^{C_t}\), the difference between the Gauss sums and the model is decomposed and estimated piece by piece. The bilinear pieces are bounded with the corrected dispersion of the lesson on corrected dispersion, and the three-prime transition with its uncorrected form. At large heights the model is removed before decomposition by a mean value estimate. The Gauss sums alone are then decomposed, and the bilinear pieces are bounded by localizing both norm variables in cells. Near the product boundary the localized diagonal is small. Away from it, integration by parts in the height gives the saving.

Everything is done for a fixed angular order \(\ell\), with \(\mathcal D_\ell\) and \(G_\ell\) as in the lesson on the level formula; \(\ell=0\) gives Theorem 4.1 of the first lesson.

**Prerequisites.** The lessons [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md), [*The level formula and Type I sums*](the-level-formula-and-type-i-sums.md), [*Corrected dispersion*](corrected-dispersion.md) and [*An exact decomposition of the prime sum*](an-exact-decomposition-of-the-prime-sum.md).

## 1. Ranges

Throughout, \(L=\log X\), \(AB\asymp X\), \(H=B^2/A\) and \(\mathcal Q=ABH^{1/3}\), so that \(A\mathcal Q=(AB)^{5/3}\asymp X^{5/3}\). Coefficients are divisor-bounded, and their moment bounds contribute fixed powers of \(L\). Both terms of \(\mathcal D_\ell(n)\) vanish unless \(n\) is squarefree, so separate squarefree restrictions may be imposed on \(a\) and \(b\) in a sum of \(\mathcal D_\ell(ab)\). Let \(V\) be a fixed smooth function with compact support in \((0,\infty)\). The decomposition of the previous lesson supplies the following ranges:

- \(|t|\le L^{C_t}\): Type I with \(R\le X^{0.40}\); bilinear with \(c_0X^{1/3}\le B\ll X^{1/2}\).
- \(L^{C_t}\le T\ll X^{0.01}\): the same ranges.
- \(X^{0.01}\ll T\ll X^{1/6+\rho}\): Type I with \(R\le X^{1/3-\kappa/2}\); bilinear with \(X^{1/3-3\kappa}\le B\ll X^{1/2}\).

## 2. Bilinear sums at low heights

**Proposition 2.1 (low-height bilinear comparison).** Let \(X^{0.32}\le B\ll\sqrt X\) and \(H\gg1\). Suppose \(\beta\) satisfies the structural hypotheses of Proposition 1.1 of the lesson on corrected dispersion, is rough, and has property (SW). For every fixed \(D,U>0\), the parameters of that proposition can be chosen so that, uniformly for \(|t|\le L^U\) and \(H\ge L^{C_g}\),
\[
\begin{aligned}
&\sum_{a,b}\alpha_a\beta_b\,\mathcal D_\ell(ab)\,N(ab)^{it}\\
&\qquad\cdot V\Bigl(\frac{N(ab)}X\Bigr)\ll X^{5/6}L^{-D}.\quad(2.1)
\end{aligned}
\]
Moreover, suppose \(b\) is a single prime, \(a\) a product of two primes, each of the three primes in its own smooth dyad of length \(X^{1/3}L^{O(1)}\), with bounded weights. If \(1\ll H<L^{C_g}\), then the left side of (2.1) is
\[
O\bigl(X^{5/6}L^{-3/2}\bigr),
\tag{2.2}
\]
uniformly for the families of dyads produced by the decomposition.

**Proof.** Put \(\theta_\ell\) into the coefficients: \(\mathcal D_\ell(ab)\) is \(\mathcal D_0(ab)\) with \(\alpha_a,\beta_b\) replaced by \(\theta_\ell(a)\alpha_a,\theta_\ell(b)\beta_b\), and the second is an admissible prime convolution with angular order \(\ell\) when \(B>X^{0.40}\). Omit the envelope first. Proposition 3.1(c) of the first lesson gives
\[
\begin{aligned}
&\sum_{a,b}\alpha_a\beta_bG(ab)N(ab)^{it}\\
&\qquad=\sum_a\alpha_aG(a)N(a)^{it}F_t(a)
\end{aligned}
\]
in the notation of the lesson on corrected dispersion. Write
\[
\begin{aligned}
&F_t(a)=c_*\overline{G(a)}N(a)^{-1/6}S(t)\\
&\quad+\bigl(F_t(a)-c_*\overline{G(a)}N(a)^{-1/6}S(t)\bigr).
\end{aligned}
\]
By Cauchy's inequality, with a smooth radial \(W\) that is at least \(1\) on the support of \(\alpha\), and the corrected estimate (1.1) of that lesson, the second part contributes
\[
\begin{aligned}
&\ll\Bigl(\sum_a|\alpha_a|^2\Bigr)^{1/2}\bigl(\mathcal QL^{-K}\bigr)^{1/2}\\
&\ll(A\mathcal Q)^{1/2}L^{-K/2+O(1)}\\
&\ll X^{5/6}L^{-K/2+O(1)} .
\end{aligned}
\]
The first part, since \(|G(a)|^2=\mu^2(a)\), is
\[
\begin{aligned}
&c_*\sum_a\alpha_a\mu^2(a)N(a)^{it-1/6}\\
&\qquad\cdot\sum_b\beta_bN(b)^{it-1/6}.
\end{aligned}
\]
The model part of \(\mathcal D_0(ab)\) is the same double sum with \(\mu^2(ab)\), that is, with the additional condition \((a,b)=1\). A common prime of \(a\) and \(b\) has norm greater than \(L^{C_r}\), and the number of pairs sharing such a prime is
\[
\ll AB\sum_{N(\mathfrak p)>L^{C_r}}N(\mathfrak p)^{-2}\ll ABL^{-C_r},
\]
since there are \(O(Y)\) ideals of norm at most \(Y\). By Cauchy's inequality and the coefficient moments, their weighted number is \(O(ABL^{-C_r/2+O(1)})\), and with the factor \(N(ab)^{-1/6}\asymp X^{-1/6}\) their contribution is \(O(X^{5/6}L^{-C_r/2+O(1)})\). Taking \(K\) and \(C_r\) large proves (2.1) without the envelope.

For the transition, the specified prime dyads and the bounded weights give
\[
\begin{gathered}
\sum_a|\alpha_a|^2\ll\frac A{L^2},\\
\sum_b|\beta_b|^2\ll\frac BL,\qquad\sum_b|\beta_b|\ll\frac BL .
\end{gathered}
\]
Apply Cauchy's inequality and the uncorrected estimate (1.2) of the lesson on corrected dispersion. The diagonal part contributes
\[
\begin{aligned}
&\Bigl(\frac A{L^2}\cdot\frac{AB}L\Bigr)^{1/2}=A\sqrt B\,L^{-3/2}\\
&\qquad=X^{5/6}H^{-1/6}L^{-3/2},
\end{aligned}
\]
the next part \(\bigl(\frac A{L^2}\cdot\frac{\mathcal Q}{L^2}\bigr)^{1/2}=X^{5/6}L^{-2}\), and the remainder \(L^{-K}\) is smaller. Since \(H\gg1\), this bounds the Gauss-sum term by (2.2). The model term is \(O(X^{5/6}L^{-3})\) by counting the three prime dyads directly.

The envelope costs no logarithm. Mellin inversion writes \(V(N(ab)/X)\) through norm twists \(N(ab)^{-iv}\) with a rapidly decreasing integrable weight. Keep \(|v|\le L^E\) for a large fixed \(E\), and choose the permitted height exponent \(U\) after \(E\). For \(L^E\le|v|\le X^{c}\), with a small fixed \(c\), the coarse bound of the lesson on corrected dispersion and Cauchy's inequality give \(X^{5/6}L^{O(1)}\) for the uncorrected sum, and the model trivially has the same bound. The rapid decay of the weight makes this range smaller than any fixed power of \(L\). Beyond \(X^c\), the decay and the trivial bound \(XL^{O(1)}\) give a power saving. \(\square\)

## 3. Bilinear sums at large heights

Fix the absolute constant \(\gamma\) of the estimate (1.4) of the lesson on corrected dispersion so small that \(0<\gamma<10^{-3}\), and choose
\[
\begin{gathered}
0<\kappa<\frac\gamma{100},\qquad 0<\rho<\frac\kappa{100},\\
0<\xi<\frac\kappa{10}.\quad(3.1)
\end{gathered}
\]
These choices precede, and do not depend on, the number of prime factors allowed in the decomposition.

**Proposition 3.1 (integrated bilinear estimate).** Let \(X_0\asymp X\) and let \(h_T\) be smooth, supported in \(T\le|t|\le2T\), with \(h_T^{(j)}(t)\ll_jT^{-j}\). Suppose \(L^{C_t}\le T\ll X^{1/6+\rho}\), \(B\ll\sqrt X\), and either

- (a) \(T\ll X^{0.01}\) and \(B\ge c_0X^{1/3}\), or
- (b) \(T\gg X^{0.01}\) and \(B\ge X^{1/3-3\kappa}\).

Assume the structural hypotheses of the lesson on corrected dispersion, but neither roughness nor (SW). For every fixed \(D\), if \(C_t\) is large enough,
\[
\begin{aligned}
&\sum_{a,b}\alpha_a\beta_bG_\ell(ab)V\Bigl(\frac{N(ab)}X\Bigr)\\
&\quad\cdot\int h_T(t)\Bigl(\frac{N(ab)}{X_0}\Bigr)^{it}\frac{dt}T\ll X^{5/6}L^{-D}.
\end{aligned}
\]

**Proof.** As before, \(\theta_\ell\) goes into the coefficients.

*The case \(B>X^{0.40}\).* Apply Cauchy's inequality in \(a\) and \(t\), and then the averaged estimate (1.3) of the lesson on corrected dispersion. The diagonal costs
\[
\begin{aligned}
&\ll\bigl(A\cdot AB\bigr)^{1/2}L^{O(1)}\asymp\frac X{\sqrt B}L^{O(1)}\\
&\ll X^{0.80}L^{O(1)},
\end{aligned}
\]
and the error costs \(X^{5/6}L^{-K/2+O(1)}\). The envelope separates by Mellin inversion, with shifts truncated at a small fixed power of \(X\); the retained shifts satisfy \(2T+|u_0|\le X^{0.17}\), since \(\rho<0.001\).

*The case \(B\le X^{0.40}\).* Partition the two fixed intervals of \(\log N(a)\) and \(\log N(b)\) into disjoint cells of width \(1/J\), where
\[
\begin{gathered}
J=L^{D'}\ \text{ in case (a)},\\
J=X^\gamma\ \text{ in case (b)}.
\end{gathered}
\]
There are \(O(J)\) cells on each side. Put \(a_i=\|\alpha\mathbf 1_{\text{cell }i}\|_2\) and \(b_j=\|\beta\mathbf 1_{\text{cell }j}\|_2\). A smooth majorant of an \(a\)-cell has derivatives of order \(s\) bounded by \(O_s(J^s)\), and its lattice-point count is \(O(A/J+\sqrt A+1)=O(A/J)\), because \(A\gg X^{0.60}\) and \(\gamma<0.30\). Restricting \(\beta\) sharply to a cell keeps its divisor bounds and squarefree support, and no prime-convolution hypothesis is needed in this range of \(B\).

For a fixed pair of cells, Cauchy's inequality and the averaged dispersion estimate give the bound
\[
\begin{gathered}
C\,a_i\Bigl(\frac AJb_j^2+\mathcal Q\varepsilon_J\Bigr)^{1/2},\quad(3.2)\\
\varepsilon_J=L^{-K}\ \text{in (a)},\\
\varepsilon_J=X^{-10\gamma}\ \text{in (b)}.
\end{gathered}
\]
This holds after any common Mellin shift, because for \(B\le X^{0.40}\) the dispersion estimate puts no restriction on \(u_0\). In particular it applies with the envelope, whose Mellin transform has bounded \(L^1\) norm.

A pair of cells is *near* if its rectangle meets \(|\log(N(ab)/X_0)|\le c_1/J\), for a fixed \(c_1>0\). Each cell has \(O(1)\) near partners, so the diagonal parts of (3.2) over the near pairs add up to
\[
\begin{aligned}
&\ll\sqrt{\frac AJ}\,\|\alpha\|_2\|\beta\|_2\\
&\ll X^{5/6}L^{O(1)}H^{-1/6}J^{-1/2}.\quad(3.3)
\end{aligned}
\]
In case (a) this is the required saving once \(D'\) is large. In case (b), \(H\gg X^{-9\kappa}\), so the extra power of \(X\) is at most \(\frac32\kappa-\frac\gamma2<0\).

The errors in (3.2) are absolute; even summed over all \(O(J^2)\) pairs they give
\[
\begin{aligned}
&\sqrt{\mathcal Q\varepsilon_J}\,J\sum_ia_i\\
&\ll\sqrt{\mathcal Q\varepsilon_J}\,J^{3/2}\|\alpha\|_2\\
&\ll X^{5/6}L^{O(1)}J^{3/2}\varepsilon_J^{1/2}.\quad(3.4)
\end{aligned}
\]
In case (a) take \(K\) large after \(D'\); in case (b) the extra factor is \(X^{3\gamma/2-5\gamma}=X^{-7\gamma/2}\).

*Far pairs.* Put \(\ell_1=\log(N(ab)/X_0)\), so that \(|\ell_1|>c_1/J\) on a far pair. Integrating by parts \(q\) times in the integral over \(t\) differentiates only \(h_T\). It produces the factor \((J/T)^q\), a new height function proportional to \(T^qh_T^{(q)}\), and the weight \((J\ell_1)^{-q}\). The new height function has the same normalized derivative bounds. The weight costs no power of \(J\): for a fixed integer \(q\ge2\), let \(F_q\) be a smooth function on \(\mathbb R\), equal to \(s^{-q}\) for \(|s|\ge c_1\) and to \(0\) near \(0\). Then \(F_q\) and \(F_q''\) are integrable, so its Fourier transform is integrable, and \(\|\widehat{F_q(J\,\cdot)}\|_1=\|\widehat F_q\|_1\). So \(F_q(J\ell_1)\) is a superposition of norm twists with \(L^1\) mass \(O_q(1)\), uniformly in \(J\). These shifts do not depend on \(t\), and shifts larger than \(T\) are allowed, since for \(B\le X^{0.40}\) the dispersion estimate permits any \(u_0\).

Applying (3.2) again with this separated weight, the diagonal parts over all pairs add up to
\[
\begin{aligned}
&\ll\sqrt{\frac AJ}\Bigl(\sum_ia_i\Bigr)\Bigl(\sum_jb_j\Bigr)\\
&\ll X^{5/6}L^{O(1)}H^{-1/6}J^{1/2},\quad(3.5)
\end{aligned}
\]
before the factor \((J/T)^q\). In case (a), \((J/T)^q\le L^{-q(C_t-D')}\), which pays for the loss when \(C_t\) is large. In case (b) it is at most a constant times \(X^{-q(0.01-\gamma)}\), which pays for \(H^{-1/6}J^{1/2}\ll X^{3\kappa/2+\gamma/2}\). The errors are already controlled by (3.4). \(\square\)

## 4. The order of the parameters

The uniformity of the final assembly rests on the order in which the constants are chosen.

1. Choose \(\gamma,\kappa,\rho\) as in (3.1), then \(\xi\) and the bin ratio of the decomposition. The decomposition then has at most \(L^{C_{\mathrm{dec}}}\) pieces. Fix \(M\) larger than all coefficient moment exponents needed; these exponents do not depend on \(C_r\).
2. Choose
\[
\begin{gathered}
D>C_{\mathrm{dec}}+10,\\
D'>2(D+M+2),\\
K>3D'+2(D+M+2).
\end{gathered}
\]
The near-cell and error bounds in case (a) are then \(X^{5/6}L^{M-D'/2}\) and \(X^{5/6}L^{M+3D'/2-K/2}\).
3. Choose \(C_t\) large enough for the averaged dispersion estimate at derivative scale \(L^{D'}\) with output power \(K\), for the far cells with a fixed \(q\ge2\), and for the model estimate of Section 6.
4. For the low heights, take the corrected-variance power larger than \(2(D+M+2)\), choose the sieve depth \(D_0\) and the transform cutoffs of the dispersion proof, and fix a height exponent covering \(L^{C_t}\) and all retained shifts.
5. Choose \(C_r\) and \(C_g\) large enough for the roughness, the diagonal and the cube approximation, and request the finitely many (SW) saving powers needed. Inserting \(L^{C_r}\) as a bin endpoint does not change \(C_{\mathrm{dec}}\), and enlarging \(C_g\) changes only constants in the number of transition configurations.
6. Finally choose all small power losses below the fixed power gaps obtained, including the gap of the sparse terms, which may depend on \(C_r\).

There is no circular dependence: the absolute power-width constant \(\gamma\) is used only for \(B\le X^{0.40}\), where it does not depend on the prime-convolution complexity.

## 5. A smooth truncation of the interval

**Lemma 5.1 (Fourier truncation).** Let \(1\le T\le X\), and let \(V\) be a fixed smooth function supported in \((\frac12,4)\), equal to \(1\) on a neighborhood of \([1,2]\). Let \(\eta\) be a fixed smooth function supported in \([-1,1]\), equal to \(1\) near \(0\), and put
\[
I_T(s)=\frac1{2\pi}\int_{\mathbb R}\eta\Bigl(\frac tT\Bigr)\frac{1-2^{-it}}{it}\,e^{its}\,dt .
\]
Then for every \(m>0\), on the support of \(V\),
\[
\begin{aligned}
&\bigl|\mathbf 1_{[1,2]}(v)-V(v)I_T(\log v)\bigr|\\
&\qquad\ll_m\sum_{b\in\{0,\log2\}}\bigl(1+T|\log v-b|\bigr)^{-m},
\end{aligned}
\]
and the difference vanishes outside it. If coefficients collected at each integer norm satisfy \(|c_n|\ll_\epsilon X^\epsilon\) for \(X/2<n<4X\), then
\[
\begin{aligned}
&\sum_n|c_n|\Bigl|\mathbf 1_{[X,2X]}(n)\\
&\qquad-V\Bigl(\frac nX\Bigr)I_T\Bigl(\log\frac nX\Bigr)\Bigr|\\
&\ll_\epsilon X^\epsilon\Bigl(1+\frac XT\Bigr).
\end{aligned}
\]

**Proof.** The Fourier transform of \(\mathbf 1_{[0,\log2]}\), in the convention of the formula, is \((1-2^{-it})/(it)\), read as \(\log2\) at \(t=0\). The inverse transform of \(\eta(t/T)\) is \(Tk(Ts)\) for a Schwartz function \(k\) with integral \(\eta(0)=1\). So \(I_T\) is the convolution of the indicator of \([0,\log2]\) with this approximate identity. At distance \(\delta\) from both endpoints, the difference from the indicator is at most the mass of the kernel beyond \(\delta\), which is \(O_m((1+T\delta)^{-m})\). Where \(V\ne1\), the distance to \([1,2]\) is bounded below, so the same estimate holds there. On \(\frac12\le v\le4\), distances in \(\log v\) and in \(v\) are comparable. Summing \((1+T|n-X_0|/X)^{-2}\) over integers \(n\), for \(X_0=X,2X\), gives \(O(1+X/T)\). \(\square\)

## 6. The dyadic comparison

**Theorem 6.1.** For every fixed integer \(\ell\),
\[
\begin{aligned}
&\sum_{X<N(\pi)\le2X}\theta_\ell(\pi)\Bigl(G(\pi)-\frac{c_*}{N(\pi)^{1/6}}\Bigr)\\
&\qquad=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\end{aligned}
\]

**Proof.** Apply Lemma 5.1 with \(T_{\max}=X^{1/6+\rho}\). At each norm the number of primary primes is at most two, and \(|G(\pi)|=1\), so the lemma applies separately to the Gauss sums and to the model. Taking \(\epsilon<\rho\), the total truncation error is
\[
\ll X^\epsilon\Bigl(1+\frac X{T_{\max}}\Bigr)=o\Bigl(\frac{X^{5/6}}L\Bigr).
\]
Split the integral defining \(I_T\) into bounded frequencies and smooth dyadic blocks of heights. Away from bounded frequencies, the two endpoint terms have the form
\[
\begin{gathered}
\int h_T(t)\Bigl(\frac{N(n)}{X_0}\Bigr)^{it}\frac{dt}T,\\
X_0=X\text{ or }2X,
\end{gathered}
\]
with \(h_T^{(j)}\ll_jT^{-j}\): the factor \(1/(it)\) is \(1/T\) times a smooth bounded function on a block, and the cutoff at \(T_{\max}\) keeps these derivative bounds. At bounded frequencies the difference of the endpoint terms is bounded, also at \(0\).

*Low heights, \(|t|\le L^{C_t}\).* Apply the decomposition for ordinary blocks to the difference \(\mathcal D_\ell\), which is legitimate because the two kernels have the same coefficients. The Type I terms are bounded by Proposition 4.1 of the lesson on the level formula: a norm twist of logarithmic height only introduces logarithmic derivative bounds. The regular bilinear terms are bounded by (2.1), with the output power \(D\) fixed in Section 4, and the sparse terms have a power saving. The remaining terms are the three-prime transition, with bounded weights, \(1\ll H<L^{C_g}\), and \(O((1+\log L)^C)\) configurations. By (2.2), and since there are \(O(1+\log L)\) low-height blocks, they contribute
\[
\begin{aligned}
&\ll X^{5/6}L^{-3/2}(1+\log L)^{C+1}\\
&\qquad=o\Bigl(\frac{X^{5/6}}L\Bigr).
\end{aligned}
\]
All other low-height terms are smaller after summing their \(L^{C_{\mathrm{dec}}}\) pieces.

*Large heights, \(T\ge L^{C_t}\): the model.* On the envelope, collect the model at equal norms into \(P_0(t)=\sum_{n\asymp X}d_nn^{it}\). There are at most two primes of each norm, so \(\sum_n|d_n|^2\ll X^{2/3}L^{O(1)}\). The mean value inequality (Lemma 5.1 of the lesson on large sieves) and Cauchy's inequality give
\[
\begin{aligned}
&\int_{T\le|t|\le2T}|P_0(t)|\frac{dt}T\\
&\ll X^{1/3}L^{O(1)}\Bigl(1+\frac XT\Bigr)^{1/2}\\
&\ll X^{5/6}L^{O(1)}T^{-1/2},
\end{aligned}
\]
since \(T<X\). Taking \(C_t\) large makes this negligible even after the \(O(L)\) height blocks. No decomposition of the model, and no cancellation between its pieces, is needed.

*Large heights: the Gauss sums.* Decompose the Gauss-sum term alone. On ordinary blocks, \(T\ll X^{0.01}\), the Type I terms without a stop have \(R\le X^{0.40}\). By Proposition 5.2 of the lesson on the level formula, the first term of their bound has exponent at most
\[
\frac12+\frac34(0.40)+\frac12(0.01)=0.805<\frac56 .
\]
On upper blocks, \(T\gg X^{0.01}\), they have \(R\le X^{1/3-\kappa/2}\), and the exponent is
\[
\begin{aligned}
&\frac12+\frac34\Bigl(\frac13-\frac\kappa2\Bigr)+\frac12\Bigl(\frac16+\rho\Bigr)\\
&\qquad=\frac56-\frac{3\kappa}8+\frac\rho2<\frac56 .
\end{aligned}
\]
The pole term in Proposition 5.2, present only for \(\ell=0\), is \(X^{5/6}L^CT^{-q}\) for every fixed \(q\), negligible above \(L^{C_t}\). These estimates allow a smooth envelope at scale \(X/N(r)\) depending on \(r\), and twists of the outer coefficients of absolute value one. Every nonsparse bilinear term falls under case (a) or (b) of Proposition 3.1, with the output power \(D\). The sparse ordinary terms keep their power saving uniformly in the twist. Summing over the \(O(L)\) height blocks and the at most \(L^{C_{\mathrm{dec}}}\) pieces costs less than the chosen saving. Different blocks may use different decompositions, since each is an exact identity on squarefree arguments.

Combining the low and large heights with the truncation error gives the theorem; changing whether the endpoints are included has a cost bounded by the divisor bound. \(\square\)

**Proof of Theorem 4.1 of the first lesson.** Sum Theorem 6.1 with \(\ell=0\) over the dyadic ranges \((X/2^{k+1},X/2^k]\) above \(X^{1/2}\). On these ranges the factor \(o(1)\) is uniform, the logarithms are comparable to \(\log X\), and the powers \(X^{5/6}2^{-5k/6}\) form a geometric series. The primes of norm below \(X^{1/2}\) contribute \(O(X^{1/2})\). So
\[
\begin{aligned}
\sum_{N(\pi)\le X}G(\pi)&=c_*\sum_{N(\pi)\le X}N(\pi)^{-1/6}\\
&\quad+o\Bigl(\frac{X^{5/6}}{\log X}\Bigr),
\end{aligned}
\]
and Proposition 4.3 of the first lesson evaluates the sum on the right as \(\frac65X^{5/6}/\log X+o(X^{5/6}/\log X)\). \(\square\)

## 7. Exercises

**7.1.** Verify the identities \(A\sqrt B=X^{5/6}H^{-1/6}\) and \(A\mathcal Q=(AB)^{5/3}\), used in Proposition 2.1.

**7.2.** In case (b) of Proposition 3.1, show that \(H\gg X^{-9\kappa}\), and that the near-cell bound (3.3) saves the power \(X^{\gamma/2-3\kappa/2}\).

**7.3.** Show that the Fourier transform of \(\mathbf 1_{[0,\log2]}\), with the convention \(\widehat f(t)=\int f(s)e^{-its}ds\), is \((1-2^{-it})/(it)\).

**7.4.** Explain why the model term at large heights can be estimated without decomposition, while the Gauss-sum term cannot.

**7.5.** Check that the truncation at \(T_{\max}=X^{1/6+\rho}\) costs \(o(X^{5/6}/\log X)\), and that a smaller \(T_{\max}\), such as \(X^{1/6-\rho}\), would not suffice.

## 8. Solutions

**7.1.** \(X^{5/6}H^{-1/6}=(AB)^{5/6}(B^2/A)^{-1/6}\)\(=A^{5/6+1/6}B^{5/6-1/3}=AB^{1/2}\). And \(\mathcal Q=AB(B^2/A)^{1/3}=A^{2/3}B^{5/3}\), so \(A\mathcal Q=A^{5/3}B^{5/3}\).

**7.2.** With \(B\ge X^{1/3-3\kappa}\) and \(A\asymp X/B\), \(H=B^2/A\asymp B^3/X\ge X^{-9\kappa}\). So \(H^{-1/6}\le X^{3\kappa/2}\), and with \(J=X^\gamma\) the bound (3.3) is \(X^{5/6}L^{O(1)}X^{3\kappa/2-\gamma/2}\). Since \(\kappa<\gamma/100\), the exponent \(\frac32\kappa-\frac\gamma2\) is negative.

**7.3.** \(\int_0^{\log2}e^{-its}ds=\frac{1-e^{-it\log2}}{it}=\frac{1-2^{-it}}{it}\).

**7.4.** The model coefficients are \(c_*\theta_\ell(\pi)N(\pi)^{-1/6}\), of size \(X^{-1/6}\) on the envelope, so their Dirichlet polynomial has mean square about \(X^{2/3}\cdot X/T\), and its mean absolute value \(X^{5/6}T^{-1/2}\) is already small for \(T\ge L^{C_t}\). The Gauss sums have size \(1\), so the same estimate gives \(X\,T^{-1/2}\), which is too large for \(T\le X^{1/3}\); only the decomposition and the arithmetic of \(G\) give the saving.

**7.5.** The cost is \(X^{\epsilon}(1+X/T_{\max})=X^{5/6-\rho+\epsilon}\), which is \(o(X^{5/6}/\log X)\) for \(\epsilon<\rho\). With \(T_{\max}=X^{1/6-\rho}\) it would be \(X^{5/6+\rho+\epsilon}\), larger than the main term. This is why the upper blocks must reach heights slightly beyond \(X^{1/6}\), and why the parameters \(\kappa\) and \(\rho\) are needed.

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 7 (bilinear sums and the sharp prime cutoff) and Appendix A.5. https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026

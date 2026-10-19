# Rigidity of first-letter identities

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves a rigidity theorem about a bounded linear map \(R\) on a finite von Neumann algebra. Suppose that on all words in a free family of Haar unitaries with pairwise distinct indices, \(R\) acts as left multiplication by \(a\) when the first letter is a generator and by \(b\) when it is the inverse of one. Then \(a=b\). The theorem is the decisive step in the Liouville theorem of a later lesson, which in turn produces the bounded primitives for Hochschild cocycles. Its proof is self-contained apart from basic facts about tracial von Neumann algebras: a norm estimate of Haagerup for free groups (Section 1), an expansion of block products with repeated indices discarded (Section 2), the computation of a polar unitary through Catalan numbers (Section 3), and a spectral argument with bounded sine sums (Section 4).

**Prerequisites.** [*The cohomology problem*](the-cohomology-problem.md), Section 2 (tracial ultrapowers and maps continuous on balls in the \(2\)-norm). From *Foundations of von Neumann algebras*: [*The spectral theorem for bounded self-adjoint operators*](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators) (Borel functional calculus and spectral projections); [*C\*-algebras: continuous functional calculus, automatic continuity, positive cones*](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones); [*Projections and types of von Neumann algebras*](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras) (finite algebras: an isometry is a unitary).

**Notation.** \((N,\tau)\) is a finite von Neumann algebra with a faithful normal tracial state, \(\|x\|_2=\tau(x^*x)^{1/2}\), and \(\|x\|\) is the operator norm. In a tracial algebra \(\|xyz\|_2\le\|x\|\,\|y\|_2\,\|z\|\). A unitary \(u\) is *Haar* if \(\tau(u^k)=0\) for all \(k\ne0\); unitaries \(g_1,g_2,\ldots\) form a *free Haar family* if \(\tau(w(g))=0\) for every nonidentity reduced word \(w\) in the free group \(\mathbb F\) on generators \(x_1,x_2,\ldots\). Then distinct reduced words \(w(g)\) are orthonormal in \(L^2(N,\tau)\). A *signed word* is \(w=x_{i_1}^{\varepsilon_1}\cdots x_{i_q}^{\varepsilon_q}\) with \(\varepsilon_j=\pm1\); its *unsigned indices* are \(i_1,\ldots,i_q\).

**Theorem 0.1 (rigidity).** Let \(R:N\to N\) be bounded and complex linear, continuous on operator-norm balls for the \(2\)-norm: \(\|R(x_n)\|_2\to0\) whenever \(\sup_n\|x_n\|<\infty\) and \(\|x_n\|_2\to0\). Let \((g_j)_{j\ge1}\) be a free Haar family in \(N\) and \(a,b\in N\). Suppose that for every nonempty signed word \(w\) with pairwise distinct unsigned indices,
\[
R\bigl(w(g)\bigr)=\begin{cases}a\,w(g),&\varepsilon_1=1,\\ b\,w(g),&\varepsilon_1=-1.\end{cases}\quad(0.1)
\]
Then \(a=b\).

The proof constructs a unitary \(V\), in an ultrapower, with \(S(V^k)=aV^k\) and \(S(V^{-k})=bV^{-k}\) for all \(k\ge1\), where \(S\) is the induced map; Section 4 shows that these identities force \(a=b\). Powers of a single \(g_j\) repeat an index, so (0.1) does not apply to them. Instead \(V\) is the polar part of an average of many free generators.

## 1. Haagerup's length estimate

Let \(\lambda\) be the left regular representation of the free group \(\mathbb F_r\) on \(\ell^2(\mathbb F_r)\), and \(|w|\) the reduced length.

**Lemma 1.1.** For finitely many coefficients \(c_w\) on reduced words of length \(q\ge0\),
\[
\Bigl\|\sum_{|w|=q}c_w\lambda(w)\Bigr\|\le(q+1)\Bigl(\sum_{|w|=q}|c_w|^2\Bigr)^{1/2}.
\]
If \(g_1,\ldots,g_r\) is a free Haar family in a von Neumann algebra with a faithful tracial state, then every polynomial \(p\) in the \(g_i^{\pm1}\) has \(\|p(g)\|=\|p(\lambda)\|\); so the estimate holds with \(w(g)\) in place of \(\lambda(w)\), and its right side equals \((q+1)\|\sum_wc_ww(g)\|_2\).

**Proof.** Let \(L=\sum_{|w|=q}c_w\lambda(w)\) act on the basis vectors \(\delta_x\), \(x\in\mathbb F_r\). The product \(wx\) of two reduced words cancels some number \(t\in\{0,\ldots,q\}\) of letters at the junction; split \(L=\sum_{t=0}^qL_t\) accordingly. For fixed \(t\), the products with exactly \(t\) cancellations are those with
\[
\begin{gathered}
w=uv,\qquad x=v^{-1}h,\qquad wx=uh,\\
|u|=q-t,\quad |v|=t,
\end{gathered}
\]
where \(uv\), \(v^{-1}h\) and \(uh\) are all reduced. An input word of length at least \(t\) determines its prefix of length \(t\), hence \(v\) and \(h\); an output word of length at least \(q-t\) determines \(h\) by deleting its prefix of length \(q-t\). So the inputs, and the outputs, split into orthogonal blocks indexed by \(h\), and \(L_t\) is the direct sum of matrices \(B_h\) with rows indexed by \(u\), columns by \(v\), and entries \(c_{uv}\) or \(0\). Since \((u,v)\mapsto uv\) is injective for fixed lengths, the Hilbert–Schmidt norm of each \(B_h\) is at most \((\sum|c_w|^2)^{1/2}\), and so is \(\|L_t\|=\sup_h\|B_h\|\). Summing over the \(q+1\) values of \(t\) gives the estimate.

For the transfer, recall that for \(A\ge0\) in a von Neumann algebra with faithful tracial state \(\rho\),
\[
\|A\|=\lim_{n\to\infty}\rho(A^n)^{1/n}.
\]
The inequality \(\le\) is \(\rho(A^n)\le\|A\|^n\). Conversely, for \(0<c<\|A\|\), the spectral projection \(e=1_{(c,\infty)}(A)\) is nonzero, so \(\rho(e)>0\) and \(\rho(A^n)\ge c^n\rho(e)\); take \(n\)-th roots and let \(c\uparrow\|A\|\). The free Haar moments give \(\tau((p(g)^*p(g))^n)=\tau_{\mathbb F_r}((p(\lambda)^*p(\lambda))^n)\) for every \(n\), where \(\tau_{\mathbb F_r}(x)=\langle x\delta_e,\delta_e\rangle\) is the trace of the free group von Neumann algebra, faithful because \(\delta_e\) is cyclic for the right regular representation, which commutes with \(\lambda\); hence \(\|p(g)\|=\|p(\lambda)\|\). Orthonormality of reduced words gives the \(2\)-norm. \(\square\)

The check script of this course tests Lemma 1.1 on truncations of \(\lambda\) for \(\mathbb F_2\) and \(q\le3\).

For the rest of the lesson, assume the hypotheses of Theorem 0.1. Put
\[
s_r=r^{-1/2}\sum_{j=1}^rg_j .
\]
By Lemma 1.1 with \(q=1\), \(\|s_r\|_2=1\) and \(\|s_r\|\le2\). Fix a free ultrafilter \(\omega\) on \(\mathbb N\) and put
\[
\begin{gathered}
\widehat N=N^\omega,\qquad S=R^\omega,\\
s=(s_r)_\omega\in\widehat N .
\end{gathered}
\]
By Lemma 2.2 of the lesson on the cohomology problem, \(S\) is bounded and continuous on operator-norm balls for the \(2\)-norm. We identify \(a,b\) with their constant images in \(\widehat N\).

## 2. Ordered blocks

For \(d\ge0\) put \(B_d(z)=z(z^*z)^d\). The powers of the polar part of \(s\) will be approximated by polynomials whose literal expansions are products of such blocks.

**Lemma 2.1.** For \(k\ge1\) and \(d_1,\ldots,d_k\ge0\), let \(P(z)=B_{d_1}(z)\cdots B_{d_k}(z)\). Then
\[
\begin{gathered}
S\bigl(P(s)\bigr)=a\,P(s),\\
S\bigl(P(s)^*\bigr)=b\,P(s)^* .
\end{gathered}
\]

**Proof.** Let \(L=\sum_j(2d_j+1)\) be the degree of \(P\).

*Endpoint signs.* Expanding \(B_d(s_r)\) gives words whose sign patterns alternate \(+,-,+,\ldots,+\), with one more plus than minus. Free reduction deletes adjacent pairs of opposite signs, so the reduced word is nonempty, alternates, and begins and ends with \(+\). At the junction of two blocks two plus letters meet, and nothing cancels. So every reduced word occurring in \(P(s_r)\) is nonempty and begins and ends with a positive letter; for \(P(s_r)^*\) the signs are reversed.

*Coefficients.* Write \(P(s_r)=\sum_{q=1}^L\sum_{|w|=q}c_w(r)\,w(g)\). An original term of the expansion is a string of \(L\) letters with coefficient \(r^{-L/2}\). Record its free reduction, carried out from left to right against the last surviving letter, as a noncrossing partial matching of the \(L\) positions: matched pairs are the cancelling pairs, and the unmatched positions spell the reduced word \(w\). There are at most \(3^L\) noncrossing partial matchings of \(L\) positions (mark each position as opening, closing or unmatched; a closing position is matched with the last unmatched opening one, so the marking determines the matching). For fixed \(w\) of length \(q\) and a fixed matching, the unmatched labels are those of \(w\), and each of the \((L-q)/2\) pairs has at most \(r\) labels. Hence
\[
\begin{aligned}
|c_w(r)|&\le3^L\,r^{(L-q)/2}\,r^{-L/2}\\
&=3^Lr^{-q/2}.\qquad(2.1)
\end{aligned}
\]

*Repeated indices.* Let \(E_{r,q}\) be the sum of the terms with \(|w|=q\) whose reduced word repeats an unsigned index; \(E_{r,1}=0\). For \(q\ge2\) there are at most \(2^q\binom q2r^{q-1}\) such words (choose two positions with equal labels, the remaining labels, and the signs). By orthonormality and (2.1), \(\|E_{r,q}\|_2^2\le9^L2^q\binom q2r^{-1}\), and by Lemma 1.1,
\[
\begin{aligned}
\|E_r\|&\le\sum_{q=2}^L(q+1)\|E_{r,q}\|_2\\
&=O_L(r^{-1/2}),\qquad E_r=\sum_qE_{r,q}.
\end{aligned}
\]

*Conclusion.* \(Q_r=P(s_r)-E_r\) is a finite sum of words with pairwise distinct unsigned indices, all beginning with a positive letter, so (0.1) gives \(R(Q_r)=aQ_r\). Hence
\[
\begin{aligned}
&\|R(P(s_r))-aP(s_r)\|\\
&\quad\le(\|R\|+\|a\|)\,\|E_r\|\to0,
\end{aligned}
\]
and, \(P(s_r)\) being bounded by \(2^L\), the identity \(S(P(s))=aP(s)\) holds in \(\widehat N\). For the adjoint, \(Q_r^*\) consists of words with distinct indices beginning with a negative letter, and the same estimate with \(b\) gives the second identity. \(\square\)

## 3. A polar unitary

**Lemma 3.1.** Let \(A=s^*s\). Then \(\widehat\tau(A^d)=C_d=\frac1{d+1}\binom{2d}d\) for all \(d\ge0\), the spectral distribution of \(A\) is
\[
d\nu(x)=\frac1{2\pi}\sqrt{\frac{4-x}{x}}\;1_{(0,4)}(x)\,dx,
\]
and the polar part \(V\) of \(s=VA^{1/2}\) is a unitary.

**Proof.** \(\tau((s_r^*s_r)^d)\) is \(r^{-d}\) times the number of labellings, by \(\{1,\ldots,r\}\), of \(2d\) positions with alternating signs \(-,+,\ldots,-,+\) whose word reduces to the identity. A reduction to the identity matches all positions in a noncrossing way, so at most \(d\) distinct labels occur; labellings with at most \(d-1\) labels number \(O_d(r^{d-1})\). If exactly \(d\) labels occur, each occurs twice and its two positions are matched, so the labelling determines a noncrossing perfect matching, each of whose pairs joins positions of opposite parity, hence of opposite sign (a pair encloses an even number of positions, matched among themselves). Conversely, every noncrossing perfect matching with distinct labels on its pairs gives an identity word, by cancelling innermost pairs. So the count is \(C_d\,r(r-1)\cdots(r-d+1)+O_d(r^{d-1})\), where \(C_d\) is the number of noncrossing perfect matchings of \(2d\) points. Matching the first point gives \(C_0=1\), \(C_d=\sum_{j=0}^{d-1}C_jC_{d-1-j}\), so the generating function satisfies \(C(z)=1+zC(z)^2\) and \(C_d=\frac1{d+1}\binom{2d}d\). Hence \(\widehat\tau(A^d)=\lim_{r\to\omega}\tau((s_r^*s_r)^d)=C_d\).

For the measure, substitute \(x=4t\) and use the beta integral:
\[
\begin{aligned}
&\int_0^4x^d\,d\nu(x)\\
&=\frac{4^{d+1}}{2\pi}\int_0^1t^{d-1/2}(1-t)^{1/2}\,dt\\
&=\frac{4^{d+1}}{2\pi}\cdot\frac{\Gamma(d+\frac12)\Gamma(\frac32)}{\Gamma(d+2)}\\
&=C_d .
\end{aligned}
\]
Both \(\nu\) and the spectral distribution \(\mu_A(f)=\widehat\tau(f(A))\) are probability measures on \([0,4]\), since \(0\le A\le4\); equal moments give equal integrals of polynomials, hence of continuous functions by Weierstrass approximation, so \(\mu_A=\nu\). Since \(\nu\) has no atom at \(0\), \(\widehat\tau(1_{\{0\}}(A))=0\), and \(1_{\{0\}}(A)=0\) by faithfulness. In the polar decomposition, \(V^*V\) is the support projection of \(A\), here \(1\); in the finite algebra \(\widehat N\), \(\widehat\tau(1-VV^*)=1-\widehat\tau(V^*V)=0\), so \(VV^*=1\). \(\square\)

**Lemma 3.2.** For every \(k\ge1\), \(S(V^k)=aV^k\) and \(S(V^{-k})=bV^{-k}\).

**Proof.** For \(\varepsilon>0\) put \(x_\varepsilon=s(A+\varepsilon)^{-1/2}=V\bigl(A/(A+\varepsilon)\bigr)^{1/2}\), a contraction. For a polynomial \(p(t)=\sum_{d=0}^Dc_dt^d\), expanding without commuting factors,
\[
\begin{aligned}
[s\,p(A)]^k&=\sum_{d_1,\ldots,d_k}c_{d_1}\cdots c_{d_k}\\
&\qquad\cdot B_{d_1}(s)\cdots B_{d_k}(s),
\end{aligned}
\]
so Lemma 2.1 gives \(S([sp(A)]^k)=a[sp(A)]^k\), and, taking adjoints of the expansion, \(S(([sp(A)]^k)^*)=b([sp(A)]^k)^*\). Let \(p\) run through polynomials converging uniformly on \([0,4]\) to \((t+\varepsilon)^{-1/2}\); norm continuity of \(S\) gives \(S(x_\varepsilon^k)=ax_\varepsilon^k\) and \(S((x_\varepsilon^k)^*)=b(x_\varepsilon^k)^*\). Next,
\[
\begin{aligned}
\|x_\varepsilon-V\|_2^2&=\int_0^4\Bigl(\sqrt{\tfrac{x}{x+\varepsilon}}-1\Bigr)^2d\nu(x)\\
&\to0\qquad(\varepsilon\to0)
\end{aligned}
\]
by dominated convergence, \(\nu\) having no atom at \(0\); and \(x_\varepsilon^k-V^k=\sum_{j=0}^{k-1}x_\varepsilon^j(x_\varepsilon-V)V^{k-1-j}\) gives \(\|x_\varepsilon^k-V^k\|_2\le k\|x_\varepsilon-V\|_2\), likewise for adjoints. All these elements are contractions, so the continuity of \(S\) on the unit ball for the \(2\)-norm passes the identities to \(V^k\) and \(V^{-k}=(V^k)^*\). \(\square\)

## 4. The spectral conclusion

**Lemma 4.1.** For all \(m\ge1\) and \(\theta\in\mathbb R\), \(\bigl|\sum_{k=1}^m\frac{\sin k\theta}k\bigr|\le1+\pi\).

**Proof.** By periodicity and oddness assume \(t=\theta\in(0,\pi]\) (the sum vanishes at \(\theta=0\)). Put \(K=\lfloor1/t\rfloor\). The terms with \(k\le\min(K,m)\) contribute at most \(Kt\le1\), since \(|\sin kt|\le kt\). For integers \(p\le q\),
\[
\begin{aligned}
\Bigl|\sum_{k=p}^q\sin kt\Bigr|&\le\Bigl|\sum_{k=p}^qe^{ikt}\Bigr|\\
&\le\frac1{\sin(t/2)}\le\frac\pi t ,
\end{aligned}
\]
using \(\sin(t/2)\ge t/\pi\) on \([0,\pi]\). If \(m\ge K+1\), Abel summation with \(A_j=\sum_{k=K+1}^j\sin kt\) gives
\[
\begin{aligned}
&\Bigl|\sum_{k=K+1}^m\frac{\sin kt}k\Bigr|\\
&=\Bigl|\frac{A_m}m+\sum_{j=K+1}^{m-1}A_j\Bigl(\frac1j-\frac1{j+1}\Bigr)\Bigr|\\
&\le\frac\pi t\cdot\frac1{K+1}\le\pi .\qquad\square
\end{aligned}
\]

(The supremum is in fact the Wilbraham–Gibbs constant \(1.8519\ldots\); only boundedness matters.)

**Lemma 4.2.** Let \((\mathcal A,\rho)\) be a finite von Neumann algebra with faithful normal tracial state, \(V\in\mathcal A\) unitary, and \(S:\mathcal A\to\mathcal A\) bounded and linear with \(S(V^k)=aV^k\) and \(S(V^{-k})=bV^{-k}\) for all \(k\ge1\). Then \(a=b\).

**Proof.** Put \(H_m(z)=\sum_{k=1}^mz^k/k\) and \(h_m=\sum_{k=1}^m1/k\). For \(\lambda\) on the unit circle write \(H_m(\lambda V)=X+iY\) with \(X=X^*\), \(Y=Y^*\); by the functional calculus and Lemma 4.1, \(\|Y\|\le B:=1+\pi\). The identities give
\[
\begin{aligned}
&S\bigl(H_m(\lambda V)-H_m(\lambda V)^*\bigr)\\
&=aH_m(\lambda V)-bH_m(\lambda V)^*\\
&=(a-b)X+i(a+b)Y .
\end{aligned}
\]
The argument of \(S\) is \(2iY\), of norm at most \(2B\). Hence, with \(c=a-b\) and \(C:=B\,(2\|S\|+\|a\|+\|b\|)\),
\[
\|cX\|\le C\qquad(4.1)
\]
uniformly in \(m\) and \(\lambda\). Let \(I\) be a half-open arc of the circle of length at most \(1/m\), with spectral projection \(e=1_I(V)\), and choose \(\lambda\) rotating the midpoint of \(I\) to \(1\). On the rotated arc \(|\theta|\le1/(2m)\), and \(\operatorname{Re}H_m(e^{i\theta})=\sum_k\frac{\cos k\theta}k\ge\cos(1)h_m\). By the Borel functional calculus there is \(F\in W^*(V)\), equal to \(1/X\) on \(I\) and \(0\) off \(I\), with \(XF=e\) and \(\|F\|\le1/(\cos(1)h_m)\). Multiplying (4.1) on the right by \(F\),
\[
\begin{gathered}
\|ce\|\le\delta_m:=\frac{C}{\cos(1)\,h_m},\\
\text{so}\quad ec^*ce\le\delta_m^2e .
\end{gathered}
\]
Partition the circle into finitely many half-open arcs of length at most \(1/m\), with spectral projections \(e_1,\ldots,e_J\), orthogonal with sum \(1\). By traciality,
\[
\begin{aligned}
\|c\|_2^2&=\sum_j\rho(c^*ce_j)\\
&=\sum_j\rho(e_jc^*ce_j)\\
&\le\delta_m^2\sum_j\rho(e_j)=\delta_m^2 .
\end{aligned}
\]
Since \(h_m\ge\log(m+1)\to\infty\), \(\|c\|_2=0\), and \(c=0\) by faithfulness. \(\square\)

The finiteness of the trace is essential: on \(\ell^2(\mathbb Z)\) with the bilateral shift \(V\), the projection \(p\) onto \(\mathbb Ce_0\) and the projection \(q\) onto the span of the \(e_n\), \(n<0\), the map \(S(X)=pXq\) satisfies \(S(V^k)=pV^k\) and \(S(V^{-k})=0\) for all \(k\ge1\) (Exercise 5.4).

**Proof of Theorem 0.1.** Lemma 3.2 gives a unitary \(V\in\widehat N\) with \(S(V^k)=aV^k\) and \(S(V^{-k})=bV^{-k}\), and Lemma 4.2 gives \(a=b\) in \(\widehat N\). The constant embedding \(N\to\widehat N\) preserves the faithful trace, so \(a=b\) in \(N\). \(\square\)

## 5. Exercises

**5.1** (easy). Show that distinct reduced words in a free Haar family are orthonormal for the \(2\)-norm, and deduce \(\|s_r\|_2=1\).

**5.2** (medium). Compute \(\tau((s_r^*s_r)^2)\) exactly, and check that it tends to \(C_2=2\).

**5.3** (medium). Show that the number of noncrossing partial matchings of \(L\) points satisfies \(M_L=M_{L-1}+\sum_{j=1}^{L-1}M_{j-1}M_{L-j-1}\), and that \(M_L\le3^L\).

**5.4** (medium). Verify the counterexample after Lemma 4.2: \(S(V^k)=pV^k\) and \(S(V^{-k})=0\) for \(k\ge1\).

**5.5** (medium). Show by an example in \(M_2(\mathbb C)\), with its normalized trace, that the conclusion of Lemma 4.2 can fail if the identities are assumed only for \(k=1\).

## 6. Solutions

**5.1.** For reduced words \(u\ne v\), \(v^{-1}u\) reduces to a nonidentity word, so \(\langle u(g),v(g)\rangle=\tau(v(g)^*u(g))=0\), while \(\tau(u^*u)=1\). So \(\|s_r\|_2^2=r^{-1}\sum_{j}\|g_j\|_2^2=1\).

**5.2.**
\[
\begin{aligned}
&\tau((s_r^*s_r)^2)=r^{-2}\#\{(i,j,k,l):\\
&\qquad g_i^{-1}g_jg_k^{-1}g_l\text{ reduces to }e\}.
\end{aligned}
\]
The reduction to the identity needs \(i=j\), \(k=l\) or \(j=k\), \(l=i\) (the two noncrossing matchings), giving \(2r^2-r\) solutions (the overlap \(i=j=k=l\) counted once). So the value is \(2-1/r\to2\).

**5.3.** Either the first point is unmatched, leaving \(L-1\) points, or it is matched with point \(j+1\), splitting the remaining points into \(j-1\) inside and \(L-j-1\) outside, matched independently. The bound \(3^L\) is the marking argument in the proof of Lemma 2.1.

**5.4.** \(V^k\) maps \(e_n\) to \(e_{n+k}\). \(pV^kq\) is nonzero only on inputs \(e_n\), \(n<0\), with \(n+k=0\), that is on \(e_{-k}\), where it equals \(pV^k\). For \(V^{-k}\), \(pV^{-k}q\) needs \(n-k=0\) with \(n<0\), impossible. And \(pV^k\) is also supported on \(e_{-k}\), so \(pV^kq=pV^k\).

**5.5.** Let \(V=\operatorname{diag}(1,i)\), so \(V^{-1}=\operatorname{diag}(1,-i)\); these two matrices are linearly independent. Extend them by \(E_{12},E_{21}\) to a basis of \(M_2(\mathbb C)\) and define \(S\) linearly by \(S(V)=V\), \(S(V^{-1})=0\), \(S(E_{12})=S(E_{21})=0\). Then \(S(V)=aV\) and \(S(V^{-1})=bV^{-1}\) with \(a=1\ne0=b\). The identities fail for \(k=2\), as Lemma 4.2 requires: \(V^2=\operatorname{diag}(1,-1)=\frac{1+i}2V+\frac{1-i}2V^{-1}\), so \(S(V^2)=\frac{1+i}2V\ne V^2=aV^2\).

## Sources

- [OpenAI-295] OpenAI, *Vanishing of higher bounded Hochschild cohomology*, OpenAI Math Release preprint, 23 September 2026, Section 4 (the rigidity theorem). https://github.com/openai/math/tree/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
- U. Haagerup, *An example of a non nuclear C\*-algebra, which has the metric approximation property*, Invent. Math. 50 (1979), 279–293, Lemma 1.4; freely readable through the Göttingen digitization centre (GDZ). The length estimate of Section 1.

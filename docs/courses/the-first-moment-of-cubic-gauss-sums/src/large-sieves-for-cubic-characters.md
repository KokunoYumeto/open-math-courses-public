# Large sieves for cubic characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the first moment for cubic Gauss sums is an argument with exponents: every sum is bounded by an inequality whose shape depends on the lengths of its variables, and the theorem follows when the exponents leave a gap. This lesson collects the inequalities and the arithmetic inputs. Section 1 fixes conventions for the estimates. Section 2 proves Poisson summation over the Eisenstein integers, and Section 3 deduces the large sieve for characters of bounded conductor. Section 4 states Heath-Brown's cubic large sieve and extends it to the coefficient classes needed later. Section 5 records two Hilbert-space inequalities, and Section 6 treats the Hecke characters of \(\mathbb Q(\omega)\): their functional equation, the characters attached to elements, and the prime number theorems with uniform conductor dependence.

**Prerequisites.** The previous lesson, [*Cubic Gauss sums and Patterson's conjecture*](cubic-gauss-sums-and-pattersons-conjecture.md), whose notation is kept. From *Harmonic analysis on locally compact abelian groups*: [*The Fourier inversion theorem and the dual Haar measure*](course:HA-LCA/src/the-fourier-inversion-theorem-and-the-dual-haar-measure), Theorem 2.1; [*The Poisson summation formula*](course:HA-LCA/src/the-poisson-summation-formula), Corollary 2.2. From *The Riemann zeta function*: [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1 (Mertens); [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03), Theorem 3.1; [*Mean values of Dirichlet polynomials and zeta*](course:NT-ZETA/NT-ZETA-16), Theorem 2.1. From *Adèles, idèles and Tate's thesis*: [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06), Theorem 6.3; [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10), Theorem 10.1. From *Class field theory*: [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws), Proposition 23.2; [*Ray class fields, conductors and ideal reciprocity*](course:NT-CFT/ray-class-fields-conductors-and-ideal-reciprocity), Theorem 18.2 and Proposition 18.3.

## 1. Conventions

Throughout the course \(X\) is a large parameter and \(L=\log X\). All lengths are norms: a variable \(n\) *of length \(Y\)* has \(N(n)\) in a dyad \([Y,2Y)\), or more generally in an interval \([Y,c_0Y)\) with a fixed \(c_0>1\). All lengths and heights that occur are bounded by fixed powers of \(X\). For the ideal divisor function \(\tau\), a sequence \((v_n)\) is *divisor-bounded* if \(|v_n|\le L^C\tau(n)^C\) for a fixed \(C\). The notation \(\ll_\epsilon X^\epsilon\) allows an arbitrarily small fixed exponent, chosen after all other fixed parameters.

**Lemma 1.1 (counting ideals).** (a) The number of ideals of norm \(m\) is at most the number \(d(m)\) of divisors of \(m\).

(b) \(\tau(n)\le d(N(n))^2\) for every nonzero ideal \(n\).

(c) For every fixed \(B\ge1\) and \(Y\ge2\), \(\sum_{m\le Y}d(m)^B\ll_BY(\log Y)^{2^B}\). Consequently a divisor-bounded sequence has \(\sum_{N(n)<2Y}|v_n|^k\ll Y L^{O(1)}\) for every fixed \(k\), also after the coefficients with the same norm are added together.

**Proof.** (a) An ideal of norm \(m\) is a product of ideals of norm \(p^e\), one for each \(p^e\) exactly dividing \(m\). By Lemma 1.2 of the previous lesson there are \(e+1\) of them for split \(p\), at most one for inert \(p\), and one for \(p=3\).

(b) If \(p\) splits and \(\mathfrak p^i\bar{\mathfrak p}^j\) exactly divides \(n\), the factor \((i+1)(j+1)\) of \(\tau(n)\) is at most \((i+j+1)^2\), the square of the factor of \(d(N(n))\) at \(p\). Inert and ramified primes are similar.

(c) We have
\[
\begin{aligned}
\sum_{m\le Y}d(m)^B&\le Y\sum_{m\le Y}\frac{d(m)^B}m\\
&\le Y\prod_{p\le Y}\Bigl(1+\frac{2^B}p+\frac{c_B}{p^2}\Bigr),
\end{aligned}
\]
and Mertens' theorem bounds the product by \(O_B((\log Y)^{2^B})\). For the consequence use (a), (b) and \(\tau(n)\le d(N(n))^2\). \(\square\)

**Mellin transforms.** For a smooth function \(W\) with compact support in \((0,\infty)\) put
\[
\mathcal MW(s)=\int_0^\infty W(v)\,v^s\,\frac{dv}v .
\]

**Lemma 1.2.** \(\mathcal MW\) is entire. For every \(j\ge0\) and \(s=\sigma+it\ne0\),
\[
|\mathcal MW(s)|\le\frac{\int_0^\infty|(v\partial_v)^jW(v)|\,v^{\sigma}\,dv/v}{|s|^j},
\]
and for every \(\sigma\) and \(v>0\),
\[
W(v)=\frac1{2\pi i}\int_{(\sigma)}\mathcal MW(s)\,v^{-s}\,ds .
\]

**Proof.** Entireness is differentiation under the integral sign over a compact set. Integrating by parts \(j\) times with \(v\partial_v\) multiplies the transform by \((-s)^{-j}\). With \(v=e^{-x}\), the function \(t\mapsto\mathcal MW(\sigma+it)\) is the Fourier transform at \(t/(2\pi)\) of the smooth compactly supported function \(x\mapsto W(e^{-x})e^{-\sigma x}\), and the inversion formula is Theorem 2.1 of the Fourier inversion lesson on \(\mathbb R\). \(\square\)

So a smooth weight in a product or quotient of variables separates into products of powers: \(W(xy)=\frac1{2\pi i}\int_{(0)}\mathcal MW(s)x^{-s}y^{-s}\,ds\), with an integrable weight decreasing faster than every power of \(|s|\). When \(W\) depends on parameters, the decay constants are controlled by its derivative bounds. If the derivatives of order \(j\) are \(O(L^{Cj})\), then for \(|t|\ge L^{C+1}\) the transform is smaller than every fixed negative power of \(L\), and similarly for power scales.

**The plane measure.** Identify \(\mathbb C\) with \(\mathbb R^2\) and put
\[
\begin{gathered}
d\mathfrak m(z)=\frac2{\sqrt3}\,d(\operatorname{Re}z)\,d(\operatorname{Im}z),\\
\widehat W(y)=\int_{\mathbb C}W(z)\,e(-\operatorname{Tr}(zy))\,d\mathfrak m(z).
\end{gathered}
\]
The parallelogram spanned by \(1\) and \(\omega\) has area \(\sqrt3/2\), so \(\mathcal O\) has covolume one for \(\mathfrak m\).

## 2. Poisson summation over \(\mathcal O\)

**Lemma 2.1.** Let \(W\) be a Schwartz function on \(\mathbb C\), \(b\in\mathcal O\) nonzero, and \(c\in\mathcal O\). Then
\[
\begin{aligned}
\sum_{\substack{x\in\mathcal O\\ x\equiv c\ (b)}}W(x)
&=\frac1{N(b)}\sum_{y\in\lambda^{-1}\mathcal O}e\Bigl(\operatorname{Tr}\frac{cy}b\Bigr)\\
&\qquad\cdot\widehat W\Bigl(\frac yb\Bigr).
\end{aligned}
\]

**Proof.** Write \(z=s+it\) and \(y=u+iv\). Then \(\operatorname{Tr}(zy)=2(su-tv)\) is the Euclidean product of \((s,t)\) with \(\xi(y)=(2u,-2v)\). If \(\varphi\) denotes \(W\) as a function on \(\mathbb R^2\) and \(\hat\varphi\) its Euclidean Fourier transform, then \(\widehat W(y)=\frac2{\sqrt3}\hat\varphi(\xi(y))\). The lattice \(\Lambda=b\mathcal O\) has Euclidean covolume \(\frac{\sqrt3}2N(b)\). Its dual lattice consists of the vectors \(\xi(y)\) with \(\operatorname{Tr}(y\,b\mathcal O)\subseteq\mathbb Z\), that is, by Lemma 1.3(a) of the previous lesson, with \(y\in b^{-1}\lambda^{-1}\mathcal O\). Corollary 2.2 of the Poisson summation lesson, applied at the point \(c\), gives
\[
\begin{aligned}
&\sum_{x\in c+b\mathcal O}W(x)\\
&=\frac2{\sqrt3\,N(b)}\sum_{y\in b^{-1}\lambda^{-1}\mathcal O}\hat\varphi(\xi(y))\\
&\qquad\cdot e(\operatorname{Tr}(cy)).
\end{aligned}
\]
Replace \(\hat\varphi(\xi(y))\) by \(\frac{\sqrt3}2\widehat W(y)\) and \(y\) by \(y/b\). \(\square\)

If \(W_Z(z)=W(z/\sqrt Z)\), then \(\widehat{W_Z}(y)=Z\,\widehat W(\sqrt Zy)\).

## 3. The large sieve for characters of bounded conductor

**Lemma 3.1 (the planar large sieve).** Let \(Z\ge1\) and \(0<\delta\le\frac12\). Let \(y_1,\ldots,y_R\in\mathbb C\) satisfy \(|y_r-y_s-\ell|\ge\delta\) for all \(r\ne s\) and all \(\ell\in\lambda^{-1}\mathcal O\). Then for all complex \(v_n\) supported on \(n\in\mathcal O\) with \(N(n)\le Z\),
\[
\begin{aligned}
&\sum_{r=1}^R\Bigl|\sum_nv_n\,e(\operatorname{Tr}(ny_r))\Bigr|^2\\
&\qquad\ll\bigl(Z+\delta^{-2}\bigr)\sum_n|v_n|^2 .
\end{aligned}
\]

**Proof.** By duality it suffices to prove the same bound for \(\sum_n|\sum_rc_re(\operatorname{Tr}(ny_r))|^2\), for all \(c\in\mathbb C^R\). Let \(\Phi(z)=e^{\pi(1-|z|^2)}\), which is at least \(1\) for \(|z|\le1\), and \(\phi(z)=\Phi(z/\sqrt Z)\). Then
\[
\begin{aligned}
&\sum_{N(n)\le Z}\Bigl|\sum_rc_re(\operatorname{Tr}(ny_r))\Bigr|^2\\
&\le\sum_{r,s}c_r\bar c_s\sum_{n\in\mathcal O}\phi(n)\\
&\qquad\cdot e(\operatorname{Tr}(n(y_r-y_s))).
\end{aligned}
\]
By Lemma 2.1 with \(b=1\), applied to \(z\mapsto\phi(z)e(\operatorname{Tr}(zw))\), the inner sum is
\[
\begin{gathered}
K(w)=Z\sum_{\ell\in\lambda^{-1}\mathcal O}\widehat\Phi\bigl(\sqrt Z(\ell-w)\bigr),\\
w=y_r-y_s .
\end{gathered}
\]
Since \(|c_rc_s|\le\frac12(|c_r|^2+|c_s|^2)\) and \(|K(w)|=|K(-w)|\), the double sum is at most \(\max_r\sum_s|K(y_r-y_s)|\) times \(\sum|c_r|^2\).

The points \(y_s+\ell\), with \(s\le R\) and \(\ell\in\lambda^{-1}\mathcal O\), are pairwise at distance at least \(\delta\): for different \(s\) by hypothesis, and for equal \(s\) because nonzero elements of \(\lambda^{-1}\mathcal O\) have length at least \(1/\sqrt3>\delta\). Disjoint discs of radius \(\delta/2\) around those within distance \(\rho\) of \(y_r\) lie in a disc of radius \(\rho+\delta/2\), so there are at most \((1+2\rho/\delta)^2\) of them. With \(|\widehat\Phi(y)|\ll(1+|y|)^{-4}\) we get
\[
\begin{aligned}
&\sum_s|K(y_r-y_s)|\\
&\ll Z\sum_{k\ge0}(1+k)^{-4}\Bigl(1+\frac{2(k+1)}{\sqrt Z\,\delta}\Bigr)^2\\
&\ll Z+\delta^{-2}. \qquad\square
\end{aligned}
\]

For a primary squarefree \(r\), a character \(\xi\) of \((\mathcal O/r\mathcal O)^\times\) is *primitive* if each of its local components, at the primes dividing \(r\), is nontrivial. We extend it by zero to all of \(\mathcal O\).

**Lemma 3.2.** Let \(r\) be primary and squarefree and \(\xi\) primitive modulo \(r\). Then
\[
\begin{gathered}
\sum_{v\bmod r}\xi(v)\,e\Bigl(\operatorname{Tr}\frac{hv}r\Bigr)\\
=\overline{\xi(h)}\,g(\xi)\quad(h\in\mathcal O),\\
|g(\xi)|=\sqrt{N(r)},
\end{gathered}
\]
where \(g(\xi)\) denotes the sum at \(h=1\).

**Proof.** For a prime \(r=\pi\) this is the computation of Proposition 3.1(b) and Exercise 6.4 of the previous lesson, which used only the nontriviality of the character. For a product of distinct primes the Chinese remainder theorem factors the sum as in Proposition 3.1(c), with a factor of absolute value one depending only on the primes. \(\square\)

**Lemma 3.3 (the ordinary character large sieve).** Let \(Q,Z\ge1\). For each primary squarefree \(r\) with \(N(r)\le Q\), let \(\Xi_r\) be a set of primitive characters modulo \(r\). Then for all complex \(v_n\) supported on primary \(n\) with \(N(n)\le Z\),
\[
\begin{aligned}
&\sum_{N(r)\le Q}\ \sum_{\xi\in\Xi_r}\Bigl|\sum_nv_n\,\xi(n)\Bigr|^2\\
&\qquad\ll(Z+Q^2)\sum_n|v_n|^2 .
\end{aligned}
\]
There is no loss of a power of \(Q\).

**Proof.** Put \(S(y)=\sum_nv_ne(\operatorname{Tr}(ny))\). Lemma 3.2 for \(\bar\xi\) gives \(\xi(n)g(\bar\xi)=\sum_{v\bmod r}\bar\xi(v)e(\operatorname{Tr}(nv/r))\) for every \(n\), so
\[
\sum_nv_n\xi(n)=\frac1{g(\bar\xi)}\sum_{v\bmod r}\bar\xi(v)\,S(v/r).
\]
Orthogonality of the characters of the group \((\mathcal O/r\mathcal O)^\times\), of order \(\varphi(r)\), gives
\[
\begin{aligned}
&\sum_{\xi\in\Xi_r}\Bigl|\sum_nv_n\xi(n)\Bigr|^2\\
&\qquad\le\frac{\varphi(r)}{N(r)}\sum_{\substack{v\bmod r\\ (v,r)=1}}|S(v/r)|^2 .
\end{aligned}
\]
The points \(v/r\), for primary squarefree \(r\) with \(N(r)\le Q\) and \(v\) prime to \(r\), are distinct modulo \(\lambda^{-1}\mathcal O\) and separated by \(1/(\sqrt3Q)\). Indeed, for \(\ell\in\lambda^{-1}\mathcal O\),
\[
\frac vr-\frac{v'}{r'}-\ell=\frac{\lambda(vr'-v'r)-\lambda\ell\,rr'}{\lambda rr'},
\]
and the numerator lies in \(\mathcal O\). If it vanished, then \(rr'\) would divide \(vr'-v'r\), as \(rr'\) is prime to \(\lambda\). Hence \(r\mid r'\) and \(r'\mid r\), so \(r=r'\) and \(v\equiv v'\pmod r\). Otherwise the numerator has absolute value at least \(1\). For \(Q\ge2\), Lemma 3.1 with \(\delta=1/(\sqrt3Q)\) finishes the proof. For \(Q<2\) only \(r=1\) occurs, and Lemma 3.1 with the single point \(0\) and \(\delta=\frac12\) applies. \(\square\)

The main application is to the cubic characters \(n\mapsto\chi_n(pq^2)\), indexed by coprime primary squarefree \(p,q\). By cubic reciprocity, \(\chi_n(pq^2)=\chi_p(n)\overline{\chi_q(n)}\) for primary \(n\), and this character is primitive modulo \(pq\). Different pairs \((p,q)\) give different characters, because the local component at a prime \(\pi\mid pq\) is \(\chi_\pi\) or \(\overline{\chi_\pi}\) according as \(\pi\) divides \(p\) or \(q\). A fixed additional factor of absolute value at most one, such as \(\chi_n(\zeta\lambda^j)\) with a unit \(\zeta\), is absorbed into the coefficients.

## 4. Heath-Brown's cubic large sieve

For cubic characters whose conductor is as long as the sums themselves, Lemma 3.3 gives \(Q^2\), whereas the following theorem gives \(Q^{4/3}\).

**Theorem 4.1 (Heath-Brown's cubic large sieve, N1).** Let \(A,B\ge1\), \(\epsilon>0\), and let \((\beta_b)\) be complex numbers supported on primary squarefree \(b\) with \(N(b)\le B\). Then
\[
\begin{aligned}
&\sum_{N(a)\le A}\mu^2(a)\Bigl|\sum_b\beta_b\,\chi_a(b)\Bigr|^2\\
&\ll_\epsilon\bigl(A+B+(AB)^{2/3}\bigr)\\
&\qquad\cdot(AB)^\epsilon\sum_b|\beta_b|^2 ,
\end{aligned}
\]
the outer sum running over primary \(a\).

This is Heath-Brown's Theorem 2 in *Kummer's conjecture for cubic Gauss sums* (2000), stated in this form as Theorem 9.1 of [DR]. It is used without proof in the programme. By reciprocity the same bound holds with \(\chi_b(a)\) in place of \(\chi_a(b)\), since both vanish unless \(a\) and \(b\) are coprime.

The squarefree hypotheses on both variables are essential in Theorem 4.1. The next lemma removes them at the cost of an arbitrarily small power of \(X\).

**Lemma 4.2 (extensions of the cubic large sieve).** Let \(P,Z,J\ge1\) be bounded by fixed powers of \(X\), and \(\epsilon>0\).

(a) Let \((v_n)\) be divisor-bounded and supported on primary \(n\) of length \(Z\). Then
\[
\begin{aligned}
&\sum_{\substack{N(a)<2P}}\mu^2(a)\Bigl|\sum_nv_n\chi_a(n)\Bigr|^2\\
&\qquad\ll_\epsilon X^\epsilon Z\bigl(P+Z+(PZ)^{2/3}\bigr).
\end{aligned}
\]
If \(v\) is supported on \(n=st^2c^3\), with \(s,t\) coprime and squarefree and with \(N(s),N(t),N(c)\) of lengths \(S,V,C\), then the bound can be replaced by
\[
X^\epsilon(VC)^2S\bigl(P+S+(PS)^{2/3}\bigr).\quad(4.1)
\]

(b) Let \((u_b)\) be supported on primary squarefree \(b\) of length \(P\). Then
\[
\begin{aligned}
&\sum_{J\le N(a)<2J}\Bigl|\sum_bu_b\chi_b(a)\Bigr|^2\\
&\ll_\epsilon X^\epsilon\bigl(J+(JP)^{2/3}+J^{1/3}P\bigr)\\
&\qquad\cdot\sum_b|u_b|^2 ,
\end{aligned}
\]
where \(a\) runs over primary elements, or over all nonzero elements of \(\mathcal O\). If \(J\ge P\), the last term is at most \((JP)^{2/3}\).

**Proof.** Every primary \(n\) is uniquely \(n=st^2c^3\) with \(s,t\) coprime squarefree primary and \(c\) primary: take the exponents of the primes in \(n\) modulo \(3\).

(a) Split \(n=st^2c^3\) into dyads \(S,V,C\) with \(SV^2C^3\asymp Z\), at a cost of \(O(L^3)\). For squarefree \(a\),
\[
\chi_a(st^2c^3)=\chi_a(s)\,\overline{\chi_a(t)}\,\mathbf 1_{(a,c)=1}.
\]
The last two factors have absolute value at most one and do not depend on \(s\). By Cauchy's inequality over the \(O(VC)\) pairs \((t,c)\),
\[
\begin{aligned}
\Bigl|\sum_nv_n\chi_a(n)\Bigr|^2&\le O(VC)\\
&\quad\cdot\sum_{t,c}\Bigl|\sum_sv_{st^2c^3}\chi_a(s)\Bigr|^2 .
\end{aligned}
\]
Theorem 4.1, applied for each \((t,c)\) to the squarefree variable \(s\), gives the bound (4.1), since \(\sum_s|v_{st^2c^3}|^2\ll X^\epsilon S\) by Lemma 1.1. As \((VC)^2S\le SV^2C^3\ll Z\) and \(S\ll Z\), summing over the dyads gives the first bound.

(b) Write \(a=st^2c^3\) in the same way, with dyads satisfying \(SV^2C^3\asymp J\). For squarefree \(b\), \(\chi_b(a)=\chi_b(s)\overline{\chi_b(t)}\mathbf 1_{(b,c)=1}\). If \(S\ge V\), fix \(t,c\), put the factors \(\overline{\chi_b(t)}\mathbf 1_{(b,c)=1}\) into the coefficients, and apply Theorem 4.1 to the outer variable \(s\). This costs
\[
X^\epsilon\,VC\,\bigl(S+P+(SP)^{2/3}\bigr)\sum_b|u_b|^2 .
\]
If \(S<V\), fix \(s,c\) and apply the theorem to \(t\), after conjugating the coefficients. This costs \(X^\epsilon SC(V+P+(VP)^{2/3})\sum_b|u_b|^2\). Both are at most the asserted bound:
\[
\begin{gathered}
VCS\le J,\qquad VC\,P\le J^{1/3}P,\\
VC(SP)^{2/3}\le(JP)^{2/3}
\end{gathered}
\]
when \(S\ge V\), and \(SCV\le J\), \(SCP\le J^{1/3}P\), \(SC(VP)^{2/3}\le(JP)^{2/3}\) when \(S<V\). Each inequality follows from \(J\asymp SV^2C^3\), \(V,C\ge1\), and the order of \(S\) and \(V\). For the full lattice write \(a=\zeta\lambda^ia'\) with a unit \(\zeta\), \(i\ge0\) and \(a'\) primary. Then \(\chi_b(\zeta\lambda^i)\) is a coefficient twist, there are \(O(L)\) values of \(i\), and \(\chi_b(\lambda^3)=1\). Finally \(J^{1/3}P\le(JP)^{2/3}\) exactly when \(P\le J\). \(\square\)

## 5. Mean values and near-orthogonality

**Lemma 5.1 (mean values of Dirichlet polynomials).** For complex numbers \(w_1,\ldots,w_Z\) and an interval \(I\subset\mathbb R\),
\[
\begin{aligned}
&\int_I\Bigl|\sum_{m\le Z}w_m\,m^{it}\Bigr|^2dt\\
&\qquad\le\bigl(|I|+6\pi Z\bigr)\sum_{m\le Z}|w_m|^2 .
\end{aligned}
\]

**Proof.** This is Theorem 2.1 of the lesson on mean values, with \(t\) replaced by \(-t\); its error term is at most \(6\pi\sum m|w_m|^2\). \(\square\)

A sum over ideals \(\sum_nv_nN(n)^{it}\) is a Dirichlet polynomial in the integers \(m=N(n)\), with coefficients \(w_m=\sum_{N(n)=m}v_n\). For divisor-bounded \(v\), Lemma 1.1 gives \(\sum|w_m|^2\ll ZL^{O(1)}\) on a dyad of length \(Z\).

**Lemma 5.2 (the Bombieri–Halász–Montgomery inequality).** In an inner product space, for vectors \(\xi,\phi_1,\ldots,\phi_R\),
\[
\sum_{r=1}^R|\langle\xi,\phi_r\rangle|^2\le\|\xi\|^2\max_r\sum_{s=1}^R|\langle\phi_r,\phi_s\rangle| .
\]

**Proof.** Let \(c_r=\langle\xi,\phi_r\rangle\), \(\Sigma=\sum|c_r|^2\), and let \(M\) be the maximum on the right. Then \(\Sigma=\langle\xi,\sum_rc_r\phi_r\rangle\le\|\xi\|\,\|\sum_rc_r\phi_r\|\). Moreover
\[
\begin{aligned}
\Bigl\|\sum_rc_r\phi_r\Bigr\|^2&\le\sum_{r,s}|c_r||c_s||\langle\phi_r,\phi_s\rangle|\\
&\le M\Sigma ,
\end{aligned}
\]
using \(|c_rc_s|\le\frac12(|c_r|^2+|c_s|^2)\). Hence \(\Sigma^2\le\|\xi\|^2M\Sigma\). \(\square\)

## 6. Hecke characters of \(\mathbb Q(\omega)\)

A *Hecke character* of \(K\) is a unitary Größencharakter. By Theorem 6.3 of the lesson on Hecke characters, it corresponds to a unitary idèle class character, and it has a conductor \(\mathfrak f\) and an infinity type. We use only characters without an imaginary norm parameter. Their infinity type is \(z\mapsto(z/|z|)^\ell\) with an integer \(\ell\), the *angular order*. The characters of angular order zero are the characters of finite order, that is, the characters of ray class groups.

**Lemma 6.1 (angular characters).** For \(\ell\in\mathbb Z\) and an ideal \(\mathfrak a\) prime to \(3\) with primary generator \(a\), put \(\Theta_\ell(\mathfrak a)=(a/|a|)^\ell\). Then \(\Theta_\ell\) is a Hecke character of angular order \(\ell\), with conductor dividing \((3)\).

**Proof.** Products of primary elements are primary, so \(\Theta_\ell\) is multiplicative. If \(\alpha\) is any generator of \(\mathfrak a\) and \(u(\alpha)\) the unit with \(u(\alpha)\alpha\) primary, then \(\Theta_\ell((\alpha))=u(\alpha)^\ell(\alpha/|\alpha|)^\ell\). By Lemma 1.1 of the previous lesson, \(u(\alpha)\) depends only on \(\alpha\) modulo \(3\). For a unit \(\varepsilon\), the element \(u(\varepsilon)\varepsilon\) is a primary unit, hence equal to \(1\), so the finite part \(\alpha\mapsto u(\alpha)^\ell\) and the infinite part agree on units. This is the definition of a Größencharakter modulo \(3\). \(\square\)

For a Hecke character \(\Psi\) with conductor \(\mathfrak f\), put \(L(s,\Psi)=\sum\Psi(\mathfrak n)N(\mathfrak n)^{-s}\) over the nonzero ideals prime to \(\mathfrak f\).

**Proposition 6.2 (the functional equation).** Let \(\Psi\) be a primitive Hecke character of angular order \(\ell\), with \(D=N(\mathfrak f)\) and \(k=|\ell|/2\). Put
\[
\Lambda(s,\Psi)=\Bigl(\frac{\sqrt{3D}}{2\pi}\Bigr)^s\Gamma(s+k)\,L(s,\Psi).
\]
Then \(\Lambda(s,\Psi)\) continues meromorphically to \(\mathbb C\), is entire unless \(\Psi\) is principal, and
\[
\Lambda(s,\Psi)=\varepsilon_\Psi\,\Lambda(1-s,\overline\Psi),\qquad|\varepsilon_\Psi|=1 .
\]

**Proof.** Apply Theorem 10.1 of the lesson on Hecke \(L\)-functions. The field has discriminant \(-3\) and one complex place, so its analytic scale is \(3D\) and its gamma factor is \(\Gamma_{\mathbb C}(s+k)=2(2\pi)^{-s-k}\Gamma(s+k)\). The resulting completion is \(2(2\pi)^{-k}\Lambda(s,\Psi)\), and the same constant appears for \(\overline\Psi\), which has angular order \(-\ell\). The completion is entire unless \(\Psi=|\cdot|^{i\tau}\), and without an imaginary norm parameter this means that \(\Psi\) is principal. \(\square\)

The characters to which these facts are applied arise from cubic residue symbols with a fixed upper entry.

**Lemma 6.3 (characters attached to elements).** Let \(h\in\mathcal O\) be nonzero.

(a) There is a modulus \(\mathfrak m_h\), divisible only by \(\lambda\) and the primes dividing \(h\), such that \(\chi_n(h)\) depends only on \(n\) modulo \(\mathfrak m_h\), for primary \(n\) prime to \(h\). So \(\mathfrak n\mapsto\chi_n(h)\) is a character of finite order of the ray class group modulo \(\mathfrak m_h\). If \(h=\zeta\lambda^j\) with a unit \(\zeta\), then \(\mathfrak m_h\) can be taken to be one fixed power of \(\lambda\).

(b) If \(h\) is not a cube in \(\mathcal O\), this character is nontrivial. An element of \(\mathcal O\) that is a cube in \(K\) is a cube in \(\mathcal O\).

(c) If \(h\) is primary, then \(\chi_n(h)=\chi_h(n)\) for primary \(n\) prime to \(h\).

**Proof.** (a) Let \(\beta^3=h\) and \(L=K(\beta)\), an abelian extension of \(K\) of degree \(1\) or \(3\) that is unramified outside \(\lambda\) and the primes dividing \(h\). By Proposition 23.2 of the reciprocity lesson, for a primary prime \(\pi\nmid 3h\), the Frobenius of \(\pi\) in \(L/K\) maps \(\beta\) to \(\chi_\pi(h)\beta\). Let \(\mathfrak m_h\) be a multiple of the conductor of \(L/K\) supported on the primes of \(3h\) (Proposition 18.3 of the ray class lesson). By Theorem 18.2 there, the Frobenius depends only on the class of the ideal in the ray class group modulo \(\mathfrak m_h\). If \(n\equiv n'\pmod{\mathfrak m_h}\) with \(n,n'\) primary, then \((n)\) and \((n')\) lie in the same ray class. The claim follows by multiplicativity. For \(h=\zeta\lambda^j\) there are finitely many fields \(L\), all unramified outside \(\lambda\).

(b) If \(h\) is not a cube in \(K\), then \(L/K\) has degree \(3\), and Theorem 18.2 shows that the Frobenius map onto its Galois group is surjective. So some prime has \(\chi_\pi(h)\ne1\). If \(h=\gamma^3\) with \(\gamma\in K\), then \(\gamma\) is integral over \(\mathbb Z\), and \(\mathcal O\) is integrally closed.

(c) This is the reciprocity law, Lemma 2.1(c) of the previous lesson. \(\square\)

By Lemma 2.1(b) of the previous lesson, \(\chi_n(-1)=1\) and \(\chi_n(\omega)=\omega^{(N(n)-1)/3}\) explicitly. The values \(\chi_n(\lambda)\) depend on \(n\) modulo \(9\); see equation (1.5) of [DR]. Only the qualitative statement (a) is used in this course.

**Theorem 6.4 (uniform prime sums for Hecke characters, N3).** Fix \(A,M>0\) and an integer \(\ell\). Let \(\Psi\) be a primitive Hecke character of \(K\) of angular order \(\ell\) and conductor norm \(D\le(\log x)^A\). Suppose that either \(\ell\ne0\), or \(\ell=0\) and \(\Psi\) is a nonprincipal character with \(\Psi^3=1\). Then
\[
\sum_{N(\mathfrak p)\le x}\Psi(\mathfrak p)\log N(\mathfrak p)\ll_{\ell,A,M}\frac x{(\log x)^M},
\]
the sum running over the prime ideals of \(K\).

Theorem 6.4 is used without proof in the programme. For \(\ell=0\) it follows from Theorem 1.4 of [TZ], applied to the cyclic cubic extension of \(K\) attached to \(\Psi\) by class field theory. There the field degree is \(2\), the discriminant is \(3\), and the conductor bound is \(D\). Weighting the counts of the three Frobenius classes by \(\Psi\) cancels their main terms. The possible exceptional zero belongs to a real character of the group of order three, which is trivial, so its term cancels too, and the error term is \(O_M(x(\log x)^{-M})\) for \(D\le(\log x)^A\). For \(\ell\ne0\) the estimate follows from Theorem 1.2 of [KT], a prime number theorem for \(L\)-functions with a standard zero-free region. Viewed over \(\mathbb Q\), \(L(s,\Psi)\) has degree \(2\), conductor \(3D\) and Langlands parameters \(k,k+1\), by the duplication formula. The zero-free region is Lemma 2.1 of [CPS], and there is no exceptional zero, since \(\Psi\) is not real. Higher prime powers contribute \(O(\sqrt x\log^2x)\).

**Corollary 6.5.** In the situation of Theorem 6.4, for \(|t|\le(\log x)^A\), a smooth weight \(W\) supported in \([\frac12,2]\) with bounded derivatives, and \(y\in[x/2,x]\),
\[
\begin{aligned}
\sum_{N(\mathfrak p)\le y}\Psi(\mathfrak p)N(\mathfrak p)^{it}&\ll_{\ell,A,M}\frac x{(\log x)^M},\\
\sum_{\mathfrak p}\Psi(\mathfrak p)W\Bigl(\frac{N(\mathfrak p)}x\Bigr)&\ll_{\ell,A,M}\frac x{(\log x)^M}.
\end{aligned}
\]
The same bounds hold after deleting the primes dividing a given element of norm \(x^{O(1)}\).

**Proof.** Partial summation removes the weight \(\log N(\mathfrak p)\) and inserts \(N(\mathfrak p)^{it}\) or \(W\), at a cost of a factor \(O(1+|t|)\), which is absorbed by enlarging \(M\). An element of norm \(x^{O(1)}\) has \(O(\log x)\) prime factors. \(\square\)

## 7. Exercises

**7.1.** Let \(W(z)=e^{-\pi|z|^2}\). Show that \(\widehat W(y)=\frac2{\sqrt3}e^{-4\pi|y|^2}\).

**7.2.** Let \(\pi=1+3\omega\). Show that \(\chi_\pi(\lambda)=\omega^2\), so that the character \(n\mapsto\chi_n(\lambda)\) of Lemma 6.3 is nontrivial.

**7.3.** Show that the term \(Q^2\) in Lemma 3.3 cannot be replaced by \(Q^{2-\delta}\) for any fixed \(\delta>0\). Take \(v\) supported on \(n=1\), and count the primitive characters modulo primary primes of norm between \(Q/2\) and \(Q\).

**7.4.** Let \(A=B=N\). Compare the bound of Theorem 4.1 with the bound that Lemma 3.3 gives for the same sum, after the characters \(b\mapsto\chi_a(b)\) are written as characters of conductor \(a\). Which exponent of \(N\) does each give?

**7.5.** Let \(\Psi\) be a nonprincipal Hecke character of finite order with \(\Psi^3=1\). Deduce from Theorem 6.4 that
\[
\begin{aligned}
&\#\{\mathfrak p:N(\mathfrak p)\le x,\ \Psi(\mathfrak p)=1\}\\
&\qquad=\frac13\pi_K(x)+O\bigl(x(\log x)^{-M}\bigr),
\end{aligned}
\]
where \(\pi_K(x)\) counts prime ideals of norm at most \(x\).

## 8. Solutions

**7.1.** With \(z=s+it\) and \(y=u+iv\), \(\operatorname{Tr}(zy)=2(su-tv)\). The Euclidean Fourier transform of \(e^{-\pi(s^2+t^2)}\) at \((2u,-2v)\) is \(e^{-4\pi(u^2+v^2)}\), and the factor \(\frac2{\sqrt3}\) comes from \(\mathfrak m\).

**7.2.** From \(1+3\omega\equiv0\) we get \(\omega\equiv2\pmod\pi\), as in Exercise 6.2 of the previous lesson, so \(\lambda=1+2\omega\equiv5\pmod\pi\). Then \(\chi_\pi(\lambda)\equiv5^2\equiv4\pmod 7\), and \(4\equiv\omega^2\) since \(\omega\equiv2\).

**7.3.** With \(v_1=1\) and \(v_n=0\) otherwise, the right side is \(O(1+Q^2)\) and the left side is \(\sum_r|\Xi_r|\). Modulo a primary prime \(\pi\), every nontrivial character of the cyclic group \((\mathcal O/\pi\mathcal O)^\times\) is primitive, and there are \(N(\pi)-2\) of them. By Lemma 4.2 of the previous lesson there are \(\gg Q/\log Q\) primary primes with \(Q/2<N(\pi)\le Q\). Taking all their nontrivial characters gives a left side \(\gg Q^2/\log Q\), which is larger than \(Q^{2-\delta}\) for large \(Q\).

**7.4.** Theorem 4.1 gives \(N^{4/3+\epsilon}\sum|\beta_b|^2\), because \((AB)^{2/3}=N^{4/3}\) dominates. For squarefree \(a\), the character \(b\mapsto\chi_a(b)=\chi_b(a)\) is primitive modulo \(a\), so Lemma 3.3 with \(Q=Z=N\) gives \((N+N^2)\sum|\beta_b|^2\). The cubic large sieve saves \(N^{2/3}\) by exploiting that the family consists of cubic characters only.

**7.5.** For a prime \(\mathfrak p\) not dividing \(\mathfrak f\), \(\frac13(1+\Psi(\mathfrak p)+\overline{\Psi(\mathfrak p)})\) is \(1\) if \(\Psi(\mathfrak p)=1\) and \(0\) otherwise. Sum over \(N(\mathfrak p)\le x\), and use Theorem 6.4 by partial summation for \(\Psi\) and \(\overline\Psi\). The primes dividing \(\mathfrak f\) number \(O(\log x)\).

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 2.1 (conventions and classical inputs) and Section 2.2 (the two large sieves). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
- [DR] A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3 (2024), Theorem 9.1 (Heath-Brown's cubic large sieve) and equation (1.5) (the supplementary laws). https://arxiv.org/abs/2109.07463v3
- [TZ] J. Thorner and A. Zaman, *A unified and improved Chebotarev density theorem*, arXiv:1803.02823v3, published in Algebra Number Theory 13 (2019), Theorem 1.4. https://arxiv.org/abs/1803.02823v3
- [KT] I. Kaneko and J. Thorner, *Highly uniform prime number theorems*, arXiv:2203.09515v2, published in Ann. Inst. Fourier 75 (2025), Theorem 1.2. https://arxiv.org/abs/2203.09515v2
- [CPS] E. Chen, P. S. Park and A. A. Swaminathan, *Linnik's theorem for Sato–Tate laws on elliptic curves with complex multiplication*, arXiv:1506.09170v3, published in Res. Number Theory 1 (2015), Lemma 2.1. https://arxiv.org/abs/1506.09170v3

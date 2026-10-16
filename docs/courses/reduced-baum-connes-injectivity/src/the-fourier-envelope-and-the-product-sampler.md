# The Fourier envelope and the product sampler

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Each edge of the tower will carry a random Heisenberg voltage \(v\) and a bounded matrix weight \(W\), drawn so that the mean \(\mathbb E[W\lambda(v)]\) is a prescribed spread symbol \(T_ifT_k^*\) of [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md). Two features of the law matter later. Its horizontal coordinates \(n,l\) (the exponents of \(x\) and \(y\)) must be independent, with small atoms, so that a fixed short word in the voltages is rarely trivial. And the weights must be bounded independently of the height. Both come from one estimate: the coefficients of \(T_ifT_k^*\) in the normal form \(x^ny^lz^c\) are dominated by a product of a function of \(n\) and a constant in \(l\), whose total mass stays bounded although there are about \(J_i\) values of \(l\). The decisive input is the residual phase \(e(-nj\alpha)\), summed by parts with the golden separation [OpenAI-BCI, Sections 5.4-5.5, Lemmas 5.3-5.4].

- Coefficients in the normal form (Section 1).
- A rescaled Fourier estimate (Section 2).
- The Fourier envelope (Section 3).
- The product sampler (Section 4).

The notation of the previous lesson is in force: \(\alpha=(\sqrt5-1)/2\), \(N_i=2^{200H_i}\), \(Z_i=2^{500H_i}\), \(J_i=2^{50H_i}\), the profiles (3.2), the spreading operators \(T_i\) of (5.1) with coefficients \(a_{ij}\), and the torus coordinates of Lemma 1.1 there. We write \(e(t)=e^{2\pi it}\) and \(\hat g(w)=\int_{\mathbb R}g(t)e(-wt)\,dt\).

## 1. Coefficients in the normal form

Every element of \(\mathsf H\) is uniquely \(x^ny^lz^c\) (Lemma 1.1 of [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md)). For a finite or absolutely summable matrix series put
\[
\begin{gathered}
A=\sum_{n,l,c}A_{n,l,c}\,\lambda(x^ny^lz^c),\\
\|A\|_1=\sum_{n,l,c}\|A_{n,l,c}\| .
\end{gathered}
\]
The triangle inequality gives \(\|A\|\le\|A\|_1\) for the operator norm on \(\ell^2(\mathsf H)\otimes\mathbb C^\ell\).

**Lemma 1.1** (coefficients of a spread symbol). Let \(f\) be a matrix function on \(\mathbb T^2\) and write \(f(\vartheta,\xi)=\sum_nf_n(\vartheta)e(n\xi)\). Then
\[
\begin{gathered}
T_ifT_k^*=\sum_{n,l}g_{n,l}(\lambda(z))\\
\times\lambda(x)^n\lambda(y)^l,\\
g_{n,l}(\vartheta)=f_n(\vartheta)\,S_{n,l}(\vartheta),\\
S_{n,l}(\vartheta)=\sum_jb_{j,l}\,e(-nj\vartheta),\\
b_{j,l}=a_{ij}a_{k,j-l},
\end{gathered}\tag{1.1}
\]
and the coefficient \(A_{n,l,c}\) of \(\lambda(x^ny^lz^c)\) is the \(c\)-th Fourier coefficient of \(g_{n,l}\).

*Proof.* By Lemma 1.1(4) of the previous lesson, \(\lambda(y)^jf=f_{(j)}\lambda(y)^j\) with \(f_{(j)}(\vartheta,\xi)=f(\vartheta,\xi-j\vartheta)\), which is \(\sum_nf_n(\vartheta)e(-nj\vartheta)e(n\xi)\). So
\[
T_ifT_k^*=\sum_{j,j'}a_{ij}a_{kj'}f_{(j)}\lambda(y)^{j-j'} ,
\]
and collecting \(l=j-j'\) gives (1.1). Finally \(\lambda(z)^c\lambda(x)^n\lambda(y)^l=\lambda(x^ny^lz^c)\), since \(z\) is central. \(\square\)

## 2. A rescaled Fourier estimate

**Lemma 2.1.** Let \(g\in C_c^\infty(\mathbb R;M_\ell(\mathbb C))\) and \(Z\ge1\), and let \(c_k\) be the Fourier coefficients of the function \(\vartheta\mapsto g(Z(\vartheta-\alpha))\) on \(\mathbb R/\mathbb Z\), assumed supported in one period. Then \(c_k=Z^{-1}e(-k\alpha)\hat g(k/Z)\), and for every integer \(A\ge0\)
\[
\begin{aligned}
&\sum_k\Bigl(1+\frac{|k|}Z\Bigr)^A\|c_k\|\\
&\quad\le C_A\sum_{j=0}^{A+2}\|g^{(j)}\|_{L^1(\mathbb R)} .
\end{aligned}\tag{2.1}
\]

*Proof.* The substitution \(\vartheta=\alpha+t/Z\) gives the formula for \(c_k\). Integrating by parts \(m\) times, \(\|\hat g(w)\|\le(2\pi|w|)^{-m}\|g^{(m)}\|_{L^1}\); with \(m=0\) and \(m=A+2\), \(\|\hat g(w)\|\) is at most \(C(1+|w|)^{-A-2}\sum_{j\le A+2}\|g^{(j)}\|_{L^1}\). Then
\[
\begin{aligned}
&\sum_k\Bigl(1+\frac{|k|}Z\Bigr)^AZ^{-1}\Bigl(1+\frac{|k|}Z\Bigr)^{-A-2}\\
&\quad=\frac1Z\sum_k\Bigl(1+\frac{|k|}Z\Bigr)^{-2},
\end{aligned}
\]
which is bounded uniformly in \(Z\ge1\), by comparison with \(\int(1+|w|)^{-2}dw\). Operator norms are used throughout, so the matrix size plays no role. \(\square\)

## 3. The Fourier envelope

**Lemma 3.1** (Fourier envelope; [OpenAI-BCI, Lemma 5.3]). Let \(|i-k|\le1\), let \(f\) be in the profile family, written at reference height \(i\), and put \(N=N_i\), \(Z=Z_i\), \(J=J_i\). For all integers \(A\ge0\) and \(P\ge3\), the coefficients of \(T_ifT_k^*\) satisfy
\[
\begin{aligned}
&\sum_c\Bigl(1+\frac{|c|}Z\Bigr)^A\|A_{n,l,c}\|\\
&\quad\le C_{A,P}\,N^{-1}\\
&\qquad\times\Bigl(1+\frac{|n|}N\Bigr)^{-P}\\
&\qquad\times\bigl(1+J\|n\alpha\|\bigr)^{-3}
\end{aligned}\tag{3.1}
\]
for \(|l|\le C_bJ\), and \(A_{n,l,c}=0\) for larger \(|l|\). The constants are uniform in the height and the profile family. In particular \(\|T_ifT_k^*\|_1\) is bounded uniformly, and for every \(\eta>0\) there is \(L_\eta\), independent of the height, such that truncating to
\[
\begin{gathered}
|n|\le L_\eta N,\quad|l|\le C_bJ,\\
|c|\le L_\eta Z
\end{gathered}\tag{3.2}
\]
changes the series by at most \(\eta\) in \(\|\cdot\|_1\).

*Proof.* *The \(\xi\)-coefficients.* With \(t=Z(\vartheta-\alpha)\) and the substitution \(u=N\xi\),
\[
\begin{gathered}
f_n(\alpha+t/Z)=N^{-1}\Phi(t,n/N),\\
\Phi(t,w)=\int_{\mathbb R}F(t,u)e(-wu)\,du ,
\end{gathered}
\]
where \(f(\vartheta,\xi)=F(Z(\vartheta-\alpha),N\xi)\). The function \(\Phi\) is supported in a fixed compact \(t\)-interval and is rapidly decreasing in \(w\), uniformly with its \(t\)-derivatives over the profile family: integration by parts in \(u\) gives \(\|\partial_t^a\Phi(t,w)\|\le C_{a,m}(1+|w|)^{-m}\) for all \(a,m\).

*The weights \(b_{j,l}\).* By (5.1) of the previous lesson, \(b_{j,l}\) vanishes unless \(|j|<J_i\) and \(|j-l|<J_k\), so unless \(|l|<C_bJ\), since \(J_k/J_i=2^{\pm50b}\) or \(1\). It has \(O_b(J)\) nonzero values in \(j\), each \(O(J^{-1})\), and since \(a\) is smooth, repeated differences \(\Delta b_{j,l}=b_{j+1,l}-b_{j,l}\) in \(j\) satisfy
\[
\sum_j|\Delta^rb_{j,l}|\le C_rJ^{-r} .
\]
Also \(\sum_j|b_{j,l}|\le1\) by the Cauchy–Schwarz inequality and \(\sum_ja_{ij}^2=1\).

*The residual phase.* Write \(S_{n,l}(\alpha+t/Z)=\sum_j\beta_j(t)\,\omega^j\) with \(\omega=e(-n\alpha)\) and \(\beta_j(t)=b_{j,l}e(-njt/Z)\). It is essential to keep the factor \(e(-njt/Z)\) in the amplitude. Since \(|j|\le C_bJ\) and \(t\) is bounded, the discrete product rule gives, for all \(r,a\ge0\),
\[
\begin{aligned}
&\sum_j\bigl|\Delta^r\partial_t^a\beta_j(t)\bigr|\\
&\quad\le C_{r,a}J^{-r}\Bigl(1+\frac{|n|J}Z\Bigr)^{r+a} ;
\end{aligned}
\]
each difference or derivative of the phase costs a factor \(O(|n|/Z)\), respectively \(O(|n|J/Z)\). Summation by parts \(r\) times, \(\sum_j\beta_j\omega^j=(1-\omega)^{-r}\sum_j(\Delta^r\beta)_j\,\omega^{j+r}\) for finitely supported sequences, and \(|1-\omega|=2|\sin\pi n\alpha|\ge4\|n\alpha\|\), give, together with the trivial bound,
\[
\begin{aligned}
&\bigl|\partial_t^aS_{n,l}(\alpha+t/Z)\bigr|\\
&\quad\le C_{r,a}\Bigl(1+\frac{|n|J}Z\Bigr)^{r+a}\\
&\qquad\times\bigl(1+J\|n\alpha\|\bigr)^{-r} .
\end{aligned}\tag{3.3}
\]

*The central coefficients.* By Lemma 1.1, \(A_{n,l,c}\) is the \(c\)-th Fourier coefficient of \(g_{n,l}(\vartheta)=G(Z(\vartheta-\alpha))\) with
\[
G(t)=N^{-1}\Phi(t,n/N)\,S_{n,l}(\alpha+t/Z).
\]
Apply Lemma 2.1 to \(G\), and (3.3) with \(r=3\) and \(a\le A+2\). Since
\[
\begin{gathered}
\frac{NJ}Z=2^{-250H_i}\le1,\\
1+\frac{|n|J}Z\le1+\frac{|n|}N ,
\end{gathered}
\]
the polynomial factors from (3.3) are absorbed by taking the decay exponent of \(\Phi\) in \(w=n/N\) larger. This proves (3.1), for all \(n\).

*Summing over \(n\).* On an interval \(I\) of \(M\) consecutive integers, two points \(n\ne n'\) satisfy \(\|(n-n')\alpha\|\ge1/(3M)\) by Lemma 4.1 of the previous lesson, so at most \(1+6Mu\) of the points \(n\alpha\bmod1\) lie within distance \(u\) of any point. Writing \((1+Jv)^{-3}=\int_v^\infty3J(1+Ju)^{-4}du\) and exchanging sum and integral,
\[
\begin{gathered}
\sum_{n\in I}\bigl(1+J\|n\alpha\|\bigr)^{-3}\\
\le\int_0^\infty\frac{3J(1+6Mu)}{(1+Ju)^4}\,du\\
=1+\frac{3M}J .
\end{gathered}\tag{3.4}
\]
Split the integers into \(|n|\le N\) and the dyadic annuli \(2^{v-1}N<|n|\le2^vN\). Since \(N\ge J\), (3.4) gives
\[
\begin{aligned}
&\sum_nN^{-1}\Bigl(1+\frac{|n|}N\Bigr)^{-3}\\
&\qquad\times\bigl(1+J\|n\alpha\|\bigr)^{-3}\\
&\quad\le\frac CJ .
\end{aligned}\tag{3.5}
\]
Summing (3.1) with \(A=0\) over the \(O_b(J)\) values of \(l\) bounds \(\|T_ifT_k^*\|_1\). Using a larger \(P\), the part with \(|n|>LN\) is at most \(CL^{-(P-3)}\), and using a larger \(A\), the part with \(|c|>LZ\) is at most \(C(1+L)^{-A}\); this gives (3.2). \(\square\)

## 4. The product sampler

**Lemma 4.1** (finite product sampler; [OpenAI-BCI, Lemma 5.4]). For every \(\eta>0\), each symbol \(T_ifT_k^*\) of Lemma 3.1 has a finite probability distribution of pairs \((W,v)\), with \(W\in M_\ell(\mathbb C)\) and \(v=x^ny^lz^c\in\mathsf H\), such that
\[
\begin{gathered}
\|W\|\le M_\eta,\\
\bigl\|\mathbb E[W\lambda(v)]-T_ifT_k^*\bigr\|_1\le\eta .
\end{gathered}
\]
The coordinates \(n\) and \(l\) are independent, with atoms
\[
\begin{gathered}
\sup_n\mathbb P(n)=O_b(J_i/N_i),\\
\sup_l\mathbb P(l)=O_b(J_i^{-1}) .
\end{gathered}\tag{4.1}
\]
All possible coordinates of \(v\) and of \(v^{-1}\) are bounded by \(2^{a_0H_i}\) with a fixed exponent, for example \(a_0=502\), after the initial height is raised. The weights can be restricted to a finite set, containing \(0\) and closed under adjoints, at the cost of any further error in \(\|\cdot\|_1\). All constants and the finite set are independent of the height.

*Proof.* Truncate the series to the box (3.2) with error at most \(\eta/2\), and call the remaining coefficients \(A_{n,l,c}\). Put
\[
w_n=N^{-1}\Bigl(1+\frac{|n|}N\Bigr)^{-3}\bigl(1+J\|n\alpha\|\bigr)^{-3} .
\]
By Lemma 3.1, \(R_{n,l}:=\sum_c\|A_{n,l,c}\|\le C_1w_n\), and \(\sum_nw_n\le C_0/J\) by (3.5). Let \(\mu\) be the probability on the allowed \(n\)-interval with masses \(Jw_n/(2C_0)\), of total at most \(\frac12\), plus the remaining mass spread uniformly over \(\{-N,\ldots,N\}\); let \(\nu\) be uniform on the interval \(|l|\le C_bJ\). Then (4.1) holds, since \(w_n\le N^{-1}\), and \(\mu(n)\nu(l)\ge Jw_n/(2C_0)\cdot1/(3C_bJ)\), so
\[
R_{n,l}\le M_\eta\,\mu(n)\nu(l)
\]
with a constant \(M_\eta\) independent of the height.

Draw \(n\sim\mu\) and \(l\sim\nu\) independently. If \(R_{n,l}>0\), draw \(c\) with probability \(\|A_{n,l,c}\|/R_{n,l}\) among the nonzero coefficients and put
\[
W=\frac{R_{n,l}}{\mu(n)\nu(l)}\cdot\frac{A_{n,l,c}}{\|A_{n,l,c}\|} ;
\]
if \(R_{n,l}=0\), put \(W=0\) and \(c=0\). The horizontal law is the same whether the weight is zero or not. Then \(\|W\|\le M_\eta\) and
\[
\begin{aligned}
&\mathbb E[W\lambda(v)]\\
&\quad=\sum_{n,l}\mu(n)\nu(l)\sum_c\frac{\|A_{n,l,c}\|}{R_{n,l}}\,\frac{R_{n,l}}{\mu(n)\nu(l)}\\
&\qquad\times\frac{A_{n,l,c}}{\|A_{n,l,c}\|}\,\lambda(x^ny^lz^c),
\end{aligned}
\]
which is the truncated series. Choose a finite subset of the ball of radius \(M_\eta\) in \(M_\ell(\mathbb C)\), containing \(0\), closed under adjoints and \(\eta/2\)-dense, and round \(W\) to a nearest element, keeping \(0\) fixed; the expectation moves by at most \(\mathbb E\|W-W'\|\le\eta/2\) in \(\|\cdot\|_1\). The set depends on \(\eta\) and \(\ell\), not on the height. A reversed edge uses the adjoint weight and the inverse voltage, not a new draw.

For the coordinates, (1.2) of the lesson on the Heisenberg group gives
\[
\begin{gathered}
(n,l,c)(n',l',c')\\
=(n+n',l+l',c+c'-ln'),\\
(n,l,c)^{-1}=(-n,-l,-c-ln).
\end{gathered}
\]
In the box, \(|n|\le L_\eta2^{200H_i}\), \(|l|\le C_b2^{50H_i}\), \(|c|\le L_\eta2^{500H_i}\) and \(|ln|\le C2^{250H_i}\); after raising the initial height, all coordinates of \(v\) and \(v^{-1}\) are at most \(2^{502H_i}\). \(\square\)

The zero symbol is allowed: a type may have mean zero at any prescribed set of heights, through the weight \(0\) of the finite set, with no new labels; the voltage of the edge is still drawn from the same diffuse horizontal law.

## 5. Exercises

**Exercise 5.1.** Show that \(|1-e(t)|\ge4\|t\|\) for real \(t\), and prove the summation by parts formula used for (3.3) for \(r=1\).

**Exercise 5.2.** Explain why the trivial estimate \(\sum_j|b_{j,l}|\le1\) alone would only give \(\|T_ifT_k^*\|_1=O(J)\), and how the factor \((1+J\|n\alpha\|)^{-3}\) recovers a bounded one-norm.

**Exercise 5.3.** Compute \(\int_0^\infty3J(1+6Mu)(1+Ju)^{-4}du\).

**Exercise 5.4.** In Lemma 4.1, why must the horizontal law be used even when the drawn weight is zero?

## 6. Solutions

**5.1.** \(|1-e(t)|=2|\sin\pi t|\), and \(|\sin\pi t|\ge2\|t\|\) by concavity of \(\sin\) on \([0,\pi/2]\). For \(r=1\), \((1-\omega)\sum_j\beta_j\omega^j=\sum_j(\beta_j-\beta_{j-1})\omega^j\) for finitely supported \(\beta\), which is \(\sum_j(\Delta\beta)_{j-1}\omega^j\).

**5.2.** Summing \(N^{-1}(1+|n|/N)^{-3}\) over \(n\) gives \(O(1)\), and there are \(O(J)\) values of \(l\). The factor \((1+J\|n\alpha\|)^{-3}\) is small unless \(n\alpha\) is within about \(1/J\) of an integer, which by (3.4) happens for only about \(N/J\) of the \(N\) values \(|n|\le N\); this gains the factor \(1/J\).

**5.3.** \(\int_0^\infty3J(1+Ju)^{-4}du=1\) and \(\int_0^\infty3J\cdot6Mu(1+Ju)^{-4}du\) equals \(\frac{18M}J\int_0^\infty v(1+v)^{-4}dv=\frac{18M}J\cdot\frac16=\frac{3M}J\).

**5.4.** The voltage of an edge must have the diffuse horizontal law in every case, because the girth argument of the next lesson bounds the probability that a word in the voltages is trivial using only the atoms (4.1), whatever the weights are. Edges of weight zero still belong to the covering graph.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 5.4-5.5, Lemmas 5.3 and 5.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026

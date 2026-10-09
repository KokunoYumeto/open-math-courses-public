# The discrete convexity conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\mu_p\) be the product law on subsets of \([N]=\{1,\dots,N\}\) with density \(p\in(0,1)\). If a family \(\mathcal D\subseteq2^{[N]}\) is likely, how much of \(2^{[N]}\) do unions of a few members of \(\mathcal D\) cover? For an integer \(k\ge1\) let
\[
E_k(\mathcal D)=\bigl\{S\subseteq[N]:S\not\subseteq D_1\cup\dots\cup D_k\text{ for all }D_1,\dots,D_k\in\mathcal D\bigr\},
\]
the sets *not* covered by \(k\) members of \(\mathcal D\); the members may repeat. Talagrand conjectured that for a suitable universal \(k\), the exceptional family \(E_k(\mathcal D)\) is \(p\)-small whenever \(\mu_p(\mathcal D)\) is close enough to \(1\), in analogy with a question about sums of a convex body with itself in Gaussian space [Tal]. Recall from Section 1 of [Integral and fractional expectation thresholds](integral-and-fractional-expectation-thresholds.md) that a family is \(p\)-small if it has a cover \(\mathcal G\) of cost \(c_p(\mathcal G)=\sum_{S\in\mathcal G}p^{|S|}\le\frac12\). This lesson proves the conjecture, following OpenAI [OpenAI-DC]:

**Theorem 7.1** (OpenAI 2026; Talagrand's discrete convexity conjecture). Let \(k=2^{75}\). For every \(N\ge1\), every \(p\in(0,1)\) and every family \(\mathcal D\subseteq2^{[N]}\) with \(\mu_p(\mathcal D)\ge1-\frac1k\), the family \(E_k(\mathcal D)\) is \(p\)-small.

No monotonicity of \(\mathcal D\) is assumed. Section 4 proves a companion result with two unions at the cost of a constant factor in the density (Corollary 4.2), from a fractional cover found by Li [Li] and Theorem 4.1 of [Integral and fractional expectation thresholds](integral-and-fractional-expectation-thresholds.md). Corollary 7.2 recovers the theorem of Park and Pham on positive selector processes [PP-S].

The method has three steps. A biased Fourier expansion of \(\mathbf 1_{\mathcal F}\) produces nonnegative weights \(w(U)\) on subsets \(U\) with \(\sum_Uq^{|U|}w(U)\le1\) (Section 2). A signed measure on arrays of \(\ell\) rows shows that every set \(S\) not covered by \(\ell\) members of \(\mathcal F\) carries a large sum of powers \(w(U)^{\ell/2}\) over its nonempty subsets (Section 3); for \(\ell=2\) this is Li's signed kernel, and the signed-operator technique goes back to work of Friedgut and of Ellis, Filmus and Friedgut. A covering lemma (Section 5) turns these two bounds into a cover when \(\ell=32\), at density \(q/2^{70}\) (Section 6), and a coupling of \(2^{70}\) rows returns to the original density (Section 7).

## 1. Unions of likely sets

The family \(E_k(\mathcal D)\) is increasing, and \(E_{k+1}(\mathcal D)\subseteq E_k(\mathcal D)\), because a union of \(k\) members is also a union of \(k+1\) members (repeat one). If \(\mathcal D\neq\varnothing\), then \(\varnothing\notin E_k(\mathcal D)\). Grouping a tuple of \(kL\) members into \(k\) groups of \(L\) shows:

**Lemma 1.1.** For \(L\ge1\) let \(\mathcal D^{(L)}=\{D_1\cup\dots\cup D_L:D_1,\dots,D_L\in\mathcal D\}\). Then \(E_k(\mathcal D^{(L)})=E_{kL}(\mathcal D)\). \(\square\)

## 2. Biased Fourier weights

Fix \(q\in(0,1)\), a family \(\mathcal F\subseteq2^{[N]}\) and \(f=\mathbf 1_{\mathcal F}\), viewed as a function on \(\{0,1\}^N\) by identifying sets with indicator vectors. For \(U\subseteq[N]\) let
\[
b(U)=(1-q)^{|U|}\sum_{z\in\{0,1\}^U}(-1)^{\sum_{i\in U}z_i}\ \mathbb E\bigl[f(z,Y)\bigr],\qquad w(U)=b(U)^2,\tag{2.1}
\]
where \(Y\) has independent Bernoulli(\(q\)) coordinates on \([N]\setminus U\) and \((z,Y)\) is the vector with coordinates \(z\) on \(U\) and \(Y\) off \(U\). In particular \(b(\varnothing)=\mu_q(\mathcal F)\).

**Lemma 2.1** (global weight bound). \(\sum_{U\subseteq[N]}q^{|U|}w(U)\le\mu_q(\mathcal F)\).

**Proof.** Under \(\mu_q\), the functions \(\chi_U(x)=\prod_{i\in U}(q-x_i)/\sqrt{q(1-q)}\) are orthonormal: each factor has mean \(0\) and variance \(1\), and the coordinates are independent. There are \(2^N\) of them, so they form an orthonormal basis of the functions on \(\{0,1\}^N\), and Parseval's identity gives \(\sum_U\widehat f(U)^2=\mathbb E f^2=\mu_q(\mathcal F)\), where \(\widehat f(U)=\mathbb E[f\chi_U]\). For a Bernoulli(\(q\)) bit, \(\mathbb P(X_i=z_i)(q-z_i)=q(1-q)(-1)^{z_i}\). Summing over the values \(z\) of the coordinates in \(U\),
\[
\widehat f(U)=\bigl(q(1-q)\bigr)^{|U|/2}\sum_{z\in\{0,1\}^U}(-1)^{\sum_iz_i}\,\mathbb E[f(z,Y)]=\Bigl(\frac q{1-q}\Bigr)^{|U|/2}b(U).
\]
Hence \(q^{|U|}w(U)=(1-q)^{|U|}\widehat f(U)^2\le\widehat f(U)^2\), and the claim follows. \(\square\)

The same basis, with the opposite sign convention, appears in Section 1 of [Biased Fourier analysis and hypercontractivity](course:sharp-thresholds-for-graph-properties/biased-fourier-analysis-and-hypercontractivity).

## 3. Signed arrays

**Lemma 3.1** (signed identity). Let \(\ell\ge1\) and \(S\in E_\ell(\mathcal F)\). Then
\[
\sum_{U\subseteq S}(-1)^{|U|}\,b(U)^\ell=0.\tag{3.1}
\]
Consequently, if \(\ell\) is even, \(\sum_{\varnothing\neq U\subseteq S}w(U)^{\ell/2}\ge\mu_q(\mathcal F)^\ell\).

**Proof.** Consider arrays \(x\in\{0,1\}^{\ell\times N}\) with rows \(x_1,\dots,x_\ell\in\{0,1\}^N\) and columns \(y\in\{0,1\}^\ell\). Let \(P(y)=\prod_{j=1}^\ell q^{y_j}(1-q)^{1-y_j}\), and
\[
R(y)=P(y)-(1-q)^\ell(-1)^{y_1+\dots+y_\ell},
\]
so that \(R(0,\dots,0)=0\). Give each column \(i\notin S\) the weight \(P\) and each column \(i\in S\) the signed weight \(R\), and let \(\nu_S(x)\) be the product of the column weights. If \(\nu_S(x)\neq0\), every column in \(S\) contains a \(1\), so the rows, read as sets, have a union containing \(S\); as \(S\in E_\ell(\mathcal F)\), they are not all in \(\mathcal F\), and \(\prod_jf(x_j)=0\). Hence
\[
\sum_x\nu_S(x)\prod_{j=1}^\ell f(x_j)=0.
\]
Expand each column factor \(R=P-(1-q)^\ell(-1)^{\sum_jy_j}\), and let \(U\subseteq S\) be the set of columns where the second term is chosen. The term indexed by \(U\) is \((-1)^{|U|}\) times
\[
\sum_x\ \prod_{i\notin U}P(x_{\cdot i})\prod_{i\in U}(1-q)^\ell(-1)^{\sum_jx_{ji}}\ \prod_{j=1}^\ell f(x_j)=\prod_{j=1}^\ell\Bigl[\sum_{x_j\in\{0,1\}^N}\ \prod_{i\notin U}q^{x_{ji}}(1-q)^{1-x_{ji}}\ (1-q)^{|U|}(-1)^{\sum_{i\in U}x_{ji}}f(x_j)\Bigr],
\]
because both products factor over the rows. Each bracket equals \(b(U)\): split \(x_j\) into its coordinates \(z\) on \(U\) and the rest, whose weights form the law of \(Y\). This proves (3.1). For even \(\ell\), \(b(U)^\ell=w(U)^{\ell/2}\ge0\), and (3.1) gives \(\mu_q(\mathcal F)^\ell=b(\varnothing)^\ell=-\sum_{\varnothing\neq U\subseteq S}(-1)^{|U|}b(U)^\ell\le\sum_{\varnothing\neq U\subseteq S}w(U)^{\ell/2}\). \(\square\)

## 4. Two unions

**Proposition 4.1** (Li). If \(\mu_q(\mathcal F)\ge\frac12\), then \(E_2(\mathcal F)\) has a fractional cover of cost at most \(\frac12\) at density \(q/2\).

**Proof.** Let \(\mu=\mu_q(\mathcal F)\), and put \(g(\varnothing)=0\) and \(g(U)=\min\{1,w(U)/\mu^2\}\) for \(U\neq\varnothing\). Let \(S\in E_2(\mathcal F)\). If \(w(U)\ge\mu^2\) for some nonempty \(U\subseteq S\), then \(g(U)=1\); otherwise \(\sum_{\varnothing\neq U\subseteq S}g(U)=\mu^{-2}\sum_{\varnothing\neq U\subseteq S}w(U)\ge1\) by Lemma 3.1 with \(\ell=2\). So \(g\) is a fractional cover of \(E_2(\mathcal F)\). Since \(w(\varnothing)=\mu^2\), Lemma 2.1 gives \(\sum_{U\neq\varnothing}q^{|U|}w(U)\le\mu-\mu^2\), and
\[
\sum_{U\neq\varnothing}g(U)\Bigl(\frac q2\Bigr)^{|U|}\le\frac1{2\mu^2}\sum_{U\neq\varnothing}q^{|U|}w(U)\le\frac{1-\mu}{2\mu}\le\frac12.\qquad\square
\]

**Corollary 4.2** (two unions; OpenAI). Let \(C=25\cdot512^4\). For every \(N\ge1\), \(p\in(0,1)\) and \(\mathcal D\subseteq2^{[N]}\) with \(\mu_p(\mathcal D)\ge\frac12\), the family \(E_2(\mathcal D)\) is \(p/(2C)\)-small.

**Proof.** If \(E_2(\mathcal D)=\varnothing\), the empty cover works. Otherwise \(E_2(\mathcal D)\) is a nontrivial increasing family (Section 1; \(\mathcal D\neq\varnothing\) since \(\mu_p(\mathcal D)>0\)). Proposition 4.1 with \(q=p\) gives a fractional cover of cost at most \(\frac12\) at density \(p/2\), and Theorem 4.1 of [Integral and fractional expectation thresholds](integral-and-fractional-expectation-thresholds.md) turns it into a cover of cost at most \(\frac12\) at density \(p/(2C)\). \(\square\)

Park had obtained the same conclusion at density \(p/(K\max\{1,\log\log(1/p)\})\) [Park]. Theorem 7.1 keeps the density \(p\) and uses \(2^{75}\) unions instead.

## 5. A covering lemma

For a family \(\mathcal G\) and \(0<\rho<1\) write \(c_\rho(\mathcal G)=\sum_{I\in\mathcal G}\rho^{|I|}\). Let \(\binom Xr\) denote the family of \(r\)-element subsets of \(X\).

**Lemma 5.1** (covering lemma; OpenAI). Let \(X\) be finite, \(0<\rho<1\), and let \(r,h\) be integers with \(1\le r\le h\) and \(h\ge64\). If \(\mathcal H\subseteq\binom Xr\) satisfies \(|\mathcal H|\rho^r\le2^{h+1}\), then the family of sets \(S\subseteq X\) containing at least \(2^{12h}\) members of \(\mathcal H\) has a cover \(\mathcal G\) with \(c_\rho(\mathcal G)\le3\cdot2^{-h}\).

**Proof.** Let \(m=2^{12h}\), \(T=2^{4h}\) and \(\pi=2^{-8h}\). For \(|I|\le r\) define the weighted degree \(d(I)=|\{e\in\mathcal H\colon I\subseteq e\}|\,\rho^{r-|I|}\).

*Large weighted degrees.* Let \(\mathcal C_0=\{I:|I|\le r,\ d(I)>T\}\). Counting pairs \(I\subseteq e\) gives \(\sum_{|I|\le r}d(I)\rho^{|I|}=2^r|\mathcal H|\rho^r\), so
\[
c_\rho(\mathcal C_0)\le T^{-1}2^r|\mathcal H|\rho^r\le2^{r+1-3h}\le2^{1-2h}.
\]
In particular \(\varnothing\notin\mathcal C_0\), since \(d(\varnothing)=|\mathcal H|\rho^r\le2^{h+1}<T\). Call \(e\in\mathcal H\) *regular* if it contains no member of \(\mathcal C_0\), and let \(\mathcal H'\) be the set of regular edges; thus \(d(I)\le T\) whenever \(I\subseteq e\in\mathcal H'\). For \(B\subseteq X\), grouping the regular edges \(e\) by \(I=e\cap B\) gives
\[
\sum_{e\in\mathcal H'}\rho^{|e\setminus B|}\le\sum_{I\in\mathcal I_B}|\{e\in\mathcal H\colon I\subseteq e\}|\,\rho^{r-|I|}\le T\sum_{i=0}^r\binom{|B|}i,\tag{5.1}
\]
where \(\mathcal I_B\) is the family of sets \(I\subseteq B\) with \(|I|\le r\) that lie in some regular edge; the last step uses \(d(I)\le T\) for these \(I\).

*Sampled pairs.* Independently for each ordered pair \((e,e')\in(\mathcal H')^2\), diagonal pairs included, sample the pair with probability \(\pi\), and let \(\mathcal C_1\) be the set of unions \(e\cup e'\) of sampled pairs. By (5.1) with \(B=e\), \(\sum_{e'}\rho^{|e'\setminus e|}\le2^rT\), so
\[
\mathbb E\,c_\rho(\mathcal C_1)\le\pi\sum_{e,e'\in\mathcal H'}\rho^{|e|}\rho^{|e'\setminus e|}\le\pi|\mathcal H|\rho^r2^rT\le2^{r+1-3h}\le2^{1-2h}.
\]

*Residual unions.* For every ordered \(m\)-tuple \((e_1,\dots,e_m)\) of distinct regular edges such that none of the \(m^2\) pairs \((e_i,e_j)\) was sampled, put \(e_1\cup\dots\cup e_m\) into \(\mathcal C_2\). Let \(\mathcal G=\mathcal C_0\cup\mathcal C_1\cup\mathcal C_2\). For every outcome of the sampling, \(\mathcal G\) covers the target family: if \(S\) contains at least \(m\) members of \(\mathcal H\) and no member of \(\mathcal C_0\), then those members are regular; take \(m\) of them. If one of their pairs was sampled, its union lies in \(\mathcal C_1\) and in \(S\); otherwise their union lies in \(\mathcal C_2\) and in \(S\).

For \(0\le t\le m\) let \(W_t\) be the sum of \(\rho^{|e_1\cup\dots\cup e_t|}\) over ordered \(t\)-tuples of distinct regular edges. A prefix with union \(B\) has \(|B|\le rm\), and by (5.1) its extensions contribute at most \(\rho^{|B|}T\sum_{i\le r}\binom{|B|}i\le\rho^{|B|}T(1+rm)^r\), using \(\sum_{i\le r}\binom bi\le(1+b)^r\) (Exercise 8.4). Hence \(W_m\le[T(1+rm)^r]^m\). The \(m^2\) pairs of a tuple of distinct edges are distinct sampling indices, so the tuple contributes with probability \((1-\pi)^{m^2}\le\mathrm e^{-\pi m^2}\le2^{-\pi m^2}\), and
\[
\mathbb E\,c_\rho(\mathcal C_2)\le[T(1+rm)^r]^m\,2^{-\pi m^2}=2^{m(4h+r\log_2(1+rm))-\pi m^2}.
\]
Here \(\pi m=2^{4h}\), and \(1+rm\le(h+1)2^{12h}\le2^{13h}\), so \(4h+r\log_2(1+rm)+1\le4h+13h^2+1\le18h^2\le2^{4h}=\pi m\) for \(h\ge64\). Thus \(\mathbb E\,c_\rho(\mathcal C_2)\le2^{-m}\), and
\[
\mathbb E\,c_\rho(\mathcal G)\le2^{1-2h}+2^{1-2h}+2^{-m}\le3\cdot2^{-h}.
\]
There are finitely many outcomes, each giving a cover, so some outcome gives a cover of cost at most \(3\cdot2^{-h}\). \(\square\)

## 6. Thirty-two unions at a fraction of the density

**Proposition 6.1** (OpenAI). Let \(L=2^{70}\). For every \(N\ge1\), \(q\in(0,1)\) and \(\mathcal F\subseteq2^{[N]}\) with \(\mu_q(\mathcal F)\ge\frac12\), the family \(E_{32}(\mathcal F)\) is \((q/L)\)-small.

**Proof.** Let \(w\) be the weights of Section 2 and \(\rho=q/L\).

*Large weights.* Let \(\mathcal G_0=\{U\neq\varnothing:w(U)\ge2^{-64|U|}\}\). For \(U\in\mathcal G_0\) with \(|U|=r\), \(\rho^r=q^r2^{-70r}\le2^{-6r}q^rw(U)\le2^{-6}q^rw(U)\), so Lemma 2.1 gives \(c_\rho(\mathcal G_0)\le2^{-6}\).

*Bins.* For \(r\ge1\) and integers \(h\), let \(\mathcal H_{r,h}\) be the set of \(U\notin\mathcal G_0\) with \(|U|=r\) and \(2^{-(h+1)}<w(U)\le2^{-h}\). Every nonempty \(U\notin\mathcal G_0\) with \(w(U)>0\) lies in exactly one bin, and an occupied bin has \(h\ge64r\), because its weights are below \(2^{-64r}\). By Lemma 2.1, \(|\mathcal H_{r,h}|q^r2^{-(h+1)}<\sum_{U\in\mathcal H_{r,h}}q^rw(U)\le1\), so \(|\mathcal H_{r,h}|\rho^r\le2^{h+1}\). Lemma 5.1 applies (\(r\le64r\le h\), \(h\ge64\)) and gives a cover \(\mathcal G_{r,h}\) of the sets containing at least \(2^{12h}\) members of \(\mathcal H_{r,h}\), with \(c_\rho(\mathcal G_{r,h})\le3\cdot2^{-h}\). There are finitely many occupied bins. Let \(\mathcal G=\mathcal G_0\cup\bigcup\mathcal G_{r,h}\). Then
\[
c_\rho(\mathcal G)\le\frac1{64}+3\sum_{r\ge1}\sum_{h\ge64r}2^{-h}=\frac1{64}+\frac6{2^{64}-1}<\frac12.
\]

*Coverage.* Let \(S\) contain no member of \(\mathcal G\). Then \(S\) contains no member of \(\mathcal G_0\) and fewer than \(2^{12h}\) members of each bin \(\mathcal H_{r,h}\), so
\[
\sum_{\varnothing\neq U\subseteq S}w(U)^{16}\le\sum_{r\ge1}\sum_{h\ge64r}2^{12h}2^{-16h}=\frac{16}{15}\cdot\frac1{2^{256}-1}<2^{-32}\le\mu_q(\mathcal F)^{32}.
\]
By Lemma 3.1 with \(\ell=32\), \(S\notin E_{32}(\mathcal F)\). So \(\mathcal G\) covers \(E_{32}(\mathcal F)\). \(\square\)

## 7. Back to the original density

**Proof of Theorem 7.1.** Let \(L=2^{70}\), so \(k=32L\), and let \(\mu_p(\mathcal D)\ge1-\frac1k\). We construct random sets \(R_1,\dots,R_L\subseteq[N]\), each of law \(\mu_p\) but not independent. Whatever their joint law, the union bound gives
\[
\mathbb P(R_j\in\mathcal D\text{ for all }j)\ge1-\frac Lk=\frac{31}{32}.\tag{7.1}
\]

*Case \(Lp<1\).* Independently for each \(i\in[N]\), choose a label \(J_i\in\{0,1,\dots,L\}\) with \(\mathbb P(J_i=0)=1-Lp\) and \(\mathbb P(J_i=j)=p\) for \(1\le j\le L\), and put \(R_j=\{i:J_i=j\}\). Each \(R_j\) has law \(\mu_p\), and \(R_1\cup\dots\cup R_L=\{i:J_i\neq0\}\) has law \(\mu_q\) with \(q=Lp\in(0,1)\). By (7.1), \(\mu_q(\mathcal D^{(L)})\ge\frac{31}{32}\), with \(\mathcal D^{(L)}\) as in Lemma 1.1. Proposition 6.1 shows that \(E_{32}(\mathcal D^{(L)})\) is \((q/L)\)-small, and \(E_{32}(\mathcal D^{(L)})=E_k(\mathcal D)\) by Lemma 1.1; since \(q/L=p\), this is the claim.

*Case \(Lp\ge1\).* Let \(t=(p-\frac1L)/(1-\frac1L)\in[0,1)\). Independently for each \(i\in[N]\), choose a row uniformly at random among the \(L\) rows and put \(i\) into it, and put \(i\) into each other row independently with probability \(t\). Each \(R_j\) then contains each \(i\) independently with probability \(\frac1L+(1-\frac1L)t=p\), so it has law \(\mu_p\), and \(R_1\cup\dots\cup R_L=[N]\) always. By (7.1) some outcome has all rows in \(\mathcal D\); repeating these \(L\) members \(32\) times gives \(k\) members of \(\mathcal D\) with union \([N]\). So \(E_k(\mathcal D)=\varnothing\), which is covered at cost \(0\). \(\square\)

**Corollary 7.2** (positive selector processes; Park and Pham). Let \(k=2^{75}\), \(p\in(0,1)\), let \(T\subseteq[0,\infty)^N\) be nonempty, \(\varphi(S)=\sup_{t\in T}\sum_{i\in S}t_i\) for \(S\subseteq[N]\), and suppose \(0<M=\mathbb E_{\mu_p}\varphi<\infty\). Then \(\{S:\varphi(S)\ge k^2M\}\) is \(p\)-small.

**Proof.** Every set has positive \(\mu_p\)-probability, so \(\varphi\) is finite. Let \(\mathcal D=\{D:\varphi(D)<kM\}\); by Markov's inequality \(\mu_p(\mathcal D)\ge1-\frac1k\). Since the \(t_i\) are nonnegative, \(\varphi(A)\le\varphi(A')\) for \(A\subseteq A'\) and \(\varphi(A\cup A')\le\varphi(A)+\varphi(A')\). So a set contained in a union of \(k\) members of \(\mathcal D\) has \(\varphi<k^2M\), and \(\{\varphi\ge k^2M\}\subseteq E_k(\mathcal D)\), which is \(p\)-small by Theorem 7.1. \(\square\)

Markov's inequality alone gives \(\mu_p(\varphi\ge k^2M)\le k^{-2}\); the corollary gives a cover, an explicit reason for the large values.

## 8. Exercises

**Exercise 8.1** (easy). Show that \(E_k(\mathcal D)=\varnothing\) if and only if \([N]\) is the union of \(k\) members of \(\mathcal D\).

**Exercise 8.2** (medium). For one row, show directly that \(\sum_{U\subseteq S}(-1)^{|U|}b(U)=\mathbb P\bigl(S\cup Y\in\mathcal F\bigr)\) for every \(S\subseteq[N]\), where \(Y\) has law \(\mu_q\) on \([N]\setminus S\), and deduce (3.1) for \(\ell=1\).

**Exercise 8.3** (easy). In the case \(Lp<1\) of the proof of Theorem 7.1, compute \(\mathbb P(i\in R_j\text{ and }i\in R_{j'})\) for \(j\neq j'\). Are the rows independent?

**Exercise 8.4** (easy). Show that \(\sum_{i=0}^r\binom bi\le(1+b)^r\) for integers \(b\ge0\) and \(r\ge0\).

## 9. Solutions

**8.1.** If \([N]=D_1\cup\dots\cup D_k\), every set is contained in this union. Conversely, if \(E_k(\mathcal D)=\varnothing\), then \([N]\notin E_k(\mathcal D)\), so \([N]\) is contained in, hence equal to, some union of \(k\) members.

**8.2.** With one row, \(R(0)=0\) and \(R(1)=q+(1-q)=1\), so \(\nu_S\) puts the coordinates in \(S\) equal to \(1\) and gives the others the Bernoulli(\(q\)) law; hence \(\sum_x\nu_S(x)f(x)=\mathbb P(S\cup Y\in\mathcal F)\). The expansion in the proof of Lemma 3.1, valid for every \(S\), shows that the same sum equals \(\sum_{U\subseteq S}(-1)^{|U|}b(U)\). If \(S\in E_1(\mathcal F)\), no member of \(\mathcal F\) contains \(S\), and the probability is \(0\).

**8.3.** The labels are exclusive, so the probability is \(0\), while \(\mathbb P(i\in R_j)\mathbb P(i\in R_{j'})=p^2>0\). The rows are not independent; only the law of each row matters in (7.1).

**8.4.** List each subset of size at most \(r\) of an ordered \(b\)-element set as its increasing sequence of elements, padded to length \(r\) with a new symbol. Different subsets give different sequences of length \(r\) over an alphabet of \(b+1\) symbols.

## References

- [OpenAI-DC] OpenAI, *Talagrand's discrete convexity conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026
- [Tal] M. Talagrand, *Are many small sets explicitly small?*, Proceedings of STOC 2010, 13–36. https://michel.talagrand.net/preprints/small.pdf
- [Li] C. Li, *On p-spread measures*, 2026. https://arxiv.org/abs/2609.08967
- [Park] J. Park, *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*, 2026. https://arxiv.org/abs/2609.14681
- [PP-S] J. Park and H. T. Pham, *On a conjecture of Talagrand on selector processes and a consequence on positive empirical processes*, Annals of Mathematics 199 (2024), 1293–1321. https://arxiv.org/abs/2204.10309

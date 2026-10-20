# Primes with controlled predecessors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Proposition 5.1 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md) with the weights \(w(d)\) of [*Weights, mass and distribution in a progression*](weights-mass-and-distribution-in-a-progression.md). A lower block sieve shows that the integers \(d\) with \(P^-(d)>x^b\) carry weight about \(\mathfrak S_Me^{-\gamma_E}X_0/(bL)\). The composite ones among them are removed in two steps. Those whose least prime factor lies below \(x^{1/2-\kappa}\) are grouped by the size of that factor; in each group the marked Type II estimate replaces the roughness condition on the cofactor by its density, and Buchstab's identity shows that all groups together carry at most the weight of the rough numbers minus the weight that Buchstab's identity assigns to the primes. Composites \(d=pq\) with both factors near \(\sqrt x\) are bounded by an upper sieve for pairs, at a cost proportional to \(\kappa\). Choosing \(\kappa\), \(b\) and the number \(K\) of prime groups in this order leaves a positive proportion of the weight on primes.

**Prerequisites.** [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), (4.1) and Proposition 5.1; [*A block sieve and rough-number densities*](a-block-sieve-and-rough-number-densities.md), (1.1)–(1.3), Lemma 1.1, Lemma 2.1 and Lemma 3.1; [*Marked Type II estimates and rough factors*](marked-type-ii-estimates.md), Section 1; [*Weights, mass and distribution in a progression*](weights-mass-and-distribution-in-a-progression.md), Sections 1–5; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 3.1 and 4.2.

Keep the data \(M,c,u,\Psi\) of Lesson 18, the weights \(w\) of (1.2) there, the total weight \(X_0\), the harmonic mass \(J_0\), the parameters \(\kappa,\epsilon,b,D\) of (4.1) there, and the densities \(g_r\) and remainders \(E_r\) of (4.2) there. As in Lesson 18, \(\ell\) runs over odd squarefree integers.

## 1. The initial lower bound

Put \(z=x^b\) and
\[
S_b=\sum_{P^-(d)>x^b}w(d).
\]

**Proposition 1.1** (the initial lower bound [OpenAI-029, (12.12)]). There are absolute constants \(b_1,C_s>0\) such that for \(0<b<b_1\)
\[
\begin{aligned}
\frac L{\mathfrak S_MX_0}\,S_b&\ge\frac{e^{-\gamma_E}}b\bigl(1-C_se^{-1/(20b)}\bigr)\\
&\quad+o(1).\quad(1.1)
\end{aligned}
\]

*Proof.* Fix \(r\le x^\epsilon\) and regard the primes \(Q\) counted in \(A_r\), with the weights \(\Psi((crQ+1)/x)\), as the objects of Lemma 2.1 of Lesson 16. The sieving primes are the odd \(p\le z\), and the bad condition at \(p\) is \(p\mid crQ+1\). For \(\ell\) composed of these primes the weight of the objects satisfying the bad conditions at all \(p\mid\ell\) is \(A_r(\ell)=g_r(\ell)A_r+E_r(\ell)\), by (4.2) of Lesson 18. Since \(g_r(p)\le1/(p-1)\le\frac12\) and \(\sum_{v<p\le v^2}1/(p-1)\) is bounded by Mertens' estimate, (2.1) of Lesson 16 holds with \(\eta_0=\frac12\) and an absolute \(C_0\). Take \(H=2\lfloor1/(40b)\rfloor\); for small \(b\) it exceeds the threshold of Lemma 2.1 of Lesson 16, and
\[
\begin{gathered}
z^{4H+2}\le x^{0.2+2b}<D,\\
e^{-H}\le e^2e^{-1/(20b)} .\quad(1.2)
\end{gathered}
\]
Every supported \(d=crQ+1\) is odd, so the objects with no bad condition are those with \(P^-(crQ+1)>z\). By (2.2) of Lesson 16 and (5.2) of Lesson 18, their weight is at least
\[
\begin{aligned}
&(1+o(1))\,A_r\,V_M(z)\bigl(1-Ce^2e^{-1/(20b)}\bigr)\\
&\qquad-C\sum_{\ell\le D}|E_r(\ell)| ,\quad(1.3)
\end{aligned}
\]
with an \(o(1)\) uniform in \(r\). Multiply by \(\mathcal W(r)\) and sum over \(r\le x^\epsilon\). By Lemma 3.1 and (4.4) of Lesson 18,
\[
\begin{aligned}
&\sum_{r\le x^\epsilon}\mathcal W(r)A_r\\
&\quad =X_0+O_K\bigl(x\exp(-\epsilon L^{1-a_K})\bigr)\\
&\quad =(1+o(1))X_0 ,\quad(1.4)
\end{aligned}
\]
and by (4.3) there with \(A=3\) the remainders contribute \(O(xJ_0L^{-3})=o(X_0/L)\). Finally \(V_M(z)=(1+o(1))\mathfrak S_Me^{-\gamma_E}/(bL)\) by Lemma 5.1 of Lesson 18, since \(\log z=bL\). The terms with \(r>x^\epsilon\) contribute nonnegatively to \(S_b\), and (1.1) follows with \(C_s=Ce^2\). \(\square\)

## 2. Mass conditioned on a prime divisor

**Lemma 2.1** (mass conditioned on a prime divisor [OpenAI-029, Lemma 12.4]). For fixed \(b\le\gamma<\gamma'\le\frac12-\kappa\),
\[
\begin{aligned}
&\sum_{\substack{x^\gamma<n\le x^{\gamma'}\\ n\ \text{prime}}}\ \sum_{\substack{n\mid d\\ P^-(d)>W}}w(d)\\
&\quad=\mathfrak S_M\,X_0\,V(W)\\
&\qquad\times\Bigl(\log\frac{\gamma'}\gamma+o(1)\Bigr).\quad(2.1)
\end{aligned}
\]

*Proof.* For large \(x\) the primes \(n\) in (2.1) exceed \(W\) and every group prime, so \(n\nmid Mr\) for every group integer \(r\), and \(g_r(n)=1/(n-1)\). Fix \(r\le x^\epsilon\) and such an \(n\), and apply Lemma 2.1 of Lesson 16 to the \(Q\) counted in \(A_r\) with \(n\mid crQ+1\), the odd primes \(p\le W\), and the bad conditions \(p\mid crQ+1\). For \(\ell\) composed of odd primes \(p\le W\), the product \(n\ell\) is odd and squarefree, and multiplicativity of \(g_r\) gives
\[
\begin{aligned}
A_r(n\ell)&=\frac{A_r}{n-1}\,g_r(\ell)+E_r(n\ell),\quad(2.2)
\end{aligned}
\]
also for \(\ell=1\). Take \(X'=A_r/(n-1)\), \(E(\ell)=E_r(n\ell)\) and \(H=2\lceil(\log L)^2\rceil\). The relative error \(e^{-H}\) tends to \(0\), and the remainder moduli satisfy
\[
\begin{gathered}
\begin{aligned}
\ell&\le W^{4H+2}\\
&=\exp\bigl(O(L^{0.24}(\log L)^2)\bigr)\\
&=x^{o(1)},
\end{aligned}\\
n\ell\le x^{1/2-\kappa+o(1)}<D .
\end{gathered}
\]
The map \((n,\ell)\mapsto n\ell\) is injective, because \(n\) is the only prime factor of \(n\ell\) above \(W\). After summing over \(n\) and over \(r\le x^\epsilon\) with the weights \(\mathcal W(r)\), all remainders together are therefore bounded by the left side of (4.3) of Lesson 18, which is \(O(xJ_0L^{-3})\); this is \(o(X_0V(W))\), because \(X_0V(W)\asymp xJ_0L^{-1.24}\) by (4.4) of Lesson 18 and (1.2) of Lesson 16.

For the main terms, the sieve product \(\prod_{2<p\le W}(1-g_r(p))\) is \((1+o(1))\mathfrak S_MV(W)\) uniformly in \(r\), by Lemma 5.1 of Lesson 18. Mertens' estimate (Theorem 3.1 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)) gives \(\sum_{x^\gamma<n\le x^{\gamma'}}1/(n-1)=\log(\gamma'/\gamma)+o(1)\), and (1.4) evaluates the sum over \(r\le x^\epsilon\). This gives the contribution of \(r\le x^\epsilon\). A supported \(d\) has at most \(\log(2x)/(bL)\le2/b\) distinct prime factors above \(x^b\), so the part of the left side of (2.1) with \(r>x^\epsilon\) is at most \((2/b)\sum_{r>x^\epsilon}\mathcal W(r)A_r\)\(=O_K(x\exp(-\epsilon L^{1-a_K}))\), which is \(o(X_0V(W))\) by Lemma 3.1 of Lesson 18. \(\square\)

## 3. Removing composites by their least prime factor

For \(b\le\gamma<\gamma'\le\frac12-\kappa\) put
\[
\begin{gathered}
U_\kappa=\sum_{P^-(d)>x^{1/2-\kappa}}w(d),\\
\begin{aligned}
T_{\gamma,\gamma'}&=\sum_{\substack{x^\gamma<n\le x^{\gamma'}\\ n\ \text{prime}}}\ \sum_{P^-(m)>x^\gamma}w(mn).
\end{aligned}\quad(3.1)
\end{gathered}
\]
If \(x^\gamma<P^-(d)\le x^{\gamma'}\), then \(n=P^-(d)\) and \(m=d/n\) satisfy \(P^-(m)\ge n>x^\gamma\), so \(w(d)\) is one of the terms of \(T_{\gamma,\gamma'}\); this holds also when \(n^2\mid d\).

**Lemma 3.1** (the cost of one bin [OpenAI-029, (12.14)]). If \(K\) is at least a bound that depends on \(b,\gamma,\kappa\) but not on the \(a_i\), then
\[
\begin{aligned}
\frac L{\mathfrak S_MX_0}\,T_{\gamma,\gamma'}&\le\sup_{\gamma\le t\le\gamma'}D_\gamma(1-t)\,\log\frac{\gamma'}\gamma\\
&\quad+o(1).\quad(3.2)
\end{aligned}
\]

*Proof.* Split \(n\) and \(m\) into dyads \([N,2N)\) and \([H_m,2H_m)\), with \(N\) and \(H_m\) powers of \(2\), and keep the pairs of dyads that contain some \(n\in(x^\gamma,x^{\gamma'}]\) and \(m\) with \(x<mn<2x\). For such a pair, \(\log m/L=1-t+O(L^{-1})\) with \(t=\log n/L\in(\gamma,\gamma']\), and \(b\le\gamma\), \(\gamma'\le\frac12-\kappa\); so for large \(x\)
\[
\begin{gathered}
\begin{aligned}
&\Bigl[\frac{\log H_m}L,\frac{\log(2H_m)}L\Bigr]\\
&\quad \subseteq[s_-,s_+],
\end{aligned}\\
s_-=\frac12+\frac\kappa2,\\
s_+=1-\frac b2 ,
\end{gathered}
\]
and \(\gamma<s_-\). Both scales are at least \(x^{b/2}\), their product is \(\asymp x\), and there are \(O(L)\) pairs, since the \(m\) with \(x<mn<2x\) for \(n\in[N,2N)\) lie in \((x/(2N),2x/N)\), which meets at most three dyads. In each pair apply Lemma 2.1 of Lesson 18 with \(\delta=b/2\), \(I=[H_m,2H_m)\), and \(b_n\) the indicator of the primes of the \(n\)-dyad in \((x^\gamma,x^{\gamma'}]\), which is supported on \(W\)-rough integers. On the support \(m\ge x^{1/2}>x^\gamma\), and the total error is \(O(xL^{-5})=o(X_0/L)\) by (4.4) of Lesson 18 and \(J_0\ge1\). Hence
\[
\begin{aligned}
T_{\gamma,\gamma'}&=\sum_{\substack{x^\gamma<n\le x^{\gamma'}\\ n\ \text{prime}}}\ \sum_m\frac{D_\gamma(\log m/L)}{L\,V(W)}\\
&\quad \,\mathbf 1_{P^-(m)>W}\,w(mn)\\
&\quad +o\Bigl(\frac{X_0}L\Bigr).
\end{aligned}
\]
By Lemma 1.1 of Lesson 16, \(D_\gamma\) is uniformly continuous on \([s_-,s_+]\), so on the support of the summand \(D_\gamma(\log m/L)\)\(\le\sup_{\gamma\le t\le\gamma'}D_\gamma(1-t)+o(1)\). Since \(n>W\), the condition \(P^-(m)>W\) is \(P^-(mn)>W\), and Lemma 2.1 gives (3.2). \(\square\)

**Proposition 3.2** (after the least-factor subtraction [OpenAI-029, (12.15)]). Let \(0<b<\min(b_0,b_1)\), where \(b_0\) and \(C_d\) are the constants of (3.2) of Lesson 16. There is a partition \(b=\gamma_0<\gamma_1<\cdots<\gamma_J=\frac12-\kappa\) such that, if \(K\) is at least a bound depending on \(b\), \(\kappa\) and the partition but not on the \(a_i\),
\[
\begin{aligned}
&\frac L{\mathfrak S_MX_0}\,U_\kappa\\
&\quad\ge0.9-\frac{e^{-\gamma_E}}b\,(C_s+C_d)\,e^{-1/(20b)}\\
&\qquad+o(1).\quad(3.3)
\end{aligned}
\]

*Proof.* The points \((\gamma,1-t)\) with \(b\le\gamma\le t\le\frac12-\kappa\) form a compact set on which \(1-t-\gamma\ge2\kappa\), so by Lemma 1.1 of Lesson 16 the function \((\gamma,t)\mapsto D_\gamma(1-t)\) is uniformly continuous there. Choose \(\eta>0\) with \(\eta\log(1/(2b))\le0.1\), then \(\delta>0\) such that \(|D_\gamma(1-t)-D_{\gamma''}(1-t'')|\le\eta\) whenever \(|\gamma-\gamma''|\le\delta\) and \(|t-t''|\le\delta\), and a partition of mesh at most \(\delta\). For \(\gamma_{j-1}\le t'\le\gamma_j\) and every \(t\in[\gamma_{j-1},\gamma_j]\), \(D_{\gamma_{j-1}}(1-t')\le D_t(1-t)+\eta\). Integrating against \(dt/t\) over each bin and using Buchstab's identity (3.1) of Lesson 16 and \(D\ge0\),
\[
\begin{aligned}
&\sum_{j=1}^J\sup_{\gamma_{j-1}\le t'\le\gamma_j}D_{\gamma_{j-1}}(1-t')\\
&\qquad \log\frac{\gamma_j}{\gamma_{j-1}}\\
&\quad \le\int_b^{1/2-\kappa}\bigl(D_t(1-t)+\eta\bigr)\frac{dt}t\\
&\quad \le D_b(1)-1+0.1 .\quad(3.4)
\end{aligned}
\]
Every \(d\) with \(x^b<P^-(d)\le x^{1/2-\kappa}\) lies in exactly one bin, so \(S_b-U_\kappa\le\sum_jT_{\gamma_{j-1},\gamma_j}\). By (1.1), (3.2) and (3.4),
\[
\begin{aligned}
\frac L{\mathfrak S_MX_0}\,U_\kappa&\ge\frac{e^{-\gamma_E}}b\bigl(1-C_se^{-1/(20b)}\bigr)\\
&\quad -D_b(1)+0.9\\
&\quad +o(1),
\end{aligned}
\]
and the bound \(D_b(1)\le\frac{e^{-\gamma_E}}b(1+C_de^{-1/(20b)})\) of (3.2) of Lesson 16 gives (3.3). \(\square\)

The term \(1\) in Buchstab's identity, which is the contribution of the primes to \(D_b(1)\), is what survives the subtraction.

## 4. An upper bound for rough pairs

**Lemma 4.1** (rough pairs [OpenAI-029, Lemma 12.5]). Let \(\mathcal B=[M_1,2M_1)\times[M_2,2M_2)\) with
\[
\begin{gathered}
\frac x4\le M_1M_2\le2x,\\
\begin{aligned}
\frac{x^{0.46}}2&\le M_i\\
&\le2x^{0.54}\quad(i=1,2).
\end{aligned}\quad(4.1)
\end{gathered}
\]
Then
\[
\begin{aligned}
&\sum_{\substack{(m,n)\in\mathcal B\\ P^-(m)>W,\ P^-(n)>W}}w(mn)\\
&\quad \le C_1X_0V(W)^2 ,\quad(4.2)
\end{aligned}
\]
where \(C_1\) depends only on \(M\) and \(\Psi\); in particular it does not depend on \(K,\kappa,b,\epsilon\).

*Proof.* *Reduction to a sieve problem.* Fix a group integer \(r\le x^{0.11}\) and put \(k=cr\) and \(z'=x^{0.002}\). If \(w(mn)\ne0\) and \(mn-1\) has group part \(r\), then \(mn-1=kQ\) with a prime \(Q>x^{0.9}\), so \(mn\equiv1\pmod k\). Let \(j\le z'\) be an odd prime with \(j\nmid r\). Then \(j\nmid k\) and \(j\ne Q\), so \(mn\not\equiv1\pmod j\); and if \(j\le W\), then \(mn\not\equiv0\pmod j\), because \(m\) and \(n\) are \(W\)-rough. The **bad condition** at \(j\) is: \(mn\equiv1\pmod j\), or \(j\le W\) and \(mn\equiv0\pmod j\). Using \(\Psi\le1\), \(F\le1\) and Lemma 1.1 of Lesson 18, the left side of (4.2) is at most \(\sum_r\mathcal W(r)S_r\), where \(S_r\) is the number of pairs in \(\mathcal B\) with \(mn\equiv1\pmod k\) and no bad condition at any odd prime \(j\le z'\) with \(j\nmid r\).

*Local counts.* Modulo a prime \(j\) there are \(j-1\) residue pairs with product \(1\) and \(2j-1\) with product \(0\). For squarefree \(\ell\) composed of these primes \(j\) put
\[
\rho(\ell)=\prod_{j\mid\ell}\bigl(j-1+(2j-1)\mathbf 1_{j\le W}\bigr).
\]
By the Chinese remainder theorem exactly \(\varphi(k)\rho(\ell)\) residue pairs modulo \(k\ell\) satisfy \(mn\equiv1\pmod k\) and the bad conditions at all \(j\mid\ell\). Each residue pair has \((M_1/(k\ell)+O(1))(M_2/(k\ell)+O(1))\) representatives in \(\mathcal B\), so the number of pairs in \(\mathcal B\) with these conditions is \(X'g(\ell)+E(\ell)\), where
\[
\begin{gathered}
X'=M_1M_2\frac{\varphi(k)}{k^2},\qquad g(\ell)=\frac{\rho(\ell)}{\ell^2},\\
\begin{aligned}
|E(\ell)|&\le C\varphi(k)\rho(\ell)\\
&\quad\times\Bigl(\frac{M_1+M_2}{k\ell}+1\Bigr).\quad(4.3)
\end{aligned}
\end{gathered}
\]
For \(j\le W\), \(g(j)=(3j-2)/j^2\le7/9\), and for \(j>W\), \(g(j)=(j-1)/j^2\le1/j\); in both cases \(g(j)\le3/j\). So (2.1) of Lesson 16 holds with \(\eta_0=2/9\) and an absolute \(C_0\), and its upper bound (2.3), with \((z')^{10}=x^{0.02}\), gives
\[
\begin{aligned}
S_r&\le C\,X'\prod_{\substack{2<j\le z'\\ j\nmid r}}(1-g(j))\\
&\quad +\sum_{\ell\le x^{0.02}}|E(\ell)| .\quad(4.4)
\end{aligned}
\]

*The remainders.* For squarefree \(\ell\), \(\rho(\ell)\le\prod_{j\mid\ell}3j\le\tau(\ell)^2\ell\), where \(\tau\) is the divisor function. With \(\varphi(k)\le k\le4r\), (4.3) gives \(|E(\ell)|\le C\tau(\ell)^2(M_1+M_2+4r\ell)\). Let \(\tau_4(n)\) be the number of ordered factorizations \(n=a_1a_2a_3a_4\) into positive integers. At a prime power \(p^e\), \((e+1)^2\le\frac{(e+1)(e+2)(e+3)}6\), so \(\tau(n)^2\le\tau_4(n)\), and for \(Y\ge2\)
\[
\begin{aligned}
\sum_{n\le Y}\tau(n)^2&\le\sum_{a_1a_2a_3\le Y}\frac Y{a_1a_2a_3}\\
&\le Y(1+\log Y)^3 .
\end{aligned}
\]
With \(Y=x^{0.02}\), \(M_1+M_2\le4x^{0.54}\) and \(r\le x^{0.11}\),
\[
\begin{aligned}
&\sum_{\ell\le x^{0.02}}|E(\ell)|\\
&\quad \le C\bigl(x^{0.56}+rx^{0.04}\bigr)L^3\\
&\quad \le C\,\frac xr\bigl(x^{-0.33}+x^{-0.74}\bigr)L^3 .\quad(4.5)
\end{aligned}
\]

*The main term.* For \(j\le W\) and for \(W<j\le z'\) respectively,
\[
\begin{aligned}
1-\frac{3j-2}{j^2}&=\bigl(1-\tfrac1j\bigr)^3\bigl(1-\tfrac1{(j-1)^2}\bigr),\\
1-\frac{j-1}{j^2}&=\bigl(1-\tfrac1j\bigr)\bigl(1+\tfrac1{j(j-1)}\bigr).
\end{aligned}
\]
The factors \(1-(j-1)^{-2}\) are at most \(1\), and the product of the factors \(1+1/(j(j-1))\) is at most \(\exp(\sum_{j\ge2}\frac1{j(j-1)})=e\). Every group prime is below \(W\), and restoring the primes \(j\mid r\) changes \(\prod_{2<j\le W}(1-1/j)^3\) by a factor \(1+o(1)\), by (5.2) of Lesson 18. Since \(\prod_{2<j\le y}(1-1/j)=2V(y)\),
\[
\begin{aligned}
&\prod_{\substack{2<j\le z'\\ j\nmid r}}(1-g(j))\\
&\quad \le(8e+o(1))\,V(W)^3\,\frac{V(z')}{V(W)}\\
&\quad =(8e+o(1))\,V(W)^2\,V(z') .\quad(4.6)
\end{aligned}
\]

*Summation.* Here \(X'\le M_1M_2/k\le2x/(cr)\le x/r\), and \(V(W)^2V(z')\asymp L^{-1.48}\) by (1.2) of Lesson 16, so (4.4)–(4.6) give \(S_r\le C(x/r)V(W)^2V(z')\) with an absolute \(C\), uniformly for \(r\le x^{0.11}\). Multiplying by \(\mathcal W(r)\) and summing, the left side of (4.2) is at most \(CxJ_0V(W)^2V(z')\). Finally \(V(z')\le C/L\), and \(xJ_0/L\le CX_0\) by (4.4) of Lesson 18 with a constant depending only on \(M\) and \(\Psi\). Only \(J_0\), and not the pointwise bound \(B_K\), entered this calculation. \(\square\)

## 5. Composites with two nearly equal prime factors

**Proposition 5.1** (balanced composites [OpenAI-029, (12.17)]). If \(K\) is at least a bound depending on \(b\) but not on the \(a_i\), then
\[
\begin{aligned}
&\sum_{\substack{P^-(d)>x^{1/2-\kappa}\\ d\ \text{composite}}}w(d)\\
&\quad\le C_2\bigl(\kappa+L^{-1}\bigr)\frac{X_0}L\\
&\qquad+o\Bigl(\frac{X_0}L\Bigr),\quad(5.1)
\end{aligned}
\]
where \(C_2\) depends only on \(M\) and \(\Psi\).

*Proof.* *Boxes.* Let \(d<2x\) be composite with \(P^-(d)>x^{1/2-\kappa}\). Three prime factors would give \(d>x^{3/2-3\kappa}>2x\), so \(d=pq\) with primes \(x^{1/2-\kappa}<p\le q<2x^{1/2+\kappa}\). Cover the ordered pairs of such primes with product in \((x,2x)\) by the dyadic boxes \(\mathcal B=[M_1,2M_1)\times[M_2,2M_2)\), with \(M_i\) powers of \(2\), that meet \([x^{1/2-\kappa},2x^{1/2+\kappa}]\) in each coordinate and contain a pair with product in \((x,2x)\). Since \(\kappa<0.01\), every such box satisfies (4.1) and lies in \([x^{0.46},x^{0.54}]^2\) for large \(x\). The first coordinate takes at most \(2\kappa L/\log2+3\) values, and the product condition leaves at most three second coordinates for each, so there are at most \(C_{\rm dyad}(\kappa L+1)\) boxes with an absolute \(C_{\rm dyad}\).

*Replacing the primes.* In a box take \(\gamma=0.4\), \(s_-=0.46\), \(s_+=0.54\) and \(\delta=b/2\) in Lemma 2.1 of Lesson 18. A composite \(m\le x^{0.54}\) has \(P^-(m)\le x^{0.27}\), so on \([x^{0.46},x^{0.54}]\) the function \(R_{0.4}\) is the indicator \(\mathbf 1_p\) of the primes; and \(D_{0.4}(s)=1/s\) for \(s<0.8\), so
\[
\begin{aligned}
B_{0.4}(m)&=\frac{\mathbf 1_{P^-(m)>W}}{V(W)\log m}\\
&=:B(m).\quad(5.2)
\end{aligned}
\]
Write
\[
\begin{aligned}
&\mathbf 1_p(m)\mathbf 1_p(n)-B(m)B(n)\\
&\quad =\bigl(\mathbf 1_p(m)-B(m)\bigr)\mathbf 1_p(n)\\
&\qquad +B(m)\bigl(\mathbf 1_p(n)-B(n)\bigr).\quad(5.3)
\end{aligned}
\]
Apply Lemma 2.1 of Lesson 18 to the first term with the companion \(\mathbf 1_p(n)\) on \([M_2,2M_2)\), and to the second with the roles of \(m\) and \(n\) exchanged and the companion \(B(m)\) on \([M_1,2M_1)\); the weight \(w(mn)\) depends only on the product, and \(0\le B(m)\le1\) for large \(x\), since \(V(W)^{-1}\asymp L^{0.24}\) and \(\log m\ge0.46L\). Both companions are supported on \(W\)-rough integers. Over all boxes the errors total \(O((\kappa L+1)xL^{-6})=o(X_0/L)\).

*The main term.* On a box, \(B(m)B(n)\le(0.46L)^{-2}V(W)^{-2}\)\(\mathbf 1_{P^-(m)>W}\mathbf 1_{P^-(n)>W}\), so Lemma 4.1 bounds its contribution by \((0.46)^{-2}C_1X_0/L^2\). The ordered prime pairs in the boxes count every composite \(d\) of (5.1) at least once, and summing over the boxes gives (5.1) with \(C_2=(0.46)^{-2}C_1C_{\rm dyad}\). \(\square\)

## 6. The choice of parameters

**Theorem 6.1** (Proposition 5.1 of Lesson 1 [OpenAI-029, Proposition 2.1]). Let \(M\) be a positive multiple of \(8\), \(c\in\{2,4\}\), and let \(u\) satisfy (4.1) of Lesson 1. For all sufficiently large \(x\) there are \(\gg_{M,c,u}x/L^2\) primes \(p\in(x,2x)\) with
\[
\begin{gathered}
p\equiv u\pmod M,\\
p-1=crQ,\\
Q>x^{0.9}\ \text{prime},\quad(6.1)
\end{gathered}
\]
where every prime divisor of the integer \(r\) lies in \(\bigl(\exp(L^{0.1}),\exp(L^{0.3})\bigr)\).

*Proof.* Fix \(M,c,u\) and a smooth \(\Psi\) as in Lesson 18; they determine \(\mathfrak S_M\) and \(C_2\). Choose the parameters in this order:

1. \(0<\kappa<0.01\) with \(C_2\kappa<\mathfrak S_M/4\), and \(0<\epsilon<\kappa\);
2. \(0<b<0.01\), below the thresholds \(b_0\) of (3.2) of Lesson 16 and \(b_1\) of Proposition 1.1, with \(\frac{e^{-\gamma_E}}b(C_s+C_d)e^{-1/(20b)}<0.2\); this is possible because the left side tends to \(0\) as \(b\to0\);
3. the partition of Proposition 3.2;
4. \(K\) at least the bounds of Lemma 3.1 for the finitely many bins and of Proposition 5.1; these bounds do not depend on the \(a_i\);
5. \(a_i=0.1+0.1i/(K+1)\) for \(1\le i\le K\).

A prime \(d\in(x,2x)\) has \(P^-(d)=d>x^{1/2-\kappa}\), so it is counted by \(U_\kappa\), and the other terms of \(U_\kappa\) are composite. By (3.3) and (5.1), for large \(x\),
\[
\begin{aligned}
&\frac L{\mathfrak S_MX_0}\sum_{d\ \text{prime}}w(d)\\
&\quad \ge0.9-0.2-\frac{C_2\kappa}{\mathfrak S_M}+o(1)\\
&\quad \ge0.9-0.2-\frac14+o(1)>\frac14 .
\end{aligned}
\]
By (4.4) of Lesson 18, \(X_0\gg xJ_0/L\ge x/L\), and \(w\le B_K\) by (1.3) there. So the number of primes \(d\) with \(w(d)>0\) is at least \(\mathfrak S_MX_0/(4B_KL)\gg x/L^2\), with a constant depending on \(M,c,u\) through the choices above. For each of them, (1.2) and Lemma 1.1 of Lesson 18 give \(x<d<2x\), \(d\equiv u\pmod M\) and \(d-1=crQ\) with \(Q>x^{0.9}\) prime and \(r\) a group integer, and a group prime \(p\) satisfies \(\exp(L^{0.1})<\exp(L^{a_1})\le p\)\(\le\exp(2L^{a_K})<\exp(L^{0.3})\) for large \(x\). \(\square\)

Together with Proposition 5.2 of Lesson 1, which Lesson 15 derives from the zero-free strip of Lessons 2–14, Theorem 6.1 proves Theorem 2.1 of Lesson 1: every admissible integer is a primitive root modulo \(\gg x/(\log x)^2\) primes in \((x,2x)\).

## 7. Exercises

**7.1.** Verify the two factorizations of \(1-g(j)\) in the proof of Lemma 4.1.

**7.2.** For a prime \(j\), count the residue pairs \((a,b)\) modulo \(j\) with \(ab\equiv1\) and with \(ab\equiv0\), and show that \((3j-2)/j^2\le7/9\) for every prime \(j\ge3\).

**7.3.** Prove \(\tau(n)^2\le\tau_4(n)\) and \(\sum_{n\le Y}\tau_4(n)\le Y(1+\log Y)^3\) for \(Y\ge2\).

**7.4.** Let \(0<\kappa<1/6\). Show that for large \(x\) an integer \(d<2x\) with \(P^-(d)>x^{1/2-\kappa}\) has at most two prime factors counted with multiplicity.

**7.5.** Show that for every \(C>0\) there is \(b_*>0\) with \(\frac{e^{-\gamma_E}}b\,C\,e^{-1/(20b)}<0.2\) for \(0<b<b_*\).

**7.6.** For \((M,c,u)=(8,4,5)\), show that every prime \(p\) of Theorem 6.1 satisfies \(p\equiv5\pmod8\) and that \((p-1)/4=rQ\) is odd.

## 8. Solutions

**7.1.** \((1-\frac1j)^3(1-\frac1{(j-1)^2})\)\(=\frac{(j-1)^3}{j^3}\cdot\frac{j(j-2)}{(j-1)^2}=\frac{(j-1)(j-2)}{j^2}\)\(=1-\frac{3j-2}{j^2}\), and \((1-\frac1j)(1+\frac1{j(j-1)})\)\(=\frac{j-1}j\cdot\frac{j^2-j+1}{j(j-1)}=\frac{j^2-j+1}{j^2}=1-\frac{j-1}{j^2}\).

**7.2.** \(ab\equiv1\) forces \(a\) to be a unit and \(b=a^{-1}\): \(j-1\) pairs. \(ab\equiv0\) means \(a\equiv0\) or \(b\equiv0\): \(j+j-1=2j-1\) pairs. The function \(3/t-2/t^2\) has derivative \((4-3t)/t^3<0\) for \(t\ge2\), so its value at a prime \(j\ge3\) is at most its value \(7/9\) at \(3\).

**7.3.** Both functions are multiplicative, with \(\tau(p^e)^2=(e+1)^2\) and \(\tau_4(p^e)=\binom{e+3}3\); the inequality \(6(e+1)\le(e+2)(e+3)\) is \(0\le e^2-e\). Next, \(\sum_{n\le Y}\tau_4(n)\) counts the quadruples with \(a_1a_2a_3a_4\le Y\), which is \(\sum_{a_1a_2a_3\le Y}\lfloor Y/(a_1a_2a_3)\rfloor\)\(\le Y(\sum_{a\le Y}1/a)^3\le Y(1+\log Y)^3\).

**7.4.** Three prime factors larger than \(x^{1/2-\kappa}\) have product larger than \(x^{3/2-3\kappa}=x\cdot x^{1/2-3\kappa}\), which exceeds \(2x\) for large \(x\) because \(1/2-3\kappa>0\).

**7.5.** With \(s=1/b\), the left side is \(e^{-\gamma_E}Cse^{-s/20}\), which tends to \(0\) as \(s\to\infty\).

**7.6.** \(p\equiv u=5\pmod8\). The prime factors of \(r\) are group primes, hence odd, and \(Q>x^{0.9}\) is an odd prime, so \(rQ=(p-1)/4\) is odd.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 12.3–12.6. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026

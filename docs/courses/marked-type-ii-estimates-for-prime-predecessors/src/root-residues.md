# Root residues

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The moment of [*From the moment to the pairing*](from-the-moment-to-the-pairing.md) is a sum over closed paths that start at a position \(P\), the *root*. Divisibility of the first coordinates along the path by group primes depends only on \(P\) modulo those primes, once the path is written in coordinates adapted to \(P\). This lesson proves that, as \(P=(u,v)\) varies over a box, the integer matrix completing \(P\) to an element of \(\mathrm{SL}_2(\mathbb Z)\) is equidistributed modulo every squarefree \(S\) up to \(\exp(L^{0.99})\), jointly with the archimedean data \(u/U\), \(v/V\) and the ratio \(r_P\). The arithmetic input is a fourth-moment bound for Kloosterman sums, from which an elementary pointwise bound \(m^{3/4+\epsilon}\) follows; this weak bound suffices because the moduli are tiny compared with the box.

**Prerequisites.** [*Physical states and good positions*](physical-states-and-good-positions.md), Section 3; [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemma 2.1.

## 1. Kloosterman sums

For an integer \(m\ge1\) and residues \(h,k\) modulo \(m\), the **Kloosterman sum** is

\[
\begin{gathered}
K_m(h,k)=\sum_{y\in(\mathbb Z/m\mathbb Z)^\times}e\Bigl(\frac{hy+k\bar y}m\Bigr),
\end{gathered}
\]

where \(\bar y\) is the inverse of \(y\) modulo \(m\).

**Lemma 1.1 (fourth moment).** \(\displaystyle\sum_{h,k\bmod m}|K_m(h,k)|^4\le2\tau_3(m)\,m^4\).

**Proof.** Expanding \(|K_m|^4=K_m^2\overline{K_m}^{\,2}\) and summing over \(h,k\) by orthogonality, the left side is \(m^2T_m\), where \(T_m\) counts unit quadruples \((y_1,y_2,z_1,z_2)\) modulo \(m\) with

\[
\begin{gathered}
y_1+y_2=z_1+z_2,\\
\bar y_1+\bar y_2=\bar z_1+\bar z_2 .
\end{gathered}
\]

Put \(\sigma=y_1+y_2\). The second relation, multiplied by the unit \(y_1y_2z_1z_2\), reads \(\sigma(z_1z_2-y_1y_2)=0\). With \(z_2=\sigma-z_1\),

\[
\begin{aligned}
&z_1z_2-y_1y_2\\
&\quad=z_1(y_1+y_2)-z_1^2-y_1y_2\\
&\quad=-(z_1-y_1)(z_1-y_2).
\end{aligned}
\]

So \(T_m\) is at most the number of triples \((y_1,y_2,z_1)\) modulo \(m\) with \(m\mid\ell_1\ell_2\ell_3\), where \(\ell_1=y_1+y_2\), \(\ell_2=z_1-y_1\), \(\ell_3=z_1-y_2\). The linear map \((y_1,y_2,z_1)\mapsto(\ell_1,\ell_2,\ell_3)\) has determinant \(2\); its kernel modulo \(m\) consists of \(y_1=y_2=z_1=y\) with \(2y\equiv0\), at most two elements, so every triple \((\ell_1,\ell_2,\ell_3)\) has at most two preimages. If \(m\mid\ell_1\ell_2\ell_3\), one can write \(m=d_1d_2d_3\) with \(d_j\mid\ell_j\), by distributing the exponent of each prime power dividing \(m\) among the three factors. For fixed \((d_1,d_2,d_3)\) there are \(m^3/(d_1d_2d_3)=m^2\) triples with \(d_j\mid\ell_j\). Hence \(T_m\le2\tau_3(m)m^2\). \(\square\)

**Lemma 1.2 (a pointwise bound).** For every \(\epsilon>0\) there is \(C_\epsilon\) such that

\[
\begin{gathered}
|K_m(h,k)|\\
\le C_\epsilon\,m^{3/4+\epsilon}(h,k,m)^{1/4}.\quad(1.1)
\end{gathered}
\]

**Proof.** For a unit \(s\), substituting \(y\mapsto sy\) shows \(K_m(hs,k\bar s)=K_m(h,k)\). The stabilizer of \((h,k)\) under \((h,k)\mapsto(hs,k\bar s)\) consists of the units \(s\) with \(h(s-1)\equiv k(s-1)\equiv0\ (m)\), that is \(s\equiv1\) modulo \(m/g\) with \(g=(h,k,m)\). So the orbit of \((h,k)\) has \(\varphi(m)/\#\{\text{stabilizer}\}=\varphi(m/g)\) elements, all with the same Kloosterman sum, and Lemma 1.1 gives \(\varphi(m/g)|K_m(h,k)|^4\le2\tau_3(m)m^4\). Since \(\tau_3(m)\le\tau(m)^2\ll_\epsilon m^{\epsilon}\) and \(\varphi(n)\gg_\epsilon n^{1-\epsilon}\) (Exercise 10.5), the bound follows after renaming \(\epsilon\). \(\square\)

The classical Weil bound gives the exponent \(1/2+\epsilon\); the weaker exponent \(3/4\) is all that is used below.

## 2. Root matrices

For a primitive vector \((u,v)\) with \(u,v\ge2\), there is a unique integer matrix

\[
\begin{gathered}
g(u,v)=\begin{pmatrix}u&c\\v&d\end{pmatrix},\\
ud-vc=1,\qquad0\le c<u,\quad(2.1)
\end{gathered}
\]

the **root matrix** of \((u,v)\), and we put \(r=c/u\in[0,1)\). This is the ratio \(r_P\) of Lesson 8 for \(P=(u,v)\). From \(ud=1+vc\) one finds \(d/v=c/u+1/(uv)\), so \(1\le d<v\) (Exercise 10.4).

For a squarefree \(S\), the group \(\mathrm{SL}_2(\mathbb Z/S\mathbb Z)\) is the product of the groups \(\mathrm{SL}_2(\mathbb F_p)\), \(p\mid S\), by the Chinese remainder theorem, and \(|\mathrm{SL}_2(\mathbb F_p)|=p(p^2-1)\). Hence

\[
\begin{gathered}
|\mathrm{SL}_2(\mathbb Z/S\mathbb Z)|\\
=S^3\prod_{p\mid S}\Bigl(1-\frac1{p^2}\Bigr).\quad(2.2)
\end{gathered}
\]

**Theorem 2.1 (equidistribution of root matrices).** Fix \(\delta>0\). For large \(x\), uniformly for \(U,V\ge x^\delta\) with \(U,V\le x^2\), squarefree \(S\le\exp(L^{0.99})\), \(g_0\in\mathrm{SL}_2(\mathbb Z/S\mathbb Z)\) and intervals \(I_1\subseteq[1,16]\), \(I_2\subseteq[1,2]\), \(I_3\subseteq[0,1]\), the number of primitive \((u,v)\) with

\[
\begin{gathered}
\frac uU\in I_1,\quad\frac vV\in I_2,\quad r\in I_3,\\
g(u,v)\equiv g_0\ (S)
\end{gathered}
\]

is

\[
\begin{gathered}
\frac{UV\,|I_1||I_2||I_3|}{\zeta(2)\,|\mathrm{SL}_2(\mathbb Z/S\mathbb Z)|}\\
+O\bigl(UV\,x^{-\delta/200}\bigr).\quad(2.3)
\end{gathered}
\]

**Proof.** Write \(g_0=\begin{pmatrix}u_0&c_0\\v_0&d_0\end{pmatrix}\). Suppose first \(U\le V\). Fix \(u\) with \(u/U\in I_1\) and \(u\equiv u_0\ (S)\). The matrix (2.1) exists with the prescribed residues exactly when the pair \((c,v)\) satisfies

\[
\begin{gathered}
c\equiv c_0,\quad v\equiv v_0\ (S),\\
cv\equiv ud_0-1\ (uS),\quad(2.4)
\end{gathered}
\]

because \(ud-vc=1\) with \(d\equiv d_0\ (S)\) means \(1+vc\equiv ud_0\) modulo \(uS\); primitivity is then automatic.

*Counting residues.* Every solution of (2.4) has \(c\) a unit modulo \(u\), since \(cv\equiv-1\ (u)\). Conversely, for \(c\equiv c_0\ (S)\) a unit modulo \(u\), write \(v=v_0+Sj\); since \(cv_0\equiv c_0v_0\equiv u_0d_0-1\ (S)\), the last congruence of (2.4) becomes a linear congruence for \(j\) modulo \(u\) with the unit coefficient \(c\), which has exactly one solution. The residues \(c=c_0+Si\), \(i\bmod u\), are units modulo every prime \(p\mid(u,S)\) automatically (from \(u_0d_0-v_0c_0\equiv1\) and \(p\mid u_0\)), and modulo each prime \(p\mid u\), \(p\nmid S\), exactly a fraction \(1-1/p\) of them are units. So the number of solutions of (2.4) modulo \(uS\) is

\[
\begin{gathered}
M(u)=u\prod_{\substack{p\mid u\\ p\nmid S}}\Bigl(1-\frac1p\Bigr).
\end{gathered}
\]

*Discrepancy.* We claim that for every rectangle \(\mathcal R\) in the torus \((\mathbb Z/uS\mathbb Z)^2\) (a product of two intervals of residues),

\[
\begin{gathered}
\#\{(c,v)\in\mathcal R\ \text{solving (2.4)}\}\\
=M(u)\frac{|\mathcal R|}{(uS)^2}+O(u^{0.99}S^2).\quad(2.5)
\end{gathered}
\]

Let \(S_1=\prod_{p\mid(u,S)}p\), \(S_2=S/S_1\) and \(m_1=uS_1\), so that \((m_1,S_2)=1\) and \(uS=m_1S_2\). Modulo \(S_2\) the pair \((c,v)\) is fixed by (2.4). Modulo \(m_1\), (2.4) says \(c\equiv c_0\ (S_1)\) and \(cv\equiv A\ (m_1)\) with \(A=ud_0-1\), which is a unit modulo \(m_1\); the condition \(v\equiv v_0\ (S_1)\) then follows. Let \(\gamma\) be the inverse of \(S_2\) modulo \(m_1\). For \((h,k)\not\equiv(0,0)\), the Chinese remainder theorem and detection of \(c\equiv c_0\ (S_1)\) by additive characters give, up to a factor of modulus one,

\[
\begin{aligned}
&\sum_{(c,v)}e\Bigl(\frac{hc+kv}{uS}\Bigr)\\
&\quad=\frac1{S_1}\sum_{j\bmod S_1}e\Bigl(-\frac{jc_0}{S_1}\Bigr)\\
&\qquad\times K_{m_1}(\gamma h+ju,\ \gamma kA).
\end{aligned}
\]

If \(g'=(\gamma h+ju,\gamma kA,m_1)\), then \(g''=(g',u)\) divides \(k\) and \(\gamma h\), hence \(h\), so \(g''\mid(h,k,u)\), and \(g'/g''\) divides \(S_1\). For \(0<\max(|h|,|k|)\le u^{0.02}\) this gives \(g'\le S_1u^{0.02}\), and Lemma 1.2 with \(\epsilon=1/200\) bounds the sum by \(O((uS)^{3/4+1/200}(Su^{0.02})^{1/4})\)\(=O(u^{0.76}S^2)\).

Next, sandwich the indicator of each of the two intervals of \(\mathcal R\), viewed in \(\mathbb R/\mathbb Z\) after division by \(uS\), between smooth functions obtained by enlarging or shrinking the interval by \(2\Delta\) and convolving with a bump of width \(\Delta=u^{-0.01}\). Their integrals differ from the interval lengths by \(O(\Delta)\), their Fourier coefficients are bounded by \(1\), and those of frequency \(n\ne0\) are \(O_j((\Delta|n|)^{-j})\) for every \(j\). The lower and upper products of these functions bound the indicator of \(\mathcal R\) from below and above. Expanding in Fourier series, the zero frequency gives \(M(u)|\mathcal R|/(uS)^2\) up to \(O(\Delta M(u))=O(u^{0.99})\); the \(O(u^{0.04})\) frequency pairs with \(\max(|h|,|k|)\le u^{0.02}\) give \(O(u^{0.80}S^2)\); and the remaining frequencies, bounded trivially by \(M(u)\le u\), give \(O(u\,\Delta^{-1}\cdot\Delta^{-10}u^{-0.18})=O(u^{0.93})\) with \(j=10\). This proves (2.5).

*Summing over \(v\).* The integers \(c\) with \(c/u\in I_3\) form an interval of length \(u|I_3|<uS\), and the integers \(v\) with \(v/V\in I_2\) an interval of length \(V|I_2|\), which is covered by \(O(V/(uS)+1)=O(V/u)\) intervals of length at most \(uS\) (recall \(u\le16U\le16V\)). Applying (2.5) to each gives the count

\[
\begin{gathered}
\frac{V|I_2||I_3|}{S^2}\prod_{\substack{p\mid u\\ p\nmid S}}\Bigl(1-\frac1p\Bigr)+O\bigl(Vu^{-0.01}S^2\bigr).
\end{gathered}
\]

*Summing over \(u\).* Expanding the product as \(\sum_{l\mid u,\,(l,S)=1}\mu(l)/l\) and counting \(u\equiv u_0\ (S)\), \(l\mid u\), in \(UI_1\) by the Chinese remainder theorem,

\[
\begin{aligned}
&\sum_{\substack{u/U\in I_1\\ u\equiv u_0\,(S)}}\prod_{\substack{p\mid u\\ p\nmid S}}\Bigl(1-\frac1p\Bigr)\\
&\quad=\frac{U|I_1|}S\sum_{(l,S)=1}\frac{\mu(l)}{l^2}+O(\log U)\\
&\quad=\frac{U|I_1|}{\zeta(2)S}\prod_{p\mid S}\Bigl(1-\frac1{p^2}\Bigr)^{-1}\\
&\qquad+O(\log U).
\end{aligned}
\]

By (2.2) the main term is the one in (2.3). The errors total \(O(UV(U^{-0.01}S^2+U^{-1}\log U))\), and \(S^2\le\exp(2L^{0.99})=x^{o(1)}\), \(U\ge x^\delta\).

*The case \(V<U\).* By Exercise 10.4, the completion with \(0\le c<u\) is also the one with \(1\le d<v\), and \(c\equiv c_0\ (S)\) together with \(ud-vc=1\) means \(ud\equiv1+vc_0\) modulo \(vS\). Fixing \(v\equiv v_0\ (S)\) and counting pairs \((d,u)\) with \(d\equiv d_0\), \(u\equiv u_0\ (S)\) and \(du\equiv1+vc_0\ (vS)\), the argument above applies with the roles of \((u,c)\) and \((v,d)\) exchanged and with the third coordinate \(d/v\) in place of \(c/u\). Since \(d/v-c/u=1/(uv)\)\(\in[1/(32UV),1/(UV)]\), the condition \(r\in I_3\) is sandwiched between two conditions \(d/v\in I_3^\pm\) for intervals that differ from \(I_3\) by \(O(1/(UV))\) at the endpoints; their main terms differ by \(O(1)\). \(\square\)

In words: the residues of the root matrix modulo \(S\) are uniformly distributed in \(\mathrm{SL}_2(\mathbb Z/S\mathbb Z)\), independently of the size of the root and of its ratio, and primitive vectors have density \(1/\zeta(2)\). The saving \(x^{-\delta/200}\) is a fixed power of \(x\), which will absorb the \(\exp(o(L))\) many residue conditions and grid cells that occur in the next lesson.

## 3. Exercises

**10.1.** Prove that \(K_m(h,k)\) is real, and that \(K_m(h,k)=K_m(k,h)\).

**10.2.** For a prime \(m=p\), count exactly the triples \((\ell_1,\ell_2,\ell_3)\) modulo \(p\) with \(p\mid\ell_1\ell_2\ell_3\), and compare with the bound \(\tau_3(p)p^2\).

**10.3.** Prove \(|\mathrm{SL}_2(\mathbb F_p)|=p(p^2-1)\) by counting first columns and their completions.

**10.4.** For a primitive \((u,v)\) with \(u,v\ge2\) and its root matrix, show \(d/v=c/u+1/(uv)\) and \(1\le d<v\).

**10.5.** Prove \(\tau(n)\ll_\epsilon n^\epsilon\) and \(\varphi(n)\gg_\epsilon n^{1-\epsilon}\).

## 4. Solutions

**10.1.** Replacing \(y\) by \(-y\) shows \(K_m(h,k)=K_m(-h,-k)=\overline{K_m(h,k)}\). Replacing \(y\) by \(\bar y\) exchanges \(h\) and \(k\).

**10.2.** The complement consists of triples of nonzero residues, so the count is \(p^3-(p-1)^3=3p^2-3p+1\le3p^2\)\(=\tau_3(p)p^2\).

**10.3.** A first column is any nonzero vector of \(\mathbb F_p^2\), in \(p^2-1\) ways. For each, the second columns with determinant \(1\) form a coset of the line spanned by the first column, in \(p\) ways.

**10.4.** From \(ud=1+vc\), \(d/v=c/u+1/(uv)\). Since \(0\le c\le u-1\), \(d=(1+vc)/u\) lies in \([1/u,(1+v(u-1))/u]\); as \(d\) is an integer and \((1+v(u-1))/u<v\) for \(u\ge2\), we get \(1\le d\le v-1\).

**10.5.** \(\tau(n)n^{-\epsilon}=\prod_{p^e\|n}(e+1)p^{-e\epsilon}\). For \(p\ge2^{1/\epsilon}\) each factor is at most \((e+1)2^{-e}\le1\); for the finitely many smaller primes each factor is bounded by \(\max_e(e+1)2^{-e\epsilon}<\infty\). For \(\varphi\), \(\varphi(n)/n=\prod_{p\mid n}(1-1/p)\). For \(p\) larger than a bound \(p_\epsilon\), \(1-1/p\ge e^{-2/p}\ge p^{-\epsilon}\); the product over these primes is at least \(n^{-\epsilon}\), and the primes below \(p_\epsilon\) contribute at least \(2^{-p_\epsilon}\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 3.4. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026

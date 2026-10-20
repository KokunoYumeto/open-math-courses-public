# A zero-free strip at large height

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Cancellation in \(\sum_p\chi(p)p^{-1+it}\) over primes \(p\asymp N\), with \(\log N\asymp\log x\) and \(|t|\) as large as \(x^2\), requires the \(L\)-functions of the characters to have no zeros in a strip to the left of \(\operatorname{Re}s=1\) up to height about \(x^2\), of width \(w\) with \(w\log x/\log\log x\to\infty\). The classical region of de la Vallée Poussin has width about \(1/\log x\) at that height, which is not enough. This lesson proves a strip of width \(c(\log\log x)^2/\log x\) for characters of modulus at most a power of \(\log x\), from the cancellation of Lesson 4.

**Prerequisites.** [*A mean value theorem and logarithmic phases at large height*](a-mean-value-theorem-and-logarithmic-phases-at-large-height.md), Theorem 2.1; [*Entire functions of order one and the Hadamard product of xi*](course:NT-ZETA/NT-ZETA-05), Theorem 1.1 and inequality (4); [*Growth bounds and wider zero-free regions*](course:NT-ZETA/NT-ZETA-13), Theorem 1.1 (Landau's lemma); [*Nonvanishing on the line one and a zero-free region*](course:NT-ZETA/NT-ZETA-08), (1.1) and Lemma 3.1.

To avoid a clash with \(L=\log x\), the Dirichlet \(L\)-function of a character \(\chi\) is written \(D(s,\chi)\). Throughout,

\[
\begin{gathered}
L=\log x,\qquad T=\log L,\\
r_*=\frac{T^4}L,
\end{gathered}
\]

\(C_0>0\) is fixed, and \(\chi\) is a character of modulus \(q\le L^{C_0}\). Constants may depend on \(C_0\).

## 1. A truncated series

For a character \(\chi\) modulo \(q\) put \(c_\chi=\varphi(q)/q\) if \(\chi\) is principal and \(c_\chi=0\) otherwise. Then \(A(u)=\sum_{n\le u}\chi(n)=c_\chi u+R(u)\) with \(|R(u)|\le q\) for all \(u\ge0\), because \(\chi\) is periodic and its sum over a period is \(\varphi(q)\) or \(0\).

**Lemma 1.1.** For \(\operatorname{Re}s=\sigma>1\) and \(Y\ge1\),

\[
\begin{gathered}
D(s,\chi)=\sum_{n\le Y}\frac{\chi(n)}{n^s}+\frac{c_\chi Y^{1-s}}{s-1}\\
+E(s),\\
E(s)=-\frac{R(Y)}{Y^s}\\
+s\int_Y^\infty\frac{R(u)\,du}{u^{s+1}} .\quad(1.1)
\end{gathered}
\]

The right side defines a meromorphic continuation of \(D(s,\chi)\) to \(\sigma>0\), holomorphic except for a simple pole at \(s=1\) when \(\chi\) is principal, and

\[
\begin{gathered}
|E(s)|\le q\Bigl(1+\frac{|s|}\sigma\Bigr)Y^{-\sigma}\\
(\sigma>0).\quad(1.2)
\end{gathered}
\]

**Proof.** For \(\sigma>1\), \(\sum_{n>Y}\chi(n)n^{-s}=\int_Y^\infty u^{-s}dA(u)\). Insert \(A=c_\chi u+R\) and integrate the \(R\) part by parts. The integral in \(E\) converges absolutely and locally uniformly for \(\sigma>0\), which gives the continuation, and (1.2) follows from \(|R|\le q\). \(\square\)

## 2. Growth near the line one

**Lemma 2.1.** For large \(x\),

\[
\begin{gathered}
\log|D(\sigma+iv,\chi)|\le C\,T^2\\
\bigl(|\sigma-1|\le10r_*,\\
\tfrac12\le|v|\le3x^3\bigr).\quad(2.1)
\end{gathered}
\]

**Proof.** Let \(s=\sigma+iv\) be in the stated range. Then \(|s-1|\ge\frac12\), and \(|\sigma-1|\le10r_*\) gives \(Y^{|1-\sigma|}\le\exp(10r_*\log Y)\) for \(Y\ge1\).

*Moderate heights, \(|v|\le\exp(L/(2T^2))\).* Take \(Y=\exp(2L/T^2)\) in (1.1). Then \(10r_*\log Y=20T^2\), so

\[
\begin{gathered}
\Bigl|\sum_{n\le Y}\frac{\chi(n)}{n^s}\Bigr|\le\sum_{n\le Y}\frac{Y^{|1-\sigma|}}n\\
\le(1+\log Y)e^{20T^2},
\end{gathered}
\]

and the pole term is at most \(2e^{20T^2}\). By (1.2), \(|E|\le L^{C_0}\cdot4|s|Y^{-\sigma}\)\(\le\exp(-3L/(2T^2)+O(T^2))\), which is negligible. Hence \(|D|\le\exp(O(T^2))\).

*Large heights, \(\exp(L/(2T^2))<|v|\le3x^3\).* Take \(Y=x^5\). The terms with \(n\le N_1:=\exp(L/T^2)\) contribute at most \((1+L)\exp(10r_*L/T^2)=\exp(O(T^2))\). Split \(N_1<n\le x^5\) into \(O(L)\) dyadic ranges \([N',2N']\). On each, write \(\chi(n)=\sum_a\chi(a)\mathbf 1_{n\equiv a\,(q)}\) over the residues \(a\) modulo \(q\) and apply Theorem 2.1 of [*A mean value theorem and logarithmic phases at large height*](a-mean-value-theorem-and-logarithmic-phases-at-large-height.md) to the phase \(n^{-iv}\); its hypotheses hold because \(N'\in[N_1,2x^5]\) and \(\exp(L/(2T^2))\le|v|\le4x^3\). Each partial sum of \(\chi(n)n^{-iv}\) over the range is therefore at most \(q\cdot(N'/q)\exp(-L/T^{10})\). Partial summation against \(n^{-\sigma}\) (Lemma 4.2 of [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md)) bounds the range by \(2N'^{1-\sigma}\exp(-L/T^{10})\)\(\le2\exp(50T^4-L/T^{10})\). The \(O(L)\) ranges together contribute \(o(1)\). The pole term is at most \(2x^{50r_*}\exp(-L/(2T^2))=o(1)\), and \(|E|\le L^{C_0}\cdot8x^3\cdot x^{-5\sigma}\le x^{-1}\). Hence again \(|D|\le\exp(O(T^2))\). \(\square\)

## 3. The logarithmic derivative on a small disc

**Lemma 3.1 (local formula).** For large \(x\), let \(1\le|v|\le\frac52x^3\) and \(s_0=1+r_*+iv\). The zeros \(\rho\) of \(D(s,\chi)\) with \(|\rho-s_0|\le4r_*\) are \(O(T^2)\) in number, counted with multiplicity, and

\[
\begin{gathered}
\frac{D'}D(s,\chi)=\sum_{|\rho-s_0|\le4r_*}\frac1{s-\rho}\\
+O\Bigl(\frac L{T^2}\Bigr)\\
(|s-s_0|\le2r_*).\quad(3.1)
\end{gathered}
\]

**Proof.** The closed disc \(|s-s_0|\le8r_*\) lies in the region of Lemma 2.1, because \(|\sigma-1|\le9r_*\) and \(||{\operatorname{Im}s}|-|v||\le8r_*\), and it avoids the pole at \(1\). So \(f(s)=D(s,\chi)\) is holomorphic there with \(|f|\le e^{CT^2}\). At the centre the Euler product gives

\[
\begin{gathered}
|f(s_0)|\ge\prod_p\Bigl(1+\frac1{p^{1+r_*}}\Bigr)^{-1}\\
=\frac{\zeta(2+2r_*)}{\zeta(1+r_*)}\ge\frac{r_*}{1+r_*},
\end{gathered}
\]

because \(\zeta(\sigma)\le1+1/(\sigma-1)\) for \(\sigma>1\). Thus \(\log(e^{CT^2}/|f(s_0)|)\)\(\le CT^2+\log(2L/T^4)=O(T^2)\).

Jensen's formula in the form (4) of [*Entire functions of order one and the Hadamard product of xi*](course:NT-ZETA/NT-ZETA-05), applied on the disc of radius \(8r_*\), bounds the number of zeros with \(|\rho-s_0|\le4r_*\) by \(O(T^2)/\log2\). Landau's lemma (Theorem 1.1 of [*Growth bounds and wider zero-free regions*](course:NT-ZETA/NT-ZETA-13)) with \(\Upsilon=8r_*\), \(R=4r_*\) and \(r=2r_*\) gives (3.1) with error at most

\[
\begin{gathered}
\frac{6\cdot O(T^2)}{2r_*\log2}=O\Bigl(\frac{T^2}{r_*}\Bigr)=O\Bigl(\frac L{T^2}\Bigr). \ \square
\end{gathered}
\]

## 4. The strip

We use the zeta function through two facts. First, for \(1<\sigma\le2\),

\[
\begin{gathered}
-\frac{\zeta'}\zeta(\sigma)\le\frac1{\sigma-1}+C_\zeta .\quad(4.1)
\end{gathered}
\]

Indeed, \(F(s)=(s-1)\zeta(s)\) is holomorphic and nonzero on \(|s-1|\le\frac14\) (Lemma 3.1 of [*Nonvanishing on the line one and a zero-free region*](course:NT-ZETA/NT-ZETA-08)), so \(-\zeta'/\zeta(\sigma)=1/(\sigma-1)-F'/F(\sigma)\) with \(F'/F\) bounded on \([1,\frac54]\); for \(\frac54\le\sigma\le2\), \(-\zeta'/\zeta(\sigma)\le-\zeta'/\zeta(\frac54)\). Second, the identity \(3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\) ((1.1) of that lesson).

**Theorem 4.1 (zero-free strip).** There is \(c>0\), depending on \(C_0\), such that for large \(x\) no \(D(s,\chi)\) with \(\chi\) of modulus \(q\le L^{C_0}\) vanishes in

\[
\begin{gathered}
\operatorname{Re}s\ge1-\frac{cT^2}L,\\
1\le|\operatorname{Im}s|\le x^3.\quad(4.2)
\end{gathered}
\]

Moreover

\[
\begin{gathered}
\Bigl|\frac{D'}D(s,\chi)\Bigr|\le C\,L\\
\Bigl(1-\frac{cT^2}{2L}\le\operatorname{Re}s\le1+\frac1L,\\
2\le|\operatorname{Im}s|\le\frac{x^3}2\Bigr).\quad(4.3)
\end{gathered}
\]

**Proof.** For \(\sigma>1\), the coefficients of \(-D'/D(s,\chi)=\sum_n\Lambda(n)\chi(n)n^{-s}\) give, term by term,

\[
\begin{aligned}
0&\le3\Bigl(-\frac{\zeta'}\zeta(\sigma)\Bigr)\\
&\quad+4\operatorname{Re}\Bigl(-\frac{D'}D(\sigma+iv,\chi)\Bigr)\\
&\quad+\operatorname{Re}\Bigl(-\frac{D'}D(\sigma+2iv,\chi^2)\Bigr).\quad(4.4)
\end{aligned}
\]

Indeed, at \(n\) with \(\chi(n)=0\) the bracket is \(3\Lambda(n)n^{-\sigma}\ge0\), and otherwise \(\chi(n)n^{-iv}=e^{i\theta}\) and the bracket is \(\Lambda(n)n^{-\sigma}(3+4\cos\theta+\cos2\theta)\ge0\).

Suppose \(\rho=\beta+iv\) is a zero with \(\beta\ge1-cT^2/L\) and \(1\le|v|\le x^3\). The Euler product shows \(\beta\le1\). Put \(\sigma=1+20cT^2/L\), which is less than \(1+r_*\) for large \(x\). Apply Lemma 3.1 at the height \(v\) with \(s=\sigma+iv\): then \(|s-s_0|<r_*\), and \(|\rho-s_0|=1+r_*-\beta\le4r_*\), so \(\rho\) occurs in the sum. Every zero \(\rho'\) in that sum has \(\operatorname{Re}\rho'\le1<\sigma\), so \(\operatorname{Re}(1/(s-\rho'))\ge0\), and the term of \(\rho\) equals \(1/(\sigma-\beta)\). Therefore

\[
\begin{gathered}
\operatorname{Re}\Bigl(-\frac{D'}D(\sigma+iv,\chi)\Bigr)\\
\le-\frac1{\sigma-\beta}+C'\frac L{T^2}.
\end{gathered}
\]

At the height \(2v\), with \(1\le2|v|\le\frac52x^3\), Lemma 3.1 applies to \(\chi^2\) (also when \(\chi^2\) is principal, since the disc avoids \(s=1\)), and dropping the nonnegative zero terms gives \(\operatorname{Re}(-D'/D(\sigma+2iv,\chi^2))\le C'L/T^2\). With (4.1), inequality (4.4) becomes

\[
\begin{gathered}
0\le\frac3{\sigma-1}-\frac4{\sigma-\beta}+5C'\frac L{T^2}+3C_\zeta .
\end{gathered}
\]

Here \(\sigma-1=20cT^2/L\) and \(\sigma-\beta\le21cT^2/L\), so the right side is at most

\[
\begin{gathered}
\frac L{T^2}\Bigl(\frac3{20c}-\frac4{21c}+5C'\Bigr)+3C_\zeta\\
=\frac L{T^2}\Bigl(5C'-\frac{17}{420c}\Bigr)+3C_\zeta,
\end{gathered}
\]

which is negative for large \(x\) once \(c<17/(4200C')\). This contradiction proves (4.2).

For (4.3), let \(s\) be in the stated region and apply Lemma 3.1 with \(v=\operatorname{Im}s\); then \(|s-s_0|\le r_*+cT^2/(2L)\le2r_*\). Every zero \(\rho'\) in the sum satisfies \(|\operatorname{Im}\rho'|\in[|v|-4r_*,|v|+4r_*]\subseteq[1,x^3]\), hence \(\operatorname{Re}\rho'<1-cT^2/L\) by (4.2), and \(|s-\rho'|\ge cT^2/(2L)\). The \(O(T^2)\) zero terms contribute \(O(L/c)\), and the error in (3.1) is \(O(L/T^2)\). \(\square\)

The width \(cT^2/L\) comes from balancing two scales: the growth bound \(\log|D|\ll T^2\) controls the zeros on discs of radius \(r_*=T^4/L\), and the logarithmic derivative is then known up to an error \(T^2/r_*=L/T^2\). The programme also contains the much wider Vinogradov–Korobov region for characters (Theorem 8.3 of [*Zero-free regions and the exceptional zero*](course:NT-DIRL/NT-DIRL-07)); the strip proved here rests only on the elementary mean value theorem of Lesson 4 and suffices for the next lesson.

## 5. Exercises

**5.1.** Check that (1.1) agrees with the Dirichlet series for \(\sigma>1\), and that for \(0<\sigma\le1\) its right side does not depend on \(Y\).

**5.2.** Prove \(\zeta(\sigma)\le\sigma/(\sigma-1)\) for \(\sigma>1\), and deduce \(|D(1+r+iv,\chi)|\ge r/(1+r)\) for every character and \(r>0\).

**5.3.** Prove \(3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\).

**5.4.** At height \(|t|=x^2\) and modulus \(q\le L^{C_0}\), the classical region has width about \(c_1/\log(q(|t|+2))\asymp1/L\). Let \(N=x^{1/2}\). Compute \(N^{-w}\) for \(w=c_1/(3L)\) and for \(w=cT^2/(2L)\), and explain which one beats every fixed power of \(L\).

**5.5.** Show that the number of zeros of \(D(s,\chi)\) with \(|\rho-(1+r_*+iv)|\le4r_*\) is \(O(T^2)\) uniformly in \(1\le|v|\le\frac52x^3\), using Jensen's formula directly rather than its corollary.

## 6. Solutions

**5.1.** For \(\sigma>1\) the identity is the partial summation of the proof. For two values \(Y<Y'\), both right sides are holomorphic in \(\sigma>0\) away from \(s=1\) and agree for \(\sigma>1\), so they agree on \(\sigma>0\) by uniqueness of analytic continuation.

**5.2.** \(\zeta(\sigma)\le1+\int_1^\infty u^{-\sigma}du\)\(=1+1/(\sigma-1)=\sigma/(\sigma-1)\). Then \(|D(1+r+iv,\chi)|\)\(\ge\zeta(2+2r)/\zeta(1+r)\)\(\ge1/\zeta(1+r)\ge r/(1+r)\), as in the proof of Lemma 3.1.

**5.3.** \(\cos2\theta=2\cos^2\theta-1\), so the left side is \(2+4\cos\theta+2\cos^2\theta\).

**5.4.** \(\log N=L/2\), so \(N^{-w}=e^{-c_1/6}\) for the classical width, a constant, and \(N^{-w}=\exp(-cT^2/4)=L^{-cT/4}\) for the strip of this lesson, which is smaller than \(L^{-A}\) for every fixed \(A\) once \(T>4A/c\).

**5.5.** With \(f(s)=D(s,\chi)\) on the disc of radius \(8r_*\) about \(s_0\), Jensen's formula gives \(\sum_{|\rho-s_0|<8r_*}\log(8r_*/|\rho-s_0|)\)\(\le\max\log|f|-\log|f(s_0)|=O(T^2)\) (after perturbing the radius to avoid zeros on the circle). Each zero with \(|\rho-s_0|\le4r_*\) contributes at least \(\log2\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Appendix, Lemmas 9.6–9.8. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026

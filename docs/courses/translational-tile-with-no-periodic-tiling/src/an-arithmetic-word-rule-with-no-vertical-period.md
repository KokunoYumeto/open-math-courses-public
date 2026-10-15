# An arithmetic word rule with no vertical period

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Aperiodicity in this course comes from a finite rule for arrays \(W(n,m)\) with finitely many columns \(n\) and infinitely many rows \(m\). The rule prescribes, through a finite list of allowed words, what the array may look like along every line of integer slope. One array obeys the rule and has no constant column: the array whose entry in row \(m\) is the last nonzero digit of \(m\) in base \(p\). But no array that obeys the rule and has no constant column can have a vertical period. The rule is the two-digit \(p\)-adic Sudoku rule of Greenfeld and Tao [Greenfeld–Tao 2025, Definition 4.5], and the proof follows their structure theorems for it [Greenfeld–Tao 2025, Theorem 4.7, Lemma 4.8 and Section 4.2], in the form proved in [OpenAI-PT, Section 2]. The lessons [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) and [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) turn the rule into tiling equations.

- Allowed words and the line rule (Section 1).
- The global affine approximation (Section 2).
- Vertical nondegeneracy (Section 3).
- The vertical-period obstruction (Section 4).
- The last-nonzero-digit model (Section 5).

Throughout the lesson \(p>200\) is a fixed prime, and
\[
\begin{gathered}N=p^2,\qquad\Sigma=\mathbb F_p^\times,\\ I=\{0,1,\ldots,N-1\}.\end{gathered}
\]
Here \(\mathbb F_p=\mathbb Z/p\mathbb Z\), and \(\Sigma\) is its set of nonzero residues, the alphabet of the words. When an integer appears in an expression over \(\mathbb F_p\), its residue modulo \(p\) is meant. We write \(p\parallel x\) when \(p\mid x\) and \(p^2\nmid x\). An *affine form* over \(\mathbb F_p\) in one variable is a function \(n\mapsto\alpha n+\beta\), in two variables \((n,m)\mapsto\alpha n+\beta m+\gamma\), with coefficients in \(\mathbb F_p\); it is *nonzero* if its coefficients are not all zero. A nonzero constant form is allowed. A nonzero affine form in one variable vanishes on at most one residue class, and two affine forms in one variable that agree at two distinct residues are equal.

## 1. Allowed words and the line rule

**Definition 1.1.** A word \(w\colon I\to\Sigma\) is *allowed* if there are integers \(a,b\), not both divisible by \(p\), such that for every \(n\in I\)
\[
\begin{aligned}
w(n)&=an+b&&\text{if }p\nmid an+b,\\
w(n)&=\tfrac{an+b}p&&\text{if }p\parallel an+b,
\end{aligned}
\]
the values being residues modulo \(p\). At indices with \(p^2\mid an+b\) the value \(w(n)\) is arbitrary. The pair \((a,b)\) is a *witness*. An array \(W\colon I\times\mathbb Z\to\Sigma\) satisfies the *line rule* if for all integers \(d,e\) the word
\[
n\longmapsto W(n,dn+e)
\]
is allowed. A *positive vertical period* of \(W\) is an integer \(M>0\) with \(W(n,m+M)=W(n,m)\) for all \((n,m)\in I\times\mathbb Z\).

The residues of \(a\) and \(b\) modulo \(p^2\) determine, for every \(n\), which of the three cases occurs and the prescribed value: if \(an+b\equiv pk\pmod{p^2}\), then \((an+b)/p\equiv k\pmod p\). So the set \(\mathcal W\subseteq\Sigma^I\) of allowed words is finite, and the line rule is a finite list of constraints along each line.

**Example 1.2.** The definition makes sense for every prime. For \(p=5\) and the witness \((a,b)=(1,0)\), the allowed words are those with \(w(n)=n\bmod 5\) for \(5\nmid n\) and \(w(5k)=k\bmod5\) for \(k=1,2,3,4\); the value \(w(0)\) is arbitrary.

Let \(w\) be allowed with witness \((a,b)\) and let \(\ell(n)=\bar an+\bar b\) be the reduction of \(an+b\) modulo \(p\). It is a nonzero form, and \(w(n)=\ell(n)\) wherever \(\ell(n)\ne0\). The zeros of \(\ell\) form at most one residue class, which contains \(N/p=p\) elements of \(I\). We call these at most \(p\) indices the *exceptional* indices of the witness.

## 2. The global affine approximation

**Lemma 2.1** (global affine approximation; [OpenAI-PT, Lemma 2.2]). If \(W\) satisfies the line rule, there is a nonzero affine form \(H(n,m)=An+Bm+C\) over \(\mathbb F_p\) such that \(W(n,m)=H(n,m)\) at every cell \((n,m)\) with \(H(n,m)\ne0\).

*Proof.* For every line \(\{(n,dn+e):n\in I\}\) with slope \(d\in\{-1,0,1\}\) and intercept \(e\in\mathbb Z\), choose a witness for its word and let \(\ell_{d,e}\) be the reduced form, so \(W(n,dn+e)=\ell_{d,e}(n)\) wherever \(\ell_{d,e}(n)\ne0\). A cell \((n,dn+e)\) is *exceptional for slope \(d\)* if \(\ell_{d,e}(n)=0\). Each line contains at most \(p\) exceptional cells.

*Step 1: a square without exceptional cells.* A *square* is a set \(\{r,\ldots,r+3\}\times\{q,\ldots,q+3\}\) of \(16\) cells. Let \(K\ge4\) and consider the squares inside the rectangle \(I\times\{0,\ldots,K-1\}\); there are \((N-3)(K-3)\) of them. The lines of slope \(0\), \(1\) and \(-1\) that meet the rectangle number \(K\), \(K+N-1\) and \(K+N-1\): for slope \(1\), the line \(m=n+e\) meets it exactly when \(-(N-1)\le e\le K-1\), and similarly for slope \(-1\). These lines carry at most \(p(3K+2N-2)\) exceptional cells in the rectangle, and each cell lies in at most \(16\) squares. So at most \(16p(3K+2N)\) squares contain an exceptional cell for some slope. Since \(p\ge49\), \(N-3-48p=p^2-48p-3>0\), and we can choose \(K\ge4\) with
\[
K>\frac{3(N-3)+32pN}{N-3-48p}.
\]
Then
\[
\begin{aligned}
&(N-3)(K-3)-16p(3K+2N)\\
&\quad=K(N-3-48p)\\
&\qquad-3(N-3)-32pN>0,
\end{aligned}
\]
so some square contains no exceptional cell for any of the three slopes.

*Step 2: an affine form on the square.* Let the square have columns \(r,\ldots,r+3\) and rows \(q,\ldots,q+3\). For each row \(m\) of the square, the row form \(\ell_{0,m}(n)=U_mn+V_m\) agrees with \(W\) on the four cells of that row in the square. Let \(m\in\{q+1,q+2\}\) and \(n\in\{r+1,r+2\}\). The cells \((n-1,m-1)\), \((n,m)\), \((n+1,m+1)\) lie in the square on one line of slope \(1\), where \(W\) agrees with an affine function of the column index; hence the second difference
\[
\begin{aligned}&W(n-1,m-1)-2W(n,m)\\&\quad+W(n+1,m+1)\end{aligned}
\]
vanishes. The same holds on the line of slope \(-1\) through \((n-1,m+1)\), \((n,m)\), \((n+1,m-1)\). Inserting the row forms, for each sign,
\[
\begin{aligned}
0={}&n\,(U_{m+1}-2U_m+U_{m-1})\\
&+(V_{m+1}-2V_m+V_{m-1})\\
&\pm(U_{m+1}-U_{m-1}).
\end{aligned}
\]
Subtracting the identities for \(n=r+1\) and \(n=r+2\) gives \(U_{m+1}-2U_m+U_{m-1}=0\). Subtracting the two signs gives \(2(U_{m+1}-U_{m-1})=0\), so \(U_{m+1}=U_{m-1}\) since \(p\) is odd. Together, \(U_{m-1}=U_m=U_{m+1}\). Taking \(m=q+1\) and \(m=q+2\), the four row slopes have a common value \(A\). The identities then give \(V_{m+1}-2V_m+V_{m-1}=0\) for \(m=q+1,q+2\), so \(V_m=Bm+C\) on the four rows for some \(B,C\in\mathbb F_p\). The form \(H(n,m)=An+Bm+C\) agrees with \(W\) on the square. It is nonzero, since the entries of \(W\) are nonzero.

*Step 3: good cells spread along lines.* Call a cell *good* if \(H(n,m)=0\) or \(W(n,m)=H(n,m)\). We claim: if four consecutive cells of a line of slope \(d\in\{-1,0,1\}\) are good, the whole line is good. On the line \(m=dn+e\), the function \(h(n)=H(n,dn+e)\), that is \(h(n)=(A+Bd)n+(Be+C)\), is an affine form in \(n\). If it is the zero form, every cell of the line is good. Otherwise \(h\) and \(\ell_{d,e}\) each vanish at most at one of the four consecutive indices, which are distinct modulo \(p\). So at least two of the four indices have \(h\ne0\) and \(\ell_{d,e}\ne0\). There goodness gives \(W=h\) and the word rule gives \(W=\ell_{d,e}\). The forms \(h\) and \(\ell_{d,e}\) agree at two distinct residues, so they are equal. Wherever this common form is nonzero, \(W=\ell_{d,e}=h\); where it vanishes, the cell is good by definition. This proves the claim.

*Step 4: every cell is good.* The four rows of the square contain four consecutive good cells each, so these four rows are entirely good. Suppose the rows \(m-4,\ldots,m-1\) are entirely good, and let \(n\in I\). Since \(N\ge8\), one of \(n+4\le N-1\) or \(n-4\ge0\) holds; choose \(\varepsilon\in\{1,-1\}\) accordingly, so that \(n+j\varepsilon\in I\) for \(1\le j\le4\). The cells \((n+j\varepsilon,m-j)\), \(1\le j\le4\), are good and are four consecutive cells of the line of slope \(-\varepsilon\) through \((n,m)\). By the claim, \((n,m)\) is good. So row \(m\) is good. Below a block of four good rows use the cells \((n+j\varepsilon,m+j)\) instead. By induction all rows are good, which is the assertion of the lemma. \(\square\)

## 3. Vertical nondegeneracy

**Lemma 3.1** (vertical nondegeneracy; [OpenAI-PT, Lemma 2.3]). Let \(W\) satisfy the line rule, and let \(H(n,m)=An+Bm+C\) be a form as in Lemma 2.1.

1. Every column of \(W\) is nonconstant if and only if \(B\ne0\). In that case every column takes every value in \(\Sigma\).
2. If \(B\ne0\), every positive vertical period of \(W\) is divisible by \(p\).

*Proof.* (1) If \(B=0\), the form \(An+C\) is nonzero, so it is nonzero at some \(n\in\{0,\ldots,p-1\}\), and column \(n\) is constant with value \(An+C\). If \(B\ne0\), then for fixed \(n\) the value \(H(n,m)\) runs through all of \(\mathbb F_p\) as \(m\) runs through \(p\) consecutive integers; at the \(p-1\) rows where it is nonzero, \(W(n,m)=H(n,m)\). So the column takes every value of \(\Sigma\), and is nonconstant since \(p-1\ge2\).

(2) Let \(M>0\) be a vertical period and fix \(n\). The rows \(m\) with \(H(n,m)=0\) or \(H(n,m+M)=0\) form at most two residue classes modulo \(p\), so some \(m\) avoids both. Then \(W(n,m)=H(n,m)\) and \(W(n,m+M)=H(n,m+M)\), and the period gives, in \(\mathbb F_p\),
\[
BM=H(n,m+M)-H(n,m)=0 .
\]
Since \(B\ne0\), \(p\mid M\). \(\square\)

## 4. The vertical-period obstruction

**Proposition 4.1** (the obstruction; [OpenAI-PT, Proposition 2.4]). No array \(W\colon I\times\mathbb Z\to\Sigma\) satisfies the line rule, has every column nonconstant, and has a positive vertical period.

*Proof.* Suppose such arrays exist, and let \(M\) be the least positive integer that is a vertical period of one of them. Choose such an array \(W\) with period \(M\) and a form \(H=An+Bm+C\) for it as in Lemma 2.1. By Lemma 3.1, \(B\ne0\) and \(p\mid M\).

*Normalization.* Choose integers \(u,v\) with \(A+Bu=0\) and \(C+Bv=0\) in \(\mathbb F_p\), and put \(\widetilde W(n,m)=W(n,m+un+v)\). The word of \(\widetilde W\) on the line of slope \(d\) and intercept \(e\) is the word of \(W\) on the line of slope \(d+u\) and intercept \(e+v\), so \(\widetilde W\) satisfies the line rule. Each column of \(\widetilde W\) is a column of \(W\) translated in the row variable, so the columns stay nonconstant and \(M\) stays a period. Moreover \(\widetilde W(n,m)=H(n,m+un+v)=Bm\) wherever \(Bm\ne0\), that is, wherever \(p\nmid m\). Replace \(W\) by \(\widetilde W\). From now on
\[
W(n,m)=Bm\quad\text{whenever }p\nmid m .
\]

*Rescaling.* Put \(W_1(n,m)=W(n,pm)\). The word of \(W_1\) on the line of slope \(d\) and intercept \(e\) is the word of \(W\) on the line of slope \(pd\) and intercept \(pe\), so \(W_1\) satisfies the line rule. By Lemma 2.1 it has a form \(H_1(n,m)=A_1n+B_1m+C_1\).

*The rescaled array has no constant column.* Suppose \(B_1=0\). Then \(A_1n+C_1\) is a nonzero form; choose \(0\le n_0<p\) with \(c=A_1n_0+C_1\ne0\). Consider the line \(m=n-n_0\) of \(W\) and a witness \((a,b)\) for its word. The forms \(\bar an+\bar b\) and \(B(n-n_0)\) both agree with \(W(n,n-n_0)\) wherever they are nonzero, and they are both nonzero on at least \(p-2\ge2\) residues. So they are equal:
\[
a\equiv B,\qquad b\equiv-Bn_0\pmod p .
\]
Hence \(p\mid an_0+b\) and \(p\nmid a\). For \(0\le k<p\) the index \(n=n_0+pk\) lies in \(I\), since \(n_0+p(p-1)\le p^2-1\), and the cell \((n_0+pk,pk)\) lies on the line. On one hand,
\[
W(n_0+pk,pk)=W_1(n_0+pk,k)=c,
\]
because \(H_1(n_0+pk,k)=A_1n_0+C_1=c\ne0\). On the other hand, \(a(n_0+pk)+b=p\,t_k\) with the integer
\[
t_k=\frac{an_0+b}p+ak .
\]
If \(p\nmid t_k\), then \(p\parallel a(n_0+pk)+b\), and the witness forces \(W(n_0+pk,pk)=t_k\bmod p\). As \(k\) runs through \(0,\ldots,p-1\), the residues of \(t_k\) run through all of \(\mathbb F_p\), since \(p\nmid a\). So the \(p-1\) indices \(k\) with \(p\nmid t_k\) give entries with \(p-1\ge2\) distinct values, while all of them equal \(c\). This contradiction shows \(B_1\ne0\).

*Conclusion.* By Lemma 3.1, every column of \(W_1\) is nonconstant. The positive integer \(M/p\) is a vertical period of \(W_1\):
\[
\begin{aligned}&W_1(n,m+M/p)\\&\quad=W(n,pm+M)=W(n,pm)\\&\quad=W_1(n,m).\end{aligned}
\]
Since \(M/p<M\), this contradicts the choice of \(M\). \(\square\)

## 5. The last-nonzero-digit model

For a nonzero integer \(t\) let \(\operatorname{ord}_p(t)\) be the largest integer \(r\ge0\) with \(p^r\mid t\), and define
\[
f(t)=\frac t{p^{\operatorname{ord}_p(t)}}\bmod p,\qquad f(0)=1 .
\]
So \(f(t)\) is the last nonzero digit of \(t\) in base \(p\), also for negative \(t\).

**Lemma 5.1** (a model for the line rule; [OpenAI-PT, Lemma 2.5]). The function \(f\) takes values in \(\Sigma\). The array \(W(n,m)=f(m)\) satisfies the line rule and every column takes every value in \(\Sigma\).

*Proof.* The integer \(t/p^{\operatorname{ord}_p(t)}\) is not divisible by \(p\), so \(f(t)\ne0\); and \(f(0)=1\). For every \(r\ge0\) and \(t\in\mathbb Z\) we have \(f(p^rt)=f(t)\), also for \(t=0\).

Fix integers \(d,e\). If \((d,e)\ne(0,0)\), let \(r\) be the largest integer with \(p^r\mid d\) and \(p^r\mid e\), and write \(d=p^ra\), \(e=p^rb\). Then \(a,b\) are not both divisible by \(p\), and \(f(dn+e)=f(an+b)\) for every \(n\). If \(p\nmid an+b\), then \(f(an+b)=an+b\bmod p\). If \(p\parallel an+b\), then \(f(an+b)=(an+b)/p\bmod p\). At the remaining indices the rule prescribes nothing. So \((a,b)\) witnesses that the word \(n\mapsto W(n,dn+e)\) is allowed. If \((d,e)=(0,0)\), the word is constantly \(f(0)=1\), with the witness \((0,1)\). Finally, column \(n\) contains the values \(f(1),\ldots,f(p-1)\), which are \(1,\ldots,p-1\). \(\square\)

The tiling equations of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) and the lessons after it parametrize the lines by points \(x=(x_1,x_2)\in\mathbb Z^2\). For \(n\in I\) put
\[
L_n(x)=x_2+nx_1,\qquad u_n=(1,-n).
\]

**Lemma 5.2** (line maps; [OpenAI-PT, Section 2]).

1. Each \(L_n\colon\mathbb Z^2\to\mathbb Z\) is a surjective homomorphism, and its kernel is \(\mathbb Zu_n\).
2. For every \(x\in\mathbb Z^2\), the word \(n\mapsto f(L_n(x))\) is allowed.
3. If \(x_1\equiv0\) and \(x_2\equiv t\pmod p\) with \(t\in\{1,2\}\), then \(f(L_n(x))=t\) for every \(n\in I\).

*Proof.* (1) \(L_n(0,t)=t\), and \(x_2+nx_1=0\) means \(x=x_1(1,-n)\). (2) The word is the word of the model array \(W(n,m)=f(m)\) on the line of slope \(x_1\) and intercept \(x_2\), allowed by Lemma 5.1. (3) Every \(L_n(x)\) is congruent to \(t\not\equiv0\) modulo \(p\), so its last nonzero digit is \(t\). \(\square\)

So at every point \(x\) the model supplies an allowed word, and at the points of two residue classes modulo \(p\) it supplies the constant words \(1\) and \(2\). The lesson [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) uses constant words of this kind to force nonconstant columns.

## 6. Exercises

**6.1.** Show that the conditions \(p^2-48p-3>0\) and \(p\ge49\) are equivalent for primes \(p\), and compute the least admissible \(K\) in Step 1 of the proof of Lemma 2.1 for \(p=211\).

**6.2.** Let \(W\) satisfy the line rule. Show that the following arrays satisfy it too: \(W(n,m+c)\) for \(c\in\mathbb Z\); \(W(n,m+un)\) for \(u\in\mathbb Z\); \(W(n,km)\) for every integer \(k\ne0\).

**6.3.** For the model array \(W(n,m)=f(m)\), find a form \(H\) as in Lemma 2.1. Then show, for any array \(W\) with the line rule, that the form \(H\) of Lemma 2.1 is uniquely determined by \(W\).

**6.4.** Show that for a witness \((a,b)\) at most one index \(n\in I\) has \(p^2\mid an+b\), and that the number of allowed words is at most \(p^4(p-1)\).

**6.5.** Let \(W\) satisfy the line rule, have every column nonconstant, and let \(M\ge1\). Show directly from Lemma 3.1 that if \(W\) has period \(M\) then \(p\mid M\), and that the array \(W_1(n,m)=W(n,pm)\) of the proof of Proposition 4.1 has period \(M/p\). Why does this not already give a contradiction without the step \(B_1\ne0\)?

## 7. Solutions

**6.1.** The roots of \(x^2-48x-3\) are \(24\pm\sqrt{579}\), and \(24+\sqrt{579}\approx48.06\), so for integers \(p\ge0\) the inequality holds exactly when \(p\ge49\). For \(p=211\): \(N=44521\), \(N-3-48p=34390\), \(3(N-3)=133554\), \(32pN=300605792\), their sum is \(300739346\), and \(300739346/34390\approx8744.97\), so the least admissible \(K\) is \(8745\).

**6.2.** The word of \(W(n,m+c)\) on the line \(m=dn+e\) is the word of \(W\) on the line \(m=dn+(e+c)\); for \(W(n,m+un)\) it is the line \(m=(d+u)n+e\); for \(W(n,km)\) it is the line \(m=kdn+ke\).

**6.3.** For the model, \(W(n,m)=f(m)=m\bmod p\) whenever \(p\nmid m\), so \(H(n,m)=m\) works. Let \(H\) and \(H'\) both have the property of Lemma 2.1, and view them as functions on \(\mathbb F_p^2\); the cells of \(I\times\mathbb Z\) reach every pair of residues. At every cell where \(H\) and \(H'\) are both nonzero, both equal \(W\), so \(H-H'\) vanishes at every point of \(\mathbb F_p^2\) outside the zero sets of \(H\) and \(H'\). The zero set of a nonzero affine form on \(\mathbb F_p^2\) is empty or a line with \(p\) points, so \(H-H'\) vanishes on at least \(p^2-2p\) points. If \(H-H'\) were nonzero, it would vanish on at most \(p\) points, and \(p<p^2-2p\) because \(p>3\). So \(H=H'\).

**6.4.** If \(p\mid a\), then \(p\nmid b\) and \(an+b\equiv b\not\equiv0\pmod p\), so no index qualifies. If \(p\nmid a\), then \(a\) is invertible modulo \(p^2\), and \(an+b\equiv0\pmod{p^2}\) holds for exactly one residue class of \(n\) modulo \(p^2\), which contains exactly one element of \(I\). The prescribed values depend only on \((a\bmod p^2,\,b\bmod p^2)\), at most \(p^4\) choices, and given these the word is determined except at the at most one free index, where it takes one of \(p-1\) values.

**6.5.** If \(W\) has nonconstant columns, Lemma 3.1 gives \(B\ne0\) and \(p\mid M\). The equalities \(W_1(n,m+M/p)=W(n,pm+M)\) and \(W(n,pm+M)=W(n,pm)\) show that \(M/p\) is a period of \(W_1\), and \(W_1\) satisfies the line rule by Exercise 6.2. But the minimality argument needs \(W_1\) to belong to the same class of arrays, that is, to have no constant column; without that, \(W_1\) could be an array with a constant column and the period \(M/p\), which is not excluded by anything.

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
- [Greenfeld–Tao 2025] R. Greenfeld, T. Tao, *Undecidability of translational monotilings*, J. Eur. Math. Soc. (2025). https://arxiv.org/abs/2309.09504

# Simultaneous fixed spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the planar argument of the next lesson, the nonsingularity of a system enters through one statement about unitary matrices. Several unitary variables \(X_1,\ldots,X_r\), of sizes \(k_1,\ldots,k_r\), occur as diagonal blocks, with exponent \(1\) or \(-1\), in block matrices that are then multiplied by arbitrary fixed unitaries \(P_j\). If the matrix of signed block counts has full row rank over \(\mathbb Q\), the variables can be chosen so that the fixed spaces of all these matrices together have dimension at least \(k_1+\cdots+k_r\). For one variable whose signs add up to \(\pm1\) this is the lemma of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space). In general the proof computes an intersection number in the rational cohomology of a product of unitary groups, and the rank condition enters as a product of nested nonzero minors [OpenAI-NS, Theorem 2].

- The theorem (Section 1).
- Target dimensions from nested minors (Section 2).
- The leading term of the incidence class (Section 3).
- The intersection number (Section 4).

Notation from [Rational cohomology of unitary groups](rational-cohomology-of-unitary-groups.md): cohomology with rational coefficients, the primitive generators \(e_{a,d}\) of \(H^*(\mathrm U(d))\), the incidence manifolds \(R(d,l)\) with projection \(p\), and the classes \(\alpha(d,l)\in H^{l^2}(\mathrm U(d))\) dual to \(p_*[R(d,l)]\).

## 1. The theorem

**Theorem 1.1** (simultaneous fixed spaces; [OpenAI-NS, Theorem 2]). Let \(r\ge0\), \(n\ge1\) and \(k_1,\ldots,k_r\ge1\). For \(1\le j\le n\) let \(\mathcal B_j\) be a finite ordered list of pairs \((i,s)\) with \(1\le i\le r\) and \(s\in\{1,-1\}\), repetitions allowed, and put
\[
d_j=\sum_{(i,s)\in\mathcal B_j}k_i,\qquad b_{ij}=\sum_{(i,s)\in\mathcal B_j}s ,
\]
the second sum over the entries with first coordinate \(i\). Suppose that the \(r\times n\) matrix \(B=(b_{ij})\) has rank \(r\) over \(\mathbb Q\). For arbitrary \(P_j\in\mathrm U(d_j)\) put
\[
\begin{gathered}
D=\prod_{i=1}^r\mathrm U(k_i),\\
F_j(X)=\operatorname{diag}_{(i,s)\in\mathcal B_j}\bigl(X_i^{\,s}\bigr)\,P_j\quad(X\in D).
\end{gathered}
\]
Then there is \(X\in D\) with
\[
\begin{aligned}
&\sum_{j=1}^n\dim_{\mathbb C}\ker\bigl(F_j(X)-I\bigr)\\
&\qquad\ge\sum_{i=1}^rk_i .
\end{aligned}
\tag{1.1}
\]

Here \(\mathrm U(0)\) and an empty product of groups are points, and a matrix of size zero has fixed space of dimension zero. For \(r=0\) there is nothing to prove.

**Example 1.2.** Let \(r=1\), \(k_1=k\), \(n=1\) and \(\mathcal B_1=((1,s_1),\ldots,(1,s_N))\) with \(\sum_ts_t=\pm1\). Then \(B=(\pm1)\), and Theorem 1.1 says that \(\operatorname{diag}(X^{s_1},\ldots,X^{s_N})P\) fixes a subspace of dimension \(k\) for some \(X\in\mathrm U(k)\): this is Lemma 5.1 of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space). If \(\sum_ts_t=0\), the conclusion can fail (Exercise 5.2).

## 2. Target dimensions from nested minors

For a matrix \(B\) and index lists, \(B[1,\ldots,t\mid j_1,\ldots,j_t]\) denotes the square submatrix with rows \(1,\ldots,t\) and columns \(j_1,\ldots,j_t\).

**Lemma 2.1.** Let \(B\) be an \(r\times n\) rational matrix of rank \(r\). There are distinct columns \(j_1,\ldots,j_r\) such that the square matrices \(B_t=B[1,\ldots,t\mid j_1,\ldots,j_t]\), \(1\le t\le r\), satisfy
\[
\det B_t\ne0 .
\tag{2.1}
\]

*Proof.* The rows of \(B\) are linearly independent, so for each \(t\) the first \(t\) rows have rank \(t\), and the columns of \(B\), cut down to these rows, span \(\mathbb Q^t\). Choose the columns one at a time. Suppose that \(j_1,\ldots,j_{t-1}\) satisfy (2.1) up to \(t-1\), so that these columns, cut down to rows \(1,\ldots,t-1\), are linearly independent (for \(t=1\) there is nothing to suppose). Then the same columns cut down to rows \(1,\ldots,t\) are linearly independent, and since the cut-down columns span \(\mathbb Q^t\), some column \(j_t\) is not in the span of these \(t-1\) vectors. It differs from \(j_1,\ldots,j_{t-1}\), the \(t\) cut-down columns form a basis of \(\mathbb Q^t\), and (2.1) holds for \(t\). \(\square\)

*Proof of Theorem 1.1, first step.* Let \(r\ge1\) and order the variables so that \(k_1\ge k_2\ge\cdots\ge k_r\); this permutes the rows of \(B\) and keeps its rank. Choose columns as in Lemma 2.1 and put
\[
\begin{gathered}
l_{j_t}=k_t\quad(1\le t\le r),\\
l_j=0\ \text{ for the other }j.
\end{gathered}
\]
Then \(l_j\le d_j\): for \(j=j_t\), the nonzero minor (2.1) has a nonzero entry \(b_{i,j_t}\) with \(i\le t\), so \(\mathcal B_{j_t}\) contains a block of size \(k_i\ge k_t\). Moreover
\[
\begin{gathered}
\sum_jl_j=\sum_ik_i,\\
\sum_jl_j^2=\sum_ik_i^2=\dim D .
\end{gathered}
\tag{2.2}
\]
We shall find \(X\in D\) with \(\dim\ker(F_j(X)-I)\ge l_j\) for every \(j\) simultaneously; by (2.2) this gives (1.1).

## 3. The leading term of the incidence class

**Lemma 3.1** ([OpenAI-NS, (2.7)]). For \(0\le l\le d\),
\[
\begin{gathered}
\alpha(d,l)=c_{d,l}\,e_{1,d}e_{2,d}\cdots e_{l,d}+\rho ,\\
c_{d,l}\ne0 ,
\end{gathered}
\]
where \(\rho\) is a combination of products of fewer than \(l\) generators.

*Proof.* For \(l=0\), \(\alpha(d,0)=1\) and \(c_{d,0}=1\). Let \(l\ge1\). A product of \(u\) distinct generators has degree at least \(1+3+\cdots+(2u-1)=u^2\), and \(\alpha(d,l)\) has degree \(l^2\). So its terms have at most \(l\) generators, and a term with exactly \(l\) generators has degrees \(1,3,\ldots,2l-1\): it is a multiple of \(e_{1,d}\cdots e_{l,d}\). Let \(c_{d,l}\) be the coefficient.

To show \(c_{d,l}\ne0\), consider
\[
\begin{gathered}
f:\mathrm U(l)\to\mathrm U(d),\\
f(X)=X\oplus(-I_{d-l}).
\end{gathered}
\]
A pair \((X,(W,E))\) with \(f(X)=p(W,E)\) has \(W=X\oplus(-I_{d-l})\) fixing an \(l\)-dimensional subspace \(E\) pointwise; the fixed vectors of \(W\) lie in \(\mathbb C^l\oplus0\), so \(E=\mathbb C^l\oplus0\) and \(X=I_l\). So there is exactly one pair, \(X=I_l\), \(W_0=I_l\oplus(-I_{d-l})\), \(E_0=\mathbb C^l\oplus0\).

At this pair the tangent images of \(f\) and \(p\) together span the tangent space \(\mathfrak u(d)W_0\) of \(\mathrm U(d)\) at \(W_0\), where \(\mathfrak u(d)\) is the space of skew-Hermitian matrices. Write matrices in blocks for \(\mathbb C^d=E_0\oplus E_0^\perp\). The curves \(f(e^{tA})=e^{tA}\oplus(-I_{d-l})\), \(A\in\mathfrak u(l)\), give the tangent vectors \(\operatorname{diag}(A,0)\). For \(p\), use the chart of Lemma 2.1 of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space) at \((W_0,E_0)\), with \(g=I\) and \(Y_1=-I_{d-l}\): with \(K_Z=\begin{pmatrix}0&-Z^*\\Z&0\end{pmatrix}\), the curves
\[
\begin{aligned}
&t\mapsto p\,\chi(tZ,tB)\\
&\quad=e^{tK_Z}\bigl(I_l\oplus(-e^{tB})\bigr)e^{-tK_Z}
\end{aligned}
\]
have at \(t=0\) the tangent vectors
\[
\begin{aligned}
&K_ZW_0-W_0K_Z+\operatorname{diag}(0,-B)\\
&\quad=\begin{pmatrix}0&2Z^*\\2Z&-B\end{pmatrix}.
\end{aligned}
\]
Multiplied on the right by \(W_0^{-1}=W_0\), the sums of these vectors are the matrices \(\begin{pmatrix}A&-2Z^*\\2Z&B\end{pmatrix}\), and every skew-Hermitian matrix has this form. By (INT)1, \(\langle f^*\alpha(d,l),[\mathrm U(l)]\rangle=\pm1\).

Joining \(-I_{d-l}\) to \(I_{d-l}\) by a path of unitaries shows that \(f\) is homotopic to the block inclusion \(\iota_{l,d}\), so by Lemma 2.1(3) of [Rational cohomology of unitary groups](rational-cohomology-of-unitary-groups.md), \(f^*e_{a,d}=e_{a,l}\) for \(a\le l\) and \(0\) for \(a>l\). A product of fewer than \(l\) generators of \(H^*(\mathrm U(l))\) has degree less than \(l^2\), so \(f^*\rho\), which has degree \(l^2\), is \(0\). Hence
\[
\begin{aligned}
\pm1&=\langle f^*\alpha(d,l),[\mathrm U(l)]\rangle\\
&=c_{d,l}\,\langle e_{1,l}\cdots e_{l,l},[\mathrm U(l)]\rangle ,
\end{aligned}
\]
and \(c_{d,l}\ne0\). For \(l=d\) the complementary blocks are absent and the same argument applies. \(\square\)

## 4. The intersection number

Write \(e^{(i)}_a\) for the generator of \(H^*(D)\) pulled back from the \(i\)-th factor. By Lemma 3.1 of [Rational cohomology of unitary groups](rational-cohomology-of-unitary-groups.md),
\[
\begin{gathered}
F_j^*e_{a,d_j}=\sum_{i:\ k_i\ge a}b_{ij}\,e^{(i)}_a\\
(1\le a\le d_j).
\end{gathered}
\tag{4.1}
\]
In particular \(F_j^*\) maps a product of \(u\) generators to a combination of products of \(u\) generators.

**Lemma 4.1.** The class
\[
\Omega=\prod_{j=1}^nF_j^*\alpha(d_j,l_j)\in H^{\dim D}(D)
\]
satisfies \(\langle\Omega,[D]\rangle\ne0\).

*Proof.* By (2.2), \(\Omega\) has degree \(\sum_jl_j^2=\dim D\). A nonzero product of generators of top degree contains every one of the \(\sum_ik_i\) generators of \(H^*(D)\). By Lemma 3.1 and (4.1), expanding the product gives terms with at most \(\sum_jl_j=\sum_ik_i\) generators, with equality only for the product of the leading terms. So
\[
\begin{aligned}
\Omega&=\Bigl(\prod_jc_{d_j,l_j}\Bigr)\prod_j\prod_{a=1}^{l_j}F_j^*e_{a,d_j}\\
&\quad+(\text{terms that vanish}\\
&\qquad\text{in top degree}).
\end{aligned}
\]
Group the factors of degree \(2a-1\), for \(1\le a\le k_1\); reordering factors of odd degree only changes the overall sign. Let \(t_a=\#\{i:k_i\ge a\}\). Since \(k_1\ge\cdots\ge k_r\), the rows with \(k_i\ge a\) are \(1,\ldots,t_a\), and the chosen columns with \(l_j\ge a\) are \(j_1,\ldots,j_{t_a}\). By (4.1), the factors of degree \(2a-1\) multiply to
\[
\begin{aligned}
&\prod_{t=1}^{t_a}\Bigl(\sum_{i=1}^{t_a}b_{i,j_t}e^{(i)}_a\Bigr)\\
&\quad=\det B[1,\ldots,t_a\mid j_1,\ldots,j_{t_a}]\\
&\qquad\cdot e^{(1)}_a\cdots e^{(t_a)}_a ,
\end{aligned}
\]
because the \(e^{(i)}_a\) anticommute and square to zero, so a product of linear combinations of them is the determinant of the coefficients times their product. Every generator \(e^{(i)}_a\) of \(H^*(D)\), which has \(a\le k_i\), that is \(i\le t_a\), occurs exactly once. So, up to sign, the coefficient of the top class \(\prod_{i,a}e^{(i)}_a\) in \(\Omega\) is
\[
\begin{aligned}
&\prod_{j=1}^nc_{d_j,l_j}\\
&\quad\cdot\prod_{a=1}^{k_1}\det B[1,\ldots,t_a\mid j_1,\ldots,j_{t_a}],
\end{aligned}
\]
a product of nonzero numbers by Lemma 3.1 and (2.1). The top class of the oriented manifold \(D\) evaluates nonzero on \([D]\). \(\square\)

*Proof of Theorem 1.1, conclusion.* Let \(N=\prod_j\mathrm U(d_j)\), \(R=\prod_jR(d_j,l_j)\), \(p=\prod_jp\) and \(F=(F_1,\ldots,F_n):D\to N\). By (2.2),
\[
\begin{aligned}
\dim D+\dim R&=\sum_ik_i^2+\sum_j(d_j^2-l_j^2)\\
&=\sum_jd_j^2=\dim N .
\end{aligned}
\] By (INT)2, the Poincaré dual of \(p_*[R]\) is \(\pm\prod_j\operatorname{pr}_j^*\alpha(d_j,l_j)\), whose pullback by \(F\) is \(\pm\Omega\). By Lemma 4.1 and (INT)1, \(F(D)\) meets \(p(R)\): there are \(X\in D\) and \((W_j,E_j)\in R(d_j,l_j)\) with \(F_j(X)=W_j\) for all \(j\). Then \(F_j(X)\) fixes the \(l_j\)-dimensional space \(E_j\) pointwise, and (2.2) gives (1.1). \(\square\)

The minors in (2.1) may be even, so the argument needs rational rather than mod-two coefficients; this is where it differs from the single-variable case of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space).

## 5. Exercises

**5.1** (easy). Let \(B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\). Find columns as in Lemma 2.1, the target dimensions \(l_j\) when \(k_1=k_2=1\), and the coefficient of the top class in Lemma 4.1 up to the constants \(c_{d,l}\).

**5.2** (easy). Let \(r=n=1\), \(k_1=1\), \(\mathcal B_1=((1,1),(1,-1))\) and \(P=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). Show that \(\operatorname{diag}(X,X^{-1})P\) has no fixed vector for any \(X\in\mathrm U(1)\).

**5.3** (medium). Let \(r=2\), \(k_1=k_2=1\), \(n=1\), \(\mathcal B_1=((1,1),(2,1))\) and \(P_1=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). Show that every row of \(B\) is nonzero, that \(B\) has rank \(1\), and that no \(X\in D\) satisfies (1.1). Find \(X\) for which \(F_1(X)\) has a fixed vector.

**5.4** (medium). Let \(k_1=2\), \(k_2=1\), and let the matrix of signed counts be \(B=\begin{pmatrix}2&0\\1&3\end{pmatrix}\). Find the columns of Lemma 2.1, the numbers \(t_1,t_2\), and the product of minors in Lemma 4.1.

## 6. Solutions

**5.1.** \(j_1=1\) (since \(b_{11}=1\ne0\)) and \(j_2=2\) (since \(\det B=-2\ne0\)). With \(k_1=k_2=1\), \(l_1=l_2=1\). Here \(t_1=2\), and the product of minors is \(\det B[1,2\mid1,2]=-2\).

**5.2.** \(\operatorname{diag}(x,x^{-1})P=\begin{pmatrix}0&-x\\x^{-1}&0\end{pmatrix}\) for \(x\in\mathrm U(1)\). A fixed vector \((v_1,v_2)\) satisfies \(-xv_2=v_1\) and \(x^{-1}v_1=v_2\), so \(v_2=-v_2\) and \(v=0\). Here \(B=(0)\) has rank \(0<1\).

**5.3.** \(B=\begin{pmatrix}1\\1\end{pmatrix}\) has nonzero rows and rank \(1<2\), and \(d_1=2\). For \(X=(x_1,x_2)\in\mathrm U(1)^2\), \(F_1(X)=\operatorname{diag}(x_1,x_2)P_1=\begin{pmatrix}0&-x_1\\x_2&0\end{pmatrix}\). The bound (1.1) asks for \(\dim\ker(F_1(X)-I)\ge2\), that is \(F_1(X)=I\), which is impossible because the diagonal of \(F_1(X)\) is zero. A fixed vector \((v_1,v_2)\) satisfies \(v_1=-x_1v_2\) and \(v_2=x_2v_1=-x_1x_2v_2\), so it exists exactly when \(x_1x_2=-1\); for \(x_1=1\), \(x_2=-1\) the vector \((1,-1)\) is fixed.

**5.4.** \(j_1=1\) (\(b_{11}=2\)), and \(j_2=2\) (\(\det B=6\)). Then \(l_1=k_1=2\), \(l_2=k_2=1\). For \(a=1\), \(t_1=2\), and for \(a=2\), \(t_2=1\). The product of minors is \(\det B[1,2\mid1,2]\cdot\det B[1\mid1]\), that is, \(6\cdot2=12\).

## References

- [OpenAI-NS] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Section 2, Theorem 2. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026

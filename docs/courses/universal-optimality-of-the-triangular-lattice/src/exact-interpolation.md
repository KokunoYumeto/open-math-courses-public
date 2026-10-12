# Exact interpolation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The interpolation system of [Gaussian damping and Fourier pairs](gaussian-damping-and-fourier-pairs.md) asks for two coefficient lists such that the functions \(H_1,H_2\) built from them have the right values and first derivatives at all nodes. [The reference lists](the-reference-lists.md) are explicit finite lists that solve it approximately. This lesson proves that the system has an exact solution with the same extra entries, that this solution is unique, and that it differs from the reference lists by less than \(2\cdot10^{-8}\).

- The system is an equation \(\mathcal L a=\psi\) in a space of summable lists. The operator \(\mathcal L\) is cut into four blocks by the node \(168\) (Section 1).
- The block of the nodes up to \(168\) is a matrix with inverse of norm less than \(40\); this uses the computed bounds for the matrix \(\mathbf D\) (Lemma 2.2). The blocks that lead to the nodes beyond \(168\) are smaller than \(1.1\cdot10^{-14}\); this uses the tail bound (Lemma 2.3).
- Hence \(\mathcal L\) is invertible (Theorem 2.4), and for every \(k\ge2.36\) the system has exactly one solution with the prescribed extra entries (Theorem 3.1).
- The solution is within \(2\cdot10^{-8}\) of the reference lists. So the functions \(H_1,H_2\) of the exact solution touch \(T_k\) and \(0\) at every node (Corollary 3.2), and their coefficient lists are known up to a tiny error.

The lesson follows [OpenAI-T, Section 4]. What remains after it for the normalized statement are the two sign conditions between the nodes.

## 1. The system as an operator equation

Let \(\mathcal E\) be the space of the lists \(a=(c_n,d_n)_{n\in\mathcal N}\) of real numbers with \(\|a\|_1=\sum_n(|c_n|+|d_n|)<\infty\). These are the positive parts of coefficient lists. For a pair \((a_1,a_2)\) we use the norm \(\|a_1\|_1+\|a_2\|_1\). An absolutely convergent series of elements of \(\mathcal E\) converges entry by entry, and its sum is in \(\mathcal E\), with norm at most the sum of the norms; this is the exchange of the order of summation in a double series with nonnegative terms.

**Lemma 1.1.** Let \(A\) be a linear map of \(\mathcal E\), or of the space of pairs, into itself with \(\|Ax\|_1\le\alpha\|x\|_1\) for all \(x\), where \(\alpha<1\). Then \(I-A\) is bijective, and \(\|(I-A)^{-1}y\|_1\le\|y\|_1/(1-\alpha)\).

**Proof.** If \((I-A)x=0\), then \(\|x\|_1=\|Ax\|_1\le\alpha\|x\|_1\), so \(x=0\). For given \(y\) the series \(x=\sum_{j\ge0}A^jy\) converges absolutely, because \(\|A^jy\|_1\le\alpha^j\|y\|_1\). Its partial sums \(x_J\) satisfy \((I-A)x_J=y-A^{J+1}y\), and \(\|A(x-x_J)\|_1\le\alpha\|x-x_J\|_1\to0\). So \((I-A)x=y\), and \(\|x\|_1\le\|y\|_1/(1-\alpha)\). \(\blacksquare\)

The same holds for square matrices with the norm \(\|\cdot\|\) of the lesson on the reference lists.

Let \(S\) be the jet operator. For \(a\in\mathcal E\) we write \(Sa\) for its value on the list with positive part \(a\) and extra entries \(0\), and for \(e=(c_0,d_0,C)\in\mathbb R^3\) we write \(S_ee\) for its value on the list with positive part \(0\) and extra entries \(e\). By Proposition 4.1 of the lesson on Gaussian damping,
\[
\begin{gathered}
\|Sa\|_1\le4000\,\|a\|_1,\\
\|S_ee\|_1\le4000\,\|e\|_1 .
\end{gathered}
\]
Let \(\ell_1,\ell_2\) be two coefficient lists with positive parts \(a_1,a_2\) and extra entries \(e_1,e_2\), and \(H_1=p_{\ell_1}+K_{p_{\ell_2}}\), \(H_2=p_{\ell_2}+K_{p_{\ell_1}}\). Since \(S\ell_i=Sa_i+S_ee_i\), the interpolation system \(\mathcal JH_1=\mathcal JT_k\), \(\mathcal JH_2=0\) is
\[
\begin{gathered}
a_1-Sa_2=\mathcal JT_k+S_ee_2,\\
a_2-Sa_1=S_ee_1 .
\end{gathered}
\]
Define the operator \(\mathcal L\) on pairs by
\[
\mathcal L(a_1,a_2)=(a_1-Sa_2,\ a_2-Sa_1).
\]
So the system is \(\mathcal L(a_1,a_2)=\psi\) with \(\psi=(\mathcal JT_k+S_ee_2,\ S_ee_1)\).

The right side is a pair of summable lists. Indeed, by Exercise 6.4 of the lesson on the reference lists, the two entries of \(\mathcal JT_k\) at a node \(n\) have absolute values adding up to at most \(\tfrac{1+3.12/k}{1.75}e^{-k(n-1)}\). This decreases in \(k\). So for \(k\ge2.36\)
\[
\begin{gathered}
|(\mathcal JT_k)_{c,n}|+|(\mathcal JT_k)_{d,n}|\\
\le c_*\,e^{-2.36(n-1)},\\
c_*=\frac{1+3.12/2.36}{1.75}=\frac{548}{413}<1.327 .
\end{gathered}
\]

As in the lesson on the reference lists let \(\mathcal F\) be the set of the \(84\) nodes \(n\le168\), and let \(\mathcal T\) be the set of the nodes \(n>168\). A list \(a\in\mathcal E\) is the sum of its part \(a_{\mathcal F}\) at the nodes of \(\mathcal F\) and its part \(a_{\mathcal T}\) at the nodes of \(\mathcal T\). Accordingly \(\mathcal L\) has four blocks: \(\mathcal L_{\mathcal F\mathcal F}\) takes a pair supported on \(\mathcal F\) to the part on \(\mathcal F\) of its image, \(\mathcal L_{\mathcal T\mathcal F}\) takes it to the part on \(\mathcal T\), and \(\mathcal L_{\mathcal F\mathcal T}\), \(\mathcal L_{\mathcal T\mathcal T}\) do the same for a pair supported on \(\mathcal T\). The equation \(\mathcal La=\psi\) is the pair of equations
\[
\begin{gathered}
\mathcal L_{\mathcal F\mathcal F}a_{\mathcal F}+\mathcal L_{\mathcal F\mathcal T}a_{\mathcal T}=\psi_{\mathcal F},\\
\mathcal L_{\mathcal T\mathcal F}a_{\mathcal F}+\mathcal L_{\mathcal T\mathcal T}a_{\mathcal T}=\psi_{\mathcal T}.
\end{gathered}
\]

## 2. The four blocks

The block \(\mathcal L_{\mathcal F\mathcal F}\) acts on pairs of columns with \(168\) entries. Let \(S_{\mathcal F\mathcal F}\) be the square matrix of the first \(168\) columns of the matrix \(S_{\mathcal F}\) of the lesson on the reference lists. Then
\[
\begin{gathered}
\mathcal L_{\mathcal F\mathcal F}(x,y)\\
=(x-S_{\mathcal F\mathcal F}\,y,\ y-S_{\mathcal F\mathcal F}\,x).
\end{gathered}
\]
Let \(\mathcal L_{\mathbf D}\) be the same expression with the quadrature form \(\mathbf D\) in place of \(S_{\mathcal F\mathcal F}\).

**Lemma 2.1.** The matrices \(I-\mathbf D\) and \(I+\mathbf D\) are invertible. With \(R_+=(I-\mathbf D)^{-1}\) and \(R_-=(I+\mathbf D)^{-1}\),
\[
\|R_+\|+\|R_-\|<37 ,
\]
and \(\mathcal L_{\mathbf D}\) is invertible with
\[
\begin{gathered}
\mathcal L_{\mathbf D}^{-1}(u,v)=(x,y),\\
x=\tfrac12R_+(u+v)+\tfrac12R_-(u-v),\\
y=\tfrac12R_+(u+v)-\tfrac12R_-(u-v).
\end{gathered}
\]
In particular \(\|x\|_1+\|y\|_1<37\,(\|u\|_1+\|v\|_1)\).

**Proof.** By Corollary 4.2 of the lesson on the reference lists, \(\|\mathbf D^{512}\|<\eta<10^{-19}\). By Lemma 1.1 the matrix \(I-\mathbf D^{512}\) is invertible, and its inverse has norm at most \(1/(1-\eta)\). Since \((I-\mathbf D)V_+=I-\mathbf D^{512}\), the matrix \(V_+(I-\mathbf D^{512})^{-1}\) is a right inverse of the square matrix \(I-\mathbf D\), hence its inverse. In the same way \(R_-=V_-(I-\mathbf D^{512})^{-1}\). By Proposition 4.1 of that lesson,
\[
\begin{aligned}
\|R_+\|+\|R_-\|&\le\frac{\|V_+\|+\|V_-\|}{1-\eta}\\
&<\frac{36}{1-\eta}<37 .
\end{aligned}
\]
The equations \(x-\mathbf Dy=u\), \(y-\mathbf Dx=v\) are equivalent to their sum and difference,
\[
\begin{gathered}
(I-\mathbf D)(x+y)=u+v,\\
(I+\mathbf D)(x-y)=u-v,
\end{gathered}
\]
that is \(x+y=R_+(u+v)\) and \(x-y=R_-(u-v)\). This gives the formulas, and
\[
\begin{aligned}
&\|x\|_1+\|y\|_1\\
&\quad\le\|R_+(u+v)\|_1+\|R_-(u-v)\|_1\\
&\quad\le(\|R_+\|+\|R_-\|)(\|u\|_1+\|v\|_1).
\end{aligned}
\]
\(\blacksquare\)

**Lemma 2.2.** The block \(\mathcal L_{\mathcal F\mathcal F}\) is invertible, and
\[
\|\mathcal L_{\mathcal F\mathcal F}^{-1}(u,v)\|<40\,(\|u\|_1+\|v\|_1).
\]

**Proof.** By Lemma 1.1 of the lesson on the reference lists every entry of \(S_{\mathcal F\mathcal F}-\mathbf D\) is less than \(2\cdot10^{-31}\) in absolute value; a column has \(168\) entries, so \(\|S_{\mathcal F\mathcal F}-\mathbf D\|<10^{-28}\). The difference \(\mathcal L_{\mathcal F\mathcal F}-\mathcal L_{\mathbf D}\) takes \((x,y)\) to \((-(S_{\mathcal F\mathcal F}-\mathbf D)y,\ -(S_{\mathcal F\mathcal F}-\mathbf D)x)\), of norm at most \(10^{-28}(\|x\|_1+\|y\|_1)\). Write
\[
\mathcal L_{\mathcal F\mathcal F}=\mathcal L_{\mathbf D}\,\bigl(I+\mathcal L_{\mathbf D}^{-1}(\mathcal L_{\mathcal F\mathcal F}-\mathcal L_{\mathbf D})\bigr).
\]
By Lemma 2.1 the map \(\mathcal L_{\mathbf D}^{-1}(\mathcal L_{\mathcal F\mathcal F}-\mathcal L_{\mathbf D})\) has the bound \(\alpha=37\cdot10^{-28}\). By Lemma 1.1 the second factor is invertible with a bound \(1/(1-\alpha)\) for its inverse. So \(\mathcal L_{\mathcal F\mathcal F}\) is invertible, with the bound \(37/(1-\alpha)<40\). \(\blacksquare\)

Let
\[
\delta=1.1\cdot10^{-14}.
\]

**Lemma 2.3.** With the function \(U_r\) of the tail bound, \(U_{168}(1,0)<\delta\) and \(U_{168}(5,0.02)<8.25\cdot10^{-14}\). For pairs \(a\) supported on \(\mathcal F\) and pairs \(a'\) supported on \(\mathcal T\),
\[
\begin{gathered}
\|\mathcal L_{\mathcal T\mathcal F}\,a\|\le\delta\,\|a\|,\\
\|(\mathcal L_{\mathcal T\mathcal T}-I)\,a'\|\le\delta\,\|a'\|,\\
\|\mathcal L_{\mathcal F\mathcal T}\,a'\|\le4000\,\|a'\| .
\end{gathered}
\]

**Proof.** Recall from [The transformed function at distant nodes](the-transformed-function-at-distant-nodes.md), Theorem 3.2,
\[
\begin{aligned}
&U_r(w,c)=800\,(w+c)\,\frac{e^{-0.70r}}{1-e^{-0.70}}\\
&\quad+5.3\Bigl(\frac{2.54\,w}r+2c\Bigr)\frac{e^{-0.187r}}{1-e^{-0.187}}.
\end{aligned}
\]
For \(r=168\): \(e^{-117.6}<10^{-51}\) and \(1-e^{-0.70}>0.5\), so the first term is less than \(10^{-47}\) for \(w+c\le6\). Further \(e^{-31.416}<2.28\cdot10^{-14}\) and \(1-e^{-0.187}>0.17\), so the last fraction is less than \(1.342\cdot10^{-13}\). For \((w,c)=(1,0)\) the factor in front of it is \(5.3\cdot2.54/168<0.0802\), and the second term is less than \(1.08\cdot10^{-14}\). For \((w,c)=(5,0.02)\) the factor is \(5.3\,(12.7/168+0.04)<0.6127\), and the second term is less than \(8.23\cdot10^{-14}\).

Let \(a=(a_1,a_2)\) be a pair in \(\mathcal E\). The part on \(\mathcal T\) of \(\mathcal La\) is
\[
\bigl(a_{1,\mathcal T}-(Sa_2)_{\mathcal T},\ a_{2,\mathcal T}-(Sa_1)_{\mathcal T}\bigr).
\]
The nodes of \(\mathcal T\) are larger than \(168\). By Theorem 3.2 of the lesson on distant nodes, applied to the two lists with positive parts \(a_2\) and \(a_1\) and extra entries \(0\), and because \(U_r(w,0)\) is proportional to \(w\),
\[
\begin{gathered}
\|(Sa_2)_{\mathcal T}\|_1+\|(Sa_1)_{\mathcal T}\|_1\\
\le U_{168}(1,0)\,\|a\| .
\end{gathered}
\]
This gives the first two inequalities. The third follows from \(\|Sa\|_1\le4000\|a\|_1\). \(\blacksquare\)

The bound of Lemma 2.3 does not depend on where the nonzero entries of \(a\) are; this is why the tail bound was proved uniformly in the position of the nodes.

**Theorem 2.4.** The operator \(\mathcal L\) is a bijection of the space of pairs in \(\mathcal E\). For every right side \(\psi\) the solution of \(\mathcal La=\psi\) is given by
\[
\begin{aligned}
a_{\mathcal T}&=\mathcal Q^{-1}\bigl(\psi_{\mathcal T}-\mathcal L_{\mathcal T\mathcal F}\mathcal L_{\mathcal F\mathcal F}^{-1}\psi_{\mathcal F}\bigr),\\
a_{\mathcal F}&=\mathcal L_{\mathcal F\mathcal F}^{-1}\bigl(\psi_{\mathcal F}-\mathcal L_{\mathcal F\mathcal T}a_{\mathcal T}\bigr),
\end{aligned}
\]
where
\[
\mathcal Q=\mathcal L_{\mathcal T\mathcal T}-\mathcal L_{\mathcal T\mathcal F}\,\mathcal L_{\mathcal F\mathcal F}^{-1}\,\mathcal L_{\mathcal F\mathcal T}
\]
is an invertible operator on the pairs supported on \(\mathcal T\).

**Proof.** By Lemma 2.2 the first of the two block equations is equivalent to the formula for \(a_{\mathcal F}\). Inserting it into the second block equation gives
\[
\mathcal Q\,a_{\mathcal T}=\psi_{\mathcal T}-\mathcal L_{\mathcal T\mathcal F}\,\mathcal L_{\mathcal F\mathcal F}^{-1}\,\psi_{\mathcal F}.
\]
By Lemmas 2.2 and 2.3, \(\mathcal Q-I\) has the bound
\[
\begin{aligned}
\delta+\delta\cdot40\cdot4000&=160001\,\delta\\
&<1.77\cdot10^{-9}.
\end{aligned}
\]
By Lemma 1.1, \(\mathcal Q\) is invertible. So the two block equations have exactly one solution, given by the formulas. \(\blacksquare\)

The matrix \(\mathbf D\) has norm larger than \(1\), so \(\mathcal L\) cannot be inverted by the series of Lemma 1.1 directly. The proof inverts the finite block by the computed bounds and treats only the small tail blocks by a series.

## 3. The solution and the reference lists

**Theorem 3.1.** Let \(k\ge2.36\). There is exactly one pair of coefficient lists \(\ell_1,\ell_2\) with positive parts in \(\mathcal E\) and extra entries \(E_1q(k)\), \(E_2q(k)\) that solves the interpolation system. With the reference lists \(\ell_i^{\mathrm{ref}}=X_iq(k)\),
\[
\begin{gathered}
\|\ell_1-\ell_1^{\mathrm{ref}}\|_1+\|\ell_2-\ell_2^{\mathrm{ref}}\|_1\\
<2\cdot10^{-8},\\
\|\ell_1\|_1+\|\ell_2\|_1<5 .
\end{gathered}
\]
Here \(\|\ell\|_1\) is the sum of the absolute values of all entries of a list, the extra entries included.

**Proof.** Existence and uniqueness are Theorem 2.4 for the right side \(\psi=(\mathcal JT_k+S_ee_2,\ S_ee_1)\) with \(e_i=E_iq(k)\). Let \(a=(a_1,a_2)\) be the solution, \(a^{\mathrm{ref}}\) the pair of the positive parts of the reference lists, and
\[
r=\psi-\mathcal La^{\mathrm{ref}},\qquad u=a-a^{\mathrm{ref}},
\]
so that \(\mathcal Lu=r\). We bound \(r\) and then \(u\). By Corollary 4.2 of the lesson on the reference lists, \(\|\ell_1^{\mathrm{ref}}\|_1+\|\ell_2^{\mathrm{ref}}\|_1<4.8\), and the entries \(C\) of the two lists have absolute values adding up to less than \(0.02\).

*The part of \(r\) on \(\mathcal F\).* Since \(S\ell_2^{\mathrm{ref}}=Sa_2^{\mathrm{ref}}+S_ee_2\), the first component of \(r\) on \(\mathcal F\) is
\[
(\mathcal JT_k)_{\mathcal F}-a_1^{\mathrm{ref}}+S_{\mathcal F}\,\ell_2^{\mathrm{ref}} .
\]
By Lemma 3.1 of the lesson on the reference lists, multiplied by \(q(k)\), and with \(\gamma_i=g_iq(k)\),
\[
a_1^{\mathrm{ref}}=\widetilde S\,\ell_2^{\mathrm{ref}}+Yq(k)-\mathbf D^{512}\gamma_1 ,
\]
because \(\mathbf Da_2^{\mathrm{ref}}+\widetilde S_ee_2=\widetilde S\,\ell_2^{\mathrm{ref}}\). So the first component is
\[
\begin{aligned}
&\bigl((\mathcal JT_k)_{\mathcal F}-Yq(k)\bigr)\\
&\quad+(S_{\mathcal F}-\widetilde S)\,\ell_2^{\mathrm{ref}}+\mathbf D^{512}\gamma_1 .
\end{aligned}
\]
In the same way the second component is \((S_{\mathcal F}-\widetilde S)\,\ell_1^{\mathrm{ref}}+\mathbf D^{512}\gamma_2\). The three kinds of terms are the target jets that \(Y\) omits, the quadrature error, and the remainder of the finite geometric sums.

(i) \(Yq(k)\) agrees with \(\mathcal JT_k\) at the nodes \(1,3,4,7,9\) and is \(0\) at the other nodes of \(\mathcal F\), which are at least \(12\). So the first term has norm at most
\[
\begin{aligned}
c_*\sum_{n\ge12}e^{-2.36(n-1)}&=c_*\,\frac{e^{-25.96}}{1-e^{-2.36}}\\
&<8\cdot10^{-12},
\end{aligned}
\]
because \(e^{-25.96}<5.4\cdot10^{-12}\), \(1-e^{-2.36}>0.9\) and \(c_*<1.327\).

(ii) Every column of \(S_{\mathcal F}-\widetilde S\) has \(168\) entries of absolute value less than \(2\cdot10^{-31}\), so the two quadrature terms together have norm less than \(4\cdot10^{-29}\cdot4.8<2\cdot10^{-28}\).

(iii) By definition \(\gamma_1=Yq(k)+\widetilde S_ee_2\) and \(\gamma_2=\widetilde S_ee_1\). By the bound for \(\mathcal JT_k\) at the nodes \(1,3,4,7,9\),
\[
\begin{aligned}
\|Yq(k)\|_1\le{}&c_*\bigl(1+e^{-4.72}+e^{-7.08}\\
&+e^{-14.16}+e^{-18.88}\bigr)<1.35
\end{aligned}
\]
(Exercise 4.1). The matrix \(\widetilde S_e\) differs from the exact one by less than \(10^{-28}\) in norm, so \(\|\widetilde S_ee_i\|_1<4001\|e_i\|_1\), and \(\|e_1\|_1+\|e_2\|_1<4.8\). Hence \(\|\gamma_1\|_1+\|\gamma_2\|_1<20000\), and the two terms with \(\mathbf D^{512}\) have norm less than \(20000\,\eta<1.4\cdot10^{-15}\).

Together, \(\|r_{\mathcal F}\|<10^{-11}\).

*The part of \(r\) on \(\mathcal T\).* The positive parts of the reference lists vanish on \(\mathcal T\). So the part of \(r\) on \(\mathcal T\) is
\[
\bigl((\mathcal JT_k)_{\mathcal T}+(S\ell_2^{\mathrm{ref}})_{\mathcal T},\ (S\ell_1^{\mathrm{ref}})_{\mathcal T}\bigr).
\]
By Theorem 3.2 of the lesson on distant nodes, applied to the two reference lists together, the transformed terms have norm at most \(U_{168}(5,0.02)<8.25\cdot10^{-14}\). The target term has norm at most \(c_*e^{-2.36\cdot168}/(1-e^{-2.36})<10^{-170}\). So \(\|r_{\mathcal T}\|<8.3\cdot10^{-14}\).

*The correction.* The block equations for \(\mathcal Lu=r\) and Lemmas 2.2 and 2.3 give
\[
\begin{aligned}
\|u_{\mathcal F}\|&\le40\,\bigl(10^{-11}+4000\,\|u_{\mathcal T}\|\bigr),\\
\|u_{\mathcal T}\|&\le8.3\cdot10^{-14}+\delta\,(\|u_{\mathcal F}\|+\|u_{\mathcal T}\|).
\end{aligned}
\]
Inserting the first into the second,
\[
\begin{aligned}
&\bigl(1-160001\,\delta\bigr)\|u_{\mathcal T}\|\\
&\quad\le8.3\cdot10^{-14}+4.4\cdot10^{-24},
\end{aligned}
\]
so \(\|u_{\mathcal T}\|<8.31\cdot10^{-14}\). Then
\[
\begin{aligned}
\|u_{\mathcal F}\|&<40\,\bigl(10^{-11}+3.324\cdot10^{-10}\bigr)\\
&<1.37\cdot10^{-8}.
\end{aligned}
\]
The extra entries of \(\ell_i\) and \(\ell_i^{\mathrm{ref}}\) are equal. So the lists differ by \(\|u\|<2\cdot10^{-8}\) in total, and \(\|\ell_1\|_1+\|\ell_2\|_1<4.8+2\cdot10^{-8}<5\). \(\blacksquare\)

**Corollary 3.2.** Let \(k\ge2.36\), let \(\ell_1,\ell_2\) be the lists of Theorem 3.1, and
\[
\begin{gathered}
H_1=p_{\ell_1}+K_{p_{\ell_2}},\\
H_2=p_{\ell_2}+K_{p_{\ell_1}} .
\end{gathered}
\]
Then \(H_1\) and \(H_2\) are entire functions, real on the real axis, and for every node \(n\in\mathcal N\)
\[
\begin{gathered}
H_1(n)=T_k(n),\qquad H_1'(n)=T_k'(n),\\
H_2(n)=0,\qquad H_2'(n)=0 .
\end{gathered}
\]
The function \(f(x)=e^{-\pi hs}H_1(s)\), \(s=b|x|^2\), is an admissible radial function with \(\widehat f(x)=e^{-\pi hs}H_2(s)\). If moreover \(H_1(s)\le T_k(s)\) and \(H_2(s)\ge0\) for all \(s\ge0\), then the normalized statement \((\mathrm N_k)\) holds.

**Proof.** The system \(\mathcal JH_1=\mathcal JT_k\), \(\mathcal JH_2=0\) says that \(H_1\) and \(T_k\), and \(H_2\) and \(0\), have equal values and equal first derivatives at every node. The rest is Corollary 3.3 of the lesson on Gaussian damping. \(\blacksquare\)

So \(T_k-H_1\) and \(H_2\) have zeros of order at least two at every node, including the nodes that are not values of \(j^2+jl+l^2\) for integers \(j,l\), such as \(24\). The uniqueness in Theorem 3.1 concerns summable lists with the given extra entries and with the values and derivatives prescribed at all nodes of \(\mathcal N\).

## 4. Exercises

**4.1.** Check that \(c_*=548/413\), and that
\[
\begin{aligned}
&c_*\bigl(1+e^{-4.72}+e^{-7.08}\\
&\quad+e^{-14.16}+e^{-18.88}\bigr)<1.35 .
\end{aligned}
\]

**4.2.** In the proof of Lemma 2.1, why is a right inverse of the square matrix \(I-\mathbf D\) its inverse? Why can the same argument not be used for the operator \(\mathcal L\) on the infinite lists?

**4.3.** Show that the solution \(a\) of \(\mathcal La=\psi\) in Theorem 2.4 satisfies \(\|a\|\le41\,\|\psi_{\mathcal F}\|+160002\,\|\psi_{\mathcal T}\|\).

**4.4.** Suppose the reference lists had been computed with a matrix \(\mathbf D'\) in place of \(\mathbf D\) whose entries differ from those of \(\mathbf D\) by at most \(10^{-12}\). Which term in the bound for \(r_{\mathcal F}\) changes, and by about how much?

## 5. Solutions

**4.1.** \(1+3.12/2.36=5.48/2.36\), and \(5.48/(2.36\cdot1.75)=5.48/4.13\), which is \(548/413\), about \(1.3269\). The sum in brackets is less than \(1+0.009+0.001+10^{-6}\), so the product is less than \(1.327\cdot1.0101<1.341\).

**4.2.** For square matrices \(AB=I\) implies that \(A\) is surjective, hence injective, because the dimension is finite; then \(B\) is the inverse. For operators on an infinite-dimensional space a right inverse need not be a left inverse, which is why Theorem 2.4 proves injectivity and surjectivity through the block equations and Lemma 1.1.

**4.3.** By Lemma 1.1 the inverse of \(\mathcal Q\) has the bound \(1/(1-1.77\cdot10^{-9})\), and by Lemmas 2.2 and 2.3 the map \(\mathcal L_{\mathcal T\mathcal F}\mathcal L_{\mathcal F\mathcal F}^{-1}\) has the bound \(40\,\delta=4.4\cdot10^{-13}\). So
\[
\begin{gathered}
\|a_{\mathcal T}\|\le\bigl(1+2\cdot10^{-9}\bigr)\,\beta,\\
\beta=\|\psi_{\mathcal T}\|+4.4\cdot10^{-13}\,\|\psi_{\mathcal F}\|,
\end{gathered}
\]
and \(\|a_{\mathcal F}\|\le40\,\|\psi_{\mathcal F}\|+160000\,\|a_{\mathcal T}\|\). Adding, \(\|a\|\le40\,\|\psi_{\mathcal F}\|+160001\,\|a_{\mathcal T}\|\), which is at most \(41\,\|\psi_{\mathcal F}\|+160002\,\|\psi_{\mathcal T}\|\). The large factor for the part on \(\mathcal T\) comes from the crude bound \(4000\) for \(\mathcal L_{\mathcal F\mathcal T}\).

**4.4.** The term (ii): the reference lists would satisfy Lemma 3.1 of the lesson on the reference lists with \(\mathbf D'\), and \(S_{\mathcal F}-\widetilde S\) would be replaced by a matrix with entries up to about \(10^{-12}\), so the term would be of the order \(168\cdot10^{-12}\cdot4.8\), about \(10^{-9}\). Then \(\|r_{\mathcal F}\|\) would be about \(10^{-9}\) and the correction about \(40\cdot10^{-9}\). The theorem would still hold with a larger bound for the distance; the accuracy \(10^{-31}\) of the quadrature rule is far more than this lesson needs.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026

# The real place: integral formula and two bounds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lessons bounded the determinants \(\Delta_N\) from below, assuming that Catalan's constant is rational. This lesson and the next bound them from above, with no hypothesis at all. The entries of \(\Delta_N\) are double integrals, so the determinant is an integral over \(n\) points \(t_1,\dots,t_n\in(-1,1)\) and \(n\) points \(s_1,\dots,s_n\in(0,1)\) of a product of three determinants. Two of these are explicit: a Cauchy determinant and a Vandermonde determinant. The third mixes the two branches of a square root, and this lesson bounds it in two ways: by a bounded holomorphic interpolating function when the points are not too close to \(\pm1\) on average, and by Hadamard's inequality otherwise. The result reduces the upper bound for \(\log|\Delta_N|\) to the supremum of an explicit function of \(2n\) real variables, which the next lesson estimates.

We use Cauchy's integral formula, Cauchy's theorem and the maximum modulus principle from the core course [Complex Analysis (C50)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), and Fubini's theorem. The determinants and rows are those of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md). A basic reference is [OpenAI-Catalan].

## 1. Three determinant identities

For a list \(y=(y_1,\dots,y_n)\) write \(V(y)=\prod_{i<j}(y_j-y_i)\) and \(\mathcal V(y)=|V(y)|\). Then \(V(y)=\det[y_i^{\,r}]_{r,i}\), with \(0\le r<n\) and \(1\le i\le n\).

**Lemma 1.1** (Andréief). Let \(\mu\) be a measure, and \(f_0,\dots,f_{n-1}\), \(g_0,\dots,g_{n-1}\) functions with all products \(f_rg_k\) integrable. Then

\[
\int\!\!\cdots\!\!\int\det[f_r(y_i)]_{r,i}\,\det[g_k(y_i)]_{k,i}\,d\mu(y_1)\cdots d\mu(y_n)=n!\,\det\Bigl[\int f_rg_k\,d\mu\Bigr]_{r,k},
\]

whenever the left integrand is integrable.

**Proof.** Expand the first determinant as \(\sum_\sigma\operatorname{sgn}\sigma\prod_if_{\sigma(i)}(y_i)\). In the term of \(\sigma\), relabel the integration variables by \(y_i=y'_{\sigma(i)}\). The product becomes \(\prod_rf_r(y'_r)\), the second determinant becomes \(\operatorname{sgn}\sigma\cdot\det[g_k(y'_r)]_{k,r}\) (its columns are permuted), and the product measure is unchanged. So each of the \(n!\) terms equals \(\int\prod_rf_r(y_r)\det[g_k(y_r)]_{k,r}\,d\mu^n\). Expanding this determinant as \(\sum_\tau\operatorname{sgn}\tau\prod_rg_{\tau(r)}(y_r)\) and integrating each product gives \(\sum_\tau\operatorname{sgn}\tau\prod_r\int f_rg_{\tau(r)}\,d\mu=\det[\int f_rg_k\,d\mu]\). \(\square\)

**Lemma 1.2** (Cauchy's double alternant). For numbers with \(t_is_j\ne1\),

\[
\det\Bigl[\frac1{1-t_is_j}\Bigr]_{i,j}=\frac{V(t)\,V(s)}{\prod_{i,j}(1-t_is_j)}.
\]

**Proof.** Multiply row \(i\) by \(\prod_j(1-t_is_j)\). The resulting determinant \(\Phi\) is a polynomial, of degree at most \(n-1\) in each \(t_i\) and in each \(s_j\), and alternating in the \(t\)'s and in the \(s\)'s. It therefore vanishes when two \(t\)'s or two \(s\)'s coincide, so it is divisible by \(V(t)V(s)\), which has degree exactly \(n-1\) in each variable; the quotient is a constant \(\kappa\). Expanding \(1/(1-t_is_j)=\sum_k(t_is_j)^k\), Cauchy–Binet (Lemma 1.2 of [Denominators at the prime two](denominators-at-the-prime-two.md)) writes the determinant as \(\sum_{k_1<\dots<k_n}\det[t_i^{k_m}]\det[s_j^{k_m}]\), whose lowest homogeneous part is \(V(t)V(s)\); the product \(\prod(1-t_is_j)\) has lowest part \(1\). Hence \(\kappa=1\). \(\square\)

**Lemma 1.3** (Hadamard's inequality). For complex column vectors \(a_1,\dots,a_n\in\mathbb C^n\), \(|\det(a_1,\dots,a_n)|\le\prod_j\|a_j\|\).

**Proof.** If the columns are dependent, the determinant is \(0\). Otherwise Gram–Schmidt writes \(A=QR\) with \(Q\) unitary and \(R\) upper triangular with diagonal entries \(r_{jj}\), \(|r_{jj}|\) being the distance from \(a_j\) to the span of \(a_1,\dots,a_{j-1}\). So \(|\det A|=\prod|r_{jj}|\le\prod\|a_j\|\). \(\square\)

## 2. The determinant as an integral

On \((-1,1)\) let \(d\mu(t)=|t|\,dt/f(t)\), with \(f(t)=\sqrt{1-t^2}\), as in the rows lesson; its mass is \(2\). For \(0\le r,k<n\) put

\[
A_r(t)=P_r(t)-\frac32\,\mathbf 1_{\{t>0\}}\,\frac{f(t)}t\,D_r(t),\qquad\psi_k(s)=s^{b+k}(1-s)^q.
\]

Then \(M(P_r,\psi_k)-\frac32Z(D_r,\psi_k)=\int_{-1}^1\int_0^1A_r(t)\,\psi_k(s)\,(1-ts)^{-1}\,ds\,d\mu(t)\): on \((0,1)\) the measure \(\mu\) has density \(t/f\), and \(\frac{t}{f}\cdot\frac ftD_r=D_r\) turns the \(Z\) integral into this form. The function \(A_r\) is bounded (the limit at \(t=0\) exists, since \(D_r(t)/t\) is a polynomial), and \(\iint(1-|t|s)^{-1}\,ds\,d\mu(t)<\infty\) (Lemma 5.1 of the rows lesson). So every integral below converges absolutely.

**Proposition 2.1** (integral formula).

\[
\Delta_N=\frac1{(n!)^2}\int_{(-1,1)^n}\int_{(0,1)^n}\mathcal R\cdot\frac{V(t)\,V(s)^2}{\prod_{i,j}(1-t_is_j)}\prod_js_j^b(1-s_j)^q\prod_it_i^{C-1}(1-t_i)^h\;ds\,d\mu^n(t),
\]

where \(\mathcal R=\det[A_r(t_i)]_{r,i}\big/\prod_it_i^{C-1}(1-t_i)^h\).

**Proof.** The entry \((r,k)\) of \(\Delta_N\) is \(\int A_r\phi_k\,d\mu\) with \(\phi_k(t)=\int_0^1\psi_k(s)(1-ts)^{-1}\,ds\). Lemma 1.1 in \(t\) gives \(\Delta_N=\frac1{n!}\int\det[A_r(t_i)]\det[\phi_k(t_i)]\,d\mu^n(t)\). For fixed \(t\), \(\det[\phi_k(t_i)]_{i,k}=\det[\int_0^1(1-t_is)^{-1}\psi_k(s)\,ds]\), and Lemma 1.1 in \(s\) gives \(\frac1{n!}\int\det[(1-t_is_j)^{-1}]_{i,j}\det[\psi_k(s_j)]_{j,k}\,ds\). Lemma 1.2 evaluates the first factor, and \(\det[\psi_k(s_j)]=\prod_js_j^b(1-s_j)^q\,V(s)\). Fubini's theorem applies by the absolute convergence noted above. \(\square\)

**Two sheets.** Use the coordinate \(x_i=t_i/(1+f(t_i))\in(-1,1)\), so that \(t_i=2x_i/(1+x_i^2)\) and

\[
d\mu(t_i)=\frac{4|x_i|}{(1+x_i^2)^2}\,dx_i.
\]

By (3.1) of the rows lesson, with \(w=x\), \(R_r=(1-t)^ht^{C-1}x^{r-g}\) and \(R_r^*=(1-t)^ht^{C-1}x^{g-r}\). On \(t<0\) the row is \(P_r=(R_r+R_r^*)/2\); on \(t>0\) it is \(P_r-\frac32\frac ftD_r=\frac{5R_r-R_r^*}4\), since \(\frac ftD_r=\frac{R^*_r-R_r}2\). Hence

\[
\mathcal R=\mathcal R_n(x):=\det\bigl[\xi_{\mathrm f}(x_i)\,x_i^{\,g-r}+\xi_{\mathrm n}(x_i)\,x_i^{\,r-g}\bigr]_{r,i},\qquad
(\xi_{\mathrm f},\xi_{\mathrm n})=\begin{cases}(\tfrac12,\tfrac12),&x<0,\\ (-\tfrac14,\tfrac54),&x>0.\end{cases}
\tag{2.1}
\]

The two terms are the evaluations on the "far" sheet \(1/x_i\) and the "near" sheet \(x_i\) of the Laurent monomials \(z^{r-g}\). Put

\[
D_*=n-1-2g=40N-1,
\]

so that \(0<D_*<n\).

## 3. A bounded interpolating function

**Lemma 3.1.** Let \(x_1,\dots,x_n\) be distinct nonzero real numbers in \((-1,1)\) with

\[
\sum_{i=1}^n\frac{1-x_i^2}{1+x_i^2}\le D_*.
\tag{3.1}
\]

There is a function \(h_*\), holomorphic on a neighbourhood of the closed unit disk, with

\[
h_*(x_i)=c_i\,x_i^{D_*},\quad c_i=\begin{cases}1,&x_i<0,\\-5,&x_i>0,\end{cases}\qquad\sup_{|z|\le1}|h_*(z)|\le K_0n,\quad K_0=10e^{12}.
\]

The neighbourhood may depend on the points; the bound does not.

**Proof.** Put \(B(z)=\prod_i\frac{z-x_i}{1-x_iz}\) and \(F(z)=z^{D_*}/B(z)\). On the unit circle \(|B|=1\).

*\(F\) on the imaginary axis.* For one factor and \(u>0\), \(\log\bigl|\frac{iu-x}{1-ixu}\bigr|=\frac12\log\frac{u^2+x^2}{1+x^2u^2}\), whose derivative with respect to \(\log u\) is

\[
\frac{(1-x^4)u^2}{(u^2+x^2)(1+x^2u^2)}=\frac{1-x^4}{1+x^4+x^2(u^2+u^{-2})}\le\frac{1-x^2}{1+x^2},
\]

using \(u^2+u^{-2}\ge2\). The logarithm vanishes at \(u=1\), so for \(0<u\le1\) integration gives \(|B(iu)|\ge u^{\sum_i(1-x_i^2)/(1+x_i^2)}\ge u^{D_*}\), by (3.1). For \(1\le u\le1+2/n\) each factor has modulus at least \(1\), since \((u^2+x^2)-(1+x^2u^2)=(u^2-1)(1-x^2)\ge0\). As \(B\) has real coefficients, the same holds at \(-iu\). Hence

\[
|F(iu)|\le e^2\qquad(|u|\le1+2/n),
\tag{3.2}
\]

using \(F(0)=0\), \(u^{D_*}/|B(iu)|\le1\) for \(|u|\le1\), and \((1+2/n)^{D_*}\le e^2\).

*The glued function.* Let \(\Gamma\) be the segment from \(-i(1+2/n)\) to \(i(1+2/n)\), oriented upwards, and \(\mathcal C(z)=\frac1{2\pi i}\int_\Gamma\frac{6F(w)}{w-z}\,dw\) for \(z\notin\Gamma\). Define

\[
h_*(z)=c_-z^{D_*}-B(z)\mathcal C(z)\ \ (\operatorname{Re}z<0),\qquad h_*(z)=c_+z^{D_*}-B(z)\mathcal C(z)\ \ (\operatorname{Re}z>0),
\]

with \(c_-=1\), \(c_+=-5\). The density \(F\) is holomorphic near every point of \(\Gamma\): its poles are the nonzero real numbers \(x_i\). Moving a short piece of \(\Gamma\) to the left changes \(\mathcal C\) by the integral over a closed positively oriented curve around \(z\), so by Cauchy's integral formula the continuation of \(\mathcal C\) from the left minus the continuation from the right equals \(6F\) near the segment. The two definitions of \(h_*\) therefore differ across \(\Gamma\) by \((c_--c_+)z^{D_*}-6B(z)F(z)=6z^{D_*}-6z^{D_*}=0\), and \(h_*\) extends holomorphically across the interior of \(\Gamma\), including its two crossings of the unit circle at \(\pm i\). The poles \(1/x_i\) of \(B\) and the endpoints of \(\Gamma\) lie outside the closed unit disk, so \(h_*\) is holomorphic on a neighbourhood of the closed disk. At \(x_i\), \(B(x_i)=0\) and \(\mathcal C\) is regular, so \(h_*(x_i)=c_\pm x_i^{D_*}\) with the sign of \(x_i\).

*The bound.* Near \(\pm i\), in the disks of radius \(\frac14\), we have \(|w|,|w-x_i|,|1-x_iw|\ge\frac34\), so \(F\) has no zeros or poles there and

\[
\Bigl|\frac{F'(w)}{F(w)}\Bigr|=\Bigl|\frac{D_*}w-\sum_i\Bigl(\frac1{w-x_i}+\frac{x_i}{1-x_iw}\Bigr)\Bigr|\le\frac43D_*+\frac83n<4n.
\]

As \(|F(\pm i)|=1\), integrating along segments gives \(|F(w)|\le e^{12}\) when \(|w\mp i|\le3/n\).

Let \(|z|=1\). If \(|\operatorname{Re}z|\ge1/(10n)\), then \(z\) has distance at least \(1/(10n)\) from \(\Gamma\), whose length is at most \(3\); by (3.2), \(|\mathcal C(z)|\le\frac{6}{2\pi}\cdot e^2\cdot3\cdot10n\le30e^2n\). If \(0<|\operatorname{Re}z|<1/(10n)\), then \(z\) is near \(i\) or \(-i\); say near \(i\). Replace the part of \(\Gamma\) from \(i(1-1/n)\) to \(i(1+2/n)\) by the other three sides of the rectangle with vertical side at real part \(-\operatorname{sgn}(\operatorname{Re}z)/n\). The swept rectangle lies in the half-plane not containing \(z\), inside the disk of radius \(\frac14\) about \(i\), and contains neither \(z\) nor a pole of \(F\), so by Cauchy's theorem \(\mathcal C(z)\) is unchanged. The new sides are within \(3/n\) of \(i\), where \(|F|\le e^{12}\), and the new contour has length at most \(3\) and distance at least \(1/(2n)\) from \(z\): the vertical side is at horizontal distance at least \(1/n\), the outer horizontal side at vertical distance at least \(2/n\), and the inner horizontal side and the rest of the segment at vertical distance at least \(\frac1n-\bigl(1-\sqrt{1-(10n)^{-2}}\bigr)>\frac1{2n}\). So \(|\mathcal C(z)|\le\frac6{2\pi}e^{12}\cdot3\cdot2n\le6e^{12}n\). The same works near \(-i\). In all cases \(|h_*(z)|\le5+6e^{12}n\le K_0n\) on the circle (at \(\pm i\) by continuity), and the maximum modulus principle gives the bound in the disk. \(\square\)

## 4. Evaluation in a finite-dimensional Hilbert space

**Proposition 4.1** (interpolation estimate). Under (3.1),

\[
|\mathcal R_n(x)|\le(1+K_0n)^n\,\mathcal V(1/x)\prod_i|x_i|^g,
\]

where \(1/x=(1/x_1,\dots,1/x_n)\).

**Proof.** Factor the far-sheet weight out of each column: with \(c_i=\xi_{\mathrm n}(x_i)/\xi_{\mathrm f}(x_i)\), which is \(1\) for \(x_i<0\) and \(-5\) for \(x_i>0\),

\[
\xi_{\mathrm f}x^{g-r}+\xi_{\mathrm n}x^{r-g}=\xi_{\mathrm f}\,x^{g-(n-1)}\bigl(x^{n-1-r}+c\,x^{D_*}x^r\bigr).
\]

So \(\mathcal R_n(x)=\prod_i\xi_{\mathrm f}(x_i)x_i^{g-(n-1)}\cdot\det\bigl[x_i^{n-1-r}+h_*(x_i)x_i^r\bigr]\), with \(h_*\) from Lemma 3.1.

Let \(H^2\) be the space of power series \(u=\sum_{m\ge0}u_mz^m\) with \(\sum|u_m|^2<\infty\), with inner product \(\langle u,v\rangle=\sum u_m\bar v_m\). For \(u\) holomorphic on a neighbourhood of the closed disk, \(\|u\|^2=\frac1{2\pi}\int_0^{2\pi}|u(e^{i\theta})|^2d\theta\) by Parseval's identity. For real \(y\) with \(|y|<1\), the function \(k_y(z)=1/(1-yz)=\sum y^mz^m\) satisfies \(\langle u,k_y\rangle=u(y)\). Multiplication by \(h_*\) has operator norm at most \(\sup_{|z|\le1}|h_*|\), by the boundary formula.

Let \(Q(z)=\prod_i(1-x_iz)\) and \(\mathcal H_Q=\{v/Q:\ v\text{ a polynomial of degree}<n\}\), an \(n\)-dimensional subspace of \(H^2\) (the zeros \(1/x_i\) of \(Q\) lie outside the closed disk). It contains the \(n\) functions \(k_{x_i}\), which are linearly independent because their poles are distinct; so they form a basis. Let \(\Pi_Q\) be the orthogonal projection onto \(\mathcal H_Q\). Then \((\Pi_Qu)(x_i)=\langle\Pi_Qu,k_{x_i}\rangle=\langle u,k_{x_i}\rangle=u(x_i)\).

Define \(R(v/Q)=\tilde v/Q\) with \(\tilde v(z)=z^{n-1}v(1/z)\). It is a linear involution of \(\mathcal H_Q\) and an isometry, since \(|\tilde v(e^{i\theta})|=|v(e^{-i\theta})|\) and \(|Q(e^{i\theta})|=|Q(e^{-i\theta})|\) (real coefficients). Put \(J=\Pi_QM_{h_*}\) on \(\mathcal H_Q\) and \(L=I+JR\); then \(\|L\|\le1+K_0n\). Let \(\mathcal E:\mathcal H_Q\to\mathbb C^n\) send \(v/Q\) to \((v(x_i))_i\); note \(\mathcal E(u)_i=Q(x_i)u(x_i)\). Since \(LR=R+J\) and projection preserves values at the \(x_i\),

\[
\mathcal E(LR(v/Q))=\bigl(\tilde v(x_i)+h_*(x_i)v(x_i)\bigr)_i.
\]

In the basis \(z^r/Q\) (\(0\le r<n\)) of \(\mathcal H_Q\), \(\mathcal E\) has the Vandermonde matrix \([x_i^r]\), \(R\) is a permutation of the basis, and \(\mathcal ELR(z^r/Q)=(x_i^{n-1-r}+h_*(x_i)x_i^r)_i\). Taking determinants, \(|\det[x_i^{n-1-r}+h_*(x_i)x_i^r]|=\mathcal V(x)\,|\det L|\), and \(|\det L|\le\|L\|^n\) by Lemma 1.3 applied to the matrix of \(L\) in an orthonormal basis. No bound for the inverse of the Vandermonde matrix enters. Finally \(|\xi_{\mathrm f}|\le1\) and \(\mathcal V(1/x)=\mathcal V(x)\prod_i|x_i|^{-(n-1)}\). \(\square\)

## 5. The Hadamard estimate

**Proposition 5.1.** For every list of distinct nonzero real numbers in \((-1,1)\),

\[
|\mathcal R_n(x)|\le\Bigl(\frac32\Bigr)^nn^{n/2}\,2^{-\binom n2}\prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.
\]

**Proof.** Expand \(\mathcal R_n\) by choosing one of the two sheets in each column. For a choice \(z_i\in\{x_i,1/x_i\}\), the determinant \(\det[z_i^{\,r-g}]\) has absolute value \(\mathcal V(z)\prod_i|z_i|^{-g}\). Write \(z_i=\tan\phi_i\) with \(|\phi_i|<\pi/2\). Then \(z_j-z_i=\sin(\phi_j-\phi_i)/(\cos\phi_i\cos\phi_j)\), so

\[
\mathcal V(z)=\prod_i(1+z_i^2)^{(n-1)/2}\prod_{i<j}|\sin(\phi_j-\phi_i)|=\prod_i(1+z_i^2)^{(n-1)/2}\,2^{-\binom n2}\,\bigl|V(e^{2i\phi_1},\dots,e^{2i\phi_n})\bigr|,
\]

and Lemma 1.3 bounds the last Vandermonde by \(n^{n/2}\), its columns having norm \(\sqrt n\). The ratio of the remaining weight on the far sheet to that on the near sheet is \(|x|^{g}(1+x^{-2})^{(n-1)/2}\big/\bigl(|x|^{-g}(1+x^2)^{(n-1)/2}\bigr)=|x|^{-D_*}\ge1\), so every choice is bounded by the far-sheet weights. The coefficients satisfy \(\sum|\prod\xi|\le\prod_i(|\xi_{\mathrm f}(x_i)|+|\xi_{\mathrm n}(x_i)|)\le(3/2)^n\). \(\square\)

## 6. Reduction to a supremum

Put \(t_i=2x_i/(1+x_i^2)\) and

\[
\mathcal J_n(x,s)=\frac{\mathcal V(t)\,\mathcal V(s)^2}{\prod_{i,j}(1-t_is_j)}\prod_js_j^b(1-s_j)^q\prod_i|t_i|^{C-1}(1-t_i)^h,
\]

\[
\mathcal I_{2,n}=\mathcal J_n\,\mathcal V(1/x)\prod_i|x_i|^g,\qquad
\mathcal I_{1,n}=\mathcal J_n\,2^{-\binom n2}\prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.
\]

Let \(\Omega_2\) be the set of configurations with distinct nonzero \(x_i\) satisfying (3.1), and \(\Omega_1\) its complement among such configurations.

**Proposition 6.1.** With \(K_n=\max\{(1+K_0n)^n,(3/2)^nn^{n/2}\}\),

\[
|\Delta_N|\le\frac{2^nK_n}{(n!)^2}\max_{\kappa\in\{1,2\}}\ \sup_{(x,s)\in\Omega_\kappa}\mathcal I_{\kappa,n}(x,s),
\]

and consequently

\[
\frac{\log|\Delta_N|}{n^2}-\frac12\log2\le\max_{\kappa}\sup_{\Omega_\kappa}\Bigl(\frac{\log\mathcal I_{\kappa,n}}{n^2}-\frac12\log2\Bigr)+O\Bigl(\frac{\log(n+2)}n\Bigr).
\]

**Proof.** In Proposition 2.1 all denominators are positive. On \(\Omega_2\) use Proposition 4.1, on \(\Omega_1\) Proposition 5.1; both cases together cover the domain up to a set of measure zero (repeated or zero \(x_i\), and boundary points). The measure \(ds\,d\mu^n(t)\) has total mass \(2^n\). For the logarithmic form, \(\log(2^nK_n)=O(n\log n)\) and \(-2\log n!\le0\). \(\square\)

The index \(\kappa\) is the exponent of the \(x\)-Vandermonde after substituting \(t=2x/(1+x^2)\): \(\mathcal V(t)\) contributes one factor \(\mathcal V(x)\), and in case \(\kappa=2\) the factor \(\mathcal V(1/x)\) contributes another.

## 7. Exercises

**Exercise 7.1 (easy).** Verify Lemma 1.2 directly for \(n=2\).

**Exercise 7.2 (easy).** Check the formula \(d\mu(t)=4|x|\,dx/(1+x^2)^2\) for \(t=2x/(1+x^2)\).

**Exercise 7.3 (medium).** Show that the right side of (3.1) cannot be dropped from Lemma 3.1: if all \(x_i\) are close to \(0\), the sum \(\sum(1-x_i^2)/(1+x_i^2)\) is close to \(n>D_*\), and explain where the proof fails.

**Exercise 7.4 (medium).** Prove \(|\det L|\le\|L\|^n\) for an operator \(L\) on an \(n\)-dimensional inner product space, using Lemma 1.3.

**Exercise 7.5 (medium).** Compute \(\int_{-1}^1d\mu=2\) in the coordinate \(x\).

## 8. Solutions

**7.1.** \(\frac1{(1-t_1s_1)(1-t_2s_2)}-\frac1{(1-t_1s_2)(1-t_2s_1)}\) has numerator \((1-t_1s_2)(1-t_2s_1)-(1-t_1s_1)(1-t_2s_2)=t_1s_1+t_2s_2-t_1s_2-t_2s_1=(t_2-t_1)(s_2-s_1)\), and the denominator is \(\prod_{i,j}(1-t_is_j)\).

**7.2.** \(dt/dx=2(1-x^2)/(1+x^2)^2\), \(f=(1-x^2)/(1+x^2)\) and \(|t|=2|x|/(1+x^2)\), so \(|t|\,dt/f=4|x|\,dx/(1+x^2)^2\).

**7.3.** For \(x\) near \(0\), \((1-x^2)/(1+x^2)\) is near \(1\), so the sum is near \(n\). In the proof the lower bound \(|B(iu)|\ge u^{D_*}\) for \(u\le1\) then fails: \(F=z^{D_*}/B\) is no longer bounded on the imaginary axis near \(0\), and the Cauchy integral can be large. This is why the complementary case is handled by Proposition 5.1.

**7.4.** In an orthonormal basis the columns of the matrix of \(L\) are the images of the basis vectors, each of norm at most \(\|L\|\).

**7.5.** \(\int_{-1}^1\frac{4|x|}{(1+x^2)^2}dx=2\int_0^1\frac{4x}{(1+x^2)^2}dx=2\bigl[-\tfrac2{1+x^2}\bigr]_0^1=2\).

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf

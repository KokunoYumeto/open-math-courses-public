# Forms, flows and Moser's method

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson collects the calculus of one-forms and two-forms on open subsets of \(\mathbf R^N\) that the course needs, in the language of vectors and matrices: pullbacks, exterior derivatives of one-forms, closed and symplectic two-forms, the volume preserved by symplectic maps (Lemma 2.4), and Moser's method, which turns a compactly supported deformation of symplectic forms into a diffeomorphism (Theorem 2.8). Moser introduced the method for volume forms [Mo]. Solutions of differential equations and their smooth dependence on the initial data are taken from the programme lesson [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport#2-differential-equations-and-their-parameters), Theorem 2.1, and the inverse function theorem from Theorem 1.2 of the same lesson.

Throughout, \(U\subseteq\mathbf R^N\) is open, "smooth" means infinitely differentiable, and vectors are columns.

## 1. One-forms and two-forms

A *one-form* on \(U\) is a smooth map \(\alpha\) assigning to each \(x\in U\) a linear functional \(\alpha(x)\) on \(\mathbf R^N\); we write \(\alpha=\sum_i\alpha_i\,dx_i\) with smooth coefficients, so that \(\alpha(x)(X)=\sum_i\alpha_i(x)X_i\). The *differential* of a smooth function is \(d\varphi=\sum_i\partial_i\varphi\,dx_i\). A *two-form* \(\Omega\) assigns to each \(x\) a skew-symmetric bilinear form,
\[
\begin{aligned}
\Omega(x)(X,Y)&=X^{\mathsf T}\,\Omega(x)\,Y\\
&=\sum_{i,j}\Omega_{ij}(x)X_iY_j,
\end{aligned}
\]
where we use the same letter for the skew-symmetric matrix of smooth functions \((\Omega_{ij})\). For one-forms, \(\alpha\wedge\beta\) is the two-form \((X,Y)\mapsto\alpha(X)\beta(Y)-\alpha(Y)\beta(X)\); in particular \(dx_i\wedge dx_j\) has the matrix \(E_{ij}-E_{ji}\). The *exterior derivative* of a one-form is the two-form
\[
\begin{aligned}
d\alpha&=\sum_j d\alpha_j\wedge dx_j,\\
(d\alpha)_{ij}&=\partial_i\alpha_j-\partial_j\alpha_i.
\end{aligned}
\]
The symmetry of second derivatives gives \(d(d\varphi)=0\). A two-form is *closed* if
\[
\partial_i\Omega_{jk}+\partial_j\Omega_{ki}+\partial_k\Omega_{ij}=0\ \text{ for all }i,j,k;
\]
a direct computation, using again the symmetry of second derivatives, shows that every \(d\alpha\) is closed. The *interior product* of a vector field \(Y\) with \(\Omega\) is the one-form \(\iota_Y\Omega=\Omega(Y,\cdot\,)\), with components \((\iota_Y\Omega)_j=\sum_kY_k\Omega_{kj}\). A two-form is *nondegenerate* if the matrix \(\Omega(x)\) is invertible at every point, and *symplectic* if it is closed and nondegenerate. On \(\mathbf R^{2n}=\mathbf R^n_q\times\mathbf R^n_p\), the standard symplectic form \(\omega_0=\sum_jdq_j\wedge dp_j\) has the matrix \(J\) of [Polar bodies and the volume product](polar-bodies-and-the-volume-product.md).

**Pullbacks.** Let \(F:U\to U'\) be smooth, \(U'\subseteq\mathbf R^{N'}\) open. For a function, a one-form and a two-form on \(U'\) put
\[
\begin{gathered}
F^*\varphi=\varphi\circ F,\\
(F^*\alpha)(x)(X)=\alpha(F(x))(DF(x)X),\\
F^*\Omega(x)=DF(x)^{\mathsf T}\,\Omega(F(x))\,DF(x).
\end{gathered}
\]
By the chain rule \((G\circ F)^*=F^*G^*\), and \(F^*\) respects wedge products of one-forms. Thus a smooth map \(e\) is symplectic in the sense of the first lesson exactly when \(e^*\omega_0=\omega_0\).

**Lemma 2.1.** For smooth functions \(\varphi,\psi\), smooth maps \(F\) and one-forms \(\alpha\):

(a) \(d(\varphi\,d\psi)=d\varphi\wedge d\psi\);

(b) \(F^*(d\varphi)=d(F^*\varphi)\) and \(F^*(d\alpha)=d(F^*\alpha)\).

**Proof.** (a) The components of \(\varphi\,d\psi\) are \(\varphi\,\partial_j\psi\), and \(\partial_i(\varphi\partial_j\psi)-\partial_j(\varphi\partial_i\psi)\) equals \(\partial_i\varphi\,\partial_j\psi-\partial_j\varphi\,\partial_i\psi\), the second derivatives of \(\psi\) cancelling.

(b) The first identity is the chain rule. For the second, write \(\alpha=\sum_j\alpha_j\,dx_j\); then \(F^*\alpha=\sum_j(\alpha_j\circ F)\,d(x_j\circ F)\). By (a), the first identity, and the definition of \(d\alpha\),
\[
\begin{aligned}
d(F^*\alpha)&=\sum_jF^*(d\alpha_j)\wedge F^*(dx_j)\\
&=F^*\Bigl(\sum_jd\alpha_j\wedge dx_j\Bigr)\\
&=F^*(d\alpha).\qquad\square
\end{aligned}
\]

**Lemma 2.2.** Let \(F:U\to\mathbf R^N\) be smooth and injective with \(DF(x)\) invertible for every \(x\). Then \(F(U)\) is open and \(F\) is a diffeomorphism of \(U\) onto \(F(U)\).

**Proof.** By the inverse function theorem ([Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport#1-contraction-and-local-inversion), Theorem 1.2), every point of \(U\) has a neighbourhood that \(F\) maps diffeomorphically onto an open set. So \(F(U)\) is open, and the inverse of the injective map \(F\) agrees near each point with one of these local inverses, hence is smooth. \(\square\)

## 2. Volume

For a skew-symmetric \(2n\times2n\) matrix \(A\), put
\[
\operatorname{Pf}(A)=\frac1{2^nn!}\sum_{\sigma}\operatorname{sgn}\sigma\prod_{i=1}^nA_{\sigma(2i-1)\sigma(2i)},
\]
the sum over all permutations \(\sigma\) of \(\{1,\dots,2n\}\).

**Lemma 2.3.** \(\operatorname{Pf}(M^{\mathsf T}AM)=\det(M)\operatorname{Pf}(A)\) for every real \(2n\times2n\) matrix \(M\), and \(\operatorname{Pf}(J)=(-1)^{n(n-1)/2}\).

**Proof.** Expanding the entries \((M^{\mathsf T}AM)_{ab}=\sum_{k,l}M_{ka}A_{kl}M_{lb}\),
\[
\begin{aligned}
&2^nn!\operatorname{Pf}(M^{\mathsf T}AM)=\sum_{k_1,l_1,\dots,k_n,l_n}\prod_iA_{k_il_i}\\
&\quad\cdot\sum_\sigma\operatorname{sgn}(\sigma)\prod_iM_{k_i\sigma(2i-1)}M_{l_i\sigma(2i)}.
\end{aligned}
\]
The inner sum is the determinant of the matrix whose rows are the rows \(k_1,l_1,\dots,k_n,l_n\) of \(M\). It vanishes unless these indices form a permutation \(\tau\) of \(\{1,\dots,2n\}\), and then it equals \(\operatorname{sgn}(\tau)\det M\); the remaining sum over \(\tau\) is \(2^nn!\operatorname{Pf}(A)\). For \(J\), the only nonzero entries are \(J_{j,n+j}=1\) and \(J_{n+j,j}=-1\). Each of the \(2^nn!\) permutations that pair every \(j\) with \(n+j\) contributes the same term, the sign of the reordering \((1,n+1,2,n+2,\dots,n,2n)\), which is \((-1)^{n(n-1)/2}\). \(\square\)

**Lemma 2.4.** (a) If \(M\) is a \(2n\times2n\) matrix with \(M^{\mathsf T}JM=J\), then \(\det M=1\).

(b) Let \(e:U\to\mathbf R^{2n}\) be an injective smooth map on an open set \(U\subseteq\mathbf R^{2n}\) with \(e^*\omega_0=\omega_0\). Then \(e(U)\) is open and \(\operatorname{vol}(e(U))=\operatorname{vol}(U)\).

(c) \(\operatorname{vol}(B^{2n}(c))=c^n/n!\).

**Proof.** (a) Lemma 2.3 gives \(\operatorname{Pf}(J)=\det(M)\operatorname{Pf}(J)\), and \(\operatorname{Pf}(J)\ne0\).

(b) By (a), \(\det De=1\) everywhere, so Lemma 2.2 applies, and the change of variables formula (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 2, Theorem 263D](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm)) gives \(\operatorname{vol}(e(U))=\int_U|\det De|=\operatorname{vol}(U)\).

(c) The unit ball of \(\mathbf R^{2n}\) has volume \(\pi^n/n!\) ([Fremlin, *Measure Theory*, Volume 2, 252Q](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm)); the ball \(B^{2n}(c)\) has radius \(\sqrt{c/\pi}\). \(\square\)

**Rescalings.** For \(s>0\), the dilation \(D_s(z)=sz\) satisfies \(D_s^*\omega_0=s^2\omega_0\), the map \(L_s(q,p)=(q,p/s)\) satisfies \(L_s^*\omega_0=s^{-1}\omega_0\), and \(Q_s(q,p)=(q/s,p)\) satisfies \(Q_s^*\omega_0=s^{-1}\omega_0\). The dilation \(D_{\sqrt s}\) maps \(B^{2n}(c)\) onto \(B^{2n}(sc)\).

## 3. Lie derivatives and flows

For a vector field \(Y\) and a two-form \(\Omega\) on \(U\), define the *Lie derivative* \(L_Y\Omega\) by
\[
\begin{aligned}
(L_Y\Omega)_{ij}=\sum_k\bigl(&Y_k\,\partial_k\Omega_{ij}+\Omega_{kj}\,\partial_iY_k\\
&+\Omega_{ik}\,\partial_jY_k\bigr).
\end{aligned}
\]

**Lemma 2.5** (Cartan's formula for closed forms). If \(\Omega\) is closed, then \(L_Y\Omega=d(\iota_Y\Omega)\).

**Proof.** With \((\iota_Y\Omega)_j=\sum_kY_k\Omega_{kj}\),
\[
\begin{aligned}
&\partial_i(\iota_Y\Omega)_j-\partial_j(\iota_Y\Omega)_i\\
&=\sum_k\bigl(\Omega_{kj}\partial_iY_k-\Omega_{ki}\partial_jY_k\\
&\qquad+Y_k(\partial_i\Omega_{kj}-\partial_j\Omega_{ki})\bigr).
\end{aligned}
\]
Since \(\Omega\) is skew, \(-\Omega_{ki}=\Omega_{ik}\), and closedness with skew-symmetry gives \(\partial_i\Omega_{kj}-\partial_j\Omega_{ki}=\partial_i\Omega_{kj}+\partial_j\Omega_{ik}\), which is \(-\partial_k\Omega_{ji}=\partial_k\Omega_{ij}\). \(\square\)

**Lemma 2.6** (compactly supported flows). Let \(I\) be an open interval containing \([0,1]\), \(C\subset\mathbf R^N\) compact, and \(Y:I\times\mathbf R^N\to\mathbf R^N\) smooth with \(Y_s(x)=Y(s,x)=0\) for \(x\notin C\). There is a smooth map \((s,x)\mapsto\varphi_s(x)\) on \([0,1]\times\mathbf R^N\) with \(\varphi_0(x)=x\) and \(\partial_s\varphi_s(x)=Y_s(\varphi_s(x))\). Each \(\varphi_s\) is a diffeomorphism of \(\mathbf R^N\) that fixes every point outside \(C\) and maps \(C\) onto \(C\), and \(\partial_sD\varphi_s(x)=DY_s(\varphi_s(x))\,D\varphi_s(x)\).

**Proof.** By Theorem 2.1 of the programme lesson cited above, every initial value problem \(y'=Y(s,y)\), \(y(s_0)=y_0\), has a unique local solution, depending smoothly on \(s\), \(s_0\) and \(y_0\). If \(y_0\notin C\), the constant curve is a solution; so a solution that is outside \(C\) at one time is constant, and a solution that starts in \(C\) stays in \(C\). A maximal solution with values in the compact set \(C\), whose derivative is bounded by \(\max|Y|\) over \([0,1]\times C\), has a limit at each finite end of its interval and can be continued there; so every solution starting at time \(0\) exists on \([0,1]\). Define \(\varphi_s(x)\) as its value at time \(s\). Covering the compact set \([0,1]\times C\) by finitely many neighbourhoods on which the local solutions depend smoothly on the data, and writing \(\varphi_s\) as a composition of finitely many such local solution maps, shows that \((s,x)\mapsto\varphi_s(x)\) is smooth. Solving backwards from time \(s\) gives an inverse of \(\varphi_s\), smooth for the same reason, and the map \(\varphi_s\) is a bijection of \(C\) and the identity outside \(C\). Differentiating the equation \(\partial_s\varphi_s(x)=Y_s(\varphi_s(x))\) in \(x\), and exchanging the derivatives in \(s\) and \(x\), gives the last formula. \(\square\)

**Lemma 2.7.** Let \(V\subseteq\mathbf R^N\) be open, \(\Omega_s\) a family of two-forms on \(V\) that is smooth in \((s,x)\in I\times V\), and \(Y\), \(\varphi_s\) as in Lemma 2.6 with \(C\subset V\). Then each \(\varphi_s\) maps \(V\) onto itself, and
\[
\frac{d}{ds}\bigl(\varphi_s^*\Omega_s\bigr)=\varphi_s^*\bigl(\partial_s\Omega_s+L_{Y_s}\Omega_s\bigr).
\]

**Proof.** The first statement holds because \(\varphi_s\) fixes \(V\setminus C\) and maps \(C\) onto itself. Write \(\Phi=D\varphi_s(x)\) and \(y=\varphi_s(x)\). By the product rule and Lemma 2.6,
\[
\begin{aligned}
&\frac{d}{ds}\bigl(\Phi^{\mathsf T}\Omega_s(y)\Phi\bigr)\\
&\quad=\Phi^{\mathsf T}\Bigl(\partial_s\Omega_s+\sum_kY_k\partial_k\Omega_s\Bigr)(y)\,\Phi\\
&\qquad+\Phi^{\mathsf T}\bigl(DY_s^{\mathsf T}\Omega_s+\Omega_sDY_s\bigr)(y)\,\Phi.
\end{aligned}
\]
The \((i,j)\) entry of \(DY^{\mathsf T}\Omega+\Omega\,DY\) is \(\sum_k(\partial_iY_k\,\Omega_{kj}+\Omega_{ik}\,\partial_jY_k)\), so the bracket is \(\partial_s\Omega_s+L_{Y_s}\Omega_s\), evaluated at \(y\). \(\square\)

## 4. Moser's method

**Theorem 2.8** (Moser). Let \(V\subseteq\mathbf R^N\) be open and \(\Omega_s\), \(s\in I\), symplectic forms on \(V\), smooth in \((s,x)\), with \(\partial_s\Omega_s=d\gamma_s\) for one-forms \(\gamma_s\) on \(V\), smooth in \((s,x)\), that all vanish outside a fixed compact set \(C\subset V\). Then there is a diffeomorphism \(\varphi\) of \(V\) onto itself, equal to the identity outside \(C\), with \(\varphi^*\Omega_1=\Omega_0\).

**Proof.** Since \(\Omega_s(x)\) is invertible, the equation \(\iota_{Y_s}\Omega_s=-\gamma_s\), that is \(\Omega_s(x)^{\mathsf T}Y_s(x)=-\gamma_s(x)\) for the column of coefficients of \(\gamma_s\), has a unique solution \(Y_s(x)\), smooth in \((s,x)\) and zero outside \(C\). Extended by zero outside \(V\), it is smooth on \(I\times\mathbf R^N\), because every point outside \(V\) has a neighbourhood disjoint from the compact set \(C\). Let \(\varphi_s\) be its flow (Lemma 2.6). By Lemma 2.7, Lemma 2.5 (each \(\Omega_s\) is closed) and \(\partial_s\Omega_s=d\gamma_s\),
\[
\begin{aligned}
\frac d{ds}\bigl(\varphi_s^*\Omega_s\bigr)&=\varphi_s^*\bigl(d\gamma_s+d(\iota_{Y_s}\Omega_s)\bigr)\\
&=\varphi_s^*(d\gamma_s-d\gamma_s)=0.
\end{aligned}
\]
Hence \(\varphi_1^*\Omega_1=\varphi_0^*\Omega_0=\Omega_0\), and \(\varphi=\varphi_1\) has the required properties. \(\square\)

The common compact support of the forms \(\gamma_s\) is what makes the flow exist up to time \(1\); no compactness of \(V\) and no regularity of its boundary is needed.

## 5. Exercises

**2.1** (easy). Show that \(d\alpha\) is closed for every one-form \(\alpha\).

**2.2** (easy). Check the three rescaling identities, and show that \(D_{\sqrt s}\circ L\circ D_{\sqrt{1/s}}\) is symplectic for every linear symplectic map \(L\).

**2.3** (medium). On \(\mathbf R^2\), let \(\Omega_s=(1+s\,\partial_x\partial_y\beta)\,dx\wedge dy\) for a smooth compactly supported function \(\beta\) with \(|\partial_x\partial_y\beta|<\frac12\). Write \(\partial_s\Omega_s\) as \(d\gamma\) with \(\gamma\) compactly supported, and describe the vector field \(Y_s\) of the proof of Theorem 2.8.

**2.4** (easy). Show that \(\operatorname{Pf}(A)^2=\det A\) for \(2\times2\) and \(4\times4\) skew-symmetric matrices \(A\).

## 6. Solutions

**2.1.** 
\[
\begin{aligned}
&\partial_i(\partial_j\alpha_k-\partial_k\alpha_j)+\partial_j(\partial_k\alpha_i-\partial_i\alpha_k)\\
&\quad+\partial_k(\partial_i\alpha_j-\partial_j\alpha_i)=0,
\end{aligned}
\]
the six terms cancelling in pairs.

**2.2.** \(DD_s=sI\), so \(D_s^*\omega_0\) has the matrix \(s^2J\); \(DL_s=\operatorname{diag}(I,s^{-1}I)\) and \(DQ_s=\operatorname{diag}(s^{-1}I,I)\) give \(s^{-1}J\). The composition has the derivative \(L\) (the scalars cancel), and \(L^{\mathsf T}JL=J\).

**2.3.** \(\partial_s\Omega_s=\partial_x\partial_y\beta\,dx\wedge dy=d\gamma\) with \(\gamma=\partial_y\beta\,dy\), since \(d(\partial_y\beta\,dy)=\partial_x\partial_y\beta\,dx\wedge dy\); \(\gamma\) vanishes outside the support of \(\beta\). With \(f_s=1+s\,\partial_x\partial_y\beta>\frac12\), the condition \(\Omega_s(Y,\cdot)=-\gamma\) reads \(f_s(Y_1\,dy-Y_2\,dx)=-\partial_y\beta\,dy\), so \(Y_s=(-\partial_y\beta/f_s,\,0)\).

**2.4.** For \(n=1\), \(\operatorname{Pf}(A)=A_{12}\) and \(\det A=A_{12}^2\). For \(n=2\), \(\operatorname{Pf}(A)=A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}\), and expanding \(\det A\) gives its square.

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
- [Mo] J. Moser, *On the volume elements on a manifold*, Transactions of the American Mathematical Society 120 (1965), 286–294. https://doi.org/10.1090/S0002-9947-1965-0182927-5

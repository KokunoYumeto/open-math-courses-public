# An exterior conformal coordinate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Faber polynomials of [Faber polynomials and a positive kernel](faber-polynomials-and-a-positive-kernel.md) are defined through a conformal map \(h\) of \(\{|\lambda|>1\}\) onto the exterior of a smooth convex domain \(\Omega\). The estimates there need \(h\) on a slightly larger set \(\{|\lambda|>r_0\}\) with \(r_0<1\), and they need the fact that \(\lambda h'(\lambda)\) is an outward normal of \(\partial\Omega\) when \(|\lambda|=1\). This lesson constructs \(h\) (Theorem 3.7). The result is classical; the form used in the course is the one of OpenAI [OpenAI-DC, Appendix A]. The proof below extends the *inverse* of a Riemann map across the boundary first, with the reflection principle for harmonic functions, and obtains the continuity of the Riemann map on the closed disc as a consequence.

Smooth convex domains are defined in [Smooth convex neighbourhoods](smooth-convex-neighbourhoods.md): bounded convex domains that are star-shaped with analytic polar boundary about one of their points. Results of complex analysis are cited by number from Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). \(\mathbf D\) is the open unit disc and \(\mathbf T\) the unit circle.

Throughout, \(\Omega\) is a smooth convex domain, star-shaped with analytic polar boundary about \(z_*\in\Omega\), with polar function \(\rho\) holomorphic on the strip \(\{|\operatorname{Im}\theta|<\eta\}\).

## 1. The inverted exterior

Put
\[
U=\{0\}\cup\Bigl\{\frac1{z-z_*}:z\in\mathbf C\setminus\overline\Omega\Bigr\}.
\]

**Lemma 3.1.** \(U\) is star-shaped with analytic polar boundary about \(0\), with polar function \(\sigma(\varphi)=1/\rho(-\varphi)\). For \(w\ne0\) and \(z=z_*+1/w\),
\[
\begin{aligned}
w\in U&\iff z\notin\overline\Omega,\\
w\in\partial U&\iff z\in\partial\Omega,\\
w\notin\overline U&\iff z\in\Omega.
\end{aligned}
\]
In particular, \(U\) is bounded and simply connected.

*Proof.* Write \(w=se^{i\varphi}\) with \(s>0\). Then \(z-z_*=s^{-1}e^{-i\varphi}\): the point \(z\) has distance \(1/s\) from \(z_*\) and polar angle \(-\varphi\). By the polar description of \(\overline\Omega\) and \(\partial\Omega\), \(z\notin\overline\Omega\) if and only if \(1/s>\rho(-\varphi)\), that is \(s<\sigma(\varphi)\); likewise \(z\in\partial\Omega\) if and only if \(s=\sigma(\varphi)\), and \(z\in\Omega\setminus\{z_*\}\) if and only if \(s>\sigma(\varphi)\). The first statement gives \(U=\{se^{i\varphi}:0\le s<\sigma(\varphi)\}\), and the polar description of \(\overline U\) and \(\partial U\) gives the other two equivalences.

The function \(\rho\) is positive on \(\mathbf R\) and uniformly continuous on \([0,2\pi]\times[-\eta/2,\eta/2]\). By periodicity there is \(0<\eta_1\le\eta/2\) with \(|\rho(\theta)-\rho(\operatorname{Re}\theta)|<\frac12\min_{\mathbf R}\rho\) for \(|\operatorname{Im}\theta|<\eta_1\). So \(\rho\) has no zeros on that strip, and \(\sigma\) is holomorphic there. \(U\) is bounded because \(\sigma\le1/\min_{\mathbf R}\rho\). It is simply connected in the sense of Definition 4.3.1: for \(a\notin U\), the function \(1/(w-a)\) is holomorphic on the star-shaped set \(U\), so by Cauchy's theorem for star-like domains (Theorem 3.2.13) every cycle in \(U\) has winding number \(0\) about \(a\). \(\square\)

## 2. Boundary charts

In Sections 2 to 4, \(U\) is any bounded domain that is star-shaped with analytic polar boundary about \(0\), with polar function \(\sigma\) holomorphic on a strip \(\{|\operatorname{Im}\zeta|<\eta_1\}\); by Lemma 3.1, the inverted exterior is such a domain. The argument at the end of the proof of Lemma 3.1 shows that \(U\) is simply connected. Put \(\Gamma(\zeta)=\sigma(\zeta)e^{i\zeta}\) on the strip, so that \(\partial U=\Gamma(\mathbf R)\). As in the proof of Lemma 3.1, there is \(0<\eta_2\le\eta_1\) such that \(\operatorname{Re}\sigma>0\) on \(|\operatorname{Im}\zeta|<\eta_2\). On that strip the principal logarithm \(L=\operatorname{Log}\sigma\) is holomorphic, real on \(\mathbf R\) and \(2\pi\)-periodic, and \(\sigma=e^L\).

**Lemma 3.2** (boundary charts). For every real \(\varphi_0\) there is \(0<\varepsilon<\eta_2\) with the following properties, where \(B=\{|\zeta-\varphi_0|<\varepsilon\}\): \(\Gamma\) is injective on \(B\), \(\Gamma(B)\) is open, the inverse of \(\Gamma:B\to\Gamma(B)\) is holomorphic, and for \(\zeta\in B\)
\[
\begin{aligned}
\Gamma(\zeta)\in U&\iff\operatorname{Im}\zeta>0,\\
\Gamma(\zeta)\in\partial U&\iff\operatorname{Im}\zeta=0,\\
\Gamma(\zeta)\notin\overline U&\iff\operatorname{Im}\zeta<0.
\end{aligned}
\]

*Proof.* Since \(\Gamma'(\varphi_0)\ne0\), the inverse function theorem (Theorem 2.2.8) gives \(\varepsilon_1>0\) such that \(\Gamma\) is injective on \(|\zeta-\varphi_0|<\varepsilon_1\), with open image and holomorphic inverse; every smaller disc about \(\varphi_0\) keeps these properties, because the inverse is continuous.

Put \(T(\zeta)=L(\zeta)+i\zeta\), so that \(\Gamma=e^T\). For \(\zeta=y+it\) write \(T(\zeta)=X+iY\) with \(X,Y\) real. Then \(|\Gamma(\zeta)|=e^X\) and \(Y\) is an argument of \(\Gamma(\zeta)\). Since \(\sigma(Y)=e^{L(Y)}\), the polar description of \(U\) gives
\[
\begin{aligned}
\Gamma(\zeta)\in U&\iff X<L(Y),\\
\Gamma(\zeta)\in\partial U&\iff X=L(Y).
\end{aligned}
\]
Let \(N(y,t)=L(Y)-X\), a continuously differentiable function of \((y,t)\). At \(t=0\), \(T(y)=L(y)+iy\), so \(X=L(y)\), \(Y=y\) and \(N(y,0)=0\). Moreover \(\partial_tX+i\,\partial_tY=iT'(\zeta)\), and \(T'(y)=L'(y)+i\) with \(L'(y)\) real; so at \(t=0\), \(\partial_tX=-1\) and \(\partial_tY=L'(y)\), and
\[
\partial_tN(y,0)=L'(y)^2+1>0.
\]
By continuity there is \(0<\varepsilon<\min(\varepsilon_1,\eta_2)\) with \(\partial_tN>0\) on the square \(|y-\varphi_0|<\varepsilon\), \(|t|<\varepsilon\). For fixed \(y\), \(t\mapsto N(y,t)\) is then strictly increasing and vanishes at \(t=0\), so \(N>0\) for \(t>0\) and \(N<0\) for \(t<0\). The disc \(B\) of radius \(\varepsilon\) lies in this square. \(\square\)

## 3. The inverse Riemann map across the boundary

By the Riemann mapping theorem (Theorem 6.3.1) there is a unique biholomorphic map \(\phi:U\to\mathbf D\) with \(\phi(0)=0\) and \(\phi'(0)>0\). Let \(g=\phi^{-1}:\mathbf D\to U\).

**Lemma 3.3.** Let \(\varphi_0\), \(\varepsilon\) and \(B\) be as in Lemma 3.2, and \(V=\Gamma(B)\). There is a holomorphic \(\tilde\phi:V\to\mathbf C\) with \(\tilde\phi=\phi\) on \(V\cap U\), \(|\tilde\phi|=1\) on \(V\cap\partial U\), \(|\tilde\phi|>1\) on \(V\setminus\overline U\), and \(\tilde\phi'\ne0\) on \(V\cap\partial U\).

*Proof.* Write \(B^\pm=\{\zeta\in B:\pm\operatorname{Im}\zeta>0\}\) and \(I=B\cap\mathbf R\). By Lemma 3.2, \(\Gamma(B^+)\subseteq U\), so \(F=\phi\circ\Gamma\) is holomorphic on \(B^+\) with values in \(\mathbf D\). It has no zeros, because \(\phi\) vanishes only at \(0\) and \(\Gamma=e^T\) does not vanish. Since \(B^+\) is convex, Corollary 4.3.5 gives a holomorphic \(\Lambda\) on \(B^+\) with \(e^\Lambda=F\); the function \(u=\operatorname{Re}\Lambda=\log|F|\) is harmonic and negative on \(B^+\).

*(a) Boundary values.* Let \(0<r<1\). The set \(K_r=g(\{|w|\le r\})\) is a compact subset of \(U\), so it has a positive distance \(d_r\) from the closed set \(\mathbf C\setminus U\), which contains \(\Gamma(\mathbf R)=\partial U\). Let \(y_0\in I\) and choose \(t_0>0\) such that the square \(|y-y_0|\le t_0\), \(|t|\le t_0\) lies in \(B\) and \(|\Gamma(y+it)-\Gamma(y)|<d_r\) on it (uniform continuity). For \(0<t\le t_0\), \(\Gamma(y+it)\notin K_r\), so \(|F(y+it)|>r\). Hence \(u\), extended by \(0\) on \(I\), is continuous on \(B^+\cup I\).

*(b) Reflection.* By the reflection principle for harmonic functions (Theorem 7.3.3) there is a harmonic \(\tilde u\) on \(B\) with \(\tilde u=u\) on \(B^+\cup I\). It satisfies \(\tilde u(\bar\zeta)=-\tilde u(\zeta)\). Indeed, \(d(\zeta)=\tilde u(\zeta)+\tilde u(\bar\zeta)\) is harmonic on \(B\), vanishes on \(I\), and \(\partial_td=0\) on \(I\). By Proposition 7.1.2, \(d=\operatorname{Re}E\) for a holomorphic \(E\) on the disc \(B\), and \(E'=\partial_yd-i\,\partial_td\) vanishes on \(I\); by the identity theorem (Theorem 2.4.7) \(E'=0\) on \(B\), so \(d\) is constant, equal to its value \(0\) on \(I\).

*(c) The extension.* By Proposition 7.1.2 there is a holomorphic \(\tilde G\) on \(B\) with \(\operatorname{Re}\tilde G=\tilde u\). On \(B^+\), \(\operatorname{Re}(\tilde G-\Lambda)=0\); by the open mapping theorem (Theorem 5.5.1) \(\tilde G-\Lambda\) is constant there, say \(i\alpha\). The function \(\tilde F=e^{\tilde G-i\alpha}\) is holomorphic on \(B\), equals \(F\) on \(B^+\), and \(|\tilde F|=e^{\tilde u}\). So \(|\tilde F|=1\) on \(I\), and \(|\tilde F(\zeta)|=e^{-\tilde u(\bar\zeta)}>1\) on \(B^-\) by (b).

*(d) The derivative on \(I\).* Since \(\tilde F'=\tilde G'\tilde F\), it suffices to show \(\tilde G'(y_0)\ne0\) for \(y_0\in I\). The function \(\tilde G\) is not constant, because \(\tilde u\) vanishes on \(I\) and is negative on \(B^+\). Suppose \(\tilde G'(y_0)=0\). Then near \(y_0\)
\[
\tilde G(\zeta)=\tilde G(y_0)+a(\zeta-y_0)^k\bigl(1+v(\zeta)\bigr)
\]
with \(k\ge2\), \(a\ne0\), and \(v\) holomorphic with \(v(y_0)=0\). Here \(\operatorname{Re}\tilde G(y_0)=\tilde u(y_0)=0\). As \(\beta\) runs through \((0,\pi)\), \(k\beta\) runs through an interval of length \(k\pi\ge2\pi\), so there is \(\beta\in(0,\pi)\) with \(\omega=\operatorname{Re}(ae^{ik\beta})>0\). For small \(s>0\), \(|a||v|<\omega\) at \(y_0+se^{i\beta}\), and
\[
\begin{aligned}
\tilde u(y_0+se^{i\beta})&=s^k\operatorname{Re}\bigl(ae^{ik\beta}(1+v)\bigr)\\
&\ge s^k(\omega-|a||v|)>0,
\end{aligned}
\]
although \(y_0+se^{i\beta}\in B^+\), where \(\tilde u<0\). So \(\tilde G'(y_0)\ne0\).

*(e)* Put \(\tilde\phi=\tilde F\circ(\Gamma|_B)^{-1}\) on \(V\). By Lemma 3.2, \(V\cap U=\Gamma(B^+)\), \(V\cap\partial U=\Gamma(I)\) and \(V\setminus\overline U=\Gamma(B^-)\), which gives the three statements on \(\tilde\phi\) and its modulus. Differentiating \(\tilde\phi(\Gamma(\zeta))=\tilde F(\zeta)\) gives \(\tilde\phi'(\Gamma(\zeta))\,\Gamma'(\zeta)=\tilde F'(\zeta)\ne0\) for \(\zeta\in I\). \(\square\)

**Proposition 3.4.** \(\phi\) extends to a homeomorphism \(\bar\phi:\overline U\to\overline{\mathbf D}\) with \(\bar\phi(\partial U)=\mathbf T\). Every \(p\in\partial U\) has an open neighbourhood \(V_p\) with an injective holomorphic \(\phi_p:V_p\to\mathbf C\) such that \(\phi_p'\ne0\), \(W_p=\phi_p(V_p)\) is open, \(\phi_p=\bar\phi\) on \(V_p\cap\overline U\), and \(|\phi_p|\ge1\) on \(V_p\setminus U\).

*Proof.* Let \(p\in\partial U\), so \(p=\Gamma(\varphi_0)\) with \(\varphi_0\) real, and take \(\tilde\phi\) from Lemma 3.3. As \(\tilde\phi'(p)\ne0\), the inverse function theorem gives an open neighbourhood \(V_p\) of \(p\) on which \(\tilde\phi\) is injective with nonvanishing derivative and open image; let \(\phi_p\) be its restriction. By Lemma 3.3, \(|\phi_p|\ge1\) on \(V_p\setminus U\). Every neighbourhood of \(p\) meets \(U\), and \(\phi_p\) is continuous and equal to \(\phi\) on \(V_p\cap U\); so \(\phi_p(p)=\lim_{w\to p,\,w\in U}\phi(w)\). This limit does not depend on the chart. So \(\bar\phi=\phi\) on \(U\) and \(\bar\phi(p)=\lim_{w\to p,\,w\in U}\phi(w)\) on \(\partial U\) defines a function that agrees with \(\phi_p\) on \(V_p\cap\overline U\); it is continuous, and \(|\bar\phi|=1\) on \(\partial U\).

The image \(\bar\phi(\overline U)\) is compact and contains \(\mathbf D\), so it contains \(\overline{\mathbf D}\). As \(\bar\phi(U)=\mathbf D\) and \(|\bar\phi|=1\) on \(\partial U\), \(\bar\phi(\partial U)=\mathbf T\).

Let \(p_1,p_2\in\partial U\) with \(\bar\phi(p_1)=\bar\phi(p_2)=\zeta_0\), and let \(\psi_i:W_{p_i}\to V_{p_i}\) be the inverse of \(\phi_{p_i}\). The open set \(W_{p_1}\cap W_{p_2}\) contains \(\zeta_0\in\mathbf T\), so there are \(w_k\in W_{p_1}\cap W_{p_2}\cap\mathbf D\) with \(w_k\to\zeta_0\). Since \(|\phi_{p_i}(\psi_i(w_k))|=|w_k|<1\), the point \(\psi_i(w_k)\) lies in \(U\), and \(\phi(\psi_1(w_k))=w_k=\phi(\psi_2(w_k))\). As \(\phi\) is injective, \(\psi_1(w_k)=\psi_2(w_k)\), and letting \(k\to\infty\) gives \(p_1=\psi_1(\zeta_0)=\psi_2(\zeta_0)=p_2\).

So \(\bar\phi\) is a continuous bijection of the compact set \(\overline U\) onto \(\overline{\mathbf D}\), and its inverse is continuous. \(\square\)

## 4. The Riemann map on a larger disc

**Theorem 3.5.** There are \(R_0>1\) and an injective holomorphic function \(G\) on \(\{|w|<R_0\}\) with \(G=g\) on \(\mathbf D\), \(G'\ne0\) everywhere, \(G(\mathbf T)=\partial U\), \(G(w)\notin\overline U\) for \(1<|w|<R_0\), and \(G(w)=0\) only for \(w=0\).

*Proof.* Let \(\bar g=\bar\phi^{-1}:\overline{\mathbf D}\to\overline U\). For \(\zeta\in\mathbf T\) let \(p=\bar g(\zeta)\) and \(\psi_p:W_p\to V_p\) the inverse of \(\phi_p\). For \(w\in W_p\cap\mathbf D\), \(|\phi_p(\psi_p(w))|=|w|<1\), so \(\psi_p(w)\in U\) and \(\phi(\psi_p(w))=w\): thus \(\psi_p=g\) on \(W_p\cap\mathbf D\). Choose \(R_\zeta>0\) with \(\{|w-\zeta|<R_\zeta\}\subseteq W_p\), and write \(\psi_\zeta\) for \(\psi_p\) on this disc.

Finitely many discs \(Q_i=\{|w-\zeta_i|<R_i/3\}\), with \(R_i=R_{\zeta_i}\), cover \(\mathbf T\). If \(Q_i\cap Q_j\ne\varnothing\) and \(R_i\ge R_j\), then \(|\zeta_i-\zeta_j|<(R_i+R_j)/3\le2R_i/3\), so \(\zeta_j\) lies in the intersection of the discs of radii \(R_i\) and \(R_j\) about \(\zeta_i\) and \(\zeta_j\). That intersection is convex, hence connected, and it meets \(\mathbf D\) because it is a neighbourhood of \(\zeta_j\in\mathbf T\). There \(\psi_{\zeta_i}=g=\psi_{\zeta_j}\), so by the identity theorem \(\psi_{\zeta_i}=\psi_{\zeta_j}\) on the whole intersection, in particular on \(Q_i\cap Q_j\). Hence \(g\) and the \(\psi_{\zeta_i}\) define one holomorphic function \(G\) on the open set \(O=\mathbf D\cup\bigcup_iQ_i\supseteq\overline{\mathbf D}\). By continuity, \(G=\bar g\) on \(\overline{\mathbf D}\).

On \(\mathbf D\), \(\phi'(g(w))\,g'(w)=1\), and near \(\zeta\in\mathbf T\), \(G=\psi_\zeta\) is the inverse of a function with nonvanishing derivative; so \(G'\ne0\) on \(\overline{\mathbf D}\).

Choose \(\delta_0>0\) with \(\{|w|<1+\delta_0\}\subseteq O\). Suppose that for every \(k>1/\delta_0\) there are \(w_k\ne w_k'\) with \(|w_k|,|w_k'|<1+1/k\) and \(G(w_k)=G(w_k')\). Passing to subsequences, \(w_k\to w\) and \(w_k'\to w'\) with \(|w|,|w'|\le1\), and \(G(w)=G(w')\); as \(\bar g\) is injective, \(w=w'\). Since \(G'(w)\ne0\), the inverse function theorem gives a neighbourhood of \(w\) on which \(G\) is injective, and it contains \(w_k\) and \(w_k'\) for large \(k\), a contradiction. So \(G\) is injective on \(\{|w|<R'\}\) for some \(R'>1\). Since \(G'\) is continuous and nonzero on the compact set \(\overline{\mathbf D}\), there is \(R_0\in(1,R']\) with \(G'\ne0\) on \(\{|w|<R_0\}\).

Finally, \(G(\mathbf T)=\bar g(\mathbf T)=\partial U\) by Proposition 3.4; for \(1<|w|<R_0\), injectivity gives \(G(w)\notin G(\overline{\mathbf D})=\overline U\); and \(G(0)=g(0)=0\). \(\square\)

## 5. The exterior coordinate

**Lemma 3.6** (supporting lines). For every \(p\in\partial\Omega\) there is a unit vector \(\nu\) with \(\operatorname{Re}(\bar\nu(z-p))\le0\) for all \(z\in\overline\Omega\).

*Proof.* \(\overline\Omega\) is compact and convex. The points \(p_k=z_*+(1+1/k)(p-z_*)\) lie outside \(\overline\Omega\) by the polar description. Let \(w_k\) be the point of \(\overline\Omega\) nearest to \(p_k\), and \(e_k=p_k-w_k\ne0\). For \(z\in\overline\Omega\) and \(0<s\le1\), \(w_k+s(z-w_k)\in\overline\Omega\), so
\[
\begin{aligned}
0&\le|e_k-s(z-w_k)|^2-|e_k|^2\\
&=-2s\operatorname{Re}\bigl(\bar e_k(z-w_k)\bigr)+s^2|z-w_k|^2 .
\end{aligned}
\]
Dividing by \(s\) and letting \(s\to0\), \(\operatorname{Re}(\bar\nu_k(z-w_k))\le0\) for the unit vector \(\nu_k=e_k/|e_k|\). Moreover \(|w_k-p|\le|w_k-p_k|+|p_k-p|\), which is at most \(2|p_k-p|\) because \(p\in\overline\Omega\), and \(2|p_k-p|\to0\). A subsequence of \((\nu_k)\) converges to a unit vector \(\nu\), which has the stated property. \(\square\)

**Theorem 3.7** (exterior coordinate). Let \(\Omega\) be a smooth convex domain. There are \(0<r_0<1\), \(c>0\) and a holomorphic function \(\kappa\) on \(\{|u|<1/r_0\}\) such that \(h(\lambda)=c\lambda+\kappa(1/\lambda)\), defined for \(|\lambda|>r_0\), has the following properties.

1. \(h\) is injective, and \(h'(\lambda)\ne0\) for \(|\lambda|>r_0\).
2. \(h\) maps \(\{|\lambda|>1\}\) onto \(\mathbf C\setminus\overline\Omega\), \(\mathbf T\) onto \(\partial\Omega\), and \(\{r_0<|\lambda|<1\}\) into \(\Omega\).
3. For \(\lambda\in\mathbf T\) and \(z\in\overline\Omega\), \(q(\lambda)=\lambda h'(\lambda)\) is nonzero, and
\[
\operatorname{Re}\bigl(\overline{q(\lambda)}(h(\lambda)-z)\bigr)\ge0.
\]

*Proof.* Take \(G\) and \(R_0\) from Theorem 3.5 and put \(r_0=1/R_0\), \(c=1/G'(0)\) and
\[
h(\lambda)=z_*+\frac1{G(1/\lambda)}\qquad(|\lambda|>r_0).
\]
Here \(G(1/\lambda)\ne0\). Since \(G'(0)=g'(0)=1/\phi'(0)>0\), \(c>0\). Write \(G(u)=uG_1(u)\) with \(G_1\) holomorphic on \(\{|u|<R_0\}\); \(G_1\) has no zeros, as \(G\) vanishes only at \(0\), where \(G'(0)\ne0\). Then
\[
\kappa(u)=z_*+\frac1u\Bigl(\frac1{G_1(u)}-\frac1{G_1(0)}\Bigr)
\]
has a removable singularity at \(u=0\) (Theorem 5.2.2), and \(h(\lambda)=c\lambda+\kappa(1/\lambda)\).

(1) \(h\) is a composition of injective maps, and \(h'(\lambda)=G'(1/\lambda)\big/\bigl(\lambda G(1/\lambda)\bigr)^2\ne0\).

(2) For \(u=1/\lambda\): if \(|\lambda|>1\) then \(u\in\mathbf D\setminus\{0\}\), and \(G\) maps \(\mathbf D\setminus\{0\}\) onto \(U\setminus\{0\}\); by Lemma 3.1, \(z_*+1/w\) runs over \(\mathbf C\setminus\overline\Omega\) as \(w\) runs over \(U\setminus\{0\}\). In the same way \(G(\mathbf T)=\partial U\) gives \(h(\mathbf T)=\partial\Omega\), and \(G(u)\notin\overline U\) for \(1<|u|<R_0\) gives \(h(\lambda)\in\Omega\) for \(r_0<|\lambda|<1\).

(3) Let \(\lambda_0=e^{i\theta_0}\), \(p=h(\lambda_0)\), and \(\nu\) as in Lemma 3.6. By (1), \(q(\lambda_0)\ne0\). The function \(\theta\mapsto\operatorname{Re}(\bar\nu(h(e^{i\theta})-p))\) is at most \(0\), because \(h(e^{i\theta})\in\partial\Omega\), and vanishes at \(\theta_0\); its derivative \(\operatorname{Re}(\bar\nu\,iq(\lambda_0))\) at \(\theta_0\) vanishes. So \(\bar\nu q(\lambda_0)=t\) is real, and \(q(\lambda_0)=t\nu\). The function \(s\mapsto\operatorname{Re}(\bar\nu(h(s\lambda_0)-p))\) is at most \(0\) on \((r_0,1]\), by (2), and vanishes at \(s=1\); so its derivative at \(s=1\), which is \(\operatorname{Re}(\bar\nu\lambda_0h'(\lambda_0))=t\), is at least \(0\). As \(q(\lambda_0)\ne0\), \(t>0\), and for \(z\in\overline\Omega\) the number \(\operatorname{Re}(\overline{q(\lambda_0)}(p-z))\) equals \(t\operatorname{Re}(\bar\nu(p-z))\ge0\). \(\square\)

Geometrically, the radial derivative \(q(\lambda)\) and the angular derivative \(iq(\lambda)\) of \(h\) at \(\lambda\in\mathbf T\) are an outward normal and a tangent of \(\partial\Omega\) at \(h(\lambda)\), and (3) says that \(\overline\Omega\) lies on the inner side of the tangent line.

**Example (ellipses).** For \(0\le a<1\), \(h(\lambda)=\lambda+a/\lambda\) satisfies \(h(\lambda)-h(\mu)=(\lambda-\mu)(1-a/(\lambda\mu))\), so it is injective on \(\{|\lambda|>\sqrt a\}\). It maps \(\mathbf T\) onto the ellipse \(h(e^{i\theta})=(1+a)\cos\theta+i(1-a)\sin\theta\) with semi-axes \(1+a\) and \(1-a\), and \(q(e^{i\theta})=(1-a)\cos\theta+i(1+a)\sin\theta\) is a positive multiple of the gradient of \(x^2/(1+a)^2+y^2/(1-a)^2\) at that point (Exercise 3.2). For \(a=0\) the domain is the unit disc and \(h(\lambda)=\lambda\).

## 6. Exercises

**3.1** (easy). For the disc \(\Omega=\{|z-z_0|<R\}\) and \(z_*=z_0\), show that \(U=\{|w|<1/R\}\), \(g(w)=w/R\), and \(h(\lambda)=z_0+R\lambda\). Check property (3) of Theorem 3.7 directly.

**3.2** (easy). Let \(0<a<1\), \(h(\lambda)=\lambda+a/\lambda\), and \(\Omega\) the interior of the ellipse \(x^2/(1+a)^2+y^2/(1-a)^2=1\). Show that \(h\) maps \(\{|\lambda|>1\}\) onto \(\mathbf C\setminus\overline\Omega\) and \(\{\sqrt a<|\lambda|<1\}\) into \(\Omega\), and that \(q(e^{i\theta})\) is a positive multiple of the gradient of \(x^2/(1+a)^2+y^2/(1-a)^2\) at \(h(e^{i\theta})\).

**3.3** (medium). Show that \(h\) in Theorem 3.7 is unique: if \(h_1,h_2\) satisfy (1) and (2) with \(c_1,c_2>0\) (and possibly different \(r_0\)), then \(h_1=h_2\) on \(\{|\lambda|>1\}\).

**3.4** (medium). For \(h(\lambda)=\lambda+a/\lambda\) with \(0<a<1\), show that \(h\) is injective on \(\{|\lambda|>r\}\) if and only if \(r\ge\sqrt a\).

## 7. Solutions

**3.1.** For \(z=z_0+1/w\) with \(w\ne0\), \(z\notin\overline\Omega\) if and only if \(|w|<1/R\). The map \(w\mapsto Rw\) sends \(U\) onto \(\mathbf D\) with derivative \(R>0\) at \(0\), so \(\phi(w)=Rw\), \(g(w)=w/R\), \(G=g\) on \(\mathbf C\), and \(h(\lambda)=z_0+1/(1/(R\lambda))=z_0+R\lambda\). For \(\lambda\in\mathbf T\), \(q(\lambda)=R\lambda\), and for \(|z-z_0|\le R\)
\[
\begin{aligned}
&\operatorname{Re}\bigl(\overline{R\lambda}(z_0+R\lambda-z)\bigr)\\
&\quad=R^2-R\operatorname{Re}\bigl(\bar\lambda(z-z_0)\bigr)\\
&\quad\ge R^2-R|z-z_0|\ge0 .
\end{aligned}
\]

**3.2.** For \(|\lambda|=s\) and \(\lambda=se^{i\theta}\), \(h(\lambda)=(s+a/s)\cos\theta+i(s-a/s)\sin\theta\), a point of the ellipse with semi-axes \(s+a/s\) and \(s-a/s\). These ellipses all have foci \(\pm2\sqrt a\), they increase with \(s\) for \(s>\sqrt a\), the one for \(s=1\) is \(\partial\Omega\), and for \(s=\sqrt a\) the image is the segment \([-2\sqrt a,2\sqrt a]\subset\Omega\). So \(|\lambda|>1\) maps into \(\mathbf C\setminus\overline\Omega\) and \(\sqrt a\le|\lambda|\le1\) into \(\overline\Omega\), with \(\sqrt a<|\lambda|<1\) going into \(\Omega\). Every \(z\in\mathbf C\setminus\overline\Omega\) is attained: \(h(\lambda)=z\) is the quadratic \(\lambda^2-z\lambda+a=0\), whose roots have product \(a\), so one root \(\lambda\) has \(|\lambda|\ge\sqrt a\); it satisfies \(|\lambda|>1\), since otherwise \(z=h(\lambda)\in\overline\Omega\). The gradient at \(((1+a)\cos\theta,(1-a)\sin\theta)\) is
\[
\begin{aligned}
&2\Bigl(\frac{\cos\theta}{1+a},\frac{\sin\theta}{1-a}\Bigr)\\
&\quad=\frac2{1-a^2}\bigl((1-a)\cos\theta,(1+a)\sin\theta\bigr),
\end{aligned}
\]
and \(q(e^{i\theta})=e^{i\theta}-ae^{-i\theta}\), which is \((1-a)\cos\theta+i(1+a)\sin\theta\).

**3.3.** \(f=h_2^{-1}\circ h_1\) is a biholomorphic map of \(\{|\lambda|>1\}\) onto itself with \(f(\lambda)/\lambda\to c_1/c_2\) as \(\lambda\to\infty\). Then \(F(u)=1/f(1/u)\) maps \(\mathbf D\setminus\{0\}\) biholomorphically onto itself and is bounded, so by Theorem 5.2.2 it extends holomorphically to \(\mathbf D\) with \(F(0)=0\) and \(F'(0)=c_2/c_1>0\). The same construction for \(f^{-1}\) extends \(F^{-1}\), so the extension of \(F\) is a biholomorphic map of \(\mathbf D\). Schwarz's lemma (Lemma 3.5.1) applied to \(F\) and \(F^{-1}\) gives \(|F'(0)|\le1\) and \(1/|F'(0)|\le1\), so \(F\) is a rotation, and \(F'(0)>0\) gives \(F(u)=u\). So \(h_1=h_2\).

**3.4.** \(h(\lambda)=h(\mu)\) with \(\lambda\ne\mu\) holds exactly when \(\lambda\mu=a\). If \(|\lambda|,|\mu|>r\ge\sqrt a\), then \(|\lambda\mu|>a\). If \(r<\sqrt a\), choose \(s\) with \(r<s<\sqrt a\): the points \(s\) and \(a/s>\sqrt a\) are distinct, both have modulus larger than \(r\), and they have the same image.

## References

- [OpenAI-DC] OpenAI, *A direct proof of the complete Crouzeix inequality*, OpenAI Math Release preprint, 26 September 2026, Appendix A. https://github.com/openai/math/tree/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
- J. Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*, version 1.9, in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50).

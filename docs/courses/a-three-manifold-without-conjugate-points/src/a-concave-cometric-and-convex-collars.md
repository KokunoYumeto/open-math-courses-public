# A concave cometric and convex collars

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs the metric on the manifold \(M\) of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md). On the neck \([0,1]\times T\) it is
\[
g=dt^2+dx^{\mathsf T}P(t)^{-1}dx,
\]
where \(P(t)\) is a smooth path of positive definite \(2\times2\) matrices, the *cometric*, chosen concave and nearly constant, with a small shear in the middle that realizes the twisted gluing. Near each boundary torus the metric is a product of a flat circle and a convex warped surface, which continues into a flat torus with a hole. Outside the open neck every sectional curvature is nonpositive; on the neck the curvature is not controlled, and the next two lessons show that the concavity of \(P\) is enough to exclude conjugate points.

- The cutoff and the matrix path (Section 1).
- Bounds on the cometric (Section 2).
- Warped products and the ends of the neck (Section 3).
- Convex collars, flat cores and the metric on \(M\) (Section 4).

Matrix norms are Euclidean operator norms, \({}^{\mathsf T}\) denotes transpose, and for symmetric matrices \(R\preceq S\) means that \(S-R\) is positive semidefinite.

## 1. The cutoff and the matrix path

Define \(a\colon\mathbb R\to[0,1)\) by \(a(u)=\exp\bigl(-1/(\tfrac23-u)\bigr)\) for \(u<\tfrac23\) and \(a(u)=0\) for \(u\ge\tfrac23\), and its primitive \(A\) by
\[
A(u)=\int_0^ua(y)\,dy . \tag{1.1}
\]
The function \(a\) is smooth: every derivative of \(\exp(-1/w)\) is a polynomial in \(1/w\) times \(\exp(-1/w)\), which tends to \(0\) as \(w\to0^+\). For \(u<\frac23\),
\[
a'(u)=-\frac{a(u)}{(\frac23-u)^2}<0 . \tag{1.2}
\]
So \(a\) is nonincreasing, \(A\) is concave, and \(A\) is constant on \([\frac23,\infty)\). Fix once and for all a smooth nondecreasing function \(\chi\colon\mathbb R\to[0,1]\) equal to \(0\) on \((-\infty,\frac5{12}]\) and to \(1\) on \([\frac7{12},\infty)\).

For \(0<\delta\le\frac12\) put \(\epsilon=\delta^2\) and, for \(0\le t\le1\),
\[
\begin{aligned}
H(t)&=e_2+\epsilon\chi(t)e_1,\\
d_1(t)&=1+\delta A(t),\\
d_2(t)&=1+\delta A(1-t),\\
P(t)&=d_1(t)\,e_1e_1^{\mathsf T}\\
&\quad+d_2(t)\,H(t)H(t)^{\mathsf T} .
\end{aligned} \tag{1.3}
\]
Put \(Q=P^{-1}\), the matrix of the torus metric, and
\[
\begin{aligned}
\kappa&=\delta a(0)=\delta e^{-3/2}>0,\\
b&=1+\delta A(1) .
\end{aligned} \tag{1.4}
\]
Since \(A(1)=A(\frac23)\le\frac23e^{-3/2}<\frac16\), we have \(1\le d_i\le\frac{13}{12}\) on \([0,1]\).

The two *end frames* are the matrices with columns
\[
\begin{aligned}
T_1&=(e_1,\ e_2),\\
T_2&=(e_2+\epsilon e_1,\ e_1),
\end{aligned} \tag{1.5}
\]
those of (1.1) in [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md) with \(\epsilon=B_1/B_2\). A linear change of coordinates \(x=T_iy\) changes the cometric to \(T_i^{-1}PT_i^{-\mathsf T}\). The *inward coordinate* is \(\tau=t\) at the first end and \(\tau=1-t\) at the second.

**Lemma 1.1** (the ends of the path). For \(0\le\tau\le\frac14\), the cometric in the end frame \(T_i\) and inward coordinate \(\tau\) is
\[
P_i(\tau)=\begin{pmatrix}1+\delta A(\tau)&0\\0&b\end{pmatrix} . \tag{1.6}
\]
In particular \(P_i(0)e_1=e_1\) and \(P_i'(0)=\kappa\,e_1e_1^{\mathsf T}\), primes denoting derivatives in \(\tau\).

*Proof.* For \(t\in[0,\frac14]\), \(\chi(t)=0\), so \(H=e_2\); and \(1-t\ge\frac23\), so \(d_2=b\). Thus \(P=\operatorname{diag}(1+\delta A(t),b)\), and \(T_1\) is the identity. For \(t\in[\frac34,1]\), \(\chi(t)=1\), so \(H=e_2+\epsilon e_1\) is the first column of \(T_2\); \(t\ge\frac23\) gives \(d_1=b\), and \(d_2=1+\delta A(\tau)\). Hence \(P=T_2\operatorname{diag}(1+\delta A(\tau),b)T_2^{\mathsf T}\), which is (1.6) after the change of frame. Finally \(A(0)=0\) and \(A'=a\). \(\square\)

## 2. Bounds on the cometric

**Lemma 2.1** ([OpenAI-NC, Lemma 3.1]). There are \(\delta_0\in(0,\frac12]\) and \(C_0\ge18\), depending only on \(\chi\), such that for \(0<\delta\le\delta_0\) the following hold on \([0,1]\), in the original coordinates and in either end frame with its inward coordinate:
\[
\begin{aligned}
&\tfrac19\operatorname{Id}\preceq P\preceq18\operatorname{Id},\\
&\tfrac1{18}\operatorname{Id}\preceq Q\preceq9\operatorname{Id},\\
&\|P'\|\le C_0\delta,
\end{aligned} \tag{2.1}
\]
\[
\begin{aligned}
&-P''\succeq0,\\
&|P'p|^2\le C_0\delta\,p^{\mathsf T}(-P'')p
\end{aligned} \tag{2.2}
\]
for every \(p\in\mathbb R^2\).

*Proof.* *Size.* Let \(R=(e_1,H)\) be the matrix with columns \(e_1\) and \(H\). Then \(P=R\operatorname{diag}(d_1,d_2)R^{\mathsf T}\), and \(R\) and \(R^{-1}=(e_1,\ e_2-\epsilon\chi e_1)\) have squared norms at most their squared Frobenius norms \(2+\epsilon^2\chi^2\le3\). With \(1\le d_i\le2\) this gives \(\frac13\operatorname{Id}\preceq P\preceq6\operatorname{Id}\). The frames \(T_i\) and their inverses also have squared norms at most \(3\), which gives the bounds (2.1) for \(P\) in the end frames, and those for \(Q=P^{-1}\) follow.

*Two estimates for \(a\).* On \([0,1]\), with \(w=\frac23-u\in(0,\frac23]\) where \(a\ne0\), (1.2) gives \(-a'=e^{-1/w}/w^2\). Since \(w^{-2}\ge\frac94\ge e^{-1/w}\), we get \(a^2=e^{-1/w}\cdot e^{-1/w}\le e^{-1/w}w^{-2}=-a'\); and \(x^2e^{-x}\le4e^{-2}<1\) for \(x=1/w\) gives \(|a'|\le1\). So on \([0,1]\)
\[
a^2\le-a',\qquad|a'|\le1 . \tag{2.3}
\]

*Outside \(I_0=[\frac5{12},\frac7{12}]\).* There \(\chi'=0\), so \(H\) is constant and, with \(q=R^{\mathsf T}p\),
\[
\begin{aligned}
&P'=\delta a(t)\,e_1e_1^{\mathsf T}-\delta a(1-t)\,HH^{\mathsf T},\\
&p^{\mathsf T}(-P'')p\\
&\quad=\delta\bigl(-a'(t)q_1^2-a'(1-t)q_2^2\bigr)\ge0 .
\end{aligned}
\]
Since \(|H|^2\le\frac{17}{16}\),
\[
\begin{aligned}
|P'p|^2&\le2\delta^2\bigl(a(t)^2q_1^2+\tfrac{17}{16}a(1-t)^2q_2^2\bigr)\\
&\le3\delta\,p^{\mathsf T}(-P'')p
\end{aligned}
\]
by (2.3), and \(\|P'\|\le3\delta\).

*On \(I_0\).* There \(t\) and \(1-t\) lie in \([\frac5{12},\frac7{12}]\), so \(w\in[\frac1{12},\frac14]\), where \(e^{-1/w}/w^2\) is increasing; hence \(-a'(t),-a'(1-t)\ge m:=144e^{-12}\). Compare \(P\) with \(P_0=\operatorname{diag}(d_1,d_2)\): the difference
\[
\begin{aligned}
E=P-P_0&=d_2\bigl(\epsilon\chi\,(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T})\\
&\qquad+\epsilon^2\chi^2e_1e_1^{\mathsf T}\bigr)
\end{aligned}
\]
and its first two derivatives are sums of terms each containing a factor \(\epsilon\) or \(\epsilon^2\), a factor \(d_2\), \(d_2'=-\delta a(1-t)\) or \(d_2''=\delta a'(1-t)\) (all bounded by \(2\)), and factors \(\chi,\chi',\chi''\). So \(\|E'\|\le C_1\epsilon\) and \(\|E''\|\le C_2\epsilon\) with \(C_1,C_2\) depending only on \(\sup|\chi'|\) and \(\sup|\chi''|\). Now \(-P_0''\succeq m\delta\operatorname{Id}\), because \(-P_0''=\delta\operatorname{diag}(-a'(t),-a'(1-t))\), and \(\epsilon=\delta^2\); for \(\delta\le m/(2C_2)\),
\[
\begin{aligned}
&-P''=-P_0''-E''\\
&\quad\succeq\bigl(m\delta-C_2\delta^2\bigr)\operatorname{Id}\succeq\tfrac12m\delta\operatorname{Id},\\
&\|P'\|\le\delta+C_1\delta^2\le(1+C_1)\delta,
\end{aligned}
\]
so
\[
\begin{aligned}
|P'p|^2&\le(1+C_1)^2\delta^2|p|^2\\
&\le\frac{2(1+C_1)^2}m\,\delta\,p^{\mathsf T}(-P'')p .
\end{aligned}
\]

*End frames.* For \(\widetilde P=T_i^{-1}PT_i^{-\mathsf T}\) and \(q=T_i^{-\mathsf T}p\), \(\widetilde P''=T_i^{-1}P''T_i^{-\mathsf T}\), so \(p^{\mathsf T}(-\widetilde P'')p=q^{\mathsf T}(-P'')q\ge0\), and \(|\widetilde P'p|^2\le3|P'q|^2\le3C\delta\,p^{\mathsf T}(-\widetilde P'')p\) with \(C\) the constant found above; also \(\|\widetilde P'\|\le3\|P'\|\). Replacing \(t\) by \(1-t\) changes the sign of the first derivative and leaves the second unchanged. Take \(\delta_0=\min\{\frac12,\,m/(2C_2)\}\), and let \(C_0\) be the largest of the numbers \(18\), \(9\), \(3(1+C_1)\) and \(6(1+C_1)^2/m\). \(\square\)

The middle of the path carries the shear: \(H\) turns from \(e_2\) to \(e_2+\epsilon e_1\) while both diagonal coefficients are strictly concave, and since the shear has size \(\epsilon=\delta^2\), it does not destroy the concavity of size \(\delta\). The periods \(B_1=\epsilon B_2\) turn this small shear into the fixed integral gluing \(h_2=h_1+f_1\), \(f_2=h_1\).

## 3. Warped products and the ends of the neck

**Lemma 3.1** (warped surfaces and products with a circle). Let \(\ell>0\) be smooth on an interval \(J\). The metric \(d\tau^2+\ell(\tau)^2dy^2\) on \(J\times\mathbb R/B\mathbb Z\) has Gaussian curvature \(-\ell''/\ell\). If a surface has Gaussian curvature \(K\le0\), every sectional curvature of its Riemannian product with a circle lies in \([K,0]\) at each point.

*Proof.* In the coordinates \((\tau,y)\), the only nonzero Christoffel symbols are \(\Gamma^\tau_{yy}=-\ell\ell'\) and \(\Gamma^y_{\tau y}=\Gamma^y_{y\tau}=\ell'/\ell\). Hence \(\nabla_{\partial_\tau}\partial_\tau=0\) and \(\nabla_{\partial_\tau}\partial_y=\nabla_{\partial_y}\partial_\tau=(\ell'/\ell)\partial_y\), and
\[
\begin{aligned}
&R(\partial_y,\partial_\tau)\partial_\tau\\
&\quad=\nabla_{\partial_y}\nabla_{\partial_\tau}\partial_\tau-\nabla_{\partial_\tau}\nabla_{\partial_y}\partial_\tau\\
&\quad=-\Bigl(\bigl(\tfrac{\ell'}\ell\bigr)'+\bigl(\tfrac{\ell'}\ell\bigr)^2\Bigr)\partial_y\\
&\quad=-\frac{\ell''}\ell\,\partial_y .
\end{aligned}
\]
So \(K=\langle R(\partial_y,\partial_\tau)\partial_\tau,\partial_y\rangle/|\partial_y|^2=-\ell''/\ell\). For the product, the curvature tensor is that of the surface on surface vectors and vanishes as soon as one argument is tangent to the flat circle. For orthonormal \(X=X_1+X_2\), \(Y=Y_1+Y_2\), split into surface and circle components, the sectional curvature is \(K\bigl(|X_1|^2|Y_1|^2-\langle X_1,Y_1\rangle^2\bigr)\), and the bracket lies in \([0,1]\). \(\square\)

In the end frame \(T_i\) with inward coordinate \(\tau\), the neck metric for \(0\le\tau\le\frac14\) is, by Lemma 1.1,
\[
\begin{aligned}
g&=d\tau^2+\ell_0(\tau)^2dy_1^2\\
&\quad+b^{-1}dy_2^2,\\
\ell_0(\tau)&=(1+\delta A(\tau))^{-1/2},
\end{aligned} \tag{3.1}
\]
the product of a warped surface and a flat circle. The function \(\ell_0\) is defined for \(\tau\ge-1\), where \(A(\tau)\ge-1\) and \(1+\delta A\ge\frac12\). Writing \(w=1+\delta A\), \(w'=\delta a\), \(w''=\delta a'\),
\[
\begin{aligned}
&\frac{\ell_0''}{\ell_0}=\frac{3\delta^2a^2}{4(1+\delta A)^2}\\
&\qquad-\frac{\delta a'}{2(1+\delta A)}\ge0
\end{aligned} \tag{3.2}
\]
on \([-1,\frac14]\), because \(a'\le0\) there. By Lemma 3.1, **the neck has nonpositive sectional curvature for \(0\le t\le\frac14\) and for \(\frac34\le t\le1\).** Also \(\ell_0'(\tau)=-\delta a(\tau)/(2w^{3/2})<0\), with \(\ell_0(0)=1\) and \(\ell_0'(0)=-\kappa/2\).

## 4. Convex collars, flat cores and the metric on \(M\)

Fix \(\delta\in(0,\delta_0]\) and a period \(B\in(0,1]\). We build a holed torus \(\Sigma\) with a collar of period \(B\) whose metric has curvature at most \(0\) and is given near its boundary by \(d\tau^2+\ell_0(\tau)^2dy_1^2\).

**The warping function.** Fix a smooth \(\tilde\chi\colon\mathbb R\to[0,1]\) equal to \(0\) on \((-\infty,-1]\) and to \(1\) on \([-\frac12,\infty)\). Since \(\ell_0''\ge0\) on \([-1,0]\), \(0\le\int_{-1}^0\tilde\chi\ell_0''\le\ell_0'(0)-\ell_0'(-1)\), which is at most \(|\ell_0'(-1)|<1\), and \(\kappa/2<1\). As \(2\pi/B\ge2\pi\), we may choose a smooth function \(\beta\ge0\) supported in \((-2,-1)\) with
\[
\int\beta=\frac{2\pi}B-\frac\kappa2-\int_{-1}^0\tilde\chi\,\ell_0''>0 .
\]
Put \(g_\ell=\tilde\chi\ell_0''+\beta\ge0\) on \([-3,0]\), and let \(\ell\) be the solution of \(\ell''=g_\ell\) with \(\ell(0)=1\), \(\ell'(0)=-\kappa/2\). Then:

1. \(\ell=\ell_0\) on \([-\frac12,0]\), since both solve the same second-order equation there with the same data at \(0\); so \(\ell\) continues smoothly by \(\ell_0\) on \([0,\frac14]\).
2. \(\ell'(\tau)=-\frac\kappa2-\int_\tau^0g_\ell<0\), so \(\ell\) is decreasing and \(\ell\ge1\) on \([-3,0]\); and \(\ell''\ge0\).
3. For \(\tau\le-2\), \(\ell'(\tau)=-2\pi/B\), so \(\ell(\tau)=\frac{2\pi}B\,(r_1-2-\tau)\) on \([-3,-2]\), where \(r_1=\ell(-2)B/(2\pi)\).

**The collar.** Let \(C=[-3,0]\times\mathbb R/B\mathbb Z\) with the metric \(d\tau^2+\ell(\tau)^2dy_1^2\). By Lemma 3.1 its curvature is \(-\ell''/\ell\le0\). On \([-3,-2]\times\mathbb R/B\mathbb Z\), the substitution \(r=r_1-2-\tau\), \(\theta=2\pi y_1/B\) turns the metric into \(dr^2+r^2d\theta^2\), the Euclidean metric in polar coordinates, on the annulus \(r_1\le r\le r_1+1\).

**The flat part.** Choose \(c>2(r_1+1)\) and let \(F_c\), \(\pi\) and \(D_\rho\) be as in Section 1 of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md). The closed annulus \(r_1\le|x|\le r_1+1\) about the origin embeds isometrically in \(F_c\) under \(\pi\), and the substitution above identifies it with \([-3,-2]\times\mathbb R/B\mathbb Z\subseteq C\). Let \(\Sigma\) be the union of \(F_c\setminus\pi(D_{r_1})\) and \(C\) glued along this isometry. Each point of \(\Sigma\) has a neighbourhood contained in one of the two pieces: points with \(r=r_1+1\) lie in the interior of the flat piece and points with \(\tau=-2\) in the interior of \(C\). So \(\Sigma\) is a smooth compact surface with boundary \(\{\tau=0\}\) and a smooth metric, flat on the first piece and of curvature \(-\ell''/\ell\le0\) on the second. Every sectional curvature of \(\Sigma\) is nonpositive.

\(\Sigma\) is a holed torus with a collar of period \(B\): the collar is \((-1,0]\times\mathbb R/B\mathbb Z\subseteq C\), and a diffeomorphism of \([-3,0]\) onto \([\frac{r_1}2,r_1+1]\) that is decreasing and equals \(r_1-2-\tau\) near \([-3,-2]\) defines, together with \(\theta=2\pi y_1/B\), a diffeomorphism of \(\Sigma\) onto \(F_c\setminus\pi(D_{r_1/2})\).

**The metric on \(M\).** Fix \(\delta\in(0,\delta_0]\) and \(B_2\in(0,1]\), and put \(B_1=\delta^2B_2\), so that \(B_1/B_2=\epsilon\). Build \(\Sigma_1\) with period \(B_1\) and \(\Sigma_2\) with period \(B_2\) as above, and form \(M\) as in Section 1 of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md). Give the neck the metric \(dt^2+dx^{\mathsf T}Q(t)dx\), which is well defined on \([0,1]\times T\) because it does not depend on \(x\), and give \(N_i=\Sigma_i\times\mathbb R/B_{3-i}\mathbb Z\) the product of the metric of \(\Sigma_i\) with \(b^{-1}dy_2^2\).

**Proposition 4.1** (the metric). These metrics fit together to a smooth Riemannian metric on the closed manifold \(M\). Every sectional curvature at every point outside the open neck \(U=(0,1)\times T\) is nonpositive, and so is every sectional curvature at points of the neck with \(t\le\frac14\) or \(t\ge\frac34\).

*Proof.* Near the first boundary torus, in the chart \((\tau,y)\mapsto(t,x)=(\tau,T_1y)\), the metric of \(N_1\) for \(-\frac12<\tau\le0\) is \(d\tau^2+\ell_0(\tau)^2dy_1^2+b^{-1}dy_2^2\), and by (3.1) the neck metric for \(0\le\tau\le\frac14\) is given by the same formula. So on \((-\frac12,\frac14)\times T\) the metric is given by one smooth formula. The second boundary torus is the same with \(T_2\) and \(\tau=1-t\). The curvature statement on \(N_i\) is Lemma 3.1 applied to \(\Sigma_i\), and on the end portions of the neck it is (3.2). \(\square\)

The neck metric, lifted to \([0,1]\times\mathbb R^2\), depends only on \(\delta\) and the fixed function \(\chi\), not on \(B_1\), \(B_2\), \(\tilde\chi\), \(\beta\) or \(c\). All estimates of the following lessons concern this lifted neck metric; \(\delta\) is fixed by them, and the periods may be chosen afterwards. In [OpenAI-NC, Section 3 and Appendix A] the cores are hyperbolic punctured tori truncated along a horocycle, whose cusp has the warped form \(dr^2+c^2e^{-2r}d\theta^2\); a convex collar joins that cusp to (3.1) in the same way, and any compact nonpositively curved holed torus whose boundary germ matches (3.1) would serve.

## 5. Exercises

**5.1.** Show that \(a(\frac18)/a(0)=e^{-9/26}\).

**5.2.** Show that \(T_2\operatorname{diag}(\alpha,\beta)T_2^{\mathsf T}=\alpha HH^{\mathsf T}+\beta e_1e_1^{\mathsf T}\) for \(H=e_2+\epsilon e_1\), and deduce Lemma 1.1 at the second end directly.

**5.3.** Compute the curvature of \(d\tau^2+e^{-2\tau}dy^2\) and of \(d\tau^2+(T-\tau)^2dy^2\) with Lemma 3.1, and identify the two surfaces.

**5.4.** Let \(\ell\) be smooth and positive with \(\ell''(\tau_0)<0\) at some point. Show that the warped surface has positive curvature near \(\tau_0\); explain why the construction of Section 4 needs \(g_\ell\ge0\).

**5.5.** Show that \(H(t)H(t)^{\mathsf T}-e_2e_2^{\mathsf T}\) equals \(\epsilon\chi(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T})+\epsilon^2\chi^2e_1e_1^{\mathsf T}\), and that its norm is at most \(3\epsilon\).

## 6. Solutions

**5.1.** By the definition of \(a\),
\[
\begin{aligned}
&\log a(\tfrac18)-\log a(0)\\
&\quad=-\frac1{2/3-1/8}+\frac1{2/3}=-\frac{24}{13}+\frac32\\
&\quad=-\frac9{26}.
\end{aligned}
\]

**5.2.** Writing \(\operatorname{diag}(\alpha,\beta)=\alpha\,e_1e_1^{\mathsf T}+\beta\,e_2e_2^{\mathsf T}\),
\[
\begin{aligned}
&T_2\operatorname{diag}(\alpha,\beta)T_2^{\mathsf T}\\
&\quad=\alpha\,T_2e_1(T_2e_1)^{\mathsf T}+\beta\,T_2e_2(T_2e_2)^{\mathsf T}
\end{aligned}
\]
with \(T_2e_1=H\), \(T_2e_2=e_1\). For \(t\ge\frac34\) and \(\tau=1-t\),
\[
\begin{aligned}
P&=b\,e_1e_1^{\mathsf T}+(1+\delta A(\tau))HH^{\mathsf T}\\
&=T_2\operatorname{diag}(1+\delta A(\tau),b)T_2^{\mathsf T},
\end{aligned}
\]
which is (1.6) in the frame \(T_2\).

**5.3.** For \(\ell=e^{-\tau}\), \(-\ell''/\ell=-1\): a hyperbolic cusp. For \(\ell=T-\tau\), \(\ell''=0\): the flat metric in polar coordinates with \(r=T-\tau\).

**5.4.** \(K=-\ell''/\ell>0\) where \(\ell''<0\), by continuity near \(\tau_0\). If \(g_\ell\) were negative somewhere, the collar would have positive curvature there, and Proposition 4.1 would fail.

**5.5.** Expand \((e_2+\epsilon\chi e_1)(e_2+\epsilon\chi e_1)^{\mathsf T}\). The norm of \(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T}\) is \(1\) and that of \(e_1e_1^{\mathsf T}\) is \(1\), so the norm is at most \(\epsilon+\epsilon^2\le3\epsilon\).

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 3 (Lemma 3.1) and Appendix A. https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026

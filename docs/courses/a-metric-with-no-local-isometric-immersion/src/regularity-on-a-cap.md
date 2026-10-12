# Regularity on a cap

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An admissible height on the model square is a solution of the height equation with a few bounds. This lesson proves that such a solution is as regular as the metric allows, with bounds that depend only on a few low-order bounds, in the lower and in the upper part of the square: bounds for the derivatives of the solution up to order eight, and bounds for all derivatives of the metric, give bounds for all derivatives of the solution. The regions in question, the *caps*, contain the curve where the curvature changes its sign, and their edge towards the centre of the square is a free edge. The proof is an induction over the order of the derivatives. Each step applies the estimate at the free edge to the differentiated height equation.

- Flow coordinates exist on the square \([-2,2]^2\), with bounds (Lemma 2.1).
- On rectangles in a cap, the differentiated height equation satisfies the three assumptions of the estimate at the free edge (Proposition 3.1).
- The right side of that equation is bounded in mean square by the derivatives of lower order (Lemma 4.2).
- Bounds for all derivatives (Theorem 5.1).

The lesson follows [OpenAI-I, Section 3, the proposition on cap regularity]. It uses the three preceding lessons of this course: the model square and admissible heights from [The metric and the theorem](the-metric-and-the-theorem.md), the identities of [The differentiated height equation](the-differentiated-height-equation.md), and the theorem of [The estimate at the free edge](the-estimate-at-the-free-edge.md).

## 1. The setting

Fix the function \(h\), the square \(S=[-3,3]^2\) and \(\mathcal P=[-\tfrac1{10},\tfrac1{10}]^2\) of the lesson on the metric and the theorem, a constant \(\kappa>0\), and numbers \(M\ge1\), \(0<c\le1\), \(-\tfrac14<b_*\le0\). A *pair* \((g,z)\) consists of a metric \(g\) on a neighbourhood of \(S\) and a function \(z\) such that:

1. \(K_g=\kappa(x^2-h(y))\) on \(S\) outside \(\mathcal P\), and \(K_g<-\tfrac12\kappa\) on \([-\tfrac15,\tfrac15]^2\);
2. \(z\) is an admissible height for \(g\);
3. on \(S\), the entries of \(g\), the function \(z\), and their derivatives of order at most \(8\) are at most \(M\) in absolute value, \(g(v,v)\ge c|v|^2\) for all vectors \(v\), \(|H_{yy}|\ge c\) and \(E\ge c\).

We use the notation of the lesson on the differentiated height equation: \(q=H_{xy}/H_{yy}\), \(D=\partial_x-q\partial_y\), \(G=E/H_{yy}^2\). By admissibility \(|q|\le\tfrac1{100}\). A number is called *controlled* if it depends only on \(h,\kappa,M,c,b_*\) and on the further numbers named at that place, and not on the pair. For example \(|q_y|\), \(|q_{yy}|\) and \(G\), \(1/G\) are bounded on \(S\) by controlled numbers: they are quotients of polynomials in the derivatives of \(g\) of order at most \(3\) and of \(z\) of order at most \(4\), with denominators that are powers of \(\det g\ge c^2\) and of \(H_{yy}\).

**Lemma 1.1.** Let \(r>0\), \(p\in\mathbb R^2\), and \(w\) a smooth function on a neighbourhood of the square \(Q=p+[-r,r]^2\). Then
\[
\begin{aligned}
|w(p)|^2&\le\frac1{r^2}\iint_Qw^2+2\iint_Q(w_x^2+w_y^2)\\
&\quad+4r^2\iint_Qw_{xy}^2 .
\end{aligned}
\]

**Proof.** For a smooth function \(\phi\) on \([-r,r]\) and \(|x|\le r\), \(\phi(0)=\phi(x)-\int_0^x\phi'\), so \(\phi(0)^2\le2\phi(x)^2+2r\int_{-r}^r\phi'^2\). Taking the mean over \(x\) gives \(\phi(0)^2\le\tfrac1r\int\phi^2+2r\int\phi'^2\). Let \(p=0\). Apply this to \(x\mapsto w(x,0)\), and then, for every \(x\), to \(y\mapsto w(x,y)\) and to \(y\mapsto w_x(x,y)\). \(\blacksquare\)

## 2. Flow coordinates on the square

**Lemma 2.1.** For every pair there is a smooth function \(y(t,s)\) on a neighbourhood of \([-2,2]^2\) with \(y_t=-q(t,y)\) and \(y(0,s)=s\). It satisfies \(|y(t,s)-s|\le\tfrac1{50}\), so \(\Phi(t,s)=(t,y(t,s))\) maps \([-2,2]^2\) into the interior of \(S\). The function \(\sigma=1/y_s\) satisfies \(\sigma_0\le\sigma\le1/\sigma_0\) with a controlled \(\sigma_0>0\), and \(|\sigma_s|,|\sigma_t|\) are bounded by controlled numbers. The map \(\Phi\) is a diffeomorphism onto its image, and for all points \(a,a'\) of \([-2,2]^2\)
\[
\begin{gathered}
\Lambda^{-1}|a-a'|\le|\Phi(a)-\Phi(a')|,\\
|\Phi(a)-\Phi(a')|\le\Lambda|a-a'|
\end{gathered}
\]
with a controlled \(\Lambda\).

**Proof.** The equation \(y_t=-q(t,y)\) has a solution as long as \((t,y)\) stays in the interior of \(S\), and \(|y_t|\le\tfrac1{100}\) gives \(|y-s|\le\tfrac{|t|}{100}\). So the solution exists for \(|t|\le2\) and \(|s|\le2\), and a little beyond, and it is smooth in \((t,s)\). By Lemma 6.1 of the lesson on the differentiated height equation, \(\sigma=\exp\int_0^tq_y(r,y(r,s))\,dr\), which lies between \(e^{-2Q_1}\) and \(e^{2Q_1}\) if \(|q_y|\le Q_1\). Differentiating gives \(\sigma_t=q_y\sigma\) and \(\sigma_s=\sigma\int_0^tq_{yy}\,y_s\,dr\). The first derivatives of \(\Phi\) are \(1,0,-q,1/\sigma\), and \(\Phi\) is injective because \(y\) is increasing in \(s\). For the two inequalities: if \(a=(t,s)\) and \(a'=(t',s')\), then the number \(\Delta=|y(t,s)-y(t',s')|\) satisfies \(\Delta\le\tfrac1{100}|t-t'|+\sigma_0^{-1}|s-s'|\) and \(\Delta\ge\sigma_0|s-s'|-\tfrac1{100}|t-t'|\). \(\blacksquare\)

A *rectangle* is a set \([t_1,t_2]\times[s_1,s_2]\). The *lower cap* is the open set \((-2,2)\times(-2,b_*)\) in the coordinates \(t,s\). If \(R\) and \(R'\) are rectangles and \(R\) lies in the interior of \(R'\), let \(\operatorname{dist}(R,R')\) be the distance from \(R\) to the complement of \(R'\).

**Lemma 2.2.** Let \(R\subseteq R'\subseteq[-2,2]^2\) be rectangles with \(\delta=\operatorname{dist}(R,R')>0\), and \(r=\delta/(2\Lambda)\). For every pair and every \(p\in\Phi(R)\), the square \(p+[-r,r]^2\) lies in \(\Phi(R')\).

**Proof.** Let \(p=\Phi(a)\) with \(a\in R\), and let \(p'\) be a point of the square. The set \(\Phi(R')\) is compact. If \(p'\notin\Phi(R')\), let \(p''\) be the first point of the segment from \(p\) to \(p'\) that is not in the image of the interior of \(R'\); it exists because that image is open, and \(p''=\Phi(a'')\) with \(a''\) on the boundary of \(R'\). Then \(\delta\le|a''-a|\le\Lambda|p''-p|\le\Lambda\sqrt2\,r<\delta\), a contradiction. \(\blacksquare\)

## 3. The assumptions of the estimate

Let \(l\ge3\). For a pair, let \(u=\partial_y^lz\). By Theorem 6.2 of the lesson on the differentiated height equation, on \([-2,2]^2\) in the coordinates \(t,s\),
\[
u_{tt}+A\,u_{ss}+B\,u_t+C\,u_s=R_l,
\]
with \(A=G_1K\), \(G_1=G\sigma^2\), \(B=-P_{z_x}-2lq_y\) and \(C=(l+1)A_s+K\rho_3\).

**Proposition 3.1.** Let \(\tfrac32\le T_1<T<2\), \(-2<s_0<s_1\le-\tfrac32\), and \(s_1<b<b_*\), and \(\Omega=[-T,T]\times[s_0,b]\). There are controlled numbers \(M_0,\alpha_0,\varepsilon,a_0,\theta_0\), depending also on \(l\), such that for every pair the assumptions (A1), (A2) and (A3) of the lesson on the estimate at the free edge hold on \(\Omega\), with these numbers and with \(T,T_1,s_0,s_1,b\).

**Proof.** There is a controlled \(\gamma\in(0,1]\) with \(\gamma\le G_1\le1/\gamma\) on \([-2,2]^2\), by Lemma 2.1 and the bounds for \(G\).

(A1) holds with \(\omega=\rho_3/G_1\), since \(K=A/G_1\). The functions \(A,A_t,A_s,B,B_s,\omega\) are formed from \(\sigma,\sigma_s,\sigma_t\) and from the values at \(\Phi(t,s)\) of the derivatives of \(g\) of order at most \(5\) and of \(z\) of order at most \(5\): \(K\) contains two derivatives of \(g\); \(\rho_1\), \(\rho_2\) and \(q_y\) contain three derivatives of \(z\) and two of \(g\); and one further derivative is taken. All denominators are powers of \(\det g\), \(H_{yy}\) and \(G_1\). So they are bounded by a controlled \(M_0\).

(A2) At a point of \(\Omega\) with \(|t|\ge T_1\), \(x=t\) and \(|x|\ge\tfrac32\), so the point \(\Phi(t,s)\) is outside \(\mathcal P\) and \(K=\kappa(t^2-h(y))\ge\tfrac54\kappa\), because \(h\le1\). At a point with \(s\le s_1\), \(y\le-\tfrac32+\tfrac1{50}\), so again the point is outside \(\mathcal P\), and \(h(y)\le h(-\tfrac{37}{25})<0\), because \(h\) is increasing on \((-\infty,0]\) and negative below \(-1\); so \(K\ge\kappa\,|h(\tfrac{37}{25})|\). Hence (A2) holds with \(\alpha_0=\gamma\kappa\min\{\tfrac54,|h(\tfrac{37}{25})|\}\).

(A3) Let \(a_0<\tfrac12\gamma\kappa\). At a point with \(|A|\le a_0\) we have \(|K|<\tfrac12\kappa\), so \(\Phi(t,s)\) is outside \([-\tfrac15,\tfrac15]^2\), and \(K=\kappa(x^2-h(y))\) near it. Then \(K_x=2\kappa t\) and \(K_y=-\kappa h'(y)\). By Lemma 6.1 of the lesson on the differentiated height equation, \(\partial_s(K\circ\Phi)=K_y/\sigma\) and \(\partial_t(K\circ\Phi)=K_x-qK_y\). So
\[
\begin{aligned}
\Theta&=-(l+\tfrac12)A_s+\tfrac\varepsilon2tA_t\\
&=G_1\kappa\,\bigl(\tau\,h'(y)+\varepsilon t^2\bigr)+K\,\mu,\\
\tau&=\tfrac{l+1/2}\sigma+\tfrac\varepsilon2tq,
\end{aligned}
\]
where \(\mu=-(l+\tfrac12)(G_1)_s+\tfrac\varepsilon2t(G_1)_t\) is bounded by a controlled \(\mu_0\). On \(\Omega\) we have \(y\le b_*+\tfrac1{50}\le\tfrac1{50}\), and \(h'(y)\ge0\) there: \(h\) is increasing on \((-\infty,0]\) and constant on \([0,\tfrac12]\). Choose \(\varepsilon\le1\) with \(16\varepsilon^2T^2M_0\le1\) and \(\varepsilon\le\tfrac12\sigma_0\). Then the factor \(\tau\) of \(h'(y)\) is at least \(\tfrac12\sigma_0-\tfrac\varepsilon{100}\ge\tfrac14\sigma_0\), and
\[
\begin{gathered}
\Theta\ge\gamma\kappa\,\nu(t,y)-|K|\mu_0,\\
\nu(t,y)=\tfrac14\sigma_0h'(y)+\varepsilon t^2 .
\end{gathered}
\]
Consider \(\nu\) on the compact set \(Z_\delta\) of the points \((t,y)\) with \(|t|\le2\), \(-\tfrac{101}{50}\le y\le\tfrac1{50}\) and \(|t^2-h(y)|\le\delta\). On \(Z_0\) it is positive: if \(t\ne0\) then \(\varepsilon t^2>0\); if \(t=0\) then \(h(y)=0\), so \(y=-1\), and \(h'(-1)=-h'(1)>0\). So \(\nu\ge2\nu_0>0\) on \(Z_0\). The sets \(Z_\delta\) decrease to \(Z_0\) as \(\delta\to0\), and \(\nu\) is continuous, so there is \(\delta_0>0\) with \(\nu\ge\nu_0\) on \(Z_{\delta_0}\); the numbers \(\nu_0,\delta_0\) depend only on \(h,\sigma_0,\varepsilon\). Now let
\[
a_0=\gamma\kappa\min\Bigl\{\tfrac14,\ \delta_0,\ \frac{\gamma\nu_0}{2\mu_0}\Bigr\}.
\]
At a point with \(|A|\le a_0\): \(|t^2-h(y)|=|K|/\kappa\le a_0/(\gamma\kappa)\le\delta_0\), so \(\nu\ge\nu_0\); and \(|K|\mu_0\le a_0\mu_0/\gamma\le\tfrac12\gamma\kappa\nu_0\). Hence \(\Theta\ge\theta_0=\tfrac12\gamma\kappa\nu_0\). \(\blacksquare\)

The curvature profile was chosen for this proof. The zero set of the curvature in the cap is the curve \(x^2=h(y)\). At its lowest point \((0,-1)\) the curvature has a nonzero derivative in \(y\), with the favourable sign; away from that point \(x\ne0\), and the term \(\varepsilon t^2\), which comes from the part \(n=\varepsilon tW\) of the multiplier, is positive.

## 4. The remainder

In this section and the next, a family of pairs is given with the following property: for every rectangle \(R\) in the lower cap and every \(k\ge0\) there is a number \(N(R,k)\) such that for every pair of the family the derivatives of the entries of \(g\) of order at most \(k\) are at most \(N(R,k)\) in absolute value on \(\Phi(R)\). Numbers that depend only on \(h,\kappa,M,c,b_*\), on the function \(N\), and on the rectangles and orders named are again called controlled.

For \(j\ge0\) and a rectangle \(R\) in the lower cap, let \(\Sigma_j(R)\) be the supremum over the family of
\[
\sum_{|\alpha|\le j}\iint_{\Phi(R)}|\partial^\alpha z|^2\,dx\,dy,
\]
where \(\partial^\alpha\) runs through the partial derivatives in \(x,y\) of order at most \(j\).

**Lemma 4.1.** Let \(j\ge2\), and let \(R\) lie in the interior of \(R'\), both rectangles in the lower cap. If \(\Sigma_j(R')\) is finite, then the derivatives of \(z\) of order at most \(j-2\) are bounded on \(\Phi(R)\) by a controlled number, depending also on \(\Sigma_j(R')\).

**Proof.** Apply Lemma 1.1 to \(w=\partial^\alpha z\), \(|\alpha|\le j-2\), on the squares of Lemma 2.2. \(\blacksquare\)

**Lemma 4.2.** Let \(l\ge8\), and let \(R\) lie in the interior of \(R'\), both rectangles in the lower cap. If \(\Sigma_l(R')\) is finite, then the mean square over \(\Phi(R)\) of the remainder \(R_l\) of Theorem 5.1 of the lesson on the differentiated height equation is bounded by a controlled number, depending also on \(l\) and \(\Sigma_l(R')\). The same holds for the remainder in the following formula: for every \(k\ge2\) and \(k\le l+1\),
\[
\begin{aligned}
&\partial_x^k\partial_y^{l+1-k}z\\
&\quad=2q\,\partial_x^{k-1}\partial_y^{l+2-k}z\\
&\qquad-(q^2+a)\,\partial_x^{k-2}\partial_y^{l+3-k}z+R_{l,k}.
\end{aligned}
\]

**Proof.** By the lesson on the differentiated height equation, \(R_l\) is a sum of terms
\[
c\cdot\partial_y^{k_1}p_{i_1}\cdots\partial_y^{k_n}p_{i_n},
\]
where \(p=(z_x,z_y,z_{xy},z_{yy})\), the \(k_j\) are at least \(1\) with sum at most \(l\), and each factor is a derivative of \(z\) of order at most \(l\); the coefficient \(c\) is an integer multiple of a partial derivative of \(P\) of order at most \(l+1\) with respect to \(y\) and the four variables, at the point \((x,y,p(x,y))\). The function \(P\) is formed from the entries of \(g\), its Christoffel symbols and \(K\) and from the four variables, with denominators that are powers of \(\det g\) and \(H_{yy}\). So \(c\) is bounded on \(\Phi(R)\) by a controlled number: it contains derivatives of \(g\) of order at most \(l+3\), bounded by \(N(R,l+3)\), and the values of \(p\), bounded by \(M\).

A factor \(\partial_y^{k_j}p_{i_j}\) is a derivative of \(z\) of order at most \(k_j+2\). If two factors of one term had order at least \(l-1\), their numbers \(k_j\) would be at least \(l-3\) each, with sum at least \(2l-6>l\). So in every term at most one factor has order \(l-1\) or \(l\), and all others have order at most \(l-2\). By Lemma 4.1 the latter are bounded on \(\Phi(R)\); the mean square of the former over \(\Phi(R)\) is at most \(\Sigma_l(R')\). This bounds the mean square of each term, and the number of terms depends only on \(l\).

For the formula, apply \(\partial_x^{k-2}\partial_y^{l+1-k}\) to \(z_{xx}=P(x,y,p)\). This is a derivative of order \(l-1\). As in the first paragraph of the proof of Lemma 4.1 of the lesson on the differentiated height equation, now with differentiations in \(x\) and \(y\), the result is \(\sum_iP_{p_i}\partial_x^{k-2}\partial_y^{l+1-k}p_i\) plus a sum of terms \(c\cdot\partial^{\beta_1}p_{i_1}\cdots\partial^{\beta_n}p_{i_n}\) with \(1\le|\beta_j|\le l-2\) and \(|\beta_1|+\dots+|\beta_n|\le l-1\). In the first sum, the terms with \(p_i=z_{xy}\) and \(p_i=z_{yy}\) are the two terms displayed, by \(P_{z_{xy}}=2q\) and \(P_{z_{yy}}=-q^2-a\); the terms with \(p_i=z_x,z_y\) are bounded multiples of derivatives of \(z\) of order \(l\). In the other terms every factor is a derivative of \(z\) of order at most \(l\), and at most one factor has order at least \(l-1\), because \(2(l-3)>l-1\). They are bounded in mean square by the same argument. \(\blacksquare\)

## 5. All derivatives

**Theorem 5.1.** Let a family of pairs be given as at the head of Section 4. Then for every rectangle \(R\) in the lower cap and every \(k\ge0\) there is a controlled number \(N'(R,k)\) such that for every pair of the family the derivatives of \(z\) of order at most \(k\) are at most \(N'(R,k)\) in absolute value on \(\Phi(R)\).

**Proof.** We show by induction on \(l\ge8\) that \(\Sigma_l(R)\) is bounded by a controlled number for every rectangle \(R\) in the lower cap. With Lemma 4.1 this gives the theorem. For \(l=8\) the derivatives are bounded by \(M\).

Suppose the claim holds for some \(l\ge8\), and let \(R\) be a rectangle in the lower cap. Choose numbers with \(\tfrac32\le T_1<T<2\), \(-2<s_0<s_1\le-\tfrac32\) and \(s_1<b_0<b<b_*\) such that \(R\subseteq\Omega_0=[-T_1,T_1]\times[s_1,b_0]\), and let \(\Omega=[-T,T]\times[s_0,b]\). Let \(R'\) be a rectangle in the lower cap that contains \(\Omega\) in its interior.

*The derivatives \(u_t,u_s\).* The function \(u=\partial_y^lz\), in the coordinates \(t,s\), satisfies the equation of Section 3 on \(\Omega\). By Proposition 3.1 the assumptions (A1), (A2), (A3) hold with controlled numbers. By Theorem 5.1 of the lesson on the estimate at the free edge,
\[
\begin{aligned}
&\iint_{\Omega_0}(u_t^2+u_s^2)\,dt\,ds\\
&\quad\le C_*\iint_\Omega(u^2+R_l^2)\,dt\,ds
\end{aligned}
\]
with a controlled \(C_*\). The integrals over sets in the coordinates \(t,s\) and over their images in the coordinates \(x,y\) differ by the factor \(\sigma\) in the integrand, which lies between \(\sigma_0\) and \(1/\sigma_0\). So the right side is at most a controlled multiple of \(\Sigma_l(\Omega)\) plus the mean square of \(R_l\) over \(\Phi(\Omega)\), which is controlled by Lemma 4.2 and the induction hypothesis for \(R'\). By Lemma 6.1 of the lesson on the differentiated height equation,
\[
\partial_y^{l+1}z=\sigma\,u_s,\qquad\partial_x\partial_y^lz=u_t+q\,\sigma\,u_s .
\]
So the mean squares over \(\Phi(\Omega_0)\) of these two derivatives of order \(l+1\) are controlled.

*The other derivatives of order \(l+1\).* By induction on \(k\), the formula of Lemma 4.2 bounds the mean square over \(\Phi(\Omega_0)\) of \(\partial_x^k\partial_y^{l+1-k}z\) for \(k=2,\dots,l+1\): the two derivatives on the right have \(k-1\) and \(k-2\) differentiations in \(x\), the coefficients \(2q\) and \(q^2+a\) are bounded, and the remainder is controlled. So \(\Sigma_{l+1}(\Omega_0)\), and with it \(\Sigma_{l+1}(R)\), is controlled. \(\blacksquare\)

**Corollary 5.2.** The statement of Theorem 5.1 holds for the *upper cap* \((-2,2)\times(-b_*,2)\) in place of the lower cap, both in the assumption on the family and in the conclusion.

**Proof.** Let \(\varrho(x,y)=(x,-y)\). For a pair \((g,z)\) let \(g'\) be the pull-back of \(g\) by \(\varrho\) and \(z'=z\circ\varrho\). By Lemma 1.2 of the lesson on heights, with the matrix \(M\) of \(\varrho\), the Hessian of \(z'\) is \(H'_{xy}=-H_{xy}\circ\varrho\), \(H'_{yy}=H_{yy}\circ\varrho\), the function \(E'\) is \(E\circ\varrho\), and \(K_{g'}=K_g\circ\varrho\). Since \(h\) is even and the squares \(S\), \(\mathcal P\) and \([-\tfrac15,\tfrac15]^2\) are symmetric, \((g',z')\) is again a pair, with \(q'=-q\circ\varrho\). The function \(y'(t,s)=-y(t,-s)\) solves \(y'_t=-q'(t,y')\) with \(y'(0,s)=s\), so the flow map of the new pair is \(\Phi'(t,s)=\varrho(\Phi(t,-s))\). It maps the lower cap onto the reflection of the image of the upper cap under \(\Phi\). So Theorem 5.1 for the reflected family is the statement for the upper cap. \(\blacksquare\)

In the theorem nothing is assumed about the pairs near the edge \(s=b_*\) of the cap beyond the bounds of order eight, and the metric may be very rough above this edge. This is how the result is used in [OpenAI-I, Section 4]: the metrics there carry a rapidly oscillating perturbation near the centre of the square, with large derivatives of high order, and the theorem gives bounds for every derivative of the heights below and above it.

## 6. Exercises

**6.1.** Prove the inequality \(\phi(0)^2\le\tfrac1r\int_{-r}^r\phi^2+2r\int_{-r}^r\phi'^2\) of the proof of Lemma 1.1, and show by an example that no inequality \(|w(p)|^2\le C\iint_Q(w^2+w_x^2+w_y^2)\) holds for all smooth functions on a square in the plane.

**6.2.** Show that the function \(\nu\) of the proof of Proposition 3.1 vanishes at the points with \(t=0\) and \(-\tfrac12\le y\le\tfrac1{50}\), and explain why this does not contradict (A3).

**6.3.** In Lemma 4.2, where is \(l\ge8\) used, and what is the smallest \(l\) for which the counting of the factors works?

**6.4.** Describe the set of the points \((x,y)\) of \(S\) with \(y\le\tfrac1{50}\) at which the curvature of a pair vanishes, and show that it does not meet \(\mathcal P\).

## 7. Solutions

**6.1.** For \(|x|\le r\), \(\phi(0)=\phi(x)-\int_0^x\phi'\), so
\[
\begin{aligned}
\phi(0)^2&\le2\phi(x)^2+2\Bigl(\int_0^x\phi'\Bigr)^2\\
&\le2\phi(x)^2+2|x|\int_{-r}^r\phi'^2 .
\end{aligned}
\]
Integrate over \(x\in[-r,r]\) and divide by \(2r\). Since \(\int_{-r}^r|x|\,dx=r^2\), this gives \(\phi(0)^2\le\tfrac1r\int\phi^2+r\int\phi'^2\), which is a little better than the inequality used in the proof. For the example take \(w_n(x,y)=\log\log(1/\rho)\) for \(\rho=\sqrt{x^2+y^2+1/n}\) small, cut off away from the origin: the integrals of \(w_n^2\) and of the squares of the first derivatives stay bounded as \(n\to\infty\), because \(\int_0^{1/2}\rho\,d\rho/(\rho\log(1/\rho))^2\) converges, while \(w_n(0)\to\infty\).

**6.2.** On \([-\tfrac12,\tfrac12]\) the function \(h\) is \(1\), so \(h'=0\) there and \(\nu(0,y)=0\). At these points \(K=\kappa(0-1)=-\kappa\) if the point is outside \(\mathcal P\), and \(K<-\tfrac12\kappa\) otherwise, so \(|A|\ge\tfrac12\gamma\kappa>a_0\). Assumption (A3) concerns only the points with \(|A|\le a_0\). Where \(A\) is negative and not small, the estimate at the free edge uses the term \(-\tfrac12H_0A\) instead of \(\Theta\).

**6.3.** The count needs \(2(l-3)>l\), that is \(l>6\), for \(R_l\), and \(2(l-3)>l-1\), that is \(l>5\), for \(R_{l,k}\). So \(l\ge7\) suffices for the counting. The induction starts at the order for which bounds are assumed, which is \(8\).

**6.4.** Inside \([-\tfrac15,\tfrac15]^2\) the curvature is negative. Outside \(\mathcal P\) it is \(\kappa(x^2-h(y))\), which vanishes where \(x^2=h(y)\); this needs \(h(y)\ge0\), that is \(-1\le y\le\tfrac1{50}\). For \(-1\le y\le-\tfrac12\) the function \(h\) increases from \(0\) to \(1\), and for \(-\tfrac12\le y\le\tfrac1{50}\) it is \(1\). So the set consists of the two arcs \(x=\pm\sqrt{h(y)}\), \(-1\le y\le-\tfrac12\), which meet at \((0,-1)\), and of the two segments \(x=\pm1\), \(-\tfrac12\le y\le\tfrac1{50}\). Its points have \(|x|=1\) or \(y\le-\tfrac12\), so they are not in \(\mathcal P\).

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026

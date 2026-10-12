# The oscillating perturbation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the patch obstruction (P), the statement on which the theorem of this course was made to depend in the lesson on the metric and the theorem. With it, the proof that a smooth metric can have no smooth local isometric immersion into \(\mathbb R^3\) is complete in the course.

The idea is to perturb a metric in a thin strip \(|\theta|\le\delta/\tau\) across the middle of the model square by a small term that oscillates with the frequency \(\tau\) along the strip. Below and above the strip, an admissible height with fixed bounds is smooth with bounds that do not depend on \(\tau\): this is the regularity on the caps, carried to the edges of the strip by the energy estimates. Inside the strip, the oscillation of the curvature forces an oscillation of the derivative of the height across the strip, of the size \(\delta\,\tau^{1-N}\), while everything else contributes at most a multiple of \(\delta^2\tau^{1-N}\). For small \(\delta\) and large \(\tau\) this is incompatible with the smoothness on both sides. So metrics with such heights cannot be dense anywhere, and the theorem of Baire gives metrics without admissible heights.

- The space of perturbations is a complete metric space, and (P) follows if certain classes of perturbations are nowhere dense (Section 1).
- Bounds at the two edges of the strip (Proposition 3.1).
- A comparison function inside the strip and the equation for the difference (Lemmas 4.1 and 4.2).
- The forcing by the oscillating term (Lemma 5.2), and the contradiction (Section 6).

The lesson follows [OpenAI-I, Section 4]. It uses [Regularity on a cap](regularity-on-a-cap.md) and [Energy estimates where the curvature is negative](energy-estimates-where-the-curvature-is-negative.md), and the definitions of [The metric and the theorem](the-metric-and-the-theorem.md).

## 1. Perturbations and the theorem of Baire

Let \(g_0\) be a model metric with the constant \(\kappa\), and \(\mathcal V\) the vector space of the perturbations: symmetric matrices of smooth functions on the plane that vanish outside \(\mathcal P\), with the norms \(\|\eta\|_{C^m}\). Let
\[
\begin{aligned}
&\operatorname{dist}(\eta,\eta')\\
&\quad=\sum_{m\ge0}2^{-m}\min\{1,\|\eta-\eta'\|_{C^m}\},
\end{aligned}
\]
and \(B_m(\eta,\varrho)=\{\eta':\|\eta'-\eta\|_{C^m}<\varrho\}\).

**Lemma 1.1.** \(\operatorname{dist}\) is a metric on \(\mathcal V\), and \(\mathcal V\) is complete. Every set \(B_m(\eta,\varrho)\) is open, and every open set that contains \(\eta\) contains a set \(B_m(\eta,\varrho)\).

**Proof.** Each term satisfies the triangle inequality. A sequence is a Cauchy sequence for \(\operatorname{dist}\) exactly if it is one for every norm \(\|\cdot\|_{C^m}\); then all derivatives converge uniformly, the limit is smooth with these limits as derivatives, and it vanishes outside \(\mathcal P\). If \(\operatorname{dist}(\eta'',\eta')<2^{-m}\epsilon\) with \(\epsilon<1\), then \(\|\eta''-\eta'\|_{C^m}<\epsilon\); so \(B_m(\eta,\varrho)\) is open. Since the norms increase with \(m\), \(\operatorname{dist}(\eta,\eta')\le2\|\eta-\eta'\|_{C^m}+2^{-m}\); so the ball of radius \(\epsilon\) around \(\eta\) contains \(B_m(\eta,\epsilon/4)\) if \(2^{-m}<\epsilon/2\). \(\blacksquare\)

A subset \(\mathcal A\) of an open set \(\mathcal U\) is *nowhere dense in \(\mathcal U\)* if every nonempty open subset of \(\mathcal U\) contains a nonempty open set that does not meet \(\mathcal A\).

**Theorem 1.2 (Baire).** Let \(\mathcal U\) be a nonempty open subset of a complete metric space, and \(\mathcal A_1,\mathcal A_2,\dots\) subsets that are nowhere dense in \(\mathcal U\). Then every nonempty open subset of \(\mathcal U\) contains a point that lies in no \(\mathcal A_n\).

**Proof.** Let \(\mathcal O\subseteq\mathcal U\) be open and not empty. Choose a closed ball \(\bar B_1\subseteq\mathcal O\) of radius at most \(\tfrac12\) that does not meet \(\mathcal A_1\), then a closed ball \(\bar B_2\) of radius at most \(\tfrac14\) inside the open ball of \(\bar B_1\) that does not meet \(\mathcal A_2\), and so on. The centres form a Cauchy sequence. Its limit lies in every \(\bar B_n\), hence in \(\mathcal O\) and in no \(\mathcal A_n\). \(\blacksquare\)

Let \(\mathcal U\) be the set of the \(\eta\in\mathcal V\) such that \(g_0+\eta\) is positive definite and \(K_{g_0+\eta}<-\tfrac12\kappa\) on \([-\tfrac15,\tfrac15]^2\). It is open, because these are strict inequalities on compact sets for quantities that depend continuously on \(\eta\) and its derivatives of order at most two, and it contains \(0\).

**Theorem 1.3 (the patch obstruction).** Every nonempty open subset of \(\mathcal U\) contains an \(\eta\) such that \(g_0+\eta\) has no admissible height. In particular statement (P) of the lesson on the metric and the theorem holds: for every \(m\) and \(\varepsilon>0\) there is such an \(\eta\) in \(B_m(0,\varepsilon)\).

For an integer \(M\ge1\) let \(v_*=\sqrt{\kappa/2}\,M^{-3/2}\) and \(L=100(1+1/v_*)\). For such \(M\) and a rational number \(q_0\), let \(\mathcal A_{M,q_0}\) be the set of the \(\eta\in\mathcal U\) for which \(g=g_0+\eta\) has an admissible height \(z\) with the following properties on \(S\): the derivatives of \(z\) of order at most \(8\) are at most \(M\) in absolute value, \(\tfrac1M\le|H_{yy}|\le M\), \(E\ge\tfrac1M\), and \(|q(0,0)-q_0|<\tfrac1{100L}\). Such a \(z\) is called a *height of the class*.

**Proposition 1.4.** Every set \(\mathcal A_{M,q_0}\) is nowhere dense in \(\mathcal U\).

**Proof of Theorem 1.3 from Proposition 1.4.** If \(g_0+\eta\) has an admissible height \(z\), then \(z\) is smooth on a neighbourhood of the compact set \(S\), and \(H_{yy}\ne0\), \(E>0\) there; so the bounds hold for some \(M\), and then for a rational \(q_0\) near \(q(0,0)\). So every such \(\eta\) lies in one of the countably many sets \(\mathcal A_{M,q_0}\). By Lemma 1.1 and Theorem 1.2 every nonempty open subset of \(\mathcal U\) contains an \(\eta\) in none of them. \(\blacksquare\)

The rest of the lesson proves Proposition 1.4.

## 2. The set-up

Suppose that \(\mathcal A=\mathcal A_{M,q_0}\) is not nowhere dense in \(\mathcal U\). Then there is a nonempty open set \(\mathcal O\subseteq\mathcal U\) such that every nonempty open subset of \(\mathcal O\) meets \(\mathcal A\). We derive a contradiction. Fix \(\eta_*\in\mathcal O\), and let \(g_*=g_0+\eta_*\). By Lemma 1.1 there are \(m_0\) and \(\varrho_0>0\) with \(B_{m_0}(\eta_*,\varrho_0)\subseteq\mathcal O\). Let
\[
N=\max\{m_0,10\}+1 .
\]
Since \(\mathcal A\) is not empty and \(|q|\le\tfrac1{100}\) for admissible heights, \(|q_0|\le\tfrac1{20}\).

Let \(\mathfrak F\) be the set of the pairs \((g,z)\) with \(g=g_0+\eta\), \(\eta\in\mathcal A\), \(\|\eta-\eta_*\|_{C^8}\le\varrho_1\), and \(z\) a height of the class, where \(\varrho_1>0\) is so small that \(g(v,v)\ge c_g|v|^2\) for these metrics, with a number \(c_g>0\) depending on \(g_*\). These are pairs in the sense of the lesson on regularity on a cap, with the bound \(\max\{M,\|g_*\|_{C^8}+1\}\) and the number \(\min\{\tfrac1M,c_g\}\). In this lesson a number is called *controlled* if it depends only on \(h,\kappa,M,q_0,g_*\) and on the functions \(\chi_0,\varphi_0\) chosen below. Controlled numbers do not depend on \(\delta\) and \(\tau\).

We use the sheared coordinates \(\xi=x\), \(\theta=y+q_0x\) of the lesson on energy estimates.

**Lemma 2.1.** There is a controlled \(r>0\) with \(2Lr\le\tfrac1{10}\) such that for every pair of \(\mathfrak F\):

1. the slab \(\Sigma\) of the points with \(|\theta|\le r\), \(|\xi|\le Lr\) lies in \(\mathcal P\) and in an open set that is hyperbolic for the pair, with \(q_0\) and \(v_*\);
2. at every point of \(\Sigma\), the flow coordinate \(s\) of the lesson on regularity on a cap satisfies \(|s-\theta|\le\tfrac1{10}r\).

**Proof.** Let \(Q_1\) be a controlled bound for the first derivatives of \(q\), and \(\varrho_c=9/(100LQ_1)\). In the disk of radius \(\varrho_c\) around the origin, \(|q-q_0|\le\tfrac1{100L}+\varrho_cQ_1=\tfrac1{10L}\). Choose \(r\) with \(2Lr\le\min\{\tfrac1{10},\varrho_c\}\). A point of \(\Sigma\) has \(|x|\le Lr\) and \(|y|\le r+\tfrac1{20}Lr\), so it lies in the interior of \(\mathcal P\) and in that open disk; the hyperbolic open set is the intersection of the two. On \([-\tfrac15,\tfrac15]^2\) we have \(K<-\tfrac12\kappa\), \(E\ge\tfrac1M\) and \(H_{yy}^2\le M^2\), so \(-a=-KE/H_{yy}^2\ge\tfrac12\kappa M^{-3}=v_*^2\). This is (1). For (2), follow the integral curve of \(D=\partial_x-q\,\partial_y\) from a point of \(\Sigma\) to the line \(x=0\). Along it \(|x|\) decreases, \(y\) changes by at most \(\tfrac1{100}Lr\), so the curve stays in the disk, and \(\theta\) changes at the rate \(D\theta=q_0-q\), in total by at most \(Lr\cdot\tfrac1{10L}\). On the line \(x=0\), \(\theta=y=s\). \(\blacksquare\)

**The test metrics.** Fix a smooth function \(\chi_0\), not identically zero, that vanishes outside \((-\tfrac18Lr,\tfrac18Lr)\), and a smooth function \(\varphi_0\ge0\), not identically zero, that vanishes outside \((-1,1)\). For \(0<\delta\le1\) and integers \(\tau\ge1\) let
\[
\pi_\tau(\xi,\theta)=\tau^{-N}\,\chi_0(\xi)\,\varphi_0\bigl(\tfrac{\tau\theta}\delta\bigr)\cos(\tau\xi),
\]
and let \(\tilde\eta_\tau\) be \(\eta_*\) plus the symmetric matrix that in the coordinates \(\xi,\theta\) has the entry \(\pi_\tau\) at the place \(\theta\theta\) and \(0\) elsewhere. For \(\tau\ge\delta/r\) the function \(\pi_\tau\) vanishes outside \(\Sigma\), so then \(\tilde\eta_\tau\in\mathcal V\). A derivative of \(\pi_\tau\) of order \(k\) is at most a controlled multiple of \(\tau^{k-N}\delta^{-k}\). Since \(N>m_0\) and \(N>10\), for fixed \(\delta\) and large \(\tau\) we have \(\tilde\eta_\tau\in B_{m_0}(\eta_*,\varrho_0)\subseteq\mathcal O\), and \(\|\tilde\eta_\tau-\eta_*\|_{C^{10}}\to0\). The set \(B_\tau(\tilde\eta_\tau,\tau^{-\tau})\cap\mathcal O\) is open and not empty, so it contains a point of \(\mathcal A\): there is \(\eta_\tau\in\mathcal A\) with
\[
\|\eta_\tau-\tilde\eta_\tau\|_{C^\tau}\le\tau^{-\tau}.
\]
Let \(g_\tau=g_0+\eta_\tau\), and let \(z_\tau\) be a height of the class for \(g_\tau\). For large \(\tau\), \((g_\tau,z_\tau)\in\mathfrak F\). We write \(\epsilon_\tau=\eta_\tau-\tilde\eta_\tau\), so that in the coordinates \(\xi,\theta\)
\[
g_\tau=g_*+\pi_\tau\,d\theta^2+\epsilon_\tau ,
\]
where \(\pi_\tau\,d\theta^2\) stands for the matrix just described.

From here on \(\delta\) is fixed, and "for large \(\tau\)" means for all \(\tau\) from some number on, which may depend on \(\delta\). A quantity is \(O_\delta(\tau^{-k})\) if its absolute value is at most \(C\tau^{-k}\) for large \(\tau\) with a number \(C\) that may depend on \(\delta\), and \(o(1)\) if it tends to \(0\) as \(\tau\to\infty\).

## 3. Bounds at the edges of the strip

**Proposition 3.1.** For every \(j\ge0\) there is a number \(B_j\), which may depend on \(\delta\), such that for large \(\tau\) the functions \(\partial_\xi^jz_\tau\) and \(\partial_\xi^j\partial_\theta z_\tau\) are at most \(B_j\) in absolute value at the points with \(\theta=\pm\delta/\tau\) and \(|\xi|\le\tfrac34Lr\).

**Proof.** Let \(b_*=-\tfrac12r\) and \(\tau\ge4\delta/r\). The function \(\pi_\tau\) vanishes outside the set \(|\theta|\le\delta/\tau\), \(|\xi|\le\tfrac18Lr\), where \(|s|\le\tfrac14r+\tfrac1{10}r<\tfrac12r\) by Lemma 2.1. So on the images under the flow maps of the rectangles of the lower cap \((-2,2)\times(-2,b_*)\) and of the upper cap, \(g_\tau=g_*+\epsilon_\tau\). The derivatives of \(\epsilon_\tau\) of order at most \(k\) are at most \(1\) for \(\tau\ge k\); for the finitely many smaller \(\tau\) the metrics \(g_\tau\) are smooth. So the family \((g_\tau,z_\tau)\), for large \(\tau\), satisfies the assumption of Theorem 5.1 and Corollary 5.2 of the lesson on regularity on a cap, and all derivatives of \(z_\tau\) are bounded, independently of \(\tau\), on the images of the rectangles of the two caps.

By Lemma 2.1 the segment \(\theta=-r\), \(|\xi|\le Lr\) lies in the image of the rectangle \([-Lr,Lr]\times[-\tfrac{11}{10}r,-\tfrac9{10}r]\) of the lower cap. So assumption (3) of Section 4 of the lesson on energy estimates holds at \(\theta_0=-r\) with \(\xi_*=Lr\). Take \(\theta_1=-\delta/\tau\) and the trapezoid \(\mathcal T\) with \(\Lambda=\tfrac14L\); its intervals contain \(|\xi|\le\tfrac34Lr\). It lies in \(\Sigma\), which is hyperbolic, and on it \(g_\tau=g_*+\epsilon_\tau\), because \(\pi_\tau=0\) for \(\theta\le-\delta/\tau\). So the assumptions (1) to (4) hold, and Proposition 4.1 of that lesson gives the bounds at \(\theta=-\delta/\tau\). For \(\theta=+\delta/\tau\), start at \(\theta=r\) and let \(\theta\) decrease. \(\blacksquare\)

## 4. The comparison inside the strip

For a metric \(g\) in the coordinates \(\xi,\theta\), the height equation solved for \(z_{\theta\theta}\) is
\[
\begin{gathered}
z_{\theta\theta}=Q_g(\xi,\theta,p),\\
p=(z_\xi,z_\theta,z_{\theta\xi},z_{\xi\xi}),
\end{gathered}
\]
with
\[
Q_g=\Gamma^i_{\theta\theta}z_i+\frac{H_{\theta\xi}^2+\mathcal K_g\,(1-|dz|_g^2)}{H_{\xi\xi}},
\]
where \(\mathcal K_g=K_g\det g\); it is defined where \(H_{\xi\xi}\ne0\). This is the solved equation of the lesson on the differentiated height equation with the two coordinates exchanged, as in the lesson on energy estimates. For \(g=g_\tau\) and \(z=z_\tau\), by that lesson, \(\partial Q_{g_\tau}/\partial z_{\xi\xi}=S_1\) and \(\partial Q_{g_\tau}/\partial z_{\theta\xi}=P_1\) at the solution.

Let \(\Sigma_\tau\) be the strip \(|\theta|\le\delta/\tau\), \(|\xi|\le\tfrac34Lr\), and \(\theta'=\theta+\delta/\tau\). We write \(z=z_\tau\) and \(p\) for its vector of derivatives.

**Lemma 4.1.** For large \(\tau\) there is a smooth function \(z^0\) on \(\Sigma_\tau\), a polynomial of degree \(N+1\) in \(\theta'\) with coefficients that are functions of \(\xi\), such that:

1. \(z^0=z\) and \(\partial_\theta z^0=\partial_\theta z\) on the edge \(\theta'=0\);
2. every derivative of \(z^0\) is bounded on \(\Sigma_\tau\) by a number that does not depend on \(\tau\), and the derivatives of order at most \(4\) by a controlled number;
3. the function \(\varrho^0=z^0_{\theta\theta}-Q_{g_*}(\xi,\theta,p^0)\), where \(p^0\) is the vector of derivatives of \(z^0\), is \(O_\delta(\tau^{-N})\) on \(\Sigma_\tau\).

**Proof.** At the edge, \(g_\tau-g_*=\epsilon_\tau\) together with its derivatives, because \(\varphi_0\) vanishes near \(\pm1\). So \(H_{\xi\xi}\) formed with \(g_*\) and \(z\) differs by \(o(1)\) from \(H_{\xi\xi}\) formed with \(g_\tau\), which is \(d_0H_{yy}\) and at least \(\tfrac{99}{100}v_*^2/M\) in absolute value. Hence \(Q_{g_*}\) is defined near the vectors \(p\) at the edge, with bounded derivatives of every order.

Let \(c_0(\xi)=z\) and \(c_1(\xi)=\partial_\theta z\) at \(\theta'=0\). Since \(Q_{g_*}\) contains at most one derivative in \(\theta\), the derivative \(\partial_\theta^k\) at \(\theta'=0\) of \(Q_{g_*}(\xi,\theta,p[Z])\), for a function \(Z\), depends only on the derivatives \(\partial_\theta^iZ\) at \(\theta'=0\) with \(i\le k+1\). So one can define \(c_2,c_3,\dots,c_{N+1}\) one after the other: \(c_{k+2}\) is that derivative for \(Z=\sum_{i\le k+1}c_i\theta'^i/i!\). Let \(z^0=\sum_{i\le N+1}c_i\theta'^i/i!\). Then (1) holds, and \(\partial_\theta^k\varrho^0=0\) at \(\theta'=0\) for \(k\le N-1\).

The functions \(c_i\) are formed from derivatives of \(g_*\) and from derivatives along \(\xi\) of \(c_0\) and \(c_1\), which are bounded by Proposition 3.1; and \(c_0,\dots,c_4\) and their derivatives along \(\xi\) up to the total order \(4\) are formed from derivatives of \(z\) of order at most \(8\), which are bounded by \(M\). On \(\Sigma_\tau\), \(\theta'\le2\delta/\tau\), so the terms of \(z^0\) of higher degree contribute \(o(1)\) to the derivatives of order at most \(4\). This is (2). For large \(\tau\) the vectors \(p^0\) on \(\Sigma_\tau\) are within \(o(1)\) of their values at the edge, so \(\varrho^0\) is defined, and its derivative \(\partial_\theta^N\varrho^0\) is bounded independently of \(\tau\). By the formula of Taylor, \(|\varrho^0|\le\sup|\partial_\theta^N\varrho^0|\,(2\delta/\tau)^N/N!\). \(\blacksquare\)

**Lemma 4.2.** Let \(w=z-z^0\) on \(\Sigma_\tau\). For large \(\tau\),
\[
\begin{aligned}
&w_{\theta\theta}-P_2\,w_{\theta\xi}-S_2\,w_{\xi\xi}\\
&\quad=\beta^\theta w_\theta+\beta^\xi w_\xi+F_\tau-\varrho^0,
\end{aligned}
\]
where \(F_\tau=Q_{g_\tau}(\xi,\theta,p)-Q_{g_*}(\xi,\theta,p)\), and \(w=w_\theta=0\) on the edge \(\theta'=0\). There are controlled numbers \(s_2>0\) and \(\beta_2\) such that for large \(\tau\), on \(\Sigma_\tau\): \(S_2\ge s_2\), \(|P_2|+\sqrt{S_2}\le\tfrac12L\), and \(|\beta^\theta|,|\beta^\xi|,|\partial_\xi P_2|,|\partial_\xi S_2|,|\partial_\theta S_2|\le\beta_2\).

**Proof.** Subtract \(z^0_{\theta\theta}=Q_{g_*}(p^0)+\varrho^0\) from \(z_{\theta\theta}=Q_{g_\tau}(p)\):
\[
w_{\theta\theta}=F_\tau+\bigl(Q_{g_*}(p)-Q_{g_*}(p^0)\bigr)-\varrho^0 .
\]
On the edge \(p=p^0\), by Lemma 4.1 (1). The derivatives in \(\theta\) of \(p\) and \(p^0\) are derivatives of \(z\) and \(z^0\) of order at most \(3\), bounded by controlled numbers; so on \(\Sigma_\tau\) both vectors are within a controlled multiple of \(\delta/\tau\) of their common value at the edge, and for large \(\tau\) the segment between them lies where \(Q_{g_*}\) is defined. By the mean value theorem in integral form,
\[
\begin{aligned}
&Q_{g_*}(p)-Q_{g_*}(p^0)=\sum_i\mu_i\,(p_i-p^0_i),\\
&\mu_i=\int_0^1\frac{\partial Q_{g_*}}{\partial p_i}\bigl(p^0+\sigma(p-p^0)\bigr)\,d\sigma,
\end{aligned}
\]
and \(p-p^0=(w_\xi,w_\theta,w_{\theta\xi},w_{\xi\xi})\). This is the equation, with \(S_2\) and \(P_2\) the numbers \(\mu_i\) for \(p_i=z_{\xi\xi}\) and \(p_i=z_{\theta\xi}\). At the edge, \(\partial Q_{g_*}/\partial z_{\xi\xi}\) at \(p\) differs by \(o(1)\) from \(\partial Q_{g_\tau}/\partial z_{\xi\xi}=S_1\ge s_{\min}\), because \(g_\tau-g_*=\epsilon_\tau\) there; and in the same way for \(P_1\). The derivatives of \(Q_{g_*}\) are bounded, so on \(\Sigma_\tau\) the integrands of the \(\mu_i\) differ from these values by \(o(1)\). With Lemma 1.1 of the lesson on energy estimates this gives \(S_2\ge\tfrac12s_{\min}\) and \(|P_2|+\sqrt{S_2}\le\tfrac14L+o(1)\le\tfrac12L\) for large \(\tau\). The derivatives of \(P_2,S_2\) are integrals of second derivatives of \(Q_{g_*}\) times first derivatives of \(p\) and \(p^0\), which are bounded by controlled numbers by Lemma 4.1 (2) and the bound \(M\). \(\blacksquare\)

## 5. The forcing

**Lemma 5.1.** For a metric \(g\) in coordinates numbered \(1,2\),
\[
\begin{aligned}
K\det g&=\partial_1\partial_2g_{12}-\tfrac12\partial_1^2g_{22}\\
&\quad-\tfrac12\partial_2^2g_{11}+\mathcal L,
\end{aligned}
\]
where \(\mathcal L\) is a polynomial in the first derivatives of \(g\) whose coefficients are polynomials in the entries of \(g\) divided by \(\det g\).

**Proof.** By the proof of Lemma 2.1 of the lesson on the differentiated height equation, \(K\det g=R_{1221}=\partial_1\Gamma_{22,1}-\partial_2\Gamma_{12,1}\) plus products of two symbols \(\Gamma_{ki,s}\) and \(\Gamma^m_{ji}\), and \(\Gamma_{22,1}=\partial_2g_{12}-\tfrac12\partial_1g_{22}\), \(\Gamma_{12,1}=\tfrac12\partial_2g_{11}\). \(\blacksquare\)

**Lemma 5.2.** On \(\Sigma_\tau\), for large \(\tau\),
\[
\begin{aligned}
F_\tau&=\tau^{2-N}\,D_\tau\,\chi_0(\xi)\,\varphi_0\bigl(\tfrac{\tau\theta}\delta\bigr)\cos(\tau\xi)\\
&\quad+O_\delta(\tau^{1-N}),
\end{aligned}
\]
where
\[
D_\tau=\frac{1-|dz|_{g_*}^2}{2\,H^*_{\xi\xi}},
\]
with \(H^*_{\xi\xi}\) formed with \(g_*\) and \(z\). There are controlled numbers \(0<c_D\le C_D\) with \(c_D\le|D_\tau|\le C_D\), and \(D_\tau\) has one sign on \(\Sigma_\tau\).

**Proof.** \(Q_g\) is a function of the entries of \(g\), of their first derivatives, of \(\mathcal K_g\) and of \(p\); it is a polynomial of degree one in \(\mathcal K_g\) with the coefficient \((1-|dz|_g^2)/H_{\xi\xi}\). On \(\Sigma_\tau\), \(g_\tau-g_*=\pi_\tau\,d\theta^2+\epsilon_\tau\). The entries of this difference and their first derivatives are \(O_\delta(\tau^{1-N})\). Only the entry \(g_{\theta\theta}\) is changed by \(\pi_\tau\), so by Lemma 5.1, with \(\xi,\theta\) numbered \(1,2\),
\[
\begin{aligned}
&\mathcal K_{g_\tau}-\mathcal K_{g_*}\\
&\quad=-\tfrac12\partial_\xi^2\pi_\tau+O_\delta(\tau^{1-N})\\
&\quad=\tfrac12\tau^{2-N}\chi_0\,\varphi_0\bigl(\tfrac{\tau\theta}\delta\bigr)\cos(\tau\xi)\\
&\qquad+O_\delta(\tau^{1-N});
\end{aligned}
\]
the derivatives of \(\pi_\tau\) in which \(\chi_0\) is differentiated are \(O(\tau^{1-N})\), and the change of \(\mathcal L\) is \(O_\delta(\tau^{1-N})\). Changing first \(g\) and its first derivatives, with \(\mathcal K_{g_\tau}\) fixed and bounded, changes \(Q\) by \(O_\delta(\tau^{1-N})\); changing then \(\mathcal K\) changes it by the coefficient formed with \(g_*\) times \(\mathcal K_{g_\tau}-\mathcal K_{g_*}\). This is the formula.

The numerator of \(D_\tau\) differs by \(o(1)\) from \(E/\det g\) formed with \(g_\tau\), which is at least a controlled positive number, since \(E\ge\tfrac1M\). The denominator differs by \(o(1)\) from \(2d_0H_{yy}\), whose absolute value lies between two controlled positive numbers. So the bounds hold for large \(\tau\), and \(D_\tau\) is continuous and without zeros on the connected set \(\Sigma_\tau\). \(\blacksquare\)

## 6. The moment

**Proof of Proposition 1.4.** We continue with the set-up of Section 2 and show that it is contradictory if \(\delta\) is small.

*The size of \(w\).* Apply Lemma 2.1 of the lesson on energy estimates to \(w\) on the trapezoid with \(\theta_0=-\delta/\tau\), \(\theta_1=\delta/\tau\), \(\xi_*=\tfrac34Lr\) and \(\Lambda=\tfrac12L\). Its intervals \(J_\theta\) contain \([-\tfrac18Lr,\tfrac18Lr]\) for large \(\tau\). By Lemma 4.2 the assumptions hold with controlled numbers, and the energy of \(w\) vanishes at \(\theta_0\). By Lemma 5.2 and Lemma 4.1 (3), the mean square of \(F_\tau-\varrho^0\) over \(J_\theta\) is at most \((C_D\|\chi_0\|\sup\varphi_0+o(1))^2\tau^{4-2N}\), where \(\|\chi_0\|^2=\int\chi_0^2\). The length of the interval of \(\theta\) is \(2\delta/\tau\). So for large \(\tau\) and all \(\theta\) of the strip
\[
\begin{aligned}
&\Bigl(\int_{J_\theta}(w_\theta^2+w_\xi^2)\,d\xi\Bigr)^{1/2}\\
&\quad\le(C_5+o(1))\,\delta\,\tau^{1-N},
\end{aligned}
\]
with a controlled \(C_5\).

*The moment.* Let \(\psi_\tau(\xi)=\chi_0(\xi)\cos(\tau\xi)\). Multiply the equation of Lemma 4.2 by \(\psi_\tau\) and integrate over \(|\theta|\le\delta/\tau\) and over \(\xi\). We estimate the terms.

(i) Since \(w_\theta=0\) at \(\theta'=0\), the integral of \(\psi_\tau w_{\theta\theta}\) is \(\int\chi_0(\xi)\cos(\tau\xi)\,w_\theta(\xi,\delta/\tau)\,d\xi\). By Proposition 3.1 and Lemma 4.1 (2), the function \(w_\theta(\cdot,\delta/\tau)\) has derivatives along \(\xi\) of every order bounded independently of \(\tau\). Integrating by parts \(N\) times, each time integrating the factor \(\cos(\tau\xi)\) or \(\sin(\tau\xi)\), shows that the integral is \(O_\delta(\tau^{-N})\).

(ii) In the integral of \(\psi_\tau P_2w_{\theta\xi}\) integrate by parts in \(\xi\): it is minus the integral of \(\partial_\xi(\psi_\tau P_2)\,w_\theta\). The derivative is at most \(\tau\sup|\chi_0|\cdot\tfrac12L\) plus a controlled number. By the bound for \(w\) and the inequality of Cauchy and Schwarz, the integral of \(|w_\theta|\) over the strip and over the support of \(\chi_0\), which lies in an interval of length \(\tfrac14Lr\), is at most
\[
\frac{2\delta}\tau\,\bigl(\tfrac14Lr\bigr)^{1/2}(C_5+o(1))\,\delta\,\tau^{1-N}.
\]
Multiplied by the bound for the derivative, this is \((C_6+o(1))\,\delta^2\tau^{1-N}\) with a controlled \(C_6\). The integral of \(\psi_\tau S_2w_{\xi\xi}\) is bounded in the same way, with \(S_2\le\tfrac14L^2\) in the place of \(|P_2|\le\tfrac12L\) and \(w_\xi\) in the place of \(w_\theta\); we take \(C_6\) so large that it serves for both. The integrals of \(\psi_\tau\beta^\theta w_\theta\) and \(\psi_\tau\beta^\xi w_\xi\) have no factor \(\tau\) and are \(O(\delta^2\tau^{-N})\).

(iii) By Lemma 5.2 the integral of \(\psi_\tau F_\tau\) is \(\tau^{2-N}\mathcal J_\tau+O_\delta(\tau^{-N})\), where
\[
\mathcal J_\tau=\iint D_\tau\,\chi_0^2\,\varphi_0\bigl(\tfrac{\tau\theta}\delta\bigr)\cos^2(\tau\xi)\,d\xi\,d\theta .
\]
Since \(D_\tau\) has one sign and \(|D_\tau|\ge c_D\), and \(\varphi_0\ge0\), the absolute value of \(\mathcal J_\tau\) is at least
\[
c_D\int\varphi_0\bigl(\tfrac{\tau\theta}\delta\bigr)\,d\theta\cdot\int\chi_0^2\cos^2(\tau\xi)\,d\xi .
\]
The first integral is \(\tfrac\delta\tau\int\varphi_0\). The second is \(\tfrac12\int\chi_0^2+\tfrac12\int\chi_0^2\cos(2\tau\xi)\,d\xi\), and the last integral is \(O(\tau^{-1})\) by one integration by parts. So the integral of \(\psi_\tau F_\tau\) is at least \((c_3+o(1))\,\delta\,\tau^{1-N}\) in absolute value, with the controlled number \(c_3=\tfrac12c_D\int\varphi_0\int\chi_0^2>0\).

(iv) The integral of \(\psi_\tau\varrho^0\) is \(O_\delta(\tau^{-N-1})\).

The equation gives that the integral in (iii) equals the sum of the integrals in (i), (ii) and (iv) with signs. Hence, for large \(\tau\),
\[
\begin{aligned}
&(c_3+o(1))\,\delta\,\tau^{1-N}\\
&\quad\le(2C_6+o(1))\,\delta^2\tau^{1-N}+O_\delta(\tau^{-N}).
\end{aligned}
\]
Divide by \(\delta\tau^{1-N}\) and let \(\tau\to\infty\): \(c_3\le2C_6\,\delta\). The numbers \(c_3\) and \(C_6\) are controlled, so they do not depend on \(\delta\). Choosing \(\delta<c_3/(2C_6)\) at the beginning of Section 2 gives a contradiction. So \(\mathcal A_{M,q_0}\) is nowhere dense in \(\mathcal U\). \(\blacksquare\)

The order of the choices is: first the class, the open set \(\mathcal O\), the metric \(g_*\), the slab and the functions \(\chi_0,\varphi_0\), which determine \(c_3\) and \(C_6\); then \(\delta\); then \(\tau\to\infty\). The forcing by the oscillation is linear in the width \(\delta\) of the strip, and the response of all other terms is quadratic, because the difference \(w\) is itself produced by the forcing during the passage through the strip.

With Theorem 1.3 the assumption (P) of Theorem 5.1 and Corollary 6.1 of the lesson on the metric and the theorem is proved. So there is a smooth metric on \((-1,1)^2\), with the Taylor series of the Euclidean metric at the origin, such that no neighbourhood of the origin has a smooth isometric immersion into \(\mathbb R^3\).

## 7. Exercises

**7.1.** Show that a derivative of \(\pi_\tau\) with \(i\) differentiations in \(\xi\) and \(k\) in \(\theta\) is at most \(C\,\tau^{i+k-N}\delta^{-k}\) in absolute value, with \(C\) depending on \(\chi_0,\varphi_0,i,k\), and that \(\pi_\tau\to0\) in the norm \(\|\cdot\|_{C^m}\) for every \(m<N\) but not for \(m=N\) in general.

**7.2.** Let \(f\) be a smooth function on \(\mathbb R\) that vanishes outside a bounded interval. Show that \(\int f(\xi)\cos(\tau\xi)\,d\xi\) is at most \(\tau^{-k}\int|f^{(k)}|\) in absolute value, for every \(k\).

**7.3.** Where does the proof of Proposition 1.4 use that the perturbation oscillates along the strip, and not across it?

**7.4.** In the set-up of Section 2, why is it necessary to approximate the test metrics by metrics of the class, and to which order of derivatives is the approximation needed?

## 8. Solutions

**7.1.** Each differentiation in \(\xi\) falls on \(\chi_0\) or on \(\cos(\tau\xi)\) and gives at most a factor \(\tau\) times a bound for derivatives of \(\chi_0\); each differentiation in \(\theta\) gives a factor \(\tau/\delta\) and a derivative of \(\varphi_0\). So \(\|\pi_\tau\|_{C^m}\le C\tau^{m-N}\delta^{-m}\to0\) for \(m<N\). For \(m=N\), the derivative \(\partial_\xi^N\) contains the term \(\pm\chi_0\varphi_0\cos(\tau\xi)\) or \(\pm\chi_0\varphi_0\sin(\tau\xi)\) without a power of \(\tau\), which does not tend to \(0\).

**7.2.** Integrate by parts \(k\) times, each time integrating the trigonometric factor, which gives a factor \(1/\tau\), and differentiating \(f\). There are no terms at the ends because \(f\) vanishes there. The last integrand is \(f^{(k)}\) times \(\pm\cos(\tau\xi)\) or \(\pm\sin(\tau\xi)\) times \(\tau^{-k}\).

**7.3.** In three places. The second derivative along the strip, \(\partial_\xi^2\pi_\tau\), is the term of the curvature that gains the factor \(\tau^2\) (Lemma 5.2); a second derivative across the strip of the entry \(g_{\theta\theta}\) does not occur in Lemma 5.1. The test function \(\psi_\tau\) oscillates along the strip with the same frequency, so its product with the forcing has a mean that does not vanish, while its product with a function with bounded derivatives along \(\xi\) is small, as in (i). And the bounds of Proposition 3.1 are bounds for derivatives along \(\xi\) at the edges; they hold because outside the strip the metric does not oscillate.

**7.4.** The assumption to be refuted concerns metrics of the class, which have a height with the bounds; a test metric is only known to lie in \(\mathcal O\), not in \(\mathcal A\). The approximation must be so close that the two cap regions and the regions between the cuts and the strip have bounds of every order independent of \(\tau\), and that the error is negligible against \(\tau^{1-N}\) in the forcing. An error of size \(\tau^{-\tau}\) in the norm \(C^\tau\) gives both, because for every fixed order \(k\) and large \(\tau\) it bounds the derivatives of order \(k\) of the error by \(\tau^{-\tau}\).

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026

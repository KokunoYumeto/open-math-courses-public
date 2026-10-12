# Energy estimates where the curvature is negative

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Where the curvature is negative the height equation is hyperbolic: it can be solved for the second derivative in one direction, and that direction plays the role of time. This lesson proves the energy estimate for the resulting equations and uses it to carry bounds for all derivatives of a solution from one line \(\theta=\theta_0\) to the lines \(\theta>\theta_0\), as long as the metric has bounds for all its derivatives. In the proof of the patch obstruction, this carries the bounds of the lesson on regularity on a cap through the central region of the model square, up to the edge of a thin strip where the metric oscillates.

- In coordinates \(\xi,\theta\) obtained by a shear, the derivatives \(v=\partial_\xi^jz\) of a solution satisfy an equation \(v_{\theta\theta}-P_1v_{\theta\xi}-S_1v_{\xi\xi}=\dots\) with \(S_1>0\) (Proposition 1.2).
- The energy inequality on intervals that shrink at the speed of propagation (Lemma 2.1).
- Bounds for all derivatives along \(\xi\) of \(z\) and \(z_\theta\) propagate in \(\theta\) (Proposition 4.1).

The lesson follows [OpenAI-I, Section 4, the parts on the bounded solution class and on the propagation to the pulse]. It uses the equation for a derivative of high order from [The differentiated height equation](the-differentiated-height-equation.md) and the notion of a pair from [Regularity on a cap](regularity-on-a-cap.md).

## 1. Sheared coordinates

Let \((g,z)\) be a pair in the sense of the lesson on regularity on a cap, with the numbers \(h,\kappa,M,c\), and \(q=H_{xy}/H_{yy}\), \(G=E/H_{yy}^2\), \(a=KG\). Let \(q_0\) be a real number with \(|q_0|\le\tfrac1{20}\). The *sheared coordinates* are
\[
\xi=x,\qquad\theta=y+q_0x .
\]
The map \(\Psi(\xi,\theta)=(\xi,\theta-q_0\xi)\) is affine with the matrix whose columns are \((1,-q_0)\) and \((0,1)\), of determinant \(1\). We pull back \(g\) and \(z\) by \(\Psi\) as in Lemma 1.2 of the lesson on heights and denote the pulled-back metric and the function \(z\circ\Psi\) again by \(g\) and \(z\), and the functions \(K,E,q,a\) composed with \(\Psi\) by the same letters. The indices \(\xi,\theta\) refer to the new coordinates. By that lemma the height equation holds in the new coordinates, with the same \(K\) and \(E\), and the covariant Hessian is
\[
\begin{gathered}
H_{\theta\theta}=H_{yy},\qquad H_{\xi\theta}=(q-q_0)\,H_{yy},\\
H_{\xi\xi}=d_0\,H_{yy},\qquad d_0=(q-q_0)^2+a .
\end{gathered}
\]
Indeed \(H_{\xi\theta}=H_{xy}-q_0H_{yy}\) and \(H_{\xi\xi}=H_{xx}-2q_0H_{xy}+q_0^2H_{yy}\), and \(H_{xx}=(q^2+a)H_{yy}\) by the height equation.

Let \(v_*>0\) and \(L=100(1+1/v_*)\). We say that a set in the plane of the coordinates \(\xi,\theta\) is *hyperbolic for the pair* (with \(q_0\) and \(v_*\)) if at its points
\[
\begin{gathered}
K<0,\qquad-a\ge v_*^2,\\
|q-q_0|\le\frac1{10L}.
\end{gathered}
\]

**Lemma 1.1.** On a hyperbolic set, \(d_0\le-\tfrac{99}{100}v_*^2\). The functions
\[
P_1=\frac{2(q-q_0)}{d_0},\qquad S_1=-\frac1{d_0}
\]
satisfy \(S_1>0\) and \(|P_1|+\sqrt{S_1}\le\tfrac14L\). There is a controlled number \(s_{\min}>0\) with \(S_1\ge s_{\min}\).

**Proof.** Since \(L\ge100/v_*\), \(|q-q_0|\le v_*/1000\), so \(d_0\le v_*^2/10^6-v_*^2\). Then \(S_1\le\tfrac{100}{99}v_*^{-2}\), \(\sqrt{S_1}\le1.01/v_*\), and \(|P_1|\le2\cdot\tfrac{v_*}{1000}\cdot\tfrac{100}{99v_*^2}<0.01/v_*\); the sum is less than \(2/v_*\le\tfrac14L\). Finally \(|d_0|\le1+|a|\), and \(|a|\) is bounded by a controlled number. \(\blacksquare\)

**Proposition 1.2.** Let \(j\ge3\) and \(v=\partial_\xi^jz\). On an open hyperbolic set,
\[
\begin{aligned}
&v_{\theta\theta}-P_1\,v_{\theta\xi}-S_1\,v_{\xi\xi}\\
&\quad=b^\theta v_\theta+b^\xi v_\xi+\tilde R_j,
\end{aligned}
\]
where \(b^\theta,b^\xi\) are bounded by controlled numbers, depending also on \(j\), and the remainder \(\tilde R_j\) is a sum of terms
\[
c\cdot\partial_\xi^{k_1}\tilde p_{i_1}\cdots\partial_\xi^{k_n}\tilde p_{i_n},
\]
with \(\tilde p=(z_\theta,z_\xi,z_{\theta\xi},z_{\xi\xi})\), in which \(1\le k_i\le j-1\), the sum of the \(k_i\) is at most \(j\), at most the factors \(\partial_\xi^{j-1}z_\theta\) and \(\partial_\xi^{j-1}z_\xi\) have \(k_i=j-1\), and each \(c\) is a quotient of polynomials in the derivatives of \(g\) of order at most \(j+3\) and in \(\tilde p\), with a denominator that is a power of \(\det g\) and of \(H_{\xi\xi}\).

**Proof.** Exchange the two coordinates: let \(\tilde x=\theta\) and \(\tilde y=\xi\). This is again an affine change of coordinates, so the height equation holds in the coordinates \(\tilde x,\tilde y\), and \(H_{\tilde y\tilde y}=H_{\xi\xi}=d_0H_{yy}\ne0\) on a hyperbolic set. So the lesson on the differentiated height equation applies with \(\tilde x,\tilde y\) in the place of \(x,y\). Its quantities are
\[
\begin{gathered}
\tilde q=\frac{H_{\theta\xi}}{H_{\xi\xi}}=\frac{q-q_0}{d_0},\\
\tilde G=\frac E{H_{\xi\xi}^2},\qquad\tilde a=K\tilde G=\frac a{d_0^2},
\end{gathered}
\]
and \(\tilde D=\partial_\theta-\tilde q\,\partial_\xi\). By Theorem 5.1 of that lesson, for \(v=\partial_\xi^jz\),
\[
\tilde D^2v+\tilde a\,v_{\xi\xi}+\tilde B\,\tilde Dv+\tilde c\,v_\xi=\tilde R_j,
\]
with bounded \(\tilde B\) and \(\tilde c\), and with the remainder described there. Since \(\tilde D^2v=v_{\theta\theta}-2\tilde qv_{\theta\xi}+\tilde q^2v_{\xi\xi}-(\tilde D\tilde q)v_\xi\), the second-order part is \(v_{\theta\theta}-2\tilde q\,v_{\theta\xi}+(\tilde q^2+\tilde a)v_{\xi\xi}\), and
\[
\begin{gathered}
2\tilde q=P_1,\\
\tilde q^2+\tilde a=\frac{(q-q_0)^2+a}{d_0^2}=\frac1{d_0}=-S_1 .
\end{gathered}
\]
The terms of first order give \(b^\theta=-\tilde B\) and \(b^\xi=\tilde B\tilde q+\tilde D\tilde q-\tilde c\). They are formed from derivatives of \(g\) of order at most \(3\) and of \(z\) of order at most \(4\), with denominators that are powers of \(\det g\), \(H_{yy}\) and \(d_0\), and \(|d_0|\ge\tfrac{99}{100}v_*^2\). The description of the remainder is that of Theorem 5.1 and Lemma 4.1 of the lesson on the differentiated height equation: the two terms \(j\,\partial_\xi[\,\cdot\,]\,\partial_\xi^{j-1}z_\theta\) and \(j\,\partial_\xi[\,\cdot\,]\,\partial_\xi^{j-1}z_\xi\), and a sum of terms with \(k_i\le j-2\). \(\blacksquare\)

The roles of the two coordinates are now exchanged with respect to the caps: there the equation was solved for \(z_{xx}\) and differentiated in \(y\); here it is solved for \(z_{\theta\theta}\), which is possible because \(H_{\xi\xi}\ne0\) where the curvature is negative, and differentiated in \(\xi\). All the factors \(\partial_\xi^k\tilde p_i\) are derivatives along \(\xi\) of the two functions \(z_\xi\) and \(z_\theta\).

## 2. The energy inequality

Let \(\theta_0<\theta_1\), \(\xi_*>0\) and \(\Lambda>0\) with \(\xi_*-\Lambda(\theta_1-\theta_0)>0\). Let \(\beta(\theta)=\xi_*-\Lambda(\theta-\theta_0)\) and
\[
\mathcal T=\{(\xi,\theta):\theta_0\le\theta\le\theta_1,\ |\xi|\le\beta(\theta)\},
\]
a trapezoid whose sides move inwards with the speed \(\Lambda\). We write \(J_\theta=[-\beta(\theta),\beta(\theta)]\).

**Lemma 2.1.** Let \(P_1,S_1,b^\theta,b^\xi,R,v\) be smooth functions on a neighbourhood of \(\mathcal T\) with
\[
\begin{aligned}
&v_{\theta\theta}-P_1\,v_{\theta\xi}-S_1\,v_{\xi\xi}\\
&\quad=b^\theta v_\theta+b^\xi v_\xi+R .
\end{aligned}
\]
Suppose that on \(\mathcal T\): \(S_1\ge s_{\min}>0\), \(|P_1|+\sqrt{S_1}\le\Lambda\), and \(|b^\theta|,|b^\xi|,|\partial_\xi P_1|,|\partial_\xi S_1|,|\partial_\theta S_1|\le\beta_1\). Let
\[
\begin{gathered}
\mathcal E(\theta)=\frac12\int_{J_\theta}\bigl(v_\theta^2+S_1v_\xi^2\bigr)\,d\xi,\\
\varrho(\theta)=\Bigl(\int_{J_\theta}R^2\,d\xi\Bigr)^{1/2}.
\end{gathered}
\]
Then, with \(c_E=3\beta_1(1+1/s_{\min})\), for \(\theta_0\le\theta\le\theta_1\),
\[
\begin{aligned}
\sqrt{\mathcal E(\theta)}\le e^{c_E(\theta-\theta_0)}\Bigl(&\sqrt{\mathcal E(\theta_0)}\\
&+\int_{\theta_0}^\theta\varrho(\theta')\,d\theta'\Bigr).
\end{aligned}
\]

**Proof.** Let \(e=\tfrac12(v_\theta^2+S_1v_\xi^2)\) and \(\jmath=\tfrac12P_1v_\theta^2+S_1v_\xi v_\theta\). Carrying out the differentiations,
\[
\begin{aligned}
&\partial_\theta e-\partial_\xi\jmath\\
&\quad=v_\theta\bigl(v_{\theta\theta}-P_1v_{\theta\xi}-S_1v_{\xi\xi}\bigr)\\
&\qquad+\tfrac12\partial_\theta S_1\,v_\xi^2-\tfrac12\partial_\xi P_1\,v_\theta^2\\
&\qquad-\partial_\xi S_1\,v_\xi v_\theta .
\end{aligned}
\]
Since \(|S_1v_\xi v_\theta|\le\sqrt{S_1}\cdot\tfrac12(S_1v_\xi^2+v_\theta^2)\), we have \(|\jmath|\le(|P_1|+\sqrt{S_1})\,e\le\Lambda e\). Let \(e_+\) and \(e_-\) be the values of \(e\) at the two ends \(\xi=\pm\beta(\theta)\) of the interval. The derivative of \(\mathcal E\) is
\[
\mathcal E'(\theta)=\int_{J_\theta}\partial_\theta e\,d\xi-\Lambda\,(e_++e_-),
\]
and \(\int_{J_\theta}\partial_\xi\jmath\,d\xi\) is the difference of the values of \(\jmath\) at the two ends, which is at most \(\Lambda(e_++e_-)\). So the terms at the two ends of the interval are together not positive, and
\[
\mathcal E'(\theta)\le\int_{J_\theta}\bigl(\partial_\theta e-\partial_\xi\jmath\bigr)\,d\xi .
\]
Insert the equation for \(v\). With \(v_\xi^2\le S_1v_\xi^2/s_{\min}\) and \(|v_\xi v_\theta|\le\tfrac12(v_\theta^2+v_\xi^2)\), the terms without \(R\) are at most \(2c_E\,e\) at every point, and \(\int|v_\theta R|\le\sqrt{2\mathcal E}\,\varrho\). Hence \(\mathcal E'\le2c_E\mathcal E+\sqrt{2\mathcal E}\,\varrho\).

For \(\eta>0\) the function \(w=\sqrt{\mathcal E+\eta}\) is differentiable, and \(w'=\mathcal E'/(2w)\le c_Ew+\varrho\). So \((e^{-c_E(\theta-\theta_0)}w)'\le\varrho\), and \(w(\theta)\le e^{c_E(\theta-\theta_0)}(w(\theta_0)+\int_{\theta_0}^\theta\varrho)\). Let \(\eta\to0\). \(\blacksquare\)

The condition \(|P_1|+\sqrt{S_1}\le\Lambda\) says that the sides of the trapezoid move inwards at least as fast as the equation propagates. Then no information from outside the interval \(J_{\theta_0}\) is needed.

## 3. A Sobolev inequality on an interval

**Lemma 3.1.** Let \(\phi\) be a smooth function on an interval \(J\) of length \(|J|\). Then for every \(x_0\in J\)
\[
\phi(x_0)^2\le\frac2{|J|}\int_J\phi^2+2|J|\int_J\phi'^2 .
\]

**Proof.** For \(x\in J\), \(\phi(x_0)=\phi(x)-\int_{x_0}^x\phi'\), so \(\phi(x_0)^2\le2\phi(x)^2+2|J|\int_J\phi'^2\). Take the mean over \(x\in J\). \(\blacksquare\)

## 4. Propagation of bounds

For a pair, \(j\ge0\) and \(\theta\in[\theta_0,\theta_1]\), let
\[
\begin{aligned}
\mathcal I_j(\theta)=\int_{J_\theta}\bigl(&(\partial_\xi^jz_\theta)^2\\
&+(\partial_\xi^jz_\xi)^2\bigr)\,d\xi .
\end{aligned}
\]
In this section a family of pairs is given, with a common number \(q_0\), and a trapezoid \(\mathcal T\) as in Section 2 with \(\Lambda=\tfrac14L\), in the coordinates \(\xi,\theta\), such that:

1. \(\mathcal T\) lies in a hyperbolic open set of every pair of the family, with common \(q_0\) and \(v_*\);
2. for every \(k\ge0\) there is a number \(N_k\) such that for every pair the derivatives of the entries of \(g\) of order at most \(k\) are at most \(N_k\) in absolute value on \(\mathcal T\);
3. for every \(j\ge0\) there is a number \(I_j\) such that \(\mathcal I_j(\theta_0)\le I_j\) for every pair;
4. the length \(2\beta(\theta_1)\) of the shortest interval is at least \(\ell_0>0\), and \(\theta_1-\theta_0\le1\).

A number is called controlled if it depends only on \(h,\kappa,M,c,v_*,\ell_0\), the numbers \(N_k\) and \(I_j\), and the orders named.

**Proposition 4.1.** For every \(j\ge0\) there is a controlled number \(I'_j\) such that \(\mathcal I_j(\theta)\le I'_j\) for every pair of the family and every \(\theta\in[\theta_0,\theta_1]\).
Consequently the functions \(\partial_\xi^jz_\theta\) and \(\partial_\xi^jz_\xi\) are bounded on \(\mathcal T\) by controlled numbers, for every \(j\).

**Proof.** The second statement follows from the first by Lemma 3.1, applied on the intervals \(J_\theta\), whose lengths are between \(\ell_0\) and \(2\xi_*\). We prove the first by induction on \(j\). For \(j\le6\) the integrands are bounded by controlled numbers, because the derivatives of \(z\) of order at most \(8\) are bounded by \(M\) and the change of coordinates is a fixed shear.

Let \(j\ge7\), and suppose the statement holds for all smaller orders. Let \(v=\partial_\xi^jz\). By Proposition 1.2 and Lemma 1.1 the assumptions of Lemma 2.1 hold on \(\mathcal T\), with \(\Lambda=\tfrac14L\), with \(R=\tilde R_j\) and with controlled \(s_{\min}\) and \(\beta_1\); the derivatives of \(P_1\) and \(S_1\) are formed from derivatives of \(g\) of order at most \(3\) and of \(z\) of order at most \(4\). We bound \(\varrho(\theta)\). Each factor \(\partial_\xi^k\tilde p_i\) of a term of \(\tilde R_j\) is a derivative along \(\xi\) of \(z_\xi\) or \(z_\theta\) of order at most \(k+1\le j\); the order \(j\) occurs only if \(k=j-1\) and \(\tilde p_i\) is \(z_{\theta\xi}\) or \(z_{\xi\xi}\), which is excluded by Proposition 1.2. So all orders are at most \(j-1\). A factor of order \(j-1\) has \(k\ge j-2\), and two such factors in one term would give a sum of at least \(2j-4>j\). So in every term at most one factor has the order \(j-1\); its mean square over \(J_\theta\) is at most \(I'_{j-1}\). All other factors have order at most \(j-2\), and by Lemma 3.1 and the induction hypothesis for the orders up to \(j-1\) they are bounded on \(J_\theta\). The coefficients \(c\) are bounded by assumption (2), by the bounds for \(\tilde p\), and by \(|H_{\xi\xi}|\ge\tfrac{99}{100}v_*^2c\). So \(\varrho(\theta)\le\varrho_j\) with a controlled \(\varrho_j\).

The energy of \(v\) at \(\theta_0\) is at most \(\tfrac12(1+S_{\max})I_j\), where \(S_{\max}=\tfrac{100}{99}v_*^{-2}\) bounds \(S_1\). By Lemma 2.1 and \(\theta_1-\theta_0\le1\),
\[
\sqrt{\mathcal E(\theta)}\le e^{c_E}\Bigl(\sqrt{\tfrac12(1+S_{\max})I_j}+\varrho_j\Bigr),
\]
and \(v_\theta^2+v_\xi^2\le2(1+1/s_{\min})\,e\), where \(v_\theta=\partial_\xi^jz_\theta\) and \(v_\xi=\partial_\xi^jz_\xi\). \(\blacksquare\)

The statement and the proof are the same if \(\theta\) decreases from \(\theta_0\): replace \(\theta\) by \(-\theta\), which changes the sign of \(P_1\) and leaves \(S_1\) unchanged.

Assumption (2) is essential, and it is the reason why the proposition cannot be continued through a region where the metric oscillates rapidly: there the numbers \(N_k\) grow with the frequency. In the proof of the patch obstruction the propagation is stopped at the edge of such a region, and what happens inside is compared with a solution for a metric without the oscillation.

## 5. Exercises

**5.1.** Verify the identity for \(\partial_\theta e-\partial_\xi\jmath\) in the proof of Lemma 2.1.

**5.2.** For the wave equation \(v_{\theta\theta}-v_{\xi\xi}=0\), which is the case \(P_1=0\), \(S_1=1\), find the smallest \(\Lambda\) allowed in Lemma 2.1, and show by the example \(v=\phi(\xi+\theta)\) that the energy on intervals that shrink more slowly can increase.

**5.3.** Show that on a hyperbolic set the matrix of the Hessian in the sheared coordinates has a negative determinant, and that \(H_{\xi\xi}\) and \(H_{\theta\theta}\) have opposite signs.

**5.4.** In the proof of Proposition 4.1, why can the induction start only at an order that is covered by the bounds of order eight, and where is \(j\ge7\) used?

## 6. Solutions

**5.1.** By the product rule,
\[
\begin{aligned}
\partial_\theta e&=v_\theta v_{\theta\theta}+S_1v_\xi v_{\xi\theta}+\tfrac12\partial_\theta S_1\,v_\xi^2,\\
\partial_\xi\jmath&=\tfrac12\partial_\xi P_1\,v_\theta^2+P_1v_\theta v_{\theta\xi}\\
&\quad+\partial_\xi S_1\,v_\xi v_\theta+S_1v_{\xi\xi}v_\theta\\
&\quad+S_1v_\xi v_{\theta\xi}.
\end{aligned}
\]
In the difference the terms \(S_1v_\xi v_{\xi\theta}\) cancel, and the rest is the right side.

**5.2.** \(|P_1|+\sqrt{S_1}=1\), so \(\Lambda\ge1\) is required. For \(v=\phi(\xi+\theta)\), \(e=\phi'(\xi+\theta)^2\), and the energy on \(|\xi|\le\xi_*-\Lambda\theta\) is the integral of \(\phi'^2\) over \([-\xi_*+(1+\Lambda)\theta,\ \xi_*+(1-\Lambda)\theta]\). For \(\Lambda<1\) the right end of this interval moves to the right, and if \(\phi'\) vanishes on the interval for \(\theta=0\) and not to the right of it, the energy increases from zero.

**5.3.** The determinant is
\[
\begin{aligned}
H_{\xi\xi}H_{\theta\theta}-H_{\xi\theta}^2&=(d_0-(q-q_0)^2)\,H_{yy}^2\\
&=aH_{yy}^2=KE<0 .
\end{aligned}
\]
And \(H_{\xi\xi}=d_0H_{\theta\theta}\) with \(d_0<0\).

**5.4.** The induction step for the order \(j\) uses bounds for the orders up to \(j-1\) on the whole trapezoid, and the bounds of order eight give them for the derivatives along \(\xi\) of \(z_\xi\) and \(z_\theta\) up to the order \(7\): a derivative of \(z\) of order \(8\) can have one differentiation in \(\theta\) and seven in \(\xi\). The count \(2j-4>j\) needs \(j>4\), and Proposition 1.2 needs \(j\ge3\); so any start at an order between \(5\) and \(7\) works.

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026

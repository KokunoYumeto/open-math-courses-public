# Hamilton trajectories under a long-range force

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Can position drift be large while the change of momentum stays small?** For \(P_0(\xi)=\xi\) and a potential depending only on position, the exact ray is \(x(t)=t+Tw\), while momentum changes by a difference of potential values. Dividing position by time exposes a decaying relative displacement even when an accumulated phase grows. This is why trajectory data and time-derivative estimates need their own scaling.

A long-range force can accumulate over an infinite interval even when its derivatives are integrable. We compare Hamilton trajectories with free rays by dividing their position error by time. This reveals a decaying displacement, a uniformly small change of frequency, and precise estimates for every derivative of the initial data. We also determine which time derivative estimates require the trajectory to start on the free graph.

The prerequisite proofs are [finite-dimensional linear algebra and the differential rules](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-linear-algebra), [compactness and the scalar mean-value theorem](../providers/analysis/hilbert-valued-integration.md#compact-scalar-calculus), [the continuous fundamental theorem of calculus](../providers/analysis/hilbert-valued-integration.md#continuous-primitives), and [exponentials, real powers and trigonometric functions](../providers/analysis/elementary-functions-and-cutoffs.md#scalar-exponential). The short-interval construction of the smooth flow and the derivative-exponent calculation are proved below. The later lesson [Regularizing long-range coefficients](long-range-coefficient-calculus.md) develops related decay classes.

For background on smooth flows see Teschl [T]; Hamiltonian characteristics are discussed by Oh [O], and long-range polynomial trajectories by Hörmander [HW]. We use Hamilton's equations \(x'=H_\xi\), \(\xi'=-H_x\), and write \(X=(1+|x|^2)^{1/2}\). Derivative estimates are in ordinary real coordinates; replacing \(\partial\) by \(D=-i\partial\) leaves their magnitudes unchanged.

Fix an integer \(\kappa\ge2\) and \(0<\delta<1/(\kappa+1)\). The full position-decay sequence is

\[
 m(j)=
 \begin{cases}
 j+\delta,&0\le j\le\kappa,\\
 1+(\kappa-1+\delta)j/\kappa,&j\ge\kappa.
 \end{cases}
 \tag{1}
\]

The two formulas agree at the joining index. Put
\[
\begin{gathered}
\mu(k)=k+1-m(k+1),\\ \theta=(1-\delta)/\kappa,\\ a(k)=\max(\mu(k),0).
\end{gathered}
\tag{2}
\]
Thus \(\mu(k)=-\delta\) for \(k<\kappa\), while
\(\mu(k)=\theta(k+1)-1>0\) for \(k\ge\kappa\).
The strict upper bound on \(\delta\) makes \(\mu(\kappa)>0\), so the integral estimates below have no zero exponent or logarithmic case. Also \(0<\theta<1/2\).

<a id="hamilton-exact-model"></a>

## 1. A trajectory that can be solved exactly

Consider \(P_0(\xi)=\xi\) on the line and \(V_L(x,\xi)=v(x)\), where
\(v(x)=a(1+x^2)^{-\delta/2}\). Hamilton's equations give \(x'=1\) and
\(\xi'=-v'(x)\). Start at time \(T\) with \(x(T)=T(1+w)\) and \(\xi(T)=\eta\).
Then

\[
 \begin{aligned}
 x(t)&=t+Tw,\\
 z(t)&=x(t)/t-1=Tw/t,\\
 \xi(t)&=\eta-v(t+Tw)+v(T(1+w)).
 \end{aligned}
 \tag{3}
\]

For \(|w|<1/2\), the frequency correction and its first data derivatives are
\(O(T^{-\delta})\), while the displacement derivative keeps the exact factor
\(T/t\). The trajectory has a uniformly small change of frequency even on an
infinite future interval. Its position can still differ from the free ray by a
long-range amount. These two features motivate the scaled variables below.

All derivatives of this model potential satisfy \(|v^{(j)}(x)|\le C_j X^{-j-\delta}\). To see this, each term after \(j\) differentiations has the form \(C x^\ell(1+x^2)^{-\delta/2-r}\), with nonnegative integers \(\ell,r\) satisfying \(2r-\ell=j\). Differentiating either factor preserves this form with \(j\) increased by one; a term with \(\ell=0\) has no derivative contribution from that factor. Its modulus is at most \(C X^{\ell-\delta-2r}=C X^{-j-\delta}\). Since \(m(j)\le j+\delta\), these bounds imply every required position estimate in (4), including the joining index and all higher orders.

<a id="hamilton-scaled-coefficients"></a>

## 2. Scaling the Hamilton equations

Take a real smooth long-range polynomial
\(V_L(x,\xi)=\sum b_\alpha(x)\xi^\alpha\), of any finite frequency order, with all mixed bounds
\[
 |\partial_\xi^\alpha\partial_x^\beta V_L(x,\xi)|
        \le C_{\alpha\beta,K}X^{-m(|\beta|)}
        \quad(\xi\in K)
 \tag{4}
\]
on each compact frequency set \(K\). Let \(P_0\) be any real polynomial; no ellipticity is needed for these flow statements. In a compact regular-velocity region assume \(|\nabla P_0(\xi)|\ge c>0\) and \(|z|\le c/2\). Define
\[
\begin{gathered}
x=t(\nabla P_0(\xi)+z),\\ U(t,z,\xi)=t^{-1}V_L(t(\nabla P_0(\xi)+z),\xi),\\ t>0.
\end{gathered}
\tag{5}
\]
The Hamilton equations \(x'=\partial_\xi(P_0+V_L)\), \(\xi'=-\partial_x V_L\) are exactly
\[
 z'=-z/t+\partial_\xi U,\qquad
 \xi'=-\partial_z U.
 \tag{6}
\]
Indeed \(x'=\nabla P_0+z+t(P_0''\xi'+z')\), while
\(\partial_\xi U=t^{-1}\partial_\xi V_L+P_0''\partial_x V_L\) and
\(\partial_z U=\partial_x V_L\). Substitution proves both signs and the damping term.

On this region \(|x|\ge ct/2\). Each total parameter derivative of order \(q\) of \(U\) is a finite sum of terms
\[
\begin{gathered}
t^{j-1}c(\xi)\,\partial_x^\beta\partial_\xi^\gamma V_L(x,\xi),\\ j=|\beta|\le q,\quad |\beta|+|\gamma|\le q,
\end{gathered}
\tag{7}
\]
with bounded smooth coefficients on compact frequency sets. Since \(j-m(j)\) is nondecreasing,
\[
 |\partial_{z,\xi}^\alpha U|\le C_\alpha t^{|\alpha|-m(|\alpha|)-1}.
 \tag{8}
\]
Repeated logarithmic time derivatives of \(tU\), at fixed \(z,\xi\), also have finite expansions with at most one new position derivative and one factor \(t\) at each step. Hence, for \(E=t\partial_t\),
\[
 |\partial_{z,\xi}^\alpha E^\tau(tU)|
       \le C_{\alpha\tau}t^{|\alpha|+\tau-m(|\alpha|+\tau)}.
 \tag{9}
\]
This includes \(\tau=0\). These complete parameter estimates concern actual coefficients with no independent time dependence.

<a id="hamilton-exponent-partitions"></a>

## 3. How the derivative exponents combine

If \(q\ge1\), \(k_i\ge1\) and \(\sum_{i=1}^q k_i=k\), then
\[
 \mu(q)+\sum_{i=1}^q a(k_i)\le\mu(k).
 \tag{10}
\]
To prove this, first suppose \(k<\kappa\). Then all \(k_i,q<\kappa\), and the left side is \(-\delta=\mu(k)\). If \(k\ge\kappa\) and none of the \(k_i\) reaches \(\kappa\), the left side is \(\mu(q)\le\mu(k)\).

In the remaining cases let \(\ell\ge1\) be the number of \(k_i\ge\kappa\). All other \(k_i\) are at least one, so
\[
\begin{gathered}
\sum_{k_i\ge\kappa}k_i\le k-q+\ell,\\ \sum_i a(k_i)\le\theta(k-q+2\ell)-\ell.
\end{gathered}
\tag{11}
\]
If \(q\ge\kappa\), adding \(\mu(q)=\theta(q+1)-1\) gives a bound
\(\mu(k)+\ell(2\theta-1)\le\mu(k)\).
If \(q<\kappa\), subtracting \(\mu(k)=\theta(k+1)-1\) from that bound plus \(-\delta\) gives at most
\[
\begin{gathered}
1-\delta-\theta(q+1)+\ell(2\theta-1)\\ \le-\delta-\theta(q-1)\le0.
\end{gathered}
\tag{12}
\]
This proves (10) in all cases, including \(q=1\).

Consequently a smooth outer function with derivative order \(q\) bounded by \(t^{\mu(q)+b}\), composed with an inner map whose positive-order derivatives \(k_i\) are bounded by \(t^{a(k_i)}\), has derivatives of total order \(k\) bounded by \(Ct^{\mu(k)+b}\). To justify the composition formula, differentiate repeatedly: every positive-order derivative is a finite sum of an outer derivative of order \(q\), evaluated on the inner map, times \(q\) inner derivatives of positive orders summing to \(k\). This follows by induction using only the finite product and chain rules. (10) bounds each term. Constants depend on the finite derivative order, independently of \(t\) and the initial time \(T\).

<a id="hamilton-uniform-future-flow"></a>

## 4. A future flow with constants uniform in its starting time

The uniform flow estimates below are Hörmander [H4, Lemma 30.3.1].

**Theorem 4.1 (uniform future flow).** Let \(\omega\subset\mathbb R^{2n}\) be open and closed under contractions of its first coordinate:
\((z,\xi)\in\omega\Rightarrow(sz,\xi)\in\omega\) for \(0\le s\le1\).
Let \(\omega'\Subset\omega\). Assume real smooth \(U\) obeys (8) uniformly on \(\omega\) for all sufficiently large \(t\). For all sufficiently large \(T\), the equations with
\((z(T),\xi(T))=(w,\eta)\in\omega'\) have a unique solution in \(\omega\) for every \(t\ge T\), and constants independent of \(T\) give
\[
\begin{gathered}
|\partial_{w,\eta}^\alpha(z,\xi)|\le C_\alpha t^{\mu(|\alpha|)},\\ |\alpha|\ge\kappa,\\ |\partial_{w,\eta}^\alpha(\xi-\eta)|\le C_\alpha T^{\mu(|\alpha|)},\\ |\alpha|<\kappa,\\ |\partial_{w,\eta}^\alpha z|\\ \le (T/t)|\partial_{w,\eta}^\alpha w|+C_\alpha t^{\mu(|\alpha|)},\\ |\alpha|<\kappa.
\end{gathered}
\tag{13}
\]

<a id="hamilton-local-flow-and-data-derivatives"></a>

**Proof.** On a closed coordinate ball and a sufficiently short time interval, the vector field \(F(t,Y)=(-z/t+U_\xi,-U_z)\) has bounded size \(M\) and Lipschitz constant \(L\); the latter follows by integrating \(D_YF\) along segments. Start in the concentric ball of half the radius. Choose the interval length \(h\) so that \(hM\) is at most half the radius and \(hL<1\). Then the integral map takes continuous paths in the closed ball to paths in the same ball and is a contraction in the supremum norm. Its iterates have geometrically summable differences. Completeness follows coordinate by coordinate: a uniformly Cauchy sequence has pointwise limits, convergence to them is uniform, and the uniform limit is continuous and remains in the closed ball. The Lipschitz estimate permits passage to the limit in the integral, so the limit solves the path equation. The contraction inequality proves uniqueness. These choices work uniformly for the initial points in the smaller ball.

We will use the following integral estimate. If \(N,b,f\ge0\) are continuous and

\[
 N(t)\le A+\int_T^t\bigl(b(s)N(s)+f(s)\bigr)\,ds,
 \qquad A\ge0,
\]

call the right side \(G(t)\). Then \(N\le G\), \(G(T)=A\), and \(G'\le bG+f\). Multiplying by \(e^{-B(t)}\), where \(B(t)=\int_T^t b(s)\,ds\), and integrating gives

\[
 N(t)\le e^{B(t)}\left(A+\int_T^t e^{-B(s)}f(s)\,ds\right).
\]

This proves the precise integrating-factor estimate needed below, including zero initial value and a nonconstant forcing. It also applies to an integrated differential inequality; the regularized norms used below are differentiable before their regularization is removed.

We justify data differentiation before estimating any jet. Write \(Y(t,a)\) for this solution with initial data \(a=(w,\eta)\). Apply the just-proved estimate with \(b=L\), \(f=0\), \(A=|h|\) to the difference of two path equations. It gives \(|Y(t,a+h)-Y(t,a)|\le C|h|\) on the fixed interval. Let \(J(t,a)\) solve

\[
 J(t,a)=I+\int_T^t D_YF(s,Y(s,a))J(s,a)\,ds.
\]

Its Picard series converges uniformly, since its term of order \(j\) is bounded by \(L^j|t-T|^j/j!\). Put \(\Delta_h=Y(t,a+h)-Y(t,a)\). The segment form of Taylor's theorem writes the difference of the two vector fields as \(D_YF(s,Y(s,a))\Delta_h+R_h(s)\Delta_h\), with \(\sup_s\|R_h(s)\|\to0\): all paths lie in one compact neighborhood and \(D_YF\) is uniformly continuous there. Subtract the equation for \(J h\) and divide by \(|h|\). The resulting remainder has zero initial value, a bounded linear coefficient, and a forcing term tending uniformly to zero. The same integrating-factor estimate makes its uniform norm tend to zero. Thus \(D_aY=J\); continuity follows from its integral equation. This proves an actual derivative, rather than only a candidate variational equation.

For higher orders, induct on the regularity of the vector field in arbitrary finite dimension. The first-derivative argument just proved the \(C^1\) step. Suppose the assertion is known for every \(C^k\) vector field, and let \(F\) be \(C^{k+1}\). The augmented equation for the pair \((Y,J)\) has vector field \((F(t,Y),D_YF(t,Y)J)\), which is \(C^k\) in its finite-dimensional variables. Its local flow is therefore \(C^k\) in the initial values by the induction hypothesis. Restrict the initial matrix to \(J(T)=I\); uniqueness identifies its matrix component with the first derivative \(D_aY\) already constructed. Thus \(D_aY\) is \(C^k\), which makes \(Y\) a \(C^{k+1}\) function of its initial data. This closes the induction without presupposing differentiability of a higher jet. Uniqueness patches the argument across successive short intervals. Time smoothness on finite intervals then follows from \(\partial_tY=F(t,Y)\). Repeated product and chain rules give the equations linear in the highest data derivative, with lower-derivative terms estimated below.

<a id="hamilton-global-continuation"></a>

Local uniqueness glues all extensions to a maximal future interval. Indeed, two extensions with the same initial data cannot first cease to agree at an interior time: continuity gives equal data there, and local uniqueness extends their agreement further. Their union is therefore a single solution wherever either is defined.

The first derivatives of \(U\) obey \(Ct^{-1-\delta}\). As long as the solution stays in \(\omega\),
\[
\begin{gathered}
|z(t)-(T/t)w|\\ \le t^{-1}C\int_T^t s^{-\delta}\,ds\le Ct^{-\delta},\\ |\xi(t)-\eta|\\ \le C\int_T^t s^{-1-\delta}\,ds\le CT^{-\delta}.
\end{gathered}
\tag{14}
\]
The contraction tube
\(\{(sw,\eta):(w,\eta)\in\overline{\omega'},\,0\le s\le1\}\)
is a compact subset of \(\omega\). Choose a positive distance from it to the complement. For sufficiently large \(T\), (14) keeps the solution in a fixed compact interior neighborhood of that tube. A finite endpoint of existence would have a limit in this compact neighborhood, because its vector field is bounded on the corresponding finite time interval; the local contraction argument extends it. Hence the solution exists for all \(t\ge T\). This also proves the two low-order estimates when \(\alpha=0\).

<a id="hamilton-uniform-data-estimates"></a>

For a first data derivative \(Y_\alpha=(z_\alpha,\xi_\alpha)\), the equations are
\[
\begin{gathered}
z_\alpha'=-z_\alpha/t+U_{\xi\xi}\xi_\alpha+U_{\xi z}z_\alpha,\\ \xi_\alpha'=-U_{z\xi}\xi_\alpha-U_{zz}z_\alpha.
\end{gathered}
\tag{15}
\]
All Hessian entries are bounded by \(Ct^{1-m(2)}=Ct^{-1-\delta}\).
In the squared Euclidean norm of all first data derivatives, the contribution of \(-z_\alpha/t\) is nonpositive. Thus
\[
 N'(t)\le Ct^{-1-\delta}N(t),\qquad N(T)=\sqrt{2n}.
 \tag{16}
\]
The integral of the coefficient from \(T\) to infinity is bounded independently of \(T\ge1\), so \(N(t)\le C\). Equation (15) then gives
\[
 |(tz_\alpha)'|\le Ct^{-\delta},\qquad
 |\xi_\alpha'|\le Ct^{-1-\delta}.
 \tag{17}
\]
Their integrations prove the two estimates for \(|\alpha|=1\).

Suppose all data derivatives below order \(k\ge2\) have been bounded. In particular their norms are at most \(Ct^{a(j)}\) at order \(j<k\). Differentiating the equations \(k\) times gives (15) for the highest derivative, with additional terms \(F_\alpha\). Each such term has an outer derivative of \(\nabla U\) of order \(q\ge2\), bounded by \(Ct^{\mu(q)-1}\), times lower data derivatives whose positive orders sum to \(k\). By (10),
\[
 |F_\alpha|\le C_k t^{\mu(k)-1}.
 \tag{18}
\]
The combined highest-derivative norm consequently satisfies
\[
\begin{gathered}
N_k'(t)\le Ct^{-1-\delta}N_k(t)+C_k t^{\mu(k)-1},\\ N_k(T)=0.
\end{gathered}
\tag{19}
\]
The norm inequality at zeros follows, for example, by first using
\((N_k^2+\varepsilon^2)^{1/2}\) and then letting \(\varepsilon\downarrow0\).
Variation of constants, with the integrable coefficient, gives a bounded \(N_k\) if \(k<\kappa\), since \(\mu(k)=-\delta\). If \(k\ge\kappa\), its positive exponent gives \(N_k(t)\le C_k t^{\mu(k)}\). For the remaining low-order refinements \(2\le k<\kappa\), return to the differentiated equations: their Hessian terms have size \(Ct^{-1-\delta}\) by the bounded \(N_k\), and so do their remainders by (18). Therefore
\[
 |(tz_\alpha)'|\le Ct^{-\delta},\qquad
 |\xi_\alpha'|\le Ct^{-1-\delta}.
 \tag{20}
\]
Their initial values vanish at these orders; integration proves the final two lines of (13). This completes the induction and the entire abstract spatial-data lemma.

<a id="hamilton-mixed-time-estimates"></a>

## 5. Time derivatives of trajectories starting on the free graph

The time-derivative estimate is Hörmander [H4, Lemma 30.3.2].

**Theorem 5.1 (mixed time and frequency derivatives).** For the Hamilton construction in Section 2, (9) holds. When \(w=0\), for every \(\alpha\) and integer \(\tau>0\),
\[
\begin{gathered}
|\partial_\eta^\alpha\partial_t^\tau(z(t,0,\eta),\xi(t,0,\eta))|\\ \le C_{\alpha\tau}t^{|\alpha|-m(|\alpha|+\tau)},\\ t\ge T.
\end{gathered}
\tag{21}
\]
The constants remain independent of sufficiently large \(T\). Here \(\eta\) ranges over any compact subset of the regular-velocity region, with \((0,\eta)\) in the initial set of Theorem 4.1. The domain can be chosen as a product of a small ball in \(z\) and a bounded open frequency neighborhood on which \(|\nabla P_0|\ge c\); it is then stable under contraction of \(z\), and (8)–(9) hold there uniformly.

**Proof.** First prove the equivalent Euler estimate
\[
\begin{gathered}
|\partial_\eta^\alpha E^\tau(z,\xi)|\\ \le C_{\alpha\tau}t^{|\alpha|+\tau-m(|\alpha|+\tau)}\\ =C_{\alpha\tau}t^{\mu(|\alpha|+\tau-1)}.
\end{gathered}
\tag{22}
\]
The equations are \(Ez=-z+tU_\xi\), \(E\xi=-tU_z\).
By (13) with \(w=0\), every pure \(\eta\) derivative of \(z\) is bounded by \(Ct^{\mu(|\alpha|)}\); pure derivatives of the whole pair are bounded by \(Ct^{a(|\alpha|)}\). By (9), every joint derivative of order \(q\) in \((z,\xi,\log t)\) of \(tU_\xi\) or \(tU_z\) is bounded by \(Ct^{\mu(q)}\).

For \(\tau=1\), apply the finite composition rule following (10) to the variable \(\eta\). It bounds \(\partial_\eta^\alpha(t\nabla U)\) by \(Ct^{\mu(|\alpha|)}\), and the \(-z\) term has that same bound. This proves (22), including \(\alpha=0\).

Induct on \(\tau\), with all \(\eta\) derivative orders at each preceding time order already available. Apply \(\partial_\eta^\alpha E^{\tau-1}\) to the Euler equations. Let \(r=|\alpha|+\tau-1\). All derivatives of the inner map
\((\eta,\log t)\mapsto(z,\xi,\log t)\)
used in this expression have time order below \(\tau\). Their total positive derivative order \(j\) is bounded by \(Ct^{a(j)}\): for positive time order the induction gives exponent \(\mu(j-1)\le a(j)\); for zero time order use (13). The last coordinate has first derivative one and all higher derivatives zero, consistent with \(a(1)=0\).

The finite composition rule therefore bounds the differentiated \(t\nabla U\) by \(Ct^{\mu(r)}\). If \(\tau\ge2\), the differentiated \(-z\) is bounded by \(Ct^{\mu(r-1)}\le Ct^{\mu(r)}\), by induction. The case \(\tau=1\) was already proved. This gives (22) at the new time order.

Finally
\[
 t^\tau\partial_t^\tau=E(E-1)\cdots(E-\tau+1).
 \tag{23}
\]
This is proved by induction from \(E(t^\ell v)=t^\ell(E+\ell)v\).
It is a finite polynomial in positive Euler powers. The exponent
\(|\alpha|+\ell-m(|\alpha|+\ell)\) increases with \(\ell\), so each term for \(1\le\ell\le\tau\) is controlled by the bound with \(\ell=\tau\), for \(t\ge1\). Divide by \(t^\tau\) to obtain (21). Multiplication by the unit complex factors in \(D=-i\partial\) leaves the derivative estimates unchanged.


The time assertion uses the joint estimate (9). Spatial bounds (8) for an independently time-dependent \(U\) alone do not imply it. Exercise 5 gives an explicit example and explains the role of zero initial displacement.

### Use the conclusion

Use the exact trajectory to test the factor \(T/t\), then check which mixed time estimates require zero initial displacement. Do not infer those estimates from spatial data derivatives alone.

<a id="hamilton-exercises-and-solutions"></a>

## 6. Exercises with complete solutions

**Exercise 1 — Basic — scaled Hamilton equations and an exact line model.**

For \(H_L(x,\xi)=P_0(\xi)+V_L(x,\xi)\), set
\(x=t(\nabla P_0(\xi)+z)\) and
\(U=t^{-1}V_L(t(\nabla P_0(\xi)+z),\xi)\).
Derive both scaled equations, including their signs. On the line, take
\(P_0(\xi)=\xi\) and \(V_L(x,\xi)=v(x)=a(1+x^2)^{-\delta/2}\).
Solve the flow with \((z(T),\xi(T))=(w,\eta)\), \(|w|<1/2\), and verify its low-order data estimates independently of \(T\ge1\).

**Solution 1.** The original equations are \(x'=P_0'(\xi)+V_{L,\xi}\) and
\(\xi'=-V_{L,x}\). Differentiating the coordinate substitution gives
\[
 x'=P_0'(\xi)+z+t(P_0''(\xi)\xi'+z').
 \tag{24}
\]
On the other hand \(U_z=V_{L,x}\) and
\(U_\xi=t^{-1}V_{L,\xi}+P_0''(\xi)V_{L,x}\).
Substitute \(\xi'=-V_{L,x}\) into the first identity and rearrange:
\[
 z'=-z/t+U_\xi,\qquad \xi'=-U_z.
 \tag{25}
\]
The \(P_0''\) term has a plus sign in \(U_\xi\); the negative \(\xi'\) in the coordinate derivative is what produces it.

In the line model \(x'=1\), so \(x(t)=t+Tw\) and \(z(t)=Tw/t\). Integration of \(\xi'=-v'(t+Tw)\) gives
\[
 \xi(t,w,\eta)=\eta-v(t+Tw)+v(T(1+w)).
 \tag{26}
\]
Because \(t+Tw\ge t/2\) and \(T(1+w)\ge T/2\),
\(|\xi-\eta|\le CT^{-\delta}\). Also
\[
 \partial_w\xi=-Tv'(t+Tw)+Tv'(T(1+w)),
 \tag{27}
\]
whose modulus is at most
\(C[Tt^{-1-\delta}+T^{-\delta}]\le CT^{-\delta}\).
The \(\eta\)-derivative of \(\xi-\eta\) is zero.
For \(z\), the only nonzero positive data derivative is
\(\partial_w z=T/t\); every \(\eta\)-derivative and higher derivative is zero. These give exactly the low-order flow estimates.

More generally
\(\partial_w^k(\xi-\eta)=T^k[-v^{(k)}(t+Tw)+v^{(k)}(T(1+w))]\),
bounded by \(CT^{-\delta}\) at every fixed \(k\).
These bounds are stronger than the permitted positive high-order growth. The constants depend on \(a,\delta,k\), but not on \(T,t\) in the stated range.

**Exercise 2 — Intermediate — compute all derivative exponents.**

Take \(\kappa=2\), \(\delta=1/5\), with the exact sequence
\(m(j)=j+\delta\) for \(j\le2\) and
\(m(j)=1+(1+\delta)j/2\) for \(j\ge2\).
Compute the first four \(\mu(k)=k+1-m(k+1)\), and give the bounds for the second and third data jets. With \(w=0\), give the bounds for
\(\partial_t^2(z,\xi)\),
\(\partial_\eta^\alpha\partial_t(z,\xi)\) at \(|\alpha|=2\), and
\(\partial_\eta^\alpha\partial_t^2(z,\xi)\) at \(|\alpha|=3\).
Explain why a high data derivative can grow while its time derivative decays.

**Solution 2.** The joining values agree:
\(m(2)=11/5\). The next values are
\(m(3)=14/5\), \(m(4)=17/5\), \(m(5)=4\). Thus
\[
\begin{gathered}
\mu(0)=\mu(1)=-1/5,\\ \mu(2)=1/5,\quad \mu(3)=3/5.
\end{gathered}
\tag{28}
\]
The second data jet is \(O(t^{1/5})\), and the third is \(O(t^{3/5})\), uniformly in sufficiently large initial \(T\). The first-order corrections \(\xi-\eta\) still have \(O(T^{-1/5})\) data derivatives, while the \(z\)-derivative retains its explicit \(T/t\) initial term plus \(O(t^{-1/5})\).

For positive time order the formula is
\(t^{|\alpha|-m(|\alpha|+\tau)}\). It gives, respectively,
\[
\begin{gathered}
\partial_t^2(z,\xi)=O(t^{-11/5}),\\ \partial_\eta^\alpha\partial_t(z,\xi)=O(t^{-4/5}),\\ \partial_\eta^\alpha\partial_t^2(z,\xi)=O(t^{-1})
\end{gathered}
\tag{29}
\]
at the specified orders. In the second estimate the same second data jet that can grow like \(t^{1/5}\) has a first time derivative bounded by \(t^{-4/5}\). Its derivative is integrable on no infinite half-line at that exponent, so there is no conflict with slow growth. The estimate records a derivative of a growing jet; it does not assert that all high jets remain bounded.

**Exercise 3 — Intermediate — the compact contraction tube.**

Let \(\omega\) be an open flow domain stable under contractions of \(z\), and \(\omega'\Subset\omega\). Assume the first scaled forcing derivatives are bounded by \(Ct^{-1-\delta}\), \(0<\delta<1\). Prove global future existence of every flow starting in \(\omega'\) at all sufficiently large \(T\), with one threshold for the entire initial set. Identify where contraction of \(z\), compactness and integrability are used.

**Solution 3.** On every existing solution, integration of
\((tz)'=tU_\xi\) gives
\[
 |z(t)-(T/t)w|
       \le \frac C t\int_T^t s^{-\delta}\,ds
       \le C t^{-\delta}.
 \tag{30}
\]
Integration of \(\xi'=-U_z\) gives
\(|\xi(t)-\eta|\le C\int_T^\infty s^{-1-\delta}\,ds
\le CT^{-\delta}\).
The free comparison points \(((T/t)w,\eta)\) lie in
\[
 \mathcal C=\{(sw,\eta):(w,\eta)\in\overline{\omega'},\ 0\le s\le1\}.
 \tag{31}
\]
The contraction hypothesis puts the whole set in \(\omega\); continuity makes it compact. Choose a fixed closed neighborhood of \(\mathcal C\) inside \(\omega\) and a positive smaller margin. Both errors are at most \(CT^{-\delta}\), so one sufficiently large \(T\) keeps every solution inside that same neighborhood.

Local existence and uniqueness follow from the short-interval integral contraction for the smooth vector field. If a maximal future endpoint were finite, the vector field would be bounded on this compact neighborhood and on its finite time interval. The solution would be Cauchy at the endpoint and have a limit in the neighborhood. Local existence from that limit would extend it, a contradiction.

Contraction of \(z\) places the free comparison curve inside the domain. Compactness gives a uniform positive margin for all initial data. The integral of \(s^{-1-\delta}\) gives the uniformly small frequency displacement, while the \(t^{-1}\) integrating factor for \(z\) converts the nonintegrable \(s^{-\delta}\) input into a decaying \(t^{-\delta}\) error. These facts, not boundedness of an arbitrary spatial set, give the uniform threshold.

**Exercise 4 — Advanced — close the full high-data-derivative induction.**

For the exact general \(\kappa\ge2\) sequence and \(0<\delta<1/(\kappa+1)\), prove
\[
\begin{gathered}
\mu(q)+\sum_{i=1}^q\max(\mu(k_i),0)\le\mu(k),\\ k_i\ge1,\quad\sum k_i=k.
\end{gathered}
\tag{32}
\]
Use it to bound every nonlinear remainder in the \(k\)-th differentiated scaled equation and derive both the high-order growth bound and the low-order refinement.

**Solution 4.** Set \(\theta=(1-\delta)/\kappa\). For \(j<\kappa\),
\(\mu(j)=-\delta\); for \(j\ge\kappa\),
\(\mu(j)=\theta(j+1)-1>0\). If \(k<\kappa\), all the positive parts are zero and the inequality is equality. If \(k\ge\kappa\) but all \(k_i<\kappa\), it follows from the monotonicity \(\mu(q)\le\mu(k)\).

Otherwise let \(\ell\ge1\) count the \(k_i\ge\kappa\). The small indices are at least one, so their removal leaves
\(\sum_{\rm large}k_i\le k-q+\ell\). Therefore
\(\sum\max(\mu(k_i),0)\le\theta(k-q+2\ell)-\ell\).
If \(q\ge\kappa\), adding \(\mu(q)\) gives at most
\(\mu(k)+\ell(2\theta-1)\le\mu(k)\).
If \(q<\kappa\), subtracting \(\mu(k)\) from the resulting bound gives at most
\(1-\delta-\theta(q+1)+\ell(2\theta-1)
\le-\delta-\theta(q-1)\le0\).
This proves every partition case.

In a nonlinear remainder at total data order \(k\), an outer derivative of \(\nabla U\) has order \(q\ge2\), hence size \(t^{\mu(q)-1}\). Its \(q\) inner derivatives have positive orders \(k_i<k\) summing to \(k\), hence size at most \(t^{\max(\mu(k_i),0)}\) by induction. The proved partition inequality gives an \(O(t^{\mu(k)-1})\) remainder.

The highest derivative enters linearly with a Hessian coefficient bounded by \(Ct^{-1-\delta}\), and damping \(-z_k/t\), which has nonpositive contribution to squared norm. Its norm thus satisfies
\[
 N_k'\le Ct^{-1-\delta}N_k+C_k t^{\mu(k)-1},\qquad N_k(T)=0
 \tag{33}
\]
for \(k\ge2\). Variation of constants has uniformly bounded amplification because the Hessian coefficient is integrable. If \(k\ge\kappa\), the positive exponent integrates to \(O(t^{\mu(k)})\). If \(2\le k<\kappa\), its negative exponent gives bounded norm. Return to the two differential components in the latter case: both their Hessian inputs and nonlinear remainders are \(O(t^{-1-\delta})\). Hence
\(|(tz_k)'|\le Ct^{-\delta}\), \(|\xi_k'|\le Ct^{-1-\delta}\).
Integrating from their zero initial values gives \(z_k=O(t^{-\delta})\) and
\(\xi_k=O(T^{-\delta})\), the required refinements. Orders zero and one are covered by the direct integration and first-variation argument.

**Exercise 5 — Advanced — the exact hypotheses for time derivatives.**

Under the mixed outer estimate (9), prove the positive-time derivative bound with \(w=0\) from the Euler equations and the partition inequality. Explain both why \(w=0\) is needed for constants independent of \(T\), and why spatial estimates on an arbitrary time-dependent \(U\) do not suffice.

**Solution 5.** Write \(E=t\partial_t\). The equations are
\(Ez=-z+tU_\xi\), \(E\xi=-tU_z\). Every total derivative of order \(q\) in
\((z,\xi,\log t)\) of \(t\nabla U\) is \(O(t^{\mu(q)})\), by (9).
With zero initial \(w\), all pure \(\eta\)-derivatives of \(z\) are
\(O(t^{\mu(|\alpha|)})\), and those of the whole pair are
\(O(t^{a(|\alpha|)})\), \(a=\max(\mu,0)\).
The finite composition rule proves the desired bound for one Euler derivative.

Induct on the positive Euler order \(\tau\), allowing all \(\eta\) orders at each preceding time order. In
\(\partial_\eta^\alpha E^{\tau-1}(t\nabla U)\), all inner time derivatives have order less than \(\tau\) and are bounded by \(t^{a(j)}\) at total derivative order \(j\). The appended coordinate \(\log t\) has first derivative one and higher derivatives zero, also fitting that bound. The partition inequality gives
\[
 |\partial_\eta^\alpha E^\tau(z,\xi)|
       \le Ct^{\mu(|\alpha|+\tau-1)}.
 \tag{34}
\]
The differentiated \(-z\) term has exponent \(\mu(|\alpha|+\tau-2)\) when
\(\tau\ge2\), which is no larger. The first Euler order used its pure-data bound. Now
\(t^\tau\partial_t^\tau=E(E-1)\cdots(E-\tau+1)\).
This finite polynomial and monotonicity of \(j-m(j)\) give
\[
 |\partial_\eta^\alpha\partial_t^\tau(z,\xi)|
       \le Ct^{|\alpha|-m(|\alpha|+\tau)}.
 \tag{35}
\]

For the necessity of the zero displacement, even \(U=0\) gives
\(z=Tw/t\). At \(t=T\), \(|\partial_tz|=|w|/T\), whereas the claimed uniform bound would be \(CT^{-1-\delta}\). For fixed \(w\ne0\), no \(T\)-independent constant makes this true.

For the time hypothesis, take
\(U=t^{-1-\delta}\sin(t^2)F(\xi)\), independent of \(z\), with
\(F'(\eta)\ne0\) in a compact frequency region. Every spatial derivative obeys (8), and \(\xi=\eta\). With \(w=0\),
\[
 z=t^{-1}F'(\eta)\int_T^t s^{-\delta}\sin(s^2)\,ds.
 \tag{36}
\]
The integral is bounded as \(t\to\infty\): substitute \(r=s^2\) and integrate the decaying amplitude against \(\sin r\) by parts. Differentiating the equation for \(z'\) gives
\[
\begin{aligned}
 z''&=2F'(\eta)t^{-\delta}\cos(t^2)\\
 &\quad -(2+\delta)F'(\eta)t^{-2-\delta}\sin(t^2)\\
 &\quad +2z/t^2.
 \end{aligned}
\tag{37}
\]
Along \(t^2=2\pi j\) its leading term is nonzero, while the last two terms are \(O(t^{-2-\delta})+O(t^{-3})\). Thus it cannot obey the required
\(O(t^{-2-\delta})\) second-time-derivative estimate. This explicitly time-dependent \(U\) is not the actual time-independent Hamilton coefficient construction. That construction supplies (9), which is the hypothesis used in the proof.


## References

[T] Gerald Teschl, [*Ordinary Differential Equations and Dynamical Systems*, free author's preliminary edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), April 2012, §§2.2, 2.4 and 2.6: Theorem 2.2, Lemma 2.7, Theorem 2.10 and Lemma 2.14.

[O] Sung-Jin Oh, [*Lecture Notes for Math 222A*, free evolving lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), University of California, Berkeley, Fall 2023, §2.4.1, pp. 23–24, equation (2.20).


[HW] Lars Hörmander, [*The existence of wave operators in scattering theory*, freely readable journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf), 1976, §3, pp. 79–82, Lemmas 3.6–3.7.

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Lemmas 30.3.1–30.3.2 and their proofs, pp. 297–300. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).

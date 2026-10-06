# Generating functions and the end of a localized force

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: What changes when the force ends after a compact region?** Once a localized force has ended, the trajectory continues freely but retains the displacement and action acquired earlier. Mixed coordinates turn that memory into a generating function. Inverting the projection and differentiating the inverse are separate tasks, and the long-range case needs bounds at every derivative order rather than just a picture of the final ray.

An escaping energy family has two useful descriptions. A global action records its tangential displacement on the frequency shell. A local generating function expresses position and frequency in mixed coordinates. We connect these descriptions, determine the exact end effect of a compactly supported force, and prove every derivative estimate for a general long-range force.

Read [Escaping Lagrangians on regular energy surfaces](escaping-lagrangians-on-regular-energy-surfaces.md), including its normalized action and near-shell restriction, and [Hamilton trajectories under a long-range force](hamilton-trajectories-under-a-long-range-force.md), especially the estimates with zero initial displacement. The [coordinate inverse proof, CI1–CI3](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse), supplies the smooth local inverses and shell charts; its [finite covering and bump construction](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions) supplies the compact-cover radius and cutoffs below. We write each derivative partition used in the estimates.

Basic freely accessible references are Oh [O] and Teschl [T]. The projection inverse below is constructed by contraction, difference quotients and monotonicity; its full weighted derivative estimates follow from the preceding Hamilton-trajectory lesson.

## 1. How an action shifts the normal rays

Use the hypotheses and notation of *Escaping Lagrangians on regular energy surfaces*. Thus \(P_0\) is proper in absolute value, \(\lambda\) is regular, \(M_\lambda\) is compact, \(V_L\) obeys the full position class for an integer \(\kappa\ge2\), and \(M_T\) is its perturbed sheet in a fixed regular collar. The escaping Lagrangian \(\Lambda_T^+\) has a globally normalized action \(d\psi=\sum x_jd\xi_j\).

First suppose \(V_L(x,\xi)=0\) for \(|x|\ge R_0\), at every frequency. Once a ray leaves this region forever, its frequency and action stop changing. The resulting function on the free shell determines the entire shift.

**Theorem 1.1 (the end of a localized force).** There is a real smooth \(\psi_\infty\) on \(M_\lambda\) such that \(\psi(x,\xi)=\psi_\infty(\xi)\) on the sufficiently distant part of \(\Lambda_T^+\). Let

\[
\begin{gathered}
r:T^*\mathbb R^n|_{M_\lambda}\longrightarrow T^*M_\lambda,
 \\ r(x,\xi)=(x|_{T_\xi M_\lambda},\xi).
\end{gathered}
\tag{1}
\]

Outside one common large position threshold, \(\Lambda_T^+\) is exactly the positive-normal part of
\(r^{-1}(\operatorname{graph}(d\psi_\infty))\).
The positive direction is specified by increasing
\(x\cdot v(\xi)/|v(\xi)|^2\).

For example, on the unit sphere with \(P_0=|\xi|^2\), the shell function
\(\psi_\infty(\xi)=a\cdot\xi\) describes the affine normal lines
\(x=a+s\xi\). Its tangential differential shifts each ray by the tangential part of \(a\). This is a geometric example of the formula; it does not assert that every chosen shell function comes from a prescribed potential.

**Proof.** If the shell is empty all assertions are vacuous. Assume it is nonempty. Assume \(V_L(x,\xi)=0\) for \(|x|\ge R_0\), at every frequency.
The uniform escaping bound \(|x(t)|\ge c_0t\) shows that after one fixed time
\(t_*\ge\max(T,R_0/c_0)\), every orbit is outside that support forever.
Thus \(\xi\) is constant for \(t\ge t_*\), and \(\psi\) is constant along those late orbit segments.
Write \(\xi_\infty(\eta)=\xi(t_*,\eta)\).
Conservation of energy gives \(P_0(\xi_\infty)=\lambda\).

Identify the initial sheet with \(M_\lambda\) through the smooth small normal graph \(u\mapsto N(u,s_T(u))\).
Its first derivatives differ from the identity embedding by \(O(T^{-\delta})\), from the full local sheet bounds.
The low data estimates in *Hamilton trajectories under a long-range force*, composed with that graph, imply that the final map
\[
\begin{gathered}
F:M_\lambda\longrightarrow M_\lambda,\\
 F(u)=\xi_\infty(N(u,s_T(u)))
\end{gathered}
\tag{2}
\]
is \(C^1\)-close to the identity, with error \(O(T^{-\delta})\).
This map is a global diffeomorphism for sufficiently large \(T\).
Here is the global step explicitly.

Choose finitely many smooth coordinate charts covering the compact shell, each with an inner coordinate ball and a larger convex coordinate ball.
The finite covering has a positive small radius so any two sufficiently close shell points belong to one such inner/outer chart arrangement.
In these coordinates, \(F-\mathrm{id}\) has derivative uniformly smaller than \(1/2\) for large \(T\).
The integral of that derivative along a segment in the larger convex ball proves injectivity of \(F\) on each inner chart.
If \(F(u)=F(v)\), the small zeroth-order displacement gives
\(|u-v|\le2\|F-\mathrm{id}\|_\infty\), so the pair falls in one such chart and \(u=v\).
Its derivative is invertible in these charts, so its image is open.
The image is also closed by compactness.
The compact shell has finitely many connected components, because a finite cover by connected coordinate balls meets every component.
Small displacement keeps points in the same component; the distinct compact components have positive separation.
The image meets each component and is both open and closed within it, so it is all of \(M_\lambda\).
The local smooth inverses therefore form one global smooth inverse.

There is consequently a real smooth function
\[
\begin{gathered}
\psi_\infty(\xi)=\psi(t_*,N(F^{-1}(\xi),s_T(F^{-1}(\xi))))
 \\\text{on }M_\lambda,
\end{gathered}
\tag{3}
\]
The initial normal graph is written explicitly in this expression.
For all sufficiently late points of the flowout,
\(\psi(x,\xi)=\psi_\infty(\xi)\).
Late trajectories have
\[
\xi(t)=\xi,\qquad x(t)=t\,\nabla P_0(\xi)+a(\xi),
\tag{4}
\]
with a smooth bounded offset \(a\) on the compact shell.
Its tangent restriction obeys
\[
x|_{T_\xi M_\lambda}=d\psi_\infty(\xi),
\tag{5}
\]
because \(d\psi=\beta\), and \(\nabla P_0(\xi)\) annihilates the tangent of the free shell.

Under the natural restriction map
\[
\begin{gathered}
r:T^*\mathbb R^n|_{M_\lambda}\longrightarrow T^*M_\lambda,
 \\ (x,\xi)\longmapsto(x|_{T_\xi M_\lambda},\xi),
\end{gathered}
\tag{6}
\]
the late flowout therefore maps to
\(\operatorname{graph}(d\psi_\infty)\).
For each fixed \(\xi\), the full inverse image is an affine line parallel to
\(\nabla P_0(\xi)\), since that is the one-dimensional annihilator of
\(T_\xi M_\lambda\).
The orbit with that final frequency fills its positive-normal half-line at infinity.
The bounded smooth offsets and compact shell give one common large position threshold.
Thus, outside that threshold and in the positive-normal direction, the flowout is exactly the corresponding part of
\[
r^{-1}(\operatorname{graph}(d\psi_\infty)).
\tag{7}
\]
This proves equality of sets at infinity, rather than only containment or a formal shift of a normal bundle.

## 2. Mixed coordinates and the generator we seek

Fix \(\xi^0\in M_\lambda\) with \(\partial_1P_0(\xi^0)>0\), and choose compact inner and outer charts where this derivative stays positive. Write the shell as \(\xi_1=E(\xi')\). Whenever \((x_1,\xi')\) are actual coordinates on the escaping family, define

\[
G=x_1\xi_1-\psi,\qquad G_0(x_1,\xi')=x_1E(\xi').
\tag{8}
\]

The exact action identity gives

\[
\begin{gathered}
 dG=\xi_1\,dx_1-\sum_{j\ne1}x_j\,d\xi_j,\\
 \xi_1=\partial_{x_1}G,\qquad
 x'=-\partial_{\xi'}G.
 \end{gathered}
\tag{9}
\]

The free generator gives \(x'=-x_1\nabla E\). Differentiating
\(P_0(E(\xi'),\xi')=\lambda\) shows that
\((1,-\nabla E)=v(E(\xi'),\xi')/\partial_1P_0\), so this is exactly the positive-normal direction.

For a localized force, Theorem 1.1 already implies the exact distant formula

\[
\begin{gathered}
 G(x_1,\xi')=x_1E(\xi')-\psi_\infty(E(\xi'),\xi'),\\
 x'=-x_1\nabla E+
       \nabla_{\xi'}[\psi_\infty(E(\xi'),\xi')].
 \end{gathered}
\tag{10}
\]

The tangential shift has a plus sign in the position equation. If another coordinate \(x_j\) is privileged, its generator is \(x_j\xi_j-\psi\); the same global action determines the transition.

The next result also allows a general long-range force.

**Theorem 2.1 (all derivatives of the generator).** For all sufficiently large \(T\), and for \(x_1\) sufficiently large, the projection \((x,\xi)\mapsto(x_1,\xi')\) gives actual smooth coordinates on the entire part of \(\Lambda_T^+\) in a fixed smaller frequency chart. The normalized generator above satisfies, for every \(\alpha=(\alpha_1,\alpha')\),

\[
|\partial_{x_1}^{\alpha_1}\partial_{\xi'}^{\alpha'}
           (G-G_0)|
       \le C_\alpha x_1^{1+|\alpha'|-m(|\alpha|)}.
\tag{11}
\]

Here \(|\alpha|=\alpha_1+|\alpha'|\), and \(m\) is the full decay sequence from the preceding lesson. The constants are uniform on the compact inner frequency chart for the fixed construction. The same geometric conclusions apply to the negative-normal end by reversing the Hamiltonian and the energy.

## 3. Weighted jets before changing coordinates

Here \(D\) denotes ordinary real derivatives, and \(t\partial_t\) is the logarithmic time derivative.

Write
\[
\begin{gathered}
\theta=(1-\delta)/\kappa,\\
 \mu(k)=k+1-m(k+1),\\
 \mu(k)=-\delta\\(k<\kappa),\\
 \mu(k)=\theta(k+1)-1>0\\(k\ge\kappa).
\end{gathered}
\tag{12}
\]
The last strict inequality uses \(\delta<1/(\kappa+1)\). The derivative-product calculation in *Hamilton trajectories under a long-range force* proves
\(\mu(q)+\sum_i\max(\mu(k_i),0)\le\mu(\sum_i k_i)\) for all positive derivative partitions. We need its positive-part variant too.


Put \(A(k)=\max(\mu(k),0)\) and \(B(k)=\max(k-m(k),0)\).
Then \(B(k)\le A(k)\), and every derivative partition satisfies
\[
\begin{gathered}
A(q)+\sum_{i=1}^q A(k_i)\le A(k),
       \\ k_i\ge1,\\\sum k_i=k.
\end{gathered}
\tag{13}
\]
For \(q\ge\kappa\), this follows from the full \(\mu\)-partition inequality, because \(A(q)=\mu(q)\) and \(A(k)=\mu(k)\).
For \(q<\kappa\), if no input order reaches \(\kappa\), the left side is zero.
Otherwise let \(\ell\ge1\) count those orders, and use
\(\sum A(k_i)\le\theta(k-q+2\ell)-\ell\).
Subtracting \(A(k)=\theta(k+1)-1\) gives at most
\[
1-\theta(q+1)+\ell(2\theta-1)
       \le-\theta(q-1)\le0.
\tag{14}
\]
This proves every case, including \(q=1\).
It controls all finite compositions and inverse jets with the \(A\) exponents. If a bounded outer function has bounded derivatives, dropping the nonnegative \(A(q)\) gives the same composition bound.

Parametrize the initial sheet by
\(\xi_T(\eta')=(E_T(\eta'),\eta')\).
Its order-\(j\) derivatives are bounded by \(CT^{B(j)}\).
Use \(s=\log t\) and write the composed flow as
\[
\begin{gathered}
\widehat z(t,\eta')=z(t,0,\xi_T(\eta')),\\
 \widehat\xi(t,\eta')=\xi(t,0,\xi_T(\eta')).
\end{gathered}
\tag{15}
\]
*Hamilton trajectories under a long-range force* gives all pure data jets of the full pair bounded by \(t^{A(j)}\), and all positive Euler-time jets of total order \(j\) bounded by
\(t^{\mu(j-1)}\le t^{A(j)}\).
The finite chain rule, \(T^{B(j)}\le t^{A(j)}\), and the positive-part partition give every joint \((s,\eta')\) jet of
\((\widehat z,\widehat\xi)\) the bound \(Ct^{A(j)}\).

The normalized position
\[
x/t=\nabla P_0(\widehat\xi)+\widehat z
\tag{16}
\]
has the same bounds. In a fixed regular chart with
\(\partial_1P_0>c_1>0\), its first component is bounded above and away from zero.
Finite differentiation of a reciprocal on that bounded interval shows that
\[
t/x_1,\qquad x'/x_1
\tag{17}
\]
also have joint order-\(j\) bounds \(Ct^{A(j)}\).
This follows from bounded derivatives of the reciprocal and the same finite partition, not from an unproved symbolic reciprocal series.

## 4. An actual inverse of the projection

On an outer fixed transverse-frequency chart,
\(\eta'\mapsto\widehat\xi'(t,\eta')\) differs from the identity by
\(O(T^{-\delta})\) in value and first derivative, uniformly in \(t\ge T\).
Extend its error by a fixed cutoff equal one near the inner chart.
If the extended error is \(e_t\), solve \(\eta'=\zeta'-e_t(\eta')\) on the complete Euclidean transverse space. Its Lipschitz constant is below \(1/2\) for large \(T\). Successive iterates have geometrically summable differences, so they converge to the unique inverse \(\eta'=Q_t(\zeta')\).

Smooth dependence follows directly from this construction. Write \(p=(t,\zeta')\) and \(F(p,y)=\zeta'-e_t(y)\). On a compact parameter neighborhood, the fixed-point equation and the contraction estimate give \(|Q(p+h)-Q(p)|\le 2C|h|\). Taylor's segment formula in that equation gives
\[
 \begin{gathered}
 \Delta Q=Q(p+h)-Q(p),\\
 \mathcal J_p=I-D_yF(p,Q(p)),\\
 \mathcal J_p\Delta Q=D_pF(p,Q(p))h+o(|h|).
 \end{gathered}
\]
The inverse of the matrix on the left is the norm-convergent geometric series \(\sum_{j\ge0}(D_yF)^j\), uniformly bounded by two. Thus \(Q\) is differentiable, its derivative has the displayed inverse-matrix formula, and this derivative is continuous. Induction on that formula proves smoothness at every finite order. Differentiating the now smooth fixed-point identity isolates the invertible coefficient \(I+De_t\), giving all parameter derivatives. The small error keeps this inverse near its final frequency for every \(\zeta'\) in the inner chart.
It lies in the region where the cutoff equals one.
There the differentiated original equation gives
\[
\partial_tQ_t
       =-(D_{\eta'}\widehat\xi')^{-1}
                        \partial_t\widehat\xi'
       =O(t^{-1-\delta}).
\tag{18}
\]
Its first data derivative is uniformly bounded.
Also \(D_{\eta'}x_1=O(t)\).
Therefore
\[
\partial_t[x_1(t,Q_t(\zeta'))]
       =\partial_1P_0(\widehat\xi)+O(t^{-\delta})\ge c_1/2.
\tag{19}
\]
The first position is comparable with \(t\) and tends to \(+\infty\).
Its value at \(t=T\) is bounded above by \(CT\), uniformly in the inner frequency chart.
For every \(x_1>2CT\), it has exactly one inverse \(t=t(x_1,\zeta')\).
This proves a unique smooth inverse of the full projection
\((t,\eta')\mapsto(x_1,\xi')\).
If a point of the full flowout has frequency in a smaller chart, its initial frequency lies in the outer chart by the uniformly small frequency change, so this parametrization describes the whole corresponding late part of the flowout.

For derivative estimates use \(X=\log x_1\).
The projection is
\[
\Psi(s,\eta')=
  \bigl(s+\log(\partial_1P_0(\widehat\xi)+\widehat z_1),
                     \widehat\xi'\bigr).
\tag{20}
\]
It is uniformly \(C^1\)-close to the fixed shear
\[
\Psi_0(s,\eta')=
       (s+\log(\partial_1P_0(E(\eta'),\eta')),\eta').
\tag{21}
\]
Indeed, the zeroth and first frequency-data differences are \(O(T^{-\delta})\);
the positive first Euler-time derivatives of the pair are \(O(t^{-\delta})\), so the \(s\)-derivative differs from \((1,0)\) by the same amount.
The shear has a uniformly bounded inverse first derivative on the fixed compact chart.
Hence the first derivative of the actual inverse of \(\Psi\) is uniformly bounded.
Every higher projection derivative of order \(q\ge2\) is
\(O(t^{A(q)})\), by the normalized estimates and finite chain rules.
Differentiating \(\Psi(\Psi^{-1})=\mathrm{id}\) at order \(k\ge2\), isolating the highest inverse derivative, and using the positive-part partition proves
\[
|D_{X,\zeta'}^k\Psi^{-1}|\le C_k x_1^{A(k)}.
\tag{22}
\]
Here \(t\asymp x_1\), so their positive powers are equivalent.
The highest derivative equation has an invertible first-projection coefficient; every other term contains an outer derivative of order \(q\ge2\) and inverse derivatives of positive orders less than \(k\), summing to \(k\).
This accounts for every term and supplies the induction.
The unbounded zeroth coordinate \(s\) is harmless: only its positive-order derivatives enter this induction.

Composing the normalized geometric functions with this inverse yields
\[
|\partial_{\zeta'}^{\gamma}(x_1\partial_{x_1})^\tau
                 (\xi_1,x'/x_1)|\le C_{\gamma\tau}x_1^{A(|\gamma|+\tau)}.
\tag{23}
\]
The ratio \(t/x_1\) has the same bounds.
In particular all inverse/normalized jets of total order below \(\kappa\) are bounded, since \(A(j)=0\) at those orders.

## 5. The cancellation at low derivative orders

For every data order \(r<\kappa\), the mixed time estimate in *Hamilton trajectories under a long-range force*, composed with the initial sheet, gives
\[
|\partial_{\eta'}^r\partial_t\widehat\xi|
          \le Ct^{-1-\delta}.
\tag{24}
\]
The initial-sheet derivatives needed at these orders are bounded; all outer terms use total derivative order at most \(\kappa\).
Integrating to infinity gives a limit \(\xi_\infty(\eta')\) in \(C^{\kappa-1}\). To justify the asserted differentiability, (24) makes each data derivative through order \(\kappa-1\) uniformly Cauchy on a compact inner chart, since \(\int_t^\infty s^{-1-\delta}\,ds=t^{-\delta}/\delta\). On a smaller coordinate box, apply the one-variable fundamental theorem along each coordinate segment to the finite-time functions and pass to their uniform limits. The resulting segment identity identifies the limit of each first derivative with the derivative of the limit. Repeat this argument at successive orders. Thus every claimed derivative exists, is continuous and has the same tail bound. Consequently
\(\rho=\widehat\xi-\xi_\infty\) has
\[
|\partial_{\eta'}^{\gamma}\partial_t^\tau\rho|
       \le Ct^{-\delta-\tau},
          \qquad |\gamma|+\tau<\kappa.
\tag{25}
\]
For \(\tau=0\), use the convergent tail integral. For \(\tau>0\), the limit has no time dependence, so use the mixed flow estimate directly.
The same low total-order bounds hold for \(\widehat z\), from its zero-displacement data estimates and its mixed time estimates.
Conserved actual energy and \(V_L(x(t),\xi(t))=O(t^{-\delta})\) show
\(\xi_\infty(\eta')\in M_\lambda\).

If a smooth \(F\) vanishes on the free shell in the current chart, write
\[
F(\widehat\xi)=
 \rho\cdot\int_0^1\nabla F(\xi_\infty+u\rho)\,du.
\tag{26}
\]
Every low total-order data/Euler derivative of this finite expression has at least one decaying \(\rho\) factor or derivative.
All other required jets are bounded, so it is \(O(t^{-\delta})\).
Conversion from Euler to ordinary time derivatives gives
\(O(t^{-\delta-\tau})\) at time order \(\tau\), for total order below \(\kappa\).

Apply this first to \(F_0(\xi)=\xi_1-E(\xi')\), and then, for \(j\ne1\), to
\[
F_j(\xi)=\partial_jP_0(\xi)
            +\partial_1P_0(\xi)\partial_jE(\xi').
\tag{27}
\]
The latter vanishes on the shell by differentiating
\(P_0(E(\xi'),\xi')=\lambda\).
Since
\[
\frac{x_j+x_1\partial_jE(\widehat\xi')}{t}
     =F_j(\widehat\xi)+\widehat z_j
                         +\widehat z_1\partial_jE(\widehat\xi'),
\tag{28}
\]
this normalized position residual has the same low-order decay.
Transport these estimates to the inverse \((X,\zeta')\) coordinates.
Every inner inverse jet used at total order below \(\kappa\) is bounded.
Finite composition therefore retains \(O(x_1^{-\delta})\) for all those weighted derivatives.
Multiplication by \(t/x_1\), whose low jets are also bounded, gives the position normalization by \(x_1\).
The exact Euler polynomial conversion finally yields
\[
\begin{gathered}
|\partial_{\zeta'}^\gamma\partial_{x_1}^\tau
                         (\xi_1-E(\zeta'))|
       \le Cx_1^{-\delta-\tau},\\
 |\partial_{\zeta'}^\gamma\partial_{x_1}^\tau
                  (x'/x_1+\nabla E(\zeta'))|
       \le Cx_1^{-\delta-\tau},
 \\ |\gamma|+\tau<\kappa.
\end{gathered}
\tag{29}
\]
This is the precise cancellation lost by bounding the two terms separately.

## 6. Recovering every derivative of the generator

Let \(h=G-G_0\), \(G_0=x_1E(\zeta')\).
The exact action normalization gives
\[
\begin{gathered}
\partial_{x_1}h=\xi_1-E(\zeta'),\\
 \nabla_{\zeta'}h=-x'-x_1\nabla E(\zeta').
\end{gathered}
\tag{30}
\]
If \(1\le|\alpha|\le\kappa\) and \(\alpha_1\ge1\), differentiate the first identity at the remaining order \(|\alpha|-1<\kappa\).
The bound is
\(Cx_1^{1-\alpha_1-\delta}\).
If \(\alpha_1=0\), differentiate one transverse-gradient identity, again at remaining total order below \(\kappa\).
It gives \(Cx_1^{1-\delta}\).
Both are exactly
\(Cx_1^{1+|\alpha'|-m(|\alpha|)}\).
For \(\alpha=0\), integrate \(\partial_{x_1}h=O(x_1^{-\delta})\) at fixed transverse frequency, starting at one fixed large \(x_1\); the initial smooth values are bounded on the compact inner chart.
Since \(\delta<1\), this gives \(h=O(x_1^{1-\delta})\).

For \(|\alpha|=k>\kappa\), use the full high-order normalized jets instead.
If \(\alpha_1\ge1\), start from \(\partial_{x_1}G=\xi_1\).
Convert the remaining \(\alpha_1-1\) radial derivatives from Euler powers, using monotonicity of \(A\).
The result is
\[
Cx_1^{-(\alpha_1-1)+A(k-1)}
   =Cx_1^{1+|\alpha'|-m(k)},
\tag{31}
\]
because \(A(k-1)=\mu(k-1)=k-m(k)\) when \(k>\kappa\).
If \(\alpha_1=0\), start from one transverse-gradient identity
\(\partial_{\zeta_j}G=-x_j=-x_1(x_j/x_1)\).
The remaining \(k-1\) transverse derivatives give
\(Cx_1^{1+A(k-1)}\), the same target exponent.
For \(G_0=x_1E\), radial derivatives of order at least two vanish; at radial orders zero and one, its bounded frequency derivatives have size at most \(Cx_1^{1-\alpha_1}\).
Since \(m(k)<k\) for \(k>\kappa\), that is no larger than the required high-order bound.
Subtracting \(G_0\) proves the target for all high orders too.


This proves Theorem 2.1. For the negative-normal end, apply the entire construction to \(-P_0,-V_L,-\lambda\). Its initial graph is \(x=-T\nabla P_0(\eta)\). The resulting future parameter is \(s\ge T\), corresponding to the original Hamilton time \(t=-s\). The cotangent form and action differential retain their signs; the initial normalized action is \(+TV_L\). If a negative normal has a negative distinguished position coordinate, reflecting that position and its paired frequency supplies a positive chart coordinate. Exercise 5 verifies these conventions.

### Use the conclusion

Compare the exact compact-force end with the low-order cancellation for a general force. Verify the actual inverse before differentiating its generating function and using those jets in the commuting-coordinate construction.

## 7. Exercises with complete solutions

**Exercise 1 — Basic — an anisotropic free shell and a tangential shift.**

On \(\mathbb R^2\), take \(P_0(\xi)=\xi_1^2+2\xi_2^2\) and \(\lambda=1\).
Use the positive branch \(\xi_1=E(\zeta)\), with
\(|\zeta|<1/\sqrt2\). Compute the free generator, its position equation, and the generator determined by the shell action \(\psi_\infty(E(\zeta),\zeta)=a\zeta\). Verify the tangent restriction of the shifted position.

**Solution 1.** The branch is
\[
E(\zeta)=\sqrt{1-2\zeta^2},\qquad
 E'(\zeta)=-\frac{2\zeta}{E(\zeta)}.
\tag{32}
\]

The free generator \(G_0=x_1E(\zeta)\) gives
\(\xi_1=E(\zeta)\) and
\[
x_2=-\partial_\zeta G_0=\frac{2x_1\zeta}{E(\zeta)}.
\tag{33}
\]

The free velocity is \((2E,4\zeta)\), whose component ratio is exactly \(2\zeta/E\). Thus the equation describes the free normal direction.

The shifted generator is \(G=x_1E-a\zeta\). It keeps \(\xi_1=E\) and gives
\[
x_2=\frac{2x_1\zeta}{E(\zeta)}+a.
\tag{34}
\]

A tangent to the shell in the \(\zeta\) coordinate is \((E',1)\). Therefore
\[
x\cdot(E',1)=x_1\left(-\frac{2\zeta}{E}\right)+x_2=a,
\tag{35}
\]
which is precisely the derivative of \(a\zeta\). The minus sign in \(G=G_0-\psi_\infty\) and the minus sign in \(x_2=-G_\zeta\) combine to give the plus tangential shift.

**Exercise 2 — Intermediate — an inverse constructed before estimating it.**

Consider the two-variable parametrization, independently of a Hamiltonian,
\[
\begin{gathered}
 \zeta=\eta+b\,t^{-\delta}\sin\eta,\\
 x_1=t(2+\cos\eta)+a\,t^{1-\delta}\cos\eta,\qquad t\ge T,
 \end{gathered}
\tag{36}
\]
where \(a,b\) are fixed real numbers and \(0<\delta<1\).
Prove that for large \(T\), every \(\zeta\in\mathbb R\) has a unique smooth inverse \(\eta=Q_t(\zeta)\). Show that at fixed final \(\zeta\), \(x_1(t,Q_t(\zeta))\) is strictly increasing, comparable to \(t\), and has a unique inverse for all sufficiently large \(x_1\). Give the bound for \(\partial_tQ_t\).

**Solution 2.** Solve
\(\eta=\zeta-bt^{-\delta}\sin\eta\) by successive iteration on \(\mathbb R\).
For \(|b|T^{-\delta}<1/2\), the right side has Lipschitz constant below one half. The successive differences form a geometric series, so the iterates converge on the complete line. The same inequality gives uniqueness. In the original equation the derivative
\(1+bt^{-\delta}\cos\eta\) is bounded below by one half. Difference quotients and successive implicit differentiation give a smooth inverse, and
\[
\begin{gathered}
Q_t(\zeta)-\zeta=O(t^{-\delta}),\\
 \partial_\zeta Q_t=(1+bt^{-\delta}\cos Q_t)^{-1},\\
 \partial_tQ_t=
 \frac{\delta b\,t^{-1-\delta}\sin Q_t}
       {1+bt^{-\delta}\cos Q_t}
       =O(t^{-1-\delta}).
\end{gathered}
\tag{37}
\]

The direct \(t\) derivative of the position is
\(2+\cos\eta+a(1-\delta)t^{-\delta}\cos\eta\), at least
\(1-Ct^{-\delta}\). Its \(\eta\) derivative is
\(-t\sin\eta-a t^{1-\delta}\sin\eta=O(t)\).
Consequently, at fixed \(\zeta\),
\[
\frac{d}{dt}x_1(t,Q_t(\zeta))=2+\cos Q_t+O(t^{-\delta})
                                  \ge\frac12
\tag{38}
\]
for large \(T\). Also \(t/2\le x_1\le4t\), after increasing \(T\) if needed. At \(t=T\) its value is at most \(4T\), uniformly in \(\zeta\), and it tends to infinity. For every \(x_1>4T\), strict monotonicity gives exactly one time, with a smooth inverse by the nonzero derivative.

This supplies a global inverse by contraction and monotonicity. The positivity of a Jacobian at individual points would give only local inverses.

**Exercise 3 — Intermediate — radial and transverse derivative rates.**

Let \(\kappa=2\), \(\delta=1/5\), and \(h=G-G_0\). Compute the allowed powers of \(x_1\) for \(h\) and for derivatives of orders
\((\alpha_1,|\alpha'|)=(1,1),(0,2),(2,1),(0,3),(3,0)\).
Explain why the full high-order proof is needed even though the first two derivatives of the initial sheet are small.

**Solution 3.** Here
\[
\begin{gathered}
m(0)=\frac15,\\ m(1)=\frac65,\\
 m(2)=\frac{11}5,\\ m(3)=\frac{14}5.
\end{gathered}
\tag{39}
\]

The target exponent is \(1+|\alpha'|-m(\alpha_1+|\alpha'|)\).
It gives
\[
\begin{aligned}
 h&=O(x_1^{4/5}),\\
 \partial_{x_1}\partial_{\xi'}h&=O(x_1^{-1/5}),\\
 \partial_{\xi'}^2h&=O(x_1^{4/5}),\\
 \partial_{x_1}^2\partial_{\xi'}h&=O(x_1^{-4/5}),\\
 \partial_{\xi'}^3h&=O(x_1^{6/5}),\\
 \partial_{x_1}^3h&=O(x_1^{-9/5}).
 \end{aligned}
\tag{40}
\]

In multiple transverse dimensions each notation denotes a derivative of the stated total transverse order. A radial derivative costs one power of \(x_1\) relative to a transverse derivative at the same total order. The low-order cancellation gives \(x_1^{1-\alpha_1-\delta}\) only through total order two. At order three,
\(A(2)=\mu(2)=1/5\); the inverse and geometric jets can have positive powers. The full finite-partition argument is therefore needed. Small initial low derivatives do not impose uniform bounds on every higher jet for an infinite future interval.

**Exercise 4 — Advanced — what the differential of the end action determines.**

On the unit sphere \(M=\{\xi:|\xi|=1\}\), let
\(\psi_\infty(\xi)=a\cdot\xi\), with \(a\in\mathbb R^n\).
Determine the full inverse image of \(\operatorname{graph}(d\psi_\infty)\) under the cotangent restriction map. More generally, explain why adding a normal multiple to a late orbit offset or adding a constant to \(\psi_\infty\) leaves the corresponding affine normal lines unchanged. Distinguish this geometric freedom from the prescribed normalization of \(\psi\).

**Solution 4.** A tangent vector \(w\in T_\xi M\) obeys \(w\cdot\xi=0\), and
\(d\psi_\infty(w)=a\cdot w\). The restriction equation is
\((x-a)\cdot w=0\) for every such \(w\). Its solutions are exactly
\[
x=a+s\xi,\qquad s\in\mathbb R,\quad \xi\in M.
\tag{41}
\]

The shell gradient is \(a-(a\cdot\xi)\xi\), the tangential part of \(a\). It determines the affine line; the remaining normal component changes only the parameter along that line. For the free quadratic Hamiltonian \(v=2\xi\), a late orbit
\(x=t\,v+a(\xi)\) with \(a\) replaced by \(a+c(\xi)v\) traverses the same affine normal line after shifting its time parameter. At sufficiently large positive normal position it has the same end.

Adding a constant to \(\psi_\infty\) changes no differential and hence no affine line. In the actual escaping construction the global action has the specified initial value \(-TV_L\). That normalization selects the action itself, including its constants on all components. The geometric description by \(d\psi_\infty\) forgets those constants, but does not authorize altering the normalized action.

**Exercise 5 — Advanced — time reversal and a change of privileged coordinate.**

Apply the escaping construction to \(H^-=-P_0-V_L\) at energy \(-\lambda\), with its future parameter \(s\ge T\). Show that its trajectories describe the negative-time escaping family for \(H=P_0+V_L\). Determine the initial action and verify that its differential remains \(\beta=\sum x_jd\xi_j\). If \(G_i=x_i\xi_i-\psi\) and \(G_j=x_j\xi_j-\psi\) are two local generators on a common part of a family, find their exact transition. Finally verify that the paired reflection \(y_1=-x_1,\eta_1=-\xi_1\) preserves the cotangent form.

**Solution 5.** The reversed initial graph is \(x=-T\nabla P_0(\eta)\), and its energy equation is
\(-P_0(\eta)-V_L(-T\nabla P_0(\eta),\eta)=-\lambda\).
Its equations are
\[
\frac{dx}{ds}=-H_\xi,\qquad
 \frac{d\xi}{ds}=H_x.
\tag{42}
\]

Put \(t=-s\). Then \(dx/dt=H_\xi\), \(d\xi/dt=-H_x\), exactly the original Hamilton equations, on \(t\le-T\). The initial action for the reversed construction is
\[
-T(-V_L)=+TV_L
\tag{43}
\]
evaluated on that negative initial graph. Its derivative along \(s\) is
\(x\cdot d\xi/ds\), and its derivative along the original \(t\) is
\[
\frac{d\psi}{dt}
    =-\frac{d\psi}{ds}
    =-x\cdot\frac{d\xi}{ds}
    =x\cdot\frac{d\xi}{dt}.
\tag{44}
\]

Thus the action differential retains the same cotangent form on the negative family. Reversing time does not negate the frequency variable or the cotangent form.

On an overlap the two generators satisfy the exact identity
\[
G_j-G_i=x_j\xi_j-x_i\xi_i.
\tag{45}
\]

No arbitrary transition constant remains because the same \(\psi\) was used. Finally,
\(y_1d\eta_1=(-x_1)d(-\xi_1)=x_1d\xi_1\); the other paired coordinates are unchanged. The reflection preserves \(\beta\) and hence its exterior derivative. It provides a positive distinguished position coordinate when the original negative-normal chart uses \(x_1<0\).


## References

[T] Gerald Teschl, [*Ordinary Differential Equations and Dynamical Systems*, free author's preliminary edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), April 2012, §§2.2, 2.4 and 2.6. Its local contraction, data derivative and continuation proofs correspond to the written programme flow prerequisite. Sections 3–6 here prove the mixed-coordinate inverse and its complete derivative estimates.

[O] Sung-Jin Oh, [*Lecture Notes for Math 222A*, free evolving lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), University of California, Berkeley, Fall 2023, §2.4.1, pp. 23–24. The Hamilton characteristic equations (2.20) provide a comparison. The programme escaping-family lesson proves the frequency-base action used here; (8)–(10) derive its mixed-coordinate signs.



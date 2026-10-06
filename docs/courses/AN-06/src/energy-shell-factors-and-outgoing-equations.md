# Energy-shell factors and outgoing equations

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Why does factorizing an energy graph leave an outgoing choice?** A first-order factor has homogeneous solutions as well as a particular solution. The outgoing condition supplies the direction of integration, just as in the transport model, but here the solution may initially have only endpoint ball bounds. The proof has to recover genuine Hilbert-space slices rather than assuming them at the start.

Near a regular energy surface, one frequency is a smooth function of the others. A small long-range perturbation moves that graph. Dividing by the graph factor suggests a first-order equation in one spatial coordinate. Such an equation still has many homogeneous solutions. An outgoing condition selects one of them, even when the initial information permits squared mass to grow proportionally to the radius of a ball.

We first prove the outgoing evolution estimate directly from its kernel. We then construct the perturbed energy graph and control every derivative of its polynomial factor and reciprocal. Read [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) for the spatial norms, and [Admissible differential perturbations](admissible-differential-perturbations.md) for the differential coefficient class. The [measure and Euclidean product proofs](../providers/analysis/finite-derivative-l2.md#measure-foundations) give the scalar integral, convergence and slice facts; the same reading proves [Fourier inversion and Plancherel](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The [coordinate inverse and bump proofs](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse) supply the regular free graph and smooth cutoffs. Section 3 constructs the vector integrals used here. Freely accessible background references are Teschl's evolution and initial-value texts [T, ODE] and Yafaev's *Lectures on scattering theory* [Y]. The evolution, rough-slice recovery, root and quotient proofs are given below.

## 1. What an outgoing condition must control

Write \(x=(s,z)\in\mathbb R\times\mathbb R^d\), where \(d=n-1\), and put \(\mathcal H=L^2(\mathbb R^d)\). For \(d=0\), use \(\mathcal H=\mathbb C\). Our convention is \(D_s=-i\partial_s\). Set

\[
 \begin{gathered}
 r_j=2^j,\qquad
 S_0=\{|x|<1\},\\
 S_j=\{2^{j-1}\le |x|<2^j\}\quad(j\ge1),\\
 \|f\|_B=\sum_{j\ge0}r_j^{1/2}\|f\|_{L^2(S_j)},\\
 \|v\|_{B^*}=\sup_{j\ge0}r_j^{-1/2}\|v\|_{L^2(S_j)}.
 \end{gathered}
 \tag{1}
\]

Shells and balls give the equivalent bound

\[
 \int_{|x|<R}|v|^2\,dx
 \le 4R\|v\|_{B^*}^2,\qquad R\ge1.
 \tag{2}
\]

Indeed, choose \(2^{j-1}<R\le2^j\) and sum the shell estimates through \(j\). The sum of the radii is at most \(2^{j+1}\le4R\).

The outgoing condition in the \(s\) direction is

\[
 \begin{gathered}
\lim_{R\to\infty}
 \frac1R\int_{\substack{|x|<R\\ s<T}}|v(x)|^2\,dx=0
 \\ \quad\text{for every fixed }T\in\mathbb R.
\end{gathered}
 \tag{3}
\]

It excludes a wave already present at \(s=-\infty\). It permits a nonzero wave escaping toward \(s=+\infty\). Exercise 1 shows both distinctions in an exact model.

Two slice estimates will be useful:

\[
 \begin{aligned}
 \int_{\mathbb R}\|f(s)\|_{\mathcal H}\,ds
   &\le\sqrt2\|f\|_B,\\
 \|v\|_{B^*}
   &\le\sqrt2\|v\|_{L^\infty(\mathbb R;\mathcal H)}.
 \end{aligned}
 \tag{4}
\]

For the first, each \(f1_{S_j}\) has slices supported in \([-r_j,r_j]\). Cauchy–Schwarz in \(s\) bounds its slice integral by \((2r_j)^{1/2}\|f\|_{L^2(S_j)}\); sum over \(j\). For the second, integrate the uniform slice bound on the same interval.

## 2. A real symbol and its adjoint defect

Let \(b(s,z,\eta)\) be real and smooth, with support in one fixed compact set of \(\eta\in\mathbb R^d\). Suppose every \(\eta\) derivative is uniformly bounded. Suppose also that there is a nonnegative \(w\in L^1(\mathbb R)\) such that

\[
 |\partial_\eta^\alpha\nabla_z b(s,z,\eta)|
 \le C_\alpha w(s).
 \tag{5}
\]

Assume its left-quantized operator \(A(s)=b(s,z,D_z)\) is continuous in operator norm as a function of \(s\). Uniform bounds on \(\partial_s\partial_\eta^\alpha b\), for all finite orders, are a sufficient condition, as the kernel estimate below shows. In dimension zero \(b(s)\) is a real bounded continuous scalar and the adjoint defect is zero.

For \(d\ge1\) the kernel is

\[
 K_s(z,y)=(2\pi)^{-d}\int
 e^{i(z-y)\cdot\eta}b(s,z,\eta)\,d\eta.
 \tag{6}
\]

Integration by parts in \(\eta\), with compact support, gives for every integer \(N\ge0\)

\[
 |K_s(z,y)|\le C_N(1+|z-y|)^{-N}.
 \tag{7}
\]

For example, applying \((1-\Delta_\eta)^k\) to the amplitude yields a factor \((1+|z-y|^2)^{-k}\). Choose \(2k\ge N\).

We will use the following kernel inequality. If

\[
 \begin{gathered}
\sup_z\int |K(z,y)|\,dy\le M_1,\\ \qquad
 \sup_y\int |K(z,y)|\,dz\le M_2,
\end{gathered}
 \tag{8}
\]

then its \(L^2\) operator norm is at most \((M_1M_2)^{1/2}\). To prove it, apply weighted Cauchy–Schwarz to \(\int K(z,y)h(y)\,dy\), then integrate in \(z\) and use Fubini. Thus (7), with \(N>d\), bounds \(A(s)\) uniformly.

Reality of \(b\) identifies the kernel of \(A(s)-A(s)^*\) as the inverse Fourier integral of
\(b(s,z,\eta)-b(s,y,\eta)\). The segment formula and (5), including its differentiated versions, bound that amplitude's \(\eta\) derivatives by \(C_\alpha w(s)|z-y|\). Repeating the integration by parts gives

\[
 \begin{aligned}
&|K_s(z,y)-\overline{K_s(y,z)}|\\
&\le C_N w(s)|z-y|(1+|z-y|)^{-N},\\
&\|A(s)-A(s)^*\|_{\mathcal H\to\mathcal H}\\
&\le Cw(s).
 \end{aligned}
 \tag{9}
\]

Take \(N>d+1\) for the second line. A real left symbol need not give a self-adjoint operator. What we have proved is an integrable bound on its failure of self-adjointness.

## 3. Constructing the outgoing evolution

**Theorem 3.1.** Under the hypotheses of Section 2, let \(g\in L^1(\mathbb R;\mathcal H)\). There is a solution of

\[
 (D_s-A(s))v=g
 \tag{10}
\]

with a continuous, locally absolutely continuous \(\mathcal H\)-valued representative, and

\[
 \|v(s)\|_{\mathcal H}
 \le C\int_{-\infty}^s\|g(t)\|_{\mathcal H}\,dt.
 \tag{11}
\]

Every distributional solution \(v\in B^*\) of (10) satisfying (3) has this representative and bound. In particular it is unique among the \(B^*\) solutions satisfying (3). The constant depends on the symbol bounds and \(\int w\), and is independent of \(g\).

Here are the integration facts needed for the full \(L^1\) forcing class. The space \(\mathcal H=L^2(\mathbb R^d)\) is separable: the Euclidean rectangle-approximation proof makes step functions on finitely many rational boxes with rational real and imaginary values dense. In dimension zero use \(\mathbb C\). A strongly measurable \(\mathcal H\)-valued function with integrable norm is approximable in integral norm by finite-valued simple functions. Explicitly, first restrict to a bounded time interval and bounded values, losing arbitrarily little norm integral. Cover its values by balls of radius \(1/j\) centered in a countable dense subset, assign each value to the first such ball, and then keep finitely many of the resulting measurable sets. The discarded tail has vanishing measure; the values on the retained interval are bounded. This gives finite simple approximations with integral error tending to zero.

For a simple function \(F=\sum_k h_k1_{E_k}\) on disjoint finite-measure sets define \(\int F=\sum_k |E_k|h_k\). The triangle inequality gives \(\|\int F\|\le\int\|F\|\), so completion defines the integral for the preceding \(L^1\) class and makes it independent of the approximation. Pairing with a fixed vector, or applying a bounded operator, commutes with the integral by the same norm estimate. In particular the primitive \(G(s)=\int_a^s F(t)\,dt\) is locally absolutely continuous: sums of its increments over disjoint intervals are bounded by the norm integral over their union, which tends to zero with that union's measure by truncating the integrable scalar function \(\|F\|\). Testing against a compact smooth scalar function and using scalar Fubini proves \(G'=F\) as a vector distribution. These facts also construct improper integrals whenever the norm has an integrable tail.

For continuous operator-valued functions on compact intervals use Riemann sums in operator norm, as in the [continuous-vector integral proof](../providers/analysis/euclidean-approximation-and-convolution.md#oscillatory-integrals-and-averages). The same uniform-continuity estimate applies in the complete normed space of bounded operators: an operator-norm Cauchy sequence has a pointwise vector limit which is linear and bounded, and convergence to it is in operator norm. Thus no operator measurability assumption beyond the stated norm continuity is required.

We begin with existence. Since \(\sup_s\|A(s)\|\le M\), iteration of
\[
 U(s,t)=I+i\int_t^s A(r)U(r,t)\,dr
 \tag{12}
\]

converges in operator norm on every bounded time interval. Its term of order \(k\) has norm at most \(M^k|s-t|^k/k!\). The same construction works for either orientation of the integral. Iterating the inequality for the difference of two solutions with zero initial value proves uniqueness of (12). Consequently

\[
 \begin{gathered}
U(s,t)U(t,r)=U(s,r),\\ \qquad U(t,s)=U(s,t)^{-1}.
\end{gathered}
 \tag{13}
\]

For \(u(s)=U(s,t)h\), its equation is \(\partial_su=iA(s)u\). The inner product is linear in the first variable. Equation (9) gives

\[
 \left|\frac{d}{ds}\|u(s)\|^2\right|
 \le Cw(s)\|u(s)\|^2.
 \tag{14}
\]

For \(\varepsilon>0\), divide (14) by \(\|u(s)\|^2+\varepsilon\). The absolute derivative of \(\log(\|u(s)\|^2+\varepsilon)\) is at most \(Cw(s)\). Integrate between the two times in either order, exponentiate and let \(\varepsilon\) decrease to zero. This proves

\[
 \begin{gathered}
\|U(s,t)\|
 \\ \le \exp\!\left(\frac C2\int_{\mathbb R}w(r)\,dr\right)
 \\ =:C_0
 \\ \quad(s,t\in\mathbb R).
\end{gathered}
 \tag{15}
\]

Define

\[
 \begin{aligned}
 v(s)&=i\int_{-\infty}^s U(s,t)g(t)\,dt,\\
 q(s)&=\int_{-\infty}^s\|g(t)\|\,dt.
 \end{aligned}
 \tag{16}
\]

The integral converges in \(\mathcal H\) by (15), and \(\|v(s)\|\le C_0q(s)\). Its integrand is strongly measurable: approximate \(g\) by simple functions; on every bounded time interval the operator factor is norm continuous, and each resulting vector factor is strongly measurable. Splitting at a finite time \(a\) and using (13) gives
\[
 v(s)=U(s,a)\left(v(a)+i\int_a^s U(a,t)g(t)\,dt\right).
\]
The bracket is locally absolutely continuous by the primitive construction, and \(U(s,a)\) is continuously differentiable in operator norm. The product is therefore locally absolutely continuous. Testing its product rule, or first using simple approximations to \(g\), gives \(\partial_sv=iAv+ig\) in distributions, including the sign in (10). The same formula gives the inhomogeneous integral equation on each finite interval.

The bound and (4) give \(v\in B^*\). To prove (3), fix \(S<\min(T,0)\). For \(R\) large enough,

\[
 \begin{gathered}
\frac1R\int_{\substack{|x|<R\\s<T}}|v|^2\,dx
 \\ \le C_0^2\left(q(S)^2+
 \frac{T-S}{R}q(T)^2\right).
\end{gathered}
 \tag{17}
\]

The first term bounds the interval \([-R,S]\); omitting a nonexistent interval only reduces it. Let \(R\to\infty\), then \(S\to-\infty\). Since \(q(S)\to0\), this proves the condition.

## 4. Recovering slices from a rough outgoing solution

We now prove the remaining assertion of Theorem 3.1. A function in \(B^*\) need not have globally square-integrable slices. The proof must produce that conclusion.

The shell estimate implies

\[
 \begin{gathered}
\int_{\mathbb R^{d+1}}(1+|x|)^{-2p}|v(x)|^2\,dx
 \\ \le C_p\|v\|_{B^*}^2,\\ \qquad p>\tfrac12.
\end{gathered}
 \tag{18}
\]

Indeed, the tail sum is bounded by a constant times
\(\sum_j2^{j(1-2p)}\). Fubini therefore gives polynomially weighted \(L^2\) slices for almost every \(s\). Their strong measurability also follows from the rectangle proof: approximate the weighted function by finite product step functions in the space-time \(L^2\) norm and take a subsequence whose slice errors tend to zero almost everywhere. On bounded time intervals the weight is equivalent to a weight in \(z\) alone. The rapidly decreasing kernel (7) acts on these slices as a distribution and as a locally square-integrable function. Indeed, for bounded output \(z\), Cauchy–Schwarz bounds its value by the weighted slice norm times the \(L^2_y\) norm of \(K_s(z,y)(1+|y|)^p\), uniformly finite on bounded output sets by (7). Integration in bounded \(s,z\) proves local square integrability.

Choose a real smooth \(\chi\), between zero and one, equal to one on the unit ball and zero outside the ball of radius two. Put
\(\chi_R(x)=\chi(x/R)\) and \(v_R=\chi_Rv\). The distributional product rule gives

\[
 \begin{aligned}
 (D_s-A(s))v_R&=\chi_Rg+e_R,\\
 e_R&=-iR^{-1}(\partial_s\chi)(x/R)v
       \\ &\quad-[A(s),\chi_R]v.
 \end{aligned}
 \tag{19}
\]

Define the finite quantity
\[
 M(r,T)=\|1_{\{|x|<r,\ s<T\}}v\|_2.
 \tag{20}
\]

By (3), \(M(r,T)=o(r^{1/2})\) for each fixed \(T\). The first error in (19), using Cauchy–Schwarz over a time interval of length at most \(4R\), has the bound

\[
 \begin{gathered}
\|R^{-1}(\partial_s\chi)(x/R)v\|
 _{L^1((-\infty,T);\mathcal H)}
 \\ \le CR^{-1/2}M(2R,T)=o(1).
\end{gathered}
 \tag{21}
\]

The commutator kernel is
\[
 K_s(z,y)\bigl(\chi_R(s,y)-\chi_R(s,z)\bigr).
 \tag{22}
\]

It is zero when \(|s|\ge2R\). The Lipschitz estimate for \(\chi\) and (7) bound its absolute value by
\(C_NR^{-1}|z-y|(1+|z-y|)^{-N}\). Thus (8) bounds its \(L^2_z\) operator norm by \(C/R\).

First apply it to the near input \(1_{\{|x|\le4R\}}v\). Integrating its slice norm for \(s<T\) gives

\
 \begin{gathered}
\|[A,\chi_R\|
 _{L^1((-\infty,T);\mathcal H)}
 \\ \le CR^{-1/2}M(4R,T)=o(1).
\end{gathered}
 \tag{23}
\]

The far input requires a separate estimate. Decompose it into annuli
\(r_j<|(s,y)|\le2r_j\), with \(r_j=4R\,2^j\). For a nonzero kernel output, \(|(s,z)|\le2R\), whereas the input cutoff is zero. Also \(|s|\le2R\), so
\[
 |z-y|\ge c r_j
 \tag{24}
\]

for a fixed \(c>0\). For example,
\(|y|\ge(r_j^2-4R^2)^{1/2}\ge\sqrt3\,r_j/2\) and
\(|z|\le2R\le r_j/2\).

For each fixed \(s\), both integrals in (8), restricted to these input and output sets, are at most \(C_Nr_j^{d-N}\). For the input integral, its volume is at most \(Cr_j^d\); for the output integral, it is at most \(CR^d\le Cr_j^d\). Equation (24) bounds the kernel by \(C_Nr_j^{-N}\). The \(j\)-th far term is consequently bounded in the slice \(L^1\) norm by

\[
 \begin{aligned}
 &C R^{1/2}r_j^{d-N}
 \|v1_{\{r_j<|x|\le2r_j\}}\|_2
 \\
 &\le C R^{1/2}r_j^{d+1/2-N}\|v\|_{B^*}.
 \end{aligned}
 \tag{25}
\]

Here (2) bounds the annular \(L^2\) norm by \(C r_j^{1/2}\|v\|_{B^*}\). Choose \(N=d+2\) and sum the geometric series. Its total is at most \(CR^{-1}\|v\|_{B^*}\). This also proves convergence of the kernel action on the far input. In dimension zero the commutator is identically zero. We have proved, in every dimension,

\[
 \|e_R\|_{L^1((-\infty,T);\mathcal H)}\longrightarrow0.
 \tag{26}
\]

Now \(v_R\) is globally \(L^2\) and has compact support. Equation (19) implies
\(\partial_sv_R=iAv_R+i(\chi_Rg+e_R)\) in local \(L^1(\mathbb R;\mathcal H)\). It therefore has a locally absolutely continuous representative, as follows directly. Subtract the vector primitive of the right side constructed in Section 3, leaving a locally integrable vector distribution \(F\) with \(F'=0\). Choose \(\rho\in C_c^\infty(\mathbb R)\), \(\int\rho=1\), and set \(h=\int\rho(s)F(s)\,ds\in\mathcal H\). Every compact smooth test \(\varphi\) has
\(\psi=\varphi-(\int\varphi)\rho\) of integral zero, so \(\Psi(s)=\int_{-\infty}^s\psi(t)\,dt\) is compact and smooth. The identity \(F'=0\) gives \(\int F\psi=0\), hence \(\int F\varphi=h\int\varphi\). Thus \(F=h\) as a vector distribution and almost everywhere. For the last conclusion pair with a countable dense subset of \(\mathcal H\); scalar convolution with compact smooth approximate identities and their local \(L^1\) convergence, proved in [Approximation and convolution](../providers/analysis/euclidean-approximation-and-convolution.md#mollification), identifies each scalar function almost everywhere. The common null set and density identify the vector. Adding the primitive back gives the claimed representative.

This representative is zero for \(s<-2R\), since it is continuous and agrees there almost everywhere with zero. Variation of constants is valid for this rough forcing as well: multiplying the integral equation by \(U(a,s)\), or approximating its \(L^1\) right side by simple functions, gives the formula in Section 3. Uniqueness follows by iterating the homogeneous norm inequality, with bound \(M^k|s-a|^k/k!\) at its \(k\)-th iteration. Thus (15) implies, for \(s\le T\),

\[
 \|v_R(s)\|\le C_0q(s)+
 C_0\|e_R\|_{L^1((-\infty,T);\mathcal H)}.
 \tag{27}
\]

Take \(R\) and the upper bound \(T\) through the positive integers. Outside one common null set, \(v_R(s,z)=\chi_R(s,z)v(s,z)\). Fatou's lemma in \(z\), followed by (26), proves \(\|v(s)\|_{\mathcal H}\le C_0q(s)\) for almost every \(s\). The slices now belong to \(\mathcal H\) and are uniformly bounded. Equation (10) gives a locally absolutely continuous representative, and continuity extends the inequality to every \(s\).

For \(g=0\) this inequality forces \(v=0\). The difference of two \(B^*\) solutions satisfying (3) again satisfies (3), by the squared triangle inequality. Thus uniqueness follows. Solutions obeying (11) satisfy (3) by (17), so the existence statement is unique in its asserted class as well. This completes Theorem 3.1. \(\square\)

## 5. Moving a regular energy graph

Let \(P(\xi)\) be a real elliptic polynomial of degree \(m\). Fix an energy \(\lambda\) and a regular graph patch

\[
 \begin{gathered}
\xi=(\xi_1,\eta),\\ \qquad
 P(E(\eta),\eta)=\lambda,\\ \qquad
 \partial_{\xi_1}P>0.
\end{gathered}
 \tag{28}
\]

Work on a compact set of \(\eta\) contained in an open graph patch. Shrink a collar around the graph so that the positive derivative has a fixed lower bound there. Let \(L(x,\xi)\) be a real polynomial in \(\xi\), of total degree at most \(m\), with smooth coefficients \(\ell_\gamma(x)\).

Fix \(0<\delta<1/3\), put \(X=(1+|x|^2)^{1/2}\), and define the continuous concave function

\[
 \mu(t)=
 \begin{cases}
 \delta+t,&0\le t\le2,\\
 1+(1+\delta)t/2,&t\ge2.
 \end{cases}
 \tag{29}
\]

Assume the full bounds
\[
 |\partial_x^\beta\ell_\gamma(x)|
 \le C_{\gamma,\beta}X^{-\mu(|\beta|)}
 \tag{30}
\]

for every \(\beta\). Suppose also that \(L=0\) on \(|x|<R_0\), where \(R_0\) may be chosen large with the constants in (30) fixed.

**Theorem 5.1.** For \(R_0\) sufficiently large, there is a unique root \(\xi_1=a(x,\eta)\) near \(E(\eta)\) of \(P(\xi)+L(x,\xi)=\lambda\). It is smooth on a neighborhood of the compact patch and satisfies, for every \(\alpha,\beta\),

\[
 |\partial_\eta^\alpha\partial_x^\beta
       (a(x,\eta)-E(\eta))|
 \le C_{\alpha,\beta}X^{-\mu(|\beta|)}.
 \tag{31}
\]

**Proof.** Write \(\xi_1=E(\eta)+h\). On a fixed small collar,
\[
 \begin{gathered}
 P(E(\eta)+h,\eta)-\lambda=h\,J(h,\eta),\\
 J(h,\eta)=\int_0^1
 \partial_{\xi_1}P(E(\eta)+th,\eta)\,dt.
 \end{gathered}
 \tag{32}
\]

The function \(J\) has a positive lower bound and bounded derivatives. The root equation becomes
\[
 \begin{gathered}
h=F(x,h,\eta),\\ \qquad
 F(x,h,\eta)=-\frac{L(x,E(\eta)+h,\eta)}{J(h,\eta)}.
\end{gathered}
 \tag{33}
\]

All mixed derivatives of \(F\), with physical order \(|\beta|\), are bounded by \(C X^{-\mu(|\beta|)}\). Frequency variables are in a fixed compact collar. Since \(L\) vanishes on the ball and \(\mu(0)=\delta>0\), increasing \(R_0\) makes \(F\) map a fixed small closed \(h\) interval into itself and makes \(|F_h|\le1/2\), uniformly in \(x,\eta\). Iteration is a contraction and produces the unique small root.

Here is smooth dependence before differentiating that root. Put \(p=(x,\eta)\). On every compact parameter neighborhood, subtracting two fixed-point equations gives \(|h(p+q)-h(p)|\le2C|q|\). Taylor's segment formula then yields
\[
 \begin{gathered}
 \Delta h=h(p+q)-h(p),\\
 j_p=1-F_h(p,h(p)),\\
 j_p\Delta h=D_pF(p,h(p))q+o(|q|).
 \end{gathered}
\]
The coefficient has absolute value at least \(1/2\), so this proves differentiability and the continuous derivative formula \(D_ph=(1-F_h)^{-1}D_pF\). Inductively differentiating that formula proves smoothness at every finite order. Uniqueness of the small root makes these local constructions agree.

For the derivative estimates, concavity gives, whenever \(b_0,\ldots,b_q\ge0\),
\[
 \sum_{j=0}^q\mu(b_j)
 \ge \mu\!\left(\sum_{j=0}^q b_j\right)+q\delta.
 \tag{34}
\]

To see this, fix their sum \(B>0\). A point in the simplex is the convex combination, with weights \(b_j/B\), of its vertices. Concavity of the sum bounds its value below by the common vertex value \(\mu(B)+q\mu(0)\). For \(B=0\) the inequality is equality.

At order zero, (33) gives (31). Induct in total mixed derivative order. Differentiating the identity produces the term \(F_h\partial_\eta^\alpha\partial_x^\beta h\), which we move to the left. Every remaining finite chain term is either a derivative of \(F\) alone, or a derivative of \(F\) multiplied by \(q\ge1\) lower-order derivatives of \(h\). Their physical orders \(b_0,\ldots,b_q\) sum to \(|\beta|\). The induction hypothesis and (34) bound the term by \(C X^{-\mu(|\beta|)}\), with additional decay when \(q>0\). Division by \(1-F_h\), whose absolute value is at least \(1/2\), proves (31) at the next order. This includes all frequency derivatives. \(\square\)

## 6. Dividing the polynomial without losing decay

Ellipticity implies that the homogeneous degree-\(m\) part of \(P\), evaluated at the first coordinate vector, is nonzero. Thus \(P\) has degree \(m\) in \(\xi_1\), with a nonzero constant leading coefficient. For \(R_0\) large the corresponding coefficient of \(L\) is uniformly small. Polynomial division therefore gives

\[
 \begin{aligned}
 P(\xi)-\lambda&=(\xi_1-E(\eta))Q_0(\xi),\\
 P(\xi)+L(x,\xi)-\lambda&=
       (\xi_1-a(x,\eta))Q(x,\xi).
 \end{aligned}
 \tag{35}
\]

Both quotients have degree \(m-1\) in \(\xi_1\). On the chosen collar \(Q_0=J(\xi_1-E(\eta),\eta)\), so it is bounded away from zero.

**Proposition 6.1.** On every fixed compact collar as above, every mixed derivative satisfies

\[
 \begin{aligned}
 |\partial_\xi^\alpha\partial_x^\beta(Q-Q_0)|
 &\le C_{\alpha,\beta}X^{-\mu(|\beta|)},\\
 |\partial_\xi^\alpha\partial_x^\beta
       (Q^{-1}-Q_0^{-1})|
 &\le C'_{\alpha,\beta}X^{-\mu(|\beta|)}.
 \end{aligned}
 \tag{36}
\]

The second assertion holds after increasing \(R_0\) if necessary.

**Proof.** Subtract the first factorization in (35), using the second root:

\[
 \begin{aligned}
 L+Q_0(a-E)&=\sum_{j=0}^m r_j(x,\eta)\xi_1^j,\\
 Q-Q_0&=\sum_{j=0}^{m-1}q_j(x,\eta)\xi_1^j.
 \end{aligned}
 \tag{37}
\]

Every derivative of each \(r_j\), with physical order \(|\beta|\), has the first bound in (36), by (30), (31) and the product rule. Coefficient comparison gives

\[
 \begin{gathered}
q_{m-1}=r_m,\\ \qquad
 q_{j-1}=r_j+a q_j\quad(1\le j<m).
\end{gathered}
 \tag{38}
\]

Induct downward in \(j\). Multiplication by \(E(\eta)\) costs no physical decay. For multiplication by \(a-E\), every product-rule term has two physical orders whose sum is \(|\beta|\). Equations (31) and (34) give at least the required exponent, with an extra \(\delta\). This proves all coefficient estimates. The polynomial's powers of \(\xi_1\) and their derivatives are bounded on the fixed collar, giving the first line of (36).

The zeroth estimate and the large zero region give
\(|Q-Q_0|\le |Q_0|/2\). Hence \(Q\) is uniformly bounded away from zero. Set \(f=Q^{-1}-Q_0^{-1}\). Its zeroth bound follows directly, and
\[
 Qf=(Q_0-Q)Q_0^{-1}.
 \tag{39}
\]

The right side has every required mixed bound. Induct on total derivative order in (39), isolating \(Q\partial_\xi^\alpha\partial_x^\beta f\). A differentiated \(Q_0\) has only frequency derivatives and a fixed bound. A differentiated \(Q-Q_0\), multiplied by a lower derivative of \(f\), is controlled by (34). The induction hypothesis thus bounds every other term by \(C X^{-\mu(|\beta|)}\). Divide by the uniformly nonzero \(Q\). This proves the second line. \(\square\)

These are exact polynomial identities. In left quantization, a product of operators can also contain terms with frequency and physical derivatives of their symbols. Equation (35) alone does not identify the forcing of a first-order equation obtained from a differential equation.

## 7. Applying the outgoing theorem to the energy root

Choose real \(\psi\in C_c^\infty\) of the \(\eta\) patch, equal to one on a smaller patch, and define
\[
 b(s,z,\eta)=\psi(\eta)a((s,z),\eta).
 \tag{40}
\]

Extend it by zero outside the patch. Smoothness follows because the cutoff is supported strictly inside the domain of \(a\). Theorem 5.1 gives uniform bounds for every \(\eta\) derivative. Physical derivatives of the free part \(\psi E\) vanish. Since \(\mu(1)=1+\delta\),
\[
 \begin{aligned}
 |\partial_\eta^\alpha\nabla_z b|
   +|\partial_\eta^\alpha\partial_s b|
 &\le C_\alpha(1+|s|)^{-1-\delta}.
 \end{aligned}
 \tag{41}
\]

The right side is integrable. The kernel proof gives operator-norm continuity in \(s\) from the same bound on its derivative. All hypotheses of Theorem 3.1 hold. Therefore, if \(v\in B^*\), \(g\in B\),
\[
 (D_s-b(s,z,D_z))v=g,
 \tag{42}
\]

and \(v\) satisfies (3), then
\[
 \|v(s)\|_{L^2_z}
 \le C\int_{-\infty}^s\|g(t)\|_{L^2_z}\,dt.
 \tag{43}
\]

The theorem also constructs its unique outgoing solution for every \(g\in L^1(\mathbb R;L^2_z)\). Once a frequency-localized differential equation has been reduced to (42), this result supplies its slice estimate and uniqueness. Construction of the long-range outgoing amplitude requires further control of the oscillating energy graph.

### Use the conclusion

Follow the outgoing kernel estimate to the slice recovery, then check the perturbed energy root and its reciprocal derivatives. The graph factorization and the outgoing uniqueness principle perform different jobs.

## 8. Exercises with complete solutions

**Exercise 1 — Foundation: a wave may leave a permanent outgoing amplitude.** Take \(A(s)=0\), \(g(s,z)=\rho(s)h(z)\), where \(\rho\in C_c^\infty((-1,1))\), \(h\in C_c^\infty(\mathbb R^d)\), and \(c=\int\rho\). Find the outgoing solution. Prove (3) and compute its total ball-mass limit divided by \(R\). Explain why adding a nonzero constant-in-\(s\) vector destroys the outgoing condition.

**Solution 1.** The formula is \(v(s,z)=i h(z)\int_{-\infty}^s\rho(t)\,dt\). It is zero for \(s<-1\) and equals \(ic h(z)\) for \(s>1\). For fixed \(T\), only a bounded \(s\) interval contributes to (3), with a bounded slice norm; its quotient tends to zero. The strip \(|s|\le1\) likewise contributes \(O(1/R)\) to the total quotient. The part \(s>1\) gives
\[
 \begin{aligned}
&|c|^2\int_{|z|<R}
 \left(\sqrt{1-|z|^2/R^2}-R^{-1}\right)_+
 \\ &\quad|h(z)|^2\,dz\\ &\longrightarrow |c|^2\|h\|_2^2.
\end{aligned}
 \tag{44}
\]

Dominated convergence proves the limit. If \(c h\ne0\), the solution consequently does not have vanishing total shell mass. Adding \(k(z)\ne0\) gives the homogeneous solution \(k\) on \(s<-1\). For any fixed \(T\), its backward ball quotient has limit \(\|k\|_2^2\): the length of the interval from \(-\sqrt{R^2-|z|^2}\) to \(\min(T,-1)\), divided by \(R\), tends to one, and is uniformly bounded for large \(R\). Dominated convergence gives the stated positive limit. In dimension zero the same computations use \(|h|^2\) and \(|k|^2\).

**Exercise 2 — Intermediate: the sharp derivative budget.** Let \(\delta=1/5\) in (29). Find the least possible value of \(\mu(b_0)+\mu(b_1)+\mu(b_2)\) for nonnegative \(b_j\) summing to \(3\). Compare it with the value for \((1,1,1)\). Explain how this estimate controls a chain term with two differentiated inner roots.

**Solution 2.** Equation (34) gives the lower bound
\(\mu(3)+2\delta=14/5+2/5=16/5\). The vertex \((3,0,0)\) attains it, so it is the minimum. For \((1,1,1)\) the value is \(3(6/5)=18/5\). A chain term with one outer derivative and two inner root derivatives has physical orders \(b_0,b_1,b_2\); its decay is at least \(X^{-16/5}\). The target for physical order three is \(X^{-14/5}\), so even the least favorable distribution has the extra factor \(X^{-2/5}\). Zero physical order does not mean zero derivative: a factor with frequency derivatives only still supplies the exponent \(\mu(0)=1/5\).

**Exercise 3 — Intermediate: an anisotropic quadratic shell.** Take \(P(\xi_1,\eta)=\xi_1^2+2\eta^2\), \(\lambda=1\), \(|\eta|\le1/4\), and \(L(x,\xi)=\ell(x)\), where \(\ell\) is real, satisfies (30), vanishes on a sufficiently large ball and has \(|\ell|\le1/8\). Compute \(E,a,Q_0,Q\), and the two differences in (31) and (36). Identify a collar where the denominators are bounded away from zero.

**Solution 3.** Put \(E=(1-2\eta^2)^{1/2}\) and choose the positive perturbed root \(a=(1-2\eta^2-\ell)^{1/2}\). Then \(E\ge\sqrt{7/8}\) and \(a\ge\sqrt{3/4}\). Exact division gives
\[
 \begin{gathered}
 a-E=-\frac{\ell}{a+E},\\ \qquad
 Q_0=\xi_1+E,\\ \qquad Q=\xi_1+a,\\
 Q-Q_0=a-E,\\ \qquad
 Q^{-1}-Q_0^{-1}
   =-\frac{a-E}{(\xi_1+a)(\xi_1+E)}.
 \end{gathered}
 \tag{45}
\]

On \(|\xi_1-E|<1/4\), \(\xi_1>1/2\), so both quotient denominators have a fixed positive lower bound. Theorem 5.1 and Proposition 6.1 apply directly. Alternatively, differentiate the first formula in (45): the square-root arguments stay in a fixed positive interval, and every physical chain term contains derivatives of \(\ell\). Equation (34) bounds their products by the required \(X^{-\mu(|\beta|)}\). Frequency derivatives have fixed bounded factors on the patch. The remaining formulas give the same estimates by the product and reciprocal rules.

**Exercise 4 — Advanced: why reality is not operator symmetry.** In one transverse dimension take
\(b(s,z,\eta)=q(s)a_0(z)\psi(\eta)\), with real smooth compactly supported \(a_0,\psi\), and \(q(s)=(1+s^2)^{-(1+\delta)/2}\). Show that the adjoint defect has integrable norm. Give choices for which it is nonzero. Derive the \(C/R\) bound on its commutator with \(\chi_R\).

**Solution 4.** If \(k(w)=(2\pi)^{-1}\int e^{iw\eta}\psi(\eta)\,d\eta\), the kernel is \(q(s)a_0(z)k(z-y)\). Reality of \(\psi\) gives \(\overline{k(-w)}=k(w)\), so the adjoint-difference kernel is
\[
 q(s)\bigl(a_0(z)-a_0(y)\bigr)k(z-y).
 \tag{46}
\]

Since \(a_0\) is Lipschitz and \(k\) is rapidly decreasing, (8) bounds the norm by \(C|q(s)|\). Its integral is finite because \(q(s)=O(|s|^{-1-\delta})\). For a concrete nonzero defect, choose a nonnegative, even, nonzero \(\psi\); then \(k(0)>0\) and \(k\) is nonzero near zero. Choose \(a_0\) with \(a_0'(z_0)\ne0\). Nearby distinct \(z,y\) give a nonzero continuous kernel in (46), so the operator is nonzero: tests supported in sufficiently small neighborhoods of these points give a nonzero pairing. Finally the commutator kernel is \(q(s)a_0(z)k(z-y)(\chi_R(s,y)-\chi_R(s,z))\). The difference is bounded by \(C|z-y|/R\). Both absolute kernel integrals are bounded by \(C/R\), uniformly in \(s\), and (8) gives that operator norm.

**Exercise 5 — Advanced: the larger forcing class is necessary.** Choose \(h\in C_c^\infty(\mathbb R^d)\), supported in \(|z|<1\), with \(\|h\|_2=1\), and set
\[
 \begin{aligned}
 \rho(s)&=\sum_{j\ge1}\frac{2^{-j}}j
       1_{[3\cdot4^j,\ 3\cdot4^j+1]}(s),\\
 g(s,z)&=\rho(s)h(z).
 \end{aligned}
 \tag{47}
\]

Show that \(g\in L^1(\mathbb R;L^2_z)\) but \(g\notin B\). For \(A=0\), verify the outgoing solution's existence, bounded slice norm and condition (3). In dimension zero use \(h=1\).

**Solution 5.** The slice integral is \(\sum_{j\ge1}2^{-j}/j<\infty\). Each pulse is wholly inside the shell with outer radius \(2^{2j+2}=4\cdot4^j\) and inner radius \(2\cdot4^j\); the fixed transverse support and interval of length one preserve both strict inequalities. Distinct pulses occupy distinct shells. That shell's \(L^2\) norm is \(2^{-j}/j\), so its contribution to the \(B\) norm is
\(2^{j+1}(2^{-j}/j)=2/j\). The sum diverges.

Nevertheless \(v(s,z)=i h(z)\int_{-\infty}^s\rho(t)\,dt\) is continuous, locally absolutely continuous, and solves \(D_sv=g\). Its slice norm is at most \(\sum_j2^{-j}/j\), so (4) puts it in \(B^*\). For each fixed \(T\), its nonzero slices with \(s<T\) occupy a bounded interval starting at \(s=12\). Their total squared mass is finite, independently of \(R\), and hence (3) holds. The uniqueness theorem applies to this forcing even though its \(B\) norm is infinite.

## References

- [T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, free author's online second edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), 2014, Theorem 5.1, pp. 145–146. This supplies the self-adjoint evolution comparison; the possibly nonsymmetric, time-dependent evolution and rough forcing used here are proved in Sections 2–4.
- [ODE] Gerald Teschl, [*Ordinary Differential Equations and Dynamical Systems*, free author's preliminary edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), April 2012, §2.2. Its integral iteration is the initial-value comparison. Section 3 writes the operator-norm series, both time directions and the integrable adjoint-defect bound explicitly.
- [Y] Dmitri Yafaev, [*Lectures on scattering theory*, free author preprint, arXiv:math/0403213v1](https://arxiv.org/pdf/math/0403213v1), 12 March 2004; lecture notes prepared by Andrew Hassell. Section 1 introduces the scattering context. The endpoint outgoing condition, slice recovery and polynomial factor estimates in this lesson have their written proofs above.

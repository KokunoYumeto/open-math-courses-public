# The smooth Dirichlet domain and its compact inverse

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This proves the exact bounded-region prerequisite used in AN06-U001. Let $n\geq1$ and let $\Omega\subset\mathbb R^n$ be a bounded open set with smooth boundary. Connectedness is unnecessary. The empty set gives the zero Hilbert space and all statements below trivially. No arbitrary rough boundary, higher-order boundary condition, or higher-order regularity theorem is asserted.

For related results, see John K. Hunter, [*Notes on Partial Differential Equations*, revised 18 June 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf): Theorem 4.27, printed pp.112-113; boundary change of variables and Theorem 4.30, pp.114-116; and Proposition 4.52/Theorem 4.53, pp.124-126. The proof below supplies its own difference-quotient signs, admissible tests, compactness, energy inverse and domain identification. The higher-regularity statements following Hunter's boundary proof are not imported.

We use weak derivatives, Lebesgue integration and the unitary Fourier transform. Write $H^k(\Omega)$ for the functions whose weak derivatives of order at most $k$ are in $L^2$, and define $H_0^1(\Omega)$ to be the $H^1$-closure of $C_c^\infty(\Omega)$. Inner products are linear in the first variable.

Read [Euclidean product measure](finite-derivative-l2.md#euclidean-products), [coordinate inverses and measurable change of variables](coordinate-inverses-and-integration.md), and then [Fourier normalization](finite-derivative-l2.md#fourier-normalization), in that order. The [approximation and convolution reading](euclidean-approximation-and-convolution.md) proves the translation, mollification and integer Sobolev approximation facts used below. The energy representation is proved explicitly in Section 2.

<a id="dirichlet-compact-embedding"></a>
## 1. The zero-boundary energy space and compact embedding

**Lemma 1.1.** For some $C_P<\infty$,
\[
 \|u\|_2\leq C_P\|\nabla u\|_2\qquad(u\in H_0^1(\Omega)).
 \tag{1}
\]
Zero extension $Eu$ belongs to $H^1(\mathbb R^n)$, with derivative equal to the zero extension of each derivative of $u$. The inclusion $H_0^1(\Omega)\longrightarrow L^2(\Omega)$ is compact.

**Proof.** Choose a cube $Q=(-R,R)^n$ containing $\overline\Omega$ in its interior. For $u\in C_c^\infty(\Omega)$, its zero extension is smooth and, on every line parallel to the first coordinate,
\[
 Eu(x_1,x')=\int_{-R}^{x_1}\partial_1Eu(t,x')\,dt.
\]
Cauchy-Schwarz, integration over $Q$ and Fubini give (1) with $C_P=2R$. For an $H^1$-convergent sequence of such functions, their zero extensions and derivatives converge in $L^2(\mathbb R^n)$. Testing against a compactly supported smooth function identifies the derivative of the limit, proving the assertion about $E$ and extending (1). This also proves the needed completeness of the energy space: $H^1$ is complete because an $L^2$ limit of functions and their first derivatives still satisfies the weak-derivative identities, and $H_0^1$ is a closed subspace. By (1), $\|\nabla u\|_2$ is an equivalent complete norm on it.

For compactness, let $P_N$ be the whole-space Fourier multiplier $1_{\{|\xi|\leq N\}}$. Plancherel gives
\[
 \|(I-P_N)Eu\|_2\leq N^{-1}\|\nabla Eu\|_2.
 \tag{2}
\]
For each fixed $N$, the operator $P_N$ on functions supported in $Q$ is compact as a map $L^2(Q)\to L^2(\mathbb R^n)$. Indeed its kernel is $c_n k_N(x-y)1_Q(y)$, where $k_N=\mathcal F^{-1}1_{\{|\xi|\leq N\}}\in L^2$ and $c_n=(2\pi)^{-n/2}$. Its squared integral is $c_n^2|Q|\|k_N\|_2^2$, by translation invariance and nonnegative Fubini.

Here are the kernel details. Every $L^2$ function on a Euclidean product is approximated by finite-measure simple functions, and then by finite sums of rectangle indicators, using the [proved rectangle approximation](finite-derivative-l2.md#euclidean-products). A rectangle in $\mathbb R^n\times\mathbb R^n$ is the product of two rectangles; intersecting its second factor with $Q$ keeps it a product. Thus finite sums $\sum_{j=1}^m a_j(x)b_j(y)$, with both factors in their respective $L^2$ spaces, are dense in $L^2(\mathbb R^n\times Q)$. A square-integrable kernel $G$ defines a bounded operator: pointwise Cauchy–Schwarz in $y$, followed by Fubini in $x$, gives $\|T_Gv\|_2\leq\|G\|_2\|v\|_2$. The same bound applies to kernel differences. The approximating product kernels have range in the finite span of the $a_j$, so their operators have finite rank. Bounded subsets of such a finite-dimensional range have compact closure by the [finite-dimensional compactness proof](compact-fredholm-families.md#fredholm-finite-tools).

To verify the displayed kernel represents the Fourier cutoff, choose $m_j\in C_c^\infty(\mathbb R^n)$ tending to $1_{\{|\xi|\leq N\}}$ in $L^2$, and set $k_j=\mathcal F^{-1}m_j$. For $v\in C_c^\infty(Q)$, the Fourier formula and absolute Fubini give $c_n k_j*v=\mathcal F^{-1}(m_j\mathcal Fv)$. The left side converges in $L^2$ to the stated kernel operator by the preceding kernel bound and $k_j\to k_N$ in $L^2$. The right side converges to $P_Nv$, since $\mathcal Fv$ is bounded and Plancherel applies. For $v\in L^2(Q)$, extend by zero, truncate to the points whose distance from the complement of $Q$ exceeds $1/j$, and then mollify with radius less than $1/(2j)$. Dominated convergence gives the truncation limit. The [mollification theorem](euclidean-approximation-and-convolution.md#mollification) permits each radius to be chosen still smaller so that its $L^2$ error tends to zero; the convolutions belong to $C_c^\infty(Q)$. This proves the required density and extends the kernel identity to all of $L^2(Q)$.

Consequently $P_N$ on functions supported in $Q$ is a norm limit of finite-rank operators. Equation (2) shows that $E:H_0^1\to L^2(\mathbb R^n)$ is a norm limit of compact operators. Such a limit is compact: a finite net for the image of a unit ball under an approximant is a slightly enlarged net for its image under the limit. Total boundedness in the complete target gives compact closure, as proved in the same finite-dimensional-tools reading. Restriction to $\Omega$ proves the claimed inclusion compact. $\square$

<a id="dirichlet-energy-inverse"></a>
## 2. The energy inverse

Put $a(u,v)=\int_\Omega\nabla u\cdot\overline{\nabla v}$. For $f\in L^2(\Omega)$ there is a unique $u\in H_0^1(\Omega)$ satisfying
\[
 a(u,v)=(f,v)\qquad(v\in H_0^1(\Omega)).
 \tag{3}
\]
Here is the Hilbert representation step explicitly. A continuous conjugate-linear functional $F$ on a Hilbert space has closed kernel. Projection onto that kernel exists: a minimizing sequence for distance is Cauchy by the parallelogram identity and converges by completeness; variation along the kernel shows its remainder is orthogonal. If $F\ne0$, choose a unit vector $e$ in the orthogonal complement of its kernel. Every vector is a kernel vector plus $ce$, since subtracting the multiple chosen by its $F$-value puts it in the kernel. Hence $F(v)=(F(e)e,v)$. The zero functional is represented by zero. Apply this argument to the complete energy inner product $a$ and $F(v)=(f,v)$, bounded by $C_P\|f\|_2\|\nabla v\|_2$.

Define $Kf=u$. Uniqueness makes $K$ linear, and testing (3) with $u$ gives
\[
 \|\nabla Kf\|_2\leq C_P\|f\|_2,\qquad
 \|Kf\|_2\leq C_P^2\|f\|_2.
 \tag{4}
\]
Thus $K:L^2\to H_0^1$ is bounded and, by Lemma 1.1, $K:L^2\to L^2$ is compact. Furthermore
\[
 (f,Kg)=a(Kf,Kg)=(Kf,g),\qquad
 (Kf,f)=\|\nabla Kf\|_2^2\geq0.
 \tag{5}
\]
Consequently $K$ is self-adjoint and positive. If $Kf=0$, (3) gives $(f,v)=0$ for all $v\in C_c^\infty(\Omega)$, so $f=0$ by their $L^2$ density. The density follows by first truncating away from the complement of $\Omega$ and then mollifying; dominated convergence and continuity of translations in $L^2$ give the two approximations. Thus $K$ is injective and has dense range: a vector orthogonal to its range is killed by $K^*=K$.

<a id="dirichlet-boundary-h2"></a>
## 3. The full second-order boundary estimate

**Theorem 3.1.** If $u\in H_0^1(\Omega)$ and $-\Delta u=f\in L^2(\Omega)$ in distributions, then
\[
 u\in H^2(\Omega),\qquad
 \|u\|_{H^2(\Omega)}\leq C_\Omega(\|f\|_2+\|u\|_2).
 \tag{6}
\]

**Proof.** The distribution equation extends to (3) by $H^1$ approximation of tests. In particular
\[
 \|\nabla u\|_2^2=(f,u)\leq\|f\|_2\|u\|_2,
 \qquad \|u\|_{H^1}\leq C(\|f\|_2+\|u\|_2).
 \tag{7}
\]

<a id="dirichlet-difference-quotients"></a>

We first give the two difference-quotient facts used below. Set $\delta_h^k q(y)=(q(y+he_k)-q(y))/h$. Translations commute with weak derivatives: substitute $y'=y+he_k$ in the integral against a compact smooth test, use the original weak-derivative identity with the oppositely translated test, and substitute back. Taking the difference and dividing by $h$ gives $\partial_i\delta_h^kq=\delta_h^k\partial_iq$ wherever those derivatives are defined. Where supports and shifts fit in a larger coordinate patch, change of variable gives
\[
 \int q\,\overline{\delta_{-h}^k r}
 =-\int\delta_h^kq\,\overline r,
 \qquad
 \delta_h^k(bq)=b(y+he_k)\delta_h^kq+(\delta_h^kb)q.
 \tag{8}
\]
For $q\in H^1$, the fundamental theorem of calculus along lines, followed by Cauchy-Schwarz and Fubini, gives
\[
 \|\delta_h^kq\|_{L^2(U)}\leq\|\partial_kq\|_{L^2(U_h)},
 \tag{9}
\]
where $U_h$ contains all intervening segments. This identity first holds for smooth functions and then for the $H^1$ limits used here. Conversely, if the difference quotients of an $L^2$ function are bounded by $M$ on $U$ for all sufficiently small $h$, then it has weak $k$th derivative there of norm at most $M$. For $\phi\in C_c^\infty(U)$, (8) yields
\[
 \left|\int q\,\overline{\partial_k\phi}\right|
 =\lim_{h\to0}\left|\int\delta_h^kq\,\overline\phi\right|
 \leq M\|\phi\|_2.
\]
The Hilbert representation argument in Section 2 represents the functional $\phi\mapsto-\int q\,\overline{\partial_k\phi}$ by an $L^2$ function. That is exactly the weak derivative, including its sign. No assertion of differentiability is made before this argument.

<a id="dirichlet-boundary-localization"></a>

Near a boundary point, write the smooth boundary as a graph after rotating coordinates, and use the graph map to flatten it. On nested, relatively compact coordinate patches it is a smooth diffeomorphism $x=\psi(y)$ with $y_n>0$ inside $\Omega$, bounded derivatives and bounded inverse derivatives. Let $w=u\circ\psi$, $J=|\det D\psi|$, and $B=D\psi^{-1}$, evaluated at $x=\psi(y)$. Changing variables in the weak formulation gives
\[
 \int A_{ij}\partial_iw\,\overline{\partial_jv}
 =\int F\overline v,\qquad
 A=JBB^T,\quad F=J(f\circ\psi).
 \tag{10}
\]
Repeated indices are summed here. The matrix is real symmetric, its entries and first derivatives are bounded, and $\xi^TA(y)\xi\geq\theta|\xi|^2$ for a common $\theta>0$ on the chosen patch. These statements follow from the determinant being bounded above and below and the inverse matrix being bounded. All Sobolev change-of-variable identities in (10) follow by taking $u_j\in C_c^\infty(\Omega)$ converging to $u$ in $H^1$, using the ordinary chain rule for $u_j$, and passing to the limit. Test functions supported away from the patch's artificial edges and belonging to the zero-boundary energy space pull back to admissible tests in (3).

Choose $\eta$ smooth with $0\leq\eta\leq1$, equal to one on the smaller patch and supported away from its artificial edges. It may meet $y_n=0$. For each tangential index $k<n$ and small $h$, use
\[
 v=-\delta_{-h}^k(\eta^2\delta_h^kw)
 \tag{11}
\]
in (10). This is an admissible $H_0^1$ test. To justify it without importing a trace theorem, multiply the transformed $u_j$ by a cutoff equal to one around all supports in (11). They are compactly supported smooth functions in the half-space and converge in $H^1$. Tangential translations preserve the half-space; for fixed $h$, differences and multiplication by $\eta$ are bounded operations on $H^1$. Their corresponding tests therefore converge to (11) in $H^1$. No normal translation across the boundary is used. At an interior patch the same test is admissible for every $k$ by choosing its support a positive distance from the patch boundary.

For clarity, put $X_h=\|\eta\delta_h^k\nabla w\|_2$ and $W=\|w\|_{H^1}$ on a fixed larger patch. Substituting (11), using (8), and expanding the derivative of $\eta^2\delta_h^kw$ leaves the principal term
\[
 \int\eta^2 A_{ij}(y+he_k)
       \delta_h^k\partial_iw\,
       \overline{\delta_h^k\partial_jw}
 \geq\theta X_h^2.
\]
The remaining terms contain either $\delta_h^kA_{ij}\,\partial_iw$ or $2\eta\partial_j\eta\,\delta_h^kw$. The coefficient differences are uniformly bounded by their first derivatives, and (9) bounds $\|\delta_h^kw\|_2$ by $W$ on the larger patch. Cauchy-Schwarz therefore bounds these terms by $C(WX_h+W^2)$. The right side of (10) is bounded by
\[
 \|F\|_2\|\delta_{-h}^k(\eta^2\delta_h^kw)\|_2
 \leq C\|F\|_2(X_h+W).
\]
For the last inequality apply (9) to $\eta^2\delta_h^kw$ and expand its $k$th derivative; its derivative term is bounded by $X_h$ because $0\leq\eta\leq1$. Hence
\[
 \theta X_h^2\leq C(W+\|F\|_2)X_h
                       +C(W^2+\|F\|_2W).
\]
The inequality $ab\leq\varepsilon a^2+(4\varepsilon)^{-1}b^2$, with fixed small $\varepsilon$, absorbs the terms linear in $X_h$ and proves
\[
 X_h\leq C(W+\|F\|_2),
 \tag{12}
\]
uniformly in $h$. The converse to (9), applied to every $\partial_iw$ where $\eta=1$, now gives $\partial_k\partial_iw\in L^2$. In the interior all second derivatives are obtained this way. At the boundary it gives every second derivative except $\partial_n^2w$; commutation of distribution derivatives includes those with the tangential derivative written second.

Equation (10) implies, in distributions on the smaller half-patch,
\[
 A_{nn}\partial_n^2w
 =-F-\sum_{(i,j)\ne(n,n)}A_{ij}\partial_j\partial_iw
     -\sum_{i,j}(\partial_jA_{ij})\partial_iw.
 \tag{13}
\]
The right side is in $L^2$ by (12). Since $A_{nn}\geq\theta$, multiplication by $1/A_{nn}$ identifies the remaining distribution derivative with an $L^2$ function of the same controlled norm. When $n=1$ the first sum in (13) is empty and this step gives the entire second-derivative conclusion directly.

To transform back explicitly, put $\phi=\psi^{-1}$ and $c_{ir}=\partial_{x_i}\phi_r$. On each compact subpatch in the interior of the half-patch, mollification approximates $w$ in $H^2$: derivatives commute with convolution there, and continuity of translations in $L^2$ proves convergence of each derivative. The ordinary chain rule for these smooth approximants, followed by change of variables and passage in $L^2$, gives
\[
 \partial_{x_j}\partial_{x_i}u
 =\sum_{r,s}c_{ir}c_{js}
       (\partial_{y_s}\partial_{y_r}w)\circ\phi
   +\sum_r(\partial_{x_j}c_{ir})
       (\partial_{y_r}w)\circ\phi.
 \tag{14}
\]
The coefficients, their first derivatives and the Jacobians are uniformly bounded on the full smaller patch. The right side therefore belongs to $L^2$ on that full patch with the asserted estimate. Exhausting its interior compact subpatches identifies it with the global weak second derivative, without requiring any $H^2$ approximation across the boundary. A finite collection of these boundary patches and interior patches covers $\overline\Omega$, which is compact. Local weak derivatives agree on overlaps since they represent the same distributions. Adding their estimates proves
\[
 \|u\|_{H^2(\Omega)}\leq C_\Omega(\|f\|_2+\|u\|_{H^1(\Omega)}).
\]
Equation (7) yields (6). $\square$

<a id="dirichlet-zero-trace"></a>

The zero-boundary condition is retained in the closure defining $H_0^1$. It also gives zero Sobolev trace in the usual sense. In a flattened strip $0<y_n<a$, a smooth $v$ supported away from the lateral edges satisfies
\[
 \|v(\cdot,0)\|_2^2
 \le a^{-1}\|v\|_2^2+2\|v\|_2\|\partial_nv\|_2
 \le (a^{-1}+1)\|v\|_2^2+\|\partial_nv\|_2^2.
\]
For each fixed $y'$, integrate the derivative of $|v(y',t)|^2$ between zero and $t$, average $t$ over $(0,a)$, and then integrate in $y'$; this proves the first inequality. Smooth functions on a neighborhood of the closed smaller half-strip are dense in its $H^1$ space, locally away from the artificial edges. To see this directly, first translate the function and each of its weak derivatives by $\delta e_n$ toward the interior and restrict to the smaller half-strip. Extend the original function and each derivative by zero only for comparing their $L^2$ translations; translation continuity gives convergence as $\delta\downarrow0$. For fixed $\delta$, mollify with radius less than $\delta/2$. Every convolution used on the smaller half-strip then lies strictly in the original open half-strip, so derivatives commute with convolution there. Choose that radius small enough to make all the finitely many $L^2$ errors tend to zero. A cutoff away from the artificial edges supplies the stated local support. Thus the inequality extends boundary restriction continuously to $H^1$, independently of the chosen approximation. Coordinate integration and the smooth chart bounds transfer it to the boundary patch. The approximating $u_j\in C_c^\infty(\Omega)$ have trace zero, so their $H^1$ limit does too. Only this implication is needed here.

<a id="dirichlet-domain-compact-resolvent"></a>
## 4. The exact operator realization

**Theorem 4.1.** On $L^2(\Omega)$, the Dirichlet Laplacian is the positive self-adjoint operator
\[
 A=-\Delta,\qquad D(A)=H^2(\Omega)\cap H_0^1(\Omega).
 \tag{15}
\]
It satisfies $A\geq C_P^{-2}I$. Its inverse $A^{-1}=K$ is bounded and compact, and every nonreal resolvent $(A-z)^{-1}$ is compact. Its graph norm is equivalent to the $H^2$ norm on (15).

**Proof.** Define initially $A=K^{-1}$ on $\operatorname{Ran}K$, which is dense by Section 2. If $u=Kf$, (3) identifies $-\Delta u=f$ in distributions, and Theorem 3.1 places $u$ in (15). Conversely, for $u$ in (15), $f=-\Delta u\in L^2$. Testing first against $C_c^\infty$ and then using its $H^1$ density in $H_0^1$ proves (3); uniqueness gives $u=Kf$. This proves both domain inclusions and the action in (15), without changing the realization.

The energy identity makes $A$ symmetric and $(Au,u)=\|\nabla u\|_2^2\geq C_P^{-2}\|u\|_2^2$. Its self-adjointness follows directly on its original domain. If $v\in D(A^*)$ and $A^*v=g$, substitute $u=Kf$ in $(Au,v)=(u,g)$ to obtain $(f,v)=(Kf,g)=(f,Kg)$ for every $f\in L^2$. Thus $v=Kg\in D(A)$ and $Av=g$. Symmetry gives the opposite adjoint inclusion. Also $A$ is closed: $u_j\to u$ and $Au_j\to f$ imply $u=Kf$ by boundedness of $K$.

For nonreal $z$, symmetry gives $\|(A-z)u\|_2\geq|\operatorname{Im}z|\|u\|_2$. Closedness makes its range closed: a convergent sequence of images gives convergence of the arguments and of their $A$-images. The orthogonal complement of that range is $\ker(A-\overline z)=0$, so the range is the whole space. Hence $R(z)=(A-z)^{-1}$ is bounded and maps into (15). The inverse identity gives
\[
 R(z)=K(I+zR(z)),
\]
which is compact since $K$ is. Finally (6), with $f=Au$, bounds the $H^2$ norm by the graph norm, while $\|\Delta u\|_2\leq C_n\|u\|_{H^2}$ gives the reverse bound. $\square$

The graph-norm inclusion $D(A)\to L^2$ is compact as well: $(Au,u)=\|\nabla u\|_2^2$ makes its graph-norm unit ball bounded in $H_0^1$, and Lemma 1.1 applies. The generic [compact positive inverse and diagonal-domain provider](compact-spectrum-domains.md#compact-inverse-domains) can then supply an eigenbasis and spectral multiplier domains. That Hilbert-space result alone does not prove any of the boundary or compact Sobolev steps established here.

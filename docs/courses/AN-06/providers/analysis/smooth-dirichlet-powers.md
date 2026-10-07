# Smooth Dirichlet regularity, power domains, and projector growth

*Written by GPT-6.1 Sol (OpenAI); revised and self-checked by GPT-6 Astra (OpenAI). Original exposition: CC0.*

This supplies the boundary regularity, recursive operator domains and parameter Sobolev input used by AN06-U051. Let $X$ be a compact smooth manifold of dimension $n\geq1$, with smooth boundary and no corners. The boundary may be empty, and connectedness is unnecessary. Let $P$ be a scalar differential operator of order two with coefficients smooth up to the boundary, formally symmetric on half densities, with real positive quadratic principal symbol $p(x,\xi)$ for $\xi\ne0$. Its homogeneous Dirichlet realization is strictly positive, as assumed in that lesson. All constants below may depend on $X$, $P$, the fixed coordinate partition and the indicated integer; they are independent of the functions and of the spectral and Sobolev parameters. The zero Hilbert space case is immediate.

John K. Hunter's [*Notes on Partial Differential Equations*, revised 18 June 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), Theorems 4.27 and 4.30 (pp.112–116), give the second-order difference-quotient method; Proposition 4.52 and Theorem 4.53 (pp.124–126) treat the Dirichlet realization. The trace discussion is Theorem 3.44 (pp.72–73). The [full second-order programme proof](dirichlet-domain-and-compactness.md#dirichlet-boundary-h2), equations (8)–(14), establishes the quotient identities, admissible tests and weak coordinate argument for arbitrary smooth real symmetric positive principal coefficients. Sections 1–3 below prove the zero-trace converse and the full higher-order boundary induction, and Sections 4–6 derive the exact recursive domains and projector bound.

We use inner products linear in the first variable and the unitary Fourier transform on $\mathbb R^n$. Fix a smooth positive density $\rho$ on $X$. Write a half density as $h=u\rho^{1/2}$, so that $\|h\|^2=\int_X|u|^2\rho$. This is a unitary identification with $L^2(X,\rho)$, and conjugates $P$ to a smooth scalar differential operator on functions, denoted again by $P$. Its principal symbol is unchanged. Sobolev spaces below refer to this scalar representative; multiplication by any other smooth positive trivializing factor gives equivalent norms. Let $H_0^1(X)$ be the $H^1$ closure of smooth functions compactly supported in $X^\circ$. On a closed component this is the full $H^1$ space. Only nonnegative integer Sobolev orders are needed.

<a id="smooth-dirichlet-approximation"></a>

## 1. Smooth approximation, trace, extension, and interpolation

Use the [finite partition construction](coordinate-inverses-and-integration.md#finite-partitions) to choose a finite smooth coordinate partition $\sum_a\chi_a=1$ on $X$, with each support inside an interior chart or a boundary chart flattened to $\mathbb R^n_+=\{y_n>0\}$. Supports stay away from each chart's artificial edges. The chart pieces $w_a=(\chi_a u)\circ\psi_a$ are extended by zero past those artificial edges, within the half space in a boundary chart. Define $H^k(X)$ by requiring their weak derivatives of order at most $k$ to be in $L^2$, with the squared norm the sum of these local squared norms. Smooth positive Jacobians make the local $L^2$ norms equivalent to the $\rho$ norm. The product rule and the iterated chain rule on the compact chart supports prove equivalence with any other such finite atlas; the weak versions follow from the approximation proved next. In particular smooth differential operators of order $d$ map $H^{k+d}$ boundedly to $H^k$.

**Lemma 1.1 (density up to a flat boundary).** For a nonnegative integer $k$, a compactly supported $w\in H^k(\mathbb R^n_+)$ is an $H^k$ limit of functions smooth on the closed half space, with supports in a common slightly larger compact set. No boundary value condition is required.

**Proof.** For $\varepsilon>0$ put $w_\varepsilon(y)=w(y+\varepsilon e_n)$ on $y_n>-\varepsilon$. Translation there commutes with every weak derivative. For each $|\alpha|\leq k$, extend $\partial^\alpha w$ by zero merely as an $L^2$ function, denoting this extension by $g_\alpha$. On $y_n>0$, $\partial^\alpha w_\varepsilon=g_\alpha(y+\varepsilon e_n)$. Continuity of translations in $L^2(\mathbb R^n)$ proves convergence of these restrictions to $\partial^\alpha w$. This assertion does not assert that $g_\alpha$ is a derivative of the zero extension of $w$.

Extend $w_\varepsilon$ by zero below $y_n=-\varepsilon$ and convolve with a smooth approximate identity of radius $\delta<\varepsilon/2$. On a neighborhood of the closed upper half space convolution samples only $y_n>-\varepsilon$, where the weak derivative identities hold. Its $\alpha$th derivative there is the convolution of $g_\alpha(\,·+\varepsilon e_n)$ with that approximate identity. The whole-space $L^2$ convergence of convolution, and then translation convergence, give $H^k$ convergence on the half space as $\delta,\varepsilon\to0$. The resulting functions are smooth across its boundary. Compact support of $w$ keeps all supports in a common enlarged compact set. Cutoffs first reduce a local chart function to this case. Interior charts use ordinary convolution. A finite partition proves smooth density up to $\partial X$ in every $H^k(X)$. $\square$

The required whole-space density, translation continuity and convolution convergence are proved in [Euclidean approximation, Sections 2–4](euclidean-approximation-and-convolution.md#finite-p-density). These statements apply to each zero-extended derivative as an individual $L^2$ function. They therefore give the convergence above without presupposing a Sobolev extension across the boundary.

<a id="smooth-dirichlet-trace"></a>

**Lemma 1.2 (trace and the zero-trace energy space).** On a flat boundary patch the value trace $T:H^1\to L^2(\partial\mathbb R^n_+)$ is continuous. If $w\in H^{r+1}$ and $\gamma$ is tangential with $|\gamma|\leq r$, then, in boundary distributions,
\[
 T(\partial'^{\gamma}w)=\partial'^{\gamma}(Tw).
 \tag{1}
\]
Consequently tangential derivatives of order at most $r$ of a zero-trace $H^{r+1}$ function belong locally to the zero-boundary energy space after an artificial-edge cutoff. Globally,
\[
 H_0^1(X)=\{u\in H^1(X):Tu=0\}.
 \tag{2}
\]

**Proof.** For a smooth function on a strip $0<y_n<a$, the fundamental theorem of calculus and Cauchy–Schwarz give
\[
 |w(y',0)|^2\leq2|w(y',t)|^2
       +2a\int_0^a|\partial_nw(y',s)|^2\,ds.
\]
Average in $0<t<a$ and integrate in $y'$ to obtain
\[
 \|w(\,·,0)\|_2^2
 \leq \frac2a\|w\|_2^2+2a\|\partial_nw\|_2^2.
 \tag{3}
\]
Lemma 1.1 extends this restriction continuously to $H^1$. For its $H^{r+1}$ approximants, tangential boundary differentiation commutes with restriction. Both the function and its tangential derivatives converge in $H^1$, and hence their traces converge in $L^2$. Testing the boundary identity against a smooth compactly supported boundary function and passing to the limit proves (1). If $Tw=0$, every trace on its left is zero.

Here is the converse required to use those derivatives as energy tests. For a compactly supported $H^1$ function on the closed half space, smooth approximation and (3) justify the integration-by-parts identity
\[
 \int_{y_n>0}w\,\partial_n\phi
 =-\int_{y_n>0}(\partial_nw)\phi
   -\int_{y_n=0}(Tw)\phi
 \tag{4}
\]
for any whole-space smooth test $\phi$. The same approximation gives tangential integration by parts without a boundary term. If $Tw=0$, these identities say that the zero extension $E_0w$ belongs to $H^1(\mathbb R^n)$ and all its weak derivatives are the corresponding zero extensions. Translate it inward by defining $v_\varepsilon(y)=E_0w(y-\varepsilon e_n)$; its support lies in $y_n\geq\varepsilon$. Mollification of radius less than $\varepsilon/2$ gives smooth compactly supported functions in the open half space. Translation and convolution converge in $H^1$, since they converge in $L^2$ for the function and all its first derivatives. Restricting proves $w\in H_0^1$ of the half space. The forward implication follows at once from (3) and the defining $H^1$ approximants with support away from the wall.

Apply this argument to the finitely many boundary chart pieces of $u$; interior pieces are mollified inside their charts. Their smooth compactly supported approximants transfer back and sum to an $H^1$ approximation in $X^\circ$. This proves (2), including the assertion about tangential derivatives after localization. In dimension one there are no nonzero tangential derivatives and the same trace proof applies at each endpoint. $\square$

<a id="smooth-dirichlet-extension"></a>

**Lemma 1.3 (one bounded extension at two orders).** For each integer $k\geq1$ there is a linear extension $E_k:H^k(\mathbb R^n_+)\to H^k(\mathbb R^n)$ with
\[
 \|E_kw\|_{H^k}\leq C_k\|w\|_{H^k},
 \qquad \|E_kw\|_2\leq C_k\|w\|_2.
 \tag{5}
\]
The same extension is used in both bounds.

**Proof.** Let $c_1,\ldots,c_k$ solve
\[
 \sum_{\ell=1}^k c_\ell(-\ell)^j=1,
 \qquad j=0,\ldots,k-1.
 \tag{6}
\]
An explicit solution is $c_\ell=\prod_{a\ne\ell}(1+a)/(a-\ell)$, with empty product equal to one. Indeed the polynomials $L_\ell(t)=\prod_{a\ne\ell}(t+a)/(a-\ell)$ satisfy $L_\ell(-b)=\delta_{\ell b}$. For a polynomial $p$ of degree less than $k$, the difference $p(t)-\sum_\ell p(-\ell)L_\ell(t)$ has degree less than $k$ and vanishes at all $k$ distinct nodes. Successively dividing by the corresponding linear factors makes this difference zero. Evaluating at $t=1$ and taking $p(t)=t^j$ proves (6). For $y_n<0$ define
\[
 E_kw(y',y_n)=\sum_{\ell=1}^k c_\ell w(y',-\ell y_n),
 \qquad E_kw=w\quad(y_n\geq0).
 \tag{7}
\]
For $w$ smooth up to the boundary, (6) matches its two one-sided normal derivatives of orders $0$ through $k-1$; tangential derivatives of these identities also match. Integration by parts on the two half spaces consequently cancels the boundary terms each time a weak derivative of order at most $k$ is taken. Its derivatives are therefore the piecewise classical derivatives, with no boundary distribution. The term with $\ell$ and $j$ normal differentiations has $L^2$ norm on the lower half space equal to $\ell^{j-1/2}$ times the corresponding upper-half-space derivative norm. The triangle inequality gives (5) for every derivative of order at most $k$, including the separate $L^2$ bound. Lemma 1.1, with truncation if needed, extends the formula by completeness to all $H^k$ functions. The $L^2$ bound identifies its limit with the explicit almost-everywhere formula (7), so it is still one extension operator at both orders. $\square$

For whole-space Sobolev functions, the [proved Fourier and Plancherel identities](finite-derivative-l2.md#fourier-normalization) identify the derivative norm with a norm equivalent to $\int(1+|\xi|^2)^k|\widehat v(\xi)|^2d\xi$. For $k\geq1$ and every $\varepsilon>0$, splitting into bounded and large $|\xi|$ gives
\[
 \|v\|_{H^{k-1}(\mathbb R^n)}
 \leq\varepsilon\|v\|_{H^k(\mathbb R^n)}+C_{k,\varepsilon}\|v\|_2.
\]
Apply this to $E_kw_a$ at a boundary chart and to the ordinary compactly supported whole-space chart function in the interior. Equation (5), followed by summation over the same finite partition and adjustment of $\varepsilon$, proves
\[
 \|u\|_{H^{k-1}(X)}
 \leq\varepsilon\|u\|_{H^k(X)}+C_{k,\varepsilon}\|u\|_2.
 \tag{8}
\]
This is proved for $u\in H^k$; membership in that space must be established before using it to absorb a lower-order term.

<a id="smooth-dirichlet-second-order"></a>

## 2. Second-order regularity for the general operator

Fix an auxiliary smooth Riemannian norm on covectors. Compactness and positivity of $p$ give a uniform ellipticity constant $\theta>0$. In the $\rho$ trivialization there is a global expression
\[
 P u=-\rho^{-1}\partial_i(\rho a^{ij}\partial_j u)
                +b^i\partial_i u+c u,
 \tag{9}
\]
in coordinates, with $a^{ij}$ real symmetric positive, and smooth possibly complex lower-order coefficients. Intrinsically the first term is the density divergence of the principal tensor; subtracting it from $P$ leaves an operator of order at most one. The expression (9) is coordinate notation for that global fact.

Its form on $H_0^1$ is
\[
 q(u,v)=\int_X a^{ij}\partial_ju\,\overline{\partial_iv}\,\rho
       +\int_X(b^i\partial_i u+c u)\overline v\,\rho.
 \tag{10}
\]
It is bounded in the $H^1$ norms. Formal symmetry says it is Hermitian on smooth interior tests; their defining density in $H_0^1$ makes it Hermitian on the entire energy space. Bounded lower coefficients and the elementary inequality $ab\leq\varepsilon a^2+(4\varepsilon)^{-1}b^2$ give constants $a_0>0$, $C_0<\infty$ such that
\[
 q(u,u)\geq a_0\|du\|_2^2-C_0\|u\|_2^2,
 \qquad u\in H_0^1(X).
 \tag{11}
\]
Here $q(u,u)$ is real. First derivatives together with $\|u\|_2$ give an equivalent global $H^1$ norm.

**Lemma 2.1.** If $u\in H_0^1(X)$ and $Pu=f\in L^2(X,\rho)$ in distributions, then
\[
 u\in H^2(X),\qquad
 \|u\|_{H^2}\leq C(\|f\|_2+\|u\|_2).
 \tag{12}
\]

**Proof.** The distribution identity first gives $q(u,v)=(f,v)$ on smooth interior tests, and then on all $H_0^1$ tests by continuity. Take $v=u$ in (11) to obtain
\[
 \|u\|_{H^1}\leq C(\|f\|_2+\|u\|_2).
 \tag{13}
\]
For example (11) bounds $a_0\|du\|_2^2$ by $\|f\|_2\|u\|_2+C_0\|u\|_2^2$, which implies (13).

Flatten a boundary patch. Change variables in the weak form, including the smooth positive density Jacobian $J$. Its leading part becomes $-\partial_i(A_{ij}\partial_jw)$ for a smooth real symmetric matrix $A$ with $A\geq\theta_1I$. The lower terms have smooth bounded coefficients $B_i,C$, and the equation is
\[
 -\partial_i(A_{ij}\partial_jw)
       =J(f\circ\psi)-B_i\partial_iw-Cw=:F_0\in L^2.
 \tag{14}
\]
The weak change of variables is justified first on the $H_0^1$ approximants, then by their $H^1$ limits. Equation (14) has exactly the coefficient and right-side hypotheses of equations (10)–(13) of the [full second-order proof](dirichlet-domain-and-compactness.md#dirichlet-boundary-h2). On nested patches use its test $-\delta_{-h}^k(\eta^2\delta_h^kw)$, $k<n$. Lemma 1.2 or the transformed $H_0^1$ approximants make this test admissible. Its discrete product rule, real ellipticity and absorption give
\[
 \|\eta\delta_h^k\nabla w\|_2
       \leq C(\|F_0\|_2+\|w\|_{H^1}).
\]
The bounded derivative functional in that proof supplies all second derivatives with a tangential factor. Expanding (14) then supplies the last one:
\[
 A_{nn}\partial_n^2w
 =-F_0-\sum_{(i,j)\ne(n,n)}A_{ij}\partial_i\partial_jw
                -\sum_{i,j}(\partial_iA_{ij})\partial_jw.
 \tag{15}
\]
Since $A_{nn}\geq\theta_1$, its smooth reciprocal identifies this distribution derivative with a bounded $L^2$ function. In dimension one the omitted-index sum is empty, so this step supplies the entire second derivative. On interior patches the quotient argument uses every direction and gives all second derivatives directly. Smooth lower terms have been moved to $F_0$, which is bounded by $C(\|f\|_2+\|u\|_{H^1})$; no derivative of $f$ is used here.

The weak coordinate formula (14) in the second-order provider transforms these derivatives back. More generally Lemma 1.1 proves the same chain rule by $H^2$ approximation in a chart. Its coefficients and Jacobians are bounded on the compact supports. A finite covering therefore gives $\|u\|_{H^2}\leq C(\|f\|_2+\|u\|_{H^1})$. Finally (13) proves (12). $\square$

The local difference-quotient argument following (13) also proves the local second-order estimate needed for differentiated functions: an $H^1$ solution on a half patch, with zero trace on its flat face and $L^2$ right side, has $H^2$ regularity on a smaller half patch, bounded by that right side and its $H^1$ norm on a larger patch. Insert a cutoff supported away from artificial edges when forming the tests. A cutoff commutator is of order one and hence is controlled by that $H^1$ norm. Symmetry is needed for (13); this local regularity estimate only needs real positive principal coefficients and bounded smooth lower terms.

<a id="smooth-dirichlet-induction"></a>

## 3. The full boundary induction

**Theorem 3.1.** For every integer $r\geq0$, an $H_0^1$ solution of $Pu=f\in H^r(X)$ belongs to $H^{r+2}(X)$ and satisfies
\[
 \|u\|_{H^{r+2}}\leq C_r(\|Pu\|_{H^r}+\|u\|_2).
 \tag{16}
\]

**Proof.** The case $r=0$ is Lemma 2.1. Suppose $r\geq1$ and the result through $r-1$ is established. Since $f\in H^{r-1}$, the induction hypothesis already gives $u\in H^{r+1}$. This prior membership justifies every commutator below.

On a flattened boundary chart write the distribution equation as $Lw=F$, where $L$ has smooth positive second-order coefficients and $F$ is the transformed $f$ (including a smooth Jacobian if the equation was multiplied by it). Then $F\in H^r$. For a tangential multi-index $\gamma$ of length $r$, $v=\partial'^\gamma w\in H^1$. Lemma 1.2 gives $Tv=\partial'^\gamma Tw=0$. In distributions,
\[
 L\partial'^\gamma w
   =\partial'^\gamma F+[L,\partial'^\gamma]w.
 \tag{17}
\]
Use the convention $[L,D]=LD-DL$. Expanding the product rule, the top derivatives in $L D w$ and $D L w$ cancel. Every remaining term differentiates a coefficient at least once, so the commutator has order at most $r+1$. Its $L^2$ norm is at most $C\|w\|_{H^{r+1}}$. The differentiated right side is thus in $L^2$, with bound $C(\|F\|_{H^r}+\|w\|_{H^{r+1}})$.

Apply the local second-order estimate of Section 2 to $v$ on nested half patches. An artificial-edge cutoff has commutator of order one on $v$, bounded by $\|v\|_{H^1}\leq C\|w\|_{H^{r+1}}$. It follows that every derivative of $w$ of total order $r+2$ containing at most two normal factors belongs to $L^2$ on a smaller patch, with the same bound: such a derivative has at least $r$ tangential factors, which can be assigned to $\gamma$, and its two remaining differentiations are supplied by $v\in H^2$.

It remains to recover derivatives with three or more normal factors. Expand the equation into nondivergence form and solve for the second normal derivative:
\[
 a_{nn}\partial_n^2w
   =-F-\sum_{(i,j)\ne(n,n)}a_{ij}\partial_i\partial_jw
          +\sum_i d_i\partial_iw+d_0w,
 \qquad a_{nn}\geq\theta_1>0.
 \tag{18}
\]
The $d_i,d_0$ are smooth and include derivatives of principal coefficients. Let a target derivative be $\partial'^\beta\partial_n^jw$ with $|\beta|+j=r+2$ and $j\geq3$. Differentiate (18) by $D=\partial'^\beta\partial_n^{j-2}$, of total order $r$. On the left its leading term is $a_{nn}\partial'^\beta\partial_n^jw$; every other product term differentiates $a_{nn}$ and contains a derivative of $w$ of total order at most $r+1$. On the right, $DF\in L^2$. The terms where a principal coefficient is not differentiated have derivatives of $w$ of total order $r+2$, with at most $j-1$ normal factors, because $(i,j)\ne(n,n)$ in that sum. All terms where a coefficient is differentiated, and all lower-order terms, have total order at most $r+1$.

Induct on the number $j$ of normal factors, starting with the already obtained cases $0,1,2$. The preceding paragraph places the whole right side and every left-side error in $L^2$ before the new derivative is asserted. Multiplication by the smooth bounded $a_{nn}^{-1}$ then identifies that derivative as an $L^2$ distribution, with bound $C(\|F\|_{H^r}+\|w\|_{H^{r+1}})$. This proves all normal cases up to $r+2$ in finitely many steps. When $n=1$, the other principal sum in (18) is empty; direct $r$-fold normal differentiation gives the same conclusion from $F\in H^r$ and $w\in H^{r+1}$, without a tangential step.

In an interior chart use (17) for every multi-index $\gamma$ of length $r$, and use the interior second-order estimate. This supplies every derivative of total order $r+2$. Weak coordinate chain rules follow from Lemma 1.1; their finite sums have bounded smooth coefficients on the supports. Localizing $u$ introduces $[P,\chi_a]u$, of order one, whose $H^r$ norm is bounded by $C\|u\|_{H^{r+1}}$. Finitely many nested patches give global membership and the estimate
\[
 \|u\|_{H^{r+2}}
    \leq C_r(\|f\|_{H^r}+\|u\|_{H^{r+1}}).
 \tag{19}
\]
Membership has now been established. Apply (8) with $k=r+2$ and choose $\varepsilon$ small enough that the resulting $C_r\varepsilon\|u\|_{H^{r+2}}$ is absorbed on the left of (19). This proves (16) and completes the induction. $\square$

All identities in this induction are distribution identities justified by weak product rules with smooth coefficients. In particular no unproved normal derivative is used as a test, and no derivative of order $r+2$ is hidden in the commutator error.

<a id="smooth-dirichlet-realization"></a>

## 4. The original Dirichlet realization and compact inverse

**Theorem 4.1.** The homogeneous Dirichlet form realization of $P$ has its exact domain
\[
 D(P)=H^2(X)\cap H_0^1(X).
 \tag{20}
\]
It is self-adjoint. Its strictly positive inverse is compact, and it has a complete orthonormal eigenbasis with eigenvalues $\lambda_j>0$, of finite multiplicity, tending to infinity in the infinite-dimensional case.

**Proof.** Choose $c_*>C_0$ large enough that (11) makes
$q_*(u,v)=q(u,v)+c_*(u,v)$ a positive complete inner product on $H_0^1$, equivalent to the $H^1$ norm. For $f\in L^2$ the continuous conjugate-linear functional $v\mapsto(f,v)$ has a unique representative $u$ for that inner product. The elementary Hilbert representation proof is given in [the energy-inverse construction](dirichlet-domain-and-compactness.md#dirichlet-energy-inverse). Define $K_*f=u$. Testing with $u$ gives $\|K_*f\|_{H^1}\leq C\|f\|_2$. Hermitian symmetry gives $(f,K_*g)=q_*(K_*f,K_*g)=(K_*f,g)$, and $(K_*f,f)=q_*(K_*f,K_*f)\geq0$. Thus $K_*$ is bounded, positive and self-adjoint on $L^2$. If $K_*f=0$, the form equation gives $(f,v)=0$ on all interior smooth tests, which are dense in $L^2$, so $f=0$. Its range is dense because its orthogonal complement is $\ker K_*^*=0$.

For completeness, the compact embedding needed here follows from the finite chart partition. A bounded $H_0^1$ family has uniformly bounded $H^1$ zero extensions of its boundary pieces by Lemma 1.2, and compactly supported $H^1$ extensions of its interior pieces. Each has support in a fixed bounded Euclidean set. The [Fourier-cutoff compactness proof](dirichlet-domain-and-compactness.md#dirichlet-compact-embedding), Lemma 1.1 and equation (2), applies to precisely such families: their high-frequency tails are bounded by $N^{-1}$ times the first-derivative norm, while the bounded-frequency operator on a fixed support has a square-integrable kernel and is a norm limit of finite-rank operators. Successively extract subsequences in the finitely many charts. The final subsequence converges in each local $L^2$, and hence globally by bounded Jacobians and $\sum_a\chi_a=1$. Thus $H_0^1(X)\to L^2(X,\rho)$ is compact, and $K_*$ is compact.

Define $Q=K_*^{-1}$ on $\operatorname{Ran}K_*$. The form identity says $(P+c_*)u=f$ in distributions for $u=K_*f$. Lemma 2.1 applied to $Pu=f-c_*u$ proves $u\in H^2\cap H_0^1$. Conversely, for $u$ in that space, $f=(P+c_*)u\in L^2$; the distribution identity and density of energy tests give $q_*(u,v)=(f,v)$, so $u=K_*f$. Hence
\[
 D(Q)=\operatorname{Ran}K_*=H^2\cap H_0^1,
 \qquad Q=P+c_*\text{ on this domain}.
 \tag{21}
\]
Self-adjointness is also on this domain: if $Q^*v=g$, test its defining identity with $u=K_*f$ to get $(f,v)=(K_*f,g)=(f,K_*g)$ for every $f$, so $v=K_*g\in D(Q)$ and $Qv=g$. Symmetry gives the reverse inclusion. The bounded real scalar shift implies $P=Q-c_*$ is self-adjoint on the same domain; indeed its adjoint identity is exactly that for $Q$ after adding $c_*(u,v)$. This constructs the usual homogeneous Dirichlet realization, with both domain inclusions proved before using spectral notation.

Apply the [compact positive inverse and diagonal-domain proof](compact-spectrum-domains.md#positive-compact-inverse) to $K_*$. It gives a complete orthonormal eigenbasis $h_j$ of $Q$, with positive eigenvalues $\nu_j$ tending to infinity and finite multiplicities. Equation (21) makes these eigenvectors eigenvectors of the original $P$, with $\lambda_j=\nu_j-c_*$. The assumed strict positivity of $P$ gives $\lambda_j>0$ for every $j$. Since the sequence tends to infinity, its infimum is positive (the finite-dimensional case is immediate). In particular even if strict positivity is stated only as $(Pu,u)>0$ for nonzero $u\in D(P)$, it gives a uniform positive lower bound here.

The diagonal $P^{-1}$ is bounded because $\inf_j\lambda_j>0$. Its finite-rank truncations converge in operator norm because $\lambda_j^{-1}\to0$, so it is compact. The two inverse identities hold on the domain (21): $\nu_j/\lambda_j=1+c_*/\lambda_j$ is bounded, so the image of the proposed inverse lies in $D(Q)$; conversely coordinate inversion gives $P^{-1}Pu=u$. It is therefore the inverse of the original realization rather than a new diagonal realization. The same compact positive inverse provider applied to $P^{-1}$ gives every exact spectral multiplier domain. $\square$

<a id="smooth-dirichlet-powers"></a>

## 5. Every recursive power domain and its elliptic estimate

**Theorem 5.1.** For each integer $m\geq1$,
\[
 \begin{aligned}
 D(P^m)&=\{u\in H^{2m}(X):P^\ell u\in H_0^1(X)
                                  \text{ for }\ell=0,\ldots,m-1\},\\
 D(P^m)&=\left\{u=\sum_j u_jh_j:
                       \sum_j\lambda_j^{2m}|u_j|^2<\infty\right\},\\
 P^m u&=\sum_j\lambda_j^m u_jh_j,\\
 \|u\|_{H^{2m}}&\leq C_m(\|P^m u\|_2+\|u\|_2).
 \end{aligned}
 \tag{22}
\]
Here $P^\ell$ in the first line is the iterated differential expression. Its boundary conditions concern the value trace of each iterate; they do not prescribe all normal derivatives of $u$.

**Proof.** The first line for $m=1$ is (20). By the definition of an iterated unbounded operator,
\[
 D(P^{m+1})=\{u\in D(P):Pu\in D(P^m)\}.
 \tag{23}
\]
Suppose the first line holds at $m$. If $u$ satisfies (23), then $u\in H^2\cap H_0^1$ and $Pu\in H^{2m}$. Theorem 3.1 with $r=2m$ yields $u\in H^{2m+2}$. The boundary conditions are $u\in H_0^1$ and $P^\ell(Pu)\in H_0^1$ for $\ell=0,\ldots,m-1$, exactly the conditions asserted at $m+1$.

Conversely let $u\in H^{2m+2}$ with $P^\ell u\in H_0^1$ for $\ell=0,\ldots,m$. Smooth coefficients give $Pu\in H^{2m}$, and its iterates of orders $0,\ldots,m-1$ have zero boundary value by the stated conditions. The inductive domain description puts $Pu\in D(P^m)$, while $u\in D(P)$ by (20). Equation (23) proves the converse. Every iterate used is a well-defined Sobolev function before its membership is asserted. This completes the domain induction.

The spectral lines follow from the [ordered diagonal power domains](compact-spectrum-domains.md#all-diagonal-multipliers-and-ordered-domains), on the original domain established in Section 4. In particular, for $0\leq\ell\leq m$, $t^{2\ell}\leq1+t^{2m}$, $t\geq0$, gives
\[
 \|P^\ell u\|_2\leq\|u\|_2+\|P^m u\|_2.
 \tag{24}
\]
The elliptic estimate at $m=1$ is (12). For $m\geq2$, Theorem 3.1 with $r=2m-2$ and the estimate at $m-1$ applied to $Pu\in D(P^{m-1})$ give
\[
 \|u\|_{H^{2m}}
 \leq C_m(\|Pu\|_{H^{2m-2}}+\|u\|_2)
 \leq C_m'(\|P^mu\|_2+\|Pu\|_2+\|u\|_2).
\]
Equation (24) proves the last line of (22). Conversely $P^m$ is a smooth differential operator of order $2m$, so $\|P^m u\|_2\leq C_m\|u\|_{H^{2m}}$. Thus its graph norm and the $H^{2m}$ norm are equivalent on the displayed domain. $\square$

For $u\in\bigcap_mD(P^m)$, (22) gives every integer Sobolev order and the zero trace of every iterate. Smoothness up to the boundary follows directly from the Fourier argument in Section 6 applied to derivatives: for a chart extension in sufficiently large $H^k$, $\xi^\alpha\widehat v\in L^1$ when $k>|\alpha|+n/2$, by weighted Cauchy–Schwarz. Fourier inversion and dominated convergence give continuous derivatives through any prescribed finite order. Every eigenfunction belongs to every power domain because $P^m h_j=\lambda_j^m h_j$, and is therefore smooth up to the boundary, with homogeneous Dirichlet value.

<a id="smooth-dirichlet-projector-growth"></a>

## 6. Parameter Sobolev estimate and polynomial projector growth

**Theorem 6.1.** If $m$ is a positive integer with $2m>n/2$, then for $s\geq1$ and $u\in H^{2m}(X)$,
\[
 s^{2m-n/2}\|u\|_\infty^2
  \leq C_m\bigl(\|u\|_{H^{2m}}^2+s^{2m}\|u\|_2^2\bigr).
 \tag{25}
\]
The supremum uses the scalar representative relative to $\rho$. With $E_\lambda=1_{(0,\lambda]}(P)$, either endpoint convention, the diagonal spectral density relative to $\rho$ and the counting function satisfy
\[
 e_{P,\rho}(x,x;\lambda)\leq C\lambda^{n/2},
 \qquad N_P(\lambda)\leq C'\lambda^{n/2},
 \qquad \lambda\geq1,
 \tag{26}
\]
uniformly up to the boundary. The same bounds hold for the diagonal density relative to the principal metric volume $dV_g$.

**Proof.** For $v\in H^{2m}(\mathbb R^n)$, Fourier inversion and weighted Cauchy–Schwarz give
\[
 \begin{aligned}
 |v(x)|^2
 &\leq(2\pi)^{-n}
     \left(\int_{\mathbb R^n}\frac{d\xi}{s^{2m}+|\xi|^{4m}}\right)
     \left(\int_{\mathbb R^n}(s^{2m}+|\xi|^{4m})
                                      |\widehat v(\xi)|^2\,d\xi\right),\\
 \int\frac{d\xi}{s^{2m}+|\xi|^{4m}}
 &=s^{n/2-2m}\int\frac{d\eta}{1+|\eta|^{4m}}<\infty.
 \end{aligned}
 \tag{27}
\]
The substitution is $\xi=s^{1/2}\eta$. The last integral is finite because $4m>n$. The other factor is at most $C_m\|v\|_{H^{2m}}^2+s^{2m}\|v\|_2^2$. The same estimate proves $\widehat v\in L^1$, so its inverse Fourier transform is a continuous representative; Fourier inversion here is justified by that integrability. Approximation or Plancherel identifies it with the original Sobolev function.

Apply (27) to $E_{2m}w_a$ in a boundary chart. Both bounds in (5) use that same extension, giving exactly the two norms on the right of (25), without replacing the parameter-weighted $L^2$ term by a higher norm. For interior pieces use the ordinary compactly supported extension. Since $u=\sum_a\chi_a u$, Cauchy–Schwarz for this finite sum and bounded coordinate and density factors prove (25) globally, with the same power of $s$. They also give a continuous representative on $X$.

Section 4 makes the spectral subspace $\operatorname{Ran}E_\lambda$ finite dimensional. Its elements belong to all power domains, and for $u$ in it the spectral norm identity gives
\[
 \|P^m u\|_2\leq\lambda^m\|u\|_2.
\]
Use (22) and then (25) with $s=\lambda\geq1$ to get
\[
 \|u\|_\infty^2\leq C\lambda^{n/2}\|u\|_2^2.
 \tag{28}
\]
Write $h_j=u_j^{(\rho)}\rho^{1/2}$ for the normalized eigenfunctions. At each $x$, the norm squared of evaluation on this finite-dimensional Hilbert subspace equals
\[
 \sum_{\lambda_j\leq\lambda}|u_j^{(\rho)}(x)|^2
     =e_{P,\rho}(x,x;\lambda).
 \tag{29}
\]
Indeed Cauchy–Schwarz gives this norm bound for the coefficient vector, and choosing coefficients proportional to the conjugates of the evaluated eigenfunction values attains it when their sum is nonzero. Equation (28) bounds (29) by $C\lambda^{n/2}$. Integrating the finite sum against $\rho$ counts exactly its orthonormal eigenfunctions, including multiplicities, proving (26).

Finally write $h_j=u_j^{(g)}(dV_g)^{1/2}$. Then
\[
 u_j^{(g)}=(\rho/dV_g)^{1/2}u_j^{(\rho)},
 \qquad e_{P,g}=(\rho/dV_g)e_{P,\rho}.
 \tag{30}
\]
This smooth positive ratio is bounded above and below on compact $X$. Thus the metric-volume diagonal has the same uniform power bound, and its integral is the same counting function. This proves the half-density convention and the stated metric normalization explicitly. $\square$

These estimates are also uniform for families on fixed $X$, with fixed $\rho$ and coordinate partition, a common positive ellipticity lower bound, and common bounds on every coefficient derivative used at the chosen order. Indeed the second-order quotient estimate uses only first derivatives of the principal coefficients and bounds on the lower coefficients. At induction level $r$, the product rule in (17)–(18) adds only finitely many coefficient derivatives through order $r+1$, and division uses the same ellipticity lower bound. The interpolation constants depend only on the fixed charts. Induction therefore gives a common constant in (16), and the finite iteration in (22) gives one in the power estimate. Finally (27) and the fixed extension operator have no operator-dependent constants, so (26) is uniform as well. This argument uses no common lower bound for the positive eigenvalues: the estimates retain the separate $L^2$ term.

The parameter inequality (25) converts the elliptic power estimate into the uniform projector and counting bounds (26). Curved diagonal asymptotics require the additional local wave analysis in [Curved boundary spectral reduction](curved-boundary-spectral-reduction.md); generalized reflected propagation is developed in [Generalized reflected curves](generalized-reflected-curves.md).

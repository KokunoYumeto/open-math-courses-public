# Wavefront-qualified pullback and restriction of phases

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="qualified-pullback"></a>

This reading proves pullback by an arbitrary smooth map under its wavefront qualification, including convergence, coordinate independence and the wavefront estimate. It then proves the order and normalization of a transverse restriction of a Lagrangian half density. For comparison, see [Hörmander, *Fourier integral operators I*, Theorem 2.5.11′ and Proposition 4.1.7](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392052). The arguments needed here are written below. Prerequisites are the [Fourier wavefront, cutoff and nonlinear-test estimates](phase-geometry-and-stationary-phase.md#phase-wavefront), its earlier phase and principal-symbol construction, and the [density quotient calculation](transverse-composition-and-graph-operators.md#density-contraction). The convention is $\widehat v(\xi)=\int e^{-ix\cdot\xi}v(x)\,dx$.

## 1. Statement and precise convergence

Let $f:Y\to X$ be smooth. Its normal set is
\[
 N_f=\{(f(y),\xi):\xi\ne0,\ df_y^T\xi=0\}.
 \tag{R1}
\]
If $\operatorname{WF}(u)\cap N_f=\varnothing$, there is a canonical scalar distribution $f^*u$ agreeing with $u\circ f$ for continuous $u$. It satisfies
\[
 \operatorname{WF}(f^*u)\subset f^*\operatorname{WF}(u)
 =\{(y,df_y^T\xi):(f(y),\xi)\in\operatorname{WF}(u)\}.
 \tag{R2}
\]
All covectors on the right are nonzero. Write $\mathcal D'_\Gamma(X)=\{v\in\mathcal D'(X):\operatorname{WF}(v)\subset\Gamma\}$. For a closed conic set $\Gamma$ avoiding $N_f$, pullback is sequentially continuous from $\mathcal D'_\Gamma(X)$ to $\mathcal D'_{f^*\Gamma}(Y)$ in the following sense. A sequence $u_j$ with every $u_j$ and its limit $u$ in this same $\mathcal D'_\Gamma$ converges there when it converges weakly as distributions and, for every compactly supported smooth $\chi$ and closed frequency cone $V$ with $(\operatorname{supp}\chi\times V)\cap\Gamma=\varnothing$ in a chart,
\[
 \sup_{\xi\in V}\langle\xi\rangle^L
       |\widehat{\chi(u_j-u)}(\xi)|\longrightarrow0
       \quad\text{for every }L.
 \tag{R3}
\]
Coordinate invariance of this convergence is proved below. This specifies both existence and the uniqueness of the extension from smooth functions. Scalar distributions act on compactly supported test densities. Pullback of a general density bundle requires additional bundle data; we distinguish that issue in Section 6.

## 2. The absolutely convergent local construction

Fix $y_0$, put $x_0=f(y_0)$, and work in compactly contained coordinate neighborhoods. For existence take $\Gamma=\operatorname{WF}(u)$; for sequential continuity use the fixed closed cone $\Gamma$ from Section 1, containing all the wavefronts in the sequence. Closedness of $\Gamma$ and compactness of unit directions allow these neighborhoods to be made small enough that a closed cone $B$ contains every direction of $\Gamma$ over the chosen $x$ neighborhood in its angular interior and
\[
 |df_y^T\xi|\ge c|\xi|\quad(\xi\in B)
 \tag{R4}
\]
throughout the chosen $y$ neighborhood. Indeed, failure after arbitrarily small shrinkings would give unit directions tending to a direction of $\Gamma$ over $x_0$ killed by $df_{y_0}^T$. This contradicts $\Gamma\cap N_f=\varnothing$. If $\Gamma$ has no directions over $x_0$, it has none over a sufficiently small neighborhood, by the same compactness argument; take $B$ empty there. In the sequential statement, the neighborhoods, cone $B$ and constant $c$ are thus fixed for the whole sequence.

Choose $\chi=1$ near the image of the smaller $y$ neighborhood and set $v=\chi u$, compactly supported in that $x$ neighborhood. The Fourier transform of $v$ has polynomial growth everywhere and is rapidly decreasing outside $B$, by the finite angular covering and cutoff estimates in the wavefront prerequisite. For $\psi\in C_c^\infty(Y)$ supported in the smaller neighborhood, put
\[
 I_\psi(\xi)=\int e^{if(y)\cdot\xi}\psi(y)\,dy,
 \qquad
 \langle f^*u,\psi\,dy\rangle
     =(2\pi)^{-\dim X}\int\widehat v(\xi)I_\psi(\xi)\,d\xi.
 \tag{R5}
\]
On $B$, the operator
$[df_y^T\xi\cdot\partial_y]/[i|df_y^T\xi|^2]$
fixes the exponential. Each transfer to $\psi$ costs at least one power of $|\xi|^{-1}$: all differentiated coefficients have that degree, with bounded angular and base derivatives by (R4). Hence, for $|\xi|\ge1$,
$|I_\psi(\xi)|\le C_L|\xi|^{-L}\max_{|\alpha|\le L}\|\partial^\alpha\psi\|_\infty$ on $B$. Everywhere else the integral is bounded by a constant times $\|\psi\|_\infty$. Thus (R5) is absolutely convergent, and a sufficiently large finite $L$ bounds it by finitely many test seminorms. It defines a distribution. Fourier inversion proves agreement with smooth composition.

## 3. Uniform bounds, approximation and locality

We supply the uniform finite-order fact used in passing to limits. If distributions $w_j$ converge weakly on a coordinate neighborhood and $K$ is a fixed compact set, then
\[
 |\langle w_j,\varphi\rangle|
 \le C\max_{|\alpha|\le M}\|\partial^\alpha\varphi\|_\infty
 \quad(\operatorname{supp}\varphi\subset K)
 \tag{R6}
\]
for some common $C,M$. Here is a proof, including its completeness step. The space of smooth functions supported in $K$, with seminorms $q_k=\max_{|\alpha|\le k}\|\partial^\alpha\varphi\|_\infty$ and metric $\sum2^{-k}\min(1,q_k(\varphi-\psi))$, is complete. A Cauchy sequence has uniform limits for every derivative; the fundamental theorem along coordinate lines identifies these limits as the derivatives of a smooth limit, still supported in $K$.

The closed sets $E_l=\{\varphi:\sup_j|w_j(\varphi)|\le l\}$ cover that space by weak convergence. They cannot all have empty interior: otherwise, successively choose a closed ball of radius less than $2^{-l}$ inside the preceding open ball and outside $E_l$. Completeness gives a common limiting point in the nested balls, outside every $E_l$, a contradiction. Some $E_l$ therefore contains a neighborhood of some $\varphi_0$. Taking differences yields a neighborhood of zero on which $\sup_j|w_j|\le2l$. Such a neighborhood contains $q_M<\delta$ for a finite $M$ and $\delta>0$. Rescaling proves (R6), including the case $q_M=0$ by arbitrary rescaling. Multiplying by a fixed compact cutoff and testing against $e^{-ix\xi}$ now gives a common polynomial Fourier bound $C\langle\xi\rangle^M$.

Weak convergence also gives uniform convergence of these Fourier transforms on bounded frequency sets. The test functions $\chi e^{-ix\xi}$, for bounded $\xi$, form a compact set in the finite $q_M$ norm; a finite net, (R6), and pointwise convergence prove uniform convergence. Together with (R3), this justifies dominated convergence in (R5): on $B$ use the common polynomial bound and arbitrarily rapid $I_\psi$; outside $B$ use the uniform rapid Fourier bounds. The same finite test estimates show weak convergence of the resulting pullbacks.

Smooth approximation in this convergence is available locally. Choose a compactly supported smooth mollifier $\rho$ of integral one, and use $v_\epsilon=\rho_\epsilon*v$ on a smaller chart. Its Fourier transform is $\widehat\rho(\epsilon\xi)\widehat v(\xi)$, so it converges weakly, has a common polynomial bound, and converges with every rapid seminorm on every cone where $\widehat v$ is rapid. The last assertion follows by splitting at a large fixed $|\xi|$: the tail is uniformly small using one stronger rapid bound, while on the bounded part $\widehat\rho(\epsilon\xi)\to1$ uniformly. For a localized seminorm (R3), choose a second cutoff equal to one near $\operatorname{supp}\chi$. Convolution of its localized distribution agrees near that support for sufficiently small $\epsilon$. Multiplication by $\chi$ is Fourier convolution with the rapidly decreasing $\widehat\chi$. Splitting this convolution into an inner cone with an angular margin and its complement gives the same convergence: on the inner cone use the rapid bounds just proved; on the complement $|\xi-\zeta|\ge c(|\xi|+|\zeta|)$ and the common polynomial bound is dominated by arbitrarily many powers of $\widehat\chi$. Thus all seminorms (R3) converge. Finite chart partitions give the same approximation on every fixed compact set; a locally finite partition and expanding compact sets give a global sequence if needed.

If two choices of $\chi$ in (R5) differ, their difference times $u$ is supported away from $f(\operatorname{supp}\psi)$. Its compact mollifications vanish near that image for sufficiently small $\epsilon$. Their smooth pullbacks are zero on $\operatorname{supp}\psi$, and the convergence just proved shows that their limiting contribution is zero. This proves locality and independence of the cutoff. If $u$ is continuous, its mollifications converge uniformly near this compact image; hence (R5) agrees with the continuous function $u\circ f$.

## 4. Wavefront estimate and convergence of its seminorms

Let $(y_0,\eta_0)$ be outside $f^*\Gamma$. After shrinking neighborhoods, choose the bad cone $B$ as above and a closed cone $C$ around $\eta_0$ such that
\[
 |df_y^T\xi-\eta|\ge c'(|\xi|+|\eta|)
       \quad(\xi\in B,\ \eta\in C).
 \tag{R7}
\]
To prove this choice, normalize $|\xi|+|\eta|=1$. A sequence of failed inequalities has a convergent subsequence. Equation (R4) rules out a nonzero $\xi$ with zero $\eta$; the boundedness of $df$ rules out zero $\xi$ with nonzero $\eta$. The remaining limit would give a direction of $f^*\Gamma$ at $(y_0,\eta_0)$, contrary to the choice of that point. The cones and neighborhoods can therefore be enlarged or shrunk by a small positive margin while retaining (R7). The same argument shows that $f^*\Gamma$ is locally closed: bounded image covectors bound $\xi$ by (R4), and a convergent subsequence stays in the closed $\Gamma$.

For a cutoff $\psi$ near $y_0$, (R5) gives
\[
 \widehat{\psi f^*u}(\eta)
  =(2\pi)^{-\dim X}\int\widehat v(\xi)
       \int e^{i(f(y)\cdot\xi-y\cdot\eta)}\psi(y)\,dy\,d\xi.
 \tag{R8}
\]
On $B$, transfer the $y$ gradient using (R7). Its normalized derivatives have order minus one in $(\xi,\eta)$, so the inner integral is bounded by $C_L(1+|\xi|+|\eta|)^{-L}$. Multiplication by the polynomial bound for $\widehat v$ and integration in $\xi$ gives every inverse power of $\langle\eta\rangle$ by increasing $L$.

Outside $B$, $\widehat v$ is rapid. Split into $|\xi|\le a|\eta|$ and $|\xi|>a|\eta|$, where $a>0$ is small enough that $\|df\|a\le1/2$. In the first region the gradient has length at least $|\eta|/2$, and each transfer gains $|\eta|^{-1}$ because all higher derivatives of the phase are $O(|\xi|+|\eta|)$. The integral of the rapidly decreasing $\widehat v$ is finite. In the second region the inner integral is bounded, and the rapid tail of $\widehat v$ again gives every inverse power of $\langle\eta\rangle$. This proves (R2).

For a convergent sequence in (R3) these estimates are uniform with arbitrarily many powers, using (R6) on $B$ and the uniform rapid bounds outside it. Thus, for any required weighted supremum in $\eta$, the large-frequency tail of the difference is uniformly small by using one extra inverse power. On a fixed bounded $\eta$ set, the inner test functions depend smoothly on $\eta$; dominated convergence in the $\xi$ integral is uniform there, by the finite-frequency convergence and integrable tail estimates from Section 3. The weighted supremum of the difference therefore tends to zero. A finite covering of the support and angular directions proves every target seminorm (R3). This establishes the asserted sequential continuity into $\mathcal D'_{f^*\Gamma}$.

## 5. Coordinates, uniqueness and composition of maps

Changing coordinates in $Y$ in (R5) is the usual change of integration variables, including the test-density Jacobian, so it gives the same distribution. For a source coordinate diffeomorphism $g$, the distributional change of coordinates is defined on tests by its smooth Jacobian; it preserves weak convergence. It preserves the convergence (R3) as well. Indeed, the localized transformed Fourier test has phase $g(x)\cdot\eta-x\cdot\xi$ (or the inverse coordinate map, according to the chart direction). On separated frequency directions its gradient is bounded below by a fixed multiple of $|\xi|+|\eta|$; repeated integration by parts gives every inverse power, against the common polynomial bound (R6). On the remaining directions the original Fourier transform is rapid whenever the transformed cone misses the transformed $\Gamma$. Splitting small and large $|\xi|/|\eta|$ exactly as in (R8) gives uniform rapid tails. On bounded frequencies weak convergence and finite nets give convergence, hence all rapid seminorms converge. These are the nonlinear Fourier-test estimates of the phase reading, now with their constants uniform for the sequence. They prove both the required coordinate rule for (R3) and its compatibility with the ordinary cotangent transformation of $\Gamma$.

Approximate $u$ smoothly as in Section 3, make the source coordinate change on that sequence, and use the proved sequential continuity in both charts. Smooth composition is coordinate independent, so its two limits agree. Locality now glues (R5) on manifolds. Any sequentially continuous extension agreeing on smooth functions must have these same limits; thus it is unique. If $g:Z\to Y$ also satisfies $f^*\Gamma\cap N_g=\varnothing$, then $\Gamma\cap N_{f\circ g}=\varnothing$ by the chain rule, and
\[
 (f\circ g)^*u=g^*(f^*u).
 \tag{R9}
\]
Apply both sides to the same smooth approximating sequence and use sequential continuity twice to prove this identity. The estimate in Section 4 ensures that the intermediate sequence has the required $f^*\Gamma$ control.

<a id="phase-restriction"></a>

## 6. Transverse restriction, half densities and the quarter order

Let $i:S\hookrightarrow X$ have codimension $k$, and use coordinates $(s,t)$ with $S=\{t=0\}$. Suppose a conic Lagrangian $\Lambda$ avoids $N^*S$ and is transverse to $T^*X|_S$. Equivalently, the function $t$ restricted to $\Lambda$ is a submersion. Let $u\in I^m(X,\Lambda;\Omega_X^{1/2})$. For restriction of this half density, choose the normal half-density frame $|dt|^{1/2}$; divide by it to interpret the restricted bundle as $\Omega_S^{1/2}$. There is no canonical such division for arbitrary embeddings without specified normal data.

Represent $u$ locally by a nondegenerate phase $\phi(s,t,\theta)$ with $N$ phase variables and amplitude order $q=m+(d-2N)/4$, where $d=\dim X$. On $C_\phi$, transversality makes the differentials $(d\phi_\theta,dt)$ independent. Restricting to $t=0$ therefore makes $d_{s,\theta}\phi_\theta$ independent: any relation between those restricted differentials would give a relation with $dt$ in the full ambient space. At a critical point, $\phi_s\ne0$, since otherwise its covector would be a nonzero element of $N^*S$. Thus $\phi(s,0,\theta)$ is a nondegenerate phase, defining the immersed restricted Lagrangian
\[
 \Lambda_S=\{(s,\xi_s):(s,0;\xi_s,\xi_t)\in\Lambda\}.
 \tag{R10}
\]
This statement is local on each phase branch; when branches meet it means their locally finite sum, not a claim that the image is globally embedded.

Restriction of the actual distribution equals this restricted phase integral. To justify that equality, cut off the original phase integral at bounded frequency. The resulting smooth kernels converge weakly to $u$. On every closed cone disjoint from a sufficiently small closed conic neighborhood $\Gamma$ of $\Lambda$, the nonstationary phase estimates in the phase reading give uniform rapid Fourier bounds for these cutoffs, with a common distribution order. Their bounded-frequency Fourier transforms converge uniformly by weak convergence and (R6). Using one stronger rapid bound proves convergence in every seminorm (R3). On the local compact support, $\Gamma$ can be chosen to avoid $N^*S$ by the stated qualification. Sequential continuity of $i^*$ then shows that restricting the smooth cutoffs tends to the qualified restriction. The nondegenerate restricted phase has its own distributional cutoff limit by the phase construction. Both limits use exactly the same cutoffs, proving the assertion.

The normalization is consequential. The old integral factor is $(2\pi)^{-(d+2N)/4}$, while the normalized integral on $S$ has factor $(2\pi)^{-(d-k+2N)/4}$. Hence its normalized amplitude and its order are
\[
 \begin{gathered}
 a_S=(2\pi)^{-k/4}a|_{t=0},\\
 q=m_S+(d-k-2N)/4,\\
 m_S=m+k/4.
 \end{gathered}
 \tag{R11}
\]
In critical densities, restricting and dividing by $|dt|$ gives
$d_{\phi|S}=d_\phi/|dt|$. To check this, use the independent coordinates $(\phi_\theta,t)$ transverse to the restricted critical set. Divide the ambient density first by $|d\phi_\theta|$, then by $|dt|$, or in the opposite order. The determinant of the block triangular coordinate matrix is the same product in either order. This is precisely the quotient-density rule proved in the composition reading. The phase Hessian in $\theta$ is unchanged at $t=0$, so its Maslov frame restricts with the same transition factors. Consequently
\[
 \sigma(i^*u)=(2\pi)^{-k/4}
       \frac{\sigma(u)|_{\Lambda\cap T^*X|_S}}{|dt|^{1/2}}
 \tag{R12}
\]
under that normal-frame choice and the natural map to the restricted phase branch. This division means the density quotient on the submersion $t|_\Lambda$, rather than division of scalar coefficients in unrelated coordinates. Different choices of normal frame give exactly the corresponding half-density bundle transformation.

<a id="wave-restrictions"></a>

## 7. The restrictions needed by a wave kernel

For a joint wave relation parametrized by $(t,y,\eta)$ with $\tau=-p(y,\eta)$, $p>0$, and nonzero spatial covectors, restriction to $t=t_0$ satisfies both conditions of Section 6: $t$ is a submersion on the relation and no covector is purely temporal. Thus
\[
 I^{-1/4}(\mathbb R\times X\times X,\Lambda)
       \longrightarrow I^0(X\times X,\Lambda_{t_0}).
 \tag{R13}
\]
With the chosen normal frame $|dt|^{1/2}$ it removes the factor $(2\pi)^{1/4}|dt|^{1/2}$ in the joint-parameter normalization (G18). This is the exact initial-symbol rule used in scalar wave transport.

For the spatial diagonal map $(t,x)\mapsto(t,x,x)$, the normal covectors are $(0,\xi,-\xi)$. The nonzero time component $\tau=-p$ excludes them. The general pullback theorem applies regardless of whether the diagonal intersection is transverse, and sends a wave covector $(\tau,\xi,-\eta)$ to $(\tau,\xi-\eta)$. No transverse-Lagrangian order assertion is made for that possibly singular intersection. For the time fiber $t\mapsto(t,x_0,y_0)$, the normal covectors have temporal component zero, again excluded by $\tau\ne0$. Finally, on the spatial diagonal the two spatial half-density factors canonically multiply to a spatial density. This bundle operation accompanies the scalar coefficient pullback and supplies the density that can be integrated to take the trace.

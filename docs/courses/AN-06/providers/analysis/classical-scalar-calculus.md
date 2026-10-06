# Classical scalar symbols, Sobolev mapping and elliptic domains

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

Finite symbol expansions control composition, adjoints and coordinate changes. Combined with the order-zero operator bound, they give real Sobolev mapping and exact elliptic domains. We use $\rho=1$, $\delta=0$, real orders, $D=-i\partial$ and inverse Fourier factor $(2\pi)^{-n}$. Read the finite scalar sections first; the graph-FIO section then connects them to phase geometry and transverse composition.

The order-zero input is the full local proof of [A finite-derivative bound for left quantization](finite-derivative-l2.md#finite-derivative-l2). Its [Euclidean product theorem](finite-derivative-l2.md#euclidean-products) and [Fourier inversion and Plancherel proofs](finite-derivative-l2.md#fourier-normalization) supply the integration and Fourier inputs below. Smooth coordinate inverses, change of variables and finite smooth partitions are proved in [Coordinate inverses, integration and surface measure](coordinate-inverses-and-integration.md#coordinate-integration). The [approximation provider, Sections 1–4](euclidean-approximation-and-convolution.md), supplies smooth approximation and weak differentiation. Taylor's formula used below follows by applying the one-dimensional fundamental theorem repeatedly to the function on the displayed line segment, giving its stated integral remainder. Operators on a closed manifold act on scalar half densities. Fix a finite smooth atlas and subordinate partition when defining Sobolev norms; all conclusions below hold for that actual atlas.

<a id="finite-scalar-calculus"></a>

## Finite symbol calculus

On a coordinate patch a symbol $a\in S^m_{1,0}$ satisfies, for every compact set of $x$ and every $\alpha,\beta$,
\[
 |\partial_x^\alpha\partial_\xi^\beta a(x,\xi)|
 \leq C_{\alpha\beta}\langle\xi\rangle^{m-|\beta|}.
\]
Use left quantization
\[
 \operatorname{Op}(a)u(x)=(2\pi)^{-n}\iint
 e^{i(x-y)\cdot\xi}a(x,\xi)u(y)\,dy\,d\xi,
\]
The following construction defines the kernel, its cutoff limit and all finite errors. Write $\langle v\rangle=(1+|v|^2)^{1/2}$. We will repeatedly use, for real $r$ and $0\le t\le1$,
\[
 \langle\xi+t\eta\rangle^r
 \le 2^{|r|/2}\langle\xi\rangle^r\langle\eta\rangle^{|r|}.
 \tag{FC1}
\]
For $r\ge0$ this follows by squaring the elementary inequality $\langle u+v\rangle\le\sqrt2\langle u\rangle\langle v\rangle$. For $r<0$ apply that inequality to $\xi=(\xi+t\eta)-t\eta$ and take the appropriate reciprocal. Thus negative orders cause no exception.

**Kernel definition and localization.** First suppose an amplitude $A(x,y,\zeta)$ is smooth, has compact support in $(x,y)$, and satisfies
\[
 |\partial_x^\alpha\partial_y^\gamma\partial_\zeta^\beta
       A(x,y,\zeta)|\le C_{\alpha\gamma\beta}
          \langle\zeta\rangle^{m-|\beta|}.
 \tag{FC2}
\]
Its kernel is the distributional limit of
$(2\pi)^{-n}\int e^{i(x-y)\cdot\zeta}A(x,y,\zeta)\chi(\varepsilon\zeta)\,d\zeta$,
where $\chi$ is compactly supported, smooth and equals one near zero. Indeed, when pairing with a compact smooth test in $(x,y)$, integrate $2L$ derivatives in $y$ using $1-\Delta_y$. The integral is then bounded by an integrable multiple of $\langle\zeta\rangle^{m-2L}$ once $2L>m+n$. Dominated convergence gives a limit independent of $\chi$. For its action on a smooth input $u$, the same integration differentiates $A(x,y,\zeta)u(y)$. After $k$ output derivatives, choose $2L>m+k+n$. This bounds the output $C^k$ seminorm by finitely many amplitude and input seminorms and proves a continuous map from smooth inputs to compactly supported smooth outputs. The transposed kernel has the same property. Transposition therefore defines the continuous distributional action whenever support makes the pairing compact.

Away from $x=y$, use
$e^{i(x-y)\zeta}=|x-y|^{-2}(x-y)\cdot D_\zeta e^{i(x-y)\zeta}$
and integrate by parts in $\zeta$. Each transfer lowers the symbol order by one. After any prescribed output and input derivatives, sufficiently many transfers leave an absolutely integrable frequency function, uniformly on compact sets separated from the diagonal. Terms differentiating the extra cutoff tend to zero by the same bound. The kernel is consequently smooth there. A cutoff equal to one near the diagonal makes the kernel properly supported, meaning that both projections of its support are proper. Its complement is a smooth kernel. Conversely, for a properly supported operator, compact localization in one position variable allows compact localization in the other without changing that piece. Thus it suffices to prove each local symbol statement for (FC2); finite partitions give the compact-manifold statements. No assertion here changes an operator outside the cutoffs without retaining its smooth remainder.

**Amplitude reduction with a finite remainder.** Put $F(x,z,\zeta)=A(x,x+z,\zeta)$ and Fourier transform in $z$ only:
\[
 \widehat F(x,\eta,\zeta)=\int e^{-iz\cdot\eta}F(x,z,\zeta)\,dz,
 \qquad
 c(x,\xi)=(2\pi)^{-n}\int
          \widehat F(x,\eta,\xi+\eta)\,d\eta.
 \tag{FC3}
\]
All these last integrals are ordinary absolutely convergent integrals. In fact, integration by parts in the compact $z$ support gives, for every integer $L\ge0$,
\[
 |\partial_x^\alpha\partial_\zeta^\beta
        \widehat F(x,\eta,\zeta)|
 \le C_{\alpha\beta L}\langle\eta\rangle^{-2L}
                      \langle\zeta\rangle^{m-|\beta|}.
 \tag{FC4}
\]
Here differentiating $x$ differentiates both position arguments of $A$, which preserves (FC2). Apply (FC1) with $r=m-|\beta|$ and choose $2L>n+|r|$. It proves every $S^m$ bound on $c$, justifies differentiation under the integral and shows that each requested seminorm uses only finitely many seminorms in (FC2).

The operator with amplitude $A$ is exactly $\operatorname{Op}(c)$. To verify this, apply it to $y\mapsto e^{iy\cdot\xi}$, which is allowed by compact input support. Set $y=x+z$ and $\zeta=\xi+\eta$ in the iterated integral, first integrating in $z$. Equations (FC3)–(FC4) give $e^{ix\cdot\xi}c(x,\xi)$. A general Schwartz input is its inverse Fourier integral. That integral and its derivatives converge in every input $C^k$ seminorm on the compact support. The continuity just proved permits the operator to pass under it, giving the left formula. The same identities hold on distributions by transposition. The left symbol is unique: take Schwartz inputs with transforms $(2\pi)^n\varepsilon^{-n}\rho((\xi-\xi_0)/\varepsilon)$, where $\rho$ is compactly supported and has integral one. Their outputs at a fixed $x$ tend to $e^{ix\xi_0}c(x,\xi_0)$ by substitution and continuity. Equality of operators therefore implies equality of symbols.

Taylor expansion in the **third** argument of $\widehat F(x,\eta,\xi+\eta)$ yields
\[
 c(x,\xi)=\left.
    \sum_{|\alpha|<N}\frac{\partial_\xi^\alpha D_y^\alpha
                                  A(x,y,\xi)}{\alpha!}
                 \right|_{y=x}+R_N(x,\xi),
 \qquad R_N\in S^{m-N}_{1,0}.
 \tag{FC5}
\]
For explicitness the error is
\[
 R_N=\frac{N}{(2\pi)^n}\sum_{|\alpha|=N}\frac1{\alpha!}
   \int_0^1(1-t)^{N-1}\int \eta^\alpha
      \partial_\zeta^\alpha\widehat F(x,\eta,\xi+t\eta)
                  \,d\eta\,dt.
 \tag{FC6}
\]
After $\partial_x^\gamma\partial_\xi^\beta$, (FC4) and (FC1) bound its integrand by
$C\langle\xi\rangle^{m-N-|\beta|}
\langle\eta\rangle^{N+|m-N-|\beta||-2L}$.
Choose $2L>n+N+|m-N-|\beta||$. This proves the asserted error, differentiation and finite-seminorm bound, uniformly in $t$. In a polynomial term Fourier inversion gives
$(2\pi)^{-n}\int\eta^\alpha\widehat F(x,\eta,\xi)\,d\eta
=D_z^\alpha F(x,0,\xi)$.
It proves the sign and every coefficient in (FC5), without any assumption about convergence of an infinite expansion.

**Ordered product.** We first work with left symbols $a,b$ compactly supported in $x$, of orders $m_1,m_2$. Their left operators send Schwartz functions continuously to compact smooth functions: differentiate the absolutely convergent frequency formula, using the rapid decay of the input Fourier transform. Define
\[
 \widehat b_x(\eta,\xi)
       =\int e^{-iz\eta}b(x+z,\xi)\,dz,
 \qquad c(x,\xi)=(2\pi)^{-n}\int
             a(x,\xi+\eta)\widehat b_x(\eta,\xi)\,d\eta.
 \tag{FC7}
\]
For $x$ in the compact support of $a$, the $z$ supports are uniformly compact. Thus $\widehat b_x$ and its derivatives satisfy (FC4) with order $m_2$. Estimate the derivatives of $a(x,\xi+\eta)$ by (FC1). For a split $\beta=\beta_1+\beta_2$ of frequency derivatives, the integrable bound has factor
$\langle\xi\rangle^{m_1-|\beta_1|+m_2-|\beta_2|}$
times $\langle\eta\rangle^{|m_1-|\beta_1||-2L}$.
This proves $c\in S^{m_1+m_2}$ with finite-seminorm control.

For the exact operator identity, write $Bu$ by its absolutely convergent frequency formula, Fourier transform its compact smooth output, and apply $A$. Fubini is legitimate after the preceding $z$ integration: arbitrary decay of $\widehat b_x$ in $\eta$ and of $\widehat u$ in $\xi$ dominates the fixed symbol powers, including any prescribed output derivatives. The phase substitution gives precisely (FC7). Hence $AB=\operatorname{Op}(c)$. Equivalently the identity follows first with bounded frequency cutoffs and then by those same integrable majorants. The localizations already explained give this identity for general properly supported local symbols, retaining their smooth errors.

Expand $a(x,\xi+\eta)$ in $\eta$. In each finite term Fourier inversion on $b(x+z,\xi)$ gives $D_x^\alpha b(x,\xi)$. The remainder is
\[
 \frac{N}{(2\pi)^n}\sum_{|\alpha|=N}\frac1{\alpha!}
 \int_0^1(1-t)^{N-1}\int
     \eta^\alpha(\partial_\xi^\alpha a)(x,\xi+t\eta)
                      \widehat b_x(\eta,\xi)\,d\eta\,dt.
 \tag{FC8}
\]
The derivative estimate just given, with $m_1$ replaced by $m_1-N$ and the additional factor $\langle\eta\rangle^N$, proves that it has order $m_1+m_2-N$. Thus, for every positive integer $N$,
\[
 c-\sum_{|\alpha|<N}\frac{1}{\alpha!}
       (\partial_\xi^\alpha a)(D_x^\alpha b)
 \in S^{m_1+m_2-N}_{1,0}.
 \tag{1}
\]
**Adjoint.** Conjugating the kernel and exchanging $x,y$ gives the amplitude $\overline{a(y,\xi)}$. Insert the actual proper-support cutoffs before the compact-local calculation. Formula (FC5) applied to this amplitude gives
\[
 a^*-\sum_{|\alpha|<N}\frac{1}{\alpha!}
       \partial_\xi^\alpha D_x^\alpha\overline a
 \in S^{m-N}_{1,0}.
 \tag{2}
\]
It is the exact formal adjoint identity on compact smooth inputs and by duality on distributions; for bounded $L^2$ realizations density gives the Hilbert adjoint. No unexamined domain equality for an unbounded realization is being asserted. As a sign check, the symbol $x_j\xi_j$ has adjoint $x_j\xi_j-i$, agreeing with $D_jx_j=x_jD_j-i$. Equation (FC6) supplies every remainder seminorm in (2).

A compact smooth kernel has a rapidly decreasing left symbol: write its left symbol as $\int e^{-i(x-y)\xi}K(x,y)\,dy$ and integrate any number of derivatives in $y$; factors produced by position and frequency differentiation remain compact smooth. Conversely, an $S^{-\infty}$ amplitude has a smooth kernel by absolute frequency integration after all derivatives. The statements extend under proper localization. In particular changing a diagonal cutoff changes the operator only by the retained smooth kernel and the local symbol only by $S^{-\infty}$.

<a id="scalar-coordinate-change"></a>

## Coordinate changes and the scalar subprincipal symbol

Write old coordinates as $x=\kappa(X)$, let $J(X)=D\kappa(X)$ and $j(X)=|\det J(X)|$. On half densities the coordinate map on coefficients is
$u\mapsto j(X)^{1/2}u(\kappa(X))$.
The change-of-variables theorem cited above shows that it preserves the local $L^2$ norm. The transformed kernel is
$j(X)^{1/2}j(Y)^{1/2}K(\kappa(X),\kappa(Y))$.
On a small convex coordinate neighborhood set
\[
 H(X,Y)=\int_0^1D\kappa\bigl(Y+t(X-Y)\bigr)\,dt.
 \tag{FC9}
\]
The fundamental theorem gives $\kappa(X)-\kappa(Y)=H(X,Y)(X-Y)$, and $H(X,X)=J(X)$. Invertibility of $J$ and continuity make $H$ invertible on a neighborhood of the compact diagonal piece. The part of the kernel outside that neighborhood is smooth by the off-diagonal argument. In the remaining part change frequencies by $\eta=H(X,Y)^T\xi$. Its exact amplitude is
\[
 \widetilde A(X,Y,\eta)=q(X,Y)
 A\bigl(\kappa(X),\kappa(Y),H(X,Y)^{-T}\eta\bigr),
 \qquad
 q(X,Y)=\frac{j(X)^{1/2}j(Y)^{1/2}}{|\det H(X,Y)|}.
 \tag{FC10}
\]
The cutoff distribution definition justifies the substitution first with finite frequency integrals and then in their limits. Indeed differentiating the transformed cutoff has the same uniform order bounds as before, since $H,H^{-1}$ and their derivatives are bounded on the fixed compact set.

Here $\langle H^{-T}\eta\rangle$ is bounded above and below by fixed multiples of $\langle\eta\rangle$. A position derivative falling on $H^{-T}\eta$ contributes one frequency factor and one frequency derivative of $A$, whose orders cancel. A frequency derivative lowers the order by one. Repeated product and chain rules therefore prove every estimate (FC2) for $\widetilde A$, with finitely many seminorms of $A$ and of the fixed coordinate map. Applying (FC5) gives the **entire finite coordinate expansion** and its $S^{m-N}$ remainder:
\[
 \widetilde a(X,\eta)-
  \left.\sum_{|\alpha|<N}\frac{
           \partial_\eta^\alpha D_Y^\alpha
                    \widetilde A(X,Y,\eta)}{\alpha!}\right|_{Y=X}
     \in S^{m-N}_{1,0}.
 \tag{FC11}
\]
Since $q(X,X)=1$, the principal symbol transforms by
$\widetilde a_m(X,\eta)=a_m(\kappa(X),J(X)^{-T}\eta)$.
This also proves preservation of classical symbols: each homogeneous amplitude term is still homogeneous in the new frequency, each frequency derivative lowers its degree by one, and (FC11) has arbitrarily low finite errors. Products and adjoints preserve classical symbols by the same argument using (1)–(2).

Here are the next-degree terms, including the half-density factor. For a classical scalar symbol define
\[
 a_{\mathrm{sub}}=a_{m-1}
       -\frac1{2i}\sum_k\partial_{x_k}\partial_{\xi_k}a_m,
 \qquad
 \{a,b\}=\sum_k(\partial_{\xi_k}a\,\partial_{x_k}b
                   -\partial_{x_k}a\,\partial_{\xi_k}b).
 \tag{FC12}
\]
Put $T(X)=J(X)^{-T}$. Directly differentiating (FC9) on the diagonal gives
$\partial_{Y_l}H|_{Y=X}=\tfrac12\partial_{X_l}J$.
The derivative of a determinant is
$\partial\det J=\det J\operatorname{tr}(J^{-1}\partial J)$:
this follows by multilinearity in its columns, or by expanding
$\det(I+\varepsilon B)=1+\varepsilon\operatorname{tr}B+O(\varepsilon^2)$.
Consequently $\partial_{Y_l}q|_{Y=X}=0$ and
$\partial_{Y_l}H^{-T}|_{Y=X}=\tfrac12\partial_{X_l}T$.
Apply (FC11) through degree $m-1$ to the left amplitude $a(\kappa(X),H^{-T}\eta)q$. It yields
\[
 \widetilde a_{m-1}=a_{m-1}(\kappa(X),T\eta)
  +\frac1{2i}\sum_l\partial_{\eta_l}
       \left[\partial_\xi a_m(\kappa(X),T\eta)
                          \cdot(\partial_{X_l}T)\eta\right].
 \tag{FC13}
\]
The chain rule and $JT^T=I$ also give
\[
 \sum_l\partial_{X_l}\partial_{\eta_l}\widetilde a_m
   =\left(\sum_k\partial_{x_k}\partial_{\xi_k}a_m\right)
                       (\kappa(X),T\eta)
    +\sum_l\partial_{\eta_l}
       \left[\partial_\xi a_m(\kappa(X),T\eta)
                          \cdot(\partial_{X_l}T)\eta\right].
 \tag{FC14}
\]
Subtracting $(2i)^{-1}$ times (FC14) from (FC13) proves that $a_{\mathrm{sub}}$ transforms as a scalar. Thus it is intrinsic on scalar half densities, with the exact convention in (FC12). Formula (1) and the product rule now give
\[
 (AB)_{\mathrm{sub}}=a_{\mathrm{sub}}b_{m_2}
       +a_{m_1}b_{\mathrm{sub}}+\frac1{2i}\{a_{m_1},b_{m_2}\},
 \qquad (A^*)_{\mathrm{sub}}=\overline{a_{\mathrm{sub}}}.
 \tag{FC15}
\]
For the first identity, expand the second derivative of $a_{m_1}b_{m_2}$ in (FC12); its two cross terms combine with the $1/i$ term in (1) to give the displayed bracket. For the second, use (2) and conjugate $1/i$. In particular $[A,B]$ has order at most $m_1+m_2-1$ and principal symbol $(1/i)\{a_{m_1},b_{m_2}\}$. A finite partition patches the finite calculus and these intrinsic symbols on a closed manifold. These arguments concern scalar pseudodifferential operators; graph-FIO composition requires the additional proof identified below.

<a id="scalar-classical-summation"></a>

## Classical summation

Let $a_j\in S^{m-j}_{1,0}$, $j\geq0$, on one patch, with their $x$ support in one fixed compact set when support is needed. There is $a\in S^m_{1,0}$ such that
\[
 a-\sum_{j<N}a_j\in S^{m-N}_{1,0}\qquad(N\geq1).
 \tag{3}
\]
Choose a smooth $\chi(\xi)$ equal to zero for $|\xi|\leq1$ and one for $|\xi|\geq2$. For a symbol $b$ write
\[
 p_{k,L}(b)=\max_{|\alpha|+|\beta|\leq L}
 \sup_{x,\xi}\langle\xi\rangle^{-m+k+|\beta|}
       |\partial_x^\alpha\partial_\xi^\beta b(x,\xi)|.
\]
Local compact $x$ sets can instead be included in this notation. For $j>k$, the product rule and support of $\chi(\xi/R)$ imply
\[
 p_{k,L}\bigl(\chi(\xi/R)a_j\bigr)
 \leq C_{j,k,L}R^{k-j}\quad(R\geq1).
 \tag{4}
\]
For derivatives falling on $\chi$ this follows on $R\leq|\xi|\leq2R$ from their factor $R^{-|\gamma|}$; for all other terms it follows on $|\xi|\geq R$ from $k-j<0$. Choose an increasing sequence $R_j\to\infty$ such that, for each $j\geq1$, (4) is at most $2^{-j}$ for every $k<j$ and $L\leq j$. There are finitely many such conditions for one $j$, so the choice is possible. Set
\[
 a=a_0+\sum_{j\geq1}\chi(\xi/R_j)a_j.
\]
This is a locally finite smooth sum, because on a bounded $\xi$ set all sufficiently large summands vanish. For a fixed derivative order $L$, the tail with $j>\max(L,k)$ has summable $p_{k,L}$ bounds. Finitely many earlier terms have their required symbol bounds. Taking $k=0$ proves $a\in S^m$. For (3), the finitely many differences $(\chi(\xi/R_j)-1)a_j$, $1\leq j<N$, have compact frequency support and therefore belong to $S^{-\infty}$; the tail $j\geq N$ belongs to $S^{m-N}$ by the same bounds with $k=N$, separating its finitely many initial indices. This proves every seminorm of (3). Exhausting noncompact $x$ patches by compact sets and including the first $j$ sets in the finite choice proves the local version. The construction does not enlarge the $x$ support. Homogeneous input terms, cut off near zero, therefore have a classical realization with exactly their prescribed expansion.

These assertions include smooth parameter families. Suppose every parameter derivative of $a_j(t,x,\xi)$ belongs to $S^{m-j}$ with seminorms locally uniform in the finite-dimensional parameter $t$. Include the first $j$ parameter-compact sets and all parameter derivatives of order at most $j$ among the finitely many conditions choosing $R_j$. Choose each radius independently of $t$. The same summable estimates then hold locally uniformly in $t$ for every derivative, so the sum is smooth as a symbol-valued function and every differentiated error in (3) has order $m-N$. The local finiteness also proves ordinary joint smoothness. For finite products, adjoints and coordinate changes, apply parameter derivatives directly in (FC3), (FC6), (FC7) and (FC10), assuming the same locally uniform symbol-family bounds on their inputs. The product rule gives finitely many of the already bounded integrals; compact parameter sets keep the coordinate inverse bounds uniform. Dominated convergence proves smooth parameter dependence and the finite-seminorm remainder bounds for every such derivative. Thus differentiating the families used below requires no separate formal-series convergence assumption.

<a id="scalar-real-sobolev"></a>

## Real Sobolev mapping

For every real $s,m$, a properly supported scalar classical operator $A$ of order $m$ maps
\[
 A:H^s_{\rm comp}\longrightarrow H^{s-m}_{\rm loc}.
 \tag{5}
\]
On a closed manifold it is bounded $H^s\to H^{s-m}$. The proof uses $J^t=\langle D\rangle^t$, whose Fourier multiplier symbol is $\langle\xi\rangle^t\in S^t_{1,0}$ for every real $t$. On Euclidean space, define $H^t$ as the tempered distributions whose Fourier transform is a function with finite norm
\[
 \|u\|_{H^t}^2
 =(2\pi)^{-n}\int\langle\xi\rangle^{2t}|\widehat u(\xi)|^2\,d\xi
 =\|J^tu\|_2^2.
\]
Multiplication by $\langle\xi\rangle^{\pm t}$ preserves Schwartz space and acts on tempered distributions by duality: every derivative of these weights has polynomial growth. The proved Fourier isometry therefore identifies $J^t:H^t\to L^2$ as an isometric bijection with inverse $J^{-t}$; in particular $H^t$ is complete. Weighted Fourier Cauchy–Schwarz gives, for a compact smooth test $\phi$,
\[
 |\langle u,\phi\rangle|
 =\left|(2\pi)^{-n}\int\widehat u(\xi)\widehat\phi(-\xi)\,d\xi\right|
 \leq\|u\|_{H^t}\|\phi\|_{H^{-t}}.
\]
The distributional pairing here is linear in its test. The equality follows from the proved distributional Fourier inverse and the absolutely integrable weighted product. It proves the distributional convergence and local dual bound used below.

A compactly supported distribution belongs to some $H^{-r}$. Indeed, continuity on tests supported in one fixed compact neighborhood gives $|\langle u,\phi\rangle|\le C\max_{|\alpha|\le N}\|\partial^\alpha\phi\|_\infty$ there for some finite $N$. To obtain this bound directly, take a basic zero-neighborhood on which the functional is bounded, containing finitely many such derivative constraints, and rescale each test into it. For a cutoff $\theta=1$ near the support of $u$, apply the bound to $\theta(x)e^{-ix\cdot\xi}$. Its Fourier transform is therefore a smooth function bounded by $C'\langle\xi\rangle^N$; difference quotients and all frequency derivatives follow by continuity on that same test space. The polar integration proof makes $\langle\xi\rangle^{-r}\widehat u$ square integrable when $r>N+n/2$. This also shows that every distribution on a compact manifold belongs to a sufficiently negative Sobolev space after finite localization.

First insert compact coordinate cutoffs on the input and output. Formula (1) and its finite remainders show that
\[
 B=J^{s-m}AJ^{-s}
\]
has order zero, up to a smoothing operator. Although the Fourier multipliers need not be properly supported, this use of the local product theorem is justified by cutting their kernels to a small neighborhood of the diagonal and choosing nested compact cutoffs around the actual input and output supports. Off that diagonal repeated $\xi$ integrations by parts make the kernels smooth. For every fixed mixed derivative and every $M$, enough integrations make the differentiated symbol integrable and bound the tail by $C_M\langle x-y\rangle^{-M}$. After a compact cutoff in the input variable, this is a Schwartz kernel in the two variables; after a compact cutoff in the output variable the same conclusion follows with the variables interchanged. These tails need not have compact support in both variables, but their derivatives have the stated rapid bounds. Their two-variable Fourier transforms are rapidly decreasing. Weighting by any fixed powers of the two frequencies remains square integrable, so Cauchy–Schwarz proves boundedness between any two real Sobolev spaces. The nested local terms use (1); their compact smooth remainders satisfy the same bound. Composing a tail with a properly supported finite-order operator preserves these estimates by its distributional and smooth symbol action. This accounts for the global tails and proves the asserted remainder bound.

The zero-order left symbol and all its derivatives required by the local finite-derivative theorem are bounded: its symbol estimates give $\langle\xi\rangle^{-|\beta|}\leq1$. That theorem therefore proves $\|Bv\|_2\leq C\|v\|_2$. Taking $v=J^su$ proves (5) initially on smooth inputs. Here is the required density for arbitrary real $s$: the multiplier $J^{-s}$ preserves Schwartz space, since all derivatives of $\langle\xi\rangle^{-s}$ have polynomial growth. Apply it to Schwartz approximations of $J^su$ in $L^2$, whose density was proved in the Fourier provider. They converge to $u$ in $H^s$. This extends the localized map to $H^s$. The extension agrees with the distributional action, because Fourier Cauchy–Schwarz implies that $H^s$ convergence is distributional and the properly supported kernel acts continuously on distributions. Multiplication by a compact smooth cutoff is the order-zero case just proved; multiplying the approximations by one equal to one near a given compact support also proves the required compact smooth density on that support neighborhood.

To justify reassembling different charts at real indices, let $V$ be a half-density coordinate change multiplied by fixed compact input and output cutoffs. It and its adjoint send compact smooth functions to compact smooth functions. The finite coordinate theorem (FC10)–(FC11), with the same diagonal localization for $J^{2s}$, makes $V^*J^{2s}V$ pseudodifferential of order $2s$ plus a smooth remainder. The already proved finite product and order-zero bound make $C=J^{-s}V^*J^{2s}VJ^{-s}$ bounded on $L^2$. For smooth inputs the change-of-variables identity and Fourier Plancherel give
\[
 \|Vu\|_{H^s}^2
   =(V^*J^{2s}Vu,u)=(CJ^su,J^su)
   \le\|C\|\,\|u\|_{H^s}^2.
 \tag{FC16}
\]
The Fourier multipliers and cutoffs are legitimate by the explicit smooth-tail estimates above. Density now proves boundedness of each localized coordinate change on every real $H^s$. Apply the inverse coordinate change for the reverse local comparison. Thus finite atlas norms agree up to constants. To see completeness and smooth density globally, map a distribution to the finite list of its partitioned coordinate representatives, each in its complete Fourier $H^s$ space. Reassemble a list by multiplying its $i$th representative by a cutoff equal to one near the support of the $i$th partition function, changing coordinates back and summing. This map is bounded by (FC16) and is a left inverse of localization, since the partition sums to one. Reassembly followed by localization is therefore a bounded projection onto the lists coming from one global distribution. That range is closed, hence complete. Approximate its entries by compact smooth functions and reassemble to obtain global smooth approximations. This proves the closed-manifold assertion of (5), including its actual Sobolev spaces. Constants for a bounded family depend on finitely many symbol seminorms by (1) and the finite-derivative theorem.

<a id="two-endpoint-sobolev"></a>

### Two-endpoint Sobolev bounds

The following proof applies to any compatible linear operator, without a symbol or a fractional-power construction. Suppose $a<b$ and $T:H^a(\mathbb R^n)\to H^a(\mathbb R^n)$ is bounded, with its restriction to $H^b$ bounded into $H^b$. For every $a<s<b$ it is bounded on $H^s$, with a bound depending only on the two endpoint norms and $a,b,s$. A family with uniform endpoint bounds has a uniform intermediate bound.

Let $\Pi_j$, $j\ge0$, be the orthogonal Fourier projections onto the disjoint measurable annuli $2^j\le\langle\xi\rangle<2^{j+1}$. Plancherel proves, for every real $t$,
\[
 2^{-2|t|}\sum_{j\ge0}2^{2tj}\|\Pi_j u\|_2^2
 \le \|u\|_{H^t}^2
 \le 2^{2|t|}\sum_{j\ge0}2^{2tj}\|\Pi_j u\|_2^2.
 \tag{FC18}
\]
The projections have norm at most one on every Fourier $H^t$. A single finite annular band of an $L^2$ function belongs to every $H^t$. Applying the endpoint bound at $t=a$ or $t=b$, followed by (FC18) on its input and output bands, gives
\[
 \|\Pi_jT\Pi_k\|_{2\to2}
 \le 2^{2|t|}\|T\|_{H^t\to H^t}\,2^{t(k-j)}
 \qquad(t=a,b).
\]
For a finite sum of input bands put $v_k=2^{sk}\|\Pi_k u\|_2$ and extend this sequence by zero to $k<0$. The triangle inequality and the smaller of the two endpoint bounds imply
\[
 2^{sj}\|\Pi_jTu\|_2\le C\sum_{k\ge0}h_{j-k}v_k,
 \qquad
 h_\ell=\begin{cases}
 2^{-(b-s)\ell},&\ell\ge0,\\
 2^{(s-a)\ell},&\ell<0.
 \end{cases}
 \tag{FC19}
\]
Here $C$ is the larger of the two displayed endpoint constants. Both tails of $h$ are geometric and $H=\sum_{\ell\in\mathbb Z}h_\ell<\infty$. Weighted Cauchy–Schwarz gives $(\sum_k h_{j-k}v_k)^2\le H\sum_k h_{j-k}v_k^2$. Summing in $j$, and interchanging nonnegative sums, proves $\sum_j(\sum_k h_{j-k}v_k)^2\le H^2\sum_kv_k^2$. Equation (FC18) therefore gives the asserted $H^s$ bound. Truncating the annular decomposition approximates every $H^s$ input in $H^s$ and also in $H^a$, because $s>a$. The output limit in $H^s$ agrees with its already defined $H^a$ image. This proves the extension and its compatibility, including negative endpoint indices.

For a closed manifold, use the finite-atlas localization $L$ and reassembly $R$ constructed immediately after (FC16). These same maps are bounded at every real index and satisfy $RL=I$. The operator $LTR$ on the finite direct sum of Euclidean spaces has the two endpoint bounds. Apply the proof above with $\Pi_j$ acting componentwise and the direct-sum $L^2$ norm in place of the scalar norm; every estimate and the weighted sequence argument are unchanged. Reassembling its intermediate bound proves $T=R(LTR)L:H^s(X)\to H^s(X)$. The localization constants are fixed independently of $T$, so the uniform-family assertion also holds on the manifold. In particular compatible bounds at all integer indices imply bounds at every real index.

<a id="scalar-elliptic-domains"></a>

## Elliptic parametrix domains

Let $P$ be a classical scalar elliptic operator of real order $m$ on a closed manifold. Its principal symbol $p_m$ is nonzero off the zero section. On each compact coordinate piece, its absolute value is bounded below by $c|\xi|^m$ at large frequency, since its homogeneous restriction to the unit sphere has a positive minimum. Repeated differentiation of $p_m(1/p_m)=1$ proves all symbol estimates of order $-m$ for the cut-off reciprocal. The coordinate transformation just proved makes its leading symbol intrinsic. Choose a partition $\chi_i$ and cutoffs $\theta_i=1$ near $\operatorname{supp}\chi_i$. The finite sum $Q_0=\sum_i\chi_i\operatorname{Op}(q_{-m,i})\theta_i$ has principal symbol $1/p_m$, so $R_0=I-PQ_0$ has order $-1$ by (1).

There is a global classical $Q$ with $Q\sim\sum_{j\ge0}Q_0R_0^j$, where the $j$th summand has order $-m-j$. To construct it, write each summand as $\sum_i\chi_i(Q_0R_0^j)\theta_i$ plus a smooth kernel; the difference is smooth because $1-\theta_i$ is separated from $\operatorname{supp}\chi_i$. Apply the already proved cutoff summation to the left symbols on each fixed chart and then sum the finitely many properly localized operators. For every finite $N$ the difference from $\sum_{j<N}Q_0R_0^j$ has order $-m-N$; the finitely many omitted smooth kernels do not change that assertion. Therefore
\[
 PQ-I=-R_0^N+P\left(Q-\sum_{j<N}Q_0R_0^j\right)
             \quad\hbox{has order }-N\quad\hbox{for every }N.
 \tag{FC17}
\]
Its local symbols lie in $S^{-\infty}$ and its kernel is smooth by the finite-calculus result above. Thus $PQ=I-R$ with $R$ smoothing. This global construction also explains the usual coefficient recursion: at degree $-j$, (1) gives $p_mq_{-m-j}$ plus known earlier coefficients, which are canceled by division by $p_m$.

Construct a left inverse $Q_L$ by the same recursion for $Q_LP$. If $Q_LP=I-S$, comparison gives
\[
 Q_L-Q=Q_LR-SQ.
\]
Both right-hand compositions are smoothing: a properly supported finite-order operator sends smooth functions continuously to smooth functions, and its distributional adjoint has the same property for the smooth-kernel composition in the other variable. Hence $QP=I-S'$ for a smoothing $S'$. This proves a two-sided parametrix without assuming convergence of an infinite formal operator expansion.

If $u$ is a distribution and $Pu\in H^{s-m}$, then
\[
 u=QPu+S'u\in H^s.
 \tag{6}
\]
A compactly supported distribution has finite order on each chart, and pairing it with the smooth kernel of $S'$ gives a smooth output. The finite partition makes this global. The mapping proof gives, for every fixed real $t$ and $u\in H^t$,
\[
 \|u\|_{H^s}\leq C_{s,t}
       \bigl(\|Pu\|_{H^{s-m}}+\|u\|_{H^t}\bigr).
 \tag{7}
\]
In particular, if $m>0$ and $P$ is formally symmetric, its densely defined realization on $H^m\subset L^2$ is self-adjoint with that exact domain. Symmetry follows by the smooth integration-by-parts identity and density, using (5). A vector $u\in D(P^*)$ satisfies $Pu=P^*u\in L^2$ distributionally, as testing against smooth inputs shows. Formula (6) with $s=m$ puts it in $H^m$. Conversely every $H^m$ vector has that adjoint identity by (5) and density. Thus $D(P^*)=H^m=D(P)$ and the operator is self-adjoint. Estimate (7), with $s=m,t=0$, identifies its graph norm with the $H^m$ norm. No boundary domain or positivity assertion is included in this statement.

Repeated use of (6) gives the smooth-kernel correspondence needed in AN06: a smoothing parametrix remainder improves every Sobolev index, and a kernel already smooth on a compact coordinate product has the rapid two-frequency estimate used above. Conversely, suppose the localized operator $A$ maps $H^{-r}$ continuously to $H^\ell$ for every $r,\ell$. For each input multi-index $\alpha$ and nonnegative integer $k$, the map $y\mapsto\partial_y^\alpha\delta_y$ is $C^k$ into $H^{-r}$ when $r>n/2+|\alpha|+k$. Its Fourier transform is a fixed polynomial of degree $|\alpha|$ times $e^{-iy\cdot\xi}$; differentiation in $y$ adds at most $k$ frequency factors, and the integrable squared weight proves the assertion by Fourier dominated convergence, including difference quotients. Applying $A:H^{-r}\to H^\ell$ preserves this $C^k$ dependence. If $\ell>n/2+|\beta|+k$, Fourier Cauchy–Schwarz gives continuous evaluation of all output derivatives through the required order. Consequently $K(x,y)=(A\delta_y)(x)$ has every mixed input and output derivative jointly continuous. Integrating this identity against a compact smooth input recovers $A$ on that input, first in a negative Sobolev space and then in $H^\ell$, so $K$ is its actual kernel. This proves the converse without assuming joint regularity from separate evaluations or an undeveloped adjoint argument.

## Graph Sobolev mapping and ordered Egorov

Read the finite scalar sections above first, followed by [Phase geometry, stationary phase and the Maslov symbol](phase-geometry-and-stationary-phase.md#phase-foundations) and then [Transverse composition and graph operators](transverse-composition-and-graph-operators.md#transverse-composition). Sections 1–7 of the latter give the actual operator-kernel product, the transverse matching rank proof, all incomparable-frequency tails, the critical-density contraction and the exact Maslov and adjoint factors. They use properly supported classical scalar kernels and unique matching, with no positive-excess assertion or restriction excluding base caustics.

For a graph FIO of order $m$, [Section 8, (G15)–(G16)](transverse-composition-and-graph-operators.md#graph-sobolev), proves $A:H^s_{\rm comp}\to H^{s-m}_{\rm loc}$ for every real $s$. It conjugates with the actual Fourier Sobolev multipliers, accounts for their smooth tails, applies the proved graph product to $B^*B$, and then uses the finite scalar order-zero bound and smooth density. The finite-atlas reassembly above supplies the closed-manifold statement. For parameter families the undifferentiated bounds are locally uniform; differentiating a moving phase can raise the operator order and is explicitly accounted for there.

[Section 9, (G17)](transverse-composition-and-graph-operators.md#graph-egorov), proves the elliptic inverse modulo smooth kernels and the ordered Egorov rule. For a unitary order-zero graph FIO $E$ with canonical graph $\chi$ and a scalar $V\in\Psi^r_{\rm cl}$, the operator $E^*VE$ is in $\Psi^r_{\rm cl}$ with principal symbol $v\circ\chi$. The line and density factors cancel by the actual identity $E^*E=I$. When the composed graph is the fixed identity, the same proof gives a smooth classical symbol family with all parameter derivatives of order $r$. Thus the convention for $E(t)=e^{-itL}$ is $e^{itL}Ve^{-itL}$ with $v\circ\chi_t$. The wave construction also uses [Scalar transport and phase action](scalar-transport-and-phase-action.md) and [Wavefront-qualified pullback](wavefront-qualified-pullback.md).

## Compact Sobolev inclusion

For all real $s>t$, $H^s\hookrightarrow H^t$ is compact. Here is a proof covering the real indices used above. Localize a bounded sequence in $H^s$ to a fixed compact coordinate set. For a common cutoff $\theta$ equal to one on that set,
\[
 \partial_\xi^\alpha\widehat u(\xi)
   =\langle u,(-ix)^\alpha\theta(x)e^{-ix\cdot\xi}\rangle
\]
up to the fixed Fourier normalization. Sobolev duality bounds this uniformly on every bounded frequency ball by the $H^s$ norm of $u$ times the $H^{-s}$ norm of the displayed compact smooth test function. Those test norms and their first frequency derivatives are uniformly bounded on the ball. The restricted Fourier transforms are therefore uniformly bounded and equicontinuous there. Finite nets on the ball, convergent subsequences at their countably many chosen net points, and the common continuity bound produce a subsequence converging uniformly on every frequency ball. This is the elementary diagonal proof of the needed compactness step.

The high-frequency tail has the uniform bound
\[
 (2\pi)^{-n}\int_{|\xi|>R}\langle\xi\rangle^{2t}|\widehat u(\xi)|^2\,d\xi
 \leq\langle R\rangle^{2(t-s)}\|u\|_{H^s}^2\longrightarrow0.
\]
Uniform convergence on the frequency ball and this tail estimate make the selected subsequence Cauchy in $H^t$. Completeness gives its limit. Successive selections over the finite atlas give one globally convergent subsequence. This proves compactness for the stated real indices.

Together with (7), the closed-manifold elliptic map $P:H^s\to H^{s-m}$ is Fredholm. The remainders in $QP=I-S'$ and $PQ=I-R$ are compact on the corresponding spaces, because a smoothing operator factors through a higher Sobolev space. On $\ker P$ the identity equals the compact operator $S'$, so the unit ball is relatively compact and the Riesz-lemma proof in [Compact Fredholm operators and strongly continuous families](compact-fredholm-families.md#compact-fredholm) gives a finite-dimensional kernel. Choose its bounded finite-dimensional projection and a closed complement. If no lower bound for $P$ held on that complement, unit vectors $u_j$ there with $Pu_j\to0$ would satisfy $u_j=QPu_j+S'u_j$ and hence have a convergent subsequence. Its limit would be a unit vector in both the complement and the kernel, a contradiction. This lower bound proves closed range. Applying the same compact-identity argument to $Q^*P^*=I-R^*$ makes the annihilator of that range finite-dimensional. Hahn–Banach identifies the dual of the quotient with this annihilator, so the quotient is finite-dimensional by the full elementary argument in the compact-Fredholm reading. Thus both defects are finite; no zero-index conclusion for every elliptic operator is asserted. For a bijective positive-order realization, take $s=m$. Its kernel is zero, so the complement is all of $H^m$ and the just-proved lower bound gives $\|u\|_{H^m}\le C\|Pu\|_2$. Hence its inverse $L^2\to H^m$ is bounded, and compact as a map $L^2\to L^2$ by the inclusion above. The positive eigenbasis and exact moment domains are proved in [Compact positive inverses and diagonal domains](compact-spectrum-domains.md#compact-inverse-domains).

## References

- Lars Hörmander, [“Fourier integral operators I”](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392052), *Acta Mathematica* 127 (1971), 79–183, Section 2.1: Theorem 2.1.1 and (2.1.4), transpose (2.1.6), ordered product (2.1.9), and Theorem 2.1.2, Proposition 2.1.3 and (2.1.11)–(2.1.17) for coordinate changes.

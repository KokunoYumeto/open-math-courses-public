# Derivative sequences and microlocal regularity

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Ordinary wavefront detects failure of smoothness. Analytic wavefront detects failure of analytic regularity. Between them, a derivative sequence can prescribe the growth allowed for each derivative order. Its wavefront set needs estimates at every order with a common constant. Smooth convergence alone does not preserve this stronger information.

Basic references are [Analytic directions of holomorphic boundary values][A] for controlled cutoffs, [Pulling back and combining analytic singularities][P] for the complete smooth constructions and analytic phase estimates, and [Gaussian packets and homogeneous Fourier directions][G] for the inverse heat expansion, full packet rotation and origin terms. Boman [B] gives background on derivative-weight wavefront sets. We specify the sequence convention here and supply the required localization, packet and Fourier-interchange proofs. [Cauchy bounds, root counts and analytic extensions][C], Lemmas 1.1 and 3.1, supplies the exact coefficient estimates and local complex extensions used in the coordinate proof.

Use the Fourier convention
\[
 \widehat f(\eta)=\int e^{-iy\cdot\eta}f(y)\,dy,\qquad
 \widehat u(\phi)=u(\widehat\phi),
 \tag{1}
\]
with inverse factor \((2\pi)^{-n}\) and complex-linear pairings. The complete Schwartz estimates and inversion used below are [Schwartz functions and Fourier inversion][F].

## 1. Fixed shifts preserve a derivative weight

Let \(L=(L_k)_{k\geq0}\) be increasing and positive, with
\[
 L_0=1,\qquad k\leq L_k,\qquad L_{k+1}\leq C_L L_k
                  \quad(k\geq0).
 \tag{2}
\]
Increase \(C_L\) to at least one. Set
\[
 M_0=1,\qquad M_k=L_k^k\quad(k\geq1).
 \tag{3}
\]
On an open set \(X\), the class \(C^L(X)\) consists of the smooth functions for which every compact \(K\subset X\) admits \(A_K\geq1\) with
\[
 \sup_K|\partial^\alpha f|\leq A_K^{|\alpha|+1}M_{|\alpha|}.
 \tag{4}
\]
Complex-valued functions are allowed.

**Lemma 1.1 (fixed shifts).** For every fixed integer \(c\geq0\), there is \(D_c\geq1\) such that
\[
 M_{N+c}\leq D_c^{N+1}M_N\quad(N\geq0),\qquad
 N^N\leq M_N\quad(N\geq1).
 \tag{5}
\]

**Proof.** Iteration of (2) gives \(L_N\leq C_L^N\) and \(L_{N+c}\leq C_L^cL_N\). Consequently
\[
 L_{N+c}^{N+c}
   \leq C_L^{c(N+c)}L_N^{N+c}
   \leq C_L^{2cN+c^2}L_N^N.
 \tag{6}
\]
This includes \(N=0\) with the convention \(M_0=1\). A sufficiently large \(D_c\) proves the first bound. The second is \(N\leq L_N\) raised to its \(N\)-th power. \(\square\)

There is no assumption that \(L_N\) has polynomial growth. For example, \(L_N=C^N\), \(C\geq2\), also satisfies (2).

**Proposition 1.2 (class algebra and analytic coordinates).** The class is closed under sums, products and differentiation. If \(F:Y\to X\) is real analytic and \(f\in C^L(X)\), then \(f\circ F\in C^L(Y)\). Analytic functions belong to every class in (2).

**Proof.** On a common compact set choose the larger of the constants in (4). In a derivative of a product of total order \(N\), a term split into orders \(j,N-j\) has weight
\[
 M_jM_{N-j}\leq L_N^jL_N^{N-j}=M_N.
 \tag{7}
\]
The sum of the multi-index Leibniz coefficients is \(2^N\). It is absorbed into the exponential constant. Finite sums are easier. A further fixed derivative order uses (5); hence differentiation preserves the class.

*Reference for the complex extension and coefficient bounds:* [C], Lemmas 1.1 and 3.1.

For analytic coordinate composition, fix a compact subset of \(Y\), shrink to finitely many neighborhoods, and extend the analytic map holomorphically there. There is a uniform complex radius and a constant \(B\) for which \(|F(z)-F(y)|\leq B|z-y|\) near each real center \(y\). Its image stays in a fixed compact neighborhood of \(F(y)\) in the real domain.

For a requested order \(N\), replace \(f\) at \(F(y)\) by its finite Taylor jet
\[
 J_Nf(w)=\sum_{|\alpha|\leq N}
              \frac{\partial^\alpha f(F(y))}{\alpha!}(w-F(y))^\alpha.
 \tag{8}
\]
The derivatives of \(J_Nf(F(z))\) through order \(N\) at \(y\) equal those of the real smooth composition: this follows by the finite Taylor formula and the ordinary chain rule. The jet is a holomorphic polynomial; the whole function \(f\) has not been assumed holomorphic.

For \(|z-y|\leq r\), the order-\(j\) terms are bounded by \(A(AaBr)^j L_N^j/j!\), where \(a\) is the dimension of \(X\). Because \(L_N\geq N\), the numbers \(L_N^j/j!\) increase for \(0\leq j\leq N\). Thus, for a fixed sufficiently small radius \(r\),
\[
 |J_Nf(F(z))|
   \leq A\frac{M_N}{N!}\sum_{j=0}^N(AaBr)^j
   \leq 2A\frac{M_N}{N!}.
 \tag{9}
\]
Cauchy's estimate on a fixed polydisc bounds every derivative of total order \(N\) at \(y\) by \(2A r^{-N}M_N\), since its multi-index factorial is at most \(N!\). The finite compact cover proves (4) for the composition.

For an analytic function, uniform Cauchy estimates on a complex neighborhood of a real compact set give \(A^{N+1}N!\). Since \(N!\leq N^N\leq M_N\), it satisfies (4). \(\square\)

For \(L_N=(N+1)^s\), \(s\geq1\), this is the Gevrey class of order \(s\). Indeed
\[
 (N/e)^N\leq N!\leq N^N,\qquad
 (N+1)^N\leq eN^N\quad(N\geq1),
 \tag{10}
\]
so the weights \((N+1)^{sN}\) and \((N!)^s\) differ only by exponential constants. The lower factorial estimate is proved in [G], Lemma 2.1. At \(s=1\), (4) is equivalent to a factorial derivative estimate; the segment Taylor proof in [G], Corollary 3.2, makes it exactly the analytic class.

## 2. A single bounded sequence localizes the class

A nonzero pair \((x_0,\xi_0)\) is absent from \(\operatorname{WF}_L(u)\) if there are a common neighborhood \(U\) of \(x_0\), a cone \(\Gamma\) about \(\xi_0\), and compactly supported distributions \(w_N\), \(N\geq1\), such that:

- all supports lie in one compact set and all distributions have one common order and bound;
- \(w_N=u\) on \(U\);
- for some \(A\geq1\),
\[
 |\widehat w_N(\eta)|\leq A^{N+1}M_N(1+|\eta|)^{-N}
                           \quad(\eta\in\Gamma).
 \tag{11}
\]
Common compact order also gives a global polynomial bound \(C(1+|\eta|)^m\), independent of \(N\). These are the complete compact-distribution estimates in [F]. Writing \(|\eta|^{-N}\) instead of \((1+|\eta|)^{-N}\) gives the same notion: on \(|\eta|\geq1\) the change costs \(2^N\); on \(|\eta|\leq1\) use the common polynomial bound and \(M_N\geq1\).

The set is closed and positively conic, because its complement is described by neighborhoods and cones. Finite sums have the union upper bound: add their witnesses at the same index, intersect their common neighborhoods and take the largest constants and compact orders.

**Lemma 2.1 (ordinary and analytic comparison).**
\[
 \operatorname{WF}(u)\subseteq\operatorname{WF}_L(u)
                         \subseteq\operatorname{WF}_A(u).
 \tag{12}
\]

**Proof.** An analytic absence witness has weight \(N^N\), which is at most \(M_N\), so it also gives (11). This proves the second inclusion.

For the first, choose one fixed smooth cutoff \(b\), supported in \(U\) and equal to one near \(x_0\). For every desired Fourier power \(p\), choose a fixed index \(N\) sufficiently larger than \(p\), the common order \(m\) and the dimension. Then \(bu=bw_N\). The complete smooth Fourier convolution estimate in [P], Section 1, applies: when the input frequency remains in the smaller regular cone, (11) provides arbitrary desired inverse power; on its complement, angular separation and the rapidly decreasing transform of the fixed \(b\) absorb the common polynomial bound. Here \(A^{N+1}M_N\) is a finite constant depending on the chosen power, which is allowed in ordinary rapid decay. The same \(b\) and smaller cone work for every \(p\). Thus ordinary absence follows. \(\square\)

**Lemma 2.2 (controlled localization and class multipliers).** Suppose the witnesses in (11) are given near a point. A sequence of the form \(\chi_{N+c}u\), with a fixed common plateau and compact support, can replace them on a smaller cone, for a sufficiently large fixed \(c\). One such sequence can serve any finite list of regular cones. Multiplication by \(a\in C^L\) satisfies
\[
 \operatorname{WF}_L(au)\subseteq\operatorname{WF}_L(u).
 \tag{13}
\]
Every differential operator with \(C^L\) coefficients has the same decrease property.

**Proof.** Use the complete controlled cutoffs of [A], Lemma 1.1:
\[
 \|\partial^{\alpha+\beta}\chi_J\|_\infty
       \leq C_\beta(CJ)^{|\alpha|}
                         \quad(|\alpha|\leq J),
 \tag{14}
\]
with support and plateau fixed, and every fixed low derivative uniform in \(J\). Put \(g_J=a\chi_J\), with support inside the common agreement neighborhood of the witnesses. For \(a=1\) this will give normalization; the general case gives the multiplier.

For each fixed \(\beta\), (4), (5) and monotonicity give
\[
 \|\partial^{\alpha+\beta}a\|
    \leq C_\beta^{|\alpha|+1}M_{|\alpha|}
    \leq C_\beta^{|\alpha|+1}L_J^{|\alpha|}
                       \quad(|\alpha|\leq J)
 \tag{15}
\]
on the fixed support. A product-rule expansion with (14), using \(J\leq L_J\), therefore gives the same mixed bound for \(g_J\). Its fixed low derivatives remain uniform. In particular
\[
 \|\widehat g_J\|_1\leq C,\qquad
 |\widehat g_J(\zeta)|
       \leq C^{J+1}M_J(1+|\zeta|)^{-J-m-n-1}.
 \tag{16}
\]
The first estimate uses fixed derivatives through \(n+1\). For the second, integrate by parts through order \(J+m+n+1\); in (15) the additional \(m+n+1\) is the fixed low index \(\beta\). Thus it costs only one \(M_J\), not an extra factorial. Directional derivative expansion and the bounded support supply the constant in (16).

For \(J=N+c\), the distribution \(v_N=g_Ju=g_Jw_J\) has a common compact support and order, by the uniform low derivatives. It agrees with \(au\) on a common plateau. Its Fourier transform is
\[
 \widehat v_N(\xi)
   =(2\pi)^{-n}\int\widehat g_J(\zeta)\widehat w_J(\xi-\zeta)\,d\zeta.
 \tag{17}
\]
Choose a smaller cone and \(\delta>0\) so \(|\zeta|\leq\delta|\xi|\) leaves \(\xi-\zeta\) in the regular input cone with length at least \(d|\xi|\). The first estimate in (16) and (11) bound this part by
\(C^{J+1}M_J(1+|\xi|)^{-J}\).

On the rest, \(\eta=\xi-\zeta\) has
\(|\zeta|\geq d'(|\xi|+|\eta|)\). The second estimate in (16), together with the common polynomial bound on \(\widehat w_J\), gives an absolute integral at most
\[
 C^{J+1}M_J(1+|\xi|)^{-J}
                     \int(1+|\eta|)^{-n-1}d\eta.
 \tag{18}
\]
The integral is finite. Bounded frequencies use the common compact order and are included by increasing the exponential constant. Lemma 1.1 turns \(M_J\) into \(C^{N+1}M_N\), proving (11) for \(v_N\).

For finitely many input witnesses choose the largest compact order, intersect their agreement neighborhoods, and use the same cutoff and shift. Apply the argument in each smaller cone. It proves simultaneous localization, with a single sequence and a single maximum constant. To cover a compact set of base points and directions, first take finitely many directional witnesses at each point, shrink their common spatial neighborhoods, and then use a finite spatial cover. The controlled partition
\[
 p_{j,J}=\chi_{j,J}\prod_{i<j}(1-\chi_{i,J})
 \tag{19}
\]
has sum one on the covered plateau. Its full derivative and analytic-chart bounds are [P], Lemma 2.2; finite products retain (14). Applying the preceding localization to each spatial term and adding proves the compact-set form.

For a constant derivative, choose the input index \(J=N+|\alpha|\). The sequence \(\partial^\alpha w_J\) still has common compact support and order, agrees with \(\partial^\alpha u\), and its Fourier multiplier costs at most \((1+|\eta|)^{|\alpha|}\). Lemma 1.1 absorbs the fixed index shift. Combine this with (13) and finite sums for general \(C^L\)-coefficient differential operators. \(\square\)

No compactly supported cutoff in the class \(C^L\) is asserted. The cutoffs in (14) are smooth families with estimates through a finite index, so the argument also applies to quasianalytic classes.

**Theorem 2.3 (base regularity).** The projection of \(\operatorname{WF}_L(u)\) to the base is precisely the set where \(u\) fails to belong locally to \(C^L\).

**Proof.** If \(u\in C^L\) near a point, choose the cutoffs \(\chi_N\) supported there. The product rule, (4), monotonicity of \(L\), and \(N\leq L_N\) show
\[
 \|\partial^\alpha(\chi_Nu)\|_\infty\leq C^{N+1}M_N
                               \quad(|\alpha|=N).
 \tag{20}
\]
Directional integrations by parts give (11) in every direction. For \(|\eta|\leq1\), use the uniform zeroth bound and absorb \(2^N\). The sequence has common order zero and a common plateau, so all nonzero covectors are absent.

Conversely, if the entire fiber is absent, finitely cover the unit covectors by witnesses and apply Lemma 2.2. It yields one compact sequence \(w_N\), agreeing with \(u\) near the point, whose estimate (11) holds in every direction. By (12), \(u\) is smooth there. For \(|\alpha|=k\), take \(N=k+n+1\) in Fourier inversion. The needed radial integral is
\[
 \int_0^\infty r^{k+n-1}(1+r)^{-k-n-1}dr
       =\frac1{k+n}.
 \tag{21}
\]
Substitution \(t=r/(1+r)\) proves the equality. Including the sphere area and inverse Fourier factor bounds the derivative by \(C^{N+1}M_N\). Lemma 1.1 with the fixed shift \(n+1\) gives \(C^{k+1}M_k\), uniformly on a smaller neighborhood. Handle \(k=0\) with its fixed bound. This is (4). \(\square\)

## 3. Gaussian packets detect the whole derivative sequence

For a tempered distribution set
\[
 T_hu(x,\xi)=u\big(e^{-|y-x|^2/(2h)}e^{-iy\cdot\xi/h}\big).
 \tag{22}
\]
For a local distribution choose a compact extension agreeing on a smaller neighborhood. The uniform Gaussian-tail lemma [G], Lemma 1.1, makes the criterion below independent of that extension.

**Theorem 3.1 (class packet criterion).** For \(\xi_0\ne0\), absence from \(\operatorname{WF}_L(u)\) is equivalent to the existence of common neighborhoods \(U,V\), a common \(h_0>0\), and one \(A\geq1\) with
\[
 |T_hu(x,\xi)|\leq A^{N+1}M_N h^N
   \quad(N\geq1,\ x\in U,\ \xi\in V,\ 0<h\leq h_0).
 \tag{23}
\]
The closure of \(V\) may be taken in a bounded annulus away from zero.

**Proof of necessity.** Use the compact witnesses \(w_N\) from (11). They have a common global polynomial Fourier bound and common agreement neighborhood. The complete Gaussian convolution formula [G], equation (19), is
\[
 T_hw_N(x,\xi)
   =\left(\frac h{2\pi}\right)^{n/2}e^{-ix\cdot\xi/h}
       \int\widehat w_N(\eta)e^{ix\cdot\eta}
                 e^{-h|\eta-\xi/h|^2/2}d\eta.
 \tag{24}
\]
Its normalized Gaussian has mass one. Shrink \(V\) inside the regular cone and let \(0<c_0\leq|\xi|\leq c_1\). On the good cone with \(|\eta|\geq c_0/(2h)\), (11) bounds the integral by \(C^{N+1}M_Nh^N\).

The complementary frequencies have
\(|\eta-\xi/h|\geq d(|\eta|+h^{-1})\), as proved geometrically in [G], equation (21). The common polynomial bound therefore gives \(Ch^{-m'}e^{-c/h}\). The off-support differences \(u-w_N\) have the same kind of bound by [G], Lemma 1.1.

For every fixed nonnegative \(b\), maximizing \(r^{N+b}e^{-cr}\), \(r=h^{-1}\), proves
\[
 h^{-b}e^{-c/h}\leq C_b^{N+1}N^N h^N
                         \leq C_b^{N+1}M_Nh^N.
 \tag{25}
\]
The maximizer is \((N+b)/c\); its fixed additional polynomial is absorbed exponentially. Thus the tails satisfy (23) with the same neighborhoods for all \(N\). Notice that the witness \(w_N\) is chosen for each index, while the packet being estimated is that of the fixed \(u\).

**Proof of sufficiency.** Fix a Schwartz order \(s\) of the compact extension and the controlled cutoffs supported in \(U\). For the desired output index \(N\), let
\[
 K=N+s,\qquad u_N=\chi_{2K}u.
 \tag{26}
\]
Its support, plateau and compact order are common. For \(\eta=r\theta\) in a smaller cone, put \(\rho=|\xi_0|>0\), \(h=\rho/r\), and
\[
 b=B_{K,h}\chi_{2K},\qquad
 B_{K,h}f=\sum_{j=0}^{K-1}\frac{(-h/2)^j}{j!}\Delta^j f.
 \tag{27}
\]
The complete inverse heat identity and weighted norm bounds are [G], Lemma 2.1 and equations (14)–(15). They give
\[
 \|S_hb-\chi_{2K}\|_{s,s}\leq C^{K+1}K^Kh^K,\qquad
 \|b\|_1\leq C e^{ChK^2},
 \tag{28}
\]
where \(S_h\) is convolution with the normalized heat Gaussian. The exact test integral is
\[
 \int b(x)T_hu(x,\rho\theta)dx
        =(2\pi h)^{n/2}\widehat{(S_hb)u}(r\theta).
 \tag{29}
\]
Every parameter integral is justified in Schwartz-test seminorms in the supplied proof.

For \(r\geq1\), the remainder paired with the frequency exponential is bounded by
\[
 C^{K+1}K^Kh^K(1+r)^s
     \leq C^{N+1}N^N r^{-N}
     \leq C^{N+1}M_N r^{-N}.
 \tag{30}
\]
Here \(K=N+s\); the fixed powers of \(\rho\) and extra powers of \(N\) are absorbed into \(C^{N+1}\), exactly as in [G], equation (25).

Take a fixed \(D\) large enough that \(r\geq DK\) ensures \(h\leq\min(1,h_0)\). Then
\[
 e^{ChK^2}=e^{C\rho K^2/r}\leq e^{C\rho K/D}\leq C_1^{N+1}.
 \tag{31}
\]
Choose a fixed integer \(c\geq n/2\) and apply (23) at index \(N+c\). After division by the factor in (29), the main term is at most
\[
 C^{N+1}M_{N+c}\,r^{n/2-N-c}
        \leq C_2^{N+1}M_N r^{-N},
 \tag{32}
\]
by Lemma 1.1. This estimate uses a fixed shift, rather than optimizing an index as a function of the frequency.

For \(r<DK=D(N+s)\), use the common compact-order bound
\(|\widehat u_N|\leq C(1+r)^s\). Multiplication by \((1+r)^N\) costs at most \(C^{N+1}N^N\), after absorbing the fixed \(s\), and hence at most \(C^{N+1}M_N\). Finally replace \(r^{-N}\) by \((1+r)^{-N}\) at large \(r\), costing \(2^N\). These bounds prove (11).

The localized distribution \(u_N\) in (26) is fixed before its transform is estimated. The auxiliary \(b\) may depend on the frequency; this does not change that sequence. \(\square\)

At the analytic weight \(L_N=N+1\), (23) is equivalent to the exponential packet bound in [G], Theorem 3.1. For any fixed \(s\geq1\), the Gevrey weight \(L_N=(N+1)^s\) makes (23) equivalent to
\[
 |T_hu(x,\xi)|\leq C e^{-c h^{-1/s}}.
 \tag{33}
\]
For the forward equivalence, choose \(N=\lfloor\varepsilon h^{-1/s}\rfloor\) with sufficiently small fixed \(\varepsilon\); the factor \(A((N+1)^sh)^N\) is exponentially decreasing in \(h^{-1/s}\). Bounded remaining \(h\)'s are absorbed into \(C\). Conversely maximize \(r^{sN}e^{-cr}\), \(r=h^{-1/s}\); its maximum is \((sN/(ce))^{sN}\), bounded by \(C^{N+1}(N+1)^{sN}\). Both directions keep the same neighborhoods.

## 4. The full homogeneous Fourier interchange holds for the class

Let
\[
 V_gu(X,\Xi)=u(e^{-|y-X|^2/2}e^{-iy\cdot\Xi}),\qquad E=y\cdot\nabla_y.
 \tag{34}
\]
Assume that a global distribution \(u\) satisfies
\[
 (E-\lambda)^{q+1}u=0
       \quad\hbox{on }\mathbb R^n\setminus\{0\},
       \qquad \lambda\in\mathbb C,\quad q\geq0.
 \tag{35}
\]
The full annular proof [G], Lemma 5.1, makes \(u\) tempered, including arbitrary angular distributions and arbitrary global extensions at the origin.

**Theorem 4.1 (derivative-sequence interchange).** Under (2) and (35),
\[
 (x,\xi)\in\operatorname{WF}_L(u)
       \quad\Longleftrightarrow\quad
 (\xi,-x)\in\operatorname{WF}_L(\widehat u),
                         \qquad x\ne0,\quad\xi\ne0.
 \tag{36}
\]
There is no parity or integer-degree condition.

**Proof.** Retain the full finite vector \(U_j=(E-\lambda)^ju\), \(0\leq j\leq q\), and its nilpotent matrix \(J_{j,j+1}=1\). By Lemma 2.2 every component has class wavefront contained in that of its zeroth component, so their union is exactly \(\operatorname{WF}_L(u)\). Fourier coordinate rules give
\[
 \widehat U_j=(-1)^j(E-\mu)^j\widehat u,\qquad
                              \mu=-n-\lambda.
 \tag{37}
\]
Thus the transformed vector's union is exactly \(\operatorname{WF}_L(\widehat u)\) as well.

Use the entire point-jet and polynomial anomaly calculation [G], Lemma 6.1 and Section 7. On compact neighborhoods away from the indicated zero entries it gives
\[
 \begin{aligned}
 V_gU(tx,t\xi)&=t^{n+\lambda}e^{(\log t)J}T_{t^{-2}}U(x,\xi)
                                      +O(t^b e^{-c t^2}),\\
 V_g\widehat U(tx,t\xi)&=
        t^{n+\mu}e^{-(\log t)J}T_{t^{-2}}\widehat U(x,\xi)
                                      +O(t^{b'}e^{-c't^2}).
 \end{aligned}
 \tag{38}
\]
The first error is valid when \(x\ne0\); the second is valid when \(\xi\ne0\). They retain the arbitrary point jets and Fourier polynomials. The matrices, their inverses and the complex powers have polynomial growth together with their inverses.

For a family satisfying the all-index bound
\(A^{N+1}M_Nt^{-2N}\), multiplication by any fixed power \(t^b\) preserves the same kind of bound. Indeed use the input index \(N+c\), \(2c\geq b\), and Lemma 1.1. Fixed powers of \(\log t\) are bounded by a further fixed power of \(t\). Also
\[
 t^b e^{-ct^2}\leq C^{N+1}N^Nt^{-2N}
                            \leq C^{N+1}M_Nt^{-2N},
 \tag{39}
\]
by the maximization used in (25), with variable \(t^2\). Therefore each line of (38) is an equivalence of the all-index packet estimates, with a new common exponential constant.

For a finite vector, intersect finitely many packet neighborhoods and take the largest constant in (23). Theorem 3.1 identifies absence for \(U\) at \((x,\xi)\) with the all-index estimate for \(V_gU(tx,t\xi)\). The whole Fourier identity [G], Lemma 4.1,
\[
 V_g(\widehat U)(X,\Xi)
     =(2\pi)^{n/2}e^{-iX\cdot\Xi}V_gU(-\Xi,X),
 \tag{40}
\]
then identifies it with the estimate for \(V_g\widehat U(t\xi,-tx)\). Apply the second line of (38) at the rotated pair, and Theorem 3.1 once more. Both entries remain bounded away from zero, so both errors apply. The component-union identities reduce this equivalence to the scalar wavefront sets. Taking complements proves (36). \(\square\)

Adding finite point jets at zero does not change (36): the physical difference vanishes at each nonzero base point, and its full Fourier transform is a polynomial, which belongs to every \(C^L\). Finite-sum inclusions in both directions show unchanged class wavefront. The exclusions in (36) and the homogeneity condition are substantive, as the constant, point delta and nonconstant plane-wave examples in [G], Solution 8, demonstrate.

## 5. Analytic pullback preserves the class covectors

Let \(F:X\subset\mathbb R^b\to Y\subset\mathbb R^a\) be real analytic, and put
\[
 N_F=\{(F(x),\eta):\eta\ne0,\ DF(x)^T\eta=0\}.
 \tag{41}
\]
Here \(a\) is the dimension of the space carrying the input distribution. The transpose derivative determines the output covector.

**Theorem 5.1 (transverse analytic pullback).** If
\[
 N_F\cap\operatorname{WF}_L(u)=\varnothing,
 \tag{42}
\]
the ordinary distributional pullback exists and satisfies
\[
 \operatorname{WF}_L(F^*u)
       \subseteq\{(x,DF(x)^T\eta):
                      (F(x),\eta)\in\operatorname{WF}_L(u)\}.
 \tag{43}
\]

**Proof.** By (12), condition (42) implies the ordinary transversality condition. Use the complete ordinary pullback construction, local Fourier formula and scalar composition law in [P], Section 1. This defines the distribution whose class regularity we estimate; no different pullback is introduced.

Fix a pair \((x_0,\xi_0)\), \(\xi_0\ne0\), outside the right side of (43). At \(y_0=F(x_0)\), the unit class-singular directions are compact. Their transpose images are nonzero by (42), and none has the positive direction of \(\xi_0\). Normalize input and output covector lengths to sum to one. Compactness gives a closed angular neighborhood \(\Omega\) of those singular directions, a compact neighborhood \(K\) of \(x_0\), and an output cone \(\Gamma\) about \(\xi_0\), with
\[
 |DF(x)^T\eta-\xi|\geq d(|\eta|+|\xi|)
           \quad(x\in K,\ \eta\in\Omega,\ \xi\in\Gamma).
 \tag{44}
\]
Indeed a zero minimum would give either a nonzero input normal covector, or an excluded positive output direction. Shrinking the neighborhoods keeps a strict positive margin. If the singular fiber is empty, take \(\Omega=\varnothing\).

The complementary unit directions have a finite regularity cover. Lemma 2.2 gives one sequence \(w_J\), agreeing with \(u\) near \(y_0\), with common order \(m\), such that
\[
 \begin{aligned}
 |\widehat w_J(\eta)|&\leq C(1+|\eta|)^m
                                          &&\hbox{everywhere},\\
 |\widehat w_J(\eta)|&\leq A^{J+1}M_J(1+|\eta|)^{-J}
                                          &&(\eta\notin\Omega).
 \end{aligned}
 \tag{45}
\]
Choose its plateau first, then shrink \(K\) so \(F(K)\) lies in it. Take controlled output cutoffs \(b_J\) supported in \(K\). Set
\[
 J=N+m+a+2,\qquad v_N=b_JF^*u.
 \tag{46}
\]
The localized output is fixed for each \(N\), has common compact support and order, and agrees with \(F^*u\) on a common plateau. By locality and the complete ordinary Fourier formula,
\[
 \widehat v_N(\xi)=(2\pi)^{-a}
       \int\widehat w_J(\eta)I_J(\xi,\eta)d\eta,\qquad
 I_J=\int b_J(x)e^{i(F(x)\cdot\eta-x\cdot\xi)}dx.
 \tag{47}
\]
On this compact output domain \(w_J\) agrees with \(u\), so the same ordinary transversality applies. The estimates below also prove absolute convergence of (47).

The full analytic phase iteration [P], Lemma 3.1, gives
\[
 |I_J(\xi,\eta)|\leq C^{J+1}J^J
                       (1+|\xi|+|\eta|)^{-J}
 \tag{48}
\]
where its phase gradient has the margin in (44). It includes every differentiated analytic coefficient and has only one factorial scale.

On \(\Omega\), combine (48) with the polynomial bound in (45). Scaling the \(a\)-dimensional \(\eta\)-integral yields
\[
 C^{J+1}J^J
       \int(1+|\xi|+|\eta|)^{-J}(1+|\eta|)^m d\eta
    \leq C^{J+1}J^J(1+|\xi|)^{m+a-J}.
 \tag{49}
\]
The remaining scaled integral is uniformly finite since \(J\geq m+a+3\).

Outside \(\Omega\), split at \(|\eta|=c_0|\xi|\), with \(c_0\) smaller than \(1/(2\sup_K\|DF^T\|)\); if the norm vanishes choose \(c_0\leq1\). Below that threshold the gradient has size at least \(|\xi|/2\), and combined lengths are comparable to \(|\xi|\). The same phase estimate and polynomial bound give (49). Above the threshold use only \(|I_J|\leq C\) and the class estimate in (45), giving
\[
 C^{J+1}M_J(1+|\xi|)^{a-J}.
 \tag{50}
\]
Radial integration proves this tail bound. At bounded \(|\xi|\), integrate the whole regular estimate and increase the constant.

In (49), \(J^J\leq M_J\); in (50), there is already just one \(M_J\). Lemma 1.1 turns either into \(C^{N+1}M_N\) for the fixed shift in (46). The exponents in (49)–(50) are at most \(-N\). Thus (11) holds for \(v_N\) in \(\Gamma\), proving (43). The proof never multiplies a nonstationary-phase factorial weight by a class Fourier weight: it uses the polynomial input bound on the phase-controlled part and the bounded amplitude on the class-controlled part. \(\square\)

**Corollary 5.2 (analytic coordinates and restriction).** For an analytic diffeomorphism, (43) is an equality. For an analytic embedding \(j:S\to X\), disjointness of its nonzero conormal bundle from \(\operatorname{WF}_L(u)\) gives the actual restriction \(j^*u\) with bound (43).

**Proof.** For a diffeomorphism apply Theorem 5.1 to it and to its analytic inverse. The scalar composition law in [P], Section 1, makes the two inclusions inverse. For an embedding, its normal set consists exactly of covectors killed by \(Dj^T\), namely the conormals. Apply the same theorem in analytic charts. The scalar Jacobians and analytic density changes agree on overlaps by the exact construction in [P], Section 1; analytic nonzero density factors preserve the class wavefront by Lemma 2.2 applied also to their analytic reciprocals. \(\square\)

## 6. Tensors and products keep their zero components

Adjoin the zero covector over the actual support:
\[
 \operatorname{WF}_{L,0}(u)=\operatorname{WF}_L(u)
                    \cup\{(x,0):x\in\operatorname{supp}u\}.
 \tag{51}
\]

**Theorem 6.1 (class tensor bound).**
\[
 \operatorname{WF}_L(u\otimes v)
       \subseteq
       \big(\operatorname{WF}_{L,0}(u)\times
                    \operatorname{WF}_{L,0}(v)\big)\setminus0.
 \tag{52}
\]

**Proof.** The ordinary tensor product and its common finite-order compact-test estimates are supplied in [P], Section 1. Outside the product of supports it vanishes. At a base point inside that product, a nonzero pair outside the right side of (52) has at least one nonzero regular component. Suppose it is \((x_0,\xi_0)\) for \(u\).

Choose compact extensions of the two local factors. The full Gaussian test is a tensor of its component tests, so
\[
 T_h(u\otimes v)((x,y),(\xi,\eta))
                         =T_hu(x,\xi)\,T_hv(y,\eta).
 \tag{53}
\]
This is the exact tensor pairing identity on Schwartz tests, with the same \(h\). On bounded position and covector sets, a fixed Schwartz order of \(v\) gives
\(|T_hv|\leq C h^{-m}\) for an integer \(m\): every required test derivative and weight is a polynomial times the Gaussian, and its maximum costs only a fixed inverse power.

Use Theorem 3.1 for \(u\) at index \(N+m\). Projection of a sufficiently small neighborhood of the full pair leaves \(\xi\) in its regular neighborhood, while \(\eta\) stays bounded. Equations (53) and (5) give
\[
 |T_h(u\otimes v)|\leq C^{N+1}M_{N+m}h^N
                       \leq C_1^{N+1}M_Nh^N.
 \tag{54}
\]
The packet criterion proves absence for the full pair. If the regular component is that of \(v\), reverse the roles. These are every excluded pair, proving (52). \(\square\)

For the projection pullback \(\pi(x,y)=x\), the constant factor is regular in every class, and
\[
 \operatorname{WF}_L(\pi^*u)
       =\{(x,y;\xi,0):(x,\xi)\in\operatorname{WF}_L(u)\}.
 \tag{55}
\]
The tensor upper bound proves one inclusion. For the other, restrict to the analytic slice \(j_y(x)=(x,y)\). Its pure-fiber normal covectors miss that upper bound. The actual ordinary identity \(j_y^*(u\otimes1)=u\) is [P], Section 5. Theorem 5.1 then forces every class covector of \(u\) into the displayed fiber. This proves equality for each fixed \(y\).

**Corollary 6.2 (nonopposing products).** If there is no pair
\[
 (x,\xi)\in\operatorname{WF}_L(u),\qquad
 (x,-\xi)\in\operatorname{WF}_L(v),\qquad \xi\ne0,
 \tag{56}
\]
the ordinary product exists, and
\[
 \operatorname{WF}_L(uv)
   \subseteq\{(x,\xi+\eta):
        (x,\xi)\in\operatorname{WF}_{L,0}(u),\
        (x,\eta)\in\operatorname{WF}_{L,0}(v)\}\setminus0.
 \tag{57}
\]

**Proof.** Ordinary inclusion (12) makes (56) imply the ordinary product condition. The diagonal map \(\Delta(x)=(x,x)\) is analytic, its transpose sends \((\xi,\eta)\) to \(\xi+\eta\), and its normal set is the nonzero opposing pairs. The tensor bound and (56) make it transverse to \(u\otimes v\). Apply Theorem 5.1 to
\(uv=\Delta^*(u\otimes v)\), using the actual ordinary diagonal construction in [P], Section 6. Zero components retain the single-factor terms. \(\square\)

All these statements are local on analytic manifolds. A zero-dimensional factor has only scalar distributional pairings and no nonzero covectors. A finite zero-dimensional fiber contributes a finite sum. Restriction to a point requires the class wavefront fiber there to be empty; Theorem 2.3 then gives a smooth \(C^L\) representative whose value is the restriction. This also covers the two-point sphere in dimension one.

## 7. Proper projection retains zero fiber covectors

**Theorem 7.1 (class projection).** Let \(\pi(x,y)=x\), and suppose its restriction to \(\operatorname{supp}u\) is proper. The ordinary distributional projection integral exists and satisfies
\[
 \operatorname{WF}_L(\pi_*u)
    \subseteq\{(x,\xi):\xi\ne0,\
          (x,y;\xi,0)\in\operatorname{WF}_L(u)
                      \text{ for some }y\}.
 \tag{58}
\]

**Proof.** The complete ordinary definition and cutoff independence are [P], Sections 1 and 7. Fix an output pair outside the right side. A compact output neighborhood sees a compact source support by properness. The fiber over the chosen point is therefore compact. Its covectors \((\xi_0,0)\) are absent from the class wavefront at every occupied source point.

Take a finite regularity cover of that fiber, with a common smaller output neighborhood and a cone about \(\xi_0\). Shrinking the output neighborhood ensures that every occupied source point above it remains in the cover: otherwise a sequence of omitted points over bases approaching \(x_0\) would have a convergent subsequence in the compact source support, giving an omitted fiber point.

Use the finite controlled partitions of Lemma 2.2 and [P], Lemma 2.2, whose sum is one on this occupied support. Include a controlled compact cutoff in \(x\) with a common plateau. The normalized source terms have common compact support and order, and their transforms obey (11) at the source covectors \((\xi,0)\), with one maximum constant for the finite cover. This follows from the mixed-derivative version of Lemma 2.2: multiplication by any of these controlled families has the bounds (15)–(18), so a fixed index shift accounts for it.

Project the sum of these compact terms. Its output sequence has common compact support and order and agrees with \(\pi_*u\) on the fixed output plateau. For every compact source term \(w_N\), the exact Fourier identity is
\[
 \widehat{\pi_*w_N}(\xi)=\widehat w_N(\xi,0).
 \tag{59}
\]
It follows directly from the ordinary test definition, or the complete formula in [P], Section 7. The source estimate thus gives (11) for the output sequence. This proves absence and hence (58). \(\square\)

**Corollary 7.2 (proper kernels on class inputs).** Suppose \(K\in\mathcal D'(X\times Y)\) and projection of its support to \(X\) is proper. For \(a\in C^L(Y)\), the kernel pairing defines \(\mathcal Ka\), and
\[
 \operatorname{WF}_L(\mathcal Ka)
    \subseteq\{(x,\xi):\xi\ne0,\
          (x,y;\xi,0)\in\operatorname{WF}_L(K)
                            \text{ for some }y\in\operatorname{supp}a\}.
 \tag{60}
\]

**Proof.** The smooth multiplier \(a(y)\) defines \(K\,a(y)\). Its support is contained in \(\operatorname{supp}K\cap(X\times\operatorname{supp}a)\), so it remains proper over \(X\). Lemma 2.2 gives \(\operatorname{WF}_L(K\,a)\subseteq\operatorname{WF}_L(K)\). Apply Theorem 7.1 to its projection. The source support gives the stated restriction to \(\operatorname{supp}a\). On compact output tests, properness supplies one compact source cutoff, so this pairing is independent of that cutoff. \(\square\)

## 8. Class estimates and ordinary continuity are distinct

The normal topology in [P], Section 8, uses strong compact-test convergence together with rapid Fourier seminorms outside a fixed ordinary wavefront cone. Its pullback and proper projection maps are continuous; tensor and nonopposing product maps are hypocontinuous and sequentially continuous, with the exact common proper-support hypothesis for projection. These complete statements apply to the ordinary constructions used above. They do not assert that ordinary convergence preserves an absence estimate with one common class constant.

**Proposition 8.1 (uniform class limits).** Let \(u_j\to u\) distributionally near a compact base neighborhood, and use compact extensions with a common support and finite order. Suppose on common packet neighborhoods \(U,V\), with a common \(h_0\) and \(A\),
\[
 |T_hu_j(x,\xi)|\leq A^{N+1}M_Nh^N
                \quad\text{for every }j,\ N\geq1,\ 0<h\leq h_0.
 \tag{61}
\]
Then \(u\) has the same absence estimate there.

**Proof.** For each fixed \(h,x,\xi\), multiply the Gaussian test by a fixed compact cutoff equal to one on the extensions' common support. Distributional convergence applies to this fixed test, giving \(T_hu_j\to T_hu\). Pass to the limit in (61) for each index and parameter. Its constants and neighborhoods remain unchanged, so Theorem 3.1 applies. If the distributions are initially only local, multiply them by one common compact extension cutoff. A distributionally convergent sequence is uniformly bounded on the fixed compact test space, and its bounded-test estimate gives one common finite order there. These complete bounded-test and finite-order facts are [P], Sections 1 and 8. \(\square\)

**Example 8.2 (smooth convergence can lose a class).** Define
\[
 f_R(x)=\int_0^R e^{-\sqrt t}e^{itx}\,dt,\qquad
 f(x)=\int_0^\infty e^{-\sqrt t}e^{itx}\,dt.
 \tag{62}
\]
For finite \(R\), the first function is entire. For every fixed derivative order \(k\),
\[
 \sup_{x\in\mathbb R}|\partial^k(f-f_R)(x)|
       \leq\int_R^\infty t^k e^{-\sqrt t}dt\longrightarrow0.
 \tag{63}
\]
Substitution \(t=r^2\) gives an integrable exponential times a polynomial. Differentiation under the integral follows from the same domination. Thus \(f\) is smooth, and \(f_R\to f\) uniformly with every fixed derivative, even on the whole real line.

At zero the exact moments are
\[
 f^{(k)}(0)=2i^k\int_0^\infty r^{2k+1}e^{-r}dr
                          =2i^k(2k+1)!.
 \tag{64}
\]
Repeated integration by parts proves the factorial integral, with both endpoint terms zero. For a Gevrey order \(s<2\), a \(C^L\) bound near zero would require
\(2(2k+1)!\leq A^{k+1}(k+1)^{sk}\).
The lower factorial estimate (10) makes the ratio grow at least as
\(C^{-k-1}k^{(2-s)k}\), which diverges for every fixed \(C\). Such a local bound is impossible. For \(s\geq2\), the moment bound gives global class regularity: \((2k+1)!\leq(2k+1)^{2k+1}\leq C^{k+1}(k+1)^{2k}\), and larger \(s\) only increases the weight.

For \(\operatorname{Im}z>0\), the integral defining \(f(z)\) is holomorphic and has the uniform bound \(|f(z)|\leq2\). It has the displayed smooth distributional boundary value by dominated convergence. The positive-polar tube theorem [A], Theorem 4.1, permits only positive analytic covectors at zero. By (12), the same holds for every class wavefront. Theorem 2.3 and the failed derivative bound force a nonempty class fiber at zero when \(1\leq s<2\). Positive conicity in one dimension then makes that fiber the entire positive ray.

This convergence also holds in the ordinary normal topology with empty ordinary wavefront cone. Strong distributional convergence follows from the uniform bound in (63) at \(k=0\). For each fixed compact smooth cutoff and each Fourier power, integrations by parts bound the rapid Fourier seminorm of its product with \(f-f_R\) by finitely many of the derivative norms in (63), which tend to zero. Hence every such seminorm tends to zero. Each entire \(f_R\) has empty class wavefront, while \(f\) has the positive class fiber at zero for orders below two. The missing information is uniformity of the class constants, neighborhoods and small-\(h\) range, rather than ordinary smooth convergence.

**Proposition 8.3 (uniform estimates for the admissible operations).** In Theorems 5.1, 6.1 and 7.1, fix the maps, compact local supports, conic transversality margins and distributional orders. If the regular input directions have common packet estimates (23) with one common constant on the finite neighborhoods used in the proofs, the output class estimates can also use common constants. For the convergence assertion, also fix ordinary wavefront cones satisfying the exact pullback, nonopposing product and projection hypotheses of [P], Theorems 8.1–8.3, and use their ordinary normal topology. Combined with those continuity or hypocontinuity results, the uniform class estimates give class-preserving limits. Proper projection limits require one common closed proper source support.

**Proof.** The converse in Theorem 3.1 constructs input compact witnesses from the same cutoffs and the same order shift. Equations (28)–(32) depend only on the common distributional order and bound, packet constant and fixed neighborhoods. Thus their witness estimates are uniform for the family.

In the pullback proof, the gradient margin, cutoff derivatives and analytic phase constants in (44)–(50) depend only on the fixed map and compact conic data. The polynomial input bound and regular Fourier bound are now uniform, so the resulting \(M_N\) estimate is uniform. The common output order also follows from a fixed-index version of (47) with a compact test amplitude: in the potentially singular input directions the normal-set margin gives \(|DF^T\eta|\geq d|\eta|\), and a fixed number of integrations absorbs the common input polynomial order; in the regular directions use the uniform decay at one sufficiently large fixed index. The test amplitude needs only those finitely many derivatives. Both integrals are then bounded by a fixed finite-order compact test norm, uniformly in the family.

The tensor finite-order estimate is the complete compact tensor bound in [P], Section 1. Its class proof uses only the common class constant for one factor and common order for the other; (54) is uniform. The diagonal and restriction statements use these already uniform tensor and pullback estimates. Projection uses a finite cover of a compact source support and the same controlled partitions; the common proper closed support makes that compact set independent of the family. Its finite-order estimate simply lifts the compact output test with one fixed compact fiber cutoff. Equation (59) then gives uniform output class estimates.

The complete ordinary normal continuity and hypocontinuity results identify the distributional limit with the corresponding operation on the limiting inputs. Apply Proposition 8.1 to the uniform output estimates. This proves the limit assertion. Tensor and product remain subject to hypocontinuity; no joint ordinary normal continuity, or class preservation without uniform class constants, is inferred. \(\square\)

## References

[A] [Analytic directions of holomorphic boundary values][A], Lemma 1.1, with the complete controlled cutoff construction and uniform fixed low derivatives.

[P] [Pulling back and combining analytic singularities][P], Section 1 and Lemmas 2.2 and 3.1, with the complete smooth constructions, controlled partitions and one-scale analytic nonstationary phase estimate.

[G] [Gaussian packets and homogeneous Fourier directions][G], Lemmas 1.1, 2.1, 4.1, 5.1 and 6.1, Section 7 and Theorem 8.1. The full inverse heat remainder and arbitrary origin anomaly identities are supplied there.

[F] [Schwartz functions and Fourier inversion][F], Sections 1–5, with all compact-distribution and Fourier identities used above.

[C] [Cauchy bounds, root counts and analytic extensions][C], Lemma 1.1 for the polydisc coefficient estimate and Lemma 3.1 for the local complex extension of a real analytic map.

[B] Jan Boman, *Microlocal Quasianalyticity for Distributions and Ultradistributions*, Publications of the Research Institute for Mathematical Sciences **31** (1995), 1079–1095. [Primary article](https://ems.press/content/serial-article-files/40593), especially Section 1 for derivative-weight wavefront conventions. It remains under its actual publisher terms; no article text or proof is redistributed here.

Original exposition and proofs here are CC0. Linked prerequisite proofs and references retain their actual component authorship and terms.

[A]: ../../AN02-L186.html#complete-proof
[P]: ../../AN02-L188.html#complete-proof
[G]: ../../AN02-L189.html#complete-proof
[F]: https://github.com/KokunoYumeto/open-math-courses-public/blob/5949a0e862f3d87dbc078ae57149cf10c2b37dd2/docs/courses/AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md
[C]: ../../AN02-L045.html

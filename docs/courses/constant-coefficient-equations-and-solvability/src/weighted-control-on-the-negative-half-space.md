# Weighted control on the negative half-space

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The analytic-branch estimate controls a supremum of one-dimensional restriction norms. We now turn it into a norm estimate on the whole negative half-space, with an arbitrary moderate weight in all frequency variables. The two changes have separate mechanisms: a spatial cutoff brings complex frequencies back to the real axis, and a compact modulated convolution window localizes the weight. The final argument uses the exact disintegration already proved.

Read [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md), [Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The statement and the normalized root hypothesis

Write \((x,t)\in\mathbb R^d\times\mathbb R\), \(d\ge1\), and let \(P(z,s)\ne0\) be a polynomial. Assume that for some \(A\ge1\), every analytic root \(\tau\) on a complex ball of radius \(A\) with real center satisfies
\[
\begin{gathered}
P(z,\tau(z))=0
       \\
\quad\Longrightarrow\\
\quad
       \sup\operatorname{Im}\tau\ge A+1
       \text{ on that ball}.
\end{gathered}
\tag{1}
\]
Let \(S_P\) denote the exact full polynomial derivative norm. For a positive moderate joint weight \(k\), use the full-space and negative-half-space norms([equation 1 in Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md))–([equation 2 in Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md)).

**Theorem.** There is \(\kappa\ge0\), depending only on \(P,A,d\), such that for every \(1\le p\le\infty\) and every such weight \(k\), there is \(C_{p,k}<\infty\) with
\[
 \|v\|^-_{p,k}\le C_{p,k}e^{\kappa L}
                         \|P(D)v\|^-_{p,k/S_P},
 \tag{2}
\]
whenever \(v\in C_c^\infty(\mathbb R^{d+1})\), \(L\ge0\), and
\(|x|\le L\) on \(\operatorname{supp}v\cap\{t<0\}\).
The exponent \(\kappa\) is independent of \(p,k\). Reducible polynomials and repeated factors are included.

## Integrating actual Schwartz representatives

We first record the integral inequality needed for a quotient norm. Fix a moderate time weight \(\rho\), and let \(H(\eta,t)\) be a continuous Schwartz-valued function of the real parameter \(\eta\in\mathbb R^d\). Assume every Schwartz seminorm of \(H(\eta,\cdot)\) has an integrable parameter bound. Its actual pointwise integral and every fixed time derivative then define a time-Schwartz function \(h=\int H(\eta,\cdot)\,d\eta\), by dominated differentiation and the seminorm bounds. The fixed restriction norm satisfies
\[
 \left\|\int H(\eta,\cdot)\,d\eta\right\|^-_{p,\rho}
                \le\int\|H(\eta,\cdot)\|^-_{p,\rho}\,d\eta.
 \tag{3}
\]
For completeness, truncated Riemann sums converge to this integral in each Schwartz seminorm. On a compact parameter box, continuity gives uniform continuity in each of finitely many specified seminorms; choose a fine mesh for them. Integrable seminorm tails give convergence as the boxes increase. A diagonal choice controls successively every seminorm. The quotient map is continuous on Schwartz space, so its composition with each continuous unit-norm functional commutes with this limit and with the scalar integral. Scalar absolute-value bounds and the norm test B6 prove(3). Equivalently its norm is bounded by the integral of its norms at the finite-sum stage and in the limit. A completed quotient or an unproved Banach-valued integral is unnecessary.

All applications below have a joint Schwartz time family multiplied by a rapidly decreasing parameter kernel, so these integrable seminorm bounds hold.

## From complex frequencies to a real integral

Assume first that \(P\) is irreducible and that \(k=k(s)\) depends only on the time frequency. Set \(g=P(D)v\) and
\[
 F(\eta)=\|\mathcal F_xg(\eta,\cdot)\|^-_{p,k/S_P(\eta,\cdot)}.
 \tag{4}
\]
This is continuous by the [Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md) varying-weight argument and is integrable. Indeed the real partial transform of \(g\) decays with every time-Schwartz seminorm as \(|\eta|\to\infty\), \(k(s)\) has polynomial growth, and \(S_P(\eta,s)\) has a uniform positive lower bound from one constant highest derivative.

Choose \(\chi\in C_c^\infty(\mathbb R^d)\) equal to one on the unit ball and supported in the closed ball of radius two. Put \(B=\max(1,L)\), \(\chi_B(x)=\chi(x/B)\). Locality of \(P(D)\) implies that \(g\)'s negative-time spatial support is also inside the radius-\(L\) ball. Therefore \(\chi_Bg=g\) for \(t<0\).

The product-transform formula gives an actual full-time Schwartz representative
\[
\begin{gathered}
\mathcal F_x(\chi_Bg)(z,t)
   \\
=(2\pi)^{-d}\int_{\mathbb R^d}
        \\
\widehat\chi_B(z-\eta)\mathcal F_xg(\eta,t)\,d\eta,
             \\z\in\mathbb C^d.
\end{gathered}
\tag{5}
\]
To justify complex \(z\), insert the real-frequency inverse transform of \(g\); compact support of \(\chi_B\), the real Schwartz decay of that transform and a finite bound on \(e^{x\cdot\operatorname{Im}z}\) make Fubini absolutely convergent. Each time derivative obeys the same bounds. This representative has the same negative-time restriction as \(\mathcal F_xg(z,\cdot)\).

Let \(m=\deg P\). The finite jet-matrix shift, valid with complex base points, gives
\(S_P(\eta,s)/S_P(z,s)\le(1+C_P|z-\eta|)^m\).
Use the fixed time weight \(k/S_P(z,\cdot)\) in(3) and then this pointwise weight comparison. The result is
\[
\begin{gathered}
\|\mathcal F_xg(z,\cdot)\|^-_{p,k/S_P(z,\cdot)}
 \\
\le (2\pi)^{-d}\int
   \\
|\widehat\chi_B(z-\eta)|\\
(1+C_P|z-\eta|)^m F(\eta)\,d\eta.
\end{gathered}
\tag{6}
\]
No parameter-dependent norm is moved through an analytic argument here: for each fixed \(z\),(3) uses one fixed weight.

For every integer \(J\), the compact spatial transform and integration by parts in a coordinate of largest complex modulus give
\[
\begin{gathered}
|\widehat\chi_B(w)|
       \\
\le C_J B^d e^{2B|\operatorname{Im}w|}
                             (1+B|w|)^{-J}.
\end{gathered}
\tag{7}
\]
The factor \(B^d\) is its exact scaling factor. For \(|Bw|\le1\), use the compact integral bound; otherwise integrate \(J\) derivatives of \(\chi\), as in the [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md) full-complex decay proof. No real-frequency-only decay estimate is substituted for this bound.

Let \(R\) be the radius in the [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) strip theorem, and take \(J\ge m\). Since \(B\ge1\), the kernel in(6) is uniformly bounded for \(|\operatorname{Im}w|<R\) by
\[
 C B^d e^{2RB}\le C' e^{(2R+1)B}.
 \tag{8}
\]
The last inequality absorbs the fixed polynomial \(B^d\) into \(e^B\). The constants depend on the symbol and cutoff, not on the time weight or norm exponent. Taking the strip supremum and then the [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) estimate yields
\[
\begin{gathered}
\sup_{\xi\in\mathbb R^d}
        \|\mathcal F_xv(\xi,\cdot)\|^-_{p,k}
       \\
\le C_0 e^{\kappa_0 L}\int_{\mathbb R^d}F(\eta)\,d\eta,
 \\\kappa_0=\kappa_{\rm WE}+2R+1.
\end{gathered}
\tag{9}
\]
Here \(B\le L+1\), so its extra fixed exponential is absorbed into \(C_0\). Most importantly, \(C_0,\kappa_0\) are uniform over all time-only weights and all \(p\): the [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) estimate is uniform in them, the integral norm inequality has coefficient one and every comparison above is a pointwise symbol comparison.

## A modulated window allows an arbitrary joint weight

Now let \(k=k(\eta,s)\) be a joint moderate weight with constants \(C_k,N_k\). Choose a nonnegative \(\phi\in C_c^\infty(\mathbb R^d)\), supported in the unit ball, with \(\int\phi=1\). Thus \(\widehat\phi(0)=1\). For each real \(\eta\), set
\[
\begin{gathered}
\phi_\eta(x)=e^{ix\cdot\eta}\phi(x),\\
\qquad
 v_\eta=\phi_\eta*_xv,\\
\qquad
 \mathcal F_xv_\eta(\xi,t)
                    =\widehat\phi(\xi-\eta)\mathcal F_xv(\xi,t).
\end{gathered}
\tag{10}
\]
Tangential convolution commutes with \(P(D)\), so \(P(D)v_\eta=\phi_\eta*_xg\). All these functions are smooth and compactly supported; at negative times their spatial support lies inside the radius-\((L+1)\) ball.

Apply(9) to \(v_\eta\) with time-only weight \(k_\eta(s)=k(\eta,s)\). Its constants are uniform in \(\eta\), since they are uniform over time weights. Evaluate its left side at \(\xi=\eta\), where the window transform equals one. Moderation of the joint weight gives
\[
\begin{gathered}
V(\eta):\\
=\|\mathcal F_xv(\eta,\cdot)\|^-_{p,k_\eta}
 \\
\le C_1 e^{\kappa_0 L}\int_{\mathbb R^d}
     K(\eta-\xi)G(\xi)\,d\xi,
\end{gathered}
\tag{11}
\]
where
\(G(\xi)=\|\mathcal F_xg(\xi,\cdot)\|^-_{p,k_\xi/S_P(\xi,\cdot)}\)
and
\(K(h)=|\widehat\phi(-h)|(1+C_k|h|)^{N_k}\).
The scalar window factor comes out of the restriction norm by homogeneity. The weight comparison is uniform in \(s\) and retains the same \(S_P(\xi,s)\) on both sides. The factor \(e^{\kappa_0}\) from the window support is absorbed into \(C_1\).

The real Schwartz transform of \(\phi\) makes \(K\in L^1\), for any fixed moderation exponent. Young's \(L^1*L^p\) inequality and the exact [Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md) identity now give
\[
 \begin{aligned}
 \|v\|^-_{p,k}
  &=(2\pi)^{-d/p}\|V\|_p\\
  &\le C_1 e^{\kappa_0 L}\|K\|_1
                      (2\pi)^{-d/p}\|G\|_p\\
  &=C_1\|K\|_1 e^{\kappa_0 L}\|P(D)v\|^-_{p,k/S_P}.
 \end{aligned}
 \tag{12}
\]
This is valid at \(p=1,\infty\) as well as every intermediate exponent. The dependence on the weight is confined to the finite constant \(\|K\|_1\); it does not change \(\kappa_0\).

## Reducible polynomials and multiplicities

Factor \(P=cP_1\cdots P_\ell\), with \(c\ne0\) and each \(P_j\) irreducible, repeating factors with their multiplicities. Every analytic root of a factor is an analytic root of \(P\), so(1) passes to each factor with the same \(A\). The already written product derivative-norm lemma gives constants \(c_*,C_*>0\) such that
\[
\begin{gathered}
c_*\prod_j S_{P_j}\le S_{P_1\cdots P_\ell}
                       \le C_*\prod_jS_{P_j},\\
\qquad
 S_P=|c|S_{P_1\cdots P_\ell}.
\end{gathered}
\tag{13}
\]
Apply the irreducible estimate successively to \(v,P_1(D)v,\ldots,P_{\ell-1}(D)\cdots P_1(D)v\), with weights \(k,k/S_{P_1},\ldots,k/\prod_{j<\ell}S_{P_j}\). These are positive moderate weights. The intermediate differential operators preserve compact support and the negative-time spatial bound by locality. Their individual exponential coefficients depend only on their symbols, so their sum is independent of all the weights.

The final restriction norm uses \(k/\prod_jS_{P_j}\). By(13) it is bounded by a constant times the norm with weight \(k/S_{P_1\cdots P_\ell}\). Scalar norm homogeneity converts the resulting last term exactly to \(\|P(D)v\|^-_{p,k/S_P}\); the scalar \(c\) cancels its identical norm factor. This proves(2) for all nonzero \(P\). A nonzero constant has \(S_P=|P|\) and gives equality. Repetition introduces another valid factor estimate, not a distinct-root assumption.

In tangential dimension zero, the full norm is the one-dimensional norm. The [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) zero-dimensional argument proves the same estimate directly, with no cutoff or window. Thus that dimension is included with its stated convention.

## Exercises with complete solutions

**Exercise 1 — basic: the window normalization.** Explain why \(\phi(0)=1\) cannot replace \(\widehat\phi(0)=1\) in(10). Construct a smooth compact example with value one at zero and transform zero at zero.

**Solution.** Evaluation at the selected frequency \(\xi=\eta\) produces the multiplier \(\widehat\phi(0)=\int\phi\), not the physical-space value. Choose a smooth cutoff \(b\) supported in a small ball about zero with \(b(0)=1\) and positive integral. Choose a nonnegative smooth bump \(a\) in another small ball inside the unit ball, disjoint from zero, with positive integral. The function
\[
\begin{gathered}
\phi=b-\frac{\int b}{\int a}a
                 \\
\quad\text{satisfies}\\
\quad
                 \phi(0)=1,\\
\qquad \widehat\phi(0)=0.
\end{gathered}
\tag{14}
\]
At the selected frequency it would erase the very fiber being estimated. A valid window is obtained by dividing any nonnegative nonzero compact bump by its positive integral. Its modulation then shifts the transform by exactly \(\eta\), and tangential convolution has the product-transform identity with no extra Fourier factor.

**Exercise 2 — intermediate: constants versus exponential rate.** Show that the spatial scaling factor \(B^d\), \(B\ge1\), can be absorbed in \(e^B\) with a degree-dependent constant. Explain why a larger moderation exponent for the joint weight need not increase \(\kappa\).

**Solution.** For \(d\ge1\), differentiation gives
\[
\begin{gathered}
\frac{d}{dB}(B^de^{-B})
                   =B^{d-1}e^{-B}(d-B),\\
\qquad
 B^d\le d^de^{-d}e^B\\
\quad(B\ge1).
\end{gathered}
\tag{15}
\]
Its maximum on this interval occurs at \(B=d\), including the endpoint \(d=1\). Dimension zero permits the weaker constant one directly. Thus the one extra support exponential in(8) suffices regardless of the scaling polynomial.

The joint weight enters later through \(K(h)=|\widehat\phi(-h)|(1+C_k|h|)^{N_k}\). For every fixed \(N_k\), choose a Schwartz decay bound of order greater than \(N_k+d\). This proves a finite \(L^1\) norm for \(K\). Increasing \(N_k\) may increase that finite constant, but the window still has spatial radius one and the first-stage exponent \(\kappa_0\) was uniform over time weights. Therefore the same \(\kappa\) remains valid.

**Exercise 3 — advanced: repeated factors and the exact derivative norm.** For the one-variable symbol \(P(s)=(s-2i)^2\), calculate \(S_P(s)\) on the real axis and compare it to the product of the two first-order derivative norms. Explain its role in the repeated-factor step.

**Solution.** Put \(R(s)=s-2i\). For real \(s\), \(S_R(s)=\sqrt{s^2+5}\). The squared norm of \(P\) includes its value, first derivative \(2(s-2i)\) and second derivative \(2\):
\[
\begin{gathered}
S_P(s)^2\\
=(s^2+4)^2+4(s^2+4)+4\\
=(s^2+6)^2,\\S_R(s)^2=s^2+5.
\end{gathered}
\tag{16}
\]
Consequently \(S_P(s)=s^2+6\), while the product of the first-order norms is \(s^2+5\). Their ratio lies between one and \(6/5\). The product weight is comparable to the exact derivative norm and is not literally identical to it. Applying the first-order estimate twice gives the weight \(k/(s^2+5)\); this comparison converts it to the target weight \(k/(s^2+6)\) with a finite constant. Its constant root \(2i\) satisfies(1) with \(A=1\), and the one-variable half-line inverse gives the resulting bound with no spatial exponential.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.

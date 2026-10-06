# Curved weights and the directions in which support can end

A solution of an elliptic equation cannot always be treated as a real-valued harmonic function. Its leading coefficients may be complex, its order may exceed two, and its initially known derivatives may stop one order short of the equation. This lesson asks a geometric question that remains meaningful in that setting: at which covectors can the support of a solution have a supporting surface?

The answer is controlled by repeated roots after complexifying a real line in frequency space. We first make this condition geometric. Two finite algebraic calculations then produce a weighted estimate, with only one derivative of any coefficient. The estimate turns a gap between weight levels into vanishing. Finally, a root-count argument explains both the dimensional distinction for complex quadratic forms and the role of a single point with real coefficients.

## 1. Support geometry, coefficients, and entry assumptions

Throughout, \(X\) is open in \(\mathbb R^n\), \(n,m\geq1\), and
\[
 P_m(x,D)=\sum_{|\gamma|=m}a_\gamma(x)D^\gamma,\qquad
 p_x(z)=\sum_{|\gamma|=m}a_\gamma(x)z^\gamma,\qquad
 D_j=-i\partial_{x_j}.                                             \tag{S1}
\]
The coefficients are complex-valued and locally Lipschitz. Ellipticity means
\[
 p_x(\xi)\ne0\quad\text{for every real }\xi\ne0.                     \tag{S2}
\]
It does not require positivity, a real symbol, or absence of complex zeros. Estimates are local, so one may work on a fixed compact coefficient neighborhood with common ellipticity and Lipschitz bounds. All unlabelled norms below are \(L^2(dx)\) norms. We use \(H^k=W^{k,2}\) for nonnegative integers.

The following entry assumptions and exact earlier results specify the proof boundary.

* **Exterior normals.** We use the following normal-set definition. For a relatively closed \(F\subset X\), an exterior normal \((x_0,N)\) has \(x_0\in F\) and \(N\ne0\), and is witnessed locally by a real \(C^2\) function \(f\) with \(df(x_0)=N\) and \(f|_F\leq f(x_0)\). Write \(N_e(F)\) for these pairs, \(N_i(F)=-N_e(F)\) for reversal in the covector fiber, and \(\overline N(F)=\overline{N_e(F)\cup N_i(F)}\) in \(T^*X\setminus0\). We prove the local reductions and the elementary boundary consequence needed here. No analytic-wavefront theorem or propagation theorem from outside these prerequisite lessons is being assumed.
* **Calculus tools.** Finite-dimensional Taylor expansion with a second-order remainder, the smooth inverse-function theorem, compactness of closed bounded subsets of Euclidean space, and smooth cutoffs on nested relatively compact open sets are entry facts. Complex numbers have square roots. Smooth coordinate changes act on integer Sobolev spaces by the weak chain rule and change of variables; locally their derivative norms through a fixed order are bounded by the corresponding finite derivative norms and Jacobian bounds.
* **Lipschitz product rule** and **integration and weak derivatives** are the weak product, integration, density, and mollification assumptions stated in Section 1 of [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md). In particular a Lipschitz function has bounded weak first derivatives. We never differentiate a coefficient twice.
* **Fourier inversion and Plancherel**, in Sections 1–2 of [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md), give the Fourier convention and Plancherel identity used below.
* **Weak elliptic regularity**, in Sections 7–8 of [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md) gives the Lipschitz commutator and local weak elliptic regularity: \(u\in H^{m-1}_{\mathrm{loc}}\) and \(P_mu\in L^2_{\mathrm{loc}}\) imply \(u\in H^m_{\mathrm{loc}}\), for the coefficients and ellipticity in (S1)–(S2).

For clarity, the initially weak product in the last statement is
\[
 aD_jw=D_j(aw)-(D_ja)w,\qquad w\in L^2_{\mathrm{loc}}.             \tag{S3}
\]
To interpret a term \(a_\gamma D^\gamma u\) with \(|\gamma|=m\), apply (S3) to one derivative of \(D^{\gamma-e_j}u\). The independence of the chosen index is proved in Section 7 of [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md). Thus the equation below is meaningful at its stated initial regularity.

Define the exceptional set
\[
\begin{split}
 \mathcal E=\{(x,N)\in T^*X\setminus0:\;&
 p_x(\xi+zN)=0,\quad
 (N\cdot\partial_\xi)p_x(\xi+zN)=0\\
 &\text{for some }\xi\in\mathbb R^n,\ z\in\mathbb C,
       \ \xi+zN\ne0\}.
\end{split}                                                       \tag{S4}
\]
The coefficient of \(z^m\) is \(p_x(N)\ne0\), so the two equalities express precisely a root of multiplicity at least two in that line polynomial. A covector outside \(\mathcal E\) will be called admissible.

**Geometric lemma.** The set \(\mathcal E\) is closed in the punctured cotangent bundle, invariant under multiplication of \(N\) by every nonzero real number, and invariant under real coordinate changes.

**Proof.** A root in (S4) cannot be real: otherwise its argument is a nonzero real vector contradicting (S2). Absorb \(\operatorname{Re}z\) into \(\xi\), leaving an argument \(\eta+itN\), with \(\eta\) real and \(t\ne0\). By homogeneity we may normalize
\[
 |\eta|^2+t^2=1.                                                  \tag{S5}
\]
For a convergent sequence \((x_\nu,N_\nu)\in\mathcal E\) with nonzero limit covector \(N\), select a convergent subsequence of these normalized witnesses. The limiting argument \(\eta+itN\) is nonzero: if it were zero, real and imaginary parts would give \(\eta=0\), \(t=0\), contrary to (S5). Both polynomial equalities pass to the limit by coefficient continuity. This proves closedness, including possible root rescaling and real translation along \(N\).

Replacing \(N\) by \(cN\), \(c\in\mathbb R\setminus0\), replaces a root \(z\) by \(z/c\). For a smooth coordinate change, the cotangent transformation at each point is an invertible real linear map \(L\). The new principal polynomial is \(z\mapsto p_x(Lz)\). It sends \(\xi+zN\) to \(L\xi+zLN\), preserves its being nonzero, and preserves the multiplicity of the line root. This proves invariance. \(\square\)

The exclusion of the zero complex vector in (S4) matters. In dimension one, every homogeneous symbol is \(az^m\), \(a\ne0\); its only root along a real line gives the zero complex vector. Hence \(\mathcal E\) is empty in that dimension for every \(m\), including \(m>1\).

Here is the local form of a support normal. Translate \(x_0\) to zero. If \(f\) witnesses \(N_e(F)\), let \(f_2\) be its quadratic Taylor polynomial there and choose any \(\kappa>0\). On a sufficiently small neighborhood,
\[
 g(x)=f_2(x)-f(0)-\kappa|x|^2<0\quad(x\in F\setminus\{0\}),\qquad
 dg(0)=N.                                                        \tag{S6}
\]
Indeed \(f-f_2=o(|x|^2)\), so \(g\leq f-f(0)-\kappa|x|^2/2\) after shrinking. Complete \(g\) to smooth coordinates with last coordinate \(y_n=g(x)\). The inverse-function theorem applies because \(N\ne0\). In these coordinates
\[
 F\cap\{y_n\geq0\}\subset\{0\}.                                   \tag{S7}
\]
The transformation is smooth even though the original witness was only \(C^2\); using the polynomial in (S6) avoids imposing \(C^m\) regularity on that witness.

Under this transformation, the principal coefficients remain locally Lipschitz. The chain rule produces additional differential terms of orders below \(m\) with locally bounded coefficients. Norms of derivatives through \(m-1\) are locally comparable. Consequently an inequality
\[
 |P_mu|\leq C\sum_{|\alpha|<m}|D^\alpha u|                          \tag{S8}
\]
retains the same form, with a new local constant and the transformed principal part. This follows first for smooth functions by the chain rule and then for \(H^{m-1}\) functions using (S3) and smooth approximation. In particular the transformed principal part remains \(L^2_{\mathrm{loc}}\) when the original one was. These observations justify using (S7) in the continuation proof.

## 2. A frequency inequality with one normal derivative

Freeze the principal polynomial at an admissible point and use linear coordinates in which the covector is \(e_n\). Put \(p=p_0\) and \(p_n=\partial_{\xi_n}p\). Admissibility and ellipticity imply that the two polynomials
\[
 p(\xi+it e_n),\qquad t\,p_n(\xi+it e_n)
\]
have no simultaneous zero for real \((\xi,t)\ne0\). When \(t\ne0\), a common zero violates (S4); when \(t=0\), ellipticity excludes a zero of \(p(\xi)\).

The continuous homogeneous polynomial
\[
 B(\xi,t)=\sum_{|\alpha|\leq m}t^{2(m-|\alpha|)}|\xi^\alpha|^2
\]
has degree \(2m\). The continuous denominator
\(|p(\xi+it e_n)|^2+t^2|p_n(\xi+it e_n)|^2\) is positive on the real unit sphere in \(\mathbb R^{n+1}\). Its positive minimum and the maximum of \(B\) give
\[
 B(\xi,t)\leq C_0\bigl(|p(\xi+it e_n)|^2+
                   t^2|p_n(\xi+it e_n)|^2\bigr).                 \tag{S9}
\]
Homogeneity extends the inequality from the sphere to every point, and both sides vanish at zero. The polynomial is allowed to have arbitrary complex coefficients.

Write \(\bar p\) for coefficientwise complex conjugation; thus
\(\bar p(\xi-it e_n)=\overline{p(\xi+it e_n)}\) for real \(\xi,t\).
Plancherel and (S9) imply
\[
 E_t(v):=\sum_{|\alpha|\leq m}t^{2(m-|\alpha|)}\|D^\alpha v\|^2
 \leq C_0\bigl(\|\bar p(D-it e_n)v\|^2+
          t^2\|\bar p_n(D-it e_n)v\|^2\bigr)                      \tag{S10}
\]
for \(t>0\), \(v\in C_c^\infty(\mathbb R^n)\). The same conclusion holds with \(p,+it\) in place of \(\bar p,-it\). No frequency cutoff, boundary condition, or positivity of \(p\) enters this estimate.

## 3. A finite norm identity for a signed quadratic weight

Let \(Q(x)=a\cdot x+\frac12\sum_jb_jx_j^2\) be real, with the \(b_j\) of either sign. For a polynomial \(q\), let \(q^{(\alpha)}=\partial_\xi^\alpha q\). On compactly supported smooth functions introduce
\[
 A_j=D_j-\frac i2Q_j,\qquad B_j=D_j+\frac i2Q_j.                   \tag{S11}
\]
Their algebra is
\[
 [A_j,A_k]=[B_j,B_k]=0,\quad [A_j,B_k]=b_j\delta_{jk},\quad
 B_j^*=A_j.                                                       \tag{S12}
\]
The signs can be checked directly from \([D_j,h]=-i\partial_jh\). In particular the two cross terms in \([A_j,B_k]\) add to \(\partial_j\partial_k Q\).

**Reordering identity.** For any polynomials \(r,s\),
\[
 r(A)s(B)=\sum_\alpha\frac{b^\alpha}{\alpha!}
                   s^{(\alpha)}(B)r^{(\alpha)}(A).               \tag{S13}
\]
Only finitely many multiindices occur. For one variable, induction in \(k\), starting from \(AB^k=B^kA+kbB^{k-1}\), yields
\[
 A^\ell B^k=
 \sum_{j=0}^{\min(\ell,k)}
  \binom{\ell}{j}\frac{k!}{(k-j)!}b^j B^{k-j}A^{\ell-j}.
\]
Commutation between different coordinates permits multiplication of these identities. Linearity in the monomials of \(r,s\) gives (S13). Thus the formula is a finite algebraic identity, with no convergence argument or sign assumption on \(b\).

Take \(r=\bar q\), \(s=q\) and pair (S13) with \(v\). Since
\((q^{(\alpha)}(B))^*=\bar q^{(\alpha)}(A)\), it follows that
\[
 \|q(B)v\|^2=
       \sum_\alpha\frac{b^\alpha}{\alpha!}
                       \|\bar q^{(\alpha)}(A)v\|^2.              \tag{S14}
\]
If \(v=e^{Q/2}u\), the intertwining identity
\(q(B)v=e^{Q/2}q(D)u\) gives equivalently
\[
 \int|q(D)u|^2e^Q\,dx
 =\int|q(D+iQ'/2)v|^2\,dx
 =\sum_\alpha\frac{b^\alpha}{\alpha!}
                  \int|\bar q^{(\alpha)}(D-iQ'/2)v|^2\,dx.       \tag{S15}
\]
A shifted polynomial here always means composition of the indicated commuting first-order differential operators, including derivatives that strike \(Q'\). It is not ordinary substitution into a pointwise symbol followed by left quantization.

The signed identity and a lower bound drawn from it are different assertions. Negative \(b_j\) give negative summands in (S14), so dropping them is unjustified. For the weight used later,
\[
 \phi(x)=x_n+\frac12x_n^2,\qquad Q=2t\phi,\qquad t>0,              \tag{S16}
\]
all nonzero Hessian entries are nonnegative. Keeping the zeroth and first normal-derivative terms in (S14) then gives
\[
 \|\bar p(D-it\phi')v\|^2+
  2t\|\bar p_n(D-it\phi')v\|^2
 \leq\|p(D+it\phi')v\|^2.                                       \tag{S17}
\]
The coefficient \(2t\), rather than \(t^2\), is what will cost one power of the parameter in the final estimate.

## 4. Exchanging derivatives across a Lipschitz multiplier

For a complex \(L\)-Lipschitz function \(a\) on an open set and \(u,v\in C_c^\infty\) there, write
\[
 I_a(\alpha,\beta)=\int aD^\alpha u\,\overline{D^\beta v}\,dx,
 \qquad N=|\alpha|+|\beta|,\quad s=\max(|\alpha|,|\beta|).
\]
Then \(I_a(\alpha,\beta)-I_a(\beta,\alpha)\) is a sum of at most
\(\sum_j|\alpha_j-\beta_j|\leq N\) terms, up to signs, of the form
\[
 \int (D_ja)D^\mu u\,\overline{D^\nu v}\,dx,\qquad
 |\mu|+|\nu|=N-1,\quad |\mu|,|\nu|\leq s.                          \tag{S18}
\]
For \(\alpha=\beta\), it is the empty sum. In particular, if all products
\(\|D^\mu u\|\|D^\nu v\|\) with total order below \(N\) and individual orders at most \(s\) are at most \(M\), then
\[
 |I_a(\alpha,\beta)-I_a(\beta,\alpha)|\leq NLM.                    \tag{S19}
\]
If \(|\alpha|\ne|\beta|\), the individual upper bound on the derivative orders in (S18), and therefore in the condition defining \(M\), can be made strict: \(|\mu|,|\nu|<s\).

**Proof of the finite representation.** One integration by parts gives, for \(\alpha_j>0\),
\[
 I_a(\alpha,\beta)-I_a(\alpha-e_j,\beta+e_j)
   =-\int(D_ja)D^{\alpha-e_j}u\,\overline{D^\beta v}\,dx.          \tag{S20}
\]
A swap, which preserves the two total derivative orders, is more useful when those orders are equal. For \(\alpha_j,\beta_k>0\), put \(f=D^{\alpha-e_j}u\), \(g=D^{\beta-e_k}v\). Integrate once in each of the two terms; the derivatives \(D_jD_kg\) cancel. Thus
\[
\begin{split}
 &I_a(\alpha,\beta)-I_a(\alpha-e_j+e_k,\beta+e_j-e_k)\\
 &\qquad=-\int D^{\alpha-e_j}u\bigl[
 (D_ja)\overline{D^\beta v}
 -(D_ka)\overline{D^{\beta+e_j-e_k}v}\bigr]\,dx.
\end{split}                                                       \tag{S21}
\]
This formula costs two first derivatives of \(a\) in two different integrals, never a second derivative in one integral.

Let \(\gamma_j=\min(\alpha_j,\beta_j)\), and write
\(\alpha=\gamma+r\), \(\beta=\gamma+q\), where \(r,q\) have disjoint supports. Reverse the desired difference if necessary to arrange \(|r|\geq|q|\). Pair every index occurrence of \(q\) with an occurrence of \(r\). Perform the \(|q|\) corresponding swaps using (S21), then transfer the remaining \(|r|-|q|\) occurrences using (S20). The endpoint is \((\beta,\alpha)\). During the swaps both total orders are unchanged; during the transfers the larger decreases while the smaller increases to it. No intermediate order exceeds \(s\). Each error has total order \(N-1\). The number of errors is
\[
 2|q|+(|r|-|q|)=|r|+|q|
                =\sum_j|\alpha_j-\beta_j|\leq N.
\]
This proves (S18). For the strict refinement, assume \(|\alpha|=s>|\beta|=r\); reversal handles the opposite case. During each initial swap, the error orders are \(s-1\) and \(r\), both less than \(s\). During a subsequent transfer, the error's left order is at most \(s-1\), while its right order increases from \(r\) only as far as \(s-1\). Thus every error in this construction has both individual orders below \(s\) when the original orders are unequal. The weak integration-by-parts rule for a Lipschitz multiplier legitimizes every step. Cauchy–Schwarz and \(|D_ja|\leq L\) almost everywhere give (S19), including its refinement. \(\square\)

**Why the equal-order case differs.** If \(|\alpha|=|\beta|=s\), (S18) puts one factor at order \(s-1\) and permits the other at order \(s\). In general both factors cannot be required to have order below \(s\). The strict refinement is for unequal original orders. To check the obstruction at equal orders directly, let \(a=x_1\), \(\alpha=e_1\), \(\beta=e_2\), and
\[
 u=v=e^{ikx_2}f(x_1)g(x_2),\qquad
 0\ne f,g\in C_c^\infty(\mathbb R;\mathbb R).
\]
Then
\[
\begin{split}
 D_1u\,\overline{D_2u}-D_2u\,\overline{D_1u}
     &=-2ik f f'g^2,\\
 \int x_1(D_1u\,\overline{D_2u}-D_2u\,\overline{D_1u})\,dx
     &=ik\|u\|^2.
\end{split}                                                       \tag{S22}
\]
The second equality uses \(\int x_1ff'=-\frac12\int f^2\). A condition allowing only individual orders below one permits \(M=\|u\|^2\), whereas (S19) would then incorrectly bound \(|k|\) by two. The non-strict bound proved above is the one used below, and it supplies the needed parameter power.

## 5. From a linear weight to a curved one

Fix the weight (S16). For \(t\geq1\) and functions supported in a fixed bounded set, the two quantities
\[
 E_t(e^{t\phi}u)
 \quad\text{and}\quad
 \sum_{|\alpha|\leq m}t^{2(m-|\alpha|)}
                     \|e^{t\phi}D^\alpha u\|^2                  \tag{S23}
\]
are comparable with constants independent of \(t\). Indeed
\[
 e^{t\phi}D_ju=(D_j+it\phi_j)(e^{t\phi}u).
\]
Iterating this equality expresses each order-\(k\) weighted derivative as a sum of terms \(c(x)t^\ell D^\beta(e^{t\phi}u)\) with
\(\ell+|\beta|\leq k\), bounded \(c\), and finitely many terms. Multiplying by \(t^{m-k}\) and using \(t\geq1\) bounds it by the parameter norm. Iterating the reverse identity
\(D_j(e^{t\phi}u)=e^{t\phi}(D_j-it\phi_j)u\) proves the reverse bound. This also checks all derivatives of \(\phi_j\) that appear during the iteration.

Let \(A=D-it\phi'\) as in (S11) with \(Q=2t\phi\), and let \(A^0=D-it e_n\). We now transfer (S10) from \(A^0\) to \(A\). On a ball of radius \(\delta<1\),
\[
\begin{split}
 &\|(\bar p(A)-\bar p(A^0))v\|^2
 +t^2\|(\bar p_n(A)-\bar p_n(A^0))v\|^2
 \\
 &\qquad\leq C(1+\delta^2t^2)F_t(v),\\
 &F_t(v):=\sum_{|\alpha|\leq m-1}
                t^{2(m-|\alpha|)-2}\|D^\alpha v\|^2.
\end{split}                                                       \tag{S24}
\]
For \(m=1\), the derivative polynomial is constant and its difference is zero.

Here is a direct expansion proof of (S24). Move every ordinary derivative in a shifted monomial to the right. Its terms with no derivative on \(\phi'\) are the ordinary binomial expansion. Since \(\phi'=e_n+x_ne_n\), the difference of their coefficient factors is bounded by \(C\delta\). The top \(D^m\) term cancels. Hence these terms in the first difference are bounded in norm by \(C\delta tF_t(v)^{1/2}\). In the polynomial \(p_n\), the top order is \(m-1\) and again cancels in the difference; multiplying its bound by \(t\) gives the same bound \(C\delta tF_t(v)^{1/2}\). Any remaining term has had at least one derivative strike \(\phi'\). It therefore has the form \(ct^\ell D^\beta\), with \(\ell+|\beta|\leq m-1\) for \(p\), or at most \(m-2\) for \(p_n\). The coefficients and their required derivatives are bounded on the fixed ball; in fact \(\phi'\) is affine. These terms contribute at most \(CF_t(v)^{1/2}\), also after the factor \(t\) for \(p_n\). Squaring the finite sums proves (S24).

Combining (S10), (S24), and the elementary inequality
\(\|f+g\|^2\leq2\|f\|^2+2\|g\|^2\), gives
\[
 E_t(v)\leq C_1\bigl(\|\bar p(A)v\|^2+
                      t^2\|\bar p_n(A)v\|^2\bigr)
       +C_2(1+\delta^2t^2)F_t(v).                                \tag{S25}
\]
This retains the remainder with all orders below \(m\). Since
\(F_t\leq t^{-2}E_t\), choose \(\delta>0\) first with \(C_2\delta^2<1/4\), then \(t_0\geq1\) with \(C_2t_0^{-2}<1/4\). Absorption yields
\[
 E_t(v)\leq 2C_1\bigl(\|\bar p(A)v\|^2+
                       t^2\|\bar p_n(A)v\|^2\bigr),\qquad t\geq t_0.
                                                                    \tag{S26}
\]
Combine this with (S17) after division by \(t\). Because \(t^{-1}\leq1\),
\[
 S_t(v):=t^{-1}E_t(v)
 \leq C\|p(D+it\phi')v\|^2.                                     \tag{S27}
\]
Together with (S23), this is the constant-coefficient curved-weight estimate. Replacing the principal coefficients by close continuous coefficients directly in its right side would produce an error of size \(tS_t\), too large to absorb uniformly. The next argument uses the cancellation in the difference of two squared norms to recover the missing power.

## 6. The uniform estimate with Lipschitz coefficients

Assume that zero and \(e_n\) form an admissible pair for (S1). There are a ball \(V\) about zero, constants \(\varepsilon_0>0\), \(t_0\geq1\), and \(C\), such that
\[
 \sum_{|\alpha|\leq m}t^{2(m-|\alpha|)-1}
       \int|D^\alpha u|^2e^{2t\phi}\,dx
 \leq C\int|P_m(\varepsilon x,D)u|^2e^{2t\phi}\,dx                \tag{S28}
\]
for every \(u\in C_c^\infty(V)\), \(0<\varepsilon\leq\varepsilon_0\), and \(t\geq t_0\). The same \(C\) works on this full parameter range. In particular order \(m\) has coefficient \(t^{-1}\), order \(m-1\) has coefficient \(t\), and order zero has coefficient \(t^{2m-1}\).

**Proof.** The ball \(V\) is chosen inside the ball used for (S26). Set
\[
 P_\varepsilon(x,\xi)=P_m(\varepsilon x,\xi),\quad
 r_\varepsilon(x,\xi)=P_\varepsilon(x,\xi)-p(\xi),\quad
 B=D+it\phi',\quad A=D-it\phi'.                                  \tag{S29}
\]
The coefficient functions of \(r_\varepsilon\), together with their weak first derivatives on \(V\), are bounded by \(C\varepsilon\). This follows from local Lipschitz continuity, \(a_\gamma(\varepsilon x)-a_\gamma(0)=O(\varepsilon)\) on the bounded ball, and the chain rule. All variable coefficients stand to the left of the shifted monomials. In particular \(\bar P_\varepsilon(x,A)\) means coefficientwise conjugation with the indicated shift; it is not a formal adjoint, which would differentiate the variable coefficients.

We prove the quadratic-form comparison
\[
\begin{split}
 |\Delta_\varepsilon(v)-\Delta_0(v)|&\leq C\varepsilon S_t(v),\\
 \Delta_\varepsilon(v)&=
    \|P_\varepsilon(x,B)v\|^2-\|\bar P_\varepsilon(x,A)v\|^2.
\end{split}                                                       \tag{S30}
\]
This is the only step where first derivatives of principal coefficients are needed.

Put \(h=\phi'\). The part of \(P_\varepsilon(x,B)\) in which no derivative strikes \(h\) is
\[
 T_\varepsilon^+=\sum_{|\alpha|\leq m}
             t^{m-|\alpha|}c_{\alpha,\varepsilon}(x)D^\alpha,
 \quad
 c_{\alpha,\varepsilon}
 =\sum_{\substack{|\gamma|=m\\\gamma\geq\alpha}}
  \binom{\gamma}{\alpha}a_\gamma(\varepsilon x)
            i^{m-|\alpha|}h^{\gamma-\alpha}.                     \tag{S31}
\]
Since \(h\) is real, the corresponding part of \(\bar P_\varepsilon(x,A)\) has coefficients \(\bar c_{\alpha,\varepsilon}\). Expanding both squared norms and reversing \(\alpha,\beta\) in the second one expresses their difference as
\[
 \sum_{\alpha,\beta}t^{2m-|\alpha|-|\beta|}
  \int c_{\alpha,\varepsilon}\bar c_{\beta,\varepsilon}
   \bigl(D^\alpha v\,\overline{D^\beta v}
        -D^\beta v\,\overline{D^\alpha v}\bigr)\,dx.              \tag{S32}
\]
After subtracting its frozen version, the multiplier in each term becomes
\[
 c_{\alpha,\varepsilon}\bar c_{\beta,\varepsilon}
       -c_{\alpha,0}\bar c_{\beta,0},
\]
whose Lipschitz norm is \(O(\varepsilon)\). Apply the finite representation (S18). If \(N=|\alpha|+|\beta|\), every error is bounded by
\[
 C\varepsilon t^{2m-N}\|D^\mu v\|\|D^\nu v\|,
 \qquad |\mu|+|\nu|=N-1,\quad |\mu|,|\nu|\leq m.                  \tag{S33}
\]
Define \(w_\mu=t^{m-|\mu|-1/2}\|D^\mu v\|\). The product in (S33), without \(C\varepsilon\), is exactly \(w_\mu w_\nu\), which is bounded by \((w_\mu^2+w_\nu^2)/2\leq S_t(v)\).

For the remaining terms, a derivative has struck \(h\). Moving derivatives to the right gives monomials \(t^\ell c(x)D^\alpha\) with
\(\ell+|\alpha|\leq m-1\). This loss of one follows directly from
\([D_j,h_k]=-i\partial_jh_k\): the differentiated multiplier retains its parameter factor but consumes one derivative. At least one of the two factors in the squared norm has this loss. After subtracting the frozen expression, such a term has the form
\[
 t^\ell\int b(x)D^\alpha v\,\overline{D^\beta v}\,dx,\qquad
 \|b\|_\infty\leq C\varepsilon,\quad
 \ell+|\alpha|+|\beta|\leq2m-1,\quad |\alpha|,|\beta|\leq m.         \tag{S34}
\]
Its absolute value is at most \(C\varepsilon S_t(v)\), by the same weighted Cauchy inequality and \(t\geq1\). Every term has been included: two leading factors occur in (S32), while one or two factors with a derivative on \(h\) occur in (S34). There are finitely many terms depending only on \(n,m\). This proves (S30) without a second derivative of any principal coefficient.

By (S17), \(\Delta_0(v)\geq2t\|\bar p_n(A)v\|^2\). Consequently (S30) implies
\[
 \|\bar P_\varepsilon(x,A)v\|^2+
       2t\|\bar p_n(A)v\|^2
 \leq\|P_\varepsilon(x,B)v\|^2+C\varepsilon S_t(v).               \tag{S35}
\]
We also need the version of (S26) with \(\bar P_\varepsilon\) replacing \(\bar p\). Direct expansion of the shifted polynomial, with no coefficient differentiation, gives
\[
 \|\bar r_\varepsilon(x,A)v\|^2\leq C\varepsilon^2 E_t(v).         \tag{S36}
\]
Insert \(\bar p(A)=\bar P_\varepsilon(x,A)-\bar r_\varepsilon(x,A)\) in (S26). For small fixed \(\varepsilon_0\), absorb the resulting \(C\varepsilon^2E_t\) term. Dividing the result by \(t\) and using \(t^{-1}\leq1\), we obtain
\[
 S_t(v)\leq C_3\bigl(\|\bar P_\varepsilon(x,A)v\|^2+
                         t\|\bar p_n(A)v\|^2\bigr).              \tag{S37}
\]
Combine (S37) with (S35). Decrease \(\varepsilon_0\) once more so that \(C_3C\varepsilon_0\leq1/2\). This absorbs the error and proves
\[
 S_t(v)\leq 2C_3\|P_\varepsilon(x,D+it\phi')v\|^2.                \tag{S38}
\]
Finally put \(v=e^{t\phi}u\) and use (S23) and
\(P_\varepsilon(x,B)v=e^{t\phi}P_\varepsilon(x,D)u\). This proves (S28).

The order of choices is fixed coefficient neighborhood, sufficiently small ball for (S26), sufficiently large lower threshold \(t_0\), and sufficiently small fixed \(\varepsilon_0\) for the two coefficient absorptions. None of these choices makes \(\varepsilon\) depend on \(t\). Shrinking \(\varepsilon_0\) also ensures \(\varepsilon V\subset X\). \(\square\)

## 7. The support theorem at the initial Sobolev regularity

**Theorem.** Suppose (S1)–(S2) hold, \(u\in H^{m-1}_{\mathrm{loc}}(X)\), and the distribution \(P_mu\), interpreted using (S3), belongs to \(L^2_{\mathrm{loc}}(X)\). If locally
\[
 |P_mu|\leq C\sum_{|\alpha|<m}|D^\alpha u|\quad\text{almost everywhere},
                                                                    \tag{S39}
\]
then
\[
                  \overline N(\operatorname{supp}u)\subset\mathcal E.
                                                                    \tag{S40}
\]
It is enough that the constant in (S39) be available on each relatively compact neighborhood; one global constant is not required.

**Proof.** First consider an exterior normal \((x_0,N)\) of \(F=\operatorname{supp}u\). Suppose it is admissible. The coordinate reduction (S6)–(S7) and invariance of the assumptions let us take \(x_0=0\), \(N=e_n\), and
\[
               0\in F,\qquad F\cap\{x_n\geq0\}=\{0\}             \tag{S41}
\]
in the coefficient neighborhood. Choose one fixed sufficiently small \(\varepsilon>0\) allowed by (S28) and set \(u_\varepsilon(x)=u(\varepsilon x)\). Homogeneity of the principal part gives
\[
 P_\varepsilon(x,D)u_\varepsilon
       =\varepsilon^m(P_mu)(\varepsilon x),\qquad
 D^\alpha u_\varepsilon(x)=\varepsilon^{|\alpha|}
                                  (D^\alpha u)(\varepsilon x).  \tag{S42}
\]
These distributional equalities follow by change of variables and (S3).

Take \(B_r\Subset V\) from (S28), with \(r<1\), and a smooth cutoff \(\chi\) supported in \(B_r\), equal to one on a neighborhood of \(\overline B_{r/2}\). Put \(U=\chi u_\varepsilon\). The exact product formula is
\[
 P_\varepsilon U
 =\varepsilon^m\chi(P_mu)(\varepsilon x)
   +\sum_{0<|\beta|\leq m}\frac{D^\beta\chi}{\beta!}
                    P_\varepsilon^{(\beta)}(x,D)u_\varepsilon,
                                                                    \tag{S43}
\]
where the superscript differentiates only the polynomial frequency variable. Each term after the first has order at most \(m-1\) on \(u_\varepsilon\), so every term is in \(L^2\). On the region where \(\chi=1\), (S39) gives
\[
 |P_\varepsilon U|
       \leq C\sum_{|\alpha|<m}
                       \varepsilon^{m-|\alpha|}|D^\alpha U|.    \tag{S44}
\]

We justify using (S28) on this nonsmooth \(U\). Section 8 of [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md) first gives \(u_\varepsilon\in H^m_{\mathrm{loc}}\) from the two initial assumptions and Lipschitz ellipticity. Hence \(U\in H^m(\mathbb R^n)\) has support compactly contained in \(V\). Convolve its zero extension with smooth approximate identities. For small mollifier radius the approximants lie in \(C_c^\infty(V)\) and converge to \(U\) in \(H^m\). On a fixed compact neighborhood, coefficients and the weight and its derivatives are bounded for each fixed \(t\). Both sides of (S28) therefore converge. Thus (S28) holds for \(U\) for every \(t\geq t_0\). The approximation limit is taken at fixed \(t\); no uniform regularization in the large parameter is being presumed.

Let \(F_\varepsilon=\varepsilon^{-1}F\). The compact set
\[
 K=F_\varepsilon\cap\operatorname{supp}\chi
                         \cap\{|x|\geq r/2\}
\]
lies in \(x_n<0\) by (S41). Since \(|x_n|<1\),
\(\phi=x_n(1+x_n/2)<0\) there. If \(K\) is nonempty, compactness gives
\[
                         \sup_K\phi\leq-c<0.                    \tag{S45}
\]
If it is empty, there are no exterior error terms and any positive \(c\) will do. Distributional derivatives of \(u_\varepsilon\) are supported in \(F_\varepsilon\); after the regularity just established this is also a statement about their almost-everywhere representatives. Thus all contributions outside \(B_{r/2}\), including the cutoff errors in (S43), are supported where (S45) holds.

Taking square roots in (S28), and using equivalence of a finite sum of norms with the square root of the sum of their squares, yields
\[
 t^{1/2}\sum_{|\alpha|<m}\|e^{t\phi}D^\alpha U\|
       \leq C_4\|e^{t\phi}P_\varepsilon U\|.
\]
Here the smallest left coefficient among orders below \(m\) is \(t^{1/2}\). Split the right side into the region with \(\chi=1\), where (S44) applies, and its complement, where (S45) applies. Since \(\varepsilon\) is now fixed, there are constants \(C_5,C_6\), independent of \(t\), with
\[
 t^{1/2}\sum_{|\alpha|<m}\|e^{t\phi}D^\alpha U\|
 \leq C_5\sum_{|\alpha|<m}\|e^{t\phi}D^\alpha U\|
                                      +C_6e^{-ct}.              \tag{S46}
\]
For large \(t\), absorb the first right-hand term. In particular
\[
                  \|e^{t\phi}U\|\leq 2C_6t^{-1/2}e^{-ct}.       \tag{S47}
\]
For each \(d>0\), restrict to \(\{\phi\geq-c+d\}\) to obtain
\(\|U\|_{L^2(\{\phi\geq-c+d\})}\leq2C_6t^{-1/2}e^{-dt}\).
Let \(t\to\infty\), then take a countable union over positive \(d\) tending to zero. It follows that \(U=0\) on \(\{\phi>-c\}\). This set contains a neighborhood of zero, where \(\chi=1\). Scaling back shows \(u=0\) near the proposed support point, a contradiction.

We have proved \(N_e(F)\subset\mathcal E\). The set \(\mathcal E\) is invariant under \(N\mapsto-N\), so \(N_i(F)\subset\mathcal E\). Closedness of \(\mathcal E\) then proves (S40). \(\square\)

In particular the conclusion concerns the closure of both signs of the normal set. It neither assumes that the support boundary is smooth nor restricts to normals realized by a plane.

**Continuation on a connected domain.** If \(\mathcal E=\varnothing\), every solution in the theorem that vanishes on a nonempty open subset of a connected \(X\) vanishes on all of \(X\).

For completeness, a nonempty proper relatively closed set \(F\) in a connected open \(X\) has an exterior normal at some boundary point. Choose \(x_0\in\partial_XF\), a closed ball \(\overline B(x_0,r)\subset X\), and points \(y\notin F\) arbitrarily close to \(x_0\). For \(|y-x_0|<r/4\), choose a point \(z\) of \(F\cap\overline B(x_0,r)\) minimizing distance to \(y\); it exists by compactness. Since \(x_0\in F\), the distance is at most \(|y-x_0|<r/4\), and the minimizing point lies in \(B(x_0,r/2)\). In a neighborhood of \(z\), the function
\[
                         f(x)=-|x-y|^2
\]
has a maximum on \(F\) at \(z\), and \(df(z)=2(y-z)\ne0\). Thus \(N_e(F)\ne\varnothing\). Applying this observation to \(\operatorname{supp}u\), which is proper if \(u\) vanishes on a nonempty open subset, contradicts (S40) unless that support is empty. Connectedness is used only to ensure a boundary between a nonempty proper closed support and its nonempty complement.

## 8. Complex quadratic forms and the dimension distinction

The statements of this section require only continuous dependence of the principal coefficients. Lipschitz regularity is needed when applying Section 7 to a differential inequality.

Let \(q:\mathbb C^n\to\mathbb C\) be a homogeneous quadratic polynomial with \(q(\xi)\ne0\) for nonzero real \(\xi\). Fix real \(N\ne0\) and \(\xi\notin\mathbb RN\). The polynomial
\[
                        z\longmapsto q(\xi+zN)                  \tag{S48}
\]
has degree two because its leading coefficient is \(q(N)\ne0\). It has no real root, since \(\xi+zN\) is a nonzero real vector when \(z\) is real.

We will use continuity of its two roots as an unordered pair, counting multiplicity. This follows directly from the quadratic formula. For \(az^2+bz+c\), \(a\ne0\), the pair is
\[
 \left\{\frac{-b+\sqrt{b^2-4ac}}{2a},
         \frac{-b-\sqrt{b^2-4ac}}{2a}\right\}.                    \tag{S49}
\]
Near a nonzero discriminant one chooses either continuous local square root, with the choice merely interchanging the pair. Near a zero discriminant, the modulus of either square root tends to zero. Thus both roots tend to the double root. It follows in particular that the number of roots in the upper half-plane is locally constant as long as no root reaches the real axis. This proof does not require a global enumeration or a global branch of the square root.

**Root-placement lemma.** If \(n>2\), (S48) has one root in each open half-plane. If \(n=2\), its two roots are distinct unless \(q\) is the square of a complex linear form. The assertion with \(\xi\notin\mathbb RN\) is vacuous when \(n=1\).

**Proof.** For \(n>2\), the space \(\mathbb R^n\setminus\mathbb RN\) is connected. One elementary description is
\(\mathbb R\times(\mathbb R^{n-1}\setminus0)\) after choosing an orthogonal complement of \(N\). Two nonzero vectors in \(\mathbb R^{n-1}\), \(n-1\geq2\), can be joined by two line segments avoiding zero: choose an intermediate vector on neither of their lines. Therefore the upper-half-plane root count in (S48) is independent of \(\xi\). Replacing \(\xi\) by \(-\xi\) replaces the pair of roots by its negatives, because \(q(-\xi+zN)=q(\xi-zN)\). If the original upper count is \(k\), the new one is \(2-k\). Hence \(k=1\), proving the assertion and excluding a double root.

For \(n=2\), use the real basis \((\xi,N)\). If \(\lambda_1,\lambda_2\) are the roots of (S48), homogeneity gives the polynomial identity
\[
 q(s\xi+tN)=q(N)(t-\lambda_1s)(t-\lambda_2s).                     \tag{S50}
\]
It holds for \(s\ne0\) by dividing by \(s^2\), then for all complex \(s,t\) as a polynomial identity. A double root makes the right side the square of a linear form after taking a complex square root of \(q(N)\). Conversely a square form gives a double root on every such line, since its linear factor is nonzero on \(N\) by ellipticity. \(\square\)

If \(\xi\in\mathbb RN\), the only root of \(q(\xi+zN)\) produces the zero complex vector and is excluded in (S4). The lemma therefore gives the complete exceptional set for second order:
\[
 \mathcal E=\varnothing\quad(n=1\text{ or }n>2),\qquad
 \mathcal E=\bigcup_{\{x:\,p_x=\ell_x^2\}}
                      (T_x^*X\setminus0)\quad(n=2),              \tag{S51}
\]
where \(\ell_x\) is a complex linear form. To verify the entire fiber in the second formula, fix any \(N\ne0\) and choose \(\xi\notin\mathbb RN\). The factor \(\ell_x(N)\) is nonzero, and
\(z=-\ell_x(\xi)/\ell_x(N)\) is nonreal; a real value would give a nonzero real zero of \(p_x\). Its complex argument is nonzero by real independence of \(\xi,N\), so this is an allowed multiple root.

**Propagation of half-plane separation in the coefficient domain.** Suppose \(X\) is connected, \(p_x\) is a continuous family of complex elliptic quadratic forms, and \(p_{x_*}\) has real coefficients at at least one point \(x_*\in X\). Then
\[
                              \mathcal E=\varnothing             \tag{S52}
\]
throughout \(X\).

For \(n=1\) or \(n>2\), this is already (S51). In dimension two, fix any pair of linearly independent real covectors \(\xi,N\). At \(x_*\), (S48) has real coefficients, no real roots, and hence a conjugate pair with one root in each half-plane. The root count is locally constant in \(x\) by (S49) and ellipticity. A locally constant integer-valued function on connected \(X\) is constant, so the same separation holds at every \(x\). Thus no \(p_x\) can be a square, by (S50). This proves (S52). The argument requires neither real coefficients away from \(x_*\) nor a continuously chosen family of linear factors.

Another useful sufficient condition is \(\operatorname{Re}p_x(\xi)>0\) for every nonzero real \(\xi\). For a fixed \(x\), the path
\[
 q_s(\xi)=\operatorname{Re}p_x(\xi)
                      +is\operatorname{Im}p_x(\xi),\qquad 0\leq s\leq1
\]
stays elliptic because its real part stays positive. At \(s=0\) its line roots are a nonreal conjugate pair; the root-count argument along this interval gives one root in each half-plane at \(s=1\). Thus every normal is admissible, including in dimension two, without assuming a point with real coefficients in the original coefficient domain. The same reasoning works when a nonzero complex scalar multiple of the form has positive real part.

Combining (S52) with Section 7 gives the following precise consequence. For a connected domain, Lipschitz complex elliptic second-order principal coefficients that are real at one point, \(u\in H^1_{\mathrm{loc}}\), \(P_2u\in L^2_{\mathrm{loc}}\), and
\[
                    |P_2u|\leq C(|u|+|Du|)
\]
locally, vanishing on a nonempty open set implies vanishing everywhere. In dimensions other than two, the real-point condition can be omitted. This is continuation from an open set. A conclusion from vanishing to infinite order at a single point requires the additional singular-weight analysis developed in the next unit.

### The first-order consequence and its exact coefficient map

This is an editorial consequence of the support theorem, retaining its original weak equation and coefficient assumptions. It also identifies the dimensions in which a scalar first-order example can exist.

For \(m=1\), write the original symbol and its real coefficient map as
\[
 p_x(z)=\sum_{j=1}^n a_j(x)z_j,\qquad
 L_x:\mathbb R^n\longrightarrow\mathbb C,\quad
 L_x\xi=\sum_{j=1}^n a_j(x)\xi_j.                    \tag{S53}
\]
Ellipticity is exactly injectivity of this real linear map. Since \(\mathbb C\) has real dimension two, an elliptic scalar first-order symbol has \(n\leq2\). In dimension one the condition is precisely \(a_1(x)\ne0\). In dimension two retain its full real matrix, determinant and inverse:
\[
 \begin{split}
 M_x&=\begin{pmatrix}\operatorname{Re}a_1&\operatorname{Re}a_2\\
                     \operatorname{Im}a_1&\operatorname{Im}a_2\end{pmatrix},\\
 d_x&=\operatorname{Re}a_1\operatorname{Im}a_2
       -\operatorname{Re}a_2\operatorname{Im}a_1
       =\operatorname{Im}(\overline{a_1}a_2),\\
 M_x^{-1}&=\frac1{d_x}
          \begin{pmatrix}\operatorname{Im}a_2&-\operatorname{Re}a_2\\
                         -\operatorname{Im}a_1&\operatorname{Re}a_1\end{pmatrix}.
 \end{split}                                                    \tag{S54}
\]
The two-dimensional condition is exactly \(d_x\ne0\); multiplication verifies both inverse identities, with the original complex coefficients and determinant retained. This identifies the map to \(\mathbb C\) with the map to its two real coordinates rather than suppressing either component.

For every real \(N\ne0\), the line polynomial has
\[
 p_x(\xi+zN)=p_x(\xi)+zp_x(N),\qquad
 \frac{d}{dz}p_x(\xi+zN)=p_x(N)\ne0.                \tag{S55}
\]
It has no multiple root. Hence \(\mathcal E=\varnothing\) for every elliptic scalar first-order operator. On a connected open domain in either permitted dimension, let the original coefficients be locally Lipschitz, let \(u\in L^2_{\mathrm{loc}}\), and suppose the weak product (S3) gives \(P_1u\in L^2_{\mathrm{loc}}\) with \(|P_1u|\leq C|u|\) on each relatively compact neighborhood. The support theorem applies with exactly \(H^{m-1}=H^0=L^2\). Its connected-domain consequence proves that vanishing on any nonempty open subset forces \(u=0\) throughout the domain. No first derivatives are required as initial data: the operative weak regularity proof supplies them. In dimensions greater than two an injective \(L_x\) is impossible, so this scalar first-order elliptic class is empty there; no statement about systems is inferred.

## 9. Worked models and limits of the criterion

**A complex anisotropic operator with no real coefficients nearby.** In three dimensions consider
\[
 q(\xi)=\xi_1^2+(2+i)\xi_2^2+(3-2i)\xi_3^2.
\]
Its real part is positive on nonzero real \(\xi\), so it is elliptic. Section 8 implies that every real normal is admissible, even though the coefficients are complex. For \(N=e_3\) and \(\xi=e_1\), the root equation is \(1+(3-2i)z^2=0\); its roots are opposite nonreal numbers, illustrating the half-plane conclusion. A sufficiently small Lipschitz perturbation remains elliptic on a neighborhood: on the real unit sphere the perturbation in modulus can be made smaller than half the minimum of \(|q|\). The continuation theorem applies to that perturbed operator at the same initial \(H^1\) regularity.

**Two binary forms with different root counts.** Put
\[
 q_a(\xi_1,\xi_2)=(\xi_1+i\xi_2)(\xi_1+ai\xi_2),\qquad a>0.
\]
Each factor has no nonzero real zero, so \(q_a\) is elliptic. For \(N=e_1\), \(\xi=e_2\), its roots are \(-i\) and \(-ai\), both in the lower half-plane. They are distinct when \(a\ne1\); consequently every normal is still admissible for \(a\ne1\). At \(a=1\), the symbol is a square and every nonzero covector is exceptional. This continuous elliptic family shows that an empty exceptional set at one point of a coefficient family, by itself, need not persist. The real-point assumption in (S52) supplies the stronger invariant of one root in each half-plane.

An exceptional normal means that the estimate proved here is not supplied by this criterion. It is not an assertion that a nonzero solution with that support must exist. In particular (S51) classifies the criterion, not every possible unique-continuation theorem for a square operator.

**An order-four failure of the simple-root test.** In dimension at least two, let
\[
                         q(\xi)=\left(\sum_j\xi_j^2\right)^2.
\]
It is elliptic. Given \(N\ne0\), choose real \(\xi\perp N\), \(\xi\ne0\). The equation
\(\sum_j(\xi_j+zN_j)^2=|\xi|^2+z^2|N|^2=0\) has two nonreal roots, and each becomes a double root for \(q\). Hence every real normal is exceptional for this symbol. Ellipticity alone, even with real coefficients, does not remove the repeated-root obstruction in higher order. This also shows why the second-order conclusion cannot be silently promoted to arbitrary elliptic order.

**Checking the parameter loss in the simplest identity.** With \(q(\xi)=\xi_n\) and \(Q=2t\phi\), (S14) says
\[
 \|(D_n+it(1+x_n))v\|^2
       =\|(D_n-it(1+x_n))v\|^2+2t\|v\|^2.
\]
This exact calculation isolates the positive contribution from curvature. A purely linear weight has \(Q''=0\), so the two norms are equal and this positive term disappears. The example diagnoses the mechanism without claiming that \(D_n\) is elliptic in dimensions greater than one.

## 10. Problems with complete solutions

**Problem 1: invariance under a nonorthogonal change of variables.** In the plane let
\(q(\xi)=\xi_1^2+2\xi_2^2\) and \(L=\begin{pmatrix}1&2\\0&1\end{pmatrix}\).
Compute the transformed symbol \(q_L(\eta)=q(L\eta)\). Show directly that it is elliptic and explain why its normals are admissible.

**Solution.** The transformed symbol is
\[
 q_L(\eta)=(\eta_1+2\eta_2)^2+2\eta_2^2
          =\eta_1^2+4\eta_1\eta_2+6\eta_2^2.
\]
For real \(\eta\), vanishing of this sum of nonnegative terms gives \(\eta_2=0\) and then \(\eta_1=0\). Thus it is elliptic. Its coefficients are real, so its line roots for independent real \(\xi,N\) form a nonreal conjugate pair. They are distinct and no normal is exceptional. Equivalently, the invertible real map \(L\) carries the entire line \(\xi+zN\) to \(L\xi+zLN\) and preserves its root multiplicities. Orthogonality is not needed.

**Problem 2: a signed Hessian cannot be discarded.** Use (S14) for \(q(\xi)=\xi_1\) and \(Q(x)=-x_1^2/2\). Determine the exact relation between the two shifted norms and show that the inequality obtained by discarding the Hessian term has the wrong direction for nonzero \(v\).

**Solution.** Here \(b_1=-1\), \(Q_1=-x_1\),
\(B_1=D_1-ix_1/2\), and \(A_1=D_1+ix_1/2\). The only polynomial derivatives are \(q\) and \(q'=1\). Thus
\[
                 \|B_1v\|^2=\|A_1v\|^2-\|v\|^2.
\]
For nonzero compactly supported \(v\), this is strictly less than \(\|A_1v\|^2\). The signed equality remains correct; a lower bound retaining only the zeroth summand is false. The absolute value of a signed coefficient may not be inserted into an identity of quadratic forms.

**Problem 3: count derivative transfers without exceeding the top order.** For
\(\alpha=(2,1)\), \(\beta=(0,2)\), exhibit a sequence of swaps and transfers from \((\alpha,\beta)\) to \((\beta,\alpha)\). Record the number and orders of the error integrals.

**Solution.** Remove the common index \((0,1)\); the remaining lists are two occurrences of index 1 on the left and one occurrence of index 2 on the right. Swap one occurrence to pass from
\[
 ((2,1),(0,2))\quad\text{to}\quad((1,2),(1,1)).
\]
Formula (S21) gives two errors with left order two and right order two. Transfer the remaining left index 1 using (S20), arriving at
\[
 ((0,2),(2,1)).
\]
This adds one error with orders two and two. There are three errors, equal to \(|2-0|+|1-2|\), each of total order four, one below the original total five. Both individual orders are at most the original maximum three. Thus the bound \(5LM\) from (S19) holds, and the particular algorithm improves its prefactor to \(3LM\).

**Problem 4: read every power in an order-three estimate.** Write (S28) for \(m=3\) by derivative order. Suppose the equation satisfies the locally bounded lower-order inequality. Which coefficient makes absorption of its order-two terms possible? Does the estimate require initially knowing all third derivatives?

**Solution.** With \(\nabla^j\) denoting the finite derivative array, the left side, up to equivalent choices of its finite-dimensional norm, is
\[
 t^5\|e^{t\phi}u\|^2+
 t^3\|e^{t\phi}\nabla u\|^2+
 t\|e^{t\phi}\nabla^2u\|^2+
 t^{-1}\|e^{t\phi}\nabla^3u\|^2.
\]
The squared lower-order right side is bounded by a constant times the sum of the first three derivative norms without these growing weights. The smallest growing coefficient among them is \(t\), on the second derivatives; choose \(t\) sufficiently large to absorb it and all lower orders. For support continuation the initial assumption is \(u\in H^2_{\mathrm{loc}}\) and \(P_3u\in L^2_{\mathrm{loc}}\), not \(H^3_{\mathrm{loc}}\). Section 8 of [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md) supplies the third derivatives before the compact cutoff is approximated. Replacing that step by an unproved application of the smooth Carleman estimate would leave a regularity gap.

**Problem 5: distinguish a vanishing open set from a vanishing jet.** Let a second-order operator satisfy the assumptions of (S52) and have Lipschitz coefficients. A solution of the local inequality vanishes in one ball in a connected \(X\). Prove that it vanishes on \(X\). Explain why the same proof, as written, does not begin from a zero Taylor jet at an isolated point.

**Solution.** Formula (S52) makes \(\mathcal E\) empty. If the support were nonempty, it would be a proper relatively closed subset of \(X\), since the given ball lies outside it. The nearest-point construction after (S47) supplies an exterior normal, contradicting (S40). Therefore the support is empty. In contrast, a function can vanish to every order at one point while having that point in the interior of its support; for example \(e^{-1/|x|^2}\), extended by zero at zero, has full support on a ball. This example is a statement about support geometry, not a solution counterexample for the given operator. The support argument has no initial nonempty open complement from a vanishing jet alone. A singular Carleman weight is needed for that separate implication.

## References

In particular, Section 4 proves the strict derivative-order refinement for unequal original orders and gives an independent equal-order example showing why that distinction matters.

Daniel Tataru's [*Carleman estimates, unique continuation and applications* (1998 notes)](https://math.berkeley.edu/~tataru/papers/book.pdf), Theorems 3.2–3.3 on pages 51–53, give a route from strong pseudoconvexity to elliptic estimates and continuation. The coefficient class there is \(C^1\); the proof uses the quadratic-form estimate in Theorem 2.7 and the regularization statement in Theorem 2.8. These notes provide a useful comparison of mechanisms, but do not replace the Lipschitz finite-algebra proof above. The [author's listing](https://math.berkeley.edu/~tataru/ucp.html) identifies the notes as unfinished.

Herbert Koch and Daniel Tataru's [*Carleman estimates and unique continuation for second order elliptic equations with nonsmooth coefficients*](https://math.berkeley.edu/~tataru/papers/esucp3.pdf), author-hosted version dated 26 December 2007, addresses strong continuation with substantially less bounded lower-order data. Theorem 1, conditions (4), (6), and (7), and the weighted estimates of §3 specify its metric and potential assumptions. It concerns second-order divergence-form operators with positive metrics; those statements are not a substitute for the arbitrary-order complex-symbol result here. Its proof develops different weighted spaces and a choice of weight adapted to the function and gradient potentials.

### Further questions

Three mathematical routes now separate naturally. One can study complex root collisions and ask when additional structure restores continuation beyond (S4); this requires a new argument, since being exceptional is not itself a nonuniqueness theorem. One can replace bounded lower-order coefficients by scale-sensitive integrability assumptions and compare the precise potential spaces in Koch–Tataru. Or one can turn from a support boundary to an isolated point and build singular weights to exploit infinite-order vanishing. These lead to different questions and require different arguments.

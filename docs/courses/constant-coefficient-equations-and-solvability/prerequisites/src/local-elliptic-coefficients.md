# Local inverses and distance-weighted elliptic estimates

**AN-03 · Unit AN03-U006 · Independent English AI draft, not admitted.**

Ellipticity gives a local inverse with exactly as many derivatives as the order of the operator. The useful question here is how little regularity its coefficients may have. Continuity will suffice for the highest-order coefficients. Lower-order coefficients can be unbounded; their admissible integrability depends on how many derivatives separate their term from the principal part.

We first build a constant-coefficient solver and record its quantitative bounds. Multiplication estimates then determine the coefficient assumptions. A separate localization argument gives estimates on arbitrary open subsets of one fixed neighborhood, with constants independent of the subset. Finally, a commutator argument supplies the missing highest derivatives when the equation is initially defined only as a distribution.

## AN03-LCE-001 — Conventions and prerequisite contracts

Let \(n,m\geq1\) be integers and \(1<p<\infty\). The order \(m\) is arbitrary. Coefficients and functions may be complex-valued. We use the Fourier convention of AN03-DEP-001 in *Prerequisite bridges*:

\[
D_j=-i\partial_j,\qquad
\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,\qquad
\mathcal F^{-1}h(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}h(\xi)\,d\xi.
\]

The space \(W^{s,p}(V)\), for a nonnegative integer \(s\), consists of distributions whose derivatives of orders at most \(s\) belong to \(L^p(V)\). We write \(\nabla^j u\) for the finite array \((D^\alpha u)_{|\alpha|=j}\), using its pointwise \(\ell^p\) norm inside an \(L^p\) norm. Switching to the sum of the component norms changes only constants depending on \(n,m,p\).

The following are precise imports, rather than additional conclusions of this unit.

* **DEP-LCE-DIST:** Distributions carry the usual test-function topology. Multiplication by a smooth function and distributional differentiation are continuous operations. A distribution supported in a compact set has finite order: after inserting a fixed cutoff near its support, its pairing is bounded by a constant times finitely many suprema of derivatives of the test function on a fixed compact neighborhood. It therefore acts on smooth functions through that cutoff and is tempered. Convolution is defined when one factor is compactly supported; differentiation transfers between its factors, and associativity holds in the uses here where all but at most one factor are compactly supported. Convolution of a tempered distribution with a compactly supported distribution is tempered. A smooth kernel paired with a compactly supported distribution gives a smooth function, also locally when all relevant kernel arguments stay away from its singular set. Fourier inversion of a compactly supported distribution is smooth, with derivatives obtained by differentiating its exponential pairing.
* **DEP-LCE-LP:** Lebesgue integration, Hölder and Young inequalities, Tonelli, dominated and monotone convergence; completeness of \(L^p\); density of \(C_c^\infty(\mathbb R^n)\) in \(L^p\) for finite \(p\); translation continuity and convergence of smooth approximate identities in these spaces. Locally, smooth approximation holds in integer \(W^{s,p}\). A distribution represented by an \(L^p\) limit has the corresponding distributional derivatives. These are the basic integration and weak-derivative prerequisites, not a new introductory distribution course.
* **DEP-LCE-MULT:** If \(b\in C^{n+2}(\mathbb R^n\setminus\{0\})\) and
  \[
  \max_{|\beta|\leq n+2}\sup_{\xi\ne0}
  |\xi|^{|\beta|}|\partial_\xi^\beta b(\xi)|\leq B,
  \]
  then \(b(D)\) extends from Schwartz functions to \(L^p(\mathbb R^n)\), with norm at most \(C_{n,p}B\). The precise independent reading is Terence Tao, *Lecture Notes 4 for 247A*, Theorem 4.4, printed/PDF pages 19–20; its singular-integral implication is Corollary 2.10, pages 8–9. This contract imports the multiplier theorem, including its dependence on finitely many symbol bounds.
* **DEP-LCE-FRAC:** For \(0<s<n\), \(1<p<q<\infty\), and \(1/q=1/p-s/n\), convolution with \(|x|^{s-n}\) maps \(L^p(\mathbb R^n)\) to \(L^q(\mathbb R^n)\). The precise independent reading is Tao, *Lecture Notes 2 for 247A*, Corollary 6.3, page 16, with Proposition 6.1 on page 15. No strong \(L^\infty\) endpoint is included.
* **DEP-LCE-LIP:** A Lipschitz scalar function has weak first derivatives in \(L^\infty\), bounded by its Lipschitz constant, and satisfies the weak product rule with smooth functions. This local fact also permits integration by parts against compactly supported smooth functions. It will be used only in the weak-coefficient part.

There is also an earlier **constant-strength antecedent, DEP-LCE-CS**: Hörmander, *The Analysis of Linear Partial Differential Operators II*, Theorem 13.2.1. For an operator with nonzero frozen symbol, continuous coefficients and constant strength near a point, it provides a local \(L^2\) right inverse, a left inverse on compactly supported smooth functions, and bounded \(Q(D)E\) when the constant-coefficient operator \(Q\) is weaker than the frozen operator. In this terminology, write
\(\widetilde q(\xi)^2=\sum_\beta|\partial_\xi^\beta q(\xi)|^2\);
“weaker” means \(\widetilde q\leq C\widetilde p\), and constant strength means pairwise comparability of the frozen \(\widetilde p_x\). This antecedent has an explicit dependency on that volume's constant-coefficient inverse theorem 10.3.7. It is not an already closed result of this course and does not supply the rough lower-coefficient \(L^p\) theorem below. We give the elliptic construction needed here directly, leaving the more general constant-strength contract separate.

The equation in DEP-LCE-CS has a specific interpretation. The finite-dimensional weaker-operator representation is
\(P(x,D)=P_0(D)+\sum_{\nu=1}^r c_\nu(x)P_\nu(D)\), with \(P_0\) the frozen operator, \(P_\nu\) weaker than \(P_0\), and continuous \(c_\nu\) vanishing at the frozen point. Define \(PEf=P_0Ef+\sum_\nu c_\nu P_\nu Ef\). Each \(P_\nu Ef\), including \(P_0Ef\), belongs to \(L^2\) by the stated operator bounds; after shrinking the neighborhood, its product with \(c_\nu\) is an \(L^2\) function. This is the interpretation in the first remark following Theorem 13.2.1, not multiplication of arbitrary distributions by continuous coefficients.

The proofs below supply the fundamental solution, the local Hölder multiplier bound, the perturbation argument, the distance-weighted estimate, and the Lipschitz commutator. The Banach-space geometric-series argument is also available in AN03-FRE-003 of *Finite defects under perturbation*; we recall its short application where it is needed.

## AN03-LCE-002 — A frozen solver without a restriction on dimension or order

Let \(q(\xi)\) be homogeneous of degree \(m\), with

\[
|q(\xi)|\geq c|\xi|^m\quad(\xi\in\mathbb R^n).                 \tag{L1}
\]

Choose \(\chi\in C_c^\infty(\mathbb R^n)\), equal to one for \(|\xi|\leq1/2\) and zero for \(|\xi|\geq1\). Set

\[
b_0(\xi)=\frac{1-\chi(\xi)}{q(\xi)},\qquad F_0=\mathcal F^{-1}b_0.
                                                                    \tag{L2}
\]

The quotient is smooth across zero because its numerator vanishes there. Repeated differentiation of a reciprocal, or induction in the identity \(q/q=1\), gives

\[
|\partial^\beta b_0(\xi)|\leq C_\beta(1+|\xi|)^{-m-|\beta|}.
                                                                    \tag{L3}
\]

In particular \(F_0\) is tempered and
\(q(D)F_0=\delta+\omega\), where \(\omega=-\mathcal F^{-1}\chi\) is Schwartz.

Here is an exact fundamental solution. When \(m<n\), the locally integrable function \(1/q\) defines a tempered distribution \(T\). When \(m\geq n\), put \(L=m-n\) and define, for \(\varphi\in\mathcal S\),

\[
\langle T,\varphi\rangle=
\int_{\mathbb R^n}\frac{\displaystyle\varphi(\xi)-\chi(\xi)
  \sum_{|\beta|\leq L}\frac{\partial^\beta\varphi(0)}{\beta!}\xi^\beta}
 {q(\xi)}\,d\xi.                                                   \tag{L4}
\]

Taylor's theorem bounds the numerator by \(C|\xi|^{L+1}\) near zero. Its quotient is integrable there, since the radial power after including the volume element is \(n-1-m+L+1=0\). At infinity, Schwartz decay applies. These same estimates, in terms of finitely many Schwartz seminorms, prove that \(T\) is tempered. As \(L<m\), all derivatives of \(q\varphi\) of orders at most \(L\) vanish at zero. Consequently \(qT=1\). Thus

\[
G=\mathcal F^{-1}T,\qquad q(D)G=\delta.                            \tag{L5}
\]

Moreover, \(T-b_0\) is supported in \(\operatorname{supp}\chi\). Its inverse Fourier transform \(H=G-F_0\) is smooth: on a fixed compact frequency set one may differentiate the exponential in its distributional pairing any number of times. Those differentiated pairings depend continuously on \(x\), by the finite-order bound for a compactly supported distribution. This proves smoothness, without assuming that \(G\) is an ordinary homogeneous function. In the dimensions where logarithmic terms occur, (L4) includes them automatically.

We need two kernel estimates. Fix \(|\alpha|=j\leq m\) and put \(k=m-j\). The symbol of \(D^\alpha F_0\) is \(\xi^\alpha b_0(\xi)\). With
\(\psi(\xi)=\chi(\xi/2)-\chi(\xi)\), its decomposition into annuli has inverse transforms

\[
K_\ell(x)=2^{\ell(n-k)}\kappa_\alpha(2^\ell x),\quad
\kappa_\alpha=\mathcal F^{-1}\!\left(\psi(\xi)\frac{\xi^\alpha}{q(\xi)}\right),
\quad \ell=0,1,\ldots.                                             \tag{L6}
\]

The function \(\kappa_\alpha\) is Schwartz. Indeed its Fourier transform is smooth with compact support away from zero; multiplication by powers of \(x\) in the inverse transform is integration by parts. The telescoping identity \(\sum_{\ell\geq0}\psi(2^{-\ell}\xi)=1-\chi(\xi)\) proves (L6) in tempered distributions. For every integer \(N\),

\[
|K_\ell(x)|\leq C_N2^{\ell(n-k)}(1+2^\ell|x|)^{-N}.              \tag{L7}
\]

If \(k>0\), then \(\sum_\ell\|K_\ell\|_1\leq C\sum_\ell2^{-\ell k}<\infty\). It therefore represents an \(L^1\) kernel. Splitting the sum at \(2^\ell|x|=1\) gives, for \(0<|x|\leq1\),

\[
|D^\alpha F_0(x)|\leq C
\begin{cases}
|x|^{k-n},&0<k<n,\\
1+|\log|x||,&k=n,\\
1,&k>n.
\end{cases}                                                       \tag{L8}
\]

For example the terms below the splitting point form a geometric sum when \(k\ne n\); when \(k=n\), their number is at most \(C(1+|\log|x||)\). Terms above the splitting point form a convergent geometric tail if \(N>n-k\). When \(|x|\geq1\), (L7), with \(N\) as large as desired, gives rapid decay. These arguments also prove smoothness away from zero by differentiating (L7). In particular,

\[
D^\alpha F_0\in L^r_{\mathrm{loc}}
\quad\hbox{if}\quad k>n(1-1/r),\qquad 1\leq r\leq\infty.          \tag{L9}
\]

For \(r<\infty\) this follows by integrating \(\rho^{r(k-n)+n-1}\); the logarithmic case is integrable to every finite power. The stated condition for \(r=\infty\) is \(k>n\). No assertion that a highest derivative is an integrable kernel is being made. When \(k=0\), its boundedness on \(L^p\) follows from DEP-LCE-MULT and (L3).

For \(0<k<n/p\), (L8), its decay at infinity, and DEP-LCE-FRAC give the finite endpoint

\[
\|D^\alpha F_0*g\|_q\leq C\|g\|_p,
\qquad \frac1q=\frac1p-\frac{k}{n}.                              \tag{L10}
\]

Together with the multiplier case \(k=0,q=p\), this is the global endpoint estimate whenever the displayed \(q\) is finite. For strictly larger \(1/q\), Young's inequality applies to a localized kernel: choose \(r\) by \(1+1/q=1/p+1/r\) and use (L9). This includes \(q=\infty\) precisely when \(k>n/p\). Interpolation with, or the finite-measure inclusion from, the finite endpoint handles the other \(p\leq q<\infty\).

Consequently, if \(V\subset B_1\), extend \(g\in L^p(V)\) by zero and define
\(S_Vg=(G*g)|_V\). For every \(j\leq m\),

\[
\|D^\alpha S_Vg\|_{L^q(V)}\leq C\|g\|_{L^p(V)},\qquad
p\leq q\leq\infty,\quad
\frac1q\geq\frac1p-\frac{k}{n},                                  \tag{L11}
\]

where the last inequality must be strict if \(q=\infty\). The constant is independent of the particular \(V\subset B_1\), with the frozen polynomial and the chosen exponents fixed. To verify the smooth correction, all arguments \(x-y\), for \(x,y\in V\), lie in \(B_2\); hence each derivative of \(H\) is bounded there and its convolution is bounded by \(C\|g\|_1\leq C|B_1|^{1-1/p}\|g\|_p\). Its \(L^q(V)\) norm has the required uniform bound. The same reasoning localizes the kernels in the strict Young estimates.

Both inverse identities are exact:

\[
q(D)S_Vg=g\text{ in }V,\qquad S_Vq(D)v=v\quad(v\in C_c^\infty(V)).
                                                                    \tag{L12}
\]

For the first, convolve (L5) with the compactly supported distribution given by the zero extension of \(g\). For the second, differentiation may be transferred to the compactly supported smooth factor: \(G*q(D)v=(q(D)G)*v=v\).

For completeness, any other fundamental solution differs from \(G\) by a smooth function. If \(q(D)w=0\), take a cutoff \(\eta\) equal to one near any prescribed compact set. Then
\[
\eta w=F_0*q(D)(\eta w)-\omega*(\eta w).
\]
Here \(q(D)(\eta w)=[q(D),\eta]w\) has compact support away from that set. The first convolution is smooth near the set because \(F_0\) is smooth away from zero; the second is smooth because \(\omega\) is smooth and \(\eta w\) has compact support. This proves the assertion locally everywhere. It also explains the smooth-remainder assertion for a regularized inverse with a different low-frequency cutoff.

## AN03-LCE-003 — A parameter in the constant-coefficient estimate

**Lemma.** For a homogeneous elliptic \(q\) of degree \(m\),

\[
\sum_{|\alpha|\leq m} A^{m-|\alpha|}\|D^\alpha v\|_p
\leq C\bigl(\|q(D)v\|_p+A^m\|v\|_p\bigr),\qquad A>0,\quad
v\in W^{m,p}(\mathbb R^n).                                        \tag{L13}
\]

The constant is independent of \(A\). It can also be chosen uniformly when \(q\) ranges over a compact set of homogeneous elliptic polynomials of degree \(m\).

**Proof.** At \(A=1\), the Fourier identity \(q b_0=1+\widehat\omega\) gives
\[
D^\alpha v=(D^\alpha F_0)*q(D)v-(D^\alpha\omega)*v.                \tag{L14}
\]
It holds first on Schwartz functions. Each first operator is bounded on \(L^p\) by the multiplier contract for top order, and by the \(L^1\) kernel estimate for lower orders. The second kernel is Schwartz. Smooth cutoff and mollification approximate any \(W^{m,p}\) function in that norm, so the identity and estimate extend to the stated domain. For \(w(y)=v(y/A)\), the derivative norm is
\(\|D^\alpha w\|_p=A^{n/p-|\alpha|}\|D^\alpha v\|_p\),
while homogeneity gives
\(\|q(D)w\|_p=A^{n/p-m}\|q(D)v\|_p\).
Apply the estimate at one and multiply by \(A^{m-n/p}\).

Finally, a compact family of elliptic polynomials has a positive common minimum of \(|q(\theta)|\) on the unit sphere. Its coefficients are bounded. The reciprocal differentiation identity bounds every required derivative in (L3) uniformly; the integrations by parts and the multiplier theorem use only finitely many of these bounds. The same \(C\) therefore works for the family. \(\square\)

## AN03-LCE-004 — The coefficient table and a local inverse in \(L^p\)

Consider
\[
P=\sum_{|\alpha|\leq m}a_\alpha(x)D^\alpha,
\qquad P_m=\sum_{|\alpha|=m}a_\alpha(x)D^\alpha                     \tag{L15}
\]
near zero. Assume that the coefficients of \(P_m\) are continuous and its frozen symbol
\(q(\xi)=\sum_{|\alpha|=m}a_\alpha(0)\xi^\alpha\) is elliptic. For every lower-order term set \(k=m-|\alpha|>0\) and require the following local integrability.

| Derivative gap \(k\) | Coefficient space \(L^{r_\alpha}_{\rm loc}\) | Exponent used for \(D^\alpha S_Vg\) |
| --- | --- | --- |
| \(k<n/p\) | \(r_\alpha=n/k\) | \(1/q_\alpha=1/p-k/n\) |
| \(k=n/p\) | \(r_\alpha=p+\varepsilon_\alpha\), some \(\varepsilon_\alpha>0\) | \(q_\alpha=p(p+\varepsilon_\alpha)/\varepsilon_\alpha\) |
| \(k>n/p\) | \(r_\alpha=p\) | \(q_\alpha=\infty\) |

There are finitely many coefficients, so different positive \(\varepsilon_\alpha\) cause no difficulty. At the critical gap any finite \(q_\alpha\) is allowed by (L11). The table gives \(1/p=1/r_\alpha+1/q_\alpha\) in every row.

**Theorem.** Every sufficiently small open neighborhood \(V\) of zero has a linear operator \(E:L^p(V)\to L^p(V)\) satisfying

\[
PEf=f\quad(f\in L^p(V)),\qquad EPv=v\quad(v\in C_c^\infty(V)),     \tag{L16}
\]

and, simultaneously for all \(|\alpha|\leq m\),

\[
D^\alpha E:L^p(V)\longrightarrow L^q(V)\text{ bounded if }
p\leq q\leq\infty,\quad
\frac1q\geq\frac1p-\frac{m-|\alpha|}{n},                           \tag{L17}
\]

with strict inequality when \(q=\infty\). The equation in (L16) is a distributional equality and every term of \(PEf\) is represented by an \(L^p\) function. In particular \(Ef\in W^{m,p}(V)\).

**Proof.** Use \(S_V\) from (L11), with the same frozen polynomial, and compute
\[
PS_V=I+R_V,\qquad
R_Vg=\sum_{|\alpha|=m}(a_\alpha-a_\alpha(0))D^\alpha S_Vg
       +\sum_{|\alpha|<m}a_\alpha D^\alpha S_Vg.                   \tag{L18}
\]
The top-order terms have norms at most
\(C\sup_V|a_\alpha-a_\alpha(0)|\|g\|_p\).
For a lower-order term, Hölder's inequality and the corresponding row of the table give
\[
\|a_\alpha D^\alpha S_Vg\|_p
\leq C\|a_\alpha\|_{L^{r_\alpha}(V)}\|g\|_p.                      \tag{L19}
\]
All \(r_\alpha\) are finite. On shrinking the surrounding ball, the first coefficients tend to zero by continuity and the norms in (L19) tend to zero by absolute continuity of their integrals. The constants in (L11) do not grow as \(V\) shrinks inside \(B_1\). Choose the ball so that \(\|R_V\|\leq1/2\) for every \(V\) contained in it.

The series \(B_V=\sum_{\nu=0}^\infty(-R_V)^\nu\) converges in operator norm, since \(L^p(V)\) is Banach. Multiplication of its finite partial sums by \(I+R_V\) leaves an error of norm at most \(2^{-N}\), so \(B_V\) is its two-sided inverse and \(\|B_V\|\leq2\). Define
\[
E=S_VB_V.                                                        \tag{L20}
\]
Equations (L18) and (L11) give the right identity and every bound in (L17). They also justify all coefficient products used in the equation.

For the left identity let \(g=q(D)v\), extended by zero, where \(v\in C_c^\infty(V)\). The second identity in (L12) gives \(S_Vg=v\), and therefore \((I+R_V)g=Pv\). The inverse on \(L^p(V)\) implies \(B_VPv=g\), and hence \(EPv=v\). This checks the same \(E\) on both stated domains. It asserts neither a boundary condition for \(Ef\) nor uniqueness among all local solutions. \(\square\)

## AN03-LCE-005 — The Hölder alternative, with its scaling made explicit

For \(0<\gamma<1\), let \(\overline C^\gamma(V)\) be the bounded functions with finite seminorm
\([f]_{\gamma,V}=\sup_{x\ne y\in V}|f(x)-f(y)|/|x-y|^\gamma\).
On a ball \(B_r\) use the equivalent, scaled norm
\[
N_r(f)=\|f\|_{\infty,B_r}+r^\gamma[f]_{\gamma,B_r}.                 \tag{L21}
\]
This is a Banach norm: a Cauchy sequence converges uniformly, and the difference quotient bound passes to that limit, including the Cauchy bound for the seminorm. The product inequality
\(N_r(fg)\leq N_r(f)N_r(g)\) follows by adding and subtracting \(f(x)g(y)\).

**Extension.** A function in this space has a unique continuous extension to \(\overline B_r\), by its Hölder bound. Extend it to all of \(\mathbb R^n\) by
\[
\mathcal A_rf(x)=
\begin{cases}
f(x),&|x|\leq r,\\
(2-|x|/r)f(rx/|x|),&r<|x|<2r,\\
0,&|x|\geq2r.
\end{cases}                                                       \tag{L22}
\]
To check the norm including pairs in different regions, let \(\pi_r\) be radial projection onto \(\overline B_r\), and let \(\theta_r(x)=\min(1,\max(0,2-|x|/r))\). Then \(\mathcal A_rf=\theta_r(f\circ\pi_r)\). The projection has Lipschitz constant at most two: for exterior points expand the difference of their normalized vectors, ordering their radii; for an interior and an exterior point insert the point where their connecting segment first meets the sphere. Also
\(|\theta_r(x)-\theta_r(y)|\leq\min(1,|x-y|/r)\leq(|x-y|/r)^\gamma\).
The product difference estimate now gives
\[
\|\mathcal A_rf\|_\infty+r^\gamma[\mathcal A_rf]_{\gamma,\mathbb R^n}
\leq C_\gamma N_r(f),                                             \tag{L23}
\]
with a constant independent of \(r\).

**The frozen Hölder bound.** For \(h\) bounded and globally \(\gamma\)-Hölder, the top-order kernels in (L6) have zero integral. Thus
\[
K_\ell*h(x)=\int K_\ell(z)(h(x-z)-h(x))\,dz,
\quad
\|K_\ell*h\|_\infty\leq C2^{-\ell\gamma}[h]_\gamma.                \tag{L24}
\]
The derivative kernel also has zero integral, and the same computation gives
\(\|\nabla(K_\ell*h)\|_\infty\leq C2^{\ell(1-\gamma)}[h]_\gamma\).
For points a distance \(t\leq1\) apart, estimate a term either by twice its supremum or by \(t\) times its derivative supremum. Sum the derivative bound where \(2^\ell t\leq1\) and the supremum bound where \(2^\ell t>1\). The geometric sums are at most
\(C_\gamma t^\gamma[h]_\gamma\).
For \(t>1\), the convergent supremum sum suffices. Therefore the sum defines a bounded \(C^\gamma\) function with norm at most \(C_\gamma(\|h\|_\infty+[h]_\gamma)\). For compactly supported \(h\), it is the distribution \((D^\alpha F_0)*h\): the symbol partial sums converge on Schwartz test functions, and (L24) identifies their locally uniform limit. For lower orders \(k>0\), the sum of the \(L^1\) kernel norms is finite, so both the supremum and the Hölder seminorm are bounded directly by convolution. Finally, convolution with \(D^\alpha H\), for \(h\) supported in \(B_2\) and output restricted to \(B_1\), is bounded in the full \(C^\gamma\) norm. Use the supremum of that derivative and its first derivatives on \(B_3\), the mean-value theorem, and \(\|h\|_1\leq|B_2|\|h\|_\infty\).

It follows that the operator \(T f=(G*\mathcal A_1 f)|_{B_1}\) satisfies
\[
\|D^\alpha Tf\|_{\overline C^\gamma(B_1)}
\leq C\|f\|_{\overline C^\gamma(B_1)},\qquad |\alpha|\leq m.       \tag{L25}
\]
This argument works directly for the full Hölder space. It does not require smooth functions to be dense in the same Hölder norm.

Rescale this single solver by
\[
S_rf(x)=r^m\,T(f(r\,\cdot))(x/r),\qquad x\in B_r.
\]
Homogeneity of \(q\) gives
\[
q(D)S_rf=f,\qquad
N_r(D^\alpha S_rf)\leq C r^{m-|\alpha|}N_r(f).                    \tag{L26}
\]
If \(g=q(D)v\) with \(v\in C_c^\infty(B_r)\), its rescaled extension in (L22) is precisely its zero extension. Equivalently \(S_rg\) is convolution with the fundamental solution \(r^{m-n}G(\cdot/r)\). Hence \(S_rq(D)v=v\). This remains true when \(G\) has logarithmic terms; no homogeneity assertion about \(G\) was used.

**Theorem.** If every coefficient of \(P\) is \(C^\gamma\) near zero and its frozen principal symbol is elliptic, then on a sufficiently small centered ball there is a linear \(E_\gamma\) on \(\overline C^\gamma\) with
\[
PE_\gamma f=f,\qquad E_\gamma Pv=v\ (v\in C_c^\infty),\qquad
D^\alpha E_\gamma:\overline C^\gamma\to\overline C^\gamma
\text{ bounded for }|\alpha|\leq m.                              \tag{L27}
\]

**Proof.** Compute \(PS_r=I+R_r\) as in (L18). For a highest-order coefficient,
\[
N_r(a_\alpha-a_\alpha(0))\leq2r^\gamma[a_\alpha]_{\gamma,B_r}.
\]
For a lower-order coefficient its norm \(N_r(a_\alpha)\) remains bounded as \(r\downarrow0\), while (L26) supplies the extra factor \(r^{m-|\alpha|}\). The product inequality therefore gives
\[
\|R_r\|_{N_r\to N_r}\leq C\left(
r^\gamma\sum_{|\alpha|=m}[a_\alpha]_{\gamma,B_r}
 +\sum_{|\alpha|<m}r^{m-|\alpha|}N_r(a_\alpha)\right)\longrightarrow0.
                                                                    \tag{L28}
\]
Choose this norm below \(1/2\), and set \(E_\gamma=S_r(I+R_r)^{-1}\). The same geometric-series and test-function argument used for (L20) proves both identities. Equation (L26) gives the stronger estimate
\(N_r(D^\alpha E_\gamma f)\leq2C r^{m-|\alpha|}N_r(f)\).
At fixed \(r\), scaled and unscaled norms are equivalent, proving (L27). The small factor in the top terms is \(r^\gamma\); the unscaled Hölder seminorm of a coefficient need not decrease on smaller balls. \(\square\)

## AN03-LCE-006 — An estimate uniform over open subsets

In this part the operator is the principal part \(P_m\) alone. Fix a compact neighborhood \(K\) of zero, contained in the coefficient domain, on which the coefficients are continuous and
\[
\left|\sum_{|\alpha|=m}a_\alpha(x)\xi^\alpha\right|
\geq c_K|\xi|^m\qquad(x\in K,\ \xi\in\mathbb R^n).                \tag{L29}
\]
Such a \(K\) is obtained by shrinking around an elliptic point, using continuity and compactness of the unit sphere. For any open \(V\subset K\), let
\(d_V(x)=\operatorname{dist}(x,\mathbb R^n\setminus V)\).

**Theorem.** There is a constant \(C\), depending on \(K,P_m,n,m,p\) but not on \(V\), such that, for \(u\in W^{m,p}(V)\) and \(0\leq j\leq m\),

\[
\|d_V^j\nabla^j u\|_{L^p(V)}
\leq C\bigl(\|d_V^mP_mu\|_{L^p(V)}+\|u\|_{L^p(V)}\bigr)^{j/m}
        \|u\|_{L^p(V)}^{1-j/m}.                                  \tag{L30}
\]

For \(j=m\) this is a linear estimate, and for \(j=0\) it is the identity bound. If \(u=0\) as an \(L^p\) function, every derivative is zero, and the assertion is interpreted accordingly. Lower-order terms are not included in \(P_m\) in (L30).

**Proof.** The frozen polynomials
\(q_y(\xi)=\sum_{|\alpha|=m}a_\alpha(y)\xi^\alpha\), \(y\in K\), form a compact family satisfying (L29). Thus (L13) has a common constant. Let \(\eta\in C_c^\infty(B_1)\) equal one on \(B_{1/2}\). For a ball \(B(y,r)\subset V\), apply (L13) to \(\eta((x-y)/r)u(x)\), extended by zero, with \(A=M/r\). On \(B(y,r/2)\) its derivatives equal those of \(u\). Expanding the frozen operator gives three types of terms:
\[
q_y(D)(\eta_yu)=\eta_yP_mu+\eta_y(q_y(D)-P_m)u+[q_y(D),\eta_y]u.
\]
The middle term is at most \(\omega_a(r)|\nabla^m u|\), up to a fixed array constant, where \(\omega_a(r)\to0\) is a common modulus of continuity of the finitely many coefficients on \(K\). Every term in the last commutator contains a derivative of \(u\) of some order \(j<m\), multiplied by a coefficient bounded by \(Cr^{j-m}\). Taking \(p\)th powers, using the finite-sum inequality, and multiplying by \(r^{mp}\), gives
\[
\begin{split}
\sum_{j=0}^m M^{p(m-j)}r^{pj}
       \int_{B(y,r/2)}|\nabla^j u|^p
\leq C\bigg(&\int_{B(y,r)}|r^mP_mu|^p
 +\omega_a(r)^p\int_{B(y,r)}|r^m\nabla^m u|^p\\
 &+\sum_{j<m}\int_{B(y,r)}|r^j\nabla^j u|^p
 +M^{mp}\int_{B(y,r)}|u|^p\bigg).
\end{split}                                                       \tag{L31}
\]
All constants in this inequality are independent of \(M,r,y,V\).

Choose a small number \(r_0>0\), to be fixed below, and put
\[
\rho(y)=\min(r_0,d_V(y)/2).                                       \tag{L32}
\]
The distance function is 1-Lipschitz, by the triangle inequality and taking an infimum. Thus \(\rho\) is \(1/2\)-Lipschitz. Every ball \(B(y,\rho(y))\) is contained in \(V\). The following two geometric bounds ensure uniform overlap when the centers, rather than a discrete covering, are integrated:
\[
\begin{array}{ll}
|x-y|<\rho(y)&\Longrightarrow\quad
       \rho(y)/2<\rho(x)<3\rho(y)/2,\\[2pt]
|x-y|<2\rho(x)/5&\Longrightarrow\quad
       4\rho(x)/5<\rho(y)<6\rho(x)/5
       \quad\hbox{and}\quad |x-y|<\rho(y)/2.
\end{array}                                                       \tag{L33}
\]
They follow immediately by subtracting the two radii and using the Lipschitz bound. The second ball of centers lies in \(V\), since \(2\rho(x)/5<d_V(x)\). Writing \(v_n=|B_1|\), they imply
\[
\int_{\{y:x\in B(y,\rho(y))\}}\frac{dy}{\rho(y)^n}\leq3^n v_n,
\qquad
\int_{\{y:x\in B(y,\rho(y)/2)\}}\frac{dy}{\rho(y)^n}\geq3^{-n}v_n.
                                                                    \tag{L34}
\]
For the upper bound, the centers lie in \(B(x,2\rho(x))\) and \(\rho(y)>2\rho(x)/3\). For the lower bound, integrate just over \(B(x,2\rho(x)/5)\), where \(\rho(y)<6\rho(x)/5\). The same estimates, with constants depending also on \(j,p\), hold if the integrands are multiplied by \(\rho(y)^{pj}\), after factoring out \(\rho(x)^{pj}\).

Integrate (L31), with \(r=\rho(y)\), against \(dy/\rho(y)^n\). Tonelli and (L34) give
\[
\begin{split}
\sum_{j=0}^m M^{p(m-j)}\|\rho^j\nabla^j u\|_p^p
\leq C\bigg(&\|\rho^mP_mu\|_p^p
 +\omega_a(r_0)^p\|\rho^m\nabla^m u\|_p^p\\
 &+\sum_{j<m}\|\rho^j\nabla^j u\|_p^p+M^{mp}\|u\|_p^p\bigg).
\end{split}                                                       \tag{L35}
\]
First choose \(r_0\) so the coefficient of the highest-order term on the right is less than \(1/2\). Next choose \(M_0\geq1\) sufficiently large that the terms of all lower orders on the right can be absorbed by half of their terms on the left whenever \(M\geq M_0\). Indeed each corresponding left coefficient is at least \(M^p\). This proves, with \(F=\|\rho^mP_mu\|_p\) and \(U=\|u\|_p\),
\[
\|\rho^j\nabla^j u\|_p
\leq C\bigl(M^{j-m}F+M^jU\bigr),\qquad M\geq M_0.               \tag{L36}
\]

If \(U>0\) and \(F>M_0^mU\), choose \(M=(F/U)^{1/m}\), obtaining
\(C F^{j/m}U^{1-j/m}\). If \(F\leq M_0^mU\), choose \(M=M_0\), obtaining \(CU\). In both cases the bound is at most
\(C(F+U)^{j/m}U^{1-j/m}\). Finally \(d_V\) is bounded above by a constant depending only on the bounded set \(K\); (L32) therefore gives \(c\,d_V\leq\rho\leq d_V/2\), with \(c>0\) depending only on \(K,r_0\). Replacing \(\rho\) by \(d_V\) proves (L30), with a constant independent of the shape, connectedness, or boundary regularity of \(V\). \(\square\)

## AN03-LCE-007 — A Lipschitz coefficient through a mollifier

We now give the exact weak product used in the remainder of the unit. If \(v\in L^p_{\rm loc}\) and \(a\) is Lipschitz, define
\[
aD_jv=D_j(av)-(D_ja)v                                             \tag{L37}
\]
as a distribution. The two products on the right are locally integrable. This definition agrees with the usual product for smooth \(v\), and depends continuously on \(v\) in \(L^p\) on compact sets, when tested against a fixed compactly supported smooth function.

If \(u\in W^{m-1,p}_{\rm loc}\), choose \(j\) with \(\alpha_j>0\) and use (L37) with \(v=D^{\alpha-e_j}u\) to define \(aD^\alpha u\), \(|\alpha|=m\). This is independent of that choice: smooth approximation of \(u\) in \(W^{m-1,p}\) on a neighborhood of a test function's support makes each definition converge to the same classical product on the approximants. The continuous dependence just proved identifies the limits.

**Commutator lemma.** Suppose \(a:\mathbb R^n\to\mathbb C\) has Lipschitz constant \(M\), \(v\in L^p(\mathbb R^n)\), and \(\varphi\in C_c^\infty(\mathbb R^n)\). Put \(\varphi_\varepsilon(x)=\varepsilon^{-n}\varphi(x/\varepsilon)\). Then
\[
\begin{split}
C_\varepsilon^a v&=(aD_jv)*\varphi_\varepsilon
                     -a(D_jv*\varphi_\varepsilon),\\
\|C_\varepsilon^a v\|_p
&\leq M\|v\|_p\int_{\mathbb R^n}
       \bigl(|\varphi(z)|+|z|\,|D_j\varphi(z)|\bigr)\,dz,
\end{split}                                                       \tag{L38}
\]
and \(C_\varepsilon^a v\to0\) in \(L^p\) for each fixed \(v\).

**Proof.** Applying (L37), or integrating by parts first for smooth \(v\), gives
\[
\begin{split}
C_\varepsilon^a v(x)
={}&\int [a(x-y)-a(x)]v(x-y)D_j\varphi_\varepsilon(y)\,dy\\
 &-\int (D_ja)(x-y)v(x-y)\varphi_\varepsilon(y)\,dy.
\end{split}                \tag{L39}
\]
The right side makes sense for \(v\in L^p\). Its absolute value is bounded by convolution of \(M|v|\) with
\(|y||D_j\varphi_\varepsilon(y)|+|\varphi_\varepsilon(y)|\).
Young's inequality yields (L38), because changing \(y=\varepsilon z\) makes that kernel's \(L^1\) norm independent of \(\varepsilon\). Approximation in \(L^p\) proves that (L39) represents the distribution in (L38), using the continuity of the product (L37) on compact sets. No boundedness of \(a\) on all of \(\mathbb R^n\) is required; its at most linear growth also makes the original products legitimate distributions.

For \(h\in C_c^\infty\), use the unintegrated expression
\[
C_\varepsilon^a h(x)=\int[a(x-y)-a(x)]D_jh(x-y)\varphi_\varepsilon(y)\,dy.
\]
Its \(L^p\) norm is at most
\(\varepsilon M\|D_jh\|_p\int|z||\varphi(z)|\,dz\), which tends to zero. Given \(v\), approximate it by such an \(h\); (L38) bounds \(C_\varepsilon^a(v-h)\) uniformly in \(\varepsilon\). Let \(\varepsilon\downarrow0\) first, and then \(\|v-h\|_p\downarrow0\). This proves strong convergence. \(\square\)

## AN03-LCE-008 — Recovering the highest derivatives from the equation

**Weak regularity and weighted estimate.** Retain the fixed compact neighborhood and ellipticity of AN03-LCE-006, and suppose that all coefficients of \(P_m\) are Lipschitz on a neighborhood of \(K\). Let \(V\subset K\) be open. If
\[
u\in W^{m-1,p}(V),\qquad P_mu\in L^p(V),                           \tag{L40}
\]
where \(P_mu\) is defined by (L37), then \(u\in W^{m,p}_{\rm loc}(V)\), all the weighted derivatives in (L30) belong to \(L^p(V)\), and (L30) holds with the same type of constant. Global unweighted highest-derivative integrability up to \(\partial V\) is not asserted.

**Proof.** Fix a ball \(B_0\) compactly contained in \(V\). Choose nested slightly larger balls inside \(V\), a cutoff \(\chi_0\) equal to one near \(\overline B_0\), and a cutoff \(\chi_1\) equal to one on an open neighborhood \(W\) of \(\operatorname{supp}\chi_0\). Take \(\overline W\subset V\). Set \(v=\chi_0u\), extend it by zero, and set \(b_\alpha=\chi_1a_\alpha\), extended by zero to \(\mathbb R^n\). These \(b_\alpha\) are globally Lipschitz and bounded. Product differentiation, justified by the smooth approximation used after (L37), gives
\[
P_mv=\chi_0P_mu+
\sum_{|\alpha|=m}\sum_{\substack{\beta\leq\alpha\\|\beta|<m}}
 \binom{\alpha}{\beta}a_\alpha(D^{\alpha-\beta}\chi_0)D^\beta u.
                                                                    \tag{L41}
\]
Every term on the right is \(L^p\) and supported in \(V\); its zero extension is also \(\sum b_\alpha D^\alpha v\) on the whole space.

Choose \(\varphi\in C_c^\infty\) of integral one and let \(v_\varepsilon=v*\varphi_\varepsilon\). For each top-order \(\alpha\), choose \(j\) as in (L37). Applying (L38) to \(D^{\alpha-e_j}v\in L^p\) shows
\[
\sum_{|\alpha|=m} b_\alpha D^\alpha v_\varepsilon
=(P_mv)*\varphi_\varepsilon
 -\sum_{|\alpha|=m}C_\varepsilon^{b_\alpha}(D^{\alpha-e_j}v)
\longrightarrow P_mv\quad\hbox{in }L^p(\mathbb R^n).              \tag{L42}
\]
For small \(\varepsilon\), the support of \(v_\varepsilon\) is in \(W\), where \(b_\alpha=a_\alpha\). In particular, (L42) is convergence of \(P_mv_\varepsilon\) in \(L^p(W)\). Also \(v_\varepsilon\to v\) in \(L^p\). Apply (L30), with \(j=m\) and open set \(W\), to the smooth difference \(v_\varepsilon-v_\delta\). Its right side tends to zero. Since \(d_W\) has a positive lower bound on \(\overline B_0\), every highest derivative is Cauchy in \(L^p(B_0)\). Its limit is the corresponding distributional derivative of \(v=u\) there. This proves local \(W^{m,p}\) regularity.

To pass to the full open set without imposing boundary regularity, put
\(V_t=\{x\in V:d_V(x)>t\}\), \(t>0\). Its closure is compact in \(V\), since \(V\subset K\) is bounded. Local regularity and a finite compact cover imply \(u\in W^{m,p}(V_t)\). For \(x\in V_t\), its own distance function satisfies
\[
d_V(x)-t\leq d_{V_t}(x)\leq d_V(x).                               \tag{L43}
\]
The first inequality follows because the ball of radius \(d_V(x)-t\) about \(x\) lies in \(V_t\), by the Lipschitz property of \(d_V\); the second follows from \(V_t\subset V\). Hence, as \(t\downarrow0\), the distances, extended by zero off \(V_t\), increase pointwise to \(d_V\). Apply (L30) on \(V_t\). Its constants are independent of \(t\). Monotone convergence for the derivative integrals, and dominated convergence for the \(u\) and \(P_mu\) integrals, give (L30) on \(V\). This also proves the asserted weighted integrability. \(\square\)

## AN03-LCE-009 — Annular decay and infinite-order vanishing

Let \(P_m\) be elliptic with continuous principal coefficients on a fixed neighborhood of zero. Suppose \(u\in W^{m,p}_{\rm loc}(K^\circ\setminus\{0\})\), and for some real \(N\) and all sufficiently small \(r>0\),
\[
\int_{r<|x|<2r}|u|^p\,dx=O(r^N),\qquad
|P_mu(x)|\leq C\sum_{|\alpha|<m}|x|^{|\alpha|-m}|D^\alpha u(x)|
\quad\hbox{a.e. off zero}.                                      \tag{L44}
\]

**Corollary.** For every \(|\alpha|\leq m\),
\[
\int_{r<|x|<2r}|r^{|\alpha|}D^\alpha u|^p\,dx=O(r^N).             \tag{L45}
\]
The same conclusion holds when the principal coefficients are Lipschitz and the initial assumption is only \(u\in W^{m-1,p}_{\rm loc}\) off zero, with (L44) interpreted distributionally as in (L37). In that case the inequality in (L44) means that the distribution \(P_mu\) has the indicated locally \(L^p\) representative.

**Proof.** On \(A_r=\{r<|x|<2r\}\), let \(d=d_{A_r}\), \(U=\|u\|_{L^p(A_r)}\), and
\(S=\sum_{j<m}\|d^j\nabla^j u\|_{L^p(A_r)}\).
The weak version is first legitimate on this annulus by AN03-LCE-008; all lower derivatives and \(P_mu\) are \(L^p\) on it because its closure lies in the punctured neighborhood. The same is true in the original strong version. Since \(d\leq r\leq|x|\), (L44) implies
\(F=\|d^mP_mu\|_p\leq C S\). Notice also that \(U\leq S\). Applying (L30) at every \(j<m\),
\[
S\leq C\sum_{j<m}S^{j/m}U^{1-j/m}
\leq C S^{(m-1)/m}U^{1/m}.                                      \tag{L46}
\]
If \(S=0\), the desired bound is immediate. Otherwise divide by \(S^{(m-1)/m}\) and raise to the \(m\)th power, obtaining \(S\leq CU\). For \(m=1\), the sum is just \(S=U\), consistent with this calculation. The top-order case of (L30) then gives \(\|d^m\nabla^m u\|_p\leq C(F+U)\leq CU\).

On \(M_r=\{4r/3<|x|<5r/3\}\) one has \(d\geq r/3\). Thus
\[
\int_{M_r}|r^j\nabla^j u|^p\,dx\leq C U^p=O(r^N),\qquad j\leq m.
                                                                    \tag{L47}
\]
To obtain the original full annulus, not just its middle, use \(M_{s r}\) for
\(s=3/4,9/10,11/10,13/10\). Their radial intervals overlap and cover \((r,2r)\): after dividing by \(r\), they are \((1,5/4)\), \((6/5,3/2)\), \((22/15,11/6)\), and \((26/15,13/6)\). Their associated larger annuli still lie in the coefficient neighborhood for small \(r\). Each application of (L47) has \((sr)^N=O(r^N)\), and \(r^j\) is a fixed multiple of \((sr)^j\). Summing these four bounds proves (L45). \(\square\)

Under the differential inequality in (L44), the condition that its annular integral be \(O(r^N)\) for every \(N>0\) is therefore equivalent to the same condition for every scaled derivative in (L45). It suffices to include orders below \(m\), because they include \(u\); the top-order bounds then follow. This is the infinite-order vanishing statement used later in unique continuation.

The annular and ball formulations agree as well. If an annular bound holds for a positive exponent \(N\), split \(B_r\setminus\{0\}\) into the disjoint annuli of inner radii \(2^{-\nu-1}r\), \(\nu\geq0\). Their bounds sum to at most \(C r^N\sum_{\nu\geq0}2^{-(\nu+1)N}\). The value at the origin has no effect on the integral. Conversely, an annulus is contained in \(B_{2r}\). For an unweighted derivative of order \(j\), replace \(N\) in (L45) by \(N+pj\); this gives every desired positive decay exponent for that derivative as well. This argument establishes decay and integrability; a conclusion that the solution vanishes in a neighborhood requires a unique-continuation theorem in addition.

## AN03-LPS-001 — Problems with full solutions

**Problem 1: all three coefficient regimes in one operator.** In dimension six, take \(m=4\), \(p=2\), and
\[
P=(1+|x|^{1/3})(D_1^2+\cdots+D_6^2)^2
  +\sum_{|\alpha|\leq3}b_\alpha(x)D^\alpha.
\]
Determine sufficient local spaces for each \(b_\alpha\), and all admissible derivative exponents for its inverse.

**Solution.** The frozen symbol is \(|\xi|^4\); the principal coefficients are continuous, although no first derivative at zero is required. The critical gap is \(n/p=3\). Order-three coefficients have gap one and may lie in \(L^6_{\rm loc}\); order-two coefficients may lie in \(L^3_{\rm loc}\); order-one coefficients require \(L^{2+\varepsilon_\alpha}_{\rm loc}\); and order-zero coefficients require only \(L^2_{\rm loc}\). These coefficients can be unbounded. For example, a coefficient of order three equal to \(|x|^{-1/2}\) near zero is in \(L^6_{\rm loc}(\mathbb R^6)\), because its sixth power has radial integral proportional to \(\int_0^r t^2\,dt\).

On a sufficiently small neighborhood, (L17) gives order-four derivatives in \(L^2\), order-three derivatives in every \(L^q\) with \(2\leq q\leq3\), order-two derivatives for \(2\leq q\leq6\), order-one derivatives for every finite \(q\geq2\), and the solution itself in \(L^\infty\) as well as all these finite spaces. The first-order term uses, in particular, \(q=2(2+\varepsilon_\alpha)/\varepsilon_\alpha\). There is no \(L^\infty\) assertion for the first derivatives at this critical gap.

**Problem 2: why \(L^p\) alone is insufficient in the critical multiplication step.** In a small disk in \(\mathbb R^2\), construct \(a\in L^2\) and \(w\in W^{1,2}\) such that \(aw\notin L^2\). Relate this to the critical row of the table.

**Solution.** Near zero write \(L(r)=\log(e/r)\) and take
\[
w(x)=L(|x|)^{1/4},\qquad
a(x)=|x|^{-1}L(|x|)^{-5/8},
\]
with smooth cutoffs away from zero. The integral for \(|a|^2\) near zero is a constant times \(\int_0^r t^{-1}L(t)^{-5/4}\,dt\), which is finite. The function \(w\) is square-integrable, and its gradient has squared radial integral bounded by \(C\int_0^r t^{-1}L(t)^{-3/2}\,dt<\infty\). These classical derivatives off zero are also its weak derivatives: integration by parts outside a disk of radius \(\delta\) produces a boundary term bounded by \(C\delta L(\delta)^{1/4}\), tending to zero. Thus \(w\in W^{1,2}\). But \(|aw|^2\) has radial integral \(\int_0^r t^{-1}L(t)^{-3/4}\,dt=\infty\).

Here \(k=1=n/p\). The example disproves the unrestricted multiplication estimate \(L^2\cdot W^{1,2}\subset L^2\), which would be needed to use just \(a\in L^p\) at the critical gap. It does not purport to be a nonexistence example for every elliptic equation. The stronger coefficient space \(L^{2+\varepsilon}\), paired with a sufficiently large finite derivative exponent, is exactly what makes (L19) valid. The displayed \(a\) belongs to no \(L^{2+\varepsilon}\), as its extra radial power already forces divergence.

**Problem 3: check the annular weights on a singular solution profile.** Let \(P_2=\sum_jD_j^2=-\Delta\), \(n\geq2\), and \(u(x)=|x|^\lambda\) off zero, with \(\lambda\in\mathbb R\). Find the annular exponent and verify the differential inequality required in (L44).

**Solution.** Direct radial differentiation gives
\(-\Delta u=-\lambda(\lambda+n-2)|x|^{\lambda-2}\).
Thus \(|P_2u|\leq C|x|^{-2}|u|\), one of the allowed terms in (L44). All derivatives exist and are locally \(L^p\) in the punctured neighborhood. On an annulus, changing variables \(x=ry\) gives
\[
\int_{r<|x|<2r}|u|^p\,dx
=r^{p\lambda+n}\int_{1<|y|<2}|y|^{p\lambda}\,dy.
\]
So \(N=p\lambda+n\), which may be negative, zero, or positive. A derivative of order \(j\leq2\) is homogeneous of degree \(\lambda-j\), unless it vanishes identically. Multiplication by \(r^j\) restores the same power \(r^{p\lambda+n}\) after integration. This verifies both the weight and the exponent in (L45), including profiles that are not integrable at the origin before imposing a sufficiently positive exponent.

**Problem 4: strong commutator convergence need not be operator norm convergence.** Let \(a(x)=x_j\) in (L38), and choose \(\varphi\in C_c^\infty\) of integral one. Show why the commutator tends to zero on each fixed \(L^p\) function even though its \(L^p\) operator norm does not tend to zero.

**Solution.** Formula (L39), with \(D_j=-i\partial_j\), gives convolution with
\[
k_\varepsilon(y)=i\partial_{y_j}\bigl(y_j\varphi_\varepsilon(y)\bigr)
=\varepsilon^{-n}k_1(y/\varepsilon).
\]
This is a nonzero smooth compactly supported kernel: if \(\partial_j(y_j\varphi)=0\), then on each line parallel to the \(j\)th axis the compactly supported function \(y_j\varphi\) is constant, hence zero, forcing \(\varphi=0\), contrary to its integral. There is \(h\in C_c^\infty\) with \(k_1*h\ne0\); for instance, convolution with a smooth approximate identity converges to the nonzero \(k_1\). Define \(h_\varepsilon(x)=\varepsilon^{-n/p}h(x/\varepsilon)\). A change of variables gives
\[
\|h_\varepsilon\|_p=\|h\|_p,\qquad
\|k_\varepsilon*h_\varepsilon\|_p=\|k_1*h\|_p>0.
\]
Thus the operator norm is bounded below independently of \(\varepsilon\). The lemma applies to a fixed input; this example changes the input with the smoothing scale. The weak regularity proof in (L42) uses precisely the strong convergence on its finitely many fixed lower derivatives.

## Reading routes and scope of the imports

The mathematical antecedent for the local coefficient theorem and the subordinate estimates in this unit is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, 1994, §17.1. The organization, exposition, expanded arguments and solved problems here are independently written. In particular, the finite-part construction, the scaled Hölder proof and the explicit annular cover expose steps needed for the stated generality. The earlier Vol. II antecedent has its separate interface in DEP-LCE-CS.

Tao's [*Lecture Notes 4 for 247A*](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf), Theorem 4.4 and Corollary 2.10, is the specified multiplier reading. His [*Lecture Notes 2 for 247A*](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf), Proposition 6.1 and Corollary 6.3, is the specified fractional-integration reading. Their normalization uses \(2\pi\) in the Fourier phase; the change of frequency variable gives our convention without changing the multiplier or exponent conditions.

In the multiplier proof on page 20 of Notes 4, read the two intermediate gradient formulas with the frequency and scale factors restored:
\[
\nabla K_j=(2\pi i\xi m_j)^\vee,\qquad
|\nabla K_j(x)|\lesssim 2^{j(d+1)}
       \min\bigl(1,(2^j|x|)^{-(d+2)}\bigr).
\]
Here \(d\) is that reading's dimension. Its subsequent expression with the factor \(|x|^{-d-1}\) already has the correct scaling. These printing corrections preserve the theorem and its \(d+2\)-derivative hypothesis.

For a complementary proof technique, John K. Hunter's [*Notes on Partial Differential Equations*, revised 18 June 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), Theorem 2.28 estimates the Newtonian potential in Hölder spaces by splitting spatial integrals. Its scope is the Laplacian; (L24)–(L26) handle arbitrary homogeneous elliptic order. Hunter's Lemma 8.11 treats a commutator for first-order systems with \(C^1\) coefficients in \(L^2\). Our proof in (L38)–(L39) gives the scalar Lipschitz, arbitrary finite \(p\) version used here. The comparisons do not substitute the smoother assumptions of those examples for the hypotheses of this unit.

The imported multiplier and fractional-integration theorems retain their own harmonic-analysis prerequisites. The general constant-strength antecedent DEP-LCE-CS retains its separate dependency on the Vol. II constant-coefficient theory.

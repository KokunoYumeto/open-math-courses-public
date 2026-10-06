# From a C*-modular condition to the GNS von Neumann algebra

The finite-weight boundedness proof, exact prerequisite bindings, trace-model domain clarification and approved-edition comparison are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0. Earlier authorship is retained.

A modular boundary condition on a C*-algebra does more than prescribe scalar functions. It makes the finite-domain involution closable, identifies a faithful normal semifinite weight on the represented von Neumann algebra, and determines the dynamics of that weight. The identification of the normal weight is essential: agreeing on a few finite elements would not identify its values at infinity.

The antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.1 Proposition 1.5 and Exercises 1–2, printed pages 95–96 (PDF pages 116–117 in the checked receipt-backed edition). The formula for the normal envelope is VII.4(5), printed pages 89–90 (PDF pages 110–111). The domain, proofs, model, and problems below are independently written. Inner products are linear in the first variable, and neither the algebra nor its GNS Hilbert space is assumed separable.

## The exact dense domains and their approximate identity

Let \(A\) be a C*-algebra, possibly nonunital or zero. Let \(\varphi:A_+\to[0,\infty]\) be faithful and norm lower semicontinuous. We assume C*-semifiniteness in the precise sense that the complex span of its finite positive elements is norm dense in \(A\), without adjoining an identity. This is norm density of the definition algebra \(\mathfrak m\), rather than unital generation by the finite cone. The finite-domain calculation makes this equivalent to norm density of \(\mathfrak n\), with

\[
\mathfrak n=\{x\in A:\varphi(x^*x)<\infty\},\qquad
\mathfrak m=\operatorname{span}\{y^*x:x,y\in\mathfrak n\},\qquad
\mathfrak a=\mathfrak n\cap\mathfrak n^*.
\tag{KL.1}
\]

The same symbol \(\varphi\) denotes the finite linear extension on \(\mathfrak m\). Let \((H,\pi,\Lambda)\) be its GNS triple. Thus

\[
\langle\Lambda(x),\Lambda(y)\rangle=\varphi(y^*x),\qquad
\pi(b)\Lambda(x)=\Lambda(bx)
\quad(x,y\in\mathfrak n,\ b\in A).
\tag{KL.2}
\]

There is a net \((e_i)\) of positive contractions in \(\mathfrak m\subseteq\mathfrak a\) which is an approximate identity of \(A\). For this very net,

\[
\pi(e_i)\longrightarrow I_H\ \text{strongly},\qquad
\Lambda(e_ix)\longrightarrow\Lambda(x)\ \text{in }H
\quad(x\in\mathfrak n).
\tag{KL.3}
\]

In particular \(\Lambda(\mathfrak a)\) is dense in \(H\), and the span of its products is dense as well.

**Proof.** The positive contractions constructed in The finite part is a hereditary algebra are
\(e_h=h(1+h)^{-1}\), directed by finite positive elements \(h\) and their positive order. They have finite weight because \(0\leq e_h\leq h\). Here the norm closure of the finite algebra is all of \(A\), so they form an approximate identity of \(A\). The inverse is taken in the unitization; the function vanishes at zero, so \(e_h\in A\).

For \(x\in\mathfrak n\), the positive elements \(x^*e_ix\) and \(x^*e_i^2x\) converge in norm to \(x^*x\) and are bounded above by it. Lower semicontinuity and that order bound give convergence of both finite weights to \(\varphi(x^*x)\). Consequently

\[
\|\Lambda(x)-\Lambda(e_ix)\|^2
=\varphi(x^*x)-2\varphi(x^*e_ix)+\varphi(x^*e_i^2x)
\longrightarrow0.
\tag{KL.4}
\]

Uniform contractivity and density of \(\Lambda(\mathfrak n)\) give the strong convergence in (KL.3), also as proved in LW-01. The left-ideal property puts \(e_ix\) in \(\mathfrak n\), while \((e_ix)^*=x^*e_i\in\mathfrak n\); hence \(e_ix\in\mathfrak a\). This proves density. If \(x\in\mathfrak a\), these same elements are products of two elements of \(\mathfrak a\). Their vector limits prove product density.

Faithfulness makes \(\Lambda\) injective. It also makes \(\pi\) faithful under the present density assumption: \(\pi(b)=0\) implies \(\varphi(x^*b^*bx)=0\) and therefore \(bx=0\) for every \(x\in\mathfrak n\). Norm density then gives \(b=0\). The injective C*-homomorphism theorem, UB02, gives isometry. Thus \(\pi\) is an isometric, nondegenerate representation. \(\square\)

These are nets on arbitrary directed sets. Sequences will occur below only when testing a Hilbert-space graph or completing a graph norm.

## The modular condition builds continuous GNS unitaries

Let \((\alpha_t)_{t\in\mathbb R}\) be an algebraic one-parameter group of *-automorphisms of \(A\). Suppose that \(\varphi\circ\alpha_t=\varphi\), and that for every \(x,y\in\mathfrak a\) there is a bounded continuous function on \(0\leq\operatorname{Im}z\leq1\), holomorphic in the interior, with

\[
F_{x,y}(t)=\varphi(\alpha_t(x)y),\qquad
F_{x,y}(t+i)=\varphi(y\alpha_t(x)).
\tag{KL.5}
\]

This is the modular condition in The same condition on a C*-algebra and its time convention. Both products lie in \(\mathfrak m\). No pointwise norm continuity of \(\alpha\) is needed for the following conclusion. Each individual automorphism is isometric by UB02, since it and its inverse are *-homomorphisms.

The formulas

\[
V_t\Lambda(x)=\Lambda(\alpha_t(x))\quad(x\in\mathfrak n),\qquad
V_t\pi(b)V_t^*=\pi(\alpha_t(b))\quad(b\in A)
\tag{KL.6}
\]

define a strongly continuous unitary group on \(H\). Therefore, with \(M=\pi(A)''\), the maps \(\beta_t=\operatorname{Ad}(V_t)|_M\) are normal automorphisms of \(M\), pointwise sigma-strong* continuous, and extend the represented original group.

**Proof.** Invariance preserves \(\mathfrak n\) and its GNS norm. The first formula gives an isometry on the dense GNS range; its inverse is the formula for \(-t\). The group law and the second formula hold on that range and extend by boundedness. Invariance also preserves \(\mathfrak a\).

For \(x,y\in\mathfrak a\), the lower boundary for the pair \((y^*,x)\) is

\[
F_{y^*,x}(t)=\langle\Lambda(x),V_t\Lambda(y)\rangle.
\tag{KL.7}
\]

It is continuous by the scalar boundary hypothesis. Density from KL-01 and \(\|V_t\|=1\) extend weak continuity to all Hilbert vectors. The identity
\(\|V_t\eta-V_s\eta\|^2=2\|\eta\|^2-2\operatorname{Re}\langle V_t\eta,V_s\eta\rangle\)
then gives strong continuity. Conjugation preserves \(\pi(A)\) and its bicommutant. It is normal, and its bounded orbits are strongly* continuous. On bounded operator sets this is also sigma-strong* continuity: the square-summable vector seminorms are handled by a finite-head and uniformly bounded tail estimate. \(\square\)

## The strip boundary closes the involution

On the dense algebra \(\mathcal A=\Lambda(\mathfrak a)\subseteq H\), put

\[
\Lambda(x)\Lambda(y)=\Lambda(xy),\qquad
S_0\Lambda(x)=\Lambda(x^*).
\tag{KL.8}
\]

Then \(\mathcal A\) is a left Hilbert algebra, its left multiplication is \(L_{\Lambda(x)}=\pi(x)\), and its generated von Neumann algebra is exactly \(M\).

**Proof of the graph assertion.** Suppose \(\xi_n=\Lambda(x_n)\to0\) and \(S_0\xi_n\to\zeta\) in \(H\), where \(x_n\in\mathfrak a\). For fixed \(y\in\mathfrak a\), apply (KL.5) to \((y,x_n^*)\). The two boundaries are

\[
F_n(t)=\langle S_0\xi_n,V_t\Lambda(y^*)\rangle,\qquad
F_n(t+i)=\langle V_t\Lambda(y),\xi_n\rangle.
\tag{KL.9}
\]

The lower boundaries converge uniformly in \(t\), and the upper ones converge uniformly to zero. Indeed, their differences are bounded by
\(\|S_0\xi_n-S_0\xi_m\|\|\Lambda(y^*)\|\) and
\(\|\xi_n-\xi_m\|\|\Lambda(y)\|\), respectively. The bounded-strip maximum principle makes \((F_n)\) Cauchy uniformly on the entire closed strip. Its limit is continuous there and holomorphic inside, with zero upper boundary. Boundary uniqueness makes this limit zero. Evaluating its lower boundary at zero gives
\(\langle\zeta,\Lambda(y^*)\rangle=0\). Since \(\Lambda(\mathfrak a)\) is dense, \(\zeta=0\). Thus \(S_0\) is closable.

The other Hilbert-algebra axioms have their exact domains in (KL.8). The GNS module identity gives bounded left multiplication with norm at most \(\|x\|\), and

\[
\langle\Lambda(xy),\Lambda(z)\rangle
=\varphi(z^*xy)
=\langle\Lambda(y),\Lambda(x^*z)\rangle
\quad(x,y,z\in\mathfrak a).
\tag{KL.10}
\]

All products evaluated by the weight are in its finite linear domain. Product density is KL-01. Finally \(\mathfrak m\subseteq\mathfrak a\) is norm dense in \(A\), so \(\pi(\mathfrak a)''=\pi(A)''\). This proves the claim. \(\square\)

Let \(S=\overline{S_0}=J\Delta^{1/2}\) be its closed involution and polar data. The graph core in this statement is the original \(\Lambda(\mathfrak a)\), whether or not that algebra is full. Since \(V_t\mathcal A=\mathcal A\) and \(S_0V_t=V_tS_0\), graph closure and polar uniqueness give

\[
V_tD(S)=D(S),\qquad SV_t=V_tS,\qquad
V_tJV_t^*=J,\qquad V_t\Delta^{1/2}V_t^*=\Delta^{1/2}.
\tag{KL.11}
\]

The last equality includes its domain. Thus \(V_t\) commutes with every spectral projection of \(\Delta\). The closed-involution and polar identities used here are proved in TC03, TC08 and TC10, and SK08 gives the precise spectral transport statement.

## The normal weight recovered from this algebra

Apply Completing the two multiplication domains through Recovering the representation and the full algebra to the left Hilbert algebra just constructed. Let \(\mathcal B_l\) and \(\mathcal A_r\) be its completed left-bounded space and right Hilbert algebra, and let \(\lambda_\xi\) and \(R_\eta\) be their multiplication operators. The canonical weight is

\[
\psi(a)=
\begin{cases}
\|\xi\|^2,&a^{1/2}=\lambda_\xi\text{ for some }\xi\in\mathcal B_l,\\
\infty,&a^{1/2}\notin\lambda(\mathcal B_l),
\end{cases}
\qquad a\in M_+.
\tag{KL.12}
\]

WH proves that it is faithful, normal for arbitrary increasing nets, and semifinite. Its GNS representation is canonically the inclusion of \(M\) on \(H\), and its closed finite-star involution is the same \(S\), by WH-08. We will identify this specific weight with the normal envelope in KL-05.

For every \(x\in\mathfrak n\), including those whose adjoints have infinite weight,

\[
\Lambda(x)\in\mathcal B_l,\qquad
\lambda_{\Lambda(x)}=\pi(x),\qquad
\psi(\pi(x)^*\pi(x))=\varphi(x^*x).
\tag{KL.13}
\]

**Proof of these additional identifications.** Set \(x_i=e_ix\). KL-01 gives \(x_i\in\mathfrak a\), \(\Lambda(x_i)\to\Lambda(x)\), and \(\pi(x_i)\to\pi(x)\) strongly. For \(\eta\in\mathcal A_r\), the defining multiplication identity on the original algebra gives

\[
R_\eta\Lambda(x_i)=\pi(x_i)\eta.
\]

Taking the Hilbert-space limit proves \(R_\eta\Lambda(x)=\pi(x)\eta\). This is the defining left-boundedness condition with bound \(\|x\|\), and proves the first two claims. The exact finite-ideal GNS norm in WH-06 gives the last. In particular \(\psi(\pi(a))=\varphi(a)\) whenever \(a\in A_+\) has finite weight, by taking \(x=a^{1/2}\). The conclusion at infinite values has a further proof below. \(\square\)

## Equality with the bounded-functional normal envelope

Let

\[
\mathcal G_\varphi=\{\rho\in A^*_+:\rho\leq c\varphi
\text{ for some }0\leq c<1\}.
\tag{KL.14}
\]

In this densely defined case Directed functionals in the dense case proves that this family is upward directed and that each \(\rho\) factors uniquely as a normal positive functional \(\bar\rho\) through \(\pi(A)''\). The precise normal weight in the source's formula is

\[
\Theta(a)=\sup_{\rho\in\mathcal G_\varphi}\bar\rho(a),
\qquad a\in M_+.
\tag{KL.15}
\]

Then

\[
\Theta=\psi\ \text{on all }M_+,\qquad
\Theta(\pi(a))=\varphi(a)\ \text{for all }a\in A_+,
\tag{KL.16}
\]

including infinite values. In particular \(\Theta\) is faithful, normal and semifinite on the original C*-weight's GNS von Neumann algebra.

**Proof.** For \(\rho\leq c\varphi\), LW-05 constructs a vector \(\eta_\rho\in H\) and an operator \(D_\rho\in M'\), \(0\leq D_\rho\leq cI\), with

\[
\bar\rho(a)=\langle a\eta_\rho,\eta_\rho\rangle,
\qquad \pi(x)\eta_\rho=D_\rho^{1/2}\Lambda(x)
\quad(x\in\mathfrak n).
\tag{KL.17}
\]

On \(\mathcal A\) this means that \(\eta_\rho\) is right bounded and its right multiplication is \(R_{\eta_\rho}=D_\rho^{1/2}\). The norm of this right-multiplication operator is at most \(\sqrt c<1\); no such bound on the Hilbert norm of the implementing vector is asserted. This operator is self-adjoint; the exact right ideal-intersection theorem therefore puts \(\eta_\rho\) in \(\mathcal A_r\), with the indicated multiplication operator. The variational formula The right weight and the variational formula consequently gives \(\bar\rho\leq c\psi\), and hence \(\Theta\leq\psi\).

Conversely, take \(\eta\in\mathcal A_r\) with \(\|R_\eta\|<1\), and set \(\omega_\eta(a)=\langle a\eta,\eta\rangle\). WH-12 proves
\(\omega_\eta\leq\|R_\eta\|^2\psi\), provided the right norm is nonzero. On each finite positive \(a\in A\), (KL.13) gives
\(\omega_\eta(\pi(a))\leq\|R_\eta\|^2\varphi(a)\); an infinite value imposes no further bound. Thus its restriction to \(A\) belongs to \(\mathcal G_\varphi\). If the right norm is zero, injectivity of right multiplication gives \(\eta=0\), and the zero functional belongs to the same family. Normality and ultraweak density of \(\pi(A)\) identify \(\omega_\eta\) with the unique normal extension of that restriction. The strict-norm variational formula for \(\psi\) now gives \(\psi\leq\Theta\). This proves equality on every positive element of \(M\).

Recovery from bounded functionals in LW-03, followed by scalar attenuation \(\rho\mapsto r\rho\), \(r\uparrow1\), gives
\(\varphi(a)=\sup_{\rho\in\mathcal G_\varphi}\rho(a)\) on all of \(A_+\). Substitution in (KL.15) proves the second identity in (KL.16).

For completeness, the supremum in (KL.15) is already additive and normal before this identification. The order of the functionals persists in their normal extensions: a positive difference on \(A\) remains positive on \(M\) by bounded positive strong approximation and normality. Directedness permits one common functional for lower bounds at two positive arguments, proving additivity. For a bounded increasing net \(a_j\uparrow a\), normality of each extension gives

\[
\sup_\rho\bar\rho(a)=\sup_{\rho,j}\bar\rho(a_j)
=\sup_j\sup_\rho\bar\rho(a_j).
\tag{KL.18}
\]

The two suprema commute as suprema of a product directed family. This is arbitrary-net normality.

Equivalently, extend \(\pi\) to the normal homomorphism \(q:A^{**}\to M\). The normal extension \(\rho^{**}\) equals \(\bar\rho\circ q\), since they agree on \(A\). Thus the universal envelope in VII.4(5) is \(\Theta\circ q\) on all positive elements of \(A^{**}\). This pullback identity is proved under finite-domain norm density; it is not asserted for an arbitrary nondensely defined weight. \(\square\)

## The original strip identifies the modular time

The strongly continuous group in KL-02 is exactly

\[
V_t=\Delta^{it},\qquad
\sigma_t^\Theta=\operatorname{Ad}(V_t)|_M.
\tag{KL.19}
\]

**Proof.** On the original graph core, (KL.7) and the other edge of the same function give

\[
G_{\xi,\eta}(t)=\langle\xi,V_t\eta\rangle,
\qquad
G_{\xi,\eta}(t+i)=\langle SV_t\eta,S\xi\rangle.
\tag{KL.20}
\]

For \(\xi=\Lambda(x)\), \(\eta=\Lambda(y)\), this is the function \(F_{y^*,x}\). Since \(SV_t=V_tS\), graph-norm approximation in each variable and the bounded-strip maximum principle extend (KL.20) to every \(\xi,\eta\in D(S)\). The limit is uniform on the closed strip: the two edge differences are bounded by the corresponding products of ordinary norms and \(S\)-norms. Thus no boundary condition on unrepresented elements of a full algebra is being assumed.

Here is the identifying calculation from Uniqueness by an imaginary shift and periodicity with this exact graph core. Let

\[
P_n=1_{[e^{-n},e^n]}(\Delta),\qquad H_n=P_nH.
\tag{KL.21}
\]

The modular operator is injective, so \(P_n\uparrow I\) strongly. KL-03 makes these projections commute with \(V_t\). For \(v\in H\), \(r>0\), define

\[
h(w)=\sqrt{r/\pi}\int_{\mathbb R}e^{-r(t-w)^2}V_tP_nv\,dt.
\tag{KL.22}
\]

The Gaussian vector lemma gives an entire \(H_n\)-valued function with
\(V_th(w)=h(w+t)\) and
\(\|h(t+is)\|\leq e^{rs^2}\|P_nv\|\). For \(\xi\in D(S)\), the function
\(z\mapsto\langle\xi,h(w+\bar z)\rangle\) is bounded and holomorphic on the upper strip and has the lower boundary in (KL.20). Boundary uniqueness and evaluation at \(z=i\) give

\[
\langle\xi,h(w-i)\rangle
=\langle\Delta^{1/2}\xi,\Delta^{1/2}h(w)\rangle
=\langle\xi,\Delta h(w)\rangle.
\tag{KL.23}
\]

Every vector in \(H_n\) is in \(D(\Delta)\), so the last equality has its domain. In more detail, the upper edge gives the pairing with \(S\) in (KL.20); since \(S=J\Delta^{1/2}\) and \(J\) is antiunitary, it equals the first pairing with \(\Delta^{1/2}\) in (KL.23). Self-adjointness then moves one half power to the second slot. No unrestricted product of unbounded operators is used. Density of \(D(S)\) implies \(h(w-i)=\Delta_nh(w)\), where \(\Delta_n\) is the bounded invertible restriction on \(H_n\).

The entire vector function \(q(w)=\Delta_n^{-iw}h(w)\) is now imaginary-periodic:
\(q(w-i)=q(w)\), because \(-i(w-i)=-iw-1\). On \(0\leq\operatorname{Im}w\leq1\) its norm is at most \(e^{n+r}\|P_nv\|\); periodicity supplies the same bound everywhere. Scalar Liouville applied to its vector coefficients makes it constant. Hence \(V_th(0)=\Delta^{it}h(0)\). Let \(r\to\infty\) to get this identity on \(P_nv\), and then \(n\to\infty\) to get it on \(v\).

Finally WH-08 identifies the GNS involution of \(\Theta=\psi\) with \(S\). The modular fundamental theorem The modular fundamental theorem therefore makes \(\operatorname{Ad}(\Delta^{it})|_M\) its modular automorphism group, proving (KL.19). \(\square\)

## The C*-to-von-Neumann modular extension theorem

Under the hypotheses of KL-01–02, the normal envelope \(\Theta\) on \(M=\pi_\varphi(A)''\), defined by (KL.15), is faithful, normal and semifinite. It agrees with \(\varphi\) on every represented positive element, and

\[
\sigma_t^\Theta\circ\pi_\varphi
=\pi_\varphi\circ\alpha_t
\quad(t\in\mathbb R).
\tag{KL.24}
\]

Its canonical GNS unitary identifies \(\Lambda_\Theta(\pi_\varphi(x))\) with \(\Lambda_\varphi(x)\) for every \(x\in\mathfrak n_\varphi\).

**Proof.** KL-03 supplies the left Hilbert algebra on the original GNS space. KL-04 and KL-05 supply and identify the exact faithful normal semifinite weight and its GNS map. KL-06 identifies the implementing group, and substitution in (KL.6) proves (KL.24). This includes arbitrary nonunital algebras and arbitrary Hilbert dimensions. For the zero algebra the Hilbert space is zero, the weight is zero and faithful in the vacuous convention, and all identities have their unique zero-space interpretation. \(\square\)

The graph core, normal-functional supremum, and Gaussian spectral comparison are distinct parts of the theorem. None can be replaced by agreement with the weight on just one finite corner.

## For a finite weight, the two edges force invariance

Let \(\omega\) be a bounded positive functional on any C*-algebra \(A\), and let \(\alpha\) be an algebraic automorphism group. Suppose only that the strip functions (KL.5) exist for every \(x,y\in A\). Then \(\omega\circ\alpha_t=\omega\) for all \(t\). Faithfulness, norm continuity of the group, and a unit are unnecessary. This proves the finite-weight exercise; a finite everywhere positive weight is a bounded positive functional by the positive-functional fact proved in the next paragraph.

**Why an everywhere-finite weight is bounded.** By CS01, a finite weight on every positive element extends uniquely to a positive complex-linear functional on their span; AC4 says that this span is all of \(A\). Suppose its values on positive contractions were unbounded. Choose positive contractions \(b_n\) with \(\omega(b_n)>2^n\), and set

\[
 a_n=2^{-n}b_n,\qquad a=\sum_{n=1}^{\infty}a_n.
\]

Completeness of the C*-algebra makes the series norm convergent. Closedness of the positive cone puts both \(a\) and every tail in that cone. For every positive integer \(N\), monotonicity and finite additivity imply

\[
 \omega(a)\geq\sum_{n=1}^{N}\omega(a_n)>N,
\]

contradicting finiteness of \(\omega(a)\). Hence its supremum \(C\) on positive contractions is finite. For self-adjoint \(u\), the positive and negative parts from AC4 have norm at most \(\|u\|\), so their functional values both lie in \([0,C\|u\|]\), giving \(|\omega(u)|\leq C\|u\|\). Writing an arbitrary element as its real part plus \(i\) times its imaginary part, each of norm at most the original norm, gives \(|\omega(x)|\leq2C\|x\|\). Thus the functional is bounded, including for nonunital algebras, without using lower semicontinuity.

**Proof of invariance.** Use its cyclic bounded-functional GNS vector \(\xi\), and choose a positive contractive approximate identity \((e_i)\). BG01–03 gives \(\pi_\omega(e_i)\xi\to\xi\). Fix \(x\in A\), and use the functions \(F_{x,e_i}\). On either boundary their difference from \(g(t)=\omega(\alpha_t(x))\) is at most

\[
\|x\|\|\xi\|\|(I-\pi_\omega(e_i))\xi\|,
\tag{KL.25}
\]

uniformly in \(t\). This follows by placing the approximate-identity error in either inner-product slot and using \(\|\alpha_t(x)\|=\|x\|\). It uses no invariant functional yet. The maximum principle makes the net Cauchy uniformly on the closed strip, with limit \(F\) satisfying

\[
F(t)=F(t+i)=g(t),\qquad
\|F\|_\infty\leq\|\omega\|\|x\|.
\tag{KL.26}
\]

Translate this strip vertically by every integer multiple of \(i\). Equality of the edges gives a continuous imaginary-periodic function on the plane. It is holomorphic across the joining lines: splitting a triangle along a joining line and taking interior approximations cancels the integrals on that line, so Morera's theorem applies. It is bounded everywhere by (KL.26), hence constant by Liouville. Thus \(g(t)=g(0)=\omega(x)\). Equality for all \(x\) proves invariance. A unital algebra permits the shorter choice \(y=1\); the net argument retains the nonunital generality. \(\square\)

## An injective trace-class density and its exact modular group

Let \(h\) be a positive injective trace-class operator on a Hilbert space \(K\), and define

\[
\omega(a)=\operatorname{Tr}(ha)\quad(a\in B(K)_+).
\tag{KL.27}
\]

This is a faithful normal finite positive functional. Its modular automorphism group is

\[
\sigma_t^\omega(a)=h^{it}ah^{-it}.
\tag{KL.28}
\]

No bounded inverse of \(h\) is assumed. The imaginary powers are everywhere defined unitaries, by injectivity and spectral calculus.

**Proof.** Here the positive trace is the supremum of finite orthonormal sums of quadratic values; being trace class means this supremum is finite. A spectral band where \(h\geq\delta I\) can have no more than \(\operatorname{Tr}(h)/\delta\) orthonormal vectors, by the definition of that supremum. These bands therefore have finite dimension. Their spectral cutoffs approximate \(h\) in operator norm, with error at most \(\delta\). In particular \(h\) is compact: from a bounded sequence choose successive subsequences on which each finite-rank cutoff converges, then take the diagonal subsequence; the uniform norm error makes its images under \(h\) Cauchy. Completeness gives a convergent subsequence. This proves the compactness used in the following familiar spectral argument directly from finite trace.

The positive spectral calculus gives finite-dimensional spectral bands \(1_{[\delta,\|h\|]}(h)K\) for every \(\delta>0\). Indeed, on such a band \(\|h\eta\|\geq\delta\|\eta\|\); an infinite orthonormal sequence would have pairwise separated images under \(h\), contradicting compactness. Each finite-dimensional self-adjoint restriction has an orthonormal eigenbasis. For completeness, its real quadratic form attains a maximum on the unit sphere, by finite-dimensional compactness from AB04. Differentiating along real and purely imaginary directions perpendicular to a maximizing unit vector shows that its image has no perpendicular component, so it is an eigenvector. Its orthogonal complement is invariant; induction proves the claim. Choose the bands increasing, retain the already chosen eigenvectors and diagonalize each new orthogonal difference, which is invariant under the self-adjoint operator. Diagonalizing these finite-dimensional restrictions and taking their increasing union gives positive eigenvalues \(\lambda_j\) and an orthonormal eigenbasis of the support of \(h\). Injectivity makes that support all of \(K\), and trace-class finiteness gives \(\sum_j\lambda_j<\infty\). There are only countably many eigenvectors in the union of these finite bands. Thus a nonzero \(K\) under these hypotheses is separable as a consequence. The trace is
\(\sum_j\lambda_j\langle a e_j,e_j\rangle\). Positivity and injectivity prove faithfulness. Interchanging a bounded increasing positive net with this positive sum proves normality.

Identify its GNS Hilbert space with the Hilbert-Schmidt space \(\mathcal S_2(K)\) by

\[
\Lambda(a)=ah^{1/2},\qquad \pi(a)Z=aZ.
\tag{KL.29}
\]

Finite matrix units are in its range, so it is dense. The initial involution sends \(e_{ij}\) to \(\sqrt{\lambda_i/\lambda_j}\,e_{ji}\). Its closure on Hilbert-Schmidt matrices is

\[
SZ=h^{-1/2}Z^*h^{1/2},\qquad
JZ=Z^*,\qquad
(\Delta Z)_{ij}=(\lambda_i/\lambda_j)Z_{ij}.
\tag{KL.30}
\]

These are unbounded-operator formulas with their spectral domains, using SK05 and SK07–09:

\[
D(S)=\left\{Z:\sum_{i,j}(\lambda_i/\lambda_j)|Z_{ij}|^2<\infty\right\},\qquad
D(\Delta)=\left\{Z:\sum_{i,j}(\lambda_i/\lambda_j)^2|Z_{ij}|^2<\infty\right\}.
\tag{KL.31}
\]

The product involving \(h^{-1/2}\) in (KL.30) requires the stated domain. Let \(Z\in D(S)\) as specified by (KL.31), and form the matrix

\[
 Y_{ij}=\sqrt{\lambda_j/\lambda_i}\,\overline{Z_{ji}}.
\]

The domain sum says exactly that \(Y\) is Hilbert-Schmidt, hence bounded: rowwise Cauchy–Schwarz gives \(\|Yv\|\leq\|Y\|_2\|v\|\) first on finite columns and then by density. For every finite column \(v\), the same coefficient sums put \(Z^*h^{1/2}v\) in \(D(h^{-1/2})\), with product equal to \(Yv\). For general \(v\), use finite-column approximants. The two bounded maps \(Z^*h^{1/2}\) and \(Y\) preserve these limits, and closedness of \(h^{-1/2}\), proved by the spectral domain theorem, gives the actual product identity on all of \(K\). Thus the displayed formula defines a Hilbert-Schmidt vector on precisely the domain stated; outside it the notation does not assert such a vector.

The coefficient formula makes the displayed \(S\) closed. It agrees with the initial involution on every \(ah^{1/2}\), since its image is \(a^*h^{1/2}\), again Hilbert-Schmidt. Finite matrix truncations of any vector in (KL.31) converge in its graph norm and belong to that initial range. These two inclusions identify the closure. Hence its polar data are exactly (KL.30), and

\[
\Delta^{it}Z=h^{it}Zh^{-it},\qquad
\Delta^{it}\pi(a)\Delta^{-it}Z=(h^{it}ah^{-it})Z.
\tag{KL.32}
\]

The modular theorem gives (KL.28), proving the second source exercise at its full generality.

There is also a C*-version on \(A=\mathcal K(K)\). Restrict \(\omega\) to compact operators. Its GNS completion is the same Hilbert-Schmidt space. Left multiplication is a faithful normal representation of \(B(K)\); The image of a faithful normal representation makes its image ultraweakly closed. Finite-rank projections \(p_F\uparrow I_K\) give \(p_Fa\to a\) strongly with a uniform norm bound; left multiplication by these compact operators converges strongly on Hilbert-Schmidt vectors by finite-matrix approximation. Thus the represented bicommutant of \(\mathcal K(K)\) is exactly that image of \(B(K)\). The normal extension in KL-07 is precisely (KL.27): normal order inequalities for functionals on the compacts extend to \(B(K)\) by finite-rank strong compressions, and the attenuated functionals \(r\omega\), \(r\uparrow1\), already reach it in (KL.15). Thus the same diagram realizes the C*-extension theorem and its modular covariance.

For \(K=\ell^2(\mathbb N_0)\) and \(\lambda_j=2^{-j-1}\), \(\omega(1)=1\), but
\(\Delta e_{ij}=2^{j-i}e_{ij}\). The modular operator and its inverse are unbounded, even though the functional is finite. The four-by-four coefficient display used to illustrate this model is a restriction to sixteen basis vectors, not a bounded approximation to the whole modular operator.

## Problems that keep the domains visible

**Problem 1.** On \(A=\mathbb C^2\), put \(\varphi(a,b)=a\) for positive pairs with \(b=0\), and \(\varphi(a,b)=\infty\) otherwise. Does the identity automorphism group satisfy the modular condition? Can the universal normal envelope be a pullback from the original GNS algebra?

**Solution.** The weight is faithful and lower semicontinuous. Its finite-star algebra is \(\mathbb C\oplus0\); all required products are in that commutative finite algebra, so constant strip functions and invariance give the modular condition. The GNS algebra is \(\mathbb C\), with \(\pi(a,b)=a\). The universal envelope gives infinite weight to \((0,1)\), whose represented image is zero. Every weight on \(\mathbb C\) gives zero at zero, so no such pullback exists. The missing hypothesis of KL-07 is finite-domain norm density.

**Problem 2.** In the model \(\lambda_j=2^{-j-1}\), compute the GNS implementer on \(e_{01}\) and the squared \(S\)-graph norm of \(Z=\sum_{j\geq1}2^{-j/2}e_{0j}\). Is \(Z\) in \(D(S)\)?

**Solution.** Equation (KL.32) gives \(V_te_{01}=2^{it}e_{01}\). The vector is Hilbert-Schmidt because \(\sum_{j\geq1}2^{-j}=1\), while its squared \(S\)-norm is
\(\sum_{j\geq1}2^j2^{-j}=\infty\). Thus it is outside \(D(S)\); its graph norm is infinite. A finite functional does not make the involution bounded.

**Problem 3.** Why does the closability argument in KL-03 not require a sequence of approximate identities, even if \(H\) is nonseparable?

**Solution.** The approximate identity in KL-01 is a net. It proves density of the test algebra and strong nondegeneracy for the given representation. The sequence in KL-03 tests closure of a subset of \(H\oplus H\), which is a metric space in every Hilbert dimension. The limit vector is tested against the whole dense algebra, not against a countable total family. These uses of nets and sequences concern different topologies.

## Source and remaining scope

KL-01–07 supply the full original proof of Takesaki II VIII.1.5, including the exact normal-envelope identity, its faithfulness, arbitrary-net normality, semifiniteness, and modular intertwining. KL-08 and KL-09 solve VIII.1 Exercises 1 and 2. The latter identifies the unbounded modular data, rather than postulating a bounded inverse of the density. The finite-domain constructions, full Hilbert-algebra correspondence, bounded-functional factorization, spectral calculus, and scalar strip arguments remain the named prerequisites of these proofs.

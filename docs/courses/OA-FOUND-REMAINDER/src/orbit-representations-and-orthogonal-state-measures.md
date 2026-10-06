<span id="orbit-representations-and-orthogonal-state-measures"></span>
# Orbit representations and orthogonal state measures

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A free action on a compact space gives one irreducible representation for each orbit. Evaluating the identity coefficient at a point gives a pure state, and integrating those states recovers a vector state of the represented crossed-product algebra. We prove the norm bound that makes point evaluation legitimate on the completed algebra, then identify the abelian algebra associated with this representing measure.

The pointwise parameter space is the closed support of the measure. At a point outside that support, evaluation may fail to descend through the represented continuous-function algebra. Our first exercise gives a finite counterexample. For a point in the support, its state and orbit representation are defined even if that point itself has measure zero.

We use the regular construction, coefficient expectation and free-action maximal-abelian test in [Crossed-product coefficients and factor tests](../reader/crossed-product-coefficients-and-factor-tests.html). Its named existing regular-model prerequisites remain in force. The implemented-action commutant formula is equation E9 of [The regular commutant in every covariant representation](../reader/orbit-proof-route/owned-4.html#the-amplified-commutant-and-the-rank-one-slice). Its general proof uses the standard coefficient Hilbert algebra, its closed polar decomposition and OA-MOD-MF-05, followed by Theorem 10.1 of the current double-commutant lesson for representation comparison, arbitrary-cardinal amplification and a rank-one normal slice. SC-02 remains an alternative positive-vector-series proof. We use its specialization to a faithful multiplication representation and a countable discrete group. Section 2.1 below spells out the matrix reconstruction in our group convention.

The decomposable operator norm formula is Theorem 10.1 of [Measurable fields and direct integrals](../reader/supplements/measurable-fields-direct-integrals.html). Cyclic representation uniqueness and the pure-state criterion are Theorems 5.5 and 8.3 of [Representations, positive functionals and GNS](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html). The operator map and multiplicativity criterion for orthogonal measures are Proposition 9.2 and Theorem 10.2 of [Integral representations of states](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html). The multiplication algebra model is Theorem 3.1 of [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html). Their complete programme proofs and the general commutant applications are linked in the accompanying proof guide.

Elementary measure and topology prerequisites are the Radon–Nikodym theorem for equivalent finite measures, the chain rule for transported measures, Fubini, regularity of finite Borel measures on compact metric spaces, density of continuous functions in \(L^2\), and Tietze extension from a closed subspace.

For a freely accessible comparison, Kawamura, Takemoto and Tomiyama's [State extensions in transformation group C*-algebras](https://acta.bibl.u-szeged.hu/15269/1/math_054_fasc_001_002_191-200.pdf), Section 1, proves a unique-extension criterion using singular translated measures; Corollary 1.4 specializes it to points with trivial stabilizer. Their abstract C*-crossed product differs from the represented algebra used here. Our complete arguments below establish the norm bound, purity, orbit equivalence and orthogonal measure in this representation. The arbitrary-covariant commutant provider retains its explicitly named standard-form and modular inputs. [Takesaki] identifies the historical assignment.

<span id="1-the-support-and-the-implemented-model"></span>
## 1. The support and the implemented model

Let \(X\) be a nonempty compact metrizable space, \(\mu\) a Borel probability measure, and \(G\) a countable discrete group acting on \(X\) by homeomorphisms. Assume the point action is free:
\[
g x=x\quad\Longrightarrow\quad g=e,
\tag{1.1}
\]
and \(\mu\) is quasi-invariant, meaning \(g_*\mu\) and \(\mu\) have the same null sets for every \(g\), where
\((g_*\mu)(B)=\mu(g^{-1}B)\).

Write \(Y=\operatorname{supp}\mu\). It is a nonempty closed \(G\)-invariant subspace. Indeed, an open set has measure zero exactly when its translate has measure zero, so the complement of the support is invariant. Second countability makes that complement a countable union of null open sets; hence \(\mu(Y)=1\). Regard \(\mu\) as a probability measure on \(Y\). It has full support there, and the restricted point action remains free.

The represented image of \(C(X)\) on \(L^2(X,\mu)\) is exactly \(C(Y)\) acting by multiplication on
\[
H=L^2(Y,\mu).
\]
The kernel of multiplication on \(C(X)\) consists precisely of functions vanishing on \(Y\): a continuous function nonzero somewhere on \(Y\) is bounded away from zero on an open set of positive measure. Restriction onto \(C(Y)\) is surjective by Tietze extension. We henceforth work on \(Y\).

Put \(D=L^\infty(Y,\mu)\), with its faithful normal multiplication representation on \(H\), and
\[
\alpha_g(f)(y)=f(g^{-1}y).
\]
Let \(r_g=d(g_*\mu)/d\mu\). Equivalence makes \(r_g\) strictly positive and finite almost everywhere. The Radon–Nikodym change-of-variables identity gives the unitary implementation
\[
(v_g\eta)(y)=r_g(y)^{1/2}\eta(g^{-1}y).
\tag{1.2}
\]
For clarity, the identity
\(\int F(y)r_g(y)\,d\mu(y)=\int F(gz)\,d\mu(z)\)
proves \(\|v_g\eta\|_2=\|\eta\|_2\). Transporting a transported measure gives
\[
r_{gh}(y)=r_g(y)r_h(g^{-1}y)
\quad\text{almost everywhere}.
\]
Thus \(v_gv_h=v_{gh}\), \(v_g^*=v_{g^{-1}}\), and
\(v_gM_fv_g^*=M_{\alpha_g(f)}\). These are operator identities on \(H\), independent of choices of representatives for the densities.

Use the regular model on \(\mathcal K=\ell^2(G;H)\):
\[
(\pi(f)\xi)(s)=\alpha_{s^{-1}}(f)\xi(s),\qquad
(u_g\xi)(s)=\xi(g^{-1}s),\qquad
R=\{\pi(D),u_g:g\in G\}''.
\tag{1.3}
\]
The multiplication algebra is maximal abelian on \(H\), so \(D'=D\). Apply BF77 E9 to the faithful normal multiplication representation \(\rho:D\to B(H)\), the discrete action \(\alpha\), and its unitary implementation \(V_g=v_g\). The discrete topology makes the continuity hypotheses automatic and gives \(\Delta_G(g)=1\). In the coordinate order \(\ell^2(G;H)\), its regular coefficient operator is exactly \(\pi(f)\) from (1.3); its constant commutant coefficient is \(\pi'(f)\); and its group generator \(V_g\otimes R_g\) acts as \(\xi(s)\mapsto v_g\xi(sg)\). Consequently E9 yields
\[
S=R'=\{\pi'(D),t_g:g\in G\}'',
\tag{1.4}
\]
where
\[
(\pi'(f)\xi)(s)=f\xi(s),\qquad
(t_g\xi)(s)=v_g\xi(sg).
\tag{1.5}
\]
These conventions agree with the regular convention in (1.3). In particular
\[
t_g\pi'(f)t_g^*=\pi'(\alpha_g(f)).
\]

Define the separable unital \(C^*\)-algebra
\[
C=C^*(\pi'(C(Y)),t_g:g\in G)\subseteq S.
\tag{1.6}
\]
Separability follows from that of \(C(Y)\) and countability of \(G\). Its weak closure is \(S\), because continuous multiplications generate \(D\) as a von Neumann algebra. Let \(C_0\) be the dense polynomial star algebra of finite sums
\[
P=\sum_{g\in F}\pi'(f_g)t_g,\qquad f_g\in C(Y).
\tag{1.7}
\]
Covariance gives closure under products and adjoints.

<span id="2-exchanging-the-models-and-recovering-the-vector-state"></span>
## 2. Exchanging the models and recovering the vector state

Set
\[
(W\xi)(s)=v_s^*\xi(s^{-1}).
\tag{2.1}
\]
Inversion of \(G\) permutes the coordinates, and each \(v_s^*\) is unitary, so \(W\) is unitary. The identity \(v_{s^{-1}}^*=v_s\) gives \(W^2=1\). Direct calculation gives
\[
W\pi'(f)W=\pi(f),\qquad Wt_gW=u_g.
\tag{2.2}
\]
For example
\[
(Wt_gW\xi)(s)
=v_s^*v_gv_{s^{-1}g}^*\xi(g^{-1}s)
=\xi(g^{-1}s),
\]
since \(v_{s^{-1}g}^*=v_g^*v_s\). Thus \(WSW=R\), and \(WCW\) is the continuous-coefficient regular \(C^*\)-algebra. These identities exchange two models after the cited commutant theorem; they do not assert a universal property for arbitrary covariant completions.

Let \(J_e:H\to\mathcal K\) put a vector in coordinate \(e\), and let \(E:R\to D\) be the regular coefficient expectation. Transport it by \(W\):
\[
F:S\longrightarrow D,\qquad
F(x)=E(WxW)=J_e^*xJ_e.
\tag{2.3}
\]
The last equality holds because \(WJ_e=J_e\). Hence \(F\) is faithful, normal, unital and completely positive, with
\[
F(\pi'(f))=f,\qquad
F(\pi'(f)x\pi'(h))=fF(x)h.
\]
It selects \(f_e\) from (1.7). It also defines unique coefficients \(F(xt_g^*)\) for arbitrary \(x\in S\), by transport of the regular coefficient theorem. The corresponding bounded matrix reconstruction uses both coordinate indices. No assertion about convergence of unordered operator Fourier sums is needed.

Let \(\xi_0=J_e1\), a unit vector, and define
\[
\Phi(x)=\langle x\xi_0,\xi_0\rangle\qquad(x\in S),\qquad
\varphi=\Phi|_C.
\]
Compression at \(e\) proves the complete vector-state formula
\[
\Phi(x)=\int_Y F(x)(y)\,d\mu(y)\qquad(x\in S).
\tag{2.4}
\]
For a polynomial it is \(\int_Y f_e\,d\mu\). For a general element of \(S\), \(F(x)\) is an \(L^\infty\) class and the integral is well-defined.

The expectation on \(C\) has continuous values:
\[
F(C)\subseteq C(Y).
\tag{2.5}
\]
Indeed, approximate \(x\in C\) in norm by polynomials \(P_n\). Contractivity of \(F\) makes \(F(P_n)\) Cauchy in \(L^\infty(Y,\mu)\). On continuous functions, full support makes this norm equal to the uniform norm. Consequently \(F(P_n)\) converges uniformly to a function in \(C(Y)\), representing \(F(x)\). This continuous representative is unique.

<span id="21-commutant-coefficients-determine-the-matrix"></span>
### 2.1. Commutant coefficients determine the matrix

The commutant formula is a statement about a generated von Neumann algebra. A formal Fourier expression also requires a precise convergence convention. Here is the bounded reconstruction that will suffice.

Use the regular convention from the coefficient lesson: on \(\ell^2(G;H)\),
\[
 (\pi(a)\xi)(s)=\alpha_{s^{-1}}(a)\xi(s),\qquad
 (u_h\xi)(s)=\xi(h^{-1}s).
\]
Assume \(V_g a V_g^*=\alpha_g(a)\), and set
\[
 (w_g\xi)(s)=V_g\xi(sg),\qquad
 (\pi'(b)\xi)(s)=b\xi(s)\quad(b\in A').
\]
The two displayed families commute with \(\pi(A)\) and all \(u_h\): for \(w_g\), the coefficient identity is
\[
 V_g\alpha_{(sg)^{-1}}(a)=\alpha_{s^{-1}}(a)V_g.
\]
Let \(T\) belong to the commutant. Write \(P_s\) for coordinate evaluation and \(T_{s,t}=P_sTP_t^*\). Commutation with every left translation gives
\[
 T_{hs,ht}=T_{s,t},\qquad T_{s,t}=T_{e,s^{-1}t}.
\]
Commutation with the coefficient operators gives
\[
 aT_{e,g}=T_{e,g}\alpha_{g^{-1}}(a).
\]
Consequently
\[
 b_g=P_eTw_g^*P_e^*=T_{e,g}V_g^*\in A',\qquad
 T_{s,t}=b_{s^{-1}t}V_{s^{-1}t}.
\]
Indeed, \(w_g^*P_e^*\eta=P_g^*V_g^*\eta\), and
\(\alpha_{g^{-1}}(a)V_g^*=V_g^*a\); substituting this in the preceding identity proves \(ab_g=b_ga\). Thus the family \((b_g)\) determines every matrix entry and determines \(T\) uniquely. The matrix entry of the formal expression \(\sum_g\pi'(b_g)w_g\) at \((s,t)\) is exactly the same one: only \(g=s^{-1}t\) contributes there.

For actual operator convergence, let \(Q_F=\sum_{s\in F}P_s^*P_s\), with \(F\) ranging over finite subsets of \(G\). Then
\[
 Q_FTQ_F
   =\sum_{s,t\in F}P_s^*b_{s^{-1}t}V_{s^{-1}t}P_t,
 \qquad \|Q_FTQ_F\|\leq\|T\|.
\]
These compressions tend strongly to \(T\), and their adjoints tend strongly to \(T^*\). To verify the first assertion on a vector \(\xi\), use
\[
 \|Q_FTQ_F\xi-T\xi\|
 \leq\|T\|\,\|Q_F\xi-\xi\|
       +\|(Q_F-1)T\xi\|\longrightarrow0;
\]
the same estimate applies to \(T^*\). This bounded two-coordinate limit supplies reconstruction, independently of a regrouping by group element. The compressions need not lie in the commutant; its generation by \(\pi'(A')\) and \(w(G)\) is the separate existing E9 theorem. Unordered Fourier partial sums need not converge strongly: already the scalar \(G=\mathbb Z\) case has the unbounded partial sums proved in Example 2.2 of the coefficient lesson.

<span id="3-a-representation-at-every-point-of-the-support"></span>
## 3. A representation at every point of the support

For \(y\in Y\), define on \(\ell^2(G)\)
\[
(d_y(f)\eta)(h)=f(hy)\eta(h),\qquad
(\ell_g\eta)(h)=\eta(g^{-1}h).
\tag{3.1}
\]
They satisfy \(\ell_gd_y(f)\ell_g^*=d_y(\alpha_g(f))\). On polynomials set
\[
\rho_y(P)=\sum_{g\in F}d_y(f_g)\ell_g.
\tag{3.2}
\]

**Theorem 3.1.** For every \(y\in Y\), (3.2) extends to a unital star representation \(\rho_y:C\to B(\ell^2(G))\), with
\[
\|\rho_y(x)\|\leq\|x\|\qquad(x\in C).
\tag{3.3}
\]
Moreover
\[
\omega_y(x)=\langle\rho_y(x)\delta_e,\delta_e\rangle=F(x)(y)
\tag{3.4}
\]
is a state, and \(y\mapsto\omega_y(x)\) is continuous for every \(x\in C\).

**Proof.** The continuous coefficients in (1.7) are unique. If \(P=0\), normal coefficient recovery gives \(f_g=0\) as an \(L^\infty\) class for each \(g\), and full support makes each continuous \(f_g\) identically zero. Thus (3.2) is well-defined on represented polynomials. Covariance makes it a unital star homomorphism there.

Let \(B:\ell^2(G;L^2(Y,\mu))\to L^2(Y,\mu;\ell^2(G))\) be the Fubini reordering unitary, and put \(U=BW\). Equations (2.2) identify
\[
UPU^*=\int_Y^\oplus \rho_y(P)\,d\mu(y).
\tag{3.5}
\]
Explicitly, on the right a term acts by
\(f_g(hy)\eta(y,g^{-1}h)\), exactly the reordered regular action. The field is measurable: its matrix entries are continuous functions of \(y\). It is uniformly bounded by \(\sum_g\|f_g\|_\infty\). The existing decomposable-norm theorem therefore gives
\[
\|P\|=\operatorname*{ess\,sup}_{y\in Y}\|\rho_y(P)\|.
\tag{3.6}
\]

For a finitely supported vector \(\eta\in\ell^2(G)\), the vector \(\rho_y(P)\eta\) has support in the fixed finite set \(F\operatorname{supp}\eta\), and all its entries are continuous in \(y\). Thus \(y\mapsto\|\rho_y(P)\eta\|\) is continuous. The operator norm is the supremum over finitely supported unit vectors, so \(y\mapsto\|\rho_y(P)\|\) is lower semicontinuous.

If its value at some \(y_0\in Y\) exceeded \(\|P\|\), one such finite vector would give that strict inequality on a neighborhood of \(y_0\). Full support gives this neighborhood positive measure, contradicting (3.6). Thus (3.3) holds for every polynomial at every point, and norm completion extends \(\rho_y\) to \(C\). Multiplication and adjoints persist by norm continuity.

On a polynomial, the inner product in (3.4) selects its identity coefficient \(f_e(y)\). Both sides extend continuously in \(x\), the right side by (2.5) and the left side by (3.3). This proves (3.4). The unit vector state of a unital representation is a state. Uniform approximation by polynomials also makes \(y\mapsto\omega_y(x)\) continuous. \(\square\)

This proof supplies a representation at every point of \(Y\), including points of measure zero. An almost-everywhere field assertion by itself would not supply that pointwise conclusion.

<span id="4-purity-and-unitary-equivalence"></span>
## 4. Purity and unitary equivalence

**Theorem 4.1.** Each \(\omega_y\), \(y\in Y\), is pure, and its GNS representation is \(\rho_y\) with cyclic vector \(\delta_e\). The representations \(\rho_{y_1}\) and \(\rho_{y_2}\) are unitarily equivalent exactly when
\[
Gy_1=Gy_2.
\tag{4.1}
\]

**Proof.** The vector \(\delta_e\) is cyclic because
\(\rho_y(t_g)\delta_e=\delta_g\).
Let \(T\) commute with \(\rho_y(C)\). Commutation with \(d_y(C(Y))\) gives, for its matrix entries,
\[
\bigl(f(hy)-f(ky)\bigr)T_{h,k}=0
\quad(f\in C(Y),\ h,k\in G).
\tag{4.2}
\]
Freeness makes \(hy\ne ky\) when \(h\ne k\), and continuous functions separate these points. Hence all off-diagonal entries vanish. Commutation with every left translation \(\ell_g\) then makes all diagonal entries equal. Thus \(T\) is scalar. The representation is irreducible. Cyclic representation uniqueness identifies it with the GNS representation of (3.4), and the existing pure-state theorem makes \(\omega_y\) pure.

Identify \(\ell^2(G)\) with \(\ell^2(Gy)\) by \(\delta_h\mapsto\delta_{hy}\), using freeness. In this orbit model the representation \(\Pi_y\) satisfies
\[
\begin{aligned}
(\Pi_y(\pi'(f))\eta)(z)&=f(z)\eta(z),\\
(\Pi_y(t_g)\eta)(z)&=\eta(g^{-1}z),
\qquad z\in Gy.
\end{aligned}
\tag{4.3}
\]
These formulas depend only on the orbit set. Equal orbits therefore give the same representation after the canonical basis identification, proving one direction of (4.1).

Conversely, if a unitary \(T:\ell^2(G)\to\ell^2(G)\) intertwines \(\rho_{y_1}\) with \(\rho_{y_2}\), multiplication intertwining gives
\[
\bigl(f(hy_2)-f(ky_1)\bigr)T_{h,k}=0
\qquad(f\in C(Y)).
\]
A unitary has some nonzero matrix entry. At that entry, separation by continuous functions implies \(hy_2=ky_1\). The two orbits intersect and hence are equal. \(\square\)

For a polynomial, the orbit formula is explicitly
\[
(\Pi_y(P)\eta)(hy)
=\sum_{g\in F} f_g(hy)\eta(g^{-1}hy).
\tag{4.4}
\]
General elements of \(C\) act by the norm-continuous extension of these finite formulas.

The state retains the point: \(\omega_y(\pi'(f))=f(y)\), so distinct \(y\) give distinct states. The representation retains the orbit, as (4.1) states.

<span id="5-the-orthogonal-representing-measure"></span>
## 5. The orthogonal representing measure

Let \(\mathfrak S(C)\) be the compact state space of \(C\), with its weak-star topology. Define
\[
j:Y\longrightarrow\mathfrak S(C),\qquad j(y)=\omega_y,\qquad
\nu=j_*\mu.
\tag{5.1}
\]
Theorem 3.1 makes \(j\) continuous. Its restriction to continuous coefficient functions makes it injective, so it is a homeomorphism from compact \(Y\) onto its closed image. This image consists entirely of pure states.

**Theorem 5.1.** The measure \(\nu\) represents \(\varphi=\Phi|_C\):
\[
\varphi(x)=\int_Y\omega_y(x)\,d\mu(y)
=\int_{\mathfrak S(C)}\omega(x)\,d\nu(\omega).
\tag{5.2}
\]
It is orthogonal, and its associated abelian algebra in the GNS commutant is exactly the original coefficient algebra \(\pi(D)\), which is maximal abelian in \(R=S'\).

**Proof.** Equation (5.2) follows from (2.4) and (3.4). We first identify the GNS space of \(\varphi\). Since \(W\xi_0=\xi_0\), the reordered vector \(U\xi_0\) is the constant section \(y\mapsto\delta_e\). The vectors
\[
\pi(f)u_g\xi_0
\]
in the regular model have only coordinate \(g\) nonzero, with value
\(\alpha_{g^{-1}}(f)\in C(Y)\). As \(f\) varies, these values range over all \(C(Y)\). Their span is dense in \(\ell^2(G;L^2(Y,\mu))\), by density of continuous functions and finite-coordinate vectors. Thus \(\xi_0\) is cyclic for \(C\), and its given representation on \(\mathcal K\) is the GNS representation of \(\varphi\).

For \(h\in L^\infty(Y,\mu)\), let \(m_h\) denote multiplication by \(h(y)\) on \(L^2(Y,\mu;\ell^2(G))\). Equations (2.2) give
\[
U\pi(h)U^*=m_h.
\tag{5.3}
\]
This multiplier commutes with the reordered action of \(C\). For
\(q\in L^\infty(\mathfrak S(C),\nu)\), put
\[
\kappa(q)=U^*m_{q\circ j}U=\pi(q\circ j).
\tag{5.4}
\]
It is a normal unital star homomorphism into the GNS commutant. For every \(x\in C\), the polynomial calculation in (3.5), followed by norm approximation, gives
\[
\begin{aligned}
\langle\kappa(q)x\xi_0,\xi_0\rangle
&=\int_Y q(j(y))
   \langle\rho_y(x)\delta_e,\delta_e\rangle\,d\mu(y)\\
&=\int_{\mathfrak S(C)}q(\omega)\omega(x)\,d\nu(\omega).
\end{aligned}
\tag{5.5}
\]
Hence uniqueness in the existing operator-map theorem identifies (5.4) with \(\kappa_\nu\). Its multiplicativity makes \(\nu\) orthogonal by the existing orthogonal-measure criterion. The homeomorphism \(j\) onto a closed full-\(\nu\)-measure subspace identifies \(L^\infty(\nu)\) with \(L^\infty(Y,\mu)\). Thus the range in (5.4) is exactly \(\pi(D)\).

Finally the induced action on \(D\) is free in the algebraic sense. If a projection \(p=1_B\) supported an identity part for \(\alpha_g\), then
\[
(f(g^{-1}y)-f(y))1_B(y)=0
\]
for every \(f\in C(Y)\). Take a countable norm-dense separating family of such functions and remove the union of its null exceptional sets. For the remaining \(y\in B\), equality holds for the dense family, hence for every continuous function. Separation gives \(g^{-1}y=y\). If \(g\ne e\), point freeness excludes this, so \(B\) is null and \(p=0\). The free-action MASA theorem now gives
\(\pi(D)'\cap R=\pi(D)\).
Since \(C''=S=R'\), its GNS commutant is \(R\), proving the final assertion. \(\square\)

The integral in (5.2) is a representing measure for the state on the separable \(C^*\)-algebra \(C\). Formula (2.4) separately describes its normal vector-state extension to \(S\).

**Proposition 5.2.** The pure state \(\omega_y\) has a normal state extension to \(S\) exactly when \(\mu(\{y\})>0\).

**Proof.** If \(\mu(\{y\})=0\), choose a compatible metric on \(Y\) and set
\[
f_n(z)=\max\{1-n\,d(z,y),0\}.
\]
These continuous positive contractions decrease pointwise to \(1_{\{y\}}\), which is zero as an \(L^\infty(\mu)\) class. Thus \(\pi'(f_n)\downarrow0\) in \(S\). A normal state extension would have values decreasing to zero. But its values on these elements must be \(\omega_y(\pi'(f_n))=f_n(y)=1\), a contradiction.

If \(\mu(\{y\})>0\), the section
\[
\zeta(z)=\mu(\{y\})^{-1/2}1_{\{y\}}(z)\delta_e
\]
is a unit vector in \(L^2(Y,\mu;\ell^2(G))\). The vector state at \(U^*\zeta\), restricted to \(S\), is normal, and (3.5) gives its value \(\omega_y(P)\) for every polynomial \(P\). Norm density gives the same equality on all \(C\). It is the required normal state extension. \(\square\)

<span id="6-graded-exercises-with-complete-solutions"></span>
## 6. Graded exercises with complete solutions

**Exercise 6.1 (introductory: the support qualification).** Let
\(X=\{0,1,2,3\}\) with the discrete topology. The two-element group acts by the permutation \((0\,1)(2\,3)\). Give \(0,1\) mass \(1/2\) each and \(2,3\) mass zero. Check freeness and quasi-invariance, then show that evaluation of the identity coefficient at \(2\) does not define a state on the represented algebra \(C\). Identify the correct support space and the represented \(C^*\)-algebra.

*Solution.* The only nonidentity group element moves every point, so the point action is free. It preserves the measure, hence the measure is quasi-invariant. Its support is \(Y=\{0,1\}\).

The continuous function \(q=1_{\{2,3\}}\) acts as zero on \(L^2(X,\mu)\), and therefore \(\pi'(q)=0\) in \(C\). Its putative identity-coefficient evaluation at \(2\) would be \(q(2)=1\). The same represented zero element also has the zero polynomial expression, whose evaluation is \(0\). Thus the proposed functional is not even well-defined.

On \(Y\), continuous functions give both diagonal projections in the orbit model, and the group generator swaps the two basis vectors. Compressing this swap between the diagonal projections gives the two off-diagonal matrix units. Hence the orbit representation has image \(M_2(\mathbb C)\). The two support points have the same orbit and unitarily equivalent representations. The norm formula in Theorem 3.1, with this finite full support, identifies the represented algebra \(C\) with \(M_2(\mathbb C)\). Its two point states are the two diagonal vector states.

**Exercise 6.2 (intermediate: unequal finite orbit weights).** Let \(Y=\mathbb Z/3\mathbb Z\), let \(G=\mathbb Z/3\mathbb Z\) act by addition, and give the points \(0,1,2\) respective masses \(1/7,2/7,4/7\). Identify \(C\), the three pure states, their GNS representations, the barycentre state and its orthogonal measure. Is the barycentre tracial?

*Solution.* The action is free. Every point has positive mass, so the support is all of \(Y\), and each transported measure is equivalent to \(\mu\). In the common orbit space \(\ell^2(Y)\), the coefficient functions act by all diagonal matrices and the group generator acts by the cyclic permutation matrix. The diagonal compressions of its powers give every matrix unit. Thus \(C\cong M_3(\mathbb C)\), with the represented norm justified by Theorem 3.1.

For each \(y\), (4.3) is the usual irreducible representation of \(M_3\) on \(\mathbb C^3\), using the same orbit basis. The state is
\(\omega_y(x)=x_{y,y}\). These are the three pure diagonal vector states. Their GNS representations are all unitarily equivalent, though their restrictions to the diagonal distinguish the three points.

The barycentre is
\[
\varphi(x)=\frac{x_{0,0}+2x_{1,1}+4x_{2,2}}7
=\operatorname{Tr}\!\left(
  \operatorname{diag}(1,2,4)x/7\right).
\]
Its representing measure places masses \(1/7,2/7,4/7\) at the respective \(\omega_y\). Theorem 5.1 makes it orthogonal. More concretely, its GNS space is the weighted sum of three copies of the usual irreducible representation, of total dimension \(9\); diagonal multiplication on the copy index is the associated three-atom algebra in the commutant.

It is not tracial: for the matrix unit \(e_{0,1}\),
\[
\varphi(e_{0,1}^*e_{0,1})=\frac27,\qquad
\varphi(e_{0,1}e_{0,1}^*)=\frac17.
\]
Quasi-invariance suffices for the orbit-state decomposition; it does not impose invariance of the finite weights.

**Exercise 6.3 (advanced: pure states on irrational circle orbits).** Let an irrational real number \(\theta\) define the action
\[
n\cdot x=x+n\theta\pmod1
\]
of \(\mathbb Z\) on \(\mathbb T\), with normalized Lebesgue measure. Prove that every point defines a pure state. Compare the representations at \(0,\theta,\theta/2\). Determine whether any of these point states has a normal extension to \(S\).

*Solution.* Lebesgue measure is invariant and has full support. If \(n\theta\) is an integer for \(n\ne0\), then \(\theta\) is rational; hence the point action is free. Theorem 4.1 gives a pure state at every point, with GNS space \(\ell^2(\mathbb Z)\).

The points \(0\) and \(\theta\) lie in the same orbit, so their GNS representations are unitarily equivalent. Their states are distinct: evaluation on the coefficient function \(f(x)=e^{2\pi i x}\) gives \(1\) and \(e^{2\pi i\theta}\), respectively.

The point \(\theta/2\) is not in the orbit of \(0\). Otherwise \(\theta/2=n\theta+k\) for integers \(n,k\), which would make \(\theta=-k/(n-1/2)\) rational. Thus its orbit is disjoint from that of \(0\), and Theorem 4.1 makes the two representations inequivalent.

Every singleton has Lebesgue measure zero. Proposition 5.2 therefore excludes a normal state extension to \(S\) for every one of these point states. Nevertheless their continuous pure-state family has the normal vector-state restriction \(\varphi\) as its integral, with the orthogonal measure supplied by Theorem 5.1.

<span id="references"></span>
## References

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer-Verlag, 1979, Chapter V, §7, Exercise 2(a–d), printed p. 373. The pointwise assertions require the support qualification proved above.

[Existing commutant theorem] OA-FLOW, *The regular commutant in every covariant representation*, equation E9, specialized to the multiplication representation. Its proof uses the standard-form commutant and normal representation-comparison results linked above.

[Earlier lessons] The exact regular coefficient, decomposable norm, GNS and orthogonal-measure proof contracts linked above.

# Entropy defect and abelian models

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. Public domain (CC0).*

## Introduction

In classical ergodic theory the entropy of a finite partition \(\alpha\) of a probability space is
\(H(\alpha)=\sum_{a\in\alpha}\eta(\mu(a))\), with \(\eta(s)=-s\log s\), and the entropy of a transformation is built
from the entropies of the joins \(\alpha\vee T^{-1}\alpha\vee\dots\vee T^{-k+1}\alpha\). A noncommutative version must
replace the partitions by finite-dimensional "observations" of a C\*-algebra \(A\) in a state \(\varphi\), and it must
say how much information a finite family of such observations carries jointly. This lesson constructs that quantity,
\(H_\varphi(\gamma_1,\dots,\gamma_n)\), for an arbitrary unital C\*-algebra and an arbitrary state, and proves its
basic properties. It is the static half of the dynamical entropy of a state-preserving automorphism, which is the
subject of the lesson "Dynamical entropy of C\*-algebras and von Neumann algebras".

Two features make the problem harder than in the tracial case treated in "Entropy of finite-dimensional subalgebras".
First, a general C\*-algebra may have no finite-dimensional subalgebra other than the scalars, so the observations
are unital completely positive maps \(\gamma_j:A_j\to A\) whose domains \(A_j\) are finite-dimensional C\*-algebras, not
subalgebras.
Second, for a state that is not a trace the restriction \(\varphi|_N\) to a subalgebra is badly behaved: there is in
general no \(\varphi\)-preserving conditional expectation onto \(N\), and the von Neumann entropy of \(\varphi|_N\) is
not monotone in \(N\). The remedy is to compare the noncommutative situation with *abelian models*: completely positive
maps \(P:A\to B\) into finite-dimensional abelian algebras with a state \(\mu\) such that \(\mu\circ P=\varphi\). Such a
model is the same thing as a decomposition \(\varphi=\sum_x\mu_x\varphi_x\) of \(\varphi\) into states, that is, a
"measurement". The Shannon entropy \(S(\mu)\) of the model overestimates the information it gives about \(A\), and the
amount of overestimation is the *entropy defect* \(s_\mu(P)\). The entropy \(H_\varphi(\gamma_1,\dots,\gamma_n)\) is the
supremum, over all abelian models with \(n\) marked subalgebras, of the Shannon entropy of the join minus the sum of all
entropy defects.

The lesson is organized as follows.

1. Unital positive maps into finite-dimensional abelian algebras and the canonical conditional expectations (Section 1).
2. Relative entropy of positive functionals on an arbitrary unital C\*-algebra, *defined* by a variational expression,
   with all properties used later proved from that definition; in finite dimensions it agrees with the Umegaki formula
   \(\operatorname{Tr}\rho_\psi(\log\rho_\psi-\log\rho_\varphi)\) (Section 2).
3. Von Neumann entropy and the entropy of mixtures (Section 3).
4. The Holevo quantity \(\varepsilon_\mu(P)\) and the entropy defect \(s_\mu(P)\) of a map into an abelian algebra
   (Section 4), including the subadditivity of the defect under joins (Theorem 4.8).
5. Completely positive maps out of matrix algebras, and the approximation of nuclear C\*-algebras (Section 5).
6. Abelian models and the definition of \(H_\varphi\) (Section 6), with its description by decompositions of
   \(\varphi\) (Proposition 6.4) and its value for abelian algebras (Proposition 6.6).
7. Monotonicity, subadditivity, convexity and concavity properties of \(H_\varphi\) (Section 7).
8. Continuity of \(H_\varphi\) in the norm topology, with an explicit modulus (Section 8).

*What is assumed.* Basic C\*-algebra theory, states and the GNS construction, and completely positive maps; for two
remarks, enveloping von Neumann algebras and conditional expectations. "Results used from other lessons" lists these
facts with the place where each is proved. From classical
information theory we use the elementary properties of the Shannon entropy of finite random variables. The lesson
"Entropy of finite-dimensional subalgebras" of this course is useful motivation but is not used. Everything else,
including all the properties of relative entropy that are needed, is proved here; the facts used from other lessons
are listed below, with the place where each is proved.

Basic references are [Connes–Narnhofer–Thirring 1987], [Connes–Størmer 1975], [Kosaki 1986] and [Connes 1994].

## Results used from other lessons

**(B1) Finite-dimensional C\*-algebras.** A finite-dimensional C\*-algebra \(A\) is isomorphic to
\(\bigoplus_{k=1}^r M_{n_k}(\mathbb C)\). Its *canonical trace* \(\operatorname{Tr}\) is the sum of the usual matrix
traces; it takes the value \(1\) on every minimal projection. Put \(N(A)=\operatorname{Tr}(1)=\sum_kn_k\), so
\(N(A)\le\dim A\). Every linear functional \(\omega\) on \(A\) has a unique *density* \(\rho_\omega\in A\) with
\(\omega(a)=\operatorname{Tr}(\rho_\omega a)\); \(\omega\) is positive iff \(\rho_\omega\ge0\), and
\(\|\omega\|=\|\rho_\omega\|_1:=\operatorname{Tr}|\rho_\omega|\). For \(a,b,c\in A\) one has
\(|\operatorname{Tr}(b)|\le\|b\|_1\) and \(\|abc\|_1\le\|a\|\,\|b\|_1\,\|c\|\). Every self-adjoint \(z\in A\) can be
written \(z=\sum_{k=1}^{N(A)}\lambda_ke_k\) with pairwise orthogonal minimal projections \(e_k\) of \(A\) summing to
\(1\); the \(\lambda_k\) are the *eigenvalues* of \(z\) counted with multiplicity, and
\(\operatorname{Tr}f(z)=\sum_kf(\lambda_k)\). The structure and the traces are proved in AF-algebras, Section 2 and
Lemma 10.2; by Lemma 2.2(1) there a self-adjoint element is a real combination of orthogonal
projections, and splitting these into minimal ones gives the eigenvalue decomposition. Densities, the trace norm and the
inequalities for it are the finite-dimensional case of Compact and trace-class operators, Sections 4–6
(Corollary 4.4(a) and Theorem 4.6 for the inequalities, Section 6 for the duality \(\|\omega\|=\|\rho_\omega\|_1\)),
applied in each summand.

**(B2) Completely positive maps.** Compositions and sums of completely positive maps are completely positive;
\(*\)-homomorphisms and compressions \(a\mapsto v^*av\) (with \(v\) a rectangular matrix over the algebra) are
completely positive. A unital completely positive map \(\gamma\) satisfies \(\|\gamma\|=1\) and the *Kadison–Schwarz
inequality* \(\gamma(a)^*\gamma(a)\le\gamma(a^*a)\). A positive map whose domain is abelian is completely positive
(Stinespring's theorem). A *conditional expectation* of a C\*-algebra \(A_0\) onto a C\*-subalgebra \(A\ni1\) is a
positive unital map \(E:A_0\to A\) with \(E(a)=a\) and \(E(a b a')=aE(b)a'\) for \(a,a'\in A\), \(b\in A_0\); it is
automatically completely positive (Tomiyama's theorem). Proved in Completely positive maps:
compositions, sums and \(*\)-homomorphisms are completely positive by definition, and compressions by Theorem 6.1(1) and
Example 6.4 there; the Kadison–Schwarz inequality and \(\|\gamma\|=\|\gamma(1)\|\) are Theorem 4.1(1)–(2); positive maps
with abelian domain are completely positive by Theorem 5.4(2). For a conditional expectation, the criterion of
Proposition 3.2(1) there applies directly: for \(x_i\in A_0\) and \(y_i\in A\),
\(\sum_{i,j}y_i^*E(x_i^*x_j)y_j=E\big((\sum_ix_iy_i)^*(\sum_jx_jy_j)\big)\ge0\). The version for norm-one projections is
Contractive retractions and the algebraic structure of expectations, §§CE-004 and CE-006.
See also [Tomiyama 1957].

**(B3) GNS and dominated functionals.** Let \((\pi_\varphi,H_\varphi,\xi_\varphi)\) be the GNS triple of a positive
functional \(\varphi\) on \(A\). If \(\psi\) is a positive functional with \(\psi\le\varphi\), there is a unique
\(t\in\pi_\varphi(A)'\) with \(0\le t\le1\) and \(\psi(a)=\langle\xi_\varphi,t\pi_\varphi(a)\xi_\varphi\rangle\) for
all \(a\); conversely every such \(t\) defines a positive functional \(\psi\le\varphi\). If \(A\) is abelian,
\(\pi_\varphi(A)'\) is abelian (an abelian von Neumann algebra with a cyclic vector is maximal abelian). Proved in Representations and positive
functionals, Lemma 8.1 and Projections and types of von Neumann algebras, Lemma
11.1.

**(B4) Shannon entropy.** For random variables \(U,V,W\) with finitely many values on a finite probability space, with
\(H(U)=\sum_u\eta(P(U=u))\) and \(H(U\mid V)=H(U,V)-H(V)\): \(H(U)\le H(U,V)\);
\(H(U,V)\le H(U)+H(V)\); \(H(U\mid V,W)\le H(U\mid V)\); \(H(U_1,\dots,U_n\mid V)\le\sum_jH(U_j\mid V)\). For
probability vectors \(p_1,p_2\) and \(\lambda\in[0,1]\),
\(\lambda H(p_1)+(1-\lambda)H(p_2)\le H(\lambda p_1+(1-\lambda)p_2)\le\lambda H(p_1)+(1-\lambda)H(p_2)+h(\lambda)\),
where \(h(\lambda)=\eta(\lambda)+\eta(1-\lambda)\). Proved in Operator convex functions and the continuity of
entropy, Proposition 4.1.

**(B5) Nuclear C\*-algebras.** A C\*-algebra \(A\) is nuclear iff it has the *completely positive approximation
property*: there are nets of completely positive contractions \(\sigma_i:A\to M_{n_i}(\mathbb C)\) and
\(\tau_i:M_{n_i}(\mathbb C)\to A\) with \(\|\tau_i\sigma_i(a)-a\|\to0\) for every \(a\in A\) (the Choi–Effros
theorem and its converse). Abelian C\*-algebras are nuclear. Proved in the course *Positive maps and
finite-dimensional approximation*: the equivalence in Tensor positivity and nuclearity, Theorem
3.1; abelian algebras have the approximation property by Completely
positive finite models, Theorem 3.3.

**(B6) Takesaki's theorem.** Fix a von Neumann algebra \(M\) with a faithful normal state \(\omega\), and a von Neumann
subalgebra \(N\subset M\). There is a conditional expectation \(E:M\to N\) with \(\omega\circ E=\omega\) iff
\(\sigma^\omega_t(N)=N\) for all \(t\); it is then unique. Proved in Conditional expectations from modular
invariance, §§ME-01 and ME-08. See also [Takesaki 1972]. (Used only in Remark 1.5.)

**(B7) Relative entropy of normal states.** For positive functionals on a C\*-algebra, the quantity \(D(\psi\|\varphi)\)
of Definition 2.1 equals the relative entropy of the normal extensions of \(\psi\) and \(\varphi\) to the enveloping von
Neumann algebra, defined through the relative modular operator. Reference: [Kosaki 1986]; see also [Araki 1976].
(Used only in Remark 2.8.)

## 1. Positive maps into abelian algebras

Throughout, \(A\) is a unital C\*-algebra, \(A^*_+\) its positive linear functionals and \(\Sigma(A)\) its states. All
maps between C\*-algebras are linear. For a finite set \(X\) we write \(C(X)=\mathbb C^X\), \(\delta_x\) for evaluation at
\(x\) and \(1_K\) for the indicator of \(K\subset X\). A state \(\mu\) on \(C(X)\) is a probability vector
\(\mu_x=\mu(1_{\{x\}})\), and \(\mu(K)=\mu(1_K)\). Every finite-dimensional abelian C\*-algebra is of the form \(C(X)\).

**Lemma 1.1.** *(a) If \((\omega_x)_{x\in X}\) is a family of states on \(A\), then \(P(a)(x)=\omega_x(a)\) defines a
unital completely positive map \(P:A\to C(X)\). Every unital positive map \(P:A\to C(X)\) arises in this way, from
\(\omega_x=P_x:=\delta_x\circ P\); in particular it is completely positive.*

*(b) The unital positive maps \(A\to C(X)\) form a convex set, closed under pointwise limits. Its extreme points are the
maps \(P\) for which every \(P_x\) is a pure state.*

**Proof.** (a) Each \(\omega_x\) is positive and \(\omega_x(1)=1\), so \(P\) is unital and positive. For complete
positivity let \([a_{ij}]\in M_m(A)\) be positive. The element \([P(a_{ij})]\) of \(M_m(C(X))=C(X,M_m(\mathbb C))\) is
positive iff for every \(x\) the scalar matrix \([\omega_x(a_{ij})]\) is positive. For \(\zeta\in\mathbb C^m\) let
\(v\in M_{m,1}(A)\) be the column with entries \(\zeta_j1\). Then
\(\sum_{i,j}\bar\zeta_i\omega_x(a_{ij})\zeta_j=\omega_x(v^*[a_{ij}]v)\ge0\), because \(v^*[a_{ij}]v\ge0\). Conversely,
if \(P\) is unital and positive, each \(\delta_x\circ P\) is a state and \(P(a)(x)=(\delta_x\circ P)(a)\).

(b) By (a), \(P\mapsto(P_x)_{x\in X}\) is an affine bijection onto \(\Sigma(A)^X\), and pointwise limits of unital
positive maps are unital positive. If some \(P_{x_0}\) is not pure, write
\(P_{x_0}=\tfrac12(\omega'+\omega'')\) with states \(\omega'\ne\omega''\) and let \(P',P''\) agree with \(P\) except
that \(P'_{x_0}=\omega'\), \(P''_{x_0}=\omega''\); then \(P=\tfrac12(P'+P'')\) with \(P'\ne P''\). Conversely, if every
\(P_x\) is pure and \(P=tP'+(1-t)P''\) with \(0<t<1\), then \(P_x=tP'_x+(1-t)P''_x\) forces \(P'_x=P''_x=P_x\) for every
\(x\). \(\square\)

**Lemma 1.2.** *Every unital \(*\)-subalgebra \(C\subset C(X)\) is the algebra of functions constant on the blocks of a
unique partition \(\pi(C)\) of \(X\), and its minimal projections are the \(1_K\), \(K\in\pi(C)\). The subalgebra
\(C_1\vee C_2\) generated by \(C_1\) and \(C_2\) corresponds to the common refinement
\(\pi(C_1)\vee\pi(C_2)=\{K\cap L\ne\emptyset:K\in\pi(C_1),L\in\pi(C_2)\}\).*

**Proof.** \(C\) is a finite-dimensional abelian C\*-algebra, so it is spanned by its minimal projections, which are
pairwise orthogonal and sum to \(1\). A projection in \(C(X)\) is an indicator \(1_K\); orthogonal indicators with sum
\(1\) are the indicators of the blocks of a partition. The algebra generated by \(C_1\) and \(C_2\) is spanned by the
products \(1_K1_L=1_{K\cap L}\). \(\square\)

**Definition 1.3.** Let \(\mu\) be a state on \(C(X)\) and \(C\subset C(X)\) a unital \(*\)-subalgebra with partition
\(\pi=\pi(C)\). The *canonical conditional expectation* \(E^\mu_C:C(X)\to C\) is
\[
E^\mu_C(f)=\sum_{K\in\pi}m_K(f)1_K,\qquad
m_K(f)=\begin{cases}\mu(f1_K)/\mu(K)&\text{if }\mu(K)>0,\\ |K|^{-1}\sum_{x\in K}f(x)&\text{if }\mu(K)=0.\end{cases}
\]

**Lemma 1.4.** *(a) \(E^\mu_C\) is a conditional expectation onto \(C\) and \(\mu\circ E^\mu_C=\mu\).*

*(b) If \(E'\) is any conditional expectation onto \(C\) with \(\mu\circ E'=\mu\), then \(E'(f)1_K=E^\mu_C(f)1_K\) for
every block \(K\) with \(\mu(K)>0\).*

*(c) If \(C_1\subset C_2\), then \(E^\mu_{C_1}\circ E^\mu_{C_2}\) agrees with \(E^\mu_{C_1}\) on every block of
\(\pi(C_1)\) of positive measure.*

**Proof.** (a) Each \(m_K\) is a state, so \(E^\mu_C\) is unital and positive. If \(g\in C\) takes the value \(g_K\) on
\(K\), then \(m_K(gf)=g_Km_K(f)\), which gives \(E^\mu_C(gf)=gE^\mu_C(f)\), and \(E^\mu_C(g)=g\). Finally
\(\mu(E^\mu_C(f))=\sum_{\mu(K)>0}\mu(K)m_K(f)=\sum_K\mu(f1_K)=\mu(f)\).

(b) Write \(E'(f)=\sum_Kc_K1_K\). Bimodularity and invariance give
\(c_K\mu(K)=\mu(E'(f)1_K)=\mu(E'(f1_K))=\mu(f1_K)\).

(c) \(E^\mu_{C_1}\circ E^\mu_{C_2}\) is a \(\mu\)-preserving conditional expectation onto \(C_1\) (a composition of
unital positive maps, \(C_1\)-bimodular because \(C_1\subset C_2\), equal to the identity on \(C_1\)); apply (b).
\(\square\)

The values of \(E^\mu_C\) on null blocks play no role anywhere below; the convention only makes the expectation
unique.

**Remark 1.5 (vocabulary).** For later use we collect the terminology. A map between C\*-algebras is *unital* if it
preserves the unit, and *completely positive* if all its matrix amplifications
\([a_{ij}]\mapsto[\gamma(a_{ij})]\) are positive. Unital completely positive maps are closed under composition and
form a convex set closed under pointwise norm limits; \(*\)-homomorphisms, in particular inclusions of unital
subalgebras, are among them. They satisfy the Kadison–Schwarz inequality (B2). Positive maps into or out of abelian
algebras are completely positive (Lemma 1.1 and (B2)), and conditional expectations are completely positive (B2). For
a faithful normal state \(\omega\) of a von Neumann algebra, a subalgebra admits an \(\omega\)-preserving conditional
expectation iff it is invariant under the modular group of \(\omega\), and then the expectation is unique (B6); we call
it canonically associated with \(\omega\). For abelian finite-dimensional algebras the modular group is trivial and
Lemma 1.4 is the elementary form of this statement, with the null blocks treated by convention.

## 2. Relative entropy

We define the relative entropy of two positive functionals on any
unital C\*-algebra by a variational expression. Every property used later follows from the definition, and in finite
dimensions the definition gives back the familiar formula (Theorem 2.3).

**Definition 2.1.** A *path* in \(A\) is a function \(x:(0,\infty)\to A\) for which there are
\(0<t_0<t_1<\dots<t_m\) such that \(x(t)=0\) for \(t<t_0\), \(x(t)=1\) for \(t\ge t_m\), and \(x\) is constant on each
\([t_{k-1},t_k)\). Put \(y(t)=1-x(t)\). For \(\psi,\varphi\in A^*_+\) let
\[
F_x(\psi\|\varphi)=\int_0^\infty\Bigl(\frac{\psi(1)}{1+t}-\psi\bigl(y(t)^*y(t)\bigr)
-\frac1t\,\varphi\bigl(x(t)x(t)^*\bigr)\Bigr)\frac{dt}t,
\qquad
D(\psi\|\varphi)=\sup_xF_x(\psi\|\varphi).
\tag{2.1}
\]
\(D(\psi\|\varphi)\) is the *relative entropy of \(\psi\) with respect to \(\varphi\)*.

We write \(I_{\psi,\varphi}(t,x)\) for the integrand of (2.1) at time \(t\) and a fixed element \(x\in A\).

**Lemma 2.2.** *For every path \(x\) the integral in (2.1) converges absolutely, and there are \(a_x=a_x^*\in A\) and
\(b_x\in A_+\), depending only on \(x\), with \(F_x(\psi\|\varphi)=\psi(a_x)-\varphi(b_x)\). In particular \(F_x\) is
jointly linear in \((\psi,\varphi)\) and weak\* continuous.*

**Proof.** For \(t<t_0\) the integrand equals \(t^{-1}(\psi(1)(1+t)^{-1}-\psi(1))=-\psi(1)(1+t)^{-1}\); for \(t\ge t_m\)
it equals \(\psi(1)t^{-1}(1+t)^{-1}-\varphi(1)t^{-2}\); on \([t_0,t_m)\) it is bounded. So the integral converges
absolutely, and it equals \(\psi(a_x)-\varphi(b_x)\) with
\(a_x=\int_0^\infty\bigl((1+t)^{-1}-y(t)^*y(t)\bigr)t^{-1}dt\) and \(b_x=\int_{t_0}^\infty x(t)x(t)^*t^{-2}dt\),
which are finite sums of elements of \(A\) with explicit scalar coefficients. \(\square\)

**Theorem 2.3 (finite dimensions).** *Let \(A\) be finite-dimensional and \(\psi,\varphi\in A^*_+\) with densities
\(\rho_\psi,\rho_\varphi\). Then*
\[
D(\psi\|\varphi)=\begin{cases}\operatorname{Tr}\bigl(\rho_\psi\log\rho_\psi\bigr)-\operatorname{Tr}\bigl(\rho_\psi
\log\rho_\varphi\bigr)&\text{if }\operatorname{supp}\rho_\psi\le\operatorname{supp}\rho_\varphi,\\
+\infty&\text{otherwise,}\end{cases}
\tag{2.2}
\]
*where \(\log\) is taken on the support (\(0\log0=0\)).*

**Proof.** Write \(\rho_\varphi=\sum_a\alpha_ap_a\) and \(\rho_\psi=\sum_b\beta_bq_b\) with distinct eigenvalues and the
corresponding spectral projections \(p_a,q_b\in A\) (eigenvalue \(0\) allowed), and put
\(w_{ab}=\operatorname{Tr}(p_aq_b)=\|p_aq_b\|_2^2\ge0\), where \(\|z\|_2^2=\operatorname{Tr}(z^*z)\). Then
\(\sum_aw_{ab}=\operatorname{Tr}q_b\), \(\sum_bw_{ab}=\operatorname{Tr}p_a\) and \(w_{ab}=0\) iff \(p_aq_b=0\).

*Step 1: the pointwise infimum.* Fix \(t>0\) and put \(q_t(x)=\psi((1-x)^*(1-x))+t^{-1}\varphi(xx^*)\) for \(x\in A\).
With \(x_{ab}=p_axq_b\),
\[
\psi(y^*y)=\operatorname{Tr}(y\rho_\psi y^*)=\sum_{a,b}\beta_b\|p_ayq_b\|_2^2,\qquad
\varphi(xx^*)=\operatorname{Tr}(\rho_\varphi xx^*)=\sum_{a,b}\alpha_a\|p_axq_b\|_2^2,
\]
so \(q_t(x)=\sum_{a,b}\bigl(\beta_b\|p_aq_b-x_{ab}\|_2^2+t^{-1}\alpha_a\|x_{ab}\|_2^2\bigr)\). The map
\(x\mapsto(x_{ab})\) is a linear bijection of \(A\) onto \(\bigoplus_{a,b}p_aAq_b\) (inverse \((x_{ab})\mapsto\sum
x_{ab}\)), so we may minimize each summand separately over \(z\in p_aAq_b\), a Hilbert space for
\(\langle z,z'\rangle=\operatorname{Tr}(z^*z')\) containing \(c=p_aq_b\). For \(\beta,\kappa\ge0\) with
\(\beta+\kappa>0\), completing the square gives
\(\beta\|c-z\|^2+\kappa\|z\|^2=(\beta+\kappa)\|z-\tfrac\beta{\beta+\kappa}c\|^2+\tfrac{\beta\kappa}{\beta+\kappa}\|c\|^2\).
With \(\kappa=\alpha_a/t\) we obtain
\[
\min_xq_t(x)=\sum_{a,b}w_{ab}\,\frac{\alpha_a\beta_b}{\alpha_a+t\beta_b},
\qquad\text{attained at}\quad x_t=\sum_{a,b}c_{ab}(t)\,p_aq_b,\quad c_{ab}(t)=\frac{t\beta_b}{t\beta_b+\alpha_a},
\tag{2.3}
\]
with the conventions that a fraction with vanishing denominator is \(0\). Since \(\psi(1)=\sum_{a,b}w_{ab}\beta_b\), the
function \(g(t)=\sup_xI_{\psi,\varphi}(t,x)=t^{-1}\bigl(\psi(1)(1+t)^{-1}-\min q_t\bigr)\) is
\(g=\sum_{a,b}w_{ab}g_{ab}\) with
\[
g_{ab}(t)=\begin{cases}0&\beta_b=0,\\ \beta_b\,t^{-1}(1+t)^{-1}&\alpha_a=0<\beta_b,\\
\beta_b\,\dfrac{\beta_b-\alpha_a}{(1+t)(\alpha_a+t\beta_b)}&\alpha_a,\beta_b>0.\end{cases}
\]

*Step 2: integration.* For \(\alpha,\beta>0\), \(\alpha\ne\beta\), partial fractions give
\(\frac{1}{(1+t)(\alpha+\beta t)}=\frac1{\alpha-\beta}\bigl(\frac1{1+t}-\frac\beta{\alpha+\beta t}\bigr)\), hence
\[
\int_0^\infty\frac{\beta-\alpha}{(1+t)(\alpha+\beta t)}\,dt=-\bigl[\log(1+t)-\log(\alpha+\beta t)\bigr]_0^\infty
=\log\frac\beta\alpha,
\tag{2.4}
\]
which also holds for \(\alpha=\beta\). So \(\int_0^\infty g_{ab}=\beta_b\log(\beta_b/\alpha_a)\) if
\(\alpha_a,\beta_b>0\), \(=0\) if \(\beta_b=0\), and \(=+\infty\) if \(\alpha_a=0<\beta_b\). Therefore
\(\int_0^\infty g(t)\,dt=\sum_{a,b:\beta_b>0}w_{ab}\beta_b\log(\beta_b/\alpha_a)\), which is \(+\infty\) iff
\(w_{ab}>0\) for some \(a,b\) with \(\alpha_a=0<\beta_b\), that is, iff \(q_b\) meets the kernel projection of
\(\rho_\varphi\) for some \(\beta_b>0\), that is, iff \(\operatorname{supp}\rho_\psi\not\le
\operatorname{supp}\rho_\varphi\). In the finite case, \(\sum_{a,b}w_{ab}\beta_b\log\beta_b=
\operatorname{Tr}\rho_\psi\log\rho_\psi\) and \(\sum_{a:\alpha_a>0}\sum_bw_{ab}\beta_b\log\alpha_a=
\operatorname{Tr}(\rho_\psi\log\rho_\varphi)\), so \(\int_0^\infty g\) equals the right side of (2.2).

*Step 3: \(D\le\int g\).* For every path, \(I_{\psi,\varphi}(t,x(t))\le g(t)\), so
\(F_x(\psi\|\varphi)\le\int_0^\infty g\) (trivial if \(\int g=+\infty\); otherwise \(g\) is integrable).

*Step 4: \(D\ge\int g\).* Let \(0<\delta<T\). The coefficients \(c_{ab}(t)\) are continuous on \([\delta,T]\) (each is
either constant or a continuous fraction with positive denominator), so \(t\mapsto x_t\) is continuous, and
\(I_{\psi,\varphi}(t,x)\) is jointly continuous on \([\delta,T]\times A\). By uniform continuity on the compact set
\(\{(t,x_s):t,s\in[\delta,T]\}\) there is a partition \(\delta=s_0<\dots<s_m=T\) such that the path
\(x(t)=0\) for \(t<\delta\), \(x(t)=x_{s_{k-1}}\) on \([s_{k-1},s_k)\), \(x(t)=1\) for \(t\ge T\), satisfies
\(\int_\delta^T I(t,x(t))dt\ge\int_\delta^Tg-\theta\), for a given \(\theta>0\). By the computation in Lemma 2.2,
\(|\int_0^\delta I(t,0)\,dt|\le\psi(1)\delta\) and \(|\int_T^\infty I(t,1)\,dt|\le(\psi(1)+\varphi(1))/T\). Hence
\(D(\psi\|\varphi)\ge\int_\delta^Tg-\theta-\psi(1)\delta-(\psi(1)+\varphi(1))/T\). As \(\delta\to0\), \(T\to\infty\),
\(\int_\delta^Tg\to\int_0^\infty g\) termwise (each \(g_{ab}\) is either integrable or positive), and \(\theta\) is
arbitrary. \(\square\)

The right side of (2.2) is the *Umegaki relative entropy*. For \(A=\mathbb C\) it reads
\(D(\beta\|\alpha)=\beta\log(\beta/\alpha)\) for \(\alpha,\beta\ge0\) (with \(0\log\frac0\alpha=0\) and
\(\beta\log\frac\beta0=+\infty\) for \(\beta>0\)).

**Remark 2.4.** One may enlarge the class of paths to step functions with finitely many values that vanish near \(0\),
with no condition at infinity; the supremum does not change. Indeed, if \(x(t)=x_\infty\) for large \(t\) and
\(\psi(y_\infty^*y_\infty)>0\), the integral is \(-\infty\). If \(\psi(y_\infty^*y_\infty)=0\), replacing \(x\) by
\(1\) on \([T,\infty)\) changes the integral by \((\varphi(x_\infty x_\infty^*)-\varphi(1))/T\), which tends to \(0\).
This is the form of the variational expression found in [Kosaki 1986], which builds on work of Pusz and Woronowicz.

**Proposition 2.5 (general properties).** *Let \(\psi,\psi_i,\varphi,\varphi_i\) be positive functionals on a unital
C\*-algebra \(A\).*

*(a) Joint convexity and homogeneity: \(D(\lambda\psi\|\lambda\varphi)=\lambda D(\psi\|\varphi)\) for \(\lambda>0\),
and \(D(\sum_i\lambda_i\psi_i\|\sum_i\lambda_i\varphi_i)\le\sum_i\lambda_iD(\psi_i\|\varphi_i)\) for \(\lambda_i\ge0\),
\(\sum\lambda_i=1\). Equivalently, \(D(\sum_i\psi_i\|\sum_i\varphi_i)\le\sum_iD(\psi_i\|\varphi_i)\).*

*(b) Lower semicontinuity: \((\psi,\varphi)\mapsto D(\psi\|\varphi)\in(-\infty,+\infty]\) is jointly lower semicontinuous
for the weak\* topology.*

*(c) Antitonicity in the reference: \(\varphi_1\le\varphi_2\) implies \(D(\psi\|\varphi_1)\ge D(\psi\|\varphi_2)\).*

*(d) Monotonicity: if \(\gamma:A_0\to A\) is a unital map satisfying the Kadison–Schwarz inequality (for instance a
unital completely positive map), then \(D(\psi\circ\gamma\|\varphi\circ\gamma)\le D(\psi\|\varphi)\). In particular
\(D(\psi|_{A_0}\|\varphi|_{A_0})\le D(\psi\|\varphi)\) for a unital C\*-subalgebra \(A_0\).*

*(e) Invariance: if moreover there is a unital Kadison–Schwarz map \(\beta:A\to A_0\) with \(\gamma\circ\beta=\mathrm{id}_A\),
then \(D(\psi\circ\gamma\|\varphi\circ\gamma)=D(\psi\|\varphi)\). In particular, if \(E:A_0\to A\) is a conditional
expectation onto a subalgebra \(A\subset A_0\), then \(D(\psi\circ E\|\varphi\circ E)=D(\psi\|\varphi)\).*

*(f) Lower bound: \(D(\psi\|\varphi)\ge\psi(1)\log\bigl(\psi(1)/\varphi(1)\bigr)\), with the conventions of Theorem 2.3
for \(A=\mathbb C\). In particular \(D(\psi\|\varphi)\ge0\) if \(\psi(1)=\varphi(1)\).*

*(g) Scaling: for \(\lambda,\kappa>0\),
\(D(\lambda\psi\|\kappa\varphi)=\lambda D(\psi\|\varphi)+\lambda\psi(1)\log(\lambda/\kappa)\).*

*(h) \(D(\psi\|\psi)=0\) and \(D(0\|\varphi)=0\).*

*(i) Convergence: if \(\gamma_\nu:A\to A\) are unital completely positive maps with \(\|\gamma_\nu(a)-a\|\to0\) for every
\(a\), then \(D(\psi\circ\gamma_\nu\|\varphi\circ\gamma_\nu)\to D(\psi\|\varphi)\).*

**Proof.** (a) and (b): by Lemma 2.2, \(D\) is a supremum of jointly linear, positively homogeneous, weak\*
continuous functions; a supremum of such functions is jointly convex, positively homogeneous and lower semicontinuous.
Subadditivity follows from \(\sup_x(F_x(\psi_1\|\varphi_1)+F_x(\psi_2\|\varphi_2))\le D(\psi_1\|\varphi_1)
+D(\psi_2\|\varphi_2)\), and conversely subadditivity and homogeneity give convexity. That \(D>-\infty\) follows from
(f) below.

(c) \(b_x\ge0\) in Lemma 2.2, so each \(F_x(\psi\|\cdot)\) is decreasing.

(d) Let \(x\) be a path in \(A_0\). Then \(\gamma\circ x\) is a path in \(A\) (since \(\gamma(0)=0\),
\(\gamma(1)=1\)) with \(1-\gamma(x(t))=\gamma(y(t))\). The Kadison–Schwarz inequality gives
\(\gamma(y)^*\gamma(y)\le\gamma(y^*y)\), and applied to \(x^*\) (a positive map preserves adjoints) it gives
\(\gamma(x)\gamma(x)^*\le\gamma(xx^*)\). Hence, pointwise in \(t\),
\(I_{\psi\circ\gamma,\varphi\circ\gamma}(t,x(t))\le I_{\psi,\varphi}(t,\gamma(x(t)))\), so
\(F_x(\psi\circ\gamma\|\varphi\circ\gamma)\le F_{\gamma\circ x}(\psi\|\varphi)\le D(\psi\|\varphi)\). The inclusion of a
unital subalgebra is a \(*\)-homomorphism, hence a Kadison–Schwarz map.

(e) Apply (d) twice: \(D(\psi\|\varphi)=D(\psi\circ\gamma\circ\beta\|\varphi\circ\gamma\circ\beta)\le
D(\psi\circ\gamma\|\varphi\circ\gamma)\le D(\psi\|\varphi)\). For a conditional expectation take \(\beta\) the
inclusion; it is a \(*\)-homomorphism, and \(E\) is unital completely positive by (B2).

(f) Apply (d) to \(\gamma:\mathbb C\to A\), \(\lambda\mapsto\lambda1\), and use Theorem 2.3 for \(A=\mathbb C\).

(g) Fix a path \(x\) and put \(c=\kappa/\lambda\). The substitution \(t=cs\) turns \(\kappa t^{-1}\) into
\(\lambda s^{-1}\) and leaves \(dt/t\) invariant, so with the path \(\tilde x(s)=x(cs)\),
\[
F_x(\lambda\psi\|\kappa\varphi)=\lambda F_{\tilde x}(\psi\|\varphi)
+\lambda\psi(1)\int_0^\infty\Bigl(\frac1{1+cs}-\frac1{1+s}\Bigr)\frac{ds}s
=\lambda F_{\tilde x}(\psi\|\varphi)+\lambda\psi(1)\log\frac1c,
\]
where the last integral is \(\int_0^\infty\frac{1-c}{(1+s)(1+cs)}ds=-\log c\) by (2.4). Since \(x\mapsto\tilde x\) is a
bijection of paths, taking suprema gives (g).

(h) By (f), \(D(\psi\|\psi)\ge0\). For the converse we show \(I_{\psi,\psi}(t,x)\le0\) for all \(t>0\) and \(x\in A\).
Put \(m=\psi(1)\), \(y=1-x\) and \(c=\psi(xx^*)^{1/2}\). The Cauchy–Schwarz inequality for \(\psi\) gives
\(|\psi(x)|^2\le\psi(xx^*)\psi(1)\) and \(|\psi(y)|^2\le\psi(1)\psi(y^*y)\). If \(m>0\) and \(c\le\sqrt m\), then
\(\psi(y^*y)\ge|m-\psi(x)|^2/m\ge(m-c\sqrt m)^2/m=(\sqrt m-c)^2\), so
\[
\psi(y^*y)+t^{-1}\psi(xx^*)\ge(\sqrt m-c)^2+c^2/t\ge\min_{u\ge0}\bigl((\sqrt m-u)^2+u^2/t\bigr)=\frac m{1+t},
\]
the minimum being attained at \(u=\sqrt m\,t/(1+t)\); if \(c>\sqrt m\), the left side is at least \(m/t\ge m/(1+t)\).
Thus \(I_{\psi,\psi}(t,x)=t^{-1}\bigl(m(1+t)^{-1}-\psi(y^*y)-t^{-1}\psi(xx^*)\bigr)\le0\), and \(D(\psi\|\psi)\le0\).
(For \(m=0\) all terms vanish.) Finally \(F_x(0\|\varphi)=-\varphi(b_x)\le0\), and for the path equal to \(0\) on
\((0,T)\) and \(1\) afterwards \(F_x(0\|\varphi)=-\varphi(1)/T\to0\).

(i) \(\psi\circ\gamma_\nu\to\psi\) and \(\varphi\circ\gamma_\nu\to\varphi\) weak\*, because
\(|\psi(\gamma_\nu(a))-\psi(a)|\le\|\psi\|\,\|\gamma_\nu(a)-a\|\). By (b),
\(\liminf_\nu D(\psi\circ\gamma_\nu\|\varphi\circ\gamma_\nu)\ge D(\psi\|\varphi)\), and by (d) each term is at most
\(D(\psi\|\varphi)\). \(\square\)

**Corollary 2.6 (finite dimensions).** *Let \(A\) be finite-dimensional and \(\psi,\varphi,\psi_1,\dots,\psi_m\in A^*_+\).*

*(a) If \(\psi(1)=\varphi(1)\), then \(D(\psi\|\varphi)\ge0\), with equality iff \(\psi=\varphi\).*

*(b) Chain rule: if \(\psi=\sum_k\psi_k\) and \(D(\psi\|\varphi)<\infty\), then*
\[
\sum_kD(\psi_k\|\varphi)=\sum_kD(\psi_k\|\psi)+D(\psi\|\varphi),
\tag{2.5}
\]
*and all terms are finite.*

*(c) Superadditivity: \(D(\sum_k\psi_k\|\varphi)\ge\sum_kD(\psi_k\|\varphi)\).*

**Proof.** (a) Keep the notation of the proof of Theorem 2.3; if \(D=+\infty\) then the supports differ and
\(\psi\ne\varphi\). Otherwise, using \(\beta\log(\beta/\alpha)\ge\beta-\alpha\) for \(\alpha,\beta>0\), with equality
iff \(\alpha=\beta\),
\[
D(\psi\|\varphi)=\sum_{a,b:\beta_b>0}w_{ab}\beta_b\log\frac{\beta_b}{\alpha_a}\ge
\sum_{a,b:\beta_b>0}w_{ab}(\beta_b-\alpha_a)\ge\sum_{a,b}w_{ab}(\beta_b-\alpha_a)=\psi(1)-\varphi(1)=0.
\]
Equality forces \(\alpha_a=\beta_b\) whenever \(w_{ab}>0\) (for \(\beta_b>0\) from the first inequality, for
\(\beta_b=0\) from the second). Since \(p_aq_b=0\) when \(w_{ab}=0\), we get
\(\rho_\varphi=\sum_{a,b}\alpha_ap_aq_b=\sum_{a,b}\beta_bp_aq_b=\rho_\psi\).

(b) The supports satisfy \(\operatorname{supp}\rho_{\psi_k}\le\operatorname{supp}\rho_\psi\le
\operatorname{supp}\rho_\varphi\) (because \(\rho_{\psi_k}\le\rho_\psi\)), so every term is finite by (2.2), and
\(D(\psi_k\|\varphi)-D(\psi_k\|\psi)=\operatorname{Tr}\rho_{\psi_k}(\log\rho_\psi-\log\rho_\varphi)\). Summing over
\(k\) gives \(D(\psi\|\varphi)\).

(c) If \(D(\psi\|\varphi)=\infty\) there is nothing to prove. Otherwise use (2.5) and \(D(\psi_k\|\psi)\le
D(\psi_k\|\psi_k)=0\), by Proposition 2.5(c) and (h). \(\square\)

**Remark 2.7.** Proposition 2.5 contains the familiar list of properties: joint convexity, scaling, positivity,
antitonicity, monotonicity under completely positive maps, invariance under conditional expectations, and convergence
along approximations of the identity. Restriction to a subalgebra is the special case of (d) for an inclusion. Because
of (a), convexity and subadditivity in both arguments are the same property.

**Remark 2.8.** By (B7), for normal positive functionals on a von Neumann algebra \(D(\psi\|\varphi)\) is Araki's
relative entropy (with the arguments in the order written here). [Connes–Narnhofer–Thirring 1987] writes the relative entropy of
\(\psi\) with respect to \(\varphi\) as \(S(\varphi,\psi)\), with the arguments in the opposite order. Nothing below uses (B7).

## 3. Von Neumann entropy and mixtures

In this section \(A\) is finite-dimensional, \(\eta(s)=-s\log s\) and \(\eta(0)=0\).

**Definition 3.1.** For \(z\in A_+\) put \(S(z)=\operatorname{Tr}\eta(z)\), and for \(\sigma\in A^*_+\) put
\(S(\sigma)=S(\rho_\sigma)\), the *von Neumann entropy*. For a state \(\mu\) on \(C(X)\) this is the Shannon entropy
\(S(\mu)=\sum_x\eta(\mu_x)\).

**Lemma 3.2.** *Let \(\sigma,\sigma_1,\sigma_2\in A^*_+\) and \(\varphi\in\Sigma(A)\).*

*(a) \(S(\sigma)=-D(\sigma\|\operatorname{Tr})\), and \(S(\lambda\sigma)=\lambda S(\sigma)+\eta(\lambda)\sigma(1)\)
for \(\lambda\ge0\).*

*(b) Concavity: \(S(\lambda\sigma_1+(1-\lambda)\sigma_2)\ge\lambda S(\sigma_1)+(1-\lambda)S(\sigma_2)\).*

*(c) \(0\le S(\varphi)\le\log N(A)\), and \(S(\varphi)=0\) iff \(\varphi\) is pure iff \(\rho_\varphi\) is a minimal
projection.*

*(d) \(S(z)\) depends only on the nonzero eigenvalues of \(z\), counted with multiplicity in each simple summand.*

**Proof.** (a) The first formula is (2.2) with \(\rho_\varphi=1\). The second follows from
\(\eta(\lambda s)=\lambda\eta(s)+s\eta(\lambda)\).

(b) By (a) and the joint convexity of \(D\) (Proposition 2.5(a)), applied with the same second argument.

(c) Write \(\rho_\varphi=\sum_{k=1}^{N(A)}\lambda_ke_k\) as in (B1). Then \(S(\varphi)=\sum_k\eta(\lambda_k)\ge0\) since
\(\lambda_k\in[0,1]\), with equality iff one \(\lambda_k\) is \(1\), that is, iff \(\rho_\varphi\) is a minimal
projection. By (a) and Proposition 2.5(g), \(D(\varphi\|N(A)^{-1}\operatorname{Tr})=-S(\varphi)+\log N(A)\), which is
\(\ge0\) by Proposition 2.5(f). If \(\rho_\varphi=e\) is a minimal projection and \(\varphi=t\varphi_1+(1-t)\varphi_2\)
with \(0<t<1\), then \(0\le t\rho_{\varphi_1}\le e\), so \((1-e)\rho_{\varphi_1}(1-e)=0\), hence
\(\rho_{\varphi_1}^{1/2}(1-e)=0\) and \(\rho_{\varphi_1}\in eAe=\mathbb Ce\); so \(\varphi_1=\varphi\), and \(\varphi\)
is pure. If \(\rho_\varphi\) is not a minimal projection, two of the \(\lambda_k\) are nonzero and
\(\varphi=\sum_k\lambda_k\operatorname{Tr}(e_k\,\cdot)\) is a nontrivial convex combination of distinct states.

(d) \(\eta(0)=0\). \(\square\)

**Lemma 3.3 (pinching).** *Let \(Z\in M_m(A)_+\) and let \(\Delta(Z)\) be its diagonal part
\(\operatorname{diag}(Z_{11},\dots,Z_{mm})\). Then \(S(Z)\le S(\Delta(Z))\), with equality iff \(Z=\Delta(Z)\). Here
\(M_m(A)\) carries its canonical trace \(\operatorname{Tr}_m(Z)=\sum_i\operatorname{Tr}(Z_{ii})\).*

**Proof.** \(\Delta\) is the \(\operatorname{Tr}_m\)-preserving conditional expectation onto the diagonal subalgebra
\(A^m\). Let \(e=1-\operatorname{supp}\Delta(Z)\), a diagonal projection. Then \(\Delta(eZe)=e\Delta(Z)e=0\), so
\(\operatorname{Tr}_m(eZe)=0\), \(eZe=0\) and \(Ze=0\); hence \(\operatorname{supp}Z\le\operatorname{supp}\Delta(Z)\)
and \(D(Z\|\Delta(Z))\), the relative entropy of the functionals with these densities, is finite. The element
\(\log\Delta(Z)\) (on the support) is diagonal, and \(\operatorname{Tr}_m(Zb)=\operatorname{Tr}_m(\Delta(Z)b)\) for
diagonal \(b\), so by (2.2)
\[
D(Z\|\Delta(Z))=\operatorname{Tr}_m(Z\log Z)-\operatorname{Tr}_m(\Delta(Z)\log\Delta(Z))=S(\Delta(Z))-S(Z).
\]
Both functionals have total mass \(\operatorname{Tr}_mZ\); Corollary 2.6(a) finishes the proof. \(\square\)

**Theorem 3.4 (entropy of a mixture).** *Let \(\sigma_1,\dots,\sigma_m\in A^*_+\) and \(\sigma=\sum_x\sigma_x\). Then*
\[
0\le\sum_xS(\sigma_x)-S(\sigma)=-\sum_xD(\sigma_x\|\sigma),
\tag{3.1}
\]
*and equality \(S(\sigma)=\sum_xS(\sigma_x)\) holds iff \(\rho_{\sigma_x}\rho_{\sigma_y}=0\) for all \(x\ne y\).*

**Proof.** The identity: \(\operatorname{supp}\rho_{\sigma_x}\le\operatorname{supp}\rho_\sigma\), so by (2.2)
\(D(\sigma_x\|\sigma)=-S(\sigma_x)-\operatorname{Tr}(\rho_{\sigma_x}\log\rho_\sigma)\), and summing,
\(\sum_x\operatorname{Tr}(\rho_{\sigma_x}\log\rho_\sigma)=-S(\sigma)\).

The inequality: let \(r_x=\rho_{\sigma_x}^{1/2}\) and let \(V\in M_{m,1}(A)\) be the column \((r_1,\dots,r_m)^T\). Then
\(V^*V=\sum_x\rho_{\sigma_x}=\rho_\sigma\in A\) and \(VV^*=[r_xr_y]_{x,y}\in M_m(A)\). In each simple summand
\(M_n(\mathbb C)\) of \(A\) the corresponding blocks of \(V^*V\) and \(VV^*\) are \(W^*W\) and \(WW^*\) for a matrix
\(W\) of size \(mn\times n\), which have the same nonzero eigenvalues with multiplicity. By Lemma 3.2(d),
\(S(\sigma)=S(V^*V)=S(VV^*)\), and by Lemma 3.3, \(S(VV^*)\le S(\Delta(VV^*))=S(\operatorname{diag}(\rho_{\sigma_x}))
=\sum_xS(\sigma_x)\). Equality holds iff \(VV^*\) is diagonal, that is, \(r_xr_y=0\) for \(x\ne y\). This is equivalent to
\(\rho_{\sigma_x}\rho_{\sigma_y}=0\): one direction is \(\rho_{\sigma_x}\rho_{\sigma_y}=r_x(r_xr_y)r_y\); for the
other, \(\rho_{\sigma_x}\rho_{\sigma_y}=0\) implies that \(\rho_{\sigma_x}\) and \(\rho_{\sigma_y}\) commute and
\(p(\rho_{\sigma_x})\rho_{\sigma_y}=0\) for polynomials \(p\) with \(p(0)=0\), hence \(f(\rho_{\sigma_x})
\rho_{\sigma_y}=0\) for continuous \(f\) with \(f(0)=0\); taking \(f=\sqrt\cdot\) twice gives \(r_xr_y=0\). \(\square\)

In normalized form, with \(\sigma_x=\mu_x\varphi_x\) for states \(\varphi_x\) and a probability vector \(\mu\), (3.1)
and Lemma 3.2 give the two-sided estimate
\[
\sum_x\mu_xS(\varphi_x)\le S\Bigl(\sum_x\mu_x\varphi_x\Bigr)\le\sum_x\mu_xS(\varphi_x)+S(\mu).
\tag{3.2}
\]

## 4. The entropy defect of a map into an abelian algebra

A reference for this section is [Connes–Narnhofer–Thirring 1987]. Fix a unital C\*-algebra \(A\), a finite set \(X\),
a unital positive map \(P:A\to C(X)\) with coordinate states \(P_x\) (Lemma 1.1), and a state \(\mu\) on \(C(X)\). The
state \(P^*\mu:=\mu\circ P=\sum_x\mu_xP_x\) is a convex combination of the \(P_x\). Conversely every decomposition
\(\varphi=\sum_x\mu_x\varphi_x\) of a state into states arises from the map with \(P_x=\varphi_x\). One should think of
\(x\) as the outcome of a measurement performed on the system in the state \(\varphi=\mu\circ P\): the outcome \(x\)
occurs with probability \(\mu_x\) and leaves the "conditional state" \(P_x\).

**Definition 4.1.** The *Holevo quantity* of \((P,\mu)\) is
\[
\varepsilon_\mu(P)=\sum_{x:\mu_x>0}\mu_x\,D(P_x\|\mu\circ P),
\]
and the *entropy defect* of \(P\) with respect to \(\mu\) is \(s_\mu(P)=S(\mu)-\varepsilon_\mu(P)\).

**Lemma 4.2.** *\(0\le\varepsilon_\mu(P)\le S(\mu)\), so \(0\le s_\mu(P)\le S(\mu)\). Moreover*
\[
s_\mu(P)=-\sum_{x\in X}D(\mu_xP_x\,\|\,\mu\circ P).
\tag{4.1}
\]

**Proof.** Put \(\varphi=\mu\circ P\). For \(\mu_x>0\), \(D(P_x\|\varphi)\ge0\) by Proposition 2.5(f). Since
\(\varphi\ge\mu_xP_x\), Proposition 2.5(c), (g), (h) give \(D(P_x\|\varphi)\le D(P_x\|\mu_xP_x)=-\log\mu_x\). Multiplying
by \(\mu_x\) and summing gives \(\varepsilon_\mu(P)\le S(\mu)\). By Proposition 2.5(g),
\(D(\mu_xP_x\|\varphi)=\mu_xD(P_x\|\varphi)+\mu_x\log\mu_x\) for \(\mu_x>0\), and \(D(0\|\varphi)=0\); summing gives
(4.1). \(\square\)

So \(\varepsilon_\mu(P)\) is always finite, and it measures how far the conditional states are, on average, from their
barycentre. The defect \(s_\mu(P)\) measures by how much the Shannon entropy \(S(\mu)\) of the outcome overestimates
this.

**Example 4.3 (a useless measurement).** If \(P_x=\varphi\) for all \(x\), then \(\varepsilon_\mu(P)=0\) and
\(s_\mu(P)=S(\mu)\), which can be as large as \(\log|X|\) although nothing is learned about \(A\). A model whose Shannon
entropy is to count as information about \(A\) must therefore pay its defect.

**Proposition 4.4 (general \(A\)).** *(a) Convexity in \(P\): for unital positive \(P',P'':A\to C(X)\) and
\(0\le\lambda\le1\),
\(\varepsilon_\mu(\lambda P'+(1-\lambda)P'')\le\lambda\varepsilon_\mu(P')+(1-\lambda)\varepsilon_\mu(P'')\); hence
\(s_\mu\) is concave in \(P\).*

*(b) Monotonicity: for a unital completely positive \(\gamma:A_0\to A\), \(\varepsilon_\mu(P\circ\gamma)\le
\varepsilon_\mu(P)\) and \(s_\mu(P\circ\gamma)\ge s_\mu(P)\). Equality holds if \(\gamma\) has a unital completely
positive right inverse \(\beta:A\to A_0\), \(\gamma\circ\beta=\mathrm{id}_A\); in particular if \(\gamma\) is a conditional
expectation of \(A_0\) onto a subalgebra \(A\).*

**Proof.** (a) Put \(P=\lambda P'+(1-\lambda)P''\). Then \(P_x=\lambda P'_x+(1-\lambda)P''_x\) and
\(\mu\circ P=\lambda\mu\circ P'+(1-\lambda)\mu\circ P''\); joint convexity (Proposition 2.5(a)) gives
\(D(P_x\|\mu\circ P)\le\lambda D(P'_x\|\mu\circ P')+(1-\lambda)D(P''_x\|\mu\circ P'')\). Multiply by \(\mu_x\) and sum.

(b) \((P\circ\gamma)_x=P_x\circ\gamma\) and \(\mu\circ P\circ\gamma=(\mu\circ P)\circ\gamma\); apply Proposition
2.5(d) termwise. For the equality, \(\varepsilon_\mu(P)=\varepsilon_\mu(P\circ\gamma\circ\beta)\le
\varepsilon_\mu(P\circ\gamma)\). \(\square\)

**Theorem 4.5 (finite-dimensional \(A\)).** *Let \(A\) be finite-dimensional, \(P:A\to C(X)\) unital positive, \(\mu\) a
state on \(C(X)\) and \(\varphi=\mu\circ P\).*

*(a) (Holevo's bound.) \(\varepsilon_\mu(P)=S(\varphi)-\sum_x\mu_xS(P_x)\). Hence \(\varepsilon_\mu(P)\le S(\varphi)\),
with equality iff \(P_x\) is pure for every \(x\) with \(\mu_x>0\).*

*(b) \(s_\mu(P)=\sum_xS(\mu_xP_x)-S(\varphi)\), and \(s_\mu(P)=0\) iff the densities of the functionals \(\mu_xP_x\) are
pairwise orthogonal.*

*(c) \(S(\varphi)=\max\{\varepsilon_\nu(Q)\}\), the maximum over all finite sets \(Y\), unital positive
\(Q:A\to C(Y)\) and states \(\nu\) on \(C(Y)\) with \(\nu\circ Q=\varphi\).*

*(d) For \(P\) extreme among the unital positive maps \(A\to C(X)\), \(s_\mu(P)=S(\mu)-S(\mu\circ P)\).*

*(e) Concavity in \(\mu\): if \(\mu=\sum_i\lambda_i\mu_i\) is a convex combination of states on \(C(X)\), then
\(\varepsilon_\mu(P)=\sum_i\lambda_i\varepsilon_{\mu_i}(P)+\bigl(S(\mu\circ P)-\sum_i\lambda_iS(\mu_i\circ P)\bigr)
\ge\sum_i\lambda_i\varepsilon_{\mu_i}(P)\).*

**Proof.** (a) Apply (3.1) to \(\sigma_x=\mu_xP_x\): by (4.1), \(s_\mu(P)=\sum_xS(\mu_xP_x)-S(\varphi)\), and
\(S(\mu_xP_x)=\mu_xS(P_x)+\eta(\mu_x)\) by Lemma 3.2(a). So \(\varepsilon_\mu(P)=S(\mu)-s_\mu(P)=S(\varphi)-
\sum_x\mu_xS(P_x)\). Since \(S(P_x)\ge0\) with equality iff \(P_x\) is pure (Lemma 3.2(c)), the rest follows.

(b) The formula was obtained in (a); the equality case is Theorem 3.4.

(c) By (a), \(\varepsilon_\nu(Q)\le S(\varphi)\). Conversely write \(\rho_\varphi=\sum_k\lambda_ke_k\) as in (B1),
\(Y=\{k\}\), \(\nu_k=\lambda_k\), \(Q_k=\operatorname{Tr}(e_k\,\cdot)\): the \(Q_k\) are pure and \(\nu\circ Q=\varphi\), so
\(\varepsilon_\nu(Q)=S(\varphi)\).

(d) By Lemma 1.1(b) all \(P_x\) are pure, so (a) gives \(\varepsilon_\mu(P)=S(\mu\circ P)\).

(e) The term \(\sum_x\mu_xS(P_x)\) in (a) is linear in \(\mu\); the remaining term is \(S(\mu\circ P)\), and
\(S(\mu\circ P)-\sum_i\lambda_iS(\mu_i\circ P)\ge0\) by concavity (Lemma 3.2(b)). \(\square\)

**Example 4.6 (zero defect).** Let \(A\) be finite-dimensional, \(\varphi\) a state, and
\(A_\varphi=\{a:\varphi(ab)=\varphi(ba)\ \forall b\}\) its centralizer. Since
\(\varphi(ab)-\varphi(ba)=\operatorname{Tr}((\rho_\varphi a-a\rho_\varphi)b)\), \(A_\varphi\) is the relative commutant of
\(\rho_\varphi\) in \(A\): a direct sum of full matrix algebras over the eigenspaces of \(\rho_\varphi\) in each simple
summand. Choose a maximal abelian subalgebra \(B\) of \(A_\varphi\). Its minimal projections \(e_1,\dots,e_N\) are
minimal projections of \(A_\varphi\), hence of \(A\), and \(\rho_\varphi\in B\) because \(\rho_\varphi\) commutes with
\(A_\varphi\supset B\) and \(B\) is maximal abelian in \(A_\varphi\). So \(\rho_\varphi=\sum_i\lambda_ie_i\). The map
\(E(a)=\sum_i\operatorname{Tr}(e_ia)e_i\) is a conditional expectation of \(A\) onto \(B\cong C(\{1,\dots,N\})\) (note
\(e_iae_i=\operatorname{Tr}(e_ia)e_i\)), with \(\varphi\circ E=\sum_i\lambda_i\operatorname{Tr}(e_i\,\cdot)=\varphi\).
With \(\mu=\varphi|_B\), the coordinate states \(E_i=\operatorname{Tr}(e_i\,\cdot)\) are pure with orthogonal
densities, so \(s_\mu(E)=0\) by Theorem 4.5(b), and \(\varepsilon_\mu(E)=S(\mu)=S(\varphi)\). This is the prototype of a
map with zero entropy defect: an optimal measurement that commutes with the state.

For the next result we need the defect of a coarse-grained map. Let \(Q:A\to C(X)\) be unital positive, \(\mu\) a state
on \(C(X)\) and \(C\subset C(X)\) a unital subalgebra with partition \(\pi\). Identify \(C\) with \(C(\pi)\). The map
\(E^\mu_C\circ Q:A\to C\) has coordinates \(\sum_{x\in K}\mu_xQ_x/\mu(K)\) for \(\mu(K)>0\), and
\((\mu|_C)\circ E^\mu_C\circ Q=\mu\circ Q\). So (4.1), applied in \(C\), gives
\[
s_{\mu|_C}\bigl(E^\mu_C\circ Q\bigr)=-\sum_{K\in\pi}D\Bigl(\sum_{x\in K}\mu_xQ_x\,\Big\|\,\mu\circ Q\Bigr).
\tag{4.2}
\]
Here, and always below, the defect of a map into \(C\) is computed with the state \(\mu|_C\), that is, with the Shannon
entropy \(S(\mu|_C)\) of the coarse outcome.

**Theorem 4.7 (defect of a join).** *Let \(A\) be finite-dimensional and let \((\sigma_{kl})_{k\in K,l\in L}\) be a
finite family in \(A^*_+\) with sum \(\sigma\), row sums \(\sigma^1_k=\sum_l\sigma_{kl}\) and column sums
\(\sigma^2_l=\sum_k\sigma_{kl}\). Then*
\[
-\sum_{k,l}D(\sigma_{kl}\|\sigma)\le-\sum_kD(\sigma^1_k\|\sigma)-\sum_lD(\sigma^2_l\|\sigma).
\]

**Proof.** All relative entropies here are finite, since each functional is dominated by \(\sigma\). For fixed \(l\),
the chain rule (2.5) with \(\psi=\sigma^2_l\) and \(\varphi=\sigma\) gives
\(\sum_kD(\sigma_{kl}\|\sigma)=\sum_kD(\sigma_{kl}\|\sigma^2_l)+D(\sigma^2_l\|\sigma)\). Summing over \(l\) and using
the subadditivity of \(D\) (Proposition 2.5(a)) for each fixed \(k\),
\[
\sum_{k,l}D(\sigma_{kl}\|\sigma)-\sum_lD(\sigma^2_l\|\sigma)=\sum_k\sum_lD(\sigma_{kl}\|\sigma^2_l)\ge
\sum_kD\Bigl(\sum_l\sigma_{kl}\Big\|\sum_l\sigma^2_l\Bigr)=\sum_kD(\sigma^1_k\|\sigma).\qquad\square
\]

**Theorem 4.8 (subadditivity of the defect).** *Let \(A\) be finite-dimensional, \(Q:A\to C(X)\) unital positive,
\(\mu\) a state on \(C(X)\), and \(B_1,B_2\subset C(X)\) unital subalgebras. Write \(Q_C=E^\mu_C\circ Q\). Then*
\[
s_{\mu|_{B_1\vee B_2}}\bigl(Q_{B_1\vee B_2}\bigr)\le s_{\mu|_{B_1}}\bigl(Q_{B_1}\bigr)+s_{\mu|_{B_2}}\bigl(Q_{B_2}\bigr).
\]

**Proof.** Let \(\pi_1,\pi_2\) be the partitions and put \(\sigma_{KL}=\sum_{x\in K\cap L}\mu_xQ_x\) for
\(K\in\pi_1\), \(L\in\pi_2\) (zero if \(K\cap L=\emptyset\)). By Lemma 1.2 the blocks of \(B_1\vee B_2\) are the
nonempty \(K\cap L\), and \(D(0\|\cdot)=0\). So by (4.2) the three defects are the three sums of Theorem 4.7 with
\(\sigma=\mu\circ Q\). \(\square\)

## 5. Completely positive maps from matrix algebras, and nuclear algebras

The observations of Section 6 are unital completely positive maps into \(A\) whose domains are finite-dimensional
C\*-algebras. This section shows that there are plenty of them and that matrix algebras suffice.

**Lemma 5.1 (Choi's correspondence).** *Let \(e_{ij}\) be the matrix units of \(M_n(\mathbb C)\). A map
\(\theta:M_n(\mathbb C)\to A\) is completely positive iff \([\theta(e_{ij})]_{i,j}\in M_n(A)\) is positive, and it is
unital iff \(\sum_i\theta(e_{ii})=1\). Thus unital completely positive maps \(M_n(\mathbb C)\to A\) correspond
bijectively to the positive \(X\in M_n(A)\) with \(\sum_iX_{ii}=1\).*

**Proof.** The matrix \(\mathbf E=[e_{ij}]\in M_n(M_n(\mathbb C))\) satisfies \(\mathbf E^*=\mathbf E\) and
\(\mathbf E^2=n\mathbf E\), so \(\mathbf E\ge0\), and \([\theta(e_{ij})]=\theta^{(n)}(\mathbf E)\ge0\) if \(\theta\)
is completely positive. Conversely let \(X=[x_{ij}]\ge0\), write \(X=V^*V\) with \(V=X^{1/2}\in M_n(A)\), and let
\(w_k\in M_{n,1}(A)\) be the column with entries \(v_{k1},\dots,v_{kn}\). Define \(\theta(b)=\sum_{i,j}b_{ij}x_{ij}\). Since
\(x_{ij}=\sum_kv_{ki}^*v_{kj}\), we get \(\theta(b)=\sum_kw_k^*(b\otimes1_A)w_k\), where \(b\mapsto b\otimes1_A=
[b_{ij}1_A]\in M_n(A)\) is a \(*\)-homomorphism. So \(\theta\) is completely positive by (B2), and
\(\theta(e_{ij})=x_{ij}\). A linear map on \(M_n(\mathbb C)\) is determined by its values on the \(e_{ij}\), and
\(\theta(1)=\sum_i\theta(e_{ii})\). \(\square\)

**Proposition 5.2 (unital approximations).** *Let \(A\) be a unital nuclear C\*-algebra.*

*(a) For every finite set \(F\subset A\) and \(\delta>0\) there are \(n\) and unital completely positive maps
\(\sigma:A\to M_n(\mathbb C)\), \(\tau:M_n(\mathbb C)\to A\) with \(\|\tau\sigma(a)-a\|\le\delta\) for \(a\in F\).*

*(b) If \(A\) is separable, there is a sequence \(\theta_\nu=\tau_\nu\circ\sigma_\nu\) of unital completely positive
maps \(A\to A\), each factoring through a matrix algebra by unital completely positive maps as in (a), with
\(\|\theta_\nu(a)-a\|\to0\) for every \(a\in A\).*

*(c) Conversely, if such a sequence exists (with finite-dimensional intermediate algebras), then \(A\) is separable.*

**Proof.** (a) Let \(0<\delta'<1\). By (B5) there are completely positive contractions \(\sigma_0:A\to M_n\) and
\(\tau_0:M_n\to A\) with \(\|\tau_0\sigma_0(a)-a\|\le\delta'\) for \(a\in F\cup\{1\}\). Put \(h=\sigma_0(1)\), so
\(0\le h\le1\), fix a state \(\omega\) on \(A\), and let \(\sigma(a)=\sigma_0(a)+\omega(a)(1-h)\). This is completely
positive (a sum of completely positive maps; \(a\mapsto\omega(a)(1-h)\) is completely positive because \(\omega\) is and
\(1-h\ge0\)) and unital. Let \(k=\tau_0(1)\). Then \(\tau_0(h)\le k\le1\), and \(\|1-\tau_0(h)\|\le\delta'\) gives
\(\tau_0(h)\ge1-\delta'\); so \(k\ge1-\delta'\) is invertible and
\(\|\tau_0(1-h)\|=\|k-\tau_0(h)\|\le\|1-\tau_0(h)\|\le\delta'\), because \(0\le k-\tau_0(h)\le1-\tau_0(h)\). Put
\(\tau(b)=k^{-1/2}\tau_0(b)k^{-1/2}\), a unital completely positive map. For \(a\in F\), with \(z=\tau_0\sigma(a)\) and
\(\|z\|\le\|a\|\),
\[
\|\tau\sigma(a)-a\|\le\|k^{-1/2}zk^{-1/2}-z\|+|\omega(a)|\,\|\tau_0(1-h)\|+\|\tau_0\sigma_0(a)-a\|
\le\|a\|\Bigl(\frac1{1-\delta'}-1\Bigr)+\|a\|\delta'+\delta',
\]
using \(\|k^{-1/2}zk^{-1/2}-z\|\le\|k^{-1/2}-1\|(\|k^{-1/2}\|+1)\|z\|\le((1-\delta')^{-1/2}-1)((1-\delta')^{-1/2}+1)\|z\|\).
Choose \(\delta'\) small.

(b) Let \((a_k)\) be dense in \(A\) and choose \(\sigma_\nu,\tau_\nu\) by (a) for \(F=\{a_1,\dots,a_\nu\}\) and
\(\delta=1/\nu\). Given \(a\) and \(\theta>0\), pick \(a_k\) with \(\|a-a_k\|<\theta\). Since \(\|\theta_\nu\|=1\), for
\(\nu\ge k\): \(\|\theta_\nu(a)-a\|\le2\theta+1/\nu\).

(c) Each \(\theta_\nu\) has finite-dimensional range, and every \(a\) is a limit of elements of the union of these
ranges, whose closure is separable. \(\square\)

**Remark 5.3.** For nonseparable nuclear algebras, such as the abelian algebra \(\ell^\infty(\mathbb N)\), part (c)
shows that no *sequence* can do this; nets must be used. Part (a) provides one: index the maps \(\tau\sigma\) of (a) by
the pairs \((F,\delta)\), ordered by \((F,\delta)\le(F',\delta')\) iff \(F\subset F'\) and \(\delta'\le\delta\); the
resulting net \(\theta_{F,\delta}\) of unital completely positive maps, each factoring through a matrix algebra,
satisfies \(\|\theta_{F,\delta}(a)-a\|\to0\) for every \(a\in A\). *Reference:* [Connes–Narnhofer–Thirring 1987] states the
existence of a sequence for every nuclear unital C\*-algebra; this fails for \(\ell^\infty(\mathbb N)\), so we prove it
for separable algebras and use nets otherwise.

**Lemma 5.4.** *Every finite-dimensional C\*-algebra \(A_0\) is a unital subalgebra of some \(M_N(\mathbb C)\) onto
which there is a conditional expectation \(E:M_N(\mathbb C)\to A_0\).*

**Proof.** Write \(A_0=\bigoplus_{k=1}^rM_{n_k}\) embedded block-diagonally in \(M_N\), \(N=\sum n_k\), and let \(f_k\) be
the block projections. \(E(m)=\sum_kf_kmf_k\) is unital and completely positive, maps into \(A_0\), is the identity on
\(A_0\), and \(E(ama')=aE(m)a'\) for \(a,a'\in A_0\) because \(a,a'\) commute with the \(f_k\). \(\square\)

## 6. Abelian models and the function \(H_\varphi\)

A reference for this section is [Connes–Narnhofer–Thirring 1987]. Fix a state \(\varphi\) of a unital C\*-algebra \(A\),
finite-dimensional C\*-algebras \(A_1,\dots,A_n\) and unital completely positive maps \(\gamma_j:A_j\to A\).

**Definition 6.1.** An *abelian model* for \((A,\varphi,n)\) consists of

1. a finite-dimensional abelian C\*-algebra \(B=C(X)\) with a state \(\mu\), and unital \(*\)-subalgebras
   \(B_1,\dots,B_n\subset B\);
2. a unital completely positive map \(P:A\to B\) with \(\mu\circ P=\varphi\).

With \(E_j=E^\mu_{B_j}\), the maps \(\rho_j=E_j\circ P\circ\gamma_j:A_j\to B_j\) are unital completely positive, and
\(\mu\circ\rho_j=\varphi\circ\gamma_j\). The *entropy of the model* for \((\gamma_1,\dots,\gamma_n)\) is
\[
\mathcal E\bigl(B,\mu,(B_j),P;(\gamma_j)\bigr)=S\bigl(\mu|_{B_1\vee\dots\vee B_n}\bigr)-\sum_{j=1}^ns_{\mu|_{B_j}}(\rho_j).
\tag{6.1}
\]
Note that a model does not depend on the \(\gamma_j\); only its entropy does.

**Definition 6.2.** \(H_\varphi(\gamma_1,\dots,\gamma_n)\) is the supremum of the entropies of all abelian models for
\((A,\varphi,n)\). When the \(\gamma_j\) are inclusions of finite-dimensional subalgebras \(N_j\subset A\) we write
\(H_\varphi(N_1,\dots,N_n)\).

The first term of (6.1) is the Shannon entropy of the joint outcome of the \(n\) coarse measurements; each defect
subtracts what the \(j\)-th coarse measurement fails to tell about the observation \(\gamma_j\).

**Proposition 6.3.** *For every abelian model,*
\[
\mathcal E=\Bigl(S(\mu|_{\vee_jB_j})-\sum_jS(\mu|_{B_j})\Bigr)+\sum_j\Bigl(S(\varphi\circ\gamma_j)-
\sum_{K\in\pi(B_j),\,\mu(K)>0}\mu(K)\,S\bigl((\rho_j)_K\bigr)\Bigr)\le\sum_{j=1}^nS(\varphi\circ\gamma_j).
\]
*Consequently \(0\le H_\varphi(\gamma_1,\dots,\gamma_n)\le\sum_jS(\varphi\circ\gamma_j)<\infty\).*

**Proof.** By definition \(s_{\mu|_{B_j}}(\rho_j)=S(\mu|_{B_j})-\varepsilon_{\mu|_{B_j}}(\rho_j)\), and Theorem 4.5(a),
applied to \(\rho_j:A_j\to B_j\) with \(\mu|_{B_j}\circ\rho_j=\varphi\circ\gamma_j\), evaluates \(\varepsilon\). The first
bracket is \(\le0\) by the subadditivity of Shannon entropy (B4) (the join \(\vee_jB_j\) is generated by the
\(B_j\)), and \(S((\rho_j)_K)\ge0\). The model \(B=\mathbb C\) has entropy \(0\), because every defect of a map into
\(\mathbb C\) vanishes (Lemma 4.2 with \(S(\mu)=0\)). \(\square\)

The next result describes \(H_\varphi\) through decompositions of \(\varphi\), which is how it is used in practice. A
*decomposition of \(\varphi\) of shape \((I_1,\dots,I_n)\)*, for finite sets \(I_j\), is a family
\((\psi_i)_{i\in I}\) of positive functionals indexed by \(I=I_1\times\dots\times I_n\) with \(\sum_i\psi_i=\varphi\). Its
*marginals* are \(\psi^{(j)}_k=\sum_{i:i_j=k}\psi_i\) for \(k\in I_j\). Its *entropy* relative to
\((\gamma_1,\dots,\gamma_n)\) is
\[
\mathcal E_\gamma(\psi)=\sum_{i\in I}\eta\bigl(\psi_i(1)\bigr)+\sum_{j=1}^n\sum_{k\in I_j}
D\bigl(\psi^{(j)}_k\circ\gamma_j\,\big\|\,\varphi\circ\gamma_j\bigr).
\tag{6.2}
\]
The relative entropies in (6.2) are \(\le0\), because \(\psi^{(j)}_k\circ\gamma_j\le\varphi\circ\gamma_j\).

**Proposition 6.4 (decompositions).** *\(H_\varphi(\gamma_1,\dots,\gamma_n)=\sup\mathcal E_\gamma(\psi)\), the supremum over
all decompositions of \(\varphi\) of all shapes. More precisely, every abelian model has the same entropy as some
decomposition, and conversely.*

**Proof.** Let \((C(X),\mu,(B_j),P)\) be a model with partitions \(\pi_j=\pi(B_j)\). Take \(I_j=\pi_j\) and
\(\psi_i=\sum_{x\in K_1\cap\dots\cap K_n}\mu_xP_x\) for \(i=(K_1,\dots,K_n)\). Then \(\sum_i\psi_i=\mu\circ P=\varphi\), and
\(\psi^{(j)}_K=\sum_{x\in K}\mu_xP_x\). The atoms of \(\vee_jB_j\) are the nonempty intersections
\(K_1\cap\dots\cap K_n\) (Lemma 1.2), of \(\mu\)-measure \(\psi_i(1)\), so \(S(\mu|_{\vee B_j})=\sum_i\eta(\psi_i(1))\).
Applying (4.2) to \(Q=P\circ\gamma_j:A_j\to C(X)\) gives
\(s_{\mu|_{B_j}}(\rho_j)=-\sum_{K\in\pi_j}D(\psi^{(j)}_K\circ\gamma_j\|\varphi\circ\gamma_j)\). So the entropy of the
model is \(\mathcal E_\gamma(\psi)\).

Conversely, given a decomposition of shape \((I_j)\), let \(X=I\), \(\mu_i=\psi_i(1)\), \(P_i=\psi_i/\psi_i(1)\) if
\(\psi_i\ne0\) and \(P_i=\varphi\) otherwise, and let \(B_j\) be the functions on \(I\) depending only on the \(j\)-th
coordinate. Then \(\mu_iP_i=\psi_i\), so \(\mu\circ P=\varphi\), and by the first part (whose construction returns the same
family, since the blocks of \(B_j\) are indexed by \(I_j\)) the entropy of this model is \(\mathcal E_\gamma(\psi)\).
\(\square\)

**Corollary 6.5 (other forms).** *Write \(\hat\sigma=\sigma/\sigma(1)\) for \(\sigma\ne0\) and
\(p^{(j)}_k=\psi^{(j)}_k(1)\). For a decomposition \(\psi\) of \(\varphi\),*
\[
\begin{aligned}
\mathcal E_\gamma(\psi)&=\sum_i\eta(\psi_i(1))-\sum_j\sum_k\eta(p^{(j)}_k)+\sum_j\sum_kp^{(j)}_k\,
D\bigl(\hat\psi^{(j)}_k\circ\gamma_j\,\|\,\varphi\circ\gamma_j\bigr)\\
&=\sum_i\eta(\psi_i(1))-\sum_j\sum_k\eta(p^{(j)}_k)+\sum_j\Bigl(S(\varphi\circ\gamma_j)-\sum_kp^{(j)}_k\,
S\bigl(\hat\psi^{(j)}_k\circ\gamma_j\bigr)\Bigr),
\end{aligned}
\]
*(sums over \(k\) with \(p^{(j)}_k>0\)). Moreover decompositions of \(\varphi\) of shape \((I_j)\) correspond bijectively,
via \(\psi_i=\langle\xi_\varphi,t_i\pi_\varphi(\cdot)\xi_\varphi\rangle\), to families \((t_i)_{i\in I}\) of positive
elements of \(\pi_\varphi(A)'\) with \(\sum_it_i=1\). So*
\[
H_\varphi(\gamma_1,\dots,\gamma_n)=\sup_{(t_i)}\Bigl[\sum_i\eta\bigl(\langle\xi_\varphi,t_i\xi_\varphi\rangle\bigr)
+\sum_j\sum_{k\in I_j}D\bigl(\langle\xi_\varphi,t^{(j)}_k\pi_\varphi(\gamma_j(\cdot))\xi_\varphi\rangle\,\big\|\,
\varphi\circ\gamma_j\bigr)\Bigr],\qquad t^{(j)}_k=\sum_{i:i_j=k}t_i.
\]

**Proof.** The first line is Proposition 2.5(g), \(D(p\hat\sigma\|\varphi)=pD(\hat\sigma\|\varphi)-\eta(p)\). The second
uses (2.2) as in the proof of Theorem 3.4: \(\sum_kp^{(j)}_kD(\hat\psi^{(j)}_k\circ\gamma_j\|\varphi\circ\gamma_j)=
S(\varphi\circ\gamma_j)-\sum_kp^{(j)}_kS(\hat\psi^{(j)}_k\circ\gamma_j)\), both sides being finite. The last statement
is (B3): each \(\psi_i\le\varphi\) has a unique \(t_i\), and \(\sum_it_i\) represents \(\varphi\), so it equals \(1\).
\(\square\)

**Proposition 6.6 (the abelian case).** *Let \(A\) be abelian and let \(N_1,\dots,N_n\) be finite-dimensional unital
subalgebras, with \(\gamma_j\) the inclusions. Then \(H_\varphi(N_1,\dots,N_n)=S(\varphi|_{N_1\vee\dots\vee N_n})\).*

**Proof.** The minimal projections of \(N_j\) form a partition of unity \(\alpha_j\) in \(A\); the join
\(N=N_1\vee\dots\vee N_n\) is finite-dimensional, with minimal projections the nonzero products
\(c=a_1\cdots a_n\), \(a_j\in\alpha_j\). Let \(\psi\) be a decomposition of \(\varphi\) of shape \((I_j)\). The numbers
\(p(i,c)=\psi_i(c)\), for \(i\in I\) and \(c\) a minimal projection of \(N\), form a probability distribution. On this
finite probability space let \(\xi_j(i,c)=i_j\), \(\zeta_j(i,c)=\) the element of \(\alpha_j\) above \(c\), and
\(\zeta=(\zeta_1,\dots,\zeta_n)\), which determines \(c\). For the abelian algebra \(N_j\), (2.2) is a classical sum, and
\[
\sum_kD\bigl(\psi^{(j)}_k|_{N_j}\,\|\,\varphi|_{N_j}\bigr)=\sum_{k,a}p(\xi_j=k,\zeta_j=a)
\log\frac{p(\xi_j=k,\zeta_j=a)}{p(\zeta_j=a)}=-H(\xi_j\mid\zeta_j).
\]
With \(\xi=(\xi_1,\dots,\xi_n)\) we get \(\mathcal E_\gamma(\psi)=H(\xi)-\sum_jH(\xi_j\mid\zeta_j)\). By (B4),
\[
H(\xi)\le H(\xi,\zeta)=H(\zeta)+H(\xi\mid\zeta)\le H(\zeta)+\sum_jH(\xi_j\mid\zeta)\le H(\zeta)+\sum_jH(\xi_j\mid\zeta_j),
\]
so \(\mathcal E_\gamma(\psi)\le H(\zeta)=S(\varphi|_N)\), and \(H_\varphi\le S(\varphi|_N)\) by Proposition 6.4. For
the converse take \(I_j=\alpha_j\) and \(\psi_{(a_1,\dots,a_n)}=\varphi(a_1\cdots a_n\,\cdot)\), a positive functional
because \(a_1\cdots a_n\) is a central projection. Then \(\xi_j=\zeta_j\) almost surely, so
\(\mathcal E_\gamma(\psi)=H(\zeta)\). \(\square\)

So for abelian algebras \(H_\varphi\) is the classical entropy of the joined partition, and the entropy defects of
the optimal model vanish.

## 7. Properties of \(H_\varphi\)

Throughout, \(\varphi\) is a state, and \(\gamma_j:A_j\to A\) are unital completely positive maps whose domains \(A_j\)
are finite-dimensional C\*-algebras.

**Theorem 7.1.** *(a) Monotonicity in the observations: if the \(A'_j\) are finite-dimensional C\*-algebras and
\(\theta_j:A'_j\to A_j\) are unital completely positive maps, then \(H_\varphi(\gamma_1\circ\theta_1,\dots,\gamma_n\circ\theta_n)\le
H_\varphi(\gamma_1,\dots,\gamma_n)\). Equality holds if each \(\theta_j\) has a unital completely positive right inverse;
in particular if each \(\theta_j\) is a conditional expectation of \(A'_j\) onto the subalgebra \(A_j\).*

*(b) Invariance: if \(\theta:A\to A\) is unital positive with \(\varphi\circ\theta=\varphi\), then
\(H_\varphi(\theta\circ\gamma_1,\dots,\theta\circ\gamma_n)\le H_\varphi(\gamma_1,\dots,\gamma_n)\), with equality if
\(\theta\) is a \(\varphi\)-preserving automorphism. (If \(\theta\) is not completely positive, the maps
\(\theta\circ\gamma_j\) are only unital positive; Definitions 6.1 and 6.2 and Proposition 6.4 apply to them verbatim,
since they use only that the maps \(\rho_j\) into abelian algebras are unital positive.)*

*(c) \(H_\varphi(\gamma_1,\dots,\gamma_n)\) depends only on the set \(\{\gamma_1,\dots,\gamma_n\}\): it is symmetric, and
\(H_\varphi(\gamma_1,\dots,\gamma_n,\gamma_n)=H_\varphi(\gamma_1,\dots,\gamma_n)\).*

*(d) For finite sets \(\mathsf X,\mathsf Y\) of such maps,
\(\max\{H_\varphi(\mathsf X),H_\varphi(\mathsf Y)\}\le H_\varphi(\mathsf X\cup\mathsf Y)\le H_\varphi(\mathsf X)+
H_\varphi(\mathsf Y)\).*

*(e) Convexity in the observations: for unital completely positive \(\gamma_j,\gamma'_j:A_j\to A\) and \(0\le\lambda\le1\),*
\[
H_\varphi\bigl(\lambda\gamma_1+(1-\lambda)\gamma'_1,\dots,\lambda\gamma_n+(1-\lambda)\gamma'_n\bigr)\le
\lambda H_\varphi(\gamma_1,\dots,\gamma_n)+(1-\lambda)H_\varphi(\gamma'_1,\dots,\gamma'_n).
\]

**Proof.** We use Proposition 6.4 throughout.

(a) For a decomposition \(\psi\), Proposition 2.5(d) gives
\(D(\psi^{(j)}_k\circ\gamma_j\circ\theta_j\|\varphi\circ\gamma_j\circ\theta_j)\le
D(\psi^{(j)}_k\circ\gamma_j\|\varphi\circ\gamma_j)\), so \(\mathcal E_{\gamma\circ\theta}(\psi)\le\mathcal E_\gamma(\psi)\).
If \(\theta_j\circ\beta_j=\mathrm{id}\), then \(\gamma_j=(\gamma_j\circ\theta_j)\circ\beta_j\) and the inequality just
proved gives the reverse inequality.

(b) If \(\psi\) is a decomposition of \(\varphi\), then \(\psi\circ\theta=(\psi_i\circ\theta)_i\) is a decomposition of
\(\varphi\circ\theta=\varphi\) (positivity of \(\theta\)), with \(\psi_i(\theta(1))=\psi_i(1)\), so
\(\mathcal E_{\theta\circ\gamma}(\psi)=\mathcal E_\gamma(\psi\circ\theta)\le H_\varphi(\gamma)\). If \(\theta\) is an
automorphism, apply this to \(\theta^{-1}\) and the maps \(\theta\circ\gamma_j\).

(c) Symmetry: permute the coordinates of the shape. Next, a decomposition \(\psi\) of shape \((I_1,\dots,I_n)\) gives
one of shape \((I_1,\dots,I_n,\{*\})\) with the same \(\eta\)-terms and an extra term
\(D(\varphi\circ\gamma_n\|\varphi\circ\gamma_n)=0\); so \(H_\varphi(\gamma_1,\dots,\gamma_n,\gamma_n)\ge
H_\varphi(\gamma_1,\dots,\gamma_n)\). Conversely let \(\psi\) have shape \((I_1,\dots,I_{n+1})\) and regard it as a
decomposition \(\psi'\) of shape \((I_1,\dots,I_{n-1},I_n\times I_{n+1})\). The \(\eta\)-terms and the terms for
\(j<n\) agree. For the last coordinate, Theorem 4.7, applied on \(A_n\) to the family
\(\sigma_{kl}=\psi'^{(n)}_{(k,l)}\circ\gamma_n\) with row and column sums \(\psi^{(n)}_k\circ\gamma_n\) and
\(\psi^{(n+1)}_l\circ\gamma_n\), gives
\(\sum_{k,l}D(\sigma_{kl}\|\varphi\circ\gamma_n)\ge\sum_kD(\psi^{(n)}_k\circ\gamma_n\|\varphi\circ\gamma_n)+
\sum_lD(\psi^{(n+1)}_l\circ\gamma_n\|\varphi\circ\gamma_n)\). Hence \(\mathcal E_{(\gamma_1,\dots,\gamma_n)}(\psi')\ge
\mathcal E_{(\gamma_1,\dots,\gamma_n,\gamma_n)}(\psi)\).

(d) By (c) we may compute with tuples. Adding trivial coordinates as in (c) gives the first inequality. For the second,
let \(\psi\) be a decomposition of shape \((I_1,\dots,I_{k+p})\) for the concatenated tuple, and let \(\psi',\psi''\) be
the decompositions of shapes \((I_1,\dots,I_k)\) and \((I_{k+1},\dots,I_{k+p})\) obtained by summing over the other
coordinates. They have the same marginals as \(\psi\), so the relative entropy terms split exactly, and by (B4),
\(\sum_i\eta(\psi_i(1))\le\sum\eta(\psi'(1))+\sum\eta(\psi''(1))\) (subadditivity of the Shannon entropy of the pair
of coordinate blocks). So \(\mathcal E(\psi)\le\mathcal E(\psi')+\mathcal E(\psi'')\).

(e) Fix a decomposition \(\psi\). The \(\eta\)-terms do not depend on the maps, and joint convexity gives
\[
D\bigl(\lambda\psi^{(j)}_k\gamma_j+(1-\lambda)\psi^{(j)}_k\gamma'_j\,\big\|\,\lambda\varphi\gamma_j+
(1-\lambda)\varphi\gamma'_j\bigr)\le\lambda D(\psi^{(j)}_k\gamma_j\|\varphi\gamma_j)+(1-\lambda)
D(\psi^{(j)}_k\gamma'_j\|\varphi\gamma'_j).
\]
So \(\mathcal E_{\lambda\gamma+(1-\lambda)\gamma'}(\psi)\le\lambda\mathcal E_\gamma(\psi)+(1-\lambda)
\mathcal E_{\gamma'}(\psi)\le\lambda H_\varphi(\gamma)+(1-\lambda)H_\varphi(\gamma')\). \(\square\)

**Theorem 7.2 (dependence on the state).** *Let \(\varphi_1,\varphi_2\) be states, \(0<\lambda<1\),
\(\varphi=\lambda\varphi_1+(1-\lambda)\varphi_2\) and \(h(\lambda)=\eta(\lambda)+\eta(1-\lambda)\).*

*(a) \(H_\varphi(\gamma_1,\dots,\gamma_n)\ge\lambda H_{\varphi_1}(\gamma_1,\dots,\gamma_n)+(1-\lambda)
H_{\varphi_2}(\gamma_1,\dots,\gamma_n)-(n-1)h(\lambda)\).*

*(b) Suppose that the element \(t\in\pi_\varphi(A)'\) with \(\lambda\varphi_1=\langle\xi_\varphi,t\pi_\varphi(\cdot)
\xi_\varphi\rangle\) (see (B3)) commutes with \(\pi_\varphi(A)'\). Then*
\[
H_\varphi(\gamma_1,\dots,\gamma_n)\le\lambda H_{\varphi_1}(\gamma_1,\dots,\gamma_n)+(1-\lambda)H_{\varphi_2}(\gamma_1,
\dots,\gamma_n)+h(\lambda).
\]
*The hypothesis of (b) holds if \(A\) is abelian, and if \(\lambda\varphi_1=\varphi(z\,\cdot)\) for some central element
\(z\) of \(A\) with \(0\le z\le1\).*

**Proof.** (a) Let \(\psi^1\), \(\psi^2\) be decompositions of \(\varphi_1,\varphi_2\) of shapes \((I^1_j)\), \((I^2_j)\).
Put \(I_j=I^1_j\sqcup I^2_j\), and let \(\psi_i=\lambda\psi^1_i\) if all coordinates of \(i\) lie in the first copies,
\(\psi_i=(1-\lambda)\psi^2_i\) if all lie in the second copies, and \(\psi_i=0\) otherwise. This is a decomposition of
\(\varphi\) whose marginals are \(\lambda\psi^{1,(j)}_k\) (\(k\in I^1_j\)) and \((1-\lambda)\psi^{2,(j)}_k\)
(\(k\in I^2_j\)). Since \(\eta(\lambda s)=\lambda\eta(s)+s\eta(\lambda)\) and \(\sum_i\psi^1_i(1)=1\),
\(\sum_i\eta(\psi_i(1))=\lambda\sum\eta(\psi^1_i(1))+(1-\lambda)\sum\eta(\psi^2_i(1))+h(\lambda)\). For the \(j\)-th
relative entropy term, write it with (3.1) as \(S(\varphi\circ\gamma_j)-\sum_kS(\cdot)\) over the marginals. By Lemma
3.2(a) the marginal entropies add up to \(\lambda\sum_kS(\psi^{1,(j)}_k\gamma_j)+(1-\lambda)\sum_kS(\psi^{2,(j)}_k
\gamma_j)+h(\lambda)\), and by concavity \(S(\varphi\gamma_j)\ge\lambda S(\varphi_1\gamma_j)+(1-\lambda)
S(\varphi_2\gamma_j)\). Hence the \(j\)-th term is at least \(\lambda\) times the corresponding term for \(\psi^1\), plus
\((1-\lambda)\) times that for \(\psi^2\), minus \(h(\lambda)\). Adding up,
\(\mathcal E_\gamma(\psi)\ge\lambda\mathcal E_\gamma(\psi^1)+(1-\lambda)\mathcal E_\gamma(\psi^2)-(n-1)h(\lambda)\).
Take suprema.

(b) Let \(\psi\) be a decomposition of \(\varphi\), with \(\psi_i=\langle\xi_\varphi,t_i\pi_\varphi(\cdot)\xi_\varphi
\rangle\), \(t_i\in\pi_\varphi(A)'_+\) (Corollary 6.5). Since \(t\) commutes with \(t_i\), \(tt_i\) and \((1-t)t_i\) are
positive elements of \(\pi_\varphi(A)'\), so
\(\psi^1_i=\lambda^{-1}\langle\xi_\varphi,tt_i\pi_\varphi(\cdot)\xi_\varphi\rangle\) and
\(\psi^2_i=(1-\lambda)^{-1}\langle\xi_\varphi,(1-t)t_i\pi_\varphi(\cdot)\xi_\varphi\rangle\) are decompositions of
\(\varphi_1\) and \(\varphi_2\) of the same shape, with \(\psi_i=\lambda\psi^1_i+(1-\lambda)\psi^2_i\) and the same
relation for the marginals. By (B4), \(\sum_i\eta(\psi_i(1))\le\lambda\sum_i\eta(\psi^1_i(1))+(1-\lambda)\sum_i
\eta(\psi^2_i(1))+h(\lambda)\), and by joint convexity each relative entropy term of \(\psi\) is at most \(\lambda\) times
that of \(\psi^1\) plus \((1-\lambda)\) times that of \(\psi^2\). So \(\mathcal E_\gamma(\psi)\le\lambda
H_{\varphi_1}+(1-\lambda)H_{\varphi_2}+h(\lambda)\).

If \(A\) is abelian, \(\pi_\varphi(A)'\) is abelian by (B3). If \(\lambda\varphi_1=\varphi(z\,\cdot)\) with \(z\)
central, then \(\pi_\varphi(z)\in\pi_\varphi(A)'\) represents \(\lambda\varphi_1\), so \(t=\pi_\varphi(z)\) by
uniqueness, and \(t\in\pi_\varphi(A)''\) commutes with \(\pi_\varphi(A)'\). \(\square\)

The hypothesis in (b) is exactly what is needed to split an arbitrary decomposition of \(\varphi\) into decompositions
of \(\varphi_1\) and \(\varphi_2\). Without it the splitting can be impossible:

**Example 7.3.** Let \(A=M_2(\mathbb C)\), \(\varphi=\operatorname{tr}\) the normalized trace, \(e_1,e_2\) the diagonal
matrix units and \(f_1,f_2\) the spectral projections of \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Then
\(\varphi=\tfrac12\omega_{e_1}+\tfrac12\omega_{e_2}=\tfrac12\omega_{f_1}+\tfrac12\omega_{f_2}\), where
\(\omega_e=\operatorname{Tr}(e\,\cdot)\). Suppose \(\psi^1_1+\psi^1_2=\omega_{f_1}\) with
\(\tfrac12\psi^1_k\le\tfrac12\omega_{e_k}\) and \(\psi^1_k\ge0\). The pure state \(\omega_{e_k}\) dominates only its own
multiples (as in the proof of Lemma 3.2(c)), so \(\psi^1_k=c_k\omega_{e_k}\) and \(\omega_{f_1}=c_1\omega_{e_1}+c_2\omega_{e_2}\) has a
diagonal density, which is false. So the decomposition \((\tfrac12\omega_{e_1},\tfrac12\omega_{e_2})\) of \(\varphi\)
cannot be written as \(\tfrac12\psi^1+\tfrac12\psi^2\) with decompositions \(\psi^1,\psi^2\) of \(\omega_{f_1}\),
\(\omega_{f_2}\): the positive cone of the dual of a noncommutative algebra lacks the Riesz decomposition property. (For
\(n=1\) and \(\gamma_1=\mathrm{id}\) the upper estimate itself holds here: by Exercise 9.3(a) it reads
\(S(\operatorname{tr})\le\tfrac12S(\omega_{f_1})+\tfrac12S(\omega_{f_2})+\log2\), that is, \(\log2\le\log2\).)

*Reference:* [Connes–Narnhofer–Thirring 1987] states the upper estimate of Theorem 7.2(b) without the commutation
hypothesis; the splitting of decompositions on which it rests fails in general (Example 7.3), so we prove it under the
hypothesis stated. We have neither a proof nor a counterexample for the upper estimate without it.

**Proposition 7.4 (matrix observations suffice).** *(a) For each \(j\), choose by Lemma 5.4 an embedding
\(A_j\subset M_{N_j}(\mathbb C)\) and a conditional expectation \(E_j:M_{N_j}(\mathbb C)\to A_j\). Then
\(H_\varphi(\gamma_1,\dots,\gamma_n)=H_\varphi(\gamma_1\circ E_1,\dots,\gamma_n\circ E_n)\).*

*(b) For \(X\in M_N(A)_+\) with \(\sum_iX_{ii}=1\), let \(\gamma_X:M_N(\mathbb C)\to A\) be the unital completely
positive map with \(\gamma_X(e_{ij})=X_{ij}\) (Lemma 5.1). Then \(H_\varphi(\gamma_{X_1},\dots,\gamma_{X_n})\) is
unchanged if some \(X_j\) is replaced by \(X_j\oplus0\in M_{N_j+1}(A)\). Consequently \(H_\varphi\) is a well-defined
function on the finite subsets of*
\[
\mathcal X(A)=\bigcup_N\Bigl\{X\in M_N(A)_+:\sum_iX_{ii}=1\Bigr\}\Big/\bigl(X\sim X\oplus0\bigr),
\]
*and every value \(H_\varphi(\gamma_1,\dots,\gamma_n)\) is a value of this function.*

**Proof.** (a) is Theorem 7.1(a) with \(\theta_j=E_j\), a conditional expectation onto \(A_j\). (b) Let
\(c:M_{N+1}\to M_N\) be the compression to the upper left corner, a unital completely positive map. Then
\(\gamma_{X\oplus0}=\gamma_X\circ c\), because both send \(e_{ij}\) to \(X_{ij}\) for \(i,j\le N\) and to \(0\)
otherwise. The map \(\beta(b)=b\oplus\operatorname{tr}(b)\) is a unital completely positive right inverse of \(c\), so
Theorem 7.1(a) gives equality. Together with Theorem 7.1(c), (a), and Lemma 5.1 (which writes \(\gamma_j\circ E_j\) as
some \(\gamma_{X_j}\)), this proves the last assertions. \(\square\)

By Proposition 5.2, for a nuclear algebra there are many such \(X\); this is the setting in which the dynamical entropy
is built in the lesson "Dynamical entropy of C\*-algebras and von Neumann algebras".

## 8. Continuity in the norm topology

For maps \(\gamma,\gamma':A_0\to A\) put \(\|\gamma-\gamma'\|=\sup_{\|a\|\le1}\|\gamma(a)-\gamma'(a)\|\). For \(N\ge1\) let
\[
F_N(\varepsilon)=3\varepsilon\Bigl(\frac12+\log\Bigl(1+\frac N\varepsilon\Bigr)\Bigr)\quad(\varepsilon>0),\qquad
F_N(0)=0.
\]
\(F_N\) is continuous and increasing on \([0,\infty)\), since the derivative of \(\varepsilon\log(1+N/\varepsilon)\) is
\(\log(1+u)-u/(1+u)>0\) with \(u=N/\varepsilon\).

**Lemma 8.1 (continuity of entropy).** *Let \(A\) be finite-dimensional and \(\varphi,\psi\) states with
\(\|\varphi-\psi\|=\varepsilon\). Then \(|S(\varphi)-S(\psi)|\le F_{N(A)}(\varepsilon)\le F_{\dim A}(\varepsilon)\).*

**Proof.** For \(s\in[0,1]\) and \(t>0\) put \(f_t(s)=\frac s{s+t}-\frac s{1+t}=\frac{s(1-s)}{(s+t)(1+t)}\in[0,1]\).
Then \(\int_0^\infty f_t(s)\,dt=s\bigl[\log\frac{s+t}{1+t}\bigr]_0^\infty=\eta(s)\), so
\(S(\varphi)-S(\psi)=\int_0^\infty\operatorname{Tr}\bigl(f_t(\rho_\varphi)-f_t(\rho_\psi)\bigr)dt\), where
\(N=N(A)\). Fix \(\delta>0\). For \(t<\delta\), both traces lie in \([0,N]\), so the integral over \((0,\delta)\) is at
most \(\delta N\) in absolute value. For \(t\ge\delta\) put \(R_\varphi=(\rho_\varphi+t)^{-1}\),
\(R_\psi=(\rho_\psi+t)^{-1}\) and \(\Delta=\rho_\varphi-\rho_\psi\), so \(\|\Delta\|_1=\varepsilon\) by (B1). Since
\(f_t(\rho)=1-tR-\rho/(1+t)\) and \(R_\psi-R_\varphi=R_\varphi\Delta R_\psi\),
\[
f_t(\rho_\varphi)-f_t(\rho_\psi)=tR_\varphi\Delta R_\psi-\frac\Delta{1+t}
=\frac{1}{1+t}R_\varphi\bigl(t\Delta-t\rho_\varphi\Delta-t\Delta\rho_\psi-\rho_\varphi\Delta\rho_\psi\bigr)R_\psi,
\]
as one checks by writing \(\Delta=R_\varphi(\rho_\varphi+t)\Delta(\rho_\psi+t)R_\psi\) and expanding. Now
\(\|R_\varphi\|,\|R_\psi\|\le1/t\), \(\|R_\varphi\rho_\varphi\|,\|\rho_\psi R_\psi\|\le1\) and, since
\(s/(s+t)\le1/(1+t)\) on \([0,1]\), \(\|R_\varphi\rho_\varphi\|,\|\rho_\psi R_\psi\|\le(1+t)^{-1}\). Using
\(\|abc\|_1\le\|a\|\|b\|_1\|c\|\), the four terms have trace norm at most \(\varepsilon/t\), \(\varepsilon/t\),
\(\varepsilon/t\) and \(\varepsilon/(1+t)^2\). Hence, with \(|\operatorname{Tr}z|\le\|z\|_1\),
\[
|S(\varphi)-S(\psi)|\le\delta N+\varepsilon\int_\delta^\infty\Bigl(\frac3{t(1+t)}+\frac1{(1+t)^3}\Bigr)dt
\le\delta N+\varepsilon\Bigl(3\log\Bigl(1+\frac1\delta\Bigr)+\frac12\Bigr).
\]
For \(\varepsilon>0\) take \(\delta=\varepsilon/N\). Finally \(N(A)\le\dim A\) and \(F_N\) increases with \(N\).
\(\square\)

**Lemma 8.2 (continuity of the defect).** *Let \(A\) be finite-dimensional, \(\mu\) a state on \(C(X)\) and
\(\rho,\rho':A\to C(X)\) unital positive maps with \(\|\rho-\rho'\|=\varepsilon\). Then
\(|s_\mu(\rho)-s_\mu(\rho')|\le2F_{N(A)}(\varepsilon)\).*

**Proof.** \(|s_\mu(\rho)-s_\mu(\rho')|=|\varepsilon_\mu(\rho)-\varepsilon_\mu(\rho')|\), and by Theorem 4.5(a)
\(\varepsilon_\mu(\rho)=S(\mu\circ\rho)-\sum_x\mu_xS(\rho_x)\). For \(\|a\|\le1\),
\(|\rho_x(a)-\rho'_x(a)|\le\|\rho(a)-\rho'(a)\|\le\varepsilon\) and likewise for \(\mu\circ\rho\), so all the relevant
states are within \(\varepsilon\) of each other. By Lemma 8.1 and the monotonicity of \(F_N\),
\(|\varepsilon_\mu(\rho)-\varepsilon_\mu(\rho')|\le F_N(\varepsilon)+\sum_x\mu_xF_N(\varepsilon)=2F_N(\varepsilon)\).
\(\square\)

**Theorem 8.3 (norm continuity of \(H_\varphi\)).** *Let \(\gamma_j,\gamma'_j:A_j\to A\) be unital completely positive,
\(d=\max_j\dim A_j\) and \(\varepsilon=\max_j\|\gamma_j-\gamma'_j\|\). Then*
\[
\bigl|H_\varphi(\gamma_1,\dots,\gamma_n)-H_\varphi(\gamma'_1,\dots,\gamma'_n)\bigr|\le2nF_d(\varepsilon)=
6n\varepsilon\Bigl(\frac12+\log\Bigl(1+\frac d\varepsilon\Bigr)\Bigr).
\]

**Proof.** Fix an abelian model. The maps \(E_j\circ P:A\to B_j\) are unital positive maps into abelian algebras, whose
coordinates are states, so they are contractions for the sup norm. Hence \(\rho_j=E_jP\gamma_j\) and
\(\rho'_j=E_jP\gamma'_j\) satisfy \(\|\rho_j-\rho'_j\|\le\varepsilon\), and by Lemma 8.2 (with \(N(A_j)\le d\) and
\(F_N\) increasing in \(N\) and \(\varepsilon\)) \(|s(\rho_j)-s(\rho'_j)|\le2F_d(\varepsilon)\). The first term of
(6.1) does not depend on the \(\gamma\)'s, so the entropies of the model for \((\gamma_j)\) and for \((\gamma'_j)\)
differ by at most \(2nF_d(\varepsilon)\). Taking suprema over all models gives
\(H_\varphi(\gamma)\le H_\varphi(\gamma')+2nF_d(\varepsilon)\) and the symmetric inequality. \(\square\)

In particular \(H_\varphi\) is uniformly continuous on the set of \(n\)-tuples of unital completely positive maps from
algebras of dimension at most \(d\), and the modulus of continuity does not depend on \(A\) or \(\varphi\).

## 9. Exercises

**Exercise 9.1 (the classical case).** Let \(A=C(Y)\) with \(Y\) finite, \(P:A\to C(X)\) unital positive and \(\mu\) a
state on \(C(X)\). Put \(p(x,y)=\mu_xP_x(\{y\})\), a probability on \(X\times Y\) with random variables \(\xi(x,y)=x\),
\(\zeta(x,y)=y\). Show that \(\varepsilon_\mu(P)=H(\xi)+H(\zeta)-H(\xi,\zeta)\) (the mutual information) and
\(s_\mu(P)=H(\xi\mid\zeta)\).

*Solution.* Here \(\varphi=\mu\circ P\) is the distribution of \(\zeta\), and by (2.2)
\(D(P_x\|\varphi)=\sum_yP_x(\{y\})\log\frac{P_x(\{y\})}{p(\zeta=y)}\). Multiplying by \(\mu_x\) and summing,
\(\varepsilon_\mu(P)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(\xi=x)p(\zeta=y)}=H(\xi)+H(\zeta)-H(\xi,\zeta)\). Then
\(s_\mu(P)=S(\mu)-\varepsilon_\mu(P)=H(\xi)-\varepsilon_\mu(P)=H(\xi,\zeta)-H(\zeta)=H(\xi\mid\zeta)\). So the
defect vanishes iff the outcome \(x\) is a function of \(y\) almost surely, in accordance with Theorem 4.5(b).

**Exercise 9.2.** Let \(A\) be finite-dimensional. Show that \(s_\mu(P)=S(\mu)\) iff \(P_x=\mu\circ P\) for every \(x\)
with \(\mu_x>0\).

*Solution.* \(s_\mu(P)=S(\mu)\) iff \(\varepsilon_\mu(P)=0\) iff \(D(P_x\|\mu\circ P)=0\) for every \(x\) with
\(\mu_x>0\), since each term is \(\ge0\). By Corollary 2.6(a), for states this happens iff \(P_x=\mu\circ P\).

**Exercise 9.3.** (a) Let \(A\) be finite-dimensional. Show that \(H_\varphi(\mathrm{id}_A)=S(\varphi)\).
(b) Let \(A=M_2(\mathbb C)\), \(\varphi=\operatorname{tr}\), and let \(D,D'\) be the diagonal subalgebra and the
subalgebra generated by \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Show that \(H_{\operatorname{tr}}(D,D')=\log2\),
whereas \(S(\operatorname{tr}|_D)+S(\operatorname{tr}|_{D'})=2\log2\).

*Solution.* (a) By Proposition 6.3, \(H_\varphi(\mathrm{id}_A)\le S(\varphi)\). Write \(\rho_\varphi=\sum_k\lambda_ke_k\)
and take the decomposition \(\psi_k=\lambda_k\operatorname{Tr}(e_k\,\cdot)\) (shape \((I_1)\), \(n=1\), over \(k\) with
\(\lambda_k>0\)). By (2.2), \(D(\psi_k\|\varphi)=\lambda_k\log\lambda_k-\lambda_k\log\lambda_k=0\), because
\(\log\rho_\varphi\) equals \(\log\lambda_k\) on \(e_k\). So \(\mathcal E(\psi)=\sum_k\eta(\lambda_k)=S(\varphi)\).

(b) Upper bound: by Theorem 7.1(a) (with \(\theta_1,\theta_2\) the inclusions of \(D,D'\) and
\(\gamma_1=\gamma_2=\mathrm{id}\)), Theorem 7.1(c) and (a), \(H_{\operatorname{tr}}(D,D')\le
H_{\operatorname{tr}}(\mathrm{id},\mathrm{id})=H_{\operatorname{tr}}(\mathrm{id})=S(\operatorname{tr})=\log2\). Lower
bound: take shape \((\{1,2\},\{*\})\) and \(\psi_{(k,*)}=\tfrac12\operatorname{Tr}(e_k\,\cdot)\). The \(\eta\)-terms give
\(\log2\). Restricted to \(D\cong C(\{1,2\})\), \(\psi_{(k,*)}\) is \(\tfrac12\delta_k\) and
\(\operatorname{tr}|_D=(\tfrac12,\tfrac12)\), so \(D(\tfrac12\delta_k\|\operatorname{tr}|_D)=\tfrac12\log1=0\). The only
marginal for the second coordinate is \(\operatorname{tr}\), with relative entropy \(0\). So
\(H_{\operatorname{tr}}(D,D')\ge\log2\). Finally \(S(\operatorname{tr}|_D)=S(\operatorname{tr}|_{D'})=\log2\). The two
observations are "complementary": together they carry no more information than the whole algebra.

**Exercise 9.4.** Let \(N\subset A\) be a finite-dimensional unital subalgebra and suppose there is a conditional
expectation \(E:A\to N\) with \(\varphi\circ E=\varphi\). Show that \(H_\varphi(N)=S(\varphi|_N)\).

*Solution.* By Proposition 6.3, \(H_\varphi(N)\le S(\varphi|_N)\). Write the density of \(\varphi|_N\) in \(N\) as
\(\sum_k\lambda_ke_k\) with minimal projections \(e_k\) of \(N\), and put \(\psi_k=\lambda_k\operatorname{Tr}_N(e_k
E(\cdot))\). These are positive functionals on \(A\) with \(\sum_k\psi_k=\varphi|_N\circ E=\varphi\), and
\(\psi_k|_N=\lambda_k\operatorname{Tr}_N(e_k\,\cdot)\) because \(E\) is the identity on \(N\). The computation of
Exercise 9.3(a), carried out in \(N\), gives \(\mathcal E(\psi)=S(\varphi|_N)\). For instance, in Exercise 9.3(b)
the trace-preserving expectations onto \(D\) and \(D'\) give \(H_{\operatorname{tr}}(D)=H_{\operatorname{tr}}(D')=\log2\),
while the pair has \(H_{\operatorname{tr}}(D,D')=\log2\) as well.

## References



- [Connes–Narnhofer–Thirring 1987] A. Connes, H. Narnhofer and W. Thirring, Dynamical entropy of C* algebras and von
  Neumann algebras, Comm. Math. Phys. 112 (1987), no. 4, 691–719. Free at https://alainconnes.org/wp-content/uploads/entropy.pdf
- [Connes–Størmer 1975] A. Connes and E. Størmer, Entropy for automorphisms of II₁ von Neumann algebras, Acta Math.
  134 (1975), no. 3–4, 289–306. Free at https://doi.org/10.1007/BF02392105
- [Connes 1994] A. Connes, *Noncommutative geometry*, Academic Press, San Diego, CA, 1994. Free at
  https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf
- [Araki 1976] H. Araki, Relative entropy of states of von Neumann algebras, Publ. Res. Inst. Math. Sci. 11
  (1975/76), no. 3, 809–833. https://doi.org/10.2977/prims/1195191148
- [Kosaki 1986] H. Kosaki, Relative entropy of states: a variational expression, J. Operator Theory 16 (1986), no. 2,
  335–348. https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-010.html
- [Takesaki 1972] M. Takesaki, Conditional expectations in von Neumann algebras, J. Functional Analysis 9 (1972),
  306–321. https://doi.org/10.1016/0022-1236(72)90004-3. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123672900043
- [Tomiyama 1957] J. Tomiyama, On the projection of norm one in W*-algebras, Proc. Japan Acad. 33 (1957), 608–612.
  https://doi.org/10.3792/pja/1195524885

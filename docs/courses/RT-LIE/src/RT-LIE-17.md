# Compact real forms and Weyl's unitary trick

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A positive Hermitian form need not be preserved by a complex Lie algebra. A compact real form supplies a smaller real algebra whose action can preserve one. Integrating that action to a compact group makes averaging available; its invariant orthogonal complements are then invariant under the whole complex algebra. This gives a second proof of complete reducibility.

Throughout, \(\mathfrak g\) is finite-dimensional and semisimple over \(\mathbb C\), and \(\kappa(X,Y)=\operatorname{Tr}(\operatorname{ad}X\operatorname{ad}Y)\). Brackets of matrices are ordinary commutators. All representation spaces are finite-dimensional **complex** vector spaces, unless expressly described as real. A representation of a real Lie algebra on such a space is real-linear in its Lie algebra argument and complex-linear in its vector argument. The signature of a real symmetric form is ordered as (positive dimension, negative dimension).

We use the root decomposition and coroots from [The root space decomposition of a semisimple Lie algebra](RT-LIE-07.md#section-2), inner derivations and the matrix Killing trace formula from [The Killing form and Cartan's criteria](RT-LIE-03.md#theorem-5-1), and the classical models and Chevalley-basis existence theorem from [The simple Lie algebras: classical models and the exceptional algebras](RT-LIE-12.md#section-5). The independent algebraic proof is in [Complete reducibility: Casimir elements and Weyl's theorem](RT-LIE-04.md#theorem-3-3). The invariant-complement argument in Section 5 does not assume that algebraic theorem; the principal rank-one construction in Lemma 8.8 later uses it. The compact-group course gives further context for maximal tori; the proof here does not assume its maximal torus theorem.

The later arguments use [the finite rank-one module classification](RT-LIE-05.md#theorem-2-1) and [its polynomial group action](RT-LIE-05.md#proposition-2-2), [the base and chamber theorem](RT-LIE-08.md#theorem-5-1), [the identity-component description of inner automorphisms](RT-LIE-10.md#theorem-3-2), and [the Serre presentation](RT-LIE-11.md#theorem-6-1) with [the scalar stabilizer and inner Cartan normalizer](RT-LIE-11.md#section-9).

## 1. Keeping the real and complex structures separate

A **real form** of \(\mathfrak g\) is a real Lie subalgebra \(\mathfrak g_0\) such that
\[
\mathfrak g=\mathfrak g_0\oplus i\mathfrak g_0
\quad\text{as real vector spaces}. \tag{1.1}
\]
Equivalently, the natural complex-linear map \(\mathfrak g_0\otimes_{\mathbb R}\mathbb C\to\mathfrak g\) is an isomorphism. In particular \(\dim_{\mathbb R}\mathfrak g_0=\dim_{\mathbb C}\mathfrak g\).

**Lemma 1.1.** Real forms are exactly the fixed spaces of conjugate-linear Lie algebra automorphisms \(\sigma\) with \(\sigma^2=1\).

**Proof.** A real form defines \(\sigma(X+iY)=X-iY\) for \(X,Y\in\mathfrak g_0\); the real bracket shows that this is a Lie automorphism. Conversely, for such a \(\sigma\), every \(Z\) has the unique decomposition
\[
Z=\frac{Z+\sigma Z}{2}+i\frac{Z-\sigma Z}{2i}. \tag{1.2}
\]
Both displayed components are fixed by \(\sigma\). A fixed vector that is also \(i\) times a fixed vector must be zero, since \(\sigma(iY)=-iY\). Fixed vectors are closed under brackets, proving (1.1). \(\square\)

The real matrix algebra \(\mathfrak{sl}_n(\mathbb R)\) is the fixed space of entrywise conjugation on \(\mathfrak{sl}_n(\mathbb C)\). Other conjugations give different real forms of the same complex algebra. Equality of complexifications does not imply real isomorphism.

If \(\mathfrak u\) is a real form, restriction gives a bijection between complex-linear representations \(\rho:\mathfrak g\to\mathfrak{gl}_{\mathbb C}(V)\) and real-linear representations \(r:\mathfrak u\to\mathfrak{gl}_{\mathbb C}(V)\): the inverse is
\[
\rho(X+iY)=r(X)+i r(Y). \tag{1.3}
\]
Expanding the bracket proves this is a representation. Complex-linear intertwiners and complex invariant subspaces are unchanged by the two operations. Representations on arbitrary real vector spaces are a different category.

## 2. Constructing the negative real form

Choose a Cartan subalgebra \(\mathfrak h\), positive roots \(\Phi^+\), simple coroots \(h_i\), and root vectors \(e_\alpha\) in the following normalization:
\[
[h_i,e_\alpha]=\alpha(h_i)e_\alpha,\qquad
[e_\alpha,e_{-\alpha}]=h_\alpha,\qquad
[h_\alpha,e_\alpha]=2e_\alpha, \tag{2.1}
\]
where all \(\alpha(h_i)\) are real and \(h_\alpha\) is a real linear combination of the \(h_i\). For \(\alpha+\beta\in\Phi\), require
\[
[e_\alpha,e_\beta]=N_{\alpha,\beta}e_{\alpha+\beta},\qquad
N_{\alpha,\beta}\in\mathbb R,\qquad
N_{-\alpha,-\beta}=-N_{\alpha,\beta}. \tag{2.2}
\]
For \(\beta\ne-\alpha\) and \(\alpha+\beta\notin\Phi\), the bracket is zero. Opposite roots must be handled by (2.1), since zero is not a root.

The simultaneous integral basis and the opposite-root sign condition have been proved in [the integral basis theorem, Theorem 5.1](RT-LIE-12.md#section-5). Apply that construction to obtain (2.1)–(2.2). Real constants suffice for the argument below; the construction supplies integers.

Put \(\mathfrak h_{\mathbb R}=\sum_i\mathbb R h_i\), and for \(\alpha>0\) set
\[
A_\alpha=e_\alpha-e_{-\alpha},\qquad
B_\alpha=i(e_\alpha+e_{-\alpha}),\qquad
\mathfrak u=i\mathfrak h_{\mathbb R}
\oplus\bigoplus_{\alpha>0}(\mathbb R A_\alpha\oplus\mathbb R B_\alpha). \tag{2.3}
\]

**Theorem 2.1 (compact real form).** The space \(\mathfrak u\) is a real form of \(\mathfrak g\), and the restriction of \(\kappa\) to \(\mathfrak u\) is real and negative definite.

**Proof of closure and the real-form assertion.** Define a conjugate-linear map on the complex basis by
\[
\tau(h_i)=-h_i,\qquad \tau(e_\alpha)=-e_{-\alpha}. \tag{2.4}
\]
It squares to the identity. We check every type of basis bracket. Cartan elements commute. For the Cartan-root bracket, realness of \(\alpha(h_i)\) gives
\[
\tau([h_i,e_\alpha])=-\alpha(h_i)e_{-\alpha}
=[-h_i,-e_{-\alpha}].
\]
For opposite roots, using \(\tau(h_\alpha)=-h_\alpha\),
\[
\tau([e_\alpha,e_{-\alpha}])=-h_\alpha
=[-e_{-\alpha},-e_\alpha].
\]
If \(\alpha+\beta\) is a root, the two sides of bracket compatibility are
\[
-N_{\alpha,\beta}e_{-\alpha-\beta},\qquad
N_{-\alpha,-\beta}e_{-\alpha-\beta};
\]
they agree precisely by (2.2). In the remaining nonopposite case both brackets vanish; this includes equal roots, since the root system is reduced. Thus \(\tau\) is a Lie automorphism.

A Cartan coefficient is fixed exactly when it is purely imaginary. For a root pair, \(a e_\alpha+b e_{-\alpha}\) is fixed exactly when \(b=-\overline a\). Writing \(a=s+it\) expresses that fixed vector as \(sA_\alpha+tB_\alpha\). Therefore \(\mathfrak u=\mathfrak g^\tau\), and Lemma 1.1 proves both closure and (1.1). This also proves that the displayed generators form a real basis. \(\square\)

**Proof of negative definiteness.** For \(H\in\mathfrak h_{\mathbb R}\), the root decomposition gives
\[
\kappa(H,H)=\sum_{\gamma\in\Phi}\gamma(H)^2. \tag{2.5}
\]
Every term is real and nonnegative. If all vanish, \(H\) commutes with every root space and with \(\mathfrak h\), so it is central and hence zero. Thus (2.5) is positive definite on \(\mathfrak h_{\mathbb R}\).

Invariance of \(\kappa\) makes \(\mathfrak h\) orthogonal to root spaces and makes \(\mathfrak g_\alpha\) orthogonal to \(\mathfrak g_\beta\) unless \(\alpha+\beta=0\). For example, choosing \(H\) with \((\alpha+\beta)(H)\ne0\) in
\(\kappa([H,X],Y)+\kappa(X,[H,Y])=0\) gives the second assertion. Write \(c_\alpha=\kappa(e_\alpha,e_{-\alpha})\). Then
\[
\kappa(h_\alpha,h_\alpha)
=\kappa([e_\alpha,e_{-\alpha}],h_\alpha)
=\kappa(e_\alpha,[e_{-\alpha},h_\alpha])
=2c_\alpha,
\]
so \(c_\alpha>0\). Consequently
\[
\kappa(A_\alpha,A_\alpha)=\kappa(B_\alpha,B_\alpha)=-2c_\alpha,
\qquad\kappa(A_\alpha,B_\alpha)=0. \tag{2.6}
\]
Different positive-root pairs are orthogonal. On \(i\mathfrak h_{\mathbb R}\), the form is the negative of (2.5). Every block is real and negative definite, proving the theorem. \(\square\)

The same real basis identifies the real Killing form of \(\mathfrak u\) with \(\kappa|_{\mathfrak u}\): extending a real matrix of \(\operatorname{ad}X\operatorname{ad}Y\) to complex scalars leaves its trace unchanged.

A semisimple real Lie algebra with negative definite Killing form is called **of compact type**. The following argument proves uniqueness of the real form under inner automorphisms; Section 3 then constructs its compact simply connected group.

### 2.1. Positive spectral powers

**Lemma 2.2.** Let \(A\) be a diagonalizable complex-linear Lie automorphism of a finite-dimensional complex Lie algebra, and suppose its eigenvalues are positive real numbers. For every real \(t\), the spectral power \(A^t\) is a Lie automorphism.

**Proof.** Write \(\mathfrak g=\bigoplus_{\lambda>0}E_\lambda\). If \(x\in E_\lambda\), \(y\in E_\mu\), then
\[
 A[x,y]=[Ax,Ay]=\lambda\mu[x,y].
\]
Thus either the bracket is zero or it lies in \(E_{\lambda\mu}\). On such a pair,
\[
 A^t[x,y]=(\lambda\mu)^t[x,y]=[A^tx,A^ty].
\]
Bilinearity proves bracket preservation on all vectors, and \(A^{-t}\) is its inverse. The matrix \(A^t=\sum_\lambda\lambda^t P_\lambda\), for fixed spectral projections \(P_\lambda\), depends continuously on \(t\). \(\square\)

We will use that each \(A^t\) is inner when \(\mathfrak g\) is complex semisimple. The path \(s\mapsto A^{st}\), \(0\le s\le1\), stays in the identity component of its algebraic automorphism group: a finite-type algebraic group has finitely many connected components, each Zariski open and closed, hence also open and closed in the ordinary complex topology. The continuous image of an interval starting at the identity cannot leave this component. [RT-LIE-10, Theorem 3.2](RT-LIE-10.md#theorem-3-2), identifies its complex points with the actual subgroup of finite products of nilpotent inner exponentials.

For completeness, \(D=\log A\) is also a derivation: on \(E_\lambda,E_\mu\), the equality \(\log(\lambda\mu)=\log\lambda+\log\mu\) gives the derivation rule. Thus \(D=\operatorname{ad}Z\) for a semisimple algebra, although this observation is not needed to replace the component argument.

### 2.2. Inner conjugacy of compact real forms

**Theorem 2.3.** Any two compact real forms of a finite-dimensional complex semisimple Lie algebra are conjugate by an inner complex Lie algebra automorphism.

**Proof.** Let \(\sigma,\tau\) be their conjugate-linear Lie involutions. A real form has the decomposition \(\mathfrak g=\mathfrak u\oplus i\mathfrak u\), so each is recovered from its fixed subspace. Every such conjugation satisfies
\[
 \kappa(\sigma x,\sigma y)=\overline{\kappa(x,y)}.
\]
Indeed, compute the trace defining the Killing form in a real basis of its fixed real form. The same assertion holds for \(\tau\).

Define Hermitian forms, linear in the first variable, by
\[
 H_\sigma(x,y)=-\kappa(x,\sigma y),\qquad
 H_\tau(x,y)=-\kappa(x,\tau y).
\]
The displayed conjugation identity and symmetry of \(\kappa\) give Hermitian symmetry. If \(x=a+ib\), \(a,b\in\operatorname{Fix}\sigma\), then
\[
 H_\sigma(x,x)=-\kappa(a,a)-\kappa(b,b)>0
 \quad(x\ne0).
\]
Thus both forms are positive definite.

Set \(S=\sigma\tau\), a complex-linear Lie automorphism. Directly,
\[
 \begin{aligned}
 H_\sigma(Sx,y)
 &=-\kappa(\sigma\tau x,\sigma y)\\
 &=-\overline{\kappa(\tau x,y)}
 =-\kappa(x,\tau y)=H_\tau(x,y).
 \end{aligned}
\]
Hermitian symmetry therefore makes \(S\) self-adjoint with respect to \(H_\sigma\), and \(H_\sigma(Sx,x)>0\) makes it positive definite. The finite-dimensional Hermitian spectral theorem gives a decomposition into positive real eigenspaces, so Lemma 2.2 applies.

The involution identity gives \(\sigma S\sigma=S^{-1}\). Because all its eigenvalues are positive real, spectral calculus gives
\[
 \sigma S^t\sigma=S^{-t}\qquad(t\in\mathbb R).
\]
For example, if \(Sx=\lambda x\), then \(S(\sigma x)=\lambda^{-1}\sigma x\), which proves this formula on every eigenspace. Put \(a=S^{-1/2}\). Then
\[
 a\sigma a^{-1}
 =S^{-1/2}\sigma S^{1/2}
 =S^{-1}\sigma=\sigma S=\tau.
\]
Consequently \(a(\operatorname{Fix}\sigma)=\operatorname{Fix}\tau\). The preceding spectral-power argument proves that \(a\) is inner. This proves the theorem for all ranks and any number of simple components; for \(\mathfrak g=0\), the unique real form and automorphism make the assertion immediate. \(\square\)

This is uniqueness under \(\operatorname{Int}(\mathfrak g)\) over \(\mathbb C\). It makes no statement about nonsplit forms over other fields.

## 3. Producing the compact group

Let \(\mathfrak u\) be the real algebra just constructed and \(b=-\kappa|_{\mathfrak u}\). Every automorphism preserves its Killing form. Thus
\[
\operatorname{Aut}(\mathfrak u)
=\{T\in O(\mathfrak u,b):T[X,Y]=[TX,TY]\ \text{for all }X,Y\} \tag{3.1}
\]
is a closed subset of a compact orthogonal group. By the closed subgroup theorem it is a compact Lie group.

Its Lie algebra is \(\operatorname{Der}(\mathfrak u)\). Differentiating bracket preservation proves one inclusion. Conversely, if \(\delta\) is a derivation, induction gives
\[
\delta^m[X,Y]=\sum_{j=0}^m\binom mj[\delta^jX,\delta^{m-j}Y].
\]
The convergent exponential series implies \(e^{t\delta}[X,Y]=[e^{t\delta}X,e^{t\delta}Y]\), proving the other inclusion.

Moreover \(\operatorname{Der}(\mathfrak u)=\operatorname{ad}\mathfrak u\). Indeed, complexify a derivation. By the verified inner-derivation theorem for \(\mathfrak g\), its extension is \(\operatorname{ad}Z\). It commutes with \(\tau\), so \(\operatorname{ad}\tau Z=\operatorname{ad}Z\). The center of \(\mathfrak g\) is zero, giving \(\tau Z=Z\), hence \(Z\in\mathfrak u\). The center of \(\mathfrak u\) is also zero, so \(\operatorname{ad}:\mathfrak u\to\operatorname{Der}(\mathfrak u)\) is an isomorphism. We have constructed a compact connected group
\[
K_{\mathrm{ad}}=\operatorname{Aut}(\mathfrak u)^0,
\qquad \operatorname{Lie}(K_{\mathrm{ad}})\simeq\mathfrak u. \tag{3.2}
\]
The identity component is closed, which is why compactness is retained.

We prove that the simply connected cover of this compact adjoint group is compact, including the needed covering and finiteness arguments.

### 3.1. Finite generation of loops

**Lemma 3.2.** The fundamental group of a compact connected Lie group \(L\) is finitely generated.

**Proof.** Choose an exponential coordinate ball \(V\) at the identity which is contractible. By continuity of multiplication and inversion, choose a smaller symmetric, path-connected exponential ball \(U\) such that \(U^4\subset V\). Compactness gives a finite set \(F\subset L\), including the identity, with \(L=\bigcup_{p\in F}pU\).

Let \(\gamma\) be a based loop at the identity. Choose a subdivision \(0=t_0<\cdots<t_N=1\) fine enough that
\[
 \gamma(t_k)^{-1}\gamma(t)\in U
 \quad(t_k\le t\le t_{k+1}).
\]
Such a subdivision exists by compactness of the interval and continuity. Put \(x_k=\gamma(t_k)\), choose \(p_k\in F\) with \(x_k=p_k u_k\), \(u_k\in U\), and take \(p_0=p_N=1\). Then
\[
 p_k^{-1}p_{k+1}
 =u_k(x_k^{-1}x_{k+1})u_{k+1}^{-1}\in U^3.
\]
For every ordered pair \((p,q)\in F^2\) satisfying \(p^{-1}q\in U^3\), choose once and for all a path \(\mu_{pq}\) from \(p\) to \(q\) inside \(pV\); its existence follows from the coordinate-ball contractibility of \(V\).

Join \(p_k\) to \(x_k\) within \(p_kU\). The path from \(p_k\) to \(p_{k+1}\) consisting of that connector, the original loop segment, and the reversed endpoint connector lies entirely in \(p_kV\): the original segment lies in \(p_kU^2\), and \(p_{k+1}U\subset p_kU^4\). Since \(p_kV\) is simply connected, this path and \(\mu_{p_kp_{k+1}}\) are homotopic with their endpoints fixed. Apply these homotopies to all segments. The intermediate connector and its reversal cancel, so \(\gamma\) is homotopic to a concatenation of the finitely many paths \(\mu_{pq}\).

These paths define a finite graph mapped into \(L\). Only its component containing \(1\) is relevant. Choose a spanning tree of that finite component, and let \(a_p\) be the unique tree path from \(1\) to its vertex \(p\). For each directed edge from \(p\) to \(q\), take the based loop \(a_p\mu_{pq}a_q^{-1}\). Any graph loop is the product of these finitely many loops for its consecutive edges: the adjacent factors \(a_q^{-1}a_q\) cancel by retracing, leaving the original graph loop. Thus no general graph fundamental-group theorem is needed. Since every loop in \(L\) is represented by a graph loop, these images finitely generate \(\pi_1(L)\). This argument is valid for continuous loops. For integration below, loops and homotopies can be replaced by piecewise smooth ones using straight segments in finitely many coordinate charts, which is the elementary smoothing input already declared in this lesson. \(\square\)

### 3.2. The covering Lie group and central kernel

Here is the basic covering construction, to make the precise topological input visible. For a connected Lie group \(L\), take endpoint-fixed homotopy classes \([\alpha]\) of paths \(\alpha\) from \(1\), and let \(p([\alpha])=\alpha(1)\). Over a contractible coordinate neighborhood \(W\) of \(x\), append paths in \(W\) to a fixed path ending at \(x\). Since any two such paths with the same endpoints are homotopic within \(W\), this gives a sheet identified with \(W\). Different path classes give disjoint sheets; these sheets define the covering topology. Distinct endpoints are separated downstairs, and distinct classes over the same endpoint are separated by disjoint sheets, so the space is Hausdorff.

The finite generation in Lemma 3.2 implies countably many classes of loops, hence countably many sheets over each member of a countable coordinate cover of \(L\). Thus for the compact \(L\) used here this is a second-countable manifold. Give its sheets the pulled-back smooth charts of \(L\).

Define
\[
 [\alpha][\beta]=[\,t\mapsto\alpha(t)\beta(t)\,],
 \qquad [\alpha]^{-1}=[\,t\mapsto\alpha(t)^{-1}\,].
\]
Endpoint-fixed homotopies show these operations are well defined; the group identities hold pointwise. The endpoint map is a homomorphism. To verify the local charts for multiplication, represent nearby classes by a fixed path \(\alpha\) followed by a short coordinate path at its endpoint, and likewise for \(\beta\). Reparametrize both to traverse the fixed parts during the first half of the interval. Their pointwise product is then the fixed product path \(\alpha\beta\) followed by the product of the two short coordinate paths. Restrict the neighborhoods so that all these short products stay in a contractible coordinate neighborhood of \(\alpha(1)\beta(1)\). The products therefore lie in the sheet over that neighborhood fixed by \([\alpha\beta]\), and their chart coordinates are exactly the smooth multiplication downstairs. Pointwise inversion has the same local chart verification using inverted short paths. This gives a Lie group \(\widetilde L\) and a local Lie isomorphism \(p:\widetilde L\to L\).

A path lifts uniquely after subdividing it among evenly covered neighborhoods. A homotopy lifts by subdividing its parameter square into finitely many small rectangles whose images lie in such neighborhoods; uniqueness on common edges glues the local lifts. The lifted path \(\alpha\) starting at the identity ends at \([\alpha]\), so \(\widetilde L\) is path connected. If a loop upstairs is based at the identity, its projected loop represents the identity path class because its lift closes. The projected loop therefore has a based null homotopy, whose lift contracts the original loop. Thus \(\widetilde L\) is simply connected.

The kernel \(\Gamma=p^{-1}(1)\) is discrete and is the group of based loop classes. The pointwise multiplication of loops agrees with concatenation up to homotopy: the square map \((s,t)\mapsto\alpha(s)\beta(t)\) carries its diagonal path to the pointwise product, and the path along the bottom and right edges to concatenation when both paths are loops; these paths are homotopic with endpoints fixed in the square. Hence \(\Gamma\cong\pi_1(L)\) as groups.

For \(\gamma\in\Gamma\), the continuous map \(x\mapsto x\gamma x^{-1}\) from the connected group \(\widetilde L\) takes values in the discrete kernel. It is constant, and its value at \(1\) is \(\gamma\). Thus \(\Gamma\) is central and, in particular, abelian.

These statements use only coordinate balls and elementary path/homotopy lifting; they do not assume finiteness of \(\Gamma\) or compactness of \(\widetilde L\).

### 3.3. Closed one-forms and real characters

**Lemma 3.3.** If \(L\) is a compact connected Lie group with perfect Lie algebra \(\mathfrak l=[\mathfrak l,\mathfrak l]\), then every homomorphism \(\pi_1(L)\to(\mathbb R,+)\) is zero.

**Proof.** First construct the averaging measure on \(L\) itself. A positive density at \(1\), translated on the left, gives a smooth positive left-invariant density \(\nu\). Its integral is finite and strictly positive on compact \(L\). Right translation preserves left invariance, so \(R_g^*\nu=c(g)\nu\) for a positive constant. Change of variables on the whole compact group gives \(\int R_g^*\nu=\int\nu\), hence \(c(g)=1\). Dividing by total mass gives a bi-invariant probability density \(d\mu\). This is also the direct Haar-density proof already in Section 5 of this lesson, and requires no representation integration.

Let \(\chi:\Gamma\to\mathbb R\) be a homomorphism, where \(\Gamma=\pi_1(L)\) is the central kernel from the preceding covering construction. We construct a closed one-form whose periods are \(\chi\), rather than invoking a de Rham or Hurewicz isomorphism.

Choose finitely many evenly covered coordinate neighborhoods \(U_i\) and smaller neighborhoods \(W_i\) with closures inside \(U_i\), with the \(W_i\) covering \(L\). Choose a smooth partition of unity \(\phi_i\) with support compactly inside \(U_i\). This uses only finite coordinate balls: choose nonnegative smooth bump functions supported inside the \(U_i\), positive on the \(W_i\), and divide by their everywhere positive sum. Such bumps are obtained from the ordinary smooth function \(\exp(-1/t)\) for \(t>0\), extended by zero.

Choose a sheet, equivalently a smooth local section \(s_i:U_i\to\widetilde L\). For \(x\in p^{-1}(U_i)\), there is a unique \(\gamma_i(x)\in\Gamma\) with
\[
 x=\gamma_i(x)s_i(p(x)).
\]
The function \(\gamma_i\) is locally constant. Define
\[
 f(x)=\sum_i\phi_i(p(x))\chi(\gamma_i(x)).
\]
A summand is zero outside \(p^{-1}(U_i)\); it is smooth there as well because its base support is compactly contained in \(U_i\). Thus \(f\) is smooth. For \(\gamma\in\Gamma\), uniqueness gives \(\gamma_i(\gamma x)=\gamma\gamma_i(x)\), and therefore
\[
 f(\gamma x)=f(x)+\chi(\gamma).
\]
It follows that \(df\) is invariant under the deck transformations and descends to a smooth real one-form \(\alpha\) on \(L\). It is closed because \(p^*(d\alpha)=d(df)=0\) and \(p\) is a local diffeomorphism. If a based loop \(\eta\) lifts from \(1\) to \(\gamma\), then
\[
 \int_\eta\alpha=\int_{\widetilde\eta}df
 =f(\gamma)-f(1)=\chi(\gamma).
 \tag{3.3}
\]

Average this form:
\[
 \overline\alpha=\int_L L_g^*\alpha\,d\mu(g).
\]
Integration of its smooth local coefficients is legitimate on the compact parameter space. Exterior differentiation commutes with this integral, so \(\overline\alpha\) is closed. Since \(L_h^*L_g^*=L_{gh}^*\), right invariance of \(\mu\) makes it left invariant.

Let \(\lambda=\overline\alpha_1\in\mathfrak l^*\). For left-invariant vector fields \(X^L,Y^L\), the formula for the exterior derivative is
\[
 d\overline\alpha(X^L,Y^L)
 =X^L(\overline\alpha(Y^L))
  -Y^L(\overline\alpha(X^L))
  -\overline\alpha([X^L,Y^L])
 =-\lambda([X,Y]).
\]
The first two terms vanish because their coefficient functions are constant. Closedness and perfectness therefore imply \(\lambda=0\), hence \(\overline\alpha=0\).

Finally averaging has not changed any loop period. For each \(g\in L\), choose a piecewise smooth path \(g_s\) from \(1\) to \(g\), possible because a connected manifold is path connected and coordinate paths can be smoothed piecewise. The map \(H(s,t)=g_s\eta(t)\) is a homotopy of closed loops. For a smooth part of this homotopy, coordinate differentiation gives
\[
 \frac{d}{ds}\int_0^1\alpha(H_t)\,dt
 =\alpha(H_s)(s,1)-\alpha(H_s)(s,0)
   +\int_0^1d\alpha(H_s,H_t)\,dt=0.
\]
The boundary terms cancel because the loops close, and the integral vanishes because \(d\alpha=0\). Applying this on finitely many smooth parts proves
\(\int_\eta L_g^*\alpha=\int_\eta\alpha\).
Thus, by integration over \(g\) and (3.3),
\[
 \chi(\gamma)=\int_\eta\alpha
 =\int_\eta\overline\alpha=0.
\]
This proves the lemma without any assertion about the cohomology of arbitrary manifolds. \(\square\)

### 3.4. Finiteness and compactness of the cover

**Theorem 3.4.** If \(L\) is a compact connected Lie group with semisimple Lie algebra, then \(\pi_1(L)\) is finite. Its universal covering Lie group is compact, connected, and simply connected, and has the same Lie algebra.

**Proof.** A semisimple Lie algebra over \(\mathbb R\) is perfect, by the actual proof of RT-LIE-03, Corollary 4.2. Lemma 3.2 and the covering construction make \(\Gamma=\pi_1(L)\) finitely generated and abelian. Lemma 3.3 gives \(\operatorname{Hom}(\Gamma,\mathbb R)=0\).

Here is the elementary algebra concluding finiteness. Write \(\Gamma=\mathbb Z^m/R\). If the rational span of \(R\) were proper in \(\mathbb Q^m\), rational linear algebra would give a nonzero rational linear functional vanishing on \(R\). Its restriction to \(\mathbb Z^m\) would descend to a nonzero map \(\Gamma\to\mathbb Q\subset\mathbb R\), a contradiction. Hence \(R\) spans \(\mathbb Q^m\). Choose \(m\) independent relation vectors in \(R\), and put them in the columns of an integral matrix \(B\). Its determinant \(d\) is nonzero. The adjugate identity \(B\operatorname{adj}(B)=dI\) gives \(d\mathbb Z^m\subset R\). Thus \(\Gamma\) is a quotient of the finite group \((\mathbb Z/d\mathbb Z)^m\). For \(m=0\), it is already trivial.

Therefore \(p:\widetilde L\to L\) has finitely many sheets. To check compactness explicitly, cover \(L\) by finitely many coordinate neighborhoods \(W_i\) whose compact closures lie inside evenly covered neighborhoods \(U_i\). In each of the finitely many sheets over \(U_i\), the inverse image of \(\overline W_i\) is homeomorphic to that compact closure. Their finite union covers \(\widetilde L\), so \(\widetilde L\) is compact. Connectedness, simple connectedness, smooth Lie group structure, and the Lie algebra identification were established in the covering construction. \(\square\)

**Corollary 3.5 (the compact real-form group).** Every compact real form \(\mathfrak u\) of a finite-dimensional complex semisimple algebra is the Lie algebra of a compact connected simply connected Lie group.

**Proof.** The opening construction of this section proves that \(K_{\mathrm{ad}}=\operatorname{Aut}(\mathfrak u)^0\) is compact and connected and that its Lie algebra is \(\operatorname{ad}\mathfrak u\cong\mathfrak u\): its Killing form makes \(\operatorname{Aut}(\mathfrak u)\) a closed subgroup of an orthogonal group; differentiating the bracket equations gives derivations; complexification and innerness of complex derivations give \(\operatorname{Der}(\mathfrak u)=\operatorname{ad}\mathfrak u\); its center is zero. Apply Theorem 3.4 to \(K_{\mathrm{ad}}\). The closed subgroup theorem used to give the automorphism group its Lie group structure remains the basic foundation already declared in the lesson. \(\square\)

For a connected Lie group, exponentials generate the group even when no global surjectivity assertion is used. An exponential chart contains a neighborhood of the identity. The subgroup generated by that neighborhood is open; its cosets are open too, so connectedness forces it to be the whole group. This elementary observation will identify invariant subspaces below.

**Proposition 3.1 (compact Cartan conjugacy for elements).** Every \(X\in\mathfrak u\) is conjugate under \(K\) into \(\mathfrak t=i\mathfrak h_{\mathbb R}\).

**Proof.** Choose \(Y\in\mathfrak t\) with \(\alpha(Y)\ne0\) for every root. Such vectors exist because finitely many proper real hyperplanes cannot cover \(\mathfrak t\). The root decomposition shows that the centralizer of \(Y\) in \(\mathfrak g\) is \(\mathfrak h\), hence its centralizer in \(\mathfrak u\) is \(\mathfrak t\). The real function \(f(k)=\kappa(X,\operatorname{Ad}(k)Y)\) attains an extremum on compact \(K\). At an extremizing \(k\), differentiation along \(k\exp(tZ)\) for arbitrary \(Z\in\mathfrak u\) gives
\[
0=\kappa(\operatorname{Ad}(k^{-1})X,[Z,Y])
=\kappa([Y,\operatorname{Ad}(k^{-1})X],Z).
\]
Nondegeneracy forces the commutator to vanish. Thus \(\operatorname{Ad}(k^{-1})X\in\mathfrak t\). For the zero algebra the assertion is immediate. \(\square\)

This proves the compact Lie-algebra conjugacy statement for elements. It does not require a group-level maximal torus theorem.

## 4. Integrating the action, with its path independence

**Proposition 4.1.** If \(K\) is connected and simply connected, every real-linear Lie algebra representation \(r:\operatorname{Lie}(K)\to\mathfrak{gl}_{\mathbb C}(V)\) integrates uniquely to a smooth representation \(\pi:K\to GL_{\mathbb C}(V)\). Intertwiners and invariant subspaces correspond.

**Proof.** For a piecewise smooth path \(\gamma:[0,1]\to K\) starting at the identity, let \(a(t)\) be its left logarithmic derivative: the tangent vector \(\gamma'(t)\) transported to the identity by left translation. In matrix notation this is \(\gamma^{-1}\gamma'\). Set \(A(t)=r(a(t))\), and solve
\[
U'(t)=U(t)A(t),\qquad U(0)=I. \tag{4.1}
\]
Ordinary finite-dimensional linear ODE theory gives a unique solution. Solving \(W'=-AW\), \(W(0)=I\), shows \((UW)'=0\), so \(U\) is invertible. The definition uses the Maurer–Cartan form of \(K\), not a presumed matrix realization of \(K\).

We verify that the endpoint depends only on the endpoint of the path. In a smooth homotopy \(\gamma(s,t)\) with fixed endpoints, put
\[
A=r(\gamma^{-1}\partial_t\gamma),\qquad
B=r(\gamma^{-1}\partial_s\gamma).
\]
The Maurer–Cartan identity is
\[
\partial_s A-\partial_t B=[A,B]. \tag{4.2}
\]
For matrices it follows immediately by differentiating the inverse and cancelling mixed partial derivatives. Intrinsically, the left Maurer–Cartan form \(\omega\) has \(d\omega(X^L,Y^L)=-[X,Y]\), since \(\omega(X^L)\) and \(\omega(Y^L)\) are constant. Left invariant fields span each tangent space, proving the same identity; applying the Lie homomorphism \(r\) gives (4.2).

Let \(U(s,t)\) solve (4.1), and set \(C=\partial_sU-UB\). Direct differentiation using (4.2) gives
\[
\partial_t C=(\partial_sU)A+U\partial_sA-UAB-U\partial_tB=CA.
\]
At \(t=0\), both \(\partial_sU\) and \(B\) vanish. Uniqueness implies \(C=0\). At \(t=1\), \(B=0\) because the endpoint is fixed, so \(\partial_sU(s,1)=0\). Thus the endpoint is unchanged under homotopy. The same argument applies piecewise; the elementary smoothing theorem for paths and homotopies in a manifold lets one use piecewise smooth representatives. Simple connectedness makes any two paths with the same endpoints homotopic relative endpoints.

Define \(\pi(g)=U_\gamma(1)\) for any path to \(g\). Concatenate a path to \(g\) with the left translate by \(g\) of a path to \(h\). The second path has the same left logarithmic derivative as the original path to \(h\), and its ODE starts at \(\pi(g)\). Hence
\[
\pi(gh)=\pi(g)\pi(h),\qquad
\pi(\exp X)=\exp r(X). \tag{4.3}
\]
The second identity and a local exponential chart show smoothness near the identity; the first then shows it everywhere. Differentiation gives \(d\pi=r\). Any other integrating representation agrees along every path by (4.1), proving uniqueness.

If a complex-linear map intertwines the Lie algebra actions, it intertwines their ODE solutions, hence the group actions. Conversely, differentiate a group intertwiner. A subspace invariant under the Lie algebra is preserved by its exponentials and therefore by the connected group. The converse again follows by differentiation. \(\square\)

This is the representation version of Lie integration, proved here. Kirillov, Theorem 3.41, pp. 40–41, gives the general Lie homomorphism theorem by a different route.

Simple connectedness matters. The natural two-dimensional \(\mathfrak{su}(2)\)-action integrates to \(SU(2)\); it does not descend to \(SO(3)=SU(2)/\{\pm I\}\), because \(-I\) acts as \(-I\). The covering relation is described in Kirillov, §3.10, pp. 44–45. Averaging over an adjoint quotient would therefore be unavailable for this representation.

## 5. Averaging and complete reducibility

We construct the integration used in averaging. Choose a positive density at the identity of the compact Lie group \(K\) and extend it by left translations. This gives a smooth positive left invariant density \(d\nu\), with finite positive total mass. A density permits integration without choosing an orientation. Right translation \(R_g\) commutes with all left translations, so \(R_g^*d\nu=c(g)d\nu\) for some positive scalar: a left invariant density is determined by its value at the identity, where its space is one-dimensional. The scalar \(c(g)\) varies continuously and is multiplicative. Its image is a compact subgroup of \(\mathbb R_{>0}\). Taking logarithms gives a compact additive subgroup of \(\mathbb R\), which must be zero, since a nonzero element has unbounded integer multiples. Therefore \(c(g)=1\).

After dividing by the total mass we obtain a positive integration density \(dk\) with
\[
\int_K dk=1,\qquad
\int_K f(gk)\,dk=\int_K f(kg)\,dk=\int_K f(k)\,dk. \tag{5.1}
\]
This is normalized Haar integration for a compact Lie group. Kirillov, Theorems 4.34 and 4.36, pp. 56–57, give its volume-form and measure formulations. Only integration of continuous finite-dimensional matrix coefficients is needed here.

**Theorem 5.1 (Weyl's unitary trick).** Restriction, integration, and differentiation give equivalent categories of finite-dimensional complex \(\mathfrak g\)-modules, real-linear \(\mathfrak u\)-actions on complex spaces, and smooth finite-dimensional complex representations of \(K\). Every such representation admits a positive definite \(K\)-invariant Hermitian form. Every finite-dimensional complex \(\mathfrak g\)-module is completely reducible.

**Proof.** The categorical assertions follow from (1.3) and Proposition 4.1, including their statements about intertwiners. Choose any positive definite Hermitian form \(H_0\) on \(V\), linear in its first argument. Define
\[
H(v,w)=\int_K H_0(\pi(k)v,\pi(k)w)\,dk. \tag{5.2}
\]
The coefficients are continuous, so the integral exists. It is Hermitian and sesquilinear. For \(v\ne0\), invertibility of \(\pi(k)\) makes the integrand on the diagonal strictly positive; its continuous minimum on compact \(K\) is positive. Thus \(H(v,v)>0\). Right invariance in (5.1) gives \(H(\pi(g)v,\pi(g)w)=H(v,w)\).

If \(W\subset V\) is a complex \(\mathfrak g\)-submodule, it is \(\mathfrak u\)-invariant and hence \(K\)-invariant. For \(v\in W^\perp\), \(w\in W\),
\[
H(\pi(g)v,w)=H(v,\pi(g^{-1})w)=0.
\]
So \(W^\perp\) is \(K\)-invariant, then \(\mathfrak u\)-invariant by differentiation, then \(\mathfrak g\)-invariant by complex extension. We have \(V=W\oplus W^\perp\). Induction on dimension decomposes \(V\) into irreducibles, starting with the zero space and with an irreducible nonzero space. \(\square\)

Differentiating invariance gives
\[
H(r(X)v,w)+H(v,r(X)w)=0\qquad(X\in\mathfrak u). \tag{5.3}
\]
Thus the compact real algebra acts by skew-Hermitian operators. The operators \(\rho(iX)=i r(X)\) generally do not. The averaged form proves complete reducibility of the complex algebra through its invariant subspaces.

The assertion concerns finite-dimensional representations. An infinite-dimensional unitary representation of a compact group need not be finite-dimensional, and a noncompact group may have finite-dimensional unitary representations. Neither stronger assertion is used.

## 6. Classical compact forms

Write \(X^*=\overline X^{\mathsf T}\) and
\(J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}\).

**Proposition 6.1.** The real algebras
\[
\begin{aligned}
\mathfrak{su}(n)&=\{X\in\mathfrak{sl}_n(\mathbb C):X^*=-X\},\\
\mathfrak{so}(N)&=\{X\in M_N(\mathbb R):X^{\mathsf T}=-X\},\\
\mathfrak{sp}(n)&=\{X\in M_{2n}(\mathbb C):X^{\mathsf T}J+JX=0,\ X^*=-X\}
\end{aligned} \tag{6.1}
\]
are compact real forms of \(\mathfrak{sl}_n(\mathbb C)\), \(\mathfrak{so}_N(\mathbb C)\), and \(\mathfrak{sp}_{2n}(\mathbb C)\), respectively. Their semisimple ranges are \(n\ge2\), \(N\ge3\), and \(n\ge1\).

**Proof.** On \(\mathfrak{sl}_n(\mathbb C)\), \(\sigma X=-X^*\) is a conjugate-linear bracket automorphism and squares to one. Its fixed algebra is \(\mathfrak{su}(n)\). Entrywise conjugation on the complex skew-symmetric matrices has fixed algebra \(\mathfrak{so}(N)\). Lemma 1.1 supplies both complexifications.

A complex symplectic matrix has the block form
\[
X=\begin{pmatrix}A&B\\C&-A^{\mathsf T}\end{pmatrix},
\qquad B^{\mathsf T}=B,\quad C^{\mathsf T}=C.
\]
The map \(-X^*\) preserves this block condition and is again a conjugate-linear bracket involution. Its fixed algebra is
\[
\mathfrak{sp}(n)=
\left\{\begin{pmatrix}A&B\\-\overline B&\overline A\end{pmatrix}:
A^*=-A,\ B^{\mathsf T}=B\right\}. \tag{6.2}
\]
The diagonal block contributes \(n^2\) real parameters and the symmetric complex block contributes \(n(n+1)\). Thus its real dimension is \(n(2n+1)\), as required. The other dimensions are \(n^2-1\) and \(N(N-1)/2\).

These are the tangent algebras of the closed bounded matrix groups \(SU(n)\), \(SO(N)\), and \(Sp(n)=U(2n)\cap\{Q:Q^{\mathsf T}JQ=J\}\); hence these groups are compact. To verify the Killing sign directly, on any of the real algebras in (6.1) use
\[
\langle Y,Z\rangle=\operatorname{Re}\operatorname{Tr}(YZ^*).
\]
For skew-Hermitian \(X\), cycling traces gives
\(\langle[X,Y],Z\rangle=-\langle Y,[X,Z]\rangle\). Thus \(\operatorname{ad}X\) is a real skew-adjoint operator. In an orthonormal basis \(E_j\),
\[
\kappa(X,X)=\operatorname{Tr}_{\mathbb R}((\operatorname{ad}X)^2)
=-\sum_j\|[X,E_j]\|^2. \tag{6.3}
\]
It is strictly negative for nonzero \(X\), since the center is zero: a central real vector would be central in the semisimple complexification verified in the classical-model lesson. This proves the assertion. \(\square\)

The boundary \(\mathfrak{so}(2)\) is an abelian compact real form of its one-dimensional complexification; its Killing form is zero. Its group \(SO(2)\) has infinite fundamental group and a noncompact universal cover. Semisimplicity is essential in Weyl's compact-cover theorem. The zero algebra poses no difficulty; its simply connected group is the trivial group.

For later use, \(SU(n)\) is connected and simply connected. Here is the topological argument. For \(n\ge2\), the first-column map
\[
SU(n)\longrightarrow S^{2n-1}
\]
has fiber \(SU(n-1)\). It is onto: complete a unit column to a unitary basis, then multiply the last column by the inverse determinant without changing the first. The same Gram–Schmidt construction near any chosen column gives local smooth sections, and hence a locally trivial fiber bundle. Starting from \(SU(1)=\{1\}\), connectedness follows by path lifting and connectedness of the fiber. The homotopy exact sequence contains
\[
\pi_1(SU(n-1))\longrightarrow\pi_1(SU(n))
\longrightarrow\pi_1(S^{2n-1}).
\]
Both outside groups vanish by induction and simple connectedness of spheres of dimension at least two, so the middle group vanishes. For \(n=2\), one can also see \(SU(2)\simeq S^3\) from
\(\begin{pmatrix}a&-\overline b\\b&\overline a\end{pmatrix}\), \(|a|^2+|b|^2=1\). The fiber-bundle homotopy facts are the elementary inputs stated in Kirillov, Theorem 2.11 and Corollary 2.12, pp. 16–17.

## 7. Noncompact forms and the Lorentz example

For \(p+q=n\), set \(S=\operatorname{diag}(I_p,-I_q)\). The conjugation \(\sigma X=-S X^* S\) on \(\mathfrak{sl}_n(\mathbb C)\) fixes
\[
\mathfrak{su}(p,q)=\{X:X^*S+SX=0,\ \operatorname{Tr}X=0\}. \tag{7.1}
\]
It is a real form by Lemma 1.1. Its matrices are
\[
X=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},
\quad A^*=-A,\quad D^*=-D,\quad \operatorname{Tr}A+\operatorname{Tr}D=0.
\]
The block diagonal part is trace-orthogonal to the off-diagonal part. The former contributes \(p^2+q^2-1\) negative directions to \(\kappa(X,X)=2n\operatorname{Tr}(X^2)\); the latter contributes \(2pq\) positive directions, since its squared trace is \(2\operatorname{Tr}(BB^*)\). Thus
\[
\operatorname{sig}\kappa_{\mathfrak{su}(p,q)}
=(2pq,\ p^2+q^2-1). \tag{7.2}
\]
For \(p,q>0\), choosing one positive and one negative coordinate gives \(X\) with a block \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Its exponential has entries \(\cosh t,\sinh t\), giving an unbounded one-parameter subgroup of \(SU(p,q)\). When \(p=0\) or \(q=0\), the form is compact.

Similarly,
\[
\mathfrak{so}(p,q)=\{X\in M_{p+q}(\mathbb R):X^{\mathsf T}S+SX=0\}
=\left\{\begin{pmatrix}A&B\\B^{\mathsf T}&D\end{pmatrix}:A^{\mathsf T}=-A,\ D^{\mathsf T}=-D\right\}. \tag{7.3}
\]
Over \(\mathbb C\), take \(T=\operatorname{diag}(I_p,iI_q)\), so \(T^{\mathsf T}ST=I\). The map \(X\mapsto T^{-1}XT\) identifies the complexification with \(\mathfrak{so}_{p+q}(\mathbb C)\). For \(p,q>0\) its real matrix group has the same hyperbolic two-coordinate subgroup and is noncompact. For \(p+q\ge3\), the Killing form is \((p+q-2)\operatorname{Tr}(XY)\), so its signature is
\[
\left(pq,\ \frac{p(p-1)}2+\frac{q(q-1)}2\right). \tag{7.4}
\]
Here is a derivation of the trace constant, with \(N=p+q\). On the complex standard space, \(v\wedge w\mapsto vw^{\mathsf T}-wv^{\mathsf T}\) identifies \(\Lambda^2\mathbb C^N\) with the skew matrices and intertwines the induced action with the adjoint action. Write \(T_X=X\otimes I+I\otimes X\), and let \(P\) exchange tensor factors. The alternating projector is \((I-P)/2\). In a tensor basis, \(\operatorname{Tr}(P(A\otimes B))=\operatorname{Tr}(AB)\), because its diagonal coefficient at \(e_i\otimes e_j\) is \(A_{ji}B_{ij}\). Therefore
\[
\operatorname{Tr}(T_XT_Y)=2N\operatorname{Tr}(XY)+2\operatorname{Tr}X\operatorname{Tr}Y,
\qquad \operatorname{Tr}(PT_XT_Y)=4\operatorname{Tr}(XY).
\]
Their half difference is \((N-2)\operatorname{Tr}(XY)+\operatorname{Tr}X\operatorname{Tr}Y\); the last term vanishes. Formula (7.3) then gives the positive and negative counts. For \(N=2\) the algebra is abelian and the Killing form vanishes.

For \(\mathfrak{sl}_n(\mathbb R)\), symmetric traceless matrices are positive and skew-symmetric matrices negative for \(2n\operatorname{Tr}(X^2)\); these subspaces are orthogonal. Hence
\[
\operatorname{sig}\kappa_{\mathfrak{sl}_n(\mathbb R)}
=\left(\frac{n(n+1)}2-1,\ \frac{n(n-1)}2\right),
\qquad
\operatorname{sig}\kappa_{\mathfrak{su}(n)}=(0,n^2-1). \tag{7.5}
\]
In particular \(\mathfrak{sl}_2(\mathbb R)\) and \(\mathfrak{su}(1,1)\) have signature \((2,1)\), whereas \(\mathfrak{su}(2)\) has signature \((0,3)\).

**Proposition 7.1 (Lorentz algebra).** There is an isomorphism of **real** Lie algebras
\[
\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\simeq\mathfrak{so}(3,1). \tag{7.6}
\]
The subscript means that complex scalar multiplication is forgotten.

**Proof.** The real space of Hermitian \(2\times2\) matrices has coordinates
\[
H=\begin{pmatrix}t+z&x-iy\\x+iy&t-z\end{pmatrix},
\qquad\det H=t^2-x^2-y^2-z^2. \tag{7.7}
\]
For \(A\in SL_2(\mathbb C)\), the real-linear transformation \(H\mapsto AHA^*\) preserves this determinant. Differentiating gives the real-linear map
\[
\varphi(X)H=XH+HX^*.
\]
It preserves the infinitesimal quadratic form, so it lands in \(\mathfrak{so}(1,3)\). Direct expansion gives \([\varphi(X),\varphi(Y)]=\varphi([X,Y])\); the right-multiplication terms combine as \(H(Y^*X^*-X^*Y^*)=H[X,Y]^*\).

If \(\varphi(X)=0\), applying it to \(H=I\) gives \(X^*=-X\). Applying it to every Hermitian \(H\) then says \([X,H]=0\). Commuting with the real diagonal matrices forces \(X\) to be diagonal; commuting with \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) makes its diagonal entries equal. Trace zero gives \(X=0\). Both real dimensions are six, so \(\varphi\) is an isomorphism. Multiplying the quadratic form by \(-1\) and reordering coordinates identifies \(\mathfrak{so}(1,3)\) with \(\mathfrak{so}(3,1)\). \(\square\)

This six-dimensional real algebra is not a real form of the three-dimensional complex algebra \(\mathfrak{sl}_2(\mathbb C)\). Its complexification is a pair of copies:
\[
\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\otimes_{\mathbb R}\mathbb C
\simeq\mathfrak{sl}_2(\mathbb C)\oplus\mathfrak{sl}_2(\mathbb C). \tag{7.8}
\]
To verify this, extend the real homomorphism \(X\mapsto(X,\overline X)\) complex-linearly. The images of \(X\) and \(iX\) span \((X,0)\) and \((0,\overline X)\); the dimensions agree. This explains the two complex simple factors behind Lorentz highest-weight notation without confusing the ground fields.

## 8. Cartan involutions and the classification pointer

For a real semisimple algebra \(\mathfrak g_0\), a **Cartan involution** is a real Lie automorphism \(\theta\) with \(\theta^2=1\) such that
\[
B_\theta(X,Y)=-\kappa(X,\theta Y)
\]
is positive definite. Its eigenspaces give \(\mathfrak g_0=\mathfrak k\oplus\mathfrak p\), for eigenvalues \(+1\) and \(-1\). Since \(\theta\) is an automorphism,
\[
[\mathfrak k,\mathfrak k]\subset\mathfrak k,\qquad
[\mathfrak k,\mathfrak p]\subset\mathfrak p,\qquad
[\mathfrak p,\mathfrak p]\subset\mathfrak k. \tag{8.1}
\]
Automorphisms preserve \(\kappa\); opposite eigenspaces are therefore orthogonal. It follows from positivity of \(B_\theta\) that \(\kappa\) is negative on \(\mathfrak k\) and positive on \(\mathfrak p\).

In the matrix examples, \(\theta X=-X^{\mathsf T}\) on \(\mathfrak{sl}_n(\mathbb R)\) and \(\mathfrak{so}(p,q)\), and \(\theta X=-X^*\) on \(\mathfrak{su}(p,q)\), have these properties. The block formulas verify that they preserve the respective algebras. Their associated forms are respectively \(2n\operatorname{Tr}(XX^{\mathsf T})\), \((p+q-2)\operatorname{Tr}(XX^{\mathsf T})\), and \(2n\operatorname{Tr}(XX^*)\) on the diagonal, hence positive in the semisimple ranges. On a compact form, \(\theta=1\) works. These arguments establish the decompositions in these examples; general existence of Cartan involutions is not needed in the unitary-trick proof.

Throughout, \(\mathfrak g\) is a finite-dimensional complex semisimple Lie algebra with compact conjugation \(\sigma\), compact form \(\mathfrak u\), and positive Hermitian form
\[
 H(x,y)=-\kappa(x,\sigma y).
\]
Sections 2–3 supply the sign-compatible compact form and compact automorphism group used below.

### 8.1. Adjoint and spectral identities

For any complex Lie automorphism \(x\), invariance of the Killing form gives
\[
 x^\dagger=\sigma x^{-1}\sigma. \tag{8.2}
\]
Indeed \(H(xv,w)=H(v,\sigma x^{-1}\sigma w)\). In particular \(x^\dagger\) is itself a complex Lie automorphism.

If a self-adjoint automorphism \(A\) has real nonzero eigenvalues, put \(P=|A|\), acting on \(E_\lambda(A)\) by \(|\lambda|\). Because \([E_\lambda,E_\mu]\subset E_{\lambda\mu}\), every \(P^t\) preserves brackets: absolute values are multiplicative and positive real powers multiply. Its inverse is \(P^{-t}\), and its continuous path from the identity makes it inner by Lemma 2.2. Also \(\theta=AP^{-1}\) preserves brackets, has eigenvalues \(+1,-1\), and satisfies \(\theta^2=1\).

These are statements about finite spectral decompositions. No polar decomposition theorem for Lie groups is being assumed.

### 8.2. Every real form has a Cartan involution

**Theorem 8.1 (Cartan-involution existence).** Every conjugate-linear Lie involution \(\rho\) of \(\mathfrak g\) is conjugate by an inner automorphism to \(\theta\sigma\), where \(\theta\) is a complex Lie involution commuting with \(\sigma\). The restriction of \(\theta\) to \(\mathfrak u\) is a real Lie automorphism.

**Proof.** Put \(A=\sigma\rho\). It is a complex Lie automorphism and
\[
 \sigma A\sigma=A^{-1}.
\]
By (8.2), \(A^\dagger=\sigma A^{-1}\sigma=A\). Hence it is diagonalizable with real nonzero eigenvalues. Set \(P=|A|\) and \(\theta=AP^{-1}\) as above. Since \(\sigma\) sends the \(A\)-eigenspace with eigenvalue \(\lambda\) to the one with eigenvalue \(\lambda^{-1}\),
\[
 \sigma P^t\sigma=P^{-t},\qquad
 \sigma\theta\sigma=\theta.
\]
Thus \(\theta\) commutes with \(\sigma\) and preserves its fixed compact form. For \(b=P^{1/2}\), which is inner, use \(\rho=\sigma A=\theta P^{-1}\sigma\) to obtain
\[
 b\rho b^{-1}
 =P^{1/2}\theta P^{-1}\sigma P^{-1/2}
 =\theta\sigma.
\]
This proves the reduction. \(\square\)

Write the eigenspaces of \(\theta\) in \(\mathfrak u\) as \(\mathfrak u_+\oplus\mathfrak u_-\). The fixed real form of \(\theta\sigma\) is
\[
 \mathfrak v_\theta=\mathfrak u_+\oplus i\mathfrak u_-.
 \tag{8.3}
\]
The summands are Killing-orthogonal because \(\theta\) preserves \(\kappa\). On this real form, \(\theta\) acts by \(+1\) on \(\mathfrak u_+\) and by \(-1\) on \(i\mathfrak u_-\), and
\[
 B_\theta(X,Y)=-\kappa(X,\theta Y)
\]
is positive definite: on the first summand it is \(-\kappa\), and for \(X=ix,Y=iy\), \(x,y\in\mathfrak u_-\), it is \(-\kappa(x,y)\). Therefore its transported involution on the original real form is a Cartan involution in exactly the convention of this section.

### 8.3. Exact isomorphism criterion

**Theorem 8.2 (real forms and compact involutions).** The real forms of \(\mathfrak g\), up to real Lie algebra isomorphism, are in bijection with the \(\operatorname{Aut}(\mathfrak u)\)-conjugacy classes of involutions of \(\mathfrak u\).

**Proof.** A real isomorphism extends uniquely by complex linearity to an automorphism of \(\mathfrak g\), and conversely an automorphism intertwining the two conjugations restricts to a real isomorphism. Thus, after Theorem 8.1, isomorphism is exactly the existence of a complex automorphism \(x\) with
\[
 x\theta\sigma x^{-1}=\theta'\sigma.
\]
Using (8.2), this is equivalent to
\[
 \theta'=x\theta x^\dagger. \tag{8.4}
\]
Set \(Z=x^\dagger x\), a positive self-adjoint Lie automorphism. Since \((\theta')^2=1\), equation (8.4) gives
\[
 \theta Z\theta=Z^{-1},\qquad
 \theta Z^t\theta=Z^{-t}.
\]
The second equation follows on the positive real spectral decomposition. Put \(y=xZ^{-1/2}\), an automorphism by Section 8.1. It satisfies \(y^\dagger y=1\), so (8.2) gives \(\sigma y\sigma=y\); hence \(y\) restricts to \(\operatorname{Aut}(\mathfrak u)\). Moreover,
\[
 y\theta y^{-1}
 =xZ^{-1/2}\theta Z^{1/2}x^{-1}
 =x\theta Zx^{-1}=x\theta x^\dagger=\theta'.
\]
Conversely, an automorphism of \(\mathfrak u\) extends complex linearly, commutes with \(\sigma\), and an ordinary conjugacy \(y\theta y^{-1}=\theta'\) intertwines \(\theta\sigma\) and \(\theta'\sigma\). Together with Theorem 8.1 this proves the bijection. The proof includes arbitrary semisimple products and the zero algebra. \(\square\)

For product bookkeeping, an involution permutes the simple ideals in cycles of length one or two. A paired cycle must consist of isomorphic ideals, and its two component maps are inverse to each other. Conjugating by component isomorphisms makes that action the plain exchange \((x,y)\mapsto(y,x)\). Its real form is
\[
 \{(z,\sigma z):z\in\mathfrak g_i\},
\]
which is isomorphic to the complex simple algebra \(\mathfrak g_i\) viewed as a real algebra. Fixed simple ideals carry individual involutions of their compact form. Thus component exchanges must be included in any general semisimple Satake statement; restricting to simple complexifications omits real simple algebras of complex type.

### 8.4. Maximal abelian split subspaces and an adapted Cartan

**Proposition 8.3.** All maximal abelian subspaces of \(\mathfrak p\) are conjugate under the compact connected group with Lie algebra \(\operatorname{ad}\mathfrak k\). Each extends to a Cartan subalgebra \(\mathfrak t_{\mathbb C}\oplus\mathfrak a_{\mathbb C}\), with \(\mathfrak t\subset\mathfrak k\).

**Proof.**

Put \(\mathfrak k=\mathfrak u_+\) and \(\mathfrak p=i\mathfrak u_-\), so \(\mathfrak v_\theta=\mathfrak k\oplus\mathfrak p\). Let \(K_\theta\) be the identity component of the closed centralizer of \(\theta\) in \(\operatorname{Aut}(\mathfrak u)^0\). This is compact, and its Lie algebra is \(\operatorname{ad}\mathfrak k\): differentiating commutation with \(\theta\) gives \(\theta X=X\) because the adjoint map is injective. Thus it acts on \(\mathfrak p\).

Choose a maximal abelian subspace \(\mathfrak a\subset\mathfrak p\). For \(X\in\mathfrak u\), invariance of \(\kappa\) and \(\sigma X=X\) give \(H([X,v],w)=-H(v,[X,w])\), so \(\operatorname{ad}X\) is skew-adjoint; multiplication by \(i\) makes it self-adjoint. Thus elements of \(\mathfrak a\) have commuting self-adjoint adjoint operators. Simultaneous Hermitian diagonalization gives finitely many real joint weights on \(\mathfrak a\). Choose \(a_0\in\mathfrak a\) outside the hyperplanes of their nonzero weights. Then
\[
 Z_{\mathfrak p}(a_0)=Z_{\mathfrak p}(\mathfrak a)=\mathfrak a.
 \tag{8.5}
\]
The second equality follows by maximality: any \(p\in\mathfrak p\) commuting with \(\mathfrak a\) could otherwise be adjoined to it.

For any \(p\in\mathfrak p\), maximize the real continuous function
\[
 f(k)=\kappa(\operatorname{Ad}(k)p,a_0)
\]
on compact \(K_\theta\). At a maximum, putting \(p_0=\operatorname{Ad}(k)p\), differentiation along \(X\in\mathfrak k\) gives
\[
 0=\kappa([X,p_0],a_0)=\kappa(X,[p_0,a_0]).
\]
Since \([\mathfrak p,\mathfrak p]\subset\mathfrak k\) and \(\kappa\) is negative definite on \(\mathfrak k\), this forces \([p_0,a_0]=0\). By (8.5), \(p_0\in\mathfrak a\).

If \(\mathfrak a'\) is another maximal abelian subspace, choose a generic \(a'_0\) with \(Z_{\mathfrak p}(a'_0)=\mathfrak a'\), and send \(a'_0\) into \(\mathfrak a\) by the preceding argument. Then \(\mathfrak a\subset Z_{\mathfrak p}(\operatorname{Ad}(k)a'_0)=\operatorname{Ad}(k)\mathfrak a'\). Maximal abelianness forces equality. All maximal abelian subspaces of \(\mathfrak p\) are therefore \(K_\theta\)-conjugate.

Let \(\mathfrak m=Z_{\mathfrak k}(\mathfrak a)\), and choose a maximal abelian subalgebra \(\mathfrak t\subset\mathfrak m\). Because all its adjoint operators are skew-adjoint, it is toral. The commuting normal operators from \(\mathfrak t\) and \(\mathfrak a\) are simultaneously diagonalizable. Their common centralizer in the real form is \(\mathfrak t\oplus\mathfrak a\): a centralizing vector splits into a \(\mathfrak k\)-part in \(Z_{\mathfrak m}(\mathfrak t)=\mathfrak t\) and a \(\mathfrak p\)-part in \(Z_{\mathfrak p}(\mathfrak a)=\mathfrak a\). Complexification gives
\[
 Z_{\mathfrak g}(\mathfrak t_{\mathbb C}\oplus\mathfrak a_{\mathbb C})
 =\mathfrak t_{\mathbb C}\oplus\mathfrak a_{\mathbb C}.
\]
Thus \(\mathfrak h=\mathfrak t_{\mathbb C}\oplus\mathfrak a_{\mathbb C}\) is a self-centralizing toral, hence Cartan, subalgebra in the standard semisimple Cartan convention already used in Lessons 07 and 10.

The split subalgebra \(\mathfrak a\) is also maximal under inclusion among real toral subalgebras whose adjoint operators have real spectrum. Indeed \(Z_{\mathfrak v_\theta}(\mathfrak a)=\mathfrak m\oplus\mathfrak a\). Write a commuting candidate as \(Y=M+A\) in this sum. The operators \(\operatorname{ad}M\) and \(\operatorname{ad}A\) commute and are respectively skew-adjoint and self-adjoint for \(H\). Simultaneous normal diagonalization shows that their eigenvalues are respectively purely imaginary and real. If \(\operatorname{ad}Y\) has only real eigenvalues, all the imaginary eigenvalues of \(\operatorname{ad}M\) vanish. Hence \(\operatorname{ad}M=0\); the centre of \(\mathfrak g\) is zero, so \(M=0\). Thus any such extension is already in \(\mathfrak a\). The conjugacy proved above concerns maximal abelian subspaces of \(\mathfrak p\); it does not assert conjugacy of arbitrary real Cartan subalgebras. \(\square\)

### 8.5. Satake diagrams and their complete classification

**Theorem 8.4.** Finite-dimensional real semisimple Lie algebras, up to real Lie algebra isomorphism, correspond bijectively to admissible finite Satake diagrams, up to isomorphism of directed decorated Dynkin diagrams. Disconnected diagrams and arrows exchanging isomorphic components are allowed. The underlying complex Dynkin diagram is the diagram of the complexification. Admissibility is the explicit condition in Definition 8.4 below, including its parity obstruction; it is not defined by existence of a real form.

#### 8.5.1. Exact root-data criterion

We use the column-coroot convention
\[
a_{ij}=\alpha_i(h_j),\qquad h_j=\alpha_j^\vee.
\tag{8.6}
\]
Let \(I\) be the vertex set of a finite-type Cartan matrix \(A\); empty and disconnected matrices are allowed. An automorphism of its directed Dynkin diagram means a permutation \(\tau\) satisfying \(a_{\tau(i),\tau(j)}=a_{ij}\) for every \(i,j\).

For \(X\subseteq I\), let \(\Phi_X=\Phi\cap\sum_{j\in X}\mathbb Z\alpha_j\) be the root subsystem with simple roots indexed by \(X\), \(W_X=\langle s_j:j\in X\rangle\), and \(w_X\) its longest element. Put
\[
\rho_X^\vee=\frac12\sum_{\beta\in\Phi_X^+}\beta^\vee,\qquad
H_X=2\rho_X^\vee=\sum_{j\in X}c_jh_j.
\tag{8.7}
\]
The subsystem assertion follows directly from the axioms: reflection in a root of the real span of \(X\) preserves that span and the full root set, and all the other axioms restrict to it. The same-sign simple expansions have zero coefficients outside \(X\), so \(X\) is its base. In particular the complete results of RT-LIE-08 apply to it, and \(A_X\) is nonsingular by positive definiteness of its simple-root Gram matrix. Its coroots form the dual root system: reflection preserves them, and its Cartan integers are the transposed integral Cartan integers. Use the same positive halfspace, since a coroot is a positive scalar multiple of its root. Every \(h_j\) is indecomposable among positive coroots: a decomposition would have only its one simple-root direction in each summand, and reducedness would force both summands to be \(h_j\), which cannot sum to \(h_j\). The positive-halfspace base theorem in RT-LIE-08 gives exactly \(|X|\) indecomposable roots in the dual system. Thus these independent \(h_j\) exhaust that base, and the same theorem gives the integral same-sign simple-coroot expansions.

The \(c_j\) are positive integers when \(X\ne\varnothing\): positive coroots have nonnegative integral simple-coroot coordinates, and each simple coroot occurs in the sum. For \(j\in X\), a simple reflection permutes positive coroots except its own, so \(s_j\rho_X^\vee=\rho_X^\vee-h_j\); comparison with \(s_jH=H-\alpha_j(H)h_j\) gives
\[
\alpha_j(\rho_X^\vee)=1,\qquad
\sum_{\ell\in X}a_{j\ell}c_\ell=2.
\tag{8.8}
\]
Thus the finite integers \(c_j\) can be calculated exactly from \(A_Xc=2\mathbf1\). The longest element is an involution, by RT-LIE-08 Theorem 5.1. The root map \(-w_X\) preserves positive roots and their indecomposability, so permutes the simple roots of \(\Phi_X\); this is its opposition permutation.

**Definition 8.4.** A pair \((X,\tau)\) is admissible if:

1. \(\tau\) is a directed Dynkin automorphism, \(\tau^2=1\), and \(\tau(X)=X\).
2. \(w_X\alpha_j=-\alpha_{\tau(j)}\) for every \(j\in X\).
3. If \(i\notin X\) and \(\tau(i)=i\), then
\[
\alpha_i(\rho_X^\vee)\in\mathbb Z,
\quad\text{equivalently}\quad
\sum_{j\in X}a_{ij}c_j\in2\mathbb Z.
\tag{8.9}
\]

Paint \(X\) black. Paint its complement white, joining each two-element orbit of \(\tau\) on that complement by an arrow. The action on black vertices is already forced by opposition and is not separately drawn. This is the admissible Satake diagram of the pair. An isomorphism of pairs is a directed Dynkin isomorphism \(f\) with \(f(X)=X'\) and \(f\tau=\tau'f\). This is exactly an isomorphism of the decorated diagrams, since the hidden black action is determined by the black root subsystem.

The choices \(X=I,\tau=-w_I\) are included; they will give the compact forms. For \(X=\varnothing\), take \(H_X=0,w_X=1\), so condition (3) is empty. For the empty matrix there is just the empty pair.

#### 8.5.2. Compact and split-Cartan normalization

Fix the complex semisimple algebra \(\mathfrak g\) with its sign-compatible generators \(e_i,f_i,h_i\) and compact conjugation
\[
c(h_i)=-h_i,\qquad c(e_i)=-f_i,\qquad c(f_i)=-e_i.
\tag{8.10}
\]
The map \(c\) is conjugate-linear. Its compact fixed form is \(\mathfrak u\). Here \(\omega\) denotes instead the complex-linear Chevalley involution with the same values on generators. The real Serre relations show directly that \(\omega\) is a Lie automorphism and commutes with \(c\). A pinned diagram automorphism \(\widehat\tau\) permutes all three sorts of generators and commutes with both.

Let \(\theta\) be a complex-linear involution commuting with \(c\), equivalently an involution of \(\mathfrak u\). Put
\[
\mathfrak g_0=\mathfrak g^{\theta c}
=\mathfrak k\oplus\mathfrak p,\qquad
\mathfrak k=\mathfrak u_+,\quad
\mathfrak p=i\mathfrak u_-.
\tag{8.11}
\]
Theorems 8.1–8.2 prove that every real form occurs and that real isomorphism is exactly conjugacy of \(\theta\) under \(\operatorname{Aut}(\mathfrak u)\). Theorem 8.1 proves positivity of \(B_\theta(x,y)=-\kappa(x,\theta y)\). Proposition 8.3 proves that maximal abelian subspaces \(\mathfrak a\subset\mathfrak p\) are conjugate under
\[
K_\theta=Z_{\operatorname{Aut}(\mathfrak u)^0}(\theta)^0,
\qquad \operatorname{Lie}K_\theta=\operatorname{ad}\mathfrak k,
\]
and constructs the Cartan subalgebra
\[
\mathfrak h=\mathfrak t_{\mathbb C}\oplus\mathfrak a_{\mathbb C},
\qquad
\mathfrak t\text{ maximal abelian in }
\mathfrak m=Z_{\mathfrak k}(\mathfrak a).
\tag{8.12}
\]
Here and below “maximally split” means this explicit construction, with \(\mathfrak a\) maximal abelian in \(\mathfrak p\); no unproved conjugacy of real tori is imported.

We supply the further normalization facts needed to make the diagram independent of choices.

**Lemma 8.5.** For fixed \(\mathfrak a\), all the choices of \(\mathfrak t\) in (8.12) are conjugate under \(Z_{K_\theta}(\mathfrak a)^0\). Every compact Cartan subalgebra of \(\mathfrak u\) is conjugate to the fixed compact Cartan under \(\operatorname{Aut}(\mathfrak u)^0\).

**Proof.** More generally, let a compact group \(M\) act on a compact Lie subalgebra \(\mathfrak l\subseteq\mathfrak u\), with Lie algebra of the action \(\operatorname{ad}\mathfrak l\). On \(\mathfrak l\) the form \(b=-\kappa\) is positive definite and invariant. For a maximal abelian subalgebra \(\mathfrak t\subset\mathfrak l\), its commuting skew-adjoint adjoint operators are simultaneously diagonalizable over \(\mathbb C\). A generic \(T\in\mathfrak t\) avoids their finitely many nonzero weight hyperplanes and has
\[
Z_{\mathfrak l}(T)=Z_{\mathfrak l}(\mathfrak t)=\mathfrak t.
\]
The last equality is just maximal abelianness. For any \(Y\in\mathfrak l\), maximize \(b(\operatorname{Ad}(m)Y,T)\) on compact \(M\). The derivative for every \(Z\in\mathfrak l\) is
\[
0=b([Z,Y_0],T)=b(Z,[Y_0,T]).
\]
Nondegeneracy gives \([Y_0,T]=0\), so \(Y_0\in\mathfrak t\). If \(Y\) was generic in another maximal abelian \(\mathfrak t'\), its transported centralizer is the transported \(\mathfrak t'\). It contains \(\mathfrak t\), hence equals it by maximal abelianness. This proves conjugacy.

For the first assertion, take \(M=Z_{K_\theta}(\mathfrak a)^0\), whose Lie algebra is \(\operatorname{ad}\mathfrak m\): differentiation gives exactly \(Z_{\mathfrak k}(\mathfrak a)\). It is a compact closed subgroup, and its action preserves \(\mathfrak m\). For the second assertion take \(\mathfrak l=\mathfrak u\), \(M=\operatorname{Aut}(\mathfrak u)^0\), as constructed in Section 3. A compact Cartan is maximal abelian: its complexification is self-centralizing and toral, and conversely a maximal abelian compact subalgebra is self-centralizing after complexification by simultaneous skew-adjoint diagonalization. The same argument applies. \(\square\)

In particular \(\mathfrak t\oplus i\mathfrak a\) is a compact Cartan, so it can be transported to the fixed one. Its complexification (8.12) can therefore be equipped with compact-compatible normalized Chevalley generators; subsequent base changes can be made by compact simple-root reflection lifts.

For an adapted positive system, choose \(a_0\in\mathfrak a\) avoiding every nonzero restricted-root hyperplane, and choose \(b_0\in i\mathfrak t\) avoiding the roots vanishing on \(\mathfrak a\). A root is positive if its value at \(a_0\) is positive, or if that value is zero and its value at \(b_0\) is positive. These are the signs of a regular element \(a_0+\varepsilon b_0\) for sufficiently small positive \(\varepsilon\). All evaluations here are real: adjoint operators from \(\mathfrak a\) and \(i\mathfrak t\) are commuting self-adjoint operators for the positive compact Hermitian form.

**Lemma 8.6.** For fixed \(\theta\), the choices of \(\mathfrak a,\mathfrak t\), and adapted positive system are all conjugate by automorphisms commuting with \(\theta\) and \(c\). The transporter can be chosen in \(K_\theta\).

**Proof.** Proposition 8.3 and Lemma 8.5 first align \(\mathfrak a\) and then \(\mathfrak t\). It remains to align the two adapted positive systems.

Let \(\Sigma\subset\mathfrak a^*\setminus\{0\}\) be the finite set of restricted roots, that is, the nonzero joint weights of \(\operatorname{ad}\mathfrak a\) on \(\mathfrak g_0\). The operators are commuting real self-adjoint operators for \(B_\theta\), so a nonzero real vector \(x\in(\mathfrak g_0)_\lambda\) exists for each \(\lambda\in\Sigma\). Also \(\theta x\) has weight \(-\lambda\). The bracket \(h_0=[x,-\theta x]\) centralizes \(\mathfrak a\), and \(\theta h_0=-h_0\); hence \(h_0\in Z_{\mathfrak p}(\mathfrak a)=\mathfrak a\). For \(A\in\mathfrak a\), invariance gives
\[
\kappa(h_0,A)=-\kappa(x,\theta x)\lambda(A).
\tag{8.13}
\]
The coefficient is \(B_\theta(x,x)>0\). Since \(\kappa\) is positive definite on \(\mathfrak a\), \(h_0\ne0\) and \(\lambda(h_0)>0\). Scale \(x\) by the positive real square root making \(\lambda([x,-\theta x])=2\). Then
\[
e=x,\quad f=-\theta x,\quad h=[e,f]
\]
obey \([h,e]=2e,[h,f]=-2f,[e,f]=h\), while \(e-f=e+\theta e\in\mathfrak k\). The automorphism
\[
n_\lambda=\exp\!\left(\frac\pi2\operatorname{ad}(e-f)\right)\in K_\theta
\]
acts on \(\mathfrak a\) by reflection in \(\ker\lambda\): it fixes that hyperplane because its elements commute with \(e,f\), and sends \(h\) to \(-h\) by the rank-one matrix calculation. Equation (8.13) says the decomposition is orthogonal for \(\kappa|_{\mathfrak a}\).

Thus this reflection preserves \(\Sigma\) and its hyperplane arrangement. These reflections generate a finite group on \(\mathfrak a\): it permutes the finite spanning set \(\Sigma\), and an operator fixing every weight is the identity. Spanning follows since an \(A\) killed by every restricted weight would centralize all of \(\mathfrak g_0\), whose centre is zero.

This reflection group is transitive on the arrangement's chambers. To see this without a restricted-Weyl theorem, join generic points of two chambers by a segment chosen to cross distinct reflecting hyperplanes at distinct times. The excluded endpoint choices lie in finitely many proper hyperplanes, as in the complete segment proof of RT-LIE-08 Theorem 5.1. The segment passes through a finite chain of adjacent chambers. Reflection in the separating wall preserves the arrangement and exchanges the two adjacent chambers, first locally near a point of that wall on no other wall, and therefore globally on their connected components. Following the chain gives the desired group element.

Choose such an element of \(K_\theta\) aligning the restricted chambers. It normalizes \(\mathfrak a\), and transports \(\mathfrak t\) to another maximal abelian subalgebra of \(\mathfrak m\). Correct it by Lemma 8.5 using an element fixing \(\mathfrak a\) pointwise, so it also normalizes \(\mathfrak h\). It then aligns the signs of every root with nonzero restriction.

The remaining roots are the black subsystem \(\Phi_X\): if a positive root has zero value at \(a_0\), its nonnegative simple-root expansion cannot involve a simple root with positive value there. Thus its support is exactly in the simple roots vanishing on \(\mathfrak a\). The Weyl group \(W_X\) is transitive on its positive systems by RT-LIE-08 Theorem 5.1, applied to that root subsystem. Its simple-reflection lifts lie in the compact black subalgebra, which centralizes \(\mathfrak a\) and is fixed by \(\theta\), as shown next. They therefore belong to \(K_\theta\), fix \(\mathfrak a\), and align the remaining signs. This proves the lemma. The black fixedness argument below is independent of this lemma, so there is no circularity. \(\square\)

#### 8.5.3. Extracting the pair and the black-root fixedness

Relative to (8.12) and an adapted base \(\Delta=\{\alpha_i\}\), let
\[
X=\{i:\alpha_i|_{\mathfrak a}=0\},\qquad
s(\alpha)=\alpha\circ(\theta|_{\mathfrak h})^{-1}.
\tag{8.14}
\]
Every root vanishing on \(\mathfrak a\) is fixed by \(s\), since \(\theta\) fixes \(\mathfrak t\) and negates \(\mathfrak a\).

**Lemma 8.7.** The black root subsystem is \(\Phi_X\), and \(\theta\) is the identity on its semisimple root subalgebra \(\mathfrak g_X\).

**Proof.** The support argument at the end of Lemma 8.6 proves that the roots vanishing on \(\mathfrak a\) are precisely \(\Phi_X\); negative roots follow by negation. For such a root \(\alpha\), its one-dimensional root space is preserved by \(\theta\), whose scalar is \(+1\) or \(-1\). If it were \(-1\), the compact conjugation \(c\), commuting with \(\theta\), would make the same scalar occur on the opposite root space. Their \(c\)-fixed real two-plane would lie in \(\mathfrak u_-\). Multiplying a nonzero vector of that plane by \(i\) gives a nonzero element of \(\mathfrak p\) centralizing \(\mathfrak a\), but outside \(\mathfrak a\), contradicting maximal abelianness. Thus the scalar is \(+1\). Opposite-root brackets give fixed coroots as well.

The subalgebra generated by the \(e_j,f_j,h_j\), \(j\in X\), is the finite semisimple algebra of matrix \(A_X\). Indeed the Serre provider gives a surjection from that algebra to this subalgebra. Every \(\Phi_X\) root space occurs in the image by transporting a black simple-root vector with the black simple-reflection operators; all \(\Phi_X\) roots are Weyl-conjugate to black simple roots. The independent coroot images and these one-dimensional root spaces give dimension \(|X|+|\Phi_X|\), the dimension of the source in RT-LIE-11 Theorem 6.1. Thus the surjection is an isomorphism. Fixedness of its generators proves the assertion. \(\square\)

On positive roots outside \(\Phi_X\), \(s\) changes the sign of the nonzero restriction, so sends them to negative roots outside that subsystem. A reflection in a black simple root changes only its black coefficient; hence \(w_X\) preserves positive roots outside \(\Phi_X\) and reverses all positive roots in \(\Phi_X\). Consequently
\[
\tau=-w_Xs
\tag{8.15}
\]
preserves all positive roots, so permutes the simple roots and is a directed Dynkin automorphism. Since \(s\) is identity on \(\Phi_X\), it commutes with \(W_X\); therefore \(\tau^2=1\). On \(X\), \(\tau=-w_X\), and \(\tau(X)=X\). Also \(\tau\) commutes with \(w_X\). Thus conditions (1)–(2) of Definition 8.4 have been proved. Condition (3) will emerge from the actual square of its reconstruction.

Lemma 8.6 shows that the extracted pair is independent of all Cartan and positivity choices up to diagram isomorphism: a transporter preserves the black subset and conjugates \(s\), and it transports \(w_X\) to the longest element of the transported black subsystem, so also conjugates (8.15).

#### 8.5.4. The black opposition lift from a principal sl2

**Lemma 8.8.** There is a compact-preserving inner automorphism \(n_X\) inducing \(w_X\) on \(\mathfrak h\), satisfying
\[
n_X(e_j)=-f_{\tau_X(j)},\quad
n_X(f_j)=-e_{\tau_X(j)},\quad
n_X(h_j)=-h_{\tau_X(j)}
\quad(j\in X),
\tag{8.16}
\]
where \(\tau_X=-w_X|_X\), and
\[
n_X^2=\exp(\pi i\,\operatorname{ad}H_X).
\tag{8.17}
\]
It commutes with \(\omega\) and with every pinned diagram automorphism preserving \(X\). When \(X\) is empty it is the identity.

**Proof.** For nonempty \(X\), put
\[
E_X=\sum_{j\in X}\sqrt{c_j}\,e_j,\quad
F_X=\sum_{j\in X}\sqrt{c_j}\,f_j,\quad
H_X=\sum_{j\in X}c_jh_j.
\]
By (8.8) and the cross relations \([e_j,f_\ell]=0\), these form an \(\mathfrak{sl}_2\) triple. Define
\[
n_X=\exp\!\left(\frac\pi2\operatorname{ad}(E_X-F_X)\right).
\tag{8.18}
\]
The vector \(E_X-F_X\) belongs to \(\mathfrak u\), so this preserves \(c\).

Here are the exact rank-one identities used for this exponential. Every finite-dimensional \(\mathfrak{sl}_2\)-module is a direct sum of the polynomial modules \(\operatorname{Sym}^n(\mathbb C^2)\), by RT-LIE-04 Theorem 3.3 and RT-LIE-05 Theorem 2.1 and Proposition 2.2. On the standard two-dimensional module,
\[
\exp\!\left(\frac\pi2(e-f)\right)
=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
=\exp(e)\exp(-f)\exp(e),
\]
its square is \(-I\), and this also equals \(\exp(\pi i h)\). Applying the supplied polynomial action to each \(\operatorname{Sym}^n\), the square is \((-1)^n\), which is \(\exp(\pi i h)\) on its weights \(n,n-2,\ldots,-n\). Differentiation, or the unique finite matrix ODE along the one-parameter subgroup, identifies the induced exponential with the exponential of its Lie operator. The identities therefore hold in every finite module, including the adjoint action on the whole \(\mathfrak g\). This proves (8.17), the product-of-three-nilpotent-exponentials expression, and \(n_XH_X=-H_X\), \(n_XE_X=-F_X\), \(n_XF_X=-E_X\).

The element \(H_X\) is regular in \(\mathfrak g_X\), since its value on every positive black root is twice that root's positive height. Thus its centralizer there is the black Cartan \(\mathfrak h_X\). The equality \(n_XH_X=-H_X\) shows that \(n_X\) normalizes \(\mathfrak h_X\). Invertibility of \(A_X\) gives the direct decomposition
\[
\mathfrak h=\mathfrak h_X\oplus
\{H:\alpha_j(H)=0\text{ for all }j\in X\}.
\]
Indeed the simple-root evaluations on the basis \(h_j\), \(j\in X\), have matrix \(A_X\), so the equations determine uniquely the \(\mathfrak h_X\)-part of any \(H\). The second summand centralizes every black generator. Hence \(n_X\) fixes that summand pointwise and normalizes all of \(\mathfrak h\).

On \(\mathfrak g_X\) it is inner, being the three nilpotent exponentials just proved. The actual normalizer theorem (9.8) in RT-LIE-11, applied to the semisimple algebra \(\mathfrak g_X\), makes its root action an element of \(W_X\). Since it sends \(H_X\) to its negative, it sends every black positive root to a negative one, so that action is \(w_X\). On the full Cartan it is \(w_X\), since both fix the complement centralizing \(\mathfrak g_X\).

Thus \(n_X\) takes \(e_j\) to a scalar multiple of \(f_{\tau_X(j)}\). The coefficients \(c_j\) are unchanged by black opposition because \(w_XH_X=-H_X\). Comparing coefficients in \(n_XE_X=-F_X\) makes all those scalars \(-1\); the same comparison for \(F_X\) and the brackets proves (8.16).

Finally \(\omega(E_X-F_X)=E_X-F_X\), so \(\omega\) commutes with (8.18). Any pinned diagram automorphism preserving \(X\) permutes its positive coroots, fixes \(H_X\), and permutes its coefficients \(c_j\); it fixes both \(E_X,F_X\), and therefore also commutes with (8.18). All assertions apply componentwise even when \(X\) is disconnected. \(\square\)

This argument proves the opposition signs and square directly. It neither assumes that longest-word representatives satisfy braid relations nor imports a theorem about Tits representatives.

#### 8.5.5. Necessity, reconstruction and the coefficient correction

For any pair satisfying conditions (1)–(2), set
\[
\theta_0=n_X\widehat\tau\omega,\qquad
s=-w_X\tau,\qquad
\delta_i=(-1)^{\alpha_i(H_X)}
=(-1)^{\sum_{j\in X}a_{ij}c_j}.
\tag{8.19}
\]
The three factors commute by Lemma 8.8, and
\[
\theta_0^2=\exp(\pi i\operatorname{ad}H_X)=D_\delta.
\tag{8.20}
\]
Here \(D_t\) denotes the torus automorphism
\[
D_t(e_i)=t_i e_i,\quad
D_t(f_i)=t_i^{-1}f_i,\quad
D_t(h_i)=h_i.
\tag{8.21}
\]
The Serre relations prove its existence; its root coefficient is the character \(t(\sum m_i\alpha_i)=\prod t_i^{m_i}\). It preserves \(c\) exactly when all \(t_i\) are unimodular. Lemma 8.8 and condition (2) show that \(\theta_0\) is the identity on \(\mathfrak g_X\), and its root action is \(s\).

For an actual \(\theta\) extracted in Section 8.5.3, \(\theta\theta_0^{-1}\) fixes \(\mathfrak h\) pointwise. The exact scalar-stabilizer proof in RT-LIE-11 §9 gives \(\theta=D_t\theta_0\). Since both preserve \(c\), \(|t_i|=1\), and their fixed black subalgebra gives \(t_j=1\) for \(j\in X\).

Conjugation by \(\theta_0\) takes \(D_t\) to \(D_{s(t)}\), where \(s(t)(\alpha)=t(s^{-1}\alpha)=t(s\alpha)\). Since a black reflection changes a weight only by black roots,
\[
s\alpha_i\equiv-\alpha_{\tau(i)}\pmod{Q_X}.
\]
For \(t|_{Q_X}=1\), therefore \(s(t)_i=t_{\tau(i)}^{-1}\), and the square condition is exactly
\[
(D_t\theta_0)^2=1
\quad\Longleftrightarrow\quad
\frac{t_i}{t_{\tau(i)}}\delta_i=1
\quad\text{for every }i.
\tag{8.22}
\]
Black vertices have \(\delta_j=1\) by (8.8). On a fixed white vertex the torus quotient is one, so (8.22) forces \(\delta_i=1\), which is precisely condition (3), including the even-integer condition (8.9). This proves necessity of the admissibility obstruction.

**Proposition 8.9 (existence).** Every admissible pair constructs a compact involution and a real form with precisely its Satake diagram.

**Proof.** The parity signs satisfy \(\delta_{\tau(i)}=\delta_i\), since \(\tau H_X=H_X\). Define \(t^0_j=1\) on black and fixed white vertices. On each white two-cycle \(\{i,\tau(i)\}\), choose one vertex and put
\[
t^0_i=1,\qquad t^0_{\tau(i)}=\delta_i.
\tag{8.23}
\]
All coefficients are unimodular, and (8.22) holds at every vertex. Hence
\[
\theta(X,\tau)=D_{t^0}n_X\widehat\tau\omega
\tag{8.24}
\]
is an involution preserving \(c\). Its conjugation \(\theta(X,\tau)c\) fixes the real form (8.11).

It remains to prove that the prescribed Cartan is maximally split and gives the specified black subsystem. In the fixed real coroot span \(\mathfrak h_{\mathbb R}\), take
\[
\mathfrak a=\{H:\theta H=-H\},\qquad
\mathfrak t=i\{H:\theta H=H\}.
\tag{8.25}
\]
These lie respectively in \(\mathfrak p\) and \(\mathfrak k\). A root vanishes on \(\mathfrak a\) exactly when it is fixed by the orthogonal root involution \(s=-w_X\tau\). Its fixed roots are exactly \(\Phi_X\). Indeed \(s\) is identity on \(\Phi_X\). Conversely, if \(s\beta=\beta\), the white simple coefficients of \(\beta\) must equal the negatives of their \(\tau\)-permuted coefficients, because \(w_X\) is identity modulo \(Q_X\). A positive root has all these coefficients nonnegative, so they are all zero; negative roots follow by negation. Thus \(\beta\in\Phi_X\).

The centralizer of \(\mathfrak a\) in \(\mathfrak g\) is therefore
\[
\mathfrak h\oplus\bigoplus_{\alpha\in\Phi_X}\mathfrak g_\alpha.
\]
The entire black subalgebra is fixed by \(\theta(X,\tau)\), while the negative Cartan eigenspace is \(\mathfrak a_{\mathbb C}\). Taking the real \(\mathfrak p\)-part gives \(Z_{\mathfrak p}(\mathfrak a)=\mathfrak a\). Thus \(\mathfrak a\) is maximal abelian in \(\mathfrak p\).

The chosen compact part \(\mathfrak t\) is also maximal abelian in \(\mathfrak m=Z_{\mathfrak k}(\mathfrak a)\). Indeed \(\mathfrak h_X\) is fixed by \(\theta\), so \(i(\mathfrak h_X)_{\mathbb R}\subseteq\mathfrak t\). Every black root is nonzero on \(\mathfrak h_X\), by nondegeneracy of the black root system. Consequently the displayed centralizer has no root-space vector centralizing both \(\mathfrak a\) and \(\mathfrak t\). Its \(\mathfrak k\)-part is exactly \(\mathfrak t\), so \(Z_{\mathfrak m}(\mathfrak t)=\mathfrak t\). This verifies both maximality conditions in (8.12).

There is an adapted positive system equal to the prescribed one. On the real root space choose a functional \(\ell\) with \(\ell(\alpha_j)=0\) on \(X\) and \(\ell(\alpha_i)=1\) on all white vertices. It is \(\tau\)-invariant and vanishes on \(Q_X\), hence \(\ell(s\beta)=-\ell(\beta)\). It is evaluation at a vector \(a_0\in\mathfrak a\). Every positive root outside \(\Phi_X\) has positive value there. Choose the positive black chamber on the fixed Cartan part; for example \(H_X\) has positive values on every positive black root. The signs of \(a_0+\varepsilon H_X\), for sufficiently small \(\varepsilon>0\), are exactly the prescribed positive roots. Equations (8.14)–(8.15) then recover \(X,\tau\) from (8.24). \(\square\)

**Lemma 8.10 (all coefficient choices are equivalent).** For a fixed admissible pair, all compact involutions \(D_t\theta_0\) with \(t|_{Q_X}=1\) and (8.22) are conjugate by a compact torus automorphism.

**Proof.** Compare \(t\) with \(t^0\) and put \(d_i=t_i/t^0_i\). Equation (8.22) gives \(d_{\tau(i)}=d_i\), and \(d_j=1\) on \(X\). Choose unimodular \(q_j=1\) on \(X\). On a fixed white vertex choose a square root \(q_i^2=d_i^{-1}\). On a white two-cycle choose \(q_i=d_i^{-1},q_{\tau(i)}=1\). These are allowed independent simple-root coefficients of (8.21). Since \(s(q)_i=q_{\tau(i)}^{-1}\),
\[
D_q(D_t\theta_0)D_q^{-1}
=D_{q\,s(q)^{-1}\,t}\theta_0
=D_{t^0}\theta_0.
\tag{8.26}
\]
Every coefficient has been checked, and equality on generators proves equality on \(\mathfrak g\). The correcting automorphism lies in \(\operatorname{Aut}(\mathfrak u)^0\): the independent unit-circle simple coefficients form a connected torus, and (8.21) is a continuous homomorphism whose image contains the identity. Equivalently, choose real arguments \(q_i=e^{iv_i}\) and use the path \(D_{(e^{itv_i})}\), \(0\le t\le1\). Thus choices of two-cycle representatives, square roots and compatible root-vector phases do not affect the real isomorphism class. \(\square\)

#### 8.5.6. Completeness and injectivity

**Proposition 8.11.** Every involution of \(\mathfrak u\) is conjugate under \(\operatorname{Aut}(\mathfrak u)^0\) to one of (8.24).

**Proof.** Use Proposition 8.3 to obtain (8.12) and an adapted positive system. Lemma 8.5 transports its compact Cartan to the fixed compact Cartan. RT-LIE-08 Theorem 5.1 transports its base to the fixed base; its simple-reflection lifts are the compact rank-one rotations used in Lemma 8.8 for singleton \(X\). The transports belong to the compact identity component. Section 8.5.3 extracts \(X,\tau\), Section 8.5.5 proves its admissibility and writes the transported involution \(D_t\theta_0\), and Lemma 8.10 gives (8.24). \(\square\)

**Proposition 8.12.** Two constructed compact involutions are conjugate under \(\operatorname{Aut}(\mathfrak u)\) if and only if their admissible pairs are isomorphic.

**Proof.** If \(\phi\theta\phi^{-1}=\theta'\) is a compact automorphism, it sends the chosen \(\mathfrak a,\mathfrak t\), and adapted positive system for \(\theta\) to such choices for \(\theta'\). Lemma 8.6 supplies a compact automorphism commuting with \(\theta'\) that aligns the transported choices with the choices used to extract the target pair. After this correction, \(\phi\) transports the Cartan and its base exactly. Its root map is then a directed Dynkin isomorphism \(f\). It carries roots vanishing on \(\mathfrak a\) to those vanishing on \(\mathfrak a'\), so \(f(X)=X'\), and intertwines \(s,s'\). It carries \(w_X\) to \(w_{X'}\); (8.15) therefore gives \(f\tau=\tau'f\).

Conversely a pair isomorphism \(f\) has the pinned Serre isomorphism \(\widehat f\), which preserves the compact conjugation. It carries \(H_X,E_X,F_X,n_X,\widehat\tau,\omega\) to their primed counterparts. It therefore transports (8.24) to a coefficient choice for the target pair. Lemma 8.10 aligns that choice with the chosen \(t^{0\prime}\), by a compact torus correction. The resulting compact automorphism conjugates the two involutions. \(\square\)

A real semisimple algebra has semisimple complexification: RT-LIE-03 Theorem 3.3 proves nondegeneracy of its Killing form, and the same Killing matrix remains nondegenerate under extension to \(\mathbb C\). The complex Serre classification supplies its finite complex Dynkin diagram. Theorems 8.1–8.2, Proposition 8.11 and Proposition 8.12 now prove Theorem 8.4 at the stated real semisimple generality.

#### 8.5.7. Components, complex type and useful checks

If \(\tau\) exchanges two connected components, \(X\) meets neither. Indeed \(\tau|_X=-w_X|_X\) cannot move a black root between components, since \(W_X\) acts separately on the components. Conversely two isomorphic components may be entirely white and exchanged by any directed diagram isomorphism between them, with its inverse on return. These satisfy admissibility and are all equivalent under component isomorphisms.

For a plain exchange of two copies of a complex simple algebra, (8.24) is \(\theta=\widehat\tau\omega\). Writing \(c=\omega c_{\rm split}\), where \(c_{\rm split}\) fixes the real Serre generators and conjugates scalars, its real conjugation is \(\theta c=\widehat\tau c_{\rm split}\). Its fixed space is
\[
\{(x,\overline x):x\in\mathfrak g_i\}.
\tag{8.27}
\]
The map \(x\mapsto(x,\overline x)\) is a real-linear bracket isomorphism from \(\mathfrak g_i\) viewed as a real algebra. An arbitrary component exchange differs by an isomorphism in one direction and its inverse in the other; conjugating by that component isomorphism makes it the plain exchange. Thus all real simple algebras of complex type are included. On components preserved by \(\tau\), the connected classification already proved applies. Permutations of repeated components are exactly the permutations allowed in diagram isomorphisms.

For an admissible pair, \(\dim\mathfrak a\) equals the number of white \(\tau\)-orbits. On the black root span \(s=1\); on the quotient of the root space by that span, \(s=-\tau\). Since an involution is diagonalizable, its negative eigenspace dimension is that of the negative eigenspace on the quotient, namely the positive eigenspace of the white permutation \(\tau\), one dimension per orbit. The \(\mathfrak h\)-trace of \(\theta\) is \(r-2\dim\mathfrak a\). All fixed roots are black, with coefficient \(+1\), and every other root space is paired with a distinct one. Thus
\[
\dim_\mathbb C\mathfrak g^\theta
=r-\dim\mathfrak a+\frac{|\Phi|+|\Phi_X|}{2}.
\tag{8.28}
\]
The real Killing signature is
\((\dim_\mathbb C\mathfrak g-\dim_\mathbb C\mathfrak g^\theta,\,
\dim_\mathbb C\mathfrak g^\theta)\).
These are consequences and useful checks, not substitutes for injectivity.

For example, in type \(A_2\), \(X=\{1\},\tau=1\) fails admissibility because \(\alpha_2(\rho_X^\vee)=-1/2\); no torus coefficient can change the resulting square \(-1\) on that fixed white root. In type \(A_3\), \(X=\{1,3\},\tau=1\) is admissible because \(\alpha_2((h_1+h_3)/2)=-1\). Also \(X=\{2\}\) is admissible with \(\tau=(1\,3)\), although it is not admissible with \(\tau=1\). These examples explicitly distinguish the obstruction from a colouring rule without parity.

There is no remaining finite-type case theorem hidden in Theorem 8.4. For any of the finite Dynkin matrices already classified internally, Definition 8.4 is a finite, non-tautological root-data test; Proposition 8.9 constructs every surviving pair and Proposition 8.12 proves exactly all equivalences and inequivalences. One may enumerate its finite tests to print a conventional table, but such a table is not needed for the existence/completeness/injectivity proof. The downloadable [exact enumeration](proofs/check_satake_admissibility.py), with its [recorded results](proofs/satake_admissibility_checks.json), checks 35 matrices: all exceptional types; classical ranks through 8; \(D_4\) triality; \(A_1\oplus A_1\) and \(A_2\oplus A_2\) component exchanges; and rank zero. It returns exceptional class counts \(5,4,3,3,2\) for \(E_6,E_7,E_8,F_4,G_2\), respectively, with the fixed-algebra dimensions and split ranks computed from (8.28). It is a sanity check of the universal proof, not its replacement. The script uses exact integer and rational arithmetic, enumerates all directed diagram automorphisms, and records every surviving representative with its black opposition, \(H_X\)-coefficients and parity evaluations.

For the empty diagram, the algebra is zero, \(c,\theta\) have their unique empty meanings, and the unique real form is zero. Compact forms \(X=I\) produce \(\theta=1\), which is allowed throughout this proof.

#### 8.5.8. Sources and further classification context

The explicit admissibility criterion corresponds to Stefan Kolb, [*Quantum symmetric Kac–Moody pairs*, arXiv:1207.6036v3, Definition 2.3](https://arxiv.org/html/1207.6036v3#S2.SS4). Its Proposition 2.2 and Theorem 2.5 treat the opposition lift and reconstruction; Theorem 2.7 and Appendix A use further classification results. The finite-dimensional lift, normalization and equivalence arguments required here have been proved in Lemmas 8.5–8.8 and 8.10 and Propositions 8.9, 8.11–8.12.

For compact-compatible Satake normalization, compare Kenny De Commer, Sergey Neshveyev, Lars Tuset and Makoto Yamashita, [*Ribbon braided module categories, quantum symmetric pairs and Knizhnik–Zamolodchikov equations*, arXiv:1712.08047v2, §2, Definitions 2.4–2.5 and Theorem 2.6](https://arxiv.org/html/1712.08047v2#S2), and [Appendix A.1](https://arxiv.org/html/1712.08047v2#A1.SS1). This lesson includes the identity compact involution and the all-black diagram. Etingof, [*Lie groups and Lie algebras*, arXiv:2201.09397v5, §§40–42](https://arxiv.org/html/2201.09397v5#S40), provides further comparison for semisimple components, compact involutions and Vogan diagrams. These sources are credited for their mathematical results; the exposition and proofs here were independently written.

Over more general fields, reductive-group classification also needs the anisotropic kernel and its compatible identification, alongside the index and separably closed type; see Milne, *Algebraic Groups*, §25c, Definition 25.29 and Theorem 25.30, pp. 555–556. The present theorem classifies real semisimple Lie algebras. Global Lie groups with the same Lie algebra additionally require their central quotient data.

## 9. Exercises with complete solutions

**Exercise 9.1 (easy).** Exhibit \(\mathfrak{su}(2)\) as a compact real form of \(\mathfrak{sl}_2(\mathbb C)\), and show that \(\mathfrak{sl}_2(\mathbb R)\) is not of compact type.

**Solution.** With the usual \(e,f,h\), a real basis of \(\mathfrak{su}(2)\) is
\[
T=ih=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
A=e-f=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
B=i(e+f)=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
\]
It satisfies \([T,A]=2B\), \([T,B]=-2A\), \([A,B]=2T\); hence its real span is closed. Conversely, every skew-Hermitian traceless matrix has the form \(aT+bA+cB\) with real \(a,b,c\). Its fixed conjugation is \(-X^*\), so its complexification is \(\mathfrak{sl}_2(\mathbb C)\). Since \(\kappa=4\operatorname{Tr}(XY)\), its Gram matrix in this basis is \(-8I_3\). The group \(SU(2)\simeq S^3\) is compact.

On \(\mathfrak{sl}_2(\mathbb R)\), use \(h,e+f,e-f\). The Killing Gram matrix is \(\operatorname{diag}(8,8,-8)\). Thus this real form is not of compact type and cannot be the Lie algebra of a compact group: averaging any positive real inner product in a compact group's adjoint representation would make its adjoint operators skew-adjoint, forcing its Killing form to be negative semidefinite by (6.3). Also \(\operatorname{diag}(e^t,e^{-t})\) is an unbounded subgroup of \(SL_2(\mathbb R)\). \(\square\)

**Exercise 9.2 (medium).** Compute the Killing signatures of \(\mathfrak{sl}_n(\mathbb R)\), \(\mathfrak{su}(n)\), and \(\mathfrak{su}(1,1)\).

**Solution.** Write a real traceless matrix uniquely as \(X=S+A\) with \(S^{\mathsf T}=S\), \(\operatorname{Tr}S=0\), and \(A^{\mathsf T}=-A\). Transposing \(SA\) and cycling its trace shows \(\operatorname{Tr}(SA)=-\operatorname{Tr}(SA)\), hence zero. Moreover \(\operatorname{Tr}S^2=\sum_{ij}S_{ij}^2\) and \(\operatorname{Tr}A^2=-\sum_{ij}A_{ij}^2\). The dimensions are \(n(n+1)/2-1\) and \(n(n-1)/2\), proving (7.5). A skew-Hermitian \(X\) satisfies \(\operatorname{Tr}X^2=-\operatorname{Tr}XX^*\), so all \(n^2-1\) directions in \(\mathfrak{su}(n)\) are negative. For \(\mathfrak{su}(1,1)\), write
\[
X=\begin{pmatrix}ia&z\\\overline z&-ia\end{pmatrix},
\qquad a\in\mathbb R,\quad z=b+ic.
\]
Then \(X^2=(b^2+c^2-a^2)I\), and \(\kappa(X,X)=8(b^2+c^2-a^2)\). Its signature is \((2,1)\). For \(n=1\), the first two algebras are zero and their signatures are \((0,0)\). \(\square\)

**Exercise 9.3 (medium).** Prove complete reducibility of finite-dimensional \(\mathfrak{sl}_n(\mathbb C)\)-modules using \(SU(n)\).

**Solution.** Restrict a module \(V\) to \(\mathfrak{su}(n)\). The fixed-conjugation decomposition proves \(\mathfrak{sl}_n(\mathbb C)=\mathfrak{su}(n)\oplus i\mathfrak{su}(n)\), so restriction retains the whole module information. Section 6 proves that \(SU(n)\) is compact, connected and simply connected. Proposition 4.1 therefore integrates the restricted action to \(\pi:SU(n)\to GL(V)\). Construct its normalized invariant density as in (5.1), and average any positive Hermitian form as in (5.2).

For a complex \(\mathfrak{sl}_n\)-submodule \(W\), Lie algebra invariance implies \(SU(n)\)-invariance by exponential generation. The averaged form makes \(W^\perp\) invariant under \(SU(n)\): for \(v\in W^\perp\), \(w\in W\), the equality \(H(\pi(g)v,w)=H(v,\pi(g^{-1})w)\) vanishes. Differentiation and complex extension make \(W^\perp\) a \(\mathfrak{sl}_n\)-submodule. Thus every submodule splits; induction on dimension gives an irreducible direct sum. The case \(n=1\) is the zero algebra, for which any basis decomposes \(V\) into one-dimensional modules. No assertion about integration to an adjoint quotient is needed. \(\square\)

**Exercise 9.4 (hard).** Prove the compact-form construction, identifying all bracket sign conditions.

**Solution.** Take (2.1)–(2.2) and define \(\tau\) by (2.4). Its bracket checks have four substantive cases. Cartan-Cartan gives zero. Cartan-root uses real Cartan integers and the sign change of the root:
\(\tau([h_i,e_\alpha])=-\alpha(h_i)e_{-\alpha}=[-h_i,-e_{-\alpha}]\).
Opposite roots give
\(\tau(h_\alpha)=-h_\alpha=[e_{-\alpha},e_\alpha]\).
For a sum that is a root, bracket preservation is equivalent to \(N_{-\alpha,-\beta}=-N_{\alpha,\beta}\); for a nonroot sum with \(\beta\ne-\alpha\), both sides vanish. These checks cover every basis pair and therefore all brackets by conjugate bilinearity.

Its fixed vectors are exactly the real span of \(ih_i,A_\alpha,B_\alpha\). Formula (1.2) gives a direct real-form decomposition. In particular closure follows with the exact stated signs, rather than from realness of the constants alone. For example, for any roots whose sum is a root,
\[
[e_\alpha-e_{-\alpha},e_\beta-e_{-\beta}]
=N_{\alpha,\beta}(e_{\alpha+\beta}-e_{-\alpha-\beta})
-N_{\alpha,-\beta}(e_{\alpha-\beta}-e_{-\alpha+\beta}), \tag{9.1}
\]
where a term is omitted if its indicated sum is not a root; this formula is used only for \(\alpha\ne\pm\beta\). Mixed and imaginary-sum brackets are already included by the \(\tau\)-checks. The remaining same-pair brackets are explicitly \([A_\alpha,B_\alpha]=2ih_\alpha\), \([iH,A_\alpha]=\alpha(H)B_\alpha\), and \([iH,B_\alpha]=-\alpha(H)A_\alpha\).

Finally, on the real Cartan span the Killing form is the positive sum of root squares (2.5). Invariance gives pairwise orthogonal Cartan/root blocks and \(c_\alpha=\kappa(h_\alpha,h_\alpha)/2>0\). The compact Cartan block has its sign reversed, and each root-pair block has Gram matrix \(-2c_\alpha I_2\). All coefficients are real; all nonzero directions are strictly negative. This proves the whole theorem, including semisimple products. For the zero algebra the negative-definiteness assertion is vacuous. If root vectors are independently rescaled without preserving (2.2), the simple formula (2.4) need not preserve brackets; one must restore the compatible normalization or change the conjugation coefficients accordingly. \(\square\)

## 10. What this lesson does not prove

The sign-compatible integral basis is proved in Lesson 12. Compact-form uniqueness, the finite fundamental group and compact simply connected cover, and the covering Lie group construction are proved in Sections 2–3 above. Section 8.5 proves the full finite Satake classification, including explicit admissibility, reconstruction and real-isomorphism equivalence. The closed subgroup theorem is the basic Lie-group foundation used in constructing the compact adjoint group; see Kirillov, Theorem 2.9(2), pp. 14–15. The elementary manifold ODE, smoothing, exponential-chart and fiber-bundle homotopy facts are also background inputs. The representation integration argument, Haar-density construction, compact-form signs, classical models, signatures and all four solutions have been proved here. Section 8 proves general Cartan-involution existence, the precise compact-involution isomorphism criterion, and maximal split Cartan existence and conjugacy of the split subspaces. Global classification of central quotients and the infinite-dimensional unitary decomposition theorem remain additional work.

References for comparison and further study:

- Alexander Kirillov Jr., *Introduction to Lie Groups and Lie Algebras*, author lecture notes, §§2.2, 3.8–3.10, 4.5–4.6 and 6.2–6.3; especially Theorems 2.7, 2.9, 3.41, 4.36 and Remark 6.11/Theorem 6.13. [Author's notes](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf).
- Maarten Solleveld, *Lie algebra cohomology and Macdonald's conjectures*, master's thesis, University of Amsterdam, 2002, §1.3, Theorems 1.16–1.17, pp. 15–18. [Author's thesis](https://www.math.ru.nl/~solleveld/scrip.pdf).
- J. S. Milne, [*Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected author edition (2021 revision, published 2022)](https://www.jmilne.org/math/Books/iAG2022.pdf), §25c, Definition 25.29 and Theorem 25.30, pp. 555–556: the index, anisotropic kernel and algebraic-group classification context.


Pavel Etingof, [*Lie groups and Lie algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), provides additional treatments of compact real forms, compact groups and invariant differential forms. The spectral-power, finite-loop and averaging arguments needed here have been supplied above.

The real-form reduction and involution isomorphism criterion can be compared with Etingof, [Theorem 41.5](https://arxiv.org/html/2201.09397v5#S41.Thmtheorem5); the proofs used in Section 8 have been given explicitly.

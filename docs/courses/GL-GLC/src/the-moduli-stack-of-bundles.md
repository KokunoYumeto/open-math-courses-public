# The moduli stack of bundles

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Draft under mathematical proof repair; full proof closure pending. Public domain (CC0).*

A bundle can have many automorphisms while admitting few deformations. A moduli stack records both. This is why its dimension can be negative, why the dimension of a coarse moduli space is a different calculation, and why its cotangent stack is a space of Higgs fields rather than an ordinary vector bundle of constant rank.

Throughout, \(X\) is a smooth projective connected curve over an algebraically closed field \(k\) of characteristic zero. Its genus is \(g\). The group \(G\) is connected reductive. We impose \(g\ge2\) only where it is needed and say so explicitly. A principal bundle is a right \(G\)-torsor; write \(\operatorname{ad}(P)=P\times^G\mathfrak g\) for its adjoint vector bundle. Complexes are cohomologically graded, so \(V[1]\) puts a vector space \(V\) in degree \(-1\).

The prerequisite is deformation theory of algebraic stacks, together with Riemann–Roch and Serre duality on a curve. The [previous lesson](from-automorphic-functions-to-automorphic-sheaves.md) constructed bundles from lattices and identified the elementary Hecke fibres. Here we examine the stack on which those correspondences act.

## 1. The moduli problem, including its arrows

For a \(k\)-scheme \(S\), the groupoid \(\operatorname{Bun}_G(S)\) consists of \(G\)-torsors on \(X\times S\) and their isomorphisms. Pullback in \(S\) makes this a stack for the fppf topology: torsors, their actions, and their isomorphisms satisfy faithfully flat descent. For \(G=GL_n\), the associated standard representation identifies this groupoid with rank-\(n\) vector bundles. For \(G=\mathbb G_m\), it is the groupoid of line bundles, usually called the Picard stack.

An algebraicity theorem is an input: \(\operatorname{Bun}_G\) is an algebraic stack locally of finite type over \(k\). One precise source covering the present constant group is [Heinloth, Proposition 1], whose hypotheses are a smooth affine group scheme of finite type on the curve. We prove smoothness and the dimension below; we do not reproduce Artin's representability theorem.

The diagonal is affine and of finite type. Here is a way to understand this assertion. Given two bundles \(P,Q\) over \(X\times S\), their isomorphism functor is the functor of sections of the affine \(X\times S\)-scheme \(\operatorname{Isom}_G(P,Q)\). Work locally on \(S\). An affine scheme of finite presentation over \(X\times S\) can be presented inside a vector bundle by finitely many equations, using a sufficiently ample twist to produce generators and relations. The section functor of that vector bundle is affine: it is represented by the degree-zero linear stack of \(R\pi_*V\), or directly by the linear equations in a two-term finite locally free presentation of that complex. Imposing the finitely many algebraic relations gives a closed affine subscheme. This represents the isomorphism functor.

For vector bundles the equations are particularly concrete. A pair of homomorphisms \(u:E\to F\) and \(v:F\to E\) is an isomorphism with its inverse precisely when \(vu=1_E\) and \(uv=1_F\). These are closed equations in the affine section functors of the two Hom bundles. Keeping the inverse as a variable explains affineness without asserting that every arbitrary open subscheme of an affine scheme is affine.

Local finite type does not mean that there is a single finite type space of all bundles. Degree and instability both produce unbounded families. We will distinguish them carefully.

## 2. Deformations and the dimension formula

**Proposition 2.1.** At a bundle \(P\), the tangent complex of \(\operatorname{Bun}_G\) is

\[
T_P\operatorname{Bun}_G\simeq R\Gamma(X,\operatorname{ad}(P))[1].
\]

Its degree \(-1\) cohomology is the Lie algebra of automorphisms, its degree zero cohomology gives first-order deformations, and degree one gives obstructions. In particular,

\[
H^{-1}(T_P)=H^0(X,\operatorname{ad}(P)),\qquad
H^0(T_P)=H^1(X,\operatorname{ad}(P)),\qquad
H^1(T_P)=0.
\]

**Proof.** Choose an affine étale cover trivializing \(P\), with transition functions \(g_{ij}\). For a square-zero thickening with ideal \(I\), smoothness of \(G\) lets us lift each transition function. The failure of the lifted functions to satisfy the cocycle equation on triple overlaps is an additive Čech 2-cocycle with coefficients in \(\operatorname{ad}(P)\otimes I\). Conjugation by the transition functions gives precisely the adjoint bundle, rather than the constant Lie algebra sheaf.

Changing the lifts by 1-cochains changes that failure by a coboundary. Consequently its cohomology class is the obstruction. If it vanishes, correcting the lifts produces a bundle. The set of lift classes is a torsor under \(H^1(\operatorname{ad}(P)\otimes I)\), and an automorphism inducing the identity before thickening is a 0-cocycle, in \(H^0(\operatorname{ad}(P)\otimes I)\). Čech cohomology computes coherent cohomology here, since the cover and its finite intersections are affine. These groups and their cochain-level maps identify the deformation complex with \(R\Gamma(\operatorname{ad}(P))[1]\). On a curve coherent cohomology vanishes above degree one, proving the last assertion. \(\square\)

The same argument applies to families and successive square-zero extensions. The relative coherent cohomological dimension is one. Thus the infinitesimal lifting criterion, combined with the algebraicity and local finite presentation already stated, proves that \(\operatorname{Bun}_G\to\operatorname{Spec}k\) is smooth.

**Theorem 2.2.** The stack \(\operatorname{Bun}_G\) is smooth and has pure dimension

\[
\dim\operatorname{Bun}_G=(g-1)\dim G.
\]

**Proof.** A smooth algebraic stack with the tangent complex above has local dimension

\[
\dim H^1(X,\operatorname{ad}(P))-
\dim H^0(X,\operatorname{ad}(P))=-\chi(X,\operatorname{ad}(P)).
\]

The minus sign is the contribution of infinitesimal stabilizers. It also follows by taking a smooth presentation \(U\to\operatorname{Bun}_G\) and subtracting its relative dimension from \(\dim U\).

The character \(\det\operatorname{Ad}:G\to\mathbb G_m\) is trivial. To see this, restrict to a maximal torus. The weights are the roots, in opposite pairs, and zero weights; their sum is zero. A character of a connected reductive group is determined by its restriction to a maximal torus. Hence \(\det\operatorname{ad}(P)\) is trivial and \(\deg\operatorname{ad}(P)=0\). Riemann–Roch gives

\[
\chi(X,\operatorname{ad}(P))=(1-g)\dim G.
\]

This is independent of \(P\), so the stated dimension is pure. \(\square\)

For \(GL_n\), the answer is \(n^2(g-1)\). For the Picard stack it is \(g-1\). The Picard scheme of a fixed degree instead has dimension \(g\), because it has forgotten the scalar automorphisms. For \(X=\mathbb P^1\), the Picard stack has dimension \(-1\): each degree component is \(B\mathbb G_m\). Negative stack dimension records the stabilizer; it is not a negative number of parameters in a scheme.

*Source comparison:* [Beilinson–Drinfeld, §2.1.1] describes the tangent and cotangent complexes in the semisimple case with \(g>1\). The proof just given also explains the reductive and low-genus cases without importing that restriction.

## 3. Why degree gives exactly the components of \(\operatorname{Bun}_{GL_n}\)

Degree is locally constant in a family of vector bundles on a proper curve. Indeed, Euler characteristic is locally constant for a flat proper family, and Riemann–Roch expresses it as \(\deg E+n(1-g)\). Thus there are disjoint open and closed substacks \(\operatorname{Bun}_n^d\). The work is to prove each is connected.

**Lemma 3.1.** The scheme \(\operatorname{Pic}^d(X)\) is connected for every integer \(d\).

**Proof.** Choose \(m\ge\max(0,2g-1)\). Riemann–Roch gives \(h^0(L)=m+1-g>0\) for every line bundle of degree \(m\). Every such \(L\) therefore has the form \(\mathcal O(D)\) for an effective divisor of degree \(m\). The Abel map \(\operatorname{Sym}^mX\to\operatorname{Pic}^mX\) is surjective: its proper image contains every closed point. The source is connected, since it is the image of the connected scheme \(X^m\). Hence the target is connected. Tensoring by \(\mathcal O((m-d)x)\), for any \(x\in X(k)\), identifies \(\operatorname{Pic}^d\) with \(\operatorname{Pic}^m\). \(\square\)

The algebraicity and representability of the Picard scheme used here are background inputs [Stacks, Tag 0B9Z]. The Picard stack in a fixed degree has the same connectedness: its map to the Picard scheme is a gerbe with connected fibre \(B\mathbb G_m\). A choice of a point of \(X\) gives a normalized Poincaré bundle and a neutralization, though connectedness does not require a chosen neutralization.

**Lemma 3.2.** Every vector bundle is connected, through algebraic families of the same rank and degree, to a direct sum of line bundles.

**Proof.** A nonzero vector in the generic fibre determines a rank-one subsheaf. Saturating it gives a line subbundle \(L\subset E\) with locally free quotient \(Q\): on a nonsingular curve, a torsion-free coherent sheaf is locally free. The extension class

\[
\eta\in\operatorname{Ext}^1(Q,L)
\]

can be multiplied by the coordinate \(t\) on \(\mathbb A^1\). The class \(t\eta\) defines a family of extensions on \(X\times\mathbb A^1\), with fibres \(E\) at \(t=1\) and \(L\oplus Q\) at \(t=0\). One may construct the family by multiplying the off-diagonal terms in transition matrices by \(t\); the extension cocycle equations are linear in those terms. The middle term remains locally free. Repeat with \(Q\) by induction on the rank. Each step keeps total degree fixed and has a connected parameter scheme. \(\square\)

**Lemma 3.3.** For line bundles \(L,M\) and \(x\in X(k)\), the bundles \(L\oplus M\) and \(L(-x)\oplus M(x)\) lie in the same connected component.

**Proof.** Start with \(V=L\oplus M(x)\). Its elementary modifications of length one at \(x\) are parameterized by the projective line of one-dimensional quotients of \(V_x\), as proved in the previous lesson. The universal kernel is a vector bundle on \(X\times\mathbb P(V_x^*)\). At the quotient supported on the second summand its kernel is \(L\oplus M\). At the quotient supported on the first summand it is \(L(-x)\oplus M(x)\). Both are fibres of this connected family. \(\square\)

**Theorem 3.4.** The degree map induces a bijection

\[
\pi_0(\operatorname{Bun}_{GL_n})\simeq\mathbb Z.
\]

**Proof.** Lemma 3.2 connects any \(E\in\operatorname{Bun}_n^d\) to \(L_1\oplus\cdots\oplus L_n\). Apply Lemma 3.3, in either direction and as many times as necessary, to transfer degrees from the last \(n-1\) summands to the first. This connects the sum to one with degree list \((d,0,\ldots,0)\). By Lemma 3.1, each degree-zero summand can be varied to \(\mathcal O_X\), and the first can be varied to the fixed line bundle \(\mathcal O_X(dx)\). Products of the corresponding Picard stacks are connected, and direct sum gives a morphism from that product to the bundle stack. Thus all \(k\)-points in degree \(d\) belong to one connected component. Every nonempty component of a stack locally of finite type over an algebraically closed field contains such a point. The degree-\(d\) stack is therefore connected. Every integer occurs, through \(\mathcal O_X(dx)\oplus\mathcal O_X^{n-1}\), and local constancy separates distinct degrees. \(\square\)

For a general connected reductive group the component theorem is

\[
\pi_0(\operatorname{Bun}_G)\simeq
\pi_{1,\mathrm{alg}}(G):=X_*(T)/\langle\text{coroots}\rangle.
\]

Here \(T\) is a maximal torus. This is the algebraic fundamental group from the root datum, not the étale fundamental group of the variety \(G\). We use the general component theorem as an input [Drinfeld–Gaitsgory, §7.2.4]. The semisimple case also appears in [Beilinson–Drinfeld, §2.1.1] and [Heinloth, Theorem 2]. The vector-bundle proof above is independent of this input. For a torus the result follows directly from its cocharacter lattice and the Picard calculation.

## 4. Stability, bounded pieces, and growing stabilizers

A vector bundle \(E\) of positive rank has slope \(\mu(E)=\deg E/\operatorname{rk}E\). It is semistable if every nonzero proper subbundle \(F\) satisfies \(\mu(F)\le\mu(E)\), and stable if every such inequality is strict. Saturation lets us use subbundles rather than all subsheaves: saturation increases degree without changing rank, so it supplies the strongest test.

For a principal bundle, reductions to maximal proper parabolics replace subbundles. If \(P_0\subset G\) is such a parabolic and \(P_{P_0}\) is a reduction, let \(\mathfrak n_{P_0}\) be the Lie algebra of its unipotent radical. Our sign convention defines semistability by

\[
\deg\bigl((\mathfrak n_{P_0})_{P_{P_0}}\bigr)\le0
\]

for every reduction, and stability by strict inequality. For \(GL_n\), the reduction belonging to \(F\subset E\), with rank \(r\), has unipotent Lie bundle \(\operatorname{Hom}(E/F,F)\), of degree

\[
n\deg F-r\deg E.
\]

Thus the convention recovers slope stability. In root notation this degree is \(\langle2\rho_{P_0},\deg P_{P_0}\rangle\). This is the convention in [Gaitsgory–Raskin, §9.1]. For a torus there are no proper parabolics, so the stability test is vacuous.

The Harder–Narasimhan theorem gives a unique filtration of a vector bundle with semistable quotients of strictly decreasing slopes, and a corresponding canonical parabolic reduction for principal bundles [Drinfeld–Gaitsgory, Theorem 7.4.3]. We state this theorem, together with openness and boundedness: in a fixed topological component, the semistable locus is an open quasicompact substack [Drinfeld–Gaitsgory, §7.3.2, Proposition 7.3.5]. These are background stability results, not consequences merely of smoothness. The fixed-component qualification matters: the semistable locus of the entire Picard stack is an infinite disjoint union of degree components and is not quasicompact.

Consider now \(X=\mathbb P^1\) and \(E_d=\mathcal O\oplus\mathcal O(d)\), with \(d>0\). Relative to this order of summands,

\[
\operatorname{Aut}(E_d)=
\left\{\begin{pmatrix}a&0\\s&b\end{pmatrix}:
a,b\in k^\times,\quad s\in H^0(\mathbb P^1,\mathcal O(d))\right\}.
\]

Its dimension is \(2+(d+1)=d+3\). The diagonal entries must be units; their nonzero product is also sufficient for invertibility, since the lower triangular inverse is again of the displayed form. For \(d=0\) the group is \(GL_2\), of dimension four. For \(d<0\) interchange the summands, obtaining dimension \(|d|+3\).

This example varies degree. To see unboundedness even in a fixed degree, use

\[
E_m=\mathcal O(m)\oplus\mathcal O(-m),\qquad m>0.
\]

These all have degree zero, and their automorphism groups have dimension \(2m+3\). A quasicompact algebraic stack locally of finite type with finite type diagonal has a uniform bound on stabilizer dimensions: cover it by finitely many finite type charts, pull back the inertia, and use the bound on fibre dimensions of a finite type morphism. The dimensions \(2m+3\) contradict such a bound. Hence \(\operatorname{Bun}_2^0(\mathbb P^1)\) is not quasicompact.

The same mechanism works on any \(X\) in rank at least two: take \(L_m\oplus L_m^{-1}\oplus\mathcal O^{n-2}\), with \(\deg L_m=m\to\infty\). Riemann–Roch gives \(h^0(L_m^2)=2m+1-g\) once \(2m>2g-2\), yielding unbounded stabilizers in degree zero. This argument is sufficient for the vector-bundle example. It does not say that each fixed-degree Picard stack is nonquasicompact.

## 5. Cotangent vectors are Higgs fields

Dualizing Proposition 2.1 gives the cotangent complex. Its degree-zero cohomology at \(P\) is

\[
H^0(T_P^*\operatorname{Bun}_G)
=H^1(X,\operatorname{ad}(P))^*
\simeq H^0(X,\operatorname{ad}(P)^*\otimes\omega_X),
\]

by Serre duality. A cotangent vector is therefore a coadjoint-valued one-form, called a Higgs field. For \(GL_n\), the trace pairing identifies \(\operatorname{End}(E)^*\) with \(\operatorname{End}(E)\), so it is a map

\[
\phi:E\longrightarrow E\otimes\omega_X.
\]

This identifies the classical cotangent stack \(T^*\operatorname{Bun}_G\) with the stack of pairs \((P,\phi)\). It is more than a pointwise dimension calculation. For a family, relative Serre duality identifies a linear functional on \(R\pi_*\operatorname{ad}(P)[1]\) with a global section of \(\operatorname{ad}(P)^*\otimes\omega_{X\times S/S}\). This description commutes with base change and gives the required equivalence of moduli functors. It also explains why jumping \(h^0\) need not give an ordinary vector bundle over the whole stack. See [Beilinson–Drinfeld, §2.2.3] for the construction.

For \(GL_n\), expand the characteristic polynomial as

\[
\det(t-\phi)=t^n+a_1t^{n-1}+\cdots+a_n,
\qquad a_i\in H^0(X,\omega_X^i).
\]

The powers of \(\omega_X\) follow from homogeneity: the coefficient is homogeneous of degree \(i\) in the matrix entries of a one-form-valued endomorphism. The **Hitchin map** is

\[
h:T^*\operatorname{Bun}_n\longrightarrow
\mathcal A_n:=\bigoplus_{i=1}^nH^0(X,\omega_X^i),
\qquad (E,\phi)\longmapsto(a_1,\ldots,a_n).
\]

For general \(G\), choose homogeneous generators of \(k[\mathfrak g^*]^G\), with degrees \(d_1,\ldots,d_r\). They give a presentation of the Hitchin base as \(\bigoplus_jH^0(X,\omega_X^{d_j})\). The base itself is canonical; the choice of polynomial generators need not be. An invariant nondegenerate pairing can identify adjoint and coadjoint bundles, but the definition should not depend on an unstated choice of pairing.

For \(GL_2\), Riemann–Roch and Serre duality give

\[
\dim\mathcal A_2=
\begin{cases}
4g-3,&g\ge2,\\
2,&g=1,\\
0,&g=0.
\end{cases}
\]

Indeed \(h^0(\omega_X)=g\). For \(g\ge2\), \(h^1(\omega_X^2)=h^0(\omega_X^{-1})=0\) and \(h^0(\omega_X^2)=3g-3\). In genus one the canonical bundle is trivial, so both summands have dimension one. On the projective line they are \(\mathcal O(-2)\) and \(\mathcal O(-4)\), with no sections.

When \(g\ge2\), the base has dimension one more than \(\dim\operatorname{Bun}_2=4g-4\). This is compatible with the generic Higgs fibre: it is a Picard stack of a smooth spectral curve, not its Picard scheme. The double spectral cover has genus \(4g-3\), so its Picard stack has dimension \(4g-4\). On the stable bundle locus the coarse moduli dimension is also \(4g-3\), because scalar automorphisms have dimension one. Forgetting the scalar stabilizer in just one of these calculations creates the apparent discrepancy.

The spectral-curve statement in this paragraph is explanatory background: for a smooth spectral cover, the spectral correspondence identifies Higgs bundles with line bundles on it. The genus follows from Riemann–Hurwitz: a generic discriminant is a section of \(\omega_X^2\), with \(4g-4\) simple zeros, and \(2g_{\Sigma}-2=2(2g-2)+(4g-4)\). We use neither a spectral correspondence nor smoothness of a generic spectral curve in the proofs above.

## 6. The global nilpotent cone

The global nilpotent cone is the zero fibre

\[
\operatorname{Nilp}_G=h^{-1}(0)\subset T^*\operatorname{Bun}_G.
\]

For \(GL_n\), its points are Higgs fields with characteristic polynomial \(t^n\). Cayley–Hamilton then gives \(\phi^n=0\), interpreted as a map \(E\to E\otimes\omega_X^n\). Conversely a nilpotent Higgs field has all characteristic coefficients zero. If it is nilpotent over the function field, those coefficients vanish there and hence everywhere on the integral curve. Thus generic nilpotence and everywhere nilpotence agree for individual fields. A family is defined scheme-theoretically by the invariant-polynomial equations, retaining the zero fibre's possibly nonreduced structure.

The target theorem is that the reduced global nilpotent cone is Lagrangian in the cotangent stack for every connected reductive \(G\) and every genus. [Beilinson–Drinfeld, Theorem 2.10.4] gives the semisimple comparison in every genus; [Ginzburg, Main Theorem] gives the \(g>1\) argument and its reductive qualification. Sections 6.1–6.3 give the nilpotent Lie triple, canonical parabolic reduction and isotropy. Sections 6.4–6.12 prove the dimension equality in every genus, including the reductive central correction and an algebraic elliptic tensor/reduction argument. Bundle-stack algebraicity and the exact recursive Lie/flag/cohomology foundations remain required for full programme certification.

The word Lagrangian has a precise stack interpretation. If \(U\to\operatorname{Bun}_G\) is a smooth presentation, then

\[
\operatorname{Nilp}_G\times_{\operatorname{Bun}_G}U
\hookrightarrow
T^*\operatorname{Bun}_G\times_{\operatorname{Bun}_G}U
\hookrightarrow T^*U
\]

is Lagrangian after taking its reduction. The symplectic form vanishes on its smooth locally closed subvarieties, and its components have half the ambient dimension. This is independent of the presentation. A zero fibre of an arbitrary map from a symplectic space need not have these properties; the theorem is additional geometry.

For a torus, the invariant linear coordinates already force the Higgs field to be zero. The nilpotent cone is the zero section, which is Lagrangian in this presentation sense. For example, locally \(\operatorname{Bun}_{\mathbb G_m}^d\simeq\operatorname{Pic}^d\times B\mathbb G_m\). In a presentation \(\operatorname{Pic}^d\to\operatorname{Pic}^d\times B\mathbb G_m\), the cone becomes the zero section of \(T^*\operatorname{Pic}^d\), of dimension \(g\), even though the original stack has dimension \(g-1\).

Write \(M=\operatorname{Bun}_G(X)\), and let \(\mathcal N_G\) denote the reduced zero fibre of the invariant-polynomial Hitchin map. The theorem to prove is:

> For every smooth presentation \(a:A\to M\), the image of \(\mathcal N_G\times_M A\) in \(T^*A\) is isotropic and every one of its irreducible components has dimension \(\dim A\).

One uses reductions throughout. The scheme-theoretic zero fibre need not be reduced; “Lagrangian” here concerns its reduction. No stable-locus restriction is imposed.

Choose a \(G\)-invariant nondegenerate symmetric pairing on \(\mathfrak g\). Such a pairing is obtained from the Killing form on the semisimple derived algebra and any nondegenerate pairing on the centre. It identifies \(\operatorname{ad}(P)^*\) with \(\operatorname{ad}(P)\). The theorem and the zero fibre are independent of this auxiliary identification.

The cotangent description already proved in the lesson gives

\[
T^*M(S)=\{(P,\phi):\phi\in H^0(X_S,\operatorname{ad}(P)\otimes\omega_{X_S/S})\}.
\]

The form on \(T^*A\) is \(d\lambda_A\), where \(\lambda_A\) is the tautological one-form: on a tangent vector to a pair \((u,\xi)\), it evaluates \(\xi\) on the variation of \(u\). All later isotropy calculations use this formula, so there is no implicit sign convention.

### 6.1. The nilpotent Lie triple

The Lie argument uses Jordan decomposition, the Killing form, Cartan root spaces and the representation strings of \(\mathfrak{sl}_2\). Actual programme arguments include RT-LIE-03 Theorem 3.3 and Lemma 6.1/Theorem 6.2, the Jordan and complete-reducibility arguments in RT-LIE-04, and the algebraic rank-one module construction in RT-LIE-05 Proposition 2.2. RT-LIE-07's Cartan/root-space proof is written over \(\mathbb C\); a complete algebraic proof or field-transfer argument with the exact matching generality is still required for its use over every algebraically closed characteristic-zero field here. The following mechanism is conditional on that Lie foundation and the flag/parabolic, torsor-stack and curve-duality foundations; those obligations do not change the statement to be proved.

**Lemma 6.1.** Let \(\mathfrak s\) be a semisimple Lie algebra over an algebraically closed field of characteristic zero. For every nonzero nilpotent \(e\in\mathfrak s\), there are \(h,f\in\mathfrak s\) with

\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\]

**Proof.** Induct on \(\dim\mathfrak s\). First suppose that the centralizer \(\mathfrak s^e\) contains a nonzero semisimple element \(s\). The root-space decomposition, after putting \(s\) in a Cartan subalgebra, shows that \(\mathfrak l=\mathfrak s^s\) is a proper reductive algebra. Its centre is toral, and its derived algebra is semisimple. The nilpotent element \(e\) lies in \([\mathfrak l,\mathfrak l]\): its central component would otherwise be a nonzero commuting semisimple summand in its Jordan decomposition. Apply the induction hypothesis in \([\mathfrak l,\mathfrak l]\).

It remains to consider the case in which \(\mathfrak s^e\) has no nonzero semisimple element. Every element of \(\mathfrak s^e\) is then nilpotent, because its semisimple Jordan summand also centralizes \(e\).

Let \(\kappa\) be the Killing form. If \(z\in\mathfrak s^e\), then \(\operatorname{ad}e\) and \(\operatorname{ad}z\) commute; their product is nilpotent since \(\operatorname{ad}e\) is nilpotent. Consequently

\[
\kappa(e,z)=\operatorname{tr}(\operatorname{ad}e\operatorname{ad}z)=0.
\]

Invariance and nondegeneracy of \(\kappa\) give

\[
(\mathfrak s^e)^\perp=[e,\mathfrak s].
\]

Indeed the annihilator of \([e,\mathfrak s]\) is exactly the kernel of \(\operatorname{ad}e\), so the equality follows by taking annihilators. There is therefore an \(h_0\) such that \([h_0,e]=2e\). Replace \(h_0\) by its semisimple Jordan part \(h\). The Jordan decomposition of \(\operatorname{ad}h_0\) preserves its eigenvector \(e\), and on that eigenvector the semisimple part has eigenvalue \(2\) and the nilpotent part is zero. Thus \([h,e]=2e\).

Decompose \(z\in\mathfrak s^e\) into the eigenspaces of \(\operatorname{ad}h\). Every component \(z_m\) still centralizes \(e\), because \([e,z_m]\) has weight \(m+2\). For \(m\ne0\), invariance gives \(m\kappa(h,z_m)=\kappa(h,[h,z_m])=0\). The weight-zero component commutes with \(h\), and is nilpotent by the case assumption. Hence \(\operatorname{ad}h\operatorname{ad}z_0\) is nilpotent and \(\kappa(h,z_0)=0\). We obtain \(h\perp\mathfrak s^e\), so \(h=[e,y]\) for some \(y\). Taking the weight \(-2\) component of \(y\) gives \(f\) with \([e,f]=h\) and \([h,f]=-2f\). These are the required relations. \(\square\)

For a reductive algebra, nilpotent elements have zero central component, and the lemma applies to the derived algebra.

### 6.2. The canonical parabolic and its extension over the curve

**Lemma 6.2.** A nilpotent element in a reductive Lie algebra has a canonical decreasing filtration \(F^j\), and \(F^0\) is a parabolic algebra whose nilradical contains the element. The filtration is preserved by scalar multiplication of the element and descends over any characteristic-zero field and any inner form.

**Proof.** Put \(N=\operatorname{ad}e\). For a nilpotent linear operator define, using only kernels, images, intersections, and sums,

\[
F^j V=\sum_{i\ge\max(0,-j)}\bigl(\ker N^{i+1}\cap\operatorname{im}N^{i+j}\bigr).
\tag{6.1}
\]

Terms with exponent larger than the nilpotence index vanish, so this is a finite sum. On a Jordan block of length \(n+1\), choose the weights \(-n,-n+2,\ldots,n\), with \(N\) raising the weight by two. Direct inspection of that block shows that (6.1) is the span of the vectors of weight at least \(j\). The calculation is independent of a chosen Jordan basis, because the right side of (6.1) is intrinsic.

Use Lemma 6.1 on \(\mathfrak g\). The decomposition into \(\mathfrak{sl}_2\)-modules shows that \(F^j\mathfrak g\) is precisely the sum of the \(h\)-weight spaces with weight at least \(j\). In particular, \(e\in F^2\mathfrak g\). After putting \(h\) in a Cartan subalgebra, its root values are integers. A positive integer multiple of \(h\) is the differential of a cocharacter: this follows by clearing denominators in the cocharacter lattice of the torus. The root-space description of the parabolic of that cocharacter gives its Lie algebra \(F^0\mathfrak g\) and its nilradical \(F^1\mathfrak g\). Moreover

\[
(F^0\mathfrak g)^\perp=F^1\mathfrak g,
\tag{6.2}
\]

because an invariant pairing matches only opposite \(h\)-weights.

The stabilizer in \(G\) of the complete filtration is this parabolic: its positive-root subgroup preserves the filtration, and a filtration-preserving element normalizes \(F^0\mathfrak g\), whose normalizer is the parabolic itself by the root-space description. Formula (6.1) is defined over the field of definition of \(e\), and is unchanged when \(e\) is multiplied by a nonzero scalar. Thus its parabolic stabilizer descends. The same argument works for an inner form after passing to an algebraic closure and descending the intrinsic filtration. No generic trivialization of the original torsor is required. \(\square\)

**Lemma 6.3.** Every nilpotent Higgs field \((P,\phi)\) has a reduction to some parabolic \(Q\subset G\) such that \(\phi\) lies in the nilradical bundle of that reduction.

**Proof.** At the function field of \(X\), trivialize the canonical line and apply Lemma 6.2 in the inner Lie algebra \(\operatorname{ad}(P)\). Scalar invariance removes dependence on that trivialization. The resulting parabolic is a point of the associated projective flag bundle \(P/Q\). Properness extends its section across each missing point of the nonsingular curve, by the valuative criterion for the local DVRs. The projection of \(\phi\) to the quotient by the nilradical vanishes generically, and is a regular section of a vector bundle. It therefore vanishes everywhere. \(\square\)

The same construction has the following spreading property. If a reduced irreducible finite-type scheme \(S\) carries a nilpotent Higgs family, perform the construction on the curve over \(k(S)\). The reduction, defined on the entire generic fibre of the curve, spreads to \(X\times S_0\) for some nonempty open \(S_0\subset S\), since the flag bundle and the section have finite presentation. After shrinking \(S_0\), the vanishing in the quotient by the nilradical also spreads. Noetherian induction gives a finite stratification of a finite-type parameter scheme with a reduction on every stratum. This argument replaces the countable-cover argument in Ginzburg and works over countable algebraically closed fields as well.

### 6.3. Vanishing of the tautological one-form

For a fixed parabolic \(Q\), let \(f:\operatorname{Bun}_Q\to\operatorname{Bun}_G\) forget the reduction. The deformation calculation of the lesson applies to \(Q\) as a smooth affine group as well: its obstruction group is \(H^2(X,\mathfrak q_P)=0\), so \(\operatorname{Bun}_Q\) is smooth once its algebraicity is established by the same torsor-stack argument. Duality identifies the pullback of a Higgs covector along \(df\) with its image in

\[
H^0(X,\mathfrak q_P^*\otimes\omega_X).
\]

By (6.2), this pullback is zero when the Higgs field belongs to the nilradical bundle.

Take a smooth presentation \(A\to M\), and write \(N=A\times_M\operatorname{Bun}_Q\). It is smooth, because \(N\to\operatorname{Bun}_Q\) is the smooth base change of \(A\to M\). Let \(F:N\to A\) be the projection. A covector \(\xi\in T_u^*A\) coming from the cotangent stack pulls back to zero along \(dF\) exactly when the original Higgs field pulls back to zero along \(df\).

Now let \(W\) be an irreducible smooth locally closed subvariety of \(\mathcal N_G\times_M A\). The spreading argument gives a nonempty open \(W_0\subset W\) and a map \(r:W_0\to N\) carrying its canonical parabolic reduction. At a tangent vector \(v\in T_wW_0\),

\[
(\lambda_A|_{W_0})(v)
=\xi\bigl(dF(dr(v))\bigr)=0.
\]

Thus \(d\lambda_A\) vanishes on \(W_0\). It vanishes on all of \(W\), because it is a regular two-form and \(W_0\) is dense. Repeating on irreducible components proves isotropy on every smooth locally closed subvariety. In particular every irreducible component of the reduced cone in \(T^*A\) has dimension at most \(\dim A\).

This proves isotropy for every connected reductive \(G\), in every genus, in algebraic characteristic zero. It does not appeal to Steinberg's generic torsor-triviality theorem or to a countable-union assertion.

The cone controls allowed automorphic singularities in later lessons. Its role here is to give a geometric condition on covectors; it is not yet the spectral singular-support condition on the derived stack of local systems.

The ground field in the main statement is **algebraically closed of characteristic zero**. The curve \(X\) is smooth, projective and connected, and \(G\) is connected reductive. Put \(M=\operatorname{Bun}_G(X)\). For a smooth presentation \(a:A\to M\), work on an open on which \(A\) is a smooth finite-type scheme and the relative dimension of \(a\) is \(m\). Write \(n=\dim A\). The cotangent pullback has its usual closed immersion into \(T^*A\). Let \(N_A\) be the reduction of the image of the global nilpotent cone under this immersion.

**Dimension theorem, conditional on the exact stack and programme foundations in N0.** Every irreducible component of \(N_A\) has dimension \(n\). Together with the already written chartwise isotropy proof, this says that the reduced global nilpotent cone is Lagrangian for every genus and every connected reductive \(G\).

We prove the three genus cases below. In genus one, we construct the necessary adjoint Harder–Narasimhan reduction from vector bundles. We do not assume the principal Harder–Narasimhan theorem, the equivalence between Ramanathan semistability and adjoint semistability, or a theorem about tensor products of semistable bundles. No countability argument is used.

### 6.4. Precise foundations and the chart (N0)

The argument uses the local Lie/parabolic and isotropy proofs above and the exact earlier programme arguments specified below. Their remaining recursive foundations retain the stated proof obligations.

* The algebraicity of \(M\), its finite-type diagonal and local finite presentation remain the lesson's representability foundation. Their present source is Heinloth, Proposition 1. A source citation alone does not certify that foundation under the current policy. Smoothness and the tangent complex are the lesson's Čech deformation calculation: \(T_{M,P}=R\Gamma(X,\operatorname{ad}P)[1]\). On a curve the obstruction \(H^2\) is zero.
* The local canonical nilpotent filtration and its isotropy proof have actually been written in GL-GLC-02, §6.1–6.3. Thus every component of \(N_A\) has dimension at most \(n\), after its indicated Lie/group and geometric foundations are supplied. N7 below gives an algebraic torus argument for the Lie-of-\(G\) semisimple centralizer step, using the actual all-field AG-RG arguments, so a complex-only Cartan argument need not be transferred silently.
* Actual AG-QC-03 supplies affine vanishing and finite affine Čech computation; actual AG-QC-05, Theorem 2.1 and Corollary 2.3, supplies relative Serre generation and projective cohomological finiteness; actual AG-QC-08, Lemma 3.1 and Theorem 3.2, supplies the universal finite projective cohomology complex for flat coherent families. Actual AG-QC-15, Theorems 4.1–4.2, supplies projective duality. The local Koszul calculation identifying the dualizing line of a smooth curve with \(\Omega_X^1\) is recalled below. Actual AG-HP-05, Theorem 4.1 and Corollary 4.2, supplies the projective Quot and Hilbert schemes. Actual AG-HP-09, Theorem 2.1, Proposition 5.1 and Theorem 6.2, supplies normalized line bundles and the smooth Picard scheme. These are actual arguments read in the indicated revisions, not specifications.
* The Lie and group ingredients used here are actual RT-LIE-02–05 and the characteristic-zero extension sections of RT-LIE-11 and RT-LIE-14, together with actual AG-RG-01, AG-RG-03–06. In particular, Engel's triangularization is actual RT-LIE-02, Theorem 2.1; the all-base parabolic parameter scheme and its projective quotient are actual AG-RG-06, Theorems 1.1–2.1. The evidence distinguishes these arguments from their remaining foundational imports.

For a smooth morphism \(A\to M\), let \(E=T_{A/M}\), a vector bundle of rank \(m\), and let \(\rho:E\to T_A\) be its differential. The classical cotangent pullback is

\[
T^*M\times_M A=\{(x,\xi):\xi\circ\rho_x=0\}\subset T^*A. \tag{N0.1}
\]

Indeed the cotangent triangle \(a^*L_M\to L_A\to L_{A/M}\), dualized, says precisely that a functional on \(T_A\) comes from a degree-zero cotangent vector of \(M\) if and only if it kills the relative tangent bundle. This identifies the functors on arbitrary ordinary test schemes, rather than just their geometric fibres. Locally (N0.1) is the zero locus of \(m\) scalar functions, with relations whenever \(\rho\) has a kernel.

Let \(z=\dim Z(G)^0\). The invariant decomposition \(\mathfrak g=\mathfrak z\oplus[\mathfrak g,\mathfrak g]\) gives a constant central summand \(\mathfrak z\otimes\mathcal O_X\) in every adjoint bundle. The boundary map in the tangent triangle embeds \(\mathfrak z\otimes\mathcal O_A\) into \(E\), and its composite with \(\rho\) is zero. Its fibre is the injection of the infinitesimal central automorphisms into the relative tangent space; hence it is a locally direct summand of \(E\). Consequently (N0.1) needs at most \(m-z\) equations locally. This is an identity of bundle maps over \(A\), including nonreduced test schemes.

For later use, here is the elementary Riemann–Roch calculation. A rational nonzero section of a line bundle \(L\) identifies it with \(\mathcal O_X(D)\). The exact sequence for adding one point changes its Euler characteristic by one. Since \(\chi(\mathcal O_X)=1-g\), this proves \(\chi(L)=\deg L+1-g\). A vector bundle has a saturated line subbundle: extend a nonzero vector of its generic fibre, then saturate; torsion-free sheaves on a nonsingular curve are locally free. Induction on rank and additivity prove

\[
\chi(V)=\deg V+(1-g)\operatorname{rk}V. \tag{N0.2}
\]

The identification of the dualizing line with \(\Omega_X^1\) is local: embed \(X\) in a smooth projective space, use the regular conormal sequence, and resolve its ideal by the local Koszul complex. Its top dual term is \(\det(I/I^2)^\vee\otimes\omega_{\mathbf P}|_X\). The determinant of \(0\to I/I^2\to\Omega_{\mathbf P}|_X\to\Omega_X\to0\) identifies that line with \(\Omega_X\); the Koszul identifications agree under change of regular generators. Thus AG-QC-15 duality gives \(h^0(\omega_X)=g\), \(h^1(\omega_X)=1\), and (N0.2) gives \(\deg\omega_X=2g-2\). In genus one a nonzero section of \(\omega_X\) has no zeros, so \(\omega_X\simeq\mathcal O_X\).

For arbitrary ordinary bases, the finite cohomology complex just cited still applies to the vector bundles used here. On an affine \(\operatorname{Spec}A\), choose a finite affine cover \(\operatorname{Spec}R_i\) of the fixed curve. Refine its base changes by finitely many distinguished opens on which the vector bundle is trivial. The distinguished-open equations, transition matrices, their inverses, and cocycle relations involve only finitely many coefficients of \(A\). Include also the finitely many unit-ideal identities proving that these opens cover each \(\operatorname{Spec}(R_i\otimes_kA)\). All this data is defined over a finitely generated \(k\)-subalgebra \(A_0\subset A\). The unit-ideal identities ensure that the descended opens still cover, and the matrix identities glue a vector bundle on \(X_{A_0}\) whose pullback is the original one. The actual AG-QC-08 argument gives a finite projective \(K_0\) computing cohomology after every \(A_0\)-algebra change. Pull it back to \(A\). Whenever fibre cohomology is zero outside degree zero, split off the contractible pairs corresponding to invertible differential entries near each parameter point. The remaining terms have zero fibre rank except in degree zero, so disappear there; the degree-zero term is locally free. Every cancellation remains valid after every tensor. This proves the locally free pushforward and arbitrary base-change claims used later, even for non-Noetherian or nonreduced \(A\). The construction concerns the cohomology complex; it never assumes that its individual cohomology sheaves always commute with base change.

The adjoint determinant of connected reductive \(G\) is trivial: on a maximal torus its weights are the roots in opposite pairs and zero weights, and root groups admit no nontrivial multiplicative character. Therefore every \(\operatorname{ad}P\) has degree zero. The Čech tangent calculation and (N0.2) give

\[
\dim M=(g-1)\dim G=:d,\qquad n=d+m. \tag{N0.3}
\]

### 6.5. Genus at least two, including the centre (N1)

We include the invariant degree calculation so that the required count is explicit. For the simply connected semisimple group with the same derived Lie algebra, let \(T\) be a maximal torus and \(W\) its Weyl group. Its fundamental representation characters \(\chi_i\) freely generate \(k[T]^W\). To prove this, use orbit sums of dominant weights as a basis. A monomial in the fundamental characters has a unique highest dominant weight, of coefficient one, and lower remaining weights. Induction in the dominance order proves generation, and distinct leading weights prove independence. The induction is finite because an interior positive coroot bounds the dominant weights below a fixed weight. The required representations have been constructed over characteristic-zero fields in the actual highest-weight and AG-RG arguments recorded in the evidence.

Complete at \(1\in T\). The formal exponential is \(W\)-equivariant and identifies this completed invariant algebra with \(k[[\mathfrak t^*]]^W\). It is a regular local ring of dimension \(r=\operatorname{rk}G_{\mathrm{der}}\), because the character algebra is polynomial. Hence the graded algebra \(k[\mathfrak t]^W\) has \(r\) indecomposable positive-degree generators. Choose a homogeneous basis of its maximal ideal modulo its square. Induction on degree shows that it generates; the dimension shows algebraic independence.

They extend to the Lie algebra: the homogeneous coefficients in

\[
\chi_i(\exp H)=\sum_{j\ge0}\operatorname{tr}(\rho_i(H)^j)/j!
\]

are restrictions of invariant polynomials on \(\mathfrak g\), and span the indecomposable quotient just used. Regular semisimple elements are dense and conjugate into \(\mathfrak t\), so restriction is injective as well. We obtain homogeneous invariant generators \(Q_i\), of degrees \(d_i\ge2\), for the derived Lie algebra.

The Jacobian of the quotient \(\mathfrak t\to\mathfrak t/W\) has simple zeros exactly on the root hyperplanes. Off these hyperplanes stabilizers are trivial; generically on one hyperplane the stabilizer is its order-two reflection, whose local quotient is \((u_1,u_2,\ldots)\mapsto(u_1^2,u_2,\ldots)\). Thus the Jacobian divisor gives

\[
\sum_i(d_i-1)=|\Phi^+|,\qquad
\sum_i(2d_i-1)=\dim G_{\mathrm{der}}. \tag{N1.1}
\]

These stabilizer assertions can be checked in the real reflection representation of the rational root datum. If a Weyl element fixes a regular complex vector, it fixes its real and imaginary parts, hence a regular real combination, and therefore a chamber, whose stabilizer is trivial. Generically on a single wall only its reflection remains. The matrices and closed exceptional loci are defined over the rational root datum, so their verified identities extend to every characteristic-zero field; no embedding of the given \(k\) into \(\mathbb C\) is assumed.

Add \(z\) central degree-one generators. Their common zero locus with the derived generators is the nilpotent cone. For completeness, the local Jacobson–Morozov proof gives a cocharacter contracting a nilpotent element and forces every positive-degree invariant to vanish there. For the converse, take the Jordan decomposition and contract the nilpotent part inside the reductive centralizer of the semisimple part. Every invariant has the same value on the element and its semisimple part. Finite Weyl invariants have zero fibre only at zero: for a nonzero vector choose a linear form nonzero on every point of its finite orbit and take the product of its Weyl translates. Thus the semisimple part and the central part must vanish.

For \(g\ge2\), duality and (N0.2) give

\[
\begin{aligned}
D:=\dim\mathcal A_G
&=\sum_i(2d_i-1)(g-1)+zg\\
&=(g-1)\dim G+z=d+z.
\end{aligned} \tag{N1.2}
\]

Each higher-degree differential has no first cohomology because its Serre-dual line has negative degree. The centre contributes \(zg\), rather than \(z(g-1)\).

The zero Hitchin fibre imposes \(D\) scalar equations on (N0.1). After lifting these functions locally to \(T^*A\), its ideal has at most

\[
(m-z)+(d+z)=m+d=n
\]

generators. The actual Krull height theorem is AG-CA-11, Theorem 3.1: a prime minimal over an ideal generated by \(n\) elements has height at most \(n\). Applied in the smooth \(2n\)-dimensional chart, with the finite-type dimension formula of actual AG-CA-09, it shows that every component has dimension at least \(n\). Isotropy gives the reverse bound. This proves the theorem for \(g\ge2\).

### 6.6. Genus zero on an arbitrary smooth presentation (N2)

In genus zero \(\deg\omega_X<0\), so every \(H^0(X,\omega_X^j)\), \(j>0\), vanishes. Hence the Hitchin base is zero and the global nilpotent cone is the full classical cotangent stack, after reduction.

We prove the needed lower bound without assuming a quotient presentation or classifying all bundles on a rational curve.

**Smooth groupoid lemma.** Let \(Y\) be a smooth algebraic stack locally of finite type over an algebraically closed characteristic-zero field, with finite-type diagonal and affine stabilizers. In a smooth finite-type presentation \(A\to Y\), every irreducible component of the image of \(T^*Y\times_Y A\) in \(T^*A\) has dimension at least \(\dim A\). The affine stabilizers of bundle stacks have the matrix smoothness proof in N7.

**Proof.** Put \(R=A\times_Y A\), with its smooth source and target maps; if it is an algebraic space use étale scheme charts for the following local constructions. For \(x\in A(k)\), its groupoid orbit \(O_x\subset A\) is smooth and locally closed. Here are the details of this assertion. Its image from the finite-type source fibre \(R_x\) is constructible, so contains a dense open in its reduced closure. At an arrow of \(R\), the kernels of the source and target differentials have the same dimension. Choose a common complementary tangent subspace and cut out a smooth local slice through the arrow with that tangent space. Both maps from this slice to \(A\) are étale after shrinking. Such local correspondences preserve the condition of belonging to \(O_x\); because étale maps are open they also preserve its reduced closure. They transport the dense open just found to a neighbourhood of every orbit point. Thus \(O_x\) is open in its closure and is locally closed. Generic smoothness in characteristic zero, followed by the same correspondences, transports a smooth open to every point of the orbit, proving smoothness. Finally the differential of \(R_x\to O_x\) is surjective: its rank is constant, since its fibres are translates of the same smooth stabilizer, and generic smoothness gives the rank equal to \(\dim O_x\).

At \(x\), the image of \(T_{A/Y,x}\to T_{A,x}\) is exactly \(T_{O_x,x}\). The equation (N0.1) therefore says that its cotangent fibre consists of the annihilator of this orbit tangent space. Consequently the entire conormal bundle \(T^*_{O_x}A\) belongs to the cotangent pullback. Each of its components has dimension \(\dim A\).

To deduce a bound for **each** component of the whole closed cone, select a closed point on that component outside the other components. The conormal bundle through this point has an irreducible component of dimension \(\dim A\). Its closure in \(T^*A\) lies in one component of the cone; the selected point forces that component to be the one selected. Its dimension is at least \(\dim A\). This avoids the invalid inference from a maximum of local component dimensions at an intersection. The existence of the selected closed point follows from the Jacobson property of a finite-type scheme over the algebraically closed field. \(\square\)

Apply the lemma to \(M\). Isotropy bounds every component by \(n\), so every component has dimension \(n\). The central torus and negative stack dimension cause no exception. No finiteness of the number of orbits, no principal-bundle classification on \(\mathbf P^1\), and no assertion of a quotient chart was used.

### 6.7. Vector bundles on a genus-one curve (N3)

Choose a nonzero differential and identify \(\omega_X\) with \(\mathcal O_X\). All bundles and morphisms in this section are algebraic. The slope of a nonzero bundle \(V\) is \(\mu(V)=\deg V/\operatorname{rk}V\); it is semistable if every subbundle has slope at most \(\mu(V)\).

### N3.1. Slope facts and existence of the vector filtration

If \(V,W\) are semistable and \(\mu(V)>\mu(W)\), every morphism \(V\to W\) is zero. For a nonzero image \(I\), its quotient description in \(V\) gives \(\mu(I)\ge\mu(V)\), while its saturation in \(W\) gives \(\mu(I)\le\mu(W)\), a contradiction. The same argument proves that a dual of a semistable bundle is semistable, and that an extension of semistable bundles of one slope is semistable: intersect any subbundle with the first term and take its image in the quotient, and add the degree inequalities.

The vector Harder–Narasimhan filtration follows directly from the maximum-slope construction. Embed \(V\) in \(\mathcal O_X(N)^b\) using global generation of a sufficiently large twist of \(V^\vee\). A rank-\(i\) subbundle has degree at most \(i\deg\mathcal O_X(N)\), by its determinant injection into the corresponding exterior power. The possible ranks are finite, and the degrees are integers bounded above, so a maximum slope is attained. Choose a subbundle of maximum slope and, among those, maximum rank. It is saturated, since saturation would increase its slope. It is semistable. Every nonzero subbundle of the quotient has smaller slope; otherwise its inverse image would contradict maximum slope or maximum rank. Induction constructs a filtration with semistable quotients of strictly decreasing slope.

Uniqueness uses the vanishing just proved. A maximum-slope subbundle maps to zero in the quotient by another such maximal-rank subbundle, whose maximum slope is strictly smaller. Thus the two first terms coincide. Repeat in the quotient. In particular, every automorphism of \(V\) preserves its filtration, and dualizing reverses the slopes and the filtration.

For a finite-type family, the same embedding can be chosen uniformly on a finite affine cover of the parameter scheme, by relative Serre generation. Semistability is open, with an actual parameter-space proof: for each rank \(i\), only finitely many integers

\[
i\mu(V)<e\le i\deg\mathcal O_X(N)
\]

can occur as the degree of a destabilizing subsheaf. The projective Quot scheme of quotients of rank \(\operatorname{rk}V-i\) and degree \(\deg V-e\) has closed image on the parameter scheme. A kernel of one of these quotients is torsion-free, and its saturation still destabilizes. Conversely every destabilizing subbundle supplies such a quotient. Therefore the finite union of these closed images is exactly the nonsemistable locus. This proves openness over schemes, including their nonreduced structure; no representability of a principal semistability locus has been assumed.

### N3.2. Degree-zero semistable bundles have line filtrations

**Lemma.** Every degree-zero semistable vector bundle \(V\) on \(X\) has a filtration by degree-zero line bundles.

**Proof.** Fix \(y\in X(k)\). The bundle \(V(y)\) is semistable of slope one. Duality and slope vanishing give \(H^1(V(y))=\operatorname{Hom}(V(y),\mathcal O_X)^\vee=0\). Riemann–Roch gives \(h^0(V(y))=r=\operatorname{rk}V\).

Take the evaluation map \(H^0(V(y))\otimes\mathcal O_X\to V(y)\). If it has generic rank less than \(r\), it has a nonzero kernel at some point \(x\). If it has generic rank \(r\), its determinant is a nonzero section of the line \(\det V(y)\), of degree \(r>0\), and so vanishes at some point \(x\). Again the evaluation at \(x\) has a nonzero kernel. In either case there is a nonzero section of \(V(y-x)\).

Its image from \(\mathcal O_X\) has a saturated line bundle of nonnegative degree. Semistability of the degree-zero bundle \(V(y-x)\) bounds that degree by zero. Thus the image was already saturated and has degree zero. Untwisting gives a degree-zero line subbundle in \(V\). The quotient has degree zero and is semistable: a positive-degree subbundle of the quotient would have a positive-degree inverse image in \(V\). Induction proves the lemma. \(\square\)

Tensor products of two such bundles consequently have filtrations by degree-zero lines: tensor the first filtration with the second and refine it by the second filtration. The extension slope argument proves semistability of their tensor product.

### N3.3. A finite étale cover clearing any denominator

We need tensor semistability also for rational, possibly nonzero, slopes. The following construction supplies the cover without importing a degree formula for multiplication on an elliptic curve.

With an origin \(o\), the map \(x\mapsto\mathcal O_X(x)\) identifies \(X\) with \(\operatorname{Pic}^1_X\) on **all ordinary test schemes**. Indeed every degree-one line has exactly one section and zero first cohomology. Its pushforward in a family is a line bundle, compatible with arbitrary base change. Evaluation defines a relative effective Cartier divisor finite flat of degree one. Such a divisor is the graph of a unique section: its rank-one finite flat algebra is the base algebra, since its unit is an isomorphism on every fibre and hence an isomorphism. The normalized line recovered from that divisor is the original one. This is also the genus-one specialization of the actual evaluation argument in AG-HP-09, Proposition 5.1. Tensoring by \(\mathcal O_X(-o)\) identifies \(X\) with the proper group scheme \(J=\operatorname{Pic}^0_X\).

For any prime \(\ell\), multiplication \([\ell]:J\to J\) is étale, since its differential is multiplication by the nonzero scalar \(\ell\), at the identity and therefore at every point by translation. It is nonconstant, proper and finite. It cannot have degree one. To see this without an isogeny-degree theorem, the line \(\mathcal O_X(3o)\) is very ample: Riemann–Roch and duality separate every subscheme of length two. It embeds \(X\) as a smooth plane cubic. Every automorphism fixing \(o\) acts projectively on this embedding and belongs to the closed subgroup of \(\operatorname{PGL}_3\) preserving the cubic and \(o\). Its tangent space injects into \(H^0(X,T_X(-o))=H^0(X,\mathcal O_X(-o))=0\). This algebraic group has dimension zero, hence finitely many geometric points. Thus every origin-preserving automorphism has finite order. Were \([\ell]\) an automorphism, some power would be the identity, whereas its differential would be \(\ell^a\), impossible in characteristic zero.

The nontrivial finite étale kernel of \([\ell]\) therefore contains a point of exact order \(\ell\), yielding a nontrivial line bundle \(L\in\operatorname{Pic}^0_X\) of exact order \(\ell\). A choice \(L^{\ell}\simeq\mathcal O_X\) defines

\[
Y=\operatorname{Spec}_X\left(\bigoplus_{j=0}^{\ell-1}L^j\right)\longrightarrow X. \tag{N3.1}
\]

Locally its equation is \(u^\ell=a\), with \(a\) invertible; its derivative is invertible, so it is finite étale of degree \(\ell\). It is connected because every nontrivial degree-zero \(L^j\) has no section, giving \(H^0(Y,\mathcal O_Y)=k\). It is a smooth proper connected genus-one curve: \(\omega_Y=p^*\omega_X\simeq\mathcal O_Y\), and duality gives genus one. It is a cyclic Galois cover, with deck transformations multiplying the local root by an \(\ell\)-th root of unity.

Repeating (N3.1) on successive genus-one curves produces a finite étale tower whose total degree is divisible by any prescribed integer. Pullback across each cyclic cover preserves semistability. If the pullback were unstable, its unique first Harder–Narasimhan subbundle would be deck-invariant; its inherited descent datum satisfies the cocycle because the subbundle is uniquely determined as a subbundle. Here is the descent as an actual subbundle. On an affine open \(\operatorname{Spec}A\subset X\), write its cyclic cover as \(\operatorname{Spec}B\), with deck group \(\Gamma\) of order \(\ell\). For the invariant subbundle \(W\subset B\otimes_AV\), put \(N=W^\Gamma\). Averaging by \(\ell^{-1}\sum_{\gamma\in\Gamma}\gamma\) is an \(A\)-linear idempotent. Thus \(N\) is finite projective over \(A\): \(W\) is finite projective over the finite projective \(A\)-algebra \(B\), and averaging makes \(N\) a direct summand. The quotient \((B\otimes_AV)/W\) is also finite projective, and exactness of averaging gives a finite projective quotient of \(V\) by \(N\). The map \(B\otimes_AN\to W\) is an isomorphism. This can be checked after the faithfully flat change \(A\to B\): the explicit cyclic-root identity \(B\otimes_AB\simeq\prod_{\gamma\in\Gamma}B\) splits the cover, its deck action permutes the factors, and invariants are the diagonal copy with the prescribed deck identifications. Faithful flatness detects the kernel and cokernel of the map. These invariant subbundles glue on overlaps and recover \(W\) after pullback. Finally the degree of a pulled-back line is \(\ell\) times its degree, since the pullback of a divisor has \(\ell\) points counted with multiplicity above each point. Apply this to determinants. The descended destabilizing subbundle therefore has slope equal to the upstairs slope divided by \(\ell\), contradicting semistability below. Conversely a destabilizing subbundle below pulls back to a destabilizing one, so semistability of the pullback also implies semistability below.

Choose such a tower of degree \(D\) clearing the denominators of the slopes of semistable \(V,W\). On its top curve, twist \(p^*V\) and \(p^*W\) by lines of respective degrees \(-D\mu(V)\) and \(-D\mu(W)\), which exist by using multiples of one point. The results are degree-zero semistable bundles. By N3.2 their tensor product is semistable of degree zero. Undo the twists and descend to prove:

**Tensor lemma.** On a genus-one curve in algebraic characteristic zero, the tensor product of semistable bundles is semistable, of the sum of their slopes.

Finally, the tensor filtration of any two Harder–Narasimhan filtrations has graded pieces which are these tensor products. Order the sums of slopes and group equal sums. The extension slope argument shows that this convolution is itself the Harder–Narasimhan filtration. A map from a bundle all of whose slopes are at least \(a\) to a bundle all of whose slopes are below \(a\) is zero, by successive use of the slope vanishing in N3.1.

### 6.8. The adjoint filtration gives the elliptic parabolic reduction (N4)

Let \(E=\operatorname{ad}P\), and use a nondegenerate invariant form, the Killing form on the derived algebra and any nondegenerate form on the centre. Write \(F^{\ge a}E\) for the part of its Harder–Narasimhan filtration of slopes at least \(a\), with \(F^{>a}\) defined similarly. The central summand is constant and has slope zero.

The tensor lemma and the uniqueness of the tensor filtration imply

\[
[F^{\ge a}E,F^{\ge b}E]\subset F^{\ge a+b}E. \tag{N4.1}
\]

Indeed the source of the bracket has all slopes at least \(a+b\), and the quotient by the proposed target has all slopes below \(a+b\). Its induced morphism to that quotient is zero. Self-duality of the filtration gives

\[
(F^{>0}E)^\perp=F^{\ge0}E. \tag{N4.2}
\]

Put \(\mathcal U=F^{>0}E\) and \(\mathcal Q=F^{\ge0}E\). Fibrewise, \(\mathcal U_x\) is a Lie algebra of nilpotent elements: its elements strictly raise the finite filtration of \(E_x\) under the adjoint action, by (N4.1). It has zero intersection with the reductive centre. The representation-preservation of Jordan decomposition, actually proved in RT-LIE-04, therefore makes it nilpotent in a faithful representation of the derived group as well.

Here is the algebraic integration used at this point. Engel triangularization puts its nilpotent representation in strictly upper triangular matrices. The finite polynomial exponential and logarithm identify its Lie algebra with a closed connected unipotent matrix group; closure and the group law follow from the finite Baker–Campbell–Hausdorff formula. That group belongs to \(G\). For a nilpotent \(v\in\mathfrak g\), the left invariant derivation defined by \(v\) preserves the defining ideal of \(G\) in a faithful matrix embedding, and its finite exponential on matrix coordinates proves \(\exp(tv)\in G\). Apply this to every \(v\in\mathcal U_x\). This is a polynomial calculation, not an analytic exponential.

A connected unipotent group is contained in a maximal connected solvable subgroup \(B\), by increasing dimension among connected solvable subgroups. Its projection to the torus quotient of \(B\) is trivial. Thus \(\mathcal U_x\) lies in the nilradical \(\mathfrak n_B\). By (N4.2), \(\mathcal Q_x\) contains \(\mathfrak n_B^\perp=\mathfrak b\).

Here is a group-level proof that this Lie subalgebra \(\mathfrak q=\mathcal Q_x\) is parabolic, avoiding a tacit integration assertion for an arbitrary subalgebra. Let \(H\) be its closed Grassmannian stabilizer in \(G\). Its Lie algebra is the Lie normalizer of \(\mathfrak q\). The latter equals \(\mathfrak q\): its quotient by \(\mathfrak q\) is annihilated by \(\mathfrak q\), whereas a Cartan algebra in \(\mathfrak b\) has no zero weights in \(\mathfrak g/\mathfrak q\), since \(\mathfrak q\) contains the whole Cartan algebra and is stable under it. The formal matrix argument in N7 makes \(H\), and \(H\cap B\), smooth. Their Lie-algebra intersection is \(\mathfrak b\), so \(H\cap B\) has the full dimension of the connected \(B\), and equals \(B\). Hence \(Q=H^0\) contains \(B\). Actual AG-RG-06, Theorem 1.1, classifies such connected subgroups as standard parabolic groups. We have \(\operatorname{Lie}Q=\mathfrak q\). Its nilradical is \(\mathfrak q^\perp\), which is exactly \(\mathcal U_x\).

Let \(H\) be the full Grassmannian stabilizer of \(\mathfrak q\). The preceding argument gives \(H^0=Q\). Every element of \(H\) normalizes its identity component \(Q\). Actual AG-RG-06, Theorem 1.1, proves the scheme-theoretic equality \(N_G(Q)=Q\); hence \(H=Q\). Thus the orbit map \(G/Q\to\operatorname{Gr}(\mathfrak g)\) is a monomorphism, with injective differential. It is proper because \(G/Q\) is projective, so is a closed immersion. The parameter scheme of parabolic Lie algebras is the finite disjoint union of these closed conjugacy orbits. Since \(X\) is connected, the type is constant. The map from the reduced curve to the Grassmannian factors scheme-theoretically through that orbit, because its defining equations vanish at all geometric points. It defines a \(Q\)-reduction of \(P\), on the entire curve. This is a construction from the existing vector filtration, not an assumed principal reduction theorem.

We need the other terms of the filtration as well. At one fibre choose a maximal torus \(T\subset Q\). By (N4.1), every \(F^{\ge a}E_x\) is stable under \(\mathfrak q\), hence under the connected group \(Q\); in characteristic zero Lie stability implies group stability by differentiating the Grassmannian stabilizer. Torus stability decomposes each term into root lines and, at weight zero, the Cartan algebra. The entire Cartan has filtration weight zero. It is contained in \(F^{\ge0}E_x=\mathfrak q\), while its intersection with \(F^{>0}E_x\) is zero: the latter consists of nilpotent elements, and every Cartan element is semisimple. Assign to each root \(\alpha\) its filtration weight \(s_\alpha\). Pairing with its opposite root gives \(s_{-\alpha}=-s_\alpha\). If \(\alpha,\beta,\alpha+\beta\) are roots, their nonzero bracket gives

\[
s_{\alpha+\beta}\ge s_\alpha+s_\beta.
\]

Bracketing \(\alpha+\beta\) with \(-\beta\) gives the reverse inequality. Therefore equality holds. Root-height induction now makes the weights an additive function on the root lattice. They define a rational cocharacter \(\mu\) in the derived torus, uniquely after imposing zero central part. It is dominant for \(B\subset Q\), is zero on the Levi roots, and is positive on the nilradical roots. Clearing denominators makes \(Q=P_G(N\mu)\), and gives exactly the filtration by the \(\mu\)-weights.

There are only finitely many \(Q\)-stable root-line filtrations with a given finite list of weights. Consequently the weights and their assignment are locally constant along the connected curve in a \(Q\)-trivialization, and the global filtration is the one associated to this fixed \(Q\)-module filtration. Its zero graded piece is \(\operatorname{ad}F_L\) for the induced Levi bundle \(F_L\), and is semistable of degree zero. Its positive graded pieces \(V_s(F_L)\), \(s>0\), are semistable of slope \(s\). Its negative graded pieces are semistable of negative slope. In particular

\[
H^0(X,\mathfrak g_P/\mathfrak q_{F_Q})=0,
\qquad H^1(X,V_s(F_L))=0\quad(s>0). \tag{N4.3}
\]

The first assertion follows from negative slopes; the second follows by duality, \(\omega_X=\mathcal O_X\), and positive slopes. Hence every Higgs field of \(P\) lies in \(H^0(X,\mathfrak q_{F_Q})\).

Conversely, fix a dominant rational \(\mu\), \(Q=P_G(N\mu)\) and its Levi \(L\). Let \(\mathcal D_\mu\subset\operatorname{Bun}_L\) be the open and closed degree conditions together with the open conditions that every \(\mu\)-graded representation \(V_s\) in \(\mathfrak g\) is semistable of slope \(s\). The zero one is \(\mathfrak l\) and has slope zero. Openness is N3.1 applied to these finitely many actual representations. For a \(Q\)-bundle above this open, the \(\mu\)-graded adjoint filtration has semistable quotients of the indicated strictly ordered slopes, so is its unique vector Harder–Narasimhan filtration. Thus this \(Q\)-reduction is canonical, and any isomorphism of the induced \(G\)-bundles preserves it.

On a finite-type chart of \(M\), only finitely many \(\mu\)'s occur. The uniform embedding of \(E\) bounds all its subbundle slopes above; its self-duality bounds them below as well. Ranks are at most \(\dim G\), so the possible slope fractions form a finite set. Assigning these finitely many values to the finitely many roots leaves only finitely many rational dominant cocharacters. This proves the local finiteness needed below directly; it assumes no principal boundedness theorem.

### 6.9. The elliptic nilpotent models and their dimensions (N5)

### N5.1. The unipotent directions have relative dimension zero

For a type \(\mu\) from N4, filter the unipotent radical \(U\) of \(Q\) by its strictly positive \(\mu\)-weights. The terms are normal in \(Q\), and successive quotients are the additive \(L\)-representations \(V_s\); a commutator strictly increases weight. The root-coordinate construction, or the finite exponential in characteristic zero, gives these actual group quotients. On \(\mathcal D_\mu\), their associated vector bundles have zero first cohomology by (N4.3).

Let \(F_L\) be a family of Levi bundles in \(\mathcal D_\mu(S)\). These vanishings and the finite locally free cohomology complex imply that \(R\pi_*\mathfrak u_{F_L}\) is a vector bundle in degree zero and commutes with arbitrary ordinary base change. The same holds for the graded quotients. Successive additive Čech lifting therefore makes every lift of \(F_L\) to a \(Q\)-bundle isomorphic, locally on \(S\), to the split lift. Its relative automorphism group is \(\mathcal H=\Gamma(X_S,U_{F_L})\). Finite exponential identifies \(\mathcal H\), as a scheme over \(S\), with the vector bundle \(\pi_*\mathfrak u_{F_L}\); its multiplication is the polynomial Baker–Campbell–Hausdorff law. It is smooth and of constant relative dimension

\[
h=\sum_{s>0}h^0(X,V_s(F_L))=
\sum_{s>0}\deg V_s(F_L). \tag{N5.1}
\]

The Čech assertion in families can be seen layer by layer: the only curve torsor obstruction is first cohomology of the additive quotient, which is zero; after arbitrary base change the quotient remains its degree-zero pushforward. Any remaining torsor under that vector bundle is a torsor on \(S\), and becomes trivial locally on \(S\). The second cohomology on the curve is zero. Thus the relative lift stack is \(B\mathcal H\).

For a fixed Levi Higgs field \(\bar\phi\), lifting it to \(\mathfrak q\) has an affine space of choices under \(\pi_*\mathfrak u_{F_L}\), since its first cohomology is zero. After the split lift, the Levi inclusion gives one such choice. The full relative stack of lifts of \((F_L,\bar\phi)\) is therefore

\[
[\mathbb A^h_S/\mathcal H], \tag{N5.2}
\]

with its polynomial conjugation action. This stack is smooth over \(S\), of relative stack dimension \(h-h=0\). The affine action need not be free; its stabilizers are retained in this calculation.

If \(\bar\phi\) is nilpotent then every lift is nilpotent, by contracting the unipotent part with \(N\mu\): every invariant of \(\phi\) equals its restriction to \(\bar\phi\). Conversely, a nilpotent parabolic element has nilpotent Levi part on geometric fibres, by its Jordan decomposition and the zero-fibre statement in N1. This converse is a statement about reduced support: the invariant ideal of \(G\) restricted to the Levi need not equal the invariant ideal of \(L\). For example, restricting the \(SL_2\) quadratic invariant to its torus gives a square instead of the torus's linear invariant. We use the model imposing nilpotence in \(L\), which has the same reduced support in the parabolic locus. We do not assert equality of the two functors on nonreduced \(S\).

### N5.2. Semistable adjoint bundles and centralizers

Let \(L\) be any connected reductive group, and consider pairs \((F,\eta)\) with \(\mathfrak l_F\) semistable of degree zero and \(\eta\) nilpotent. Every endomorphism of this vector bundle has constant rank. If \(K,I\) are its kernel and image, semistability gives \(\deg K\le0\), hence \(\deg I\ge0\). The saturation \(\bar I\) in the target has degree at most zero. Since \(\deg\bar I\ge\deg I\), all degrees are zero and the saturation torsion is zero. Thus the image is a subbundle. Apply this to \(\operatorname{ad}\eta\).

There are finitely many nilpotent \(L\)-orbits, by the local Lie-triple proof: put the semisimple element \(h\) of a triple in a dominant Cartan. All its adjoint weights are integers of absolute value at most \(\dim\mathfrak l-1\), by the explicit \(\mathfrak{sl}_2\)-module classification. Hence only finitely many simple-root values, and therefore only finitely many \(h\)'s, can occur. For a fixed \(h\), \([e,-]:\mathfrak l_0\to\mathfrak l_2\) is onto, by that same module calculation. The centralizer of \(h\) has an open orbit at \(e\) in the irreducible vector space \(\mathfrak l_2\). Two open orbits cannot be disjoint, so there is at most one. This proves finiteness without a table of nilpotent orbits.

The section \(\eta\) has a single orbit \(C\) at every point of \(X\). Its generic orbit is one of this finite list; all other fibre orbits lie in its closure. A boundary orbit has strictly smaller dimension, while constant rank of \(\operatorname{ad}\eta\) keeps the orbit dimension constant. There can be no boundary fibre.

Fix \(e\in C\), and write \(Z=C_L(e)\), possibly disconnected. A section of the orbit bundle \(F\times^L C=F/Z\) is exactly a \(Z\)-reduction. Thus the functor of pairs whose section takes values scheme-theoretically in this orbit is \(\operatorname{Bun}_Z\), with the open condition that the induced adjoint \(L\)-bundle is semistable. With further \(\mathcal D_\mu\) conditions, it is still an open substack.

The determinant of the adjoint representation of \(Z\) is trivial. In the exact sequence of \(Z\)-representations

\[
0\to\mathfrak z\to\mathfrak l\to\mathfrak l/\mathfrak z\to0,
\]

the middle determinant is trivial. The last term has the nondegenerate \(Z\)-invariant alternating form

\[
([a,e],[b,e])\longmapsto\kappa(e,[a,b]). \tag{N5.3}
\]

Invariance of \(\kappa\) identifies its kernel precisely with the centralizer before passing to the quotient. A symplectic representation has determinant one, including the disconnected components. Therefore \(\det\mathfrak z=1\). For any \(Z\)-torsor \(R\), \(\deg\mathfrak z_R=0\). Its bundle stack is smooth by the same additive Čech deformation calculation and \(H^2=0\), and has dimension

\[
-\chi(\mathfrak z_R)=0. \tag{N5.4}
\]

Algebraicity here introduces no new kind of moduli theorem: over \(\operatorname{Bun}_L\), these reductions are the functor of sections in the orbit subbundle of \(\mathfrak l_F\), a locally closed subfunctor of the finite-type section space. Vanishing of the orbit-closure equations is a closed condition on sections; avoiding its boundary on the entire proper curve is open. The usual Čech lifting uses smoothness of \(Z\), established algebraically in characteristic zero as recalled in N7 below. Only the determinant, rather than the whole adjoint bundle, has been shown trivial.

Consequently every fixed-orbit piece of the Levi nilpotent stack with the \(\mathcal D_\mu\) conditions is smooth of pure dimension zero. This is an assertion about the actual all-scheme orbit-factorization functor. Finitely many such pieces cover the geometric points of the reduced Levi nilpotent locus; infinitesimal points need not belong to a single piece.

### 6.10. Every elliptic component, with finite-type families (N6)

For each \(\mu\) and nilpotent Levi orbit \(C\), let \(\mathcal R_{\mu,C}\) be the following actual stack: its objects are a \(Q\)-bundle with Levi bundle in \(\mathcal D_\mu\), a Levi Higgs section taking values in the orbit bundle \(C\), and a lift of that section to the parabolic algebra. By N5.1–N5.2 it is smooth of pure stack dimension zero. Forgetting the reduction gives a map

\[
\mathcal R_{\mu,C}\longrightarrow\mathcal N_G. \tag{N6.1}
\]

It is representable: after fixing the underlying \(G\)-bundle and its Higgs field, its fibre is the scheme of parabolic reductions with the indicated conditions. It has at most one geometric point in each fibre. Indeed its induced adjoint filtration is the unique vector Harder–Narasimhan filtration, by the converse in N4, so its parabolic reduction is fixed. An isomorphism of induced bundles respecting the Higgs field respects this reduction. The possible infinitesimal movement of a reduction is \(H^0(X,(\mathfrak g/\mathfrak q)_{F_Q})=0\). Thus the fibres are zero-dimensional; no stabilizers have been discarded in constructing the source stack.

Every geometric point of \(\mathcal N_G\) belongs to one of these images. Construct its parabolic reduction by N4; its Higgs field lies in the parabolic algebra by (N4.3); its Levi part is nilpotent. The semistable zero graded piece makes that Levi part have constant orbit, by N5.2. This is exactly an object of one of the sources. This includes the type \(\mu=0\), \(Q=G\), and the zero orbit. The reductive central Higgs part is zero by its invariant linear equations.

We now verify the finite-type issue, which is needed to turn these sources into a component-dimension proof. Over a finite-type chart \(A\) of \(M\), the types \(\mu\) are finite by the last paragraph of N4, and each Levi has finitely many nilpotent orbits. The parameter space of the relevant reductions is finite type over \(A\). One explicit verification uses the projective flag bundle

\[
\mathscr F=P_A\times^G(G/Q)\longrightarrow X\times A.
\]

Embed it by the parabolic-algebra Grassmannian and its Plücker line. Twisting that relative ample line by a sufficiently high fixed power of an ample line on \(X\), on a finite cover of \(A\), makes it ample for the projective morphism \(\mathscr F\to A\). The degree of its restriction to the graph of a reduction is fixed by \(\mu\): the Plücker line has restriction \(\det\mathfrak q_{F_Q}^{\vee}\), of degree

\[
-\deg\mathfrak q_{F_Q}=-\sum_{s>0}s\operatorname{rk}V_s,
\]

and the chosen twist contributes a fixed integer. The graph is a genus-one curve, so this fixes its Hilbert polynomial. The corresponding actual AG-HP-05 Hilbert scheme is projective and finite type over \(A\). The locus where projection of the universal subscheme to \(X\times A\) is an isomorphism is open and represents sections: properness first removes the locus of positive-dimensional fibres; on the finite locus, the kernel and cokernel of the map of finite algebras vanish near any base point whose fibre map is an isomorphism, by flatness and Nakayama. Thus its graph locus is of finite type.

The \(\mathcal D_\mu\) conditions are open degree conditions and semistability conditions on the associated Levi bundles. Conditions on the Higgs field are finite-type section equations; on any finite chart, a finite locally free cohomology complex realizes the section functor as the kernel of a map between finite vector bundles. Factoring the Levi section through the orbit is locally closed: impose finitely many equations of its orbit closure and avoid the boundary on the whole proper curve. These descriptions show that

\[
Y_{\mu,C}:=\mathcal R_{\mu,C}\times_M A
\]

is a finite-type algebraic space, in fact a scheme in the section/graph description. It is smooth of pure dimension \(m\), because \(A\to M\) is smooth of relative dimension \(m\) and \(\mathcal R_{\mu,C}\) is smooth of stack dimension zero. In genus one (N0.3) gives \(m=n\).

The induced morphism \(Y_{\mu,C}\to N_A\) has zero-dimensional geometric fibres. Every irreducible component of its source therefore has image closure of dimension \(m\). This follows from the finite-type dimension formula: the extension of function fields at the generic image is algebraic when the generic fibre is zero-dimensional, and both dimensions are the corresponding transcendence degrees. Étale scheme charts give the same argument for algebraic spaces.

There are only finitely many such source components: the types and orbits are finite, and each \(Y_{\mu,C}\) is finite type. Their image closures lie in \(N_A\), have dimension \(m\), and cover every geometric closed point of \(N_A\), by the construction above. Their finite union is closed. Since a finite-type scheme over an algebraically closed field is Jacobson, that union is all of \(N_A\). The irreducible components of a finite closed union are its maximal irreducible members. All these members have dimension \(m=n\). Therefore **every** component of \(N_A\) has dimension \(n\).

This proves the elliptic dimension equality without using an external principal Harder–Narasimhan theorem or a countable union. It also avoids assuming that a fibrewise canonical reduction exists over an arbitrary nonreduced base: we use actual reduction stacks, actual all-base orbit-factorization functors, and their finite-type maps, which cover geometric points. Nilpotent thickenings of their images do not affect the reduced component dimensions.

### 6.11. Smooth stabilizers and the characteristic-zero calculation (N7)

For completeness, the smooth affine stabilizers used above can be established by a direct formal matrix argument. Let \(H\subset\operatorname{GL}(V)\) be a finite-type closed group over characteristic-zero \(k\), let \(R\) be an Artinian local \(k\)-algebra with residue field \(k\), and let \(I\) be its maximal ideal. For \(g\in H(R)\) reducing to \(1\), set

\[
g(t)=\sum_{j\ge0}\binom{t}{j}(g-1)^j.
\]

This is a finite polynomial because \(I\) is nilpotent. At every nonnegative integer \(t\), it is \(g^t\in H(R)\). Applying the defining equations of \(H\) gives polynomials over \(R\) which vanish at all these integers. Vandermonde matrices on finitely many distinct integers are invertible over the characteristic-zero field, so the polynomials vanish identically. Differentiating at zero gives \(\log g\in\operatorname{Lie}H\otimes I\).

Conversely, for \(v\in\operatorname{Lie}H\otimes I\), its left invariant derivation preserves the Hopf ideal of \(H\). Its finite exponential, evaluated at the identity, gives \(\exp v\in H(R)\). The finite matrix logarithm and exponential are inverse. Thus the identity formal group of \(H\), as a functor on these Artinian rings, is the formal affine space \(\operatorname{Lie}H\). Its completed local ring is a power series ring. Finite presentation and the infinitesimal smoothness criterion give smoothness at the identity; translation gives smoothness everywhere. This proves the affine characteristic-zero case of the smooth-group theorem needed here, including disconnected \(H\).

All the relevant stabilizers have such matrix embeddings. A faithful representation of \(G\) makes \(Z=C_G(e)\) a closed matrix subgroup. For \(\operatorname{Aut}_G(P)\), twist its associated faithful vector bundle until it is globally generated with zero first cohomology. The automorphism acts faithfully on its finite-dimensional section space, because the evaluation is onto. Preserving the bundle and the \(G\)-reduction gives closed equations in the general linear group of that space. Equivalently, over each Artinian ring, logarithms of bundle automorphisms glue as sections of \(\operatorname{ad}P\), and exponentials of those sections give the inverse. These are the same smooth formal coordinates. The stabilizers in the genus-zero groupoid proof and the centralizers in N5 are therefore smooth. The finite-type diagonal and matrix realization remain within the lesson's bundle algebraicity foundation.

Here is the matching algebraic Cartan step for the Lie algebra of the assigned reductive group. Let \(s\in\mathfrak g\) be semisimple, and diagonalize its action in a faithful representation of \(G\); Jordan preservation makes this action semisimple. For the reductive centre use its torus weight decomposition. Write its eigenvalues as \(\lambda_1,\ldots,\lambda_b\), and put

\[
L=\{(a_i)\in\mathbb Z^b:\textstyle\sum_i a_i\lambda_i=0\}.
\]

This sublattice is saturated, since characteristic is zero. The diagonal subtorus \(D\subset\operatorname{GL}_b\) defined by the characters in \(L\) has \(s\) in its Lie algebra. In fact \(D\subset G\). Every equation \(f\) of \(G\), restricted to the diagonal torus, is a Laurent polynomial. Evaluate it on \(\exp(us)\) in \(k[[u]]\). The formal matrix argument above gives \(\exp(us)\in G(k[[u]])\), so this evaluation is zero. Group its finitely many monomials by the values \(\sum a_i\lambda_i\). Distinct resulting formal exponentials are linearly independent: their first finitely many derivatives at zero form an invertible Vandermonde matrix. Thus the coefficient sum in every group is zero. Two monomials restrict to the same character on \(D\) exactly when their difference lies in \(L\). These coefficient sums say precisely that \(f|_D=0\), proving \(D\subset G\).

Contain \(D\) in a maximal torus and use actual AG-RG-01 torus conjugacy to put \(s\) in the Lie algebra of a chosen maximal torus of \(G\). Its Lie centralizer equals the torus centralizer's Lie algebra: in the faithful matrix adjoint representation, a diagonal character has derivative zero on \(s\) exactly when it is trivial on \(D\), by the definition of \(L\). Actual AG-RG-02, Lemma 1.1, makes \(C_G(D)\) smooth and connected. Its root spaces consist of the pairs of opposite roots trivial on \(D\). It is reductive: the Lie algebra of a normal unipotent radical is a torus-stable ideal of nilpotent matrices; a nonzero root vector in it would yield a nonzero toral coroot by bracketing with its opposite root vector, a contradiction, and a nonzero zero-weight vector is already toral. Thus that ideal is zero, and the smooth unipotent radical is trivial. The usual root decomposition therefore gives a toral centre and a semisimple derived centralizer, with strictly smaller derived dimension when \(s\) is nonzero in a semisimple algebra.

This proves exactly the semisimple-centralizer input for the existing Lie-triple induction applied to the Lie algebra of any reductive algebraic \(G\) over the present \(k\). It also supplies actual-group conjugacy into a torus for the invariant-polynomial argument. For \(h\) in a Lie triple, the faithful representation has integral \(h\)-weights by the rank-one module calculation; its torus hull therefore has an integral cocharacter with differential \(h\). Alternatively clear denominators in its root values. The canonical cocharacter parabolic thus belongs to the given algebraic group, including a non-simply-connected one. The all-field group root arguments and the rational rank-one modules, rather than a complex-only Cartan statement, provide the exact matching foundations used here.

Every use of a field order, real chamber or integral weight in this module concerns the rational root datum and its real reflection model, not an order on \(k\). The elliptic cyclic covers use characteristic zero for the derivative of \([\ell]\) and for the automorphism-order contradiction. The formal exponentials, Jacobson–Morozov and Lie-to-group passage use characteristic zero as well. No positive-characteristic assertion follows from the module.

### 6.12. Conclusion and exact proof boundary (N8)

The module gives three independent lower bounds, paired with the already written isotropy:

| Genus | Lower bound or direct dimension mechanism | Reductive centre |
|---|---|---|
| \(g\ge2\) | At most \((m-z)+(d+z)=n\) equations in \(T^*A\) | Constant central kernel cancels the extra Hitchin dimension |
| \(g=0\) | Every cotangent point lies on a conormal bundle of dimension \(n\); choose a point outside other components | Included in the full orbit/stabilizer calculation |
| \(g=1\) | Finite-type zero-fibre maps from smooth pure-\(n\) reduction models; finitely many image closures cover \(N_A\) | Central Higgs component zero; Levi and centralizer determinants give degree zero |

This proves the geometric dimension statement for all smooth charts and includes arbitrary ordinary test-scheme families in the constructions. It does **not** say that the nilpotent cone is flat over \(\operatorname{Bun}_G\), that its fibres there have constant dimension, or that a family with a constant set of fibrewise orbit/HN labels necessarily factors through the corresponding schematic stratum. All such stronger statements would be different assertions.

The main theorem retains exactly the lesson's algebraically closed characteristic-zero boundary. If one defines the theorem over a general characteristic-zero field as a geometric Lagrangian assertion, the same proof after algebraic closure gives that geometric assertion, provided the bundle/cotangent/invariant constructions commute with that base change. No arithmetic statement about rational torsor triviality, splitness or rational nilpotent-orbit representatives is claimed.

The bundle-stack representability/algebraicity foundation and complete recursive closure of the specified programme foundations remain open. Specifically, the existing bundle-stack source invokes foundations whose proofs are still required: the Artin criterion and formal algebraization invoked by its source have not been independently proved here or assigned to a verified exact earlier proof. The actual cohomology/base-change, duality, Quot and group arguments listed above supply the particular claims used here; N0 supplies the vector-family extension and smooth-curve adjunction identification, and N7 supplies the algebraic semisimple torus step. The local algebra, quotient/descent and representability foundations cited by those earlier courses are not proved here. Within those recorded foundations, **no genus-one principal Harder–Narasimhan/tensor-semistability gap and no genus-zero quotient-chart gap remains in this dimension module**. The nilpotent Lie triple and isotropy must remain proved in the integrated lesson before this module is used. Uniformization and Beauville–Laszlo gluing are independent open work; this module proves neither and assigns neither to the absent GL-SAT-03 file.

Free source comparison, not substitutes for these proofs: [Ginzburg, *The global nilpotent variety is Lagrangian*, alg-geom/9704005v6](https://arxiv.org/pdf/alg-geom/9704005v6), chiefly the chartwise definition and the higher-genus equation count; [Beilinson–Drinfeld, author draft, §2.10.4](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), for the division by genus and the elliptic centralizer idea; [Heinloth, *Uniformization of G-bundles*, 0711.4450v2, Proposition 1](https://arxiv.org/pdf/0711.4450v2), for the exact smooth-affine finite-type group hypotheses of the existing algebraicity foundation. Public free PDFs were verified accessible. The elliptic tensor argument, construction from the adjoint vector filtration and finite-family image argument above are written out independently; the BD source's unproved principal stability package is not imported. Its final inference that trivial determinant makes the entire centralizer adjoint bundle trivial is not used: trivial determinant alone gives the needed degree zero.

The component calculations count chart dimensions rather than coarse-space dimensions, retain automorphisms in (N5.2), use actual finite-type image closures in N6, and distinguish reduced support from nilpotent test-family equations. The proof establishes tensor semistability in arbitrary algebraic characteristic zero and retains the stated recursive foundation obligations.

## 7. One point of uniformization: what it covers

Fix \(x\in X(k)\), put \(U=X\setminus\{x\}\), and write \(\operatorname{Gr}_{G,x}=G(k((t)))/G(k[[t]])\). A point of this Grassmannian is a bundle on \(X\) equipped with a trivialization on \(U\). This description, in families, uses Beauville–Laszlo gluing [Beilinson–Drinfeld, Theorems 2.3.4–2.3.5]. Changing the trivialization is an action of the group functor \(G(U)\).

Consequently the quotient \(G(U)\backslash\operatorname{Gr}_{G,x}\) maps to \(\operatorname{Bun}_G\), and identifies the substack of bundles that are trivial on \(U\) locally over their parameter schemes. It is an equivalence onto all of \(\operatorname{Bun}_G\) once every bundle admits such a trivialization locally in the relevant topology.

For semisimple simply connected \(G\), that last assertion is the uniformization theorem, whose complete programme proof remains required: families become trivial on \(U\) after an étale cover of the parameter scheme [Heinloth, Theorem 4, constant-group case]. It gives the quotient equivalence as an étale stack quotient. Gluing and uniformization are distinct inputs: the first tells us how to use two trivializations; the second supplies the missing trivialization on \(U\).

For \(G=\mathbb G_m\), a lattice at one point produces only line bundles \(\mathcal O(dx)\). On a positive-genus curve many degree-zero line bundles are absent. In detail, the localization sequence for divisors gives

\[
\operatorname{Pic}(U)\simeq
\operatorname{Pic}(X)/\mathbb Z[\mathcal O(x)].
\]

To verify it, extend a divisor on \(U\) to \(X\) to get surjectivity. A line bundle restricting trivially has a rational trivializing section whose divisor is supported at \(x\), so it is \(\mathcal O(dx)\). A nontrivial line bundle \(L\in\operatorname{Pic}^0(X)\) cannot be \(\mathcal O(dx)\), since degree would force \(d=0\). Hence \(L|_U\) is nontrivial. The bundle \(L\oplus\mathcal O^{n-1}\) similarly obstructs an unconditional \(GL_n\) assertion through its determinant. On \(\mathbb P^1\), in contrast, \(U\simeq\mathbb A^1\) and vector bundles on \(U\) are free, by the classification of finite projective modules over the principal ideal domain \(k[t]\). One-point uniformization then covers all vector bundles.

This does not conflict with the previous lesson's adelic dictionary: that construction used lattices at every closed point and allowed a rational generic frame. Triviality on one prescribed affine complement is stronger.

## 8. Exercises

**Exercise 8.1 (easy).** Derive \(\dim\operatorname{Bun}_n=n^2(g-1)\) directly from \(\operatorname{End}(E)\). For \(E=\mathcal O\oplus\mathcal O(3)\) on \(\mathbb P^1\), compute \(h^0(\operatorname{End}E)\) and \(h^1(\operatorname{End}E)\), and check the difference.

**Exercise 8.2 (easy).** Compute \(\operatorname{Aut}(\mathcal O\oplus\mathcal O(d))\) for all integers \(d\). Explain why \(\mathcal O(m)\oplus\mathcal O(-m)\) proves nonquasicompactness of the degree-zero rank-two stack.

**Exercise 8.3 (medium).** Compute the \(GL_2\) Hitchin-base dimension in all genera. For \(g\ge2\), reconcile it with the bundle-stack dimension and with the stable coarse moduli dimension.

**Exercise 8.4 (medium).** Give a connected-family proof that every degree-\(d\) rank-\(n\) bundle lies in the component of \(\mathcal O(dx)\oplus\mathcal O^{n-1}\). Specify how extensions are split in a family and how a unit of degree is transferred between two summands.

**Exercise 8.5 (hard).** Let \(g=2\) and consider \(SL_2\)-bundles. Compute the stack dimension of the space of reductions with a saturated line subbundle \(L\) of degree \(e\ge0\). Prove that the non-stable locus has codimension exactly one, whereas the non-semistable locus has codimension at least three. Identify where an estimate valid away from the genus-two \(A_1\) case fails.

## 9. Solutions

**Solution 8.1.** The bundle \(\operatorname{End}(E)\) has rank \(n^2\) and degree zero. Riemann–Roch gives \(h^1-h^0=n^2(g-1)\), the dimension of deformations minus infinitesimal automorphisms. For the particular bundle,

\[
\operatorname{End}(E)\simeq
\mathcal O^{\oplus2}\oplus\mathcal O(3)\oplus\mathcal O(-3).
\]

On \(\mathbb P^1\), \(h^0(\mathcal O(3))=4\), \(h^0(\mathcal O(-3))=0\), and \(h^1(\mathcal O(-3))=2\). Thus \(h^0=6\), \(h^1=2\), and \(h^1-h^0=-4=2^2(0-1)\). A large stabilizer is compatible with the same stack dimension as every other rank-two bundle.

**Solution 8.2.** For \(d>0\) the group is the triangular group displayed in section 4, with two nonzero diagonal constants and \(d+1\) lower off-diagonal parameters. Its dimension is \(d+3\). For \(d<0\) it is the analogous upper triangular group, of dimension \(-d+3\). For \(d=0\) it is \(GL_2\), of dimension four; the off-diagonal entries in both directions are allowed. Tensoring \(\mathcal O\oplus\mathcal O(2m)\) by \(\mathcal O(-m)\) preserves its automorphism group, so the degree-zero example has stabilizer dimension \(2m+3\). A finite type inertia morphism on finitely many finite type charts cannot have unbounded fibre dimensions. This is the required contradiction to quasicompactness.

**Solution 8.3.** The base is \(H^0(\omega_X)\oplus H^0(\omega_X^2)\). For \(g\ge2\), the two dimensions are \(g\) and \(3g-3\), so the sum is \(4g-3\). For \(g=1\), both line bundles are trivial and the sum is two. For \(g=0\), both have negative degree and the sum is zero. The bundle stack has dimension \(4g-4\) in every genus. On its stable locus, when nonempty, scalar automorphisms have dimension one, so the coarse stable moduli dimension is \(4g-3\).

For completeness, let \(f\ne0\) be an endomorphism of a stable bundle. If its image has smaller positive rank, stability applied to its kernel makes the image quotient have slope greater than \(\mu(E)\); stability applied to the saturation of its image makes its slope smaller than \(\mu(E)\). This is impossible. Thus \(f\) has full rank; its torsion cokernel has degree zero, since source and target have equal degree, so \(f\) is an isomorphism. For any endomorphism \(u\), choose an eigenvalue \(a\in k\) at one fibre. The determinant of \(u-a\) is a constant function on \(X\) and vanishes at that fibre. It is therefore zero, so \(u-a\) cannot be invertible and must be zero. This proves the scalar assertion. The scalar stabilizer accounts for the one-dimensional difference. The low-genus base values show why the formula \(4g-3\) must not be used there.

**Solution 8.4.** Saturate a generic line to obtain \(0\to L\to E\to Q\to0\). Multiply its extension cocycle by \(t\in\mathbb A^1\) to connect \(E\) with \(L\oplus Q\); induct on \(\operatorname{rk}Q\). Given two resulting line summands \(L,M\), vary the quotient of \(L\oplus M(x)\) at \(x\) over \(\mathbb P^1\). Its universal kernels connect \(L\oplus M\) to \(L(-x)\oplus M(x)\). Reverse this path when needed and repeat to get degree list \((d,0,\ldots,0)\). Connectedness of each Picard degree component, proved using the surjective Abel map, then varies those summands to \(\mathcal O(dx),\mathcal O,\ldots,\mathcal O\). Every family has constant total degree. Conversely, degree is locally constant and every degree occurs, so these are exactly the components.

**Solution 8.5.** An \(SL_2\)-bundle is a rank-two bundle together with a chosen determinant trivialization. A Borel reduction is a line subbundle \(L\subset E\), with quotient canonically \(L^{-1}\). The extension data lie in \(H^1(X,L^2)\), and automorphisms inducing the identity on the two graded terms lie in \(H^0(X,L^2)\). The base of line bundles of degree \(e\) is the Picard stack, of dimension \(g-1=1\). Hence the reduction stack has dimension

\[
1+h^1(L^2)-h^0(L^2)
=1-\chi(L^2)=2-2e.
\]

This remains valid when the individual cohomology dimensions jump: their difference is fixed by Riemann–Roch. A bundle is non-stable precisely when it has such a line with \(e\ge0\). Since \(\dim\operatorname{Bun}_{SL_2}=3\), each of these images has dimension at most two. Locally on a finite type chart only finitely many degrees of subbundles above zero can occur, by boundedness of the family. Thus their union has dimension at most two there. For non-semistability \(e\ge1\), the dimension is at most zero, giving codimension at least three.

To show the dimension-two bound for the non-stable locus is attained, choose \(L\in\operatorname{Pic}^0(X)\) with \(L^2\not\simeq\mathcal O_X\) and choose a nonsplit extension \(0\to L\to E\to L^{-1}\to0\). Such extensions exist: \(h^0(L^2)=0\) and Riemann–Roch gives \(h^1(L^2)=1\). Both line terms are semistable of degree zero, so their extension is semistable. If \(M\subset E\) is another degree-zero line subbundle, its map to \(L^{-1}\) is either zero or an isomorphism. In the first case it equals \(L\); in the second it splits the extension, which is impossible. The degree-zero reduction is therefore unique. Its infinitesimal deformations with fixed \(E\) are \(H^0(\operatorname{Hom}(L,L^{-1}))=H^0(L^{-2})=0\). The forgetful morphism from this open part of the reduction stack has zero-dimensional fibres and therefore a dimension-two image. The full non-stable locus has dimension two and codimension one.

For comparison, a Borel reduction in genus \(g\) has dimension \(2(g-1)-2e\), so the codimension bound is \(g-1+2e\). At \(g=2,e=0\), it equals one. This is the exceptional case in [Gaitsgory–Raskin, §7.2, proof of the estimate for the complement of the stable locus]. Their term “unstable” there means “not stable,” including these strictly semistable bundles. Replacing it by “not semistable” would erase the exception.

## What this lesson does not prove

We use algebraicity and local finite presentation of the torsor stack [Heinloth, Proposition 1]; the general component theorem [Drinfeld–Gaitsgory, §7.2.4]; and the background Harder–Narasimhan, openness and fixed-component boundedness theorems [Drinfeld–Gaitsgory, Theorem 7.4.3, §7.3.2 and Proposition 7.3.5]. [Gaitsgory–Raskin, §9.1] supplies the stability convention. We use Riemann–Roch, Serre duality, the Picard scheme, and proper flat constancy of Euler characteristic from algebraic geometry. The smoothness, dimension, vector-bundle connectedness, cotangent identification, examples and exercise calculations are proved here.

The nilpotent-cone Lagrangian proof is written in §6, relative to its exact stack and recursive programme foundations. Beilinson–Drinfeld, Theorem 2.10.4, and Ginzburg, Main Theorem, are human-source comparisons. Beauville–Laszlo gluing and semisimple simply connected uniformization are imported [Beilinson–Drinfeld, Theorems 2.3.4–2.3.5; Heinloth, Theorem 4]. The smooth spectral-curve correspondence is mentioned only to explain the dimensions; its construction is not proved here. Neither the categorical Langlands theorem nor a theorem about spectral singular support follows from these bundle calculations alone.

## References

- [Beilinson–Drinfeld] A. Beilinson and V. Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*. [Author's preprint](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf). Sections 2.1.1, 2.2.3, 2.3.4–2.3.5, and 2.10.2–2.10.4.
- [Gaitsgory–Raskin] D. Gaitsgory and S. Raskin, *Proof of the geometric Langlands conjecture V: the multiplicity one theorem*. [Open preprint](https://arxiv.org/abs/2409.09856). Section 7.2, proof of the complement estimate, and §9.1, stability convention. Section references follow the version with these section titles.
- [Heinloth] J. Heinloth, *Uniformization of \(\mathcal G\)-bundles*, Math. Ann. **347** (2010), 499–528. [Open preprint, version 2](https://arxiv.org/abs/0711.4450v2). Proposition 1 and Theorems 2 and 4.
- [Ginzburg] V. Ginzburg, *The global nilpotent variety is Lagrangian*. [Open preprint, version 6](https://arxiv.org/abs/alg-geom/9704005v6). Main Theorem and footnote 1.
- [Drinfeld–Gaitsgory] V. Drinfeld and D. Gaitsgory, *Compact generation of the category of D-modules on the stack of G-bundles on a curve*. [Open preprint, version 8](https://arxiv.org/abs/1112.2402v8). Sections 7.2.4 and 7.3.2, Proposition 7.3.5 and Theorem 7.4.3.
- [Stacks] The [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) supplies the background on curves, cohomology and moduli stacks, retaining the tags of the [Stacks project](https://stacks.math.columbia.edu/). In particular see [Riemann–Roch, Tag 0B5B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#section-Riemann-Roch) and [duality on curves](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#section-duality). Its AI-written additions and proposed corrections have not been reviewed by the Stacks project's maintainers. We cite the mathematical background and reproduce no text from either edition.


Section 6 now contains the Lie/parabolic isotropy and all-genus component-dimension arguments for the reduced global nilpotent cone. The central equation count, genus-zero orbit-conormal argument and algebraic elliptic tensor/parabolic source construction retain automorphisms and prove each component bound. Bundle-stack Artin/formal algebraization and exact recursive local-algebra, cohomology, Quot, Picard, flag and descent providers remain open. One-point uniformization also remains unfinished: its proof must include generic torsor triviality, modification geometry, passage to families and Beauville–Laszlo gluing. These are active obligations within the original connected reductive and semisimple simply connected scopes.

# The Jacobian theorem on a measurable source set

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Original exposition is CC0. Independent review remains separate.*

Let \(D\subseteq\mathbb R^n\) be Lebesgue measurable, and let \(\phi:D\to\mathbb R^n\) be injective. Suppose that for each \(x\in D\) a linear map \(T(x)\) is specified and
\[
 \frac{|\phi(y)-\phi(x)-T(x)(y-x)|_\infty}{|y-x|_\infty}
 \longrightarrow0\quad(y\to x,\ y\in D\setminus\{x\}).
 \tag{JC0.1}
\]
At an isolated point this condition is vacuous. No extension of \(\phi\) to an open set and no continuity of \(T\) is assumed. We prove the determinant measure identity, the nonnegative change-of-variables formula and the equivalence of scalar integrability on the image with integrability of the Jacobian-weighted pullback. We then transfer the result to any finite-dimensional real normed space with one additive Haar measure used on both source and target.

Read [Cubes, density and changes in volume](euclidean-volume-foundations.md), GV1–GV5, first. Its geometric arguments and the earlier scalar integration proofs are our prerequisites. Until JC7, measure means completed Lebesgue measure; this allows arbitrary changes on null sets. JC7 explains the interpretation for the Borel measures in the course contract. Put \(J(x)=|\det T(x)|\).

## JC1. Relative continuity and a countable matrix cover

Condition (JC0.1) implies continuity of \(\phi\) on \(D\): sufficiently near \(x\), its increment has norm at most \((\|T(x)\|+1)|y-x|_\infty\). For the matrix norm used here,
\[
 \max_{i,j}|a_{ij}|\leq\|A\|\leq n\max_{i,j}|a_{ij}|.
 \tag{JC1.1}
\]
The first inequality follows by testing coordinate vectors; the second follows by estimating each coordinate of \(Av\) for \(|v|_\infty\leq1\). Thus rational-entry matrices are dense, and matrix space has a countable basis.

Let \(\zeta(A)>0\) be any assigned tolerance for each matrix \(A\). The balls \(B(A,\zeta(A)/2)\) have a countable subfamily covering matrix space. To prove this without an additional covering theorem, use the countable basis: for each basis set contained in one of those balls, select one such ball. Every point lies in a basis neighbourhood contained in a ball of the original cover, and hence in the ball selected for that neighbourhood. Enumerate the resulting centres as \(A_j\). No measurability or continuity of \(\zeta\) is required.

## JC2. Measurable pieces with a uniform linear estimate

**Lemma.** Under (JC0.1), for any positive tolerances \(\zeta\) there is a countable measurable partition \(D=\bigcup_\ell D_\ell\), with each \(D_\ell\) bounded, and matrices \(A_\ell\), such that
\[
 \begin{split}
 \|T(x)-A_\ell\|&\leq\zeta(A_\ell)\quad(x\in D_\ell),\\
 |\phi(y)-\phi(x)-A_\ell(y-x)|_\infty
 &\leq\zeta(A_\ell)|y-x|_\infty\quad(x,y\in D_\ell).
 \end{split}
 \tag{JC2.1}
\]
Measurability of \(T\) is a conclusion below, not a hypothesis of this lemma.

*Proof.* Choose the countable centres from JC1. For every such centre \(A_j\) and every closed coordinate box \(Q\) with rational endpoints, put
\[
 H_{j,Q}=\left\{x\in D\cap Q:
 |\phi(y)-\phi(x)-A_j(y-x)|_\infty
 \leq\zeta(A_j)|y-x|_\infty\ \text{for all }y\in D\cap Q\right\}.
 \tag{JC2.2}
\]
For each fixed \(y\), this is a closed condition on \(x\) relative to \(D\), by continuity of \(\phi\). Intersect these closed conditions and the closed box. Thus \(H_{j,Q}\) is relatively closed in \(D\), measurable, bounded and of finite measure. Define, for the moment only as a set,
\[
 H'_{j,Q}=\{x\in H_{j,Q}:\|T(x)-A_j\|\leq\zeta(A_j)\}.
 \tag{JC2.3}
\]

These sets cover \(D\). Indeed, at any \(x\in D\) choose \(j\) with \(\|T(x)-A_j\|<\zeta(A_j)/2\). The relative derivative condition gives a neighbourhood of \(x\) on which its remainder is at most
\((\zeta(A_j)-\|T(x)-A_j\|)|y-x|_\infty\). Choose a sufficiently small rational closed box \(Q\) containing \(x\) and contained in that neighbourhood; rational density permits this even with \(x\) in its interior. The triangle inequality gives the condition (JC2.2), and the derivative bound gives (JC2.3).

We now prove measurability of \(H'_{j,Q}\), rather than presume it from the unknown function \(T\). Write \(H=H_{j,Q}\), \(A=A_j\). At every density point \(x\in H\), GV3.5 implies that for every fixed vector \(v\) there are points \(y_h\in H\) with
\( (y_h-x)/h\to v\) as positive \(h\downarrow0\). Choose points at distance from \(x+hv\) no greater than its distance to \(H\) plus \(h^2\); the case \(v=0\) is immediate. Apply (JC2.2) to \(x,y_h\), and use (JC0.1) at \(x\). After division by \(h\) and passage to the limit, we obtain
\[
 |(T(x)-A)v|_\infty\leq\zeta(A)|v|_\infty.
 \tag{JC2.4}
\]
This holds for every \(v\), so \(\|T(x)-A\|\leq\zeta(A)\), and \(x\in H'_{j,Q}\). By GV3.4 almost every point of \(H\) is a density point. Therefore \(H\setminus H'_{j,Q}\) is a subset of a null set and is measurable for the completed measure. It follows that \(H'_{j,Q}\) is measurable.

Enumerate the countable covering family \(H'_{j,Q}\), and subtract from each member the union of its predecessors. The resulting sets form the desired measurable partition. Keep the corresponding matrix centre. Both inequalities (JC2.1) are inherited by subsets, and every piece remains bounded. \(\square\)

## JC3. Derivatives, null sets and measurable images

Apply JC2 for each tolerance \(\zeta(A)=2^{-k}\). On each piece assign its constant matrix centre, obtaining a countably valued measurable matrix function \(T_k\). Formula (JC2.1) gives \(\|T_k(x)-T(x)\|\leq2^{-k}\). Every matrix entry of \(T\) is therefore a pointwise limit of measurable functions. Hence \(T\) and its continuous polynomial \(J=|\det T|\) are measurable for the completed measure.

The possible nonuniqueness of a relative derivative is harmless. At a density point of \(D\), the directional approximation used in JC2 shows that any two relative derivatives agree on every vector, by subtracting their remainder estimates. Thus two choices agree almost everywhere on \(D\). At isolated points or other null exceptional sets they may differ. For example, every linear map is a relative derivative on a singleton, but the integral over that singleton is zero.

Use JC2 with \(\zeta(A)=1\). On its \(\ell\)-th piece,
\[
 |\phi(y)-\phi(x)|_\infty\leq(1+\|A_\ell\|)|y-x|_\infty.
 \tag{JC3.1}
\]
Thus the domain has been partitioned into measurable pieces on which the map is Lipschitz. If \(E\subseteq D\) is measurable, each \(E\cap D_\ell\) is measurable and has measurable image by GV2. Their countable union is \(\phi(E)\), which is therefore measurable. If \(E\) is null, each of these images is null by GV2.1, so \(\phi(E)\) is null as well. These conclusions hold even without injectivity.

## JC4. The determinant measure identity

**Theorem.** If \(\phi\) is injective and satisfies (JC0.1), then for every measurable \(E\subseteq D\),
\[
 m(\phi(E))=\int_E J(x)\,dx.
 \tag{JC4.1}
\]
Either side may be infinite.

*Proof.* First let \(D\) be bounded. Given \(\varepsilon>0\), use JC2 with \(\zeta(A)=\delta(A,\varepsilon)\) from GV5, and put \(J_\ell=|\det A_\ell|\). On the \(\ell\)-th piece, GV5 and (JC2.1) give
\[
 |J(x)-J_\ell|\leq\varepsilon,\qquad
 |m(\phi(D_\ell))-J_\ell m(D_\ell)|\leq\varepsilon m(D_\ell).
 \tag{JC4.2}
\]
All terms for an individual piece are finite: the piece is bounded, the derivative determinant is bounded there by \(J_\ell+\varepsilon\), and its image is Lipschitz and bounded. Consequently
\[
 \begin{split}
 m(\phi(D_\ell))&\leq\int_{D_\ell}J+2\varepsilon m(D_\ell),\\
 \int_{D_\ell}J&\leq m(\phi(D_\ell))+2\varepsilon m(D_\ell).
 \end{split}
 \tag{JC4.3}
\]
The images are measurable by JC3 and disjoint by injectivity. Sum the two inequalities, using countable additivity and monotone convergence:
\[
 m(\phi(D))\leq\int_DJ+2\varepsilon m(D),\qquad
 \int_DJ\leq m(\phi(D))+2\varepsilon m(D).
 \tag{JC4.4}
\]
Since \(m(D)<\infty\), these inequalities rule out either side being infinite while the other is finite. If both are infinite they are equal; otherwise let \(\varepsilon\downarrow0\). Thus (JC4.1) holds for bounded \(D\).

For arbitrary \(D\), restrict to \(D\cap[-k,k]^n\). These sets and their images increase to \(D\) and \(\phi(D)\). Continuity from below and monotone convergence prove (JC4.1) for \(E=D\). Finally, restriction to any measurable \(E\subseteq D\) preserves relative differentiability with the same specified matrices, so the result applies to \(\phi|_E\). \(\square\)

## JC5. The nonnegative formula and measurability of the weighted pullback

Set \(D_+=\{x\in D:J(x)>0\}\) and \(D_0=\{x\in D:J(x)=0\}\). By JC4,
\[
 m(\phi(D_0))=0.
 \tag{JC5.1}
\]
For a function \(g\) on \(\phi(D)\), define its weighted pullback to be \(J(x)g(\phi(x))\) on \(D_+\), and zero on \(D_0\). This convention also applies to nonnegative extended-valued \(g\), so \(0\cdot\infty=0\).

We first check measurability for indicator functions, including completed-measurable target sets. Let \(F\subseteq\phi(D)\) be measurable. By the definition of completion there are Borel sets \(B,Z\subseteq\mathbb R^n\), with \(m(Z)=0\), such that \(F\mathbin{\triangle}B\subseteq Z\). The preimage of a Borel set is measurable, since \(\phi\) is continuous relative to its measurable domain. Put \(N=D_+\cap\phi^{-1}(Z)\). It is measurable, and
\(\int_NJ=m(\phi(N))\leq m(Z)=0\) by JC4. On \(N\cap\{J\geq1/k\}\) this bounds its measure by zero, so \(m(N)=0\). Thus
\(D_+\cap\phi^{-1}(F)\) differs from \(D_+\cap\phi^{-1}(B)\) by a subset of a measurable null set, and is measurable. The weighted indicator is consequently measurable. It agrees almost everywhere with \(J1_{\phi^{-1}(B)}\), and JC4 gives
\[
 \int_D J(x)1_F(\phi(x))\,dx=m(F).
 \tag{JC5.2}
\]
Indeed, \(\phi(\phi^{-1}(B))=B\cap\phi(D)\), which agrees with \(F\) off \(Z\). This reasoning uses equality almost everywhere and does not subtract possibly infinite measures.

Nonnegative simple functions now satisfy the formula by additivity. Increasing simple approximations and monotone convergence on both spaces prove, for every nonnegative measurable \(g\),
\[
 \int_{\phi(D)}g(y)\,dy
 =\int_D J(x)g(\phi(x))\,dx.
 \tag{JC5.3}
\]
They also prove measurability of the weighted pullback. No finiteness assumption is needed for (JC5.3).

There is a converse measurability assertion. If \(h=J(g\circ\phi)\) is measurable, then \(h/J=g\circ\phi\) is measurable on \(D_+\). For every real \(a\), the superlevel set of \(g\) in \(\phi(D_+)\) is
\[
 \phi\{x\in D_+:h(x)/J(x)>a\},
 \tag{JC5.4}
\]
which is measurable by JC3. The rest of the superlevel set lies in the null set \(\phi(D_0)\), so is measurable by completeness. Hence \(g\) is measurable. For real or complex \(h,g\), apply the same reasoning to real and imaginary parts. Forward measurability for these scalars follows by applying the indicator and simple-approximation argument to their positive and negative real components. Thus measurability on the image is equivalent to measurability of the weighted pullback, with the stated zero convention.

## JC6. Scalar integrability in both directions

**Theorem.** For a real or complex function \(g\) on \(\phi(D)\), the following are equivalent:

1. \(g\) is integrable on \(\phi(D)\).
2. Its weighted pullback \(h=J(g\circ\phi)\), set to zero where \(J=0\), is integrable on \(D\).

When these conditions hold,
\[
 \int_{\phi(D)}g(y)\,dy
 =\int_D J(x)g(\phi(x))\,dx,
 \qquad
 \int_{\phi(D)}|g(y)|\,dy=\int_D|h(x)|\,dx.
 \tag{JC6.1}
\]

*Proof.* JC5 gives measurability in both directions. Apply (JC5.3) to \(|g|\); its weighted pullback is exactly \(|h|\). Equality of the two nonnegative integrals proves finiteness in one space if and only if there is finiteness in the other. Once this holds, apply (JC5.3) separately to the positive and negative parts of the real and imaginary parts and combine by scalar linearity. This proves (JC6.1). \(\square\)

A function defined only almost everywhere on the image may be assigned arbitrary finite values on its exceptional target null set. The proof in JC5 shows that the preimage of that set inside \(D_+\) is null; on \(D_0\) the weighted pullback is already zero. Hence neither integral depends on the extension. This supplies precisely the almost-everywhere measurable formulation used by the scalar integration contract.

## JC7. Borel measures, other norms and additive Haar measure

The theorem has been proved for completed Lebesgue measure, so in particular it applies to Borel source sets. Integrals for the underlying Borel measure use almost-everywhere measurable representatives and have the same values: completed-measurable real or complex functions have Borel-measurable representatives, by the simple-function replacement proof in PI3. Replacing countably many simple level sets by Borel sets changes them only on a Borel null set; taking the pointwise limit gives the representative. Nonnegative extended functions are handled in the same way. Thus the completed formulation establishes the scalar integral identities and integrability equivalence in the Borel-measure convention as well. We have not assumed a separate theorem about Borel images of Borel injections.

Let now \(V\) be a real normed space of finite dimension \(n\), with a chosen basis \(e_1,\ldots,e_n\) and coordinate map \(L:\mathbb R^n\to V\). Its norm is equivalent to the coordinate maximum norm. The upper bound is
\(\|Lx\|\leq(\sum_i\|e_i\|)|x|_\infty\). For the lower bound, if unit vectors for \(|\cdot|_\infty\) could have \(\|Lx\|\to0\), coordinate compactness from GV1 would give a subsequence converging to \(x\) with \(|x|_\infty=1\). The upper bound gives continuity of \(L\), so \(\|Lx\|=0\), contradicting linear independence of the basis. This proves a positive lower bound. Relative differentiability and continuity are therefore unchanged by passing to coordinates. At \(\xi\in L^{-1}(D)\), the derivative of \(L^{-1}\phi L\) is \(L^{-1}T(L\xi)L\). Its determinant is the determinant of \(T(L\xi)\), independently of the basis, by the determinant multiplicativity proved in GV4.

Let \(\mu\) be a nonzero additive Haar measure on \(V\). Its coordinate measure \(\nu(E)=\mu(LE)\) is translation invariant and finite on compact sets. We prove that \(\nu=c\,m\) for some \(c>0\), rather than import uniqueness of Haar measure. Put \(c=\nu([0,1)^n)\), which is finite because its closure is compact. It is positive: if it were zero, countably many integer translates would give zero measure to all of \(\mathbb R^n\), contradicting nonzero \(\nu\).

Partition the unit half-open cube into \(q^n\) translates of a half-open cube of side \(1/q\). Translation invariance and finite additivity give each the measure \(c/q^n\). Tiling a rectangle with rational side lengths by such cubes gives \(c\) times its volume; translating proves the same for rational-endpoint half-open boxes. These boxes generate the Borel sigma-algebra, and \([-k,k)^n\) gives a common finite-measure exhaustion. The already proved measure-uniqueness lemma PI1 gives \(\nu=c\,m\) on Borel sets and hence on their completions.

Multiply both sides of the Euclidean identities JC4–JC6 by \(c\), and transport them by \(L\). This proves the same identities, with the absolute derivative determinant, for \(\mu\) on \(V\). Both the source and target use this same Haar measure. In dimension zero the only space is \(\{0\}\); the source is empty or that singleton, the nonempty injective map is the identity, and the empty determinant is one. Every claimed identity then follows directly from the mass of the singleton.

## JC8. The declared course interface

The theorem applies to every Borel source set in the finite-dimensional real normed-space contract, with pointwise relative differentiability, injectivity, an arbitrary specified derivative, and additive Haar measure. It includes nonnegative extended integrals and the two-way scalar integrability statement. In dimension one the determinant is the scalar derivative, so its absolute value is the full-line measure factor. The earlier PI5 proves translations, reflections and dilations directly. PI6 proves the polar identity on positive radii and angles between \(-\pi\) and \(\pi\), with determinant \(r\), and proves its omitted ray null. The orientation-sensitive finite substitution is separately proved in FT5.

The free human reference is [D. H. Fremlin, *Measure Theory*, Chapter 26](https://www1.essex.ac.uk/maths/people/fremlin/chap26.pdf), especially 262M–262P and 263C–263D. Those passages explain the measurable decomposition and relative-differentiability theorem. The written programme route here includes the needed density, volume, measurability and integration arguments, including the singular determinant and completed-measure cases. It does not import an unproved covering theorem, a source citation as a proof, or a C1 restriction in place of the declared hypothesis. Completing this scalar prerequisite alone does not certify the full modular course.

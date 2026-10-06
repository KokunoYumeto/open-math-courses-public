# Real and complex representations: weights, gamma factors and classical forms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

At a real place, a representation can be read from a ladder of rotation weights. Raising and lowering either connect the whole ladder, stop at one endpoint, or stop at both. Reflection exchanges the positive and negative ladders. These possibilities explain the principal series, discrete series and finite-dimensional representations, and they also determine which classical forms can occur.

We use the rotation orientation and unitary adelic normalization of Lesson 2:
\[
r_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix},
\qquad \jmath=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
Our real additive character is \(\psi(x)=e^{2\pi ix}\), as in the preceding local lessons, and \(d^\times x=dx/|x|\). At a complex place we use
\[
|z|_{\mathbb C}=z\bar z,\qquad
\psi_{\mathbb C}(z)=e^{2\pi i(z+\bar z)},\qquad
dz=2\,du\,dv,\quad
d^\times z=\frac{2\,du\,dv}{\pi|z|_{\mathbb C}}.
\tag{0.1}
\]
[Archimedean local zeta integrals and gamma factors](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-08.html), Propositions 8.2–8.4, proves the scalar Tate calculations with the negative additive characters. Its explicit character-change formula gives the positive phases used here. In either convention
\[
\Gamma_{\mathbb R}(z)=\pi^{-z/2}\Gamma(z/2),\qquad
\Gamma_{\mathbb C}(z)=2(2\pi)^{-z}\Gamma(z),
\quad
\Gamma_{\mathbb C}(z)=\Gamma_{\mathbb R}(z)\Gamma_{\mathbb R}(z+1).
\tag{0.2}
\]
We write \(z\) for the variable of an \(L\)-function, to distinguish it from a principal-series parameter.

The algebraic prerequisites are [Representations of \(\mathfrak{sl}_2\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-05.html), Theorem 2.1, Proposition 4.1 and the normal-ordering argument of Lemma 5.1, and Representations of compact groups, Proposition 1.2 and Theorem 3.1. The finite-dimensional highest-weight classification and compact averaging belong to those lessons. Here we prove the classification with unbounded weight ladders and the additional reflection action.

## 1. The compact generators and a scalar Casimir

A \((\mathfrak{gl}_2,O(2))\)-module is a complex vector space with compatible actions of the complexified real Lie algebra and \(O(2)\). Compatibility means that differentiation gives the specified Lie action on the Lie algebra of \(O(2)\), and that
\[
kXk^{-1}v=(\operatorname{Ad}k)(X)v.
\]
Every vector must be \(O(2)\)-finite. **Admissible** means that each irreducible compact type occurs with finite multiplicity. Restricting to the circle gives the algebraic decomposition
\[
V=\bigoplus_{n\in\mathbb Z}V_n,\qquad
r_\theta v=e^{in\theta}v\quad(v\in V_n).
\]
Each \(V_n\) is finite-dimensional in an admissible module. These are algebraic direct sums: each vector has finitely many components.

Put
\[
U=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
H=-iU,\quad
E=\frac12\begin{pmatrix}1&i\\i&-1\end{pmatrix},\quad
F=\frac12\begin{pmatrix}1&-i\\-i&-1\end{pmatrix}.
\]
Matrix multiplication gives
\[
[H,E]=2E,\quad [H,F]=-2F,\quad [E,F]=H;
\quad
\jmath H\jmath=-H,\quad \jmath E\jmath=F.
\tag{1.1}
\]
Thus \(H\) has eigenvalue \(n\) on \(V_n\), \(E\) raises that weight by two, \(F\) lowers it by two, and reflection sends \(V_n\) to \(V_{-n}\). Define
\[
\Omega=H^2+2H+4FE=H^2-2H+4EF,\qquad
\Delta=-\frac14\Omega.
\tag{1.2}
\]
The identity between the two expressions uses \(EF-FE=H\). The brackets show that \(\Omega\) commutes with \(H,E,F\); for example
\[
[\Omega,E]=2HE+2EH+4E-4HE=0.
\]
Reflection exchanges its two expressions, so it commutes with \(O(2)\) as well.

**Theorem 1.1 (scalar infinitesimal data).** On every irreducible admissible \((\mathfrak{gl}_2,O(2))\)-module, \(\Omega\) and the central matrix \(I\) act by scalars.

**Proof.** Choose a nonzero weight space \(V_n\). The operator \(\Omega\) preserves this finite-dimensional complex space, so it has an eigenvector with eigenvalue \(\lambda\). Its eigenspace in all of \(V\), namely \(\ker(\Omega-\lambda)\), is nonzero and invariant under the Lie algebra and \(O(2)\). Irreducibility makes it all of \(V\). The same argument applies to \(I\). \(\square\)

Write
\[
\Omega=s^2-1,\qquad I=2t,
\]
where \(s\) is determined up to sign. On weight \(n\), (1.2) now gives the two crucial products
\[
FE=\frac{s^2-(n+1)^2}{4},\qquad
EF=\frac{s^2-(n-1)^2}{4}.
\tag{1.3}
\]
The positive real center acts as \(aI\mapsto a^{2t}\) in the associated group representation. A negative scalar is a positive scalar times \(-I=r_\pi\), so its sign action is fixed by the weight parity.

## 2. Classify the connected ladders first

We first consider irreducible admissible \((\mathfrak{sl}_2,SO(2))\)-modules. The same finite-weight-space argument proves that \(\Omega\) is scalar.

**Lemma 2.1 (multiplicity one and connected support).** Each nonzero weight space of such a module is one-dimensional. Its weights form an interval in one parity class, and both arrows between any two consecutive occupied weights are nonzero.

**Proof.** A nonzero weight vector \(v\) generates the module under \(H,E,F\): its generated subspace is \(SO(2)\)-invariant, since all generated vectors have integral weights. Normal ordering, proved in the \(\mathfrak{sl}_2\) prerequisite, spans the enveloping algebra by \(F^aH^bE^c\). When these act on \(v\), each paired raising and lowering step reduces to a scalar by (1.3). Thus every resulting weight is spanned by one vector \(E^jv\) or \(F^jv\). This proves multiplicity one.

Missing a weight between two occupied weights separates two invariant ladders, which contradicts irreducibility. If \(E:V_n\to V_{n+2}\) vanished at an interior edge, the weights at most \(n\) would form a proper nonzero submodule; if \(F\) vanished there, the upper tail would do so. \(\square\)

There are now exactly three kinds of simple ladders.

* A **full ladder** contains every \(n\equiv\epsilon\pmod2\), for one \(\epsilon\in\{0,1\}\). It exists precisely when
  \[
  s^2\ne(n+1)^2\quad\text{for every }n\equiv\epsilon\pmod2.
  \tag{2.1}
  \]
* A **lowest ladder** has weights \(k,k+2,\ldots\), where \(k\ge1\), and \(\Omega=k(k-2)\). A highest ladder has the opposite weights and the same scalar.
* A **finite ladder** has weights \(-m,-m+2,\ldots,m\), where \(m\ge0\), and \(\Omega=m(m+2)\). It is the module \(V(m)\) of the prerequisite.

Here is the endpoint argument establishing exhaustiveness. If \(a\) is the lowest occupied weight, \(F\) kills it, so \(EF\) at \(a\) is zero and \(s^2=(a-1)^2\). Unless \(a\ge1\), the second zero of (1.3) stops the upper end at \(-a\). This produces the finite ladder with \(m=-a\). If \(a\ge1\), there is no interior zero and the ladder can continue forever. The highest-end argument is identical with signs reversed. If neither end exists, Lemma 2.1 gives the full ladder and forbids every zero in (2.1).

Existence and uniqueness also follow from the products. On a full ladder one can use
\[
Ev_n=\frac{s+1+n}{2}v_{n+2},\qquad
Fv_n=\frac{s+1-n}{2}v_{n-2}.
\tag{2.2}
\]
Their commutator is \(H\) and their Casimir is \(s^2-1\). At a lowest endpoint \(k\), use (2.2) with \(s=k-1\) and keep only weights at least \(k\); the first lowering coefficient is zero. Reflect this construction for a highest ladder. The finite modules are already constructed in the prerequisite. In every case all interior products are nonzero. A nonzero submodule contains a weight component, isolated by interpolation in \(H\), and then all weights by the arrows. This proves irreducibility. Rescaling successive basis vectors matches every other module having the same support and products, proving uniqueness.

This classification is a classification of integral rotation-weight modules. Arbitrary simple Lie-algebra modules without a compatible circle action need not belong to it.

## 3. Add reflection and identify the principal series

Reflection is essential for the full real group.

**Lemma 3.1 (the two-component argument).** An irreducible admissible \((\mathfrak{gl}_2,O(2))\)-module restricts to the connected system in one of two ways: an irreducible ladder invariant under reflection, or two inequivalent irreducible ladders exchanged by reflection. A reflection-invariant ladder has exactly two extensions; an exchanged pair has exactly one, and this extension is unchanged up to isomorphism by twisting with \(\operatorname{sgn}\det\).

**Proof.** If the restriction is reducible, take a proper nonzero connected submodule \(W\). The intersection \(W\cap\jmath W\) and the sum \(W+\jmath W\) are invariant under the full system. Hence the intersection is zero and the sum is all of \(V\). Any proper nonzero connected submodule of \(W\), together with its reflected copy, would similarly have to fill \(V\), which is impossible on projection onto \(W\). Thus both summands are simple.

They cannot be equivalent. If they were, choose an intertwiner identifying them. Reflection would then give an intertwiner from one simple module to its reflected version. Its square is scalar by multiplicity one, and can be normalized to one. More explicitly, write the module as pairs \((w,u)\), with connected action \((\sigma(X)w,\sigma(\operatorname{Ad}\jmath X)u)\) and reflection \((w,u)\mapsto(u,w)\). If \(A\) identifies the reflected action with \(\sigma\) and is normalized by \(A^2=1\), then \((w,u)\mapsto(Au,Aw)\) commutes with both actions, squares to one and has two nonzero proper eigenspaces. This contradicts irreducibility.

For a reflection-invariant simple ladder, an operator implementing reflection is unique up to scalar: any quotient of two such operators commutes with the connected action. Normalizing its square to one leaves exactly its two signs. They are inequivalent, since a connected intertwiner is scalar. For two inequivalent exchanged ladders, reflection must exchange them, and changing a basis in one summand removes any scalar ambiguity. Multiplication by \(+1\) on one summand and \(-1\) on the other identifies this extension with its determinant-sign twist. \(\square\)

For real quasi-characters
\[
\mu_i(x)=\operatorname{sgn}(x)^{\epsilon_i}|x|^{t_i},
\qquad \epsilon_i\in\{0,1\},
\]
let \(I(\mu_1,\mu_2)\) be normalized induction: its functions satisfy
\[
f\left(\begin{pmatrix}a&b\\0&d\end{pmatrix}g\right)
=\mu_1(a)\mu_2(d)|a/d|^{1/2}f(g),
\tag{3.1}
\]
and the action is right translation. Set
\[
s=t_1-t_2,\qquad t=(t_1+t_2)/2,\qquad
\epsilon=\epsilon_1+\epsilon_2\pmod2.
\]
Its compact model has basis \(v_n(r_\theta)=e^{in\theta}\), \(n\equiv\epsilon\pmod2\). Differentiating (3.1) gives (2.2), \(I=2t\), and
\[
\jmath v_n=(-1)^{\epsilon_1}v_{-n}.
\tag{3.2}
\]
For instance, \(E\) has compact adjoint weight two, so \(Ev_n\) is a multiple of \(v_{n+2}\). At the identity, the diagonal derivative in (3.1) gives \(s+1\), while the compact derivative gives \(n\); dividing the matrix \(\begin{pmatrix}1&i\\i&-1\end{pmatrix}\) by two gives the first coefficient of (2.2). The other coefficient and (3.2) follow by reflection. These computations also verify the Casimir value directly.

**Theorem 3.2 (real classification, with no repetition).** Every irreducible admissible module for the full real group is exactly one of the following:

1. An irreducible \(I(\mu_1,\mu_2)\), indexed by the unordered pair \(\{\mu_1,\mu_2\}\), except that the case \(s=0,\epsilon=1\) is included in item 2.
2. \(D_k\otimes|\det|^t\), for \(k\ge1\) and \(t\in\mathbb C\). Its weights are
   \[
   k,k+2,\ldots\quad\text{and}\quad -k,-k-2,\ldots.
   \]
   Here \(D_1\) is the limit of discrete series; \(D_k\), \(k\ge2\), is the full-group discrete series. Twisting with \(\operatorname{sgn}\det\) gives an isomorphic module.
3. A finite module \(F_{m,t,\delta}\), for \(m\ge0\), \(t\in\mathbb C\), \(\delta\in\{+1,-1\}\). Its weights are \(-m,-m+2,\ldots,m\). Precisely, take the finite quotient of (2.2) with \(s=m+1\), \(I=2t\), and reflection \(v_n\mapsto\delta v_{-n}\).

Normalized induction is reducible precisely when
\[
s\in\mathbb Z\setminus\{0\},\qquad s-\epsilon\text{ is odd}.
\tag{3.3}
\]
Equivalently, \(\mu_1\mu_2^{-1}(x)=x^p\operatorname{sgn}(x)\) for a nonzero integer \(p\).

**Proof.** The connected classification and Lemma 3.1 leave full ladders, finite ladders with their two extensions, and the exchanged lowest/highest pair. Formula (3.2) realizes both extensions of a full ladder by the two possible pairs of sign characters. It realizes both finite extensions as well. The exchanged pair is exactly the module in item 2. Its central character is
\[
\omega_{k,t}(a)=\operatorname{sgn}(a)^k|a|^{2t}.
\tag{3.4}
\]
The finite central character has sign parity \(m\).

In the compact principal model, interior arrow products vanish exactly when \(s-\epsilon\) is an odd integer. For \(s=k-1>0\), the two tails \(|n|\ge k\) give the unique full invariant proper submodule \(D_k|\det|^t\), and the central finite interval gives its quotient with \(m=k-2\). For negative \(s\) the finite module is a submodule and the exchanged tails form the quotient. At \(s=0,\epsilon=1\), the only broken edge is between \(-1\) and \(1\): the two tails are exchanged by reflection, so the *full* induction is irreducible and is \(D_1|\det|^t\). This explains the exclusion of zero in (3.3).

It remains to prove the parameter identifications. Exchanging \(\mu_1,\mu_2\) changes \(s\) to \(-s\) and exchanges the two sign exponents. An intertwiner \(v_n\mapsto a_nv'_n\) is given recursively by
\[
a_{n+2}=\frac{-s+n+1}{s+n+1}a_n.
\tag{3.5}
\]
For a full simple ladder none of these numerators or denominators vanishes. Start with \(a_0=1\) in even parity, or \(a_1=1,a_{-1}=-1\) in odd parity. The recurrence gives
\(a_{-n}=(-1)^\epsilon a_n\), exactly the condition needed for (3.2). Thus it is an isomorphism. At the limit parameter the edge is zero in both directions; the same two choices on the half-ladders provide the isomorphism.

Conversely, the weights and central derivative fix \(\epsilon,t\); the Casimir fixes \(s\) up to sign. At a fixed nonexceptional \(s\), the connected simple ladder has only scalar endomorphisms, so its two reflection extensions are inequivalent. Thus the only principal-series identification is the exchange of the two characters. The smallest positive weight and central derivative distinguish all \(D_k|\det|^t\); the dimension, central derivative and reflection extension distinguish all finite modules. Their support shapes distinguish the three items. \(\square\)

The full-group classification should not call a single positive discrete ladder an \(O(2)\)-module: reflection would take it outside itself.

## 4. Compact types and the unitary list

Write \(\rho_n\), \(n>0\), for the two-dimensional \(O(2)\)-type whose rotation weights are \(n,-n\). Its reflection exchanges the two lines. At weight zero there are two types, \(\kappa_0^+\) and \(\kappa_0^-\), with reflection \(+1\) and \(-1\).

All types in the following table occur once.

| Module | \(O(2)\)-types |
|---|---|
| Principal series, \(\epsilon=0\) | \(\kappa_0^{(-1)^{\epsilon_1}},\rho_2,\rho_4,\ldots\) |
| Principal series, \(\epsilon=1\) | \(\rho_1,\rho_3,\ldots\) |
| \(D_k\lvert\det\rvert^t\) | \(\rho_k,\rho_{k+2},\ldots\) |
| \(F_{m,t,\delta}\), \(m\) odd | \(\rho_m,\rho_{m-2},\ldots,\rho_1\) |
| \(F_{m,t,\delta}\), \(m\) even | \(\rho_m,\rho_{m-2},\ldots,\rho_2,\kappa_0^\delta\) |

Odd principal series can have the same compact types and still be inequivalent: the way the Lie arrows fit the reflection also matters.

**Lemma — the rotation-weight convolution algebra.** Let \(G^+=\{g\in\mathrm{GL}_2(\mathbb R):\det g>0\}\), \(K^+=SO(2)\), and \(\chi_n(r_\theta)=e^{in\theta}\). In an irreducible strongly continuous unitary representation of \(G^+\), the \(\chi_n\)-space has dimension at most one.

**Proof.** Normalize Haar measure on \(K^+\) to one. The orthogonal weight projection is
\[
P_n=\int_{K^+}\chi_n(k)^{-1}\pi(k)\,dk.
\]
Compressing a compactly supported continuous convolution function on both sides by this projection produces a function in
\[
\mathcal A_n=\{f\in C_c(G^+):
 f(k_1gk_2)=\chi_n(k_1)^{-1}\chi_n(k_2)^{-1}f(g)\}.
\]
This space is closed under convolution and the adjoint \(f^*(g)=\overline{f(g^{-1})}\). Here \(G^+\) is unimodular; one Haar measure is \(d^4g/(\det g)^2\).

Consider the measure-preserving anti-automorphism
\[
\tau(g)=\jmath g^{\mathsf T}\jmath.
\]
It fixes every rotation, every positive scalar, and every positive diagonal matrix. Singular-value decomposition gives
\[
g=z\,k_1
 \begin{pmatrix}e^u&0\\0&e^{-u}\end{pmatrix}k_2,
\qquad z>0,\quad u\ge0,\quad k_i\in K^+.
\]
For completeness, the orthogonal factors in singular-value decomposition have the same determinant. If both have determinant \(-1\), insert \(\jmath^2=1\) on either side of the diagonal matrix, with which \(\jmath\) commutes, to make both factors rotations. The product of their two character values is unchanged when they are exchanged. Thus \(f\circ\tau=f\) for every \(f\in\mathcal A_n\). Changing variables in convolution gives
\[
(f*h)\circ\tau=(h\circ\tau)*(f\circ\tau).
\]
Since \(f*h\) again belongs to \(\mathcal A_n\), it follows that \(f*h=h*f\). This is the elementary Gelfand transpose argument, with the compact character included.

We spell out why commutativity bounds the weight multiplicity. On a nonzero weight space \(E=P_n\mathcal H\), the compressed convolution algebra acts irreducibly as a bounded adjoint-closed algebra. Indeed, suppose \(M\subset E\) is a closed reducing subspace. Approximate a point mass at \(g\) by compactly supported continuous kernels. Strong continuity gives
\[
P_n\pi(f_j)P_n\longrightarrow P_n\pi(g)P_n
\quad\text{strongly}.
\]
The compressed kernels belong to \(\mathcal A_n\), so the limit preserves \(M\) and \(M^\perp\cap E\). For \(v\in M\) and \(w\in M^\perp\cap E\), consequently,
\[
\langle\pi(g)v,\pi(h)w\rangle
 =\langle P_n\pi(h^{-1}g)P_nv,w\rangle=0.
\]
The closed group spans of these two subspaces are orthogonal invariant subspaces. Irreducibility implies that \(M=0\) or \(M=E\).

Every self-adjoint operator in a commutative adjoint-closed algebra has spectral projections commuting with that algebra. Irreducibility makes these projections zero or the identity, so the operator is scalar. Applying this to real and imaginary parts makes every compressed convolution operator scalar. Every closed subspace of \(E\) would then be reducing; hence \(\dim E=1\). No admissibility or classification was assumed. \(\square\)

**Theorem — real Hilbert admissibility and finite-vector irreducibility.** Every irreducible strongly continuous unitary representation of \(\mathrm{GL}_2(\mathbb R)\) has finite-dimensional \(O(2)\)-type spaces. Its \(O(2)\)-finite vectors are smooth, form an irreducible \((\mathfrak{gl}_2,O(2))\)-module, and have a scalar Casimir. In particular, they belong to the classification of Theorem 3.2.

**Proof.** First justify restriction to the determinant-positive subgroup, rather than assume it remains irreducible. Let \(\mathcal B\) be the bounded commutant of \(\pi(G^+)\), and let
\(\alpha(T)=\pi(\jmath)T\pi(\jmath)^{-1}\). It is an involution of \(\mathcal B\). Its fixed algebra is the commutant of the full irreducible representation, hence \(\mathbb C I\), by unitary Schur's lemma.

Every \(T\in\mathcal B\) is the sum of a scalar fixed part and an anti-fixed part. If a nonzero anti-fixed part exists, taking its real or imaginary self-adjoint part supplies a nonzero self-adjoint \(B\) with \(\alpha(B)=-B\). Then \(B^2\) is fixed, so \(B^2=cI\) for \(c>0\). Rescale to \(B^2=I\). For any anti-fixed \(C\), the product \(BC\) is fixed, so \(C\) is a scalar multiple of \(B\). Therefore either
\[
\mathcal B=\mathbb C I
\quad\text{or}\quad
\mathcal B=\mathbb C I+\mathbb C B.
\]
In the first case restriction to \(G^+\) is irreducible. In the second, the two projections \((I\pm B)/2\) give two irreducible restrictions, exchanged by \(\jmath\): the commutant on either summand is its one-dimensional corner of \(\mathcal B\). To see this last assertion directly, any operator commuting with the restriction on a summand extends by zero on the other summand to an element of \(\mathcal B\). Both summands are nonzero, because conjugation exchanges the two projections. The preceding lemma now gives
\[
\dim\mathcal H_n\le2
\]
for every rotation weight of the full representation. This already proves compact admissibility, including the two possible reflection actions at weight zero.

Every such finite-dimensional weight space consists of smooth vectors. Choose smooth compactly supported approximate identities \(h_\epsilon\) in \(G^+\), and average them under conjugation by \(K^+\). The operators \(\pi(h_\epsilon)\) preserve weights, have smooth images, and converge strongly to the identity. The smoothing assertion follows by differentiating the left translates of the kernel under its compact integral. On a fixed finite-dimensional \(\mathcal H_n\), strong convergence is operator-norm convergence. For small \(\epsilon\), the restriction of \(\pi(h_\epsilon)\) is therefore invertible on \(\mathcal H_n\). Every vector in that space is the smoothed image of another vector in it. Finite sums of weights are smooth as well; they are dense by circle Fourier projection.

The real center acts by a continuous unitary character, again by unitary Schur's lemma. Thus its differentiated scalar is imaginary. The operator \(\Omega\) of (1.2) is symmetric on smooth vectors, preserves each \(\mathcal H_n\), and commutes with the full group, including reflection. Choose an eigenvector in a nonzero finite-dimensional weight space, with real eigenvalue \(\lambda\). To extend this scalar beyond that vector requires no assertion about essential self-adjointness of the Casimir. Define its weak eigenspace by
\[
\mathcal N_\lambda=
 \{u\in\mathcal H:
   \langle u,d\pi(\Omega)\phi\rangle
      =\lambda\langle u,\phi\rangle
       \text{ for every }\phi\in\mathcal H^\infty\}.
\]
It is closed, because each defining functional is bounded in \(u\), and it is group invariant, because smooth test vectors are group invariant and \(\Omega\) is central. The chosen eigenvector lies in it. Hilbert irreducibility gives \(\mathcal N_\lambda=\mathcal H\). Symmetry and density of smooth tests then imply \(d\pi(\Omega)u=\lambda u\) for every smooth \(u\).

Let \(V=\bigoplus_n\mathcal H_n\) be the finite vectors. It is stable under the Lie algebra and \(O(2)\). On weight \(n\), the adjoint relation \(E^*=-F\) and (1.3) give
\[
\|Ev\|^2=\frac{(n+1)^2-(\lambda+1)}4\|v\|^2,
\qquad
\|Fv\|^2=\frac{(n-1)^2-(\lambda+1)}4\|v\|^2.
\]
These identities hold even before establishing algebraic irreducibility. They bound every generator by a constant times \(1+|n|\) on that weight. A word of length \(m\) starting in a finite weight packet \(|n|\le N\) passes only through \(|n|\le N+2m\). Expanding any real Lie generator \(X\) into \(H,E,F,I\) consequently gives
\[
\|d\pi(X)^mv\|\le C_v A_X^m m!\,m^{b_v}.
\]
The exponential constant \(A_X\) is independent of the starting packet. Explicitly, the word bound is a constant to the \(m\)-th power times
\(\prod_{j=1}^m(1+N+2j)\); divide by \(2^m m!\) and use
\(\prod_{j=1}^m(1+c/j)\le e^c m^c\).
Taylor's integral remainder for a unitary one-parameter group is bounded by
\(|t|^m\|d\pi(X)^mv\|/m!\). Thus its Taylor series converges to \(\pi(\exp(tX))v\) for \(|t|A_X<1\), with the same radius for all finite vectors.

For a nonzero algebraic submodule \(W\subset V\), those Taylor partial sums lie in \(W\). Its Hilbert closure is therefore invariant under small real exponentials, by the common radius and continuity, and hence under \(G^+\); reflection gives invariance under the full group. It must be all of \(\mathcal H\). Each weight projection preserves \(W\) algebraically: the compact orbit of a finite vector lies in a finite-dimensional subspace, so its averaging integral is a linear combination in that subspace. Projecting the dense \(W\) to \(\mathcal H_n\) gives a dense linear subspace of a finite-dimensional space, hence all of \(\mathcal H_n\). Thus \(W=V\). This proves the asserted algebraic irreducibility and completes the passage to Theorem 3.2. \(\square\)

**Proposition 4.1 (unitarizability).** Up to the identifications of Theorem 3.2, the unitary list is:

* Principal series with \(\operatorname{Re}t=0\) and \(s\in i\mathbb R\).
* Complementary series with \(\operatorname{Re}t=0\), \(\epsilon=0\), and real \(0<|s|<1\).
* \(D_k|\det|^t\), \(k\ge1\), with \(\operatorname{Re}t=0\).
* The two one-dimensional characters \(F_{0,t,\delta}\), with \(\operatorname{Re}t=0\).

The odd principal parameter \(s=0\) is the already-counted \(D_1\).

**Proof of the invariant forms and necessity.** In a unitary module \(H^*=H\), \(E^*=-F\), and \(I^*=-I\). The last equality forces \(\operatorname{Re}t=0\). The Casimir is self-adjoint, so \(s^2\) is real: \(s\) is real or purely imaginary. Distinct weights are orthogonal. If \(h_n=\|v_n\|^2\), (2.2) requires
\[
\frac{h_{n+2}}{h_n}
=\frac{n+1-\bar s}{n+1+s}.
\tag{4.1}
\]
For imaginary \(s\) this is one. For real \(s\), even parity has smallest \(|n+1|=1\), so every ratio is positive precisely when \(|s|<1\). Choose \(h_0>0\) and propagate; the recurrence also gives \(h_{-n}=h_n\), making reflection unitary. In odd parity the edge from \(-1\) to \(1\) has ratio \(-1\) for nonzero real \(s\), which rules it out. At \(s=0\) that edge is absent and the two limit ladders admit the forms below.

For \(D_k\), choose \(s=k-1\) on the positive ladder. The recurrence is
\[
h_{k+2j+2}/h_{k+2j}=(j+1)/(k+j)>0.
\tag{4.2}
\]
Give the reflected ladder the same norms. These forms satisfy every adjoint relation. A nontrivial finite ladder has an interior vector with \(FE>0\), whereas
\(\langle FEv,v\rangle=-\|Ev\|^2\le0\) in a positive form. Thus \(m>0\) is impossible. For \(m=0\), only the unitary central character and the two reflection signs remain.

**Direct integration of the positive forms.** The principal-series group realization needs no general globalization theorem. Restrict (3.1) to \(O(2)\): its smooth vectors are smooth functions with the specified parity, and its finite vectors are the Fourier polynomials \(v_n\). Iwasawa decomposition writes right translation as composition with a smooth compact-coordinate diffeomorphism and multiplication by the smooth inducing character and positive modulus. This defines a jointly smooth action on the compact \(C^\infty\) model, whose differentiated action is exactly (2.2), (3.2).

For \(D_k\), use this same model with \(s=k-1\) and retain precisely the Fourier weights \(|n|\ge k\) of the appropriate parity. This is a closed smooth subspace and is group invariant. To verify that last point, project onto the excluded finite interval \(|n|\le k-2\). The arrows from the two retained boundary weights into the excluded interval vanish in (2.2). Along each real one-parameter subgroup, therefore, the excluded Fourier coefficients satisfy a finite homogeneous linear ordinary differential system depending only on the excluded coefficients themselves. If they start at zero, uniqueness makes them remain zero. Real Lie generators give the connected group; reflection preserves the retained pair of tails. For \(k=1\) the excluded interval is empty and the full odd principal model at \(s=0\) supplies the two limit ladders. The one-dimensional cases integrate by the characters already specified in Theorem 3.2.

The coefficients \(h_n\) of every positive form above have at most polynomial growth. For imaginary \(s\) they are constant; for real complementary \(s\), take logarithms in (4.1), whose differences are \(O(1/|n|)\); summing gives an \(O(\log(1+|n|))\) bound on \(|\log h_n|\). The discrete recurrence (4.2) gives the same bound directly. Thus the form is continuous on the compact smooth model, whose Fourier coefficients decrease faster than every power. Fourier partial sums converge with all differentiated actions, and the adjoint identities extend to smooth vectors.

For a real Lie generator \(X\), differentiating
\(\langle\pi(\exp(uX))f,\pi(\exp(uX))h\rangle\) now gives zero. Hence connected group translation preserves the form, and reflection does so by \(h_{-n}=h_n\). Completion gives a unitary representation. It is strongly continuous: this holds on the dense smooth model by its continuous action and the continuous form, and then on its completion by unitarity. Its weight spaces have exactly the dimensions of the original Fourier spaces. Indeed the bounded orthogonal Fourier projections have those finite-dimensional images on the dense model, so their images on the completion are the same closed spaces.

This completion is irreducible. A nonzero closed invariant subspace has a nonzero weight projection, and that projected vector is an original finite vector. Its intersection with the finite-vector module is then a nonzero algebraic submodule, so Theorem 3.2 makes it contain all finite vectors, which are dense.

Conversely, the preceding real Hilbert-admissibility theorem supplies an irreducible finite-vector module for every irreducible unitary group representation. The necessity calculation applies to it and forces the displayed list. The positive form on each such module is unique up to a scalar, by the arrow recurrence and reflection; the one-dimensional case is immediate. A normalized module isomorphism is therefore an isometry on finite vectors. The common-radius Taylor argument in that theorem makes it intertwine real exponentials, as well as compact actions, so it extends to a unitary group isomorphism of the completions. This proves the entire real unitary classification, including its group realization and uniqueness, without using Casselman–Wallach or general reductive-group admissibility. \(\square\)

**Proposition — square integrability of the discrete ladders.** The unitary \(D_k|\det|^t\), \(\operatorname{Re}t=0\), is square integrable modulo the center precisely when \(k\ge2\). The representation \(D_1\) is the limit case and is not square integrable.

**Proof.** A concrete model also supplies the coefficient estimate. The Cayley matrix
\[
C=\frac1{\sqrt2}\begin{pmatrix}1&i\\1&-i\end{pmatrix}
\]
takes \(\mathrm{SL}_2(\mathbb R)\) to \(SU(1,1)\), takes \(r_\theta\) to
\(\operatorname{diag}(e^{-i\theta},e^{i\theta})\), and takes
\(a_u=\operatorname{diag}(e^{u/2},e^{-u/2})\) to
\[
\begin{pmatrix}c&s\\s&c\end{pmatrix},
\qquad c=\cosh(u/2),\quad s=\sinh(u/2).
\]
For \(k>1\), use holomorphic functions on the unit disk with norm
\[
\|f\|_k^2=\frac{k-1}{\pi}
 \int_{|z|<1}|f(z)|^2(1-|z|^2)^{k-2}\,dA(z).
\]
Polar integration and the beta integral give
\(\|z^j\|_k^2=j!/(k)_j\); distinct monomials are orthogonal. At \(k=1\), use the Hardy norm \(\|\sum a_jz^j\|_1^2=\sum|a_j|^2\), equivalently the boundary \(L^2\) norm.

For \(g^{-1}=\left(\begin{smallmatrix}\alpha&\beta\\\bar\beta&\bar\alpha\end{smallmatrix}\right)\), define
\[
(\sigma_k(g)f)(z)
 =(\bar\beta z+\bar\alpha)^{-k}
 f\left(\frac{\alpha z+\beta}{\bar\beta z+\bar\alpha}\right).
\]
Composition of fractional linear maps and their denominators verifies the representation law. The denominator has no zero on the closed disk. For the fractional linear map \(\varphi(z)=(\alpha z+\beta)/(\bar\beta z+\bar\alpha)\), the identities
\[
1-|\varphi(z)|^2=\frac{1-|z|^2}{|\bar\beta z+\bar\alpha|^2},
\qquad dA(\varphi(z))=|\bar\beta z+\bar\alpha|^{-4}\,dA(z)
\]
show invariance of the weighted norm. At \(k=1\), the boundary angular Jacobian is the same denominator to power \(-2\), giving the Hardy-norm invariance. The action is strongly continuous on polynomials by these formulas, and hence on their dense Hilbert completion by unitarity.

The monomial \(z^j\) has rotation weight \(k+2j\). Directly, \(CEC^{-1}\) is the lower matrix unit and \(CFC^{-1}\) the upper matrix unit. Differentiating the displayed inverse pullback therefore gives \(Ez^j=(k+j)z^{j+1}\) and \(Fz^j=-jz^{j-1}\), exactly the positive ladder of (2.2). The constant function is cyclic: for \(u>0\),
\[
\sigma_k(a_u)1=c^{-k}(1-rz)^{-k},
\qquad r=\tanh(u/2),
\]
has nonzero coefficient in every monomial, and compact projection extracts each of them. Conversely, any nonzero closed invariant subspace has a nonzero monomial projection. The constant coefficient of
\(\sigma_k(a_u)z^j\) is \(c^{-k}(-r)^j\), so this subspace contains the constant and is all of the model. Thus the connected representation is irreducible. Its lowest weight is \(k\), so Sections 2 and 4 identify its finite vectors and unitary completion with the positive ladder of \(D_k\). Reflection supplies the negative ladder; the unitary positive-central twist does not change coefficient magnitudes modulo the center.

For arbitrary monomials the same formula gives
\[
\sigma_k(a_u)z^j
 =c^{-k}(z-r)^j(1-rz)^{-k-j}.
\]
Its coefficient of \(z^i\) is \(c^{-k}\) times a polynomial in \(r\), obtained by taking the finitely many terms of degree at most \(i\) in the second factor. It is bounded for \(0\le r\le1\). Consequently every fixed finite-vector coefficient is bounded by \(A\cosh(u/2)^{-k}\) on a Cartan double coset; compact translations only change its finitely many weight phases.

The Haar measure modulo the center in Cartan coordinates has radial factor \(\sinh u\,du\). This can be checked directly, without a discrete-series formula: hyperbolic disk area is
\(4\rho\,d\rho\,d\varphi/(1-\rho^2)^2\); inserting
\(\rho=\tanh(u/2)\) gives \(\sinh u\,du\,d\varphi\), and the remaining rotation fiber is compact. The other determinant-sign component contributes the same finite factor. The square-integral tail is therefore bounded by
\[
A^2\int_1^\infty \cosh(u/2)^{-2k}\sinh u\,du,
\]
which converges exactly for \(k>1\). Near zero the coefficient is bounded and \(\sinh u=O(u)\). This proves square integrability for every finite-vector coefficient when \(k\ge2\), in particular for a nonzero one.

At \(k=1\), the constant coefficient is exactly \(c^{-1}\), whose square times \(\sinh u\) tends to \(2\). More generally the polynomial multiplying \(c^{-1}\) in every monomial-pair coefficient has a nonzero limit at \(r=1\): formally taking that limit in the coefficient formula gives
\[
(z-1)^j(1-z)^{-1-j}=\frac{(-1)^j}{1-z}.
\]
Every fixed coefficient in this expression is \((-1)^j\). Thus every nonzero monomial-pair coefficient has a divergent square-integral tail. No coefficient of two arbitrary nonzero Hilbert vectors can be square integrable either. If it were, averaging its left and right compact translates against two rotation characters would preserve its \(L^2\) property, by the triangle inequality and Haar invariance. Choose nonzero weight projections of those two vectors. The resulting average is a nonzero monomial-pair coefficient in the same ladder, or after reflection in the exchanged ladder, contradicting the divergence just established. This proves the limit assertion. \(\square\)

## 5. Principal-series \(L\)- and epsilon factors

We first prove real Whittaker existence and uniqueness, then construct the full Gaussian-polynomial family and compute its Fourier Weyl action. These give the analytic models used in the factor calculation.

**Theorem — real Whittaker existence and uniqueness.** Every infinite-dimensional irreducible module in Theorem 3.2 has a nonzero moderate-growth Whittaker realization for \(\psi(x)=e^{2\pi ix}\). The space of such intertwining realizations is one-dimensional.

**Proof of existence.** For a principal series, choose the order of the parameters so that \(\operatorname{Re}s\ge0\), using the proved parameter exchange of Theorem 3.2. Work first in its smooth compact model. On the open Bruhat line put
\[
\phi_f(x)=f(w_0n(x)),\qquad
\Lambda(f)=\int_{\mathbb R}\phi_f(x)e^{-2\pi ix}\,dx.
\]
Iwasawa decomposition of \(w_0n(x)\), whose lower row is \((-1,-x)\), gives height \((1+x^2)^{-1}\). Differentiating the compact coordinate therefore gives, on either tail,
\[
|\phi_f^{(j)}(x)|\le C_j(f)(1+|x|)^{-1-\operatorname{Re}s-j}.
\]
The constants are controlled by finitely many compact smooth seminorms. The integral defining \(\Lambda\) is an improper oscillatory integral when necessary. It converges: the boundary term in one integration by parts vanishes, and the derivative is absolutely integrable. This also proves continuity on the smooth compact model. Translation of the integration variable gives
\(\Lambda(\pi(n(b))f)=e^{2\pi ib}\Lambda(f)\).
It is nonzero, because a smooth compactly supported function in the open line can be chosen with a nonzero Fourier integral.

Define \(W_f(g)=\Lambda(\pi(g)f)\). This is smooth, has the required left unipotent covariance, and transforms by the given central character. It has moderate growth. To check the last assertion explicitly, the compact right-action formula is a smooth change of compact coordinate times its inducing multiplier. The lengths appearing in that formula lie between the smallest and largest singular values of \(g\). Derivatives of the coordinate change and multiplier involve only further powers of those lengths and matrix entries. Hence every fixed compact seminorm of \(\pi(g)f\) is bounded by
\[
C_f\max(1,\|g\|,\|g^{-1}\|)^A
\]
for some \(A\) depending on the inducing parameters and the seminorm. Continuity of \(\Lambda\) gives the same kind of bound for \(W_f\), and for its right derivatives. Restriction to finite vectors is nonzero because Fourier polynomials are dense in the compact smooth model. For an irreducible principal module, the kernel of this restriction is an algebraic submodule, and is thus zero.

For \(D_k\), use the invariant tails in the principal compact model with \(s=k-1\). The lowest compact vector has Bruhat-line function
\[
\phi_{v_k}(x)=(-1)^k(x+i)^{-k}.
\]
Indeed \(e^{i\theta}=(-x+i)/\sqrt{1+x^2}\) in the Iwasawa decomposition above; multiply its \(k\)-th power by the height factor \((1+x^2)^{-k/2}\). The Fourier transform is nonzero on the positive half-line. An explicit check, valid also at \(k=1\), follows from
\[
(x+i)^{-k}=\frac{i^{-k}}{\Gamma(k)}
 \int_0^\infty u^{k-1}e^{-u}e^{iux}\,du.
\]
Taking Fourier transforms as distributions gives
\[
\int_{\mathbb R}(x+i)^{-k}e^{-2\pi iyx}\,dx
 =\frac{i^{-k}(2\pi)^k}{\Gamma(k)}
 1_{y>0}y^{k-1}e^{-2\pi y}.
\]
To justify this computation, pair first with a Schwartz test function, interchange the absolutely integrable Laplace and test integrals, and use Fourier inversion. On \(y>0\) the resulting smooth function agrees with the convergent oscillatory integral; integration by parts gives this agreement as above. In particular, evaluation at \(y=1\) is nonzero. Thus the same \(\Lambda\) restricts nontrivially to \(D_k\), including the full odd limit at \(k=1\), and gives an injective moderate realization. A central twist multiplies by \(|\det g|^t\) and preserves all these assertions.

**Proof of uniqueness.** This can be checked directly on moderate functions, so no automatic-continuity theorem for abstract Whittaker functionals is needed. Write a realization as \(v\mapsto W_v\). On weight \(n\), remove the common central twist and put
\(h_n(y)=|y|^{-t}W_{v_n}(d(y))\).
The Iwasawa differential operators (6.1), valid for every rotation weight, are
\[
E_n=y\frac d{dy}-2\pi y+\frac n2,\qquad
F_n=y\frac d{dy}+2\pi y-\frac n2.
\]
Their product is
\[
F_{n+2}E_n
 =y^2\frac{d^2}{dy^2}-4\pi^2y^2+2\pi ny-\frac{n(n+2)}4.
\]
Since \(\Omega=\lambda\), every such restriction consequently solves
\[
h_n''(y)=
 \left(4\pi^2-\frac{2\pi n}{y}+\frac{\lambda}{4y^2}\right)h_n(y).
\]
On \(y>0\), the space of solutions of this equation with polynomial growth at infinity has dimension at most one. Here is a proved bound that avoids asymptotic special-function formulas. Apply Lesson 4, Section 4, the uniform elliptic and nonconstant-mode lemmas, to the single Fourier mode
\(e^{2\pi ix}h_n(y)\) of weight \(n\) and Casimir \(\lambda\). Those lemmas apply to every complex eigenvalue; arithmetic invariance is unnecessary for their local cylinder calculation. They show that any polynomial-growth solution and its first derivative decay exponentially at positive infinity. The Wronskian of two solutions is constant, because the ordinary equation has no first-derivative term. Exponential decay forces that constant to be zero. Ordinary-equation uniqueness then makes the two solutions dependent on all \(y>0\).

In a simple full principal ladder, all interior arrows are nonzero. A nonzero realization has nonzero restriction to \(y>0\) on every weight: if one were zero there, applying raising and lowering would make all weights zero there. Reflection gives
\[
W_{\jmath v}(d(y))=W_v(d(-y)),
\]
so they would vanish on \(y<0\) as well. Unipotent and central covariance and Iwasawa decomposition would make the entire realization zero. For two nonzero realizations choose their common scalar by comparing one positive-half-line weight restriction, using the Wronskian argument. Their difference vanishes on that restriction, hence on every restriction and on the whole group by the same arrow and reflection argument. This proves uniqueness for every irreducible principal ladder.

For \(D_k\), the lowest vector satisfies \(F_kh_k=0\). Therefore
\[
h_k(y)=C_\pm |y|^{k/2}e^{-2\pi y}
\]
on the two sign components. Polynomial growth forces \(C_-=0\). The positive constant determines all raised vectors, and reflection determines the entire negative ladder. If it were zero, the realization would be zero. Thus this case, including \(k=1\), also has exactly one scalar of freedom. A finite-dimensional module has no nonzero Whittaker realization: its unipotent Lie operator is nilpotent, whereas evaluation of the left covariance would require a functional with nonzero eigenvalue \(2\pi i\). This completes the claimed real existence and uniqueness. \(\square\)

**Proposition — the Gaussian realization and Fourier Weyl action.** In an irreducible principal series, after ordering the parameters with \(\operatorname{Re}(t_1-t_2)\ge0\), its \(K\)-finite Whittaker functions have the Gaussian-polynomial realization
\[
\phi_\Phi(y)=W_\Phi(d(y))
=|y|^{1/2}\int_{\mathbb R^\times}
 \mu_1(u)\mu_2(y/u)\Phi(u,y/u)\,d^\times u,
\qquad d(y)=\operatorname{diag}(y,1),
\tag{5.1}
\]
where \(\Phi\) ranges over polynomials times \(e^{-\pi(u^2+v^2)}\). Every finite Whittaker vector is represented this way, and right translation by the Weyl element is the positive-character Fourier transform with the two coordinates exchanged.

**Proof.** Let \(\chi=\mu_1\mu_2^{-1}\), with \(\operatorname{Re}s\ge0\), and use row vectors. For a Schwartz function \(\Phi\) on \(\mathbb R^2\), form the section
\[
f_\Phi(g)=\chi(-1)\mu_1(\det g)|\det g|^{1/2}
 \int_{\mathbb R^\times}
 \chi(t)|t|\Phi((0,t)g)\,d^\times t.
\]
The integral converges near zero because its scalar radial exponent has real part \(1+\operatorname{Re}s>0\), and at infinity by Schwartz decay. It defines a smooth compact-model vector. If
\(b=\left(\begin{smallmatrix}a&b_0\\0&d\end{smallmatrix}\right)\), the change of variable \(r=td\) gives
\[
f_\Phi(bg)=\mu_1(a)\mu_2(d)|a/d|^{1/2}f_\Phi(g),
\]
exactly (3.1), including both signs of \(a,d\). Right translation is induced by
\[
(T_h\Phi)(v)=\mu_1(\det h)|\det h|^{1/2}\Phi(vh),
\qquad f_{T_h\Phi}(g)=f_\Phi(gh).
\]

Let \(\mathcal G\) be the polynomials times \(e^{-\pi(u^2+v^2)}\). Compact orthogonal substitutions preserve \(\mathcal G\); each bounded polynomial-degree space is finite dimensional and compact invariant. Differentiation of \(T_h\) gives polynomial linear vector fields and a scalar determinant term, so also preserves \(\mathcal G\). Hence the sections \(f_\Phi\), \(\Phi\in\mathcal G\), form a finite-vector submodule of the principal series. This submodule is nonzero. If \(\chi(-1)=(-1)^\epsilon\), take
\(\Phi(u,v)=v^\epsilon e^{-\pi(u^2+v^2)}\). At the identity its integral is a nonzero constant times
\[
\Gamma_{\mathbb R}(s+1+\epsilon),
\]
whose argument has positive real part. Irreducibility of the full principal module makes the image all its finite vectors. This includes the full odd limit at \(s=0\). No Schwartz-space quotient or theta-correspondence theorem is needed.

Apply the preceding Jacquet functional to \(f_\Phi\), and denote the resulting realization by \(W_\Phi^J\). First take \(\operatorname{Re}s>0\). Since
\((0,t)w_0n(x)d(y)=(-ty,-tx)\), absolute integration gives
\[
W_\Phi^J(d(y))
=\chi(-1)\mu_1(y)|y|^{1/2}
 \int_{\mathbb R^\times}\int_{\mathbb R}
 \chi(t)|t|\Phi(-ty,-tx)e^{-2\pi ix}\,dx\,d^\times t.
\]
For absolute convergence, substituting \(v=-tx\) leaves
\(\int |t|^{\operatorname{Re}s}\int|\Phi(-ty,v)|\,dv\,d^\times t\);
it is integrable at zero precisely in this open half-plane and is integrable at infinity by Schwartz decay. Thus both changes of variable and Fubini are justified here.

Put
\[
\Psi(u,v)=\int_{\mathbb R}\Phi(u,x)e^{-2\pi ivx}\,dx.
\]
The substitutions \(v=-tx\), then \(u=-ty\), cancel the \(|t|\) Jacobian and give
\[
W_\Phi^J(d(y))
=\mu_2(y)|y|^{1/2}
 \int_{\mathbb R^\times}\chi(u)\Psi(u,y/u)\,d^\times u.
\]
Here the two factors \(\chi(-1)\) cancel, and
\(\mu_1(y)\chi(y)^{-1}=\mu_2(y)\); this checks the signs as well as the central exponents. The expression is exactly (5.1).

The identity holds at \(\operatorname{Re}s=0\) too. Fix the parity and central exponent, and vary \(s\) holomorphically. The section integral is holomorphic for \(\operatorname{Re}s>-1\), uniformly in every compact smooth seminorm on smaller closed strips. The Jacquet integral is holomorphic there as well: one tail integration by parts has vanishing boundary because \(\operatorname{Re}s>-1\), and its derivative integral converges uniformly on compact subsets. On the other side, \(y\ne0\) forces at least one coordinate of \((u,y/u)\) to infinity at either end, so the Schwartz hyperbola integral is entire in \(s\). The identity theorem extends the displayed equality to the required boundary. It introduces no value assigned to a divergent double integral.

Partial Fourier transform maps \(\mathcal G\) bijectively to itself. One direct verification differentiates the Gaussian Fourier identity: the transform of \(x^j e^{-\pi x^2}\) is a degree-\(j\) polynomial times the same Gaussian, with nonzero leading coefficient; the inverse transform gives the inverse triangular map. Therefore every \(\Psi\in\mathcal G\) occurs, and surjectivity of the section map proves that these are exactly the full finite-vector Whittaker family.

Finally compute the Weyl action in these coordinates. Right translation by \(w_0\), whose determinant is one, replaces \(\Phi(u,v)\) by \(\Phi(-v,u)\). Its second-coordinate Fourier transform is
\[
\Psi^{w_0}(u,v)
 =\int_{\mathbb R}\Phi(-x,u)e^{-2\pi ivx}\,dx
 =\int_{\mathbb R}\Phi(a,u)e^{2\pi iva}\,da.
\]
Fourier inversion in the second coordinate of \(\Phi\) therefore gives
\[
\Psi^{w_0}(u,v)=\widehat\Psi(v,u),
\qquad
\widehat\Psi(a,b)=\int_{\mathbb R^2}
 \Psi(x,z)e^{2\pi i(ax+bz)}\,dx\,dz.
\]
All these integrals are Schwartz integrals. Thus the Weyl action is precisely the positive-character Fourier transform with its coordinates exchanged, with no unrecorded scalar. This proves both the full Gaussian realization and the action used below. Jacquet–Langlands, Theorem 5.13 and Lemma 5.13.1, remains the historical source for this model. \(\square\)

An archimedean factor is normalized by requiring all \(K\)-finite Mellin integrals, divided by it, to be entire, and a Gaussian test to have normalized integral one. We use the usual gamma normalization (0.2) and specify the test, including its constant, explicitly.

**Theorem 5.1.** For an irreducible real principal series,
\[
L(z,I(\mu_1,\mu_2))
=\Gamma_{\mathbb R}(z+t_1+\epsilon_1)
 \Gamma_{\mathbb R}(z+t_2+\epsilon_2),
\qquad
\varepsilon(z,I(\mu_1,\mu_2),\psi)=i^{\epsilon_1+\epsilon_2}.
\tag{5.2}
\]

**Proof.** Define \(M_z(W)=\int_{\mathbb R^\times}W(d(y))|y|^{z-1/2}d^\times y\). For \(\Phi(u,v)=f_1(u)f_2(v)\), substitute \(y=uv\) in (5.1). In a common right half-plane all integrals are absolutely convergent, by the Gaussian bounds, so Fubini gives
\[
M_z(W_\Phi)
=Z(f_1,\mu_1|\cdot|^z)\,Z(f_2,\mu_2|\cdot|^z).
\tag{5.3}
\]
Expand any Gaussian polynomial into its finitely many monomials. For the \(i\)-th coordinate, a monomial \(x^r e^{-\pi x^2}\) contributes zero unless \(r\equiv\epsilon_i\pmod2\). If \(r=\epsilon_i+2a\), its Tate integral is
\[
\Gamma_{\mathbb R}(z+t_i+\epsilon_i+2a)
=\pi^{-a}\left(\frac{z+t_i+\epsilon_i}{2}\right)_a
 \Gamma_{\mathbb R}(z+t_i+\epsilon_i),
\tag{5.4}
\]
where \((b)_a=b(b+1)\cdots(b+a-1)\) and \((b)_0=1\). The identity follows from the gamma recurrence. Thus every normalized integral is a polynomial, hence entire. For the test
\(\Phi=u^{\epsilon_1}v^{\epsilon_2}e^{-\pi(u^2+v^2)}\), (5.3) equals the product in (5.2) exactly. It is nonzero as a meromorphic function, so this is a nonzero Whittaker vector. This proves the factor for the entire \(K\)-finite family, including odd and nonspherical vectors.

For the functional equation, put \(\omega=\mu_1\mu_2\) and
\[
\widetilde M_{1-z}(W)=
\int_{\mathbb R^\times}W(d(y)w_0)\omega(y)^{-1}
 |y|^{1/2-z}d^\times y,\qquad w_0=r_{\pi/2}.
\tag{5.5}
\]
The Fourier-and-swap action in the model turns (5.5) into the product of the two dual Tate integrals. Apply the scalar functional equation from NT-ADL-08, with its additive character changed to the positive one. Each coordinate contributes \(i^{\epsilon_i}\). By linearity this proves, for every Gaussian polynomial,
\[
\frac{\widetilde M_{1-z}(W)}{L(1-z,I(\mu_1^{-1},\mu_2^{-1}))}
=i^{\epsilon_1+\epsilon_2}\frac{M_z(W)}{L(z,I(\mu_1,\mu_2))}.
\]
No interchange of an absolutely divergent oscillatory integral is needed: the model supplies the Weyl transform, and the Tate equations apply to the finitely many Schwartz tensor tests. \(\square\)

At \(s=0,\epsilon=1\), this formula is
\(\Gamma_{\mathbb R}(z+t)\Gamma_{\mathbb R}(z+t+1)=\Gamma_{\mathbb C}(z+t)\), with epsilon \(i\). It agrees with the limit calculation below.

## 6. The discrete-series integral, including every raised vector

Let \(D_{k,t}=D_k|\det|^t\) and \(a=(k-1)/2\), for \(k\ge1\). In a positive weight \(n\), after removing the central twist, the real Whittaker differential operators on \(h(y)\) are
\[
E_n=y\frac d{dy}-2\pi y+\frac n2,\qquad
F_n=y\frac d{dy}+2\pi y-\frac n2.
\tag{6.1}
\]
They follow from the matrices in (1.1) and Iwasawa coordinates; equivalently, insert the left covariance \(\psi(x)\) into Lesson 2's raising and lowering derivatives. In the twisted restriction \(W(d(y))\), replace \(y\,d/dy\) by \(y\,d/dy-t\).

The equation \(F_kh=0\) gives \(h(y)=C|y|^{k/2}e^{-2\pi y}\) on each sign component. Polynomial growth at infinity forces the negative component to be zero. The real Whittaker theorem of Section 5 ensures a nonzero lowest vector. Normalize it by
\[
W_0(d(y))=2\,1_{y>0}\,y^{t+k/2}e^{-2\pi y}.
\tag{6.2}
\]
Every positive-ladder vector is \(E^jW_0\), and reflection gives the negative ladder.

**Theorem 6.1.**
\[
L(z,D_{k,t})=\Gamma_{\mathbb C}(z+t+a),\qquad
\varepsilon(z,D_{k,t},\psi)=i^k.
\tag{6.3}
\]

**Proof of the \(L\)-factor.** The bottom integral is
\[
M_z(W_0)=2\int_0^\infty y^{z+t+a}e^{-2\pi y}\frac{dy}{y}
=2(2\pi)^{-(z+t+a)}\Gamma(z+t+a).
\tag{6.4}
\]
It converges initially when \(\operatorname{Re}(z+t+a)>0\). Hence it is exactly the claimed factor.

For all raised vectors, put \(x=4\pi y\). Applying (6.1) successively gives
\[
(E^jW_0)(d(y))=2\,1_{y>0}\,y^{t+k/2}e^{-2\pi y}P_j(4\pi y),
\]
where
\[
P_0=1,\qquad P_{j+1}=xP'_j+(k+j-x)P_j,\qquad
P_j(x)=(k)_j\sum_{r=0}^j
 \frac{(-j)_r}{(k)_r\,r!}x^r.
\tag{6.5}
\]
To check the last expression, its constant coefficient is \((k)_j\). Comparing the coefficient of \(x^r\) in the recurrence gives
\((r+k+j)c_{j,r}-c_{j,r-1}\); substitution of the displayed finite coefficients gives \(c_{j+1,r}\), including \(r=0,j+1\). Thus induction proves it. Its leading term is \((-x)^j\), so no raised vector vanishes.

Write \(b=z+t+a\). Termwise integration, using the gamma recurrence, yields
\[
M_z(E^jW_0)=\Gamma_{\mathbb C}(b)Q_j(b),\qquad
Q_j(b)=(k)_j\sum_{r=0}^j
 \frac{(-j)_r(b)_r\,2^r}{(k)_r\,r!}.
\tag{6.6}
\]
This is a polynomial in \(b\). Reflection changes positive support to negative support and multiplies the Mellin integral by a fixed nonzero scalar. Consequently every \(K\)-finite vector has an entire normalized integral, and the bottom vector has normalized integral one. This proves the full assertion about \(L\).

**Proof of the phase.** The beta identity proved in NT-ADL-08 gives, for \(0<\operatorname{Re}b<k\),
\[
\frac{Q_j(b)}{(k)_j}
=\frac{\int_0^1 u^{b-1}(1-u)^{k-b-1}(1-2u)^j\,du}
       {B(b,k-b)}.
\tag{6.7}
\]
Expand the finite power: the ratio of the \(r\)-th beta integral to \(B(b,k-b)\) is \((b)_r/(k)_r\), giving (6.6). Now replace \(u\) by \(1-u\). The beta denominator is symmetric and the polynomial acquires \((-1)^j\). Hence, first on the strip and then as a polynomial identity,
\[
Q_j(k-b)=(-1)^jQ_j(b).
\tag{6.8}
\]

The Weyl element \(w_0=r_{\pi/2}\) acts on weight \(k+2j\) by \(i^{k+2j}=i^k(-1)^j\). In (5.5), multiplication by \(\omega_{k,t}(y)^{-1}\) removes twice the central exponent on positive \(y\). The dual Mellin variable is therefore
\(1-z-t+a=k-b\). Equations (6.6)–(6.8) show that the two factors \((-1)^j\) cancel, leaving \(i^k\). On the negative ladder, the Weyl phase is \(i^{-k-2j}\) and the negative central sign contributes \((-1)^k\); again the same epsilon \(i^k\) results. Linearity proves the functional equation on every \(K\)-finite vector. \(\square\)

For \(k=1\) the proof uses the same half-ladders and proves the limit factor, agreeing with (0.2). For the negative additive character the phase is \((-i)^k\). More generally, with the new self-dual measure for \(\psi_c(x)=\psi(cx)\),
\[
\varepsilon(z,\pi,\psi_c)=
\omega_\pi(c)|c|^{2z-1}\varepsilon(z,\pi,\psi).
\tag{6.9}
\]
The change-of-variable proof is the one in Lesson 9, Section 6: replace \(W(g)\) by \(W(d(c)g)\), compare both Mellin integrals, and use \(\det d(c)=c\). It applies unchanged to the real integrals. For \(c=-1\), (3.4) changes \(i^k\) to \((-i)^k\).

For comparison, the finite-dimensional module \(F_{m,t,\delta}\) has no Whittaker functional: the unipotent Lie generator is nilpotent, whereas a nontrivial additive character would require a functional with nonzero eigenvalue. Its standard factor is defined using its principal-series Langlands quotient data, with \(s=m+1\), sign exponents chosen by \(\delta=(-1)^{\epsilon_1}\) and \(\epsilon_1+\epsilon_2\equiv m\pmod2\):
\[
L(z,F_{m,t,\delta})
=\Gamma_{\mathbb R}(z+t+(m+1)/2+\epsilon_1)
 \Gamma_{\mathbb R}(z+t-(m+1)/2+\epsilon_2).
\tag{6.10}
\]
The matrix-factor proposition in Section 8 proves this nongeneric extension for every coefficient, with epsilon phase \(i^{\epsilon_1+\epsilon_2}\). Jacquet–Langlands, §5, immediately before Theorem 5.15, fixes the historical convention. The discrete factor (6.3) uses its own infinite constituent and has already been calculated separately.

## 7. Why holomorphic and Maass forms have these infinity types

**Theorem 7.1 (holomorphic infinity type).** A nonzero weight-\(k\) holomorphic cusp form, \(k\ge2\), in the unitary adelic normalization generates \(D_k\) at infinity.

**Proof.** Lesson 2, Proposition 3.1, proves that its adelic lift \(v\) has rotation weight \(k\), central derivative zero and \(Fv=0\). The lift lies in the unitary cuspidal Hilbert space described in Lessons 3–4. From (1.2),
\(\Omega v=k(k-2)v\). Using the commutator or (1.3) inductively gives
\[
FE^{j+1}v=-(j+1)(k+j)E^jv,\qquad
\|E^jv\|^2=j!(k)_j\|v\|^2.
\tag{7.1}
\]
In particular, all the raised vectors are nonzero. Their distinct weights are \(k,k+2,\ldots\), and lowering returns along the same ladder. This is the unique irreducible lowest ladder from Section 2. Reflection generates its negative counterpart; their supports are disjoint, and Lemma 3.1 makes their full \(O(2)\)-module \(D_k\). Positive scalar invariance removes the twist \(t\). Thus the infinity module is forced to be \(D_k\).

This is a local statement about the module generated by the lifted form. The tensor-product theorem in the next lesson identifies it with the named infinity factor of the whole automorphic representation; the local proof does not assume that theorem. \(\square\)

In particular,
\[
L_\infty(z,\pi_f)=\Gamma_{\mathbb C}(z+(k-1)/2),\qquad
\varepsilon_\infty=i^k.
\tag{7.2}
\]
Classical \(L(f,w)\) uses \(w=z+(k-1)/2\). That shift is the unitary normalization, not an additional gamma factor.

For a weight-zero Maass form \(u\), the Casimir is the hyperbolic Laplacian. If
\[
-y^2(\partial_x^2+\partial_y^2)u=(1/4+r^2)u,
\]
then \(\Omega=-1-4r^2\), so the inducing difference is \(s=2ir\). If
\(u(-\bar z)=(-1)^\eta u(z)\), its real principal data are
\[
\mu_1=\operatorname{sgn}^\eta|\cdot|^{ir},\qquad
\mu_2=\operatorname{sgn}^\eta|\cdot|^{-ir}.
\]
The two sign exponents agree because the rotation parity is even. Hence
\[
L_\infty(z,\pi_u)=
\Gamma_{\mathbb R}(z+ir+\eta)\Gamma_{\mathbb R}(z-ir+\eta),
\qquad \varepsilon_\infty=(-1)^\eta.
\tag{7.3}
\]
When the Laplace eigenvalue is below \(1/4\), the difference parameter is real and the unitary list identifies the possible complementary series. A Laplace eigenvalue alone does not determine the reflection parity.

## 8. Complex places: compact multiplicities, classification and factors

Here the maximal compact subgroup is \(U(2)\). We first prove the Hilbert-to-module passage.

**Lemma — the complex compact multiplicity bound.** In every irreducible strongly continuous unitary representation of \(\mathrm{GL}_2(\mathbb C)\), each irreducible \(U(2)\)-type occurs at most once.

**Proof.** Put \(G=\mathrm{GL}_2(\mathbb C)\), \(K=U(2)\). Every complex \(2\times2\) matrix is unitarily conjugate to its transpose. Indeed choose an eigenvector and extend it to an orthonormal basis, giving an upper triangular matrix
\(\left(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}\right)\); changing the second basis vector's phase makes \(b\ge0\). Triangularize the transpose with the same first eigenvalue \(a\), so its diagonal is again \(a,d\). The squared Frobenius norm is unchanged by transpose and unitary conjugation, and is \(|a|^2+|d|^2+b^2\). Hence its nonnegative off-diagonal entry is the same \(b\). This proves the assertion even for a repeated eigenvalue.

Let \(\mathcal A\) be the compactly supported continuous functions on \(G\) invariant under \(K\)-conjugation. It is an adjoint-closed convolution algebra. The anti-automorphism \(\tau(g)=g^{\mathsf T}\) preserves Haar measure, and every \(f\in\mathcal A\) satisfies \(f\circ\tau=f\), by the preceding conjugacy. Since convolution preserves \(K\)-conjugation invariance,
\[
(f*h)\circ\tau=(h\circ\tau)*(f\circ\tau)
\]
makes \(\mathcal A\) commutative. The measure assertion is also explicit: \(d^8g/|\det g|_{\mathbb C}^2\) is a left and right Haar measure, and transpose merely permutes its real matrix coordinates.

We justify the multiplicity inference for a nonabelian compact type. By compact Hilbert decomposition, its isotypic space is
\[
E_\rho=P_\rho\mathcal H=V_\rho\otimes M_\rho,
\qquad d=\dim V_\rho<\infty.
\]
A conjugation-averaged convolution operator restricts to \(I\otimes b_f\). We claim that these \(b_f\) act irreducibly on a nonzero \(M_\rho\). For any compactly supported kernel, write its compression as a \(d\times d\) matrix of bounded operators,
\(A=P_\rho\pi(f)P_\rho\). Averaging the left-translated operator \(\pi(k)\pi(f)\) under compact conjugation gives, on \(E_\rho\),
\[
I\otimes\frac1d
 \operatorname{Tr}_{V_\rho}\bigl((\rho(k)\otimes I)A\bigr).
\]
This is an operator of the stated form with a conjugation-invariant compactly supported kernel. The linear span of the matrices \(\rho(k)\) is all \(\operatorname{End}(V_\rho)\). To see this with the required normalization, Schur's lemma gives
\[
\int_K\rho(k)B\rho(k)^*\,dk=\frac{\operatorname{tr}B}{d}I.
\]
Take \(B\) to be a matrix unit and read its entries. This gives
\(\int_K\rho(k)_{ij}\overline{\rho(k)_{\ell m}}\,dk
 =\delta_{i\ell}\delta_{jm}/d\).
Integrating the matrices \(\rho(k)\) against those conjugate coefficients therefore extracts each matrix unit. Thus their partial traces extract every entry of \(A\).

If \(M_0\) is a closed reducing subspace for all \(b_f\), it follows that \(V_\rho\otimes M_0\) reduces every compressed \(\pi(f)\). Approximating point masses strongly gives the same assertion for \(P_\rho\pi(g)P_\rho\). For \(v\) in this subspace and \(w\) in its orthogonal complement within \(E_\rho\),
\[
\langle\pi(g)v,\pi(h)w\rangle
 =\langle P_\rho\pi(h^{-1}g)P_\rho v,w\rangle=0.
\]
Their closed group spans are orthogonal invariant subspaces. Hilbert irreducibility forces \(M_0=0\) or \(M_0=M_\rho\). The commutative adjoint-closed algebra on \(M_\rho\) is consequently irreducible. Its self-adjoint elements are scalar by their spectral projections, and hence every element is scalar. Every subspace would then reduce it, so \(\dim M_\rho=1\). This proves the lemma without any admissibility input. \(\square\)

**Theorem — complex Hilbert admissibility and finite-vector irreducibility.** Every irreducible strongly continuous unitary representation of \(\mathrm{GL}_2(\mathbb C)\) is compact-admissible. Its \(U(2)\)-finite vectors are smooth, form an irreducible \((\mathfrak{gl}_2(\mathbb C)_{\mathbb R},U(2))\)-module, and have scalar action of the entire complexified enveloping center.

**Proof.** The preceding lemma makes each compact isotypic space finite dimensional. A smooth compactly supported approximate identity, averaged under conjugation by \(U(2)\), preserves those spaces, has smooth image, and converges strongly to the identity. Its restriction to any such finite-dimensional space is invertible once sufficiently close to the identity. Thus every finite compact vector is smooth. Compact Fourier projections also give their density.

Take the inner product linear in its first variable. For any element \(Z\) of the complexified enveloping center, its action preserves a nonzero finite-dimensional compact isotypic space. Choose an eigenvector there, with eigenvalue \(\lambda\). Let \(Z^*\) be its formal unitary adjoint; it is central as well, since the adjoint involution reverses products and preserves the enveloping center. Define
\[
\mathcal N_\lambda=
 \{u\in\mathcal H:
  \langle u,d\pi(Z^*)\phi\rangle
       =\lambda\langle u,\phi\rangle
          \text{ for every smooth }\phi\}.
\]
This is a closed group-invariant subspace containing the eigenvector. Centrality is group centrality because the complex group is connected. Irreducibility makes it all of \(\mathcal H\), and differentiation against smooth tests gives \(d\pi(Z)u=\lambda u\) for every smooth \(u\). This argument works separately for each central element and needs no assertion about its essential self-adjointness.

Here are the norm bounds required to pass from Hilbert to algebraic irreducibility. Let \(\sigma_j\) be the three Pauli matrices and put
\[
K_j=\frac i2\sigma_j,\qquad P_j=iK_j,\qquad
\mathcal C=\sum_{j=1}^3(P_j^2-K_j^2).
\]
These are real Lie generators: the \(K_j\) are compact, and \(P_j=iK_j\) denotes another real Lie vector obtained by multiplying the original complex matrix by \(i\). The \(P_j\) are noncompact. Their brackets are
\[
[K_i,K_j]=-\varepsilon_{ijk}K_k,\quad
[K_i,P_j]=-\varepsilon_{ijk}P_k,\quad
[P_i,P_j]=\varepsilon_{ijk}K_k.
\]
Expanding a commutator and exchanging \(j,k\) shows that \(\mathcal C\) is central. It is formally symmetric, so its scalar \(c\) is real.

On a compact \(SU(2)\)-type of highest weight \(\ell\), the positive compact Casimir \(-\sum K_j^2\) has scalar \(\ell(\ell+2)/4\). To check the constant, work in the complexification of the compact \(\mathfrak{su}_2\) and put \(H=-2iK_3\), \(E=K_2-iK_1\), \(F=-K_2-iK_1\). These are its standard \(\mathfrak{sl}_2\) generators, with the \(i\)'s now scalar coefficients in that complexification:
\[
-\sum K_j^2=\frac14(H^2+2H+4FE).
\]
The highest vector has \(H=\ell\), \(E=0\), giving the claimed scalar; centrality makes it hold on the type. Unitarity now gives
\[
\sum_j\|d\pi(P_j)v\|^2
 =\left(\frac{\ell(\ell+2)}4-c\right)\|v\|^2.
\]
For a finite packet with \(\ell\le L\), orthogonality of compact types gives the corresponding bound by \(A(1+L)^2\|v\|^2\). Compact generators satisfy the same kind of norm bound. The two real central generators are scalar because the group center acts by a unitary character.

The span of the \(P_j\) transforms under \(SU(2)\) as the highest-weight-two adjoint representation. Its action on a compact type of highest weight \(\ell\) can therefore produce only types with highest weight at most \(\ell+2\). This requires only the elementary tensor weight bound: every weight of the tensor product is a sum of a weight at most \(\ell\) and a weight at most two. Compact generators preserve the types. Central-circle weights are unchanged.

Consequently a word of length \(m\) starting in a packet \(\ell\le L\) passes only through packets with \(\ell\le L+2m\). Expanding any real Lie generator \(X\) and multiplying the displayed norm bounds gives
\[
\|d\pi(X)^mv\|\le C_v A_X^m m!\,m^{b_v},
\]
with \(A_X\) independent of the starting packet. The factorial comparison and unitary Taylor integral remainder are exactly those proved in the real Hilbert theorem of Section 4. Thus finite vectors have a common-radius convergent Taylor series along each real one-parameter subgroup.

Let \(W\) be a nonzero algebraic submodule of the finite vectors. Taylor partial sums and continuity make its Hilbert closure invariant under the connected complex group, so this closure is all of \(\mathcal H\). Every compact-type projection preserves \(W\) algebraically, since each compact orbit is finite dimensional. Its image is dense in the finite-dimensional isotypic space and therefore equals that space. Taking all compact types gives \(W=\mathcal H_{\rm fin}\). This proves algebraic irreducibility. \(\square\)

**Lemma — compact types of a complex principal series.** Write
\(\mu_i(z)=(z/|z|)^{n_i}|z|_{\mathbb C}^{t_i}\).
The finite vectors of normalized complex induction contain precisely one copy of each \(U(2)\)-type with central weight \(n_1+n_2\) and \(SU(2)\)-highest weight
\[
\ell=|n_1-n_2|,\ |n_1-n_2|+2,\ |n_1-n_2|+4,\ldots.
\]
Their dimensions are \(\ell+1\); these assertions do not require irreducibility of the induction.

**Proof.** Restriction to \(K=U(2)\) identifies the compact model with smooth functions satisfying
\[
f(\operatorname{diag}(e^{i\alpha},e^{i\beta})k)
 =e^{i(n_1\alpha+n_2\beta)}f(k).
\]
The inducing modulus and radial characters are one on this compact torus. An irreducible compact type has the form
\[
V_{a,b}=\det^b\operatorname{Sym}^{a-b}(\mathbb C^2),
\qquad a\ge b,\quad a,b\in\mathbb Z.
\]
Indeed the compact center is scalar; the restriction to \(SU(2)\) is irreducible because \(U(2)\) is the product of \(SU(2)\) and its scalar circle. The finite \(\mathfrak{sl}_2\) classification gives a highest weight \(\ell\ge0\). The product-cover kernel \((-I,-1)\) requires the central weight \(m\) to have the same parity as \(\ell\), so \(a=(m+\ell)/2\), \(b=(m-\ell)/2\). This gives exactly the displayed types. Their torus weights, read from the monomial basis, are
\[
(a-j,b+j),\qquad 0\le j\le a-b,
\]
each once.

Here compact reciprocity is explicit. A right-\(K\)-equivariant map \(T:V_{a,b}\to I|_K\) is determined by the functional \(\lambda(v)=T(v)(1)\), since
\(T(v)(k)=\lambda(kv)\). The required left covariance says
\(\lambda(tv)=\mu_1(t_1)\mu_2(t_2)\lambda(v)\) on the compact diagonal torus. Conversely any such functional gives that smooth matrix coefficient and the equivariant map. Thus its multiplicity is exactly the dimension of the torus-weight space \((n_1,n_2)\), which is one if this weight occurs and zero otherwise.

Occurrence is equivalent to \(a+b=n_1+n_2\) and \(a-j=n_1\), \(b+j=n_2\) for some \(0\le j\le\ell\). These are exactly
\(\ell\ge|n_1-n_2|\) and \(\ell\equiv n_1-n_2\pmod2\). Compact decomposition accounts for every finite vector. The real parts of \(t_i\) never enter. \(\square\)

We now prove the classification, including exhaustion and the precise inducing pair. The reducibility condition is
\[
\mu_1/\mu_2=z^p\bar z^q\quad\text{or}\quad z^{-p}\bar z^{-q},
\qquad p,q\in\mathbb Z_{\ge1}.
\tag{8.1}
\]
The following support lemmas replace the general separation and embedding assertions by proofs for this group.

**Lemma — the compact centralizer in the complex enveloping algebra.** Identify the traceless complexified real algebra with
\(\mathfrak s\oplus\mathfrak s\), \(\mathfrak s=\mathfrak{sl}_2(\mathbb C)\), so that the complexified compact algebra is the diagonal copy. This uses the automorphism \(X\mapsto-X^{\mathsf T}\) on the antiholomorphic factor: in the original holomorphic/antiholomorphic coordinates a compact matrix has the form \((X,-X^{\mathsf T})\). Write \(\Omega_1,\Omega_2\) for the two standard Casimirs and \(\Omega_K\) for the diagonal compact Casimir, each normalized by
\(H^2+2H+4FE\). Then
\[
U(\mathfrak{gl}_2(\mathbb C)_{\mathbb R}\otimes\mathbb C)^{U(2)}
 =\mathbb C[J_1,J_2,\Omega_1,\Omega_2,\Omega_K],
\]
where the two \(J_i\) are the scalar Lie directions. In particular this algebra is commutative.

**Proof.** First prove the polynomial invariant assertion required by PBW, rather than assume it. On two traceless matrices set
\[
A=\tfrac12\operatorname{tr}(X^2),\quad
B=\tfrac12\operatorname{tr}(XY),\quad
C=\tfrac12\operatorname{tr}(Y^2).
\]
Every simultaneous-conjugation invariant polynomial is a polynomial in \(A,B,C\). For the proof, diagonalize a generic \(X\) as
\(\operatorname{diag}(t,-t)\), \(t\ne0\), and write
\(Y=\left(\begin{smallmatrix}u&v\\w&-u\end{smallmatrix}\right)\).
The diagonal stabilizer of \(X\) scales \(v,w\) with opposite weights, so the restricted invariant is a polynomial in \(t,u,vw\). The Weyl element changes \(t,u\) to \(-t,-u\) and preserves \(vw\). Every surviving monomial has even total degree in \(t,u\). Substituting
\[
t^2=A,\qquad tu=B,\qquad vw=C-B^2/A
\]
therefore expresses it as \(P(A,B,C)/A^r\) for a polynomial \(P\) and some \(r\ge0\).

These apparent denominators must cancel. The polynomial identity
\(A^r f(X,Y)=P(A,B,C)\), initially proved for generic \(X\), holds everywhere by density. If \(r>0\), set \(X\) to the upper matrix unit. Now \(A=0\), while \(B=w/2\) and \(C=u^2+vw\) can range over a dense subset of the entire \((B,C)\)-plane: take \(w\ne0\), \(u=0\), and choose \(v\). Hence \(P(0,B,C)=0\), so \(A\) divides \(P\). Cancel one denominator and repeat. This proves the invariant claim. The quantities are algebraically independent too, since \(A\ne0\) with \(X\) diagonal lets \(B,C\) be arbitrary. Compact invariance is the same invariant condition: differentiation complexifies \(\mathfrak{su}_2\) to diagonal \(\mathfrak{sl}_2\), whose connected conjugation group preserves the polynomial.

Use the invariant trace pairing to identify the leading PBW symbols with these polynomial functions. For a traceless matrix
\(\left(\begin{smallmatrix}x&v\\w&-x\end{smallmatrix}\right)\),
the linear symbols of \(H,E,F\) are \(2x,w,v\). Thus the Casimir symbol is \(4(x^2+vw)\). The leading symbols of \(\Omega_1,\Omega_2,\Omega_K\) are respectively
\[
4A,\qquad4C,\qquad4(A+C+2B).
\]
The scalar directions contribute their two independent linear coordinates and are unaffected by compact conjugation.

The leading symbol of any compact-invariant enveloping element is consequently a polynomial in the leading symbols of the five displayed generators. Subtract the same polynomial in the generators themselves; the result is still compact invariant and has lower PBW degree. Induction on that degree proves generation. The \(J_i,\Omega_i\) are full central elements; \(\Omega_K\) commutes with them. All generators therefore commute. \(\square\)


The full enveloping center is
\[
Z(U(\mathfrak g_{\mathbb C}))
 =\mathbb C[J_1,J_2,\Omega_1,\Omega_2].
\]
For completeness, its leading PBW symbol is invariant under the two independent traceless factors. A polynomial invariant on one traceless matrix restricts on \(\operatorname{diag}(t,-t)\) to an even polynomial in \(t\), by the Weyl element. It is therefore a polynomial in \(A=t^2\) on the dense diagonalizable locus, hence everywhere. Applying this argument to each factor with the other coordinates as coefficients gives the invariant ring \(\mathbb C[A,C]\), together with the scalar coordinates. The same degree-subtraction argument proves the asserted center. Thus matching the four displayed scalars matches the whole central character.


**Lemma — compact multiplicity and central-character separation for admissible modules.** Let \(V\) be an irreducible admissible \((\mathfrak{gl}_2(\mathbb C)_{\mathbb R},U(2))\)-module. Every compact type occurs at most once. Two such modules with the same enveloping central character and a compact type in common are isomorphic.

**Proof.** Central elements are scalar on \(V\). Each preserves a nonzero finite-dimensional compact isotypic space and has an eigenvector there; its eigenspace is an invariant nonzero submodule and hence all of \(V\). Denote the resulting character by \(\eta\). Fix a compact type \(\rho\) of \(SU(2)\)-highest weight \(\ell\). Its scalar-circle weight is fixed by the central character. On its isotypic space
\(E_\rho=V_\rho\otimes M_\rho\), the algebra of the preceding centralizer lemma acts by scalars: its full-central generators act by \(\eta\), and \(\Omega_K\) acts by \(\ell(\ell+2)\).

We record a compression argument which works without any Hilbert completion. The adjoint compact orbit of an enveloping element \(u\) lies in a finite-dimensional PBW-degree space. Therefore its action on \(E_\rho\) can produce only a finite packet of compact types, independent of their multiplicities. All those types have the same scalar-circle weight. The different \(SU(2)\)-highest weights have distinct compact Casimir eigenvalues. A polynomial \(Q(\Omega_K)\) can thus be chosen to be one on \(\rho\) and zero on every other type in this packet. The operator \(u'=Q(\Omega_K)u\) maps \(E_\rho\) into itself and restricts there to its \(\rho\)-compression.

Every matrix \(B\in\operatorname{End}(V_\rho)\) is the restriction of an element of the compact enveloping algebra. Indeed its formal \(H\)-weights in the finite \(\mathfrak{sl}_2\) ladder are distinct. Polynomial interpolation isolates each weight line, and a suitable nonzero string of \(E\)'s or \(F\)'s carries that line to any other; rescaling produces every matrix unit. This also covers the scalar type.

Average \(Bu'\) under compact conjugation. Its orbit is finite dimensional, so this integral is an actual enveloping element in the compact centralizer. On \(E_\rho\), with \(d=\dim V_\rho\), its restriction is
\[
I_{V_\rho}\otimes\frac1d
 \operatorname{Tr}_{V_\rho}\bigl((B\otimes I)A\bigr),
\qquad A=u'|_{E_\rho}.
\]
This identity follows by compact matrix-coefficient orthogonality, whose trace normalization was proved in the complex Hilbert lemma; it is an identity in a finite matrix of linear operators and needs no topology on \(M_\rho\). The averaged element acts by a scalar here. Taking \(B\) to be the successive matrix units makes every entry of \(A\) a scalar times \(I_{M_\rho}\). Hence every enveloping compression on this isotypic space has the form
\[
P_\rho u|_{E_\rho}=A_u\otimes I_{M_\rho}.
\]

If \(M_0\subset M_\rho\) were a proper nonzero linear subspace, the submodule generated by \(V_\rho\otimes M_0\) would have its \(\rho\)-projection still contained in \(V_\rho\otimes M_0\), by the displayed compression formula. That generated subspace is compact invariant too: compact conjugation preserves the enveloping algebra and the starting compact type. It could not fill \(V\), contradicting irreducibility. Thus \(\dim M_\rho=1\).

For separation, use an explicit universal module rather than assume an exhaustion theorem. Form
\[
\mathcal U_{\rho,\eta}
 =\left(
 U(\mathfrak g_{\mathbb C})\otimes_{U(\mathfrak k_{\mathbb C})}V_\rho
 \right)\big/\langle Z-\eta(Z):Z\in Z(U(\mathfrak g_{\mathbb C}))\rangle.
\]
The compact action is \(k(u\otimes v)=(\operatorname{Ad}k)u\otimes\rho(k)v\). It is locally finite and differentiates to the specified compact Lie action; the adjoint PBW orbits and \(V_\rho\) are finite dimensional. Every irreducible module containing \(\rho\) with character \(\eta\) is a quotient, by sending its distinguished generating copy of \(V_\rho\) to that type. In particular the universal module is nonzero and this distinguished copy remains injective.

The compression argument applies in this universal module as well. It did not use finite multiplicity: the finite output type packet came from the adjoint orbit of \(u\), and the centralizer scalars came from the imposed character and the compact Casimir. The distinguished copy consequently already equals the whole \(\rho\)-isotypic space: the universal module is generated by this copy, and every projection of an enveloping translate back to \(\rho\) remains in it.

Every algebraic submodule here is compact invariant: each vector has a finite-dimensional compact orbit, and Lie invariance inside that orbit integrates to the connected group \(U(2)\). Hence its compact projections preserve the submodule. Any proper algebraic submodule of \(\mathcal U_{\rho,\eta}\) has zero \(\rho\)-projection. Otherwise it contains that irreducible compact type and therefore the generators, making it the whole module. The sum of all proper submodules still has zero \(\rho\)-projection and is proper. It is the unique maximal submodule. The quotient by it is the unique irreducible quotient containing \(\rho\). Thus any two irreducible modules with that compact type and central character are isomorphic. This proves separation without a general globalization or Harish-Chandra embedding theorem. \(\square\)



**Lemma — faithful Verma modules and the tensor-Casimir constraint.** Use the standard \(\mathfrak{sl}_2\) generators and \(\Omega=H^2+2H+4FE\). The Verma module \(M_h\) is faithful for
\[
U(\mathfrak{sl}_2)/(\Omega-h(h+2)).
\]
If \(V_\ell\) is the finite highest-weight-\(\ell\) module and \(a=h+1\), the coproduct Casimir on \(M_h\otimes V_\ell\) satisfies
\[
\prod_{j=0}^{\ell}
 \left(\Omega_{\rm total}-((a+\ell-2j)^2-1)\right)=0.
\]

**Proof.** Write the Verma basis as \(F^nv_h\), \(n\ge0\). Commutation gives
\[
HF^nv_h=(h-2n)F^nv_h,\qquad
EF^nv_h=n(h-n+1)F^{n-1}v_h.
\]
The Casimir acts by \(h(h+2)\). In the central quotient, the identities
\[
FE=\frac{h(h+2)-H^2-2H}{4},\qquad
EF=\frac{h(h+2)-H^2+2H}{4}
\]
and normal ordering reduce every element to a finite sum of terms
\(F^rp_r(H)\), \(r\ge0\), and \(q_r(H)E^r\), \(r\ge1\).
They have distinct weight shifts on the Verma basis. For the raising-in-\(F\) terms, vanishing on every sufficiently large \(n\) makes \(p_r(h-2n)\) vanish infinitely often and hence makes \(p_r=0\). For \(E^r\), the scalar is
\[
n(n-1)\cdots(n-r+1)
 \prod_{j=0}^{r-1}(h-n+j+1).
\]
It is nonzero for all but finitely many integer \(n\ge r\). Thus vanishing makes \(q_r(h-2(n-r))\) vanish infinitely often, and \(q_r=0\) also. Every annihilating element is zero in the central quotient. This proves faithfulness for all \(h\), including the reducible integral Verma parameters.

For the tensor identity, let \(\mathfrak b\) be spanned by \(H,E\). The induced module
\(U(\mathfrak{sl}_2)\otimes_{U(\mathfrak b)}
 (\mathbb C_h\otimes V_\ell)\)
maps to \(M_h\otimes V_\ell\) by letting an enveloping element act diagonally. The balancing relations agree on \(H,E\). PBW expresses the source as \(F^n\otimes V_\ell\). On that expression the map is
\[
F^n\otimes v\longmapsto
 \sum_{r=0}^n\binom nr F^{n-r}v_h\otimes F^rv.
\]
It is triangular in the Verma degree with identity diagonal and has an inverse on each bounded-degree subspace. Hence it is an isomorphism.

The flag of \(V_\ell\) formed by its successive highest weights is \(\mathfrak b\)-stable. Its quotients have one-dimensional weights
\(\ell,\ell-2,\ldots,-\ell\) and trivial \(E\)-action. Induction is exact because PBW makes \(U(\mathfrak{sl}_2)\) free as a right \(U(\mathfrak b)\)-module. The tensor therefore has a filtration with quotients \(M_{h+\ell-2j}\), \(0\le j\le\ell\). On each quotient the diagonal Casimir is \((a+\ell-2j)^2-1\). The product of its scalar-subtracted factors annihilates the filtration, since all those factors commute. This proves the stated polynomial identity.

More is established by this argument: the same identity holds in
\[
\bigl(U(\mathfrak{sl}_2)/(\Omega-(a^2-1))\bigr)
 \otimes\operatorname{End}(V_\ell)
\]
for the coproduct Casimir. Faithfulness on the first factor, just proved, makes its tensor matrix representation on \(M_{a-1}\otimes V_\ell\) faithful as well. Thus the identity applies to every representation of the first factor with that scalar Casimir, not only to a Verma realization. Its coefficients are even polynomials in \(a\): replacing \(a\) by \(-a\) reverses the symmetric list \(\ell-2j\) before squaring. They are consequently polynomials in \(a^2\). \(\square\)

**Corollary — an integral principal parameter from a compact type.** Let an irreducible admissible module for the complex real group have scalar Casimirs
\(\Omega_1=a^2-1\), \(\Omega_2=b_0^2-1\), and contain compact highest weight \(\ell\). One can choose a sign of the second square root so that
\[
b=a+\ell-2j,\qquad
m=a-b\in\{-\ell,-\ell+2,\ldots,\ell\}.
\]
In particular \(m\) is an integer of the same parity as \(\ell\).

**Proof.** Consider the universal module generated by that compact type:
\[
U(\mathfrak s\oplus\mathfrak s)
 \otimes_{U(\mathfrak s_{\rm diag})}V_\ell.
\]
PBW identifies it with \(U(\mathfrak s)\otimes V_\ell\). The first factor acts by left multiplication. A generator \(X\) of the second factor acts by
\[
u\otimes v\longmapsto -uX\otimes v+u\otimes Xv:
\]
subtract its first-factor copy from the diagonal generator and use the balancing relation. Negative right multiplication is a Lie representation, and its Casimir is right multiplication by \(\Omega\), equal to left multiplication by the same central element. After imposing \(\Omega_1=a^2-1\), the matrix identity from the lemma therefore applies to \(\Omega_2\). This universal module maps to the given module through its included compact type. The polynomial relation gives
\[
\prod_{j=0}^{\ell}
 \bigl(b_0^2-(a+\ell-2j)^2\bigr)=0.
\]
Choose the corresponding root \(b=a+\ell-2j\). The asserted integrality and parity follow. Scalar central directions can be imposed separately and do not affect this traceless calculation. \(\square\)



**Lemma — the finite head and infinite tail of complex induction.** Put
\[
\chi=\mu_1/\mu_2,\qquad
m=n_1-n_2,\qquad s=t_1-t_2.
\]
The full finite-vector induction is simple unless
\(\chi=z^p\bar z^q\) or \(z^{-p}\bar z^{-q}\), with integers \(p,q\ge1\).
At the negative ratio it has a unique proper nonzero submodule, which is finite dimensional and has compact highest weights
\[
|p-q|,\ |p-q|+2,\ldots,p+q-2.
\]
At the positive ratio its unique proper nonzero submodule is the infinite tail with compact highest weights \(p+q,p+q+2,\ldots\). In either case this submodule and its quotient are simple.

**Proof of the finite submodules.** We first recall the exact compact tensor decomposition needed below. The character of the highest-weight-\(r\) compact module is
\(x^r+x^{r-2}+\cdots+x^{-r}\). Multiplying this expression by the corresponding character for \(q\), and counting each weight, gives
\[
V_r\otimes V_q
 =\bigoplus_{j=0}^{\min(r,q)}V_{r+q-2j}.
\]
Indeed the multiplicity of a weight in the product is the number of pairs producing it; it increases by one up to the shorter ladder, is constant where that ladder is entirely overlapped, and decreases symmetrically. The displayed sum has exactly the same counts. Compact complete reducibility and the finite highest-weight classification then prove the formula. Complex conjugation on the \(SU(2)\) standard module gives its dual, which is isomorphic to itself through its invariant alternating form. Thus the same list applies to a holomorphic symmetric power tensored with an antiholomorphic one.

A finite-dimensional simple submodule \(A\) of induction has scalar action of the two central directions and, by the finite \(\mathfrak{sl}_2\) highest-weight classification, traceless representation
\(\operatorname{Sym}^r\mathbb C^2\otimes\operatorname{Sym}^q\overline{\mathbb C^2}\), \(r,q\ge0\). The elementary tensor-product assertion for the two commuting simple factors follows by taking an isotypic decomposition for the first: its multiplicity space carries the second, and simplicity forces it to be simple too. The compact scalar circle then gives a smooth scalar character \(\chi_0\) such that the full representation is
\[
\rho=\chi_0(\det)\,
 \operatorname{Sym}^r\mathbb C^2
 \otimes\operatorname{Sym}^q\overline{\mathbb C^2}.
\]
To check that \(\chi_0\) exists, subtract the algebraic scalar-circle weight \(r-q\) from the given central-circle weight \(N\). The result is even because \(N\equiv r+q\pmod2\) on the compact types just listed. Half of this difference is the integer angular exponent of \(\chi_0\); its radial exponent is determined by the remaining scalar derivative. These exponents define a character of \(\mathbb C^\times\). The explicit \(\rho\) and \(A\) then have the same Lie action and compact action.

Evaluation at the identity is a nonzero functional \(\lambda\) on \(A\). Here this does not require a globalization theorem. For any real Lie vector \(X\), the finite column of functions from \(A\), restricted to \(g\exp(tX)\), satisfies the constant-matrix differential equation prescribed by \(d\rho(X)\). Its initial value determines it uniquely. Products of such exponentials cover the connected group. Consequently
\[
f_v(g)=\lambda(\rho(g)v).
\]
If evaluation were zero, all the functions would be zero. Left induction covariance requires \(\lambda\) to be fixed by the upper unipotent and to have diagonal character
\(\mu_1(a)\mu_2(d)|a/d|_{\mathbb C}^{1/2}\).
In the symmetric-power monomial basis the upper-unipotent-invariant covector is uniquely the coefficient of
\(e_2^r\otimes\bar e_2^q\). This is also immediate from the raising ladder: a covector annihilating the raising image can see only its bottom basis vector. Its diagonal character in \(\rho\) is
\(\chi_0(ad)d^r\bar d^q\). Comparison for independent \(a,d\) gives
\[
\mu_1=\chi_0|\cdot|_{\mathbb C}^{-1/2},\qquad
\mu_2=\chi_0 z^r\bar z^q|\cdot|_{\mathbb C}^{1/2},
\qquad
\chi=z^{-(r+1)}\bar z^{-(q+1)}.
\]
Conversely these equalities make the matrix coefficients of that covector a submodule of the induction. Their map is nonzero and has zero kernel by finite simplicity. For \(\chi=z^{-p}\bar z^{-q}\), it embeds
\(\chi_0(\det)\operatorname{Sym}^{p-1}\otimes
\operatorname{Sym}^{q-1}\overline{\mathbb C^2}\),
with \(\chi_0=\mu_1|\cdot|_{\mathbb C}^{1/2}\).
Its compact list is precisely the stated finite head. The principal compact multiplicity one shows that there is only one such head. A finite submodule is completely reducible: the traceless factors are semisimple in finite dimension, and the scalar directions already act by scalars on the whole induction. Thus every nonzero finite submodule contains this simple head, and no other finite simple type is possible. It equals the head.

**Proof that these are all submodules.** A compact-invariant subspace of induction is a sum of its compact types, since their multiplicities are one. The noncompact traceless Lie vectors transform as \(V_2\). The tensor decomposition just proved therefore permits only changes \(\ell\mapsto\ell-2,\ell,\ell+2\). The scalar and compact vectors preserve the type. If a nonzero submodule \(W\) has a first missing type above its least type, its finite initial block is itself an invariant submodule: at its lower boundary the output below \(W\) is zero, and at its upper boundary the missing type has zero output because \(W\) is invariant. Otherwise \(W\) is the whole upper tail and is cofinite dimensional.

There is a nondegenerate invariant bilinear pairing of finite-vector modules
\[
I(\mu_1,\mu_2)\times I(\mu_1^{-1},\mu_2^{-1})
 \longrightarrow\mathbb C,\qquad
(f,h)\longmapsto\int_{U(2)}f(k)h(k)\,dk.
\]
We verify invariance, including its modulus. In the compact projective coordinate choose a unit bottom row \(r\). Right multiplication by \(g\) induces the projective map \(r\mapsto rg/\|rg\|\); its area Jacobian is
\[
J_g(r)=\frac{|\det g|_{\mathbb C}}{\|rg\|^4}.
\]
In a local coordinate \(r=(x,1)/(1+|x|^2)^{1/2}\), this follows by differentiating the fractional linear map and using the projective area density
\((1+|x|^2)^{-2}d^2x\). If \(kg=bk'\), then \(|d|=\|rg\|\), \(ad=\det g\), and the product of the two inducing multipliers is
\(|a/d|_{\mathbb C}=J_g(r)\). The angular and radial character factors cancel. Change of projective variables consequently proves right-group invariance of the integral on smooth compact models, and differentiation proves Lie invariance on their finite vectors. It is nondegenerate: on \(K\), choose \(h=\bar f\), which has the required inverse torus covariance and is again compact finite. Orthogonality of compact types gives perfect pairings type by dual type.

Thus a proper nonzero \(W\) has a proper nonzero annihilator \(W^\perp\) in the inverse induction; missing compact types account exactly for that annihilator, and double annihilation returns \(W\). Each of \(W,W^\perp\) either contains a finite simple head, by the finite-initial-block argument, or is an upper tail. If one is an upper tail, its annihilator is finite dimensional and contains a finite simple head. They cannot both contain finite heads: the preceding necessary condition would make both \(\chi\) and \(\chi^{-1}\) negative powers with both exponents strictly negative. Therefore any proper submodule requires one of the two ratios in the lemma.

For the negative ratio, the head exists and every proper \(W\) must be exactly it. In fact \(W^\perp\) cannot have a finite head, so it is a tail; hence \(W\) is finite dimensional and equals the unique head. For the positive ratio, the annihilator of the inverse induction's head gives a proper infinite tail, and the same argument makes it the only proper nonzero submodule. Its compact list is the complement of the inverse head's list, namely \(\ell\ge p+q\). Uniqueness of the proper submodule proves that both it and its quotient are simple. Outside the two ratios there can be no proper nonzero submodule. \(\square\)


**Theorem — full complex classification and exact parameter identification.** Every irreducible admissible
\((\mathfrak{gl}_2(\mathbb C)_{\mathbb R},U(2))\)-module is a constituent of normalized induction. Define
\(\pi(\mu_1,\mu_2)=I(\mu_1,\mu_2)\) when the induction is simple; at either reducible ratio in (8.1), define \(\pi(\mu_1,\mu_2)\) to be its finite-dimensional constituent. Then this parametrizes all simple admissible modules, and
\[
\pi(\mu_1,\mu_2)\simeq\pi(\mu'_1,\mu'_2)
 \quad\Longleftrightarrow\quad
 \{\mu_1,\mu_2\}=\{\mu'_1,\mu'_2\}.
\]
The infinite constituent at the ratio \(z^p\bar z^q\), \(p,q\ge1\), is a simple full principal series with the same product of inducing characters and ratio \(z^p\bar z^{-q}\).

**Proof of exhaustion.** Let \(V\) be any such simple module and choose a compact type with scalar-circle weight \(N\) and \(SU(2)\)-highest weight \(\ell\). Its center is scalar by the compact-corner lemma. The scalar directions define the character
\[
\omega(z)=(z/|z|)^N|z|_{\mathbb C}^{T}
\]
for some \(T\in\mathbb C\). This is the actual central action: the circle exponent is fixed by \(K\), and the radial scalar derivative determines \(T\). The two traceless Casimir scalars may be written \(a^2-1,b_0^2-1\). The tensor-Casimir corollary chooses
\[
b=a+\ell-2j,\qquad
m=a-b=-\ell+2j,\qquad s=(a+b)/2.
\]
Since \(N\equiv\ell\pmod2\), the integers
\[
n_1=(N+m)/2,\qquad n_2=(N-m)/2
\]
are well defined. Set \(t_1=(T+s)/2,\ t_2=(T-s)/2\), and form the characters
\(\mu_i(z)=(z/|z|)^{n_i}|z|_{\mathbb C}^{t_i}\).
Their product is \(\omega\); their induction contains our compact type because \(|m|\le\ell\) with the required parity.

We check its infinitesimal character directly. Locally write
\(\mu_1/\mu_2=z^{p_0}\bar z^{q_0}\), with
\(p_0=s+m/2=a\), \(q_0=s-m/2=b\). This notation for possibly nonintegral powers means the differentiated local character; its global single-valuedness was already ensured by the integer angular exponent \(m\). On the open Bruhat coordinate \(x\), the holomorphic traceless operators are
\[
E=\partial_x,\quad
H=-2x\partial_x-(p_0+1),\quad
F=-x^2\partial_x-(p_0+1)x.
\]
For example right diagonal translation scales \(x\) by \(d/a\) and contributes the inducing multiplier
\((\mu_1/\mu_2)(d)|d/a|_{\mathbb C}^{1/2}\) when \(ad=1\), giving \(H\); right unipotent translation gives \(E\), and the opposite unipotent gives the displayed \(F\). They satisfy the standard brackets. Direct substitution in \(H^2+2H+4FE\) cancels both derivative terms and gives \(p_0^2-1\). The antiholomorphic operators similarly give \(q_0^2-1\). The second-factor Chevalley identification used in the compact lemmas preserves its Casimir. Thus the induction shares both Casimir scalars and both scalar-direction derivatives with \(V\), hence the entire central character by the proved center description.

The finite-head/tail lemma accounts for every constituent of this induction and for every compact type in it: at a reducible point the head and tail lists partition the compact list, and otherwise the induction is simple. Choose its simple constituent containing our type. It shares the central character and that type with \(V\). Compact-corner separation makes it isomorphic to \(V\). This proves exhaustion without an embedding theorem.

**Proof of exchange and of the infinite companion.** Exchanging the two characters changes \(m,s\) to \(-m,-s\). It preserves the product, both squared Casimir roots, and every compact type of the full induction. In the simple case separation gives an isomorphism of the two full inductions. In the reducible case their finite constituents have the same head list and central character and are likewise isomorphic. Their infinite constituents also have the same tail list and are isomorphic.

For the positive ratio \(z^p\bar z^q\), its \(m=p-q\) and \(2s=p+q\). With the same product \(\omega\), take new \(m'=p+q\), \(2s'=p-q\). These define actual characters: \(m'\equiv m\equiv N\pmod2\). Their ratio is \(z^p\bar z^{-q}\), whose induction is simple by the finite-head/tail lemma. Its Casimir roots are \(p,-q\), so their squares and its center agree with the original. Its compact support begins at \(\ell=p+q\), exactly the original infinite tail. Separation identifies the two. This also identifies the infinite quotient for the negative original ratio, by the exchange already proved. Every infinite simple admissible module is consequently a simple full induction; the remaining simple modules are the finite constituents used in the definition of \(\pi\).

**Proof of no repetition.** The center determines \(N,T\). The traceless central scalars determine the two roots \(a,b\) up to their independent signs, with the factors kept in their holomorphic and antiholomorphic order. For any inducing pair these are
\[
a=s+m/2,\qquad b=s-m/2,\qquad m\in\mathbb Z,\quad m\equiv N\pmod2.
\]
Changing both signs is precisely the exchange of the two characters. The only possible further unordered pair comes from changing one sign, say \(b\mapsto-b\); it changes \(m\) to \(2s\) and \(2s\) to \(m\). It is available only if \(2s\) is an integer congruent to \(N\) modulo two. If that condition fails there is no additional pair.

If it holds and \(|2s|>|m|\), the original roots \(a,b\) are nonzero integers with the same sign. Its ratio is reducible, so its canonical \(\pi\) has the finite head list ending at \(|2s|-2\). The alternative roots have opposite signs and give a simple induction with compact list starting at \(|2s|\). They have no type in common and cannot be isomorphic. If \(|m|>|2s|\), the original induction is simple with compact list starting at \(|m|\), and the alternative canonical \(\pi\) is finite with list ending at \(|m|-2\); again they differ. Equality means \(a=0\) or \(b=0\). Flipping that zero changes nothing, and flipping the other root is already the simultaneous sign change, hence the ordinary character exchange. These cases exhaust all root choices. The unordered pair is therefore unique. \(\square\)


Write
\[
\mu_i(z)=\left(\frac z{|z|}\right)^{n_i}|z|_{\mathbb C}^{t_i},
\qquad n_i\in\mathbb Z,
\]
where the unadorned \(|z|\) is the ordinary radius. The classification theorem identifies every infinite simple module with a simple full induction and allows its parameters to be exchanged. Consequently the ordered Gaussian proposition below covers every generic complex simple module through its explicit continuous model. The general moderate-model theorem following that proposition proves uniqueness for arbitrary moderate realizations as well. The finite-dimensional nongeneric factor in (8.2) uses its proved inducing pair. The matrix-factor proposition below proves that its entire matrix-coefficient family has exactly this product, using the all-field induction kernel of Lesson 9, Lemma 8.2:
\[
L(z_0,\pi(\mu_1,\mu_2))
=\prod_{i=1}^2\Gamma_{\mathbb C}(z_0+t_i+|n_i|/2),
\qquad
\varepsilon(z_0,\pi,\psi_{\mathbb C})=i^{|n_1|+|n_2|}.
\tag{8.2}
\]
**Proposition — the complex principal Gaussian model and factors.** Suppose \(I_{\mathbb C}(\mu_1,\mu_2)\) is irreducible, and order its parameters so that \(\operatorname{Re}(t_1-t_2)\ge0\). In its explicit smooth compact model, the continuous Whittaker functional for \(\psi_{\mathbb C}\) exists and is unique up to a scalar. Its full finite-vector family has
\[
W_\Psi(d(y))=|y|_{\mathbb C}^{1/2}
 \int_{\mathbb C^\times}\mu_1(u)\mu_2(y/u)
 \Psi(u,y/u)\,d^\times u,
\]
where \(\Psi\) runs through polynomials in \(u,\bar u,v,\bar v\) times
\(e^{-2\pi(|u|^2+|v|^2)}\). Right Weyl translation is the positive-character Fourier transform with its two coordinates exchanged. For this irreducible principal series, its \(L\)- and epsilon factors are exactly (8.2).

**Proof of the functional.** Put \(s=t_1-t_2\) and \(\chi=\mu_1\mu_2^{-1}\). On the open Bruhat line write \(\phi_f(x)=f(w_0n(x))\), \(x\in\mathbb C\). Iwasawa decomposition gives, with respect to the ordinary radius,
\[
|\nabla^j\phi_f(x)|\le C_j(f)(1+|x|)^{-2-2\operatorname{Re}s-j}.
\]
The radial modulus is \((1+|x|^2)^{-1-s}\); differentiating its compact angular and projective coordinates gives these bounds. The constants are controlled by compact smooth seminorms.

For \(\operatorname{Re}s>0\), the Jacquet integral
\(\Lambda(f)=\int_{\mathbb C}\phi_f(x)\psi_{\mathbb C}(-x)\,dx\)
is absolutely convergent. It has a continuous extension to
\(\operatorname{Re}s>-\tfrac12\), including the required boundary. If \(x=u+iv\), define it there by
\[
\Lambda(f)=\frac1{4\pi i}
 \int_{\mathbb C}\partial_u\phi_f(x)e^{-4\pi iu}\,dx.
\]
The derivative is absolutely integrable in two real dimensions in precisely this larger range. This agrees with the original integral where that converges. Inserting a cutoff supported in \(|x|\le2R\), equal to one on \(|x|\le R\), proves the agreement with its oscillatory cutoff limit: the integration-by-parts boundary is \(O(R^{-1-2\operatorname{Re}s})\), and tends to zero. The same estimates prove continuity and holomorphy on smaller closed parameter strips. Translating the whole derivative integral gives
\(\Lambda(\pi(n(b))f)=\psi_{\mathbb C}(b)\Lambda(f)\).
A smooth test function supported in the open line makes the functional nonzero.

Its uniqueness among continuous functionals can be proved on this compact model. Such a functional is a distribution on the compact projective line, with its inducing line bundle. On the open line, the translation eigencondition makes it a multiple of integration against \(\psi_{\mathbb C}(-x)\). Here is the elementary distribution argument. After removing that exponential, both real derivatives of the distribution vanish. Every compactly supported test function of integral zero is a sum of two compactly supported derivatives: integrate in the first coordinate after subtracting \(\rho(u)\int\phi(u,v)\,du\), where \(\int\rho=1\); its remaining one-variable integral has total integral zero and is a derivative in the second coordinate. Thus the distribution annihilates every zero-integral test and is a constant multiple of Haar integration.

The difference of two proposed extensions is supported at the single point at infinity. A distribution supported at a point depends on finitely many jets. Indeed continuity gives a finite derivative-order bound; multiply a test vanishing through that order by a shrinking cutoff. Taylor's estimate makes the bounded derivatives of this product tend to zero, while support at the point leaves its distribution value unchanged. Therefore that value is zero, proving the finite-jet assertion.

Near infinity use the coordinate \(z=1/x\). Right unipotent translation sends \(z\) to \(z/(1+bz)\). Its line-bundle multiplier is one at \(z=0\) and has infinitesimal terms of degree at least one. The infinitesimal action on finite jets raises Taylor degree: the vector field has coefficients of degree at least two, and the multiplier term has degree at least one. On the dual finite-jet space it is consequently nilpotent. The required real unipotent eigenvalue is \(4\pi i\), which a nilpotent operator cannot have. No distribution supported at infinity can satisfy the eigencondition. This proves continuous-functional uniqueness.

**Proof of the full Gaussian family.** With the measures of (0.1), form the row-vector section
\[
f_\Phi(g)=\chi(-1)\mu_1(\det g)|\det g|_{\mathbb C}^{1/2}
 \int_{\mathbb C^\times}\chi(t)|t|_{\mathbb C}
 \Phi((0,t)g)\,d^\times t.
\]
It is smooth for \(\operatorname{Re}s>-1\). Changing \(t\) to \(td\) proves the exact normalized left covariance under
\(\left(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}\right)\).
Right translation is the linear Schwartz action
\(\Phi(v)\mapsto\mu_1(\det h)|\det h|_{\mathbb C}^{1/2}\Phi(vh)\).
Gaussian polynomials are stable under its differentiated real Lie action and under \(U(2)\), whose action preserves degree and the Gaussian. Their sections thus form a finite-vector submodule.

This submodule is nonzero. Write \(m=n_1-n_2\). Use
\(\Phi(u,v)=\bar v^m e^{-2\pi(|u|^2+|v|^2)}\) if \(m\ge0\), or \(v^{-m}\) times that Gaussian if \(m<0\). Its section at the identity is a nonzero constant times
\(\Gamma_{\mathbb C}(s+1+|m|/2)\), whose argument has positive real part. Irreducibility makes its image the full finite-vector module.

For \(\operatorname{Re}s>0\), insert this section in the Jacquet integral. The row identity
\((0,t)w_0n(x)d(y)=(-ty,-tx)\) allows absolute Fubini. After \(v=-tx\), its absolute majorant is
\[
\int_{\mathbb C^\times}|t|_{\mathbb C}^{\operatorname{Re}s}
 \int_{\mathbb C}|\Phi(-ty,v)|\,dv\,d^\times t.
\]
It converges at zero for \(\operatorname{Re}s>0\) and at infinity by Schwartz decay. The additive Jacobian is \(|t|_{\mathbb C}^{-1}\). Put
\[
\Psi(u,v)=\int_{\mathbb C}\Phi(u,x)\psi_{\mathbb C}(-vx)\,dx.
\]
The further substitution \(u=-ty\) cancels both \(\chi(-1)\) factors, and
\(\mu_1(y)\chi(y)^{-1}=\mu_2(y)\) gives exactly the asserted hyperbola formula. The left side is holomorphic for \(\operatorname{Re}s>-\tfrac12\), by the derivative-integral argument, and the hyperbola side is entire in \(s\) for fixed \(y\ne0\). Continuation from the absolute half-plane therefore proves the identity at \(\operatorname{Re}s=0\).

The self-dual complex Fourier transform for \(\psi_{\mathbb C}\) and \(dx=2\,du\,dv\) preserves \(e^{-2\pi|x|^2}\). Differentiating this Gaussian identity shows that partial Fourier transform is bijective on complex Gaussian polynomials; its inverse is the opposite-sign transform. Thus the full finite-vector image is exactly the family in the statement.

Right translation by \(w_0\) replaces \(\Phi(u,v)\) by \(\Phi(-v,u)\). Partial Fourier transform and inversion give
\[
\Psi^{w_0}(u,v)=\widehat\Psi(v,u),\qquad
\widehat\Psi(a,b)=\int_{\mathbb C^2}
 \Psi(x,z)\psi_{\mathbb C}(ax+bz)\,dx\,dz.
\]
This proves the precise Weyl action with the given self-dual measures.

**Proof of the factors.** For a tensor Gaussian test, substituting \(y=uv\) in
\(M_{z_0}(W)=\int W(d(y))|y|_{\mathbb C}^{z_0-1/2}d^\times y\)
gives the product of the two scalar complex Tate integrals. Absolute convergence holds in a common right half-plane. For a monomial \(x^a\bar x^b\) in the \(i\)-th coordinate, angular integration makes its integral zero unless
\(a-b+n_i=0\). In the nonzero case \(a+b=|n_i|+2r\), \(r\ge0\). Polar integration with (0.1) then gives
\[
4\int_0^\infty
 \rho^{2(z_0+t_i)+|n_i|+2r}e^{-2\pi\rho^2}\frac{d\rho}{\rho}
 =\Gamma_{\mathbb C}(z_0+t_i+|n_i|/2+r).
\]
Dividing by the factor with \(r=0\) gives
\((2\pi)^{-r}(z_0+t_i+|n_i|/2)_r\), a polynomial. Every finite-vector Mellin integral is therefore entire after division by the product in (8.2). The tensor test with \(a=\max(-n_i,0)\), \(b=\max(n_i,0)\) in each coordinate has normalized integral exactly one. This also proves that its Whittaker function is nonzero. The finite-vector Whittaker map therefore has a proper invariant kernel; irreducibility makes that kernel zero.

Put \(\omega=\mu_1\mu_2\) and use the dual Weyl Mellin integral
\[
\widetilde M_{1-z_0}(W)=
 \int_{\mathbb C^\times}W(d(y)w_0)\omega(y)^{-1}
 |y|_{\mathbb C}^{1/2-z_0}\,d^\times y.
\]
The Fourier-and-swap formula and \(y=uv\) make its two characters exactly \(\mu_1^{-1},\mu_2^{-1}\), with exponent \(1-z_0\). Apply the scalar complex Tate functional equation proved in NT-ADL-08, with its explicit additive-character change to \(\psi_{\mathbb C}\). The positive Fourier transform contributes \(i^{|n_i|}\) in each coordinate. The checked Fourier-and-swap action turns the dual Weyl Mellin integral into precisely those two dual Tate integrals, with characters \(\mu_i^{-1}\) and exponents \(1-z_0\). Thus, for every finite vector,
\[
\frac{\widetilde M_{1-z_0}(W)}
 {\prod_i\Gamma_{\mathbb C}(1-z_0-t_i+|n_i|/2)}
 =i^{|n_1|+|n_2|}
 \frac{M_{z_0}(W)}
 {\prod_i\Gamma_{\mathbb C}(z_0+t_i+|n_i|/2)}.
\]
This proves (8.2) for this irreducible principal series, with both its phase and dual shifts checked.

The classification theorem above identifies every infinite admissible simple module and permits this parameter ordering. The following theorem identifies every arbitrary moderate realization with this explicit continuous Gaussian model. The following matrix-factor proposition supplies the finite-dimensional case. \(\square\)



**Proposition — the matrix factors of the finite-dimensional modules.** The finite-dimensional real factors in (6.10), and the complex factors in (8.2), are the factors of their whole matrix-coefficient zeta families. Every such integral is entire after division by the displayed \(L\)-factor. A finite sum of normalized integrals is a nonzero exponential in the zeta variable. With the positive Fourier conventions of this lesson, the matrix functional equation has
\[
\gamma(z,\pi,\psi)=
 \prod_{i=1}^2\gamma(z,\mu_i,\psi),\qquad
\varepsilon(z,\pi,\psi)=
 \prod_{i=1}^2\varepsilon(z,\mu_i,\psi).
\]
In particular the real finite module has epsilon \(i^{\epsilon_1+\epsilon_2}\), and the complex finite module has epsilon \(i^{|n_1|+|n_2|}\).

**Proof.** Use the matrix integral and trace Fourier transform of Lesson 9, (8.1). Its Lemma 8.2 was proved for all three kinds of local field. The compact induction pairing, upper-triangular measure and two-variable Fourier marginal reduce every induced coefficient integral to the two Tate integrals. The finite-dimensional module is a subquotient of that induction by the classifications proved here. Extend a finite compact-type functional or lift a finite compact-type vector, as appropriate. Thus every coefficient of the finite module is an induced coefficient; its normalized holomorphy and product functional equation follow from that lemma.

We must still show that this pole bound is attained within the finite constituent. Its least compact type occurs once in the induction and belongs entirely to that constituent. For the real group it is the weight-zero type with reflection \(\delta\) when \(m\) is even, and the two-dimensional weight-one type when \(m\) is odd. For the complex group it has \(SU(2)\)-highest weight
\(\ell=|n_1-n_2|\), with central-circle exponent \(n_1+n_2\), as proved in the finite-head classification.

We construct a Gaussian matrix test supported in precisely this compact type on both sides. Write a matrix as
\(Y=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\).
For \(\mathbb R\), multiply \(e^{-\pi(a^2+b^2+c^2+d^2)}\) by the following polynomial:
\[
\begin{array}{c|c}
(\epsilon_1,\epsilon_2)&P(Y)\\ \hline
(0,0)&1\\
(1,1)&ad-bc\\
(1,0)&a-ib\\
(0,1)&c-id
\end{array}
\]
The first two are respectively the trivial and determinant compact types on both sides. Each of the latter two lies in the weight-one compact type on both sides. One may check this directly by multiplying by a rotation: each relevant row or column has only weights \(1,-1\); reflection exchanges them. Integrating the upper-triangular marginal over \(b\), with \(c=0\), kills its odd Gaussian term. The remaining polynomial is respectively \(1,ad,a,-id\). It therefore gives the tensor of the fundamental real Tate Gaussian tests for the two specified sign characters, up to a nonzero constant.

For \(\mathbb C\), use the Gaussian
\(e^{-2\pi(|a|^2+|b|^2+|c|^2+|d|^2)}\).
Put \(p_n(z)=\bar z^n\) for \(n\ge0\), and \(p_n(z)=z^{-n}\) for \(n\le0\). Choose \(P\) as follows; a zero exponent is interpreted as one:
\[
\begin{array}{c|l}
\text{condition}&P(Y)\\ \hline
n_1,n_2\ge0&
 \overline{\det Y}^{\,\min(n_1,n_2)}
 \bar a^{\,\max(n_1-n_2,0)}
 \bar d^{\,\max(n_2-n_1,0)}\\
n_1,n_2\le0&
 (\det Y)^{\,\min(-n_1,-n_2)}
 a^{\,\max(n_2-n_1,0)}
 d^{\,\max(n_1-n_2,0)}\\
n_1\ge0,\ n_2\le0&\bar a^{\,n_1}d^{-n_2}\\
n_1\le0,\ n_2\ge0&a^{-n_1}\bar d^{\,n_2}
\end{array}
\]
On an upper-triangular matrix each polynomial becomes exactly
\(p_{n_1}(a)p_{n_2}(d)\). Its marginal is consequently a nonzero constant times the tensor of the fundamental complex Tate tests.

We verify the compact type, rather than assuming it from the diagonal value. Determinants are invariant under \(SU(2)\). In the first two cases the remaining power of one matrix entry lies in a symmetric power of degree \(|n_1-n_2|\), on either side. In the mixed-sign cases, write
\(k=\left(\begin{smallmatrix}u&v\\-\bar v&\bar u\end{smallmatrix}\right)\).
For example, under right multiplication both \(\bar a\) and \(d\) are linear in \((\bar u,v)\), and under left multiplication both are linear in \((\bar u,\bar v)\). Their product is homogeneous of degree \(n_1-n_2\). The other mixed case is the conjugate calculation. The space of homogeneous polynomials of degree \(\ell\) in these two variables is the irreducible symmetric power \(V_\ell\); hence there are no smaller compact types. The scalar circle acts on \(P\) with exponent \(-n_1-n_2\). In the induction kernel this is paired with the required exponent \(n_1+n_2\); the inverse \(h\)-argument supplies the dual type on the other side. Thus both sides select exactly the least compact type of the finite constituent and its dual.

Apply the evaluation argument in the last paragraph of Lesson 9, Lemma 8.2, to this kernel. Its finite compact-type spaces now consist only of that least type. The coefficient vectors and dual vectors representing evaluation at \((e,e)\) can therefore be chosen inside this type. If the finite constituent is a submodule, those vectors belong to it. If it is a quotient, the corresponding dual type annihilates the other constituent, which has only the disjoint upper-tail types; the vectors project to the quotient. In either case the evaluation is a finite sum of coefficients of the finite-dimensional module itself. Its diagonal marginal is the tensor of fundamental Tate tests just computed, so this sum is \(L(z,\mu_1)L(z,\mu_2)\) times a nonzero exponential. The asserted bound is attained.

Finally apply the same induction argument to the inverse pair for the contragredient. The product Tate gamma formula then has exactly its two \(L\)-ratios. Cancelling these ratios gives the epsilon product above, with the phases proved in NT-ADL-08 and the character-change rule at the start of this lesson. This proves both the matrix interpretation and the all-vector assertions for the nongeneric modules. No Whittaker functional on a finite-dimensional module has been used. \(\square\)

**Theorem — the general moderate complex Whittaker model.** For every infinite-dimensional simple admissible complex module \(V\), there is exactly one finite-vector space of smooth functions on \(\mathrm{GL}_2(\mathbb C)\), equivalent to \(V\), with left covariance \(\psi_{\mathbb C}\) and polynomial growth along \(d(t)\), \(t\to+\infty\). Its functions are the Gaussian Whittaker functions of the preceding proposition. The same uniqueness holds if a proposed model is initially assumed continuous and invariant under the smooth compact-finite convolution algebra: its compact finite vectors are automatically smooth.

**Proof of existence and growth.** The classification identifies \(V\) with a simple full induction, and exchange orders its radial parameters. The preceding proposition supplies its injective finite-vector Whittaker realization. Its continuous functional has finite order in compact smooth seminorms. Right translation by \(g\) in the compact model acts by a projective linear substitution and its inducing line-bundle multiplier. If the bottom unit row is \(r\), its denominator has size \(\|rg\|\), bounded below by the smallest singular value of \(g\). Differentiating this substitution and the multiplier a fixed number of times therefore bounds every required seminorm by a fixed power of
\[
1+\|g\|+\|g^{-1}\|.
\]
The character multipliers satisfy the same bound: their angular parts have absolute value one, and their radial powers are bounded by fixed powers of singular values and their inverses. Thus for each finite vector \(v\),
\(W_v(g)=\Lambda(\pi(g)v)\) has polynomial growth in this matrix norm. In particular it is polynomial along \(d(t)\). Smoothness follows from the explicit compact action and continuity of \(\Lambda\).

**Proof of smoothness for an initially continuous model.** Each compact isotypic space is finite dimensional by admissibility. Smooth compactly supported approximate identities, averaged under compact conjugation, preserve it. Insert its compact isotypic projector on both sides of each kernel. The resulting kernels are still smooth and compactly supported, are compact finite on both sides, and belong to the stipulated convolution algebra. Their action on the chosen isotypic space is unchanged, and they have smooth image on continuous functions. They converge to the identity uniformly on every compact set of group points. Finitely many point evaluations separate a basis of this finite-dimensional function space: select them successively, since a nonzero function has a nonzero value. Convergence at those points consequently gives convergence in its finite-dimensional topology, so the smoothing operator is invertible there once sufficiently close to the identity. Every vector of that type is therefore smooth. Taking the compact types proves the assertion. Differentiated right translation agrees with the prescribed Lie action. Indeed differentiation of these kernels yields kernels in the same algebra: differentiating a compact-finite kernel adds only the finite adjoint compact orbit of the Lie vector to its compact-type packet. On a chosen isotypic space use the invertible smoothing kernel just constructed. The identity obtained by differentiating its right convolution expresses \(R_X\) through the action of the differentiated kernel and the inverse smoothing operator. A convolution-module isomorphism therefore intertwines this derivative with the corresponding Lie action in the explicit principal model.

**Proof of the radial equations.** Remove the center and work on \(\mathrm{SL}_2(\mathbb C)\). In the original holomorphic and antiholomorphic complexified factors use \(E_1,F_1,H_1\) and \(E_2,F_2,H_2\), before the second-factor Chevalley change. Its Casimir scalar is still \(b^2-1\); the first is \(a^2-1\). The compact complexification is generated by
\[
C_H=H_1-H_2,\qquad
C_E=E_1-F_2,\qquad C_F=F_1-E_2.
\]
These satisfy the standard \(\mathfrak{sl}_2\) brackets. Choose any occurring compact type \(V_\ell\) and the basis
\[
v_j=F_K^jv_0,\qquad
H_Kv_j=(\ell-2j)v_j,\quad
E_Kv_j=j(\ell-j+1)v_{j-1},\quad
F_Kv_j=v_{j+1},
\]
where \(0\le j\le\ell\), and vectors outside this interval are zero. In a proposed function model set
\[
a_t=\operatorname{diag}(t^{1/2},t^{-1/2}),\qquad
\phi_j(t)=W_{v_j}(a_t),\quad
D=t\,d/dt,\quad k_j=\ell/2-j.
\]

Left unipotent covariance and
\(a_tn(x)=n(tx)a_t\) give, at \(a_t\),
\[
(R_{E_1}W_v)(a_t)=(R_{E_2}W_v)(a_t)
 =2\pi it\,W_v(a_t).
\]
Here the holomorphic and antiholomorphic infinitesimal derivatives of
\(\psi_{\mathbb C}(x)=e^{2\pi i(x+\bar x)}\) are both \(2\pi i\). Their product is \(-4\pi^2t^2W_v(a_t)\); the two unipotent directions commute. Real diagonal variation gives \(R_{H_1}+R_{H_2}=2D\), and compact diagonal variation gives \(R_{H_1}-R_{H_2}=2k_j\) on the \(j\)-th coordinate. Hence \(R_{H_1}\) and \(R_{H_2}\), including their squares on that weight, restrict to \(D+k_j\) and \(D-k_j\).

Use \(F_1=C_F+E_2\) and
\(C_FE_1=E_1C_F-H_1\). Then
\[
(R_{F_1E_1}W_{v_j})(a_t)
 =-4\pi^2t^2\phi_j+2\pi it\,\phi_{j+1}
  -(D+k_j)\phi_j.
\]
Similarly \(F_2=E_1-C_E\) and
\(C_EE_2=E_2C_E+H_2\) give
\[
(R_{F_2E_2}W_{v_j})(a_t)
 =-4\pi^2t^2\phi_j
  -2\pi it\,j(\ell-j+1)\phi_{j-1}
  -(D-k_j)\phi_j.
\]
Substitution in \(\Omega_i=H_i^2+2H_i+4F_iE_i\) proves the coupled equations, with all Fourier constants included:
\[
\begin{aligned}
\bigl((D+k_j-1)^2-16\pi^2t^2-a^2\bigr)\phi_j
 &=-8\pi it\,\phi_{j+1},\\
\bigl((D-k_j-1)^2-16\pi^2t^2-b^2\bigr)\phi_j
 &=8\pi it\,j(\ell-j+1)\phi_{j-1}.
\end{aligned}
\]
The first equation recursively determines every \(\phi_j\) from \(\phi_0\), since \(t>0\). At \(j=0\) the second becomes
\[
\bigl((D-\ell/2-1)^2-16\pi^2t^2-b^2\bigr)\phi_0=0.
\]
Write
\[
\phi_0(t)=t^{(\ell+1)/2}u(t).
\]
Direct differentiation cancels the first derivative and yields
\[
u''(t)=\left(16\pi^2+\frac{b^2-1/4}{t^2}\right)u(t).
\]

**Proof of uniqueness.** Polynomial growth of the model along \(d(t)\) implies polynomial growth of every \(\phi_j\) along \(a_t\): their ratio is the scalar
\(\omega(t^{1/2})\), another fixed complex power. Thus \(u\) has polynomial growth as \(t\to\infty\). Its displayed equation is exactly the nonzero-frequency cylinder equation used in Lesson 4, Section 4, with real Fourier frequency two, rotation weight zero, Laplace eigenvalue \(1/4-b^2\) and Casimir parameter \(4b^2-1\). Indeed \(e^{4\pi ix}u(y)\) has
\(-y^2(\partial_x^2+\partial_y^2)\)-eigenvalue \(1/4-b^2\). Those proved local lemmas apply to arbitrary complex parameters and do not require arithmetic invariance. They make both \(u\) and \(u'\) decay exponentially at infinity.

The Wronskian of two such solutions is constant because this equation has no first derivative. Exponential decay makes that constant zero. Ordinary differential-equation uniqueness then makes the two solutions proportional on all \(t>0\). The recursion makes all the \(\phi_j\) proportional with the same scalar. If \(\phi_0\) were identically zero, the recursion would make the entire compact type vanish on all \(a_t\), and hence everywhere: Iwasawa decomposition is \(G=ZNAK\), left \(N\)-covariance and scalar center determine those factors, and the right compact orbit is the chosen finite type. Thus a nonzero model has a nonzero \(\phi_0\).

Two proposed models of \(V\) may be compared using isomorphisms from \(V\) and any common compact type. The preceding argument makes their function maps proportional on that type. The type generates the simple module under the enveloping algebra and compact action, so the same proportionality holds on every vector. Multiplication by a nonzero scalar leaves the image function space unchanged. There is exactly one such moderate model. In particular it is the preceding explicit Gaussian model. \(\square\)


**Example 8.1 (a nonspherical complex principal series).** Take
\(\mu_1=(z/|z|)^2|z|_{\mathbb C}^{ir}\) and
\(\mu_2=(z/|z|)^{-1}|z|_{\mathbb C}^{-ir}\), \(r\in\mathbb R\).
Their ratio cannot have both holomorphic and antiholomorphic positive integer exponents as in (8.1), so the induction is irreducible. Its \(SU(2)\)-types have highest weights \(3,5,7,\ldots\), each once, by the compact-type lemma just proved; their dimensions are \(4,6,8,\ldots\). The central circle has angular exponent \(2+(-1)=1\). Formula (8.2) gives
\[
L(z_0,\pi)=\Gamma_{\mathbb C}(z_0+ir+1)
 \Gamma_{\mathbb C}(z_0-ir+1/2),\qquad \varepsilon=-i.
\]
Replacing the second absolute angular degree by \(-1\) would give an incorrect shift.

**Example 8.2 (why a subquotient needs its own data).** The ratio in
\(I_{\mathbb C}(|\cdot|_{\mathbb C}^{1/2},|\cdot|_{\mathbb C}^{-1/2})\)
is \(z\bar z\). Its finite quotient is the trivial representation, with
\(L(z_0)=\Gamma_{\mathbb C}(z_0+1/2)\Gamma_{\mathbb C}(z_0-1/2)\).
Its infinite submodule has data \((z/|z|),(z/|z|)^{-1}\), whose ratio is \(z/\bar z\). Its factor is instead \(\Gamma_{\mathbb C}(z_0+1/2)^2\). Its \(SU(2)\)-types are \(2,4,6,\ldots\), of dimensions \(3,5,7,\ldots\); these are precisely the tail left after removing the trivial compact type. Both have trivial central character, but different \(L\)-factors.

## 9. Explicit real examples

For \(D_2\), the weights are \(\pm2,\pm4,\ldots\), \(\Omega=0\), \(\Delta=0\), central sign is even, and
\[
W_0(d(y))=2\,1_{y>0}\,y e^{-2\pi y},\quad
L(z,D_2)=2(2\pi)^{-(z+1/2)}\Gamma(z+1/2),\quad \varepsilon=-1.
\]
The next vector is \(W_0(d(y))(2-4\pi y)\); its normalized Mellin integral is \(1-2z\), by (6.6).

For \(D_3\), the weights are \(\pm3,\pm5,\ldots\), \(\Omega=3\), \(\Delta=-3/4\), central sign is odd, and
\[
W_0(d(y))=2\,1_{y>0}\,y^{3/2}e^{-2\pi y},\quad
L(z,D_3)=2(2\pi)^{-(z+1)}\Gamma(z+1),\quad \varepsilon=-i.
\]
For \(D_{12}\), the corresponding data are weights \(\pm12,\pm14,\ldots\), \(\Omega=120\), \(\Delta=-30\), trivial real central sign,
\(L(z)=\Gamma_{\mathbb C}(z+11/2)\), and epsilon \(1\). Thus the holomorphic discriminant form has this infinity module in unitary normalization.

The limit \(D_1\) has weights \(\pm1,\pm3,\ldots\), \(\Omega=-1\), \(\Delta=1/4\), \(L(z)=\Gamma_{\mathbb C}(z)\), and epsilon \(i\). On restriction to the connected group its two ladders separate. For the full real group they form one irreducible representation.

## 10. Exercises with complete solutions

**Exercise 10.1 — the Casimir normalization.** Compute both \(\Omega\) and \(\Delta\) on \(D_k\), and compare with the trace-form Casimir in the \(\mathfrak{sl}_2\) prerequisite.

**Solution 10.1.** At the lowest vector \(v_k\), \(Fv_k=0\), so the second expression in (1.2) gives
\(\Omega v_k=(k^2-2k)v_k\). Commutation with \(E\), and reflection, give this scalar on both full ladders. Thus
\[
\Omega=k(k-2),\qquad \Delta=-k(k-2)/4=k(2-k)/4.
\]
The trace-form element in RT-LIE-05 is
\(C_B=EF+FE+H^2/2\). Since \(EF=FE+H\), one has \(\Omega=2C_B\); the Killing-form element there is \(C_\kappa=C_B/4=\Omega/8\). Hence its value on \(D_k\) is \(k(k-2)/8\). The three values for \(k=1\) are \(-1,1/4,-1/8\), checking both signs and the factor eight.

**Exercise 10.2 — every compact type.** Determine the \(SO(2)\)- and \(O(2)\)-types of every module in Theorem 3.2. Explain the two finite extensions and the limit exception.

**Solution 10.2.** Principal induction restricts to the functions \(e^{in\theta}\) with \(n\equiv\epsilon_1+\epsilon_2\pmod2\), each once. Formula (3.2) pairs \(n\) with \(-n\). For \(n>0\) this is the single two-dimensional type \(\rho_n\), since changing the scale of one line removes its reflection sign. When zero occurs, its reflection is \((-1)^{\epsilon_1}\), which cannot be removed by a basis change. This gives the first two rows of the table.

The positive discrete ladder has weights \(k+2j\), \(j\ge0\); reflection supplies their negatives. Each pair gives \(\rho_{k+2j}\), with no zero type. At \(k=1\), the connected restriction is the direct sum of the lowest and highest limit ladders, but reflection exchanges them; there is no proper full invariant summand.

A finite module has weights \(m,m-2,\ldots,-m\). Pairing them gives the last two rows. If \(m=0\), these are simply the trivial and determinant compact characters. If \(m>0\) is even, their weight-zero reflection signs already distinguish them. If \(m\) is odd, the compact types coincide, but the two full extensions remain distinct: an isomorphism commuting with the connected finite simple module would have to be scalar, and cannot change the sign of its reflection operator. Their difference concerns the compatible Lie action as well as the compact action.

**Exercise 10.3 — the discrete gamma factor.** Compute \(L(z,D_k)\) directly, including its constant, and explain why higher weights need no further denominator.

**Solution 10.3.** Use (6.2) with \(t=0\). The Mellin integrand is
\(2y^{k/2}e^{-2\pi y}y^{z-1/2}dy/y\) on positive \(y\). Put \(v=2\pi y\). Its integral is
\[
2(2\pi)^{-(z+(k-1)/2)}
\int_0^\infty v^{z+(k-1)/2-1}e^{-v}\,dv
=\Gamma_{\mathbb C}(z+(k-1)/2).
\]
The initial convergence condition is \(\operatorname{Re}(z+(k-1)/2)>0\); gamma continuation then gives the meromorphic value. Every raised vector multiplies the same exponential and power by the finite polynomial \(P_j(4\pi y)\). Integrating its \(r\)-th term replaces \(\Gamma(b)\) by \(\Gamma(b+r)=(b)_r\Gamma(b)\), and changes the scale by \(2^r\). Thus its quotient by the displayed factor is the polynomial \(Q_j(b)\). Reflection introduces a fixed scalar and gives no new poles. This verifies the factor for all compact-finite vectors, not just the bottom one.

**Exercise 10.4 — the connected classification.** Classify all irreducible \((\mathfrak{sl}_2,SO(2))\)-modules. Do not assume reflection. Explain why no multiplicity greater than one remains, even if admissibility was not imposed initially.

**Solution 10.4.** An irreducible module is generated by a nonzero weight vector \(v\): its Lie-generated subspace is circle-stable. Normal-order spanning makes its dimension countable. The commuting Casimir must be scalar even without a finite-weight-space assumption. Here is the countable-dimensional argument.

If \(\Omega-\alpha\) had nonzero kernel for some \(\alpha\), simplicity would make that kernel the entire module. Otherwise every \(\Omega-\alpha\) is an invertible module endomorphism: its image is a nonzero submodule and its kernel is zero. In the latter case the vectors
\((\Omega-\alpha)^{-1}v\), \(\alpha\in\mathbb C\), would be linearly independent. Indeed, a finite relation, multiplied by \(\prod(\Omega-\alpha)\), gives \(P(\Omega)v=0\) for a nonzero polynomial \(P\); its nonzero coefficients follow by evaluating the corresponding rational-function identity at each of its distinct poles. Over \(\mathbb C\), \(P\) factors into scalars and factors \(\Omega-\beta\), all assumed invertible, a contradiction. An uncountable independent family cannot lie in a countable-dimensional vector space. Hence \(\Omega=s^2-1\) is scalar.

Normal ordering and (1.3) then reduce every generated weight to a single raising or lowering vector. Thus each weight space has dimension at most one, so admissibility is automatic. Interior arrows must be nonzero, since a vanished arrow leaves a proper invariant tail; missing weights similarly separate the support. The possible supports are therefore:

* All \(n\equiv\epsilon\pmod2\), with \(s^2\ne(n+1)^2\) on every edge.
* \(k,k+2,\ldots\), \(k\ge1\), or its negative, with \(\Omega=k(k-2)\).
* \(-m,-m+2,\ldots,m\), \(m\ge0\), with \(\Omega=m(m+2)\).

At a lowest endpoint \(a\), \(EF=0\) forces \(s^2=(a-1)^2\). If \(a\le0\), the other zero forces the highest endpoint \(-a\); if \(a\ge1\), no interior zero remains and the infinite lowest ladder is possible. The highest-end calculation is the reflection of this argument, used only to describe another connected module. Formula (2.2) constructs the full and infinite lowest ladders and its reflected formula constructs the highest ones; RT-LIE-05 constructs the finite ones. The nonzero interior products prove irreducibility by weight projection and propagation. They also prove uniqueness by successive basis rescaling. In the full ladder \(s\) and \(-s\) give isomorphic connected modules by (3.5); the support and Casimir are otherwise complete invariants. The lowest and highest ladders are inequivalent here. They become one full-group module only when reflection is added.

## 11. Prerequisites and exact source boundaries

The real algebraic classification, its equivalence conditions, the Casimir scalar assertion, the invariant-form test, the real principal and discrete \(L\)-factor calculations, their epsilon phases, and the local holomorphic identification have been proved above. Every exercise has a full solution.

Section 4 proves admissibility and finite-vector irreducibility for every irreducible unitary representation of the full real GL₂, using the rotation-weight convolution algebra and the index-two restriction argument. It also integrates every positive form in the real list directly in a compact principal-series model or its invariant tail subspace. The general reductive-group admissibility and globalization results of Getz–Hahn, §4.4 (Theorems 4.4.2, 4.4.5–4.4.6 and the Casselman–Wallach remark after Proposition 4.4.3) are broader background, rather than proof substitutes for these real GL₂ assertions. The disk-model coefficient calculation in Section 4 also proves square integrability exactly for k≥2 and its failure at k=1; Getz–Hahn, §4.8 remains historical context for the terminology. We have not proved the general Langlands classification of §4.9.

Section 5 proves real moderate-growth Whittaker existence and uniqueness by the convergent Jacquet integral, an explicit lowest-vector Fourier transform and the single-mode decay estimates of Lesson 4. It also proves the full Gaussian-polynomial realization and its positive-character Fourier-and-swap Weyl action through a Schwartz section of principal induction and a checked partial Fourier transform. Jacquet–Langlands, Theorem 5.13 and Lemma 5.13.1 remains historical credit, rather than an unproved model input. Sections 5–6 then prove the real generic factors for all finite vectors. The matrix-factor proposition in Section 8 proves the nongeneric finite-dimensional factor (6.10), including normalized holomorphy for every coefficient, an attaining finite Gaussian family and the positive-character epsilon phase. The definitions on printed pages 96–97 retain their historical normalization credit.

Section 8 proves complex unitary Hilbert admissibility, compact multiplicity one, scalar infinitesimal character and finite-vector irreducibility. It proves every compact type of normalized complex induction and the full complex classification: the PBW invariant calculation gives the compact centralizer and full center; compact compression proves multiplicity one and central-character separation; faithful Verma modules and the tensor-Casimir identity supply compatible principal parameters; the finite-head/tail and compact-pairing argument proves reducibility and all constituents; these together prove exhaustion, exchange, the infinite companion and uniqueness of the unordered pair. Jacquet–Langlands, Theorem 6.2(i)–(vii) remains historical credit for the classification now proved here.

For every infinite simple complex module, Section 8 supplies an ordered irreducible full principal model with continuous Whittaker existence/uniqueness, the complete Gaussian family, exact positive-character Fourier Weyl action and all-vector complex Tate factors. The general moderate-model theorem then proves smoothness even for an initially continuous convolution model, derives the coupled radial Casimir equations with the exact Fourier constants, reduces the extremal coordinate to a nonzero-frequency equation of Lesson 4, and uses its proved decay estimates and the constant Wronskian to obtain uniqueness of every moderate realization. Jacquet–Langlands, Theorem 6.3 is historical credit for this assertion now proved here. The matrix-factor proposition proves the finite-dimensional nongeneric factors from their inducing pair: explicit Gaussian polynomials select the least compact type on both sides, their triangular marginals are the fundamental Tate tensors, and compact evaluation attains the whole product within the finite constituent. Lesson 9, Lemma 8.2, supplies the fully proved all-field matrix induction and Fourier comparison; the definitions preceding Theorem 6.4 retain their historical credit. Lemma 6.1(ii) remains historical credit for compact types now proved here.

The elementary normal ordering and finite \(\mathfrak{sl}_2\) results, compact decomposition, scalar Fourier and Mellin theory, and holomorphic lowering equation are the exact earlier-course imports identified at the start and in Section 7. The beta identity and duplication formula are used from NT-ADL-08 rather than reproved. The global tensor-product theorem remains the subject of the next lesson.

## References

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, 1970, §5, especially Lemma 5.6, Theorems 5.11, 5.13 and 5.15, Proposition 5.18 and Corollary 5.19; §6, Theorems 6.2–6.4; §13, Theorem 13.1 and the finite-dimensional Gaussian tests. These distinguish connected ladders, their reflection extensions and the irreducible pair used for complex factors.
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§4.4 and 4.7–4.9. Our difference parameter \(s\) corresponds to twice the parameter of their compact model minus one; (1.2) fixes the Laplacian normalization. Both reflection extensions are included explicitly here.
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §6.7, for the unitary representation attached to a classical holomorphic form. With the rotation orientation fixed in Lesson 2, our lowest weight is \(+k\).

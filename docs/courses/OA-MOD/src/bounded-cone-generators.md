# Bounded generators of cone symmetries

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 5 October 2026. Original exposition is CC0.*

Fix a sigma-finite von Neumann algebra in standard form \((M,H,J,P)\). We prove that a bounded complex-linear operator \(D\) on \(H\) satisfies

\[
\begin{gathered}
e^{tD}P=P\quad(t\in\mathbb R) \\
\Longleftrightarrow \\
D=x+JxJ \\
\text{for some }x\in M.
\end{gathered}
\]

This is the full generator assertion of Takesaki II, Exercise IX.1(9) in the approved edition. It follows from positive cone automorphisms, Jordan reconstruction and the innerness theorem for bounded derivations. The innerness provider is the programme spectral-tail proof, imported from OA-FLOW with its bounded input bridge and exact analytic foundations.

The earlier inputs are positive cone automorphisms, Jordan reconstruction, central splitting and implementation, standard implementation and uniqueness, the standard-form axioms, bounded calculus, spectral calculus and normality. No Hilbert-space separability is assumed.

## Norm limits keep both directions of the cone action

Write \(G(P)\) for the group of invertible operators \(A\in B(H)\) with \(AP=P\). If \(A\in G(P)\), then \(A^*\in G(P)\). Indeed, for \(\xi,\eta\in P\),

\[
 \langle A^*\xi,\eta\rangle=\langle\xi,A\eta\rangle\ge0.
\]

Self-duality gives \(A^*P\subset P\). Apply the same argument to \(A^{-1}\) to obtain the reverse inclusion. Each \(A\in G(P)\) commutes with \(J\): the two maps \(AJ\) and \(JA\) agree on the cone and consequently on its complex span, with their antilinearity taken into account. Thus a generator of such a real-parameter group satisfies \(JDJ=D\).

For bounded operators \(X,Y\), the norm Lie–Trotter formula is

\[
\begin{gathered}
e^{t(X+Y)}={} \\
\lim_{n\to\infty}(e^{tX/n}e^{tY/n})^n.
\end{gathered}
\tag{GN.1}
\]

Here is the needed proof, rather than an unbounded-generator import. On every bounded interval of real \(s\), the absolutely convergent exponential series gives

\[
 \|e^{sX}e^{sY}-e^{s(X+Y)}\|\le C s^2
\]

for a constant depending only on the interval and \(\|X\|+\|Y\|\): the constant and first-degree terms agree, and the sum of the remaining absolute terms is bounded by a constant times \(s^2\). For \(V=e^{tX/n}e^{tY/n}\), \(W=e^{t(X+Y)/n}\), the telescoping identity gives

\[
 V^n-W^n=\sum_{j=0}^{n-1}V^j(V-W)W^{n-1-j}.
\]

Every product of powers in this estimate is bounded by \(e^{|t|(\|X\|+\|Y\|)}\). Hence the difference is at most a fixed constant times \(t^2/n\), proving (GN.1).

If \(e^{tD}\in G(P)\) for every real \(t\), the adjoint result gives \(e^{tD^*}\in G(P)\). Apply (GN.1) to the appropriate halves of \(D,D^*\) and \(D,-D^*\). Closedness of \(P\) shows that both

\[
\begin{gathered}
S=(D+D^*)/2, \\
K=(D-D^*)/2
\end{gathered}
\]

generate groups mapping \(P\) into itself. The same limits at negative time give the inverse inclusions. Thus \(e^{tS},e^{tK}\in G(P)\) for every real \(t\). We have reduced the problem to a self-adjoint generator and a skew-adjoint generator, without assuming \(S\) and \(K\) commute.

## A single positive implementation determines its generator

Let \(S=S^*\) and \(e^{tS}P=P\). The operator \(e^S\) is positive and invertible, so PA-06 gives a unique positive invertible \(h\in M\) with

\[
 e^S=hJhJ.
\]

Put \(a=\log h\in M_{\mathrm{sa}}\), using bounded continuous functional calculus on the compact positive spectrum bounded away from zero. Real functional calculus and conjugation give \(J e^aJ=e^{JaJ}\). The two self-adjoint operators \(a,JaJ\) commute, so multiplication of their absolutely convergent exponential series gives

\[
 hJhJ=e^a e^{JaJ}=e^{a+JaJ}.
\]

The exponential is injective on bounded self-adjoint operators: applying continuous \(\log\) on the positive spectrum recovers its self-adjoint exponent. Therefore

\[
 S=a+JaJ.
 \tag{GN.2}
\]

This argument never assumes continuity of an as-yet-unidentified family of algebra implementers. It supplies that property afterwards: the unique positive element implementing \(e^{tS}\) is \(h_t=e^{ta}\), because the same commuting exponential identity proves

\[
 e^{tS}=e^{ta}Je^{ta}J.
\]

It follows that \(h_{s+t}=h_sh_t\), that \(t\mapsto h_t\) is norm differentiable, and that \(h'_0=a\). This justifies all of the positive-lift conclusions used in the source's part (b).

## A continuous Jordan flow fixes the center first

Now suppose \(K^*=-K\), and put \(U_t=e^{tK}\). This is a norm-continuous unitary group preserving \(P\). JR reconstruction gives a unique normal Jordan star automorphism \(\theta_t\) of \(M\), and its uniqueness gives

\[
 \theta_{s+t}=\theta_s\theta_t,
 \qquad U_t=U_{\theta_t}.
\]

JI's central splitting implies that every Jordan star automorphism sends the center onto itself: in each of its multiplicative and antimultiplicative central pieces, an element commuting with the whole algebra has an image commuting with that whole image piece; the two pieces sum to the target algebra.

For any \(x\in M\), let \(j(x)=(x+Jx^*J)/2\). JR-02 proves \(U_tj(x)U_t^*=j(\theta_t(x))\). If \(z\in Z(M)\), the central standard-form identity gives \(j(z)=z\); since \(\theta_t(z)\) is central too,

\[
 \theta_t(z)=U_tzU_t^*.
 \tag{GN.3}
\]

Choose \(\varepsilon>0\) such that \(2\|U_t-I\|<1\) whenever \(|t|<\varepsilon\). For every central projection \(p\), (GN.3) gives

\[
 \|\theta_t(p)-p\|\le2\|U_t-I\|<1.
\]

Two distinct commuting projections have difference of norm one: one of their two orthogonal difference corners is nonzero, and a unit vector there attains norm one. Thus \(\theta_t(p)=p\) for every central projection and every such \(t\). For arbitrary real \(s\), write \(\theta_s=(\theta_{s/n})^n\) with \(|s/n|<\varepsilon\). It follows that every \(\theta_s\) fixes every central projection. Norm spectral approximation and complex linearity then show that it fixes \(Z(M)\) pointwise.

For fixed \(s\), apply JI-04 to \(\gamma=\theta_{s/2}\). Because \(\gamma\) fixes the center, its multiplicative central piece and its antimultiplicative central piece are invariant under \(\gamma\); the source and target central projections coincide. On the first piece \(\gamma^2\) is multiplicative. On the second piece the two product reversals cancel, so \(\gamma^2\) is also multiplicative. Hence \(\theta_s=\gamma^2\) is a normal star automorphism on all of \(M\).

The center-fixing step is essential to this reasoning. A square of an arbitrary Jordan automorphism need not be an automorphism; GN-07 gives an explicit example. The one-parameter group and norm continuity provide precisely the additional fact required here.

## The skew generator is a bounded star derivation

For a normal star automorphism, SE-10 gives its canonical standard-form unitary implementing the left algebra. Its cone-vector functional identity agrees with the defining identity of \(U_{\theta_t}\). Uniqueness in SE-11/JI-06 therefore identifies these unitaries. Consequently

\[
 \theta_t(x)=U_txU_t^*\qquad(x\in M).
\]

The exponential series can be differentiated in operator norm, giving

\[
\begin{gathered}
d(x)=\left.\frac{d}{dt}\theta_t(x)\right|_{t=0} \\
=[K,x]\in M, \\
\|d\|\le2\|K\|.
\end{gathered}
\tag{GN.4}
\]

Membership follows because the difference quotients belong to the norm-closed algebra \(M\). Direct multiplication proves \(d(xy)=d(x)y+xd(y)\), and \(K^*=-K\) gives \(d(x^*)=d(x)^*\). Thus this is a bounded complex-linear star derivation on the arbitrary von Neumann algebra \(M\).

Apply the bounded innerness theorem, with the preceding input proofs. It supplies \(b=b^*\in M\) with

\[
 d(x)=i[b,x].
 \tag{GN.5}
\]

The implementation does not require a factor, trace, semifiniteness or a separable representation. The linked reading includes the supporting Fourier, filter and tail arguments and binds their exact integration, projection and calculus inputs.

## J-reality removes the commutant remainder

Equation (GN.5) implies \(K-ib\in M'\). This difference is skew-adjoint, so write \(K=ib+ic\) with \(c=c^*\in M'\). By GN-01, \(JKJ=K\). The antilinearity of \(J\) gives

\[
 b+c=-(JbJ+JcJ).
\]

Set \(z=b+JcJ\). This belongs to \(M\); the same displayed equality writes it as \(-(JbJ+c)\), which belongs to \(M'\). Thus \(z\in Z(M)_{\mathrm{sa}}\). Conjugating its first expression gives

\[
 JzJ=JbJ+c=-z.
\]

But the central standard-form identity also gives \(JzJ=z\). Hence \(z=0\), so \(c=-JbJ\). We have proved

\[
\begin{gathered}
K=ib-iJbJ \\
=ib+J(ib)J.
\end{gathered}
\tag{GN.6}
\]

This uses exactly one \(ib\) term in the conjugated expression for \(K\); any duplicated term in the printed intermediate line is unnecessary and inconsistent with that expression.

An equivalent check uses uniqueness of standard implementation: the group \(e^{itb}Je^{itb}J\) implements the same automorphisms as \(U_t\), and preserves the cone. The two groups therefore agree, and their norm derivatives give (GN.6).

## Assemble the general generator and prove the converse

Apply GN-02 to \(S\), and GN-03–05 to \(K\), from GN-01. There are \(a,b\in M_{\mathrm{sa}}\) with

\[
 D=S+K=(a+ib)+J(a+ib)J.
\]

This proves the forward assertion with \(x=a+ib\). Conversely, if \(D=x+JxJ\), the two summands commute. For real \(t\), absolute convergence and conjugate-linearity give

\[
 e^{tD}=e^{tx}J e^{tx}J.
 \tag{GN.7}
\]

SF-05 puts the image of \(P\) inside \(P\); applying the same identity to \(-t\) proves equality. No self-adjointness or normality of \(x\) is needed for this converse.

There is a precise uniqueness statement for the algebra representative. If \(x+JxJ=0\), then \(x=-JxJ\in M\cap M'\), and the central standard-form identity yields \(x=-x^*\). Conversely every central skew-adjoint element satisfies this identity. Therefore the representatives of a fixed generator form one coset of \(iZ(M)_{\mathrm{sa}}\), as a real vector space. This does not assert complex linearity of the map \(x\mapsto x+JxJ\).

## A Jordan square can reverse multiplication

On \(M=M_2(\mathbb C)\oplus M_2(\mathbb C)\), put

\[
 \gamma(x,y)=(y^{\mathsf T},x).
\]

Transpose is complex linear, star preserving and square preserving, so \(\gamma\) is a Jordan star automorphism. But

\[
 \gamma^2(x,y)=(x^{\mathsf T},y^{\mathsf T})
\]

is not multiplicative. With \(x=(E_{12},0)\), \(y=(E_{21},0)\), one has \(\gamma^2(xy)=(E_{11},0)\) whereas \(\gamma^2(x)\gamma^2(y)=(E_{22},0)\). This map exchanges the two central summands, precisely the behavior ruled out by GN-03 for the small elements of the continuous flow.

For a positive-generator check, in the Hilbert–Schmidt standard form and for \(a=a^*\), the operator \(S(X)=aX+Xa\) satisfies \(e^S(X)=e^aXe^a\). The unique positive multiplier is \(h=e^a\), whose logarithm recovers \(a\). For the skew case \(K(X)=i[b,X]\), one has \(K=ib+J(ib)J\), because \(JX=X^*\) changes \(ib\) to the right multiplication operator by \(-ib\). These calculations check the signs in both parts of the general theorem.

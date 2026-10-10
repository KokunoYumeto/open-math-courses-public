# Curve selection and Łojasiewicz inequalities

Suppose a calculation gives a small residual. Does that force a small error? If a function approaches a limiting value, how small can its gradient be? And when a set approaches a boundary point through a narrow curved region, can one follow that approach by an analytic path? These questions ask for different measurements of the same geometry. We will use function values as parameters for the gradient problem, error thresholds for the residual problem, and distance for the boundary problem.

*Original exposition, examples and solutions: CC0 1.0 Universal. The classical results and the human mathematical methods used are credited in the final section.*

Here **definable** means globally subanalytic. A map is definable if its graph is. A **definable arc** is a continuous definable map from a positive interval \((0,\epsilon)\); it can be constant or unbounded and need not have an endpoint in its target. All norms and manifold gradients below use the ambient Euclidean metric.

## A polynomial shows why the two exponents differ

On the square \([-1,1]^2\), set

\[
P(x,y)=x^2+y^4,\qquad e(x,y)=\sqrt{x^2+y^2}.
\]

The zero set of \(P\) is the origin, so \(e\) measures the error in solving \(P=0\). Direct computation gives

\[
e^4=(x^2+y^2)^2\le2(x^4+y^4)\le2P.
\tag{1}
\]

The exponent four is necessary: on the vertical axis, an estimate \(e^N\le CP\) would say \(|y|^N\le C|y|^4\). No \(N<4\) works as \(y\to0\).

For the gradient, the relevant comparison is different:

\[
\nabla P=(2x,4y^3),\qquad
P^{3/4}\le |x|^{3/2}+|y|^3
\le |x|+|y|^3\le\tfrac34|\nabla P|.
\tag{2}
\]

The first inequality uses \((u+v)^r\le u^r+v^r\) for \(u,v\ge0\) and \(0<r<1\). The last uses \(2|x|\le|\nabla P|\) and \(4|y|^3\le|\nabla P|\). Again the vertical axis determines the smallest possible exponent, now \(3/4\): an exponent \(\rho<3/4\) would require \(|y|^{4\rho}\le4C|y|^3\).

| Approach | Error \(e\) | Residual \(P\) | Gradient norm |
| --- | --- | --- | --- |
| \((t,0)\), \(t>0\) | \(t\) | \(t^2\) | \(2t\) |
| \((0,t)\), \(t>0\) | \(t\) | \(t^4\) | \(4t^3\) |

Thus raising an error to an integer power and raising a function value to an exponent below one are distinct operations. Our proofs must explain both, without assuming that a general function is polynomial or that its domain is closed.

## What a one-variable parameter can tell us

We use three proved inputs from *Analytic finiteness for preparation*: [finite analytic cells](analytic-finiteness-for-preparation.md#finite-analytic-cells-for-arbitrary-globally-subanalytic-sets), [Boolean operations, projection and closure](analytic-finiteness-for-preparation.md#full-global-preparation-and-the-complement-theorem), and [convergent one-variable Puiseux expansions](analytic-finiteness-for-preparation.md#one-variable). Their roles are limited and explicit.

Every definable subset of the line is a finite union of points and intervals. Consequently a property holding at positive parameters arbitrarily close to zero holds on a whole interval after shrinking, provided its parameter set is definable. Every scalar definable function on such an interval has an expansion

\[
u(t)=\sum_{j\ge j_0}a_jt^{j/q},\qquad
q\in\mathbb Z_{>0},\quad j_0\in\mathbb Z,
\tag{3}
\]

convergent for small positive \(t\). It is analytic away from zero on that interval. Boundedness excludes negative powers; convergence to zero excludes a nonzero constant term. A nonzero function therefore has a first term \(ct^\alpha\), with rational \(\alpha\). Differentiating (3) is legitimate after writing it as a convergent Laurent series in \(t^{1/q}\).

Here is the consequence that will control gradients.

**Bounded-curve speed lemma.** If \(z:(0,\epsilon)\to\mathbb R^n\) is bounded and definable, then it has a limit \(b\). After shrinking it is analytic, and either it is constant or there are rational \(\beta>0\) and \(K>0\) such that

\[
|z'(t)|\le Kt^{\beta-1}.
\tag{4}
\]

In particular it has finite length near zero.

**Proof.** Apply (3) to each coordinate. Its constant coefficient is the corresponding coordinate of \(b\). Among all nonconstant coordinates, let \(\beta\) be the smallest first positive exponent after subtracting that constant. Termwise differentiation gives the stated bound, after enlarging \(K\) to cover the finitely many coordinates. Finally
\(\int_0^\eta Kt^{\beta-1}\,dt=K\eta^\beta/\beta<\infty\). \(\square\)

We also need to select points subject to definable conditions. The precise fact is that every definable relation with nonempty fibres has a definable section. A full proof using compact subsets of locally closed fibres appears in the final proof section, [Choosing a point without assuming that an open fibre has a minimum](#definable-choice). Whenever we select a curve below, this fact gives a definable map; (3), coordinate by coordinate, supplies its eventual continuity and differentiability. No continuity of a section on its entire parameter space is assumed.

<a id="the-gradient-inequality"></a>

## Why must a gradient exponent be less than one?

The useful parameter here is the function value itself. A curve that visits value \(t\) at time \(t\) must satisfy the chain rule with derivative one. A very small gradient would force that curve to move too fast for (4).

**Level-set lemma.** Let \(U\subset\mathbb R^n\) be a bounded definable \(C^1\) submanifold, and let \(F:U\to\mathbb R\) be definable and \(C^1\). There exist \(\eta>0\), \(c>0\) and rational \(\rho\in(0,1)\) such that

\[
|\nabla_U F(x)|\ge c|F(x)|^\rho
\quad\text{if }x\in U\text{ and }0<|F(x)|<\eta.
\tag{5}
\]

Neither \(U\) nor its level sets need be closed. The function need not extend continuously to every boundary point of \(U\).

**Proof.** Put \(R=|F|(U)\cap(0,\infty)\). If zero is not an accumulation point of \(R\), choose \(\eta\) below all its positive values; (5) is then vacuous, and \(c=1\), \(\rho=1/2\) work. Otherwise \(R\) contains \((0,\eta_0)\). Define the least possible slope at level \(t\) by

\[
h(t)=\inf\{\,|\nabla_UF(x)|:x\in U,\ |F(x)|=t\,\},
\qquad 0<t<\eta_0.
\tag{6}
\]

Every fibre is nonempty, so \(h(t)\) is finite and nonnegative. Infima of definable real families are definable: being a lower bound and having a point below every larger number are quantified conditions, handled by Boolean operations and projection. The gradient is definable as well. Its differential and tangent space can be expressed by limits of difference quotients in definable charts; the induced gradient is their unique Euclidean Riesz representative. None of these statements uses a minimum in (6).

First, \(h(t)>0\) for all sufficiently small positive \(t\). Otherwise its definable zero set contains an interval next to zero. On that interval select \(z(t)\in U\) with

\[
|F(z(t))|=t,\qquad |\nabla_UF(z(t))|<t.
\tag{7}
\]

The map \(z\) is bounded because \(U\) is bounded, and it is nonconstant because its function values vary. The speed lemma gives (4). On the open set where \(F\ne0\), the function \(|F|\) is \(C^1\), with gradient norm \(|\nabla_UF|\). Also \(z'(t)\in T_{z(t)}U\). Therefore

\[
1=\left|\frac{d}{dt}|F(z(t))|\right|
\le |\nabla_UF(z(t))|\,|z'(t)|
\le Kt^\beta,
\]

which is impossible as \(t\downarrow0\).

We may now shrink so that \(h>0\). Its first Puiseux term is \(at^\alpha\), where \(a>0\) and \(\alpha\in\mathbb Q\). Choose, without requiring attainment of the infimum, a definable \(z(t)\in U\) satisfying

\[
|F(z(t))|=t,\qquad
|\nabla_UF(z(t))|<2h(t).
\tag{8}
\]

Again \(z\) is bounded and nonconstant. Combining its speed bound with the chain rule gives

\[
1\le 2h(t)|z'(t)|\le K_1t^{\alpha+\beta-1}.
\tag{9}
\]

Thus \(\alpha+\beta\le1\), and in particular \(\alpha<1\). If \(\alpha>0\), take \(\rho=\alpha\); if \(\alpha\le0\), take \(\rho=1/2\). For small \(0<t<1\), the lower Puiseux bound gives
\(h(t)\ge(a/2)t^\alpha\ge(a/2)t^\rho\).
Since every point on level \(t\) has gradient norm at least \(h(t)\), this proves (5). \(\square\)

Put \(U_\eta=\{x\in U:0<|F(x)|<\eta\}\). The maps used in this argument are then:

\[
\begin{array}{ccc}
(0,\eta)&\overset{z}{\longrightarrow}&U_\eta\\
\Vert&&\downarrow |F|\\
(0,\eta)&\overset{\mathrm{id}}{\longrightarrow}&(0,\eta).
\end{array}
\]

The derivative of the bottom map is one. The derivative of the top map is integrably bounded. The vertical derivative must supply the remaining size.

**Gradient inequality at a boundary value.** Let \(M\subset\mathbb R^n\) be a definable \(C^1\) submanifold, let \(f:M\to\mathbb R\) be definable and \(C^1\), and let \(a\in\overline M\). Suppose \(f\) has a continuous extension at \(a\), of value \(f(a)\). Then some neighborhood \(W\) of \(a\), some \(C>0\), and some rational \(\rho\in(0,1)\) satisfy

\[
|f(x)-f(a)|^\rho\le C|\nabla_Mf(x)|
\qquad(x\in M\cap W).
\tag{10}
\]

**Proof.** Take \(U=M\cap B(a,r)\) for any positive finite \(r\), and apply the level-set lemma to \(F=f-f(a)\) on this bounded open submanifold. Its tangent spaces and induced gradient agree with those of \(M\). Continuity at \(a\) supplies a smaller neighborhood \(W\subset B(a,r)\) where \(|F|<\eta\). Apply (5) where \(F\ne0\); where \(F=0\) the left side of (10) is zero. Set \(C=1/c\). Only continuity at the specified point was used. \(\square\)

For \(f(x)=x^m\) on \((0,1)\), with integer \(m\ge2\), the selected level curve is \(z(t)=t^{1/m}\). Its speed is \(t^{1/m-1}/m\), while the slope at level \(t\) is \(m t^{1-1/m}\). Equality holds in the chain-rule product. This explains directly the exponent \(1-1/m<1\).

<a id="an-inequality-detected-by-arcs"></a>

## How much residual is needed to sustain a fixed error?

Now let \(A\) be any definable set and \(f,g:A\to\mathbb R\) any definable functions. They need not be continuous. Assume \(f\) is bounded. Think of \(|f|\) as an error and \(|g|\) as a residual. The following quantity asks for the smallest residual compatible with an error of at least \(s\):

\[
m(s)=\inf\left(
\{\min(1,|g(x)|):x\in A,\ |f(x)|\ge s\}\cup\{1\}
\right),\qquad s>0.
\tag{11}
\]

The adjoined value one covers empty fibres. Thus \(m\) is always defined, takes values in \([0,1]\), is definable and is nondecreasing.

**Arc-detected inequality.** Suppose that for every definable arc \(\gamma:(0,\epsilon)\to A\),

\[
g(\gamma(t))\longrightarrow0
\quad\Longrightarrow\quad
f(\gamma(t))\longrightarrow0.
\tag{12}
\]

Then there are an integer \(N\ge1\) and \(C>0\) such that

\[
|f(x)|^N\le C|g(x)|\qquad(x\in A).
\tag{13}
\]

**Proof.** We first show that \(m(s)>0\) for every fixed \(s>0\). If \(m(s)=0\), then for every small \(r>0\) there is \(x\in A\) with \(|f(x)|\ge s\) and \(|g(x)|<r\). Definable selection gives such an \(x=x(r)\). Its coordinates have Puiseux expansions, possibly with negative powers, so after shrinking it is a continuous definable arc. Along it \(g\to0\) and \(|f|\ge s\), contrary to (12). This argument permits an arc escaping to infinity; boundedness of the selected points was not assumed. Constant arcs are included in (12), so in particular \(g=0\) forces \(f=0\).

Choose a positive bound \(M\ge1\) for \(|f|\). Because \(m\) is positive and bounded, its first Puiseux term at zero is \(as^\alpha\) with \(a>0\) and rational \(\alpha\ge0\). The exponent zero is allowed. Choose \(0<\eta<1\), \(c_0>0\) so that

\[
m(s)\ge c_0s^\alpha\quad(0<s<\eta),
\]

and choose an integer \(N\ge\max(1,\alpha)\). On this interval, \(s^N\le s^\alpha\). On \([\eta,M]\), monotonicity gives
\(m(s)\ge m(\eta)\ge m(\eta)s^N/M^N\).
Consequently

\[
m(s)\ge c s^N\quad(0<s\le M),\qquad
c=\min\{c_0,m(\eta)/M^N\}>0.
\tag{14}
\]

If \(|f(x)|>0\), substitute \(s=|f(x)|\) into (11)–(14):
\(c|f(x)|^N\le m(|f(x)|)\le |g(x)|\).
If \(f(x)=0\), (13) is automatic. This proves the global statement with \(C=1/c\), including the part where the error is bounded away from zero and the empty-set case. \(\square\)

There is a particularly simple case which should not be hidden inside an asymptotic expansion. Suppose \(f=0\) whenever \(|g|<\delta\), for some \(\delta>0\). For a positive bound \(M\) of \(|f|\), take

\[
N=1,\qquad C=\max\{1,M/\delta\}.
\tag{15}
\]

For \(|g|<\delta\) the left side is zero; for \(|g|\ge\delta\), one has \(|f|\le M\le(M/\delta)|g|\). This includes the zero fibres. In a proof using the supremum of \(|f|\) over small positive \(|g|\)-fibres, this is exactly the branch where that supremum is identically zero. It has its own constants and requires no leading nonzero term.

**Compact zero-set criterion.** If \(A\) is compact, \(f,g\) are continuous and definable on \(A\), and \(g^{-1}(0)\subset f^{-1}(0)\), then (13) holds.

**Proof.** The function \(f\) is bounded. For fixed \(s>0\), the set \(A_s=\{x\in A:|f(x)|\ge s\}\) is compact. If it is nonempty, \(|g|\) has a positive minimum on it: a zero of \(g\) there would contradict the zero-set inclusion. If it is empty, (11) gives \(m(s)=1\). Thus \(m(s)>0\) for every \(s>0\), and the argument (14) proves (13) directly. No limiting point of an arc has to be chosen for this compact argument. \(\square\)

Compactness cannot simply be omitted from that criterion. On \([1,\infty)\), take \(f=1\) and \(g(x)=1/x\). Neither function vanishes, so the zero-set inclusion holds, but (13) would require \(1\le C/x\) for all \(x\ge1\). The escaping arc \(\gamma(t)=1/t\) is the missing test in (12).

<a id="curve-selection"></a>

## Can an analytic path stay inside a narrowing region?

Consider

\[
A=\{(x,y):0<x<1,\ x^2<y<x^2+x^5\}.
\tag{16}
\]

Its closure contains the origin, but no straight ray through the origin stays in \(A\) near that point. Indeed \(y/x\) would have to be a constant strictly between \(x\) and \(x+x^4\). In contrast,

\[
\gamma(t)=(t^2,t^4+\tfrac12t^{10})
\tag{17}
\]

lies in \(A\) for both signs of every sufficiently small nonzero \(t\), and is analytic through zero. Curvature and a change of parameter are doing useful work.

**Analytic curve selection.** For a definable \(A\subset\mathbb R^n\) and \(a\in\overline A\), there is an analytic map \(\gamma:(-\epsilon,\epsilon)\to\mathbb R^n\) with \(\gamma(0)=a\) and \(\gamma(t)\in A\) for \(0<t<\epsilon\). One may also require membership for both signs of nonzero \(t\). If \(a\in\overline{A\setminus\{a\}}\), the map can be chosen nonconstant and avoiding \(a\) away from zero.

**Proof.** If \(a\) is not an accumulation point of \(A\setminus\{a\}\), then \(a\in A\) and the constant map suffices. Otherwise the definable set of positive distances
\(\{|x-a|:x\in A\setminus\{a\}\}\)
accumulates at zero and therefore contains \((0,\delta)\). Select a definable \(z(r)\in A\) on each of these distance levels:

\[
|z(r)-a|=r,\qquad 0<r<\delta.
\tag{18}
\]

The coordinates of \(z-a\) are bounded, tend to zero and have convergent Puiseux expansions. Choose a common denominator \(q\). In each coordinate, substitute \(r=t^{2q}\) into its expansion. The resulting exponents are even nonnegative integers, with positive exponents for every nonzero term. Their power series converge on a two-sided interval and define an analytic \(\gamma\) with value \(a\) at zero. For either sign of \(t\ne0\), the series equals the actual \(z(t^{2q})\), since \((t^{2q})^{j/q}=t^{2j}\). Hence (18) gives \(\gamma(t)\in A\) and \(|\gamma(t)-a|=t^{2q}>0\). \(\square\)

The factor two is not a cosmetic addition: \(\sqrt{t^2}=|t|\), while \(\sqrt{t^4}=t^2\). For a local subanalytic set in an analytic manifold, first use a bounded coordinate neighborhood on which that set is globally subanalytic; the chart inverse carries this construction back to the manifold. Equivalently, if a one-sided analytic germ has already been obtained, \(t\mapsto\gamma(c t^2)\), with \(c>0\) sufficiently small, gives membership on both sides. This retains the full two-sided use of curve selection without asserting global definability of the manifold.

## What extra information does distance from the endpoint give?

The gradient inequality (10) was proved using function-value levels. A separate estimate records geometric distance. Under the same hypotheses on \(M,f,a\), there are \(C_0>0\) and a neighborhood of \(a\) such that

\[
|f(x)-f(a)|\le C_0|x-a|\,|\nabla_Mf(x)|.
\tag{19}
\]

Here is a proof which makes the uniform constant explicit as an existence assertion over the whole neighborhood, rather than merely proving one inequality on each individually chosen arc.

Translate \(a\) to zero and subtract \(f(a)\). If (19) failed for every neighborhood and constant, then for each small \(s>0\) we could select \(x(s)\in M\) with

\[
0<|x(s)|<s,\qquad f(x(s))\ne0,\qquad
|x(s)|\,|\nabla_Mf(x(s))|<s|f(x(s))|.
\tag{20}
\]

This is a definable relation, so choose \(x\) definably and shrink until it is analytic. Set \(r(s)=|x(s)|\). It tends to zero and has a positive leading Puiseux term; its derivative is positive for small \(s\). Thus it has a definable inverse \(s=s(r)\) on a positive interval. Reparameterize as \(z(r)=x(s(r))\), so that \(|z(r)|=r\).

Every coordinate of \(z\) is bounded by \(r\). In its Puiseux series every nonzero first exponent is consequently at least one. Differentiating shows \(|z'(r)|\le K\). The function \(u(r)=f(z(r))\) is nonzero and tends to zero by continuity at the origin. Write its first term as \(dr^\lambda\), with \(d\ne0\) and rational \(\lambda>0\). Then

\[
\frac{r|u'(r)|}{|u(r)|}\longrightarrow\lambda.
\]

For small \(r\), the chain rule now gives

\[
\tfrac\lambda2|u(r)|
\le r|u'(r)|
\le Kr|\nabla_Mf(z(r))|
<K s(r)|u(r)|,
\]

where the last inequality is (20). Dividing by the nonzero \(|u(r)|\) contradicts \(s(r)\to0\). This proves (19), including points at which the gradient vanishes. In particular any such nearby point has \(f(x)=f(a)\). This radial argument is not an input to the proof of (10).

<a id="definable-choice"></a>

## Choosing a point without assuming that an open fibre has a minimum

For completeness we prove the selection fact used above in all fibre dimensions at once.

**Definable choice.** If \(E\subset\mathbb R^m\times\mathbb R^n\) is definable and \(B\) is its projection to \(\mathbb R^m\), there is a definable \(s:B\to\mathbb R^n\) with \((b,s(b))\in E\) for every \(b\in B\).

**Proof.** The empty-base case uses the empty map; for \(n=0\) there is nothing to choose. Suppose \(n\ge1\). First make all fibres bounded by the semialgebraic homeomorphism

\[
T:\mathbb R^n\longrightarrow B(0,1),\qquad
T(y)=\frac{y}{\sqrt{1+|y|^2}},\qquad
T^{-1}(v)=\frac{v}{\sqrt{1-|v|^2}}.
\tag{21}
\]

This is only a change of coordinates in the fibre; it is not a definition of global subanalyticity. Apply the finite cell theorem to the image \(E'\) under \((b,y)\mapsto(b,T(y))\), and list its cells as \(C_1,\ldots,C_k\). Each cell is locally closed. Indeed a continuous graph is closed relative to its base times \(\mathbb R\), and a band is open relative to that product; induction from intervals and points proves the claim. A slice at a fixed base point is therefore locally closed as well.

For each \(b\in B\), choose the least index \(i\) for which the fibre \(C=(C_i)_b\) is nonempty. This partitions \(B\) into finitely many definable pieces. Fix such a piece for the construction. The set \(C\) is bounded and locally closed. Put

\[
K_b=\overline C,\qquad D_b=K_b\setminus C.
\]

The closure is taken in the fibre \(\mathbb R^n\), not in the total parameter space. Its graph is definable by the quantified condition “every positive-radius ball in this fibre meets \(C\).” The set \(K_b\) is nonempty and compact. Because \(C\) is open in its own closure, \(D_b\) is compact too. Define on \(K_b\)

\[
\delta_b(v)=
\begin{cases}
\operatorname{dist}(v,D_b),&D_b\ne\varnothing,\\
1,&D_b=\varnothing.
\end{cases}
\tag{22}
\]

For fixed \(b\), this is continuous. It is positive at every point of \(C\) and zero on \(D_b\) when that set is present. Consequently its maximum on \(K_b\) is positive, and the set \(Q_b\) of maximizing points is a nonempty compact subset of \(C\). Distance, the maximum, and \(Q_b\) are definable by quantified conditions on the bounded fibres. Their definability requires no prior selection theorem and no continuity in \(b\).

Choose the lexicographically least point of \(Q_b\). Such a point exists: minimize its first coordinate on the compact set, then its second coordinate on the resulting compact subset, and so on through the finite list of coordinates. It is unique. The condition that a point lies in \(Q_b\) and no point of \(Q_b\) is lexicographically smaller defines its graph. Thus it is a definable function of \(b\). Finally apply \(T^{-1}\) and combine the finitely many base pieces.

The construction has the following chain of sets in each fibre:

\[
C\subset K_b,\qquad
\varnothing\ne Q_b=\operatorname*{argmax}_{K_b}\delta_b\subset C,
\qquad
\{v_b\}=\operatorname{lexmin}Q_b.
\]

Compactness is used only after the missing boundary has been excluded by maximizing its distance. Thus an open or unbounded original fibre presents no problem. \(\square\)

## Exercises with complete solutions

### Which exponent is forced by a narrow direction?

Let \(m\ge2\) be an integer and put \(P_m(x,y)=x^2+y^{2m}\) on \([-1,1]^2\). Determine the smallest integer \(N\) for which \((x^2+y^2)^{N/2}\le CP_m\) can hold, and the smallest positive \(\rho\) for which \(P_m^\rho\le C|\nabla P_m|\) can hold near zero.

**Solution.** The vertical axis forces \(N\ge2m\) and \(\rho\ge1-1/(2m)\). These bounds are attained. Since \((a+b)^m\le2^{m-1}(a^m+b^m)\) for \(a,b\ge0\),
\((x^2+y^2)^m\le2^{m-1}(x^{2m}+y^{2m})\le2^{m-1}P_m\).
For \(\rho=1-1/(2m)\), subadditivity of the \(\rho\)-power gives
\(P_m^\rho\le |x|^{2-1/m}+|y|^{2m-1}\le |x|+|y|^{2m-1}\).
Both terms are bounded by fixed multiples of
\(|\nabla P_m|=\sqrt{4x^2+4m^2y^{4m-2}}\).
Thus the stated lower bounds are the exact exponents.

### Why must the arc test include escape to infinity?

On \(A=[1,\infty)\), take \(f=1\) and \(g(x)=1/x\). Check the implication (12) for bounded definable arcs, then decide whether it implies (13).

**Solution.** On a bounded arc, its values lie in \([1,R]\) for some \(R\), so \(g\ge1/R\); the antecedent of (12) cannot occur. Nevertheless (13) would require \(1\le C/x\) on all of \(A\), which fails. The definable arc \(x(t)=1/t\), for \(0<t<1\), detects the failure. Restricting the theorem to bounded arcs would change its content.

### Why is boundedness of the error necessary?

On \(A=(0,\infty)\), take \(f(x)=x\) and \(g(x)=x/(1+x)\). Prove (12), and show that no global conclusion (13) is possible.

**Solution.** If \(g(x(t))\to0\), then
\(x(t)=g(x(t))/(1-g(x(t)))\to0\), so (12) holds for every arc. But \(g<1\), whereas \(f(x)^N=x^N\) is unbounded for every \(N\ge1\). Hence no fixed \(C\) works. The compact tail in (14) is an error bound \(|f|\le M\), not an unspoken bound on the domain.

### A slope infimum which is never a minimum

Let \(U=(0,1)^2\) and \(F(x,y)=x(1+y)\). Compute (6) for \(0<t<1\). Explain how (8) still has a valid selection.

**Solution.** On level \(t\), put \(v=1+y\in(1,2)\); then \(x=t/v\in(0,1)\) and
\(|\nabla F|^2=v^2+t^2/v^2\).
Its derivative in \(v\) is \(2v-2t^2/v^3>0\), so
\(h(t)=\sqrt{1+t^2}\), approached as \(y\downarrow0\) but never attained in \(U\). The definable curve
\(z(t)=(t/(1+t),t)\)
lies in the required level for \(0<t<1\). Its slope tends to one, as does \(h(t)\), so its slope is less than \(2h(t)\) after shrinking. Approximate minimization is sufficient. Here \(\alpha=0\), and any fixed rational \(\rho\in(0,1)\) gives a weaker valid local lower bound after adjusting constants.

### Build a two-sided curve in a thin band

For \(A=\{(x,y):0<x<1,\ x^3<y<x^3+x^7\}\), give an analytic curve through zero which lies in \(A\) for both signs of a nonzero parameter. Show that no straight ray has the same property even on the positive side.

**Solution.** Take
\(\gamma(t)=(t^2,t^6+\tfrac12t^{14})\).
For \(0<|t|<1\), its first coordinate is in \((0,1)\), and its second is strictly between \(x^3=t^6\) and \(x^3+x^7=t^6+t^{14}\). A ray with positive \(x\)-component has constant ratio \(y/x\), whereas membership requires
\(x^2<y/x<x^2+x^6\).
That constant would have to be zero in the limit, which violates the strict lower inequality. A ray with nonpositive \(x\)-component cannot enter the band.

### The gradient exponent and the selected speed

On \(M=(0,1)\), let \(f(x)=x^{3/2}\), extended continuously by zero at the endpoint. Compute the slope as a function of the value \(t=f(x)\), the selected curve's speed, and the least possible gradient exponent. Check the radial estimate as well.

**Solution.** The level curve is \(x(t)=t^{2/3}\), with derivative \((2/3)t^{-1/3}\). Its gradient norm is \((3/2)t^{1/3}\). Their product is one, so (9) is sharp with \(\alpha=1/3\) and \(\beta=2/3\). The estimate \(f^\rho\le C|f'|\) becomes
\(x^{3\rho/2}\le(3C/2)x^{1/2}\), and holds near zero precisely when \(\rho\ge1/3\). Finally
\(f(x)=\tfrac23 x|f'(x)|\), so the distance-sensitive estimate holds with equality for \(C_0=2/3\).

## Mathematical sources and proof-method credits

Guillaume Valette, [*On subanalytic geometry*](https://arxiv.org/abs/2507.23622v1), arXiv:2507.23622v1, 31 July 2025, §2.2, pp. 47–50, is the human treatment used for the classical results: definable choice (Proposition 2.2.1), analytic curve selection (Lemma 2.2.3), the arc and compact inequalities (Theorem 2.2.5 and Corollary 2.2.6), the radial estimate (Lemma 2.2.8), and the gradient inequality (Corollary 2.2.9). The paper is cited here, not copied.

The reduction from a definable family to a selected one-variable witness, the use of convergent Puiseux orders, and the chain-rule comparison for the radial estimate are mathematical methods used from that treatment. Here the gradient theorem is proved instead by approximate minimum slopes on value levels and the speed of bounded selected curves; it does not use the arc inequality or a distance-defined auxiliary manifold. The residual theorem uses the minimum residual compatible with an error threshold, and compactness is applied directly to those threshold sets. The selection proof uses compact maximizing sets inside locally closed fibres. The polynomial tests, diagrams of maps and six solved exercises develop these arguments; no claim that the classical theorems or general methods are new is intended.

The current programme providers linked above supply finite analytic cells, the set operations and convergent Puiseux expansions. Their own human-source notices remain in force. The arguments here require no finite triangulation theorem for a noncompact analytic manifold.

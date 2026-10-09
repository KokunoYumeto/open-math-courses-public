# Finite covers and normal circles in projective complements

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(F\) be a nonzero homogeneous complex polynomial of degree \(m\geq1\) in \(d+1\) variables, with \(d\geq1\). Put
\[
 U=\mathbb P^d\setminus\{F=0\}.
 \tag{1}
\]
We prove the ordinary rational homology bound \(H_j(U;\mathbb Q)=0\) for \(j>d\), then apply it to the positive-normal-circle tube of a hyperplane section. Singularities and repeated factors of the removed divisor are permitted.

The construction is elementary at the level of finite chains. The affine level \(F=1\) is a smooth closed hypersurface and a finite cyclic cover of \(U\). A proper squared distance on that level has finitely many Morse critical points; a transfer that sums all lifts of a simplex descends the homology bound. The subsequent tube argument uses the exact already written homological Thom and tubular-neighborhood construction.

Basic references are Allen Hatcher's *Algebraic Topology* [H] for finite-cover transfer, Arthur Sard's critical-value theorem [S], and Atiyah, Bott and Gårding's projective-cycle arguments [A]. The needed transfer is proved here. The exact internal inputs are [Rational top forms detect cycles in a hypersurface complement, Lemmas 6.1–6.2](../../AN02-L182.html#6-why-the-graph-has-finite-dimensional-ordinary-homology), for equal-dimensional critical values and finite discrete semialgebraic sets; [Ordinary finite-chain Morse handles](../../AN02-L125.html#mh0-statement-coefficients-and-boundary-cases), for the actual relative sublevel groups and the passage to finite-chain homology; and [Projective exhaustion and the finite-chain tube receiver](../../AN02-L124.html#tp6-the-included-normal-bundle-argument-and-the-tube-deduction), for the explicitly oriented homological Thom/excision map. Their stated lower smooth and finite-chain foundations are retained. This argument does not require a general Stein homology theorem or a globally constructed Morse perturbation.

## 1. A smooth affine level with a cyclic covering map

Define
\[
 X=\{Z\in\mathbb C^{d+1}:F(Z)=1\},\qquad
 p:X\longrightarrow U,\quad Z\longmapsto[Z].
 \tag{2}
\]

**Proposition 1.1.** The set \(X\) is a closed smooth complex manifold of dimension \(d\). The map \(p\) is an \(m\)-sheeted covering by holomorphic local diffeomorphisms. Multiplication by the \(m\)-th roots of unity supplies a free transitive cyclic deck action on every fiber. The covering need not be connected.

**Proof.** Euler's polynomial identity is
\[
 \sum_{j=0}^{d} Z_j\frac{\partial F}{\partial Z_j}(Z)=mF(Z).
 \tag{3}
\]
It follows by checking each degree-\(m\) monomial and summing. On \(X\), the right side is \(m\ne0\), so the complex differential of \(F\) is nonzero. A coordinate partial derivative is therefore nonzero. The inverse function theorem in that coordinate gives a smooth complex hypersurface, of dimension \(d\). Closedness follows from continuity of \(F\), and \(0\notin X\).

Given \([Z]\in U\), all representatives on its line have the form \(\lambda Z\), \(\lambda\ne0\). They belong to \(X\) exactly when
\[
 \lambda^mF(Z)=1.
 \tag{4}
\]
This equation has exactly \(m\) distinct nonzero complex roots, since \(F(Z)\ne0\) and its derivative at a root is \(m\lambda^{m-1}F(Z)\ne0\). Thus each fiber has \(m\) points.

For the local covering description choose a projective chart section \(s(y)\) near a point of \(U\). Shrink its domain \(B\) so that \(F(s(y))\) takes its values in a disk not containing zero. On this disk a holomorphic logarithm \(\ell\) exists. Explicitly, centered at a nonzero value \(b\), take a smaller disk with \(|(z-b)/b|<1\), choose one logarithm of \(b\), and use the convergent power series for \(\log(1+(z-b)/b)\). It exponentiates to \(z\). Put
\[
 t(y)=\exp\bigl(-\ell(F(s(y)))/m\bigr)s(y).
 \tag{5}
\]
Then \(F(t(y))=1\). If \(\zeta=e^{2\pi i/m}\), all the local inverse sections of \(p\) are
\[
 t_j(y)=\zeta^j t(y),\qquad 0\leq j<m.
 \tag{6}
\]
They are distinct and holomorphic. Every point of \(p^{-1}(B)\) is in exactly one of their images. In the chart representation \(Z=\lambda s(y)\), the factor \(\lambda\) is a continuous holomorphic coordinate, so these finite disjoint sections are open branches of \(p^{-1}(B)\). This proves the evenly covered local description and the local diffeomorphism claim.

Multiplication by \(\zeta^j\) preserves \(X\) and is a deck transformation. Its action on every fiber is free and transitive, directly by (4). We use this specified cyclic action; it need not exhaust all deck transformations when the covering is disconnected. For example \(F(Z)=Z_0^m\) gives \(m\) separate affine \(d\)-planes in \(X\), mapping onto the single affine chart \(U\). \(\square\)

## 2. A finite-critical-point squared distance on the affine level

**Proposition 2.1.** Some \(a\in\mathbb C^{d+1}\) makes
\[
 \rho_a(Z)=|Z-a|^2\quad(Z\in X)
 \tag{7}
\]
a bounded-below proper strictly plurisubharmonic Morse function with finitely many critical points.

**Proof.** Write the ambient affine space as \(\mathbb R^N\), \(N=2d+2\). Put
\[
 g_1=\operatorname{Re}F-1,\qquad
 g_2=\operatorname{Im}F,\qquad n_j=\nabla g_j .
 \tag{8}
\]
These are real polynomial data. Their two gradients are independent on \(X\): the nonzero complex differential of \(F\), established in (3), is real-surjective onto \(\mathbb C\cong\mathbb R^2\). The gradients span the real normal space to \(X\).

Consider the smooth map
\[
 \Phi:X\times\mathbb R^2\longrightarrow\mathbb R^N,\qquad
 \Phi(Z,\lambda)=Z-\lambda_1n_1(Z)-\lambda_2n_2(Z).
 \tag{9}
\]
Its domain has real dimension \(2d+2=N\), the same as its target. The manifold \(X\) is a second-countable subspace of Euclidean space. Its implicit-function charts therefore have a countable subcover, and their products with countably many open boxes cover \(X\times\mathbb R^2\) by countably many coordinate domains. To justify the subcover, each chart contains a member of a countable topological basis around any point; for every basis member contained in a chart choose one such chart. Those choices cover the manifold.

In each coordinate domain, the equal-dimensional critical-value lemma cited above applies to \(\Phi\). The set of its critical values is a countable union of measure-zero sets and hence has measure zero. Choose \(a\) outside that union. Then \(a\) is a regular value of (9), in every chart and thus intrinsically.

A critical point of (7) satisfies precisely
\[
 Z-a=\lambda_1n_1(Z)+\lambda_2n_2(Z)
 \tag{10}
\]
for a unique pair \(\lambda\). At a solution put
\[
 A=I-\lambda_1\operatorname{Hess}g_1
        -\lambda_2\operatorname{Hess}g_2 .
 \tag{11}
\]
The restricted real Hessian of \(\rho_a\) is \(B(v,t)=2\,v\cdot At\) for \(v,t\in T_ZX\). Indeed, for a curve \(Z(s)\) in \(X\) with \(Z'(0)=v\), differentiating \(g_j(Z(s))=0\) twice gives \(n_j\cdot Z''(0)=-v\cdot(\operatorname{Hess}g_j)v\). Inserting (10) into the second derivative of \(|Z(s)-a|^2\) gives the asserted diagonal Hessian; polarization gives the bilinear expression.

The differential of (9) is
\[
 D\Phi(v,\mu)=Av-\mu_1n_1-\mu_2n_2 .
 \tag{12}
\]
Its tangent projection is \(P_TAv\), half the Hessian operator. If this tangent operator is invertible, its output determines \(v\), and the normal output then uniquely determines \(\mu\). Conversely a nonzero tangent kernel vector has \(Av\) normal, so a unique \(\mu\) gives a nonzero kernel vector in (12). Thus (12) is invertible exactly when the restricted Hessian is nonsingular. Regularity of \(a\) makes all the critical points Morse.

The actual solution set for their critical pairs is
\[
 S_a=\{(Z,\lambda)\in\mathbb R^{N+2}:
       g_1(Z)=g_2(Z)=0,\ 
       Z-a=\lambda_1n_1(Z)+\lambda_2n_2(Z)\}.
 \tag{13}
\]
It is semialgebraic, by its polynomial equations. The inverse function theorem makes each preimage of \(a\) in (9) isolated. The embedded coordinates of \(X\times\mathbb R^2\) have the Euclidean subspace topology, so \(S_a\) is discrete as a subset of \(\mathbb R^{N+2}\). The finite-discrete-semialgebraic lemma cited above makes it finite. Hence (7) has finitely many critical points, without a compactness assumption on the critical set.

Since \(X\) is closed, its intersection with a closed ambient ball is compact. This proves properness of (7); it is nonnegative. In any holomorphic local parametrization \(Z=Z(y)\), its Levi form is
\[
 \mathcal L_{\rho_a}(v)
       =\sum_{j=0}^{d}|dZ_j(v)|^2>0\quad(v\ne0),
 \tag{14}
\]
because the parametrization is an immersion. The center \(a\) contributes constants and has no effect on this Levi form. Thus the function is strictly plurisubharmonic. No smoothness or square-free assumption on the removed projective divisor was used. \(\square\)

**Corollary 2.2.** For any coefficient ring \(R\), ordinary finite-chain \(H_j(X;R)\) vanishes for \(j>d\). For a field \(R\), all these groups are finite dimensional.

**Proof.** At a critical point of a smooth strictly plurisubharmonic function the real Hessian obeys
\[
 B(v,v)+B(Jv,Jv)=4\mathcal L_{\rho_a}(v)>0\quad(v\ne0).
 \tag{15}
\]
Expansion of the Wirtinger derivatives gives this identity, with the factor four, as proved in the cited finite-chain handle lesson. If a negative subspace \(W\) had dimension \(r>d\), then \(\dim(W\cap JW)\geq2r-2d>0\). For \(0\ne v=Jw\in W\cap JW\), also \(Jv=-w\in W\); both real Hessian terms would be negative, contradicting (15). Every Morse index is therefore at most \(d\).

The exact handle theorem gives an increasing open sublevel cover, starting empty, whose relative group at each critical step is a finite sum of copies of \(R\) in the crossed indices. There are finitely many such points and values by Proposition 2.1. The pair exact sequences show inductively that every sublevel group above degree \(d\) is zero. Over a field, the exact segment
\[
 H_j(W_{i-1};R)\longrightarrow H_j(W_i;R)
                         \longrightarrow H_j(W_i,W_{i-1};R)
 \tag{16}
\]
also proves finite dimensionality: the first term bounds the kernel dimension, and the finite relative term bounds the image dimension.

Choose a regular sublevel above all critical values. Later relative groups are zero, so the pair sequences make all later absolute maps isomorphisms. The finite-chain direct-limit statement in the cited theorem applies: a finite cycle or bounding chain has compact image and lies in one of the increasing open stages. Thus the groups of the whole \(X\) are those of that single finite stage. This proves vanishing over all \(R\) and finite dimensionality over fields. It does not assert a cellular chain complex or forget possible attaching-map cancellations. \(\square\)

## 3. Lifting simplices without a hidden covering-space premise

We need the covering transfer for arbitrary continuous singular simplices. Its construction requires the following elementary lifting fact.

**Lemma 3.1.** If \(q:E\to B\) is a finite covering, \(\sigma:\Delta^j\to B\) is continuous, and \(v_0\) is a vertex of the simplex, then every \(e_0\in q^{-1}(\sigma(v_0))\) determines a unique continuous lift \(\widetilde\sigma:\Delta^j\to E\) with \(\widetilde\sigma(v_0)=e_0\). Evaluation at any point of the simplex bijects the set of all lifts with the fiber over that point. If \(E,B\) are smooth and the covering branches are local diffeomorphisms, a smooth simplex has smooth lifts.

**Proof.** First a continuous path \(\gamma:[0,1]\to B\) has a unique lift from a specified initial fiber point. Pull back the evenly covered neighborhoods to an open cover of its compact parameter interval and choose a finite subdivision so the image of each closed segment lies in one such neighborhood. On the first segment choose the inverse branch containing the specified starting point. At the next endpoint choose the unique branch containing that endpoint, and continue. The branches agree at each endpoint and give a continuous lift. Another lift must agree on the first segment by its branch and starting value, and then successively on every segment. Equivalently the agreement set is open and closed along the parameter interval. Thus the path lift is unique.

For each \(y\in\Delta^j\), lift the radial path
\[
 \gamma_y(t)=\sigma((1-t)v_0+ty)
 \tag{17}
\]
from \(e_0\), and define \(\widetilde\sigma(y)\) to be its endpoint. This definition always projects to \(\sigma(y)\); for \(y=v_0\) it gives \(e_0\).

We prove its continuity instead of assuming it. Fix \(y_*\). Compactness and continuity give a finite partition \(0=t_0<\cdots<t_s=1\) such that, on each closed segment, \(\gamma_{y_*}\) lies in an evenly covered neighborhood \(B_\ell\). By first choosing overlapping open parameter segments and a finer subdivision, the closed images can be kept inside those neighborhoods. Uniform continuity of \((t,y)\mapsto\sigma((1-t)v_0+ty)\) near this compact path then makes the same segments lie in \(B_\ell\) for all \(y\) in some relative neighborhood of \(y_*\). On the first segment the fixed initial point selects a branch for all these paths. Its endpoint depends continuously on \(y\). At the next segment, that endpoint stays in the same open branch of \(q^{-1}(B_2)\) after possibly shrinking the neighborhood of \(y_*\). Its branch inverse is continuous, so the next endpoint is continuous. Repeat the finite construction through all the segments. The final endpoint \(\widetilde\sigma(y)\) is continuous near \(y_*\). This holds at every point, including the boundary in its relative topology.

Any continuous lift of \(\sigma\) restricts on every radial path to the unique path lift from \(e_0\), so it equals the constructed map. More generally, two lifts agreeing at one point agree near it by the local branch inverse. Their agreement and disagreement sets are both open: near two unequal fiber points use their distinct covering branches. Connectedness of \(\Delta^j\) makes agreement at one point imply equality everywhere.

Distinct choices of \(e_0\) therefore give distinct values at every point. Conversely, starting the same radial construction at any selected point of \(\Delta^j\) gives a lift from any element of its fiber, since the simplex is convex. This proves the evaluation bijection. In particular an \(m\)-sheeted covering gives exactly \(m\) lifts of every simplex.

For a smooth simplex, at any point of its domain the continuous lift lies in one branch over an evenly covered neighborhood. On a relative neighborhood it is the composition of \(\sigma\) with that smooth local inverse. The smooth extension of \(\sigma\) near the compact simplex gives a local smooth extension of this composition even at its boundary; smoothness is local, so the lift is a smooth simplex. No differentiability of the radial path construction at the vertex is required. \(\square\)

## 4. The chain transfer and its coefficient condition

For any coefficient ring \(R\), singular chains are the free \(R\)-module on continuous singular simplices, each chain being a finite sum. For an \(m\)-sheeted covering \(q:E\to B\) define
\[
 \operatorname{tr}_j(\sigma)
          =\sum_{\widetilde\sigma:\,q\widetilde\sigma=\sigma}
                                    \widetilde\sigma .
 \tag{18}
\]
There are exactly \(m\) terms by Lemma 3.1. Extend linearly. The term “transfer” here denotes this explicit finite-chain operator.

**Proposition 4.1.** The transfer commutes with the singular boundary and satisfies
\[
 q_\#\operatorname{tr}=mI.
 \tag{19}
\]
For the cyclic covering (2), with deck maps \(D_\ell(Z)=\zeta^\ell Z\), it also satisfies
\[
 \operatorname{tr}\,p_\#=\sum_{\ell=0}^{m-1}(D_\ell)_\# .
 \tag{20}
\]
The same identities hold for the induced homology maps and for smooth chains when the covering is smooth.

**Proof.** For each face inclusion \(a_i:\Delta^{j-1}\to\Delta^j\), restrict every lift of \(\sigma\) to that face. These restrictions are exactly all the lifts of \(\sigma a_i\), each once. To check it, evaluate at any one face point. The evaluations of the \(m\) full lifts biject onto its \(m\)-point fiber by Lemma 3.1, and that fiber likewise bijects onto the lifts of the face simplex. Thus
\[
 \begin{aligned}
 \partial\operatorname{tr}_j\sigma
 &=\sum_{\widetilde\sigma}\sum_{i=0}^j
                             (-1)^i\widetilde\sigma a_i\\
 &=\sum_{i=0}^j(-1)^i
           \operatorname{tr}_{j-1}(\sigma a_i)
  =\operatorname{tr}_{j-1}\partial\sigma .
 \end{aligned}
 \tag{21}
\]
For \(j=0\), both boundaries are zero. Each lift projects to the original simplex, so (19) is literal equality of chains.

For (20), take a simplex \(\beta\) in \(X\). Each \(D_\ell\beta\) lifts \(p\beta\). Their values at a vertex run through the fiber, since the deck action is free and transitive there. By Lemma 3.1 these are all the lifts, giving (20). Smoothness of lifts gives the same argument on smooth chains. Chain maps send cycles to cycles and boundaries to boundaries, so the identities pass to ordinary homology. \(\square\)

**Theorem 4.2.** If \(m\) is invertible in the coefficient ring \(R\), then
\[
 H_j(U;R)=0\quad(j>d).
 \tag{22}
\]
For a field of characteristic zero or characteristic not dividing \(m\), every \(H_j(U;R)\) is finite dimensional. For integral coefficients the transfer proof establishes the narrower assertion
\[
 m\,H_j(U;\mathbb Z)=0\quad(j>d).
 \tag{23}
\]
It does not infer integral vanishing from division by \(m\).

**Proof.** Apply Proposition 4.1 to (2). On homology,
\[
 p_*\operatorname{tr}_*=mI .
 \tag{24}
\]
When \(m\) is invertible, \(\operatorname{tr}_*\) is injective. Corollary 2.2 makes its target zero above \(d\), proving (22). Over a field, its target is finite dimensional in every degree, so its injected source is finite dimensional as well.

With integral coefficients and \(j>d\), the target of the transfer is still zero by Corollary 2.2; (24) therefore gives (23). Multiplication by \(m\) can kill a nonzero abelian-group element, so no integral vanishing follows from this calculation alone. This last limitation is about the inference supplied by the transfer, not a claim that a particular complement has nonzero homology in those degrees. \(\square\)

## 5. The oriented hyperplane tube is injective over the rationals

Let \(L\) be a nonzero linear form, and put
\[
 Y=\{L=0\}\cap U,\qquad V=U\setminus Y
                    =\mathbb P^d\setminus\{FL=0\}.
 \tag{25}
\]
The hyperplane is smooth in projective space, and \(Y\) is its open part where \(F\ne0\). Thus \(Y\) is a closed embedded complex hypersurface of \(U\), even when the zero set of \(F\) is singular. It can be empty, in which case all the tube claims below have zero source.

Use the complex orientation of the real rank-two normal bundle of \(Y\) in \(U\). The exact homological Thom/excision construction in the cited projective-exhaustion lesson gives
\[
 \Theta:H_{d-1}(Y;\mathbb Q)
            \xrightarrow{\ \cong\ }H_{d+1}(U,V;\mathbb Q).
 \tag{26}
\]
It uses ordinary finite chains, oriented normal disc first, and its actual included tubular-neighborhood and Thom proofs. Define the normal-circle-first tube by
\[
 \tau=\partial_{U,V}\Theta:
                   H_{d-1}(Y;\mathbb Q)\longrightarrow H_d(V;\mathbb Q).
 \tag{27}
\]
This definition names a specific map, rather than choosing a possibly differently oriented geometric representative.

**Theorem 5.1.** The map (27) is injective.

**Proof.** Theorem 4.2 applies over \(\mathbb Q\), since \(m\geq1\) is invertible there, and gives \(H_{d+1}(U;\mathbb Q)=0\). The pair exact sequence contains
\[
 H_{d+1}(U;\mathbb Q)\longrightarrow H_{d+1}(U,V;\mathbb Q)
              \xrightarrow{\partial_{U,V}}H_d(V;\mathbb Q).
 \tag{28}
\]
Its first group is zero, so exactness makes the relative boundary injective. Composing with (26) proves the claim.

The local orientation and coefficient are fixed by the same map. For a base cycle \(b\) of dimension \(d-1\), the local relative representative is \(D^2\times b\), with the positively oriented complex normal disc first. The product boundary identity is
\[
 \partial(D^2\times b)=S^1\times b+
                                   D^2\times\partial b.
 \tag{29}
\]
The second term vanishes for a base cycle; the first is the positive counterclockwise normal circle first, with coefficient one. Moving the normal two-disc after the base changes orientation by \((-1)^{2(d-1)}=1\), so it agrees with the cited Thom convention. Moving its boundary circle after the base instead changes orientation by \((-1)^{d-1}\). The map (27) retains the circle-first convention.

For a nontrivial normal bundle, (29) describes the local restrictions of the global homological Thom construction. It does not assert one global product chart or multiply its coefficient by the degree of the affine cover. The finite-cover degree entered only to prove the vanishing of the first group in (28). The relative normal boundary itself has coefficient one. \(\square\)

## 6. The general rational-period receiver now has both inputs

The complete rational-top-form theorem is already written in the linked lesson. In coordinates \(Z_0=L,Z_1,\ldots,Z_d\), let
\[
 \omega=\sum_{j=0}^d(-1)^j Z_j
      dZ_0\wedge\cdots\wedge\widehat{dZ_j}
                             \wedge\cdots\wedge dZ_d .
 \tag{30}
\]

**Corollary 6.1.** If \(\beta\in H_{d-1}(Y;\mathbb Q)\) and its tube (27) has zero periods against every
\[
 \frac{P\omega}{F^kL^s},\qquad
 k,s\geq1,\quad P\ \hbox{homogeneous},\quad
                          \deg P=mk+s-d-1 ,
 \tag{31}
\]
then \(\beta=0\).

**Proof.** The exact preceding Corollary 8.1 of [Rational top forms detect cycles in a hypersurface complement](../../AN02-L182.html#8-the-projective-homogeneous-family-with-positive-pole-exponents) says that (31) detects ordinary rational \(d\)-cycle homology on \(V\), including singular and repeated \(F\). Its actual homology/smooth comparison lets us represent the tube by a finite smooth cycle and take those periods. Their vanishing gives \(\tau\beta=0\) in \(H_d(V;\mathbb Q)\). Theorem 5.1 is injective, so \(\beta=0\).

Equivalently the rational forms span the smooth complex top-degree de Rham group; zero periods give complex null homology, and the exact faithful coefficient comparison in the preceding integration lesson gives rational null homology. The two formulations use the same proved rational receiver. No inference about integral torsion is made. \(\square\)

A separately specified affine equatorial cycle must still be identified with its projective class and with the map (27), including any orientation or multiplicity. The projective covering (2), whose degree is \(m\), is distinct from that normal-circle construction and from projectivizing an affine cycle. Corollary 6.1 therefore completes the general projective period receiver, without presuming the remaining affine comparison or a full component-constancy argument.

## References

[H] Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), §3.G, “Transfer Homomorphisms”. [Author's freely readable text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). The finite-chain lifting and transfer arguments needed here are proved in §§3–4.

[S] Arthur Sard, *The measure of the critical values of differentiable maps*, Bulletin of the American Mathematical Society **48** (1942), 883–890. [Original article](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/sard.pdf). The cited internal lemma gives a complete proof of the equal-dimensional \(C^1\) case; the countable chart passage is written in Proposition 2.1.

[A] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, II*, Acta Mathematica **131** (1973), 145–206. [Primary article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6156-11511_2006_Article_BF02392039.pdf). Its projective tube method is historical context. Here the vanishing group is established by the actual finite cyclic cover and the supplied finite-chain Morse argument; the required homological Thom/excision map is the exact linked internal construction.

Original exposition is CC0-1.0. The linked historical works retain their own rights and are not reproduced. All homology statements use ordinary finite chains; the coefficient hypotheses are stated explicitly.

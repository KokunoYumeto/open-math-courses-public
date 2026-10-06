# The oriented cobordism ring

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Independently authored text dedicated under CC0.*

Oriented cobordism records when the difference between two closed manifolds is the boundary of a compact manifold. Its operations are disjoint union and Cartesian product. We construct the smooth collars and gluing needed for those definitions, track the boundary signs, and then use Pontryagin numbers to detect independent classes.

The [bundle chapter](DG-CHAR-01.html) proves smooth partitions and metrics. The [manifold chapter](DG-CHAR-07.html), Lemma 3.1, gives full local-inverse and smooth-flow proofs. The [integer fundamental-class proof](DG-CHAR-09.html), Lemma 5.1, supplies the outward-oriented boundary identity. The [number chapter](DG-CHAR-11.html) proves exact integer Pontryagin boundary vanishing and general projective-product independence. All manifolds here are smooth, Hausdorff and second countable; closed means compact with empty boundary.

## 1. Boundary charts, orientations and smooth collars

A smooth \(d\)-manifold with boundary, \(d\geq1\), has charts in the half-space
\[
H^d=\{(t,z)\in\mathbb R\times\mathbb R^{d-1}:t\geq0\}.
\]
Smoothness at \(t=0\) means local extension to a smooth map on an open Euclidean set. Chart changes and their inverses have such extensions. Their derivatives at the boundary are invertible: differentiate the inverse identities first for \(t>0\), then take the limit to \(t=0\). They carry the tangent hyperplane \(t=0\) to itself. The induced derivative on the normal quotient is positive, since both maps carry the inward half-space into the inward half-space. Thus the boundary is itself a smooth \((d-1)\)-manifold and its inward normal direction is intrinsic.

The compact exhaustion, shell-cover and bump proof in the bundle chapter applies to half-space charts by restricting its Euclidean bump functions to the half-space. Their zero extensions across support edges are still smooth; local extensions across \(t=0\) give the required boundary smoothness. This proves smooth subordinate partitions of unity and metrics on manifolds with boundary as well.

If \(W\) is oriented and \(d\geq2\), orient \(\partial W\) by declaring a tangent basis positive precisely when putting an outward vector first gives the orientation of \(W\). Changing the outward vector adds tangential terms and multiplies its normal component by a positive number, so does not change this definition. An oriented one-dimensional manifold induces a sign on each boundary point: \(+\) if its positive tangent direction points outward, and \(-\) if it points inward. Degree-zero cobordism uses both signs. The earlier rank-zero Euler evaluations had the stated canonical positive-point convention.

**Theorem 1.1 — Smooth collar.** A smooth manifold with boundary \(W\) has an open neighbourhood of its boundary diffeomorphic to \(\partial W\times[0,1)\), by a map fixing its boundary.

**Proof.** Boundary coordinates give smooth vector fields pointing inward along the boundary. Choose a locally finite smooth partition subordinate to those charts and interior charts. In a boundary chart use its positive \(t\)-direction, and in an interior chart use the zero field. Extend the partition-weighted fields by zero outside their charts and sum. This gives a smooth field \(X\) on \(W\) whose normal quotient at every boundary point is strictly inward: a positive weighted sum of inward vectors remains inward.

Near a boundary point extend \(X\) across \(t=0\) in its chart. The full smooth-flow lemma provides local solutions. Solutions starting on the boundary enter the interior for sufficiently small positive time, since the initial derivative of their height \(t\) is positive. Solutions which remain in \(W\) agree on chart overlaps by uniqueness, independently of the chosen extensions. Write \(\phi(x,s)\) for the resulting solution with initial boundary point \(x\). On a sufficiently small boundary neighbourhood \(U\) there is a common \(b_U>0\) such that all these solutions exist, stay in their boundary chart and have strictly positive height for \(0<s<b_U\).

The derivative at \((x,0)\) of this map is
\[
(a,\lambda)\longmapsto a+\lambda X_x,\qquad
T_x\partial W\oplus\mathbb R\longrightarrow T_xW,
\tag{1.1}
\]
an isomorphism. The ordinary local-inverse theorem on the extended chart applies. Its inverse carries the half-space side to \(s\geq0\): the extended height vanishes at \(s=0\) and has positive \(s\)-derivative nearby, so its sign equals that of \(s\). This proves a local boundary diffeomorphism near \((x,0)\). At positive \(s\), the derivative remains invertible along the solution. Indeed a local flow map has inverse given by the negative-time local flow, by uniqueness; its derivative transports (1.1), while \(X\) transports to itself by differentiating the flow identity. Hence \(\phi\) is locally a diffeomorphism throughout these small half-collars.

Choose a smooth positive function \(\rho\) on \(\partial W\) for which \(0\leq s<\rho(x)\) is within one of the just constructed allowed solution intervals at \(x\). Here is a precise choice. Put \(b(x)=\sup_{x\in U}b_U\), after bounding each \(b_U\) above by one. It is positive and lower semicontinuous, since \(\{b>c\}\) is the union of the corresponding \(U\). Choose a locally finite smooth partition subordinate to relatively compact boundary charts on which \(b\) has a positive lower bound. Multiply its members by positive constants smaller than those bounds and sum. The resulting smooth positive \(\rho\) is smaller than \(b\) at every point. Thus its allowed time belongs to some interval with \(b_U\) larger than that time.

This restricted flow is globally injective. Suppose
\(\phi(x,s)=\phi(y,t)\), with \(s\geq t\). Uniqueness along the compact common solution segments gives
\(\phi(x,s-t)=y\): run both solutions backwards from their common endpoint for time \(t\), using finitely many local uniqueness intervals. If \(s>t\), the left side is interior whereas \(y\) is a boundary point, a contradiction. If \(s=t\), it gives \(x=y\). The argument includes a zero time. Thus the map is an injective local diffeomorphism on
\(\{(x,s):0\leq s<\rho(x)\}\). Its image is open in \(W\), and the local inverses agree to give a smooth global inverse. Finally the change \((x,u)\mapsto(x,\rho(x)u)\) identifies this domain with \(\partial W\times[0,1)\). The empty-boundary case has the empty collar. ∎

The proof works for a noncompact boundary; no uniform positive collar width was presumed. For a compact boundary one can also take a single sufficiently small time interval.

## 2. Gluing and the equivalence relation

**Lemma 2.1 — Oriented gluing.** Let \(X,Y\) be compact oriented manifolds with boundary, and suppose chosen unions of boundary components are identified by an orientation-reversing diffeomorphism \(f\). The quotient obtained by this identification is a smooth compact oriented manifold. Its boundary consists of the remaining boundary components with their original induced orientations.

**Proof.** Use the smooth collars of Theorem 1.1. Write a seam coordinate \(r\), negative on the \(X\)-collar and positive on the \(Y\)-collar, by \(r=-t_X\) and \(r=t_Y\); identify their boundary coordinates with \(f\). Together these are charts across the seam. Away from it keep the original charts. Their transitions are smooth, since on the negative and positive sides the respective smooth collars and \(f\) give the transitions. A smaller collar chart about each seam point has no boundary.

The quotient is Hausdorff. Its equivalence relation is closed in the compact Hausdorff disjoint union: it is the union of the diagonal and the two compact graphs of \(f\) and \(f^{-1}\). For completeness, distinct equivalence classes are compact. Closedness of the relation and a finite subcover give neighbourhoods of these two classes whose Cartesian product misses the relation. Replace each neighbourhood by the complement of the relation-image of its complement; this is an open saturated neighbourhood, because images of closed compact sets under the relation are closed. These saturated neighbourhoods are disjoint and descend to disjoint quotient neighbourhoods. The displayed charts cover the quotient; compactness supplies finitely many, each with a countable coordinate basis, so it is second countable.

Let \(N\) denote the oriented boundary piece of \(Y\). The corresponding \(X\)-piece has orientation \(-N\), after using \(f\). The outward-first convention says that in an inward collar the ambient orientation is \(-dt\) followed by the boundary orientation. Hence on the \(X\)-side it is
\(-dt_X\wedge o_{-N}=dt_X\wedge o_N=-dr\wedge o_N\),
and on the \(Y\)-side it is
\(-dt_Y\wedge o_N=-dr\wedge o_N\).
They agree across the seam. This determinant argument includes signed boundary points when the ambient dimension is one. The untouched boundary charts retain their orientations. ∎

For closed oriented \(d\)-manifolds define \(M\sim N\) if a compact oriented \((d+1)\)-manifold \(W\) has outward boundary orientation-preservingly diffeomorphic to \(M\sqcup(-N)\). An orientation-preserving diffeomorphism already gives such a relation by a cylinder.

**Proposition 2.2.** This relation is reflexive, symmetric and transitive.

**Proof.** Orient \([0,1]\times M\) by its time direction first and the orientation of \(M\) second. Its top boundary is \(M\) and bottom boundary is \(-M\), giving reflexivity. Reversing the orientation of a cobordism reverses both its boundary orientations and proves symmetry. For transitivity glue the \(-N\) boundary of a cobordism from \(M\) to \(N\) to the \(N\) boundary of a cobordism from \(N\) to \(P\). Lemma 2.1 gives a compact oriented smooth manifold with boundary \(M\sqcup(-P)\). This proves transitivity, including disconnected and empty manifolds. ∎


## 3. The group and its graded product

Write \(\Omega_d^{SO}\) for the set of oriented cobordism classes of closed oriented \(d\)-manifolds. Superscript \(SO\) records the orientation structure; it does not impose a connection or metric. Disjoint union defines addition:
\[
[M]+[N]=[M\sqcup N],\qquad
0=[\varnothing],\qquad -[M]=[-M].
\tag{3.1}
\]
It is well defined. Given two representing cobordisms, their disjoint union has the required disjoint-union boundary. The natural component permutations are orientation-preserving, giving associativity and commutativity, and adjoining the empty manifold changes nothing. The cylinder proves \([M]+[-M]=0\), so this is an abelian group.

In degree zero we use finite sets of signed points. A compact zero-manifold is finite because its point neighbourhoods form an open cover. Define its signed count
\[
\epsilon(M)=\sum_{x\in M}\operatorname{sign}(x).
\tag{3.2}
\]
For any compact oriented one-manifold \(W\), the relative fundamental class from the integer compact-set proof has boundary equal to the sum of these signed points. This statement can also be checked at each endpoint directly: an oriented local interval chain has boundary its positive terminal point minus its initial point. Excision and point-value detection identify its endpoint coefficient with \(+\) when the positive tangent points outward and \(-\) when it points inward. The pair sequence makes that sum zero in \(H_0(W;\mathbb Z)\), and projection to a point shows its total signed count is zero. Thus (3.2) is a cobordism invariant.

Conversely, a signed finite set with zero count has equally many positive and negative points. Pair them and take one oriented interval for each pair. The endpoint rule gives a compact cobordism bounding the set. Every integer is realized by its absolute number of identically signed points, so
\[
\Omega_0^{SO}\cong\mathbb Z
\tag{3.3}
\]
by signed count. In particular the positive point represents \(1\).

Orient \(M^m\times N^n\) by the \(M\)-tangent basis first and the \(N\)-tangent basis second. Define
\[
[M][N]=[M\times N]\in\Omega_{m+n}^{SO}.
\tag{3.4}
\]
When a factor is zero-dimensional its point sign multiplies the orientation on the other factor. This agrees with the signed count convention.

**Theorem 3.1.** These operations make
\(\Omega_*^{SO}=\bigoplus_{d\geq0}\Omega_d^{SO}\)
a unital graded ring. Its homogeneous products satisfy
\[
\alpha\beta=(-1)^{mn}\beta\alpha,
\qquad \alpha\in\Omega_m^{SO},\ \beta\in\Omega_n^{SO}.
\tag{3.5}
\]

**Proof.** If \(M\sim M'\) by \(X\), then \(X\times N\) is a compact manifold with boundary, without corners since \(N\) is closed. An outward vector lies in the \(X\)-factor. Putting it before the remaining product basis shows
\(\partial(X\times N)=(\partial X)\times N\)
with its product orientation. Thus the product does not depend on its first representative.

For independence of the second representative, use \(M\times Y\), where \(\partial Y=N\sqcup(-N')\). To move an outward vector of \(Y\) to the first position crosses \(m\) tangent vectors. Consequently its boundary orientation is
\((-1)^m M\times\partial Y\).
Multiply the ambient product orientation by \((-1)^m\); its boundary is now exactly
\((M\times N)\sqcup(-(M\times N'))\).
This proves independence of the second representative as well. These sign computations include dimension-zero factors by their assigned signs.

The usual product associator preserves the ordered triple tangent basis, proving associativity. Products distribute over disjoint unions by the component identifications, giving bilinearity. The positive point is the two-sided identity. Finally the swap diffeomorphism crosses each of \(m\) basis vectors with each of \(n\) basis vectors. Its determinant sign is \((-1)^{mn}\); hence the oriented manifold it identifies is \(M\times N\) with that sign times \(N\times M\). Equation (3.1) interprets a negative orientation as the additive inverse and proves (3.5). Finite sums of degrees give the stated direct-sum ring. ∎

A closed oriented sphere is zero in positive-dimensional cobordism: the standard disk has its sphere as outward boundary. This does not force its Euler number to vanish; even-dimensional spheres have Euler number two. Euler numbers and stable Pontryagin numbers behave differently under boundaries.

## 4. Connected sums through an explicit trace

Let \(M,N\) be connected closed oriented \(d\)-manifolds, \(d\geq2\). Remove interiors of two positively parametrized disks and identify their boundary spheres by a reflection of one disk coordinate. With product collars this produces the oriented connected sum \(M\#N\); the reflection reverses the sphere orientation, so Lemma 2.1 gives its smooth structure and orientation. The outside portions retain their original orientations.

**Lemma 4.1 — Connected-sum trace.** There is a compact oriented cobordism from \(M\sqcup N\) to \(M\#N\). Therefore
\[
[M\#N]=[M]+[N].
\tag{4.1}
\]

**Proof.** Start with \(C=[0,1]\times(M\sqcup N)\), with time first. At its top choose one positive disk in each component. Attach a handle
\[
H=[-1,1]\times D^d
\]
by its two end disks to those disks. The orientation of \(H\) is its interval direction first and its disk direction second. Its left end has disk orientation \(-D^d\), whereas its right end has \(+D^d\). The top of \(C\) has the orientations of \(M,N\). Thus at the left end use the positive disk parametrization and at the right end use the parametrization precomposed with a reflection. Both attaching maps reverse the induced end/top boundary orientations.

There is a mild corner at the rim of each attaching disk, which we now smooth explicitly. In a collar of a disk rim write \(q\) for its disk radial displacement and \(r\) for the inward collar height. After the two halves of the attaching disk are glued, the local cross-section of the union is
\[
\{r\geq0\}\ \cup\ \{q\leq0,\ r\leq0\}.
\tag{4.2}
\]
The rim sphere directions are additional product coordinates. This is a plane with its lower-right quadrant removed. Round its two boundary rays by a smooth curve in the cross-section, joining the downward ray to the rightward ray and agreeing with the rays outside a small neighbourhood of their meeting.

Here is an actual construction of the curve. Put
\(\beta(u)=\exp(-1/((u-1/3)(2/3-u)))\) for \(1/3<u<2/3\) and zero elsewhere, and set
\(\theta(u)=\frac{\pi}{2}\int_0^u\beta(v)\,dv/\int_0^1\beta(v)\,dv\).
The proved bump-extension argument makes \(\theta\) smooth and nondecreasing, equal to zero near \(0\) and to \(\pi/2\) near \(1\). Put
\[
(q(u),r(u))=(0,-a)+
c\int_0^u(\sin\theta(v),\cos\theta(v))\,dv,
\]
where \(a=c\int_0^1\cos\theta(v)\,dv\).
Its initial point lies on the downward ray, its terminal point on the rightward ray, and its derivative is everywhere nonzero. At the ends it is a straight ray segment, with all curvature derivatives zero there. A small positive \(c\) puts the joining curve inside the chosen coordinate neighbourhood. Replace (4.2) in that neighbourhood by the side of this curve which contains the upper-left quadrant. The curve lies in the formerly missing quadrant, so this replacement fills a small rounded region. The new region is taken in the auxiliary full \((q,r)\)-coordinate plane and glued to the old region where their rays and interiors agree; no additional global ambient space is required. The same replacement in the product with the rim sphere has its original overlap charts away from the corner. Its boundary is smooth.

The curve is monotone in both coordinates; its boundary arc, together with the continued rays, has one interval parametrization in the same order as the original two rays. The replacement is homeomorphic to the original neighbourhood, fixing its outer overlap. To see this explicitly, take a point \(p\) in the upper-left quadrant. The angular derivative along the joining curve has numerator
\((q-p_q)r'-(r-p_r)q'>0\).
Thus each affected ray from \(p\) meets the old two-ray boundary once and the new curve once, with intersection distances varying continuously. Reparametrize these radial intervals by increasing piecewise linear maps, fixing a small disk about \(p\) and the unchanged outer overlap and sending old boundary to new boundary. Their inverses have the same continuous radial description. This gives the claimed homeomorphism and preserves all component identifications. Taking its product with the rim sphere also proves that replacing the coordinate patches preserves Hausdorffness, compactness and second countability.

Use the curve's arc-length coordinate and the rim coordinate as boundary coordinates; a small normal coordinate is valid by the ordinary local-inverse theorem. Compactness of the rim supplies a uniform normal width. Because the two attaching rims are compact and disjoint, choose a common small \(c\) for each, within the disk radial and collar coordinate domains. The replacements agree with the original regions near the outer edges of those domains. Their local half-space charts and the unchanged charts give the resulting compact smooth manifold. The compatible ambient orientations extend over the filled regions by their cross-section coordinates.

Its bottom boundary is \(-(M\sqcup N)\). Its top boundary consists of the two punctured manifolds joined by the side \([-1,1]\times S^{d-1}\) of the handle, with the described rounding at its ends. This is precisely the connected-sum gluing with an inserted sphere cylinder; stretching the two sphere collars identifies it diffeomorphically with \(M\#N\). The end attachment used one reflection, giving the orientation specified at the start of this section. Thus its boundary is \((M\#N)\sqcup(-(M\sqcup N))\), and symmetry of cobordism proves (4.1). ∎

The collar stretching in this last identification can be made smooth while fixing the exterior charts. Each rounded boundary arc is a smooth interval with straight end segments. Choose short end segments in the source and target intervals. A positive smooth function, equal to one there and adjusted by a bump in the middle to have the required total integral, integrates to an increasing interval diffeomorphism agreeing with the exterior coordinates at both ends. Apply this same interval map in the product with the rim sphere. It absorbs the inserted cylinder and matches the unchanged punctured-manifold charts on open end segments, so gives the asserted global diffeomorphism.

Replacing \(N\) by its orientation reverse gives
\([M\#(-N)]=[M]-[N]\).
The trace, rather than a claim about the punctured tangent bundles alone, is what lets every stable characteristic number be added under connected sum.

## 5. Pontryagin homomorphisms and projective classes

For \(I\vdash k\), \(k\geq1\), the number chapter proves vanishing of the integer \(p_I\) number on every outward-oriented boundary. Naturality and additivity of the fundamental class give
\[
p_I[M\sqcup N]=p_I[M]+p_I[N],\qquad
p_I[-M]=-p_I[M].
\tag{5.1}
\]
If \(M\sim N\), apply boundary vanishing to \(M\sqcup(-N)\). It gives \(p_I[M]=p_I[N]\). Thus each number defines a group homomorphism
\[
p_I:\Omega_{4k}^{SO}\longrightarrow\mathbb Z.
\tag{5.2}
\]
This proves the assigned Pontryagin boundary lemma and its homomorphism corollary in positive dimension, with every sign retained. In dimension zero the empty characteristic product is \(1\) and its evaluation on a signed point set is its signed count, which also vanishes on boundaries by Section 3.

**Theorem 5.1 — Independent projective products.** The oriented manifolds
\[
\mathbb {CP}^{2j_1}\times\cdots\times\mathbb {CP}^{2j_r},
\qquad (j_1,\ldots,j_r)\vdash k,
\tag{5.3}
\]
represent linearly independent elements of \(\Omega_{4k}^{SO}\). Consequently
\[
\dim_{\mathbb Q}(\Omega_{4k}^{SO}\otimes\mathbb Q)\geq p(k),
\tag{5.4}
\]
where \(p(k)\) is the number of partitions of \(k\).

**Proof.** Suppose an integer linear combination of these cobordism classes is zero. Apply all the homomorphisms (5.2). Their values form exactly the projective-product Pontryagin matrix of the number chapter, Theorem 4.2, which is nonsingular over \(\mathbb Q\). Thus all its integer coefficients are zero. The same argument applies to a rational combination in the tensor product: each homomorphism extends to a rational linear map, and the same nonsingular matrix forces every rational coefficient to vanish. This proves both assertions; no exact rank or torsion classification is used. The empty product in degree zero is the positive point and agrees with (3.3). ∎

In particular \([\mathbb {CP}^2]\) has infinite order, because \(p_1[\mathbb {CP}^2]=3\). The two degree-eight classes \([\mathbb {CP}^4]\) and \([\mathbb {CP}^2\times\mathbb {CP}^2]\) are independent; their \(p_1^2,p_2\) matrix has determinant \(45\). No positive disjoint union of either is an oriented boundary.

Connected-sum traces and (5.1) give the requested contrasting examples:
\[
p_1[\mathbb {CP}^2\#\mathbb {CP}^2]=6,\qquad
p_1[\mathbb {CP}^2\#(-\mathbb {CP}^2)]=0.
\tag{5.5}
\]
The first is not an oriented boundary. The second actually is: (4.1) identifies its class with \([\mathbb {CP}^2]-[\mathbb {CP}^2]=0\), and transitivity with the bounding cylinder gives a compact bounding manifold. Its vanishing number alone would only remove this obstruction; here the explicit trace provides the stronger conclusion.

The signature is another invariant of oriented cobordism. Its boundary-vanishing proof and relation to the Pontryagin homomorphisms will be established in the signature chapter. The present rank lower bound requires only the proved integer numbers. The rational spanning assertion and exact rank require Thom's theorem, developed next.


## 6. Exercises with solutions

**Exercise 6.1 — Easy.** Prove that oriented cobordism is an equivalence relation, including its smooth gluing step.

**Solution.** Time-first orientation on \([0,1]\times M\) gives top \(M\) and bottom \(-M\), proving reflexivity. Reversing the ambient orientation of a representing manifold reverses its boundary, proving symmetry. For transitivity identify the common boundary pieces with opposite orientations. Smooth collars give one signed transverse coordinate across the join, and the two ambient orientations both become \(-dr\) followed by the chosen seam orientation. Lemma 2.1 shows the quotient is a smooth compact oriented manifold with just the two unglued boundary pieces. This proves transitivity, including the empty and disconnected cases.

**Exercise 6.2 — Medium.** Prove that Pontryagin numbers are homomorphisms on oriented cobordism groups.

**Solution.** For a boundary \(M=\partial W\), the smooth outward unit normal splits \(TW|_M=TM\oplus\varepsilon\). Exact Pontryagin stability extends each factor \(p_i(TM)\) from \(W\). The signed relative fundamental identity puts \([M]\) in the image of the pair connecting map, so \(i_*[M]=0\). A top Pontryagin product therefore evaluates to
\(\langle p_I(TW),i_*[M]\rangle=0\).
If \(\partial W=M\sqcup(-N)\), this gives \(p_I[M]=p_I[N]\). Fundamental classes and evaluations add over disjoint unions, so the induced map to \(\mathbb Z\) is an additive homomorphism. In dimension zero the empty product evaluates as signed count; the endpoint boundary rule and projection to a point give the same vanishing.

**Exercise 6.3 — Medium.** Compute \(p_1\) on
\(\mathbb {CP}^2\#\mathbb {CP}^2\) and
\(\mathbb {CP}^2\#(-\mathbb {CP}^2)\). Determine what boundary vanishing alone says, then use the trace.

**Solution.** The projective tangent formula gives \(p_1[\mathbb {CP}^2]=3\), and orientation reversal gives \(-3\). The connected-sum trace turns either sum into a cobordism sum, on which the homomorphism is additive. The numbers are consequently \(6\) and \(0\). The first cannot bound. The zero value merely removes this particular obstruction for the second; in this example the trace gives the stronger identity \([\mathbb {CP}^2\#(-\mathbb {CP}^2)]=0\). Glue its trace along the lower boundary to the cylinder of \(\mathbb {CP}^2\). The lower \(+\) and \(-\) components cancel in the gluing, leaving a compact oriented filling of the connected sum.

**Exercise 6.4 — Hard.** Prove that the projective products indexed by partitions of \(k\) are independent in \(\Omega_{4k}^{SO}\), and obtain its rank lower bound.

**Solution.** Apply every top \(p_I\) homomorphism to a proposed integer relation between those products. The resulting vector equation has the number chapter's nonsingular rational Pontryagin matrix as its coefficient matrix. Its inverse over \(\mathbb Q\) forces all the integer coefficients to vanish. Tensor the homomorphisms with \(\mathbb Q\) to give the same argument for a relation in \(\Omega_{4k}^{SO}\otimes\mathbb Q\). There are \(p(k)\) such independent rational classes, proving the lower bound. In degree eight the concrete matrix is
\[
\begin{pmatrix}25&18\\10&9\end{pmatrix},
\]
with determinant \(45\), for rows \(p_1^2,p_2\) and columns \(\mathbb {CP}^4,\mathbb {CP}^2\times\mathbb {CP}^2\). Nonsingularity proves independence; it does not prove that these two classes generate the integral group.

**Exercise 6.5 — Easy.** Determine the oriented cobordism group of signed finite point sets.

**Solution.** An oriented interval contributes one positive and one negative endpoint. More generally the relative fundamental boundary identity, followed by \(H_0(W)\to H_0(\mathrm{pt})\), makes the signed count of any one-dimensional boundary zero. Thus signed count is necessary for a zero class. It is sufficient: pair each positive point with a negative point and fill each pair by an oriented interval. Every integer count occurs, so signed count gives an isomorphism \(\Omega_0^{SO}\to\mathbb Z\). The one positive point is the identity for the product ring; the one negative point is its additive inverse.

**Exercise 6.6 — Medium.** Check both the boundary sign of \(M^m\times Y\) and the graded commutativity sign of the product.

**Solution.** In the ambient product basis the \(m\) tangent vectors of \(M\) precede the \(Y\)-vectors. Moving an outward \(Y\)-normal to the first position crosses exactly those \(m\) vectors. The induced boundary is therefore \((-1)^m M\times\partial Y\). Reversing the ambient orientation by that sign makes it the desired cobordism between \(M\times N\) and \(M\times N'\) when \(\partial Y=N\sqcup(-N')\). Under the swap \(M\times N\to N\times M\), each \(M\)-basis vector crosses each \(N\)-basis vector, for \(mn\) transpositions. Hence the sign is \((-1)^{mn}\), proving (3.5). A sign reversal of the whole manifold is exactly the additive inverse in the cobordism group.

## Sources and scope

Freely readable treatments include Ioan Mărcuț, [*Manifolds. Lecture Notes — Fall 2017*](https://www.math.ru.nl/~imarcut/index_files/lectures_2017.pdf), Section 15.1, pages 137–141, and Haynes Miller, [*Notes on Cobordism*](https://math.mit.edu/~hrm/papers/cobordism.pdf), December 5, 2001, Chapter 1, Section 1, and Chapter 2, Section 1. Miller's notes were typed by Dan Christensen and Gerd Laures from his lectures. Mărcuț gives the inward-field construction and a collar proof for compact boundary; the positive variable width above also treats noncompact boundary. Miller introduces the oriented relation and group, leaving the smooth transitivity step to differential topology. The full collar, gluing, trace and signed product proofs are given here. The projective-class independence follows from the complete integral number calculation in the preceding chapter; Miller's 2020 [Algebraic Topology II notes](https://ocw.mit.edu/courses/18-906-algebraic-topology-ii-spring-2020/pages/lecture-notes/), Lecture 40, give further context on rational oriented bordism.

The boundary orientation is outward normal first, with signed points explicitly included in dimension zero. The ring is graded commutative; its product construction uses a manifold with boundary times a closed manifold and therefore creates no product corners. The sole handle corners used for the trace are explicitly rounded. Projective products give a rank lower bound and rational independence; the exact rational rank and spanning statement is proved in [the rational-bordism companion](rational-oriented-bordism-and-projective-generators.md). Integral generation and torsion are separate questions. Author-instance AI self-check is distinct from independent review. The immediate proofs used here are given in this chapter and its linked prerequisites.

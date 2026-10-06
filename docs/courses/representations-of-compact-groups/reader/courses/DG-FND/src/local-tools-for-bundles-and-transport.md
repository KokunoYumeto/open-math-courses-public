# Local tools for bundles and transport

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text dedicated to the public domain under CC0 1.0.*

Geometry uses local coordinates to build objects and then forgets those coordinates. This lesson proves the three local tools used in the first part of the course: local inversion, solutions of ordinary differential equations, and smooth partitions of unity. It also constructs the smooth quotient by an embedded closed Lie subgroup. These proofs make the later bundle constructions explicit.

The prerequisites are completeness of the real numbers, finite-dimensional linear algebra, multivariable differentiation, integration of continuous functions on a compact interval, and the definition of a smooth manifold. A manifold here is finite dimensional, Hausdorff and second countable, without boundary unless a boundary is specified. A Lie group is such a manifold with smooth multiplication and inversion. The arguments below are given in full.

## 1. Contraction and local inversion

**Lemma 1.1 (contraction).** Let \(X\) be a complete metric space. If \(T:X\to X\) satisfies \(d(Tx,Ty)\leq qd(x,y)\), where \(0\leq q<1\), it has exactly one fixed point.

**Proof.** Set \(x_{j+1}=Tx_j\). For \(m>n\), the triangle inequality gives

\[
d(x_m,x_n)\leq\sum_{j=n}^{m-1}q^j d(x_1,x_0)
\leq\frac{q^n}{1-q}d(x_1,x_0).
\]

The sequence converges to a point \(x\). The Lipschitz inequality implies \(Tx=\lim Tx_j=\lim x_{j+1}=x\). If \(Ty=y\), then \(d(x,y)\leq qd(x,y)\), so \(x=y\). □

**Theorem 1.2 (smooth inverse function theorem).** Suppose \(f:U\to\mathbb R^n\) is smooth on an open set and \(Df(a)\) is invertible. There are open neighbourhoods of \(a\) and \(f(a)\) on which \(f\) is a smooth diffeomorphism.

**Proof.** Translate the points to zero and replace \(f\) by \(Df(a)^{-1}(f-f(a))\). Thus \(f(0)=0\) and \(Df(0)=I\). Choose a closed ball \(B_r\subset U\) on which \(\|Df-I\|\leq q<1\). The fundamental theorem of calculus on line segments shows that \(k(x)=x-f(x)\) is \(q\)-Lipschitz on this ball. If \(\|y\|<(1-q)r\), the map

\[
T_y(x)=y+k(x)
\]

maps \(B_r\) to itself and is a contraction. Its fixed point \(g(y)\) is the unique solution of \(f(x)=y\) in the ball. It lies in its interior. Subtracting two fixed-point equations gives

\[
\|g(y)-g(z)\|\leq(1-q)^{-1}\|y-z\|.
\]

Every \(Df(x)\) on the ball is invertible: the convergent series \(\sum_{j\geq0}(I-Df(x))^j\) is its inverse. Write \(x=g(y)\), \(\delta=g(y+h)-g(y)\). Taylor's first-order formula gives

\[
h=Df(x)\delta+o(\|\delta\|).
\]

The Lipschitz bound makes the remainder \(o(\|h\|)\). Therefore \(Dg(y)=Df(g(y))^{-1}\). This derivative is continuous. The displayed identity then proves smoothness by induction: matrix inversion is smooth where the determinant is nonzero, as follows from the cofactor formula. Restrict the ball to the inverse image of the open ball \(\|y\|<(1-q)r\). On this open set \(f\) and \(g\) are smooth inverses. Undo the two initial changes of coordinates. □

**Corollary 1.3 (submersion coordinates).** A smooth map whose differential is surjective at a point has local coordinates in which it is projection onto the first coordinates. Its level set through that point is an embedded submanifold, and it has a smooth local section through that point.

**Proof.** In coordinates choose a complementary linear projection \(\ell\) onto the kernel of the differential. The map \(x\mapsto(f(x),\ell(x-a))\) has invertible differential at \(a\), and is a local coordinate system by Theorem 1.2. In these coordinates \(f\) is the first projection, its level set is obtained by fixing those first coordinates, and a section is obtained by fixing the last coordinates at zero. □

**Corollary 1.4 (constant rank).** If a smooth map has constant rank \(r\) near a point, its local image is contained in an embedded \(r\)-dimensional submanifold, and coordinates on that image make the map projection onto \(r\) variables.

**Proof.** Select an invertible \(r\)-by-\(r\) minor of its derivative. Use its corresponding \(r\) output functions together with the unused input coordinates as new input coordinates; Theorem 1.2 makes this change invertible. In these coordinates the map is \((u,z)\mapsto(u,\psi(u,z))\). Constant rank \(r\) forces every \(z\)-derivative of \(\psi\) to vanish, since its first \(r\) derivative rows are \((I,0)\). On a product coordinate box, \(\psi\) is therefore independent of \(z\), by integration on line segments in the \(z\)-variables. The image is the graph of \(\psi(u)\), and graph coordinates give the asserted projection. □

## 2. Differential equations and their parameters

**Theorem 2.1 (local flow).** Let \(F(t,x,\lambda)\) be smooth on an open subset of \(\mathbb R\times\mathbb R^n\times\mathbb R^m\). Near every initial datum \((t_0,x_0,\lambda_0)\), the equation \(x'=F(t,x,\lambda)\) has a unique local solution. The solution is smooth in time, initial value and parameter. A solution extends past a finite endpoint whenever its graph remains in a compact subset of the domain, with the time coordinate included.

**Proof.** Choose a rectangular neighbourhood with compact closure in the domain. On it \(\|F\|\leq B\) and \(\|D_xF\|\leq L\). For initial values in a smaller rectangle choose \(\epsilon>0\) uniformly so that \(\epsilon B\) is smaller than the distance to the spatial boundary and \(\epsilon L<1\). On continuous curves in the spatial closed ball, the integral operator

\[
(Tu)(t)=x_0+\int_{t_0}^t F(s,u(s),\lambda)\,ds
\]

preserves that ball and is a contraction in the supremum norm. Continuous curves form a complete space: a uniformly Cauchy sequence converges pointwise in \(\mathbb R^n\), uniformly, and the uniform limit is continuous. Lemma 1.1 supplies a fixed point. The fundamental theorem of calculus makes it a solution. Any two solutions agree on sufficiently short common intervals by the same contraction estimate; successive intervals prove uniqueness on their entire common domain.

Here are the parameter details. If a nonnegative continuous function obeys \(u(t)\leq c+L\int_{t_0}^t u(s)\,ds\), put \(v=c+L\int u\). Then \(v'\leq Lv\), whence \(v(t)\leq ce^{L(t-t_0)}\) by differentiating \(e^{-Lt}v\); for \(c=0\) first replace \(c\) by a positive number and let it decrease to zero. This estimate applied to the difference of two integral equations proves continuous, locally Lipschitz dependence on the initial data and parameters.

For one parameter \(z\), consider the linear integral equation

\[
Y(t)=Y(t_0)+\int_{t_0}^t\bigl(D_xF(s,x(s),\lambda)Y(s)+D_zF(s,x(s),\lambda)\bigr)\,ds.
\]

Here \(D_zF\) is zero for an initial-value parameter and is the corresponding partial derivative for an external parameter; \(Y(t_0)\) is the derivative of the initial value. The same contraction argument solves this equation. Subtract it from the difference quotient of the original integral equation. The mean-value formula expresses the remaining coefficients as averages of derivatives of \(F\) along segments joining nearby solutions. Uniform continuity on the compact rectangle makes these coefficients converge uniformly to those in the linear equation. The preceding exponential estimate forces the difference quotient to converge uniformly to \(Y\). Thus the first parameter derivatives exist and are continuous. Differentiating the linear integral equation repeats this argument for each higher derivative: the highest derivative enters linearly with coefficient \(D_xF\), and the inhomogeneous terms involve only already constructed lower derivatives and derivatives of \(F\). Induction proves smooth dependence of every order. The equation itself gives all time derivatives. A varying initial time can be included by translating \(t=t_0+s\), so the same argument covers it.

Finally, a compact subset of the domain is covered by finitely many rectangles of the preceding type. The minima of their allowed time lengths and spatial margins give a positive uniform existence time for starting points in that compact set, after shrinking the rectangles. Starting sufficiently near a finite endpoint therefore extends the solution across it. Uniqueness makes this extension agree with the original solution. □

Coordinate changes preserve the equation by the chain rule. Thus the theorem applies to smooth time-dependent vector fields on a manifold. Local solutions in intersecting charts agree by uniqueness.

**Lemma 2.2 (invariant equations do not escape).** Let \(G\) be a Lie group, and let \(b:[a,c]\to\mathfrak g\) be continuous. The equation

\[
g'(t)=(dR_{g(t)})_e b(t)
\]

has a unique \(C^1\) solution on all of \([a,c]\) for every initial value. The same holds piecewise for \(b\) continuous on finitely many closed pieces, with possible jumps between them.

**Proof.** Work in a fixed coordinate neighbourhood of \(e\). The values of \(b\) lie in a compact subset of \(\mathfrak g\). The coordinate vector field is continuous in time and smooth in position, with uniform bounds on itself and its position derivative in a smaller compact coordinate box. The integral-operator proof of Theorem 2.1 uses exactly those bounds for existence and uniqueness; it does not differentiate the time variable. Thus it gives a positive existence time \(\epsilon\), uniform in the starting time, for a solution \(h\) starting at \(e\). If a solution is to start at \(g_0\), set \(g=h g_0\). Right translation commutes with the displayed equation, so this solves it with the same uniform time length. Starting afresh at the end of each interval of length less than \(\epsilon\) reaches \(c\) after finitely many steps. Uniqueness glues the pieces. Apply this argument to each continuous piece when necessary. No compactness assumption on \(G\) has been used. □

The constant equation \(g'=(dL_g)_e A\) is handled by the identical proof with left translation. Define \(\exp(tA)\) as its solution with initial value \(e\). Uniqueness gives \(\exp((s+t)A)=\exp(sA)\exp(tA)\). Smooth dependence gives smoothness of \(\exp:\mathfrak g\to G\). Since the initial derivative is \(A\), \(D\exp_0\) is the identity. Theorem 1.2 makes the exponential map a local diffeomorphism. Conjugating the equation gives

\[
a\exp(tA)a^{-1}=\exp(t\operatorname{Ad}(a)A).
\]

This also defines the linear adjoint representation as the differential at the identity of conjugation.

## 3. Smooth weights with controlled support

**Theorem 3.1 (partition of unity).** Every open cover of a smooth manifold admits a locally finite smooth partition of unity subordinate to it. The supporting sets can be chosen to have compact closure in coordinate neighbourhoods lying in members of the cover. If \(K\) is closed and \(U\) is an open neighbourhood of \(K\), there is a smooth function \(\chi:M\to[0,1]\) equal to one on a neighbourhood of \(K\), with support contained in \(U\).

**Proof.** A countable atlas, refined by coordinate balls with rational centres and radii and compact closures, gives a countable cover \(B_j\) by relatively compact open sets. Construct compact sets \(K_j\) recursively so that \(K_j\subset\operatorname{int}K_{j+1}\), \(\overline B_1\cup\cdots\cup\overline B_j\subset K_j\), and \(\bigcup K_j=M\). To do this, cover the preceding compact set and the next finite collection of closures by finitely many relatively compact coordinate balls, and take the union of their closures. Begin with \(K_0=K_{-1}=\varnothing\).

For each \(j\geq1\), the compact layer \(K_j\setminus\operatorname{int}K_{j-1}\) has a finite cover by coordinate balls \(V_{j\ell}\) whose closures lie in slightly larger coordinate balls \(W_{j\ell}\). Choose the latter inside a member of the given cover and inside

\[
\operatorname{int}K_{j+1}\setminus K_{j-2}.
\]

This is possible because the compact layer lies in that open set. Choose the smaller balls to cover the layer and then take a finite subcover. The family of larger balls is locally finite: a neighbourhood contained in \(\operatorname{int}K_N\) meets none of the sets with \(j\geq N+2\); only finitely many sets have the remaining indices.

In each larger coordinate ball choose a smooth nonnegative bump function positive on the closure of the smaller ball and supported in the larger ball. Such a bump follows explicitly from \(\eta(t)=e^{-1/t}\) for \(t>0\), \(\eta(t)=0\) for \(t\leq0\), composed with squared Euclidean distances. Its derivatives at zero vanish because every polynomial in \(1/t\) times \(e^{-1/t}\) tends to zero. Extend the bump by zero outside its chart. Call the resulting functions \(b_i\). Their locally finite sum \(b\) is smooth and strictly positive. Then \(\rho_i=b_i/b\) is the required partition.

For the last assertion apply the first part to \(\{U,M\setminus K\}\), and let \(\chi\) be the sum of the functions assigned to \(U\). The union of their supports is closed because the supports are locally finite; it is contained in \(U\). Near each point of \(K\), local finiteness and the fact that every other support misses \(K\) make all functions assigned to \(M\setminus K\) vanish. Thus \(\chi=1\) on an open neighbourhood of \(K\). □

## 4. Quotients by a closed Lie subgroup

In this section an **embedded Lie subgroup** \(H\subset G\) is a subgroup which is an embedded submanifold and whose Lie operations are the restricted operations. Closedness alone is not being used as a substitute for the embedded-subgroup hypothesis.

**Theorem 4.1 (smooth homogeneous quotient).** If \(H\) is an embedded closed Lie subgroup of \(G\), the coset space \(G/H\) is a Hausdorff second-countable smooth manifold. The quotient map \(q:G\to G/H\) is a smooth submersion with local smooth sections. Moreover, \(G\to G/H\) is a principal \(H\)-bundle.

**Proof.** Choose a vector-space complement \(\mathfrak m\) to \(\mathfrak h=T_eH\) in \(\mathfrak g\). The map

\[
\mathfrak m\times H\longrightarrow G,\qquad (X,h)\longmapsto\exp(X)h
\]

has invertible differential at \((0,e)\). Theorem 1.2 supplies small neighbourhoods on which it is a diffeomorphism onto an open neighbourhood of \(e\). Let \(S\) be a sufficiently small exponential slice \(\exp(U_{\mathfrak m})\). Shrink it so that \(s^{-1}s'\) lies in the chosen identity neighbourhood for all \(s,s'\in S\). Because \(H\) is embedded, elements of \(H\) in a sufficiently small ambient neighbourhood of \(e\) lie in the chosen subgroup chart.

If \(s'=sh\) with \(s,s'\in S\), then \(h=s^{-1}s'\) belongs to that small subgroup chart. The uniqueness in the preceding local product chart forces \(s=s'\) and \(h=e\). Thus each coset meets \(S\) at most once. The multiplication map \(S\times H\to SH\) has invertible differential at every point: at \((s,e)\) this holds after the initial shrinking by continuity, and at \((s,h)\) it follows by right translation. It is injective by the coset observation. It is consequently a bijective local diffeomorphism onto its image, and its image \(SH\) is open. Its local smooth inverses agree, so it is a diffeomorphism.

The quotient map is open, since \(q^{-1}(q(V))=VH\) is open for open \(V\subset G\). Hence \(q(SH)\) is open, and the unique representative in \(S\) gives a homeomorphism \(q(SH)\to S\). Left translates of these charts cover the quotient. Their transitions are smooth: on an overlap, use the smooth product inverse \(SH\to S\times H\), translated by the relevant group elements, and take its \(S\)-component. These charts make \(q\) a submersion, because in the product chart it is the projection onto \(S\). Their inverses give smooth local sections.

The equivalence relation is closed: \(q(g)=q(g')\) exactly when \(g^{-1}g'\in H\). To separate distinct cosets, take neighbourhoods \(V,V'\) of their representatives with \(v^{-1}v'\notin H\) for all \(v\in V,v'\in V'\), using closedness of \(H\) and continuity. The open sets \(q(V),q(V')\) are disjoint. Second countability follows by projecting a countable basis of \(G\) under the open quotient map. Finally, a local section \(s\) gives the principal trivialization \((x,h)\mapsto s(x)h\); its inverse is smooth by the product chart. □

## 5. Worked examples

For \(G=\mathrm{GL}(n,\mathbb R)\), a complement to \(\mathfrak o(n)\) consists of symmetric matrices. The local quotient coordinate of Theorem 4.1 can be represented by positive-definite symmetric matrices. For a positive-definite matrix \(Q\), Gram–Schmidt applied with inner product \(v^TQw\) depends smoothly on \(Q\): each step uses addition, multiplication and division by a positive square root. The resulting orthonormal matrix is a local section of the quotient map. This is the local ingredient in reducing a frame bundle using a metric.

For \(G=\mathbb R_{>0}\) under multiplication, Lemma 2.2 reads \(g'=b(t)g\). Its solution is

\[
g(t)=g(a)\exp\left(\int_a^t b(s)\,ds\right).
\]

It exists on every compact interval on which \(b\) is continuous, although the group is noncompact. The finite-interval conclusion comes from invariance, not from a general assertion that arbitrary smooth vector fields are complete.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Solve \(x'=x^2\), \(x(0)=1\), and compare it with Lemma 2.2.

**Solution.** Separation gives \(x(t)=1/(1-t)\), with maximal interval \((-\infty,1)\). The vector field is not translation-invariant on the additive group \(\mathbb R\). Its blow-up does not contradict the invariant-equation lemma.

**Exercise 6.2 (medium).** Prove that a smooth section of a vector bundle given on a neighbourhood of a closed set extends to a global section which agrees on a smaller neighbourhood.

**Solution.** Let the section be \(s\) on \(U\), and choose \(\chi\) from Theorem 3.1. Define \(\chi s\) on \(U\) and zero outside \(U\). At a point outside \(U\), an open neighbourhood misses \(\operatorname{supp}\chi\), so the extension is identically zero there. It is therefore smooth, and equals \(s\) wherever \(\chi=1\).

**Exercise 6.3 (medium).** Show directly that \(\mathbb R/\mathbb Z\) has smooth local sections.

**Solution.** Any interval of length less than one maps injectively to the quotient. Around a chosen coset select such an interval centred at one representative. The quotient map is open; its restriction is a homeomorphism onto its image, and changes between these inverses are translations by integers. This defines smooth quotient charts and sections.

**Exercise 6.4 (hard).** Explain why closedness cannot be dropped from the Hausdorff conclusion of Theorem 4.1. Use the image \(H\) of \(t\mapsto(e^{it},e^{i\alpha t})\) in \(\mathbb T^2\), with irrational \(\alpha\).

**Solution.** The image is not closed. One can see its density by first fixing the first coordinate: replacing \(t\) by \(t+2\pi k\) gives the second coordinates \(e^{i\alpha t}e^{2\pi i\alpha k}\). Irrational rotations are dense on the circle. Indeed, pigeonholing \(N+1\) multiples of \(\alpha\) into \(N\) equal intervals gives a nonzero multiple whose distance to an integer is less than \(1/N\); its successive multiples approximate any point of the circle to this accuracy. Letting \(N\) grow proves density. Therefore every nonempty open saturated subset of \(\mathbb T^2\) is all of \(\mathbb T^2\): its complement, if nonempty and invariant under dense translations, is closed and would contain the entire torus. The quotient has more than one point, since this one-parameter image is not the torus (a fibre of the first coordinate contains only countably many points of the image), but it cannot separate those points. Also this \(H\), with its immersed one-dimensional topology, is not an embedded subgroup; the slice proof explicitly required embeddedness.


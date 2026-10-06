# Flat connections and infinitesimal holonomy

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text dedicated to the public domain under CC0 1.0.*

A flat connection has no local curvature, yet transport around a topologically nontrivial loop may still change a frame. Its remaining information is a representation of the fundamental group. At the other extreme, a curved connection has infinitesimal data at every point. For smooth connections these data can miss curvature arbitrarily nearby. For analytic connections, derivatives at one point determine the entire holonomy Lie algebra.

Take first Reduction and the holonomy theorem, especially its flatness criterion and its full proof of Ambrose–Singer. We use the smooth-family subgroup lemma in [Curvature and holonomy groups](curvature-and-holonomy-groups.md) and the inverse, exponential and ODE proofs in [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md). The definition of the fundamental group uses continuous homotopies with endpoints fixed. Section 2 constructs the universal cover needed here. Section 5 proves the analytic ODE fact rather than assuming smooth solutions are analytic. A basic reference is [Ambrose–Singer].

The base \(M\) is connected, finite dimensional, Hausdorff and second countable. We keep the right principal action. Loop concatenation \(\gamma*\delta\) travels first along \(\gamma\), then along \(\delta\), and \(h_{\gamma*\delta}=h_\delta h_\gamma\).

## 1. What remains when curvature vanishes

Call a principal connection **flat** when its curvature is zero. The preceding lesson proves that this is equivalent both to trivial restricted holonomy and to local parallel sections with zero potential.

If two paths \(\lambda,\mu\) have the same endpoints and are homotopic relative to those endpoints, their transports agree for a flat connection. Indeed, the loop formed by one path and the reverse of the other is nullhomotopic, so its transport is the identity. This argument applies to arbitrary finitely piecewise \(C^1\) representatives; it does not require a smooth homotopy.

Fix \(p\in P_x\). Define the **monodromy representation**

\[
\rho:\pi_1(M,x)\longrightarrow G,\qquad
\rho([\gamma])=h_\gamma^{-1}.
\]

Homotopy invariance makes it well defined. The inverse compensates for the reversed holonomy multiplication:

\[
\rho([\gamma][\delta])
=(h_\delta h_\gamma)^{-1}
=\rho([\gamma])\rho([\delta]).
\]

Its image is the full holonomy group as a set, because a subgroup contains the inverses of all its elements. Its abstract source is discrete; its image need not be a closed subgroup of \(G\). Changing the initial frame to \(pb\) replaces \(\rho\) by \(b^{-1}\rho b\).

**Proposition 1.1 (flatness on a simply connected base).** A flat principal bundle with connection over a simply connected base is isomorphic, with its connection, to \(M\times G\) with horizontal spaces tangent to the first factor.

**Proof.** Transport \(p\) to \(y\) along any path and call the endpoint \(s(y)\). Every two such paths are homotopic relative to their endpoints: their difference loop contracts, and a contraction gives the path homotopy. Hence \(s\) is well defined. Radial coordinate paths show it is smooth. Adjoining any path from \(y\) proves the section is parallel. The section-trivialization theorem gives \(P\cong M\times G\), and parallelness makes the potential zero. The resulting product connection has precisely the stated horizontal spaces. □

This is a statement about a bundle **with its connection**. It is stronger than triviality of the underlying bundle. A trivial bundle can support many inequivalent flat connections on a nonsimply connected base.

## 2. A cover and the classification by representations

We first supply the covering-space construction. It also fixes the action convention in the classification.

**Lemma 2.1 (universal cover of a manifold).** A connected manifold \(M\) has a connected simply connected smooth covering \(\widetilde M\to M\). Its points can be taken to be endpoint-preserving homotopy classes \([\lambda]\) of paths starting at \(x\). The fundamental group acts freely by deck transformations

\[
a\cdot[\lambda]=[a*\lambda],
\]

and acts transitively on every fibre. The cover is Hausdorff and second countable.

**Proof.** Send \([\lambda]\) to its endpoint. For a simply connected coordinate ball \(U\) containing that endpoint, extend \(\lambda\) by paths in \(U\). Two extensions to the same new endpoint give the same class, since their difference loop lies in \(U\). These classes define a sheet over \(U\), in bijection with \(U\). Two sheets over a ball are either disjoint or identical: a common class identifies their paths, and extensions inside the ball then identify every point of the sheets. Overlap maps between sheets are the identity on the underlying open subsets of \(M\). These charts give the covering topology and its smooth structure, with projection a local diffeomorphism.

Different base endpoints can be separated in \(M\). Different classes in one fibre lie in disjoint sheets over a sufficiently small ball. Thus the cover is Hausdorff. Every class is reached from the constant class by lifting its representative, so it is path connected.

Here are the lifting details. Subdivide a path into finitely many pieces lying in evenly covered balls, then successively use the inverse of projection on the sheet containing the preceding endpoint. This gives a unique lift. For a homotopy on a square, subdivide finely enough that the image of each small rectangle lies in an evenly covered ball. Given the lift along the lower and one side boundary, select the sheet at one vertex of the first rectangle and lift its whole image by that sheet's inverse projection. Adjacent rectangles agree on their shared edge by uniqueness of path lifting. Induction over rows constructs the full continuous lift. The same argument with fixed outer sides proves endpoint-preserving homotopy lifting.

For a loop in \(\widetilde M\) based at the constant class, its projected path \(\gamma\) has lifted endpoint \([\gamma]\): this follows directly by extending the successive representative paths in the sheet construction. If the lift closes, \([\gamma]\) is the constant class, so \(\gamma\) contracts in \(M\). Lift that based contraction. The fixed outer sides remain fixed by uniqueness, giving a contraction of the original loop in \(\widetilde M\). Moving the base point by a path handles loops based elsewhere. Thus \(\widetilde M\) is simply connected.

Prepending a loop preserves the sheets and their coordinates, so the displayed action is smooth and covers the identity. It is an action because prepending \(b\), then \(a\), prepends \(a*b\). It is free: if \(a*\lambda\) is homotopic to \(\lambda\), append the reverse of \(\lambda\) to obtain that \(a\) is nullhomotopic. It is transitive on a fibre: for two paths \(\lambda,\mu\) to the same endpoint, the loop \(\mu*\lambda^{-1}\) carries \([\lambda]\) to \([\mu]\). Any deck transformation is determined by its value at one point, since path lifting determines its value everywhere, so these are all deck transformations.

Finally, the preceding holonomy lesson proved \(\pi_1(M,x)\) countable. Take a countable cover of \(M\) by coordinate balls, each with a countable basis. There are at most countably many sheets over each ball, since its fibre is in bijection with \(\pi_1\). Their lifted bases give a countable basis of \(\widetilde M\). □

The paths in this lemma can be chosen piecewise smooth: the coordinate-segment replacement in the preceding fundamental-group proof produces such a representative of every continuous homotopy class.

**Theorem 2.2 (classification of flat principal bundles).** Isomorphism classes of smooth principal \(G\)-bundles with flat connection over \(M\), where isomorphisms cover the identity and preserve the connection, correspond bijectively to conjugacy classes of homomorphisms \(\pi_1(M,x)\to G\).

**Proof.** Given \(\rho\), form

\[
P_\rho=(\widetilde M\times G)/\pi_1(M,x),
\qquad
a\cdot(u,g)=(a\cdot u,\rho(a)g).
\]

This action commutes with the right \(G\)-action. In a sheet over a coordinate ball, every equivalence class has a unique representative with first coordinate in that sheet. Thus its quotient is locally \(U\times G\). On an overlap, two sheets differ by a locally constant deck element; the corresponding group-coordinate change is left multiplication by a constant element of \(G\). These product charts prove directly that the quotient is a smooth Hausdorff second-countable principal bundle. For separation, use disjoint base neighbourhoods when endpoints differ and ordinary separation in one product chart otherwise. Countable sheet and group bases give second countability.

The product horizontal distribution on \(\widetilde M\times G\) descends, since all these coordinate changes are constant in the base. Its local potentials are zero, so the connection is flat. Let \(u_0\) be the constant path class. A loop representing \(a\) lifts from \(u_0\) to \(a\cdot u_0\), and horizontal transport keeps the group coordinate equal to \(e\). In the quotient,

\[
[a\cdot u_0,e]=[u_0,\rho(a)^{-1}],
\]

so its monodromy representation is exactly \(\rho\).

Conversely, for a flat bundle choose \(p\), form its representation \(\rho\), and define

\[
\Psi([\lambda],g)=T_\lambda(p)\,g.
\]

Homotopy invariance makes this independent of the representative. The radial charts prove smoothness. If \(a\) is a based loop, then

\[
T_{a*\lambda}(p)=T_\lambda(p)\rho(a)^{-1},
\]

so \(\Psi(a\cdot u,\rho(a)g)=\Psi(u,g)\). It descends to a bundle map \(P_\rho\to P\). In every sheet chart it is a product trivialization using the parallel section obtained by transport, hence a smooth bundle isomorphism preserving the connection.

If \(\rho'=b^{-1}\rho b\), the map \([u,g]\mapsto[u,b^{-1}g]\) from \(P_\rho\) to \(P_{\rho'}\) is well defined: \(b^{-1}\rho(a)=\rho'(a)b^{-1}\). It preserves the product horizontal spaces. Conversely, a connection-preserving isomorphism intertwines transport. Comparing its chosen initial frame with the other initial frame gives exactly this conjugacy. This proves both directions and the bijection. □

On one **fixed** underlying bundle, only those representations whose constructed bundle is isomorphic to it occur. The theorem classifies bundles together with connections; it does not assert that every representation is realized on every prescribed bundle.

For any subgroup \(L\leq\pi_1(M,x)\), the quotient \(L\backslash\widetilde M\) is a covering, by the same sheet construction. Its fundamental group identifies with \(L\): a projected loop lifts closed precisely when its class lies in \(L\); homotopy lifting proves injectivity of the induced fundamental-group map. The pullback of \(P_\rho\) therefore has monodromy \(\rho|_L\). In particular, the cover associated to \(\ker\rho\) trivializes the connection. For a subgroup \(N\) of the full holonomy group, take \(L=\rho^{-1}(N)\); its pulled-back holonomy is exactly \(N\). If \(N\) is normal, the covering deck group is \(\pi_1/L\cong\operatorname{im}(\rho)/N\): normality makes left multiplication descend to its sheets, and the transitive fibre action identifies every deck transformation.

## 3. Curvature derivatives at one frame

Choose coordinates \(x^1,\ldots,x^n\) near \(x\). Let \(H_i\) be the horizontal lift of \(\partial_i\), and write

\[
C_{ij}=\Omega(H_i,H_j):P|_U\longrightarrow\mathfrak g.
\]

Define the **infinitesimal holonomy algebra** at \(p\) to be the linear span

\[
J(p)=\operatorname{span}_{\mathbb R}
\{(H_{i_r}\cdots H_{i_1}C_{ij})(p):r\geq0\}.
\tag{3.1}
\]

It is finite dimensional, since it lies in \(\mathfrak g\). No bound on derivative order is asserted uniformly over the base.

**Proposition 3.1.** The space \(J(p)\) is independent of the chosen coordinates, is a Lie subalgebra, and satisfies

\[
J(p)\subset\operatorname{Lie}(\operatorname{Hol}_p(U))
\]

for every sufficiently small coordinate neighbourhood \(U\) of \(x\). Also \(J(pa)=\operatorname{Ad}(a^{-1})J(p)\).

**Proof.** Every horizontal field is a linear combination of the \(H_i\), with smooth coefficient functions on \(P|_U\). Curvature on two such fields is a linear combination of the \(C_{ij}\). Applying further horizontal derivatives and expanding by the ordinary product rule gives a linear combination of the functions in (3.1), with smooth scalar coefficients. Thus the span is unchanged if its definition allows all smooth horizontal fields and all horizontal curvature arguments. This intrinsic description proves coordinate independence.

The fields \(H_i\) are right invariant, so every function in (3.1) is equivariant with adjoint type. Differentiation in a fundamental vertical direction therefore gives

\[
\xi^\# f=-[\xi,f].
\]

The commuting coordinate fields downstairs and the horizontal-bracket formula upstairs give

\[
[H_i,H_j]=-C_{ij}^{\#},
\]

where the right side uses the pointwise, possibly varying, Lie algebra value \(C_{ij}\). Acting on any equivariant derivative function \(f\), we obtain the identity

\[
[C_{ij},f]=H_iH_jf-H_jH_if.
\tag{3.2}
\]

It holds as a function, so further horizontal differentiation is permitted.

We prove by induction on \(r\) that the bracket of an order-\(r\) derivative function of \(C_{ij}\) with any derivative function \(f\) is a finite linear combination of derivative functions. The case \(r=0\) is (3.2). If \(a=H_k a_0\), the product rule gives

\[
[a,f]=H_k[a_0,f]-[a_0,H_kf].
\]

By induction, the bracket in the first term is already a linear combination of derivative functions; its derivative remains such a combination. The second bracket has the same property by induction, since \(H_kf\) is another derivative function. This proves the assertion for every \(r\). Evaluating at \(p\) proves \([J(p),J(p)]\subset J(p)\).

For inclusion in the local holonomy algebra, use the holonomy reduction for the connection restricted to \(U\). At each locally reachable frame its curvature lies in that algebra. Flowing a horizontal field a short time stays among locally reachable frames. A derivative of a function with values in a fixed finite-dimensional linear subspace remains in the subspace, by taking difference quotients. Induction therefore puts every derivative in (3.1) at \(p\) in the local holonomy algebra. Finally, right invariance of the fields and curvature equivariance give the displayed frame-change formula for every derivative function and hence for their span. □

For clarity, the pointwise notation in (3.2) does not differentiate \(C_{ij}\) as a coefficient of the vertical vector field: applying that field to \(f\) evaluates the directional derivative at its current Lie algebra value. Derivatives of coefficients occur only when subsequently differentiating the identity.

**Lemma 3.2 (a subalgebra gives a connected immersed group).** A Lie subalgebra \(\mathfrak k\subset\mathfrak g\) is the Lie algebra of the connected immersed subgroup generated by \(\exp(tX)\), \(X\in\mathfrak k\). Two connected immersed subgroups with the same Lie algebra coincide, with the same Lie-group topology.

**Proof.** First, \(\operatorname{Ad}(\exp(tX))Y\) solves \(Z'=[X,Z]\). To check the initial derivative, the flow of the left invariant field \(X^L\) is \(g\mapsto g\exp(tX)\). Pulling \(Y^L\) back by this flow gives at the identity \(\operatorname{Ad}(\exp(tX))Y\). In coordinates, differentiating the pullback gives \(DY\,X-DX\,Y=[X^L,Y^L]\). The group law then gives the same derivative at every \(t\). Since \(\mathfrak k\) is bracket closed, this linear equation keeps \(Z\) in \(\mathfrak k\), by uniqueness of its coordinate ODE.

Apply the smoothly generated subgroup lemma to all these exponential curves. Differentiating any product of them gives, after left translation, a sum of adjoint translates of their \(X\)'s. These lie in \(\mathfrak k\), so the maximal rank is at most \(\dim\mathfrak k\). A product using a basis of \(\mathfrak k\) has rank \(\dim\mathfrak k\) at its zero parameter. Thus the constructed subgroup has exactly that Lie algebra. For uniqueness, the exponential maps of any two such groups agree in \(G\) by uniqueness of the invariant ODE. Exponential neighbourhoods therefore give the same identity neighbourhood with the same smooth coordinates. A connected group is generated by any identity neighbourhood, since the subgroup it generates is open and all its cosets are open. Both groups and their translated charts consequently agree. □

Call the group associated to \(J(p)\) the **infinitesimal holonomy group**. Proposition 3.1 and the exponential construction put it inside every sufficiently local holonomy group, and inside restricted holonomy.

Smoothness alone does not make these groups equal. On the product \(U(1)\)-bundle over \(\mathbb R^2\), put

\[
A=if(x)\,dy,\qquad
f(x)=
\begin{cases}
e^{-1/x^2},&x>0,\\
0,&x\leq0.
\end{cases}
\]

Every derivative of \(f\) at zero vanishes. Indeed, on \(x>0\) its derivatives are polynomials in \(1/x\) times \(e^{-1/x^2}\). For every \(N\), \(x^{-N}e^{-1/x^2}\to0\): put \(u=x^{-2}\) and use \(e^u\geq u^k/k!\) with \(k>N/2\). Extending each derivative by zero proves smoothness inductively, including its derivative at zero by the same estimate with one extra power of \(1/x\).

Curvature is \(if'(x)\,dx\wedge dy\). All its horizontal derivatives at a frame over the origin vanish, so \(J(p)=0\). Nevertheless, every neighbourhood of the origin contains points with \(f'(x)>0\). Ambrose–Singer on any coordinate ball about the origin gives holonomy \(U(1)\), because one nonzero curvature value spans \(i\mathbb R\). Thus even all infinitesimal derivatives at one point can miss the local holonomy of a smooth connection.

## 4. Local groups and constant dimension

For a coordinate ball \(U\) about \(x\), let \(H_U(p)\) be the holonomy group of the restricted connection on \(P|_U\). It is connected because \(U\) is simply connected. Define

\[
H^{\mathrm{loc}}_p=\bigcap_{U\ni x}H_U(p),
\]

using coordinate balls centred at \(x\). Using all connected open neighbourhoods gives the same intersection, since coordinate balls form a neighbourhood basis.

**Proposition 4.1 (stabilization).** Some ball \(U_0\) satisfies \(H_U(p)=H^{\mathrm{loc}}_p=H_{U_0}(p)\) for every coordinate ball \(U\subset U_0\) about \(x\). Consequently local holonomy is a connected immersed Lie subgroup. Its Lie algebra contains \(J(p)\).

**Proof.** Among the nonnegative integers \(\dim H_U(p)\), choose a minimum, attained at \(U_0\). For \(U\subset U_0\), the inclusion \(H_U(p)\to H_{U_0}(p)\) is a smooth homomorphism: its product charts are formed from smooth loop families, which are also such families for the larger ball. Minimality makes its dimension equal to that of the larger group. The inverse function theorem makes its image open; the larger group is connected, so the image is the whole group. For any other neighbourhood \(V\) of \(x\), choose a ball inside \(U_0\cap V\). Its group equals \(H_{U_0}(p)\) and is contained in the group for \(V\). Hence the intersection is exactly this stabilized group. Proposition 3.1 puts \(J(p)\) in its Lie algebra. □

There are two different semicontinuity statements. The function \(\dim J(p)\), considered on the base, is **lower semicontinuous**: any finite independent list of derivative functions remains independent in a nearby section, because an appropriate matrix minor remains nonzero. By equivariance, its dimension is independent of the frame in a fibre. Thus the set where this dimension is at least any given integer is open.

The dimension of local holonomy is **upper semicontinuous**. To see this, take a stabilizing ball \(U_0\) at \(p\). For \(y\in U_0\), choose a frame \(q\) obtained by transport from \(p\) inside \(U_0\). Holonomy of the whole restricted connection at \(q\) equals \(H_{U_0}(p)\), by adjoining the outgoing path and its reverse. Local holonomy at \(q\) is contained in that group, so its dimension is no larger. All other frames over \(y\) are conjugate. Thus the set where the local dimension is at most any given integer is open.

**Theorem 4.2 (local groups generate restricted holonomy).** Restricted holonomy is generated by the groups \(H^{\mathrm{loc}}_q\) at all frames \(q\) reachable horizontally from \(p\). Its Lie algebra is the linear span of their Lie algebras.

**Proof.** Every local group is contained in \(\operatorname{Hol}_p^0\): transport to \(q\), take a loop in a small ball, and return; that based lasso is nullhomotopic. Let \(S\) be the span of the local Lie algebras. The curvature at each reachable \(q\) lies in its local Lie algebra, by the reduction for a stabilizing ball. Ambrose–Singer therefore gives \(\mathfrak h\subset S\). The reverse inclusion holds by subgroup inclusion, so \(S=\mathfrak h\).

Generate a group \(K\) by the local groups, or equivalently by their identity-chart families. The smooth-family lemma applied inside \(\operatorname{Hol}_p^0\) constructs a connected immersed Lie subgroup. Its Lie algebra contains every local Lie algebra and therefore all of \(\mathfrak h\). Equal dimensions make its inclusion open; connectedness of \(\operatorname{Hol}_p^0\) gives \(K=\operatorname{Hol}_p^0\). □

**Theorem 4.3 (constant infinitesimal dimension).** If \(\dim J\) is constant near \(x\), infinitesimal and local holonomy agree at frames over a sufficiently small neighbourhood of \(x\). If \(\dim J\) is constant on the connected base, infinitesimal, local and restricted holonomy all agree at each frame.

**Proof.** Choose finitely many derivative functions \(f_1,\ldots,f_r\) whose values form a basis of \(J(p)\). They remain independent along a nearby local section. Constant dimension makes them a basis of \(J\) there, and their adjoint equivariance makes them a basis over the entire restricted bundle on that small neighbourhood. All horizontal derivatives \(H_if_\alpha\) belong to \(J\), by its definition. Expressing them in this basis gives smooth coefficients: choose an invertible matrix minor locally and solve by its inverse. Uniqueness of the coefficients and equivariance show they are unchanged by right translation.

Along a horizontal \(C^1\) curve \(q(t)\) in this neighbourhood, the basis vectors \(v_\alpha(t)=f_\alpha(q(t))\) satisfy a linear system

\[
v_\alpha'(t)=\sum_\beta A_{\alpha\beta}(t)v_\beta(t)
\]

with continuous coefficients. The linear systems used below exist across the compact time interval: the integral equation and the exponential estimate bound each matrix norm by its initial norm times \(e^{\int\|A\|}\), and the compact-graph continuation criterion extends the solution. The fundamental matrix is invertible: solve \(B'=-BA\) with \(B(0)=I\); differentiating \(BC\), where \(C'=AC\), gives \(BC=I\). The reversed product follows by finite-dimensional injectivity. Thus each \(v_\alpha(t)\) is an invertible linear recombination of the initial basis. The subspace \(J(q(t))\subset\mathfrak g\) is constant along the curve.

Choose a small ball \(U\) where this basis exists. Every locally reachable frame has the same \(J\)-subspace as \(p\), and its curvature belongs to that subspace. Ambrose–Singer for \(U\) gives \(\operatorname{Lie}(H_U(p))\subset J(p)\). Proposition 3.1 gives the reverse inclusion. The infinitesimal group and \(H_U(p)\) are connected groups with the same algebra, hence coincide by Lemma 3.2. This works at every point after shrinking the neighbourhood, proving the local conclusion.

If the dimension is constant everywhere, cover any horizontal path by finitely many of these neighbourhoods. The constant-subspace conclusion propagates through the successive pieces, so \(J(q)=J(p)\) at every reachable frame. Ambrose–Singer on the whole base now gives \(\mathfrak h=J(p)\), and Lemma 3.2 identifies the connected groups. The stabilized local group lies between infinitesimal and restricted holonomy, so it too agrees. □

Two useful consequences are worth making precise. If \(J(p)\) already equals the local holonomy algebra at one frame, the opposing semicontinuity inequalities and \(J\subset\mathfrak h^{\mathrm{loc}}\) force both dimensions to be constant and equal in a neighbourhood. Theorem 4.3 then makes their groups agree there, and their subspaces agree along local horizontal paths.

If instead local holonomy dimension is constant on the whole base, local holonomy alone equals restricted holonomy. In a stabilizing ball, the local groups at horizontally reachable nearby frames are subgroups of the initial local group with equal dimension, hence equal. A finite chain along any horizontal path propagates this equality. Theorem 4.2 then identifies the generated restricted group with this one local group. Neither consequence requires analyticity.

## 5. Why analyticity changes the answer

A real analytic function is locally represented by an absolutely convergent real power series. We assume here that the base, group, principal-bundle charts and connection are real analytic. This makes the horizontal lifts of analytic coordinate fields and all the functions in (3.1) analytic. We need an analytic version of the local ODE theorem.

**Lemma 5.1 (analytic solutions).** The solution of a finite-dimensional real analytic ODE is real analytic in time wherever it is defined.

**Proof.** Work near an initial point and translate time and initial value to zero. Write \(y'=F(t,y)\), \(y(0)=0\), with \(y\in\mathbb R^d\). Absolute convergence of the coefficient series on a sufficiently small polydisc supplies numbers \(R,C>0\) such that every coefficient \(c_{m,\alpha}\) of every component obeys

\[
|c_{m,\alpha}|\leq C R^{-m-|\alpha|}.
\]

For example, take a polydisc on which the sum of the absolute weighted coefficients is finite and choose \(C\) at least that sum. The formal solution coefficients are uniquely determined recursively: the coefficient of \(t^k\) on the right determines \((k+1)y_{k+1}\), using only \(y_1,\ldots,y_k\), since \(y(0)=0\).

Majorize each component by the scalar formal solution

\[
v'=\frac{C}{(1-t/R)(1-v/R)^d},
\qquad v(0)=0.
\]

The right side has nonnegative coefficients and bounds the sum obtained by substituting componentwise absolute values into the series for \(F\). Induction in the coefficient recursion therefore gives \(|(y_k)_i|\leq v_k\) for every component. The scalar solution is explicitly

\[
\begin{aligned}
B(t)&=1+(d+1)C\log(1-t/R),\\
v(t)&=R\bigl(1-B(t)^{1/(d+1)}\bigr).
\end{aligned}
\]

Differentiate to check its ODE and initial value. The logarithm and binomial series converge near zero, so this is an analytic function there; its coefficients are the unique nonnegative formal coefficients just defined. Thus the component series for \(y\) converge absolutely on a smaller interval. Termwise differentiation and substitution are justified on still smaller closed intervals by absolute convergence of power series; the sums solve the ODE. Smooth uniqueness identifies them with its existing solution. Repeating around any point of a solution proves analyticity throughout its domain. Analytic coordinate changes transfer the assertion to manifolds. □

We also need only the following elementary identity principle. If an analytic scalar function on a connected interval vanishes on an open subinterval, it vanishes everywhere. Let \(Z\) be the set of points where every derivative vanishes. It is closed by continuity of all derivatives and open because the convergent Taylor series vanishes near each point of \(Z\). It is nonempty and the interval is connected, so \(Z\) is the whole interval. Applying this to linear functionals that annihilate a fixed subspace gives the same assertion for an analytic vector-valued function taking values in that subspace.

**Theorem 5.2 (analytic infinitesimal holonomy theorem).** For a real analytic connection on a real analytic principal bundle over a connected base,

\[
J(p)=\operatorname{Lie}(\operatorname{Hol}_p),
\qquad
H^{\mathrm{inf}}_p=H^{\mathrm{loc}}_p=\operatorname{Hol}_p^0.
\]

**Proof.** Consider a straight coordinate path, contained in one analytic chart, and its horizontal lift \(q(t)\). It is the integral curve of \(X=\sum a^iH_i\) with constant real coefficients \(a^i\). The field is analytic, so Lemma 5.1 makes \(q(t)\) analytic locally at every time.

For any derivative function \(f=H_{i_r}\cdots H_{i_1}C_{ij}\), the function \(f(q(t))\) is analytic. Its \(k\)-th time derivative at the initial time is \(X^k f(q(0))\), a linear combination of further functions in (3.1). Every one of these derivatives belongs to \(J(q(0))\). Its convergent Taylor series therefore lies in that fixed finite-dimensional subspace near the initial time. The identity principle extends this conclusion over the whole path interval. This is done for each \(f\) separately; a uniform convergence radius over all derivative orders is unnecessary. Hence

\[
J(q(t))\subset J(q(0)).
\]

Apply the same argument to the reversed coordinate path to obtain the reverse inclusion. Thus the two subspaces agree along every such segment.

Any two base points can be joined by finitely many straight analytic coordinate segments: the set reachable by such segments is open, and so are the other reachability classes; connectedness leaves one class. The equality propagates through those segments and coordinate changes. Every frame over the terminal point differs from the transported frame by a group element; adjoint equivariance preserves the dimension of \(J\). Consequently \(\dim J\) is constant on the whole base. The global conclusion of Theorem 4.3 proves the asserted group and algebra equalities. □

The smooth example in Section 3 violates the conclusion precisely because its zero Taylor series does not determine nearby values. Analyticity supplies that determination and then propagates it along the connected base. The theorem concerns the holonomy **Lie algebra** and restricted group; it does not eliminate the discrete monodromy part of full holonomy.

## 6. Examples of flat monodromy

Over \(S^1\), the fundamental group is \(\mathbb Z\). Lifting angles shows that a loop class is its integer angle increment; a zero-increment lift contracts linearly on \(\mathbb R\). Thus a flat principal \(G\)-bundle with connection is determined by a conjugacy class of one element of \(G\).

This includes disconnected groups. For \(G=\{1,-1\}\), the nontrivial monodromy gives the connected double cover of the circle as a principal \(G\)-bundle. Its vertical tangent is zero, so every tangent is horizontal and curvature is zero. Its underlying principal bundle is nontrivial: a global section would give a product with two connected components. Flatness alone therefore does not imply a trivial bundle over the circle.

For the two-torus, angle lifting gives \(\pi_1(\mathbb T^2)=\mathbb Z^2\): the two increments determine the class, and zero-increment lifts contract in \(\mathbb R^2\). Representations correspond to pairs of commuting elements of \(G\), up to simultaneous conjugacy.

For \(G=U(1)\), every pair commutes. On the trivial bundle take

\[
A=i\alpha\,d\theta+i\beta\,d\psi.
\]

Its representation sends \((m,n)\) to

\[
e^{2\pi i(\alpha m+\beta n)}.
\]

Every representation occurs by choosing real arguments of its two values. The classification therefore shows that every flat principal \(U(1)\)-bundle over the two-torus is trivial as a bundle, although its connection need not have trivial monodromy. Changing \((\alpha,\beta)\) by an integer pair is the gauge change \(g=e^{i(k\theta+\ell\psi)}\), since \(A'=A+g^{-1}dg\). Conversely, equivalent connections have the same representation, so their parameters differ by integers. Their moduli set is \((\mathbb R/\mathbb Z)^2\).

## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** A flat connection has monodromy \(\rho\). Describe its holonomy after pullback to the universal cover and to the cover associated to \(\rho^{-1}(N)\), for a subgroup \(N\leq\operatorname{im}\rho\).

**Solution.** The universal cover is simply connected, so the pullback has trivial full holonomy and a global parallel trivialization. For the second cover, the image of its fundamental group is \(\rho^{-1}(N)\). The pullback representation is the restriction, whose image is \(N\). Holonomy is this subgroup, since taking inverses does not change the underlying subgroup. Normality is unnecessary for this conclusion; it is needed only to describe the cover by a quotient deck group.

**Exercise 7.2 (medium).** Classify flat principal \(U(1)\)-bundles with connection over the two-torus, and distinguish the monodromy representation from the transport multiplier.

**Solution.** A representation is specified by arbitrary \(u,v\in U(1)\), and conjugacy has no effect. Choose \(u=e^{2\pi i\alpha}\), \(v=e^{2\pi i\beta}\). The connection \(A=i\alpha d\theta+i\beta d\psi\) has this representation, while its transport multiplier for class \((m,n)\) is \(u^{-m}v^{-n}\). Integer changes of parameters are gauge equivalent and are the only equivalences. Thus the moduli set is \(U(1)^2\), or equivalently \((\mathbb R/\mathbb Z)^2\), and all the underlying bundles are trivial by the classification theorem.

**Exercise 7.3 (medium).** For \(A=ix^3\,dy\) on the product circle bundle over \(\mathbb R^2\), determine curvature, infinitesimal holonomy at the origin, and restricted holonomy. At which derivative order is curvature first detected there?

**Solution.** \(F=3ix^2\,dx\wedge dy\). Since the coefficient is a function on the base and the group is abelian, its horizontal derivatives are its ordinary base derivatives. At the origin both its value and first derivatives vanish, but \(\partial_x^2(3ix^2)=6i\). Hence \(J(p)=i\mathbb R\), and infinitesimal holonomy is \(U(1)\). The analytic theorem gives the same restricted group, also confirmed by Ambrose–Singer at points with \(x\ne0\). Detection requires second derivatives of curvature, or third derivatives of the potential.

**Exercise 7.4 (hard).** Explain why equality of infinitesimal and local holonomy at one point persists in a neighbourhood, yet does not by itself force equality with global restricted holonomy.

**Solution.** Let their common Lie-algebra dimension at that point be \(r\). Lower semicontinuity of \(\dim J\) gives \(\dim J\geq r\) nearby; upper semicontinuity of local dimension gives \(\dim\mathfrak h^{\mathrm{loc}}\leq r\). The inclusion \(J\subset\mathfrak h^{\mathrm{loc}}\) forces both to equal \(r\), and Theorem 4.3 and Lemma 3.2 identify the groups there.

For a counterexample to the global conclusion, choose a nonzero smooth function \(\chi\) supported in \(1<x<2\), with \(\chi'\) nonzero somewhere, and take \(A=i\chi(x)\,dy\) on \(\mathbb R^2\). Near the origin the potential and curvature vanish identically, so both infinitesimal and local holonomy are trivial. At a point where \(\chi'\ne0\), curvature is nonzero and Ambrose–Singer gives global restricted holonomy \(U(1)\). The example is smooth and nonanalytic, consistent with Theorem 5.2.

## References

[Ambrose–Singer] Warren Ambrose and Isadore M. Singer, “A theorem on holonomy,” *Transactions of the American Mathematical Society* **75** (1953), 428–443, [publisher record](https://doi.org/10.1090/S0002-9947-1953-0063739-1).

# Linear and affine connections

A covariant derivative compares nearby vectors; an affine connection also records the motion of their origins. Construction uses only exact freely accessible material and earlier programme proofs.

## A. Covariant differentiation and the frame bundle

Let \(E\to M\) be a smooth vector bundle of finite rank \(r\) over \(\mathbb F=\mathbb R\) or \(\mathbb C\). The base manifold and all tangent directions are real. In the complex case, a smooth complex function is a pair of smooth real functions, and a real vector field differentiates its real and imaginary parts. A frame \(e=(e_1,\ldots,e_r)\) acts on a column \(v\in\mathbb F^r\) by \(ev=\sum e_jv^j\). Our change-of-frame convention is \(\widetilde e=eg\), so a section has coordinates \(s=ev=\widetilde e\,\widetilde v\) with \(\widetilde v=g^{-1}v\).

The free construction source is Peter W. Michor's [author manuscript, *Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §§19.10–19.12 and 22.11. We supply the converse frame correspondence and every local-to-global step explicitly. **Local**, **PB**, **Conn** and **Curv** refer respectively to the complete earlier programme lessons [Local tools](local-tools-for-bundles-and-transport.md), [Principal bundles](principal-bundles-and-associated-bundles.md), [Connections and parallel transport](connections-and-parallel-transport.md) and [Curvature and holonomy groups](curvature-and-holonomy-groups.md). The external manuscript supplies construction material, never a substitute for these proofs.

A **covariant derivative** is a map \((X,s)\mapsto\nabla_Xs\) from real smooth vector fields and smooth sections to smooth sections. It is additive in both entries, linear over real smooth functions in \(X\), linear over \(\mathbb F\)-constants in \(s\), and satisfies
\[
\nabla_X(fs)=X(f)s+f\nabla_Xs
\quad(f\in C^\infty(M,\mathbb F)).
\tag{A.1}
\]

**Lemma A.1 (locality and connection matrices).** These axioms determine a unique compatible covariant derivative on every open subset of \(M\). In a local frame there is a unique matrix-valued real one-form \(A\) such that
\[
\nabla_X(ev)=e\bigl(X(v)+A(X)v\bigr).
\tag{A.2}
\]
Its entries take values in \(\mathbb F\), and changing the frame to \(eg\) changes it to
\[
\widetilde A=g^{-1}Ag+g^{-1}dg.
\tag{A.3}
\]
Conversely, smooth local matrix one-forms obeying (A.3) define a unique covariant derivative. The value \((\nabla_Xs)(x)\) depends only on \(X(x)\) and the first derivative and value of the local coordinate column of \(s\) at \(x\).

**Proof.** First suppose that a global section \(s\) vanishes on a neighbourhood \(U\) of \(x\). By Local 3.1 choose a smooth real cutoff \(\chi\) supported in \(U\) and equal to one near \(x\). The section \(\chi s\) is zero everywhere, so (A.1) at \(x\) gives \((\nabla_Xs)(x)=0\); the term \(X(\chi)(x)\) vanishes. If instead a global vector field \(X\) vanishes near \(x\), then \(\chi X=0\), and linearity in the first entry gives the same conclusion. Taking differences proves locality in each entry.

For local fields and sections, multiply each by such a cutoff with support in its domain, and extend by zero. The extension is smooth: outside the closed support it vanishes on a neighbourhood, and inside the original domain it is a smooth product. Evaluate the global derivative at \(x\). Locality proves that the result is independent of the cutoff and extensions. Using one cutoff equal to one on a whole smaller neighbourhood proves smoothness of the resulting local section. These definitions agree on overlaps and retain the axioms, because the extensions can be chosen to agree on the neighbourhood where an identity is being checked. Uniqueness follows from the same locality argument. This also proves the restriction assertion.

Take real coordinates \(x^1,\ldots,x^n\) and a frame on one such neighbourhood. Define smooth coefficients by
\[
\nabla_{\partial_i}e_b=\sum_a e_a(A_i)^a{}_b,
\qquad A=\sum_i A_i\,dx^i.
\]
Linearity in \(X=\sum_i X^i\partial_i\) and the product rule in \(s=\sum_b v^be_b\) give (A.2) there. Hence \(A(X)\) depends only on the real tangent vector \(X(x)\), not on an extension. On overlapping coordinate charts this uniquely specified linear map has the ordinary one-form transformation rule, so it defines a matrix-valued one-form on the entire frame domain. Its smoothness follows from the displayed coefficients. This proves existence, uniqueness and the dependence on first derivatives.

Write \(s=eg\widetilde v\). The product rule for the matrix product, proved entrywise by Local 0.3, gives
\[
X(g\widetilde v)+A(X)g\widetilde v
=gX(\widetilde v)+\bigl(X(g)+A(X)g\bigr)\widetilde v.
\]
Multiplying by \(g^{-1}\) proves (A.3). Conversely this calculation shows that (A.2) gives the same section in two frames whenever their matrices obey (A.3). The local definitions therefore agree and produce a smooth global section. Additivity, the two linearities and (A.1) follow from the ordinary product rule in each frame. Local frames cover the base, so they also prove uniqueness. Rank zero has only the zero section and empty matrices; the argument and conclusions remain valid. □

**Theorem A.2 (the full frame correspondence).** Covariant derivatives on \(E\) correspond bijectively to principal connections on its full frame bundle \(\operatorname{Fr}_{\mathbb F}(E)\), with structure group \(\operatorname{GL}(r,\mathbb F)\). In the chart \((x,g)\mapsto e(x)g\), the principal form associated to (A.2) is
\[
\omega_{(x,g)}(v,\dot g)=g^{-1}A_x(v)g+g^{-1}\dot g.
\tag{A.4}
\]
Every such bundle admits a covariant derivative. If \(u(t)\) is a horizontal frame along a path, then \(u(t)c\) is the parallel vector with initial coordinate \(c\); all parallel vectors arise this way.

**Proof.** PB C.1 proves the real frame-bundle construction and its identification \([u,c]\mapsto u(c)\) with \(E\). Here is the needed complex extension. Identify a complex vector space with its underlying real space and let \(J\) be multiplication by \(i\). Complex linear maps are exactly the real matrices commuting with \(J\), a real linear subspace. Its invertible elements form an open subset of that subspace by Local 0.4. If an invertible real matrix commutes with \(J\), multiplying that equality on both sides by its inverse shows the inverse also commutes with \(J\). The smooth real inversion of Local 0.4 consequently restricts to smooth complex inversion. Thus \(\operatorname{GL}(r,\mathbb C)\) is a real Lie group with Lie algebra all complex matrices; its operations are matrix multiplication and inversion.

For a complex local frame, every other frame is uniquely \(e(x)g\). On overlaps these coordinates change by smooth left multiplication by the complex transition matrix. PB A.1 therefore constructs a principal bundle for this Lie group, just as in the real case. The map \([u,c]\mapsto u(c)\) is well defined under \([ug,c]=[u,gc]\), and its local expression is the original complex vector-bundle chart. It and its inverse are smooth and complex linear on fibres. This proves precisely the complex version of the facts from PB C.1 used below.

By A.1, a derivative determines potentials with (A.3). Conn A.3 proves that these are exactly the transition identities for a unique principal connection, with local form (A.4). Conversely a principal connection has such potentials, so A.1 defines a covariant derivative. Each construction recovers the same \(A\) in every local frame, proving that they are inverse. This also agrees with the induced derivative of Conn D.1, because the derivative of the standard matrix representation is the same matrix, making its formula \(dv+Av\).

Conn B.1 gives a smooth principal connection on the full frame bundle, proving existence. Conn C.1–C.2 give horizontal frame transport on every finite smooth or piecewise smooth path. In a frame chart write \(u(t)=e(\gamma(t))g(t)\). Equation (A.4) says that horizontality is
\[
g'(t)=-A_{\gamma(t)}(\gamma'(t))g(t).
\tag{A.5}
\]
Thus the column \(g(t)c\) satisfies \(v'+A(\gamma')v=0\). Conn D.2 proves existence and uniqueness for that equation, and identifies it with the induced vector transport. The evaluation is linear over \(\mathbb F\) and the transported frame stays invertible, so every initial vector and hence every parallel vector is obtained. For a general field along the path, write \(s(t)=u(t)c(t)\). The product rule and (A.5) give \(D_ts=u(t)c'(t)\); this is zero exactly when \(c\) is constant. At finitely many junctions use the endpoint values to pass to the next interval. Rank zero again has the unique empty frame and zero vector. □

**Theorem A.3 (differences of covariant derivatives).** The difference of two covariant derivatives is an element of \(\Omega^1(M,\operatorname{End}_{\mathbb F}E)\). Conversely, adding any such endomorphism-valued one-form to a covariant derivative gives another. Thus the nonempty set of derivatives is an affine space over that vector space.

**Proof.** Subtract the two local formulas (A.2). Their ordinary derivative terms cancel, leaving
\[
(\nabla'_X-\nabla_X)(ev)=e\bigl((A'-A)(X)v\bigr).
\tag{A.6}
\]
Subtracting (A.3) for the two potentials gives \(\widetilde A'-\widetilde A=g^{-1}(A'-A)g\). This is precisely the endomorphism change of coordinates from PB C.2: an operator acting on a column in the new frame is conjugated by \(g^{-1}\) on the left and \(g\) on the right. The complex case follows by the same basis computation, with complex entries. Hence (A.6) is the evaluation of a smooth real one-form with complex-linear endomorphism values when \(\mathbb F=\mathbb C\), or real-linear values when \(\mathbb F=\mathbb R\).

Conversely, an endomorphism-valued form has that conjugation law, so adding its matrices to \(A\) preserves (A.3). A.1 gives the new derivative. Equivalently its tensorial term is linear in the tangent and the section value, so the additional term preserves (A.1). Addition acts freely, because zero difference means equality, and transitively by the first assertion. Nonemptiness is A.2. These statements are exactly the asserted affine-space structure; no choice of a preferred derivative is implied. □

## B. Differentiation along maps and paths

Michor's free [author manuscript](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §§19.10–19.12 and 22.8–22.9, motivates the connector description. We use the sign convention \(\nabla=d+A\). The next proofs give its two linear structures, all coordinate changes and the chain rule explicitly. No immersion or submersion hypothesis is placed on a map along which a section is differentiated.

**Theorem B.1 (the connector and horizontal splitting).** Let \(\pi:E\to M\) carry a covariant derivative. There is a unique smooth map \(\mathcal K:TE\to E\), over the base \(M\), whose expression in a frame \(e\) is
\[
\mathcal K(x,y;v,z)=e(x)\bigl(z+A_x(v)y\bigr).
\tag{B.1}
\]
Here \((x,y)\) denotes \(e(x)y\in E\), while \((v,z)\) is its tangent coordinate. The bundle \(TE\) has two linear structures, over \(E\) by its tangent projection and over \(TM\) by \(d\pi\). The map \(\mathcal K\) is real linear on the first fibres and \(\mathbb F\)-linear on the second. For the vertical lift
\[
\operatorname{vl}(u,w)=\left.\frac d{dt}\right|_0(u+tw),
\qquad u,w\in E_x,
\tag{B.2}
\]
it satisfies \(\mathcal K(\operatorname{vl}(u,w))=w\). Conversely these linearity and vertical-normalization properties characterize the connectors of covariant derivatives.

Their kernels give smooth horizontal complements to \(\ker d\pi\). More explicitly,
\[
\begin{split}
H_{e(x)y}(v)&=(x,y;v,-A_x(v)y),\\
T_{e(x)y}E&=H_{e(x)y}(T_xM)\oplus V_{e(x)y}E,\\
(x,y;v,z)&=H_{e(x)y}(v)+\operatorname{vl}\bigl(e(x)y,\mathcal K(x,y;v,z)\bigr).
\end{split}
\tag{B.3}
\]
For every section \(s\), \(\nabla_Xs=\mathcal K\circ ds\circ X\).

**Proof.** Differentiate the frame-coordinate change \(\widetilde y=g(x)^{-1}y\). Local 0.3 gives
\[
\widetilde z=g^{-1}z-g^{-1}(dg(v))g^{-1}y.
\tag{B.4}
\]
Combining this with (A.3) yields
\(\widetilde z+\widetilde A(v)\widetilde y=g^{-1}(z+A(v)y)\).
The two vectors in (B.1) therefore agree after multiplication by their respective frames. Ordinary base-coordinate changes replace \(v\) by its Jacobian image and \(A\) by the corresponding one-form, which leaves the evaluation unchanged. Thus (B.1) defines a unique smooth global map.

The first linear structure of \(TE\) is the usual tangent vector space at fixed \((x,y)\): its fibre coordinates are \((v,z)\). Formula (B.1) is real linear in these. For the second, fix \((x,v)\in TM\); the fibre coordinates are \((y,z)\). The transition (B.4), together with \(\widetilde y=g^{-1}y\), is linear over \(\mathbb F\) in this pair. It is invertible by reversing the frame change, and the chain rule proves the cocycle identities. These are vector-bundle charts for \(d\pi:TE\to TM\). Formula (B.1) is \(\mathbb F\)-linear in \((y,z)\) at fixed \((x,v)\). The vertical lift has tangent coordinates \((0,w_e)\), where \(w=e(x)w_e\), so its connector is exactly \(w\). This also proves smoothness and the claimed normalization of (B.2).

Conversely, let a smooth map \(\mathcal K\) over \(M\) have the stated properties, and denote its frame-coordinate value by \(k(x,y;v,z)\). Real linearity in \((v,z)\), followed by the vertical normalization, gives
\[
k(x,y;v,z)=k(x,y;v,0)+z.
\]
Linearity in \((y,z)\) at fixed \((x,v)\) says that \(y\mapsto k(x,y;v,0)\) is \(\mathbb F\)-linear. Its dependence on \(v\) is real linear by the first property. Evaluating on fixed coordinate bases produces a smooth matrix-valued real one-form \(A_x(v)\) with \(k(x,y;v,0)=A_x(v)y\). Applying (B.4) to the global map \(\mathcal K\) forces (A.3), by comparing the coefficients of \(y\). A.1 reconstructs the derivative uniquely.

In (B.1), the equation \(\mathcal K=0\) is exactly \(z=-A_x(v)y\), so its solutions have the horizontal graph in (B.3). This graph is smooth and \(d\pi\) maps it isomorphically to \(T_xM\). The complementary vertical vectors are exactly those with \(v=0\), and subtracting the horizontal vector gives the last formula in (B.3). These intrinsic descriptions are independent of coordinates because \(\mathcal K\), \(d\pi\) and the vertical lift are. Finally a section has tangent coordinates \((v,d y(v))\); inserting them into (B.1) gives (A.2), proving the derivative identity. This proves both constructions and all asserted properties, also in rank zero. □

**Theorem B.2 (pullback derivatives and the chain rule).** For any smooth map \(f:N\to M\), sections of the pullback bundle \(f^*E\) identify with smooth maps \(s:N\to E\) satisfying \(\pi s=f\). The derivative induced by \(\nabla\) is
\[
\nabla^f_Xs=\mathcal K\circ ds\circ X.
\tag{B.5}
\]
In a pulled-back frame, if \(s(q)=e(f(q))y(q)\), this becomes
\[
\nabla^f_Xs=e(f(q))\bigl(dy_q(X)+A_{f(q)}(df_qX)y(q)\bigr).
\tag{B.6}
\]
For a further smooth map \(h:Q\to N\) and \(v\in T_zQ\),
\[
\nabla^{f\circ h}_v(s\circ h)
=\nabla^f_{dh_zv}s.
\tag{B.7}
\]
The right side is evaluated at \(h(z)\). If \(Y\) and \(X\) are \(h\)-related vector fields, this says \(\nabla^{f\circ h}_Y(s\circ h)=(\nabla^f_Xs)\circ h\).

Along a smooth curve \(\gamma:I\to M\) these definitions give a derivative \(D_t\) of every section along the curve, satisfying
\[
D_t(fv)=f'v+fD_tv,\qquad
D_t(\sigma\circ\gamma)=\nabla_{\gamma'(t)}\sigma.
\tag{B.8}
\]
For every differentiable field \(v(t)\in E_{\gamma(t)}\),
\[
D_tv(t)=\lim_{h\to0}
\frac{T_{t+h,t}v(t+h)-v(t)}h.
\tag{B.9}
\]
Here \(T_{a,b}\) is linear transport along \(\gamma\) from time \(a\) to time \(b\), so the quotient lies in the single fibre \(E_{\gamma(t)}\). At interval endpoints the limit is one-sided.

**Proof.** The pullback consists of pairs \((q,u)\) with \(f(q)=\pi(u)\). In a vector chart it has coordinates \((q,y)\mapsto(q,e(f(q))y)\), with transitions \(g\circ f\). These charts prove the asserted smooth identification of sections, including maps \(f\) with critical points. They are the vector-bundle version of PB A.3 and B.1.

The tangent map of \(s(q)=e(f(q))y(q)\) has coordinates \((df_qX,dy_qX)\). Applying (B.1) gives (B.6), and proves smoothness of (B.5). The local potential is \(f^*A\); pulling back (A.3) gives its transformation law by Local 0.3. A.1 consequently proves all derivative axioms and independence of the frame. Alternatively these follow directly from (B.6). For a scalar function on \(N\), its derivative is \(X(f_0)\); thus the product rule uses the actual parameter-space tangent direction and does not require a vector field extending \(dfX\) on \(M\).

The ordinary chain rule \(d(s\circ h)=ds\circ dh\) proves (B.7) after composition with \(\mathcal K\). The assertion for related vector fields is its evaluation at each point. Applying this to the time interval gives (B.8), including the second identity when the field comes from a section near the curve.

To prove (B.9), choose a horizontal frame \(u(\tau)\) on a time interval containing \(t\), supplied by A.2, and write \(v(\tau)=u(\tau)c(\tau)\). Evaluation in the inverse frame makes \(c\) differentiable. The transport identities and A.2 give
\[
T_{t+h,t}v(t+h)=u(t)c(t+h),
\qquad D_tv(t)=u(t)c'(t).
\]
The ordinary derivative of \(c\) proves (B.9). For a piecewise smooth curve the same statements hold on each smooth time piece, with the respective one-sided derivatives at junctions; no two-sided derivative at a corner is asserted. This proves the transport formula with the correct order of the two time indices. □

**Theorem B.3 (curvature under arbitrary pullback).** For a covariant derivative on \(E\), define
\[
R^E(X,Y)s=\nabla_X\nabla_Ys-\nabla_Y\nabla_Xs-\nabla_{[X,Y]}s.
\tag{B.10}
\]
It is a smooth endomorphism-valued two-form, with local matrix
\[
R^E=dA+A\wedge A,\qquad
(A\wedge A)(X,Y)=A(X)A(Y)-A(Y)A(X).
\tag{B.11}
\]
For the pullback derivative along any \(f:N\to M\),
\[
R^{f^*E}(X,Y)s(q)=R^E_{f(q)}(df_qX,df_qY)s(q).
\tag{B.12}
\]

**Proof.** In one frame write \(D_X=X+A(X)\) on column functions. Expand \(D_XD_Yv-D_YD_Xv-D_{[X,Y]}v\). The ordinary second derivatives cancel because \([X,Y]v=X(Yv)-Y(Xv)\), the coordinate bracket identity proved in PB C.3. The terms containing first derivatives of \(v\) also cancel in opposite pairs. The remaining matrix is
\[
X(A(Y))-Y(A(X))-A([X,Y])+[A(X),A(Y)].
\]
The first three terms are \(dA(X,Y)\), by Curv A.2, proving (B.11). That expression is alternating and linear over real smooth functions in \(X,Y\), and is linear over \(\mathbb F\) in the value of \(s\). It is smooth. Since (B.10) was defined without a frame, the local endomorphisms agree on overlaps. Thus it is the asserted global two-form.

B.2 makes the pullback potential \(f^*A\). Curv A.2 proves \(d(f^*A)=f^*(dA)\) for every smooth map, without a rank condition. Evaluation of the two matrix products proves \((f^*A)\wedge(f^*A)=f^*(A\wedge A)\). Apply (B.11) on \(N\) to obtain (B.12). In particular one need not, and in general cannot, choose vector fields on \(M\) related to arbitrary \(X,Y\); naturality of forms gives the identity directly. □

## C. Tensor operations and compatible metrics

The free construction source is Michor's [author manuscript](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §22.12 for tensor differentiation and §22.1 for the partition-of-unity construction of positive metrics. We give the vector-bundle and complex versions in full. The metric-connection construction below uses A.2–A.3 and an explicit correction tensor; it does not require a torsion-free connection or a theorem about the Levi-Civita connection.

**Theorem C.1 (dual, tensor and homomorphism derivatives).** Covariant derivatives induce unique derivatives on dual bundles and on tensor products that obey the evaluation and tensor product rules. Explicitly,
\[
\begin{split}
(\nabla_X\alpha)(s)&=X(\alpha(s))-\alpha(\nabla_Xs),\\
\nabla_X(s\otimes t)&=(\nabla_Xs)\otimes t+s\otimes\nabla_Xt,\\
(\nabla_XT)s&=\nabla^F_X(Ts)-T\nabla^E_Xs
\quad(T:E\to F).
\end{split}
\tag{C.1}
\]
On functions the derivative is ordinary differentiation by \(X\). The induced derivatives commute with permutations of tensor factors and with contractions of a dual factor against its vector factor. They restrict to symmetric and alternating tensors, hence to symmetric and exterior powers. Transport on these bundles is respectively the inverse dual, the tensor product, and
\[
T\longmapsto T^F_\gamma\circ T\circ(T^E_\gamma)^{-1}.
\tag{C.2}
\]
For complex bundles, conjugation induces a connection on \(\overline E\), with local matrix \(\overline A\), and differentiation commutes with conjugation along real tangent directions.

**Proof.** Use the dual and tensor constructions proved by bases and transition matrices in PB C.2. Their algebraic arguments apply over \(\mathbb C\) as well, since they use only finite sums, products and evaluation in a basis. A dual vector is a row \(\alpha\); the first expression in (C.1), evaluated on a column \(v\), is
\[
X(\alpha v)-\alpha(Xv+A(X)v)
=\bigl(X\alpha-\alpha A(X)\bigr)v.
\]
It is linear over \(\mathbb F\) in \(v\), is smooth, and so defines a dual section. Replacing the argument section by \(fs\) gives the same assertion intrinsically: the two \(X(f)\alpha(s)\) terms cancel. The expression depends only on the value of \(s\), either by this local calculation or A.1's locality. Thus the first rule defines a global derivative. Its additivity and Leibniz rule in \(\alpha\) follow by differentiating a scalar product; its linearity in \(X\) is immediate. In column coordinates its connection matrix is \(-A^{\mathsf T}\).

Let \(e_a,f_b\) be local frames of two bundles, with matrices \(A,B\). Every tensor section is uniquely \(\sum_{a,b}c^{ab}e_a\otimes f_b\), by PB C.2's basis construction. Define its derivative by differentiating each coefficient and applying the second rule of (C.1) to each basis tensor. Its matrix on the product basis is
\[
A(X)\otimes I+I\otimes B(X).
\]
For arbitrary local sections \(s,t\), expansion of their coordinates and the ordinary product rule verify the stated tensor rule. Under a frame change \((e,f)\mapsto(eg,fh)\), differentiating
\(g\otimes h\) gives \(dg\otimes h+g\otimes dh\). Combining this with (A.3) proves exactly the transition rule (A.3) for the tensor matrix. Hence these locally defined derivatives agree globally. A.1 proves their axioms; spanning by the basis tensors proves uniqueness.

Iteration gives a finite sum of one connection action on each factor of any mixed tensor. Permuting factors permutes this finite sum and thus commutes with the derivative. Contracting a dual factor and its vector factor cancels their two connection terms: in rows and columns they are \(-\alpha A\) and \(Av\), whose evaluated contributions are \(-\alpha Av+\alpha Av=0\). The ordinary derivative of their evaluation is the ordinary product rule already checked. On a general tensor, expand in pure tensors and scalar coefficients; they span every fibre and form local frames, so this proves commutation for all contractions.

The symmetrizer and antisymmetrizer are the averages of the finitely many factor permutations, with respectively coefficient \(1/k!\) or the permutation sign divided by \(k!\). Their images are exactly the symmetric and alternating tensors: permuting an average gives the prescribed symmetry, and applying the average to a tensor already having that symmetry returns it. Thus they are projections. They commute with the derivative by the permutation result. Their images are smooth subbundles: in a frame, the symmetric tensors indexed by nondecreasing tuples and the alternating tensors indexed by strictly increasing tuples are bases, as the finite expansion in PB C.2 shows. The induced derivative consequently preserves these subbundles. The exterior-power identification is the alternating-basis identification from PB C.2. Degree zero is the scalar line, with its ordinary derivative; powers larger than the rank in the alternating case are zero and cause no exception.

For homomorphisms, identify \(\operatorname{Hom}_{\mathbb F}(E,F)=F\otimes E^*\) by \(t\otimes\alpha:s\mapsto t\alpha(s)\). Matrix units in local bases prove this is a smooth isomorphism. The tensor and dual rules give its matrix formula
\[
\nabla_XT=X(T)+B(X)T-TA(X),
\tag{C.3}
\]
which is precisely the third rule of (C.1). They also prove uniqueness.

To check transport, use horizontal frames for the original bundles on a path, by A.2. Their dual frames, tensor-product frames and matrix-unit frames have zero derivative by the rules just proved. A field in one of these frames is parallel precisely when all its coefficients are constant, again by A.2 applied to that induced derivative. Hence its transport is the indicated algebraic operation on the original transports; the dual evaluation is held constant by composing with the inverse original transport. This proves (C.2) and all transport assertions.

Finally, for a complex bundle define \(\overline E\) by the conjugated transition matrices and local coordinates \(\overline v\); multiplication by a complex scalar in that bundle corresponds to multiplication by its conjugate in \(E\). Conjugating (A.3) proves the correct change rule for \(\overline A\). Because the tangent direction \(X\) is real, \(X(\overline v)=\overline{X(v)}\). Formula (A.2) therefore proves the claimed commutation. □

**Theorem C.2 (positive metrics and compatible derivatives).** Every smooth real vector bundle has a smooth positive definite inner product, and every smooth complex vector bundle has a smooth positive definite Hermitian form. For each such metric \(h\), a compatible covariant derivative exists. With the convention that a Hermitian metric is conjugate linear in its first entry, compatibility means
\[
X(h(s,t))=h(\nabla_Xs,t)+h(s,\nabla_Xt).
\tag{C.4}
\]
It holds if and only if parallel transport along every smooth path preserves the metric. In a frame with Gram matrix \(H\), the condition is
\[
dH=A^*H+HA,
\tag{C.5}
\]
where \(*\) is transpose in the real case and conjugate transpose in the complex case. In an orthonormal frame, it is precisely \(A^*=-A\).

**Proof.** For existence of a metric, take the Euclidean or standard Hermitian form in each vector chart. Use a locally finite subordinate smooth partition of unity \((\phi_i)\), from Local 3.1, and set \(h=\sum_i\phi_i h_i\). Each weighted form extends smoothly by zero outside its chart because its support is contained in that chart, and locally only finitely many terms occur. The sum is smooth, symmetric or Hermitian, and positive definite: for a nonzero vector at least one positive coefficient multiplies a positive squared norm, while every other term is nonnegative. This is also the real construction of PB D.2. Rank zero has the unique form on the zero space.

The covariant derivative of the metric is well defined by C.1, regarding it in the complex case as a section of \(\overline E^*\otimes E^*\). Directly, it is the right-side defect
\[
(\nabla_Xh)(s,t)=X(h(s,t))-h(\nabla_Xs,t)-h(s,\nabla_Xt).
\tag{C.6}
\]
The derivative-of-scalar terms cancel when either section is multiplied by a smooth scalar, with conjugation in the first entry. Thus it depends only on their values. In a frame, inserting \(s=eu\), \(t=ev\) and \(h(s,t)=u^*Hv\) gives
\[
(\nabla_Xh)(s,t)
=u^*\bigl(X(H)-A(X)^*H-HA(X)\bigr)v.
\tag{C.7}
\]
The terms containing derivatives of \(u,v\) cancel, proving (C.5). If \(H=I\), it gives the skew-adjoint condition. Real orthonormal local frames are supplied by PB D.2. In the complex case use the same Gram–Schmidt construction with projection \(u_k h(u_k,e_j)\) and positive real denominator \(\sqrt{h(v_j,v_j)}\). At each step independence ensures the nonzero remainder, conjugate symmetry proves its orthogonality, and smoothness follows from the smooth positive square root as in PB D.2. Thus the orthonormal-frame assertion is meaningful in both cases.

To construct a compatible derivative, start with any \(\nabla^0\), which exists by A.2. Write \(S=\nabla^0h\), with local matrix
\(S_X=X(H)-A^0(X)^*H-HA^0(X)\).
This matrix is self-adjoint because \(H^*=H\) and \(X\) is real. Define
\[
B(X)=\tfrac12 H^{-1}S_X.
\tag{C.8}
\]
The inverse is smooth by Local 0.4. Under a frame change, \(\widetilde H=g^*Hg\) and \(\widetilde S=g^*Sg\), the latter because (C.6) is an intrinsic tensor. Thus \(\widetilde B=g^{-1}Bg\), so (C.8) defines an endomorphism-valued one-form globally. Put \(\nabla=\nabla^0+B\), using A.3. Since \(H^*=H\) implies \((H^{-1})^*=H^{-1}\), equation (C.8) gives
\[
HB=\tfrac12S,\qquad B^*H=\tfrac12S.
\]
Substituting \(A=A^0+B\) in (C.7) makes its defect \(S-B^*H-HB=0\). This proves compatibility and existence. In rank zero the construction is the unique zero derivative; no matrix inverse need be taken.

If (C.4) holds, apply (C.7) along a path, using B.2's pulled-back derivative. For two parallel fields the derivative of \(h(u(t),v(t))\) is zero. The fundamental theorem of calculus, Local 0.3, makes this scalar constant on each path interval, hence on any finite concatenation. Transport therefore preserves the metric.

Conversely assume all smooth path transports preserve it. Fix \(x\), \(v\in T_xM\) and two fibre vectors. A coordinate straight line represents \(v\) as the velocity of a smooth path at \(x\), on a sufficiently small interval. Extend the two vectors by parallel transport along this path, as A.2 permits. Their metric pairing is constant by assumption, so its derivative at the initial time is zero. Formula (C.7) along the path identifies that derivative with \((\nabla_vh)_x\) on the prescribed two vectors. They and \(v\) were arbitrary, so \(\nabla h=0\), proving (C.4). □

**Example C.3 (a varying metric on a trivial bundle).** On the trivial real line over \(\mathbb R\), take the metric \(h_x(u,v)=e^{2x}uv\). Its unique compatible connection has potential \(A=dx\) in the standard frame. Transport from \(x_0\) to \(x_1\) multiplies the fibre coordinate by \(e^{x_0-x_1}\), which preserves this varying metric but does not preserve the standard coordinate norm in general.

**Proof.** The Gram matrix is the scalar \(H=e^{2x}\). Equation (C.5) is \(2e^{2x}dx=2e^{2x}A\), giving \(A=dx\) and uniqueness. Along a path \(x(t)\), equation (A.5) for a vector coordinate is \(v'+x'v=0\). Differentiating \(e^{x(t)}v(t)\) shows it is constant; conversely the resulting formula solves the equation. The ordinary exponential and product rules are supplied by Local 2.3 for the multiplicative positive-real group and Local 0.3. At the endpoints,
\(e^{2x_1}(e^{x_0-x_1}u)(e^{x_0-x_1}v)=e^{2x_0}uv\),
which verifies preservation directly. The smooth frame \(e^{-x}\) is orthonormal and its transformed potential is zero by (A.3), giving the same conclusion in that frame. □

## D. Tangent velocities and the failure of symmetry

In this part \(E=TM\), \(n=\dim M\), and \(P=\operatorname{Fr}(TM)\) is the real full frame bundle. A frame \(u:\mathbb R^n\to T_xM\) acts on columns. We use the exact free Michor author manuscript already cited, Sections 22.10 and 25.4–25.6, as construction material. The differential-form rules and the basic-form correspondence used below are proved in [Curvature A.1–A.2 and A.5–A.6](curvature-and-holonomy-groups.md); the frame bundle and tangent bracket are proved in [PB C.1 and C.3](principal-bundles-and-associated-bundles.md). No metric or torsion-free hypothesis is imposed.

**Theorem D.1 (solder form and torsion).** Define the solder form on \(P\) by
\[
\theta_u(Z)=u^{-1}(d\pi_uZ).
\tag{D.1}
\]
It is smooth, vanishes on vertical vectors, and satisfies \(R_a^*\theta=a^{-1}\theta\). Under the associated-bundle identification \([u,v]\mapsto u(v)\), it represents the identity \(TM\to TM\). If \(\omega\) is the principal connection of \(\nabla\), the horizontal equivariant two-form
\[
\Theta=D\theta=d\theta+\omega\wedge\theta
\tag{D.2}
\]
represents the tensor
\[
\mathcal T(X,Y)=\nabla_XY-\nabla_YX-[X,Y].
\tag{D.3}
\]

**Proof.** In a local frame \(e\), write \(u=e(x)g\) and let \(\sigma\) denote the vector of dual one-forms: \(\sigma_x(v)=e(x)^{-1}v\). Formula (D.1) is \(g^{-1}\sigma\) in this chart, so is smooth. Its vertical and equivariance properties follow immediately from \(d\pi\,dR_a=d\pi\) and \((ua)^{-1}=a^{-1}u^{-1}\). Evaluation gives \(u\theta_u(Z)=d\pi Z\), which proves the identity assertion, including surjectivity on each horizontal space.

The representation of \(\mathrm{GL}(n,\mathbb R)\) on \(\mathbb R^n\) has derivative the identity matrix action, as proved in A.2. Curvature A.5 therefore proves both equality in (D.2) and its horizontality and equivariance. In the section \(e\), put \(A=e^*\omega\). For \(Y=e\sigma(Y)\), A.1 gives
\[
e^{-1}\nabla_XY=X(\sigma(Y))+A(X)\sigma(Y).
\]
Subtract the expression with \(X,Y\) interchanged and then \(\sigma([X,Y])\). The coordinate formula for \(d\sigma\) in Curvature A.2 identifies the result with \((d\sigma+A\wedge\sigma)(X,Y)=e^*\Theta(X,Y)\). This proves (D.3).

For completeness its tensoriality is also visible directly. PB C.3 gives \([fX,Y]=f[X,Y]-Y(f)X\). Using the derivative axioms, the two terms \(Y(f)X\) cancel in \(\mathcal T(fX,Y)\), leaving \(f\mathcal T(X,Y)\). Skew-symmetry gives linearity over smooth functions in the second entry as well. In local bases, these properties and smoothness identify a smooth \(TM\)-valued two-form, with no external tensor criterion required. □

**Theorem D.2 (both structure identities with arbitrary torsion).** Let \(\Omega=d\omega+\omega\wedge\omega\). Then
\[
D\Theta=\Omega\wedge\theta,\qquad
d\Omega+\omega\wedge\Omega-\Omega\wedge\omega=0.
\tag{D.4}
\]
In a local frame these read
\[
\tau=d\sigma+A\wedge\sigma,\quad F=dA+A\wedge A,
\qquad d\tau+A\wedge\tau=F\wedge\sigma.
\tag{D.5}
\]
In particular, if \(\mathcal T=0\), then
\[
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0.
\tag{D.6}
\]

**Proof.** Curvature A.4 identifies the matrix curvature with \(\Omega\); its A.6 gives \(D^2\theta=\Omega\wedge\theta\) and the second identity of (D.4). These are applications to the horizontal equivariant form already established in D.1. One can check the first identity without cancelling an implicit sign:
\[
\begin{aligned}
d\Theta+\omega\wedge\Theta
&=d\omega\wedge\theta-\omega\wedge d\theta
  +\omega\wedge d\theta+\omega\wedge\omega\wedge\theta\\
&=(d\omega+\omega\wedge\omega)\wedge\theta.
\end{aligned}
\]
Here \(d^2\theta=0\), and the minus sign is the degree-one product rule from Curvature A.1–A.2. Pullback by \(e\) gives (D.5). When \(\tau=0\), evaluate \(F\wedge\sigma=0\) on \(X,Y,Z\): it is
\(F(X,Y)\sigma(Z)+F(Y,Z)\sigma(X)+F(Z,X)\sigma(Y)=0\).
Multiplication by \(e\) and B.3's curvature formula give (D.6). No torsion-free identity is asserted when \(\mathcal T\ne0\). □

**Lemma D.3 (the connector detects torsion, also along maps).** In coordinates on \(TTM\), the rule
\[
\kappa(x,y;v,z)=(x,v;y,z)
\tag{D.7}
\]
defines a smooth involution independent of coordinates. If \(\mathscr K:TTM\to TM\) is B.1's connector, then
\[
\mathcal T(X,Y)=(\mathscr K\kappa-\mathscr K)\,dX(Y).
\tag{D.8}
\]
For every smooth \(f:N\to M\) and fields \(U,V\) on \(N\), including at critical points of \(f\),
\[
\begin{aligned}
\mathcal T(df(U),df(V))
&=\nabla^f_U(df(V))-\nabla^f_V(df(U))-df([U,V])\\
&=(\mathscr K\kappa-\mathscr K)\,d(df)\,dU(V).
\end{aligned}
\tag{D.9}
\]

**Proof.** A coordinate change \(q=q(x)\) acts on these four entries by
\[
(x,y;v,z)\longmapsto
(q(x),dq_x y;dq_x v,d^2q_x(v,y)+dq_x z).
\]
The symmetry of \(d^2q\), proved by the mixed-partial calculation of PB C.3, makes this commute with (D.7). Thus the maps glue, are smooth, and square to the identity. Write \(A_x(v)y\) for the bilinear term of the connector, so that \(\mathscr K(x,y;v,z)=z+A_x(v)y\). Subtracting after interchange gives
\[
(\mathscr K\kappa-\mathscr K)(x,y;v,z)=A_x(y)v-A_x(v)y.
\]
At \(dX(Y)\), \(y=X,v=Y\). Expanding (D.3) in the coordinate frame cancels \(dY(X)-dX(Y)=[X,Y]\), leaving exactly this expression. This proves (D.8), with the order of its two entries fixed.

For (D.9) work in arbitrary charts on \(N,M\). By B.2,
\[
\nabla^f_U(df(V))=d^2f(U,V)+df(dV(U))+A_{f}(df(U))df(V).
\]
Subtract its counterpart with \(U,V\) exchanged. The Hessians cancel by symmetry, and the two first-derivative terms cancel \(df([U,V])\). What remains is the left side by the preceding coordinate expression. Also \(d(df)dU(V)\) has its second and third entries \(df(U),df(V)\); its fourth entry is \(d^2f(V,U)+df(dU(V))\). That fourth entry cancels from the connector difference, proving the last equality. No inverse to \(df\) has been used. □

**Example D.4 (changing torsion and a constant nonzero example).** If \(\nabla'_XY=\nabla_XY+S_XY\), then
\[
\mathcal T'(X,Y)=\mathcal T(X,Y)+S_XY-S_YX.
\tag{D.10}
\]
Every tangent connection can therefore be replaced by a torsion-free one with the same equation \(\nabla_{\dot\gamma}\dot\gamma=0\). On \(\mathbb R^2\), the connection whose only nonzero coordinate coefficient is \(\nabla_{\partial_x}\partial_y=\partial_x\) has \(\mathcal T(\partial_x,\partial_y)=\partial_x\).

**Proof.** Substitution in (D.3) gives (D.10), since the bracket is unchanged. The tensor \(S_XY=-\mathcal T(X,Y)/2\) is permitted by A.3 and D.1. Its antisymmetrization is \(-\mathcal T\), so the new torsion is zero. Along a curve, B.2 evaluates the difference of the two derivatives at \(S_{\dot\gamma}\dot\gamma=0\); thus the equations agree. This assertion compares equations and does not invoke a geodesic existence theorem. For the example take \(A=N\,dx\), where \(N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\), in the coordinate frame. A.1 constructs the connection. The coordinate fields commute, giving the claimed torsion. More generally, if \(\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k\), the coefficients are \(\Gamma^k_{ij}-\Gamma^k_{ji}\). They cannot in general be replaced by \(2\Gamma^k_{ij}\); no symmetry has been assumed. □

## E. Connections on affine frames

An affine frame of \(T_xM\) is a bijective affine map \(q:\mathbb R^n\to T_xM\), written uniquely \(q(w)=b+u w\), where \(b\in T_xM\) and \(u\in\operatorname{Fr}(T_xM)\). The origin \(b\) is part of the frame. We derive its connection theory directly from the complete programme constructions [PB A.1–A.2 and B.1](principal-bundles-and-associated-bundles.md), [Conn A.2–A.3 and C.1–C.2](connections-and-parallel-transport.md), and [Curvature A.4 and C.5](curvature-and-holonomy-groups.md). The arguments below supply the affine group calculations; no separate affine-connection theorem is assumed.

**Lemma E.1 (the affine group and affine frame bundle).** The group \(G=\operatorname{Aff}(n,\mathbb R)\) consists of pairs \((a,c)\) acting by \(w\mapsto aw+c\), with
\[
(a,c)(h,d)=(ah,c+ad),\qquad
(a,c)^{-1}=(a^{-1},-a^{-1}c).
\tag{E.1}
\]
It is a Lie group, represented faithfully by matrices
\[
\begin{pmatrix}a&c\\0&1\end{pmatrix}.
\]
Its Lie algebra consists of \((B,v)\), represented by the same block matrix with bottom-right entry zero, and has bracket
\[
[(B,v),(C,w)]=([B,C],Bw-Cv).
\tag{E.2}
\]
Affine frames form a smooth principal right \(G\)-bundle \(Q\to M\). There is an embedding \(j:P\to Q\), \(j(u)(w)=u w\), and a smooth linear-part map \(\ell:Q\to P\), \(\ell(b+u\,\cdot)=u\), equivariant for \(p:G\to\mathrm{GL}(n,\mathbb R)\), \(p(a,c)=a\).

**Proof.** Composition of the two affine maps gives (E.1), and substitution verifies the inverse. The manifold is the product of the open set of invertible matrices with \(\mathbb R^n\). Multiplication is polynomial and inversion smooth by Local 0.4, so it is a Lie group. The block representation is injective and smooth with smooth inverse onto its image. Tangent vectors at the identity are exactly the displayed matrices with arbitrary \(B,v\). For completeness, in any matrix group the left-invariant field belonging to a tangent matrix \(X\) is \(g\mapsto gX\). Differentiation gives its bracket with \(g\mapsto gY\) as \(g(XY-YX)\), by PB C.3's bracket convention. Block multiplication gives (E.2).

For a local linear frame \(e\), every affine frame has unique coordinates

\(q(w)=e(x)(c+a w)=j(e(x))(a,c)(w)\).

If \(e'=eg\), primed coordinates \((a',c')\) and unprimed coordinates satisfy \((a,c)=(ga',gc')\), the left multiplication by \((g,0)\). These smooth transitions satisfy the cocycle condition, so PB A.1 supplies all manifold, separation and countability properties and the principal action, which is composition on the right. The set thereby constructed is exactly the stated set of affine maps by its unique coordinates. In these charts \(j(ea)\) has \(c=0\), proving it is an embedding; \(\ell(x,a,c)=(x,a)\) is smooth. Direct composition gives \(\ell(q(a,c))=\ell(q)a\). These arguments also cover \(n=0\), when both groups and fibres consist of one point. □

**Theorem E.2 (generalized and normalized affine connections).** Principal connections \(\eta\) on \(Q\) correspond bijectively to pairs \((\nabla,K)\), where \(\nabla\) is a linear connection on \(TM\) and \(K:TM\to TM\) is a smooth bundle endomorphism. On the zero-origin copy of \(P\),
\[
j^*\eta=
\begin{pmatrix}\omega&\varphi\\0&0\end{pmatrix},
\qquad \varphi_u(Z)=u^{-1}K_x(d\pi Z).
\tag{E.3}
\]
The connection is called normalized when \(K=I\), equivalently \(\varphi=\theta\). Thus normalized affine connections correspond bijectively to linear connections. In a local zero-origin affine section \(j(e)\), its potential is
\[
\mathcal A=\begin{pmatrix}A&k\\0&0\end{pmatrix},
\qquad k=e^{-1}K\in\Omega^1(U,\mathbb R^n),
\tag{E.4}
\]
where \(k(X)=e^{-1}K(X)\).

**Proof.** Pull a principal connection on \(Q\) back by \(j\) and separate its two Lie-algebra components. On a fundamental vector for \(B\in\mathfrak{gl}(n)\), reproduction gives \((B,0)\). Equivariance under \((a,0)\) gives
\[
R_a^*\omega=a^{-1}\omega a,\qquad R_a^*\varphi=a^{-1}\varphi.
\]
Consequently \(\omega\) is a connection on \(P\) by Conn A.2, hence corresponds to \(\nabla\) by A.2. The second form vanishes on vertical vectors. For \(X\in T_xM\), choose \(u\in P_x\) and a lift \(Z\in T_uP\) of \(X\), and define \(K_x(X)=u\varphi_u(Z)\). Vertical vanishing makes this independent of the lift. Equivariance makes it independent of \(u\). Local section coordinates prove that it is a smooth fibrewise linear endomorphism, and establish (E.3).

Conversely, given \((\nabla,K)\), put (E.4) in each local section \(j(e)\). When \(e'=eg\), A.1 gives \(A'=g^{-1}Ag+g^{-1}dg\) and the definition gives \(k'=g^{-1}k\). These are exactly the block entries of
\[
\mathcal A'=\begin{pmatrix}g&0\\0&1\end{pmatrix}^{-1}
\mathcal A\begin{pmatrix}g&0\\0&1\end{pmatrix}
+\begin{pmatrix}g&0\\0&1\end{pmatrix}^{-1}d\begin{pmatrix}g&0\\0&1\end{pmatrix}.
\]
Conn A.3 therefore produces a unique global principal connection. Its pullback along \(j\) has (E.3), by that theorem's full local formula. Every point of \(Q\) is \(j(e(x))h\), so the same full local formula proves uniqueness from these potentials and that the two constructions are inverse. Finally \(u^{-1}K(X)=u^{-1}X\) for every \(u,X\) is equivalent to \(K=I\), proving normalization. □

**Theorem E.3 (curvature and projected holonomy).** Let \(\widehat\Omega=d\eta+\eta\wedge\eta\). Then
\[
j^*\widehat\Omega=
\begin{pmatrix}\Omega&d\varphi+\omega\wedge\varphi\\0&0\end{pmatrix}.
\tag{E.5}
\]
For \(K=I\) its upper-right entry is \(\Theta\). The linear-part homomorphism maps full affine holonomy onto full linear holonomy, and restricted affine holonomy onto restricted linear holonomy, using \(q\in Q_x\) and \(\ell(q)\in P_x\) as base frames.

**Proof.** Pullback commutes with \(d\) and matrix wedge multiplication by Curvature A.1–A.2. Squaring the block matrix in (E.3) gives upper-left entry \(\omega\wedge\omega\) and upper-right entry \(\omega\wedge\varphi\); this proves (E.5). D.2 proves the normalized assertion.

To prove the holonomy statement, first check equality of connection forms \(\ell^*\omega=p_*\eta\) on all of \(Q\). In the chart \(q=j(e)h\), with \(h=(a,c)\), Conn A.3 gives \(\eta=h^{-1}\mathcal A h+h^{-1}dh\). Its upper-left block is \(a^{-1}Aa+a^{-1}da\), exactly the principal form on \(\ell(q)=ea\). This establishes the equality without asserting that the zero-origin subbundle is horizontal. Thus the linear part of a horizontal affine lift is a horizontal linear lift. Initial values and uniqueness from Conn C.1 identify these lifts on their entire intervals; the conclusion also holds on finitely many \(C^1\) pieces by Curvature C.2.

For any based loop \(c\), write its affine endpoint as \(q h(c)\). Equivariance of \(\ell\) and the preceding lift identity give the linear endpoint \(\ell(q)p(h(c))\). Freeness of the linear action means its holonomy element is precisely \(p(h(c))\). Conversely every linear holonomy element comes from a loop, and the same loop has an affine lift by Conn C.1 (or Curvature C.2), so lies in this image. The argument applies to exactly the same continuously nullhomotopic loops on both sides, giving the restricted assertion. Curvature C.5 supplies the full and restricted holonomy groups; no closedness assumption on either is made. □

## F. Transporting points and developing paths

We now derive affine transport from the connection just constructed. The only integration and transport facts used are the complete proofs in [Local 0.3](local-tools-for-bundles-and-transport.md), [Conn C.1–C.2](connections-and-parallel-transport.md), and B.2. Curvature D.0, proved in the [curvature chapter](curvature-and-holonomy-groups.md), supplies circle angles and winding for the example below.

**Theorem F.1 (affine transport and development).** For a finitely piecewise smooth path \(\gamma:[0,b]\to M\), let \(T_{st}:T_{\gamma(s)}M\to T_{\gamma(t)}M\) be linear transport. For the generalized affine connection \((\nabla,K)\), set
\[
\delta_K(t)=\int_0^t T_{r0}K_{\gamma(r)}\dot\gamma(r)\,dr\in T_{\gamma(0)}M.
\tag{F.1}
\]
Its affine transport is
\[
F_{0t}(v)=T_{0t}(v-\delta_K(t)),\qquad F_{0t}^{-1}(0)=\delta_K(t).
\tag{F.2}
\]
It is the unique solution of the inhomogeneous equation
\[
D_t w=-K\dot\gamma,\qquad w(0)=v.
\tag{F.3}
\]
When \(K=I\), \(\delta=\delta_I\) is the development of the path in its initial tangent space; \(\delta(0)=0\) and \(\dot\delta(t)=T_{t0}\dot\gamma(t)\) on each smooth piece. Affine transports are invertible, concatenate in path order, and are unchanged by orientation-preserving piecewise smooth reparametrization.

**Proof.** The bundle associated to \(Q\) by its affine action on \(\mathbb R^n\) is \(TM\) as a bundle of affine spaces: the evaluation map \([q,z]\mapsto q(z)\) is well defined because \([qh,z]=[q,hz]\). In a local zero-origin frame its formula and inverse are simply the ordinary tangent-bundle coordinates. PB B.1 therefore gives a smooth bundle identification. A horizontal path \(q(t)\) defines \(F_{0t}(q(0)z)=q(t)z\). Equivariance of principal transport shows this definition is independent of the chosen initial affine frame.

In a local section write \(q(t)=j(e(\gamma(t)))h(t)\), where
\(h=\left(\begin{smallmatrix}a&c\\0&1\end{smallmatrix}\right)\).
Conn C.1 gives \(h'=-\mathcal A(\dot\gamma)h\), hence
\[
a'=-A(\dot\gamma)a,\qquad c'=-A(\dot\gamma)c-k(\dot\gamma).
\]
The coordinates \(y(t)=a(t)z+c(t)\) of \(q(t)z\) consequently satisfy \(y'+A(\dot\gamma)y=-k(\dot\gamma)\). By B.2 this is (F.3), independent of the local frame.

Choose an initial linear frame and transport it along the whole path by A.2. In that moving frame B.2 gives
\[
\frac{d}{dt}\bigl(T_{t0}w(t)\bigr)=T_{t0}D_t w(t).
\]
The integrand in (F.1) is continuous on each closed smooth piece and has the appropriate one-sided values at the finitely many corners. Componentwise integration and the fundamental theorem in Local 0.3 give (F.2), with continuity across corners. Conversely differentiating this integral gives (F.3) and its initial value. If two solutions exist, their difference has constant coordinates in the moving frame and initial value zero, proving uniqueness. Since \(T_{0t}\) is invertible, (F.2) gives the inverse image of zero exactly as stated. The derivative formula for \(\delta\) is again the fundamental theorem on each piece. Finally the evaluation construction transfers inverse, concatenation and reparametrization identities from Conn C.2 to \(F\); these also follow from the just-proved uniqueness. No completeness assumption on the manifold or connection is involved. □

**Theorem F.2 (moving the origin and parallel point fields).** For a vector field \(V\), let \(j_V(u)(z)=V(x)+uz\). In the generalized connection,
\[
j_V^*\eta=
\begin{pmatrix}\omega&\varphi+Dv\\0&0\end{pmatrix},
\qquad v(u)=u^{-1}V(x),\quad Dv=dv+\omega v.
\tag{F.4}
\]
Thus \(Dv\) represents \(\nabla V\). A vector field \(V\), considered as a point in every affine tangent space, is parallel along every path exactly when
\[
\nabla_XV=-K(X)\quad\hbox{for every }X.
\tag{F.5}
\]
For the normalized flat connection on connected \(\mathbb R^n\), these fields are exactly \(V(x)=c-x\). For the normalized flat connection on the circle with its global angular frame parallel, there is no parallel point field. Its affine holonomy consists of the translations by \(2\pi\mathbb Z\), although its linear holonomy is trivial.

**Proof.** The relation \(j_V(u)=j(u)t(v(u))\), with
\(t(v)=\left(\begin{smallmatrix}I&v\\0&1\end{smallmatrix}\right)\),
and Conn A.3's variable right-translation formula give
\[
t(v)^{-1}\begin{pmatrix}\omega&\varphi\\0&0\end{pmatrix}t(v)+t(v)^{-1}dt(v)
=\begin{pmatrix}\omega&\varphi+\omega v+dv\\0&0\end{pmatrix}.
\]
This proves (F.4) on \(P\). A.2 or Curvature A.5 identifies \(Dv\) with \(\nabla V\). Along any path, F.1 says that \(V(\gamma(t))\) is transported as a point exactly when \(\nabla_{\dot\gamma}V=-K\dot\gamma\). Equation (F.5) implies this for every path by uniqueness. Conversely every tangent vector is the initial velocity of a coordinate straight path on a sufficiently small interval; differentiation along those paths gives (F.5).

For the standard flat connection on \(\mathbb R^n\), (F.5) is \(dV=-I\). Along a line segment, Local 0.3 gives \(V(x)+x=V(0)\); thus \(V=c-x\), and differentiation checks every such field. In rank zero the same statement has its unique empty-vector value.

For the circle use \(z\in U(1)\), its global nonzero tangent frame \(e(z)=iz\), and the global angular form \(\alpha\) of Curvature D.0, so \(\alpha(e)=1\). Declare \(\nabla e=0\); A.1 makes this a global tangent connection. Its matrix curvature and torsion are zero since every two-form on a one-dimensional space is zero, and its linear transport sends \(e\) to \(e\). For a loop of winding \(m\), D.0 gives \(\int\alpha=2\pi m\), so F.1 gives
\[
F(ae_x)=(a-2\pi m)e_x.
\tag{F.6}
\]
Every integer winding occurs by D.0, proving the holonomy assertion, with either sign giving the same translation subgroup. A parallel point field would have a value fixed by the once-positive loop; no real \(a\) satisfies \(a-2\pi=a\). This proves nonexistence. In particular, preserving zero is not automatic for a normalized affine connection. □

**Example F.3 (a noncommuting potential and a varying frame).** On the trivial rank-two bundle over \(\mathbb R^2\), let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
A=N\,dx+H\,dy,\quad a=I+xN.
\]
In the frame \(e'=ea\), the potential and curvature are
\[
A'=2N\,dx+(H+2xN)\,dy,\qquad
F=F'=-2N\,dx\wedge dy=a^{-1}Fa.
\tag{F.7}
\]
Transport along any horizontal coordinate segment from \(x_0\) to \(x_1\) has matrix \(I-(x_1-x_0)N\) in the original frame and \(I-2(x_1-x_0)N\) in the new frame. The dual potential on column coordinates is \(-A^{\mathsf T}\).

**Proof.** Direct matrix multiplication gives \(N^2=0\), \(HN=N\), \(NH=-N\). Thus \(a^{-1}=I-xN\), \(a^{-1}Na=N\), \(a^{-1}Ha=H+2xN\) and \(a^{-1}da=N\,dx\). A.1 gives \(A'\). B.3 gives \(F=[N,H]\,dx\wedge dy=-2N\,dx\wedge dy\). For the new potential, the derivative term is \(2N\,dx\wedge dy\) and its wedge square is \([2N,H+2xN]\,dx\wedge dy=-4N\,dx\wedge dy\); their sum is (F.7). Conjugation fixes \(N\), verifying the last equality independently.

Along the segment, differentiating \(I-(x(t)-x_0)N\) verifies the equation \(G'=-\dot x NG\), since \(N^2=0\), with initial matrix \(I\). A.2's uniqueness therefore gives the transport. New coordinates multiply it by \(a(x_1)^{-1}\) on the left and \(a(x_0)\) on the right; \(N^2=0\) reduces the product to the stated doubled coefficient. C.1's dual formula is \(X\lambda-\lambda A\) for row coordinates; transposing gives the column potential \(-A^{\mathsf T}\). □

## G. Geodesics and a complete latitude calculation

The construction source for the sphere frame is Michor's exact free [author manuscript](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §25.7, native pages 327–328. We compute the connection, development and affine holonomy explicitly. [DG-CHAR-17 V.1 and V.5](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md) prove the Levi-Civita theorem and the smooth round-sphere model. Conn E.1 proves the circle exponential, its period and differentiation, so the trigonometric notation below has an earlier programme foundation.

**Theorem G.1 (development and affine parameter).** For a \(C^2\) curve, its normalized development satisfies
\[
\delta''(t)=T_{t0}D_t\dot\gamma(t).
\tag{G.1}
\]
Consequently \(D_t\dot\gamma=0\) if and only if \(\delta(t)=t v\) for a constant initial tangent vector \(v\), with initial time zero. For the standard flat connection on \(\mathbb R^n\), \(\delta(t)=\gamma(t)-\gamma(0)\). A straight image alone does not imply affine parametrization.

**Proof.** Curvature C.2 extends the transport used in F.1 to \(C^1\) paths. F.1's integral and moving-frame proof requires only continuous velocity, so its derivative formula \(\delta'=T_{t0}\dot\gamma\) remains valid there. For a \(C^2\) curve, \(\dot\gamma\) is \(C^1\); differentiating its coordinates in a horizontal frame, as proved in A.2 and B.2, gives (G.1). Invertibility of transport proves that one side vanishes precisely when the other does. Integrate twice using Local 0.3 and \(\delta(0)=0\) to obtain the asserted affine function; differentiating it proves the converse. In the standard flat frame transport is the identity, so F.1 and Local 0.3 give the difference of endpoints. For \(\gamma(t)=t^2v\) with \(v\ne0\), the image is straight but \(\delta''=2v\ne0\); this verifies the final distinction.

For a closed path, if a horizontal frame has endpoint \(u(b)=u(0)a\) and \(d=u(0)^{-1}\delta(b)\), F.1 gives its affine holonomy coordinates \((a,-ad)\). This follows by applying \(F_{0b}\) to every \(u(0)v\), obtaining \(u(0)a(v-d)\); it determines the affine map uniquely. If the alternative law \(D_tw=+\dot\gamma\) is chosen, it is E.2's generalized connection with \(K=-I\), and F.1 instead gives \(T_{0t}(v+\delta(t))\). The two signs therefore refer to two explicitly specified connection conventions. □

**Theorem G.2 (all nondegenerate latitudes).** On the unit round sphere, fix a colatitude \(0<\theta<\pi\), put \(s=\sin\theta>0\), \(c=\cos\theta\), and traverse the positive latitude
\[
\gamma(\phi)=(s\cos\phi,s\sin\phi,c),\qquad 0\le\phi\le2\pi.
\tag{G.2}
\]
Use the periodic orthonormal tangent frame
\[
\begin{aligned}
e_\theta(\phi)&=(c\cos\phi,c\sin\phi,-s),\\
e_\phi(\phi)&=(-\sin\phi,\cos\phi,0),\qquad E=(e_\theta,e_\phi),
\end{aligned}
\tag{G.3}
\]
and identify the initial tangent space with \(\mathbb R^2\) by \(E(0)\). Define
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
R(a)=\begin{pmatrix}\cos a&-\sin a\\\sin a&\cos a\end{pmatrix}.
\]
Linear transport in this moving frame is \(R(-c\phi)\), while the development has initial-frame coordinates
\[
d(\phi)=
\begin{cases}
\dfrac{s}{c}\bigl(\cos(c\phi)-1,\ \sin(c\phi)\bigr),&c\ne0,\\
(0,\phi),&c=0.
\end{cases}
\tag{G.4}
\]
For \(c\ne0\), this developed path lies on the circle of radius \(|s/c|\) centred at \(a=(-s/c,0)\), with signed central-angle change \(2\pi c\). The affine holonomy of the full latitude is the rotation
\[
F(v)=a+R(-2\pi c)(v-a).
\tag{G.5}
\]
Its unique fixed point is \(a\). At the equator it is instead the translation \(F(v)=v-(0,2\pi)\); linear holonomy there is the identity.

**Proof.** The sphere is a smooth surface with the induced positive metric by DG-CHAR-17 V.5. At a point \(q\) of the unit sphere, the orthogonal tangent projection is \(P_q(w)=w-(q\cdot w)q\), as direct dot products verify. For tangent fields define \(\nabla_XY=P_q(dY(X))\). This is smooth and obeys the derivative axioms by the product rule. Since tangent vectors are orthogonal to \(q\), projection has no effect on their inner products with \(dY(X)\); differentiating \(Y\cdot Z\) therefore proves metric compatibility. In any local sphere coordinates, the difference \(dY(X)-dX(Y)\) equals the tangent bracket: expand the fields in coordinate derivatives and cancel the symmetric second derivatives of the parametrization using PB C.3. Projection fixes this tangent bracket, so torsion is zero. DG-CHAR-17 V.1 identifies this connection as the round Levi-Civita connection, on the entire sphere.

The trigonometric derivative and product identities follow from the circle exponential in Conn E.1. Dot products show that both vectors in (G.3) have norm one, are orthogonal to each other and to \(\gamma\), and have cross product \(e_\theta\times e_\phi=\gamma\). Hence the frame is tangent and outward oriented. Direct differentiation gives
\[
\dot\gamma=s e_\phi,\qquad
\nabla_{\partial_\phi}e_\theta=c e_\phi,\qquad
\nabla_{\partial_\phi}e_\phi=-c e_\theta.
\tag{G.6}
\]
For the last formula, \(e_\phi'=(-\cos\phi,-\sin\phi,0)\) has tangent components \((-c,0)\); its remaining component is normal and is removed by projection. Thus the connection matrix along the curve is \(cJ\,d\phi\).

The matrix \(R(a)\) is the real matrix of multiplication by \(\exp(ia)\). Conn E.1 gives \(R'(a)=JR(a)=R(a)J\), \(R(a+b)=R(a)R(b)\) and \(R(0)=I\). Consequently \(R(-c\phi)\) solves the horizontal frame equation of A.2 with initial value \(I\); uniqueness proves the transport assertion. The inverse transport sends the velocity to
\[
R(c\phi)(0,s)=(-s\sin(c\phi),s\cos(c\phi)).
\]
Integrating these two coordinates from zero, using Local 0.3, proves (G.4) for \(c\ne0\). If \(c=0\), then \(s=1\) and the velocity is constantly \((0,1)\), giving the second case directly without dividing by zero.

For \(c\ne0\), subtracting \(a\) from (G.4) gives \((s/c)(\cos(c\phi),\sin(c\phi))\), proving the radius and signed angle assertions, also when \(c<0\). The frame is periodic at \(2\pi\); hence linear holonomy in the initial frame is \(R(-2\pi c)\). Formula F.2 gives
\[
F(v)=R(-2\pi c)(v-d(2\pi)).
\]
Write \(r=s/c\). Since \(d(2\pi)=r(R(2\pi c)-I)(1,0)\), its constant term is \(r(R(-2\pi c)-I)(1,0)=a-R(-2\pi c)a\). This is (G.5), with its sign determined by the affine transport equation. Here \(-1<c<1\). If \(c\ne0\), then \(c\) is not an integer, so Conn E.1's period and injectivity show that \(R(-2\pi c)\ne I\). Moreover \(\det(I-R(b))=2(1-\cos b)>0\) for any nonidentity rotation, by direct multiplication and \(\cos^2b+\sin^2b=1\). Thus its fixed-point equation has the unique solution \(a\). At \(c=0\), (G.4) and F.2 give the stated nonzero translation and identity linear part. The poles are excluded because the latitude degenerates there and (G.3) no longer supplies the stated loop parametrization by a nonzero velocity. □

**Example G.3 (the specified latitudes and the equator).** At \(\theta=\pi/3\),
\[
d(\phi)=\sqrt3\bigl(\cos(\phi/2)-1,\sin(\phi/2)\bigr).
\]
The full latitude develops into a semicircle ending at \((-2\sqrt3,0)\), and its affine holonomy is the half-turn about \((-\sqrt3,0)\). At \(\theta=\pi/4\),
\[
\begin{aligned}
d(\phi)&=\bigl(\cos(\phi/\sqrt2)-1,\sin(\phi/\sqrt2)\bigr),\\
F(v)&=(-1,0)+R(-\sqrt2\pi)\bigl(v+(1,0)\bigr).
\end{aligned}
\tag{G.7}
\]
The unique fixed centre is \((-1,0)\). At \(\theta=\pi/2\), the development is the segment \((0,\phi)\), and the affine holonomy has no fixed point.

**Proof.** We justify the special trigonometric constants. The exponential of Conn E.1 has kernel \(2\pi\mathbb Z\) and traverses the circle once positively. Its value at \(\pi\) is the nonidentity solution of \(z^2=1\), hence \(-1\). On the interval \((0,\pi)\) it remains in the upper half-circle: its initial tangent at \(1\) is positive imaginary, and it cannot cross the real axis at \(1\) or \(-1\) sooner by injectivity. Therefore its value at \(\pi/2\), whose square is \(-1\), is \(i\). The value at \(\pi/4\) is the upper-half-plane root of \(z^2=i\), namely \((1+i)/\sqrt2\). The value at \(\pi/3\) is the upper-half-plane root of \(z^3=-1\), namely \((1+i\sqrt3)/2\), as direct multiplication and factorization of \(z^3+1\) verify. Positive square roots exist by Local 0.0. Thus the three pairs \((s,c)\) are \((\sqrt3/2,1/2)\), \((1/\sqrt2,1/\sqrt2)\) and \((1,0)\). Substitute into G.2. At \(\pi/3\) the central angle is \(\pi\) and the holonomy matrix is \(-I\), giving the stated endpoint and centre. At \(\pi/4\) the angle is \(\sqrt2\pi\), which gives (G.7). At the equator G.2's nonzero translation cannot fix any vector. □

## H. Projection criteria, standard fields and metric scope

These final checks connect the preceding constructions to the complete earlier programme arguments. [Curvature B.7](curvature-and-holonomy-groups.md) proves smooth homogeneity at the zero section from the freely accessible Saldaña Moncada–Weingart paper credited there; its full proof is an earlier programme provider. We spell out its consequences for complex bundles and derivatives here. No external paper is used in place of a programme proof.

**Theorem H.1 (dilations, projection and linear differentiation).** Let \(E\to M\) be a real vector bundle and \(\Phi:TE\to VE\) a smooth connection projection: on each tangent space it is linear, takes values in the vertical space, and is the identity on that space. The following are equivalent:

1. Every scalar dilation \(\Lambda_\lambda(u)=\lambda u\) is parallel, meaning \(\Phi\,d\Lambda_\lambda=d\Lambda_\lambda\,\Phi\), including \(\lambda=0\).
2. In every linear bundle chart the reduced vertical coordinate has the form
\[
\Phi(x,y;v,z)=(x,y;0,z+A_x(v)y).
\tag{H.1}
\]
3. The reduced section derivative \(\nabla_Xs=\operatorname{pr}_2\operatorname{vl}^{-1}(\Phi(ds(X)))\) is additive and real homogeneous in \(s\).

Under these conditions the reduced derivative is precisely a covariant derivative, and \(\Phi(W)=\operatorname{vl}(u,\mathscr K(W))\) for B.1's connector at \(W\in T_uE\). On a complex vector bundle these are initially real statements. The derivative is complex linear exactly when multiplication by \(i\) is also parallel; equivalently all complex scalar multiplications are parallel.

**Proof.** Tangent-space linearity and vertical normalization first give the general coordinate form
\[
\Phi(x,y;v,z)=(x,y;0,z+\Gamma(x,y)v),
\]
where \(\Gamma(x,y)\) is a smooth real linear map in the base tangent argument. A dilation sends \((v,z)\) at \((x,y)\) to \((v,\lambda z)\) at \((x,\lambda y)\). The parallelness identity is therefore exactly
\[
\Gamma(x,\lambda y)v=\lambda\Gamma(x,y)v.
\tag{H.2}
\]
Fix \(x,v\) and differentiate this identity with respect to \(\lambda\) at zero. Local 0.3 gives
\(\Gamma(x,y)v=d_y\Gamma(x,0)[y]v\).
The derivative at zero is linear in \(y\); its dependence on \(v\) is also linear, and its coefficients are smooth in \(x\). Denote this bilinear map by \(A_x(v)y\), giving (H.1). Conversely that formula immediately gives (H.2). This is the full zero-section argument, rather than an inference from homogeneity on punctured fibres.

The vertical lift identification of B.1 sends \((u,w)\) to the derivative of \(u+tw\). Hence the general reduced derivative in a chart is \(Xs+\Gamma(x,s)X\). Under (H.1) it is \(Xs+A(X)s\), proving condition 3. Conversely, at any \(x\) fix a local coordinate direction and local sections constant in the fibre coordinates near \(x\). Additivity and real homogeneity in their values make \(y\mapsto\Gamma(x,y)v\) linear. If the hypothesis is initially imposed only on global sections, multiply the constant sections and local vector field by a cutoff equal to one near \(x\), using Local 3.1, and extend by zero. Their values and derivatives at \(x\) are unchanged, so the same conclusion follows. Smooth coefficients then give (H.1). Its Leibniz and function-linearity axioms follow directly by the product rule; coordinate independence follows from the original global \(\Phi\), or from B.1's connector reconstruction. This proves all equivalences and the claimed correspondence with the connection already constructed.

For a complex bundle use its underlying real charts and let \(J\) be fibre multiplication by \(i\). Under (H.1), parallelness of \(J\) says \(A_x(v)Jy=JA_x(v)y\). This is exactly complex linearity of each real endomorphism \(A_x(v)\), since every complex scalar is \(a+bi\). The formula \(Xs+A(X)s\) then commutes with \(J\) and is complex linear in sections. Conversely complex linearity of the derivative, tested on sections constant near a point, gives that matrix commutation. Commuting with \(aI+bJ\) gives parallelness of every complex scalar, and the converse includes the real dilations and \(J\). Thus none of the real-linearity or complex-linearity assumptions is omitted. □

**Theorem H.2 (the frame coframe and standard horizontal brackets).** On \(P=\operatorname{Fr}(TM)\), the map
\[
(\theta,\omega)_u:T_uP\longrightarrow\mathbb R^n\oplus\mathfrak{gl}(n,\mathbb R)
\tag{H.3}
\]
is a linear isomorphism. Define \(B(v)\) by \(\theta(B(v))=v\), \(\omega(B(v))=0\), for constant \(v\in\mathbb R^n\). It is a smooth field, linear in \(v\), and
\[
 dR_a B(v)_u=B(a^{-1}v)_{ua},\qquad
 [\zeta_C,B(v)]=B(Cv).
\tag{H.4}
\]
For two such standard fields,
\[
\begin{aligned}
\theta([B(v),B(w)])&=-\Theta(B(v),B(w)),\\
\omega([B(v),B(w)])&=-\Omega(B(v),B(w)).
\end{aligned}
\tag{H.5}
\]
Thus torsion and curvature give respectively the horizontal and vertical components of this bracket in the coframe (H.3).

**Proof.** Conn A.2 splits a tangent vector uniquely into a horizontal vector and a fundamental vertical vector \(\zeta_C\). The map \(d\pi\) is an isomorphism from the horizontal space to \(T_xM\); composing with the frame inverse makes \(\theta\) an isomorphism on that space, by D.1. On vertical vectors \(\theta=0\) and \(\omega(\zeta_C)=C\). This proves (H.3). Smoothness of its inverse follows in local coordinates from smooth matrix inversion, Local 0.4, so \(B(v)\) is smooth and linear in \(v\).

Right translation preserves horizontality and sends the solder value to \(a^{-1}v\), by Conn A.2 and D.1. Uniqueness in (H.3) proves the first identity in (H.4). The flow of \(\zeta_C\) is \(R_{\exp(tC)}\), by Local 2.3 and the fundamental-vector definition. The pullback of \(B(v)\) by this flow is
\(dR_{\exp(-tC)}B(v)_{u\exp(tC)}=B(\exp(tC)v)_u\).
Differentiation at zero gives \(B(Cv)\). That derivative is the bracket \([\zeta_C,B(v)]\): in local coordinates differentiating \(d\varphi_{-t}Y(\varphi_t(u))\) gives \(dY(X)-dX(Y)\), the bracket formula of PB C.3, with the flow derivative justified by Local 2.1. This proves the sign in (H.4).

The functions \(\theta(B(v))\) and \(\theta(B(w))\) are constant. Curvature A.2's degree-one exterior formula therefore gives \(d\theta(B(v),B(w))=-\theta([B(v),B(w)])\). The wedge term in D.2 vanishes on two horizontal arguments, proving the first line of (H.5). Likewise \(\omega(B(v))=\omega(B(w))=0\), so the same formula and Curvature A.4 give the second line. The direct sum (H.3) identifies the two components exactly. In particular all these standard fields commute if and only if both torsion and curvature vanish: they span each horizontal space, and both two-forms are horizontal by D.1 and Curvature A.4. □

**Example H.3 (why the prescribed structure group matters).** Existence of a derivative compatible with a chosen metric, as in C.2, concerns the full frame bundle. A connection induced from a prescribed smaller frame bundle need not have that freedom. On the trivial real line over \(\mathbb R\), prescribe only its standard frame, so the principal group is \(\{1\}\), and give the line the metric \(h_x(v,w)=e^{2x}vw\). The unique connection on this prescribed principal bundle does not preserve the metric.

**Proof.** The principal bundle with this one-element group identifies with the base; its vertical tangent spaces and Lie algebra are zero. Conn A.2 forces the unique connection form to be zero and its horizontal spaces to be the entire tangent spaces. Its associated transport consequently holds the coordinate constant. The squared length of the constant section 1 is \(e^{2x}\), with nonzero derivative \(2e^{2x}\), so it is not preserved. C.3 already proves that the full-frame compatible derivative instead has potential \(dx\). The prescribed frame has length one only at \(x=0\), so its unit frames do not even cover the base and cannot constitute a reduction.

More generally, suppose a prescribed frame bundle \(P\) has a smooth principal subbundle \(Q\) consisting of exactly its frames that are orthonormal for the metric. A connection on \(P\) preserves \(Q\) by horizontal transport if and only if its associated vector transport preserves that metric. For one direction, evaluation of any transported orthonormal frame on fixed coordinates preserves all pairings, by A.2. For the other, metric-preserving transport sends every frame of \(Q\) to another orthonormal frame, remains in \(P\), and therefore remains in \(Q\) by its definition. Once such a reduction exists, this is also the parallel-reduction conclusion proved in [Reduction A.4](reduction-and-the-holonomy-theorem.md). The existence of the reduction is a genuine hypothesis; the preceding example shows why it cannot be inferred for an arbitrary prescribed group. □

**Theorem H.4 (derivations and the section-operator formulation).** Real smooth vector fields identify exactly with real-linear derivations of \(C^\infty(M,\mathbb R)\): operators \(L\) satisfying \(L(fg)=fL(g)+gL(f)\). A covariant derivative on \(E\) identifies exactly with an additive, \(\mathbb F\)-linear operator
\[
D:\Gamma(E)\longrightarrow\Omega^1(M,E),\qquad
D(fs)=df\otimes s+fDs,
\tag{H.6}
\]
where the tangent arguments of the one-form remain real in the complex case. These are first-order local operators. Additivity in the section is part of the hypothesis, not a consequence silently inferred from the displayed Leibniz rule alone.

**Proof.** A vector field differentiates functions in coordinates and is a real-linear derivation by Local 0.3. Conversely let \(L\) be such a derivation. The identity for \(1\cdot1\) gives \(L(1)=0\), hence it kills real constants. If \(f\) is zero near \(x\), choose a cutoff \(\chi=1\) near \(x\) supported in that neighbourhood, using Local 3.1. Since \(\chi f=0\), evaluating \(L(\chi f)=\chi Lf+fL\chi\) at \(x\) gives \(Lf(x)=0\). This proves locality and defines \(L\) on local functions by supported extension, independently of that extension. Choosing one cutoff on a smaller neighbourhood proves that this local operator still has smooth values.

In a coordinate ball, for a fixed point \(x\) and \(y\) sufficiently close to it, the segment from \(x\) to \(y\) lies in the ball and Local 0.3 gives
\[
f(y)-f(x)=\sum_i(y^i-x^i)h_i(y),\qquad
h_i(y)=\int_0^1\partial_i f(x+t(y-x))\,dt.
\]
The functions \(h_i\) are smooth: the chain rule gives every parameter derivative of the integrand, and the uniform estimates on a compact segment in Local 0.3 justify differentiation under this integral on a smaller ball. They satisfy \(h_i(x)=\partial_i f(x)\). Apply \(L\), evaluate at \(x\), and use the product rule and vanishing of \(y^i-x^i\) there. The result is
\[
Lf(x)=\sum_i L(y^i)(x)\,\partial_i f(x).
\]
The coefficients \(L(y^i)\) are smooth. Thus they define a smooth vector field in this chart. The formulas agree on overlaps because their action on every local function is \(L\); coordinate functions determine each tangent vector. This gives a global field, uniquely, and proves that the two constructions are inverse and depend only on the first derivative of the function.

For the connection statement set \((Ds)(X)=\nabla_Xs\). A.1 proves dependence only on the tangent value of \(X\); in a frame its formula \(Ds=e(ds_e+As_e)\) is a smooth \(E\)-valued one-form. Additivity and constant \(\mathbb F\)-linearity, together with (H.6), are the derivative axioms of A.1. Conversely define \(\nabla_Xs=(Ds)(X)\) from an operator as in (H.6). A one-form is linear over real smooth functions in \(X\), while the asserted properties of \(D\) give additivity, constant \(\mathbb F\)-linearity in \(s\), and the required Leibniz rule. Hence these are the covariant-derivative axioms, and the constructions are inverse. A.1 now proves locality and the first-jet formula, also over \(\mathbb C\). □

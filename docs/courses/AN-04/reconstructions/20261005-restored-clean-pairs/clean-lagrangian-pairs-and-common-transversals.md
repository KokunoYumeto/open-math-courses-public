# Clean Lagrangian pairs and common transversals

Two conic Lagrangians through the same nonzero covector always share a radial tangent direction. Their intersection therefore cannot be transverse. Clean intersection is the condition that lets us straighten both submanifolds at once: the actual intersection must be smooth, and its tangent space must be exactly the intersection of their tangent spaces. We prove the simultaneous homogeneous normal form, then construct a Lagrangian plane transverse to both tangent planes.

Our conventions are \(\omega=\sum_j dp_j\wedge dq_j\), \(\iota_{H_f}\omega=-df\), and \(\{f,g\}=H_fg\). The prerequisites are the full coordinate-extension, isotropic fiber and conormal-germ theorems in [Prescribed canonical coordinates and isotropic fibers](../20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md). The exact smooth-calculus proofs are [P2–P3, inverse and implicit functions](../20261004-free-stationary-phase/prerequisite-completions.md) and [F0–F1, tangent flows, transversality and commuting fields](../20261005-restored-submanifolds/flows-constant-rank-and-leaves.md), with the complete [finite-coordinate flow construction](../20261005-restored-phase-space/finite-coordinate-flows.md). The preceding lesson's Theorem 5.1 includes the full constant-rank map proof. The [differential-form foundation](../20261005-restored-phase-space/differential-forms-and-flow-pullbacks.md) proves exterior differentiation, pullback and the radial primitive formula. The [proof map](proof-map.json) binds every used programme proof and its earlier inputs. No pseudodifferential estimate or additional external course import is used.

The primary source is the reprint of Hörmander III, second edition (1994), Theorem 21.2.10 and Corollary 21.2.11, printed 288–289 / PDF 303–304. We supply the clean-pair coordinate construction, the common defining functions, the radial dimension counts, and an explicit change of the full homogeneous coordinate system. Every nonlinear normal-form assertion below is local, as an equality of germs near the marked point or ray.

## 1. Clean intersection gives an actual simultaneous smooth chart

Let \(V_1,V_2\) be embedded submanifolds of a smooth \(m\)-manifold, of dimensions \(a,b\). They intersect **cleanly near \(c\)** if their intersection \(I\) is an embedded submanifold near \(c\), of fixed dimension \(k\), and
\[
 T_zI=T_zV_1\cap T_zV_2\qquad(z\in I\text{ near }c).
 \tag{1.1}
\]
The condition concerns a neighborhood in the intersection. Merely finding a tangent-space intersection of some dimension at one point does not assert cleanliness.

**Lemma 1.1 (smooth pair chart).** A clean pair has local coordinates
\[
 (u,v,w,z)\in
 \mathbb R^k\times\mathbb R^{a-k}\times
 \mathbb R^{b-k}\times\mathbb R^{m-a-b+k}
 \tag{1.2}
\]
in which \(V_1=\{w=z=0\}\), \(V_2=\{v=z=0\}\), and \(I=\{v=w=z=0\}\).

**Proof.** Choose one parameterization \(i(u)\) of \(I\). Extend it to parameterizations \(F_1(u,v)\) of \(V_1\) and \(F_2(u,w)\) of \(V_2\), so that both agree with \(i(u)\) at their zero second argument. To construct these extensions, choose coordinates \(\psi_i\) on \(V_i\) near \(c\), and write \(a_i(u)=\psi_i(i(u))\). This map has injective differential: in an ambient chart adapted to \(V_i\), the smooth inclusion of \(I\) is represented by its first \(\dim V_i\) coordinate functions and has the original injective tangent map. Choose a fixed linear map \(Z_i:\mathbb R^{\dim V_i-k}\to\mathbb R^{\dim V_i}\) complementing the range of \(Da_i(0)\). Then \((u,v)\mapsto a_i(u)+Z_i v\) has invertible differential at the origin. The inverse function theorem makes it a local coordinate map, and \(F_i(u,v)=\psi_i^{-1}(a_i(u)+Z_i v)\) gives the required extension, including when the complementary block is empty. Work in an ordinary ambient coordinate chart and choose a fixed linear injection \(Z\) whose range complements \(T_cV_1+T_cV_2\). Its dimension is \(m-a-b+k\), by (1.1). Define
\[
 F(u,v,w,z)=F_1(u,v)+F_2(u,w)-i(u)+Zz.
 \tag{1.3}
\]
At the origin, the \(u\) derivative spans \(T_cI\), the \(v\) and \(w\) derivatives supply complementary parts of the two tangent spaces, and the \(z\) derivative supplies the ambient complement. Condition (1.1) makes their direct sum the entire tangent space. Thus \(DF\) is invertible.

The inverse function theorem makes \(F\) a local diffeomorphism. On \(w=z=0\) it equals \(F_1\), and on \(v=z=0\) it equals \(F_2\). These restrictions parameterize open neighborhoods of \(c\) in the respective submanifolds. After shrinking, they give equalities of germs, not just containments. Their intersection is the \(u\)-plane. \(\square\)

The common functions \(z_1,\ldots,z_{m-a-b+k}\) vanish on both submanifolds. Their independent differentials span the annihilator of \(T_cV_1+T_cV_2\). There may also be nonlinear functions vanishing on both, but the indicated list already supplies the entire common conormal space at the marked point.

## 2. Remove the radial direction without losing cleanliness

Let \(S\) be a conic symplectic manifold of dimension \(2n\), with dilation generator \(R\ne0\), and let \(V_1,V_2\) be conic Lagrangians meeting cleanly. Write \(I=V_1\cap V_2\), \(\dim I=k\). Since \(R\) is tangent to both,
\[
 1\leq k\leq n,\qquad R\in TI.
 \tag{2.1}
\]
In particular this is not the dimension range for arbitrary linear Lagrangian pairs, which may have zero-dimensional intersection.

Choose a positive degree-one ray coordinate \(\rho\), rescaled so \(\rho(c)=1\), and a transverse section \(\Sigma=\{\rho=1\}\). Local conic coordinates are \((t,s)\mapsto M_t(s)\) for \(s\in\Sigma\). For any one of \(V_1,V_2,I\), dilation invariance gives a local product with its intersection with \(\Sigma\). At a point of this section its tangent space splits as
\[
 T_zV_i=\mathbb R R(z)\oplus T_z(V_i\cap\Sigma),\qquad
 T_zI=\mathbb R R(z)\oplus T_z(I\cap\Sigma).
 \tag{2.2}
\]
Indeed \(d\rho(R)=\rho=1\); subtracting \(d\rho(v)R\) from a tangent vector \(v\) produces its unique tangent component in \(\Sigma\). Thus intersecting the two splittings proves that the slice pair is clean. Its dimensions are
\[
 \dim\Sigma=2n-1,\qquad
 \dim(V_i\cap\Sigma)=n-1,\qquad
 \dim(I\cap\Sigma)=k-1.
 \tag{2.3}
\]

Lemma 1.1 on \(\Sigma\) consequently has
\[
 (2n-1)-2(n-1)+(k-1)=k
 \tag{2.4}
\]
common normal coordinates \(z_j\). Extend them constantly along rays and put \(f_j=\rho z_j\). These are degree-one smooth functions vanishing on both \(V_i\). At \(c\), because \(z_j(c)=0\),
\[
 df_j(c)=\rho(c)\,dz_j(c).
 \tag{2.5}
\]
They are independent, annihilate \(T_cV_1+T_cV_2\), and their Hamilton vectors span
\[
 (T_cV_1+T_cV_2)^\omega
 =(T_cV_1)^\omega\cap(T_cV_2)^\omega
 =T_cV_1\cap T_cV_2=T_cI.
 \tag{2.6}
\]
Here each Lagrangian plane equals its symplectic orthogonal. On either entire submanifold, a function vanishing there has Hamilton field tangent there, by the same orthogonality argument. Thus every \(H_{f_j}\) preserves both submanifolds by its local flow. When \(k>1\), their span has a vector independent of \(R(c)\); choose a constant linear combination \(f\) with that property. It still has degree one and vanishes on both germs.

## 3. Straighten both conic Lagrangians

We will use the full cotangent lift of a base coordinate change. For \(Q=\psi(q)\), with invertible derivative \(J=D\psi(q)\), set \(P=J^{-T}p\). Its inverse is \(q=\psi^{-1}(Q)\), \(p=D\psi(\psi^{-1}(Q))^T P\). Matrix inversion and the inverse function theorem prove that both maps are smooth. The exact identity \(P\cdot dQ=P^TJ\,dq=p\cdot dq\) proves primitive preservation; exterior differentiation proves symplecticity. The map commutes with positive covector dilation, and sends the entire local fiber over \(q_0\) onto the fiber over \(\psi(q_0)\). For a linear base map one can send any fixed nonzero covector to \(e_1\): choose the first row to be that covector and extend it to a basis of row covectors. Then \(J^Te_1=p_0\), so \(J^{-T}p_0=e_1\).

**Theorem 3.1 (clean conic pair).** Under the assumptions of Section 2, there is a homogeneous symplectomorphism to a conic neighborhood of \((0,e_1)\in T^*\mathbb R^n\setminus0\), where \(e_1=(1,0,\ldots,0)\), such that
\[
 \begin{aligned}
 V_1&=\{Q_1=\cdots=Q_n=0\},\\
 V_2&=\{Q_1=\cdots=Q_k=0,\quad
                  P_{k+1}=\cdots=P_n=0\}.
 \end{aligned}
 \tag{3.1}
\]
The intersection has free first \(k\) momenta and has dimension \(k\). Positions have degree zero and momenta degree one. The map preserves the canonical primitive \(\lambda=\iota_R\omega\) as well as the symplectic form.

**Proof, base case \(k=1\).** The isotropic fiber theorem from the preceding lesson first makes \(V_1\) a full cotangent fiber \(q=0\). A linear change of the base, with its cotangent lift, can put the marked nonzero covector at \(e_1\); this does not change that fiber. At the marked point,
\[
 \ker(d\pi|_{T_cV_2})=T_cV_2\cap T_cV_1=T_cI=\mathbb R R(c).
 \tag{3.2}
\]
Therefore \(\pi|_{V_2}\) has rank \(n-1\) at \(c\). A nonzero minor keeps its rank at least \(n-1\) on a neighborhood in \(V_2\). The radial field is a nonzero kernel vector at every point of that neighborhood, so the rank is at most \(n-1\) there. It is genuinely constant near \(c\).

The conormal-recognition theorem from the preceding lesson now identifies \(V_2\) with a local germ of \(N^*Y\setminus0\), where \(Y\) is an embedded hypersurface through the base origin. Choose a defining function \(h\) for \(Y\). The marked covector is \(\alpha\,dh(0)\) for a nonzero real \(\alpha\). Take \(Q_1=\alpha h\) and complete it to a base coordinate system with all \(Q_j(0)=0\). Explicitly, complete the nonzero covector \(\alpha\,dh(0)\) to a basis using constant linear covectors, take their linear functions vanishing at zero as \(Q_2,\ldots,Q_n\), and apply the inverse function theorem. This works for either sign of \(\alpha\); it does not reverse the positive dilation parameter. Its cotangent lift satisfies \(\xi=\sum_jP_j\,dQ_j\); hence the marked momentum becomes \(P=e_1\). The same lift leaves \(V_1\) a fiber and sends \(V_2\) to
\[
 Q_1=0,\qquad P_2=\cdots=P_n=0.
 \tag{3.3}
\]
Both are equalities of germs, including the permitted directions near the marked normal ray. The case \(n=1\) is included: the hypersurface is a point and both germs are the same local fiber.

**Induction step \(k>1\).** Use the degree-one common function \(f\) from Section 2, with \(H_f(c)\) independent of \(R(c)\). The homogeneous prescribed-coordinate theorem applies with \(f\) as the last momentum \(p_n\). Choose all marked positions zero, \(p_1(c)=1\), and all other marked momenta zero. This is allowed because \(n\geq k>1\), the only prescribed momentum has value zero, and no position has been prescribed. Shrink to \(p_1>0\).

Now \(p_n=0\) on both \(V_i\), and \(H_f=H_{p_n}=\partial_{q_n}\) is tangent to both. Each \(V_i\) is consequently a genuine local position cylinder. In fact the flow \(q_n\mapsto q_n+t\) preserves it; flowing a point to \(q_n=0\) and back gives
\[
 V_i=\{\text{small }q_n\text{ interval}\}\times W_i,
 \qquad W_i=V_i\cap\{q_n=p_n=0\}.
 \tag{3.4}
\]
This equality follows from flow uniqueness and transversality to \(q_n=0\), rather than from a tangent-space count alone.

The section \(S_0=\{q_n=p_n=0\}\) is a conic symplectic manifold of dimension \(2(n-1)\), with form \(\omega_0=\sum_{j<n}dp_j\wedge dq_j\). Each \(W_i\) is conic Lagrangian of dimension \(n-1\): its tangent lies in the section, is isotropic for the restricted form, and has half the section dimension. Its radial field is nonzero since \(p_1>0\).

The intersection \(I\) is itself a cylinder, with the same \(q_n\) direction. The intersection \(J=W_1\cap W_2\) has dimension \(k-1\). Splitting \(\partial_{q_n}\) off the tangent spaces gives
\[
 \begin{aligned}
 T_zV_i&=\mathbb R\partial_{q_n}\oplus T_zW_i,\\
 T_zI&=\mathbb R\partial_{q_n}\oplus T_zJ,\\
 T_zJ&=T_zW_1\cap T_zW_2.
 \end{aligned}
 \tag{3.5}
\]
The product description also makes \(J\) an actual embedded submanifold. Thus the reduced pair is clean, including at nearby intersection points.

Induct on \(k\), applying the theorem to \(W_1,W_2\) in \(S_0\). Extend that homogeneous canonical map to the full coordinate neighborhood by the identity on \((q_n,p_n)\). This is a symplectic product extension: the reduced map preserves \(\omega_0\), the unchanged pair preserves \(dp_n\wedge dq_n\), and its full inverse is the reduced inverse times the identity. All reduced positions and momenta have the required degrees under simultaneous dilation, while the unchanged pair already has them. It retains the marked point. Choose the domain to be the reduced conic domain times the removed coordinate pair, then restrict to a conic neighborhood of the marked ray with the retained covector nonzero. The extension and its inverse are defined throughout that neighborhood. Relabel its reduced coordinates \((q_j,p_j)\), \(j<n\). The two full auxiliary models are
\[
 \begin{aligned}
 V_1&=\{q_1=\cdots=q_{n-1}=0,\quad p_n=0\},\\
 V_2&=\{q_1=\cdots=q_{k-1}=0,\quad p_k=\cdots=p_n=0\}.
 \end{aligned}
 \tag{3.6}
\]
The free \(q_n\) position has not yet become a fiber direction. The next explicit map completes the induction.

**Simultaneous homogeneous model change.** On \(p_1>0\), set
\[
 \begin{aligned}
 Q_1&=q_1+q_np_n/p_1,&\quad P_1&=p_1,\\
 Q_n&=p_n/p_1,& P_n&=-q_np_1,\\
 Q_j&=q_j,& P_j&=p_j\quad(2\leq j<n).
 \end{aligned}
 \tag{3.7}
\]
Every \(Q_j\) has degree zero and every \(P_j\) has degree one. The inverse is
\[
 q_n=-P_n/P_1,\qquad p_n=Q_nP_1,\qquad
 q_1=Q_1+P_nQ_n/P_1,
 \tag{3.8}
\]
with \(p_1=P_1\) and the other pairs unchanged. Both maps are smooth on the positive-momentum neighborhoods. Direct differentiation gives the full primitive identity
\[
 P_1\,dQ_1+P_n\,dQ_n=p_1\,dq_1+p_n\,dq_n.
 \tag{3.9}
\]
The added terms \(q_n\,dp_n-(q_np_n/p_1)dp_1\) in the first summand cancel the same terms with opposite signs in the second. Differentiating (3.9), and adding the unchanged pairs, proves symplecticity. The marked point remains \((0,e_1)\).

On both models (3.6), \(p_n=0\), so \(Q_n=0\) and \(Q_1=q_1\). The first image is exactly \(Q_1=\cdots=Q_n=0\); its previously free \(q_n\) becomes the free momentum \(P_n\). The second image is exactly
\[
 Q_1=\cdots=Q_{k-1}=Q_n=0,\qquad
 P_k=\cdots=P_{n-1}=0.
 \tag{3.10}
\]
The inverse (3.8) verifies both reverse containments. Finally order the paired indices as
\[
 1,\ldots,k-1,n,k,\ldots,n-1.
 \tag{3.11}
\]
This simultaneous permutation of positions and momenta preserves both their degrees and the primitive. It moves the distinguished zero position \(Q_n\) into index \(k\), and (3.10) becomes the second model in (3.1). The first remains a fiber. When \(k=n\), the permutation is the identity and the two models coincide, as expected for a full-dimensional clean intersection. This completes the induction. \(\square\)

A literal exchange of \(q_n\) and \(p_n\) would violate their homogeneous degrees. The denominator and companion correction in (3.7) are essential; a tangent-space exchange alone does not give this conic chart.

## 4. Linear pairs and a common transverse Lagrangian plane

Let \(A,B\) be Lagrangian subspaces of a symplectic vector space \(E\), \(\dim E=2n\), and put \(K=A\cap B\), \(\dim K=k\). Here \(0\leq k\leq n\).

**Lemma 4.1 (linear pair form).** There is a symplectic linear coordinate system in which
\[
 A=\{Q=0\},\qquad B=\{Q'=0,\ P''=0\},
 \tag{4.1}
\]
where primes denote indices \(1,\ldots,k\) and double primes \(k+1,\ldots,n\).

**Proof.** Choose a basis \(\varepsilon_1,\ldots,\varepsilon_k\) of \(K\) and extend it to \(\varepsilon_1,\ldots,\varepsilon_n\) in \(A\). The form induces a perfect pairing
\[
 A/K\ \times\ B/K\longrightarrow\mathbb R.
 \tag{4.2}
\]
It is well defined because \(K\subset A\cap B\) pairs to zero with either Lagrangian. If a vector \(a\in A\) pairs to zero with all of \(B\), then \(a\in B^\omega=B\), so its class in \(A/K\) is zero. The analogous assertion holds in the other argument, and both quotient dimensions are \(n-k\). Thus the pairing is nondegenerate.

Choose representatives \(e_{k+1},\ldots,e_n\in B\) dual to the quotient basis, with \(\omega(\varepsilon_i,e_j)=\delta_{ij}\) for \(i,j>k\). All their other pairings with the chosen vectors are zero: both individual subspaces are isotropic, and \(K\) is common. Their span \(U=A+B\) is therefore isometric, for the possibly degenerate restricted alternating form, to the standard span of all vertical vectors and the last \(n-k\) horizontal vectors. The alternating-subspace extension lemma proved in the preceding lesson extends this isometry to a full symplectic isomorphism. It takes \(A,B\) to (4.1). This includes the empty quotient case \(k=n\) and the zero-intersection case \(k=0\). \(\square\)

**Corollary 4.2 (common transverse plane).** There exists a Lagrangian subspace \(L\subset E\) transverse to both \(A\) and \(B\).

**Proof.** In the model (4.1), take
\[
 L=\{P'=0,\quad P''=Q''\}.
 \tag{4.3}
\]
The free variables \(Q',Q''\) give dimension \(n\). Pulling the symplectic form back to \(L\) gives zero: the primed momentum differentials vanish, and each double-primed term is \(dQ_j\wedge dQ_j=0\). Hence \(L\) is Lagrangian.

In \(L\cap A\), all positions vanish, and (4.3) forces all momenta to vanish. In \(L\cap B\), the primed positions and double-primed momenta vanish; (4.3) forces the remaining positions and momenta to vanish as well. Both intersections are zero. Since the spaces have dimension \(n\), this is precisely transversality in dimension \(2n\). Pull \(L\) back by the symplectic isomorphism of Lemma 4.1. For \(k=0\), (4.3) is the diagonal \(P=Q\); for \(k=n\), it is the horizontal plane \(P=0\). \(\square\)

At a marked point of the nonlinear clean pair, this corollary supplies a plane transverse to both tangent planes. It asserts a linear choice at that point; a global field of common transversals or a global canonical chart would require additional construction and is not claimed here.

## 5. Ordinary clean pairs and a concrete curved example

For clarity, the ordinary smooth normal form has no radial restriction.

**Theorem 5.1 (ordinary clean pair).** Two embedded Lagrangians in a symplectic \(2n\)-manifold, meeting cleanly in dimension \(k\), \(0\leq k\leq n\), have simultaneous ordinary symplectic coordinates with models (3.1), marked point \((0,0)\).

**Proof.** First obtain an ordinary fiber chart for \(V_1\). Here is a local construction using only the ordinary prescribed-coordinate theorem. If \(n>0\), choose a defining function \(f\) of \(V_1\) with \(df(c)\ne0\), make it the last momentum, and make the marked coordinates zero. Its Hamilton field is tangent to \(V_1\), so the same cylinder argument as (3.4) reduces the Lagrangian dimension by one. Induct, extending the reduced symplectic chart by the cylinder pair. The ordinary exchange \(Q_n=p_n,\ P_n=-q_n\) turns that cylinder into a fiber direction. It preserves \(dp_n\wedge dq_n\). The dimension-zero starting case is a point. Thus the full ordinary fiber chart is proved.

When \(k=0\), the projection of \(V_2\) to the base in that chart has invertible differential at the marked point. It is therefore a graph \(p=\alpha(q)\) near the point. The Lagrangian identity implies \(d\alpha=0\). On a small star-shaped base neighborhood, the explicit function
\[
 F(q)=\int_0^1\alpha(tq)\cdot q\,dt
 \tag{5.1}
\]
satisfies \(dF=\alpha\). Here is the component calculation. Smoothness on the compact integration interval permits differentiation under the integral, as in the parameter fundamental-theorem proof. It gives \(\partial_jF=\int_0^1[\alpha_j(tq)+t\sum_iq_i\partial_j\alpha_i(tq)]\,dt\). Since \(d\alpha=0\), replace \(\partial_j\alpha_i\) by \(\partial_i\alpha_j\); the integrand is then \(\frac{d}{dt}[t\alpha_j(tq)]\). The fundamental theorem gives \(\partial_jF=\alpha_j(q)\), because the endpoint at \(t=0\) vanishes. This proves every component of the asserted identity. The momentum translation \(P=p-dF(q)\), \(Q=q\), is symplectic because its primitive changes by \(-dF\). It leaves the entire first fiber at \(q=0\) a fiber, sends \(V_2\) to \(P=0\), and keeps the marked momentum zero since \(\alpha(0)=0\).

For \(k>0\), Lemma 1.1 in the full ambient manifold supplies \(k\) independent common defining functions. Choose any one with nonzero differential and normalize it as \(p_n\) by ordinary prescribed coordinates, with all marked values zero. Its Hamilton field is tangent to both Lagrangians, so both are cylinders. The reduced pair is clean of dimensions \(n-1,n-1,k-1\), by the same actual product and tangent splitting as (3.4)-(3.5). Induct and extend by the cylinder pair. The full auxiliary models are (3.6). Now use the ordinary exchange
\[
 Q_n=p_n,\qquad P_n=-q_n,
 \tag{5.2}
\]
keeping all other pairs fixed. Both model images have \(Q_n=0\); the first is a fiber and the second has (3.10). The paired permutation (3.11) gives (3.1). The exchange changes the primitive by \(-d(q_np_n)\) and preserves its exterior derivative. This completes the ordinary proof. \(\square\)

The momentum translation and exchange in this proof are ordinary operations. The conic proof used degree-one common functions and (3.7) instead; it proves exact primitive preservation and requires \(k\geq1\).

**Example 5.2 (a curved conormal meeting a fiber).** In \(T^*\mathbb R^3\setminus0\), take the fiber \(V_1\) over the origin and the positive conormal germ \(V_2\) of
\[
 Y=\{x_1=x_2^2+x_3^3\},\qquad
 \xi=\rho(1,-2x_2,-3x_3^2),\quad \rho>0.
 \tag{5.3}
\]
The intersection is the positive ray \(x=0,\ \xi=\rho e_1\). The conormal parameterization has coordinates \((x_2,x_3,\rho)\). At a point of that ray, its two base derivatives have nonzero, independent base components, while the radial derivative is vertical. Consequently its tangent intersection with the first fiber is exactly the radial line, so the intersection is clean with \(k=1\).

Flatten the hypersurface by
\[
 Q_1=x_1-x_2^2-x_3^3,\quad Q_2=x_2,\quad Q_3=x_3.
 \tag{5.4}
\]
The full cotangent lift is
\[
 P_1=\xi_1,\qquad
 P_2=\xi_2+2x_2\xi_1,\qquad
 P_3=\xi_3+3x_3^2\xi_1.
 \tag{5.5}
\]
Indeed \(\sum_jP_jdQ_j=\sum_j\xi_jdx_j\). It is homogeneous and invertible, with \(x_1=Q_1+Q_2^2+Q_3^3\) and the obvious reversed momentum formulas. It retains the origin fiber and takes (5.3) to \(Q_1=0,\ P_2=P_3=0,\ P_1>0\), exactly the theorem's model near \((0,e_1)\).

**Example 5.3 (a smooth intersection that is not clean).** In \(\mathbb R^2\) with coordinates \((q,p)\), the two Lagrangian curves \(A=\{p=0\}\) and \(B=\{p=q^2\}\) intersect in the single point \((0,0)\). This is a smooth zero-dimensional intersection, but both tangent lines there are horizontal. Their tangent intersection has dimension one, rather than zero. No local diffeomorphism can turn this pair into the clean \(k=0\) model: the derivative would preserve their coincident tangent lines, whereas the model tangent lines are transverse. Smoothness of the set-theoretic intersection alone is insufficient.

## 6. Graded exercises with complete solutions

**Exercise 6.1 (common normal count; foundational).** Two \(n\)-dimensional submanifolds of a \(2n\)-manifold intersect cleanly in dimension \(k\). Count the common normal coordinates in Lemma 1.1. Repeat on a ray slice in the conic case. Explain why the conic answer is not \(k-1\).

**Solution.** In the full manifold the number is \(2n-n-n+k=k\). On the ray slice the ambient dimension is \(2n-1\), each submanifold dimension is \(n-1\), and the intersection dimension is \(k-1\). Thus the number is \((2n-1)-2(n-1)+(k-1)=k\) again. Removing one common tangent direction also removes one ambient direction and one tangent direction from each of the two submanifolds. It does not remove a common normal dimension.

**Exercise 6.2 (common Hamilton span; foundational).** For Lagrangian planes \(A,B\) with \(\dim(A\cap B)=k\), prove \((A+B)^\omega=A\cap B\). Deduce the Hamilton span of the common defining functions, and justify the choice of a field independent of the radial vector when \(k>1\).

**Solution.** A vector is orthogonal to \(A+B\) exactly when it is orthogonal to both summands. Since \(A^\omega=A\) and \(B^\omega=B\), this is precisely \(A\cap B\). The symplectic identification \(df\mapsto H_f\) takes the annihilator of \(A+B\) onto this space, so independent common normal differentials give a basis of its \(k\)-dimensional Hamilton span. A nonzero radial vector lies in that span. If \(k>1\), the whole span cannot equal its one-dimensional radial subspace; some constant linear combination supplies an independent vector.

**Exercise 6.3 (the base-case rank is locally constant; intermediate).** After straightening the first conic Lagrangian to a fiber, assume the clean intersection has dimension one at the marked point. Establish the constant-rank hypothesis needed for conormal recognition on a neighborhood of the second Lagrangian.

**Solution.** The kernel of its base projection at the marked point is its intersection with the vertical first tangent plane, which is the one-dimensional intersection tangent. Thus the rank is \(n-1\). A nonvanishing \((n-1)\)-minor remains nonvanishing nearby, so the rank cannot fall below \(n-1\). The nonzero radial field is vertical at every point of a conic Lagrangian, so the rank cannot exceed \(n-1\). These two bounds prove constant rank on a neighborhood, rather than just a numerical rank at one point. For \(n=1\), the radial bound already forces rank zero everywhere.

**Exercise 6.4 (clean reduction of cylinders; intermediate).** Suppose two cleanly intersecting Lagrangians both satisfy \(p_n=0\) and are invariant under \(\partial_{q_n}\). Prove the exact dimension and tangent-intersection assertions for the reduced pair in \(q_n=p_n=0\).

**Solution.** The flow preserves each submanifold and is transverse to \(q_n=0\). Flowing to that section and back identifies each with a position interval times an embedded \(W_i\) of dimension \(n-1\). It identifies the actual intersection with the same interval times \(J=W_1\cap W_2\), of dimension \(k-1\). The coordinate direction \(\partial_{q_n}\) splits off every tangent. Equality \(TV_1\cap TV_2=TI\) then gives \(TW_1\cap TW_2=TJ\). The section's restricted symplectic form vanishes on \(TW_i\), and \(\dim W_i\) is half its ambient dimension, so each \(W_i\) is Lagrangian. In the conic construction its radial direction survives through the positive remaining momentum.

**Exercise 6.5 (the full projective exchange; intermediate).** Verify the degrees, primitive identity, inverse, and marked-point behavior of (3.7). Explain the role of \(Q_1\)'s correction term.

**Solution.** The ratio \(p_n/p_1\) and the product \(q_np_n/p_1\) have degree zero, while \(-q_np_1\) has degree one. Solving first for \(p_1\), then \(q_n,p_n,q_1\), gives (3.8). It is smooth on \(P_1>0\). Differentiation yields
\[
 \begin{aligned}
 P_1dQ_1&=p_1dq_1+p_ndq_n+q_ndp_n
                    -(q_np_n/p_1)dp_1,\\
 P_ndQ_n&=-q_ndp_n+(q_np_n/p_1)dp_1.
 \end{aligned}
 \tag{6.1}
\]
Their sum is exactly \(p_1dq_1+p_ndq_n\). Without the correction term in \(Q_1\), the first row would be just \(p_1dq_1\), and the cancellation would fail. At \(q=0,p=e_1\), every added term vanishes and the marked point remains unchanged.

**Exercise 6.6 (both model images; intermediate).** For \(n=4,k=3\), carry both auxiliary models (3.6) through (3.7) and the paired permutation, proving equalities of model germs.

**Solution.** Initially \(V_1\) has \(q_1=q_2=q_3=0,p_4=0\), and \(V_2\) has \(q_1=q_2=0,p_3=p_4=0\). Since \(p_4=0\) on both, their images have \(Q_4=0,Q_1=q_1\). The first has all \(Q_j=0\); the free \(q_4\) supplies free \(P_4=-q_4p_1\). The second has \(Q_1=Q_2=Q_4=0,P_3=0\). Order the pairs as \(1,2,4,3\): then its first three positions and last momentum vanish, exactly the required second model. Inserting these image equations into (3.8) recovers every original defining equation and permits all original free variables locally. This proves both reverse containments. The first three final momenta parameterize the common intersection.

**Exercise 6.7 (common transversals, including empty blocks; foundational).** Verify (4.3) is Lagrangian and transverse to both model planes for every \(0\leq k\leq n\). Identify its form at both endpoints.

**Solution.** Parameterize it by \(Q\), with \(P'=0,P''=Q''\). The pullback form is zero and there are \(n\) parameters. In the first model all positions vanish, forcing \(P=0\). In the second model \(Q'=0,P''=0\), which also forces \(Q''=0,P'=0\). Thus either intersection consists of zero alone. At \(k=0\), all indices are double primed and the transversal is \(P=Q\), diagonal between the vertical and horizontal planes. At \(k=n\), all indices are primed and it is \(P=0\), horizontal and transverse to the coinciding vertical planes.

**Exercise 6.8 (flatten a curved hypersurface; intermediate).** Derive (5.5) from (5.4), write the complete inverse momentum formulas, and verify cleanliness and marked-covector normalization for Example 5.2.

**Solution.** Expand \(\sum P_jdQ_j\). Its \(dx_1\) coefficient is \(P_1\), its \(dx_2\) coefficient is \(P_2-2x_2P_1\), and its \(dx_3\) coefficient is \(P_3-3x_3^2P_1\), giving (5.5). Conversely \(\xi_1=P_1,\xi_2=P_2-2Q_2P_1,\xi_3=P_3-3Q_3^2P_1\), with the inverse base map stated after (5.5). At the origin the two tangent derivatives of the conormal parameterization have independent base directions, so their combination is vertical only when both coefficients vanish. The remaining radial derivative spans the common tangent. The actual intersection is the positive ray, with that tangent, proving cleanliness along it. The point \((0,e_1)\) is fixed and its conormal coefficient is \(P_1=1\).

**Exercise 6.9 (an ordinary exact translation; intermediate).** Let \(V_1\) be the fiber at zero in \(T^*\mathbb R^2\), and let \(V_2\) be the graph of \(dF\), where \(F(q)=q_1q_2^2+q_1^3\). Show the pair is clean with \(k=0\) and find its simultaneous ordinary model. Determine the change of primitive.

**Solution.** The graph is parameterized by \(q\), with momentum \((q_2^2+3q_1^2,2q_1q_2)\); hence it meets the first fiber only at \((q,p)=(0,0)\). Its tangent projects isomorphically onto the base, so its tangent intersection with the vertical plane is zero. The intersection is therefore clean. Set \(Q=q\) and \(P=p-(q_2^2+3q_1^2,2q_1q_2)\). This invertible map retains the first fiber and sends the second to \(P=0\). Its primitive is \(P\cdot dQ=p\cdot dq-dF\), so the exterior derivative is unchanged. The nonzero added momentum functions have degree zero in \(p\), so this is not a homogeneous conic construction.

**Exercise 6.10 (nonclean tangency; foundational).** For the curves in Example 5.3, calculate the actual and tangent intersection dimensions. Prove their failure cannot be repaired by an ordinary symplectomorphism.

**Solution.** Solving \(0=q^2\) gives the singleton intersection, with tangent dimension zero. The derivatives of the parameterizations \((q,0)\) and \((q,q^2)\) at zero are both \((1,0)\). Their tangent intersection is therefore one dimensional. The derivative of any diffeomorphism is an invertible linear map, so it preserves that tangent-intersection dimension and the actual dimension of the intersection. A clean pair would have those dimensions equal; no diffeomorphism, and thus no symplectomorphism, can turn this pair into such a model.

## 7. Source and validation note

The source pair theorem and common-transversal corollary occur in Hörmander III, Section 21.2. This lesson gives original expanded proofs, including the simultaneous smooth pair chart, common degree-one defining functions, an actual clean cylinder reduction, the full homogeneous model change and inverse, and an ordinary counterpart with its exact primitive corrections. The examples and graded exercises were derived for the course.

The preserved proof and its exact current programme dependencies were reviewed for this restoration; independent human mathematical review and the remaining course work are pending. Bounded exact checks test common normal and radial dimensions, homogeneous and ordinary model changes with both images, common transverse planes including empty blocks, the curved conormal lift, and the clean-versus-tangent distinction. These finite checks support the written proof; they do not independently certify arbitrary smooth pair charts, flow invariance, or the general induction. No source chapter closure, global simultaneous chart, or global field of transversals is claimed.

## Sources and restoration

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the second edition (1994), Theorem 21.2.10 and Corollary 21.2.11, printed 288–289 / PDF 303–304. Both full normal forms and the pointwise linear transversal statement are proved above with their precise ranges and germ qualifications.
- The [source and restoration record](source-provenance.json) identifies the edition, exact restored proof and reproducible finite checks.

Original lesson, examples and ten solutions: GPT-6.1 Sol (OpenAI), Ultra, September 2026, CC0. Restoration and exact prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original additions here are CC0. Linked components retain their individual licences. No book file or text is included.

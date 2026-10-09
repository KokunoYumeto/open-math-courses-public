# Submanifolds and hypersurfaces

An immersion supplies two kinds of information: a metric within the manifold and the way its tangent spaces turn in the ambient space. A single connection on the sum of the tangent and normal bundles keeps track of both. Its curvature gives the compatibility equations, and a flat version of that connection reconstructs the immersion.

All manifolds, maps and tensors below are smooth. Manifolds are nonempty, have no boundary unless one is specified, and are Hausdorff and second countable. Connectedness is stated where it is used. Inner products are positive definite. An immersion has injective differential; an embedding is an immersion which is a homeomorphism onto its image. Compactness includes no boundary. We use
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
\]
Thus the round sphere has positive sectional curvature. The free notes of Florit and Petersen, in the exact versions listed at the end, provide further reading. Every result used here is proved below or in the linked earlier programme lessons.

## A. Tangent and normal data

Let \(f:(M^n,g)\to(\overline M^{n+p},\bar g)\) be an isometric immersion. Work on the pullback bundle \(f^*T\overline M\), so that different points of \(M\) mapping to the same ambient point still have their own fibres. Identify \(TM\) with \(df(TM)\). Its orthogonal complement is the **normal bundle** \(N_fM\). Write \(D\) for the pulled-back ambient Levi–Civita connection.

**Proposition A.1 (The orthogonal connection blocks).** There are a metric connection \(\nabla^\perp\) on \(N_fM\), a symmetric normal-valued bilinear tensor \(\alpha\), and self-adjoint endomorphisms \(A_\xi\) of \(TM\), linear in the normal vector \(\xi\), such that
\[
\begin{aligned}
D_Xdf(Y)&=df(\nabla_XY)+\alpha(X,Y),\\
D_X\xi&=-df(A_\xi X)+\nabla^\perp_X\xi,\\
g(A_\xi X,Y)&=\bar g(\alpha(X,Y),\xi).
\end{aligned}
\tag{A.1}
\]
Here \(\nabla\) is exactly the Levi–Civita connection of \(g\). The tensor \(\alpha\) is the second fundamental form and \(A_\xi\) is the shape operator in direction \(\xi\).

**Proof.** In local coordinates an immersion supplies \(n\) independent smooth columns \(f_i=df(\partial_i)\). If \(G=(\bar g(f_i,f_j))\), their orthogonal projection is
\[
P(v)=\sum_{i,j}f_i(G^{-1})^{ij}\bar g(f_j,v).
\]
The matrix \(G\) is positive definite and has smooth inverse by the cofactor formula. Thus \(P\) is a smooth projection of constant rank, and \(I-P\) describes the smooth normal bundle. Local frames for its image can be chosen by selecting an independent minor and applying the Gram–Schmidt construction of [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2).

Define \(\nabla\), \(\alpha\) and \(\nabla^\perp\) by the two projections in the first two lines of (A.1); define \(-A_\xi X\) to be the tangent part of \(D_X\xi\). The connection rules show that the projected tangent and normal derivatives are connections. In the normal part of \(D_Xdf(hY)\), the Leibniz term \(X(h)df(Y)\) projects to zero; hence \(\alpha\) is tensorial in \(Y\), and it is already tensorial in \(X\).

The pullback connection satisfies
\[
D_Xdf(Y)-D_Ydf(X)=df([X,Y]).
\]
In coordinate tangent fields this is the equality of the mixed derivatives of the coordinate functions of \(f\), together with symmetry of the ambient Christoffel symbols; bilinearity then proves it for all fields. Its normal part makes \(\alpha\) symmetric and its tangent part makes \(\nabla\) torsion-free. Differentiating \(g(Y,Z)=\bar g(df(Y),df(Z))\) shows that \(\nabla\) preserves \(g\). Levi–Civita uniqueness, [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), identifies it. The same differentiation for normal sections proves metric compatibility of \(\nabla^\perp\).

Finally differentiate \(\bar g(\xi,df(Y))=0\). The result is
\(-g(A_\xi X,Y)+\bar g(\xi,\alpha(X,Y))=0\).
It proves the last formula, self-adjointness, tensoriality and linearity in \(\xi\). The pullback and tensor-connection rules used throughout are [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). □

Define
\[
(\nabla_X\alpha)(Y,Z)=
\nabla^\perp_X(\alpha(Y,Z))
-\alpha(\nabla_XY,Z)-\alpha(Y,\nabla_XZ).
\tag{A.2}
\]
For the shape family put
\[
(\nabla_X A)_\xi Z
=\nabla_X(A_\xi Z)-A_\xi\nabla_XZ-A_{\nabla^\perp_X\xi}Z.
\]
Differentiating the last line of (A.1) gives
\[
g((\nabla_XA)_\xi Z,W)
=\bar g((\nabla_X\alpha)(Z,W),\xi).
\tag{A.3}
\]

**Theorem A.2 (Curvature of the two blocks).** For tangent fields \(X,Y,Z,W\) and normal fields \(\xi,\eta\),
\[
\begin{aligned}
g(R(X,Y)Z,W)
&=\bar g(\bar R(dfX,dfY)dfZ,dfW)\\
&\quad+\bar g(\alpha(Y,Z),\alpha(X,W))
-\bar g(\alpha(X,Z),\alpha(Y,W)),\\
(\bar R(dfX,dfY)dfZ)^\perp
&=(\nabla_X\alpha)(Y,Z)-(\nabla_Y\alpha)(X,Z),\\
\bar g(R^\perp(X,Y)\xi,\eta)
&=\bar g(\bar R(dfX,dfY)\xi,\eta)
+g([A_\xi,A_\eta]X,Y).
\end{aligned}
\tag{A.4}
\]
These are the Gauss, Codazzi and Ricci equations. In Euclidean ambient space all terms involving \(\bar R\) vanish. In a space of constant sectional curvature \(c\), the Gauss equation adds the term \(c(g(Y,Z)X-g(X,Z)Y)\), and the Codazzi and Ricci equations have the same right-hand ambient terms, zero, as in Euclidean space.

**Proof.** Compute \(R^D(X,Y)=D_XD_Y-D_YD_X-D_{[X,Y]}\) using (A.1). On \(df(Z)\) its tangent part is
\[
df\bigl(R(X,Y)Z-A_{\alpha(Y,Z)}X+A_{\alpha(X,Z)}Y\bigr),
\tag{A.5}
\]
and its normal part is
\[
(\nabla_X\alpha)(Y,Z)-(\nabla_Y\alpha)(X,Z).
\tag{A.6}
\]
For example, the normal part before collecting terms is
\[
\alpha(X,\nabla_YZ)+\nabla^\perp_X\alpha(Y,Z)
-\alpha(Y,\nabla_XZ)-\nabla^\perp_Y\alpha(X,Z)
-\alpha([X,Y],Z).
\]
Substitute \([X,Y]=\nabla_XY-\nabla_YX\) and use symmetry of \(\alpha\) to obtain (A.6); the tangent terms collect directly into (A.5).

On \(\xi\), the normal part of the same expansion is
\[
R^\perp(X,Y)\xi-\alpha(X,A_\xi Y)+\alpha(Y,A_\xi X).
\tag{A.7}
\]
Pairing the last two terms with \(\eta\) gives
\[
-g(A_\eta X,A_\xi Y)+g(A_\eta Y,A_\xi X)
=-g([A_\xi,A_\eta]X,Y).
\]
The curvature of a pulled-back connection is the pullback of its curvature, as proved in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Thus (A.5)–(A.7) equal the corresponding components of \(\bar R(dfX,dfY)\), giving (A.4). This calculation also proves the displayed signs without any convention about a chosen unit normal.

For constant curvature, [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) gives
\(\bar R(u,v)w=c(\bar g(v,w)u-\bar g(u,w)v)\).
It is tangent when all three vectors are tangent, and vanishes when \(w\) is normal and the first two are tangent. These facts give the final assertions. □

**Proposition A.3 (Coordinates, principal curvatures and intrinsic Gaussian curvature).** For a Euclidean hypersurface of positive dimension parametrized by \(f(x^1,\ldots,x^n)\), choose a unit normal \(\nu\) locally and write
\[
g_{ij}=\langle f_i,f_j\rangle,\qquad
b_{ij}=\langle f_{ij},\nu\rangle,\qquad
f_{ij}=\Gamma^k_{ij}f_k+b_{ij}\nu.
\tag{A.8}
\]
Then \(A^i{}_j=g^{ik}b_{kj}\), \(d\nu(X)=-df(AX)\), and
\[
\Gamma^\ell_{ij}
=\tfrac12 g^{\ell k}
(\partial_i g_{jk}+\partial_jg_{ik}-\partial_k g_{ij}).
\tag{A.9}
\]
The eigenvalues \(\lambda_i\) of \(A\) are real. For a nonzero vector \(v=\sum_i v_i e_i\) in an orthonormal principal basis, its normal curvature is
\[
\frac{b(v,v)}{g(v,v)}
=\frac{\sum_i\lambda_i v_i^2}{\sum_i v_i^2}.
\tag{A.10}
\]
The mean curvature relative to \(\nu\) is \(\operatorname{tr}A/n\); the Gauss–Kronecker curvature is \(\det A\). Changing \(\nu\) to \(-\nu\) changes every \(\lambda_i\) to its negative.

For \(n=2\), Gaussian curvature is
\[
K=\det A
=\frac{b_{11}b_{22}-b_{12}^2}{g_{11}g_{22}-g_{12}^2}
=\frac{g(R(\partial_1,\partial_2)\partial_2,\partial_1)}
{g_{11}g_{22}-g_{12}^2}.
\tag{A.11}
\]
In particular it depends only on the metric, is preserved by local isometries, and is unchanged by reversing the normal.

**Proof.** A unit normal has normal derivative zero in its own normal line, because \(\langle D_X\nu,\nu\rangle=0\). Equations (A.8) and the formula for \(d\nu\) follow from A.1; pairing \(A\partial_j\) with \(\partial_i\) gives its matrix formula. Differentiate \(g_{ij}=\langle f_i,f_j\rangle\), add the equations for \(\partial_i g_{jk}\) and \(\partial_jg_{ik}\), and subtract that for \(\partial_k g_{ij}\). Equality of mixed partials leaves \(2\langle f_{ij},f_k\rangle\); multiplication by \(g^{-1}\) proves (A.9).

The self-adjoint spectral theorem, with its proof in [De Rham decomposition H.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-h-2), supplies the orthonormal eigenbasis. Expanding \(v\) gives (A.10), including the minimum and maximum principal curvatures as the extreme normal curvatures. In dimension two the expression on a unit vector \(\cos t\,e_1+\sin t\,e_2\) is \(\lambda_1\cos^2t+\lambda_2\sin^2t\). The trace, determinant and sign statements follow from the same basis and the defining relation for \(A_\nu\).

For a surface, Gauss in A.2 makes the numerator in the last expression of (A.11) equal to \(b_{11}b_{22}-b_{12}^2\); the determinant identity \(\det(g^{-1}b)=\det b/\det g\) gives the first equality. To see the metric dependence in coordinates with no extrinsic quantities, that numerator is
\[
\sum_{\ell=1}^2 g_{1\ell}
\left(
\partial_1\Gamma^\ell_{22}-\partial_2\Gamma^\ell_{12}
+\sum_{m=1}^2
(\Gamma^\ell_{1m}\Gamma^m_{22}
-\Gamma^\ell_{2m}\Gamma^m_{12})
\right).
\tag{A.12}
\]
Indeed expand the definition of \(R\) in the commuting coordinate fields, as in [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3). Formula (A.9) expresses all these coefficients through \(g\) and its derivatives. The denominator is positive because \(g\) is positive definite. Naturality of Levi–Civita curvature under a local isometry, [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), proves invariance. Reversing the normal negates \(b\) but leaves its two-dimensional determinant unchanged. □

**Proposition A.4 (The Gauss map and the projected connections).** For a Euclidean immersion \(f:M^n\to\mathbb R^{n+p}\), let
\[
\mathcal G(x)=df_x(T_xM)\in\operatorname{Gr}_n(\mathbb R^{n+p}).
\]
The tangent space to the Grassmannian at a plane \(V\) is \(\operatorname{Hom}(V,V^\perp)\), and
\[
d\mathcal G_x(X)(df_xY)=\alpha_x(X,Y).
\tag{A.13}
\]
The tangent and normal connections of the immersion are pullbacks of the projected connections on the tautological bundle and its orthogonal complement. For a cooriented hypersurface its spherical Gauss map is \(\nu:M\to S^n\), with
\[
d\nu=-df\circ A,\qquad
\nu^*g_{S^n}(X,Y)=g(AX,AY).
\tag{A.14}
\]
It is a local diffeomorphism exactly where \(A\) is invertible.

**Proof.** Fix an orthogonal splitting \(\mathbb R^{n+p}=V\oplus V^\perp\). Every nearby plane whose projection to \(V\) is invertible is the graph of a unique map \(L:V\to V^\perp\). Its entries give a chart; changes of splitting use multiplication and inversion of the appropriate invertible projection matrices, so are smooth. These charts cover all planes: choose independent coordinate projections of any basis of a plane. Topologize the planes by their orthogonal projection matrices, a subset of the Euclidean space of real matrices. It is Hausdorff and second countable in the subspace topology. For a graph the projection is \(J(J^*J)^{-1}J^*\), where \(Jv=(v,Lv)\); its dependence on \(L\) and the reverse coordinate formula by an invertible projection minor are continuous. Thus these are indeed manifold charts in that topology. This constructs the Grassmannian and identifies its tangent space at \(L=0\) with \(\operatorname{Hom}(V,V^\perp)\).

Along a curve in \(M\), choose a smooth tangent frame \(Y_i\). At the starting point, the derivative of its spanned ambient plane is the normal projection of \(D_Xdf(Y_i)\). Terms due to the change of the tangent frame itself are tangent, so the result is independent of its choice. Equation (A.1) now proves (A.13).

The tautological bundle has fibre the plane itself, inside the trivial ambient bundle; its complementary bundle has fibre the perpendicular space. If \(P\) is orthogonal projection to the plane, their connections are \(P\,d\) and \((I-P)d\). Pulling them back by \(\mathcal G\) gives exactly the projections used in A.1. One can check their curvatures directly:
\[
F^S=P(dP\wedge dP)|_S,\qquad
F^{S^\perp}=(I-P)(dP\wedge dP)|_{S^\perp}.
\tag{A.15}
\]
To prove the first formula differentiate \(P^2=P\), which gives \(P(dP)P=0\). If \(s=Ps\), then \(ds=(dP)s+Pds\), and
\((P\,d)^2s=P(dP\wedge ds)=P(dP\wedge dP)s\).
For the second replace \(P\) by \(I-P\).

In the graph chart a tangent map \(L_X\) gives
\[
(dP)_X=
\begin{pmatrix}0&L_X^*\\ L_X&0\end{pmatrix}.
\]
This follows by differentiating the projection at the zero graph, or by differentiating its symmetry and its action on vectors \(v+tL_Xv\). Hence the two curvature blocks are \(L_X^*L_Y-L_Y^*L_X\) and \(L_XL_Y^*-L_YL_X^*\). With \(L_XY=\alpha(X,Y)\), these are precisely the Euclidean Gauss and Ricci formulas of A.2. This also identifies both pulled-back connections and their signs. Finally (A.14) is A.3 followed by taking inner products. The inverse theorem, [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), proves the local-diffeomorphism assertion. □

## B. Constructing the immersion

**Lemma B.1 (Flat trivialization and a primitive).** A flat metric connection on a Euclidean vector bundle over a connected simply connected manifold has a global parallel orthonormal trivialization, uniquely specified at one point. A closed \(\mathbb R^q\)-valued one-form on that manifold has a smooth primitive, uniquely specified by its value at one point.

**Proof.** The frame-bundle connection corresponding to the vector-bundle connection is constructed in [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1). Flatness is zero curvature for that connection. [Flat connections E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1) proves path-homotopy invariance of flat transport, with a full local flat-section construction and continuation over a homotopy square. Simple connectivity therefore makes transport from a fixed point independent of the path. Transport a chosen orthonormal frame: metric compatibility preserves its inner products, and the local flat sections prove smoothness and parallelism. Every parallel section is determined by its initial value by the parallel ODE, [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2), giving uniqueness.

Here is a direct application of the same flat-transport theorem to the one-form assertion. On the trivial principal additive group bundle \(M\times\mathbb R^q\), give a lift \((\gamma(t),z(t))\) the horizontal equation
\[
z'(t)=\omega_{\gamma(t)}(\gamma'(t)).
\tag{B.1}
\]
The corresponding connection form is \(dz-\omega\); its curvature is \(-d\omega=0\), since the additive group is abelian. These statements follow from the connection and curvature formulas in [Connections A.2](connections-and-parallel-transport.md#theorem-a-2) and [Curvature and holonomy A.2](curvature-and-holonomy-groups.md#lemma-a-2). [Flat connections E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1) makes the endpoint \(z\) independent of the path on a simply connected base. Define \(F(x)\) to be that endpoint, starting with the prescribed value at the base point. In a coordinate ball it is the integral along a fixed path to its centre and then a straight coordinate segment, so it is smooth by differentiation of parameter integrals ([Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations)). Adjoining a short curve at its endpoint and differentiating (B.1) gives \(dF=\omega\). If two primitives agree at one point, their difference has zero derivative and is constant along the piecewise coordinate paths of [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4). They are equal everywhere. □

**Theorem B.2 (Euclidean realization of tangent and normal data).** Let \((M^n,g)\) be connected and simply connected. Let \(N\to M\) be a rank-\(p\) Euclidean vector bundle with a metric connection \(\nabla^\perp\), and let \(\alpha:TM\times TM\to N\) be a smooth symmetric bilinear form. Define \(A_\xi\) by
\[
g(A_\xi X,Y)=\langle\alpha(X,Y),\xi\rangle.
\]
There exists an isometric immersion \(f:M\to\mathbb R^{n+p}\), together with a fibre isometry \(j:N\to N_fM\) preserving the normal connection and second fundamental form, if and only if the Euclidean equations (A.4) hold for the prescribed data. The realization is unique up to a single Euclidean motion. Its position and any compatible isometry
\[
T_{x_0}M\oplus N_{x_0}\longrightarrow\mathbb R^{n+p}
\]
may be prescribed at one point. Every point has a neighbourhood on which \(f\) is an embedding.

In particular, for a hypersurface with a global unit normal, the data are a metric and a self-adjoint field \(A\); their necessary and sufficient equations are
\[
\begin{aligned}
R(X,Y)Z&=g(AY,Z)AX-g(AX,Z)AY,\\
(\nabla_XA)Y&=(\nabla_YA)X.
\end{aligned}
\tag{B.2}
\]

**Proof.** Necessity is A.2. For sufficiency put \(E=TM\oplus N\), with its orthogonal sum metric, and define
\[
\mathcal D_X(Z,\xi)=
\bigl(\nabla_XZ-A_\xi X,\ 
\alpha(X,Z)+\nabla^\perp_X\xi\bigr).
\tag{B.3}
\]
The connection rules are immediate from tensoriality of \(\alpha\) and \(A\). It is metric: the two off-diagonal inner-product terms cancel by the definition of \(A_\xi\), while the diagonal connections already preserve their metrics.

We verify flatness in all blocks. On \((Z,0)\), the tangent curvature component is
\[
R(X,Y)Z-A_{\alpha(Y,Z)}X+A_{\alpha(X,Z)}Y,
\]
and the normal component is
\((\nabla_X\alpha)(Y,Z)-(\nabla_Y\alpha)(X,Z)\),
by the expansion in A.2. On \((0,\xi)\), the tangent component is
\[
-(\nabla_XA)_\xi Y+(\nabla_YA)_\xi X,
\]
which vanishes by (A.3) and Codazzi after pairing with any tangent vector. The normal component is (A.7), which vanishes by Ricci after pairing with any normal vector. Thus all four blocks vanish.

Lemma B.1 provides a parallel fibre isometry
\(\Phi:E\to M\times\mathbb R^{n+p}\)
with the prescribed initial value. Its parallelism means
\[
d_X(\Phi s)=\Phi(\mathcal D_Xs).
\tag{B.4}
\]
Define the vector-valued one-form \(\omega(X)=\Phi(X,0)\). Then
\[
\begin{aligned}
d\omega(X,Y)
&=\Phi\bigl(\nabla_XY-\nabla_YX-[X,Y],\
\alpha(X,Y)-\alpha(Y,X)\bigr)=0.
\end{aligned}
\]
The first component is zero because \(\nabla\) is torsion-free, and the second because \(\alpha\) is symmetric. B.1 gives \(f\) with \(df=\omega\) and the prescribed position. The isometry property of \(\Phi\) shows that \(df\) is injective and preserves \(g\). Put \(j(\xi)=\Phi(0,\xi)\). It is perpendicular to \(df(TM)\) and has rank \(p\), so is exactly its normal bundle. Applying (B.4) first to \((Z,0)\) and then to \((0,\xi)\) gives (A.1) with second form \(j\alpha\) and normal connection \(j\nabla^\perp\). This proves all realization assertions.

Conversely any realization gives a parallel isometry \(\Phi(Z,\xi)=df(Z)+j(\xi)\) for (B.3). For two realizations, their trivializations differ by a constant orthogonal matrix: (B.4) makes the derivative of their comparison zero, and connectedness makes it constant. Their differentials therefore differ by that orthogonal matrix; integrating along paths shows that their positions differ by one additional constant translation. The initial data select both constants.

To see local embedding, choose \(n\) ambient coordinate components of \(f\) whose derivative minor is nonzero at the point. The inverse theorem ([Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion)) makes these components local coordinates on \(M\). The remaining components are smooth functions of them, so the local image is a graph, and the graph parametrization is an embedding.

For the hypersurface specialization take \(N=M\times\mathbb R\) with its standard metric connection and \(\alpha(X,Y)=g(AX,Y)\). Its normal curvature vanishes and all scalar shape operators commute, so Ricci is automatic. Gauss and Codazzi are exactly (B.2), by (A.3). The section \(1\) of \(N\) becomes the desired global unit normal. □

**Proposition B.3 (The global descent conditions).** On a connected manifold which need not be simply connected, data as in B.2 admit a realization of both the immersion and its specified normal-bundle data if and only if:

1. their connection \(\mathcal D\) in (B.3) is flat and has trivial transport around every loop;
2. in a global parallel orthonormal trivialization \(\Phi\), the closed form \(\omega(X)=\Phi(X,0)\) has zero integral around every loop.

Changing the initial orthonormal frame does not change these conditions. On the universal cover, the realization exists whenever \(\mathcal D\) is flat. Its full tangent-and-normal realization descends exactly when its associated Euclidean monodromy is the identity.

**Proof.** Trivial loop transport makes parallel transport from a base point independent of path: two paths differ by their concatenation with a reversed path, and transport of this loop is the identity. The same local flat-section argument as B.1 gives a smooth parallel \(\Phi\). The form \(\omega\) is closed by the computation in B.2. If its loop integrals vanish, define \(f(x)\) by its integral along any path from the base point; path independence and the local computation of B.1 give \(df=\omega\). Thus B.2's verification constructs the full realization. Conversely a realization produces the parallel ambient trivialization \(df\oplus j\), so its loop transport is the identity and its form is \(df\), with zero loop integrals. Any other parallel orthonormal trivialization differs by a constant orthogonal matrix, which preserves the zero-integral condition.

The universal cover and path lifting are [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) and [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3). Pulling the flat data to that cover and using B.2 produces \((\widetilde f,\widetilde j)\). For each deck transformation \(\gamma\), uniqueness in B.2 compares the transformed realization with the original one by a constant Euclidean motion
\[
\widetilde f(\gamma x)=Q_\gamma\widetilde f(x)+b_\gamma,
\qquad
\widetilde\Phi_{\gamma x}\circ\gamma_E
=Q_\gamma\widetilde\Phi_x.
\tag{B.5}
\]
Here \(\gamma_E\) is the natural deck identification of the pulled-back \(E\) fibres. Composition gives
\(Q_{\gamma\delta}=Q_\gamma Q_\delta\) and
\(b_{\gamma\delta}=Q_\gamma b_\delta+b_\gamma\);
these equalities follow first for the full fibre isometry, which spans the ambient vector space, and then for the position. Thus (B.5) is a homomorphism to the Euclidean group. The complete realization is deck-invariant exactly when \(Q_\gamma=I\) and \(b_\gamma=0\) for every \(\gamma\), since its tangent and normal images together span \(\mathbb R^{n+p}\). This is precisely descent in covering charts. The assertion concerns the specified normal identification as well as \(f\); invariance of the position alone would be a weaker condition when the image is contained in a smaller affine space. □

## C. What the curvature remembers about shape

For vectors \(u,v\) in a Euclidean space, write
\((u\wedge v)z=\langle v,z\rangle u-\langle u,z\rangle v\).
If \(u,v\) are independent, this operator has image exactly their two-plane: its restriction there has an invertible matrix in an orthonormal basis. At a Euclidean hypersurface point, Gauss reads
\[
R(X,Y)=AX\wedge AY.
\tag{C.1}
\]

**Lemma C.1 (Rank, curvature nullity and the sign ambiguity).** At a Euclidean hypersurface point, \(R=0\) if and only if \(\operatorname{rank}A\leq1\). If \(\operatorname{rank}A\geq2\), the curvature nullity
\[
\mathcal N=\{X:R(X,Y)=0\text{ for every }Y\}
\]
is \(\ker A\). If self-adjoint maps \(A,B\) have the same Gauss tensor and \(\operatorname{rank}A\geq3\), then \(B=A\) or \(B=-A\).

**Proof.** If the image of \(A\) has dimension at most one, every wedge in (C.1) vanishes. If it has dimension at least two, choose \(X,Y\) with independent images, giving a nonzero wedge. In that case \(AX=0\) certainly puts \(X\) in \(\mathcal N\); if \(AX\ne0\), choose \(Y\) with \(AY\) independent of \(AX\), so \(X\notin\mathcal N\). This proves both first assertions and shows that the rank \(n-\dim\mathcal N\) is intrinsic at a nonflat hypersurface point.

Now suppose \(A\) has rank at least three and shares its Gauss tensor with \(B\). The common tensor is nonzero, so \(B\) has rank at least two. Both kernels equal the same \(\mathcal N\); self-adjointness makes both images \(W=\mathcal N^\perp\). Their restrictions to \(W\) are invertible. With \(C=BA^{-1}:W\to W\), (C.1) becomes
\[
Cu\wedge Cv=u\wedge v\qquad(u,v\in W).
\]
Consequently \(C\) preserves every two-plane, by the image observation preceding the lemma. In dimension at least three any line is the intersection of two distinct two-planes containing it: extend a nonzero vector in the line by two independent vectors. Hence \(C\) preserves every line. Write \(Cu=a u\), \(Cv=b v\) for independent \(u,v\); applying line preservation to \(u+v\) forces \(a=b\). Comparing any two lines, with an auxiliary independent line if necessary, shows \(C=cI\). The wedge equation gives \(c^2=1\). The maps therefore equal up to this sign on \(W\), and both vanish on \(\mathcal N\), proving the result. □

**Lemma C.2 (A regular argument of a flat bilinear form).** Let \(\beta:V\times U\to W\) be bilinear on finite-dimensional real spaces, with a nondegenerate, possibly indefinite, symmetric form on \(W\). Put \(\beta_x(u)=\beta(x,u)\), and call \(x\) regular when \(\operatorname{rank}\beta_x\) is maximal. Regular arguments form an open dense set. For regular \(x\),
\[
\beta(V,\ker\beta_x)\subseteq\operatorname{Im}\beta_x.
\tag{C.2}
\]
If \(\beta\) is flat, meaning
\[
\langle\beta(x,u),\beta(y,v)\rangle
=\langle\beta(x,v),\beta(y,u)\rangle,
\tag{C.3}
\]
then the image in (C.2) lies in
\[
U_x=\operatorname{Im}\beta_x\cap(\operatorname{Im}\beta_x)^\perp.
\tag{C.4}
\]
In particular, if the form on \(W\) is positive definite,
\[
\dim\{u:\beta(V,u)=0\}\geq\dim U-\dim W.
\tag{C.5}
\]

**Proof.** Choose bases. Entries of \(\beta_x\) are linear in the coordinates of \(x\); maximal rank \(r\) is detected by some nonzero \(r\)-minor polynomial. Its nonzero set is open and dense. To justify density, a nonzero real polynomial cannot vanish on an open box: regard it as a polynomial in the last variable; vanishing on an interval makes every coefficient zero on a box of one fewer variables, and induction makes the polynomial zero. The one-variable starting fact is that a nonzero degree-\(d\) polynomial has at most \(d\) distinct roots. If \(a\) is one root, the identities \(t^j-a^j=(t-a)\sum_{i=0}^{j-1}t^{j-1-i}a^i\) factor the polynomial as \((t-a)q(t)\), and induction on the degree gives that bound. The union of all nonzero maximal-minor sets is exactly the regular set; rank zero uses the empty minor \(1\).

Fix regular \(x\), \(y\in V\), and \(u\in\ker\beta_x\). For small \(t\), maximal rank persists and a fixed set of independent columns of \(\beta_{x+ty}\) is a basis of its image. Their Gram matrix for any auxiliary positive definite inner product on \(W\) stays invertible, so the corresponding orthogonal image projection depends continuously on \(t\). For \(t\ne0\),
\(\beta_{x+ty}(u)=t\beta_y(u)\);
thus \(\beta_y(u)\) belongs to that image. Taking \(t\to0\) gives (C.2). Under (C.3),
\[
\langle\beta_y(u),\beta_x(v)\rangle
=\langle\beta_y(v),\beta_x(u)\rangle=0.
\]
This proves (C.4). If the form is positive definite, \(U_x=0\), so every vector in \(\ker\beta_x\) is killed by all \(\beta_y\). The converse is immediate. Rank-nullity gives its dimension \(\dim U-r\geq\dim U-\dim W\), proving (C.5). □

**Lemma C.3 (Otsuki's dimension inequality).** Suppose \(V,W\) are Euclidean spaces and \(\beta:V\times V\to W\) is symmetric bilinear, with
\[
\langle\beta(x,x),\beta(y,y)\rangle-|\beta(x,y)|^2\leq0
\quad\text{for all }x,y,
\tag{C.6}
\]
and \(\beta(x,x)\ne0\) for every nonzero \(x\). Then \(\dim W\geq\dim V\).

**Proof.** The assertion is immediate if \(V=0\). Otherwise minimize \(|\beta(v,v)|^2\) on its compact unit sphere, using [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). At a minimizer set \(a=\beta(v,v)\ne0\). For unit \(w\perp v\), differentiate along \(v\cos t+w\sin t\). The first derivative is \(4\langle a,\beta(v,w)\rangle\), hence zero. Thus the linear map \(w\mapsto\beta(v,w)\) from \(v^\perp\) takes values in \(a^\perp\).

If \(\dim V>\dim W\), rank-nullity supplies a unit \(w\perp v\) with \(\beta(v,w)=0\). In the same variation,
\[
\beta(v\cos t+w\sin t,v\cos t+w\sin t)
=a+t^2(\beta(w,w)-a)+o(t^2).
\]
The second derivative of its squared norm is
\(4\langle a,\beta(w,w)-a\rangle\), which is nonnegative at a minimum. Hence
\(\langle\beta(v,v),\beta(w,w)\rangle\geq|a|^2>0\).
But (C.6) and \(\beta(v,w)=0\) make that inner product nonpositive, a contradiction. The elementary derivative tests and trigonometric differentiations used here are [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). □

**Proposition C.4 (The two nullities).** For a Euclidean submanifold of codimension \(p\), let
\[
\Delta=\{X:\alpha(X,Y)=0\text{ for every }Y\},\qquad
\nu=\dim\Delta,\quad \mu=\dim\mathcal N.
\]
Then
\[
\Delta\subseteq\mathcal N,\qquad \nu\leq\mu\leq\nu+p.
\tag{C.7}
\]

**Proof.** The inclusion is immediate from Gauss. The algebraic symmetries of Riemannian curvature, proved in [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1), show that a vector in \(\mathcal N\) makes the four-tensor zero in any slot: move it to the first slot by skew-symmetry and pair interchange. At the point in question consider
\[
\beta:TM\times\mathcal N\longrightarrow N_fM,\qquad
\beta(X,U)=\alpha(X,U).
\]
For \(U,V\in\mathcal N\), Gauss and the vanishing of \(g(R(X,Y)U,V)\) give
\[
\langle\alpha(X,U),\alpha(Y,V)\rangle
=\langle\alpha(X,V),\alpha(Y,U)\rangle.
\]
Thus \(\beta\) satisfies (C.3) with a positive definite target of dimension \(p\). Its common kernel in its second argument is exactly \(\Delta\), since \(\Delta\subseteq\mathcal N\). Lemma C.2 gives \(\nu\geq\mu-p\). □

For a system \(A_1,\ldots,A_k\) of self-adjoint maps on \(V\), say it has **type at least \(r\)** if there are \(x_1,\ldots,x_r\in V\) such that the \(rk\) vectors \(A_a x_i\), \(1\leq a\leq k\), \(1\leq i\leq r\), are linearly independent. The condition is unchanged by orthogonal change of the \(k\) maps or by an isometry of \(V\).

**Theorem C.5 (The shape-system lemma).** Suppose \(A_1,\ldots,A_k\) and \(B_1,\ldots,B_k\) are self-adjoint maps on a Euclidean space, the first system has type at least three, and
\[
\sum_{a=1}^k A_aX\wedge A_aY
=\sum_{a=1}^k B_aX\wedge B_aY
\quad\text{for all }X,Y.
\tag{C.8}
\]
There is a unique orthogonal matrix \(Q\in O(k)\) such that
\[
B_a=\sum_b Q_{ab}A_b.
\tag{C.9}
\]

**Proof.** Define symmetric forms with values in \(\mathbb R^k\) by
\[
\alpha(X,Y)=(\langle A_aX,Y\rangle)_a,\qquad
\alpha'(X,Y)=(\langle B_aX,Y\rangle)_a.
\]
On \(\mathbb R^k\oplus\mathbb R^k\) use the form
\(\langle(u,u'),(v,v')\rangle=\langle u,v\rangle-\langle u',v'\rangle\).
It is nondegenerate of signature \((k,k)\). Equation (C.8), paired with arbitrary two further vectors, says that \(\beta=(\alpha,\alpha')\) is flat in the sense of (C.3).

Let \(r\) be the maximal rank of \(\beta_X\). Among regular \(X\), let \(d\) be the minimum of \(\dim U_X\), with \(U_X\) as in (C.4). The set of regular \(X\) having this minimum is open and dense. Indeed, the Gram matrix of all the columns of \(\beta_X\) has polynomial entries; on the regular set its rank is \(r-\dim U_X\). The maximal-rank set of that Gram matrix is open and dense by the polynomial-minor argument in C.2, and intersects the regular set. Their intersection gives exactly the asserted minimum set.

Choose \(x_1,x_2,x_3\) in this open dense set with the \(3k\) vectors \(A_a x_i\) still independent. Such a choice is possible because independence is a nonempty open condition on triples, and a product of three dense open subsets meets every open product box. A totally isotropic subspace of \(\mathbb R^{k,k}\) has dimension at most \(k\): projection to the first \(\mathbb R^k\) is injective on it, since a vector with first component zero and zero squared norm has second component zero. Hence \(d\leq k\). Also \(\operatorname{Im}\beta_{x_1}\subseteq U_{x_1}^\perp\), so
\[
r\leq2k-d,\qquad
\dim\ker\beta_{x_1}\geq n-2k+d.
\]
Lemma C.2 shows that \(\beta_{x_2}\) maps this kernel into \(U_{x_1}\), losing at most \(d\) dimensions on taking the next kernel. Likewise \(\beta_{x_3}\) maps the intersection of the first two kernels into \(U_{x_2}\). Therefore
\[
\dim\bigcap_{i=1}^3\ker\beta_{x_i}\geq n-2k-d.
\tag{C.10}
\]
That intersection is contained in \(\bigcap_i\ker\alpha_{x_i}\). The latter is the perpendicular complement of the independent \(3k\) vectors \(A_a x_i\), so has dimension \(n-3k\). Comparing with (C.10) gives \(d\geq k\), and consequently \(d=k\).

Since the \(A_a x_1\) are independent, \(\alpha_{x_1}:V\to\mathbb R^k\) is onto. Thus \(r\geq k\). The preceding bound now gives \(r=k=d\). For every regular minimum-radical argument, its image therefore equals its radical and is totally isotropic. In particular
\[
\langle\beta(X,Y),\beta(X,Z)\rangle=0
\]
for all \(Y,Z\) and for \(X\) in a dense set, hence for every \(X\) by continuity. The four-linear form
\(S(X,Y,Z,W)=\langle\beta(X,Y),\beta(Z,W)\rangle\)
is symmetric in all four arguments: it is symmetric within each pair and between pairs, and flatness interchanges the middle arguments after these pair symmetries. Polarizing the displayed zero identity in the two occurrences of \(X\) therefore gives \(2S(X,Y,Z,W)=0\). Thus \(\beta\) is null and
\[
\langle\alpha(X,Y),\alpha(Z,W)\rangle
=\langle\alpha'(X,Y),\alpha'(Z,W)\rangle
\tag{C.11}
\]
for all arguments.

The values of \(\alpha\) span \(\mathbb R^k\), since a coefficient vector perpendicular to all its values would give a zero linear combination of the independent maps \(A_a\). Equation (C.11) makes the assignment \(\alpha(X,Y)\mapsto\alpha'(X,Y)\) well-defined on their span: any zero linear combination has image with squared norm zero. It preserves inner products, so is an isometry \(Q:\mathbb R^k\to\mathbb R^k\), necessarily onto. The spanning condition makes it unique. Taking its components gives (C.9). □

## D. Parallel normal spaces, rigidity and leaves

The **first normal space** at \(x\) is
\[
W_x=\operatorname{span}\{\alpha_x(X,Y):X,Y\in T_xM\}\subseteq N_xM.
\]
When its dimension is constant, the spaces form a smooth subbundle: select independent values of \(\alpha\) at one point; their Gram matrix stays invertible nearby, and they supply a local frame. Shape type refers to an orthonormal frame of this bundle and the definition preceding C.5.

**Proposition D.1 (Type two and codimension reduction).** On a connected Euclidean submanifold with constant first normal dimension \(k>0\), type at least two makes \(W\) parallel for \(\nabla^\perp\). Its image lies in one affine \((n+k)\)-plane. More generally, the latter conclusion holds whenever a parallel rank-\(k\) normal subbundle contains the entire second fundamental form.

**Proof.** We first record the linear implication used here and below. If a type-two system \(A_1,\ldots,A_k\) and covectors \(\ell_a\) obey
\[
\sum_a\ell_a(X)A_aY=\sum_a\ell_a(Y)A_aX,
\tag{D.1}
\]
then all \(\ell_a\) vanish. Choose \(u,v\) for which the \(2k\) vectors \(A_a u,A_a v\) are independent. Setting \((X,Y)=(u,v)\) gives \(\ell_a(u)=\ell_a(v)=0\) for every \(a\). Next set \((X,Y)=(u,Z)\); independence of \(A_a u\) gives \(\ell_a(Z)=0\) for every \(Z\).

Choose local orthonormal sections \(\eta_a\) of \(W\) and a section \(\xi\) of \(W^\perp\). Since \(\langle\alpha(Y,Z),\xi\rangle=0\), differentiating and applying Euclidean Codazzi gives
\[
\langle\alpha(Y,Z),\nabla^\perp_X\xi\rangle
=\langle\alpha(X,Z),\nabla^\perp_Y\xi\rangle.
\]
Pairing \(\nabla^\perp_X\xi\) with each \(\eta_a\) defines the covectors \(\ell_a(X)\). The last equation for every \(Z\) is (D.1), with \(A_a=A_{\eta_a}\). The linear implication makes all these covectors zero. Thus \(W^\perp\) is preserved by \(\nabla^\perp\); metric compatibility makes \(W\) parallel as well.

For the more general assertion let \(L= df(TM)\oplus W\) inside \(M\times\mathbb R^{n+p}\). By (A.1), \(\alpha\) taking values in \(W\) and its normal parallelism imply that the ordinary derivative of any section of \(L\) in any tangent direction lies in \(L\). Its orthogonal complement is also preserved, by differentiating inner products. Along a path a parallel orthonormal frame of \(L\), for the restricted ordinary connection, is therefore constant as an ambient frame. Existence and uniqueness along the path are [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2). Hence \(L_x\) is one fixed vector subspace \(L_0\) on the connected manifold. Since \(df(TM)\subseteq L_0\), integrating along paths shows \(f(M)\subseteq f(x_0)+L_0\), an affine plane of dimension \(n+k\). □

**Theorem D.2 (Rigidity in type at least three).** Let \(f,\widetilde f:(M,g)\to\mathbb R^{n+p}\) be isometric immersions of the same connected manifold. Suppose both first normal bundles have constant dimension \(k>0\), and the first immersion has type at least three everywhere. Then \(\widetilde f=T\circ f\) for one Euclidean motion \(T\).

For hypersurfaces this says: if \(\operatorname{rank}A_f\geq3\) everywhere, two isometric immersions differ by one Euclidean motion. A global unit normal and simple connectivity are not required.

**Proof.** In local orthonormal frames of the two first normal bundles, equality of the intrinsic Gauss tensors gives (C.8). Theorem C.5 supplies a unique fibre isometry \(J:W\to\widetilde W\) taking \(\alpha\) to \(\widetilde\alpha\). It is smooth: locally choose \(k\) second-form values which form a frame of \(W\). Their images under \(J\) are the corresponding smooth second-form values of the other immersion, and inversion of the frame's Gram matrix expresses \(J\) smoothly. Uniqueness makes the local definitions agree on overlaps. Formula (C.9) also preserves the type, so both first normal bundles satisfy D.1 and are parallel.

Pull back the second normal connection by \(J\), and subtract the first. Their difference is an endomorphism-valued one-form \(C_X\) on \(W\). Codazzi for the two immersions, together with \(J\alpha=\widetilde\alpha\), gives
\[
C_X\alpha(Y,Z)=C_Y\alpha(X,Z).
\tag{D.2}
\]
For each fixed row in an orthonormal normal frame, the coefficients of \(C_X\) give covectors satisfying (D.1). Type at least two makes every row zero. Thus \(C=0\) and \(J\) preserves the normal connections.

By D.1 each immersion has its tangent-plus-first-normal bundle equal to a fixed vector \((n+k)\)-plane, say \(L_0,\widetilde L_0\). Define a fibre isometry by
\[
df(X)+\xi\longmapsto d\widetilde f(X)+J\xi.
\]
Equations (A.1), equality of the second forms under \(J\), and parallelism of \(J\) show that it intertwines the ordinary ambient derivatives. Its derivative is therefore zero when expressed in constant bases of \(L_0,\widetilde L_0\); connectedness makes it one constant isometry \(Q_0\). Hence \(d\widetilde f=Q_0df\) and \(\widetilde f-Q_0f\) is a constant vector. Extend \(Q_0\) to an orthogonal map of the whole ambient space by choosing orthonormal bases of the equal-dimensional complements. Adding that constant translation gives \(T\).

For a hypersurface of rank at least three, its first normal line has dimension one everywhere, and three tangent vectors with independent shape images give type at least three. The fibre isometry of its normal lines can equivalently be read from Lemma C.1: the shapes agree up to the locally chosen normal sign. The argument above handles their global line bundles directly, so does not assume either normal bundle has been trivialized. □

**Proposition D.3 (Nullity distributions are totally geodesic).** Where its dimension is constant, the intrinsic curvature nullity of a Riemannian manifold is a smooth involutive distribution, and its leaves are totally geodesic. The same holds for the relative nullity \(\Delta\) of an immersion into a space of constant curvature. For relative-nullity leaves, their second fundamental form in the ambient space is zero as well.

**Proof.** Both distributions are kernels of smooth families of linear maps. At constant rank, choose a nonzero maximal minor and solve for the dependent coordinates; this constructs smooth local bases of the kernels.

For intrinsic nullity use the four-tensor \(\mathcal R(U,V,Z,W)=g(R(U,V)Z,W)\). Its algebraic symmetries make a nullity vector kill every slot, as in C.4. If \(X,Y\) are local nullity sections, apply the second Bianchi identity to the directions \(X,U,V\), with the last slots \(Y,W\):
\[
(\nabla_X\mathcal R)(U,V,Y,W)
+(\nabla_U\mathcal R)(V,X,Y,W)
+(\nabla_V\mathcal R)(X,U,Y,W)=0.
\]
The last two terms vanish. Indeed their underlying tensor evaluations have both \(X\) and \(Y\) as nullity arguments; in differentiating them, every resulting term still has at least one of these two arguments. In the first term all contributions vanish except
\(-\mathcal R(U,V,\nabla_XY,W)\).
It follows that \(\nabla_XY\) is in the nullity. The second Bianchi identity is proved, with the present convention, in [Geodesics C.2](geodesics-normal-coordinates-and-curvature.md#theorem-c-2), and the algebraic symmetries in [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1).

For relative nullity in a constant-curvature ambient space, Codazzi from A.2 has zero ambient normal term. If \(X,Y\in\Delta\), it gives
\[
(\nabla_Z\alpha)(X,Y)=(\nabla_X\alpha)(Z,Y).
\]
The left side is zero: after differentiating, each term has either \(X\) or \(Y\) as a nullity input. On the right the only possibly nonzero term is
\(-\alpha(Z,\nabla_XY)\).
Thus \(\nabla_XY\in\Delta\) again.

In either case torsion-freeness gives \([X,Y]=\nabla_XY-\nabla_YX\) in the distribution. The full Frobenius and maximal-leaf proofs are [De Rham decomposition B.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-2) and [De Rham decomposition B.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-3). The restriction of \(\nabla\) to a leaf is its metric, torsion-free connection, and the established derivative property makes its ambient second form in \(M\) vanish. Its geodesics are therefore geodesics of \(M\), by [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) and uniqueness. For a relative-nullity leaf, (A.1) has also \(\alpha(X,Y)=0\), so the same derivative property holds in the original ambient manifold. □

## E. Shape spectra and compact hypersurfaces

**Theorem E.1 (Umbilical hypersurfaces).** Let \(f:M^n\to\mathbb R^{n+1}\) be a connected isometric immersion, \(n\geq2\), whose shape is a scalar at every point. Its image is an open subset of an affine hyperplane or of a round sphere, and \(f\) is a local isometry onto that subset. If \(M\) is complete, \(f\) is an embedding onto the whole hyperplane or sphere.

**Proof.** On a neighbourhood with a unit normal, write \(A=cI\). Codazzi gives
\[
(Xc)Y=(Yc)X.
\]
Taking independent \(X,Y\) at a point shows that both derivatives vanish; varying them gives \(dc=0\), since \(n\geq2\). Changing the unit normal changes only the sign of \(c\), so \(|c|\) is globally locally constant, hence constant on connected \(M\).

If \(c=0\), equation (A.1) makes each local normal a constant ambient vector. Also \(d\langle f,\nu\rangle=0\). Thus each neighbourhood maps into an affine hyperplane. On overlapping neighbourhoods the hyperplanes coincide, because their direction is the common \(n\)-dimensional tangent plane and they contain a common image point. Connectedness gives one hyperplane for all of \(M\).

If \(|c|>0\), the mean curvature vector \(H=\frac1n\operatorname{tr}\alpha\) is a nowhere-zero global normal section. Take \(\nu=H/|H|\), so \(A=cI\) with the positive constant \(c=|H|\). The Weingarten equation gives
\[
d(f+c^{-1}\nu)=df-c^{-1}df\circ A=0.
\]
Consequently \(f(M)\) lies in the sphere of radius \(c^{-1}\) about the constant vector \(f+c^{-1}\nu\). In either case, the differential into the indicated \(n\)-manifold is an isometry and an isomorphism. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes \(f\) a local diffeomorphism, hence its image is open. If \(M\) is complete, Hopf–Rinow E.4 makes this local isometry a covering onto the entire connected target. The hyperplane is simply connected by its straight-line contraction, and the sphere is simply connected for \(n\geq2\) by [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3). [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) then makes the connected covering a diffeomorphism. □

**Theorem E.2 (Ricci and Einstein hypersurfaces).** For a Euclidean hypersurface,
\[
\operatorname{Ric}^{\sharp}=(\operatorname{tr}A)A-A^2.
\tag{E.1}
\]
If \(n\geq3\) and \(\operatorname{Ric}=\rho g\) for a constant \(\rho\), then \(\rho\geq0\). For \(\rho=0\) the induced metric is flat. For \(\rho>0\) the hypersurface is umbilical and has constant sectional curvature \(\rho/(n-1)\); if it is connected and complete, it is an embedded round sphere.

**Proof.** For an orthonormal basis \(e_i\), the Euclidean Gauss equation gives
\[
\begin{aligned}
\operatorname{Ric}(Y,Z)
&=\sum_i\langle R(e_i,Y)Z,e_i\rangle\\
&=(\operatorname{tr}A)\langle AY,Z\rangle-\langle AY,AZ\rangle .
\end{aligned}
\]
This proves (E.1). The spectral theorem [De Rham decomposition H.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-h-2) applies to \(A\). Every eigenvalue \(t\) therefore satisfies
\[
t^2-st+\rho=0,\qquad s=\operatorname{tr}A.
\tag{E.2}
\]
If \(\rho=0\), the eigenvalues are \(0,s\). For \(s\ne0\), if its multiplicity is \(m\), taking the trace yields \(s=ms\), hence \(m=1\). For \(s=0\), (E.2) gives \(A^2=0\), so all eigenvalues vanish. In both cases \(\operatorname{rank}A\leq1\), and C.1 proves flatness.

Suppose two distinct eigenvalues \(\lambda,\mu\) occur, with positive multiplicities \(m,l\), \(m+l=n\). Equation (E.2) implies
\[
\lambda+\mu=s=m\lambda+l\mu,\qquad
\lambda\mu=\rho,
\quad\text{so}\quad
(m-1)\lambda+(l-1)\mu=0.
\tag{E.3}
\]
If \(\rho>0\), both roots have the same nonzero sign. Equation (E.3) would require \(m=l=1\), contradicting \(n\geq3\). Thus there is only one eigenvalue and \(A=\lambda I\); (E.1) gives \(\rho=(n-1)\lambda^2\). The curvature assertion follows from Gauss, and the complete conclusion from E.1.

If \(\rho<0\), the single-eigenvalue case is impossible, so the two roots have opposite signs everywhere. Locally their multiplicities are constant: the spectral projections
\[
\frac{A-\mu I}{\lambda-\mu},\qquad
\frac{A-\lambda I}{\mu-\lambda}
\]
vary smoothly, and their integer traces are continuous. Here the roots are the smooth functions \((s\pm\sqrt{s^2-4\rho})/2\). Neither multiplicity can be one, since (E.3) would force the other to be one too. Their fixed ratio in (E.3), together with \(\lambda\mu=\rho\), makes both eigenvalues constant on such a neighbourhood.

Let \(X\) belong to the \(\lambda\)-eigenspace bundle and \(Y\) to the \(\mu\)-eigenspace bundle. Codazzi, with these constant eigenvalues, says
\[
(\mu I-A)\nabla_XY=(\lambda I-A)\nabla_YX.
\tag{E.4}
\]
The left side is in the \(\lambda\)-bundle, the right side in the orthogonal \(\mu\)-bundle, so both vanish. Thus \(\nabla_XY\) belongs to the \(\mu\)-bundle and \(\nabla_YX\) to the \(\lambda\)-bundle. Metric compatibility then gives the same preservation when both differentiated fields belong to one bundle; for example
\(\langle\nabla_X X',Y\rangle=-\langle X',\nabla_XY\rangle=0\).
Both bundles are parallel. Curvature therefore preserves them, so a mixed orthonormal plane has
\(\langle R(X,Y)Y,X\rangle=0\).
Gauss instead gives \(\lambda\mu=\rho<0\), a contradiction. This excludes negative \(\rho\). □

**Theorem E.3 (Compact convex hypersurfaces).** For a compact connected Euclidean hypersurface \(f:M^n\to\mathbb R^{n+1}\), without boundary and with \(n\geq2\), the following conditions are equivalent:

1. The shape is definite at every point, for either choice of local unit normal.
2. There is a global unit normal whose Gauss map is a diffeomorphism \(M\to S^n\).
3. The Gauss–Kronecker curvature \(\det A\) is nowhere zero, with its nonvanishing understood independently of the normal sign.

Under these conditions \(f\) is an embedding. Every tangent hyperplane supports the whole image and meets the image at exactly its point of tangency.

**Proof.** First any compact immersed hypersurface has an elliptic point. Fix \(z\in\mathbb R^{n+1}\) and maximize \(h=\frac12|f-z|^2\) on \(M\). At a maximum \(x\), the vector \(r=f(x)-z\) is normal and
\[
\operatorname{Hess}h(X,X)
=|X|^2+\langle\alpha(X,X),r\rangle\leq0.
\tag{E.5}
\]
The maximum value is positive for a positive-dimensional immersion, so \(r\ne0\). Thus \(A_r\) is negative definite.

Assume condition 3. On each neighbourhood with a normal, a nonsingular symmetric matrix cannot change its numbers of positive and negative eigenvalues: continuity of its quadratic form on the unit sphere preserves any strictly positive or negative subspace under a sufficiently small perturbation, and the dimensions add to \(n\). Thus the subset where the shape is definite is both open and closed. The elliptic point and connectedness make it all of \(M\), proving condition 1.

Under condition 1, choose at each point the unique unit normal \(\nu\) for which \(A_\nu\) is negative definite. These local smooth choices agree on overlaps and define a global smooth normal. By A.4, its differential is \(-df\circ A_\nu\), hence nonsingular. The pullback by \(\nu\) of the round metric is a smooth Riemannian metric on compact \(M\), and is complete by Hopf–Rinow B.3. Hopf–Rinow E.4 makes \(\nu\) a covering of \(S^n\). [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3) and [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) make it a diffeomorphism. This proves condition 2. Conversely condition 2 and the same differential formula give condition 3.

For any unit \(u\), the critical points of the height \(h_u=\langle f,u\rangle\) are precisely the points with \(\nu=\pm u\), since the normal space is a line. There are exactly two. At the point with \(\nu=u\) the Hessian is \(A_\nu\), negative definite; at the point with \(\nu=-u\) it is \(-A_\nu\), positive definite. A global maximum exists by compactness and must be critical. It cannot be the latter point, which is a strict local minimum on a positive-dimensional manifold. Thus the former is the unique global maximum. All of the image lies on one side of its tangent hyperplane, with equality only at that point.

If \(f(x)=f(y)\), take \(u=\nu(x)\). Both points have the same maximal height, so uniqueness forces \(x=y\). An injective immersion from a compact manifold is an embedding: it is a continuous bijection onto its image, and images of closed subsets are compact, hence closed in the Hausdorff ambient space; its inverse is therefore continuous, while the local immersion charts give the embedded smooth structure. This proves the remaining assertions. □

**Theorem E.4 (Compact codimension bound).** Let \(f:M^n\to\mathbb R^{n+p}\) be an isometric immersion of a compact manifold without boundary. Suppose at every point there is an \(m\)-dimensional tangent subspace on which all sectional curvatures are nonpositive. Then \(p\geq m\). In particular a compact manifold with \(K\leq0\), including a flat one, cannot be immersed isometrically in a Euclidean space of dimension less than \(2n\).

**Proof.** For the zero-dimensional tangent subspace the claim is immediate. Otherwise the manifold has positive dimension, and the calculation (E.5) did not use codimension one. At a maximum of \(\frac12|f-z|^2\) it shows that \(\alpha(v,v)\ne0\) for every nonzero \(v\). Restrict \(\alpha\) to the given \(m\)-plane there. By Gauss its extrinsic sectional expression is nonpositive on that plane. Otsuki's lemma C.3, with this plane as domain and the \(p\)-dimensional normal space as target, gives \(p\geq m\). Take \(m=n\) for the last assertion. □

**Theorem E.5 (Compact hypersurface holonomy).** The restricted holonomy group of a compact connected Euclidean hypersurface \(M^n\) is \(SO(n)\), acting on each tangent space. For \(n\leq1\) this means the trivial group.

**Proof.** Dimension zero is immediate, since the tangent space is zero. For positive dimension, equation (E.5) supplies a point with invertible shape \(A\). For tangent vectors at that point, Gauss expresses its curvature endomorphisms as \(AX\wedge AY\), with the convention in C.1. Since \(A\) is invertible, their span is all skew-adjoint endomorphisms: in an orthonormal basis the wedges \(e_i\wedge e_j\), \(i<j\), are a basis of that space. [Curvature and holonomy G.3](curvature-and-holonomy-groups.md#theorem-g-3) puts this entire space inside the restricted holonomy Lie algebra.

Metric transport and the connected restricted holonomy construction in that theorem put the restricted group inside \(SO(n)\). The equality of Lie algebras makes its inclusion a local diffeomorphism at the identity by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), so its image contains an identity neighbourhood and is an open subgroup. The elementary plane-rotation argument in [Affine transformations G.1](affine-transformations-and-the-isometry-group.md#theorem-g-1) proves that \(SO(n)\) is connected, so an open subgroup must be the whole group: its cosets are open, and a proper one would disconnect the group. Transport to another base point conjugates these groups by a linear isometry, preserving \(SO(n)\). In dimension one the only connected subgroup of \(O(1)\) is the identity, giving the stated case. □

## F. Two principal curvatures and complete surfaces

**Lemma F.1 (Opposite principal-curvature extrema).** Let \(\lambda>\mu\) be the principal curvatures near a nonumbilical point of an immersed Euclidean surface, for a local unit normal. If \(\lambda\) has a local maximum and \(\mu\) a local minimum at the same point, the Gaussian curvature there is nonpositive.

**Proof.** Away from an umbilic the two roots of the characteristic polynomial of \(A\) are smooth. The projections \((A-\mu I)/(\lambda-\mu)\) and \((A-\lambda I)/(\mu-\lambda)\) give smooth eigenline bundles. Applying each to a fixed local field which has nonzero projection at the point, then normalizing, gives a local orthonormal principal frame \(e_1,e_2\). Write
\[
\nabla_{e_1}e_1=a e_2,\quad \nabla_{e_1}e_2=-a e_1,
\qquad
\nabla_{e_2}e_1=b e_2,\quad \nabla_{e_2}e_2=-b e_1.
\tag{F.1}
\]
Codazzi, evaluated on \(e_1,e_2\), gives
\[
a=\frac{e_2\lambda}{\lambda-\mu},
\qquad b=\frac{e_1\mu}{\lambda-\mu}.
\tag{F.2}
\]
Indeed the \(e_1,e_2\) coefficients of \((\nabla_{e_1}A)e_2\) are
\(a(\lambda-\mu),e_1\mu\), and those of
\((\nabla_{e_2}A)e_1\) are \(e_2\lambda,b(\lambda-\mu)\).
Torsion-freeness gives \([e_1,e_2]=-a e_1-b e_2\). Substituting (F.1) into the definition of curvature yields
\[
K=\langle R(e_1,e_2)e_2,e_1\rangle
=-e_1b+e_2a-a^2-b^2.
\tag{F.3}
\]
At the stated extrema all first derivatives of both eigenvalue functions vanish, so \(a=b=0\). Differentiating (F.2) there reduces (F.3) to
\[
K=\frac{e_2e_2\lambda-e_1e_1\mu}{\lambda-\mu}\leq0.
\]
The numerator has the asserted sign because along any smooth curve through a local maximum the second derivative is nonpositive, and at a minimum it is nonnegative. The first-derivative terms from the curve acceleration vanish at these critical points. □

**Theorem F.2 (Positive-curvature rigidity for surfaces).** Let a compact connected Euclidean immersed surface have \(K>0\). Choose its global normal so that both principal curvatures are positive, and order them \(\lambda\geq\mu>0\). If \(\mu=\psi(\lambda)\) for a nonincreasing function \(\psi\) on their range, the immersion is an embedding onto a round sphere. In particular:

1. A connected complete immersed Euclidean surface of constant positive Gaussian curvature is an embedded round sphere.
2. A compact connected immersed Euclidean surface with \(K>0\) and constant mean curvature is an embedded round sphere.

**Proof.** Gauss gives \(\lambda\mu=K>0\); the shape is definite. The unique choice of unit normal making it positive is smooth on overlaps, just as in E.3. Its ordered eigenvalues are continuous, since they are the two explicit quadratic roots. Let \(x\) maximize \(\lambda\). The monotonicity assumption makes \(x\) minimize \(\mu\). If \(\lambda(x)>\mu(x)\), they are smooth near \(x\) and F.1 contradicts \(K(x)>0\). Thus \(\lambda(x)=\mu(x)=c\). For every \(y\),
\[
\lambda(y)\leq c=\mu(x)\leq\mu(y)\leq\lambda(y).
\]
All terms are equal; the surface is umbilical. Compactness implies completeness by Hopf–Rinow B.3, and E.1 gives the sphere and embedding.

For a complete surface of constant \(K>0\), [Sectional curvature D.2](sectional-curvature-and-space-forms.md#theorem-d-2) gives a surjective covering local isometry from the round \(2\)-sphere of curvature \(K\). Its image is compact, hence the surface is compact. Now use \(\psi(t)=K/t\) and the result just proved. Constant mean curvature gives \(\mu=2H-\lambda\), also a nonincreasing relation, and proves the second case. □

**Theorem F.3 (No complete negative constant curvature immersion).** No complete connected surface of constant negative Gaussian curvature admits a smooth isometric immersion in \(\mathbb R^3\).

**Proof.** Rescale a proposed immersion and its induced metric by constant factors to make \(K=-1\). A constant positive metric scaling preserves completeness, as distances scale by its square root. Pass to the universal covering surface with the pulled-back metric and immersion. It is simply connected by [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) and remains complete by the covering and geodesic argument in Hopf–Rinow E.4. Thus we may assume \(M\) simply connected and complete.

The two unit choices in each normal line form a smooth double cover. [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) trivializes it, so choose a global normal. Gauss gives \(\det A=-1\). The eigenvalues are distinct and have the smooth global labels
\(\lambda>0\) and \(\mu=-1/\lambda<0\).
The spectral projections used in F.1 define smooth eigenline bundles; their unit-vector double covers likewise have global sections. Hence there is a global orthonormal principal frame \(e_1,e_2\).

Define a smooth function \(0<\theta<\pi/2\) by \(\tan\theta=\lambda\). This is legitimate since the derivative of \(\tan\) is positive on this interval, with limits \(0,+\infty\); its inverse is smooth by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion). The sine and cosine and their derivatives are given by the circle exponential calculation in [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Substitution in (F.2) gives
\[
a=\tan\theta\,e_2\theta,\qquad
b=\cot\theta\,e_1\theta .
\]
Set
\[
P=\cos\theta\,e_1,\qquad Q=\sin\theta\,e_2.
\tag{F.4}
\]
The product rule for brackets and (F.1) give
\[
\begin{aligned}
[P,Q]
={}&(-\cos\theta\sin\theta\,a+\sin^2\theta\,e_2\theta)e_1\\
&+(-\cos\theta\sin\theta\,b+\cos^2\theta\,e_1\theta)e_2=0 .
\end{aligned}
\]
Both fields have norm at most one. Such a smooth field on a complete Riemannian manifold is complete: on any integral curve approaching a finite endpoint in time, the distance between two points is at most the elapsed time. The curve is Cauchy and has a limit by metric completeness. A local solution neighbourhood at this limit, from [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), extends the curve past the endpoint by uniqueness. The same argument applies backwards.

The complete flows of \(P,Q\) commute by [De Rham decomposition B.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-b-1). They therefore define an \(\mathbb R^2\)-action. For a fixed point \(p\), its orbit map
\[
F(u,v)=\phi_P^u\phi_Q^v(p)
\]
has differential with columns \(P,Q\), which are independent everywhere. Every orbit is open by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), so connectedness makes this one orbit all of \(M\). The stabilizer \(H=\{(u,v):F(u,v)=p\}\) is discrete, since \(F\) is a local diffeomorphism at \(0\), and
\(F(a)=F(b)\) holds exactly when \(a-b\in H\).
Choose a small inverse chart \(U\) about \(0\) whose differences meet \(H\) only at \(0\). Then
\[
F^{-1}(F(U))=\coprod_{h\in H}(U+h),
\]
and each piece maps diffeomorphically onto \(F(U)\). Translating this argument in the action gives an evenly covered neighbourhood at every point of \(M\). Thus \(F:\mathbb R^2\to M\) is a covering, and simple connectivity makes it a diffeomorphism by [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3).

In these global coordinates, \(F_*\partial_u=P\), \(F_*\partial_v=Q\), and the metric and scalar second form are
\[
g=\cos^2\theta\,du^2+\sin^2\theta\,dv^2,\qquad
b=\sin\theta\cos\theta\,(du^2-dv^2).
\]
Put \(s=(u+v)/2,\ t=(u-v)/2\) and \(\varphi=2\theta\). These are again global coordinates on \(\mathbb R^2\), with \(0<\varphi<\pi\), and
\[
g=ds^2+2\cos\varphi\,ds\,dt+dt^2,\qquad
b=2\sin\varphi\,ds\,dt.
\tag{F.5}
\]
Here a cross term \(2b_{st}\,ds\,dt\) means \(b_{st}=b_{ts}\).
For completeness, the metric formula in A.3 gives the following nonzero Christoffel symbols:
\[
\Gamma^s_{ss}=\cot\varphi\,\varphi_s,\quad
\Gamma^t_{ss}=-\csc\varphi\,\varphi_s,\quad
\Gamma^s_{tt}=-\csc\varphi\,\varphi_t,\quad
\Gamma^t_{tt}=\cot\varphi\,\varphi_t,
\qquad \Gamma^s_{st}=\Gamma^t_{st}=0.
\]
To compute \(\langle R(\partial_s,\partial_t)\partial_t,\partial_s\rangle\), use the zero mixed symbols to differentiate
\(\nabla_t\partial_t=-\csc\varphi\,\varphi_t\partial_s+
\cot\varphi\,\varphi_t\partial_t\)
in direction \(s\). The derivative-of-\(\csc\) term cancels the \(\partial_s\)-connection contribution. The two resulting coefficients are
\(-\csc\varphi\,\varphi_{st}\) and
\(\cot\varphi\,\varphi_{st}\). Taking the inner product with \(\partial_s\) gives
\(-\sin\varphi\,\varphi_{st}\).
Since \(\det g=\sin^2\varphi\), curvature \(K=-1\) is exactly
\[
\varphi_{st}=\sin\varphi>0
\quad\text{on the entire }(s,t)\text{-plane}.
\tag{F.6}
\]

There is no such smooth function with values in \((0,\pi)\). Indeed \(\varphi_s\) cannot vanish everywhere by (F.6). If its nonzero value somewhere is negative, replace \((s,t)\) by \((-s,-t)\); (F.6) is unchanged and that derivative becomes positive. Continuity supplies \(a<b\), a time \(t_0\), and \(\delta>0\) such that
\(\varphi_s(s,t_0)\geq\delta\) on \([a,b]\).
Equation (F.6) makes \(\varphi_s(s,t)\geq\delta\) there for all \(t\geq t_0\).
Choose \(a<a_1<b_1<b\). Integrating this inequality in \(s\), and using \(0<\varphi<\pi\), gives, for a fixed sufficiently small \(0<\epsilon<\pi/2\),
\[
\epsilon\leq\varphi(s,t)\leq\pi-\epsilon
\quad(a_1\leq s\leq b_1,\ t\geq t_0).
\]
For instance take \(\epsilon\) smaller than both
\(\delta(a_1-a)\) and \(\delta(b-b_1)\).
Twice applying the fundamental theorem of calculus ([Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations)) to (F.6) now gives
\[
\begin{aligned}
&\varphi(b_1,T)-\varphi(a_1,T)
-\varphi(b_1,t_0)+\varphi(a_1,t_0)\\
&\qquad=\int_{t_0}^T\int_{a_1}^{b_1}\sin\varphi(s,t)\,ds\,dt
\ \geq\ (T-t_0)(b_1-a_1)\sin\epsilon .
\end{aligned}
\]
The left side has absolute value less than \(2\pi\), whereas the right side tends to infinity. This contradiction proves the theorem. □

## G. Totally geodesic submanifolds and affine fixed sets

**Proposition G.1 (The quotient second form and torsion).** For an immersion into a manifold with an arbitrary affine connection \(\overline\nabla\), let
\[
B(X,Y)=[\,\overline\nabla_Xdf(Y)\,]\in f^*T\overline M/df(TM).
\tag{G.1}
\]
The immersion is autoparallel, meaning that ambient parallel transport along its curves preserves its tangent spaces, exactly when \(B=0\). It is totally geodesic, meaning that each ambient geodesic initially tangent to a local immersed branch stays in that branch locally, exactly when \(B(X,X)=0\) for all \(X\). These conditions are equivalent if the ambient torsion of two tangent vectors is tangent; in particular they are equivalent for a torsion-free connection.

**Proof.** The derivative-of-a-function term in the Leibniz rule is a multiple of \(df(Y)\), so vanishes in the quotient. Thus \(B\) is bilinear over smooth functions and defines a smooth tensor. In a local branch, coordinate brackets give
\[
B(X,Y)-B(Y,X)=[\,\overline T(df(X),df(Y))\,].
\tag{G.2}
\]
Choose a local smooth complement of \(df(TM)\), for example by a local inner product and orthogonal projection. Projection of \(\overline\nabla\) onto \(df(TM)\) gives a connection \(\nabla^T\). If \(B=0\), its parallel-transport equation is also the ambient equation, so uniqueness in [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) proves preservation of tangent spaces. Conversely, if ambient transport preserves tangent spaces, a tangent vector transported along a curve has ambient derivative zero and remains tangent. Such transported vectors form a local frame along the curve. Expressing any tangent field in this frame makes its ambient derivative tangent too. This gives \(B=0\) in every curve direction.

The ambient acceleration of a curve in a local branch decomposes into its \(\nabla^T\)-acceleration and \(B(\dot\gamma,\dot\gamma)\). If the latter always vanishes, a \(\nabla^T\)-geodesic is an ambient geodesic; existence and uniqueness of the geodesic initial-value problem ([Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1)) proves total geodesy. Conversely a tangent ambient geodesic which stays locally in the branch has zero quotient acceleration, giving \(B(v,v)=0\) for every initial tangent vector \(v\). Polarization says this is equivalent to the vanishing of the symmetric part of \(B\). Equation (G.2) makes \(B\) symmetric under the stated torsion condition, and proves the equivalence.

The torsion qualification cannot be dropped. On \(\mathbb R^3\) with coordinates \(x,y,z\), set
\[
\overline\nabla_{\partial_x}\partial_y=\partial_z,\qquad
\overline\nabla_{\partial_y}\partial_x=-\partial_z
\]
and set all other coordinate Christoffel symbols to zero. The terms \(\Gamma(v,v)\) cancel, so every geodesic is a straight line. The plane \(z=0\) is totally geodesic, but its quotient form has
\(B(\partial_x,\partial_y)=[\partial_z]\ne0\); it is not autoparallel. Its ambient torsion on these two tangent vectors is \(2\partial_z\). □

**Proposition G.2 (Induced connection and inherited tensors).** On an autoparallel submanifold the ambient connection restricts to a tangent connection. Its torsion and curvature are the ambient torsion and curvature on tangent inputs. In adapted frames its connection matrix preserves the tangent block. All covariant derivatives of the restricted torsion and curvature likewise agree with their ambient counterparts on tangent inputs. For a Riemannian totally geodesic submanifold this connection is its Levi-Civita connection, and both the tangent and normal bundles are parallel along the submanifold.

**Proof.** Since \(B=0\), define \(df(\nabla_XY)=\overline\nabla_Xdf(Y)\). It satisfies both connection axioms because the ambient connection does. Computing torsion by subtracting the two derivatives and the bracket gives the asserted restriction; (G.2) ensures it is tangent. Computing curvature as the commutator of two covariant derivatives minus the bracket derivative gives
\[
df(R(X,Y)Z)=\overline R(df(X),df(Y))df(Z).
\tag{G.3}
\]
All terms are tangent by autoparallelism.

In a frame whose first vectors span \(df(TM)\), differentiation of those vectors has no component in the complementary quotient. Thus the connection matrix has block form
\[
\begin{pmatrix}\omega^T&\beta\\0&\omega^Q\end{pmatrix}.
\]
The top-left block is the tangent connection and the bottom-right block induces the quotient connection. The component formula for a tensor derivative is the derivative of its evaluation minus one term for each differentiated argument, with the output connection added; see [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Since each tangent input remains tangent under differentiation, this formula and (G.3) prove the restriction assertion for the first covariant derivative, and induction proves it for every further derivative. The same argument applies to any ambient tensor whose restriction has the required tangent-valued outputs.

In the Riemannian torsion-free case, G.1 gives autoparallelism from total geodesy. The tangent restriction is metric and torsion-free, hence is the Levi-Civita connection by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Orthogonality and metric compatibility show that the normal bundle is parallel as well: for a normal section \(\xi\) and tangent \(Y\),
\(\langle\overline\nabla_X\xi,df(Y)\rangle
=-\langle\xi,\overline\nabla_Xdf(Y)\rangle=0\).
Thus an orthonormal adapted frame has block diagonal connection. Tangent parallel transport is intrinsic parallel transport; along a loop it is the tangent restriction of ambient transport along the image loop. In particular parallel ambient curvature restricts to parallel intrinsic curvature. □

**Theorem G.3 (Great-sphere classification).** A connected \(k\)-dimensional totally geodesic isometric immersion into the unit sphere has image an open subset of a great \(k\)-sphere and is a local isometry to that great sphere. If it is complete, it covers the whole great sphere. For \(k\geq2\) it is an embedding onto it; for \(k=1\) the complete possibilities include its universal and finite multiple coverings.

**Proof.** Write the immersion as \(f:M\to S^N\subset\mathbb R^{N+1}\). [Sectional curvature C.1](sectional-curvature-and-space-forms.md#theorem-c-1) computes the Euclidean second form of the unit sphere as \(-g(X,Y)f\). Total geodesy in the sphere, A.1, and G.2 therefore give
\[
D_X f=df(X),\qquad
D_Xdf(Y)=df(\nabla_XY)-g(X,Y)f.
\tag{G.4}
\]
Consequently the rank-\((k+1)\) bundle spanned by \(f\) and \(df(TM)\) is preserved by the ordinary Euclidean connection. The parallel-frame argument of D.1 makes it one constant vector \((k+1)\)-plane \(L\). Thus the image lies in \(L\cap S^N\), a great \(k\)-sphere. The differential is an isometry between spaces of the same dimension, so [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a local isometry with open image.

For a complete source, Hopf–Rinow E.4 makes this a covering onto the great sphere. When \(k\geq2\), [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3) and [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) make it a diffeomorphism. For \(k=1\), the unit-speed parametrization
\(t\mapsto(\cos t,\sin t)\)
is its universal cover, with deck translations \(2\pi\mathbb Z\), by [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) classifies its connected covers by the subgroups of this group. A nonzero subgroup of \(\mathbb Z\) is \(m\mathbb Z\): choose its least positive member \(m\) and apply division with remainder; the zero subgroup gives the universal cover. These are exactly the finite multiple and universal coverings stated. In dimension zero the connected source is a point and the assertion reduces to that point. □

**Theorem G.4 (Homogeneity of complete totally geodesic submanifolds).** A connected complete totally geodesic immersed Riemannian submanifold of a homogeneous Riemannian manifold is itself homogeneous.

**Proof.** The ambient isometry group is a Lie group with smooth action by [Affine transformations C.2](affine-transformations-and-the-isometry-group.md#theorem-c-2). Homogeneity and Invariant connections A.2 say that the differential of each orbit map is surjective. Equivalently, the values of its fundamental Killing fields span every ambient tangent space. These fields are defined on the whole ambient manifold, as the infinitesimal fields of one-parameter isometry groups.

For such an ambient Killing field \(K\), decompose its pullback along \(f\) into tangent and normal parts, \(K=df(V)+\xi\). This defines a global smooth field \(V\) on the immersed manifold, even when distinct points have the same image. Because the second form vanishes, the tangent part of \(\overline\nabla_XK\) is \(df(\nabla_XV)\), by A.1 and G.2. The ambient Killing equation therefore restricts to
\[
\langle\nabla_XV,Y\rangle+\langle X,\nabla_YV\rangle=0 .
\]
[Affine transformations A.3](affine-transformations-and-the-isometry-group.md#corollary-a-3) makes \(V\) an intrinsic Killing field. Completeness of \(M\) makes its flow complete by [Affine transformations D.4](affine-transformations-and-the-isometry-group.md#theorem-d-4).

At each point, these projected fields span \(TM\), since the ambient values span the ambient tangent space and orthogonal projection is onto. Choose \(k=\dim M\) of them whose values are a basis there. The map obtained by successively flowing for parameters \(t_1,\ldots,t_k\) has invertible differential at zero. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes its image contain a neighbourhood of the point. Thus every orbit of the group generated by these complete intrinsic isometries is open. Connectedness makes there be just one orbit: otherwise one orbit and the union of all others would be disjoint nonempty open subsets. This is homogeneity of \(M\). □

**Theorem G.5 (Common affine fixed sets).** On a manifold with any affine connection, the common fixed set of an arbitrary family of global affine transformations is closed, and each of its connected components is an embedded autoparallel submanifold. The same conclusion holds for the common zero set of any family of globally defined infinitesimally affine fields; the fields need not be complete. Components can have different dimensions.

**Proof.** Fixed sets of continuous self-maps are closed in a Hausdorff manifold, and zero sets of smooth fields are closed. Intersections remain closed. We prove the local submanifold and autoparallel assertions.

Let \(p\) be fixed by every transformation \(F\) in the family, and put
\[
E_p=\bigcap_F\ker(dF_p-I)\subseteq T_pM.
\]
A finite subfamily has this same intersection: start with the full tangent space and, whenever its current intersection is larger than \(E_p\), choose a transformation whose kernel cuts it down. Each such choice strictly lowers its dimension, so the process stops in at most \(\dim M\) steps. Choose a normal exponential ball at \(p\). Shrink it so that the selected finite set of differentials also sends it inside an injectivity neighbourhood of \(\exp_p\). Affine exponential naturality, proved in [Affine transformations A.1](affine-transformations-and-the-isometry-group.md#lemma-a-1), gives
\[
F(\exp_p v)=\exp_p(dF_p v).
\tag{G.5}
\]
For a common fixed point \(q=\exp_p v\) in this smaller ball, injectivity makes \(dF_pv=v\) for the finite subfamily, hence \(v\in E_p\). Conversely if \(v\in E_p\), (G.5) gives \(F(q)=q\) for every member of the entire family. The right side is defined in this case because \(dF_pv=v\). Thus the common fixed set near \(p\) is exactly \(\exp_p(E_p)\) intersected with the chosen normal ball. It is an embedded submanifold there, with tangent space \(E_p\) at \(p\).

On each such local submanifold, a transformation fixes tangent vector fields pointwise. Preservation of the connection implies that it also fixes \(\overline\nabla_XY\), for tangent \(X,Y\). This derivative is therefore in the common fixed subspace of the differentials at the point, which is exactly the tangent space just identified. Proposition G.1 proves autoparallelism.

For the infinitesimal assertion let all fields \(Z\) vanish at \(p\), and take a normal ball there. Their local flows fix \(p\), and their differentials there are \(\exp(t\,dZ_p)\), by the linearized ODE in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). For each fixed \(v\) in that ball and each fixed field, the flow is defined for a common small time along the compact radial geodesic from \(p\) to \(\exp_pv\). This follows by a finite cover of its image by local flow neighbourhoods. Differentiating (G.5) for that flow at \(t=0\) gives
\[
Z(\exp_pv)=(d\exp_p)_v(dZ_pv).
\tag{G.6}
\]
The exponential differential is invertible in the chosen normal ball. Thus the common zero set there is precisely
\[
\exp_p\left(\bigcap_Z\ker dZ_p\right)
\]
inside the ball, with no uniform flow time for the entire family needed. This proves the embedded local description.

To prove autoparallelism, use the tensor \(A_Z=L_Z-\nabla_Z\) of [Affine transformations A.2](affine-transformations-and-the-isometry-group.md#theorem-a-2). At a zero of \(Z\), it is \(-dZ\), as the coordinate bracket formula shows. The affine infinitesimal equation is \(\nabla_XA_Z=R(Z,X)\). Along the common zero submanifold this vanishes, and \(A_ZY=0\) for every tangent \(Y\). Differentiating along a tangent \(X\) gives
\[
0=\nabla_X(A_ZY)=(\nabla_XA_Z)Y+A_Z\nabla_XY
=A_Z\nabla_XY.
\]
Hence \(\nabla_XY\) belongs to the common kernel, which the local description identifies with the tangent space. Again G.1 applies. The dimensions in either local description are locally constant along the fixed or zero set, so each connected component has one dimension and carries the asserted embedded submanifold structure. □

## H. Exercises with complete solutions

**Exercise H.1 (Curvature of a graph).** For the graph \(f(x,y)=(x,y,h(x,y))\) with upward normal, derive its Gaussian curvature. Evaluate it at the origin when \(h=ax^2+bxy+cy^2\), and explain its independence of normal orientation and its intrinsic meaning.

**Solution.** Put \(w=\sqrt{1+h_x^2+h_y^2}\). The two tangent vectors, their Gram matrix, and the upward normal are
\[
f_x=(1,0,h_x),\quad f_y=(0,1,h_y),\qquad
g=\begin{pmatrix}1+h_x^2&h_xh_y\\h_xh_y&1+h_y^2\end{pmatrix},
\quad \nu=w^{-1}(-h_x,-h_y,1).
\]
Thus \(\det g=w^2\), while
\(b_{ij}=\langle f_{ij},\nu\rangle=h_{ij}/w\).
Gauss and the determinant formula A.3 give
\[
K=\frac{\det b}{\det g}
=\frac{h_{xx}h_{yy}-h_{xy}^2}{(1+h_x^2+h_y^2)^2}.
\tag{H.1}
\]
For the quadratic graph the gradient vanishes at \(0\) and its Hessian there is
\(\begin{pmatrix}2a&b\\b&2c\end{pmatrix}\), so \(K(0)=4ac-b^2\).
Replacing \(\nu\) by \(-\nu\) changes \(b\) and \(A\) to their negatives; their \(2\)-by-\(2\) determinants are unchanged. Although (H.1) uses the graph's ambient derivatives, A.3 proves that its value also equals the curvature computed from \(g\), its first derivatives and its second derivatives alone. That equality is the intrinsic content of the calculation; it does not assert that the individual principal curvatures are determined by the metric. □

**Exercise H.2 (Gauss alone does not reconstruct a surface).** Derive Codazzi by expanding Euclidean ambient derivatives. On a rectangle with metric \(dx^2+dy^2\), prescribe
\(A\partial_x=a(x,y)\partial_x,\ A\partial_y=0\).
Determine precisely when a cooriented realization exists and give all such data explicitly up to Euclidean motion.

**Solution.** Write \(D_Xdf(Y)=df(\nabla_XY)+\alpha(X,Y)\) and
\(D_X\xi=-df(A_\xi X)+\nabla^\perp_X\xi\).
The normal component of \(D_XD_Ydf(Z)\) is
\[
\alpha(X,\nabla_YZ)+\nabla^\perp_X\alpha(Y,Z).
\]
Subtract the expression with \(X,Y\) interchanged and the normal component
\(\alpha([X,Y],Z)\) of \(D_{[X,Y]}df(Z)\). The ambient curvature is zero. Insert
\([X,Y]=\nabla_XY-\nabla_YX\); grouping the resulting terms gives
\[
0=(\nabla_X\alpha)(Y,Z)-(\nabla_Y\alpha)(X,Z),
\]
with the covariant derivative defined in A.2. In codimension one this is
\((\nabla_XA)Y=(\nabla_YA)X\), since the unit normal has zero normal derivative.

For the prescribed matrix, \(\det A=0\), so Gauss holds for every \(a\). The coordinate frame is parallel. Codazzi for \(\partial_y,\partial_x\) says
\[
a_y\partial_x=(\nabla_{\partial_y}A)\partial_x
=(\nabla_{\partial_x}A)\partial_y=0 .
\]
Consequently it is necessary that \(a_y=0\). On a rectangle this means \(a=a(x)\), by integration along its vertical intervals. It is also sufficient, explicitly. Choose \(x_0\), define
\[
\theta(x)=\theta_0+\int_{x_0}^x a(r)\,dr,\qquad
\gamma(x)=\gamma_0+
\int_{x_0}^x(\cos\theta(r),\sin\theta(r))\,dr,
\]
and put
\[
f(x,y)=(\gamma_1(x),\gamma_2(x),y),\qquad
\nu(x,y)=(-\sin\theta(x),\cos\theta(x),0).
\tag{H.2}
\]
Then \(f_x,f_y\) are orthonormal, \(f_{xx}=a\nu\), and the other second derivatives vanish. Equivalently \(\nu_x=-a f_x,\ \nu_y=0\). The metric and prescribed shape are exactly the required ones. The integrations are justified by [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Changing \(\gamma_0,\theta_0\) gives Euclidean motions of this realization. Every other cooriented realization of the same data differs by such a motion by B.2, since a rectangle is simply connected by straight-line contraction. For example \(a(x,y)=y\) satisfies Gauss everywhere but violates Codazzi everywhere, so it has no realization. □

**Exercise H.3 (Completeness and great spheres).** Prove the great-sphere conclusion for a connected totally geodesic immersion, state what completeness adds, and give a proper incomplete example and a complete multiple covering.

**Solution.** The constant-plane argument (G.4) in G.3 proves containment in one great sphere and openness of the image. The same theorem proves that completeness makes the immersion a covering of the entire great sphere, with an embedding in dimension at least two. No stronger embedding assertion holds for curves. Indeed
\[
(-\pi/2,\pi/2)\longrightarrow S^2,\qquad
t\longmapsto(\cos t,\sin t,0)
\]
is a totally geodesic unit-speed immersion into a proper open arc of the equator. It is incomplete: a sequence tending to \(\pi/2\) is Cauchy for its interval metric and has no limit there. Total geodesy follows either from the great-circle geodesic formula in [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2) or directly from \(f''=-f\), whose tangent projection to the sphere is zero.

The same formula on \(\mathbb R/(4\pi\mathbb Z)\), with metric \(dt^2\), gives a double covering of the equator. It is well-defined because sine and cosine have period \(2\pi\), is locally unit-speed and totally geodesic, and is complete because its source is compact (Hopf–Rinow B.3). The two distinct classes of \(0\) and \(2\pi\) have the same image, so it is not an embedding. □

**Exercise H.4 (Reconstruction and a cylinder period).** Prove existence and uniqueness for compatible \((g,A)\) on a connected simply connected manifold. For
\[
M_L=(\mathbb R/L\mathbb Z)\times\mathbb R,\quad
g=ds^2+dt^2,\quad
A\partial_s=c\partial_s,\quad A\partial_t=0,\quad L>0,
\]
determine when a cooriented isometric realization in \(\mathbb R^3\) exists and when it is an embedding.

**Solution.** The full existence and uniqueness proof for the first assertion is B.2: take the trivial normal line, form the metric connection on \(TM\oplus\mathbb R\) with off-diagonal entries \(g(A\,\cdot,\cdot)\) and \(-A\), and compute its curvature blocks. Gauss and Codazzi make them zero. B.1 then supplies a global parallel trivialization and a primitive of its closed tangent-valued one-form. Its derivative is isometric, its normal has shape \(A\), and comparison of two parallel trivializations is one constant orthogonal map; the two primitives differ by a translation. This proves both assertions, including arbitrary compatible initial frame and position, without replacing the proof by an external reference.

Lift the cylinder data to the simply connected \((s,t)\)-plane. Gauss and Codazzi hold because the matrix is constant and has rank at most one. For \(c\ne0\), (H.2) gives the realization
\[
\begin{aligned}
f_c(s,t)&=\left(\frac{\sin(cs)}c,\frac{1-\cos(cs)}c,t\right),\\
\nu_c(s,t)&=(-\sin(cs),\cos(cs),0).
\end{aligned}
\tag{H.3}
\]
Direct differentiation gives the prescribed metric and \(A\), including for negative \(c\). By B.2 every cooriented realization on the plane is obtained from this one by one Euclidean motion. Therefore one descends to \(M_L\) exactly when this pair is periodic under \(s\mapsto s+L\). The trigonometric identities and the circle kernel \(2\pi\mathbb Z\) of [Connections E.1](connections-and-parallel-transport.md#lemma-e-1) give precisely
\[
cL\in 2\pi\mathbb Z,\qquad c\ne0.
\tag{H.4}
\]
Necessity can also be read from the derivative at \(s=0\), which must agree after a shift by \(L\). Under (H.4) the position and normal are both periodic, so it is sufficient.

Write \(|c|L=2\pi m\), \(m\) a positive integer. The first two components of (H.3) traverse a circle of radius \(1/|c|\) exactly \(m\) times as \(s\) runs through one period. If \(m=1\), they give a diffeomorphism of \(\mathbb R/L\mathbb Z\) onto that circle, since equality of the sine and cosine parameters is exactly equality modulo its period; local smooth inverses follow from its nonzero derivative. Product with \(t\) makes \(f_c\) an embedding onto the round cylinder. If \(m>1\), the distinct classes of \(0\) and \(2\pi/|c|\) have the same image, so no realization of the data is an embedding.

For \(c=0\), the plane development is \(f_0(s,t)=(s,0,t)\) with constant normal. Its shift under \(s\mapsto s+L\) is the nonzero translation \((L,0,0)\). Uniqueness on the cover makes it impossible for any Euclidean motion of this development to descend. Thus (H.4) lists all realizable cases, and an embedding occurs exactly for \(|c|L=2\pi\). This last case separates the two obstructions of B.3: at \(c=0\) the flat connection has trivial linear holonomy, but the tangent one-form still has a nonzero period. □

## Further reading

- Luis A. Florit, [*Submanifold Theory: class guide*, version 20260916.1308](https://luis.impa.br/aulas/imis/aulas.pdf), §§6–11, 15–16 and 19. The notes discuss the immersion equations, normal spaces, flat bilinear forms, rigidity and codimension bounds.
- Peter Petersen, [*Classical Differential Geometry*, university-hosted lecture notes](https://www.math.stonybrook.edu/~anderson/mat362-spr15/petersen.pdf), §6.4, printed pp. 149–159. This section treats surface compatibility, curvature and the global obstruction for constant negative curvature.

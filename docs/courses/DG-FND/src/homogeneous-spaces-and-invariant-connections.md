# Homogeneous spaces and invariant connections

This chapter develops invariant affine and metric connections, homogeneous holonomy, product decompositions and the invariant almost complex structures on the six-sphere. It also proves the homogeneous complex-coordinate criterion and reconstructs reductive homogeneity from complete parallel torsion, curvature and connection-difference data.

Let \(G\) be a finite-dimensional real Lie group, \(H\) a closed subgroup, and \(M=G/H\) a connected homogeneous space. Write \(o=eH\), \(\mathfrak g=T_eG\), \(\mathfrak h=T_eH\), and \(V=\mathfrak g/\mathfrak h\). A bar denotes a class in \(V\). The quotient charts and principal bundle \(q:G\to M\) have their complete construction in [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup). The isotropy representation is
\[
\lambda(h)\bar X=\overline{\operatorname{Ad}_hX}.
\]
It includes every component of \(H\). Our curvature convention is
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
\]
The free accounts of Alberto Elduque and Masahiro Morimoto listed below inform the affine and metric constructions. Every proof used from the programme is identified where it enters.

## A. Frames turn invariance into linear algebra

**Theorem A.1 (Classification without a reductive hypothesis).** The \(G\)-invariant affine connections on \(G/H\) correspond bijectively to linear maps \(W:\mathfrak g\to\mathfrak{gl}(V)\) satisfying
\[
\begin{aligned}
W(Z)&=\lambda_*(Z) &&(Z\in\mathfrak h),\\
W(\operatorname{Ad}_hX)&=\lambda(h)W(X)\lambda(h)^{-1}
&&(h\in H,\ X\in\mathfrak g).
\end{aligned}
\tag{A.1}
\]
If this set is nonempty, it is an affine space with translation space
\(\operatorname{Hom}_H(V,\mathfrak{gl}(V))\), where \(H\) acts on the endomorphisms by conjugation. For a smooth curve \(g(t)\in G\) and a vector \(v(t)\in V\), the corresponding connection obeys
\[
\nabla_t(j_{g(t)}v(t))
=j_{g(t)}\bigl(v'(t)+W(g(t)^{-1}g'(t))v(t)\bigr),
\tag{A.2}
\]
where \(j_g\bar X=d(L_g)_o(dq_eX)\); the notation \(g^{-1}g'\) means the left Maurer–Cartan form and does not require a matrix group.

**Proof.** The map \(j_g:V\to T_{gH}M\) is an isomorphism, and differentiating \(gh\exp(tX)H=g\exp(t\operatorname{Ad}_hX)H\) gives
\[
j_{gh}=j_g\lambda(h).
\]
Consequently the frame bundle is \(G\times_H\mathrm{GL}(V)\): the pair \((g,a)\) represents \(j_ga\), and \((gh,a)\) represents the same frame as \((g,\lambda(h)a)\). Local sections of \(q\), supplied by [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup), make this identification a smooth principal-bundle isomorphism.

[Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) proves, in both directions, the correspondence between a covariant derivative and a principal connection on its frame bundle. Apply the complete invariant-bundle classification in Invariant connections B.2 to this associated frame bundle and its isotropy homomorphism \(\lambda\). It says exactly that the pullback of the connection form by \(j:G\to FM\) is
\[
j^*\omega=W\theta_G
\]
with (A.1), and reconstructs the connection on \(G\times\mathrm{GL}(V)\) as
\[
\omega_{(g,a)}=\operatorname{Ad}_{a^{-1}}(W\theta_G)+\theta_{\mathrm{GL}(V)}.
\]
That proof checks descent for all of \(H\), reproduction of vertical fields, right equivariance, and the inverse construction; thus no existence condition is suppressed here. The frame formula for the covariant derivative in [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) gives (A.2).

The difference of two admissible maps vanishes on \(\mathfrak h\) and has the indicated equivariance, hence factors uniquely through an element of \(\operatorname{Hom}_H(V,\mathfrak{gl}(V))\). Conversely adding any such element preserves (A.1).

For later comparison of signs, let \(Y^*\) be the fundamental vector field of the left action, \(Y^*(gH)=\left.\frac{d}{ds}\right|_0\exp(sY)gH\). Its moving-frame coefficient is \(\overline{\operatorname{Ad}_{g^{-1}}Y}\). Along \(g(t)=\exp(tX)\), its coefficient derivative at zero is \(-\overline{[X,Y]}\). Therefore
\[
(\nabla_{X^*}Y^*)_o=W(X)\bar Y-\overline{[X,Y]}.
\tag{A.3}
\]
This distinguishes fundamental fields from the local frames used next. □

**Theorem A.2 (A reductive complement and a bilinear product).** Suppose
\(\mathfrak g=\mathfrak h\oplus\mathfrak m\), with
\(\operatorname{Ad}_h\mathfrak m=\mathfrak m\) for every \(h\in H\). Identify \(V\) with \(\mathfrak m\). The connections in A.1 correspond to all \(H\)-equivariant bilinear products
\(\alpha:\mathfrak m\times\mathfrak m\to\mathfrak m\), by
\[
W(Z+X)=\operatorname{ad}(Z)|_{\mathfrak m}+\Lambda(X),
\qquad \Lambda(X)Y=\alpha(X,Y).
\tag{A.4}
\]
In the local frame \(Y^\#(x)=j_{s(x)}Y\) defined by the section
\(s(\exp(X)H)=\exp(X)\), one has
\[
(\nabla_{X^\#}Y^\#)_o=\alpha(X,Y).
\tag{A.5}
\]

**Proof.** The exponential exists smoothly by [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). The derivative at zero of \(X\mapsto\exp(X)H\), restricted to \(\mathfrak m\), is the quotient isomorphism onto \(T_oM\). The inverse function theorem in [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes this map a chart and defines the stated section. In that chart the derivative of \(s\) at \(o\) sends \(j_eX\) to \(X\).

Restriction of (A.1) to \(\mathfrak m\) is precisely the equivariance of \(\alpha(X,Y)=W(X)Y\). Conversely (A.4) is linear, agrees with \(\lambda_*\) on \(\mathfrak h\), and is \(H\)-equivariant: both summands have this property, the first by the adjoint bracket identity and the second by the assumed equivariance of \(\alpha\). The direct-sum decomposition makes these operations inverse. Finally the coefficient of \(Y^\#\) is constant in the frame \(j_s\); apply (A.2) at \(o\) along \(X^\#\), where \(\theta_G ds(X^\#)=X\), to obtain (A.5). □

**Example A.3 (Nonexistence and disconnected isotropy).** Some homogeneous spaces admit no invariant affine connection. Even when a reductive complement exists, equivariance under \(\mathfrak h\) alone need not give equivariance under \(H\).

**Proof.** First take \(G=\mathrm{SL}(2,\mathbb R)\) and its closed subgroup \(H\) of upper triangular matrices. Its quotient is the space of lines in \(\mathbb R^2\): the action is transitive since a nonzero vector can be completed to a basis of determinant one, and the stabilizer of the first coordinate line is exactly \(H\). This line space is connected, being the image of the connected circle. The matrices
\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix}
\]
satisfy \([E,F]=D\), \([D,F]=-2F\), and \(\mathfrak h=\operatorname{span}(D,E)\). Thus \(V=\mathbb R\bar F\), \(\lambda_*(E)=0\), and \(\lambda_*(D)=-2\). Differentiating the second identity of (A.1) along \(\exp(tE)\) would give
\[
W([E,F])=[\lambda_*(E),W(F)]=0,
\]
whereas its first identity gives \(W([E,F])=W(D)=-2\). This contradiction proves nonexistence. The Lie-group and quotient hypotheses here can also be checked directly: determinant one is a smooth matrix submanifold because its derivative is the nonzero functional \(A\mapsto\operatorname{tr}(g^{-1}A)\), and multiplication and inversion restrict smoothly; the subgroup is closed, so [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) applies.

For the second assertion use \(G=\mathbb R\rtimes\{1,-1\}\), with
\((a,\epsilon)(b,\delta)=(a+\epsilon b,\epsilon\delta)\), and
\(H=\{(0,1),(0,-1)\}\). Then \(G/H=\mathbb R\), \(\mathfrak h=0\), and \(\mathfrak m=\mathbb R\) is a reductive complement. A bilinear product has the form \(\alpha(x,y)=cxy\). Equivariance under the nonidentity element of \(H\) requires
\(\alpha(-x,-y)=-\alpha(x,y)\), so \(c=0\). The infinitesimal condition, with \(\mathfrak h=0\), would have imposed no restriction. This also verifies explicitly why the classification in A.2 uses the whole isotropy group. □

## B. Torsion, curvature and complete orbit geodesics

**Theorem B.1 (Torsion and curvature in the moving frame).** For the connection specified by \(W\), the tensors at \(o\) are
\[
\begin{aligned}
T_o(\bar X,\bar Y)&=W(X)\bar Y-W(Y)\bar X-\overline{[X,Y]},\\
R_o(\bar X,\bar Y)&=[W(X),W(Y)]-W([X,Y]).
\end{aligned}
\tag{B.1}
\]
For a reductive presentation and the product of A.2, these become
\[
\begin{aligned}
T_o(X,Y)&=\alpha(X,Y)-\alpha(Y,X)-[X,Y]_{\mathfrak m},\\
R_o(X,Y)&=[\Lambda(X),\Lambda(Y)]
-\Lambda([X,Y]_{\mathfrak m})
-\operatorname{ad}([X,Y]_{\mathfrak h})|_{\mathfrak m}.
\end{aligned}
\tag{B.2}
\]

**Proof.** Pull the solder form on \(FM\) back by \(j\). At a left-invariant vector \(X^L\) on \(G\) it equals \(\bar X\), so it is the \(\mathfrak g/\mathfrak h\) projection of \(\theta_G\). Its exterior derivative on \(X^L,Y^L\) is \(-\overline{[X,Y]}\). The torsion structure equation \(T=d\theta+\omega\wedge\theta\), with its identification with covariant torsion proved in [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1), now gives the first line of (B.1).

Invariant connections B.3 computes the curvature of \(W\theta_G\) as the bracket defect in the second line. [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) identifies the induced endomorphism with \(R\) in our convention. These formulas descend to \(V\): if, for example, \(X=Z\in\mathfrak h\), the first line is
\(\overline{[Z,Y]}-0-\overline{[Z,Y]}=0\), and the second vanishes by the infinitesimal form of (A.1). Alternation handles the other argument. Substitution of (A.4), separating the two components of \([X,Y]\), proves (B.2). □

**Theorem B.2 (Canonical connection and the torsion-free orbit connection).** On a reductive space let \(\bar\nabla\) denote the connection with \(\alpha=0\). Every \(G\)-invariant tensor is \(\bar\nabla\)-parallel. In particular
\[
\bar T_o(X,Y)=-[X,Y]_{\mathfrak m},\qquad
\bar R_o(X,Y)=-\operatorname{ad}([X,Y]_{\mathfrak h})|_{\mathfrak m}
\tag{B.3}
\]
are parallel, and \(\bar\nabla\) is geodesically complete.

More generally, all the curves
\[
t\longmapsto g\exp(tX)H \quad(g\in G,\ X\in\mathfrak m)
\tag{B.4}
\]
are affinely parametrized geodesics for the connection \(\alpha\) if and only if \(\alpha(X,X)=0\) for every \(X\). Among these connections there is exactly one torsion-free connection: it has
\(\alpha(X,Y)=\tfrac12[X,Y]_{\mathfrak m}\).

**Proof.** Along (B.4) the left Maurer–Cartan coefficient of the lift \(g\exp(tX)\) is the constant \(X\), and its tangent vector has the constant frame coefficient \(X\). Formula (A.2) gives acceleration \(j_{g\exp(tX)}\alpha(X,X)\). This proves the stated equivalence, since one can also take \(g=e,t=0\). In particular it vanishes for \(\alpha=0\). Every initial tangent vector at every point is \(j_gX\) for some \(X\in\mathfrak m\). Smooth ODE uniqueness, proved in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), therefore identifies every geodesic of \(\bar\nabla\) with a curve (B.4), which exists for all real \(t\).

For \(\bar\nabla\), (A.2) also shows that the frame \(j_{g\exp(tX)}\) is parallel. The coefficients of a \(G\)-invariant tensor in \(j_g\) equal its coefficients in \(j_e\): invariance says exactly this for both vector and covector slots. They are therefore constant along (B.4). The tensor-derivative rule of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) makes its derivative zero along each such curve. Their initial velocities exhaust every tangent space, so the tensor is parallel. Torsion and curvature are \(G\)-invariant by (B.1) and the equivariance of \(W\), and (B.3) follows from (B.2).

Finally polarization of \(\alpha(X,X)=0\) gives
\(\alpha(X,Y)=-\alpha(Y,X)\). The first line of (B.2) makes torsion-freeness equivalent to \(2\alpha(X,Y)=[X,Y]_{\mathfrak m}\). This product is \(H\)-equivariant, so A.2 gives its existence as well as uniqueness. Notice that the general-point curves in (B.4) have \(g\) on the left; the complement \(\mathfrak m\) was fixed at \(o\). □

## C. Invariant metrics and their geodesics

Throughout this section the reductive complement is invariant under all of \(H\).

**Theorem C.1 (Invariant metrics and their unique metric torsion-free connection).** The \(G\)-invariant pseudo-Riemannian metrics on \(G/H\) correspond to the nondegenerate symmetric bilinear forms \(B\) on \(\mathfrak m\) invariant under \(\operatorname{Ad}(H)|_{\mathfrak m}\). The metric determined by \(B\) has a unique torsion-free metric connection. It is the invariant connection with
\[
\alpha(X,Y)=\tfrac12[X,Y]_{\mathfrak m}+U(X,Y),
\tag{C.1}
\]
where the symmetric bilinear map \(U\) is determined by
\[
2B(U(X,Y),Z)=B([Z,X]_{\mathfrak m},Y)+B(X,[Z,Y]_{\mathfrak m}).
\tag{C.2}
\]
An arbitrary invariant connection \(\alpha\) is metric precisely when every \(\Lambda(X)\) is \(B\)-skew:
\[
B(\alpha(X,Y),Z)+B(Y,\alpha(X,Z))=0.
\tag{C.3}
\]

**Proof.** Invariance forces a metric at \(gH\) to have the value
\[
g_{gH}(j_gX,j_gY)=B(X,Y).
\]
The identity \(j_{gh}=j_g\lambda(h)\) makes this independent of the representative \(g\) exactly when \(B\) is \(H\)-invariant. Local sections make the resulting tensor smooth. Nondegeneracy and symmetry hold at every point because \(j_g\) is an isomorphism. Conversely restricting an invariant metric to \(T_oM\) gives such a \(B\), so the constructions are inverse.

Compute the covariant derivative at \(o\) in the local frame of A.2, whose metric coefficients are constant. The tensor rule in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) gives
\[
(\nabla_Xg)_o(Y,Z)=-B(\alpha(X,Y),Z)-B(Y,\alpha(X,Z)).
\]
Invariance propagates this identity to every point and proves (C.3).

Nondegeneracy of \(B\) makes \(v\mapsto B(v,\cdot)\) a linear isomorphism onto \(\mathfrak m^*\); thus (C.2) defines a unique bilinear \(U\). Interchanging \(X,Y\), and using symmetry of \(B\), proves that \(U\) is symmetric. Applying an element of \(H\) to all three inputs of (C.2) preserves its right side. Uniqueness then proves equivariance of \(U\), so (C.1) defines an invariant connection by A.2. Its torsion is zero by B.1.

For metric compatibility, insert (C.1) and (C.2) into twice the left side of (C.3). The result is the sum
\[
\begin{aligned}
&B([X,Y]_{\mathfrak m},Z)+B([Z,X]_{\mathfrak m},Y)
+B(X,[Z,Y]_{\mathfrak m})\\
&\quad+B(Y,[X,Z]_{\mathfrak m})+B([Y,X]_{\mathfrak m},Z)
+B(X,[Y,Z]_{\mathfrak m}),
\end{aligned}
\]
which vanishes in pairs by skew symmetry of the bracket and symmetry of \(B\). This proves existence without any positive-definiteness assumption.

To prove uniqueness among all connections, the difference \(A\) of two covariant derivatives is a tensor by [Linear connections A.3](linear-and-affine-connections.md#theorem-a-3). If both are torsion free, \(A(X,Y)=A(Y,X)\). If both are metric, \(a(X,Y,Z)=g(A(X,Y),Z)\) satisfies \(a(X,Y,Z)=-a(X,Z,Y)\). Combining these two symmetries gives
\[
\begin{aligned}
a(X,Y,Z)&=a(Y,X,Z)=-a(Y,Z,X)\\
&=-a(Z,Y,X)=a(Z,X,Y)=a(X,Z,Y)=-a(X,Y,Z).
\end{aligned}
\]
Thus \(a=0\), and nondegeneracy gives \(A=0\). In particular the metric torsion-free connection constructed above is the Levi-Civita connection. □

**Theorem C.2 (Natural reductivity and the curvature numerator).** Call \(B\) naturally reductive for this complement when
\[
B([X,Y]_{\mathfrak m},Z)+B(Y,[X,Z]_{\mathfrak m})=0
\quad(X,Y,Z\in\mathfrak m).
\tag{C.4}
\]
This is equivalent to \(U=0\) in C.1. In this case the Levi-Civita connection is geodesically complete, including in indefinite signature, and all its geodesics have the form (B.4). Its curvature is
\[
\begin{aligned}
R(X,Y)Z={}&\tfrac14[X,[Y,Z]_{\mathfrak m}]_{\mathfrak m}
-\tfrac14[Y,[X,Z]_{\mathfrak m}]_{\mathfrak m}\\
&-\tfrac12[[X,Y]_{\mathfrak m},Z]_{\mathfrak m}
-[[X,Y]_{\mathfrak h},Z].
\end{aligned}
\tag{C.5}
\]
Writing \(K=[X,Y]_{\mathfrak m}\), its sectional-curvature numerator is
\[
B(R(X,Y)Y,X)=\tfrac14 B(K,K)-B([[X,Y]_{\mathfrak h},Y],X).
\tag{C.6}
\]
If \(Q\) is a positive-definite \(\operatorname{Ad}(G)\)-invariant form on \(\mathfrak g\), \(\mathfrak m=\mathfrak h^{\perp_Q}\), and \(B=Q|_{\mathfrak m}\), then
\[
B(R(X,Y)Y,X)
=\tfrac14\lVert[X,Y]_{\mathfrak m}\rVert_Q^2
+\lVert[X,Y]_{\mathfrak h}\rVert_Q^2\geq0.
\tag{C.7}
\]

**Proof.** Condition (C.4), with \(X\) replaced by \(Z\), makes the right side of (C.2) zero, hence \(U=0\). Conversely if \(U=0\), the connection \(\alpha(X,Y)=\tfrac12[X,Y]_{\mathfrak m}\) is metric, and (C.3) is (C.4). B.2 then gives all the geodesics and their completeness, without using a metric distance or positive definiteness. Substitution of \(\Lambda(X)Y=\tfrac12[X,Y]_{\mathfrak m}\) into (B.2) proves (C.5).

For \(Z=Y\), the first term of (C.5) is zero. Combining the next two, using \([K,Y]_{\mathfrak m}=-[Y,K]_{\mathfrak m}\), gives
\[
R(X,Y)Y=\tfrac14[Y,K]_{\mathfrak m}-[[X,Y]_{\mathfrak h},Y].
\]
By (C.4) the inner product of \([Y,K]_{\mathfrak m}\) with \(X\) is
\(-B(K,[Y,X]_{\mathfrak m})=B(K,K)\), which proves (C.6). In indefinite signature, sectional curvature on a nondegenerate plane is this numerator divided by \(B(X,X)B(Y,Y)-B(X,Y)^2\); no claim is made for degenerate planes.

For the last assertion, invariance of \(Q\) makes \(\mathfrak m\) invariant under all of \(H\). Differentiating its invariance under \(\exp(tA)\) gives
\[
Q([A,B_1],B_2)+Q(B_1,[A,B_2])=0.
\]
For \(X,Y,Z\in\mathfrak m\), orthogonality allows the projections in (C.4) to be removed inside \(Q\), and this identity proves natural reductivity. Put \(A=[X,Y]_{\mathfrak h}\). The same identity, together with symmetry, gives
\[
Q([A,Y],X)=Q(A,[Y,X])=-Q(A,A).
\]
Here the \(\mathfrak m\) part of \([X,Y]\) is orthogonal to \(A\). Equation (C.7) follows from (C.6). □

**Example C.3 (Three connections on a Lie group).** On a Lie group \(L\), for each real number \(s\), the prescription
\[
\nabla^{(s)}_{X^L}Y^L=s[X,Y]^L
\tag{C.8}
\]
defines a bi-invariant affine connection with
\[
T^{(s)}(X,Y)=(2s-1)[X,Y],\qquad
R^{(s)}(X,Y)=(s^2-s)\operatorname{ad}[X,Y].
\tag{C.9}
\]
At \(s=0\) all left-invariant fields are parallel; at \(s=1\) all right-invariant fields are parallel; at \(s=\tfrac12\) the connection is torsion free. All three, and indeed every member of the family, are geodesically complete. The torsion-free member is also the canonical connection of the symmetric presentation
\((L\times L)/\operatorname{diag}L\), acting by \((a,b)x=axb^{-1}\).

**Proof.** For the left translation presentation \(L/\{e\}\), A.2 constructs (C.8) from the bilinear product \(s[X,Y]\). Its torsion follows immediately from B.1. Jacobi's identity gives \([\operatorname{ad}X,\operatorname{ad}Y]=\operatorname{ad}[X,Y]\), so its curvature in (B.2) is \(s^2\operatorname{ad}[X,Y]-s\operatorname{ad}[X,Y]\). This proves (C.9).

Right translation by \(a\) takes the left frame at \(x\) to the left frame at \(xa\) with the constant coefficient change \(\operatorname{Ad}_{a^{-1}}\). This change preserves the bracket, so formula (A.2) intertwines the derivatives and proves right invariance; left invariance already holds by construction.

For \(s=0\), the left-frame coefficients of every left-invariant field are constant, giving parallelism directly. The left-frame coefficient of \(Y^R\) at \(x\) is \(\operatorname{Ad}_{x^{-1}}Y\). Along a curve with left velocity \(X(t)\), differentiating the adjoint action gives its derivative \(-[X(t),\operatorname{Ad}_{x^{-1}}Y]\), which the \(s=1\) connection term cancels. Thus the right-invariant fields are parallel. Torsion-freeness at \(s=\tfrac12\) and completeness of every member follow from (C.9) and B.2, since \(s[X,X]=0\).

For the last assertion set
\[
\mathfrak h=\{(Z,Z):Z\in\mathfrak l\},\qquad
\mathfrak m=\{(X/2,-X/2):X\in\mathfrak l\}.
\]
The complement is invariant under the full diagonal subgroup, identifies with \(T_eL\) by \(X\), and its self-bracket lies in \(\mathfrak h\). Its canonical connection has zero torsion by (B.3). Its geodesics starting at \(e\) are
\[
\exp(tX/2)\exp(tX/2)=\exp(tX).
\]
Left translations show that all other geodesics have the corresponding left translates. Relative to \(L/\{e\}\), it must therefore have a skew product by B.2; torsion-freeness forces that product to be \(\tfrac12[X,Y]\). This proves the claimed equality of connections, despite the different reductive presentations.

Finally a left-invariant nondegenerate symmetric metric is bi-invariant exactly when its value \(B\) at \(e\) is \(\operatorname{Ad}(L)\)-invariant, by the same frame change. Differentiating this condition makes the bracket \(B\)-skew. C.1 then identifies its Levi-Civita connection with \(s=\tfrac12\), including indefinite metrics. □

## D. Holonomy and a round model

**Theorem D.1 (A finite holonomy calculation).** For \(W\) in A.1 put
\[
\begin{aligned}
C_W(X,Y)&=[W(X),W(Y)]-W([X,Y]),\\
V_0&=\operatorname{span}\{C_W(X,Y):X,Y\in\mathfrak g\},\\
V_{r+1}&=V_r+\operatorname{span}\{[W(X),A]:X\in\mathfrak g,\ A\in V_r\}.
\end{aligned}
\tag{D.1}
\]
This sequence stabilizes in at most \((\dim M)^2\) strict increases. Its stable value is the holonomy Lie algebra in the frame \(j_e\). For the canonical connection of a reductive space it is already
\[
\mathfrak{hol}(\bar\nabla)
=\operatorname{span}\{\operatorname{ad}([X,Y]_{\mathfrak h})|_{\mathfrak m}:X,Y\in\mathfrak m\}.
\tag{D.2}
\]
The restricted canonical holonomy is a connected analytic normal subgroup of \(\lambda(H)\); it can be strictly smaller.

**Proof.** The hypotheses of the complete homogeneous holonomy theorem, Invariant connections C.1, hold for the frame bundle in A.1. That theorem proves that (D.1) stabilizes, that its stable space is automatically closed under brackets, and that it is the Lie algebra both of full and restricted holonomy. It also identifies restricted holonomy with the connected analytic subgroup generated by its exponentials. Dimension bounds the number of strict increases by \(\dim\mathfrak{gl}(V)=(\dim M)^2\).

For the canonical connection, \(W\) is zero on \(\mathfrak m\) and is \(\lambda_*\) on \(\mathfrak h\). Its curvature span is the space on the right of (D.2), with an immaterial overall minus sign by (B.3). This space is invariant under conjugation by every \(\lambda(h)\): the projection of \([X,Y]\) to \(\mathfrak h\) commutes with \(\operatorname{Ad}_h\), and conjugating its action on \(\mathfrak m\) gives the action of \(\operatorname{Ad}_h[X,Y]_{\mathfrak h}\). Differentiating this invariance makes the space stable under brackets with \(\lambda_*(\mathfrak h)=W(\mathfrak g)\). Thus \(V_1=V_0\), which proves (D.2).

The principal connection on \(G\to G/H\) with horizontal spaces \(dL_g\mathfrak m\) is constructed in Invariant connections C.2, and induces this tangent connection through \(\lambda\). A lifted loop starting at \(e\) ends in \(H\), and parallel tangent vectors are \(j_{g(t)}v\). At its endpoint their transformation is \(\lambda(h)\), proving containment of full canonical holonomy in \(\lambda(H)\). Normality of restricted holonomy under every \(\lambda(h)\) follows because conjugation preserves the Lie algebra (D.2) and hence preserves the subgroup generated by its exponentials. Uniqueness of that connected analytic subgroup is also proved in [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1).

For strictness take the Euclidean motion presentation
\[
(\mathbb R^n\rtimes\mathrm{SO}(n))/\mathrm{SO}(n)=\mathbb R^n,\qquad n\geq2.
\]
Translation vectors form \(\mathfrak m=\mathbb R^n\), whose brackets vanish. The canonical connection is ordinary coordinate differentiation by (A.2), so transport around every loop is the identity. Its holonomy is trivial, whereas \(\lambda(H)=\mathrm{SO}(n)\) is not: a nontrivial rotation in a coordinate two-plane gives an element different from the identity. Thus even normality does not imply equality. □

**Exercise D.2 (The sphere, its reductive complement and its holonomy).** For \(n\geq1\), identify \(S^n\) with \(\mathrm{SO}(n+1)/\mathrm{SO}(n)\) at \(e_0=(1,0,\ldots,0)\). Compute the canonical torsion, curvature, geodesics and full holonomy.

**Solution.** [De Rham Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2) proves transitivity of \(\mathrm{SO}(n+1)\) on this sphere. Its stabilizer at \(e_0\) consists exactly of \(\operatorname{diag}(1,h)\) with \(h\in\mathrm{SO}(n)\): the first column is \(e_0\), orthogonality forces the first row as well, and the remaining determinant is one. The transitive-action submersion of Invariant connections A.2 and the quotient charts of [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) identify the quotient smoothly with \(S^n\).

Every skew matrix splits uniquely as a stabilizer matrix plus
\[
A(x)=
\begin{pmatrix}0&-x^{\mathsf T}\\x&0\end{pmatrix},
\qquad x\in\mathbb R^n.
\]
These \(A(x)\) form an \(\operatorname{Ad}(H)\)-invariant complement, with \(A(x)e_0=(0,x)\) and
\(\operatorname{Ad}_{\operatorname{diag}(1,h)}A(x)=A(hx)\). The isotropy representation is therefore the ordinary \(\mathrm{SO}(n)\) representation. Direct multiplication gives
\[
[A(x),A(y)]
=\begin{pmatrix}0&0\\0&yx^{\mathsf T}-xy^{\mathsf T}\end{pmatrix}.
\]
Its \(\mathfrak m\) component is zero, so (B.3) gives \(T=0\) and
\[
R(x,y)z=\langle y,z\rangle x-\langle x,z\rangle y.
\tag{D.3}
\]
The Euclidean inner product on \(\mathfrak m\) gives the round metric. With zero projected bracket, C.1 gives its Levi-Civita product \(\alpha=0\); thus this is exactly the canonical connection. Its geodesics are the \(G\)-translates of
\[
\exp(tA(x))e_0
=\cos(t|x|)e_0+\frac{\sin(t|x|)}{|x|}(0,x)
\]
when \(x\ne0\), and the constant curve when \(x=0\). To verify the formula, the right side has initial value \(e_0\) and satisfies \(c'=A(x)c\), since \(A(x)e_0=(0,x)\) and \(A(x)(0,x)=-|x|^2e_0\). Uniqueness of the linear ODE in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) identifies it with the exponential.

For \(n\geq2\), taking \(x,y\) to be distinct coordinate vectors shows that the curvature endomorphisms span all elementary skew matrices, hence \(\mathfrak{so}(n)\). [De Rham Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2) proves that \(\mathrm{SO}(n)\) is connected. The connected subgroup generated by exponentials of its whole Lie algebra is the group itself: the exponential is a local diffeomorphism at zero by [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), so this subgroup is open, and its disjoint open cosets would otherwise disconnect the group. D.1 therefore gives restricted holonomy \(\mathrm{SO}(n)\). Full holonomy is contained in the same isotropy group, so it too is \(\mathrm{SO}(n)\). For \(n=1\), the isotropy group and both holonomy groups are trivial; (D.3) vanishes in one dimension, consistently with this conclusion. □

## E. Homogeneity and the intrinsic product factors

The metric in this section is positive definite. The Euclidean factor of the de Rham decomposition is kept as one factor; zero-dimensional factors are omitted.

**Theorem E.1 (Connected closed groups on the factors).** Suppose \(G\) is connected and acts transitively by isometries on a simply connected Riemannian manifold \(M=G/H\). For each based factor leaf \(L_i\) of its de Rham decomposition, its set stabilizer
\[
K_i=\{g\in G:gL_i=L_i\}
\]
is a closed connected Lie subgroup containing \(H\). It acts transitively on \(L_i\), and
\[
L_i\cong K_i/H
\tag{E.1}
\]
as a homogeneous Riemannian manifold.

**Proof.** Hopf–Rinow B.3 proves completeness of a homogeneous Riemannian manifold. [De Rham E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3) therefore supplies a finite product \(M=\prod_i M_i\) of complete simply connected factors, with each \(L_i\) the \(i\)-th axis through \(o=(o_j)_j\). [De Rham K.5](holonomy-and-the-de-rham-decomposition-theorem.md#corollary-k-5) proves that a connected group of isometries preserves each of the factor foliations and acts as a product of factor isometries. The given action is continuous in the compact-open topology used there: for a compact subset, continuity of the smooth action gives a common parameter neighbourhood with any prescribed uniform displacement bound, by a finite covering of that subset. Thus connectedness of \(G\) really does put its image in the identity component considered in that theorem.

Write \(g_j\) for the action on \(M_j\). Then
\[
K_i=\{g:g_j(o_j)=o_j\text{ for every }j\ne i\},
\tag{E.2}
\]
because the factors are preserved and \(g_i\) maps \(M_i\) onto itself. This is a closed subgroup and contains \(H\). Invariant connections A.1 makes it an embedded Lie subgroup. If \(p\in L_i\), transitivity on \(M\) supplies \(g\) with \(go=p\); its other coordinates satisfy (E.2), so \(g\in K_i\). This proves transitivity on the leaf. Its stabilizer of \(o\) is \(H\), and the transitive-action theorem in Invariant connections A.2, together with [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup), gives the diffeomorphism (E.1). The induced metric is invariant under \(K_i\), giving the Riemannian statement.

It remains to prove connectedness, which does not follow from transitivity alone. The action of \(G\) on \(N_i=\prod_{j\ne i}M_j\) is transitive: complete a specified point of \(N_i\) by \(o_i\) and use transitivity on \(M\). Its stabilizer is \(K_i\). The same quotient theorem gives \(G/K_i\cong N_i\). This base is simply connected: loops and homotopies in a finite product are exactly their coordinate loops and homotopies.

Let \(K_i^0\) be the identity component of \(K_i\). Components of a Lie group are open, since coordinate balls are locally path connected, and are closed as components of a topological space. Thus \(K_i^0\) is a closed Lie subgroup. The natural map
\[
G/K_i^0\longrightarrow G/K_i
\tag{E.3}
\]
is a covering. Indeed a local principal-bundle section for \(G\to G/K_i\), supplied by [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup), identifies its inverse image in (E.3) with \(U\times(K_i/K_i^0)\). The second factor is discrete, giving disjoint sheets over \(U\). The space \(G/K_i^0\) is connected as an image of connected \(G\). The complete covering classification of [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) says that a connected covering of a simply connected base has one sheet. Hence \(K_i/K_i^0\) has one point, and \(K_i=K_i^0\). If there is only one factor, the other-factor product is a point and the same reasoning simply gives \(K_i=G\). □

**Theorem E.2 (The ideals generated by naturally reductive factors).** Under E.1, suppose additionally that the action is effective and a reductive complement makes the metric naturally reductive. Identify
\(\mathfrak m=\bigoplus_i\mathfrak m_i\) with the de Rham tangent splitting at \(o\). Then
\[
[\mathfrak m_i,\mathfrak m_j]=0\quad(i\ne j).
\tag{E.4}
\]
Define
\[
\mathfrak h_i=\operatorname{span}\{[X,Y]_{\mathfrak h}:X,Y\in\mathfrak m_i\},
\qquad \mathfrak k_i=\mathfrak m_i\oplus\mathfrak h_i.
\]
Each \(\mathfrak k_i\) is an ideal in \(\mathfrak g\), distinct such ideals commute, and the ideal generated by \(\mathfrak m\) is
\[
\mathfrak k(\mathfrak m)=\mathfrak m+[\mathfrak m,\mathfrak m]
=\bigoplus_i\mathfrak k_i,\qquad
\mathfrak h\cap\mathfrak k(\mathfrak m)=\bigoplus_i\mathfrak h_i.
\tag{E.5}
\]
The ideal \(\mathfrak k(\mathfrak m)\) need not be all of \(\mathfrak g\).

**Proof.** E.1 and [De Rham K.5](holonomy-and-the-de-rham-decomposition-theorem.md#corollary-k-5) make the orthogonal projections onto the factor distributions \(G\)-invariant. B.2 makes them parallel for the canonical connection \(\bar\nabla\); they are parallel for the Levi-Civita connection \(\nabla\) by [De Rham E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3). Hence their commutators with the difference \(S=\nabla-\bar\nabla\) vanish: applying the tensor derivative rule of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) to a projection \(P\) gives \(0=(\nabla_XP-\bar\nabla_XP)=[S_X,P]\). Thus every \(S_X\) preserves each factor. C.2 identifies
\[
S_XY=\tfrac12[X,Y]_{\mathfrak m}.
\]
For \(X\in\mathfrak m_i,Y\in\mathfrak m_j\), \(i\ne j\), this lies in \(\mathfrak m_j\); reversing \(X,Y\) places its negative in \(\mathfrak m_i\). Their intersection is zero, so \([X,Y]_{\mathfrak m}=0\).

For \(X\in\mathfrak m_i\), the operator \(\Lambda(X)=\tfrac12[X,\cdot]_{\mathfrak m}\) vanishes on every other summand and preserves \(\mathfrak m_i\). Thus if \(Y\in\mathfrak m_j\), \(i\ne j\), the two operators commute and the projected bracket is zero. The curvature formula (B.2) reduces to
\[
R(X,Y)=-\operatorname{ad}([X,Y]_{\mathfrak h})|_{\mathfrak m}.
\]
Mixed curvature is zero by [De Rham C.3](holonomy-and-the-de-rham-decomposition-theorem.md#corollary-c-3), so the right side vanishes.

Here the isotropy action of \(\mathfrak h\) on \(\mathfrak m\) is faithful. To prove this, if \(A\in\mathfrak h\) acts as zero, \(\exp(tA)\) fixes \(o\) and has identity derivative there for every \(t\); the derivative is \(\exp(t\lambda_*A)\) by the representation ODE. An isometry preserves geodesics and their initial derivatives by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Hence it fixes every \(\exp_o(v)\). Hopf–Rinow B.2 makes \(\exp_o\) surjective, so it fixes all of \(M\). Effectiveness gives \(\exp(tA)=e\) for every \(t\), and differentiation gives \(A=0\). Apply this to \([X,Y]_{\mathfrak h}\). This proves (E.4).

The full subgroup \(H\) preserves the factor splitting, so its adjoint action preserves every \(\mathfrak m_i\), and equivariance of the bracket projection preserves every \(\mathfrak h_i\). In particular
\[
[\mathfrak h,\mathfrak m_i]\subseteq\mathfrak m_i,\qquad
[\mathfrak h,\mathfrak h_i]\subseteq\mathfrak h_i.
\tag{E.6}
\]
For \(X,Y\in\mathfrak m_i\), \([X,Y]_{\mathfrak m}\in\mathfrak m_i\), as already follows from preservation by \(S_X\). If \(Z\in\mathfrak m_j\), \(j\ne i\), Jacobi and (E.4) give
\[
[[X,Y]_{\mathfrak h},Z]
=[[X,Y],Z]-[[X,Y]_{\mathfrak m},Z]=0.
\]
Thus \(\mathfrak h_i\) annihilates each other \(\mathfrak m_j\). For \(A\in\mathfrak h_i\) and \(Y,Z\in\mathfrak m_j\), differentiation of bracket-projection equivariance gives
\[
[A,[Y,Z]_{\mathfrak h}]
=[[A,Y],Z]_{\mathfrak h}+[Y,[A,Z]]_{\mathfrak h}=0.
\]
Therefore \([\mathfrak h_i,\mathfrak h_j]=0\) for \(i\ne j\). Equations (E.4) and (E.6), and
\([\mathfrak m_i,\mathfrak m_i]\subseteq\mathfrak m_i+\mathfrak h_i\), now show both that each \(\mathfrak k_i\) is an ideal of
\(\mathfrak g=\mathfrak h+\sum_j\mathfrak m_j\) and that the different \(\mathfrak k_i\) commute.

The sum of the \(\mathfrak h_i\) is direct. If \(\sum_i A_i=0\), \(A_i\in\mathfrak h_i\), apply its isotropy action to \(\mathfrak m_j\). All terms except \(A_j\) vanish, so \(A_j\) annihilates \(\mathfrak m_j\) too. It then annihilates all of \(\mathfrak m\), and faithfulness gives \(A_j=0\). Together with the directness of \(\mathfrak h\oplus\mathfrak m\), this proves directness in (E.5). Its right side is an ideal containing \(\mathfrak m\), and is contained in every ideal containing \(\mathfrak m\), since each bracket projection \([X,Y]_{\mathfrak h}\) is \([X,Y]-[X,Y]_{\mathfrak m}\). This proves the equality with the generated ideal and its displayed intersection with \(\mathfrak h\).

Finally the effective Euclidean motion example of D.1, with \(n\geq2\), is naturally reductive, simply connected and has one Euclidean factor. Its translation complement is abelian. Thus \(\mathfrak k(\mathfrak m)=\mathbb R^n\), while
\(\mathfrak g=\mathbb R^n\rtimes\mathfrak{so}(n)\) is larger. All the stated hypotheses hold, so equality with \(\mathfrak g\) would be false. □

## F. Invariant almost complex structures and the six-sphere

An almost complex structure is a smooth tangent endomorphism \(J\) with \(J^2=-I\). It comes from complex coordinates if the manifold has charts to open subsets of \(\mathbb C^k\) in which \(J\) is multiplication by \(i\) and the transition maps are holomorphic.

**Lemma F.1 (The invariant Nijenhuis obstruction).** For an almost complex structure, the expression
\[
N_J(U,V)=[JU,JV]-[U,V]-J[JU,V]-J[U,JV]
\tag{F.1}
\]
is a skew bilinear tensor. It vanishes for every almost complex structure coming from complex coordinates. On a reductive \(G/H\), invariant almost complex structures correspond precisely to the \(H\)-equivariant endomorphisms \(I:\mathfrak m\to\mathfrak m\) with \(I^2=-1\), and
\[
(N_J)_o(X,Y)
=[IX,IY]_{\mathfrak m}-[X,Y]_{\mathfrak m}
-I[IX,Y]_{\mathfrak m}-I[X,IY]_{\mathfrak m}.
\tag{F.2}
\]
In particular (F.2) is a necessary algebraic condition for invariant complex coordinates.

**Proof.** Real bilinearity and skew symmetry follow from the bracket. To check multiplication by a smooth scalar \(f\) in the first slot, the four additional derivative terms in \(N_J(fU,V)-fN_J(U,V)\) are, respectively,
\[
-(JVf)JU,\qquad (Vf)U,\qquad
(Vf)J(JU),\qquad +(JVf)JU.
\]
They cancel since \(J^2=-1\). Skew symmetry gives scalar linearity in the other slot. Hence the expression depends only on the values of the vector fields at a point and is a tensor. In complex coordinates its value on each pair of real coordinate fields is zero: those fields and their \(J\)-images have constant coefficients and commute. Tensoriality makes it zero everywhere.

An invariant \(J\) is determined by \(I=j_e^{-1}J_oj_e\). Changing the representative \(g\) of a coset in the translation formula \(J_{gH}=j_gIj_g^{-1}\) shows that it is well defined exactly when \(I\lambda(h)=\lambda(h)I\) for all \(h\). The local sections used in A.1 give smoothness, and squaring gives \(J^2=-1\) precisely when \(I^2=-1\). These operations are inverse.

For such an invariant \(J\), B.2 gives \(\bar\nabla J=0\). Substitute
\[
[U,V]=\bar\nabla_UV-\bar\nabla_VU-\bar T(U,V)
\]
into each bracket of (F.1). For example,
\(\bar\nabla_{JU}(JV)=J\bar\nabla_{JU}V\), and
\(J\bar\nabla_U(JV)=-\bar\nabla_UV\).
The eight covariant-derivative terms cancel in pairs. The remaining expression is
\[
-\bar T(JU,JV)+\bar T(U,V)+J\bar T(JU,V)+J\bar T(U,JV).
\]
At \(o\), use \(\bar T(X,Y)=-[X,Y]_{\mathfrak m}\) from (B.3) to obtain (F.2). The proof establishes the stated obstruction without presupposing any converse integrability theorem. □

**Theorem F.2 (Cayley triples and their stabilizers).** Let
\(\mathbb O=\mathbb H\oplus\mathbb H\) be the octonions with multiplication
\[
(a,b)(c,d)=(ac-\overline d\,b,\ da+b\overline c).
\tag{F.3}
\]
Put \(i=(i,0)\), \(j=(j,0)\), \(e=(0,1)\). Given unit imaginary octonions \(\xi,\eta,\zeta\) with
\[
\xi\perp\eta,\qquad
\zeta\perp\operatorname{span}_{\mathbb R}\{\xi,\eta,\xi\eta\},
\]
there is exactly one real algebra automorphism \(A\) with
\[
A(i)=\xi,\qquad A(j)=\eta,\qquad A(e)=\zeta.
\tag{F.4}
\]
In particular it sends the orthonormal basis
\[
1,i,j,ij,e,ie,je,(ij)e
\]
to
\[
1,\xi,\eta,\xi\eta,\zeta,\xi\zeta,\eta\zeta,(\xi\eta)\zeta,
\tag{F.5}
\]
with all products transported by that map. The stabilizer of a unit imaginary octonion in \(G_2=\operatorname{Aut}_{\mathbb R}(\mathbb O)\) is exactly \(\mathrm{SU}(3)\); the stabilizer of an ordered orthonormal imaginary pair is \(\mathrm{SU}(2)\).

**Proof.** [De Rham Z.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-1) proves (F.3), its norm, conjugation and alternativity, and [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2) proves that automorphisms are orthogonal and that \(v\mapsto uv\) is an orthogonal complex structure on \(u^\perp\cap\operatorname{Im}\mathbb O\) for unit imaginary \(u\). [De Rham Z.7](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-7) proves that \(G_2\) is transitive on the unit imaginary sphere. Choose an automorphism \(A_1\) sending \(i\) to \(\xi\).

We recall exactly what the stabilizer proof supplies. At \(i\), [De Rham Z.6](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-6) uses the complex basis with real vectors \(j,e,je\) and imaginary partners \(ij,ie,-(ij)e\). It writes the octonion three-form as
\[
\varphi=i^*\wedge\omega+\operatorname{Re}\Omega,
\tag{F.6}
\]
where \(\omega\) is the Hermitian two-form and \(\Omega\) is the complex volume form in that basis. An automorphism fixing \(i\) preserves the metric and commutes with multiplication by \(i\), hence is unitary on the complex three-space \(i^\perp\). Preservation of \(\operatorname{Re}\Omega\), evaluated on a real complex basis and then with its first vector multiplied by \(i\), forces its complex determinant to be one. Conversely every special unitary transformation preserves both summands in (F.6), and [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2) proves directly that an orthogonal transformation preserving \(\varphi\) extends by fixing \(1\) to an octonion automorphism. This gives both inclusions in the stabilizer assertion; conjugating by \(A_1\) gives the assertion at \(\xi\).

[De Rham Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2) proves that \(\mathrm{SU}(3)\) acts transitively on the unit sphere of its complex three-space. The vector \(A_1(j)\) and the prescribed \(\eta\) are both unit vectors perpendicular to \(\xi\). There is consequently an automorphism \(A_2\) fixing \(\xi\) and sending \(A_1(j)\) to \(\eta\). The composition \(B=A_2A_1\) fixes the prescribed images of \(i,j\), and hence also sends \(ij\) to \(\xi\eta\).

Within this \(\mathrm{SU}(3)\), the subgroup fixing the real vector \(\eta\) fixes its complex partner \(\xi\eta\) as well. In an orthonormal complex basis starting with \(\eta\), its matrices are exactly \(\operatorname{diag}(1,C)\), \(C\in\mathrm{SU}(2)\): unitarity forces the zero off-diagonal blocks, and determinant one forces \(\det C=1\). The remaining complex two-space is the real orthogonal complement of \(\xi,\eta,\xi\eta\) in the imaginary octonions. Both \(B(e)\) and \(\zeta\) are unit vectors there. The \(\mathrm{SU}(2)\) sphere transitivity proved in [De Rham Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2) supplies \(A_3\) fixing \(\xi,\eta\) and sending \(B(e)\) to \(\zeta\). Then \(A=A_3B\) has (F.4).

The basis in (F.5) on the source side is the real orthonormal basis of the two quaternion summands in (F.3). Every automorphism fixes \(1\) and preserves products. Therefore its values on \(i,j,e\) force its values on this entire basis, proving uniqueness. Existence and orthogonality prove that the target list is also orthonormal. Multiplication is transported because \(A\) is an automorphism, not merely an orthogonal linear map. More explicitly, writing \(Q=\operatorname{span}(1,\xi,\eta,\xi\eta)\), the transported formula is
\[
(a+b\zeta)(c+d\zeta)
=(ac-\overline d\,b)+(da+b\overline c)\zeta
\quad(a,b,c,d\in Q).
\tag{F.7}
\]
Indeed \(A\) restricts to the quaternion algebra isomorphism from the first summand onto \(Q\); it preserves conjugation since it preserves real parts and fixes \(1\). Apply \(A\) to (F.3), where \((a,b)=a+be\). This proves every case of (F.7) with its multiplication order. The block argument above proves the ordered-pair stabilizer assertion as well. □

**Theorem F.3 (All invariant almost complex structures on \(S^6\)).** On
\[
S^6=\{p\in\operatorname{Im}\mathbb O:|p|=1\}=G_2/\mathrm{SU}(3)
\]
there are exactly two \(G_2\)-invariant almost complex structures:
\[
J_pv=p\times v,\qquad -J_pv=-p\times v
\quad(v\perp p).
\tag{F.8}
\]
Neither comes from complex coordinates.

**Proof.** The cross product and its square identity are proved in [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2). Thus \(J_p^2v=-v\) on \(p^\perp\), its image is tangent, and it is smooth because the cross product is bilinear. Automorphisms preserve that product, so \(J\) and \(-J\) are invariant.

The sphere quotient and its full stabilizer are proved in [De Rham Z.7](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-7) and [De Rham Z.6](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-6). An invariant tangent endomorphism is therefore determined by its value at \(p=i\), which must commute with the standard real action of \(\mathrm{SU}(3)\) on \(\mathbb C^3\). To compute this commutant directly, let \(L\) be such a real-linear endomorphism. The central scalar
\(\zeta=-\tfrac12+\tfrac{\sqrt3}{2}i\) has \(\zeta^3=1\), so \(\zeta I\in\mathrm{SU}(3)\). Commutation with it gives commutation with
\[
J_i=\frac{2}{\sqrt3}\bigl(\zeta I+\tfrac12 I\bigr).
\]
Hence \(L\) is complex linear. Commutation with both
\(\operatorname{diag}(-1,-1,1)\) and
\(\operatorname{diag}(-1,1,-1)\) forces it to preserve each complex coordinate line, since their pairs of eigenvalues distinguish the three lines. Its matrix is thus complex diagonal. A cyclic permutation of the three coordinate vectors is unitary of determinant one; commutation with it makes the three diagonal entries equal. Consequently \(L=a+bJ_i\) with real \(a,b\). The equation \(L^2=-1\) gives
\[
a^2-b^2=-1,\qquad 2ab=0.
\]
If \(b=0\) the first equation is impossible over \(\mathbb R\); otherwise \(a=0\) and \(b=\pm1\). Transitivity then makes the invariant almost complex structure exactly \(J\) or \(-J\) everywhere.

We compute the obstruction of F.1 at one point, directly in the established octonion table. Fix \(p\in S^6\) and \(u,v\perp p\). Extend them to tangent fields
\[
U(q)=u-\langle u,q\rangle q,\qquad
V(q)=v-\langle v,q\rangle q.
\]
Since \(q\times q=0\), one has \(JU(q)=q\times u\) and \(JV(q)=q\times v\). With the bracket convention \([A,B]=DB(A)-DA(B)\), differentiating these ambient formulas at \(p\) gives
\[
\begin{aligned}
[U,V]_p&=0,\\
[JU,JV]_p&=(p\times u)\times v-(p\times v)\times u,\\
[JU,V]_p&=u\times v-cp,\\
[U,JV]_p&=u\times v-cp,\qquad
c=\langle p\times u,v\rangle.
\end{aligned}
\tag{F.9}
\]
For clarity, \(DV_p(w)=-\langle v,w\rangle p\) and
\(DU_p(w)=-\langle u,w\rangle p\) for tangent \(w\), since \(u,v\perp p\); meanwhile \(D(JU)_p(w)=w\times u\) and \(D(JV)_p(w)=w\times v\). These four identities give (F.9), using alternation of
\(\langle a\times b,c\rangle\) from [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2). The two mixed brackets are tangent because the normal component of \(u\times v\) is \(cp\).

Applying (F.1), and using \(p\times p=0\), now yields
\[
(N_J)_p(u,v)
=(p\times u)\times v-(p\times v)\times u-2p\times(u\times v).
\tag{F.10}
\]
Use the exact basis of [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2):
\[
e_1=(i,0),\ e_2=(j,0),\ e_3=(ij,0),\
e_4=(0,1),\ e_5=(0,i),\ e_6=(0,j),\ e_7=(0,ij).
\]
Its table gives
\[
\begin{aligned}
e_1\times e_2&=e_3,& e_1\times e_4&=e_5,\\
e_2\times e_4&=e_6,& e_1\times e_6&=-e_7,\\
e_3\times e_4&=e_7,& e_5\times e_2&=-e_7.
\end{aligned}
\]
At \(p=e_1,u=e_2,v=e_4\), (F.10) is therefore
\[
(N_J)_{e_1}(e_2,e_4)=e_7-(-e_7)-2(-e_7)=4e_7\ne0.
\]
Each term in (F.1) is unchanged when \(J\) is replaced by \(-J\), so \(N_{-J}=N_J\). F.1 excludes complex coordinates for both invariant structures. This conclusion concerns precisely the \(G_2\)-invariant structures classified here. □

## G. From the invariant obstruction to complex coordinates

We now prove the converse to the obstruction in F.1. The analytic method is described in Daniel Beltiţă's free arXiv preprint listed below. We give the finite-dimensional analytic and Frobenius arguments in full, including the analyticity of the homogeneous charts.

**Lemma G.1 (Complex power series, flows and analytic Cauchy–Riemann equations).** Locally absolutely convergent complex power series admit termwise derivatives, compositions, local inverses with invertible complex derivative, and local flows with analytic dependence on complex time and parameters. A real-analytic map extends locally to such a series in the complexified variables, uniquely near the real slice. If a real-analytic map between open subsets of complex vector spaces has complex-linear real derivative at every point, it is locally a convergent power series in the complex coordinates alone.

**Proof.** Here a holomorphic power series means
\(f(z)=\sum_{\nu\in\mathbb N^d}c_\nu z^\nu\) with complex coefficients and
\(\sum_\nu|c_\nu|r^\nu<\infty\) for some positive radius vector \(r\).
[Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) proves completeness and the product bound in the coefficient norm
\[
\|f\|_r=\sum_\nu |c_\nu|r^\nu,
\qquad \|fg\|_r\leq\|f\|_r\|g\|_r.
\tag{G.1}
\]
That proof uses limits of coefficients, absolute values and the triangle inequality, so it applies unchanged to complex coefficients: a Cauchy coefficient sequence converges in \(\mathbb C=\mathbb R^2\), and its finite partial sums satisfy the same bounds. On smaller radii, the bounds on \(|\nu|^kq^{|\nu|}\), \(q<1\), prove uniform convergence of every derivative series. The proof there of differentiation by passage from polynomial sums works along real and imaginary coordinate segments, giving the complex derivatives. It also proves convergence of substitutions by the majorant
\(\sum_\nu |c_\nu|\prod_j\|w_j\|_r^{\nu_j}\).

For specificity the inverse and flow constructions require no complex-analysis existence theorem. Normalize an equation with invertible unknown derivative to \(u=T(u,z)\), with \(T(0,0)=0\) and \(D_uT(0,0)=0\), as in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). Choose an unknown coefficient-norm ball of radius \(b\) and parameter radii small enough that the substituted derivative of \(T\) has norm at most \(q<1\) and
\(\|T(0,z)\|_r<(1-q)b\). The monomial difference identity bounds
\(\|T(u,z)-T(v,z)\|_r\leq q\|u-v\|_r\) over complex coefficients too. The contraction proof in [Local tools 1.1](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a unique power-series fixed point. With the equation \(f(u)-z=0\), this constructs the inverse, and pointwise uniqueness makes it the inverse map on small neighbourhoods.

For the equation \(u'=F(t,u,\lambda)\), use
\[
u=\eta+\int_0^t F(s,u(s),\lambda)\,ds.
\tag{G.2}
\]
In the coefficient algebra, integration of \(t^j\) replaces it by \(t^{j+1}/(j+1)\), so its norm is at most the time radius. With bounds \(M,L\) for the substituted \(F,D_uF\), choose that radius with \(r_tM<b/2\), \(r_tL<1\), and \(\|\eta\|<b/2\). Contraction gives a series in \(t,\eta,\lambda\). Termwise differentiation proves (G.2), and the same contraction gives uniqueness. This proves the claimed holomorphic flows and parameter dependence. Restricted to real time, uniqueness in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) identifies them with the ordinary smooth flows. Finitely many compositions extend parameter analyticity along any already existing compact real-time segment, as proved in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1).

A real-analytic series in real variables, with real or complex values, has the same absolute convergence bound after those variables are allowed to be complex. It therefore extends as stated. If such a complex series vanishes on a real neighbourhood, all its derivatives in the real coordinate directions vanish at the centre. Termwise differentiation identifies these derivatives with the factorial multiples of all its complex coefficients; those coefficients are zero. This proves local uniqueness and allows analytic identities valid on the real slice to be complexified.

Finally write the real coordinates of \(\mathbb C^k\) as \(x,y\). Substitute
\[
x_j=\tfrac12(z_j+w_j),\qquad
y_j=\tfrac1{2i}(z_j-w_j)
\]
in a real-analytic series for a component of the given map, and shrink radii. The composition bound above gives an absolutely convergent series
\(\sum_{\alpha,\beta}a_{\alpha\beta}z^\alpha w^\beta\), representing the map when \(w=\bar z\). Complex linearity of the real derivative is precisely
\(\partial f/\partial\bar z_j=\tfrac12(\partial_{x_j}+i\partial_{y_j})f=0\).
Termwise differentiation gives
\(\sum_{\alpha,\beta}\beta_j a_{\alpha\beta}z^\alpha w^{\beta-e_j}=0\) on that slice. Substitution back to \(x,y\), followed by uniqueness of real power-series coefficients, makes this a zero series. The invertible linear change between the formal variables \((x,y)\) and \((z,w)\) then makes every \(\beta_j a_{\alpha\beta}\) zero. Thus only \(\beta=0\) terms survive. This is the required holomorphic power series in \(z\). □

**Theorem G.2 (Holomorphic Frobenius in finite dimensions).** Let \(D\) be a rank-\(r\) complex distribution on an open subset of \(\mathbb C^N\), locally spanned by holomorphic power-series vector fields. Suppose the bracket of any two such local sections belongs to \(D\). Near each point there are holomorphic coordinates in which \(D\) is the span of the first \(r\) coordinate fields. Equivalently, it is the kernel of a holomorphic submersion to \(\mathbb C^{N-r}\).

**Proof.** We induct on \(r\). For \(r=0\) any holomorphic coordinate chart works. If \(r>0\), choose a local frame \(X_1,\ldots,X_r\) with \(X_1\ne0\) at the chosen point. A complex-linear coordinate change makes the first component of \(X_1\) nonzero there. G.1 supplies its holomorphic flow. The map
\[
(t,w)\longmapsto \Phi_{X_1}^t(0,w)
\]
has derivative whose columns are \(X_1(0)\) and the remaining coordinate vectors. They are independent. The holomorphic inverse of G.1 therefore provides coordinates \((t,w)\) in which \(X_1=\partial_t\).

Subtract from the other frame fields their \(\partial_t\) components times \(X_1\). The resulting fields \(B_2,\ldots,B_r\) have only \(w\)-components, remain independent, and together with \(\partial_t\) span \(D\). Involutivity gives
\[
\partial_t B=B\,C(t,w),
\tag{G.3}
\]
where \(B\) is the matrix of their columns and \(C\) is a holomorphic \((r-1)\)-square matrix. To see that its entries are holomorphic, choose a nonzero \((r-1)\)-minor of \(B\) at the base point and restrict to where it stays invertible. The coefficients of any field in their span are then obtained by applying that holomorphic inverse matrix to the selected components. The absence of a \(\partial_t\) component eliminates any \(X_1\) term.

Solve the parameter-dependent matrix equation
\[
\partial_t P=-CP,\qquad P(0,w)=I.
\]
G.1 gives a holomorphic solution, invertible after shrinking because its determinant is initially one. Equation (G.3) implies \(\partial_t(BP)=0\). Thus the columns of \(\widehat B=BP\) are independent of \(t\), as follows also by comparing their power-series coefficients. They define a rank-\((r-1)\) holomorphic distribution on the \(w\)-space. It is involutive: the brackets have no \(\partial_t\) component, are independent of \(t\), and belong to \(D\); therefore they belong to the span of \(\widehat B\). Apply induction in dimension \(N-1\) to obtain holomorphic \(w\)-coordinates straightening it. Keep \(t\) as the first coordinate. These coordinates straighten \(D\), and projection to the last \(N-r\) coordinates is the desired submersion. If \(r=1\) the matrix step is empty; if \(r=N\) the target is the zero-dimensional complex vector space. □

**Lemma G.3 (Analytic homogeneous coordinates).** A smooth finite-dimensional Lie group has a compatible real-analytic atlas of translated exponential charts. Its left translations are analytic in these charts. For a closed subgroup \(H\) and a vector-space complement \(\mathfrak m\) to \(\mathfrak h\), the charts
\[
v\longmapsto g\exp(v)H,\qquad v\in\mathfrak m\text{ near }0,
\tag{G.4}
\]
give a compatible real-analytic atlas on \(G/H\), and left translation by \(G\) is analytic. If the complement is \(H\)-invariant and \(I\) commutes with its isotropy action, the invariant endomorphism \(j_gIj_g^{-1}\) is real analytic.

**Proof.** [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) provide exponential charts in the existing smooth structure. We compute their left Maurer–Cartan matrix. For
\(F(t,s)=\exp(t(v+sw))\), write
\(a=\theta_G(\partial_tF)=v+sw\) and
\(b=\theta_G(\partial_sF)\). Pullback of the Maurer–Cartan equation from [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3) gives
\[
\partial_t b-\partial_s a+[a,b]=0.
\]
At \(s=0\), this is \(b'=w-[v,b]\), \(b(0)=0\). The explicit solution is
\(\int_0^t e^{-(t-u)\operatorname{ad}v}w\,du\): differentiating the matrix power series verifies the equation, and [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives uniqueness. Thus
\[
(\exp^*\theta_G)_v(w)=B(v)w,\qquad
B(v)=\int_0^1 e^{-t\operatorname{ad}v}\,dt
=\sum_{\ell=0}^\infty\frac{(-\operatorname{ad}v)^\ell}{(\ell+1)!}.
\tag{G.5}
\]
In fixed finite-dimensional norms \(\|\operatorname{ad}v\|\leq C\|v\|\), so the displayed series and its coefficient majorants converge on bounded small boxes. It is real analytic. As \(B(0)=I\), it is invertible near zero, with analytic inverse by [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). A left-invariant field with coefficient \(X\) therefore has coordinate expression \(B(v)^{-1}X\), an analytic function of \(v,X\).

In an exponential chart, multiplication \(\exp(v)\exp(u)\), where the indicated points and path remain in the chart, is computed by the time-one solution of
\[
z'(t)=B(z(t))^{-1}u,\qquad z(0)=v.
\tag{G.6}
\]
Indeed its group curve has constant left velocity \(u\). For \(v\) near any fixed chart point and \(u\) sufficiently small, smooth existence keeps the whole path in the chart. Analytic ODE dependence in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) makes its endpoint \(\mu(v,u)\) analytic in \(v,u\).

We check chart compatibility. Suppose a point in two translated exponential charts has coordinates \(v_0,w_0\), so
\(g\exp(v_0)=h\exp(w_0)\). Nearby points are uniquely
\[
g\exp(v_0)\exp(u)=h\exp(w_0)\exp(u)
\]
for small \(u\). Their two coordinates are \(\mu(v_0,u)\) and \(\mu(w_0,u)\). The derivative of the first map in \(u\) at zero is invertible by (G.5). Its analytic inverse, followed by the second map, is the coordinate transition. This proves an analytic atlas. Left multiplication takes a chart centred at \(g\) to the chart centred at \(ag\) with the same coordinate \(v\), so every left translation is analytic. Right multiplication is analytic too: exponential conjugation from [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives \(g\exp(v)a=ga\exp(\operatorname{Ad}_{a^{-1}}v)\), a fixed linear coordinate change in charts centred at \(g\) and \(ga\).

The subgroup exponential is the restriction of the ambient exponential: its left-invariant ODE has the same image curve, by uniqueness in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). For \(v\in\mathfrak m,Z\in\mathfrak h\) near zero, the group coordinates of
\(\exp(v)\exp(Z)\) are therefore the analytic function \(\mu(v,Z)\). Its derivative at \((0,0)\) is \((v,Z)\mapsto v+Z\), an isomorphism. Analytic inversion gives a local product chart and an analytic map to its \(v\)-coordinate. The smooth quotient construction of [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) identifies this \(v\)-coordinate with the quotient chart (G.4). To check transitions, suppose \(g\exp(v_0)H=h\exp(w_0)H\), and choose \(k_0\in H\) with \(g\exp(v_0)=h\exp(w_0)k_0\). For \(v\) near \(v_0\), the analytic lift \(g\exp(v)k_0^{-1}\) lies near \(h\exp(w_0)\) in the second translated product chart. Taking its analytic \(\mathfrak m\)-coordinate gives the second quotient coordinate, since right multiplication by \(k_0^{-1}\) leaves its coset unchanged. This proves analytic compatibility even when the two representatives differ by an element of \(H\). Left translation sends the quotient chart centred at \(gH\) to the one centred at \(agH\) with the same coordinate \(v\), so it is analytic as well.

Finally use the reductive identification \(V=\mathfrak m\). The derivative of the chart \(\phi(v)=\exp(v)H\) satisfies, by (G.5),
\[
d\phi_v(w)=j_{\exp(v)}\,C(v)w,\qquad
C(v)=\operatorname{pr}_{\mathfrak m}B(v)|_{\mathfrak m}.
\]
Since \(C(0)=I\), it is analytically invertible near zero. In these coordinates the invariant endomorphism has matrix
\[
C(v)^{-1}IC(v).
\tag{G.7}
\]
This is analytic, and translated charts give the same conclusion at every point. All constructed atlases have their original smooth coordinate maps, so they are compatible with the given smooth structures. □

**Theorem G.4 (The complete homogeneous complex-coordinate criterion).** For the invariant almost complex structure determined by \(I\) on a reductive space, the condition
\[
[IX,IY]_{\mathfrak m}-[X,Y]_{\mathfrak m}
-I[IX,Y]_{\mathfrak m}-I[X,IY]_{\mathfrak m}=0
\quad(X,Y\in\mathfrak m)
\tag{G.8}
\]
is necessary and sufficient for complex coordinates inducing that structure. The resulting complex atlas is compatible with the homogeneous real-analytic atlas, and every element of \(G\) acts holomorphically. Neither \(G\) nor \(H\) needs to be connected.

**Proof.** Necessity is F.1. Conversely (G.8) makes \(N_J\) zero at \(o\), and invariance makes it zero everywhere. G.3 proves that \(J\) is real analytic in the homogeneous atlas. Work in one such real coordinate neighbourhood, identified with an open set in \(\mathbb R^{2k}\). By G.1 extend its matrix \(J(x)\) to a holomorphic matrix \(J(z)\) on a neighbourhood in \(\mathbb C^{2k}\). The identity \(J^2=-I\) persists after complexification by the uniqueness assertion of G.1.

The matrices \(P_\pm(z)=\tfrac12(I\mp iJ(z))\) are complementary holomorphic projections onto the \(+i\) and \(-i\) eigenspaces. At the real centre each eigenspace has complex dimension \(k\): conjugation exchanges them, and their direct sum is \(\mathbb C^{2k}\). Choose bases of the two images there and project those fixed vectors by \(P_\pm(z)\). The resulting \(2k\) vectors remain a basis near the centre because their determinant remains nonzero. Thus
\[
D_z=\ker(J(z)+iI)
\]
is a holomorphic rank-\(k\) distribution.

The tensor \(N_J\) in coordinates is formed from the coefficients of \(J\) and their first derivatives. This follows either by expanding (F.1) on coordinate fields or from its tensoriality proof there. Its holomorphic extension vanishes since it vanishes on the real slice. If \(A,B\) are holomorphic sections of \(D\), their eigenvalue identities \(JA=-iA,JB=-iB\) give
\[
0=N_J(A,B)=-2[A,B]+2iJ[A,B].
\]
Hence \(J[A,B]=-i[A,B]\), proving involutivity. G.2 supplies a holomorphic submersion \(f\) to \(\mathbb C^k\) with \(\ker df=D\).

Since \((J+iI)(J-iI)=0\), the image of \(J-iI\) lies in \(D\), and consequently
\[
df\circ J=i\,df.
\tag{G.9}
\]
At the real centre the restriction of \(df\) to \(\mathbb R^{2k}\) is injective: a real vector in its kernel would satisfy \(Jv=-iv\), with a real left side and purely imaginary right side, forcing \(v=0\). Both real dimensions are \(2k\), so it is an isomorphism. The real-analytic inverse theorem of [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) makes the restriction of \(f\) a real-analytic local diffeomorphism onto an open subset of \(\mathbb C^k\). Equation (G.9) says precisely that these coordinates turn \(J\) into multiplication by \(i\).

Carry out this construction at every point. A transition between two resulting charts is real analytic, because the underlying homogeneous transitions and the maps \(f\) and their real-analytic inverses are. Its real derivative commutes with multiplication by \(i\), by (G.9). The final assertion of G.1 then makes it holomorphic. We have obtained a complex atlas with the required compatibility. Each left action by an element of \(G\) is real analytic by G.3 and preserves \(J\) by invariance, so in the new charts its derivative is complex linear. G.1 again proves holomorphicity. All isotropy conditions used were imposed on the whole of \(H\); no connectedness argument entered. If \(k=0\), the coordinate domains are points and the conclusion is immediate. □

## H. Recovering homogeneity from complete parallel data

The free preprint of J. L. Carmona Jiménez and M. Castrillón López treats the relation between parallel data and reductive homogeneity. The next two lemmas provide the global integration and connected-fibre arguments needed for the reconstruction here.

**Lemma H.1 (A complete constant-bracket frame gives a Lie group).** Let \(N\) be a connected simply connected smooth manifold with a global frame \(X_1,\ldots,X_d\). Suppose every \(X_i\) is complete and
\[
[X_i,X_j]=\sum_\ell c_{ij}^{\ell}X_\ell
\]
with constant real coefficients. For each chosen \(o\in N\), there is a unique Lie-group structure with identity \(o\) for which this frame is left invariant.

**Proof.** The case \(d=0\) is a point. For \(d>0\), on \(N\times N\) consider the rank-\(d\) distribution
\[
\mathcal D_{(x,y)}
=\operatorname{span}\{(X_i(x),X_i(y)):1\leq i\leq d\}.
\]
The coefficients in both factors are the same constants, so the bracket of two displayed fields is their same constant linear combination. The bracket product rule then makes the distribution involutive. [De Rham B.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-2) and [De Rham B.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-3) give its connected maximal integral leaves with their Hausdorff second-countable manifold structures. Each projection from such a leaf \(L\) to \(N\) is a local diffeomorphism: its derivative takes the displayed basis to the frame basis.

We prove that each projection is a covering, retaining the global completeness hypothesis explicitly. Write \(\Phi_i^t\) for the complete flow of \(X_i\), and
\[
\Psi_x(t)=\Phi_d^{t_d}\cdots\Phi_1^{t_1}(x).
\]
For fixed \(x\), its derivative at \(t=0\) is the frame at \(x\); [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a small open box \(B\) on which \(\Psi_x\) is a diffeomorphism onto a neighbourhood \(U\) of \(x\). The finite word \(\Phi_d^{t_d}\cdots\Phi_1^{t_1}\) is a global diffeomorphism for every real \(t\), because every constituent flow is complete.

The orbit of any point under all finite words in these flows is open by the same inverse-function argument. These orbits partition connected \(N\) into open sets, so there is only one orbit. The simultaneous flows \((\Phi_i^t,\Phi_i^t)\) preserve every leaf of \(\mathcal D\): their trajectories are tangent to it, and the plaque construction in [De Rham B.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-3) makes their restrictions smooth. Hence each projection \(L\to N\) is onto.

For every \((x,y)\in L\) over \(x\), the map
\[
U\longrightarrow L,\qquad
\Psi_x(t)\longmapsto(\Psi_x(t),\Psi_y(t))
\tag{H.1}
\]
is a smooth section of the first projection. Its image is open in \(L\): its derivative has rank \(d\), since composition with the projection has invertible derivative, and the inverse function theorem applies on the leaf. Two such images are disjoint unless their initial \(y\)'s agree, because the same global flow word is injective. They exhaust the inverse image of \(U\): given \((x',y')\in L\) with \(x'=\Psi_x(t)\), apply the inverse simultaneous word to reach a unique point \((x,y)\in L\). This proves that \(U\) is evenly covered. The same reasoning with the factors reversed proves the assertion for the second projection.

[Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) now makes both projections diffeomorphisms, since \(N\) is simply connected and \(L\) is connected. Thus the leaf through \((o,y)\) is the graph of a global diffeomorphism \(F_y:N\to N\) with \(F_y(o)=y\) and
\[
(F_y)_*X_i=X_i.
\tag{H.2}
\]
It is the only such diffeomorphism: the graph of any other is a connected integral manifold through \((o,y)\), hence lies in that maximal leaf, and the first projection already determines its single value over each point.

Set \(y\cdot z=F_y(z)\). The identity map is \(F_o\). Composition and inversion preserve (H.2), so uniqueness gives
\[
F_yF_z=F_{F_y(z)},\qquad F_y^{-1}=F_{F_y^{-1}(o)}.
\]
These identities prove associativity, the identity law, and inverses.

We verify smoothness jointly in both variables. The uniqueness of flows in [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and (H.2) imply that \(F_y\) commutes with every \(\Phi_i^t\). Fix \(z_0\), and choose a finite flow word \(P\) with \(P(o)=z_0\), which is possible by the orbit argument above. A coordinate parametrization near \(z_0\) is \(z=\Psi_{z_0}(t)\) for small \(t\). Commutation gives
\[
F_y(\Psi_{z_0}(t))
=\Phi_d^{t_d}\cdots\Phi_1^{t_1}P(y).
\tag{H.3}
\]
The right side is smooth jointly in \(y,t\), by smooth dependence of complete flows on each bounded time neighbourhood. This proves smooth multiplication near every pair. For inversion solve \(y\cdot z=o\): the derivative in \(z\) is that of the diffeomorphism \(F_y\), hence invertible. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a smooth solution \(z\) near each pair \((y,y^{-1})\), and uniqueness of the group inverse identifies these solutions. The resulting group is a Lie group on the original manifold.

Its left translations are precisely \(F_y\), so the frame is left invariant. In any other Lie-group structure with this identity and left-invariant frame, left translation by \(y\) would satisfy (H.2) and send \(o\) to \(y\); uniqueness of \(F_y\) forces the same multiplication. Notice that only completeness of the frame fields was used; completeness of all their linear combinations was not assumed. □

**Lemma H.2 (Connected fibres after a connected covering).** Let \(Q\to M\) be a smooth locally trivial bundle with manifold fibre. Suppose \(M\) is connected and simply connected, and \(r:E\to Q\) is a connected smooth covering onto \(Q\). Then the composite \(p:E\to M\) is locally trivial with manifold fibres, and every fibre of \(p\) is connected.

**Proof.** Choose a bundle trivialization \(Q|_U\cong U\times F\), with \(U\) a coordinate ball convex in its coordinates and centred at \(x_0\). Put \(F'=r^{-1}(\{x_0\}\times F)\), a possibly disconnected manifold. For \(a\in F'\), with \(r(a)=(x_0,f)\), lift the path
\[
t\longmapsto(x_0+t(x-x_0),f),\qquad 0\leq t\leq1,
\]
starting at \(a\), and let \(\Theta(x,a)\) be its endpoint. The covering path-lifting proof in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) gives existence and uniqueness on the whole interval. The lift varies smoothly locally with \(x,a\): subdivide one lifted path into finitely many covering charts and use their smooth inverse branches in order; the same subdivision works in a neighbourhood of its parameters by continuity and compactness. This is also the smooth-parameter verification in that lifting proof.

The map \(\Theta:U\times F'\to r^{-1}(Q|_U)\) is a diffeomorphism. Its inverse takes a point over \((x,f)\) to \(x\) and the endpoint obtained by lifting the reverse radial path to \(x_0\). Reversal and uniqueness make these maps inverse, and the same local inverse-branch argument proves smoothness of the inverse. This proves the asserted local triviality of \(p\).

Form the set \(C\) of connected components of all fibres of \(p\), with the quotient topology from \(E\). In a local trivialization \(U\times F'\), every component of \(F'\) is open: a manifold is locally path connected, so its connected components are unions of open path components and are themselves path connected. Thus \(C\) has local charts
\[
U\times\pi_0(F')\longrightarrow U,
\tag{H.4}
\]
with the second factor discrete. These charts give exactly the quotient topology. In fact an open subset of \(U\times F'\) meets each component in an open set, whose projection to \(U\) is open; its image in \(U\times\pi_0(F')\) is consequently open. The transition maps preserve the base point and permute component labels locally constantly, because a continuous family of fibre diffeomorphisms cannot move a connected component's chosen point between disjoint open components on a connected small parameter neighbourhood.

Hence \(C\to M\) is a covering. It is Hausdorff: distinct base points separate downstairs, and distinct points over one base point separate in the disjoint sheets of (H.4). The quotient map \(E\to C\) is open by the preceding projection argument, so the images of a countable basis of \(E\) give a countable basis of \(C\). The covering charts therefore also give its usual smooth manifold structure. It is connected as the continuous image of connected \(E\). [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) makes this covering one-sheeted, since \(M\) is simply connected. Thus every fibre of \(p\) has exactly one connected component. □

**Theorem H.3 (The complete parallel-data criterion).** Let \(M\) be a connected simply connected smooth manifold with an affine connection \(\nabla\). The following are equivalent:

1. A connected Lie group acts transitively on \(M\), preserving \(\nabla\), and has a reductive presentation \(M=G/K\).
2. There is a geodesically complete affine connection \(\bar\nabla\) such that
\[
\bar\nabla\bar T=0,\qquad \bar\nabla\bar R=0,\qquad
\bar\nabla S=0,\qquad S=\nabla-\bar\nabla.
\tag{H.5}
\]

In the reconstruction from the second condition, \(G\) may be chosen simply connected, \(K\) is closed and connected, and \(\bar\nabla\) is the canonical connection for the resulting reductive complement. The action preserves every \(\bar\nabla\)-parallel tensor.

**Proof.** Assume the first condition. Choose its reductive complement and the canonical connection \(\bar\nabla\) from B.2. That theorem proves geodesic completeness and parallel torsion and curvature. The difference \(S\) is a tensor by [Linear connections A.3](linear-and-affine-connections.md#theorem-a-3); both connections are invariant, so \(S\) is invariant. B.2 then gives \(\bar\nabla S=0\). This proves (H.5).

For the converse fix a frame \(u_0:\mathbb R^n\to T_oM\) and take the intrinsic reachable holonomy reduction \(Q\) of \(\bar\nabla\), with full holonomy structure group \(H_0\) and Lie algebra \(\mathfrak h_0\). [Curvature and holonomy G.4](curvature-and-holonomy-groups.md#theorem-g-4) proves that it is a Hausdorff second-countable principal bundle with the restricted connection, even when its inclusion in the full frame bundle is only immersed. It is connected: every point is reached from \(u_0\) by a horizontal path, continuous in that intrinsic structure.

[Geodesics D.3](geodesics-normal-coordinates-and-curvature.md#theorem-d-3) supplies a coframe \((\theta,\omega)\) on \(Q\) and the global fields
\[
Z_{A,a}=A^\#+B(a),\qquad A\in\mathfrak h_0,\ a\in\mathbb R^n,
\]
whose constant bracket is
\[
[Z_{A,a},Z_{C,b}]
=Z_{[A,C]-r(a,b),\,Ab-Ca-t(a,b)}.
\tag{H.6}
\]
Here \(t,r\) are the constant frame components of \(\bar T,\bar R\). We need a complete frame. Choose bases of \(\mathfrak h_0\) and \(\mathbb R^n\); their fields \(A^\#\) and \(B(a)\) form one. The vertical fields are complete, with flows \(u\mapsto u\exp(tA)\) in the intrinsic principal bundle. The horizontal fields are complete as well. By [Geodesics G.1](geodesics-normal-coordinates-and-curvature.md#theorem-g-1) their projected curves are the geodesics with initial velocity \(ua\), which exist for all real times by hypothesis. On every compact time interval, [Connections C.1](connections-and-parallel-transport.md#theorem-c-1) lifts that geodesic inside the principal bundle \(Q\); the coframe calculation in [Geodesics G.1](geodesics-normal-coordinates-and-curvature.md#theorem-g-1) identifies the lift with the integral curve of \(B(a)\). Uniqueness makes these compact-interval lifts agree. Thus completeness holds on \(Q\) itself.

[Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) constructs its connected simply connected covering
\(r:\widetilde Q\to Q\) as a smooth Hausdorff second-countable manifold. Each frame field lifts uniquely through this local diffeomorphism. Its lift is complete: lift its whole flow trajectory from any chosen point on each finite time interval by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1), and join the compatible intervals by uniqueness. The local inverse branches make the lifted curve smooth and give its differential equation. Naturality of brackets from [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3) shows that the lifted frame has the same constants (H.6).

Apply H.1 to \(\widetilde Q\), with a chosen lift of \(u_0\) as identity. It becomes a connected simply connected Lie group \(G\). Its Lie algebra is
\(\mathfrak h_0\oplus\mathbb R^n\) with bracket (H.6), and the lifted \(\theta,\omega\) are left-invariant forms: they take constant values on the left-invariant frame. Let
\[
p:G\xrightarrow{r}Q\longrightarrow M.
\]
It is a surjective submersion. H.2 proves that all its fibres are connected. They are also closed, since \(M\) is Hausdorff. Its vertical distribution is the left-invariant distribution corresponding to
\(\mathfrak k=\{(A,0):A\in\mathfrak h_0\}\), because \(\theta\) vanishes exactly on vertical vectors.

Let \(K=p^{-1}(o)\). We show that this fibre is a subgroup. Equation (H.6) makes \(\mathfrak k\) a Lie subalgebra. [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1) supplies its connected analytic subgroup, generated by \(\exp(\mathfrak k)\). Its left cosets are exactly the maximal integral leaves of the vertical distribution: finite words in these flows stay in a leaf, their orbit is open in that leaf by the inverse function theorem applied to a basis of \(\mathfrak k\), and the orbits partition a connected leaf into open sets. On the other hand the fibres of \(p\) are exactly these leaves. A vertical path has constant \(p\)-value by differentiation; and any two points of a connected fibre can be joined by finitely many coordinate paths inside that fibre, tangent to its kernel distribution. It follows that \(K\) is the subgroup just constructed and every fibre is a left coset \(gK\).

Since \(K\) is closed, Invariant connections A.1 makes it an embedded Lie subgroup; its tangent space at the identity is \(\ker dp_e=\mathfrak k\). [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) gives the smooth quotient \(G/K\). The induced map
\[
G/K\longrightarrow M,\qquad gK\longmapsto p(g)
\tag{H.7}
\]
is bijective by the fibre calculation and is a local diffeomorphism: its derivative is the isomorphism obtained from the surjection \(dp_g\) by dividing out its vertical kernel. Local quotient sections verify smoothness, and its local inverses give a global smooth inverse. Thus left translation on \(G/K\) gives the required transitive action on \(M\).

Set \(\mathfrak m=\{(0,a):a\in\mathbb R^n\}\). Equation (H.6) gives
\[
[(A,0),(0,a)]=(0,Aa).
\tag{H.8}
\]
Therefore \(\operatorname{ad}(\mathfrak k)\mathfrak m\subseteq\mathfrak m\). The adjoint ODE of [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3) shows that \(\operatorname{Ad}(\exp A)\) preserves \(\mathfrak m\) for each \(A\in\mathfrak k\): solve that linear ODE in \(\mathfrak m\) and use uniqueness. The connected group \(K\) is generated by these exponentials, as in [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1), so all of \(\operatorname{Ad}(K)\) preserves \(\mathfrak m\). This is a reductive complement for the full stabilizer.

It remains to prove preservation of the connection and tensors, rather than only homogeneity of the manifold. Write \(u_g=r(g)\) for the frame in \(Q\), and \(\ell_a\) for the action of \(a\in G\) on \(M\). For any \(V\in T_gG\), the pulled-back solder identity is
\[
dp_g(V)=u_g\,\theta_g(V).
\]
Left invariance of \(\theta\) and \(p\circ L_a=\ell_a\circ p\) give
\[
d\ell_a\,u_g=u_{ag}.
\tag{H.9}
\]
Indeed every vector in \(\mathbb R^n\) occurs as \(\theta_g(V)\). Thus the natural action on frames, restricted to \(Q\), is exactly the one induced from \(L_a\) through \(r\).

The pulled-back connection form \(\omega\) is left invariant too. Since \(r\) is a covering local diffeomorphism, (H.9) implies that this natural frame action preserves the connection on \(Q\), and hence on the full frame bundle by right equivariance and local frames. [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) then proves preservation of \(\bar\nabla\). Its horizontal spaces on \(G\) are precisely \(dL_g\mathfrak m=\ker\omega_g\). These are the canonical horizontal spaces for the reductive presentation in Invariant connections C.2, so \(\bar\nabla\) is the canonical connection claimed.

If a tensor \(P\) is \(\bar\nabla\)-parallel, its coefficients in a parallel frame are constant by [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) and [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2). Every frame in \(Q\) is horizontally reachable from \(u_0\), so those coefficients have the same value throughout \(Q\). Equation (H.9) therefore makes \(P\) invariant under every \(\ell_a\). In particular \(S\) is invariant by (H.5), and preservation of \(\bar\nabla\) and \(S\) gives preservation of \(\nabla=\bar\nabla+S\). This finishes every assertion. □

## Freely accessible sources

- Alberto Elduque, *Reductive homogeneous spaces and nonassociative algebras*, Communications in Mathematics **28** (2020), 199–229. [Free journal article](https://dml.cz/bitstream/handle/10338.dmlcz/148703/ActaOstrav_28-2020-2_8.pdf), §§4–5 and the Lie-group examples at the start of §6. The moving-frame classification, bilinear products and metric computations are developed in A–D above.
- Masahiro Morimoto, *The parallel transport map over reductive homogeneous space*, [arXiv:2512.01522v1](https://arxiv.org/pdf/2512.01522v1), 1 December 2025, §2. This version describes local reductive frames and invariant affine connections, including the product-group presentation used in C.3.

- Daniel Beltiţă, *Integrability of almost complex structures on Banach manifolds*, [arXiv:math/0407395v1](https://arxiv.org/pdf/math/0407395v1), 23 July 2004, Theorems 6, 7, 13 and 15 and Proposition 11. Part G develops the finite-dimensional analytic construction, with complete power-series, Frobenius and homogeneous-chart proofs before the complex-coordinate criterion.
- J. L. Carmona Jiménez and M. Castrillón López, *The Ambrose–Singer Theorem for general homogeneous manifolds with applications to symplectic geometry*, [arXiv:2001.06254v2](https://arxiv.org/pdf/2001.06254v2), 19 August 2021, Theorem 2.2 and its proof. Part H proves the complete parallel-data criterion, including the global frame integration and fibre-connectedness arguments used in the reconstruction.

The complete programme proofs supporting the global product argument are in [De Rham E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3) and [De Rham K.5](holonomy-and-the-de-rham-decomposition-theorem.md#corollary-k-5). The octonion multiplication, stabilizer and sphere-action proofs are in [De Rham Z.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-1), [De Rham Z.2](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-z-2), [De Rham Z.6](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-6) and [De Rham Z.7](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-z-7); F.2 combines those results to construct the prescribed Cayley triples, and F.3 computes the obstruction explicitly in their fixed multiplication convention.

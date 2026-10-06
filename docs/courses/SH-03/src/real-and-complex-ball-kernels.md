# Real and complex ball kernels

A boundary kernel carries three kinds of data: the side on which its sheaf lives, the direction selected in the cotangent bundle, and the degree produced by integration with compact supports. We separate these data in two explicit calculations. For a real sphere, changing the side can reverse the motion or change the global transform without changing the motion. For a complex quadratic boundary, a square-root branch selects the motion, while an oriented family of real balls determines the shift.

We first compare the three real supports and compute their operators. An open–closed triangle then relates the closed exterior to the normalized ball kernels in the literature, with its exact degree shift and localization domain. The complex calculation follows from its own support equations and cotangent selection. Four solved exercises test the radius, side, branch and degree separately.

Use When a kernel quantizes a contact transformation and the signed boundary tests. These examples use arbitrary commutative unital finite-global-dimension coefficients. Fix \(n\geq1\). The contact criterion requires a cohomologically constructible kernel, its microsupport condition over either selected region, and the actual identity-induced microlocal endomorphism map. We check these separately; properness of the cotangent graph does not assert properness of the ordinary kernel support.

The closed-submanifold microlocal Hom calculation, together with its identity section, supplies the local identity test. Formal cohomological constructibility follows from the proved submanifold models and convex half-space models: their local ordinary and compact-support systems stabilize with perfect representatives. The smooth coordinate and closed-embedding descriptions below reduce these supports to those models.

The displayed geometric microsupport equalities assume \(k\ne0\). For the zero ring all sheaves and microsupports are zero, the same geometric graphs still satisfy the containment conditions of the contact criterion, and the operator identities and equivalences concern zero categories.

*Original text by GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, September–October 2026. New original text is public domain (CC0).*

## Choosing a side of the sphere

For radius \(R>0\), write \(h_R(x,y)=|x-y|^2-R^2\). At the sphere, the boundary tests give the following signs relative to \(dh_R\). The second physical kernel covector is negated when it is read as an input covector.

| Support of the constant kernel | Boundary sign | Motion |
| --- | --- | --- |
| Closed interior | Negative | Inward |
| Open interior | Positive | Outward |
| Closed exterior | Positive | Outward |

The displacement has length \(R\). A cohomological shift changes the degree of an operator but leaves its microsupport unchanged. Thus the two outward rows need a further comparison: their common cotangent graph does not identify their ordinary sheaf operators. We compute the closed exterior first, then give the comparison map itself.

## A real kernel with an outward covector

Take \(X=Y=\mathbb R^n\), with its standard Euclidean metric, and put

\[
S=\{(x,y):|x-y|^2\geq1\},\qquad K=k_S.
\qquad\text{(1)}
\]

This is the constant sheaf on the **closed exterior** of the unit ball in the difference variable, extended by zero. Set \(h(x,y)=|x-y|^2-1\). At its boundary, \(dh=2(x-y)\cdot(dx-dy)\) never vanishes. The closed-positive-half-space test in a coordinate chart therefore gives the nonzero part of the kernel microsupport:

\[
\Lambda=\{(x,y;\xi,\nu):
|x-y|=1,\ \xi=-\nu=\lambda(x-y),\ \lambda>0\}.
\qquad\text{(2)}
\]

To justify this use of the one-dimensional test in \(2n\) dimensions, complete \(h\) to smooth coordinates near the boundary. The sheaf is the inverse image of \(k_{0,\infty)}\) under the coordinate submersion. The exact [submersion pullback formula pulls its microsupport back from the positive ray with zero tangential components. In the interior of \(S\), it is locally constant; outside \(S\), it is zero. Thus the only other microsupport points are zero covectors over \(S\).

On the punctured cotangent regions, the twisted relation (2) is the graph of

\[
\chi(y;\eta)=\left(y+\frac{\eta}{|\eta|};\eta\right),
\qquad \eta\ne0.
\qquad\text{(3)}
\]

Its inverse subtracts the same unit vector, so both projections are diffeomorphisms and proper homeomorphisms. The kernel support itself is not proper over \(X\). The selected cotangent graph is what supplies admissibility.

The map (3) preserves the tautological form. Indeed
\(\theta_X=\eta\cdot dx\), and
\(\eta\cdot d(\eta/|\eta|)=0\), since \(\eta/|\eta|\) has constant norm. Consequently \(\chi^*\theta_X=\eta\cdot dy=\theta_Y\). It also commutes with positive covector scaling, so it is a contact transformation on the punctured bundles.

The identity condition is checked locally, including its map. In the boundary coordinate \(t=h\), the triangle

\[
k_{\{t>0\}}\longrightarrow k_{\{t\geq0\}}
\longrightarrow k_{\{t=0\}}\xrightarrow{+1}
\qquad\text{(4)}
\]

has first term invisible in the positive conormal direction. Thus \(K\) is microlocally the constant sheaf of the boundary there. Its self microlocal Hom on that conormal has value \(k\), and its identity section is one, by the submanifold formula. Local identities agree on chart overlaps, so the identity-induced morphism is exactly an isomorphism \(k_\Lambda\to\mu\operatorname{hom}(K,K)|_\Lambda\). The contact criterion therefore makes \(\Phi_K\) an equivalence on punctured cotangent regions.

## Three real integration tests

Let \(A=\{x:|x|\geq1\}\). The following are ordinary sheaf-operator identities, hence also hold after localization:

\[
\Phi_K(k_{\{0\}})=k_A,\qquad
\Phi_K(k_Y)=0,\qquad
\Phi_K(k_{Y\setminus\{0\}})=k_A[-1].
\qquad\text{(5)}
\]

For the first, the input is supported at \(y=0\); projection of the restricted support identifies it with \(A\), without a shift. For the second, the proper-support fibre formula for \(!\) gives the stalk at \(x\) as compact-support cohomology of the closed exterior \(\{y:|x-y|\geq1\}\). It is zero. To check this with its map, use the open-ball triangle in \(\mathbb R^n\). Compact-support cohomology of both the open ball and \(\mathbb R^n\) is \(k[-n]\); extension by zero gives their orientation isomorphism, so the remaining closed exterior has zero compact-support cohomology. The comparison is induced by the common point-support class in the two coordinate balls, as proved there; equality of the abstract cohomology groups alone would not identify this map. Every output stalk is zero.

Finally the input triangle
\(k_{Y\setminus\{0\}}\to k_Y\to k_{\{0\}}\xrightarrow{+1}\)
is sent to a triangle whose middle term is zero and whose third term is \(k_A\). Its first term is therefore \(k_A[-1]\). The shift places the copy of \(k\) in degree one. This third test is an input on the punctured base space, rather than a hypersurface input.

## Comparing the exterior with the normalized ball kernel

Let \(P=\mathbb R^n\times\mathbb R^n\), \(U_R=\{|x-y|<R\}\) and \(E_R=P\setminus U_R\), with \(R>0\). Set \(B_R=k_{U_R}\) and \(C_R=k_{E_R}\). The open–closed sequence is exact on every stalk, and gives the triangle

\[
B_R\longrightarrow k_P\longrightarrow C_R
\xrightarrow{\partial}B_R[1].
\tag{BK1}
\]

The middle kernel is locally constant, so its microsupport lies in the zero section. In the kernel category localized at any selected punctured cotangent region it is zero. The cone of the connecting morphism \(\partial\) is a shift of that middle term; hence \(\partial\) itself becomes an isomorphism. With the outward normalized kernel \(Q_R=B_R[n]\), we obtain

\[
C_R\xrightarrow[\partial]{\sim}B_R[1]=Q_R[1-n]
\quad\text{on the selected punctured cotangent regions.}
\tag{BK2}
\]

The kernel \(Q_R\) occurs at time \(-R\) in Guillermou–Kashiwara–Schapira, [Example 3.10](https://arxiv.org/abs/1005.1517v4), p. 25. Their positive time moves against the covector direction. Guillermou's [Example 2.1.4](https://arxiv.org/abs/1905.07341v3), pp. 31–32, reverses this time convention, so its time \(+R\) is the same outward kernel. Both examples use the open ball shifted by the dimension for this outward motion; the closed interior gives the inverse motion. The boundary signs in the preceding table also prove these directions directly, without invoking a general isotopy theorem.

The localization in (BK2) matters. Proper-support integration of \(Q_R\) against a constant input gives a constant output: each oriented open ball has compact-support complex \(k[-n]\), and the normalization \([n]\) cancels this degree. Translations identify the fibres and their orientation generators, so this is an isomorphism of constant sheaves, not just a stalk count. In contrast, the closed exterior sends the constant input to zero by the actual orientation isomorphism in the preceding integration test. Applying the transform to (BK1) is another way to see the latter vanishing. Constant objects are already zero in the punctured localization, so these two global answers agree with the localized comparison.

These real examples fix the normalized-ball antecedent and the time convention. The comparison with the exterior is the explicit connecting-map proof (BK1)–(BK2). The complex quadratic support below requires its own calculation.

## A complex square-root branch

Now take \(X=Y=\mathbb C^n\). Write \(z=x+iy\), \(w=u+iv\), and use the complex bilinear quadratic expression
\(a^2=\sum_j a_j^2\), which is not a Hermitian norm. The underlying real cotangent forms are

\[
\theta_X=2\operatorname{Re}\sum_j\zeta_j\,dz_j,
\qquad \theta_Y=2\operatorname{Re}\sum_j\eta_j\,dw_j.
\qquad\text{(6)}
\]

Take the open regions \(\Omega_X=\{(z;\zeta):\zeta^2\notin\mathbb R_{\geq0}\}\) and the corresponding \(\Omega_Y\). For \(\eta\) in this domain let

\[
s(\eta)=\sqrt{-\eta^2},\qquad \operatorname{Re}s(\eta)>0.
\qquad\text{(7)}
\]

This is the holomorphic square-root branch on the plane slit along the nonpositive real axis for \(-\eta^2\). The zero value is excluded. Define

\[
\chi(w;\eta)=\left(w+\frac{\eta}{s(\eta)};\eta\right).
\qquad\text{(8)}
\]

It is invertible by subtracting the displayed vector, and homogeneous for positive real scaling. Since \(s^2=-\eta^2\), differentiation gives
\(ds=-(\eta\cdot d\eta)/s\) and
\(\eta\cdot d(\eta/s)=0\).
Thus (8) preserves the holomorphic tautological form and, by taking twice the real part, both forms in (6).

Put \(h(z,w)=(z-w)^2\), and let

\[
Z=\{h=-1\},\qquad
Z_+=\{\operatorname{Im}h=0,\ \operatorname{Re}h<-1\},
\qquad K=k_{Z_+}.
\qquad\text{(9)}
\]

The kernel is on a locally closed real subset, extended by zero. The open strict inequality in (9) is essential. Near its closed support, \(dh\ne0\), so \(a=\operatorname{Re}(h+1)\), \(b=\operatorname{Im}(h+1)\) are two independent real coordinates. The local kernel is \(k_{\{a<0,b=0\}}\) times the constant sheaf in the remaining coordinates.

The open-negative-half-line has a positive boundary covector; the closed \(b=0\) condition permits either normal sign. First pull back the half-line calculation along the coordinate submersion inside \(b=0\), then use the closed-embedding microsupport equality. This proves the required product case without assuming equality for arbitrary external tensor products. To translate through (6), a real normal \(\alpha\,da+\beta\,db\) corresponds to \(\kappa=\alpha-i\beta\); in particular \(\operatorname{Re}\kappa=\alpha\). We obtain

\[
\operatorname{SS}(K)=
\left\{(z,w;\zeta,\nu):
\begin{array}{l}
\operatorname{Im}h=0,\ \operatorname{Re}h\leq-1,\\
\zeta=-\nu=\kappa(z-w),\quad\operatorname{Re}\kappa\geq0,\\
(1+\operatorname{Re}h)\operatorname{Re}\kappa=0
\end{array}\right\}.
\qquad\text{(10)}
\]

The equality includes zero covectors over the closed support. Locally the coordinates \(a,b\) reduce the assertion to the product of the one-dimensional half-line and point formulas; their submersion transport gives all and only the displayed covectors. The coefficient ring may be the zero ring, in which case the microsupport is empty and (10) is read as a containment; the subsequent categorical statements are then vacuous. For nonzero coefficients the equality holds.

On either selected region, (10) forces \(\operatorname{Re}\kappa>0\): if \(\operatorname{Re}\kappa=0\), then \(\kappa^2h\) is nonnegative real, contrary to the definition of \(\Omega\). It then forces \(h=-1\) and gives \(s(\zeta)=\kappa\). The selected relation is exactly the graph of (8), with actual second kernel covector \(-\eta\). Its two projections are proper homeomorphisms.

The identity condition follows from a local triangle on the smooth real hypersurface \(b=0\):

\[
k_{\{a<0,b=0\}}\longrightarrow k_{\{a\leq0,b=0\}}
\longrightarrow k_{\{a=0,b=0\}}\xrightarrow{+1}.
\qquad\text{(11)}
\]

The middle term has nonpositive \(a\)-normal component, so it is invisible at the selected positive component \(\operatorname{Re}\kappa>0\). Consequently \(K\simeq k_Z[-1]\) there. Self microlocal Hom of this shifted submanifold sheaf has value \(k\) on its conormal, with identity section one. The local identity maps glue, establishing the exact condition required by the contact criterion. Thus this kernel quantizes (8).

## A real subspace becomes an open exterior

Let \(N=\{w\in\mathbb C^n:\operatorname{Im}w=0\}\). Then

\[
\Phi_K(k_N)=k_{\{z=x+iy:\ |y|^2>1\}}[1-n].
\qquad\text{(12)}
\]

Here \(|y|^2=\sum_j y_j^2\) is a real Euclidean norm. To prove the formula, apply the proper-support fibre formula at \(z=x+iy\). Its compact-support fiber is

\[
\{w\in\mathbb R^n:
\langle x-w,y\rangle=0,\quad |x-w|^2<|y|^2-1\}.
\qquad\text{(13)}
\]

Let \(U=\{z=x+iy:|y|>1\}\), let \(j:U\hookrightarrow\mathbb C^n\), and put \(m=n-1\). Write \(F=\Phi_K(k_N)\). The proper-support fibre formula identifies \(F_z\) with the compactly supported cohomology of (13). In particular all stalks outside \(U\), including its boundary, are zero. For \(z\in U\), put \(r(z)=\sqrt{|y|^2-1}>0\).

Over \(U\), the spaces \(E_z=y^\perp\) form a rank-\(m\) real vector bundle \(E\): the fibrewise orthogonal projection is the smooth matrix

\[
P_y=I-\frac{yy^{\mathsf T}}{|y|^2}.
\]

Its image has constant rank \(m\). The map

\[
(z,v)\longmapsto (z,w=x-r(z)v),\qquad
v\in E_z,\quad |v|<1,
\]

identifies its unit open-ball bundle with the support of the integration kernel over \(U\). Thus \(j^{-1}F\) is the proper-support image of the constant sheaf of this ball bundle.

Orient \(E\) by the standard orientation of \(\mathbb R^n\) and the positive unit normal \(y/|y|\), with one fixed order for tangent and normal factors. On a small base chart choose an oriented orthonormal frame of \(E\). The ball bundle becomes the product with an open \(m\)-ball, and the proper-support product computation gives \(k[-m]\) on that chart. On an overlap the two orthonormal frames differ by an orientation-preserving linear transformation. Its action on top compactly supported cohomology is the determinant sign, hence \(+1\), by the proved orientation-coordinate comparison. These local generators consequently glue to the constant sheaf \(k_U\) in degree \(m\); every other cohomology sheaf is zero. The truncation isomorphism for a complex with just this one cohomology sheaf therefore gives

\[
j^{-1}F\simeq k_U[-m]=k_U[1-n].
\]

This uses the orientation line, and does not assert that \(E\) itself has a global frame. In rank zero the fibres are points; their degree-zero generator gives the same conclusion directly, on each component of \(U\).

Let \(i:\mathbb C^n\setminus U\hookrightarrow\mathbb C^n\). Since inverse image is exact and every stalk of \(i^{-1}F\) vanishes, \(i^{-1}F=0\). The open–closed localization triangle

\[
j_!j^{-1}F\longrightarrow F\longrightarrow i_*i^{-1}F
\xrightarrow{+1}
\]

then identifies the **adjunction map** \(j_!j^{-1}F\to F\) as an isomorphism. It follows that

\[
F\simeq j_!k_U[1-n]=k_{\{|\operatorname{Im}z|^2>1\}}[1-n].
\]

The strict inequality, the zero boundary stalks and the degree-zero answer when \(n=1\) are all retained. The argument determines the local-system gluing and the boundary attachment; it does not infer a sheaf merely from its stalk groups.

## Exercises with complete solutions

### Moving by a radius

*Difficulty: Introductory.*

Replace (1) by \(S_R=\{|x-y|\geq R\}\), where \(R>0\). Find the contact map and its inverse. Compute the images of a skyscraper at \(y_0\) and of the constant input.

**Solution.** The boundary conormal is the positive multiple of \((x-y,-(x-y))\), with \(|x-y|=R\). The twisted relation is
\((y;\eta)\mapsto(y+R\eta/|\eta|;\eta)\), and its inverse subtracts \(R\eta/|\eta|\). The skyscraper becomes \(k_{\{|x-y_0|\geq R\}}\) without shift. The constant input still becomes zero: compact-support cohomology of each closed exterior vanishes by the open-ball orientation triangle, with radius \(R\). The latter vanishing is consistent with the equivalence on punctured regions because the constant input is already zero in that localization.

### The other side of a real sphere

*Difficulty: Intermediate.*

Use \(k_{\{|x-y|\leq1\}}\) instead of (1). Find its nonzero cotangent graph and the image of the constant input. Explain the difference from (3) and (5).

**Solution.** This is a closed negative sublevel of \(h=|x-y|^2-1\), so the normal multiplier is negative. For the twisted input \(\eta\), the relation sends
\((y;\eta)\) to \((y-\eta/|\eta|;\eta)\). It is the inverse geometric motion. Each integration fiber is a compact closed ball with cohomology \(k\) in degree zero, so the constant input becomes the constant output \(k_X\). On the punctured cotangent localization both constant objects vanish. Choosing the opposite side changes the directional motion and the global integration calculation; it is not a harmless replacement of the support inequality.

### Tracking the complex branch

*Difficulty: Intermediate.*

For \(n=1\), take \(\eta=it\), \(t\in\mathbb R\setminus\{0\}\), in (8). Compute \(s(\eta)\), the displacement, and its behavior for positive and negative \(t\). Explain why the physical input covector of the kernel remains \(-\eta\).

**Solution.** Here \(-\eta^2=t^2>0\), so the selected square root is \(|t|\). The displacement is \(i\operatorname{sgn}(t)\). Its square is \(-1\), as required for the boundary \(Z\). Positive scaling preserves the sign and the displacement. The physical conormal of \(h\) has components \((\kappa(z-w),-\kappa(z-w))\); with \(\kappa=|t|\), these are \((it,-it)\). The twisted convention negates the second to produce input \(\eta=it\). Reversing the branch reverses the displacement, while omitting the twisted minus sign changes the relation itself.

### Checking the complex shift

*Difficulty: Advanced.*

Evaluate (12) for \(n=1\) and \(n=2\), and describe what happens at \(|y|=1\). Why would ordinary fiber cohomology give a wrong answer for \(n=2\)?

**Solution.** For \(n=1\), the nonempty fiber in (13) is a point and the output is the degree-zero sheaf on \(|y|>1\), extended by zero. For \(n=2\), the nonempty fiber is an open interval, whose compact-support cohomology is \(k[-1]\); the output is the same open-support sheaf shifted by \([-1]\), with nonzero cohomology in degree one. At \(|y|=1\), the strict radius inequality has no solution, so the stalk is zero in both cases. Ordinary cohomology of an open interval is \(k\) in degree zero, and would erase the shift. The operator uses \(!\), so proper base change prescribes compact supports even though the input subspace \(N\) is noncompact.

## References

The classical contact-kernel theory is due to M. Kashiwara and P. Schapira; see [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.3. The local equivalence and identity conditions used here are proved in the programme criterion linked at the beginning.

S. Guillermou, M. Kashiwara and P. Schapira, [*Sheaf quantization of Hamiltonian isotopies and applications to nondisplaceability*](https://arxiv.org/abs/1005.1517v4), version 4 (2011), Example 3.10, p. 25, supplies the normalized real ball family. S. Guillermou, [*Sheaves and symplectic geometry of cotangent bundles*](https://arxiv.org/abs/1905.07341v3), version 3 (2022), Example 2.1.4, pp. 31–32, gives the reversed time convention and explains how compact-support convolution and attachment maps determine the family. Its final uniqueness assertion for a nonzero triangle is stated over a field; no such uniqueness assertion is used here.

The closed-exterior comparison, the complex bilinear square-root selection and the real-subspace transform are the calculations given in this lesson, relative to the exact boundary, operation, microlocal Hom and orientation proofs linked at their uses. The two cited real examples are credited for their stated real kernels, rather than for the complex model.

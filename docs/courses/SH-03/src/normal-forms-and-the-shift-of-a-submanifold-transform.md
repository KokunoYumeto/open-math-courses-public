# Normal forms and the shift of a submanifold transform

A submanifold transform can turn a hypersurface into a submanifold of higher codimension. Its cohomological shift records which fibre directions are integrated with compact support. We first obtain a local coordinate model from a clean conormal intersection, then compute every part of that shift. Positive, negative and null quadratic directions play different roles.

The sheaf-operation inputs are the formal kernel-composition comparison, the direct-germ formula (MC.25), and proper-support base change. The fibre proof below uses the actual localization and trace maps specified at each step. We prove the clean cotangent reduction and bind the exact programme Morse lemma with parameters before applying them to the hypersurface. The smooth inverse, implicit, submersion and constant-rank theorems, differentiation of smooth parameter integrals, and finite-dimensional symmetric-form diagonalization are calculus prerequisites. We work over a commutative ring \(k\) of finite global dimension, and \(L\in D^b(k)\) may have arbitrary coefficient modules.

*Written by GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, September–October 2026. Independently written exposition is public domain (CC0); cited human works retain their own terms.*

## Clean intersection supplies the coordinate model

Let \(f:Y\to X\) be a submersion, \(N\subset Y\) a closed smooth hypersurface, and \(M\subset X\) a closed smooth submanifold. Embed

\[
V=Y\times_X T^*X\subset T^*Y
\]

by the cotangent pullback \(f_d(y;\xi)=(y;df_y^t\xi)\), and put \(A=T_N^*Y\). Fix a nonzero \(p\in A\cap V\). Assume the intersection is clean near \(p\): it is a submanifold with tangent space \(T_pA\cap T_pV\). Assume also that the image under \(f_\pi:V\to T^*X\) is \(T_M^*X\) as a germ at \(f_\pi(p)\).

The image hypothesis is part of the theorem; it does not follow from smoothness of \(f\) alone. Cleanliness will imply that the restricted map to this image is a submersion. Here is the rank calculation, including the possible excess directions.

## Clean cotangent reduction has constant rank

Put \(m=\dim X\) and \(d=\dim(Y/X)\), so \(\dim Y=m+d\). In submersion coordinates \(f(x,t)=x\), write a covector on \(Y\) as \((\xi,\tau)\). Then

\[
V=\{\tau=0\},\qquad
f_\pi(x,t;\xi,0)=(x;\xi),\qquad
\omega_Y|_V=f_\pi^*\omega_X.
\]

At a point \(z\in C=A\cap V\), let \(E=T_zT^*Y\), \(W=T_zV\), and \(\ell=T_zA\). The plane \(W\) is coisotropic: in these coordinates its symplectic orthogonal is the \(d\)-plane

\[
K=W^\omega=\ker d(f_\pi|_V)
              =\operatorname{span}\{\partial_{t_j}\}.
\]

The plane \(\ell\) is Lagrangian. The map
\(\ell\to K^*\), \(v\mapsto\omega_Y(v,\cdot)|_K\),
has kernel \(\ell\cap K^\omega=\ell\cap W\).
Its transpose has kernel \(K\cap\ell^\omega=K\cap\ell\).
Writing \(e_z=\dim(K\cap\ell)\), equal ranks of a linear map and its transpose give

\[
\dim(\ell\cap W)=m+d-(d-e_z)=m+e_z.
\]

Cleanliness says \(T_zC=\ell\cap W\). Its dimension is constant near the selected point, so \(e_z=\dim C-m\) is constant as well. The kernel of \(d(f_\pi|_C)\) is \(\ell\cap K\), and hence

\[
\operatorname{rank}d(f_\pi|_C)=\dim C-e_z=m.
\]

The image tangent is isotropic: lift two of its vectors to \(T_zC\subset\ell\), use the displayed pullback identity, and use \(\omega_Y|_\ell=0\). Its dimension \(m\) makes it Lagrangian in \(T_{f_\pi(z)}T^*X\). Under the stated image-germ hypothesis the map has values in \(T_M^*X\), another \(m\)-dimensional manifold, and its derivative is onto that tangent space. The submersion theorem therefore gives a local submersion onto an open part of this conormal germ. This proves the required clean-reduction statement with excess fibre dimension \(\dim C-m\). It makes no assertion about a global image or a transverse intersection. \(\square\)

This is the cotangent instance of Lagrangian reduction. The programme's Phase space and generating families, Proposition 2.3 also proves the corresponding linear statement for every Lagrangian and isotropic constraint. The argument above supplies the local rank and submersion conclusions used in this lesson.

## A nondegenerate critical family has fixed quadratic coordinates

**Morse lemma with parameters.** Let \(h(a,t)\) be smooth near \((a_0,0)\), with \(a\) in a finite-dimensional parameter space and \(t\in\mathbb R^b\). Assume, for every nearby \(a\),

\[
h(a,0)=0,\qquad d_t h(a,0)=0,
\]

and assume the Hessian \(d_t^2h(a_0,0)\) is nondegenerate. There is a parameter-preserving local coordinate change \((a,t)\mapsto(a,v)\), taking \(t=0\) to \(v=0\), for which

\[
h(a,t)=\sum_{j=1}^{b_+}v_j^2
             -\sum_{j=b_++1}^{b}v_j^2.
\]

The positive and negative dimensions are those of the original Hessian. If the critical point is instead a smooth section \(t=c(a)\), translate by that section; if its critical value is \(h(a,c(a))\), subtract that value before applying the lemma.

**Proof from the exact programme prerequisite.** Lemma 4.1 of the written AN-04 lesson Stationary phase and critical manifolds proves a stronger parameter Morse statement: a smoothly varying nondegenerate critical point has coordinates satisfying \(h(F(z,a),a)=c(a)+z^TJz/2\), with fixed signs, a smooth inverse and the exact determinant normalization. Its proof constructs the critical section by the implicit function theorem, completes one square using the integrated second derivative, and proves the remaining Hessian is the invertible Schur complement before inducting. All parameter dependence and signs are retained.

Apply that result with the fibre variables \(t\) and parameters \(a\). The critical-point uniqueness in its proof makes its critical section exactly our given \(t=0\); the assumed value makes \(c(a)=0\). Set \(v=z/\sqrt2\) in its final coordinates to obtain the displayed normalization without the factor \(1/2\). The same provider covers a moving critical section and a varying critical value, giving the final variant. For \(b=0\), the hypotheses themselves give \(h=0\). Thus every part of the stated lemma is supplied by an exact, written internal proof. The smooth-calculus prerequisites stated by that lesson remain prerequisites here. \(\square\)

## Coordinates adapted to the clean conormal image

**Normal-form theorem.** There are coordinates

\[
x=(x_1,x',x''),\qquad (x,t,u)\text{ on }Y,
\quad x',u\in\mathbb R^r,
\qquad\text{(1)}
\]

in which the selected base points are zero and

\[
\begin{split}
f(x,t,u)&=x, &p&=(0;dx_1),\\
M&=\{x_1=x'=0\},
&N&=\{x_1=q(t)+\langle x',u\rangle\}.
\end{split}
\qquad\text{(2)}
\]

Here \(q\) is a quadratic form, possibly degenerate, and \(\operatorname{codim}_XM=r+1\). If the conormal intersection with \(V\) is transverse, \(q\) is nondegenerate.

**Proof.** Near the nonzero conormal \(p\), projection from \(A\cap V\) to \(Y\) has a one-dimensional kernel: the radial conormal direction. Cleanliness makes its rank constant. Its image is therefore a submanifold \(D\subset N\), and projectivizing the positive conormal ray identifies \(A\cap V\) locally with \(D\) times that ray. The clean-reduction prerequisite makes \(D\) a submersion over the corresponding projectivized piece of \(T_M^*X\).

Choose coordinates on \(X\) with \(M=\{x_1=x'=0\}\) and the selected covector \(dx_1\). On the projectivized conormal chart use
\(u=-\xi'/\xi_1\), together with \(x''\), as coordinates. Complete their pullbacks to coordinates \((x'',u,t'')\) on \(D\). The minus sign is fixed by the conormal of a graph \(x_1=g\): its covector has \(\xi'=-\xi_1\partial_{x'}g\).

Because \(f\) is a submersion, the independent coordinates \(x_1,x'\) vanish on \(D\) and can be completed by coordinates \(t'\) vanishing there. Thus
\((x_1,x',x'',t',t'',u)\) are coordinates on \(Y\), with
\(D=\{x_1=x'=t'=0\}\).
The selected conormal has nonzero \(dx_1\) component, so the hypersurface can be written

\[
x_1=g(x',x'',t',t'',u)
=\langle x',u\rangle+h(x',x'',t',t'',u).
\qquad\text{(3)}
\]

On \(\{x'=t'=0\}\) we have

\[
h=0,\qquad \partial_{x'}h=0,
\qquad \partial_{t'}h=0.
\qquad\text{(4)}
\]

The first comes from \(D\subset N\), the second from the definition of \(u\), and the third from the requirement that the conormal over \(D\) be a pulled-back covector. Derivatives along \(x'',t'',u\) of these identities vanish there as well.

We claim the Hessian \(H=\partial_{t't'}^2h(0)\) is nondegenerate. Write fibre coordinates \((\xi,\tau',\tau'',v)\) dual to \((x,t',t'',u)\). The conormal of (3), with multiplier \(\xi_1\), has
\(\tau'=-\xi_1\partial_{t'}h\),
\(\tau''=-\xi_1\partial_{t''}h\), and
\(v=-\xi_1(x'+\partial_uh)\).
The tangent equations at the selected point, using (4), imply that membership in \(T_pA\cap T_pV\) forces

\[
\delta x_1=\delta x'=0,\qquad
\delta\tau'=\delta\tau''=\delta v=0,
\qquad H\,\delta t'=0.
\qquad\text{(5)}
\]

Conversely a vector in \(\ker H\) can be completed in the free \(\delta\xi'\) components to a tangent vector with these properties. Cleanliness says this intersection is the tangent of \(A\cap V\). Its projection lies in \(T_0D\), where \(\delta t'=0\). Thus \(\ker H=0\).

Apply the Morse lemma with parameters \((x'',t'',u)\) to \(h(0,x'',t',t'',u)\). Its critical value is zero by (4), its critical point is \(t'=0\), and its Hessian is nondegenerate. A parameter-dependent change of \(t'\), extended independently of \(x'\), makes that restriction a fixed nondegenerate quadratic form \(q(t')\). Hadamard's lemma then gives

\[
h=q(t')+\langle x',\phi(x',x'',t',t'',u)\rangle,
\qquad \phi=0\text{ on }\{x'=t'=0\}.
\qquad\text{(6)}
\]

Replace the old coordinate \(u\) by \(u_{\mathrm{new}}=u+\phi\). Its derivative in \(u\) on the displayed submanifold is the identity, so this is a coordinate change near the origin. It preserves \(f\) and turns (3) into (2), with \(t=(t',t'')\) and \(q\) zero on \(t''\).

The dimension of \(A\cap V\) is \(\dim X+\dim t''\): projectivized conormal coordinates contribute \(\dim X-1\), the ray contributes one, and \(t''\) is the remaining fibre. A transverse intersection has the expected dimension \(\dim X\). Hence in the transverse case there are no \(t''\) directions, and \(q\) is nondegenerate. \(\square\)

## The closed side and the three quadratic dimensions

Choose the closed upper side

\[
N^+=\{x_1\geq q(t)+\langle x',u\rangle\}.
\qquad\text{(7)}
\]

Diagonalize the form and write

\[
t=(s_+,s_-,w),\qquad
q(t)=|s_+|^2-|s_-|^2.
\qquad\text{(8)}
\]

Let their dimensions be \(n_+,n_-,n_0\), respectively. The last is the dimension of the radical \(\ker q\). It is not the dimension of a maximal isotropic subspace of an indefinite nondegenerate form. Set \(d=\dim(Y/X)\) and \(c=\operatorname{codim}M=r+1\). Counting the fibre variables gives

\[
d=n_++n_-+n_0+r,
\qquad n_++n_-+n_0=d-c+1.
\qquad\text{(9)}
\]

Fix the coordinate orientations for the \(s_-,w,u\) spaces. The compact-support generator, (M5)–(M6) starts with the increasing-interval boundary difference and takes ordered products. It gives \(R\Gamma_c(\mathbb R^a;L)=L[-a]\), with its actual normalization for arbitrary bounded \(L\).

Here is the extension to the open convex fibres used below. Translate an interior point of a nonempty open convex \(O\subset\mathbb R^a\) to zero and choose a ball of radius \(\rho>0\) inside \(O\). Its gauge

\[
p(v)=\inf\{t>0:v\in tO\}
\]

is finite, nonnegative and positively homogeneous. Convexity gives subadditivity, and the interior ball gives \(p(v)\leq\lVert v\rVert/\rho\). Applying these bounds to \(v-w\) and \(w-v\) proves \(|p(v)-p(w)|\leq\lVert v-w\rVert/\rho\). Thus \(p\) is continuous, and openness and convexity give \(O=\{p<1\}\). The maps

\[
h(v)=\frac{v}{1+p(v)},\qquad
h^{-1}(u)=\frac{u}{1-p(u)}
\]

are inverse homeomorphisms \(\mathbb R^a\leftrightarrow O\), by homogeneity. This includes unbounded directions where \(p=0\). Near zero, \(h(v)=v+O(\lVert v\rVert^2)\), so it preserves the positive local orientation class. Transporting the compact generator by \(h\) gives \(R\Gamma_c(O;L)=L[-a]\) with that orientation.

The composition and open-extension identity for trace, (M27) says that extending a compact class from one such open convex set to another preserves its integral. Both oriented integrals are isomorphisms, so their extension map is the identity under the same \(L[-a]\) identification. The dual-generator normalization, (O9)–(O10) fixes its sign, and projection with arbitrary bounded coefficients carries the generator and the trace to \(L\). Closed balls instead have ordinary cohomology \(L\) by constant-coefficient convex acyclicity and are compact. The zero-dimensional ball is a point. No flatness or finite-generation condition on \(L\), or global orientability of \(Y\), is assumed.

## Four fibre integrations determine the shift

For small \(\epsilon>0\), choose \(\eta>0\) so that
\(\eta(1+\epsilon)<\epsilon\). Consider the open neighborhood

\[
U_{\eta,\epsilon}=
\{|x|<\eta,\ |w|<\epsilon,\ |u|<\epsilon,
\ |s_+|^2<\epsilon,\ |s_-|^2<\epsilon\}.
\qquad\text{(10)}
\]

Shrinking these parameters gives a neighborhood system at zero. Factor \(f\) into projections which forget \(s_-\), then \(s_+\), then \(w\), then \(u\). At each step the derived proper-image fibre formula and composition of proper images calculate the fibre. We also identify the extension across its parameter boundaries, so that a stalk calculation alone is not asked to determine a sheaf.

For the first projection put
\(a=|s_+|^2+\langle x',u\rangle-x_1\).
Its fibre is

\[
\{s_-:a\leq|s_-|^2<\epsilon\}.
\qquad\text{(11)}
\]

For \(a\leq0\) this is an open ball, with compact cohomology \(L[-n_-]\). For \(a\geq\epsilon\) it is empty. When \(0<a<\epsilon\), it is a shell with the inner boundary included and the outer boundary omitted. Its compact cohomology vanishes. To verify the last claim, use the compact-support triangle for the inner open ball inside the outer open ball. The map between their compact cohomologies is the orientation trace isomorphism, so the shell is its zero cone. If \(n_-=0\), (11) is simply a point for \(a\leq0\) and empty otherwise, which gives the same result.

The parameterwise comparison to the open ball is obtained by the localization triangle in these two squared-radius regions. Thus the surviving sheaf is the constant coefficient on the **closed** condition
\(x_1\geq|s_+|^2+\langle x',u\rangle\), shifted by \([-n_-]\). The transition at \(a=0\) comes from the same ball trace; it is not a separate choice of a nonzero stalk.

For the second projection let \(b=x_1-\langle x',u\rangle\). The positive-variable fibre is
\(\{s_+:|s_+|^2\leq b,\ |s_+|^2<\epsilon\}\).
It is empty for \(b<0\), a point for \(b=0\), and a closed ball for \(0<b<\epsilon\). The bound on \(\eta\) ensures \(|b|<\epsilon\) on the retained base neighborhood. Projection on this closed-ball support is proper locally over each compact part of that base neighborhood. Its unit from the constant coefficient is an isomorphism on every fibre, hence is an isomorphism of sheaves. We obtain the closed condition \(x_1\geq\langle x',u\rangle\), with **no new shift**.

The third projection integrates the independent open \(w\)-ball. The product trace adds \([-n_0]\) and changes nothing else.

For the fourth projection consider the compact-support triangle over the open \(u\)-ball

\[
L_{\{|u|<\epsilon,\ \langle x',u\rangle>x_1\}}
\longrightarrow L_{\{|u|<\epsilon\}}
\longrightarrow
L_{\{|u|<\epsilon,\ \langle x',u\rangle\leq x_1\}}
\xrightarrow{+1}.
\qquad\text{(12)}
\]

The first fibre is empty when \(x_1\geq\epsilon|x'|\). Otherwise it is a nonempty open convex set; its compact-cohomology map to the whole open ball is the orientation trace isomorphism. Thus the third term has compact cohomology zero outside that closed parameter condition, and \(L[-r]\) on it. The first term's convex-set trace identifies its direct image with the open-extension coefficient on \(\{x_1<\epsilon|x'|\}\), shifted by \([-r]\). Triangle (12) identifies the third image with the closed-extension coefficient on its complement. Therefore, as a sheaf calculation on \(|x|<\eta\), all four integrations give

\[
Rf_!L_{N^+\cap U_{\eta,\epsilon}}
\simeq
L_{\{x_1\geq\epsilon|x'|,\ |x|<\eta\}}[\delta],
\qquad
\delta=-n_--n_0-r=n_+-d.
\qquad\text{(13)}
\]

The support and the degree can be checked independently at each stage. In this table, the base restriction \(|x|<\eta\) and the cutoffs on variables not yet integrated are understood.

| Variable forgotten | Fibre and comparison which select the support | Surviving closed condition | Additional shift |
|---|---|---|---|
| \(s_-\) | The open ball survives when \(a\leq0\); for \(0<a<\epsilon\), inner-ball extension is an isomorphism and kills the half-open shell. | \(x_1\geq \lVert s_+\rVert^2+\langle x',u\rangle\) | \([-n_-]\) |
| \(s_+\) | The proper closed ball, including its radius-zero point, is identified by the constant-section unit. | \(x_1\geq\langle x',u\rangle\) | \([0]\) |
| \(w\) | The independent open ball is integrated by its oriented trace. | \(x_1\geq\langle x',u\rangle\) | \([-n_0]\) |
| \(u\) | The open convex cap has the same trace as the whole ball when nonempty; localization leaves its empty-cap locus. | \(x_1\geq\epsilon\lVert x'\rVert\) | \([-r]\) |

Thus the positive variables alter support but add no degree, while the negative, null and \(u\) variables contribute exactly the three negative terms in (13). The table includes dimension-zero factors: their ball is a point, their shift is zero, and the same inequalities decide whether it remains. It also applies to \(L=0\), including the zero ring, since every comparison is a natural map of coefficient complexes.

Nested neighborhoods use restriction and compact traces from these same triangles, so the comparisons are compatible. Notice that the output in (13) is a closed cone inside an open base neighborhood. It is not the coefficient on \(M\) as an ordinary sheaf.

## The comparison becomes an isomorphism at the selected covector

The closed cone \(C_\epsilon=\{x_1\geq\epsilon|x'|\}\) contains \(M\). Restriction supplies
\(L_{C_\epsilon}\to L_M\). The vertex restriction for a convex cone is a microlocal isomorphism on the interior of its nonnegative polar. In the \((x_1,x')\) variables this polar is

\[
C_\epsilon^\circ=
\{(\xi_1,\xi'): \xi_1\geq0,
\ |\xi'|\leq\epsilon\xi_1\}.
\qquad\text{(14)}
\]

The selected covector \(dx_1\) is in its interior. Here is the actual restriction map and its proof. In the normal variables \(E=\mathbb R^{r+1}\), put \(\gamma=-C_\epsilon\) and \(P_\gamma=\phi_\gamma^{-1}R\phi_{\gamma*}\). The correspondence projector (G10) and its vertex calculation give

\[
P_\gamma L_{\{0\}}\simeq L_{-\gamma}=L_{C_\epsilon}.
\]

Indeed, on the vertex-supported input its kernel condition is \(0-x\in\gamma\); projection identifies that support homeomorphically with \(-\gamma\). This calculation is exact for coefficient modules and hence for their bounded complexes. The adjunction counit is restriction to the vertex, with the identity map on its coefficient. The counit-cone estimate (T26) makes the cone of this specific map invisible on \(\operatorname{Int}\gamma^{\circ a}=\operatorname{Int}C_\epsilon^\circ\). Its parameter version retains the unchanged \(x''\) factor and gives exactly \(L_{C_\epsilon}\to L_M\); that factor carries zero tangential covector. Consequently this restriction is invertible at \(f_\pi(p)=(0;dx_1)\), including \(r=0\). This proves the positive sign and the actual cutoff comparison, rather than inferring a map from equality of microsupport sets.

Combining it with (13) gives a morphism of pro-objects

\[
\text{“}\!\lim_{U\ni0}\!\text{”}\ Rf_!L_{N^+\cap U}
\longrightarrow L_M[\delta],
\qquad
\delta=1-c-(n_0+n_-)=n_+-d.
\qquad\text{(15)}
\]

For an arbitrary neighborhood one first chooses a smaller neighborhood of the form (10) inside it; common smaller choices give the same pro-morphism. Its restriction to the point-localized category is an isomorphism. By the direct-germ formula (MC.25), this neighborhood system computes the formal microlocal proper-support image. Thus the calculation itself represents that image by \(L_M[\delta]\), including the clean case with null directions. No isolated-incidence hypothesis is inserted here: the representation follows from the compatible explicit comparisons (13)–(15). Neither an ordinary global inverse limit nor a global isomorphism with \(L_M[\delta]\) is asserted.

The boundary kernel \(L_N\) gives the same formal image, by a direct comparison that retains all null directions. Write \(F=x_1-q(t)-\langle x',u\rangle\), \(O=\{F>0\}\), and let \(B_\epsilon\) be the product of the four open fibre balls in (10). Work over the interior target ball \(|x|<\eta\). There,

\[
L_{O\cap U_{\eta,\epsilon}}
=L_O\otimes^L k_{B_\epsilon}.
\]

By the open-extension boundary estimate, the nonzero boundary covectors of \(L_O\) have the form \(a\,dF\) with \(a<0\), hence negative \(dx_1\) coefficient. All covectors of the independent fibre cutoff \(k_{B_\epsilon}\) have zero \(dx_1\) coefficient. The tensor is noncharacteristic: a cancellation \(a\,dF+b=0\) forces \(a=0\) from that component and then \(b=0\). The tensor estimate (MO21) consequently puts every microsupport covector of \(L_{O\cap U_{\eta,\epsilon}}\) in the half-space with nonpositive \(dx_1\) coefficient, including all fibre faces and corners.

Choose the closures of the fibre balls inside the coordinate chart. The closed support is then proper over the retained base ball. The proper direct-image estimate (MO8) gives the same nonpositive coefficient bound for \(Rf_!L_{O\cap U_{\eta,\epsilon}}\), so it is invisible at \((0;dx_1)\). Applying \(Rf_!\) to the ordinary localization triangle

\[
L_{O\cap U_{\eta,\epsilon}}
\longrightarrow L_{N^+\cap U_{\eta,\epsilon}}
\longrightarrow L_{N\cap U_{\eta,\epsilon}}
\xrightarrow{+1}
\]

makes this actual boundary restriction an isomorphism at the selected positive covector. These arrows commute with compact-support extension between nested neighborhoods, so they give the formal comparison with the same shift as (15). This verifies the comparison directly for every clean excess dimension.

## Expressing the shift by three Lagrangian planes

Use the cotangent symplectic form \(\omega=d\theta\), so in linear coordinates
\(\omega((x;\xi),(y;\eta))=\langle\xi,y\rangle-\langle\eta,x\rangle\).
For three Lagrangian planes define their inertia index as the signature of

\[
Q(v_0,v_N,v_1)=
\omega(v_0,v_N)+\omega(v_N,v_1)+\omega(v_1,v_0).
\qquad\text{(16)}
\]

### The ordered index: degeneracy, parity and the cocycle

Here is a proof of the structural identities needed in the next lessons. Let \(E\) be a real symplectic vector space of dimension \(2n\), with the convention above, and let \(\lambda_1,\lambda_2,\lambda_3\) be Lagrangian planes. There is a Lagrangian complement transverse to any prescribed finite collection of Lagrangian planes: AN-04, Gaussian lines and invariant symbols, Proposition 1.2 proves this using the positive-codimension intersection strata in symmetric graph charts. Choose this common complement as the vertical plane and a complementary Lagrangian as horizontal. Then every \(\lambda_i\) is \(p=A_iq\), where \(A_i\) is symmetric. Formula (16) becomes

\[
Q=q_1^T(A_1-A_2)q_2+q_2^T(A_2-A_3)q_3
  +q_3^T(A_3-A_1)q_1.
\]

Make the invertible change

\[
q_1=x+z,\quad q_2=x+y,\quad q_3=y+z;
\qquad x=\tfrac12(q_1+q_2-q_3),\quad
y=\tfrac12(-q_1+q_2+q_3),\quad
z=\tfrac12(q_1-q_2+q_3).
\]

Expanding and using \((A_1-A_2)+(A_2-A_3)+(A_3-A_1)=0\) cancels all mixed terms. Consequently

\[
Q=x^T(A_1-A_2)x+y^T(A_2-A_3)y+z^T(A_3-A_1)z,
\qquad
\tau(\lambda_1,\lambda_2,\lambda_3)
=\operatorname{sgn}(A_1-A_2)+\operatorname{sgn}(A_2-A_3)
 +\operatorname{sgn}(A_3-A_1).
\]

No difference matrix was inverted, so this proof includes degenerate intersections. A cyclic permutation preserves \(Q\); an odd permutation negates it. Reversing \(\omega\) negates \(\tau\), and symplectic direct sums add the signatures. For four planes choose one common chart. Cancelling the six ordered matrix differences in the displayed signature formula gives the full four-plane identity

\[
\tau(\lambda_1,\lambda_2,\lambda_3)
+\tau(\lambda_1,\lambda_3,\lambda_4)
=\tau(\lambda_1,\lambda_2,\lambda_4)
+\tau(\lambda_2,\lambda_3,\lambda_4).
\]

For completeness, the radical has an intrinsic description. Polarizing (16) says that a triple lies in the radical precisely when
\(v_2-v_3\in\lambda_1\), \(v_3-v_1\in\lambda_2\), and \(v_1-v_2\in\lambda_3\). The assignments

\[
a_{12}=\tfrac12(v_1+v_2-v_3),\quad
a_{23}=\tfrac12(-v_1+v_2+v_3),\quad
a_{31}=\tfrac12(v_1-v_2+v_3)
\]

put \(a_{ij}\) in \(\lambda_i\cap\lambda_j\). Their inverse is
\(v_1=a_{12}+a_{31}\), \(v_2=a_{12}+a_{23}\), \(v_3=a_{23}+a_{31}\). Thus the radical is isomorphic to the direct sum of the three pairwise intersections. The rank is \(3n-\sum_{i<j}\dim(\lambda_i\cap\lambda_j)\). Since the signature and rank of a real symmetric form have the same parity,

\[
\tau(\lambda_1,\lambda_2,\lambda_3)
\equiv n+\sum_{i<j}\dim(\lambda_i\cap\lambda_j)\pmod2.
\]

In a continuous family with all three intersection dimensions fixed, choose local continuous frames for the three planes. The matrix of \(Q\) varies continuously and has constant rank by the radical calculation. At a given parameter, its nonzero eigenvalues have a positive distance from zero; on a smaller neighborhood their signs persist. Constant rank prevents any remaining eigenvalue from becoming nonzero. The positive and negative counts, hence \(\tau\), are locally constant. This works on an arbitrary topological parameter space and requires no path-connectivity assumption.

### Reduction by an isotropic plane contained in two arguments

We also need the following precise reduction rule. If an isotropic \(I\) is contained in \(\lambda_1\cap\lambda_2\), set \(E_0=I^\omega/I\) and
\(\overline\lambda_i=((\lambda_i\cap I^\omega)+I)/I\). Then

\[
\tau_E(\lambda_1,\lambda_2,\lambda_3)
=\tau_{E_0}(\overline\lambda_1,\overline\lambda_2,\overline\lambda_3).
\]

All three reduced planes are Lagrangian by the linear reduction proved in AN-04, Phase space and generating families, Proposition 2.3. To prove the signature assertion, split \(E=I\oplus I^*\oplus E_0\), with \(I\oplus I^*\) symplectic and \(E_0\) its symplectic orthogonal. Put \(d=\dim I\) and \(J=I\cap\lambda_3\), \(j=\dim J\). We have \(\lambda_1=I\oplus L_1\), \(\lambda_2=I\oplus L_2\), with \(L_i\subset E_0\). Pairing with \(I\) on \(\lambda_3\) has rank \(d-j\): its transpose has kernel \(I\cap\lambda_3^\omega=J\). Choose a complement \(W\) to \(\lambda_3\cap I^\omega\) in \(\lambda_3\). Then \(\omega\) pairs \(I/J\) perfectly with \(W\).

Write \(v_1=i_1+l_1\), \(v_2=i_2+l_2\), and \(v_3=w_0+w\), where \(w\in W\), \(w_0\in\lambda_3\cap I^\omega\). A section of the projection of \(w_0\) to \(\overline\lambda_3\) separates its \(J\)-coordinate. The form is exactly

\[
Q=Q_0(l_1,l_2,\overline w_0)
+\omega(i_2-i_1,w)+\omega(l_2-l_1,w_{E_0}),
\]

where \(Q_0\) is the three-plane form on \(E_0\). The last term is a linear functional of \(w\) whose coefficients depend linearly on \((l_1,l_2)\). Perfect pairing lets us absorb it by translating the \(I/J\)-coordinate of \(i_2-i_1\). This triangular change of variables is invertible. What remains is \(Q_0\), a hyperbolic pairing of dimension \(2(d-j)\), and a radical of dimension \(d+2j\) from \(i_1\), the unused \(J\)-coordinate of \(i_2-i_1\), and the \(J\)-coordinate of \(w_0\). The hyperbolic pairing has equally many positive and negative directions. This proves the rule, including \(j>0\); alternation gives the same rule when \(I\) is contained in either other pair. This proves reduction for a constraint contained in one pair of arguments. The following argument proves the stronger rule for the sum of the pairwise intersections.

**Reduction by a subspace of the sum of the pairwise intersections.** Set \(J_{ij}=\lambda_i\cap\lambda_j\) and \(J=J_{12}+J_{23}+J_{31}\). The sum \(J\) is isotropic: each summand is isotropic, and any two summands lie in one common Lagrangian. We claim that every \(I\subset J\) can be reduced without changing \(\tau\).

First record reduction in stages. If \(I\subset J\) are isotropic and \(E_I=I^\omega/I\), then

\[
(J/I)^{\omega_{E_I}}=J^\omega/I,
\qquad (E_I)_{J/I}=J^\omega/J=E_J.
\]

The reduced planes agree as well. Since \(I\subset J^\omega\subset I^\omega\),

\[
\bigl((\lambda\cap I^\omega)+I\bigr)\cap J^\omega
=(\lambda\cap J^\omega)+I.
\]

To check this equality, write a vector on the left as \(l+i\). Both \(l+i\) and \(i\) belong to \(J^\omega\), hence \(l\) does too. The reverse inclusion is immediate. Adding \(J\) and quotienting by \(J\) gives the plane \(((\lambda\cap J^\omega)+J)/J\). Thus these are canonical identifications of the quotient spaces and their three reduced planes.

Now reduce successively by \(J_{12}\), the image of \(J_{23}\), and the image of \(J_{31}\). Each constraint is still in the indicated pairwise intersection: all the original \(J_{ij}\) lie in the isotropic \(J\), so they are orthogonal to the constraints already removed. The common-pair proof applies at every stage, and reduction in stages identifies the final triple with its reduction in \(E_J\). Its index equals the original one.

For an arbitrary \(I\subset J\), the images \((J_{ij}+I)/I\) in \(E_I\) belong to the corresponding pairwise intersections and span \(J/I\). Apply the same three common-pair reductions to this triple. Its final quotient and planes are again those in \(E_J\). Comparing the two routes proves

\[
\tau_E(\lambda_1,\lambda_2,\lambda_3)
=\tau_{E_I}\bigl((\lambda_1)_I,(\lambda_2)_I,(\lambda_3)_I\bigr),
\qquad I\subset
(\lambda_1\cap\lambda_2)+(\lambda_2\cap\lambda_3)+(\lambda_3\cap\lambda_1).
\]

No complement to the pairwise intersections and no transversality among the three planes has been assumed. The restriction \(I\subset J\) is essential to this argument. \(\square\)

### The submanifold transform's ordered triple

The order matters. In \(E=T_pT^*Y\) take
\(\lambda_0=T_p\pi_Y^{-1}(0)\),
\(\lambda_N=T_pT_N^*Y\), and
\(\lambda_1=T_p f_\pi^{-1}(\pi_X^{-1}(0))\), with the last inverse image taken inside \(V\). Set \(\tau=\tau_E(\lambda_0,\lambda_N,\lambda_1)\).

Write \(q(t)=\tfrac12\langle At,t\rangle\), with \(A\) symmetric, in the normal form. Its tangent conormal equations are
\(x_1=\xi''=0\), \(\xi'=-u\), \(\tau_t=-At\), \(v=-x'\).
The vertical plane has \(x=t=u=0\), while \(\lambda_1\) has \(x=\tau_t=v=0\). We calculate the signature directly in these coordinates. The fibre-variable contribution is the triple in \((t;\tau_t)\)

\[
\{t=0\},\qquad \{\tau_t=-At\},
\qquad \{\tau_t=0\}.
\qquad\text{(17)}
\]

For the \(x_1\) coordinate all three planes are vertical, so its form is zero. In the \(x''\) block the planes are vertical, horizontal, vertical; its form is \((a-c)^Tb\). This is a hyperbolic pairing plus a radical and has signature zero.

In the coupled \((x',u;\xi',v)\) block, take a vertical vector with momenta \((a,b)\), a conormal vector with bases \((c,d)\) and momenta \((-d,-c)\), and a third-plane vector with bases \((0,e)\) and momenta \((f,0)\). Formula (16) becomes

\[
a^Tc+b^Td-c^Te-f^Tc-b^Te
=c^T(a-f-e)+b^T(d-e).
\]

The change of variables \((a,d)\mapsto(a-f-e,d-e)\), retaining \((b,c,e,f)\), is invertible. The resulting two hyperbolic pairings have zero signature, and the remaining variables are radical. Finally, on (17), with a vertical vector \(a\), a graph vector \((b,-Ab)\), and a horizontal vector \(c\), the form is

\[
a^T(b-c)-b^TAc
=(a+Ab)^Tz-b^TAb,\qquad z=b-c.
\]

The change \((a,b,c)\mapsto(a+Ab,b,z)\) is invertible even when \(A\) is singular. Its hyperbolic pairing has signature zero, leaving the signature of \(-A\). The blocks are independent, so
\(\tau=-\operatorname{sgn}A=-(n_+-n_-)\).
This proves the complete ordered calculation, including null directions. The graph sign in (17) fixes the minus sign.

Furthermore \(\dim((T_pV)^\perp\cap\lambda_N)=n_0\), since that intersection imposes \(u=0\) and \(At=0\) on the remaining fibre-base vector. Substitute these identities and (9) into (15). We obtain

\[
\delta=\frac12\bigl[
1+\dim M-\dim Y
-\dim((T_pV)^\perp\cap\lambda_N)-\tau
\bigr].
\qquad\text{(18)}
\]

Thus the half-integer-looking expression is an integer. Indeed its bracket equals \(-2(n_-+n_0+r)\). Formula (18) is a coordinate-independent description of the same local shift once the symplectic and index conventions are fixed.

## Exercises with complete solutions

### Count the integrated directions

*Difficulty: Introductory.*

Let \(q\) have two positive, three negative and one null direction, and let \(\operatorname{codim}M=3\). Find \(d\) and \(\delta\) in both forms of (15).

**Solution.** Here \(r=2\), so \(d=2+3+1+2=8\). Counting compactly integrated negative, null and \(u\) directions gives \(\delta=-3-1-2=-6\). The alternative expression is \(n_+-d=2-8=-6\). The positive closed balls contribute no shift.

### An annulus with one boundary missing

*Difficulty: Intermediate.*

For \(0<a<b\), compute the compact cohomology with coefficients \(L\) of \(\{v\in\mathbb R^m:a\leq|v|^2<b\}\). Include the case \(m=0\), and compare with a compact closed annulus.

**Solution.** For \(m>0\), the inner open ball \(\{|v|^2<a\}\) and outer open ball \(\{|v|^2<b\}\) both have compact cohomology \(L[-m]\). The open-extension map is the orientation trace isomorphism. Their complement's compact cohomology is its cone, hence zero. For \(m=0\) the displayed set is empty. A compact closed annulus has ordinary cohomology of its sphere factor and is generally nonzero; replacing the omitted outer boundary by an included one changes the answer and invalidates the first integration in (13).

### The cone comparison is directional

*Difficulty: Intermediate.*

For \(r=0\), compare \(k_{[0,\infty)}\to k_{\{0\}}\) at positive and negative covectors at zero. Work with \(k\ne0\).

**Solution.** The open/closed boundary triangle is
\(k_{(0,\infty)}\to k_{[0,\infty)}\to k_{\{0\}}\xrightarrow{+1}\).
The open half-line has its nonzero boundary microsupport on the negative ray. Thus the second arrow is an isomorphism at every positive covector. At a negative covector the closed half-line is null, whereas the point sheaf is not; the map is not an isomorphism. The cone comparison in (15) therefore uses the selected positive covector and is not a global sheaf equivalence.

### Null directions need not mean isotropic directions

*Difficulty: Intermediate.*

For \(q(a,b)=a^2-b^2\), determine \(n_0\) and exhibit a nonzero isotropic vector. Explain which number enters (9).

**Solution.** Its symmetric matrix is invertible, so its radical is zero and \(n_0=0\). The vector \((1,1)\) satisfies \(q(1,1)=0\), so it is isotropic and nonzero. The null directions integrated as independent open balls in the proof are the radical directions, not arbitrary zero-value vectors. Hence (9) uses zero in this example.

### Check the index sign and parity

*Difficulty: Advanced.*

Take \(A=\operatorname{diag}(2,-3,0)\) and \(r=1\). Compute \(\tau\), \(\dim((T_pV)^\perp\cap\lambda_N)\), and (18). What happens to \(\tau\) if the last two planes in (16) are exchanged?

**Solution.** There is one positive, one negative and one null direction, so \(\tau=-(1-1)=0\) and the displayed intersection has dimension one. Here \(d=4\), \(c=2\), and \(1+\dim M-\dim Y=1-c-d=-5\). The bracket in (18) is \(-5-1-0=-6\), giving \(\delta=-3\), in agreement with \(-n_--n_0-r=-3\). Interchanging the last two planes negates the inertia index by alternation. In this balanced example it remains zero; for an unbalanced quadratic form that exchange would change the shift expression unless its ordered convention were corrected too.

### The null parameter still contributes a shift

*Difficulty: Advanced.*

Let \(f:\mathbb R^2\to\mathbb R\) be \(f(x,t)=x\), take \(N=\{x=0\}\), and choose the positive conormal \(dx\). Compare it with the model \(N=\{x=t^2\}\). Compute the formal local image of the closed upper-side coefficient in each case.

**Solution.** For \(x=0\) the quadratic form in the fibre is zero: \(n_0=1\), \(n_+=n_-=0\), \(r=0\), \(d=1\). The local fibre is an independent open interval, so (15) gives \(L_{\{0\}}[-1]\) at the positive covector. For \(x=t^2\), the form has \(n_+=1\) and no negative or null direction. Its positive-variable fibre is a compact interval for \(x\geq0\) near zero, so the formal image is \(L_{\{0\}}\) without shift. Both outputs are supported on the same submanifold in the selected category. Their different shifts record the different fibre integrations, not different output support sets.

### A parameter changes coordinates before it changes signature

*Difficulty: Intermediate.*

For \(a\) near zero, consider
\(h(a,t,u)=(1+a+t)t^2-u^2\).
Give exact parameter-preserving Morse coordinates near the zero critical family and check their local invertibility. Compare with \(g(a,t)=t^2+at\): why must its critical point and value be translated before applying the zero-value version of the lemma?

**Solution.** Restrict to \(1+a+t>0\) and set \(v=t\sqrt{1+a+t}\), \(w=u\). Then \(h=v^2-w^2\) exactly. At \((a,t,u)=(0,0,0)\), the derivative of \((a,t,u)\mapsto(a,v,w)\) is invertible; more generally its fibre derivative at \(t=u=0\) is \(\operatorname{diag}(\sqrt{1+a},1)\). The inverse function theorem gives smooth local inverse coordinates, retaining \(a\). The positive and negative dimensions remain one and one. For \(g\), the fibre derivative at \(t=0\) is \(a\), so \(t=0\) is not the critical family when \(a\ne0\). The true critical point is \(t_c(a)=-a/2\), with value \(-a^2/4\). Completing the square gives \(g=(t+a/2)^2-a^2/4\); translate by that critical section and subtract that critical value. Omitting either change would falsely claim the zero-value quadratic identity.

### A changing intersection can change inertia

*Difficulty: Intermediate.*

In \(\mathbb R^2\) with \(\omega=dp\wedge dq\), let \(\lambda_a=\{p=aq\}\). For \(-1<t<1\), compute \(\tau(\lambda_0,\lambda_t,\lambda_1)\), its radical dimension and its parity at \(t=0\) and on either side. Check the four-plane identity for \((\lambda_0,\lambda_t,\lambda_1,\lambda_2)\) at \(t=0\) and \(0<t<1\). Why does this not contradict continuity?

**Solution.** The graph formula gives
\(\tau=\operatorname{sgn}(-t)+\operatorname{sgn}(t-1)+\operatorname{sgn}(1)\).
It is \(1\) for \(t<0\), \(0\) at zero, and \(-1\) for \(t>0\). All pairwise intersections vanish off zero, so the radical is zero and its rank is three; the signature is odd, as required. At zero the first two planes coincide, with one-dimensional intersection, while both meet the third in zero. The radical is one-dimensional, its rank is two and its signature is even. At \(t=0\), the four ordered indices \((\tau_{123},\tau_{134},\tau_{124},\tau_{234})\) are \((0,-1,0,-1)\), giving \(-1=-1\). For \(0<t<1\), all four are \(-1\), giving \(-2=-2\). The pairwise intersection dimension changes at zero, so the hypothesis of the local-constancy theorem fails exactly where this jump occurs. The cocycle remains valid throughout, including the degenerate triple.

## References

The ordered signature and its reduction laws are classical results of Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985): Definition 7.1.1 and Proposition 7.1.2, printed pp. 121–122 (PDF pp. 124–125). Example 7.1.4, printed p. 123, uses the same symplectic form \(d\theta\). The matrix, radical and reduction arguments above prove the identities needed here, including degenerate intersections. The common-complement and parameter Morse arguments use the exact programme proofs linked in the text.

The related proper direct-image theorem is Theorem 7.3.1, printed pp. 129–131 (PDF pp. 132–134). It assumes a transverse conormal incidence, an isolated contributing covector and properness on the sheaf's support. Its degree is a purity degree: Example 7.2.6(i), printed p. 128, assigns the constant sheaf on a codimension-\(c\) submanifold degree \(c/2\). Thus for a hypersurface input its source and target purity degrees are \(1/2\) and \(c/2+\delta\). Substitution into that theorem gives (18) when the excess is zero, with precisely the vertical/conormal/pulled-vertical order in (16).

The clean excess, arbitrary bounded coefficient complex and represented local proper-support image in this lesson are established by the coordinate and four-integration proofs above. In particular the independent null variables contribute \(-n_0\), a term absent from the transverse theorem. The calculation follows the supports and their actual trace maps before recovering the invariant index; it does not infer a local clean theorem from a proper transverse statement.

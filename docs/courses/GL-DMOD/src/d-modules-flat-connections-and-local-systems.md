# D-modules, flat connections and local systems

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The equation \(u'=u\) has the solution \(e^x\). We can record the equation algebraically without adjoining that function: take a generator \(e\) and impose \(\partial e=e\). A map from this module to a space of functions sends \(e\) to a solution. A horizontal section **inside** the module, however, is \(e^{-x}e\). These two uses of the exponential have opposite signs. Keeping them distinct will organize the passage from differential equations to modules and then to local systems.

We assume the [preceding lesson](differential-operators-and-the-weyl-algebra.md), elementary coherent sheaf theory, Nakayama's lemma and the separatedness of the maximal-ideal filtration on a Noetherian local ring. The analytic part uses holomorphic power series and locally constant sheaves; its local differential-equation argument is proved below. The [Algebraic Geometry Bridge](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D100), [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) and [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50) provide background.

Throughout, \(k\) has characteristic zero and \(X\) is a smooth separated variety of pure dimension \(d\) over \(k\). Write \(\mathcal D=\mathcal D_X\), \(\mathcal T=\mathcal T_X\) and \(\omega_X=\bigwedge^d\Omega_X^1\). A D-module is a left \(\mathcal D\)-module quasi-coherent over \(\mathcal O_X\). Coherence over \(\mathcal O_X\) and coherence over \(\mathcal D\) are different conditions. Analytification is used only over \(\mathbf C\). All local systems here have finite-dimensional complex stalks. No cohomological shift enters the horizontal-section functor in this lesson.

## 1. Three meanings of a section

On an étale coordinate chart, put \(\partial_i=\partial/\partial x_i\). A left D-module gives operators on its sections satisfying

\[
\partial_i(fm)=\partial_i(f)m+f\partial_i(m),
\qquad [\partial_i,\partial_j]m=0.
\tag{1.1}
\]

Thus differentiation acts on both a coefficient and a module element. For a local frame \(e=(e_1,\ldots,e_r)\), write sections as \(e v\), where \(v\) is a column. Matrices \(A_i\) defined by \(\partial_i(e v)=e(\partial_i v+A_i v)\) encode the action. Horizontal sections satisfy

\[
\partial_i v=-A_i v.
\tag{1.2}
\]

For a cyclic module \(M=\mathcal D/\mathcal D P\), a D-linear map \(M\to F\) is determined by the image \(u\) of the generator, and the condition is \(Pu=0\). In symbols,

\[
\mathcal H om_{\mathcal D}(\mathcal D/\mathcal D P,F)
=\ker(P:F\longrightarrow F).
\tag{1.3}
\]

Here \(u\) is a section of the **target** \(F\). If \(M\) itself is a bundle with connection, its horizontal sections are instead elements of \(M\) killed by its connection. For \(\partial e=a e\), the represented equation is \(u'=a u\), whereas the horizontal coefficient equation is \(v'=-a v\). The solution local system is the dual of the horizontal local system: a horizontal covector is exactly a D-linear map to \(\mathcal O\). Section 7 will compute both on the punctured line.

## 2. The connection carried by a D-module

A connection on an \(\mathcal O_X\)-module \(M\) is a \(k\)-linear sheaf map

\[
\nabla:M\longrightarrow\Omega_X^1\otimes_{\mathcal O_X}M,
\qquad \nabla(fm)=df\otimes m+f\nabla m.
\tag{2.1}
\]

Contracting with a vector field gives \(\nabla_\xi\). Extend the map to forms by

\[
\nabla(\alpha\otimes m)=d\alpha\otimes m+(-1)^q\alpha\wedge\nabla m,
\qquad \alpha\in\Omega_X^q.
\tag{2.2}
\]

The coefficient Leibniz rule makes this formula balanced over \(\mathcal O_X\). The connection is **integrable**, or flat, if \(\nabla^2=0\). Its curvature evaluated on vector fields is

\[
R(\xi,\eta)=[\nabla_\xi,\nabla_\eta]-\nabla_{[\xi,\eta]}.
\tag{2.3}
\]

This is \(\mathcal O_X\)-linear in both vector fields and in \(m\). In commuting coordinates, (2.2) gives

\[
\nabla^2m=\sum_{i<j}dx_i\wedge dx_j\otimes
[\nabla_{\partial_i},\nabla_{\partial_j}]m.
\tag{2.4}
\]

Hence vanishing in (2.3) and (2.4) are equivalent. For a bundle matrix as in Section 1, flatness reads

\[
\partial_i A_j-\partial_j A_i+[A_i,A_j]=0.
\tag{2.5}
\]

**Theorem 2.1.** Left D-module structures on a fixed quasi-coherent \(\mathcal O_X\)-module are in bijection with integrable connections. The correspondence also identifies their morphisms.

**Proof.** A D-action defines \(\nabla_\xi m=\xi m\). The relation \(\xi f-f\xi=\xi(f)\) gives (2.1), and the relation between commutators of vector fields gives (2.3) with zero curvature. Since \(\mathcal T\) is locally free and dual to \(\Omega_X^1\), these contracted maps uniquely specify \(\nabla\).

Conversely, choose étale coordinates. Flatness makes the operators \(\nabla_i=\nabla_{\partial_i}\) commute. For the unique normal form established in the preceding lesson, set

\[
\left(\sum_\alpha a_\alpha\partial^\alpha\right)m
=\sum_\alpha a_\alpha\nabla_1^{\alpha_1}\cdots\nabla_d^{\alpha_d}m.
\tag{2.6}
\]

Iterating (2.1) yields the multi-index Leibniz identity

\[
\nabla^\alpha(fm)=
\sum_{\beta\leq\alpha}\binom\alpha\beta
\partial^\beta(f)\nabla^{\alpha-\beta}m.
\tag{2.7}
\]

For completeness, differentiating one more time splits each summand into the derivative of its coefficient and the derivative of its module part; Pascal's identity joins the two contributions. This proves (2.7) by induction on \(|\alpha|\). It is exactly the multiplication rule for normal forms in \(\mathcal D\), so (2.6) respects composition and the identity.

If \(\xi=\sum_i b_i\partial_i\), its action is \(\sum_i b_i\nabla_i\), which is the intrinsic contraction \(\nabla_\xi\). The local actions agree on functions and all vector fields on overlaps; these generate \(\mathcal D\), so the actions glue and do not depend on coordinates. The two constructions are inverse because the same generators determine the action. Finally, an \(\mathcal O_X\)-linear map commutes with \(\nabla\) precisely when it commutes with vector fields, hence with all of \(\mathcal D\). \(\square\)

This argument applies even when \(M\) has infinitely many generators. It is a statement about quasi-coherent modules with connection, not only about vector bundles. The ordinary Leibniz and integrability formulas agree with the formulas in the crystalline setting of [Stacks, Tag 07J5]; the identification with the characteristic-zero differential-operator action is proved here.

## 3. Why finite modules cannot have relations at a smooth point

The next theorem upgrades a finite module with a connection to a vector bundle. We first isolate the local mechanism.

At a \(k\)-rational smooth point \(p\), étale parameters \(t_i=x_i-x_i(p)\) identify the completed local ring with \(k[[t_1,\ldots,t_d]]\). One way to obtain this description is to apply the unique lifting property of the coordinate chart to each quotient by a power of the maximal ideal, and then take the inverse limit. Coordinate derivations extend continuously to the completion and become the formal partial derivatives. Consequently a nonzero element, or a nonzero vector of elements, has a finite least total degree. If that degree is positive, some partial derivative of its leading homogeneous part is nonzero and lowers the degree by one. Characteristic zero is essential for this last assertion.

**Theorem 3.1.** A D-module coherent over \(\mathcal O_X\) is locally free of finite rank.

**Proof.** First suppose \(k\) is algebraically closed, and let \(A=\mathcal O_{X,p}\) at a closed point, with maximal ideal \(\mathfrak m\). Choose a minimal set \(m_1,\ldots,m_r\) of generators of \(M_p\). If \(r=0\), Nakayama's lemma gives \(M_p=0\), which is free of rank zero. Otherwise let

\[
0\longrightarrow K\longrightarrow A^r\xrightarrow{\pi}M_p\longrightarrow0.
\tag{3.1}
\]

Minimality means that the images of the generators form a basis of \(M_p/\mathfrak mM_p\); therefore \(K\subset\mathfrak m A^r\). For each coordinate derivative choose a matrix \(B_i\) whose columns lift the elements \(\nabla_i m_j\). The operator \(D_i(v)=\partial_i v+B_i v\) on \(A^r\) then satisfies

\[
\pi D_i(v)=\nabla_i\pi(v),\qquad D_i(K)\subset K.
\tag{3.2}
\]

Suppose \(0\ne v\in K\). Separatedness embeds \(A^r\) in its completion, so \(v\) has a finite order \(q\geq1\). Choose \(i\) so that \(\partial_i\) does not kill its leading homogeneous vector. Then \(\partial_i v\) has order \(q-1\), while \(B_i v\) has order at least \(q\). Thus \(D_i(v)\in K\) is nonzero of order \(q-1\). Repeating, with a suitable derivative at each step, gives a relation of order zero. That contradicts \(K\subset\mathfrak m A^r\). Hence \(K=0\), proving freeness at \(p\).

A finite presentation makes freeness at a stalk persist on an open neighborhood: lift a stalk basis to sections, and shrink until the finitely generated kernel and cokernel of the resulting presentation vanish. Every point of a finite-type variety specializes to a closed point. An open neighborhood of that closed point contains its generalizations. Therefore these neighborhoods cover \(X\).

For a general characteristic-zero field, extend scalars to an algebraic closure. The pulled-back connection has the same properties, so the pulled-back module is locally free. To justify descent without a geometric shortcut, work on an affine chart \(\operatorname{Spec}A\). For every \(A\)-module \(N\), flat base change gives

\[
\operatorname{Tor}_1^A(M,N)\otimes_k\overline k
\cong\operatorname{Tor}_1^{A\otimes_k\overline k}
(M\otimes_k\overline k,N\otimes_k\overline k)=0.
\tag{3.3}
\]

Faithfulness of the field extension makes the group on the left zero before base change. Thus \(M\) is flat over \(A\). A finite flat module over a Noetherian local ring is free: for a minimal presentation (3.1), tensor with the residue field. Flatness and minimality imply \(K/\mathfrak mK=0\), so Nakayama gives \(K=0\). This proves the assertion over \(k\). \(\square\)

The proof used the Leibniz rule and smoothness, but did not need zero curvature. Any connection on a coherent module in characteristic zero already forces local freeness. Integrability determines which bundles carry a D-action.

## 4. Analytic flat frames and local systems

Let \(X\) now be a complex manifold. By a holomorphic flat bundle we mean a finite-rank holomorphic vector bundle with an integrable holomorphic connection. An algebraic flat bundle on a smooth complex variety gives such a bundle on \(X^{an}\).

The analytic differential-operator sheaf used below consists in coordinates of finite sums \(\sum a_\alpha(z)\partial^\alpha\) with holomorphic coefficients. Its normal forms are independent by testing on coordinate monomials; its multiplication follows from Leibniz's rule. Thus the coordinate algebra arguments also apply to these holomorphic operators.

**Lemma 4.1.** Near every point a holomorphic flat bundle has a frame of horizontal sections.

**Proof.** Trivialize the bundle on a polydisc with coordinates \(z_1,\ldots,z_d\) centered at the point, and write the matrices \(A_i\) as in (2.5). We will construct an invertible holomorphic matrix \(H\) satisfying

\[
\partial_i H=-A_iH\quad(1\leq i\leq d).
\tag{4.1}
\]

Here is the required one-variable existence argument with parameters. For a holomorphic matrix \(A(z,w)\), uniformly bounded by \(C\) on a smaller closed polydisc, solve \(\partial_z H=-AH\), \(H(0,w)=I\), by iterated integrals. Set \(U_0=I\) and

\[
U_{n+1}(z,w)=-\int_0^z A(\zeta,w)U_n(\zeta,w)\,d\zeta.
\tag{4.2}
\]

Integration is along the straight segment. Each term is holomorphic in all variables, and \(\|U_n\|\leq C^n|z|^n/n!\). The series \(H=\sum_{n\geq0}U_n\) therefore converges uniformly on compact subsets, is holomorphic, and solves the integral equation and hence the differential equation. For uniqueness, the integral equation for a difference with zero initial value, iterated \(n\) times, bounds it by \(C^n|z|^n/n!\) times its supremum; letting \(n\) grow gives zero. Multilinearity of the determinant and the differential equation give \(\partial_z\det H=-(\operatorname{tr}A)\det H\). Its initial value is one, so \(\det H=\exp(-\int_0^z\operatorname{tr}A)\ne0\).

Apply this construction to \(A_1\), treating \(z_2,\ldots,z_d\) as parameters, and use the frame change \(e'=eH\). Its connection matrices are

\[
A_i'=H^{-1}A_iH+H^{-1}\partial_iH.
\tag{4.3}
\]

Thus \(A_1'=0\). Curvature transforms by conjugation, so (2.5) becomes \(\partial_1A_j'=0\) for \(j>1\). The remaining matrices depend only on \(z_2,\ldots,z_d\) and form a flat connection in those variables. Induction on \(d\), starting with the one-variable construction, kills all the remaining matrices by a frame change independent of \(z_1\). The resulting frame is horizontal. \(\square\)

**Theorem 4.2.** Taking horizontal sections is an equivalence between holomorphic flat bundles on \(X\) and finite-rank complex local systems on \(X\). Its inverse is

\[
L\longmapsto(\mathcal O_X\otimes_{\mathbf C}L,d\otimes1).
\tag{4.4}
\]

**Proof.** In a horizontal frame, a section is horizontal precisely when all partial derivatives of its coefficients vanish. On a connected small polydisc these coefficients are constant. The kernel sheaf is therefore locally constant with stalk dimension equal to the bundle rank. Evaluation gives a natural isomorphism

\[
\mathcal O_X\otimes_{\mathbf C}\ker\nabla\longrightarrow M.
\tag{4.5}
\]

It is an isomorphism because horizontal frames are local bases, and it preserves connections by the Leibniz rule. Conversely, local trivializations of a local system have locally constant transition matrices. Extending these matrices to holomorphic functions glues a vector bundle, and their derivatives vanish, so the trivial local connections glue. Its horizontal sections recover \(L\). A map between flat bundles, written in horizontal frames, preserves connections precisely when its matrix has constant entries. Such matrices are exactly maps between the corresponding local systems. This proves the equivalence on objects and morphisms. \(\square\)

This is an analytic equivalence. It does not say that an algebraic connection is determined by its horizontal local system. The exponential example in Section 7 will exhibit two distinct algebraic connections with isomorphic analytic flat bundles. Their behavior at infinity belongs to the later study of regular singularities.

## 5. Densities change the side of the action

A right module must respect operator composition in the opposite order from a left module. The canonical bundle supplies the correction needed when coordinates change. For a top form \(\rho\), define

\[
\rho\cdot f=f\rho,
\qquad \rho\cdot\xi=-\mathcal L_\xi\rho.
\tag{5.1}
\]

Here \(\mathcal L_\xi\) is the Lie derivative. If \(\rho\) is a nonvanishing local top form, define \(\operatorname{div}_\rho\xi\) by \(\mathcal L_\xi\rho=(\operatorname{div}_\rho\xi)\rho\). For the coordinate volume form and \(\xi=\sum b_i\partial_i\), the divergence is \(\sum\partial_i b_i\). Indeed Cartan's formula \(\mathcal L_\xi=d\iota_\xi+\iota_\xi d\) applied to \(dx_1\wedge\cdots\wedge dx_d\) differentiates precisely those coefficients.

**Theorem 5.1.** For a left D-module \(M\), the tensor product \(M^r=\omega_X\otimes_{\mathcal O_X}M\) has the right action

\[
(\rho\otimes m)\cdot\xi
=-\mathcal L_\xi\rho\otimes m-\rho\otimes\nabla_\xi m.
\tag{5.2}
\]

The resulting functor is an equivalence from left to right quasi-coherent D-modules, with inverse \(N\mapsto\omega_X^{-1}\otimes_{\mathcal O_X}N\).

**Proof.** Formula (5.2) is balanced. Moving a coefficient \(f\) between its factors gives the same extra term \(-\xi(f)\rho\otimes m\), because both the Lie derivative and the connection satisfy their Leibniz rules.

In the coordinate volume frame, (5.2) becomes \(m\cdot\partial_i=-\nabla_i m\). The transpose

\[
t(f)=f,\qquad t(\partial_i)=-\partial_i,
\qquad t(PQ)=t(Q)t(P)
\tag{5.3}
\]

is an anti-automorphism of the coordinate differential-operator algebra. To check it, transposing \(\partial_i f-f\partial_i=\partial_i(f)\) gives the same relation, and commuting coordinate derivatives remain commuting. The normal form from the preceding lesson then establishes it on the whole algebra. It is involutive on the generators, hence on every operator. Thus the local right action \(m\cdot P=t(P)m\) is an associative action. For \(\xi=\sum b_i\partial_i\), it reads

\[
m\cdot\xi=-\sum_i\nabla_i(b_i m)
=-\nabla_\xi m-(\operatorname{div}_\rho\xi)m,
\tag{5.4}
\]

which is exactly (5.2). Since (5.2) is intrinsic, the local right actions glue. Setting \(M=\mathcal O_X\) recovers (5.1).

For the inverse construction, choose a local nonvanishing form \(\rho\). On \(\rho^{-1}\otimes N\), set

\[
\nabla_\xi(\rho^{-1}\otimes n)
=\rho^{-1}\otimes
\bigl(-n\cdot\xi-(\operatorname{div}_\rho\xi)n\bigr).
\tag{5.5}
\]

This is independent of the frame. Replacing \(\rho\) by \(g\rho\) replaces the coefficient \(n\) representing a fixed section by \(gn\). The identities

\[
(gn)\cdot\xi=g(n\cdot\xi)-\xi(g)n,
\qquad \operatorname{div}_{g\rho}\xi
=\operatorname{div}_\rho\xi+g^{-1}\xi(g)
\tag{5.6}
\]

show that the extra terms cancel in (5.5). In coordinate volume frames it is just the inverse of (5.3); hence it is a flat connection and defines a left D-action by Theorem 2.1. The evaluation isomorphisms \(\omega_X^{-1}\otimes\omega_X\otimes M\cong M\) and \(\omega_X\otimes\omega_X^{-1}\otimes N\cong N\) preserve the actions by (5.2) and (5.5). They also commute with morphisms. This proves the equivalence. \(\square\)

The divergence explains a frequent shift in Euler parameters. On the punctured line let \(\theta=x\partial\) and \(\theta e=\lambda e\). In the frame \(dx\), the right generator has

\[
(dx\otimes e)\cdot\theta=-(\lambda+1)(dx\otimes e).
\tag{5.7}
\]

In the invariant frame \(dx/x\), the divergence of \(\theta\) is zero, so its right eigenvalue is \(-\lambda\). The generators differ by the invertible function \(x^{-1}\); the two formulas describe the same right module.

## 6. Tensor products and covectors

For two left D-modules, define on \(M\otimes_{\mathcal O_X}N\)

\[
\nabla_\xi(m\otimes n)
=\nabla_\xi m\otimes n+m\otimes\nabla_\xi n.
\tag{6.1}
\]

Both ways of moving a function across the tensor product produce the same \(\xi(f)m\otimes n\), so the action is well-defined and satisfies the Leibniz rule. Its curvature is

\[
R_{M\otimes N}(\xi,\eta)
=R_M(\xi,\eta)\otimes1+1\otimes R_N(\xi,\eta).
\tag{6.2}
\]

To verify this identity, expand the two composite actions in (6.1): the terms differentiating both factors occur once in each order and cancel in the commutator. Subtracting the action of \([\xi,\eta]\) leaves the two curvatures. Thus the tensor product is again a D-module. Quasi-coherence is preserved by the ordinary sheaf tensor product. The tensor unit is \(\mathcal O_X\) with its usual derivations.

For the sheaf \(\mathcal H om_{\mathcal O_X}(M,N)\), put

\[
(\nabla_\xi\phi)(m)
=\nabla_\xi^N\phi(m)-\phi(\nabla_\xi^M m).
\tag{6.3}
\]

The coefficient terms cancel to make \(\nabla_\xi\phi\) \(\mathcal O_X\)-linear in \(m\). The formula satisfies the Leibniz rule in \(\phi\), and expanding its commutator gives \(R_N\phi-\phi R_M=0\). It therefore defines a flat connection on this sheaf. If \(M\) is a finite-rank bundle, the Hom sheaf is \(M^\vee\otimes N\), hence quasi-coherent and a D-module in our category. For arbitrary quasi-coherent \(M\), the Hom sheaf need not be quasi-coherent; the connection formula still makes sense, but that categorical qualifier is necessary.

For example, on \(\operatorname{Spec}k[x]\), the Hom sheaf from \(\bigoplus_{n\geq0}\mathcal O\) to \(\mathcal O\) has sections \(\prod_{n\geq0}k[x]\). On \(D(x)\) it has sections \(\prod_{n\geq0}k[x,x^{-1}]\). Localization of the first product has a common bound on the denominators of every component. The tuple \((1,x^{-1},x^{-2},\ldots)\) has no such bound, so this sheaf is not the quasi-coherent sheaf associated to its affine sections.

For a flat bundle \(M\), its dual connection is the special case \(N=\mathcal O_X\) of (6.3). Evaluation \(M^\vee\otimes M\to\mathcal O_X\) is D-linear because its two connection terms sum to the derivative of the pairing. Horizontal covectors are D-linear maps to \(\mathcal O_X\), establishing the duality between the two local systems described in Section 1.

## 7. Calculations on the line

### Functions, operators and a point module

The structure sheaf \(\mathcal O_X\) is a D-module by ordinary differentiation. The regular left module \(\mathcal D_X\) is generated by one element over \(\mathcal D_X\), but on a positive-dimensional coordinate chart it has infinitely many independent \(\mathcal O_X\)-basis elements \(\partial^\alpha\). Thus D-coherence alone does not imply the finite-rank conclusion of Theorem 3.1.

On \(\mathbf A^1\), let \(A_1=k\langle x,\partial\rangle/(\partial x-x\partial-1)\). Normal form gives

\[
A_1/A_1\partial\cong k[x],
\qquad \partial(x^j)=j x^{j-1}.
\tag{7.1}
\]

For the point module \(\delta_0=A_1/A_1x\), order the normal form with \(x\) on the right. Its basis is \(\delta,\partial\delta,\partial^2\delta,\ldots\), with

\[
x\partial^j\delta=-j\partial^{j-1}\delta,
\qquad \partial(\partial^j\delta)=\partial^{j+1}\delta.
\tag{7.2}
\]

Indeed \([x,\partial^j]=-j\partial^{j-1}\), and the term \(\partial^jx\delta\) is zero. Each vector is killed by a sufficiently large power of \(x\), so localization away from zero vanishes. Yet \(x\delta_0=\delta_0\), since every \(\partial^j\delta\) is \(x(-\partial^{j+1}\delta/(j+1))\). Its ordinary fiber \(\delta_0/x\delta_0\) is zero although the module is nonzero. There is no contradiction with Nakayama: this module is not finite over \(k[x]\).

### Exponential connections

For \(f\in k[x]\), define \(E^f=k[x]e\) by

\[
\partial(ge)=(g'+f'g)e.
\tag{7.3}
\]

It is the cyclic module \(A_1/A_1(\partial-f')\). To see this, repeated reduction of the highest power of \(\partial\) by the monic operator \(\partial-f'\), with coefficients on the left, leaves a unique polynomial coefficient times the generator. The resulting action is (7.3); a nonzero polynomial remainder cannot annihilate the free generator of \(k[x]e\).

Over \(\mathbf C\), the represented scalar equation has solutions \(u=c e^f\); horizontal module sections are \(c e^{-f}e\). For \(f=x\), any algebraic \(\mathcal O\)-module isomorphism \(\mathcal O\to E^x\) multiplies its generator by a unit of \(k[x]\), hence by a nonzero constant. D-linearity would require \(g'+g=0\), impossible for that constant. The modules are not algebraically D-isomorphic. Analytically, multiplication by the nowhere-zero entire function \(e^{-x}\) gives an isomorphism \(\mathcal O^{an}\to(E^x)^{an}\) preserving the connections. Both analytic horizontal local systems are constant of rank one.

### Powers and their monodromy

On \(\mathbf G_m\), put \(B=k[x,x^{-1}]\) and \(\theta=x\partial\). The module

\[
K_\lambda=\mathcal D_{\mathbf G_m}/\mathcal D_{\mathbf G_m}(\theta-\lambda)
=B e_\lambda
\tag{7.4}
\]

has action \(\partial(ge_\lambda)=(g'+\lambda x^{-1}g)e_\lambda\). Monic reduction by \(\partial-\lambda x^{-1}\) proves that its underlying \(B\)-module is free of rank one. In particular,

\[
\theta(x^j e_\lambda)=(j+\lambda)x^j e_\lambda.
\tag{7.5}
\]

Choose a branch of \(\log x\) on a simply connected analytic open set. Its horizontal sections are \(c x^{-\lambda}e_\lambda\), with positive-loop monodromy \(e^{-2\pi i\lambda}\). The scalar equation \((\theta-\lambda)u=0\) has solutions \(c x^\lambda\), with monodromy \(e^{2\pi i\lambda}\). These are dual rank-one local systems. Tensoring the generators gives

\[
K_\lambda\otimes_{\mathcal O}K_\mu\cong K_{\lambda+\mu},
\qquad K_\lambda^\vee\cong K_{-\lambda}.
\tag{7.6}
\]

The ordinary Laurent-polynomial module with the usual derivative is \(K_0\). As a module on \(\mathbf A^1\), \(k[x,x^{-1}]\) still has a D-action; it is not coherent over \(k[x]\). It is generated over \(A_1\) by \(x^{-1}\): derivatives supply all negative powers, and multiplication by \(x\) supplies the nonnegative powers.

### Euler weights before restriction

On the full affine line the cyclic module \(Q_\lambda=A_1/A_1(\theta-\lambda)\) has the basis

\[
u_j=x^j e\ (j\geq0),\qquad
u_{-s}=\partial^s e\ (s\geq1).
\tag{7.7}
\]

The actions are

\[
xu_j=\begin{cases}u_{j+1}&j\geq0,\\
(\lambda+j+1)u_{j+1}&j<0,\end{cases}
\qquad
\partial u_j=\begin{cases}(\lambda+j)u_{j-1}&j>0,\\
u_{j-1}&j\leq0.\end{cases}
\tag{7.8}
\]

In particular \(\theta u_j=(\lambda+j)u_j\). To prove these formulas, commute \(\partial\) past a positive power of \(x\), or commute \(x\) past a positive power of \(\partial\), and use \(\theta e=\lambda e\). They reduce any mixed monomial \(x^a\partial^b e\) with \(a,b>0\), proving spanning. For independence, start with an abstract vector space on the displayed \(u_j\) and define the two actions by (7.8). Direct substitution gives \((\partial x-x\partial)u_j=u_j\), including \(j=-1,0\): at \(-1\) the two coefficients are \(\lambda\) and \(\lambda-1\), and at zero they are \(\lambda+1\) and \(\lambda\). Thus this is an \(A_1\)-module generated by \(u_0\), with \((\theta-\lambda)u_0=0\). The spanning map from \(Q_\lambda\) onto it proves independence as well.

Restriction to \(\mathbf G_m\) sends the positive vectors to \(x^j e_\lambda\) and sends

\[
\partial^s e\longmapsto
\lambda(\lambda-1)\cdots(\lambda-s+1)x^{-s}e_\lambda.
\tag{7.9}
\]

This follows by differentiating successively in (7.4). The falling factorial records precisely which of these vectors disappear on restriction at integral parameters. For example, at \(\lambda=0\) every \(u_{-s}\) restricts to zero. Those vectors form a nonzero submodule supported at the origin. Local systems on the punctured line alone cannot detect it.

### The Euler solution complex at zero

Consider on the analytic line the unshifted two-term complex

\[
\mathcal O^{an}\xrightarrow{z\partial_z-\lambda}\mathcal O^{an},
\quad\text{in degrees }0,1.
\tag{7.10}
\]

It computes the degree-zero solution sheaf and the first derived solution sheaf of \(\mathcal D/\mathcal D(z\partial_z-\lambda)\). Indeed right multiplication by this nonzero operator gives an injective map of free left D-modules: the order-symbol domain argument in coordinates proves injectivity. Applying Hom into \(\mathcal O^{an}\) gives (7.10).

At the origin, write a holomorphic germ as \(\sum_{j\geq0}a_jz^j\). The operator multiplies its \(j\)-th coefficient by \(j-\lambda\). If \(\lambda\notin\mathbf Z_{\geq0}\), these numbers are nonzero and their inverses are uniformly bounded for \(j\geq0\); division therefore preserves convergence. Both kernel and cokernel stalks at zero vanish. If \(\lambda=N\in\mathbf Z_{\geq0}\), the kernel is \(\mathbf C z^N\) and the cokernel is the one-dimensional class of \(z^N\), since the same convergent division works for the other coefficients.

Away from zero the kernel is the rank-one system of branches of \(z^\lambda\). The cokernel is locally zero: for a given holomorphic \(g\), on a small simply connected open set avoiding zero the formula

\[
u=z^\lambda\left(c+\int z^{-\lambda-1}g(z)\,dz\right)
\tag{7.11}
\]

solves \((z\partial_z-\lambda)u=g\). Thus for nonintegral \(\lambda\) the kernel has no nonzero section on the full punctured disc, because its monodromy has no fixed vector. For negative integral \(\lambda\) it is constant on the punctured disc but has zero stalk at the origin. For nonnegative integral \(\lambda\), the kernel extends as a constant rank-one sheaf, generated locally by \(z^N\), and the first cohomology sheaf is a skyscraper at zero. This reproduces the example of [Kashiwara–Schapira, Section 2.9.14] by direct power-series calculation. Perverse normalization would shift this solution complex by \([1]\); its extensions will be studied later.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Give the isomorphisms in (7.1) and (7.2), including the actions, and compute the ordinary fiber of the point module at zero.

**Solution.** The map \(A_1\to k[x]\), \(P\mapsto P(1)\), is surjective. In the normal form \(P=\sum a_j(x)\partial^j\), its value is \(a_0(x)\); hence its kernel is \(A_1\partial\). This proves (7.1) and the usual actions. The reversed normal form \(P=\sum b_j(\partial)x^j\) is unique by transposition of normal form. Modulo \(A_1x\), only \(b_0(\partial)\) remains, giving the basis \(k[\partial]\delta\). The commutator calculation yields (7.2). Multiplication by \(x\) is surjective on this basis, so the ordinary fiber is zero. Its localization at zero is nevertheless nonzero: if \(h(x)\) has nonzero constant term, \(h(x)\delta=h(0)\delta\ne0\), so \(\delta\) survives that localization.

**Exercise 8.2 (easy).** Compute the coordinate transpose of \(P=x^2\partial^2+x\partial\), and compare the right Euler actions in the frames \(dx\) and \(dx/x\).

**Solution.** Reversing the factors gives

\[
t(P)=\partial^2x^2-\partial x
=x^2\partial^2+3x\partial+1,
\tag{8.1}
\]

because \(\partial^2x^2=x^2\partial^2+4x\partial+2\) and \(\partial x=x\partial+1\). For a left Euler eigenvector of eigenvalue \(\lambda\), (5.2) gives \(-\lambda-1\) in the volume frame \(dx\), whose divergence is one. The invariant form \(dx/x\) has Lie derivative zero, giving eigenvalue \(-\lambda\). Equivalently, if \(n=dx\otimes e\), the right-module identity gives \((x^{-1}n)\theta=x^{-1}(n\theta)-\theta(x^{-1})n=-\lambda x^{-1}n\).

**Exercise 8.3 (medium).** Determine when \(E^f\) and \(E^g\), for polynomials \(f,g\in k[x]\), are algebraically isomorphic as D-modules. Over \(\mathbf C\), determine when their analytifications are isomorphic.

**Solution.** An algebraic isomorphism must send \(e_f\) to \(h e_g\), where \(h\) is a unit of \(k[x]\), hence a nonzero constant. Commuting with \(\partial\) gives \(h'+g'h=f'h\), so \(f'=g'\). In characteristic zero this says \(f-g\) is constant; the converse is immediate because the actions then agree. Analytically the nonzero entire function \(h=e^{f-g}\) satisfies the same equation, so any two of these analytic flat bundles are isomorphic. In particular \(E^x\) and \(E^0\) give the required distinction between algebraic and analytic connections.

**Exercise 8.4 (medium).** Verify integrability of a tensor connection and compute \(K_\lambda\otimes K_\mu\) and \(\mathcal H om_{\mathcal O}(K_\lambda,K_\mu)\), including both monodromy conventions.

**Solution.** Expanding two successive applications of (6.1) gives the two curvatures in (6.2); the mixed terms cancel. Thus flat factors give a flat tensor connection. For \(e_\lambda\otimes e_\mu\), the Euler eigenvalue is \(\lambda+\mu\), so the tensor module is \(K_{\lambda+\mu}\). The map \(\phi(e_\lambda)=e_\mu\) is a basis of the Hom line, and (6.3) gives \(\theta\phi=(\mu-\lambda)\phi\); hence the Hom module is \(K_{\mu-\lambda}\). Their horizontal monodromies are respectively \(e^{-2\pi i(\lambda+\mu)}\) and \(e^{-2\pi i(\mu-\lambda)}\). Their scalar solution monodromies are the reciprocals.

**Exercise 8.5 (hard).** Prove that every Fitting ideal of a coherent module with connection is stable under derivations. Use this to give a second proof of Theorem 3.1.

**Solution.** Work in a local coordinate ring \(A\), and let \(M\) be finite. For a presentation \(A^s\to A^r\to M\to0\), the ideal \(\operatorname{Fitt}_i(M)\) is generated by the \((r-i)\)-minors of its relation matrix, with the usual conventions for zero-size or oversized minors. These ideals are independent of presentation. Invertible row and column operations preserve the minor ideals. Adjoining a generator with its defining relation, then eliminating its coefficient by row operations, adjoins an identity block and preserves the prescribed minor ideal. Adjoining a redundant relation also changes no minor ideal, by multilinearity in its column. Adjoin the generators of both presentations to obtain the same surjection onto \(M\). Their two sets of relation columns generate the same kernel, so each set consists of linear combinations of the other; multilinearity then proves equality of their minor ideals. The same description shows that Fitting ideals commute with ring base change.

Fix a derivation \(\delta\), and put \(B=A[\epsilon]/(\epsilon^2)\). The map \(\sigma(a)=a+\epsilon\delta(a)\), \(\sigma(\epsilon)=\epsilon\), is an automorphism of \(B\) with inverse given by the minus sign. On \(M\otimes_A B=M\oplus\epsilon M\), the map

\[
T(m+\epsilon n)=m+\epsilon(n+\nabla_\delta m)
\tag{8.2}
\]

is an invertible \(\sigma\)-semilinear map. Its semilinearity is exactly the Leibniz rule; its inverse replaces \(\nabla_\delta\) by its negative. Transporting a presentation by \(T\) and \(\sigma\) gives

\[
\sigma\bigl(\operatorname{Fitt}_i(M)B\bigr)
=\operatorname{Fitt}_i(M)B.
\tag{8.3}
\]

For \(a\) in the Fitting ideal, \(a+\epsilon\delta(a)\) lies in its extension to \(B\). Membership is coefficientwise in \(A\oplus\epsilon A\); therefore \(\delta(a)\) lies in the original ideal. This proves stability.

At an algebraically closed smooth closed point, a nonzero derivation-stable ideal \(J\) equals \(A\). Indeed a nonzero element has finite order in the completed power-series ring; repeated suitable coordinate derivatives lower that order until an element has nonzero constant term and is a unit. All these derivatives still belong to \(J\).

Now choose a minimal presentation (3.1) of \(M_p\) with \(r>0\). The entries of any finite generating relation matrix lie in \(\mathfrak m\). Their ideal is \(\operatorname{Fitt}_{r-1}(M_p)\), so it is proper. Its derivation stability forces it to be zero. Thus every relation entry is zero, \(K=0\), and \(M_p\) is free. The rank-zero case follows from Nakayama. The open-neighborhood and field-descent arguments of Theorem 3.1 finish the proof globally. This proof, too, needs a connection but not its integrability.

**Exercise 8.6 (medium).** Classify the algebraic D-isomorphisms between \(K_\lambda\) and \(K_\mu\) on \(\mathbf G_m\). Show that over \(\mathbf C\) the answer agrees with the isomorphism classification of their horizontal local systems.

**Solution.** An isomorphism sends \(e_\lambda\) to \(h e_\mu\) with \(h\in B^\times\). Every Laurent-polynomial unit is \(c x^n\), \(c\ne0\), \(n\in\mathbf Z\): the difference between its highest and lowest exponents adds under multiplication, so a unit has that difference zero. D-linearity requires \(\theta(h)+\mu h=\lambda h\), which gives \(n+\mu=\lambda\). Hence the modules are isomorphic exactly when \(\lambda-\mu\in\mathbf Z\). The horizontal local systems have monodromies \(e^{-2\pi i\lambda}\) and \(e^{-2\pi i\mu}\); these agree exactly under the same condition. This agreement for this family does not eliminate the exponential counterexample on the affine line.

**Exercise 8.7 (hard).** In characteristic \(p>0\), give a coherent nonfree module with an integrable connection on the affine line, and explain why it does not carry the action of every Grothendieck differential operator extending the usual multiplication action.

**Solution.** On \(M=k[x]/(x^p)\), ordinary differentiation is well-defined because \(\partial(x^p)=0\), and defines a connection by \(\nabla m=dx\otimes\partial m\). In dimension one its curvature is zero. The module is finite and nonfree near zero. However, the Hasse operator \(H_p(x^j)=\binom jp x^{j-p}\) satisfies \([H_p,x^p]=1\) as an operator on \(k[x]\), by the binomial identity \(\binom{j+p}p=\binom jp+1\) in characteristic \(p\). Since \(x^p\) acts by zero on \(M\), its commutator with any endomorphism of \(M\) is zero; it cannot equal the identity on this nonzero module. Thus the connection does not extend to the full differential-operator ring. This pinpoints why both the connection-to-D-module argument and the order-lowering proof use characteristic zero.

## What this lesson does not prove

The commutative algebra prerequisites are [Nakayama's lemma, Stacks Tag 00DV](https://stacks.math.columbia.edu/tag/00DV), separatedness \(\bigcap_q\mathfrak m^qA=0\) for a Noetherian local ring, and the local coordinate description of a smooth variety. For the separatedness assertion, [Krull's intersection theorem, Stacks Tag 00IP](https://stacks.math.columbia.edu/tag/00IP), states that \(\bigcap_n I^nM=0\) for a finite module over a Noetherian local ring and a proper ideal \(I\); apply it to \(M=A\) and \(I=\mathfrak m\). Étale coordinates identify the completed local ring at a rational smooth point with a formal power-series ring by nilpotent lifting, as discussed in Section 3. We also use the elementary flat-base-change identity for Tor, which follows by tensoring a free resolution with a flat algebra. Smooth coordinate charts and étale lifting were the geometric prerequisites of the preceding lesson.

All four central equivalences and local-freeness assertions are proved here. We have not proved algebraic Riemann–Hilbert, a regularity criterion at the boundary of a compactification, or the extension theory of perverse sheaves. Nor have we identified flat connections with crystals on a de Rham prestack; that requires a later construction. The crystalline definitions in [Stacks, Tags 07IR and 07J5] provide background, with their own divided-power hypotheses, rather than a substitute for the characteristic-zero proofs above.

## References

- The Stacks project, *Crystalline Cohomology*, [Tag 07J5, Connections](https://stacks.math.columbia.edu/tag/07J5), and [Tag 07IR, Crystals in modules](https://stacks.math.columbia.edu/tag/07IR); *Sheaves of Modules*, [Tag 0G3P](https://stacks.math.columbia.edu/tag/0G3P). These sections were compared in the [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/crystalline.html#section-connections), an edition with AI-proposed corrections and additions, not reviewed by the official Stacks maintainers.
- Edward Frenkel, *Lectures on the Langlands Program and Conformal Field Theory*, Sections 3.4–3.6, for cyclic equations, the Euler example and the distinction between algebraic and analytic descriptions. [Author's arXiv text](https://arxiv.org/abs/hep-th/0512172). The actions and sign conventions used here are derived from \([\partial,x]=1\).
- Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, Sections 7.2.1–7.2.3, for D-complexes, differential forms and tensor structures. Side-changing is given directly in Section 5 above; no derived equivalence from that appendix is required here.
- V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), for solution complexes of D-modules. Section 7 above computes the stalks and local monodromy of the Euler solution complex directly, without the general Riemann–Hilbert theorem.

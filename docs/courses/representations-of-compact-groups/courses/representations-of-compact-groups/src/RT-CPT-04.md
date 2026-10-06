# SU(2), SO(3) and spherical harmonics

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

Rotating a vector, rotating a quadratic form and rotating a two-component spinor produce different representation spaces. Their dimensions alone are suggestive—three, five and two—but dimensions do not explain why a spinor requires a covering group or why a quadratic form has an invariant scalar part. We will connect these examples through explicit group maps and descent conditions.

Start with ordinary geometric measurements, then construct the quaternion covering maps. Polynomial representations provide the complete irreducible list on the covering group; checking its central elements tells us which representations describe \(SO(3)\), \(SO(4)\) and \(U(2)\). After that classification, harmonic polynomials turn the rotation types into a complete basis of functions on the sphere. Their zonal functions diagonalize the great-circle transform and prove the central-section uniqueness theorem for symmetric convex bodies.

We use [unitarization, complete reducibility and Schur's lemma](RT-CPT-01.md), [coefficient density](RT-CPT-02.md), and [character completeness and the character test](RT-CPT-03.md). Round measure on \(S^2\) and Haar measures have mass one. Our spherical Laplacian has nonpositive eigenvalues.

## What a quadratic measurement sees

A complex quadratic polynomial on \(\mathbb R^3\) has the form \(x^{\mathsf T}Ax\), with \(A\) a complex symmetric \(3\times3\) matrix. A rotation acts by \(A\mapsto RAR^{\mathsf T}\), so it preserves the trace. Consequently this six-dimensional space splits into a one-dimensional part spanned by \(x^2+y^2+z^2\) and a five-dimensional part given by trace-zero matrices. Direct differentiation gives
\[
\Delta_{\mathbb R^3}(x^{\mathsf T}Ax)=2\operatorname{tr}A.
\]
Thus the trace-zero measurements are precisely the harmonic quadratics. On the sphere the scalar part is constant; the other part measures directional variation. For example, the rotation-invariant function \(x^2+y^2+z^2\) cannot belong to the same irreducible type as \(2z^2-x^2-y^2\). We have not yet proved that all five trace-zero directions form one irreducible. The classification below will explain that fact, and will show why the analogous degree-\(\ell\) space has dimension \(2\ell+1\).

## A covering group built from unit quaternions

Identify the quaternion algebra with the real span of \(1,i,j,k\), with \(i^2=j^2=k^2=-1\) and \(ij=k=-ji\), cyclically. An explicit algebra embedding is

\[
a+bi+cj+dk\longmapsto
\begin{pmatrix}
a+bi&c+di\\
-c+di&a-bi
\end{pmatrix}.
\tag{1.1}
\]

The images of \(i,j,k\) satisfy these multiplication relations, so linearity verifies multiplication on the entire algebra. If \(q=a+bi+cj+dk\), quaternion conjugation gives \(q\bar q=|q|^2\), and (1.1) has determinant \(|q|^2\). Its adjoint corresponds to \(\bar q\). Every element of \(SU(2)\) has the displayed matrix form with \(|q|=1\): its second column is the unique unit vector orthogonal to the first that makes the determinant one. Thus \(SU(2)\) is exactly the unit quaternions, with underlying space \(S^3\).

Left and right multiplication by a unit quaternion are real linear isometries of \(\mathbb R^4\), because quaternion norms multiply. They preserve round surface measure. Consequently normalized round measure on \(S^3\) is Haar measure on this group.

## Ordinary rotations and the factor of two

The imaginary quaternions form \(\mathbb R^3\). For a unit quaternion \(q\), define

\[
\kappa(q)v=qvq^{-1}.
\tag{3.1}
\]

This real linear map preserves the imaginary subspace and its norm. It is orthogonal, and its determinant is one by continuity on the connected sphere \(S^3\), since the identity has determinant one.

If \(q=\cos\theta+u\sin\theta\), choose a perpendicular unit vector \(v\) and put \(w=u\times v=uv\). Quaternion multiplication gives

\[
\kappa(q)u=u,\qquad
\kappa(q)v=\cos(2\theta)v+\sin(2\theta)w,\qquad
\kappa(q)w=-\sin(2\theta)v+\cos(2\theta)w.
\tag{3.2}
\]

For instance, expand \((c+su)v(c-su)\), use \(uv=-vu=w\) and \(uvu=v\), and obtain \((c^2-s^2)v+2csw\). This proves the first rotation formula; the second follows in the same basis. Thus the quaternion parameter \(\theta\) gives a spatial rotation of angle \(2\theta\).

Every matrix in \(SO(3)\) fixes some unit vector: its nonreal eigenvalues occur in conjugate pairs, while its real eigenvalues are \(1\) or \(-1\), and determinant one in odd dimension forces an eigenvalue one. On the orthogonal plane it is an orientation-preserving planar rotation. Equation (3.2) realizes that axis and angle. Hence \(\kappa\) is surjective. Its kernel consists of the quaternions commuting with all imaginary quaternions, hence with \(i,j,k\); their multiplication relations force such a quaternion to be real. Among unit quaternions these are \(1,-1\).

We have proved

\[
SO(3)\simeq SU(2)/\{I,-I\}.
\tag{3.3}
\]

The isomorphism is topological as well: a continuous bijection from the compact quotient onto a Hausdorff group is a homeomorphism.

## Four-dimensional rotations and U(2)

Quaternion multiplication defines

\[
\Phi:SU(2)\times SU(2)\longrightarrow SO(4),\qquad
\Phi(a,b)q=aqb^{-1}.
\tag{6.1}
\]

It is a homomorphism because its left and right actions commute. They are orthogonal, and their determinant is one by connectedness. To prove surjectivity, take \(R\in SO(4)\) and put \(q=R(1)\). The operator \(L_{q^{-1}}R\) fixes the real unit vector \(1\), hence acts on its imaginary orthogonal complement as an element of \(SO(3)\). By (3.3), it is conjugation by some \(b\). Therefore \(R(x)=qbx b^{-1}=\Phi(qb,b)x\). If \(\Phi(a,b)\) is identity, its value at \(1\) gives \(a=b\), and then \(a\) commutes with every quaternion, forcing \(a=b=\pm1\). We have proved

\[
SO(4)\simeq
(SU(2)\times SU(2))/\{(1,1),(-1,-1)\}.
\tag{6.2}
\]

For \(U(2)\), the map \((z,g)\mapsto zg\) from \(S^1\times SU(2)\) is surjective: choose \(z^2=\det U\) and take \(g=z^{-1}U\). Its kernel is \(\{(1,I),(-1,-I)\}\).

These maps separate the geometric quotient from the representation question. For a surjective continuous map \(H\to H/N\) of compact groups, pullback preserves invariant subspaces and equivalence. A representation of \(H\) factors through the quotient exactly when every element of \(N\) acts as identity; the resulting map is continuous by the quotient topology. We will therefore classify on the covering groups and then test their kernels. The relevant tests are \(-I\) for \(SO(3)\), \((-I,-I)\) for \(SO(4)\), and \((-1,-I)\) for \(U(2)\).

## Integrating on the class interval

**Proposition 1.2 (conjugacy and integration).** Each element of \(SU(2)\) is conjugate to exactly one

\[
t_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta}),
\qquad 0\leq\theta\leq\pi.
\]

For every continuous central function \(f\),

\[
\int_{SU(2)}f(g)\,dg
=\frac2\pi\int_0^\pi f(t_\theta)\sin^2\theta\,d\theta.
\tag{1.3}
\]

**Proof.** The finite-dimensional spectral theorem diagonalizes a unitary matrix. Determinant one makes its eigenvalues \(z,z^{-1}\), with \(|z|=1\). Multiplying a diagonalizing unitary matrix by a scalar makes its determinant one without changing the conjugation. The matrix corresponding to \(j\) interchanges the two eigenvalues. We can therefore choose \(\theta\in[0,\pi]\). Trace is \(2\cos\theta\), which is injective on this interval, proving uniqueness.

Write a unit quaternion as

\[
q=\cos\theta+u\sin\theta,\qquad u\in S^2,\quad 0<\theta<\pi.
\tag{1.4}
\]

The derivative in the \(\theta\) direction has length one and is orthogonal to the two \(u\) directions. Their lengths are multiplied by \(\sin\theta\). The round metric is therefore \(d\theta^2+\sin^2\theta\,ds_{S^2}^2\), and the volume element is \(\sin^2\theta\,d\theta\,dA(u)\). Its total volume is \(4\pi\int_0^\pi\sin^2\theta\,d\theta=2\pi^2\). The poles have measure zero. The real part of \(q\), equivalently half its matrix trace, is \(\cos\theta\), so (1.4) lies in the class of \(t_\theta\). Integrating over \(u\) and dividing by \(2\pi^2\) proves (1.3). ∎

The class interval is also a topological quotient: its coordinate \(\theta=\arccos(\operatorname{tr}(g)/2)\) is continuous. Continuous central functions correspond precisely to \(C([0,\pi])\).

## Polynomial representations and the complete list

Let \(P_m\) be the complex homogeneous polynomials of degree \(m\) in two variables. Use column variables \(Z=(z,w)^t\) and the action

\[
(\pi_m(g)p)(Z)=p(g^{-1}Z),\qquad m\geq0.
\tag{2.1}
\]

This is a representation: applying \(h\), then \(g\), substitutes \(h^{-1}g^{-1}Z=(gh)^{-1}Z\). It is continuous and has dimension \(m+1\). An invariant inner product is obtained by restricting polynomials to the unit sphere in \(\mathbb C^2\) and integrating \(p\bar q\). It is positive definite, since a homogeneous polynomial vanishing on that sphere vanishes everywhere. Unitary changes of variables preserve it.

The monomial \(z^{m-j}w^j\) has eigenvalue \(e^{i(2j-m)\theta}\) under \(t_\theta\). Hence its character is

\[
\chi_m(t_\theta)
=\sum_{j=0}^m e^{i(2j-m)\theta}
=\frac{\sin((m+1)\theta)}{\sin\theta}.
\tag{2.2}
\]

The quotient is interpreted continuously at the endpoints: its values are \(m+1\) at zero and \((-1)^m(m+1)\) at \(\pi\). Formula (2.1) fixes the individual eigenvalue signs; reversing the polynomial action would change them, although the total character here is unchanged.

**Theorem 2.3.** The representations \(\pi_m\), \(m=0,1,\ldots\), are irreducible, pairwise inequivalent, and exhaust all irreducible continuous unitary representations of \(SU(2)\).

**Proof.** Equations (1.3) and (2.2) give

\[
\langle\chi_m,\chi_n\rangle
=\frac2\pi\int_0^\pi
\sin((m+1)\theta)\sin((n+1)\theta)\,d\theta
=\delta_{mn}.
\tag{2.4}
\]

Indeed, twice the product of the sines is the difference of the cosines with frequencies \(m-n\) and \(m+n+2\). Every nonzero integral frequency has cosine integral zero on \([0,\pi]\); the constant frequency contributes \(\pi\). The character norm test in the preceding lesson proves irreducibility, and orthogonality proves inequivalence.

To prove exhaustion, \(\chi_0=1\), \(\chi_1=2\cos\theta\), and

\[
\chi_m-\chi_{m-2}=2\cos(m\theta)\qquad(m\geq2).
\tag{2.5}
\]

Thus their span contains every cosine polynomial. The identity \(\cos(m\theta)=T_m(\cos\theta)\), obtained inductively from the cosine addition rule, says that these span all polynomials in \(\cos\theta\): the degree-\(m\) polynomial \(T_m\) has nonzero leading coefficient. Since \(\cos\theta\) identifies \([0,\pi]\) with \([-1,1]\), Stone–Weierstrass makes this span uniformly dense in the continuous class functions. An additional irreducible character would be orthogonal to every \(\chi_m\), hence to every continuous class function, including itself. Its squared norm is one, a contradiction. ∎

For example, \(\chi_1=2\cos\theta\) and \(\chi_2=4\cos^2\theta-1\). The two-dimensional defining representation has character \(\chi_1\), so it is equivalent to our action on linear polynomials, which is its dual. Every \(\chi_m\) is real, so every \(\pi_m\) is equivalent to its dual.

## Which polynomial types descend to ordinary rotations

**Corollary 3.4.** The irreducible representations of \(SO(3)\) are \(\tau_\ell\), \(\ell=0,1,\ldots\), whose pullbacks are \(\pi_{2\ell}\). Their dimensions are \(2\ell+1\).

Indeed, pulling back along a surjection preserves irreducibility and equivalence. A representation of \(SU(2)\) descends exactly when \(-I\) acts trivially. Formula (2.1) gives \(\pi_m(-I)=(-1)^mI\), so exactly the even indices descend. On a rotation about the third axis by angle \(\varphi\), the weights of \(\tau_\ell\) are

\[
e^{ik\varphi},\qquad k=-\ell,-\ell+1,\ldots,\ell,
\tag{3.5}
\]

each once. Substitute \(\theta=\varphi/2\) in the weights of \(\pi_{2\ell}\).

## Scalar charge and the irreducibles of U(2)

In an irreducible representation of \(U(2)\), scalar matrices act as \(z^kI\), \(k\in\mathbb Z\), by Schur and the circle character classification imported in the first lesson. Its restriction to \(SU(2)\) is irreducible, because any invariant subspace is also invariant under those scalars and therefore under all \(U(2)\). Consequently every irreducible is

\[
\rho_{m,k}(zg)=z^k\pi_m(g),
\qquad m\geq0,\quad k\in\mathbb Z,\quad k\equiv m\pmod2.
\tag{6.3}
\]

The parity condition is exactly triviality on \((-1,-I)\). Conversely this condition makes (6.3) well defined; restriction to \(SU(2)\) proves irreducibility. The two restrictions recover \(m,k\), proving inequivalence. Its dimension is \(m+1\). The case \(m=0,k=2j\) is \(\det^j\); the defining two-dimensional representation is \(m=1,k=1\).

For example, the same three-dimensional \(SU(2)\) type \(\pi_2\) extends to \(U(2)\) with any even scalar charge \(k\). These extensions are inequivalent because scalar matrices distinguish their charges. Charge zero is realized by conjugation on the trace-zero endomorphisms of \(\mathbb C^2\): scalars act trivially, and restriction to \(SU(2)\) has character \(\chi_1^2-1=\chi_2\), by the tensor formula below. Thus the spatial three-dimensional type and the defining two-dimensional \(U(2)\) type require different central data, even though both come from polynomial representations of \(SU(2)\).

For \(SO(4)\), the two covering factors supply independent labels \((m,n)\). The diagonal kernel acts by \((-1)^{m+n}\), so only labels of even total parity descend. The complete product-representation argument and its dimensions are given in Exercise 3. Notice the difference from \(SO(3)\): neither label individually has to be even. The pair \((1,1)\) descends and has dimension four, whereas \((1,0)\) does not descend.

## Combining two polynomial measurements

**Theorem 2.6 (Clebsch–Gordan).** For \(m,n\geq0\),

\[
\pi_m\otimes\pi_n
\simeq\bigoplus_{k=0}^{\min(m,n)}\pi_{m+n-2k}.
\tag{2.7}
\]

**Proof.** Assume \(m\geq n\), and put \(Q_m(t)=\sum_{a=0}^m t^{m-2a}\). In \(Q_mQ_n\), the coefficient of \(t^{m+n-2r}\) counts pairs \(a+b=r\), with \(0\leq a\leq m\), \(0\leq b\leq n\). For \(0\leq r\leq m+n\), this count is

\[
\begin{cases}
r+1,&0\leq r\leq n,\\
n+1,&n\leq r\leq m,\\
m+n-r+1,&m\leq r\leq m+n.
\end{cases}
\tag{2.8}
\]

In \(\sum_{k=0}^n Q_{m+n-2k}\), the same power occurs once for each \(k\) with \(0\leq k\leq n\) and \(k\leq r\leq m+n-k\). Its count is exactly (2.8). All coefficients agree. Taking \(t=e^{i\theta}\) proves the character identity on every conjugacy class. Finite-dimensional characters determine representations, so it proves (2.7). ∎

In particular, \(\pi_1\otimes\pi_1=\pi_2\oplus\pi_0\). On the defining space \(V=\mathbb C^2\), the symmetric tensors give the three-dimensional summand, while \(\bigwedge^2V\) is the one-dimensional trivial representation because every matrix has determinant one.

The simplest tensor identity has a visible linear-algebra model. In \(V\otimes V\), with \(V=\mathbb C^2\), interchange of the two factors commutes with the group action. Its \(+1\) space has basis \(e_1\otimes e_1, e_1\otimes e_2+e_2\otimes e_1,e_2\otimes e_2\), and its \(-1\) space is spanned by \(e_1\otimes e_2-e_2\otimes e_1\). The latter transforms by determinant and is therefore trivial for \(SU(2)\). This gives the actual three-plus-one splitting underlying \(\pi_1\otimes\pi_1=\pi_2\oplus\pi_0\); the general character count identifies every higher tensor product.

## Harmonic polynomials give the whole two-sphere

Let \(\mathcal P_\ell\) be the complex homogeneous polynomials of degree \(\ell\) in real coordinates \(x,y,z\), let \(r^2=x^2+y^2+z^2\), and put

\[
\mathcal H_\ell=\ker\Delta_{\mathbb R^3}\cap\mathcal P_\ell,
\qquad
H_\ell=\{h|_{S^2}:h\in\mathcal H_\ell\}.
\tag{4.1}
\]

Use the rotation action \((R\cdot f)(v)=f(R^{-1}v)\). Rotations commute with the Euclidean Laplacian, so these spaces are invariant. Restriction is injective on a homogeneous degree: vanishing on the unit sphere implies vanishing at every nonzero point by scaling.

**Lemma 4.2 (harmonic decomposition).**

\[
\mathcal P_\ell
=\mathcal H_\ell\oplus r^2\mathcal P_{\ell-2}
=\bigoplus_{j=0}^{\lfloor\ell/2\rfloor}r^{2j}\mathcal H_{\ell-2j},
\qquad
\dim H_\ell=2\ell+1.
\tag{4.3}
\]

Spaces with negative degree are zero.

**Proof.** If \(h\) is homogeneous harmonic of degree \(a\), the product rule and Euler's identity \(\sum x_i\partial_i h=ah\) give

\[
\Delta(r^{2j}h)=2j(2a+2j+1)r^{2j-2}h,\qquad j\geq1.
\tag{4.4}
\]

To verify the coefficient, \(\Delta r^{2j}=2j(2j+1)r^{2j-2}\), and twice the gradient product contributes \(4ja\,r^{2j-2}h\).

Proceed by induction on \(\ell\). The degrees zero and one are harmonic. By the inductive decomposition of \(\mathcal P_{\ell-2}\), the map \(q\mapsto\Delta(r^2q)\) is diagonal on its summands \(r^{2j}\mathcal H_{\ell-2-2j}\), with the nonzero coefficients \(2(j+1)(2(\ell-2-2j)+2(j+1)+1)\). It is therefore an isomorphism of \(\mathcal P_{\ell-2}\). Given \(p\in\mathcal P_\ell\), choose the unique \(q\) with \(\Delta(r^2q)=\Delta p\). Then \(p-r^2q\) is harmonic. The same isomorphism shows that a harmonic polynomial in \(r^2\mathcal P_{\ell-2}\) is zero. This proves the first direct sum, and induction proves the second.

The number of degree-\(\ell\) monomials is \(\binom{\ell+2}{2}\). Hence

\[
\dim H_\ell=\binom{\ell+2}{2}-\binom{\ell}{2}=2\ell+1,
\tag{4.5}
\]

with the second term zero for \(\ell=0,1\). ∎

**Theorem 4.6 (spherical harmonics).**

\[
H_\ell\simeq\tau_\ell,\qquad
L^2(S^2)=\widehat{\bigoplus}_{\ell\geq0}H_\ell,\qquad
\Delta_{S^2}|_{H_\ell}=-\ell(\ell+1)I.
\tag{4.7}
\]

**Proof.** The nonzero polynomial \((x+iy)^\ell\) is harmonic, because its \(x\) and \(y\) second derivatives cancel and its \(z\) derivatives vanish. Under a third-axis rotation by \(\varphi\), it has weight \(e^{-i\ell\varphi}\) for our inverse-variable action. Decompose the finite-dimensional unitary space \(H_\ell\) into irreducibles \(\tau_a\). Some summand has that weight. By (3.5) its index satisfies \(a\geq\ell\), so its dimension is at least \(2\ell+1\). This is already the entire dimension (4.5). Therefore \(H_\ell\) is that single summand, with \(a=\ell\). The dimensions make the different \(H_\ell\) inequivalent.

The sphere inner product is rotation-invariant. Orthogonal projection from one invariant finite-dimensional subspace to another intertwines their actions; Schur's lemma makes it zero for these inequivalent types. Thus the \(H_\ell\) are mutually orthogonal.

Restrictions of polynomials form a conjugation-closed algebra containing constants and separating points of \(S^2\), so Stone–Weierstrass makes them uniformly dense in \(C(S^2)\). Decompose each homogeneous part by (4.3). On the sphere \(r^2=1\), so its restriction is a finite sum of harmonic restrictions. Continuous functions are \(L^2\)-dense for the round measure. Hence the orthogonal sum of the \(H_\ell\) is all \(L^2(S^2)\).

Finally the polar-coordinate identity

\[
\Delta_{\mathbb R^3}
=\partial_r^2+\frac2r\partial_r+\frac1{r^2}\Delta_{S^2}
\tag{4.8}
\]

applied to \(r^\ell Y(v)\) gives
\(0=r^{\ell-2}(\ell(\ell+1)Y+\Delta_{S^2}Y)\).
This proves the eigenvalue in (4.7). The coordinate identity is the differential-geometric prerequisite specified below. ∎

At degree one, \(H_1\) is spanned by \(x,y,z\) restricted to the sphere; its Laplacian eigenvalue is \(-2\). At degree two, a basis is

\[
xy,\quad xz,\quad yz,\quad x^2-y^2,\quad 2z^2-x^2-y^2.
\tag{4.9}
\]

Each has Laplacian zero in \(\mathbb R^3\), they are independent, and the dimension is five. Their spherical eigenvalue is \(-6\).

## Zonal functions and the central-section transform

The rotations fixing the north pole form \(SO(2)\). Formula (3.5) shows that its fixed subspace in \(H_\ell\) has dimension one. Its element taking value one at that pole is

\[
Y_\ell(v)=P_\ell(v_z),\qquad
P_\ell(t)=\frac1{2^\ell\ell!}\frac{d^\ell}{dt^\ell}(t^2-1)^\ell.
\tag{5.1}
\]

Here \(P_\ell\) is the Legendre polynomial. We verify this identification rather than infer it from the name. Expanding the derivative gives

\[
P_\ell(t)=2^{-\ell}
\sum_{j=0}^{\lfloor\ell/2\rfloor}
(-1)^j
\frac{(2\ell-2j)!}{j!(\ell-j)!(\ell-2j)!}\,t^{\ell-2j}.
\tag{5.2}
\]

The coefficients satisfy
\((k+2)(k+1)a_{k+2}+[\ell(\ell+1)-k(k+1)]a_k=0\),
so substitution proves

\[
(1-t^2)P_\ell''-2tP_\ell'+\ell(\ell+1)P_\ell=0.
\tag{5.3}
\]

Also \(P_\ell(1)=1\): in differentiating \((t-1)^\ell(t+1)^\ell\) \(\ell\) times at \(1\), only the term differentiating the first factor \(\ell\) times survives, with value \(\ell!2^\ell\). The expression \(r^\ell P_\ell(z/r)\) is a homogeneous polynomial by (5.2). For a function of \(t=v_z\), the spherical Laplacian is \((1-t^2)\partial_t^2-2t\partial_t\), obtained from the round metric in polar coordinates. Equations (4.8) and (5.3) make that polynomial harmonic. Its restriction is axis-invariant and has pole value one, proving (5.1).

Define the great-circle transform of a continuous function by

\[
(Ff)(n)=\int_{\substack{u\in S^2\\u\perp n}} f(u)\,ds(u),
\tag{5.4}
\]

where arc length on each unit circle has mass \(2\pi\). Local continuous choices of rotations carrying the north pole \(e_z\) to \(n\) show that \(Ff\) is continuous. One such choice away from \(n=-e_z\) is quaternion conjugation by
\((1+n_z+e_z\times n)/\sqrt{2(1+n_z)}\); equation (3.2) verifies its action, and its coefficients are continuous. Rotating this construction gives a choice near every \(n\). Invariance of arc length shows that \(F\) commutes with rotations.

This transform extends boundedly to \(L^2(S^2)\). Cauchy–Schwarz on each circle and integration in \(n\) give

\[
\|Ff\|_2^2
\leq2\pi\int_{S^2}\int_{u\perp n}|f(u)|^2\,ds(u)\,dn
=(2\pi)^2\|f\|_2^2.
\tag{5.5}
\]

For the last identity, the inner-circle incidence measure, integrated over uniformly distributed \(n\), gives a rotation-invariant measure in \(u\) of total mass \(2\pi\). Uniqueness of invariant probability measure on the sphere follows by averaging any continuous function over \(SO(3)\): transitivity makes its group average constant, so every invariant probability has the same integral. Thus the marginal is \(2\pi\,du\). Applying this first to continuous functions proves (5.5), and density gives the extension.

By the multiplicity-one decomposition (4.7) and Schur's lemma, \(F\) acts on \(H_\ell\) as a scalar. More explicitly, project \(F|_{H_\ell}\) onto each \(H_a\); all the projections with \(a\ne\ell\) are zero, and completeness leaves its image in \(H_\ell\). Evaluate the zonal function (5.1) at the north pole to find

\[
F|_{H_\ell}=2\pi P_\ell(0)I,\qquad
P_{2j}(0)=(-1)^j\frac{\binom{2j}{j}}{4^j},
\qquad P_{2j+1}(0)=0.
\tag{5.6}
\]

The values follow directly from (5.2). In particular every even-degree eigenvalue is nonzero.

**Theorem 5.7 (central sections determine an origin-symmetric body).** A compact convex body \(B\subset\mathbb R^3\) with nonempty interior and \(B=-B\) is uniquely determined by the areas of its sections by planes through the origin.

**Proof.** The origin is interior: if \(v\) has an interior ball in \(B\), its reflected ball does too, and convexity puts a ball about zero inside \(B\). Choose \(a,b>0\) with the radius-\(a\) ball contained in \(B\) and \(B\) contained in the radius-\(b\) ball. Its Minkowski functional \(p_B(x)=\inf\{s>0:x\in sB\}\) is positively homogeneous and subadditive by convexity. Symmetry makes it even. These facts give
\(|p_B(x)-p_B(y)|\leq p_B(x-y)\leq|x-y|/a\).
On the sphere it lies between \(1/b\) and \(1/a\). Therefore the radial function \(r_B(u)=1/p_B(u)\) is positive, continuous and even.

For completeness, subadditivity follows because \(x\in sB\) and \(y\in tB\) imply \(x+y\in(s+t)B\), by the convex combination with coefficients \(s/(s+t)\) and \(t/(s+t)\); take infima. Closedness of \(B\) makes \(B=\{x:p_B(x)\leq1\}\), so its ray in direction \(u\) ends exactly at \(r_B(u)u\).

Polar integration in the plane normal to \(n\) gives its section area

\[
A_B(n)=\frac12\int_{u\perp n}r_B(u)^2\,ds(u)
=\frac12F(r_B^2)(n).
\tag{5.8}
\]

If two bodies have equal areas, their continuous even difference \(f=r_{B_1}^2-r_{B_2}^2\) has \(Ff=0\). Antipodal reflection acts on \(H_\ell\) as \((-1)^\ell\), by homogeneity. Hence an even \(f\) has only even-degree harmonic components. Boundedness, equivariance and (5.6) make each such component of \(Ff\) the corresponding nonzero scalar times the component of \(f\). All components of \(f\) vanish, so \(f=0\) in \(L^2\), and continuity makes it zero everywhere. Positivity gives \(r_{B_1}=r_{B_2}\). These radial functions determine the bodies, proving equality. ∎

This proof uses injectivity on even functions. It does not claim a bounded inverse on all continuous even functions. In fact \(\binom{2j}{j}/4^j=\prod_{k=1}^j(1-1/(2k))\) tends to zero: its logarithm is at most \(-\sum_{k=1}^j1/(2k)\). Normalizing a nonzero even harmonic to supremum norm one makes the norm of its image tend to zero. Thus a bounded inverse on the range, for the supremum norm, is impossible. Origin symmetry is essential to the argument: the transform annihilates every odd function.

## Real and quaternionic forms of the same character

The character \(\chi_m\) of \(V_m=\operatorname{Sym}^m\mathbb C^2\) is real-valued for every \(m\). That fact alone does not say whether its matrices can be made real. The symmetric-power example in §32 of Etingof's freely accessible 2026 version distinguishes the two possibilities. We give the compact-group construction and a character test.

On \(\mathbb C^2\) put \(J(a,b)=(-\overline b,\overline a)\). Direct multiplication with the displayed \(SU(2)\) matrices shows that \(J\) commutes with the action, is antiunitary, and satisfies \(J^2=-I\). The tensor map \(J^{\otimes m}\) preserves the symmetric tensors, so it restricts to an antiunitary \(J_m\) on \(V_m\) with \(J_m^2=(-1)^mI\). The invariant bilinear form
\[
B_m(v,w)=\langle v,J_mw\rangle
\]
is nondegenerate. With our first-variable-linear inner product, antiunitarity and the square relation give \(B_m(w,v)=(-1)^m B_m(v,w)\). For even \(m\), the fixed vectors of \(J_m\) are a real form: every \(v\) decomposes as
\[
v=\frac{v+J_mv}{2}+i\frac{v-J_mv}{2i},
\]
with both displayed vectors fixed. For odd \(m\), the square \(-I\) gives a quaternionic structure; there is no invariant symmetric nondegenerate bilinear form. Indeed, Schur's lemma makes the space of invariant forms one-dimensional, and its existing form is alternating. An invariant real form would supply a symmetric form by averaging a real inner product, a contradiction.

The Frobenius–Schur character indicator detects exactly this sign:
\[
\int_{SU(2)}\chi_m(g^2)\,dg=(-1)^m.
\]
To prove it, let \(P=\int\pi_m(g)\otimes\pi_m(g)\,dg\), the orthogonal projection onto invariant tensors, and let \(\tau(v\otimes w)=w\otimes v\). In bases, \(\operatorname{tr}(\tau(A\otimes A))=\operatorname{tr}(A^2)\). Thus the integral is \(\operatorname{tr}(\tau P)\). Invariant tensors correspond to invariant bilinear forms on the dual. Schur's lemma gives a single line, and transposition on it has the symmetry sign of \(B_m\), namely \((-1)^m\). This proves the indicator. The vector representation \(m=2\) is real; the spinor \(m=1\) is quaternionic. Both have real characters.

## Exercises with complete solutions

**Exercise 1 — first characters (easy).** Check orthonormality of \(\chi_0,\chi_1,\chi_2\) using (1.3).

**Solution.** Their class functions are \(1,2\cos\theta,4\cos^2\theta-1\). Multiplication by \(\sin\theta\) gives \(\sin\theta,\sin2\theta,\sin3\theta\). For \(a,b\in\{1,2,3\}\), the product-to-sum formula gives integral zero when \(a\ne b\) and \(\pi/2\) when \(a=b\). Multiplying by \(2/\pi\) gives the \(3\times3\) identity Gram matrix. The endpoints cause no exception, since they have measure zero.

**Exercise 2 — tensor product multiplicities (medium).** Prove (2.7) from characters, and compute \(\pi_3\otimes\pi_2\).

**Solution.** Assume \(m\geq n\). In the product \((\sum_{a=0}^m t^{m-2a})(\sum_{b=0}^n t^{n-2b})\), a power indexed by \(r=a+b\) has multiplicity \(r+1\) up to \(n\), then \(n+1\) up to \(m\), then \(m+n-r+1\). In \(\sum_{k=0}^n\sum_{c=0}^{m+n-2k}t^{m+n-2k-2c}\), its multiplicity counts \(k\leq n,r,m+n-r\), giving those same three values. These finite Laurent polynomials coincide, including at \(t=\pm1\). They are the characters on diagonal matrices and therefore on all group elements. The preceding lesson's character test identifies the finite-dimensional representations, with each listed summand once. For \(m=3,n=2\), the result is \(\pi_5\oplus\pi_3\oplus\pi_1\), of total dimension \(6+4+2=12=4\cdot3\).

**Exercise 3 — all SO(4) irreducibles (medium).** Classify them using (6.2).

**Solution.** First an irreducible representation \(V\) of a product \(G_1\times G_2\) of compact groups is finite-dimensional. Decompose its restriction to \(G_1\) into isotypic components. The \(G_2\) action commutes with \(G_1\), so it preserves every such component. Irreducibility of the product leaves one type \(\sigma\). The canonical multiplicity construction of the first lesson identifies \(V\) with \(V_\sigma\otimes M\); every operator commuting with \(G_1\) is \(I\otimes A\), since Schur applied to its matrix of blocks gives scalar entries. Thus \(G_2\) acts on \(M\). This action must be irreducible, or a proper invariant \(N\subset M\) would give \(V_\sigma\otimes N\). Conversely, for irreducible \(\sigma,\eta\), the product action on \(V_\sigma\otimes V_\eta\) is irreducible: a commuting projection is \(I\otimes A\) by the first factor and scalar by the second, so it is zero or identity.

Apply this to the two \(SU(2)\) factors. The complete product list is \(\pi_m\boxtimes\pi_n\), with \(m,n\geq0\), and the ordered pair is determined by restriction and its multiplicity type. The element \((-I,-I)\) acts by \((-1)^{m+n}\). The representation descends to \(SO(4)\) precisely when \(m+n\) is even. Pullback along the quotient preserves irreducibility and equivalence, so this is the complete inequivalent list. Its dimension is \((m+1)(n+1)\).

**Exercise 4 — completeness on S² (hard).** Prove the dimension, irreducibility and density statements in (4.7).

**Solution.** Use (4.4) and induction to make \(q\mapsto\Delta(r^2q)\) an isomorphism on each degree \(\ell-2\): on the summand \(r^{2j}\mathcal H_a\) it multiplies by \(2(j+1)(2a+2j+3)\), a nonzero number. Subtract the unique \(r^2q\) having the same Laplacian as \(p\in\mathcal P_\ell\). This gives \(\mathcal P_\ell=\mathcal H_\ell\oplus r^2\mathcal P_{\ell-2}\). Its dimension difference is \(2\ell+1\), and restriction to the sphere is injective by homogeneity.

The harmonic vector \((x+iy)^\ell\) has third-axis weight \(-\ell\). Complete reducibility puts that weight into some \(\tau_a\); the explicit weight list (3.5) forces \(a\geq\ell\). Its dimension \(2a+1\) cannot exceed the total \(2\ell+1\), so \(a=\ell\) and there is only this summand. Different indices are inequivalent, hence orthogonal under the invariant sphere inner product. Polynomial restrictions are uniformly dense by Stone–Weierstrass. The iterated harmonic decomposition expresses each of them as a finite sum of \(H_a\), since \(r^2=1\) on the sphere. Continuous-function density now makes the closed orthogonal sum all of \(L^2(S^2)\). Finally (4.8) on \(r^\ell Y\) gives the eigenvalue \(-\ell(\ell+1)\), with multiplicity \(2\ell+1\).

## What this lesson does not prove

We import the compact-group decomposition, character criteria and Stone–Weierstrass consequences at the opening locators. The circle characters used in (6.3) are the exact classification imported in the first lesson from *Characters and the dual group*, Theorem 3.1 and Corollary 3.2, with angle coordinate \(x=\theta/(2\pi)\).

The finite matrix spectral theorem, elementary polar integration, Euler's identity for homogeneous polynomials and standard measure approximation are prerequisites. Here is a derivation of the polar Laplacian formula (4.8). In coordinates with volume density \(v=\sqrt{|g|}\), integration by parts against compactly supported test functions gives \(\operatorname{div}X=v^{-1}\partial_i(vX^i)\); the defining pairing of the gradient gives \((\operatorname{grad}f)^i=g^{ij}\partial_jf\). Combining them gives the coordinate rule \(\Delta f=|g|^{-1/2}\partial_i(|g|^{1/2}g^{ij}\partial_j f)\). On the unit two-sphere this is
\(\partial_\theta^2+\cot\theta\,\partial_\theta+\sin^{-2}\theta\,\partial_\varphi^2\)
because the sphere metric is \(d\theta^2+\sin^2\theta\,d\varphi^2\). Euclidean polar coordinates have metric \(dr^2+r^2g_{S^2}\) and volume density \(r^2\sin\theta\); the same rule gives \(\partial_r^2+2r^{-1}\partial_r+r^{-2}\Delta_{S^2}\), exactly (4.8). The coordinate singularities are avoided by computing in open charts and extending the smooth operator. All representation, harmonic-decomposition and convex-body conclusions were proved above.

The Lie-algebra classification of \(\mathfrak{sl}_2\) is a separate topic; we did not require it here. General homogeneous-space reciprocity will be developed later in this course.

## References

- C. Gruson and V. Serganova, *A Journey Through Representation Theory* (2018), Chapter 3, §3; Theorem 3.6 for the central-section application.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §32, in particular the symmetric powers of the defining SU(2) module. The real/quaternionic example motivates the construction above. The antiunitary maps and Haar character-indicator identity are proved here; no source expression is reproduced.

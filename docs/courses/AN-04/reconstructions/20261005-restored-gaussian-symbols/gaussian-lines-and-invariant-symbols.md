# Gaussian lines, densities and invariant symbols

An amplitude attached to a phase is not yet an invariant symbol. A change of phase can alter its Jacobian and its complex phase. The Jacobian belongs to a half density on the Lagrangian; the remaining phase belongs to a locally constant complex line bundle. We construct those two factors from linear Gaussian distributions, then prove the principal-symbol isomorphism for ordinary Lagrangian distributions.

The exact earlier programme proofs are:

- The restored [phase-space lesson](../20261005-restored-phase-space/phase-space-and-generating-families.md), including its symplectic basis and common-complement proofs; the restored [intrinsic-regularity lesson](../20261005-restored-intrinsic-regularity/intrinsic-lagrangian-regularity.md), including both prescribed-phase converses; and the restored [tangent-zoom lesson](../20261005-restored-tangent-zoom/tangent-zoom-and-quadratic-models.md), including singular Gaussian evaluation.
- [Quadratic stationary phase, Q1–Q6](../20261004-free-stationary-phase/quadratic-stationary-phase.md), [finite calculus and inverse maps](../20261004-free-stationary-phase/prerequisite-completions.md), and [convergent series, P13](../20261004-free-stationary-phase/exponential-prerequisite-completions.md). The [stationary lesson's Appendix A.4–A.6](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md) supplies compact bumps, quotient densities and fiber integration.
- [Completed measure and product integration, M0–M4](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), [coordinate and wavefront transport](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md), and [conic parametrices and full-symbol cutoffs, K0–K7](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md).
- [The geometric Maslov line, M0–M7](../20261004-free-intrinsic-graph/prerequisites/relative-maslov-line.md), [the global principal-symbol proof, PS0–PS6](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md), and [symbols on conic bundles](../20261004-free-canonical-composition/homogeneous-symbol-transport.md). PS5 proves the partition with supports locally finite over the base; PS6 proves global gluing and the exact kernel. Their phase-coordinate conventions are identified explicitly with the geometric Gaussian line in M6 and PS28–PS29.
- The restored oscillatory lesson supplies clean Fourier reduction with the normalization used here. The restored [phase-equivalence lesson](../20261005-restored-phase-equivalence/homogeneous-phase-equivalence-and-stabilization.md) supplies the exact homogeneous stabilization used in Exercise 9.3.

The [proof map](proof-map.json) binds each use to its exact source and complete dependency chain. The primary sources are the exact reprints of Hörmander III, corrected second printing (1994), Section 21.6 and Hörmander IV, corrected second printing (1994), Section 25.1. This lesson retains its independent exposition and exercises. The earlier programme alternatives and their reproducible figures remain available through the links above. Manifolds used for the global construction are Hausdorff and second countable, as in PS0.

Our symplectic form is \(\omega=\sum d\xi_j\wedge dx_j\). The distinguished vertical plane is \(\lambda_0=\{x=0\}\), and \(D=-i\partial\). The signature of a real symmetric form counts positive eigenvalues minus negative eigenvalues; zero eigenvalues count zero.

## 1. Charts and intersection strata of Lagrangian planes

Let \(S\) be a real symplectic vector space of dimension \(2n\). Its Lagrangian Grassmannian \(\mathcal L(S)\) consists of its \(n\)-dimensional Lagrangian subspaces. For a fixed Lagrangian \(\mu\), write

\[
\mathcal U_\mu=\{\lambda:\lambda\cap\mu=0\}.
\]

**Proposition 1.1.** The set \(\mathcal U_\mu\) is an affine space whose translation space is the space of symmetric maps \(\mu^*\to\mu\), equivalently \(\operatorname{Sym}^2\mu\). These charts make \(\mathcal L(S)\) a real analytic manifold of dimension \(n(n+1)/2\).

**Proof.** The symplectic pairing identifies \(S/\mu\) with \(\mu^*\). Projection restricts to an isomorphism on each transverse \(\lambda\), whose inverse is a section \(T:\mu^*\to S\). If \(T\) and \(T+R\) both have Lagrangian images, then \(R\) takes values in \(\mu\). Expanding \(\omega(Tv+Rv,Tw+Rw)=0\), and using isotropy of \(\mu\), says that the pairing of \(Rv\) with \(w\) is symmetric in \(v,w\). Conversely this symmetry makes the new image Lagrangian. It proves the affine assertion without choosing an origin section.

In coordinates with \(\mu\) vertical, a transverse plane is \(\xi=Cx\), \(C=C^T\), so the parameter count is \(n(n+1)/2\). If new symplectic coordinates are
\[
y=Px+Q\xi,\qquad \eta=Rx+T\xi,
\]
then on this plane \(y=(P+QC)x\). Wherever \(P+QC\) is invertible, its new symmetric graph matrix is
\[
(R+TC)(P+QC)^{-1}.
\tag{1.1}
\]
Thus the transitions are rational, with nonzero denominators on the chart overlaps. To check real analyticity directly at \(C_0\), set \(M_0=P+QC_0\) and \(Z=M_0^{-1}Q(C-C_0)\). For small matrix entries of \(C-C_0\), the inverse is the convergent matrix series \((P+QC)^{-1}=\sum_{j\geq0}(-Z)^jM_0^{-1}\). Each summand is a homogeneous polynomial of degree \(j\) in those entries. Choosing their absolute values sufficiently small bounds the sum of absolute monomial contributions by a geometric series. The finite geometric identity has remainder tending to zero, so this series is the actual inverse and is a convergent real power series. Multiplication by \(R+TC\) proves the claimed analytic transition. The charts cover every plane, because every Lagrangian has a complementary Lagrangian. ∎

For the topology, choose a Euclidean inner product on \(S\) and send a plane with basis-column matrix \(V\) to its orthogonal projection \(P_\lambda=V(V^TV)^{-1}V^T\). This is independent of the basis and determines the plane as its range. It varies continuously in every graph chart. Conversely, near a fixed rank-\(n\) projection, select \(n\) of its columns that are independent there; they remain independent nearby, and the graph coefficients are obtained continuously by an invertible minor. Thus the chart topology is exactly the subspace topology in the finite-dimensional space of matrices. It is Hausdorff and second countable by the rational-ball basis of that space.

**Proposition 1.2.** For fixed \(\mu\), the stratum \(\dim(\lambda\cap\mu)=k\) is a smooth submanifold of codimension \(k(k+1)/2\). In particular any countable collection of Lagrangian planes has a common Lagrangian complement.

**Proof.** Near a given \(\lambda\), choose a common Lagrangian complement to \(\lambda\) and \(\mu\). In its graph chart, the intersection is the kernel of the difference of two symmetric matrices. At the selected point that difference has rank \(n-k\). Choose a basis so its upper \((n-k)\)-square block remains invertible nearby, and write the difference as
\[
\begin{pmatrix}C&D\\D^T&E\end{pmatrix}.
\]
It has rank \(n-k\) exactly when \(E=D^TC^{-1}D\), by block elimination. These are \(k(k+1)/2\) independent smooth equations: the entries of the symmetric block \(E\) are free coordinates before imposing them. This proves the stratum assertion, including the endpoints \(k=0,n\).

Here is the measure argument with its countability made explicit. In a Euclidean chart of dimension \(d=n(n+1)/2\), a positive-codimension smooth submanifold is locally a smooth graph over \(\mathbb R^l\), with \(l<d\), by the inverse theorem. On a compact parameter box inside such a graph domain, all first derivatives are bounded. Divide that box into cubes of side at most \(\delta\). There are at most \(C\delta^{-l}\) cubes, and the graph above each has diameter at most \(C'\delta\), by the segment fundamental theorem. Its image lies in a \(d\)-dimensional cube of volume at most \(C''\delta^d\). The total covering volume tends to zero as \(\delta^{d-l}\). For \(l=0\) the graph is one point and the same conclusion follows from a single shrinking cube. The outer-measure construction M2 therefore makes each compact graph patch null.

Rational boxes exhaust each open parameter domain countably. The ambient Euclidean chart has a countable rational-ball basis, so its submanifold admits a countable subcover of these graph neighborhoods: for each basis member lying in one neighborhood choose one such neighborhood; these choices cover every point. Thus the whole stratum in that chart is null. Smooth positive chart densities are bounded on compact subcharts and preserve this conclusion. The nontransverse set is the finite union of the strata with \(k\geq1\). For a countable collection of fixed planes, the union of their nontransverse sets is consequently null in any one nonempty chart, and cannot contain a coordinate box of positive volume. A plane outside that union is a common complement. If \(n=0\), the unique zero plane is already such a complement. ∎

## 2. The Gaussian line determined by a plane

Choose a horizontal Lagrangian \(H\) complementary to \(\lambda_0\), so its adapted coordinates have \(H=\{\xi=0\}\). For an arbitrary Lagrangian \(\lambda\), let \(\mathcal I(\lambda,H)\) be the space of half-density distributions satisfying

\[
\ell(x,D)u=0
\quad\text{for every real linear form }\ell\text{ vanishing on }\lambda.
\tag{2.1}
\]

Changing dual bases in these adapted coordinates transforms the distributions as half densities and leaves the definition unchanged.

**Lemma 2.1.** This space is a complex line. If \(\lambda\) is transverse to \(H\), write \(\lambda=\{(B\xi,\xi)\}\), \(B=B^T\). Every element is

\[
u_B(x)=c(2\pi)^{-3n/4}
\int e^{i(x\cdot\xi-\xi^TB\xi/2)}\,d\xi\ |dx|^{1/2}.
\tag{2.2}
\]

The formula remains meaningful for singular \(B\).

**Proof.** First assume this transverse representation. The equations are \((x_j-(BD)_j)u=0\). Diagonalize \(B\) orthogonally, separating its nonzero eigenvalues from its kernel. The kernel equations \(z_j u=0\) force a simple layer \(\delta_0(z)\otimes v(y)\), with no normal derivatives. To verify this directly, fix \(\chi\in C_c^\infty\) in the \(z\) variables, equal to one near zero. For a compact test \(f\), put \(F(y,z)=f(y,z)-\chi(z)f(y,0)\). The segment fundamental theorem gives \(F(y,z)=\sum_j z_j\int_0^1\partial_{z_j}F(y,tz)\,dt\). Multiply the integrals by one compact smooth cutoff equal to one on \(\operatorname{supp}F\); this makes every resulting \(g_j\) compactly supported while retaining the equality \(F=\sum_jz_jg_j\). The equations \(z_j u=0\) kill these terms. The functional \(v(h)=u(h(y)\chi(z))\) has a finite-order bound on each compact \(y\)-support, hence is a distribution, and \(u(f)=v(f(\cdot,0))\). This proves the simple-layer assertion and excludes normal derivatives.

For each nonzero eigenvalue \(\beta_j\), the remaining equation is \((y_j-\beta_jD_j)v=0\). Multiplying by \(\exp(-i\sum y_j^2/(2\beta_j))\) turns it into \(\partial_{y_j}w=0\). A distribution with all first derivatives zero is constant. Here is the compact-primitive argument. In the \(k\) remaining variables choose compact smooth \(\rho_j\) of integral one. For a test \(f\), let \(M_jf\) be its integral in the first \(j\) variables, with \(M_0f=f\). Telescoping writes \(f-(\prod_j\rho_j)\int f\) as the sum, for \(j=1,\ldots,k\), of \((\prod_{i<j}\rho_i)(M_{j-1}f-\rho_jM_jf)\). Each bracket has integral zero in variable \(j\). Its primitive from \(-\infty\) to that variable is smooth and compactly supported, since it vanishes on both tails; all other variables also have common compact support. Thus each summand is a compact first derivative. The equations \(\partial_jw=0\) annihilate their sum, giving \(w(f)=c\int f\), with \(c=w(\prod_j\rho_j)\). For \(k=0\), the test space is already one-dimensional. Compact parameter integration and product integration justify all marginals and derivatives. This proves the constant assertion without assuming temperedness.

Every solution is consequently a constant Gaussian times a simple layer, hence is tempered. Fourier transformation is now justified without assuming temperedness at the outset. Its equations give
\[
i\partial_\xi\widehat u-B\xi\widehat u=0,
\qquad \widehat u=C e^{-i\xi^TB\xi/2}.
\]
Fourier inversion gives (2.2), after changing the constant to the displayed normalization. The exact Gaussian evaluation in the preceding lesson shows that it is nonzero for \(c\ne0\).

For a general \(\lambda\), choose another complement \(H'\) transverse to both \(\lambda_0\) and \(\lambda\), by the common-complement lemma. The chirp change in the next paragraph is an isomorphism between the two solution spaces, so the just-proved case establishes the assertion for the original \(H\). ∎

A new horizontal plane has the form \(H'=\{\xi=Ax\}\), \(A=A^T\). Its adapted coordinates are \(y=x\), \(\eta=\xi-Ax\). The exact identification is

\[
\mathcal I(\lambda,H)\longrightarrow\mathcal I(\lambda,H'),
\qquad u\longmapsto e^{-ix^TAx/2}u.
\tag{2.3}
\]

Indeed, \(D(e^{-ix^TAx/2}u)=e^{-ix^TAx/2}(D-Ax)u\), which transforms every equation (2.1) to the equation in the new coordinates. Changes (2.3) are transitive. Their equivalence classes form an intrinsic Gaussian line \(\mathcal I(\lambda)\), with \(\lambda_0\) still distinguished.

The annihilating system is maximal: if a nonzero solution also satisfies a real linear equation \(\ell(x,D)u=0\), commute it with all equations in (2.1). The linear Poisson bracket is the scalar \(i[\ell(x,D),\ell'(x,D)]\), so it must vanish for every \(\ell'\) annihilating \(\lambda\). Nondegeneracy of the symplectic form and \(\lambda^\omega=\lambda\) then force \(\ell\) itself to vanish on \(\lambda\). Thus the Gaussian line recovers its Lagrangian plane.

## 3. Separate the positive density from the phase

For \(\lambda\) transverse to \(H\), projection to \(\lambda_0\) along \(H\) identifies \(\xi\) as coordinates on \(\lambda\). Assign to (2.2) the translation-invariant half density

\[
d_H=c|d\xi|^{1/2}\quad\text{on }\lambda.
\tag{3.1}
\]

This assignment does not depend on the dual bases used. Explicitly, set \(x=Py\) and \(\xi=P^{-T}\eta\). Pullback of \(u\) as a half density multiplies its coefficient by \(|\det P|^{1/2}\), while changing the Fourier measure multiplies it by \(|\det P|^{-1}\). Thus \(c_y=c|\det P|^{-1/2}\). On the same plane, \(|d\eta|^{1/2}=|\det P|^{1/2}|d\xi|^{1/2}\), so \(c_y|d\eta|^{1/2}=c|d\xi|^{1/2}\).

Suppose both \(H\) and \(H'\) are transverse to \(\lambda\). With \(H'=\{\xi=Ax\}\) and \(\lambda=\{x=B\xi\}\), put

\[
K(A,B)=\begin{pmatrix}-A&I\\I&-B\end{pmatrix}.
\tag{3.2}
\]

The matrix is invertible precisely when \(I-AB\) is invertible, the condition \(\lambda\cap H'=0\). In the new coordinates, \(\eta=(I-AB)\xi\) on \(\lambda\), and its graph matrix is \(B'=B(I-AB)^{-1}\), which is symmetric.

**Proposition 3.1 (transition).** The two assigned half densities satisfy

\[
d_{H'}=e^{i\pi\operatorname{sgn}K(A,B)/4}d_H.
\tag{3.3}
\]

**Proof.** Apply the chirp (2.3), then Fourier transform in \(x\). The resulting Gaussian has quadratic Hessian \(K(A,B)\) in \((x,\xi)\), and its critical equations give \(x=B'\eta\). The exact real Gaussian formula gives its new normalized coefficient
\[
c'=c\,e^{i\pi\operatorname{sgn}K/4}|\det K|^{-1/2}.
\]
All powers of \(2\pi\) cancel: the initial integral has coefficient \((2\pi)^{-3n/4}\), the \(2n\)-variable Gaussian contributes \((2\pi)^n\), and conversion of the Fourier transform to the coefficient in (2.2) contributes \((2\pi)^{-n/4}\).

Block elimination, first for invertible \(B\) and then by polynomial continuation, gives
\[
\det K=(-1)^n\det(I-AB).
\tag{3.4}
\]
The density change is \(|d\eta|^{1/2}=|\det(I-AB)|^{1/2}|d\xi|^{1/2}\). It cancels the positive determinant in \(c'\), leaving (3.3). ∎

Since an invertible \(2n\)-square symmetric matrix has even signature, write

\[
\sigma(\lambda_0,\lambda;H',H)
=\tfrac12\operatorname{sgn}K(A,B)\in\mathbb Z.
\tag{3.5}
\]

The phase in (3.3) is \(i^\sigma\). The integer is symplectically invariant: adapted dual basis changes give congruent matrices. It is locally constant wherever all four transversality requirements hold.

**Lemma 3.2 (integer cocycle).** If \(H,H',H''\) are complements of \(\lambda_0\) transverse to \(\lambda\), then
\[
\sigma(\lambda_0,\lambda;H'',H)
=\sigma(\lambda_0,\lambda;H'',H')
+\sigma(\lambda_0,\lambda;H',H).
\tag{3.6}
\]
Reversing the last pair changes the sign. Also, whenever its four arguments satisfy the cross-transversality conditions,
\[
\sigma(\lambda_0,\lambda;H',H)
=-\sigma(H,H';\lambda,\lambda_0).
\tag{3.7}
\]

**Proof.** Write \(H''=\{\xi=A'x\}\). Initially assume \(B\) invertible. Completing squares in (3.2) gives
\[
\operatorname{sgn}K(A,B)=\operatorname{sgn}(B^{-1}-A)-\operatorname{sgn}B.
\]
The intermediate graph satisfies \((B')^{-1}=B^{-1}-A\), and the new shear from \(H'\) to \(H''\) is \(A'-A\). Thus twice the right side of (3.6) is
\[
\begin{aligned}
&\operatorname{sgn}(B^{-1}-A')-\operatorname{sgn}B'\\
&\qquad+\operatorname{sgn}(B^{-1}-A)-\operatorname{sgn}B
=\operatorname{sgn}(B^{-1}-A')-\operatorname{sgn}B,
\end{aligned}
\]
because a real symmetric invertible matrix and its inverse have the same signature. This is the left side. Small symmetric perturbations of \(B\) make it invertible while keeping every specified transverse intersection transverse. All invertible \(K\)'s retain their signatures under such perturbations, so the identity holds also for singular \(B\). Taking \(H''=H\), whose zero shear gives signature zero, proves reversal.

For (3.7), use the symplectic coordinates \(y=-\xi\), \(\eta=x\). The new distinguished vertical plane is the old \(H\), the variable plane is the old \(H'\), and the new reference planes are the old \(\lambda\) and \(\lambda_0\). Its matrix is \(\begin{pmatrix}B&I\\I&A\end{pmatrix}\). This is congruent to \(-K(A,B)\), by a block sign change followed by block interchange. Its signature is therefore the negative of the original signature. ∎

## 4. The Maslov line and its bundle form

Use the open sets \(\mathcal U_H\) for complements \(H\) of \(\lambda_0\). They cover \(\mathcal L(S)\), again by the common-complement lemma. On their overlaps, define the transition of a coefficient by

\[
c_{H'}=i^{\sigma(\lambda_0,\lambda;H',H)}c_H.
\tag{4.1}
\]

Equation (3.6) is the exact cocycle identity; hence these transitions define a complex line bundle \(M\), the Maslov line relative to \(\lambda_0\). Its transitions are locally constant fourth roots of unity. Together with the positive half-density transitions on \(\lambda\), (3.3) identifies

\[
\mathcal I(\lambda)\simeq M_\lambda\otimes\Omega^{1/2}(\lambda).
\tag{4.2}
\]

For a symplectic vector bundle with a distinguished Lagrangian subbundle, perform the same construction in local symplectic frames adapted to that subbundle. Such frames exist by smoothly choosing a basis and its symplectic dual, then making the complementary basis isotropic as in the earlier basis-extension proof. The construction agrees on overlapping frames because the integer in (3.5) is symplectically invariant. It therefore defines the Maslov line on its bundle of Lagrangian planes.

For a conic Lagrangian \(\Lambda\subset T^*X\setminus0\), use the symplectic bundle \(T(T^*X)|_\Lambda\), with its distinguished vertical tangents and its section of tangent planes \(T\Lambda\). Pulling back the preceding line gives \(M_\Lambda\). This specifies its geometric meaning, independently of phase variables.

## 5. Quadratic phases and the signature difference

Let \(Q(x,\theta)\) be a real quadratic form on \(\mathbb R^n\times\mathbb R^N\). Assume its phase-critical equations \(Q_\theta=0\) have independent differentials; equivalently the radical of its full Hessian contains no nonzero vector \((0,\theta)\). Its critical space \(C\) maps bijectively to the Lagrangian plane
\[
\lambda=\{(x,Q_x):Q_\theta=0\}.
\]
Indeed \(C\) has dimension \(n\), because its \(N\) defining linear equations are independent. If \((x,Q_x)=0\) on \(C\), then \(x=0\) and both components of the full Hessian applied to \((0,\theta)\) vanish. The phase nondegeneracy condition forces \(\theta=0\), proving injectivity. For two vectors of \(C\), the symplectic pairing of their images is zero: symmetry of the full Hessian equates the two full bilinear pairings, and their phase-gradient terms vanish on \(C\). The image is therefore isotropic of dimension \(n\), hence Lagrangian. This direct linear proof also covers an empty phase-variable block.

The integral
\[
u_Q=a(2\pi)^{-(n+2N)/4}\int e^{iQ(x,\theta)}\,d\theta\ |dx|^{1/2}
\tag{5.1}
\]
is an element of the Gaussian line \(\mathcal I(\lambda,H)\), with \(H\) horizontal. To define it concretely, split off the nondegenerate part of \(Q_{\theta\theta}\) and evaluate that Gaussian by Fresnel inversion. The remaining phase variables occur linearly and produce a delta layer in independent base constraints. This yields a tempered Gaussian simple layer. Moreover, if \(\ell\) vanishes on \(\lambda\), the linear form \(\ell(x,Q_x)\) vanishes on \(C\), and is therefore a constant linear combination of the independent \(Q_\theta\)'s. Integrating their derivatives proves (2.1).

Define a positive density \(d_C\) by the ambient delta density \(\delta(Q_\theta)|dx\,d\theta|\). Explicitly, if \(s\) are coordinates on \(C\), extended linearly off it,
\[
d_C=\left|\det\frac{D(s,Q_\theta)}{D(x,\theta)}\right|^{-1}|ds|.
\tag{5.2}
\]
This is independent of \(s\): ordinary change of variables supplies its density transformation law.

When \(\lambda\) is transverse to the horizontal plane, take \(s=Q_x=\xi\). The full Hessian \(G=Q''\) is then invertible. Fourier evaluation of (5.1) gives its normalized coefficient
\[
c=a e^{i\pi\operatorname{sgn}G/4}|\det G|^{-1/2},
\qquad
d_H=a e^{i\pi\operatorname{sgn}G/4}d_C^{1/2}.
\tag{5.3}
\]
The same cancellation of Gaussian powers explains the normalization in (5.1).

**Lemma 5.1.** If two nondegenerate quadratic phases \(Q,\widetilde Q\) parametrize the same \(\lambda\), then
\[
\operatorname{sgn}Q-\operatorname{sgn}\widetilde Q
=\operatorname{sgn}Q_{\theta\theta}
-\operatorname{sgn}\widetilde Q_{\widetilde\theta\widetilde\theta}.
\tag{5.4}
\]

**Proof.** Complete squares in the nonzero eigenspace of \(Q_{\theta\theta}\). After an invertible linear change, \(Q\) is the sum of that pure nondegenerate quadratic form and
\[
Q_0(x,\theta')=q(x)+x\cdot T\theta',
\]
where \(T\) is injective: otherwise a nonzero pure phase direction would lie in the full radical. Its critical equations say \(T^Tx=0\). Put \(V=\ker T^T\). The corresponding Lagrangian is \(\{(x,q'(x)+T\theta'):x\in V\}\); hence both \(V\), its annihilator \(\operatorname{ran}T\), and the restriction \(q|_V=\xi\cdot x/2\) are determined by \(\lambda\).

Choose base variables \((x',x'')\) with \(V=\{x'=0\}\), and change the remaining phase basis so the cross term is \(x'\cdot\theta'\). A linear shift of \(\theta'\) absorbs every term of \(q\) containing \(x'\). Thus \(Q_0\) is congruent to \(x'\cdot\theta'+q(0,x'')\). The cross block has equal positive and negative eigenvalue counts and contributes zero signature. Therefore
\[
\operatorname{sgn}Q-\operatorname{sgn}Q_{\theta\theta}
=\operatorname{sgn}(q|_V),
\]
which only depends on \(\lambda\). Applying this to both phases proves (5.4), including singular full Hessians. ∎

If (5.1) and its tilde version represent the same element, it follows that
\[
\widetilde a\,d_{\widetilde C}^{1/2}
=e^{i\pi(\operatorname{sgn}Q_{\theta\theta}
-\operatorname{sgn}\widetilde Q_{\widetilde\theta\widetilde\theta})/4}
a\,d_C^{1/2}.
\tag{5.5}
\]
For a plane transverse to the horizontal reference this follows from (5.3) and (5.4). For any other plane, change to a common horizontal complement transverse to it. The change subtracts a base quadratic form from both phases, leaves their phase-variable Hessians and critical densities unchanged, and makes both full Hessians invertible. The preceding argument then proves (5.5) in general.

This gives phase trivializations of the same Maslov line. If the two phase-variable counts differ, their transition can be an eighth root of unity. With a fixed count, the signature difference is even whenever computed from the invertible full Hessians, so it is a fourth root. The geometric bundle in Section 4 has structure group consisting of fourth roots; allowing other phase counts changes local frame choices, rather than that geometric construction.

## 6. Symbols on a conic manifold carry density degree

For a conic manifold \(V\) with dilation \(M_t\), an ordinary scalar symbol of order \(q\) is a smooth function for which \(t^{-q}M_t^*a\) is bounded in every \(C^k\) seminorm on each compact set, \(t\geq1\). This is the usual ordinary symbol condition in homogeneous coordinates.

The same definition applies to sections with a specified dilation action. If a positive half-density frame \(\omega\) is homogeneous of degree \(\mu\), then
\[
a=\omega b\in S^q(V;\Omega^{1/2})
\quad\Longleftrightarrow\quad b\in S^{q-\mu}(V).
\tag{6.1}
\]
Indeed \(M_t^*\omega=t^\mu\omega\); substitution in the definition proves both implications with all derivatives. Such frames can be chosen locally on a dilation slice and extended by the requested homogeneity. The Maslov frames are constant along dilation, and the lifted bundle \(\pi^*E\) has unchanged base point.

In frequency coordinates on \(\Lambda\), the frame \(|d\xi|^{1/2}\) has degree \(n/2\). Thus \(b\in S^{m-n/4}\) produces
\[
b|d\xi|^{1/2}\in S^{m+n/4}(\Lambda;\Omega^{1/2}).
\tag{6.2}
\]
The \(n/4\) is a consequence of density degree and is not interchangeable with \(n/2\).

## 7. The invariant principal-symbol isomorphism

Let \(E\to X\) be a smooth finite-rank complex vector bundle. Use the closed conic Lagrangian and intrinsic global class from the preceding lesson; the assertions also hold microlocally on an open cotangent cone, with all supports interior to that cone. Write \(\widetilde E=\pi^*E|_\Lambda\) and \(\nu=m+n/4\).

**Theorem 7.1.** There is a canonical isomorphism
\[
\frac{I^m(X,\Lambda;\Omega_X^{1/2}\otimes E)}
{I^{m-1}(X,\Lambda;\Omega_X^{1/2}\otimes E)}
\ \xrightarrow{\ \sigma\ }\ 
\frac{S^\nu(\Lambda;M_\Lambda\otimes\Omega_\Lambda^{1/2}\otimes\widetilde E)}
{S^{\nu-1}(\Lambda;M_\Lambda\otimes\Omega_\Lambda^{1/2}\otimes\widetilde E)}.
\tag{7.1}
\]
In a base chart making \(\Lambda\) a frequency graph, its representative is
\[
\sigma(u)=b(\xi)|d\xi|^{1/2},
\qquad b=(2\pi)^{-n/4}e^{iH}\widehat u,
\tag{7.2}
\]
in the Maslov frame determined by that chart's horizontal tangent planes and a local frame of \(E\).

**Proof of well-definedness.** Choose a compact proper microlocal cutoff whose full symbol is one modulo \(S^{-\infty}\) on a smaller cone about the point, with microsupport inside the graph chart. K7 and PS3 construct such a cutoff. Its output \(u_1\) differs from \(u\) by a distribution \(u_2\) regular on that smaller cone; apply (7.2) to \(u_1\). Two such decompositions have a wavefront-regular difference there. Their compact Fourier transforms, and all fixed frequency derivatives, are rapidly decreasing there. Thus (7.2) is independent of that decomposition even modulo \(S^{-\infty}\).

For a nondegenerate phase representation with amplitude \(a\), Fourier reduction gives
\[
b|d\xi|^{1/2}
=e^{i\pi\operatorname{sgn}G/4}a|_{C_\phi}d_{C_\phi}^{1/2}
\quad\bmod S^{\nu-1},
\tag{7.3}
\]
where \(d_{C_\phi}=\delta(\phi_\theta)|dx\,d\theta|\), interpreted by the Jacobian formula (5.2). The square root of that density has degree \(N/2\); with the amplitude order \(m+(n-2N)/4\), its total degree is \(\nu\).

The linearized quadratic phase at a critical point parametrizes \(T_\gamma\Lambda\). Its critical density is exactly the value of \(d_{C_\phi}\) there, and its full Hessian is \(G\). Formula (5.3) therefore identifies (7.3) with the element of the geometric Gaussian line, including its Maslov frame, rather than defining a separate transition convention.

For a base change \(x=\kappa(y)\), put \(J(y)=|\det D\kappa(y)|\) and \(\widetilde\phi(y,\theta)=\phi(\kappa(y),\theta)\). The amplitude becomes \(\widetilde a=J^{1/2}a\circ(\kappa,\mathrm{id})\). Since \(\widetilde\phi_\theta=\phi_\theta\circ(\kappa,\mathrm{id})\), pullback of the old ambient delta density is \(J\,d_{C_{\widetilde\phi}}\). Thus pullback of \(a d_{C_\phi}^{1/2}\) is exactly \(\widetilde a d_{C_{\widetilde\phi}}^{1/2}\).

There is also a change of horizontal reference tangent plane. At the critical point write \(P=D\kappa\), \(\xi=\phi_x\), and \(C=\sum_j\xi_jD^2\kappa_j\). Differentiating \(\eta=P^T\xi\) gives
\[
\delta x=P\delta y,\qquad
\delta\eta=P^T\delta\xi+C\delta y.
\tag{7.3a}
\]
The Hessian of \(\widetilde\phi-y\cdot\eta\) is the congruence of \(G\) by \(\operatorname{diag}(P,I)\), plus \(C\) in its base block. Accordingly its quadratic Gaussian model is the linearly pulled-back old model multiplied by \(e^{iy^TCy/2}\). After the linear basis change, the new horizontal reference has old frequency coordinate \(-Cy\); this is exactly (2.3) with \(A=-C\). Its coefficient phase is therefore (3.3), with the positive density change already accounted for. This proves that (7.3) patches in \(M_\Lambda\otimes\Omega_\Lambda^{1/2}\). If either original horizontal plane is not transverse to the tangent Lagrangian, insert a common transverse complement to compute the same identification; transitivity (3.6) removes that auxiliary choice.

A change of frame of \(E\) is multiplication by a smooth matrix \(g(x)\). Fourier reduction replaces the leading coefficient by \(g(H'(\xi))b(\xi)\), with a one-lower-order remainder. This is exactly the lifted bundle transition. These observations prove global well-definedness modulo \(S^{\nu-1}\).

**Kernel and surjectivity.** In a graph chart the intrinsic criterion says that (7.2) has order \(\nu-1\) precisely when \(u\) has order \(m-1\). Elliptic localization and a finite cosphere cover give this conclusion at every compact base set; the kernel is exactly the displayed denominator.

For surjectivity, first take a symbol section supported inside a compactly generated graph cone. Its local scalar coefficient is a symbol of order \(\nu-n/2=m-n/4\). The normalized inverse phase integral (1.2) of the previous lesson, multiplied by a base cutoff equal to one near the graph's base image, has that coefficient modulo one lower order. Fourier reduction proves the last assertion, and the intrinsic converse puts the distribution in \(I^m\).

For a general section, use the explicit construction in PS5: a precompact base exhaustion, a locally finite base partition, a homogeneous positive frequency norm, finite phase charts above each compact base support, and their degree-zero partition. This gives a locally finite cover of the cosphere of \(\Lambda\) by the required chart cones. Take the cover in relatively compact base/direction boxes, with closures still inside their graph domains, locally finite in the ambient cosphere. Over a compact base set its cosphere is compact, so only finitely many boxes meet it. Construct a local distribution for each symbol piece, with its compact base support in the corresponding base box. Their sum is locally finite as a distribution and has the prescribed symbol class by (7.3) and the transition laws. This proves surjectivity and (7.1). ∎

For two nondegenerate representations of the same \(u\) in fixed base coordinates, the explicit consequence is
\[
\widetilde a\,d_{C_{\widetilde\phi}}^{1/2}
-e^{i\pi(\operatorname{sgn}\phi_{\theta\theta}
-\operatorname{sgn}\widetilde\phi_{\widetilde\theta\widetilde\theta})/4}
a\,d_{C_\phi}^{1/2}\in S^{\nu-1}.
\tag{7.4}
\]
The Hessian signature difference is locally constant, even if either phase-variable Hessian changes rank. One may compute it from the two invertible full Hessians after choosing a common graph chart, by Lemma 5.1; their signatures are locally constant.

For a clean phase of excess \(e\), split the phase variables so \(\theta''\) parametrizes its local compact fiber \(C_\xi\), and let \(G'\) be the normal Hessian used in clean Fourier reduction. Then the representative in that same graph Maslov frame is
\[
\sigma(u)=|d\xi|^{1/2}
\int_{C_\xi}
e^{i\pi\operatorname{sgn}G'/4}
\frac{a(x,\theta)}{|\det G'|^{1/2}}\,d\theta''
\quad\bmod S^{\nu-1}.
\tag{7.5}
\]
This follows from the proved clean reduction and the normalized coefficient in (7.2); no \(2\pi\) factor remains. Here the clean oscillatory integral uses the prefactor \((2\pi)^{-(n+2N-2e)/4}\) from the restored intrinsic lesson, equation (4.2). Its stated conversion to the earlier companion's fixed prefactor must be included when comparing amplitude formulas. The normal-density change proved in clean stationary phase makes the expression independent of the chosen fiber/normal split. Its order is \(\nu\): the scalar amplitude contributes \(m+(n-2N-2e)/4\), the determinant contributes \(-(n-N+e)/2\), the fiber measure contributes \(e\), and \(|d\xi|^{1/2}\) contributes \(n/2\). Adding them gives \(m+n/4\). Compact fiber support is part of this local statement; a global fiber integral requires its own properness hypothesis.

## 8. Conjugation reflects the covector and the Maslov phase

Let \(\iota(x,\xi)=(x,-\xi)\), and write \(\overline\Lambda=\iota\Lambda\). If \(j:E\to F\) is any smooth antilinear bundle map, then
\[
u\in I^m(X,\Lambda;\Omega_X^{1/2}\otimes E)
\quad\Longrightarrow\quad
ju\in I^m(X,\overline\Lambda;\Omega_X^{1/2}\otimes F).
\tag{8.1}
\]
Its symbol is obtained by applying \(j\) to the vector coefficient, conjugating the Maslov factor and transporting by \(\iota\). No invertibility or equality of bundle ranks is required.

**Proof.** In a phase representation, conjugation replaces \(\phi\) by \(-\phi\) and \(a\) by \(\overline a\). The critical set and positive critical density are unchanged, while the critical covector and full Hessian change sign. Formula (7.3) therefore conjugates the Fresnel factor and reflects the covector. A smooth antilinear map in local frames is a smooth matrix times complex conjugation; its matrix multiplication contributes its value at the critical base point, as in the bundle transition proof, and preserves the amplitude order. This proves (8.1) locally and hence globally.

For the bundle identification, \(\iota\) reverses the symplectic form. In the matrices of Section 3 it sends \((A,B)\) to \((-A,-B)\). The matrix \(K(-A,-B)\) is congruent to \(-K(A,B)\), so every transition \(i^\sigma\) is conjugated to \(i^{-\sigma}\). Thus transport by \(\iota\) identifies the conjugated Maslov line with \(M_{\overline\Lambda}\). Positive densities transform by their ordinary absolute Jacobians. This verifies the stated global symbol law. ∎

## 9. Exercises with complete solutions

**Exercise 9.1 (an intersection stratum; introductory).** In a symplectic space of dimension six, determine the codimensions and dimensions of the strata \(\dim(\lambda\cap\mu)=k\), \(k=0,1,2,3\).

**Solution.** The Grassmannian has dimension \(3\cdot4/2=6\). The codimensions are \(0,1,3,6\), so the dimensions are \(6,5,3,0\). The last stratum is the single plane \(\lambda=\mu\); the generic nontransverse stratum is a hypersurface, while intersection dimension at least two has codimension at least three.

**Exercise 9.2 (one-dimensional transition; intermediate).** Take \(n=1\), \(H'=\{\xi=x\}\), and \(\lambda=\{x=b\xi\}\), \(b\ne1\). Compute the Maslov transition from the horizontal reference to \(H'\), and verify the positive density cancellation.

**Solution.** Here \(K=\begin{pmatrix}-1&1\\1&-b\end{pmatrix}\), with determinant \(b-1\). If \(b<1\), the determinant is negative, so the eigenvalues have opposite signs and the signature is zero. If \(b>1\), both are negative, since the determinant is positive and the trace is negative; the signature is \(-2\). Hence the transition is one for \(b<1\) and \(-i\) for \(b>1\). The new frequency is \(\eta=(1-b)\xi\); its half-density Jacobian \(|1-b|^{1/2}\) cancels the coefficient factor \(|\det K|^{-1/2}\), leaving exactly those unit phases.

**Exercise 9.3 (stabilization; intermediate).** Add \(k\) quadratic phase variables with invertible block \(D\). What transition does (7.4) require between the original and stabilized critical amplitudes?

**Solution.** The stabilized phase-variable signature is the old signature plus \(\operatorname{sgn}D\). Thus its critical amplitude half density must be \(e^{-i\pi\operatorname{sgn}D/4}\) times the old one, modulo the one-lower-order symbol class. The positive factor from the new block belongs to the critical-density Jacobian, rather than the Maslov phase. In the homogeneous stabilization of the earlier lesson the block is \(D/r\), with \(r>0\), so its signature is unchanged and the required factor is exactly the one there. For one positive variable the phase is \(e^{-i\pi/4}\), illustrating the eighth-root phase frame when variable counts differ.

**Exercise 9.4 (density order; intermediate).** In a graph chart of dimension \(n\), let the normalized coefficient have order \(r\). Compute the order of its symbol half density and the order of the resulting distribution. Apply this to a point mass with a vector coefficient.

**Solution.** The half-density symbol has order \(r+n/2\), while the distribution has order \(m=r+n/4\). These satisfy \(r+n/2=m+n/4\). For \(u=v\delta_0\), the normalized coefficient is \((2\pi)^{-n/4}v\), of order zero, so \(m=n/4\) and its symbol half density has order \(n/2\). Its vector lies in the lifted fiber \(E_0\), and its Maslov frame is the chosen horizontal one. No order shift is introduced by the finite vector rank.

**Exercise 9.5 (a noninvertible antilinear map; advanced).** Let \(E\) have rank two, \(F\) rank one, and \(j(z_1,z_2)=\overline{z_1}\). For a phase amplitude with vector \((a_1,a_2)\), describe the symbol of \(ju\) and explain what happens if its first component has one lower symbol order.

**Solution.** The reflected Lagrangian is \(\iota\Lambda\). Its scalar critical coefficient is \(\overline{a_1}\), its Maslov phase is the conjugate of the original phase, and its positive critical density is transported by \(\iota\). The second vector component is discarded. If the first component has one lower order, the principal symbol of \(ju\) vanishes even when that of \(u\) is nonzero; Theorem 7.1 then places \(ju\) in \(I^{m-1}\). This is compatible with (8.1), which asserts membership and the symbol law, without asserting preservation of a nonzero principal symbol under a noninjective map.

## References

- [Hörmander III, §21.6] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, Springer, 1994, §21.6.
- [Hörmander IV, §25.1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, corrected second printing, Springer, 1994, §25.1.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Self-checked by the writing AI. Original text: public domain (CC0).*

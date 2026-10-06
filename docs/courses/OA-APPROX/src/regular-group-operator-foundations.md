# Regular group operator foundations

*Original text: public domain (CC0 1.0).*

This lesson constructs the bounded operators and group traces needed for the subgroup-orbit and affine MASA arguments. Compression to a subgroup supplies its expectation. Positive inverses recover kernel projections, while explicit matrix entries compute the regular commutants. The final sections prove normal group-trace uniqueness and the intrinsic finite or countably infinite matrix size used for MASA multiplicity.

H00–H04 begin with square-summable coordinates. Their C*-algebra calculus input is the complete F03–F08 proof chain in Infinite tensor products. G00–G05 then construct the group algebra and subgroup maps. T04a–T04c prove polar decomposition, trace bounds for projection joins and continuity of an order-normal functional along bounded trace-square-null sequences. T04 applies these proofs to preserve the group trace under an abstract isomorphism. The source comparisons at the end of G05 identify the freely readable group-operator arguments.

<a id="h00"></a>
## H00. Square-summable coordinates and bounded operators

Our scalar boundary is the complete real ordered field and its complex field. For any set \(I\), let \(\ell^2(I)\) consist of the functions \(\xi\) with \(\sum_{i\in I}|\xi(i)|^2<\infty\), where a sum of nonnegative terms is the supremum of its finite partial sums. Every such vector has at most countable support: for each positive integer \(m\), only finitely many coordinates can have modulus at least \(1/m\), and the union of those finite sets contains every nonzero coordinate. The inner product is \(\langle\xi,\eta\rangle=\sum_i\overline{\xi(i)}\eta(i)\), linear in the second variable. Finite-dimensional Cauchy–Schwarz follows by minimizing \(\|\xi-z\eta\|^2\) over \(z\in\mathbb C\); if \(\eta=0\) its assertion is immediate. Taking finite partial sums proves absolute convergence of the displayed inner product and Cauchy–Schwarz for \(\ell^2(I)\).

This space is complete. If \((\xi_j)\) is norm Cauchy, each coordinate is Cauchy and has a limit \(\xi(i)\). A uniform bound on \(\|\xi_j\|\) bounds every finite sum of squares of these limits, so \(\xi\in\ell^2(I)\). For a chosen \(\varepsilon>0\), sufficiently late \(j,k\) have \(\|\xi_j-\xi_k\|<\varepsilon\). Taking \(k\) to infinity in each finite-coordinate sum and then taking the supremum gives \(\|\xi_j-\xi\|\le\varepsilon\). Finite-coordinate truncations converge in norm; the coordinate vectors are therefore an orthonormal basis. A bijection between two coordinate sets induces a unitary by carrying one basis onto the other. The Hilbert tensor product of two such spaces is \(\ell^2(I\times J)\): finite elementary tensors have the product inner product, and their coordinate tensors span a dense subspace of that complete space.

A bounded linear functional \(f\) on \(\ell^2(I)\) has the form \(f(\eta)=\langle\xi,\eta\rangle\). Indeed set \(\overline{\xi(i)}=f(\delta_i)\). Testing finite linear combinations with coefficients \(\xi(i)\) gives \(\sum_{i\in F}|\xi(i)|^2\le\|f\|^2\) for every finite \(F\), by dividing by the square root of that sum when it is nonzero. Thus \(\xi\in\ell^2(I)\), and agreement on finite-coordinate vectors extends by continuity. This also gives \(\|f\|=\|\xi\|\). Applied to \(\eta\mapsto\langle\zeta,T\eta\rangle\), it constructs the adjoint \(T^*\) of every bounded operator, with \(\|T^*\|=\|T\|\). The operator norm is complete: a norm-Cauchy sequence of operators converges on each vector, and its uniform operator-norm bound makes the limit bounded and the convergence uniform on the unit ball. Furthermore
\[
\|T^*T\|\le\|T\|^2,
\qquad
\|T\xi\|^2=\langle\xi,T^*T\xi\rangle\le\|T^*T\|\|\xi\|^2
\]
give \(\|T^*T\|=\|T\|^2\). Thus bounded operators form a unital C*-algebra. The continuous calculus proved in Infinite tensor products, F03–F08 applies to it and its norm-closed self-adjoint subalgebras.

<a id="h01"></a>
## H01. Orthogonal projections and strong limits in commutants

Every closed linear subspace \(V\) of a Hilbert space has an orthogonal projection. For \(\xi\), let \(d=\inf_{v\in V}\|\xi-v\|\), and take a sequence \(v_j\) approaching this infimum. The parallelogram identity gives
\[
\|v_j-v_k\|^2
=2\|\xi-v_j\|^2+2\|\xi-v_k\|^2
-4\left\|\xi-\frac{v_j+v_k}{2}\right\|^2\longrightarrow0.
\]
The limit \(v\in V\) attains \(d\). Minimality of \(\|\xi-v-tv'\|^2\) for real and purely imaginary \(t\), for every \(v'\in V\), gives \(\xi-v\perp V\). This decomposition is unique, because \(V\cap V^\perp=\{0\}\). It gives a linear projection \(P_V\), with \(\|P_V\|\le1\), \(P_V^*=P_V\), and range \(V\). If every operator in a self-adjoint family preserves \(V\), it preserves \(V^\perp\) as well, so \(P_V\) commutes with that family.

For a family \(\mathcal S\) of bounded operators, its commutant is \(\mathcal S'=\{T:Ts=sT\text{ for all }s\in\mathcal S\}\). If \(\mathcal S\) is self-adjoint, its commutant is a unital self-adjoint algebra. It is norm closed and strongly closed: if \(T_j\xi\to T\xi\) for every \(\xi\), then \(T_js\xi=sT_j\xi\) passes to the limit. The relation \(\mathcal S'''=\mathcal S'\) follows directly from the inclusions \(\mathcal S\subset\mathcal S''\) and the fact that \(\mathcal S'\) commutes with \(\mathcal S''\). In particular \(M=\mathcal S''\) satisfies \(M''=M\). An operator in \(M\) invertible on the Hilbert space has its inverse in \(M\), since its inverse commutes with every operator commuting with it. These facts use the definition of a commutant, rather than a density theorem for operator polynomials.

<a id="h02"></a>
## H02. Kernel projections from positive inverses

An operator \(S=S^*\) is positive if \(\langle\xi,S\xi\rangle\ge0\) for all \(\xi\). For \(t>0\), the operator \(1+tS\) is invertible and its inverse \(Q_t\) has norm at most \(1\). Indeed
\[
\|(1+tS)\xi\|\|\xi\|
\ge\langle\xi,(1+tS)\xi\rangle\ge\|\xi\|^2
\]
proves the lower bound \(\|(1+tS)\xi\|\ge\|\xi\|\). It has zero kernel and closed range: a Cauchy sequence of images has Cauchy preimages by this bound. The orthogonal complement of its range is the kernel of its adjoint, hence zero. The range is therefore both dense and closed, and is the whole space. The same bound proves the inverse norm assertion.

The operators \(Q_t\) fix \(\ker S\). They commute with \(S\), and
\[
Q_tS=\frac{1-Q_t}{t},\qquad \|Q_tS\|\le\frac2t.
\]
Thus they converge to zero on \(\operatorname{ran}S\), and, by their uniform norm bound, on its closure. Since \(S=S^*\), \((\operatorname{ran}S)^\perp=\ker S\). H01 decomposes the space as \(\ker S\oplus\overline{\operatorname{ran}S}\); hence \(Q_t\) converges strongly to the kernel projection as \(t\to\infty\). If \(S\in M\), each \(Q_t\in M\) by H01, and the projection belongs to \(M\) by strong closedness.

The positive quadratic form also obeys Cauchy–Schwarz, by expanding \(\langle\xi+z\eta,S(\xi+z\eta)\rangle\ge0\) and minimizing over \(z\). If one diagonal value is zero, varying the magnitude and phase of \(z\) first shows the corresponding mixed value is zero. Consequently \(\langle\xi,S\xi\rangle=0\) implies \(\langle\eta,S\xi\rangle=0\) for every \(\eta\), and then \(S\xi=0\). This supplies a direct kernel argument without a square-root assumption.

The square-root formulation is also available. For a positive \(S\), a real \(\lambda<0\) gives an invertible \(S-\lambda\) by the same range argument. For nonreal \(\lambda\), the imaginary part of \(\langle\xi,(S-\lambda)\xi\rangle\) gives the lower bound \(|\operatorname{Im}\lambda|\|\xi\|\), and its adjoint has the same bound, so the range argument again proves invertibility. The spectrum of \(S\) is therefore nonnegative. The continuous calculus F06–F08 in Infinite tensor products supplies \(S^{1/2}\), and \(\langle\xi,S\xi\rangle=\|S^{1/2}\xi\|^2\). Conversely a self-adjoint operator with nonnegative spectrum has this self-adjoint square root, so its quadratic form is nonnegative. Thus spectral positivity and quadratic-form positivity agree. This justifies either version of the kernel calculation. Its support projection is \(1-P_{\ker S}\), the projection onto \(\overline{\operatorname{ran}S}\). If \(S\in pMp\), this range lies in \(p\mathcal H\), so the support is at most \(p\) and belongs to \(pMp\). A nonzero \(S\) has nonzero support.

<a id="h03"></a>
## H03. A concrete separable predual

For a separable Hilbert space \(\mathcal H\), a countable dense sequence gives a countable orthonormal basis: successively subtract its projections on the finite span of earlier chosen vectors, and normalize each nonzero remainder. Every member of the dense sequence lies in the resulting closed span, so that span is the whole space. Finite orthogonal truncations consequently converge to every vector. The coordinate map is an isometry onto \(\ell^2(I)\), because finite-coordinate vectors are in its image and completeness makes that image closed. This also includes finite-dimensional and zero spaces and transfers the representation argument of H00. Form the algebraic tensor product \(\overline{\mathcal H}\otimes\mathcal H\), and give it the projective norm
\[
\|u\|_\pi=\inf\left\{\sum_j\|\xi_j\|\|\eta_j\|:
u=\sum_j\overline{\xi_j}\otimes\eta_j\right\}.
\]
This is a norm. A nonzero algebraic tensor lies in the tensor product of two finite-dimensional spans; coordinate functionals in bases of those spans detect a nonzero coefficient and extend to bounded functionals using H00 and H01. Their product bounds its value by a constant times every displayed sum, so \(\|u\|_\pi>0\). The triangle inequality follows by concatenating representations. Let \(E\) be the completion. Finite rational complex combinations of tensors of a countable orthonormal basis are dense, because finite-coordinate truncations approximate each factor in the projective norm. Thus \(E\) is separable.

The dual of \(E\) is isometrically \(B(\mathcal H)\). A bounded operator \(T\) acts by \(\overline\xi\otimes\eta\mapsto\langle\xi,T\eta\rangle\), with dual norm \(\|T\|\). Conversely a bounded functional on \(E\) gives a bounded form, conjugate linear in \(\xi\) and linear in \(\eta\). H00 represents this form as \(\langle\xi,T\eta\rangle\), and its bound makes \(T\) bounded. Every \(u\in E\) can be represented by a series \(\sum_j\overline{\xi_j}\otimes\eta_j\) with \(\sum_j\|\xi_j\|\|\eta_j\|<\infty\): approximate \(u\) by algebraic tensors with geometrically decreasing errors, represent each successive difference within a geometrically decreasing error of its projective norm, and concatenate the finite representations. Conversely every such series converges in \(E\). The weak* topology from \(E\) is precisely the ultraweak topology defined by the functionals
\[
T\longmapsto\sum_j\langle\xi_j,T\eta_j\rangle,
\qquad \sum_j\|\xi_j\|\|\eta_j\|<\infty.
\]

If \(M=\mathcal S''\), its commutation constraints with \(\mathcal S'\) are ultraweak continuous: \(\langle\xi,(Ta-aT)\eta\rangle\) is the difference of two one-term functionals. Let \(N\subset E\) be the norm-closed span of the corresponding tensors, for all \(a\in\mathcal S'\) and \(\xi,\eta\in\mathcal H\). Then \(M=N^\perp\subset E^*\), exactly by these constraints. The dual of \(E/N\) is \(N^\perp\): a bounded functional on the quotient pulls back to a functional killing \(N\), and such a functional descends with the same norm, by the quotient norm definition. The quotient is complete: from a quotient-Cauchy sequence choose a subsequence whose successive quotient distances are below \(2^{-j}\), lift each difference to a vector of norm below \(2^{1-j}\), and sum those lifts in \(E\). Its image is the limit of the subsequence, and Cauchyness gives the same limit for the full sequence. The image of a countable dense set in \(E\) is dense in the quotient. Therefore \(E/N\) is a separable predual for \(M\). In particular every countable group algebra in its regular representation has separable predual. This proof does not need a compact-operator spectral decomposition.

On a norm-bounded set, weak operator convergence implies ultraweak convergence. Given a series-vector functional, choose a finite initial segment whose remaining sum of products of vector norms is small. The finite segment converges by weak operator convergence; the remaining segment is bounded uniformly by the common operator-norm bound times that remaining sum. Applying this also to the limit operator proves convergence of the whole series. This argument works for nets, since the finite initial segment imposes only finitely many convergence conditions.

For an arbitrary coordinate Hilbert space \(\ell^2(I)\), the same projective-tensor, dual and commutation-constraint arguments construct a predual and give this series-vector definition of the ultraweak topology. The separability conclusion is asserted only when \(I\) is countable. H00 supplies the representation and completeness facts for those arbitrary coordinate spaces as well.

<a id="h04"></a>
## H04. Why an infinite-dimensional finite factor has no minimal projection

Let \(M\) be a factor with a faithful normalized trace \(\tau\). If it has a minimal nonzero projection \(p\), then \(pMp=\mathbb Cp\). To prove this, suppose a self-adjoint element \(a\in pMp\) were nonscalar. Its spectrum has at least two points: F04 of Infinite tensor products makes a self-adjoint element with singleton spectrum a scalar. Choose a real \(c\) between two spectral points. The continuous positive and negative parts of \(a-cp\), supplied by F06–F08, are nonzero and have zero product. H02 gives their nonzero support projections in \(pMp\); their ranges are orthogonal because their product is zero. This contradicts minimality of \(p\). Thus every self-adjoint element of the corner is scalar, and its real and imaginary parts show the same for every element.

The closed span of the ranges of \(upu^*\), over the unitaries \(u\in M\), has a projection \(z\in M\). Indeed every such range reduces \(M'\); H01 gives its projection in \(M''=M\). Conjugation by any unitary of \(M\) preserves this span, so \(z\) commutes with those unitaries. They linearly span \(M\): for a self-adjoint contraction \(h\), the continuous calculus gives the unitary \(h+i(1-h^2)^{1/2}\), whose real part is \(h\); scaling and taking real and imaginary parts treats any element. Thus \(z\) is central. Since \(p\ne0\), the factor property gives \(z=1\).

For any nonzero projection \(q\in M\), it follows that \(qMp\ne0\). Otherwise \(qup=0\) for every unitary \(u\), making \(q\) vanish on the dense span just described. Choose \(x=qap\ne0\). Since \(x^*x\in pMp\), it equals \(\alpha p\) for \(\alpha>0\). Then \(v=\alpha^{-1/2}x\) satisfies \(v^*v=p\), and \(vv^*\le q\) is a projection equivalent to \(p\).

Starting with \(p\), repeat this in the complement of the sum of the projections already chosen. Each new projection has trace \(\tau(p)>0\). Since the sum has trace at most \(1\), after finitely many steps there can be no nonzero complement. We obtain \(p_1+\cdots+p_m=1\), with each \(p_i\) equivalent to \(p\). Choose \(v_i^*v_i=p\), \(v_iv_i^*=p_i\). The operators \(v_iv_j^*\) are matrix units, and for \(x\in M\), every \(v_i^*xv_j\) lies in \(pMp=\mathbb Cp\). Expanding \(x=\sum_{i,j}p_ixp_j\) therefore proves \(M\cong M_m(\mathbb C)\). An infinite-dimensional factor with a faithful normalized trace consequently has no minimal projections; it is a type \(\mathrm{II}_1\) factor. An infinite discrete group's unitaries are linearly independent on \(\delta_e\), so its ICC group factor is infinite dimensional and this conclusion applies.

This also gives the formulation in terms of abelian projections. The central-support argument above applies to every nonzero projection \(r\), not just a minimal one; hence \(qMr\ne0\) for any nonzero projections \(q,r\) in a factor. If a nonzero projection \(e\) has commutative corner \(eMe\) and \(0<q<e\), put \(r=e-q\). Commutativity gives \(qMr=q(eMe)r=0\), a contradiction. Thus an abelian projection in a factor is minimal. The infinite-dimensional case has no nonzero abelian projections. Finally the trace makes the identity finite: if \(v^*v=1\), then \(\tau(vv^*)=1\), so faithfulness applied to \(1-vv^*\) gives \(vv^*=1\). This proves both the type-II and finite parts of the type \(\mathrm{II}_1\) designation.

## Regular representations and conventions

Let \(G\) be a discrete group with identity \(e\). The space

\[
\ell^2(G)=\left\{\xi:G\longrightarrow\mathbb C:
             \sum_{s\in G}|\xi(s)|^2<\infty\right\}
\]

has inner product \(\langle\xi,\eta\rangle=\sum_s\overline{\xi(s)}\eta(s)\), antilinear in its first variable. Its usual orthonormal basis is \((\delta_s)_{s\in G}\). All sums over \(G\) below use finite partial sums and are independent of ordering. H00 shows that square-summable vectors have countable support; whenever a scalar product is rearranged, its absolute convergence is proved first. Thus the commutant and subgroup arguments also apply to arbitrary discrete groups.

H00 proves the bounded-operator, adjoint and Hilbert-space representation facts used below, including density of finitely supported vectors. A bounded operator \(T\) is **positive** when \(\langle\xi,T\xi\rangle\geq0\) for every \(\xi\). Order is the order defined by positive differences. We will prove both preservation of bounded increasing positive suprema and ultraweak continuity for the trace and subgroup expectation. The elementary existence of these suprema is proved below.

For a set \(S\) of bounded operators write

\[
S'=\{T:TA=AT\text{ for every }A\in S\},\qquad S''=(S')'.
\]

The left and right regular representations are

\[
\lambda(g)\delta_t=\delta_{gt},\qquad
\rho(g)\delta_t=\delta_{tg^{-1}}.
\tag{1}
\]

These operators permute an orthonormal basis, so they are unitary. Their products satisfy \(\lambda(g)\lambda(h)=\lambda(gh)\), \(\rho(g)\rho(h)=\rho(gh)\), and \(\lambda(g)\rho(h)=\rho(h)\lambda(g)\). We define the group von Neumann algebra by

\[
L(G)=\lambda(G)''.
\tag{2}
\]

This definition lets us establish the particular commutant identities needed here directly. No operator approximation by finite Fourier sums is needed.

<a id="g00"></a>
## G00. Matrix products and the regular commutants

For \(T\in B(\ell^2(G))\), let \(T_{s,t}=\langle\delta_s,T\delta_t\rangle\). Its \(t\)-th column lies in \(\ell^2(G)\), with norm \(\|T\delta_t\|\leq\|T\|\). Its \(s\)-th row lies in \(\ell^2(G)\), with norm \(\|T^*\delta_s\|\leq\|T\|\). Indeed, \((T^*)_{t,s}=\overline{T_{s,t}}\).

If \(A,B\) are bounded, then

\[
(AB)_{s,t}=\sum_{r\in G}A_{s,r}B_{r,t},
\qquad
\sum_r|A_{s,r}B_{r,t}|
\leq\|A^*\delta_s\|\,\|B\delta_t\|.
\tag{3}
\]

The inequality is Cauchy–Schwarz. To verify the equality, expand \(B\delta_t\) in the orthonormal basis. Its finite partial sums converge in Hilbert space norm. Applying \(A\), then taking the \(s\)-th coordinate, gives (3). Operators with the same matrix entries agree: they agree on each basis vector and hence, by boundedness and density, on every vector.

**Lemma 1.** A bounded operator \(x\) commutes with \(\rho(G)\) if and only if there is a function \(a\in\ell^2(G)\) such that

\[
x_{s,t}=a(st^{-1})\quad(s,t\in G).
\tag{4}
\]

A bounded operator \(y\) commutes with \(\lambda(G)\) if and only if there is a function \(b\in\ell^2(G)\) such that

\[
y_{s,t}=b(t^{-1}s)\quad(s,t\in G).
\tag{5}
\]

*Proof.* If \(x\rho(g)=\rho(g)x\), put \(a=x\delta_e\). Since \(\delta_t=\rho(t^{-1})\delta_e\),

\[
x\delta_t=\rho(t^{-1})a,
\]

whose \(s\)-th coordinate is \(a(st^{-1})\). Conversely, if (4) holds, the \(s\)-th coordinates of \(x\rho(g)\delta_t\) and \(\rho(g)x\delta_t\) are both \(a(sgt^{-1})\). Equality on the basis proves commutation.

For the second assertion put \(b=y\delta_e\), and use \(\delta_t=\lambda(t)\delta_e\). This gives \(y\delta_t=\lambda(t)b\) and (5). Conversely, the \(s\)-th coordinates of \(y\lambda(g)\delta_t\) and \(\lambda(g)y\delta_t\) are both \(b(t^{-1}g^{-1}s)\). Again equality on the basis suffices. \(\square\)

**Theorem 2 (regular commutants).** For every discrete \(G\),

\[
\boxed{\lambda(G)''=\rho(G)',\qquad
       \rho(G)''=\lambda(G)'.}
\tag{6}
\]

*Proof.* Since every \(\rho(g)\) commutes with \(\lambda(G)\), we have \(\rho(G)\subseteq\lambda(G)'\); taking commutants gives \(\lambda(G)''\subseteq\rho(G)'\).

For the reverse inclusion take \(x\in\rho(G)'\) and an arbitrary \(y\in\lambda(G)'\). Let \(a,b\) be their functions in (4) and (5). Formula (3) gives

\[
(xy)_{s,t}=\sum_{r\in G}a(sr^{-1})b(t^{-1}r),
\tag{7}
\]

and

\[
(yx)_{s,t}=\sum_{u\in G}b(u^{-1}s)a(ut^{-1}).
\tag{8}
\]

Both sums converge absolutely. For example the maps \(r\mapsto sr^{-1}\) and \(r\mapsto t^{-1}r\) are bijections of \(G\), so the sum of absolute values in (7) is at most \(\|a\|_2\|b\|_2\); the same argument applies to (8). In (8) substitute

\[
u=sr^{-1}t.
\]

This is a bijective change of index, and it gives \(u^{-1}s=t^{-1}r\), \(ut^{-1}=sr^{-1}\). Thus (7) and (8) are equal. All matrix entries of \(xy\) and \(yx\) agree, hence \(xy=yx\). Since \(y\) was arbitrary in \(\lambda(G)'\), \(x\in\lambda(G)''\).

Finally, for every set \(S\), \(S'''=S'\): the inclusion \(S\subseteq S''\) yields \(S'''\subseteq S'\), while each element of \(S'\) commutes with each element of \(S''\) by the definition of \(S''\). Taking commutants of the first identity in (6) therefore gives the second. \(\square\)

In particular \(L(G)=\rho(G)'\) is a unital algebra closed under adjoints: if \(x\) commutes with all \(\rho(g)\), then \(x^*\) does too, by taking adjoints and using \(\rho(g)^*=\rho(g^{-1})\). It is closed in both the weak and strong operator topologies. For example, if \(x_i\to x\) strongly and each \(x_i\) commutes with a fixed \(\rho(g)\), then for every vector \(\xi\),

\[
x\rho(g)\xi=\lim_i x_i\rho(g)\xi
             =\lim_i\rho(g)x_i\xi=\rho(g)x\xi.
\]

For weak convergence take the matrix coefficient against an arbitrary vector on both sides of the same equality. This proves the closure assertions directly.

<a id="g01"></a>
## G01. Increasing positive operators and the canonical trace

We first record an order fact so that normality will not hide a density or continuity theorem.

**Lemma 3 (monotone convergence of bounded operators).** Let \((T_i)\) be an increasing net of positive bounded operators on a Hilbert space, with \(\sup_i\|T_i\|\leq C<\infty\). There is a positive operator \(T\) such that \(T_i\to T\) strongly, and \(T\) is their least upper bound. If every \(T_i\) belongs to a strongly closed algebra, \(T\) belongs to that algebra.

*Proof.* A positive operator \(A\) has the positive-form Cauchy–Schwarz inequality

\[
|\langle\eta,A\xi\rangle|^2
\leq\langle\eta,A\eta\rangle\langle\xi,A\xi\rangle.
\tag{9}
\]

To prove it, expand \(\langle\eta+z\xi,A(\eta+z\xi)\rangle\geq0\) for \(z\in\mathbb C\) and minimize the resulting quadratic polynomial. If \(\langle\xi,A\xi\rangle=0\), the linear term must vanish for every \(z\), which proves the zero case too. The positivity condition also implies self-adjointness, by polarization of this quadratic form.

For each \(\xi\) the numbers \(q_i(\xi)=\langle\xi,T_i\xi\rangle\) increase to a finite limit \(q(\xi)\), bounded by \(C\|\xi\|^2\). Polarization shows that each \(\langle\eta,T_i\xi\rangle\) has a limit. These limits form a bounded sesquilinear form, of absolute value at most \(C\|\eta\|\|\xi\|\), since this bound holds for each \(i\). The Hilbert space representation theorem supplies a bounded operator \(T\) with those matrix coefficients. It is positive and \(0\leq T_i\leq T\leq CI\).

Put \(A_i=T-T_i\). By (9), taking the supremum over unit vectors \(\eta\),

\[
\|A_i\xi\|^2
=\sup_{\|\eta\|=1}|\langle\eta,A_i\xi\rangle|^2
\leq C\langle\xi,A_i\xi\rangle\longrightarrow0.
\tag{10}
\]

Thus \(T_i\to T\) strongly. If \(S\) is any self-adjoint upper bound, then \(\langle\xi,(S-T_i)\xi\rangle\geq0\) for every \(i\); taking the limit gives \(S\geq T\). This proves that \(T\) is the supremum. The last assertion is strong closure. \(\square\)

Define

\[
\tau_G(x)=\langle\delta_e,x\delta_e\rangle\quad(x\in L(G)).
\tag{11}
\]

**Theorem 4 (canonical trace).** The functional \(\tau_G\) is a faithful normal tracial state on \(L(G)\).

*Proof.* It is linear, positive, and \(\tau_G(I)=1\), directly from (11). Also \(|\tau_G(x)|\leq\|x\|\). It has norm one because equality holds at \(I\).

The vector \(\delta_e\) is separating for \(L(G)\). Indeed, if \(x\delta_e=0\), then, because \(x\in\rho(G)'\),

\[
x\delta_t=x\rho(t^{-1})\delta_e
          =\rho(t^{-1})x\delta_e=0
\]

for every \(t\). Hence \(x=0\). It is also cyclic, since \(\lambda(t)\delta_e=\delta_t\) and finitely supported vectors are dense.

For \(x\in L(G)\),

\[
\tau_G(x^*x)=\|x\delta_e\|^2.
\tag{12}
\]

This proves faithfulness in the form \(\tau_G(x^*x)=0\Rightarrow x=0\). It also proves faithfulness on arbitrary positive operators without invoking a square root: if \(p\geq0\) and \(\tau_G(p)=0\), inequality (9) gives \(\langle\eta,p\delta_e\rangle=0\) for every \(\eta\), so \(p\delta_e=0\), and the separating property gives \(p=0\).

For traciality let \(a=x\delta_e\), \(c=y\delta_e\), where \(x,y\in L(G)=\rho(G)'\). Equations (3) and (4) give

\[
\tau_G(xy)=\sum_{r\in G}a(r^{-1})c(r),\qquad
\tau_G(yx)=\sum_{u\in G}c(u^{-1})a(u).
\tag{13}
\]

Both sums have sum of absolute values at most \(\|a\|_2\|c\|_2\). Changing \(u\) to \(r^{-1}\) in the second proves \(\tau_G(xy)=\tau_G(yx)\) for the arbitrary bounded operators under consideration.

If \(x_i\) is an increasing bounded net of positive elements of \(L(G)\), Lemma 3 and strong closure give its supremum \(x\in L(G)\) and \(x_i\delta_e\to x\delta_e\). Therefore

\[
\tau_G(x)=\lim_i\tau_G(x_i)=\sup_i\tau_G(x_i).
\]

This proves order normality. Formula (11) is a one-term series-vector functional in H03, so the trace is also ultraweakly continuous. \(\square\)

The trace also directly rules out proper isometries in \(L(G)\). If \(v^*v=I\), then \(vv^*\) is a projection and \(\tau_G(I-vv^*)=\tau_G(I)-\tau_G(v^*v)=0\). Faithfulness gives \(vv^*=I\). This observation uses no classification of finite factors.

<a id="g02"></a>
## G02. Fourier coefficients and their precise convergence

For \(x\in L(G)\) define its Fourier coefficient at \(g\) by

\[
\widehat x(g)=\langle\delta_g,x\delta_e\rangle.
\tag{14}
\]

Lemma 1 gives the complete matrix from these coefficients:

\[
x_{s,t}=\widehat x(st^{-1}).
\tag{15}
\]

In particular the coefficients determine \(x\) uniquely. They satisfy

\[
\widehat x(g)=\tau_G\bigl(x\lambda(g)^*\bigr),
\qquad
\widehat{x^*}(g)=\overline{\widehat x(g^{-1})},
\tag{16}
\]

and

\[
\widehat{xy}(s)=\sum_{r\in G}\widehat x(sr^{-1})\widehat y(r),
\qquad
\sum_r|\widehat x(sr^{-1})\widehat y(r)|
\leq\|x\delta_e\|\,\|y\delta_e\|.
\tag{17}
\]

For the first identity in (16), \(\lambda(g)^*\delta_e=\delta_{g^{-1}}\), so (15) gives the coefficient \(x_{e,g^{-1}}=\widehat x(g)\). The adjoint identity follows by exchanging the matrix indices in (15) and taking complex conjugates. Formula (17) is the \(s,e\) case of (3), with Cauchy–Schwarz as indicated.

Put \(\|x\|_2=\tau_G(x^*x)^{1/2}\). By (12),

\[
\|x\|_2^2=\sum_{g\in G}|\widehat x(g)|^2.
\tag{18}
\]

The map \(V_\tau:x\mapsto x\delta_e\) is an isometry from \(L(G)\), with the inner product \(\tau_G(x^*y)\), into \(\ell^2(G)\). Its range is dense because it contains every \(\delta_g=\lambda(g)\delta_e\). It therefore extends to a unitary from the Hilbert space completion, denoted \(L^2(L(G),\tau_G)\), onto \(\ell^2(G)\).

If \(F\subset G\) is finite and

\[
x_F=\sum_{g\in F}\widehat x(g)\lambda(g),
\]

then

\[
\|x-x_F\|_2^2=\sum_{g\notin F}|\widehat x(g)|^2\longrightarrow0
\tag{19}
\]

as the finite subsets exhaust \(G\). This is exactly convergence in the Hilbert space just defined. Equation (19) makes no assertion about strong or weak operator convergence of the \(x_F\), and gives no uniform operator norm bound for these finite sums.

<a id="g03"></a>
## G03. The subgroup algebra inside the group algebra

Let \(H\leq G\) be any subgroup. Write \(\lambda_H,\rho_H\) for its regular representations on \(\ell^2(H)\). Applying Theorem 2 to \(H\) gives

\[
L(H)=\lambda_H(H)''=\rho_H(H)'.
\]

To identify this algebra inside \(L(G)\), partition \(G\) into right cosets \(Ht\). Choose one representative \(t\) in each coset, including \(e\) for \(H\), and let \(\mathcal T\) be the representatives. Then

\[
\ell^2(G)=\bigoplus_{t\in\mathcal T}\ell^2(Ht),
\qquad U_t:\ell^2(H)\longrightarrow\ell^2(Ht),\quad
U_t\delta_h=\delta_{ht}.
\tag{20}
\]

Each \(U_t\) is unitary onto its summand and intertwines \(\lambda_H(h)\) with \(\lambda_G(h)\) on that summand. Define

\[
\iota_H(b)=\bigoplus_{t\in\mathcal T}U_tbU_t^*
             \quad(b\in L(H)).
\tag{21}
\]

The direct sum is bounded: the square of its value on \(\xi=\bigoplus_t\xi_t\) has norm at most \(\|b\|^2\sum_t\|\xi_t\|^2\). Conversely restriction to the \(H\) summand has norm \(\|b\|\), so \(\|\iota_H(b)\|=\|b\|\). Products and adjoints are computed on each summand, making \(\iota_H\) an injective unital *-homomorphism. It is independent of representatives: replacing \(t\) by \(h_0t\) changes \(U_t\) to \(U_t\rho_H(h_0^{-1})\), and \(b\) commutes with that right regular unitary. Its values on group elements are

\[
\iota_H(\lambda_H(h))=\lambda_G(h)\quad(h\in H).
\tag{22}
\]

**Theorem 5 (subgroup embedding).** The map \(\iota_H\) identifies \(L(H)\) with

\[
L_G(H):=\lambda_G(H)''\subseteq L(G).
\tag{23}
\]

It preserves the canonical trace and suprema of increasing bounded positive nets.

*Proof.* Let \(P_t\) be the projection onto \(\ell^2(Ht)\). If \(y\in\lambda_G(H)'\), every block

\[
y_{u,t}=U_u^*P_u yU_t:\ell^2(H)\longrightarrow\ell^2(H)
\]

commutes with \(\lambda_H(H)\). Explicitly, for \(h\in H\) the intertwining relations and commutation of \(y\) give

\[
\lambda_H(h)y_{u,t}
=U_u^*P_u\lambda_G(h)yU_t
=U_u^*P_u y\lambda_G(h)U_t
=y_{u,t}\lambda_H(h).
\]

Thus \(y_{u,t}\in\lambda_H(H)'\). For \(b\in\lambda_H(H)''\),

\[
b\,y_{u,t}=y_{u,t}\,b
\]

for each pair of cosets. These are precisely the blocks of \(\iota_H(b)y\) and \(y\iota_H(b)\). Equality of all blocks implies equality of the operators: for a vector in one summand their projections to all summands agree, and finite sums of such vectors are dense. Hence \(\iota_H(b)\in\lambda_G(H)''\).

Conversely let \(x\in\lambda_G(H)''\). Each \(P_t\) commutes with \(\lambda_G(H)\), so \(x\) commutes with \(P_t\). Thus \(x\) is block diagonal. For any \(u,t\in\mathcal T\), the bounded partial isometry

\[
V_{u,t}=U_uU_t^*P_t
\]

also commutes with \(\lambda_G(H)\). Commutation with \(x\) says that its diagonal blocks, transported to \(\ell^2(H)\), are all the same bounded operator \(b\). For each \(z\in\lambda_H(H)'\), the diagonal operator \(\bigoplus_t U_tzU_t^*\) belongs to \(\lambda_G(H)'\), so \(x\) commutes with it. Restricting to the \(H\) summand gives \(bz=zb\). Consequently \(b\in\lambda_H(H)''=L(H)\) and \(x=\iota_H(b)\). This proves equality of the range with (23). Inclusion in \(L(G)\) follows from \(\lambda_G(H)\subseteq\lambda_G(G)\): taking commutants reverses the inclusion, and taking commutants again restores it.

Because the \(H\) summand uses \(t=e\),

\[
\tau_G(\iota_H(b))=\langle\delta_e,b\delta_e\rangle=\tau_H(b).
\tag{24}
\]

For the order assertion let \(b_i\uparrow b\) be a bounded increasing net in \(L(H)_+\). Lemma 3 gives strong convergence on \(\ell^2(H)\). The positive operator \(\iota_H(b)\) is an upper bound for all \(\iota_H(b_i)\). To verify strong convergence on \(\ell^2(G)\), fix \(\xi=\bigoplus_t\xi_t\) and bound \(\|b-b_i\|\) by a common constant \(D\). For a finite collection \(K\subset\mathcal T\),

\[
\|\bigl(\iota_H(b)-\iota_H(b_i)\bigr)\xi\|^2
\leq\sum_{t\in K}\|(b-b_i)U_t^*\xi_t\|^2
       +D^2\sum_{t\notin K}\|\xi_t\|^2.
\tag{25}
\]

First make the tail as small as desired by choosing \(K\), then use strong convergence for its finitely many vectors. Thus \(\iota_H(b_i)\to\iota_H(b)\) strongly. Lemma 3, or its least-upper-bound argument, proves that \(\iota_H(b)\) is their supremum. \(\square\)

An element \(\iota_H(b)\) has Fourier coefficients zero outside \(H\), and its coefficient at \(h\in H\) is \(\widehat b(h)\), because \(\iota_H(b)\delta_e=b\delta_e\in\ell^2(H)\).

<a id="g04"></a>
## G04. Compression and the subgroup expectation

Let \(P_H\) denote the orthogonal projection of \(\ell^2(G)\) onto \(\ell^2(H)\), and let \(j_H:\ell^2(H)\hookrightarrow\ell^2(G)\) be inclusion. Thus \(j_H^*=P_H\), with the range of \(P_H\) viewed as \(\ell^2(H)\). For \(x\in L(G)\) put

\[
c_H(x)=j_H^*xj_H\in B(\ell^2(H)).
\tag{26}
\]

For \(h\in H\), the right translation \(\rho_G(h)\) preserves \(H\) and its complement, so \(P_H\rho_G(h)=\rho_G(h)P_H\), and its restriction is \(\rho_H(h)\). Since \(x\) commutes with \(\rho_G(h)\),

\[
c_H(x)\rho_H(h)=\rho_H(h)c_H(x).
\]

Theorem 2 for \(H\) now proves \(c_H(x)\in L(H)\). We can therefore define

\[
\boxed{E_H(x)=\iota_H(c_H(x))\in L_G(H).}
\tag{27}
\]

This distinguishes the compression on \(\ell^2(H)\) from the resulting operator on \(\ell^2(G)\).

**Theorem 6 (subgroup expectation).** The map \(E_H:L(G)\to L_G(H)\) is linear, positive, unital, contractive, normal, faithful, and trace preserving. It fixes \(L_G(H)\), hence is an idempotent map onto it. For \(b_1,b_2\in L_G(H)\) and \(x\in L(G)\),

\[
E_H(b_1xb_2)=b_1E_H(x)b_2.
\tag{28}
\]

Its Fourier coefficients are

\[
\widehat{E_H(x)}(g)=
\begin{cases}
\widehat x(g),&g\in H,\\
0,&g\notin H.
\end{cases}
\tag{29}
\]

*Proof.* Compression is linear, preserves adjoints, sends \(I\) to the identity on \(\ell^2(H)\), and has norm at most one. It is positive because for \(\xi\in\ell^2(H)\),

\[
\langle\xi,c_H(x)\xi\rangle
=\langle j_H\xi,xj_H\xi\rangle\geq0\quad(x\geq0).
\]

The direct sum defining \(\iota_H\) preserves positivity and the unit and is isometric, so \(E_H\) has these same properties, including \(\|E_H(x)\|\leq\|x\|\). Also \(c_H(\iota_H(b))=b\), proving that \(E_H\) fixes its range and \(E_H^2=E_H\).

Each element of \(L_G(H)\) is block diagonal for the decomposition (20). In particular it commutes with \(P_H\) and restricts on \(H\) to its corresponding element in \(L(H)\). If \(b_j=\iota_H(d_j)\), then

\[
c_H(b_1xb_2)=d_1c_H(x)d_2.
\]

Applying the multiplicative map \(\iota_H\) proves (28).

To prove normality let \(0\leq x_i\uparrow x\) be bounded in \(L(G)\). Lemma 3 gives \(x_i\to x\) strongly. Consequently \(c_H(x_i)\to c_H(x)\) strongly on \(\ell^2(H)\). The compressed net is positive, increasing, and bounded, and its limit is its supremum by Lemma 3. The order assertion of Theorem 5 then gives

\[
E_H(x_i)\uparrow E_H(x).
\]

Since \(\delta_e\in\ell^2(H)\),

\[
\tau_G(E_H(x))
=\tau_H(c_H(x))
=\langle\delta_e,x\delta_e\rangle
=\tau_G(x).
\tag{30}
\]

If \(x\geq0\) and \(E_H(x)=0\), equation (30) gives \(\tau_G(x)=0\); Theorem 4 gives \(x=0\). This proves faithfulness.

Finally \(E_H(x)\delta_e=c_H(x)\delta_e=P_Hx\delta_e\), viewed as a vector in \(\ell^2(G)\). Its coordinates are exactly (29). \(\square\)


The embedding and compression are ultraweakly continuous directly. For compression, a test \(\sum_j\langle\xi_j,c_H(x)\eta_j\rangle\) pulls back to \(\sum_j\langle j_H\xi_j,xj_H\eta_j\rangle\), with the same summable norm products. For amplification, decompose the two vectors in each test into their right-coset coordinates \(\xi_{j,t},\eta_{j,t}\). The pullback is the series of tests
\[
\sum_{j,t}\langle\xi_{j,t},b\eta_{j,t}\rangle,
\qquad
\sum_{j,t}\|\xi_{j,t}\|\|\eta_{j,t}\|
\le\sum_j\|\xi_j\|\|\eta_j\|<\infty,
\]
by Cauchy–Schwarz over the cosets. Absolute convergence permits flattening the countable double series. H03 therefore proves ultraweak continuity of both maps and their composite \(E_H\), in addition to the positive-supremum calculation.
When the coset set is uncountable, each vector still has only countably many nonzero coset coordinates by the finite-partial-sum argument of H00. The union of these supports over the countably many tests is countable, so exactly the same summable-series proof applies.

These are the defining properties of a trace-preserving conditional expectation. Positivity also holds at every matrix level if that form is needed: for \(X=[x_{ij}]\geq0\) acting on \(\ell^2(G)^{\oplus n}\), its matrix of compressions \([c_H(x_{ij})]\) is the compression by \(j_H^{\oplus n}\), so is positive on \(\ell^2(H)^{\oplus n}\). The matrix \([E_H(x_{ij})]\), after grouping coordinates by right cosets, is a direct sum of copies of this positive matrix. It is therefore positive. Thus \(E_H\) is completely positive, by direct compression.

Under the isometry \(V_\tau\) of G02,

\[
V_\tau(E_H(x))=P_HV_\tau(x).
\tag{31}
\]

Consequently its extension to \(L^2(L(G),\tau_G)\) is the orthogonal projection onto the copy of \(\ell^2(H)\). Explicitly,

\[
\|E_H(x)\|_2^2=\sum_{h\in H}|\widehat x(h)|^2
\leq\|x\|_2^2.
\tag{32}
\]

The range of the extended projection is the Hilbert space closure of \(L_G(H)\), because the vectors \(\lambda(h)\delta_e=\delta_h\), \(h\in H\), span a dense subspace of \(\ell^2(H)\).

**Corollary 7 (Fourier support).** For \(x\in L(G)\),

\[
x\in L_G(H)
\quad\Longleftrightarrow\quad
\widehat x(g)=0\text{ for every }g\notin H.
\tag{33}
\]

*Proof.* The forward implication was established after Theorem 5. If the coefficients vanish off \(H\), equation (29) says that \(x\) and \(E_H(x)\) have identical coefficients. Equation (15) or the separating property gives \(x=E_H(x)\in L_G(H)\). \(\square\)

**Corollary 8 (uniqueness).** Suppose \(F:L(G)\to L_G(H)\) is a linear map with \(\tau_G\circ F=\tau_G\) and the bimodule property (28). Then \(F=E_H\).

*Proof.* For \(h\in H\),

\[
\widehat{F(x)}(h)
=\tau_G(F(x)\lambda(h)^*)
=\tau_G(F(x\lambda(h)^*))
=\tau_G(x\lambda(h)^*)=\widehat x(h).
\]

Off \(H\) all coefficients of \(F(x)\) vanish by Corollary 7, since its value is in \(L_G(H)\). Thus \(F(x)\) and \(E_H(x)\) have the same coefficients, so they are equal. \(\square\)

<a id="g05"></a>
## G05. Conjugacy classes and the factor criterion

The center of \(L(G)\) is the set of its elements commuting with every element of \(L(G)\). It is enough to commute with the regular group unitaries: if \(x\in L(G)\cap\lambda(G)'\), then every element of \(L(G)=\lambda(G)''\) commutes with \(x\) by the definition of the second commutant.

For \(g\in G\) and \(x\in L(G)\),

\[
(\lambda(g)x\lambda(g)^*)\delta_e
=\lambda(g)x\delta_{g^{-1}}
=\lambda(g)\rho(g)x\delta_e.
\tag{34}
\]

The permutation \(\lambda(g)\rho(g)\) sends \(\delta_t\) to \(\delta_{gtg^{-1}}\). Taking coordinates in (34) gives

\[
\widehat{\lambda(g)x\lambda(g)^*}(s)
=\widehat x(g^{-1}sg).
\tag{35}
\]

Fourier uniqueness therefore proves that \(x\) is central exactly when \(\widehat x\) is constant on each conjugacy class.

**Theorem 9 (group factor criterion).** The center of \(L(G)\) consists of the scalars if and only if every conjugacy class of a nonidentity element of \(G\) is infinite.

*Proof.* Suppose those conjugacy classes are infinite and \(x\) is central. Let \(C\) be any such class and let \(c\) be the constant value of \(\widehat x\) on \(C\). For every positive integer \(N\), choose \(N\) distinct points of \(C\). Equation (18) gives

\[
N|c|^2\leq\|x\|_2^2.
\]

Letting \(N\) grow proves \(c=0\). Thus \(\widehat x\) vanishes off \(e\), and \(x\) and \(\widehat x(e)I\) have the same Fourier coefficients. They are equal.

Conversely suppose \(C\) is a finite conjugacy class containing a nonidentity element. The finite sum

\[
z_C=\sum_{s\in C}\lambda(s)
\]

belongs to \(L(G)\). For every \(g\in G\), conjugation by \(\lambda(g)\) permutes its summands, so \(\lambda(g)z_C\lambda(g)^*=z_C\). By the observation preceding (34), \(z_C\) is central. Yet

\[
z_C\delta_e=\sum_{s\in C}\delta_s
\]

is nonzero and orthogonal to \(\delta_e\), because \(e\notin C\). A scalar operator cannot have this value on \(\delta_e\), so \(z_C\) is not scalar. \(\square\)

A von Neumann algebra with scalar center is called a **factor**. The group condition in Theorem 9 is usually called the ICC condition. If a convention requires an ICC group to be infinite, state the criterion as: \(L(G)\) is a factor exactly when \(G\) is trivial or is ICC. The trivial group satisfies the displayed conjugacy-class condition vacuously and has \(L(G)=\mathbb C\). No assertion about the type of an infinite factor or about its predual is required for this criterion.

## Reading

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, free author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Section 1.3.1, printed pages 6–9: the regular representations, canonical trace, Theorem 1.3.6, Remark 1.3.7, and Proposition 1.3.9. For the general trace-preserving expectation theorem and its Hilbert space interpretation, see Theorem 9.1.2 and Remark 9.1.3. The full group-specific arguments used in this lesson are given above.

<a id="t01"></a>
## T01. Bounded weak convergence and ultraweak functionals

Let \(T_j\in B(\mathcal H)\) satisfy \(\sup_j\|T_j\|\le C\), and suppose \(T_j\to0\) weakly. Every ultraweak series-vector functional has the form
\[
F(T)=\sum_{r=1}^\infty\langle\xi_r,T\eta_r\rangle,
\qquad \sum_r\|\xi_r\|\|\eta_r\|<\infty.
\]
For each \(R\), the first \(R\) terms tend to zero, while
\[
\left|\sum_{r>R}\langle\xi_r,T_j\eta_r\rangle\right|
\le C\sum_{r>R}\|\xi_r\|\|\eta_r\|.
\]
Choosing \(R\) and then \(j\) proves \(F(T_j)\to0\). Thus a uniformly bounded weakly convergent family is ultraweakly convergent. The proof works for nets as well as sequences, and for a limit other than zero after subtraction. A bounded strongly convergent family is weakly convergent and therefore has the same ultraweak limit.

For a concrete von Neumann algebra \(M\subset B(\mathcal H)\), an ultraweakly continuous linear functional on \(M\) is a restriction of a series-vector functional. Here is the relevant elementary topological point. Continuity at zero supplies finitely many series-vector tests \(F_1,\ldots,F_k\) and a constant \(c\) with \(|\varphi(x)|\le c\max_i|F_i(x)|\) on \(M\). Consequently \(\varphi\) vanishes on the kernel of \(x\mapsto(F_1(x),\ldots,F_k(x))\), so it factors through this map. Extend the resulting linear functional on its image to \(\mathbb C^k\). Then \(\varphi=\sum_i a_i F_i|_M\); concatenating the finitely many absolutely summable series gives the asserted form. In particular T01 applies to every normal functional, where "normal" here means ultraweakly continuous.

<a id="t02"></a>
## T02. Escaping conjugates in an ICC group

Let \(G\) be a countable discrete ICC group, \(M=L(G)\) in its left regular representation on \(\ell^2(G)\), and
\[
\lambda_g\delta_t=\delta_{gt},\qquad
\rho_g\delta_t=\delta_{tg^{-1}},\qquad
\tau(x)=\langle\delta_e,x\delta_e\rangle.
\]
Let \(\sigma\) be a normal normalized tracial state on \(M\). Fix \(g\ne e\). Its conjugacy class is infinite, so choose pairwise distinct conjugates \(g_j=h_jgh_j^{-1}\). A sequence of distinct elements leaves every finite subset of \(G\). For basis vectors,
\[
\langle\delta_s,\lambda_{g_j}\delta_t\rangle
=1_{\{s=g_jt\}}\longrightarrow0.
\]
The same convergence holds for finite-support vectors by linearity. For arbitrary \(\xi,\eta\), choose finite-support approximants \(\xi_0,\eta_0\). Since \(\|\lambda_{g_j}\|=1\), the difference from the finite-support matrix coefficient is at most
\[
\|\xi-\xi_0\|\|\eta\|+\|\xi_0\|\|\eta-\eta_0\|,
\]
uniformly in \(j\). Hence \(\lambda_{g_j}\to0\) weakly, and T01 makes this convergence ultraweak. Traciality gives
\[
\sigma(\lambda_{g_j})
=\sigma(\lambda_{h_j}\lambda_g\lambda_{h_j}^*)
=\sigma(\lambda_g).
\]
Normality therefore gives \(\sigma(\lambda_g)=0\). At the identity, \(\sigma(1)=1\). Thus \(\sigma\) and \(\tau\) agree on the algebraic span of the group unitaries.

This calculation by itself proves agreement only on that span. Extending it by ultraweak density would require the double commutant density theorem. T03 instead proves agreement on every \(x\in M\) directly.

<a id="t03"></a>
## T03. Uniqueness of the normal normalized trace on an ICC group algebra

For \(h\in G\), put \(V_h=\lambda_h\rho_h\), so that \(V_h\delta_t=\delta_{hth^{-1}}\). A vector fixed by every \(V_h\) has coordinates constant on conjugacy classes. ICC and square summability force all nonidentity coordinates to vanish. The common fixed space is therefore \(\mathbb C\delta_e\).

Fix \(x\in M\), and let \(K\) be the norm-closed convex hull in \(\ell^2(G)\) of \(\{V_hx\delta_e:h\in G\}\). This nonempty bounded closed convex set has a unique vector of smallest norm. To see existence, put \(d=\inf_{\xi\in K}\|\xi\|\), and choose \(\xi_j\in K\) with \(\|\xi_j\|^2\to d^2\). Convexity and the parallelogram identity give
\[
\|\xi_j-\xi_k\|^2
\le2\|\xi_j\|^2+2\|\xi_k\|^2-4d^2\longrightarrow0.
\]
Completeness and closedness give a minimizing limit. If two vectors minimize, applying the same identity to their midpoint proves that they coincide.

Each \(V_h\) maps \(K\) onto itself and preserves the norm; it must fix the unique minimizer. The preceding fixed-space calculation makes this minimizer a scalar multiple of \(\delta_e\). Every vector in \(K\) has identity coefficient \(\langle\delta_e,x\delta_e\rangle=\tau(x)\), because conjugation fixes the identity coordinate. Thus the minimizer is exactly \(\tau(x)\delta_e\).

Choose finite convex combinations \(a_j\) of the conjugates \(\lambda_hx\lambda_h^*\) whose vectors at \(\delta_e\) converge in norm to \(\tau(x)\delta_e\). These are exactly the corresponding convex combinations in \(K\): left and right translations commute and \(x\) commutes with \(\rho_h\), so
\[
\lambda_hx\lambda_h^*\delta_e
=\lambda_hx\rho_h\delta_e
=V_hx\delta_e.
\]
Also \(\|a_j\|\le\|x\|\). Every \(a_j\in M\) commutes with every right translation. For \(t\in G\), \(\delta_t=\rho_{t^{-1}}\delta_e\), hence
\[
(a_j-\tau(x)1)\delta_t
=\rho_{t^{-1}}(a_j-\tau(x)1)\delta_e\longrightarrow0.
\]
It follows on finite-support vectors, and then by the uniform bound on arbitrary vectors, that \(a_j\to\tau(x)1\) strongly. T01 upgrades this to ultraweak convergence.

Traciality makes \(\sigma(a_j)=\sigma(x)\) for every \(j\). Normality and normalization now give
\[
\sigma(x)=\lim_j\sigma(a_j)=\sigma(\tau(x)1)=\tau(x).
\]
Thus \(\tau\) is the unique normal normalized tracial state on \(L(G)\). In fact the same proof shows that a normal linear functional invariant under all group conjugations equals its value at \(1\) times \(\tau\).

Neither T02 nor T03 proves uniqueness among nonnormal tracial states. T03 needs no polynomial-density theorem, trace-class spectral decomposition, projection comparison, or generic finite-factor trace theorem.

<a id="t04a"></a>
## T04a. Polar decomposition from bounded positive inverses

Let \(M\subset B(\mathcal H)\) be a von Neumann algebra and \(x\in M\). The continuous calculus gives \(a=|x|=(x^*x)^{1/2}\in M\). For every \(\xi\),
\[
\|a\xi\|^2=\langle\xi,x^*x\xi\rangle=\|x\xi\|^2.
\]
Thus \(a\xi\mapsto x\xi\) is a well-defined isometry from \(\operatorname{ran}a\) onto \(\operatorname{ran}x\). It extends to an isometry from \(\overline{\operatorname{ran}a}\) onto \(\overline{\operatorname{ran}x}\). Define \(v\) to be that isometry on the first space and zero on its orthogonal complement \(\ker a\), using H01. Then \(x=va\); \(v^*v\) is the projection onto \(\overline{\operatorname{ran}a}\), and \(vv^*\) is the projection onto \(\overline{\operatorname{ran}x}\).

This operator belongs to \(M\). For \(\varepsilon>0\), put
\[
v_\varepsilon=x(a+\varepsilon1)^{-1}\in M.
\]
The inverse belongs to \(M\) by H01 and the positive-inverse argument of H02. The continuous calculus and the C*-identity give
\[
\|v_\varepsilon\|^2
=\|a^2(a+\varepsilon1)^{-2}\|
=\max_{s\in\sigma(a)}\frac{s^2}{(s+\varepsilon)^2}\le1.
\]
On \(\ker a\), both \(v_\varepsilon\) and \(v\) vanish. On a vector \(a\xi\),
\[
v_\varepsilon a\xi-x\xi
=-x\varepsilon(a+\varepsilon1)^{-1}\xi,
\qquad
\|x\varepsilon(a+\varepsilon1)^{-1}\|
=\max_{s\in\sigma(a)}\frac{s\varepsilon}{s+\varepsilon}\le\varepsilon.
\]
Hence \(v_\varepsilon\to v\) strongly on the dense sum of \(\operatorname{ran}a\) and \(\ker a\), and then on all of \(\mathcal H\), by the uniform norm bound. Strong closedness puts \(v\) in \(M\). This proves the polar decomposition and both its support projections without an unbounded-operator theorem. A bounded operator whose initial projection \(v^*v\) is a projection is called a partial isometry; its final projection is \(vv^*\).

<a id="t04b"></a>
## T04b. Trace bounds for joins of projections

Let \(\tau\) be a faithful normalized trace on \(M\), and suppose it preserves bounded increasing positive suprema. For projections \(p,q\in M\), let \(p\vee q\) be the projection onto \(\overline{p\mathcal H+q\mathcal H}\). This closed span reduces \(M'\), so its projection belongs to \(M''=M\) by H01. It is the least projection dominating \(p\) and \(q\), by inclusion of ranges.

Apply T04a to \(x=(1-p)q\). Its initial projection is at most \(q\), since \(x\) vanishes on \(q^\perp\mathcal H\). Its final projection is
\[
vv^*=(p\vee q)-p.
\]
Indeed \(p\mathcal H\) is orthogonal to \(\operatorname{ran}x\), and
\[
\overline{p\mathcal H+q\mathcal H}
=p\mathcal H\oplus\overline{\operatorname{ran}(1-p)q}:
\]
one inclusion follows from \(q\xi=pq\xi+(1-p)q\xi\), and the other from \((1-p)q\xi=q\xi-pq\xi\). Traciality and positivity therefore give
\[
\tau(p\vee q)
=\tau(p)+\tau(vv^*)
=\tau(p)+\tau(v^*v)
\le\tau(p)+\tau(q).
\tag{36}
\]

For countably many projections \((e_j)\), their finite initial joins increase to the projection onto the closed span of all their ranges. To see the supremum and strong convergence directly, each vector in this span is approximated by vectors in finite sums of those ranges; the finite-join projections eventually fix each such approximant, and all these projections have norm at most one. On the orthogonal complement they are zero. Thus the limit is that closed-span projection, denoted \(\bigvee_j e_j\), and it belongs to \(M\). Induction in (36) and order normality of \(\tau\) yield
\[
\tau\left(\bigvee_j e_j\right)\le\sum_j\tau(e_j).
\tag{37}
\]
The sum may be infinite; the assertion is useful when it is finite. For the canonical group trace, the required order normality and faithfulness were proved in G01.

<a id="t04c"></a>
## T04c. Order-normal functionals and bounded trace-square convergence

A positive linear functional \(\sigma\) is order normal if \(\sigma(y_i)\uparrow\sigma(y)\) whenever \(0\le y_i\uparrow y\) is bounded. Let \(\tau\) satisfy T04b. We prove that for every operator-norm-bounded sequence \((x_j)\) in \(M\),
\[
\tau(x_j^*x_j)\longrightarrow0
\quad\Longrightarrow\quad
\sigma(x_j)\longrightarrow0.
\tag{38}
\]
Here \(\sigma\) is any positive order-normal functional; ultraweak continuity of \(\sigma\) is not assumed.

First we need a spectral cutoff whose projection is constructed by H02. For \(a\ge0\) and \(c>0\), let
\[
b=(a-c1)_+,\qquad e=1-P_{\ker b}.
\]
The positive part is the continuous function \(s\mapsto\max(s-c,0)\) of \(a\); H02 puts its support projection \(e\) in \(M\). The resolvents of \(b\) commute with \(a\), so \(e\) does too. On \(\operatorname{ran}b\), the quadratic form of \(a-c1\) is nonnegative because \(b(a-c1)b\) is the continuous function \((s-c)\max(s-c,0)^2\ge0\) of \(a\). By continuity the same holds on its closure, \(e\mathcal H\). On \((1-e)\mathcal H=\ker b\), the identity
\[
a-c1=(a-c1)_+-(c1-a)_+
\]
gives \(a\le c1\). If \(\|a\|\le C^2\), these two reducing blocks imply
\[
a\ge ce,\qquad
a\le C^2e+c1,\qquad
\tau(e)\le\tau(a)/c.
\tag{39}
\]
Every positivity assertion here uses H02's spectral-to-quadratic-form bridge.

Assume first that \(\|x_j\|\le C\) and \(\tau(x_j^*x_j)\le2^{-4j}\). Apply (39) to \(a_j=x_j^*x_j\) and \(c_j=2^{-2j}\), obtaining projections \(e_j\) with
\[
\tau(e_j)\le2^{-2j},\qquad
a_j\le C^2e_j+2^{-2j}1.
\]
Let \(q_k=\bigvee_{j\ge k}e_j\). By (37),
\[
\tau(q_k)\le\sum_{j\ge k}2^{-2j}\longrightarrow0.
\]
These projections decrease. Their strong limit is the projection onto \(\bigcap_k q_k\mathcal H\): apply the increasing-projection argument to \(1-q_k\), or use H01 on the orthogonal closed span. Order normality of \(\tau\), applied to \(1-q_k\), shows that the limit projection has trace zero; faithfulness makes it zero. Thus \(1-q_k\uparrow1\). Order normality of \(\sigma\) gives \(\sigma(q_k)\downarrow0\). Since \(e_j\le q_j\),
\[
0\le\sigma(a_j)
\le C^2\sigma(q_j)+2^{-2j}\sigma(1)\longrightarrow0.
\]
Positive-functional Cauchy–Schwarz gives
\[
|\sigma(x_j)|^2\le\sigma(1)\sigma(x_j^*x_j)\longrightarrow0.
\]
For completeness, that inequality follows by expanding \(\sigma((1+zx)^*(1+zx))\ge0\) and minimizing over complex \(z\); the zero diagonal case follows by varying the phase and magnitude of \(z\), just as in H02's positive-form proof. Positivity also makes \(\sigma(x^*)=\overline{\sigma(x)}\): self-adjoint elements are differences of positive elements by the continuous positive/negative-part calculus, so they have real values; decomposing \(x\) into its self-adjoint real and imaginary parts gives the assertion. The order bound \(x^*x\le\|x\|^2 1\) then shows \(|\sigma(x)|\le\sigma(1)\|x\|\), so \(\sigma\) is bounded.

For a general uniformly bounded sequence with \(\tau(x_j^*x_j)\to0\), suppose (38) failed. Some subsequence would have \(|\sigma(x_j)|\ge\delta>0\). Choose a further subsequence whose \(r\)-th trace square is at most \(2^{-4r}\). The argument just proved makes its \(\sigma\)-values tend to zero, a contradiction. This proves (38) for the whole original sequence.

<a id="t04"></a>
## T04. Order-normal group traces and abstract isomorphisms

Let \(G\) be a countable ICC group, \(M=L(G)\), and \(\sigma\) a normalized order-normal tracial state on \(M\). For \(x\in M\), T03 constructs finite convex averages \(a_j\) of group-unitary conjugates of \(x\), with \(\|a_j\|\le\|x\|\) and
\[
\|(a_j-\tau_M(x)1)\delta_e\|\longrightarrow0.
\]
By G02 this is trace-square convergence. T04c therefore gives \(\sigma(a_j-\tau_M(x)1)\to0\). Traciality makes \(\sigma(a_j)=\sigma(x)\), and normalization makes \(\sigma(\tau_M(x)1)=\tau_M(x)\). Consequently
\[
\sigma(x)=\tau_M(x)\qquad(x\in M).
\tag{40}
\]
Thus the canonical group trace is the unique normalized order-normal trace. The preceding argument used positivity and order normality, rather than assuming ultraweak continuity of \(\sigma\).

Now let \(\theta:M\to N\) be an abstract surjective \(*\)-isomorphism between the two countable ICC group factors occurring in the double-coset lesson. Surjectivity makes it unital. It preserves and reflects positivity, since a positive element is a square \(y^*y\). It is isometric as well: it preserves invertibility and spectra, F04 gives norm equals spectral radius for self-adjoint elements, and the C*-identity gives
\[
\|\theta(x)\|^2
=\|\theta(x^*x)\|=\|x^*x\|=\|x\|^2.
\]
As an order isomorphism it preserves every bounded increasing positive supremum. Indeed, if \(y_i\uparrow y\), then \(\theta(y)\) is an upper bound of the images; any other upper bound pulls back to an upper bound of all \(y_i\), so it dominates \(\theta(y)\). The canonical trace on \(N\) is order normal by G01. Therefore
\[
\sigma=\tau_N\circ\theta
\]
is a normalized positive order-normal tracial state on \(M\). Equation (40) proves
\[
\tau_N\circ\theta=\tau_M.
\tag{41}
\]
This supplies trace preservation under the original abstract-isomorphism hypothesis. T08 then constructs its trace-space unitary and transports the MASA complement. The proof needs no prior general theorem equating order normality with ultraweak continuity.

The range-isometry construction in T04a is the bounded polar-decomposition argument in Richard Melrose, [*18.102, Chapter 3*, Proposition 3.19, printed pages 100–102](https://math.mit.edu/~rbm/18-102-S18/Chapter3.pdf). The resolvent limit above also proves membership in the algebra. The projection \((1-p)q\) in T04b, the trace bound for joins, the summable tails in T04c and the order-isomorphism argument in T04 are standard methods found in Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, Proposition 2.4.5, Corollary 2.5.9 and Lemmas 7.2.6–7.2.7, printed pages 37, 44 and 104–105](https://www.math.ucla.edu/~popa/Books/IIunV15.pdf). T04c supplies the bounded trace-square continuity needed here using the positive-part and support constructions already proved in H02.

<a id="t05a"></a>
## T05a. Character separation from the Banach spectrum

Let \(D\ne0\) be a unital commutative complex C*-algebra. A character means a unital complex linear multiplicative map \(\chi:D\to\mathbb C\). We prove that such maps are bounded and preserve adjoints, and that for each \(d\in D\setminus\{0\}\) there is a character with \(|\chi(d)|=\|d\|\). In particular characters separate elements.

The spectral inputs are Infinite tensor products, F03 (Neumann inversion; nonempty compact spectrum in a nonzero unital complex Banach algebra with normalized unit; spectral norm bound), F04 (real self-adjoint spectra and the norm spectral-radius equality for normal elements), and F08 (\(d^*d\) has nonnegative spectrum). These are the spectral/calculus inputs to the proof. All ideal and quotient steps used here are supplied below.

<a id="cs01"></a>
## CS01. Maximal ideals are closed

An ideal here is a complex linear algebraic ideal. Every proper ideal \(J\) is contained in a maximal proper ideal. Indeed, order the proper ideals containing \(J\) by inclusion. The union of a chain is an ideal: any two of its elements lie together in one ideal of the chain, so their sum lies there, and multiplication by any element of \(D\) preserves membership. The union remains proper, because if it contained \(1\), one member of the chain would contain \(1\) and equal \(D\). Zorn's lemma therefore supplies a maximal proper ideal \(I\).

The norm closure \(\overline I\) is an ideal. For example, if \(a_j\in I\) and \(a_j\to a\), then for any \(b\in D\), \(ba_j\to ba\), by \(\|b(a_j-a)\|\le\|b\|\|a_j-a\|\); closure is also a complex linear subspace. This closure is proper. Otherwise it would contain \(1\), and some \(i\in I\) would satisfy \(\|1-i\|<1\). The Neumann series from F03 then makes \(i=1-(1-i)\) invertible. Multiplying \(i\in I\) by its inverse would put \(1\) in \(I\), contradicting properness. Maximality now gives \(\overline I=I\). Thus every maximal proper ideal is norm closed.

<a id="cs02"></a>
## CS02. The quotient is a complete normalized Banach algebra

Let \(I\) be a closed proper ideal. Give \(Q=D/I\) the quotient norm
\[
\|a+I\|_Q=\inf_{i\in I}\|a+i\|.
\]
This is independent of the representative. It is nonnegative, is homogeneous, and satisfies the triangle inequality by adding representatives whose norms approach their respective infima. If \(\|a+I\|_Q=0\), there are \(i_j\in I\) with \(a+i_j\to0\), and closedness gives \(a\in I\). Hence it is a norm. The quotient map \(\pi:D\to Q\) is contractive.

The algebra multiplication \((a+I)(b+I)=ab+I\) is well defined, since changing either representative changes the product by an element of \(I\). For every \(i,j\in I\),
\[
\|ab+I\|_Q\le\|(a+i)(b+j)\|
\le\|a+i\|\|b+j\|.
\]
Taking the infimum in each representative separately proves submultiplicativity of the quotient norm.

To prove completeness, let \((q_k)\) be a Cauchy sequence in \(Q\). Select a subsequence \((q_{k_j})\) with
\[
\|q_{k_{j+1}}-q_{k_j}\|_Q<2^{-j}\qquad(j\ge1).
\]
For each \(j\), the definition of the quotient norm supplies a lift \(b_j\in D\) of this difference with \(\|b_j\|<2^{1-j}\). Choose any lift \(a\) of \(q_{k_1}\). The series \(a+\sum_{j\ge1}b_j\) converges to an element \(b\in D\), because \(D\) is complete and the sum of the norm bounds is finite. For every \(r\),
\[
\pi\left(a+\sum_{j=1}^{r}b_j\right)=q_{k_{r+1}}.
\]
Contractivity of \(\pi\) shows that this subsequence converges to \(\pi(b)\). The full sequence does too: given \(\varepsilon>0\), take a Cauchy tail in which all pairwise distances are below \(\varepsilon/2\), and a subsequence term in that tail at distance below \(\varepsilon/2\) from \(\pi(b)\). The triangle inequality bounds every later term's distance from \(\pi(b)\) by \(\varepsilon\).

The quotient is nonzero and its unit is \(1+I\). The C*-identity in \(D\) implies \(\|1\|=1\), since \(\|1\|^2=\|1\|\) and \(1\ne0\). Thus \(\|1+I\|_Q\le1\). If its quotient norm were below \(1\), some \(i\in I\) would have \(\|1+i\|<1\). F03 would then make \(-i=1-(1+i)\) invertible, again contradicting properness of \(I\). Therefore \(\|1+I\|_Q=1\). We have proved that \(Q\) is a nonzero unital complex Banach algebra with normalized unit, exactly as required to apply F03.

<a id="cs03"></a>
## CS03. The maximal quotient consists of scalars

Suppose now that \(I\) is maximal proper. Every nonzero element \(a+I\) of \(Q\) is invertible. In fact \(a\notin I\), so the ideal \(I+aD\) strictly contains \(I\) and must be \(D\). Consequently \(1=i+ab\) for some \(i\in I\), \(b\in D\), and
\[
(a+I)(b+I)=1+I.
\]
Commutativity gives the inverse on both sides.

Fix \(q\in Q\). Its spectrum in \(Q\) is nonempty by F03, applied to the complete normalized Banach algebra of CS02. Choose \(\lambda\) in that spectrum. The element \(\lambda1_Q-q\) is not invertible. Since every nonzero element of \(Q\) is invertible, it must be zero. Thus \(q=\lambda1_Q\). This scalar \(\lambda\) is unique because \(1_Q\ne0\).

The map \(\alpha:Q\to\mathbb C\), defined by \(\alpha(\lambda1_Q)=\lambda\), is therefore a unital complex linear algebra isomorphism. Composing with the quotient map gives a character \(\chi_I=\alpha\circ\pi\) of \(D\), whose kernel is exactly \(I\). This proves the needed scalar-quotient assertion directly from nonemptiness of the Banach-algebra spectrum.

<a id="cs04"></a>
## CS04. Characters are bounded and preserve adjoints

For any character \(\chi\) and any \(a\in D\), the scalar \(\chi(a)\) belongs to \(\sigma_D(a)\). If \(a-\chi(a)1\) had an inverse \(b\), applying the unital multiplicative map \(\chi\) to \((a-\chi(a)1)b=1\) would give \(0=1\). F03's spectral norm bound therefore gives
\[
|\chi(a)|\le\|a\|.
\]
Thus \(\chi\) is bounded with norm at most \(1\), and \(\chi(1)=1\) makes its norm exactly \(1\).

If \(h=h^*\), F04 gives a real spectrum, so \(\chi(h)\in\mathbb R\). For arbitrary \(a\), put
\[
h=\frac{a+a^*}{2},\qquad
k=\frac{a-a^*}{2i}.
\]
Then \(h,k\) are self-adjoint, \(a=h+ik\), and \(a^*=h-ik\). Complex linearity and the real values of \(\chi(h)\), \(\chi(k)\) give
\[
\chi(a^*)=\chi(h)-i\chi(k)=\overline{\chi(a)}.
\]
Every character is consequently a bounded unital *-homomorphism. The quotient argument did not need to assume in advance that an algebraic maximal ideal is closed under adjoints; the adjoint assertion is a consequence of this proof.

<a id="cs05"></a>
## CS05. Characters detect the norm and separate elements

Fix \(d\ne0\), and put \(h=d^*d\). The C*-identity gives \(\|h\|=\|d\|^2>0\). By F08, \(h\) has nonnegative spectrum; by F04, its spectral radius is \(\|h\|\). F03 gives compactness and attainment of the maximum spectral modulus. It follows that
\[
t=\|h\|=\|d\|^2\in\sigma_D(h).
\]
The principal ideal \(J=(h-t1)D\) is proper. Indeed, if it contained \(1\), we would have \((h-t1)b=1\) for some \(b\in D\), and commutativity would make \(b\) a two-sided inverse of \(h-t1\), contradicting \(t\in\sigma_D(h)\).

By CS01, choose a maximal proper ideal \(I\) containing \(J\). The character \(\chi_I\) constructed in CS03 vanishes on \(h-t1\), hence \(\chi_I(h)=t\). CS04 gives
\[
|\chi_I(d)|^2
=\chi_I(d^*)\chi_I(d)
=\chi_I(d^*d)
=t=\|d\|^2.
\]
Thus \(|\chi_I(d)|=\|d\|>0\). Applying the bound in CS04 to all characters, and this norm-detecting character to each nonzero \(d\), proves
\[
\|d\|=\sup_{\chi}|\chi(d)|\qquad(d\in D).
\]
Characters exist, since the proper ideal \(\{0\}\) can be used in CS01-CS03. For \(d=0\), both sides of the norm identity are zero. If two elements have equal values at every character, apply norm detection to their difference; they must be equal.

<a id="cs06"></a>
## CS06. The exact finite-matrix consequence

For finite \(n\ge1\), apply a character entrywise to obtain
\[
\chi_n:M_n(D)\longrightarrow M_n(\mathbb C),
\qquad \chi_n((a_{ij}))=(\chi(a_{ij})).
\]
Complex linearity, multiplicativity, unitality and preservation of adjoints follow entrywise from CS04 and the finite matrix multiplication formula. Scalar-entry matrices show that \(\chi_n\) is onto. If \(\chi_n(T)=0\) for every character, every entry of \(T\) vanishes by CS05, so \(T=0\). These are precisely the character properties used in T05's rank and central-support proof. The result concerns the finite matrices and requires no normality assertion about characters.

<a id="t05"></a>
## T05. Finite matrices over an abelian algebra

Let \(D\ne0\) be a unital abelian C*-algebra and let \(n\ge1\) be finite. The character-separation proof in [T05a](#t05a) gives unital \(*\)-characters \(\chi:D\to\mathbb C\) which separate elements. Only separation and \(*\)-preservation are used below.

Entrywise evaluation defines a surjective \(*\)-homomorphism
\[
\chi_n:M_n(D)\longrightarrow M_n(\mathbb C).
\]
Surjectivity follows by using scalar entries. Characters separate matrices, since they separate every entry.

The center of \(M_n(D)\) is \(D1_n\). Indeed an element commuting with all constant matrix units has zero off-diagonal entries and equal diagonal entries; conversely \(d1_n\) commutes with every matrix because \(D\) is abelian. In particular \(e_{11}\) is an abelian projection: \(e_{11}M_n(D)e_{11}\cong D\). It has full central support, since a central projection \(z1_n\) satisfying \((z1_n)e_{11}=e_{11}\) must have \(z=1\). All diagonal matrix projections have these properties and are mutually equivalent through the matrix units.

Every isometry \(v\in M_n(D)\) is unitary. For every character, \(\chi_n(v)^*\chi_n(v)=1_n\); an isometry on a finite-dimensional space is onto, so \(\chi_n(v)\chi_n(v)^*=1_n\). Character separation gives \(vv^*=1_n\). Thus this matrix algebra is finite, by the intrinsic definition that its unit is not equivalent to a proper subprojection.

Now let \(p\in M_n(D)\) be an abelian projection with full central support. Put \(p_\chi=\chi_n(p)\). Evaluating the corner is onto \(p_\chi M_n(\mathbb C)p_\chi\): any matrix in the latter corner is \(p_\chi Bp_\chi\), the evaluation of \(pBp\) with constant matrix \(B\). Since \(pM_n(D)p\) is commutative, this matrix corner is commutative. A matrix corner of rank \(r\) is \(M_r(\mathbb C)\), by choosing an orthonormal basis of its range, and is commutative only for \(r\le1\). Therefore \(\operatorname{rank}p_\chi\in\{0,1\}\).

Rank zero cannot occur even at a nonnormal character. Put \(t=\sum_{i=1}^np_{ii}\in D\). Then \(\chi(t)=\operatorname{rank}p_\chi\). The element
\[
z=\prod_{k=1}^n(1-t/k)\in D
\]
has character value \(1\) when that rank is zero and \(0\) for every positive possible rank. Hence character separation gives \(z=z^*=z^2\), so \(z1_n\) is a central projection. Entrywise evaluation also gives \((z1_n)p=0\). Full central support forces \(z=0\). If any character had rank zero, it would have \(\chi(z)=1\), contradicting \(z=0\). Consequently every \(p_\chi\) has rank exactly one.

Suppose \(p_1,\ldots,p_k\) are mutually orthogonal abelian projections of full central support, with \(\sum_{i=1}^kp_i=1_n\). Evaluating at any character gives \(k\) orthogonal rank-one projections summing to the identity of \(\mathbb C^n\). Thus \(k=n\). There cannot be an infinite family of such projections: any \(n+1\) of them would already evaluate to \(n+1\) orthogonal rank-one projections in \(\mathbb C^n\).

This is the intrinsic finite matrix-size argument. Equivalence of the projections is allowed, and holds for the standard diagonal family, but does not need to be assumed in the last counting argument. Character evaluation was used only on finite sums; no character was assumed normal and no character was applied to an infinite von Neumann sum.

<a id="t06"></a>
## T06. Finite versus countably infinite multiplicity

Let \(D,E\ne0\) be unital abelian von Neumann algebras, and let \(n,m\) be positive integers or countable infinity. Consider
\[
D\,\bar\otimes\,B(\ell^2(n)),\qquad
E\,\bar\otimes\,B(\ell^2(m)).
\]
When \(n\) is finite, the first algebra is \(M_n(D)\), and T05 proves it finite. When \(n=\infty\), let \(S\delta_j=\delta_{j+1}\) on \(\ell^2(\mathbb N)\). Then
\[
(1_D\otimes S)^*(1_D\otimes S)=1,
\qquad
(1_D\otimes S)(1_D\otimes S)^*=1-1_D\otimes e_{11}\ne1.
\]
It contains a proper isometry, so it is not finite. An abstract \(*\)-isomorphism preserves the relations defining an isometry and a unitary; consequently the finite and infinite cases cannot be isomorphic.

If both \(n,m\) are finite, an isomorphism sends the \(n\) standard diagonal projections of \(M_n(D)\) to mutually orthogonal abelian projections of full central support summing to \(1\) in \(M_m(E)\). These properties are intrinsic: a \(*\)-isomorphism sends centers onto centers, sends corners isomorphically to corners, and preserves projection order. Full central support means that the only central projection dominating the projection is \(1\), an assertion preserved by an order isomorphism. T05 in \(M_m(E)\) therefore gives \(n=m\). If both are countably infinite then their multiplicity parameters already coincide. These arguments prove preservation of the exact parameter needed in the double-coset lesson without a general type-I classification theorem or projection comparison.

<a id="t07"></a>
## T07. The type-II1 bridge in the affine proposition

H04 proves that a factor with a faithful normalized trace and a nonzero minimal projection is a finite matrix algebra. The following short argument makes its final type assertion valid with the intrinsic type definition using abelian projections.

For any nonzero projection \(r\) in a factor \(M\), the closed span of the ranges \(uru^*\), over all unitaries \(u\in M\), has a nonzero central projection as its orthogonal projection, by exactly the central-support argument of H04. That projection is \(1\). If \(q\ne0\) is another projection and \(qMr=0\), then \(qur=0\) for every such unitary, so \(q\) vanishes on this dense span, a contradiction. Thus \(qMr\ne0\) whenever \(q,r\ne0\).

If a nonzero projection \(e\) has commutative corner \(eMe\), and \(0<q<e\), put \(r=e-q\). Then \(q,r\ne0\), but for every \(x\in M\),
\[
qxr=q(exe)r=0,
\]
because \(q\) and \(r\) are orthogonal projections in the commutative corner. This contradicts \(qMr\ne0\). Hence every nonzero abelian projection in a factor is minimal. H04 consequently shows that an infinite-dimensional factor with a faithful normalized trace has no nonzero abelian projections.

A faithful trace also proves finiteness directly. If \(v^*v=1\), traciality gives \(\tau(1-vv^*)=0\); faithfulness makes \(vv^*=1\). Thus its unit is finite, it has no nonzero abelian projection, and its only nonzero central projection \(1\) itself is a nonzero finite projection. These are exactly the intrinsic definition of type \(\mathrm{II}_1\). For an infinite ICC group, the group unitaries are linearly independent (apply a finite linear combination to \(\delta_e\)), so its faithful tracial factor is infinite dimensional and the argument applies. This supplies the type assertion in the original affine Proposition 3.1 without invoking classification.

<a id="t08"></a>
## T08. Transporting the MASA multiplicity block

Let \(\theta:M\to N\) carry one of the two group MASAs onto the other. T04 gives \(\tau_N\theta=\tau_M\). Therefore
\[
U_\theta(x\Omega_M)=\theta(x)\Omega_N
\]
preserves inner products on the dense trace vectors: their inner products are \(\tau_M(x^*y)=\tau_N(\theta(x)^*\theta(y))\). Surjectivity of \(\theta\) makes its range dense, so it extends to a unitary. It intertwines left multiplication and trace conjugation \(J(x\Omega)=x^*\Omega\), and maps the closure of \(A\Omega_M\) onto the closure of \(\theta(A)\Omega_N\). It consequently conjugates the canonical subgroup projection and the left/right-generated commutant, and restricts to an isomorphism of the two complementary commutants.

The already computed complementary commutants are \(D\bar\otimes B(\ell^2(n))\) and \(E\bar\otimes B(\ell^2(m))\). T06 gives \(n=m\). This proves the pair-isomorphism multiplicity assertion using the abstract isomorphism hypothesis.

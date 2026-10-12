# Complete trace commutants and finite-action representation inputs

*Original programme exposition: CC0-1.0 to the extent of rights held.*

The [finite outer-action lesson](../src/finite-outer-actions.md) needs the whole tracial commutant, a faithful normal range with a normal inverse, the central kernel of a normal homomorphism, and the actual matrix-base Bernoulli products. These arguments cover arbitrary Hilbert spaces and finite factors without a separability assumption.

The complete earlier inputs are CF's calculus, Hahn–Banach and Hilbert constructions, CP's concrete preduals, and BD's bounded density, [NT1–2](central-sequence-foundations.md), [PC/FCT](central-finite-trace-inputs.md), [FH0's normal canonical finite-factor trace](fullness-hypercentrality-and-tail-inputs.md#fh0-normality-of-factor-tracial-states), [AF1–5](central-afd-uniqueness-inputs.md), and [SS0–2's finite matrix coordinates and whole tracial products](strong-stability-matrix-and-product-inputs.md). Inner products are linear in the second variable.

<a id="fo0-whole-trace-gns-and-commutant"></a>

## FO0. The entire trace representation and its commutant

Let \(M\) be a nonzero von Neumann algebra with a faithful normal normalized trace \(\tau\). Complete \(M\) under
\(\langle a,b\rangle=\tau(a^*b)\) to \(H_\tau\), with \(\Omega=\widehat1\). Faithfulness makes this a genuine inner product; CF supplies the whole Hilbert completion. Left multiplication \(L_x\) has norm at most \(\|x\|\), because \(x^*x\leq\|x\|^21\), and adjoint \(L_{x^*}\).

It is faithful and isometric. For the lower bound at \(x\ne0\), continuous calculus gives a nonzero positive \(f(x^*x)\) supported in a spectral interval above \(\|x\|^2-\varepsilon\). Faithfulness makes \(\tau(f^2)>0\). Therefore
\[
\|L_x(f\Omega)\|_2^2
=\tau(fx^*xf)\geq(\|x\|^2-\varepsilon)\tau(f^2).
\]
Let \(\varepsilon\downarrow0\). The faithful homomorphism is consequently isometric at every \(x\).

It is normal on its entire domain. Pairings between bounded trace vectors have the form \(\tau(a^*xb)\), normal by CP's fixed-multiplier tests. Approximate arbitrary vectors by bounded trace vectors; the uniform bound \(\|L_x\|\leq\|x\|\) gives predual norm convergence of their coefficient functionals. CP's norm-closed predual makes those limits normal. Finally every normal functional on \(B(H_\tau)\) is a summable vector-pair series; norm convergence gives the same conclusion for its composition with \(L\). FO1 below then proves that \(L(M)\) is a von Neumann algebra and that its faithful normal identification with \(M\) has a whole normal inverse.

Right multiplication \(R_b(a\Omega)=ab\Omega\) is bounded with norm at most \(\|b\|\), using the trace to write
\(\tau(b^*a^*ab)=\tau(a^*abb^*)\leq\|b\|^2\tau(a^*a)\).
Its adjoint is \(R_{b^*}\), and it commutes with every left multiplier. We prove that these are all operators in \(L(M)'\), including on the entire Hilbert completion.

Fix \(T\in L(M)'\), put \(\xi=T\Omega\), and \(C=\|T\|\). For \(a=v|a|\), its bounded polar decomposition from PC1, adjoint identities and commutation give
\[
\begin{aligned}
|\langle a\Omega,\xi\rangle|
&=|\langle |a|^{1/2}\Omega,
T(|a|^{1/2}v^*\Omega)\rangle|\\
&\leq C\,\tau(|a|).
\end{aligned}
\tag{FO0.1}
\]
The two vector square norms are both \(\tau(|a|)\): the second uses
\(\tau(v|a|v^*)=\tau(|a|v^*v)=\tau(|a|)\).

The convex set
\[
\mathcal B_C=\{b\Omega:b\in M,\ \|b\|\leq C\}
\]
is weakly compact in \(H_\tau\). Indeed CP/CF makes the operator ball ultraweakly compact; every bounded-vector coefficient \(\tau(a^*b)\) is normal. Approximation of an arbitrary Hilbert test by bounded trace vectors, with the uniform vector norm bound \(C\), makes this ball-to-Hilbert map weakly continuous. Thus its image is compact in the Hausdorff weak Hilbert topology, hence weakly closed and norm closed.

For each bounded trace vector, its support functional on this ball is exactly
\[
\sup_{\|b\|\leq C}\operatorname{Re}\langle a\Omega,b\Omega\rangle
=C\tau(|a|).
\tag{FO0.2}
\]
The upper bound follows from the positive functional \(z\mapsto\tau(|a|z)\), whose norm is \(\tau(|a|)\), tested on \(v^*b\). Its positivity follows by the trace and positive half powers; NT1 gives the stated norm. Equality holds at \(b=Cv\), including \(a=0\).

FO0.1–2 imply that every bounded trace test of \(\xi\) is at most the corresponding support functional of \(\mathcal B_C\). Approximate any Hilbert test by these dense vectors; both the pairing with \(\xi\) and the support functional change by at most \(C\) times that approximation error. The inequality therefore holds for every Hilbert vector.

Here is the complete separation argument needed to conclude membership. The Hilbert norm is weakly lower semicontinuous by
\(\|\zeta\|=\sup_{\|\eta\|\leq1}|\langle\eta,\zeta\rangle|\), with equality tested at a normalized \(\zeta\). Nested nonempty distance sublevel sets in the weakly compact \(\mathcal B_C\) consequently supply a closest point \(b_0\) to \(\xi\). If \(\xi\notin\mathcal B_C\), put \(\eta=\xi-b_0\ne0\). For every \(b\in\mathcal B_C\), convexity and minimality at \(b_0+t(b-b_0)\) give
\[
0\leq-2t\operatorname{Re}\langle\eta,b-b_0\rangle
+t^2\|b-b_0\|^2.
\]
Dividing by \(t>0\) and decreasing \(t\) to zero yields
\(\operatorname{Re}\langle\eta,b\rangle\leq\operatorname{Re}\langle\eta,b_0\rangle\).
But \(\operatorname{Re}\langle\eta,\xi\rangle=\operatorname{Re}\langle\eta,b_0\rangle+\|\eta\|^2\), contradicting the support-functional inequality for this \(\eta\). Hence \(\xi=b\Omega\) for some \(\|b\|\leq C\). At \(C=0\) this conclusion is immediate.

Now \(T(a\Omega)=aT\Omega=ab\Omega=R_b(a\Omega)\) on the dense bounded trace vectors. Both operators are bounded, so \(T=R_b\) on all \(H_\tau\). Thus
\[
L(M)'=\{R_b:b\in M\}.
\tag{FO0.3}
\]
The trace rule makes \(J(a\Omega)=a^*\Omega\) antiunitary, with \(J^2=1\). Direct evaluation gives \(JL_xJ=R_{x^*}\); FO0.3 therefore gives \(JL(M)J=L(M)'\). It also gives \(JL(M)'J=L(M)\), on the whole space. The right algebra is the normal faithful representation of \(M^{\mathrm{op}}\): its bounded coefficients are normal trace multiplier functionals, and the same full vector-series argument proves normality. Its vector trace is faithful normal and tracial. Factoriality and the presence or absence of abelian corners transfer through this opposite-algebra identification.

<a id="fo1-full-normal-faithful-range-and-inverse"></a>

## FO1. A faithful normal representation has a whole normal inverse

Let \(A\) be any von Neumann algebra and \(\pi:A\to B(K)\) a faithful normal star representation, possibly with proper identity projection \(p=\pi(1)\). Work first on \(pK\). The map is isometric: contractivity is the C* estimate from CF; if a positive element lost norm, a continuous function zero on \([0,\|\pi(a)\|]\) but nonzero at \(\|a\|\) would give a nonzero \(f(a)\) in its kernel. Choose \(f(0)=0\), so this argument also covers a proper identity corner. The C* identity gives isometry for every element.

The unit ball of \(\pi(A)\) is the normal image of the compact ultraweak unit ball of \(A\), hence compact and ultraweakly closed. The image is a norm-closed C* algebra. BD supplies bounded strong approximants from its unit ball to every contraction in its bicommutant on \(pK\), and its vector-series tail argument gives ultraweak convergence. Compact-ball closedness puts each such limit back in \(\pi(A)\). Thus the image is the entire bicommutant and is a von Neumann algebra. In \(B(K)\) all its ultraweak limits remain compressed by \(p\), giving the same conclusion there.

On these unit balls \(\pi\) is a continuous bijection from a compact space to a Hausdorff space. Images of closed subsets are compact and closed, so its inverse is continuous on the ball. To obtain the entire-domain normal inverse, prove the required linear criterion rather than assuming convergence of arbitrary nets is norm bounded.

Let \(E\) be Banach, \(X=E^*\), and \(\lambda\in X^*\) weak-star continuous at zero on \(B_X\). For \(\varepsilon>0\), finitely many tests \(e_j\in E\) and a positive tolerance make \(|\lambda(x)|\leq\varepsilon\) on the unit ball with all those tests zero. Put \(F=\bigcap_j\ker e_j\). Thus \(\|\lambda|_F\|\leq\varepsilon\). CF's Hahn–Banach theorem extends this restriction to \(h\in X^*\) with \(\|h\|\leq\varepsilon\). The functional \(\lambda-h\) factors through the finite-dimensional coordinate map \(x\mapsto(e_j(x))_j\), so it is a finite linear combination of the \(e_j\)'s. Therefore the distance of \(\lambda\) from \(E\) is at most \(\varepsilon\). The canonical copy of \(E\) in \(E^{**}\) is isometric by the norming Hahn–Banach identity and closed by completeness. Letting \(\varepsilon\) decrease to zero proves \(\lambda\in E\).

For each \(\psi\in A_*\), apply this criterion to the bounded linear \(\psi\pi^{-1}\) on the concrete dual \(\pi(A)=(\pi(A)_*)^*\). Ball inverse continuity proves the hypothesis, so \(\psi\pi^{-1}\) is normal. This holds for every normal test and proves whole-domain ultraweak continuity of the inverse. Both directions consequently preserve positive normal-functional square tests as well. No separability, countability or arbitrary-weight theorem has been used.

<a id="fo2-whole-central-kernel-of-a-normal-homomorphism"></a>

## FO2. The central projection of a closed kernel

Let \(I\) be an ultraweakly closed two-sided star ideal in a von Neumann algebra \(A\). For \(a\in I_+\), the contractions \(a(a+1/n)^{-1}\) belong to \(I\) and converge strongly to \(s(a)\), the support projection. On the kernel they vanish; on a vector \(a\xi\), their error from the identity is \((1/n)(a+1/n)^{-1}a\xi\), of norm at most \(\|\xi\|/n\). Their common bound and density in the support range give the whole strong limit, exactly as in PC1's support construction. Bounded strong convergence is ultraweak by CP/BD, so \(s(a)\in I\).

The join of two projections of \(I\) is the support of their positive sum: its kernel is exactly the intersection of their kernels. Thus all finite joins remain in \(I\). The net of finite joins of all its projections increases strongly to their supremum \(z\), so \(z\in I\). This net exists without a countability assumption; PC0–1 constructs arbitrary projection joins.

Conjugation by every unitary of \(A\) preserves \(I\) and its largest projection, and therefore fixes \(z\). NT1's four-unitary span makes \(z\) central. For \(x\in I\), the support \(s(x^*x)\leq z\), so \(x=xz=zx\). Conversely \(z\in I\) and the ideal property give \(Az\subseteq I\). Hence
\[
I=Az.
\tag{FO2.1}
\]
The kernel of any normal star homomorphism is such an ideal. On a factor its central projection is zero or one; a nonzero identity image excludes one. Once the kernel is zero, FO1 proves the entire normal range and normal inverse, including if its identity is a proper corner.

<a id="fo3-actual-matrix-base-bernoulli-products"></a>

## FO3. Matrix-base products, coordinate permutations and all index boundaries

For a countably infinite set \(I\), put one \(M_2\), with normalized matrix trace, at every \(i\in I\). A countable enumeration identifies its local finite matrix stages with SS2's complete tracial product; thus its whole normal closure is the separable AFD \(\mathrm{II}_1\) factor \(R_I\cong R\). The Hilbert construction and all product trace inner products are in SS2. Every permutation of \(I\) preserves the local trace vector inner products, so it extends to a Hilbert unitary intertwining the local algebras and their BD closures. CP and the faithful normal GNS inverse make the induced permutation an entire trace-preserving normal automorphism. Composition and inverses are checked on every site, then extend to the whole algebra.

AF1's trace projections onto the increasing finite matrix stages give bounded trace-norm approximation of every \(x\in R_I\). If sites \(i_n\) escape every finite subset, \(Z=\operatorname{diag}(1,-1)\) at \(i_n\), with identities elsewhere, commutes with each finite stage eventually. Therefore its commutator with arbitrary \(x\) has trace norm at most \(2\|x-x_0\|_2\) once \(x_0\) is a chosen local approximant. The adjoint bound is the same; its trace functional commutator is zero. The full tracial centrality criterion makes this sequence ordinary centralizing.

At distinct sites the two \(Z\)-operators are trace-zero unitaries and their mixed trace factors to zero. Their squared distance is exactly \(1+1-2\operatorname{Re}(0)=2\). This supplies both the finite-group repeated-index example and the countably infinite group shift.

For finite nonempty \(H\), use \(I=H\times\mathbb N\). Left multiplication sends \((h,n)\) to \((kh,n)\). The finite matrix stages \(H\times\{1,\ldots,n\}\) are invariant. The \(Z\)'s at \((e,n)\) escape every finite stage, while their translates at \(k\ne e\) are distinct and have squared distance two. An inner automorphism would move the central sequence by a trace-norm-zero difference. Thus every nonidentity group element acts outerly; for the trivial group that assertion is vacuous and the fixed algebra is the whole \(R_I\).

For an infinite countable discrete \(\Gamma\), take \(I=\Gamma\). A left action moves site \(g\) to site \(hg\), hence places \(x_{h^{-1}g}\) at output site \(g\). For fixed \(h\ne e\), choose an increasing finite exhaustion \(F_n\) and \(g_n\notin F_n\cup h^{-1}F_n\). Both \(g_n\) and \(hg_n\) escape every finite set and are distinct, since left multiplication by nonidentity \(h\) has no fixed site. The same trace-zero sequence proves outerness, with no order assumption on \(h\).

If the output instead receives \(x_{hg}\), the site moves to \(h^{-1}g\). These maps are \(\gamma_h=\beta_{h^{-1}}\), and satisfy \(\gamma_h\gamma_k=\gamma_{kh}\). Since the site permutations are faithful, they satisfy the left action law for every pair exactly when the indexing group is abelian.

For a finite index set \(\Gamma\), the bare matrix-base product is one full matrix algebra \(M_{2^{|\Gamma|}}\). Every automorphism is inner: apply the explicit matrix implementation in CT1, or multiply the images of a full matrix-unit system with a single diagonal partial isometry. No escaping sequence exists. It is the repeated \(H\times\mathbb N\) index, not merely a finite group, that gives the infinite outer example.

<a id="fo4-complete-finite-average-and-trace-projection"></a>

## FO4. The finite average and its full Hilbert range

Let a finite \(G\) act normally and trace-preservingly on any nonzero von Neumann algebra with faithful normal normalized trace. Put \(N=M^G\) and \(E=|G|^{-1}\sum_g\alpha_g\). The fixed equations define an ultraweakly closed star subalgebra. Finite summation gives normality, unitality and complete positivity of \(E\). Group reindexing makes its range precisely \(N\), and its restriction there the identity. Fixed elements \(a,b\in N\) give \(E(axb)=aE(x)b\). The trace is preserved; unital Schwarz or the triangle inequality for the trace-implementing unitaries makes it a trace \(2\)-contraction. It is faithful, since \(E(x)\geq x/|G|\) for \(x\geq0\).

On the whole trace Hilbert space the unitaries \(W_g(x\Omega)=\alpha_g(x)\Omega\) give the bounded extension \(P=|G|^{-1}\sum_gW_g\). Inversion permutes \(G\), so \(P^*=P\), and group multiplication gives \(P^2=P\). Its range is exactly the fixed vector space. Moreover \(P(M\Omega)=N\Omega\), and density of \(M\Omega\) makes its entire range \(\overline{N\Omega}=L^2(N)\). This proves the full orthogonal projection assertion, not only a formula on bounded vectors.

The normal map also embeds \(N_*\) isometrically into \(M_*\) by \(\eta\mapsto\eta E\): contraction gives one inequality and restriction to the unit ball that \(E\) fixes gives the other. Its image is closed. Any predual separability conclusion therefore follows when \(M_*\) is separable; otherwise none is implied by this finite averaging step.

# Symbols, finite defects, and the index on a closed manifold

An elliptic symbol describes the directions that an operator can recover at high frequency. The missing directions form a finite-dimensional space, but their number is not usually determined by the symbol at one point. This lesson connects three operations: removing compact errors, moving symbols through invertible maps, and taking products on different manifolds. The analytic estimates come first, so the topological index introduced later does not enter its own proof.

Throughout, \(X\) is a compact Hausdorff second-countable smooth manifold without boundary, and bundles are smooth complex bundles of finite rank. Their ranks may differ in preliminary constructions; every two-sided elliptic symbol below has equal source and target ranks on each positive-dimensional component. Write \(\mathcal E=E\otimes\Omega_X^{1/2}\) and \(\mathcal F=F\otimes\Omega_X^{1/2}\), where \(\Omega_X\) is the density line. Half-densities allow integration without orienting \(X\). Orders \(m,s\) are real. Unless explicitly called continuous, a symbol belongs to the standard estimate class \(S^m=S^m_{1,0}\); it need not have a homogeneous expansion. The notation \(\Psi^m_{\mathrm{cl}}\) additionally requires a polyhomogeneous expansion with leading degree \(m\). The Fourier convention is \(D=-i\partial\).

The analytic tools used here are in [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md), especially Sections 5–6 and 8–9 for matrix composition, adjoints, all-order Sobolev bounds and inversion, and in [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md), especially Sections 4–6, 11 and 13 for assembly, smoothing parametrices, bundle Sobolev spaces and anti-duals. [Finite defects under perturbation](fredholm-stability.md), Sections 2–7, supplies Fredholm composition, compact perturbations, two-sided parametrices and strong families with two collectively compact error families. Section 9 of [Traces that survive passage to cohomology](traces-and-complexes.md) proves a bounded tensor identity used for comparison; the smooth-domain calculation needed here is proved in Section 11.4.

The entry facts are smooth partitions, chart changes and bundle gluing; distributional pairing, restriction and finite order on compact sets; Fourier inversion and Plancherel with distributional Fourier extension; and elementary integration and calculus. For Hilbert spaces we use orthogonal projections, adjoints and Parseval, as developed in [Traces that survive passage to cohomology](traces-and-complexes.md), Section 1. The all-real-order interpolation step uses the annular Fourier proof in [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md), Section 8, with sequence exponent two; Section 10.2 spells out its use here. Finite-bundle compactness, smoothing approximation, order-changing and controlled-quantization adapters are proved below. No K-theoretic or characteristic-class index formula is assumed or concluded.

## 1. Compactness and duality in bundle Sobolev spaces

Choose a finite family of relatively compact bundle charts, smooth local frames, and cutoffs \(\chi_j\) such that \(\sum_j\chi_j^2=1\). One construction starts with nonnegative subordinate functions \(\rho_j\) whose sum is positive and sets \(\chi_j=\rho_j/(\sum_k\rho_k^2)^{1/2}\). A smooth Hermitian metric is obtained by adding the local metrics with a partition of unity. Define \(H^s(X;\mathcal E)\) by the finite sum of local \(H^s(\mathbb R^n)\) norms of \(\chi_j u\), expressed as vector-valued half-density components and extended by zero. [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md) proves equivalence of these norms under changes of frame, charts, and cutoffs. Completion can equally be taken inside distributions: the local limits agree on overlaps, because multiplication and coordinate changes are continuous. Thus the spaces are Hilbert, smooth sections are dense, and
\[
\bigcap_{s\in\mathbb R}H^s(X;\mathcal E)=C^\infty(X;\mathcal E),
\qquad
\bigcup_{s\in\mathbb R}H^s(X;\mathcal E)=\mathcal D'(X;\mathcal E).
\tag{I1}
\]
For the first equality, in each chart Cauchy–Schwarz gives absolute convergence of the differentiated inverse Fourier integral when \(s>k+n/2\), hence \(k\) continuous derivatives. Conversely a compact smooth section has rapidly decreasing local Fourier transforms. For the second, the finite-order distribution bound on each of the finitely many chart supports bounds the local Fourier transform by a polynomial; it is consequently square integrable after multiplication by a sufficiently negative Sobolev weight. A common negative order works for all charts. Density follows by local convolution and cutoffs, first for each of the finitely many local components and then by summing.

For every \(\delta>0\), the inclusion
\[
H^{s+\delta}(X;\mathcal E)\longrightarrow H^s(X;\mathcal E)
\quad\text{is compact.}
\tag{I2}
\]
Here is a local proof that includes negative \(s\). For a distribution \(v\) supported in a fixed compact chart set, let \(L_R\) be the Fourier multiplier \(\psi(\xi/R)\), with \(\psi=1\) near zero and compactly supported. Then
\(\|(I-L_R)v\|_{H^s}\leq C R^{-\delta}\|v\|_{H^{s+\delta}}\).
Choose compact smooth \(\theta\) equal to one on that support. The same estimate after multiplication by \(\theta\) bounds \(v-\theta L_Rv\). On this support the latter operator has the smooth compactly supported kernel
\(\theta(x)\check\psi_R(x-y)\theta_1(y)\), where \(\theta_1=1\) on the input support. Any such kernel gives a compact map between any two fixed Sobolev spaces. To verify this claim, enclose its support in two cubes, extend it smoothly and periodically by zero in larger cubes, and expand in a double Fourier series. Integration by parts gives coefficients decreasing faster than every power of both indices. Each finite sum is a finite-rank kernel with smooth input and output functions; Cauchy–Schwarz with the fixed Sobolev weights bounds the operator-norm tail by a convergent weighted square sum. The kernel is therefore an operator-norm limit of finite-rank maps. Letting \(R\to\infty\) proves local compactness, and finitely many charts prove (I2). The same argument proves that a smooth bundle kernel is compact between all fixed Sobolev spaces and can be approximated there by smooth finite-rank kernels.

The anti-dual bundle \(E^*\) consists of conjugate-linear functionals on \(E\). As in [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md), use \(\langle u,v\rangle=\overline{v(u)}\), linear in the first argument and conjugate-linear in the second. Integration identifies the continuous anti-dual of \(H^s(X;\mathcal E)\) with \(H^{-s}(X;E^*\otimes\Omega_X^{1/2})\). Locally, this is the Fourier identity between weighted \(L^2\) spaces: Cauchy–Schwarz proves boundedness, and Hilbert representation gives every bounded functional by a Fourier function with the reciprocal weight. To pass to bundles, localize a functional with cutoffs, use that representation in each frame, and sum the resulting anti-dual sections. The pairing transition law from [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md) makes this construction independent of charts. For a closed subspace of this Hilbert space, orthogonal projection separates every vector outside it by a bounded functional. Indeed its nonzero orthogonal component supplies such a functional by the inner product. Hilbert representation itself follows from the projection theorem: for a nonzero functional, the orthogonal complement of its kernel is one-dimensional, and its value on a unit vector in that line determines the representing vector. Thus a closed subspace is exactly the common nullspace of its annihilating functionals. These statements will determine the correct cokernel space, rather than an adjoint chosen from an unrelated Sobolev inner product.

## 2. The global elliptic alternative

Let \(P\in\Psi^m(X;\mathcal E,\mathcal F)\). Its principal symbol is a class
\[
p\in S^m(T^*X;\operatorname{Hom}(\pi^*E,\pi^*F))/S^{m-1}.
\tag{I3}
\]
It is elliptic when a representative has an inverse at sufficiently large covectors with
\(\|p(x,\xi)^{-1}\|\leq C\langle\xi\rangle^{-m}\), in finitely many bundle charts. Equivalently there is \(q\in S^{-m}\) such that \(qp-I\) and \(pq-I\) lie in \(S^{-1}\). The equivalence follows from matrix inversion and differentiation as in Section 9 of [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md): a one-sided error of norm less than one is invertible, equal finite ranks give a genuine fiber inverse, and repeated differentiation of \(p^{-1}p=I\) gives every inverse-symbol estimate. A cutoff across bounded covectors completes the smooth representative. Both remainders are required as typed bundle maps; the square-matrix algebra explains why either suffices for equal ranks.

Quantize \(q\) using the local construction in Section 4 and the bundle assembly in Section 13 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md). Composition gives \(QP=I-K_E\), \(PQ=I-K_F\), with \(K_E,K_F\in\Psi^{-1}\). In the realizations
\[
P_s:H^s(X;\mathcal E)\longrightarrow H^{s-m}(X;\mathcal F),
\qquad
Q_s:H^{s-m}(X;\mathcal F)\longrightarrow H^s(X;\mathcal E),
\tag{I4}
\]
the errors are compact by (I2). Section 5 of [Finite defects under perturbation](fredholm-stability.md) implies that \(P_s,Q_s\) are Fredholm and have opposite indices. Iterating \(u=K_Eu\) for a nullvector increases its Sobolev order by any positive integer. Thus
\[
N=\ker P_s=\{u\in C^\infty(X;\mathcal E):Pu=0\}
\tag{I5}
\]
is finite-dimensional and independent of \(s\).

The distributional half-density adjoint is
\[
P^*:H^{m-s}(X;F^*\otimes\Omega_X^{1/2})
 \longrightarrow H^{-s}(X;E^*\otimes\Omega_X^{1/2}).
\tag{I6}
\]
It is elliptic of order \(m\), with the anti-dual symbol of \(p\), by Section 13 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md). Applying the same regularity argument gives the finite-dimensional smooth space
\(N^*=\ker P^*\subset C^\infty(X;F^*\otimes\Omega_X^{1/2})\), independent of the realization. By the duality of Section 1 and the closed range in (I4),
\[
\operatorname{ran}P_s
 =\{f\in H^{s-m}(X;\mathcal F):\langle f,v\rangle=0\text{ for every }v\in N^*\},
\quad
\operatorname{ind}P_s=\dim N-\dim N^*.
\tag{I7}
\]
The functionals furnished by a basis of \(N^*\) are independent: otherwise their linear combination is the zero distribution, and all its coefficients are zero. Hence the codimension in (I7) is exactly \(\dim N^*\), not merely bounded by it.

The smooth and distributional realizations have these same defects. A smooth \(f\) satisfying the obstructions has a Sobolev solution by (I7); the full smoothing parametrix from Section 6 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md), or iteration of the order-one gain, makes that solution smooth. A distributional \(f\) belongs to one Sobolev space by (I1), so the same argument gives a distributional solution when it annihilates \(N^*\). Conversely every solution annihilates \(N^*\) by the distributional adjoint identity. Thus the smooth and distributional ranges are precisely the respective finite intersections of kernels of these continuous functionals, and in particular are closed in their natural topologies. Their index means the difference of finite algebraic defects, as in the Sobolev realizations.

If \(R\in\Psi^{m-1}\), then \(R:H^s\to H^{s-m}\) factors through \(H^{s-m+1}\) and is compact. Therefore \(P+R\) has the same index. This proves dependence only on (I3). For composable elliptic \(P_2:E\to F\) and \(P_1:F\to G\), use the Sobolev spaces \(H^s(E)\), \(H^{s-m_2}(F)\), \(H^{s-m_2-m_1}(G)\) in Section 4 of [Finite defects under perturbation](fredholm-stability.md) to obtain
\[
\operatorname{ind}(P_1P_2)=\operatorname{ind}P_1+\operatorname{ind}P_2,
\qquad \operatorname{ind}P^*=-\operatorname{ind}P.
\tag{I8}
\]
The second formula follows equally from (I5)–(I7) and the double anti-dual identification. If \(E=F^*\) and \(P-P^*\in\Psi^{m-1}\), the operators have the same principal class and opposite indices, so their integer index is zero. Hermitian metrics turn this statement into the familiar assertion for a formally selfadjoint principal symbol; they are an explicit identification, not a deletion of the anti-dual bundles.

## 3. Exact order changes with index zero

On positive-dimensional components choose a smooth positive homogeneous function \(h(x,\xi)\) of degree one away from the zero section, for example a cotangent norm from a Riemannian metric. On a zero-dimensional component use the identity as every order-changing map; its section spaces are finite-dimensional and every operator is smoothing. On a Hermitian bundle \(E\), and for each real \(r\), quantize \(h^r I_E\) with a cutoff near zero and symmetrize the operator in the geometric \(L^2\) pairing. The resulting \(A_r\in\Psi^r_{\mathrm{cl}}\) is formally selfadjoint, elliptic, and has principal symbol \(h^rI_E\). Its index is zero by Section 2. Let \(\Pi\) be the \(L^2\)-orthogonal projection onto its smooth finite-dimensional nullspace, using the Hermitian metric. This is a smooth finite-rank kernel: for an orthonormal basis \(e_1,\ldots,e_d\), it is \(\sum_j e_j\langle\,\cdot\,,e_j\rangle\).

Then
\[
J_E^r=A_r+\Pi:H^s(X;\mathcal E)\longrightarrow H^{s-r}(X;\mathcal E)
\tag{I9}
\]
is bijective for every real \(s\). Indeed, the range of \(A_r\) is the annihilator of that same nullspace in every target Sobolev space; the projection supplies its missing finite-dimensional component. Its kernel is zero, since pairing \((A_r+\Pi)u=0\) with each \(e_j\) gives \(\Pi u=0\), and then \(A_ru=0\). The inverse is bounded by the Banach inverse theorem. These inverses agree on overlaps of their domains by uniqueness of the distributional solution.

The inverse is itself in \(\Psi^{-r}\). If \(B\) is a smoothing-error parametrix, then
\((J_E^r)^{-1}=B+(J_E^r)^{-1}(I-J_E^rB)\).
The second term is a smooth kernel: its input remainder maps every Sobolev order to every higher order, and the coherent inverse is bounded with shift \(r\) at all orders. Applying the same reasoning to the adjoint proves smoothness in the input variable as well; more explicitly, local Fourier coefficients of its kernel decrease faster than every polynomial in both indices by these two-sided bounds. This is the smooth-kernel criterion used in Section 1. Thus the claimed inverse belongs to the calculus. We use \(J_E^r\) as a notation for this construction, not as an assertion that \(J_E^rJ_E^t=J_E^{r+t}\).

In particular any operator norm problem \(H^s(\mathcal E)\to H^{s-m}(\mathcal F)\) is converted, by the exact isomorphisms
\[
A=J_E^{-s}:L^2(\mathcal E)\to H^s(\mathcal E),
\qquad
B=J_F^{s-m}:H^{s-m}(\mathcal F)\to L^2(\mathcal F),
\tag{I10}
\]
into an \(L^2\) problem for \(BPA\). Its principal symbol is \(h^{s-m}ph^{-s}=h^{-m}p\), when the same cotangent function is used. Both conjugating operators have index zero. This construction does not presuppose the norm-limit theorem proved next.

## 4. Measuring a principal symbol by operator norms

First let \(P\in\Psi^m_{\mathrm{cl}}\) and take compactly supported vector functions \(u,v\) in one chart, a nonzero real covector \(\theta\), and \(u_t(x)=e^{itx\cdot\theta}u(x)\). Fourier translation and dominated convergence give, for every real \(a\),
\[
t^{-a}\|u_t\|_{H^a(\mathbb R^n)}\longrightarrow |\theta|^a\|u\|_2.
\tag{I11}
\]
For completeness, the squared integral has weight \((t^{-2}+|\theta+\eta/t|^2)^a\). On \(|\eta|\leq t|\theta|/2\) it converges with a fixed polynomial majorant. On the complement, the rapid decay of \(\widehat u(\eta)\) absorbs any fixed positive or negative power of \(t\) and of \(\langle\eta\rangle\); choosing a larger decay exponent makes its integral tend to zero. This also proves the assertion for negative \(a\), where a uniform lower bound on the weight over all frequencies would be false.

The local exponential-test formula of Section 2 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md), or directly Fourier translation in the defining symbol integral, gives
\[
t^{-m}\langle Pu_t,v_t\rangle\longrightarrow
 \int\langle p_m(x,\theta)u(x),v(x)\rangle\,dx.
\tag{I12}
\]
Here \(p_m\) is the homogeneous leading symbol. In the integral representation, \(t^{-m}a(x,t\theta+\eta)\to p_m(x,\theta)\) uniformly on compact \(x,\eta\) sets. Symbol bounds and the rapidly decreasing test transforms handle the remaining frequencies exactly as in (I11). A localized smoothing remainder contributes \(o(t^m)\) by integration by parts in both compact input and output variables. Pairing through \(H^{s-m}\) and its anti-dual \(H^{m-s}\), equations (I11)–(I12) imply a local bound for \(p_m\) by the norm of \(P:H^s\to H^{s-m}\). Testing with \(u=\phi w\), \(v=\phi z\), shrinking \(\phi\) to a point, and then taking unit fiber vectors \(w,z\), detects the full matrix norm. Finitely many charts and homogeneity show that
\[
\sup_{(x,\theta)\in S_h^*X}\|p_m(x,\theta)\|
 \leq C_{s,m}\|P\|_{H^s\to H^{s-m}},
\qquad S_h^*X=\{h=1\}.
\tag{I13}
\]
The constant depends only on the fixed norms and charts, not on \(P\). In geometric \(L^2\) with \(m=0\), chart cutoffs and local orthonormal frames can be chosen with multiplication norms at most one, so the constant is one. This is a statement about the homogeneous symbol; an arbitrary full symbol can be changed at bounded frequencies without being detected by this limit.

We need the converse estimate modulo a smooth finite-rank error. If \(P\in\Psi^0_{\mathrm{cl}}(\mathcal E,\mathcal F)\), set \(c=\sup_{S_h^*X}\|p_0\|\). For every \(\eta>0\) there is a smooth finite-rank operator \(R\) such that
\[
\|P-R\|_{L^2\to L^2}\leq c+\eta.
\tag{I14}
\]
To prove it, choose \(M>c^2\). The positive definite bundle endomorphism \(M I_E-p_0^*p_0\) has a smooth positive square root \(b_0\). This finite-dimensional fact needs no operator spectral theorem: in a compact parameter set choose \(L\) larger than its largest eigenvalue and use the binomial power series for \(L^{1/2}(I-(I-L^{-1}(M I-p_0^*p_0)))^{1/2}\). The argument of the power series has norm strictly below one uniformly. Termwise differentiated series converge, proving smoothness in charts; uniqueness of the positive square root makes the local definitions agree. Radial extension gives an order-zero homogeneous symbol. Quantize it as \(B\); the calculus gives the selfadjoint compact error
\[
P^*P+B^*B=M I+K,\qquad K\in\Psi^{-1}.
\tag{I15}
\]
Let \(\Pi_N\) be increasing \(L^2\)-orthogonal projections onto finite-dimensional spaces of smooth sections with dense union. Such spaces are obtained by choosing a countable dense sequence of smooth sections and Gram–Schmidt, deleting zero vectors. Compactness of \(K\) implies \(\|K(I-\Pi_N)\|\to0\): finite-rank approximation reduces this to strong convergence of the projections on finitely many adjoint vectors. For \(w=(I-\Pi_N)u\), (I15) yields
\(\|Pw\|^2\leq(M+\|K(I-\Pi_N)\|)\|w\|^2\).
Choose \(M\) and then \(N\) so that the square root of this bound is at most \(c+\eta\). The operator \(R=P\Pi_N\) has smooth input and output vectors and proves (I14). This proof allows derivatives of \(p_0\) to be large; only the finite-rank correction depends on them.

Consequently, if a sequence of smooth invertible degree-zero bundle symbols \(b_j\) has uniformly bounded pointwise norms, it admits quantizations \(Q_j\) with those principal symbols and uniformly bounded \(L^2\) operator norms. Start with arbitrary quantizations and apply (I14), subtracting the corresponding smooth finite-rank errors. Uniform symbol-derivative estimates for \(b_j\) are unnecessary. This is the exact norm-control statement used below.

## 5. Ellipticity survives an operator-norm limit

Suppose \(P_j\in\Psi^m_{\mathrm{cl}}(X;\mathcal E,\mathcal F)\) converges to a bounded map \(P:H^s\to H^{s-m}\) in operator norm at one real \(s\). By (I13), the homogeneous symbols \(p_j\) are uniformly Cauchy on the compact cosphere; their limit \(p\) is continuous, homogeneous of degree \(m\), and the convergence is uniform on every compact subset of \(T^*X\setminus0\). If \(p\) is invertible there, then \(P\) is Fredholm and
\[
\operatorname{ind}P=\operatorname{ind}P_j\quad\text{for all sufficiently large }j.
\tag{I16}
\]
No membership of \(P\) in a pseudodifferential class is asserted.

First take \(s=m=0\). Compactness of the cosphere and uniform convergence imply that \(p_j\) are invertible for large \(j\), with a common bound for \(p_j^{-1}\). Quantize those inverses as \(Q_j\) with uniformly bounded norms using Section 4. Then \(Q_jP_j-I\) and \(P_jQ_j-I\) have order minus one and are compact. For large \(j\), both \(Q_j(P-P_j)\) and \((P-P_j)Q_j\) have norm less than one. Hence
\[
Q_jP=\bigl(I+Q_j(P-P_j)\bigr)+\bigl(Q_jP_j-I\bigr),
\quad
PQ_j=\bigl(I+(P-P_j)Q_j\bigr)+\bigl(P_jQ_j-I\bigr)
\tag{I17}
\]
are Fredholm of index zero, by the geometric series and compact perturbation invariance. Composing their inverses modulo compact errors with \(Q_j\) gives a left and a right parametrix for \(P\); Section 5 of [Finite defects under perturbation](fredholm-stability.md) makes \(P\) Fredholm. Now that Fredholmness is established, operator-norm stability gives (I16). For arbitrary \(s,m\), apply this argument to \(BP_jA\to BPA\), with (I10). Its symbols are \(h^{-m}p_j\). The exact inverse maps \(A^{-1},B^{-1}\) transport Fredholmness and index back to \(P\). Thus no ill-defined Sobolev Hilbert adjoint occurs in the reduction.

Assume more strongly that the same sequence converges compatibly at every real Sobolev order. Compatibility means that the resulting bounded maps agree on intersections, as they do automatically when their limits on smooth sections agree distributionally. Write \(N_s=\ker(P:H^s\to H^{s-m})\) and \(M_{m-s}=\ker(P^*:H^{m-s}(F^*\otimes\Omega^{1/2})\to H^{-s}(E^*\otimes\Omega^{1/2}))\). If \(s_2>s_1\), then \(N_{s_2}\subset N_{s_1}\), while \(M_{m-s_2}\supset M_{m-s_1}\). The index in (I16) is the same at every \(s\), since each \(P_j\) has that property. Therefore
\[
\dim N_{s_1}-\dim N_{s_2}
=\dim M_{m-s_1}-\dim M_{m-s_2}.
\tag{I18}
\]
The left side is nonnegative and the right side nonpositive, so both vanish. Finite dimension and inclusion give equality of these spaces for every pair of orders. By (I1) both nullspaces consist of smooth sections, and the range at every order is the annihilator of the same smooth adjoint nullspace. Single-order convergence alone has none of this smoothness consequence; an example below makes the distinction concrete.

## 6. Bounded symbol homotopies with strong continuity

Let \(t\in[0,1]\). Suppose \(a_t,b_t\) are continuous in the compact-open smooth topology on \(T^*X\), uniformly bounded in \(S^m\) and \(S^{-m}\), respectively, and
\[
a_tb_t-I_F\text{ and }b_ta_t-I_E
\quad\text{are uniformly bounded in }S^{-1}.
\tag{I19}
\]
The maps have the appropriate pulled-back bundle types. Then all quantizations of the endpoint principal classes have the same index. Continuity in every full symbol seminorm is not assumed.

Here are the operator-family details. Fix one finite system of charts, bundle frames, density identifications and cutoffs with \(\sum_j\chi_j^2=1\). Quantize each local representative and place \(\chi_j\) on both sides; extend by zero outside the chart and sum. Coordinate transport and the product formula in [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md) show that the resulting \(A_t,B_t\) have principal classes \(a_t,b_t\). Every seminorm in their products and their order-minus-one errors is bounded by finitely many seminorms in (I19) and the original families. Thus \(A_t:H^s\to H^{s-m}\), \(B_t:H^{s-m}\to H^s\), and
\[
K_t=I-B_tA_t:H^s\to H^{s+1},
\qquad
L_t=I-A_tB_t:H^{s-m}\to H^{s-m+1}
\tag{I20}
\]
are uniformly bounded.

For a fixed smooth input, a local oscillatory formula proves continuity of the output in every fixed Sobolev norm: restrict frequency to a large ball, use compact-open smooth continuity there, and control the tail by a uniform symbol bound times the rapidly decreasing Fourier transform of the input. Derivatives of the output are handled by increasing that uniform bound. On the compact manifold these estimates patch through finitely many charts. Smooth density in each input Sobolev space and uniform operator bounds extend continuity to every fixed input. Consequently both \(A_t\) and \(B_t\), and hence the errors in (I20), are strongly continuous. By (I2) the union of the images of the unit balls under each of \(K_t,L_t\) has compact closure in its original Sobolev space. This proves collective compactness on both sides. Section 7 of [Finite defects under perturbation](fredholm-stability.md) now implies constant index. Altering either endpoint by a lower-order operator is compact by Section 2, so the assertion holds for arbitrary endpoint quantizations.

This argument also works on any compact parameter space with these continuity and boundedness properties: the index is locally constant there, and is constant on each connected component. Compactness of the parameter space is used through the stated uniform bounds and the abstract family theorem; no sequential compactness or metric structure on that parameter space is needed.

## 7. Moving all high frequencies to one sphere

An elliptic symbol with estimates need not approach a homogeneous limit. Nevertheless its index can be read on one sufficiently distant cotangent sphere. Let \(p\in S^m\) represent an elliptic principal class and let \(h>0\) be smooth and homogeneous of degree one away from zero. For every sufficiently large \(R\), the degree-zero symbol
\[
p_R(x,\xi)=p\bigl(x,R\xi/h(x,\xi)\bigr),\qquad \xi\ne0,
\tag{I21}
\]
is invertible and has the same analytic index as \(p\).

First let \(m=0\). Choose \(q\in S^0\) equal to the exact inverse of \(p\) for \(h\geq R_0\), by a cutoff and the inverse derivative estimates. Fix \(R>2R_0\) and a smooth positive function \(k\) on \([0,\infty)\), equal to one for \(r\leq1\), equal to \(r^{-1}\) for \(r\geq2\), with \(r k(r)\geq1\) for \(r\geq1\). Such a function is obtained by a smooth convex combination of \(1\) and \(1/r\) in \([1,2]\). Define
\[
F_t(x,\xi)=\bigl(x,\xi k(th(x,\xi)/R)\bigr),
\qquad p_t=p\circ F_t,\quad q_t=q\circ F_t,
\quad 0\leq t\leq1.
\tag{I22}
\]
At zero covectors use the identity map: the cutoff is exactly one in a neighborhood of the zero section, so no nonsmooth norm is evaluated in a nonconstant expression there. For \(th/R\leq1\), the map is the identity. In the transition region \(1\leq th/R\leq2\), its radial scale is comparable to one and its frequency derivatives of order \(\ell\geq1\) have size at most \(C_\ell h^{1-\ell}\); base derivatives have size at most \(C h\). For \(th/R\geq2\), the image is \((x,R\xi/(t h))\), of size comparable to \(R/t\). In that region every frequency derivative costs \(h^{-1}\), while each derivative of an order-zero input symbol costs the reciprocal of the image size. Iterated chain rules therefore prove uniform \(S^0\) bounds for \(p_t,q_t\), for all \(t\in[0,1]\). These bounds include mixed base and frequency derivatives. Equivalently, on the transition annulus one may set \(\eta=t\xi/R\); its compact angular and radial bounds reduce all estimates to the uniform order-zero estimates for \(p(x,(R/t)\eta)\) and \(q\). This also explains why uniform symbol bounds remain valid as \(t\downarrow0\).

The families are continuous in the compact-open smooth topology, including at \(t=0\), since on each fixed compact set they eventually equal the original symbols. Above \(h\geq R\), their image has \(h\geq R\): if \(th/R\leq1\) this is immediate, and otherwise it equals \((R/t)(th/R)k(th/R)\geq R\). Hence their two pointwise products are exactly the identity there. All derivatives of the product errors are uniformly bounded on the remaining compact set, so those errors form a bounded family in every negative symbol order. Apply Section 6. At \(t=1\), the resulting symbol equals \(p_R\) for \(h\geq2R\); a cutoff of its homogeneous extension therefore has that same principal class. This proves (I21) in order zero.

For general \(m\), right-compose the operator with \(J_E^{-m}\) from Section 3. The product has order zero, index unchanged, and principal representative \(p h^{-m}\) outside a compact set. Its radial restriction is \(R^{-m}p_R\). Multiplication by the positive scalar \(R^{-m}\) is an invertible order-zero operator of index zero. The order-zero argument consequently proves the assertion for \(p\). There is no need to assume \(p\) has a limit along rays, and no deformation through an uncontrolled family of orders has been used.

## 8. The index of a continuous symbol

Let \(p:T^*X\to\operatorname{Hom}(\pi^*E,\pi^*F)\) be continuous and invertible outside a compact set \(K\). It need not satisfy symbol derivative estimates. Choose \(h\) as above and a large \(R\) with \(K\subset\{h<R\}\). The restriction (I21) is a continuous degree-zero isomorphism on \(T^*X\setminus0\), determined by its values on the compact cosphere.

A continuous section of a finite-rank smooth bundle over a compact smooth manifold can be approximated uniformly by smooth sections. To prove the version needed here, choose finitely many local frames and subordinate compactly supported partition functions. Express the product of each partition function with the section in that frame, extend its components by zero inside a larger coordinate domain, and convolve with a compact smooth approximate identity. Uniform continuity gives uniform convergence; for sufficiently small convolution radii the supports remain in their charts. Sum the resulting local sections. Compactness and bounded transition matrices give convergence in the bundle norm. This construction applies to the Hom bundle over the cosphere, without separately smoothing source and target frames.

If \(a,b\) are two continuous invertible degree-zero symbols and
\[
\sup_{S_h^*X}\|a^{-1}b-I\|<1,
\tag{I23}
\]
then \((1-t)a+tb=a[I+t(a^{-1}b-I)]\) is invertible for every \(t\). Choose a smooth approximation \(b\) to \(p_R\) so close that (I23) holds, extend it homogeneously, and quantize with a cutoff near zero. Define
\[
\operatorname{sind}(p)=\operatorname{ind}\operatorname{Op}(b).
\tag{I24}
\]
This definition is independent of the choices. For two sufficiently close smooth approximations, their convex combination remains within the uniform relative-error ball of radius less than one about \(p_R\); its inverse is smooth and uniformly bounded with all derivatives on the compact parameter-cosphere product. Its homogeneous extensions satisfy Section 6. Thus both quantizations have the same index. For arbitrary approximations satisfying (I23), the same convex-combination argument works because the two error bounds have a common maximum strictly below one. Changing the quantization changes only a lower-order operator. The same reasoning proves that (I23) preserves the index when both symbols are merely continuous: approximate both endpoints so closely that the entire straight-line family remains invertible, and compare the resulting smooth path.

Changing the radius introduces the continuous path
\(p(x,((1-t)R_1+tR_2)\xi/h)\), entirely outside \(K\). Changing \(h\) to another positive continuous homogeneous function \(h_1\) introduces
\(p(x,R\xi/((1-t)h+t h_1))\), for a radius large enough to keep all its images outside \(K\). On the compact parameter-cosphere product the smallest singular value has a positive minimum. Uniform continuity partitions the interval into finitely many subintervals on which adjacent symbols satisfy (I23). This proves independence of both choices. It proves at the same time:

**Continuous homotopy theorem.** If \(p_t\) is jointly continuous in \((t,x,\xi)\), \(0\leq t\leq1\), and is invertible outside one compact set \(K\subset T^*X\) for every \(t\), then \(\operatorname{sind}(p_t)\) is constant. The condition concerns one common compact set, not a separate set allowed to escape with \(t\).

The characterization by this homotopy property and agreement with analytic index for smooth degree-zero homogeneous principal symbols is unique. Indeed, first deform any continuous \(p\) to a radial extension using (I22); the same formula is continuous for continuous input and its noninvertibility remains in \(\{h\leq R\}\). Then approximate its cosphere map and join it to that smooth approximation by a straight line. Extend the latter line continuously across bounded covectors by multiplying its homogeneous part with a fixed radial cutoff and retaining any continuous compact filling. Invertibility during the deformation is required only above a common radius. The final smooth homogeneous principal symbol determines the value by analytic agreement. This reduces every value to the prescribed one, proving uniqueness without a K-theory classification theorem.

Every elliptic \(P\in\Psi^m\) has
\[
\operatorname{ind}P=\operatorname{sind}(p),
\tag{I25}
\]
for any continuous principal representative, by Section 7 and (I24). For a continuous degree-\(m\) symbol defined only off zero, choose any continuous filling on a bounded cotangent region after an exterior cutoff; fillings differ through a homotopy supported in a common compact set, so the index is well defined. Such a filling exists even when \(m\leq0\): make it zero near the zero section and interpolate with a radial scalar cutoff, with no requirement of invertibility in that region.

Combining (I25) with Section 5 gives the precise index in the norm-limit theorem:
\[
P_j\longrightarrow P\text{ in }\mathcal L(H^s,H^{s-m}),\quad
p_j\longrightarrow p\text{ invertible on }T^*X\setminus0
\quad\Longrightarrow\quad
\operatorname{ind}P=\operatorname{sind}(p).
\tag{I26}
\]
The relative-error condition applies to \(p_j\) and \(p\) on a cosphere for large \(j\), so the index on the right equals the stabilized value in (I16).

For a zero-dimensional component, \(X\) is a finite set and all section spaces are finite-dimensional. There is no cosphere. Define its contribution as \(\sum_{x\in X}(\operatorname{rank}E_x-\operatorname{rank}F_x)\), the index of every linear map between its section spaces. All preceding statements reduce there to rank-nullity, and products below include these finite-dimensional factors. A compact manifold has finitely many connected components, so these contributions add to the positive-dimensional ones. This convention also covers the empty manifold and the zero bundle.

## 9. A circle calculation that fixes the sign

Write \(X=\mathbb R/(2\pi\mathbb Z)\), with Fourier vectors \(e_k(x)=e^{ikx}\). Suppose a scalar continuous elliptic symbol has exterior branches \(a_+(x)\ne0\) for positive frequency and \(a_-(x)\ne0\) for negative frequency, after radial restriction. Multiplication by \(a_-^{-1}\) has symbol equal on both branches and contributes index zero: approximate it smoothly if necessary, and use the actual invertible multiplication operator. The ratio \(r=a_+/a_-\) is a loop in \(\mathbb C\setminus0\).

Its winding number \(w\) can be defined without assuming differentiability. Divide the circle into arcs on which \(r(x)/r(x_0)\) lies in the disk of radius less than one about one. The power series logarithm on that disk gives local continuous logarithms. Starting at \(x=0\), add multiples of \(2\pi i\) to make neighboring logarithms agree at endpoints. This constructs a continuous logarithm \(\ell\) of \(r\) on \([0,2\pi]\), with \(\ell(2\pi)-\ell(0)=2\pi i w\) for one integer \(w\). Different initial logarithms change \(\ell\) by a constant integral multiple of \(2\pi i\), leaving \(w\) fixed. Thus \(r(x)=e^{iwx+g(x)}\) with periodic continuous \(g\), and the path \(e^{iwx+(1-t)g(x)}\) reduces the calculation to \(r=e^{iwx}\).

Let \(\Pi_+\) project onto Fourier modes \(k\geq0\), and set \(\Pi_-=I-\Pi_+\). This projection is a classical order-zero pseudodifferential operator with principal branches one and zero. Here is a direct kernel justification. Choose a smooth function \(\beta(\xi)\), zero for \(\xi\leq-3/4\), one for \(\xi\geq-1/4\); it equals \(1\) at all nonnegative integers and \(0\) at negative integers. The derivative of \(\beta\) is compactly supported, so its inverse Fourier distribution is smooth away from zero and rapidly decreasing there by integration by parts. Periodize that distribution over translations by \(2\pi\). Off the diagonal the derivative series converges locally uniformly, while near the diagonal only the untranslated singularity remains. Its Fourier coefficients are \(\beta(k)\), by testing the periodized distribution against \(e^{-ikx}\) and the Fourier inversion convention. The periodic convolution operator is therefore \(\Pi_+\), and locally it has the Euclidean symbol \(\beta\) plus a smooth kernel. This proves the pseudodifferential claim without a theorem about holomorphic boundary values.

Consider
\[
T_w=e^{iwx}\Pi_++\Pi_-.
\tag{I27}
\]
It sends \(e_k\) to \(e_{k+w}\) for \(k\geq0\), and to \(e_k\) for \(k<0\). If \(w\geq0\), the images are the disjoint orthonormal sets with frequencies \(k<0\) and \(k\geq w\). The kernel is zero and the missing frequencies \(0,\ldots,w-1\) give a cokernel of dimension \(w\). If \(w=-d<0\), all frequencies occur, and the two image families overlap precisely at \(-d,\ldots,-1\). For \(0\leq j<d\), \(e_j-e_{j-d}\) spans one relation. These \(d\) relations are independent and exhaust the kernel, since all other frequencies have a unique preimage. Thus in every case
\[
\operatorname{sind}(a)=-\operatorname{wind}(a_+/a_-).
\tag{I28}
\]
All defect vectors are smooth, so the calculation agrees with every Sobolev realization.

To check the orientation version, orient \(T^*X\) by \(dx\wedge d\xi\). On the boundary of \(\{|\xi|\leq R\}\), contraction with the outward normal gives orientation \(-dx\) on the upper circle and \(+dx\) on the lower circle. The degree of the phase map is therefore \(-\operatorname{wind}(a_+)+\operatorname{wind}(a_-)\), exactly (I28). Reversing the phase-space orientation reverses that degree; it does not change the analytic convention for the index.

## 10. Partial operators can be approximated on every Sobolev scale

### 10.1. The local approximation statement

Put \(z=(x,y)\in\mathbb R^n\times\mathbb R^{n'}\), \(\zeta=(\xi,\eta)\), and \(\langle\zeta\rangle=(1+|\zeta|^2)^{1/2}\). Let \(m>0\). Suppose \(a(z,\xi)\) is a classical symbol of order \(m\) in the \(\xi\) variables, uniformly over the entire \(z\)-space. Thus, for every pair of multiindices,

\[
 \sup_{z,\xi}\langle\xi\rangle^{-m+|\beta|}
       \|\partial_z^\alpha\partial_\xi^\beta a(z,\xi)\|<\infty.
 \tag{I29}
\]

Its classical expansion has smooth components \(a_{m-j}(z,\xi)\), homogeneous of degree \(m-j\) for \(\xi\ne0\), with the corresponding uniform bounds on \(|\xi|=1\); after a fixed low-frequency cutoff, each remainder has order \(m-N\), uniformly in the same sense. The symbols may be fixed-size complex matrices. No compactness assumption on the base variables replaces the uniform estimates in (I29).

Choose a smooth scalar function \(\chi(\xi,\eta)\) with

\[
 \chi=1\quad\hbox{if }|\eta|\leq\max(1,|\xi|),\qquad
 \chi=0\quad\hbox{if }|\eta|\geq2\max(1,|\xi|),
 \tag{I30}
\]

and homogeneous of degree zero in the region \(|\eta|>2\). These conditions make \(\chi\) a classical symbol of order zero on the full frequency space. Indeed, away from the cone where \(|\eta|\) and \(|\xi|\) are comparable it is identically zero or one; in that cone, outside a bounded set, the stated homogeneity supplies the symbol estimates. Write \(\chi_0\) for its leading homogeneous part. For \(0<\varepsilon\leq1\) define

\[
 a_\varepsilon(z,\xi,\eta)
       =a(z,\xi)\chi(\xi,\varepsilon\eta),\qquad
 A=a(z,D_x),\qquad A_\varepsilon=\operatorname{Op}_{x,y}(a_\varepsilon).
 \tag{I31}
\]

For each fixed positive \(\varepsilon\), \(a_\varepsilon\) is a full-variable classical symbol of order \(m\). Its leading symbol is

\[
 a_{\varepsilon,m}(z,\xi,\eta)
     =a_m(z,\xi)\chi_0(\xi,\varepsilon\eta),
 \tag{I32}
\]

extended by zero across \(\xi=0,\eta\ne0\). Extend \(a_m(z,\xi)\) itself by zero at \(\xi=0\). This extension is continuous because \(m>0\). There are constants independent of \(\varepsilon\) such that

\[
 \sup_{z,\,|\xi|^2+|\eta|^2=1}
   \|a_{\varepsilon,m}(z,\xi,\eta)-a_m(z,\xi)\|
       \leq C\varepsilon^m,
 \tag{I33}
\]

and, for every real \(s\),

\[
 \|A_\varepsilon-A\|_{H^{s+m}(\mathbb R^{n+n'})\to
                          H^s(\mathbb R^{n+n'})}
       \leq C_s\varepsilon^m.
 \tag{I34}
\]

The constants in (I34) depend on finitely many of the uniform symbol seminorms of \(a\), on \(s,m,n,n'\), and on \(\chi\); they do not require uniform full-variable symbol seminorms of \(a_\varepsilon\) as \(\varepsilon\downarrow0\). Those latter seminorms generally grow.

**Full-variable symbol assertion.** On the support of \(\chi(\xi,\varepsilon\eta)\), or of any nonzero derivative of that cutoff,

\[
 \varepsilon|\eta|\leq2\max(1,|\xi|),\qquad
 \langle\xi,\eta\rangle\leq C_\varepsilon\langle\xi\rangle.
 \tag{I35}
\]

The reverse inequality with constant one always holds. For fixed \(\varepsilon>0\), the linear change \((\xi,\eta)\mapsto(\xi,\varepsilon\eta)\) preserves the order-zero symbol estimates for the cutoff. Apply the product rule to (I31). Each derivative of \(a\) is estimated by (I29); (I35) converts its frequency weight to the full-variable weight. Each derivative falling on the cutoff contributes its full frequency-order loss. This proves the \(S^m_{1,0}\) estimates with constants allowed to depend on \(\varepsilon\).

For the classical expansion, multiply each \(a_{m-j}\) by \(\chi_0(\xi,\varepsilon\eta)\). On the punctured full frequency space the latter factor vanishes in a neighborhood of the set \(\xi=0\), so the zero extension is smooth there even when \(m-j\leq0\). Each product is homogeneous of degree \(m-j\). The classical remainder estimate follows from (I35); changing from a cutoff in \(\xi\) to a cutoff in \((\xi,\eta)\) changes only a bounded-frequency region for this fixed \(\varepsilon\). This proves (I32) and the full classical assertion.

For (I33), the difference vanishes when \(|\xi|\geq\varepsilon|\eta|\). On its remaining support, homogeneity and the uniform leading-symbol bound give

\[
 \|a_m(z,\xi)\|\leq C|\xi|^m
      \leq C\varepsilon^m|\eta|^m.
\]

The uniform bound on \(\chi_0-1\) completes the estimate on the total unit sphere. This also checks uniformity near the two frequency axes, where pointwise convergence alone would be insufficient.

### 10.2. The estimate at every real Sobolev order

Set \(C_\varepsilon=\chi(D_x,\varepsilon D_y)\) and \(T_\varepsilon(a)=A_\varepsilon-A\). Left quantization gives the exact identity

\[
 T_\varepsilon(a)=a(z,D_x)(C_\varepsilon-I).
 \tag{I36}
\]

There is no composition remainder in (I36), since the right factor is a Fourier multiplier.

**Output order zero.** For fixed \(y\), the symbol \(a(x,y,\xi)\langle\xi\rangle^{-m}\) has uniformly bounded derivatives of the finite orders required in Section 6 of [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md). Therefore that section's matrix-valued \(L^2\) estimate yields

\[
 \|a(x,y,D_x)v(\cdot,y)\|_{L^2_x}
      \leq C\|v(\cdot,y)\|_{H^m_x},
 \tag{I37}
\]

with the same \(C\) for every \(y\). Integrate its square in \(y\), then apply partial and full Plancherel to \(v=(C_\varepsilon-I)u\). The multiplier can differ from one only where

\[
 \varepsilon|\eta|>\max(1,|\xi|),\qquad
 \langle\xi\rangle^2\leq2\varepsilon^2|\eta|^2
                    \leq2\varepsilon^2\langle\xi,\eta\rangle^2.
 \tag{I38}
\]

Consequently

\[
 \begin{aligned}
 \|T_\varepsilon(a)u\|_2^2
 &\leq C\int\langle\xi\rangle^{2m}
       |\chi(\xi,\varepsilon\eta)-1|^2
       |\widehat u(\xi,\eta)|^2\,d\xi\,d\eta\\
 &\leq C'\varepsilon^{2m}\|u\|_{H^m}^2.
 \end{aligned}
 \tag{I39}
\]

The full Fourier factors in the coefficient \(C\) of (I39) are calculated below in (FC1)--(FC3). The same proof applies to every base derivative \(D_z^\gamma a\), because it still satisfies the uniform order-\(m\) estimates.

**Nonnegative integer output orders.** The cutoff multiplier commutes with every \(D_{z_j}\), and differentiation of the left-quantized integral gives

\[
 [D_{z_j},T_\varepsilon(a)]=T_\varepsilon(D_{z_j}a).
 \tag{I40}
\]

Thus, on Schwartz functions,

\[
 D_z^\alpha T_\varepsilon(a)u
   =\sum_{\gamma\leq\alpha}{\alpha\choose\gamma}
       T_\varepsilon(D_z^\gamma a)D_z^{\alpha-\gamma}u.
 \tag{I41}
\]

For \(|\alpha|\leq k\), apply (I39) to every summand, use \(\|D^{\alpha-\gamma}u\|_{H^m}\leq C\|u\|_{H^{m+k}}\), and sum over the finitely many derivatives defining the equivalent integer \(H^k\) norm. This gives (I34) for every integer \(s=k\geq0\).

**Negative integer output orders.** Let \(k\geq1\). Expand the polynomial

\[
 (1+|\zeta|^2)^k
      =\sum_{|\alpha|\leq k}c_\alpha\zeta^{2\alpha},
      \qquad c_\alpha>0,
 \tag{I42}
\]

and define

\[
 \widehat{u_\alpha}(\zeta)
        =c_\alpha\zeta^\alpha\langle\zeta\rangle^{-2k}
                        \widehat u(\zeta).
 \tag{I43}
\]

Then

\[
 u=\sum_{|\alpha|\leq k}D^\alpha u_\alpha,
 \qquad
 \sum_{|\alpha|\leq k}\|u_\alpha\|_{H^m}^2
       \leq C_k\|u\|_{H^{m-k}}^2.
 \tag{I44}
\]

The identity follows by multiplying (I42) by \(\langle\zeta\rangle^{-2k}\widehat u\). For the estimate, the sum of squared multipliers in (I43) is bounded by \(C_k\langle\zeta\rangle^{-2k}\), again by (I42). This constructs the negative-order decomposition instead of assuming it.

Move the derivatives in (I44) to the left using (I40) in reverse:

\[
 T_\varepsilon(a)D^\alpha
   =\sum_{\gamma\leq\alpha}(-1)^{|\gamma|}
       {\alpha\choose\gamma}
       D^{\alpha-\gamma}T_\varepsilon(D_z^\gamma a).
 \tag{I45}
\]

Every derivative outside \(T_\varepsilon\) has order at most \(k\), hence is bounded from \(L^2\) to \(H^{-k}\). Use (I39) for its remaining factor and then the finite-sum Cauchy–Schwarz inequality in (I44). The result is

\[
 \|T_\varepsilon(a)u\|_{H^{-k}}
       \leq C_k\varepsilon^m\|u\|_{H^{m-k}},
 \tag{I46}
\]

which is exactly (I34) for \(s=-k\). All identities were proved on Schwartz inputs; density in each \(H^r\) and the estimates give their consistent extensions.

**Noninteger orders and the exact interpolation interface.** We use only the two-endpoint implication proved in Section 8 of [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md), equation (E39) and its annular convolution argument, with sequence exponent two. In explicit terms: if a consistent linear map is bounded \(H^{m+r_j}\to H^{r_j}\) for \(r_0<s<r_1\), then it is bounded \(H^{m+s}\to H^s\), with a constant controlled by the two endpoint constants and the distances of \(s\) from the endpoints. This is a statement on the full Euclidean frequency space, not separate interpolation in \(x\) and \(y\).

For clarity, choose sharp dyadic full-frequency projections \(\Pi_j\). Apply the two endpoint estimates to \(\Pi_j u\), then project the output to band \(k\). After inserting the weights \(2^{ks}\) and \(2^{j(m+s)}\), the two estimates have the summable majorant

\[
 c_{k-j}=C\min\{2^{(k-j)(s-r_0)},
                         2^{(k-j)(s-r_1)}\}.
 \tag{I47}
\]

The \(\ell^1*\ell^2\to\ell^2\) convolution bound proves the claimed \(H^{m+s}\to H^s\) estimate. Pass from finite band sums by density; the Fourier norm is equivalent to the band-weighted \(\ell^2\) norm. Apply this implication to \(\varepsilon^{-m}T_\varepsilon(a)\) and the consecutive integers around \(s\). Its endpoint constants are independent of \(\varepsilon\) by (I41) and (I46), proving (I34) with the same power \(\varepsilon^m\) for every real \(s\). No analytic interpolation theorem with an unspecified domain is needed.

The same argument, with \(C_\varepsilon-I\) omitted and \(\langle\xi\rangle\leq\langle\xi,\eta\rangle\) in place of (I38), also proves that the partial operator \(A\) itself maps \(H^{s+m}\) continuously to \(H^s\) for all real \(s\).

### Every Fourier factor and finite derivative coefficient

We make the constants in (I39)--(I46) explicit. Use exactly the
Fourier transform and inverse from [Fourier transforms, finite spectra
and convex separation](prerequisite-bridges.md): the forward integral has no
prefactor and the inverse in dimension \(d=n+n'\) has
\((2\pi)^{-d}\). Thus

\[
 \begin{aligned}
 \widehat u(\xi,\eta)&=\int_{\mathbb R^n\times\mathbb R^{n'}}
   e^{-i(x\cdot\xi+y\cdot\eta)}u(x,y)\,dx\,dy,\\
 u(x,y)&=(2\pi)^{-d}\int
   e^{i(x\cdot\xi+y\cdot\eta)}\widehat u(\xi,\eta)\,d\xi\,d\eta,\\
 \|u\|_{H^r}^2&=(2\pi)^{-d}\int
       \langle(\xi,\eta)\rangle^{2r}|\widehat u(\xi,\eta)|^2
                    \,d\xi\,d\eta.
 \end{aligned}
 \tag{FC1}
\]

The component norm is the original Euclidean bundle-frame norm; it
does not identify different fibers. Put
\(M_\chi=\sup_{\xi,\eta}|\chi(\xi,\eta)-1|\). This number is finite
by the stated smooth low-frequency and homogeneous high-frequency
conditions. No sign condition on the cutoff is needed. For each
multi-index \(\gamma\), let \(A_\gamma\) be a uniform constant in
the actual partial mapping estimate (I37) for \(D_z^\gamma a\):

\[
 \| (D_z^\gamma a)(x,y,D_x)v\|_{L^2_x}
        \leq A_\gamma\|v\|_{H^m_x},
 \qquad y\in\mathbb R^{n'}.
 \tag{FC2}
\]

Its value depends on the retained symbol seminorms and matrix sizes.
Let \(w=(C_\varepsilon-I)u\). Apply (FC2) at each \(y\), integrate
in \(y\), and use partial Plancherel first in \(x\) and then in
\(y\). The two factors are respectively \((2\pi)^{-n}\) and
\((2\pi)^{-n'}\). Using the full inequality (I38) gives

\[
 \begin{aligned}
 \|T_\varepsilon(D_z^\gamma a)u\|_2^2
 &\leq A_\gamma^2(2\pi)^{-n}
       \int_{y,\xi}\langle\xi\rangle^{2m}
                    |\mathcal F_x w(\xi,y)|^2\,d\xi\,dy\\
 &=A_\gamma^2(2\pi)^{-n}(2\pi)^{-n'}
       \int_{\xi,\eta}\langle\xi\rangle^{2m}
        |\chi(\xi,\varepsilon\eta)-1|^2
                     |\widehat u(\xi,\eta)|^2\,d\xi\,d\eta\\
 &\leq A_\gamma^2 2^m M_\chi^2\varepsilon^{2m}
      (2\pi)^{-d}\int_{\xi,\eta}
       \langle(\xi,\eta)\rangle^{2m}|\widehat u(\xi,\eta)|^2
                                                   \,d\xi\,d\eta\\
 &=L_\gamma^2\varepsilon^{2m}\|u\|_{H^m}^2,
 \qquad L_\gamma=2^{m/2}M_\chi A_\gamma.
 \end{aligned}
 \tag{FC3}
\]

Where the cutoff difference is zero both sides of the pointwise
comparison are zero; on its support (I38) applies. In particular,
no Fourier factor or differentiated coefficient is dropped.

For an integer \(k\geq0\), the actual coefficients in (I42) are

\[
 c_\alpha=\frac{k!}{\alpha_1!\cdots\alpha_d!(k-|\alpha|)!},
 \quad |\alpha|\leq k,\qquad
 \|v\|_{H^k}^2=\sum_{|\alpha|\leq k}c_\alpha\|D^\alpha v\|_2^2.
 \tag{FC4}
\]

The multinomial theorem applied to the unchanged polynomial
\((1+\zeta_1^2+\cdots+\zeta_d^2)^k\) proves the first formula;
Plancherel with (FC1) proves the second. Every multiplier
\(\zeta^{\alpha-\gamma}\) in (I41) is bounded by
\(\langle\zeta\rangle^k\) when \(\gamma\leq\alpha\) and
\(|\alpha|\leq k\). Apply (FC3) to every displayed summand in
(I41), retaining its binomial coefficient. Then

\[
 \begin{aligned}
 \|T_\varepsilon(a)u\|_{H^k}
 &\leq \varepsilon^m C_k^+\|u\|_{H^{m+k}},\\
 (C_k^+)^2
 &=\sum_{|\alpha|\leq k}c_\alpha
       \left(\sum_{\gamma\leq\alpha}
              {\alpha\choose\gamma}L_\gamma\right)^2.
 \end{aligned}
 \tag{FC5}
\]

For the negative-order decomposition in (I43), set
\(c_{\max,k}=\max_{|\alpha|\leq k}c_\alpha\). Its exact squared
norm sum is

\[
 \begin{aligned}
 \sum_{|\alpha|\leq k}\|u_\alpha\|_{H^m}^2
 &=(2\pi)^{-d}\int\langle\zeta\rangle^{2m-4k}
       \left(\sum_{|\alpha|\leq k}c_\alpha^2\zeta^{2\alpha}\right)
                        |\widehat u(\zeta)|^2\,d\zeta\\
 &\leq c_{\max,k}(2\pi)^{-d}\int
       \langle\zeta\rangle^{2m-2k}|\widehat u(\zeta)|^2\,d\zeta\\
 &=c_{\max,k}\|u\|_{H^{m-k}}^2.
 \end{aligned}
 \tag{FC6}
\]

Here every \(\zeta^{2\alpha}\) is nonnegative and
\(c_\alpha^2\leq c_{\max,k}c_\alpha\); the full polynomial
(I42), including its constant term, gives the middle inequality.
The identity in (I44) keeps every coefficient in (I43).

For \(|\alpha|\leq k\) and \(\gamma\leq\alpha\), the operator
\(D^{\alpha-\gamma}:L^2\to H^{-k}\) has norm at most one, since
\(\langle\zeta\rangle^{-k}|\zeta^{\alpha-\gamma}|\leq1\).
Use all signs and binomial coefficients in (I45), then the triangle
inequality for each \(\alpha\) and Cauchy--Schwarz for the finite
sum over \(\alpha\). Equations (FC3) and (FC6) yield

\[
 \begin{aligned}
 \|T_\varepsilon(a)u\|_{H^{-k}}
 &\leq \varepsilon^m C_k^-\|u\|_{H^{m-k}},\\
 (C_k^-)^2
 &=c_{\max,k}\sum_{|\alpha|\leq k}
       \left(\sum_{\gamma\leq\alpha}
                 {\alpha\choose\gamma}L_\gamma\right)^2.
 \end{aligned}
 \tag{FC7}
\]

All these calculations hold first on Schwartz inputs. Fourier
completion and the displayed bounds give the same maps on the
stated completed spaces. The real-order interpolation following
(I47) uses these actual endpoint constants. Thus the cutoff
approximation keeps the original Fourier convention, all matrix
components and every finite derivative contribution.

## 11. Multiplication of the continuous symbol index

### 11.1. The bundle type of the product symbol

Let \(X,Y\) be compact smooth manifolds without boundary, with Hermitian complex bundles \(E_X,F_X,E_Y,F_Y\). Write \(\boxtimes\) for the external tensor product. Let

\[
 p(x,\xi):E_{X,x}\longrightarrow F_{X,x},\qquad
 q(y,\eta):E_{Y,y}\longrightarrow F_{Y,y}
\]

be continuous bundle maps on their respective cotangent spaces, invertible outside compact sets \(K_X,K_Y\). No differentiability of these two maps is assumed. On \(T^*(X\times Y)=T^*X\times T^*Y\), define

\[
 \begin{aligned}
 E_+&=(E_X\boxtimes E_Y)\oplus(F_X\boxtimes F_Y),\\
 E_-&=(F_X\boxtimes E_Y)\oplus(E_X\boxtimes F_Y),
 \end{aligned}
\]

with cotangent pullbacks understood, and put

\[
 d=\begin{pmatrix}
 p\otimes I_{E_Y}&-I_{F_X}\otimes q^*\\
 I_{E_X}\otimes q&p^*\otimes I_{F_Y}
 \end{pmatrix}:E_+\longrightarrow E_-.
 \tag{I48}
\]

Here the star is the fiberwise Hermitian adjoint. The block types in (I48) determine every identity factor and the sign of the off-diagonal entry.

Since different tensor factors commute, direct multiplication gives

\[
 d^*d=\begin{pmatrix}
 p^*p\otimes I_{E_Y}+I_{E_X}\otimes q^*q&0\\
 0&pp^*\otimes I_{F_Y}+I_{F_X}\otimes qq^*
 \end{pmatrix},
 \tag{I49}
\]

and

\[
 dd^*=\begin{pmatrix}
 pp^*\otimes I_{E_Y}+I_{F_X}\otimes q^*q&0\\
 0&p^*p\otimes I_{F_Y}+I_{E_X}\otimes qq^*
 \end{pmatrix}.
 \tag{I50}
\]

If \(p\) is invertible at the point in question, both \(p^*p\) and \(pp^*\) are positive definite; hence all diagonal blocks in (I49)–(I50) are positive definite. The same conclusion follows from invertibility of \(q\). Positivity follows directly from squared norms; for a positive definite factor, its positive minimum on the finite-dimensional unit sphere gives a positive lower bound after tensoring. Thus \(d\) is injective and surjective whenever either \(p\) or \(q\) is invertible. It is therefore invertible outside \(K_X\times K_Y\), so its symbol index is defined.

The claim is

\[
 \operatorname{sind}d
     =(\operatorname{sind}p)(\operatorname{sind}q).
 \tag{I51}
\]

This formula uses the homotopy and norm-limit properties of the symbol index proved earlier in this lesson. We now prove the remaining reduction and computation.

### 11.2. Reduction of continuous symbols to degree one

Choose metrics on the cotangent bundles and choose \(R>0\) so large that \(p\) is invertible when \(|\xi|\geq R\). For \(r=|\xi|\geq R\), \(\omega=\xi/r\), and \(0\leq t\leq1\), set

\[
 r_t=(1-t)r+tR,\qquad
 p_t(x,r\omega)=\frac r{r_t}\,p(x,r_t\omega).
 \tag{I52}
\]

Keep \(p_t=p\) for \(r\leq R\). The two definitions agree at \(r=R\). Every \(p_t\) is invertible outside the same compact radius-\(R\) disk bundle. At \(t=1\) it is homogeneous of degree one outside that disk bundle. We may next linearly change its values inside the disk bundle to

\[
 \widetilde p(x,r\omega)=\frac rR\,p(x,R\omega),\qquad
 \widetilde p(x,0)=0.
 \tag{I53}
\]

The change is stationary on the boundary and outside the disk bundle, so it is another permissible homotopy. Continuity at the zero section follows from compactness of the unit cosphere bundle and the factor \(r\).

On the unit cosphere bundle, approximate the continuous bundle map \(R^{-1}p(x,R\omega)\) uniformly by a smooth bundle map. Such approximation follows from finitely many trivializations, local convolution, and a smooth partition of unity: apply convolution to the finitely many matrix components on precompact coordinate neighborhoods, and sum the resulting local sections with the partition. The original map has a uniform positive lower singular-value bound on this compact cosphere bundle. An approximation error below that bound preserves invertibility along the straight segment between the original and the approximant: factor out the original map and apply the convergent finite-matrix Neumann series. Extend the approximant by homogeneity of degree one and set its value to zero at the zero section. This gives a representative smooth away from the zero section, continuous everywhere, and invertible on every nonzero fiber.

Apply the same construction to \(q\). During either homotopy, (I49)–(I50) show that the corresponding product \(d_t\) remains invertible outside a fixed product of compact disk bundles. Thus the two factor indices and the product index are unchanged. For the rest of the proof we may assume that \(p\) and \(q\) have degree one and are smooth away from their respective zero sections. Their block product \(d\) has degree one in \((\xi,\eta)\) and is invertible away from the total zero section. It is continuous on that punctured space, including its two axes; it need not be smooth on those axes.

If a manifold has zero-dimensional components, its cotangent space there is a finite set. The corresponding symbol may be homotoped to zero on that finite set without an invertibility condition at infinity; its symbol index is the index of a map between finite-dimensional section spaces. The same construction below works with that finite-dimensional factor and no frequency variable on it. More explicitly, if \(X\) is a finite set, homotope its symbol to zero. At a point \(x\) put \(r_x=\operatorname{rank}E_{X,x}\), \(f_x=\operatorname{rank}F_{X,x}\). After a fixed permutation of the target blocks, (I48) is the direct sum of \(r_x\) copies of \(q\) and \(f_x\) copies of \(-q^*\). Direct sums add finite kernel and cokernel dimensions; fixed invertible permutations and the scalar minus sign have index zero. Its index is therefore \((r_x-f_x)\operatorname{sind}q\). Summing over \(x\) proves (I51) in this case. The argument with \(Y\) finite is identical with the factors interchanged and the blocks permuted; if both are finite, rank-nullity gives the formula immediately. No equal-rank assumption is imposed on a zero-dimensional component by a vacuous condition at infinity. It suffices below to treat positive-dimensional components of both manifolds.

### 11.3. From local approximation to a global operator

Choose classical elliptic operators \(P:E_X\otimes\Omega_X^{1/2}\to F_X\otimes\Omega_X^{1/2}\) and \(Q:E_Y\otimes\Omega_Y^{1/2}\to F_Y\otimes\Omega_Y^{1/2}\), of order one, with leading symbols \(p,q\). Their construction is the bundle quantization established earlier in this lesson using Section 13 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md). All operator stars in what follows are geometric adjoints for the \(L^2\) pairing of Hermitian bundle half-density sections. They are not the Hilbert adjoints of arbitrary \(H^s\to H^{s-1}\) realizations.

Take finite smooth real cutoff families with

\[
 \sum_j\phi_j^4=1\ \hbox{on }X,\qquad
 \sum_k\psi_k^4=1\ \hbox{on }Y,
 \tag{I54}
\]

each cutoff supported compactly within a bundle-trivializing chart. For example, from an ordinary nonnegative subordinate family with no common zero, divide each member by the fourth root of the sum of its fourth powers. Set

\[
 P_0=\sum_j\phi_j^2P\phi_j^2,\qquad
 Q_0=\sum_k\psi_k^2Q\psi_k^2.
 \tag{I55}
\]

Their principal symbols remain \(p,q\) by (I54). Hence they are elliptic, their kernels and geometric-adjoint kernels are smooth and finite-dimensional, and

\[
 \operatorname{ind}P_0=\operatorname{sind}p,\qquad
 \operatorname{ind}Q_0=\operatorname{sind}q.
 \tag{I56}
\]

Form the partial operator on the product manifold

\[
 D_0=\begin{pmatrix}
 P_0\otimes I&-I\otimes Q_0^*\\
 I\otimes Q_0&P_0^*\otimes I
 \end{pmatrix}:
 C^\infty(E_+\otimes\Omega_{X\times Y}^{1/2})
 \longrightarrow C^\infty(E_-\otimes\Omega_{X\times Y}^{1/2}).
 \tag{I57}
\]

It is generally not an ordinary pseudodifferential operator on \(X\times Y\). We need an approximation argument precisely for that reason.

Here are the chart and cutoff details. Write \(P_j=\phi_j^2P\phi_j^2\). Since its input and output supports lie in a single precompact chart, its matrix kernel has a global left symbol \(a_j(x,\xi)\) after extension to that Euclidean chart; this includes its smoothing remainder. This is the localized left-symbol construction of the ordinary bundle calculus. The symbol is classical of order one, has uniform derivatives of all required orders, and its kernel vanishes when the input or output leaves a fixed compact subset of the chart. The term \(P_j\otimes\psi_k^4\) is a partial operator in a product chart, with symbol \(a_j(x,\xi)\psi_k(y)^4\). Multiplication by a fixed product-chart input cutoff \(\theta_{jk}\) that is one near both compact supports leaves this partial operator unchanged. The same description applies to \(\phi_j^4\otimes(\psi_k^2Q\psi_k^2)\) and to the geometric-adjoint terms.

Apply Sections 10.1–10.2 with \(m=1\) to each such partial symbol, using the reversed roles of the variables for terms acting in \(Y\). Multiply each approximating full operator on the right by its fixed \(\theta_{jk}\) and use a fixed output chart cutoff equal to one on the old output support. The exact original term is unchanged by these two cutoffs. Multiplication by fixed cutoffs is bounded on every Sobolev space by Section 8 of [Symbols, operators and Sobolev scales](euclidean-symbol-calculus.md), so the error retains the bound \(C_s\varepsilon\). The resulting approximants have both kernel supports within the product chart and therefore extend to global classical operators. Their leading symbols converge uniformly on the chart's total cosphere to the old continuous partial leading symbols, by (I33); the fixed cutoffs do not alter the limit.

Sum over the finitely many charts and blocks. Since

\[
 P_0\otimes I=\sum_{j,k}P_j\otimes\psi_k^4,
 \qquad
 I\otimes Q_0=\sum_{j,k}\phi_j^4\otimes(\psi_k^2Q\psi_k^2),
\]

this gives genuine classical order-one operators \(D_\varepsilon\) on \(X\times Y\) satisfying, for every real \(s\),

\[
 \|D_\varepsilon-D_0\|_{H^s\to H^{s-1}}
       \leq C_s\varepsilon,
 \qquad
 \sigma_1(D_\varepsilon)\longrightarrow d
          \quad\hbox{uniformly on the total cosphere bundle}.
 \tag{I58}
\]

The local Sobolev-to-global Sobolev passage uses finite chart sums and the coordinate and bundle Sobolev equivalence proved in Sections 11–13 of [Detecting regularity without choosing coordinates](geometric-microlocal-calculus.md). The exponent \(s\) in (I58) is arbitrary. No claim is made that the symbols \(\sigma_1(D_\varepsilon)\) converge smoothly across the axes or that the full \(S^1\) seminorms stay uniformly bounded.

The norm-limit theorem of Section 5 applies to (I58), since its continuous limiting symbol \(d\) is invertible off zero. It proves that every realization \(D_0:H^s\to H^{s-1}\) is Fredholm, that its distributional kernel and geometric-adjoint obstruction space are smooth and independent of \(s\), and that

\[
 \operatorname{ind}D_0=\operatorname{sind}d.
 \tag{I59}
\]

This invocation supplies both closed range and regularity before any tensor-kernel count is used. The smooth kernel calculation alone would not have supplied those facts.

### 11.4. Compute both kernels without spectral theory

Operators in different factors commute on smooth product sections. One way to check the needed domain statement is to work first on finite sums of separated smooth sections, where it is the ordinary tensor identity. Such sums are dense in the smooth topology: use finite product charts and cutoffs, extend each compactly supported smooth coefficient to a periodic box, and take rectangular partial Fourier sums. Integration by parts gives Fourier coefficients decreasing faster than every polynomial, so all differentiated sums converge uniformly. The product Fourier modes separate into an \(x\)-mode and a \(y\)-mode. The partial operators are continuous on smooth sections, so the commutation identity extends to all smooth inputs. Geometric integration by parts and Fubini give their stated adjoints for the product half-density \(L^2\) pairing.

Use the abbreviations \(P_x=P_0\otimes I\), \(Q_y=I\otimes Q_0\), with the bundle type fixing each occurrence. For smooth even sections \((u,v)\), expand both squares in \(\|D_0(u,v)\|_2^2\). The cross terms cancel because

\[
 \langle P_xu,Q_y^*v\rangle
   =\langle Q_yP_xu,v\rangle
   =\langle P_xQ_yu,v\rangle
   =\langle Q_yu,P_x^*v\rangle.
\]

Thus

\[
 \|D_0(u,v)\|_2^2
  =\|P_xu\|_2^2+\|Q_yu\|_2^2
        +\|Q_y^*v\|_2^2+\|P_x^*v\|_2^2.
 \tag{I60}
\]

This is the smooth-domain version of the tensor identity in Section 9 of [Traces that survive passage to cohomology](traces-and-complexes.md), (T44); the bounded-Hilbert-space theorem there is not applied to unbounded partial operators without a domain argument.

We prove the simultaneous-kernel assertion directly. Let \(e_1,\ldots,e_a\) be an orthonormal basis of the finite-dimensional smooth space \(\ker P_0\). Suppose \(u\) is smooth and \(P_xu=Q_yu=0\). In a local frame for \(E_Y\), fixing \(y\) makes each coefficient \(u(\cdot,y)\) a smooth section in \(\ker P_0\). Therefore

\[
 u(x,y)=\sum_{i=1}^a e_i(x)\otimes f_i(y),
 \qquad
 f_i(y)=\int_X\langle u(x,y),e_i(x)\rangle_X.
 \tag{I61}
\]

The partial contraction is independent of the chosen \(Y\)-frame and defines an \(E_Y\)-valued half-density section. Differentiation under the integral over compact \(X\) shows that \(f_i\) is smooth. Applying \(Q_y\) to (I61) and taking the same finite projection gives \(Q_0f_i=0\). Conversely every such finite tensor sum is killed by both partial operators. It follows that their simultaneous smooth kernel is the algebraic tensor product \(\ker P_0\otimes\ker Q_0\). Being finite-dimensional, it is already complete for the Hilbert tensor norm. If \(\ker P_0=0\), (I61) is an empty sum. If \(\ker Q_0=0\), every coefficient \(f_i\) vanishes. Either case gives the same conclusion.

Apply this observation to the four nonnegative terms in (I60). Since all distributional nullvectors are smooth by (I59), it gives the full kernel formula

\[
 \ker D_0=(\ker P_0\otimes\ker Q_0)
               \oplus(\ker P_0^*\otimes\ker Q_0^*).
 \tag{I62}
\]

The geometric adjoint has blocks

\[
 D_0^*=\begin{pmatrix}
 P_0^*\otimes I&I\otimes Q_0^*\\
 -I\otimes Q_0&P_0\otimes I
 \end{pmatrix}:E_-\longrightarrow E_+.
\]

Its squared-norm expansion has the same cancellation, with the first odd component killed by \(P_0^*\) in \(X\) and by \(Q_0\) in \(Y\), and the second killed by \(P_0\) in \(X\) and by \(Q_0^*\) in \(Y\). Hence

\[
 \ker D_0^*=(\ker P_0^*\otimes\ker Q_0)
               \oplus(\ker P_0\otimes\ker Q_0^*).
 \tag{I63}
\]

Put \(a=\dim\ker P_0\), \(b=\dim\ker P_0^*\), \(c=\dim\ker Q_0\), and \(e=\dim\ker Q_0^*\). Equations (I59), (I62), and (I63) now give

\[
 \operatorname{sind}d
   =ac+be-bc-ae
   =(a-b)(c-e)
   =(\operatorname{sind}p)(\operatorname{sind}q),
 \tag{I64}
\]

using (I56) in the last step. This proves (I51) without an eigenfunction expansion or a spectral theorem for an unbounded operator.

## 12. Four ways the analytic hypotheses matter

**A smooth approximating sequence with a rough limiting kernel.** Use normalized Fourier vectors on the circle. Let \(f=c\sum_{k\geq1}k^{-1}e_k\), with \(c>0\) chosen so that \(\|f\|_2=1\), and let \(f_N\) be its normalized finite truncation. The Fourier norm shows that \(f\in H^t\) exactly when \(t<1/2\). Define
\[
P_Nu=u-\langle u,f_N\rangle f_N,
\qquad Pu=u-\langle u,f\rangle f.
\tag{I65}
\]
Each \(P_N\) is a classical order-zero elliptic operator with principal symbol one: its correction has a smooth finite-rank kernel. Since \(f_N\to f\) in \(L^2\), the difference of the two rank-one projections has norm at most \(2\|f_N-f\|_2\). Hence \(P_N\to P\) in operator norm on \(L^2\). The limit has index zero and kernel \(\mathbb C f\), which is not smooth. This respects Section 5: the all-order hypothesis was not imposed. Indeed \(Pe_1=e_1-\langle e_1,f\rangle f\notin H^{1/2}\), so \(P\) does not even preserve that Sobolev space.

**An elliptic symbol with no leading homogeneous limit.** On the circle take the Fourier multiplier
\[
Ae_k=\bigl(2+\sin(\log\langle k\rangle)\bigr)e_k.
\tag{I66}
\]
The smooth Euclidean symbol \(a(\xi)=2+\sin(\log\langle\xi\rangle)\) has \(|\partial_\xi^j a|\leq C_j\langle\xi\rangle^{-j}\), by repeated chain rules, and \(1\leq a\leq3\). Periodizing its kernel as in Section 9 gives an order-zero circle operator. Its reciprocal multiplier is bounded on every \(H^s\), so its index is zero. The symbol has no limit on a positive ray: choosing \(\xi\) with \(\log\langle\xi\rangle\) equal to \(2\pi j+\pi/2\) or \(2\pi j+3\pi/2\) gives the two limits three and one. Thus it is not classical polyhomogeneous of order zero. Section 7 still applies, and its radial restrictions are positive constants, giving the same zero index.

**A matrix symbol whose two defects do not cancel as spaces.** On the rank-two trivial circle bundle take positive branch \(\operatorname{diag}(e^{2ix},e^{-3ix})\) and negative branch \(I_2\). One quantization is \(T_2\oplus T_{-3}\). Section 9 gives kernel dimension three, cokernel dimension two and index one. The nonzero kernel lies in the second component and the cokernel in the first; an integer cancellation does not identify these spaces. If \(U(x),V(x)\) are smooth invertible matrix functions, then \(U(T_2\oplus T_{-3})V\) has the same index, because multiplication by either matrix has an exact bounded inverse on every Sobolev space. Its symbol need not remain diagonal.

**The scale of partial regularization.** With both frequency factors nontrivial, the order-zero symbol \(a=1\) gives \(A_\varepsilon-A=C_\varepsilon-I\). On an open set with \(|\xi|<1\) and \(\varepsilon|\eta|>2\), this Fourier multiplier equals minus one. An input supported there in Fourier space shows that its norm on every \(H^s\) is at least one. Positive order is essential in (I34). Conversely, for \(a(\xi)=\langle\xi\rangle^m\), \(m>0\), concentrate Fourier inputs near \((R\omega,3R\omega'/\varepsilon)\), with both direction vectors unit and \(R\to\infty\). The cutoff is zero on sufficiently small neighborhoods. The norm ratio from \(H^{s+m}\) to \(H^s\) tends to \((1+9/\varepsilon^2)^{-m/2}\), which is at least \(10^{-m/2}\varepsilon^m\) for \(0<\varepsilon\leq1\). Thus the exponent in (I34) is attained up to a constant by this elementary symbol family.

## 13. Exercises with complete solutions

**1. Moving both finite defects.** Start with \(T_1\) from (I27). Change only the image of \(e_0\), setting it to zero. Compute both defects and check the principal symbol.

**Solution.** The modified operator is \(S=T_1-R\), where \(Ru=\langle u,e_0\rangle e_1\) in the normalized Fourier basis. The kernel is \(\mathbb C e_0\); the remaining input frequencies have distinct images. The missing output frequencies are zero and one, so the cokernel has dimension two. Hence \(\operatorname{ind}S=1-2=-1=\operatorname{ind}T_1\). The rank-one kernel of \(R\) is smooth, so the principal symbol is unchanged. Compact perturbation preserves the difference of defects, while each dimension can change.

**2. A compact exceptional set cannot escape.** Choose a smooth \(\rho:\mathbb R\to[0,1]\), zero on \(( -\infty,1]\) and one on \([2,\infty)\), and on \(T^*S^1\) set
\[
p_t(x,\xi)=1+\rho(t\xi)(e^{ix}-1),\qquad 0\leq t\leq1.
\tag{I67}
\]
Show that every individual symbol is invertible outside a compact set, but its index is not constant in \(t\). Locate the missing homotopy hypothesis.

**Solution.** At \(t=0\) the symbol is identically one, of index zero. For \(t>0\) its exterior branches are \(e^{ix}\) and one, so Section 9 gives index minus one. It is jointly smooth in \((t,x,\xi)\). By the intermediate value theorem choose \(u_0\in(1,2)\) with \(\rho(u_0)=1/2\). Then \(p_t(\pi,u_0/t)=0\). Those points escape every compact set as \(t\downarrow0\); no common compact exceptional set exists. For each fixed \(t>0\), the entire noninvertible set is contained in the compact region \(|\xi|\leq2/t\).

**3. A negative-order decomposition without duality.** For \(z\in\mathbb R^N\), construct \(u_0,u_1,\ldots,u_N\) such that \(u=u_0+\sum_jD_ju_j\) and \(\sum_{j=0}^N\|u_j\|_{H^m}^2\leq\|u\|_{H^{m-1}}^2\).

**Solution.** Put \(\widehat u_0=\langle\zeta\rangle^{-2}\widehat u\) and \(\widehat u_j=\zeta_j\langle\zeta\rangle^{-2}\widehat u\). The differentiated sum has multiplier \((1+|\zeta|^2)\langle\zeta\rangle^{-2}=1\). The sum of the squared \(H^m\) weights equals \(\langle\zeta\rangle^{2m-2}\). Integration gives equality in the stated estimate. This proves the decomposition for every real \(m\), first on Schwartz functions and then by Fourier completion.

**4. The sign in the product block.** For one-dimensional fibers and \(p=1\), \(q=i\), calculate \(d\), its determinant and \(d^*d\). Repeat with the upper-right minus sign removed.

**Solution.** The correct block is \(\begin{pmatrix}1&i\\i&1\end{pmatrix}\), with determinant two and \(d^*d=2I\). Removing the minus sign gives \(\begin{pmatrix}1&-i\\i&1\end{pmatrix}\), whose determinant is zero. Thus the sign is necessary even when both factor maps are invertible. Tensor commutation alone does not cancel the off-diagonal terms without it.

**5. A product with six obstructions.** Let \(P=T_2J^1\) and \(Q=T_{-3}J^1\) on two circles, using an order-changing isomorphism from Section 3. Find the kernel and cokernel dimensions of their partial product (I57).

**Solution.** Right composition by an isomorphism preserves both finite defects. Thus \(\dim\ker P=0\), \(\dim\ker P^*=2\), \(\dim\ker Q=3\), \(\dim\ker Q^*=0\). The two operators have order one and the required elliptic symbols. Section 11 first supplies Fredholmness and smoothness on the product, then (I62)–(I63) give kernel dimension zero and cokernel dimension six. The index is \((-2)(3)=-6\). The cokernel is the tensor product of the two-dimensional adjoint kernel of \(P\) and the three-dimensional kernel of \(Q\); no spectral expansion of either order-one operator is needed.

**6. Quantitative freedom to smooth.** Let \(a\) be a continuous invertible degree-zero bundle symbol, and put \(M=\sup\|a^{-1}\|\) on the cosphere. If a smooth symbol \(b\) satisfies \(\sup\|b-a\|\leq\delta<M^{-1}\), prove an inverse bound along the straight segment and show that its symbol index equals that of \(a\).

**Solution.** For \(a_t=a+t(b-a)\), factor \(a_t=a[I+t a^{-1}(b-a)]\). The bracket has inverse given by its norm-convergent geometric series, bounded by \((1-M\delta)^{-1}\). Hence \(\sup\|a_t^{-1}\|\leq M/(1-M\delta)\). The path is continuous on the compact parameter-cosphere product and invertible there; homogeneous extension and any common compact filling give the homotopy in Section 8. The indices are equal. No derivative bound on \(b\) is used in this comparison. Derivatives are needed for each individual quantization, whose norm can be controlled modulo a smooth finite-rank correction by Section 4.

## References

The exposition above organizes the proof around finite errors and norm control before introducing continuous symbols. The circle calculation uses direct Fourier images and relations; the partial product calculation establishes all-order convergence before counting smooth tensor kernels.

[Gerd Grubb, *Distributions and Operators*, chapter 8](https://web.math.ku.dk/~grubb/dist8n.pdf), Theorem 8.11 and Corollary 8.12, give the compact-manifold Fredholm alternative and dependence on the principal symbol. The proof is written in scalar notation and explicitly states its bundle extension; it provides a useful comparison for Sections 1–3. It does not by itself supply the weaker bounded-symbol homotopy hypothesis, the norm-limit theorem or the partial approximation estimate used here. [Richard Melrose, *Lectures on Pseudodifferential Operators*](https://math.mit.edu/~rbm/18.157-F05.pdf), version 0.7E revised 29 November 2006, Lecture 9, gives finite-rank parametrices and homotopy invariance for continuous families in the pseudodifferential topology. Lecture 19 treats multiplicativity in a broader family and fibration setting using an additional product calculus and index-bundle machinery. Those additional constructions are not assumed in the proofs above. The linked readings are mathematical comparisons, with no prose, diagrams or exercises imported. A compatible redistribution grant was not identified in the inspected copies, so no part of either reading is incorporated as licensed course content.

## Further questions

Three directions start from specific proved interfaces:

- **Complete the order-zero operator algebra.** Equations (I13)–(I14) identify the principal-symbol size after compact errors are removed. Use them to investigate the norm completion of the order-zero calculus and its symbol map. A complete argument must construct the quotient and prove that every continuous cosphere section is represented in the appropriate quotient; this lesson does not assume that algebraic extension or its K-theory.
- **Follow defects in parameter families.** Section 6 preserves an integer under strong continuity and two collectively compact error families. To obtain a bundle of defects over a parameter space, first stabilize the finite-dimensional obstructions and prove local triviality of the resulting kernels. Constancy of the integer alone supplies neither constant kernel dimension nor such a bundle. Melrose's family treatment indicates the additional constructions to examine.
- **Track product estimates beyond two factors.** Iterate the parity block and the local estimate (I34), keeping the bundle ordering and the geometric adjoints explicit. A quantitative many-factor version should specify how cutoff scales, chart constants and Sobolev orders enter the approximation error. If positive orders tend to zero, the fourth worked example shows why uniform norm approximation cannot be inferred from the present argument.

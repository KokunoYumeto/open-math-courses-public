# Complex stalk–costalk Euler numbers and function duality

A complex constructible sheaf has the same integer Euler number at a stalk and at its point costalk. Its punctured normal model explains this: complex scalar orbits meet a unit sphere in circles, and every finite local system on a circle has Euler characteristic zero. This remains true when the orbit monodromy is nontrivial. It follows that duality fixes every complex constructible function.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Complex nearby cycles as normal and conormal sections for complex and perfect constructibility of specialization, and Holomorphic operations and complex Fourier symmetries for the complex Euler annihilator. Perfect operations and finite microlocal coefficients and Perfect coefficients on compact fibres supply the finite complexes used below. Euler numbers and vector-field indices proves integer Euler additivity, including arbitrary fields. Constructible functions and Euler integration supplies the germ-local costalk description of function duality.

The exact written SH-02 point-specialization provider is Reading a sheaf at the normal scale. Its ordinary unit and exceptional counit identify both the stalk and the costalk of specialization. Its coefficient domain includes every field. We also use its positive conicity and the standing whole-complex descent over a contractible interval. Lower compatible triangulation, analytic and sheaf foundations retain their precise programme obligations; the arguments here are full own proofs relative to these providers.

## Integer Euler numbers and the point-specialization maps

Let \(k\) be any field. For a perfect coefficient complex \(P\), set

\[
 \chi(P)=\sum_j(-1)^j\dim_k H^j(P)\in\mathbb Z.
 \qquad\text{(1)}
\]

The sum is finite, and it is additive in distinguished triangles. Dualizing a finite complex over \(k\) reverses cohomology degrees and preserves (1). These are integer calculations in every characteristic.

Let \(X\) be a complex analytic manifold of complex dimension \(d\), with the standing Hausdorff, countability and finite dimension assumptions. Let
\(F\in D^b_{\mathbb C\text{-c}}(k_X)\) be globally bounded with finite perfect stalks. Fix \(x\in X\), and write \(i:\{x\}\hookrightarrow X\). Specialize at that point:

\[
 V=T_xX,\qquad K=\nu_xF,\qquad e:\{0\}\hookrightarrow V,
 \qquad
 e^{-1}K\simeq F_x,\quad e^!K\simeq i^!F.
 \qquad\text{(2)}
\]

The same ordinary unit identifies \(R\Gamma(V;K)\) with \(F_x\). The exceptional identification in (2) comes from the positive-chamber support counit. For a point-supported coefficient, its positive parameter shift \([1]\) cancels the endpoint costalk shift \([-1]\), and the boundary map is the identity. Thus no dimension shift or independent orientation scalar has been inserted in (2).

The written specialization theorem makes \(K\) positively conic, complex constructible and perfect. It applies over \(k\), including positive characteristic. These facts and the general point-specialization maps suffice for the proof.

## Both radial directions are invisible to the microsupport

Write a real cotangent covector as the real part of a complex covector \(\xi\), and put \(\Lambda=\operatorname{SS}(K)\). Positive conicity and the real Euler criterion give
\(\operatorname{Re}\langle v,\xi\rangle=0\) on \(\Lambda\). Complex constructibility also puts \(i\xi\) in \(\Lambda\). Applying the same criterion to \(i\xi\) gives the imaginary part:

\[
 \operatorname{Re}\langle v,\xi\rangle=0,\qquad
 \operatorname{Re}\langle v,i\xi\rangle
       =-\operatorname{Im}\langle v,\xi\rangle=0,
 \qquad
 \langle v,\xi\rangle=0.
 \qquad\text{(3)}
\]

Hence the covectors in \(\Lambda\) annihilate both the real radial vector \(v\) and the angular vector \(iv\). In a holomorphic chart for the scalar-orbit quotient on \(V\setminus\{0\}\), exact submersion pullback and horizontal microsupport descent make the cohomology of \(K\) locally constant along each \(\mathbb C^*\)-orbit. This is a local assertion on the orbit; continuation around it can have monodromy.

Choose a Hermitian norm and let \(S\) be its unit sphere. The real analytic polar homeomorphism is

\[
 (0,\infty)\times S\xrightarrow{\sim}V\setminus\{0\},
 \qquad(r,s)\longmapsto rs,\qquad L=K|_S.
 \qquad\text{(4)}
\]

Whole-complex descent along the contractible positive radial coordinate identifies the pullback of \(K\) in (4) with the pullback of \(L\). Consequently
\(R\Gamma(V\setminus\{0\};K)\simeq R\Gamma(S;L)\).
The comparison uses the actual restriction at radius one and interval descent. It imposes no angular trivialization.

## A circle contributes zero even with monodromy

Let \(A\) be a rank-\(r\) local system on a circle. Cutting at one vertex gives its cellular cochain complex

\[
 k^r\xrightarrow{T-I}k^r,
 \qquad
 H^0(S^1;A)=\ker(T-I),\quad
 H^1(S^1;A)=\operatorname{coker}(T-I),
 \qquad\text{(5)}
\]

where \(T\) is its invertible monodromy. There are no other cohomology groups. Rank-nullity gives equal dimensions for the kernel and cokernel, so \(\chi(R\Gamma(S^1;A))=0\).

For a bounded complex \(B\) with finite locally constant cohomology on the circle, the finite hypercohomology spectral sequence gives

\[
 \chi(R\Gamma(S^1;B))
   =\sum_j(-1)^j\chi(R\Gamma(S^1;H^j(B)))=0.
 \qquad\text{(6)}
\]

Indeed its cohomology-sheaf rows are confined to finitely many \(j\), and the circle columns are zero and one. Passing from any page to the next preserves the alternating dimension sum: the image of a differential cancels in its two adjacent total degrees. The limit filtration has the same sum. Formula (5) makes each row sum zero. This proves (6) for the entire bounded complex, retaining its extension data.

## Proper circle fibres make the whole link Euler number zero

Assume \(d\ge1\). The Hopf projection is

\[
 q:S\longrightarrow\mathbb P(V)\simeq\mathbb{CP}^{d-1},
 \qquad q(s)=\mathbb C s.
 \qquad\text{(7)}
\]

It is proper because \(S\) is compact. Each fibre is the unit circle in its complex line. In the chart of lines with a specified nonzero coordinate, represent the line by a vector with that coordinate one, normalize its length, and multiply it by a unit complex number. This gives a local product with a circle and proves that \(q\) is a real analytic submersion.

The restriction \(L\) is real constructible and perfect on the real analytic sphere. Proper constructible direct image therefore makes \(Q=Rq_*L\) bounded and perfect constructible on the compact projective space. Proper base change and orbit constancy identify its stalks:

\[
 Q_\ell\simeq R\Gamma(q^{-1}(\ell);L),\qquad
 \chi(Q_\ell)=0\quad(\ell\in\mathbb P(V)).
 \qquad\text{(8)}
\]

The second equality is (6), because that fibre is contained in one complex scalar orbit.

We explain why these stalk Euler numbers determine the global Euler number, even when \(Q\) does not split into its cohomology sheaves. Choose a finite triangulation compatible with the cohomology strata of \(Q\). Filter the compact base by closed skeleta. Closed/open localization makes the global Euler number the sum of compact open-simplex contributions. On a simplex of dimension \(a\), every cohomology sheaf is a constant finite-dimensional vector space. Its compact cohomology contributes its dimension with the shift \(a\). The finite hypercohomology argument used in (6) consequently gives

\[
 \chi(R\Gamma(\mathbb P(V);Q))
   =\sum_{\tau}(-1)^{\dim\tau}\chi(Q_{\ell_\tau})=0.
 \qquad\text{(9)}
\]

Here \(\ell_\tau\) is any point of that open simplex. This is a finite integer sum. A derived splitting of \(Q\) was never required.

Composition of ordinary direct images, (4), and (9) now give

\[
 \chi(R\Gamma(V\setminus\{0\};K))
       =\chi(R\Gamma(S;L))=0.
 \qquad\text{(10)}
\]

For \(d=0\), the punctured vector space is empty and (10) holds directly.

## The point-localization triangle proves the Euler equality

Let \(j:V\setminus\{0\}\hookrightarrow V\). The closed/open localization triangle, followed by ordinary sections on \(V\), is

\[
 R\Gamma_{\{0\}}(V;K)
       \longrightarrow R\Gamma(V;K)
       \longrightarrow R\Gamma(V\setminus\{0\};K)
       \xrightarrow{+1}.
 \qquad\text{(11)}
\]

Every term is perfect. The first two are the point complexes in (2); the third is finite compact-sphere cohomology through (4). Euler additivity and (10) prove the theorem:

\[
 \boxed{\chi(i^!F)=\chi(F_x)
       \qquad\text{for every }x\in X\text{ and every field }k.}
 \qquad\text{(12)}
\]

For a point embedding, \(R\Gamma_{\{x\}}(X;F)\) is precisely \(i^!F\), regarded as a coefficient complex on that point. Thus (12) is the assigned supported-cohomology conclusion as well.

The proof preserves the actual specialization maps and the angular monodromy, and uses integer dimensions throughout. It applies to arbitrary finite perfect coefficients along the strata, without demanding trivial scalar-orbit monodromy.

## Duality fixes the complex constructible function

Constructible Verdier duality has the actual stalk–costalk pairing

\[
 (D_XF)_x\simeq R\operatorname{Hom}_k(i^!F,k).
 \qquad\text{(13)}
\]

Coefficient duality preserves the Euler number in (1), so (12) gives

\[
 \chi_X(D_XF)(x)=\chi(i^!F)=\chi_X(F)(x).
 \qquad\text{(14)}
\]

Let \(\varphi\) be an integer-valued complex constructible function: it is constant on the strata of a locally finite complex analytic stratification. Function duality is a germ-local additive operation, with
\((D_X\varphi)(x)=\chi(i^!F)\) for any local realization \(\chi_X(F)=\varphi\).

Here such a realization can be chosen complex constructible. Near a given point choose a neighborhood meeting only finitely many strata \(S_\alpha\), and let \(n_\alpha=\varphi|_{S_\alpha}\). With extension by zero from each locally closed stratum, take

\[
 F=
 \bigoplus_{n_\alpha>0} k_{S_\alpha}^{\,n_\alpha}
 \ \oplus\
 \bigoplus_{n_\alpha<0} k_{S_\alpha}^{\,-n_\alpha}[1].
 \qquad\text{(15)}
\]

The sum is finite. Its cohomology is constant on the given strata with finite stalks, and the shift \([1]\) supplies each negative weight. Hence it is a bounded complex constructible realization. Formula (14) and the germ-local costalk formula prove

\[
 \boxed{D_X\varphi=\varphi.}
 \qquad\text{(16)}
\]

For the function operation one may use \(\mathbb Q\) in (15), within its existing Grothendieck/function definition. The stalk–costalk theorem itself was proved over every field. Neither conclusion identifies a sheaf complex with its Verdier dual: the equality records integer Euler data, and examples below retain the different complexes.

## Exercises with complete solutions

### A shifted unipotent circle coefficient
*Difficulty: Introductory.*

Over any field take the rank-two circle local system with monodromy
\(T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\). Compute the cohomology and Euler number of \(R\Gamma(S^1;A[1])\), including in characteristic two.

**Solution.** The matrix \(T-I\) has rank one in every field. Both its kernel and its cokernel have dimension one. Thus \(R\Gamma(S^1;A)\) has one-dimensional cohomology in degrees zero and one. Shifting by \([1]\) moves them to degrees minus one and zero. The integer Euler number is \(-1+1=0\). The nontrivial monodromy and the characteristic-two Jordan matrix do not alter this calculation.

### The two extensions from a punctured disk
*Difficulty: Advanced.*

Let \(j:\Delta^*\hookrightarrow\Delta\) be a punctured complex disk, and let \(A\) have invertible monodromy \(T\) on a finite-dimensional space \(W\). Compare the stalk and costalk Euler numbers at zero of \(j_!A\) and \(Rj_*A\).

**Solution.** Put \(C=[W\xrightarrow{T-I}W]\) in degrees zero and one. Radial interval descent computes punctured-disk sections as \(C\). The stalk of \(j_!A\) at zero is zero. Its point-localization triangle is
\(i^!j_!A\to0\to C\xrightarrow{+1}\), so \(i^!j_!A\simeq C[-1]\).
Its cohomology is \(\ker(T-I)\) in degree one and \(\operatorname{coker}(T-I)\) in degree two. Their dimensions are equal, giving Euler number zero.

The stalk of \(Rj_*A\) is \(C\). Its costalk vanishes: the map from \(Rj_*A\) to \(Rj_*j^{-1}Rj_*A\) is the identity under open adjunction, and the localization triangle gives zero for the supported term. Thus both stalk and costalk Euler numbers are zero for each extension. For \(T=I\) the first extension has nonzero costalk and zero stalk, while the second has nonzero stalk and zero costalk. These different complexes satisfy the same Euler theorem.

### A constant complex with an arbitrary shift
*Difficulty: Introductory.*

On \(\mathbb C^d\) take \(F=k[r]\). Compute its stalk and point costalk at zero, including \(d=0\).

**Solution.** The stalk is \(k[r]\). The real manifold has dimension \(2d\) and its complex orientation trivializes the local orientation line. The point costalk of the constant sheaf is \(k[-2d]\), so \(i^!F=k[r-2d]\). Their Euler numbers are respectively \((-1)^r\) and \((-1)^{r-2d}=(-1)^r\). For \(d=0\) the two actual complexes agree. In higher dimension their nonzero cohomology degrees differ by \(2d\).

### Negative weights and a special point value
*Difficulty: Intermediate.*

On \(\mathbb C\), let \(\varphi=-3\) off zero and \(\varphi(0)=2\). Construct a bounded complex realization and compute \(D\varphi\).

**Solution.** The function is \(-3\,1_{\mathbb C}+5\,1_{\{0\}}\). Thus
\(F=k_{\mathbb C}^{\,3}[1]\oplus k_{\{0\}}^{\,5}\) realizes it. Away from zero its stalk Euler is \(-3\); at zero it is \(-3+5=2\). The constant summand has costalk \(k^3[-1]\) at zero, of Euler \(-3\), and the point summand has costalk \(k^5\), of Euler five. Their total is two. At a nonzero point, the constant costalk has the same Euler \(-3\) and the point summand vanishes. Hence \(D\varphi=\varphi\). Formula (15) also realizes the same function using the two disjoint strata directly.

### The crossing has two costalk degrees
*Difficulty: Advanced.*

Let \(Z=\{z_1z_2=0\}\subset\mathbb C^2\), and take its constant sheaf extended from this closed subset. Compute the stalk and point costalk cohomology at the crossing.

**Solution.** The union of the two complex axes is contractible, and its constant sheaf has stalk \(k\) at zero. Its punctured link is the disjoint union of two circles. Consequently link cohomology is \(k^2\) in degrees zero and one. The restriction \(k\to k^2\) in degree zero is diagonal. The point-localization long exact sequence gives zero supported cohomology in degree zero, its diagonal cokernel \(k\) in degree one, and \(k^2\) in degree two, with no other groups. The costalk Euler number is \(-1+2=1\), equal to the stalk Euler number. As a function,
\(1_Z=1_{\{z_1=0\}}+1_{\{z_2=0\}}-1_{\{0\}}\); all three indicators are fixed by (16), so their same integer combination is fixed too.

### A proper image with zero stalk Euler need not split
*Difficulty: Advanced.*

For the Hopf projection \(q:S^3\to\mathbb{CP}^1\), put \(Q=Rq_*k_{S^3}\). Compute its cohomology sheaves. Show that it is nonzero, has zero Euler number at every stalk, and is not isomorphic to
\(k_{\mathbb{CP}^1}\oplus k_{\mathbb{CP}^1}[-1]\).

**Solution.** Proper base change gives the cohomology of a circle at each stalk. The local product transitions rotate that circle, so they act identically on its degree-zero and degree-one cohomology. Thus \(H^0(Q)=k_{\mathbb{CP}^1}\) and \(H^1(Q)=k_{\mathbb{CP}^1}\), with no other cohomology sheaves. In particular \(Q\ne0\), while its stalk Euler number is \(1-1=0\).

If the proposed splitting existed, ordinary global sections would give
\(R\Gamma(\mathbb{CP}^1;k)\oplus R\Gamma(\mathbb{CP}^1;k)[-1]\), with one copy of \(k\) in each of degrees zero, one, two and three. But direct-image composition gives \(R\Gamma(\mathbb{CP}^1;Q)=R\Gamma(S^3;k)\), which has cohomology only in degrees zero and three. The zero- and top-dimensional cell structures of the sphere and of \(\mathbb{CP}^1\simeq S^2\) give these calculations over every field. The contradiction rules out the splitting. Formula (9) retains precisely the extension data that can cancel the two middle degrees.

### A real ray fails the complex conclusion
*Difficulty: Intermediate.*

Inside the complex line take the closed real ray \(H=\{t\in\mathbb R:t\ge0\}\), and its constant sheaf extended from that closed subset. Compute stalk and point costalk Euler numbers at zero.

**Solution.** The stalk at zero is \(k\). Closed-embedding adjunction computes the ambient point costalk intrinsically on \(H\). In a small half-interval, ordinary sections and sections on the punctured half-interval are both \(k\), and their restriction map is the identity. The relative localization complex is therefore zero, so the point costalk Euler number is zero. The stalk Euler number is one.

This sheaf is real constructible on the complex line, but the ray is not a stratum of any locally finite complex analytic stratification with the required constant stalks. In particular it does not satisfy the complex hypothesis used in (3). Its Euler function has value one at zero, whereas its dual function has value zero there. Complex constructibility is essential to both conclusions.

### A cusp retains two normal branches and their monodromy
*Difficulty: Advanced.*

Let \(Z=\{y^2=x^3\}\subset\mathbb C^2\), with its constant sheaf \(F=k_Z\). Compute its stalk and costalk at the cusp. Explain why its point specialization has rank two on the nonzero tangent line, although its central stalk has rank one.

**Solution.** The map \(t\mapsto(t^2,t^3)\) is a homeomorphism from \(\mathbb C\) onto \(Z\). It is bijective: off zero its inverse is \(t=y/x\), and zero has only the preimage zero. The inverse is continuous at zero because \(|t|^2=|x|\). This also proves properness over compact subsets. Intrinsic closed-support adjunction therefore gives stalk \(k\) and point costalk \(k[-2]\), with Euler number one for each.

For the real positive normal-deformation parameter \(a>0\), normal coordinates \((u,w)\) satisfy
\(w^2=a u^3\). Near a nonzero tangent point \((u_0,0)\), choose a small complex disk in \(u\) avoiding zero and a branch of \(u^{3/2}\). The positive chamber consists of the two graphs
\(w=\pm\sqrt a\,u^{3/2}\). For sufficiently small \(a\) both lie in the chosen vertical neighborhood. They are disjoint, and each is a product of that disk with a positive interval. The constant coefficient on each has ordinary sections \(k\) and no higher cohomology. The cofinal chamber restrictions preserve both copies. Hence specialization has rank two there. Off the tangent line it vanishes by the normal-cone support bound.

A loop in \(u\) around zero changes the sign of \(u^{3/2}\) and interchanges the two branches. The tangent-line local system consequently has transposition monodromy. Its circle cochains have \(T=\begin{pmatrix}0&1\\1&0\end{pmatrix}\); kernel and cokernel of \(T-I\) each have dimension one, even in characteristic two. The central specialization stalk is \(k\) by (2). The restriction to the invariant circle sections is the diagonal map \(c\mapsto(c,c)\): it is specialization of the constant-section unit \(k_{\mathbb C^2}\to k_Z\). This is an isomorphism onto the invariant line. The localization triangle then gives costalk \(k[-2]\), in agreement with the original cusp. The two approaching branches and their monodromy are therefore retained by specialization while the Euler equality holds.

## References

The complex stalk–costalk Euler equality and the duality of complex constructible functions belong to the calculus of constructible functions; see P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), J. Pure Appl. Algebra 72 (1991), 83–93. The specialization-and-circle argument is developed here into a complete integer argument with the point-specialization maps, orbit monodromy, proper projective projection and finite skeleton calculation. The lessons named above supply specialization, the microsupport annihilator, finite proper images and the costalk description of function duality.

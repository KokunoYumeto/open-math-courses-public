# Microlocal types and Stein cohomology

The dimension shift in a microlocal coefficient type turns the local Levi-form estimate into a cohomology theorem. On a Stein manifold, the upper microlocal cut forces ordinary cohomology to vanish in positive degrees. The lower cut forces compactly supported cohomology to vanish in negative degrees. The two proofs use different closed support tests and different limit maps. We prove both, including the degree-one inverse-limit step.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 3 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Pure and simple sheaves from directional tests, How simple-sheaf shifts change along a Lagrangian, Constructible gluing on an interval, and Holomorphic Morse exhaustions on Stein manifolds. The exact proper-image microsupport and proper-base-change proofs belong to the preceding Microsupport operations, source edition, in its section on collecting tests along a fibre; the ordinary bounded derived and exceptional-operation foundations retain their existing programme providers.

Throughout, \(k\) is a commutative ring of finite global dimension, \(X\) is a complex manifold of dimension \(n\), and \(F\) is a bounded weakly complex-constructible complex of \(k\)-module sheaves. No field, finite-generation or perfect-stalk assumption is imposed. We retain the preceding analytic conormal, regularity, rank-dimension and finite-dimensional Sard prerequisites. Their lower foundational proofs remain owned course work. The local-to-global cohomology arguments below are supplied in full.

## Normalize the coefficient before imposing a cut

At a smooth point \(p\) of \(\Lambda=\operatorname{SS}(F)\), denote the type with numerical shift zero by \(T_p(F)\). Complex Lagrangian tangent planes have even real vertical-intersection dimension, so this numerical shift is allowed.

For an integer \(a\), define the upper and lower microlocal cuts by

\[
\begin{aligned}
F\in{}^\mu D^{\leq a}(X)
&\quad\Longleftrightarrow\quad
H^j(T_p(F))=0\quad(j>a-n),\\
F\in{}^\mu D^{\geq a}(X)
&\quad\Longleftrightarrow\quad
H^j(T_p(F))=0\quad(j<a-n),
\end{aligned}
\tag{1}
\]

at every smooth point of its microsupport. The cuts are vacuous for the zero object. The notation refers to full subcategories of the specified bounded weakly complex-constructible category; their equality with the ordinary perverse cuts will be proved later.

Suppose additionally that the cotangent projection has constant rank near \(p\). The local conormal geometry and coefficient-object theorem give a complex submanifold \(Y\), of dimension \(d\), and a bounded coefficient complex \(Q\) with \(F\simeq Q_Y\) in \(D^b(X;p)\). Set \(L=Q[-d]\). The real codimension is \(2(n-d)\), and the conormal type formula gives

\[
F\simeq L_Y[d],\qquad
T_p(F)\simeq Q[n-d]=L[n].
\tag{2}
\]

Thus the condition on \(T_p(F)\) in (1) is exactly \(L\in D^{\leq a}(k)\), or \(L\in D^{\geq a}(k)\), respectively. The ambient dimension, rather than the dimension of \(Y\), is the shift of the normalized type.

It suffices in (1) to check all smooth points where projection has locally constant rank. Here is the proof of this reduction. On a smooth complex Lagrangian chart the type is locally constant as an isomorphism class of bounded complexes. The preceding continuity proof applies to arbitrary bounded coefficient complexes. For its complex specialization, multiplication by \(i\) on all arguments changes the real index form to its negative, so its signature is zero; the explicit simultaneous complex complement keeps this correction zero on a neighborhood. Hence numerical shift zero stays fixed.

Every sufficiently small connected smooth chart contains a dense open set of points where projection has constant rank. In holomorphic coordinates, take the maximal rank on that chart and a minor attaining it. The minor is a holomorphic function which is not identically zero. The holomorphic identity theorem makes its nonvanishing locus dense, and on that locus the rank is locally the same maximal rank. Shrink the chart until the type is constant there. Any point in the chart has the same type class as a constant-rank point. A cohomological cut therefore holds at every smooth point if it holds at all constant-rank ones.

This also proves that one constant-rank point suffices on each connected component of the smooth microsupport. The customary formulation with one point on each irreducible analytic component additionally uses connectedness and density of that component's regular locus. The analytic regular-locus bridge remains an explicit lower foundational obligation; this paragraph does not replace its proof or identify a connected smooth component with an irreducible component.

## A Stein exhaustion supplies both local tests

Assume now that \(X\) is Stein. The preceding lesson constructs a smooth nonnegative proper strictly plurisubharmonic exhaustion \(\varphi\) whose differential graph meets \(\Lambda\) only at regular constant-projection-rank points and transversally. Write

\[
P=\{x\in X:(x;d\varphi_x)\in\Lambda\},
\qquad \mathcal T=\varphi(P).
\tag{3}
\]

The set \(P\) is closed and discrete, and each closed sublevel contains finitely many of its points. Consequently \(\mathcal T\subset[0,\infty)\) is locally finite. Different points may have the same value. There may be infinitely many values in total.

For \(x\in P\), put \(c=\varphi(x)\) and define

\[
C_{+,x}=(R\Gamma_{\{\varphi\geq c\}}F)_x,
\qquad
C_{-,x}=(R\Gamma_{\{\varphi\leq c\}}F)_x.
\tag{4}
\]

Both supports are closed. The first test factors through \(D^b(X;d\varphi_x)\); the second factors through \(D^b(X;-d\varphi_x)\). Complex conicity makes the antipodal map preserve \(\Lambda\), including its regular constant-rank locus. Its action also takes the transverse graph intersection to the corresponding intersection for \(-\varphi\). Apply (2) separately at these two covectors. Denote the resulting coefficient complexes by \(L_+\) and \(L_-\). No identification of these two complexes is needed.

The local restricted Hessian on a \(d\)-dimensional complex submanifold has \(l\geq d\) positive eigenvalues. The preceding closed support calculation gives

\[
C_{+,x}\simeq L_+[l-d]\otimes\operatorname{or}(E_-),
\qquad
C_{-,x}\simeq L_-[d-l]\otimes\operatorname{or}(E_+).
\tag{5}
\]

Here the lower representative is normalized on its own local conormal chart; the antipodal chart has the same projected submanifold dimension. The finite free orientation lines do not change cohomological bounds. It follows that

\[
\begin{aligned}
F\in{}^\mu D^{\leq0}(X)&\Longrightarrow C_{+,x}\in D^{\leq0}(k),\\
F\in{}^\mu D^{\geq0}(X)&\Longrightarrow C_{-,x}\in D^{\geq0}(k).
\end{aligned}
\tag{6}
\]

Indeed the first cohomology group is \(H^{j+l-d}(L_+)\), which vanishes for \(j>0\); the second is \(H^{j+d-l}(L_-)\), which vanishes for \(j<0\). This uses the permitted ring \(k\) directly.

## Proper pushforward collects the local changes

Put \(G=R\varphi_*F\). Properness gives \(R\varphi_*F=R\varphi_!F\). These are bounded complexes: if \(F\) has amplitude \([b,e]\), proper base change and the finite sheaf-cohomological dimension of the real \(2n\)-manifold bound the fibre cohomology by \([b,e+2n]\). A closed fibre is handled by its exact closed direct image into \(X\), so the same dimension bound applies.

The proper-image microsupport estimate shows that, away from zero covectors, \(\operatorname{SS}(G)\) lies over \(\mathcal T\). For a nonzero covector \(\tau\,dt\) to occur over \(t\), its pullback \(\tau\,d\varphi_x\) must belong to \(\Lambda\) for some \(x\) with \(\varphi(x)=t\). Positive and negative real scaling both preserve this complex conic set, so \(x\in P\). It follows that \(G\) is locally constant on each interval of \(\mathbb R\setminus\mathcal T\). It is zero on \((-\infty,0)\). Thus \(G\) is weakly constructible for the locally finite decomposition by these points and intervals.

At \(c\in\mathcal T\), define its two line tests by

\[
J_{+,c}=(R\Gamma_{[c,\infty)}G)_c,
\qquad
J_{-,c}=(R\Gamma_{(-\infty,c]}G)_c.
\tag{7}
\]

Proper base change, with the closed-support localization triangle, gives

\[
J_{+,c}\simeq\bigoplus_{\substack{x\in P\\\varphi(x)=c}}C_{+,x},
\qquad
J_{-,c}\simeq\bigoplus_{\substack{x\in P\\\varphi(x)=c}}C_{-,x}.
\tag{8}
\]

To verify the support step, the supported complex on the compact fibre has zero stalk at every point whose corresponding signed differential avoids \(\operatorname{SS}(F)\), by the defining microsupport test. Its remaining support is the finite displayed set. A complex supported at finitely many closed points is the finite direct sum of its closed point direct images; taking sections on that fibre is therefore the direct sum of their stalk complexes. For the negative test use the antipodal-invariance of \(\Lambda\). This establishes (8) with both actual signed support functors. No finite-dimensionality of the coefficient modules is involved.

## The two interval triangles point in different directions

We prove the line calculation used at every critical value. Suppose an interval has one distinguished point \(c\), with coefficient diagram

\[
L^\bullet\xleftarrow{r_-}V^\bullet\xrightarrow{r_+}R^\bullet.
\tag{9}
\]

The bounded derived diagram theorem in the preceding interval lesson represents its restriction by these complexes and maps. Localization at either closed half-line gives

\[
J_+=\operatorname{Cone}(V^\bullet\xrightarrow{r_-}L^\bullet)[-1],
\qquad
J_-=\operatorname{Cone}(V^\bullet\xrightarrow{r_+}R^\bullet)[-1].
\tag{10}
\]

For the first formula the complement is the left open half interval, whose ordinary cohomology is \(L^\bullet\); for the second it is the right half interval with cohomology \(R^\bullet\). Taking the stalk of the respective localization triangle proves each formula, including its map.

Choose successive regular levels \(u<v\) with just \(c\) between them. Let \(U_u=(-\infty,u)\), \(U_v=(-\infty,v)\), and put \(A_u=R\Gamma(U_u;G)\), \(B_u=R\Gamma_c(U_u;G)\), with the analogous notation at \(v\). Then

\[
J_{+,c}\longrightarrow A_v\longrightarrow A_u\xrightarrow{+1},
\qquad
B_u\longrightarrow B_v\longrightarrow J_{-,c}\xrightarrow{+1}.
\tag{11}
\]

The map \(A_v\to A_u\) is restriction. Cover \(U_v\) by \(U_u\) and an interval \(W=(a,v)\) with \(a<u<c\) and no other distinguished point. The interval theorem gives \(R\Gamma(W;G)=V^\bullet\); on the overlap it gives \(L^\bullet\). The Mayer–Vietoris homotopy pullback square has map \(V^\bullet\to L^\bullet\) equal to \(r_-\). Its fibre over \(A_u\) is therefore the first cone in (10), proving the first triangle.

The map \(B_u\to B_v\) is extension of compactly supported sections by zero. Open–closed localization inside \(U_v\), followed by compact sections, has third term \(R\Gamma_c([u,v);G)\). Its left piece \([u,c)\) has zero compact cohomology for a constant complex: compactify by \([u,c]\) and remove the right endpoint; the map from cohomology of that closed interval to its endpoint is the identity. Its right open piece \((c,v)\) has compact cohomology \(R^\bullet[-1]\): compactification by \([c,v]\) gives the fibre of the diagonal map \(R^\bullet\to R^\bullet\oplus R^\bullet\). The closed point \(c\) contributes \(V^\bullet\). Consequently the remaining localization triangle is
\(R^\bullet[-1]\to R\Gamma_c([u,v);G)\to V^\bullet\to R^\bullet\).
Its last map is \(r_+\), with the chosen increasing-coordinate orientation. This can be checked on the right-hand restriction in (9), or directly in the endpoint compactification. Hence its middle term is the second cone in (10), proving the second triangle in (11).

These interval and endpoint calculations use finite free complexes and hold for arbitrary bounded module complexes. They preserve the restriction and extension maps, rather than just their dimensions. If there is no distinguished point between \(u\) and \(v\), the same calculations make both maps isomorphisms.

## Exhausting the line gives finite-stage vanishing

List the distinct values as \(c_1<c_2<\cdots\). Choose \(u_0<0\) and regular \(u_i\) between successive values so that \(u_i\to\infty\). If there are finitely many values, continue choosing increasing levels above the last one; if there are none, \(G\) is already zero. Write

\[
A_i=R\Gamma((-\infty,u_i);G),\qquad
B_i=R\Gamma_c((-\infty,u_i);G).
\tag{12}
\]

Both initial complexes are zero. Formula (11), with the finite sum (8) for all points at a given value, gives the induction:

\[
\begin{aligned}
F\in{}^\mu D^{\leq0}(X)&\Longrightarrow
H^j(A_i)=0\ (j>0),\quad
H^0(A_i)\twoheadrightarrow H^0(A_{i-1}),\\
F\in{}^\mu D^{\geq0}(X)&\Longrightarrow
H^j(B_i)=0\ (j<0).
\end{aligned}
\tag{13}
\]

For the upper assertion, \(H^j(J_{+,c})\) and \(H^{j+1}(J_{+,c})\) vanish when \(j>0\), so the restriction is an isomorphism in those degrees. At degree zero its cokernel injects into \(H^1(J_{+,c})=0\), proving surjectivity. For the lower assertion, \(H^{j-1}(J_{-,c})\) and \(H^j(J_{-,c})\) vanish when \(j<0\); thus the extension map is an isomorphism in negative degrees. These arguments also cover a step with no critical value.

To finish, we must justify passage from (13) to the whole line. Merely replacing an infinite exhaustion by its limit would leave the upper degree-one step unproved.

## Ordinary sections retain a derived inverse-limit term

Let \(Z=\bigcup_i W_i\) be an increasing countable union of open sets, and let \(K\) be a bounded-below sheaf complex. Choose a bounded-below injective resolution \(I^\bullet\). Restrictions to open sets remain injective, since open restriction is right adjoint to exact extension by zero. Injective sheaves are flasque: for open \(V\subset U\), the monomorphism \(k_V\hookrightarrow k_U\) and injectivity make
\(\operatorname{Hom}(k_U,I)\to\operatorname{Hom}(k_V,I)\), or \(\Gamma(U;I)\to\Gamma(V;I)\), surjective.

Put \(E_i^\bullet=\Gamma(W_i;I^\bullet)\), with restriction \(r_i:E_{i+1}^\bullet\to E_i^\bullet\). There is an exact sequence of complexes

\[
0\longrightarrow\Gamma(Z;I^\bullet)
\longrightarrow\prod_i E_i^\bullet
\xrightarrow{\Delta}\prod_i E_i^\bullet
\longrightarrow0,\qquad
\Delta((a_i))=(a_i-r_i(a_{i+1})).
\tag{14}
\]

The kernel is precisely compatible sections, which glue on the union. For surjectivity choose \(a_0\), then recursively lift \(a_i-b_i\) through the surjective \(r_i\); this solves \(\Delta(a)=b\) in each cochain degree. Products of modules are exact, so their cohomology is the product of the cohomology groups. The long exact sequence of (14) therefore yields

\[
0\longrightarrow
\operatorname{coker}\!\left(\Delta:\prod_iH^{j-1}(E_i)\to\prod_iH^{j-1}(E_i)\right)
\longrightarrow H^j(Z;K)
\longrightarrow
\ker\!\left(\Delta:\prod_iH^j(E_i)\to\prod_iH^j(E_i)\right)
\longrightarrow0.
\tag{15}
\]

This is the countable Milnor sequence, proved here with the actual restriction maps. The cokernel is the first derived inverse-limit term. If the maps on \(H^{j-1}(E_i)\) are surjective, the same recursion makes this cokernel zero.

Apply (15) to \(K=G\), \(W_i=(-\infty,u_i)\). For \(j>1\), both products in the relevant degrees vanish by (13). For \(j=1\), the kernel term still vanishes, and surjectivity of the degree-zero restriction maps makes the cokernel vanish. Thus

\[
H^j(\mathbb R;G)=0\qquad(j>0).
\tag{16}
\]

The module products occur after taking sections; no assertion of exact products in the category of sheaves is needed.

## Compact sections use an exact direct limit

For the same increasing union, extension by zero gives
\(\Gamma_c(W_i;I^\bullet|_{W_i})\to\Gamma_c(W_{i+1};I^\bullet|_{W_{i+1}})\).
A section with compact support inside \(W_i\) extends by zero on the complement of that support. Conversely every compact subset of \(Z\) is contained in some \(W_i\), by a finite subcover and increasingness. Hence degreewise

\[
\Gamma_c(Z;I^\bullet)=
\underset{i}{\operatorname{colim}}\,
\Gamma_c(W_i;I^\bullet|_{W_i}).
\tag{17}
\]

The restricted injective resolutions compute the right-derived compact-section functors. Filtered colimits of modules are exact: a representative becomes zero, or satisfies a finite relation, at some later stage. In particular they commute with kernels, images and cohomology. Taking cohomology in (17) gives

\[
H_c^j(Z;K)=\underset{i}{\operatorname{colim}}\,H_c^j(W_i;K).
\tag{18}
\]

There is no inverse-limit cokernel in this calculation. Apply (18) to \(G\). All its stage groups in negative degrees are zero by (13), so \(H_c^j(\mathbb R;G)=0\) for \(j<0\).

Finally, composition of ordinary direct images identifies \(R\Gamma(\mathbb R;G)\) with \(R\Gamma(X;F)\). Composition of proper direct images identifies \(R\Gamma_c(\mathbb R;G)\) with \(R\Gamma_c(X;F)\), since \(G=R\varphi_!F\). We have proved the full vanishing statement:

**Stein vanishing theorem.** For the coefficient ring and bounded weakly complex-constructible category specified above,

\[
\begin{aligned}
F\in{}^\mu D^{\leq0}(X)&\Longrightarrow H^j(X;F)=0\quad(j>0),\\
F\in{}^\mu D^{\geq0}(X)&\Longrightarrow H_c^j(X;F)=0\quad(j<0).
\end{aligned}
\tag{19}
\]

For general \(a\), apply this result to \(F[a]\). It gives ordinary vanishing above \(a\) for the upper cut \({}^\mu D^{\leq a}\), and compact vanishing below \(a\) for the lower cut \({}^\mu D^{\geq a}\). Arbitrary repeated critical values, a countably infinite exhaustion and arbitrary permitted coefficient modules are all included.

## Exercises with complete solutions

### Ambient dimension determines the type shift

*Difficulty: Introductory.*

Let \(Y\) have complex dimension \(d\) in a complex \(n\)-manifold, and let \(F=M_Y[s]\). Calculate its shift-zero type and the upper and lower microlocal cuts when \(M\) is a nonzero module in degree zero.

**Solution.** Its unshifted conormal coefficient is \(Q=M[s]\), and half the real codimension is \(n-d\). Thus \(T_p(F)=M[s+n-d]\), with its nonzero cohomology in degree \(d-n-s\). The upper condition in (1) is \(d-n-s\leq a-n\), or \(d-s\leq a\). The lower condition is \(d-n-s\geq a-n\), or \(d-s\geq a\). In particular \(s=d\) gives both cuts at \(a=0\). In the normalized form \(L_Y[d]\), the coefficient is \(L=M[s-d]\), whose nonzero degree is \(d-s\), agreeing with both inequalities.

### The two closed tests remember different arrows

*Difficulty: Intermediate.*

Over \(k=\mathbb Z\), take \(L=R=V=\mathbb Z\) in degree zero, with \(r_-=2\) and \(r_+=3\). Compute the two complexes (10).

**Solution.** For a map of degree-zero modules, its cone shifted by \(-1\) has cohomology equal to the kernel in degree zero and the cokernel in degree one. Both displayed maps are injective. Thus \(J_+\) has \(\mathbb Z/2\) in degree one, and \(J_-\) has \(\mathbb Z/3\) in degree one; all other groups vanish. Their complexes are respectively \((\mathbb Z/2)[-1]\) and \((\mathbb Z/3)[-1]\). Replacing the two arrows by one common map would lose the signed support information. The example is an interval diagram calculation, not an assertion that this particular \(G\) satisfies both Stein local-cut estimates.

### Why degree one needs more than finite-stage vanishing

*Difficulty: Advanced.*

Consider the inverse system \(E_i=\mathbb Z\) in degree zero with all transition maps multiplication by \(2\). Show that the cokernel of \(\Delta:\prod\mathbb Z\to\prod\mathbb Z\), \(\Delta(a)_i=a_i-2a_{i+1}\), is nonzero, although every stage has zero positive cohomology.

**Solution.** Define \(\mathbb Z_2=\lim_N\mathbb Z/2^N\), and map a sequence \(b\) to \(S(b)=\sum_{i\geq0}2^i b_i\) in this inverse limit. The partial sums stabilize modulo every \(2^N\), so the map is defined. It is onto, by choosing binary digits for any compatible residues. Telescoping gives \(S(\Delta(a))=a_0\) in \(\mathbb Z_2\). Conversely if \(S(b)=m\in\mathbb Z\), put
\(a_i=(m-\sum_{h<i}2^h b_h)/2^i\).
The numerator is divisible by \(2^i\), by the equality in \(\mathbb Z_2\), and direct substitution gives \(\Delta(a)=b\). Therefore the cokernel is \(\mathbb Z_2/\mathbb Z\). It is nonzero: take binary digits equal to one precisely at \(i=t!\) for integers \(t\geq2\). They are neither eventually zero nor eventually one, whereas the binary digits of a nonnegative integer are eventually zero and those of a negative integer in \(\mathbb Z_2\) are eventually one. The resulting element is not an integer. Formula (15) allows exactly such a cokernel in degree one; the surjectivity in (13) removes it in the Stein proof.

### Equal critical values still give one finite triangle

*Difficulty: Intermediate.*

Suppose three graph intersections have the same critical value \(c\). Their upper local tests are bounded complexes \(C_1,C_2,C_3\) in \(D^{\leq0}(k)\). Explain why the upper induction remains valid without separating their values.

**Solution.** Properness makes the relevant fibre compact, and its supported test complex is supported at these three points. Its section complex is \(J_{+,c}=C_1\oplus C_2\oplus C_3\). This finite direct sum still belongs to \(D^{\leq0}(k)\). The first triangle of (11) has this one term, so its long exact sequence makes the positive-degree restriction maps isomorphisms and the degree-zero map surjective. No perturbation separating values and no independence of the three maps is required. The same argument with a finite direct sum in \(D^{\geq0}\) works for the lower compact triangle.

### Compactness chooses one exhaustion stage

*Difficulty: Introductory.*

Prove that a compactly supported section on an increasing open union belongs to the extension-by-zero image of a single stage. Explain why the argument also applies to each degree of a resolution.

**Solution.** Cover the compact support \(K\) by the open sets \(W_i\). A finite subcover exists; because the family is increasing, its largest index \(m\) contains \(K\). Restrict the section to \(W_m\). It has compact support there. On \(Z\setminus K\) it is zero, so its extension by zero agrees with the original section, by the sheaf gluing axiom. Conversely extending a section whose support is compact inside \(W_m\) preserves that compact support in \(Z\). This is a statement about sections of any sheaf, so it applies separately to each sheaf \(I^q\). Extension commutes with the differential, giving the equality of complexes (17).

### Ordinary and compact cohomology occupy opposite degrees

*Difficulty: Intermediate.*

Take \(X=\mathbb C^d\), with \(F=M_X[d]\) for a nonzero \(k\)-module \(M\). Compute its ordinary and compact cohomology and compare them with (19). Include \(k=\mathbb Z\), \(M=\mathbb Z/2\).

**Solution.** The contractible space \(\mathbb C^d\) has ordinary constant-coefficient cohomology \(M\) in degree zero. Its one-point compactification is a \(2d\)-sphere, whose finite free reduced cochain model gives compact cohomology \(M\) in degree \(2d\). The shift by \(d\) puts ordinary cohomology in degree \(-d\) and compact cohomology in degree \(d\). Its normalized type is \(M[d]\) at zero-section points, namely \(M[n]\) with \(n=d\), so both microlocal cuts are zero. The two computed degrees satisfy (19). The same finite free sphere calculation gives these answers for \(\mathbb Z/2\); field duality or flatness of \(M\) is unnecessary.

### Shift the complete vanishing statement

*Difficulty: Intermediate.*

Let \(F\in{}^\mu D^{\leq a}(X)\) or \(F\in{}^\mu D^{\geq a}(X)\). Derive the general degree bounds from (19), checking the direction of the shift.

**Solution.** Type is compatible with coefficient shifts, so \(T_p(F[a])=T_p(F)[a]\). Its degree-\(j\) group is \(H^{j+a}(T_p(F))\). The upper bound \(a-n\) for \(F\) therefore becomes \(-n\) for \(F[a]\), and the lower bound does the same. Apply (19) to \(F[a]\). Since \(H^j(X;F[a])=H^{j+a}(X;F)\), its positive-degree vanishing says \(H^h(X;F)=0\) for \(h>a\). Compact negative-degree vanishing says \(H_c^h(X;F)=0\) for \(h<a\). Replacing \([a]\) by \([-a]\) would produce the wrong thresholds.

## Sources and the next comparison

Microlocal types and their relation to perverse sheaves are part of Kashiwara and Schapira's theory of pure sheaves; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §9.5 (perverse sheaves and pure sheaves). The zero complex inertia statement and the type-continuity argument are proved in the preceding lessons.

The accessible article by Yongqiang Liu, Laurenţiu Maxim and Botong Wang, [Non-abelian Mellin transformations and applications (2022), Theorem 2.3](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/nonabelian-mellin-transformations-and-applications/6DABA2C08D3CDA4BB9989AA548FC5D02), states the ordinary perverse version for its Noetherian coefficient rings and points to the Kashiwara–Schapira proof. It is a later application and context source. The complete exhaustion, local tests, interval triangles and both limit arguments are supplied inside this course.

For subsequent developments, Olivier Benoist's [On the Artin vanishing theorem for Stein spaces (2025)](https://www.math.ens.psl.eu/~benoist/articles/Artinvanishing.pdf), §3.1, studies relative cohomology with respect to holomorphically convex compact subsets, including singular Stein spaces. That broader setting requires additional geometry; the result proved here retains the full Stein-manifold statement.

The next steps are the full transverse-restriction and specialization arguments and the equality between microlocal and ordinary perverse cuts. The one-point-per-irreducible-component criterion also retains its precise analytic regular-locus prerequisite. None of these later claims is inferred merely from (19).

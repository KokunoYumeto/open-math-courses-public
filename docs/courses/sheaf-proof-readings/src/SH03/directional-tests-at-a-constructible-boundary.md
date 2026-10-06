# Directional tests at a constructible boundary

The restriction maps of a constructible sheaf tell us which direction can obstruct continuation across a boundary. On an interval, this can be calculated without a coordinate-free microlocal construction: one cone measures the positive direction and another measures the negative direction. The calculation gives a complete microsupport description for the one-point model, including open and closed supports and their different cohomological shifts.

The prerequisite is Constructible gluing on an interval. We also use the definition of microsupport by local cohomology tests, taught in Detecting and removing directional obstructions. The source account below credits the classical definition and examples and explains the direct interval proof.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Two local cohomology complexes

Keep \(I=(-1,1)\) with distinguished point zero. Let \(k\) be a commutative ring of finite global dimension. Represent a bounded complex with constructible cohomology for these three pieces by

\[
L^\bullet\xleftarrow{r_-}V^\bullet\xrightarrow{r_+}R^\bullet.
\tag{1}
\]

The neighboring complexes may have arbitrary coefficient modules. Perfection is not assumed. Define

\[
J_+(F)=\bigl(R\Gamma_{\{t\geq0\}}F\bigr)_0,
\qquad
J_-(F)=\bigl(R\Gamma_{\{t\leq0\}}F\bigr)_0.
\tag{2}
\]

These are local cohomology with support in a closed half interval, evaluated at its boundary. They differ from the costalk at a point, whose support is the point itself.

**Proposition 1.** There are natural isomorphisms

\[
J_+(F)\simeq\operatorname{Cone}(V^\bullet\xrightarrow{r_-}L^\bullet)[-1],
\qquad
J_-(F)\simeq\operatorname{Cone}(V^\bullet\xrightarrow{r_+}R^\bullet)[-1].
\tag{3}
\]

**Proof.** The complement of \(\{t\geq0\}\) is the negative half interval. The localization triangle at zero is therefore

\[
J_+(F)\longrightarrow V^\bullet\longrightarrow
\bigl(Rj_{-*}j_-^{-1}F\bigr)_0\longrightarrow J_+(F)[1].
\]

On a sufficiently small negative half interval, the complex is constant with value \(L^\bullet\). Ordinary cohomology of that interval is \(L^\bullet\), and the map from the stalk at zero is \(r_-\). The fibre is the first cone in (3). The other closed half interval has positive complement, which gives the second cone. \(\square\)

The plus sign in \(J_+\) refers to the support inequality, so its cone uses the restriction to the *opposite*, negative side. This convention will determine the covector sign below.

## Microsupport from monotone tests

Identify \(T^*I\) with pairs \((t,\xi)\), where the covector is \(\xi\,dt\). By definition, \((t_0,\xi_0)\) is absent from \(\operatorname{SS}(F)\) if there is a cotangent neighborhood on which every local test

\[
\bigl(R\Gamma_{\{\varphi\geq\varphi(t)\}}F\bigr)_t
\]

vanishes when \(\varphi\) is \(C^1\) and \((t,d\varphi_t)\) belongs to that neighborhood. The neighborhood must control both base point and covector; testing one function at one point is insufficient for proving absence.

**Theorem 2.** At the distinguished point,

\[
\begin{aligned}
\operatorname{SS}(F)\cap\{(0,\xi):\xi>0\}
&=\begin{cases}\varnothing,&r_-\text{ is a quasi-isomorphism},\\
\{(0,\xi):\xi>0\},&r_-\text{ is not a quasi-isomorphism},\end{cases}\\
\operatorname{SS}(F)\cap\{(0,\xi):\xi<0\}
&=\begin{cases}\varnothing,&r_+\text{ is a quasi-isomorphism},\\
\{(0,\xi):\xi<0\},&r_+\text{ is not a quasi-isomorphism}.\end{cases}
\end{aligned}
\tag{4}
\]

Away from zero there are no nonzero covectors in the microsupport. Its intersection with the zero section is the closed support of \(F\).

**Proof.** Suppose \(r_-\) is not a quasi-isomorphism. Then \(J_+(F)\neq0\) by (3). For any \(\xi>0\), the function \(\varphi(t)=\xi t\) has support inequality \(t\geq0\) at zero. Its test complex is \(J_+(F)\). Thus every positive covector at zero fails a test and belongs to microsupport.

Now suppose \(r_-\) is a quasi-isomorphism and fix \(\xi_0>0\). Choose a cotangent neighborhood whose covector coordinates are positive. For any test function and any base point in this neighborhood, continuity of its derivative makes it strictly increasing on some neighborhood of that base point. At zero, its closed support inequality is locally \(t\geq0\), and (3) makes its test vanish. At a nonzero base point, shrink the neighborhood to one side of zero. The sheaf complex is constant there. The local support complex is the fibre of the restriction isomorphism \(C\xrightarrow{\sim}C\), so it is zero. Every required test therefore vanishes throughout the cotangent neighborhood. This proves absence of \((0,\xi_0)\). The proof for negative covectors uses decreasing functions and \(J_-(F)\).

The same constant-complex calculation proves absence of nonzero covectors away from zero. For the zero section, a point outside the closed support has a neighborhood on which the complex vanishes, so all tests vanish. Conversely, suppose a point lies in the closed support. Every base neighborhood meets a point with a nonzero cohomology stalk. At that nearby point a constant test function has zero differential and support equal to the entire local neighborhood. Its test is that nonzero stalk. Hence no cotangent neighborhood of the original zero covector can satisfy the vanishing criterion. This proves the zero-section assertion. \(\square\)

In this model, \(\operatorname{SS}(F)\) contains only zero covectors near zero exactly when both arrows in (1) are quasi-isomorphisms. In that case the map from the constant complex \(V^\bullet_I\) to (1), with components \(r_-,\mathrm{id},r_+\), is a stalkwise quasi-isomorphism. Thus the microsupport criterion recovers local constancy of the whole complex, including its extension data.

## Open and closed boundary conditions

Assume \(k\neq0\). Consider the positive half interval. Extension by zero from its open interior has diagram

\[
0\leftarrow0\longrightarrow k.
\]

Its positive test vanishes. Its negative test is \(k[-1]\), and its nonzero boundary covectors are negative. The sheaf supported on the closed half interval has diagram

\[
0\leftarrow k\xrightarrow{\mathrm{id}}k.
\]

Its positive test is \(k\). Its negative test vanishes, and its nonzero boundary covectors are positive. These two choices differ both in covector direction and in the degree of the nonzero test.

For a shift by \([s]\), local cohomology commutes with the shift. The open-boundary test becomes \(k[s-1]\), with cohomology in degree \(1-s\). The closed-boundary test becomes \(k[s]\), with cohomology in degree \(-s\). Microsupport itself is unchanged by the shift. Keeping the test complex, rather than only its support, retains this degree information.

The skyscraper diagram \(0\leftarrow k\to0\) has \(J_+=J_-=k\). It therefore has the full cotangent fibre over zero. The constant diagram \(k\leftarrow k\to k\), with identity arrows, has both tests zero and only the zero section as microsupport.

## The fixed diagram's test and comparison maps

Return to the integral attachment diagram, with \(r_-=2q\), \(r_+=q\), \(q(a,b)=a+2b\) and \(u=(-2,1)\). Formula (3) gives the positive test \([\,\mathbb Z^2\xrightarrow{2q}\mathbb Z\,]\) in degrees zero and one, with kernel \(\mathbb Zu\) and cokernel \(\mathbb Z/2\). The negative test \([\,\mathbb Z^2\xrightarrow q\mathbb Z\,]\) has that same kernel and zero cokernel. Consequently neither test vanishes. Both positive and negative boundary covectors occur by (4), although the negative test's attachment is surjective.

The point costalk \([\,V\xrightarrow{(2q,q)}L\oplus R\,]\) maps to these two tests by projection of the degree-one term and identity on \(V\). Projection to \(L\) is the identity on degree-zero cohomology and reduction \(\mathbb Z\to\mathbb Z/2\) on degree-one cohomology, under the costalk quotient coordinate \(x-2y\). Its preceding map \(R\to H^1(i^!E)\) is \(-2\), since the inclusion of the kernel complex sends \(y\) to \((0,y)\). This is the same exact comparison (B4), with the same simultaneous cone-sign normalization. Projection to \(R\) has zero degree-one target. Directional tests forget different parts of the combined attachment; they do not replace the point costalk.

The perverse origin correction keeps the degree-zero costalk kernel and its exceptional counit. It is therefore sensitive to the map information that the directional computation retains. The abstract t-structure proof and the arbitrary-coefficient geometric estimate remain separate steps of that route.

## A kernel application

Let \(h:I\to J\) be a diffeomorphism of intervals with \(h(0)=0\). Its graph kernel implements the exact direct image. The cotangent transformation from Sheaf kernels and cotangent correspondences is

\[
(t,\xi)\longmapsto(h(t),\xi/h'(t)).
\tag{5}
\]

If \(h'(0)>0\), it preserves positive and negative directions, and it preserves which of \(r_-\) and \(r_+\) is tested. If \(h'(0)<0\), it interchanges the two sides. The pushed-forward diagram has left value \(R^\bullet\), middle value \(V^\bullet\), and right value \(L^\bullet\); its two arrows are the old \(r_+\) and \(r_-\). Formula (4) then swaps the two test complexes, just as (5) swaps their cotangent directions. No additional shift occurs for a diffeomorphism.

## Exercises with solutions

### The punctured interval

*Difficulty: Introductory.*

Take the direct sum of the two open half-interval extensions with value \(k\neq0\). Determine the boundary tests, costalk and microsupport.

**Solution.** The diagram is \(k\leftarrow0\to k\). The two tests are both \(k[-1]\), so every nonzero covector at zero belongs to microsupport. Away from zero only zero covectors occur. At zero the costalk is \((k\oplus k)[-1]\), because it is the fibre of \(0\to k\oplus k\). Its zero covector also belongs to microsupport: the stalk at zero is zero, but zero lies in the closed support. This distinguishes closed support from the set of nonzero stalks.

### One direction with torsion

*Difficulty: Intermediate.*

Let \(k=\mathbb Z\), \(V=L=R=\mathbb Z\), \(r_-(v)=5v\), and \(r_+(v)=v\). Compute the two boundary tests and identify all nonzero covectors at zero.

**Solution.** The map to \(L\) is injective with cokernel \(\mathbb Z/5\). Thus \(J_+=\mathbb Z/5[-1]\). The map to \(R\) is an isomorphism, so \(J_-=0\). Exactly the positive boundary covectors occur. The test detects torsion even though every stalk of the original sheaf is free.

### Reversing the interval

*Difficulty: Intermediate.*

Push the preceding sheaf forward by \(h(t)=-t\). Give its diagram and test complexes, and check the cotangent sign.

**Solution.** The new diagram still has three copies of \(\mathbb Z\), but the left arrow is the identity and the right arrow is multiplication by five. Hence its positive test is zero and its negative test is \(\mathbb Z/5[-1]\). Formula (5) sends \((0,\xi)\) to \((0,-\xi)\), so it takes the old positive covectors to the new negative ones.

### Euler signs of the directional tests

*Difficulty: Intermediate.*

Work over a field and take perfect complexes in (1). Prove

\[
\chi(J_+)=\chi(V)-\chi(L),\qquad
\chi(J_-)=\chi(V)-\chi(R).
\]

Compare the positive and negative open half intervals with their closed counterparts.

**Solution.** Apply additivity of Euler characteristic to the two fibre triangles in Proposition 1. The open positive half has \(J_+=0\), \(J_-=k[-1]\), so its pair of Euler characteristics is \((0,-1)\). The closed positive half has pair \((1,0)\). Reversing the interval exchanges the entries: the open negative half gives \((-1,0)\), and the closed negative half gives \((0,1)\). These are Euler characteristics of the specified local test complexes; orientations for a characteristic cycle still require their own definition.

### A branched map

*Difficulty: Advanced.*

Let \(f:\mathbb R\to\mathbb R\) be \(f(t)=t^2\), and let \(k\neq0\). Determine \(Rf_*k_{\mathbb R}\) near zero, its two boundary tests, and its nonzero microsupport directions. Compare with the cotangent direct-image estimate.

**Solution.** The map is proper and its fibres are finite. Proper base change shows that higher cohomology sheaves vanish, and gives stalks zero on the negative side, \(k\) at zero, and \(k\oplus k\) on the positive side. A constant section near the source point zero restricts to the same value on the two positive preimages. Thus the local diagram is \(0\leftarrow k\xrightarrow{\Delta}k\oplus k\), where \(\Delta(v)=(v,v)\). Its positive test is \(k\) and its negative test is \(k[-1]\), since the diagonal is injective with cokernel \(k\). Both boundary directions occur. In the cotangent estimate, a target covector \(\xi\) pulls back to \(2t\xi\). It belongs to the zero-section microsupport of the source constant sheaf only if \(2t\xi=0\). At \(t=0\), every target covector is permitted; away from zero only the zero covector is permitted. Thus the estimate agrees exactly with the computed nonzero boundary fibre in this example. The calculation is for a real branched map; it does not assert a general equality for finite complex-analytic maps.

## References

**Microsupport and the half-space signs.** Pierre Schapira, [*A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §2.2, Definition 2.3 and Example 2.5, pp. 6–8, gives the local-cohomology definition, the closed-support zero section and the open/closed half-space examples. The theory and these standard examples are due to Kashiwara and Schapira. The notes work with bounded complexes over a commutative ring of finite global dimension; they do not impose perfect stalks for this definition. That matches the arbitrary-module boundary tests here. The half-space signs and shift invariance are classical facts, not discoveries from changing the numerical examples.

**What proves the interval formulas.** We use the definition itself after the interval diagram realization. The supported-cohomology triangle takes the fibre of the attachment to the opposite half interval. A test with nonzero derivative is locally monotone, which gives the complete neighborhood test for absence. Linear tests witness presence; constant tests at nearby nonzero stalks supply the closed-support zero section even when the stalk at the boundary is zero. This proves the two formulas and their degree information without using the general involutivity theorem or a general cutoff theorem. The fibre comparison also retains the integral example's reduction modulo two and its preceding negative multiplication map. The classical open and closed boundary cases are applications of this calculation.

**Images and examples.** Theorem 2.9 of the same notes, pp. 10–11, states and proves the proper-on-support direct-image bound using local cohomology and the proper fibre formula. It explains the estimate compared with the final branched-map exercise. The actual stalks, diagonal attachment, two nonzero tests and cotangent equation for that example are calculated in the solution; a general equality under proper direct image is not assumed. The diffeomorphism exercise follows by transporting the attachment diagram and using the inverse derivative on covectors.

**Proof and expression scope.** The exposition is organized around the two attachment maps and their relation to the point costalk, then follows the same integral diagram into the perverse lesson. It retains complete solutions and gives the one-dimensional proof rather than treating the survey's examples as supplied proofs. The preceding diagram lesson, local cohomology, constant-interval acyclicity and proper base change are the exact foundational inputs. Their complete transitive proof clearance, and that of the later general kernel and perverse constructions, remain separate obligations. Independently written programme text is CC0; separately linked human-derived components retain their own stated terms.

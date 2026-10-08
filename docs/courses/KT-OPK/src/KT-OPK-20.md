# Irrational rotation algebras

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Independently authored CC0 lesson; self-checked by the writing AI.*

The groups of a rotation algebra do not depend on its angle, but their trace pairing does. For an irrational angle the trace detects every stable projection class. An explicit projection then determines the positive cone, and the normalized trace distinguishes the algebras themselves.

We use the [Pimsner–Voiculescu sequence](KT-OPK-18.md), the [trace range theorem](KT-OPK-19.md), and [smooth action algebras](KT-OPK-15.md). Write \(\mathbb T=\mathbb R/\mathbb Z\), \(z(t)=e^{2\pi it}\), and use unnormalized matrix traces throughout.

## 1. Covariance fixes the angle

For \(\theta\in\mathbb R\), define an automorphism of \(C(\mathbb T)\) by

\[
\begin{gathered}
\alpha_\theta(h)(t)=h(t+\theta),\\
A_\theta=C(\mathbb T)\rtimes_{\alpha_\theta}\mathbb Z.
\end{gathered}
\tag{1.1}
\]

Let \(u\) be the coefficient function \(z\) and \(v\) the implementing unitary. Thus

\[
vuv^*=e^{2\pi i\theta}u,\qquad
vu=e^{2\pi i\theta}uv.
\tag{1.2}
\]

In the inverse-pullback convention for actions on functions, (1.1) is the action of the geometric rotation \(t\mapsto t-\theta\). Using the geometric rotation by \(+\theta\) instead gives \(\alpha_{-\theta}\). Keeping this distinction explicit prevents an erroneous determinant sign.

**Proposition 1.1 (universal property).** Given unitaries \(a,b\) in a unital C*-algebra \(D\) satisfying \(ba=e^{2\pi i\theta}ab\), there is a unique unital *-homomorphism \(A_\theta\to D\) sending \(u\) to \(a\) and \(v\) to \(b\).

*Proof.* Continuous functional calculus gives \(\pi:C(\mathbb T)\to D\), \(\pi(h)=h(a)\). The relation and its adjoint give
\(b\pi(z^k)b^*=\pi(\alpha_\theta(z^k))\) for every integer \(k\). Density of Laurent polynomials extends covariance to every \(h\). The universal crossed-product property integrates \((\pi,b)\). Conversely, the canonical pair satisfies (1.2); it generates the crossed product, since its coefficient algebra and all implementing powers generate the dense finite sums. This also proves uniqueness and identifies the crossed product with the universal algebra of the two unitaries. \(\square\)

The relation is unchanged by adding an integer to \(\theta\). Replacing \(v\) by \(v^*\) changes the parameter to \(-\theta\). Applying these replacements twice gives inverse homomorphisms, so

\[
A_{\theta+k}\cong A_\theta\cong A_{-\theta}
\qquad(k\in\mathbb Z).
\tag{1.3}
\]

**Proposition 1.2.** If \(\theta\) is irrational, \(A_\theta\) is simple and has a unique tracial state \(\tau\). It is faithful, and

\[
\tau(u^m v^n)=
\begin{cases}1,&(m,n)=(0,0),\\0,&\text{otherwise}.\end{cases}
\tag{1.4}
\]

*Proof.* An irrational rotation is free and minimal: no nonzero power has a fixed point, and its generated subgroup is dense in the circle. The subgroup argument is given in Lesson 19, Exercise 19.5. The simplicity criterion [KT-CP-03, Corollary 3.6](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-03.html#minimality-removes-the-remaining-ideals) applies to the reduced crossed product. Full and reduced products agree for \(\mathbb Z\), by KT-CP-05, Proposition 5.1, so it applies here.

Haar integration \(\tau_0\) on the coefficient circle is invariant and faithful. The faithful expectation \(E\) gives the faithful tracial state \(\tau=\tau_0E\), by KT-CP-03, Theorem 3.1 and Proposition 3.2. This gives (1.4).

If \(\rho\) is any tracial state, conjugation by \(v\) multiplies \(u^m v^n\) by \(e^{2\pi i m\theta}\), and conjugation by \(u\) multiplies it by \(e^{-2\pi i n\theta}\). Trace invariance under both conjugations forces its value to vanish unless \(m=n=0\). It equals one there. Density of the finite sums proves \(\rho=\tau\). Thus trace uniqueness has been proved on the crossed product itself. \(\square\)

For every real \(\theta\), the Haar trace \(\tau_0E\) still exists and is faithful. Only its uniqueness will require irrationality below.

## 2. The two K-groups for every angle

The path \(s\mapsto\alpha_{s\theta}\), \(0\leq s\leq1\), is continuous in norm on each coefficient function. Homotopy invariance makes both \(\alpha_{\theta,*}\) identity maps. Since
\(K_0(C(\mathbb T))=\mathbb Z[1]\) and \(K_1(C(\mathbb T))=\mathbb Z[z]\), the sequence of Lesson 18 gives

\[
\begin{gathered}
0\longrightarrow\mathbb Z[1]
 \xrightarrow{\iota_*}K_0(A_\theta),\\
K_0(A_\theta)\xrightarrow{d_0}\mathbb Z[z]\longrightarrow0;\\
0\longrightarrow\mathbb Z[z]
 \xrightarrow{\iota_*}K_1(A_\theta),\\
K_1(A_\theta)\xrightarrow{d_1}\mathbb Z[1]\longrightarrow0.
\end{gathered}
\tag{2.1}
\]

**Theorem 2.1.** For every \(\theta\in\mathbb R\),

\[
\begin{gathered}
K_0(A_\theta)\cong\mathbb Z^2,\\
K_1(A_\theta)=\mathbb Z[u]\oplus\mathbb Z[v].
\end{gathered}
\tag{2.2}
\]

*Proof.* Each rightmost group in (2.1) is free. Choose a lift of its generator; its integer multiples define a splitting. The resulting direct sums prove the abstract group assertions and show that \([1]\) is primitive in \(K_0\).

To identify the second \(K_1\)-generator, use the equivariant unital inclusion \(\mathbb C\to C(\mathbb T)\), with the trivial action on \(\mathbb C\). Its crossed-product map \(C(\mathbb T)\to A_\theta\) sends the scalar system's implementing circle coordinate to \(v\). In that scalar system the PV boundary is an isomorphism \(\mathbb Z[z]\to\mathbb Z[1]\), hence sends \([z]\) to \(\pm[1]\). Naturality therefore gives \(d_1[v]=\pm[1]\). The left injection in (2.1) sends \([z]\) to \([u]\). A generator of the kernel together with an element mapping to a generator of the quotient is a basis: subtract a multiple of \([v]\) from any class, then use the kernel; applying \(d_1\) also proves independence. No numerical choice of the boundary's sign is needed. \(\square\)

## 3. The trace determines the stable classes

Use the matrix extension \(\tau_r=\tau\circ\operatorname{Tr}_r\) to define \(\tau_*:K_0(A_\theta)\to\mathbb R\). On \(K_0(C(\mathbb T))\) the coefficient trace has range \(\mathbb Z\). The action fixes every circle \(K_1\)-class. For its generator the relative unitary used in Lesson 19 is

\[
z\alpha_\theta(z^*)=e^{-2\pi i\theta}1.
\tag{3.1}
\]

The path \(s\mapsto e^{-2\pi i s\theta}1\) has trace integral \(-\theta\), so its determinant is \(-\theta\) modulo \(\mathbb Z\). On \([z^k]\) it is \(-k\theta\) modulo \(\mathbb Z\). Lesson 19, Theorem 4.1 identifies the full trace range with the inverse image of this determinant subgroup under \(\mathbb R\to\mathbb R/\mathbb Z\). Consequently

\[
\tau_*(K_0(A_\theta))=\mathbb Z+\theta\mathbb Z.
\tag{3.2}
\]

This holds even for rational angles. Changing the action to \(\alpha_{-\theta}\) changes the displayed determinant to \(+\theta\), while leaving (3.2) unchanged.

**Theorem 3.1.** For irrational \(\theta\), the map

\[
\tau_*:K_0(A_\theta)\longrightarrow
\mathbb Z+\theta\mathbb Z
\tag{3.3}
\]

is an isomorphism of abelian groups and sends \([1]\) to \(1\).

*Proof.* Irrationality makes \(1,\theta\) an integral basis of the subgroup on the right. The domain is free of rank two by Theorem 2.1, and (3.2) proves surjectivity. A surjective homomorphism between two rank-two free abelian groups has zero kernel: tensoring with \(\mathbb Q\) gives an isomorphism, so the kernel has rank zero; as a subgroup of a free group it is torsion free and therefore zero. Normalization gives the unit assertion. \(\square\)

This supplies the trace isomorphism used as input in formula (8.3) of [Connections and curvature from symmetries of an algebra](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/connections-and-curvature-for-c-star-dynamical-systems.html#8-constant-curvature-and-its-normalization). Its frame and curvature proofs are separate from the present computation.

## 4. The same Powers–Rieffel projection

Suppose \(0<\theta<1\). The geometry lesson's relation (6.1) is \(UV=e^{2\pi i\theta}VU\). Identify its generators by

\[
U=u,\qquad V=v^*.
\tag{4.1}
\]

Then its projection (6.2), \(V^*g(U)+f(U)+g(U)V\), is exactly

\[
e_\theta=g(u)v^*+f(u)+vg(u).
\tag{4.2}
\]

Thus we use the functions and supports from [NCG-CYCLIC, §6 and Proposition 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/connections-and-curvature-for-c-star-dynamical-systems.html#6-the-smooth-rotation-algebra), with the explicit generator identification (4.1).

Here are the functions needed to verify the projection. Choose
\(0<a<b<a+\theta<b+\theta<1\). Let \(H\) be a smooth increasing step from zero to one on \([a,b]\), flat at its ends, and put \(F=\sin^2(\pi H/2)\). Write \(I_r=[a,b]\), \(I_p=[b,a+\theta]\), and \(I_f=[a+\theta,b+\theta]\); on \(I_f\) write \(F_\theta(t)=F(t-\theta)\). Define the periodic functions

\[
f(t)=
\begin{cases}
F(t),&t\in I_r,\\
1,&t\in I_p,\\
1-F_\theta(t),&t\in I_f,\\
0,&\text{otherwise},
\end{cases}
\tag{4.3}
\]

and \(g(t)=\sqrt{f(t)-f(t)^2}\) on the falling interval \([a+\theta,b+\theta]\), zero elsewhere. These are smooth: the square root there is the translate of \(\sin(\pi H/2)\cos(\pi H/2)\), flat at both ends. Such intervals exist by choosing \(b-a<\min(\theta,1-\theta)\) and then a sufficiently small positive \(a\).

**Proposition 4.1.** The element (4.2) is a smooth orthogonal projection and \(\tau(e_\theta)=\theta\).

*Proof.* Set \(W=v^*\), so \(Wh(u)W^*=h(t-\theta)\). Write \(g_+(t)=g(t+\theta)\). Formula (4.2) becomes
\(e_\theta=f+gW+g_+W^{-1}\), and is self-adjoint. Coefficients multiply by

\[
\begin{aligned}
&(hW^j)(kW^\ell)\\
&\quad=h(t)k(t-j\theta)W^{j+\ell}.
\end{aligned}
\tag{4.4}
\]

The construction gives the three identities

\[
\begin{gathered}
f^2+g^2+g_+^2=f,\\
g(t)\bigl(f(t)+f(t-\theta)\bigr)=g(t),\\
g(t)g(t-\theta)=0.
\end{gathered}
\tag{4.5}
\]

For the first, \(g^2\) supplies \(f-f^2\) on the falling interval and \(g_+^2\) supplies it on the rising interval; elsewhere \(f\) is zero or one. On the falling interval \(f(t)+f(t-\theta)=1\), proving the second. The support interval of \(g\) and its translate by \(\theta\) are disjoint on the circle because its length is less than both \(\theta\) and \(1-\theta\), proving the third. Equations (4.4)–(4.5) give the coefficients of \(W^0,W^1,W^2\) in \(e_\theta^2=e_\theta\). The two negative coefficients follow by adjoints. These are all possible coefficients, so the equality is proved.

The trace deletes the nonzero powers of \(W\), giving \(\tau(e_\theta)=\int_0^1 f(t)dt\). The two transition integrals sum to \(b-a\), since one is \(F\) and the other its translated complement. The plateau has length \(\theta-(b-a)\). Their sum is \(\theta\). Smoothness follows from the smooth functions and the smooth torus action on the generators. \(\square\)

For irrational \(0<\theta<1\), Theorem 3.1 now proves

\[
\begin{gathered}
K_0(A_\theta)=\mathbb Z[1]\oplus\mathbb Z[e_\theta],\\
\tau_*(m[1]+n[e_\theta])=m+n\theta.
\end{gathered}
\tag{4.6}
\]

This basis assertion uses trace injectivity, rather than presuming the projection generates before its trace is known. For any irrational parameter, first use its fractional part and the isomorphism (1.3).

### An alternative trace calculation with interval indicators

The trace range can also be obtained by enlarging the coefficient algebra until its degree-one K-group vanishes. This is the discontinuous-function method of Cuntz [1981 II, §2.5, printed p. 107]. We supply the interval algebra, its finite stages and the trace computation explicitly. The resulting theorem is the same trace-range theorem as in §3, but the proof uses PV directly rather than the determinant range theorem.

Fix an irrational \(0<\theta<1\). Retain this lesson's convention
\(\alpha(h)(t)=h(t+\theta)\) on \(\mathbb T=\mathbb R/\mathbb Z\), and put
\(f=1_{[0,\theta)}\). The functions here are actual bounded functions with the supremum norm; they are not classes modulo sets of measure zero. Every circular arc below includes its initial endpoint and excludes its terminal endpoint. Let \(D\) be the smallest closed unital *-subalgebra of \(\ell^\infty(\mathbb T)\) containing \(C(\mathbb T)\) and \(f\), and invariant under both \(\alpha\) and \(\alpha^{-1}\).

**Proposition 4.2 (Cuntz's interval enlargement).** The algebra \(D\) is a commutative sequential AF algebra, and \(K_1(D)=0\). Haar integration extends to an invariant tracial state \(\mu\) on \(D\), with
\[
\mu_*(K_0(D))=\mathbb Z+\theta\mathbb Z.
\tag{4.7}
\]
If \(C=D\rtimes_\alpha\mathbb Z\), the natural equivariant coefficient inclusion induces a unital embedding
\(\eta:A_\theta\to C\). With \(\widehat\mu=\mu E_D\),
\[
\begin{gathered}
\widehat\mu_*(K_0(C))=\mathbb Z+\theta\mathbb Z,\\
\widehat\mu\eta=\tau.
\end{gathered}
\tag{4.8}
\]
Consequently \(\tau_*(K_0(A_\theta))\subseteq\mathbb Z+\theta\mathbb Z\). The unit and the projection of Proposition 4.1 give the reverse containment. Thus this proves the irrational trace-range formula independently of Lesson 19, Theorem 4.1.

*Proof.* Put \(\Gamma=\{\{m\theta\}:m\in\mathbb Z\}\subset[0,1)\), where braces denote fractional part, and let \(\rho=\alpha^{-1}\), so \(\rho h(t)=h(t-\theta)\). For each integer \(m\), define
\[
S_m=
\begin{cases}
\sum_{k=0}^{m-1}\rho^k f,&m>0,\\
0,&m=0,\\
-\sum_{k=m}^{-1}\rho^k f,&m<0.
\end{cases}
\]
These functions satisfy the exact pointwise identity
\[
S_m(t)=\lfloor m\theta\rfloor+1_{[0,\{m\theta\})}(t).
\tag{4.9}
\]
To check it including endpoints, take the representative \(0\le t<1\). For \(m>0\), \(\rho^kf\) indicates the image modulo one of the half-open real interval \([k\theta,(k+1)\theta)\). These intervals partition \([0,m\theta)\) before reduction modulo one. Write \(m\theta=l+a\), \(l=\lfloor m\theta\rfloor\), \(0\le a<1\). The \(l\) complete unit intervals cover the circle \(l\) times, and the remainder covers \([0,a)\) once. For \(m<0\), the signed sum counts the interval \([m\theta,0)\) negatively. If \(m\theta=l+a\), the interval contributes \(-(-l-1)\) full covers and one negative cover of \([a,1)\), which is \(l+1_{[0,a)}\). The case \(m=0\) is immediate. The half-open endpoint rule makes all these identities literal everywhere.

It follows that \(1_{[0,a)}\in D\) for every \(a\in\Gamma\). Translating by \(\rho^r\) gives the indicator of every circular arc starting at \(\{r\theta\}\) and having length \(\{m\theta\}\). In particular every circular arc with distinct endpoints in \(\Gamma\) lies in \(D\), since their difference modulo one has that form.

Enumerate \(\Gamma\) and choose increasing finite endpoint sets \(Q_r\) containing both 0 and \(\theta\) whose union is \(\Gamma\). Arrange each set in circular order and partition the circle into its successive half-open arcs. Let \(F_r\) be the functions constant on these arcs. Each \(F_r\) is a finite-dimensional algebra \(\mathbb C^{|Q_r|}\), generated by the arc indicators, and \(F_r\subset F_{r+1}\subset D\). Irrationality makes \(\Gamma\) dense, as proved in Lesson 19, Exercise 19.5. The largest arc length in these partitions tends to zero. Indeed, for a prescribed positive length, a finite subset of the dense endpoint set already divides the circle into shorter arcs, and that subset eventually lies in \(Q_r\).

Uniform continuity now shows that every \(h\in C(\mathbb T)\) is a uniform limit of these step functions: on each arc choose a point and use its function value. The maximum error tends to zero with the maximum arc length. The closure \(D_0=\overline{\bigcup_rF_r}\) therefore contains \(C(\mathbb T)\) and \(f\). It is invariant under \(\alpha^{\pm1}\), because these maps translate arc endpoints within \(\Gamma\). Thus minimality of \(D\) gives \(D\subseteq D_0\); the converse was proved by the indicator construction. This establishes the exact sequential AF presentation \(D=D_0\).

The exact sequential AF presentation and [Lesson 16, Proposition 1.1](KT-OPK-16.md#1-af-algebras-and-their-complete-invariant) now give \(K_1(D)=0\). That proof contracts every finite-stage matrix unitary through its polar and spectral paths and then uses K-theory continuity.

Integration is well-defined on the actual step functions and their uniform closure: every such function is bounded and Borel measurable, and \(|\int h|\le\|h\|_\infty\). It is positive, has value one at the unit, and is invariant under the circle translations. As \(D\) is commutative it is a trace. On \(F_r\), the \(K_0\)-pairing sends the basis class of an arc indicator to the length of that arc. The ordered rank computation for finite sums of scalars and the full continuity theorem in Lesson 5, Theorem 3.3, imply that every class of \(K_0(D)\) comes from one such stage. Its trace is an integer combination of arc lengths. Each length is \(\{m\theta\}=m\theta-\lfloor m\theta\rfloor\) for some integer \(m\), so the range is contained in \(\mathbb Z+\theta\mathbb Z\). The projections 1 and \(f\) have traces 1 and \(\theta\); their classes give the reverse containment. This proves (4.7), for differences of projections as well as projections.

The equivariant inclusion \(C(\mathbb T)\to D\) and the implementing unitary \(V\) of \(C\) form a covariant representation with the same positive function action as in (1.1). Universality gives \(\eta\) with \(\eta(u)=z\in D\) and \(\eta(v)=V\). It is injective. One may verify this directly with the gauge averages: \(E_D\eta=\eta E_{\mathbb T}\) on dense Laurent polynomials and hence everywhere, and \(\eta\) is injective on the coefficient algebra. If \(\eta(x)=0\), these identities force \(E_{\mathbb T}(x^*x)=0\), and faithfulness of the source average gives \(x=0\). The required faithful gauge averages and their coefficient ranges are Lesson 19, §1, including its proof preceding Proposition 1.1. No simplicity assertion about \(D\) is required.

That proposition makes \(\widehat\mu=\mu E_D\) a tracial state on \(C\). The coefficient trace restricts to Haar integration on the circle and the expectation identity shows \(\widehat\mu\eta=\tau\). Apply Lesson 18, Corollary 3.5, with its actual Toeplitz coefficient inclusion \(i:D\to C\). The relevant exact segment is
\[
\begin{gathered}
K_0(D)\xrightarrow{i_*}K_0(C)\\
\longrightarrow K_1(D)=0.
\end{gathered}
\tag{4.10}
\]
Thus \(i_*\) is onto. Naturality of the bounded trace pairing, Lesson 13, Theorem 1.1, gives
\(\widehat\mu_*i_*=\mu_*\), and hence
\(\widehat\mu_*(K_0(C))=\mu_*(K_0(D))\). Naturality again, now for \(\eta\), proves the claimed containment of the trace range of \(A_\theta\). This argument uses only surjectivity of a specified coefficient K-map; no sign choice for a PV boundary enters it.

Finally \([1]\) and the independently verified projection \([e_\theta]\) of Proposition 4.1 pair to 1 and \(\theta\). Their integer linear combinations lie in \(K_0(A_\theta)\), so the containment is equality. Combined with the abstract rank-two group calculation of Theorem 2.1, the elementary rank argument of Theorem 3.1 also recovers injectivity of the trace map. Proposition 4.1's projection and trace computation do not use Theorem 3.1; its subsequent basis conclusion does. Thus the alternative calculation introduces no dependency cycle. \(\square\)

This enlargement is a commutative AF coefficient algebra followed by an integer crossed product. It does not embed \(A_\theta\) into an AF algebra, and it proves no AF classification theorem. Its use of interval indicators concerns the ambient coefficient algebra; the original rotation algebra retains its continuous circle coefficients.

[Cuntz 1981 II] Joachim Cuntz, *K-theory for certain C*-algebras. II*, Journal of Operator Theory 5 (1981), 101–108, §2.5, p.107. [Freely readable original paper](https://www.theta.ro/jot/archive/1981-005-001/1981-005-001-009.pdf). The interval-enlargement method is credited to this paper. The proof above is independently written and supplies the steps abbreviated there as \(K_1(D)=0\) and the immediate coefficient trace-range calculation.

## 5. Positive classes and cancellation

**Theorem 5.1 (order).** Under (3.3),

\[
K_0(A_\theta)^+=
(\mathbb Z+\theta\mathbb Z)\cap[0,\infty).
\tag{5.1}
\]

The unit corresponds to \(1\). The traces of projections in \(A_\theta\) itself are exactly \((\mathbb Z+\theta\mathbb Z)\cap[0,1]\).

*Proof.* A projection in a matrix algebra has nonnegative trace, and faithfulness makes that trace strictly positive unless the projection is zero.

Conversely let \(r=m+n\theta>0\). If \(n=0\), use a diagonal matrix of \(m\) units. If \(n\ne0\), put \(\nu=\{n\theta\}\in(0,1)\). The unitaries \(u^n,v\) satisfy the relation for parameter \(\nu\). Proposition 1.1 gives a unital map \(A_\nu\to A_\theta\); its source is simple, so it is injective. The restricted normalized trace is the unique trace of \(A_\nu\). Therefore the image \(p\) of its projection \(e_\nu\) has trace \(\nu\). Write \(r=k+\nu\), where \(k=\lfloor r\rfloor\geq0\). The projection with diagonal blocks \(k\) units and \(p\) has trace \(r\). By injectivity of \(\tau_*\), its class is the class corresponding to \(r\). Zero is realized by the zero projection. This proves (5.1).

If \(0<r<1\), this construction has \(k=0\), so \(p\) belongs to \(A_\theta\) itself. The endpoints are realized by zero and one. Conversely any projection \(p\) in the unital algebra satisfies \(0\leq p\leq1\), hence \(0\leq\tau(p)\leq1\). \(\square\)

**Corollary 5.1a (short support and a fixed matrix size).** Let \(\theta\) be irrational. Every \(r\in(\mathbb Z+\theta\mathbb Z)\cap[0,1]\) is the trace of a smooth projection with only the implementing powers \(v^{-1},1,v\). More generally, for every integer \(N\geq1\),

\[
\begin{gathered}
\{(\tau\otimes\operatorname{Tr}_N)(p):
\\ p=p^*=p^2\in M_N(A_\theta)\}
\\ =(\mathbb Z+\theta\mathbb Z)\cap[0,N].
\end{gathered}
\tag{5.1a}
\]

Here \(\operatorname{Tr}_N\) is the unnormalized matrix trace.

*Proof.* The endpoints \(r=0,1\) are given by the zero and unit projections. If \(0<r<1\), write \(r=a+b\theta\) with integers \(a,b\). Then \(b\ne0\), and \(r=\{b\theta\}\). The unital homomorphism

\[
\begin{gathered}
\phi_b:A_r\longrightarrow A_\theta,
\\ \phi_b(u_r)=u^b,\quad \phi_b(v_r)=v.
\end{gathered}
\tag{5.1b}
\]

exists by Proposition 1.1 because
\(vu^b=e^{2\pi i b\theta}u^bv=e^{2\pi ir}u^bv\).
The pullback \(\tau\circ\phi_b\) is the unique normalized trace of \(A_r\), by Proposition 1.2. Thus Proposition 4.1 gives the projection

\[
\begin{gathered}
p_r= g_r(u^b)v^*+f_r(u^b)
\\ {}+vg_r(u^b),
\\ \tau(p_r)=r.
\end{gathered}
\tag{5.1c}
\]

Its functions are precisely the smooth functions of (4.3), with parameter \(r\). The map \(t\mapsto bt\) preserves smoothness of these functions, and \(u^b,v\) are smooth for the gauge action. Moving the last coefficient to the left by covariance rewrites \(vg_r(u^b)\) as a coefficient function times \(v\). Consequently its implementing support is contained in \(\{-1,0,1\}\), for every positive or negative \(b\).

Now let \(r\in(\mathbb Z+\theta\mathbb Z)\cap[0,N]\). If \(r\) is an integer, take \(r\) unit diagonal entries and \(N-r\) zero entries. Otherwise write \(r=k+s\), where \(k=\lfloor r\rfloor\) and \(0<s<1\). We have \(k\leq N-1\), and the diagonal projection consisting of \(k\) units, \(p_s\), and \(N-k-1\) zeros has unnormalized trace \(r\). Conversely, every such projection has its trace in \(\mathbb Z+\theta\mathbb Z\) by Theorem 3.1, and positivity gives \(0\leq(\tau\otimes\operatorname{Tr}_N)(p)\leq N\). This proves both inclusions. \(\square\)

This is the implementing-support refinement in Rieffel's Theorem 1.1 [1981, pp. 418–419]. It makes explicit a feature of the construction already used in Theorem 5.1: the coefficient power can grow with the requested dimension, while the implementing support stays in three degrees.

We now prove the stronger conclusion about individual modules. The mechanism is Rieffel's: combine a finite stable-rank bound with full equivalence modules of arbitrarily small dimension. We include the approximation and cancellation arguments themselves.

**Theorem 5.2 (Rieffel's cancellation theorem).** For irrational \(\theta\), finite projective right \(A_\theta\)-modules satisfy cancellation: if \(P\oplus Q\cong P'\oplus Q\), then \(P\cong P'\). Consequently trace dimension completely determines their isomorphism class. Projective submodules of \(A_\theta^N\) have exactly the dimensions in \((\mathbb Z+\theta\mathbb Z)\cap[0,N]\).

The proof uses the next three lemmas. They supply, respectively, the finite approximation bound, the actual removal of a summand, and the small modules with the needed endomorphism algebras.

**Lemma 5.3 (a finite stable-rank bound).** For every real \(\nu\), the pairs \((b_1,b_2)\) in \(A_\nu^2\) for which \(b_1^*b_1+b_2^*b_2\) is invertible are dense. In the usual notation, \(\operatorname{tsr}(A_\nu)\leq2\).

*Proof.* First, invertible functions are dense in \(C(\mathbb T)\). Uniformly approximate a continuous complex-valued function by a polygonal function on a subdivision of the circle. Its image is a finite union of line segments. A complex number of arbitrarily small absolute value can be chosen outside that union; subtracting it gives a nowhere-zero function, still arbitrarily close to the original one.

Write \(B=C(\mathbb T)\rtimes_{\alpha_\nu}\mathbb Z=A_\nu\), and denote its implementing unitary by \(w\). The algebra \(L\) of finite sums \(\sum_k a_kw^k\), \(a_k\in C(\mathbb T)\), is dense in \(B\). Its coefficients are unique: applying the faithful expectation to \(pw^{-k}\) recovers \(a_k\). For a nonzero polynomial let its length be its largest exponent minus its smallest exponent plus one; give zero length zero. Multiplication on the left by \(w^j\) translates the exponents and applies \(\alpha_\nu^j\) to the coefficients, so preserves length.

Let \(U\) be any nonempty open subset of \(B^2\). Consider all pairs \(ED\), where \(D\in U\cap L^2\) and \(E\) is a product of elementary invertible two-by-two matrices over \(L\). Choose one minimizing the sum of the two lengths. Such a minimum exists among nonnegative integers. Write this chosen pair as \((p,q)\). A sufficiently small polynomial perturbation of it remains in \(EU\), so its inverse image under the fixed \(E\) remains in \(U\cap L^2\).

Suppose both polynomials are nonzero. By the elementary signed interchange of two coordinates, arrange that \(p\)'s length is at most \(q\)'s. Multiply \(p\) by a power \(w^j\) which aligns its highest exponent with that of \(q\). Its lowest exponent is then no smaller than \(q\)'s. Perturb only the highest coefficient of \(p\), as little as necessary, so that the highest coefficient \(a\) of \(w^jp\) is invertible in \(C(\mathbb T)\). The density just proved permits this; the automorphism on coefficients preserves norms and invertibility. Let \(b\) be \(q\)'s highest coefficient. The elementary row operation

\[
q\longmapsto q-ba^{-1}w^jp
\tag{5.2}
\]

deletes the highest exponent of \(q\), and introduces no exponent below its original lowest exponent. Thus its length decreases, while \(p\)'s length stays the same. This contradicts the chosen minimum, with the small perturbation pulled back through \(E\). Hence the minimizing pair has a zero coordinate.

Replace that zero coordinate by \(\varepsilon1\), with \(\varepsilon>0\) small enough that the pair stays in \(EU\). It now generates the unit as a left ideal. Pulling it back through \(E^{-1}\) gives a left-generating pair in \(U\). For completeness, a pair \((c_1,c_2)\) is left-generating exactly when \(S=c_1^*c_1+c_2^*c_2\) is invertible. In one direction \(S^{-1}c_j^*\) are left coefficients summing to the unit. In the other, a left inverse row \(d\) for the column \(c\) gives
\(1=(dc)^*(dc)\leq\|d\|^2c^*c\), so \(S\) is bounded below. Invertible changes of rows preserve left generation. This proves the asserted density. \(\square\)

This is the Laurent-polynomial length argument of Rieffel's stable-rank theorem, specialized to the circle coefficients. Sudo's proof of Theorem 2.2, pp. 501–503, is a comparison source for the length reduction; here the implementing operator is unitary, so shifts preserve both endpoints exactly. We use neither a semigroup variant nor density of invertibles in the rotation algebra itself.

**Lemma 5.4 (removing a full-module summand).** Let \(Y,Z\) be finite projective right modules over a unital C*-algebra \(A\), and put \(D=\operatorname{End}_A(Y)\). Suppose left-generating pairs are dense in \(D^2\). For \(N\geq3\), every split injection \(x:Y\to Z\oplus Y^N\) can be carried by a module automorphism of its target to the standard inclusion into its last copy of \(Y\). Consequently, if

\[
P\oplus Y\cong Z\oplus Y^N,
\tag{5.3}
\]

then \(P\cong Z\oplus Y^{N-1}\).

*Proof.* All module maps between finite projective Hilbert modules are bounded and adjointable: represent them as matrix corners over \(A\). Write
\(x=(z,a_1,\ldots,a_N)\), where \(z:Y\to Z\) and \(a_i\in D\). Let \(\phi:Z\oplus Y^N\to Y\) be a splitting, so \(\phi x=1_Y\). Perturb the first \(N-1\) entries, leaving \(z,a_N\) fixed, to obtain entries \(a_i'\) with a left inverse row \((c_i)\):

\[
\sum_{i=1}^{N-1}c_i a_i'=1_Y.
\tag{5.4}
\]

It suffices to perturb the first two entries to a left-generating pair; set the other left coefficients zero. Choose the perturbation small enough that
\(T=1+(x'-x)\phi\) is invertible by its Neumann series. Then \(Tx=x'\), so this perturbation is realized by an actual module automorphism.

Now apply the following shears to the target, in order. Subtract \(z\sum c_i y_i\) from its \(Z\) coordinate; subtract \(a_N\sum c_i y_i\) from its last \(Y\) coordinate. On \(x'\), these make both coordinates zero by (5.4), leaving the first \(N-1\) coordinates unchanged. Add \(\sum c_i y_i\) to the last coordinate; it becomes identity on the image of \(Y\). Finally subtract \(a_i' y_N\) from each earlier \(Y\) coordinate; they become zero. Each operation is an invertible triangular module map, with inverse obtained by reversing the sign, since its source coordinates are not changed by that operation. Their composite sends \(x\) to the standard last inclusion.

For (5.3), apply this to the image of its source summand \(Y\). The isomorphism followed by the target automorphism maps that summand exactly onto the last target summand. Passing to quotient modules by these two summands gives the asserted isomorphism. This removes an actual summand, rather than only a K-class. \(\square\)

**Lemma 5.5 (small equivalence modules).** For irrational \(\theta\) and every \(\varepsilon>0\), there is a full finite projective right \(A_\theta\)-module \(Y\) with trace dimension \(0<\delta<\varepsilon\), such that

\[
\begin{gathered}
\operatorname{End}_{A_\theta}(Y)\cong A_\nu\\
\text{for an irrational real }\nu.
\end{gathered}
\tag{5.5}
\]

*Proof.* We use the exact written [Hilbert C*-modules Lesson 15, *Morita equivalence of noncommutative tori*](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-equivalence-of-noncommutative-tori.html#3-compatibility-and-completion), Theorems 3.2 and 6.1 and the trace normalization (4.4). Its Schwartz-module proof checks both commuting actions, coefficient positivity through the finite frame, the Poisson compatibility identity, the entire compact left algebra and fullness. It constructs an \(A_{1/t}\)–\(A_t\) equivalence for positive irrational \(t\), of right dimension \(t\). Its sign isomorphisms give dimension \(|t|\) for negative \(t\). Integer shift and negation are isomorphism modules of dimension one. Its Euclidean reduction and tensor transitivity supply the equivalence module for every word in these three transformations.

We spell out the scale for the word we need. For a generator matrix \(M_j=\begin{pmatrix}a_j&b_j\\c_j&d_j\end{pmatrix}\) and successive parameter \(t_{j-1}\), the right trace multiplier is \(|c_jt_{j-1}+d_j|\): it is one for shifts and negation, and \(|t_{j-1}|\) for inversion. The trace transport theorem in that course's [Lesson 14, Proposition 7.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html#7-examples-units-bundles-and-traces), makes these multipliers multiply under tensoring, in the successive domain and codomain order. The identity
\(M_j(t_{j-1},1)^T=(c_jt_{j-1}+d_j)(t_j,1)^T\)
shows that their product for the composite matrix \(M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) is \(|c\theta+d|\). Thus its constructed \(A_{M\theta}\)–\(A_\theta\) module has precisely that right dimension. Every intermediate parameter is irrational and every denominator is nonzero, as proved in that provider.

Pigeonhole approximation gives relatively prime integers \(c,d\) with \(0<|c\theta+d|<\varepsilon\). Indeed, among the \(K+1\) fractional parts \(j\theta\), \(0\leq j\leq K\), two have distance at most \(1/K\). Their difference gives \(q\geq1,p\in\mathbb Z\) with \(0<|q\theta-p|\leq1/K\). Divide both integers by their gcd and take \(K>1/\varepsilon\). Bezout's identity completes this primitive pair \((c,d)\) to the bottom row of a unimodular integer matrix \(M\). Use its constructed equivalence module as \(Y\), with \(\nu=M\theta\) and \(\delta=|c\theta+d|\).

An imprimitivity module between unital algebras is finite projective: its left unit is the compact identity, and the [finite-frame criterion](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/finite-projective-modules-frames-and-k0.html#2-compact-identity-and-algebraic-finiteness) proves this conclusion. Its adjointable endomorphism algebra equals its compact algebra, identified with \(A_\nu\). Both fullness and (5.5) are therefore actual module properties supplied by the construction; they have not been inferred from equal K-groups or a classification of projective modules. \(\square\)

The statement-level dependency here is acyclic. The torus provider uses only this lesson's already proved ordered K-group, trace and unit, Theorems 2.1, 3.1 and 5.1. It does not use Theorem 5.2 or this lesson's Morita-context paragraph to construct the equivalences.

*Proof of Theorem 5.2.* It is enough to show that any two projective modules \(P,P'\) with equal K-class are isomorphic. Their common trace dimension \(r\) is nonnegative; if it is zero, faithfulness of the matrix trace makes both modules zero. Suppose \(r>0\). Choose \(Y\) as in Lemma 5.5 with \(3\delta<r\). The positive-cone proof in Theorem 5.1 supplies a projective module \(Z\) whose K-class has trace \(r-3\delta\). Trace injectivity then gives

\[
[P]=[P']=[Z]+3[Y].
\tag{5.6}
\]

No cancellation has been used to obtain this equality.

We next justify changing a free stabilizer to copies of \(Y\). Fullness gives finitely many \(\xi_i,\eta_i\in Y\) with \(\sum_i\langle\xi_i,\eta_i\rangle=1_A\). To obtain the exact equality, first choose a finite sum within distance less than one from the unit, and multiply its second vectors on the right by the inverse of that sum. Thus
\(a\mapsto(\eta_i a)_i\) is a split injection \(A\to Y^l\), with left inverse \((y_i)\mapsto\sum_i\langle\xi_i,y_i\rangle\). Its complement is finite projective: its splitting defines an idempotent on a finite projective module, whose range is a direct summand. Consequently \(A^m\) is a direct summand of \(Y^k\) for some \(k\), for every finite \(m\).

Equality (5.6) means that \(P\) and \(Z\oplus Y^3\) become isomorphic after adding a common finite projective module \(W\). Choose a complement for \(W\) in \(A^m\); adding it gives
\(P\oplus A^m\cong Z\oplus Y^3\oplus A^m\).
Choose a complement for \(A^m\) in \(Y^k\) as just proved and add it to this isomorphism. We obtain

\[
P\oplus Y^k\cong Z\oplus Y^{k+3}.
\tag{5.7}
\]

By (5.5) and Lemma 5.3, left-generating pairs are dense in \(\operatorname{End}(Y)^2\). Apply Lemma 5.4 to the last source copy of \(Y\) in (5.7). It removes one copy on both sides; repeat until all \(k\) stabilizing copies have been removed. At every step the target has at least four copies, so the hypothesis \(N\geq3\) always holds. This proves \(P\cong Z\oplus Y^3\). The same reasoning gives \(P'\cong Z\oplus Y^3\), hence \(P\cong P'\). In particular a common summand in the theorem's hypothesis cancels.

Finally equality of trace dimensions gives equality in \(K_0\) by Theorem 3.1, so the result classifies the individual projective modules by dimension. Every value in \((\mathbb Z+\theta\mathbb Z)\cap[0,N]\) is realized by the integer units and fractional projection of Theorem 5.1 in an \(N\)-by-\(N\) matrix; the converse follows from \(0\leq p\leq1_N\). Exercise 20.5 gives equivalence in that fixed matrix algebra. \(\square\)

The cancellation theorem is due to Rieffel (1983). His 1988 Section 7 explains the small-full-module and finite-rank mechanism in the general torus setting. The present proof writes out the two-generator approximation and all summand removals; it does not import Warfield's cancellation theorem or presuppose stable rank one.

## 6. Isomorphism classification and examples

**Theorem 6.1.** If \(\theta,\theta'\) are irrational, then

\[
\begin{gathered}
A_\theta\cong A_{\theta'}\\
\Longleftrightarrow\quad\theta'-\theta\in\mathbb Z\\
\text{or}\quad\theta'+\theta\in\mathbb Z.
\end{gathered}
\tag{6.1}
\]

*Proof.* Any C*-algebra isomorphism between these unital algebras preserves the unit. Uniqueness of the normalized trace implies that it preserves trace values on matrix projections and differences. Thus it gives equality of the actual subgroups
\(\mathbb Z+\theta\mathbb Z=\mathbb Z+\theta'\mathbb Z\) inside \(\mathbb R\). Write, with integers \(a,b,c,d\),

\[
\begin{gathered}
\theta'=a+b\theta,\\
\theta=c+d\theta'.
\end{gathered}
\tag{6.2}
\]

Substitution gives \((1-db)\theta=c+da\). Irrationality forces \(db=1\) and \(c+da=0\), hence \(b=d=1\) or \(b=d=-1\). This proves the necessity. Conversely the explicit isomorphisms of (1.3) prove sufficiency, with inverse maps already checked. \(\square\)

**Theorem 6.1a (matrix size and angle).** If \(\theta,\theta'\) are irrational and \(m,n\geq1\) are integers, then

\[
\begin{gathered}
M_m(A_\theta)\cong M_n(A_{\theta'})
\\ \Longleftrightarrow\quad m=n\ \text{ and }
\\ \theta'\equiv\theta\text{ or }-\theta\pmod{\mathbb Z}.
\end{gathered}
\tag{6.2a}
\]

*Proof.* First identify the tracial state on the matrix algebra. If \(\rho\) is a tracial state on \(M_m(A_\theta)\), matrix units show that all \(\rho(e_{ii}\otimes1)\) are equal, so each is \(1/m\). The functional \(a\mapsto m\rho(e_{11}\otimes a)\) is a tracial state on \(A_\theta\); it is \(\tau\) by Proposition 1.2. Cyclicity gives
\(\rho(e_{ii}\otimes a)=\rho(e_{11}\otimes a)=\tau(a)/m\).
For \(i\ne j\),

\[
\begin{gathered}
\rho(e_{ij}\otimes a)
\\ =\rho\bigl((e_{ii}\otimes1)(e_{ij}\otimes a)\bigr)
\\ =\rho\bigl((e_{ij}\otimes a)(e_{ii}\otimes1)\bigr)=0.
\end{gathered}
\tag{6.2b}
\]

Therefore the unique tracial state is
\(\tau^{(m)}=(\tau\otimes\operatorname{Tr}_m)/m\).
Corollary 5.1a gives its projection range as

\[
\begin{gathered}
R_m(\theta)
\\ =\left(\frac1m(\mathbb Z+\theta\mathbb Z)\right)\cap[0,1].
\end{gathered}
\tag{6.2c}
\]

Irrationality implies that \((a+b\theta)/m\) can be rational only when \(b=0\). Hence

\[
\begin{gathered}
R_m(\theta)\cap\mathbb Q
\\ =\{0,1/m,2/m,\ldots,1\}.
\end{gathered}
\tag{6.2d}
\]

An isomorphism preserves the identity and pulls the unique normalized trace back to the unique normalized trace. It therefore gives \(R_m(\theta)=R_n(\theta')\). Comparing their smallest positive rational elements yields \(m=n\).

The additive group generated by \(R_m(\theta)\) is exactly
\(m^{-1}(\mathbb Z+\theta\mathbb Z)\): the range contains \(1/m\) and \(\{\theta\}/m\), which generate this group, and is contained in it. Thus equality of ranges, now with \(m=n\), gives
\(\mathbb Z+\theta\mathbb Z=\mathbb Z+\theta'\mathbb Z\).
The integer calculation in the proof of Theorem 6.1 then gives
\(\theta'\equiv\pm\theta\pmod{\mathbb Z}\).
Conversely, the explicit shift and sign isomorphisms (1.3), applied to every matrix entry, give the required isomorphism when \(m=n\). \(\square\)

Rieffel [1981, Proposition 1.3 and Theorem 3, pp. 416 and 420] proves the same rigidity with both angles reduced to \([0,1/2]\). The division by matrix size here concerns the normalized state on the entire matrix algebra; the K-theory trace extension used elsewhere in this lesson remains unnormalized. Matrix stability identifies the abstract K-groups, while the normalized projection range recovers the matrix size.

Isomorphism here preserves the normalized unit. Strong Morita equivalence permits a different scale: its full irrational-parameter classification is the fractional linear action of \(GL_2(\mathbb Z)\), proved in [Hilbert C*-modules Lesson 15, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-equivalence-of-noncommutative-tori.html#6-sufficiency-signs-and-the-groupoid-picture), using the explicit Schwartz equivalence and ordered K-group. Rosenberg's Theorem 4.2 retains its historical source credit. This distinction corrects the \(SL_2\)-only formulation in [Blackadar 2006, II.10.4.12(i)]; parameter negation is already an isomorphism. The statement-level prerequisites of that programme proof are the ordered groups proved here before cancellation.

**Example 6.2 (golden ratio).** Let \(\theta=(\sqrt5-1)/2\). Then \(K_1\) has basis \([u],[v]\); \(K_0\) has basis \([1],[e_\theta]\), with order
\(m[1]+n[e_\theta]>0\) exactly when \(m+n\theta>0\). There are projections of trace \(\theta\), \(1-\theta\), and \(2\theta-1\), the last by Exercise 20.4. The algebras for \(\theta\) and \(1-\theta\) are isomorphic.

**Example 6.3 (rational angles).** If \(\theta=p/q\) in lowest terms, the two groups in (2.2) remain \(\mathbb Z^2\), and the Haar trace range is \(q^{-1}\mathbb Z\). Its kernel on \(K_0\) has rank one, so it is not a classification of stable classes. The algebra is not simple: restriction to any finite rotation orbit gives a nonzero quotient with a nonzero coefficient function in its kernel, as proved in KT-CP-03, Exercise 3. For \(\theta=0\), the universal commuting pair gives \(C(\mathbb T^2)\). We have not used a rational-angle bundle description to infer an irrational-angle result. The clock-and-shift matrices below provide a different, quantitative comparison between rational relations and commuting matrices.

### Nearly commuting matrices with a persistent obstruction

The rational relations in Example 6.3 admit concrete finite matrices. They also explain why a small commutator is not enough to approximate a pair by a commuting pair. This is Voiculescu's clock-and-shift example, recalled in [Willett 2019, §3]. We give a finite-dimensional logarithm proof with an explicit distance bound.

For unitary matrices \(U,V\in M_n(\mathbb C)\), assume
\(\varepsilon=\|UV-VU\|<2\). The unitary commutator \(C=VUV^*U^*\) satisfies \(\|C-1\|=\varepsilon\), so \(-1\) is outside its spectrum. Its principal logarithm, with eigenvalue arguments in \((-\pi,\pi)\), defines

\[
\nu(U,V)=\frac{1}{2\pi i}\operatorname{Tr}\log(VUV^*U^*).
\tag{6.3}
\]

The trace is unnormalized. This integer is the logarithmic obstruction used below; identifying it with other Bott-index representatives is not needed for the proof.

**Lemma 6.4.** The number \(\nu(U,V)\) is an integer, is constant along continuous paths of pairs whose commutator norm is less than two, and is zero for a commuting pair.

*Proof.* Diagonalize \(C\), with eigenvalues \(e^{i\phi_j}\) and \(-\pi<\phi_j<\pi\). Since \(\det C=1\), \(\exp(i\sum_j\phi_j)=1\), so \(\sum_j\phi_j\) is an integer multiple of \(2\pi\). This proves integrality. Along a path avoiding \(-1\), the logarithm depends continuously on \(C\): locally choose a common contour and use holomorphic functional calculus for the principal branch. The trace is therefore a continuous integer-valued function, and hence is constant. A commuting pair has \(C=1\) and logarithm zero. \(\square\)

**Proposition 6.5 (a quantitative separation).** If \(\nu(U,V)\ne0\), every commuting unitary pair \(U',V'\) of the same size satisfies

\[
\begin{gathered}
\max\{\|U-U'\|,\|V-V'\|\}\\
\geq\frac{2-\varepsilon}{4}.
\end{gathered}
\tag{6.4}
\]

*Proof.* Suppose the maximum \(\delta\) is smaller than the right side. In particular \(\delta<2\). The principal logarithms of \(U^*U'\) and \(V^*V'\) exist and give unitary paths
\(U_t=U\exp(t\log(U^*U'))\) and
\(V_t=V\exp(t\log(V^*V'))\).
For an eigenvalue \(e^{i\phi}\), \(|\phi|<\pi\), the quantity \(|e^{it\phi}-1|=2\sin(t|\phi|/2)\) is at most \(|e^{i\phi}-1|\). Thus both paths stay within \(\delta\) of their initial matrices. Product differences give

\[
\begin{aligned}
\|U_tV_t-V_tU_t\|
&\leq\varepsilon+2\|U_t-U\|\\
&\quad+2\|V_t-V\|\\
&\leq\varepsilon+4\delta<2.
\end{aligned}
\tag{6.5}
\]

Lemma 6.4 makes \(\nu\) constant along this path, but its terminal pair commutes and has \(\nu=0\). This contradiction proves (6.4). \(\square\)

For \(n\geq3\), set \(\omega=e^{2\pi i/n}\) and, on the cyclically indexed basis \(e_0,\ldots,e_{n-1}\), put

\[
U_ne_j=\omega^j e_j,
\qquad V_ne_j=e_{j+1}.
\tag{6.6}
\]

Then \(U_nV_n=\omega V_nU_n\), while
\(V_nU_nV_n^*U_n^*=\omega^{-1}1\). Let \(d_n\) be the infimum of \(\max\{\|U_n-U'\|,\|V_n-V'\|\}\) over all commuting unitary pairs of size \(n\). Consequently

\[
\begin{aligned}
\varepsilon_n&=2\sin(\pi/n)\longrightarrow0,\\
\nu(U_n,V_n)&=-1,\\
d_n&\geq\frac{1-\sin(\pi/n)}{2}.
\end{aligned}
\tag{6.7}
\]

The logarithm is \((-2\pi i/n)1\), which gives the exact sign in (6.7); the case \(n=2\) lies at the excluded branch point. In the convention of §1, the assignments \(u\mapsto U_n,v\mapsto V_n\) represent \(A_{-1/n}\); interchanging the assignments represents \(A_{1/n}\). Although their commutators tend to zero, the distance bound tends to \(1/2\). Thus their small-angle relations cannot be made commuting by perturbations tending to zero. This does not identify a rational matrix quotient with the whole rotation algebra, and does not contradict the parameter-independent K-groups computed in §2.

## 7. The smooth algebra

The action \(\beta_{s,t}(u)=e^{2\pi is}u\), \(\beta_{s,t}(v)=e^{2\pi it}v\) defines the smooth subalgebra

\[
\begin{gathered}
A_\theta^\infty=\{a(c):c\in\mathcal S(\mathbb Z^2)\},\\
a(c)=\sum_{m,n\in\mathbb Z}c_{m,n}u^m v^n.
\end{gathered}
\tag{7.1}
\]

Here \(\mathcal S(\mathbb Z^2)\) denotes the rapidly decreasing sequences: \(\sup_{m,n}(1+|m|+|n|)^k|c_{m,n}|<\infty\) for every nonnegative integer \(k\).

Indeed, Fourier projection for the torus action has range \(\mathbb C u^m v^n\), first on the dense polynomials and then by continuity on the whole algebra. Repeated integration by parts on a smooth orbit map bounds its coefficients with arbitrary polynomial weights. Conversely rapid decrease makes the series and every differentiated series absolutely convergent in norm, since all monomials are unitaries. Termwise differentiation proves smoothness. Product Fejér convolution of the continuous orbit map converges in norm, so the coefficients uniquely determine the element; no convergence assertion for ordinary Fourier partial sums is needed.

[Lesson 15, Theorem 4.1](KT-OPK-15.md#4-smooth-actions-and-regular-spectral-triples) proves density, completeness in the derivative seminorms, matrix holomorphic functional calculus and the resulting K-theory isomorphisms. Thus the projection of §4 is smooth and represents the same class in the smooth and completed algebras. Under (4.1), the geometry lesson's ordered second derivation differentiates \(v^*\) positively, hence differentiates \(v\) negatively. Its Chern-number convention is retained by that identification.

## 8. Exercises with solutions

**Exercise 20.1 (basic: parameter changes).** Give explicit inverse isomorphisms for \(A_\theta\cong A_{\theta+1}\cong A_{-\theta}\).

*Solution.* For the integer shift send each generator to the generator with the same name; the scalar in (1.2) is identical. The reverse map does the same. For negation, if the target generators are \(u',v'\), send \(u\mapsto u'\), \(v\mapsto v'^*\). The target relation implies \(v'^*u'=e^{2\pi i\theta}u'v'^*\). The reverse map also preserves the first generator and takes the adjoint of the second, so both compositions fix the generators. Universality proves the claims. \(\square\)

**Exercise 20.2 (intermediate: coefficient equations).** For real continuous \(f,g\), derive the exact conditions making (4.2) a projection and verify them for (4.3).

*Solution.* Use \(W=v^*\) and \(g_+(t)=g(t+\theta)\). The expression is automatically self-adjoint. The coefficients of \(W^0,W^1,W^2\) in its square are respectively
\(f^2+g^2+g_+^2\), \(g(f+f(t-\theta))\), and \(g(t)g(t-\theta)\). The negative coefficients are adjoints. Coefficient uniqueness from the faithful expectation makes (4.5) necessary and sufficient. The rising and falling intervals give the first identity, their complementary values give the second, and the disjoint translated supports give the third. It is essential to retain both translated square terms in the constant coefficient; the unshifted equation \(g^2=f-f^2\) alone is not the projection condition. \(\square\)

**Exercise 20.3 (intermediate: determinant sign).** Compute the relative determinant of \(z\) for \(\alpha_\theta\), and compare it with inverse pullback by the geometric rotation \(r_\theta(t)=t+\theta\).

*Solution.* For (1.1), \(z\alpha_\theta(z^*)=e^{-2\pi i\theta}\). Along \(w(s)=e^{-2\pi i s\theta}\), the logarithmic derivative is \(w'w^*=-2\pi i\theta\), so \(\Gamma_{\tau_0}(w)=-\theta\) and the determinant is \(-\theta+\mathbb Z\). For \(h\mapsto h\circ r_\theta^{-1}=\alpha_{-\theta}(h)\), the relative product is \(e^{2\pi i\theta}\), and the increasing exponential path gives \(+\theta+\mathbb Z\). Both generate the same subgroup of \(\mathbb R/\mathbb Z\) and hence the same trace range. \(\square\)

**Exercise 20.4 (advanced: a small projection).** For irrational \(1/2<\theta<1\), construct a projection in \(A_\theta\) of trace \(2\theta-1\). Explain the bounds on ordinary projection traces.

*Solution.* Set \(\nu=2\theta-1\in(0,1)\). Since \(v u^2=e^{2\pi i\nu}u^2v\), the universal map \(A_\nu\to A_\theta\) sends its generators to \(u^2,v\). It is injective because \(\nu\) is irrational and its source is simple. Apply the functions constructed for parameter \(\nu\) to get
\(p=g_\nu(u^2)v^*+f_\nu(u^2)+vg_\nu(u^2)\). Proposition 4.1 proves this is a projection. The pullback of \(\tau\) is the unique normalized trace on \(A_\nu\), so \(\tau(p)=\nu\). Every projection in \(A_\theta\) satisfies \(0\leq p\leq1\); positivity and normalization give its trace in \([0,1]\). In \(M_N(A_\theta)\) with the unnormalized matrix trace the bound is \([0,N]\). \(\square\)

**Exercise 20.5 (advanced: cancelling complements).** Using Theorem 5.2, prove that two projections \(p,q\in M_N(A_\theta)\) with the same trace are unitarily equivalent in that same matrix algebra.

*Solution.* Trace injectivity gives \([p]=[q]\) in \(K_0\). The definition of group completion supplies a common finite projective stabilizing module. Cancellation gives \(pA_\theta^N\cong qA_\theta^N\). An isomorphism is a rectangular corner operator; its polar normalization gives a partial isometry \(s\) with \(s^*s=p\), \(ss^*=q\). Apply the same argument to the complements, whose classes are \([1_N]-[p]\) and \([1_N]-[q]\), obtaining \(t^*t=1_N-p\), \(tt^*=1_N-q\). Their initial and final supports are orthogonal, so all cross terms vanish and \(w=s+t\) is unitary. Moreover \(wpw^*=q\). This conclusion uses cancellation, whereas Theorem 5.1's computation of the positive cone did not. \(\square\)

## Proof inputs and source comparison

We imported PV exactness and naturality from Lesson 18, the numerical determinant range theorem from Lesson 19, and the smooth-action density theorem from Lesson 15. The coefficient expectation and simplicity criterion are the precise KT-CP-03 results cited above; amenability of \(\mathbb Z\) is KT-CP-05. Theorem 5.2 now proves Rieffel's cancellation theorem in full, including the finite stable-rank reduction, small full equivalence modules, and every stabilizer removal. The Morita classification after Theorem 6.1 has the exact written Hilbert C*-modules Lesson 15 proof; its small-module construction is used in Lemma 5.5 with the trace direction specified there. Neither the unit-preserving isomorphism proof nor the ordered-group computation uses cancellation.

[Blackadar 1998, Exercise 10.11.6(a)–(e)] uses \(uv=e^{2\pi i\theta}vu\), while (1.2) uses the reverse order. Our determinant calculation and (4.1) account for that difference. The geometry lesson's supports and projection have been retained. [Emerson 2024, Exercise 6.6.4(a)] compresses the projection equations incorrectly: the constant coefficient needs the sum of the two shifted square terms in (4.5). Its short-support construction of a projection in the unital algebra requires an angle in \((0,1)\); larger positive trace dimensions require matrix projections. Corollary 11.5.14 gives the abstract groups; the irrational generator identifications are proved here rather than left as a verification. In [Rosenberg 2012], basic facts are §4.1, the smooth algebra is §4.2, and cancellation is Theorem 4.6 in §4.3. Connes's Chapter II, §2 explains quotient-space algebras through open covers and the infinite dihedral group; it is background, not a rotation-algebra trace computation.

Two rational-angle statements in Rosenberg's §4.1 also need care. For coprime \(p,q\), the group \(\mathbb Z+(p/q)\mathbb Z\) is \(q^{-1}\mathbb Z\), which need not equal \((p/q)\mathbb Z\). A line bundle's endomorphism algebra is commutative and therefore cannot describe \(A_{p/q}\) when \(q>1\); its matrix-bundle description requires higher-rank fibers. Neither erroneous formulation enters our proof.

## References

- **[Blackadar 1998]** Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Exercise 10.11.6(a)–(e) and its following remarks; §§10.2 and 10.10 for the prerequisite route. [Author's book](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Blackadar 2006]** Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, II.10.4.12(i). [Author's revised edition](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Rosenberg 2012]** Jonathan Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, 2012, pp. 93–129, §4, especially Theorems 4.1, 4.2 and 4.6. [Publisher's volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).
- **[Emerson 2024]** Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §6.6 and Corollary 11.5.14.
- **[Rieffel 1981]** Marc A. Rieffel, *C*-algebras associated with irrational rotations*, Pacific Journal of Mathematics 93 (1981), 415–429, Theorems 1.1–1.2 and Proposition 1.4. [Original paper](https://msp.org/pjm/1981/93-2/pjm-v93-n2-p12-s.pdf).
- **[Rieffel 1983]** Marc A. Rieffel proved the cancellation theorem for projective modules over the irrational rotation C*-algebras in 1983. Theorem 7.1 of Marc A. Rieffel, *Projective modules over higher-dimensional non-commutative tori*, Canadian Journal of Mathematics 40 (1988), 257–338, proves cancellation for every noncommutative torus with non-rational parameter, by an argument parallel to the two-generator proof. [Author's paper](https://math.berkeley.edu/~rieffel/papers/projective88.pdf). Theorem 5.2 proves the full cancellation statement reproduced in Rosenberg's Theorem 4.6, using the finite-rank mechanism of Rieffel 1988 and a length reduction as in Sudo 2005.
- **[Connes 1994]** Alain Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, §2, pp. 90–93. [Author's book](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

- **[Rieffel 1988]** Marc A. Rieffel, *Projective modules over higher-dimensional non-commutative tori*, Canadian Journal of Mathematics 40 (1988), 257–338, §3, Propositions 3.9–3.10, and §7, Theorems 7.1–7.5 and Lemma 7.6. [Author's paper](https://math.berkeley.edu/~rieffel/papers/projective88.pdf). The small-full-module mechanism is credited; Lemmas 5.3–5.4 supply the approximation and cancellation steps directly in the present two-generator case.
- **[Sudo 2005]** Takahiro Sudo, *Stable rank of the semigroup crossed products by natural numbers*, Scientiae Mathematicae Japonicae Online e-2005, 499–509, notation and Theorem 2.2, pp. 500–503. [Original journal paper](https://www.jams.jp/scm/contents/e-2005-6/2005-58.pdf). Comparison of Rieffel's elementary length-reduction argument; Lemma 5.3 uses only the unitary, integer-group case.
- **[Hilbert C*-modules Lesson 15]** *Morita equivalence of noncommutative tori*, GPT-6.1 Sol (OpenAI), Ultra, CC0, §§1–6.1, especially Theorem 3.2, (4.4), Theorems 5.2 and 6.1. [Complete written programme proof](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-equivalence-of-noncommutative-tori.html#3-compatibility-and-completion). Lemma 5.5 specifies its full required scope, the exact trace multiplier and the result-level dependency on the already proved ordered K-group.

- **[Willett 2019]** R. Willett, *Bott periodicity and almost commuting matrices*, author version dated 7 January 2019, §3, equation (1) and Theorem 3.1; published in *Contemporary Mathematics* 749 (2020), 379–388. [Freely available author version](https://math.hawaii.edu/~rufus/Bott.pdf#page=4). Voiculescu's example and Loring's Bott-theoretic explanation are credited there. The logarithmic invariant, its path proof and the explicit bound (6.4) are independently written here; no source expression is adapted.

[Rieffel1981, support and matrix rigidity] M. A. Rieffel, *C*-algebras associated with irrational rotations*, Pacific Journal of Mathematics93(2)(1981),415–429, complete mathematical body §§0–2, especially Theorem1.1pp418–419, Proposition1.3 and proof of Theorem3p420. [Freely readable original](https://msp.org/pjm/1981/93-2/pjm-v93-n2-p12-s.pdf). Corollary5.1a proves smooth three-degree support and each fixed matrix-size range before cancellation; Theorem6.1a proves normalized matrix trace uniqueness, rational-value detection of matrix size and full angle rigidity. The existing trace-range proof supplies containment, so the original externally cited AF embedding is not a new proof input.

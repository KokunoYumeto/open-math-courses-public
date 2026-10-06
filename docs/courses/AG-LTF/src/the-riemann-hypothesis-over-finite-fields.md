# The Riemann hypothesis over finite fields

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, with bounded internal checks of the geometric providers and their integration recorded separately. Independent human review is not claimed. Public domain (CC0).*

The smooth-proper reduction in §6 uses the complete Smooth projective alterations and Stable pointed-family extension proofs and gives its rational pullback-and-trace projector explicitly.

For a smooth projective variety over a finite field, Frobenius on degree-\(i\) cohomology has eigenvalues of complex absolute value \(q^{i/2}\), under every conjugate embedding. This lesson proves the higher-dimensional theorem from the pencil theory and the fundamental estimate developed in Lessons 9–10. Section 6 passes to the canonical theorem for every smooth proper variety using the smooth projective alteration constructed in the two proof lessons named above. Its pullback-and-trace splitting, finite-field descent, integrality and independence of \(\ell\) are proved explicitly here.

The remaining rationality issue is substantive: a vanishing quotient of fibre cohomology need not visibly have rational characteristic polynomials. We settle it by recovering the constant factors of fibre zeta functions. Chebotarev and a measure-zero argument prevent those factors from being hidden by systematic cancellation. We then prove the even-dimensional estimate with error \(1/2\), remove that error by tensor powers, and derive integrality, independence of \(\ell\), and point-count bounds.

## 1. The statement, inputs and reductions

Let \(X_0\) be smooth and projective over \(\mathbf F_q\), and let
\(X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q\). All cohomology has coefficients in \(\mathbf Q_\ell\), \(\ell\ne\operatorname{char}\mathbf F_q\), unless a finite coefficient-field extension is specified. Frobenius \(F\) is geometric, so its eigenvalue on \(\mathbf Q_\ell(-r)\) is \(q^r\).

**Theorem 1.1 (Deligne).** Every eigenvalue of \(F\) on \(H^i(X,\mathbf Q_\ell)\) is algebraic over \(\mathbf Q\). Every complex conjugate has absolute value \(q^{i/2}\).

This is *Weil I*, (1.7); the integer characteristic polynomials and independence of \(\ell\) in its stronger (1.6) are proved in §6. Finiteness, Künneth and the trace formula come from the preceding lessons. Smooth traces, duality and Gysin maps, §§1–2 and 8–13, constructs the higher-dimensional trace, smooth duality and the actual Gysin adjunctions. We prove the weak Lefschetz deduction below, using the written affine theorem at its exact proof home. The geometric existence and local/global pencil inputs are those of Lesson 9; their use is isolated in §§4–5. Hard Lefschetz is not an input.

Lesson 9 proves the geometric statements used here. Theorem 1.0 gives characteristic-sensitive pencil existence; Sections NC, Q and PL prove the higher-dimensional singular rank-one calculation and the Picard–Lefschetz normalization with actual support and trace maps; Section 4 proves tameness, compatible inertia conjugacy, the zero-cycle alternative and the invariant-space description; Sections 5–6 prove symplectic openness. Its general higher-dimensional restriction excludes characteristic two with even fibre dimension; degree zero is treated separately in every characteristic. Section 5 below needs only odd-dimensional fibres: in characteristic two their higher-dimensional polar form is nondegenerate, and the odd-dimensional local and tame conclusions of Lesson 9 apply. The deductions in §§4–5 retain both the nonzero-cycle and zero-cycle cases.

The independent curve prerequisite is Lesson 5, Theorem 5.3: its §§2.1–2.7 prove the surface Hodge inequality, and §5 applies it to Frobenius graphs on \(C\times C\). That argument proves rationality, the functional equation and the Riemann hypothesis for every smooth projective curve inside this course. We use it on the covering curves and their twists in §2.

### Affine vanishing and weak Lefschetz

The precise affine input is [*Cohomological dimension and the Künneth formula*, Theorem 5.1](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula). Its §§2–5 give the complete simultaneous dimension induction: limits and curve/field bounds, strict-local finite models, closed support approximation, and the two Leray spectral sequences for \(\mathbf A^d\subset\mathbf P^1\times\mathbf A^{d-1}\). The result is
\[
H^r(W,G)=0\quad(r>\dim W)
\tag{1.1}
\]
for **every torsion étale sheaf** \(G\) on an affine finite-type scheme \(W\) over an algebraically closed field. Neither smoothness of \(W\) nor local constancy of \(G\) is required. We consume its prime-to-characteristic constant-coefficient case; the all-torsion assertion does not extend Poincaré duality to characteristic-primary coefficients.

**Proposition 1.2 (weak Lefschetz, with its dual map).** Let \(X/k\) be smooth projective of pure dimension \(d\ge1\), with \(k\) algebraically closed, and let \(i:Y\hookrightarrow X\) be a smooth ample effective Cartier divisor. For any integer \(a\), restriction
\[
i^*:H^r(X,\mathbf Q_\ell(a))\longrightarrow
H^r(Y,\mathbf Q_\ell(a))
\tag{1.2}
\]
is an isomorphism for \(r<d-1\) and injective for \(r=d-1\). Its dual Gysin map
\[
i_*:H^{2d-2-r}(Y,\mathbf Q_\ell(-1))
\longrightarrow H^{2d-r}(X,\mathbf Q_\ell)
\tag{1.3}
\]
is an isomorphism in the first range and surjective at \(r=d-1\). All maps are Frobenius-equivariant when the pair is defined over a finite field.

**Proof.** Put \(U=X-Y\). This complement is affine. Indeed, choose a power \(L^{\otimes b}\) of the ample line bundle \(L=\mathcal O_X(Y)\) which is very ample. Include the nonzero section \(s^b\), whose vanishing support is \(Y\), in a basis of its global sections. The resulting embedding realizes \(U\) as the closed subscheme of the affine chart where that coordinate is nonzero. If a component is disjoint from \(Y\), ampleness would make a positive-dimensional projective component affine, which is impossible; dimension-zero components are excluded by pure dimension \(d\). Thus \(U\) is smooth of pure dimension \(d\).

Work first over \(\Lambda_b=\mathbf Z/\ell^b\mathbf Z\). The affine theorem gives \(H^{2d-t}(U,\Lambda_b(d-a))=0\) for \(t<d\). The finite-coefficient smooth duality theorem in the supporting lesson identifies its exact \(\Lambda_b\)-dual with \(H^t_c(U,\Lambda_b(a))\); hence
\[
H^t_c(U,\Lambda_b(a))=0\quad(t<d).
\tag{1.4}
\]
For these smooth schemes the finite-coefficient groups are finite. Their inverse systems therefore satisfy Mittag–Leffler: the descending images in each fixed finite group stabilize. The Milnor sequence for derived inverse limit consequently has zero \(\varprojlim^1\) term. Taking \(R\varprojlim_b\) in (1.4), then tensoring with \(\mathbf Q_\ell\), gives \(H^t_c(U,\mathbf Q_\ell(a))=0\) for \(t<d\). This also explains why an unexamined ordinary inverse limit of an exact sequence would be insufficient.

The closed-open triangle on proper \(X\) gives
\[
H^r_c(U,\mathbf Q_\ell(a))\longrightarrow H^r(X,\mathbf Q_\ell(a))
\xrightarrow{i^*}H^r(Y,\mathbf Q_\ell(a))
\longrightarrow H^{r+1}_c(U,\mathbf Q_\ell(a)).
\tag{1.5}
\]
Both outer terms vanish when \(r<d-1\); the first vanishes when \(r=d-1\). This proves the restriction assertions, including \(d=1\), where the asserted isomorphism range in nonnegative degrees is empty.

For \(a=0\), the transpose of restriction under the perfect pairings is the map from \(H^{2d-2-r}(Y,\mathbf Q_\ell(d-1))\) to \(H^{2d-r}(X,\mathbf Q_\ell(d))\). It is the Gysin counit, because the supporting lesson's projection formula and trace compatibility give
\(\int_Y i^*x\cup y=\int_Xx\cup i_*y\).
Cancelling the common twist \((d)\) gives exactly (1.3). The dual of an injective map of finite-dimensional spaces is surjective, and the dual of an isomorphism is an isomorphism. The constructions commute with field automorphisms, so the equivariance and the twisted assertions follow. \(\square\)

In particular, for a smooth \(n\)-dimensional pencil fibre and its smooth hyperplane section, the degree-\(n-1\) restriction is injective and
\(H^{n-1}(Y)(-1)\twoheadrightarrow H^{n+1}(X_u)\).
These are the two maps used in §5, with their precise Tate sign. We have obtained them before any weight theorem or hard Lefschetz theorem.

Here are three reductions we will use throughout.

- Replacing \(\mathbf F_q\) by \(\mathbf F_{q^r}\) replaces \(F\) by \(F^r\) and \(\alpha\) by \(\alpha^r\). If \(\alpha^r\) is algebraic, then \(\alpha\) is algebraic, since it satisfies \(T^r-\alpha^r=0\). Bounds for every conjugate of \(\alpha^r\) give the corresponding bounds for every conjugate of \(\alpha\) by taking \(r\)-th roots.
- After a finite extension, Frobenius preserves every geometric component. A smooth connected variety over an algebraically closed field is irreducible, since its regular irreducible components cannot meet. Thus disjoint unions and finite extension reduce to geometrically irreducible varieties of a fixed dimension.
- Duality identifies complementary operators by \(\alpha\mapsto q^d/\alpha\) between degrees \(i\) and \(2d-i\). It converts weight \(i\) into weight \(2d-i\), with algebraicity and all conjugates preserved.

We first prove the rationality needed for a pencil. The final purity argument is in §§5–6.

## 2. Chebotarev, including constant fields

Let \(U_0\) be a smooth geometrically connected curve over \(\mathbf F_q\), not necessarily proper, and let \(Y_0\to U_0\) be a connected finite étale Galois cover with group \(G\). Let its field of constants be \(\mathbf F_{q^e}\). The geometric subgroup \(H\) has index \(e\), with
\[
1\longrightarrow H\longrightarrow G\longrightarrow
\mathbf Z/e\mathbf Z\longrightarrow1.
\tag{2.1}
\]
Choose the quotient generator to be **geometric** constant-field Frobenius. Write \(G_d\) for the coset mapping to \(d\bmod e\). A degree-\(d\) geometric Frobenius class can only lie in \(G_d\).

For a conjugacy-invariant subset \(C\subset G\), let \(A_C(d)\) count degree-\(d\) closed points of \(U_0\) whose geometric Frobenius lies in \(C\).

**Theorem 2.1 (Chebotarev with an error bound).** There is a constant \(K\), depending only on the cover and its compactifications, such that
\[
\left|A_C(d)-
\frac{e\,|C\cap G_d|}{|G|}\frac{q^d}{d}\right|
\le K\frac{q^{d/2}}d
\quad(d\ge1).
\tag{2.2}
\]
In particular the Dirichlet density of these closed points is \(|C|/|G|\).

One permissible explicit constant is
\[
K=2g_Y+e+B_Y+(2+2g_U)\frac q{q-1},
\tag{2.3}
\]
where \(g_U\) is the genus of the smooth projective completion of \(U_0\), \(g_Y\) is the sum of the genera of the \(e\) geometric components of the smooth projective completion of \(Y_0\), and \(B_Y\) is the number of geometric boundary points of that completion.

**Proof.** We first count rational points over \(\mathbf F_{q^d}\), including those of smaller closed degree. To avoid an inverse hidden in a deck-action convention, make this part of the calculation with arithmetic Frobenius \(\Phi^d\) on geometric points. At the end replace each arithmetic conjugacy class by its inverse; the quotient in (2.1) was chosen with the inverse, geometric generator.

Fix a compatible arithmetic class represented by \(g\). The operator \(g^{-1}\Phi^d\) preserves each of the \(e\) geometric components of \(Y_0\). It is the Frobenius of a twist over \(\mathbf F_{q^d}\): twist the constant-field descent datum by the finite-order deck transformation \(g^{-1}\). This is effective finite Galois descent for a quasiprojective variety, or for its projective completion. Compatibility is exactly what makes each component descend over this field. Each resulting completed curve has the same geometric genus as the original component. The curve Riemann hypothesis therefore gives
\[
\left|\#\operatorname{Fix}(g^{-1}\Phi^d\mid Y)
-e q^d\right|
\le 2g_Yq^{d/2}+e+B_Y.
\tag{2.4}
\]
The \(e\) accounts for the constant terms in the projective curve counts; removing the boundary changes the count by at most \(B_Y\). In an incompatible class no component is preserved, so the count is zero.

Over \(u\in U_0(\mathbf F_{q^d})\), the geometric fibre is a \(G\)-torsor. If its arithmetic Frobenius is conjugate to \(g\), exactly \(|Z_G(g)|\) points in that fibre satisfy \(\Phi^d y=g y\); otherwise none do. Indeed changing a torsor point conjugates the element describing Frobenius, and the number giving a specified conjugate is its centralizer order. Thus (2.4), divided by \(|Z_G(g)|\), counts the rational base points with that class. Since \(1/|Z_G(g)|=|[g]|/|G|\), summing over compatible classes and then taking inverses gives
\[
R_C(d):=\#\{u\in U_0(\mathbf F_{q^d}):
\text{geometric Frobenius over }\mathbf F_{q^d}\text{ lies in }C\}
\]
with
\[
\left|R_C(d)-
\frac{e|C\cap G_d|}{|G|}q^d\right|
\le(2g_Y+e+B_Y)q^{d/2}.
\tag{2.5}
\]
We used \(|C|/|G|\le1\) to obtain a single constant for every \(C\).

Every degree-\(m\) point, \(m\mid d\), gives \(m\) rational points over \(\mathbf F_{q^d}\), with Frobenius the \((d/m)\)-th power of its degree-\(m\) Frobenius. Consequently
\[
R_C(d)=dA_C(d)+
\sum_{\substack{m\mid d\\m<d}}
m\,\#\{x:\deg x=m,\ F_x^{d/m}\in C\}.
\tag{2.6}
\]
Every proper divisor \(m\) is at most \(d/2\). The omitted sum is bounded by
\[
\sum_{1\le m\le d/2}\#U_0(\mathbf F_{q^m})
\le(2+2g_U)\sum_{1\le m\le d/2}q^m
\le(2+2g_U)\frac q{q-1}q^{d/2}.
\]
Here the curve count bound is \(q^m+1+2g_Uq^{m/2}\), and removing boundary points only decreases it. Combining with (2.5) and dividing by \(d\) proves (2.2)–(2.3).

For density, put \(z=q^{1-s}\), \(s>1\), and sum (2.2) against \(q^{-sd}\). The error sum stays bounded as \(s\downarrow1\). The sequence
\(a_d=e|C\cap G_d|/|G|\) has period \(e\) and mean \(|C|/|G|\). A periodic sequence of mean zero has bounded partial sums; summation by parts shows that its contribution to \(\sum a_dz^d/d\) stays bounded for \(0<z<1\). Thus
\[
\sum_{\substack{x\in|U_0|\\F_x\in C}}q^{-s\deg x}
=\frac{|C|}{|G|}\bigl[-\log(1-z)\bigr]+O(1).
\tag{2.7}
\]
The total closed-point sum is \(-\log(1-z)+O(1)\), by the curve count and the same proper-divisor estimate. Their ratio tends to \(|C|/|G|\), the asserted Dirichlet density. \(\square\)

When \(e>1\), a class can have no points in some degrees. Replacing the coefficient in (2.2) by \(|C|/|G|\) in every degree would be false. If the connected base curve has a larger constant field, take that as the base field; rescaling all degrees in the two sums leaves the density statement unchanged. Disconnected bases are handled component by component.

**Corollary 2.2.** In a compact image \(\Gamma\) of \(\pi_1(U_0)\), Frobenius conjugacy classes are dense. A closed conjugacy-invariant subset of Haar measure zero is hit by closed-point Frobenius with Dirichlet density zero.

**Proof.** Every finite quotient of \(\Gamma\) corresponds to a connected finite étale Galois cover. A nonempty conjugacy-stable open subset contains the inverse image of a nonempty union of classes in one such quotient; its density is positive by Theorem 2.1. This proves density of the union of Frobenius conjugacy classes.

For a closed invariant set \(Z\) of measure zero, choose normal open subgroups decreasing to the identity. The inverse images of the images of \(Z\) in their finite quotients are conjugacy-stable clopen neighbourhoods decreasing to \(Z\). Their normalized Haar measures tend to zero. Theorem 2.1 identifies their closed-point densities with those measures, so the upper density of the points hitting \(Z\) is at most every one of them, hence zero. \(\square\)

In particular, the points with degree \(1\bmod M\) have density \(1/M\): use the constant extension \(\mathbf F_{q^M}\). Such a set cannot be contained in a density-zero exceptional set. This elementary consequence will keep the reconstruction argument from assuming a good point in every degree.

## 3. Avoiding prescribed eigenvalues and recovering power families

### The measure-zero step

Let \(\mathcal V_0\) be a nonzero lisse sheaf with a nondegenerate alternating pairing into \(\mathbf Q_\ell(-n)\), and open geometric monodromy in its symplectic group. This is the vanishing quotient from Lesson 9, with odd \(n\). The following argument does not assume its local polynomials are rational.

Write \(\Gamma\) for the compact image of
\[
\pi_1(U_0)\longrightarrow\widehat{\mathbf Z}
\times\operatorname{GSp}(V),\qquad h\longmapsto(\deg h,\rho(h)),
\tag{3.1}
\]
using geometric Frobenius as the degree generator. Then
\(\mu(\rho(h))=q^{n\deg h}\), where \(\mu\) is the similitude multiplier. The degree projection is surjective. Its kernel is an open compact subgroup of \(\operatorname{Sp}(V)\). The degree-\(z\) fibre is a translate of that kernel inside the algebraic similitude fibre with multiplier \(q^{nz}\).

In fact \(\Gamma\) is open in the ambient group
\(\{(z,g):\mu(g)=q^{nz}\}\). Here is a direct topological proof. If it were not open, take elements \(h_i\notin\Gamma\) tending to the identity. Choose \(\gamma_i\in\Gamma\) with the same degree. Compactness gives a convergent subsequence \(\gamma_i\to\gamma\), with \(\gamma\) in the degree-zero kernel. Now \(h_i\gamma_i^{-1}\) lies in the ambient symplectic kernel and tends to \(\gamma^{-1}\). Openness of the geometric image in that kernel forces these elements eventually into \(\Gamma\), hence \(h_i\in\Gamma\), a contradiction. These groups are metrizable, so the sequence criterion for openness used here applies.

For any \(\ell\)-adic unit \(\delta\) in a finite extension of \(\mathbf Q_\ell\), the power \(\delta^z\) is defined continuously for \(z\in\widehat{\mathbf Z}\): exponentiation of integers extends into the compact closure of its cyclic unit subgroup. Consider
\[
Z_\delta=\{(z,g)\in\Gamma:\det(g-\delta^z)=0\}.
\tag{3.2}
\]
It is closed and conjugacy-invariant.

For fixed \(z\), the eigenvalue equation is a proper algebraic hypersurface in the similitude fibre. To check properness, in a symplectic basis choose a diagonal similitude with eigenvalues
\[
t_1,\ldots,t_r,\quad q^{nz}/t_1,\ldots,q^{nz}/t_r;
\]
each nonzero \(t_i\in\mathbf Q_\ell\) can avoid the finitely many values making one of these equal \(\delta^z\). Thus the equation is not identically zero. Its restriction to any nonempty analytic open ball in that fibre is also not identically zero, since the fibre is an irreducible translate of the symplectic group.

For completeness, a nonzero convergent \(\ell\)-adic analytic function on a ball has a zero set of measure zero. In one variable, after rescaling to the unit ball, let \(N\) be the largest index at which the coefficient has maximal absolute value; the coefficients tend to zero. Division by a root \(a\) in the ball gives coefficients
\[
b_j=\sum_{i\ge j+1}a_i a^{i-j-1},
\]
and lowers that largest maximal index by one. If \(N=0\), the constant term dominates and there is no root. Induction gives at most \(N\) distinct roots. This is the elementary Strassmann argument. In several variables, expand in the last variable. At least one coefficient is a nonzero analytic function of the other variables. By induction its zero set has measure zero; off that set the last-variable function has only finitely many roots. Fubini proves the claim. Analytic group charts identify Haar measure with a nonvanishing local density times product \(\ell\)-adic measure, so the same conclusion holds on our compact open fibre.

Conditional Haar measure on each fibre of \(\Gamma\to\widehat{\mathbf Z}\) is translated Haar measure on its kernel. The fibre of \(Z_\delta\) therefore has measure zero for every \(z\), and Fubini gives \(\operatorname{measure}(Z_\delta)=0\). Corollary 2.2 now proves:

**Lemma 3.1.** The closed points \(x\) for which \(\delta^{\deg x}\) is an eigenvalue of \(F_x\) on \(\mathcal V_{0,x}\) have Dirichlet density zero. The same holds for a finite union of prescribed units.

This supplies Deligne's (6.11)–(6.13), with the measure-zero and finite-quotient density steps made explicit. In the source, the degree generator in the multiplier equation is arithmetic; (3.1) uses the geometric generator, so the exponent has the corresponding opposite sign.

### Power-family rigidity

For a finite multiset \(A\) of field elements write
\[
A^{[d]}=\{a^d:a\in A\},\qquad
P_A^{[d]}(T)=\prod_{a\in A}(1-a^dT).
\tag{3.3}
\]
Multiplicities are retained.

**Lemma 3.2 (Deligne (6.7)).** Let \(A,B\) be finite multisets in a field. If \(A^{[d]}=B^{[d]}\) for every sufficiently large positive \(d\) not divisible by any member of a fixed finite set of integers at least \(2\), then \(A=B\).

**Proof.** Equality for one such \(d\) gives equal cardinalities and equal numbers of zeros; remove the zero entries. If an entry \(a\in A\) equals no entry \(b\in B\), the positive integers satisfying \(a^d=b^d\) are either absent or the multiples of the order \(h_b\ge2\) of the root of unity \(a/b\). Choose \(M\) divisible by all these finitely many orders and by all the prescribed excluded integers. Arbitrarily large \(d\equiv1\bmod M\) avoid them all. Then \(a^d\) equals no entry of \(B^{[d]}\), a contradiction. Some equal pair can therefore be removed; equality of the power multisets survives removing it, and induction proves the lemma. \(\square\)

The excluded integers must be nontrivial positive divisors. Allowing an exclusion that divides every positive integer would make the hypothesis vacuous.

We also need its sparse closed-point version: if two finite multisets of nonzero elements have equal degree-power multisets outside a density-zero exceptional set and finitely many divisibility exclusions, they are equal. The identical proof works: choose \(M\) as above, and Corollary 2.2 supplies a good closed point of degree \(1\bmod M\). Remove equal pairs and repeat. It is not necessary to claim a good point in each sufficiently large degree.

**Lemma 3.3 (denominator and universal-divisor detection).** For \(\mathcal V_0\) as above, let \(A,B\) be finite multisets of \(\ell\)-adic units, with no common entry. Outside a density-zero set and finitely many nontrivial degree-divisibility conditions, the reduced denominator of
\[
\det(1-F_xT\mid\mathcal V_{0,x})
\frac{P_A^{[\deg x]}(T)}{P_B^{[\deg x]}(T)}
\tag{3.4}
\]
is exactly \(P_B^{[\deg x]}(T)\). Moreover, if for finite unit multisets \(R,S\),
\[
P_S^{[\deg x]}\ \mid\
P_R^{[\deg x]}\det(1-F_xT\mid\mathcal V_{0,x})
\quad\text{for every }x,
\tag{3.5}
\]
then \(P_S^{[1]}\mid P_R^{[1]}\).

**Proof.** A collision \(a^d=b^d\) with \(a\ne b\) can occur only when \(d\) is divisible by a root-of-unity order at least \(2\). Exclude these finitely many orders. Lemma 3.1 excludes, on a density-zero set, all occurrences of \(b^{\deg x}\) as a varying eigenvalue. No denominator factor in (3.4) can then cancel.

For (3.5), cancel common entries of \(R,S\), with multiplicity. If \(S\) still has an entry \(s\), exclude its possible degree-power coincidences with \(R\) and its varying-eigenvalue exceptional set. A degree-\(1\bmod M\) point outside that exceptional set exists by Corollary 2.2. At this point \(s^{\deg x}\) is a reciprocal root of the left polynomial but not the right polynomial, contradicting divisibility. No entry of \(S\) remains. \(\square\)

## 4. Rationality of the vanishing quotient

Let \(f_0:\widetilde X_0\to D_0\simeq\mathbf P^1_{\mathbf F_q}\) be a Lefschetz pencil on a smooth projective geometrically connected variety of even dimension \(n+1\), so \(n\) is odd. Let \(U_0=D_0-S_0\). On \(U_0\) put
\[
\mathcal H_0=(R^nf_{0*}\mathbf Q_\ell)|_{U_0},\qquad
\mathcal E_0=\text{vanishing subspace sheaf},\qquad
\mathcal R_0=\mathcal E_0\cap\mathcal E_0^\perp,\qquad
\mathcal V_0=\mathcal E_0/\mathcal R_0.
\tag{4.1}
\]
These are defined arithmetically: Frobenius permutes the local vanishing directions and preserves their span, orthogonal complement and radical. The pairing on \(\mathcal V_0\) is alternating, nondegenerate and valued in \(\mathbf Q_\ell(-n)\). The twist convention in (4.1) is **untwisted** middle cohomology, unlike the scalar-normalized notation of Lesson 9.

**Theorem 4.1 (Deligne (6.2)).** For every closed point \(x\in U_0\),
\[
P_x(T):=\det(1-F_xT\mid\mathcal V_{0,x})\in\mathbf Q[T].
\tag{4.2}
\]

**Proof.** If \(\mathcal V_0=0\), then \(P_x=1\). Assume otherwise. Lesson 9 gives open geometric symplectic monodromy, so Lemmas 3.1–3.3 apply.

The sheaves \(R^if_{0*}\mathbf Q_\ell\) for \(i\ne n\), \(\mathcal H_0/\mathcal E_0\), and \(\mathcal R_0\) are geometrically constant. For the quotient, local Picard–Lefschetz transformations differ from the identity by vectors in \(\mathcal E_0\); for the radical, Lesson 9 identifies it with a subspace of the geometric invariants. A geometrically constant lisse sheaf comes from a representation of \(\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_q)\), so its degree-\(d\) polynomial is the product of \(1-\lambda^dT\) over the eigenvalues \(\lambda\) of base-field Frobenius.

These eigenvalues are \(\ell\)-adic units. Indeed any compact \(\ell\)-adic matrix group preserves a lattice: the sum of all translates of a fixed lattice is contained in a bounded larger lattice, hence finitely generated, and is stable. Both a matrix and its inverse are integral on that stable lattice, so every eigenvalue and its inverse are integral.

The cohomological zeta formula for the smooth fibre \(X_x\), and the filtration
\(\mathcal R_0\subset\mathcal E_0\subset\mathcal H_0\), now give finite unit multisets \(A,B\), independent of \(x\), such that
\[
Z(X_x,T)=P_x(T)
\frac{P_A^{[d_x]}(T)}{P_B^{[d_x]}(T)}\in\mathbf Q(T).
\tag{4.3}
\]
The middle dimension \(n\) is odd, so its determinant occurs in the numerator. All its remaining factors and every other degree factor are constant-field factors of the indicated type. The last rationality is the whole-fibre zeta rationality proved in Lesson 8; it does not assume rationality of the individual middle quotient. Cancel common entries of \(A,B\).

By Lemma 3.3, at good points the normalized reduced denominator of (4.3) is exactly \(P_B^{[d_x]}\). It is therefore rational. A good point exists, so every \(b\in B\) is algebraic over \(\mathbf Q\): \(b^{d_x}\) is a reciprocal root of a rational polynomial, and taking a \(d_x\)-th root preserves algebraicity. Moreover every conjugate of \(b\) remains an \(\ell\)-adic unit. Its degree power is a reciprocal root of that same polynomial, all of whose reciprocal roots are the original unit entries \(b'^{\,d_x}\).

For every automorphism \(\sigma\) of \(\overline{\mathbf Q}/\mathbf Q\), rationality of the good-point reduced denominators gives
\[
B^{[d_x]}=(\sigma B)^{[d_x]}
\quad\text{at all good points}.
\]
The sparse rigidity statement after Lemma 3.2 implies \(B=\sigma B\). Hence \(P_B^{[1]}\in\mathbf Q[T]\).

Multiplying (4.3) by \(P_B^{[d_x]}\) gives, at every point, the polynomial
\[
Q_x(T)=P_x(T)P_A^{[d_x]}(T)\in\mathbf Q[T].
\tag{4.4}
\]
The right expression is a polynomial, and the left is a rational function over \(\mathbf Q\); its finite Taylor coefficients therefore are rational. Every \(a\in A\) is algebraic by taking a reciprocal root of one such \(Q_x\). Its conjugates are units as well: all reciprocal roots of \(Q_x\) are unit eigenvalues from \(P_x\) or unit entries from \(A\).

Since \(Q_x\) is rational, \(P_{\sigma A}^{[d_x]}\) divides \(Q_x=P_xP_A^{[d_x]}\) for every \(x\). This is genuine polynomial divisibility over \(\overline{\mathbf Q}\): the original divisor is algebraic, and polynomial division of \(Q_x\) by it has zero remainder. Lemma 3.3 yields \(P_{\sigma A}^{[1]}\mid P_A^{[1]}\). They have equal degrees, so they coincide. Thus \(P_A^{[1]}\in\mathbf Q[T]\).

Finally (4.3) expresses \(P_x=Z(X_x,T)P_B^{[d_x]}/P_A^{[d_x]}\) as a rational function over \(\mathbf Q\). It is already known to be a polynomial; hence it belongs to \(\mathbf Q[T]\). \(\square\)

The conjugates in this argument were proved to be units using rational point polynomials before Lemma 3.3 was applied to them. No assumption that an arbitrary automorphism of an algebraic closure of \(\mathbf Q_\ell\) preserves its valuation was made. The sparse rigidity argument also avoids strengthening density zero into a nonexistent guarantee about every degree.

**Corollary 4.2.** The eigenvalues on
\(H^1(D,j_*\mathcal V)\) are algebraic, and all conjugates satisfy
\[
q^{n/2}\le|\alpha|\le q^{n/2+1}.
\tag{4.5}
\]
**Proof.** The pairing, Lesson 9's openness, and Theorem 4.1 verify all hypotheses of the fundamental estimate with \(\beta=n\). Apply Lesson 10, Corollary 6.2. This is Deligne (6.3). \(\square\)

## 5. The even-dimensional estimate

**Lemma 5.1 (Deligne (7.1)).** Let \(X_0\) be smooth, projective and geometrically irreducible, of even dimension \(d\). Every eigenvalue on \(H^d(X,\mathbf Q_\ell)\) is algebraic and every complex conjugate satisfies
\[
q^{d/2-1/2}\le|\alpha|\le q^{d/2+1/2}.
\tag{5.1}
\]

**Proof.** Induct over even \(d\). For \(d=0\), \(X\) is a point and the only eigenvalue is \(1\).

Let \(d=n+1=2m+2\ge2\). By Lesson 9 and the finite-extension reduction, choose a Lefschetz pencil after re-embedding. Extend the field further so that its singular parameters are rational, its sign-defined vanishing cycles in \(H^n(m)\) are defined over the field, it has a rational smooth member \(X_u\), and that member has a smooth hyperplane section \(Y\) defined over the field. Each condition requires only a finite extension. The section \(Y\) has even dimension \(d-2\); if it is disconnected, apply the induction componentwise.

The codimension-two blow-up formula injects \(H^d(X)\) as a Frobenius-stable summand of \(H^d(\widetilde X)\). For \(f:\widetilde X\to D=\mathbf P^1\), Leray gives a Frobenius-equivariant filtration whose associated pieces are subquotients of
\[
H^2(D,R^{n-1}f_*\mathbf Q_\ell),\quad
H^1(D,R^nf_*\mathbf Q_\ell),\quad
H^0(D,R^{n+1}f_*\mathbf Q_\ell).
\tag{5.2}
\]
It suffices to bound every eigenvalue on these three terms. Taking invariant subspaces, quotients or finite extensions of representations cannot introduce a new eigenvalue. No degeneration of Leray is asserted.

**The first term.** The sheaf \(R^{n-1}f_*\mathbf Q_\ell\) is geometrically constant in both pencil alternatives of Lesson 9. Its arithmetic fibre is \(H^{n-1}(X_u)\), hence the term is
\(H^{n-1}(X_u)(-1)\). Weak Lefschetz gives the equivariant injection
\[
H^{n-1}(X_u)(-1)\hookrightarrow
H^{d-2}(Y)(-1).
\tag{5.3}
\]
The induction bound for \(Y\) is \(q^{(d-2)/2\pm1/2}\). Twisting by \((-1)\) multiplies eigenvalues by \(q\), giving (5.1).

**The third term.** The dual Gysin map
\[
H^{d-2}(Y)(-1)\twoheadrightarrow H^{n+1}(X_u)
\tag{5.4}
\]
is surjective, so the same bound applies to its target. If the cycles are nonzero, \(R^{n+1}f_*\mathbf Q_\ell\) is geometrically constant and its \(H^0\) is this target. If the cycles are zero, the global exceptional sequence of Lesson 9 makes its \(H^0\) an extension of that target by a subquotient of
\[
\bigoplus_{s\in S}\mathbf Q_\ell(m-n).
\tag{5.5}
\]
There is no \(H^1\) of this punctual sheaf. Since \(m-n=-d/2\), Frobenius on (5.5) is \(q^{d/2}\), within (5.1). This uses the chosen field of definition of the sign-defined cycles.

**The middle term.** Put \(M=R^nf_*\mathbf Q_\ell\). If all cycles are zero, \(M\) is geometrically constant and \(H^1(D,M)=0\). Otherwise \(M=j_*\mathcal H\). Use \(\mathcal E,\mathcal R,\mathcal V\) from (4.1); the vanishing cycles are conjugate.

First suppose their images in \(\mathcal V\) are nonzero. The following sequences of sheaves on \(D\) are exact:
\[
0\to j_*\mathcal E\to M\to C_1\to0,\qquad
0\to C_2\to j_*\mathcal E\to j_*\mathcal V\to0,
\tag{5.6}
\]
where \(C_1\) is the geometrically constant quotient \(\mathcal H/\mathcal E\), and \(C_2=j_*\mathcal R\) is geometrically constant.

We check surjectivity at a singular point, where taking inertia invariants need not generally be exact. A stalk of \(M\) is
\(\delta_s^\perp\subset H^n(X_u)\). Any class of \(H/\mathcal E\) has a representative orthogonal to \(\delta_s\): adjust it by an element of \(\mathcal E\), whose pairing with \(\delta_s\) is nonzero for a suitable element because \(\delta_s\notin\mathcal R\). This proves the first surjectivity. For the second, an invariant class in \(\mathcal V\) is orthogonal to the nonzero \(\bar\delta_s\). Every lift in \(\mathcal E\) has that same pairing, since \(\mathcal R\) pairs trivially; hence the lift is inertia-invariant. This proves the second surjectivity. The kernels are the indicated subspaces, and away from \(S\) exactness is immediate.

Since \(H^1(D,C_i)=0\), the long exact sequences give a surjection
\[
H^1(D,j_*\mathcal E)\twoheadrightarrow H^1(D,M)
\]
and an injection
\[
H^1(D,j_*\mathcal E)\hookrightarrow H^1(D,j_*\mathcal V).
\]
Thus \(H^1(D,M)\) is a subquotient of the space in Corollary 4.2. Its bounds \(q^{n/2}\) to \(q^{n/2+1}\) are precisely (5.1).

The remaining alternative is that the nonzero cycles all belong to the radical. Their span is then \(\mathcal E=\mathcal R\subset\mathcal E^\perp\), and \(\mathcal E^\perp\) is geometrically constant by the invariant-space theorem. The quotient \(C=\mathcal H/\mathcal E^\perp\) is also geometrically constant: every local transformation changes a vector by a vector in \(\mathcal E\), hence acts trivially on this quotient. At \(s\), the image of \(M_s=\delta_s^\perp\) in \(C\) is the kernel of the nonzero functional given by pairing with \(\delta_s\). Consequently there are exact sequences
\[
0\to j_*\mathcal E^\perp\to M\to K\to0,\qquad
0\to K\to C\to
\bigoplus_{s\in S}\mathbf Q_\ell(m-n)_s\to0.
\tag{5.7}
\]
The final map is surjective at each punctual stalk because \(\delta_s\ne0\) and the full fibre pairing is nondegenerate. Since the two constant sheaves have no \(H^1\), these sequences inject \(H^1(D,M)\) into \(H^1(D,K)\), which is a quotient of (5.5). Its eigenvalues are therefore \(q^{d/2}\).

This last case is needed before hard Lefschetz has been proved. The punctual line in (5.7) has twist \(m-n=-d/2\), as follows directly from \(x\mapsto(x,\delta_s)\) with \(\delta_s\in H^n(m)\). The printed \(n-m\) in Deligne's (7.1.5) and its following cohomology line would give \(q^{-d/2}\), contrary to the stated \(q^{d/2}\). The local pairing fixes the sign used here.

All terms in (5.2) have algebraic eigenvalues with the all-conjugates bound (5.1). The Leray filtration and the blow-up summand then prove the lemma. \(\square\)

## 6. Removing the error and proving all degrees

**Proposition 6.1.** Middle cohomology of a smooth projective geometrically irreducible \(d\)-fold is pure of weight \(d\).

**Proof.** For every positive even \(k\), Künneth places
\[
H^d(X)^{\otimes k}\subset H^{kd}(X^k)
\]
as a Frobenius-stable direct summand. Thus \(\alpha^k\) is an eigenvalue in middle degree \(kd\), which is even. Lemma 5.1 gives algebraicity and
\[
q^{kd/2-1/2}\le|\alpha'|^k\le q^{kd/2+1/2}
\tag{6.1}
\]
for every conjugate \(\alpha'\), once algebraicity of \(\alpha\) is recovered from any one such power. Take \(k\)-th roots and let \(k\to\infty\) through the even integers. Both bounds tend to \(q^{d/2}\). \(\square\)

**Proof of Theorem 1.1 in every degree.** After the component and extension reductions of §1, assume \(X_0\) geometrically irreducible of dimension \(d\). Middle degree is Proposition 6.1. If \(i<d\), successively choose smooth hyperplane sections over finite extensions. Weak Lefschetz embeds \(H^i(X)\) into the degree-\(i\) cohomology of a smooth projective variety of dimension \(i\); at the last step restriction is injective, and earlier steps are isomorphisms. Proposition 6.1 applies to the middle degree of each component of that variety. Eigenvalues of the original subspace satisfy the same algebraicity and all-conjugates assertion. The finite-extension reduction descends it to the original field.

If \(i>d\), Poincaré duality reduces to \(2d-i<d\). Its paired eigenvalue is \(q^d/\alpha\), of modulus \(q^{(2d-i)/2}\), giving \(|\alpha|=q^{i/2}\). Degrees outside \(0,\ldots,2d\) have zero cohomology. The zero-dimensional reduction is the permutation action on the finitely many geometric points, whose eigenvalues are roots of unity. Disjoint unions finish the general case. \(\square\)

### An alternative passage from middle degree to all degrees

There is also a product argument, attributed to A. Mellit in Milne's *Lectures*, §28, footnote on printed p.162. It begins **after** Proposition 6.1, so it does not remove the weak Lefschetz input from Lemma 5.1. We spell it out to distinguish the two reductions.

Let \(d>0\) and let \(X_0\) be geometrically connected. Frobenius on \(H^0(X)\) is \(1\), and on \(H^{2d}(X)\) is \(q^d\), by the normalized trace. If \(\alpha\) occurs in \(H^i(X)\) and \(i>d\), Künneth puts
\[
H^i(X)^{\otimes d}\otimes H^0(X)^{\otimes(i-d)}
\subset H^{id}(X^i).
\tag{6.1a}
\]
The product has dimension \(id\), and its middle eigenvalue includes \(\alpha^d\). Proposition 6.1 therefore makes \(\alpha\) algebraic and gives \(|\sigma(\alpha)|^d=q^{id/2}\), hence weight \(i\).

If \(0\le i<d\), use instead
\[
H^i(X)^{\otimes d}\otimes H^{2d}(X)^{\otimes(d-i)}
\subset H^{d(2d-i)}(X^{2d-i}).
\tag{6.1b}
\]
Its eigenvalue is \(\alpha^d q^{d(d-i)}\). Middle purity makes this algebraic and has modulus \(q^{d(2d-i)/2}\). Dividing by the rational power \(q^{d(d-i)}\) and taking the \(d\)-th root again gives \(q^{i/2}\) for every conjugate. An eigenvalue of a tensor product is a product of eigenvalues even for nondiagonalizable operators: triangularize each matrix over a splitting field and read the diagonal of the tensor matrix. Thus neither reduction assumes semisimplicity. The component and finite-extension reductions of §1 finish this second proof.

### The integer polynomials and independence of \(\ell\)

Put \(P_i(T)=\det(1-FT\mid H^i(X,\mathbf Q_\ell))\). Lesson 8 gives
\[
Z(X_0,T)=\prod_iP_i(T)^{(-1)^{i+1}}\in\mathbf Q(T),
\qquad Z(X_0,T)\in1+T\mathbf Z[[T]].
\tag{6.2}
\]
The theorem separates the reciprocal roots in degree \(i\) by their modulus \(q^{i/2}\). Different degrees have different moduli, so no cancellation occurs between different degree factors. The reduced numerator and denominator of \(Z\) therefore determine \(P_i\) uniquely by this modulus and its parity. Every conjugate of a degree-\(i\) eigenvalue has the same modulus, so these factors are Galois-stable and belong to \(\mathbf Q[T]\). The same unique factorization of the same rational zeta function determines them for every \(\ell\), proving independence of \(\ell\).

We include the integrality argument. Write the reduced zeta fraction \(P/Q\), normalized by \(P(0)=Q(0)=1\), over \(\mathbf Q\). For any prime \(v\), its integral Taylor coefficients converge \(v\)-adically on \(|T|_v<1\). There can be no denominator root in that disc: the convergent identity \(Q(T)Z(T)=P(T)\) at such a root would force a common numerator root, contradicting reduction. Hence every reciprocal denominator root has \(|\alpha|_v\le1\), for every embedding into a \(v\)-adic algebraic closure and every \(v\). These roots are algebraic integers.

For clarity, that last criterion is elementary: the conjugate roots of the monic minimal polynomial all have \(v\)-adic absolute value at most \(1\), so every rational elementary-symmetric coefficient belongs to \(\mathbf Z_v\) for every prime \(v\), and therefore to \(\mathbf Z\). The coefficients of \(Q\) are thus integers. Then \(P=QZ\) also has integer coefficients. Its reciprocal polynomial is monic integral because \(P(0)=1\), so its reciprocal roots are algebraic integers too.

Each rational \(P_i\) is a factor selected from these numerator or denominator roots. Its coefficients are rational algebraic integers, hence integers. We have proved
\[
P_i(T)\in\mathbf Z[T],
\quad\text{independent of }\ell.
\tag{6.3}
\]
This argument does not invoke a separate unproved general integrality theorem.

Together, (6.2)–(6.3), Theorem 1.1, and the duality functional equation proved in Lesson 8 give the Weil conjectures. If \(X_0\) has pure dimension \(d\) and Euler characteristic \(\chi\), that functional equation is
\[
Z(X_0,1/(q^dT))
=\varepsilon\,q^{d\chi/2}T^\chi Z(X_0,T),
\qquad\varepsilon\in\{1,-1\},
\tag{6.4}
\]
with the precise sign as in Lesson 8. No comparison with singular cohomology of a complex lift was needed; the \(b_i=\dim H^i(X,\mathbf Q_\ell)\) here are étale Betti numbers.

### The full smooth-proper scope and its alteration proof

**Smooth-proper theorem (Deligne, Weil II (3.3.9)).** For every smooth proper \(X_0/\mathbf F_q\), without a projectivity, pure-dimension or geometric-connectedness assumption, every eigenvalue on \(H^i(X,\mathbf Q_\ell)\) is algebraic and every complex conjugate has modulus \(q^{i/2}\). Each individual polynomial
\[
P_i(T)=\det(1-FT\mid H^i(X,\mathbf Q_\ell))
\in\mathbf Z[T]
\tag{6.5}
\]
is independent of \(\ell\). This is the full purity input needed for the smooth-proper factorization theorem of Lesson 8. The projective case is already proved above. We now give the geometric input at its proof homes and the complete cohomological passage to the proper case.

**Geometric input (smooth projective alteration).** For each smooth proper geometrically integral \(d\)-fold \(X_0/\mathbf F_q\), Smooth projective alterations, Theorem 1.1 gives, after a finite extension \(k'=\mathbf F_{q^a}\), a proper dominant generically finite and generically separable morphism
\[
 f_0:Y_0\longrightarrow X_0\times_{\mathbf F_q}k',
\]
where \(Y_0/k'\) is smooth projective and geometrically integral. Its generic degree \(e\) is a positive integer, and it is finite étale of rank \(e\) over a nonempty open.

Here is the precise dependency of this geometric theorem. The alteration lesson first makes a projective birational modification of a proper integral target, then constructs and flattens a marked curve fibration. Its §5 uses Stable pointed-family extension, Theorem S.9 in §9, including genus zero and genus one, with the labelled generic identifying isomorphism retained. Its §6 extends the curve map; §7 proves the global monomial resolution and the induction for pairs with boundary. Those modifications are projective and birational, and the field-changing covers are generically separable. Thus the result has the smooth projective source required here.

The finite-field assertion is the finite-algebraic descent in its §8. Over \(\overline{\mathbf F}_q\), the schemes, morphisms, projective embeddings, finitely many coherent blowup ideals and a dense finite étale comparison open use only finitely many coefficients. They therefore descend together to one finite extension \(k'\). Smoothness, geometric integrality, properness and the comparison open's finite étale rank descend by faithfully flat base change. The completed coordinates used to check local charts are proof certificates; no arbitrary formal power series has to descend. This supplies exactly the former alteration premise of Proposition 6.2.

**Proposition 6.2 (pullback and trace).** The geometric input above, the projective theorem, and the constructed smooth trace and duality maps imply the full smooth-proper theorem.

**Proof.** First let \(X_0\) be geometrically integral of dimension \(d>0\). Base change \(f_0\) to \(\overline{\mathbf F}_q\) and write \(f:Y\to X\). Put \(E=\mathbf Q_\ell\). Both \(X\) and \(Y\) are smooth proper of dimension \(d\), so Smooth traces, duality and Gysin maps, Theorem 10.1 and coefficient recovery give the normalized perfect pairings
\[
 H^i(X,E)\times H^{2d-i}(X,E(d))
 \longrightarrow E,\qquad (x,v)\longmapsto\int_X x\cup v,
\]
and the same pairing on \(Y\). Define an actual linear map
\[
 f_*:H^i(Y,E)\longrightarrow H^i(X,E)
 \quad\text{by}\quad
 \int_X f_*u\cup v=\int_Y u\cup f^*v
 \tag{6.6}
\]
for every \(v\in H^{2d-i}(X,E(d))\). Perfection makes the right side the functional of one and only one class. The trace and pullback are natural under field automorphisms; since \(f_0\) is defined over \(k'\), \(f_*\) and \(f^*\) commute with \(F^a\). We do not assume that \(f\) is smooth.

We verify the degree normalization rather than assume a pushforward formula. Choose the dense open \(U\subset X\) on which \(f\) is finite étale of rank \(e\), and put \(V=f^{-1}U\). Write \(j:U\hookrightarrow X\) and \(j':V\hookrightarrow Y\). Both proper complements have dimension at most \(d-1\). Their cohomology vanishes in degrees \(2d-1\) and \(2d\), by the compact-support dimension bound and properness. Localization consequently gives isomorphisms
\[
 j_!:H^{2d}_c(U,E(d))\xrightarrow{\sim}H^{2d}(X,E(d)),
 \qquad
 j'_!:H^{2d}_c(V,E(d))\xrightarrow{\sim}H^{2d}(Y,E(d)).
\]
The map \(f\) is proper, so pullback preserves these compact supports. The Cartesian open square, or equivalently \(f^*j_!E=j'_!E\), identifies this pullback with the finite étale pullback from \(U\) to \(V\); it is compatible with the two displayed extension maps.

On the finite étale cover, the actual sheet-sum trace satisfies
\[
 \operatorname{tr}_{V/U}\circ f^*=e\,\mathrm{id}.
\]
The trace lesson's §2.4 proves compatibility of the smooth trace with these étale sheet sums and with open extension. Hence for \(z\in H^{2d}(X,E(d))\), lift \(z\) uniquely to \(z_U\in H^{2d}_c(U,E(d))\) and calculate
\[
 \int_Y f^*z
 =\int_V f^*z_U
 =\int_U\operatorname{tr}_{V/U}f^*z_U
 =e\int_U z_U
 =e\int_X z.
 \tag{6.7}
\]
Every map here is one of the previously constructed trace, pullback or open-extension maps. In particular this calculation uses smoothness of the two varieties and étaleness on the comparison open, without a trace construction on a singular alteration source.

For \(x\in H^i(X,E)\) and the complementary-degree test class \(v\), cup-product naturality gives
\[
 \int_X f_*f^*x\cup v
 =\int_Y f^*(x\cup v)
 =e\int_X x\cup v.
\]
Perfection proves \(f_*f^*=e\,\mathrm{id}\) in every degree. The integer \(e\) is invertible in \(E\), even when \(\ell\mid e\). Thus \(r=e^{-1}f_*\) is a retraction of \(f^*\), and
\[
 p=e^{-1}f^*f_*:H^i(Y,E)\longrightarrow H^i(Y,E),
 \qquad p^2=p,
 \tag{6.8}
\]
is a rational \(\ell\)-adic projector commuting with \(F^a\). Its image is \(f^*H^i(X,E)\), and its kernel is \(\ker f_*\). We obtain the actual \(F^a\)-stable decomposition
\[
 H^i(Y,E)=f^*H^i(X,E)\oplus\ker f_*.
\]
No prime-to-\(\ell\) degree restriction and no Frobenius semisimplicity are needed.

If \(\alpha\) is an eigenvalue of \(F\) on \(H^i(X,E)\), then \(\alpha^a\) is an eigenvalue of \(F^a\); triangularization proves this also for a nondiagonalizable operator. The splitting places it among the eigenvalues on \(H^i(Y,E)\). Projective purity over \(k'\) makes \(\alpha^a\) algebraic and gives every complex conjugate modulus \(q^{ai/2}\). If \(m(S)\in\mathbf Q[S]\) annihilates \(\alpha^a\), then \(m(T^a)\) annihilates \(\alpha\), proving its algebraicity. Every embedding \(\sigma:\mathbf Q(\alpha)\hookrightarrow\mathbf C\) restricts to one on \(\mathbf Q(\alpha^a)\), so
\[
 |\sigma(\alpha)|^a
 =|\sigma(\alpha^a)|=q^{ai/2}.
\]
Taking the positive \(a\)-th root gives \(|\sigma(\alpha)|=q^{i/2}\). This is the complete weight descent through the finite-field extension.

For a general smooth proper \(X_0\), its finitely many geometric irreducible components are disjoint: they are the connected components of a regular scheme. After a finite extension each component and its defining equations descend separately, and Frobenius raised to that extension degree preserves them. Apply the preceding argument to each geometrically integral component in its own dimension. A zero-dimensional smooth component consists geometrically of points and has only degree-zero cohomology with permutation eigenvalues. Direct sums and the same power descent therefore prove algebraicity and weight \(i\) without a dimension or connectedness restriction.

It remains to recover the individual integer polynomials over the original field. Use only Lesson 8's whole-function rationality, Corollary 3.2, and its Euler product (1.2):
\[
 Z(X_0,T)=\prod_i\det(1-FT\mid H^i(X,E))^{(-1)^{i+1}}
 \in\mathbf Q(T)\cap(1+T\mathbf Z[[T]]).
\]
Lesson 8's individual-factor Theorem 3.4 is a forward consequence of the purity we have just proved, so it is not an input. Pure weights give different moduli \(q^{i/2}\) in different degrees, and therefore prevent cancellation between their factors. Every algebraic conjugate stays in the same degree's modulus group. Grouping the reciprocal roots of the reduced rational numerator and denominator by those moduli, with their multiplicities, makes each \(P_i\) Galois-stable and hence rational. The prime-by-prime argument of (6.2)–(6.3) makes these roots algebraic integers and their rational factor coefficients integers. Finally the point-count zeta function and this unique grouping are independent of \(\ell\). This proves (6.5) for the full smooth-proper scope. \(\square\)

The route consists of the constructed smooth projective alteration and the splitting just proved. It establishes the canonical constant-coefficient smooth-proper statement without importing Weil II's general direct-image theorem. The mixed-sheaf, pure-lisse and hard-Lefschetz results in §7 retain their separate stated proof requirements.

## 7. Applications and examples

### Complete intersections

**Theorem 7.1 (Deligne (8.1)).** Let \(X_0\subset\mathbf P^{n+r}_{\mathbf F_q}\) be a smooth complete intersection of dimension \(n\). Let \(b\) be the dimension of its primitive middle cohomology, defined as the quotient by the ambient middle class when \(n\) is even and as all middle cohomology when \(n\) is odd. Then for every \(a\ge1\),
\[
\left|\#X_0(\mathbf F_{q^a})-\#\mathbf P^n(\mathbf F_{q^a})\right|
\le bq^{an/2}.
\tag{7.1}
\]

We first justify the cohomology outside the middle, including for a presentation whose intermediate intersections might be singular. Fix the multidegrees \(d_1,\ldots,d_r\). Over the algebraic closure, tuples of defining equations belong to a product of projective coefficient spaces. The locus \(T\) where their intersection is smooth of the expected dimension is open and contains the given tuple. It is an irreducible, hence connected, nonempty open subset. The universal complete intersection over \(T\) is smooth and proper. Smooth proper base change makes each \(R^if_*\mathbf Q_\ell\) lisse, so its rank is constant on \(T\).

There is a tuple for which all successive intersections are smooth: choose each equation generally on the previous smooth intersection, using Bertini for the very ample bundle \(\mathcal O(d_j)\). For that tuple, successive weak Lefschetz and duality give the ranks
\[
\dim H^i(X)=
\begin{cases}
1,&i\ne n,\ 0\le i\le2n,\ i\text{ even},\\
0,&i\ne n,\ i\text{ odd}.
\end{cases}
\tag{7.2}
\]
Rank constancy proves (7.2) for every smooth tuple in \(T\). This deformation argument uses étale smooth proper base change, not a complex lift.

To recover exactly Deligne's topological constant, form the same product of coefficient projective spaces over \(\mathbf Z\). Its open locus \(T_{\mathbf Z}\) of smooth complete intersections of the expected dimension is integral and contains the given characteristic-\(p\) tuple. The universal family on that locus is smooth proper. The connected open \(T_{\mathbf Z}[1/\ell]\) contains that tuple and a characteristic-zero geometric point, so smooth proper base change equates their étale Betti numbers. Embed the latter point's algebraic-number field in \(\mathbf C\). [*Comparison with singular cohomology*, Theorem 7.2 and §14](course:ag-etale-cohomology/comparison-with-singular-cohomology) proves proper finite-coefficient comparison and its derived-limit passage to \(\mathbf Q_\ell\), using its expressly stated Riemann-existence and projective-curve GAGA inputs. Consequently
\[
b=b_n(X^{\mathrm{an}}_{\mathbf C})-\begin{cases}1,&n\text{ even},\\0,&n\text{ odd},\end{cases}
\tag{7.2a}
\]
for any complex smooth complete intersection of these multidegrees. Thus the étale formulation gives the same constant as Deligne (8.1); topological comparison is needed for this identification, not for the point-count inequality itself.

Let \(h=c_1(\mathcal O_X(1))\in H^2(X,\mathbf Q_\ell(1))\). The degree formula
\(\int_Xh^n=d_1\cdots d_r\ne0\) shows that every \(h^j\), \(0\le j\le n\), is nonzero: if one were zero, multiplication by the remaining powers would make \(h^n\) zero. Therefore it generates each one-dimensional even group outside the middle. Frobenius on its untwisted degree-\(2j\) line is \(q^j\). When \(n\) is even it also gives a Frobenius-stable middle line, of eigenvalue \(q^{n/2}\); use the quotient by this line to define the primitive part. No splitting by hard Lefschetz is required.

The trace formula, subtracting these ambient lines, gives the exact identity
\[
\#X_0(\mathbf F_{q^a})
 =1+q^a+\cdots+q^{an}
   +(-1)^n\operatorname{Tr}(F^a\mid H^n_{\rm prim}(X)).
\tag{7.3}
\]
The primitive quotient has \(b\) eigenvalues. Theorem 1.1 gives modulus \(q^{n/2}\) for each; powers have modulus \(q^{an/2}\), and the triangle inequality proves (7.1). For \(n=0\), the ambient line is the unit class in \(H^0\), \(b=\deg X_0-1\), and the same argument applies. \(\square\)

### Odd-dimensional hypersurfaces and the pencil shortcut

For a smooth hypersurface of odd dimension \(n\), (7.2) says that the entire middle group is primitive, and
\[
Z(X_0,T)=
\frac{\det(1-FT\mid H^n(X))}
     {\prod_{j=0}^{n}(1-q^jT)}.
\tag{7.4}
\]
Its middle numerator is rational even before the final purity separation: multiply its rational zeta function by the displayed rational denominator. The integral-series argument of §6 then makes this polynomial integral.

Here is the geometry behind Deligne's remark (5.12). In a genuine Lefschetz pencil of degree-\(d\) hypersurfaces on \(\mathbf P^{n+1}\), let \(B\) be the smooth axis. The blow-up formula and (7.2) for the even-dimensional complete intersection \(B\) give
\[
H^n(\widetilde{\mathbf P}^{n+1})
 =H^n(\mathbf P^{n+1})\oplus H^{n-2}(B)(-1)=0.
\tag{7.5}
\]
For \(n=1\) the second summand is a negative-degree group and is zero.

After the theorem proved in §6, we can check explicitly that all middle cohomology is vanishing. In Leray, \(H^0(D,R^nf_*\mathbf Q_\ell)\) embeds into the cohomology of a smooth fibre, so it is pure of weight \(n\). The possible outgoing differential
\[
H^0(D,R^nf_*\mathbf Q_\ell)
\longrightarrow H^2(D,R^{n-1}f_*\mathbf Q_\ell)
\]
has target pure of weight \(n+1\), because \(R^{n-1}\) is geometrically constant and \(H^2(D)\) adds \((-1)\). Frobenius-equivariance and disjoint eigenvalue moduli force this differential to vanish. There are no other outgoing or incoming differentials at this position. Equation (7.5) forces the source to be zero. The invariant-space theorem of Lesson 9 identifies this source with \(E^\perp\); hence \(E^\perp=0\), and \(E=H^n\). Its pairing is nondegenerate, so the vanishing quotient is also all \(H^n\).

Consequently, when this identification and a pencil containing the fibre are available, the fundamental estimate of Lesson 10, with \(\beta=n\), applies directly to the middle numerator (7.4). Our verification of the identification above uses the completed purity theorem. It is an application of that theorem and supplies no circular input to §5.

Deligne explicitly notes in (5.12), printed p.294, that the required pencil for an arbitrary prescribed hypersurface is not supplied by the sketch and that completing the argument needs the later induction. The unconditional assertion for every smooth odd-dimensional hypersurface follows from §6 and (7.1), including when that shortcut has not been constructed.

### Smooth cubic surfaces

Use the classical geometric fact that every smooth cubic surface over an algebraically closed field is the blow-up of \(\mathbf P^2\) at six points in general position. This additional input for the example is recorded in Dolgachev–Duncan, §2, pp.8–9, in arbitrary characteristic.

Successive blow-up formulas give seven divisor classes spanning \(H^2(X,\mathbf Q_\ell(1))\): the pullback of a line and the six exceptional divisors. They are all defined over some finite extension of the finite base field. Thus some power \(F^a\) acts as the identity on this twisted group. Every untwisted \(H^2\)-eigenvalue is \(q\zeta\) with \(\zeta^a=1\). This proves its weight directly from algebraic classes. Formula (7.2) gives no odd cohomology, and the trace formula becomes
\[
\#X_0(\mathbf F_q)=1+q^2+q\sum_{j=1}^7\zeta_j.
\tag{7.6}
\]
The ambient hyperplane class contributes \(\zeta=1\); the primitive dimension is six. If all seven classes are defined over the base field, the count is \(q^2+7q+1\).

For a concrete nonsplit example, the Fermat cubic \(\sum_{j=0}^3x_j^3=0\) is smooth over \(\mathbf F_5\). Cubing is a bijection of \(\mathbf F_5\), so its affine cone has \(5^3\) points and its projective surface has \((5^3-1)/4=31\) points. Its 27 lines are obtained by partitioning the four coordinates into two pairs and setting \(x_i+\omega x_j=x_k+\eta x_l=0\), where \(\omega^3=\eta^3=1\). They are all defined over \(\mathbf F_{25}\). Six skew lines and the hyperplane class span \(H^2(1)\): in the blow-up model the latter is \(3H-\sum E_i\), so they also recover \(H\). Therefore every \(H^2\)-eigenvalue squares to \(25\). The trace is \(31-1-25=5\); seven eigenvalues each equal to \(5\) or \(-5\) must consist of four \(5\)'s and three \(-5\)'s. Thus
\[
P_2(T)=(1-5T)^4(1+5T)^3,\qquad
\#X_0(\mathbf F_{25})=25^2+7\cdot25+1=801.
\tag{7.6a}
\]

### Kloosterman sums

For \(a\in\mathbf F_q^\times\) and a nontrivial additive character \(\psi\), put
\[
\operatorname{Kl}(a)
 =\sum_{x\in\mathbf F_q^\times}\psi(x+a/x).
\]
The Artin–Schreier calculation of Lesson 8 identifies this with the negative Frobenius trace on a two-dimensional nontrivial-character sector of the smooth projective completion of
\[
z^p-z=x+a/x.
\tag{7.7}
\]
For an arbitrary \(\psi\), absorb its nonzero scalar into the right-hand side. The two simple poles remain, so the sector still has dimension two. The compact-support group on \(\mathbf G_m\) maps isomorphically to this sector: the boundary points are totally ramified and their permutation representations have no nontrivial character sector. Hence this particular \(H_c^1\) is a summand of projective curve \(H^1\), and is pure of weight one. If its eigenvalues are \(\beta_1,\beta_2\), Theorem 1.1 gives
\[
|\operatorname{Kl}(a)|=|\beta_1+\beta_2|\le2\sqrt q.
\tag{7.8}
\]
This explanation of the compact-support group matters: general \(H_c^1\) of an open curve need not be pure of weight one.

For example, over \(\mathbf F_3\), with \(a=1\) and \(\psi(1)=e^{2\pi i/3}\), the two summands are \(\psi(2)\) and \(\psi(1)\), so \(\operatorname{Kl}(1)=-1\). Its sector polynomial, computed in Lesson 8, is \(1-T+3T^2\), with reciprocal roots \((1\pm i\sqrt{11})/2\); both have modulus \(\sqrt3\).

### Two further statements and the Weil II outlook

**Exponential-sum bound (Deligne (8.4), stated).** Let \(Q\in\mathbf F_q[x_1,\ldots,x_s]\) have degree \(D\ge1\), prime to \(p\), and suppose its leading homogeneous part defines a smooth hypersurface in \(\mathbf P^{s-1}\). For a nontrivial additive character,
\[
\left|\sum_{x\in\mathbf F_q^s}\psi(Q(x))\right|
\le(D-1)^s q^{s/2}.
\tag{7.9}
\]
For \(D=1\) the sum is zero. The higher-degree deduction requires Deligne's (8.5)–(8.13): the nontrivial Artin–Schreier sectors are concentrated in degree \(s\), have dimension \((D-1)^s\), and have a perfect compact-support pairing, so inject into smooth projective cohomology. His parameter-family argument obtains these facts from the separated polynomial \(\sum x_j^D\), Künneth and the one-variable Swan calculation. Its additional geometric premise is a simultaneous smooth projective compactification with relative normal-crossing boundary, constructed using canonical resolution of surfaces because the singularities at infinity are étale locally products with a fixed surface singularity. That resolution and family construction are not proved here. Thus (7.9) is a stated application with a specific additional proof requirement, rather than a consequence of the general weight bound alone.

**Ramanujan–Petersson (Deligne (8.2), stated).** Let \(f=\sum_{m\ge1}a_m e^{2\pi imz}\), \(a_1=1\), be a holomorphic cuspidal newform of weight \(k\ge2\), level \(N\), and nebentype \(\varepsilon\). For a prime \(v\nmid N\), both roots of
\[
T^2-a_vT+\varepsilon(v)v^{k-1}
\]
have modulus \(v^{(k-1)/2}\). In particular
\[
|a_v|\le2v^{(k-1)/2}.
\tag{7.10}
\]
Its deduction uses the realization of these roots in middle cohomology through Eichler–Shimura and Kuga–Sato constructions. Those constructions are outside this course.

Weil II extends the framework from constant coefficients on projective varieties to mixed sheaves and separated maps. Fix \(\ell\ne p\), a finite coefficient extension \(E/\mathbf Q_\ell\), and an embedding \(\iota:\overline{\mathbf Q}_\ell\to\mathbf C\). A constructible \(E\)-Weil sheaf is \(\iota\)-pure of weight \(w\) if, at every closed point \(x\), each Frobenius eigenvalue has \(\iota\)-absolute value \(q_x^{w/2}\). It is \(\iota\)-mixed of weights at most \(w\) if it has a finite filtration with pure graded pieces of weights at most \(w\). For algebraic eigenvalues, asserting this for every embedding is the all-conjugates version used in this lesson. No definition of purity includes diagonalizability.

**Weil II direct-image theorem (Deligne (3.3.1) and (3.3.10), stated).** If \(f:X_0\to Y_0\) is separated and of finite type over \(\mathbf F_q\), and \(\mathcal F_0\) is a constructible \(\iota\)-mixed \(E\)-Weil sheaf of weights at most \(w\), then \(R^if_!\mathcal F_0\) is \(\iota\)-mixed of weights at most \(w+i\). This includes a bound on each closed fibre. It does not assert purity of those direct images. Deligne (3.3.10) is the fixed-\(\iota\), real-weight version; (3.3.1) is the algebraic, integral-weight formulation.

For constant coefficients of weight zero, the theorem and smooth duality would give the following broader conclusions:

| Geometry of \(X_0\) | Cohomology | Weight conclusion |
| --- | --- | --- |
| separated, finite type | \(H^i_c(X)\) | mixed, weights at most \(i\) |
| proper, possibly singular | \(H^i(X)=H^i_c(X)\) | mixed, weights at most \(i\) |
| smooth of pure dimension \(d\) | \(H^i(X)\) | mixed, weights at least \(i\) |
| smooth proper | \(H^i(X)=H^i_c(X)\) | pure of weight \(i\) |

For the third row, duality pairs \(H^i(X)\) with \(H^{2d-i}_c(X)\) into \(E(-d)\). An upper weight \(v\le2d-i\) of the compact group gives weight \(2d-v\ge i\) on the ordinary group. For the last row the lower and upper bounds meet. More generally a pure lisse sheaf of weight \(w\) on smooth proper \(X_0\) has \(H^i\) pure of weight \(w+i\), by applying the direct-image theorem to it and its dual. These deductions explain the canonical smooth-proper extension without pretending that a nonprojective variety has the pencils used in §5. The general direct-image theorem itself requires the additional weight and local-monodromy arguments of Weil II; it has not been proved by the special symplectic estimate of Lesson 10.

The formulation in Stacks, Tag 03VH, starts with a representation whose closed-point characteristic polynomials have coefficients in a number field and whose eigenvalues are pure of weight zero. Under those stipulated conclusions, the theorem above with \(w=0\) gives its compact-cohomology bound, and smooth proper duality gives purity in degree \(i\). Obtaining number-field coefficients and compatible companion representations from an irreducible representation with finite-order determinant is a separate representation-theoretic problem; it is not a consequence of our constant-coefficient tensor argument.

For example, localization for \(\mathbf G_m=\mathbf P^1-\{0,\infty\}\) gives \(H^1_c(\mathbf G_m,E)=E\) and \(H^2_c(\mathbf G_m,E)=E(-1)\), whereas duality gives \(H^1(\mathbf G_m,E)=E(-1)\). The degree-one compact group has weight zero, and its ordinary counterpart has weight two. The two inequalities are sharp and cannot be replaced by degree-one purity.

**Hard Lefschetz (Deligne (4.1.1) and the coefficient extension (6.2.13), stated).** If \(X_0\) is smooth projective of pure dimension \(d\), \(\mathcal F_0\) is a pure lisse \(E\)-Weil sheaf, and \(h\) is the class of an ample line bundle, then for \(0\le r\le d\),
\[
h^r:H^{d-r}(X,\mathcal F)
\xrightarrow{\ \sim\ }
H^{d+r}(X,\mathcal F(r)).
\tag{7.11}
\]
Theorem (4.1.1) is the constant-coefficient theorem. For the coefficient extension apply (6.2.13) with \(K=\mathcal F\) in degree zero and \(n=d\): on smooth \(X\), \(DK[-2d]=\mathcal F^\vee(d)\) is also in degree zero and both support conditions hold. The sheaf spread from the given finite-field pure sheaf supplies potential purity. Its proof requires Weil II's Lefschetz and invariant-cycle arguments in addition to weights. These are outlook results with these separate proof requirements; (7.11) is not available to simplify the radical case of (5.7).

The finite-field theorem supplies local Frobenius weights for varieties over finite residue fields. An analogue for a global arithmetic zeta function would require further global objects and analytic properties; no such global construction follows from this proof.

## 8. Graded exercises with solutions

**Exercise 11.1 (easy — the curve consequence).** For a smooth projective geometrically connected curve of genus \(g\), derive its Riemann-hypothesis factorization and point-count bound from Theorem 1.1. Identify where the independent curve proof was used in this lesson.

**Solution.** Its three cohomological polynomials are \(P_0=1-T\), \(P_1=\prod_{j=1}^{2g}(1-\alpha_jT)\), and \(P_2=1-qT\). The theorem gives \(|\sigma(\alpha_j)|=\sqrt q\), and §6 gives \(P_1\in\mathbf Z[T]\), independent of \(\ell\). Therefore
\[
Z(C_0,T)=\frac{P_1(T)}{(1-T)(1-qT)},\qquad
\#C_0(\mathbf F_{q^a})=q^a+1-\sum_j\alpha_j^a,
\]
and the absolute difference from \(q^a+1\) is at most \(2gq^{a/2}\). Lesson 5, Theorem 5.3, proves the curve Riemann hypothesis independently using the surface Hodge inequality and Frobenius graphs on \(C\times C\). We used that result on completed covering curves and their twists in §2. The consequence above is consistent with that input and does not replace its independent proof.

**Exercise 11.2 (medium — the tensor-power reduction).** Assume only the even-dimensional estimate (5.1), weak Lefschetz, duality and Künneth. Prove purity in every dimension and degree, including algebraicity and descent through finite extensions.

**Solution.** For a geometrically irreducible \(d\)-fold and a middle eigenvalue \(\alpha\), every positive even \(k\) gives \(\alpha^k\) in middle cohomology of \(X^k\), of even dimension \(kd\). Algebraicity of \(\alpha^2\) makes \(\alpha\) algebraic, since it satisfies \(T^2-\alpha^2=0\). Every complex conjugate \(\alpha'\) then satisfies
\[
q^{d/2-1/(2k)}\le|\alpha'|\le q^{d/2+1/(2k)}.
\]
Letting even \(k\) tend to infinity proves middle purity.

For \(i<d\), choose smooth successive hyperplane sections over a finite extension until dimension \(i\). The restriction maps are isomorphisms while \(i<\dim(\text{section})\), and the final one is injective. Thus every degree-\(i\) eigenvalue is a middle eigenvalue on a component of the last section. For \(i>d\), duality pairs it with \(q^d/\alpha\) in degree \(2d-i\), so the lower-degree result gives modulus \(q^{i/2}\).

If the construction required \(\mathbf F_{q^a}\), it proved algebraicity and modulus \(q^{ai/2}\) for \(\alpha^a\). The equation \(T^a-\alpha^a=0\) gives algebraicity of \(\alpha\); for every conjugate \(\alpha'\), its \(a\)-th power is a conjugate of \(\alpha^a\), hence \(|\alpha'|^a=q^{ai/2}\). This descends purity. Split geometric components after a finite extension; direct sums and this same descent handle their permutations over the original field. Zero-dimensional groups have permutation eigenvalues, which are roots of unity; degrees outside the cohomological range are zero.

**Exercise 11.3 (medium — complete-intersection counts).** Establish the bound in Theorem 7.1, explaining the primitive quotient, the case of singular intermediate intersections, and the finite-extension counts.

**Solution.** For fixed multidegrees, the smooth expected-dimension locus in the product of coefficient projective spaces is irreducible. The universal intersection is smooth proper, so all geometric cohomology ranks are constant there. Choose one tuple with smooth successive intersections by Bertini; weak Lefschetz and duality give the projective-space ranks outside degree \(n\). Thus those ranks hold for the given tuple even if its specified intermediate intersections are singular.

The hyperplane powers are nonzero since their top product has nonzero degree \(d_1\cdots d_r\). They span the even groups outside the middle. If \(n\) is even, remove the one-dimensional middle hyperplane line by taking its quotient; if \(n\) is odd, use all \(H^n\). Call its dimension \(b\). Trace additivity for the quotient gives
\[
\#X_0(\mathbf F_{q^a})-\sum_{j=0}^{n}q^{aj}
=(-1)^n\sum_{j=1}^{b}\alpha_j^a.
\]
Theorem 1.1 gives \(|\alpha_j|=q^{n/2}\). The triangle inequality gives \(bq^{an/2}\). For \(n=0\), quotient by the unit line and use \(b=\deg X_0-1\). All groups and traces are étale; no assertion about complex topological Betti numbers is needed.

**Exercise 11.4 (medium — power-family rigidity).** Prove Lemma 3.2, retaining zero entries and multiplicities. Explain why equality only for degrees divisible by a fixed integer would be insufficient.

**Solution.** Choose one admissible positive exponent. Equal powered multisets have the same total cardinality and the same number of zero entries, because a field element has zero positive power exactly when it is zero. Remove their common zeros. If \(a\in A\) has no equal entry in \(B\), equality \(a^d=b^d\) can occur only when \(a/b\) is a root of unity of finite order \(h_b\ge2\) and \(h_b\mid d\). Let \(M\) be a common multiple of these orders and of the finitely many divisibility exclusions in the hypothesis. There are arbitrarily large \(d\equiv1\bmod M\); they meet the hypothesis and avoid every \(h_b\). For them \(a^d\) appears on the left and nowhere on the right, a contradiction.

Thus there is an equal pair \(a=b\). Remove one occurrence on each side; for every admissible exponent, one equal occurrence of its power is removed from each powered multiset, so equality survives with all remaining multiplicities. Induct on cardinality. The counterexample to restricting to multiples is \(A=\{1\}\), \(B=\{-1\}\) in characteristic zero: all even powers agree, but the original families differ. The degree-\(1\bmod M\) argument is what excludes such torsion ambiguity.

**Exercise 11.5 (hard — Chebotarev from covering curves).** Prove Chebotarev for a connected finite étale Galois cover of a smooth curve, allowing a larger field of constants and nonproper curves. Give a uniform error constant and deduce density. Explain its relation to the covering-curve/Artin-character method.

**Solution.** Let the group be \(G\), its geometric subgroup \(H\), and \(e=[G:H]\). Use the geometric generator of \(G/H\); the Frobenius of a degree-\(d\) point lies in its coset \(G_d\).

For the fixed-point calculation use arithmetic Frobenius \(\Phi^d\). If \(g\) is in the compatible arithmetic coset, \(g^{-1}\Phi^d\) preserves all \(e\) components of the completed cover. Twisting descent makes each component a curve over \(\mathbf F_{q^d}\). Curve purity bounds the sum of their counts by \(e(q^d+1)\) with error \(2g_Yq^{d/2}\). Removing the geometric boundary adds error at most \(B_Y\). Thus its open fixed count differs from \(eq^d\) by at most \(2g_Yq^{d/2}+e+B_Y\). Incompatible \(g\) has zero fixed points.

Each base point with Frobenius class \([g]\) contributes exactly \(|Z_G(g)|\) fixed points; points of another class contribute none. Divide by this centralizer order, sum over the desired classes, and replace the arithmetic classes by their inverses. The resulting rational-base-point count \(R_C(d)\) differs from \(e|C\cap G_d|q^d/|G|\) by at most \((2g_Y+e+B_Y)q^{d/2}\).

Subtract points of smaller closed degree:
\[
R_C(d)-dA_C(d)
=\sum_{\substack{m\mid d\\m<d}}m\,
 \#\{x:\deg x=m,\ F_x^{d/m}\in C\}.
\]
This is nonnegative and at most
\[
\sum_{m\le d/2}\#U_0(\mathbf F_{q^m})
\le(2+2g_U)\frac q{q-1}q^{d/2}.
\]
Dividing by \(d\) proves the error estimate with
\[
K=2g_Y+e+B_Y+(2+2g_U)\frac q{q-1}.
\]
For \(z=q^{1-s}\), summing against \(q^{-sd}\) gives an error bounded as \(s\downarrow1\). The main coefficient \(e|C\cap G_d|/|G|\) is periodic with mean \(|C|/|G|\). Its zero-mean remainder has bounded partial sums, hence bounded contribution to \(\sum z^d/d\) by summation by parts. The numerator of the density ratio is therefore
\((|C|/|G|)(-\log(1-z))+O(1)\); the total-point denominator is \(-\log(1-z)+O(1)\). Their ratio tends to \(|C|/|G|\).

The alternative Artin-character calculation expands the class indicator as
\[
1_C(h)=\sum_{\chi\in\widehat G}a_\chi\chi(h),
\qquad
a_\chi=\frac1{|G|}\sum_{g\in C}\overline{\chi(g)}.
\]
The trivial coefficient is \(|C|/|G|\). Characters factoring through \(G/H\) supply the periodic constant-field main term; the other terms come from \(H^1\) of completed covering curves and, for open curves, boundary terms. The curve terms have square-root bounds and the boundary eigenvalues are roots of unity. Intermediate-cover counts use the permutation characters \(\operatorname{Ind}_J^G1\) for \(Y/J\). Our twist count above computes the same class indicator through the regular \(G\)-torsor and centralizers, without requiring an unproved Artin holomorphy assertion. It also retains the representation multiplicities that must accompany a regular-character decomposition.

**Exercise 11.6 (advanced — the exceptional Tate sign).** In the radical case of (5.7), let \(n=2m+1\) and \(\delta_s\in H^n(X_u,\mathbf Q_\ell(m))\) be rational over the chosen field. Determine the target of \(x\mapsto(x,\delta_s)\) for untwisted \(x\in H^n(X_u,\mathbf Q_\ell)\), and the Frobenius eigenvalue on the punctual quotient. Explain why hard Lefschetz cannot be used to remove this case from the proof.

**Solution.** The untwisted pairing has target \(H^{2n}(X_u)=\mathbf Q_\ell(-n)\). Pairing with a class carrying twist \((m)\) changes that target to \(\mathbf Q_\ell(m-n)\). Since
\[
m-n=-m-1=-(n+1)/2=-d/2,
\]
geometric Frobenius acts there as \(q^{n-m}=q^{d/2}\). The map is nonzero and surjective on each one-dimensional punctual target, because the full fibre pairing is nondegenerate and \(\delta_s\ne0\). The two exact sequences (5.7) therefore make \(H^1(D,M)\) a subquotient of the direct sum of these lines, which already satisfies (5.1). Using the opposite twist would give \(q^{-d/2}\) and fail the claimed bound. Hard Lefschetz would constrain the radical, but it is a later consequence of Weil II and was not among the inputs to the proof of Weil I; the exceptional case must be handled by these sequences.

**Exercise 11.7 (medium — the actual weak Lefschetz maps).** For a smooth projective \(d\)-fold and smooth ample divisor \(Y\), derive the exact restriction and Gysin ranges from torsion affine vanishing. Explain the inverse-limit step, and specialize the result to the two maps (5.3)–(5.4).

**Solution.** The ample section's sufficiently high power embeds its nonvanishing locus as a closed subscheme of an affine projective chart, so \(U=X-Y\) is affine. Over \(\Lambda_b\), affine vanishing and finite duality give \(H^t_c(U,\Lambda_b(a))=0\) for \(t<d\). The finite cohomology groups have stabilizing images, so \(\varprojlim^1\) vanishes; derived inverse limit and rationalization give the same compact-support vanishing over \(\mathbf Q_\ell\). In (1.5) both outer terms vanish for \(r<d-1\), and the first vanishes for \(r=d-1\). Transposing restriction and cancelling the common twist \((d)\) gives (1.3): Gysin is an isomorphism onto degree \(2d-r>d+1\) and a surjection onto degree \(d+1\). Set the ambient dimension equal to the pencil fibre dimension \(n\) and \(r=n-1\); this gives the injection \(H^{n-1}(X_u)\hookrightarrow H^{n-1}(Y)\) and surjection \(H^{n-1}(Y)(-1)\twoheadrightarrow H^{n+1}(X_u)\). Neither map uses hard Lefschetz.

**Exercise 11.8 (medium — compact support and ordinary weights).** Compute the four nonzero ordinary and compact-support groups of \(\mathbf G_m\), with their Frobenius eigenvalues, and compare them with the Weil II outlook table.

**Solution.** Localization in \(\mathbf P^1\) has degree-zero restriction \(E\to E\oplus E\), \(c\mapsto(c,c)\). Its cokernel is \(H^1_c(\mathbf G_m,E)=E\), with eigenvalue \(1\); its kernel is zero, so \(H^0_c=0\). The remaining compact group is \(H^2_c=E(-1)\), with eigenvalue \(q\). Connectedness gives \(H^0=E\), with eigenvalue \(1\); curve duality gives \(H^1=E(-1)\), with eigenvalue \(q\), and \(H^2=0\). Thus compact degree one has weight zero and ordinary degree one weight two, while both degree-zero ordinary and degree-two compact groups have their indicated pure weights. The general upper and lower bounds allow these values. The computations themselves follow from localization and duality and do not use Weil II.

## Scope and references

Chebotarev, the unit-family lemmas, vanishing-quotient rationality, the even-dimensional estimate, the tensor-power removal of its error, projective integrality and independence of \(\ell\), and the complete-intersection bound have been proved here from the identified inputs. Proposition 1.2 supplies the complete weak Lefschetz deduction from the exact written affine theorem and the course’s smooth-duality proof. Künneth and the trace formula come from earlier lessons; §§4–5 use the precise pencil inputs and openness theorem of Lesson 9, the fundamental estimate of Lesson 10, and the independently proved curve Riemann hypothesis in Lesson 5. The all-degree product argument gives a second reduction after middle purity. Proposition 6.2 gives the extension to every smooth proper variety through the smooth projective alteration and stable pointed-family proof lessons identified in §6. Its explicit rational pullback-and-trace projector and finite-field descent retain the full theorem, including individual integer polynomials independent of \(\ell\). Bertini and smooth proper base change supply the complete-intersection deformation argument, and the exact owned proper-comparison theorem identifies its topological constant. The classical six-point model is an additional geometric input only for the cubic-surface example. The two further applications and the Weil II results are stated with their separate proof requirements.

- [Deligne, *La conjecture de Weil I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), (1.6)–(1.7) for the theorem; remark (5.12), printed p.294, for the qualified hypersurface shortcut; §6, pp.294–298, especially (6.2), (6.6)–(6.8), and (6.11)–(6.13), for rationality; §7, pp.299–301, for the even-dimensional induction and tensor powers; (8.1)–(8.4), pp.301–303, for applications. The punctual Tate sign in (7.1.5), p.300, is corrected in §5 and Exercise 11.6 by its defining pairing.
- [Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day*](https://arxiv.org/abs/1509.00797), “Proof of the Riemann hypothesis for hypersurfaces of odd degree,” “The main lemma (restricted form),” “A reduction,” “Completion of the proof,” and “Beyond the Riemann hypothesis over finite fields.” Despite that heading's “odd degree,” its numerator formula and skew pairing require **odd dimension**, as in Deligne (5.12). The lower exponent in its completion passage is \(d/2-1/2\), as follows from duality, rather than the printed \(d-1/2\). Vanishing-quotient rationality requires §4, not just the induction hypothesis for full fibre cohomology.
- [Stacks, The Trace Formula](https://stacks.math.columbia.edu/tag/0F5Q), especially [03VH](https://stacks.math.columbia.edu/tag/03VH), the stated Weil II theorem, and [03W3](https://stacks.math.columbia.edu/tag/03W3), the Chebotarev sketch with its warning about the coefficient. Section 2 supplies the constant-field term and error explicitly. The regular representation has each irreducible with its dimension as multiplicity; for an actual rank-\(r\) geometrically nontrivial irreducible local system on a proper unramified curve, the \(H^1\)-dimension is \((2g-2)r\).
- [Deligne, *La conjecture de Weil II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), (3.3.1), (3.3.4)–(3.3.10), (4.1.1) and (6.2.13), for the exact smooth-proper scope, mixed-weight bounds and the constant and pure-lisse forms of hard Lefschetz. These later results have distinct proofs and are not inputs to the proof of Weil I.
- [A. J. de Jong, *Smoothness, semi-stability and alterations*](https://www.numdam.org/item/PMIHES_1996__83__51_0/), Theorem 4.1 and Remark 4.2, is the primary comparison for the geometric theorem used in Proposition 6.2. The course proof homes are Smooth projective alterations, §§1–8, and Stable pointed-family extension, Theorem S.9. They supply the projective source, separable generic field and finite-algebraic descent; §6 above proves the actual rational cohomological splitting.
- [Dolgachev and Duncan, *Automorphisms of cubic surfaces in positive characteristic*](https://arxiv.org/abs/1712.01167), §2, pp.8–9, for the classical six-point blow-up model in arbitrary characteristic.
- [Milne, *Lectures on Étale Cohomology*, version 2.21](https://www.jmilne.org/math/CourseNotes/LEC.pdf), §§26–28 and 33, printed pp.151–162 and 193–196. Section 33 expressly omits vanishing-quotient rationality and the zero-cycle case; §§3–5 here prove both. Its footnote on p.162 credits A. Mellit for the further product reduction, proved in (6.1a)–(6.1b).
- [*Cohomological dimension and the Künneth formula*, §§2–5, Theorem 5.1](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula), for the complete affine proof; Smooth traces, duality and Gysin maps, for the coefficient-compatible smooth pairing and actual counits. Proposition 1.2 proves the needed weak Lefschetz statement here.
- Lesson 5, Theorem 5.3; Lesson 9; Lesson 10; and Lesson 8, for the precise course inputs used above.

The Stacks comparisons were also read in [AI Integrated Stacks Project, English, *The Trace Formula*](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-theorem-weil-II), at source revision `565b10e987aba5969b21145a0833f42d69f96790`, and its [affine cohomological-dimension proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-proposition-cd-affine). The degree-\(i\) weight exponent is \(i/2\), as in Theorem 1.1. The Chebotarev comparison retains constant fields, boundary errors and regular-representation multiplicities as in §2. Human Stacks authors retain their credit and GFDL terms; the AI-integrated additions and corrections are not independent verification of this lesson.

The exposition, proofs, examples and exercise solutions are independently authored. Linked sources retain their own rights.

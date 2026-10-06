# The ℓ-adic Tate module of an elliptic curve

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Point counts on an elliptic curve become traces of a two-dimensional representation. The determinant comes from a pairing; the trace comes from the kernel of a geometric endomorphism. The positivity of its degree then bounds the point count. This chapter develops those three connections, so that the passage from geometry to a Galois representation has a concrete meaning.

We assume Frobenius elements and determination by traces. The algebraic foundations are the existing programme lesson *Abelian varieties*: Lemma 9.11 proves curve Riemann–Roch and duality, Example 9.12 constructs a pointed Weierstrass cubic in every characteristic, Lemma 9.0a and Theorem 9.0 construct its group law, and Proposition 6.3 proves finite translation quotients. Section 1 gives the elliptic arguments needed here, including algebraic construction of the dual isogeny and every property of the pairing used below. These proofs apply in positive characteristic. Freely accessible author notes and the Stacks Project, listed below, are source material for comparison; none takes the place of a proof. The Tate module is covariant, and Frobenius is arithmetic. In particular its cyclotomic determinant at a good prime is \(p\), not \(p^{-1}\).

## 1. Algebraic geometry before the representation

An elliptic curve over \(K\) is a smooth projective geometrically integral curve of genus one with a specified \(K\)-point \(O\). Genus here means \(\dim_K H^1(E,\mathcal O_E)\). In the arguments about geometric points we extend scalars to \(\bar K\); descent of the constructions will be stated separately.

### 1.1. The group law and divisor classes

The earlier curve theorem cited in the introduction gives \(\Omega_E^1\simeq\mathcal O_E\) and
\[
h^0(E,L)=\deg L,\qquad H^1(E,L)=0\quad(\deg L>0).
\]
Indeed duality identifies the latter group with the sections of \(L^{-1}\), which has negative degree, and Riemann–Roch then gives the former. The same calculation after removing a length-two subscheme shows that \(3O\) separates points and tangent vectors. Thus its three sections embed the curve as a smooth plane cubic. Choosing functions with exact pole orders two and three gives
\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,
\qquad O=[0:1:0].
\tag{G1}
\]
For completeness, the seven functions \(1,x,y,x^2,xy,x^3,y^2\) lie in the six-dimensional space \(H^0(6O)\); their relation has nonzero \(x^3\) and \(y^2\) coefficients, since all smaller pole orders are distinct. Rescaling gives (G1). The line at infinity cuts out \(3O\). This construction never divides by two or three.

The chord construction of the earlier Theorem 9.0 has the following algebraic explanation. The line through \(P,Q\), with the tangent used when \(P=Q\), meets the cubic in a third point \(R\), counted with multiplicity. Define \(P+Q\) as the third point of the line through \(R,O\). The quotient of these two line equations has divisor
\[
(P)+(Q)-(P+Q)-(O).
\tag{G2}
\]
These operations are morphisms, including at tangents. In the universal family over \(E^2\), the three coefficients of a secant generate the ideal of the diagonal. That diagonal is Cartier; dividing by its local equation gives the tangent on the diagonal and a regular map to the dual projective plane. Remove the two graph divisors from the line's intersection divisor. In an étale curve parameter their equations are \(t-u,t-v\), and divisibility by each implies divisibility by their product, also on the diagonal. The residual divisor has fibre length one. Its local equation consequently has unit derivative in the curve parameter, so it is étale of degree one over \(E^2\), hence the graph of a morphism. Reflection through \(O\) is constructed in the same way. This is the family argument in the earlier theorem; it applies in characteristics two and three as well.

The map
\[
j:E(\bar K)\longrightarrow\operatorname{Pic}^0(E_{\bar K}),
\qquad P\longmapsto[(P)-(O)]
\tag{G3}
\]
is bijective. A degree-zero divisor class, after adding \(O\), has degree one, hence has a unique effective representative by the displayed dimension formula. This gives surjectivity and uniqueness. Equivalently, two distinct points cannot be linearly equivalent: their quotient function would give a degree-one map to \(\mathbf P^1\), whereas a smooth genus-one curve has a nonzero regular differential and \(\mathbf P^1\) has none. Equation (G2) says that \(j\) carries addition to addition of classes. Associativity, commutativity, identity and inverse follow by injectivity. Equality on geometric points proves equality of the resulting morphisms, because their sources \(E,E^2,E^3\) are geometrically reduced and their target is separated. This proves the group identities as scheme identities, so they persist under every base change.

In particular, over \(\bar K\) a divisor \(\sum n_P(P)\) is principal exactly when
\[
\sum n_P=0\quad\text{and}\quad\sum n_PP=O.
\tag{G4}
\]

### 1.2. Degree and multiplication in every characteristic

A nonzero group homomorphism \(u:E\to E'\) is nonconstant: a constant homomorphism has value \(O\). A nonconstant map of smooth projective integral curves has finite fibres and is finite and surjective. Here we use the direct projective-curve proof in the earlier Lemma 9.0a: choose a hyperplane missing a finite target fibre and remove the closed image of its intersection with the source. The inverse image of the remaining affine target neighbourhood is affine; the proof there shows, using valuation rings, that its coordinate algebra is integral and of finite type over the target, hence finite. That argument applies to any projective target curve, since it only uses these affine neighbourhoods. At a target DVR the finite module is torsion-free, hence free. Consequently the map is finite flat, and
\[
\deg u=[K(E):u^*K(E')]
=\operatorname{length}u^{-1}(O).
\tag{G5}
\]
Translation identifies every geometric fibre with the schematic kernel. The degree is positive, degrees multiply under composition by the tower formula, and the zero homomorphism has degree zero. Pulling back the degree-one bundle \(\mathcal O_{E'}(O)\) has degree \(\deg u\); this includes nonreduced fibres and inseparable maps.

**Lemma 1.1 (multiplication degree).** For every integer \(m\ne0\), \([m]\) is an isogeny of degree \(m^2\), in every characteristic.

**Proof.** Put \(L=\mathcal O_E(O)\). On \(E\times E\), the rational function \(x(P)-x(Q)\) from (G1) has divisor
\[
\Delta+\Delta^- -2(E\times\{O\})-2(\{O\}\times E),
\]
where \(\Delta\) is \(P=Q\) and \(\Delta^-\) is \(P=-Q\). Its poles have order two in each variable. Generically its zeros are precisely the two points with a given \(x\)-coordinate, and each has order one. Inversion is \((x,y)\mapsto(x,-y-a_1x-a_3)\); it is nontrivial even in characteristic two. If both \(a_1,a_3\) vanished there, the affine equation would have a singular geometric point, since its \(y\)-derivative would vanish identically. Thus the generic quadratic \(x\)-map is separable, justifying the two multiplicities in all characteristics. Divisors are determined in codimension one, so their possible intersections cause no extra term.

In line bundles this identity is
\[
s^*L\otimes d^*L\simeq p_1^*L^{\otimes2}\otimes p_2^*L^{\otimes2},
\quad s(P,Q)=P+Q, d(P,Q)=P-Q.
\tag{G6}
\]
Unlike substituting into the rational function, pulling back this bundle identity is valid even for a map contained in a diagonal. Pull it back along \(P\mapsto([a]P,[b]P)\) and take degrees. With \(d_m=\deg([m]^*L)\), including \(d_0=0\), it gives
\[
d_{a+b}+d_{a-b}=2d_a+2d_b.
\]
Now \(d_1=1\), inversion preserves \(L\), and the recurrence with \(b=1\) gives \(d_m=m^2\) by induction for all integers. Its positivity for \(m\ne0\) excludes a constant map. Formula (G5) identifies this bundle degree with the isogeny degree. \(\square\)

### 1.3. Separability and torsion

For a group homomorphism, translation identifies its differential at every geometric point with its differential at \(O\). A finite map between smooth curves is separable exactly when this differential is nonzero: at function fields a finite extension has vanishing relative differentials exactly when it is separable, and a nonzero differential on curves detects that condition. A separable isogeny is therefore unramified everywhere. Its finite flatness makes it étale. Its geometric kernel is then reduced, so (G5) gives
\[
\#\ker u(\bar K)=\deg u\quad(u\text{ separable}).
\tag{G7}
\]
These equivalences are also the dimension-one case of the earlier *Abelian varieties*, Theorem 6.8. For multiplication the tangent group law gives \(d[m]=m\,\mathrm{id}\), by induction and inversion.

**Lemma 1.2 (prime-to-characteristic torsion).** If \(m>0\) is invertible in \(K\), then
\[
E[m](\bar K)\simeq(\mathbb Z/m\mathbb Z)^2.
\]
If \(\ell\ne\operatorname{char}K\), multiplication by \(\ell\) maps \(E[\ell^{a+1}]\) onto \(E[\ell^a]\).

**Proof.** Lemma 1.1 and the differential calculation make \([m]\) finite étale of degree \(m^2\). Thus its kernel has exactly \(m^2\) geometric points, all separable over \(K\). For \(m=\ell^a\), write the finite abelian group as \(\bigoplus_{i=1}^r\mathbb Z/\ell^{b_i}\), with \(1\le b_i\le a\). Its subgroup killed by \(\ell\) is \(E[\ell]\), of size \(\ell^2\), so \(r=2\). Its total size gives \(b_1+b_2=2a\); therefore both exponents are \(a\). The primary decomposition gives the general statement for \(m\). Finally, surjectivity of \([\ell]\) gives a point \(Q\) with \(\ell Q=P\) for any \(P\in E[\ell^a]\); it satisfies \(\ell^{a+1}Q=O\). \(\square\)

### 1.4. Dual isogenies, including inseparable ones

**Lemma 1.3 (the dual).** An isogeny \(u:E\to E'\), of degree \(d\), has a unique dual \(\widehat u:E'\to E\), defined over the same field, such that
\[
\widehat u u=[d],\qquad u\widehat u=[d].
\tag{G8}
\]
On degree-zero divisor classes it is pullback under (G3), and \(\widehat{[m]}=[m]\).

**Proof.** We construct a morphism realizing pullback of classes. Put \(F=K(E')\), and let \(Q\in E'(F)\) be its generic point. The divisor \(D=u^*((Q)-(O))\) on \(E_F\) has degree zero. Riemann–Roch makes \(D+(O)\) linearly equivalent to a unique effective degree-one divisor; that divisor is a point \(R\in E(F)\). Thus \(R\) gives a rational map \(E'\dashrightarrow E\) over \(K\). It extends to a morphism \(\widehat u:E'\to E\). Indeed embed \(E\) in projective space. At any closed point of \(E'\), its smooth local ring is a DVR; scale the rational homogeneous coordinates so that they all lie in this ring and one is a unit. The equations of \(E\) continue to hold, giving the extension there. The finitely many coordinate expressions spread it to a neighbourhood, and separatedness makes these extensions agree. This proves the curve extension directly.

Its value at every geometric point still represents the pulled-back class. To check this specialization, on the regular surface \(E\times E'\) take the relative divisor \(D\) obtained by pulling back the diagonal under \(u\times\mathrm{id}\), minus the fixed fibre divisor \(u^*(O)\times E'\). The line bundle of \(D+\{O\}\times E'-\Gamma_{\widehat u}\) is trivial on the generic fibre over \(E'\). A rational trivializing section consequently has a divisor supported on vertical prime divisors. Each such prime divisor is an entire fibre \(E\times\{Q_0\}\), since the curve is geometrically integral; hence the bundle is pulled back from a divisor on \(E'\). Its restriction to every fibre is trivial. This proves the class assertion on every fibre, including after extension to \(\bar K\). Pullback adds divisor classes, so (G3) makes \(\widehat u\) a group homomorphism and gives \(\widehat u(O)=O\).

Now work over \(\bar K\) and write the kernel divisor as \(\sum_R e_R(R)\). Its length is \(\sum_R e_R=d\), and the fibre at \(u(P)\) is its translate \(\sum_R e_R(P+R)\). Thus the sum of the points in the difference of the two fibres is
\[
\sum_R e_R(P+R)-\sum_R e_RR=dP.
\]
Equations (G3)–(G4) give \(\widehat u u(P)=[d]P\). This calculation keeps the fibre multiplicities, so it includes inseparable isogenies. Equality on geometric points is equality of morphisms as above. Since \(u\) is surjective,
\(u\widehat u u=u[d]=[d]u\) gives the other identity. The first makes \(\widehat u\) nonzero and hence an isogeny. It also gives uniqueness by cancelling the surjective \(u\). For \(u=[m]\), Lemma 1.1 says \(d=m^2\), and \([m][m]=[m^2]\); uniqueness gives the last assertion. The construction and the unique extension were over \(K\), so no descent of a chosen geometric kernel point is required. \(\square\)

### 1.5. Constructing and proving the pairing

Fix \(m>0\) prime to \(\operatorname{char}K\), and first work over \(\bar K\). For \(Q\in E[m]\), choose a degree-zero divisor \(D_Q\) in its class (G3). By Lemma 1.3 the class of \([m]^*D_Q\) is \([m]Q=O\), so there is a rational function \(g_Q\) with
\[
\operatorname{div}g_Q=[m]^*D_Q.
\]
For \(P\in E[m]\), translation by \(P\) preserves this divisor. The quotient \(g_Q(X)/g_Q(X+P)\) has no zeros or poles and is therefore constant. Define
\[
e_m(P,Q)=\frac{g_Q(X)}{g_Q(X+P)}.
\tag{G9}
\]
The displayed choice is the reciprocal-translation convention in the freely accessible [Milne notes, I §13, pp.57–58](https://www.jmilne.org/math/CourseNotes/AV.pdf). Reversing all pairing values would give the same determinant statements.

**Lemma 1.4 (pairing properties).** Formula (G9) is independent of all choices and gives a perfect, bilinear, alternating and Galois-equivariant pairing
\(E[m]\times E[m]\to\mu_m\). For \(u:E\to E'\),
\[
e_m^{E'}(uP,Q)=e_m^E(P,\widehat uQ).
\tag{1}
\]
For \(r,n\) prime to the characteristic and \(P,Q\in E[rn]\),
\[
e_{rn}(P,Q)^r=e_n(rP,rQ).
\tag{G10}
\]

**Proof.** A constant multiplier of \(g_Q\) cancels in (G9). Replacing \(D_Q\) by \(D_Q+\operatorname{div}h\) replaces \(g_Q\), up to a scalar, by \(g_Q(h\circ[m])\). Its extra factor is invariant under translation by \(P\), so it cancels too. The value is consequently independent of the representative. Translating repeatedly proves additivity in \(P\); translating \(m\) times proves its value has \(m\)-th power one. Since \(D_{Q+Q'}\) can be represented by \(D_Q+D_{Q'}\), the function \(g_Qg_{Q'}\) proves additivity in \(Q\). These arguments include the zero point.

For nondegeneracy, suppose \(e_m(P,Q)=1\) for every \(P\in E[m]\). Then \(g_Q\) is invariant under all deck translations of \([m]\). They are \(m^2\) distinct automorphisms, and \([m]\) has degree \(m^2\). Put \(F=\bar K(E)\) and \(F_0=[m]^*F\). Every invariant element \(g\) has these same \(m^2\) automorphisms fixing \(F_0(g)\). A finite extension has at most its degree many embeddings: in a tower of simple generators each next image is a root of its minimal polynomial, so the root bounds multiply to the tower degree. Hence \([F:F_0(g)]\ge m^2=[F:F_0]\), forcing \(g\in F_0\). Applied to \(g_Q\), this gives \(g_Q=h\circ[m]\). Now
\([m]^*D_Q=[m]^*\operatorname{div}h\). Pullback of divisors is injective, since every target point has a nonempty fibre and positive multiplicities. Hence \(D_Q\) is principal and \(Q=O\). This gives an injection of the second factor into \(\operatorname{Hom}(E[m],\mu_m)\). Both groups have size \(m^2\), by Lemma 1.2, so the injection is an isomorphism: the pairing is perfect.

We prove actual alternation, including even \(m\), rather than infer it from skew symmetry. Take \(P\) of order \(s\mid m\), and quotient by its cyclic subgroup:
\[
\beta:E\longrightarrow B=E/\langle P\rangle.
\]
The earlier finite-translation-quotient Proposition 6.3 constructs the smooth proper group curve \(B\), its group law and the finite flat map \(\beta\) of degree \(s\). The map is étale: its base change along itself is the projection \(\langle P\rangle\times E\to E\), whose relative differentials vanish, since \(\langle P\rangle\) is a constant finite group. Faithful flatness therefore makes \(\Omega_{E/B}=0\); the finite flat differential criterion gives étaleness. It has genus one: \(\beta^*\Omega_B^1\simeq\Omega_E^1\), so \(s\deg\Omega_B^1=0\); the earlier curve duality formula \(\deg\Omega_B^1=2g_B-2\) gives \(g_B=1\). Its quotient group law agrees with the pointed cubic law: Corollary 2.3 of that lesson makes the identity map between these two pointed abelian varieties a homomorphism. Multiplication factors as \([m]=v\beta\), where \(v:B\to E\) is separable of degree \(m^2/s\); separability follows either from the tower of function fields or from the nonzero differential of the composite. Choose \(R\) with \(mR=P\). The two fibres of \(v\) over \(P,O\) are respectively \(\beta R+\ker v\) and \(\ker v\). Thus the point sum of
\(D=v^*((P)-(O))\), on \(B\), is
\[
\frac{m^2}{s}\beta R
=\beta\left(\frac ms P\right)=O.
\]
It also has degree zero. Formula (G4) on the elliptic curve \(B\) makes it principal, say \(D=\operatorname{div}h\). Therefore
\(\operatorname{div}g_P=\beta^*D=\operatorname{div}(h\circ\beta)\). Up to a scalar \(g_P=h\circ\beta\), which is invariant under translation by \(P\). Formula (G9) gives \(e_m(P,P)=1\). Bilinearity applied to \(P+Q\) now gives \(e_m(P,Q)e_m(Q,P)=1\), and perfection holds in both variables. This cyclic-quotient proof uses no reciprocity theorem as an unstated input.

For (1), represent \(Q\) by \(D\) on \(E'\). Pullback represents \(\widehat uQ\), and \(g_Q\circ u\) has divisor
\(u^*[m]^*D=[m]^*u^*D\). Translating \(X\) by \(P\) in this function is translating \(uX\) by \(uP\). Substitution into (G9) proves (1), without any separability assumption on \(u\).

For compatibility, if \(P\in E[rn]\) and \(Q\in E[n]\), use \(g_Q\circ[r]\) at level \(rn\), where \(g_Q\) is chosen at level \(n\). Its divisor is \([rn]^*D_Q\). Formula (G9) gives
\(e_{rn}(P,Q)=e_n(rP,Q)\). Replace \(Q\) by \(rQ\) and use bilinearity to obtain (G10). In particular
\[
e_{\ell^{a+1}}(P,Q)^\ell
=e_{\ell^a}(\ell P,\ell Q),
\]
which is exactly the inverse-limit compatibility required later. Finally a field automorphism sends a function and its divisor to their conjugates and respects translation. Applying it to (G9) gives \(e_m(\sigma P,\sigma Q)=\sigma(e_m(P,Q))\). The torsion points lie in the separable closure by Lemma 1.2, so this is the asserted Galois action over an arbitrary field. \(\square\)

### 1.6. Frobenius and rational points

**Lemma 1.5 (Frobenius morphism degree).** On an elliptic curve over \(\mathbb F_q\), the coordinate map \(\varphi:(x,y)\mapsto(x^q,y^q)\) is a purely inseparable isogeny of degree \(q\). The map \(1-\varphi\) is separable and
\[
\deg(1-\varphi)=\#E(\mathbb F_q).
\tag{G11}
\]

**Proof.** Frobenius respects every polynomial group-law identity over \(\mathbb F_q\), hence is a homomorphism. Put \(F=\overline{\mathbb F}_q(E)\). Smoothness provides a separating parameter \(t\), so \(F\) is a finite separable extension of \(\overline{\mathbb F}_q(t)\), of some degree \(h\). Frobenius carries a basis to a basis and gives
\([F^q:\overline{\mathbb F}_q(t^q)]=h\), whereas
\([\overline{\mathbb F}_q(t):\overline{\mathbb F}_q(t^q)]=q\). The tower formula yields \([F:F^q]=q\). Because the constants are perfect, the image of \(\varphi^*\) is \(F^q\). Its extension is purely inseparable: every \(z\in F\) has \(z^q\in F^q\). Thus the degree is \(q\), and its geometric fibres have one point. The separating parameter used here is supplied by the smooth curve's étale-coordinate chart; the earlier Kähler-differential and smoothness lessons prove that coordinate criterion.

The differential of \(\varphi\) is zero, so the differential of \(1-\varphi\) is the identity. It is consequently a nonzero separable isogeny. Its geometric kernel is exactly the points whose coordinates are fixed by the \(q\)-power map, namely \(E(\mathbb F_q)\). Formula (G7) proves (G11). \(\square\)

The smooth proper model and finite étale lifting needed for good reduction will be proved in Section 3 before their arithmetic application. The preceding arguments already supply every elliptic-curve input for the two determinant theorems.

## 2. A representation from all ℓ-power torsion

Assume \(\ell\ne\operatorname{char}K\). Define
\[
 T_\ell E=\varprojlim_a E[\ell^a](\bar K),
 \qquad V_\ell E=T_\ell E\otimes_{\mathbb Z_\ell}\mathbb Q_\ell,
\]
with transition map multiplication by \(\ell\). Choosing a basis at level \(\ell\), lift it successively to bases at every higher level. A lift is a basis because its reduction is a basis and each torsion group is free of rank two over \(\mathbb Z/\ell^a\mathbb Z\). Thus
\[
 T_\ell E\simeq\mathbb Z_\ell^2,
 \qquad V_\ell E\simeq\mathbb Q_\ell^2.
\]
Galois acts on every torsion group and respects the transition maps. The resulting homomorphism
\[
 \rho_{E,\ell}:G_K\longrightarrow\operatorname{GL}(T_\ell E)
\]
is continuous: prescribing the matrix modulo \(\ell^a\) prescribes its action on a finite set of algebraic points and hence is an open condition.

The compatible Weil pairings give a perfect alternating pairing
\[
 T_\ell E\times T_\ell E\longrightarrow\mathbb Z_\ell(1).
 \tag{2}
\]
Here \(\mathbb Z_\ell(1)=\varprojlim_a\mu_{\ell^a}\), with the Galois action of the cyclotomic character.

**Theorem 2.1 (cyclotomic determinant).** For an elliptic curve over any field \(K\), with \(\ell\ne\operatorname{char}K\),
\[
 \det\rho_{E,\ell}=\chi_\ell|_{G_K}.
\]

**Proof.** A perfect alternating pairing on a rank-two module identifies its exterior square with the target of the pairing. Thus (2) identifies \(\bigwedge^2T_\ell E\) with \(\mathbb Z_\ell(1)\). On the exterior square a matrix acts by its determinant; on the target Galois acts by \(\chi_\ell\). Equivariance gives their equality. Equivalently, in a basis \(P,Q\) modulo \(\ell^a\), bilinearity and alternation give \(e_{\ell^a}(gP,gQ)=e_{\ell^a}(P,Q)^{\det g}\), whereas Galois equivariance gives exponent \(\chi_\ell(g)\). Perfection makes the pairing value primitive, so the exponents agree modulo \(\ell^a\) for every \(a\). \(\square\)

The same argument applied to an endomorphism gives a second interpretation of determinant.

**Theorem 2.2 (degree as determinant).** For every endomorphism \(\alpha\) of an elliptic curve and every \(\ell\) different from the field characteristic,
\[
 \det(\alpha\mid T_\ell E)=\deg\alpha
 \quad\text{in }\mathbb Z_\ell.
 \tag{3}
\]

**Proof.** The zero endomorphism satisfies (3). Otherwise it is an isogeny. Substitute \(Q=\alpha Q'\) into (1). The dual-isogeny identity gives
\[
 e_{\ell^a}(\alpha P,\alpha Q')
 =e_{\ell^a}(P,\widehat\alpha\alpha Q')
 =e_{\ell^a}(P,Q')^{\deg\alpha}.
\]
In a torsion basis the left side is also \(e_{\ell^a}(P,Q')^{\det\alpha}\). Its primitive order gives \(\det\alpha\equiv\deg\alpha\pmod{\ell^a}\) for every \(a\). Taking the inverse limit proves equality, including for an inseparable isogeny. \(\square\)

The action of \(\operatorname{End}(E)\) on \(T_\ell E\) is faithful. Indeed an endomorphism with zero action kills every \(E[\ell^a]\), since the projections from the inverse limit are surjective. A nonzero endomorphism is an isogeny and has a finite geometric kernel, which cannot contain these groups of unbounded size. Consequently a polynomial identity on the Tate module is also an identity of elliptic-curve endomorphisms.

## 3. Good reduction makes Frobenius visible

Let \(K_v\) be a complete discretely valued field with residue field \(\mathbb F_q\) of characteristic \(p\), and let \(E/K_v\) have good reduction \(\widetilde E\). Assume \(\ell\ne p\).

Good reduction means that \(E\) extends to a smooth proper group curve \(\mathcal E\) over the valuation ring \(R\), with geometrically integral genus-one fibres and its origin section. We need the following relative and local arguments.

**Relative finiteness lemma.** A proper étale morphism with Noetherian target is finite étale.

**Proof.** We give the proof needed for our model, without importing the general proper quasi-finite theorem. At a point \(y\) of the target, put \(A=\mathcal O_{Y,y}\), choose a separable closure of its residue field \(k\), and form \(H\), the filtered colimit of marked affine étale neighbourhoods. A marking embeds the selected point's residue field in \(k^{\mathrm{sep}}\). Products give common refinements, and the open diagonal of an étale map equalizes two arrows with the same marking. Thus the system is filtered. Principal refinements invert every element outside the selected prime. Isolating its factor in the finite étale closed fibre shows that \(H\) is local, with maximal ideal \(\mathfrak m_AH\). Its residue field is \(k^{\mathrm{sep}}\): any finite separable residue extension occurs by lifting its monic defining polynomial and inverting its derivative. These are the explicit constructions in the earlier *Étale neighbourhoods, henselization and quasi-finite morphisms*, Sections 1 and 3.

Every point of the closed fibre of an étale \(H\)-scheme has a section through it. Indeed choose an affine chart through that point. Its finite presentation and its invertible square Jacobian descend to an étale stage \(B\) of the colimit. The chart, as an étale \(B\)-algebra, is itself an allowed marked étale \(A\)-stage. Its canonical map to \(H\) gives the section. The residue marking exists because \(k^{\mathrm{sep}}\) has no proper finite separable extensions. This proves the section assertion directly from the colimit; it does not use a general quasi-finite factorization theorem.

Apply this to the proper étale map after base change to \(H\). Its closed fibre has finitely many points, since it is quasi-compact and étale over a field. Their sections are open immersions because the map is étale, and closed immersions because it is separated. Distinct sections are disjoint: their equalizer is open and closed in the connected local spectrum and misses its closed point. The complement of their union is therefore proper over \(H\). Its closed image misses the closed point, so is empty, since every nonempty closed subset of a local spectrum contains that point. The base change is a finite disjoint union of copies of \(\operatorname{Spec}H\).

This splitting holds over an étale neighbourhood \(U\to Y\) of \(y\), rather than only over the colimit. The finitely many sections descend to one common stage: their affine coordinate images and their finitely many relations involve only finitely many coefficients. These are finite presentations because the target is Noetherian. Remove the closed equalizers of distinct descended sections. Their images are then disjoint open-and-closed sections. The complement is proper; remove its closed image, which misses the selected point. After this shrinking the entire source is the disjoint union of those sections over \(U\).

Finally descend finiteness from this étale cover. The fully proved module and affine descent in the opening section of the earlier *Quotients and torsors* makes the original morphism affine locally on the target. Its coordinate algebra \(C\) becomes finite over a faithfully flat coordinate extension \(B/A\). Choose finitely many elements of \(C\) spanning after that extension by collecting the coefficients of finite \(B\)-module generators. Their \(A\)-span \(N\) has \((C/N)\otimes_AB=0\), so faithful flatness gives \(C=N\). Thus \(C\) is finite over \(A\). Affine target opens have finite étale covers of this kind, by quasi-compactness and openness of étale maps. This proves finiteness everywhere. Étaleness was already assumed. \(\square\)

**Lemma 3.0 (étale multiplication and lifting).** If \(m\) is a unit of \(R\), then \([m]:\mathcal E\to\mathcal E\) and its kernel are finite étale, of degree and rank \(m^2\), respectively. Over the henselian unramified valuation ring with residue field \(\overline{\mathbb F}_q\), that kernel is a disjoint union of \(m^2\) sections. Its generic and special points correspond bijectively.

**Proof.** The tangent group law over \(R\) gives \(d[m]=m\,\mathrm{id}\) at the origin; translations give this at every point. Both source and target are smooth of relative dimension one. In local smooth coordinates their relative Jacobian is therefore invertible, so the map is étale. The coordinate criterion is proved in the programme's *Smooth morphisms*, Theorem 4.1, together with *Étale morphisms and their local structure*, Sections 1–2. One can check the lifting criterion directly: smoothness first lifts a source point across a square-zero ideal; the resulting error in its image is a tangent vector, and the inverse differential corrects it uniquely. This proves formal étaleness, and the finite-presentation criterion in those earlier lessons makes it étale. The map is proper: its graph is closed and the projection is a base change of the proper structure map. The preceding relative finiteness lemma makes it finite. A finite étale map is locally free; its rank, calculated on either elliptic fibre by Lemma 1.1, is \(m^2\). The target is connected: any nonempty open-and-closed component meets the generic fibre because a smooth map is open, and that fibre is connected. Thus there is one rank. Pulling back along the origin gives the asserted kernel.

Here is the lifting argument in this local-field setting, including its algebra. For every finite extension of \(\mathbb F_q\), lift a monic separable irreducible defining polynomial to \(R[T]\). Its quotient is a finite free complete local \(R\)-algebra whose reduction is that field; its derivative is a unit. Its maximal ideal is generated by the original uniformizer, and division by successive powers of that uniformizer shows it is a DVR. Its fraction field is the corresponding unramified extension. Compatible such rings inside an algebraic closure have a union \(R^{\mathrm{nr}}\) with residue field \(\overline{\mathbb F}_q\). The unramified extension and residue-field correspondence is also proved in the earlier *Unramified and totally ramified extensions*, Theorem 2.1.

This union is henselian. A polynomial, a simple residue root and their finitely many coefficients belong to some finite stage after enlarging its residue field. There Newton iteration
\[
b_{j+1}=b_j-\frac{f(b_j)}{f'(b_j)}
\]
converges in that complete DVR: \(f'(b_j)\) remains a unit, and Taylor's formula shows the error valuation at least doubles at each step. Two roots with the same residue are equal, since their difference times a unit is zero by the same Taylor identity. Thus every simple residue root lifts uniquely to \(R^{\mathrm{nr}}\).

Let \(B\) be the coordinate algebra of the kernel over \(R^{\mathrm{nr}}\). It is finite locally free, hence free over this local ring, and its reduction is \(\overline{\mathbb F}_q^{\,m^2}\), since a finite étale algebra over an algebraically closed field is a product of that field. Choose \(b\in B\) with distinct coordinates in this reduction; the residue field is infinite. Its multiplication characteristic polynomial \(F(T)\) reduces to a product of \(m^2\) distinct linear factors. Hensel's argument lifts these to roots \(a_i\in R^{\mathrm{nr}}\), with all \(a_i-a_j\) units, and polynomial division gives \(F=\prod_i(T-a_i)\). Cayley–Hamilton and the interpolation polynomials
\[
e_i=\prod_{j\ne i}\frac{b-a_j}{a_i-a_j}
\]
give orthogonal idempotents with sum one. Consequently \(B=\prod_i e_iB\). Each summand is a finite projective module of residue dimension one, hence free of rank one by Nakayama. Its unit generates it, so its algebra is the base ring itself. We obtain \(B\simeq(R^{\mathrm{nr}})^{m^2}\). This proves the section decomposition and the point bijection, rather than importing them from an external reference. The argument is the special case of the freely accessible Stacks lemma [Tag 04GK](https://stacks.math.columbia.edu/tag/04GK) needed here. \(\square\)

**Theorem 3.1 (unramified torsion).** Reduction identifies the prime-to-\(p\) torsion groups equivariantly:
\
 E[\ell^a\simeq
 \widetilde E[\ell^a](\overline{\mathbb F}_q).
\]
Inertia acts trivially on \(T_\ell E\), and arithmetic Frobenius acts through the endomorphism \(\varphi:(x,y)\mapsto(x^q,y^q)\) of \(\widetilde E\).

**Proof.** Apply Lemma 3.0 with \(m=\ell^a\). Its \(\ell^{2a}\) sections over \(R^{\mathrm{nr}}\) give all generic torsion points: they already have the number \(\ell^{2a}\) proved in Lemma 1.2. Their generic points are defined over the maximal unramified extension, so inertia fixes every one of them. Reduction bijects them with the special-fibre torsion points and respects addition and the residue-field Galois action. On that residue field arithmetic Frobenius is the \(q\)-power map, acting on coordinates as \(\varphi\). The identifications commute with multiplication by \(\ell\), so they pass to the Tate module. \(\square\)

To compute the trace we work entirely on the special fibre. Lemma 1.5 proves that its \(q\)-power Frobenius has degree \(q\), and that \(1-\varphi\) is separable with the rational points as its kernel. Thus
\[
 \#\widetilde E(\mathbb F_q)=\deg(1-\varphi).
 \tag{4}
\]

**Theorem 3.2 (Frobenius polynomial).** Put \(a_q=q+1-\#\widetilde E(\mathbb F_q)\). Then
\[
 \det(X-\varphi\mid V_\ell\widetilde E)=X^2-a_qX+q.
 \tag{5}
\]
For \(E/\mathbb Q\) and a prime \(p\ne\ell\) of good reduction, this is the arithmetic-Frobenius polynomial of \(\rho_{E,\ell}\). It is independent of \(\ell\).

**Proof.** Write \(t=\operatorname{tr}(\varphi\mid V_\ell\widetilde E)\). Formula (3) gives \(\det\varphi=q\). Since the space has dimension two,
\[
 \det(1-\varphi)=1-t+q.
\]
Equations (3) and (4) give \(\#\widetilde E(\mathbb F_q)=1-t+q\), so \(t=a_q\). This proves (5). Theorem 3.1 identifies this operator with arithmetic Frobenius on the original Tate module. Both coefficients of (5) are integer point-counting data, so no choice of \(\ell\ne p\) affects them. \(\square\)

This establishes more than the determinant assertion alone. In particular, it identifies the trace as an integer without needing to show separately that an endomorphism has an integral trace.

## 4. Positivity gives the Hasse bound

**Theorem 4.1 (Hasse).** Every elliptic curve over \(\mathbb F_q\) satisfies
\[
 |q+1-\#E(\mathbb F_q)|\le2\sqrt q.
\]

**Proof.** Let \(a=q+1-\#E(\mathbb F_q)\). For integers \(m,n\), the endomorphism \([m]+[n]\varphi\) has nonnegative degree. By Theorem 2.2 and the trace and determinant in (5),
\[
 0\le\deg([m]+[n]\varphi)
 =\det(m+n\varphi)=m^2+amn+qn^2.
 \tag{6}
\]
If \(a^2>4q\), the real polynomial \(z^2+az+q\) is negative on a nonempty open interval around \(-a/2\). That interval contains a rational number \(m/n\), with \(n\ne0\). Multiplying its negative value by \(n^2\) contradicts (6). Hence \(a^2\le4q\). \(\square\)

The two roots \(\alpha,\beta\) of (5) have complex absolute value \(\sqrt q\). If the discriminant is negative, they are complex conjugates with product \(q\). If it is zero, both are \(\pm\sqrt q\). The bound excludes a positive discriminant. This observation will control convergence of the elliptic-curve Euler product.

The cohomological normalization deserves care. There are natural identifications
\[
 H^1_{\mathrm{et}}(E_{\bar K},\mathbb Q_\ell)
 \simeq(V_\ell E)^\vee\simeq V_\ell E(-1).
\]
Here is a proof of the first identification as well as the normalization. Over \(\bar K\), adjoining an \(m\)-th root of a unit is étale when \(m\) is prime to the characteristic: its polynomial derivative is a unit at the root. Hence the Kummer sequence
\[
1\longrightarrow\mu_m\longrightarrow\mathbf G_m
\xrightarrow{\,m\,}\mathbf G_m\longrightarrow1
\]
is exact on the étale site. Its degree-one calculation says
\(H^1_{\mathrm{et}}(E_{\bar K},\mu_m)\simeq\operatorname{Pic}(E_{\bar K})[m]\), since every nonzero constant has an \(m\)-th root. One may see this directly: a \(\mu_m\)-torsor supplies transition functions of a line bundle with a trivialized \(m\)-th power. Conversely, choose an étale cover on which the trivialization has an \(m\)-th root; the line-bundle transitions then become \(\mu_m\)-valued. Changes of frames give exactly the coboundaries, and divisibility of the constants removes the trivialization ambiguity. A torsion line bundle has degree zero, so (G3) identifies this Picard torsion with \(E[m]\). These constructions are natural under Galois and multiplication in \(m\).

Taking the inverse limit for \(m=\ell^a\) therefore gives \(H^1_{\mathrm{et}}(E_{\bar K},\mathbb Z_\ell(1))\simeq T_\ell E\). In the continuous-cohomology convention the only possible degree-one correction is \(\varprojlim{}^1 H^0(E_{\bar K},\mu_{\ell^a})\). This correction vanishes explicitly: for a system with surjective maps \(u_a:A_{a+1}\to A_a\), the map \((b_a)\mapsto(b_a-u_ab_{a+1})\) on \(\prod A_a\) is onto, by choosing \(b_1\) and then successively lifting \(b_a-c_a\) for any prescribed \((c_a)\); its cokernel is the defining \(\varprojlim{}^1\). Here \(A_a=\mu_{\ell^a}\) and \(u_a\) is the surjective power map. Tensoring with \(\mathbb Q_\ell\) and untwisting gives \(H^1_{\mathrm{et}}(E_{\bar K},\mathbb Q_\ell)\simeq V_\ell E(-1)\). Lemma 1.4 identifies this last module with \((V_\ell E)^\vee\), via its perfect pairing. Arithmetic Frobenius on the dual has the inverses of the eigenvalues in (5). Geometric Frobenius on the dual has the original eigenvalues. This proves the degree-one cohomological interpretation while retaining our covariant arithmetic convention.

## 5. Two point-counting examples

For a nonsingular projective Weierstrass cubic there is one point at infinity. Count the affine points one \(x\)-coordinate at a time.

**Example 5.1.** Let \(E:y^2+y=x^3-x^2\). Its integral discriminant is \(-11\). To specify and check the arithmetic convention, for (G1) put
\[
b_2=a_1^2+4a_2,\quad b_4=a_1a_3+2a_4,\quad b_6=a_3^2+4a_6,
\]
\[
b_8=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2,
\quad\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6.
\]
Here \((b_2,b_4,b_6,b_8)=(-4,0,1,-1)\), so \(\Delta=16-27=-11\). We check smoothness directly. The point at infinity is smooth because the homogeneous equation's \(Z\)-derivative there is one. For the affine equation \(f=y^2+y-x^3+x^2\), its \(y\)-derivative is one in characteristic two. In odd characteristic a singular point must have \(y=-1/2\) and \(x(2-3x)=0\). In characteristic three this forces \(x=0\), where \(f=-1/4\ne0\). In every other odd characteristic the possibilities are \(x=0\), again impossible, and \(x=2/3\), where \(f=-11/108\). Thus the equation is nonsingular at exactly the primes other than \(11\). In increasing order \(x=0,1,\dots,p-1\), the numbers of \(y\)-solutions are:

| \(p\) | Numbers of solutions for successive \(x\) | \(\#E(\mathbb F_p)\) | \(a_p\) |
|---|---|---|---|
| 2 | 2, 2 | 5 | −2 |
| 3 | 2, 2, 0 | 5 | −1 |
| 5 | 2, 2, 0, 0, 0 | 5 | 1 |
| 7 | 2, 2, 0, 0, 2, 2, 1 | 10 | −2 |
| 13 | 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0 | 10 | 4 |

For odd \(p\), these entries are obtained by setting \(u=2y+1\): one solves \(u^2=1+4x^3-4x^2\). A zero right side gives one solution, a nonzero square gives two, and a nonsquare gives none. At \(p=2\), the left side \(y^2+y\) is zero for both elements and so is \(x^3-x^2\).

The good-prime traces just computed coincide with the corresponding coefficients of \(f=\eta(z)^2\eta(11z)^2\). Indeed
\[
 f=q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2.
\]
Multiplying only factors with exponent at most \(12\) gives
\[
 f=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7
 -2q^9-2q^{10}+q^{11}-2q^{12}+4q^{13}+O(q^{14}).
\]
Thus the prime coefficients through \(13\) agree with the counts. The absence of a \(q^8\) term means its coefficient is zero. Identification with a modular form is treated in *Galois representations of weight-two newforms*; this calculation itself only multiplies a finite product.

At \(11\) the cubic is singular, so Theorem 3.2 does not apply. Its projective point count is \(11\), computed from the affine counts \(2,2,0,0,0,2,0,1,1,0,2\) and the point at infinity. Its singular point is \((8,5)\); putting \(u=x-8,v=y-5\) gives \(v^2=u^2+u^3\). The two tangent lines \(v=u\) and \(v=-u\) are distinct and defined over \(\mathbb F_{11}\). It is therefore a split node. Under the multiplicative local-factor convention, which assigns coefficient \(+1\) to a split node and \(-1\) to a nonsplit node, its bad-prime coefficient is \(1\) and its factor has degree one. The general comparison of this convention with the Galois local factor belongs to the bad-reduction lesson. Counting this singular cubic must not be presented as good reduction.

**Example 5.2.** Let \(E':y^2=x^3-x\). The displayed discriminant formula gives \((b_2,b_4,b_6,b_8)=(0,-2,0,-1)\), hence \(\Delta=64\). The point at infinity is smooth as before. At an odd prime an affine singular point would have \(y=0\), hence \(x=0,1,-1\), but the \(x\)-derivative \(1-3x^2\) is respectively \(1,-2,-2\), all nonzero. In characteristic two, \((1,0)\) is singular. This verifies the good and bad primes directly. At odd primes,
\[
 \#E'(\mathbb F_p)=p+1+\sum_{x\in\mathbb F_p}
 \left(\frac{x^3-x}{p}\right),
\]
where the Legendre symbol is zero at zero. The square map on \(\mathbb F_p^\times\) has kernel \(\{1,-1\}\), so the nonzero squares form an index-two subgroup; this proves multiplicativity of the symbol. If \(p\equiv3\pmod4\), a square root of \(-1\) would have order four, contradicting Lagrange's theorem in the group of order \(p-1\). Thus \(\left(\frac{-1}{p}\right)=-1\). The substitution \(x\mapsto-x\) negates the symbol, since \((-x)^3-(-x)=-(x^3-x)\). The sum is therefore zero, and \(a_p=0\) for every such prime, not just the small examples. In particular \(\#E'(\mathbb F_p)=p+1\) at \(p=3,7,11,19,23\).

At \(5\) the successive affine counts are \(1,1,2,2,1\), giving \(\#E'=8\) and \(a_5=-2\). At \(13\) they are \(1,1,0,0,0,2,0,0,2,0,0,0,1\), giving \(\#E'=8\) and \(a_{13}=6\). Each satisfies the Hasse bound. The curve has bad reduction at \(2\), which is excluded from these statements.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Count the points of \(y^2+y=x^3-x^2\) at every prime at most \(13\), distinguishing the bad prime.

**Solution.** Use the six lists in Example 5.1. Their affine totals at \(2,3,5,7,11,13\) are \(4,4,4,9,10,9\); adding the unique point at infinity gives \(5,5,5,10,11,10\). The good-prime traces are respectively \(-2,-1,1,-2,4\) with \(11\) omitted. The partial-derivative calculation in that example verifies the bad prime indicated by \(\Delta=-11\). Its singular cubic has \(11\) projective points and a split node, so the multiplicative convention assigns coefficient \(1\) and a degree-one factor rather than the degree-two good factor.

**Exercise 6.2 (medium).** Derive \(\deg\alpha=\det(\alpha\mid T_\ell E)\) from the Weil pairing, allowing an inseparable endomorphism.

**Solution.** A nonzero endomorphism is an isogeny and has a dual. Equation (1) applied to \(\alpha P,\alpha Q\) gives exponent \(\deg\alpha\); the rank-two determinant identity gives exponent \(\det\alpha\). Since a torsion basis has primitive Weil-pairing value, the two exponents agree modulo every \(\ell^a\). The inverse limit gives equality in \(\mathbb Z_\ell\). The dual-isogeny identity applies to inseparable isogenies as well, so no separability condition has entered. The zero map has zero degree and zero determinant.

**Exercise 6.3 (medium).** Prove the Hasse bound from nonnegativity of degree, and justify the passage from integer pairs to a real discriminant inequality.

**Solution.** Equation (6) holds for all integer pairs. A negative value of \(z^2+az+q\) would persist on an open interval, and rational density supplies an integer pair \((m,n)\), \(n\ne0\), making (6) negative. Thus the polynomial is nonnegative on the real line. Its minimum at \(-a/2\) is \(q-a^2/4\), so \(a^2\le4q\).

**Exercise 6.4 (hard).** Prove \(a_p=0\) for \(y^2=x^3-x\) when \(p\equiv3\pmod4\), and explain the supersingular conclusion.

**Solution.** The character sum in Example 5.2 changes sign under the bijection \(x\mapsto-x\), so it equals its negative as an integer and is zero. With \(a_p=0\), Theorem 3.2 and Cayley–Hamilton give \(\varphi^2+[p]=0\) on the Tate module. Faithfulness, proved after Theorem 2.2, gives the same identity in \(\operatorname{End}(E')\). Thus \([p]=-\varphi^2\) is purely inseparable: Lemma 1.5 proves this for \(\varphi\), and multiplication by \(-1\) is an automorphism. Its geometric kernel has only one point. This is exactly the definition of a supersingular elliptic curve, \(E'[p](\overline{\mathbb F}_p)=\{O\}\). The argument includes \(p=3\).

## Proof dependencies and further study

The general curve foundations used here have actual earlier programme proofs: *Abelian varieties*, Lemma 9.11 and Example 9.12, for Riemann–Roch, curve duality and pointed cubic embedding; Lemma 9.0a and Theorem 9.0 for point classes, projective-curve finiteness and the group law; Proposition 6.3 for finite translation quotients. The earlier morphism lessons supply the smooth-coordinate criterion and the étale-neighbourhood colimit construction; the opening module and affine descent proofs of *Quotients and torsors* are used in the relative finiteness lemma. The local-field lesson supplies the unramified extension correspondence. Section 1 proves the elliptic multiplication degrees, torsion structure and transitions, the dual identities including inseparable isogenies, every property of the Weil pairing used here, and the Frobenius degree and kernel formula. Section 3 proves the needed relative finiteness and finite étale lifting calculations. The five arithmetic theorems and the degree-one Kummer comparison are then proved in this lesson.

The displayed eta-product computation compares finitely many coefficients. Its identification as the modular form attached to the curve and the general bad-reduction local-factor theorem belong to the subsequent lessons; they are not inputs to the determinant or Hasse proofs. General higher-dimensional abelian-variety theory and higher-degree étale cohomology are not needed here.

## Freely accessible primary material

- J. S. Milne, *Abelian Varieties*, author’s course notes, version 2.0 (2008), I §§7–9 and §13, especially printed pp.57–58 for the rational-function pairing construction and its normalization. [Author’s PDF](https://www.jmilne.org/math/CourseNotes/AV.pdf). Its deferred proofs of pairing properties are supplied by Lemma 1.4 above.
- Andrew V. Sutherland, *Elliptic Curves*, MIT 18.783 author’s lecture notes (2023): [Lecture 5, §§5.1 and 5.6](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf), [Lecture 6, §6.3](https://math.mit.edu/classes/18.783/2023/LectureNotes6.pdf), and [Lecture 23, §§23.4–23.5](https://math.mit.edu/classes/18.783/2023/LectureNotes23.pdf). These provide comparisons for isogenies, torsion and pairings. The all-characteristic proofs and the proofs deferred in those notes are written above or have the exact earlier programme providers named above.
- The Stacks Project, [Lemma 10.153.7, Tag 04GK](https://stacks.math.columbia.edu/tag/04GK), for comparison with the finite étale splitting argument in Lemma 3.0.

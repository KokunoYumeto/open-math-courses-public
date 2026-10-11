# Nuclear biduals and extensions

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

There are two different approximation questions here. A finite model of a C*-algebra must approximate each chosen element in norm. A finite model of its bidual is tested by normal functionals. We will connect those questions after constructing the central projection that separates an ideal from its quotient.

The central projection is useful even before approximation enters the argument: it explains how the quotient map acts on the bidual, and why the original algebra need not split. The other construction is a completely positive retraction onto a represented commutant. We build it on a dilation space, including the extra step needed when the coefficient algebra has no unit. These two constructions meet in the nuclearity and extension theorems below.

Prerequisites are [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md), [Finite models of a von Neumann algebra](semidiscrete-finite-models.md), and Averaging, crossed products, and injectivity. The [state representation and bidual construction](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#constructing-the-bidual-before-using-it) identifies \(A^{**}\) with its universal represented closure and its predual with \(A^*\). [The normal-extension theorem](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#oa-fnd-wa-02) gives central kernels and normal isomorphisms onto essential represented closures. Its [second-adjoint proof](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#second-adjoints-of-homomorphisms) treats inclusions and quotients. The underlying central-ideal result is [Theorem 8.3(4)](../../foundations-of-von-neumann-algebras/src/the-double-commutant-theorem.md#oa-fnd-bi-10).

All algebras may be nonunital, and all Hilbert spaces and index sets may be arbitrary. Zero algebras have the unique zero interpretation. Inner products are linear in the second variable.

## Read the approximation topology first

**Example 3.3.** For any set \(I\), \(c_0(I)^*=\ell^1(I)\) and \(c_0(I)^{**}=\ell^\infty(I)\). Coordinate truncations through \(\mathbb C^F\), directed by finite subsets \(F\subset I\), approximate the identity of \(c_0(I)\) in norm. On the bidual the same truncations approximate the identity ultraweakly, because every normal functional is an absolutely summable coordinate family. Both algebras therefore have the appropriate finite models, even when \(I\) is uncountable. The maps land in finite commutative algebras, which embed as diagonal matrix algebras with completely positive diagonal retractions.

Exercise 5 gives the estimate that separates ultraweak convergence from norm convergence in this model.

<a id="4-an-ideal-splits-the-bidual"></a>
## Construct the ideal projection and the quotient map

The dual of a quotient consists of precisely the functionals annihilating its kernel. We first realize that Banach-space fact by a projection in the universal representation.

**Proposition 4.1.** Let \(I\) be a norm-closed two-sided ideal of \(A\), and let \(q:A\to A/I\) be the quotient map. There is a central projection \(p\in A^{**}\) such that
\[
I^{**}\cong pA^{**},\qquad
(A/I)^{**}\cong(1-p)A^{**},\qquad
A^{**}\cong I^{**}\oplus(A/I)^{**}.
\]
All identifications are normal *-isomorphisms; the first extends the inclusion of \(I\), and the second is induced by \(q^{**}\).

**Proof.** Work in the universal representation of \(M=A^{**}\). The ultraweak closure \(J\) of \(I\) is an ideal in \(M\): first multiply approximating elements of \(I\) by a fixed element of \(A\), then use ultraweak density of \(A\) and separate ultraweak continuity of multiplication to allow any fixed element of \(M\).

Choose a positive contractive approximate identity \((u_i)\) of \(I\). It converges strongly to the projection \(p\) onto \(\overline{IH}\). Indeed it tends to the identity on vectors \(a\eta\), \(a\in I\), by norm approximation of \(a\); it vanishes on the orthogonal complement, since that complement is killed by \(I\). Uniform boundedness extends the convergence to all vectors. The subspace \(\overline{IH}\) reduces \(A\), since \(I\) is a two-sided *-ideal, so \(p\in M'\). Also \(p\in M\), as the bounded strong limit of \((u_i)\). Thus \(p\) is central.

Every element of \(I\), and hence of \(J\), satisfies \(x=px\). Conversely \(u_i x\in J\) for \(x\in M\), and \(u_i x\to px\) ultraweakly. Hence \(J=pM\). The second adjoint of the inclusion identifies \(I^{**}\) normally and isometrically with this closure.

On the dual side \(q^*:(A/I)^*\to A^*\) is an isometry with range
\[
I^\perp=\{f\in A^*:f|_I=0\}.
\]
Therefore
\[
\ker q^{**}=(I^\perp)^\perp=J=pM.
\]
The middle equality is the weak* annihilator identity proved in [CP-05](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.5): a point outside a weak* closed linear subspace is separated from it by a finite linear combination of the coordinates defining a disjoint basic neighborhood. The map \(q^{**}\) is onto: a bounded functional on \(I^\perp\subset A^*\) extends to \(A^*\) by Hahn–Banach, and that extension is an element of \(A^{**}\) with the required image. It is a normal \*-homomorphism by the second-adjoint theorem. Restricting to \(E=(1-p)M\) gives a bijective normal \*-homomorphism \(V:E\to N=(A/I)^{**}\). An injective \*-homomorphism is isometric. Moreover \(V\) maps the closed unit ball onto the closed unit ball: Hahn–Banach gives a lift of any \(Y\in N\) with norm \(\|Y\|\), and compression by \(1-p\) leaves its image unchanged and cannot increase its norm.

<a id="ideal-splitting-normal-inverse"></a>

Here is a direct proof that the inverse is normal. The concrete predual of \(E\) is the quotient of \(M_*\) by the annihilator of \(E\), with \(E=(E_*)^*\) isometrically, by [CP-05–06](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.5). The preadjoint \(V_*:N_*\to E_*\) is an isometry because \(V\) maps the unit ball onto the unit ball, so its range is norm closed. If \(X\in E=(E_*)^*\) annihilates that range, then \(\rho(VX)=0\) for every \(\rho\in N_*\), whence \(VX=0\) and \(X=0\). Hahn–Banach makes the range norm dense: otherwise it would supply a nonzero bounded functional annihilating its closed range. Thus \(V_*\) is a surjective isometry, its inverse is bounded, and \(V^{-1}=(V_*^{-1})^*\) is weak* continuous. This proves normality of the inverse, including zero summands. Combining the two central summands proves the decomposition. \(\square\)

The splitting takes place in \(A^{**}\). It does not assert that \(A\) is a direct sum of its ideal and quotient.

<a id="2-a-nuclear-algebra-gives-a-gns-commutant-retraction"></a>
## Construct a retraction on a dilation space

**Proposition 2.1.** If \(A\) is nuclear, every state GNS commutant \(C=\pi_\varphi(A)'\) is injective.

**Proof.** Write \(\pi:A\to B(H)\) for the state GNS representation and put \(C=\pi(A)'\). Only nondegeneracy of \(\pi\) is needed in this proof. The state case has \(H\ne0\). Nuclearity and the tensor-norm construction give a *-homomorphism
\[
\rho:C\otimes_{\min}A\longrightarrow B(H),
\qquad \rho(c\otimes a)=c\pi(a).
\]
Indeed the two commuting representations first give a homomorphism for the maximal norm, and nuclearity identifies that norm with the minimal norm. Spatial tensor injectivity embeds \(D=C\otimes_{\min}A\) in \(L=B(H)\otimes_{\min}A\).

Use forced unitizations, with the same newly adjoined unit for \(D^\dagger\subset L^\dagger\), even if these algebras already have units. The map
\(\rho^\dagger(d+\lambda1)=\rho(d)+\lambda1_H\)
is a unital *-homomorphism. The full [Arveson extension proof](completely-positive-finite-models.md#theorem-2-3) extends it to a ucp map \(\Phi:L^\dagger\to B(H)\). The full [unital dilation construction](completely-positive-lifting.md#unital-dilation) supplies a representation \(\sigma:L^\dagger\to B(K)\) and an isometry \(V:H\to K\) such that
\[
\Phi(l)=V^*\sigma(l)V.
\]
For every \(d\in D\), the fact that \(\Phi\) agrees with a homomorphism on \(D\) gives
\[
\sigma(d)V=V\rho(d),\qquad
V^*\sigma(d)=\rho(d)V^*.
\]
For completeness, the squared norm of \(\sigma(d)V\eta-V\rho(d)\eta\) is the quadratic form of
\(\Phi(d^*d)-\Phi(d)^*\Phi(d)=0\).
Apply the same computation to \(d^*\) and take adjoints to get the second identity.

<a id="nonunital-dilation-retraction"></a>

The operator \(b\otimes1_A\) need not be an element of \(L\). We now construct its action without assuming that \(A\) has a unit. Let \((u_i)\) be a positive contractive approximate identity of \(A\), put \(h_i=1_H\otimes u_i\), and set
\(K_0=\overline{\sigma(L)K}\).
The operators \(\sigma(h_i)\) converge strongly to the projection \(P\) onto \(K_0\). On vectors \(\sigma(l)\zeta\) this follows from \(h_i l\to l\) in norm; on \(K_0^\perp\) every \(\sigma(l)\) vanishes. The common contraction bound extends convergence to all of \(K\). Since
\[
V^*\sigma(h_i)V=\rho(h_i)=\pi(u_i)\longrightarrow1_H
\]
strongly, \(V^*PV=1_H\). Consequently
\(\|(1-P)V\eta\|^2=0\), so \(VH\subset K_0\). The space \(K_0\) reduces \(\sigma\), and we henceforth restrict the dilation to it.

For \(b\in B(H)\), the uniformly bounded operators \(\sigma(b\otimes u_i)|_{K_0}\) converge strongly to an operator \(\tau(b)\). To check this, use the dense vectors \(\sigma(c\otimes a)\zeta\), with \(c\in B(H)\), \(a\in A\):
\[
\sigma(b\otimes u_i)\sigma(c\otimes a)\zeta
=\sigma(bc\otimes u_i a)\zeta
\longrightarrow\sigma(bc\otimes a)\zeta.
\]
The bound \(\|\sigma(b\otimes u_i)\|\le\|b\|\) makes the limit well defined on all of \(K_0\), independent of the chosen approximate identity. This formula on dense vectors proves linearity and multiplication for \(\tau\). Applying it also to \(b^*\), and taking vector coefficients, proves \(\tau(b)^*=\tau(b^*)\). The case \(b=1_H\) gives \(\tau(1_H)=1_{K_0}\). Thus \(\tau:B(H)\to B(K_0)\) is a unital *-representation. On the same dense vectors, \(\tau(b)\) commutes with \(\sigma(1_H\otimes a)\) for every \(a\in A\).

Define
\[
E(b)=V^*\tau(b)V\qquad(b\in B(H)).
\]
Compression of a unital *-representation by an isometry is ucp. The intertwining identities for \(1_H\otimes a\in D\) now show
\[
E(b)\pi(a)
=V^*\tau(b)\sigma(1_H\otimes a)V
=V^*\sigma(1_H\otimes a)\tau(b)V
=\pi(a)E(b).
\]
Hence \(E(b)\in C\). If \(c\in C\), apply the intertwining identity instead to \(c\otimes u_i\in D\). Strong convergence gives
\[
\tau(c)V\eta
=\lim_i\sigma(c\otimes u_i)V\eta
=\lim_iVc\pi(u_i)\eta=Vc\eta.
\]
Therefore \(E(c)=c\). This is the required ucp retraction onto \(C\), and proves injectivity. No normality of \(E\) is asserted or needed. \(\square\)

<a id="1-cyclic-representations-detect-injectivity-of-the-bidual"></a>
## Assemble cyclic information by finite central covers

**Lemma 1.1.** Suppose that \(\pi_\varphi(A)''\) is injective for every state \(\varphi\) on \(A\). Then \(A^{**}\) is injective.

**Proof.** The zero algebra has zero bidual and needs no construction. Otherwise put \(M=A^{**}\). For each state \(\varphi\), its normal representation extension has a central kernel \(M(1-z_\varphi)\), and identifies \(Mz_\varphi\) normally with \(\pi_\varphi(A)''\). Thus each \(Mz_\varphi\) is injective. Moreover
\[
\bigvee_\varphi z_\varphi=1.
\]
An element killed by all these extensions acts as zero in every state GNS summand of the faithful universal representation. Hence the intersection of their kernels is zero, which proves the displayed equality.

For a finite set \(F=\{\varphi_1,\ldots,\varphi_n\}\), let \(z_F=\bigvee_{\varphi\in F}z_\varphi\). Although the projections may overlap, they admit the finite partition
\[
p_1=z_{\varphi_1},\qquad
p_k=z_{\varphi_k}\prod_{j<k}(1-z_{\varphi_j})\quad(2\le k\le n).
\]
These are orthogonal central projections with sum \(z_F\), and \(p_k\le z_{\varphi_k}\). Central corners and finite products of injective algebras are injective, so \(Mz_F\) is injective. This conclusion is independent of the enumeration of \(F\).

Represent \(M\) faithfully and normally on \(H\). For each \(F\), choose a ucp retraction \(B(z_FH)\to Mz_F\), and compose with compression \(b\mapsto z_Fbz_F\). Regard its values as elements of \(M\), and call the resulting cpc map \(E_F:B(H)\to M\). For \(x\in M\),
\[
E_F(x)=z_Fx,\qquad E_F(1)=z_F.
\]
The finite sets are directed by inclusion, and \(z_F\uparrow1\) strongly, hence ultraweakly, by the bounded monotone convergence theorem. The compactness of the product of ultraweakly compact balls gives a subnet of \((E_F)\) converging ultraweakly at each \(b\in B(H)\). Its limit \(E\) is linear and completely positive: each matrix quadratic form is a finite sum of vector coefficients and preserves positivity under the limit. Its norm is at most one, \(E(1)=1\), and \(E(x)=x\) for all \(x\in M\). Thus \(E\) is a ucp retraction onto \(M\). This uses finite overlapping covers rather than a maximal disjoint family of cyclic summands, and works for arbitrary state sets and Hilbert spaces. \(\square\)

The full [normal-extension theorem](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#oa-fnd-wa-02) supplies the central kernels used here. Bounded monotone convergence is [Vigier's theorem](../../foundations-of-von-neumann-algebras/src/the-spectral-theorem-for-bounded-self-adjoint-operators.md#oa-fnd-st-06). The product compactness and predual inputs are [CF-02–03](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.2) and [CP-05–06](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.5). The commutant permanence theorem also lets the hypothesis be stated using injectivity of each \(\pi_\varphi(A)'\).

<a id="3-nuclearity-is-injectivity-of-the-universal-bidual"></a>
## Convert the two approximation questions

**Theorem 3.1.** For any C*-algebra \(A\),
\[
A\text{ is nuclear}
\quad\Longleftrightarrow\quad
A^{**}\text{ is injective}.
\]

**Proof.** Starting with nuclear \(A\), Proposition 2.1 constructs a retraction onto every state GNS commutant. Commutant permanence gives injectivity of the corresponding represented von Neumann algebras; the finite-cover construction of Lemma 1.1 then gives injectivity of \(A^{**}\).

In the reverse direction, let \(M=A^{**}\) be injective. The injective/semidiscrete equivalence in the averaging lesson produces cpc predual factorizations
\[
M_*\longrightarrow M_n^*\longrightarrow M_*
\]
approximating the identity at each predual element in norm. The identification \(M_*=A^*\) preserves both the norm and the dual matrix orders. These factorizations therefore satisfy the pointwise weak* hypothesis of Corollary 4.2 in the tensor-positivity lesson, which proves nuclearity of \(A\). The norm on \(M_n^*\) is the trace norm. Thus the passage from normal tests back to norm approximation uses predual approximation and the proved tensor corollary. \(\square\)

**Corollary 3.2.** If \(A\) is nuclear, the von Neumann algebra generated by every nondegenerate representation of \(A\) is injective and semidiscrete. Conversely, this property for the universal representation, or injectivity for every state GNS representation, implies nuclearity.

**Proof.** A nondegenerate represented closure is normally isomorphic to a central summand of \(A^{**}\). Central corners preserve injectivity, and injectivity gives semidiscreteness. The universal representation realizes the whole bidual. The last assertion follows from Lemma 1.1 and Theorem 3.1. \(\square\)

For a degenerate representation, the represented closure is understood on its essential Hilbert space. Taking the bicommutant in an ambient space with a zero representation summand adds an unrelated identity there; the normal extension theorem is applied to the essential space.

## Apply the projection to an extension

**Theorem 4.2.** For a closed two-sided ideal \(I\subseteq A\),
\[
A\text{ is nuclear}
\quad\Longleftrightarrow\quad
I\text{ and }A/I\text{ are nuclear}.
\]

**Proof.** Write the normal splitting from Proposition 4.1 as
\(A^{**}=pA^{**}\oplus(1-p)A^{**}\).
If \(A\) is nuclear, Theorem 3.1 makes its bidual injective. Its two central corners are injective, so their identifications with \(I^{**}\) and \((A/I)^{**}\), followed by Theorem 3.1, make \(I\) and \(A/I\) nuclear. Conversely, nuclearity of those two algebras makes both bidual summands injective. Their product is injective, and the normal splitting then makes \(A^{**}\) injective. Theorem 3.1 returns nuclearity of \(A\). \(\square\)

**Example 4.3.** Let \(A=C([0,1])\), and \(I=\{f:f(0)=0\}\cong C_0((0,1])\). Evaluation at zero gives \(A/I\cong\mathbb C\). The ideal and quotient are nuclear by the commutative finite-model construction, so the extension theorem gives nuclearity of \(A\). The central projection selecting \(I^{**}\) belongs to \(A^{**}\) and not to \(A\); the next exercise section verifies this directly.

## Order laboratory: domination and ambient norm

The retraction proof above uses a dilation. A different useful question is how a dominated functional determines an operator in a cyclic commutant. The following construction is retained in full for Exercises 3 and 4; it explains why an order inverse need not be an ambient Banach-space inverse.

Fix a state \(\varphi\), its nondegenerate GNS representation \((\pi,H,\xi)\), and \(C=\pi(A)'\). The GNS dominated-functional theorem gives the complete order isomorphism
\[
R_\varphi:C\longrightarrow D_\varphi\subset A^*,\qquad
R_\varphi(c)(a)=\langle\xi,\pi(a)c\xi\rangle,
\]
where \(D_\varphi\) is the linear span of positive functionals dominated by scalar multiples of \(\varphi\). It sends \(1\) to \(\varphi\), and
\[
0\le f\le r\varphi
\quad\Longrightarrow\quad
0\le R_\varphi^{-1}(f)\le r1.
\]
The inverse need not be bounded for the ambient norm of \(A^*\). The distinction between these two bounds is the subject of Exercises 3 and 4.

The full order proof is the cyclic construction in Section 2 of [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md#2-keep-a-marginal-exactly-fixed), now applied to \(\pi(A)\xi\). Namely, for \(0\le f\le r\varphi\), define
\[
\langle\pi(a)\xi,z_f\pi(b)\xi\rangle=f(a^*b).
\]
Cauchy–Schwarz and domination bound this form by \(r\|\pi(a)\xi\|\|\pi(b)\xi\|\), so it represents a unique \(0\le z_f\le r1\). The form identity with \(a^*cb\), for \(c\in A\), shows that \(z_f\) commutes with \(\pi(A)\), hence belongs to \(C\). If \(A\) is nonunital, use a positive contractive approximate identity \((u_i)\): \(\pi(u_i)\xi\to\xi\) and \(f(u_i a)\to f(a)\) give
\[
R_\varphi(z_f)(a)=\langle\xi,\pi(a)z_f\xi\rangle=f(a).
\]
Commutation identifies all other form coefficients from this functional, proving injectivity. Conversely each \(0\le z\le r1\) gives the dominated positive vector functional \(R_\varphi(z)\le r\varphi\); decomposing an arbitrary element of \(C\) into four positive parts gives exactly the claimed linear range. At matrix level, positive matrices over the two commuting algebras pair positively, as proved in the tensor lesson. For the inverse, positivity of \([f_{ij}]\) gives
\[
\sum_{i,j}\langle\pi(a_i)\xi,z_{ij}\pi(a_j)\xi\rangle
=\sum_{i,j}f_{ij}(a_i^*a_j)\ge0,
\qquad z_{ij}=R_\varphi^{-1}(f_{ij}).
\]
Density of \(\pi(A)\xi\) proves \([z_{ij}]\ge0\). Thus both directions preserve every matrix cone even in the nonunital case, while no ambient inverse norm bound has been introduced.

## 5. Exercises with solutions

**Exercise 1.** Let \(A=\mathbb C\), and take the direct sum of two copies of its scalar representation on \(\mathbb C\). Compute the commutant of this sum and compare it with the product of the two separate commutants.

*Solution.* The summed representation is \(\lambda\mapsto\lambda1_2\), whose commutant is all of \(M_2\). The product of the separate commutants is the diagonal algebra \(\mathbb C\oplus\mathbb C\). Off-diagonal matrix units intertwine the identical summands. This is why Lemma 1.1 uses central supports rather than a product assertion about universal commutants.

**Exercise 2.** Assume, as in Lemma 1.1, that every state GNS represented closure of \(A\) is injective. Let \(M=A^{**}\) act universally, let \(z\in M\) be a nonzero central projection, choose a unit vector \(\xi\in zH\), and let \(e\in M'\) be the projection onto \(\overline{A\xi}\). Verify that \(w=c_{M'}(e)\le z\), although \(e\) need not belong to \(M\).

*Solution.* The projection \(z\) is central in both \(M\) and \(M'\), and \(e\le z\). The central support in \(M'\) is the least central projection of that algebra majorizing \(e\), so it is at most \(z\). Since \(e\ne0\), also \(w\ne0\). If the cyclic represented closure is injective, its normal extension has kernel \(M(1-w)\): an operator commuting with \(M'\) and vanishing on \(eH\) vanishes on \(\overline{M' eH}=wH\). The normal-extension theorem then identifies that closure with the nonzero central summand \(Mw\subset zM\).

**Exercise 3.** Suppose a positive map \(\Theta:B\to A^*\) has \(\Theta(1)=\varphi\), where \(B\) is unital and \(\varphi\) is a state. Explain why \(R_\varphi^{-1}\Theta\) is defined on all of \(B\). If \(\Theta\) is completely positive, show that this composition has norm one.

*Solution.* For \(b\ge0\), the inequality \(b\le\|b\|1\) gives \(0\le\Theta(b)\le\|b\|\varphi\), placing \(\Theta(b)\) in \(D_\varphi\). Positive elements span \(B\), so every image belongs to that linear space. The complete order inverse makes the composition completely positive, and its value at the unit is \(R_\varphi^{-1}(\varphi)=1\). A unital completely positive map has norm one. No ambient norm bound for \(R_\varphi^{-1}\) is needed.

**Exercise 4.** For \(A=C([0,1])\) with the integration state \(\varphi(f)=\int_0^1f(t)\,dt\), let \(c_n\) be multiplication by \(1_{[0,1/n]}\) in the GNS commutant. Compute \(\|c_n\|\) and \(\|R_\varphi(c_n)\|\). What does this show about the complete order inverse in the order laboratory?

*Solution.* The multiplication projection has norm one. Its positive functional is \(f\mapsto\int_0^{1/n}f(t)\,dt\), with norm \(1/n\), attained at the unit. Thus \(R_\varphi^{-1}\) is unbounded in the inherited Banach norm of its range. The composition in Exercise 3 remains bounded because it is completely positive and unital, with the required order bounds. Proposition 2.1 constructs its retraction directly by dilation.

**Exercise 5.** In Example 3.3, prove ultraweak convergence of finite-coordinate truncations on \(\ell^\infty(I)\). Explain why their convergence on the unit is usually not norm convergence.

*Solution.* For \(x\in\ell^\infty(I)\), \(a\in\ell^1(I)\), and \(P_Fx=1_Fx\),
\[
|\langle a,x-P_Fx\rangle|
\le\|x\|_\infty\sum_{i\notin F}|a_i|\longrightarrow0.
\]
Every absolutely summable family has finite tails as small as desired, giving the directed convergence. If \(I\) is infinite, \(\|1-P_F1\|_\infty=1\) for every finite \(F\). Semidiscrete approximation is tested by normal functionals rather than the operator norm of the unit error.

**Exercise 6.** Verify surjectivity of \(q^{**}\) in Proposition 4.1 directly from \(q^*\), including its norm control.

*Solution.* Identify \((A/I)^*\) isometrically with \(I^\perp\) through \(q^*\). An element \(Y\in(A/I)^{**}\) becomes a bounded functional on \(I^\perp\) of norm \(\|Y\|\). Hahn–Banach extends it to \(X\in(A^*)^*=A^{**}\) with the same norm. The adjoint definition then gives \(q^{**}X=Y\). Multiplying \(X\) by \(1-p\) leaves its image unchanged and cannot increase its norm.

**Exercise 7.** In Example 4.3 use \(u_n(t)=\min(1,nt)\) as an approximate identity for \(I\). Determine the values of the central support projection \(p\in A^{**}\) under all point-evaluation states. Prove \(p\notin A\).

*Solution.* Uniform convergence \(u_nf\to f\) for \(f\in I\) follows by making \(f\) small near zero and using \(u_n=1\) away from zero for large \(n\). Hence \(u_n\to p\) strongly in the universal representation. The canonical normal extensions of evaluation at \(t\) take value zero on \(p\) when \(t=0\) and value one when \(t>0\). If \(p\) came from \(A\), that continuous function would have these point values, which is impossible at zero. Thus the bidual splitting uses a projection absent from the original C*-algebra.

**Exercise 8.** Show that the nuclearity–bidual theorem does not justify passing nuclearity to an arbitrary C*-subalgebra merely by inclusion. Identify the unsupported step in that attempted argument.

*Solution.* An inclusion \(B\subseteq A\) induces an inclusion \(B^{**}\subseteq A^{**}\). Injectivity of the larger algebra does not itself supply a ucp retraction onto this smaller von Neumann algebra. The permanence results proved here apply to corners, products, suitable directed limits and the explicit averaged fixed-point algebras. An arbitrary von Neumann subalgebra has not been shown to be one of those. Thus Theorem 3.1 cannot establish general subalgebra permanence by that argument; an additional extension or retraction mechanism would be required.

## References

Nathanial P. Brown, [The symbiosis of C*- and W*-algebras](https://arxiv.org/pdf/0812.1763v1), arXiv:0812.1763v1 (9 December 2008). Proposition 2.3.6, printed p.7, gives injectivity of the commutant of a nuclear represented algebra by an extension into the commuting range. Proposition 3.2.1, Theorem 3.2.2 and Corollary 3.2.3, printed p.10, describe the nuclearity–bidual equivalence and the ideal/quotient extension consequence. Brown leaves injectivity implying semidiscreteness to further von Neumann algebra theory; that implication here uses the full construction in Averaging, crossed products, and injectivity. Proposition 2.1 constructs the represented retraction by a tensor dilation and proves the approximate-identity step needed to define the first tensor factor on the essential dilation space. Lemma 1.1 assembles the state kernels through finite overlapping central covers and a pointwise ultraweak limit. Brown's shared-unit tensor extension and standard-form conjugation are distinct from these full local constructions.

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorem 1.2.3 proves the extension method behind Brown's commuting-range construction. Lemma 1.4.1 and Theorem 1.4.2 prove the dilation-commutant order correspondence. The full extension and unital dilation providers are linked in Proposition 2.1, which then supplies the nonunital tensor-factor construction. The order laboratory supplies the scalar cyclic form, both matrix directions and the precise domination bound.

- Bruce Blackadar, [Operator Algebras](https://www.bruceblackadar.com/Mathematics/Cycr.pdf#page=347), author-hosted edition dated 8 February 2017. III.1.1.13, printed pp.238–239 (PDF pp.246–247), describes central ideals; III.5.2.9–11, printed p.339 (PDF p.347), describes representation extensions, second adjoints of homomorphisms and the ideal bidual splitting. The full ideal approximate-unit, duality and normal-inverse arguments are given in the linked proofs and Proposition 4.1 above.
- [Bidual foundations] The [state representation and predual identification](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#constructing-the-bidual-before-using-it), [Lemma 2.1](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#oa-fnd-wa-02), and the [second-adjoint proof](../../foundations-of-von-neumann-algebras/src/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md#second-adjoints-of-homomorphisms), in the foundations of von Neumann algebras course. The central-kernel input is [Theorem 8.3(4)](../../foundations-of-von-neumann-algebras/src/the-double-commutant-theorem.md#oa-fnd-bi-10).
- [GNS order] *Completely positive maps*, Theorem 7.3(1) and (4), in the existing foundations course. The inverse is used with domination by the distinguished state, with no unjustified ambient norm bound.
- [Central support] *Projections and types of von Neumann algebras*, Proposition 3.5, in the existing foundations course. The central-support geometry is used in Exercise 2. Lemma 1.1 instead uses the normal-extension theorem for all state kernels and finite covers.

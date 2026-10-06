# Explicit local reciprocity and the existence theorem

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

Lubin–Tate division fields turn local reciprocity into a formula. Write an element of a local field as a unit times a power of a uniformizer. Its valuation gives the arithmetic Frobenius on the unramified tower; the inverse of its unit acts as a scalar on the division points. These two actions account for every finite abelian extension.

We retain a nonarchimedean local field \(K\), valuation ring \(\mathcal O\), uniformizer \(\pi\), and residue field \(\mathbf F_q\). Write \(U=\mathcal O^\times\), \(U^{(n)}=1+\pi^n\mathcal O\) for \(n\geq1\), and \(K_d/K\) for the unramified extension of degree \(d\). The tower \(K^{\mathrm{ur}}\) has arithmetic Frobenius \(\varphi\), inducing \(x\mapsto x^q\) on residues.

The proofs use the actual reciprocity construction from [Frobenius lifts and abstract reciprocity](frobenius-lifts-and-abstract-reciprocity.md), the finite reciprocity isomorphism and subgroup correspondence from [The reciprocity law and the class field correspondence](the-reciprocity-law-and-the-class-field-correspondence.md), and its local hypotheses and norm openness proved in [Local reciprocity and norm groups](local-reciprocity-and-norm-groups.md). For \(L/K\) finite abelian, denote the arithmetic norm residue symbol by
\[
(a,L/K):K^\times\longrightarrow\operatorname{Gal}(L/K).
\]
Its kernel is \(N_{L/K}L^\times\).

We also use Theorem 7.5 of [Formal groups and Lubin–Tate modules](formal-groups-and-lubin-tate-modules.md) and the division-field results of [Lubin–Tate division fields](lubin-tate-division-fields.md). No explicit reciprocity formula is assumed.


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-9) shows which results are proved in published lessons and which full proofs are still missing. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. Bringing a point back from a completion

The uniformizer-comparison series has coefficients in the completed unramified field, so its value initially lies in a completion. The Frobenius-lift definition, however, uses an algebraic fixed field. We first establish the passage between them.

### Lemma. Separable algebraic elements in a completed union

Let \(M\) be a directed union of complete finite extensions of \(K\), with their compatible valuations, and let \(\widehat M\) be its completion. Any element of \(\widehat M\) that is separable algebraic over \(M\) belongs to \(M\).

**Proof.** Let \(z\) be such an element. Multiplying it by an element of \(K^\times\), we may suppose \(z\) is integral. A separable polynomial over \(M\) vanishing at \(z\) can be multiplied by a nonzero constant to obtain \(P\) with integral coefficients and \(P'(z)\ne0\). Put \(s=v(P'(z))\geq0\).

Choose \(b\in M\) integral and sufficiently close to \(z\) that \(v(b-z)>2s\). Taylor expansion with integral coefficients gives
\[
v(P'(b))=s,\qquad v(P(b))>2s.
\tag{1}
\]
Indeed \(P'(b)-P'(z)\) has valuation greater than \(s\); and \(P(b)-P(z)\) is the sum of \(P'(z)(b-z)\) and terms containing \((b-z)^2\).

Put all coefficients and \(b\) in one complete finite field \(M_0\subset M\), and run Newton iteration there:
\[
b_{j+1}=b_j-\frac{P(b_j)}{P'(b_j)},\qquad b_0=b.
\]
If \(d_j=v(P(b_j))>2s\), its increment has valuation \(r_j=d_j-s>s\). All iterates are integral, their derivatives retain valuation \(s\), and cancellation of the linear Taylor term gives
\[
d_{j+1}\geq2r_j,\qquad r_{j+1}\geq2r_j-s.
\]
Thus \(r_j-s\) at least doubles; the sequence converges in \(M_0\) to a root \(c\), with \(v(c-b)>s\). If an iterate is already a root, use it as \(c\).

Both \(c\) and \(z\) are within valuation distance greater than \(s\) of \(b\). Taylor expansion at \(z\) gives, if \(c\ne z\),
\[
P(c)-P(z)=(c-z)\bigl(P'(z)+(c-z)Q\bigr),
\]
where \(Q\) is integral because \(P,c,z\) are integral. The parenthesis has valuation \(s\), so cannot be zero. Since both are roots, this is impossible. Therefore \(z=c\in M_0\subset M\). Undo the initial scaling. \(\square\)

## 2. Computing the Frobenius lift

The reciprocity map \(r_{L/K}\) in lesson 4 runs in the opposite direction to the norm residue symbol. If \(s\) is a positive Frobenius lift of \(\sigma\in\operatorname{Gal}(L/K)\) to \(LK^{\mathrm{ur}}\), and \(\Sigma\) is the fixed field of the closure of its powers, its definition is
\[
r_{L/K}(\sigma)
 =N_{\Sigma/K}(\pi_\Sigma)\pmod{N_{L/K}L^\times},
\tag{2}
\]
with \(\pi_\Sigma\) any uniformizer of \(\Sigma\). Lesson 5 proves that the symbol is the inverse of this isomorphism.

### Theorem 9.1. Explicit local reciprocity

For \(a=u\pi^r\), \(u\in U\), \(r\in\mathbf Z\), the compatible symbol on \(K^{\mathrm{ur}}K_\pi\) acts as
\[
(a,K^{\mathrm{ur}}K_\pi/K)|_{K^{\mathrm{ur}}}=\varphi^r,
\qquad
(a,K^{\mathrm{ur}}K_\pi/K)(x)=[u^{-1}]_f(x)
\tag{3}
\]
for every division point \(x\) of a Lubin–Tate module for \(\pi\).

**Proof.** Fix \(n\geq1\), and put \(L=K_{\pi,n}\). Use the polynomial series
\[
f(X)=\pi X+X^q.
\]
By Theorem 8.3 there is a unique \(\sigma\in\operatorname{Gal}(L/K)\) acting on \(T_n(f)\) by \([u^{-1}]_f\).

Since \(L/K\) is totally ramified and \(K^{\mathrm{ur}}/K\) is unramified, their intersection is \(K\); their finite levels are Galois and linearly disjoint. Thus
\[
\Gamma=\operatorname{Gal}(LK^{\mathrm{ur}}/K)
 \simeq\operatorname{Gal}(L/K)\times\widehat{\mathbf Z}.
\]
Choose \(s=(\sigma,\varphi)\). It has degree 1. Its closed cyclic subgroup is the graph \(t\mapsto(\sigma^t,t)\), where \(\sigma^t\) uses the residue of \(t\) modulo the finite order of \(\sigma\). The quotient has \(|\operatorname{Gal}(L/K)|=D_n\) elements. Its fixed field \(\Sigma\) therefore has degree \(D_n\); the degree and ramification calculation in lesson 4, equation (3), gives residue degree 1, so \(\Sigma/K\) is totally ramified.

Set \(\pi'=u\pi\), and choose \(f'(X)=\pi'X+X^q\). Let \(\widehat{\mathcal O}^{\,\mathrm{ur}}\) be the valuation ring of the completion of \(K^{\mathrm{ur}}\). Theorem 7.5 supplies an \(\mathcal O\)-linear isomorphism
\[
\theta:F_f\longrightarrow F_{f'},\qquad
\theta\in\widehat{\mathcal O}^{\,\mathrm{ur}}[[X]],\qquad
\theta^\varphi=\theta\circ[u]_f.
\tag{4}
\]
Its linear coefficient is a unit. The superscript applies \(\varphi\) to the coefficients.

Let \(\lambda\) be a primitive point of \(T_n(f)\) and evaluate \(y=\theta(\lambda)\) in the completion of \(M=LK^{\mathrm{ur}}\). The isomorphism and its integral inverse converge there. Since \(\pi'=u\pi\) differs by a unit, \(\mathcal O\)-linearity makes \(y\) a primitive \(\pi'^n\)-division point for \(F_{f'}\). In particular it is a root of the separable polynomial \(f'^{\circ n}\), by the root calculation in Proposition 8.1. The preceding lemma gives \(y\in M\).

The valuation-preserving automorphism \(s\) extends continuously to the completion. On the coefficients of \(\theta\) it acts as \(\varphi\), and on \(\lambda\) as \([u^{-1}]_f\). Hence
\[
s(y)=\theta^\varphi([u^{-1}]_f(\lambda))
     =\theta([u]_f([u^{-1}]_f(\lambda)))=y.
\tag{5}
\]
Thus \(y\in\Sigma\). Theorem 8.3 applied to \(\pi'\) gives
\[
[K(y):K]=D_n,\qquad K(y)=K_{\pi',n}.
\]
This equals \([\Sigma:K]\), so \(\Sigma=K(y)\). Because \(f'\) is the polynomial model, Proposition 8.4 gives the exact norm
\[
N_{\Sigma/K}(-y)=\pi'=u\pi.
\tag{6}
\]
The element \(-y\) is a uniformizer of \(\Sigma\). Substituting it in (2), and using that \(\pi\) is a norm from \(L\), gives
\[
r_{L/K}(\sigma)=u\pi\equiv u\pmod{N_{L/K}L^\times}.
\]
Consequently \((u,L/K)=\sigma\), which is the inverse-unit action in (3). The same norm fact gives \((\pi,L/K)=1\), so multiplying by any integer power of \(\pi\) does not alter the action on this division field.

The symbol on every finite unramified field is \(\varphi^{v_K(a)}=\varphi^r\), by the unramified formula in lesson 6. These formulas are compatible under restriction. Taking all \(n\) and all finite unramified fields proves (3). Finally the integral comparison between any two series for \(\pi\) is defined over \(K\) and commutes with scalars; it transports the formula from the polynomial model to every \(f\). \(\square\)

The inverse in \([u^{-1}]_f\) is forced by (4)–(5) and the direction of the reciprocity isomorphism. Our normalization sends a uniformizer to arithmetic Frobenius on the unramified tower.

## 3. Which norm groups occur?

For an integer \(d\geq1\), set
\[
B_{d,n}=\langle\pi^d\rangle\,U^{(n)}
       =\{u\pi^r:u\in U^{(n)},\ d\mid r\}.
\tag{7}
\]

### Corollary 9.2. Norm groups of the explicit fields

We have
\[
N_{K_{\pi,n}/K}K_{\pi,n}^\times
 =\langle\pi\rangle U^{(n)},\qquad
N_{K_dK_{\pi,n}/K}(K_dK_{\pi,n})^\times=B_{d,n}.
\tag{8}
\]

**Proof.** The symbol on \(K_{\pi,n}\) is trivial exactly when \([u^{-1}]_f\) acts identically on \(T_n(f)\). Proposition 8.1 says this occurs exactly when \(u\equiv1\pmod{\pi^n}\). Finite local reciprocity identifies this kernel with the norm group, giving the first equality.

On \(K_d\), the symbol is trivial exactly when \(d\mid r\). An automorphism of the compositum is trivial exactly when both restrictions are trivial. Its kernel is therefore \(B_{d,n}\), and reciprocity for that finite abelian compositum gives the second equality. \(\square\)

### Theorem 9.3. The local existence theorem

Every open subgroup \(H\subset K^\times\) of finite index is the norm group of a unique finite abelian extension of \(K\).

**Proof.** Openness supplies \(n\geq1\) with \(U^{(n)}\subset H\). Since \(K^\times/H\) is finite, the image of \(\pi\) has finite order \(d\); then \(\pi^d\in H\). Thus \(B_{d,n}\subset H\).

Let \(A=K_dK_{\pi,n}\). Corollary 9.2 and finite reciprocity identify \(K^\times/B_{d,n}\) with \(\operatorname{Gal}(A/K)\). Let \(J\) be the image of \(H/B_{d,n}\), and put \(E=A^J\). Restriction of the reciprocity symbol to \(E\) is the quotient by \(J\), by its functoriality. Its kernel is exactly \(H\); finite reciprocity identifies that kernel with \(N_{E/K}E^\times\). This constructs the required abelian extension.

For uniqueness use the subgroup correspondence proved in Theorem 5.3: finite abelian fields are determined by their norm groups, and norm inclusion reverses field inclusion. Equivalently, if two such fields have norm group \(H\), their compositum has the intersection of the two norm groups, again \(H\). The norm-index formula makes the compositum and each field have degree \([K^\times:H]\), so they coincide. \(\square\)

The finite-index hypothesis matters. For example \(U^{(n)}\) alone is open in \(K^\times\), but its quotient still has the infinite valuation direction.

## 4. The entire abelian closure

### Theorem 9.4. The maximal abelian extension and completion

Inside a fixed separable closure,
\[
K^{\mathrm{ab}}=K^{\mathrm{ur}}K_\pi.
\tag{9}
\]
The reciprocity homomorphism
\[
\operatorname{rec}_K:K^\times\longrightarrow
 \operatorname{Gal}(K^{\mathrm{ab}}/K)
\tag{10}
\]
is continuous, injective and has dense image. It extends to an isomorphism from the profinite completion taken with respect to **open subgroups of finite index**. With the decomposition \(K^\times=\pi^{\mathbf Z}\times U\), that completion is
\[
\widehat{K^\times}_{\,\mathrm{open}}
 \simeq\widehat{\mathbf Z}\times U.
\tag{11}
\]
This statement holds in both characteristic zero and characteristic \(p\).

**Proof.** Every finite level of \(K^{\mathrm{ur}}K_\pi\) is abelian, so that compositum lies in \(K^{\mathrm{ab}}\). Conversely let \(E/K\) be finite abelian. Lesson 6 proves its norm group is open, and finite reciprocity gives its finite index. As in Theorem 9.3 it contains some \(B_{d,n}\). Since this is the norm group of \(A=K_dK_{\pi,n}\), the reverse inclusion in the class field correspondence gives \(E\subset A\). Taking the union over \(E\) proves (9).

The kernels on the cofinal fields \(A\) are \(B_{d,n}\). Each is open, so the inverse-limit map (10) is continuous. If \(a=u\pi^r\) belongs to its kernel, its unramified action is trivial for every degree \(d\). Thus \(r\) is divisible by every positive integer, and \(r=0\). Its action on every \(T_n\) is then trivial, so \(u\in\bigcap_nU^{(n)}=\{1\}\). This proves injectivity.

Finite reciprocity is onto on each finite abelian field. Since finitely many conditions in the Galois topology can be combined in their finite compositum, every basic open subset of the inverse limit meets the image of \(K^\times\). The image is dense.

The \(B_{d,n}\) are cofinal among open finite-index subgroups, as already shown. Hence the required completion is
\[
\varprojlim_{d,n}K^\times/B_{d,n}
 \simeq\varprojlim_{d,n}
       \bigl((\mathbf Z/d\mathbf Z)\times U/U^{(n)}\bigr)
 \simeq\widehat{\mathbf Z}\times U.
\]
The last unit limit is \(U\) by the completeness argument in Corollary 8.5. The finite reciprocity isomorphisms commute with restriction, so their inverse limit is the asserted topological isomorphism with the Galois group. \(\square\)

Under the action coordinates
\(\operatorname{Gal}(K^{\mathrm{ur}}/K)\simeq\widehat{\mathbf Z}\) and
\(\operatorname{Gal}(K_\pi/K)\simeq U\), the map is
\[
u\pi^r\longmapsto(r,u^{-1}).
\tag{12}
\]
The chosen uniformizer fixes these coordinates. Equation (9) shows why the compositum is independent of that choice, even though \(K_\pi\) itself need not be.

In positive characteristic the word “open” in the completion is essential: one must use the local-field topology and its continuous finite quotients, rather than silently adding every abstract finite quotient. Formula (11) already uses the correct topology and requires no characteristic-zero restriction.

## 5. The local Kronecker–Weber theorem

### Corollary 9.5. Abelian extensions of \(\mathbf Q_p\)

Every finite abelian extension of \(\mathbf Q_p\) is contained in a cyclotomic extension, and
\[
\mathbf Q_p^{\mathrm{ab}}=\mathbf Q_p(\mu_\infty).
\tag{13}
\]
For \(a=up^r\), \(u\in\mathbf Z_p^\times\),
\[
(a,\mathbf Q_p(\zeta_{p^n})/\mathbf Q_p)(\zeta_{p^n})
 =\zeta_{p^n}^{\,u^{-1}\bmod p^n}.
\tag{14}
\]
On prime-to-\(p\) roots of unity the symbol acts by arithmetic Frobenius to the power \(r\).

**Proof.** The multiplicative Lubin–Tate module in lesson 8 gives
\[
(\mathbf Q_p)_p=\bigcup_n\mathbf Q_p(\zeta_{p^n}).
\]
The unramified tower is generated by the prime-to-\(p\) roots of unity: Corollary 3.1 of [Unramified and totally ramified extensions](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-07) constructs its degree-\(d\) field from the roots of order \(p^d-1\), and shows that every prime-to-\(p\) root lies in that tower. Theorem 9.4 now gives (13).

A finite extension contained in the union is generated by finitely many elements. Each lies in some finite field \(\mathbf Q_p(\zeta_{p^n},\zeta_m)\), \(p\nmid m\); taking a common \(n,m\) puts them in \(\mathbf Q_p(\zeta_{p^nm})\). Thus the assertion is containment in a finite cyclotomic field, not merely in an infinite union.

The inverse-unit action from Theorem 9.1 and the exponent description in lesson 8 give (14). On a root \(\zeta_m\) with \(p\nmid m\), arithmetic Frobenius is \(\zeta_m\mapsto\zeta_m^p\). Thus the symbol is \(\zeta_m\mapsto\zeta_m^{p^r\bmod m}\); for negative \(r\), the exponent uses the inverse of \(p\) modulo \(m\). \(\square\)

For example, \(p\) acts trivially on every \(\mathbf Q_p(\zeta_{p^n})\), while a unit \(u\) acts through its inverse residue modulo \(p^n\). The class field of \(\langle p\rangle(1+p\mathbf Z_p)\) is \(\mathbf Q_p(\zeta_p)\). When \(p=2\), that group is all of \(\mathbf Q_2^\times\), and the first field is simply \(\mathbf Q_2\), consistently with the degree formula.

## 6. Exercises and complete solutions

### Exercise 1 — easy

Compute the symbol on \(\mathbf Q_3(\zeta_9)\) for \(a=3,2,4,7\).

**Solution.** The valuation part \(3\) is trivial on the division field. The inverses of \(2,4,7\) modulo 9 are \(5,7,4\), respectively. Consequently the four symbols send \(\zeta_9\), in the displayed order, to
\[
\zeta_9,\qquad\zeta_9^5,\qquad\zeta_9^7,\qquad\zeta_9^4.
\]
These exponents all define automorphisms because they are units modulo 9.

### Exercise 2 — medium

Derive both norm equalities in Corollary 9.2 directly from the explicit symbol.

**Solution.** Write \(a=u\pi^r\). On \(K_{\pi,n}\), it is trivial if and only if \(u^{-1}\) is the identity scalar modulo \(\pi^n\), equivalently \(u\in U^{(n)}\). There is no restriction on \(r\), giving the kernel \(\langle\pi\rangle U^{(n)}\). On \(K_d\) it is trivial if and only if \(r\equiv0\pmod d\). Triviality on the compositum requires both conditions, giving \(\langle\pi^d\rangle U^{(n)}\). Each field is finite abelian, so its symbol kernel is its norm group by finite reciprocity.

### Exercise 3 — medium

Construct the class field of an arbitrary open subgroup \(H\) of finite index, and prove uniqueness among finite abelian extensions.

**Solution.** Choose \(U^{(n)}\subset H\), and choose \(d\) equal to the order of \(\pi H\) in the finite group \(K^\times/H\). Then \(B_{d,n}\subset H\). The explicit field \(A=K_dK_{\pi,n}\) has this norm group, so its reciprocity isomorphism takes \(H/B_{d,n}\) to a subgroup \(J\subset\operatorname{Gal}(A/K)\). For \(E=A^J\), the restriction of the symbol has kernel exactly \(H\), hence \(NE^\times=H\).

If \(E'\) is another finite abelian field with this kernel, the compositum norm group is the intersection \(H\cap H=H\), by Theorem 5.3. Therefore reciprocity gives
\([EE':K]=[E:K]=[E':K]=[K^\times:H]\).
The inclusions force \(EE'=E=E'\). This also shows that the construction does not depend on \(d,n\).

### Exercise 4 — hard

Compute Theorem 9.1 from the Frobenius-lift definition, explaining how the auxiliary prime belongs to its algebraic fixed field.

**Solution.** Fix \(L=K_{\pi,n}\), use \(f=\pi X+X^q\), and let \(\sigma=[u^{-1}]_f\) on its torsion. On \(M=LK^{\mathrm{ur}}\) choose the lift \(s=(\sigma,\varphi)\); its fixed field \(\Sigma\) has degree \(D_n\) and residue degree 1. Compare with the polynomial group for \(\pi'=u\pi\), obtaining \(\theta^\varphi=\theta[u]_f\) as in (4). For a primitive \(\lambda\), put \(y=\theta(\lambda)\).

The series converges in \(\widehat M\). Its value is primitive torsion for \(\pi'\), hence satisfies the separable polynomial \(f'^{\circ n}\). The complete Newton argument of the lemma descends it to \(M\). Equation (5) makes it fixed by \(s\), so it lies in \(\Sigma\). The degree of \(K(y)\) is \(D_n\), proving \(K(y)=\Sigma\); the polynomial norm calculation gives \(N_{\Sigma/K}(-y)=u\pi\).

The Frobenius-lift definition thus gives \(r_{L/K}(\sigma)=u\pi\) modulo norms. Since \(\pi=N_{L/K}(-\lambda)\), this class is \(u\). Inverting reciprocity gives \((u,L/K)=\sigma\), and the norm of \(\pi\) makes \((u\pi^r,L/K)=\sigma\) for every integer \(r\). On unramified fields the already proved symbol is \(\varphi^r\). Passing through all levels and transporting by the strict comparison for any other series gives the full formula.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The completed-ring Frobenius calculation and descent back to algebraic fields give the explicit unit action. The remaining sections prove local existence and the maximal abelian extension, with the sign conventions kept explicit.

- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
- [Teruyoshi Yoshida, Local class field theory via Lubin–Tate theory, arXiv:math/0606108v2](https://arxiv.org/abs/math/0606108v2).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.

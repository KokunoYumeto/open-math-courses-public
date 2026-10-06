# Homogeneous extensions and angular moments

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

A scaling law on punctured space need not survive extension through the origin. The obstruction is a finite list of angular moments. When it is nonzero, the constant term of a meromorphic family still gives an extension, but its scaling law acquires an explicit logarithmic point term.

We work with arbitrary angular distributions in every dimension \(n\ge1\). The accompanying [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5, construct the sphere test space and prove all radial Taylor estimates, the point-jet theorem, polar integration and the sphere constants. [Order, positivity and distributional limits](order-positivity-and-limits.md), Section 1, supplies finite-order estimates and the characterization of bounded compact-test sets. [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Theorems 2.1 and 3.1, supplies the smooth and continuous-field flux theorems. [Finite parts of singular powers](finite-parts-of-singular-powers.md) fixes the one-dimensional Laurent and symmetric finite-part normalizations, and proves meromorphic uniqueness from the supplied holomorphic identity theorem. All other proof inputs are included with those lessons.

## Separate scale from direction

Let \(X=\mathbb R^n\setminus\{0\}\), \(S=\mathbb S^{n-1}\), and \(a\in\mathbb C\). For a distribution on \(X\) or on \(\mathbb R^n\), put
\[
 \langle D_tu,\phi\rangle=t^{-n}\langle u,\phi(\cdot/t)\rangle,
 \qquad t>0.
 \tag{1.1}
\]
For a locally integrable function this represents \(u(tx)\), by affine substitution. We call \(u\) homogeneous of degree \(a\) if \(D_tu=t^au\), where \(t^a=e^{a\log t}\). Let \(E=\sum_jx_j\partial_j\).

For \(\phi\in\mathcal D(X)\), its radial average is
\[
 A_a\phi(\omega)=\int_0^\infty r^{a+n-1}\phi(r\omega)\,dr.
 \tag{1.2}
\]
All radii that can meet its support lie in a fixed compact interval inside \((0,\infty)\). Foundation A2 proves that this is a smooth sphere function and bounds each sphere seminorm by finitely many test derivatives. For \(n=1\) it means two integrals, one on each ray.

**Lemma 1.1 (scaling, Euler and radial averages).** For \(u\in\mathcal D'(X)\), the following conditions are equivalent: \(D_tu=t^au\) for every \(t>0\); \(Eu=au\); and \(u(\phi)=0\) whenever \(A_a\phi=0\). The first two conditions are also equivalent on \(\mathbb R^n\). Differentiation lowers the degree by one, and multiplication by a smooth homogeneous function of degree \(b\) adds \(b\).

**Proof.** On a compact interval of positive \(t\)'s, the tests in (1.1) have a common compact support in the appropriate domain. The chain rule and the fundamental theorem give their difference quotients and derivatives in every fixed test seminorm; the finite-order bound of \(u\) permits applying \(u\) to these limits. Differentiation yields
\[
 t\frac d{dt}\langle D_tu,\phi\rangle
       =\langle D_tEu,\phi\rangle.
 \tag{1.3}
\]
Indeed the derivative of \(t^{-n}\phi(x/t)\) is \(t^{-n-1}[-n\phi(x/t)-(x/t)\cdot\nabla\phi(x/t)]\), and \(-n-E\) is the test transpose of \(E\). A scaling law implies \(Eu=au\) at \(t=1\). Conversely the Euler equation makes the derivative of \(t^{-a}\langle D_tu,\phi\rangle\) zero; the fundamental theorem makes it constant. This works on either domain.

On \(X\), the Euler equation is exactly
\[
 u((a+n)\psi+E\psi)=0.
 \tag{1.4}
\]
The radial average of this test is the integral of
\(\partial_r[r^{a+n}\psi(r\omega)]\); both endpoints vanish. Thus annihilating zero radial averages implies (1.4). Conversely, if \(A_a\phi=0\), set
\[
 \psi(r\omega)=r^{-a-n}\int_0^r s^{a+n-1}\phi(s\omega)\,ds.
 \tag{1.5}
\]
It vanishes below the inner support radius and above the outer one, the latter because the full radial average is zero. On \(X\) it is smooth by differentiation under the integral on compact annuli, justified in A2. Hence it is a compact test. Direct radial differentiation gives \((a+n)\psi+E\psi=\phi\), so (1.4) implies \(u(\phi)=0\). Finally, differentiating the scaled test formula proves \(D_t\partial_j u=t^{-1}\partial_jD_tu\); for a smooth homogeneous multiplier \(h\), substitution gives \(D_t(hu)=t^b hD_tu\). These prove the degree rules. \(\square\)

An angular distribution is a continuous complex-linear form on the concrete \(C^\infty(S)\) of foundation A1. Its increasing seminorms \(q_m\) use the derivatives of \(g(x/|x|)\) on \(1/2\le|x|\le2\). Every such \(T\) satisfies \(|T(g)|\le Cq_m(g)\) for some finite \(m\).

**Theorem 1.2 (angular description).** Every degree-\(a\) distribution on \(X\) is uniquely
\[
 u(\phi)=T(A_a\phi)
 \tag{1.6}
\]
for an angular distribution \(T\). Conversely every angular distribution defines such a \(u\). Both correspondences are continuous for weak and strong dual topologies.

**Proof.** Choose \(h\in C_c^\infty(\mathbb R)\) with integral one; normalize a nonnegative nonzero bump by its positive integral. Define
\[
 \eta_a(r)=r^{-a-n}h(\log r),\qquad
 \int_0^\infty r^{a+n-1}\eta_a(r)\,dr=1.
 \tag{1.7}
\]
The last equality is the scalar substitution \(s=\log r\) on a compact positive interval. The test map \(g\mapsto\eta_a(|x|)g(x/|x|)\) is continuous and has one fixed compact annular support, by A2. Define \(T(g)\) by applying \(u\) to that test. The radial average of
\(\phi-\eta_a(|x|)A_a\phi(x/|x|)\) is zero, so Lemma 1.1 proves (1.6). Also \(A_a(\eta_a g)=g\). This proves uniqueness and independence of the normalized bump.

In the other direction, A2 bounds \(A_a\phi\) in every sphere seminorm for tests on any fixed compact subset of \(X\). Combining with the finite bound of \(T\) proves that (1.6) is a distribution. The endpoint computation in (1.4) proves its homogeneity.

For the topology assertion, the weak topology is evaluation on individual tests. The strong topology has seminorms \(\sup_{\phi\in B}|u(\phi)|\) over bounded test sets; on the sphere use the corresponding bounded sphere-test sets. The two correspondences are test transposes. The map \(A_a\) sends each bounded compact-test set to a set bounded in every \(q_m\), by A2 and U008, (T1). The map \(g\mapsto\eta_a g\) sends bounded sphere-test sets to bounded tests on its one fixed annulus, again by A2. Thus composing any strong seminorm with either transpose bounds it by an appropriate strong seminorm of the original dual. This proves both continuities, including on the homogeneous subspace. \(\square\)

If \(u(r\omega)=r^ag(\omega)\) with integrable angular density \(g\), polar formula (A14) shows that \(T(q)=\int_S gq\,d\sigma\). The same formula gives local integrability through zero when \(\operatorname{Re}a>-n\). No density is required in Theorem 1.2: \(T=\delta_{\omega_0}\), for example, produces a distribution on a single ray.

## A meromorphic radial integral isolates the origin

For a fixed angular distribution \(T\) and \(\operatorname{Re}z>-n\), define
\[
 W_z(T)(\phi)
 =T\left(\int_0^\infty r^{z+n-1}\phi(r\omega)\,dr\right),
 \qquad\phi\in\mathcal D(\mathbb R^n).
 \tag{2.1}
\]
The angular integral is smooth by A2: its derivatives are dominated at zero by an integrable power, and at infinity its radial range is bounded. Thus this is meaningful for every angular \(T\).

**Theorem 2.1 (radial continuation and residues).** The family extends meromorphically to every \(z\), with at most simple poles at \(z=-n-k\), \(k=0,1,\ldots\). Its residue at that point is
\[
 Q_k(T)=(-1)^k\sum_{|\alpha|=k}
       \frac{T(\omega^\alpha)}{\alpha!}\partial^\alpha\delta_0.
 \tag{2.2}
\]
Equivalently,
\[
 Q_k(T)(\phi)=T(P_k\phi),\qquad
 P_k\phi(\omega)=\sum_{|\alpha|=k}
       \frac{\partial^\alpha\phi(0)}{\alpha!}\omega^\alpha.
 \tag{2.3}
\]
All regular values and Laurent coefficients are distributions. On \(X\), this family is the angular representation (1.6) of degree \(z\).

**Proof.** Use the full multivariable Taylor formula A2 to write, for \(0\le r\le1\),
\[
 \phi(r\omega)=\sum_{j=0}^{M-1}r^jP_j\phi(\omega)
                      +R_M(r,\omega),\qquad M\ge1.
 \tag{2.4}
\]
Its differentiated integral remainder proves, for every angular derivative order \(q\),
\[
 q_q(R_M(r,\cdot))
       \le C_{M,q}r^M\|\phi\|_{C^{M+q}(\overline B(0,1))}.
 \tag{2.5}
\]
Thus the continued angular integral is
\[
 \begin{aligned}
 \mathcal A_z\phi={}&
     \int_0^1 r^{z+n-1}R_M(r,\omega)\,dr\\
 &+\int_1^\infty r^{z+n-1}\phi(r\omega)\,dr
       +\sum_{j=0}^{M-1}\frac{P_j\phi(\omega)}{z+n+j}.
 \end{aligned}
 \tag{2.6}
\]
On \(\operatorname{Re}z+n+M>0\), the first integral converges in every sphere seminorm. Each parameter derivative adds a logarithmic power. The formula
\(\int_0^1r^{c-1}|\log r|^l\,dr=l!/c^{l+1}\), proved in the gamma companion, gives a common bound on compact parameter subsets with \(c>0\). The second integral is over \(1\le r\le R\), where \(R\) bounds the test support, so it and all derivatives have uniform elementary bounds. The fundamental-theorem difference quotient in the complex parameter, dominated in each \(q_q\), proves the stated holomorphy before \(T\) acts.

Different \(M\)'s give the same expression in \(\operatorname{Re}z>-n\), by integrating the Taylor polynomial. The meromorphic identity principle of U016, applied after evaluation or any continuous sphere functional, extends equality on the overlaps. Taking arbitrarily large \(M\) covers the plane. Since \(|T(g)|\le Cq_q(g)\) for one finite \(q\), (2.5)–(2.6) also provide a finite derivative bound on each common compact test support. This proves that the regular values, parameter derivatives and Laurent coefficients define distributions. At \(z=-n-k\), take \(M>k\): only \(P_k\phi/(z+n+k)\) has a pole. Its coefficient is exactly (2.3), which is (2.2) by the sign convention for delta derivatives. Vanishing residue means that the displayed simple pole is removable.

For a test supported away from zero all Taylor coefficients at zero vanish, and its ordinary annular radial integral is entire. Therefore (2.6) restricts on \(X\) to (1.6), for every \(z\). \(\square\)

The radial kernel is precisely the one-dimensional meromorphic power \(U_{z+n-1}\) of U016. Indeed, for each \(\omega\), \(r\mapsto\phi(r\omega)\) is a smooth compact test on the full real line; in the initial half-plane its pairing with \(U_{z+n-1}\) is the integral here, and meromorphic uniqueness identifies the continuations. All \(\omega\)-derivatives have a common compact support in \(r\) and finite test bounds. Thus the resulting angular function is smooth, and its Laurent constant uses exactly U016's normalization, including the harmonic-number terms.

## Away from resonance the extension is unique

Call \(-n,-n-1,\ldots\) the resonant degrees.

**Theorem 3.1 (nonresonant extension).** For nonresonant \(a\), every degree-\(a\) distribution on \(X\) has a unique homogeneous extension \(\operatorname{Ext}_a u\) to \(\mathbb R^n\). This extension map is weakly and strongly continuous on the homogeneous subspace. If \(P\) is a homogeneous polynomial of degree \(m\ge0\), then
\[
 \operatorname{Ext}_{a+m}(Pu)=P\operatorname{Ext}_a u.
 \tag{3.1}
\]
If also \(a\ne1-n\), then
\[
 \operatorname{Ext}_{a-1}(\partial_j u)
       =\partial_j\operatorname{Ext}_a u.
 \tag{3.2}
\]

**Proof.** Take \(T\) from Theorem 1.2 and set \(\operatorname{Ext}_a u=W_a(T)\). Substitution \(r=ts\) in (2.1) proves
\[
 D_tW_z(T)=t^zW_z(T)
 \tag{3.3}
\]
in its initial region. The scalar meromorphic identity principle extends it to the plane. Since \(a\) is nonresonant, evaluating there proves homogeneity and Theorem 2.1 gives the required restriction.

The difference of two extensions is supported at zero. Foundation A3 writes it as a finite sum of independent point jets, with
\[
 E\partial^\alpha\delta_0=-(n+|\alpha|)\partial^\alpha\delta_0.
 \tag{3.4}
\]
Its Euler equation has coefficient \(-n-|\alpha|-a\ne0\) on each jet. Independence forces every coefficient to vanish.

At fixed nonresonant \(a\), (2.6) defines a continuous test map \(\phi\mapsto\mathcal A_a\phi\) into \(C^\infty(S)\). For a bounded set of compact tests, their supports lie in one compact and all derivatives are bounded, by U008. Estimate (2.5) then bounds every \(q_q\) of their images. The transpose \(T\mapsto W_a(T)\) is consequently continuous in both dual topologies, by the seminorm argument in Theorem 1.2. Composition with \(u\mapsto T\) proves the extension assertion.

The right side of (3.1) extends \(Pu\) and has degree \(a+m\). This is nonresonant: adding a nonnegative integer cannot turn a noninteger complex number into a resonant integer, nor turn an integer greater than \(-n\) into one. Uniqueness proves (3.1). Similarly the derivative extension has degree \(a-1\). For nonresonant \(a\), that degree is resonant exactly when \(a=1-n\); outside that one case uniqueness proves (3.2). \(\square\)

This includes \(\operatorname{Re}a>-n\) but is not limited to that half-plane, or to angular distributions given by functions.

## At resonance finitely many moments decide

At \(a=-n-k\), let \(F_{a,T}\) be the constant Laurent coefficient:
\[
 W_{a+w}(T)=\frac{Q_k(T)}w+F_{a,T}+O(w).
 \tag{4.1}
\]
It restricts to the original punctured distribution, whether or not the residue vanishes.

**Theorem 4.1 (obstruction and ambiguity).** The constant coefficient satisfies
\[
 \begin{aligned}
 D_tF_{a,T}&=t^a\bigl(F_{a,T}+(\log t)Q_k(T)\bigr),\\
 (E-a)F_{a,T}&=Q_k(T).
 \end{aligned}
 \tag{4.2}
\]
Every extension with the same logarithmic scaling law has the unique form
\[
 F_{a,T}+\sum_{|\alpha|=k}c_\alpha\partial^\alpha\delta_0.
 \tag{4.3}
\]
A homogeneous extension exists precisely when
\[
 T(\omega^\alpha)=0\quad\hbox{for all }|\alpha|=k.
 \tag{4.4}
\]
When this holds, (4.3) describes all homogeneous extensions. Constant-Laurent extensions commute with multiplication by a homogeneous polynomial, including shifts to a nonresonant degree.

**Proof.** Insert (4.1) and \(t^{a+w}=t^a(1+w\log t+O(w^2))\) in (3.3), then compare constant coefficients. This gives the first formula (4.2), with positive logarithmic sign. Differentiate it at \(t=1\) using the test-seminorm calculation of Lemma 1.1 to obtain the second.

Two extensions with that same law differ by a point-supported homogeneous distribution of degree \(a\). A3 and (3.4) leave exactly the jets of order \(k\), and each such jet does satisfy that law for the difference. This proves (4.3) and its uniqueness.

For an arbitrary correction supported at zero, A3 still gives only finitely many jets, of possibly different orders. On them,
\[
 (E-a)\partial^\alpha\delta_0
       =(k-|\alpha|)\partial^\alpha\delta_0.
 \tag{4.5}
\]
This is zero on order \(k\). By jet independence, other orders cannot cancel a nonzero order-\(k\) obstruction \(Q_k(T)\). Thus a homogeneous extension is impossible when that obstruction is nonzero. Formula (2.2) and independence say that its vanishing is precisely (4.4). If it vanishes, (4.2) gives a homogeneous extension and (4.3) gives all of them.

For a homogeneous polynomial \(P\) of degree \(m\), define \(PT\) by \((PT)(g)=T(P(\omega)g)\); this is continuous by A1. Directly in the initial integrals,
\[
 W_{z+m}(PT)=P W_z(T).
 \tag{4.6}
\]
Meromorphic uniqueness extends this equality. Constant coefficients at \(z=a\) prove the last assertion. At a regular point its constant is its ordinary value, so the formula also covers a shift out of resonance. \(\square\)

For a degree-\(-n\) distribution \(v\) on \(X\), choose a compact smooth \(\psi\) there such that
\[
 \int_0^\infty\psi(rx)\,\frac{dr}{r}=1
       \quad(x\ne0),\qquad S(v)=v(\psi).
 \tag{4.7}
\]
For example \(\psi(x)=h(\log|x|)\), with \(\int h=1\), has this property by translating the logarithmic variable. The difference of two choices has zero radial average at degree \(-n\), so Lemma 1.1 proves independence. Equivalently, \(S(v)=T_v(1)\). For a continuous homogeneous function, polar integration identifies its angular distribution and gives
\[
 S(v)=\int_S v(\omega)\,d\sigma(\omega).
 \tag{4.8}
\]
If \(u\) has degree \(-n-k\), its product with \(x^\alpha\), \(|\alpha|=k\), has degree \(-n\) and angular distribution \(\omega^\alpha T\), as is seen directly in (1.2). Hence
\[
 S(x^\alpha u)=T(\omega^\alpha).
 \tag{4.9}
\]
The obstruction is therefore intrinsic; no angular density or preferred annular test is needed. For \(u(x)=|x|^{-n}\), it is \(\sigma(S)\delta_0\ne0\), so every extension fails exact homogeneity.

## Parity removes the obstruction

Let \(\mathcal Ru(\phi)=u(\phi(-\cdot))\) and \((\mathcal RT)(g)=T(g(-\cdot))\).

**Theorem 5.1 (parity-preserving extension).** Suppose \(a=-n-k\), \(k\ge0\), and
\[
 \mathcal Ru=(-1)^{k+1}u\quad\hbox{on }X.
 \tag{5.1}
\]
Then all degree-\(k\) moments vanish and \(F_{a,T}\) is the unique homogeneous extension with this parity.

More generally, for any integer \(a\), put \(\ell=a+n-1\) and assume \(\mathcal Ru=(-1)^\ell u\). Define on the real line
\[
 p_\ell(r)=
 \begin{cases}
 r^\ell,&\ell\ge0,\\
 \operatorname{pf}(1/r^{-\ell}),&\ell<0.
 \end{cases}
 \tag{5.2}
\]
Then that unique parity-preserving homogeneous extension is
\[
 U(\phi)=\tfrac12T\bigl(\langle p_\ell(r),\phi(r\omega)\rangle\bigr).
 \tag{5.3}
\]
Equivalently, for \(x\ne0\) set \(K_\phi(x)=\langle p_\ell(r),\phi(rx)\rangle\). Then
\[
 U(\phi)=\tfrac12S(uK_\phi).
 \tag{5.4}
\]

**Proof.** Reflection commutes with the radial test maps, so Theorem 1.2 makes (5.1) equivalent to \(\mathcal RT=(-1)^{k+1}T\). But the monomial \(\omega^\alpha\) of degree \(k\) changes by \((-1)^k\). The two signs force each moment to be zero. The radial family and its constant coefficient preserve the parity of \(T\), so Theorem 4.1 gives the desired homogeneous extension. Any ambiguity is an order-\(k\) point jet, whose parity is \((-1)^k\) by A3. Opposite parity removes all of it.

For \(\ell<0\), put \(j=-\ell\ge1\), so \(k=j-1\). U016 proves \(p_\ell=F_j+(-1)^\ell\mathcal RF_j\). The sphere-valued pairing with the first term is smooth: the line tests \(\phi(r\omega)\) have a common compact support and vary smoothly in every test seminorm, by the chain rule and finite-order bound. The second term replaces \(\omega\) by \(-\omega\). Applying \(T\) and its parity makes its contribution equal to the first. Thus the factor \(1/2\) leaves precisely the positive-side Laurent constant \(F_{a,T}\), whose normalization was identified after Theorem 2.1.

If \(\ell\ge0\), split the ordinary line integral against \(r^\ell\) into positive and negative halves. The identical parity calculation again makes the halves equal after applying \(T\). Their half-sum is \(W_a(T)\), with \(a>-n\); Theorem 3.1 proves uniqueness. Every integer case is covered.

On any compact subset of \(X\), the tests \(r\mapsto\phi(rx)\) have one common compact support in \(r\); all their parameter derivatives converge in every line-test seminorm, by the chain rule and uniform continuity on the resulting compact set. Applying the finite-order distribution \(p_\ell\) proves that \(K_\phi\) is smooth. Its homogeneity follows from the scalar homogeneity of \(p_\ell\):
\(K_\phi(tx)=t^{-\ell-1}K_\phi(x)\).
Thus \(uK_\phi\) has degree \(a-\ell-1=-n\), and its angular total is \(T(K_\phi|_S)\). This proves (5.4). \(\square\)

The opposite-parity requirement is essential: the parity of order-\(k\) point jets would retain, rather than remove, the ambiguity in (4.3).

## Divergence recovers angular flux

**Theorem 6.1 (the point-source coefficient).** Suppose \(u_1,\ldots,u_n\in\mathcal D'(X)\) have degree \(1-n\), and \(\sum_j\partial_j u_j=0\) on \(X\). Let \(U_j\) be their unique homogeneous extensions. Then
\[
 \begin{aligned}
 \sum_j\partial_jU_j&=c\delta_0,\\
 c&=\sum_jS\left(\frac{x_j}{|x|^2}u_j\right).
 \end{aligned}
 \tag{6.1}
\]

**Proof.** Degree \(1-n\) is nonresonant. The extended divergence vanishes away from zero and has degree \(-n\). The point-jet theorem and (3.4) therefore leave only \(c\delta_0\). Choose a smooth compact radial test \(\phi(x)=\chi(|x|)\), with \(\chi=1\) near zero. Constancy near zero makes this smooth there. The annular function \(\psi(r)=-r\chi'(r)\) has \(\int_0^\infty\psi(r)\,dr/r=1\), by the fundamental theorem, and
\[
 -\partial_j\phi(x)=\psi(|x|)\frac{x_j}{|x|^2}.
 \tag{6.2}
\]
Thus
\[
 c=-\sum_j U_j(\partial_j\phi)
   =\sum_j u_j\left(\psi(|x|)\frac{x_j}{|x|^2}\right).
 \tag{6.3}
\]
Each multiplier \(x_j/|x|^2\) has degree \(-1\), so each product has degree \(-n\). Formula (4.7) identifies its pairing with the annular test as the corresponding term of (6.1). \(\square\)

**Corollary 6.2 (flux through any enclosing boundary).** Let \(v\) be a continuous degree-\(-n\) function on \(X\). If \(\Omega\) is a bounded open neighborhood of zero with compact \(C^1\) boundary, then
\[
 S(v)=\int_{\partial\Omega}v(x)x\cdot\nu(x)\,dS(x).
 \tag{6.4}
\]

**Proof.** By Lemma 1.1 the continuous vector field \(F(x)=v(x)x\) has weak divergence \(nv+Ev=0\) on \(X\); the distributional product rule follows by the ordinary product rule on tests. Remove a closed ball \(\overline B(0,\varepsilon)\subset\Omega\). Multiply \(F\) by a smooth compact cutoff equal to one near the closure of the remaining domain. U011, Theorem 3.1, applies to this continuous field with weak divergence zero in that domain. Its inner normal points toward zero, so its outer flux equals
\[
 \int_{|x|=\varepsilon}v(x)\varepsilon\,dS_\varepsilon(x)
   =\int_Sv(\omega)\,d\sigma(\omega)=S(v).
\]
Here (A12) and \(v(\varepsilon\omega)=\varepsilon^{-n}v(\omega)\) cancel every radial factor. The cutoff does not change either flux. For \(n=1\) use the ordinary endpoint fundamental theorem on each component of \(\Omega\setminus[-\varepsilon,\varepsilon]\); the continuous homogeneous field is constant on each half-line, and the same endpoint identity follows. \(\square\)

For \(u_j(x)=x_j/|x|^n\), direct differentiation makes the punctured divergence zero. Polar integration bounds the absolute value near zero by a constant times \(\int_0^\varepsilon1\,dr\), so the ordinary locally integrable field is its unique homogeneous extension. Summing the angular multipliers in (6.1) gives \(|x|^{-n}\). Hence
\[
 \operatorname{div}\frac{x}{|x|^n}=\sigma(S)\delta_0.
 \tag{6.5}
\]
Foundation A5 gives \(2\pi\) in dimension two and \(4\pi\) in dimension three; in dimension one it gives 2.

## Exercises

**Exercise 1 (intermediate: one ray).** In \(\mathbb R^2\), take \(T=\delta_{e_1}\). Give the initial integral for \(W_z(T)\), its residues at \(-3\) and \(-4\), and their values on tests with \(\partial_1\phi(0)=5\), respectively \(\partial_1^2\phi(0)=8\). Decide homogeneous extendibility.

**Exercise 2 (intermediate: radial resonance).** Let \(F\) be the Laurent-constant extension of \(|x|^{-3}\) in \(\mathbb R^3\). Compute \(D_2F\) and its pairing correction beyond \(2^{-3}F(\phi)\) when \(\phi(0)=3\).

**Exercise 3 (advanced: two weighted rays).** In \(\mathbb R^2\), take \(T=\delta_{e_1}+2\delta_{e_2}\) at degree \(-3\). Find the Euler obstruction, evaluate it at a test with gradient \((4,-1)\) at zero, and show that no point-supported correction removes it.

**Exercise 4 (advanced: even line extension).** Instead take \(T=\delta_{e_1}+\delta_{-e_1}\) at degree \(-3\). Express its unique even homogeneous extension using a one-dimensional symmetric finite part and a transverse delta. Give the ambiguity when evenness is not required.

**Exercise 5 (advanced: moving a resonance).** For \(n\ge2\), multiply \(F_{-n-2,T}\) by \(x_1^2\). Identify the resulting Laurent constant, compute \(x_1^2Q_2(T)\) directly, and evaluate its coefficient for ordinary surface integration on \(S^1\).

**Exercise 6 (intermediate: a missing divergence hypothesis).** For complex \(A,B\), let \(u=(Ax_1/|x|^2,Bx_2/|x|^2)\) on punctured \(\mathbb R^2\). Determine when its divergence vanishes there. In those cases compute the divergence after homogeneous extension, and explain what fails in the other cases.

**Exercise 7 (intermediate: elliptical flux).** Let \(v(r\omega)=r^{-2}(1+3\omega_1^2)\) in punctured \(\mathbb R^2\). Find the outward flux of \(v(x)x\) through \(x_1^2/4+x_2^2=1\). Show that different annular tests normalized as in (4.7) give the same angular total.

**Exercise 8 (advanced: merging angular atoms).** On \(S^1\), set \(\omega_j=(\cos(1/j),\sin(1/j))\) and \(T_j=j(\delta_{\omega_j}-\delta_{e_1})\). Prove strong convergence to angular differentiation at \(e_1\). At degree \(-5/2\), prove strong convergence of their extensions in \(\mathbb R^2\) and express the limit as a transverse derivative of a ray distribution, with its sign.

## Complete solutions

In the line formulas below, \(w(x_1)\otimes\delta_0(x_2)\) means the explicitly defined functional \(\phi\mapsto w(t\mapsto\phi(t,0))\). Restriction to this line sends tests on a fixed compact set to line tests on a fixed compact interval and bounds every derivative. Thus it defines a distribution whenever \(w\) does; no general tensor-product theorem is being assumed.

**Solution 1.** The initial pairing is \(\int_0^\infty r^{z+1}\phi(r,0)\,dr\). At \(-3=-2-1\) the residue is \(-\partial_1\delta_0\), whose pairing is \(5\). At \(-4=-2-2\) it is \(\partial_1^2\delta_0/2\), whose pairing is \(4\). The corresponding angular moments \(T(\omega_1)\) and \(T(\omega_1^2)\) are both 1. Theorem 4.1 therefore forbids homogeneous extension at both degrees, even though the Laurent constants supply nonhomogeneous extensions.

**Solution 2.** Here \(Q_0=4\pi\delta_0\), by (A15). Formula (4.2) gives
\[
 D_2F=2^{-3}\bigl(F+4\pi\log2\,\delta_0\bigr).
\]
The additional pairing is \(2^{-3}\cdot4\pi\log2\cdot3=(3\pi/2)\log2\), with positive sign. Adding a delta cannot remove it because a delta already has degree \(-3\).

**Solution 3.** Formula (2.2) gives \(Q_1=-\partial_1\delta_0-2\partial_2\delta_0\). It pairs as \(4+2(-1)=2\), and \((E+3)F_{-3,T}=Q_1\). An order-\(d\) point jet is multiplied by \(1-d\) under \(E+3\). This coefficient is zero for the two first derivatives in the obstruction. Jets of other orders are independent of them, by A3. Thus no finite point-supported correction cancels \(Q_1\).

**Solution 4.** The degree-one moments vanish because the two opposite atoms have equal weights. Their angular parity is even, the opposite of order-one point jets. The positive-side radial exponent is \(-2\); adding the equal opposite ray gives \(F_2+\mathcal RF_2=S_2\), with exactly U016's normalization. The unique even extension is therefore
\[
 \operatorname{pf}(1/x_1^2)\otimes\delta_0(x_2).
\]
Its degree is \(-2-1=-3\), as follows directly by applying (1.1) to the line-restriction definition above and scalar homogeneity. Without evenness, all additions \(c_1\partial_1\delta_0+c_2\partial_2\delta_0\) remain possible. Each has the required degree and odd parity, so the parity condition removes both.

**Solution 5.** The angular multiplier is \(\omega_1^2T\); (4.6) gives
\[
 x_1^2F_{-n-2,T}=F_{-n,\omega_1^2T}.
\]
On a test, \((x_1^2\partial_1^2\delta_0)(\phi)=\partial_1^2(x_1^2\phi)(0)=2\phi(0)\). Every other order-two jet is killed, because fewer than two \(x_1\)-derivatives leave a zero factor at the origin. The coefficient of \(\partial_1^2\delta_0\) in \(Q_2\) is \(T(\omega_1^2)/2\). Therefore \(x_1^2Q_2(T)=T(\omega_1^2)\delta_0\). For surface integration on \(S^1\), (A16) gives this moment as \(\pi\).

**Solution 6.** Differentiation off zero gives
\[
 \operatorname{div}u
       =\frac{(B-A)(x_1^2-x_2^2)}{|x|^4}.
\]
It vanishes everywhere there exactly when \(A=B\), as testing \(x=(1,0)\) shows necessity. In that case the field is \(Ax/|x|^2\), and (6.5) gives \(2\pi A\delta_0\). If \(A\ne B\), the extended divergence restricts to the displayed nonzero function on punctured space. It cannot consist only of a distribution supported at zero, so Theorem 6.1's point-source conclusion does not apply.

**Solution 7.** The angular integral is \(2\pi+3\pi=5\pi\), by (A16). The ellipse bounds a smooth neighborhood of zero, so Corollary 6.2 gives outward flux \(5\pi\). The difference of any two normalized annular tests has zero radial average at degree \(-2\); Lemma 1.1 annihilates it. Hence both tests give that same total without any radial assumption on the ellipse.

**Solution 8.** Write \(g_\circ(\theta)=g(\cos\theta,\sin\theta)\). The fundamental theorem gives
\[
 T_j(g)=j\int_0^{1/j}g_\circ'(s)\,ds,\qquad
 |T_j(g)-g_\circ'(0)|\le\frac{\|g_\circ''\|_\infty}{2j}.
\]
The chain rule bounds this second derivative by a constant times \(q_2(g)\). Thus the error tends to zero uniformly on every bounded sphere-test set: \(T_j\to T\) strongly, where \(T(g)=g_\circ'(0)\). The degree \(-5/2\) is nonresonant in dimension two, so the continuous transposes in Theorems 1.2 and 3.1 prove strong convergence of both punctured distributions and their extensions.

To identify the limit, use (2.6) with \(M=1\). The functional \(T\) annihilates the constant Taylor term. Differentiating \(\phi(r\cos\theta,r\sin\theta)\) at zero gives \(r\partial_2\phi(r,0)\). The subtracted expression, its parameter integral and this angular derivative have the bounds (2.5); hence the pairing is
\[
 \int_0^\infty r^{-1/2}\partial_2\phi(r,0)\,dr
 =\left\langle-\partial_2
       \bigl(x_{1,+}^{-1/2}\otimes\delta_0(x_2)\bigr),\phi\right\rangle.
\]
The integral is absolutely convergent at zero and has compact support at infinity. The minus sign compensates for the minus sign in a distributional derivative. Its degree is \(-1/2-1-1=-5/2\); its punctured restriction is the angular limit, and uniqueness confirms the extension.

## Programme proof locations and freely accessible sources

- [Angular tests, point jets and polar integration](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5: all sphere topology, bounded radial maps, full Taylor remainders, finite independent point jets, surface scaling, polar measure and constants.
- [Order, positivity and distributional limits](order-positivity-and-limits.md), Section 1; [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Theorems 2.1 and 3.1 and Corollary 2.4; [Finite parts of singular powers](finite-parts-of-singular-powers.md), meromorphic uniqueness and Proposition 5.1. The separately credited foundation selections retain their stated CC0 1.0 licences.
- [Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Theorem 4.19, Lemma 4.22 and Section 5.1: free point-support and homogeneous-extension proofs, the latter for \(\operatorname{Re}a>-n\). The complete arbitrary-degree, angular-distribution and exceptional-moment arguments are supplied above.
- [Michael E. Taylor, *Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*, author-hosted text](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), Section 8, especially (8.18), (8.25) and (8.38): freely accessible Taylor-subtraction constructions for smooth angular densities. Here the seminorm estimates prove the construction for arbitrary angular distributions, and (4.1) fixes the constant-Laurent normalization.

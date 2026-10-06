# The Weyl character formula for compact connected Lie groups

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

The integration formula and integer weight multiplicities turn an irreducible character into a single alternating orbit sum. To obtain every irreducible, one must also prove that the proposed quotients extend over singular torus points. We supply that cancellation step, including roots that are not primitive characters.

Let \(G\) be compact and connected, \(T\) a maximal torus, \(X=X^*(T)\) its analytic character lattice, and \(\Phi^+\) a positive system. We use [highest weights](RT-CPT-10.md), [Weyl integration](RT-CPT-08.md), torus conjugacy, and the complete character basis from lesson three. Simple-root and chamber facts are the root-system prerequisites already used in lessons seven and ten.

Write \(\rho=\frac12\sum_{\alpha>0}\alpha\), \(\epsilon(w)=\det(w|\mathfrak t)\), and \(e^\eta(H)=\exp(2\pi i\eta(H))\) on the real space \(\mathfrak t\). The invariant inner product identifies \(\mathfrak t^*\) with \(\mathfrak t\); \(\rho^\sharp\) denotes its dual vector. The Weyl group fixes central directions, so its determinant agrees with that on the root span.

## The shifted lattice and denominator

For an exponent \(\nu\), put
\[
A_\nu=\sum_{w\in W}\epsilon(w)e^{w\nu},\qquad
\delta=\prod_{\alpha>0}(1-e^{-\alpha}). \tag{1.1}
\]
Individual terms of \(A_\rho\) need not be functions on \(T\). However \(2\rho\in Q=\mathbb Z\Phi\subset X\), and \(w\rho-\rho\in Q\). Thus for \(\lambda\in X\)
\[
R_\lambda=e^{-\rho}A_{\lambda+\rho}
=\sum_w\epsilon(w)e^{w(\lambda+\rho)-\rho}\in\mathbb Z[X]. \tag{1.2}
\]
Every exponent on the right is an actual torus character. Formal orbit calculations can be carried out in the finite-rank lattice \(L=X+\mathbb Z\rho\subset\tfrac12X\), and then shifted back into \(X\). Equivalently the unshifted sums live on \(\mathfrak t\), or on the torus cover with period lattice \(\{\gamma\in\Lambda:\rho(\gamma)\in\mathbb Z\}\). This cover has degree two when \(\rho\notin X\).

**Theorem 1.3 (denominator identity).**
\[
A_\rho=e^\rho\delta
=\prod_{\alpha>0}(e^{\alpha/2}-e^{-\alpha/2}). \tag{1.4}
\]
The identity is formal in fractional exponentials and therefore also holds on \(\mathfrak t\). In particular \(|A_\rho|^2=|\delta|^2\) descends to \(T\).

*Proof.* Call the product \(D\). A simple reflection permutes the positive roots other than its own simple root and changes that root's sign. Consequently it negates \(D\); the simple reflections generate \(W\), so \(D\) is anti-invariant.

Its exponents lie in \(\rho+Q\), and are of the form
\(\rho-\sum_{\alpha\in S}\alpha\), where \(S\subset\Phi^+\). In any finite anti-invariant sum, coefficients on a regular Weyl orbit are signed copies of the coefficient at its unique dominant representative. A singular orbit has coefficient zero: its dominant representative lies on a simple reflection wall, and that reflection both fixes and negates its coefficient. Hence
\[
D=\sum_{\nu\text{ regular dominant}}c_\nu A_\nu.
\]
If \(c_\nu\neq0\), its dominant exponent occurs in \(D\), so \(\nu\leq\rho\). Its simple coroot pairings are positive integers, because \(\nu\in\rho+Q\). Therefore \(\mu=\nu-\rho\) is dominant and lies in the root span. But \(\nu\leq\rho\) writes \(\mu=-\sum_i m_i\alpha_i\), \(m_i\geq0\). Dominance gives
\((\mu,\rho)=\frac12\sum_{\alpha>0}(\mu,\alpha)\geq0\), whereas any nonzero such negative sum has \((\mu,\rho)<0\), since \((\rho,\alpha_i)=\|\alpha_i\|^2/2>0\). Thus \(\mu=0\).

Only the orbit of \(\rho\) remains. Its coefficient at \(e^\rho\) is one in \(D\): no nonempty positive subset can sum to zero. It is also one in \(A_\rho\), since \(\rho\) is regular and its stabilizer is trivial. Hence \(D=A_\rho\). For an empty root system, \(W\) is trivial and both sides are one. \(\square\)

## Fourier orthogonality forces the character formula

For dominant \(\lambda,\mu\in X\), the exponents in \(R_\lambda\) are distinct, and the supports of \(R_\lambda,R_\mu\) are disjoint unless \(\lambda=\mu\). Indeed \(\lambda+\rho\) is strictly dominant in the root directions, and distinct such dominant vectors have disjoint Weyl orbits, with central components unchanged. Torus Fourier orthogonality therefore gives
\[
\int_T R_\lambda\overline{R_\mu}\,dt
=|W|\delta_{\lambda\mu}. \tag{2.1}
\]
This uses actual exponents in \(X\), not orthogonality of fractional characters.

**Theorem 2.2 (character formula).** If an irreducible representation has highest weight \(\lambda\), then on regular \(H\in\mathfrak t\)
\[
\chi_\lambda(\exp H)=\frac{A_{\lambda+\rho}(H)}{A_\rho(H)}
=\frac{R_\lambda(\exp H)}{\delta(\exp H)}. \tag{2.3}
\]

*Proof.* The torus character \(\chi_\lambda=\sum_\eta m(\eta)e^\eta\) has nonnegative integer coefficients, is \(W\)-invariant, and has unique highest term \(e^\lambda\), with coefficient one. Its product with \(A_\rho\) is anti-invariant in the coset \(\rho+X\). Every regular dominant exponent \(\nu\) in that coset has \(\nu-\rho\in X\) dominant, since its positive integer simple pairings are at least one. The same orbit-coefficient argument as above gives a finite expansion
\[
\chi_\lambda A_\rho=\sum_{\mu\in X,\ \mu\text{ dominant}}c_\mu A_{\mu+\rho},
\qquad c_\mu\in\mathbb Z.
\]
After multiplying by \(e^{-\rho}\), (2.1), Schur orthogonality and normalized Weyl integration yield
\[
1=\int_G|\chi_\lambda|^2\,dg
=\frac1{|W|}\int_T|\chi_\lambda\delta|^2\,dt
=\sum_\mu |c_\mu|^2. \tag{2.4}
\]
Exactly one coefficient is \(1\) or \(-1\).

The product has highest term \(e^{\lambda+\rho}\), with coefficient one: all other character weights subtract a nonzero positive-root sum, and every other term of \(D=e^\rho\delta\) does likewise. Consequently \(c_\lambda=1\), so all other coefficients vanish. Dividing on the regular set proves (2.3). \(\square\)

## Cancellation and existence

**Lemma 3.1 (integral cancellation).** For every dominant \(\lambda\in X\), \(\delta\) divides \(R_\lambda\) in the Laurent ring \(\mathbb Z[X]\). The quotient \(q_\lambda\) is a \(W\)-invariant Laurent polynomial and extends to a continuous class function on \(G\).

*Proof.* Fix a positive root \(\alpha\), which may be nonprimitive in \(X\). On \(\ker\chi_\alpha\subset T\), its reflection fixes every torus point: for each \(\eta\in X\), \(s_\alpha\eta-\eta\) is an integer multiple of \(\alpha\). The transformation rule from (1.2) is
\[
s_\alpha R_\lambda=-e^{\rho-s_\alpha\rho}R_\lambda.
\]
Here \(\rho-s_\alpha\rho=\langle\rho,\alpha^\vee\rangle\alpha\), with integer pairing. On that kernel the factor is one, so \(R_\lambda=-R_\lambda\), and \(R_\lambda\) vanishes.

Write \(\alpha=d\beta\), with \(\beta\) primitive in \(X\). Extend \(\beta\) to an integer basis of \(X\), and use \(z=e^\beta\) as its first Laurent variable. The kernel contains all points with \(z^d=1\) and arbitrary remaining unit-circle coordinates. After a monomial shift, divide by the monic polynomial \(z^d-1\). The remainder has degree less than \(d\). At every choice of the other circle coordinates it vanishes at all \(d\) distinct roots of unity, so is zero. Its coefficient Laurent polynomials are zero by torus Fourier independence. Monic division was over the integer Laurent ring, so \(1-e^{-\alpha}\) divides \(R_\lambda\) integrally.

The factors for distinct positive roots are pairwise coprime. To check this even for nonprimitive roots, work first over \(\mathbb C\): the factors for \(d\beta\) are \(e^\beta-\zeta\), with \(\zeta^d=1\); these are prime after a primitive basis change. Two such factors can be associates only when their primitive exponent directions agree up to sign. Distinct positive roots in a reduced root system are not parallel. Thus no factors are shared over \(\mathbb C\). The integer factors are primitive, so no integer prime is shared either, and they are coprime in the UFD \(\mathbb Z[X]\). Their product divides \(R_\lambda\).

The quotient is \(A_{\lambda+\rho}/A_\rho\) on the regular set. Both numerator and denominator have the same Weyl sign, making the quotient invariant there, and the Laurent identity extends invariance everywhere. Torus conjugacy identifies continuous \(W\)-invariant torus functions with continuous class functions. \(\square\)

**Theorem 3.2 (existence).** Every dominant \(\lambda\in X^*(T)\) is the highest weight of an irreducible representation.

*Proof.* Lemma 3.1 supplies genuine continuous class functions \(q_\lambda\), with no singularities left. Weyl integration and (2.1) give
\[
\langle q_\lambda,q_\mu\rangle_{L^2(G)}=\delta_{\lambda\mu}. \tag{3.3}
\]
The preceding highest-weight theorem assigns a dominant analytic weight to every existing irreducible, and Theorem 2.2 identifies its character with the corresponding \(q_\mu\). If a proposed \(\lambda\) did not occur, (3.3) would make \(q_\lambda\) orthogonal to every irreducible character. Completeness of that class-function basis would force \(q_\lambda=0\) in \(L^2(G)\), contradicting its norm one. Hence it occurs; uniqueness from its weight was already proved. It follows also that the \(q_\lambda\)'s form the complete character basis. \(\square\)

This completes general compact existence without assuming the Lie-algebra existence theorem or using an expression undefined on singular torus points.

## Dimension and classical specializations

**Corollary 4.1 (dimension formula).**
\[
\dim V_\lambda=\prod_{\alpha>0}
\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)}
=\prod_{\alpha>0}
\frac{\langle\lambda+\rho,\alpha^\vee\rangle}
{\langle\rho,\alpha^\vee\rangle}. \tag{4.2}
\]

*Proof.* Weyl invariance of the inner product, replacing \(w\) by \(w^{-1}\), gives
\[
A_{\lambda+\rho}(t\rho^\sharp)=A_\rho(t(\lambda+\rho)^\sharp).
\]
Use the denominator identity in numerator and denominator:
\[
q_\lambda(\exp(t\rho^\sharp))
=\prod_{\alpha>0}
\frac{\sin(\pi t(\lambda+\rho,\alpha))}
{\sin(\pi t(\rho,\alpha))}.
\]
All denominator pairings are positive. Taking \(t\to0\) gives (4.2), by continuous cancellation and \(\sin u/u\to1\). The character at the identity is the dimension. Coroot rescaling cancels separately in each factor. For a torus the products are empty and the irreducibles have dimension one. Central components do not affect any root pairing. \(\square\)

For \(SU(3)\), write \(\lambda=a\omega_1+b\omega_2\), \(a,b\geq0\). The three positive coroots give
\[
\dim V_{a,b}=\frac{(a+1)(b+1)(a+b+2)}2.
\]
Labels \((0,0),(1,0),(0,1),(2,0),(1,1),(3,0)\) give dimensions \(1,3,3,6,8,10\); the two dimension-three representations are dual.

For the classical signed-root systems, put \(x_i=\lambda_i+r_i\). Grouping roots \(e_i-e_j\) and \(e_i+e_j\) gives the following explicit formulas.

| Group or Lie type | \((r_1,\ldots,r_r)=\rho\) | Dimension |
| --- | --- | --- |
| \(Sp(r)=USp(2r)\), type \(C_r\) | \((r,r-1,\ldots,1)\) | \(\displaystyle\prod_i\frac{x_i}{r_i}\prod_{i<j}\frac{x_i^2-x_j^2}{r_i^2-r_j^2}\) |
| \(SO(2r+1)\) or its spin cover, type \(B_r\) | \((r-\tfrac12,r-\tfrac32,\ldots,\tfrac12)\) | \(\displaystyle\prod_i\frac{x_i}{r_i}\prod_{i<j}\frac{x_i^2-x_j^2}{r_i^2-r_j^2}\) |
| \(SO(2r)\) or its spin cover, type \(D_r\), \(r\geq2\) | \((r-1,r-2,\ldots,0)\) | \(\displaystyle\prod_{i<j}\frac{x_i^2-x_j^2}{r_i^2-r_j^2}\) |

These formulas follow directly from the roots: type \(C\) has \(2e_i\), type \(B\) has \(e_i\), and type \(D\) has neither. Thus type \(D\) has no individual factor with zero denominator \(r_r=0\). For \(Sp(r)\) the dominant labels are decreasing nonnegative integers. The \(SO\) torus requires integer coordinates. Spin labels can also have uniformly half-integral coordinates; type \(B\) dominance ends at \(\lambda_r\geq0\), and type \(D\) at \(\lambda_{r-1}\geq|\lambda_r|\). Half-integral representations must not be called representations of \(SO\).

For the type \(B_r\) spin weight \((\tfrac12,\ldots,\tfrac12)\), index the coordinates by \(k=1,\ldots,r\), so \(x_k=k\), \(r_k=k-\tfrac12\). The product becomes
\[
\prod_{k=1}^r\frac{k}{k-\tfrac12}
\prod_{k=2}^r\prod_{\ell=1}^{k-1}\frac{k+\ell}{k+\ell-1}
=\prod_{k=1}^r\frac{k}{k-\tfrac12}
\prod_{k=2}^r\frac{2k-1}{k}
=2^r. \tag{4.3}
\]
This agrees with the explicit spin module in lesson ten.

For \(G_2\), choose simple roots \(\alpha_1\) short and \(\alpha_2\) long, with squared lengths \(2,6\) and \((\alpha_1,\alpha_2)=-3\). The positive roots have coordinate pairs
\((1,0),(0,1),(1,1),(2,1),(3,1),(3,2)\).
Their coroot coordinate pairs are
\((1,0),(0,1),(1,3),(2,3),(1,1),(1,2)\).
Consequently
\[
\dim V_{a,b}=
\frac{(a+1)(b+1)(a+b+2)(a+2b+3)(a+3b+4)(2a+3b+5)}{120}. \tag{4.4}
\]
The Cartan determinant is one, so \(Q=P\), and \(Q\subset X\subset P\) makes every such dominant label analytic. The fundamental dimensions are \(7\) and \(14\); the latter is the adjoint. The octonion-derivation construction belongs to **RT-LIE-12** and is not used in this dimension computation.

## Computing every weight multiplicity

The proof above determines the character without a weight-multiplicity recursion. Two useful formulas follow from the character and Casimir identities. The complete algebraic proofs in [**RT-LIE-16**, Theorems 4.1 and 5.1](course:RT-LIE/RT-LIE-16#4-kostant-s-coefficient-formula) give the semisimple counterpart. We supply the compact version, retaining its central directions and arbitrary invariant metric. If \(m_\lambda(\mu)\) is the multiplicity, set it to zero outside the finite weight set. Freudenthal's identity is
\[
\begin{aligned}
&\bigl(\|\lambda+\rho\|^2-\|\mu+\rho\|^2\bigr)m_\lambda(\mu)\\
&\qquad=2\sum_{\alpha>0}\sum_{k\geq1}
(\mu+k\alpha,\alpha)m_\lambda(\mu+k\alpha).
\end{aligned}
\]
The sum is finite under the stated convention. For Kostant's formula, let \(\mathcal P(\beta)\) count the nonnegative integer tuples \((n_\alpha)_{\alpha>0}\) with \(\beta=\sum_{\alpha>0}n_\alpha\alpha\), and put it to zero when no such tuple exists. Then
\[
m_\lambda(\mu)
=\sum_{w\in W}\epsilon(w)\,
\mathcal P\bigl(w(\lambda+\rho)-(\mu+\rho)\bigr).
\]
*Proof of the two formulas.* Kostant's formula follows by multiplying the numerator in (2.3) by
\[
\prod_{\alpha>0}(1-e^{-\alpha})^{-1}
=\sum_\beta\mathcal P(\beta)e^{-\beta}
\]
and comparing the coefficient of \(e^\mu\). For any fixed positive-cone height, each exponent has finitely many partitions, so the formal product and coefficient extraction are defined. The finite Weyl sum then gives the stated formula, including zero outside the finite weight set. All shifted exponents return to the actual character lattice as in (1.2).

For Freudenthal, choose any invariant positive metric \(B\) used for the displayed weight norm. For real \(X\in\mathfrak t\), put \(H_X=X/(2\pi i)\) in the complexified algebra, so its eigenvalue on a weight vector is \(\mu(X)\). Extend \(B\) complex bilinearly and use the invariant form \(\kappa=-4\pi^2 B\). Then \(\kappa(H_X,H_Y)=B(X,Y)\). Choose root vectors with \(\kappa(E_\alpha,F_\alpha)=1\). Invariance gives \([E_\alpha,F_\alpha]=H_{\alpha^\sharp}\). A basis and its \(\kappa\)-dual define a central quadratic element: the infinitesimal action on the two tensor factors cancels, by invariance of the form. Ordering the opposite root factors writes that element as
\[
\Omega=\sum_a H_a^2+2\sum_{\alpha>0}F_\alpha E_\alpha+2H_{\rho^\sharp},
\]
where \(H_a=H_{X_a}\) for a \(B\)-orthonormal torus basis. On a highest vector this has eigenvalue \((\lambda,\lambda+2\rho)\), since the positive root factors kill it. It commutes with the group, by the same invariant-dual-basis construction, so Schur's lemma makes that its scalar everywhere.

Write \(T_\alpha(\mu)=\operatorname{tr}_{V_\mu}(F_\alpha E_\alpha)\). Taking the trace of the last identity on \(V_\mu\) gives
\[
\bigl(\|\lambda+\rho\|^2-\|\mu+\rho\|^2\bigr)m_\lambda(\mu)
=2\sum_{\alpha>0}T_\alpha(\mu).
\]
For maps between finite-dimensional spaces, \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\), even when their source spaces differ; both expressions sum the same matrix-entry products. Apply this to the raising and lowering maps between \(V_\mu\) and \(V_{\mu+\alpha}\). The bracket relation yields
\[
T_\alpha(\mu)=T_\alpha(\mu+\alpha)
+(\mu+\alpha,\alpha)m_\lambda(\mu+\alpha).
\]
Iterate until the weight space is zero, which happens because there are only finitely many weights. Substitution proves Freudenthal's formula at every \(\mu\), including a zero-dimensional weight space. This proof includes the central Cartan operators; they have no root contribution. Thus no semisimplicity, simple-group normalization, or division by a potentially zero recursion denominator was assumed. \(\square\)

## Exercises with complete solutions

**Exercise 1 (easy).** Recover the unitary character formula of lesson nine.

*Solution.* For \(U(n)\), roots are \(e_i-e_j\), \(i<j\), and
\(\rho_i=(n+1-2i)/2\). Let \(c=(n-1)/2\) and \(\delta_0=(n-1,n-2,\ldots,0)\); then \(\rho=\delta_0-c(1,\ldots,1)\). The Weyl group is \(S_n\), so its alternating sums are determinants. Both contain the same formal monomial \(e^{-c\sum_i e_i}\), which cancels, leaving
\[
\chi_\lambda(z)=
\frac{\det[z_j^{\lambda_i+n-i}]_{i,j=1}^n}
{\det[z_j^{n-i}]_{i,j=1}^n}.
\]
The last expression uses only integer exponents, remains valid for negative labels, and is the earlier bialternant. The cancellation lemma extends it across repeated eigenvalues. The general existence theorem realizes every decreasing integer tuple, reproducing the full classification.

**Exercise 2 (medium).** Derive the \(SU(3)\) dimension formula.

*Solution.* The positive roots are \(\alpha_1,\alpha_2,\alpha_1+\alpha_2\), all of the same length. Their coroots are \(\alpha_1^\vee,\alpha_2^\vee,\alpha_1^\vee+\alpha_2^\vee\). Since \(\rho=\omega_1+\omega_2\), the three denominator pairings are \(1,1,2\); the numerator pairings are \(a+1,b+1,a+b+2\). Their product ratio is precisely \((a+1)(b+1)(a+b+2)/2\). Substitution yields \(1,3,3,6,8,10\) for the six labels listed above. Interchanging \(a,b\) gives the same dimension and interchanges defining and dual representations.

**Exercise 3 (medium).** Match the rank-two symplectic and orthogonal fundamental dimensions.

*Solution.* For \(Sp(2)\), \(\rho=(2,1)\). Its weights \((1,0)\) and \((1,1)\) give respectively
\[
\frac32\frac{9-1}{4-1}=4,\qquad
\frac32\cdot2\frac{9-4}{4-1}=5.
\]
For type \(B_2\), \(\rho=(\tfrac32,\tfrac12)\). The defining weight \((1,0)\) gives
\[
\frac53\cdot1\frac{25/4-1/4}{9/4-1/4}=5.
\]
The spin weight \((\tfrac12,\tfrac12)\) gives
\[
\frac43\cdot2\frac{4-1}{9/4-1/4}=4.
\]
The five-dimensional symplectic primitive exterior-square representation has trivial action of the center \(-I\). To verify the quotient identification, let \(J\) be the antiunitary quaternionic structure on \(\mathbb C^4\), so \(J^2=-1\) and \(Sp(2)\) commutes with \(J\). The induced \(\Lambda^2J\) squares to one. Its fixed vectors form a real six-dimensional space with an invariant positive inner product. The invariant symplectic line is stable under this real structure; its orthogonal complement is a real five-dimensional representation. Connectedness puts its image in \(SO(5)\).

If \(g\) acts trivially on that complement, it also acts trivially on the invariant line, hence on \(\Lambda^2\mathbb C^4\). Diagonalizing the unitary \(g\), all pairwise products of its four eigenvalues equal one. Comparing pairs shows that all eigenvalues are the same, and their common square is one. Thus the kernel is exactly \(\{\pm I\}\). The differential is injective, and \(\dim Sp(2)=\dim SO(5)=10\); consequently its compact image is both open and closed in connected \(SO(5)\), hence is all of \(SO(5)\). This proves the quotient identification and the defining-representation match.

Under the \(C_2\)-to-\(B_2\) root-coordinate identification
\[
(c_1,c_2)\longmapsto
\left(\frac{c_1+c_2}{2},\frac{c_1-c_2}{2}\right),
\]
the symplectic defining weight \((1,0)\) becomes the spin weight \((\tfrac12,\tfrac12)\), while \((1,1)\) becomes the orthogonal defining weight \((1,0)\). The four-dimensional representation has central value \(-I\) and cannot descend to \(SO(5)\). Thus the fundamental dimension comparison is \(4\leftrightarrow4\), \(5\leftrightarrow5\), while only the latter passes to the quotient. The next integral \(B_2\) weight \((1,1)\), twice the spin weight, gives dimension ten, not four.

**Exercise 4 (hard).** Prove the denominator identity without assuming the character formula.

*Solution.* The product \(e^\rho\prod_{\alpha>0}(1-e^{-\alpha})\) is negated by every simple reflection, using the permutation of the other positive roots. Thus it is anti-invariant. Expand it in formal exponentials. Singular dominant exponents have zero coefficients because a wall reflection fixes the exponent and negates the coefficient; regular dominant exponents collect into signed Weyl orbit sums.

Every occurring exponent lies below \(\rho\) and in \(\rho+Q\). If \(\nu\) is dominant regular, its integral simple pairings are at least one, so \(\nu-\rho\) is dominant. It also is a nonpositive integral simple-root sum. Pairing with \(\rho\) is nonnegative by dominance and negative for a nonzero such sum, forcing \(\nu=\rho\). There is therefore just the orbit sum \(cA_\rho\). The coefficient at the highest exponent \(e^\rho\) in the product is one, because a nonempty positive subset has positive evaluation on a chamber vector. Its coefficient in \(A_\rho\) is one, because the stabilizer of \(\rho\) is trivial. Thus \(c=1\). This proof uses root-system facts and coefficient comparison after establishing that the quotient is constant; it does not invoke character existence.

## Source comparisons and normalization

Milne Section 22d, especially Theorem 22.52, compares the formula with line-bundle cohomology and vanishing. In positive characteristic it gives the character of the global-section module, which need not be simple; the irreducible interpretation requires characteristic zero. Milne also explains adjoining half-characters when \(\rho\notin X\). Our shifted Laurent sums instead keep the actual analytic lattice visible throughout.

Deligne–de Man, *La série exceptionnelle de groupes de Lie II* uses the form inverse to the Killing form, with longest-root square \(1/h^\vee\). Relative to the convention of longest-root square two, it is scaled by \(1/(2h^\vee)\). Their measure is
\[
M(\eta)=\sum_{\alpha>0}\delta_{\,12(\eta,\alpha)_{\rm can}},\qquad
L(\lambda)=M(\lambda+\rho)-M(\rho).
\]
If \(L(\lambda)=\sum_q m(q)\delta_q\), their formulas (1)–(2) express
\(\dim V_\lambda=\prod_q q^{m(q)}\). The equal numbers of numerator and denominator factors cancel both the factor twelve and the form scaling, giving exactly (4.2). For \(G_2\), \(h^\vee=4\), so the canonical form is one eighth of a long-root-square-two form. In the coordinates used for (4.4), the long-root square is six, so the canonical form is instead one twenty-fourth of that displayed form. This comparison concerns ordinary simple groups; no supergroup dimension formula or interpolation theorem is imported.

## What this lesson does not prove

The compact highest-weight theorem, normalized integration formula, complete character basis and torus conjugacy are the results of lessons ten, eight, three and six. The root-system facts used above are the simple-root expansion, Weyl chamber orbit representatives, simple-reflection permutation of the other positive roots, and \(\langle\rho,\alpha_i^\vee\rangle=1\), as in [**RT-LIE-08**, §§2–5](course:RT-LIE/RT-LIE-08#5-simple-transitivity-and-the-longest-element) and lesson ten. The classical root lists are computed in lesson seven, and the \(G_2\) root system is the rank-two model in [**RT-LIE-08**, §6](course:RT-LIE/RT-LIE-08#6-all-rank-two-systems). The spin construction is given in lesson ten. Freudenthal's and Kostant's formulas have complete proofs above; RT-LIE-16 supplies the semisimple algebraic comparison. Milne's line-bundle interpretation and the exceptional-series interpolation of Deligne–de Man are comparisons only.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §27. Its Verma/Casimir argument is an alternative character proof. Kostant multiplicities are posed there as an exercise. Both multiplicity identities are proved above with compact central directions and arbitrary invariant metrics, rather than importing that exercise as a proof.

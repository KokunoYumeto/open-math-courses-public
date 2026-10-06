# Homogeneous spaces, induced representations and Gelfand pairs

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

Choosing an observation point in a space with symmetry also chooses its stabilizer. Functions on that space are the group functions that ignore motion inside this stabilizer. In Peter–Weyl coordinates, ignoring those motions is an orthogonal projection on each finite coefficient space. This turns the geometric question “which modes can be observed here?” into a fixed-vector calculation.

We first perform that compression for scalar functions. It gives the multiplicity formula and the criterion for commuting invariant filters. A finite permutation space makes both statements concrete. We then allow vector values with a prescribed stabilizer action; a circle example shows how this changes the permitted frequencies, and full Frobenius reciprocity identifies all multiplicity spaces. Finally, on spheres the scalar compression produces harmonic polynomials and normalized Gegenbauer coefficients.

Throughout, \(G\) is compact Hausdorff and \(K\) is closed. Haar measures have mass one and inner products are linear in the first variable. We use [Peter–Weyl and coefficient orthogonality](RT-CPT-02.md) and the [Fourier convention](RT-CPT-03.md)
\[
\widehat f(\pi)=\int_G f(g)\pi(g)^*\,dg,\qquad
(f*h)(g)=\int_G f(x)h(x^{-1}g)\,dx.
\tag{1.1}
\]
Thus \(\widehat{f*h}(\pi)=\widehat h(\pi)\widehat f(\pi)\). No countability assumption on \(G\) is imposed.

## Quotient measure and invariant functions

The space \(G/K\) is compact Hausdorff: the equivalence relation \(xK=yK\) is closed, since \(x^{-1}y\in K\). Let \(q:G\to G/K\) be its quotient map and let \(\mu=q_*dg\). It is a \(G\)-invariant probability measure with full support. Indeed, inverse images of nonempty open sets are nonempty open subsets of \(G\), and such sets have positive Haar measure.

**Proposition 1.2 (compact Weil formula).** This is the unique invariant probability measure on \(G/K\), and for \(f\in C(G)\),
\[
\int_G f(g)\,dg
=\int_{G/K}\int_K f(gk)\,dk\,d\mu(gK).
\tag{1.3}
\]
Pullback by \(q\) identifies \(L^2(G/K,\mu)\) unitarily with the right-\(K\)-fixed subspace of \(L^2(G)\).

*Proof.* The inner integral is continuous and right-\(K\)-invariant, so descends to the quotient. By the definition of \(\mu\), the right side is \(\int_G\int_Kf(gk)\,dk\,dg=\int_Gf(g)\,dg\), using Fubini and right invariance.

If \(\nu\) is another invariant probability measure and \(u\in C(G/K)\), invariance gives
\[
\int u\,d\nu
=\int_{G/K}\int_Gu(xgK)\,dx\,d\nu(gK).
\]
The inner integral equals \(\int_Gu(xK)\,dx\), independently of \(gK\), by right Haar invariance. Thus \(\nu=\mu\).

Pullback is an isometry by the pushforward definition. On \(L^2(G)\), the operator
\[
P_Kf=\int_K R_kf\,dk,\qquad R_kf(g)=f(gk),
\tag{1.4}
\]
is the orthogonal projection onto the common fixed space of the \(R_k\)'s: Haar averaging is self-adjoint, idempotent and fixes exactly the fixed vectors. Strong continuity of right translations makes the vector integral legitimate. Averaging continuous approximants shows that its range is the \(L^2\) closure of the continuous right-invariant functions. Those are exactly pullbacks of \(C(G/K)\), which is dense in \(L^2(G/K,\mu)\). Hence the closed isometric image of pullback is precisely that range. All fixed-space equalities refer to \(L^2\) classes. \(\square\)

For compact abelian groups, [**HA-LCA-10, Theorem 4.1**](course:HA-LCA/HA-LCA-10#section-4) proves the general subgroup–quotient Weil formula, with compatible Haar measures. Equation (1.3) proves the compact case here, including nonnormal \(K\); no quotient group is required.

## Compressing a coefficient space to an observation space

Write a coefficient in the form
\[
f_{v,\ell}(g)=\ell(\pi(g^{-1})v),\qquad v\in V_\pi,\quad\ell\in V_\pi^*.
\]
Then \(L_xf_{v,\ell}=f_{\pi(x)v,\ell}\), while \(R_kf_{v,\ell}=f_{v,\pi^*(k)\ell}\). The coefficient basis from lesson 2, with its \(\sqrt{d_\pi}\) normalization, identifies the \(\pi\)-type for the left action with \(V_\pi\otimes V_\pi^*\). Averaging the right \(K\) action therefore preserves the first factor and projects the second onto \((V_\pi^*)^K\). Proposition 1.2 identifies the range of this average with \(L^2(G/K)\), so
\[
L^2(G/K)\simeq
\widehat{\bigoplus}_{\pi\in\widehat G}
V_\pi\otimes(V_\pi^*)^K,\qquad
\operatorname{mult}(\pi,L^2(G/K))=\dim V_\pi^K.
\tag{2.5}
\]
The last equality follows from the antilinear Riesz identification of \(V_\pi\) with its dual, which preserves fixed vectors for a unitary action. Projection on each block extends to the full Hilbert sum by boundedness and finite-sum density. This proves the formula without evaluating arbitrary \(L^2\) functions and without choosing one exceptional null set for all of \(K\).

There are two limiting cases worth checking. If \(K=\{1\}\), every dual vector survives and the regular multiplicity is \(d_\pi\). If \(K=G\), only the trivial type survives and the quotient is a point. For a general stabilizer, multiplicities can decrease to zero, but cannot exceed the regular multiplicity. A space is **multiplicity free** when each surviving type has multiplicity one.

## Commutativity and spherical functions

Let \(\mathcal A=C(K\backslash G/K)\) be the continuous functions invariant under both left and right multiplication by \(K\), with convolution (1.1). The integral triangle inequality makes it a Banach algebra in the supremum norm, since \(\|f*h\|_\infty\leq\|f\|_\infty\|h\|_\infty\). It usually has no identity.

**Theorem 3.1.** The following are equivalent:

1. \(L^2(G/K)\) is multiplicity free.
2. \(\dim V_\pi^K\leq1\) for every irreducible \(\pi\).
3. \(\mathcal A\) is commutative.

A pair with these properties is a **Gelfand pair**. Multiplicity free allows irreducibles to occur zero times.

*Proof.* Equivalence of the first two statements is (2.5). Put \(p_\pi=\int_K\pi(k)\,dk\), the orthogonal projection onto \(V_\pi^K\). The Fourier transform of any bi-invariant \(f\) satisfies
\[
\widehat f(\pi)=p_\pi\widehat f(\pi)p_\pi.
\tag{3.2}
\]
This follows by substituting left and right \(K\)-translations into (1.1). Conversely these equalities for all \(\pi\) imply both invariances, by Fourier injectivity.

Every matrix on \(V_\pi^K\), extended by zero on its orthogonal complement, is the Fourier block of a continuous bi-invariant coefficient function: the inversion function \(d_\pi\operatorname{tr}(B\pi(g))\) has precisely that block and all other blocks zero, by coefficient orthogonality. Consequently if a fixed space has dimension at least two, two noncommuting matrix units supply noncommuting functions. If all fixed spaces have dimension at most one, all blocks are scalar or zero; the reversed multiplication rule and injectivity make every convolution commute. \(\square\)

**Proposition 3.3 (Gelfand's trick).** Suppose \(\tau:G\to G\) is a continuous involutive anti-automorphism with \(\tau(g)\in KgK\) for every \(g\). Then \((G,K)\) is a Gelfand pair.

*Proof.* An anti-automorphism preserves normalized Haar measure: composing with inversion gives an automorphism, and both preserve Haar measure on a compact group. Substitution in the convolution integral gives
\[
(f*h)\circ\tau=(h\circ\tau)*(f\circ\tau).
\]
Every bi-invariant function is fixed by \(\tau\). Their convolution is bi-invariant too, so \(f*h=h*f\). Apply Theorem 3.1. \(\square\)

For a Gelfand pair and an irreducible \(\pi\) with a fixed unit vector \(v\), the **zonal spherical function** is
\[
\phi_\pi(g)=\langle\pi(g)v,v\rangle.
\tag{3.4}
\]
It is independent of the phase of \(v\), bi-invariant, and has value one at the identity. Coefficient orthogonality gives
\[
\|\phi_\pi\|_2^2=\frac1{d_\pi},\qquad
\phi_\pi*\phi_\eta
=\delta_{\pi\eta}\frac{\phi_\pi}{d_\pi}.
\tag{3.5}
\]
The nonzero multiplicative functionals of \(\mathcal A\) are precisely
\[
b_\pi(f)=\int_G f(g)\phi_\pi(g^{-1})\,dg.
\tag{3.6}
\]
To prove this claim, (3.2) makes \(\widehat f(\pi)=b_\pi(f)p_\pi\); hence \(b_\pi\) is bounded and multiplicative. Bi-averaging the uniformly dense finite coefficient sums proves uniform density of the span of all \(\phi_\pi\) in \(\mathcal A\). Every nonzero multiplicative linear functional \(b\) on a Banach algebra is bounded by its norm: extend it to the unitization by \(b(f+c1)=b(f)+c\). If \(|b(f)|>\|f\|\), the geometric series makes \(b(f)1-f\) invertible, whereas its image under the extended functional is zero, a contradiction.

The elements \(e_\pi=d_\pi\phi_\pi\) are orthogonal idempotents. Density and continuity imply \(b(e_\pi)\ne0\) for some \(\pi\); that value must be one. Moreover \(f*e_\pi=b_\pi(f)e_\pi\), by its Fourier blocks. Applying \(b\) proves \(b=b_\pi\), and orthogonal idempotents give uniqueness. Thus (3.6) means a functional obtained by integrating against the spherical function, rather than point evaluation at a group element.

## A finite observation space

For \(S_m/S_{m-1}\), \(m\geq2\), the coset representation is \(\mathbb C^m=\mathbb C(1,\ldots,1)\oplus W\), where \(W\) consists of the zero-sum vectors. It is irreducible: in any nonzero invariant subspace of \(W\), choose \(a\) with unequal coordinates. Subtract its image under the transposition of those coordinates; the result is a nonzero multiple of \(e_i-e_j\). All such differences are permutation translates and span \(W\). Thus the coset representation has two inequivalent irreducibles, each once, and the pair is Gelfand. With \(S_{m-1}\) fixing \(m\), its nontrivial spherical function is \(1\) when \(g(m)=m\) and \(-1/(m-1)\) otherwise: use the normalized vector proportional to \(e_m-\frac1m(1,\ldots,1)\). The trivial spherical function is constant one.

An invariant operator on the \(m\) observation points has a matrix with a common diagonal entry and a common off-diagonal entry: simultaneous permutation of its two indices preserves exactly the cases “same point” and “different point”. Hence it is \(aI+bJ\), where \(J\) is the all-ones matrix. Such operators commute. The constant line and the zero-sum space are their common scalar-response spaces. This is the matrix form of the Gelfand criterion above, rather than an extra classification assumption.

## Prescribing a stabilizer response changes the frequencies

Before defining vector-valued induction, consider the circle \(G=\mathbb T\) and its subgroup \(K\) of \(q\)-th roots of unity, \(q\geq2\). Let \(\sigma(k)=k^r\), where \(r\) is an integer taken modulo \(q\). A scalar function with this prescribed covariance satisfies \(F(gk)=k^{-r}F(g)\). The circle basis \(e_n(g)=g^n\) satisfies it precisely when \(n+r\) is divisible by \(q\). Indeed the projection onto the permitted functions is
\[
\begin{aligned}
(P_rF)(g)&=\frac1q\sum_{k\in K}k^rF(gk),\\
P_re_n&=\left(\frac1q\sum_{k\in K}k^{n+r}\right)e_n.
\end{aligned}
\]
The geometric sum in parentheses is one in that congruence class and zero otherwise. Thus the permitted functions have the complete orthonormal basis \(e_{qj-r}\), \(j\in\mathbb Z\). Left translation by \(x\) acts on \(e_n\) by \(x^{-n}\); the resulting representation labels are exactly the integers congruent to \(r\) modulo \(q\). For \(r=0\) these are ordinary quotient functions; nonzero \(r\) imposes a different response to the same stabilizer. General induction replaces this scalar response by a finite-dimensional representation of \(K\).

## Induction and compact Frobenius reciprocity

Let \(\sigma:K\to U(V_\sigma)\) be finite dimensional. Define
\[
\mathcal I_\sigma
=\{F\in L^2(G,V_\sigma):R_kF=\sigma(k)^{-1}F
\text{ for every }k\in K\}.
\tag{2.1}
\]
Each equality is an equality in \(L^2\). This avoids choosing a common exceptional null set for an uncountable subgroup. The operators
\[
Q_kF(g)=\sigma(k)F(gk)
\]
form a strongly continuous unitary representation of \(K\). Their Haar average is the projection onto \(\mathcal I_\sigma\), so continuous covariant functions are dense in it. Left translation
\[
(\operatorname{Ind}_K^G\sigma)(x)F(g)=F(x^{-1}g)
\tag{2.2}
\]
commutes with every \(Q_k\). It therefore defines a continuous unitary representation on \(\mathcal I_\sigma\).

A continuous covariant function gives a section of the associated quotient \(G\times_KV_\sigma\), by \(gK\mapsto[g,F(g)]\), where \((g,v)\sim(gk,\sigma(k)^{-1}v)\). Its squared norm descends to \(G/K\), and (1.3) makes the section norm equal to \(\int_G\|F(g)\|^2\,dg\). Thus (2.1) is the Hilbert completion of these sections. Local triviality of an associated bundle is not needed for arbitrary compact Hausdorff groups.

**Theorem 2.3 (Frobenius reciprocity).** For an irreducible \(\pi\) of \(G\),
\[
\operatorname{Hom}_G(V_\pi,\mathcal I_\sigma)
\simeq\operatorname{Hom}_K(V_\pi|_K,V_\sigma).
\tag{2.4}
\]
In particular the multiplicity of \(\pi\) in \(\operatorname{Ind}_K^G\sigma\) is the dimension of the right side. The trivial \(\sigma\) recovers the scalar formula (2.5) already proved; we now prove the full vector-valued statement.

*Proof.* Use coefficient functions
\[
f_{v,\ell}(g)=\ell(\pi(g^{-1})v).
\]
Left translation acts on \(v\) by \(\pi(x)\), and right translation acts on \(\ell\) by the dual representation \(\pi^*(k)\). The coefficient version of Peter–Weyl, with its Hilbert–Schmidt normalization, therefore gives
\[
L^2(G,V_\sigma)\simeq
\widehat{\bigoplus}_\pi
V_\pi\otimes(V_\pi^*\otimes V_\sigma).
\]
The \(K\)-average acts on the second factor as \(\pi^*|_K\otimes\sigma\). Taking its range gives
\[
\mathcal I_\sigma\simeq
\widehat{\bigoplus}_\pi
V_\pi\otimes\operatorname{Hom}_K(V_\pi,V_\sigma).
\tag{2.6}
\]
Here \(\ell\otimes w\) corresponds to \(v\mapsto\ell(v)w\); fixed tensors correspond exactly to intertwiners. Schur's lemma identifies the second factor as the multiplicity space. For the trivial target, taking adjoints again identifies this multiplicity dimension with \(\dim V_\pi^K\), consistently with (2.5).

Explicitly, a \(K\)-intertwiner \(A:V_\pi\to V_\sigma\) gives
\[
(T_Av)(g)=A\pi(g^{-1})v.
\tag{2.7}
\]
It is continuous, covariant, and \(G\)-equivariant. Averaging \(\pi(g)A^*A\pi(g)^*\) gives its scalar trace divided by \(d_\pi\), so
\[
\|T_Av\|_2^2
=\frac{\|A\|_{\mathrm{HS}}^2}{d_\pi}\|v\|^2.
\tag{2.8}
\]
Thus the tensor identification in (2.6) uses \(\sqrt{d_\pi}T_A\) for Hilbert–Schmidt normalized \(A\). Conversely the range of every \(G\)-intertwiner \(T\) lies in the finite-dimensional \(\pi\)-coefficient block of \(L^2(G,V_\sigma)\). Its elements have unique continuous representatives, because Haar measure has full support. Evaluation there is defined; \(A(v)=(Tv)(1)\) satisfies \(A\pi(k)=\sigma(k)A\). Equivariance gives \((Tv)(g)=A\pi(g^{-1})v\). These operations are inverse and prove (2.4) directly. \(\square\)

For finite groups, [**RT-FIN-06, Theorem 3.1**](course:RT-FIN/induced-representations-and-frobenius-reciprocity#3-both-adjunctions) proves both induction adjunctions. Its function model uses \(f(hx)=h f(x)\) and \((a f)(x)=f(xa)\). Replacing \(x\) by \(g^{-1}\) gives exactly the covariance and left action in (2.1)–(2.2). Normalized Haar counting measure only rescales the Hilbert norm; it does not change multiplicities.

## Spherical harmonics in every dimension

Let \(n\geq3\), \(G=SO(n)\), \(K=SO(n-1)\) fixing \(e_n\). The map \(gK\mapsto ge_n\) identifies \(G/K\) with \(S^{n-1}\). Its invariant probability measure is normalized surface measure, since rotations preserve that measure and Proposition 1.2 proves uniqueness.

The \(K\)-orbits on the sphere are determined by \(t=x_n\). Indeed \(SO(n-1)\), with \(n-1\geq2\), acts transitively on each sphere in the first \(n-1\) coordinates; the endpoint orbits are single points. Double cosets in \(G\) are therefore determined by
\[
t(g)=\langle ge_n,e_n\rangle=g_{nn}.
\]
Inversion leaves this entry unchanged. Proposition 3.3 proves the Gelfand property before we classify its irreducible summands.

Let \(\mathcal P_k\) denote the complex homogeneous polynomials of degree \(k\) in \(n\) real variables, and put
\[
r^2=\sum_{i=1}^n x_i^2,\qquad
\Delta_{\mathbb R^n}=\sum_i\partial_{x_i}^2,\qquad
\mathcal H_k=\ker\Delta_{\mathbb R^n}\cap\mathcal P_k.
\]
Negative-degree spaces are zero. Restriction embeds \(\mathcal H_k\) in \(C(S^{n-1})\): a homogeneous polynomial vanishing on the sphere vanishes at every nonzero real point, and hence is the zero polynomial.

**Lemma 4.1 (harmonic decomposition).**
\[
\mathcal P_k=\mathcal H_k\oplus r^2\mathcal P_{k-2},\qquad
\dim\mathcal H_k
=\binom{n+k-1}{k}-\binom{n+k-3}{k-2},
\tag{4.2}
\]
where the second binomial is interpreted as zero for \(k<2\).

*Proof.* If \(h\in\mathcal H_d\), the product rule and Euler's identity give
\[
\Delta_{\mathbb R^n}(r^{2j}h)
=2j(2d+2j+n-2)r^{2j-2}h.
\tag{4.3}
\]
Induct on \(k\), starting with \(k=0,1\). The inductive harmonic decomposition of \(\mathcal P_{k-2}\) splits it into the spaces \(r^{2j}\mathcal H_{k-2-2j}\). Equation (4.3) shows that
\(\Delta_{\mathbb R^n}:r^2\mathcal P_{k-2}\to\mathcal P_{k-2}\)
is an isomorphism: each of those summands is multiplied by the nonzero scalar \(2(j+1)(2(k-2-2j)+2(j+1)+n-2)\). For every \(p\in\mathcal P_k\), choose the unique \(q\in r^2\mathcal P_{k-2}\) with \(\Delta q=\Delta p\); then \(p-q\) is harmonic. Injectivity proves directness. Counting monomials gives \(\dim\mathcal P_k=\binom{n+k-1}{k}\), proving (4.2). Iteration gives the full decomposition into \(r^{2j}\mathcal H_{k-2j}\). \(\square\)

**Theorem 4.4.**
\[
L^2(S^{n-1})
=\widehat{\bigoplus}_{k\geq0}\mathcal H_k.
\tag{4.5}
\]
Each \(\mathcal H_k\) is an irreducible \(SO(n)\)-representation, with dimension (4.2), and different degrees are inequivalent.

*Proof.* First compute its fixed space under \(K\). Write \(x=(x',t)\), \(s=|x'|^2\). A homogeneous \(K\)-invariant polynomial is a linear combination of
\[
t^{k-2j}s^j,\qquad 0\leq j\leq\lfloor k/2\rfloor.
\]
For completeness, an invariant homogeneous polynomial in \(x'\) is constant on each sphere; evaluating it on \(ue_1\) shows it is zero in odd degree and a scalar multiple of \(|x'|^{2j}\) in degree \(2j\). Rotation by \(\pi\) sends \(e_1\) to \(-e_1\), and equality on real points is a polynomial identity. Apply this argument to every coefficient of \(t\).

For \(\sum a_jt^{k-2j}s^j\) to be harmonic, the coefficients must satisfy
\[
2(j+1)(2j+n-1)a_{j+1}
=-(k-2j)(k-2j-1)a_j.
\tag{4.6}
\]
This follows from \(\Delta_{x'}s^{j+1}=2(j+1)(2j+n-1)s^j\) and differentiation twice in \(t\). The last \(t\)-power is zero or one, so there is no further condition. Every \(a_j\) is determined by \(a_0\), and \(a_0=1\) gives a nonzero polynomial with value one at \(e_n\). Thus \(\dim\mathcal H_k^K=1\).

Complete reducibility splits \(\mathcal H_k\) into irreducible summands. Each summand embeds in \(L^2(G/K)\); (2.5) forces its fixed space to be nonzero. The one-dimensional total fixed space therefore permits exactly one summand. This proves irreducibility.

To distinguish degrees and prove orthogonality, set \(E=\sum x_i\partial_{x_i}\) and \(L_{ij}=x_i\partial_{x_j}-x_j\partial_{x_i}\). Expanding each square gives
\[
\sum_{i<j}L_{ij}^2
=r^2\Delta_{\mathbb R^n}-E(E+n-2).
\tag{4.7}
\]
Indeed the second-order terms are \(r^2\Delta-\sum_{i,j}x_ix_j\partial_i\partial_j\), and the first-order terms are \(-(n-1)E\); use \(E^2=\sum_{i,j}x_ix_j\partial_i\partial_j+E\). On \(\mathcal H_k\), (4.7) is the scalar \(-k(k+n-2)\).

Rotation flows preserve surface measure, so their generators \(L_{ij}\) are skew-adjoint on smooth functions under integration. Their sum of squares is symmetric, hence different values of \(k\) give orthogonal spaces. Intertwiners commute with differentiated rotations and (4.7), so the distinct scalars also prohibit equivalence. Finally restrictions of polynomials are uniformly dense in continuous functions by Stone–Weierstrass. Lemma 4.1, with \(r^2=1\) on the sphere, puts every restricted polynomial in the algebraic sum of the \(\mathcal H_k\)'s. Continuous functions are \(L^2\)-dense, proving (4.5). \(\square\)

The operator (4.7) on the sphere is its nonpositive round Laplacian: at \(x\in S^{n-1}\), the rotation fields satisfy \(\sum_{i<j}L_{ij}(x)\otimes L_{ij}(x)=I-x\otimes x\), the tangent projection, and each field has divergence zero. Thus its spectrum on these spaces is \(-k(k+n-2)\), consistently with the sign fixed in [Casimir operators and Laplacians](RT-CPT-12.md).

## Gegenbauer polynomials and examples

Put \(\nu=(n-2)/2>0\). Define \(C_k^\nu(t)\) by the generating function
\[
(1-2tz+z^2)^{-\nu}
=\sum_{k\geq0}C_k^\nu(t)z^k.
\tag{5.1}
\]
The binomial expansion gives a degree-\(k\) polynomial with powers of the same parity as \(k\). Differentiating the left side verifies
\[
(1-t^2)F_{tt}-(n-1)tF_t
+(z\partial_z)^2F+(n-2)z\partial_zF=0.
\]
Comparing coefficients yields
\[
(1-t^2)(C_k^\nu)''-(n-1)t(C_k^\nu)'
+k(k+n-2)C_k^\nu=0.
\tag{5.2}
\]
Setting \(t=1\) in (5.1) gives
\[
C_k^\nu(1)=\frac{(2\nu)_k}{k!}>0,
\tag{5.3}
\]
where \((a)_k=a(a+1)\cdots(a+k-1)\), with \((a)_0=1\).

A zonal homogeneous polynomial has the form \(r^kp(t/r)\); its Laplacian is
\[
r^{k-2}\bigl[(1-u^2)p''(u)-(n-1)u p'(u)
+k(k+n-2)p(u)\bigr],\qquad u=t/r.
\]
This follows by the product and chain rules, or by (4.7) and \(\Delta=\partial_r^2+(n-1)r^{-1}\partial_r+r^{-2}\Delta_S\). The degree and parity in (5.1) make \(r^kC_k^\nu(t/r)\) a polynomial. Equation (5.2) makes it harmonic. By the fixed-line computation (4.6), it is the unique zonal harmonic normalized by (5.3).

The spherical function for \(\mathcal H_k\) is consequently
\[
\phi_k(g)=
\frac{C_k^{(n-2)/2}(g_{nn})}{C_k^{(n-2)/2}(1)}.
\tag{5.4}
\]
Here is the coefficient identification, including its normalization. Evaluation \(h\mapsto h(e_n)\) on \(\mathcal H_k\) has a nonzero Riesz vector \(Z\), which is \(K\)-fixed. The action is \((\pi(g)h)(x)=h(g^{-1}x)\), so for \(v=Z/\|Z\|\),
\(\langle\pi(g)v,v\rangle=Z(g^{-1}e_n)/Z(e_n)\).
Since \(g^{-1}_{nn}=g_{nn}\), this is exactly (5.4).

When \(n=3\), \(\nu=1/2\) and \(C_k^{1/2}=P_k\), the Legendre polynomials defined by (5.1). Thus the \(SO(3)/SO(2)\) spherical functions begin \(1,t,(3t^2-1)/2\), with dimensions \(1,3,5\). This recovers [the degree-\(k\) harmonics](RT-CPT-04.md), corresponding to the \(SU(2)\) highest weight \(2k\). The constant representation is included at \(k=0\).

Finally \((U(n),U(n-1))\) is Gelfand. For \(n\geq2\), the branching theorem in [Unitary groups](RT-CPT-09.md), Theorem 3.2, shows that the trivial \(U(n-1)\)-label occurs at most once. It occurs exactly for
\[
\lambda=(p,0,\ldots,0,-q),\qquad p,q\in\mathbb Z_{\geq0}.
\tag{5.5}
\]
Indeed the interlacing condition for \(\mu=(0,\ldots,0)\) forces each middle entry of \(\lambda\) to be zero and its endpoints to have those signs. For \(n=2\) there are no middle entries. For \(n=1\), \(U(0)\) is trivial and every circle irreducible is one-dimensional; hence that pair is Gelfand too.

## Positive kernels from spherical coefficients

A continuous function \(q\) on a topological group \(H\) is **positive definite** if every finite matrix \([q(h_i^{-1}h_j)]_{i,j}\) is positive semidefinite. In particular \(q(e)\geq0\), \(q(h^{-1})=\overline{q(h)}\), and \(|q(h)|\leq q(e)\), by its one- and two-point matrices. Positive definiteness is a condition on all these matrices, rather than pointwise positivity of the function.

Here is the Hilbert-space construction we will need. Give the formal span of symbols \(e_h\) the sesquilinear form
\[
\langle e_h,e_k\rangle=q(k^{-1}h),
\]
linear in the first variable. The matrix condition makes this form nonnegative. Cauchy–Schwarz follows by applying nonnegativity to \(u+av\) and minimizing over \(a\in\mathbb C\); hence null vectors are orthogonal to every vector. Quotient by the null space and complete. Left translation of the symbols preserves the form and induces unitaries \(U(a)e_h=e_{ah}\). With \(\xi=e_e\),
\[
q(a)=\langle U(a)\xi,\xi\rangle.
\]
These unitaries are strongly continuous: on a basis symbol the squared displacement is \(2q(e)-2\operatorname{Re}q(h^{-1}ah)\), which tends to zero as \(a\to e\). Finite linear combinations follow by the triangle inequality, and density and unitarity give the assertion on the completion. Conversely every coefficient \(\langle U(a)\xi,\xi\rangle\) is positive definite, since its matrices are Gram matrices. This proves the required coefficient characterization without a countability assumption.

**Theorem 5.3.** Let \((G,K)\) be a compact Hausdorff Gelfand pair, and let \(L\) be any locally compact Hausdorff group. A continuous function \(q:G\times L\to\mathbb C\), bi-invariant under \(K\) in its first variable, is positive definite if and only if
\[
\begin{gathered}
q(g,l)=\sum_{\pi:\,V_\pi^K\ne0}\beta_\pi(l)\phi_\pi(g),\\
\sum_\pi\beta_\pi(e_L)<\infty,
\end{gathered}
\]
where every \(\beta_\pi\) is a continuous positive definite function on \(L\). The series is absolutely and uniformly convergent on all of \(G\times L\), and the coefficients are uniquely determined by
\[
\beta_\pi(l)=d_\pi\int_G q(g,l)\overline{\phi_\pi(g)}\,dg.
\]
Moreover \(\sum_\pi\beta_\pi(e_L)=q(e_G,e_L)\), and at most countably many coefficients are nonzero, even if \(\widehat G\) is uncountable.

*Proof.* Apply the construction above to \(G\times L\). Bi-invariance and the displacement formula show that \(U(k,e_L)\xi=\xi\) for every \(k\in K\). The arbitrary-Hilbert-space decomposition of a compact representation from lesson one writes
\[
\mathcal H=\bigoplus_\pi V_\pi\otimes M_\pi,
\qquad U(g,e_L)=\bigoplus_\pi\pi(g)\otimes I.
\]
The commuting operators \(U(e_G,l)\) preserve these isotypic subspaces. On each they have the form \(I\otimes U_\pi(l)\). To justify this even for infinite-dimensional \(M_\pi\), take matrix coefficients between two vectors of \(M_\pi\); each resulting operator on the finite-dimensional \(V_\pi\) commutes with \(\pi(G)\), and is scalar by Schur's lemma. The scalars define the bounded operator on \(M_\pi\), giving the asserted tensor form. Unitarity, the group law and strong continuity descend by restricting to \(v\otimes M_\pi\) for a fixed unit vector \(v\).

The \(K\)-fixed component of \(\xi\) belongs to \(V_\pi^K\otimes M_\pi\). Theorem 3.1 makes this space either zero or \(\mathbb Cv_\pi\otimes M_\pi\), where \(v_\pi\) is a fixed unit vector. Thus \(\xi_\pi=v_\pi\otimes w_\pi\). Set
\[
\beta_\pi(l)=\langle U_\pi(l)w_\pi,w_\pi\rangle.
\]
It is continuous and positive definite, and \(\beta_\pi(e_L)=\|w_\pi\|^2\). Orthogonality gives \(\sum_\pi\|w_\pi\|^2=\|\xi\|^2=q(e_G,e_L)\). Computing the coefficient of \(\xi\) gives the asserted expansion. The bounds \(|\phi_\pi(g)|\leq1\) and \(|\beta_\pi(l)|\leq\beta_\pi(e_L)\) prove absolute uniform convergence, using finite-subset sums. A summable nonnegative family has only finitely many entries exceeding \(1/m\) for each positive integer \(m\), so its positive support is countable. A coefficient with zero value at the identity vanishes everywhere by the same two-point bound.

Conversely a product \(\beta_\pi(l)\phi_\pi(g)\) is a coefficient of the tensor product of their unitary representations, using the construction above for \(\beta_\pi\). It is positive definite. Finite sums preserve the matrix condition, and the uniform limit does too. The sum is continuous and bi-invariant. Finally the spherical orthogonality relation (3.5), and uniform convergence under the integral, recover exactly the displayed coefficient formula and prove uniqueness. \(\square\)

Taking \(L\) to be the trivial group gives the compact Bochner–Godement theorem: the continuous bi-invariant positive definite functions are precisely \(\sum_\pi a_\pi\phi_\pi\) with \(a_\pi\geq0\) and \(\sum_\pi a_\pi<\infty\). The proof above includes that theorem, rather than assuming it as a source result. For an abelian compact group with \(K=\{e\}\), this is the positive Fourier-series criterion.

**Corollary 5.4.** For \(n\geq3\), a continuous function \(c:[-1,1]\to\mathbb C\) defines a positive semidefinite kernel \((x,y)\mapsto c(x\cdot y)\) on the unit sphere \(S^{n-1}\) if and only if
\[
\begin{gathered}
c(t)=\sum_{k=0}^\infty a_k\frac{C_k^{(n-2)/2}(t)}{C_k^{(n-2)/2}(1)},\\
a_k\geq0,\qquad \sum_k a_k<\infty.
\end{gathered}
\]
The coefficients are unique, convergence is uniform, and \(\sum_k a_k=c(1)\).

*Proof.* Set \(G=SO(n)\), \(K=SO(n-1)\), and \(p=e_n\). These form the Gelfand pair already proved above; its spherical functions are the displayed normalized Gegenbauer polynomials evaluated at \(p\cdot gp\). The stabilizer acts transitively on each latitude of the sphere for \(n\geq3\), including its endpoint latitudes, so this scalar parametrizes the double cosets. It follows that \(g\mapsto c(p\cdot gp)\) is a continuous bi-invariant function. Its positive-definiteness matrices are exactly the matrices \([c(x_i\cdot x_j)]\), because \(x_i=g_ip\) ranges over all sphere points and
\(p\cdot g_i^{-1}g_jp=(g_ip)\cdot(g_jp)\). Apply Theorem 5.3 with trivial \(L\). \(\square\)

For example,
\[
t^2=\frac1n+\frac{n-1}{n}\frac{C_2^{(n-2)/2}(t)}{C_2^{(n-2)/2}(1)}.
\]
Its two coefficients are nonnegative. Directly, the kernel is the Gram kernel of \(x\mapsto x\otimes x\), since \(\langle x\otimes x,y\otimes y\rangle=(x\cdot y)^2\). In contrast, \(c(t)=1-\varepsilon t\), with \(0<\varepsilon<1\), is pointwise positive but fails the kernel condition: antipodal points give the matrix
\[
\begin{pmatrix}1-\varepsilon&1+\varepsilon\\1+\varepsilon&1-\varepsilon\end{pmatrix},
\]
whose eigenvalues are \(2\) and \(-2\varepsilon\).

The product theorem also handles time or another group parameter. On \(L=\mathbb R\), the functions \(\beta_0(s)=1/2\) and \(\beta_1(s)=\cos(s)/2\) are positive definite, the latter being the average of the two characters \(e^{is}\) and \(e^{-is}\), divided by two. Hence
\[
((x,t),(y,u))\longmapsto\frac12+\frac12\cos(u-t)(x\cdot y)
\]
is a positive covariance kernel on \(S^{n-1}\times\mathbb R\). An explicit Gram realization is the feature vector \(2^{-1/2}(1,\cos(t)x,\sin(t)x)\). This example connects spherical frequencies with covariance while keeping positivity visible.

## Four exercises with complete solutions

### Exercise 1 — the diagonal pair

For any compact \(G\), prove that \((G\times G,\operatorname{diag}G)\) is a Gelfand pair and identify its spherical functions.

**Solution.** Every irreducible of \(G\times G\) is \(\pi\otimes\eta\): restrict to the first factor, whose finite-dimensional isotypic spaces are preserved by the second factor. Irreducibility leaves one isotypic type \(V_\pi\otimes M\). Schur's lemma makes the second factor act on \(M\), and this action is irreducible; thus \(M=V_\eta\).

Diagonal invariants in \(V_\pi\otimes V_\eta\) are identified with \(\operatorname{Hom}_G(V_\pi^*,V_\eta)\), of dimension one if \(\eta\simeq\pi^*\) and zero otherwise. Theorem 3.1 proves the Gelfand property. Identify \(V_\pi\otimes V_\pi^*\) with its Hilbert–Schmidt endomorphisms. The action of \((g,h)\) is \(A\mapsto\pi(g)A\pi(h)^*\), and the fixed unit vector is \(I/\sqrt{d_\pi}\). Its coefficient is
\[
\phi_\pi(g,h)=\frac{\chi_\pi(gh^{-1})}{d_\pi}.
\tag{6.1}
\]
This is bi-invariant under diagonal multiplication and equals one at \((1,1)\), fixing both the inverse and the dimension factor.

### Exercise 2 — counting harmonics

Prove the dimension formula in (4.2), and compute the first three dimensions on \(S^2\) and the degree-two dimension on \(S^3\).

**Solution.** Formula (4.3) and the inductive decomposition show that \(\Delta:r^2\mathcal P_{k-2}\to\mathcal P_{k-2}\) is bijective: on \(r^{2j+2}\mathcal H_d\) its scalar is \(2(j+1)(2d+2j+n)\), which is positive. Thus \(\Delta:\mathcal P_k\to\mathcal P_{k-2}\) is onto, with kernel \(\mathcal H_k\). Monomial counting and rank–nullity give
\[
\dim\mathcal H_k=\dim\mathcal P_k-\dim\mathcal P_{k-2}
=\binom{n+k-1}{k}-\binom{n+k-3}{k-2}.
\]
For \(n=3\), this is \(2k+1\), including \(k=0,1\), so the first three values are \(1,3,5\). For \(n=4,k=2\), the value is \(10-1=9\). Degree-two harmonics are precisely the trace-zero quadratic forms, another direct count.

### Exercise 3 — the rotation Gelfand trick

Prove that \((SO(3),SO(2))\) is Gelfand by inversion on double cosets.

**Solution.** Take \(SO(2)\) to fix \(e_3\). Two vectors on the unit sphere lie on the same \(SO(2)\)-orbit exactly when they have the same third coordinate: the horizontal circles are transitive orbits, and the poles are fixed. Hence \(KgK\) is specified by \(g_{33}\). Since \((g^{-1})_{33}=(g^t)_{33}=g_{33}\), inversion preserves every double coset. It is a continuous involutive anti-automorphism preserving Haar measure. Substitution reverses convolution as in Proposition 3.3, and all bi-invariant functions and their convolutions are fixed. Their convolution therefore commutes, giving the Gelfand pair.

### Exercise 4 — reciprocity with the evaluation issue resolved

Prove the morphism isomorphism (2.4), explaining why evaluation at the identity is permitted. Give the normalization of an induced copy.

**Solution.** Peter–Weyl places the image of any \(G\)-intertwiner \(T:V_\pi\to L^2(G,V_\sigma)\) in the finite-dimensional \(\pi\)-coefficient block. Every vector there has a continuous representative, unique by full Haar support. For a covariant image the \(L^2\) covariance becomes an equality of continuous functions, separately for each \(k\). Therefore \(A(v)=(Tv)(1)\) is defined and
\[
A\pi(k)v=(T\pi(k)v)(1)=(Tv)(k^{-1})
=\sigma(k)(Tv)(1).
\]
It is a \(K\)-intertwiner. Equivariance at \(g^{-1}\) also yields
\((Tv)(g)=(T\pi(g^{-1})v)(1)=A\pi(g^{-1})v\).
Conversely that formula for any \(K\)-intertwiner \(A\) gives a continuous covariant function and obeys
\[
(L_xT_Av)(g)=A\pi(g^{-1}x)v=T_A(\pi(x)v)(g).
\]
Evaluation recovers \(A\), so both maps are inverse. To check its norm, the averaged positive operator
\[
\int_G\pi(g)A^*A\pi(g)^*\,dg
=\frac{\operatorname{tr}(A^*A)}{d_\pi}I
\]
follows from Schur and trace. Consequently (2.8) holds. If \(\|A\|_{\mathrm{HS}}=1\), the map \(\sqrt{d_\pi}T_A\) is an isometric copy of \(V_\pi\); orthogonal Hilbert–Schmidt intertwiners give orthogonal copies, by polarization of the same identity. This proves the multiplicity claim, without evaluating an arbitrary \(L^2\) class.

## What this lesson assumes

Hilbert complete reducibility, Schur's lemma, Peter–Weyl, Fourier injectivity and coefficient orthogonality were proved in lessons 1–3. Haar measure is supplied by the full internal analysis proofs identified in lesson 1. The \(U(n)\) branching theorem is lesson 9, Theorem 3.2, including its internally proved determinant–tableau identity. Scalar Fubini, regular measure density, compact Hausdorff quotient topology and Stone–Weierstrass are the measure and topology prerequisites; the exact internal Stone–Weierstrass proof is identified in lesson 2. All induction, compact quotient measure, reciprocity, Gelfand-pair criteria, spherical-harmonic decomposition and zonal polynomial formulas used here have been proved in this lesson.

The comparisons with **RT-FIN-06, Theorem 3.1 and Exercise 4**, and [**HA-LCA-10, Theorem 4.1**](course:HA-LCA/HA-LCA-10#section-4), refer to their proved statements. General noncompact induction needs quasi-invariant measures and may require modular corrections; the present formulas use compact probability Haar measure throughout.

## References

- C. Gruson and V. Serganova, *A Journey Through Representation Theory* (2018), Chapter 2, §9, Proposition 9.5 and Lemma 9.6; Chapter 3, §3, for the circle, \(SU(2)\), \(SO(3)\) and degree harmonics.

- Pavel Etingof, [*Lie groups and Lie algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), §35, exercise on homogeneous spaces: compact Lie quotient multiplicities. The scalar formula (2.5) and full reciprocity (2.4) are proved here for arbitrary compact Hausdorff groups, including the normalization and evaluation issue.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §37. Its homogeneous-space coefficient exercise gives a compact comparison, with the source countable-base convention. General vector-valued induction and compact reciprocity for arbitrary closed subgroups are proved here.

Christian Berg, [*A unified view of space-time covariance functions through Gelfand pairs*, arXiv:2004.12842v2](https://arxiv.org/abs/2004.12842v2), Theorem 3.7, points to the product expansion of Christian Berg, Ana P. Peron and Emilio Porcu, [*Orthogonal expansions related to compact Gelfand pairs*, arXiv:1612.03718v1](https://arxiv.org/abs/1612.03718v1), Theorem 3.3 with proof in §4 and the sphere specialization in §5 (accessed 3 October 2026). Theorem 5.3 here proves that expansion through the Hilbert-space construction and compact isotypic decomposition, and includes the needed compact Bochner–Godement argument.

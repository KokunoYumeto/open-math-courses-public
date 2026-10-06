# Residual representations and Serre's modularity theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A characteristic-zero representation can be irreducible while its reduction is reducible. An isogeny can identify rational Tate modules while leaving different integral reductions. These phenomena are central to congruences between modular forms. The modularity theorem of Serre, proved by Khare and Wintenberger with Kisin's lifting results, goes in the reverse direction: an odd irreducible residual representation comes from a modular form.

We use \(p\) for the residual characteristic and \(q\) for a different local prime. Frobenius at \(q\) is **arithmetic**, so \(\bar\chi_p(\operatorname{Fr}_q)=q\bmod p\). Local reciprocity sends a uniformizer to geometric Frobenius, and our Weil–Deligne convention remains \(r(w)Nr(w)^{-1}=|w|N\). The residual inertia calculation below uses the actual torsion representation, before semisimplifying it.

The actual earlier proof bindings are Theorems 2.1–2.4 and Lemma 3.3/Example 3.4 of lesson 1, Theorem 3.0c of lesson 2, Lemmas 1.2, 1.6–1.7 of lesson 5, and Lemma 3.0/Theorem 3.1/Lemma 4.0 of lesson 8. For level-one forms, the written earlier *Valence formula and the ring of modular forms of level one*, Theorems 2.1–2.3, 4.1 and 5.1, proves the dimensions, product and Eisenstein identities; *Modular forms, lattice functions and Eisenstein series*, Theorem 4.2 and Solution 4, proves the expansions and Bernoulli computation. Sections 5–8 distinguish actual proofs from the remaining required parts of the full modularity argument. The full theorems and classical weight recipe remain requirements of this lesson; the presence of their free primary papers does not certify their proof closure.

## 1. Reduction, Frobenius, and oddness

The general attached representation and its good-prime formula remain part of the full construction required in lessons 11–12; their explicitly unclosed arithmetic-model, geometric comparison and irreducibility interfaces are not supplied by this lesson. Whenever \(\rho_{f,\lambda}\) is used below, that construction is a required prerequisite. The reductions and comparisons proved here apply to any representation satisfying its displayed good-prime formula.

Let \(f=\sum_{n\ge1}a_nq^n\) be a normalized cuspidal eigenform of weight \(k\ge2\), level \(N\), and character \(\varepsilon\). For a prime \(\lambda\) of its coefficient field above \(p\), choose a stable lattice \(T\) in the two-dimensional \(K_\lambda\)-representation \(\rho_{f,\lambda}\). Define
\[
\bar\rho_{f,\lambda}=(T/\lambda T)^{\mathrm{ss}},
\tag{1}
\]
with scalars extended to \(\overline{\mathbf F}_p\) when needed. The semisimplification is independent of the lattice, by the finite-length exact-sequence argument in the first lesson, Theorem 2.2. The reduction before semisimplification need not be independent of it.

At \(q\nmid Np\), reduction of the good-prime polynomial gives
\[
\det(X-\bar\rho_{f,\lambda}(\operatorname{Fr}_q))
=X^2-\bar a_qX+\bar\varepsilon(q)q^{k-1}.
\tag{2}
\]
The global determinant is
\[
\det\bar\rho_{f,\lambda}=\bar\varepsilon_G\bar\chi_p^{\,k-1}.
\tag{3}
\]
To prove (3) directly from (2), the quotient of the two determinant characters has finite image and factors through a finite Galois group. It equals one at every good prime by (2). Theorem 3.0c of lesson 2 supplies a prime outside the finite excluded set in every conjugacy class of this quotient. The character is consequently one on every class, hence identically one. The Dirichlet Galois character is the actual cyclotomic construction of lesson 1, Proposition 3.1, and the finite-character construction in the weight-one lesson, Lemma 0.1.

Every continuous map \(G_{\mathbf Q}\to\operatorname{GL}_d(\overline{\mathbf F}_p)\), with discrete target, has finite image: compact subsets of a discrete space are finite. Its finitely many matrix entries lie in some finite field, and its kernel is open. Thus it factors through a finite Galois group.

This makes a residual version of Frobenius determination especially concrete. Given two such representations, pass to the finite quotient cutting out both kernels. Theorem 3.0c of lesson 2 proves finite Chebotarev, including its positive Dirichlet density for every conjugacy class. Removing a finite set does not change that density, so every class still occurs. Equality of the polynomials (2) at those primes therefore gives equality of characteristic polynomials everywhere on that quotient. Brauer–Nesbitt gives equality of the semisimplifications. We use the **whole polynomial**, including the determinant, rather than an unrestricted trace-only assertion in small characteristic.

**Proposition 1.1 (residual oddness).** For complex conjugation \(c\),
\[
\det\bar\rho_{f,\lambda}(c)=-1.
\tag{4}
\]
If \(p>2\), its eigenvalues are \(1,-1\).

**Proof.** The transformation law under \(-I\) gives \(\varepsilon(-1)=(-1)^k\). Since \(\bar\chi_p(c)=-1\), the finite-quotient determinant identity (3) yields
\[
\bar\varepsilon_G(c)\bar\chi_p(c)^{k-1}
=(-1)^k(-1)^{k-1}=-1.
\tag{5}
\]
For \(p>2\), \(c^2=1\) and \(X^2-1\) has distinct roots, so its action is diagonalizable; the determinant forces one of each eigenvalue. For \(p=2\), equation (4) reads \(1=1\) and makes no eigenvalue distinction. The determinant definition of oddness is vacuous in that characteristic; one must not infer two distinct eigenvalues there. ∎

We supply the characteristic-polynomial comparison used above. The characteristic-zero proof in lesson 2 ends by cancelling integers in the coefficient field; that last step cannot be copied into characteristic \(p\).

**Lemma 1.2 (characteristic-polynomial Brauer–Nesbitt).** Let \(F=\overline{\mathbf F}_p\), and let \(V,W\) be finite-dimensional representations of a finite group \(H\). If
\[
\det(X-h\mid V)=\det(X-h\mid W)\quad\text{for every }h\in H,
\]
then \(V^{\mathrm{ss}}\simeq W^{\mathrm{ss}}\).

**Proof.** A stable filtration gives block triangular matrices, so characteristic polynomials multiply over its composition factors. Replace both modules by their semisimplifications. Put \(M=V\oplus W\), and let \(A\) be the \(F\)-linear span of the image of \(H\) in \(\operatorname{End}_F(M)\). It is an algebra, and \(M\) is a faithful semisimple \(A\)-module.

The regular-module embedding from lesson 2, Lemma 4.1, works in every characteristic: for a basis \(m_1,\ldots,m_d\) of \(M\), the map \(a\mapsto(am_1,\ldots,am_d)\) embeds \(A\) in \(M^d\). Thus the regular module is semisimple. Its isotypic decomposition gives two-sided ideals \(A_i\) and central orthogonal idempotents, exactly as in that proof. Write
\[
A_i\simeq S_i^{\,n_i}
\]
as left modules, where the \(S_i\) are pairwise nonisomorphic simple modules. Every simple type in \(M\) occurs here, since \(a\mapsto as\) maps \(A\) onto any simple module containing a nonzero vector \(s\).

We need an operator of trace one on each \(S_i\), rather than an idempotent whose trace could be zero. Schur's lemma over \(F\) gives \(\operatorname{End}_A(S_i)=F\): an endomorphism has an eigenvalue, and its eigenspace is a nonzero invariant subspace, hence all of \(S_i\). Let \(d_i=\dim_F S_i\). Endomorphisms of the left regular module \(A_i\) are its right multiplications. Counting their dimensions in the displayed decomposition gives
\[
\dim_F A_i=n_i d_i
=\dim_F\operatorname{End}_A(A_i)=n_i^2,
\qquad n_i=d_i.
\]
The action \(A_i\to\operatorname{End}_F(S_i)\) is injective: its kernel annihilates every copy of \(S_i\), hence the regular module \(A_i\), and therefore its identity. Both sides have dimension \(d_i^2\), so the map is surjective. Choose \(b_i\in A_i\) acting as a diagonal matrix unit on \(S_i\). It has trace one there and acts as zero on all other simple types.

Equality of characteristic polynomials gives equality of traces on \(H\), hence on its span \(A\). Evaluating at \(b_i\) shows that the two multiplicities of \(S_i\) are equal **modulo \(p\)**. Cancel their common copies in \(V,W\). The remaining multiplicities are nonnegative multiples of \(p\); write the remaining modules as \(V_1^{\oplus p},W_1^{\oplus p}\). Cancellation preserves characteristic-polynomial equality. For every \(h\),
\[
\det(X-h\mid V_1)^p=\det(X-h\mid W_1)^p.
\]
The \(p\)-th power map on \(F[X]\) is injective, so the polynomials for \(V_1,W_1\) agree too. Repeat the argument, or induct on \(\dim V+\dim W\): after cancellation this sum has decreased by a factor \(p\), unless both remaining modules are zero. The induction forces all multiplicities to agree. Restoring the cancelled constituents proves the lemma. ∎

A trace-only failure can occur even in the same dimension. Over \(\mathbf F_4\), let a generator of \(C_3\) act through a character \(\xi\) with value \(\alpha\ne1\), \(\alpha^3=1\). The two semisimple modules \(1\oplus1\) and \(\xi\oplus\xi\) have trace zero at every element. At the generator their characteristic polynomials are \((X-1)^2\) and \((X-\alpha)^2\), with distinct constant terms \(1,\alpha^2\). Lemma 1.2 retains this information.

## 2. The congruence modulo 691

Let
\[
\Delta=q\prod_{n\ge1}(1-q^n)^{24}
=\sum_{n\ge1}\tau(n)q^n.
\tag{6}
\]
We can prove Ramanujan's full congruence using the two-dimensional space of level-one forms of weight twelve.

**Proposition 2.1 (Ramanujan's congruence).** For every positive \(n\),
\[
\tau(n)\equiv\sigma_{11}(n)\pmod{691},
\qquad \sigma_{11}(n)=\sum_{d\mid n}d^{11}.
\tag{7}
\]

**Proof.** The level-one prerequisite gives
\[
\begin{aligned}
E_4&=1+240\sum_{n\ge1}\sigma_3(n)q^n,\\
E_6&=1-504\sum_{n\ge1}\sigma_5(n)q^n,\\
E_{12}&=1+\frac{65520}{691}\sum_{n\ge1}\sigma_{11}(n)q^n,
\qquad E_4^3-E_6^2=1728\Delta.
\end{aligned}
\tag{8}
\]
The third expression uses \(B_{12}=-691/2730\) in the Eisenstein-series formula. Since \(M_{12}\) has basis \(E_4^3,\Delta\), its forms are determined by the constant and first coefficients. Comparing those coefficients gives the identity
\[
691E_{12}=441E_4^3+250E_6^2
=691E_4^3-432000\Delta.
\tag{9}
\]
Indeed the constant coefficients are \(691\), and the first coefficients on the middle expression are \(441\cdot720+250\cdot(-1008)=65520\).

The coefficients of \(E_4^3\) are integers. Taking the \(n\)-th coefficient in (9) gives
\[
65520\sigma_{11}(n)=691[q^n]E_4^3-432000\tau(n).
\tag{10}
\]
Modulo the prime \(691\), both \(65520\) and \(-432000\) equal \(566\), which is nonzero. Cancelling it proves (7) for every \(n\). This is a modular-form identity argument, not an inference from a finite coefficient check. ∎

**Theorem 2.2 (the residual representation of \(\Delta\) at 691).**
\[
\bar\rho_{\Delta,691}\simeq 1\oplus\bar\chi_{691}^{\,11}.
\tag{11}
\]

**Proof.** For each prime \(q\ne691\), Proposition 2.1 gives \(\tau(q)\equiv1+q^{11}\). Both representations in (11) are unramified there, and their characteristic polynomials are
\[
X^2-(1+q^{11})X+q^{11}
=(X-1)(X-q^{11}).
\tag{12}
\]
The determinant comes from (3), with trivial character and \(k=12\). The finite-quotient Chebotarev and characteristic-polynomial argument in §1 proves (11). The right side is semisimple; (11) says nothing about whether a particular unreduced lattice has a split reduction. ∎

For later numerical checks, the first coefficients from (6) include
\[
\tau(2)=-24,\quad\tau(3)=252,\quad
\tau(5)=4830,\quad\tau(7)=-16744.
\tag{13}
\]
They can be obtained by multiplying only the factors with \(n\le7\), since larger factors cannot affect these coefficients.

## 3. Rational 5-torsion and the two level-11 lattices

Use the notation of the weight-two lesson:
\[
E_0:y^2+y=x^3-x^2,\qquad
E_1:y^2+y=x^3-x^2-10x-20.
\tag{14}
\]
The explicit degree-five isogeny \(E_0\to E_1\) was verified there. The first lesson, Lemma 3.3 and Example 3.4, already proves the actual torsion pairing, this isogeny and the integral inertia distinction. We retain the explicit points and give the uniform Tate-curve criterion for arbitrary semistable curves here.

**Proposition 3.1 (torsion and residual semisimplification).** Both curves have a rational point of exact order five, and
\[
E_0[5]^{\mathrm{ss}}\simeq E_1[5]^{\mathrm{ss}}
\simeq1\oplus\bar\chi_5.
\tag{15}
\]

**Proof.** On \(E_0\), put \(P_0=(0,0)\). Its tangent has slope zero and meets the cubic again at \((1,0)\). Negation on these equations is \((x,y)\mapsto(x,-y-1)\), so
\[
2P_0=(1,-1).
\tag{16}
\]
The tangent there has slope \((3-2)/(2(-1)+1)=-1\) and meets the cubic again at \((0,0)\). Therefore \(4P_0=(0,-1)=-P_0\), and \(5P_0=0\). Since \(P_0\ne0\) and five is prime, its order is exactly five. Its nonzero multiples are precisely the four points with \(x=0,1\) and \(y=0,-1\).

On \(E_1\), put \(P_1=(5,5)\). The tangent slope is
\[
\frac{3\cdot25-2\cdot5-10}{2\cdot5+1}=5.
\tag{17}
\]
Substitution of \(y=5x-20\) into the equation leaves a cubic with roots \(5,5,16\). Its third point is \((16,60)\), so \(2P_1=(16,-61)\). The tangent at this point has slope
\[
\frac{3\cdot256-2\cdot16-10}{2(-61)+1}=-6.
\tag{18}
\]
The line is \(y=-6x+35\), and its third intersection is \((5,5)\). Thus \(4P_1=(5,-6)=-P_1\), proving exact order five again.

Each fixed nonzero point generates a trivial \(G_{\mathbf Q}\)-submodule of the two-dimensional \(\mathbf F_5\)-space \(E_i[5]\). The determinant is \(\bar\chi_5\), by the alternating perfect pairing actually constructed in lesson 1, Lemma 3.3. The one-dimensional quotient therefore has character \(\bar\chi_5\). Semisimplifying that short exact sequence proves (15). ∎

It follows at every common good \(q\ne5\) that
\[
a_q(E_i)\equiv1+q\pmod5.
\tag{19}
\]
At \(q=5\) this residual Frobenius argument is unavailable; at \(q=11\) the curves have bad reduction. Here are direct counts for all other primes at most 23. The vector lists the number of \(y\)-solutions at \(x=0,\ldots,q-1\) on \(E_1\); add one for the point at infinity.

| \(q\) | Numbers of solutions, in order | \(\#E_1(\mathbf F_q)\) | \(a_q=q+1-\#E_1(\mathbf F_q)\) |
|---:|---|---:|---:|
| 2 | \(2,2\) | 5 | \(-2\) |
| 3 | \(0,2,2\) | 5 | \(-1\) |
| 7 | \(0,1,2,0,2,2,2\) | 10 | \(-2\) |
| 13 | \(2,0,1,2,0,2,0,0,0,0,2,0,0\) | 10 | \(4\) |
| 17 | \(0,1,0,2,2,2,0,2,2,0,0,0,0,2,2,2,2\) | 20 | \(-2\) |
| 19 | \(2,0,2,2,0,2,0,1,2,2,2,0,2,0,0,0,2,0,0\) | 20 | \(0\) |
| 23 | \(2,0,2,0,0,2,0,2,2,0,2,0,2,0,2,0,2,2,2,0,2,0,0\) | 25 | \(-1\) |

For odd \(q\), each count is \(1+\left(\frac{1+4(x^3-x^2-10x-20)}q\right)\), with Legendre symbol zero allowed. For \(q=2\), both \(y\)-values solve each equation. The displayed totals are divisible by five, as rational 5-torsion predicts. The isogeny gives the same \(a_q\) on \(E_0\).

To distinguish the actual torsion representations, we need local inertia rather than their semisimplifications.

## 4. The Tate-curve residual criterion

**Theorem 4.1 (semistable residual inertia).** Let \(E/\mathbf Q_q\) be semistable and \(p\ne q\). Then
\[
E[p]\text{ is unramified at }q
\quad\Longleftrightarrow\quad
p\mid v_q(\Delta_{\min}).
\tag{20}
\]
At good reduction the valuation is zero. At multiplicative reduction this is a criterion for the full two-dimensional representation, not just its semisimplification.

**Proof.** At good reduction the prime-to-\(q\) Tate module is unramified, by the local elliptic-curve lesson, so (20) holds. Suppose first the reduction is split multiplicative, and write \(E=E_z\) for its Tate parameter \(z\), with
\[
z=\pi^m u,\qquad m=v_q(z)>0,\quad u\in\mathbf Z_q^\times.
\tag{21}
\]
Tate uniformization identifies
\[
E_z[p]=\{\zeta_p^a z^{b/p}:a,b\in\mathbf Z/p\mathbf Z\}
\quad\text{inside }\overline{\mathbf Q}_q^\times/z^{\mathbf Z}.
\tag{22}
\]
The two generators are independent: if their product lies in \(z^{\mathbf Z}\), valuations force \(b=0\bmod p\), and then \(a=0\bmod p\).

Let \(K^{\mathrm{nr}}\) be the maximal unramified extension of \(\mathbf Q_q\). It contains \(\mu_p\): extend the residue field to contain the \(p\)-th roots of unity and lift the simple roots of \(X^p-1\). It also contains a \(p\)-th root of \(u\): choose one in the algebraic residue field and apply Hensel's lemma to \(X^p-u\); its derivative is nonzero because \(p\ne q\). Consequently inertia fixes \(\zeta_p\) and the unit root, and its action in the basis (22) is
\[
\bar\rho_{E_z,p}(\sigma)=
\begin{pmatrix}1&m\,\bar t_p(\sigma)\\0&1\end{pmatrix},
\qquad \sigma\in I_q.
\tag{23}
\]
Here \(\sigma(\pi^{1/p})/\pi^{1/p}=\zeta_p^{\bar t_p(\sigma)}\).

The character \(\bar t_p:I_q\to\mathbf F_p\) is surjective. Indeed \(\pi^{1/p}\) has valuation \(1/p\), while every element of \(K^{\mathrm{nr}}\) has integer valuation. The polynomial \(X^p-\pi\) is Eisenstein and has degree \(p\); the resulting extension, with \(\mu_p\) already present, is tame cyclic of degree \(p\). Thus (23) is trivial for every \(\sigma\) exactly when \(p\mid m\).

The local Tate-model calculation gives \(v_q(\Delta_{\min})=v_q(z)\). In detail, its discriminant is \(z\prod_{n\ge1}(1-z^n)^{24}\), whose product factors are units, and its \(c_4\) is a unit, so the model is minimal and multiplicative. This identifies \(m\) with the valuation in (20). For nonsplit multiplicative reduction, the representation is the split Tate representation tensored with the **unramified** quadratic splitting character. This twist is trivial on inertia, so the same criterion applies. These are actually proved in lesson 8, Lemma 3.0 (uniformization and the parameter), Theorem 3.1 (torsion and its Kummer cocycle), and Lemma 4.0 (quadratic descent and its unramified multiplicative cases). At good reduction use the explicit prime-to-residue-characteristic reduction proof in lesson 3, Lemma 3.0 and Theorem 3.1. ∎

When \(p\nmid m\), the inertia image in (23) has order \(p\), its invariant space has dimension one, and its Swan conductor is zero since the image is tame. The residual conductor exponent at \(q\) is therefore one. When \(p\mid m\), it is zero. Both local semisimplifications in (23) are \(1\oplus1\), independently of \(m\); semisimplifying locally would erase the distinction.

**Corollary 4.2 (different level-11 reductions).** The \(G_{\mathbf Q}\)-modules \(E_0[5]\) and \(E_1[5]\) are not isomorphic, although the rational 5-adic Tate modules are isomorphic and their residual semisimplifications agree.

**Proof.** For the displayed integral equations (14), direct Weierstrass calculations give
\[
\begin{array}{c|rrr}
 &c_4&c_6&\Delta\\ \hline
E_0&16&-152&-11\\
E_1&496&20008&-11^5.
\end{array}
\tag{24}
\]
At 11, both \(c_4\) are units. An integral model with unit \(c_4\) is minimal: a change reducing the discriminant valuation by twelve would divide \(c_4\) by \(11^4\), contradicting integrality of the new model. Their positive discriminant valuations give multiplicative reduction. It is split in each case, since \(-c_6\) modulo 11 is \(9\) for \(E_0\) and \(1\) for \(E_1\), both squares; this is the split-node criterion from the local elliptic-curve lesson.

Theorem 4.1 now gives nontrivial inertia of order five on \(E_0[5]\), because \(5\nmid1\), and trivial inertia on \(E_1[5]\), because \(5\mid5\). Isomorphic global representations have isomorphic inertia restrictions, so these cannot be isomorphic. On rational Tate modules the degree-five isogeny is invertible, with inverse given by its dual divided by five. That division is permitted over \(\mathbf Q_5\) and not over \(\mathbf Z_5\). Equation (15) proves the common semisimplification. This completes the earlier lattice example. ∎

## 5. Serre's level, weight, and character

Let \(\bar\rho:G_{\mathbf Q}\to\operatorname{GL}_2(\overline{\mathbf F}_p)\) be continuous, odd, and irreducible. Irreducibility here is over the algebraic closure. Define its **Serre level** by
\[
N(\bar\rho)=\prod_{q\ne p}q^{a_q(\bar\rho)},\qquad
a_q(\bar\rho)=\sum_{i\ge0}
\frac{\dim(V/V^{G_i})}{[G_0:G_i]}.
\tag{25}
\]
Take \(G_i\) from a finite local Galois quotient through which the representation factors. **Lemma 5.0 (the residual conductor formula).** Formula (25) is independent of the finite local quotient, vanishes precisely for an unramified representation, and is the sum of \(\dim V-\dim V^{I_q}\) and a nonnegative Swan term. The Swan term is additive on exact sequences. For a one-dimensional determinant,
\[
 a_q(\det V)\le a_q(V).
 \tag{25A}
\]

**Proof.** Extend lower groups to real indices by \(G_t=G_{\lceil t\rceil}\), \(t>0\), and use the Herbrand function. On an interval with group \(G_i\), its derivative is \(1/[G_0:G_i]\). Therefore a change of variable in the finite sum gives
\[
 a_q(V)=\dim V-\dim V^{I_q}
       +\int_0^\infty\bigl(\dim V-\dim V^{G_{\mathbf Q_q}^{u}}\bigr)\,du.
 \tag{25B}
\]
Endpoints do not affect the integral. Lesson 5, Lemma 1.6, actually proves that absolute upper groups surject onto every finite upper group. Their action on \(V\), and hence every fixed space in (25B), is independent of the quotient. This proves independence in (25).

The inertia term is nonnegative and vanishes only if all of inertia fixes \(V\). In that case the positive upper groups fix it too. Conversely, vanishing of the sum forces the inertia term to be zero. There are only finitely many ramified primes. Choose a primitive element of the finite kernel field, multiply by an integer to make it integral, and write its monic minimal polynomial \(F\in\mathbf Z[X]\). Its discriminant is a nonzero integer, because the extension has characteristic zero. At a prime not dividing that integer, the residue polynomial is separable and splits in some finite residue extension. Proposition 0F.2 and simple-root Hensel in lesson 1 lift all its roots to the corresponding unramified local extension. The splitting field, and hence the kernel field, is unramified there. This proves finite support of the product defining the level without importing a trace-pairing étaleness criterion.

For \(u>0\), the finite image of \(G_{\mathbf Q_q}^{u}\) is a \(q\)-group by lesson 5, Lemma 1.2. Its order is invertible in characteristic \(p\). The operator \(|B|^{-1}\sum_{b\in B}b\) projects onto invariants. Averaging a lift of an invariant vector proves that taking invariants preserves surjections, hence is exact. Fixed-space codimensions, and their integral, are additive. This argument does not apply to all tame inertia. In (23), a nontrivial extension has inertia codimension one, while the sum of its two trivial constituents has codimension zero.

For any subgroup \(B\), if \(\dim V^B=2\), its determinant is trivial; if \(\dim V^B\le1\), the determinant codimension is at most one, hence at most \(2-\dim V^B\). Apply this to every term of (25), whose weights are nonnegative, to prove (25A). ∎

**Lemma 5.0C (integrality in modular coefficients).** For every finite-dimensional continuous residual local representation at \(q\ne p\), its Swan conductor and (25) are nonnegative integers. Consequently \(N(\bar\rho)\) is a positive integer prime to \(p\).

**Proof.** Let \(I\) and \(P\) be its finite inertia and wild-inertia groups. Lemmas 1.2 and 1.7 of lesson 5 prove that \(P\) is a \(q\)-group and \(I/P\) is cyclic. We first prove the coefficient-lifting fact needed for \(P\); we do not assume a lift of the whole residual representation.

If \(B\) is any finite group of order prime to \(p\), a simple \(\overline{\mathbf F}_p[B]\)-module \(S\) has a characteristic-zero \(B\)-module \(\widetilde S\) of the same dimension reducing to \(S\), and the lift is unique up to isomorphism once the correspondence of prime-to-\(p\) roots of unity has been fixed. Indeed the averaging proof makes the regular modular algebra semisimple, and the matrix-factor proof of Lemma 1.2 supplies a primitive idempotent \(e\) whose left ideal is \(S\). All its coefficients and all matrix entries lie in some finite field \(k\). Choose the complete unramified characteristic-zero DVR \(\mathcal O\) with residue field \(k\), using lesson 1, Proposition 0F.2, and start with a coefficient lift \(e_0\in\mathcal O[B]\). In this complete finite free algebra perform
\[
 e_{r+1}=e_r-(e_r^2-e_r)(2e_r-1)^{-1}.
 \tag{25C}
\]
The inverse exists: \((2e_r-1)^2=1+4(e_r^2-e_r)\), and the inverse of an element congruent to one is its convergent geometric series. These quantities commute, since they are polynomials or convergent power series in \(e_r\). Substitution shows the idempotence error is squared times a unit at each step. Thus \(e_r\) converges to an idempotent \(\widetilde e\) reducing to \(e\), including when \(p=2\). The direct summand \(\mathcal O[B]\widetilde e\) is finite free of rank \(\dim S\) and supplies the lift. Its characteristic-zero representation is absolutely irreducible: a proper invariant subspace after a finite coefficient extension intersects a full stable lattice in a saturated sublattice, whose nonzero proper reduction would contradict absolute simplicity of \(S\). The lattice and saturation arguments are proved in lesson 1, §§0A and 2.

Every element of \(B\) has prime-to-\(p\) order. Its eigenvalues are roots of unity of that order, with simple, distinct residue roots. Simple-root Hensel gives a bijection between these roots and their reductions. The characteristic polynomial in the residue field records their **integer multiplicities** as root multiplicities; hence it uniquely records the eigenvalue multiset of any lift. All lifts consequently have the same characteristic-zero characters and are isomorphic by the matrix-factor comparison of lesson 2, Lemma 4.1. A finite set of matrix entries generates a finitely generated characteristic-zero field. Embed it into \(\mathbf C\), first on its algebraic part and then on a transcendence basis and its algebraic extension. This realizes the lifts as complex finite-group representations; the chosen root correspondence is carried along this embedding.

Now let \(V\) be a simple modular \(I\)-module. Its restriction to \(P\) is semisimple, since \(|P|\) is invertible. The \(P\)-isotypic summands are permuted by \(I\); there is one orbit, since a union of smaller orbits would be an invariant proper summand. Choose a type \(S\) and let \(J\) be its stabilizer. Its isotypic summand \(U\) is a simple \(J\)-module: a proper \(J\)-submodule would give, by its translates in the other distinct summands, a proper \(I\)-submodule. We have \(U\simeq S\otimes k^r\) as \(P\)-modules. Let \(gP\) generate the cyclic group \(J/P\). Conjugation by \(g\) preserves the type of \(S\), so choose an intertwining operator \(A_0\) on \(S\). The operator of \(g\) on \(U\) is \(A_0\otimes D\): dividing by \(A_0\) leaves an operator commuting with the full matrix algebra on \(S\), hence acting only on its multiplicity space. Since the coefficient field is algebraically closed, \(D\) has an eigenvector. Its line gives a nonzero \(J\)-stable copy of \(S\). Simplicity forces \(r=1\).

Lift \(S\) to \(\widetilde S\) over \(\mathbf C\) as above. Its conjugate by \(g\) is isomorphic to it, because the modular characteristic polynomials agree on \(P\), and their root multisets determine the lifted character. Choose an intertwiner \(A\). If \(m=|J/P|\), then \(g^m\in P\), and
\(A^m\widetilde S(g^m)^{-1}\) commutes with \(P\); Schur's lemma makes it a nonzero scalar. Also \(A\) commutes with \(\widetilde S(g^m)\), since conjugation by \(g\) fixes \(g^m\). Rescale \(A\) by an \(m\)-th root of that scalar's inverse, so \(A^m=\widetilde S(g^m)\). The conjugation relation and this power relation now define a representation of \(J\): reduce every word to a \(P\)-element times \(g^a\), \(0\le a<m\), and these relations give exactly its multiplication law. Induce it to \(I\). Its restriction to \(P\) is the direct sum of the lifted types in the orbit, each once, precisely matching \(V|_P\).

For every subgroup \(B\subset P\), use the direct sum of the original DVR lattices lifting the \(P\)-types, before the embedding into \(\mathbf C\). Its averaging projector is an idempotent direct summand. The restriction to \(P\) of the complex representation just constructed is the complexification of these lifted types, with the same multiplicities. Its rank equals the dimension of its reduction, because a finite projective module over a local DVR is free. Thus its invariant dimension agrees in characteristic zero and in characteristic \(p\). Every positive lower ramification group lies in \(P\). The complex representation just constructed and \(V\) consequently have the same Swan sum. Regard \(I\) as the Galois group of the ramified local extension \(L/L^I\). Its lower groups are the original \(G_i\), since their definition uses only the action and valuation on \(L\). The actual characteristic-zero integrality proof in lesson 5, Theorem 2.6, therefore makes this Swan sum a nonnegative integer.

Finally apply the Swan exact-sequence additivity proved in Lemma 5.0 to a composition series of an arbitrary modular \(I\)-module. It is a sum of the integer Swan conductors of its simple factors. Adding the integer tame codimension \(\dim V-\dim V^I\) gives (25). Lemma 5.0 supplies finite support and nonnegativity, proving the assertion about \(N\). No exactness of tame invariants, and no characteristic-zero lift of the entire residual extension, has been assumed. ∎

We retain the **classical Serre weight**, including both exceptional choices and characteristic two. It differs from the Katz weight-one convention. The following local classification supplies the forms to which the recipe applies; its optimal modular weight and the finite-flat exceptional test have further proof obligations specified after the recipe. The freely accessible comparison is Bosman's thesis, §1.4.3, printed pp.39–40; it is not an optimization proof.

**Lemma 5.1 (the full local shapes).** Put \(\omega=\bar\chi_p|_{I_p}\). A continuous two-dimensional representation of \(G_{\mathbf Q_p}\) over \(\overline{\mathbf F}_p\) has either tame inertia with two level-one characters, tame inertia with a conjugate pair of level-two characters, or nontrivial wild inertia with a unique wild-fixed line and an upper triangular inertia action whose diagonal characters are powers of \(\omega\).

**Proof.** The representation factors through a finite group. Its wild inertia image \(P\) is a \(p\)-group, normal in the local image. Any nonzero module of a finite \(p\)-group in characteristic \(p\) has a nonzero fixed vector. Here is a proof: the conjugation class equation shows that a nontrivial \(p\)-group has nontrivial center. Choose a central element \(z\) of order \(p\), by taking a power of a nonidentity central element. The operator \(z-1\) has \((z-1)^p=z^p-1=0\), so its kernel is nonzero and stable under the group. On that kernel apply induction to the smaller group \(P/\langle z\rangle\). This gives the fixed vector; the trivial group starts the induction.

If \(P\) acts nontrivially, \(V^P\) is therefore one-dimensional. Normality makes it a local Galois-stable line. On that line and on the quotient a \(p\)-group acts trivially, since the multiplicative group of the coefficient field has no nonidentity element of \(p\)-power order. The resulting diagonal characters are tame. Lesson 5, Lemma 1.7, or lesson 7, Proposition 1.0, proves that tame inertia is procyclic of order prime to \(p\), and arithmetic Frobenius conjugates by the \(p\)-th power. A one-dimensional local character consequently satisfies \(\varphi^p=\varphi\) on inertia; it has order dividing \(p-1\), and is a power of \(\omega\). The off-diagonal entry cannot vanish on all wild inertia, since that would make \(P\) trivial on \(V\). This proves the wild case, including a local invariant line even if the global representation is irreducible.

If \(P\) is trivial, the finite cyclic inertia image has order prime to \(p\), so a generator is diagonalizable: its minimal polynomial divides the separable polynomial \(X^m-1\). Frobenius permutes its two character spaces, or acts inside a repeated character space. Each orbit has length one or two. In a length-one orbit the same relation gives a power of \(\omega\). In a length-two orbit the characters are \(\varphi,\varphi^p\), with \(\varphi^{p^2-1}=1\) and \(\varphi^{p-1}\ne1\).

For precision, the fundamental level-two characters come from the action on a \((p^2-1)\)-st root of a uniformizer over the maximal unramified extension, followed by one of the two embeddings of the residue roots of unity into \(\overline{\mathbf F}_p\). Their \((p+1)\)-st powers are the fundamental level-one character. This is \(\omega\): on the uniformizer \(\zeta_p-1\) of the totally ramified cyclotomic field, the ratio
\(g(\zeta_p-1)/(\zeta_p-1)\) reduces to the exponent \(a\) in \(g(\zeta_p)=\zeta_p^a\), by the finite geometric sum. The Eisenstein equation \(((1+X)^p-1)/X\) has constant term \(p\) and the other nonleading coefficients divisible by \(p\); the earlier local degree proof makes this a tame extension of index \(p-1\). The canonical tame action ratios of Lemma 1.7 therefore give exactly \(\omega\). Thus choose \(\psi\) with \(\psi^{p+1}=\omega\).

Write the exponent of \(\varphi\) uniquely as \(a+pb\), with \(0\le a,b\le p-1\) and not both \(p-1\). Multiplication by \(p\) modulo \(p^2-1\) interchanges the digits. Equal digits would give a level-one character, so they are distinct; interchange the two characters to arrange \(a<b\). This proves all asserted shapes. ∎

For odd \(p\), the classical recipe is as follows.

- If the two tame characters have level two, choose a fundamental character \(\psi\) with \(\psi^{p+1}=\omega\). After interchanging them they are \(\psi^{a+pb},\psi^{pa+b}\), with \(0\le a<b\le p-1\). Set
  \[
  k_{\mathrm S}(\bar\rho)=1+pa+b.
  \tag{26}
  \]
- If inertia is tame and the characters have level one, write them as \(\omega^a,\omega^b\), with \(0\le a\le b\le p-2\). Set \(k_{\mathrm S}=1+pa+b\), except when \(a=b=0\), where set \(k_{\mathrm S}=p\). The Katz convention assigns weight one in that exceptional case.
- If wild inertia acts nontrivially, the restriction has a nonsplit upper triangular form
  \[
  \begin{pmatrix}\omega^\beta&*\\0&\omega^\alpha\end{pmatrix},
  \qquad0\le\alpha\le p-2,\quad1\le\beta\le p-1.
  \tag{27}
  \]
  Put \(a=\min(\alpha,\beta)\), \(b=\max(\alpha,\beta)\). Normally \(k_{\mathrm S}=1+pa+b\). If \(\beta-\alpha\equiv1\pmod{p-1}\) and the local representation \(\bar\rho|_{G_{\mathbf Q_p}}\otimes\bar\chi_p^{-\alpha}\) is **not finite flat**, add \(p-1\).

“Finite flat” means that the finite étale group scheme over \(\mathbf Q_p\) corresponding to the local residual representation extends to a finite flat group scheme over \(\mathbf Z_p\), with its finite coefficient-field action. The exceptional extension in (27) is often described as très ramifiée. Keeping the extension and the order of its characters matters; its semisimplification alone does not determine that exceptional choice.

For \(p=2\), the classical recipe is \(k_{\mathrm S}=2\) if the local representation is finite flat, and \(k_{\mathrm S}=4\) otherwise. The free Khare–Wintenberger author paper, introduction p.2, uses exactly these classical weights. In particular the theorem below does not make an additional weight-one Katz assertion in characteristic two.

The recipe has two mathematically distinct remaining requirements: prove that the finite-flat test in the cyclotomic extension case agrees with the unit Kummer, or peu ramifiée, condition; and prove that exactly the displayed classical weight can be realized at the minimal prime-to-\(p\) level. Lemma 5.1 proves the shapes and digit choices, not these optimization statements. Characteristic two also requires the finite-flat weight-two versus weight-four argument. The full recipe is retained, and these are explicit unclosed parts of its proof.

In every case the recipe gives the determinant restriction
\[
\det\bar\rho|_{I_p}=\omega^{k_{\mathrm S}-1}.
\tag{28}
\]
For (26), multiply the two characters to get \(\psi^{(p+1)(a+b)}=\omega^{a+b}\); \(pa+b\equiv a+b\pmod{p-1}\). The level-one cases are the same calculation; adding \(p-1\), or replacing \(1\) by \(p\), does not change it. At \(p=2\) both sides are trivial.

Define the residual character
\[
\bar\varepsilon_G=\det\bar\rho\,\bar\chi_p^{\,1-k_{\mathrm S}}.
\tag{29}
\]
It is unramified at \(p\). Its conductor away from \(p\) divides \(N(\bar\rho)\): at each ramification subgroup, the codimension of invariants for the determinant is at most that for \(V\), and sum (25) preserves the inequality. Kronecker–Weber then identifies (29) with a character of \((\mathbf Z/N(\bar\rho)\mathbf Z)^\times\). The earlier Kronecker–Weber proof is NT-CFT 20, Theorem 20.2, with Proposition 20.5 for the conductor and primitive Dirichlet character; the prerequisites behind that proof are not checked in this lesson. These statements apply to (29) by lifting its finite, prime-to-\(p\) image. To check that lift directly, put its values in \(\mathbf F_{p^r}\). Each nonzero value is a simple residue root of \(X^{p^r-1}-1\). Lesson 1, Lemma 0D.1 and Proposition 0F.2, give exactly one root with that residue in the complete unramified coefficient extension. The product of two lifts has the product residue and is again such a root; uniqueness makes the lift multiplicative. This proves the unique Teichmüller character \(\varepsilon\), rather than merely selecting complex representatives of its values. For \(p>2\), oddness gives \(\varepsilon(-1)=(-1)^{k_{\mathrm S}}\); for \(p=2\), the recipe gives even weight and the Teichmüller character is trivial on \(-1\).

**Serre's modularity theorem.** Let \(\bar\rho:G_{\mathbf Q}\to\operatorname{GL}_2(\overline{\mathbf F}_p)\) be continuous, odd and absolutely irreducible. There is a normalized cuspidal eigenform of weight \(k_{\mathrm S}(\bar\rho)\), level \(N(\bar\rho)\), and some characteristic-zero Dirichlet character \(\varepsilon'\) modulo that level, with \(\bar\varepsilon'=\bar\varepsilon_G\), whose semisimplified residual representation is \(\bar\rho\). For \(p\ge5\), \(\varepsilon'\) can be chosen to be the Teichmüller character \(\varepsilon\) constructed above. For \(p=2,3\), its \(p\)-power part must be allowed. The minimal level and the displayed classical weight are retained in all characteristics.

The former version of this theorem prescribed \(\varepsilon'=\varepsilon\) for **every** \(p\). That assertion is false. Serre's freely accessible 1988 notes, printed pp.54–55, give the characteristic-three counterexample at level 13 and weight two: the nonzero eigenspaces have nebentypus of order six, whereas the space with its order-two reduction lifted by Teichmüller is zero. Allen–Wake, §1.2, identifies the same newform orbit \(13.2.e.a\); its complete §5 explains the torsion-cohomology obstruction rather than removing it. The scanned original explicitly notes the corresponding characteristic-two obstruction. These are source-verified counterexamples to the discarded character clause; the geometric realization and the computation of all minimal residual invariants in that counterexample are not additional completed proofs in this programme.

Here is the determinant check, which does not need that geometric computation. For the level-13 form write \(\varepsilon'(2)=\zeta_6\). In characteristic three, \(X^2-X+1=(X+1)^2\), so \(\bar\zeta_6=-1\). Thus \(\bar\varepsilon'\) is the quadratic character modulo 13 and, in weight two, \(\det\bar\rho=\bar\varepsilon'_G\bar\chi_3\), exactly (29). The order-three part of \(\varepsilon'\) disappears on reduction. More generally a finite-order character lifting \(\bar\varepsilon_G\) is \(\varepsilon\eta\), where \(\eta\) has \(p\)-power order: decompose its cyclic image into its prime-to-\(p\) and \(p\)-primary subgroups; simple-root uniqueness identifies the first factor with \(\varepsilon\), and in characteristic \(p\), \(X^{p^r}-1=(X-1)^{p^r}\) kills the second. Conversely every such product has the required reduction. Its parity still satisfies \(\varepsilon'(-1)=(-1)^{k_{\mathrm S}}\). At \(p=2\), reduction alone cannot impose this parity; the even classical weight imposes it on the chosen lift.

**Lemma 5.2 (propagation inside a compatible system).** Suppose a semisimple compatible system has coefficients in a number field \(E\) and common good-prime polynomials \(P_q(T)\in E[T]\). If one characteristic-zero member is the representation of an eigenform \(g\), with the same polynomials, then every member is the corresponding representation of \(g\), and every stable-lattice reduction has its residual eigenpacket.

**Proof.** Embed the compositum of the coefficient fields into the coefficient field of the known member. Equality there of each coefficient of \(P_q\) with the coefficient for \(g\) is equality in that compositum, since an embedding is injective. Apply any other coefficient embedding. The good-prime traces are now equal in characteristic zero. Theorem 4.2 of lesson 2 gives equality of the semisimple representations, and Theorem 2.2 of lesson 1 gives lattice-independent semisimplified reduction. This proves the assertion. It does not produce a modular member from a residual member. ∎

The remaining full proof of Serre's theorem must produce that modular member and the optimal weight and level. The actually read free Khare–Wintenberger proof has the following precise structure. In Part I, §8, let \(L_r\) be the good-dihedral, odd-level assertion with at most \(r\) ramified primes, and \(W_r\) its reduced weight-two version. Their arguments require \(W_1\), the implication \(W_r\Rightarrow L_r\) by weight reduction, and \(L_r\Rightarrow W_{r+1}\) by killing ramification. Once these implications are proved, induction gives \(W_1,L_1,W_2,L_2,\ldots\), and every finite ramification set is covered. Raising and then removing the auxiliary good-dihedral prime reduces the general case to these assertions. Lemma 5.2 proves the propagation step used after a successful change of residual characteristic. It does not prove the existence of the prescribed lifts or modularity lifting.

Part I, §9, also handles even level and the classical characteristic-two weight-four case. Its minimal weight-two versus non-finite-flat weight-four passage uses a change to characteristic three and potentially Barsotti–Tate modularity. Kisin's free author DVI, Theorem 0.1 and Corollary 0.2, supplies the theorem called Hypothesis (H) there. In Part II, §§9–10, the prescribed-lift and modularity-lifting proofs require deformation-ring local conditions, the global deformation/Hecke comparison and potential modularity descent. Those arguments have not been reconstructed here or bound to completed earlier programme proofs. The optimal-weight argument, including finite-flat classification, and the minimal-level argument remain required with their full stated scope. The formal induction just given is not a proof of its missing implications, and the free primary papers are not substituted for them. In particular this lesson is not certified as a complete proof of Serre's theorem.

## 6. Level lowering and exceptional examples

**Ribet level lowering, a weight-two case.** Let \(p>3\), let \(f\) be a weight-two eigenform of level \(N\) and trivial character with \(p\nmid N\), and suppose \(\bar\rho_{f,\lambda}\) is absolutely irreducible. If \(q\ne p\), \(q\parallel N\), and the residual representation is unramified at \(q\), then the same residual representation comes from a weight-two eigenform of level \(N/q\) and trivial character. In particular no condition \(q\not\equiv1\pmod p\) is imposed. The full unrestricted conclusion remains a required proof here. The actual free author notes of Ribet–Stein, §§3.9–3.11, distinguish the restricted Mazur principle from the quaternionic pivot needed to remove that restriction.

**Lemma 6.0 (the two numerical steps in level lowering).** The restricted Mazur argument and the quaternionic pivot have the following conclusions under their explicitly listed geometric hypotheses.

First, suppose \(V\) is an unramified two-dimensional residual constituent at \(q\) in the identity-component specialization sequence for the modular Jacobian at \(q\). Suppose Frobenius on its torus is \(qU_q\), and that failure of descent to the old quotient puts \(V\) entirely in that torus. For a new exact-level weight-two trivial-character packet, this failure implies \(q\equiv1\pmod p\).

Second, suppose the two specialized Jacobians \(J,J'\) in a quaternionic pivot have residual multiplicities \(\lambda>0,\mu\ge0\). Let \(X_t\) be the specialized character groups modulo the eigenpacket. Suppose the unramified prime \(q\) gives
\[
\dim X_q(J)\ge2\lambda,\qquad \dim X_q(J')\ge2\mu,
\]
the ramified pivot prime \(s\) gives
\[
\dim X_s(J)\le\lambda,\qquad \dim X_s(J')\le\mu,
\]
and the character-group comparisons identify
\(X_q(J)\simeq X_s(J')\), \(X_s(J)\simeq X_q(J')\).
These hypotheses are incompatible.

**Proof.** In the first case, \(U_q\) is the scalar \(a_q\) on the eigenpacket. Corollary 1.0d of the earlier weight-two lesson proves \(a_q^2=1\) at a prime dividing the primitive level exactly once. Frobenius is therefore the scalar \(qa_q\), with determinant \(q^2\). Its unramified residual determinant is also \(q\), by (3). As \(q\ne p\), cancellation gives \(q=1\) in the residue field. This proves precisely why that argument alone cannot handle the unrestricted theorem.

For the second case the comparisons give \(2\lambda\le\mu\) and \(2\mu\le\lambda\). Combining them gives \(4\lambda\le\lambda\), contrary to \(\lambda>0\). This is the entire numerical contradiction. It does not establish any of the specialization, character-group or multiplicity hypotheses. ∎

The full Ribet theorem above requires those geometric hypotheses, including their component-group and integral multiplicity assertions. The actually read free Ribet–Stein notes, §§3.9–3.11, construct the argument with a ramified pivot and, when necessary, an auxiliary raised prime. Here is the elementary prime-selection step. Form the joint finite quotient of the residual representation and \(\bar\chi_p\). The image of complex conjugation has cyclotomic component \(-1\) and residual eigenvalues \(1,-1\), by oddness and \(p>2\). Finite Chebotarev, lesson 2, Theorem 3.0c, supplies infinitely many auxiliary primes outside the finite excluded set with this class. At each, \(q'\equiv-1\pmod p\) and the Frobenius matrix is nonscalar, with eigenvalue ratio \(q'\). This proves the required selection, not the level-raising theorem. The level-raising existence, integral character-group comparisons, and specialized multiplicity bounds in Lemma 6.0 remain unclosed core inputs. They are retained without imposing \(q\not\equiv1\pmod p\) on the theorem.

Theorem 4.1 explains how the local hypothesis can arise for a semistable elliptic curve: its \(p\)-torsion forgets a multiplicative prime when \(p\) divides the minimal discriminant valuation. Level lowering is the deep assertion that the same **irreducible** representation can then be obtained from a form with that prime removed. For the level-11 example at \(p=5\), irreducibility fails, so one cannot apply this theorem to deduce a weight-two form of level one. The residual conductor of the full \(E_1[5]\) is already trivial at 11; the reducibility is essential to interpreting that fact.

For \(\Delta\), the six familiar exceptional residual primes have particularly explicit descriptions:

| \(p\) | Semisimplified residual representation |
|---:|---|
| 2 | \(1\oplus1\) |
| 3 | \(1\oplus\bar\chi_3\) |
| 5 | \(\bar\chi_5\oplus\bar\chi_5^2\) |
| 7 | \(\bar\chi_7\oplus\bar\chi_7^4\) |
| 23 | the standard \(S_3\)-representation over \(\mathbf F_{23}\) described below |
| 691 | \(1\oplus\bar\chi_{691}^{11}\) |

**Proposition 6.1 (the four small-prime congruences, with proof).** For every prime \(q\ne p\), the traces of \(\bar\rho_{\Delta,p}(\operatorname{Fr}_q)\) for \(p=2,3,5,7\) are respectively
\(0,1+q,q+q^2,q+q^4\).

**Proof.** Write \(\theta=(2\pi i)^{-1}d/dz=q\,d/dq\), \(F=E_4\), \(G=E_6\). The earlier level-one dimension proof gives \(S_{12}=\mathbf C\Delta\). We prove two exact differential identities rather than assuming congruences:
\[
 4F\theta^2F-5(\theta F)^2=960\Delta,
 \qquad
 2F\theta G-3G\theta F=-1728\Delta.
 \tag{30A}
\]
Let \(j=cz+d\), \(C=c/(2\pi i)\), and \(H\) have weight \(k\). Differentiating its transformation law and using \((\gamma z)'=j^{-2}\) gives
\[
 \theta H(\gamma z)=j^{k+2}\theta H(z)+kCj^{k+1}H(z),
\]
\[
 \theta^2H(\gamma z)=j^{k+4}\theta^2H(z)
 +(2k+2)Cj^{k+3}\theta H(z)
 +k(k+1)C^2j^{k+2}H(z).
\]
For the first expression of (30A), the extra linear terms have coefficients \(4\cdot10-5\cdot8=0\), and the quadratic terms \(4\cdot20-5\cdot16=0\). For the second, the extra coefficient is \(2\cdot6-3\cdot4=0\). Thus both expressions have weight twelve. They are holomorphic and have zero constant term; the level-one group has only the one cusp orbit. Their coefficients of \(q\) are \(4\cdot240=960\) and \(2(-504)-3(240)=-1728\). This proves (30A), including its sign.

Expanding the first identity and symmetrizing its finite convolution yields the integer identity
\[
 \tau(n)=n^2\sigma_3(n)
 +60\sum_{m=1}^{n-1}(9m^2-5mn)\sigma_3(m)\sigma_3(n-m).
 \tag{30B}
\]
Indeed before symmetrization the convolution is
\(240\sum(n-m)^2\sigma_3(m)\sigma_3(n-m)-300\sum m(n-m)\sigma_3(m)\sigma_3(n-m)\);
replace \((n-m)^2\) by \(m^2\) in its sum to get (30B). Consequently
\(\tau(n)\equiv n^2\sigma_3(n)\pmod{2,3,5}\).
At an odd prime \(q\), \(q^2(1+q^3)\) is even. Modulo three, \(q^2=1\) and \(q^3=q\), giving \(1+q\). Modulo five, \(q^5=q\), giving \(q^2+q\). For comparison, the alternative exponent expression retained from the original example is
\[
 q^{-30}(1+q^{71})=q^2(1+q^3)=q^2+q
 \quad\text{in }\mathbf F_5.
 \tag{30}
\]
No congruence at a residual prime itself is needed.

The second identity of (30A), after expanding coefficients, gives
\[
 12\tau(n)=5n\sigma_3(n)+7n\sigma_5(n)
 +840\sum_{m=1}^{n-1}(2n-5m)\sigma_3(m)\sigma_5(n-m).
 \tag{30C}
\]
Modulo seven this is \(5\tau(n)=5n\sigma_3(n)\), so
\(\tau(n)\equiv n\sigma_3(n)\); at a prime it is \(q+q^4\).

The determinants of all four character pairs in the table are \(\bar\chi_p^{11}\), using the exponents modulo \(p-1\). Their full good-prime polynomials therefore agree with (2). Finite Chebotarev and Lemma 1.2 prove all four residual identifications. The 691 row was proved in §2. ∎

The free primary Ramakrishnan–Sahu paper, Theorem 2.1(ix),(x) and §4.1, contains the differential approach; the transformation, constants, signs, convolution and each residual comparison have been proved here. In particular the sign of the second expression in (30A) is fixed by its coefficient of \(q\).

**Proposition 6.2 (the exceptional representation at 23).** Let \(L\) be the splitting field of \(X^3-X-1\). On
\[
W=\{(x_1,x_2,x_3)\in\mathbf F_{23}^3:x_1+x_2+x_3=0\},
\tag{31}
\]
let \(S_3=\operatorname{Gal}(L/\mathbf Q)\) permute the coordinates. Then
\[
\bar\rho_{\Delta,23}\simeq W.
\tag{32}
\]

**Proof.** The actual earlier weight-one lesson, Lemmas 5.0A–5.0B and §5, proves that the class group of \(\mathbf Q(\sqrt{-23})\) is cyclic of order three, that \(L\) is its unramified cyclic cubic class field, and that the form
\[
h(z)=\eta(z)\eta(23z) =q\prod_{n\ge1}(1-q^n)(1-q^{23n}) \tag{32A} \] has, at every prime \(q\ne23\), coefficient equal to the trace of this standard representation. Its proof includes the binary-theta Poisson transformation, both cusp conditions, the ideal coefficient identity, the cubic inertia computation and the class-field identification using the actually written NT-CFT 19, Theorem 19.1. We use those specific proofs, not the general Deligne–Serre theorem or a numerical congruence import.

The product proof of \(\Delta\) in the earlier level-one lesson, Theorem 4.1, gives a coefficientwise identity over \(\mathbf Z\). In \(\mathbf F_{23}[[q]]\),
\[
(1-q^n)^{24}=(1-q^n)(1-q^{23n}).
\tag{32B}
\]
Indeed \((A+B)^{23}=A^{23}+B^{23}\) since all intermediate binomial coefficients are divisible by 23. Multiply (32B) over \(n\). The coefficient of \(q^m\) only involves factors with \(n\le m\), so the identity passes to the infinite formal products without an interchange of analytic limits. It proves \(\tau(m)\equiv a_m(h)\pmod{23}\) for **every** \(m\).

For completeness, on \(W\) the identity, a transposition and a three-cycle have traces \(2,0,-1\). The permutation representation splits as its fixed line plus \(W\), since 3 is invertible in \(\mathbf F_{23}\). Subtracting that fixed line from its three traces \(3,1,0\) proves the displayed traces. The determinant on \(W\) is the permutation sign. By the quadratic-subfield computation in the earlier §5 this is \((q/23)\) at a good prime. Euler's criterion gives
\[
\det W(\operatorname{Frob}_q)
=\left(\frac q{23}\right)=q^{11}\pmod{23}.
\tag{33}
\]
To check Euler's criterion directly, the finite-field multiplicative group is cyclic by lesson 1, §0F: writing \(q=g^r\) gives \(q^{11}=(-1)^r\), which is one exactly for a square. Thus both the trace and determinant agree with the residual \(\Delta\) polynomial at every \(q\ne23\). Since 23 does not divide \(|S_3|\), the averaging projection proves semisimplicity of \(W\). Finite Chebotarev and Lemma 1.2 prove (32). ∎

## 7. The odd two-dimensional Artin consequence

**Odd Artin modularity.** Every continuous odd irreducible complex representation \(\rho:G_{\mathbf Q}\to\operatorname{GL}_2(\mathbf C)\) with finite image comes from a weight-one cuspidal newform. The full assertion includes projective \(A_5\) image. The remaining weight-one descent in its proof is specified below; it is not replaced by a reduction in a single characteristic.

**Lemma 7.1 (integral models and infinitely many usable reductions).** Such a \(\rho\) has a model over a number field \(E\) and a stable full \(\mathcal O_E\)-lattice. Its reductions are absolutely irreducible at all but finitely many prime ideals. There are infinitely many rational primes \(p>3\) outside that exceptional set at which \(\rho\) is unramified and its Frobenius eigenvalues are \(1,-1\).

**Proof.** Write \(H\) for its finite image. Average over \(H\) to prove Maschke's splitting over \(\overline{\mathbf Q}\), as in lesson 2, Lemma 4.1. The regular module is a sum of simple modules, and its algebra is a product of full matrix algebras over the algebraically closed field. That proof applies over \(\overline{\mathbf Q}\), and extension to \(\mathbf C\) gives the same matrix factors. Every complex simple representation is therefore obtained by extending one of these algebraic simple modules. Finitely many entries of its finitely many group matrices generate a number field \(E\), giving the desired model. The module
\(L=\sum_{h\in H}\rho(h)\mathcal O_E^2\)
is finitely generated, contains \(\mathcal O_E^2\), spans \(E^2\) and is stable. It need not be globally free; after localization at a prime it is free over the DVR by lesson 1, Lemma 0A.1.

Absolute irreducibility makes the span of \(\rho(H)\) the full algebra \(M_2(E)\), by the algebra argument in lesson 2, Lemma 4.1. Choose four image matrices forming an \(E\)-basis. Their determinant in the four matrix-coordinate entries is nonzero. Choose an \(E\)-basis of \(L\) after inverting a fixed nonzero integer and exclude its denominator primes, those of the matrices, and the primes dividing that nonzero determinant. At every remaining prime the four reductions still span \(M_2(k)\), and remain a basis after algebraic scalar extension. An invariant proper line would then be invariant under every two-by-two matrix, which is impossible. Thus the reduction is absolutely irreducible.

The image of complex conjugation has eigenvalues \(1,-1\): its square is one, the characteristic is zero and its determinant is \(-1\). Apply finite Chebotarev to the field fixed by the kernel of \(\rho\), choosing that conjugacy class. There are infinitely many primes in it, and deleting the finite denominator, exceptional and ramification sets still leaves infinitely many. At such a prime the characteristic polynomial is exactly \((X-1)(X+1)\), so the two roots remain distinct on reduction when \(p>3\). ∎

**Lemma 7.2 (recovery from a fixed classical weight-one space).** Fix a level \(M\), a number field containing the determinant character of \(\rho\), and a full finite integral Hecke-stable lattice in the classical space \(S_1(\Gamma_1(M))\). Suppose infinitely many of the reductions in Lemma 7.1 occur as eigenpackets in the reduction of this lattice, with their good-prime traces and determinant character. Then one characteristic-zero weight-one cusp eigenpacket has the good-prime traces and determinant of \(\rho\).

**Proof.** The finite-lattice eigenpacket lifting proof in the earlier weight-one lesson, Lemma 3.0C, lifts each packet to characteristic zero after extending its coefficient field. For this fixed lattice, the generated commutative Hecke algebra is a finite free subgroup of its finite endomorphism module. It has only finitely many characteristic-zero characters, since its scalar extension is a finite-dimensional commutative algebra. Thus one character occurs for infinitely many of the residual primes. Its eigenvalues \(a_q\), the determinant-character values, and \(\operatorname{tr}\rho(\operatorname{Frob}_q)\) are algebraic integers in one fixed compositum. For each fixed \(q\nmid M\) outside the ramification set, their differences vanish modulo infinitely many distinct rational primes. A nonzero algebraic integer has nonzero integer norm, whose prime divisors are finite. Every difference is consequently zero. The same argument on the finite diamond group proves equality of the determinant characters. Faithfulness and the local-factor decomposition in Lemma 3.0C supply a nonzero cusp eigenvector for that character; the usual full Hecke normalization gives its normalized eigenpacket. This proves the assertion. ∎

The actual weight-one lattice construction is written in the earlier lesson, Lemma 3.0, by the rational kernel of \((g_5,g_7)\mapsto E_6g_5-E_4g_7\), integral coefficient division and the finite intersection of diamond translates. Its rational Fourier-basis and analytic dimension prerequisites still have their separately recorded programme closure requirements. Lemma 7.2 proves recovery once classical weight-one reductions in a fixed lattice are available; it does not assert their availability.

This is the essential remaining point. At the primes selected in Lemma 7.1, the local representation is unramified. The classical Serre recipe in §5 assigns it weight \(p\), not weight one. Even full Serre modularity therefore does not put those reductions directly into \(S_1\). Khare–Wintenberger Part I, Theorem 10.1(ii) and its proof, uses the distinct Frobenius roots together with companion-form/weight-one descent and a fixed-level integral comparison. The required descent, the Katz-to-classical comparison for infinitely many primes, and the fixed-level conclusion have not been proved here or supplied by an inspected earlier programme proof. They remain required for the full odd Artin theorem, including its \(A_5\) case. Lemmas 7.1–7.2 prove the integral reduction and recovery parts without asserting this missing bridge.

Once the full odd Artin theorem and the exact-conductor and all-local-factor theorem of Deligne–Serre in the weight-one lesson are closed, their complete conclusion gives
\[
L(s,\rho)=L(s,f)
\tag{34}
\]
for the primitive weight-one form of the Artin conductor. The cusp-form analytic continuation gives entireness of the uncompleted Artin \(L\)-function here. Thus the strong Artin conjecture holds for **odd irreducible two-dimensional representations over \(\mathbf Q\)**, including projective \(A_5\) image. This does not assert the even case or the corresponding theorem over every number field.

## 8. Proof closure

The actual earlier proof bindings and local arguments now prove stable-lattice independence, characteristic-polynomial comparison, semistable residual inertia, the two mod-five lattice examples, the universal congruence modulo 691 and all five other exceptional rows. Lemmas 5.0 and 5.0C prove quotient independence, modular-coefficient integrality of the residual conductor and its zero criterion; Lemma 5.1 proves the complete tame/wild local shapes and the niveau-two digit choices. Equation (28), the character lift and its determinant reduction are proved in §5. The false universal Teichmüller clause has been corrected with its explicit source-verified small-characteristic counterexample. No paid text supplies the mathematics of these arguments.

Full proof compliance remains unclosed. The general attached higher-weight representations and their good-prime arithmetic comparison require the full construction retained in lessons 11–12. The finite-flat/peu ramifiée equivalence and optimal classical weights, including \(p=2\), need full local and modular proofs. The full Serre theorem needs the prescribed lifts, all modularity-lifting and deformation/Hecke comparisons, potential modularity descent, good-dihedral auxiliary steps and optimal level/weight arguments described in §5. The unrestricted Ribet theorem needs the geometric and integral hypotheses explicitly exposed in Lemma 6.0, together with auxiliary level raising. The full odd Artin theorem needs the weight-one descent between Lemmas 7.1 and 7.2. The exact conductor and all-local-factor use in (34) retains the unclosed general primitive weight-one interfaces in the earlier lesson. Its cusp-form analytic continuation also needs its actual earlier analytic proof chain. The full statements, all equation tags and complete exercise solutions are preserved; these unresolved true mathematical obligations are not discharged by their free citations.

The written earlier proofs used here have exact local locators. The missing deep proofs described above are not given here.

## 9. Exercises, with complete solutions

**Exercise 9.1 (easy).** Verify \(\tau(q)\equiv1+q^{11}\pmod{691}\) for primes \(q\le7\).

**Solution.** Use the coefficients (13). Their reductions, and direct modular powers, give:

| \(q\) | \(\tau(q)\) | \(\tau(q)\bmod691\) | \(1+q^{11}\bmod691\) |
|---:|---:|---:|---:|
| 2 | \(-24\) | 667 | 667 |
| 3 | 252 | 252 | 252 |
| 5 | 4830 | 684 | 684 |
| 7 | \(-16744\) | 531 | 531 |

For example \(4830=7\cdot691-7\), giving \(684\); \(16744=24\cdot691+160\), so its negative gives \(531\). Repeated squaring gives the right column. These checks illustrate the universal identity (7); they do not replace its proof. ∎

**Exercise 9.2 (medium).** Verify (19) for all primes \(q\le23\), \(q\ne5,11\).

**Solution.** The count vectors in §3 give \(a_q=-2,-1,-2,4,-2,0,-1\), for \(q=2,3,7,13,17,19,23\). Their reductions modulo five are \(3,4,3,4,3,0,4\). The numbers \(q+1\) reduce to the identical list. All counts include the point at infinity, so the congruence is equivalently \(5\mid\#E_1(\mathbf F_q)\). On \(E_0\), the explicit isogeny and the earlier proof of isogeny invariance give the same traces; the separate rational point \(P_0\) also proves the congruence for every good prime away from five. ∎

**Exercise 9.3 (medium).** Prove oddness of \(\bar\rho_{f,\lambda}\). Explain the characteristic-two qualification.

**Solution.** The central matrix \(-I\) acts through both \((-1)^k\) and the character \(\varepsilon(-1)\), hence these are equal. Evaluate the determinant \(\bar\varepsilon_G\bar\chi_p^{k-1}\) at \(c\): the result is \((-1)^k(-1)^{k-1}=-1\). Semisimplification preserves the determinant because determinants multiply along a stable filtration. For \(p>2\), the involution is diagonalizable with eigenvalues \(1,-1\). For \(p=2\), these coincide; an involution can even have a nontrivial unipotent Jordan block. The determinant equality still holds but does not distinguish odd from even reductions. ∎

**Exercise 9.4 (hard).** Prove the Tate-curve criterion (20), and use it to distinguish the two lattices in (14). Explain why local semisimplification is insufficient.

**Solution.** For \(p\ne q\), pass to the maximal unramified extension, where \(\mu_p\) and a \(p\)-th root of the unit part of \(z=\pi^mu\) exist by simple-root Hensel lifting. The only inertia action on (22) comes from \(\pi^{m/p}\), giving the upper entry \(m\bar t_p\) in (23). The character \(\bar t_p\) is onto because adjoining \(\pi^{1/p}\) gives a tame totally ramified cyclic degree-\(p\) extension. Thus every upper entry is zero exactly when \(p\mid m\). The Tate discriminant has valuation \(m\); the nonsplit case has the same inertia after an unramified quadratic twist. Good reduction gives the zero-valuation case.

At \(q=11,p=5\), (24) gives \(m=1\) on \(E_0\) and \(m=5\) on \(E_1\). The first inertia image is nontrivial of order five; the second is trivial. This proves nonisomorphism of the actual reductions. Locally, both matrices have two trivial composition factors, so both local semisimplifications are \(1\oplus1\). Globally, Proposition 3.1 gives \(1\oplus\bar\chi_5\) for both. The rational isogeny identifies \(V_5E_0,V_5E_1\) but cannot make these distinct inertia actions on integral reductions agree. ∎

## References

These are freely accessible author or institutional copies actually read; their scope is specified in §§5–8 and the accompanying proof record. No bibliographic entry discharges an omitted proof.

- J.-P. Serre, [*Sur les représentations modulaires de degré 2 de Gal(Q̄/Q)*, free author-institution copy](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5835292064138487263_Serre_Repr.modulaires_Galois.pdf), §§1–3, for the original local recipe and the original character formulation.
- J.-P. Serre, [*Formes modulaires (mod p)*, free Collège de France notes](https://www.numdam.org/item/CJPS_1988__8_/), printed pp.53–56, especially the counterexample on pp.54–55.
- P. B. Allen and P. Wake, [*Modular analogs of character formulas and minimal lifts of modular forms*](https://arxiv.org/pdf/2509.21426), version 2, §1.2 and the full §5 argument, for the precise small-characteristic character obstruction. Its modular block-theory dependencies are not used as programme proof substitutes.
- C. Khare and J.-P. Wintenberger, [*Serre's modularity conjecture (I)*](https://www.math.ucla.edu/~shekhar/papers/results.pdf), §§3.1–3.2, 4–5, 8–10; the author PDF has 23 pages.
- C. Khare and J.-P. Wintenberger, [*Serre's modularity conjecture (II)*](https://www.math.ucla.edu/~shekhar/papers/proofs.pdf), §§9–10; the author PDF has 98 pages. The proof dependencies in §10 are distinguished from results proved in this lesson.
- M. Kisin, [*Modularity of 2-adic Barsotti–Tate representations*, free author DVI](https://people.math.harvard.edu/~kisin/dvifiles/serre2.dvi), Theorem 0.1, Corollary 0.2 and §3.3. The DVI is the actual author-page download, not a publisher access link.
- K. A. Ribet and W. A. Stein, [*Lectures on Serre's conjectures*, free author notes](https://wstein.org/papers/serre/ribet-stein.pdf), §§3.9–3.11, printed pp.43–50, for the Mazur principle, pivot argument and its geometric prerequisites.
- J. G. Bosman, [*Explicit computations with modular Galois representations*, freely accessible Leiden thesis](https://math.leidenuniv.nl/scripties/BosmanPhD.pdf), §§1.3.5 and 1.4.1–1.4.4, printed pp.34–41, for the exact classical local recipe and its explicitly identified integrality input.
- B. Ramakrishnan and B. Sahu, [*Identities for the Ramanujan tau function and certain convolution sum identities for the divisor functions*, free author PDF](https://www.niser.ac.in/~brundaban.sahu/imnt-final.pdf), Theorem 2.1(ix),(x) and §4.1. Proposition 6.1 proves the needed identities and congruences locally.

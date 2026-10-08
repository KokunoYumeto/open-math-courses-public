# Quotients and torsors

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the subsection “Ample neighbourhoods and finite descent” by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Original text: public domain (CC0).*

Taking an orbit set forgets functions, nilpotents and families. A scheme quotient must recover all three. For an affine finite groupoid, invariant functions provide the candidate quotient; norms prove that this candidate has the correct points. For an equivalence relation, a further module argument proves that the relation itself is recovered by a fibre product. Torsors will then describe quotients which become ordinary group translations locally.

The base scheme is arbitrary unless a field is specified. We first prove the faithfully flat module and affine descent used below. We assume determinant norms for finite locally free algebras and basic commutative algebra. Finite locally free means finite and locally free as a module, with locally constant finite rank; it does not require a Noetherian base.

## Faithfully flat affine descent

The algebra behind affine descent works without a finiteness condition. Let \(A\to B\) be faithfully flat. A descent datum on a \(B\)-module \(M\) is an isomorphism between its two pullbacks to \(B\otimes_A B\), satisfying the cocycle identity over \(B\otimes_A B\otimes_A B\). Write this isomorphism in the direction

\[
\theta:M\otimes_A B\longrightarrow B\otimes_A M
\]

and put \(\rho(m)=\theta(m\otimes1)\). Linearity, the cocycle identity and restriction to the diagonal give the following three identities. If \(\rho(m)=\sum_i b_i\otimes m_i\), they are

\[
\rho(bm)=(b\otimes1)\rho(m),\qquad
\sum_i b_i m_i=m,\qquad
\sum_i b_i\otimes\rho(m_i)=\sum_i b_i\otimes1\otimes m_i.
\]

The diagonal identity follows from the cocycle: the diagonal restriction of \(\theta\) is both invertible and idempotent, hence is the identity. The last displayed identity is the cocycle applied to \(m\otimes1\otimes1\); the positions of the two scalar factors fix the convention for \(\theta\).

**Lemma. Module descent.** Set

\[
N=\{m\in M:\rho(m)=1\otimes m\}.
\]

Then multiplication is an isomorphism \(B\otimes_A N\to M\), compatible with the descent datum. Equivariant module homomorphisms descend uniquely to \(A\)-linear homomorphisms of the corresponding invariant modules.

**Proof.** The module \(N\) is the kernel of \(d:M\to B\otimes_A M\), \(d(m)=\rho(m)-1\otimes m\). Flatness identifies \(B\otimes_A N\) with the kernel of \(1\otimes d\) inside \(B\otimes_A M\). The cocycle identity puts \(\rho(M)\) in this kernel. Conversely, if \(x=\sum_j c_j\otimes u_j\) is in the kernel, then

\[
\sum_j c_j\otimes\rho(u_j)=\sum_j c_j\otimes1\otimes u_j.
\]

Multiply the first two scalar factors. By the first identity for \(\rho\), the result says \(\rho(\sum_j c_j u_j)=x\). The diagonal identity says that multiplication composed with \(\rho\) is the identity on \(M\). Thus these two maps identify \(M\) with the kernel, proving the asserted isomorphism. Its compatibility with \(\theta\) follows from the last identity for \(\rho\). An equivariant map preserves \(N\); after the isomorphism just proved it is the scalar extension of its restriction. Uniqueness follows from faithful flatness. \(\square\)

**Corollary. Affine descent.** Affine schemes with faithfully flat descent data descend effectively and uniquely. The assertion also holds for affine morphisms over schemes.

**Proof.** For a \(B\)-algebra \(C\), let its descent datum be an algebra isomorphism. The module lemma produces an \(A\)-module \(D\) with \(B\otimes_A D\simeq C\). The unit and multiplication are equivariant maps, so descend uniquely. Associativity, commutativity and the unit identities can be checked after faithful scalar extension; hence \(D\) is an \(A\)-algebra. Taking spectra gives the descended affine scheme and its original datum. Algebra homomorphisms descend by the same argument, giving uniqueness and descent of morphisms.

Over a general base, apply this construction on affine opens. On their overlaps the descended algebras and morphisms are uniquely identified, so their relative spectra glue. This proves the assertion for affine morphisms. In particular a scheme which becomes affine after a faithfully flat field extension is affine: descend the coordinate algebra of that affine base change with its canonical datum. The descended scheme and the original scheme have identical local maps after the cover, and those maps glue uniquely. \(\square\)

The same equalizer argument with \(M=B\) gives

\[
A=\{b\in B:b\otimes1=1\otimes b\}.
\]

It is the elementary mechanism behind the invariant-ring quotients that follow. These proofs supply the module and affine descent prerequisite used in *Diagonalizable groups and groups of multiplicative type*, Section 5. They do not assert effectivity of descent for arbitrary schemes; the ample-neighbourhood argument later in this lesson addresses that additional problem.

We shall also use the positive-degree part of this same descent calculation. For an \(A\)-module \(N\), the augmented **Amitsur complex** has terms \(N\) in degree \(-1\) and \(B^{\otimes_A(p+1)}\otimes_A N\) in degree \(p\geq0\). Its differential is the alternating sum of the maps inserting \(1\) into one of the scalar positions. It is exact. After tensoring with \(B\), distinguish the extra first scalar factor; multiplying that factor by the first ordinary scalar factor defines a homotopy lowering the degree by one. The term inserting \(1\) into the first ordinary position gives the identity, and each other term cancels with its counterpart in the opposite composite. Hence \(hd+dh=1\). Flatness preserves kernels and images, and faithful flatness detects a zero cohomology module, so the original complex is exact as well. This proves both the equalizer assertion and the vanishing of the additive descent obstructions used in the appendix.

## 1. What the quotient must retain

An **\(S\)-groupoid scheme** has an object scheme \(U\), an arrow scheme \(R\), source and target \(s,t:R\to U\), identity, inverse and composition

\[
c:R\times_{s,U,t}R\longrightarrow R.
\]

We write \(r:u\to v\) when \(s(r)=u\), \(t(r)=v\); composition sends a pair \((a,r)\) to \(a\circ r\), with \(s(a)=t(r)\). These conventions are used on every test scheme.

An **equivalence relation** is a groupoid for which

\[
j=(t,s):R\longrightarrow U\times_SU
\]

is a monomorphism. It means that between two fixed test points there is at most one arrow, including over test schemes with nilpotents. For an action of \(G/S\) on \(U\), the action groupoid has \(R=G\times_SU\), source \(u\), and target \(gu\). The action is **schematically free** when its \(j\) is a monomorphism. Freeness only on rational points is weaker.

For affine \(U=\operatorname{Spec}A\) and \(R=\operatorname{Spec}B\), use \(s^\sharp,t^\sharp:A\to B\) for the two ring maps. The invariant ring is

\[
C=\{a\in A:s^\sharp(a)=t^\sharp(a)\}.
\tag{1}
\]

It is a subring, with the inclusion giving \(q:U\to M=\operatorname{Spec}C\). This construction initially uses the underlying schemes and rings. When \(S\) is affine, its functions lie in \(C\), so it is also a construction over \(S\). In the effective quotient below, the map to a general \(S\) descends as part of the universal property.

For a finite abstract group \(\Gamma\) acting on \(A\), its constant action groupoid has

\[
B=\prod_{\gamma\in\Gamma}A,\qquad C=A^\Gamma.
\]

Every \(a\in A\) satisfies the invariant monic polynomial

\[
\prod_{\gamma\in\Gamma}(T-\gamma(a)).
\tag{2}
\]

Thus \(A\) is integral over \(A^\Gamma\), and lying over makes \(q\) surjective. An invariant morphism \(U\to\operatorname{Spec}D\) is exactly a ring map \(D\to A\) whose image is invariant, so it factors uniquely through \(C\). This proves the affine categorical property without any division by \(|\Gamma|\).

If \(\Lambda\) is a flat algebra over the ground ring, flatness preserves the kernel of

\[
A\longrightarrow\prod_{\gamma\in\Gamma}A,\qquad
a\longmapsto(\gamma(a)-a)_\gamma.
\]

Consequently taking invariants commutes with that flat base change. The same kernel argument will work for any finite locally free affine groupoid. The proof that geometric fibres are orbits requires more: it will follow from the norm argument of Section 3.

**Example 1.1. A singular quotient.** Let \(\operatorname{char}k\ne2\), and let the nonidentity element of \(\mathbf Z/2\) send \((x,y)\) to \((-x,-y)\). A polynomial is invariant exactly when its monomials have even total degree. Every such monomial is a product of \(x^2,xy,y^2\). Hence

\[
k[x,y]^{\mathbf Z/2}
\simeq k[u,v,w]/(uw-v^2),
\qquad (u,v,w)=(x^2,xy,y^2).
\tag{3}
\]

For completeness, the indicated relation generates the kernel: reducing by \(v^2=uw\) expresses every polynomial as \(F(u,w)+vH(u,w)\). Its image is the sum of monomials whose two exponents are even and monomials whose two exponents are odd, respectively. These distinct monomials are linearly independent, so only the zero reduced polynomial maps to zero.

The cone in (3) has dimension two and a three-dimensional tangent space at its vertex, because its equation has no linear term. It is singular there. The action is not free at the origin; the quotient theorem for a free action will have a stronger conclusion. In characteristic two this particular action is trivial, so the stated invariant-ring computation has an essential characteristic condition.

## 2. Norms make invariant equations

Assume now that \(U,R\) are affine and both source and target are finite locally free. Their ranks are positive: the identity section makes each map surjective.

For \(f\in A\), define the source norm

\[
N(f)=\det\bigl(m_{t^\sharp(f)}:B\to B\bigr),
\tag{4}
\]

where \(B\) is viewed as a finite projective \(A\)-module through \(s^\sharp\), and \(m\) means multiplication. The determinant is defined on each constant-rank open and these functions glue. It commutes with arbitrary scalar extension.

**Lemma 2.1. Norm invariance.** The function \(N(f)\) belongs to \(C\).

**Proof.** Over the universal arrow \(r\in R(R)\), composition with \(r\) identifies the family of arrows with source \(t(r)\) with the family of arrows with source \(s(r)\):

\[
a\longmapsto a\circ r,\qquad
a\circ r\longmapsto(a\circ r)\circ r^{-1}.
\]

These are mutually inverse scheme morphisms over \(R\), by the groupoid identities. Composition does not change the final target. Therefore the function \(t^\sharp(f)\), and multiplication by it on these two finite locally free families, correspond under this isomorphism. Their determinants are equal.

The first determinant is the pullback of \(N(f)\) by \(t\), and the second is its pullback by \(s\), by base-change compatibility of the determinant. Thus \(t^\sharp(N(f))=s^\sharp(N(f))\), proving (1). \(\square\)

The same composition isomorphism shows that source rank is constant along every arrow. Inversion identifies target and source ranks. Thus there is a decomposition

\[
U=\coprod_{r\geq1}U_r
\tag{5}
\]

into invariant open and closed subschemes on which both maps have rank \(r\). Only finitely many occur, because \(U\) is quasi-compact. The idempotent defining \(U_r\) is invariant: its source and target pullbacks define the same open and closed subset of \(R\), and idempotents are determined by their associated clopen subsets. Hence (5) also decomposes \(C\) and \(M\). This proves the rank-decomposition assertion, including its schematic invariance.

**Theorem 2.2. Integrality.** The algebra \(A\) is integral over \(C\).

**Proof.** Use (5) to reduce to constant rank \(r\). Apply Lemma 2.1 to the groupoid with an extra coordinate \(T\), and the function \(T-f\). Its norm is

\[
P_f(T)=\det(T-m_{t^\sharp(f)})\in C[T].
\tag{6}
\]

It is monic of degree \(r\). Cayley–Hamilton on the finite projective \(A\)-module \(B\) gives

\[
s^\sharp(P_f)(t^\sharp(f))=0.
\]

Since each coefficient is invariant, the left side is \(t^\sharp(P_f(f))\). Pulling back along the identity section, which is a left inverse of \(t^\sharp\), gives \(P_f(f)=0\). Each element of \(A\) therefore satisfies an invariant monic polynomial.

For several rank pieces, take a common positive multiple \(n\) of their ranks and on the rank-\(r\) piece use \(P_f^{n/r}\). The resulting polynomials glue across the idempotent decomposition to a monic degree-\(n\) polynomial over \(C\) annihilating \(f\). This proves integrality globally. \(\square\)

*Comparison locators:* [Stacks, Tags 03BH–03BJ]. Integrality is the conclusion at this stage; no finite generation of \(A\) over \(C\) has been assumed.

## 3. Base change and the actual fibres

Let \(C\to D\) be any ring map, and put

\[
A_D=A\otimes_CD,\qquad B_D=B\otimes_CD,\qquad
C_D^{\mathrm{inv}}=\ker(s_D^\sharp-t_D^\sharp:A_D\to B_D).
\]

The groupoid maps descend to these algebras because source and target agree on \(C\). There is a natural map \(\phi:D\to C_D^{\mathrm{inv}}\). Non-flat scalar extension may fail to preserve its being an isomorphism.

**Lemma 3.1. Base-change control.** The following assertions hold.

1. If \(D\) is flat over \(C\), then \(\phi\) is an isomorphism.
2. Every element of \(\ker\phi\) is nilpotent.
3. For each \(f\in C_D^{\mathrm{inv}}\), there is a positive integer \(n\) and a polynomial \(P\in D[T]\) whose image in \(C_D^{\mathrm{inv}}[T]\) is \((T-f)^n\).

**Proof.** Equation (1) is a kernel of \(C\)-modules. Tensoring with a flat module preserves the exact sequence at that kernel, proving assertion 1.

The integral inclusion \(C\subset A\) gives an integral surjection on spectra. It remains surjective after every base change, so \(\operatorname{Spec}A_D\to\operatorname{Spec}D\) is surjective. Any element in the kernel \(D\to A_D\) therefore lies in every prime of \(D\), and is nilpotent. Since \(C_D^{\mathrm{inv}}\subset A_D\), this kernel is exactly \(\ker\phi\), proving assertion 2.

For assertion 3, first use the invariant idempotents to reduce to constant rank \(r\). Choose a polynomial \(C\)-algebra \(E\) with a surjection \(E\to D\), and lift \(f\) to \(g\in A\otimes_CE\). The algebra \(E\) is flat over \(C\), including when it has infinitely many variables. Apply the norm construction to \(T-g\) in this scalar-extended groupoid. By Lemma 2.1 its coefficients are invariant, and assertion 1 identifies those invariants with \(E\). Thus it gives a polynomial \(Q\in E[T]\).

After applying \(E\to D\), invariance of \(f\) says \(t_D^\sharp(f)=s_D^\sharp(f)\). Multiplication by \(t_D^\sharp(T-f)\) is now scalar multiplication by \(T-f\) on a rank-\(r\) module. Its determinant is \((T-f)^r\). The image of \(Q\) in \(D[T]\) is the required \(P\).

For varying ranks, take a common multiple \(n\) and raise each rank-\(r\) polynomial to \(n/r\). The rank idempotents come from \(C\), so persist in \(D\); the resulting polynomials glue over \(D\). \(\square\)

We now identify the fibres without assuming flatness of \(q\).

**Theorem 3.2. Points of the invariant quotient.** The morphism \(q:U\to M=\operatorname{Spec}C\) is integral and surjective. Its point fibres are the groupoid orbits:

\[
|M|=|U|/|R|.
\tag{7}
\]

For every algebraically closed field \(K\), it also satisfies

\[
M(K)=U(K)/R(K).
\tag{8}
\]

Moreover \(j:R\to U\times_MU\) is surjective.

**Proof.** Integrality is Theorem 2.2, and surjectivity is lying over for the inclusion \(C\subset A\). Fix a point \(C\to K\), where \(K\) is algebraically closed. The algebra \(A_K\) is nonzero and integral over \(K\). Every prime residue field is therefore algebraic over \(K\), and equals \(K\). This supplies a lift in \(U(K)\), proving surjectivity in (8).

Suppose \(u_0,u_1\in U(K)\) have the same image in \(M(K)\). There are only finitely many arrows with source \(u_1\) on \(K\)-points, since that source fibre is a finite \(K\)-scheme. List their targets as \(v_1,\ldots,v_m\). If no arrow went from \(u_1\) to \(u_0\), all these points would differ from \(u_0\). In \(A_K\), the Chinese remainder theorem for these finitely many distinct maximal ideals supplies a function \(f\) with

\[
f(u_0)=0,\qquad f(v_i)=1\quad(1\leq i\leq m).
\]

Take its norm \(g=N(f)\) in the scalar-extended groupoid. At \(u_1\), the function \(t^\sharp(f)\) has value \(1\) at every point of the finite source fibre. It is therefore a unit in that finite-dimensional algebra, and its determinant is nonzero. Thus \(g(u_1)\ne0\). At \(u_0\), the identity arrow has target \(u_0\), where \(f\) vanishes. Multiplication by \(t^\sharp(f)\) on that source fibre is not invertible, so its determinant is zero. Thus \(g(u_0)=0\).

But \(g\) is invariant. Lemma 3.1 supplies \(P\in K[T]\) whose image is \((T-g)^n\) for some \(n>0\). Evaluating at \(u_0,u_1\) gives the two equalities in \(K[T]\)

\[
P(T)=(T-g(u_0))^n=(T-g(u_1))^n.
\]

Each of these polynomials has its indicated value as its unique root, so the values must agree. This contradicts their being zero and nonzero. There is an arrow between the two points. The converse is immediate from invariance, proving (8).

For two ordinary points over one \(m\in M\), their residue fields are algebraic over \(\kappa(m)\), by integrality. Embed both into an algebraic closure \(K\) of \(\kappa(m)\), thereby lifting them to points with the same map \(C\to K\). Equation (8) supplies an arrow; its image in \(R\) connects the original points. This proves (7).

Finally, take any point \(z\in U\times_MU\) and extend its residue field to an algebraic closure. The two resulting \(K\)-points have the same \(M(K)\)-image, so (8) supplies a \(K\)-arrow mapping to \(z\). Hence \(j\) is surjective on the entire fibre product. \(\square\)

*Comparison locators:* [Stacks, Tags 03BK–03BL]. The argument detects arrows after residue-field extension, rather than assuming that ordinary \(k\)-points see all fibres.

In particular finite constant group actions have the orbit fibres promised in Section 1. The finite locally free groupoid hypotheses do not, by themselves, make \(j\) an isomorphism: stabilizer arrows may remain. The next argument uses the equivalence-relation condition to eliminate exactly that issue.

## 4. Recovering the relation, including its nilpotents

We continue with affine \(U=\operatorname{Spec}A\), \(R=\operatorname{Spec}B\) and invariant ring \(C\). All module structures on \(B\) in this section use \(s^\sharp\).

**Lemma 4.1. An invariant basis.** Suppose there are \(x_1,\ldots,x_r\in A\) such that \(t^\sharp(x_1),\ldots,t^\sharp(x_r)\) form an \(A\)-basis of \(B\). Then \(x_1,\ldots,x_r\) form a \(C\)-basis of \(A\), and the natural map

\[
A\otimes_CA\longrightarrow B,\qquad
a\otimes b\longmapsto s^\sharp(a)t^\sharp(b)
\tag{9}
\]

is an isomorphism.

**Proof.** For any \(a\in A\), uniquely write

\[
t^\sharp(a)=\sum_i s^\sharp(a_i)t^\sharp(x_i),\qquad a_i\in A.
\tag{10}
\]

Take the universal composable arrows \(r:u\to v\) and \(q:v\to w\). Applying (10) to \(q\) evaluates the coefficients at \(v\), whereas applying it to \(q\circ r\) evaluates them at \(u\). Both expressions evaluate \(a\) at \(w\). Subtracting gives

\[
\sum_i\bigl(a_i(v)-a_i(u)\bigr)x_i(w)=0.
\]

This is an equality of functions on the scheme of composable arrows, not merely an equality on field-valued points. Viewed as a scheme over the universal \(r\), its arrow \(q\) varies in the source fibre over \(t(r)\). Its coordinate module is the base change of \(B\) along \(t^\sharp:A\to B\), and the \(x_i(w)\) are the base-changed basis. Thus each coefficient vanishes in \(B\):

\[
t^\sharp(a_i)=s^\sharp(a_i).
\]

So \(a_i\in C\). Pulling (10) back along the identity arrow gives \(a=\sum_i a_ix_i\). Conversely, a \(C\)-linear relation among the \(x_i\), after applying \(t^\sharp\), becomes an \(A\)-linear relation among the prescribed basis of \(B\). Its coefficients vanish under \(s^\sharp\), which is injective because the identity is a retraction. Therefore \(A=\bigoplus_iCx_i\). Map (9) sends the resulting \(A\)-basis \(1\otimes x_i\) to the \(A\)-basis \(t^\sharp(x_i)\), proving the last assertion. \(\square\)

We next produce such a basis without a Noetherian hypothesis.

**Lemma 4.2. Simultaneous basis selection.** Let \(C\) be local with infinite residue field \(k\), let \(A\) be an integral semilocal \(C\)-algebra, and let \(B\) be a finite projective \(A\)-module of constant rank \(r\). Suppose \(s^\sharp,t^\sharp:A\to B\) are ring maps agreeing on \(C\), and that \(t^\sharp(A)\) spans \(B\) as an \(A\)-module through \(s^\sharp\). Then some \(t^\sharp(x_1),\ldots,t^\sharp(x_r)\), with \(x_i\in A\), are an \(A\)-basis.

**Proof.** Choose \(z_1,\ldots,z_N\in A\) whose images under \(t^\sharp\) span \(B\). There are finitely many maximal ideals \(\mathfrak n_j\) of \(A\). Since \(A/C\) is integral, every one contracts to the maximal ideal of \(C\), and its residue field \(K_j\) is algebraic over \(k\).

Choose a basis of the \(r\)-dimensional vector space \(B\otimes_AK_j\). The determinant of the \(r\) proposed vectors

\[
\sum_{\nu=1}^N\lambda_{\nu i}t^\sharp(z_\nu)
\quad(1\leq i\leq r)
\]

is a polynomial \(F_j\) in the \(Nr\) coefficients \(\lambda_{\nu i}\), with coefficients in \(K_j\). It is nonzero because the \(t^\sharp(z_\nu)\) span that vector space. Embed the finitely many \(K_j\) in a common algebraic closure of \(k\). The product of the nonzero \(F_j\) is still nonzero. A nonzero polynomial over any extension of an infinite field cannot vanish at all tuples from that field: for one variable this is the bound on the number of roots, and induction on the number of variables, applied to a nonzero coefficient polynomial, proves the assertion in general. Choose one tuple in \(k^{Nr}\) avoiding this product and lift its entries to \(C\).

Put \(x_i=\sum_\nu\lambda_{\nu i}z_\nu\), using these lifts. Because the two ring maps agree on \(C\), \(t^\sharp(x_i)\) are the chosen linear combinations. They give a basis in every maximal fibre. The cokernel of \(A^r\to B\) is finite and has zero localization at every maximal ideal, by Nakayama's lemma, so it is zero. Since \(B\) is projective, this surjection splits. Its kernel is a finite projective module of rank zero at every maximal ideal and is therefore zero. \(\square\)

**Theorem 4.3. The affine effective quotient.** Suppose \(j=(t,s)\) is a monomorphism and \(s,t:R\to U\) are finite locally free. Then

\[
q:U\longrightarrow M=\operatorname{Spec}C
\]

is finite locally free and surjective, map (9) is an isomorphism, and

\[
R\simeq U\times_MU.
\tag{11}
\]

Moreover \(M\) represents the fppf sheaf quotient \(U/R\). In particular every invariant morphism from \(U\) to any scheme factors uniquely through \(q\), and formation of this effective quotient is compatible with every base change on \(M\).

**Proof.** First, \(R\to U\times_{\operatorname{Spec}\mathbf Z}U\) is a monomorphism: \(j\) is one, and \(U\times_SU\to U\times_{\operatorname{Spec}\mathbf Z}U\) is one. It is finite, because any finite generating set of \(B\) as an \(A\)-module through \(s^\sharp\) also generates it over \(A\otimes_{\mathbf Z}A\). A finite monomorphism is a closed immersion [Stacks, Tag 03BB]. Hence

\[
A\otimes_{\mathbf Z}A\longrightarrow B
\]

is surjective. It factors through (9), since the two maps agree on \(C\); consequently (9) is surjective and \(t^\sharp(A)\) spans \(B\) over \(s^\sharp(A)\).

Fix a prime \(\mathfrak p\) of \(C\). Localize at it and then make the faithfully flat local extension

\[
C_{\mathfrak p}\longrightarrow
C' = C_{\mathfrak p}[Z]_{\mathfrak p C_{\mathfrak p}[Z]}.
\tag{12}
\]

This ring has residue field \(\kappa(\mathfrak p)(Z)\), which is infinite. The extension is flat as a polynomial extension followed by localization, and faithful because it is a local flat map with nonzero residue fibre. Lemma 3.1 identifies the invariants after this extension with \(C'\).

By Theorem 2.2, \(A'=A\otimes_CC'\) is integral over \(C'\). It is semilocal. Indeed all its maximal ideals lie over the unique closed point of \(\operatorname{Spec}C'\). Fix one such maximal point of \(\operatorname{Spec}A'\), which exists by lying over. The orbit-fibre assertion of Theorem 3.2 puts every other maximal point in its orbit. A source fibre of the finite map \(s\) has finitely many points; its targets therefore include only finitely many points. Thus there are finitely many maximal ideals of \(A'\).

The invariant rank decomposition of Section 2 makes \(B'=B\otimes_CC'\) have one positive rank \(r\) over \(A'\): its finitely many rank idempotents are in the local invariant ring \(C'\), and only one can be nonzero. Surjectivity of (9) persists under base change. Apply Lemma 4.2, then Lemma 4.1. They show that \(A'\) is free of rank \(r\) over \(C'\) and that the scalar extension of (9) is an isomorphism.

Faithful flatness in (12), for each \(\mathfrak p\), now detects that (9) is an isomorphism globally and that \(A\) is flat over \(C\). Theorem 3.2 already gave surjectivity of \(q\), so \(C\to A\) is faithfully flat. As an \(A\)-module, its base change \(A\otimes_CA\) is the finite projective module \(B\). Finite presentation and finite generation of modules descend under faithfully flat ring maps [Stacks, Tag 03C4]. Thus \(A\) is finite and finitely presented over \(C\); together with flatness this says it is finite projective. This proves that \(q\) is finite locally free and proves (11).

For completeness, these algebraic conclusions give the asserted sheaf quotient directly. Every map \(T\to M\) lifts to \(U\) after the fppf covering \(U\times_MT\to T\). Two lifts have the same image in \(M\) exactly when they are the source and target of a unique \(R\)-arrow, by (11). Hence the associated fppf sheaf of the orbit presheaf \(U/R\) is \(M\). A morphism from this quotient to any fppf sheaf is exactly an invariant morphism from \(U\); represented target schemes are fppf sheaves. This also descends the structural map to a possibly nonaffine \(S\), making \(M\) an \(S\)-scheme.

After arbitrary base change on \(M\), \(q\) remains a finite locally free surjection and (11) remains an isomorphism. The same lifting argument proves the base-change assertion. \(\square\)

*Comparison locators:* [Stacks, Tags 03C8 and 03BM]. The distinction between flat base change of invariants for a general groupoid and arbitrary base change of an effective equivalence-relation quotient is essential.

**Corollary 4.4. Finite free group actions.** Let a finite constant group \(\Gamma\) act schematically freely on an affine \(S\)-scheme \(U\). Its invariant quotient \(q:U\to M\) is finite étale and is a \(\Gamma\)-torsor.

**Proof.** Its action groupoid is an equivalence relation, and \(s\) is the projection \(\Gamma_S\times_SU\to U\), a finite locally free map; inversion gives the same property for \(t\). Theorem 4.3 gives

\[
\Gamma_S\times_SU\simeq U\times_MU.
\]

After the faithfully flat base change \(q\), the map \(q\) is therefore the finite étale projection \(\Gamma_S\times_SU\to U\). Étaleness descends faithfully flatly, so \(q\) is finite étale. The displayed isomorphism and the fppf covering \(q\) are precisely the torsor conditions. \(\square\)

This has no condition on \(|\Gamma|\). For example, translation \(x\mapsto x+1\) by \(\mathbf F_p\) on the affine line in characteristic \(p\) is free and has finite étale quotient, although the group order equals the characteristic.

## 5. From affine orbit neighbourhoods to a scheme

**Lemma 5.1. Invariant affine neighbourhoods.** Let \((U,R,s,t,c)\) be a groupoid scheme with \(s,t\) finite locally free. Suppose the orbit \(F\) of a point of \(U\) is contained in an affine open \(W\). Then there is an invariant affine open containing \(F\).

**Proof.** The orbit is a finite set, since it consists of targets of a finite source fibre. Define the closed subset

\[
E=R\setminus\bigl(s^{-1}W\cap t^{-1}W\bigr)
\]

and the open subset \(W'=U\setminus t(E)\). The image \(t(E)\) is closed because \(t\) is finite. A point lies in \(W'\) exactly when its entire orbit lies in \(W\): if an arrow has that target, its source must lie in \(W\); conversely arrows to points of \(W\) with every source in \(W\) avoid \(E\). Inversion and composition make this condition constant on orbits. Thus \(W'\) is invariant, contained in \(W\), and contains \(F\).

Let \(I\subset\Gamma(W,\mathcal O_W)\) define the closed subset \(W\setminus W'\). No prime corresponding to a point of \(F\) contains \(I\). Finite prime avoidance supplies \(f\in I\) outside all those primes [Stacks, Tag 00DS]. Therefore

\[
F\subset D_W(f)\subset W'.
\]

On \(W'\), take the determinant norm \(g=N_s(t^*f)\) for the restricted finite locally free groupoid. Lemma 2.1 is local on the object scheme, so it proves that \(g\) is invariant here as well. Its nonvanishing at a point is equivalent to \(f\) being a unit at every target in that point's source fibre. This follows by taking the determinant in the finite-dimensional residue-field algebra: multiplication is invertible exactly when the element lies in no maximal ideal.

It follows that \(g\) is nonzero at every point of \(F\), and that \(D_{W'}(g)\) is invariant. The identity arrow shows

\[
D_{W'}(g)\subset D_W(f).
\]

The open on the right is affine and contained in \(W'\). Restricting the regular function \(g\) to it gives

\[
D_{W'}(g)=D_{D_W(f)}(g),
\]

a principal open of an affine scheme. This is the required invariant affine neighbourhood. \(\square\)

*Comparison locator:* [Stacks, Tag 03JE].

**Theorem 5.2. The global finite quotient.** Let \(R\rightrightarrows U\) be an equivalence relation of \(S\)-schemes, with \(s,t\) finite locally free. Assume each orbit is contained in an affine open of \(U\). Then the fppf sheaf quotient \(U/R\) is a scheme \(M\), the map \(q:U\to M\) is a finite locally free surjection, and \(R\simeq U\times_MU\).

**Proof.** Lemma 5.1 supplies an invariant affine open cover \(U_i\) of \(U\). The restriction \(R_i=s^{-1}(U_i)=t^{-1}(U_i)\) is finite over the affine \(U_i\), hence affine. Theorem 4.3 gives an effective quotient \(q_i:U_i\to M_i\).

An invariant open \(V\subset U_i\) descends to an open of \(M_i\). To see this without presuming a quotient theorem for \(V\), note that \(q_i\) is integral and closed. The invariant closed complement \(U_i\setminus V\) is a union of whole fibres, by Theorem 3.2. Its image is therefore closed, and

\[
O=M_i\setminus q_i(U_i\setminus V),\qquad q_i^{-1}(O)=V.
\]

Restriction of the finite locally free covering \(q_i\) and of its relation shows that \(O\) represents the fppf quotient \(V/R|_V\), by the lifting proof in Theorem 4.3.

Apply this to \(V=U_i\cap U_j\). Its quotient is represented by open subschemes of both \(M_i\) and \(M_j\). The two opens identify uniquely because they represent the same sheaf. On triple intersections these identifications satisfy the cocycle condition, again by uniqueness. Glue the \(M_i\) along them to obtain a scheme \(M\).

The maps \(q_i\) glue to \(q\), with \(q^{-1}(M_i)=U_i\). Finiteness, local freeness and surjectivity are local on the target, and the isomorphisms \(R_i\simeq U_i\times_{M_i}U_i\) cover the relation. Hence they give the asserted properties of \(q\) and the global equality \(R\simeq U\times_MU\). The fppf lifting argument identifies \(M\) with \(U/R\). \(\square\)

The affine-orbit hypothesis has a concrete role: it produces the affine charts which can be glued. It is automatic for an affine \(U\), but is not to be silently removed for an arbitrary scheme.

**Corollary 5.3. Radicial finite descent.** Let \(X\to Y\) be surjective, finite locally free and radicial. Every descent datum on a scheme \(V\to X\) is effective.

**Proof.** A descent datum identifies the two pullbacks of \(V\) to \(X\times_YX\), with the usual identity and cocycle conditions. It makes

\[
R=V\times_YX\rightrightarrows V
\]

an equivalence relation: source forgets the new \(X\)-coordinate, while target transports the point of \(V\) to that coordinate using the datum. The arrow is determined by its source and target, since the target specifies the new \(X\)-coordinate. Thus its map to \(V\times_YV\) is a monomorphism. The source is the base change of \(X\to Y\), and target has the same properties by inversion.

The source \(R\to V\) is a universal homeomorphism, with the identity as a section. Its unique point over any point of \(V\) is therefore the identity point. Source and target agree on underlying points, so every orbit is a singleton. Such an orbit always lies in an affine open. Theorem 5.2 gives a scheme quotient \(W\) and a finite locally free surjection \(V\to W\). The invariant map \(V\to Y\) descends to \(W\to Y\).

The comparison \(V\to W\times_YX\) is an isomorphism. Indeed, after the faithfully flat base change \(V\to W\), it becomes the isomorphism

\[
V\times_WV\simeq R=V\times_YX
\]

which remembers the source and the \(X\)-coordinate of the target. Isomorphisms descend faithfully flatly. This recovers \(V\) with its given datum from \(W\), proving effectivity. \(\square\)

*Comparison locator:* [Stacks, Tag 0H8L].

### Ample neighbourhoods and finite descent

By Theorem 5.2, a descent datum along a finite locally free covering is effective once every orbit of the associated equivalence relation lies in an affine open. Orbits are finite, so what is needed is one affine open containing a given finite set of points, not an affine neighbourhood of each point separately. Ample invertible sheaves provide such opens. Here an invertible sheaf \(L\) on a scheme \(Z\) is **ample** if \(Z\) is quasi-compact and \(Z\) is covered by the opens \(Z_s=\{z:s(z)\ne0\}\) that are affine, where \(s\) runs over global sections of \(L^{\otimes n}\), \(n\ge1\). The results of this subsection are proved in the Stacks Project, *Properties*, Tags 01PW, 01Q1 and 01ZY, and *Algebra*, Tag 00JS (homogeneous prime avoidance).

**Lemma 5.4. Finite sets and an ample sheaf.** If a scheme has an ample invertible sheaf, each finite set of its points lies in some affine open. The same conclusion holds for a scheme that embeds as a locally closed subscheme of \(\operatorname{Proj}R\), where \(R\) is any graded ring.

**Proof.** *Step 1: sections over \(Z_s\).* Let \(L\) be ample on \(Z\) and let \(R=\bigoplus_{n\ge0}\Gamma(Z,L^{\otimes n})\). Choose finitely many sections \(s_1,\ldots,s_m\) of positive degrees with affine \(Z_{s_i}\) covering \(Z\). If \(Z_s\) is affine and \(t\) has degree \(b\), then \(Z_s\cap Z_t\) is the locus in \(Z_s\) where the function \(t^{a}/s^{b}\) does not vanish, \(a=\deg s\). So it is a principal open of an affine scheme, hence affine. The pairwise intersections of the \(Z_{s_i}\) are therefore affine, so \(Z\) is quasi-compact and quasi-separated.

Let \(s\in\Gamma(Z,L^{\otimes d})\) with \(d\ge1\). Sending \(a/s^k\), for \(a\in\Gamma(Z,L^{\otimes dk})\), to the function \(a|_{Z_s}/(s|_{Z_s})^k\) defines a ring map

\[
R_{(s)}\longrightarrow\Gamma(Z_s,\mathcal O_Z)
\]

from the degree-zero part of \(R_s\). We show that it is bijective. Cover \(Z\) by finitely many affine opens \(U_j=\operatorname{Spec}A_j\) on which \(L\) is trivial, and let \(s_j\in A_j\) correspond to \(s\) under a trivialization; then \(Z_s\cap U_j=\operatorname{Spec}(A_j)_{s_j}\). If \(a/s^k\) maps to zero, each local function \(a_j\) of \(a\) vanishes in \((A_j)_{s_j}\), so \(s_j^{N}a_j=0\) for one \(N\) that works for all \(j\). Then \(s^Na=0\) and \(a/s^k=0\) in \(R_{(s)}\). The same argument applies to sections over any quasi-compact open in place of \(Z\). Conversely, let \(\varphi\) be a function on \(Z_s\). On \(Z_s\cap U_j\) it is \(c_j/s_j^{n}\) for some \(c_j\in A_j\), with one exponent \(n\) for all \(j\). So \(s^n\varphi\) extends over each \(U_j\) to a section \(\gamma_j\) of \(L^{\otimes dn}\). Two such extensions agree on \(Z_s\cap U_j\cap U_l\), and \(U_j\cap U_l\) is quasi-compact because \(Z\) is quasi-separated. By the injectivity argument on \(U_j\cap U_l\), a single power \(s^M\) kills all the differences \(\gamma_j-\gamma_l\). The sections \(s^M\gamma_j\) therefore glue to a global section \(\gamma\) of \(L^{\otimes d(n+M)}\), and \(\varphi\) is the image of \(\gamma/s^{n+M}\).

*Step 2: an open immersion into \(\operatorname{Proj}R\).* By Step 1, \(Z_{s_i}=\operatorname{Spec}\Gamma(Z_{s_i},\mathcal O_Z)\cong\operatorname{Spec}R_{(s_i)}=D_+(s_i)\). On \(Z_{s_i}\cap Z_{s_j}=Z_{s_is_j}\) both identifications are induced by the ring map \(R_{(s_is_j)}\to\Gamma(Z_{s_is_j},\mathcal O_Z)\), so they glue to a morphism \(Z\to\operatorname{Proj}R\). At a point of \(Z_{s_j}\), the image lies in \(D_+(s_i)\) exactly when \(s_i\) does not vanish there. So the preimage of \(D_+(s_i)\) is \(Z_{s_i}\), which maps isomorphically onto it, and \(Z\) is isomorphic to the open subscheme \(\bigcup_iD_+(s_i)\) of \(\operatorname{Proj}R\). It therefore suffices to prove the general statement.

*Step 3: a locally closed subscheme of \(\operatorname{Proj}R\).* Let \(Z\subset\operatorname{Proj}R\) be locally closed, and let \(E=\{z_1,\ldots,z_r\}\subset Z\), with homogeneous primes \(\mathfrak p_1,\ldots,\mathfrak p_r\). The set \(Z\) is open in its closure, so \(T=\overline Z\setminus Z\) is closed in \(\operatorname{Proj}R\). The opens \(D_+(h)\), with \(h\) homogeneous of positive degree, form a basis of \(\operatorname{Proj}R\). Choose such \(h_1,\ldots,h_n\) with \(E\subset\bigcup_kD_+(h_k)\) and \(D_+(h_k)\cap T=\varnothing\), and let \(I=(h_1,\ldots,h_n)\). No \(\mathfrak p_j\) contains \(I\). We find a homogeneous \(f\in I\) of positive degree that lies in no \(\mathfrak p_j\).

Since the grading has no negative degrees, every homogeneous element of \(I\) has positive degree. A homogeneous element avoiding a prime \(\mathfrak q\) avoids every prime contained in \(\mathfrak q\). We may therefore keep only the primes \(\mathfrak p_j\) that are maximal for inclusion in the list; these are pairwise incomparable. We now induct on their number \(r\). For \(r=1\), some \(h_k\notin\mathfrak p_1\). Let \(r\ge2\), and let \(f'\in I\) be homogeneous and outside \(\mathfrak p_1,\ldots,\mathfrak p_{r-1}\). If \(f'\notin\mathfrak p_r\) we are done. Otherwise, the homogeneous ideal \(I\mathfrak p_1\cdots\mathfrak p_{r-1}\) is not contained in the prime \(\mathfrak p_r\), because no factor is. So it contains a homogeneous element \(g\notin\mathfrak p_r\), a product of homogeneous elements of the factors. Put \(f=f'^{\deg g}+g^{\deg f'}\), homogeneous of degree \(\deg f'\deg g>0\). Modulo \(\mathfrak p_r\) only the second term survives, and modulo \(\mathfrak p_j\), \(j<r\), only the first. Hence \(f\) lies in no \(\mathfrak p_j\). No assumption on residue fields is involved.

Now \(E\subset D_+(f)\). Since \(f\in I\), every homogeneous prime not containing \(f\) misses some \(h_k\), so \(D_+(f)\subset\bigcup_kD_+(h_k)\), and \(D_+(f)\) does not meet \(T\). Thus \(Z\cap D_+(f)=\overline Z\cap D_+(f)\) is closed in \(D_+(f)\). An immersion with closed image is a closed immersion, so the open subscheme \(Z\cap D_+(f)\) of \(Z\) is closed in \(D_+(f)=\operatorname{Spec}R_{(f)}\) and hence affine. It contains \(E\). \(\square\)

**Theorem 5.5. Finite locally free descent with ample neighbourhoods.** Suppose \(X\to Y\) is finite locally free and surjective, and let \(V\to X\) carry a descent datum relative to \(X\to Y\). The datum is effective if \(V\to X\) is projective or quasi-projective, if \(V\) has an ample invertible sheaf, or if \(V\) has an \(X\)-ample or an \(X\)-very ample invertible sheaf.

**Proof.** The construction in the proof of Corollary 5.3 turns the datum into an equivalence relation \(R_V=V\times_YX\rightrightarrows V\) with finite locally free projections. It uses only the identity and cocycle conditions, not radiciality. An orbit of \(R_V\) lies over a single point \(y\in Y\), and it is finite because the fibre of \(X\to Y\) over \(y\) is finite. By Theorem 5.2 it suffices to show that each finite set \(E\subset V\) lying over one point \(y\) is contained in an affine open of \(V\).

If \(V\) has an ample invertible sheaf, this is Lemma 5.4. In the other cases, replace \(Y\) by an affine open neighbourhood of \(y\), and \(X\) and \(V\) by the parts over it, which contain \(E\). Then \(X\) is affine, since a finite morphism is affine. Over the affine scheme \(X\), an \(X\)-ample invertible sheaf on \(V\) is ample in the sense used above. Following the Stacks Project, *quasi-projective* means of finite type with an \(X\)-ample invertible sheaf, so that case is included. A projective morphism, and a morphism with an \(X\)-very ample sheaf, give an immersion of \(V\) into a projective bundle over \(X\), closed in the projective case. Over the affine \(X=\operatorname{Spec}A\), the projective bundle of a quasi-coherent module \(\mathcal E\) is \(\operatorname{Proj}\operatorname{Sym}_A(\Gamma(X,\mathcal E))\). So \(V\) is a locally closed subscheme of \(\operatorname{Proj}R\) for a graded ring \(R\), and Lemma 5.4 applies.

So Theorem 5.2 gives a scheme \(W\) representing the quotient of \(V\) by \(R_V\), a finite locally free surjection \(V\to W\), and \(V\times_WV\simeq R_V\). The invariant morphism \(V\to Y\) factors through \(W\to Y\). Consider \(V\to W\times_YX\). Pulled back along the faithfully flat \(V\to W\), this map is the isomorphism \(V\times_WV\simeq R_V=V\times_YX\). Isomorphisms descend faithfully flatly, so \(V\cong W\times_YX\), and this isomorphism carries the canonical datum to the given one. \(\square\)

This is the effectivity statement of [AI Integrated Stacks Project, Tag 0CCJ]. The base is arbitrary and the schemes may be nonreduced. Only the given datum is assumed; the ample sheaf itself need not carry a descent datum.

## 6. Torsors are local copies of a group

From here on we use **right** actions. A left action becomes a right action by \(p\cdot g=g^{-1}p\), so the earlier quotient examples also fit this convention.

Let \(G\to S\) be a group scheme. A **pseudo \(G\)-torsor** is an \(S\)-scheme \(P\) with a right action for which

\[
P\times_SG\longrightarrow P\times_SP,\qquad
(p,g)\longmapsto(p,p\cdot g)
\tag{12}
\]

is an isomorphism. This permits empty fibres; it does not assert local existence of sections. A **\(G\)-torsor** means a pseudo-torsor which becomes equivariantly isomorphic to \(G\), with its right regular action, on an fpqc covering of \(S\). For a specified topology \(\tau\), a **\(\tau\)-torsor** requires such trivializations on a \(\tau\)-covering. We use \(\tau=\) Zariski, étale or fppf as needed.

The same definitions apply to a sheaf of groups on a site, with \(P\) a sheaf of sets. For sheaves, (12) says that whenever \(P(T)\) is nonempty, \(G(T)\) acts simply transitively on it. A torsor additionally has sections locally in the site's topology. Representability is a separate assertion. Descent of arbitrary schemes is not always effective, whereas descent of sheaves is. In general fppf torsors under group schemes can require algebraic spaces rather than schemes; the distinction is discussed in [Stacks, Section 036Z, “Variant on torsors in fppf topology”]. These nonrepresentability phenomena belong to the later study of algebraic spaces. The affine-group result below supplies scheme representatives for the computations in this lesson.

**Lemma 6.1. Sections and equivariant maps.** A pseudo-torsor with a section \(p\in P(S)\) is trivial, by the map \(g\mapsto p\cdot g\). A torsor is trivial exactly when it has a global section. Every equivariant morphism of torsors is an isomorphism.

**Proof.** Pull (12) back along the section in its first factor. It becomes the stated isomorphism \(G\simeq P\). The converse follows from the identity section of \(G\). For an equivariant map \(P\to P'\), choose local sections of \(P\) on a covering. The image sections trivialize \(P'\), and in these trivializations the map is the identity on \(G\). Thus it is locally an isomorphism and hence globally one. The same argument works for sheaves. \(\square\)

*Comparison locators:* [Stacks, Tags 0498–049B and 03AH–03AI]. In particular a pseudo-torsor that is merely surjective on underlying points need not be a torsor over an arbitrary base; local sections are part of the condition.

**Proposition 6.2. Representability for affine groups.** Every sheaf \(G\)-torsor in the fpqc or fppf topology is represented by a scheme affine over \(S\) when \(G\to S\) is affine. If \(G\) is also flat, this represented torsor is faithfully flat over \(S\). If \(G\) is flat and locally of finite presentation, it is an fppf torsor.

**Proof.** Choose a covering with sections. Lemma 6.1 identifies the sheaf there with the represented affine schemes \(G_{S_i}\). The identifications on double overlaps are descent data, and satisfy the cocycle condition on triple overlaps. Faithfully flat descent for affine morphisms produces an affine \(S\)-scheme \(P\). Its functor of points agrees with the given sheaf after the cover, hence agrees globally. The action and (12) descend too. Flatness, local finite presentation and surjectivity descend from \(G_{S_i}\to S_i\). In the last case \(P\to S\) is a flat locally finitely presented surjection, and its own pullback gives a section and hence a trivialization. \(\square\)

**Theorem 6.3. Smooth torsors have étale local sections.** If \(G\to S\) is smooth, every represented fpqc \(G\)-torsor \(P\) is an étale torsor.

**Proof.** The local identifications \(P_{S_i}\simeq G_{S_i}\) imply that \(P\to S\) is smooth and surjective by faithfully flat descent. For each \(s\in S\), the étale-local-section theorem for smooth morphisms gives an étale neighbourhood \(S'\to S\) containing a point over \(s\) and a map \(S'\to P\) [Stacks, Tag 055U]. This is a section of \(P_{S'}\to S'\). Lemma 6.1 trivializes the torsor on \(S'\), and these neighbourhoods cover \(S\). \(\square\)

Notice where smoothness enters: it produces local sections in the étale topology. A flat group such as \(\mu_p\) in characteristic \(p\) instead requires fppf coverings for its general torsors.

## 7. Transition functions and first cohomology

Fix a covering \(\{S_i\to S\}\) in a topology \(\tau\). Write \(S_{ij}=S_i\times_SS_j\) and similarly for triple overlaps. For a right \(G\)-torsor trivialized on this covering, choose sections \(p_i\). There is a unique

\[
g_{ij}\in G(S_{ij}),\qquad p_j=p_i\cdot g_{ij}.
\]

On \(S_{ijk}\) simple transitivity gives

\[
g_{ij}g_{jk}=g_{ik}.
\tag{13}
\]

On the diagonal \(S_i\to S_{ii}\), the pullback of \(g_{ii}\) is \(1\); swapping the two factors identifies \(g_{ji}\) with \(g_{ij}^{-1}\). For a general covering, \(S_{ii}\) need not be \(S_i\), and \(g_{ii}\) need not be \(1\) away from the diagonal. Replacing \(p_i\) by \(p_i\cdot h_i\) replaces the cocycle by

\[
g'_{ij}=h_i^{-1}g_{ij}h_j.
\tag{14}
\]

The set of cocycles modulo (14) is the **nonabelian Čech set** \(\check H^1(\{S_i/S\},G)\). Its distinguished point is the class of the cocycle \(1\). Unless \(G\) is commutative, there is no natural multiplication of its classes.

**Theorem 7.1. Čech classification, with representability specified.** This pointed set classifies sheaf \(G\)-torsors trivialized by the given covering. For affine \(G\), it classifies represented torsors as well. Refining coverings and identifying equivalent classes gives the pointed set \(H^1_\tau(S,G)\) of all sheaf torsors.

**Proof.** Starting with a cocycle, take copies of the right regular \(G\)-sheaf on \(S_i\). On \(S_{ij}\), identify the \(j\)-coordinate \(a\) with the \(i\)-coordinate \(g_{ij}a\). Left multiplication commutes with the right regular action, and (13) makes these identifications agree on triple overlaps. Descent for sheaves glues them into a sheaf \(P\). Locally it is \(G\), hence is a torsor.

Its local identity sections satisfy \(p_j=p_i g_{ij}\), so this recovers the original cocycle. Conversely the local map \(a\mapsto p_i a\) identifies a given torsor with this glued sheaf. Formula (14) gives precisely the change of local sections: the coordinate identification from the new \(i\)-copy to the old one is \(a\mapsto h_i a\). Thus gauge-equivalent cocycles give isomorphic torsors. Any equivariant isomorphism between two glued torsors carries each chosen section to another section and hence is described by such \(h_i\); it yields (14). These constructions are inverse on isomorphism classes and preserve the distinguished points.

Each torsor has local sections on some covering by definition. Two coverings have a common refinement by fibre products. An isomorphism of torsors gives the corresponding gauge relation after such a refinement. These facts prove the global classification. Proposition 6.2 supplies representability in the affine case. \(\square\)

We now check that for an abelian sheaf this torsor definition agrees with **derived** first cohomology; no assumption that a chosen covering computes higher cohomology is needed. On any site write \(\Gamma\) for global sections and \(H^1\) for the first right derived functor of \(\Gamma\).

**Theorem 7.2. Abelian torsors and derived \(H^1\).** For every abelian sheaf \(H\) on a site there is a canonical bijection

\[
\{\text{isomorphism classes of }H\text{-torsors}\}
\simeq H^1(H).
\tag{15}
\]

The trivial torsor corresponds to zero. Under this bijection, addition is the contracted sum of torsors.

**Proof.** Use additive notation. For an \(H\)-torsor \(T\), form the free abelian sheaf \(\mathbf Z[T]\), with augmentation

\[
\epsilon:\mathbf Z[T]\longrightarrow\underline{\mathbf Z},
\qquad \sum_i n_i[t_i]\longmapsto\sum_i n_i.
\]

It is surjective as a sheaf because \(T\) has local sections. There is a well-defined map \(d:\ker\epsilon\to H\). Locally choose a section \(t\) and write \(t_i=t+h_i\); set

\[
d\left(\sum_i n_i[t_i]\right)=\sum_i n_i h_i
\quad\text{when }\sum_i n_i=0.
\]

Changing \(t\) subtracts the same element from every \(h_i\), leaving this sum unchanged. The rule is additive and compatible with restriction, so it defines the map of sheaves. Push out the augmentation sequence along \(d\) to obtain

\[
0\longrightarrow H\longrightarrow E_T
\longrightarrow\underline{\mathbf Z}\longrightarrow0.
\tag{16}
\]

Locally, a section \(t\) identifies \(E_T\) with \(H\oplus\underline{\mathbf Z}\) by \([t+h]\mapsto(h,1)\). Hence the natural map \(T\to E_T\) identifies \(T\) with the fibre over \(1\). Apply the connecting homomorphism of (16) to \(1\); this gives a canonical class \(\xi_T\in H^1(H)\).

We verify both directions explicitly. Embed \(H\) into an injective abelian sheaf \(I\), and put \(Q=I/H\). Since \(H^1(I)=0\), the long exact sequence gives

\[
H^1(H)=\Gamma(Q)/\operatorname{im}\Gamma(I).
\tag{17}
\]

For \(q\in\Gamma(Q)\), the fibre sheaf

\[
T_q=\{x\in I\mid x\bmod H=q\}
\]

is an \(H\)-torsor: \(I\to Q\) is locally surjective, and two lifts differ uniquely by a section of \(H\). Translation by \(i\in\Gamma(I)\) identifies \(T_q\) with \(T_{q+\bar i}\).

Conversely push (16) out from \(H\) to \(I\). The resulting injection \(I\to E_T^I\) has a retraction \(\rho:E_T^I\to I\), because \(I\) is injective. The composite \(T\to E_T\to E_T^I\to I\) is \(H\)-equivariant. Its image in \(Q\) is independent of the local section of \(T\), so it is a global \(q\). Locally the composite is translation between two simply transitive \(H\)-sets; it is therefore an isomorphism \(T\simeq T_q\).

Two choices of \(\rho\) differ by a homomorphism \(\underline{\mathbf Z}\to I\), hence by a global section \(i\) of \(I\), and change \(q\) by \(\bar i\). More generally, any equivariant isomorphism \(T_q\to T_{q'}\) has locally constant difference in the following sheaf sense: if \(x\) is a local lift, subtract \(x\) from its image in \(I\). Equivariance makes this difference independent of the lift, so it glues to \(i\in\Gamma(I)\), with \(q'-q=\bar i\). Thus (17) classifies torsors bijectively.

Finally the map \(E_T\to I\) induced by \(\rho\), together with \(E_T\to\underline{\mathbf Z}\), gives a map from (16) to \(0\to H\to I\to Q\to0\), whose last map sends \(n\) to \(nq\). Naturality of connecting homomorphisms shows \(\xi_T=\delta(q)\). This identifies the just-proved bijection with the canonical construction (16) and proves independence of the chosen injective embedding.

For two torsors the contracted sum identifies \((t+h,t')\) with \((t,t'+h)\). Its local transition differences are the sums of those of the two torsors. Equivalently the local lifts in \(I\) add, giving \(T_{q+q'}\). By (17) this is addition in \(H^1(H)\). \(\square\)

*Comparison locator:* [Stacks, Tag 03AJ]. The inverse constructions and their compatibility are included above.

### Twisting

Let \(P\) be a right \(G\)-torsor and \(V\) a sheaf with a left \(G\)-action. The **associated sheaf**

\[
P\times^GV=(P\times V)/\bigl((p g,v)\sim(p,g v)\bigr)
\tag{18}
\]

is locally \(V\). In the trivialization by \(p_i\), its overlap map from the \(j\)-copy to the \(i\)-copy is \(v\mapsto g_{ij}v\). Equation (13) proves the gluing condition. This establishes the construction, including when no representing scheme has yet been asserted.

For \(V=G\) with conjugation action, the overlap maps are the group automorphisms \(a\mapsto g_{ij}ag_{ij}^{-1}\). Hence \(P\times^GG\) is a sheaf of groups, locally isomorphic to \(G\): the **inner form** obtained by twisting. It is also the sheaf of equivariant automorphisms of \(P\). Indeed, on a trivialized right torsor an equivariant automorphism is left multiplication by one \(a\); changing from the \(j\)-frame to the \(i\)-frame conjugates \(a\) by \(g_{ij}\), exactly as above. If \(G\) is affine, these local group schemes and their morphisms descend to an affine group scheme.

## 8. Frames, line bundles and Hilbert 90

**Theorem 8.1. Torsors for the general linear group.** For any scheme \(S\) and \(n\geq1\), fpqc \(\mathrm{GL}_{n,S}\)-torsors correspond naturally to locally free \(\mathcal O_S\)-modules of rank \(n\). Every such torsor is Zariski-locally trivial. Thus Zariski, étale, fppf and fpqc \(H^1(S,\mathrm{GL}_n)\) all classify the same vector bundles. Over a field \(k\),

\[
H^1(k,\mathrm{GL}_n)=\{1\}.
\tag{19}
\]

**Proof.** A rank-\(n\) bundle \(E\) has a frame functor

\[
\operatorname{Fr}(E)(T)
=\operatorname{Isom}_{\mathcal O_T}(\mathcal O_T^n,E_T).
\]

It has a right action \(\varphi\cdot g=\varphi\circ g\). Locally where \(E\simeq\mathcal O_S^n\), this functor is \(\mathrm{GL}_n\), represented by the determinant-open subset of the affine scheme of matrices. These local schemes glue, and any two frames differ by a unique invertible matrix. Hence \(\operatorname{Fr}(E)\) is a Zariski torsor.

Conversely, choose local sections of a torsor \(P\). Its matrices \(g_{ij}\) satisfy (13), so the maps \(v\mapsto g_{ij}v\) give faithfully flat descent data on the modules \(\mathcal O_{S_i}^n\). Descent for quasi-coherent modules gives \(E\) on \(S\), and finite local freeness of rank \(n\) descends. Equivalently this is the associated bundle \(P\times^{\mathrm{GL}_n}\mathbf A^n\).

There is a natural equivariant map \(P\to\operatorname{Fr}(E)\): a local point \(p\) gives the frame \(v\mapsto[p,v]\). It is equivariant because \([p g,v]=[p,g v]\), and it is an isomorphism in each trivialization. Conversely, the associated bundle of \(\operatorname{Fr}(E)\) identifies with \(E\) by \([\varphi,v]\mapsto\varphi(v)\). Thus the constructions are inverse, independently of the chosen cover.

Since \(E\) is locally free in the Zariski topology, its frame torsor is Zariski-locally trivial, even if the original trivializations used fpqc coverings. Over \(\operatorname{Spec}k\), every \(n\)-dimensional vector space has a basis and hence is isomorphic to \(k^n\); its frame torsor is trivial. This proves (19). \(\square\)

This is **Hilbert 90 in torsor form**. It applies to all fields, without a perfectness assumption.

For \(n=1\), vector bundles are invertible sheaves. Theorem 7.2 now gives

\[
H^1_{\mathrm{Zar}}(S,\mathbf G_m)
=H^1_{\mathrm{\acute et}}(S,\mathbf G_m)
=H^1_{\mathrm{fppf}}(S,\mathbf G_m)
=H^1_{\mathrm{fpqc}}(S,\mathbf G_m)
=\operatorname{Pic}(S).
\tag{20}
\]

These are group identifications: the contracted product of frame torsors corresponds to tensor product of line bundles, since \([\varphi,\psi]\) gives the frame \(a\mapsto a\,\varphi(1)\otimes\psi(1)\). In particular \(H^1(k,\mathbf G_m)=0\). *Comparison locator:* [Stacks, Tag 03P8] for the Zariski, étale and fppf identifications.

**Lemma 8.2. Additive torsors over a field.** For every field \(k\), \(H^1_{\mathrm{fppf}}(k,\mathbf G_a)=0\), and the same holds in the étale and fpqc topologies.

**Proof.** Proposition 6.2 represents an additive torsor by an affine faithfully flat \(P=\operatorname{Spec}L\) over \(k\). Its own cover gives a section, and the two pullbacks of this section differ by an additive cocycle \(c\in L\otimes_kL\) satisfying

\[
c_{13}=c_{12}+c_{23}\quad\text{in }L\otimes_kL\otimes_kL.
\]

Because \(L\ne0\), choose a \(k\)-linear map \(\lambda:L\to k\) with \(\lambda(1)=1\), by extending \(1\) to a vector-space basis. Put \(b=(\lambda\otimes1)(c)\). Applying \(\lambda\) to the first factor of the cocycle identity gives

\[
1\otimes b=b\otimes1+c.
\]

Thus \(c=1\otimes b-b\otimes1\) is a coboundary. Subtract \(b\) from the chosen section; its two pullbacks now agree, so the sheaf condition descends it to a section over \(k\). Lemma 6.1 makes the torsor trivial. The same argument works for the other topologies. \(\square\)

## 9. Roots of units: the Kummer sequence

Fix an integer \(n\geq1\). For every scheme \(S\) the sequence of fppf sheaves

\[
0\longrightarrow\mu_{n,S}\longrightarrow\mathbf G_{m,S}
\xrightarrow{x\mapsto x^n}\mathbf G_{m,S}\longrightarrow0
\tag{21}
\]

is exact. If \(n\) is invertible on \(S\), it is also exact for the étale topology.

**Proof of exactness.** The kernel is \(\mu_n\) by its defining equation. For a unit \(a\) on a test scheme \(T\), form

\[
P_a=\operatorname{Spec}_T\bigl(\mathcal O_T[z]/(z^n-a)\bigr).
\tag{22}
\]

On an affine chart this algebra is free with basis \(1,z,\ldots,z^{n-1}\), so \(P_a\to T\) is a finite locally free surjection of rank \(n\). The element \(z\) is a unit, with inverse \(a^{-1}z^{n-1}\), and \(a=z^n\) after this fppf cover. If \(n\) is invertible, the derivative \(nz^{n-1}\) is a unit, making the cover étale. This proves local surjectivity in the stated topologies. \(\square\)

In fact \(P_a\) is a \(\mu_n\)-torsor: use the right action \(z\mapsto z\zeta\). Given two roots \(z,w\) over the same test scheme, their ratio \(w/z\) is the unique \(\zeta\) with \(\zeta^n=1\) relating them. This ratio and multiplication are inverse morphisms

\[
P_a\times_T\mu_n\simeq P_a\times_TP_a.
\]

All assertions are scheme-theoretic and remain valid when \(\mu_n\) is nonreduced.

**Theorem 9.1. Kummer classes over a field.** For every field \(k\) and every \(n\geq1\),

\[
H^1_{\mathrm{fppf}}(k,\mu_n)
\simeq k^\times/k^{\times n},
\tag{23}
\]

with the class of \(a\) represented by \(z^n=a\).

**Proof.** Apply abelian cohomology and Theorem 7.2 to (21). Its beginning is

\[
k^\times\xrightarrow{(\cdot)^n}k^\times
\xrightarrow{\delta}H^1_{\mathrm{fppf}}(k,\mu_n)
\longrightarrow H^1_{\mathrm{fppf}}(k,\mathbf G_m).
\]

The last group is zero by (20). Thus \(\delta\) identifies the quotient in (23) with \(H^1\). The boundary torsor is the sheaf of lifts of \(a\) through the \(n\)-th-power map, precisely (22). If \(b=a c^n\), scaling \(z\mapsto c z\) gives an isomorphism from the root torsor for \(a\) to that for \(b\); conversely exactness says all equivariant isomorphisms identify the same class modulo \(k^{\times n}\). \(\square\)

For a general scheme the same argument and (20) give an exact sequence

\[
0\longrightarrow
\Gamma(S,\mathcal O_S^\times)/\Gamma(S,\mathcal O_S^\times)^n
\longrightarrow H^1_{\mathrm{fppf}}(S,\mu_n)
\longrightarrow\operatorname{Pic}(S)[n]\longrightarrow0.
\tag{24}
\]

The last map forgets the \(n\)-th-power trivialization of the associated line bundle; the map on Picard groups induced by \((\cdot)^n\) is \(L\mapsto L^{\otimes n}\), as seen by raising its transition functions to the \(n\)-th power. Formula (23) is the field case, where Picard groups vanish.

**Example 9.2. The power map itself.** The morphism

\[
\mathbf G_{m,S}\longrightarrow\mathbf G_{m,S},\qquad x\longmapsto x^n
\tag{25}
\]

is a finite locally free \(\mu_n\)-torsor of rank \(n\). Its relative differentials on an affine chart are

\[
\Omega_{A[x,x^{-1}]/A[u,u^{-1}]}
\simeq \bigl(A[x,x^{-1}]/(n)\bigr)\,dx,
\qquad u=x^n.
\]

Consequently it is étale exactly when \(n\) is invertible on \(S\): sufficiency follows from the derivative criterion, and necessity follows from vanishing of this module, checked locally, and the faithful flatness of \(A\to A[x,x^{-1}]\).

In characteristic \(p\), the map \(x\mapsto x^p\) therefore remains an fppf \(\mu_p\)-torsor, although it is not étale. The étale Kummer sequence cannot replace (21) in this case. For example, over \(k=\mathbf F_p(t)\) the unit \(t\) has no \(p\)-th root in any separable algebraic extension: such a root would be purely inseparable and, if also separable, would already belong to \(k\); the \(t\)-adic valuation rules out a root in \(k\). Thus \(t\) does not acquire a root on an étale covering of \(\operatorname{Spec}k\).

When \(\operatorname{char}k\ne2\), the involution \(x\mapsto-x\) on \(\mathbf G_m\) is schematically free. Its invariant ring is \(k[x^2,x^{-2}]\), and the quotient is (25) with \(n=2\). Since \(\mu_2\simeq(\mathbf Z/2)_k\) in this case, this is also Corollary 4.4's finite étale torsor.

*Comparison locators:* [Stacks, Tags 040N and 03PL].

## 10. Artin–Schreier torsors

Let \(S\) have characteristic \(p>0\). The polynomial \(z^p-z\) is additive, so

\[
\wp:\mathbf G_a\longrightarrow\mathbf G_a,\qquad z\longmapsto z^p-z
\]

is a homomorphism. Its kernel is the constant group scheme \(\underline{\mathbf F_p}\). Indeed

\[
T^p-T=\prod_{c\in\mathbf F_p}(T-c),
\]

and the differences between distinct \(c\)'s are units, so the Chinese remainder theorem identifies the kernel algebra with the product of \(p\) copies of the ground algebra.

For any function \(a\) on \(T\), the scheme

\[
Q_a=\operatorname{Spec}_T\bigl(\mathcal O_T[z]/(z^p-z-a)\bigr)
\tag{26}
\]

is finite free of rank \(p\) and étale, because its derivative is \(-1\). It is surjective by faithful flatness. It supplies a local lift of \(a\), proving exactness of

\[
0\longrightarrow\underline{\mathbf F_p}
\longrightarrow\mathbf G_a\xrightarrow{\wp}\mathbf G_a
\longrightarrow0
\tag{27}
\]

both étale-locally and fppf-locally. Translation \(z\mapsto z+c\) makes (26) a torsor. Two roots differ by a unique section of the kernel, so the difference map is the inverse to

\[
Q_a\times_T\underline{\mathbf F_p}\longrightarrow Q_a\times_TQ_a.
\]

**Theorem 10.1. Artin–Schreier classes over a field.** For every field \(k\) of characteristic \(p\),

\[
H^1_{\mathrm{\acute et}}(k,\mathbf Z/p)
=H^1_{\mathrm{fppf}}(k,\mathbf Z/p)
\simeq k/\wp(k).
\tag{28}
\]

The class of \(a\) is the torsor \(z^p-z=a\).

**Proof.** The cohomology sequence of (27) and Lemma 8.2 identify \(H^1\) with the cokernel of \(\wp:k\to k\). Its boundary is the sheaf of lifts of \(a\), namely (26). If \(b=a+\wp(c)\), the translation \(z\mapsto z+c\) identifies its torsor with that for \(b\); exactness proves the converse and the completeness of the list. Every represented torsor under the constant smooth group is étale-locally trivial by Theorem 6.3, giving the agreement of the two topologies also directly. \(\square\)

**Example 10.2. A nontrivial class.** In \(k=\mathbf F_p(t)\), the torsor \(z^p-z=t\) is nontrivial. If a rational function \(b\) has a pole of order \(m>0\) at a place, then \(b^p-b\) has pole order \(pm\): the leading \(p\)-th-power term has strictly larger pole order and cannot cancel with \(b\). The function \(t\) has a pole of order one at infinity. It therefore cannot be \(b^p-b\). This proves nontriviality by (28), while (26) still provides a finite étale cover which trivializes the torsor.

*Comparison locator:* [Stacks, Section 0A3J].

## 11. Categorical and geometric quotients

For a groupoid \(R\rightrightarrows U\), an invariant morphism satisfies \(f\circ s=f\circ t\). A **categorical quotient in schemes over \(S\)** is an invariant \(q:U\to M\) such that every invariant \(f:U\to Y\) factors uniquely as

\[
f=\bar f\circ q.
\]

The category matters: a universal property for affine targets alone does not characterize a quotient in all schemes. A categorical quotient is **universal** if it remains categorical after every base change on \(M\), and **uniform** if this is required only for flat base changes. These definitions agree with [Stacks, Sections 048D and 048I].

For a groupoid, an **orbit space** is an invariant surjection \(q:U\to M\) for which \(R\to U\times_MU\) is surjective. Geometrically, two points with the same image become related after a common algebraically closed field extension. This formulation avoids imposing a bound on residue-field extensions in the definition of an orbit.

A **geometric quotient** is an orbit space which is universally submersive and whose functions are exactly the invariant functions. Here submersive means that a subset of \(M\) is open exactly when its inverse image in \(U\) is open. The assertion about functions means

\[
\mathcal O_M\simeq
\ker\bigl(q_*\mathcal O_U
\rightrightarrows(q\circ s)_*\mathcal O_R\bigr)
\tag{29}
\]

on the étale site of \(M\). This is the convention of [Stacks, Section 04AD]; see also Section 048M for geometric orbits.

**Proposition 11.1. The finite quotients already constructed.** The affine invariant quotient of a finite locally free groupoid is geometric and is a categorical quotient in all schemes. An effective quotient from Theorem 4.3 or 5.2 is universal categorical and geometric.

**Proof.** Theorem 3.2 gives the orbit-space assertion. An integral surjection is universally closed and surjective, so it is universally submersive: if an inverse image is closed, its image is the original subset and is closed; the converse follows by continuity. On any affine étale chart \(\operatorname{Spec}D\to\operatorname{Spec}C\), flat base change in Lemma 3.1 identifies the invariant ring with \(D\). These identifications give (29).

To prove the categorical property for the general affine groupoid, take an invariant \(f:U\to Y\). It is constant on every orbit, so the inverse image \(V\) of an affine open of \(Y\) is a saturated open of \(U\). Its complement is closed and saturated; since \(q\) is integral with orbit fibres, there is an open

\[
O=M\setminus q(U\setminus V),\qquad q^{-1}(O)=V.
\]

Cover \(O\) by principal opens \(D(c)\), \(c\in C\). On \(\operatorname{Spec}A_c=q^{-1}(D(c))\), the invariant morphism to the chosen affine target factors uniquely through \(\operatorname{Spec}C_c\), since localization is flat and invariants are \(C_c\). These local maps glue. Indeed, if two maps from an open of \(M\) agree after pullback to \(U\), surjectivity of \(q\) first makes their underlying point maps agree. Near any point choose a common affine target chart and an affine source chart. Injectivity of the corresponding invariant-ring inclusion then makes their ring maps agree. This also proves uniqueness of the glued factorization.

For an effective quotient, the sheaf property proved in Theorems 4.3 and 5.2 gives the categorical property after every base change. Finite locally free surjectivity remains integral and surjective, and the fibre-product relation remains effective. Faithfully flat descent of regular functions gives (29) after every base change as well. Thus these quotients are universal categorical and geometric. \(\square\)

### Algebraic groups: the general scheme quotient

The algebraic-space step has an exact internal provider: *Algebraic spaces and stacks*, *The bootstrap theorem*, Theorem 4.1 and Corollary 4.2. That theorem, with its geometric reductions and appendices, proves that a free action of a flat, locally finitely presented group on an algebraic space has an algebraic-space quotient, and that the original space is its torsor. The following argument supplies the additional scheme assertion needed here. It keeps all nilpotents and does not require either group to be affine or smooth.

**Lemma 11.1a. A dense affine part.** A separated algebraic space \(X\) of finite type over a field has a dense open affine subscheme containing every generic point of its irreducible components.

**Proof.** Choose a finite union of affine étale charts covering \(X\), and let their disjoint union be the affine scheme \(U=\operatorname{Spec}A\). Put \(R=U\times_XU\). Separatedness of \(X\) makes \(R\) a closed subscheme of \(U\times_kU\), hence affine. Its projections \(s,t\) are étale, quasi-compact and separated. In particular \(R\to U\) is of finite type and has finite fibres. Write its source algebra as \(A\to B\).

At a minimal prime \(\eta\) of the Noetherian ring \(A\), the local ring \(A_\eta\) is Artinian. The étale finite-type algebra \(B\otimes_AA_\eta\), modulo the nilpotent maximal ideal of \(A_\eta\), is a finite product of finite separable fields. It is therefore finite over \(A_\eta\). Explicitly, lift finitely many module generators from that quotient; their cokernel \(M\) satisfies \(M=\mathfrak m_\eta M\), and iteration of this equality gives \(M=0\) because \(\mathfrak m_\eta\) is nilpotent. Each algebra generator of \(B\) consequently satisfies a monic equation after localization at \(\eta\). Clearing the finitely many denominators and equations gives an element \(f\notin\eta\) for which \(B_f\) is finite over \(A_f\). Thus the open locus where \(s\) is finite contains all generic points of \(U\).

Let \(W\subset U\) be the largest such open. It is invariant under the relation. Indeed \(s\) is the base change of the chart map \(U\to X\) by that same chart. Its two further pullbacks to \(R\), along \(s\) and \(t\), are canonically identified by changing the chosen lift to \(U\); the cocycle is precisely relation composition. Finiteness is local under an étale cover, by the affine and module descent proved at the start of this lesson. Consequently the two inverse images of its maximal open locus coincide, giving \(s^{-1}(W)=t^{-1}(W)\). The restricted relation on \(W\) has finite étale projections.

All generic points of \(W\) can be put in one affine open. There are finitely many of them. Around each, remove the other irreducible components and choose an affine neighbourhood in the remaining open. These neighbourhoods are pairwise disjoint: an intersection would belong to two components, both of which have been removed there. Their finite disjoint union is affine and contains all the generic points. A finite étale relation carries generic points to generic points; hence each orbit of one of these points lies in this affine open. Lemma 5.1 gives invariant affine neighbourhoods of these finite orbits. Their affine quotients, supplied by Theorem 4.3, are open subschemes of \(X\) containing its generic points. If more than one is needed, first shrink them to pairwise disjoint affine neighbourhoods of the distinct generic points of \(X\), by the same removal-of-components argument. Their finite disjoint union is the required affine open. \(\square\)

The argument is the finite-type separated form of the schematic-locus proof in AI Integrated Stacks Project, Properties of Algebraic Spaces, Tag 06NH. Here the generic finiteness step was proved directly over the Artinian generic local rings; no scheme form of Zariski's Main Theorem is being substituted for that step.

**Theorem 11.1b. Quotients by arbitrary closed algebraic subgroups.** Let \(G/k\) be a group scheme of finite type, and let \(H\subset G\) be a closed subgroup scheme. The fppf quotient of right cosets is represented by a separated finite-type \(k\)-scheme \(X=G/H\). The quotient map is a faithfully flat morphism of finite presentation and an \(H\)-torsor. If \(H\) is normal, \(X\) is a group scheme and the quotient map is a homomorphism.

**Proof.** Right multiplication by \(H\) is schematically free: cancellation gives a unique transporter on every test scheme. Over a field \(H\) is flat, and finite type makes it finitely presented. The internal flat quotient theorem therefore gives an algebraic space \(X\), a flat surjection of finite presentation \(q:G\to X\), and

\[
G\times_kH\simeq G\times_XG,\qquad
(g,h)\longmapsto(g,gh).
\]

Finite type over \(k\) descends through this fppf cover, and quasi-compactness follows from the surjectivity of the quasi-compact source \(G\); hence \(X\) is of finite type. Its diagonal is closed. After the covering \(G\times G\to X\times X\), the diagonal is the relation just displayed, which is the inverse image of the closed subgroup \(H\) under \((g,g')\mapsto g^{-1}g'\). Closed immersions descend by the ideal and algebra descent at the start of the lesson. This proves separatedness, including the schematic assertion with nilpotents.

Left translation by \(G\) acts on the quotient sheaf and therefore on \(X\). Over an algebraic closure \(\overline k\), it is transitive on geometric points. Indeed any point of \(X(\overline k)\) lifts through \(q\): its nonempty finite-type fibre has a closed point, and that point is rational over the algebraically closed field.

By Lemma 11.1a choose an affine open \(V\subset X\) containing all generic points. Its base change \(V_{\overline k}\) is dense in every geometric component. To see this, the projection from a field base change is flat, and the generic point of each geometric component contracts to a generic point of \(X\); thus that point lies in the base-changed open.

We next show that any finite set \(E\subset X(\overline k)\) can be translated into \(V_{\overline k}\) by one element of \(G^0(\overline k)\). The finite-type identity component is open and geometrically irreducible, by *Group schemes over a field*, Theorem 2.3. The images under \(q_{\overline k}\) of the finitely many components of \(G_{\overline k}\) are irreducible opens. Any two of these images are either equal or disjoint. If they meet, choose lifts \(g_1,g_2\) of a common geometric point. Then \(g_2=g_1h\) for some \(h\in H(\overline k)\); right translation by \(h\) identifies the two source components and leaves \(q\) unchanged. Their images thus coincide. These images form a finite disjoint open cover, so are also closed and are precisely the irreducible components of \(X_{\overline k}\).

For each \(x\in E\), the orbit map \(G^0_{\overline k}\to X_{\overline k}\), \(g\mapsto gx\), is open and surjects onto the component containing \(x\). It is, after choosing a lift of \(x\), the restriction of the fppf open map \(q_{\overline k}\) to a translate of \(G^0\). Consequently

\[
T_x=\{g\in G^0_{\overline k}:gx\in V_{\overline k}\}
\]

is a nonempty open in the irreducible \(G^0_{\overline k}\). The intersection of these finitely many opens is nonempty, and has a rational point. Such a point gives the desired common translator. This is a topological argument on the schemes with their original structures; it does not replace \(X\) by its reduction.

It remains to construct affine neighbourhoods over \(k\) itself. Choose any point of \(X\) having a representative over a finite extension of \(k\), and let \(E\) be the finite set of conjugates of that representative in \(X(\overline k)\). Pick \(g\) as above. Both \(g\) and these representatives are defined over a finite extension. Enlarge it to a finite normal extension \(L/k\). Its maximal separable subextension \(L_s/k\) is Galois, and \(L/L_s\) is purely inseparable; every automorphism of \(L_s/k\) extends uniquely to \(L\). Form

\[
W_L=\bigcap_{\sigma\in\operatorname{Aut}(L/k)}
       (\sigma g)^{-1}V_L\quad\subset X_L.
\]

This is affine. Each translate is affine, and in a separated algebraic space the intersection of two affine open subschemes is closed in their product, by the closed diagonal, hence affine. Induction treats the finite intersection. It contains \(E\): applying \(\sigma^{-1}\) to a point of \(E\) gives another such point, whose image under \(g\) lies in \(V\).

The purely inseparable projection \(X_L\to X_{L_s}\) is a universal homeomorphism, so this open comes from a unique open \(W_s\subset X_{L_s}\). Its base change is exactly \(W_L\). Affine descent makes \(W_s\) an affine scheme: descend the coordinate algebra of \(W_L\), and identify its represented sheaf with the existing open subspace by uniqueness of faithfully flat descent. The open \(W_s\) is invariant under \(\operatorname{Gal}(L_s/k)\). Its two pullbacks to \(L_s\otimes_kL_s\), the product indexed by this Galois group, agree. Thus it descends to an open \(W\subset X\), and affine descent again shows that \(W\) is an affine scheme. It contains the point originally chosen.

These affine opens cover \(X\). In fact every nonempty closed subspace of a finite-type algebraic space over \(k\) has a point with a representative over a finite extension: pull it back to a finite-type affine étale chart, choose a closed point there, and apply the field-algebra form of Zariski's lemma. If the complement of the union of our affine opens were nonempty, it would supply just such a point, contrary to their construction. Hence \(X\) has an open cover by affine schemes and is itself a scheme.

The torsor and fppf assertions obtained from the algebraic-space theorem now hold as assertions about schemes. They are valid on all test schemes, including nonreduced ones. When \(H\) is normal, multiplication and inverse on local coset representatives are independent of their choices. They therefore define operations on the quotient sheaf; as it is represented, these are scheme morphisms. The group identities hold locally on the fppf covers of representatives and descend, proving the final assertion. \(\square\)

*Scholarly comparison:* Milne, *Algebraic Groups*, Chapter 5c, Theorem 5.28 and Corollary 5.27, and Appendix B, Theorem B.37. The scheme step above is written out, with the flat algebraic-space step supplied by the exact internal programme theorem.

**Lemma 11.1c. A reduced target detects the flat image.** Let \(f:G\to Q\) be a schematically dominant homomorphism of affine finite-type group schemes over an algebraically closed field. If \(Q\) is reduced, then \(f\) is faithfully flat and of finite presentation.

**Proof.** The components of the reduced \(Q\) are disjoint integral open-and-closed schemes, by *Group schemes over a field*, Theorems 1.3 and 2.3. We first obtain a nonempty faithfully flat open on every component by a direct generic-freeness argument. Write \(A\) for the coordinate domain of one component, \(K\) for its fraction field, and \(B=A[x_1,\ldots,x_n]/J\) for its inverse image algebra. The ideal \(J\) is finitely generated, since \(A\) is Noetherian. Order monomials by total degree and then lexicographically. This order is compatible with multiplication and has no infinite decreasing sequence. The ideal generated by the leading monomials of the nonzero elements of \(J_K\) has a finite set of these monomials as generators, because \(K[x_1,\ldots,x_n]\) is Noetherian. Choose a polynomial realizing each generator, and divide by its leading coefficient. This is a finite monic Gröbner basis: division successively decreases the leading monomial and terminates, and a nonzero remainder belonging to \(J_K\) would have a leading monomial divisible by one of those generators, contradicting the definition of a remainder.

Invert one nonzero element \(a\in A\) so that all coefficients of this basis lie in \(A_a\), each basis polynomial belongs to \(J_a\), and each original generator of \(J\) belongs to the ideal generated by that basis. Only finitely many coefficients and expressions occur, so one localization suffices. Monic division now shows that the standard monomials span \(B_a\) as an \(A_a\)-module. They are linearly independent: a relation among them would remain such a relation in \(B_K\), where the Gröbner basis makes them a basis, and \(A_a\) embeds in \(K\). Thus \(B_a\) is free, possibly with an infinite basis. It is nonzero because schematic dominance gives \(A\hookrightarrow B\). A nonzero free module is faithfully flat. This constructs a dense open \(V\subset Q\), meeting every component, over which \(f\) is faithfully flat.

For any \(q\in Q(k)\), the opens \(V\) and \(qV\) meet: both are dense in every component. Choose a rational point \(u\) in their intersection and write \(u=qv\) with \(v\in V(k)\). The fibres over \(u,v\) are nonempty finite-type schemes over the algebraically closed field, so have rational points in \(G\). Their quotient maps to \(uv^{-1}=q\). Hence every rational point of \(Q\) is in the image. Translation by its lift in \(G\) identifies the inverse image over \(V\) with the inverse image over \(qV\), so \(f\) is faithfully flat there too. These translates cover \(Q\), since they contain every closed point and a nonempty closed subset of a finite-type scheme has a closed point. This proves faithful flatness everywhere. Finite presentation follows from finite type between finite-type schemes over a field. \(\square\)

**Theorem 11.1d. Normal quotients of affine algebraic groups are affine.** If \(G\) in Theorem 11.1b is affine and \(H\) is normal, then \(G/H\) is affine.

**Proof.** Affineness descends through a faithfully flat field extension by the first section of the lesson, so work over an algebraically closed field. We first treat a reduced \(G\), which is smooth by *Group schemes over a field*, Proposition 4.1. The subgroup \(H\) need not be reduced.

Let \(A=k[G]\) and \(I\) be the ideal of \(H\). Choose finite generators of \(I\), and a finite-dimensional right regular subcomodule \(V\subset A\) containing these generators and \(1\), using *Group schemes, actions and Hopf algebras*, Lemma 5.1. Put \(W=I\cap V\). Its scheme stabilizer is precisely \(H\). Indeed, right translation by \(h\in H(T)\) preserves \(H_T\), its ideal, and \(V_T\), so preserves \(W_T\); intersections commute with scalar extension from the field. Conversely a translation preserving \(W_T\) preserves the ideal it generates, namely \(I_T\), and therefore preserves \(H_T\). Evaluating this translation on the identity puts its parameter in \(H(T)\). This holds for every test scheme.

The line \(D=\bigwedge^{\dim W}W\) in \(\bigwedge^{\dim W}V\) has the same stabilizer. One can check this over any test ring by choosing a basis starting with a basis of \(W\): preservation of the wedge line makes the corresponding square minor a unit; the minors replacing one row force the remaining block to be zero. Thus the first block maps \(W\) onto itself. The zero-dimensional case is the line \(\bigwedge^0V=k\), with stabilizer all of \(G\), as required when \(H=G\). The action of \(H\) on \(D\) is a character \(\chi\).

Consider the sum \(E\) of all \(H\)-stable lines in this wedge representation. Normality makes every translate of such a line by \(G(k)\) another \(H\)-stable line. Since the reduced finite-type \(G\) has schematically dense rational points, the equations saying that a subspace is stable show that \(E\) is stable under the group scheme \(G\). As an \(H\)-module, \(E\) is a sum of one-dimensional simple modules and is semisimple. Explicitly choose a maximal independent collection of stable lines spanning it. Distinct characters have independent group-like functions: a minimal relation \(\chi_m=\sum_{i<m}c_i\chi_i\), with the earlier functions independent and every \(c_i\ne0\), gives after applying comultiplication

\[
\sum_{i<m}c_i\chi_i\otimes(\chi_m-\chi_i)=0.
\]

Independence of the first tensor factors forces \(\chi_m=\chi_i\), contrary to distinctness. Applying this independence to the coaction of a relation among weight vectors shows that the weight spaces form a direct sum. Within the space of one character every subspace is stable. Consequently the chosen line \(D\) has an \(H\)-stable complement in \(E\). Its dual then supplies a line \(D'\subset E^*\) on which \(H\) acts through \(\chi^{-1}\).

In the tensor product of the wedge representation with \(E^*\), the line \(D\otimes D'\) is fixed pointwise by \(H\), and its stabilizer is still \(H\). Preservation of a pure tensor line implies preservation of both factor lines, on every test ring: the product of their first coordinates is a unit, hence both first coordinates are units; each other coordinate multiplied by the opposite first coordinate must vanish. The first factor therefore forces membership in \(H\), while \(H\) preserves both factors. Take the subspace \(F\) of \(H\)-fixed vectors in this tensor representation. It is \(G\)-stable by normality: for \(g\in G(T)\), \(h\in H(T')\),

\[
h(gv)=g(g^{-1}hg)v=gv
\]

for a fixed vector after the same extension. Fixed subspaces commute with scalar extension over the field, since they are kernels of the coaction minus the trivial coaction. Thus the representation on \(F\) has schematic kernel exactly \(H\): its kernel contains \(H\), and fixes the distinguished line, whose stabilizer is \(H\).

Let \(Q\subset\mathrm{GL}(F)\) be the schematic image. Its coordinate algebra is the image of the matrix-coordinate Hopf algebra in \(A\); the Hopf operations preserve the kernel, so \(Q\) is a closed affine group. It is reduced because this algebra is a subalgebra of the reduced \(A\). The homomorphism \(G\to Q\) is schematically dominant and has kernel \(H\). Lemma 11.1c makes it fppf. Its equality relation is \(G\times H\), by subtracting two points with the same image. Hence it represents the same quotient sheaf as Theorem 11.1b, proving \(G/H\simeq Q\), which is affine.

In characteristic zero every finite-type \(G\) is reduced by the finite-type Cartier theorem proved in *Lie algebras and smoothness of group schemes*, Theorem 4.3. This finishes that characteristic without using the arbitrary-group theorem to be proved later.

Now let the characteristic be \(p>0\) and allow nonreduced \(G\). Choose \(r\) large enough to kill the nilradicals of both \(G\) and \(H\) by \(p^r\)-th powers; their finite-type coordinate rings are Noetherian and their nilradicals are nilpotent. Relative Frobenius then factors through

\[
F:G\longrightarrow I=(G_{\mathrm{red}})^{(p^r)},
\qquad
F_H:H\longrightarrow J=(H_{\mathrm{red}})^{(p^r)}.
\]

These maps are finite: the monomials in finitely many algebra generators with exponents less than \(p^r\) span over the subalgebra of \(p^r\)-th powers. They are schematically dominant: a function on the reduced twist whose pullback is zero has \(p^r\)-th power zero, and was already zero in the reduced ring. The groups \(I,J\) are reduced and smooth, and Lemma 11.1c makes both maps faithfully flat. Normality of \(J\) in \(I\) follows on all test schemes by lifting both a conjugating element and an element of \(J\) along these faithfully flat maps, applying normality of \(H\), and descending the closed-subgroup condition. The reduced-source case just proved gives an affine group quotient \(Q=I/J\).

The morphism \(F\) induces a homomorphism \(\varphi:X=G/H\to Q\). Put \(K=\ker F\); it is a finite group scheme. The kernel of \(\varphi\), as a sheaf, is

\[
N=K/(K\cap H).
\]

For an element of \(G\) mapping into \(J\), lift its image locally to \(H\) through the faithfully flat \(F_H\); dividing by this lift puts it in \(K\). Two elements of \(K\) then give the same coset exactly when their ratio belongs to \(K\cap H\). This proves the displayed identification with its full scheme meaning. The finite-groupoid quotient theorem represents it by a finite scheme: the relation on the affine finite \(K\) has finite locally free projections, and its invariant algebra is a subspace of the finite-dimensional \(k[K]\). Thus \(N\) is finite locally free over the field.

The composite \(G\to I\to Q\) is an fppf cover and gives a local section of \(X\to Q\). The group identity identifies its pullback with \(G\times N\): two lifts differ uniquely by the kernel. This pullback is finite locally free over \(G\). Faithfully flat descent therefore makes \(X\to Q\) finite locally free. A finite morphism to an affine scheme is affine, so \(X\) is affine. Descent from the algebraic closure finishes the original field case. \(\square\)

*Scholarly comparison:* Milne, *Algebraic Groups*, Chapter 5c, Lemmas 5.15–5.17 and Proposition 5.29. The proof here gives the stabilizer and character arguments, the flat-image step, and the reduction by finite Frobenius internally. General subgroup quotients need not be affine, as the following calculation shows.

**Example 11.2. A projective quotient with constant affine invariants.** Let \(B\subset\mathrm{GL}_{2,k}\) be the upper triangular subgroup. Send a matrix to the line spanned by its first column. Over a test scheme this is a rank-one direct summand of \(\mathcal O^2\), giving a map

\[
\mathrm{GL}_2\longrightarrow\mathbf P^1.
\]

Every such line has, Zariski-locally, a generator and a complementary generator, so locally it is the first column line of an invertible matrix. Two matrices give the same line precisely when their ratio on the right is in \(B\): preserving the first coordinate line forces the lower-left entry to be zero, and invertibility forces the diagonal entries to be units. This works on all test schemes, not just over fields. Therefore the map is a Zariski \(B\)-torsor and represents \(\mathrm{GL}_2/B\).

An invariant regular function on \(\mathrm{GL}_2\) descends along its local sections to a regular function on \(\mathbf P^1\), and every such function pulls back to an invariant one. But

\[
\Gamma(\mathbf P^1,\mathcal O)
=k[t]\cap k[t^{-1}]=k
\]

inside \(k[t,t^{-1}]\). Thus the affine invariant ring is only \(k\), although the quotient is \(\mathbf P^1\). The source and target maps of this groupoid have positive-dimensional fibres; the finite locally free hypothesis of Theorem 4.3 does not apply. *Comparison locator:* [Stacks, Tag 03BG].

## 12. Exercises

**Exercise 1 (easy): the cone and its characteristic condition.** Over a field \(k\) of characteristic different from two, compute the invariant ring for \((x,y)\mapsto(-x,-y)\) on \(\mathbf A^2_k\), identify its defining equation, and prove that the quotient is singular at the image of the origin. What changes in characteristic two?

**Exercise 2 (medium): the power torsor over a general base.** For \(n\geq1\), prove over any scheme \(S\) that \(x\mapsto x^n\) on \(\mathbf G_m\) is a finite locally free \(\mu_n\)-torsor of rank \(n\). Give the inverse to its torsor isomorphism and prove that the map is étale exactly when \(n\) is invertible on \(S\).

**Exercise 3 (medium): frames and transition matrices.** Construct both directions of the correspondence between fppf \(\mathrm{GL}_n\)-torsors and rank-\(n\) vector bundles. With the right-action convention \(p_j=p_i g_{ij}\), determine the transition maps on vector coordinates and the effect of changing the frames. Deduce Zariski local triviality.

**Exercise 4 (medium): Kummer classes.** Compute \(H^1_{\mathrm{fppf}}(k,\mu_n)\) for any field, including when its characteristic divides \(n\). Describe representatives and equivalence. Specialize to \(k=\mathbf R\): how many classes are there for odd and even \(n\)?

**Exercise 5 (hard): a free finite-group quotient.** Let a finite constant group \(\Gamma\) act schematically freely on \(U=\operatorname{Spec}A\). Prove that \(U\to\operatorname{Spec}A^\Gamma\) is a finite étale \(\Gamma\)-torsor. Specify where schematic freeness enters and why no invertibility assumption on \(|\Gamma|\) is needed.

**Exercise 6 (medium): geometric points miss a stabilizer.** In characteristic \(p\), let \(\alpha_p\) act trivially on a nonempty affine scheme \(U\). Show that every geometric point has trivial stabilizer as an abstract group of geometric points, but that the action is not schematically free. Test the discrepancy over the dual numbers.

**Exercise 7 (hard): additive classes in characteristic \(p\).** Derive the Artin–Schreier classification over a field \(k\) of characteristic \(p\), including a proof that additive torsors over \(k\) are trivial. Show directly that \(z^p-z=t\) is a nontrivial torsor over \(\mathbf F_p(t)\).

**Exercise 8 (hard): recover a scheme after a radicial cover.** Let \(X\to Y\) be a surjective finite locally free radicial morphism, and let \(V\to X\) carry a descent datum. Construct its relation, explain why every orbit is a singleton, and prove that its quotient \(W\) satisfies \(V\simeq W\times_YX\).

## 13. Complete solutions

**Solution 1.** A monomial \(x^a y^b\) is fixed exactly when \(a+b\) is even. If both exponents are even it is a product of \(x^2,y^2\); if both are odd it is \(xy\) times such a product. Hence the invariants are generated by \(u=x^2,v=xy,w=y^2\). The relation \(uw=v^2\) holds. Reducing any proposed relation to \(F(u,w)+vH(u,w)\), its two images involve distinct even-even and odd-odd monomials, so both polynomials must vanish. This proves

\[
k[x,y]^\Gamma=k[u,v,w]/(uw-v^2).
\]

The ring has dimension two, while at the vertex its maximal ideal modulo its square has basis \(u,v,w\), since the equation has no linear part. The local ring is not regular, and the quotient is singular. In characteristic two the sign automorphism is the identity, every polynomial is invariant, and the quotient is \(\mathbf A^2\); the cone description no longer describes the invariant ring.

**Solution 2.** On an affine base the algebra of (25) is \(A[u,u^{-1}][x]/(x^n-u)\), with basis \(1,x,\ldots,x^{n-1}\); \(x\) is already invertible because \(u\) is. It is finite free of positive rank, hence faithfully flat. The right action multiplies \(x\) by \(\zeta\in\mu_n\). In a pair \((x,y)\) over the same \(u\), the inverse torsor map is

\[
(x,y)\longmapsto(x,y/x),
\]

because \((y/x)^n=1\). These expressions are regular and inverse on every algebra, proving the scheme isomorphism. The relative differential module is \(B/(n)\,dx\), since \(x\) is a unit. If the map is étale this module vanishes, forcing \(n\) to be a unit; faithful flatness detects that condition on the base. Conversely a unit \(n\) gives the unit derivative \(nx^{n-1}\), proving étaleness. The constructions glue over general \(S\).

**Solution 3.** For a vector bundle \(E\), its frames \(\operatorname{Isom}(\mathcal O^n,E)\) form a scheme locally isomorphic to \(\mathrm{GL}_n\), with right action by precomposition. Each local basis is a section, and any pair of frames differs by a unique matrix; this is its torsor identity.

For a torsor \(P\), choose local sections \(p_i\) and write \(p_j=p_i g_{ij}\). The cocycle relation is \(g_{ij}g_{jk}=g_{ik}\). The map from the \(j\)-coordinate vector to the \(i\)-coordinate vector is \(v_i=g_{ij}v_j\), so the free local modules descend to a bundle \(E\). If \(p'_i=p_i h_i\), then \(g'_{ij}=h_i^{-1}g_{ij}h_j\) and \(v'_i=h_i^{-1}v_i\); these changes give isomorphic descended bundles. The map \(p\mapsto(v\mapsto[p,v])\) identifies \(P\) with the frames of \(E\), and evaluation identifies the associated bundle of \(\operatorname{Fr}(E)\) with \(E\). Thus the operations are inverse. The bundle has bases on Zariski opens, so its frame torsor is Zariski-locally trivial.

**Solution 4.** For a unit \(a\), adjoining a root of \(z^n-a\) is a finite free fppf cover of rank \(n\), irrespective of the characteristic. This proves exactness of (21). The cohomology sequence ends, in degree one, with \(H^1(k,\mathbf G_m)=\operatorname{Pic}(k)=0\). Hence

\[
H^1_{\mathrm{fppf}}(k,\mu_n)=k^\times/k^{\times n}.
\]

The boundary of \(a\) is the root torsor \(z^n=a\); its class is trivial exactly when \(a\) has a root in \(k\). Two classes agree exactly when their representatives differ by an \(n\)-th power, with multiplication by that root giving an equivariant isomorphism of torsors. For \(\mathbf R\), the odd-power map is surjective, so there is one class. For even \(n\), its image is the positive real numbers, so there are two classes, represented by \(1\) and \(-1\).

**Solution 5.** The action groupoid \(R=\Gamma\times U\) has finite étale source projection and, by inversion, finite étale target. Schematic freeness says that \((t,s):R\to U\times U\) is a monomorphism. This is precisely the hypothesis used in Theorem 4.3 to make the tensor map \(A\otimes_{A^\Gamma}A\to\prod_\Gamma A\) surjective; the basis argument then proves it is an isomorphism and makes \(q\) finite locally free and surjective. Thus

\[
\Gamma\times U\simeq U\times_{\operatorname{Spec}A^\Gamma}U.
\]

Base change of \(q\) by this faithfully flat \(q\) is the finite étale source projection. Étaleness descends, proving \(q\) finite étale; the displayed isomorphism and the covering \(q\) give the torsor. No step averages functions or divides by the group order. Norms, finite-module descent and étale descent work in every characteristic.

**Solution 6.** Over any algebraically closed field \(K\) of characteristic \(p\), an element of \(\alpha_p(K)\) must satisfy \(a^p=0\), so \(a=0\). The stabilizer of every \(K\)-point therefore has just its identity as an abstract group of \(K\)-points. Scheme-theoretically the stabilizer is the whole group \(\alpha_p\), because the action is trivial.

Choose a geometric point \(u\) of \(U\), with field \(K\), and pull it back to \(T=\operatorname{Spec}K[\epsilon]/(\epsilon^2)\). There are two distinct arrows at this same \(T\)-point, given by \(0\) and \(\epsilon\in\alpha_p(T)\); indeed \(\epsilon^p=0\). Both map to the pair \((u_T,u_T)\) under \((t,s)\). This violates the test-scheme injectivity required for a monomorphism. Thus the action is not schematically free.

**Solution 7.** If an additive torsor is trivialized over a faithfully flat \(k\)-algebra \(L\), its cocycle \(c\in L\otimes_kL\) satisfies \(c_{13}=c_{12}+c_{23}\). Choose a \(k\)-linear \(\lambda:L\to k\) with \(\lambda(1)=1\). Applying it to the first factor gives \(c=1\otimes b-b\otimes1\), where \(b=(\lambda\otimes1)c\). Subtracting \(b\) from the local section kills the cocycle and descends a global section. This proves \(H^1(k,\mathbf G_a)=0\).

The map \(z\mapsto z^p-z\) has kernel the constant group \(\mathbf F_p\), and every equation \(z^p-z=a\) gives a rank-\(p\) finite étale cover, with derivative \(-1\). Its translation action has torsor inverse given by the difference of two roots. The cohomology sequence therefore yields \(H^1(k,\mathbf Z/p)=k/\wp(k)\), with \(a\) corresponding to this equation. If a rational function \(b\) has a pole of order \(m>0\), then \(b^p-b\) has pole order \(pm\). Since \(t\) has pole order one at infinity, it cannot lie in \(\wp(\mathbf F_p(t))\). The corresponding torsor is nontrivial.

**Solution 8.** Set \(R=V\times_YX\). Its source is the projection to \(V\), and its target is the transported point specified by the descent isomorphism on \(X\times_YX\). The cocycle and identity conditions give composition and identity; inversion is the reverse transport. Source and target determine the new \(X\)-coordinate and the point of \(V\), so \(R\to V\times_YV\) is a monomorphism.

The source is finite locally free and radicial, hence a universal homeomorphism. Since it has the identity section, its unique point above \(v\) is that identity point; target also sends it to \(v\). Every orbit is therefore a singleton and has an affine neighbourhood. Theorem 5.2 gives \(W=V/R\), with \(V\to W\) finite locally free and surjective. The invariant map to \(Y\) descends. The comparison \(V\to W\times_YX\), after the faithfully flat base change \(V\to W\), becomes \(V\times_WV\simeq R=V\times_YX\). It is therefore an isomorphism before base change as well, and recovers the given descent datum.

## Appendix. An affine quotient through a nilpotent thickening

The approximation argument for arbitrary group schemes needs a quotient result beyond the finite groupoids considered earlier. The arrows in this appendix need not be of finite type. A nilpotent ideal, rather than a bound on the fibres, makes the argument finite.

**Lemma A.1. A square-zero flatness criterion.** Let \(B\to A\) be a ring map and \(K\subset B\) an ideal with \(K^2=0\). Suppose \(A/KA\) is flat over \(B/K\), and multiplication gives an isomorphism

\[
K\otimes_{B/K}(A/KA)\longrightarrow KA.
\]

Then \(A\) is flat over \(B\).

**Proof.** Tensor \(0\to K\to B\to B/K\to0\) with \(A\). Since \(K\otimes_BA=K\otimes_{B/K}(A/KA)\), the assumed injectivity gives \(\operatorname{Tor}_1^B(B/K,A)=0\). For any \(B/K\)-module \(M\), choose a surjection \(F\to M\) with \(F\) free over \(B/K\), and kernel \(L\). The Tor exact sequence injects \(\operatorname{Tor}_1^B(M,A)\) into the kernel of \(L\otimes_BA\to F\otimes_BA\). The former Tor of \(F\) is zero by the calculation for \(B/K\). The latter kernel is zero by flatness of \(A/KA\), since these tensors are \(L\otimes_{B/K}(A/KA)\) and \(F\otimes_{B/K}(A/KA)\). Thus the Tor group vanishes for every \(B/K\)-module. For an arbitrary \(B\)-module \(M\), both \(KM\) and \(M/KM\) are \(B/K\)-modules. Apply the Tor exact sequence to \(0\to KM\to M\to M/KM\to0\); it gives \(\operatorname{Tor}_1^B(M,A)=0\). This is the flatness criterion. No module finiteness is used. \(\square\)

**Theorem A.2. Nilpotent affine quotients.** Let \(R\rightrightarrows U\) be an equivalence relation of affine schemes, with faithfully flat projections. Write \(U=\operatorname{Spec}A\), \(R=\operatorname{Spec}\Gamma\), and let \(I\subset A\) be an ideal with \(I^N=0\) and

\[
s(I)\Gamma=t(I)\Gamma.
\]

Put \(A_0=A/I\) and \(\Gamma_0=\Gamma/I\Gamma\). Suppose there is a faithfully flat map \(B_0\to A_0\) identifying the restricted relation with its fibre relation,

\[
\Gamma_0\simeq A_0\otimes_{B_0}A_0,
\]

compatibly with the projections and groupoid operations. Then

\[
B=\{a\in A:s(a)=t(a)\}
\]

maps surjectively to \(B_0\), the map \(B\to A\) is faithfully flat, and the endpoint map identifies

\[
\Gamma\simeq A\otimes_BA.
\]

Consequently \(\operatorname{Spec}B\) represents the fpqc quotient \(U/R\), with a nilpotent closed subscheme \(\operatorname{Spec}B_0\). If \(B_0\) is of finite type over a field and \(I\) is finitely generated, then \(B\) is of finite type over that field as well.

**Proof.** Filter \(A\) by \(I^n\), and every algebra of composable arrows by the ideal generated by \(I^n\) at any one endpoint. The endpoint choice does not matter, by the displayed equality of ideals and by composition. Flatness of the arrow projections gives

\[
I^n\Gamma/I^{n+1}\Gamma
\simeq\Gamma_0\otimes_{A_0}(I^n/I^{n+1}).
\]

The identifications at the two endpoints give a descent datum on the \(A_0\)-module \(I^n/I^{n+1}\). Its cocycle holds because the identifications are those of the same ideal on a triple of composable arrows. Module descent therefore supplies a \(B_0\)-module \(M_n\) with

\[
I^n/I^{n+1}\simeq A_0\otimes_{B_0}M_n.
\tag{A.1}
\]

For \(n=0\), this means \(M_0=B_0\). The associated graded additive cochain complex of the groupoid is exactly the Amitsur complex for \(B_0\to A_0\) with coefficients in \(M_n\). To check this identification, its degree \(p\) term is the algebra of \(p\) composable arrows modulo consecutive ideal powers, namely

\[
A_0^{\otimes_{B_0}(p+1)}\otimes_{B_0}M_n.
\]

The cofaces forget an endpoint or compose adjacent arrows, so on this fibre relation they insert \(1\) into the scalar factors. The alternating differential is thus the one whose exactness was proved at the start of the lesson. In particular its cohomology vanishes in positive degree and its degree-zero kernel is \(M_n\).

An invariant element modulo \(I\) lifts to an invariant element of \(A\). Indeed, lift it arbitrarily to \(a\in A\). Its difference \(d a=t(a)-s(a)\) lies in \(I\Gamma\). This difference is an additive 1-cocycle: the alternating sum of its two endpoint pullbacks and composition pullback is zero. Modulo \(I^2\Gamma\), exactness in degree one expresses it as the difference of some element of \(I/I^2\). Subtract a lift of that element from \(a\). The new difference lies in \(I^2\Gamma\). Repeat with the next graded module, and stop at \(I^N=0\). The corrected element lies in \(B\). As the invariants of \(A_0\) are \(B_0\), this proves surjectivity \(B\to B_0\).

The identical correction starting from a class in \(M_n\subset I^n/I^{n+1}\) produces an invariant lift in \(I^n\); its initial difference lies in \(I^{n+1}\Gamma\). Consequently, with \(J_n=B\cap I^n\),

\[
B/J_1=B_0,\qquad J_n/J_{n+1}\simeq M_n.
\tag{A.2}
\]

The multiplication maps on these modules are the descended multiplication on the associated graded algebra of \(A\). That algebra is generated in degree one over \(A_0\): a class in \(I^n/I^{n+1}\) is a sum of products of \(n\) classes in \(I/I^2\). After the faithful flat extension \(B_0\to A_0\), the maps \(\operatorname{Sym}^n_{B_0}M_1\to M_n\) are therefore surjective; faithful flatness proves their surjectivity before extension. Lift their factors to \(J_1\) using (A.2). This gives

\[
J_n=J_1^n+J_{n+1}.
\]

Starting at \(J_N=0\) and proceeding downwards gives \(J_n=J_1^n\) for all \(n\). Moreover (A.1) in degree one gives \(I=J_1A+I^2\). Modulo \(J_1A\), this says that the image ideal \(\bar I\) equals \(\bar I^2\); its nilpotence forces \(\bar I=0\). Hence

\[
I=J_1A,\qquad I^n=J_1^nA,
\qquad
J_1^n/J_1^{n+1}\otimes_{B_0}A_0
\simeq I^n/I^{n+1}.
\tag{A.3}
\]

We prove flatness of \(A/B\) by induction on the nilpotence bound. The case \(I=0\) is the assumed flatness over \(B_0\). For the induction step, remove the top power \(K=J_1^{N-1}\), whose corresponding power in \(A\) is \(KA=I^{N-1}\). The quotient rings have the same graded identifications (A.3) and a smaller nilpotence bound, so \(A/KA\) is flat over \(B/K\). Since \(J_1K=0\), (A.3) at the top power identifies

\[
K\otimes_{B/K}(A/KA)
=K\otimes_{B_0}A_0\simeq KA.
\]

Lemma A.1 applies and proves flatness. It is faithful: nilpotent ideals do not change prime spectra, and the induced map on the quotient spectra is that of the faithfully flat map \(B_0\to A_0\), hence is surjective.

There is a natural map \(A\otimes_BA\to\Gamma\), given by the two endpoints. Both its source and target are flat modules over \(A\) through the first endpoint. Modulo \(I\) it is the asserted isomorphism \(A_0\otimes_{B_0}A_0\to\Gamma_0\). For any flat \(A\)-module \(F\), tensoring the ideal-power exact sequences gives

\[
I^nF/I^{n+1}F
\simeq (I^n/I^{n+1})\otimes_{A_0}(F/IF).
\]

Thus our map is an isomorphism on every graded piece of this finite filtration. Induction through the filtration makes it an isomorphism. The fpqc map \(\operatorname{Spec}A\to\operatorname{Spec}B\) now has exactly the relation \(R\) as its fibre relation, proving quotient representability by the sheaf condition.

Finally suppose \(I\) is finitely generated and \(B_0\) is of finite type over the field. The module \(I/I^2\) is finite over \(A_0\). Finite generation descends faithfully flatly, so (A.1) makes \(M_1\) finite over \(B_0\). For completeness, choose finite generators after extension, express them using finitely many elements of \(M_1\), and tensor the cokernel of that finite span with \(A_0\); its vanishing and faithful flatness give the assertion. Every \(M_n\) is then finite because it is a quotient of \(\operatorname{Sym}^n M_1\). Lift finitely many algebra generators of \(B_0\) and finitely many generators of \(M_1\) to \(B\) and \(J_1\). The former generate modulo \(J_1\); products of the latter, with polynomial coefficients in the former, generate each \(J_1^n/J_1^{n+1}\). Successively subtracting these expressions and using \(J_1^N=0\) shows that this finite collection generates \(B\) as an algebra. \(\square\)

**Corollary A.3. The nilpotent step for group quotients.** Let \(H\subset L\subset G\) be closed subgroup schemes over a field, with \(H\) affine. Suppose \(L\subset G\) is defined by a finitely generated nilpotent ideal sheaf, and \(L/H\) is represented by a finite-type scheme, with \(L\to L/H\) an fpqc \(H\)-torsor. Then the fpqc quotient \(G/H\) is a finite-type scheme, with \(G\to G/H\) an fpqc \(H\)-torsor. No finite-type hypothesis on \(G\) or \(H\) is used.

**Proof.** A nilpotent closed immersion is a homeomorphism on underlying spaces. Thus every open of \(L\) has a unique corresponding open of \(G\). For an affine open \(V\subset L/H\), its preimage \(U_0\subset L\) is affine: it is a torsor under the affine group \(H\), and affine morphisms descend by the first section of the lesson. Let \(U\subset G\) be the corresponding open. It is affine as well, by the nilpotent thickening argument below.

The action preserves \(U\). On \(L\) this is the preimage of a quotient open, and the underlying spaces of \(G\), \(L\), and their field products with \(H\) coincide under the nilpotent immersion. Hence the open containment holds also for the action on \(G\); restriction to an open is then a schematic factorization. Its relation is the affine scheme \(U\times H\), with faithfully flat projections, and the ideal of \(U_0\) is invariant because \(L\) is stable under right multiplication by \(H\). Its quotient relation modulo that ideal is \(U_0\times_VU_0\). Theorem A.2 gives an affine finite-type quotient \(W\) of \(U\), with \(V\) as a nilpotent closed subscheme.

These quotients are open subfunctors of the quotient sheaf \(G/H\). Indeed their inverse images are the invariant opens \(U\), and membership can be tested after any fpqc lift to \(G\). On every test scheme it is an open condition, by descent of opens. They cover the quotient and agree on overlaps because they represent the same open subfunctors. Thus they glue to a scheme. A finite affine cover of the quasi-compact finite-type scheme \(L/H\) gives a finite cover by the finite-type schemes \(W\), so the glued scheme is of finite type. The relation and faithfully flat torsor maps are those proved on each open quotient, and glue too.

Here is the scheme fact used above, including its proof. If \(Y_0\subset Y\) is a nilpotent closed immersion and \(Y_0\) is affine, then \(Y\) is affine. Filter its ideal sheaf by powers. Each graded quotient is a quasi-coherent module on the affine \(Y_0\), whose positive cohomology vanishes. This affine module assertion follows directly from a finite basic-open cover: clear all denominators in a Čech cocycle, choose a partition \(1=\sum a_if_i^m\), and contraction by that partition gives a coboundary. The same contraction works in every positive degree. Induction through the finite ideal filtration gives \(H^1(Y,\mathcal I)=0\), so global functions surject onto \(\Gamma(Y_0,\mathcal O_{Y_0})\).

The space \(Y\) is quasi-compact and quasi-separated: it has the same underlying space as \(Y_0\), and intersections of affine opens are quasi-compact because their reductions are affine opens in the separated affine scheme \(Y_0\). Choose finitely many basic opens of \(Y_0\), each contained in the reduction of an affine open of \(Y\), and covering \(Y_0\). Lift their defining functions to global functions \(f_i\) on \(Y\). Their nonvanishing opens are principal opens in those affine opens of \(Y\), hence affine. Section localization on a quasi-compact quasi-separated scheme, proved by the denominator-clearing argument in Lemma 5.4, identifies their coordinate rings with \(\Gamma(Y,\mathcal O_Y)_{f_i}\). The \(f_i\) generate the unit ideal in the global ring: they do modulo its nilpotent kernel onto \(\Gamma(Y_0,\mathcal O_{Y_0})\), and an element congruent to \(1\) modulo a nilpotent ideal is a unit. These affine charts are therefore precisely the basic-open cover of the spectrum of the global ring. Their localization identifications glue to an isomorphism, proving affineness. \(\square\)

This is the affine-torsor form of the nilpotent quotient step used in Perrin's approximation proof ([thesis](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/99/55/99556864-9947-4630-8154-76b1bc0b3edc/p_perrin-109.pdf), Chapter IV, Lemma 3.1). The argument above proves the needed form by invariant lifting and flatness.

## What this lesson does not prove

The general existence theorem for \(G/H\), including nonaffine and nonreduced \(G,H\), is proved in Lemma 11.1a and Theorem 11.1b using the exact internal flat quotient provider. Lemma 11.1c and Theorem 11.1d prove the affineness assertion for a normal subgroup of an affine algebraic group. Effectivity of finite locally free descent under all five projectivity or ample-sheaf hypotheses is proved in Lemma 5.4 and Theorem 5.5. The appendix proves the affine nilpotent quotient step needed in arbitrary-group approximation. Section 6 records the possible failure of scheme representability for general torsors, with its locator in Examples of Stacks, Section 036Z; no nonrepresentable example is constructed here.

Faithfully flat descent for affine schemes and quasi-coherent modules is proved at the start of this lesson. Descent of flatness, smoothness and étaleness, and the étale-local-section theorem for smooth morphisms are prerequisites. The proof of Theorem 4.3 uses the general facts that a finite monomorphism is a closed immersion [Stacks, Tag 03BB] and that finite module presentation descends faithfully flatly [Stacks, Tag 03C4]. Lemma 5.1 uses finite prime avoidance [Stacks, Tag 00DS]; Lemma 5.4 includes its required homogeneous version. Basic sheaf theory supplies descent for sheaves, enough injectives and connecting homomorphisms; Theorem 7.2 proves their application to torsors, including the inverse constructions.

## References

The Stacks Project, in **AI Integrated Stacks Project**, Groupoid Schemes, Sections 03BE, 03JD, 0497 and 0CCH; Cohomology on Sites, Tags 03AH–03AJ; Étale Cohomology, Tags 03P8, 03PL, 040N and Section 0A3J; More on Morphisms, Tag 055U; Quotients of Groupoids, Sections 048D, 048I, 048M and 04AD; Examples of Stacks, Section 036Z. AI Integrated Stacks Project is an unofficial edition with AI additions. Prerequisite algebra locators are given above.

J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition dated 5 October 2021, Cambridge University Press, 2022: Chapter 2j for torsors; Chapter 5b–c for quotient maps and existence; Chapter 7e for quotients of affine algebraic groups. [Author's edition](https://www.jmilne.org/math/Books/iAG2022.pdf).

## Sources and licence

Lemma 5.4 and Theorem 5.5 are proved in the Stacks Project, *Properties*, Tags 01PW, 01Q1 and 01ZY, *Algebra*, Tag 00JS, and *Groupoid Schemes*, Tag 0CCJ. The other sections name the Stacks tags and the other sources with which their arguments are compared. The AI Integrated Stacks Project edition used for these locators is pinned at [revision 565b10e9](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790); the Stacks Project itself is at [stacks.math.columbia.edu](https://stacks.math.columbia.edu).

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the subsection *Ample neighbourhoods and finite descent* by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. The lesson text is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

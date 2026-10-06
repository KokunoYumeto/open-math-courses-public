# The Grothendieck group and \(K_0\) of a unital algebra

*Public domain (CC0).*
A projection records a subspace; an idempotent over an algebra records a finitely generated projective module. Direct sum adds these objects, but subtraction has no meaning among actual modules. The Grothendieck group supplies formal differences and tells us exactly when two such differences agree. Applied to matrix idempotents, it produces \(K_0\).

This lesson develops that construction, its behavior under homomorphisms, and its first calculations. It assumes [Idempotents, projections and their equivalences](#what-this-lesson-does-not-prove) and [Vector bundles and finitely generated projective modules](#what-this-lesson-does-not-prove). The precise facts needed from those lessons are recalled at the end, with references that also establish them directly. Freely accessible comparisons are [Blackadar 1998] and [Weibel, group completion], together with the exact [AF] and [Traces] results recalled below.

Throughout, algebras are complex and unital. Homomorphisms between Banach algebras are bounded algebra homomorphisms; between C*-algebras we use *-homomorphisms. A homomorphism need not preserve the identity. Allowing such maps is essential for corner embeddings. Spaces called compact are compact Hausdorff, and vector bundles are complex, locally trivial and of finite rank. The nonunital definition belongs to *Nonunital algebras: unitization, relative classes and half-exactness*.

## 1. Additive measurements and formal subtraction

An **abelian monoid** \(M\) is a set with an associative, commutative addition and a zero. Examples are \(\mathbb N_0\), dimensions of vector spaces, and isomorphism classes of projective modules under direct sum. An additive measurement with values in an abelian group should send a formal difference \(a-b\) to the difference of the measurements of \(a\) and \(b\).

The subtlety is cancellation. If \(a+c=b+c\), any group-valued additive measurement gives the same value to \(a\) and \(b\), even when they are distinct in \(M\). Thus group completion must identify them.

**Theorem 1.1 (Group completion).** On \(M\times M\), define
\[
(a,b)\equiv(a',b')
\quad\Longleftrightarrow\quad
a+b'+c=a'+b+c\text{ for some }c\in M.
\]
This is an equivalence relation. Its quotient \(G(M)\) is an abelian group under
\[
\langle a,b\rangle+\langle a',b'\rangle
=\langle a+a',b+b'\rangle,
\qquad
-\langle a,b\rangle=\langle b,a\rangle.
\]
The map \(j_M(a)=\langle a,0\rangle\) is a monoid homomorphism, and every monoid homomorphism \(h:M\to H\) into an abelian group has a unique extension \(\bar h:G(M)\to H\) satisfying \(\bar h j_M=h\).

*Proof.* Reflexivity uses \(c=0\), and symmetry uses the same witness. For transitivity, suppose
\[
a+b'+c=a'+b+c,
\qquad a'+b''+d=a''+b'+d.
\]
Adding \(b''+d\) to the first equation and substituting the second gives
\[
a+b''+(b'+c+d)=a''+b+(b'+c+d).
\]
This is the required witness.

If two pairs are replaced by equivalent pairs with witnesses \(c,d\), adding their defining equations shows that their sums are equivalent with witness \(c+d\). Thus addition is well defined. Associativity and commutativity descend from \(M\). The zero is \(\langle0,0\rangle\), and
\(\langle a,b\rangle+\langle b,a\rangle=\langle a+b,a+b\rangle=0\).
The formula for \(j_M\) respects addition and zero.

Set
\[
\bar h(\langle a,b\rangle)=h(a)-h(b).
\]
Applying \(h\) to a witnessing equality and cancelling in \(H\) proves independence of the representative. The formula is additive and extends \(h\). Since every element is \(j_M(a)-j_M(b)\), any extension must have this formula. \(\square\)

We write \([a]-[b]\) for \(\langle a,b\rangle\). In particular,
\[
j_M(a)=j_M(b)
\quad\Longleftrightarrow\quad
a+c=b+c\text{ for some }c\in M.
\]
The extra summand is part of the equality criterion; it cannot be omitted without a cancellation hypothesis.

**Example 1.2.** For \(M=\mathbb N_0\), the map \(\langle a,b\rangle\mapsto a-b\) identifies \(G(M)\) with \(\mathbb Z\). Every integer is a difference of nonnegative integers, and two pairs give the same integer exactly when their cross sums agree.

For a contrasting example, let \(M=\{0,s\}\), with \(s+s=s\). In \(G(M)\), the equation \([s]+[s]=[s]\) forces \([s]=0\). Hence \(G(M)=0\), although \(M\) has two elements. Completion can lose information.

The construction is functorial: a monoid map \(f:M\to N\) induces
\(G(f)(\langle a,b\rangle)=\langle f(a),f(b)\rangle\).
Witnesses map to witnesses, and the formulas give the identity and composition laws.

## 2. The objects measured by \(K_0\)

Write \(M_n(A)\) for the \(n\)-by-\(n\) matrices over \(A\), and include it in \(M_{n+1}(A)\) by \(a\mapsto\operatorname{diag}(a,0)\). The union is
\[
M_\infty(A)=\bigcup_{n\geq1}M_n(A).
\]
Every element belongs to a finite matrix algebra. Even though \(A\) is unital, this union has no identity. Symbols such as \(1_n\) always refer to a specified finite matrix algebra.

For idempotents \(e\in M_r(A)\), \(f\in M_s(A)\), write \(e\sim_a f\) when there are rectangular matrices
\[
x\in M_{r,s}(A),\quad y\in M_{s,r}(A),
\qquad xy=e,\quad yx=f,
\]
with \(x=exf\), \(y=fye\). This is the algebraic equivalence of the prerequisites, expressed without unnecessary zero rows. It agrees with algebraic equivalence after padding into a common square matrix algebra.

**Definition 2.1.** Let \(V_{\mathrm{id}}(A)\) be the algebraic equivalence classes of matrix idempotents. Denote the class of \(e\) by \(v(e)\), and put
\[
v(e)+v(f)=v(e\oplus f),\qquad
e\oplus f=\begin{pmatrix}e&0\\0&f\end{pmatrix}.
\]

**Proposition 2.2.** This addition makes \(V_{\mathrm{id}}(A)\) an abelian monoid. For orthogonal idempotents \(e,f\in M_n(A)\), meaning \(ef=fe=0\), one has \(v(e+f)=v(e)+v(f)\).

*Proof.* Block sums of equivalence witnesses show that addition respects classes. Adding zero leaves the same class after padding, and iterated block sums give associativity. To see commutativity, first pad \(e,f\) to the same size \(N\). The scalar rotation
\[
R_t=\begin{pmatrix}
\cos t\,1_N&-\sin t\,1_N\\
\sin t\,1_N&\cos t\,1_N
\end{pmatrix}
\]
conjugates \(e\oplus f\), at \(t=\pi/2\), to \(f\oplus e\). Similar idempotents are algebraically equivalent, so the sums agree. Padding and changing the positions of zero blocks only introduce permutation similarities.

For the last assertion take \(x=\begin{pmatrix}e&f\end{pmatrix}\) and \(y=\begin{pmatrix}e\\f\end{pmatrix}\). Then \(xy=e+f\), while \(yx=\operatorname{diag}(e,f)\). The witnesses have the required supports. \(\square\)

By the projective-module correspondence from the prerequisites,
\[
V_{\mathrm{id}}(A)\cong
\{\text{isomorphism classes of finitely generated projective right }A\text{-modules}\},
\qquad v(e)\longmapsto[eA^r].
\]
It respects addition because the range of a block sum is the direct sum of the ranges. Thus including all matrix sizes includes all finitely generated projective modules, rather than only those represented by an idempotent in \(A\) itself.

For a C*-algebra define \(V_{\mathrm{pr}}(A)\) using projections \(p=p^*=p^2\) and Murray–von Neumann equivalence. For different sizes this means that a rectangular \(w\) satisfies \(w^*w=p\), \(ww^*=q\). Addition is again block sum. This is exactly the monoid \(V(A)\) of [AF, Definition 7.4].

**Theorem 2.3 (Projection and idempotent descriptions).** If \(A\) is a unital C*-algebra, inclusion of projections among idempotents induces a monoid isomorphism
\[
V_{\mathrm{pr}}(A)\longrightarrow V_{\mathrm{id}}(A).
\]
Consequently it induces an isomorphism of their Grothendieck groups.

*Proof.* A partial isometry gives algebraic witnesses \(w^*,w\), so the map is well defined, and it preserves block sums. Every matrix idempotent is similar to a projection by the prerequisite result [Blackadar 1998, Proposition 4.6.2], giving surjectivity. If two projections have the same idempotent class, pad them into one finite matrix algebra. Algebraic equivalence of projections is Murray–von Neumann equivalence by [Blackadar 1998, Proposition 4.6.4], giving injectivity. Apply \(G\) to this monoid isomorphism and its inverse. \(\square\)

We henceforth write \(V(A)\) for the idempotent monoid of a Banach algebra, using the projection description when \(A\) is a C*-algebra.

## 3. Differences, complements and equality

**Definition 3.1.** For a unital Banach algebra,
\[
K_0(A)=G(V(A)).
\]
Write \([e]\) for the image of \(v(e)\) in this group. Every element is \([e]-[f]\), and \([e\oplus f]=[e]+[f]\). For a unital C*-algebra, Theorem 2.3 shows that this definition agrees with completion of the projection monoid. No choice of an orthogonal representative changes the resulting group.

This unital definition agrees with [Blackadar 1998, Proposition 5.5.5] and [Blackadar 2006, Definition V.1.1.15]. Agreement here does not assert that completion of \(V(A)\) is the general nonunital definition.

An idempotent \(f\in M_m(A)\) has a complement \(1_m-f\). Proposition 2.2 gives
\[
v(f)+v(1_m-f)=v(1_m).
\]
For a projection the complement is also a projection. This simple identity explains why free modules suffice to test equality after group completion.

**Theorem 3.2 (Representatives and equality).** Every element of \(K_0(A)\) has a representative \([e]-[1_m]\). Moreover,
\[
[e]=[f]\text{ in }K_0(A)
\quad\Longleftrightarrow\quad
e\oplus1_k\sim_a f\oplus1_k\text{ in }M_\infty(A)
\text{ for some }k\geq0.
\]
In a C*-algebra one may take projections throughout and use Murray–von Neumann equivalence. Matrices of different sizes are padded with zeros before comparison; \(1_0\) means no added block.

*Proof.* If \(f\in M_m(A)\), then
\[
[e]-[f]=[e\oplus(1_m-f)]-[1_m].
\]
This proves the representative assertion.

If \([e]=[f]\), Theorem 1.1 supplies a matrix idempotent \(g\in M_k(A)\) with
\(v(e)+v(g)=v(f)+v(g)\).
Add \(v(1_k-g)\) to both sides. The complement identity yields
\(v(e)+v(1_k)=v(f)+v(1_k)\), which is exactly the asserted equivalence. Conversely, that equivalence gives \([e]+[1_k]=[f]+[1_k]\); cancelling in the group gives \([e]=[f]\). For C*-algebras use the projection monoid and its projection complements. \(\square\)

More generally, the same argument gives
\[
[e]-[f]=[e']-[f']
\quad\Longleftrightarrow\quad
e\oplus f'\oplus1_k\sim_a e'\oplus f\oplus1_k
\text{ for some }k.
\]
Notice that equality in \(V(A)\) and equality in \(K_0(A)\) are different questions. The latter permits an extra common summand. Neither criterion permits cancellation inside \(V(A)\) without further hypotheses.

The distinguished class \([1_A]\) need not generate \(K_0(A)\). It records the free module of rank one, and \([1_m]=m[1_A]\). For matrix algebras, this class can be a nonprimitive multiple of a generator.

## 4. Changing the algebra

**Proposition 4.1 (Functoriality).** A homomorphism \(\phi:A\to B\) induces
\[
\phi_*:K_0(A)\longrightarrow K_0(B),
\qquad
\phi_*([e]-[f])=[\phi^{(r)}(e)]-[\phi^{(s)}(f)],
\]
where \(\phi^{(n)}\) acts on matrix entries. Identity maps induce identity maps and \((\psi\circ\phi)_*=\psi_*\circ\phi_*\). If \(\phi\) is unital, \(\phi_*[1_A]=[1_B]\).

*Proof.* Multiplicativity preserves idempotents and the equations for algebraic equivalence. Entrywise application also preserves block sums and zero. Thus \(\phi\) induces a monoid map on \(V\), and Theorem 1.1 extends it uniquely to the stated group map. Entrywise identities and composition prove the functor laws. A *-homomorphism preserves projections and partial isometries, so the projection description gives the same map. The last assertion follows by applying \(\phi\) to the identity. \(\square\)

For a nonunital homomorphism between unital algebras, \(\phi(1_A)\) is an idempotent, and the correct formula is \(\phi_*[1_A]=[\phi(1_A)]\). This distinction will matter below.

**Theorem 4.2 (Homotopy invariance).** Suppose \((\phi_t)_{0\leq t\leq1}\) is a family of bounded homomorphisms \(A\to B\), continuous in the **point-norm topology**: for each \(a\in A\), the map \(t\mapsto\phi_t(a)\) is norm continuous. Then \((\phi_0)_*=(\phi_1)_*\). The same holds for a point-norm continuous family of *-homomorphisms.

*Proof.* Fix \(e=(e_{ij})\in M_r(A)\). Each of the finitely many entries \(\phi_t(e_{ij})\) varies continuously, so \(t\mapsto\phi_t^{(r)}(e)\) is a norm-continuous path in \(M_r(B)\). Multiplicativity makes every point of this path an idempotent. The endpoint equivalence theorem from the prerequisites [Blackadar 1998, Proposition 4.3.3] makes its endpoints similar, hence algebraically equivalent. Therefore
\([\phi_0^{(r)}(e)]=[\phi_1^{(r)}(e)]\).
Applying this to both terms of every difference \([e]-[f]\) proves equality of the group maps. For *-homomorphisms the same path consists of projections; Theorem 2.3 identifies the two descriptions. \(\square\)

Only point-norm continuity was used. Continuity in a weaker operator topology does not provide the norm-continuous idempotent path required by the theorem.

**Proposition 4.3 (Inner invariance).** If \(u\in A\) is invertible, \(\operatorname{Ad}u:a\mapsto uau^{-1}\) induces the identity on \(K_0(A)\). In the C*-category take \(u\) unitary.

*Proof.* For \(e\in M_r(A)\) set \(U=\operatorname{diag}(u,\ldots,u)\) and \(f=UeU^{-1}\). The rectangular witnesses, here square, are
\[
x=eU^{-1},\qquad y=Ue,
\qquad xy=e,\quad yx=f.
\]
They show \([f]=[e]\). If \(e=p\) is a projection and \(u\) is unitary, \(Up\) has initial projection \(p\) and final projection \(UpU^*\). Every difference is therefore fixed. No path from \(u\) to the identity is needed. \(\square\)

**Theorem 4.4 (Matrix corners).** For \(n\geq1\), the corner homomorphism
\[
\iota:A\longrightarrow M_n(A),\qquad
a\longmapsto\operatorname{diag}(a,0,\ldots,0)
\]
induces an isomorphism \(\iota_*:K_0(A)\to K_0(M_n(A))\). Its inverse flattens matrices of blocks:
\[
F_n([P]-[Q])=[\operatorname{flat}(P)]-[\operatorname{flat}(Q)],
\quad M_r(M_n(A))\cong M_{rn}(A).
\]

*Proof.* Flattening preserves products, block sums, adjoints and equivalence witnesses. It therefore induces a monoid map \(\lambda:V(M_n(A))\to V(A)\). This map is onto: pad any \(k\)-by-\(k\) idempotent with zeros to a size divisible by \(n\), and group its entries into \(n\)-by-\(n\) blocks. It is one-to-one: if two flattened matrices are equivalent, pad them and their witnesses to a common size divisible by \(n\), then group the witnesses into blocks. This gives equivalence over \(M_n(A)\).

For \(e\in M_r(A)\), applying \(\iota\) to its entries and flattening places its nonzero entries at coordinate positions
\(1,n+1,\ldots,(r-1)n+1\).
A permutation of coordinates moves these positions to \(1,\ldots,r\), giving \(e\) padded with zero. Hence \(\lambda\circ V(\iota)\) is the identity. Since \(\lambda\) is bijective, \(V(\iota)\) is its inverse. Group completion proves the assertion and the formula. \(\square\)

Under \(F_n\), the class of \(1_{M_n(A)}\) is \(n[1_A]\). The corner sends \([1_A]\) to \([E_{11}\otimes1_A]\). Also, the unital map \(a\mapsto\operatorname{diag}(a,\ldots,a)\), followed by \(F_n\), induces multiplication by \(n\). These observations separate matrix invariance from the behavior of a particular unital embedding.

## 5. Calculations: dimensions, absorption and bundles

**Example 5.1 (Matrices).** A projection in \(M_k(\mathbb C)\) is determined up to Murray–von Neumann equivalence by its rank. An implementing partial isometry restricts to a unitary between the ranges, so equivalent projections have equal rank. Conversely, any unitary between equal-dimensional ranges, extended by zero on the orthogonal complement, is such a partial isometry.

All nonnegative ranks occur in sufficiently large matrices. Block sum adds ranks. Consequently
\[
V(\mathbb C)\cong\mathbb N_0,
\qquad K_0(\mathbb C)\cong\mathbb Z,
\qquad [p]-[q]\longmapsto\operatorname{rank}p-\operatorname{rank}q.
\]
Flattening gives the same calculation for \(M_d(\mathbb C)\). Its group generator is the class of a rank-one projection, while its identity has class \(d\).

**Example 5.2 (Finite direct sums).** For unital algebras \(A_1,\ldots,A_r\), idempotents and equivalence witnesses in a matrix algebra over \(\bigoplus_i A_i\) are coordinatewise. Given finitely many representatives or witnesses, pad them to a common size. Thus
\[
V\left(\bigoplus_{i=1}^rA_i\right)\cong\prod_{i=1}^rV(A_i).
\]
Taking a difference in each coordinate gives
\(G(\prod_iV(A_i))\cong\bigoplus_iG(V(A_i))\): the equality witnesses can also be chosen coordinatewise. Hence
\[
K_0\left(\bigoplus_{i=1}^rM_{d_i}(\mathbb C)\right)\cong\mathbb Z^r.
\]
The coordinates are ordinary ranks, and the identity has vector \((d_1,\ldots,d_r)\). By the finite-dimensional structure theorem [AF, Theorem 2.4], this computes every finite-dimensional C*-algebra with \(r\) simple summands.

In particular \(K_0(\mathbb C\oplus\mathbb C)=\mathbb Z^2\). The diagonal homomorphism \(z\mapsto(z,z)\) sends a rank-one projection to rank vector \((1,1)\), so its induced map is \(k\mapsto(k,k)\).

**Theorem 5.3 (All bounded operators).** For every infinite-dimensional complex Hilbert space \(H\),
\[
K_0(B(H))=0.
\]

*Proof.* Write \(\kappa=\dim H\), an infinite cardinal. The identification \(M_m(B(H))=B(H^{\oplus m})\) follows by writing operators as finite blocks. Projections in this algebra are equivalent exactly when their ranges have equal Hilbert dimension: a partial isometry restricts to a unitary of the ranges, and a unitary of ranges extended by zero gives the converse.

Let \(p\in M_m(B(H))\). Its range has dimension \(\lambda\leq m\kappa=\kappa\), so
\(\dim(pH^{\oplus m}\oplus H)=\lambda+\kappa=\kappa\).
Thus, after padding into \(M_{m+1}(B(H))\), the projections \(p\oplus1_H\) and \(1_H\) are equivalent. Therefore
\[
v(p)+v(1_H)=v(1_H),
\qquad [p]+[1_H]=[1_H].
\]
Cancellation in the group gives \([p]=0\), and all its generators vanish. This works for finite-rank and infinite-rank \(p\), and requires no separability of \(H\). \(\square\)

One can already see \([1_H]=0\) from \(H\oplus H\cong H\). However, the vanishing of this one class alone is not the reason all of \(K_0\) vanishes; the absorption argument applies to every matrix projection.

**Theorem 5.4 (Bundles).** For compact Hausdorff \(X\), let \(\operatorname{Vect}(X)\) be the monoid of isomorphism classes of finite-rank complex vector bundles under direct sum. There is a canonical isomorphism
\[
K_0(C(X))\cong G(\operatorname{Vect}(X)),
\qquad [p]-[q]\longmapsto[E_p]-[E_q],
\]
where \((E_p)_x=p(x)\mathbb C^n\) for \(p\in M_n(C(X))\).

*Proof.* Serre–Swan identifies \(\operatorname{Vect}(X)\) with the monoid of finitely generated projective \(C(X)\)-modules through continuous sections. The idempotent-module correspondence identifies the latter with \(V(C(X))\). These are the precise prerequisite statements recalled below. Both respect direct sum, and the section module of \(E_p\) is \(pC(X)^n\). Their composite is a monoid isomorphism, so completion gives the asserted group isomorphism and formula. \(\square\)

Thus \(K_0\) generalizes virtual vector bundles. Point evaluation at \(x\) induces the homomorphism \([E]-[F]\mapsto\operatorname{rank}E_x-\operatorname{rank}F_x\): evaluating a representing projection computes that rank. If \(X\) is connected, each rank is constant because it is locally constant. The bundle need not be trivial merely because its rank is constant.

**Example 5.5 (The circle).** Every finite-rank complex vector bundle on \(S^1\) is trivial by [Lesson 2, Proposition 5.1](KT-OPK-02.md#5-gluing-around-a-circle-and-across-a-sphere). We use that exact result to compute the rank monoid and its group completion.

Since \(S^1\) is connected, rank classifies its bundles and identifies their direct-sum monoid with \(\mathbb N_0\). Theorem 5.4 now gives
\[
K_0(C(S^1))\cong\mathbb Z,
\]
generated by the trivial line bundle, or equivalently by \([1]\).

## 6. Traces as additive measurements

A **tracial linear functional** is a complex-linear map \(\tau:A\to\mathbb C\) with \(\tau(ab)=\tau(ba)\). Its matrix extension is the unnormalized sum
\[
\tau_n(a)=\sum_{i=1}^n\tau(a_{ii}).
\]
Using an average would change the value when a matrix is padded by zero.

**Proposition 6.1 (Trace pairing).** A tracial linear functional induces a homomorphism
\[
\tau_*:K_0(A)\longrightarrow\mathbb C,
\qquad \tau_*([e]-[f])=\tau_r(e)-\tau_s(f).
\]
No continuity assumption on \(\tau\) is needed for this algebraic statement. If \(A\) is a C*-algebra and \(\tau\) is positive, the values are real and the values on projection classes are nonnegative.

*Proof.* For rectangular \(x\in M_{r,s}(A)\) and \(y\in M_{s,r}(A)\),
\[
\tau_r(xy)=\sum_{i,j}\tau(x_{ij}y_{ji})
=\sum_{j,i}\tau(y_{ji}x_{ij})=\tau_s(yx).
\]
Thus algebraically equivalent idempotents have the same value. Zero padding does not change the sum, and a block sum adds the values. The resulting monoid map \(V(A)\to\mathbb C\) therefore extends uniquely by Theorem 1.1. Positivity makes projection values nonnegative real numbers, so their differences are real. \(\square\)

In particular \(\tau_*[1_n]=n\tau(1_A)\). The ordinary trace on \(M_d(\mathbb C)\) gives the rank coordinate of Example 5.1; the normalized trace gives \(1/d\) on its generator. For a type II\(_1\) factor, the normalized trace instead measures all real dimensions. The advanced exercise proves this precisely. Further questions about positive pairings and states belong to *Traces, states and the pairing with \(K_0\)*.

## 7. Exercises

**Exercise 7.1 (Basic: multiplicities).** Use rank-one generators to compute \(K_0(M_2(\mathbb C)\oplus M_3(\mathbb C))\). For the unital embedding
\[
\phi(a,b)=\operatorname{diag}(a,a,a,b,b)\in M_{12}(\mathbb C),
\]
compute \(\phi_*\), its kernel and its image, and check its action on the identity.

**Exercise 7.2 (Basic: absorption).** For infinite-dimensional \(H\), prove \([1_H]=0\) in \(K_0(B(H))\), and then justify why every matrix projection has zero class. Explain the extra argument needed for the second assertion.

**Exercise 7.3 (Intermediate: cancellation).** Prove that \(j_M:M\to G(M)\) is injective if and only if \(M\) has cancellation. Apply this to \(V(A)\), and exhibit a unital C*-algebra for which the map to \(K_0\) is not injective.

**Exercise 7.4 (Intermediate: a corner and its inverse).** Describe explicitly the inverse of \(\iota_*:K_0(A)\to K_0(M_n(A))\), and verify the two compositions. For \(n=2\), track the coordinate positions of an idempotent \(e\in M_2(A)\). Compute the image, under the inverse, of \([1_{M_n(A)}]\).

**Exercise 7.5 (Advanced: real dimensions).** Let \(M\) be a type II\(_1\) factor with its faithful normal tracial state \(\tau\), normalized by \(\tau(1)=1\). Using comparison of projections, prove that
\[
\tau_*:K_0(M)\longrightarrow(\mathbb R,+)
\]
is an isomorphism. Prove, rather than assume, that every number in \([0,1]\) is the trace of a projection in \(M\).

## 8. Solutions

**Solution 7.1.** Example 5.2 gives \(\mathbb Z^2\), with generators represented by a rank-one projection in each summand. Their images have ranks \(3\) and \(2\), respectively. Thus
\[
\phi_*(x,y)=3x+2y.
\]
Its kernel is \(\mathbb Z(2,-3)\): \(3x=-2y\) forces \(x=2k\), \(y=-3k\). Its image is all of \(\mathbb Z\), since \(3-2=1\). The identity has vector \((2,3)\), whose image is \(6+6=12\), the class of \(1_{12}\). Using the identity classes as if they were rank-one generators would give the wrong coordinates.

**Solution 7.2.** Choose a unitary \(W:H\oplus H\to H\), possible because twice an infinite Hilbert dimension is the same dimension. The rectangular partial isometry \(W\) witnesses equivalence of \(1_H\oplus1_H\) and \(1_H\). Hence \(2[1_H]=[1_H]\), so \([1_H]=0\).

For \(p\in M_m(B(H))\), its range has dimension at most \(\dim H\). Adding a copy of \(H\) gives a space of dimension exactly \(\dim H\). The corresponding unitary of ranges witnesses \(p\oplus1_H\sim1_H\), so \([p]+[1_H]=[1_H]\) and \([p]=0\). The group is generated by these classes. Vanishing of the identity alone would not establish this without the equivalence for each \(p\).

**Solution 7.3.** If \(M\) has cancellation and \(j_M(a)=j_M(b)\), Theorem 1.1 gives \(a+c=b+c\), hence \(a=b\). Conversely, if \(a+c=b+c\), applying \(j_M\) and cancelling in the group gives \(j_M(a)=j_M(b)\); injectivity gives \(a=b\).

For \(A=B(\ell^2(\mathbb N))\), the projections \(0\) and \(1_A\) have different classes in \(V(A)\), since their ranges cannot be unitarily isomorphic. Both map to zero in \(K_0(A)\). More explicitly, a rank-one projection \(r\) satisfies \(v(r)+v(1_A)=v(1_A)\), while \(v(r)\neq0\). Thus this monoid fails cancellation.

**Solution 7.4.** The inverse is \(F_n\) from Theorem 4.4: view every matrix of \(n\)-by-\(n\) blocks as an ordinary matrix over \(A\), then take the same formal difference. Changing representatives is harmless because flattening sends each equivalence witness to an equivalence witness.

For \(e=(e_{ij})\in M_2(A)\), entrywise application of the corner with \(n=2\), followed by flattening, gives
\[
\begin{pmatrix}
e_{11}&0&e_{12}&0\\
0&0&0&0\\
e_{21}&0&e_{22}&0\\
0&0&0&0
\end{pmatrix}.
\]
Ordering the coordinates as \(1,3,2,4\) gives \(e\oplus0_2\), proving \(F_2\iota_*([e])=[e]\). For general \(n\), use the positions \(1,n+1,\ldots\) and the same permutation argument.

In the other direction, if \(P\in M_r(M_n(A))\), flattening gives a matrix of size \(rn\). Applying the corner to its entries and flattening again produces the flattened \(P\) with zero coordinates inserted. A permutation removes these inserted coordinates up to zero padding. Because flattening on \(V\) is injective, as proved in Theorem 4.4 by grouping witnesses into blocks, this gives \(\iota_*F_n([P])=[P]\). Both statements extend to differences. Finally, \(F_n[1_{M_n(A)}]=[1_n]=n[1_A]\).

**Solution 7.5.** We use two established projection facts: projections in a von Neumann algebra have suprema, and projections in a finite factor with a faithful normal trace are equivalent exactly when their traces agree. The exact references and trace amplification statement are given below. Type II means that \(M\) has no nonzero minimal projections.

First, every nonzero projection \(r\) contains projections of arbitrarily small positive trace. Choose a proper nonzero subprojection \(s<r\). Both \(s\) and \(r-s\) have positive trace by faithfulness; choose the one whose trace is at most \(\tau(r)/2\). Repeat inside that nonzero projection. The resulting traces are positive and at most \(2^{-k}\tau(r)\).

Fix \(t\in[0,1]\), and partially order
\[
\mathcal P_t=\{p\in M:p=p^*=p^2,\ \tau(p)\leq t\}
\]
by inclusion. A nonempty chain has a supremum \(p\), and normality gives \(\tau(p)=\sup\tau(p_i)\leq t\). The empty chain has upper bound zero. Zorn's lemma gives a maximal \(p\in\mathcal P_t\). If \(\tau(p)<t\), then \(1-p\neq0\), and the preceding splitting argument gives a nonzero \(s\leq1-p\) with \(\tau(s)<t-\tau(p)\). The projection \(p+s\) is strictly larger and still belongs to \(\mathcal P_t\), a contradiction. Hence \(\tau(p)=t\).

Extend \(\tau\) to matrices by \(\tau_n=\operatorname{Tr}_n\otimes\tau\), with no division by \(n\). For every \(x\geq0\), write \(x=k+t\) with \(k\in\mathbb N_0\), \(0\leq t<1\). If \(p_t\in M\) has trace \(t\), then \(1_k\oplus p_t\) has matrix trace \(x\). For \(k=0\) take \(p_t\) alone. All nonnegative real numbers therefore occur in the image of projection classes; taking differences proves surjectivity onto \(\mathbb R\).

For injectivity suppose \(\tau_*([p]-[q])=0\). Pad both projections into \(M_N(M)\). This is a factor: a central matrix must commute with the scalar matrix units, hence is \(a1_N\), and commuting with diagonal elements from \(M\) forces \(a\in\mathbb C1_M\). The trace \(\tau_N\) is faithful and normal by [Traces, Proposition 6.5]. It is finite, with value \(N\) on the identity; consequently this factor is finite. Indeed, an isometry has final projection of trace \(N\), so faithfulness makes that final projection the identity.

Now \(\tau_N(p)=\tau_N(q)\), and the finite-factor trace comparison result [Traces, Corollary 5.4] gives \(p\sim q\). Thus \([p]-[q]=0\). Proposition 6.1 gives the homomorphism property, so \(\tau_*\) is an isomorphism, with \([1_M]\) corresponding to \(1\). The splitting argument also shows why this calculation is specific to diffuse finite factors rather than finite-dimensional matrix algebras.

## What this lesson does not prove

The following prerequisite results are used with their stated hypotheses. The constructions and calculations of \(K_0\) above are proved from these results.

- **Equivalence of idempotents.** Algebraic equivalence is an equivalence relation; its witnesses can be supported on the idempotents. Similarity implies algebraic equivalence. A norm-continuous idempotent path in a unital Banach algebra has similar endpoints. After finite zero stabilization, algebraic equivalence, similarity and norm homotopy give the same classes. These are the results of *Idempotents, projections and their equivalences* used here; direct references are [Blackadar 1998, Propositions 4.2.2–4.2.3, 4.3.1, 4.3.3 and 4.4.1].
- **Projection reduction.** In a unital C*-algebra, every idempotent is similar to a projection, and two projections are algebraically equivalent exactly when they are Murray–von Neumann equivalent [Blackadar 1998, Propositions 4.6.2 and 4.6.4]. These statements apply to every finite matrix algebra. Theorem 2.3 proves the consequent equality of the two \(K_0\) definitions.
- **Projective modules and Serre–Swan.** Over a unital algebra, \(e\mapsto eA^n\) identifies algebraic equivalence classes of matrix idempotents with isomorphism classes of finitely generated projective right modules. For compact Hausdorff \(X\), continuous sections identify finite-rank complex vector bundles with finitely generated projective \(C(X)\)-modules, preserving direct sums. These are the results of *Vector bundles and finitely generated projective modules* used here [Blackadar 1998, §1.7.1; Blackadar 2006, V.1.1.5]. Theorem 5.4 proves their group-completion consequence. No second-countability hypothesis is needed.
- **Finite-dimensional structure.** Every finite-dimensional C*-algebra is a finite direct sum of full complex matrix algebras [AF, Theorem 2.4]. We prove its \(K_0\) calculation, without repeating the structure theorem or AF classification.
- **Von Neumann projection and trace theory.** Projections have suprema, increasing projection nets converge strongly to their supremum, and a normal positive functional preserves their suprema [Types, Proposition 3.1; Traces, Conventions]. Every finite factor has a faithful normal tracial state normalized at the identity [Traces, Theorem 5.2]. In such a factor, projections are equivalent exactly when their traces agree [Traces, Corollary 5.4], using the comparison theorem [Types, Theorem 5.5]. Finite matrix amplification extends a faithful normal trace to the faithful normal trace \(\tau_n(a)=\sum_i\tau(a_{ii})\) [Traces, Proposition 6.5]. These results are used only in Exercise 7.5; the real trace range and the resulting \(K_0\) isomorphism are proved in its solution.

## References

- **[AF]** *AF-algebras*, in *Foundations of von Neumann algebras*, §§2 and 7, [Open Mathematics Courses](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html).
- **[Types]** *Projections and types of von Neumann algebras*, §§3 and 5, [Open Mathematics Courses](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html).
- **[Traces]** *Traces on von Neumann algebras*, §§5 and 6, [Open Mathematics Courses](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/preparation.html#dependency-a598030ddbea).
- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Sections 5.1–5.3 and Proposition 5.5.5, printed pp. 27–31 (PDF pp. 41–45), compare the matrix monoid and unital definition. Propositions 4.3.3, 4.6.2 and 4.6.4 are the exact projection and homotopy prerequisites.
- **[Blackadar 2006]** B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006. [Author's revised edition](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024.
- **[Weibel, group completion]** Charles A. Weibel, *The K-book: An Introduction to Algebraic K-theory*, author-hosted Chapter II, §1, Proposition 1.1 and Corollaries 1.2–1.3, chapter pp. 1–2; §2, chapter p. 5. [Freely readable Chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf#page=1). The free-abelian-group presentation supplies a second construction of group completion and the same extra-summand equality criterion. Theorem 1.1 and Theorem 3.2 here retain their complete pair-quotient and complement proofs. Chapter pagination differs from the AMS printed book.

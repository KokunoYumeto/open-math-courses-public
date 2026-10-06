# Abelian varieties

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A proper group scheme has no room for a function to escape to infinity. That simple observation becomes rigidity: a family of maps cannot start by collapsing a whole proper fibre and then vary freely. For abelian varieties it forces commutativity and controls line bundles under addition. The theorem of the cube turns that control into a quadratic formula for multiplication, from which the degree of the torsion schemes follows.

We work over an arbitrary field, including imperfect fields and positive characteristic. We prove a relative theorem of the cube on a connected parameter scheme, so its proof retains nilpotent parameters. Dual abelian varieties, Picard schemes and polarizations are outside this lesson. Cohomology and base change, elementary properties of ample line bundles and faithfully flat descent are prerequisites.

## 1. Proper groups that remain integral

An **abelian variety** over \(k\) is a group scheme \(A/k\) whose underlying scheme is proper and geometrically integral. In particular it is of finite type and separated. Write \(0\) for its identity and \(g=\dim A\). Commutativity and projectivity will be consequences of this definition.

**Lemma 1.1. Constants and field extension.** An abelian variety remains an abelian variety after every field extension. If \(X/k\) is a proper geometrically integral scheme, then

\[
\Gamma(X,\mathcal O_X)=k,\qquad
\Gamma(X\times_k\operatorname{Spec}R,\mathcal O)=R
\tag{1}
\]

for every \(k\)-algebra \(R\).

**Proof.** Group operations and their identities base change. Properness and geometric integrality are preserved by field extension, proving the first assertion.

Proper coherent cohomology makes \(\Gamma(X,\mathcal O_X)\) finite-dimensional over \(k\). Over an algebraic closure, this algebra is a domain because the scheme is integral; a finite-dimensional domain over an algebraically closed field is that field. Flat base change for \(H^0\) therefore gives

\[
\Gamma(X,\mathcal O_X)\otimes_k\overline k
=\Gamma(X_{\overline k},\mathcal O)=\overline k.
\]

The left side has dimension \(\dim_k\Gamma(X,\mathcal O_X)\) over \(\overline k\), so that dimension is one and the unit map from \(k\) is an isomorphism. Every \(k\)-algebra is flat as a \(k\)-module. Applying the same flat base-change statement to \(R\) proves the second formula. The formulas also give \(p_*\mathcal O_{X\times Y}=\mathcal O_Y\) for any \(k\)-scheme \(Y\), by checking on its affine opens. \(\square\)

The last base-change calculation only requires \(X\) proper and \(H^0(X,\mathcal O_X)=k\); geometric integrality supplied that condition here.

**Proposition 1.2. Smoothness and projectivity.** Every abelian variety is smooth and projective over its field.

**Proof.** Over an algebraic closure, \(A\) is reduced and of finite type. The reduced-group smoothness theorem over a perfect field, proved in *Lie algebras and smoothness of group schemes*, makes it smooth there. Smoothness descends through the faithfully flat field extension, so \(A/k\) is smooth. This argument uses geometric reducedness and therefore applies equally to imperfect \(k\).

The quasi-projectivity theorem proved in *Group schemes over a field* supplies a locally closed immersion \(A\hookrightarrow\mathbf P^N_k\). Since \(A\) is proper and the target is separated, this morphism is proper: its graph is closed, and projection from \(A\times\mathbf P^N\) to \(\mathbf P^N\) is proper. A proper locally closed immersion is a closed immersion. Thus \(A\) is projective. \(\square\)

If \(g=0\), geometric integrality makes \(A\) a single geometrically reduced point; its \(k\)-rational identity then identifies it with \(\operatorname{Spec}k\). We will keep this case explicit when discussing multiplication. *Comparison locators:* [Stacks, Tags 03RO, 0BFA–0BFC].

## 2. Rigidity of maps

The local assertion below needs no connectedness assumption on the parameter scheme. Connectedness and a separated target supply its global form.

**Theorem 2.1. Rigidity.** Let \(X/k\) be a nonempty proper scheme with \(H^0(X,\mathcal O_X)=k\), let \(Y/k\) be a scheme, and let \(f:X\times_kY\to Z\) be a morphism.

If the fibre over a point \(y_0\in Y\) maps to a single point of \(Z\), there is an open neighbourhood \(U\) of \(y_0\) and a morphism \(h:U\to Z\) with

\[
f|_{X\times U}=h\circ\operatorname{pr}_U.
\tag{2}
\]

If in addition \(Y\) is connected and \(Z\) is separated over \(k\), this factorization holds over all of \(Y\), and \(h\) is unique.

**Proof.** Choose an affine open \(V\subset Z\) containing the fibre's image. The closed subset \((X\times Y)\setminus f^{-1}(V)\) has closed image under the proper projection to \(Y\). Its image misses \(y_0\). Remove that image to obtain \(U\), so that \(f(X\times U)\subset V\).

For an affine open \(U'=\operatorname{Spec}R\subset U\), formula (1), in its \(H^0(X)=k\) form, identifies the ring map defining \(f:X\times U'\to V\) with a ring map \(\Gamma(V,\mathcal O_V)\to R\). This gives the required \(h\) on \(U'\). These maps agree on overlaps: their pullbacks agree, and the projection \(X\times U'\to U'\) is faithfully flat. They glue, proving the local assertion. In particular the factorization is an equality of morphisms even for a nonreduced \(U\).

For the global assertion, on \(X\times X\times Y\) consider the two maps

\[
(x,x',y)\longmapsto f(x,y),\quad f(x',y).
\]

Their equalizer \(E\) is closed because \(Z\) is separated. Projection \(q:X\times X\times Y\to Y\) is flat, of finite presentation and surjective, hence open. Consequently

\[
C=Y\setminus q\bigl((X\times X\times Y)\setminus E\bigr)
\tag{3}
\]

is closed. Its points are exactly the points whose fibre is contracted. To check this set-theoretic description, extend the residue field to an algebraic closure and compare any two geometric points of \(X\). If every pair has equal image, the image is a single point. The affine-open argument just given then makes the contraction a scheme-theoretic factorization through the residue-field point.

At every point of \(C\), the local assertion supplies a neighbourhood on which all fibres are contracted. Thus \(C\) is also open. It contains \(y_0\), and connectedness gives \(C=Y\). The local factorizations now cover \(Y\) and glue uniquely by faithful flatness of \(X\times Y\to Y\). This proves both existence and uniqueness. \(\square\)

The connectedness condition cannot be omitted from the global assertion. Take \(X=\mathbf P^1\), let \(Y\) be two disjoint points, and use the constant map to \(\mathbf P^1\) on the first component of \(X\times Y\) and the identity on the second. One fibre is contracted but no global factorization exists. The separatedness condition was used to close the equalizer in (3).

**Corollary 2.2. Commutativity.** The group law of an abelian variety is commutative.

**Proof.** Initially write the group law multiplicatively. Its commutator morphism is

\[
c:A\times A\longrightarrow A,\qquad
c(x,y)=xyx^{-1}y^{-1}.
\]

Use the second copy of \(A\) as \(X\) and the first as the connected parameter \(Y\). For \(x=0\), this map is constant at \(0\). Theorem 2.1 makes \(c\) independent of \(y\). Evaluating at \(y=0\) shows that the remaining map is also constantly \(0\). The equality of morphisms \(c=0\) proves commutativity on every test scheme. \(\square\)

We henceforth write addition. For every integer \(n\), multiplication is the homomorphism \([n]:A\to A\).

**Corollary 2.3. Morphisms are translations of homomorphisms.** For abelian varieties \(A,B/k\), every morphism \(f:A\to B\) has the unique form

\[
f=t_b\circ u,\qquad b=f(0)\in B(k),
\tag{4}
\]

where \(u:A\to B\) is a group homomorphism and \(t_b\) is translation by \(b\).

**Proof.** Replace \(f\) by \(u=t_{-f(0)}\circ f\), so \(u(0)=0\). Consider

\[
v(x,y)=u(x+y)-u(x)-u(y).
\]

It is zero for \(y=0\). Rigidity makes it independent of \(x\); its value at \(x=0\) is zero as well. Hence \(v=0\), exactly the homomorphism identity. The condition at \(0\) determines \(b\), then \(u\), proving uniqueness. \(\square\)

*Comparison locators:* [Stacks, Tag 0BFD] for commutativity and [Stacks, Tag 0AH8] for the local proper-fibre argument. The proof above supplies the explicit global rigidity statement.

## 3. Cohomology detects trivial line bundles

We next isolate the technical steps for the cube. They are useful because fibrewise triviality alone can miss a deformation over a base with nilpotents.

We use the following cohomology-and-base-change prerequisite [Stacks, Tag 0B91]: if \(p:W\to B\) is proper, flat and of finite presentation and \(\mathcal L\) is a line bundle, then \(Rp_*\mathcal L\) is perfect, and its derived pullback to any \(T\to B\) computes \(R(p_T)_*\mathcal L_T\). Locally on an affine base a perfect object is represented by a bounded complex of finite free modules.

**Lemma 3.1. A complex adapted to one fibre.** Near any point \(b\) one can choose that free complex \(P^\bullet\) so that its differentials vanish after tensoring with \(\kappa(b)\), and

\[
\operatorname{rank}P^i
=\dim_{\kappa(b)}H^i(W_b,\mathcal L_b).
\tag{5}
\]

In particular it has no terms in negative degrees.

**Proof.** Start with a bounded free representative near \(b\). If a differential has a nonzero matrix entry modulo the prime of \(b\), invert that entry on a smaller neighbourhood. Row and column operations then put a unit in a separate \(1\times1\) block. The relation \(d^2=0\) lets one clear the preceding and following maps in that block. It splits off the contractible complex \(R\xrightarrow{1}R\), which can be deleted without changing the represented object.

Repeat. Each deletion lowers the sum of the finite ranks, so the procedure stops after finitely many steps. All remaining differential entries vanish at \(b\). The residue-field complex now has zero differentials, so its terms are its cohomology groups; base change gives (5). Negative fibre cohomology is zero, hence the corresponding free terms have rank zero. All the inversions and basis changes used only finitely many entries and take place on one neighbourhood. \(\square\)

This is the elementary cancellation underlying [Stacks, Tag 0BCD].

**Lemma 3.2. Universal constants in an integral proper family.** If \(p:W\to B\) is proper, flat and of finite presentation with geometrically integral fibres, then

\[
\mathcal O_T\xrightarrow{\sim}
(p_T)_*\mathcal O_{W_T}
\tag{6}
\]

for every \(T\to B\).

**Proof.** Lemma 1.1 gives \(H^0(W_b,\mathcal O)=\kappa(b)\). Apply Lemma 3.1 to \(\mathcal O_W\). On a neighbourhood of \(b\), its complex starts

\[
R\xrightarrow{d^0}P^1\longrightarrow\cdots .
\]

The unit morphism \(\mathcal O_B\to Rp_*\mathcal O_W\) is represented by a map of complexes from \(R\) in degree zero. Its degree-zero coefficient is nonzero at \(b\), since the unit spans \(H^0(W_b,\mathcal O)\). Shrink so that this coefficient is a unit. The chain-map identity \(d^0a=0\) then forces \(d^0=0\). It follows after every scalar extension that degree-zero cohomology is the base ring, with its given unit map. Arbitrary derived base change gives (6), locally and hence globally. \(\square\)

*Comparison locator:* [Stacks, Tag 0E0L].

**Lemma 3.3. The local product assertion.** Let \(X,Y\to B\) be proper, flat morphisms of finite presentation with geometrically integral fibres, and let \(x:B\to X\), \(y:B\to Y\) be sections. Suppose a line bundle \(\mathcal L\) on \(W=X\times_BY\) is trivial on \(X\times y(B)\) and \(x(B)\times Y\). If \(\mathcal L_b\) is trivial for one \(b\in B\), then \(\mathcal L\) is trivial over \(W_U\) for some open neighbourhood \(U\) of \(b\).

**Proof.** Work on an affine neighbourhood \(\operatorname{Spec}R\). Apply Lemma 3.1 simultaneously to

\[
C=R(p_W)_*\mathcal L,\qquad
D=R(p_X)_*\mathcal O_X,\qquad
F=R(p_Y)_*\mathcal O_Y.
\]

The degree-zero terms are \(R,R,R\). The first differentials of \(D,F\) are zero, by the unit argument in Lemma 3.2. Trivialize the two restrictions of \(\mathcal L\). Pullback of sections then gives derived morphisms \(C\to D\) and \(C\to F\). Since the source complex is bounded and free, these morphisms are represented by actual maps of complexes on the affine base.

After passing to \(\kappa(b)\), choose a trivialization of \(\mathcal L_b\). The two degree-one maps become the restrictions

\[
H^1(X_b\times Y_b,\mathcal O)
\longrightarrow
H^1(X_b,\mathcal O)\oplus H^1(Y_b,\mathcal O),
\tag{7}
\]

possibly multiplied on each summand by a nonzero scalar from the chosen trivializations. Map (7) is an isomorphism. Indeed the field Künneth formula [Stacks, Tag 0BED] decomposes its source as

\[
\bigl(H^1(X_b,\mathcal O)\otimes H^0(Y_b,\mathcal O)\bigr)
\oplus
\bigl(H^0(X_b,\mathcal O)\otimes H^1(Y_b,\mathcal O)\bigr).
\]

The two \(H^0\)'s are \(\kappa(b)\). Restriction by the sections is the identity on the corresponding summand and zero on the other, because a point has no positive-degree coherent cohomology.

Consequently the combined matrix

\[
B:C^1\longrightarrow D^1\oplus F^1
\]

has a full-column minor which is a unit at \(b\). Shrink to make that minor invertible; then \(B\) is split injective. The chain-map equations give

\[
B\,d_C^0=(d_D^0a,d_F^0a')=0.
\]

Thus \(d_C^0=0\). A basis vector of \(C^0=R\) now determines a global section of \(\mathcal L\) whose restriction to \(W_b\) is a nonzero constant multiple of a trivializing section.

Its zero scheme is closed in \(W\), and has closed image in \(B\) by properness. That image misses \(b\). Removing it makes the section nowhere vanishing, so it trivializes \(\mathcal L\). Every step works over \(R\) itself, retaining its nilpotents. \(\square\)

*Comparison locator:* [Stacks, Tag 0BF3], whose product assertion we have proved here.

**Lemma 3.4. A closed fibre locus.** For \(p:W\to B\) as in Lemma 3.2, and a line bundle \(\mathcal L\), the set

\[
C(\mathcal L)=\{b\in B:\mathcal L_b\simeq\mathcal O_{W_b}\}
\tag{8}
\]

is closed.

**Proof.** On a proper integral fibre, \(\mathcal L_b\) is trivial exactly when both \(\mathcal L_b\) and \(\mathcal L_b^{-1}\) have a nonzero section. For if \(s,t\) are such sections, their product is a nonzero section of \(\mathcal O_{W_b}\): integrality prevents it from vanishing identically. By Lemma 1.1 it is a nonzero scalar, so both sections are invertible.

The conditions \(h^0(\mathcal L_b)\geq1\) and \(h^0(\mathcal L_b^{-1})\geq1\) are closed. One can see the required upper semicontinuity directly in a free cohomology complex starting in degree zero: if its degree-zero rank is \(r\), then

\[
h^0_b=r-\operatorname{rank}(d^0\otimes\kappa(b)).
\]

The condition \(h^0_b\geq1\) is the vanishing of the \(r\times r\) minors of \(d^0\); for \(r=0\) the locus is empty. Such complexes exist locally by Lemma 3.1. The intersection of these two closed conditions is (8). \(\square\)

This lemma concerns a closed set of points; the next proof separately establishes local triviality on the actual base scheme.

## 4. The theorem of the cube and the square

**Theorem 4.1. Relative cube.** Let \(S\) be a scheme. Let \(X,Y\to S\) be proper, flat morphisms of finite presentation with geometrically integral fibres and sections \(x,y\). Let \(Z\to S\) have connected underlying space. Suppose a line bundle \(\mathcal L\) on \(X\times_SY\times_SZ\) is trivial on

\[
x(S)\times_SY\times_SZ,\qquad
X\times_Sy(S)\times_SZ,
\]

and is trivial on the fibre \(X\times_SY\times_S\operatorname{Spec}\kappa(z_0)\) for at least one \(z_0\in Z\). Then \(\mathcal L\) is trivial.

**Proof.** Apply the preceding lemmas after base change from \(S\) to \(Z\). The fibre-trivial locus (8) is closed by Lemma 3.4. At each of its points, Lemma 3.3 supplies an open neighbourhood on which \(\mathcal L\) itself is trivial. Thus that locus is also open. It is nonempty by \(z_0\), so connectedness makes it all of \(Z\).

Choose these neighbourhoods as an open cover of \(Z\), with trivializations of \(\mathcal L\) over their inverse images. The ratios on overlaps are units on the product family. By Lemma 3.2, those units come uniquely from the overlaps in \(Z\); the same is true of their inverses. Their cocycle therefore glues a line bundle \(\mathcal N\) on \(Z\) with

\[
\mathcal L\simeq p_Z^*\mathcal N.
\]

Pull back along \(x\times y\times\operatorname{id}_Z\). The left side is trivial by the slice hypotheses, and the right side is \(\mathcal N\). Hence \(\mathcal N\) and then \(\mathcal L\) are trivial. This proves the relative statement, including nonreduced and non-Noetherian parameter schemes. \(\square\)

*Comparison locator:* [Stacks, Tag 0BF4].

For an abelian variety, let \(m_I:A^3\to A\) add the coordinates indexed by \(I\). Let \(p:A^3\to\operatorname{Spec}k\) be the structure map. The pullback \(0^*L\) is a one-dimensional \(k\)-vector space, viewed as a line bundle on the point.

**Corollary 4.2. The cube on an abelian variety.** For every line bundle \(L\) on \(A\), the line bundle

\[
\begin{aligned}
\mathcal C(L)={}&m_{123}^*L
\otimes m_{12}^*L^{-1}
\otimes m_{13}^*L^{-1}
\otimes m_{23}^*L^{-1}\\
&\otimes m_1^*L\otimes m_2^*L\otimes m_3^*L
\otimes p^*(0^*L)^{-1}
\end{aligned}
\tag{9}
\]

is trivial.

**Proof.** If any coordinate is zero, terms in (9) cancel in pairs, including the last constant line. Thus all three coordinate-zero slices are trivial. Apply Theorem 4.1 with \(X=Y=Z=A\), the identity sections in the first two factors, and \(z_0=0\) in the third. The required properness, geometric integrality and connectedness were established above. \(\square\)

Choosing a trivialization of \(0^*L\) gives the usual seven-term identity

\[
m_{123}^*L\otimes m_1^*L\otimes m_2^*L\otimes m_3^*L
\simeq m_{12}^*L\otimes m_{13}^*L\otimes m_{23}^*L.
\tag{10}
\]

Formula (9) keeps track of the constant line before that choice. *Comparison locator:* [Stacks, Tag 0BFE].

**Corollary 4.3. The square.** For \(a,b\in A(k)\),

\[
t_{a+b}^*L\otimes L\simeq t_a^*L\otimes t_b^*L.
\tag{11}
\]

The same assertion holds for points over any field extension of \(k\).

**Proof.** Pull (9) back by \(A\to A^3\), \(z\mapsto(z,a,b)\). Its varying factors are exactly those of (11); the others are the constant lines \(L_a,L_b,L_{a+b},L_0\). They are one-dimensional vector spaces over the field and therefore trivial line bundles on \(A\). Choosing their trivializations yields (11). Base change gives the assertion over every extension field. \(\square\)

Equivalently, the rule \(a\mapsto[t_a^*L\otimes L^{-1}]\) is additive into the group of line-bundle isomorphism classes. This conclusion needs no construction of a Picard scheme. Over a general test scheme the constant factors in (9) must be retained; the field-point formula alone does not remove them canonically.

## 5. Multiplication pulls back quadratically

**Theorem 5.1. The integer formula.** For every line bundle \(L\) on \(A\) and every integer \(n\),

\[
[n]^*L\simeq
L^{\otimes n(n+1)/2}\otimes
([-1]^*L)^{\otimes n(n-1)/2}.
\tag{12}
\]

Negative tensor powers mean powers of the dual line bundle. If \(L\) is **symmetric**, meaning \([-1]^*L\simeq L\), this reduces to

\[
[n]^*L\simeq L^{\otimes n^2}.
\tag{13}
\]

**Proof.** Work in the additive group of line-bundle isomorphism classes. Set \(F_n=[n]^*[L]\), \(l=[L]\), and \(i=[-1]^*[L]\). Then \(F_0=0\), since pullback by the constant map is a trivializable constant line, and \(F_1=l\).

Pull the cube back along \(x\mapsto(x,x,-x)\). Its three-coordinate sum is \(x\), its two nonzero pair sums are \(2x\) and the two constant zeros, and its individual sums are \(x,x,-x\). Cancellation gives

\[
F_2=3l+i.
\]

Next pull back along \(x\mapsto(x,x,[n-1]x)\). This gives, for every \(n\),

\[
F_{n+1}+2l+F_{n-1}=F_2+2F_n,
\quad\text{hence}\quad
F_{n+1}-2F_n+F_{n-1}=l+i.
\tag{14}
\]

For \(n\geq0\), the initial conditions and this recurrence uniquely determine

\[
F_n=\frac{n(n+1)}2\,l+\frac{n(n-1)}2\,i.
\]

One verifies the initial conditions directly; each of the two quadratic coefficients has second difference one. This proves (12) for nonnegative \(n\).

For \(n=-m<0\), pull the formula for \(m\) back by \([-1]\). That operation exchanges \(l\) and \(i\), giving the same formula with \(n=-m\). If \(L\) is symmetric, the two coefficients sum to \(n^2\), proving (13). \(\square\)

*Comparison locator:* [Stacks, Tag 0BFF].

Projectivity supplies an ample line bundle \(H\). The line bundle

\[
N=H\otimes[-1]^*H
\tag{15}
\]

is ample and symmetric: inversion is an automorphism and exchanges its two factors. This choice lets us use (13) without assuming that a given ample line bundle is symmetric.

## 6. The degree and étaleness of multiplication

**Theorem 6.1. Finite locally free multiplication.** If \(d\) is a nonzero integer, then

\[
[d]:A\longrightarrow A
\]

is finite, surjective and locally free of degree \(d^{2g}\). In particular

\[
A[d]=\ker[d]
\]

is finite locally free over \(k\) of rank \(d^{2g}\).

**Proof.** Choose \(N\) as in (15). Theorem 5.1 gives \([d]^*N\simeq N^{d^2}\), an ample line bundle.

We first show that every geometric fibre is zero-dimensional. If a fibre had positive dimension, it would contain an integral projective curve \(C\): take a positive-dimensional irreducible component and successively cut by hyperplanes until its dimension is one. The pullback of \(N\) to that curve is trivial, because \([d]\) is constant on the fibre. On the other hand \(N^{d^2}|_C\) is ample and therefore has positive degree. The trivial line bundle has degree zero, a contradiction.

The morphism \([d]\) is proper, as a morphism between proper schemes with separated target. Its zero-dimensional fibres make it quasi-finite, and a proper quasi-finite morphism is finite. After extending to an algebraic closure, its closed image has dimension \(g\), since a finite morphism preserves the dimension of its source and image. The target is irreducible of dimension \(g\); a proper closed subset has smaller dimension. Thus the image is all of \(A\), proving surjectivity, which descends to \(k\).

For flatness, again work over an algebraic closure. At every closed point of the source and its image, the two local rings are regular of dimension \(g\), since \(A\) is smooth. The source ring is Cohen–Macaulay, and the local fibre has dimension zero. The local dimension equality therefore satisfies miracle flatness [Stacks, Tag 00R4], so \([d]\) is flat at every closed point. The flat locus of this finite-presentation morphism is open. Any nonempty complement on a scheme of finite type over the algebraically closed field has a closed point, so the complement is empty. Flatness descends, and finite flatness of finite presentation is finite local freeness.

Let its rank be \(r\), constant because \(A\) is connected. We compute \(r\) with Hilbert polynomials. For a finite morphism, pushforward is exact and the projection formula gives

\[
\chi(A,N^{d^2m})
=\chi\bigl(A,[d]_*\mathcal O_A\otimes N^m\bigr).
\tag{16}
\]

Here \([d]_*\mathcal O_A\) is a vector bundle of rank \(r\). For any rank-\(r\) vector bundle \(E\) on an integral projective \(g\)-fold, the leading coefficient of \(\chi(E\otimes N^m)\) is \(r\) times that of \(\chi(N^m)\). To verify this, take \(t\) large enough that \(E\otimes N^t\) is globally generated, and choose \(r\) sections forming a basis at the generic point. They give an injection

\[
(N^{-t})^{\oplus r}\longrightarrow E
\]

with cokernel supported in dimension less than \(g\). Injectivity follows because the source is torsion-free on the integral scheme and the map is generically injective. The cokernel's Hilbert polynomial has degree less than \(g\), and replacing \(m\) by \(m-t\) does not change the leading coefficient. This proves the assertion. In dimension zero the cokernel is zero and the assertion is the same rank calculation.

Write the positive leading coefficient of \(\chi(N^m)\) as \(c\), so its degree is \(g\). The two sides of (16) have leading coefficients \(c\,d^{2g}\) and \(rc\). Thus \(r=d^{2g}\). Finally the fibre over \(0\), namely \(A[d]\), inherits this rank by base change. \(\square\)

*Comparison locators:* [Stacks, Tag 0BFG] and the general degree calculation [Stacks, Tag 0BEX]. The proof uses the Hilbert-polynomial leading term, so it does not require a Riemann–Roch formula for abelian varieties.

**Theorem 6.2. The étaleness criterion.** If \(g>0\), then \([d]\) is étale exactly when \(d\) is invertible in \(k\). For \(d\ne0\), the same criterion holds for the finite group scheme \(A[d]\). If \(g=0\), every \([d]\), including \([0]\), is the identity of \(\operatorname{Spec}k\).

**Proof.** For \(d\ne0\), Theorem 6.1 supplies finite flatness. The differential at the identity is

\[
\operatorname{Lie}([d])=d\,\operatorname{id}_{\operatorname{Lie}(A)}.
\tag{17}
\]

Indeed the tangent group law adds tangent vectors, as proved in the Lie-algebra lesson; induction and inversion give (17) for every integer. Translation identifies the differential at any geometric point with that at \(0\).

If \(d\) is invertible, these differentials are isomorphisms. The relative cotangent module vanishes at every geometric closed point, hence everywhere by Nakayama and finite type. Thus \([d]\) is unramified; finite flat unramified morphisms are étale.

If \(d=0\) in \(k\) and \(g>0\), (17) is zero on a nonzero \(g\)-dimensional tangent space, so \([d]\) is not unramified at \(0\) and cannot be étale. The left exactness of the Lie functor gives

\[
\operatorname{Lie}(A[d])=\ker\operatorname{Lie}([d])
=\operatorname{Lie}(A)
\]

in this case. A finite étale scheme over a field has zero tangent space, so \(A[d]\) is not étale either. In the invertible case it is an étale base change of \([d]\).

The integer \(d=0\) gives a constant morphism; if \(g>0\), its fibre over \(0\) is \(A\), so it is not étale. If \(g=0\), Section 1 identifies \(A\) with the trivial group scheme, proving the stated exception. \(\square\)

*Comparison locator:* [Stacks, Tag 0BFH], which assumes a nonzero abelian variety. The dimension-zero exception must also be retained when using a summary of the torsion properties.

Over an algebraically closed field, the surjectivity in Theorem 6.1 makes \(A(k)\) a divisible abelian group: every point has a \(d\)-division point for every \(d\geq1\). Surjectivity on points follows because every nonempty finite fibre over that field has a rational point.

## 7. Torsion points and Tate modules

Fix a separable closure \(k_s\) and its absolute Galois group \(\Gamma\).

**Theorem 7.1. Torsion of invertible order.** If \(n\geq1\) is invertible in \(k\), then

\
A[n\simeq(\mathbf Z/n)^{2g}
\tag{18}
\]

as abstract abelian groups. The isomorphism is generally not canonical and does not assert that the Galois action is trivial.

**Proof.** The finite group scheme \(A[n]\) is étale of rank \(n^{2g}\). Over the separably closed field, a finite étale algebra is a product of copies of \(k_s\). Thus its group of points has exactly \(n^{2g}\) elements.

First take \(n=\ell^r\), with \(\ell\) a prime invertible in \(k\), and \(r\geq1\). Put \(H=A\ell^r\). It is a finite abelian group killed by \(\ell^r\), so its elementary-divisor decomposition is

\[
H\simeq\bigoplus_{i=1}^a\mathbf Z/\ell^{b_i},
\qquad 1\leq b_i\leq r.
\]

Its subgroup killed by \(\ell\) is exactly \(A\ell\), of size \(\ell^{2g}\). Every summand contributes \(\ell\), so \(a=2g\). The size of \(H\) is \(\ell^{2gr}\); hence \(\sum_i b_i=2gr\). There are \(2g\) terms, each at most \(r\), so every \(b_i=r\).

For general \(n=\prod_\ell\ell^{r_\ell}\), the elementary Chinese-remainder idempotents in \(\mathbf Z/n\) decompose the killed-by-\(n\) group into its \(\ell\)-primary subgroups. Those are \(A\ell^{r_\ell}\): the idempotents project onto them and their sum is one. The prime-power result and the Chinese remainder theorem prove (18). \(\square\)

In particular the cardinality alone at one composite \(n\) would not have determined the group; the degree calculation for its prime divisors is the additional input.

For a prime \(\ell\) invertible in \(k\), define

\
T_\ell(A)=\varprojlim_r A[\ell^r,
\tag{19}
\]

with transition maps multiplication by \(\ell\). It is a \(\mathbf Z_\ell\)-module.

**Theorem 7.2. The Tate module.** There is an isomorphism

\[
T_\ell(A)\simeq\mathbf Z_\ell^{\,2g}.
\tag{20}
\]

The action of \(\Gamma\) is continuous for the inverse-limit topology and defines, after choosing a basis, a continuous homomorphism

\[
\rho_{A,\ell}:\Gamma\longrightarrow
\mathrm{GL}_{2g}(\mathbf Z_\ell).
\tag{21}
\]

**Proof.** The transition map \(P_{r+1}\to P_r\), where \(P_r=A\ell^r\), is surjective. Given a point in \(P_r\), its fibre under \([\ell]\) is a nonempty finite étale scheme over \(k_s\), and therefore has a \(k_s\)-point. Any such lift is killed by \(\ell^{r+1}\).

Choose a basis \(v_{1,1},\ldots,v_{2g,1}\) of \(P_1\). Recursively lift each \(v_{i,r}\) to \(v_{i,r+1}\) with \(\ell v_{i,r+1}=v_{i,r}\). These lifts form a basis at every level. To prove it, Theorem 7.1 identifies \(P_{r+1}\) as a free \(\mathbf Z/\ell^{r+1}\)-module of rank \(2g\). Multiplication by \(\ell^r\) induces an isomorphism

\[
P_{r+1}/\ell P_{r+1}\xrightarrow{\sim}P_1.
\]

The chosen lifts map to the original basis in \(P_1\). Nakayama over the local ring \(\mathbf Z/\ell^{r+1}\) makes them generators; their number and the equal finite cardinalities make the resulting map from the free module an isomorphism.

In these compatible bases the transition maps send a coordinate modulo \(\ell^{r+1}\) to its reduction modulo \(\ell^r\), because \(\ell v_{i,r+1}=v_{i,r}\). Taking inverse limits proves (20).

The Galois action on each \(P_r\) factors through a finite quotient: the finite étale scheme splits over a finite separable extension. It commutes with multiplication by \(\ell\), so acts on the inverse limit. Stabilizers of each finite-level tuple are open, exactly the continuity condition for (21) with its \(\ell\)-adic topology. \(\square\)

## 8. What changes in characteristic \(p\)

Suppose \(\operatorname{char}k=p>0\). The group scheme \(A[p]\) still has rank \(p^{2g}\), but its geometric points can be far fewer.

**Theorem 8.1. The point bound.** The geometric kernel of \([p]\) has at most \(p^g\) points.

**Proof.** Extend to an algebraically closed field; neither geometric points nor \(g\) change. The case \(g=0\) is immediate. Let \(K\) be the function field of the target \(A\), and \(L\) that of the source of \([p]\). Theorem 6.1 gives \([L:K]=p^{2g}\), where \(K\) is embedded by \([p]^*\).

By (17) and translations, the differential of \([p]\) vanishes everywhere. Thus its function-field image lies in \(L^p\): over the perfect ground field a function has zero differential exactly when it is a \(p\)-th power [Stacks, Tag 031W].

The smooth \(g\)-dimensional function field \(K\) has a \(p\)-basis \(t_1,\ldots,t_g\): the \(p^g\) monomials \(\prod t_i^{e_i}\), \(0\leq e_i<p\), form a basis over \(K^p\). This follows from the correspondence between \(p\)-bases and bases of \(\Omega_{K/k}\) [Stacks, Tags 07P1–07P2]. Adjoining their \(p\)-th roots gives a purely inseparable extension \(K^{1/p}/K\) of degree \(p^g\). Since each \([p]^*t_i\) has a \(p\)-th root in \(L\), it embeds as an intermediate field

\[
K\subset E\simeq K^{1/p}\subset L,\qquad
[E:K]=[L:E]=p^g.
\tag{22}
\]

We make the point count on an actual open fibre, rather than only on the function fields. On a nonempty affine open \(U=\operatorname{Spec}R\) in the target, shrink so that the \(t_i\) are regular and their chosen roots are regular on \([p]^{-1}(U)=\operatorname{Spec}B\). This is possible because \([p]\) is finite: the closed locus where any of the finitely many source rational functions is not regular has proper closed image, missing the generic point.

There is then a factorization

\[
\operatorname{Spec}B\longrightarrow
\operatorname{Spec}C\longrightarrow\operatorname{Spec}R,
\quad
C=R[u_1,\ldots,u_g]/(u_i^p-t_i).
\tag{23}
\]

The ring \(C\) is free over \(R\) on the \(p^g\) bounded monomials. Its map to \(B\) is injective: it is injective after passage to \(K\) by (22), and \(C\) is \(R\)-free. Thus \(C\) is a domain with fraction field \(E\). The extension \(B/C\) is finite, since a finite list of \(R\)-module generators of \(B\) also generates it over \(C\).

After one more shrinking of \(U\), \(B\) is free of rank \(p^g\) over \(C\). Here is a concrete justification. Choose an \(E\)-basis from \(B\); clearing the finitely many denominators expressing module generators gives a nonzero \(c\in C\) for which \(B_c\) is free of that rank. The determinant \(N_{C/R}(c)\) is nonzero, since multiplication by \(c\) is invertible over the fraction field. On \(D(N_{C/R}(c))\subset U\), the adjugate formula makes \(c\) a unit in \(C\), so this target shrinking suffices.

For every algebraically closed residue field, the second map in (23) has exactly one point in its fibre: each equation \(u_i^p=t_i\) has a unique root. The first map has at most \(p^g\) points over that point, because its fibre algebra has vector-space dimension \(p^g\). Therefore \([p]\) has at most \(p^g\) points over a closed point of this nonempty \(U\).

All closed-point fibres of \([p]\) have the same number of points. It is surjective, and a preimage of a point translates the kernel isomorphically to that fibre. The count over \(U\) consequently gives the same bound for the kernel. \(\square\)

*Comparison locator:* [Stacks, Tag 0C0Y].

The **\(p\)-rank** \(f\) of \(A\) is defined by

\[
A[p](\overline k)\simeq(\mathbf Z/p)^f.
\]

Such an \(f\) exists because the group is finite and killed by \(p\); Theorem 8.1 gives \(0\leq f\leq g\). More generally

\[
A[p^r](\overline k)\simeq(\mathbf Z/p^r)^f.
\tag{24}
\]

To prove it, multiplication by \(p\) surjects from \(A[p^{r+1}](\overline k)\) onto \(A[p^r](\overline k)\), using divisibility of \(A(\overline k)\). Its kernel is \(A[p](\overline k)\), so induction gives cardinality \(p^{fr}\). An elementary-divisor decomposition at level \(r\) has \(f\) summands, as seen by taking its killed-by-\(p\) subgroup. Each exponent is at most \(r\), and their sum is \(fr\); all are therefore \(r\). This proves (24). It describes geometric points and does not identify the nonreduced finite group scheme.

## 9. Elliptic curves make the difference visible

An **elliptic curve** is a one-dimensional abelian variety. We now construct the group law on a smooth plane cubic with a chosen rational flex. The construction includes coincident points and tangent lines, and proves the identities as identities of morphisms, so they hold on families with nilpotent parameters as well.

**Lemma 9.0a. Point classes on a cubic.** Let \(C\) be a smooth plane cubic over an algebraically closed field. If two points \(P,Q\) have linearly equivalent degree-one divisors, then \(P=Q\).

**Proof.** First \(C\) is integral. A reducible cubic has a line component and a remaining degree-two component; their equations have a common point over the algebraically closed field, because the latter restricts to a positive-degree homogeneous polynomial on that line. At that point the derivative of their product vanishes. A repeated component similarly contradicts smoothness. Thus the cubic is irreducible and reduced.

There is a nowhere vanishing regular differential on \(C\), in every characteristic. Write its homogeneous equation as \(F(X,Y,Z)=0\). On \(Z\ne0\), put \(x=X/Z\), \(y=Y/Z\) and \(f(x,y)=F(x,y,1)\). On the opens where the indicated denominator is a unit, set

\[
\omega=\frac{dx}{f_y}=-\frac{dy}{f_x}.
\]

The equality follows from \(df=f_xdx+f_ydy=0\), and the smooth-curve differential module shows that each expression is a regular generator on its open. Those opens cover this affine chart: if both partials vanished, Euler's homogeneous identity on \(F=0\) would also force \(F_Z=0\), contrary to smoothness. No division by the characteristic or by the degree is involved.

On \(Y\ne0\), use the cyclic coordinates \(u=Z/Y\), \(v=X/Y\), with equation \(g(u,v)=F(v,1,u)\), and take \(du/g_v=-dv/g_u\). On the overlap with \(Z\ne0\), we have \(u=1/y\), \(v=x/y\) and \(g_v=y^{-2}f_x\). Hence \(du/g_v=-dy/f_x\), proving that these generators agree. The same cyclic calculation on \(X\ne0\) completes the gluing. Thus \(\omega\) is globally regular and nowhere vanishing.

If \(P\ne Q\) and \((P)-(Q)\) were principal, its defining rational function \(h\) would give a nonconstant morphism \(f:C\to\mathbf P^1\) with a single simple pole at \(Q\). The local extension to a morphism is explicit: the regular local ring of a smooth curve is a DVR, so at each point either \(h\) or \(h^{-1}\) is regular. These expressions give its two projective charts and agree on their overlap.

Here is the finiteness argument in this particular projective-curve situation. The graph embeds \(C\) as a closed subscheme of \(\mathbf P^2\times\mathbf P^1\), so \(f\) is projective and proper. Its fibres are finite: the inverse image of a point is a proper closed subset of the integral curve, hence has dimension zero and finitely many points. At each closed target point, choose a linear form on \(\mathbf P^2\) not vanishing at any point of that fibre. Such a form exists over the infinite algebraically closed field. The image of its zero section on \(C\) is closed by properness and misses the chosen target point. On an affine neighbourhood \(V=\operatorname{Spec}A\) avoiding this image, the whole inverse image lies in the affine chart where the linear form is nonzero. It is closed in \(\mathbf A^2\times V\), and therefore is affine, say \(\operatorname{Spec}B\). These neighbourhoods cover the target, since a nonempty closed subset of \(\mathbf P^1\) has a closed point.

Every element \(b\in B\) is integral over \(A\). For if a nonzero \(b\) were not integral, then \(b^{-1}\) would be a nonunit of \(A[b^{-1}]\): an equation making it a unit would, after multiplication by a power of \(b\), give a monic equation for \(b\). Choose a maximal ideal containing \(b^{-1}\), and a valuation ring of \(k(C)\) dominating the resulting local domain. Its existence is proved in *Valuation rings and the valuative criterion of separatedness*, Theorem 2.1. The generic point map to \(C\) extends to this valuation ring: scale its three homogeneous coordinates so that all lie in the valuation ring and one is a unit; the equation of \(C\) continues to hold. Its composite to \(V\) is the given map because the two maps agree generically and \(V\) is separated. Thus it factors through \(f^{-1}(V)=\operatorname{Spec}B\), which puts \(b\) in the valuation ring. This contradicts \(b^{-1}\) being in its maximal ideal. Therefore \(B/A\) is integral. It is of finite type, so finitely many algebra generators satisfy monic equations; their bounded powers span a finite \(A\)-module. Hence \(f\) is finite.

It is flat, since its finite coordinate module over each target DVR is torsion-free and hence free. Its fibre at infinity has length one, so its finite flat rank is one. The unit map to a finite locally free algebra of rank one is an isomorphism, as can be checked on its residue fields and then by Nakayama. The curve would therefore be isomorphic to \(\mathbf P^1\).

But \(\mathbf P^1\) has no nonzero regular differential. On its affine chart such a differential is \(h(t)dt\) with polynomial \(h\); under \(t=1/u\), every nonzero such expression has a pole at \(u=0\). This contradicts the differential \(\omega\) just constructed. Hence \(P=Q\). \(\square\)

**Theorem 9.0. The cubic group law.** Let \(C/k\) be a smooth plane cubic with a rational flex \(O\). There is a commutative group-scheme structure on \(C\) with identity \(O\). If a line cuts out the divisor \((P)+(Q)+(R)\), counting multiplicities, then \(P+Q+R=O\). For geometric points,

\[
[(P+Q)-(O)]=[(P)-(O)]+[(Q)-(O)]
\]

in the group of degree-zero divisor classes. More precisely, for every field extension \(L/k\) and \(P,Q\in C(L)\), the divisor \((P)+(Q)-(P+Q)-(O)\) is principal over \(L\) itself. The group law is a morphism on \(C\times_k C\), including the diagonal; its scheme identities remain valid after every base change.

**Proof.** Smoothness implies geometric integrality by the preceding irreducibility argument after extending the field. The curve is smooth, projective and one-dimensional. It remains to construct the operations and verify their identities.

**Secants across the diagonal.** Put \(B=C\times_k C\), and denote its two universal points by \(P,Q\). For distinct points their joining line has coefficients given by the three minors of their homogeneous coordinate vectors, or equivalently by \(\det(P,Q,-)\). These are locally sections of one invertible sheaf on \(B\). Their common ideal is the diagonal ideal: the analogous minors define the diagonal of \(\mathbf P^2\), whose pullback to \(C\times C\) is exactly the diagonal of the closed immersion \(C\to\mathbf P^2\).

The diagonal of a smooth curve is an effective Cartier divisor. Divide the three coefficients by a local equation of this divisor. The quotients generate the unit ideal, since the original coefficients generate the diagonal ideal. Thus they define a morphism from \(B\) to the dual projective plane; changes of local equation multiply all three by the same unit, so the maps glue. Its value on the diagonal is the tangent line: the divided coordinate differences are precisely the first derivatives of the curve's immersion. We have obtained a universal secant-or-tangent line \(\ell\), without choosing a slope or omitting vertical lines.

**The residual point in families.** In \(C\times B\), the equation of \(\ell\) cuts out a relative divisor \(D\). The two graphs \(\Gamma_P,\Gamma_Q\) are Cartier divisors, and its section vanishes on both. The equation is divisible by their product, including where \(P=Q\). Here is a local check at such an intersection. Choose an étale parameter on the smooth curve; near the triple diagonal the graph ideals have equations \(a=t-p\), \(b=t-q\). Their difference defines the diagonal in the parameter base. In particular \(a,b\) form a regular sequence. If an element divisible by \(a\) also belongs to \((b)\), reducing modulo \(b\) and using that \(a\) is a non-zero-divisor there proves divisibility by \(ab\). Away from their intersection the same assertion is immediate. These local factorizations give a global residual divisor

\[
D-\Gamma_P-\Gamma_Q.
\]

On every geometric fibre the line meets the cubic in length three: restriction of its homogeneous cubic equation to the line is a nonzero degree-three polynomial on \(\mathbf P^1\). It is nonzero because an integral cubic has no line component. The two graph divisors remove length two, with multiplicity when they coincide. The residual divisor therefore has length one on every geometric fibre.

It is the graph of a section \(r:B\to C\). To justify this family assertion, a residual zero of length one on a smooth curve has a nonzero derivative in a curve parameter. The étale-coordinate criterion consequently makes the residual divisor étale over \(B\). Its geometric fibres each consist of one reduced point. The diagonal of this étale morphism is an open immersion; it contains every geometric point of the fibre product, and therefore is an isomorphism. Thus the morphism is a monomorphism. It is also a surjective étale covering, so its unique local sections descend and give an inverse. It is an isomorphism to \(B\), as asserted. This proves that the third-intersection point is a morphism, also for tangents and flexes. All these statements concern the universal family over \(B\); their pullbacks apply to every test scheme.

Define \(i(P)=r(P,O)\) and \(m(P,Q)=i(r(P,Q))\). Both are morphisms over \(k\). We prove that they are inversion and addition.

The principal-divisor formula already holds over the field of definition. For \(P,Q\in C(L)\), put \(R=r(P,Q)\) and \(S=i(R)\). The secant-or-tangent line \(\ell_{P,Q}\) and the line \(\ell_{R,O}\) are defined over \(L\) by the morphism just constructed. Their respective intersection divisors are \((P)+(Q)+(R)\) and \((R)+(O)+(S)\). The quotient of their linear equations, restricted to \(C_L\), is a nonzero rational function with divisor

\[
\operatorname{div}\bigl(\ell_{P,Q}/\ell_{R,O}\bigr)
=(P)+(Q)-(S)-(O).
\]

The restrictions are nonzero because the cubic has no line component. This computation includes repeated points and coincident lines; in the latter case the quotient is constant and the divisor is zero. It proves principality over \(L\), without a descent assertion about divisor classes. After identifying \(m\) with addition, it is the promised formula with \(S=P+Q\).

**Divisor classes give the identities.** Work over an algebraic closure for this verification. Every line section is linearly equivalent to the hyperplane divisor. The tangent line at the flex \(O\) cuts out \(3(O)\), so for every pair of points

\[
(P)+(Q)+(r(P,Q))\sim3(O),\qquad
(R)+(O)+(i(R))\sim3(O).
\]

Subtracting these identities gives

\[
[(m(P,Q))-(O)]=[(P)-(O)]+[(Q)-(O)],\qquad
[(i(P))-(O)]=-[(P)-(O)].
\]

By Lemma 9.0a the map \(P\mapsto[(P)-(O)]\) is injective. Associativity and commutativity of divisor-class addition therefore prove those identities for \(m\) on every geometric triple or pair. The zero class proves the identity law for \(O\), and the second formula proves the inverse law for \(i\). They also prove the asserted principal-divisor relation and the line rule.

Finally these are identities of morphisms. The sources \(C\), \(C^2\) and \(C^3\) are geometrically reduced schemes of finite type, and the target is separated. The closed equalizer of two of the morphisms contains every geometric point; on affine charts its equations consequently lie in the nilradical, which is zero. Thus the morphisms agree after the algebraic closure and hence over \(k\). Identities of scheme morphisms persist after arbitrary base change, including bases with nilpotents. The resulting smooth projective geometrically integral group curve is an abelian variety. \(\square\)

*Comparison and credit:* Milne, *Algebraic Groups*, Chapter 2c, records the cubic group-law construction. The proof above supplies the secant family, residual section, injective point classes and all scheme identities internally; it does not assume representability of a Picard scheme or an elliptic group law in order to construct this one.

**Example 9.1. Four points of order dividing two.** Let \(\operatorname{char}k\ne2\), and let \(f(x)\) be a separable cubic. The smooth projective curve with affine equation

\[
E:y^2=f(x)
\]

has a unique point \(O=[0:1:0]\) at infinity, a rational flex. Its affine partial derivatives are \(2y\) and \(-f'(x)\); a common zero on the curve would be a repeated root of \(f\), so none exists. The homogeneous \(Z\)-partial is nonzero at \(O\), proving smoothness there as well. A smooth plane cubic is geometrically integral: distinct positive-degree components in the geometric plane would meet and make the curve singular. The vertical line through \((x,y)\) meets the cubic at \((x,y),(x,-y),O\). Thus inversion is \((x,y)\mapsto(x,-y)\). An affine point is killed by two exactly when \(y=0\). Over \(\overline k\) these are the three distinct points \((r_i,0)\) at the roots of \(f\). Together with \(O\) they give

\[
E[2](\overline k)\simeq(\mathbf Z/2)^2.
\tag{25}
\]

The group is killed by two and has four elements, which proves the isomorphism directly. It is also the \(g=1,n=2\) instance of (18).

**Example 9.2. Ordinary and supersingular in characteristic two.** Over an algebraically closed field of characteristic two consider

\[
E_{\mathrm{ord}}:y^2+xy=x^3+1,\qquad
E_{\mathrm{ss}}:y^2+y=x^3.
\tag{26}
\]

Both are smooth projective cubics with the flex \(O=[0:1:0]\) at infinity. For the first, the homogeneous equation is

\[
F=Y^2Z+XYZ+X^3+Z^3=0.
\]

On the affine chart \(Z=1\), its partial derivatives in \(x,y\) are \(y+x^2,x\). A singular point would have \(x=y=0\), which does not lie on the curve. At infinity the equation forces \(X=0\), and \(F_Z\) is nonzero at \(O\). For the second cubic the homogeneous equation is \(Y^2Z+YZ^2+X^3=0\); its three partial derivatives are \(X^2,Z^2,Y^2\), which cannot all vanish at a projective point.

In each equation a vertical line's two affine intersections are exchanged by

\[
(x,y)\longmapsto(x,y+x)\quad\text{on }E_{\mathrm{ord}},
\qquad
(x,y)\longmapsto(x,y+1)\quad\text{on }E_{\mathrm{ss}}.
\]

The third intersection is \(O\), so these are the inverse maps. In the first curve an affine point fixed by inversion has \(x=0\), then \(y^2=1\), giving the unique point \((0,1)\). Its two-torsion has two geometric points including \(O\), hence \(p\)-rank one. In the second curve no affine point is fixed, so its two-torsion has only \(O\), hence \(p\)-rank zero.

An elliptic curve is called **ordinary** when its \(p\)-rank is one and **supersingular** when it is zero. These two cases exhaust the possibilities by \(f\leq g=1\). The computations in (26) realize both. Theorem 6.1 nevertheless gives rank four for both finite group schemes \(E[2]\); the point counts two and one record different nonreduced structures.

**Example 9.3. Products.** If \(A=E_1\times\cdots\times E_g\), then it is an abelian variety: smoothness, properness and geometric integrality are preserved in this finite product, and the group law is coordinatewise. Its torsion schemes and point groups are the corresponding products. In positive characteristic its \(p\)-rank is the sum of the elliptic \(p\)-ranks. In characteristic two, taking \(f\) copies of the first curve in (26) and \(g-f\) of the second realizes every point count \(2^f\), \(0\leq f\leq g\), while the kernel rank remains \(2^{2g}\).

## 10. Equivalent definitions and families

**Proposition 10.1. Sixteen definitions.** Choose one property from each row:

| Properness | Connectedness | Smoothness or reducedness |
|---|---|---|
| proper or projective | connected, geometrically connected, irreducible or geometrically irreducible | smooth or geometrically reduced |

A \(k\)-group scheme with those three chosen properties is an abelian variety, and every abelian variety has all the listed properties.

**Proof.** Every combination implies the weakest one: proper, connected and geometrically reduced. Properness gives finite type. The connected-group results of *Group schemes over a field* give geometric irreducibility for a connected group scheme; together with geometric reducedness this is geometric integrality. Thus the weakest combination already gives our definition.

Conversely an abelian variety is proper and geometrically integral, hence satisfies all four connectedness properties and geometric reducedness. Proposition 1.2 gives projectivity and smoothness. This proves the assertion for all \(2\cdot4\cdot2=16\) choices. \(\square\)

*Comparison locators:* [Stacks, Tags 03RP and 0H2U]. In the multiplication criteria of the summary, the trivial abelian variety has the dimension-zero exception from Theorem 6.2.

An **abelian scheme** over \(S\) is a smooth proper commutative \(S\)-group scheme of finite presentation with geometrically connected fibres. Each fibre is an abelian variety: it is proper, smooth and geometrically connected, so Proposition 10.1 applies over its residue field. Abelian varieties are the case \(S=\operatorname{Spec}k\). This is the family notion used in *Néron models*, where the extension across a missing special fibre is governed by a mapping property.

## 11. Exercises

**Exercise 1 (easy): remove the translation.** Use rigidity to prove that every morphism of abelian varieties is a homomorphism followed by a unique translation.

**Exercise 2 (medium): two-torsion on a cubic.** For \(y^2=f(x)\), with \(f\) a separable cubic and \(\operatorname{char}k\ne2\), compute the four geometric points of \(E[2]\), and determine their abstract group.

**Exercise 3 (medium): extract the square.** Pull the cube back along \(z\mapsto(z,a,b)\), \(a,b\in A(k)\). Identify every varying and constant factor, and deduce the theorem of the square.

**Exercise 4 (medium): symmetric multiplication.** Prove formula (12) from the cube and deduce (13). Construct a symmetric ample line bundle from an arbitrary ample line bundle.

**Exercise 5 (hard): recover the torsion group.** Prove \(An\simeq(\mathbf Z/n)^{2g}\) for invertible \(n\), using the degrees of multiplication for the prime divisors of \(n\). Explain why the order at a single \(n\) is insufficient by itself.

**Exercise 6 (hard): compatible Tate bases.** Prove surjectivity of the transition maps in (19), construct compatible bases, and deduce that the Galois action on \(T_\ell(A)\) is continuous.

**Exercise 7 (medium): the missing connectedness hypothesis.** Give a proper geometrically integral \(X\) and a disconnected \(Y\) for which one fibre of \(X\times Y\to Z\) is contracted but the morphism does not globally factor through \(Y\). Locate the step of the rigidity proof that fails.

**Exercise 8 (hard): why nilpotent parameters survive the cube proof.** In Lemma 3.3, write down the equation between the degree-zero differentials and degree-one restriction matrices. Explain why an invertible minor forces a section to lift over the entire local base ring, and how properness turns it into a local trivialization of the family.

**Exercise 9 (medium): equal length, unequal point counts.** Check the smoothness and inverse maps of the two cubics (26). Compute their geometric two-torsion points and compare with the ranks of their two-torsion schemes.

**Exercise 10 (hard): higher \(p\)-power points.** Assuming the point bound and surjectivity of every \([d]\), prove (24). Determine the \(p\)-rank of a product and verify the dimension-zero exception to the étaleness criterion.

## 12. Complete solutions

**Solution 1.** Set \(b=f(0)\), and \(u=t_{-b}\circ f\). It satisfies \(u(0)=0\). The morphism \(v(x,y)=u(x+y)-u(x)-u(y)\) is zero on \(A\times\{0\}\). The source factor \(A\) is proper with \(H^0(A,\mathcal O)=k\), the parameter factor is connected, and the target is separated. Rigidity therefore makes \(v\) independent of \(x\). Its restriction to \(\{0\}\times A\) is also zero, so \(v=0\). This is the homomorphism identity for \(u\), and \(f=t_b\circ u\). Any homomorphism sends \(0\) to \(0\), so evaluation determines \(b\) and then \(u\) uniquely.

**Solution 2.** The point at infinity is \(O\). On an affine vertical line the two intersections are \((x,y)\) and \((x,-y)\), and the third is \(O\); the line rule makes them inverses. A finite point of order dividing two therefore satisfies \(y=-y\). Since two is invertible, this means \(y=0\). The curve equation then gives precisely the three points at the distinct roots of \(f\). There are four points including \(O\), all killed by two. An abelian group killed by two is a vector space over \(\mathbf F_2\); its size four gives dimension two and group \((\mathbf Z/2)^2\). No root coincidence is possible because \(f\) is separable.

**Solution 3.** Along \((z,a,b)\), the pullback of (9) is

\[
t_{a+b}^*L\otimes(t_a^*L)^{-1}
\otimes(t_b^*L)^{-1}\otimes L
\otimes
(L_{a+b})^{-1}\otimes L_a\otimes L_b\otimes(L_0)^{-1},
\]

where the last four factors mean constant line bundles on \(A\). The cube says the product is trivial. Each constant factor is a one-dimensional \(k\)-vector space and hence has a basis; trivializing them yields

\[
t_{a+b}^*L\otimes L\simeq t_a^*L\otimes t_b^*L.
\]

The calculation also shows the exact correction factors if \(a,b\) are families over a more general base, where those lines need not have chosen global bases.

**Solution 4.** In line-bundle classes write \(F_n=[n]^*[L]\), \(l=[L]\), \(i=[-1]^*[L]\). The substitution \((x,x,-x)\) gives \(F_2=3l+i\). The substitution \((x,x,[n-1]x)\) gives

\[
F_{n+1}-2F_n+F_{n-1}=l+i.
\]

With \(F_0=0,F_1=l\), the unique solution for nonnegative integers is

\[
F_n=\frac{n(n+1)}2l+\frac{n(n-1)}2i.
\]

For negative integers pull back by inversion, which exchanges \(l,i\). If \(L\) is symmetric, \(i=l\), and the total coefficient is \(n^2\). Given any ample \(H\), inversion preserves ampleness and the tensor product of ample line bundles is ample. Thus \(H\otimes[-1]^*H\) is ample; inversion exchanges its two factors, making it symmetric.

**Solution 5.** Finite étaleness gives \(|Ad|=d^{2g}\) for every invertible positive divisor \(d\) of \(n\). For \(n=\ell^r\), decompose the killed-by-\(\ell^r\) group as \(\bigoplus_{i=1}^a\mathbf Z/\ell^{b_i}\), \(1\leq b_i\leq r\). Its killed-by-\(\ell\) subgroup is \(A\ell\), so \(a=2g\). Its total order gives \(\sum b_i=2gr\). The upper bounds on the \(2g\) terms force \(b_i=r\) for every \(i\). Chinese-remainder primary decomposition gives the general \(n\) result.

For comparison, a group of order \(\ell^4\) killed by \(\ell^2\) could be \((\mathbf Z/\ell^2)^2\), \(\mathbf Z/\ell^2\oplus(\mathbf Z/\ell)^2\), or \((\mathbf Z/\ell)^4\). The total order and exponent bound alone do not distinguish them. Their killed-by-\(\ell\) subgroup sizes do, which is why the lower-order degree information is needed.

**Solution 6.** Given \(x\in A\ell^r\), the fibre of \([\ell]\) over \(x\) is nonempty and finite étale. It has a \(k_s\)-point \(y\); since \(\ell y=x\), it is killed by \(\ell^{r+1}\). This proves surjectivity. Choose a basis at level one and recursively lift it through these maps.

At level \(r+1\), multiplication by \(\ell^r\) identifies \(P_{r+1}/\ell P_{r+1}\) with \(P_1\), by the already-proved free structure of \(P_{r+1}\). The compatible lifts map to the original basis there. Nakayama makes them generators over \(\mathbf Z/\ell^{r+1}\); a generating map from a free module of the same rank is bijective here because the two finite sets have equal cardinalities. The coordinates reduce under the transition maps, so the limit is \(\mathbf Z_\ell^{2g}\).

At each finite level the Galois action factors through the finite Galois group of a splitting field for the finite étale torsion scheme. The kernels of all these finite-level actions are open in \(\Gamma\). They are the preimages of the congruence neighbourhoods of the identity in \(\mathrm{GL}_{2g}(\mathbf Z_\ell)\), proving continuity.

**Solution 7.** Take \(X=\mathbf P^1_k\), \(Y=\operatorname{Spec}k\amalg\operatorname{Spec}k\), and \(Z=\mathbf P^1_k\). On the first component let the map be constant at a rational point, and on the second let it be the identity. The first fibre is contracted and the second is not, so no map from \(Y\) can recover it by projection. In (3) the contracted-fibre locus is the first open and closed component. It is nonempty but is not all of \(Y\); the connectedness step is exactly what fails.

**Solution 8.** Represent the three derived pushforwards by free complexes \(C,D,F\) adapted to the fibre. Their degree-zero terms are the base ring \(R\), and the unit sections make \(d_D^0=d_F^0=0\). Let \(a,a'\) be the degree-zero maps of restriction and \(B=(b,b')\) the combined degree-one map. The chain equations are

\[
B\,d_C^0=(d_D^0a,d_F^0a')=(0,0).
\]

Künneth makes \(B\) injective after reduction to the residue field. Inverting a full-column minor makes \(B\) split injective over \(R\), so \(d_C^0=0\) over \(R\), including any nilpotents. The basis of \(C^0\) therefore lifts the trivializing fibre section to a genuine section of \(\mathcal L\). Its zero scheme has closed image under the proper product family and misses the chosen point. Removing that image makes the lifted section invertible on the whole inverse image of an open neighbourhood. This supplies local triviality on the scheme, rather than merely at its reduced points.

**Solution 9.** For \(y^2+xy=x^3+1\), the affine partials \(y+x^2,x\) would both vanish only at \((0,0)\), which is off the curve. Its unique point at infinity is \(O\), where the homogeneous \(Z\)-partial is nonzero. For \(y^2+y=x^3\), the homogeneous partials are \(X^2,Z^2,Y^2\), with no common projective zero. Both curves are smooth.

The vertical-line involutions are \(y\mapsto y+x\) and \(y\mapsto y+1\), respectively. They preserve the equations and exchange the two finite intersections on the line; their third intersection is \(O\), so they give inversion. The first involution fixes exactly the affine point \((0,1)\), while the second fixes no affine point. Including \(O\) gives two and one geometric two-torsion points. In both cases \(g=1,d=2\), so Theorem 6.1 gives finite locally free rank \(2^2=4\). Hence the ranks agree while the \(p\)-ranks are one and zero.

**Solution 10.** Over \(\overline k\), surjectivity of \([p]\) gives a \(p\)-division point of any \(p^r\)-torsion point, and such a lift is killed by \(p^{r+1}\). Thus

\[
0\longrightarrow A[p](\overline k)
\longrightarrow A[p^{r+1}](\overline k)
\xrightarrow{p}A[p^r](\overline k)
\longrightarrow0
\]

is exact. If the first group has size \(p^f\), induction gives size \(p^{fr}\) at level \(r\). The elementary-divisor decomposition of that level has exactly \(f\) factors, counted by its killed-by-\(p\) subgroup. Each exponent is at most \(r\), and their sum is \(fr\), so all exponents are \(r\). This proves (24).

Products have coordinatewise kernels and point groups, so their \(p\)-ranks add. Finally a zero-dimensional abelian variety is \(\operatorname{Spec}k\). Its group is trivial and every multiplication is its identity, an étale map regardless of whether \(d\) is invertible. The positive-dimensional hypothesis in the converse of Theorem 6.2 is therefore necessary.

## What this lesson does not prove

The construction of the elliptic-curve group law from a smooth plane cubic and its rational flex is proved in Lemma 9.0a and Theorem 9.0, including the rational-function divisor formula over every extension field and the scheme identities in families. Its line rule supplies the inversion and torsion computations. We also prove the smoothness and all torsion calculations of the chosen cubics. The point-class argument gives its own projective-curve finiteness proof; its valuation-ring domination input is the full internal proof in *Morphisms of schemes*, *Valuation rings and the valuative criterion of separatedness*, Theorem 2.1. The remaining elementary ring input is that a finite torsion-free module over a DVR is free.

The general cohomology-and-base-change theorem for proper flat finite-presentation families and perfect complexes is a prerequisite [Stacks, Tag 0B91], as are field Künneth [Stacks, Tag 0BED], flat base change for coherent cohomology [Stacks, Tag 02KH], the elementary Hilbert-polynomial and ampleness results, and miracle flatness [Stacks, Tag 00R4]. The Hilbert-polynomial support-degree statement was also checked in the AI Integrated Stacks Project, Tag 0HDJ. The field-theoretic \(p\)-basis facts used in Section 8 have locators [Stacks, Tags 031W and 07P1–07P2]. Their role and hypotheses are identified at the points of use. Lemmas 3.1–3.4 supply the additional local and global line-bundle arguments rather than importing the theorem of the cube.

The earlier course proofs of smoothness, quasi-projectivity and connected-group structure are used explicitly. Dual abelian varieties, Picard schemes, polarizations and the classification of the nonreduced \(p\)-torsion group schemes are beyond this lesson.

## References

The Stacks Project, read in **AI Integrated Stacks Project**, Groupoid Schemes, Section 0BF9, Tags 03RO, 0BFA–0BFH, 0C0Y, 03RP and 0H2U; More on Morphisms, Tag 0BF4 and the comparison product lemma 0BF3, together with the proper-fibre lemma 0AH8. Cohomology and algebra prerequisites are cited individually above. The AI Integrated Stacks Project is an AI-integrated edition; its additions have not been reviewed by the official Stacks maintainers. The cited material was checked at published revision 565b10e987aba5969b21145a0833f42d69f96790.

J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition dated 5 October 2021, Cambridge University Press, 2022: Chapter 2c for the cubic examples, and Chapter 8e for anti-affine groups and abelian varieties. [Author's edition](https://www.jmilne.org/math/Books/iAG2022.pdf).

# Faithful flatness and the local criterion for flatness

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A flat extension preserves exact sequences. A faithfully flat extension also detects their failure: a relation, a nonzero quotient, or a missing generator cannot disappear after that extension. This makes faithful flatness a tool for descent. The local criterion addresses a different difficulty. A module can be finite over an algebra without being finite over the base ring, yet one Tor group at the closed point can still determine its flatness over that base.

Rings are commutative with identity; local rings have exactly one maximal ideal and need not be Noetherian unless specified. A finite module is finitely generated. We use the ideal criterion, tensor identities, Tor long exact sequences and finite flat module theorems from *Tor and flat modules*. The Noetherian local criteria also use Artin–Rees and Krull intersection from *Noetherian and Artinian rings*, Theorems 5.1 and 6.1, and Nakayama from *Localization, local properties and support*, Theorem 4.2. Every flatness and descent result stated below is proved.

## 1. Detecting nonzero modules

An \(R\)-module \(F\) is **faithfully flat** if tensoring with \(F\) preserves and reflects exactness of complexes. Reflection means that a complex which becomes exact was already exact. In particular, this condition implies flatness. For a flat module and a complex \(C_\bullet\), preservation of kernels and images gives

\[
H_i(C_\bullet\otimes_R F)\simeq H_i(C_\bullet)\otimes_R F.
\tag{1}
\]

Indeed, tensor the sequences defining cycles, boundaries and their quotient; flatness preserves the injections as well as the right exact parts. Thus detection of exactness amounts to detection of zero modules.

**Theorem 1.1.** For a flat \(R\)-module \(F\), the following are equivalent:

1. \(F\) is faithfully flat.
2. \(N\otimes_R F\ne0\) for every nonzero \(R\)-module \(N\).
3. \(\kappa(\mathfrak p)\otimes_R F\ne0\) for every prime \(\mathfrak p\).
4. \(F/\mathfrak mF\ne0\) for every maximal ideal \(\mathfrak m\).

**Proof.** If tensoring reflects exactness, apply it to the complex consisting only of \(N\) in one degree: \(N\otimes F=0\) forces \(N=0\). Conversely, (2) and (1) reflect the vanishing of every homology module, so reflect exactness. The implications (2) to (3) to (4) follow by taking residue fields; for a maximal ideal, \(\kappa(\mathfrak m)=R/\mathfrak m\).

Assume (4), and choose \(0\ne n\in N\). Its cyclic submodule is \(Rn\simeq R/I\) for a proper ideal \(I\). Choose a maximal ideal \(\mathfrak m\supset I\). There is a surjection \(F/IF\to F/\mathfrak mF\), so \(F/IF\ne0\). Flatness preserves \(Rn\subset N\), embedding \(F/IF\) into \(N\otimes F\). Thus (2) holds. \(\square\)

For the zero ring, there are no primes or maximal ideals and no nonzero modules. All four conditions are vacuous, consistently with reflection of exactness in its zero module category.

A useful consequence is that tensoring with a faithfully flat module detects zero maps. For \(u:A\to B\), flatness identifies \(\operatorname{im}(u\otimes F)\) with \(\operatorname{im}(u)\otimes F\). If \(u\otimes F=0\), detection makes \(\operatorname{im}(u)=0\), hence \(u=0\). More generally, flatness preserves kernels and cokernels, and faithful detection shows that injectivity, surjectivity and isomorphisms are reflected.

## 2. Faithfully flat ring maps

A ring map \(R\to S\) is faithfully flat when \(S\) is faithfully flat as an \(R\)-module.

**Theorem 2.1.** A flat ring map \(R\to S\) is faithfully flat if and only if \(\operatorname{Spec}S\to\operatorname{Spec}R\) is surjective. It is enough that every maximal ideal of \(R\) be the contraction of a prime of \(S\). In particular, a flat local homomorphism of local rings is faithfully flat.

**Proof.** Prime ideals of \(S\) contracting to \(\mathfrak p\) correspond to prime ideals of the fibre ring \(S\otimes_R\kappa(\mathfrak p)\), by the localization lesson, Theorem 3.2. That fibre has a prime exactly when it is nonzero: every nonzero ring has a maximal ideal. Theorem 1.1 therefore gives both the all-prime and maximal-ideal tests. For a local map \((R,\mathfrak m)\to(S,\mathfrak n)\), the quotient \(S/\mathfrak mS\) is nonzero because \(\mathfrak mS\subset\mathfrak n\). The maximal-ideal test proves the final assertion, agreeing with Lemma 6.2 of the flat module lesson. \(\square\)

**Theorem 2.2 (injection and contraction).** If \(R\to S\) is faithfully flat, then for every \(R\)-module \(N\) the natural map

\[
N\longrightarrow N\otimes_R S,\qquad n\longmapsto n\otimes1
\tag{2}
\]

is injective. Consequently \(R\to S\) is injective and \(IS\cap R=I\) for every ideal \(I\subset R\).

**Proof.** Tensor (2) once more with \(S\). The resulting map sends \(n\otimes s\) to \(n\otimes1\otimes s\); multiplication of the two \(S\) factors retracts it:

\[
n\otimes s\otimes t\longmapsto n\otimes st.
\]

It is therefore injective. Faithful flatness reflects injectivity, so (2) is injective. Take \(N=R\) for injection of the ring map and \(N=R/I\) for the injective map \(R/I\to S/IS\). Its kernel is the inverse image of \(IS\) modulo \(I\). Identifying \(R\) with its image in \(S\), this says \(IS\cap R=I\). \(\square\)

**Proposition 2.3 (base change and composition).** Faithfully flat maps remain faithfully flat under any base change, and the composite of faithfully flat maps is faithfully flat.

**Proof.** If \(R\to A\) is any map, flatness of \(A\to A\otimes_R S\) follows from flat base change. For a nonzero \(A\)-module \(N\),

\[
N\otimes_A(A\otimes_R S)\simeq N\otimes_R S\ne0,
\]

since its underlying \(R\)-module is nonzero. For composition \(R\to S\to T\), tensor a nonzero \(R\)-module first with \(S\), then with \(T\). Both stages preserve nonzeroness; flatness composes as well. Theorem 1.1 applies. \(\square\)

For a finite list \(f_1,\ldots,f_r\in R\), the map

\[
R\longrightarrow\prod_{i=1}^r R_{f_i}
\tag{3}
\]

is flat because its underlying module is a finite direct sum of flat localizations. Its spectrum maps onto \(\bigcup_iD(f_i)\). To see this, a prime of a finite product chooses exactly one factor: the factor idempotents sum to one and their pairwise products are zero, so exactly one lies outside the prime. Prime correspondence for localization then identifies its image with \(D(f_i)\). Thus (3) is faithfully flat exactly when these opens cover, equivalently when \((f_1,\ldots,f_r)=R\). The empty product convention is harmless for \(R=0\); otherwise an empty list cannot cover its nonempty spectrum.

## 3. Descending finiteness and flatness

There is no Noetherian assumption in this section.

We first record a presentation fact. If \(L\) is finitely presented over a ring \(A\), the kernel of **any** finite free surjection \(A^n\to L\) is finite. Choose one finite presentation \(A^r\to L\) with finite kernel \(K_0\), and form the pullback

\[
P=\{(x,y)\in A^n\oplus A^r:x\text{ and }y\text{ have the same image in }L\}.
\]

Projection to \(A^n\) is surjective with kernel \(K_0\), and splits because \(A^n\) is free. Thus \(P\simeq K_0\oplus A^n\) is finite. Projection to \(A^r\) likewise splits, with kernel equal to the kernel of \(A^n\to L\). This kernel is a direct summand of the finite module \(P\), hence finite. This argument prevents a hidden assumption that submodules of finite modules are always finite.

**Theorem 3.1 (descent).** Let \(R\to S\) be faithfully flat and \(M\) an \(R\)-module. If \(M_S=M\otimes_R S\) is finite, finitely presented or flat over \(S\), respectively, then \(M\) has the corresponding property over \(R\). Each property also ascends to \(M_S\).

**Proof.** Suppose \(M_S\) is finite. Express a finite generating list as finite tensor sums, and collect all the \(M\)-coordinates into a finite list \(m_1,\ldots,m_n\). Let \(M_0\) be their \(R\)-span. The map \(M_0\otimes S\to M\otimes S\) is surjective. Right exactness gives \((M/M_0)\otimes S=0\); faithful detection gives \(M=M_0\).

If \(M_S\) is finitely presented, it is finite, so the first part supplies a surjection \(R^n\to M\) with kernel \(K\). Flatness of \(S\) identifies \(K\otimes S\) with the kernel of \(S^n\to M_S\). The presentation fact makes this kernel finite over \(S\). Apply finite generation descent to \(K\); its finite generators are the finite relation list for a presentation of \(M\).

If \(M_S\) is flat, let \(A\subset B\) be any inclusion of \(R\)-modules. The map obtained by tensoring \(A\otimes_R M\to B\otimes_R M\) with \(S\) identifies with

\[
(A\otimes_R S)\otimes_S M_S
\longrightarrow (B\otimes_R S)\otimes_S M_S.
\]

It is injective, first by flatness of \(S\), then by flatness of \(M_S\). Faithful flatness reflects injectivity, so \(M\) is flat. Ascent of finite generation and finite presentation follows by tensoring their finite generating maps and presentations; ascent of flatness is flat base change. \(\square\)

**Corollary 3.2.** Finite projectivity descends and ascends along faithfully flat ring maps.

**Proof.** A finite projective module is finitely presented and flat, by the flat module lesson. These two properties descend by Theorem 3.1, and together imply finite projectivity by that lesson's Theorem 5.3. For ascent, tensor a decomposition \(R^n=M\oplus K\) to obtain \(S^n=M_S\oplus K_S\). \(\square\)

This does not assert that an arbitrary \(S\)-module comes from an \(R\)-module. We began with \(M\), and descended properties of its known base change. Descent of objects themselves requires additional compatibility data.

## 4. One Tor group at the closed point

Fix a local homomorphism of Noetherian local rings

\[
(R,\mathfrak m,\kappa)\longrightarrow(S,\mathfrak n),
\]

and a finite \(S\)-module \(M\). The distinction between finite over \(S\) and finite over \(R\) is essential.

**Lemma 4.1.** If \(\operatorname{Tor}_1^R(\kappa,M)=0\), then \(\operatorname{Tor}_1^R(L,M)=0\) for every finite-length \(R\)-module \(L\).

**Proof.** Every simple module over a commutative local ring is its residue field: a nonzero cyclic generator of a simple module identifies it with \(R\) modulo a maximal ideal. A composition series of \(L\) therefore has factors \(\kappa\). Induct on its length using the segment

\[
\operatorname{Tor}_1^R(L',M)\longrightarrow
\operatorname{Tor}_1^R(L,M)\longrightarrow
\operatorname{Tor}_1^R(L'',M)
\]

for a short exact sequence reducing that length. Both outer terms vanish. Length zero is immediate. \(\square\)

**Theorem 4.2 (local criterion for flatness).** In the situation above,

\[
M\text{ is flat over }R
\quad\Longleftrightarrow\quad
\operatorname{Tor}_1^R(\kappa,M)=0.
\tag{4}
\]

**Proof.** Flatness implies Tor vanishing by the previous lesson. Assume the right side, and let \(J\subset R\) be an ideal. We will prove \(J\otimes_R M\to M\) injective.

For \(n\geq1\), the modules \(R/\mathfrak m^n\) have finite length: their filtration has factors \(\mathfrak m^i/\mathfrak m^{i+1}\), which are finite-dimensional \(\kappa\)-spaces because \(R\) is Noetherian. Their quotients \(R/(J+\mathfrak m^n)\) also have finite length. Lemma 4.1 and the Tor ideal formula therefore show that both

\[
\mathfrak m^n\otimes_R M\longrightarrow M,
\qquad (J+\mathfrak m^n)\otimes_R M\longrightarrow M
\]

are injective. Now tensor the exact intersection-and-sum sequence

\[
0\longrightarrow J\cap\mathfrak m^n
\xrightarrow{a\mapsto(a,-a)}J\oplus\mathfrak m^n
\xrightarrow{(a,b)\mapsto a+b}J+\mathfrak m^n
\longrightarrow0.
\tag{5}
\]

Let \(z\in J\otimes M\) multiply to zero in \(M\). The image of \((z,0)\) in \((J+\mathfrak m^n)\otimes M\) is zero, since its product is zero and the latter ideal map is injective. Right exactness of the tensored sequence (5) expresses \((z,0)\) as the image of a tensor from \((J\cap\mathfrak m^n)\otimes M\). In particular, \(z\) lies in its image in \(J\otimes M\).

Apply Artin–Rees to \(J\subset R\) with ideal \(\mathfrak m\). There is \(c\) such that

\[
J\cap\mathfrak m^n\subset\mathfrak m^{n-c}J
\qquad(n\geq c).
\]

It follows that \(z\in\mathfrak m^{n-c}(J\otimes_R M)\) for every sufficiently large \(n\). Here \(J\otimes_R M\) is a finite **\(S\)-module**: a finite generating list of \(J\) gives a surjection from a finite direct sum of copies of \(M\). The ideal \(\mathfrak mS\) lies in \(\mathfrak n\). Krull intersection over the Noetherian local ring \(S\) gives

\[
\bigcap_{d\geq0}(\mathfrak mS)^d(J\otimes_R M)=0.
\]

Thus \(z=0\). Every ideal passes the injection test, so \(M\) is flat. \(\square\)

The argument does not require completion or any assertion about its faithful flatness.

**Lemma 4.3 (passing through a quotient).** Let \(R\) be any ring, \(I\) an ideal, and \(M\) any module. If \(M/IM\) is flat over \(R/I\) and \(\operatorname{Tor}_1^R(R/I,M)=0\), then

\[
\operatorname{Tor}_1^R(N,M)=0
\quad\text{whenever some power of }I\text{ annihilates }N,
\]

and \(M/I^dM\) is flat over \(R/I^d\) for every \(d\geq1\).

**Proof.** First let \(IN=0\), and choose \(0\to K\to F\to N\to0\) with \(F\) free over \(R/I\), possibly of infinite rank. Tor commutes with this direct sum: take the direct sum of free \(R\)-resolutions of \(R/I\), then use exactness of direct sums to compute homology. Thus \(\operatorname{Tor}_1^R(F,M)=0\). The Tor sequence embeds \(\operatorname{Tor}_1^R(N,M)\) into the kernel of \(K\otimes_R M\to F\otimes_R M\). Both modules in this map are killed by \(I\) before tensoring, so it identifies with

\[
K\otimes_{R/I}(M/IM)\longrightarrow F\otimes_{R/I}(M/IM).
\]

It is injective by the assumed quotient flatness. This proves the vanishing for \(IN=0\).

If \(I^dN=0\), use \(0\to IN\to N\to N/IN\to0\). Induction and the Tor sequence give vanishing for \(N\), since \(I^{d-1}(IN)=0\). Finally an exact sequence of \(R/I^d\)-modules remains exact after tensoring with \(M\), by this Tor vanishing. Its tensor agrees with tensor over \(R/I^d\) with \(M/I^dM\), proving the final assertion. \(\square\)

**Corollary 4.4 (ideal variant).** For the local Noetherian map and finite \(S\)-module of Theorem 4.2, let \(I\subsetneq R\). Then \(M\) is flat over \(R\) if and only if \(M/IM\) is flat over \(R/I\) and \(\operatorname{Tor}_1^R(R/I,M)=0\).

**Proof.** Necessity follows from base change and the Tor criterion. Conversely, \(I\subset\mathfrak m\), so Lemma 4.3 applies to \(\kappa\), which is killed by \(I\). Theorem 4.2 now proves flatness. \(\square\)

In particular, if \(t\in\mathfrak m\) is a nonzerodivisor of \(R\), the two-term free resolution of \(R/(t)\) identifies its first Tor with the kernel of multiplication by \(t\) on \(M\). Consequently

\[
M\text{ flat over }R
\Longleftrightarrow
\bigl(t:M\to M\text{ injective and }M/tM\text{ flat over }R/(t)\bigr).
\tag{6}
\]

**Proposition 4.5 (all infinitesimal quotients).** Under the same local Noetherian and finiteness hypotheses, for any proper ideal \(I\subset R\), flatness of every \(M/I^dM\) over \(R/I^d\) implies flatness of \(M\).

**Proof.** For an ideal \(J\), its image \(\bar J\) in \(R/I^d\) is \(J/(J\cap I^d)\). Flatness of \(M/I^dM\) makes \(\bar J\otimes_{R/I^d}(M/I^dM)\to M/I^dM\) injective. Since \(\bar J\) is killed by \(I^d\), its source equals \(\bar J\otimes_R M\). A tensor \(z\) in the kernel of \(J\otimes_R M\to M\) therefore maps to zero in \(\bar J\otimes_R M\). Right exactness puts it in the image of \((J\cap I^d)\otimes_R M\). Artin–Rees gives \(J\cap I^d\subset I^{d-c}J\) for large \(d\). Thus \(z\) belongs to every power of \(IS\) acting on the finite \(S\)-module \(J\otimes_R M\). Since \(IS\subset\mathfrak n\), Krull intersection makes \(z=0\). Apply the ideal criterion. \(\square\)

## 5. Lifting a regular equation from the fibre

The residue field alone cannot test flatness of an arbitrary module, as the previous lesson showed. Here Noetherianity and finiteness turn an injective map on the closed fibre into an injective map before reduction.

**Lemma 5.1 (lifting injectivity).** Let \(R\to S\) be a local map of Noetherian local rings, with maximal ideals \(\mathfrak m,\mathfrak n\). Let \(N,P\) be finite \(S\)-modules, \(P\) flat over \(R\), and \(u:N\to P\) an \(S\)-linear map. If \(N/\mathfrak mN\to P/\mathfrak mP\) is injective, then \(u\) is injective and its cokernel is flat over \(R\).

**Proof.** We first prove injectivity modulo \(\mathfrak m^d\) for all \(d\geq1\). The base case is the hypothesis. Suppose it holds for \(d\). Put \(V_d=\mathfrak m^d/\mathfrak m^{d+1}\), a \(\kappa\)-vector space. There is a surjection

\[
V_d\otimes_\kappa(N/\mathfrak mN)
\longrightarrow\mathfrak m^dN/\mathfrak m^{d+1}N,
\tag{7}
\]

obtained by multiplication. For \(P\) the corresponding map is an isomorphism: tensor \(0\to\mathfrak m^{d+1}\to\mathfrak m^d\to V_d\to0\) and use flatness to identify the ideal tensors with their images in \(P\). The map between the left sides of (7) for \(N\) and \(P\) is injective, because tensor over the field preserves the assumed residue injection. It follows that the map between their \(d\)-th layers is injective: lift a layer element to the left side of (7); a zero image forces its lift zero by that injection and the isomorphism for \(P\).

Now an element in the kernel modulo \(\mathfrak m^{d+1}\) reduces to zero modulo \(\mathfrak m^d\) by induction, so belongs to the \(d\)-th layer, where we just proved injectivity. This proves the induction. An element of \(\ker u\) consequently lies in every \(\mathfrak m^dN\). Krull intersection over \(S\), with ideal \(\mathfrak mS\), makes it zero.

Write \(C=\operatorname{coker}u\), finite over \(S\). The Tor sequence of \(0\to N\to P\to C\to0\), using flatness of \(P\), identifies \(\operatorname{Tor}_1^R(\kappa,C)\) with the kernel of the residue injection. It vanishes, so Theorem 4.2 makes \(C\) flat over \(R\). \(\square\)

**Theorem 5.2 (Grothendieck's slicing lemma).** Let \((R,\mathfrak m)\to(S,\mathfrak n)\) be flat and local, with both rings Noetherian. If \(f\in\mathfrak n\) is a nonzerodivisor on \(S/\mathfrak mS\), then \(f\) is a nonzerodivisor on \(S\) and \(S/fS\) is flat over \(R\).

**Proof.** Apply Lemma 5.1 to \(u:S\to S\), multiplication by \(f\). Its residue map is injective by hypothesis, and its target is flat over \(R\). The conclusions give exactly the claimed injection and quotient flatness. \(\square\)

A **regular sequence** \(f_1,\ldots,f_c\) on a ring means that each \(f_i\) acts injectively on the quotient by its predecessors, and the final quotient is nonzero. For elements in the maximal ideal of a local ring, the quotient properness is automatic.

**Corollary 5.3 (successive slicing).** For the map of Theorem 5.2, if \(f_1,\ldots,f_c\in\mathfrak n\) have regular images in \(S/\mathfrak mS\), then they form a regular sequence in \(S\), and every \(S/(f_1,\ldots,f_i)\) is flat over \(R\).

**Proof.** Theorem 5.2 handles the first element. Its quotient is again a Noetherian local ring, flat over \(R\), and its closed fibre is the preceding fibre quotient. Repeat the theorem one element at a time. The elements remain in the maximal ideal of each quotient, so all quotients stay proper. \(\square\)

There is also a comparison between two bases. It is often called the Noetherian fibre criterion [Stacks, Tag 00MP].

**Theorem 5.4 (fibre criterion).** Let \(R\to S\to T\) be local maps of Noetherian local rings, let \(\mathfrak m\) be the maximal ideal of \(R\), and let \(M\ne0\) be a finite \(T\)-module. The following are equivalent:

1. \(M\) is flat over \(R\), and \(M/\mathfrak mM\) is flat over \(S/\mathfrak mS\).
2. \(S\) is flat over \(R\), and \(M\) is flat over \(S\).

**Proof.** Condition (2) implies (1) by composition and base change. Conversely put \(I=\mathfrak mS\). The surjection \(\mathfrak m\otimes_R S\to I\) gives, after tensoring with \(M\) over \(S\), a surjection

\[
\mathfrak m\otimes_R M\longrightarrow I\otimes_S M.
\]

Its composite with multiplication into \(M\) is injective by \(R\)-flatness. A surjective first arrow with injective composite is an isomorphism, and the second arrow is injective. Thus \(\operatorname{Tor}_1^S(S/I,M)=0\). The assumed fibre flatness and Corollary 4.4, applied to \(S\to T\), make \(M\) flat over \(S\).

This \(S\)-module is faithfully flat. If \(\mathfrak n\) and \(\mathfrak l\) are the maximal ideals of \(S\) and \(T\), Nakayama gives \(M/\mathfrak lM\ne0\), since \(M\) is finite over \(T\) and nonzero. It is a quotient of \(M/\mathfrak nM\), so that quotient is nonzero too. Theorem 1.1 applies to the local ring \(S\).

Finally, for an injection \(A\subset B\) of \(R\)-modules, the map \(A\otimes_R S\to B\otimes_R S\), after tensoring over \(S\) with \(M\), becomes \(A\otimes_R M\to B\otimes_R M\). It is injective by \(R\)-flatness of \(M\). Faithful \(S\)-flatness reflects injection, so \(S\) is flat over \(R\). \(\square\)

The nonzero hypothesis matters: \(M=0\) would satisfy (1) over any such maps and could not force \(S\) flat over \(R\).

## 6. Four concrete tests

**An extension that keeps every prime.** The Gaussian integer ring \(\mathbb Z[i]\) has \(\mathbb Z\)-basis \(1,i\). Tensoring a module \(N\) with it gives \(N\oplus N\), so this extension is faithfully flat. In contrast \(\mathbb Z[1/2]\) is flat but kills \(\mathbb Z/2\). Its image in the integer spectrum omits the prime \((2)\).

**Two complementary charts.** For any \(f\in R\), the elements \(f,1-f\) generate the unit ideal. Thus \(R\to R_f\times R_{1-f}\) is faithfully flat by (3). Neither chart individually needs to detect all modules, but together they do. A module or relation cannot vanish on both charts unless it vanishes globally.

**A nodal closed fibre without base torsion.** Set

\[
B=k[t,x,y]/(xy-t),\quad R=k[t]_{(t)},\quad S=B_{(t,x,y)}.
\]

Substitution \(t=xy\) identifies \(B\) with the domain \(k[x,y]\), hence \(S\) with \(k[x,y]_{(x,y)}\). Both local rings are Noetherian. The residue field of \(R\) is \(k\), and its free resolution is \(0\to R\xrightarrow{t}R\to k\to0\). On \(S\), multiplication by \(t=xy\) is injective. Therefore \(\operatorname{Tor}_1^R(k,S)=0\), and Theorem 4.2, with \(S\) finite over itself, proves \(R\)-flatness. The closed fibre is \((k[x,y]/(xy))_{(x,y)}\), with two branches. It may be reducible even though the total algebra is flat.

**A component with torsion.** For \(B=k[t,x]/(tx)\), take the local map \(k[t]_{(t)}\to S=B_{(t,x)}\). The class of \(x\) is nonzero even after this localization: if an element outside \((t,x)\) killed it, reduction modulo \(t\) would give a nonzero polynomial with nonzero constant term killing \(x\) in the domain \(k[x]\). But \(tx=0\). The same two-term resolution therefore gives a nonzero element of \(\operatorname{Tor}_1^{k[t]_{(t)}}(k,S)\). The local criterion rules out flatness.

## 7. Exercises

**Exercise 7.1 (easy: the local case).** Show that a flat local homomorphism of local rings is faithfully flat, without assuming Noetherianity.

**Exercise 7.2 (easy: recovering an ideal).** For a faithfully flat map \(R\to S\), prove \(IS\cap R=I\). Explain why injectivity of the ring map by itself would not suffice, using \(\mathbb Z\to\mathbb Z[1/2]\).

**Exercise 7.3 (medium: a cubic family).** Use the local criterion to prove that \(k[t]\to B=k[t,x,y]/(y^2-x^3-t)\) is flat. Check every localization needed for a global conclusion, not just the point \((t,x,y)\).

**Exercise 7.4 (medium: descending generators and bases).** Let \(R\to S\) be faithfully flat. Prove finite generation descends. If \(M\) is finitely presented over \(R\) and \(M\otimes_R S\) is finite projective over \(S\), prove \(M\) finite projective and explain how local free bases enter the conclusion.

**Exercise 7.5 (hard: regular equations in an ambient fibre).** Let \(R\) be Noetherian, \(P=R[x_1,\ldots,x_n]\), and \(B=P/(f_1,\ldots,f_r)\). Fix \(\mathfrak q\in\operatorname{Spec}B\), with inverse image \(\mathfrak Q\subset P\) and contraction \(\mathfrak p\subset R\). Suppose the images of \(f_1,\ldots,f_r\) form a regular sequence in

\[
(P_{\mathfrak Q})\otimes_{R_{\mathfrak p}}\kappa(\mathfrak p),
\]

the local ring of the **ambient polynomial fibre** at the point determined by \(\mathfrak Q\). Prove \(B_{\mathfrak q}\) flat over \(R_{\mathfrak p}\). The regularity test precedes quotienting by the equations.

**Exercise 7.6 (hard: all finite-order tests).** For a local map of Noetherian local rings \(R\to S\), a finite \(S\)-module \(M\), and a proper ideal \(I\subset R\), prove that \(M/I^dM\) flat over \(R/I^d\) for every \(d\geq1\) forces \(M\) flat over \(R\). Identify where each finiteness and local hypothesis is used.

## 8. Solutions

**Solution 7.1.** Write the map as \((R,\mathfrak m)\to(S,\mathfrak n)\). Locality gives \(\mathfrak mS\subset\mathfrak n\), so \(S/\mathfrak mS\ne0\). Theorem 1.1, applied to the flat \(R\)-module \(S\) and the single maximal ideal of \(R\), gives faithful flatness. Equivalently, a nonzero module has a cyclic submodule \(R/I\), with \(I\subset\mathfrak m\); tensoring embeds the nonzero quotient \(S/IS\) into its tensor. Neither argument uses Noetherianity.

**Solution 7.2.** The map \(R/I\to (R/I)\otimes_R S=S/IS\) is injective by Theorem 2.2. Its kernel is the inverse image of \(IS\) modulo \(I\), so that inverse image is exactly \(I\). For \(I=0\) this gives injection of the ring map, permitting the intersection notation. For the injective flat map \(\mathbb Z\to\mathbb Z[1/2]\), however, the extension of \((2)\) is the whole target ring. Its contraction is \(\mathbb Z\), strictly larger than \((2)\). This map is missing faithfulness.

**Solution 7.3.** Eliminating \(t\) gives \(B\simeq k[x,y]\) with \(t\mapsto y^2-x^3\). The map \(k[t]\to B\) is injective: for a nonzero polynomial \(h(t)\) of degree \(d\), the polynomial \(h(y^2-x^3)\) has \(y\)-degree \(2d\) with nonzero leading coefficient. Thus it is nonzero in the domain \(B\).

For any \(\mathfrak q\in\operatorname{Spec}B\), let \(\mathfrak p\) be its contraction. If \(\mathfrak p=(0)\), the base localization is the field \(k(t)\), over which every module is flat. Otherwise \(\mathfrak p=(h(t))\) for an irreducible polynomial \(h\), since \(k[t]\) is a principal ideal domain. Put \(R=k[t]_{(h)}\), \(S=B_{\mathfrak q}\). This is a local map of Noetherian local rings. A free resolution of \(\kappa(\mathfrak p)\) over \(R\) is \(0\to R\xrightarrow{h}R\to\kappa(\mathfrak p)\to0\). Multiplication by \(h(y^2-x^3)\) is injective on the localized domain \(S\). Therefore its first Tor is zero, and Theorem 4.2 gives flatness of \(S\) over \(R\).

To turn this into a global statement, take any inclusion \(A\subset C\) of \(k[t]\)-modules and the kernel \(K\) of \(A\otimes B\to C\otimes B\). It is a \(B\)-module. At every prime \(\mathfrak q\) of \(B\), the localized map identifies with \(A_{\mathfrak p}\otimes_R S\to C_{\mathfrak p}\otimes_R S\), which is injective by the local flatness just proved. Thus every \(K_{\mathfrak q}=0\). Local detection over \(B\) gives \(K=0\). This proves the original map flat. As an additional check, monic division in \(y\) gives \(B\) basis \(1,y\) over \(k[t,x]\), which is itself free over \(k[t]\).

**Solution 7.4.** Write a finite \(S\)-generating list of \(M\otimes S\) as tensor sums and collect their finitely many \(M\)-entries \(m_i\). If \(M_0=\sum Rm_i\), then \((M/M_0)\otimes S=0\); faithful detection gives \(M=M_0\). This proves finite generation descent without assumptions on either ring.

For the projectivity claim, \(M\otimes S\) is flat, so Theorem 3.1 descends flatness to \(M\). Its given finite presentation and Theorem 5.3 of the flat module lesson make it finite projective. At every prime \(\mathfrak p\), the localized module \(M_{\mathfrak p}\) is finite flat over a local ring, hence finite free by that lesson's Theorem 5.2. Finite presentation, together with the projective splitting construction, gives a free basis on an actual neighborhood \(D(f)\) of each prime, as proved there. Merely asserting free stalks for a finite module would not establish this step: finite flat modules without finite presentation can fail projectivity. One can also remove the given finite-presentation assumption here, since finite projectivity upstairs implies finite presentation upstairs, which descends by Theorem 3.1.

**Solution 7.5.** The map \(R_{\mathfrak p}\to P_{\mathfrak Q}\) is local: its maximal ideal contracts to \(\mathfrak pR_{\mathfrak p}\). It is flat because a polynomial ring is free over its coefficient ring and localization is flat. Both rings are Noetherian by Hilbert basis and localization. Its closed fibre is

\[
P_{\mathfrak Q}/\mathfrak pP_{\mathfrak Q}
\simeq(P_{\mathfrak Q})\otimes_{R_{\mathfrak p}}\kappa(\mathfrak p).
\]

It is a local ring, equivalently the localization of \(\kappa(\mathfrak p)[x_1,\ldots,x_n]\) at the fibre prime determined by \(\mathfrak Q\). Each \(f_i\) belongs to \(\mathfrak Q\), because \(\mathfrak q\) is a prime of their quotient. The assumed regular sequence is therefore in the maximal ideal of this fibre local ring. Corollary 5.3 successively lifts its regularity and proves every quotient of \(P_{\mathfrak Q}\) by an initial list flat over \(R_{\mathfrak p}\). The final quotient is \(B_{\mathfrak q}\), giving the claim. The equations would already be zero in the quotient fibre of \(B\); that is why their regularity must be tested in the ambient polynomial fibre.

**Solution 7.6.** Fix an ideal \(J\subset R\) and a tensor \(z\in\ker(J\otimes_R M\to M)\). For every \(d\), the image \(J/(J\cap I^d)\) is an ideal of \(R/I^d\). The assumed quotient flatness gives its tensor injection into \(M/I^dM\). Since \(z\) maps to zero there, it lies in the image of \((J\cap I^d)\otimes_R M\) in \(J\otimes_R M\), by right exactness. Artin–Rees over the Noetherian ring \(R\) supplies \(c\) with \(J\cap I^d\subset I^{d-c}J\). Hence \(z\) lies in every sufficiently high power of \(IS\) acting on \(J\otimes_R M\).

The ideal \(J\) is finite because \(R\) is Noetherian, and \(M\) is finite over \(S\); consequently \(J\otimes_R M\) is finite over \(S\). Properness of \(I\) in local \(R\) puts it in \(\mathfrak m\), and locality puts \(IS\) in \(\mathfrak n\). Noetherianity of \(S\) now permits Krull intersection for that finite \(S\)-module, giving \(z=0\). The ideal criterion proves flatness. Without the intersection conclusion, passing every finite-order quotient test would not complete the proof.

## What this lesson does not prove

The tensor and Tor formalism and the Noetherian finiteness tools are imported from the prerequisite lessons identified in the introduction. All faithful flatness, descent, local, quotient, slicing and fibre criteria stated here have proofs. Faithful flatness of completion belongs to *Completion* and has not been used here. Descent of modules as objects and geometric globalization belong to later courses.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra. Faithful flatness: [Tag 00HO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-easy-ff), [Tag 00HP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ff), [Tag 00HQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ff-rings), [Tag 00HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-local-flat-ff), [Tag 05CK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-faithfully-flat-universally-injective). Descent: [Tag 03C4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-descend-properties-modules), [Tag 00HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flatness-descends).
- The same work, local criteria: [Tag 00MJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-prepare-local-criterion-flatness), [Tag 00MK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-local-criterion-flatness), [Tag 00ML](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-variant-local-criterion-flatness), [Tag 051C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-what-does-it-mean). Injection and slicing: [Tag 00ME](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-mod-injective), [Tag 00MF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-grothendieck), [Tag 00MG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-grothendieck-regular-sequence), [Tag 00MP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-flatness-fibre-Noetherian). These links use the AI Integrated Stacks Project English reader described in the course introduction.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 24.5, especially 24.5.1–3 and their exercises on faithful flatness; Section 24.6 on local, slicing and fibre criteria. [Author’s public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
- Timothy J. Ford, *Commutative Algebra*, version of 23 September 2026, Chapter 3, Section 5 on faithfully flat modules and algebras, and Chapter 10, Section 4.2 on the local criteria for flatness and on lifting regular sequences from the closed fibre. [Author’s version](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf).

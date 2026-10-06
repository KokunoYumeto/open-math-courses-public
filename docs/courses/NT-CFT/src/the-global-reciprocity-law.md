# The global reciprocity law

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

A local symbol tells how one completion acts on an abelian extension. The global question is whether the symbols at all completions can be assembled into an invariant of an idèle class. Multiplying them defines a map on idèles immediately. It does not immediately define a map on classes: a principal element appears at every place, and its local contributions must cancel.

We first inspect that cancellation in two explicit examples. The proof then has two tasks. Construct a map that is already defined on classes, using the abstract reciprocity theorem and the global cyclic norm axiom. Identify it with the local product by comparing one local norm quotient at a time. The identification proves both the principal product law and the exact global norm kernel.

The abstract theorem is [The reciprocity law and the class field correspondence](the-reciprocity-law-and-the-class-field-correspondence.md), Theorem 5.1. Its arithmetic input here is the cyclic axiom in [The norm index bound and Hasse's norm theorem](the-norm-index-bound-and-hasses-norm-theorem.md), sections 1–8; the later quadratic-form proof is not used. Local symbols and their explicit cyclotomic convention were proved in lessons 6 and 9. Fixed idèle classes and compact norm-one classes were proved in lessons 13 and 14. The data will use integer degree for function fields and a profinite degree for number fields, so the valuation hypothesis must allow both.

## 1. The cancellation that the theorem must explain

Take the principal element \(-6\) in \(\mathbf Q(\zeta_5)/\mathbf Q\). At 2 and 3 its local symbols act on \(\zeta_5\) with exponents 2 and 3. At 5 it is a unit, whose exponent is \((-6)^{-1}\equiv4\pmod5\). At infinity it is negative, whose exponent is \(-1\equiv4\pmod5\). All other finite components are unramified units and act trivially. The total exponent is
\[
2\cdot3\cdot4\cdot4\equiv1\pmod5.
\]
Each ramified or infinite correction matters. Looking only at the prime divisors of 6 would give exponent 1 modulo 5 in this particular case, but it would hide two nontrivial compensating actions. The individual contributions, rather than their coincidental partial product, are what the theorem must organize.

For a function-field example, take \(K=\mathbf F_7(t)\), a constant extension of degree six, and \(a=(t^2+1)/t^2\). Since \(-1\) is not a square in \(\mathbf F_7\), the numerator defines a degree-two place. Its valuation is 1, while the degree-one place \(t\) has valuation \(-2\), and infinity has valuation zero. Their constant-field Frobenius exponents add to \(2\cdot1+1\cdot(-2)=0\). The product is again the identity. Here cancellation is a degree equation rather than an archimedean sign correction.

These examples establish the rule only for cyclotomic or constant extensions, using the explicit local results. For arbitrary abelian extensions the principal product law is still to be proved. In particular, we cannot assume a map on \(C_K\) merely because we have written a finite product on \(J_K\).

## 2. The product on idèles

For a finite abelian extension \(L/K\), choose \(w\mid v\). The local Galois group is the decomposition group \(D_w\subseteq\operatorname{Gal}(L/K)\). Since the latter is abelian, changing \(w\) conjugates this subgroup and its map trivially. Define
\[
[x,L/K]=\prod_v\operatorname{rec}_{L_w/K_v}(x_v),
\qquad x\in J_K.
\tag{1}
\]
At almost all finite places the extension is unramified and \(x_v\) is a unit, so the factor is \(1\). The arithmetic convention sends a uniformizer in an unramified extension to residue-field Frobenius \(z\mapsto z^{Nv}\).

The map is continuous: finitely many local open norm kernels, together with units outside a finite set, give an open subgroup of its kernel. An idèle norm lies in the kernel, because each local factor is a norm from the product of the completions over that place.

**Proposition 16.1.** Suppose \(K\subseteq K'\), \(L\subseteq L'\), and both \(L/K\) and \(L'/K'\) are finite abelian. Then
\[
[N_{K'/K}x,L/K]
=[x,L'/K']|_L.
\tag{2}
\]
The symbols also commute with conjugation and restriction in towers. Each map (1) is surjective.

**Proof.** The \(v\)-component of \(N_{K'/K}x\) is
\(\prod_{v'\mid v}N_{K'_{v'}/K_v}x_{v'}\).
Local norm functoriality, proved in [Local reciprocity and norm groups](local-reciprocity-and-norm-groups.md), identifies its symbol with the product of the restrictions of the \(v'\)-symbols. Multiplication over \(v\) proves (2). Local conjugation and tower compatibility give the other two identities.

The image of (1) contains each decomposition group, since local reciprocity is onto and we may vary just that idèle component. The fixed field of the image therefore splits completely at every place of \(K\). Corollary 14.4 says that a nontrivial finite separable extension has infinitely many places failing complete splitting. The fixed field must be \(K\), so the image is the whole Galois group. \(\square\)

For an infinite abelian extension, define the symbol by these compatible finite quotients. This is equivalently a convergent product of local symbols in the profinite group: in any fixed finite quotient only finitely many factors are nontrivial. At an infinite local extension we use the union of its finite localizations, not an assertion that an algebraic union is complete.

## 3. Principal cyclotomic and constant-field symbols

**Proposition 16.2.** If \(K\) is a number field, \(a\in K^\times\), and \(\zeta\) is a root of unity, then
\[
[a,K(\zeta)/K]=1.
\tag{3}
\]
For a function field, every principal idèle likewise has trivial symbol in every finite constant extension.

**Proof for number fields.** By (2), restriction of the left side to \(\mathbf Q(\zeta)\) equals
\([N_{K/\mathbf Q}a,\mathbf Q(\zeta)/\mathbf Q]\).
Restriction is injective on \(\operatorname{Gal}(K(\zeta)/K)\), so it suffices to work over \(\mathbf Q\). Split the order of \(\zeta\) into prime powers; it suffices to treat order \(\ell^m\).

Write \(a=u_\ell\ell^{v_\ell(a)}\). The explicit local theorem in [Explicit local reciprocity and existence](explicit-local-reciprocity-and-existence.md), Corollary 9.5, gives the exponents acting on \(\zeta_{\ell^m}\):
\[
\begin{array}{c|c}
\text{place}&\text{exponent}\\ \hline
p\ne\ell,\ \ p\text{ finite}&p^{v_p(a)}\\
\ell&u_\ell^{-1}\pmod{\ell^m}\\
\infty&\operatorname{sgn}(a).
\end{array}
\tag{4}
\]
Negative valuations use inverse powers modulo \(\ell^m\). Since
\[
u_\ell=\operatorname{sgn}(a)\prod_{p\ne\ell}p^{v_p(a)},
\]
the product of the exponents in (4) is \(1\) in
\((\mathbf Z/\ell^m)^\times\). This proves (3), including the real sign.

**Proof for function fields.** Let \(k=\mathbf F_q\) be the full constant field of \(K\). In \(K_m=K\mathbf F_{q^m}\), the local extension at \(v\) is unramified, with residue degree \(m/\gcd(m,\deg v)\). Its uniformizer symbol acts on constants as the \(\deg v\)th power of \(q\)-Frobenius. Thus the product symbol of a principal element is Frobenius to the power
\(\sum_v\deg(v)v(a)=0\), by the product formula. \(\square\)

Here \([K_m:K]=m\). Indeed an irreducible finite-field polynomial remains irreducible over \(K\): a monic factor would have coefficients in the algebraic constant field as well as in \(K\), hence in \(k\), contradicting irreducibility. Its roots generate the constant extension. This also shows that the full constant field of \(K_m\) is \(\mathbf F_{q^m}\).

For example, take \(a=-1\), \(L=\mathbf Q(i)\). At \(2\) the inverse unit \(-1\) gives complex conjugation, and at infinity the negative sign gives the same automorphism. Every odd place contributes \(1\). The two conjugations multiply to \(1\).

## 4. Constructing a map on idèle classes

The special cases provide exactly the degree direction needed for a map on classes. The remaining input is the cyclic norm axiom, already proved without global reciprocity. It is useful to view these inputs as a checklist: fixed classes, a procyclic Galois degree, a compatible valuation of norm images, and the two cyclic Tate conditions.

### The module and its fixed classes

Fix a separable closure of a ground global field \(k_0\), and put
\[
A=\varinjlim_{K/k_0\text{ finite separable}}C_K.
\tag{5}
\]
The transition maps are the diagonal embeddings. They are injective by lesson 13. Give \(A\) the discrete topology for its Galois-module structure; every element is defined over a finite extension, so its stabilizer is open. This does not change the ordinary locally compact topology used on each \(C_K\).

One has \(A^{G_K}=C_K\). To check this, represent a fixed element in \(C_M\) with \(M/K\) finite Galois. Invariance in the direct limit is invariance in \(C_M\), by injectivity. The invariant descent \(C_M^{\operatorname{Gal}(M/K)}=C_K\) was proved using Hilbert 90 in lesson 13. The group-theoretic module norm is exactly the idèle-class norm, since both are the product of Galois conjugates. Thus the cyclic class field axiom of Theorem 15.1 is the precise axiom required by the abstract theorem.

What remains is its degree and valuation data.

### Integer degree for function fields

For a function field \(k_0\) with full constants \(\mathbf F_q\), let \(\widetilde{k_0}=k_0\overline{\mathbf F}_q\). Arithmetic constant-field Frobenius supplies
\(d:G_{k_0}\to\widehat{\mathbf Z}\).
For a finite separable \(K/k_0\), \(f_K\) is the degree of its full constant field over \(\mathbf F_q\), and \(d_K\) is Frobenius normalized for those full constants.

The degree map
\[
v_K(c)=\deg_K c=\sum_v[\kappa(v):k_K]v(x_v),
\qquad c=[x]\in C_K,
\tag{8}
\]
is well-defined by the product formula. It is onto \(\mathbf Z\). To prove the last assertion without a point-count estimate, let \(\delta\) be the greatest common divisor of all place degrees. If a prime \(\ell\mid\delta\), every residue field contains the degree-\(\ell\) constant field. The nontrivial constant extension \(K\mathbf F_{|k_K|^\ell}/K\) then splits completely at every place, contrary to Corollary 14.4. Hence \(\delta=1\). Bézout applied to finitely many of the degrees produces an idèle of degree \(1\).

For every finite separable \(L/K\), the local valuation formula for norms gives
\[
\deg_K(N_{L/K}c)=[k_L:k_K]\deg_L(c).
\tag{9}
\]
Indeed the coefficient at \(v\) is the sum of
\([\kappa(v):k_K]f(w/v)v_w(x_w)
=[k_L:k_K][\kappa(w):k_L]v_w(x_w)\).
Here \([k_L:k_K]=f_{L/K}\), the index of the constant-field degree images. Thus the henselian conditions hold with \(V=\mathbf Z\subset\widehat{\mathbf Z}\); surjectivity means onto \(\mathbf Z\), not onto its profinite completion. By Proposition 16.2 the constant-extension symbol is precisely Frobenius to this integer degree.

### Profinite degree for number fields

Take \(k_0=\mathbf Q\). In lesson 1 we proved
\[
\operatorname{Gal}(\mathbf Q(\mu_\infty)/\mathbf Q)
\simeq\widehat{\mathbf Z}^{\,\times}
\simeq\widehat{\mathbf Z}\times T,
\]
where \(T\) is a product of finite torsion factors. The closure of the finite-order elements is \(T\). It matters that we take the closure: the product \(T\) can contain elements of infinite order. Its fixed field \(\widetilde{\mathbf Q}\) has Galois group \(\widehat{\mathbf Z}\). Choose an isomorphism once, obtaining \(d:G_{\mathbf Q}\to\widehat{\mathbf Z}\).

For a number field \(K\), set
\[
f_K=[K\cap\widetilde{\mathbf Q}:\mathbf Q],
\qquad d_K=f_K^{-1}d|_{G_K},
\qquad\widetilde K=K\widetilde{\mathbf Q}.
\]
Proposition 16.2 lets the product symbol in \(\widetilde K/K\) descend to \(C_K\). Define
\[
v_K(c)=d_K[c,\widetilde K/K]\in\widehat{\mathbf Z}.
\tag{6}
\]
Here \(d_K\) denotes its induced isomorphism on that procyclic Galois group.

This map is onto. Proposition 16.1 makes its image onto every finite quotient, hence dense. Split
\(C_K=C_K^1\times\mathbf R_{>0}\)
using a chosen archimedean component. The positive-real factor is divisible and every finite quotient kills it: take an \([L:K]\)th root before applying a finite symbol. The image consequently comes from compact \(C_K^1\), is closed, and is all of \(\widehat{\mathbf Z}\).

For every finite extension \(L/K\), norm functoriality gives
\[
v_K(N_{L/K}c)=f_{L/K}v_L(c),
\qquad
f_{L/K}=[d(G_K):d(G_L)].
\tag{7}
\]
Since \(v_L\) is onto, the norm image under \(v_K\) is exactly \(f_{L/K}\widehat{\mathbf Z}\). The normalization also gives
\(v_K=f_K^{-1}v_{\mathbf Q}N_{K/\mathbf Q}\).
These are exactly the henselian valuation conditions of lesson 4, with value group \(V=\widehat{\mathbf Z}\); an integer-only condition would be inappropriate here.

**Proposition 16.3.** The Galois module (5), the cyclotomic degree and valuation (6) for number fields, or the constant-field degree and valuation (8) for function fields, form a class field theory in the sense of lessons 4–5.

**Proof.** The invariant-module and norm identifications are those just proved for (5). The degree maps are continuous surjections, with normalized images for finite subfields as in lesson 4. The two valuation constructions above prove the henselian norm-image conditions. Both value groups satisfy \(V/nV\simeq\mathbf Z/n\). The cyclic axiom is Theorem 15.1. These verify every input to Theorem 5.1. \(\square\)

## 5. Comparing the maps on local norm quotients

The map on classes supplied by the abstract theorem has the correct norm kernel, but that does not yet identify the action of a single completion. The local product is the map whose completion-by-completion behavior we want. For both maps a local norm dies, so the comparison reduces to a finite quotient. The following proof makes every class of that quotient accessible from an extension on which the comparison is already known.

Apply the abstract theorem. For every finite Galois \(L/K\) it gives
\[
r_{L/K}:\operatorname{Gal}(L/K)^{\mathrm{ab}}
\xrightarrow{\sim}C_K/N_{L/K}C_L.
\tag{10}
\]
Write \(\rho_{L/K}\) for its inverse on \(C_K\). It is continuous because its kernel is the open norm subgroup. Norm, conjugation and tower compatibility are Proposition 5.2.

For finite subextensions of \(\widetilde K/K\), its formula is
\[
\rho_{L/K}(c)=\varphi_{L/K}^{\,v_K(c)\bmod[L:K]}.
\tag{11}
\]
By the definition of \(v_K\), this equals \([c,L/K]\). We must extend the comparison to every abelian extension.

### Making a local quotient accessible from a degree extension

At a finite place of a number field, every cyclotomic \(\mathbf Z_p\)-extension has infinite local degree. If the residue characteristic is \(p\), the \(p\)-power cyclotomic local degrees grow without bound by the totally ramified division fields of lesson 8; adjoining the fixed finite completion cannot bound them. If the residue characteristic is \(\ell\ne p\), the extension is unramified and its Frobenius projects to the \(p\)-adic unit \(\ell^{f_v}\) modulo torsion. This is not torsion, since no positive power of the positive rational integer \(\ell^{f_v}>1\) equals \(1\). Its closed cyclic image in \(\mathbf Z_p\) is therefore a nonzero open subgroup. These observations also apply when \(p=2\), using the finite sign factor.

For function fields the constant \(\mathbf Z_p\)-extension has local degree image \(\deg(v)\mathbf Z_p\), also nonzero and open. Thus in either case there is a \(\mathbf Z_p\)-subextension \(T/K\) of \(\widetilde K/K\) with infinite local degree at the specified finite place.

Suppose now that \(L/K\) is cyclic of \(p\)-power degree, generated by \(\sigma\), and its decomposition group at the specified place is the whole group. Put \(M=LT\), and let \(D\subseteq\operatorname{Gal}(M/K)\) be the decomposition subgroup there. It maps onto \(\operatorname{Gal}(L/K)\), and its image in \(\operatorname{Gal}(T/K)=\mathbf Z_p\) is open. The image of the kernel of \(D\to\operatorname{Gal}(L/K)\) is still open, since that kernel has finite index in \(D\).

Choose \(g\in D\) restricting to \(\sigma\), and adjust it by this kernel so its \(\mathbf Z_p\)-coordinate is a nonzero positive ordinary integer. This is possible because the allowed coordinates form a coset of an open subgroup \(p^b\mathbf Z_p\), and every such coset contains a positive integer. Let \(H=\overline{\langle g\rangle}\), and \(K'=M^H\). The coordinate map on \(H\) is injective, with open image, so \(H\simeq\mathbf Z_p\) and \([K':K]<\infty\). Also \(H\cap\operatorname{Gal}(M/T)=1\), whence
\[
M=K'T,\qquad L'=K'L\subseteq\widetilde{K'}.
\tag{12}
\]
Because \(H\subseteq D\), the chosen place has full decomposition group in \(M/K'\). The finite local group for \(L'/K'\) maps onto \(\operatorname{Gal}(L/K)\), sending the restriction of \(g\) to \(\sigma\). This proves the required auxiliary construction, including its local property.

### Comparing at finite places

For abelian \(L/K\), compose \(K_v^\times\to C_K\) with \(\rho_{L/K}\), and compare it with local reciprocity followed by \(D_v\hookrightarrow\operatorname{Gal}(L/K)\). Both maps kill the local norm group: a local norm gives a global idèle norm supported at that place. They therefore factor through the finite local norm quotient \(D_v\). It suffices to compare on its prime-power elements.

Take such an element \(\sigma\), and replace the base by \(K_0=L^{\langle\sigma\rangle}\). At the chosen place \(L/K_0\) has full cyclic decomposition group \(\langle\sigma\rangle\). Apply the auxiliary construction just proved to get \(L'/K'\) as in (12). Comparison for \(L'/K'\) is already known by (11), because it is cyclotomic or constant. Local reciprocity supplies an element \(a'\) whose local symbol is the lift of \(\sigma\). Norm it down to \(K_{0,v_0}\), then to \(K_v\). Global norm functoriality for \(\rho\) and local norm functoriality give \(\sigma\) on both sides. Since both maps already factor through \(D_v\), this proves their equality. Every element of a finite abelian group is a product of prime-power elements, so the comparison holds on all \(K_v^\times\).

### Comparing at infinite places

Only a real place becoming complex has nontrivial local group. First take the special extension \(F(i)/F\) at a real place of a number field \(F\). Proposition 16.2 makes its product symbol a map on \(C_F\); it kills norms and is onto, since a negative component at that place maps to conjugation. Its norm quotient has order \(2\) by Theorem 15.1. There is just one isomorphism between groups of order \(2\), so this product map is \(\rho_{F(i)/F}\).

For a general complexification, let \(\sigma\) be its conjugation element and pass to \(K_0=L^{\langle\sigma\rangle}\). In \(M=L(i)\), extend \(\sigma\) by the chosen complex conjugation, and let \(K'\) be its fixed field. The chosen completion of \(K'\) is real, and
\[
L'=K'L=M=K'(i).
\]
The equality follows since both \(L\) and \(i\) are moved by that conjugation and \(M/K'\) has degree \(2\). Norm functoriality now reduces the comparison to the special case, exactly as above. At real places staying real and at complex places both maps are trivial because the local norm group is all of \(K_v^\times\).

## 6. Artin reciprocity

**Theorem 16.4 (Artin reciprocity).** For every finite abelian extension \(L/K\) of global fields, the product (1) induces an isomorphism
\[
C_K/N_{L/K}C_L\xrightarrow{\sim}\operatorname{Gal}(L/K).
\tag{13}
\]
In particular
\[
\prod_v\operatorname{rec}_{L_w/K_v}(a)=1
\quad(a\in K^\times),
\tag{14}
\]
and
\[
J_K/(K^\times N_{L/K}J_L)\simeq\operatorname{Gal}(L/K).
\tag{15}
\]

**Proof.** Section 5 identifies the product and \(\rho\) on every idèle supported at one place. Finite products of such idèles are dense in the restricted product: a basic neighborhood restricts only finitely many components, with unit conditions on the tail. Both maps are continuous to a finite group, so they agree everywhere on \(J_K\). The abstract map factors through \(C_K\), proving (14), and has kernel \(NC_L\), proving (13)–(15). \(\square\)

For an unramified finite place, the global symbol of its idèle uniformizer is its arithmetic Frobenius. Thus this theorem includes the usual Frobenius prescription at primes, as well as every ramified and archimedean component. For nonabelian finite Galois extensions (10) remains valid, and the norm group equals that of the maximal abelian subextension by norm limitation in lesson 5.

For an infinite abelian extension the map on \(C_K\) has dense image, because it is onto every finite quotient. Over number fields it is onto: the positive-real factor is killed and the image of compact \(C_K^1\) is closed. Over function fields its constant-field projection is the integer degree subgroup of \(\widehat{\mathbf Z}\), so it is not onto the infinite constant extension. The next lesson describes the precise topology and the existence correspondence.

The construction of the abstract number-field degree involved a choice of an isomorphism with \(\widehat{\mathbf Z}\). The final map is independent of that choice, since the comparison identifies it with the product of the fixed arithmetic local maps.

## 7. Quadratic reciprocity as a product formula

Let \(p,q\) be distinct odd rational primes, and put \(p^*=(-1)^{(p-1)/2}p\). Take \(L=\mathbf Q(\sqrt{p^*})\) and the principal element \(q\). By the explicit Hilbert symbol formulas of [Hilbert symbols and local conics](hilbert-symbols-and-local-conics.md), its local actions on \(\sqrt{p^*}\) are
\[
\begin{array}{c|c}
v&\text{multiplying sign}\\ \hline
q&(p^*/q)\\
p&(q/p)\\
2&1\\
\infty&1.
\end{array}
\tag{16}
\]
At \(q\) the extension is unramified and Frobenius gives the residue square character. At \(p\), the odd-place Hilbert formula has valuations \(0\) and \(1\), giving \((q/p)\). At \(2\), both entries are odd and \(p^*\equiv1\pmod4\), so the odd-unit \(2\)-adic Hilbert formula gives \(1\). At infinity \(q>0\). All other places have an unramified unit symbol.

Theorem 16.4 now gives \((p^*/q)(q/p)=1\). Since
\((-1/q)=(-1)^{(q-1)/2}\), this is
\[
(p/q)(q/p)=(-1)^{(p-1)(q-1)/4}.
\tag{17}
\]
No prior global quadratic reciprocity theorem was used: only the already proved local Hilbert formulas and the global product theorem.

## 8. Exercises and complete solutions

### Exercise 1 — The real sign (easy)

Verify the product formula for \(-1\) in \(\mathbf Q(i)/\mathbf Q\).

**Solution.** At \(2\), Corollary 9.5 acts on \(i\) by the inverse of the unit \(-1\) modulo \(4\), hence sends \(i\) to \(-i\). At infinity, \(-1\) gives complex conjugation. At every odd prime the extension is unramified or split and \(-1\) is a unit, so the symbol is trivial. The product is conjugation squared, hence \(1\). Omitting infinity would give the wrong product.

### Exercise 2 — A fifth root of unity (medium)

Verify the product formula for \(3\) in \(\mathbf Q(\zeta_5)/\mathbf Q\).

**Solution.** At \(3\), arithmetic Frobenius sends \(\zeta_5\) to \(\zeta_5^3\). At \(5\), the unit \(3\) acts through its inverse modulo \(5\), which is \(2\). The positive real component is trivial, and every other finite component is an unramified unit. Composing the two nontrivial actions gives exponent \(3\cdot2=6\equiv1\pmod5\).

### Exercise 3 — The quadratic law (medium)

Derive quadratic reciprocity for distinct odd primes from Theorem 16.4.

**Solution.** Use \(L=\mathbf Q(\sqrt{p^*})\), \(a=q\), and the four local calculations in (16). The product is \(1\), so \((p^*/q)=(q/p)\). Expanding \(p^*=(-1)^{(p-1)/2}p\) and evaluating the finite-field character of \(-1\) gives (17). The special choice \(p^*\equiv1\pmod4\) makes the \(2\)-adic contribution trivial; using \(p\) without that sign adjustment would require retaining it.

### Exercise 4 — Verify the class field theory data (hard)

Prove Proposition 16.3, including its value-group distinction.

**Solution.** Injectivity and invariant descent from lesson 13 identify the discrete union module's \(G_K\)-invariants with \(C_K\), and the coset norm with the idèle norm. Theorem 15.1 supplies both cyclic Tate groups required by the abstract axiom.

For number fields, take the torsion-closure quotient of the cyclotomic Galois group as the degree map. Proposition 16.2 kills principal elements in its product symbol, so (6) is defined on \(C_K\). Proposition 16.1 makes its image dense in \(\widehat{\mathbf Z}\). The divisible positive-real factor maps trivially to every finite quotient, and compact \(C_K^1\) has closed image; the map is onto. Norm compatibility gives precisely \(f_{L/K}\widehat{\mathbf Z}\) as the valuation of the norm image.

For function fields, take constant Frobenius as the degree map, and use integer idèle degree as valuation. If its image had greatest common divisor \(\delta>1\), a prime dividing \(\delta\) would give a nontrivial constant extension split at every place, contradicting lesson 14. Thus the image is \(\mathbf Z\). Local norm valuations yield (9), with \(f_{L/K}\) the full-constant-field degree. Both \(\mathbf Z\) and \(\widehat{\mathbf Z}\) have quotient \(\mathbf Z/n\) by their \(n\)-multiples. These verify all hypotheses; falsely requiring the function-field degree to be onto \(\widehat{\mathbf Z}\), or the number-field valuation to be integer-valued, would not.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The principal cancellation, local comparison and auxiliary procyclic construction are proved here. Number-field cyclotomic degree and function-field constant degree are constructed separately; the permitted profinite valuation image is retained.

- [Jürgen Neukirch, Class Field Theory — The Bonn Lectures, Online Edition 2.0 (May 2015), edited by Alexander Schmidt](https://www.mathi.uni-heidelberg.de/~schmidt/Neukirch-en/Neukirch_cft_02_may15.pdf).
- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.

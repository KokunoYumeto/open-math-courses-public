# Regular sequences, depth and Cohen–Macaulay modules

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. This edition incorporates AI Integrated Stacks Project proofs under GNU FDL 1.2; see the attribution and licence notice below.*

Dimension counts how many equations should be needed to isolate a point. Regularity asks whether each equation acts without killing a nonzero class left by the previous equations. Depth is the number of equations that can be imposed in this stronger way. A Cohen–Macaulay module is one for which depth reaches the dimension of its support. On such a module, the dimension count itself detects regular sequences.

We use Dimension theory of Noetherian local rings for one-equation dimension bounds and Hilbert–Samuel degree, and Associated primes and primary decomposition for associated primes, their localization, and finite prime avoidance. Nakayama, Artin–Rees and Krull intersection retain their earlier hypotheses. The required lesson Resolutions, Tor and Ext, Theorem 1.1 and Section 4, supplies free resolutions, their comparison up to homotopy, and both long exact sequences of Ext; the depth argument using that formalism is proved here.

Rings are commutative with identity. A local ring has one maximal ideal and is nonzero; Noetherianity is always an additional hypothesis. A finite module is finitely generated. Unless a statement says otherwise, depth and Cohen–Macaulay modules below concern finite modules over a Noetherian local ring \((R,\mathfrak m,\kappa)\). Put \(\operatorname{depth}(0)=\infty\) and \(\dim\operatorname{Supp}(0)=-\infty\). We reserve “Cohen–Macaulay module” for a **nonzero** finite module.

## 1. Equations that act injectively

For any ring and module, a list \(f_1,\ldots,f_r\) is **\(M\)-regular** if multiplication by \(f_i\) is injective on \(M/(f_1,\ldots,f_{i-1})M\) for every \(i\), and
\[
M/(f_1,\ldots,f_r)M\ne0.
\tag{1}
\]
The empty list is regular precisely when \(M\ne0\). The condition on the last quotient prevents units from supplying artificial regular sequences.

**Proposition 1.1 (flat extension).** Under a flat map \(R\to S\), a regular sequence retains all its successive injectivity conditions on \(M\otimes_RS\). It is regular there if its last quotient remains nonzero. Under a faithfully flat map, regularity is equivalent before and after extension. Consequently, for a flat local map of Noetherian local rings and a nonzero finite \(M\),
\[
\operatorname{depth}_S(M\otimes_RS)\geq\operatorname{depth}_R(M).
\tag{2}
\]

**Proof.** Tensor each multiplication injection with \(S\). Right exactness identifies its quotient with the corresponding quotient of \(M\otimes_RS\). Faithful flatness detects zero kernels and nonzero quotients, proving both directions. A flat local map is faithfully flat by Lemma 6.2 of *Tor and flat modules*. It sends \(\mathfrak m\) into the target maximal ideal, so every regular sequence used in computing the right side is available for the left side. \(\square\)

**Proposition 1.2 (local permutation).** Every permutation of a regular sequence on a nonzero finite module over a Noetherian local ring is regular.

**Proof.** It suffices to interchange two adjacent entries, after quotienting by the preceding ones. Write these entries as \(x,y\), with \(x\) injective on the resulting module \(N\), and \(y\) injective on \(N/xN\). All entries belong to \(\mathfrak m\): a unit would make the final quotient zero.

Let \(K=\ker(y:N\to N)\). If \(z\in K\), regularity modulo \(x\) gives \(z=xu\). Then \(0=yz=xyu\), so injectivity of \(x\) gives \(u\in K\). Thus \(K=xK\). The kernel is finite, and Nakayama gives \(K=0\). Next suppose \(xz=yu\). Modulo \(xN\), injectivity of \(y\) gives \(u=xv\), and cancellation of \(x\) gives \(z=yv\). Hence \(x\) acts injectively on \(N/yN\). The quotient by both entries is unchanged, as are all later conditions. Adjacent interchanges give any permutation. \(\square\)

The local and finite hypotheses matter. Exercise 8.2 gives a failure in a polynomial ring before localization.

**Proposition 1.3 (powers).** For arbitrary \(R,M\) and positive integers \(e_i\),
\[
f_1,\ldots,f_r\text{ is }M\text{-regular}
\quad\Longleftrightarrow\quad
f_1^{e_1},\ldots,f_r^{e_r}\text{ is }M\text{-regular}.
\tag{3}
\]

**Proof.** First record an elementary fact about \(0\to L\to E\to Q\to0\). If \(a\) is injective on both end modules, it is injective on \(E\). Moreover,
\[
0\longrightarrow L/aL\longrightarrow E/aE\longrightarrow Q/aQ\longrightarrow0
\tag{4}
\]
is exact: if \(ae\in L\), its image satisfies \(a\bar e=0\) in \(Q\), so \(e\in L\). Apply this argument successively to a list of elements. If all successive injections hold on each factor of a finite filtration, they hold on the whole module, and the quotients retain a filtration by the corresponding factor quotients. The last quotient is zero exactly when all its factors are zero.

Suppose \(x\) acts injectively on \(M\). The module \(N_e=M/x^eM\) has a filtration with \(e\) factors isomorphic to \(N_1=M/xM\), given by the powers of \(x\); cancellation verifies the isomorphisms. In particular, \(N_1\) embeds as \(x^{e-1}M/x^eM\).

For a fixed tail \(f_2,\ldots,f_r\), its successive injections on \(N_1\) imply those on \(N_e\) by (4). Conversely, the first injection on \(N_e\) restricts to the embedded \(N_1\). Once the first \(j\) tail entries have been shown to satisfy the injections on \(N_1\), (4) gives a filtration of \(N_e/(f_2,\ldots,f_{j+1})N_e\) whose first factor is an embedded copy of the corresponding quotient of \(N_1\). The next injection restricts to this copy. Induction proves every injection on \(N_1\). After the whole tail, the same filtration proves that the final quotient is nonzero on \(N_e\) exactly when it is nonzero on \(N_1\).

Finally, \(x^e\) is injective exactly when \(x\) is: one direction follows by composition, the other from \(xz=0\Rightarrow x^ez=0\). Thus replacing the first entry by a positive power preserves and reflects regularity. Induct on the length of the tail, over \(M/xM\), to replace all the other entries. This proves (3), including the empty list. \(\square\)

## 2. Depth and its homological measurement

We first bound lengths without assuming any homological characterization.

**Lemma 2.1 (support after one equation).** For nonzero finite \(M\), \(f\in\mathfrak m\), and \(D=\dim\operatorname{Supp}(M)\),
\[
\operatorname{Supp}(M/fM)=\operatorname{Supp}(M)\cap V(f),
\qquad
D-1\leq\dim\operatorname{Supp}(M/fM)\leq D.
\tag{5}
\]
The quotient is nonzero. If \(f\) acts injectively, its support dimension is exactly \(D-1\).

**Proof.** At a prime not containing \(f\), the quotient vanishes. At a prime containing \(f\), Nakayama for the finite localized module says that \((M/fM)_{\mathfrak p}\ne0\) exactly when \(M_{\mathfrak p}\ne0\). This proves the support identity, and Nakayama at \(\mathfrak m\) proves nonzero.

Put \(A=R/\operatorname{Ann}(M)\). Its spectrum is the support of \(M\), so the quotient support is the spectrum of \(A/(\bar f)\). Theorem 3.2 of *Dimension theory of Noetherian local rings* gives (5), and equality when \(\bar f\) avoids every minimal prime of \(A\). If \(f\) is injective, it avoids every associated prime of \(M\), hence every minimal point of its support, by Theorems 1.2 and 3.2 of *Associated primes and primary decomposition*. \(\square\)

Each entry of a regular sequence in \(\mathfrak m\) therefore lowers support dimension by one. Its length is at most \(D\). Define **depth** as the maximum of these lengths. The maximum exists, and any regular sequence can be extended until it is maximal: each extension increases a bounded nonnegative length. “Maximal” here means that no further element of \(\mathfrak m\) can be appended; we will prove that every such list has maximum length.

Recall the precise homological formalism. For a free resolution \(F_\bullet\to\kappa\),
\[
\operatorname{Ext}^i_R(\kappa,M)
=H^i\bigl(\operatorname{Hom}_R(F_\bullet,M)\bigr).
\tag{6}
\]
Resolution comparison makes this independent of the resolution, naturally in both arguments. A short exact sequence in the second argument gives a long exact sequence, since each \(F_i\) is free and the resulting Hom complexes form a short exact sequence. These are the resolution facts used below.

Every \(x\in\mathfrak m\) kills the groups in (6). To see this directly, multiplication by \(x\) on \(F_\bullet\) lifts the zero endomorphism of \(\kappa\), so resolution comparison makes it homotopic to zero. Precomposition with that chain map is multiplication by \(x\) on the Hom complex, since the ring is commutative. It consequently acts as zero on cohomology.

**Lemma 2.2.** The following are equivalent:
\[
\operatorname{depth}(M)=0,
\qquad \mathfrak m\in\operatorname{Ass}(M),
\qquad \operatorname{Hom}_R(\kappa,M)\ne0.
\tag{7}
\]

**Proof.** If every element of \(\mathfrak m\) is a zero divisor, the associated-prime union and finite prime avoidance put \(\mathfrak m\) inside an associated prime. That prime must be \(\mathfrak m\). Conversely, an associated element killed by \(\mathfrak m\) makes every element of \(\mathfrak m\) a zero divisor. Such a nonzero element is exactly a nonzero homomorphism \(\kappa\to M\). Nakayama ensures that every injective element in \(\mathfrak m\) would be a regular sequence of length one, so these alternatives are exactly depth zero. \(\square\)

**Theorem 2.3 (Ext and maximal sequences).** For nonzero finite \(M\),
\[
\boxed{\operatorname{depth}_R(M)
=\min\{i\geq0:\operatorname{Ext}^i_R(\kappa,M)\ne0\}.}
\tag{8}
\]
This minimum is finite. Every maximal \(M\)-regular sequence in \(\mathfrak m\) has this length. For every injective \(x\in\mathfrak m\),
\[
\operatorname{depth}(M/xM)=\operatorname{depth}(M)-1.
\tag{9}
\]

**Proof.** Let \(e(M)\) denote the minimum in (8), provisionally allowing infinity. If there is no injective element in \(\mathfrak m\), Lemma 2.2 gives \(e(M)=0\).

Otherwise choose any injective \(x\in\mathfrak m\), and set \(N=M/xM\). The long exact sequence of \(0\to M\xrightarrow{x}M\to N\to0\), with its multiplication maps zero, gives for every \(i\geq0\)
\[
0\longrightarrow\operatorname{Ext}^i_R(\kappa,M)
\longrightarrow\operatorname{Ext}^i_R(\kappa,N)
\longrightarrow\operatorname{Ext}^{i+1}_R(\kappa,M)
\longrightarrow0.
\tag{10}
\]
Also \(\operatorname{Hom}_R(\kappa,M)=0\), by injectivity of \(x\). Induct on support dimension, which drops by one in Lemma 2.1. The induction hypothesis gives a finite \(s=e(N)\). For \(i<s\), (10) forces both adjacent Ext groups of \(M\) to vanish. At \(i=s\), the left group vanishes and the middle group does not, so \(\operatorname{Ext}^{s+1}_R(\kappa,M)\ne0\). For \(s=0\), the same conclusion uses the already proved Hom vanishing. Thus
\[
e(M)=e(N)+1<\infty
\tag{11}
\]
for every injective choice of \(x\). Dimension zero starts the induction because an injective element would give a nonzero quotient of dimension \(-1\), impossible.

Now take any maximal regular list of length \(r\). Repeated use of (11) gives \(e(M)=r+e(M/(f_1,\ldots,f_r)M)\). The terminal quotient admits no injective element of \(\mathfrak m\), so its \(e\) is zero by Lemma 2.2. Hence every maximal list has length \(e(M)\). Every list extends to one, so its maximum length is \(e(M)\). This proves (8), the assertion about maximal lists, and (9). \(\square\)

**Proposition 2.4 (depth lemma).** If \(0\to A\to B\to C\to0\) is an exact sequence of finite modules over \(R\), then
\[
\begin{aligned}
\operatorname{depth}B&\geq\min(\operatorname{depth}A,\operatorname{depth}C),\\
\operatorname{depth}A&\geq\min(\operatorname{depth}B,\operatorname{depth}C+1),\\
\operatorname{depth}C&\geq\min(\operatorname{depth}A-1,\operatorname{depth}B).
\end{aligned}
\tag{12}
\]
Use the usual extended-integer conventions for infinity.

**Proof.** The long exact sequence contains
\[
\operatorname{Ext}^i(\kappa,A)\to\operatorname{Ext}^i(\kappa,B)
\to\operatorname{Ext}^i(\kappa,C)\to\operatorname{Ext}^{i+1}(\kappa,A).
\]
For the first inequality, both outside groups vanish below the indicated minimum. For the second, use the segment from \(\operatorname{Ext}^{i-1}(\kappa,C)\) through \(\operatorname{Ext}^i(\kappa,A)\) to \(\operatorname{Ext}^i(\kappa,B)\); at \(i=0\) the absent negative group is zero. For the third, use the displayed segment around \(\operatorname{Ext}^i(\kappa,C)\). Theorem 2.3 converts these vanishings into (12). If a module is zero, all its Ext groups vanish and the same reasoning applies. \(\square\)

If an ideal \(J\) kills \(M\), its depth over \(R\) equals its depth over the local quotient \(R/J\): lists in the quotient lift to \(\mathfrak m\), and every multiplication and quotient on \(M\) is the same. This is a statement about regular sequences, and requires no identification of Ext groups over the two different rings.

## 3. Depth is bounded at every associated point

The elementary bound from Lemma 2.1 is \(\operatorname{depth}M\leq\dim\operatorname{Supp}M\). The stronger statement below bounds depth by the dimension of **each** associated component, including embedded ones.

**Theorem 3.1.** For every \(\mathfrak p\in\operatorname{Ass}(M)\),
\[
\operatorname{depth}M\leq\dim(R/\mathfrak p)
\leq\dim\operatorname{Supp}M.
\tag{13}
\]

**Proof.** Induct on depth. At depth zero, the first inequality follows from nonnegative dimension. In positive depth choose an injective \(x\in\mathfrak m\). Then \(x\notin\mathfrak p\). In the local domain \(R/\mathfrak p\), the one-equation theorem gives
\[
\dim R/(\mathfrak p+(x))=\dim(R/\mathfrak p)-1.
\tag{14}
\]
Its finitely many minimal primes cover its spectrum by their closed sets. The finite closed-cover dimension formula, proved in Section 1 of *Krull dimension and Noether normalization*, supplies a prime \(\mathfrak q\) minimal over \(\mathfrak p+(x)\) such that \(\dim R/\mathfrak q\) equals the right side of (14).

An associated element embeds \(N\cong R/\mathfrak p\) in \(M\). Artin–Rees for \((x)\), Theorem 5.1 of *Noetherian and Artinian rings*, gives some \(n\geq1\) with
\[
N\cap x^nM\subset xN.
\tag{15}
\]
Indeed, for \(n\geq c+1\), its formula makes that intersection \(x^{n-c}(N\cap x^cM)\subset xN\). The image
\[
L=N/(N\cap x^nM)\subset M/x^nM
\]
surjects onto \(N/xN\). Thus \(\mathfrak q\in\operatorname{Supp}L\). Its annihilator contains \(\mathfrak p\) and \(x^n\), so every prime in \(\operatorname{Supp}L\) contains \(\mathfrak p+(x)\). Minimality of \(\mathfrak q\) over that ideal makes it a minimal point of \(\operatorname{Supp}L\), hence an associated prime of \(L\). The submodule inclusion makes it associated to \(M/x^nM\), by Proposition 2.1 of *Associated primes and primary decomposition*.

Multiplication by \(x^n\) is injective, so Theorem 2.3 gives depth \(\operatorname{depth}M-1\) to this quotient. Induction applied at \(\mathfrak q\) yields
\[
\operatorname{depth}M-1\leq\dim R/\mathfrak q
=\dim R/\mathfrak p-1.
\]
This is the first inequality in (13). The second follows from \(V(\mathfrak p)\subset\operatorname{Supp}M\). \(\square\)

The use of \(x^n\), rather than an unjustified assertion about \(x\) itself, lets the embedded copy of \(R/\mathfrak p\) survive with the associated point needed for induction.

## 4. When dimension detects regularity

A nonzero finite module is **Cohen–Macaulay**, abbreviated CM, when
\[
\operatorname{depth}M=\dim\operatorname{Supp}M.
\tag{16}
\]
A **maximal Cohen–Macaulay module** instead has depth \(\dim R\). Theorem 3.1 shows that this implies (16), but a CM module can have smaller support than \(\operatorname{Spec}R\).

**Theorem 4.1 (associated components).** If \(M\) is CM of support dimension \(D\), then
\[
\operatorname{Ass}(M)=\min\operatorname{Supp}(M),
\qquad \dim R/\mathfrak p=D
\quad(\mathfrak p\in\operatorname{Ass}(M)).
\tag{17}
\]
In particular there are no embedded associated primes, and every irreducible component of its support has dimension \(D\).

**Proof.** Theorem 3.1 places \(\dim R/\mathfrak p\) between \(\operatorname{depth}M=D\) and \(D\), giving equality. Suppose an associated \(\mathfrak p\) were not minimal in the support. Choose a minimal support prime \(\mathfrak q\subsetneq\mathfrak p\), which is itself associated. A chain in \(R/\mathfrak p\) of length \(D\) exists because its dimension is the finite integer \(D\). Prepending \(\mathfrak q\) gives a chain in \(R/\mathfrak q\) of length \(D+1\), contradicting its dimension \(D\). Every minimal support prime is associated by the earlier associated-prime theorem, proving (17). \(\square\)

**Theorem 4.2 (the expected dimension criterion).** Let \(M\) be CM of support dimension \(D\). If \(g_1,\ldots,g_c\in\mathfrak m\) satisfy
\[
\dim\operatorname{Supp}\bigl(M/(g_1,\ldots,g_c)M\bigr)=D-c,
\tag{18}
\]
then this list is \(M\)-regular, and its quotient is CM of dimension and depth \(D-c\).

**Proof.** First take one element \(g\) that lowers support dimension from \(D\) to \(D-1\). If it were a zero divisor, it would belong to some \(\mathfrak p\in\operatorname{Ass}M\). The support identity (5) would then put all of \(V(\mathfrak p)\), of dimension \(D\) by (17), inside the quotient support. This contradicts the asserted drop. Thus \(g\) is injective. Theorem 2.3 and Lemma 2.1 lower depth and dimension by one, so \(M/gM\) is CM.

For the given list, Nakayama keeps every intermediate quotient nonzero. At each step (5) says that dimension decreases by at most one and never increases. The total decrease \(c\) in (18) forces a decrease of exactly one at each of the \(c\) steps. Apply the one-element argument successively. \(\square\)

A **system of parameters for \(M\)** is a list of \(D=\dim\operatorname{Supp}M\) elements of \(\mathfrak m\) whose quotient has finite length. Such lists exist: choose parameters in \(R/\operatorname{Ann}M\) by Theorem 2.1 of *Dimension theory of Noetherian local rings* and lift them. Their quotient support is just the closed point. A finite module supported there has finite length, since a power of \(\mathfrak m\) kills it and its successive maximal-ideal layers are finite-dimensional \(\kappa\)-spaces. Conversely, finite length gives support only at that point.

**Corollary 4.3 (parameters).** Every system of parameters of a CM module is regular. Conversely, if a module has a regular system of parameters, it is CM. Every regular sequence on a CM module extends to a regular system of parameters.

**Proof.** A nonzero finite-length quotient has support dimension zero, so Theorem 4.2 applies to a system of \(D\) parameters. Conversely, such a regular list gives depth at least \(D\), and (13) gives the reverse bound. For extension, each regular quotient is CM by (9) and the exact dimension drop in Lemma 2.1. Choose a system of parameters of the final quotient and lift it; the resulting concatenation is regular and has total length \(D\). \(\square\)

The parameters here belong to the **module's support**. For \(R=k[x,y]_{(x,y)}\) and \(M=R/(x)\), the module is CM of dimension one: \(y\) acts injectively and its quotient is \(k\). Although \(x,y\) are ring parameters, \(x\) acts as zero on \(M\). Ring parameters cannot replace module parameters in Corollary 4.3 without an additional maximal-CM hypothesis.

## 5. Localization and Cohen–Macaulay rings

**Theorem 5.1 (module localization).** If \(M\) is CM and \(\mathfrak p\in\operatorname{Supp}M\), then the nonzero finite \(R_{\mathfrak p}\)-module \(M_{\mathfrak p}\) is CM.

**Proof.** Put \(h=\dim\operatorname{Supp}_{R_{\mathfrak p}}M_{\mathfrak p}\). We construct an \(M\)-regular list inside \(\mathfrak p\) of length \(h\). Suppose \(r<h\) elements have been constructed, and let \(N\) be their global quotient. The depth and dimension drops show that \(N\) is CM. Its localization at \(\mathfrak p\) is nonzero by repeated Nakayama, since each chosen element belongs to \(\mathfrak pR_{\mathfrak p}\). Flat localization preserves the successive injections, and Lemma 2.1 applied locally gives
\[
\dim\operatorname{Supp}(N_{\mathfrak p})=h-r>0.
\tag{19}
\]

The ideal \(\mathfrak p\) cannot be contained in an associated prime \(\mathfrak q\) of \(N\). Indeed, \(\mathfrak p\) is in its support, while \(\mathfrak q\) is minimal in that support by (17). Such a containment would force \(\mathfrak p=\mathfrak q\), making the localized support have just its closed point and dimension zero, contrary to (19). Finite prime avoidance therefore selects an element of \(\mathfrak p\) outside all associated primes of \(N\). It is injective on \(N\) and supplies the next entry. The quotient is again CM and stays nonzero locally.

After \(h\) steps we have a regular sequence of length \(h\) on \(M_{\mathfrak p}\). The local depth bound (13) makes its depth exactly \(h\), as required. For \(h=0\), that bound directly gives depth zero. \(\square\)

A Noetherian local ring is **Cohen–Macaulay** when it is CM as a module over itself. A general Noetherian ring is CM when every prime localization is a CM local ring; the zero ring satisfies this condition vacuously.

**Corollary 5.2.** Every prime localization of a CM local ring is CM. A CM local ring is equidimensional: all its minimal-prime quotients have dimension \(\dim R\). Its associated primes are exactly its minimal primes.

**Proof.** Apply Theorem 5.1 and (17) to \(M=R\). Every prime belongs to the support of \(R\). \(\square\)

One sometimes describes (17) as **unmixedness** of the module, meaning equal dimensions of its associated-prime quotients. This statement does not assert equal heights of those primes in an arbitrary ambient ring, nor does it assert a property of a completion. The precise quotient dimensions in (17) are what the proof gives.

**Theorem 5.3 (polynomial permanence).** If \(R\) is a Noetherian CM ring, then \(R[T_1,\ldots,T_n]\) is Noetherian and CM for every finite \(n\).

**Proof.** Hilbert basis gives Noetherianity. It suffices to add one variable and check an arbitrary prime \(\mathfrak q\subset R[T]\). Put \(\mathfrak p=\mathfrak q\cap R\), \(A=R_{\mathfrak p}\), \(B=R[T]_{\mathfrak q}\), and \(d=\dim A\). Choose a regular system of parameters \(f_1,\ldots,f_d\) of \(A\). The flat local map \(A\to B\) preserves its regularity, by Proposition 1.1. The ring \(A_0=A/(f_1,\ldots,f_d)\) is Artinian local, so its maximal ideal \(\mathfrak p_0\) is nilpotent. The resulting local quotient of \(B\) is a localization of \(A_0[T]\). Modulo \(\mathfrak p_0\) it is either \(\kappa(\mathfrak p)(T)\), or \(\kappa(\mathfrak p)[T]_{(F)}\) for a monic irreducible polynomial \(F\).

In the first case that quotient has dimension zero: every prime contains the nilpotent ideal, and its reduction is a field. Thus the parameter ideal generated by the \(f_i\)'s is primary to the maximal ideal of \(B\). The height theorem gives \(\dim B\le d\), while the regular sequence and the depth bound give \(d\le\operatorname{depth}B\le\dim B\). Equality proves that \(B\) is CM.

In the second case lift the coefficients of \(F\) to \(A\) to obtain a monic polynomial \(f\) lying in the maximal ideal of \(B\). Multiplication by \(f\) on \(A_0[T]\) is injective: the leading coefficient of a nonzero polynomial vector remains its nonzero leading coefficient after multiplication by a monic polynomial. Localization preserves this injection. Its quotient is a localization of the finite \(A_0\)-module \(A_0[T]/(f)\), hence has dimension zero; it is nonzero by local Nakayama. Therefore \(f_1,\ldots,f_d,f\) is a regular system of parameters of \(B\). The same height and depth bounds give dimension and depth \(d+1\). These two cases cover every prime, including the generic point of a polynomial fibre. Induction proves the finite-variable assertion. \(\square\)

**Lemma 5.4 (dimension formula in a CM local ring).** For every prime \(\mathfrak p\) of a CM local ring \(A\),
\[
\dim A=\dim A_{\mathfrak p}+\dim A/\mathfrak p.
\tag{19a}
\]

**Proof.** Write \(h=\dim A_{\mathfrak p}\), \(d=\dim A\). The construction in the proof of Theorem 5.1, applied to the module \(A\), produces an \(A\)-regular sequence of length \(h\) inside \(\mathfrak p\). Its quotient \(C\) is CM of dimension \(d-h\), by the exact regular dimension drop. Localizing \(C\) at \(\mathfrak p\) has dimension zero: the localized sequence is regular of length \(h\) on the CM local ring \(A_{\mathfrak p}\). Thus \(\mathfrak p\) is minimal over this sequence; a strictly smaller prime over it would give a positive-length chain in that localization. The associated-component theorem 4.1 now says that the quotient of \(C\) by this minimal prime has dimension \(d-h\). That quotient is exactly \(A/\mathfrak p\), proving (19a). \(\square\)

**Theorem 5.5 (universal catenarity).** A Noetherian CM ring is universally catenary: every finite-type algebra over it is catenary.

**Proof.** First let \(R\) be CM and let \(\mathfrak p\subsetneq\mathfrak q\) be a saturated pair of primes. In \(A=R_{\mathfrak q}\), the quotient \(A/\mathfrak pA\) has dimension one: its only primes are its zero prime and maximal ideal, by saturation. Lemma 5.4 gives
\[
\dim R_{\mathfrak q}-\dim R_{\mathfrak p}=1.
\]
Every chain in a fixed prime interval is finite and can be extended to a saturated one, since it is bounded by the finite dimension of the upper prime's Noetherian local ring. Adding these differences along any saturated chain gives the common length \(\dim R_{\mathfrak q}-\dim R_{\mathfrak p}\). Hence \(R\) is catenary.

Theorem 5.3 makes every finite-variable polynomial ring over \(R\) CM, hence catenary by the preceding argument. Every finite-type algebra is a quotient of one of these polynomial rings. Prime intervals in a quotient are exactly the corresponding prime intervals in the original ring above the quotient ideal, with the same intermediate primes and saturated chains. Catenarity therefore passes to quotients. This proves universal catenarity. It does not assert that an arbitrary quotient is CM. \(\square\)

## 6. Regular local rings and complete intersections

Recall that a Noetherian local ring \((A,\mathfrak n,\kappa)\) is **regular** if
\[
D=\dim A=\dim_\kappa\mathfrak n/\mathfrak n^2.
\tag{20}
\]
We prove the foundation needed for the hypersurface examples now; the later lesson *Regular local rings* will develop its further consequences.

**Theorem 6.1.** A regular local ring is a domain and is Cohen–Macaulay. Any minimal list of generators of its maximal ideal is a regular sequence.

**Proof.** If \(D=0\), Nakayama gives \(\mathfrak n=0\), so \(A\) is a field and all assertions hold. Suppose \(D\geq1\), and choose minimal generators \(x_1,\ldots,x_D\). They induce a graded surjection
\[
P=\kappa[T_1,\ldots,T_D]\longrightarrow
\operatorname{gr}_{\mathfrak n}(A).
\tag{21}
\]
Every degree is generated by products of the degree-one classes, because powers of \(\mathfrak n\) are generated by the corresponding products of the \(x_i\).

If the kernel contained a nonzero homogeneous \(F\) of degree \(a\geq1\), each graded dimension on the right would be bounded by that of \(P/(F)\). Multiplication by \(F\) is injective on the polynomial ring, so for large \(n\)
\[
\begin{aligned}
\ell_A(A/\mathfrak n^n)
&\leq\sum_{j=0}^{n-1}\dim_\kappa(P/(F))_j\\
&=\binom{n+D-1}{D}-\binom{n-a+D-1}{D}.
\end{aligned}
\tag{22}
\]
The polynomial on the last line has degree at most \(D-1\). But Corollary 2.2 of *Dimension theory of Noetherian local rings* identifies the Hilbert–Samuel degree of \(A\) with \(D\), and its leading coefficient is positive. Inequality (22) is impossible for large \(n\). Thus (21) is an isomorphism.

Krull intersection, Theorem 6.1 of *Noetherian and Artinian rings* with the ideal \(\mathfrak n\), says that every nonzero element of \(A\) has a finite order: the unique \(v\geq0\) for which it lies in \(\mathfrak n^v\setminus\mathfrak n^{v+1}\). The initial forms of two nonzero elements have nonzero product in the polynomial graded ring. Their product therefore has order the sum of their orders and is nonzero. Hence \(A\) is a domain, and \(x_1\) acts injectively.

Order additivity gives, for \(n\geq1\),
\[
(x_1)\cap\mathfrak n^n=x_1\mathfrak n^{n-1}.
\tag{23}
\]
It also identifies the kernel of the natural map from \(\operatorname{gr}_{\mathfrak n}A\) to the associated graded ring of \(A/(x_1)\). In degree \(n\), a kernel representative in \(\mathfrak n^n\cap((x_1)+\mathfrak n^{n+1})\) differs by an element of \(\mathfrak n^{n+1}\) from something in \((x_1)\cap\mathfrak n^n\). Formula (23) makes its initial form a multiple of \(T_1\). The converse is immediate, and degree zero has no kernel. Therefore
\[
\operatorname{gr}\bigl(A/(x_1)\bigr)
\cong\kappa[T_2,\ldots,T_D].
\tag{24}
\]
This local quotient is Noetherian and Krull-separated. The same initial-form argument makes it a domain and its next generator injective; (23) then proves the next quotient graded ring is the polynomial ring on the remaining variables. Repeating shows that \(x_1,\ldots,x_D\) is regular. Its final quotient is \(\kappa\ne0\). Thus depth is at least \(D\), and (13) makes it exactly \(D\). \(\square\)

**Corollary 6.2 (hypersurfaces and intersections).** If \(A\) is regular local and \(0\ne f\in\mathfrak n\), then \(A/(f)\) is CM of dimension \(D-1\). More generally, a quotient by an \(A\)-regular list of length \(c\) is CM of dimension \(D-c\). A list in \(\mathfrak n\) whose quotient has dimension \(D-c\) is itself regular and gives a CM quotient.

**Proof.** Theorem 6.1 gives both the CM property of \(A\) and injectivity of a nonzero \(f\). Equations (5) and (9) lower dimension and depth by one. Apply this repeatedly to a regular list, or apply Theorem 4.2 to the stated dimension condition. Depth of each quotient as a module agrees with depth over its own local ring. \(\square\)

Here a complete intersection means a quotient by a regular sequence. The dimension criterion supplies the regularity when only a list with the expected dimension is initially given. The conditions on a hypersurface equation are substantive: \(f=0\) gives the ambient ring, and a unit gives the zero quotient, which is excluded from our local CM-module convention.

## 7. Three ways depth can fall short

**A line with an embedded point.** In
\[
B=\bigl(k[x,y]/(x^2,xy)\bigr)_{(x,y)},
\]
the nilpotent \(x\) lies in every prime, so the spectrum has the dimension-one support of the \(y\)-line. The element \(x\) remains nonzero after localization: a denominator with nonzero constant term multiplies it by that constant. Both generators of the maximal ideal kill it. Thus the maximal ideal is associated, and (7) gives depth zero. An embedded point obstructs the first regular equation.

**Two planes meeting only at the origin.** Put
\[
P=k[x,y,z,w]_{(x,y,z,w)},\quad I=(x,y),\quad J=(z,w),
\qquad B=P/(I\cap J).
\tag{25}
\]
Its spectrum is the union of the two closed planes, so \(\dim B=2\). The intersection sequence is
\[
0\longrightarrow B\longrightarrow P/I\oplus P/J
\xrightarrow{\ (u,v)\mapsto u-v\ }\kappa\longrightarrow0.
\tag{26}
\]
The last map uses the residues modulo \(I+J\). Its kernel is the diagonal image of \(P/(I\cap J)\): lifts with equal residue can be adjusted by elements of \(I\) and \(J\) to a common lift. It is surjective, so (26) is exact.

On the middle module, \(x+z,y+w\) acts as the two coordinate variables on each plane. This is a regular list of length two, with final quotient \(\kappa\oplus\kappa\). The support dimension bound makes its depth exactly two. Its Hom and first Ext from \(\kappa\) therefore vanish. The long exact sequence of (26) gives
\[
\operatorname{Hom}_P(\kappa,B)=0,
\qquad\operatorname{Ext}^1_P(\kappa,B)\cong
\operatorname{Hom}_P(\kappa,\kappa)\cong\kappa.
\tag{27}
\]
Thus \(\operatorname{depth}B=1<2\), using quotient-ring invariance of depth. The ring is reduced because \(I\) and \(J\) are prime and their intersection is radical. It has no embedded primes by Solution 8.4 of *Associated primes and primary decomposition*, and its components have equal dimension. Those properties alone do not imply CM.

**A domain with a defective parameter pair.** Let
\[
S=k[s^4,s^3t,st^3,t^4]\subset k[s,t],\qquad
R=S_{\mathfrak m},\quad
\mathfrak m=(s^4,s^3t,st^3,t^4).
\tag{28}
\]
It is a domain. Write \(a=s^4\), \(b=t^4\). The other two generators are integral over \(k[a,b]\), since their fourth powers are \(a^3b\) and \(ab^3\). The fraction field has transcendence degree two, and \(S/\mathfrak m=k\). The height formula in Theorem 4.3 of *Krull dimension and Noether normalization* gives \(\dim R=2\). Modulo \((a,b)\), both remaining generators are nilpotent, so this pair is a system of parameters.

Set \(u=(s^3t)^2=s^6t^2\). It is not in \(aR\), but
\[
bu=a(st^3)^2\in aR.
\tag{29}
\]
The localization nonmembership is established in Solution 8.6 below, by comparing homogeneous degrees. Therefore \(b\) kills a nonzero class modulo \(a\). The parameter pair is not regular, so Corollary 4.3 shows that \(R\) is not CM. Since the domain has the injective element \(a\in\mathfrak m\), its depth is at least one; being non-CM of dimension two, its depth is exactly one. A domain can therefore fail CM without any embedded associated prime.

## 8. Exercises

**Exercise 8.1 (easy).** For a nonzero finite module over a Noetherian local ring, prove that depth zero is equivalent to the maximal ideal being associated. Describe the nonzero element detected by \(\operatorname{Hom}_R(\kappa,M)\).

**Exercise 8.2 (easy).** In \(k[x,y,z]\), prove that \(x,y(1-x),z(1-x)\) is a regular sequence, but \(y(1-x),z(1-x),x\) is not. Exhibit the kernel element responsible for failure, and check that the final quotient is nevertheless nonzero.

**Exercise 8.3 (medium).** Prove that every zero-dimensional Noetherian local ring is CM, including nonreduced rings. Prove that every reduced one-dimensional Noetherian local ring is CM.

**Exercise 8.4 (medium).** For the two-plane ring (25), establish the exact intersection sequence and calculate depth at the origin using Ext. Explain why reducedness and equal component dimensions do not settle this question.

**Exercise 8.5 (hard).** Let \(A=k[x_1,\ldots,x_n]_{(x_1,\ldots,x_n)}\), and take \(f_1,\ldots,f_c\) in its maximal ideal. Suppose \(\dim A/(f_1,\ldots,f_c)=n-c\). Prove that the list is regular and its quotient is CM. Include the case of an empty list.

**Exercise 8.6 (hard).** For (28), prove that \(s^4,t^4\) is a system of parameters. Prove both \(s^6t^2\notin s^4S\) and \(s^6t^2\notin s^4R\), and compute the depth of \(R\). The second nonmembership requires an argument about denominators.

## 9. Complete solutions

**Solution 8.1.** If \(\mathfrak m\) is associated, there is \(0\ne z\in M\) with annihilator \(\mathfrak m\). Every element of \(\mathfrak m\) kills \(z\), so none acts injectively, and no positive-length regular sequence is possible. Conversely, at depth zero every element of \(\mathfrak m\) is a zero divisor: an injective one would leave a nonzero quotient by Nakayama and give a regular sequence. The finite associated-prime union and prime avoidance put \(\mathfrak m\) in one associated prime, which must equal \(\mathfrak m\). A homomorphism from \(\kappa\) is determined by the image \(z\) of \(1\), and it is well-defined exactly when \(\mathfrak m z=0\). A nonzero such image has annihilator exactly \(\mathfrak m\).

**Solution 8.2.** The polynomial ring is a domain, so \(x\) is injective. Modulo \(x\), the second element becomes \(y\) in \(k[y,z]\), and modulo \(x,y\), the third becomes \(z\) in \(k[z]\). Both are injective, and the final quotient is \(k\). Hence the original list is regular.

For the proposed permutation, the first element \(y(1-x)\) is still injective in the domain. But modulo its ideal, \(z(1-x)\) kills the class of \(y\), since their product is \(z[y(1-x)]\). This class is nonzero: an equality \(y=y(1-x)h\) would allow cancellation of \(y\) in the polynomial domain, giving \(1=(1-x)h\), impossible on evaluating at \(x=1\). The second entry therefore fails injectivity. Adding \(x\) to the two-element ideal makes it \((x,y,z)\), so the final quotient is again \(k\). Failure comes from an intermediate kernel, not from the final quotient condition. At the origin the factor \(1-x\) becomes a unit, in agreement with the local permutation theorem.

**Solution 8.3.** A nonzero zero-dimensional local ring has support dimension zero as a module over itself. The bound \(0\leq\operatorname{depth}R\leq\dim R=0\) makes it CM. Nothing in this argument requires reducedness. Concretely, its Noetherian zero-dimensional local structure is Artinian, with nilpotent maximal ideal. If that ideal is nonzero, the last nonzero power contains an element killed by the whole ideal; if it is zero, the ring is a field. In both cases depth is zero.

For a reduced one-dimensional Noetherian local ring, Solution 8.4 of *Associated primes and primary decomposition* says that the associated primes are exactly the finitely many minimal primes. The maximal ideal is not minimal: dimension one supplies a strictly smaller prime. Hence it is contained in none of the minimal primes, and prime avoidance chooses \(x\in\mathfrak m\) outside all of them. This \(x\) is injective; Nakayama makes its quotient nonzero. Thus depth is at least one, and the dimension bound makes it exactly one.

**Solution 8.4.** For arbitrary ideals \(I,J\) of \(P\), the diagonal map from \(P/(I\cap J)\) into \(P/I\oplus P/J\) is injective. The difference of residues maps the latter onto \(P/(I+J)\). To verify its kernel, let lifts \(u,v\) satisfy \(u-v=i+j\) with \(i\in I,j\in J\). The element \(u-i=v+j\) has the prescribed residues modulo both ideals. This proves (26), whose last module is \(k\).

The plane quotients have dimension two by the field polynomial height theorem, so the union of their closed supports has dimension two. On each summand, \(x+z,y+w\) is the ordinary pair of its independent coordinates. They are successively injective and give nonzero final quotients; hence the middle module has depth two by (13). Its Hom and first Ext from \(k\) vanish. Exactness then identifies \(\operatorname{Ext}^1_P(k,B)\) with \(\operatorname{Hom}_P(k,k)=k\) and makes \(\operatorname{Hom}_P(k,B)=0\). Theorem 2.3 gives depth one, which remains one over \(B\) by quotient-ring invariance. The ring is therefore not CM at the origin. Although the defining ideal is radical and the two components have the same dimension, the first nonzero Ext group occurs before the support dimension; those geometric conditions do not remove the obstruction in (27).

**Solution 8.5.** The field polynomial height theorem gives \(\dim A=n\). The maximal ideal has the displayed \(n\) generators, so its embedding dimension is at most \(n\), and Proposition 4.2 of *Dimension theory of Noetherian local rings* bounds it below by \(\dim A=n\). Thus \(A\) is regular local, and Theorem 6.1 makes it CM. Its quotient by the given list is nonzero by Nakayama, and its support as an \(A\)-module is the spectrum of that quotient. The assumed dimension is exactly the hypothesis (18). Theorem 4.2 proves regularity and the CM property, with depth \(n-c\). Quotient-ring invariance makes this also the depth as a module over its own local ring. When \(c=0\), the list is empty and the conclusion is simply that \(A\) is CM; when \(n=0\), this is the field case. The nonzero quotient dimension condition entails \(c\leq n\).

**Solution 8.6.** The four generators make \(S\) a finite-type Noetherian domain. The elements \(a=s^4,b=t^4\) are algebraically independent: distinct monomials in them have distinct exponent pairs in \(k[s,t]\). Writing \(v=s^3t,w=st^3\), the relations \(v^4=a^3b\) and \(w^4=ab^3\) make \(S\) finite integral over \(k[a,b]\), by the finite-generator integral criterion. Its fraction field is therefore algebraic over \(k(a,b)\) and has transcendence degree two. The maximal ideal \(\mathfrak m\) has residue field \(k\), so the height formula gives \(\operatorname{ht}\mathfrak m=2\) and \(\dim R=2\).

The ring \(S/(a,b)\) is generated over \(k\) by the images of \(v,w\), whose fourth powers vanish. It is spanned by \(v^iw^j\), \(0\leq i,j<4\), so is finite-dimensional over \(k\). It has just one prime, generated by these nilpotent images. Localizing gives a nonzero finite-length quotient \(R/(a,b)\). The two elements consequently form a system of parameters.

Monomials of \(S\) have exponent pairs in the additive semigroup generated by
\[
(4,0),\ (3,1),\ (1,3),\ (0,4).
\]
They are linearly independent in \(k[s,t]\). If \(u=s^6t^2\) belonged to \(aS\), cancellation in this polynomial domain would put \(s^2t^2\) in \(S\). Its total degree is four, so its exponent pair would have to be one of the four generators: any sum of two or more has degree at least eight. The pair \((2,2)\) is none of them. Thus \(u\notin aS\).

Give \(S\) its total-degree grading. Its positive-degree ideal is \(\mathfrak m\), so any \(q\notin\mathfrak m\) has nonzero constant term \(q_0\in k\). If \(u/1\in aR\), equality of fractions, or injectivity of the localization of this domain, would give some \(q\notin\mathfrak m\) with \(qu\in aS\). The ideal \(aS\) is homogeneous. Its degree-eight component would then contain \(q_0u\), forcing \(u\in aS\), a contradiction. Hence \(u\notin aR\).

Finally \(bu=s^6t^6=a w^2\). Thus \(b\) is a zero divisor on \(R/aR\). Since \(a,b\) is a parameter system, its failure of regularity proves non-CM by Corollary 4.3. The nonzero element \(a\) is injective in the domain, giving depth at least one; the depth bound and failure of CM make it exactly one.

## Proof dependencies and licence

Theorems 5.3 and 5.5 prove polynomial permanence and universal catenarity, including the local dimension formula that the chain argument needs. Ext comparison and both long exact sequences have complete proofs in *Resolutions, Tor and Ext*, Theorem 1.1 and Section 4. The scalar-annihilation argument, the least-nonzero-Ext characterization, and all depth consequences used here are proved above.

The polynomial and catenarity arguments incorporate the Stacks Project Authors' proofs in [AI Integrated Stacks Project at the pinned revision](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L26280), `lemma-maximal-CM-polynomial-algebra`, `lemma-CM-polynomial-algebra` and `lemma-CM-ring-catenary`. The source-linked supplementary proof 19, by GPT-6 Astra, supplies the support and leading-coefficient details. GPT-6.1 Sol checked the arguments, treated both kinds of prime in a polynomial fibre, and derived the dimension formula directly from the regular-sequence construction already proved here. This adapted lesson is licensed under GNU Free Documentation License 1.2, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts; the licence text accompanies its transparent source. History: Stacks Project Authors, *Commutative Algebra*, pinned AI Integrated Stacks Project revision; GPT-6 Astra, supplementary proof 19, September 2026; GPT-6.1 Sol, original CC0 lesson and this adaptation, October 2026. The earlier original material remains available under CC0. The later lesson *Projective dimension and the Auslander–Buchsbaum formula* relates depth to resolution length; no such formula is assumed here.

## References

The [official Stacks project](https://stacks.math.columbia.edu/) is the maintained reference. Tag links here use [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition with AI-proposed corrections and AI-written additions that have not been reviewed by the Stacks project maintainers. The original exposition and solutions are independently written; the incorporated polynomial and catenarity proofs retain the source credit and licence below.

- Regular sequences, local permutation, powers and flat behaviour: [Stacks, Tag 00LF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-regular-sequence), [Stacks, Tag 00LJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-permute-xi), [Stacks, Tag 07DV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-regular-sequence-powers), [Stacks, Tag 00LM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flat-increases-depth).
- Depth, Ext, the depth lemma and the associated-prime bound: [Stacks, Tag 00LI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-depth), [Stacks, Tag 00LW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-depth-ext), [Stacks, Tag 00LX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-depth-in-ses), [Stacks, Tag 0BK4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-depth-dim-associated-primes).
- CM modules, expected dimension, minimal associated points and localization: [Stacks, Tag 00N3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-CM), [Stacks, Tag 00N6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-CM-module), [Stacks, Tag 0BUS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-CM-ass-minimal-support), [Stacks, Tag 00NB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-CM). The distinction from maximal CM is [Stacks, Tag 00NF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-maximal-CM).
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, §9.5 and §§26.1–26.2: regular sequences, depth and Cohen–Macaulay geometry.

## Copyright and licence

Copyright (C) 2005–2025 Johan de Jong. The incorporated source is *The Stacks Project*, as distributed in AI Integrated Stacks Project at revision `565b10e987aba5969b21145a0833f42d69f96790`.

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. A copy is supplied as GNU Free Documentation License 1.2.

The original course material remains available under its CC0 dedication. This combined edition, including the incorporated and adapted proof, is distributed under GNU FDL 1.2 or later. The source authors, incorporated source titles and mathematical adaptations are identified above. History: Stacks Project Authors, original source; the credited AI Integrated Stacks Project editorial contributors, where used; OpenAI GPT-6.1 Sol, course adaptation, October 2026.


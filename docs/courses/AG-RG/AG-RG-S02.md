# Projective cohomology and smooth affine models

This supporting lesson proves the projective formal functions and smooth model statements needed before the reductive group lessons. It also records the precise earlier programme proofs used for completion, projective finiteness and curve duality. It follows the supporting lesson [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), whose Sections 1–9 supply the affine, homological, projective-space and Serre calculations. Both supporting lessons precede AG-RG-01. All mathematical sources listed here are freely readable. Source citations identify the material used to write the proofs; they do not replace any proof below.

The formal functions exposition adapts the freely readable Stacks Project proofs. The smooth affine component argument below specializes the Stacks model route and supplies its intermediate arguments. Permission is granted to copy, distribute and modify this lesson under the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The complete license is included in [the complete GNU FDL 1.2](assets/GFDL-1.2.txt). The original source notice, Copyright (C) 2005–2025 Johan de Jong, is retained in the cached introduction. The Stacks Project contributors retain their source rights. Original finite complex and curve bridge passages previously released as CC0 remain CC0; inclusion here does not remove either source's rights.

## 1. Earlier programme proofs used in this lesson

The following references are to proofs already written in programme lessons. Their numbered statements delimit exactly what is used.

* **AG-CA-03, Noetherian and Artinian rings:** Proposition 1.2 (finite modules over a Noetherian ring are Noetherian), Theorem 2.1 (Hilbert basis), Theorem 5.1 Artin–Rees, and Theorem 6.1 (Krull intersection). In particular Artin–Rees is proved by finite generation of the graded submodule of the Rees module; it is not taken from a book.
* **AG-CA-19, Completion:** Theorem 1.2 (exact inverse limits with a Mittag–Leffler kernel), Lemma 2.1 (completion preserves surjections with the induced kernel filtration), Proposition 2.2 (finite ideal powers in a completion), Theorems 3.1–3.3 (finite-module exactness, completion tensor comparison, flatness, faithful flatness and Noetherianity). These statements have full proofs there. Thus a finite module over an already complete Noetherian ring is complete, and local Noetherian completion is faithfully flat.
* **AG-CA-17, Formally smooth, unramified and étale ring maps:** Theorem 3.1 (formal smoothness is the split conormal criterion), Theorems 4.1 and 5.1 (standard smooth presentations and local standard form), and Lemma 6.2 (unique lifting of idempotents across a square-zero ideal). These are written lifting and matrix proofs. Lemma 1.1 extends idempotent lifting to a nilpotent ideal by successive square-zero steps.
* **AG-CA-18, Smooth algebras over a field and the Jacobian criterion:** Theorem 2.1 proves regularity of smooth field-algebra local rings. Its proof uses standard smooth equations and the regular parameter quotient theorem. Base change of smoothness, proved in AG-CA-17, consequently gives geometric regularity.
* **AG-CA-14, Regular local rings:** Theorem 1.1 and Proposition 1.4 prove regular parameter quotients and generation of a regular quotient's ideal by part of a regular system of parameters. The graded and regular-sequence assertions used there are the full proof of Theorem 6.1 in **Regular sequences, depth and Cohen–Macaulay modules**. The Koszul resolution and its Hom calculation are the corresponding earlier depth lesson proofs.
* **AG-CA-07, Tor and flat modules:** Theorems 5.3 and 6.1 contain the finite-projective and flat-kernel calculations corresponding to Section 5. That section writes its universal-tail flatness and global splitting arguments directly, without taking the Tor criterion as an additional prerequisite.
* **AG-CA-05, Integral extensions:** Theorems 3.2–3.4 prove lying over and incomparability. Section 6 below contains the complete DVR argument in Lemma 6.C and the separable trace-lattice, finite normalization, function-field rational-map spreading and dense equalizer arguments in Lemma 6.4. The homogeneous-coordinate extension over every DVR is written there as well.
* **AG-MO-03, Limits of schemes and Noetherian approximation:** Theorem 1.1, Lemma 2.1 and Theorems 4.1–4.2 prove affine limits, retention of finite open covers, finite-presentation descent, eventual equality of maps and descent of closed immersions. Only the proved affine approximation Theorem 5.1 is needed here. The external-proof-only absolute approximation Theorem 5.2 is not used.
* **AG-MO-06, Quasi-finite morphisms and Chevalley's theorem:** Theorem 3.1 proves the Noetherian constructibility criterion and Theorem 4.2 proves Chevalley's theorem. The argument in Section 4 below uses these particular proved statements.
* **AG-FSE, Flat morphisms:** Lemma 5.1 and Corollary 5.2 prove generic freeness over a domain, including for a finite module over a finite type algebra. No openness-of-flatness theorem is needed in Section 4.
* **AG-CA-18, Smooth algebras over a field and the Jacobian criterion:** Theorem 6.1 and Corollary 6.2 prove smooth and étale flatness over arbitrary bases. Together with AG-CA-17 Theorem 5.1 and Lemma 7.1 these give the separating generic coordinates used below.
* **AG-RG-S01, Sections 4–6:** the finite ordered Čech comparison, affine quasi-coherent vanishing and flat base change are proved before this lesson. A finite affine cover of a separated scheme therefore computes quasi-coherent cohomology by its finite section complex. The same written complex calculation treats finite and arbitrary direct sums and flat localization.
* **AG-RG-S01, Sections 7–8:** Theorems 7.2–7.3 compute every projective-space twist and the perfect monomial pairing. Proposition 8.2 and Theorem 8.4 prove finite quotients by twists, finite coherent cohomology and eventual vanishing, including the closed-immersion passage to projective schemes. Lemmas 8.1 and 8.3 give denominator extension and the ample-power immersion; Corollary 7.B makes it closed for a proper source. Theorem 8.5 treats every sufficiently large power, as applied in Section 7 below.
* **AG-QC-14, Ext sheaves and Serre duality on projective space:** Proposition 1.1, Proposition 1.2, Proposition 2.1 and Theorem 5.1 give the local Ext calculation, vector-bundle tensor-Hom comparison, local-to-global Ext spectral sequence and ambient projective Serre duality. The duality proof uses the monomial trace, a two-stage twist presentation and explicit dimension shifting. Its reference to “proper finiteness” in Theorem 4.1 is supplied here by the full projective finiteness proof in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Section 8 (AG-QC-05 Theorem 2.1), without using the general proper-finiteness provider. Section 6 below also spells out the single-row local-to-global Ext comparison being consumed, using the earlier finite filtered-complex construction; no general proper duality theorem is needed here.

These references are a finite proof dependency list, not a declaration that unnamed results are ordinary foundations. In particular the further smoothness descent and connected model results are proved in Sections 3–4.

### 1.1. The consumed Artin–Rees and completion arguments

The following records the actual arguments of AG-CA-03 Theorem 5.1 and AG-CA-19 Theorems 3.1–3.3 before their uses. Let \(A\) be Noetherian and \(I\subset A\) an ideal.

**Lemma 1.1 (Artin–Rees).** If \(N\subset M\) are finite \(A\)-modules, there is \(c\) such that

\[
N\cap I^nM=I^{n-c}(N\cap I^cM)\quad(n\geq c).
\]

**Proof.** The Rees algebra \(B=\bigoplus I^nt^n\) is generated by the finitely many generators of \(I\) in degree one, so is Noetherian by Hilbert basis. The module \(\bigoplus I^nMt^n\) is finite over it, generated by any finite list of generators of \(M\) in degree zero. Its graded submodule \(\bigoplus(N\cap I^nM)t^n\) is finite. Choose homogeneous generators of degrees at most \(c\). For \(n\geq c\), the degree \(n\) component is a sum of \(I^{n-d}(N\cap I^dM)\), for \(d\leq c\); each is contained in \(I^{n-c}(N\cap I^cM)\). The reverse inclusion follows by multiplication and the submodule property. \(\square\)

The consumed Krull intersection statement also follows from this proof. For a finite module over a Noetherian local ring, with \(I\) in its maximal ideal, the submodule \(N=\bigcap_n I^nM\) is finite. Lemma 1.1 gives \(N=IN\) by taking \(n=c+1\), since \(N\cap I^nM=N\) at every index. Nakayama gives \(N=0\). This is the actual AG-CA-03 Theorem 6.1 argument used in the earlier regular-ring proof.

**Lemma 1.2 (exact finite-module completion).** Writing \(\widehat M=\varprojlim M/I^nM\), completion is exact on finite modules and

\[
\widehat M=M\otimes_A\widehat A.
\]

**Proof.** For \(0\to N\to M\to L\to0\), the quotients give

\[
0\to N/(N\cap I^nM)\to M/I^nM\to L/I^nL\to0.
\]

The kernel system has surjective transitions. Compatible lifts in the middle system can therefore be chosen successively: given a lift at stage \(n\), take any lift of the desired next quotient element and adjust its image's difference at stage \(n\) by lifting that difference from the kernel system. This proves surjectivity on inverse limits. Injectivity and equality with the limit kernel hold coordinatewise. By Lemma 1.1, \(I^nN\subset N\cap I^nM\subset I^{n-c}N\); hence the two filtrations of \(N\) are cofinal. Their limits identify explicitly by taking a sufficiently far coordinate to define a coordinate of the other system, independent of that choice by compatibility. Thus the displayed inverse-limit sequence is \(0\to\widehat N\to\widehat M\to\widehat L\to0\).

A finite module has a finite presentation, since submodules of finite modules are finite over a Noetherian ring. Complete \(A^r\to A^s\to M\to0\), using the just-proved exactness. Tensor the same presentation with \(\widehat A\), using tensor's right exactness. Finite direct sums complete coordinatewise, so both cokernels are the cokernel of the same matrix \(\widehat A^r\to\widehat A^s\). This gives the canonical tensor comparison. In particular, when \(A\) is already complete, every finite module is complete. \(\square\)

**Lemma 1.3 (flat, faithfully flat and Noetherian completion).** The ring \(\widehat A\) is Noetherian, is complete for \(I\widehat A\), and is \(A\)-flat. If \(I\) is contained in the Jacobson radical, the completion is faithfully flat.

**Proof.** Flatness follows directly from the preceding finite-module exactness. Every module is the filtered union of its finite generated submodules. A tensor element uses finitely many such generators, and an equality to zero holds in a sufficiently large finite submodule, because tensor commutes with filtered colimits by its generators and relations. For an injection \(M'\to M\), put a proposed tensor kernel element in a finite submodule \(N\subset M'\), and put its vanishing equality in some finite submodule of \(M\) containing the image of \(N\). Exactness of completion for these finite modules proves injectivity there, hence kills the proposed kernel. Thus tensor with \(\widehat A\) preserves every injection.

For faithfulness, if \(M\ne0\), choose \(0\ne x\in M\), with cyclic submodule \(Ax=A/J\). Choose a maximal ideal \(\mathfrak m\supset J\). Since \(I\subset\mathfrak m\), the module \(A/\mathfrak m\) is unchanged by completion. The tensor comparison gives \(\widehat A/\mathfrak m\widehat A=A/\mathfrak m\ne0\), a quotient of \((A/J)\otimes\widehat A\). Flatness injects the latter into \(M\otimes\widehat A\), so this is nonzero. This proves faithful flatness and, by applying it to a tensor kernel, detection of exactness.

Apply Lemma 1.2 to \(0\to I^a\to A\to A/I^a\to0\). The last module is unchanged by completion, since a power of \(I\) kills it. The image of \(I^a\otimes\widehat A\) is exactly \(I^a\widehat A\), whence

\[
\widehat A/I^a\widehat A=A/I^a.
\]

Writing \(J=I\widehat A\), its powers are \(I^a\widehat A\); these identities and the defining inverse limit prove \(J\)-adic completeness and separatedness. Their successive kernels identify \(\operatorname{gr}_J\widehat A\) with \(\operatorname{gr}_IA\). The latter is a quotient of a polynomial ring over \(A/I\) on the finite generators of \(I\), and is Noetherian.

For any ideal \(Q\subset\widehat A\), its initial classes form a homogeneous ideal of this Noetherian graded ring. Choose finite homogeneous generators and lift them to \(q_i\in Q\), with orders \(d_i\). For \(q\in Q\), subtract at stage \(n\) a combination \(\sum_i a_{i,n}q_i\) matching its residual initial class, with \(a_{i,n}\in J^{n-d_i}\) and zero when \(n<d_i\). The new residual is in \(J^{n+1}\). Each coefficient series converges, since its orders tend to infinity. Its sums \(a_i\) satisfy \(q=\sum_i a_iq_i\) by separatedness. Thus every ideal is finite and \(\widehat A\) is Noetherian. No prior assertion that \(Q\) is closed was used. \(\square\)

For a local ring with maximal ideal \(\mathfrak m\), its completion is local: an element with nonzero residue is a unit in every quotient \(A/\mathfrak m^n\), and the compatible inverses give its inverse in the limit. Projection onto the residue field is surjective by successive lifting. The preceding quotient identity makes its kernel \(\mathfrak m\widehat A\). Thus Lemma 1.3 gives the exact local completion statement used by the group lessons.

**Lemma 1.4 (idempotents across a nilpotent ideal).** Every idempotent of \(R/J\), for a nilpotent ideal \(J\), has a unique idempotent lift to \(R\).

**Proof.** First suppose \(J^2=0\). For a lift \(e\), put \(\delta=e^2-e\in J\). Then \(e'=e-(2e-1)\delta\) is idempotent: expand its square and use \(\delta^2=0\) and \((2e-1)^2=1+4\delta\). For two idempotent lifts the difference \(u\in J\) satisfies \((2e-1)u=0\); the element \(2e-1\) is a unit since its square is one, so \(u=0\). Apply this square-zero argument successively to \(J^a/J^{a+1}\), starting with \(a=1\); each is square-zero because \(2a\geq a+1\), and nilpotence makes the list finite. \(\square\)

## 2. Formal functions on a projective scheme

Let \(A\) be Noetherian, \(I\subset A\) an ideal, \(X\to\operatorname{Spec}A\) projective and \(F\) coherent. Write

\[
B=\bigoplus_{n\geq0}I^nt^n\subset A[t],\qquad
M_n^q=H^q(X,I^nF),\qquad M^q=M_0^q.
\]

The transition maps \(M_m^q\to M_n^q\), for \(m\geq n\), come from inclusion of ideal powers. Multiplication \(I^d\otimes M_n^q\to M_{n+d}^q\) is compatible with these transitions: both sheaf maps are multiplication followed by the same inclusion. Applying cohomology preserves their equality.

**Lemma 2.1.** The graded \(B\)-module \(\bigoplus_{n\geq0}M_n^qt^n\) is finite for every \(q\).

**Proof.** Generators of \(I\), placed in degree one, generate \(B\) as an \(A\)-algebra; Hilbert basis makes \(B\) Noetherian. Let \(X_B=X\times_A\operatorname{Spec}B\), with affine projection \(\pi\). On \(U=\operatorname{Spec}R\subset X\), put \(F|_U=\widetilde N\). The graded module \(\bigoplus I^nN\) is finite over \(R\otimes_AB\): finitely many \(R\)-generators of \(N\), placed in degree zero, generate it. Here \(R\otimes_AB\to\bigoplus I^nR\) is a surjection, and need not be an isomorphism. No flatness assumption is being made.

Localization gives the same modules on overlaps. They glue to a coherent sheaf \(G\) on \(X_B\), with \(\pi_*G=\bigoplus I^nF\). Coherence holds because \(R\otimes_AB\) is Noetherian and the module is finite. Base changing a projective closed immersion shows that \(X_B\) is projective over \(B\); AG-QC-05 Theorem 2.1 and its closed-immersion passage give finite \(H^q(X_B,G)\) over \(B\).

Use the inverse images of a finite affine cover of \(X\). Each intersection is affine on both schemes, and its sections of \(G\) are the sections of \(\bigoplus I^nF\) on the original intersection. Thus their ordered section complexes are identical. Finite products in that complex commute with direct sums, and direct sums of modules are exact. Taking cohomology therefore identifies

\[
H^q(X_B,G)=\bigoplus_{n\geq0}H^q(X,I^nF),
\]

with the graded \(B\)-action preserved. This proves finiteness. \(\square\)

This writes the projective case of the free proofs [Stacks 02O8](https://stacks.math.columbia.edu/tag/02O8) and [0897](https://stacks.math.columbia.edu/tag/0897). General proper coherent pushforward and its dévissage are unnecessary: both spaces just used are projective.

Put

\[
J_n^q=\operatorname{im}(M_n^q\to M^q),\qquad
K_n^q=\ker(M_n^q\to M^q).
\]

**Lemma 2.2.** There are constants \(a_q,b_q\geq0\) such that

\[
I^nM^q\subset J_n^q\subset I^{n-a_q}M^q\quad(n\geq a_q),
\]

and \(K_m^q\to K_n^q\) is zero whenever \(m\geq n+b_q\).

**Proof.** Multiplication by \(u\in I^n\) on \(F\) factors through \(I^nF\), proving the first inclusion. The image and kernel of the graded map from Lemma 2.1 to the corresponding degreewise copies of \(M^q\) are graded subquotients of a finite \(B\)-module. More explicitly, multiplication and transition compatibility show that \(\bigoplus J_n^qt^n\) is the graded image module and \(\bigoplus K_n^qt^n\) is a graded submodule of \(\bigoplus M_n^qt^n\). Both are finite, because \(B\) is Noetherian.

Choose homogeneous generators of the image module of degrees \(d\leq a_q\). Its degree \(n\) is a sum of terms \(I^{n-d}J_d^q\subset I^{n-a_q}M^q\), proving the other inclusion. Choose homogeneous kernel generators \(z_j\in K_{d_j}^q\), with \(d_j\leq b_q\). An element in degree \(m\) is a sum of \(u_jz_j\), where \(u_j\in I^{m-d_j}\). If \(m\geq n+b_q\), express \(u_j\) as a sum of products \(vw\), \(v\in I^n\), \(w\in I^{m-d_j-n}\). Transition of \(vwz_j\) to \(M_n^q\) factors as transition of \(z_j\) to \(M_0^q\), followed by multiplication by \(w\), then by \(v\) into \(M_n^q\). The first map kills \(z_j\). Every such product, and hence the transition, is zero. \(\square\)

**Theorem 2.3.** There is a canonical isomorphism

\[
H^q(X,F)^\wedge_I\ \xrightarrow{\sim}\
\varprojlim_nH^q(X,F/I^nF).
\]

It is a homeomorphism for the quotient inverse-limit topologies.

**Proof.** Write \(T_n^q=H^q(X,F/I^nF)\). The sheaf short exact sequence gives compatible exact sequences

\[
0\longrightarrow M^q/J_n^q\longrightarrow T_n^q
\longrightarrow K_n^{q+1}\longrightarrow0.
\]

For \(m\geq n+b_{q+1}\), the transition on the last term is zero. Hence the image of \(T_m^q\to T_n^q\) is contained in the first term \(M^q/J_n^q\). It equals that term: transition \(M^q/J_m^q\to M^q/J_n^q\) is onto and these modules inject into \(T_m^q,T_n^q\). This proves the Mittag–Leffler assertion and its stable image, with a written uniform bound.

If \((u_n)\) is a compatible family in \(T_n^q\), its image in \(K_n^{q+1}\) is zero at every coordinate, because that image is the transition of a sufficiently distant kernel term. Thus \(u_n\) has a unique preimage in \(M^q/J_n^q\); uniqueness makes those preimages compatible. Consequently

\[
\varprojlim_nT_n^q=\varprojlim_nM^q/J_n^q.
\]

Lemma 2.2 gives \(I^nM^q\subset J_n^q\) and \(J_{n+a_q}^q\subset I^nM^q\). Projection and projection from the shifted index define inverse maps between the two quotient limits. A common finer index proves that their composites are the identity. Each map is continuous coordinate by coordinate, proving the topological assertion. Every construction is the canonical quotient map, so the isomorphism is the asserted one. \(\square\)

This supplies the critical image, kernel and limit arguments of [Stacks 02OA](https://stacks.math.columbia.edu/tag/02OA), [02OB](https://stacks.math.columbia.edu/tag/02OB) and [02OC](https://stacks.math.columbia.edu/tag/02OC). In particular, the proof uses the kernel transition bound directly; it does not rely on the incorrect part-number reference presently printed in 02OB. No inverse limit has been interchanged with an unexplained cohomology operation.

**Corollary 2.4.** If \(A\) is complete local Noetherian, every compatible idempotent on the maximal-ideal thickenings of a projective \(X\) comes from a unique idempotent of \(\Gamma(X,\mathcal O_X)\).

**Proof.** Projective finiteness makes \(M=\Gamma(X,\mathcal O_X)\) finite. Lemma 1.2 gives \(M=M\otimes_A\widehat A=\widehat M\). Theorem 2.3 identifies this ring with the limit of the thickened section rings. The equality \(e^2=e\) holds in this limit coordinatewise and hence holds for the corresponding actual section. Uniqueness follows from the same ring isomorphism. Idempotents at successive levels are compatible whenever they lift the same initial idempotent, by Lemma 1.4's unique nilpotent lifting. \(\square\)

## 3. Smoothness and line bundles at a finite stage

**Lemma 3.0 (the split conormal criterion).** For a polynomial presentation \(C=P/J\), the algebra is formally smooth precisely when \(d:J/J^2\to\Omega_{P/B}\otimes_PC\) has a \(C\)-linear left inverse.

**Proof.** Formal smoothness lifts the identity of \(C\) to a section \(s:C\to P/J^2\). The map \(D(p)=p\bmod J^2-s(p\bmod J)\) takes values in \(J/J^2\), satisfies the product rule because this ideal is square-zero, and sends \(j\in J\) to its class. The universal derivation for the polynomial ring therefore factors it through \(\Omega_{P/B}\otimes C\), giving a left inverse of \(d\). Conversely a left inverse gives this derivation by composition with the polynomial universal derivation. The map \(p\mapsto p\bmod J^2-D(p)\) is multiplicative by the product rule and the square-zero condition. It kills \(J\) and is the identity after reduction to \(C\), so gives a section. In any square-zero lifting test, lift the polynomial variables arbitrarily. The resulting map from \(P\) sends \(J\) into the square-zero test ideal and kills \(J^2\); composing its factor through \(P/J^2\) with the section gives the required lift. Polynomial differentials are free on the variable symbols by the product rule, so no unproved splitting assertion enters this argument. \(\square\)

<a id="smooth-map-differential"></a>

**Lemma 3.A (maps between smooth schemes).** Let \(X\) and \(Y\) be smooth schemes locally of finite presentation over any scheme \(S\), and let \(h:X\to Y\) be an \(S\)-map. If the map on relative tangent spaces at a point \(x\), with scalars extended to \(\kappa(x)\), is surjective, then \(h\) is smooth near \(x\). If that map is an isomorphism, then \(h\) is étale near \(x\). In particular, on a smooth morphism of relative dimension \(d\), local functions \(q_1,\ldots,q_d\) whose differentials form a basis at \(x\) give an étale coordinate map to \(\mathbb A^d_S\) near \(x\).

**Proof.** Work on compatible affine neighbourhoods of \(x\), \(h(x)\) and their image in \(S\). Write their algebras as \(C,D,A\). The map \(D\to C\) is finitely presented: choose finite presentations of \(D\) and \(C\) over \(A\), and add, to the presentation of \(C\), the finitely many equations equating each generator of \(D\) with a polynomial representing its image in \(C\). This gives a finite presentation over \(D\).

The split conormal criterion makes \(\Omega_{C/A}\) and \(\Omega_{D/A}\) finite projective. Indeed, in a finite polynomial presentation the conormal injection has a left inverse, so its cokernel is a direct summand of the finite free module of polynomial differentials. Such a summand is flat, and the local finite-freeness proof in AG-RG-S01, Lemma 1.2, applies. Shrink the affine neighbourhoods to trivialize these modules. Dualizing the asserted tangent surjection gives an injection on the fibre of
\[
u:C\otimes_D\Omega_{D/A}\longrightarrow\Omega_{C/A}.
\]
A full-size minor of its matrix is nonzero at \(x\); invert it. Projecting to the corresponding rows and multiplying by that square matrix's inverse gives a \(C\)-linear left inverse of \(u\). In the tangent-isomorphism case its matrix is square and invertible after this shrink.

Consider an arbitrary square-zero surjection \(R\to R/J\), an \(A\)-algebra map \(C\to R/J\), and a prescribed \(D\)-algebra structure on \(R\) agreeing with it after reduction. Formal smoothness of \(C/A\), as proved by Lemma 3.0, supplies an \(A\)-algebra lift \(v:C\to R\). Its restriction to \(D\) differs from the prescribed map by an \(A\)-derivation \(\delta:D\to J\): expanding a product leaves the two first-order terms, since \(J^2=0\). It corresponds to a map \(C\otimes_D\Omega_{D/A}\to J\), where the \(C\)-action on \(J\) is through the given reduced map. Compose it with the left inverse of \(u\) to obtain \(\Omega_{C/A}\to J\), hence an \(A\)-derivation \(\widetilde\delta:C\to J\). The map \(v-\widetilde\delta\) is again an \(A\)-algebra map by the same square-zero product expansion. Its restriction to \(D\) is the prescribed map. Thus \(C/D\) is formally smooth. Its finite presentation makes it smooth.

If \(u\) is an isomorphism, two such \(D\)-lifts differ by a derivation \(C\to J\) whose differential map vanishes on the image of \(u\). That image is all of \(\Omega_{C/A}\), so the lifts agree. The map is formally étale and finitely presented, hence étale. The coordinate assertion is this case with \(Y=\mathbb A^d_S\): its pulled-back differentials have basis \(dq_1,\ldots,dq_d\), and the given basis condition makes \(u\) an isomorphism near \(x\). No Noetherian, reducedness, characteristic or residue-field separability hypothesis was used. \(\square\)

**Lemma 3.1.** Let \(A=\varinjlim A_i\) be a filtered ring colimit. A finitely presented algebra map \(B_0\to C_0\) over \(A_0\) whose base change over \(A\) is smooth becomes smooth after a finite stage.

**Proof.** Present \(C_0=B_0[x_1,\ldots,x_r]/(f_1,\ldots,f_s)\). At stage \(i\), let \(P_i=B_i[x_1,\ldots,x_r]\), \(J_i=(f_{1,i},\ldots,f_{s,i})\) and \(C_i=P_i/J_i\). Lemma 3.0, the split conormal criterion of AG-CA-17 Theorem 3.1, says that the map

\[
J/J^2\xrightarrow{d}C^r
\]

over the colimit has a \(C\)-linear left inverse \(\rho\). Each \(\rho(dx_k)\) is a finite sum of classes of the \(f_j\) with coefficients in \(C\). Lift these finitely many coefficients to one stage and define \(\rho_i:C_i^r\to J_i/J_i^2\) by those images. The equations \(\rho_i(df_{j,i})=f_{j,i}\bmod J_i^2\) are finitely many equations. Their truth in the colimit is witnessed by finite sums of products of the \(f_j\), representing membership in \(J^2\). Lift these witnesses and enlarge the stage until the polynomial equalities hold. Then \(\rho_id\) fixes all generators of \(J_i/J_i^2\), so is its identity. The same criterion gives formal smoothness at that stage, and the existing finite presentation gives smoothness. \(\square\)

This is the actual finite witness proof in [Stacks 0C0B](https://stacks.math.columbia.edu/tag/0C0B).

**Proposition 3.2.** A smooth scheme of finite presentation over an affine filtered limit has a smooth finite-presentation model at a finite stage. A projective embedding and a specified line bundle can be retained simultaneously.

**Proof.** First descend the finite-presentation scheme, the embedding if specified, and finitely many affine source and target charts by AG-MO-03 Theorem 4.1. Retain the closed immersion by its Theorem 4.2. Choose a finite affine cover of the original source on which the chart algebra maps are smooth. Descend these opens and the maps, and retain their covering property by Lemma 2.1 of that lesson. Apply Lemma 3.1 on the finitely many chart maps and take a common later stage. Smoothness is now true on a cover, hence globally.

For an invertible sheaf, refine the cover so that it is trivial on each chart. On finite affine overlap covers record each transition unit and its inverse. Record their inverse equations, their agreements on overlap refinements, and the cocycle equations on finite covers of triple overlaps. The sections and their finite equality witnesses descend by the section and eventual-equality parts of AG-MO-03. At a common stage these equations hold, so gluing the trivial rank-one sheaves gives an invertible sheaf there. Retain the finite chart covers, smoothness and the projective closed immersion at that same stage. Pullback recovers the original sheaf and scheme. \(\square\)

This fills the finite-cover step omitted in [Stacks 0C0C](https://stacks.math.columbia.edu/tag/0C0C). It proves only the finite chart and line bundle case being used, without importing general coherent sheaf descent or a general perfection theorem.

## 4. Geometrically connected smooth affine models

The model needed for the normalizer argument is smooth and affine. We prove this case; the unrestricted finite-presentation connected-fibre theorem is not needed.

**Lemma 4.1.** Over an algebraically closed field \(k\), an affine finite type connected scheme remains connected after every field extension. A smooth affine finite type scheme has disjoint irreducible components, and each connected component is integral and remains integral after every field extension of an algebraically closed ground field.

**Proof.** Connectedness of \(\operatorname{Spec}B\) is equivalent to absence of nontrivial idempotents. Indeed an idempotent gives the disjoint opens \(D(e),D(1-e)\); conversely a disjoint open-and-closed decomposition gives a section with values one and zero, hence an idempotent by affine sections.

Suppose an extension \(L/k\) supplies a nontrivial idempotent \(e\in B\otimes_kL\). Express \(e\) and \(1-e\) using finite lists of \(k\)-linearly independent elements of \(B\), with coefficients in \(L\). Let \(R\subset L\) be the finite type \(k\)-algebra generated by these coefficients, inverted nonzero coefficients ensuring that both expressions stay nonzero, and the finitely many coefficients needed for \(e^2=e\). The relation already holds over \(R\), since \(B\otimes_kR\to B\otimes_kL\) is injective. The nonzero finite type algebra \(R\) has a \(k\)-valued point by the proved Nullstellensatz in AG-CA-06. Specializing at it gives a nontrivial idempotent in \(B\), a contradiction.

For smooth \(B\), every local ring is a regular local domain by AG-CA-18 and AG-CA-14. Two distinct irreducible components cannot meet at a point, since their distinct minimal primes would give distinct minimal primes in that local ring. There are finitely many components; they are consequently both closed and open. Smoothness also makes the ring reduced. Each connected component is thus reduced and irreducible, hence integral. After extending an algebraically closed field, connectedness just proved and smoothness preserved by base change give the same conclusion. \(\square\)

It follows that the number of geometric connected components of a smooth affine finite type scheme is invariant under field extensions. To check this, embed the chosen algebraic closures of the two fields into a common algebraically closed extension. Apply Lemma 4.1 to each of the finitely many open-and-closed components. Extension is faithfully flat and preserves nonemptiness, so each component remains one component.

**Lemma 4.2.** Let \(A\) be a Noetherian domain with fraction field \(K\). If a smooth affine finite type \(A\)-scheme has geometrically integral generic fibre, there is a nonempty principal open of \(\operatorname{Spec}A\) on which all its fibres are geometrically integral.

**Proof.** Write the algebra as \(B\). Smoothness makes \(B\) \(A\)-flat, so \(B\hookrightarrow B_K\). Since the latter is a domain, \(B\) is a domain. Let \(L=\operatorname{Frac}(B_K)\). An étale coordinate chart at the generic point gives algebraically independent \(t_1,\ldots,t_d\in L\) with \(L\) finite separable over \(K(t_1,\ldots,t_d)\): use the standard smooth chart and its zero-relative-dimension coordinate map from AG-CA-17 Theorem 5.1, applied over the field, followed by AG-CA-18 Corollary 6.2 and AG-CA-17 Lemma 7.1. A primitive element \(u\) writes

\[
L=K(t_1,\ldots,t_d)(u).
\]

For completeness the primitive element assertion needs no additional theorem here. A finite separable extension of degree \(n\) has exactly \(n\) embeddings into an algebraic closure: adjoining finitely many generators successively, every previous embedding extends once for each distinct root of the next separable minimal polynomial; multiplication of these numbers agrees with multiplication of the field degrees. Over an infinite field these finitely many embeddings can be separated as follows. A linear combination of a finite generating list can be chosen to have different values under every pair of embeddings: the bad coefficients lie in finitely many proper linear hyperplanes, whose product of nonzero linear equations does not vanish on every tuple over an infinite field. A nonzero polynomial cannot vanish everywhere over an infinite field: induct on the number of variables, choose a point where its nonzero leading coefficient does not vanish, and then avoid the finitely many roots in the last variable. Its minimal polynomial then has the full extension degree. Over a finite field the multiplicative group of any finite extension is cyclic: the exponent is realized as an element order by taking the maximal prime-power orders and multiplying their commuting representatives; every element is a root of \(T^m-1\), so the root bound forces the group size to be at most this exponent. A generator of that cyclic group generates the field.

Clear denominators in the minimal polynomial of \(u\), removing the coefficient content, to obtain a primitive polynomial \(P\in K[t_1,\ldots,t_d,T]\). It is absolutely irreducible. Indeed \(B_K\otimes_K\overline K\) is a domain, and localizing it gives the domain \(L\otimes_K\overline K\). The algebra \(K[t_1,\ldots,t_d,T]/(P)\) embeds in \(L\) by its primitive minimal-polynomial presentation. Tensoring this injection with the field \(\overline K\) keeps it injective. Its target is the just-obtained domain, so the polynomial quotient over \(\overline K\) is a domain, proving absolute irreducibility without any assertion about contents after field extension.

Here is the needed polynomial Gauss argument. A product of primitive polynomials over a UFD stays primitive: modulo any prime coefficient factor, the two reductions are nonzero polynomials over a domain, so their product is nonzero. Starting with a field and inducting on the number of variables, factor the coefficient content and then factor the primitive part over the fraction field, whose one-variable polynomial ring has Euclidean division. Clear the denominators and normalize each factor to primitive content. The preceding product calculation shows that this gives a factorization over the coefficient ring, and uniqueness follows from the fraction-field uniqueness and the content. Thus each polynomial coefficient ring is a UFD; its primitive minimal polynomial generates the kernel of evaluation in the field extension, as used above.

Enlarge a nonzero localization of \(A\) until \(P\) has coefficients there. There is a further nonempty localization on which its specialization is absolutely irreducible in every residue field. Here is a finite proof of this assertion. A triangular variable change \(x_i=y_i+y_n^{N_i}\) makes the weights of the finitely many monomials distinct, using successive powers of an integer larger than all occurring exponents. The unique largest weight gives a nonzero leading coefficient in \(y_n\). Invert it and divide by it, making \(P\) monic of degree \(r>0\) in that variable. Let \(D_i\) bound its degrees in the other variables. A nontrivial factorization over a field has monic factors of positive \(y_n\)-degrees \(e,r-e\), \(1\leq e<r\), with other degrees at most \(D_i\); degrees add in each variable over a domain. For each \(e\), introduce the finitely many coefficients of these possible factors and impose the coefficients of \(P-Q_1Q_2\). This gives a finite type \(A\)-algebra \(R_e\). Its generic fibre is zero by absolute irreducibility and the Nullstellensatz over \(\overline K\). Therefore \(1=0\) after tensoring with \(K\), so some nonzero \(a_e\in A\) makes \((R_e)_{a_e}=0\). Inverting the finite product excludes every nontrivial factorization over every field extension of every residue field. Degree-zero factors in the monic variable are units and are excluded from this list. This is the finite coefficient proof of the free [Stacks 0557](https://stacks.math.columbia.edu/tag/0557) result, with only positive factor degrees used.

Put \(B'=A[t_1,\ldots,t_d,T]/(P)\) over the localization just obtained. Its generic fraction field and that of \(B\) are the same. The two generic affine integral schemes have a common nonempty affine principal open: represent the finite generators of each algebra as fractions in the other, invert their finitely many denominators, and invert the denominators needed for these descriptions to be inverse. AG-MO-03's map descent and eventual equality spread this isomorphism after another nonzero base localization. Thus we have \(B_h\cong B'_{h'}\), with \(h\ne0\) and nonempty generic open.

Apply AG-FSE Corollary 5.2 in **Flat morphisms** to the finite \(B\)-module \(B/hB\), and shrink so that it is \(A\)-flat. In the sequence \(0\to B\xrightarrow{h}B\to B/hB\to0\), flatness of the last term makes multiplication by \(h\) injective after every field base change. The smooth fibre is reduced and Noetherian. A nonzerodivisor belongs to no minimal prime: if it did, localization at that minimal prime would make it zero in the field of a reduced Noetherian ring, giving an annihilator outside the prime. Therefore \(D(h)\) is dense in every geometric fibre.

Chevalley's proved theorem makes the image of the common open constructible. It contains the generic point, so contains a nonempty open of the base. Shrink to a principal open in it; now the common open is nonempty in every fibre, and remains so after field extension. The \(B'\)-fibre is geometrically integral by the polynomial argument. Its nonempty open \(D(h')\), identified with \(D(h)\), is geometrically irreducible. Being dense in the smooth, geometrically reduced \(B\)-fibre, it forces that whole fibre to be irreducible and reduced. This proves the lemma. \(\square\)

**Lemma 4.3.** For a smooth affine finite type morphism over a Noetherian base, the number of geometric connected components of its fibres is a constructible function.

**Proof.** By the Noetherian constructibility criterion in AG-MO-06 Theorem 3.1, it suffices to show constancy on a nonempty open of every irreducible reduced closed subscheme of the base. Restrict to such an integral affine base \(\operatorname{Spec}A\), with fraction field \(K\).

If the generic fibre is empty, its flat affine algebra injects into zero and is zero, so the component number is constantly zero. Otherwise the generic geometric fibre has finitely many open-and-closed integral components by Lemma 4.1. Their finitely many orthogonal idempotents, summing to one, descend to a finite separable extension \(K'/K\). To justify separability, first express them over \(\overline K\). In positive characteristic each expression uses finitely many coefficients which become separable after some common \(p\)-power. Since an idempotent equals its own \(p\)-power, raising its expression to this power puts its coefficients in \(K^{\mathrm{sep}}\). In characteristic zero this step is unnecessary. The finite list of algebraic separable coefficients lies in one finite separable extension. Its components are geometrically integral, as checked after extension to \(\overline K\).

Write \(K'=K[v]\) by the primitive element argument in Lemma 4.2. Clear denominators in its monic minimal polynomial and a Bezout identity with its derivative. After a nonzero localization, \(A'=A[v]\) is finite free étale over \(A\), with generic fibre the field \(K'\). It is a domain because its monic polynomial presentation is free over \(A\) and embeds in \(K'\). The finite generic idempotents extend after inverting finitely many elements of \(A'\); their finite orthogonality and sum equations hold after shrinking, or directly by the generic injection coming from flatness. They split the base-changed smooth algebra into finitely many smooth factors. Each has geometrically integral generic fibre. Apply Lemma 4.2 to all factors and invert a common nonzero \(a\in A'\). At every point of \(D(a)\) the factors are exactly the geometric connected components.

The determinant of multiplication by \(a\) on the finite free \(A\)-module \(A'\) is nonzero, because this map is invertible on the generic field. Invert this determinant in \(A\). The adjugate makes \(a\) invertible on the whole finite étale cover. That cover is surjective, since a nonzero finite free algebra has nonzero fibres, and those fibres have points. Field-extension invariance from Lemma 4.1 now proves the same constant component number on this nonempty base open. This verifies the criterion on every irreducible closed base. Noetherian induction, removing such a nonempty open on each of finitely many irreducible components and then applying the induction hypothesis to their proper closed complement, gives a finite locally closed stratification with constant component count. This proves constructibility as a function, and in particular of its one-component locus. \(\square\)

This proves the smooth affine case needed from the free chain [055I](https://stacks.math.columbia.edu/tag/055I), [055H](https://stacks.math.columbia.edu/tag/055H), [055G](https://stacks.math.columbia.edu/tag/055G). The hypersurface and flat quotient arguments above supply the generic constancy input explicitly; none of those tags is being substituted for a proof.

**Lemma 4.4.** Suppose \(A=\varinjlim A_i\), \(A_0\) is Noetherian, and \(E\subset\operatorname{Spec}A_0\) is constructible. If the image of \(\operatorname{Spec}A\) lies in \(E\), the image of \(\operatorname{Spec}A_i\) lies in \(E\) at some finite stage.

**Proof.** Express the complement as a finite union of pieces \(V(J)\cap D(g)\), with \(J\) finitely generated. Its pullback has empty spectrum, so \((A/JA)_g=0\). This says \(g^m\in JA\) for some \(m\), with a finite expression in generators of \(J\). Its coefficients and the finite equality descend to a stage. The same localized quotient there is zero, so that complement piece has empty pullback. Take a common stage for the finitely many pieces. \(\square\)

This is a direct affine proof of the needed [Stacks 05F4](https://stacks.math.columbia.edu/tag/05F4) step.

**Theorem 4.5.** A smooth affine finite-presentation scheme with geometrically connected fibres over an arbitrary affine ring has a smooth affine model with geometrically connected fibres over a finitely generated \(\mathbf Z\)-algebra. Finitely many specified maps, group laws and closed immersions can be retained.

**Proof.** Descend the finite presentations and finite identities to \(A_0\), a finitely generated \(\mathbf Z\)-subalgebra of the given ring, using AG-MO-03. Retain smoothness by Section 3 and closed immersions by the earlier proved closed-immersion descent. On this Noetherian model let \(E\) be the locus of exactly one geometric connected component. It is constructible by Lemma 4.3. Its pullback contains the image of the original base, by field-extension invariance and the original hypothesis. Apply Lemma 4.4 to enlarge the coefficient ring to a finite stage whose whole image lies in \(E\). Pullback of the model at that stage has geometrically connected fibres and remains smooth. Previously descended finite identities and closed immersions remain true under this base change. \(\square\)

This is the consumed smooth affine case of [Stacks 05FI](https://stacks.math.columbia.edu/tag/05FI). It applies simultaneously to the smooth affine group and its smooth affine subgroup in the normalizer lemma. Projectivity of quotient fibres has not been imposed on unrelated fibres of the model.

## 5. A universal finite complex for a line bundle

The following is the previously written finite complex proof, retained here before its uses.

**Lemma 5.1.** Let \(A\) be Noetherian and \(C\) a complex of flat \(A\)-modules concentrated in \([a,b]\), with finite cohomology modules. There is a complex \(K\) of finite projective modules in \([a,b]\) and a quasi-isomorphism \(K\to C\) which remains a quasi-isomorphism after tensoring with every \(A\)-module.

**Proof.** Construct a bounded-above complex \(P\) of finite free modules and a map \(f:P\to C\), descending from degree \(b\). With terms above \(j\) chosen, the cone has terms

\[
D^i=C^i\oplus P^{i+1},\qquad
d(c,p)=(d_Cc+f(p),-d_Pp).
\]

Its cohomology is finite: the cone long exact sequence uses finite cohomology of \(C\) and finite cohomology of the finite portion of \(P\) chosen so far. Choose finitely many cocycles \((c_\ell,p_\ell)\) generating \(H^j(D)\). Let \(P^j\) be free on \(e_\ell\), and set \(f(e_\ell)=c_\ell\), \(d_P(e_\ell)=-p_\ell\). The cocycle equations give \(d_P^2=0\) and \(d_Cf=fd_P\). The new cone differential sends \((0,e_\ell)\) to \((c_\ell,p_\ell)\), killing \(H^j\) without changing higher cohomology. Continue to the left. Each degree stabilizes, giving a quasi-isomorphism \(P\to C\).

Its cone is acyclic, bounded above and termwise flat. Such a complex stays acyclic after every tensor: start at its last degree and descend through \(0\to Z^i\to D^i\to Z^{i+1}\to0\). The quotient is flat, so the kernel is flat and the sequence remains exact under tensor. Thus \(H^i(P\otimes_AM)=H^i(C\otimes_AM)\) for every \(M\).

Put \(Q=\operatorname{coker}(P^{a-1}\to P^a)\). The left tail is a free resolution of \(Q\), and its first positive homology after tensoring with every \(M\) is \(H^{a-1}(P\otimes_AM)=0\), because \(C\otimes_AM\) starts in degree \(a\). Consequently \(Q\) is flat: tensor that free resolution with a short exact sequence \(0\to M'\to M\to M''\to0\). Its free terms give a short exact sequence of complexes; the homology exact sequence and the just-proved degree-one vanishing give an injection \(Q\otimes M'\to Q\otimes M\). This is the definition of flatness.

The finite presentation of \(Q\) makes it locally finite free by [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Lemma 1.2. It is finite projective as follows. Take a surjection \(A^r\to Q\) and a finite principal cover on which it splits. A local splitting extends after multiplication by a power of that chart element, since Hom from a finite presented module commutes with localization: use its finite presentation and exact localization to identify the kernel describing Hom. Increase that power until its composite with the surjection is the same power times the identity globally; equality can be checked on finitely many generators. Thus there are maps \(\tau_i:Q\to A^r\) whose composites are \(f_i^{N_i}\operatorname{id}_Q\). These powers generate the unit ideal, since the \(D(f_i)\) cover. A linear combination of the \(\tau_i\) whose coefficients combine the powers to one is a global splitting. Hence \(Q\) is a direct summand of a finite free module and is finite projective. Set \(K^a=Q\), \(K^i=P^i\) for \(a<i\leq b\). The map to \(C\) factors through \(Q\) since \(C^{a-1}=0\). Truncation preserves cohomology, and the same acyclic flat cone argument proves the assertion after every tensor. \(\square\)

**Proposition 5.2.** Let \(X\to S\) be smooth projective of finite presentation and \(L\) invertible. If all positive cohomology of \(L\) on every geometric fibre vanishes, then \(f_*L\) is finite locally free, all positive higher direct images vanish, and these statements commute with every base change.

**Proof.** Work over \(S=\operatorname{Spec}A\). Section 3 gives a smooth projective model \(X_0\to\operatorname{Spec}A_0\), \(A_0\) Noetherian, and an invertible \(L_0\) pulling back to \(L\). A finite affine cover of \(X_0\) has affine intersections. Its section complex \(C_0\) computes cohomology by the earlier finite-cover and affine-vanishing proofs. Its terms are \(A_0\)-flat: an invertible module is projective over its chart algebra, and that algebra is base-flat by smoothness. Projective finiteness makes its cohomology finite. After every algebra base change the section complex is \(C_0\otimes_{A_0}B\), by affine modules and localization. Lemma 5.1 therefore gives a bounded finite projective \(K_0\) computing cohomology after every such change.

Put \(K=K_0\otimes_{A_0}A\), and trivialize its terms near a point \(s\). If a differential has an entry invertible at \(s\), shrink and use row and column operations to make it an identity block. The equation \(d^2=0\) makes the adjacent differentials zero on that block, splitting off a contractible pair \(A\xrightarrow{1}A\). After finitely many cancellations the remaining differentials vanish over \(\kappa(s)\). Each remaining free term tensored with \(\kappa(s)\) is then the cohomology in its degree. In positive degrees it is zero by the hypothesis and faithful field extension; in negative degrees it is zero because the section complex begins in degree zero. All remaining terms other than degree zero have rank zero. The degree-zero term is finite free. Cancelled pairs remain contractible under every tensor, so the same description computes all base changes. It proves the assertions on every affine open and every affine base change. The canonical maps from sections and the section complexes commute with restriction, so glue to the claimed direct-image and base-change isomorphisms. \(\square\)

Vanishing was required on the original fibres only. No vanishing on unrelated Noetherian model fibres, reduced-base assumption or flat-base-change assumption was used.

## 6. The smooth curve regular immersion calculation

The following retains the full independently authored CC0 proof of AG-QC-14, Sections 3–5, with its formerly general proper-finiteness input replaced by the projective proof already given in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md). Its injective and finite-cover foundations are proved in that preceding support, Sections 3–5. We first record the vector-bundle Ext identity used in the argument. For finite locally free \(V\), tensor-Hom adjunction gives \(\mathcal H om(V,I)=V^\vee\otimes I\). Tensoring by \(V\) is exact, so its right adjoint \(V^\vee\otimes-\) takes injectives to injectives: Hom into it is Hom from an exact functor into an injective. Applying this adjunction to an injective resolution gives

\[
\operatorname{Ext}^j_P(V,G)=H^j(P,V^\vee\otimes G).
\]

Hom into each injective is contravariantly exact. A short exact sequence in its first argument therefore gives a short exact sequence of Hom complexes, whose cohomology gives the connecting maps and long exact sequence used below.

### 6.0. Ambient projective-space trace and duality

Put \(P=\mathbf P^n_k\) for a field \(k\), and define
\[
\omega_P=\mathcal O_P(-n-1).
\]
Its identification with \(\det\Omega_P\) is explicit. On \(U_i=D_+(T_i)\), use the ordered frame \(\sigma_i=(-1)^i\bigwedge_{j\ne i}d(T_j/T_i)\). On \(U_0\cap U_i\), the substitution \(T_0/T_i=1/(T_i/T_0)\), \(T_j/T_i=(T_j/T_0)/(T_i/T_0)\) gives Jacobian determinant \((-1)^i(T_i/T_0)^{-n-1}\); thus \(\sigma_i=(T_i/T_0)^{-n-1}\sigma_0\). These are exactly the transitions of \(\mathcal O_P(-n-1)\), proving the identification. For \(n=0\), the differential determinant and every twist are both the one-dimensional trivial line on a point. The cohomological normalization uses the ordered standard affine cover
\(D_+(T_0),\ldots,D_+(T_n)\), with alternating Čech differential. For \(n\geq1\), the projective-space calculation gives
\[
H^n(P,\omega_P)=k\cdot\left[\frac1{T_0\cdots T_n}\right].
\]
Define the trace \(\operatorname{tr}:H^n(P,\omega_P)\to k\) by sending that class to one. For \(n=0\), \(P\) is a point; the same expression is the generator of the degree \(-1\) part of \(k[T_0,T_0^{-1}]\), so this convention still identifies its one-dimensional space of sections with \(k\).

Multiplication followed by this trace pairs
\[
H^0(P,\mathcal O(d))\ \times\
H^n(P,\mathcal O(-d-n-1))\longrightarrow k.
\]
For \(n\geq1\) and \(d\geq0\), the first basis consists of \(T^b\), where \(b_i\geq0\) and \(\sum b_i=d\). The matching top-cohomology basis consists of
\(T_0^{-b_0-1}\cdots T_n^{-b_n-1}\). Their products have trace one precisely for matching exponent vectors, and zero otherwise. For \(d<0\), both spaces in the trace pairing vanish. Thus the trace pairing is perfect for every \(d\). When \(n=0\), both spaces are one-dimensional for every twist, and multiplication has the same conclusion. Negative twists on a point do not vanish.

More generally, projective-space cohomology and this coefficient computation give perfect pairings
\[
H^j(P,\mathcal O(d))\ \times\
H^{n-j}(P,\mathcal O(-d-n-1))\longrightarrow k
\]
for all \(j\): intermediate groups vanish and the two end cases are the computed pairing and its transpose. Maps between direct sums of twists are matrices of homogeneous polynomials. Multiplication is associative, so these pairings commute with all such matrices, including matrices between different twists. This naturality is the part needed to pass from twists to arbitrary coherent sheaves.

#### Duality in degree zero

For any coherent \(F\), a morphism \(u:F\to\omega_P\) induces a functional on its top cohomology:
\[
\theta_F^0(u)=\operatorname{tr}\circ H^n(u).
\]
This construction is contravariantly natural in \(F\).

**Ambient Lemma 6.A.** The trace map is an isomorphism
\[
\operatorname{Hom}_P(F,\omega_P)
 \ \cong\ H^n(P,F)^\vee
\]
for every coherent \(F\).

**Proof.** Choose a surjection \(P_0\twoheadrightarrow F\) with \(P_0\) a finite sum of twists, by the proved finite generation by twists in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Proposition 8.2. Its coherent kernel \(K\) is likewise a quotient of a finite sum of twists \(P_1\). Thus
\(P_1\to P_0\to F\to0\) is a presentation. Hom into \(\omega_P\) gives
\[
0\to\operatorname{Hom}(F,\omega_P)
 \to\operatorname{Hom}(P_0,\omega_P)
 \to\operatorname{Hom}(P_1,\omega_P).
\]
The standard cover has \(n+1\) affine opens with affine intersections. Consequently cohomology of quasi-coherent sheaves vanishes above \(n\). The two short exact sequences defining this presentation therefore give
\[
H^n(P,P_1)\to H^n(P,P_0)\to H^n(P,F)\to0.
\]
Dualizing gives another left-exact sequence in the same direction as the Hom sequence. All spaces are finite-dimensional, by the proved projective finiteness in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Theorem 8.4. The maps \(\theta^0\) give a morphism of these sequences. The two maps for \(P_0,P_1\) are isomorphisms by the trace pairing, and commute with the presentation map by its polynomial-matrix description. Their kernels are therefore isomorphic, which proves the assertion. \(\square\)

Only two stages of a presentation were used. In particular, this argument does not claim that repeated coherent kernels eventually become sums of line bundles.

#### Serre duality in every degree

**Ambient Theorem 6.B (Serre duality on projective space).** For every coherent sheaf \(F\) and every integer \(i\), there are natural isomorphisms
\[
\operatorname{Ext}^i_P(F,\omega_P)
 \ \cong\ H^{n-i}(P,F)^\vee.
\]
They extend the trace map, using its fixed trace.

**Proof.** For \(i\geq0\), consider the contravariant cohomological sequences
\[
A^i(F)=\operatorname{Ext}^i_P(F,\omega_P),
\qquad B^i(F)=H^{n-i}(P,F)^\vee.
\]
Exactness of vector-space duality and vanishing above \(n\) make the second a contravariant delta functor starting in degree zero, just as Ext is. Choose \(q>0\) sufficiently large so that \(F(q)\) is generated by its sections and all positive cohomology of \(\omega_P(q)\) vanishes. There is an epimorphism
\[
Q=\mathcal O_P(-q)^{\oplus m}\twoheadrightarrow F
\]
with coherent kernel \(K\). The vector-bundle identity above and projective Serre vanishing in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Theorem 8.4 give \(A^j(Q)=0\) for every \(j>0\). The twist calculation gives \(B^j(Q)=0\) for every \(j>0\): if \(0\leq n-j<n\), the corresponding cohomology of a strictly negative twist vanishes, and if \(n-j<0\) it vanishes by convention. This also covers \(n=0\), where every positive \(B^j\) is zero.

Both long exact sequences consequently identify their degree-one value on \(F\) with the cokernel of their degree-zero map from \(Q\) to \(K\). Ambient Lemma 6.A identifies these cokernels. For \(i\geq2\), the sequences give
\[
A^i(F)\cong A^{i-1}(K),
\qquad B^i(F)\cong B^{i-1}(K).
\]
Induction gives the desired isomorphisms for every \(i\geq0\).

These isomorphisms are canonical. The epimorphisms just used efface all positive values of both delta functors. The following comparison gives uniqueness: a morphism in degree zero determines the cokernel map in degree one and then every dimension-shifted map. For two choices of epimorphism, take their fiber product over \(F\), which is coherent, and an epimorphism from sufficiently negative twists onto that fiber product. The resulting maps of short exact sequences compare both choices. The same construction over a morphism of coherent sheaves proves naturality, and compatibility with connecting maps follows from the exact sequences. Thus the induction is the unique extension of the trace map.

If \(i<0\), the left side vanishes, and the right side is cohomology above dimension \(n\), hence also zero. This proves the displayed duality for all integers. \(\square\)

The following direct DVR argument supplies this local algebra before the degree calculations.

**DVR Lemma 6.C.** A one-dimensional Noetherian normal local domain is a discrete valuation ring.

**Proof.** Let $(R,\mathfrak m)$ be such a ring and choose $0\ne a\in\mathfrak m$. Every prime containing $a$ is $\mathfrak m$, since any other nonzero prime would give a chain of length at least two. Thus the radical of $(a)$ is $\mathfrak m$. Finite generation of $\mathfrak m$ gives $\mathfrak m^n\subset(a)$ for some $n$: choose a power of each generator lying in $(a)$ and use the pigeonhole principle on monomials. Choose the least $n$ and $b\in\mathfrak m^{n-1}\setminus(a)$. Then $c=b/a\notin R$ and $c\mathfrak m\subset R$.

If $c\mathfrak m\subset\mathfrak m$, apply the determinant trick to multiplication by $c$ on the finite module $\mathfrak m$. Its resulting monic polynomial annihilates this module, hence is zero in $\operatorname{Frac}(R)$ because the domain has a nonzero element in $\mathfrak m$. Normality would imply $c\in R$, a contradiction. Consequently $cx$ is a unit for some $x\in\mathfrak m$. It follows that $\pi=c^{-1}=x/(cx)\in\mathfrak m$ and $\mathfrak m=\pi R$.

The intersection $N=\bigcap_j\pi^jR$ is zero. In fact $N$ is a finite ideal, since $R$ is Noetherian, and cancellation of $\pi\ne0$ shows $N=\pi N$: if $x=\pi y$ lies in every $\pi^{j+1}R$, then $y$ lies in every $\pi^jR$. Nakayama gives $N=0$. Repeated division of a nonzero nonunit by $\pi$ must therefore stop. Every nonzero element is uniquely a unit times $\pi^j$, and every nonzero ideal is generated by the element of smallest such exponent. This is the discrete valuation ring assertion. $\square$

**Lemma 6.1.** A closed immersion \(i:C\hookrightarrow\mathbf P^N_k\) of a smooth pure one-dimensional projective curve is locally cut out by a regular sequence of length \(c=N-1\), and

\[
0\to I/I^2\to i^*\Omega_{\mathbf P^N/k}\to\Omega_{C/k}\to0
\]

is exact.

**Proof.** First extend \(k\) to an algebraic closure. At a closed point the two local rings are regular, of dimensions \(N\) and one, by the proved smooth field criterion. AG-CA-14 Proposition 1.4 gives a regular sequence of \(c\) parameters generating the ideal. Their linear classes are precisely the kernel of the surjection of tangent cotangent spaces. Thus their differentials are independent in the ambient differential fibre. The conormal module is free on their classes: tensor the Koszul resolution with the quotient, or use its degree-one relations, to see that all relations among the generators have coefficients in the ideal. The conormal map therefore has rank \(c\) on a neighbourhood of that closed point. Its cokernel is \(\Omega_{C/k}\) by the proved differential conormal sequence. Since these finite type neighbourhoods cover every closed point, they cover the curve; every nonempty closed complement in a finite type scheme over a field has a closed point by the Nullstellensatz.

Here is the descent back to \(k\). The finite module \(I/I^2\) becomes locally free of rank \(c\) after this faithful field extension, so it is flat before extension: any kernel of a tensor injection vanishes after the faithfully flat field extension, hence vanishes already. A finite presented flat module is projective by the earlier module theorem. Locally choose a basis and lift it to \(c\) generators of \(I\). At each ambient local ring, \(I=(f_1,\ldots,f_c)+I^2\); Nakayama applied to the finite module \(I/(f_1,\ldots,f_c)\), with \(I\) in the maximal ideal, gives generation of \(I\). The corresponding Koszul complex becomes exact in positive degrees after the field extension, because any minimal \(c\)-generator list differs by an invertible matrix from the parameter list already obtained. Its finite cohomology modules therefore vanish before extension by faithful flatness. Equivalently the list is regular: the Koszul cone for the last generator makes multiplication by that generator surjective on every positive homology module of the preceding Koszul complex. Those modules are finite and the generator lies in the maximal ideal, so Nakayama kills them. The same exact sequence gives injectivity of the last generator on degree-zero homology. Induction proves regularity. Finally exactness of the conormal sequence descends by faithful flatness as well. \(\square\)

This is the field-curve case actually needed from the more general free [Stacks 067U](https://stacks.math.columbia.edu/tag/067U) regular immersion theorem. It uses the existing regular quotient proof, rather than importing the full syntomic arbitrary-base theorem.

**Theorem 6.2.** For such a curve and an invertible \(L\), there is a natural isomorphism

\[
H^1(C,L)^\vee\cong H^0(C,\Omega_{C/k}\otimes L^{-1}).
\]

**Proof.** The regular sequence Koszul resolution from Lemma 6.1, dualized into \(\omega_{\mathbf P^N}=\det\Omega_{\mathbf P^N/k}\), has cohomology only in degree \(c\), with that sheaf equal to

\[
i_*\bigl(L^{-1}\otimes i^*\omega_{\mathbf P^N}
\otimes\det(I/I^2)^*\bigr).
\]

The determinant comes from the top exterior term of the dual Koszul complex, so the star and the sign of the canonical twist are fixed. Taking determinants of the conormal exact sequence identifies \(i^*\omega_{\mathbf P^N}\otimes\det(I/I^2)^*\) with \(\Omega_{C/k}\). Here is the full consumed local-to-global comparison from AG-QC-14 Proposition 2.1, with its finite filtered-complex input supplied by [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Section 4. Resolve \(\omega_{\mathbf P^N}\) by injectives \(I^\bullet\) and put \(E^\bullet=\mathcal H om(i_*L,I^\bullet)\). Each term is flasque: on \(U\subset V\), extension by zero gives a stalkwise injection \(j_!((i_*L)|_U)\hookrightarrow(i_*L)|_V\), and injectivity of \(I^q|_V\) extends every morphism from that submodule. Thus Hom sections restrict surjectively. Form the double complex of sections of \(E^q\) on the finite standard affine intersections of projective space. Its rows have Čech cohomology only in degree zero, since the terms and all their open restrictions are flasque and the earlier finite-cover comparison applies. One filtration therefore identifies total cohomology with \(H^*\Gamma(E^\bullet)=\operatorname{Ext}^*_{\mathbf P^N}(i_*L,\omega_{\mathbf P^N})\).

On any affine intersection, choose a resolution of \(i_*L\) by finite free sheaves, allowing an infinite left tail; Noetherianity makes its successive kernels finite. The first-quadrant Hom double complex with \(I^\bullet\) compares its Hom into \(\omega\) with \(E^\bullet\). In the resolution direction injectivity makes Hom exact. In the other direction its finite free source reduces to finite sums of \(\omega\), whose positive cohomology on this affine is zero by affine vanishing. Hence the vertical cohomology of the section double complex is the section module of the locally calculated sheaf Ext. Lemma 6.1 and the dual Koszul calculation above show that it is zero except in degree \(c\). The other filtration therefore has only that row, the finite Čech complex of \(i_*(L^{-1}\otimes\Omega_{C/k})\). Each total degree has finitely many terms, so the finite filtration calculation gives convergence and no completion or infinite-product issue. In total degree \(c\) it gives

\[
\operatorname{Ext}^{c}_{\mathbf P^N}(i_*L,\omega_{\mathbf P^N})
=H^0(C,L^{-1}\otimes\Omega_{C/k}).
\]

Ambient Theorem 6.B, the full trace and dimension-shifting proof of AG-QC-14 Theorem 5.1 reproduced above, identifies the same group with \(H^{N-c}(\mathbf P^N,i_*L)^\vee=H^1(C,L)^\vee\). The Koszul determinant, conormal determinant and trace are natural, giving the stated isomorphism. \(\square\)

**Lemma 6.3 (divisors, Euler characteristic and genus).** Suppose now that \(k\) is algebraically closed and \(C\) is connected. Put \(g=\dim_k H^1(C,\mathcal O_C)\). For every invertible \(L\),

\[
\chi(C,L)=\deg L+1-g,\qquad
\deg\Omega_{C/k}=2g-2.
\]

A line bundle of negative degree has no nonzero section.

**Proof.** Smooth local rings are regular domains. Thus different irreducible components cannot meet, and the finitely many components are open and closed. Connectedness makes \(C\) integral. Projective finiteness makes \(H^0(C,\mathcal O_C)\) a finite-dimensional domain over \(k\). It is a field, since multiplication by a nonzero element is an injective endomorphism of a finite-dimensional vector space and hence is surjective. Algebraic closedness makes this field \(k\).

There are two affine opens covering \(C\). In a projective embedding choose a hyperplane not containing \(C\); its intersection with the curve is finite, since a proper closed subset of a Noetherian integral curve has dimension zero and finitely many points. Choose another hyperplane avoiding those finitely many points, possible because \(k\) is infinite and a finite union of proper linear subspaces does not exhaust its coefficient space. The complements of these hyperplanes on \(C\) are affine and cover \(C\). Their intersection is affine by separatedness. The proved finite Čech computation consequently gives \(H^q(C,L)=0\) for \(q>1\). All the remaining groups are finite by projective finiteness, so their Euler characteristic is defined and additive in short exact sequences.

A nonzero rational section of \(L\) exists by choosing a generator at the generic point. Each closed-point local ring is a DVR: a one-dimensional regular local ring has its maximal ideal generated by a parameter, and the direct DVR characterization is Lemma 6.C above, the actual AG-CA-15 Theorem 1.2 argument. Relative to a local generator, the section has an integer valuation. There are only finitely many nonzero valuations, since a finite trivializing affine cover represents it by rational functions with finitely many zeros and poles. These valuations define a divisor \(D=\sum_x n_xx\) and identify \(L\) with \(\mathcal O_C(D)\): at \(x\), the identification sends the local module \(\pi_x^{-n_x}\mathcal O_{C,x}\) to the section's generated fractional module. The descriptions agree at the generic point and hence on overlaps.

For every divisor and closed point there is an exact sequence

\[
0\longrightarrow\mathcal O_C(D)\longrightarrow\mathcal O_C(D+x)
\longrightarrow k_x\longrightarrow0.
\]

At \(x\) the quotient is \(\pi^{-n_x-1}R/\pi^{-n_x}R\cong k\); elsewhere it is zero. The skyscraper \(k_x\) has \(H^0=k\) and no higher cohomology (its restrictions are surjective, so the previously proved flasque acyclicity applies). Additivity, successively adding or subtracting points, gives

\[
\chi(C,\mathcal O_C(D))=\sum_xn_x+\chi(C,\mathcal O_C).
\]

This both proves that the integer \(\deg L=\sum n_x\) is independent of the rational section and gives the first formula. Tensor product adds these divisors, so degrees add and inversion negates degree. A nonzero regular section has only nonnegative valuations, which proves the negative-degree assertion.

Theorem 6.2 with \(L=\mathcal O_C\) gives \(h^0(\Omega_{C/k})=g\). The same theorem with \(L=\Omega_{C/k}\) gives \(h^1(\Omega_{C/k})=h^0(\mathcal O_C)=1\). Its Euler characteristic is therefore \(g-1\). The first formula applied to \(\Omega_{C/k}\) gives \(g-1=\deg\Omega_{C/k}+1-g\), as claimed. In particular \(T_C=\Omega_{C/k}^{-1}\) has degree \(2-2g\). \(\square\)

**Lemma 6.4 (degree under a separable curve map).** Let \(f:D\to C\) be a nonconstant map between smooth connected projective curves over algebraically closed \(k\), and suppose the function-field extension is separable of degree \(n\). Then \(f\) is finite and locally free of rank \(n\), and \(\deg f^*L=n\deg L\).

**Proof.** The extension is finite: both finitely generated function fields have transcendence degree one, so the larger field is generated by finitely many algebraic elements over the smaller one. Write it as \(E/F\). On an affine open \(\operatorname{Spec}R\subset C\), the ring \(R\) is a Noetherian normal domain. Its integral closure \(S\) in \(E\) is finite. Here is the full finiteness argument used in AG-MO-13 Theorem 4.1. A primitive element, proved in Lemma 4.2 above, has \(n\) distinct conjugates. The trace pairing on its power basis has matrix \(V^{\mathsf T}V\), for the Vandermonde matrix on these conjugates, so has nonzero determinant. Scale a field basis \(b_i\) by nonzero elements of \(R\) so it becomes integral: if an algebraic element has equation \(T^m+\sum_{j<m}a_jT^j\), choose one common denominator \(d\) and the equation for \(dT\) has coefficients \(d^{m-j}a_j\in R\). The map \(E\to F^n\), \(z\mapsto(\operatorname{Tr}(b_i z))_i\), is an isomorphism. For \(z\in S\) all these traces lie in \(R\): the conjugates of an integral element are integral, their symmetric coefficients lie in \(F\), and normality puts those coefficients, and hence their traces, in \(R\). Thus \(S\) is an \(R\)-submodule of the free trace lattice, and is finite by Noetherianity.

These closures localize correctly. If \(z\) is integral over \(R_a\), multiply it by a sufficiently high power of \(a\) in its monic equation to make that multiple integral over \(R\). The two inclusions then give \(S_a\) as the integral closure of \(R_a\). They glue to a finite normal curve \(C'\to C\) with function field \(E\). Its one-dimensional local rings are DVRs by Lemma 6.C; dimension one follows from lying over and incomparability for integral extensions, proved in AG-CA-05 Theorems 3.2–3.4.

The given map factors as \(D\to C'\): an integral element of \(S\) satisfies a monic equation in every local ring of \(D\) above this open, so belongs to each such normal local ring. It is therefore regular locally and defines the factorization; the fraction expression forces uniqueness and gluing. Conversely, choose an affine neighbourhood of the generic point of \(D\). Its finitely many algebra generators become fractions in the function field of \(C'\); clearing their finitely many denominators gives a morphism on a nonempty affine open of \(C'\), and hence a rational map \(C'\dashrightarrow D\). It extends over every point directly using a projective embedding of \(D\): at a DVR multiply the generic homogeneous coordinates by the inverse of their least parameter power, making all coordinates regular and one a unit. The finitely many defining homogeneous equations still vanish, so this is a map into \(D\), and the finitely many coordinates spread to a neighbourhood. The maps glue by the following equalizer calculation. The equalizer of two maps to the separated \(D\) is closed, since it is a pullback of its diagonal. If the maps agree on a dense open of the integral source, each local generator of its defining ideal is zero in the function field and therefore zero in the local domain. The equalizer is the whole source. Apply the same calculation to their composites, which agree with the identity on a dense open. Thus those composites are the identity everywhere. Thus \(D=C'\) and \(f\) is finite.

A finite torsion-free module over a DVR is free. For clarity, lift a residue-field basis of the module and use Nakayama for generation. A relation among these lifts can be divided by the least parameter power in its coefficients, using torsion-freeness; reduction would then give a nontrivial relation in the residue-field basis. No such relation exists. Applying this to \(S\) over each \(\mathcal O_{C,x}\) gives rank \([E:F]=n\).

The fibre over a closed point \(x\) has vector-space dimension \(n\). Its finite-dimensional algebra splits into its finitely many local factors: powers of the distinct maximal ideals are comaximal and kill the algebra's nilradical, so the Chinese remainder theorem gives the split. At a point \(y\) of this fibre, the target parameter has valuation \(e_y>0\); the local quotient of the source DVR has length \(e_y\). Residue fields are \(k\), so \(\sum_{f(y)=x}e_y=n\). Pulling back the local equation for \(x\) gives the divisor \(\sum e_y y\). Add the coefficients of an arbitrary divisor for \(L\) to obtain \(\deg f^*L=n\deg L\). \(\square\)

**Proposition 6.5.** A smooth connected projective curve over algebraically closed \(k\) dominated by \(\mathbf P^1_k\) has genus zero. A genus-zero smooth connected projective curve over such \(k\) is isomorphic to \(\mathbf P^1_k\).

**Proof.** First suppose \(f:\mathbf P^1\to C\) is separable of degree \(n\). The differential map \(f^*\Omega_{C/k}\to\Omega_{\mathbf P^1/k}\) is generically nonzero: the conormal differential sequence for the separable field extension has zero relative differentials by AG-CA-17 Lemma 7.1, so the map of the one-dimensional spaces of absolute differentials is an isomorphism. A generically nonzero map of line bundles on an integral smooth curve is injective and has an effective zero divisor \(R\). Its local matrix is a nonzero DVR element, whose valuation is the coefficient of that divisor. Thus

\[
-2=\deg\Omega_{\mathbf P^1/k}
=n(2g-2)+\deg R.
\]

Here the degree on \(\mathbf P^1\) is \(-2\), either by the two-coordinate calculation \(dz=-t^{-2}dt\), or by Lemma 6.3 and \(H^1(\mathbf P^1,\mathcal O)=0\) from AG-QC-04. Since \(n>0\) and \(R\) is effective, \(g\geq1\) is impossible.

In characteristic \(p>0\), an inseparable dominant map also yields a separable dominant map from a projective line. Regard \(k(C)\) as a subfield of \(k(t)\). Choose the largest \(e\) such that \(k(C)\subset k(t^{p^e})\). Such an \(e\) is bounded: for one nonconstant rational function of \(k(C)\), containment in \(k(t^{p^e})\) makes its coprime numerator and denominator powers of \(t^{p^e}\), so \(p^e\) is bounded by their maximum degree. Put \(z=t^{p^e}\). The kernel of \(d/dz\) on \(k(z)\) is exactly \(k(z^p)\). Indeed the basis \(1,z,\ldots,z^{p-1}\) over \(k(z^p)\) makes the derivative's kernel its constant summand; independence follows by clearing the polynomial denominators in a relation: the summands then have exponents in distinct congruence classes modulo \(p\), so every coefficient is zero. The same reduction writes every polynomial as such a sum, and inverting a nonzero polynomial preserves this finite field extension, so these elements are a field basis. Maximality supplies \(a\in k(C)\) with derivative nonzero. If \(a=P(z)/Q(z)\) in coprime form, the polynomial \(P(T)-aQ(T)\) has nonzero derivative at \(z\); the minimal polynomial of \(z\) over \(k(a)\) therefore has nonzero derivative and the extension is separable. The intermediate extension \(k(z)/k(C)\) is separable as well, since an element separable over a smaller field remains separable over an intermediate field. Its field embedding gives a rational map \(\mathbf P^1_z\dashrightarrow C\), extended everywhere by the homogeneous-coordinate DVR argument above. The separable calculation applies and gives genus zero.

Conversely let \(g=0\) and fix \(q\in C(k)\). For \(m\geq0\), Lemma 6.3 and duality give

\[
h^0(\mathcal O_C(mq))=m+1,
\]

because \(\Omega_{C/k}(-mq)\) has degree \(-2-m<0\). Choose \(x\) complementing the constants in \(H^0(\mathcal O_C(q))\). It is a rational function with its only pole at \(q\), of exact order one. The functions \(1,x,\ldots,x^m\) have different pole orders and hence are linearly independent; their number is \(m+1\), so they form the displayed space's basis.

Every rational function \(h\) lies in \(k(x)\). To see this without a degree-one-map assertion, list its finitely many poles outside \(q\). At each such \(a\), the function \(x-x(a)\) is nonzero and has positive valuation. Multiply \(h\) by sufficiently large powers of all these functions to cancel its poles there. The product then lies in some \(H^0(\mathcal O_C(mq))\), and therefore is a polynomial in \(x\). Dividing by the multiplying polynomial proves the claim. Thus \(k(C)=k(x)\). Inverse rational maps between \(C\) and \(\mathbf P^1\) extend at every DVR by their projective homogeneous coordinates and agree globally by the equalizer argument. They are inverse isomorphisms. \(\square\)

These proofs must be placed before AG-RG-01. In particular, for a nonempty finite boundary divisor \(D\) on a smooth completion, \(\deg T_C(-D)=2-2g-\deg D<0\) when \(g\geq1\), and Lemma 6.3 gives \(H^0(C,T_C(-D))=0\). This is the exact degree-and-genus input used by the one-dimensional unipotent classification; none of it is deferred to a later group lesson.

## 7. Applying the proof route in the group lessons

The normalizer construction in AG-RG-03 uses Theorem 4.5 to choose smooth affine group and subgroup models with geometrically connected fibres; its finite group equations and closed immersion descend in the same finite list. The projective homogeneous quotient proof uses Theorem 2.3 on its actual projective closure and Corollary 2.4 for the formal idempotent. Lemma 1.3 supplies faithful flatness of local completion, the actual argument of AG-CA-19 Theorem 3.2. Section 5 supplies the line bundle cohomology statement over arbitrary, including nonreduced, bases used in AG-RG-03 and AG-RG-06. Section 6 supplies the smooth curve duality, divisor degrees, genus calculation and domination by a projective line used in AG-RG-01 and AG-RG-03; it must precede AG-RG-01.

For AG-RG-06's use of sufficiently large powers of an ample line bundle, the exact earlier embedding proofs are AG-RG-S01, Lemma 8.1 and Lemma 8.3: finitely many nonvanishing sections with affine domains, denominator clearing for their coordinate generators, and an immersion from those generators. [AG-RG-S01, Corollary 7.B](AG-RG-S01.html#projective-properness) turns that immersion into a closed immersion when the source is proper. AG-RG-S01, Theorem 8.5 treats every sufficiently large power by applying its projective finiteness and vanishing argument to all finitely many residue classes modulo the embedding exponent.

## Freely readable sources and history

Mathematical source material for this adapted lesson is the freely readable [Stacks Project](https://stacks.math.columbia.edu/), especially the exact tags linked next to the proved statements. The cached editable chapters are pinned at commit `a04446e57ec1fbc252a871afcec7752fb2807b14`; the cache includes their original license. The proof differences were written on 5 October 2026. The formal functions argument retains the previously written finite Rees and kernel argument in programme AG-QC-10, specialized to projective schemes to use the full earlier AG-QC-05 proof. The finite complex and curve arguments retain the previously written programme bridges, with the formerly external smooth model and curve immersion steps supplied here. No paid book supplies an argument or a public citation in this lesson.

## History

Source: *The Stacks Project*, the Stacks Project authors, copyright (C) 2005–2025 Johan de Jong, published openly by the Stacks Project under the GNU Free Documentation License, version 1.2 or later. Exact freely readable source tags are identified in this lesson.

Modified edition: *Projective cohomology and smooth affine models*, 5 October 2026. Author and publisher of the modified edition: GPT-6.1 Sol (OpenAI), Codex, Ultra setting, for Open mathematics courses. Formal functions, affine smooth models, universal cohomology complexes and the curve arguments; missing intermediate proof steps supplied. Self-checked by the writing AI. Original contributions retain their separate CC0 dedication, and adapted Stacks expression retains its GNU FDL terms.

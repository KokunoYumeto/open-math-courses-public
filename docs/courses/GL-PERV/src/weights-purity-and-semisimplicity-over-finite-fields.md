# Weights, purity and semisimplicity over finite fields

*AI-generated exposition by GPT-6.1 Sol and GPT-6 Astra (OpenAI), October 2026. Public domain (CC0).*

There are three different questions behind the word purity. What sizes can Frobenius eigenvalues have? How do those sizes change with cohomological degree? Which extensions disappear when Frobenius is forgotten? A punctured line, a unipotent matrix and a singular projective curve separate these questions. We will use their calculations to organize the weight theorems and then derive the perverse consequences.

Throughout, \(k=\mathbb F_q\), \(\ell\ne\operatorname{char}k\), and \(\Lambda=\overline{\mathbb Q}_\ell\). All schemes have finite type over \(k\); maps in the operation statements are separated. A subscript \(0\) retains the \(k\)-structure, and its omission denotes geometric base change. We use geometric Frobenius, acting on \(\Lambda(1)\) by \(q^{-1}\). Our convention is \(\mathcal H^b(K[r])=\mathcal H^{b+r}(K)\).

The sheaf tools come from [Constructible complexes on algebraic varieties](constructible-complexes-on-algebraic-varieties.md), [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and [Affine morphisms, Artin vanishing and perverse cohomology](affine-morphisms-artin-vanishing-and-perverse-cohomology.md). The ordinary and adic operation, trace, duality and weight foundations are specified where used. Their full prerequisite proofs remain required. Appendix A contains the curve and cover arguments supporting the perverse weight criterion. Appendix B supplies the pencil geometry. Appendix C computes its three arithmetic local contributions and the specialization sequence. Appendix D derives the general compact-support estimate by a family filtration and dimension induction. Appendix E proves mixed stability of the remaining operations, beginning with ordinary direct image before duality. Each appendix states the ordinary cohomological inputs it uses.

## 1. Two obstructions to an unqualified splitting statement

Start on a point. Let geometric Frobenius act on a two-dimensional vector space by
\[
F(e_1)=e_1,\qquad F(e_2)=e_2+e_1.                         \tag{1.1}
\]
This is an actual continuous arithmetic representation. If \(N(e_2)=e_1\) and \(N(e_1)=0\), the map \(a\mapsto1+aN\) from \(\mathbb Z_\ell\) is a continuous homomorphism because \(N^2=0\). Compose with the procyclic Galois group's \(\mathbb Z_\ell\)-quotient, choosing the generator sign for geometric Frobenius. Every Frobenius eigenvalue is one. Nevertheless no line complementary to \(\Lambda e_1\) is invariant: a generator \(e_2+ce_1\) acquires the extra term \(e_1\). The representation is an arithmetic nonsplit extension of two trivial lines. Its underlying geometric object is simply a vector space and splits.

Now remove a point from the affine line. Write \(j:\mathbb G_m\hookrightarrow\mathbb A^1\) and \(i:\{0\}\hookrightarrow\mathbb A^1\). Compact-support localization, using \(H_c^2(\mathbb A^1)=\Lambda(-1)\) and no other nonzero affine-line compact cohomology, gives
\[
H_c^1(\mathbb G_m)=\Lambda,\qquad H_c^2(\mathbb G_m)=\Lambda(-1).
                                                               \tag{1.2}
\]
The first group is the image of \(H^0(\{0\})\) in the long exact sequence; the second maps isomorphically to the affine-line group. Smooth curve duality then gives
\[
H^0(\mathbb G_m)=\Lambda,\qquad H^1(\mathbb G_m)=\Lambda(-1).
                                                               \tag{1.3}
\]
Thus degree-one ordinary cohomology has eigenvalue \(q\), while degree-one compact cohomology has eigenvalue one. Their weights are two and zero. The difference is geometric: this space is not proper.

At the sheaf level the same puncture produces
\[
0\longrightarrow\Lambda_{\mathbb A^1}[1]
\longrightarrow Rj_*\Lambda[1]
\longrightarrow i_*\Lambda(-1)\longrightarrow0.             \tag{1.4}
\]
Affine-open exactness makes the three objects perverse. The puncture calculation gives stalk groups \(\Lambda\) in degree \(-1\) and \(\Lambda(-1)\) in degree zero, and localization gives \(i^!Rj_*=0\). These identify the quotient in (1.4). A splitting would supply a nonzero map from the supported quotient back to the middle term. Adjunction identifies that Hom group with a Hom into its zero costalk. Hence (1.4) stays nonsplit even geometrically. Duality, followed by twist \((-1)\), gives the other nonsplit sequence
\[
0\longrightarrow i_*\Lambda\longrightarrow j_!\Lambda[1]
\longrightarrow\Lambda_{\mathbb A^1}[1]\longrightarrow0.     \tag{1.5}
\]
The ordinary direct-image sheaf \(j_*\Lambda\) is just \(\Lambda_{\mathbb A^1}\): each punctured strict local neighbourhood is connected. It is the derived object in (1.4) that carries the two different perverse weights. We next fix the convention that makes this distinction precise.

## 2. Measure weights on stalks and costalks

At a closed point of degree \(e\), a Frobenius eigenvalue has weight \(a\) if it is algebraic over \(\mathbb Q\) and every complex conjugate has modulus \(q^{ea/2}\). A constructible sheaf is pointwise pure of weight \(a\) if all its stalk eigenvalues satisfy this condition. A mixed sheaf has a finite filtration with pointwise pure quotients of integral weights. The inequalities on a mixed sheaf refer to the weights of these quotients. Jordan blocks are permitted: (1.1) is pointwise pure of weight zero.

For a fixed embedding \(\iota:\overline{\mathbb Q}_\ell\to\mathbb C\), one can instead impose only the corresponding absolute-value condition. This is \(\iota\)-purity. Some curve arguments in Appendix A use real \(\iota\)-weights; they do not silently supply integral weights or bounds at all embeddings. Unless qualified in this way, mixedness below uses integral weights and all conjugates.

Let \(D^b_m(X_0,\Lambda)\) consist of bounded constructible complexes with mixed ordinary cohomology. Define
\[
\begin{aligned}
K_0\le w&\quad\Longleftrightarrow\quad
       \mathcal H^bK_0\text{ has weights }\le w+b\text{ for all }b,\\
K_0\ge w&\quad\Longleftrightarrow\quad D_{X_0}K_0\le-w.
\end{aligned}                                                \tag{2.1}
\]
The complex is pure of weight \(w\) when both hold. The minus sign in the dual condition is essential. These are Deligne's complex-weight conventions in Weil II, 6.2.2–6.2.4.

Equivalently, at every closed point, the groups \(H^b(i_x^*K_0)\) have weights at most \(w+b\), and \(H^b(i_x^!K_0)\) have weights at least \(w+b\). For the upper test use exactness of stalks. For the lower one use \(i_x^*DK_0=D(i_x^!K_0)\): point duality reverses degrees and inverts eigenvalues. These are different tests on a variety. Only on a point do stalk and costalk agree, making degree-\(b\) cohomology of a pure complex pointwise pure of weight \(w+b\).

Three bookkeeping rules now have short proofs:
\[
\mathrm{wt}(K_0[r])=w+r,\qquad
\mathrm{wt}(K_0(m))=w-2m,\qquad
\mathrm{wt}(DK_0)=-w.                                      \tag{2.2}
\]
For the first, substitute \(b+r\) in the upper test; duality sends the shift to \([-r]\), giving the lower test. For the second, every degree-\(e\) eigenvalue is multiplied by \(q^{-em}\), and \(D(K(m))=(DK)(-m)\). Biduality proves the third. On a smooth \(d\)-fold the formula \(D(L[d])=L^\vee(d)[d]\) therefore shows that a weight-\(a\) lisse sheaf becomes pure perverse of weight \(a+d\) in shift \([d]\).

For projective space, the earlier projective-space calculation is
\[
H^{2r}(\mathbb P^n)=\Lambda(-r)\ (0\le r\le n),\qquad
H^{2r+1}(\mathbb P^n)=0.                                   \tag{2.3}
\]
The Frobenius-invariant hyperplane class belongs to \(H^2(\mathbb P^n,\Lambda(1))\), so its untwisted \(r\)-th power has eigenvalue \(q^r\). Its weight is \(2r\), exactly its degree. Consequently the global cohomology complex has weight zero; the sheaf \(\Lambda_{\mathbb P^n}[n]\) has weight \(n\). These two assertions concern different objects.

Equations (1.3) cannot fit any single complex weight: degree zero forces \(w=0\), whereas degree one would force \(w=1\). Likewise the generic part of \(Rj_*\Lambda[1]\) forces weight one, but its degree-zero boundary stalk has weight two. Sequence (1.4) has constituents of weights one and two; its increasing weight filtration will be its displayed subobject followed by the whole object. In (1.5) the constituents have weights zero and one. A filtration ordered by weight need not split.

The punctured-line calculation extends without a new weight theorem. Remove \(r\ge1\) distinct \(k\)-rational points \(D\) from \(\mathbb P^1\), and put \(U=\mathbb P^1\setminus D\). Localization gives
\[
0\to\Lambda\xrightarrow{(1,\ldots,1)}\Lambda^r
\to H_c^1(U)\to0,\qquad H_c^2(U)=\Lambda(-1).
\]
Thus \(H_c^1(U)=\Lambda^{r-1}\), and duality gives \(H^1(U)=\Lambda(-1)^{r-1}\). Over \(\mathbb F_Q\), where \(Q=q^n\), the compactly supported alternating trace is \(Q-r+1\), matching the count of the remaining points. Here the boundary term, its Frobenius and its weight are visible in the diagonal map itself.

## 3. Singularities change the constant sheaf and the intersection complex differently

### The two branches of a rational node

Suppose \(q\) is odd and consider
\[
C_0:\ y^2z=x^2(x+z),\qquad
\nu([s:t])=[s(t^2-s^2):t(t^2-s^2):s^3].                     \tag{3.1}
\]
The three coordinates have no common zero and satisfy the cubic equation. Outside the node \([0:0:1]\), the rational inverse is \([s:t]=[x:y]\); the infinity chart completes it. The two points mapping to the node are \([1:1]\) and \([1:-1]\). The proper map has finite fibres, is birational, and its smooth source is normal, so it is the finite normalization. This uses the finite-normalization facts from the earlier curve example.

At the node the normalized direct image \(\nu_*\Lambda[1]\) has stalk \(\Lambda^2[1]\). Its costalk is \(\Lambda(-1)^2\) in degree one by proper duality on the smooth source. The strict boundary characterization therefore identifies it with \(\operatorname{IC}_{C_0}\). Its global intersection cohomology is
\[
IH^0(C)=\Lambda,\qquad IH^1(C)=0,\qquad IH^2(C)=\Lambda(-1).
                                                               \tag{3.2}
\]
The constant sheaf has a different answer. Subtracting the values on the two branches gives an exact sequence
\[
0\to\Lambda_{C_0}\to\nu_*\Lambda_{\mathbb P^1}
\to i_*\Lambda\to0.                                       \tag{3.3}
\]
Its map on global constants is zero. The long exact sequence consequently gives ordinary \(H^0=\Lambda\), \(H^1=\Lambda\), \(H^2=\Lambda(-1)\). The extra degree-one class has eigenvalue one, hence weight zero. In the perverse heart (3.3), shifted by one, becomes
\(0\to i_*\Lambda\to\Lambda_{C_0}[1]\to\operatorname{IC}_{C_0}\to0\).
The constant perverse complex has a weight-zero boundary piece and a weight-one IC quotient.

Over \(\mathbb F_Q\), normalization removes two rational points and inserts one, so \(\#C_0(\mathbb F_Q)=Q\). The normalized IC trace is \(-1\) at every smooth point and \(-2\) at the node. Their sum is \(-(Q-1)-2=-(Q+1)\), also the alternating trace of (3.2) after shift \([1]\). The negative sign records the normalization, not a negative Frobenius eigenvalue.

### A threefold with one exceptional projective line

Fix \(F_2\subset k^4\) of dimension two and set
\[
X_0=\{W\in\operatorname{Gr}(2,4):\dim(W\cap F_2)\ge1\}.
                                                               \tag{3.4}
\]
Choose \(F_2=\langle e_1,e_2\rangle\). The equation is \(p_{34}=0\) inside the Plücker quadric, hence \(p_{13}p_{24}=p_{14}p_{23}\) in \(\mathbb P^4\). All four partial derivatives vanish precisely at the point with only \(p_{12}\ne0\). Thus \(X_0\) is a threefold smooth away from the vertex \(v=F_2\), in every characteristic.

Resolve it by remembering a line:
\[
Y_0=\{(L,W):L\subset F_2,\ \dim L=1,\ L\subset W\},\qquad
\pi(L,W)=W.                                                \tag{3.5}
\]
Over \(\mathbb P(F_2)\), the second choice is a line in \(k^4/L\), so \(Y_0\) is a smooth projective \(\mathbb P^2\)-bundle over \(\mathbb P^1\). Off \(v\), its inverse is \(W\mapsto(W\cap F_2,W)\), a morphism because the kernel has constant rank one there. The fibre at \(v\) is \(\mathbb P^1\).

For \(P_0=R\pi_*\Lambda[3]\), proper base change and duality give
\[
\begin{array}{c|cc}
&\text{degrees}&\text{nonzero groups}\\ \hline
i_v^*P_0&-3,-1&\Lambda,\ \Lambda(-1)\\
i_v^!P_0&1,3&\Lambda(-2),\ \Lambda(-3).
\end{array}                                                \tag{3.6}
\]
Indeed \(DP_0=P_0(3)\), so dualizing the twisted stalk gives the displayed costalk. On the smooth open \(P_0=\Lambda[3]\). The strict boundary bounds prove \(P_0=\operatorname{IC}_{X_0}\), using neither decomposition nor a general small-map theorem. They also exhibit its weight-three upper and lower tests directly: the stalk weights are \(0,2\), while the costalk weights are \(4,6\). Both tests are equalities in their nonzero degrees.

The \(\mathbb P^2\)-bundle has \((Q+1)(Q^2+Q+1)\) rational points. Replace its exceptional \(Q+1\) points by the vertex to obtain
\[
\#X_0(\mathbb F_Q)=Q^3+2Q^2+Q+1.                           \tag{3.7}
\]
The projective-bundle cohomology basis gives the ranks \(1,2,2,1\) in degrees \(0,2,4,6\), with Tate coefficients \(\Lambda(-r)\) in degree \(2r\). Because of the proved IC identification, these are \(IH^{2r}(X)\); odd groups vanish. Their normalized global trace is \(-(1+2Q+2Q^2+Q^3)\). Subtract the smooth contribution \(-(Q^3+2Q^2+Q)\); the remaining vertex trace is \(-(1+Q)\), also obtained from (3.6). The point count alone would give the constant-sheaf trace. Recovering IC requires its geometric identification or its independently computed global cohomology as well.

## 4. From ordinary estimates to purity of intermediate extensions

**Theorem 4.1 (Deligne's compact-support estimate, relative to the stated ordinary foundations).** For a separated finite-type \(f:X_0\to Y_0\) and a mixed sheaf \(F_0\) of weights at most \(a\),
\[
R^rf_!F_0\text{ is mixed of weights at most }a+r.             \tag{4.1}
\]
Appendix D derives (4.1) from the optimal curve estimate, constructing actual finite mixed filtrations and a decreasing dimension induction. Its ordinary foundations, and those of Appendices A–C, remain explicitly required. A further assertion is that mixed constructible categories are stable under \(f^*,f^!,Rf_*,Rf_!\), tensor product, derived internal Hom and Verdier duality. Appendix D gives mixedness for \(Rf_!\), inverse image and tensor product. Appendix E proves ordinary direct-image mixedness by a generic-dimension induction, then derives duality, exceptional inverse image and internal Hom. This order avoids assuming dual mixedness in the direct-image proof. The primary loci are Weil II, 3.3.1 and 6.1.1–6.1.11. These deductions retain the explicitly specified ordinary geometric and adic foundations as hypotheses.

Here is the precise passage to complexes. The spectral sequence
\[
R^uf_!\mathcal H^vK_0\Longrightarrow\mathcal H^{u+v}Rf_!K_0
                                                               \tag{4.2}
\]
has upper bound \(w+v+u\) when \(K_0\le w\). For each total degree this is one common bound on every term. Subquotients and the finite abutment filtration preserve it. Dualize the result to obtain the lower estimate for \(Rf_*\). Exactness of ordinary inverse image gives the upper bound for \(f^*\): a residue-field extension raises Frobenius eigenvalues to a power and multiplies the residue degree by the same number. Duality gives the last operation. In this notation,
\[
\begin{array}{c|c}
f^*,Rf_!&K_0\le w\ \Longrightarrow\ \text{output}\le w\\
f^!,Rf_*&K_0\ge w\ \Longrightarrow\ \text{output}\ge w.
\end{array}                                                \tag{4.3}
\]
If \(f\) is proper, its two direct images agree. Applying the two rows proves that \(Rf_*\) preserves pure complex weight. The punctured-line computation explains why the same conclusion is unavailable for a general nonproper direct image.

The step from these ordinary bounds to perverse subquotients uses **Gabber's criterion**: a mixed perverse \(P_0\) has lower bound \(w\) exactly when \(H^0(V,P)\) has weights at least \(w\) on every affine étale \(V_0\to X_0\). Appendix A, Theorem A.3, gives the cover-growth and hyperplane proof, retaining its ordinary prerequisites. Its mixedness argument also proves that perverse truncations preserve mixedness and that mixed perverse objects form a Serre subcategory.

**Proposition 4.2.** Each weight bound is preserved by subobjects and quotients in the mixed perverse heart.

**Proof.** A quotient preserves the lower bound: on an affine test, Artin vanishing makes its \(H^0\) a quotient of the original \(H^0\), so the criterion applies. Given \(0\to A_0\to P_0\to B_0\to0\) with \(P_0\ge w\), first obtain \(B_0\ge w\). On every affine test, the segment \(H^{-1}(V,B)\to H^0(V,A)\to H^0(V,P)\), together with (4.3), gives \(A_0\ge w-1\).

Amplify this bound by an exterior tensor power. Over our coefficient field, stalk and costalk Künneth add the perverse degree bounds on each product stratum; hence an exterior product of two heart objects lies in the heart. Finite truncation then proves t-exactness with one heart factor, and its long exact sequence gives exactness on the heart. Tensor weight bounds add by the same stalk formula and duality. Thus \(A_0^{\boxtimes m}\subset P_0^{\boxtimes m}\) has lower bound \(mw-1\). If an eigenvalue in costalk degree \(b\) of \(A_0\) had weight \(c<w+b\), its \(m\)-fold tensor would have degree \(mb\) and weight \(mc\). The bound would require \(mc\ge mw-1+mb\), impossible for large \(m\). Therefore \(A_0\ge w\). Duality exchanges subobjects and quotients and reverses weight inequalities, proving both upper-bound assertions. \(\square\)

Let \(L_0\) be pointwise pure of weight \(a\) on a smooth dense \(d\)-dimensional open. On an affine neighbourhood shrink to a dense principal open where its IC is the intermediate extension. The shifted lisse object has weight \(a+d\). Affine \(j_!\) and \(Rj_*\) are perverse and have the respective upper and lower bounds \(a+d\). Their image is a quotient of the former and a subobject of the latter, so Proposition 4.2 proves
\[
\operatorname{IC}_{X_0}(L_0)\text{ is pure of weight }a+d.    \tag{4.4}
\]
Transitivity of intermediate extension identifies the result after shrinking, and the stalk/costalk tests make it local on the ambient space. This proves the general assertion from the specified inputs. In Section 3 the two explicit IC computations already verified those tests directly.

A simple mixed perverse object is consequently pure. Its description as an IC gives an irreducible local system on a regular dense open. Shrink until the ordinary mixed filtration is lisse. Irreducibility leaves one pure step, and (4.4) applies. This uses the simple-object and finite-length theorems in the preceding perverse lessons, together with Appendix A's Serre argument.

## 5. Frobenius on extensions and the weight filtration

For \(A_0\le\alpha\) and \(B_0\ge\beta\), tensor and duality give
\(R\mathcal Hom(A_0,B_0)=D(A_0\otimes DB_0)\ge\beta-\alpha\).
Apply ordinary direct image to the point in (4.3) and read degree \(r\). The result is
\[
\operatorname{Hom}_{D^b_c(X)}(A,B[r])
\text{ has weights }\ge\beta-\alpha+r.                     \tag{5.1}
\]
These are geometric Hom groups carrying Frobenius. Their fixed parts govern arithmetic morphisms.

### Continuous Galois descent for arithmetic extensions

**Lemma 5.G (the actual arithmetic derived-Hom complex).** Let \(a:X_0\to s=\operatorname{Spec}k\) be the structural map, let \(X=X_0\times_k\bar k\), and let \(A_0,B_0\in D^b_c(X_0,\Lambda)\). Write \(A,B\) for their geometric pullbacks and \(F\) for geometric Frobenius. There is a natural identification
\[
\begin{aligned}
C_0&=R\operatorname{Hom}_{X_0}(A_0,B_0),
&C&=R\operatorname{Hom}_{X}(A,B),\\
C_0&\simeq\operatorname{Cone}(F-1:C\longrightarrow C)[-1].
\end{aligned}
\tag{5.G1}
\]
The map from \(C_0\) to \(C\) in the resulting triangle is ordinary geometric restriction. The action is on the derived complex, not just a separately chosen action on each cohomology group.

We use the standard finite-coefficient-field meaning of \(D^b_c(-,\bar{\mathbf Q}_\ell)\): its objects, morphisms and finite diagrams are obtained by extension from finite extensions \(E/\mathbf Q_\ell\), with morphisms identified after a further finite coefficient extension. Thus a finite diagram under discussion has a common field of definition. This is not the category of arbitrary discrete \(\bar{\mathbf Q}_\ell\)-modules, nor a change to completed algebraic-closure coefficients. First prove the assertion for such an \(E\); we return to \(\Lambda\) below.

**Identifying the geometric fibre.** Form the constructible complex on the point
\[
\begin{aligned}
H_0&=Ra_*R\mathcal Hom_{X_0}(A_0,B_0),\\
\bar s^*H_0&\simeq R\Gamma\bigl(X,R\mathcal Hom_X(A,B)\bigr)=C.
\end{aligned}
\tag{5.G2}
\]
Here the first expression is bounded constructible by BV.5, the rational identification of BX.7, and [Corollary E.2n.1](#one-open-for-completed-and-rational-coefficients). The last corollary applies with parameter base \(s\): its dense open must be all of \(s\). Consequently its ordinary base-change comparison applies to the structural map and to every finite-type open immersion needed below, with no shrinking or properness assumption on \(X_0\).

One must also justify internal Hom in the second line of (5.G2); inverse image does not commute with every internal Hom. Use the finite constructible stratification and local finite perfect models of BO.6 and BX.3. On a stratum where the first argument is a local finite complex of finite free modules, internal Hom is its dual tensor the target. Pullback commutes with that expression. For an open immersion \(j\) with closed complement \(i\), the adjunctions give
\[
\begin{aligned}
R\mathcal Hom(j_!L,B_0)&\simeq Rj_*R\mathcal Hom(L,j^*B_0),\\
R\mathcal Hom(i_*L,B_0)&\simeq i_*R\mathcal Hom(L,i^!B_0),\\
i_*i^!B_0&\simeq\operatorname{Fib}(B_0\longrightarrow Rj_*j^*B_0).
\end{aligned}
\tag{5.G3}
\]
The last identity is the open–closed localization proved in BX.2. Field-extension pullback commutes with the displayed ordinary open direct image by E.2n.1, and with closed direct image by its proper comparison. It is exact, so preserves the displayed fibre; applying closed inverse image identifies the exceptional pullback comparison as well. Now devissage of the *first* Hom argument by its finite open–closed support triangles reduces internal-Hom base change to the local perfect case. All maps are induced by evaluation and adjunction; the isomorphism obtained is the canonical internal-Hom comparison. Applying the structural ordinary comparison proves (5.G2). Its naturality under automorphisms of \(\bar k/k\) retains the actual Galois action.

**Continuous coefficients at the point.** Let \(O\) be the valuation ring of \(E\), with uniformizer \(\pi\). Choose a bounded constructible integral model of \(H_0\) using BX.6–BX.7. The coefficient-ring adjunction BW.2–BW.3 identifies it with a complete constant-\(O\) complex \(P\). At the finite-field point, BU.4, (BU.14) realizes \(P\) by a bounded complex of strict adic heart objects. This uses realization **only at a point**, where it is proved; it does not assume realization for a positive-dimensional \(X_0\).

Here is the actual coefficient calculation being used. Let \(T\) denote arithmetic Frobenius. For a finite continuous coefficient module \(N\), the finite-field lesson, Sections 1–3 and 6 identifies sheaf cohomology with continuous cochains and computes finite cyclic inflation. BU.1 records the natural quasi-isomorphism
\[
C^\bullet_{\mathrm{cont}}(\widehat{\mathbf Z},N)
\longrightarrow [N\xrightarrow{T-1}N],
\qquad c^1\longmapsto c^1(T),
\tag{5.G4}
\]
with identity in degree zero, zero in degrees at least two, and target in degrees zero and one. Explicitly, inflation from a cyclic quotient of order \(d\) to one of order \(ed\) multiplies degree-\(r\) representatives by \(e^{\lfloor r/2\rfloor}\). A sufficiently divisible \(e\) kills higher finite-torsion cohomology, while degree-one inflation is the identity and the enlarged norm is zero. This proves the quasi-isomorphism, naturally in the coefficient module; it is not a calculation for the abstract underlying group.

For a finite \(O\)-module \(M\) with continuous action, apply (5.G4) to \(M/\pi^nM\). The surjective quotient transitions commute with that cochain map. BU.2 takes their homotopy inverse limit and obtains the actual two-term complex on \(M\); the termwise surjectivity removes the potential derived-limit contribution at this step. Let \(M^\bullet\) be the bounded complex of these modules corresponding to the chosen heart model of \(P\). Naturality makes the two-term comparisons a map of double complexes. Finite totalization in the bounded heart direction gives
\[
\begin{aligned}
R\Gamma(s,P)&\simeq\operatorname{Cone}
 (T-1:M^\bullet\longrightarrow M^\bullet)[-1],\\
R\Gamma(\bar s,P|_{\bar s})&\simeq M^\bullet.
\end{aligned}
\tag{5.G5}
\]
The geometric-point fibre is exact on this heart, so the second line is the termwise underlying-module complex. BU.14 compares actual higher morphisms, making the result independent in the derived category of the chosen bounded heart model. The construction also respects the augmentation giving restriction to the geometric point. Finally BX.4 commutes sections with the uniformly bounded-below multiplication-by-\(\pi\) tower. Hence rationalization of (5.G5) computes \(R\Gamma(s,H_0)\); flat scalar extension commutes with its finite cone. We have first completed finite torsion coefficients and only then inverted \(\pi\). Using the vanishing of positive cohomology for *discrete* rational modules instead would be wrong here.

**Frobenius and coefficient conventions.** On the geometric complex in (5.G2), geometric Frobenius is \(F=T^{-1}\). The explicit chain isomorphism of BU.6 is
\[
\begin{aligned}
\bigl[M^\bullet\xrightarrow{T-1}M^\bullet\bigr]
&\xrightarrow{(1,-T^{-1})}
\bigl[M^\bullet\xrightarrow{F-1}M^\bullet\bigr],\\
-T^{-1}(T-1)&=T^{-1}-1.
\end{aligned}
\tag{5.G6}
\]
It preserves the degree-zero restriction map. On geometric Hom, the action is the usual conjugation \(h\mapsto F_BhF_A^{-1}\), as in BU.3; it does not change this lesson's Tate-twist convention. Composing sections of (5.G2) with (5.G5) and (5.G6) proves (5.G1) over \(E\).

For each finite coefficient extension \(E'/E\), tensoring with \(E'\) is a finite free coefficient operation. Its comparisons with internal Hom, sections and the Frobenius cone are obtained by finite sums, or on the finite perfect stratum models above; these comparisons commute with further extension and with the evaluation maps. Passing through the defining filtered coefficient extensions gives
\[
\begin{aligned}
H^r(C_0)\otimes_E\Lambda
 &\simeq\operatorname{Hom}_{D^b_c(X_0,\Lambda)}
 (A_0\otimes_E\Lambda,B_0\otimes_E\Lambda[r]),\\
H^r(C)\otimes_E\Lambda
 &\simeq\operatorname{Hom}_{D^b_c(X,\Lambda)}
 (A\otimes_E\Lambda,B\otimes_E\Lambda[r]).
\end{aligned}
\tag{5.G7}
\]
Flatness preserves kernels, cokernels and the finite cone. This proves the full \(\bar{\mathbf Q}_\ell\) statement without replacing it by a finite-field-of-coefficients special case. \(\square\)

The long exact sequence of (5.G1) gives, for every integer \(r\), the natural short exact sequence
\[
\begin{aligned}
0\longrightarrow H^{r-1}(C)_F
&\longrightarrow\operatorname{Hom}_{D^b_c(X_0)}(A_0,B_0[r])\\
&\longrightarrow H^r(C)^F\longrightarrow0.
\end{aligned}
\tag{5.G8}
\]
The first map is the connecting map and the second is restriction. There is no claim of a natural splitting. For perverse heart objects the negative geometric Hom groups vanish, so degree zero gives arithmetic Hom as geometric invariants. In degree one, heart \(\operatorname{Ext}^1\) agrees with ambient derived \(\operatorname{Hom}^1\): a short exact sequence gives its connecting morphism; conversely, in a triangle \(B_0\to E_0\to A_0\to B_0[1]\), perverse cohomology puts \(E_0\) in the heart and gives that short exact sequence. These constructions are inverse on extension classes. This fact needs no general equivalence between the derived category of the perverse heart and \(D^b_c(X_0)\).

**Descent and arithmetic extensions.** This supplies the continuous descent and completed-coefficient connection used in (5.2), relative to the exact ordinary-operation proofs just cited. Those ordinary-operation and perverse foundations are required hypotheses. In particular, arithmetic coinvariants can still be nonzero: the nonsplit arithmetic example (1.1) and the distinction between a vanishing invariant part and vanishing of every geometric extension apply here.

For two heart objects, the continuous procyclic Galois calculation gives
\[
0\to\operatorname{Hom}(A,B)_F\to
\operatorname{Ext}^1(A_0,B_0)\to
\operatorname{Ext}^1(A,B)^F\to0,                            \tag{5.2}
\]
where \(V_F=\operatorname{coker}(F-1)\) and \(V^F=\ker(F-1)\). To obtain it, apply the two-term continuous Galois complex with differential \(F-1\) to geometric derived Hom. Negative geometric Hom groups vanish for heart objects, so total degree one has exactly these two terms. Heart extensions equal derived degree-one Hom: the triangle of a short exact sequence gives one direction, and perverse cohomology of a degree-one cone gives the converse. Lemma 5.G supplies this continuous derived-descent and finite-to-adic comparison from the exact point-level and ordinary-operation providers, under the geometric and coefficient hypotheses of those proofs.

If \(\beta>\alpha\), both geometric Hom and geometric Ext in (5.2) have positive weights. Hence \(F-1\) is invertible and
\[
\operatorname{Hom}(A_0,B_0)=
\operatorname{Ext}^1(A_0,B_0)=0.                            \tag{5.3}
\]
When \(\alpha=\beta=w\) and both objects are pure, geometric Ext still has weights at least one. An arithmetic extension therefore becomes split geometrically. The kernel on the left of (5.2) need not vanish, as (1.1) demonstrates. Nor must all geometric extension classes vanish: only the fixed part is forced to be zero.

**Theorem 5.1.** A mixed perverse object has a unique finite increasing filtration \(W_mP_0\) with pure weight-\(m\) graded objects. Every morphism is strict for it.

**Proof.** Fix \(m\) and divide the simple constituents into weights at most \(m\) and weights greater than \(m\). Call the corresponding finite-length objects low and high. They have upper bound \(m\) and lower bound \(m+1\), respectively, by extension closure. Thus (5.3) kills Hom and Ext from a low object to a high one.

Induct on the length of \(P_0\). Quotient by a simple subobject \(S_0\), and in that quotient use the already constructed low subobject \(L_0\) with high quotient. If \(S_0\) is low, its inverse image is the required low subobject. If \(S_0\) is high, that inverse image is an extension of \(L_0\) by \(S_0\). It splits, uniquely, by (5.3). The lifted \(L_0\) is low and has high remaining quotient. Any other low subobject maps to zero in that high quotient, hence is contained in this one. This proves existence and uniqueness of a maximal low subobject, which we call \(W_mP_0\).

Maximality makes these subobjects increasing. Their extreme terms are zero and \(P_0\), because the length is finite. The constituents of \(W_m/W_{m-1}\) all have weight \(m\); both bounds are extension closed, so it is pure. Conversely any filtration with the stated pure quotients gives the same maximal low subobjects.

For strictness let \(f:P_0\to Q_0\) and \(I_0=\operatorname{im}f\). The image \(f(W_mP_0)\) is low, and its quotient in \(I_0\) is a quotient of the high object \(P_0/W_mP_0\). It is therefore \(W_mI_0\). Likewise \(I_0\cap W_mQ_0\) is low, and its quotient embeds in the high object \(Q_0/W_mQ_0\); it too is \(W_mI_0\). Hence
\[
f(W_mP_0)=I_0\cap W_mQ_0.                                  \tag{5.4}
\]
This proves strictness directly from the low/high characterization. \(\square\)

For a lisse sheaf on a smooth \(d\)-fold, apply the theorem after shift \([d]\) and subtract \(d\) from the filtration indices. Its subobjects are lisse subsystems. Indeed on a dense normal open their fibres are invariant subspaces; restriction of fundamental groups is surjective, since a connected finite étale cover of a normal connected variety stays connected over a dense open. The subspaces therefore extend across that open, and the IC boundary characterization leaves no additional supported subobject or quotient. This proves the lisse weight filtration and its strictness. The geometric-semisimplicity conclusion below also extends to lisse sheaves on a normal variety: restriction to its dense smooth locus preserves the geometric monodromy image.

**Theorem 5.2.** A pure perverse sheaf becomes a direct sum of simple perverse sheaves over \(\bar k\).

**Proof.** First an arithmetic simple local system becomes geometrically semisimple. The needed group statement has an elementary proof. If \(V\) is finite-dimensional and irreducible for \(\Gamma\), and \(N\triangleleft\Gamma\), choose an \(N\)-submodule \(U\ne0\) of minimal dimension. It is simple. Each translate \(gU\) is again simple for \(N\), and all translates span a nonzero \(\Gamma\)-submodule, hence span \(V\). Build a direct sum by adding a translate not already contained in the current sum. Its intersection with that sum is zero, by simplicity. Finite dimension makes the process terminate. Thus \(V|_N\) is semisimple, without an averaging hypothesis.

Take \(\Gamma\) to be the arithmetic fundamental group and \(N\) the normal geometric subgroup. Continuity is retained on all these invariant subspaces. If the support is not geometrically connected, pass to its finite constant field and apply the same argument on each conjugate component. Additivity of IC proves geometric semisimplicity of an arithmetic simple perverse object.

Now choose an arithmetic composition series of pure \(P_0\) of weight \(w\). Proposition 4.2 makes every step and quotient pure of that same weight. Each short exact sequence becomes split geometrically by (5.1)–(5.2). Induction splits the series, and the preceding group argument splits its simple arithmetic factors into geometric simples. This proves the assertion. Arithmetic semisimplicity would contradict (1.1), and is not asserted. \(\square\)

## 6. Perverse cohomology, global purity and the Lefschetz twist

**Proposition 6.1.** For a mixed bounded complex,
\[
\begin{aligned}
K_0\le w&\ \Longleftrightarrow\ {}^pH^iK_0\le w+i\text{ for all }i,\\
K_0\ge w&\ \Longleftrightarrow\ {}^pH^iK_0\ge w+i\text{ for all }i.
\end{aligned}
                                                               \tag{6.1}
\]
**Proof.** For the upper forward implication, induct on support dimension locally on an affine neighbourhood. Choose a dense principal regular open where all ordinary cohomology is lisse. On a component of dimension \(d\), its perverse cohomology is \(\mathcal H^{i-d}K_0[d]\), with upper bound \(w+i\). Affine \(j_!\) is t-exact and preserves that upper bound. The closed restriction \(i^*K_0\) has upper bound \(w\) and smaller support dimension. Its perverse cohomology has the desired bounds by induction. The perverse long exact sequence of localization expresses \({}^pH^iK_0\) as an extension of subquotients of these two known objects. Proposition 4.2 finishes the induction. Conversely the finite perverse truncation filtration has terms \({}^pH^iK_0[-i]\), all with upper bound \(w\). Extension closure gives the bound on \(K_0\). Perverse duality converts this equivalence to the lower one. \(\square\)

It follows that perverse cohomology of a pure weight-\(w\) complex is pure of weight \(w+i\). Its geometric truncation triangles split as well. The connecting map from \({}^pH^nK_0[-n]\) to \({}^p\tau_{\le n-1}K_0[1]\) is an arithmetic map from a pure weight-\(w\) object to a pure weight-\(w+1\) object. By (5.1), the geometric Hom group has positive weights. Its invariant map is zero. Exactness of Hom then gives a section in the geometric triangle; that section and the first arrow identify the middle object with the direct sum. Repeating over the finite range gives
\[
K\simeq\bigoplus_i{}^pH^i(K)[-i].                          \tag{6.2}
\]
The sections are choices. The displayed splitting is geometric and need not be canonical or Frobenius compatible.

If \(X_0\) is proper of pure dimension \(d\), define
\(IH^r(X,L)=H^{r-d}(X,\operatorname{IC}_{X_0}(L_0)|_X)\)
for a pointwise pure weight-\(a\) lisse sheaf on a smooth dense open. Formula (4.4) gives IC weight \(a+d\), proper pushforward preserves that complex weight, and the degree-\(r-d\) point test gives
\[
IH^r(X,L)\text{ is pure of weight }a+r.                     \tag{6.3}
\]
This is the precise role of IC purity in the global statement. Properness alone cannot turn the constant complex of the node into IC.

For projective \(f:X_0\to Y_0\), pure perverse \(P_0\), and the class \(\eta=c_1(\mathcal L)\) of an \(f\)-ample line bundle, relative hard Lefschetz states
\[
\eta^r:{}^pH^{-r}(Rf_*P_0)
\xrightarrow{\sim}{}^pH^r(Rf_*P_0)(r),\qquad r\ge0.         \tag{6.4}
\]
The universal-hyperplane proof is in [The decomposition theorem](the-decomposition-theorem.md#5-lefschetz-splitting-and-degeneration), with the same explicit ordinary prerequisites. It uses the weight consequences established here before invoking ampleness; they do not assume this Lefschetz statement. The original results are BBD, 5.4.10, and Weil II, 4.1.1 for the smooth projective case.

For \(P_0\) of weight \(w\), Proposition 6.1 makes the source weight \(w-r\). The target has weight \(w+r-2r=w-r\). This explains the twist necessary for Frobenius equivariance. For the structure map and IC, the statement becomes \(IH^{d-r}(X,L)\simeq IH^{d+r}(X,L)(r)\). The weight calculation checks its compatibility; it does not prove the ample cup-product map is an isomorphism.

## 7. Exercises with solutions

### Exercise 1 — eigenvalues before and after a shift

Compute the Frobenius eigenvalues and weights in projective-space cohomology and affine-line compact cohomology. Determine the complex weights and the weight of \(\Lambda_{\mathbb P^n}[n]\).

**Solution.** The projective-space basis is \(1,h,\ldots,h^n\). Its \(r\)-th term lies in degree \(2r\) and has untwisted eigenvalue \(q^r\), because the cycle class with twist \((r)\) is Frobenius invariant. Hence \(H^{2r}=\Lambda(-r)\) has weight \(2r\), and every odd group vanishes. Compact cohomology of the affine line has only \(H_c^2=\Lambda(-1)\), also with weight two. In both complexes, weight equals degree, so (2.1) gives complex weight zero. After shifting projective cohomology by \([n]\), degree \(2r-n\) retains weight \(2r=n+(2r-n)\), giving weight \(n\). The smooth dual formula separately proves that the perverse constant sheaf on \(\mathbb P^n\) has weight \(n\). The alternating traces are \(1+Q+\cdots+Q^n\) and \(Q\), respectively, over \(\mathbb F_Q\).

### Exercise 2 — a puncture and the two cohomologies

Derive the degree-one ordinary and compactly supported cohomology of \(\mathbb G_m\). Decide whether its ordinary cohomology complex is pure and check its point count.

**Solution.** In the compact-support localization sequence the only degree-zero boundary group is \(H^0(\{0\})=\Lambda\); the affine-line group in degree zero vanishes. Its connecting map is therefore an isomorphism onto \(H_c^1(\mathbb G_m)\). Degree two is inherited from \(\mathbb A^1\), giving \(\Lambda(-1)\); there are no other groups. Curve duality says \(H^i(\mathbb G_m)^\vee=H_c^{2-i}(\mathbb G_m)(1)\). Thus \(H^1=\Lambda(-1)\), weight two, and \(H^0=\Lambda\), weight zero. For one pure complex weight \(w\), these would require both \(w=0\) and \(w+1=2\), which is impossible. Both groups are nonetheless mixed. Compactly supported trace is \(-1+Q\), the number of nonzero elements of \(\mathbb F_Q\). Ordinary alternating trace is \(1-Q\); it is not the trace formula used for this nonproper space.

### Exercise 3 — what a positive Ext weight actually kills

Let \(A_0,B_0\) be pure perverse sheaves of the same weight. Prove geometric splitting of any arithmetic extension of \(A_0\) by \(B_0\), and distinguish the two conclusions that do not follow.

**Solution.** Formula (5.1) puts all eigenvalues of \(\operatorname{Ext}^1(A,B)\) in weights at least one. None can equal one, so the invariant group on the right of (5.2) is zero. The arithmetic extension therefore has zero underlying geometric class, which means its short exact sequence splits over \(\bar k\). The arithmetic class may still lie in \(\operatorname{Hom}(A,B)_F\). For two trivial point sheaves that group is \(\Lambda\), and (1.1) represents a nonsplit arithmetic extension. Also the geometric Ext group itself can be nonzero: on an elliptic curve, for \(A_0=B_0=\Lambda[1]\), it is \(H^1(X,\Lambda)\), of dimension two and weight one. The elliptic-curve cohomology and ordinary curve Riemann hypothesis are inputs to this example. Its nonzero classes fail to be Frobenius invariant; the weight argument never asserts their absence.

### Exercise 4 — normalize the degree of intersection cohomology

For proper pure-dimensional \(X_0\) and a pure weight-\(a\) local system on its smooth dense open, find the weight of \(IH^r\). Check the projective Lefschetz twist.

**Solution.** Put \(d=\dim X_0\). Intermediate extension gives complex weight \(a+d\), and proper pushforward preserves it. The ordinary degree used for \(IH^r\) is \(r-d\), so its weight is \(a+d+r-d=a+r\). In the projective case, the source \(IH^{d-r}\) has weight \(a+d-r\); the target \(IH^{d+r}(r)\) has weight \(a+d+r-2r=a+d-r\). Without the twist these would disagree for \(r>0\). The proof of IC purity uses Proposition 4.2 and its stated foundations, and hard Lefschetz uses the separate ample-hyperplane argument. The present computation supplies the resulting indices, not those prerequisite theorems by citation.

### Exercise 5 — determine the correction at the Schubert vertex

For (3.4), identify IC by a direct stalk/costalk calculation, count points over every finite extension, and recover the vertex trace both locally and globally.

**Solution.** Introduce \(L\subset W\cap F_2\) as in (3.5). For each line \(L\subset F_2\), the planes containing it form \(\mathbb P(k^4/L)=\mathbb P^2\). The resulting threefold is smooth and projective; its map to \(X_0\) has a point fibre away from \(F_2\), with the constant-rank inverse, and fibre \(\mathbb P^1\) at \(F_2\). Proper base change for \(R\pi_*\Lambda[3]\) gives \(\Lambda\) in vertex stalk degree \(-3\) and \(\Lambda(-1)\) in degree \(-1\). Proper duality gives its twist \((3)\) as its dual. Therefore the costalk has \(\Lambda(-2)\) in degree one and \(\Lambda(-3)\) in degree three. These strict boundary inequalities identify the direct image with the intermediate extension of \(\Lambda[3]\). No decomposition theorem is needed.

The count can also be performed without subtracting fibres. For each rational \(L\subset F_2\), the nonvertex planes with intersection exactly \(L\) are all lines in \(k^4/L\) except the one corresponding to \(F_2/L\). There are \(Q^2+Q\) of them. Distinct \(L\)'s give disjoint sets of nonvertex planes. Adding the single vertex gives \(1+(Q+1)(Q^2+Q)=Q^3+2Q^2+Q+1\), agreeing with (3.7).

Both nonzero vertex stalk degrees are odd, so their eigenvalues \(1,Q\) give trace \(-(1+Q)\). For the global calculation, the projective-bundle basis \(1,\xi,\xi^2\) over \(H^*(\mathbb P^1)\) gives dimensions \(1,2,2,1\) and eigenvalues \(1,Q,Q^2,Q^3\) in degrees \(0,2,4,6\). The IC identification shifts these degrees by three. Its global alternating trace is consequently \(-(1+2Q+2Q^2+Q^3)\). Every smooth point contributes \(-1\), and there are \(Q^3+2Q^2+Q\) such points; subtracting that contribution leaves \(-(1+Q)\). The global method uses the computed IC cohomology as well as the count and trace formula. The local method additionally determines the separate degrees and twists. Neither is a deduction of an unknown IC stalk from point counts alone.

## Appendix A. Curve estimates and the affine weight criterion

### Euler products and boundary bounds

The next two arguments precede the general weight theorem. Their ordinary inputs are curve compact-support localization, finite-dimensional adic cohomology, smooth curve duality and the trace formula. The actual curve trace proof is in The trace formula for curves, Sections 1–5. Its passage to a characteristic-zero local system with a stable integral lattice is described at the start of Section 6. For a constructible lattice, stratify the curve into its lisse open and finitely many points; localization and additivity give the same passage. The compatible finite-coefficient cohomology models and inverse-limit comparison are retained ordinary adic prerequisites. L-functions, rationality and the functional equation, Sections 1–2 proves the determinant identity from the traces of all Frobenius powers in characteristic zero. We use that proof, not its separately stated finite-coefficient determinant theorem.

Write
\[
\mathscr L(T_0,F_0,t)=
\prod_{x\in|T_0|}\det(1-F_xt^{\deg x}\mid F_{\bar x})^{-1},
\qquad P_r(t)=\det(1-tF\mid H_c^r(T,F)).
\]
For a curve the trace identity is
\[
\mathscr L(T_0,F_0,t)=\frac{P_1(t)}{P_0(t)P_2(t)}.
\tag{A.1}
\]
All factors are defined over a finite coefficient extension before enlarging to \(\Lambda\).

**Lemma (coarse curve bounds and the boundary).** If \(L_0\) is lisse and pointwise pure of weight \(a\) on a smooth geometrically connected curve \(U_0\), then every eigenvalue on \(H_c^1(U,L)\) has absolute value at most \(q^{(a+2)/2}\) under each complex embedding. If \(j:U_0\hookrightarrow C_0\) is a dense open in a smooth curve, every eigenvalue of the boundary stalk of the ordinary sheaf \(j_*L_0\) has absolute value at most \(q_x^{a/2}\). These conclusions do not use Theorem 4.1.

**Proof.** First suppose \(U_0\) is affine. A compactly supported section of a lisse sheaf on this connected nonproper curve is zero: in a proper completion its extension by zero vanishes near infinity, and a lisse section vanishing on a nonempty open vanishes everywhere. Thus \(H_c^0(U,L)=0\). Smooth duality gives
\[
H_c^2(U,L)=H^0(U,L^\vee)^\vee(-1).
\]
The geometric invariant subspace \(H^0(U,L^\vee)\) is stable under arithmetic Frobenius. At a closed point of degree \(e\), its Frobenius power is the restriction of the stalk operator of \(L_0^\vee\). Its eigenvalues therefore have absolute value \(q^{-a/2}\), without a semisimplicity assumption. Consequently \(H_c^2(U,L)\) is pure of weight \(a+2\).

A nonconstant map of the smooth proper completion to \(\mathbb P^1\) is finite, of some degree \(B\). It bounds the number of rational points of the curve over \(\mathbb F_{q^n}\) by \(B(q^n+1)\). In particular its number of degree-\(n\) closed points is \(O(q^n)\). Fix a complex embedding. Pointwise purity now makes the logarithmic series of the Euler product absolutely and locally uniformly convergent for
\[
|t|<q^{-(a+2)/2}.
\]
Indeed, its terms have modulus at most a constant times
\(q^n\sum_{m\ge1}(q^{a/2}|t|)^{mn}/m\), whose sum over \(n\) converges in that disk. The product is the exponential of this series, hence is holomorphic and nonzero. The roots of \(P_2\) lie on the boundary circle of the disk. Equation (A.1) therefore shows that \(P_1\) has no zero inside it. This proves the coarse \(H_c^1\) bound. For a proper curve, remove one closed point: localization surjects the new compactly supported degree-one group onto the original one, so the same bound holds.

For the boundary assertion, choose an affine connected neighbourhood \(C'_0\) of the boundary point and put \(U'_0=C'_0\cap U_0\). The same extension-by-zero argument gives \(H_c^0(C',j_*L)=0\); a section of \(j_*L\) is determined by its restriction to the connected lisse open. The sequence
\[
0\longrightarrow j_!L_0\longrightarrow j_*L_0
\longrightarrow i_*i^*j_*L_0\longrightarrow0
\]
also identifies \(H_c^2(C',j_*L)=H_c^2(U',L)\), because a finite set has no positive cohomology. Its eigenvalues again have weight \(a+2\). The Euler product on \(C'_0\) is the product on \(U'_0\), multiplied by the reciprocals of the finitely many boundary determinants. Equation (A.1) for \(j_*L_0\) has no pole in the disk above. The open product is holomorphic and nonzero there. Hence no boundary determinant can vanish in that disk: such a zero would give a pole, and the other boundary factors have no numerator to cancel it. We obtain the initial boundary bound \(a+2\).

Let \(V\) be the local geometric generic fibre and \(I_x\) its full inertia group. The boundary stalk is \(V^{I_x}\). For every \(m\ge1\),
\[
(V^{I_x})^{\otimes m}\hookrightarrow(V^{\otimes m})^{I_x}
\]
is an injective Frobenius-equivariant map. An eigenvalue \(\alpha\) on \(V^{I_x}\) therefore gives \(\alpha^m\) on this subspace. Apply the initial bound to the pointwise pure sheaf \(L_0^{\otimes m}\), of weight \(ma\). For each embedding,
\[
m\,\operatorname{wt}_x(\alpha)\le ma+2.
\]
Letting \(m\) tend to infinity gives \(\operatorname{wt}_x(\alpha)\le a\). Residue-field extensions replace Frobenius by a power and preserve this normalized inequality. This proves the lemma, including its fixed-embedding form. \(\square\)

### The monodromy filtration at a boundary point

The preceding inequalities alone do not construct an integral weight filtration at the boundary. We obtain it from a tensor invariant and its dual.

First recall why local inertia becomes unipotent on a finite cover. A continuous lisse representation has a stable lattice over the integers of a finite extension of \(\mathbb Q_\ell\). The wild pro-\(p\) group has finite image: reduction of the lattice has finite image, and its intersection with the pro-\(\ell\) congruence kernel is trivial. After killing that finite image, tame inertia is procyclic. The relation between a tame generator and a Frobenius lift permutes its finitely many eigenvalues by the \(q_x\)-power map, or its inverse. Each eigenvalue is thus a root of unity. A sufficiently deep finite congruence quotient kills the finite wild image and these finite semisimple eigenvalues. The associated finite étale cover of \(U_0\), followed by normalization of its smooth completion, makes local inertia unipotent. This uses the ordinary local description of curve inertia and the finite étale fundamental-group classification; it introduces no weight theorem.

On this cover write \(V\) for the local fibre. The logarithm of unipotent tame inertia is a nilpotent operator
\[
N:V\longrightarrow V(-1),\qquad FNF^{-1}=q_x^{-1}N.
\]
The canonical increasing monodromy filtration, centred at zero, is
\[
M_iV=\sum_{\substack{r,s\ge0\\r-s=i}}
\bigl(\ker N^{r+1}\cap\operatorname{im}N^s\bigr).
\tag{A.2}
\]
Only finitely many terms can contribute. On a Jordan chain of length \(j+1\), with vectors \(v,Nv,\ldots,N^jv\), their grades are \(j,j-2,\ldots,-j\). This verifies both the formula and
\(N^i:\operatorname{Gr}_i^MV\simeq\operatorname{Gr}_{-i}^MV(-i)\) for \(i\ge0\). Kernels and images in (A.2) are Frobenius stable, so the filtration is arithmetic.

**Proposition.** If \(L_0\) is pointwise pure of weight \(a\), then \(\operatorname{Gr}_i^MV\) is pure of weight \(a+i\). In particular \(V^{I_x}\) is mixed of weights \(\le a\), and the ordinary sheaf \(j_*L_0\) is mixed of weights \(\le a\).

**Proof.** Tensor with the constant rank-one arithmetic sheaf on which geometric Frobenius is \(q^{-a/2}\); choose the root in a finite coefficient field. It is an \(\ell\)-adic unit, so its powers extend continuously from \(\mathbb Z\) to \(\widehat{\mathbb Z}\). We can therefore suppose \(a=0\).

Write the multiplicative Jordan decomposition of Frobenius as \(F=F_sF_u\). Since conjugation scales \(N\) by \(q_x^{-1}\), its semisimple part scales \(N\) by that number and its unipotent part fixes \(N\). Thus
\[
F_sNF_s^{-1}=q_x^{-1}N,\qquad F_uN=NF_u.
\]
Choose a Jordan-chain basis for \(N\) homogeneous for the eigenspaces of \(F_s\). Such a basis can be chosen because every kernel and image of a power of \(N\) is graded by these eigenspaces. Choose homogeneous representatives in the usual primitive quotients
\(\ker N^{j+1}/(\ker N^j+N\ker N^{j+2})\), and take their chains. The ordinary Jordan-basis proof, applied with these graded complements, gives a basis. If a top vector satisfies \(F_sv=\gamma v\), its bottom vector \(N^jv\) has eigenvalue \(\alpha=\gamma q_x^{-j}\).

In the tensor square consider the nonzero vector
\[
c_j=\sum_{r=0}^j(-1)^rN^rv\otimes N^{j-r}v.
\]
The operator \(N\otimes1+1\otimes N\) kills it: adjacent terms cancel and the two end terms vanish. The semisimple tensor Frobenius acts on it by
\[
\gamma^2q_x^{-j}=\alpha^2q_x^j.
\]
The kernel is Frobenius stable. The restriction of a semisimple operator remains semisimple, while the restriction of its commuting unipotent part remains unipotent; hence this number is also an eigenvalue of the full Frobenius on that kernel. Unipotent inertia invariants are precisely this kernel. Apply the independently proved boundary bound to \(L_0\otimes L_0\), still of weight zero. For every embedding,
\[
|\iota(\alpha)|\le q_x^{-j/2}.
\]
The corresponding dual Jordan block has bottom eigenvalue
\(\gamma^{-1}=\alpha^{-1}q_x^{-j}\). Apply the same argument to \(L_0^\vee\): it gives the reverse inequality. Therefore
\[
|\iota(\alpha)|=q_x^{-j/2}.
\]
The vector \(N^rv\) has eigenvalue \(\gamma q_x^{-r}\), of weight \(j-2r\), exactly its monodromy grade. Frobenius need not preserve each individual chain; its eigenvalues on the graded spaces equal those of its semisimple part. Restoring the original twist gives weight \(a+i\).

In the usual all-embedding version these eigenvalues are algebraic. Indeed a transcendental eigenvalue can be sent by a field embedding to a transcendental complex number of arbitrarily large modulus, with that embedding extended to the coefficient field; this contradicts the asserted bounds for every embedding. Thus the graded pieces are pure in the algebraic, all-conjugate sense of Section 2. The argument for one fixed embedding gives the corresponding \(\iota\)-purity assertion without that extra algebraicity conclusion.

Passing to a finite cover only scales \(N\) by a nonzero constant and replaces local Frobenius by a power. Neither changes the monodromy filtration or the normalized weight conclusion. Return to the original point. For an open unipotent inertia subgroup \(I'_x\), the full invariant space is
\[
V^{I_x}=(\ker N)^{I_x/I'_x}.
\]
The finite quotient preserves the filtration and its invariants are exact in characteristic zero. The grades of \(\ker N\) are the bottom grades \(-j\le0\) of the Jordan chains. Their induced filtration therefore makes \(V^{I_x}\) mixed of weights \(\le a\), retaining wild inertia as well. Finally \(j_!L_0\) is pointwise pure of weight \(a\); the finite boundary sheaf has the just constructed mixed filtration. The open–closed ordinary exact sequence gives mixedness and the bound for \(j_*L_0\). \(\square\)

This is the boundary and monodromy mechanism of Deligne, Weil II, 1.8.1, 1.8.4 and 1.8.8.1. The explicit alternating tensor replaces an appeal to a primitive-tensor decomposition. It uses no general compact-support weight estimate, perverse weight theorem or Frobenius diagonalizability.

### Positivity rules out equality in the coarse bound

**Proposition (Deligne).** For a lisse pointwise \(\iota\)-pure sheaf \(L_0\) of weight \(a\) on a smooth curve,
\[
|\iota(\alpha)|<q^{(a+2)/2}
\quad\text{for every Frobenius eigenvalue on }H_c^1(C,L).
\tag{A.3}
\]
This is Weil II, Corollary 2.2.10. The strict inequality is the useful improvement over the preceding coarse bound. We give a curve specialization of Deligne's positivity argument.

**Proof.** A finite-dimensional continuous representation of a profinite group over a finite extension of \(\mathbb Q_\ell\) has a stable integral lattice. Its compact image is bounded; the integral span of the translates of any lattice is again a lattice. Thus Frobenius eigenvalues in stalks and compact cohomology are \(\ell\)-adic units. Every such unit \(u\) defines a continuous unramified rank-one sheaf \(\chi_u\), with geometric Frobenius \(u\): its powers extend from \(\mathbb Z\) to \(\widehat{\mathbb Z}\) in the profinite unit group. Twisting multiplies a degree-\(e\) stalk eigenvalue by \(u^e\), and a cohomological eigenvalue by \(u\).

After a finite constant-field extension work on geometrically connected components, then restrict to a nonempty affine open \(U_0\). Localization surjects \(H_c^1(U,L)\) onto \(H_c^1(C,L)\). Finite field extension replaces both Frobenius and eigenvalues by powers, so preserves (A.3). For a nonzero sheaf choose a closed point of degree \(e\) and an eigenvalue \(\delta\) there. An \(e\)-th root \(u\) of \(\delta^{-1}\) is a unit with \(|\iota(u)|=q^{-a/2}\). Twist by \(\chi_u\) to reduce to weight zero. This choice also works for a real fixed-embedding weight; it does not presume that an arbitrary prescribed positive real scalar lies in the image of \(\iota\).

Degree-one bounds pass through extensions, by the compact-support long exact sequence. Reduce first to an arithmetic irreducible lisse constituent. Its geometric representation is semisimple by the following elementary argument: for a normal subgroup \(N\) of a group \(\Gamma\) acting irreducibly on a finite-dimensional space, choose a smallest nonzero \(N\)-stable subspace. Its \(\Gamma\)-translates are simple \(N\)-modules and span the space; adding translates outside the current sum gives a direct sum, because their intersections are zero by simplicity. Finite dimension terminates this process. No weight theorem is involved.

After another finite constant-field extension, Frobenius fixes each of the finitely many geometric simple types. Each geometric isotypic component is then arithmetic stable: the geometric group and a Frobenius lift generate a dense subgroup of the arithmetic fundamental group. Write such a component as \(S\otimes M\), with \(S\) geometrically simple. A chosen intertwiner of \(S\) with its Frobenius conjugate factors the actual Frobenius operator as \(T\otimes B\); Schur's lemma gives this factorization. A \(B\)-stable complete flag of \(M\) gives arithmetic subquotients that are geometrically simple. They inherit continuity from the original representation; we do not assert a separately continuous descent for the arbitrary intertwiner \(T\). All their local eigenvalues still have modulus one. We have reduced to a weight-zero geometrically simple sheaf \(E_0\).

If \(E\) is geometrically trivial, it has rank one and is an unramified character of modulus one. The constant sheaf on a proper smooth curve has degree-one eigenvalues of modulus \(q^{1/2}\): Weil's proof for curves, Theorem 3.12 proves the point-count Riemann hypothesis, and the curve trace identity identifies its numerator with \(\det(1-tF\mid H^1)\), since \(H^0=\Lambda\) and \(H^2=\Lambda(-1)\). This independent theorem uses its stated Riemann–Roch and surface intersection/Hodge-index prerequisites. Open–closed localization adds only boundary roots of unity to the degree-one compact-support eigenvalues. Tensoring by our unramified character preserves their moduli, all strictly less than \(q\).

Suppose \(E\) is geometrically nontrivial. Duality and simplicity give \(H_c^2(U,E)=H_c^2(U,E^\vee)=0\). The geometric invariant subspace of \(\operatorname{End}E\) is the scalar identity, fixed by arithmetic Frobenius. Its trace pairing identifies its dual with itself. Thus
\[
H_c^2(U,\operatorname{End}E)=\Lambda(-1),
\qquad H_c^2(U,\Lambda)=\Lambda(-1).
\]
Affineness kills degree zero for these lisse sheaves. The determinant identity gives polynomials
\(\mathscr L(E,t)=P_E(t)\) and \(\mathscr L(E^\vee,t)=P_{E^\vee}(t)\), whereas
\[
Z(U_0,t)=\frac{P_{\rm const}(t)}{1-qt},
\qquad \mathscr L(\operatorname{End}E,t)=\frac{P_{\rm end}(t)}{1-qt}.
\tag{A.4}
\]
All four numerators have constant term one. The earlier Euler-product argument already bounds the eigenvalues on \(H_c^1(U,E)\) by \(q\).

If an eigenvalue \(\alpha\) has \(|\iota(\alpha)|=q\), twist \(E_0\) by \(\chi_{q/\alpha}\). This is a continuous unit character of complex modulus one. The twisted sheaf is still geometrically simple and pointwise \(\iota\)-pure of weight zero, its endomorphism sheaf is unchanged, and it now has cohomological eigenvalue \(q\). Denote it again by \(E_0\). Then \(\iota P_E(1/q)=0\). Local dual eigenvalues are the inverses of unit-circle eigenvalues, hence their complex conjugates. The dual Euler series therefore has conjugate coefficients, and \(\iota P_{E^\vee}(1/q)=0\) also. Jordan blocks affect neither power traces nor this identity.

The rational function
\[
Q(t)=Z(U_0,t)\,\iota\mathscr L(\operatorname{End}E,t)
\,\iota P_E(t)\,\iota P_{E^\vee}(t)
\]
is consequently a polynomial: the two zeros cancel the only two possible denominator factors \(1-qt\). But if \(z_{x,m}=\operatorname{Tr}(\iota F_x^m\mid E_{\bar x})\), its formal Euler logarithm is
\[
\log Q(t)=\sum_x\sum_{m\ge1}|1+z_{x,m}|^2
\frac{t^{m\deg x}}m.
\tag{A.5}
\]
Indeed the endomorphism trace is \(z_{x,m}\overline{z_{x,m}}\), including for nonsemisimple operators. Every coefficient in (A.5) is nonnegative, and some coefficient is positive. To see the latter, fix a closed point. Positive powers of its finitely many unit-circle eigenvalues can approach one simultaneously: partition the compact product of circles into finitely many sets of sufficiently small diameter and place more consecutive powers than sets in them; two powers in one set have a positive quotient power close to the identity. The trace of that power is close to \(\operatorname{rank}E\), so \(|1+z_{x,m}|^2>0\).

If \(b_N>0\) is a coefficient of \(\log Q\), then the coefficient of \(t^{kN}\) in \(\exp(\log Q)\) is at least \(b_N^k/k!>0\) for every \(k\). This contradicts polynomiality. Equality is impossible. Undoing the initial twist and the reductions proves (A.3). The auxiliary equality twist preserves fixed-embedding purity; it need not preserve usual purity at every embedding. \(\square\)

When the original local eigenvalues are algebraic, so are these degree-one eigenvalues. On an affine curve the top polynomial \(P_2\) has algebraic coefficients: each arithmetic invariant eigenvalue has a power among the algebraic local eigenvalues. Every formal coefficient of the Euler product is algebraic, because finitely many local factors contribute. The equality \(P_1=\mathscr L P_2\) therefore makes the finite polynomial \(P_1\) algebraic, and hence its reciprocal roots algebraic. Extension of the constant field and the affine-open surjection transfer this to the original curve. The strict bound holds under every complex embedding in the usual pointwise-pure setting. It is still a coarse bound; it does not yet give the optimal \(a+1\) estimate or integral mixedness for general \(H_c^1\).


### Real sheaves and determinant weights

The next argument needs a purity criterion for real coefficients before it can improve the coarse curve bound. Fix an embedding \(\iota:\overline{\mathbb Q}_\ell\hookrightarrow\mathbb C\), and use **geometric Frobenius** throughout. For an eigenvalue at a point of degree \(e\), write
\[
w_{q^e}(\alpha)=2\log_{q^e}|\iota(\alpha)|.
\]
A lisse sheaf is \(\iota\)-real if every local characteristic polynomial has real coefficients after applying \(\iota\). The coefficients are étale: each representation descends to a finite extension of \(\mathbb Q_\ell\) and is continuous. Real weights in this subsection need not be integers.

**Lemma (Deligne's real-sheaf criterion).** On a smooth geometrically connected curve over \(\mathbb F_q\), every arithmetic irreducible constituent of an \(\iota\)-real lisse sheaf is pointwise \(\iota\)-pure of a real weight.

The ordinary inputs are the curve trace determinant identity, compact-support localization and duality, and the independent constant-coefficient curve Riemann hypothesis used above. The representation-theoretic inputs are Schur's lemma, the isotypic intertwiner decomposition, reductivity of a group with a faithful semisimple representation, the central-torus structure of a connected reductive group, and finiteness of the centre and algebraic outer automorphism group of a connected semisimple group. These are characteristic-zero algebraic-group facts, not consequences of the weight theorem being proved.

**Proof.** First, every rank-one continuous arithmetic étale character has finite geometric image. Choose a finite coefficient field \(E\). After a finite étale cover its image lies in a sufficiently deep principal-unit subgroup on which the \(\ell\)-adic logarithm is injective; choose it deep enough also when \(\ell=2\). The logarithm on the geometric fundamental group gives a Frobenius-invariant class in
\[
H^1(C_{\overline{\mathbb F}_q},E).
\]
This is geometric cohomology. On the smooth proper completion its constant-coefficient degree-one eigenvalues have weight one by the independent curve Riemann hypothesis. Localization makes the additional open-curve quotient a subspace of boundary terms of weight two. Neither group has eigenvalue one. The invariant logarithmic class is therefore zero. Injectivity of the logarithm kills the geometric character on this finite cover, proving the assertion. Finite constant-field extensions made along the way preserve it.

Consequently a rank-one character has local eigenvalues \(u^e\) times roots of unity, with one arithmetic scalar \(u\). For an arithmetic simple constituent \(K_j\) of rank \(n_j\), let \(b_j\) be the weight of \(\det K_j\) divided by \(n_j\). At every closed point,
\[
\sum_{\alpha\text{ on }(K_j)_x}w_{q^{\deg x}}(\alpha)=n_jb_j.
\tag{A.6}
\]
This is initially an average, not a purity assertion.

We establish the tensor and exterior rules for these averages. Replace the sheaf by its arithmetic semisimplification. Its restriction to the normal geometric group is semisimple by the minimal-subspace and translate argument in the strict estimate. Thus its connected geometric algebraic monodromy \(H^0\) is reductive. After a finite arithmetic cover fixes its finitely many geometric simple types, Frobenius on an isotypic block \(S\otimes M\) has the form \(T\otimes B\). A \(B\)-stable flag gives arithmetic subquotients which are geometrically simple; stability extends from the geometric group and the chosen Frobenius power to the full subgroup by continuity and density. Their determinant characters have finite geometric image. The connected central torus acts scalarly on each \(S\), and the rank-th power of that scalar character has finite image. A character of a connected torus with finite image is trivial. The torus therefore acts trivially on the faithful representation and is trivial. Hence \(H^0\) is semisimple.

Let \(H\) be the full geometric algebraic monodromy group. The bookkeeping group \(\Gamma=H\rtimes\mathbb Z\) records conjugation by a lift of geometric Frobenius and its integral degree; no topological splitting of the full profinite arithmetic group is asserted. It has a central element \(c\) of positive degree \(d\). Indeed, a power of Frobenius acts on \(H^0\) by an inner automorphism, because the outer automorphism group is finite. Correct that power by an element of \(H^0\) to centralize \(H^0\), then take a power acting trivially on \(H/H^0\). Its commutator with each component representative lies in the finite centre of \(H^0\). Another common power kills these finitely many commutators, producing an element centralizing \(H\). Its commutator with the original Frobenius belongs to \(Z(H)\), which is finite: its intersection with \(H^0\) is finite, and there are finitely many components. One final power kills this commutator.

Schur's lemma makes \(c\) a scalar \(\lambda_j\) on each arithmetic simple \(K_j\). Taking determinants, the geometric factor contributes a root of unity, so
\[
b_j=\frac{2}{d}\log_q|\iota(\lambda_j)|.
\]
Central scalars multiply on tensors. On an exterior power they are the products of selected scalar entries, repeating \(\lambda_j\) exactly \(n_j\) times. Each nonzero central eigenspace has a simple arithmetic subquotient. Therefore tensor determinant weights add, and the largest determinant weight of an exterior power is the sum of the largest selected entries of the list consisting of \(b_j\) repeated \(n_j\) times. Semisimplification preserves the diagonal eigenvalues of tensor and exterior matrices, so the same rules apply before semisimplification.

Now let \(K\) be real and put \(r=\max_j b_j\). Its local power traces are real. For every positive integer \(m\), the formal Euler logarithm of \(K^{\otimes 2m}\) has nonnegative real coefficients: each trace is the \(2m\)-th power of a real trace. Exponentiating gives nonnegative coefficients in each local reciprocal determinant and in their product, all with constant coefficient one.

Pass to an affine open retaining the closed point to be tested. Degree-zero compact cohomology vanishes. Ordinary curve duality identifies degree two with geometric coinvariants followed by the twist \((-1)\). On coinvariants the geometric part of \(c\) disappears. The tensor scalar rule thus bounds its cohomological eigenvalues by weight \(2mr+2\). The trace determinant identity puts every possible pole of the Euler product on or outside
\[
|t|=q^{-(2mr+2)/2}.
\]
Its rational Taylor series consequently converges inside this circle. Positivity lets us compare a single local factor with the whole product: the product of the other factors has nonnegative coefficients and constant coefficient one, so the local factor is coefficientwise bounded by the global series. It converges in the same disk. A local eigenvalue \(\alpha\) at degree \(e\) contributes \(\alpha^{2m}\) to the tensor power and a pole of modulus \(|\iota(\alpha)|^{-2m/e}\) to its reciprocal determinant. There is no numerator to cancel that pole. Therefore
\[
w_{q^e}(\alpha)\le r+\frac1m.
\]
Letting \(m\) grow bounds every local eigenvalue by \(r\). This also applies to exterior powers, whose local multisets remain real.

Fix a constituent of determinant weight \(b\) and one of its local eigenvalues \(\alpha\). Let \(N\) be the total rank of constituents with determinant weight strictly greater than \(b\). In \(\bigwedge^{N+1}K\), select \(\alpha\) and all eigenvalues of those greater-weight constituents. Their product has weight
\[
w_{q^e}(\alpha)+\sum_{b_j>b}n_jb_j.
\]
The largest determinant weight of that exterior power is \(b+\sum_{b_j>b}n_jb_j\). The bound just proved gives \(w_{q^e}(\alpha)\le b\). Equation (A.6) forces equality for every eigenvalue of the chosen constituent. This works at every closed point and for every constituent, proving the lemma. It produces pure constituents of real weights; it supplies no integrality assertion. \(\square\)

This is the mechanism of Weil II, 1.3.4–1.3.13 and 1.5.1–1.5.3. Neither the general cohomological weight estimate nor pure perverse semisimplicity entered the proof.

### The surface-pencil argument and successive improvements

**Proposition, with explicit ordinary geometric prerequisites.** Assume the surface-pencil package described in the next paragraph, its stated local vanishing-cycle calculations, and the ordinary adic cohomology, base-change, trace, duality, Künneth and Leray foundations. For a pointwise \(\iota\)-pure lisse sheaf \(L_0\) of weight \(a\) on a smooth curve,
\[
w_q(\alpha)\le a+1\quad\text{on }H_c^1(U,L).
\tag{A.7}
\]
For the usual algebraic purity at every complex embedding and integral \(a\), this cohomology has an integral mixed filtration with weights at most \(a+1\).

Here is the geometric package proved in Proposition B.2, together with the cohomological hypotheses still needed. After sufficient ampleness and a finite constant-field extension, a smooth projective surface with normal-crossing boundary has a pencil whose axis is transverse and disjoint from that boundary. Blowing up its finitely many axis points produces a map to \(\mathbb P^1\). Outside finitely many exceptional values its open fibres and coefficient sheaf are transversely tamely locally acyclic. Each exceptional fibre has at most one exceptional point, of one of three types: an interior ordinary node, simple tangency with a smooth boundary branch, or passage through a crossing of two boundary branches. Propositions C.1–C.3 compute the ordinary arithmetic node and both boundary configurations, including the coefficient filtration. The relevant primary loci are Weil II, 3.1.1–3.1.5 and 3.2.14. Appendix B proves the pencil geometry, including the actual étale nodal equation, and deduces transverse tame local acyclicity from explicit ordinary covering and cohomology inputs. Appendix C derives the arithmetic nodal formula from a proper conic and an intrinsic branch calculation. Ordinary smooth local acyclicity is supplied by Constructible complexes, AT.1–AT.3, with its canonical nearby-cycle unit in AT.5. Lemma B.3c below supplies ordinary proper nearby-cycle transport from Constructible complexes, BE.7–BE.8 and BZ.2. Projective-line cohomology, normal-crossing purity and normalized adic comparison remain separate inputs; both supplied comparison proofs retain their recursive foundations. Neither the inequalities below nor nearby-cycle t-exactness alone supplies those foundations.

**Proof.** The unit-character normalization in the strict estimate reduces \(a\) to zero: choose an eigenvalue \(\delta\) at a closed point of degree \(e\), and twist by the continuous character with geometric Frobenius an \(e\)-th root of \(\delta^{-1}\). Its complex modulus is \(q^{-a/2}\); it is an \(\ell\)-adic unit. Undoing it adds \(a\) to every weight. Define \(B(k)\), for integers \(k\ge0\), to be the assertion
\[
w_q(\alpha)\le1+2^{-k}
\quad\text{on }H_c^1\text{ of every weight-zero pure lisse curve sheaf}.
\]
The independent coarse bound proves \(B(0)\). If a constructible sheaf \(E\) on a curve has a pure lisse restriction of weight \(b\) to a dense smooth open \(j:W\hookrightarrow C\), the ordinary open–closed sequence gives
\[
H_c^1(W,j^*E)\twoheadrightarrow H_c^1(C,E),
\tag{A.8}
\]
because the finite complement has no positive cohomology. Thus \(B(k)\) bounds the latter group by \(b+1+2^{-k}\), regardless of its boundary stalks.

First make the boundary monodromy of \(L\) tame and unipotent. Its finite-cover reduction and later descent are given below. Let \(X_0\) be the smooth proper completion of \(U_0\), and set
\[
S_0=X_0\times X_0,\qquad V_0=U_0\times U_0,
\qquad G_0=L_0\boxtimes L_0.
\]
This is the external tensor square. Künneth gives a Frobenius-equivariant direct summand
\[
H_c^1(U,L)\otimes H_c^1(U,L)\subset H_c^2(V,G).
\tag{A.9}
\]
Choose the pencil from the stated geometric package. Write \(\pi:\widetilde S_0\to S_0\) for the blowup, \(\widetilde V_0=\pi^{-1}(V_0)\), and \(f:\widetilde V_0\to P_0=\mathbb P^1_{\mathbb F_q}\). Its regular parameter open is \(w:W_0\hookrightarrow P_0\). Put
\[
E_r=R^rf_!\pi^*G_0,\qquad E=E_1.
\]
Over \(W_0\), base change identifies their stalks with compact cohomology of smooth open curve fibres. The strict bound makes every eigenvalue of \(w^*E\) have weight strictly less than two.

We need pure constituents before using this strict inequality. The weight-zero sheaf \(G_0\oplus G_0^\vee\) is real, since its dual eigenvalues are the complex conjugates of its eigenvalues. Compact degree-one cohomology of a smooth curve with pure real coefficients has real characteristic polynomial: its Euler product is real, and the strict degree-one bound separates numerator zeros from the top-degree circle of weight two. Thus its top determinant, recovered from the poles on that circle, is real. On a proper connected curve the degree-zero determinant is real by applying this observation to the twisted dual and using duality; on a nonproper connected curve degree zero vanishes. The determinant identity then makes degree one real. A Frobenius orbit of geometric components contributes \(\det(1-t^sF^s)\), so the same conclusion holds for disconnected fibres.

Consequently \(w^*E\) is a direct summand of a real lisse sheaf. The preceding lemma gives a finite filtration \(G_i(w^*E)\) with pure graded pieces of real weights \(b_i<2\). These weights have not yet been shown integral.

At an exceptional value \(t\), denote its exceptional point by \(x\), and use the geometric generic point \(\bar\eta\) of the strict local trait. Lemma B.4 and Propositions C.1–C.3 show that the unshifted vanishing cycles of the extension by zero of \(\pi^*G\) are supported at \(x\) in ordinary degree one. For locally constant coefficients \(A\), their formulas are
\[
\begin{array}{c|c}
\text{interior node}&A(-1)\otimes\varepsilon(B)\\
\text{boundary tangency}&A\otimes\varepsilon(B)\\
\text{boundary crossing}&A\otimes\varepsilon(B),
\end{array}
\tag{A.10}
\]
where \(\varepsilon(B)\) is the sign of the two branches in the first and third cases, and of the two nearby boundary points in the second. The proper-conic computation and branch descent in Proposition C.1 supply the nodal Tate factor \((-1)\). At tangency, the triangle for the boundary reduces vanishing cycles to the quotient of the two-point permutation space by its diagonal, shifted from the boundary into degree one. At a crossing, if \(\nu:D'\to D\) normalizes the two boundary branches, the exact sequence
\[
0\to j_!\Lambda\to\Lambda_{\widetilde S}
\to\nu_*\Lambda_{D'}\to\Lambda_x\otimes\varepsilon(B)\to0
\]
reduces to the last point-supported term: the ambient map and normalized branches are smooth. Proposition C.2 proves both reductions, keeping the degree-\(-1\) cycles of the point-supported term and the separable characteristic-two tangency. The sign representations have finite image and weight zero; exchanging branches must not be discarded. The nodal Tate factor has weight two.

The independently proved boundary monodromy grading filters each factor of our coefficients by locally constant, inertia-trivial grades of integral weights. Their external tensor grades have the summed integral weights. Apply (A.10) to these grades. Proposition C.3 proves exactness of the induced cycle filtration, including its finite-to-adic passage, and gives concentration in degree one with a finite integral mixed filtration of \(\Phi_x^1\). Interior coefficients already have weight zero. The specialization sequence is therefore
\[
0\to E_{\bar t}\to E_{\bar\eta}\to\Phi_x^1
\to(E_2)_{\bar t}\to(E_2)_{\bar\eta}\to0.
\tag{A.11}
\]
Its derivation in (C.19) uses the proper pencil compactification and is distinct from compact-support localization on \(U\).

The injective specialization shows that \(E\) has no exceptional point-supported section, hence \(E\hookrightarrow w_*w^*E\). Extend its filtration by intersections,
\[
G_iE=E\cap w_*G_i(w^*E),\qquad Q_i=G_iE/G_{i-1}E.
\]
Filtering the cokernel of \(E_{\bar t}\to E_{\bar\eta}\) by the images of \(G_iE_{\bar\eta}\) yields exact sequences
\[
0\to(Q_i)_{\bar t}\to(Q_i)_{\bar\eta}\to A_t^i\to0,
\]
where \(A_t^i\) is a subquotient of \(\Phi_x^1\), hence has integral weights. Local monodromy applied to the pure lisse restriction of \(Q_i\) puts every generic local eigenvalue in weights \(b_i+\mathbb Z\). The real-weight version follows by the same unit normalization and untwisting as above. If any \(A_t^i\ne0\), comparison of an eigenvalue forces \(b_i\in\mathbb Z\).

If every \(A_t^i\) vanishes, specialization is an isomorphism everywhere, with inertia trivial on the source. Thus \(Q_i\) is lisse on the entire projective line. Its geometric fundamental group is trivial, so it is geometrically constant. Every nonconstant \(Q_i\), therefore, has integral \(b_i<2\), hence \(b_i\le1\). Constants need no such integrality conclusion: their degree-one cohomology on \(P\) vanishes. For nonconstant grades, (A.8) and \(B(k)\) give the bound \(2+2^{-k}\). The filtration exact sequences give
\[
H^1(P,E_1):\quad w_q\le2+2^{-k}.
\]

The two other total-degree-two terms are elementary. Degree-zero compact cohomology of a curve with weight-zero coefficients has weights at most zero, by evaluation on stalks. Degree two has weights at most two, by normalization of the fibre and ordinary smooth curve duality. Thus \(E_0\) and \(E_2\) have pointwise bounds zero and two. Global sections inject into finitely many stalks, giving \(H^0(P,E_2)\le2\). For \(H^2(P,E_0)\), remove finitely many points until \(E_0\) is lisse. Localization identifies this group with top compact cohomology of that open, whose coinvariant description adds two. The pointwise upper bound also bounds the arithmetic eigenvalues on coinvariants: a Frobenius power on any closed stalk induces that power on the geometrically constant quotient. Hence
\[
H^0(P,E_2):\ w_q\le2,
\qquad H^2(P,E_0):\ w_q\le2.
\]
No degree-one estimate is used for these extremal groups.

Compact-support Leray now reads
\[
H^p(P,R^rf_!\pi^*G)\Longrightarrow
H_c^{p+r}(\widetilde V,\pi^*G).
\]
Only \((p,r)=(1,1),(0,2),(2,0)\) contribute to total degree two. The abutment has a filtration by subquotients of these groups, so its weights are at most \(2+2^{-k}\); degeneration is unnecessary. Proper pullback along the blowup injects \(H_c^2(V,G)\) into this abutment. The ordinary smooth-surface degree-one trace is a retraction; equivalently the blowup formula adds only the axis-point fibres \(G_z(-1)\) in degree two.

If \(\alpha\) is an eigenvalue on \(H_c^1(U,L)\), its square is an eigenvalue on the Künneth summand (A.9). Triangularizing Frobenius proves this also with Jordan blocks. Therefore
\[
2w_q(\alpha)\le2+2^{-k},
\qquad w_q(\alpha)\le1+2^{-(k+1)}.
\tag{A.12}
\]
This proves \(B(k+1)\) in the tame unipotent case.

For arbitrary boundary monodromy, the stable-lattice and local-monodromy argument already used above supplies a finite étale cover killing the finite wild image and finite tame semisimple parts, leaving unipotent tame inertia. Normalize the proper completion of that cover. Pullback on compact cohomology is injective because its composite with finite-étale trace is multiplication by the nonzero degree. Finite constant-field extensions replace eigenvalues by powers and preserve normalized weights. These two descents prove \(B(k+1)\) for the original curve. Starting from \(B(0)\) and letting \(k\) tend to infinity proves (A.7).

For integral mixedness, let \(j:U_0\hookrightarrow X_0\) and \(i:D_0\hookrightarrow X_0\) be its finite boundary. The ordinary sheaf sequence for \(j_!L\to j_*L\) gives the complete segment
\[
\begin{split}
0\to H_c^0(U,L)\to H^0(X,j_*L)
\to H^0(D,i^*j_*L)\to H_c^1(U,L)\\
\to H^1(X,j_*L)\to0,
\qquad H_c^2(U,L)\simeq H^2(X,j_*L).
\end{split}
\tag{A.13}
\]
The final zero and the top isomorphism use the vanishing of positive cohomology on the finite boundary. The quotient \(H^1(X,j_*L)\) has upper bound \(a+1\). Ordinary parabolic curve duality pairs it perfectly with \(H^1(X,j_*(L^\vee(1)))\). The latter has upper bound \(-a-1\) by (A.7), so reciprocal eigenvalues give the reverse bound \(a+1\) on the original group. It is pure of weight \(a+1\). This is ordinary curve duality, not proper perverse purity. Algebraicity follows from the independent algebraic Euler-product and top-determinant argument in the strict estimate.

The full boundary grading already proved makes \(i^*j_*L\) mixed of integral weights at most \(a\). Finite-set cohomology preserves that filtration. Sequence (A.13) therefore expresses \(H_c^1(U,L)\) as an extension of a quotient of this boundary group by the pure group of weight \(a+1\), supplying an actual integral mixed filtration. Ordinary cohomology long exact sequences handle mixed lisse inputs, and (A.8) handles constructible curve inputs. \(\square\)

The improvement and the final localization are Weil II, 3.2.4–3.2.15. The proof records the real-sheaf input, nonconstant/integer distinction and all three Leray terms. Appendix B supplies the geometry and transverse support reduction, and Appendix C supplies the arithmetic local formulas and exact specialization sequence. Their stated ordinary cohomological foundations remain required. Appendix D uses this curve theorem for the higher-dimensional compact-support estimate. Appendix E derives the remaining mixed-operation stability from it and the stated ordinary foundations.

### Intermediate extension on a smooth curve

**Proposition.** Let \(j:U_0\hookrightarrow C_0\) be a dense open of a smooth curve, and let \(L_0\) be lisse and pointwise pure of weight \(a\). Then \(j_{!*}L_0[1]\) is pure of weight \(a+1\). This follows from the independent boundary argument above and curve duality, before Theorem 4.1, Gabber's criterion or higher-dimensional IC purity.

**Proof.** The ordinary sheaf \(j_*L_0\) is mixed of weights \(\le a\) by the preceding proposition. The curve intermediate extension is \(P_0=j_*L_0[1]\). At a boundary point, the ordinary inertia-cohomology description of \(Rj_*L[1]\) has groups \(V^{I_x}\) in degree \(-1\) and \(H^1(I_x,V)\) in degree zero. Truncating away the latter gives \(j_*L[1]\). Localization, and \(i_x^!Rj_*=0\), give its costalk \(H^1(I_x,V)[-1]\), in degree one. Thus it is perverse and has neither a subobject nor a quotient supported on the boundary; lesson 4's characterization identifies it with \(j_{!*}L[1]\). This calculation uses ordinary curve inertia cohomological dimension, including wild invariants.

Its sole ordinary cohomology sheaf, in degree \(-1\), has weights \(\le a\), so \(P_0\le a+1\). Duality of intermediate extension and smooth curve duality give
\[
D_{C_0}P_0=j_{!*}(L_0^\vee(1)[1])
=j_*(L_0^\vee(1))[1].
\]
The dual twisted local system is pointwise pure of weight \(-a-2\). The already proved boundary result applied to it gives \(D_{C_0}P_0\le-a-1\), hence \(P_0\ge a+1\) by (2.1). Both bounds prove purity, including the fixed-embedding version. \(\square\)


### Growth under products of curve covers

We will prove the perverse weight assertions from the ordinary estimates above, using the pure-curve continuation just proved. The curve cohomology used below also includes the Euler characteristic formula
\[
\chi_c(V,L)=\operatorname{rank}(L)\chi_c(V,\Lambda)
-\sum_{x\in\bar V\setminus V}\operatorname{Swan}_x(L),
\tag{A.14}
\]
for a smooth curve \(V\), a lisse sheaf \(L\), and its smooth proper compactification \(\bar V\). This ordinary input remains separate from Gabber's criterion. The preceding curve-purity proof did not use the general intermediate-extension purity theorem which we are about to deduce.

First note that perverse truncation preserves mixedness. The construction in [The perverse t-structure](the-perverse-t-structure.md) uses, on a dense regular open where all ordinary cohomology is lisse, an ordinary truncation with the dimension shift. It then uses open–closed localization and the already constructed truncation on the smaller closed complement. Ordinary truncation and the six operations preserve mixedness. Induction on dimension therefore proves the assertion, without any weight bound on perverse cohomology.

Mixed perverse sheaves also form a Serre subcategory. Here is a useful proof of the point that a subobject need not be an ordinary subsheaf. Take a simple perverse subobject \(S\) of a mixed perverse sheaf \(P\), and let \(Z\) be its support. After shrinking to a regular dense open of \(Z\), write \(S=L[d]\). Adjunction puts this local system in the degree \(-d\) cohomology of the exceptional restriction of \(P\). The latter is mixed and, on this open, has ordinary degrees at least \(-d\). Thus \(L\) is mixed. Its intermediate extension is mixed: it is the image of the map between the degree-zero perverse cohomology of \(j_!L[d]\) and \(Rj_*L[d]\), and kernels, cokernels and images of maps between mixed objects are computed by cones and perverse truncation. The simple-object classification identifies this extension with \(S\). The quotient \(P/S\) is mixed by its triangle. Repeating gives a finite composition series with mixed terms. Intersecting an arbitrary subobject with that series proves mixedness of every subobject and quotient.

On a curve the simple terms of this series are pure. A point-supported simple is an irreducible Frobenius representation. A positive-dimensional simple is the intermediate extension of an irreducible mixed lisse sheaf. On a smaller open all steps of its ordinary mixed filtration are lisse; irreducibility leaves just one pure step. The pure-curve continuation theorem then applies. This curve assertion precedes the higher-dimensional purity theorem.

**Lemma A.1 (growth on products of curves).** Let \(C_1,\ldots,C_n\) be smooth proper connected curves over an algebraically closed field, and \(C=\prod C_a\). Fix a bounded constructible complex \(K\) on \(C\). Pull it back to products \(\widetilde C\) of connected finite étale covers of the \(C_a\), each of degree \(D\). There is a constant independent of the covers such that every Betti number is \(O(D^n)\). If \(K\in{}^pD^{\le0}\), then, for \(r>0\),
\[
\dim H^r(\widetilde C,K)=O(D^{n-r}),
\quad H^r(\widetilde C,K)=0\ (r>n).
\tag{A.15}
\]
For \(K\in{}^pD^{\ge0}\), the analogous estimate holds in negative degrees with exponent \(n-|r|\).

**Proof.** The upper half is built, by ordinary truncation, from sheaves \(F[N]\) with \(\dim\operatorname{Supp}F\le N\). Finite triangles preserve both estimates, so these suffice. Induct on \(n\), the point case being immediate. Project to \(C_1\). Generic constructible local acyclicity gives a nonempty open \(V\subsetneq C_1\) on which the projection and \(F\) are locally acyclic and their direct-image sheaves are lisse. This is the generic local-acyclicity prerequisite, beyond smooth local acyclicity alone. Split off the finitely many omitted fibres by localization. A complex supported on one such fibre has, after covering, \(D\) copies of the cohomology on the product of the other curves. Ordinary restriction preserves the upper perverse half. Induction gives \(O(D^n)\) in all degrees and \(O(D^{n-r})\) in positive degree \(r\), as required.

For the remaining extension by zero from the inverse image of \(V\), put \(Y=\prod_{a>1}C_a\). Its restriction to a geometric generic fibre, shifted by \([-1]\), is upper-perverse on \(Y\): the dimension of the support of \(F\) drops by at least one. Write \(L_q\) for the lisse degree-\(q\) direct-image sheaf over \(V\), after making the covers of the other curves. Proper base change and induction give
\[
\operatorname{rank}L_q
=\dim H^{q+1}(\widetilde Y,K_\eta[-1])
=O(D^{n-q-2})\quad(q\ge0),
\tag{A.16}
\]
with zero when the exponent is negative; in every degree the bound is \(O(D^{n-1})\).

The same bounds hold for the Swan conductors at each omitted point. Indeed, proper nearby-cycle base change expresses the local inertia representation of \(L_q\) as
\[
H^{q+1}(\widetilde Y,R\psi K[-1]).
\tag{A.17}
\]
The upper nearby-cycle bound is proved in [Nearby and vanishing cycles](nearby-and-vanishing-cycles.md#the-%C3%A9tale-proof-keeps-full-inertia), independently of weights. The wild action on the fixed bounded constructible cycle object has finite image: its continuous action on its finite-dimensional endomorphism algebra preserves a lattice, and a pro-\(p\) group has trivial intersection with the pro-\(\ell\) congruence kernel. This fixed finite quotient and its ramification breaks also act on every pulled-back object and its cohomology. The definition of Swan conductor as a finite weighted sum of the codimensions of ramification-group invariants therefore bounds it by a fixed constant times the dimension in (A.17). Induction applies. This argument includes wild inertia.

#### A fixed wild quotient for all curve covers

**Lemma A.1a (uniformity of the conductor bound).** The finite-image step in (A.17) uses one fixed nearby-cycle object, not a newly chosen monodromy bound for each cover. More generally, let \(E/\mathbf Q_\ell\) be finite, let \(I\) be the inertia group of the strict henselian curve trait under consideration, with wild subgroup \(P\) and residue characteristic \(p\ne\ell\), and let \(M\) be an object with a continuous action
\[
\rho:I\longrightarrow A^\times,
\qquad A=\operatorname{End}(M),\qquad \dim_E A<\infty.
\tag{A.W1}
\]
The continuity is for the \(E\)-vector-space topology on \(A\). There is a real \(b\ge0\), depending only on this action and this trait, such that every finite-dimensional representation \(W\) obtained by applying an \(E\)-linear functor to this same equivariant object satisfies
\[
I^u\text{ acts trivially on }W\quad(u>b),
\qquad \operatorname{Swan}(W)\le b\dim_E W.
\tag{A.W2}
\]
Here \(I^u\), for \(u>0\), is the upper wild ramification filtration used in the definition of the conductor in (A.14). The functor must carry the given action to the action on \(W\); one cannot add an unrelated parameter character afterwards. In residue characteristic zero the wild group is trivial and the assertion has \(b=0\).

**Proof.** The useful faithful representation is **left multiplication** on \(A\), not conjugation on \(A\): a nontrivial scalar automorphism would be invisible to conjugation. The action of \(P\) is compact. Start with an \(O_E\)-lattice \(L_0\subset A\). Boundedness of its compact family of translate matrices puts their sum inside \(\pi^{-a}L_0\) for some \(a\); this sum contains \(L_0\) and is finitely generated over the Noetherian valuation ring. It is therefore an invariant lattice \(L\). The kernel of
\[
\operatorname{GL}(L)\longrightarrow\operatorname{GL}(L/\pi L)
\tag{A.W3}
\]
is pro-\(\ell\): successive congruence quotients are subgroups of the finite additive matrix groups over the residue field, and their intersection is the identity. The compact image of the pro-\(p\) group \(P\) is a pro-\(p\) group. Its intersection with that kernel is both pro-\(p\) and pro-\(\ell\), hence trivial, since all its finite quotients are trivial. Its image injects into the finite group on the right of (A.W3). Thus \(\rho(P)\) is finite. This is the faithful-lattice argument of Nearby and vanishing cycles, Appendix B, applied to the entire endomorphism algebra in (A.W1), rather than only to selected stalk representations.

Put \(N=\ker(\rho|_P)\). It is open in \(P\) with its subspace topology. A sufficiently small open normal subgroup \(J\) of the profinite group \(I\) has \(J\cap P\subseteq N\). Hence the action of the image of \(P\) is detected by the single finite quotient \(I/J\). In this finite quotient the ramification groups are the identity above a finite upper break \(b\). Finiteness of that bound is part of the elementary finite-extension filtration: each nonidentity automorphism moves some integral element, whose difference has finite valuation; taking a maximum over the finite group kills the lower groups at a finite index. The increasing, piecewise-linear upper reindexing carries this to a finite upper bound. We use the quotient-compatible upper filtration of the conductor definition, not an identification of lower indices across changing quotients.

For \(u>b\), the subgroup \(I^u\) lies in \(J\cap P\), and therefore acts as the identity on \(M\). Any functor carrying its action sends those identity morphisms to identities on \(W\). The same \(b\) works for every such functor, regardless of the dimension of \(W\). By the upper-filtration definition,
\[
\operatorname{Swan}(W)
 =\int_0^b\operatorname{codim}_E W^{I^u}\,du
 \le b\dim_E W.
\tag{A.W4}
\]
Endpoints of the finitely many jumps do not affect the integral. This proves both assertions. No bound on the tame image, and no semisimplicity of the full inertia action, was assumed. \(\square\)

**Application to (A.17).** At each of the finitely many omitted points of \(C_1\), use the fixed object \(M=R\psi K[-1]\) on \(Y\). Nearby and vanishing cycles, Lemma B.0 supplies finite-dimensional derived endomorphisms and continuity of this actual whole-object inertia action, using complete integral Hom, its coefficient topology and finite-stage factorization of the identity. Its normalized coefficient comparison is Lemma C.2a below. Bounded constructibility of the first nearby reduction remains the geometric Appendix A input; the finiteness lemma does not replace it. Lemma A.1a then gives the fixed wild quotient and its uniform conductor bound. These arguments retain the arbitrary algebraically closed field in Lemma A.1; it is not silently replaced by the algebraic closure of a finite field.

An allowed cover \(v:\widetilde Y\to Y\) is defined over the algebraically closed constant field. Its product with the strict curve trait has no additional inertia action on the cover. Étale base change identifies the pulled nearby object with \(v^*M\), and the proper nearby-cycle comparison identifies its cohomology with the representation in (A.17). Both are the canonical equivariant comparisons, not merely equalities of dimensions. Consequently \(H^{q+1}(\widetilde Y,v^*M)\) carries exactly the functorially induced action to which Lemma A.1a applies.

The full-inertia perverse bound, Appendix B, including its regular-representation recovery and finite truncation argument, gives the upper-perverse input used in the induction. It does not discard the wild summand by replacing nearby cycles with tame invariants. Thus the dimension estimate in (A.17) gives the same exponent for its Swan conductor. There are only finitely many omitted points; take the largest of their fixed constants. Every cover and every cohomological degree then use that common bound. Extending a finite coefficient field preserves the ranks of invariant idempotents and hence these conductors, so the usual finite-coefficient-field interpretation gives the stated \(\overline{\mathbf Q}_\ell\) case as well.

**Separate inputs, proved below.** Formula (A.14) is the full Grothendieck–Ogg–Shafarevich input, including wild conductors. The subsection *The full curve conductor formula* supplies its proof and normalization. A Frobenius trace formula for curves or finite-dimensionality of curve cohomology does not prove it. The generic constructible local-acyclicity of the fixed \(F\) and cover-independent open \(V\) required in Lemma A.1 are supplied below by the ordinary argument, Corollary A.1m, and the general-field rational comparison of Lemma A.1n and Corollary A.1o. Smooth/locally constant local acyclicity alone would not have supplied that input. The fixed wild-quotient deduction remains a separate argument.

#### The common open and its exact local-acyclicity inputs

The open used before (A.16) must be chosen **before** any of the covers. Making each covered direct image lisse on its own generic open would not supply a common open for infinitely many covers. The relevant human source is Deligne, [SGA \(4\frac12\), *Cohomologie étale*](https://publications.ias.edu/sites/default/files/Number32.pdf), “Théorèmes de finitude”, 2.13–2.15, printed pp. 242–243. Its smooth-postcomposition input 2.14 is proved in Illusie's appendix, 2.1–2.7, printed pp. 256–259, using the finite-base-change criterion 1.1, pp. 252–253. The following argument supplies the ordinary generic reduction. Proposition A.1c and Corollary A.1m discharge its postcomposition input, and Lemma A.1n with Corollary A.1o supplies the rational common-open comparison at the full algebraically closed-field scope used here. This deduction requires the exact geometric and coefficient prerequisites of the cited propositions.

**Lemma A.1b (finite defects of a proper map are detected).** Let \(S\) be Noetherian, let \(f:X\to S\) be proper, and let \(A\) be a left-Noetherian ring killed by an integer invertible on \(S\). Let \(H\in D^b_c(X_{\mathrm{\acute et}},A)\). Suppose its possible failures of universal local acyclicity lie in a closed \(T\subset X\) finite over \(S\). If the cohomology sheaves of \(Rf_*H\) are locally constant, then \(f\) is universally locally acyclic relative to \(H\).

Here the support hypothesis means that after every \(S'\to S\), local acyclicity holds outside the inverse image of \(T\). It is not just an assertion about one geometric generic fibre. For a geometric specialization \(t\to S_{(s)}\), write
\[
X_s\xrightarrow{i}X_{S_{(s)}}\xleftarrow{u}X_t,
\qquad
\Delta_{s,t}(H)=\operatorname{Cone}
 \bigl(i^*H\longrightarrow i^*Ru_*(H|_{X_t})\bigr).
\tag{A.U1}
\]
The arrow is the restricted adjunction unit. It is not an unspecified isomorphism between stalk vector spaces.

**Proof.** Constructible complexes, BZ.1–BZ.2 proves the actual cone comparison under a proper map. Apply it with the map from the base to itself as its second map. The comparison gives
\[
R\Gamma(X_s,\Delta_{s,t}(H))
 \simeq\operatorname{Cone}
 \bigl((Rf_*H)_s\longrightarrow(Rf_*H)_t\bigr).
\tag{A.U2}
\]
The map on the right is specialization, through the same units and restrictions as in (A.U1). The proof in BZ.2 uses BE.7–BE.8, whose proper comparison holds for bounded-below torsion complexes without a constructibility assumption on the nearby-cycle term. It therefore does not assume the finiteness assertion being sought. For left \(A\)-modules, the underlying-torsion comparison and its adjunction maps are exactly those checked in the left-module part of E.2m; forgetting the module structure detects a quasi-isomorphism.

Local constancy makes the specialization in (A.U2) an isomorphism on every cohomology sheaf, so its cone vanishes. On the other hand, (A.U1) is supported on \(T_s\). The finite-support formula (BZ.6), applied to the closed-support complex, identifies its global cohomology with the finite direct sum of its geometric stalk complexes. A finite direct sum is zero if and only if every summand is zero in every degree. Hence \(\Delta_{s,t}(H)=0\). This is detection by the complex, not by an Euler characteristic, where cancellation could occur.

After an arbitrary base change, proper comparison identifies the new direct image with the pullback of \(Rf_*H\). Its cohomology is still locally constant, the support remains finite, and the same bounded-below comparison applies even if the new base is not Noetherian. Repeat (A.U1)–(A.U2) there. This proves universality. \(\square\)

**The geometric reduction in the generic theorem.** Here is the part of the dimension induction which locates those finite defects. Work over an integral affine Noetherian \(S=\operatorname{Spec}R\), with generic field \(Q\), and let the dimension of the generic source be at most \(d\). The induction hypothesis is the full generic ULA statement in dimensions less than \(d\), for every integral Noetherian base. A second, separate input is:

> (PC) If \(a:W\to B\) is universally locally acyclic relative to a bounded constructible torsion complex and \(b:B\to S\) is smooth, then \(ba\) is universally locally acyclic relative to that same complex.

PC is “Théorèmes de finitude” 2.14, not merely smooth ULA for a locally constant sheaf on \(W\). The argument below is conditional on PC; smoothness of the original source alone does not imply PC.

Take an affine chart \(W\) of the source and a closed embedding \(W\hookrightarrow\mathbf A^m_R\). For each coordinate \(z_j\), regard \(W\) as a scheme over \(\mathbf A^1_R\). Any generic component on which \(z_j\) is algebraic over \(Q\) disappears over the fraction field of the parameter line. On every other component, the transcendence-degree dimension formula in M.1 drops the generic dimension by one. Thus this coordinate map has generic dimension at most \(d-1\), or empty generic source. The algebraic-component case must not be treated as a dominant map of unchanged dimension.

The induction hypothesis provides a dense open \(V_j\subset\mathbf A^1_R\) on which this coordinate map is ULA. For an empty generic source, the same conclusion follows by clearing the equation \(1=0\) on finitely many affine charts and removing its image. Since \(V_j\) meets the generic point of \(\mathbf A^1_R\), its closed complement on \(\mathbf A^1_Q\) lies in the zero set of a nonzero monic polynomial. Choose such a polynomial, lift its coefficients after one localization of \(R\), and shrink \(S\) further so that the whole complement is contained in its zero set. To justify the last step, the part of that complement where the polynomial is nonzero is a finite-type scheme with empty generic fibre; a finite affine cover again clears the equation \(1=0\). We obtain monic polynomials \(h_j\in R[z_j]\) such that
\[
T_W=W\cap\bigcap_{j=1}^m V(h_j(z_j)),
\qquad
T_W\longrightarrow S\text{ is finite}.
\tag{A.U3}
\]
Indeed its coordinate algebra is a quotient of
\[
R[z_1,\ldots,z_m]/(h_1(z_1),\ldots,h_m(z_m)).
\tag{A.U4}
\]
Repeated monic division spans this algebra by the monomials whose exponent in \(z_j\) is less than \(\deg h_j\). The quotient need not be flat; finite generation is all that is needed. If one polynomial is \(1\), the intersection is empty. No point-counting or assumption that \(R\) is a field enters this argument.

Off \(T_W\), some coordinate lies in \(V_j\). PC, applied to \(V_j\to S\), then proves ULA there. For \(d=0\) all coordinate generic sources are empty, so this construction starts the induction without an appeal to a negative-dimensional case. In dimension \(d>0\) it uses only already established dimensions, never the desired theorem at dimension \(d\).

To complete this conditional induction, localize on the original source, take the projective closure of each affine chart, and extend the coefficient complex by zero. Its generic dimension is unchanged; restriction back to the affine open preserves the actual local-fibre comparisons. For a proper source use finitely many affine charts and the preceding construction on each. Let \(E_f(H)\) be the closed failure locus defined using all base changes in BZ.1. Its intersection with each chart is closed in the finite \(T_W\), hence finite over \(S\). Thus \(E_f(H)\to S\) has finite fibres. It is proper because it is closed in the proper source, so AU.6 makes it finite over the Noetherian base. This is why the closure of the failure locus causes no unnoticed boundary component.

E.2m makes the proper direct image bounded constructible. There are only finitely many nonzero cohomology sheaves. On an integral Noetherian base, each is locally constant on a dense open by its finite constructible partition. Intersect these finitely many opens. Lemma A.1b removes the remaining finite defect. A finite source cover gives the original, possibly non-separated, finite-type source. Bounded complexes use their finite cohomology towers and exactness of the local comparison cone. This proves the ordinary generic theorem over the integral base using PC, now supplied by Proposition A.1c and Corollary A.1m, and the explicitly linked earlier providers. In particular it explains the reduction required over the integral curve \(C_1\) without replacing a constructible sheaf by a lisse one on the entire source.

**Why covers do not require new opens.** Suppose the generic ULA input for the fixed complex on \(Y\times C_1\) has supplied \(V\). An étale map of sources identifies strict localizations at selected compatible geometric points. AT.1–AT.4 and BZ.1 identify both the local fibres and their unit maps. Thus every finite étale \(\widetilde Y\to Y\) preserves ULA over this same \(V\), and ULA also persists after any change of the curve base. It is essential to use the selected strict-local factor, not the entire product with every lift.

For the proper projection \(\widetilde Y\times V\to V\), the cone comparison (A.U2) now says that all geometric specialization maps on its ordinary direct-image cohomology are isomorphisms. Its cohomology is bounded constructible by the proper-support part of E.2m. Here is the local-constancy check for finitely generated left-module stalks. A stalk module \(M\) is finitely presented, since \(A\) is left-Noetherian. Lift its finite generators and finite relations to one pointed étale neighbourhood to obtain \(\underline M\to\mathcal H^q\). This is an isomorphism at the chosen point. Naturality of the invertible specialization maps makes its isomorphism locus stable under specialization and generization. Remove the finitely many irreducible components of this Noetherian neighbourhood not containing that point. Each remaining generic point is a generization of it, and each other point specializes from such a generic point, so the map is an isomorphism on all geometric stalks. This proves local constancy without shrinking \(V\) for that cover. Bounds or ranks may vary with the cover; the open does not.

**The completed coefficient comparison and its limit.** A separate exact implication is available for the reduction-defined complete category of E.2n. Let \(P\) be a derived-complete constant-\(O\) complex whose first derived reduction is a bounded classical constructible complex \(P_1\). If \(f\) is ULA for \(P_1\) on \(V\), then its completed local-fibre comparison for \(P\) is invertible on \(V\), after every base change. Form the comparison using completed inverse images at the geometric point and on the selected local geometric fibre. Both its source and its derived-sections target are complete: right adjoints preserve the product-cone defining completion. The perfect two-term coefficient resolution and BK.2–BK.6 identify reduction of this very arrow with the ordinary local-fibre comparison for \(P_1\). Its cone \(Q\) therefore satisfies
\[
Q\simeq R\varprojlim_n(Q\otimes_O^L O/\pi^n),
\qquad Q\otimes_O^L O/\pi=0
\quad\Longrightarrow\quad Q=0.
\tag{A.U5}
\]
For the last implication, the first coefficient triangle makes multiplication by \(\pi\) invertible; its powers are invertible, so all higher reduction cones vanish, and completeness gives zero. These maps are the unit-induced maps, as in E.2n, not abstract identifications of their reductions. This proves the completed implication on one first-reduction open, not an intersection of infinitely many opens. The selected local geometric fibres are affine, hence qcqs, so BK.2's classical comparison applies.

This implication does **not** reduce a rational complex modulo \(\pi\), which would give zero information, and does not presume that naive inverse image preserves completion. Lemma A.1n below supplies the actual integral-model, coefficient-ring, ringed inverse-image and rationalization comparisons over every algebraically closed ground field required in Lemma A.1. Its providers BW–BX have that broader field scope; E.2n.1 itself retains its finite-field statement.

**The common-open comparisons are supplied below.** Proposition A.1c and Lemmas A.1d–A.1m provide the ordinary comparison for the strict-local map \(X_{(x)}\to B_{(b)}\), its finite-base-change property and postcomposition input. Lemma A.1n transports the actual local-fibre arrow to rational coefficients at the algebraically closed-field scope of Lemma A.1, and Corollary A.1o applies the ordinary generic argument with one first reduction. The finite-defect test, monic-coordinate reduction and cover-uniformity deduction are retained. These arguments do not use weights or the Grothendieck–Ogg–Shafarevich formula; (A.14) is proved separately in the full curve conductor subsection.

#### The strict-local postcomposition map

The implication (PC) can be separated into a canonical comparison and one exact geometric input. We prove the comparison here and isolate that input without changing the statement of the generic theorem. The source for the finite-base-change route is Illusie's appendix to Deligne's [*Cohomologie étale*](https://publications.ias.edu/sites/default/files/Number32.pdf). Its use of local acyclicity concerns all geometric specializations, not merely equality of the dimensions of nearby cohomology groups.

**The finite descent calculation.** Let \(v:T\to B\) be a finite surjection of schemes and let \(A\) be a sheaf of rings on \(B\). No flatness of \(v\), commutativity of \(A\), or invertibility of the degree of \(v\) is assumed. Put \(T_r=T\times_B\cdots\times_BT\), with \(r+1\) factors, and let \(v_r:T_r\to B\). For a sheaf \(M\) of left \(A\)-modules, the augmented complex
\[
0\longrightarrow M\longrightarrow v_{0*}v_0^*M
 \longrightarrow v_{1*}v_1^*M\longrightarrow\cdots
\tag{A.P1}
\]
is exact. Its differential is the alternating sum of the pullbacks which omit one factor. This is descent through a finite surjection, not an assertion that \(v\) is an étale covering.

Indeed Constructible complexes, AX.5 proves exact finite direct image and its arbitrary-base stalk formula. At a geometric point \(b\), write \(I\) for the nonempty finite set of geometric lifts to \(T\). The degree-\(r\) term of (A.P1) is the group of functions \(I^{r+1}\to M_b\). Choose \(i_0\in I\) just for this stalk calculation. Inserting \(i_0\) as the first argument gives a degree-minus-one operator \(h\). Expanding the alternating sums gives
\[
dh+hd=1
\tag{A.P2}
\]
on the augmented complex: all terms involving deletion after the inserted argument cancel in pairs, and deleting that first argument leaves the original function. The same identity includes the augmentation in degree minus one. Exactness follows on every stalk. The contraction need not glue, and no choice of a global section of \(v\) is claimed.

For \(E\in D^+(B_{\mathrm{\acute et}},A)\), apply (A.P1) degreewise to a bounded-below representative. In horizontal degree \(r\) and internal degree \(q\), take the total differential to be \(d_{\mathrm{Cech}}+(-1)^r d_E\). The two parts then anticommute. In every total degree only finitely many terms occur, since \(r\geq0\) and \(q\) has a fixed lower bound. Thus the total augmented resolution is a quasi-isomorphism. Finite direct image is exact and preserves injectives, its inverse-image left adjoint being exact; consequently the same construction computes the corresponding derived direct images. This proves bounded-below finite-surjective cohomological descent with its actual maps.

Here is the related cone argument used in the finite-base-change criterion. Suppose a comparison is resolved by such a simplicial cover, and write \(C_r\) for the cone in column \(r\). If all these cones have zero cohomology in degrees at most \(N\), and column zero is acyclic in every degree, then their total cone has zero cohomology in degrees at most \(N+1\). In the column spectral sequence a term contributing to degree \(n\leq N+1\) has the form \(H^{n-r}(C_r)\). For \(r=0\) it is zero by the stronger hypothesis; for \(r>0\), \(n-r\leq N\). The common lower bound makes the filtration finite in each degree. This is the degree-raising induction, not a claim that an arbitrary nonzero Čech column may be discarded.

**The exact additional input.** For a locally acyclic map \(a:W\to B\), a geometric point \(w\), and its image \(b\), let
\[
a_w:W_{(w)}\longrightarrow B_{(b)},\qquad E^{\mathrm{loc}}_w=E|_{W_{(w)}}.
\tag{A.P3}
\]
The input required below is:

> (FB) Formation of \(Ra_{w*}E^{\mathrm{loc}}_w\) commutes with every finite change of base over \(B_{(b)}\), by the canonical adjunction base-change map.

This is Illusie's Corollary 2.6. It is not a consequence of finite direct image alone: \(a_w\) need not be finite. Lemmas A.1d–A.1k and Theorem A.1l below supply the normalization and cospecialization route, and Corollary A.1m discharges (FB). The conditional proof that follows is retained with its actual maps; its additional ordinary input is now available.

We first spell out a consequence of (FB) needed twice. Finite base change extends to quasi-finite separated changes and to affine inverse limits of those changes. Locally on the changing scheme, AW.5 factors a separated quasi-finite map as an open immersion into a finite map. The finite part uses (FB); the open part uses the restriction of the direct-image resolution to the open subsite. Quasi-isomorphisms are local on this changing scheme, so these comparisons glue. For an affine inverse limit use BA.5 on affine étale test objects and their inverse images. The morphism (A.P3) is affine, since both its schemes are affine, so these inverse images are qcqs. The lower bound on \(E^{\mathrm{loc}}_w\) makes the cohomological comparison a finite-diagonal argument. These constructions extend the canonical arrow; they do not replace it by an abstract isomorphism.

A geometric point obtained by taking a separable algebraic closure of a residue field is such an inverse limit of separated quasi-finite changes. For \(B=\operatorname{Spec}R\), write its residue field as the localization of \(R/\mathfrak p\) at the nonzero elements. The quotient is a closed immersion and each localization is an open immersion. A separable algebraic closure is the filtered union of finite field extensions. These extensions, their defining equations, and finitely many required inverses descend to finite algebras after a further localization. Affine composition gives the asserted system. Such points suffice to test isomorphisms of étale sheaves. An arbitrary larger geometric field is not automatically an algebraic extension, and its treatment below is a separate step.

**Proposition A.1c (postcomposition under (FB)).** Let \(W\xrightarrow{a}B\xrightarrow{b}S\) be qcqs morphisms and \(E\in D^+(W_{\mathrm{\acute et}},A)\), where \(A\) is a locally constant sheaf of rings pulled back from \(S\) and killed by an integer \(n\) invertible on \(S\). Assume that \(a\) is locally acyclic relative to \(E\), that (FB) holds for its strict-local maps, and that \(b\) is locally acyclic relative to every locally constant left-module coefficient sheaf. Then \(ba\) is locally acyclic relative to \(E\). If these hypotheses hold after every base change of \(S\), the conclusion is universal. Smooth \(b\) satisfies the coefficient hypothesis by AT.2–AT.3. This includes the full ordinary-coefficient scope required in (PC); it makes no assertion for residue-characteristic torsion.

**Proof.** Choose \(w\), with images \(b_0\) and \(s\). Work on the selected strict localizations
\[
W_0=W_{(w)}\xrightarrow{a_0}B_0=B_{(b_0)}
 \xrightarrow{b_0'}S_0=S_{(s)}.
\tag{A.P4}
\]
The notation \(b_0'\) denotes the induced morphism, not a new geometric point. The coefficient ring becomes constant here. Write \(M=E_w\) for the stalk complex. AT.1 identifies \(R\Gamma(W_0,E)=M\) by the actual closed-stalk map. The counit from constant sheaves to sections, followed by the direct-image adjunction, therefore gives a specified morphism
\[
\underline M_{B_0}\longrightarrow Ra_{0*}(E|_{W_0}).
\tag{A.P5}
\]
For a geometric \(z\to B_0\), (FB) and its inverse-limit extension identify the target stalk with
\(R\Gamma(W_0\times_{B_0}z,E)\). Under this identification the stalk of (A.P5) is precisely restriction from \(M\) to that local geometric fibre. Local acyclicity of \(a\) at \(w\) says that this restriction is an isomorphism. Thus (A.P5) is a quasi-isomorphism on all geometric stalks, and hence on \(B_0\). We have proved constancy of this particular derived direct image without assuming its constructibility, and without inferring constancy just from equal ranks.

First choose a geometric specialization \(t\to S_0\) whose field is a separable algebraic closure of its residue field, and put \(B_t=B_0\times_{S_0}t\) and \(W_t=W_0\times_{S_0}t\). Base changing the inverse-limit description of \(t\to S_0\) makes \(B_t\to B_0\) an affine inverse limit of separated quasi-finite maps. Consequently the already justified extension of (FB), followed by derived composition of sections, gives
\[
R\Gamma(B_t,(Ra_{0*}E)|_{B_t})
 \xrightarrow{\sim}R\Gamma(W_t,E).
\tag{A.P6}
\]
By (A.P5) its left side is \(R\Gamma(B_t,\underline M)\). Local acyclicity of \(b\) for constant coefficient sheaves identifies this with \(M\). The same holds for the bounded-below complex \(M\): the hypercohomology filtration has terms \(H^p(B_t,\underline{H^q(M)})\), which vanish for \(p>0\); the degree-zero terms are \(H^q(M)\) by their constant-section maps. Fixed total degrees again have finite filtrations. Combining these arrows proves
\[
E_w\longrightarrow R\Gamma(W_{(w)}\times_{S_{(s)}}t,E)
\quad\text{is an isomorphism}.
\tag{A.P7}
\]
It is the required local-acyclicity arrow: (A.P5) comes from the section counit, and (A.P6) from base-change adjunction and restriction. The triangle identities identify their composite with restriction of that same section to \(W_t\), not merely with an isomorphism of its cohomology groups.

For completeness, allow any separably closed geometric field \(L\) above the same residue point. Choose an embedded separable algebraic closure \(K\) of that residue field inside \(L\), and compatible algebraic closures \(\overline K\subset\overline L\). The vertical extensions from the separably closed fields are purely inseparable. BE.4 proves that their induced inverse images on étale sheaves are equivalences, by the actual stalk units and counits. Over the perfect field \(\overline K\), each finitely generated subfield of \(\overline L\) is the function field of an integral finite-type scheme with a nonempty smooth open, as in M.1. Its spectrum is the affine inverse limit of affine opens within that smooth open. Taking all finitely generated subfields expresses \(\operatorname{Spec}\overline L\to\operatorname{Spec}\overline K\) as an affine inverse limit of smooth maps. AS.7 therefore gives cohomology comparison for the qcqs scheme \(W_t\) and its bounded-below torsion complex. Together with the two purely inseparable equivalences, it proves that (A.P7) remains the same isomorphism after \(K\subset L\). This supplies the larger-field case; it does not label a transcendental extension quasi-finite. Module structures are retained by the canonical maps, and forgetting to underlying torsion groups detects the quasi-isomorphisms.

We have proved the assertion for every \(w,t\). Applying the identical construction after each change of \(S\) proves the universal assertion. For smooth \(b\), AT.3 supplies exactly the arbitrary-base torsion coefficient assertion used above. \(\square\)

**The postcomposition and coefficient inputs.** Proposition A.1c gives the composition argument under (FB), and Corollary A.1m proves that input. Checking only the closed point of a strict local base would still be insufficient; Lemmas A.1f–A.1i and Theorem A.1l supply the all-target-stalk comparison, transitivity and arbitrary-base reduction. Lemma A.1n then provides the rational coefficient passage over every algebraically closed field needed here. The full conductor identity (A.14) has its separate proof in the conductor subsection below.

#### Integral normalization covers and the local comparison

The normalization used in [Illusie's appendix, Proposition 1.1 and §2](https://publications.ias.edu/sites/default/files/Number32.pdf) need not be finite over the original scheme. Thus the finite-cover calculation (A.P1) must be extended before it can be applied to that proof. We give the extension and the normalized local calculation here. We do not infer the whole finite-base-change criterion from a comparison at one closed point.

**Lemma A.1d (integral-surjective descent).** Let \(v:T\to B\) be an integral surjection of qcqs schemes, let \(A\) be a sheaf of rings on \(B\), and let \(E\in D^+(B_{\mathrm{\acute et}},A)\). Rings and left modules need not be commutative, finite, or torsion. Put \(T_r=T^{r+1}_B\) and write \(v_r:T_r\to B\). The canonical augmentation is a quasi-isomorphism
\[
E\longrightarrow\operatorname{Tot}_{r\geq0}
 Rv_{r*}v_r^*E.
\tag{A.N1}
\]
This remains true after any change of base. In particular it applies to an integral normalization cover, without asserting that its algebra is a finite module.

**Proof.** The assertion is local on \(B\), so take \(B=\operatorname{Spec}R\) and \(T=\operatorname{Spec}D\). Express \(D\) as the filtered union of its finitely generated \(R\)-subalgebras \(D_i\). Each generator satisfies a monic equation over \(R\); reducing powers by those equations gives a finite spanning set of products. Hence each \(D_i\) is finite over \(R\). A finite presentation is not needed here. Each \(\operatorname{Spec}D_i\to B\) is surjective, because the surjection from \(T\) factors through it. An inclusion \(D_i\subset D_j\) is integral, so its map on spectra is also surjective. This gives
\[
T=\varprojlim_i T_i,\qquad
T_i\longrightarrow B\text{ finite and surjective}.
\tag{A.N2}
\]
The same diagonal system computes each finite fibre power \(T_r\): every finite list of elements and relations in a tensor product occurs at a common stage. All its transition maps are affine.

Fix a geometric point \(b\) of \(B\). After passage to \(B_{(b)}\), the finite schemes \(T_i\) are finite disjoint unions of strictly local schemes by Constructible complexes, AX.5. Let \(I_i\) be their finite nonempty sets of geometric lifts of \(b\). Their transition maps are surjective. The inverse limit \(I=\varprojlim I_i\) is nonempty and profinite. One can see nonemptiness by the finite-intersection property in the product of the finite discrete sets: any finite list of compatibility conditions is satisfied using a common later stage. The same argument shows that the projection \(I\to I_i\) is onto.

For an \(A\)-module sheaf \(M\) on \(B\), finite direct image gives the product of copies of \(M_b\), indexed by \(I_i\). Higher cohomology on those strictly local components vanishes. BA.5, applied after this strict-local base change, now gives
\[
(v_*v^*M)_b
 =\varinjlim_i M_b^{I_i}
 =C_{\mathrm{lc}}(I,M_b),\qquad
(R^qv_*v^*M)_b=0\quad(q>0).
\tag{A.N3}
\]
Here \(M_b\) has its discrete topology, and \(C_{\mathrm{lc}}\) means locally constant functions, not all functions. Indeed a locally constant function on the compact space \(I\) has a finite clopen fibre partition. Cylinder sets form a clopen basis; compactness and a common refinement put that partition at a finite stage. Conversely every function from \(I_i\) pulls back to a locally constant function. Surjectivity of \(I\to I_i\) also detects equality at that stage. These observations identify the displayed colimit and its actual pullback maps.

For degree \(r\), replace \(I\) by \(I^{r+1}\). Choose one \(i_0\in I\), only for this stalk calculation. Insertion of \(i_0\) in the first position preserves locally constant functions. With the alternating deletion differential, it gives
\[
dh+hd=1
\quad\text{on}\quad
M_b\longrightarrow C_{\mathrm{lc}}(I,M_b)
 \longrightarrow C_{\mathrm{lc}}(I^2,M_b)\longrightarrow\cdots.
\tag{A.N4}
\]
The cancellations are those of (A.P2), including the augmentation. This proves exactness of the augmented sheaf complex. It does not require a global choice of \(i_0\), an étale section of \(v\), or division by a cover degree.

For clarity, the functors \(M\mapsto v_{r*}v_r^*M\) are exact: on a stalk they are filtered colimits of finite products of the original stalk, and filtered colimits of modules are exact. Equation (A.N3), with the fibre powers in place of \(T\), also says that the pulled-back coefficient sheaves are acyclic for \(v_{r*}\). A bounded-below representative of \(E\) can therefore be used to compute every \(Rv_{r*}v_r^*E\) with these terms. In bidegree \((r,q)\), use \(d_{\mathrm{Cech}}+(-1)^r d_E\). Each total degree has finitely many terms, since \(r\geq0\) and the internal degree has a common lower bound. The exact augmented rows then prove (A.N1), by the finite filtration in each total degree. No assertion about unbounded totalizations is being made.

Integral surjections and their fibre powers remain integral and surjective after base change. Repeating the same ring and stalk argument on the new base proves the final assertion. All maps are the augmentation, pullback and restriction maps, so the comparisons are compatible with those base changes. \(\square\)

The distinction between locally constant and arbitrary functions is essential. For example, on \(I=\{0,1\}^{\mathbf N}\), the indicator of the all-zero sequence is not locally constant at that sequence: every cylinder neighbourhood also contains a sequence with a later nonzero coordinate. It is not represented by a function on any finite stage. Replacing \(C_{\mathrm{lc}}(I,M_b)\) by an unrestricted infinite product would change the descent calculation.

**The normalization really may be infinite.** For \(R=\mathbf C[[t]]\), its integral closure in a separable algebraic closure of \(\mathbf C((t))\) contains all the roots \(t^{1/n}\). The elements \(1,t^{1/n},\ldots,t^{(n-1)/n}\) are linearly independent over \(\mathbf C((t))\): in a nonzero linear combination their nonzero summands have distinct valuations modulo \(\mathbf Z\), so the term of least valuation cannot cancel. The extension degrees are therefore unbounded. A finite \(R\)-module would have finite-dimensional generic fibre, which is impossible. This strictly local example rules out silently replacing the normalization cover by a finite one. Lemma A.1d uses the genuine integral cover.

**Lemma A.1e (the selected normalized local tube).** Let \(B\) be strictly local and let \(b\) be the spectrum of its separably closed residue field. Choose a point \(\eta\in B\), and give its closure the reduced integral structure \(Z\). Choose a separable algebraic closure \(K\) of \(k(\eta)\), put \(t=\operatorname{Spec}K\), and let \(N\) be the normalization of \(Z\) in \(K\). Then \(N\to Z\) is integral and surjective, \(N\) is strictly local, and its closed residue extension over \(b\) is purely inseparable. If \(a:W\to B\) is a qcqs map, \(w\) lies over \(b\), and \(E\in D^+(W_{\mathrm{\acute et}},a^*A)\), write \(W_0=W_{(w)}\). There are canonical identifications
\[
R\Gamma(W_0\times_BN,E)=E_w,
\qquad
R\Gamma(W_0\times_Bb,E)=E_w.
\tag{A.N5}
\]
If \(a\) is locally acyclic relative to \(E\) at \(w\), restriction further gives an isomorphism
\[
R\Gamma(W_0\times_BN,E)
 \longrightarrow R\Gamma(W_0\times_Bt,E).
\tag{A.N6}
\]
Under (A.N5), this is exactly the local-acyclicity map from the stalk \(E_w\).

**Proof.** Write \(Z=\operatorname{Spec}R\). A quotient of a henselian local ring is henselian: a finite algebra over the quotient is also a finite algebra over the original ring and has the same local-factor decomposition. The residue field is unchanged. Thus \(R\) is a strictly henselian local domain. Its integral closure \(D\) in \(K\) is the union of finite \(R\)-subalgebras \(D_i\), each a domain. By the finite-algebra decomposition in AX.5 each \(D_i\) is local: a nontrivial product decomposition would give a nontrivial idempotent in a domain. Each local factor is henselian, and its residue field is finite purely inseparable over the separably closed residue field of \(R\). The inclusions are local maps. Their union is local, its residue field is the union of these purely inseparable extensions, and it is henselian: a monic polynomial and a selected simple residue root are finite data at a stage, where the root lifts. Its residue field is separably closed. Therefore \(D\) is strictly henselian.

Lying over proves surjectivity of \(N\to Z\). Its fraction field is \(K\): for any element of the algebraic extension \(K/k(\eta)\), multiply by a common nonzero denominator for the coefficients of a monic equation. The resulting element is integral over \(R\), so the original element belongs to \(\operatorname{Frac}D\). This use of an algebraic geometric generic field is explicit; an arbitrary transcendental geometric extension is not being identified with a finite or integral field extension.

Now let \(C\) be the ring of \(W_0\times_BN\), integral over the strict local ring of \(W_0\). Its closed fibre is nonempty and has exactly one geometric point with purely inseparable residue extension: the same is true of the closed fibre of \(N\to B\), and remains so after the residue-field extension at \(w\). This fibre statement includes any nilpotents; it does not assert that the tensor product is a field. Every finite subalgebra \(C_i\subset C\) is a finite algebra over the strict local ring. Since \(C\) is integral over \(C_i\), lying over shows that its closed fibre surjects onto the closed fibre of \(C_i\). Thus \(C_i\) has only one local factor and is strictly henselian, as in AX.5. The directed union argument from the preceding paragraph proves that \(C\) is strictly henselian as well.

The scheme \(W_0\times_Bb\) is a quotient of the strictly local scheme \(W_0\), because \(b\) is the selected residue-field point of \(B\). It is nonempty and strictly local, with the selected stalk unchanged. AT.1 identifies derived sections on these strictly local schemes with their actual closed stalks. Pullback identifies those stalks with \(E_w\), giving (A.N5). These identifications commute with restriction because they are induced by the stalk maps, not chosen isomorphisms of groups.

The composite from \(E_w=R\Gamma(W_0,E)\) through the first group in (A.N5) to \(R\Gamma(W_0\times_Bt,E)\) is the ordinary restriction to the selected geometric local fibre. It is an isomorphism by local acyclicity at \(w\), and the first arrow is already an isomorphism by the same closed-stalk calculation. This proves (A.N6). In particular the closed-centre cospecialization is the specified composite
\[
R\Gamma(W_0\times_Bt,E)
 \xrightarrow{\ (A.N6)^{-1}\ }
R\Gamma(W_0\times_BN,E)
 \longrightarrow R\Gamma(W_0\times_Bb,E),
\tag{A.N7}
\]
inverse to the local-acyclicity restriction from \(E_w\). \(\square\)

**How the sheafwise criterion is completed below.** Lemma A.1d supplies integral descent, Lemma A.1e the selected closed-centre calculation, and Lemmas A.1f–A.1i the other target stalks over \(B\) and transitive comparison maps. Theorem A.1l supplies the normalization/cone reduction, so Corollary A.1m proves (FB). Lemma A.1n separately supplies the actual rational coefficient comparison. The GOS formula has its own proof in the conductor subsection below.

#### All-stalk comparisons and composable cospecializations

We supply the map compatibility required by [Illusie's appendix, §§2.2–2.6](https://publications.ias.edu/sites/default/files/Number32.pdf). The normalization criterion of §1.1 is a separate step, proved after these map calculations in Theorem A.1l. Throughout this subsection a geometric point is the spectrum of an **algebraic closure of the residue field of its image**. Replacing a separable algebraic closure by its purely inseparable algebraic closure leaves the étale site unchanged, by Constructible complexes, BE.4. A transcendental enlargement is not included in that assertion. All coefficients below are ordinary étale complexes in \(D^+\); no adic or rational coefficient passage is implicit.

**Lemma A.1f (branches of an integral normalization).** Let \(B=\operatorname{Spec}R\) be strictly local, let \(t\to B\) be one of the selected geometric points, and let \(N=\operatorname{Spec}A\) be the normalization of the reduced closure of its image in \(K=k(t)\). For a strict localization \(P=\mathcal O^{\mathrm{sh}}_{B,y}\), put
\[
D=A\otimes_R P,\qquad T=K\otimes_R P,
\qquad J=\operatorname{Spec}T.
\tag{A.C1}
\]
Let \(I\) be the profinite set of closed geometric lifts in the integral scheme \(\operatorname{Spec}D\to\operatorname{Spec}P\), formed from its finite subalgebras as in (A.N3). Specializing a generic branch to its closed point gives a canonical homeomorphism \(J\simeq I\). Empty fibres are allowed.

**Proof.** The ring \(A\) is a domain with fraction field \(K\). To check the latter assertion, clear denominators in a monic equation for an element of \(K\) over the fraction field of \(R/\ker(R\to K)\): a suitable nonzero scalar multiple is integral. Every monic polynomial over \(A\) splits into linear factors in \(A\), since its roots in the algebraically closed field \(K\) are integral over \(A\), hence over the image of \(R\). Consequently every prime quotient \(A/\mathfrak p\) has the same splitting property. Such a quotient is integrally closed: a fraction satisfying a monic equation must equal one of that equation's roots in the quotient. Its fraction field is algebraically closed, by clearing denominators and rescaling the variable in an arbitrary polynomial. Localizations have these properties as well.

By BA.2, every affine étale scheme over \(A\) is a finite disjoint union of opens, and every \(A_{\mathfrak p}\) is strictly henselian. Here the residue fields are algebraically closed by the preceding splitting argument. The algebra \(D\) is ind-étale over \(A\), because \(P\) is the filtered colimit of the coordinate algebras of the pointed affine étale neighborhoods defining the strict localization of \(R\). If \(\mathfrak q\subset D\) lies over \(\mathfrak p\subset A\), localize each such neighborhood at its selected point. The corresponding open branch has local ring \(A_{\mathfrak p}\). The transition maps are the identity on this ring. Taking their filtered colimit proves
\[
D_{\mathfrak q}\simeq A_{\mathfrak p}.
\tag{A.C2}
\]
In particular these local rings are domains with fraction field \(K\). The map \(A\to D\) is flat. A minimal prime of \(D\) therefore contracts to the zero prime of \(A\): the going-down property for a flat map lifts the zero prime below any selected contraction. It follows also from (A.C2) that every prime of \(D\) contains a unique minimal prime. Each minimal-prime quotient has fraction field \(K\): it contains \(A\), embeds in the corresponding local ring, and that local ring has fraction field \(K\).

The algebra \(D\) is integral over \(P\). For a minimal prime \(\mathfrak a\), the domain \(D/\mathfrak a\) is a filtered union of finite domain algebras over the strictly local quotient \(P/\ker(P\to D/\mathfrak a)\). Each finite algebra is local, since a finite algebra over a henselian local ring is a product of local rings and a domain has no nontrivial product decomposition. These finite local subalgebras have compatible maximal ideals. Their union is local: any element outside the union of their maximal ideals is already a unit at a finite stage. Thus each minimal prime of \(D\) has a unique closed specialization. Conversely every closed point has a unique minimal prime by (A.C2). Minimal primes and closed points are in bijection.

Inverting the nonzero elements of \(A\) identifies \(T\) with the localization of \(D\) at those elements. Its primes are exactly these minimal primes, by (A.C2). Also \(T\) is a filtered colimit of finite products of \(K\), because it is ind-étale over the algebraically closed field \(K\). Hence \(J\) is compact, Hausdorff and zero-dimensional, and every local ring on \(J\) is \(K\). At each finite integral stage of \(D/P\), its local factors give orthogonal idempotents. Their pullbacks partition \(J\) into clopen sets. These partitions show that the branch-to-closed-lift bijection is continuous into the inverse limit \(I\). A continuous bijection from compact \(J\) to Hausdorff \(I\) is a homeomorphism. This includes the empty case. \(\square\)

**Lemma A.1g (the canonical comparison on all stalks).** Suppose \(f:X\to S\) is qcqs and locally acyclic relative to \(E\in D^+(X_{\mathrm{\acute et}})\). For a selected specialization \(u:t\to S_{(s)}\), let \(N\) be the normalization of the reduced closure of \(t\) in \(k(t)\), and write \(g_N:X_N\to X\) and \(g_t:X_t\to X\). The restriction map is a quasi-isomorphism
\[
Rg_{N*}E_N\longrightarrow Rg_{t*}E_t.
\tag{A.C3}
\]
Consequently the actual restriction \(\rho_u:R\Gamma(X_N,E_N)\to R\Gamma(X_t,E_t)\) is an isomorphism.

**Proof.** First work over \(B=S_{(s)}\). Local acyclicity is unchanged by this pointed ind-étale base change: the selected strict localizations and the corresponding local geometric fibres agree, as in AT.1. Proving the comparison on \(X_B\), then applying the derived direct image to \(X\), proves the stated version. This use of a strict localization does not assume local acyclicity after an arbitrary base change.

Take any geometric point \(x\) of \(X_B\), with image \(y\), and put \(W=(X_B)_{(x)}\) and \(P=\mathcal O^{\mathrm{sh}}_{B,y}\). If \(y\) is outside the closure being normalized, both stalks are zero. Otherwise apply Lemma A.1f. BA.5, including formula (BA.9) computes the two stalks as
\[
R\Gamma(W\times_P\operatorname{Spec}D,E),
\qquad
R\Gamma(W\times_P J,E).
\tag{A.C4}
\]
Write \(E_x\) for the actual stalk complex, not for the restriction of \(E\) to \(W\). The integral calculation (A.N3), on the strictly local scheme \(W\), identifies the first complex with \(C_{\mathrm{lc}}(I,E_x)\). The closed-lift set remains \(I\): at each finite stage, extending the separably closed residue field of \(P\) to that of \(W\) neither splits nor merges its purely inseparable closed residue extensions. This identification is induced by the section counit on each finite local component, and then by filtered colimit.

For the second complex, project \(\pi:W\times_P J\to J\). At \(j\in J\), the strict local scheme of \(J\) is \(\operatorname{Spec}K\). Applying (BA.9) to \(\pi\) therefore gives
\[
(R\pi_*E)_j
 =R\Gamma(W\times_P\operatorname{Spec}K,E).
\tag{A.C5}
\]
The equality uses the map to \(P\) specified by the branch \(j\). Local acyclicity at \(x\) says that the canonical map from \(E_x\) to (A.C5) is an isomorphism. On all of \(J\) these maps come from one map \(\underline{E_x}\to R\pi_*E\): identify \(E_x\) with \(R\Gamma(W,E)\) by AT.1 and use the section counit before restricting to \(W\times_P J\). Thus that map is an isomorphism on every stalk, not a collection of unrelated group isomorphisms.

The étale site of \(J\) has its clopen opens as a basis. Indeed an affine étale algebra of finite presentation descends to a finite product of \(K\)'s, where its branches are copies of \(K\); pulling back gives clopen branches. Global sections of abelian sheaves on \(J\) are exact: local lifts of a section under an epimorphism admit a finite cover by clopen sets, which can be refined to a finite disjoint clopen partition, and the lifts then glue. Hence, for bounded-below complexes,
\[
R\Gamma(W\times_P J,E)
 \simeq C_{\mathrm{lc}}(J,E_x).
\tag{A.C6}
\]
The coefficient complex may be represented by any bounded-below complex; the constant-sheaf functor and these global sections are exact. The comparison from the first complex of (A.C4) to the second is the pullback of locally constant functions along \(J\to I\). To see that it is the actual map, restrict the section counit to each finite idempotent component: its value at a generic branch is precisely its value at that branch's closed specialization. The resulting square commutes before taking colimits and derived sections. Lemma A.1f makes this pullback an isomorphism. This proves (A.C3) at every \(x\). Applying \(R\Gamma\) proves the last assertion. \(\square\)

The use of locally constant functions matters. A normalization can have infinitely many branches after localizing at an intermediate point. An arbitrary infinite product of copies of \(E_x\), or just the single closed-centre comparison (A.N7), is not the stalk computation above.

**Proposition A.1h (composition of cospecializations).** Under the hypotheses of Lemma A.1g define
\[
\operatorname{cosp}(u)=\sigma_u\rho_u^{-1}:
R\Gamma(X_t,E_t)\longrightarrow R\Gamma(X_s,E_s),
\tag{A.C7}
\]
where \(\sigma_u\) is restriction from \(X_N\) to its closed geometric fibre. For composable selected specializations \(r\xrightarrow{v}t\xrightarrow{u}s\), these maps satisfy
\[
\operatorname{cosp}(u)\operatorname{cosp}(v)
 =\operatorname{cosp}(uv).
\tag{A.C8}
\]

**Proof.** Work over \(S_{(s)}\), and let \(A\) be its normalization along \(r\) in \(k(r)\). The chosen factorization through \(t\) selects a prime \(\mathfrak p\subset A\). More explicitly, base change to \(S_{(t)}\); the chosen generic branch in (A.C1) has a unique closed specialization by Lemma A.1f, and its contraction to \(A\) is \(\mathfrak p\). Its component is local, and (A.C2) identifies it with \(A_{\mathfrak p}\). The residue-field identification with the chosen \(k(t)\) is part of this selected branch: both are the algebraic closure extending the prescribed separable residue closure, with a unique purely inseparable completion.

These rings describe all three normalizations:
\[
N(r/s)=\operatorname{Spec}A,\quad
N(r/t)=\operatorname{Spec}A_{\mathfrak p},\quad
N(t/s)=\operatorname{Spec}(A/\mathfrak p).
\tag{A.C9}
\]
For the second equality, the selected component of the integral base change is integral over the image of \(\mathcal O^{\mathrm{sh}}_{S,t}\), has fraction field \(k(r)\), and is normal by (A.C2). It is therefore its integral closure: any element integral over the smaller image is integral over this normal ring and belongs to it. For the third equality, \(A/\mathfrak p\) is integral over the reduced closure of \(t\), is normal by the monic splitting argument in Lemma A.1f, and has fraction field \(k(t)\). The same argument identifies it with the required normalization. Thus no unsupported commutation of normalization with an arbitrary quotient is being used. It is the algebraically closed generic field that gives the additional quotient property here.

Abbreviate \(H_V=R\Gamma(X_V,E_V)\). Let \(\alpha:H_A\to H_{A_{\mathfrak p}}\) and \(\beta:H_A\to H_{A/\mathfrak p}\) be restriction. The three maps to generic fibres
\[
\rho_A:H_A\xrightarrow{\sim}H_r,\quad
\rho_p:H_{A_{\mathfrak p}}\xrightarrow{\sim}H_r,\quad
\rho_q:H_{A/\mathfrak p}\xrightarrow{\sim}H_t
\tag{A.C10}
\]
are isomorphisms by Lemma A.1g applied to the original locally acyclic morphism and the respective specializations. We have not assumed that the arbitrary base-changed morphism over \(A\) is locally acyclic. If \(\tau:H_{A_{\mathfrak p}}\to H_t\) and \(\sigma_q:H_{A/\mathfrak p}\to H_s\) are restriction, functoriality of pullback gives
\[
\rho_p\alpha=\rho_A,\qquad
\tau\alpha=\rho_q\beta,\qquad
\sigma_A=\sigma_q\beta.
\tag{A.C11}
\]
In particular \(\alpha\) is invertible. Substitution in the composite yields
\[
\sigma_q\rho_q^{-1}\tau\rho_p^{-1}
 =\sigma_q\rho_q^{-1}\tau\alpha\rho_A^{-1}
 =\sigma_q\beta\rho_A^{-1}
 =\sigma_A\rho_A^{-1},
\tag{A.C12}
\]
which is (A.C8). All identifications used the selected branches. Their uniqueness and restriction functoriality also show that isomorphic choices of these normalization models give the same map. \(\square\)

**Corollary A.1i (the strict-local normalization tests).** Let \(f\) be locally acyclic relative to \(E\), and let \(f_{(x)}:X_{(x)}\to S_{(s)}\) be its selected strict-local restriction. Every cospecialization of the selected algebraic geometric points for this restriction is an isomorphism. For every associated normalization \(N\), restriction from \(X_{(x)}\times_{S_{(s)}}N\) to its closed geometric fibre is an isomorphism.

**Proof.** The selected strict-local restriction remains locally acyclic by the same ind-étale local-fibre identification used in Lemma A.1g. At the closed centre, Lemma A.1e identifies the cospecialization with the inverse of the local-acyclicity map from the actual stalk \(E_x\). Its calculation also applies to the algebraic closures used here: adjoining the purely inseparable completion of the separable generic closure gives an integral universal homeomorphism between the normalizations. Indeed each new integral element has a suitable characteristic-power in the old integral closure. The corresponding étale sites and actual restriction maps agree by the purely inseparable invariance input of BE.4. The cospecialization is therefore an isomorphism for every selected specialization to the centre. Given a specialization between two other geometric points of \(S_{(s)}\), compose it with the canonical specialization to the closed centre. Such a specialization is fixed by the pointed strictly local structure: each pointed étale neighborhood of the centre has its unique section. Proposition A.1h identifies the composite of cospecializations with the cospecialization to the centre. Two-out-of-three now makes the original cospecialization invertible. Finally \(\sigma_u=\operatorname{cosp}(u)\rho_u\), and both factors are invertible by the preceding argument and Lemma A.1g. \(\square\)

**From tests to finite base change.** Corollary A.1i supplies the normalization tests; Theorem A.1l proves their sufficiency without a Noetherian or finite-component assumption; and Corollary A.1m discharges **FB**. Lemma A.1n handles rational coefficients through an integral model and its actual local-fibre arrow. No arbitrary transcendental cohomology invariance is inferred from algebraic geometric-point tests. The full conductor formula (A.14) is supplied separately in the conductor subsection below.

#### The normalization criterion over an arbitrary base

The preceding cospecialization proofs give normalization tests. We now prove their sufficiency, including the arbitrary-base reduction in [Illusie's appendix, Proposition 1.1](https://publications.ias.edu/sites/default/files/Number32.pdf), and discharge **FB** in Proposition A.1c. The proof does not replace an arbitrary scheme by finitely many irreducible components. Instead we construct one integral cover whose individual components are normalization tests, and use its entire Čech nerve. Throughout this subsection schemes and morphisms are qcqs, coefficients are ordinary sheaves of abelian groups or left modules over the pulled-back sheaf of rings, and complexes are bounded below. No commutativity, Noetherianity, finiteness or torsion assumption on that coefficient ring is needed for the criterion.

**Lemma A.1j (integral direct image).** For an integral morphism \(v:T\to B\), direct image on abelian étale sheaves is exact and commutes with arbitrary change of base. These are the canonical comparison maps. The same assertions hold for pulled-back ring-module categories and for their bounded-below derived categories.

**Proof.** We first describe an integral scheme over a strictly local affine base \(\operatorname{Spec}R\). Write its algebra \(D\) as the filtered union of its finite \(R\)-subalgebras \(D_i\). By AX.5, each finite scheme is a finite disjoint union of strictly local schemes. Their finite closed-point sets \(I_i\) form an inverse system; put \(I=\varprojlim I_i\). This is a profinite space, possibly empty. The associated idempotents define a continuous map from \(T\) to \(I\). Its fibre at a closed point \(z\) is the local scheme \(T_z=\operatorname{Spec}D_z\), and
\[
T_z=\varprojlim_{U\ni z}T_U,
\tag{A.B1}
\]
where \(U\) runs over clopen neighborhoods in \(I\) and \(T_U\) is the corresponding open-and-closed part of \(T\).

Here are the algebraic details of this assertion. A compatible choice of finite local factors of the \(D_i\)'s has a local filtered colimit. An element outside its maximal ideal is already a unit in a selected finite local factor. Thus this colimit is exactly \(D_z\). Each selected finite factor is obtained by an idempotent localization, which gives (A.B1). The resulting local ring is strictly henselian: any monic equation with a simple residue root descends to one finite local stage, where the root lifts, and its residue field is the filtered union of separably closed algebraic extensions of the separably closed residue field of \(R\). Finite polynomial data show this union is separably closed. In particular \(T_z\) is strictly local. These arguments also show that the closed points of \(T\), with their finite-stage clopen neighborhoods, are precisely \(I\).

For any abelian étale sheaf \(F\) on \(T\), the assignment \(U\mapsto\Gamma(T_U,F)\) is a sheaf \(\mathcal G_F\) on the clopen basis of \(I\). Coverings of a clopen compact set have finite refinements, so the usual sheaf gluing suffices. By the section continuity in BA.5, its stalk is
\[
(\mathcal G_F)_z=\Gamma(T_z,F)=F_z.
\tag{A.B2}
\]
The last equality is the actual closed-stalk map on a strictly local scheme, as in AT.1. Hence \(F\mapsto\mathcal G_F\) is exact, by stalks. Global sections on a profinite space are exact: a section under an epimorphism lifts on a finite clopen cover, and refining to a disjoint clopen partition glues those lifts. It follows that \(\Gamma(T,-)=\Gamma(I,\mathcal G_{(-)})\) is exact.

Let \(s\) be an algebraic geometric closed point of \(\operatorname{Spec}R\). The reduced geometric fibre \((T_s)_{\mathrm{red}}\) is an inverse limit of finite disjoint copies of \(s\); its étale site is the site of the same clopen space \(I\). Finite presentation descends every étale object to a finite stage, proving this description. Nilpotents do not change the site: for a nil ideal every finite list of elements lies in a nilpotent finitely generated subideal, and the unique étale lifts across nilpotent thickenings pass to the limit. The same argument for purely inseparable algebraic extensions is the stalk-unit calculation of BE.4. Restriction from \(T\) to \(T_s\) induces the identity on the stalks (A.B2), and therefore
\[
R\Gamma(T,F)=\Gamma(T,F)
 \xrightarrow{\sim}\Gamma(T_s,F|_{T_s}).
\tag{A.B3}
\]
This is an assertion about sections of the given sheaf, not an assertion that all sheaves on \(T\) are constant.

For general \(B\), the higher-direct-image stalk formula (BA.9) applies after strict localization of \(B\). The exactness just proved makes \(R^qv_*F=0\) for \(q>0\), and (A.B3) identifies the degree-zero stalk with sections on the geometric fibre. An integral scheme over a separably closed field has algebraic residue fields; extending that field to any larger separably closed field leaves its finite-stage sets of geometric points and their clopen partitions unchanged. The fibre étale sites, and the pulled-back sheaf sections on them, are therefore canonically identified. Compute the two sides of any base-change map at a geometric point using that same field. The identifications (A.B3) make the map the identity on these sections. This proves arbitrary base change. Forgetting module structure detects exactness, and the maps are linear over the appropriate pulled-back rings. Applying these exact functors to bounded-below complexes gives the derived assertion. \(\square\)

**Lemma A.1k (a cover with normalization components).** Let \(R\) be strictly local and let \(R'\) be an integral \(R\)-algebra. There is an integral surjection \(N\to\operatorname{Spec}R'\) such that every connected component of \(N\) is a strictly local normal domain scheme whose fraction field is an algebraic closure of a residue field of \(R\). Each component is an inverse limit of clopen neighborhoods in \(N\), and is the normalization in that field of the corresponding reduced point closure in \(\operatorname{Spec}R\).

**Proof.** For each prime \(\mathfrak p\subset R'\), choose an algebraic closure \(K_{\mathfrak p}\) of \(\kappa(\mathfrak p)\). Map \(R'\) to the product of these fields, and let \(D\) be the elements of the product integral over its image:
\[
R'\longrightarrow \prod_{\mathfrak p\in\operatorname{Spec}R'}K_{\mathfrak p},
\qquad
D=\{a:\ a\text{ is integral over the image of }R'\}.
\tag{A.B4}
\]
The kernel of the first map is the nilradical. Thus \(D\) contains a copy of \((R')_{\mathrm{red}}\), is integral over it, and lying over makes \(\operatorname{Spec}D\to\operatorname{Spec}R'\) surjective. Set \(N=\operatorname{Spec}D\). The product itself is not claimed integral; only its integral elements are used. The ring \(D\) is reduced.

Every monic polynomial over \(D\) splits in \(D\). Choose roots in every coordinate field, label them within each coordinate, and assemble each labeled root into an element of the product. It is integral over \(D\), and hence over \(R'\), so belongs to \(D\). Also every idempotent of the product belongs to \(D\). In particular, if \(e_a\) is the characteristic function of the coordinates where \(a\in D\) vanishes, then
\[
\operatorname{Ann}_D(a)=e_aD.
\tag{A.B5}
\]
Indeed this equality holds coordinatewise, and \(e_a\in D\). Each local ring of \(D\) is a domain: if \(ab=0\), then \(b=e_ab\), and in a local ring the idempotent \(e_a\) is zero or one; in the first case \(b=0\), in the second \(a=0\). Thus every prime contains a unique minimal prime.

Let \(\mathfrak a\) be a minimal prime of \(D\). The domain \(D/\mathfrak a\) inherits monic splitting. As in Lemma A.1f, it is normal and has algebraically closed fraction field. It is integral over the image \(R/\mathfrak q\) of \(R\), so that fraction field is algebraic over \(\operatorname{Frac}(R/\mathfrak q)=\kappa(\mathfrak q)\). The ring is the full integral closure of \(R/\mathfrak q\) in this field: any further element integral over \(R/\mathfrak q\) is integral over the normal ring \(D/\mathfrak a\), and hence belongs to it. It is local, because its finite domain subalgebras over the henselian quotient \(R/\mathfrak q\) are local and have compatible maximal ideals. It is strictly henselian by the same finite-stage argument as in Lemma A.1e; alternatively all its local rings are strictly henselian by BA.2. Thus its spectrum is connected and has a unique closed point.

We check the claimed clopen limit, rather than presuming that infinitely many components are open. If \(a\in\mathfrak a\), it vanishes in the field \(D_{\mathfrak a}\). There is a \(c\notin\mathfrak a\) with \(ca=0\). By (A.B5), \(c=e_ac\), so \(e_a\notin\mathfrak a\) and \(1-e_a\in\mathfrak a\). Since \(a=(1-e_a)a\), the ideal \(\mathfrak a\) is generated by its idempotents. Consequently
\[
\operatorname{Spec}(D/\mathfrak a)
 =\varprojlim_{\substack{e^2=e\in D\\ e\notin\mathfrak a}}\operatorname{Spec}D_e.
\tag{A.B6}
\]
At its unique closed point these are exactly a cofinal family of clopen neighborhoods: idempotents have the same zero/one values at the generic and closed points of a domain. Lemma A.1j identifies the closed-point space of \(N\) as profinite. Since each prime of \(D\) contains a unique minimal prime, and the corresponding quotient is local, these connected domains are exactly its components. No finite-component assertion has been used. \(\square\)

**Theorem A.1l (normalization criterion).** Let \(f:X\to Y\) be a morphism over \(S\), and let \(E\in D^+(X)\). The following conditions are equivalent.

1. Formation of \(Rf_*E\) commutes with every finite change of the base \(S\).
2. It commutes with every quasi-finite change of \(S\) and with affine-transition inverse limits of such changes.
3. For every specialization of algebraic geometric points \(t\to S_{(s)}\), let \(N\) normalize the reduced closure of \(t\) in \(k(t)\). For \(f_N:X_N\to Y_N\), restriction to its closed geometric fibre induces an isomorphism
\[
i^*Rf_{N*}E_N\longrightarrow Rf_{s*}E_s.
\tag{A.B7}
\]
Here the closed geometric fibre is formed with its actual selected field; purely inseparable algebraic changes are identified by their canonical étale equivalences.

**Proof of the easy implications.** Condition 2 contains condition 1. Conversely, AW.5 factors a separated quasi-finite change locally as an open immersion into a finite change. The finite comparison followed by restriction gives its canonical comparison. A general quasi-finite change is covered by such separated affine pieces, so these local comparisons suffice. BA.5 passes to affine-transition limits on affine étale test objects and their qcqs inverse images. Bounded-below truncation justifies the corresponding derived comparison in each degree. This proves 1 implies 2.

Both \(N\to S\) and its closed algebraic geometric point \(s\to S\) are affine-transition limits of quasi-finite changes, locally on \(S\). For the normalization, first express the strict localization as pointed affine étale neighborhoods. Its integral algebra is a filtered colimit of finite, finitely presented algebras by BA.6's monic-generator-and-relation construction. Each such finite presentation descends to one pointed neighborhood; the composite is quasi-finite over \(S\). The algebraic geometric point is obtained by a closed quotient, localization and algebraic field extensions, using the same finite-presentation approximation. The composition identity for canonical base-change maps then deduces (A.B7) from the comparisons for these two maps. Thus 2 implies 3.

**Proof that the tests suffice.** Fix a strict localization \(\operatorname{Spec}R=S_{(s)}\). We will prove simultaneously for every strictly local integral \(R\)-algebra \(R'\) that the comparison to its closed geometric fibre is an isomorphism. Its residue field is an algebraic purely inseparable extension of that of \(R\), so compatible algebraic geometric closed fields can be identified. Write \(C(R')\) for the cone of that comparison, an object on the corresponding \(Y_s\). If \(E\in D^{\geq m}\), then
\[
C(R')\in D^{\geq m-1}
\quad\text{for every }R'.
\tag{A.B8}
\]
This common lower bound is independent of the algebra and of any Čech degree.

Choose the integral cover \(N=\operatorname{Spec}D\to\operatorname{Spec}R'\) of Lemma A.1k, and let \(N_r\) be its \((r+1)\)-fold fibre power over \(R'\). Let \(Z_r=N_r\times_{R'}s\). On \(Y_{Z_r}\) denote by \(C_r\) the cone comparing \(Rf_{N_r*}E_{N_r}\) with its direct image on this closed fibre. We claim that \(C_0\) is acyclic. At a geometric point of \(Y_{Z_0}\), the image in \(N\) is a closed point. By (A.B6), its component is the inverse limit of clopen neighborhoods and is one of the normalization schemes in condition 3. Restricting direct images to a clopen piece is exact, and BA.5 identifies their stalks at the component limit. Equivalently, the selected strict local scheme of \(Y_N\) sends every idempotent to its value at that point, so factors through precisely this component. The closed fibres are identified by the nilpotent and purely inseparable equivalences used in Lemma A.1j. Thus the stalk of \(C_0\) is the stalk of the comparison (A.B7) for that component. Hypothesis 3 makes it zero. This proves the claim on every target stalk.

Suppose inductively that \(\mathcal H^qC(R'')=0\) for \(q\leq d\), for every strictly local integral \(R\)-algebra \(R''\). Each \(N_r\) is integral over \(R\). At any closed point \(z\) over \(s\), its local ring is again a strictly local integral \(R\)-algebra: the proof of (A.B1) expresses it as the filtered colimit of the finite local factors over \(R\), each of which is finite and integral over \(R\). It is an inverse limit of clopen neighborhoods in \(N_r\). The same stalk and continuity argument identifies the stalks of \(C_r\) there with those for this strictly local algebra. The induction hypothesis therefore gives \(\mathcal H^qC_r=0\) for \(q\leq d\) at every geometric point of \(Y_{Z_r}\).

Lemma A.1d supplies cohomological descent along the integral surjection \(N\to\operatorname{Spec}R'\), both for \(X_{R'}\) and for its closed fibre. Apply \(Rf_*\) to the first resolution. Lemma A.1j commutes the integral direct images with restriction to the closed fibre. Taking the cone gives a first-quadrant-in-the-horizontal-direction double complex with columns
\[
v_{r,s*}C_r,\qquad
v_{r,s}:Y_{Z_r}\longrightarrow Y_s.
\tag{A.B9}
\]
Its total complex represents \(C(R')\). These identifications use the actual descent augmentations, restrictions and adjunction maps; they are not an abstract choice of a cone with the same cohomology groups. Integral direct image is exact by Lemma A.1j, so the column cohomology is \(v_{r,s*}\mathcal H^qC_r\).

Column zero is acyclic in all degrees. In every other column a term contributing to total degree \(n\leq d+1\) has vertical degree \(n-r\leq d\), so vanishes by the induction hypothesis. The uniform lower bound (A.B8) makes every total-degree filtration finite. Explicitly the column spectral sequence is
\[
E_1^{r,q}=v_{r,s*}\mathcal H^qC_r
\ \Longrightarrow\ \mathcal H^{r+q}C(R').
\tag{A.B10}
\]
It proves vanishing through degree \(d+1\), simultaneously for all \(R'\). Start at \(d=m-2\), where (A.B8) supplies the hypothesis, and iterate. Each fixed cohomological degree is reached after finitely many steps. Thus every \(C(R')\) is acyclic.

To finish, take any finite change \(S'\to S\) and any geometric point of \(Y_{S'}\). Strict-localize \(S\) at its image and select the finite local factor \(R'\) of \(S'\times_S\operatorname{Spec}R\) containing its lift. This factor is strictly local, even when its algebra is neither reduced nor a domain, by AX.5. Pointed ind-étale base change preserves the direct-image stalks by BA.5. The comparisons just proved for \(R\) and \(R'\) identify both sides of the original finite-base-change arrow at that geometric point with the same direct image on the closed geometric fibre. The canonical composition identity makes the induced arrow the identity. It is therefore an isomorphism on every target stalk, proving condition 1. This reduction never required finitely many irreducible components. \(\square\)

Algebraic geometric points suffice for the criterion: they form a conservative family of points of each étale topos. In the final stalk test, one may also use the same larger separably closed field for a point and its composite; Lemma A.1j accounts for the integral-fibre identifications. The proof does not claim that arbitrary cohomology over a field is invariant under a transcendental extension. That stronger assertion is neither used nor needed to obtain finite base change.

**Corollary A.1m (the ordinary strict-local input).** If \(a:W\to B\) is locally acyclic relative to \(E\in D^+(W)\), then, for every geometric \(w\) with image \(b\), formation of
\[
Ra_{w*}(E|_{W_{(w)}}),\qquad
a_w:W_{(w)}\longrightarrow B_{(b)},
\tag{A.B11}
\]
commutes with every finite change of base of \(B_{(b)}\). This is **FB**, at the full ordinary bounded-below scope.

**Proof.** Corollary A.1i verifies the normalization tests for this strict-local morphism. A normalization base is strictly local, so its closed direct-image stalk is its actual derived global sections, by AT.1. Hence those tests are precisely condition 3 of Theorem A.1l, not merely equality of geometric-fibre dimensions. The theorem proves (A.B11). \(\square\)

Substituting Corollary A.1m into Proposition A.1c removes its extra hypothesis **FB**. The ordinary postcomposition assertion in **PC** is therefore proved for its stated invertible-torsion ring coefficients; applying it after each permitted base change gives the stated universal version. The larger geometric fields in that assertion are handled by the purely inseparable and smooth-limit argument following (A.P7), not by declaring a transcendental extension quasi-finite. This closes the ordinary normalization/postcomposition dependency. The next subsection supplies the rational-coefficient bridge at every algebraically closed ground field. The full conductor identity (A.14) is proved separately below.

#### Rational coefficients and the cover-independent open

The coefficient comparison needed by Lemma A.1 is already available at a broader geometric scope than Corollary E.2n.1 states. Constructible complexes, BV starts with finite-type schemes over a field, not only a finite field. BW and BX retain that scope. We now apply their exact coefficient maps to local acyclicity. This is a use of those earlier proofs, not an extension of a finite-field assertion by analogy. No Frobenius or weight argument enters.

Fix a finite extension \(E/\mathbb Q_\ell\), with valuation ring \(O\), uniformizer \(\pi\), and finite residue field \(\kappa\). On a scheme \(Z\) write
\[
A_Z=\underline O,\qquad R_Z=\widehat O_Z,
\qquad E_Z=R_Z[1/\pi].
\tag{A.R1}
\]
These are different sheaves of rings. In particular a geometric inverse image uses the map \(h^{-1}R_Z\to R_{Z'}\); it does not identify the two rings without a comparison. Rational constructible complexes mean the bounded constructible subcategory of the ambient pro-étale derived category used in BX. For the usual \(\overline{\mathbb Q}_\ell\)-coefficient convention, take the filtered scalar-extension category over the finite extensions \(E\). A fixed object and its finite diagram are represented at one such field by the definition of that category. This is not a claim about arbitrary sheaves over a completed infinite coefficient field.

**Lemma A.1n (rationalizing the local-fibre comparison).** Let \(X\) and \(S\) be separated finite-type schemes over a field of characteristic different from \(\ell\), and let \(f:X\to S\). Let \(M\) be a bounded constructible \(E_X\)-complex. There is a bounded constructible complete \(R_X\)-complex \(P\), with classical first derived reduction \(P_1\), such that
\[
P[1/\pi]\simeq M,
\qquad P\otimes_{R_X}^{L}\kappa\simeq\nu_X^*P_1.
\tag{A.R2}
\]
If \(f\) is universally locally acyclic for \(P_1\), it is universally locally acyclic for \(M\), with its actual rational local-fibre maps. The same implication holds on any specified base open.

**Proof: choose the model at the stated field scope.** BX.6–BX.7 supplies (A.R2). Its construction first obtains lattices on étale neighbourhoods, replaces these by finite étale covers on a finite stratification, and descends the sum of their finitely many translates. It then lifts extension classes and the finite cohomological tower. The resulting model is constructible, not a presumed globally lisse lattice. BW.2–BW.3 identifies its underlying complete constant-\(O\) complex by an adjunction whose unit and counit induce the identity on the actual derived reductions. These constructions require neither a finite ground field nor descent of \(X\) to one. They also do not require realization from the bounded derived category of the constructible heart.

We need the model after arbitrary base changes and strict localizations, where finite type over the original field may be lost. Here is the specific extension of scope. BO.6 and BX.3 give a finite algebraic stratification of \(X\), with pro-étale local bounded finite free \(O\)-complexes on its strata. Pull back that finite filtration and those covers along any \(h:Z\to X\). On each pulled stratum the actual ringed pullback is the same finite complex over \(R_Z\), so is complete and has the same finite amplitude. The open–closed support formulas in BX.2–BX.3 identify its gluing with ordinary ringed pullback. Their neighbourhood construction works over arbitrary rings; the closed pieces here remain finitely presented after base change. Both extension by zero and closed-support image preserve completeness by the product-cone argument there. Finite devissage therefore proves
\[
Lh_R^*P\simeq C_{R_Z}Lh_R^*P,
\qquad Lh_R^*P\in D^{[a,b]}
\tag{A.R3}
\]
for some interval fixed by the finite stratum models, independently of \(h\). Reduction is the pulled-back classical derived reduction. Only these inherited models are asserted on \(Z\); a new equivalence of all constructible categories on every non-Noetherian scheme is unnecessary.

**Proof: retain the particular arrow.** Make any base change \(T\to S\), choose a geometric point \(x\) of \(X_T\) with image \(s\), and a geometric point \(t\to T_{(s)}\). Put
\[
V=(X_T)_{(x)}\times_{T_{(s)}}t.
\tag{A.R4}
\]
This is the selected local geometric fibre, not the whole base-changed neighbourhood with every lift. It is qcqs: strict localizations are affine, and a morphism between affine schemes is affine. Write \(L=(X_T)_{(x)}\). There is an actual restriction map \(R\Gamma(L,P_L)\to R\Gamma(x,Lx_R^*P)\). Both objects are complete by (A.R3) and the section argument below. Its first reduction is the closed-stalk map for the classical first reduction on a strictly local scheme, which is an isomorphism by AT.1 and BK.2. First-reduction detection therefore makes this restriction an isomorphism. Use its inverse followed by restriction from \(L\) to \(V\) to define the local-fibre comparison
\[
\alpha_P:P_x\longrightarrow R\Gamma(V,P_V),
\quad
P_x=R\Gamma(x,Lx_R^*P),\quad P_V=Lv_R^*P,
\tag{A.R5}
\]
where pullback from the original \(X\) is understood in both terms and \(v:V\to X\) is the composite map. All complexes in this display can be regarded as constant-\(O\) module complexes after restriction of coefficients. The geometric point is a weakly contractible pro-étale object, so its derived sections are its actual coefficient complex. By (A.R3), both pulled-back models are complete. Derived sections preserve completeness: they preserve the products and cones defining completion and commute with the finite free two-term complexes \([O\xrightarrow{\pi^n}O]\), as in BK.3–BK.6.

Those same two-term complexes, and the étale/pro-étale comparison of BK.2, identify the first reduction of \(\alpha_P\) with the ordinary local-fibre map for \(P_1\). This identifies the map, not just its domain and codomain: coefficient extension, restriction and the adjunction unit commute, and BW.5 preserves those units. Let \(Q=\operatorname{Cone}(\alpha_P)\). Universal local acyclicity of \(P_1\) gives
\[
Q\otimes_O^L\kappa=0,\qquad
Q\simeq\operatorname{holim}_n(Q\otimes_O^LO/\pi^n)
\quad\Longrightarrow\quad Q=0.
\tag{A.R6}
\]
Indeed the first equality makes multiplication by \(\pi\) invertible on \(Q\), hence all higher coefficient cones zero; the displayed complete reconstruction then gives zero. This is derived first-reduction detection, not reduction of a rational object.

Finally BX.4 commutes derived sections on a qcqs scheme with uniformly bounded-below filtered colimits. The multiplication-by-\(\pi\) tower of \(P_V\) has the common bound (A.R3), so its localization gives the natural isomorphisms
\[
\begin{aligned}
P_x[1/\pi]&\simeq M_x,\\
R\Gamma(V,P_V)[1/\pi]&\simeq
R\Gamma(V,P_V[1/\pi])=R\Gamma(V,M_V).
\end{aligned}
\tag{A.R7}
\]
Here \(P_V[1/\pi]\simeq M_V\) is the ordinary ringed pullback comparison (BX.21), with its coefficient map retained. Thus the localization of the particular arrow (A.R5) is precisely the rational local-fibre comparison \(\alpha_M\). Exact localization takes the zero cone in (A.R6) to zero. This proves the lemma for every \(T,x,t\), including geometric fields larger than algebraic closures of residue fields. We have used the qcqs continuity proof for the inherited bounded models, not an unsupported assertion about arbitrary field-extension cohomology. \(\square\)

**Corollary A.1o (the common open at rational scope).** Let \(k\) be any algebraically closed field with \(\ell\ne\operatorname{char}k\), let \(S\) be an integral finite-type \(k\)-scheme, and let \(f:X\to S\) be of finite type. For a bounded constructible rational complex \(M\) on \(X\), a nonempty open \(U\subset S\) makes \(f_U\) universally locally acyclic for \(M|_{X_U}\). That same \(U\) works after every étale change of source and every change of base.

**Proof.** First shrink to a nonempty affine open of \(S\). Cover its inverse image by finitely many affine schemes. On each choose the model (A.R2). The ordinary generic argument in the preceding subsection, Lemma A.1b and its monic-coordinate induction, applies to its one bounded constructible first reduction over the finite field \(\kappa\). Its ground field is \(k\), not \(\kappa\). The extra input PC in that argument is now supplied by Proposition A.1c and Corollary A.1m; proper constructibility is the exact ordinary theorem E.2m. Hence it supplies one nonempty open for each first reduction. Their finite intersection is nonempty because \(S\) is integral. Lemma A.1n upgrades these comparisons to the rational ones. Local acyclicity is local on the source, since selected strict localizations agree on an open neighbourhood of the point. Thus the affine results give the stated assertion without requiring the original \(X\) to be separated. Universality already includes all base changes. For an étale change of source the selected strict localization and the local comparison map are unchanged, as in AT.4. No new shrinking is involved. \(\square\)

Apply this to the fixed complex of Lemma A.1 and the projection \(Y\times C_1\to C_1\), where \(Y=\prod_{a>1}C_a\). Choose a global integral model on this proper product and choose \(U\) from its first reduction as above. For every finite étale \(\widetilde Y\to Y\), use its pullback model \(P'\) and put \(g:\widetilde Y\times U\to U\). The same first reduction remains ULA. Proper comparison and the specialization argument following (A.U2) make the finitely many cohomology sheaves of \(Rg_*P'_1\) locally constant on this already chosen \(U\). The finite-module argument there applies to the finite \(\kappa\)-stalks. The complex \(Rg_*P'\) is complete, and its first reduction is that ordinary proper image; its boundedness is the coefficient-triangle and repleteness argument of E.2n. BO.6 therefore gives its local finite-complex description on \(U\). BW–BX then identify
\[
(Rg_*P')[1/\pi]\simeq Rg_*(M|_{\widetilde Y\times U}).
\tag{A.R8}
\]
On the local finite-complex models, cohomology after localization is a finite-dimensional constant \(E\)-space. Consequently all these direct-image cohomology sheaves are lisse on the same \(U\). Their amplitudes and ranks may depend on the cover; the open does not. Removing an additional point, if needed, gives the proper open \(V\subsetneq C_1\) used in the curve calculation, still independently of the cover. Its complement is finite. Pulling back along a cover of \(C_1\) preserves the same comparisons.

For \(\overline{\mathbb Q}_\ell\) in the stated scalar-extension convention, choose the finite coefficient field for the fixed input once. Extending coefficients is exact and faithful, and the local comparison is the scalar extension of the one just proved. The common open is therefore still chosen once, before the covers. This proves the generic rational local-acyclicity and common-open input of Lemma A.1 relative to the exact earlier providers. The full Swan-conductor identity (A.14) is proved in the next subsection. The other nearby-cycle and perverse prerequisites remain additional hypotheses.

#### The full curve conductor formula

We prove (A.14), including wild ramification and lisse sheaves with infinite monodromy. Let \(V\) be a smooth connected curve over an algebraically closed field \(k\), let \(X\) be its smooth proper compactification, and put \(B=X-V\). Fix \(\ell\ne\operatorname{char}k\). Rational coefficients mean a finite extension \(E/\mathbb Q_\ell\), or the scalar-extension convention for \(\overline{\mathbb Q}_\ell\) stated above. The calculation is geometric; no finite-field descent or weight theorem is used.

**Ramification conventions and the residue-field issue.** At a boundary point the completed fraction field is \(k((x))\). For a finite Galois extension with valuation ring \(k[[t]]\), write \(I\) for its group and normalize \(v_t(t)=1\). All residue extensions are trivial. For \(\sigma\ne1\), put
\[
i(\sigma)=v_t(\sigma t-t),\qquad
I_j=\{\sigma:i(\sigma)\ge j+1\},\qquad i(1)=+\infty.
\tag{A.G1}
\]
This is independent of the parameter: every integral element is a power series in \(t\), so its motion has value at least the motion of \(t\); apply the same argument to a second parameter. We use \(I_s=I_{\lceil s\rceil}\) for \(s>0\). Define
\[
\phi(v)=\int_0^v\frac{|I_s|}{|I|}\,ds,
\qquad I^u=I_{\phi^{-1}(u)}.
\tag{A.G2}
\]
Positive lower groups are \(p\)-groups in characteristic \(p>0\). Indeed the first linear coefficient gives an injection \(I/I_1\hookrightarrow k^\times\), and the next nonzero coefficient injects \(I_j/I_{j+1}\) into the additive group of \(k\) for \(j\ge1\). The filtration terminates since the group is finite. In characteristic zero all these positive groups are trivial: the additive group has no nontrivial finite subgroup. Thus positive-group invariants are exact over either characteristic-zero coefficients or a field of characteristic \(\ell\).

The hypotheses here are not those of a finite-residue local field. Here is the required justification for using the quotient argument in Herbrand's function, §§2–4. The integral closure of \(A=k[[x]]\) in a finite separable extension is finite over \(A\). Indeed choose an integral field basis \(b_1,\ldots,b_e\) by scaling a basis with powers of \(x\). Every integral element belongs to the trace-dual lattice of \(\sum A b_i\), because the traces of its products with the integral \(b_i\) are integral and belong to the integrally closed ring \(A\). Nondegeneracy of the separable trace pairing makes this dual lattice finite free. Its submodule, the integral closure, is therefore finite over the Noetherian ring \(A\). Completeness gives the Hensel property by successive Newton lifting, so that finite integral domain is local; its normal one-dimensional local ring is a DVR. Its residue field is \(k\), and it is complete. It is consequently \(k[[t]]\): successive removal of residue coefficients gives a unique power-series expansion. If the ramification index is \(e\), the elements \(1,t,\ldots,t^{e-1}\) form an integral basis. Linear independence follows from their distinct valuation classes modulo \(e\); spanning follows by successive removal of the term of smallest valuation, completeness, and collection of the coefficients in \(k[[x]]\). Equivalently, the finite free rank is \(\dim_k k[[t]]/(x)=e\), and these elements are a basis by the same successive approximation. This proves degree equals ramification index and applies to every intermediate valuation ring. The degree of the preliminary field basis need not be known to equal the ramification index until this argument has established it.

For clarity, the decisive quotient identity can now be proved at this scope. Let \(H\triangleleft I\), let \(t'\) be a parameter of the fixed field, and let \(f(T)\in k[[t']][T]\) be the monic minimal polynomial of \(t\). For a lift \(\sigma\) of a nonidentity \(s\in I/H\), the elements \(st'-t'\) and \((\sigma f)(t)\) generate the same ideal in \(k[[t]]\). One divisibility follows by expressing every coefficient of \(f\) in the integral basis generated by \(t'\) over \(k[[x]]\). For the other, express \(t'=P(t)\), divide \(P(T)-t'\) by the monic \(f\), and apply \(\sigma\) to the resulting factorization before evaluating at \(t\). Taking valuations gives
\[
i_{I/H}(s)=\frac1{|H|}\sum_{\sigma\mapsto s}i_I(\sigma).
\tag{A.G3}
\]
Choose a lift in that coset with maximal motion \(m\). The ultrametric inequality, with equality at unequal values, gives \(i_I(\sigma h)=\min(m,i_H(h))\). Since
\(\phi_H(v)=|H|^{-1}\sum_h\min(i_H(h),v+1)-1\), (A.G3) gives \(i_{I/H}(s)-1=\phi_H(m-1)\). Hence the image of \(I_v\) is \((I/H)_{\phi_H(v)}\). Counting kernels shows that the derivatives of \(\phi_I\) and \(\phi_{I/H}\circ\phi_H\) agree; both vanish at argument zero. Their equality proves that upper groups commute with quotients. The finite-group inverse-limit argument in §4 of the same provider therefore defines the absolute upper groups and surjects onto every finite upper group also for \(k((x))\). No Hasse–Arf or local class-field theorem is required.

For a representation \(M\), define its Swan conductor by positive upper groups:
\[
\operatorname{Sw}(M)=\int_{0}^{\infty}
  \operatorname{codim}M^{I^u}\,du
 =\sum_{j\ge1}\frac{|I_j|}{|I|}\operatorname{codim}M^{I_j}
\tag{A.G4}
\]
when its wild action is computed in the displayed finite quotient. Quotient compatibility proves independence of that quotient. The lower sum uses the interval \(j-1<s\le j\); endpoints have measure zero. This is the wild conductor only. The Artin conductor additionally contains \(\operatorname{rank}M-\dim M^I\). That extra tame term must not be inserted in (A.14).

**Finite monodromy in characteristic zero.** First suppose a finite connected Galois étale cover \(W\to V\), with group \(G\), trivializes \(L\). Normalize \(X\) in its function field to obtain a smooth proper curve \(Y\); a normal curve over the perfect field \(k\) is smooth. For \(y\in Y-W\), its stabilizer \(I_y\) is also its inertia group, of order the ramification index \(e_y\). For \(\sigma\in I_y-\{1\}\), use the motion \(i_y(\sigma)\) of (A.G1).

We first compute the identity character, retaining the different. The parameter \(t\) above has Eisenstein minimal polynomial \(F(T,x)\) over \(k[[x]]\). Its constant coefficient has \(x\)-order one, and its other nonleading coefficients are divisible by \(x\). Consequently \(F_x(t,x)\) is a unit. Differentiating \(F(t,x)=0\) in continuous differentials gives that \(dx/dt\) and \(F_T(t,x)\) generate the same ideal. The latter derivative is the product of \(t-\sigma t\) over nonidentity local automorphisms. Therefore the order of the canonical differential comparison is
\[
d_y=v_t(dx/dt)=\sum_{\sigma\in I_y-\{1\}}i_y(\sigma).
\tag{A.G5}
\]
The comparison is nonzero by separability. The injection of canonical line bundles has this zero divisor. Taking degrees and using the proved [canonical degree \(2g-2\)](../AG-LTF/cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves.html#2-3-curve-riemann-roch-ample-twisting-and-smooth-divisors) gives the wild Riemann–Hurwitz equality. The curve cohomology ranks in The multiplicative group on a curve, Theorem 6.2 identify the constant étale Euler characteristic with \(2-2g\). Subtracting the finite boundary, and using \(\sum_{y\mid x}e_y=|G|\), gives
\[
\chi_c(W,E)=|G|\chi_c(V,E)
 -\sum_{y\in Y-W}\sum_{\sigma\in I_y-\{1\}}
       (i_y(\sigma)-1).
\tag{A.G6}
\]

For a nonidentity \(g\in G\), every fixed point is in \(Y-W\), since the action on \(W\) is free. The weighted graph–diagonal formula, Theorem 4.1 gives its alternating trace on proper cohomology as the sum of the local lengths \(i_y(g)\). The boundary has one degree-zero basis vector at each point and no higher cohomology. The equivariant localization triangle therefore gives
\[
\operatorname{Tr}(g;R\Gamma_c(W,E))
 =\sum_{\substack{y\in Y-W\\gy=y}}(i_y(g)-1).
\tag{A.G7}
\]
In particular, absence of fixed points on the open curve does **not** make this trace zero in the wildly ramified case. The proper formula and the boundary subtraction must both be retained. Inverting the automorphism does not change any motion number, so (A.G7) is compatible with either pullback convention for a left group action.

Let \(M\) be the representation defining the associated sheaf, of dimension \(r\). Finite étale descent identifies its compactly supported cohomology with the diagonal \(G\)-invariants of \(R\Gamma_c(W,E)\otimes_E M\), after the corresponding inverse convention is fixed. This follows already on the trivializing cover and its Čech nerve; averaging kills positive group cohomology in characteristic zero. Averaging the alternating trace, substituting (A.G6)–(A.G7), and grouping conjugate boundary points yields
\[
\begin{aligned}
\chi_c(V,L)&=r\chi_c(V,E)\\
 &\quad-\sum_{x\in B}\frac1{|I_y|}
   \sum_{\sigma\in I_y-\{1\}}(i_y(\sigma)-1)
          \bigl(r-\operatorname{Tr}(\sigma;M)\bigr),
 \qquad y\mid x.
\end{aligned}
\tag{A.G8}
\]
If the descent convention produces \(\sigma^{-1}\) in the trace, reindex the inner sum by inversion. For each \(j\ge1\), averaging over \(I_{y,j}\) projects onto its invariants. Each \(\sigma\ne1\) occurs in exactly \(i_y(\sigma)-1\) such groups. The inner sum divided by \(|I_y|\) is consequently
\[
\sum_{j\ge1}\frac{|I_{y,j}|}{|I_y|}
     \bigl(r-\dim M^{I_{y,j}}\bigr)
 =\operatorname{Sw}_x(L).
\tag{A.G9}
\]
This proves the full wild formula for finite-monodromy rational sheaves, without assuming that \(|G|\) is prime to \(\ell\).

**Coefficient comparison, without a global finite-monodromy assumption.** Let \(O\) be the valuation ring of \(E\), with uniformizer \(\pi\) and residue field \(\kappa\). A continuous representation of the profinite group \(\pi_1(V)\) on \(E^r\) has a stable finite free \(O\)-lattice. Its compact image sends \(O^r\) into a fixed \(\pi^{-N}O^r\); the sum of these translates is a finitely generated torsion-free module between the two lattices, and is stable under the group and its inverses. Let \(P\) be the corresponding complete lisse integral sheaf and let \(\bar P=P/\pi\).

We need an actual Euler comparison, not equality of separate ranks conjectured from reduction. The complete coefficient and support arguments BK.2–BK.6, BX.2–BX.4, and the ordinary constructible finiteness proof E.2m apply on the proper curve \(X\). They give a complete complex \(C=R\Gamma(X,j_!P)\), its actual first derived reduction \(R\Gamma_c(V,\bar P)\), and its rationalization \(R\Gamma_c(V,P[1/\pi])\). Here \(j:V\hookrightarrow X\). The localization is taken after the integral model, using bounded-below continuity; the rational sheaf itself is never reduced modulo \(\pi\).

Here is why this complex is perfect over \(O\). Its first reduction has finite-dimensional cohomology in a bounded interval \([a,b]\). Successive coefficient triangles make every \(C\otimes_O^L O/\pi^n\) bounded in that same interval with finite-length cohomology. These groups are finite sets, since \(\kappa\) is finite, so each inverse system satisfies the Mittag–Leffler condition. Completeness and the inverse-limit exact sequence put \(C\) itself in \([a,b]\). Lift a basis of the top cohomology of its first reduction to \(H^b(C)\); surjectivity of that lift follows from the coefficient triangle and \(H^{b+1}(C)=0\). Map a finite free module in degree \(b\) to \(C\). The reduction of its cone has top degree at most \(b-1\). Repeat, always using the finite-reduction bound and completeness to justify the next lift. After degree \(a\), the remaining cone has zero first reduction and is complete, hence is zero. This expresses \(C\) as a finite iterated cone of finite free modules. Thus
\[
\chi_c(V,P[1/\pi])
 =\sum_q(-1)^q\operatorname{rank}_O C^q
 =\chi_c(V,\bar P).
\tag{A.G10}
\]
This statement concerns an alternating sum. Individual integral cohomology groups may have torsion, which cancels in that sum; they need not all be free.

Wild inertia is pro-\(p\), whereas the kernel of \(\mathrm{GL}_r(O)\to\mathrm{GL}_r(\kappa)\) is pro-\(\ell\): successive congruence quotients are additive groups in characteristic \(\ell\). A closed subgroup that is both pro-\(p\) and pro-\(\ell\) is trivial, since every finite quotient has both prime-power orders. The image of wild inertia therefore injects into the finite reduction group, and is a finite \(p\)-group. Its averaging idempotent is integral over \(O\). For every positive upper group, this idempotent commutes with reduction and scalar extension and has a finite free image. Consequently
\[
\dim_E(P[1/\pi])^{I_x^u}
 =\dim_\kappa\bar P^{I_x^u}\quad(u>0),
\qquad \operatorname{Sw}_x(P[1/\pi])=
       \operatorname{Sw}_x(\bar P).
\tag{A.G11}
\]
The positive upper action factors through a finite quotient; quotient compatibility proved above identifies its normalization with (A.G4). There are only finitely many nonzero intervals. In characteristic zero both sides of the conductor assertion are zero. No assertion about reduction of tame inertia invariants is made or needed.

**Why the finite-coefficient case follows from the finite-monodromy case.** A finite \(\kappa\)-local system has a finite monodromy group \(G\). We give the representation argument needed when \(\ell\) divides \(|G|\); an arbitrary modular representation is not presumed to lift. After a finite extension of \(\kappa\), the simple \(\kappa[G]\)-modules split and \(\kappa\) contains all roots of unity of prime-to-\(\ell\) order dividing \(|G|\). Such a finite extension suffices because over the algebraic closure there are finitely many simple modules, each given by finitely many matrices; those entries and the finitely many required roots all lie in one finite field. In particular every character of the cyclic subgroups used below is defined over this field. Cohomology and invariant dimensions are unchanged by this finite scalar extension.

Let \(S_1,\ldots,S_d\) be these simple modules. Their ordinary traces in characteristic \(\ell\) are linearly independent as functions on \(G\). To see this without a semisimplicity assumption on \(\kappa[G]\), choose a basis \(v_{i,1},\ldots,v_{i,n_i}\) in each simple module. The image of
\[
\kappa[G]\longrightarrow\bigoplus_i S_i^{n_i},
\qquad a\longmapsto(a v_{i,j})_{i,j}
\tag{A.G12}
\]
is the whole target. Otherwise its semisimple quotient would have a nonzero map onto one of the \(S_i\). Schur's lemma makes the composite a scalar linear combination of the projections onto the copies of that \(S_i\). Vanishing on (A.G12), evaluated at \(a=1\), contradicts linear independence of its chosen basis. Here the quotient is semisimple because it is generated by the finitely many images of the simple summands: add these one at a time, retaining a summand exactly when its intersection with the preceding sum is zero; otherwise simplicity makes it already contained. A nonzero map between simples is an isomorphism by its kernel and image. Endomorphisms of an absolutely simple module are scalar by taking an eigenvalue over the algebraic closure and using the kernel of the difference; the matrix entries then put that scalar back in the splitting field. Surjectivity in (A.G12) allows a group-algebra element with any prescribed matrices on the simples. In particular its trace can be one on one simple and zero on all others, proving the stated independence.

Write each \(g\in G\) as a product of its commuting \(\ell\)-regular and \(\ell\)-power parts. The latter acts unipotently in characteristic \(\ell\), and preserves each eigenspace of the former. Hence the trace of \(g\) equals the trace of its \(\ell\)-regular part. The trace functions remain independent on the \(\ell\)-regular conjugacy classes. Lift the prime-to-\(\ell\) eigenvalues multiplicatively to roots of unity in an unramified characteristic-zero coefficient extension. The resulting Brauer characters \(b_i\) are independent in characteristic zero too: an independence minor of their reductions has nonzero determinant, so its lifted determinant is a unit. These characters are additive on short exact sequences, since at a prime-to-\(\ell\) element the eigenvalue multisets are additive.

The restrictions of the characters
\[
\operatorname{Ind}_H^G\theta,
\qquad H\subset G\text{ cyclic of order prime to }\ell,
\quad\theta:H\to\kappa^\times,
\tag{A.G13}
\]
span all characteristic-zero class functions on the \(\ell\)-regular classes. Indeed extend an orthogonal class function by zero on the other classes. The ordinary induction sum and finite character pairing reduce its pairing with (A.G13) to its Fourier pairing on \(H\). Vanishing for every character of a cyclic \(H\) forces its restriction to \(H\) to be zero, by the invertible finite Fourier matrix. Every \(\ell\)-regular element belongs to such a subgroup, so the original function is zero. Each character in (A.G13) is the Brauer character of the reduction of an actual characteristic-zero representation: lift \(\theta\) to its root-of-unity character and induce its free integral lattice. At an \(\ell\)-regular element its eigenvalues reduce bijectively, so ordinary and Brauer characters agree there.

Every such reduction is an integral combination of the \([S_i]\) in the Grothendieck group. The preceding span and independence statements show that the matrix of these composition multiplicities has rank \(d\). Since its entries are integers, its rank is already \(d\) over \(\mathbb Q\). Thus the classes of the reductions in (A.G13) span \(G_0(\kappa[G])\otimes\mathbb Q\). This is rational spanning, not an assertion of an integral lift for every modular module, and it does not average \(G\)-invariants in characteristic \(\ell\).

For the fixed cover trivializing a modular local system, consider the additive defect
\[
D(M)=\chi_c(V,\mathcal L_M)
 -\dim_\kappa M\,\chi_c(V,\kappa)
 +\sum_{x\in B}\operatorname{Sw}_x(\mathcal L_M).
\tag{A.G14}
\]
Euler characteristic is additive by the finite cohomology long exact sequence. Each positive ramification group is a \(p\)-group, so its averaging idempotent makes its invariants exact in characteristic \(\ell\); hence the Swan term is additive as well. Thus \(D\) is a homomorphism on the Grothendieck group. It vanishes on every reduction in (A.G13): the lifted local system has finite monodromy, so (A.G8)–(A.G9) applies, while (A.G10)–(A.G11) identifies its Euler and Swan quantities with those of the reduction. Rational spanning forces \(D(M)=0\) for every \(M\). The defect takes rational values, so no torsion is lost by this argument. This proves (A.14) for all finite-field local systems.

Finally take the stable lattice in an arbitrary lisse rational \(L\). Its first reduction is one of the finite local systems just treated. Equations (A.G10)–(A.G11), including (A.G10) for the constant lattice, transport that identity to \(L\). A finite scalar extension does not change any dimension in these identities. The same proof therefore applies to the usual \(\overline{\mathbb Q}_\ell\) scalar-extension category. Disconnected smooth curves are handled componentwise. We have proved (A.14) at its full stated lisse rational scope, with the wild Swan term, relative to the explicitly linked earlier cohomology and algebraic-curve foundations. The general perverse and nearby-cycle statements require further arguments in addition to this conductor formula.

**Normalization checks.** A tame but nontrivial rank-one local system still has Swan conductor zero, not Artin conductor zero. For a cyclic wild group of order \(p\) with lower break \(m\), a nontrivial character has Swan conductor \(m\): the positive groups are the whole group for \(1\le j\le m\), and trivial afterwards. Its regular representation has conductor \(m(p-1)\). The different is \((m+1)(p-1)\), so the boundary term in (A.G6) is exactly \(m(p-1)\), agreeing with the conductor of that regular representation. These checks retain the distinction between the different exponent, the Swan conductor and the full Artin conductor.

Let \(j:V\hookrightarrow C_1\). For each connected covered curve, \(H^0(C_1',j_!L_q)=0\): a section vanishing near the nonempty boundary is zero on the connected lisse locus. Curve duality bounds \(H^2\) by \(\operatorname{rank}L_q\). Formula (A.14) gives \(H^1=-\chi_c+H^2\). An unramified proper degree-\(D\) cover multiplies this Euler characteristic by \(D\): it multiplies the Euler characteristic of the open curve, and its fibres repeat each identical Swan conductor \(D\) times. For \(q\ge0\), the degree-one term is consequently \(O(D^{n-q-1})\); the degree-two term is \(O(D^{n-q-2})\). Their total cohomological degrees are respectively \(q+1\) and \(q+2\). These are exactly (A.15). The all-degree estimate follows from the corresponding rank and conductor bounds. The Leray spectral sequence has only curve degrees one and two and a fixed finite range of \(q\), so subquotients and its finite abutment filtration preserve the estimates.

Finally, proper duality identifies \(H^r(\widetilde C,K)^\vee\) with \(H^{-r}(\widetilde C,DK)\); Verdier duality exchanges the two perverse halves over our field coefficients. This proves the negative-degree assertion. A general bounded complex has finitely many upper-perverse shifts, so the all-degree bound follows too. \(\square\)

**Corollary A.2 (local covers).** For a perverse sheaf \(P\) near a point \(x\), there is an affine étale neighbourhood \(V\) and finite étale covers \(V_D\to V\) of degrees proportional to \(D^n\), tending to infinity, such that
\[
\dim H^{-1}(V_D,P)=O(D^{n-1}).
\tag{A.18}
\]
The fibre over \(x\) has degree proportional to \(D^n\).

**Proof.** Work affinely, embed into \(\mathbb A^n\), and translate \(x\) to the origin after extending the finite field if necessary. Choose a smooth proper curve of genus at least two with a finite separable map to \(\mathbb P^1\), unramified above zero. Remove the inverse images of its branch values and infinity to obtain an affine étale map \(C'\to\mathbb A^1\) whose image contains zero. Smooth proper curves of positive genus admit connected unramified covers of unbounded degree, for example from cyclic quotients of the prime-to-characteristic Tate module of their Jacobian. Their products, restricted to \((C')^n\), and base changed to our affine space give \(V_D\). For the quasi-finite separated map \(b:V\to C^n\), ordinary \(Rb_*\) preserves the lower perverse half: its left adjoint \(b^*\) preserves the upper half because quasi-finite inverse image does not increase support dimension. Smooth base change along the finite étale covers identifies the pullbacks of \(Rb_*P\) with the corresponding direct images from \(V_D\). Apply the negative-degree assertion of Lemma A.1 to \(Rb_*P\), using \(R\Gamma(C^n,Rb_*P)=R\Gamma(V,P)\). On the zero fibre each covering degree is multiplied in every coordinate, so the total degree is a fixed positive multiple of \(D^n\). Disconnected base changes may be retained: the estimate is for their total cohomology, and their total fibre degree has the asserted value. \(\square\)

### Detecting the lower weight bound on affine tests

**Theorem A.3.** A mixed perverse sheaf \(P_0\) has weights \(\ge w\) if and only if
\[
H^0(V,P)\text{ has weights }\ge w
\tag{A.19}
\]
for every affine étale \(V_0\to X_0\). The test uses Frobenius on the geometric cohomology of \(V_0\). This is Gabber's criterion.

**Proof.** Necessity follows from the lower direct-image estimate: étale inverse image equals exceptional inverse image and preserves the lower bound; ordinary direct image to a point also preserves it. Its degree-zero group has weights \(\ge w\).

The condition passes to étale restrictions and to quotients in the perverse heart. For the latter, affine cohomology of a perverse sheaf has no positive degrees, so \(H^0\) of the original object surjects onto \(H^0\) of its quotient. It also passes to \({}^pH^0Rf_*P\) for affine \(f\). Indeed \(Rf_*P\in{}^pD^{\le0}\); its negative perverse truncation contributes no degree-zero or degree-one cohomology on an affine étale test space. Thus \(H^0\) of \({}^pH^0Rf_*P\) is \(H^0\) of the affine pullback of \(P\). Finite extension of the base field preserves the condition: an affine étale test over the extension is still affine étale over the original field, and Frobenius powers on its geometric components have the same weights.

We first prove sufficiency on a curve. Take a composition series of \(P_0\); the simple terms are pure by the curve discussion above. Let \(r\) be the sum of their generic ranks. On any connected affine étale curve, the degree-minus-one cohomology of every perverse quotient has dimension at most \(r\), because it is the space of sections of its degree-minus-one lisse sheaf on a dense open. The long exact sequences of the composition series then show the following: \(H^0\) of each simple graded term has a quotient whose kernel has dimension at most \(r\), and this quotient is a subquotient of \(H^0\) of the tested \(P\). To see the bound directly, lift its \(H^0\) through the corresponding step of the filtration; the kernel of that step's map to \(H^0(P)\) is an image of \(H^{-1}\) of the remaining quotient.

For a point-supported simple of weight \(b\), choose étale covers with more than \(r\) points over its support. Its pure degree-zero cohomology then has dimension greater than \(r\). The surviving nonzero quotient has weight \(b\) and is a subquotient of a representation with weights \(\ge w\). Hence \(b\ge w\).

For a positive-dimensional simple \(j_{!*}L[1]\) of weight \(b\), first choose a cover of its dense affine curve whose proper compactification has genus at least two. Such covers exist in positive characteristic by Artin–Schreier equations with a pole of arbitrarily large order prime to the characteristic at a boundary point; Riemann–Hurwitz makes the genus tend to infinity. Next take connected unramified covers of that proper curve. Formula (A.14), including the nonnegative boundary conductor terms, gives
\[
\dim H^1(\bar V,j_*L)\ge
\operatorname{rank}(L)(2g(\bar V)-2).
\tag{A.20}
\]
This tends to infinity. Pure-curve continuation and proper purity make this group pure of weight \(b\). It injects into \(H^0(V,j_{!*}L[1])\): the support localization sequence has zero degree-zero term on the removed points because the intermediate extension has no point-supported subobject. Its image therefore survives the loss of at most \(r\) dimensions. Again \(b\ge w\). All simple terms have the lower bound, so extension closure proves it for \(P_0\). This proves the curve case without higher-dimensional intermediate-extension purity.

Now induct on dimension. The question is local, and closed pushforward preserves both the weight bound and the test, so embed an affine neighbourhood into \(\mathbb A^n\). Let \(G_0\subset P_0\) be its maximal subobject with finite support, and let \(Q_0=P_0/G_0\). Finite length gives this subobject; taking the sum of all geometric point-supported subobjects makes it Frobenius stable. On the local covers of Corollary A.2, the kernel of
\[
H^0(V_D,G)\longrightarrow H^0(V_D,P)
\]
has dimension at most \(\dim H^{-1}(V_D,Q)=O(D^{n-1})\). Every nonzero Frobenius weight sector of \(G\) instead has dimension proportional to \(D^n\): étale pullback repeats its point fibre that many times. If it had a weight below \(w\), its entire image in the weight-bounded \(H^0(V_D,P)\) would vanish. That would require a kernel of order \(D^n\), contradicting (A.18). Thus \(G_0\ge w\).

The quotient \(Q_0\) still satisfies the test and has no point-supported subobject. Fix any closed point \(x\). Over a finite extension choose a hyperplane \(i:H\hookrightarrow\mathbb A^n\) through \(x\) containing no positive-dimensional support of a geometric simple constituent of \(Q\). Its affine complement and affine exactness give \(i^!Q\in{}^pD^{[0,1]}\). Its degree-zero part would push forward to a subobject of \(Q\) supported on \(H\); a simple subobject of that object would contradict either the chosen hyperplane or the absence of point-supported subobjects. Therefore
\[
R=i^!Q[1]\in\operatorname{Perv}(H).
\tag{A.21}
\]

We verify the lower-weight test for \(R\) with bound \(w+1\). Choose linear coordinates identifying the ambient space with \(H\times\mathbb A^1\). For an arbitrary affine étale \(V\to H\), use the affine étale ambient space \(V\times\mathbb A^1\to H\times\mathbb A^1\) and pull \(Q\) back to it. Let \(f:V\times\mathbb A^1\to\mathbb A^1\) be projection and put \(A={}^pH^0Rf_*Q\), now with this pulled-back input. This perverse sheaf on a curve satisfies (A.19), so the curve case gives \(A\ge w\). Exceptional restriction gives \(i_0^!A[1]\ge w+1\), where \(i_0\) is the origin. Exceptional base change identifies \(i_0^!Rf_*Q[1]\) with \(R\Gamma(V,R|_V)\). Both \(Rf_*\) and \(i_0^![1]\) are upper t-exact here, so taking degree zero depends only on \({}^pH^0Rf_*Q\). Thus \(H^0(V,R|_V)\) has weights \(\ge w+1\). This verifies the whole test on every such \(V\), and the induction hypothesis gives \(R\ge w+1\).

Taking the exceptional stalk at \(x\), and undoing the shift, gives \(i_x^!Q\ge w\). The chosen point was arbitrary. The closed-point costalk test proves \(Q_0\ge w\). Finally \(0\to G_0\to P_0\to Q_0\to0\) and extension closure give \(P_0\ge w\). \(\square\)

## Appendix B. Constructing the surface pencil

The geometry needed in Appendix A can be obtained by prescribing finitely many Taylor coefficients. This also separates an ordinary node of a surface fibre from a boundary tangency in characteristic two.

### Interpolation at two points

Fix a projective embedding of a smooth surface \(S\) over an algebraically closed field \(k\), and write \(A=\mathcal O_S(1)\). Let \(W_d\) be the restrictions to \(S\) of degree-\(d\) homogeneous polynomials on the ambient projective space.

**Lemma B.1.** If \(d\ge7\) and \(x\ne y\) are geometric points, then
\[
W_d\longrightarrow
(A^d\otimes\mathcal O_S/\mathfrak m_x^4)
\oplus(A^d\otimes\mathcal O_S/\mathfrak m_y^4)
\tag{B.1}
\]
is surjective.

**Proof.** Choose a linear form \(H\) nonzero at both points and a linear form \(B_y\) zero at \(y\) but nonzero at \(x\). In the chart \(H\ne0\), coordinate differences generate the maximal ideal at \(x\). Their monomials of degree at most three span the quotient by its fourth power: successively subtract the constant, linear, quadratic and cubic terms. Thus a homogeneous cubic \(Q\), divided by \(H^3\), gives any requested element of that quotient.

The element \((B_y/H)^4\) is a unit at \(x\). First multiply the requested jet by its inverse in the quotient, then choose the corresponding \(Q\). The section
\[
B_y^4QH^{d-7}
\tag{B.2}
\]
has the requested \(x\)-jet in the trivialization by \(H^d\), and zero \(y\)-jet. Exchange the points and add the two sections. Restriction to a smooth boundary branch gives the same interpolation for branch jets. This proof uses no division by the characteristic. \(\square\)

### General position with a normal-crossing boundary

**Proposition B.2.** Let \(D\) be a reduced normal-crossing divisor on \(S\), and let \(d\ge7\). There exist independent sections \(s_0,s_1\in W_d\) such that their pencil has the following properties. Its base scheme is finite, reduced, transverse and disjoint from \(D\). On the blowup of that base scheme the pencil is a morphism
\[
f:\widetilde S\longrightarrow\mathbb P^1.
\tag{B.3}
\]
Every surface critical point is outside \(D\) and has an ordinary nodal fibre. Every critical point on the normalization of \(D\) is away from its crossings and has contact order two. The normalization maps are generically separable, including in characteristic two. All surface critical points, boundary critical points and crossings have distinct images under \(f\). Consequently each exceptional fibre has exactly one exceptional point, of precisely one of the three types used in (A.10).

If the original data are defined over a finite field, the sections and these properties can be defined over a finite extension of that field.

**Proof.** Put \(n=\dim W_d\) and parameterize ordered pairs by \(P=W_d\oplus W_d\), an irreducible affine space of dimension \(2n\). We exclude bad incidences of dimension at most \(2n-1\). Here we use the elementary dimension facts for finite-type algebraic sets: an incidence whose fibres over an \(r\)-dimensional base have dimension at most \(e\) has dimension at most \(r+e\), and the closure of its image has no larger dimension. These facts and the regular-local-ring Jacobian criterion are the ordinary algebraic-geometric foundations of this argument. The incidence conditions below are polynomial conditions in jets; finite coordinate covers suffice to apply these facts.

At a fixed point of \(S\), a base point imposes \(s_0=s_1=0\), two independent conditions. Dependence of their differentials imposes the additional determinant equation in a freely variable \(2\)-by-\(2\) matrix. Varying the point in dimension two leaves a bad incidence of dimension at most \(2n-1\). Base points on \(D\) impose two conditions with only one point dimension, so their incidence has the same bound. Excluding both images makes the common zero scheme reduced and zero-dimensional; projectivity makes it finite. Locally its equations \(u=s_0,v=s_1\) are étale coordinates after trivializing the line bundle. The two blowup charts have coordinates \((u,v/u)\) and \((u/v,v)\). Their respective pencil coordinates are \(v/u\) and \(u/v\), so the blowup is smooth and \(f\) has no critical point on an exceptional divisor.

Away from the base scheme use the chart \(s_0(x)\ne0\). For a parameter \(t\), set \(h=s_1-ts_0\); the other chart exchanges the sections. At fixed \(x,t\), the conditions
\[
h(x)=0,\qquad dh(x)=0
\tag{B.4}
\]
are three independent equations. The quadratic term remains arbitrary. For a binary quadratic \(a u^2+buv+c v^2\), a repeated tangent factor is given by \(b^2-4ac=0\); in characteristic two its reduced bad locus is \(b=0\). This is one further proper hypersurface. Thus degenerate surface critical points impose four conditions while \(x,t\) vary in three dimensions. Surface critical points lying on \(D\) impose three conditions while \(x,t\) vary in two dimensions. Both bad loci can be excluded.

The remaining surface critical points have invertible Hessian, also in characteristic two, where its off-diagonal entry is \(b\ne0\). The two first derivatives therefore have independent linear terms. The critical locus is reduced and isolated at each of its points, hence finite on the proper surface \(\widetilde S\). Its fibres have two distinct tangent branches; the actual étale nodal equation will be proved below.

Write \(C\) for the finite crossing locus of \(D\). At a smooth boundary point and fixed \(t\), the conditions that \(h\) vanish and its first branch coefficient vanish impose two equations. Vanishing of the second branch coefficient imposes a third. The point and parameter vary in dimension two, so general pairs have no boundary contact of order at least three. At a crossing, the same first two equations on either normalization branch have only the one parameter dimension; exclude them as well. Thus both branch maps at a crossing are smooth.

In characteristic two also prescribe a nonzero cubic coefficient at a boundary critical point. In a branch parameter \(u\), write
\[
s_0=a_0+a_1u+\cdots,\qquad
h=h_2u^2+h_3u^3+\cdots,
\quad a_0h_2\ne0.
\]
The cubic coefficient of \(f-t=h/s_0\) is
\[
\frac{a_0h_3-a_1h_2}{a_0^2}.
\tag{B.5}
\]
Its vanishing is one independent equation in the free coefficient \(h_3\). Together with the boundary criticality equations it again gives three conditions over a two-dimensional point/parameter space. Exclude that image. A remaining characteristic-two boundary germ has
\[
f-f(x)=a u^2+b u^3+O(u^4),\qquad ab\ne0.
\tag{B.6}
\]
Changing the branch parameter rescales the nonzero cubic coefficient: the square term produces no cubic term in characteristic two. Changing the parameter on the pencil line contributes only terms of order at least four, apart from a common nonzero scalar.

For each component of the normalization of \(D\), choose one point away from the crossings and require the branch derivative there to be nonzero. Each requirement is a nonempty open condition by Lemma B.1; there are finitely many components. These conditions ensure generically separable nonconstant maps of proper smooth curves to \(\mathbb P^1\), hence finite maps with finitely many critical points. In characteristic two (B.6) has local degree two and nonzero differential \(bu^2du+\cdots\). Its nearby geometric boundary consists of two points, although its parameter ramification is wild. The purely inseparable equation \(t=u^2\) cannot replace (B.6).

It remains to separate exceptional values. The three strata of possible exceptional points have dimensions \(r=2,1,0\): the interior, smooth boundary and crossing locus. At a fixed point and fixed parameter, the respective conditions impose \(r+1\) equations: value plus two derivatives, value plus one derivative, or just value. For two distinct points of dimensions \(r,r'\) at the same parameter, Lemma B.1 makes their \(r+r'+2\) equations independent. The two points and common parameter vary in dimension \(r+r'+1\). Each of the six possible unordered pairs of strata therefore gives a bad incidence of dimension at most \(2n-1\). Excluding their image closures separates every exceptional value.

Intersect these finitely many nonempty opens with the open of independent section pairs. Irreducibility of \(P\) makes the intersection nonempty. Off the finite exceptional set, the surface fibres are smooth and meet the boundary transversely. At a boundary critical point the surface map is smooth and the contact order is two. At a crossing the fibre is smooth and transverse to both branches. This proves the asserted classification. Over a finite field, the finitely many coefficients of any chosen pair over its algebraic closure belong to a finite extension. A further finite extension can make all exceptional geometric points and values rational when needed. \(\square\)

### The actual étale equation of a node

**Lemma B.3.** At a surface critical point from Proposition B.2, after a separable extension splitting its tangent branches, the map has an étale local equation \(UV=t\), where \(t\) is a parameter at its critical value. This statement concerns the map, not just the completed special fibre.

**Proof.** In the regular local ring of the surface choose actual parameters \(u,v\) along the two tangent factors. Rescaling one gives \(h=f^*t=uv\bmod\mathfrak m^3\). Since \(\mathfrak m=(u,v)\), write the exact identity
\[
h=a u^2+buv+c v^2,
\qquad a,c\in\mathfrak m,\quad b\in1+\mathfrak m.
\tag{B.7}
\]
Adjoin a root \(z\) of \(az^2+bz+c=0\) near \(z=0\) above the given point. The derivative \(2az+b\) is a unit there, so this equation defines an étale neighbourhood after shrinking. On it put
\[
U=u-zv,\qquad V=au+(b+az)v.
\tag{B.8}
\]
Their product is \(au^2+buv-(az^2+bz)v^2=h\). Their linear terms at the point are \(u,v\), so \(U,V\) form étale coordinates by the Jacobian criterion. The asserted equation follows. The two tangent factors are distinct, so they split over a separable residue extension, including in characteristic two. This construction does not choose an arithmetic ordering of the branches: any Galois exchange still acts on their two-element set. The Tate factor and branch character require the separate cohomological calculation in Proposition C.1. \(\square\)

### Removing tame ramification branch by branch

**Lemma B.3a.** Let \(R\) be a discrete valuation ring with uniformizer \(\pi\), fraction field \(K\), and residue field \(k\). Let \(L\) be a finite product of finite separable extensions of \(K\). Write \(T\) for its integral closure over \(R\). Assume that at every maximal ideal \(\mathfrak q\) of \(T\), the ramification index \(e_{\mathfrak q}\) is invertible in \(R\) and \(\kappa(\mathfrak q)/k\) is separable. This is the finite-cover meaning of *tame* used here; separability of the residue extensions is part of the hypothesis. If \(n\) is any invertible common multiple of these indices, put

\[
\begin{gathered}
R_n=R[t]/(t^n-\pi),\\
K_n=\operatorname{Frac}(R_n).
\end{gathered}
\tag{B.8a}
\]

The integral closure \(D_n\) of \(R_n\) in \(L\otimes_K K_n\) is finite étale over \(R_n\). No Galois hypothesis or restriction on the total degree of \(L/K\) is imposed.

**Proof.** Products may be handled one factor at a time, so first let \(L\) be a field. We use the finite normalization proof in Constructible complexes, AP.6: an integral field basis and its inverse trace matrix bound every integral element inside a finite fractional free module. A submodule is finite because the base is Noetherian. This argument applies to every finite separable field factor below. The elementary root-ring calculation at the beginning of AP.7 makes \(R_m=R[z]/(z^m-\pi)\) a DVR for every positive \(m\), with uniformizer \(z\) and residue field \(k\). If \(m\) is invertible, its generic extension is separable. These two statements do not require the later Galois hypothesis of AP.7.

Fix one \(\mathfrak q\), set \(B=T_{\mathfrak q}\), and write \(\pi=u s^e\), where \(s\) is a uniformizer of \(B\), \(u\in B^\times\), and \(e=e_{\mathfrak q}\). Let \(D_e\) be the finite normalization over \(R_e=R[z]/(z^e-\pi)\). The normalization over \(R\), over \(T\), or over \(R_e\) inside the same generic algebra is identical: both larger base rings are integral over \(R\), so integrality in either direction follows from containment and transitivity. Integral closure commutes with localization, by the denominator argument of Constructible complexes, AG.3. Consequently

\[
D_e\otimes_T B=B[v]/(v^e-u),\qquad z=sv.
\tag{B.8b}
\]

Here is a verification of this equality, including normality. The right-hand algebra is finite free over \(B\); its polynomial derivative \(ev^{e-1}\) is a unit, so it is étale. Its generic algebra is \(L\otimes_K K_e\) under the displayed substitution, with inverse \(v=z/s\). At a closed point its residue algebra is a finite separable field extension of \(\kappa(\mathfrak q)\), so its maximal ideal is generated by \(s\); flatness makes \(s\) a nonzerodivisor. The one-dimensional regular local criterion proved in Constructible complexes, L.1 makes this local ring a DVR. Generic local rings are fields. Thus the algebra is normal in its total fraction algebra. An element integral over \(B\) is integral over this algebra and hence belongs to it; conversely all its elements are integral over \(B\). This proves (B.8b), not merely an isomorphism between generic fibres.

At every closed point of \(D_e\) lying over this chosen \(\mathfrak q\), the element \(z=sv\) is a uniformizer and the residue extension over \(k\) is separable. The finite torsion-free module \(D_e\) over the DVR \(R_e\) is free. At such a point its closed fibre is a separable field, with no nilpotents because \(z\) generates the maximal ideal. Differentials of that fibre vanish. Base change for differentials and Nakayama therefore give vanishing of \(\Omega_{D_e/R_e}\) at the point. The finite-flat criterion in AO.3 proves étaleness there. Let \(V_e\subset\operatorname{Spec}D_e\) be the étale locus over \(R_e\). It contains all points over our chosen \(\mathfrak q\); it need not contain the points belonging to other ramification indices.

Now use the actual ring map \(R_e\to R_n\) sending \(z\) to \(t^{n/e}\). The algebra \(C=D_e\otimes_{R_e}R_n\) is finite free over \(R_n\) and injects into its generic algebra \(L\otimes_KK_n\). Its normalization in that algebra is \(D_n\), by integrality of \(C/R_n\). Over the open

\[
V_e\times_{\operatorname{Spec}R_e}\operatorname{Spec}R_n
\tag{B.8c}
\]

the algebra is étale over the DVR \(R_n\). Its local rings are normal by the same uniformizer-and-separable-fibre argument used above. Normalization therefore changes nothing on this open: on each affine localization, an integral element in the total fraction algebra already belongs to that normal ring.

Every closed point of \(D_n\) contracts to a maximal ideal \(\mathfrak q\) of \(T\). Choose its index \(e\). The inclusion \(D_e\hookrightarrow D_n\) is induced by the compatible generic embedding, and its image point lies in \(V_e\). The preceding normal open thus proves that \(D_n/R_n\) is étale at this point. Its generic fibre is already a product of separable fields. These are all points of the finite algebra over a DVR, so \(D_n\) is finite étale everywhere. For a product \(L\), take the product of these normalizations and one common multiple of all indices. The empty cover corresponds to the empty product and is immediate. \(\square\)

In particular, residue degrees need not be prime to the residue characteristic. For example, the unramified extension \(\mathbb F_{p^p}((\pi))/\mathbb F_p((\pi))\) has degree \(p\), index one and separable residue extension; \(n=1\) suffices. Conversely an inseparable residue extension is not made tame merely by an index prime to \(p\). Both distinctions are retained in the lemma.

### Tame covers of a strictly local regular pair

**Proposition B.3b.** Let \(A\) be a Noetherian strictly henselian regular local ring, and let \(f\) be a regular parameter such that \(A/(f)\) is regular. Set \(U=\operatorname{Spec}A[1/f]\). Let \(Y\to U\) be finite étale and tame over the DVR \(A_{(f)}\) in the sense of Lemma B.3a. Suppose the ramification indices are units in \(A\), and choose a common multiple \(n\) which is also a unit in \(A\). Then, for

\[
\begin{gathered}
A'=A[t]/(t^n-f),\\
U'=\operatorname{Spec}A'[1/t],
\end{gathered}
\tag{B.8d}
\]

the pullback \(Y\times_UU'\) extends to a finite étale cover of \(\operatorname{Spec}A'\), and that extension is a disjoint union of copies of \(\operatorname{Spec}A'\). The condition on the indices being units in \(A\) is automatic for the smooth equal-characteristic pairs used in this lesson: choose \(n\) prime to their characteristic. No perfectness assumption on the residue field of \(A_{(f)}\) is made.

**Proof.** The ring \(A'\) is finite free over \(A\). Its closed fibre is \(\kappa(A)[t]/(t^n)\), which has only one prime, so integrality shows that \(A'\) is local. Multiplication by \(f\), and hence by \(t\), is injective. Its quotient by \(t\) is \(A/(f)\). The regular-parameter lifting criterion proved in Constructible complexes, Y.4 therefore makes \(A'\) regular; explicitly, \(t\) together with lifts of a regular system of parameters of \(A/(f)\) generates its maximal ideal with the required dimension. In particular \(A'\) is a domain.

A finite local algebra over a henselian local ring is henselian, by the finite-algebra and idempotent argument in AJ.1. Its residue field here is exactly \(\kappa(A)\), which is separably closed. Thus \(A'\) is strictly henselian. Only this general finite-algebra argument from AJ.1 is used, not its later equalities specialized to a curve with an algebraically closed coefficient field.

The complement of \(U'\) is the regular prime divisor \((t)\). Its only height-one generic point has local ring

\[
A'_{(t)}=A_{(f)}[t]/(t^n-f).
\tag{B.8e}
\]

Indeed the right-hand side is a DVR with maximal ideal \((t)\), by the root-ring calculation; localizing either side in the indicated way gives this ring. Lemma B.3a says that the generic algebra of \(Y\times_UU'\) has finite étale normalization over it. Apply Constructible complexes, AQ.2, whose proof spreads this codimension-one algebra and then uses AP.4–AP.5 across the remaining regular points. This gives a finite étale algebra \(E\) over \(A'\) with the specified restriction on \(U'\). The argument applies also in dimension one, when there is no higher-codimension remainder.

Since the residue field is separably closed, \(E/\mathfrak m_{A'}E\) is a finite product of that field. Henselian idempotent lifting separates the corresponding factors of \(E\). Each factor is a finite projective \(A'\)-module of residue dimension one, hence free of rank one; its unit is a basis by Nakayama. Each factor is therefore \(A'\) as an algebra. This proves the claimed splitting. Restriction is fully faithful by AQ.1, so every specified map and identity on the punctured cover extends uniquely once the covers extend. \(\square\)

**Consequences for coefficients and neighbourhoods.** A finite locally constant sheaf is represented by its finite étale space of elements. Apply Proposition B.3b to that space. If it carries a module structure over a finite ring, extend addition, zero and each scalar map using the full faithfulness just proved; products of extending covers also extend. The module identities hold because they hold on the dense open. Thus the extension is an actual locally constant module, not only a cover with the correct number of points. The same argument extends morphisms and finite systems of compatibilities.

On an equal-characteristic strictly local pair, the root cover \(U'\to U\) is finite étale, connected and a \(\mu_n\)-torsor. Its derivative is invertible after \(t\) is inverted; connectedness follows from the domain \(A'\). Its torsor identity follows by factoring the difference of two \(n\)-th powers, or by the isomorphism sending the ratio of the two invertible roots to the coordinate of \(\mu_n\). Hensel lifting supplies the distinct \(n\)-th roots of unity in \(A\). All finite tame covers are trivialized by these root covers, by the proposition, and the root covers themselves are tame. With compatible geometric lifts as base points, their deck groups therefore give

\[
I^{\mathrm t}\simeq\varprojlim_{(n,p)=1}\mu_n
             =\prod_{\ell\ne p}\mathbb Z_\ell(1)
\tag{B.8f}
\]

in characteristic \(p>0\); in characteristic zero use all positive \(n\). This means the fundamental group of the category of finite covers tame along this divisor. The inverse-limit identification is the cofinal-cover description of that group: a cover split by \(U'\) is its finite fibre with the deck action, and refinement is the map between the corresponding root torsors. It preserves the root-of-unity action and its Tate convention. It does not assert a new equivalence with a different ramification definition in imperfect residue fields.

Tameness in this sense survives pointed étale localization of the smooth pair. At a point over the generic boundary, the map between the boundary DVRs is étale and keeps \(f\) as uniformizer. If \(T\) is the finite normalization before this base change, its tensor product with the new DVR is normal: it is étale over \(T\), and the closed local rings over each DVR branch again have its uniformizer as nonzerodivisor generating the maximal ideal and separable residue fibre. The tensor product is consequently the new normalization. The equation \(f=u s^e\) keeps the same branch index, and separable residue extensions remain separable after field base change and passage to a factor. At the filtered strict-local limit the same conclusion holds: its local branches retain the uniformizer, and their residue algebras are factors of the base-changed finite separable residue algebra. The normalization remains finite and normal by these local DVR descriptions. Thus the strict-local hypothesis used in the proposition is supplied by codimension-one tameness of the original smooth pair, not a new assumption about its total degree.

Finally let \(A\) be the strict localization of a smooth pair at a geometric point. The root equation, the finite cover and an isomorphism with the split cover are finitely presented. In the filtered system of pointed étale neighbourhoods defining \(A\), their finitely many coefficients, relations, inverse maps and inverse identities occur at one stage. After enlarging that stage, \(n\) is a unit there and the isomorphism holds. This gives an actual étale neighbourhood on which the sheaf extends over the root cover. Module operations and any specified finite diagram descend in the same way. For an adic system this assertion is made separately at each finite coefficient level: neither one root degree nor one neighbourhood is asserted to work for infinitely many levels. Lemma D.1a handles those compatible coefficient limits separately.

For the ramification statements, see the pinned [AI Integrated Stacks, More on Algebra](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex), `lemma-abhyankar` and `lemma-characterize-tame`, and [Fundamental Groups of Schemes](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/565b10e987aba5969b21145a0833f42d69f96790/pione.tex), `lemma-abhyankar-one-divisor`. The programme purity, gluing, regular-local algebra and henselian providers are the exact links above. The finite-cover argument uses their regular-local and henselian hypotheses.

### Proper transport of the specialization triangle

**Lemma B.3c.** Let \(S\) be a strictly henselian trait, choose geometric points \(\bar s\) and \(\bar\eta\) over its closed and generic points, and let \(h:X\to Y\) be a proper \(S\)-morphism. Write \(h_{\bar s}:X_{\bar s}\to Y_{\bar s}\) and \(h_{\bar\eta}:X_{\bar\eta}\to Y_{\bar\eta}\) for its fibre maps, and \(i_X,j_X,i_Y,j_Y\) for the respective maps from those fibres to the total spaces. For a bounded-below complex \(E\) of étale \(\Lambda=\mathbb Z/\ell^n\)-module sheaves on \(X\), define ordinary nearby cycles and the unshifted specialization cone by
\[
R\Psi_X E=i_X^*Rj_{X,*}j_X^*E,\qquad
R\Phi_X E=\operatorname{Cone}(i_X^*E\xrightarrow{u_X}R\Psi_X E).
\tag{B.8g}
\]
The map \(u_X\) is restriction of the adjunction unit. Then there are natural comparison isomorphisms
\[
\begin{aligned}
i_Y^*Rh_*E&\xrightarrow{\sim}Rh_{\bar s,*}i_X^*E,\\
R\Psi_Y(Rh_*E)&\xrightarrow{\sim}Rh_{\bar s,*}R\Psi_X E,\\
R\Phi_Y(Rh_*E)&\xrightarrow{\sim}Rh_{\bar s,*}R\Phi_X E.
\end{aligned}
\tag{B.8h}
\]
They identify the specialization triangles, including the first arrow and the connecting map. The comparison is natural for coefficient maps and geometric-generic-point automorphisms. In particular it retains the inertia action and any arithmetic descent present in the data. No invertibility of the degree of a finite \(h\) is required.

**Proof.** The input is the actual proper-base-change morphism proved in Constructible complexes, BE.7–BE.8. Its BZ.2 gives the corresponding strict-local transport argument. We spell out the maps and the prime-power coefficient check needed here. All derived images can be computed on underlying abelian complexes; naturality in scalar endomorphisms gives the displayed maps their \(\Lambda\)-linearity. Multiplication by \(\ell^n\) is the zero chain map on \(E\). Derived image is additive and therefore carries that zero morphism to multiplication by \(\ell^n\) on its image. Thus every cohomology sheaf of \(Rh_*E\), \(Rj_{X,*}j_X^*E\) and the other iterated images is killed by \(\ell^n\). These images are bounded below, since their left exact direct-image functors have bounded-below injective resolutions. Consequently BE.14 applies also to \(Rj_{X,*}j_X^*E\); its cohomology need not be constructible. No field-coefficient assumption from the opening scope of Appendix BZ is needed for this deduction.

Denote proper base change in the generic and special squares by \(\beta_j\) and \(\beta_i\). The first isomorphism in (B.8h) is \(\beta_i(E)\). The second is the following composite, with every term on \(Y_{\bar s}\):
\[
\begin{aligned}
i_Y^*Rj_{Y,*}j_Y^*Rh_*E
&\xrightarrow{i_Y^*Rj_{Y,*}\beta_j(E)}
 i_Y^*Rj_{Y,*}Rh_{\bar\eta,*}j_X^*E\\
&\xrightarrow{\sim}i_Y^*Rh_*Rj_{X,*}j_X^*E\\
&\xrightarrow{\beta_i(Rj_{X,*}j_X^*E)}
 Rh_{\bar s,*}i_X^*Rj_{X,*}j_X^*E.
\end{aligned}
\tag{B.8i}
\]
The middle arrow is derived composition for the equality \(j_Yh_{\bar\eta}=hj_X\), not base change for a nonproper direct image. Direct image preserves injectives because its left adjoint, inverse image of abelian sheaves, is exact. Composing these injective models therefore gives the stated derived-composition isomorphism. The two other arrows are BE.14 for the proper map \(h\), which remains proper after either change of base.

We check the specialization arrow itself. Before applying \(i_Y^*\), there are two maps from \(Rh_*E\) to \(Rj_{Y,*}Rh_{\bar\eta,*}j_X^*E\): the generic unit followed by \(Rj_{Y,*}\beta_j(E)\), and \(Rh_*\) of the unit \(E\to Rj_{X,*}j_X^*E\), followed by the composition identification. Transpose each through \(j_Y^*\dashv Rj_{Y,*}\) and then \(h_{\bar\eta}^*\dashv Rh_{\bar\eta,*}\). Both transposes are the same morphism
\[
j_X^*h^*Rh_*E\xrightarrow{j_X^*\epsilon_h(E)}j_X^*E,
\tag{B.8j}
\]
where \(\epsilon_h:h^*Rh_*E\to E\) is the counit. For the first map this is the defining adjoint of \(\beta_j\). For the second, the \(j_X\)-unit followed by its counit cancels by the adjunction triangle identity, leaving precisely (B.8j). Equality of the transposes proves equality of the two maps. Restricting to \(Y_{\bar s}\) and using naturality of \(\beta_i\) now identifies \(u_Y\) with \(Rh_{\bar s,*}u_X\) under (B.8h).

Use the mapping-cone triangles of these maps on injective complex models, as constructed for abelian sheaves in Constructible complexes, BF.3–BF.4. A homotopy-commuting square is carried to its cone map with the homotopy in the off-diagonal entry; its cone inclusion and projection commute with the first two maps. This is the cone comparison for the unit/counit construction above, not an arbitrary choice of a third arrow from an abstract isomorphism of groups. Derived direct image preserves these cone models. The comparison of their first two terms therefore induces the third isomorphism of (B.8h), with its connecting map and the convention (B.8g). All comparisons were defined by restriction, composition, units and counits. Applying a coefficient homomorphism or an automorphism of the chosen geometric generic point preserves each defining transpose, hence preserves the entire comparison. This proves the asserted actions without a choice of inertia generator. \(\square\)

Two consequences identify the uses below. For a proper \(f:X\to S\), apply the lemma to \(h=f\). The geometric-point form of BE.8 identifies the resulting middle term with \(R\Gamma(X_{\bar\eta},E|_{X_{\bar\eta}})\). Thus applying \(R\Gamma(X_{\bar s},-)\) to the specialization triangle gives the actual special-to-generic cohomology map used in (C.5). For a finite boundary map, its geometric direct image is the finite sum of the fibre stalks and has no higher direct images. A constant section restricts to that same section at every generic point; when the special fibre has one underlying point and the generic fibre is the finite set \(B\), the unit is exactly the diagonal \(\Lambda\to\Lambda^B\). This gives the map in the tangency calculation, including a possibly wild permutation action.

The lemma applies to closed immersions, finite normalizations and finite root covers because they are proper. It does not assert commutation with arbitrary nonproper pushforward. It supplies the ordinary finite-level comparison only: normalized adic nearby cycles and passage through coefficient limits require their own comparison. The recursive algebraic, curve and cohomological inputs of BE.1–BE.8 remain the stated dependencies of the provider.

### Vanishing away from the exceptional points

We give the transverse boundary deduction with its cohomological inputs explicit. Use the proved tame Kummer covering description of a strictly local regular pair together with ordinary smooth local acyclicity for finite torsion coefficients of order invertible on the surface, as proved in Constructible complexes, AT.3 and AT.5. The required ordinary finite/proper pushforward comparison, including the specialization cone, is [Lemma B.3c](#proper-transport-of-the-specialization-triangle). The covering description says that a finite tame local system on the complement of a smooth divisor becomes constant after a cover obtained by adjoining a prime-to-characteristic root of its boundary parameter. Lemma B.3a and Proposition B.3b above prove the general tame DVR calculation and the strictly local covering description. Their purity and extension inputs are the exact programme proofs in Constructible complexes, AP.1–AP.5 and AQ.1–AQ.2. No prime-to-characteristic restriction on the total degree is introduced. Proposition B.2 alone does not supply this separate finite-cover argument.

**Lemma B.4.** Under these inputs, if both \(f:X\to B\) and \(D\to B\) are smooth near a point of a smooth boundary divisor, then
\[
R\Phi_f(j_!L)=0
\tag{B.9}
\]
there for every finite tame lisse sheaf \(L\) on \(X-D\). The same deduction applies to adic sheaves by [Lemma C.2a](#normalized-nearby-cycles-and-the-completed-fibre): its normalized comparison retains the finite specialization cones, and a complete complex with zero reductions is zero.

**Proof.** For a constant module \(M\), the sequence
\[
0\longrightarrow j_!M\longrightarrow M_X
\longrightarrow i_*M_D\longrightarrow0
\tag{B.10}
\]
reduces the claim to smooth local acyclicity on \(X,D\), using [Lemma B.3c](#proper-transport-of-the-specialization-triangle) for the proper closed immersion \(i\). The constant sheaves meet the locally constant invertible-torsion hypotheses of Constructible complexes, AT.3; AT.5 identifies their actual specialization units, so their cones vanish. This applies separately on the smooth total space and smooth boundary after passage to the strict trait. It neither assumes the Kummer degree invertible in the coefficient ring nor passes to adic coefficients.

Pass to the strictly local pair. Choose a Kummer cover \(g:X'\to X\), given in transverse coordinates by \(y=v^m\), which makes \(L\) constant on its open complement \(U'\); here \(m\) is prime to the field characteristic. Both \(X'\) and its boundary remain smooth over \(B\). On the complements, the adjunction map embeds \(L\) into \(g'_*g'^*L\): after the étale cover it is the diagonal map into a direct sum indexed by the cover. The cokernel is again a local system trivialized by that same cover. Iteration gives
\[
0\longrightarrow L_i\longrightarrow g'_*M_i
\longrightarrow L_{i+1}\longrightarrow0,
\qquad L_0=L,
\tag{B.11}
\]
where each \(M_i\) is constant on \(U'\). Extension by zero is exact, and \(j_!g'_*M_i=g_*j'_!M_i\). The middle term has zero vanishing cycles by (B.10) upstairs and [Lemma B.3c](#proper-transport-of-the-specialization-triangle). Thus
\[
R\Phi_f(j_!L_i)\simeq R\Phi_f(j_!L_{i+1})[-1].
\tag{B.12}
\]
For a degree-zero sheaf, the defining cone of its specialization map to \(R\Psi\) has no cohomology below degree \(-1\). Iterating (B.12) more than \(q+1\) times identifies its degree-\(q\) cohomology with a group below degree \(-1\), which is zero. This proves all degrees vanish. It does not divide by \(m\), so it is valid even when the coefficient prime divides the Kummer degree.

For an adic sheaf, choose a stable lattice and apply the finite argument to its reductions. [Lemma C.2a](#normalized-nearby-cycles-and-the-completed-fibre) carries their zero nearby-cycle cones to zero in the derived-complete category, and inverting the coefficient prime preserves zero. Alternatively, for the tame-unipotent coefficients of Appendix A, the procyclic local tame representation has a finite flag with trivial grades. Extend those grades as constant sheaves and use (B.10) successively. This shorter argument still requires the local covering description and ordinary local-acyclicity formalism. \(\square\)

Apply the lemma to \(j_!\pi^*G\) on the pencil surface. Off the exceptional values, the boundary is smooth over the parameter line, so (B.9) and interior smooth local acyclicity give local acyclicity everywhere. Proper compatibility and constructibility then give lisse sheaves \(R^rf_!\pi^*G\) on that parameter open. Over a strict trait at an exceptional value, vanishing cycles are supported at its unique exceptional point. This proves the support reduction used for (A.11), relative to the stated ordinary foundations. Propositions C.1–C.3 compute the étale cohomology of that local model, its arithmetic descent and the two boundary cases, proving the required degree-one concentration.

## Appendix C. Arithmetic at the exceptional point

The three rows of (A.10) have different geometric origins. A node compares two proper components with one smooth conic. A boundary tangency compares one special point with two nearby points. A boundary crossing requires two successive localization sequences. We compute each before passing to filtered coefficients.

Our convention throughout is
\[
R\Phi_f K=\operatorname{Cone}(i^*K\longrightarrow R\Psi_fK).
\tag{C.1}
\]
In particular a sheaf supported on the special fibre has vanishing cycles equal to its shift by \([1]\), not by \([-1]\). Initially let \(\Lambda=\mathbb Z/\ell^n\), with \(\ell\) invertible on the surface. For a two-element set \(B\), put
\[
\varepsilon_\Lambda(B)=\Lambda^B/\Lambda_{\mathrm{diag}}.
\tag{C.2}
\]
It is free of rank one, and interchanging the elements acts by \(-1\). This description also works at \(\ell=2\); only its reduction modulo two has trivial sign.

The ordinary foundations used below are finite-coefficient proper base change, smooth local acyclicity, the specialization triangle and its étale locality, finite normalization, and the cohomology of the projective line with the degree-one Chern-class normalization. For the smooth local-acyclicity input, Constructible complexes, AT.1–AT.3 gives the strict-local restriction isomorphism for locally constant invertible-torsion coefficients, and AT.5 identifies it with the nearby-cycle unit. Its input is the canonical smooth comparison of AS.1–AS.7, with the actual stalk map in AT.1. Thus the constant finite coefficients used here have zero ordinary vanishing cycles on the smooth locus. The intrinsic branch calculation uses the smooth-pair purity and explicit root-tower calculation of [Lemma C.0a](#two-parameters-and-their-actual-root-tower) below, at the equal-characteristic smooth-surface scope of B.2–B.3. Ordinary proper comparison and its specialization triangle are supplied by [Lemma B.3c](#proper-transport-of-the-specialization-triangle) from BE.7–BE.8 and BZ.2. The normalized finite-system and completed-fibre comparison is supplied by [Lemma C.2a](#normalized-nearby-cycles-and-the-completed-fibre). For the projective line, Constructible complexes, BI.2 constructs the unit/Chern-class splitting, sends \(c_1(\mathcal O(1))\) to \(1\), and proves naturality; AL.3 preserves this actual degree map under field extension. AL.2 supplies the exact finite pushforward for the nonflat normalization and point immersion in (C.6). The recursive curve, coefficient-continuity and algebraic foundations of those providers are required hypotheses of these comparisons. No weight estimate or perverse purity theorem is an input to the local computations.

### Two parameters and their actual root tower

**Lemma C.0a (the two-parameter root calculation).** Let \(S=\operatorname{Spec}R\) be the strict localization at a geometric closed point of a smooth surface over a field of characteristic \(p\). Let \(u,v\) be étale coordinates there, put \(D_u=V(u)\), \(D_v=V(v)\), and write \(U=S\setminus(D_u\cup D_v)\). Fix \(\Lambda=\mathbb Z/\ell^n\), with \(\ell\ne p\). In characteristic zero every positive integer is understood to be prime to \(p\). Then the Kummer classes give
\[
\begin{aligned}
H^0(U,\Lambda)&=\Lambda,\\
H^1(U,\Lambda)&=\Lambda(-1)^{\oplus2},\\
H^2(U,\Lambda)&=\Lambda(-2),\\
H^q(U,\Lambda)&=0\quad(q>2).
\end{aligned}
\tag{C.K1}
\]
More precisely, the degree-one classes in twisted cohomology are \(\kappa(u),\kappa(v)\in H^1(U,\Lambda(1))\), their squares are zero even when \(\ell=2\), and \(\kappa(u)\smile\kappa(v)\) generates \(H^2(U,\Lambda(2))\). These statements specify the exterior-algebra identification, not just the ranks.

For \(m\) prime to \(p\), form
\[
\begin{aligned}
R_m&=R[a_m,b_m]/I_m,\\
I_m&=(a_m^m-u,b_m^m-v),\\
U_m&=\operatorname{Spec}R_m[1/(a_mb_m)].
\end{aligned}
\tag{C.K2}
\]
For \(m\mid mr\), the transition is \(a_m\mapsto a_{mr}^{r}\), \(b_m\mapsto b_{mr}^{r}\). In the indicated Kummer bases its pullback multiplies degree \(q\) by \(r^q\). The affine limit \(U_\infty=\varprojlim_m U_m\) has constant cohomology \(\Lambda\) in degree zero and zero in every positive degree.

If \(t=uv\) is the parameter of the strict trait in Proposition C.1, the intermediate tower obtained by adjoining roots of \(t\) has cohomology computed by the kernel of multiplication
\[
\begin{aligned}
\Gamma&=\widehat{\mathbb Z}^{(p')}(1)^2,\\
H&=\ker\left(\Gamma\longrightarrow\widehat{\mathbb Z}^{(p')}(1)\right),\\
&\hspace{1em}(\zeta,\xi)\longmapsto\zeta\xi.
\end{aligned}
\tag{C.K3}
\]
Here multiplicative notation at each finite root level becomes addition in (C.10). The calculation concerns this equal-characteristic smooth pair; it does not invoke absolute purity for arbitrary regular mixed-characteristic schemes.

**Proof: localization, including the product sign.** Constructible complexes, AL.1 proves that sections on a strictly henselian local scheme equal its closed geometric stalk and are exact. It applies to \(S,D_u,D_v\) and their closed intersection. Finite Tate sheaves on each are constant, since every prime-to-characteristic root of unity lifts from the separably closed residue field. Thus their positive cohomology vanishes, and their degree-zero groups are the stated Tate lines.

The closed-support triangle and its maps are those of M.5. For our coordinate divisors, BJ.6 gives smooth-pair purity and its Gysin counit. Apply it first on the smooth étale neighbourhoods defining \(S\). BA.5 carries the cohomology of the neighbourhood, divisor and complement, with their actual restriction maps, to the strict-local limit. Supported cohomology is the fibre of the restriction map, so exact filtered colimits carry its long exact sequence too. The cup products and coefficient maps descend on the same finite diagrams. This justifies using this particular purity sequence on \(S\); no general exceptional-base-change assertion is being assumed.

Put \(U_u=S\setminus D_u\). The sequence is
\[
\begin{aligned}
\cdots&\longrightarrow H^{q-2}(D_u,\Lambda(j-1))\\
&\longrightarrow H^q(S,\Lambda(j))\\
&\longrightarrow H^q(U_u,\Lambda(j))\\
&\xrightarrow{\partial_u}H^{q-1}(D_u,\Lambda(j-1))\\
&\longrightarrow\cdots .
\end{aligned}
\tag{C.K4}
\]
The preceding vanishing proves that \(H^0(U_u,\Lambda(j))=\Lambda(j)\), \(H^1(U_u,\Lambda(j))=\Lambda(j-1)\), and every higher group is zero. Under the positive orientation, \(\partial_u\kappa(u)=-1\). Indeed BJ.6 identifies the positive parameter-section class with the negative supported Kummer boundary, using AI.2. Thus \(\kappa(u)\) is the specified generator, not merely a nonzero class. Applying the same argument on the strict local curve \(D_v\), with closed point cut out by \(u\), gives for \(E=D_v\setminus D_u\) degree zero \(\Lambda(j)\), degree one \(\Lambda(j-1)\) generated by the restricted \(\kappa(u)\), and no higher groups.

Remove \(E\) from \(U_u\). Smooth-pair purity on this open gives the same sequence as (C.K4), now with \((D_u,S,U_u)\) replaced by \((E,U_u,U)\). Its degree-one part is
\[
\begin{aligned}
0&\longrightarrow H^1(U_u,\Lambda(j))\\
&\longrightarrow H^1(U,\Lambda(j))\\
&\xrightarrow{\partial_v}H^0(E,\Lambda(j-1))\\
&\longrightarrow0.
\end{aligned}
\tag{C.K5}
\]
The Kummer class \(\kappa(v)\) has boundary \(-1\), so it splits this sequence, with the minus sign if the target generator is \(+1\). In degree two the boundary is an isomorphism to \(H^1(E,\Lambda(j-1))\); in larger degrees the neighbouring groups vanish.

We identify the degree-two generator explicitly. If \(\alpha\) is a degree-\(r\) cocycle on \(U_u\) and \(\beta\) a class on its complement, the localization connecting map obeys
\[
\begin{aligned}
&\partial_v(\alpha|_U\smile\beta)\\
&\qquad=(-1)^r\alpha|_E\smile\partial_v\beta.
\end{aligned}
\tag{C.K6}
\]
To check the sign, lift a representative of \(\beta\) to the middle complex in a short exact model of the support triangle. Differentiating its product with the closed cocycle \(\alpha\) gives \((-1)^r\alpha\smile d\widetilde\beta\). This is the connecting representative; the purity shift is two and adds no further parity. The support-module identification is the Gysin counit's projection formula in BJ.6 and BH.7. Hence \(\partial_v(\kappa(u)\smile\kappa(v))=\kappa(u)|_E\), since both signs are negative. This proves the product assertion. The square of \(\kappa(u)\) is pulled back from \(H^2(U_u,\Lambda(2))=0\). Exchanging \(u,v\) proves the square of \(\kappa(v)\) is zero. Graded commutativity gives the remaining relation. In particular the square-zero assertion does not divide the identity \(2\alpha^2=0\) by two. This proves (C.K1), with its maps and all coefficient twists.

**Proof: the root maps and the limit.** The algebra \(R_m\) is finite over the henselian local ring \(R\), and its closed fibre is \(\kappa(\bar x)[a_m,b_m]/(a_m^m,b_m^m)\), with one maximal ideal and the same separably closed residue field. The finite-algebra decomposition and lifting in AL.1 therefore make \(R_m\) strictly henselian local. It is also the strict-local coordinate chart obtained by base change of the original étale surface chart along \((a,b)\mapsto(a^m,b^m)\), followed by the selected local limit. It is regular with parameters \(a_m,b_m\): the finite-stage chart is étale over the smooth \((a,b)\)-plane. Thus the preceding two-divisor proof applies to \(R_m\). The punctured chart is connected, since these strict-local regular coordinate rings are domains. On it both polynomial derivatives are units, so \(U_m\to U\) is the finite étale \(\mu_m^2\)-torsor described by the actual root equations.

The Kummer sequence is natural and \(\kappa(z^r)=r\kappa(z)\). Consequently the displayed transition sends each degree-one generator to \(r\) times its namesake upstairs, and sends their product to \(r^2\) times the product. Degree zero maps identically. For fixed coefficients, a transition with \(r=\ell^n\) kills every positive degree; it is allowed because \(\ell\ne p\). BA.5 applies to these affine schemes and finite transitions, and identifies cohomology on \(U_\infty\) with the direct limit under these actual pullbacks. The result is \(\Lambda\) in degree zero and zero above, as claimed. No interchange with an inverse limit of cohomology groups is used.

**Proof: the intermediate tower and descent.** Let \(K\) be the fraction field of the strict trait, and choose compatible roots of \(t\). Its maximal tame extension is \(K^t=\bigcup_{(m,p)=1}K(t^{1/m})\): a tame extension of a strictly henselian trait has separable residue extension, hence trivial residue extension, and its prime-to-\(p\) uniformizer ramification is removed by precisely such a root, as in Lemma B.3a. There is no remaining nontrivial finite étale extension of the strict trait. Set \(W=U\times_K K^t\).

At level \(m\) the product \(a_mb_m\) is a root of \(t\). Multiplying its two root coordinates by \((\zeta,\xi)\) multiplies that product by \(\zeta\xi\). This gives (C.K3) and identifies \(W\) with the intermediate root tower. Concretely, the invariants of the subgroup \((\zeta,\zeta^{-1})\) in the root algebra are generated over the base by \(a_mb_m\): in its monomial basis a term \(a_m^ib_m^j\) is invariant exactly when \(i=j\bmod m\). This assertion can be checked after the finite étale trivialization, so it does not divide by \(m\) in \(\Lambda\). The compatible limit is a pro-finite-étale \(H\)-torsor \(U_\infty\to W\).

Here is the descent argument needed to use its acyclicity. Write that torsor as a limit of connected finite Galois covers \(V_i\to W\), with groups \(H_i\). The augmented Čech complexes of the covers are exact as complexes of sheaves: locally choose a lift, and inserting it is a contracting homotopy. Filtered colimits remain exact. The degree-\(r\) term is the colimit of the direct images from \(V_i^{\times_W(r+1)}\). Finite pushforward is exact and computes cohomology on the source by AL.2, with its arbitrary-base extension AX.5. The torsor identity identifies this fibre product with \(H_i^r\times V_i\). BA.5, including its fixed-scheme filtered-coefficient assertion, therefore computes the higher cohomology of the colimit term as the colimit of functions from \(H_i^r\) to \(H^q(V_i,\Lambda)\). For \(q>0\), every such finite list dies at a common later stage, since the limit is \(H^q(U_\infty,\Lambda)=0\). In degree zero, connectedness gives exactly the continuous functions \(H^r\to\Lambda\).

Thus this exact augmented sheaf resolution is acyclic for sections in every term. Its section complex is the continuous group-cochain complex, with the ordinary alternating Čech faces. It gives the canonical comparison
\[
H^q(W,\Lambda)=H^q_{\mathrm{cont}}(H,\Lambda).
\tag{C.K7}
\]
The comparison is natural in the root characters and in their permutation. In degree one it sends the two Kummer torsors to the restrictions to \(H\) of the two coordinate characters of \(\Gamma\). Those restrictions are opposite and either generates the \(\ell\)-primary character line. The continuous cohomology of that line is computed explicitly immediately after (C.10). This proves the precise root-tower input used there, without using a weight theorem, perverse purity, or a characteristic-zero topological model. \(\square\)

### Compute a node inside a proper family

**Proposition C.1.** For the étale local equation \(uv=t\) of Lemma B.3, the full finite-coefficient vanishing cycles satisfy
\[
\Phi_x^q(\Lambda)=0\quad(q\ne1),\qquad
\Phi_x^1(\Lambda)\simeq\Lambda(-1)\otimes\varepsilon_\Lambda(B),
\tag{C.3}
\]
where \(B\) is the set of the two geometric branches. The isomorphism respects arithmetic descent: geometric Frobenius acts by its Tate character times its permutation sign on \(B\).

**Proof of concentration and rank.** Work first over a strictly henselian trait \(T=\operatorname{Spec}R\), with uniformizer \(t\). Compactify the displayed local model as
\[
C=\{XY=tZ^2\}\subset\mathbb P^2_R.
\tag{C.4}
\]
The only nonsmooth point of the map on the special fibre is \(x=[0:0:1]\). The chart \(Z=1\) is exactly \(uv=t\). The special fibre consists of two projective lines, indexed by \(B\), meeting at \(x\). The geometric generic fibre is a smooth conic with a rational point, hence a projective line. For example its parametrization is
\[
[s:r]\longmapsto[t s^2:r^2:sr];
\]
on the charts with \(s\ne0\) or \(r\ne0\), the inverse is given by the corresponding ratio of the displayed coordinates. The equations and parametrization remain valid in characteristic two.

The ordinary smooth-locus comparison of Constructible complexes, AT.5 puts all vanishing cycles at \(x\). If \(V^q=\Phi_x^q(\Lambda)\), [Lemma B.3c](#proper-transport-of-the-specialization-triangle) applied to this proper conic family gives
\[
\cdots\to H^q(C_{\bar s},\Lambda)\to
H^q(C_{\bar\eta},\Lambda)\to V^q\to
H^{q+1}(C_{\bar s},\Lambda)\to\cdots.
\tag{C.5}
\]
For the normalization \(\nu\) of the special fibre, the exact sheaf sequence is
\[
0\to\Lambda_{C_{\bar s}}\to
\nu_*\Lambda_{\mathbb P^1\sqcup\mathbb P^1}\to
\Lambda_x\otimes\varepsilon_\Lambda(B)\to0.
\tag{C.6}
\]
At the intersection its maps are the diagonal and the quotient in (C.2); elsewhere exactness is immediate. The degree-zero quotient map \(\Lambda^B\to\varepsilon_\Lambda(B)\) is onto. Projective-line cohomology therefore gives
\[
H^0(C_{\bar s},\Lambda)=\Lambda,\qquad
H^1(C_{\bar s},\Lambda)=0,\qquad
H^2(C_{\bar s},\Lambda)=\Lambda(-1)^B,
\tag{C.7}
\]
with higher groups zero. The generic fibre has the same groups except that its degree-two group has only one summand.

The degree-zero specialization is the identity on constant sections. We must identify the degree-two map, rather than assume it from a vanishing-cycle formula. The two sections \([1:0:0]\) and \([0:1:0]\) of (C.4) lie in the smooth locus and meet different special components. They are Cartier divisors: in the chart \(X=1\), the first is \(Z=0\) with \(Y=tZ^2\), and the other chart is identical with the variables exchanged. Each divisor has degree one on its generic fibre, degree one on the special component it meets, and degree zero on the other component.

Here is the Chern-class compatibility being used. For an invertible \(m\), the kernel of the power map on \(\mathbb G_m\) is \(\mu_m\), and a unit \(a\) acquires an \(m\)-th root on the finite étale cover defined by \(z^m=a\): the derivative \(mz^{m-1}\) is invertible. Thus the Kummer sequence is exact on the étale site. Its cohomology connecting map sends a line bundle to \(c_1\in H^2(\mu_m)\), naturally under restriction. Apply it to the two section divisors, with \(m=\ell^n\). By the degree-one normalization on a projective line, each component basis class specializes to the generic basis class. Hence the map in degree two is exactly
\[
\Sigma:\Lambda(-1)^B\longrightarrow\Lambda(-1),
\qquad(a_b)\longmapsto\sum_{b\in B}a_b.
\tag{C.8}
\]
It is surjective. The exact sequence (C.5) now gives zero in every degree except one, and \(V^1=\ker\Sigma\).

There is a permutation-equivariant isomorphism
\[
\varepsilon_\Lambda(B)\longrightarrow
\ker(\Lambda^B\xrightarrow{\Sigma}\Lambda),
\qquad [e_b]\longmapsto e_b-e_c\quad(B=\{b,c\}).
\tag{C.9}
\]
The two images sum to zero, and either image is a basis of the kernel. No division by two occurs. This proves the asserted full rank and concentration. In the split conic, inertia acts trivially on the component cohomology and on the Tate twist: roots of unity of order prime to the residue characteristic belong to the maximal unramified extension. It therefore acts trivially on \(V^1\). In particular there is no additional wild-inertia contribution. Étale locality transports these facts to the split germ from Lemma B.3.

**Proof of the intrinsic arithmetic factor.** A coordinate change of a nodal germ need not extend to our compactification, so the component computation alone does not justify arbitrary arithmetic descent. To identify its intrinsic generator, use the tame root covers of its two parameters. Their group maps by addition as
\[
\widehat{\mathbb Z}^{(p')}(1)^2\longrightarrow
\widehat{\mathbb Z}^{(p')}(1),
\tag{C.10}
\]
where the target records roots of \(t=uv\). The kernel is a single copy of \(\widehat{\mathbb Z}^{(p')}(1)\). Lemma C.0a proves the exterior Kummer calculation, the actual root-cover pullbacks (multiplication by \(m^q\) in positive degree \(q\) for the \(m\)-th root map), and the acyclicity of their affine limit in this smooth-surface setting. Its explicit descent comparison (C.K7) computes tame geometric nearby cohomology from the kernel in (C.10), and identifies the two coordinate Kummer characters under that comparison. No stronger absolute-purity assertion is needed.

For completeness, the last group calculation has no higher-degree term. Prime-to-\(\ell\) finite quotients have exact invariants by averaging. For the remaining \(\mathbb Z_\ell\), its completed group algebra has the resolution
\[
0\to\Lambda[[\mathbb Z_\ell]]
\xrightarrow{\gamma-1}\Lambda[[\mathbb Z_\ell]]\to\Lambda\to0.
\]
Writing the algebra as \(\Lambda[[T]]\) makes injectivity the injectivity of multiplication by \(T\). Applying continuous Hom with trivial coefficients gives one copy of \(\Lambda\) in each of degrees zero and one, with the degree-one Tate twist arising from (C.10). Thus the degree-one Kummer classes satisfy
\[
[u]+[v]=[t]=0,\qquad
[u]\text{ generates }R^1\Psi^t(\Lambda)(1).
\tag{C.11}
\]
Wild invariants are exact for \(\ell\)-primary coefficients, since every relevant finite wild quotient is a \(p\)-group. Tame nearby cohomology is therefore the wild-invariant part of full nearby cohomology. The conic computation has already made that wild action trivial in this specific germ, so (C.11) identifies its full degree-one group.

A branch-preserving change replaces a branch parameter by a unit times that parameter. Every unit on the strictly local total scheme has an \(\ell^n\)-th root, by the same étale polynomial and the strictly henselian property; its Kummer class vanishes. Exchanging branches instead sends \([u]\) to \([v]=-[u]\). Thus the sole extra arithmetic character is the permutation sign of the branches. Removing the twist in (C.11) gives (C.3), including its Frobenius action. Notice that \([u/v]=2[u]\); it is not an integral generator at \(\ell=2\). \(\square\)

### The two boundary configurations

**Proposition C.2.** Suppose that the surface map is smooth at \(x\), and let \(j\) denote the complement of its boundary. At a simple boundary tangency,
\[
R\Phi_f(j_!\Lambda)_x\simeq
\varepsilon_\Lambda(B)[-1],
\tag{C.12}
\]
where \(B\) is the set of two geometric nearby boundary points. At a transverse crossing of two boundary branches the same formula holds, with \(B\) the branch set. Both identifications retain the full permutation action, and neither has a Tate factor.

**Proof at a tangency.** In the strictly local trait the boundary map is finite of degree two and generically separable by Proposition B.2. Its geometric generic fibre is \(B\); its special fibre has one underlying geometric point. Nilpotents do not change the étale site. The finite-map case of [Lemma B.3c](#proper-transport-of-the-specialization-triangle) gives nearby cohomology \(\Lambda^B\) in degree zero and identifies the specialization map with the diagonal \(\Lambda\to\Lambda^B\). Thus, for the boundary immersion \(i_D\),
\[
R\Phi_f(i_{D*}\Lambda_D)_x=\varepsilon_\Lambda(B)[0].
\]
Apply (C.1) to the exact sequence
\[
0\to j_!\Lambda\to\Lambda_X\to i_{D*}\Lambda_D\to0.
\tag{C.13}
\]
The middle term has zero vanishing cycles by Constructible complexes, AT.5, at the stated finite invertible coefficient level. The resulting triangle gives (C.12), with its nonzero cohomology in degree one.

In characteristic two, the boundary germ (B.6) is separable because its cubic coefficient is nonzero. Its two-point permutation action can be wildly ramified as a representation of the parameter trait. This is allowed in (C.12). The inseparable germ \(t=u^2\) would have only one geometric nearby point and cannot be substituted. Tameness of the coefficient around the boundary divisor is a separate condition from ramification of this boundary map.

**Proof at a crossing.** Write \(\nu:D'\to D\) for the boundary normalization and \(S_x=\Lambda_x\otimes\varepsilon_\Lambda(B)\). Stalkwise diagonal and quotient maps give
\[
0\to j_!\Lambda\to\Lambda_X\to\nu_*\Lambda_{D'}\to S_x\to0.
\tag{C.14}
\]
Let \(T\) be the image of its middle map. The ambient map and both normalized branch maps are smooth. Therefore \(R\Phi_f\Lambda_X=0\) and \(R\Phi_f\nu_*\Lambda_{D'}=0\), using [Lemma B.3c](#proper-transport-of-the-specialization-triangle) for the finite normalization in the latter. Since \(S_x\) has zero generic restriction, (C.1) gives \(R\Phi_f S_x=S_x[1]\), concentrated in degree \(-1\). Applying vanishing cycles to the two short exact sequences defined by \(T\) gives
\[
R\Phi_f(j_!\Lambda)=R\Phi_fT[-1]
=R\Phi_fS_x[-2]=S_x[-1].
\tag{C.15}
\]
All maps respect permutations of the two branches. This proves the second formula and its arithmetic sign. \(\square\)

### Normalized nearby cycles and the completed fibre

**Lemma C.2a.** The finite-system comparison needed here is a comparison in the derived-complete category, not an interchange of an ordinary stalk and an inverse limit. Let \(O\) be the integers of a finite extension of \(\mathbb Q_\ell\), with uniformizer \(\pi\), and write \(O_n=O/\pi^n\). Let \(X\) be a scheme over a strictly henselian trait \(S\), with \(\ell\) invertible on \(S\). Choose geometric closed and generic points, and denote the induced maps by \(i:X_{\bar s}\to X\) and \(j:X_{\bar\eta}\to X\). On each pro-étale site use the constant coefficient sheaf \(\underline O\). Write \(C\) for derived \(\pi\)-completion, \(D^c\) for its complete objects, and \(a_c^*=Ca^*\) for completed inverse image.

Let \(K\in D^c(X_{\mathrm{pro\acute et}},\underline O)\), and suppose its actual derived reductions \(K_n=K\otimes_O^LO_n\) come from bounded-below étale complexes \(K_n^{\mathrm e}\). Use the coherent reduction diagram, with its quotient transitions, rather than independently chosen identifications at each level. Define
\[
\begin{aligned}
R\Psi^c K&=i_c^*Rj_*j_c^*K,\\
u_K^c&:i_c^*K\longrightarrow i_c^*Rj_*j_c^*K,\\
R\Phi^c K&=\operatorname{Cone}(u_K^c).
\end{aligned}
\tag{C.14a}
\]
Here \(u_K^c\) is \(i_c^*\) applied to the unit of \(j_c^*\dashv Rj_*\); the cone has the convention (C.1). These are complete complexes, and their reductions, including the unit and the cone maps, are
\[
\begin{aligned}
(R\Psi^c K)_n&\simeq
 \nu_{\bar s}^*\bigl(i_{\mathrm e}^*Rj_{\mathrm e,*}j_{\mathrm e}^*K_n^{\mathrm e}\bigr),\\
(R\Phi^c K)_n&\simeq
 \nu_{\bar s}^*\operatorname{Cone}
 \bigl(i_{\mathrm e}^*K_n^{\mathrm e}
 \longrightarrow i_{\mathrm e}^*Rj_{\mathrm e,*}j_{\mathrm e}^*K_n^{\mathrm e}\bigr).
\end{aligned}
\tag{C.14b}
\]
The map \(\nu_{\bar s}\) is the pro-étale to étale morphism of sites. In particular these are the normalized coefficient-diagram nearby cycles. When the reductions have the constructibility and boundedness established by the local calculations below, they belong to the constructible adic category.

For a geometric point \(x:\operatorname{Spec}\Omega\to X_{\bar s}\), its completed geometric fibre is \(x_c^*R\Phi^c K\). Its cohomology as a coefficient complex is computed by
\[
R\Gamma\bigl((\operatorname{Spec}\Omega)_{\mathrm{pro\acute et}},
 x_c^*R\Phi^c K\bigr)
\simeq
R\varprojlim_n (R\Phi K_n^{\mathrm e})_{\bar x}.
\tag{C.14c}
\]
This comparison retains the coefficient transitions, inertia, arithmetic descent and all maps of specialization triangles.

**Proof.** The constructions and their maps are the ones proved in Constructible complexes, BK.1–BK.6 and BL.6. In particular
\[
(C A)\otimes_O^LO_n\simeq A\otimes_O^LO_n,\qquad
(Ra_*A)\otimes_O^LO_n\simeq Ra_*(A\otimes_O^LO_n)
\tag{C.14d}
\]
are the actual reduction maps. The second uses the perfect two-term \(O\)-complex \([O\xrightarrow{\pi^n}O]\), not a claim that \(O_n\) has finite projective dimension over every \(O_m\). Its transition from \(m\) to \(n\) is multiplication by \(\pi^{m-n}\) in degree minus one and the identity in degree zero. Derived image preserves this finite cone and its transition maps. It also preserves homotopy limits, as the right adjoint of exact inverse image. Thus it preserves completeness. Completion, completed inverse image and finite cones have the other stated completeness properties.

Apply (C.14d) successively to \(j_c^*,Rj_*,i_c^*\). For the passage from the pro-étale image to the étale image use the actual comparison BK.4, proved in BK.2. Its direct-image hypothesis is qcqs, with bounded-below classical coefficients. It applies to this \(j\): the generic point of the affine trait is the principal open of a uniformizer, extension to its geometric field is affine, and \(j\) is the base change of their composite. Hence \(j\) is affine, in particular qcqs. It need not be of finite type. We have not applied a finite-type six-operation theorem to this geometric-generic-point map.

BL.6 identifies the reductions of its completed adjunction unit and counit with the ordinary finite-coefficient unit and counit. BK.2 identifies the pro-étale/étale comparison by those same restriction maps. Consequently the first comparison of (C.14b) carries the reduction of \(u_K^c\) to the finite-level specialization unit, not merely to some map between isomorphic objects. Taking the actual cone comparison gives its second line and connecting map. The cone models and homotopy-square maps are BF.3–BF.4.

The word “normalized” here specifies a category and a functor. BR.1–BR.4 identifies complete complexes with actual derived-cartesian coefficient diagrams. BS.1–BS.3 supplies their bounded-below étale presentation, retaining transitions, units, counits and derived morphisms. Thus (C.14b) identifies the coefficient diagram of (C.14a) with the finite nearby-cycle diagram in that presentation. In the present application the reductions of the input lattice extended by zero are sheaves: the nearby-cycle reductions have lower bound zero and their cone reductions lower bound minus one, uniformly in \(n\). This supplies the common lower bound for the bounded-below diagram comparison. No equivalence with the bounded derived category of its heart is being assumed.

To prove (C.14c), apply completed inverse image to the cone. BL.6 identifies each of its reductions with
\(\nu_x^*(R\Phi K_n^{\mathrm e})_{\bar x}\).
Completeness reconstructs the object as the homotopy limit of these actual reductions, by BK.4. Derived sections is a right adjoint, so it preserves that homotopy limit. On the geometric point the étale coefficient category is the category of coefficient modules; its sections functor is exact. The comparison BK.3 therefore identifies the derived sections of each displayed classical pullback with \((R\Phi K_n^{\mathrm e})_{\bar x}\) itself. Taking the homotopy limit gives (C.14c). Only derived sections **after completed inverse image** have been moved past the limit; an arbitrary ordinary sheaf stalk has not.

All maps just used come from coefficient reduction, adjunction and restriction. Pullback by a geometric-generic-point automorphism commutes with these constructions, so the comparisons preserve the actual inertia actions and their arithmetic descent. The same argument preserves the connecting map in a coefficient-filtration triangle. If every finite cone is zero, the complete cone is zero by BK.4's reduction detection. This proves the finite-to-adic vanishing used in Appendix B. Likewise the completed proper-transport mate reduces to Lemma B.3c's proper-transport map at every level; its complete cone has zero reductions, so that mate is an isomorphism.

For the constructible assertion needed by Proposition C.3, work on the geometric special fibre of the finite-type surface family. The finite calculations concentrate the cone on its finite exceptional locus and give finite modules there, in one degree. Its first reduction is therefore bounded constructible. This is precisely the constructible subcategory defined in BM.6, with its normalized cohomology supplied by BQ.1–BQ.5. Alternatively, at an individual geometric point (C.14c) already gives the required coefficient calculation without a general constructibility theorem for arbitrary nearby cycles.

Finally rational coefficients here are obtained from the integral normalized construction by inverting \(\pi\). This is the exact localization of BW.6. Changing a stable lattice does not change the result: two lattices in the same finite-dimensional representation are commensurable, so an inclusion after multiplication by a power of \(\pi\) has quotient killed by a power of \(\pi\). Extension by zero and the exact \(O\)-linear functors in (C.14a) carry that torsion cone to a torsion cone, which becomes zero upon localization. The comparison is the one induced by the lattice maps and respects their common refinements. Finite extension of the coefficient field is compatible as well: its integer ring is finite free over \(O\), so extension of scalars commutes with the finite cones, products and adjunction maps above. The two uniformizer-adic filtrations are cofinal, since a power of the new uniformizer is a unit times \(\pi\). Thus the completions agree under this scalar extension. This supplies the normalized rational comparison used below, without claiming a new arbitrary nonproper rational-image comparison. \(\square\)

### Coefficient filtrations and the adic limit

**Proposition C.3.** Let \(L\) have a finite arithmetic-stable filtration on the punctured local surface whose grades extend lisse across the boundary. Denote the corresponding coefficient spaces on the strict local total scheme by \(A_m\). Its extension by zero has vanishing cycles concentrated in ordinary degree one, with a filtration whose grades are
\[
\begin{cases}
A_m(-1)\otimes\varepsilon(B),&\text{at a node},\\
A_m\otimes\varepsilon(B),&\text{at either boundary configuration}.
\end{cases}
\tag{C.16}
\]
This holds for rational-adic coefficients by the normalized finite-system and completed-fibre comparison of [Lemma C.2a](#normalized-nearby-cycles-and-the-completed-fibre).

**Proof.** A finite free lisse grade is constant on the strict local total scheme. Tensoring the preceding free finite-coefficient computations with its module gives the three formulas. Since extension by zero is exact, a filtration step gives a triangle of vanishing cycles. Inductively both end terms have cohomology only in degree one. Its long exact sequence is consequently the short exact sequence
\[
0\to\Phi^1(j_!F_{m-1}L)\to\Phi^1(j_!F_mL)
\to\Phi^1(j_!\operatorname{Gr}_m L)\to0.
\tag{C.17}
\]
This constructs an actual filtration with the claimed grades.

For the adic assertion choose a stable free lattice over the integers \(\mathcal O_E\) of a finite extension of \(\mathbb Q_\ell\). Intersect it with each rational filtration term. These intersections are saturated: if a nonzero integral multiple of a lattice vector lies in a rational subspace, the vector itself lies there. Their successive quotients are finite free over the discrete valuation ring. Reduction modulo \(\varpi^n\) therefore preserves exactness. The constant-grade calculations remain valid over \(\mathcal O_E/\varpi^n\), by extending the free finite complexes already computed.

Each grade cycle module is finite free over \(\mathcal O_E/\varpi^n\), and reduction is its usual surjective transition map. Induction in (C.17), lifting first in its quotient and then correcting in its submodule, proves surjectivity of the transitions for every filtration term. The surjective map at successive levels factors through reduction modulo the lower power of the uniformizer. Both sides are free of the same rank, determined by the constant-grade formula, so that reduction map is an isomorphism: after choosing bases its matrix is invertible modulo the maximal ideal, and its determinant is consequently a unit. Lift a basis successively through these maps. Nakayama's argument, or the same determinant test, makes the lifts bases; their compatible limit identifies the limit module with a finite free lattice of that rank. This proves actual coefficient reduction compatibility, not just equality of ranks. These systems satisfy Mittag-Leffler. Explicitly, the map \((a_n)\mapsto(a_n-r_n a_{n+1})\) on their products is surjective: given its target sequence, choose \(a_1\) and lift recursively through the surjections \(r_n\). The product description of the derived limit thus has no degree-one obstruction. Taking limits in (C.17) stays exact and creates no additional cohomological degree. Inverting \(\varpi\) and extending scalars gives (C.16). Formula (C.14c) of [Lemma C.2a](#normalized-nearby-cycles-and-the-completed-fibre) identifies this derived module limit with the completed geometric fibre of the actual normalized cone. Its comparisons preserve the filtration maps, inertia and arithmetic signs. Thus this calculation supplies the asserted normalized constructible adic vanishing cycles; it does not claim that arbitrary stalks commute with arbitrary inverse limits. \(\square\)

The requisite filtrations exist for tame-unipotent coefficients. For one or two boundary branches, the tame Kummer description gives commuting unipotent operators \(\exp(t_\ell N_i)\), with nilpotent \(N_i\). The prime-to-\(\ell\) part acts trivially: its compact image injects into a finite congruence quotient, whereas a finite unipotent group in characteristic zero is trivial. The filtration
\[
F_mA=\{v:N_{i_1}\cdots N_{i_m}v=0
\text{ for every sequence }i_1,\ldots,i_m\},\qquad F_0A=0,
\tag{C.18}
\]
is finite and exhaustive. Indeed a sufficiently long product of commuting nilpotents contains a vanishing power of one of them. Also \(N_iF_mA\subset F_{m-1}A\), so its grades have trivial inertia. Arithmetic conjugation rescales the \(N_i\) by cyclotomic units and may permute them; hence the filtration is stable. The tame covering and extension criterion then extends the grades across the boundary.

For weights, the filtration (C.18) alone does not assert purity of its grades. For the actual coefficient \(L\boxtimes L\) of Appendix A, use its independently established curve monodromy grading. At one boundary factor its grade of integral weight \(i\) is tensored with a pure weight-zero interior stalk. At a crossing the convolution of the two filtrations has grades of weights \(i+j\). The two curve inertia groups act separately, so these grades extend locally. Their arithmetic stability also survives an exchange of factors.

Every sign in (C.16) has finite image and root-of-unity eigenvalues, including the possibly wild tangency sign in characteristic two. Thus a pure local grade of weight \(w\) gives weight \(w+2\) at the interior node and weight \(w\) at either boundary point. The interior coefficient is already pure of weight zero. Consequently all exceptional \(\Phi_x^1\) in the surface-pencil argument have finite filtrations of integral pure weights. This obtains the local integrality needed in Appendix A without using the general direct-image weight estimate.

### Specialization with compact supports

Let \(\bar f:\widetilde S\to\mathbb P^1\) be the proper pencil compactification, let \(j:\widetilde V\hookrightarrow\widetilde S\), and put \(K=j_!\pi^*G\). The cohomology of \(K\) on a proper fibre is the compact-support cohomology of its open part. Hence \(R^r\bar f_*K=E_r\) with the notation of Appendix A.

At an exceptional parameter the vanishing cycles are supported at its unique exceptional point by Lemma B.4. Propositions C.1–C.3 place them in degree one. Proper comparison applied to the specialization triangle, followed by its cohomology sequence, therefore gives
\[
0\to(E_1)_{\bar t}\to(E_1)_{\bar\eta}\to\Phi_x^1(K)
\to(E_2)_{\bar t}\to(E_2)_{\bar\eta}\to0.
\tag{C.19}
\]
Degree-zero specialization is an isomorphism. The left zero in (C.19) uses \(\Phi_x^0=0\); the right zero uses \(\Phi_x^2=0\). This proves (A.11) with its full arithmetic action. The comparison is applied to the proper map \(\bar f\), so it requires no nearby-cycle base-change assertion for an arbitrary nonproper direct image.

## Appendix D. From curve cohomology to the general compact-support estimate

We now derive the compact-support assertion of Theorem 4.1 from the curve arguments. The proof must construct mixed sheaves on the target: unrelated weight bounds at its individual closed points would not by themselves give a finite mixed filtration. We first obtain pure proper-curve cohomology, then exhibit the boundary filtration in a family, and finally give a decreasing dimension induction.

The ordinary cohomological inputs are constructibility and finite amplitude of compact-support direct image, its geometric-stalk base change, localization, Leray, finite-cover trace, curve Poincaré duality with the natural forget-support pairing, and invariance under finite universal homeomorphisms. The geometric inputs are generic flatness and dimension, finite étale covers classified by fundamental groups, smooth proper curve models after finite purely inseparable extension, and spreading finitely presented geometric objects after shrinking an integral base. The relative tame boundary comparison is stated below and derived from the finite tame-covering input in Lemma D.1a. These inputs, together with the explicitly retained foundations of Appendices A–C, still require their recursive programme proofs. They are distinct from the weight conclusion to be deduced.

### Exact operation providers for D and E

Here is the coefficient and map convention for these two appendices. Schemes and morphisms have their standing separated finite-type scope over the finite ground field, and the coefficient prime is invertible on them. Work first over a finite extension \(E/\mathbb Q_\ell\), with valuation ring \(O\), uniformizer \(\pi\), and finite residue field. Constructible complexes, BX.7, equation (BX.20), identifies the rationalized complete category with the full subcategory of actual rational sheaf complexes having bounded constructible cohomology. Its comparisons (BX.21)–(BX.22) identify inverse image and ordinary direct image, and its final paragraphs identify compact support, internal Hom, duality, and their actual maps. Thus the operations below do not mean independently chosen finite-level isomorphisms. Nor do we need to identify this category with the bounded derived category of its heart.

BM.1–BM.6 constructs compact-support direct image by a proper–open factorization, proves independence with its refinement maps and associative composition, and supplies the actual geometric base-change arrow and finite cohomological bounds. In particular BM.5 includes geometric-point base changes, and BM.6 proves constructibility and boundedness without discarding the inverse-limit term. BV.1 supplies ordinary-image constructibility. These are ordinary operation results, not weight-preservation results.

BV.4–BV.7 supplies the smooth trace formula, closed supports, evaluation-defined singular biduality, and the dual exchanges. In particular BV.6 retains the actual double-evaluation map, and BV.7 constructs the exchanges by transposing the specified evaluation and counit. BW.5–BW.7 and BX.7 transport these maps to the rational category, preserving their positive Tate orientation. Smooth duality for a lisse sheaf therefore has its specified twist and shift, not merely matching stalk dimensions.

The two elementary passages used below can be made explicit in this category. For \(X\xrightarrow gW\xrightarrow hY\), filter \(Rg_!F\) by its ordinary cohomological truncations. There are only finitely many nonzero cohomology sheaves. Applying \(Rh_!\) to that finite tower produces the cohomology spectral sequence with terms \(R^ah_!(R^bg_!F)\) and the finite abutment filtration. BM.4 identifies its abutment with \(R^{a+b}(hg)_!F\) by its associative composition map; BM.6 supplies finite bounds. This is the Leray sequence used in (D.14), not a degeneration claim. The same truncation construction applies to ordinary direct image, using BV.1 and the ordinary composition adjunction.

For a finite map, AL.2 gives the finite-coefficient stalk sum and its actual base-change map. The completed and rational comparisons above preserve that finite sum and its exactness. For a finite étale cover the diagonal unit and sum trace are already maps of sheaves: on a trivializing étale cover they are the diagonal and sum of the same finite list of summands, and permutations of that list preserve both maps. They therefore descend, commute with all coefficient transitions, and rationalize. Their composite is the degree times the identity. This supplies the precise retraction in (D.10), without assuming the covering degree invertible in \(O\); it is inverted only in \(E\).

The curve-pair and radicial comparisons are supplied by [Proposition D.2a and Lemma D.2b](#the-geometric-changes-used-in-the-induction) below; Lemma E.2a supplies the higher-dimensional spreading in E. The operation providers above also retain their recursive finite-coefficient and algebraic prerequisites. The spreading deduction assumes those geometric and coefficient foundations. No weight conclusion from this lesson is used to construct them.

### Pure cohomology of an ordinary curve extension

Let \(j:U_0\hookrightarrow C_0\) be a dense open of a smooth proper curve over \(\mathbb F_q\), and let \(L_0\) be lisse and pure of integral weight \(a\). Here \(j_*\) always denotes the ordinary direct-image sheaf.

**Lemma D.1.** Under the ordinary curve foundations above,
\[
H^r(C,j_*L)\text{ is pure of weight }a+r.
\tag{D.1}
\]

**Proof.** Put \(B=i^*j_*L\) at the finite boundary \(i:C-U\hookrightarrow C\). The exact sequence \(0\to j_!L\to j_*L\to i_*B\to0\) gives a surjection
\[
H_c^1(U,L)\twoheadrightarrow H^1(C,j_*L).
\tag{D.2}
\]
The degree-one edge sequence for ordinary \(j_*\) inside \(Rj_*\) gives an injection \(H^1(C,j_*L)\hookrightarrow H^1(U,L)\). The composite with (D.2) is the forget-support map. Consequently
\[
H^1(C,j_*L)=
\operatorname{im}\bigl(H_c^1(U,L)\longrightarrow H^1(U,L)\bigr).
\tag{D.3}
\]
The optimal curve bound of Appendix A therefore gives the upper bound \(a+1\).

Write \(L'=L^\vee(1)\). Ordinary curve duality pairs \(H_c^1(U,L)\) perfectly with \(H^1(U,L')\), and \(H^1(U,L)\) perfectly with \(H_c^1(U,L')\). Functoriality of the trace pairing makes the two forget-support maps adjoint, up to the harmless degree-one sign. A map and its transpose have perfectly dual images: the kernel of the transpose is the annihilator of the image, and quotienting by that kernel proves nondegeneracy in both variables. Applying this linear-algebra fact to (D.3) gives a Frobenius-equivariant perfect pairing
\[
H^1(C,j_*L)\otimes H^1(C,j_*L')\longrightarrow\Lambda.
\tag{D.4}
\]
The coefficient \(L'\) has weight \(-a-2\). Its upper bound from (D.2) is \(-a-1\); taking the dual in (D.4) gives the lower bound \(a+1\). Both bounds hold for every embedding. The groups inherit algebraicity and mixedness from the curve theorem, so this proves purity in degree one without a general proper-pushforward weight theorem.

In degree zero, \(H^0(C,j_*L)=H^0(U,L)\) is the geometric invariant subspace of a lisse fibre. At a closed point of degree \(e\), the action on this subspace is the \(e\)-th power of arithmetic Frobenius on global sections. Its eigenvalues thus have weight \(a\). In degree two the finite boundary has no positive cohomology, so
\[
H^2(C,j_*L)=H_c^2(U,L)
=H^0(U,L^\vee)^\vee(-1),
\tag{D.5}
\]
which is pure of weight \(a+2\) by the degree-zero argument. Higher groups vanish by the ordinary curve cohomological bound. If geometric components are permuted, apply the same reasoning over their fields of definition. The characteristic polynomial on an orbit of length \(e\) is \(\det(1-T^eF^e)\); taking \(e\)-th roots preserves the normalized weights. \(\square\)

### Build the mixed filtration in a family

Let \(p:\overline X_0\to Y_0\) be a smooth proper family of curves, with \(Y_0\) smooth, and let \(i:D_0\hookrightarrow\overline X_0\) be a divisor finite étale over \(Y_0\). Write \(j:U_0\hookrightarrow\overline X_0\), \(f=pj\) and \(b=pi\). Let \(L_0\) be lisse, pure of integral weight \(a\), and tamely ramified along \(D_0\).

The relative tame comparison needed here has two parts. Ordinary \(j_*L_0\) must restrict on each geometric fibre to the ordinary extension \(j_{y*}L_y\). Further, the local monodromy filtration induced on \(B=i^*j_*L_0\) must be a finite filtration by constructible subsheaves whose geometric fibres are the induced monodromy filtrations on inertia invariants. Its formation must commute with those fibres. This is an assertion at the full adic scope, not merely a finite-presentation statement about the geometry. Shrinking a smooth integral target to obtain this comparison is allowed in the induction below; the removed locus will be treated separately. It is the ordinary compatibility used in Weil II, 1.8.6–1.8.8 and 3.3.1.

### Relative tame extension at full adic scope

**Lemma D.1a.** In the smooth relative-curve pair just specified, the relative tame comparison holds without a further shrinking of the base. Here the finite geometric input is the tame covering theorem proved in Lemma B.3a and Proposition B.3b: in a strictly local regular pair with smooth boundary parameter \(t\), every finite local system tame along that boundary becomes constant after adjoining \(t^{1/m}\), for an integer \(m\) prime to the residue characteristic. In a neighbourhood rather than a strict localization, this says that it extends as a finite locally constant sheaf on such a Kummer cover. Lemma B.3a and Proposition B.3b supply this finite covering theorem at the required smooth equal-characteristic scope, including arbitrary tame finite covers, the actual root normalization and descent to an étale neighbourhood. They reuse Constructible complexes, AP.1–AP.5 and AQ.1–AQ.2 for purity and gluing; the algebraic prerequisites of those purity and gluing statements are also required. The narrower Galois result AP.7 has the narrower Galois hypotheses stated there. The proof below derives the full adic and filtration comparison from that finite input; it does not assume that comparison as another theorem.

#### Coefficient categories used in the boundary comparison

We use the following proved coefficient constructions. Constructible complexes, N.3–N.5 identifies strict lisse systems with continuous finite modules, including all maps and their pullbacks, and constructs a stable free lattice for a finite-dimensional rational representation. In particular the compatible free modules in (D.5b) recover a finite free integral module with its action; the construction does not choose a single trivializing cover for all coefficient levels.

For precision on the sheaf side, write \(\nu:X_{\mathrm{pro\acute et}}\to X_{\mathrm{\acute et}}\), let \(C\) be derived \(\varpi\)-completion on constant \(\mathcal O\)-coefficients, and put \(a_c^*=Ca^*\). BP.1–BP.5 realizes a strict constructible system \((F_r)\) as the degree-zero complete sheaf \(\varprojlim_r\nu^*F_r\), recovers its ordinary quotients and every morphism, and identifies its lisse subcategory. The torsion correction is part of that proof: ordinary quotients are not substituted for derived reductions. BQ.3–BQ.5 identifies this category as the constructible heart and proves that completed inverse image is t-exact. Here a heart is simply the subcategory of complexes with cohomology only in degree zero. Its exactness statement includes the specified finite-coefficient comparison maps.

In this heart, the notation \(j_*\) means the ordinary direct-image sheaf \(H^0(Rj_*(-))\), not the entire derived image. To check that this is the same operation under the identifications just made, realize the lattice as \(L_{\mathcal O}^c=\varprojlim_r\nu^*L_r\). The open immersion \(j\) is separated and of finite type between finite-type schemes over the ground field, with \(\ell\) invertible. BV.1 therefore places \(Rj_*L_{\mathcal O}^c\) in the complete constructible category. BQ makes its degree-zero cohomology a heart object. Since derived direct image is the right derived functor of ordinary sheaf direct image, this degree-zero sheaf is exactly the ordinary \(j_*L_{\mathcal O}^c\). At a finite level, the punctured strictly local sections in the proof below are inertia-fixed vectors. The product-cone formula of BK.1 computes their derived inverse limit; all these section complexes have no negative cohomology, so its degree-zero cohomology is the inverse limit of their degree-zero sections. This supplies the degree-zero interpretation used in (D.5c), without discarding positive cohomology of \(Rj_*\).

For the coefficient extension \(E=\mathcal O[1/\varpi]\), BW.6–BW.7 proves exact rationalization and identifies the rational heart, including kernels, cokernels and its adjunction maps. BX.7, equations (BX.20)–(BX.22), identifies this heart and its ordinary direct image with actual constructible rational sheaves and their direct image. Thus the integral calculation followed by inverting \(\varpi\) computes the \(j_*L_0\) used here. This uses the finite-type scope just checked, not an unrestricted rational direct-image theorem.

Inverse images such as \(a_y^*\) and \(i^*\) in (D.5d) are the induced exact functors on this rational constructible heart. Integrally they are \(a_{y,c}^*\) and \(i_c^*\); BQ.5 identifies their cohomology and strict-system maps. The same proof applies to a geometric fibre: exact finite-coefficient pullback preserves the finite constructible partition, the image and quotient diagrams, and the common torsion exponent. It therefore retains the normalization and its maps. Rationally, (BX.21) identifies these functors with ringed inverse image. On lisse objects N.3–N.5 identifies them with restriction of the continuous representation. Consequently the kernel, image, intersection, sum and finite-group-idempotent calculations in (D.5e)–(D.5f) are sheaf calculations with the indicated fibre maps. Isomorphisms are detected by these constructible fibre functors, not by assuming that ordinary étale points detect every pro-étale sheaf. No assertion that arbitrary stalks commute with inverse limits, or that the bounded derived category of this heart is the whole constructible derived category, is required.

**Proof.** Put \(c=\operatorname{char}k\), keeping \(p\) for the structural morphism. Work over a finite coefficient extension \(E/\mathbb Q_\ell\), with valuation ring \(\mathcal O\) and uniformizer \(\varpi\), over which the lisse coefficient is defined. Choose a stable free lattice \(L_{\mathcal O}\) and put \(L_r=L_{\mathcal O}/\varpi^r\). All constructions below are compatible with finite extension of \(E\). The zero-rank case is immediate; write \(h\) for a positive rank on a connected coefficient component.

**Transverse coordinates and the finite construction.** Étale locally along \(D_0\), choose its equation \(t\) so that \((p,t):\overline X_0\to\mathbb A^1_{Y_0}\) is étale near the point in question. This is possible because the divisor is étale over the base: its conormal parameter gives a basis of the relative cotangent line. For \(m\) prime to the characteristic, form
\[
\begin{aligned}
X_m&=\overline X_0\times_{\mathbb A^1_{Y_0},\,t}\mathbb A^1_{Y_0},\\
t&=s^m.
\end{aligned}
\tag{D.5a}
\]
The map from \(X_m\) to the last affine line is étale. Thus \(X_m\to Y_0\) is smooth, including at \(s=0\), and the reduced inverse image of the boundary is a copy of \(D_0\). Its deck action is \(s\mapsto\zeta s\), with \(\zeta\in\mu_m\).

For each \(r\), the stated finite tame covering theorem supplies an \(m_r\) for which the pullback of \(L_r\) extends to a locally constant \(\mathcal O/\varpi^r\)-module on \(X_{m_r}\), locally along the boundary. Restrict this extension to \(s=0\). Denote the result by \(\Psi_r\); retain the deck action, rather than taking its invariants at this stage. Replacing \(m_r\) by a multiple gives the same boundary module: pull back the locally constant extension to the larger cover and use the identity on its boundary. Extensions and maps between them are unique once their restriction to the dense open is fixed. Indeed finite locally constant sheaves and their Hom sheaves are finite étale objects; over a normal connected scheme a section on a dense open extends uniquely when both objects already extend. Equivalently, the map from the fundamental group of the dense open onto that of the normal scheme is surjective. Apply this observation to the module operations and transition maps as well.

For each fixed level, uniqueness glues these constructions over the boundary chart. We do not intersect an infinite sequence of shrinking neighbourhoods. Taking common multiples for any two levels therefore gives compatible reductions
\[
\Psi_{r+1}/\varpi^r\Psi_{r+1}\simeq\Psi_r.
\tag{D.5b}
\]
Each module has rank \(h\). The compatible system defines a lisse free adic module \(\Psi_{\mathcal O}\), and \(\Psi=\Psi_{\mathcal O}\otimes_{\mathcal O}E\). It carries continuous tame inertia, the local procyclic group \(I=\prod_{\nu\ne c}\mathbb Z_\nu(1)\), where \(\nu\) ranges over primes, with its arithmetic action. No single Kummer degree is asserted to trivialize the entire adic coefficient. The degrees \(m_r\) may increase with \(r\).

This construction commutes with the geometric fibres of \(p\). To see the actual comparison, restrict (D.5a) and its locally constant extension to a fibre. The cover is still smooth, its boundary is still \(s=0\), and its open restriction is the pullback of \(L_r\). Uniqueness identifies this extension with the one used to construct the boundary module of \(L_{r,y}\). The maps agree after passage to a common covering degree, so they respect every transition in (D.5b) and the inertia action. On compatible free modules these give the adic comparison as well: it is the same free lattice and the same inertia operators in the two fibre functors, not a claim that an arbitrary sheaf stalk commutes with an arbitrary inverse limit.

**Ordinary extension means invariants of that lattice.** In the strictly local punctured pair the finite covering description identifies sections with inertia-fixed vectors. Consequently the ordinary extension at the boundary is computed by fixed vectors of the continuous lattice representation, followed by rationalization. For a geometric boundary fibre \(M_{\mathcal O}\) of \(\Psi_{\mathcal O}\), write \(M_r=M_{\mathcal O}/\varpi^rM_{\mathcal O}\) and \(M=M_{\mathcal O}\otimes_{\mathcal O}E\). The exact statements are
\[
\begin{aligned}
M_{\mathcal O}^{I}
  &=\varprojlim_r M_r^{I},\\
(M_{\mathcal O}^{I})\otimes_{\mathcal O}E
  &=M^{I}.
\end{aligned}
\tag{D.5c}
\]
The first equality follows in both directions by taking the compatible coordinates of a vector: every inertia element fixes the vector exactly when it fixes all its reductions. The second follows by multiplying any invariant rational vector by a power of \(\varpi\) that puts it in the lattice. Neither argument asserts exactness of taking inverse limits of an unrelated sequence. In degree zero, the inverse-limit extension is computed in this representation category by this left-exact fixed-vector construction; no negative cohomology can contribute a derived-limit term to degree zero.

In particular, we do **not** identify \(M_{\mathcal O}^{I}/\varpi^r\) with \((M_{\mathcal O}/\varpi^r)^I\). For example, the continuous action generated on \(\mathcal O^2\) by \(T=1+\varpi E_{12}\) has invariant lattice \(\mathcal O e_1\), whereas \(T\) is the identity modulo \(\varpi\). Reduction would create a second invariant vector. Formula (D.5c), not that false interchange, is used here.

The finite fibre comparison preserves the whole inertia representation before (D.5c) is applied. It therefore identifies the natural ordinary base-change map on boundary stalks; on the open part that map is already the identity. Geometric stalks detect isomorphisms, so for the fibre inclusions \(a_y:\overline X_y\to\overline X_0\) and \(u_y:U_y\to U_0\) we have
\[
\begin{aligned}
a_y^*j_*L_0&\simeq j_{y*}u_y^*L_0,\\
i^*j_*L_0&\simeq\Psi^I.
\end{aligned}
\tag{D.5d}
\]
The second description is local in the transverse coordinate. A change of that coordinate changes a chosen lift by tame inertia; it acts trivially on the invariant part. Thus these invariant objects and the displayed natural maps descend to the actual boundary sheaf \(B\).

**The filtration is a sheaf filtration, not just a list of stalks.** The local inertia argument in Appendix A gives quasi-unipotence at a finite-field closed point: Frobenius permutes the finitely many tame eigenvalues by a power map, hence each is a root of unity. This applies to the boundary representation just constructed. Since it is lisse with its Tate-inertia action, the resulting matrix identities propagate along a connected boundary neighbourhood. Locally there is an integer \(e\), prime to the characteristic, such that \(eI\) acts unipotently. A finite cover of the quasi-compact boundary suffices; take a common multiple of the finitely many such integers. This \(e\) only removes the finite semisimple part. It does not trivialize a nonzero unipotent adic action.

Its logarithm gives a morphism of lisse \(E\)-sheaves \(N:\Psi\to\Psi(-1)\), with \(N^h=0\). Locally the action on \(eI\) is \(\exp(t_\ell(\sigma)N)\). The logarithm and exponential are finite polynomials in a unipotent or nilpotent operator. Hence they commute with pullback, and the construction retains the arithmetic Tate twist. Put \(K=\ker N\). Since \(\exp(cN)-1=cN\,Q(N)\) for a polynomial \(Q\) with constant term one, \(Q(N)\) is invertible. Choosing an element with \(c\ne0\) shows that the invariants under \(eI\) are exactly \(K\). Thus \(I/eI\) acts on \(K\) through a finite group \(G\), and \(B=K^G\). Locally trivializing this finite group scheme, its invariants are the image of \(|G|^{-1}\sum_{g\in G}g\). This is an idempotent over \(E\), even when \(\ell\) divides \(|G|\).

An explicit, coordinate-independent formula for the monodromy filtration centred at zero uses \(K_i=\ker N^{i+1}\) and \(J_j=\operatorname{im}\bigl(N^j(j):\Psi(j)\to\Psi\bigr)\):
\[
M_k\Psi=
\sum_{\substack{i,j\ge0\\i-j=k}}
 (K_i\cap J_j).
\tag{D.5e}
\]
Only finitely many nonzero terms occur, since \(N^h=0\). All the maps in this formula have specified targets: the twist on the image puts it in \(\Psi\). To check the formula, take a Jordan chain \(v_0,\ldots,v_d\) with \(Nv_b=v_{b-1}\). Its displayed summand is the span of the first \(\min(i+1,d+1-j)\) vectors. Their sum includes exactly those \(v_b\) with \(2b-d\le k\). Thus the grades of the chain are \(-d,-d+2,\ldots,d\), and \(N^k\) identifies the grade \(k\) with grade \(-k\), with twist \(-k\). This verifies the monodromy filtration properties without choosing a global Jordan basis. Scaling a local generator of the Tate line does not change any kernel or image in (D.5e).

Kernels, images, intersections and finite sums in (D.5e) are lisse subsheaves: on a connected trivializing representation category they are invariant linear subspaces. Inverse image in this category is exact and therefore commutes with all those operations. It also commutes with the finite-group idempotent. It follows that
\[
M_kB=(K\cap M_k\Psi)^G
\tag{D.5f}
\]
is a finite filtration by lisse, hence constructible, subsheaves, with precisely the induced monodromy filtration in every geometric fibre. Coordinate changes preserve the inertia action, its logarithm with its Tate line, and its invariant subspaces. Therefore (D.5f) glues along with (D.5d); none of the choices changes the filtration on \(B\).

On a Jordan chain only \(v_0\) survives in \(K\), in grade \(-d\le0\). Taking \(G\)-invariants is exact over \(E\), so it does not introduce positive grades. The nonzero indices lie between \(-(h-1)\) and zero for the boundary invariants. This proves both required comparisons, including uniform finite length and arithmetic compatibility. Purity of these grades is the separate curve-monodromy result of Appendix A, not a consequence of this ordinary comparison alone. \(\square\)

The primary construction is Deligne, [*La conjecture de Weil : II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), 1.7.8–1.7.11, printed pages 172–174; its boundary-weight application is 1.8.6–1.8.8, pages 176–177. Lemma B.3a and Proposition B.3b now supply the finite covering argument using the existing purity and gluing providers. The coefficient-category constructions used here are supplied by N.3–N.5, BP–BQ, BV.1 and BW–BX through the precise identifications above. Their recursive foundations and the other ordinary curve-cohomology inputs at the start of Appendix D remain separate. No single finite root cover for an entire adic system is asserted. Formulae (D.5a)–(D.5f) supply the limit, fibre and filtration deductions needed here; source availability by itself is not their proof.

**Lemma D.2.** With the comparison proved in Lemma D.1a from the stated finite covering input, \(R^rf_!L_0\) is mixed of weights at most \(a+r\).

**Proof.** Put \(A_r=R^rp_*j_*L_0\). Proper base change and the stated fibre compatibility identify its closed geometric stalk with \(H^r(\overline X_y,j_{y*}L_y)\). Lemma D.1 makes \(A_r\) pointwise pure of weight \(a+r\). A constructible pointwise pure sheaf is a pure grade in the definition of mixedness; neither lissity nor Frobenius semisimplicity is needed here.

The monodromy proof in Appendix A shows that the grades of inertia invariants have weights \(a+k\) with \(k\le0\): on each nilpotent Jordan chain, only its bottom grade remains in the kernel, and finite inertia invariants are exact in characteristic zero. The relative comparison makes these into the actual grades of the filtration of \(B\). Their weights hold at every closed point of \(D_0\), so \(B\) is mixed of weights at most \(a\). The indices are uniformly finite, bounded by the ranks of the finitely many coefficient pieces.

Because \(b\) is finite, its direct image is exact and has no higher cohomology. At a point with residue-field degree \(e\) over its image, Frobenius acts on the induced stalk by a cyclic permutation whose \(e\)-th power is the original Frobenius. Thus it preserves normalized weights. Applying \(b_*\) to the boundary filtration proves that \(b_*B\) is mixed of weights at most \(a\).

Apply \(Rp_*\) to \(0\to j_!L_0\to j_*L_0\to i_*B\to0\). The complete low-degree sequence is
\[
0\to R^0f_!L_0\to A_0\to b_*B
\to R^1f_!L_0\to A_1\to0,
\tag{D.6}
\]
and \(R^rf_!L_0=A_r\) for \(r\ge2\). If \(Q=\operatorname{coker}(A_0\to b_*B)\), its quotient filtration has weights at most \(a\), and
\[
0\to Q\to R^1f_!L_0\to A_1\to0
\tag{D.7}
\]
constructs a finite mixed filtration with upper bound \(a+1\). Degree zero is a subobject of the pure weight-\(a\) sheaf \(A_0\); higher degrees use the displayed isomorphism. This proves mixedness of the sheaves themselves, in addition to their stalk bounds. \(\square\)

### Exact reductions that preserve the bound

For ordinary constructible sheaves, mixedness with an upper bound is closed under subobjects, quotients and extensions. To check a subobject, intersect it with the finite mixed filtration; every resulting grade embeds in the corresponding pure grade. Its stalk eigenvalues are a subset of that grade's eigenvalues, hence have the same weight. Quotients are treated by the quotient filtration. For an extension, concatenate the subobject's filtration with inverse images of the quotient's filtration. These constructions do not assume semisimple Frobenius.

Open extension by zero and closed direct image preserve pure grades: outside the supporting locally closed subspace their stalks are zero. If \(v:V\hookrightarrow Y\) has closed complement \(z:Z\hookrightarrow Y\), the ordinary exact sequence
\[
0\to v_!v^*H\to H\to z_*z^*H\to0
\tag{D.8}
\]
therefore glues mixedness and an upper bound from the two restrictions. Repeating this for a finite stratification supplies a global finite filtration.

For \(0\to A\to B\to C\to0\), the compact-support long exact sequence gives two useful rules. If the degree-\(r\) outputs of \(A,C\) both have upper bound \(n+r\), the degree-\(r\) output of \(B\) has that bound. If all outputs of \(B,C\) satisfy their indexed bounds, the relevant segment is
\[
R^{r-1}f_!C\to R^rf_!A\to R^rf_!B.
\tag{D.9}
\]
Its outer bounds are \(n+r-1\) and \(n+r\), so the same conclusion holds for \(A\). There is no symmetric quotient rule from knowing only \(A,B\): the next group \(R^{r+1}f_!A\) would have the weaker bound \(n+r+1\). We will use extension, source localization and direct summands, avoiding that inference.

A separated finite-type map with zero-dimensional geometric fibres has \(R^rf_!=0\) for \(r>0\), and \(f_!\) is exact: its geometric stalks are finite direct sums of the fibre stalks. The Frobenius induction calculation used for \(b\) shows that it preserves purity of a fixed weight and finite mixed filtrations. This includes nonproper zero-dimensional maps and nonreduced fibres, since nilpotents do not change the étale topos.

For a finite étale cover \(v:Z\to X\) of constant degree \(e>0\), the unit and trace satisfy
\[
L\longrightarrow v_*v^*L\longrightarrow L,
\qquad\text{composite}=e\,\mathrm{id}.
\tag{D.10}
\]
Indeed on a geometric stalk the first map is the diagonal and the second is the sum. Division by \(e\) is permitted in characteristic-zero coefficients, so this is a retraction. Applying \(R^rf_!\) preserves the retraction, and finite pushforward plus transitivity identifies its middle term with \(R^r(fv)_!v^*L\). Thus the original output is a direct summand of the covered output. A locally varying degree is handled on the finitely many connected components. Pullback preserves purity, because a residue-field extension raises Frobenius to a power and multiplies the residue degree by the same factor.

### The geometric changes used in the induction

We now connect the geometric steps of D.3 and E.1–E.3 to their exact providers. A homeomorphism of underlying spaces alone does not identify étale sheaves. The first comparison below uses the stronger algebraic hypotheses; the second retains the actual boundary and open immersion while spreading the curve.

**Proposition D.2a (finite radicial changes with their coefficient maps).** Let \(q:S'\to S\) be a finite, surjective, radicial morphism of finite-type finite-field schemes. Its pullback is an exact equivalence on ordinary constructible rational sheaves and on the full bounded constructible derived categories used here. It transports finite mixed filtrations, their weights, and the ordinary- and compact-support direct-image comparisons in a Cartesian square.

**Proof.** Pushforward, pullback and finite morphisms, Theorem 6.2 proves that the actual adjunction \(q^{-1}\dashv q_*\) on small étale sheaves is an equivalence. It covers integral surjective radicial maps, not only finite ones. Here its finite-case calculation is especially explicit: Theorem 4.1 identifies \((q_*F)_{\bar s}\) with the product over geometric lifts of \(\bar s\). Radiciality and surjectivity give exactly one lift. The adjunction unit and counit become identity maps of that stalk, so enough geometric points proves both are isomorphisms. This proves equivalence of sheaves, rather than inferring it from a bijection of spaces. Both functors are exact on module sheaves and preserve the constant coefficient ring.

Apply this equivalence to the entire diagram of \(O_n=O/\pi^n\)-module sheaves, not separately chosen isomorphism classes at each \(n\). Its functors, units and counits commute with every coefficient transition. Exact monoidal inverse image commutes with derived extension of coefficients; its inverse equivalence does too. Therefore the equivalence preserves the derived cartesian condition on the diagram and all its higher morphisms. It preserves the constructible restriction: finite locally closed partitions are transported by the universal homeomorphism, and local constancy and finite fibres are preserved by the equivalence of sheaf categories. Constructible complexes, BR.4 and BS.3 identify these diagram categories with the complete constructible categories, using their actual reduction and limit adjunctions. Their standard hearts agree with strict constructible systems. Thus the transported equivalence is t-exact, including integral torsion; ordinary quotient systems have not been substituted for derived reductions.

BW.7 rationalizes the equivalence, and BX.7 identifies its inverse image and direct image with the actual rational operations. This uses whole coefficient diagrams and does not assume that stalks commute with arbitrary inverse limits.

For clarity let \(f:X\to S\), let \(X'=X\times_SS'\), and write \(q_X:X'\to X\) and \(f':X'\to S'\). The same equivalence applies to \(q_X\). Composition of ordinary direct images and the unit for this equivalence give
\[
\begin{gathered}
Rf_*K\simeq Rf_*Rq_{X,*}q_X^*K\\
\simeq Rq_*Rf'_*q_X^*K.
\end{gathered}
\tag{D.10a}
\]
Applying the inverse equivalence \(q^*\) gives \(q^*Rf_*K\simeq Rf'_*q_X^*K\). It is the canonical base-change map: transpose it through the two adjunctions and one obtains the commuting inverse-image square followed by the same counit. Composition of these comparisons follows from the composite adjunction identities. This argument is specific to the two vertical equivalences; it does not assert arbitrary nonproper base change. For compact support use the actual comparison BM.5. Its finite reductions and coefficient maps are the comparisons just used, with the proper–open construction.

At corresponding closed points, the residue extension is finite purely inseparable between finite fields and hence is the identity: finite fields are perfect. The arithmetic Frobenius and its degree are therefore unchanged on the identified stalks. An exact equivalence transports subobjects, quotients and the full finite filtration, in both directions. It consequently preserves and detects pure grades, mixedness and the numerical weight bounds. This includes reduction maps, since the schemes here are Noetherian and their nilradicals are nilpotent. \(\square\)

**Lemma D.2b (spread the curve together with its étale boundary).** In the relative-dimension-one step of D.3, one may, after the indicated finite purely inseparable change of generic field and a shrinking of the integral target, work on a dense source open in a smooth proper curve over a smooth target, whose complementary divisor is finite étale over that target. The discarded source and target complements have smaller total source dimension. No descent of an infinite adic coefficient system is asserted.

**Proof.** Write \(K\) for the target function field and first pass to its perfection \(F\). Constructible complexes, AH.1 proves the universal homeomorphism of spaces under this purely inseparable extension, preserving components and density. The étale equivalence, when needed at this possibly infinite field extension, is instead Theorem 6.2 of the finite-morphisms lesson, or the explicit field-extension proof BE.4. These are distinct inputs.

The reduction of the generic curve over the perfect field has a dense smooth affine open. O.1 constructs its smooth proper completion by normalizing a projective closure and proves that its boundary is finite. Give that boundary its reduced structure. Its coordinate algebra is a finite product of finite extensions of \(F\); because \(F\) is perfect, these extensions are separable. Thus this particular finite boundary is étale, including the empty-boundary case.

Descend this whole finite diagram: the completed curve, its finite map to the fixed projective closure, the selected open, the inverse identification with the chosen source open, and the boundary closed immersion. O.2 descends the standard-smooth presentations and inverse Jacobian minors, with relative dimension one. AH.4 checks the Noetherian, finite-presentation and quasi-compact-open hypotheses of the finite-diagram descent proof, including equality of the complementary opens. To retain étaleness of the boundary, write each finite separable field factor as a tower of simple separable extensions. Keep its monic polynomials, the Bezout equations inverting their derivatives, the product idempotents, and the finitely many equations for the boundary algebra isomorphism and its inverse. All these coefficients and equations descend to one finite purely inseparable extension \(K'/K\). They make the descended boundary finite étale, not merely finite. This is the same explicit finite étale algebra construction used in O.4.

Spread over an affine integral target \(A\) with fraction field \(K\). The construction in O.3 chooses \(B\subset K'\), finite over a localization of \(A\), and one \(q=p^e\) with \(B^q\subset A\); its spectrum is finite, surjective and radicial over that open. The finite map to the fixed projective closure keeps the completed curve proper. Descend the smooth charts, open and closed immersions, complementary-open equality, finite boundary algebra and its étale presentations as above, now by clearing finitely many denominators in \(B\). The boundary remains finite étale after that shrinking.

Here is also the divisor assertion needed for the smooth pair. Étale locally on the base, the finite étale boundary splits into disjoint sections of the smooth relative curve. Near a point of one section, choose an étale relative coordinate \(t\), and replace it by \(t-s^*t\), where \(s\) is that section. The section lies in the zero fibre of this coordinate. That fibre is étale over the base, so the section is an open part of it; after shrinking the neighbourhood and excluding the other boundary sections, its zero fibre is exactly the selected section. The coordinate is a non-zero-divisor: it is pulled back from the indeterminate in a polynomial algebra along a flat étale map. Thus the boundary ideal is locally invertible and defines a relative effective Cartier divisor on these charts. This conclusion descends along the faithfully flat étale cover: finite presentation makes rank-one local freeness descend, and faithful flatness detects the kernel of the inclusion of the ideal. This proves the assertion for the whole boundary, with the empty boundary represented by the unit ideal.

The new integral finite-type target has a dense smooth locus over the perfect finite ground field. Choose a principal open of \(\operatorname{Spec}B\) inside it. Every required localization \(B_b\) can be made while retaining the finite map over an open of the original target: invert \(b^q\in A\), since \(b^{-1}=b^{q-1}/b^q\). Combine the finitely many such localizations. The final target is smooth and hence normal; its finite algebra is the normalization in \(K'\), since an element of \(K'\) integral over \(A\) is integral over \(B\) and normality puts it in \(B\).

The coefficient on the previously chosen finite étale cover is already defined. Pull it back and restrict it to this open; nothing in the preceding construction tries to spread its infinitely many coefficient levels from a generic fibre. Its pro-\(\ell\) image still kills every pro-\(p\) wild inertia group. The resulting smooth pair therefore meets exactly the hypotheses of D.1a and D.2. Finally finite radicial changes preserve the underlying dimension, and every discarded subset is a proper closed subset of an integral source or the inverse image of a proper closed subset of its dominant integral target. Its total dimension is strictly smaller. A discarded subset may contain a whole special fibre; no claim that all discarded fibres are finite is used. \(\square\)

The proper quasi-finite step in E.1–E.3 has its own exact provider: Constructible complexes, AU.6 proves that a proper map with finite fibres over a locally Noetherian target is finite. Its proof uses coherent-cohomology finiteness and completion, followed by an explicit affineness argument; the corresponding finiteness and completion hypotheses are required. All targets here are finite type over a field and hence Noetherian. The curve-pair construction and radicial comparisons are given above. Lemma E.2a below supplies the arbitrary-dimensional smooth spreading in E's general-source step. Its dimension, smoothness and normalization inputs have the hypotheses specified there.

### A dimension induction with a strict decrease

**Theorem D.3.** For every separated finite-type morphism of finite-field schemes \(f:X_0\to Y_0\), and every ordinary mixed constructible \(F_0\) of weights at most \(n\), the preceding curve results and explicitly stated ordinary foundations imply
\[
R^rf_!F_0\text{ is mixed of weights at most }n+r.
\tag{D.11}
\]

**Proof.** Induct on the dimension \(D\) of the source; the assertion is empty for the empty source. Assume it for all sources of dimension less than \(D\), for every target and every mixed input. Source localization separates dense opens of the finitely many maximal-dimensional irreducible components; their intersections and the remaining strata have smaller dimension. Reductions do not change étale sheaves. A finite closed immersion preserves the assertion, so each integral source can be viewed as dominant over the reduced closure of its image.

Reduce the input by its finite mixed filtration, using the extension rule, to a pure grade of weight \(a\le n\). Restrict it to a dense smooth source open where it is lisse; its closed complement has dimension less than \(D\) and is handled by induction and source localization. Likewise the inverse image of a proper closed subset of the integral target is a proper closed subset of this dominant integral source, hence has dimension less than \(D\). Compact-support base change and (D.8) permit shrinking the target. In particular we may make it smooth and remove fibre-dimension jumps. Notice the distinction: a discarded source subset can contain an entire special fibre. Its smaller total dimension, not an assertion that every discarded fibre is finite, justifies induction.

At this fixed source dimension first prove the cases with generic relative dimension zero or one. The zero-dimensional case follows after removing fibre-dimension jumps from the calculation preceding (D.10).

For the curve case choose a stable lattice for the lisse representation on the dense source. Such a lattice exists because its profinite image is compact: the integral span of the translates of any lattice is bounded and still a full lattice. Reduction modulo a sufficiently deep power of the coefficient uniformizer has finite image; its kernel is pro-\(\ell\), by the filtration of congruence subgroups with finite \(\ell\)-group quotients. Take the finite étale cover corresponding to this finite representation quotient. On it the coefficient image lies in that pro-\(\ell\) kernel. Every wild inertia group of a characteristic-\(p\) boundary trait is pro-\(p\); its continuous image in a pro-\(\ell\) group is trivial when \(p\ne\ell\). This kills wild ramification wherever a smooth boundary model is subsequently constructed. Formula (D.10) reduces the desired assertion to the covered coefficient; split its finitely many components if necessary.

Work on its generic curve over \(K=\mathbb F_q(Y_0)\). Over the perfection of \(K\), the reduced curve has a smooth dense open with smooth proper completion, and its finite boundary has separable residue fields. [Lemma D.2b](#the-geometric-changes-used-in-the-induction) supplies this curve model and the finite-presentation descent of its finite étale boundary after a finite purely inseparable extension \(K'/K\). Normalize a normal target open in \(K'\). After shrinking, this is a finite universal homeomorphism. Étale invariance and compact-support base change allow this replacement: they transport actual sheaf filtrations. At finite-field closed points the purely inseparable residue extension is trivial, so Frobenius weights are unchanged.

Spread the finite geometric data of the generic completion, open immersion and boundary over a dense target open. Shrink until the completion is smooth proper and its boundary is finite étale. The generic identification with a dense open of the covered source also spreads after shrinking; the omitted source has dimension less than \(D\). The coefficient is already defined on that source: restrict and pull it back along the identification. No claim that an arbitrary infinite adic system is finitely presented is needed. Its pro-\(\ell\) image makes the extended boundary ramification tame by the preceding inertia argument. Lemma D.1a supplies the relative tame comparison on this smooth pair, from its explicit finite covering input; no additional shrinking is needed for that step. That lemma proves (D.11) on the retained open. The lower-dimensional source and target complements, the universal-homeomorphism equivalence, and the trace retraction recover the entire relative-curve case. Each discarded complement is treated by the outer induction; no arbitrary relative-dimensional case at dimension \(D\) has been used.

Now let the generic relative dimension be \(d\ge2\). Choose \(d-1\) algebraically independent elements of the source function field over the target function field. On a dense source open they define a dominant map to \(\mathbb A_{Y_0}^{d-1}\). Generic flatness and fibre dimension give a nonempty target open \(W_0\) on which this map has pure relative dimension one. Its inverse image is dense; the discarded source again has dimension less than \(D\). On that retained source the original map factors as
\[
X'_0\xrightarrow{g}W_0\xrightarrow{h}Y_0.
\tag{D.12}
\]
These maps are separated. The projection \(h\) is separated, so the graph of \(g\) in \(X'_0\times_{Y_0}W_0\) is closed; the projection of that product to \(W_0\) is a base change of the separated original map. Their composite is \(g\). Crucially,
\[
\dim W_0=\dim Y_0+d-1=D-1.
\tag{D.13}
\]
The relative-curve case just proved, still allowing source dimension \(D\), makes \(R^bg_!F_0\) mixed of weights at most \(n+b\). Outer induction applies to \(h\), whose source has the smaller dimension in (D.13), and gives
\[
R^ah_!\bigl(R^bg_!F_0\bigr)
\text{ of weights at most }n+a+b.
\tag{D.14}
\]
These are the terms of compact-support Leray. Each surviving term in total degree \(r\) is a subquotient of one bounded by \(n+r\); the finite abutment filtration preserves mixedness and that bound. No degeneration assertion is required. Localization restores the discarded source and completes induction on \(D\). Finally reassemble the original finite coefficient filtration to obtain (D.11). \(\square\)

For a bounded complex whose ordinary cohomology sheaves have bounds \(w+b\), the ordinary-cohomology spectral sequence for \(Rf_!\) now gives upper bound \(w\) on the resulting complex, exactly as in (4.2). Ordinary inverse image preserves mixedness and weights by the residue-field calculation, and tensor product preserves mixedness by its finite tensor filtration and multiplication of stalk eigenvalues. The remaining operations require a further argument. Appendix E first proves mixedness for ordinary direct image without assuming dual mixedness, and then obtains duality, exceptional inverse image and derived internal Hom. A formal lower inequality expressed using a dual would not by itself establish that stability.

## Appendix E. Mixedness of the remaining operations

The compact-support theorem does not establish ordinary direct-image mixedness merely by writing a duality formula: that would already require mixedness of the dual. We first prove ordinary direct-image mixedness without that assumption. Duality is then obtained by stratification, and the other operations follow.

We work in the finite-field constructible characteristic-zero étale category of this lesson. In addition to Appendix D, the ordinary inputs are bounded constructibility and generic base change for ordinary direct image, relative smooth Poincaré duality, finite universal-homeomorphism invariance, finite étale descent, open–closed localization, and constructible Verdier biduality with its functorial exchanges. The geometric inputs include generic smoothness after reduction and finite purely inseparable base change, projective closure of affine schemes, and the dimension formula. Proposition D.2a supplies the radicial coefficient comparison; the paragraph after D.2b identifies AU.6 as the exact proper quasi-finite provider. Lemma E.2a supplies the arbitrary-dimensional smooth-spreading argument with its exact algebraic providers. The operation providers and coefficient identifications listed in Appendix D supply the ordinary constructibility, support, smooth-trace and biduality maps at this full adic scope. Their recursive inputs and the geometric statements remain hypotheses of this deduction. The first proof of Lemma E.2 below does not use generic base change. Proposition E.2b proves the smooth/lisse geometric-fibre comparison for the alternative relative-pairing proof. E.2m below supplies the ordinary constructible generic-base-change theorem; E.2n supplies the uniform completed comparison and its actual rational-sheaf identification. No assertion about preservation of weights by these operations is assumed.

### Mixedness can be detected after a finite map

The ordinary subquotient, extension and stratification arguments in Appendix D show that bounded mixed complexes are closed under triangles and ordinary truncations. Mixedness is also local on a finite Zariski open cover. Indeed, partition the union successively into each open's portion not already covered; these are locally closed pieces. Restrict the finite filtrations there and use extension by zero and open–closed gluing. The filtrations on overlapping opens need not coincide.

**Lemma E.1.** If \(b:T_0\to S_0\) is finite and \(b_*H\) is mixed, then the ordinary sheaf \(H\) is mixed. Consequently finite pushforward detects mixedness of bounded complexes.

**Proof.** For a finite étale map, \(H\) is a direct summand of \(b^*b_*H\). In the finite étale fibre product \(T_0\times_{S_0}T_0\), the diagonal is both open and closed. The projector onto that component gives the summand, or, on stalks, selects the summand at the given point from the finite fibre sum. Pullback preserves mixedness by the Frobenius-power calculation, so ordinary subquotient closure proves the assertion.

For a general finite map, stratify the reduced base into integral pieces and work first at a generic point. Its finite reduced source algebra is a product of finite field extensions. After a finite purely inseparable extension of the base field, the reductions of these algebras are separable. This can be seen over the perfection, then descended to a finite stage since the algebras and their separability conditions are finitely presented. Spread that finite radicial change over a normal base open. After shrinking, the reduced finite source is étale over the changed base. Finite base change and invariance of étale topoi under the radicial maps reduce to the first paragraph. At closed finite-field points those maps do not change residue fields, so the equivalence transports pure grades and finite mixed filtrations with their weights.

The omitted closed base has smaller dimension. Finite base change identifies the restricted pushforward there; induction proves mixedness on its inverse image. Open–closed gluing supplies a finite mixed filtration on all of \(H\). For a complex, finite pushforward is exact and commutes with ordinary cohomology, so apply the sheaf assertion to every nonzero cohomology sheaf. \(\square\)

### A smooth map over a dense base open

**Lemma E.2.** Let \(a:V_0\to S_0\) be smooth of pure relative dimension \(d\), with \(S_0\) integral, and let \(L_0\) be a pure lisse sheaf. On a dense open of \(S_0\), the complex \(Ra_*L_0\) is mixed.

#### A proof using the already constructed operations

**Proof of Lemma E.2 without generic base change.** We may shrink the integral finite-field base \(S_0\) to its nonempty smooth locus. Write \(s=\dim S_0\); then the smooth source \(V_0\) is smooth over the finite field of pure dimension \(s+d\). This uses only the geometric smooth-locus input already specified, and leaves the lemma's dense-open conclusion unchanged. If \(V_0\) is empty the result is immediate.

Set \(A=Ra_!L_0^\vee\). Appendix D makes \(A\) bounded mixed. For each of its finitely many nonzero cohomology sheaves choose a finite mixed filtration. Constructibility lets us shrink the integral base once more so that every term and every grade in this finite list is lisse: intersect their finitely many dense lisse opens. Formation of \(Ra_!\) commutes with this open restriction by BM.5; ordinary direct image commutes with open restriction by the slice adjunction. We replace \(S_0,V_0\) by these opens. No claim about ordinary direct image under a closed or arbitrary geometric-fibre base change is needed.

Use the rational operation comparisons just specified. Put \(D_TK=R\mathcal Hom(K,\omega_T)\), where \(\omega_T\) is the exceptional inverse image of the rational unit under \(T\to\operatorname{Spec}\mathbb F_q\). For a smooth \(T\) of dimension \(t\), BV.4 gives \(\omega_T=E_T(t)[2t]\). Finite lisse sheaves are dualizable; their evaluation identifies their double dual with themselves. BV.7, transported by BX.7, consequently gives
\[
\begin{gathered}
D_{S_0}A\\
\simeq Ra_*D_{V_0}(L_0^\vee),\\
D_{V_0}(L_0^\vee)\\
\simeq L_0(s+d)[2s+2d].
\end{gathered}
\tag{E.1a}
\]
These are the dual-exchange and smooth-orientation maps, so they retain the arithmetic action. Moving the shift and the Tate object through direct image is the projection comparison for an invertible rank-one coefficient object; equivalently it can be checked after trivializing that object and descended through its transition maps. Thus (E.1a), together with the smooth formula for \(\omega_{S_0}\), yields
\[
\begin{aligned}
Ra_*L_0&\simeq B(-d)[-2d],\\
B&=R\mathcal Hom(A,E_{S_0}).
\end{aligned}
\tag{E.1b}
\]
In particular the base-dimension twist and shift cancel. This is a statement about the actual derived image, before taking cohomology, not an identification inferred from a fibre calculation.

Here is the cohomology calculation in (E.1b). If \(H\) is finite lisse, then \(R\mathcal Hom(H,E_{S_0})=H^\vee\) in degree zero: locally \(H\) is finite free, where internal Hom is a finite direct sum of the identity functor and is exact, and these identifications glue by the dual transition maps. Apply this to the cohomology sheaves of \(A\), using its finite ordinary truncation tower. The resulting internal-Hom cohomology spectral sequence has only its degree-zero internal-Ext row. It gives the natural identification
\[
\begin{gathered}
\mathcal H^r(Ra_*L_0)\\
\simeq\bigl(\mathcal H^{\,2d-r}(A)\bigr)^\vee(-d).
\end{gathered}
\tag{E.1c}
\]
This also proves that the ordinary-image cohomology sheaves are lisse on the chosen open; their lissity was not an additional assumption. The finite-tower calculation does not assert a general equivalence with the derived category of the constructible heart.

For completeness let \(0=F_0\subset F_1\subset\cdots\subset F_m=H\) be one of the chosen lisse mixed filtrations of \(H=\mathcal H^{2d-r}(A)\). The filtration on \(H^\vee\) is explicitly
\[
\begin{gathered}
G_i=\ker(H^\vee\longrightarrow F_{m-i}^\vee),\\
G_i/G_{i-1}\\
\simeq(F_{m-i+1}/F_{m-i})^\vee.
\end{gathered}
\tag{E.1d}
\]
The first formula is for \(0\leq i\leq m\), and the second for \(1\leq i\leq m\). Restriction to a lisse subrepresentation is surjective on dual vector spaces, hence is an epimorphism of these lisse sheaves. This proves the displayed graded identification and exactness, without a semisimplicity assumption. Dualizing a pure lisse grade inverts its Frobenius eigenvalues and negates its weight; twisting by \((-d)\) adds \(2d\). Formula (E.1c) therefore supplies an actual finite mixed filtration for every \(R^ra_*L_0\). The inverse filtration works equally for zero sheaves, and only finitely many degrees occur by the ordinary-image bound. This proves the full assertion of Lemma E.2.

The only dual-mixedness fact used in this proof is the explicit dual filtration (E.1d) for lisse sheaves. We have not assumed Theorem E.4, general mixed stability of Verdier duality, or generic base change. The relative-pairing proof below uses the actual fibre comparison supplied by Proposition E.2b. \(\square\)

#### The actual fibre comparison for the relative-pairing proof

**Proposition E.2b (smooth source and lisse coefficients).** Let \(a:V\to S\) be a separated smooth morphism of pure relative dimension \(d\) between finite-type schemes over a finite field, with \(S\) integral. Let \(E\) be a finite extension of \(\mathbb Q_\ell\), where \(\ell\) is invertible on \(S\), and let \(L\) be a finite-rank lisse \(E\)-sheaf on \(V\). There is a dense open \(U\subset S\) such that every \(R^ra_*L|_U\) is lisse and, for every geometric point \(g:\bar s=\operatorname{Spec}\Omega\to U\), the canonical map
\[
\begin{gathered}
\beta_g:g^*Ra_*L\longrightarrow Ra_{\bar s,*}L_{\bar s},\\
(R^ra_*L)_{\bar s}\longrightarrow
H^r(V_{\bar s},L_{\bar s})
\end{gathered}
\tag{E.F1}
\]
is an isomorphism, in the derived category and on cohomology, respectively. Here the morphism and the sheaf on the right are the pullbacks to \(\bar s\), and on the left \(a\) has been restricted over \(U\). The algebraically closed field \(\Omega\) need not be finite over a residue field. No purity, mixedness, semisimplicity or smoothness of \(S\) is assumed. This proposition proves the comparison used in the following proof. It does not state generic base change for arbitrary morphisms and arbitrary constructible coefficients.

**Proof: relative duality before taking a fibre.** All operations below are the actual rational constructible operations identified in Constructible complexes, BX.7. Put \(A=Ra_!L^\vee\), \(B=Ra_*L\), and \(A^\vee=R\mathcal Hom_E(A,E_S)\). Bounded constructibility is supplied by BV.1 and BM.6 there. Applying the internal exceptional adjunction (BV.22) to \(K=L^\vee\) and \(G=E_S\), and using the smooth orientation (BV.15), gives the particular map
\[
\lambda:B\xrightarrow{\sim}A^\vee(-d)[-2d].
\tag{E.F2}
\]
Indeed \(a^!E_S=E_V(d)[2d]\), while
\(R\mathcal Hom_E(L^\vee,E_V)=L\): on a pro-étale trivialization this is finite-dimensional double evaluation, with its dual transition maps. Thus (BV.22) identifies \(B(d)[2d]\) with \(A^\vee\). Moving the invertible Tate line through ordinary direct image is its projection comparison. No dualizing complex for a smooth base is needed.

Specify the pairing that defines \(\lambda\). In the following display \(\otimes\) denotes derived tensor over the indicated coefficient sheaf, \(\varepsilon:a^*Ra_*L\to L\) is the ordinary adjunction counit, and the last arrow is the positive smooth trace with its twist and shift removed:
\[
\begin{aligned}
B\otimes A
&\longrightarrow Ra_!(a^*B\otimes L^\vee)\\
&\xrightarrow{Ra_!(\varepsilon\otimes1)}Ra_!(L\otimes L^\vee)\\
&\xrightarrow{Ra_!(\mathrm{ev})}Ra_!E_V
\xrightarrow{\mathrm{Tr}_a}E_S(-d)[-2d].
\end{aligned}
\tag{E.F3}
\]
The first arrow is the proper-support projection isomorphism. BV.7 proves that (BV.22) is obtained by transposing this evaluation through the specified exceptional counit; consequently (E.F2) is the transpose of (E.F3), not an arbitrary isomorphism between its source and target.

**Proof: a dense open and dual pullback.** Only finitely many cohomology sheaves of \(A\) occur. For each choose a dense open of the integral base on which it is lisse, and intersect these opens to obtain \(U\). Restriction of both images to this open is the usual slice restriction; for proper support it is also BM.5. On \(U\), every \(\mathcal H^q(A)\) is locally finite free in the pro-étale topology. The evaluation-defined map
\[
\kappa_g:g^*A^\vee\longrightarrow
R\mathcal Hom_E(g^*A,E_{\bar s})
\tag{E.F4}
\]
is an isomorphism. Here \(g^*\) is derived ringed inverse image, including the coefficient map, not an unmentioned identification of coefficient sheaves. For a shifted finite lisse sheaf, pull back its trivializing cover: both sides are the same finite dual module with the same transition maps, and (E.F4) is its identity comparison. Both sides are contravariantly exact in \(A\). Apply the finite ordinary truncation triangles of \(A\); induction through this finite tower proves the assertion for \(A\). This argument neither takes an infinite limit of duals nor assumes realization from the derived category of the constructible heart. The same tower, before pullback, gives
\[
\mathcal H^r(B)\simeq
\bigl(\mathcal H^{2d-r}(A)\bigr)^\vee(-d),
\tag{E.F5}
\]
so these sheaves are lisse. This follows because internal Hom from a finite lisse sheaf is exact locally; the finite internal-Ext spectral sequence has only its degree-zero row.

**Proof: identify the canonical map.** Write \(g_V:V_{\bar s}\to V\) for the other projection, and set
\(A_{\bar s}=Ra_{\bar s,!}L_{\bar s}^\vee\) and
\(B_{\bar s}=Ra_{\bar s,*}L_{\bar s}\). The compact-support comparison is
\[
\alpha_g:g^*A\xrightarrow{\sim}A_{\bar s}.
\tag{E.F6}
\]
BM.5 constructs this map for arbitrary base change, explicitly including bases not of finite type over the original field. Its proper compactification and quasi-compact open pull back to \(\bar s\). For rational coefficients the same map is obtained from that completed comparison by localization: BW.7 preserves the comparison, and BX.3 and BX.7 identify inverse image and proper support with their actual ringed functors. The local finite-complex inverse-image calculation and the quasi-compact-slice localization calculation used there apply also to \(g\). On the fibre, apply BV and BX over the algebraically closed field \(\Omega\), where \(V_{\bar s}\) is of finite type. This gives
\(\lambda_{\bar s}:B_{\bar s}\xrightarrow{\sim}A_{\bar s}^\vee(-d)[-2d]\).

Define the map on duals in the required direction by
\[
\begin{gathered}
\delta_g:g^*A^\vee\longrightarrow A_{\bar s}^\vee,\\
\delta_g=R\mathcal Hom_E(\alpha_g^{-1},E_{\bar s})\circ\kappa_g.
\end{gathered}
\tag{E.F7}
\]
It is an isomorphism. The inverse in this formula is essential: duality reverses the arrow \(\alpha_g\).

The ordinary comparison \(\beta_g\) is defined by the ordinary adjunction \(a_{\bar s}^*\dashv Ra_{\bar s,*}\). Its transpose is the map
\(a_{\bar s}^*g^*B=g_V^*a^*B\xrightarrow{g_V^*\varepsilon}L_{\bar s}\).
In particular, with \(\varepsilon_{\bar s}\) the fibre counit,
\[
\varepsilon_{\bar s}\circ a_{\bar s}^*\beta_g
=g_V^*\varepsilon.
\tag{E.F8}
\]
Both sides are maps \(a_{\bar s}^*g^*B\to L_{\bar s}\). Expand (E.F3) on the base and on the fibre. The projection comparisons commute with (E.F6), since they are induced by the same tensor adjunction and support maps. Their next arrows commute by (E.F8); evaluation commutes with pullback of a finite lisse dual. Finally the trace commutes with this base change. The latter is the coordinate-trace assertion of BJ.6: coordinate covers, the affine-space positive trace and the étale summation trace all pull back, including to geometric fields. BV.2–BV.4 construct the compatible coefficient-diagram counits from those traces; BW.7 and BX.7 preserve these maps. Thus this use requires no exceptional adjoint on an arbitrary scheme outside their field scope.

Consequently, if \(p\) and \(p_{\bar s}\) denote the two pairings (E.F3), then
\(p_{\bar s}\circ(\beta_g\otimes\alpha_g)=g^*p\), with the canonical tensor and Tate identifications. Transposing this equality, and using the definition (E.F4), proves the equality of actual morphisms
\[
\lambda_{\bar s}\circ\beta_g
=\delta_g(-d)[-2d]\circ g^*\lambda.
\tag{E.F9}
\]
The three maps other than \(\beta_g\) in this equality are isomorphisms. Therefore \(\beta_g\) itself is an isomorphism. Inverse image is exact on constructible rational sheaves (BQ and BX.3), so cohomology gives exactly the second map in (E.F1). The construction uses only canonical evaluation, counits and the fixed positive trace, and hence also retains any arithmetic action carried by the original sheaves. For the empty source all objects and maps are zero; for \(d=0\) the trace is the same étale summation trace. Unequal relative dimensions are treated on the finitely many open-and-closed relative-dimension pieces, not identified with one another. \(\square\)

E.2m and E.2n below supply the broader ordinary and adic/rational generic-base-change statements; E.2b remains an independent smooth/lisse proof rather than their substitute. It supplies the smooth/lisse instance, including the canonical geometric-fibre map, used in the relative-pairing argument below.

#### Recovering comparison on a finite residual locus

The general generic-base-change argument must eventually pass from a comparison on an open set to a comparison on the whole target. Here is the precise detection step. It does not require knowing in advance that the unknown direct-image complex is constructible. We first state it for ordinary étale sheaves of modules over a fixed commutative ring \(\Lambda\); an adic or rational application needs its own coefficient comparison.

**Lemma E.2c (finite residual detection).** Let \(b:Y\to S\) be a morphism of schemes, \(i:Z\hookrightarrow Y\) a closed immersion, and \(u:W=Y\setminus Z\hookrightarrow Y\) its open complement. Suppose \(q=b i:Z\to S\) is finite. For a morphism
\[
\alpha:M\longrightarrow N,\qquad
M,N\in D^+(Y_{\mathrm{\acute et}},\Lambda),
\tag{E.R1}
\]
assume that both \(u^*\alpha\) and \(Rb_*\alpha\) are isomorphisms. Then \(\alpha\) is an isomorphism. Neither constructibility of \(M,N\) nor properness of \(b\) is an additional hypothesis of this lemma.

**Proof: why the finite direct image detects a map.** Finite pushforward, Theorem 4.1 proves exactness and the natural geometric-stalk formula
\[
(q_*G)_{\bar s}=\prod_{\bar z\mid\bar s}G_{\bar z},
\qquad R^rq_*G=0\quad(r>0).
\tag{E.R2}
\]
The same formulas hold for \(\Lambda\)-modules: the restrictions defining them respect the coefficient action. The finite set indexes the geometric lifts with one fixed algebraically closed field, not chosen isomorphism classes of stalks. Every geometric point of \(Z\) is a lift of its image in \(S\). Consequently \(q_*G=0\) implies that every stalk of \(G\) is zero, so \(G=0\). Surjectivity of \(q\) is unnecessary. An empty fibre contributes the zero module and loses no point upstairs.

Exactness gives \(\mathcal H^r(Rq_*K)=q_*\mathcal H^r(K)\) for a bounded-below complex \(K\). Thus \(Rq_*K=0\) implies \(K=0\). Applying this conclusion to a cone shows that \(Rq_*\) reflects isomorphisms. This is a property of the finite morphism \(q\), not an assertion that an arbitrary proper direct image is conservative.

Put \(C=\operatorname{Cone}(\alpha)\). Inverse images and extension by zero for the open and closed immersions are exact. Localization, Proposition 5.2 therefore gives the natural triangle
\[
u_!u^*C\longrightarrow C\longrightarrow i_*i^*C
\longrightarrow (u_!u^*C)[1].
\tag{E.R3}
\]
It follows by applying the sheaf-level short exact sequence to a representative complex; exact functors preserve its quasi-isomorphisms. The first assumption gives \(u^*C=0\), hence the displayed map identifies \(C\) with \(i_*i^*C\). The second assumption gives \(Rb_*C=0\).

There is a natural composition identification \(Rb_*i_*K=Rq_*K\). Indeed \(i_*\) is exact by (E.R2), and it sends injectives to injectives because its left adjoint \(i^*\) is exact. An injective resolution of \(K\) thus computes both sides, using the actual equality \(b_*i_*=q_*\). With \(K=i^*C\) we obtain
\[
0=Rb_*C=Rq_*i^*C.
\tag{E.R4}
\]
Finite detection gives \(i^*C=0\), and (E.R3) then gives \(C=0\). Thus the original morphism \(\alpha\), rather than some independently chosen comparison of its endpoints, is invertible. \(\square\)

**Corollary E.2d (the actual base-change map).** Let \(f:X\to Y\), let \(a=b f:X\to S\), and let \(F\in D^+(X_{\mathrm{\acute et}},\Lambda)\). For any \(g:T\to S\), form the Cartesian diagrams, with the indicated projections:
\[
\begin{gathered}
X_T\xrightarrow{f_T}Y_T\xrightarrow{b_T}T,\qquad
X\xrightarrow{f}Y\xrightarrow{b}S,\\
h_X:X_T\to X,\quad h_Y:Y_T\to Y,\quad a_T=b_Tf_T,\\
Z_T=Z\times_ST,\quad W_T=W\times_ST.
\end{gathered}
\tag{E.R5}
\]
Retain the hypothesis that \(Z\to S\) is finite. Assume the following three particular maps are isomorphisms:

1. The restriction to \(W_T\) of \(\beta_{f,g}:h_Y^*Rf_*F\to Rf_{T*}h_X^*F\).
2. The canonical comparison \(\gamma_{b,g}:g^*Rb_*Rf_*F\to Rb_{T*}h_Y^*Rf_*F\).
3. The canonical comparison \(\beta_{a,g}:g^*Ra_*F\to Ra_{T*}h_X^*F\).

Then \(\beta_{f,g}\) itself is an isomorphism everywhere on \(Y_T\).

**Proof: compatibility under composition.** Use the composition identifications for ordinary derived direct images. They are computed by injective resolutions because direct image preserves injectives, its inverse-image left adjoint being exact. The comparison maps satisfy
\[
\beta_{a,g}
= Rb_{T*}(\beta_{f,g})\circ\gamma_{b,g}.
\tag{E.R6}
\]
Here both sides go from \(g^*Rb_*Rf_*F\) to \(Rb_{T*}Rf_{T*}h_X^*F\). To verify equality rather than merely compare these objects, recall the defining adjunction transpose of ordinary base change. For \(f\), this is
\[
f_T^*h_Y^*Rf_*F
=h_X^*f^*Rf_*F
\xrightarrow{h_X^*\varepsilon_f}h_X^*F,
\tag{E.R7}
\]
where \(\varepsilon_f:f^*Rf_*\to\mathrm{id}\) is the derived counit. Transpose the right side of (E.R6) successively across \(b_T^*\dashv Rb_{T*}\) and \(f_T^*\dashv Rf_{T*}\). Naturality of the latter comparison and the defining transpose of \(\gamma_{b,g}\) give, in order, the pullback of \(f^*\varepsilon_b\) followed by the pullback of \(\varepsilon_f\). Their composite is the counit of the composed adjunction \(a^*=f^*b^*\dashv Rb_*Rf_*=Ra_*\). This is precisely the transpose defining \(\beta_{a,g}\); uniqueness of adjunction transposes proves (E.R6).

Assumptions 2 and 3 now imply that \(Rb_{T*}(\beta_{f,g})\) is invertible. The closed complement \(Z_T\to T\) is finite, since it is a base change of \(q\). Apply Lemma E.2c over \(T\) to the morphism \(\beta_{f,g}\), using assumption 1 on \(W_T\). This proves the corollary. \(\square\)

If \(b\) is proper, a proper-base-change theorem at the stated coefficient and boundedness scope can supply assumption 2. It must apply to the actual object \(Rf_*F\); invoking a version restricted to constructible inputs before establishing constructibility of that object would be circular. The corollary deliberately records that comparison as an input, rather than concealing such an assumption.

For the qcqs, bounded-below ordinary torsion case, [Proposition E.2g below](#proper-comparison-before-constructibility) now supplies this precise input from the existing BE.14 proof, with torsion preservation and coefficient compatibility checked explicitly. It does not require the still-unknown constructibility of \(Rf_*F\).

This is the finite-residual step in the proof strategy of Deligne, [*SGA 4½*, Théorèmes de finitude, §2.6](https://publications.ias.edu/node/378), printed p.240. The deduction also requires a good open locus, a finite complement, a whole-space comparison and bounded constructibility at the required coefficients. In particular E.2b's geometric-fibre statement is not automatically an arbitrary-base-change statement; the corollary uses it only at that scope. Nor does it pass from torsion levels to adic or rational coefficients by an infinite intersection of dense opens. These lemmas complete the detection argument, not the general generic-base-change theorem.

[Lemma E.2h and Proposition E.2i below](#constructibility-and-bounds-on-the-finite-residual-locus) give the separate constructibility-and-boundedness detection step over Noetherian schemes. They retain explicit whole-space finiteness inputs; invertibility of a comparison map alone does not establish constructibility.

#### Constructing the finite residual locus by coordinates

Lemma E.2c requires a complement that is **finite over the base**, not merely a finite set in a generic fibre. We now supply the geometric construction used in the dimension induction. The geometry works over an integral Noetherian base; no smoothness, reducedness, or equality of component dimensions is imposed on the schemes over that base.

**Lemma E.2e (coordinate opens and their finite complement).** Let \(S\) be integral Noetherian with generic field \(K\), and let \(Y\to S\) be of finite type. On a finite affine cover of \(Y\), after replacing \(S\) by an affine neighbourhood of its generic point, choose closed embeddings
\[
Y_a\hookrightarrow\mathbf A^{r_a}_S,\qquad
p_{ai}:Y_a\longrightarrow\mathbf A^1_S.
\tag{E.G1}
\]
Suppose that for every chosen coordinate there is a dense open \(V_{ai}\subset\mathbf A^1_S\). Set
\[
W=\bigcup_{a,i}p_{ai}^{-1}(V_{ai})\subset Y.
\tag{E.G2}
\]
After one further nonempty open restriction of \(S\), the reduced closed complement \(Z=(Y\setminus W)_{\mathrm{red}}\) is finite over \(S\). A chart needing no generators may be embedded using the extra coordinate zero, so every \(r_a\) can be taken positive.

**Proof on an affine chart.** Write \(S=\operatorname{Spec}A\). Since \(A\) is a domain, \(\mathbf A^1_S\) is integral and every dense open \(V_{ai}\) contains its generic point. Give its closed complement an ideal \(I_{ai}\subset A[T]\). This ideal contains a nonzero polynomial. Choose one and invert its nonzero leading coefficient in \(A\); after scaling, it is a monic polynomial
\[
P_{ai}(T)=T^{d_{ai}}+\sum_{e<d_{ai}}c_{ai,e}T^e\in I_{ai}A_s[T].
\tag{E.G3}
\]
There are finitely many coordinates and charts, so the same nonzero \(s\in A\) works for all of them. If the polynomial has degree zero, its scaled value is one and that closed complement is empty. Otherwise the quotient \(A_s[T]/I_{ai}A_s[T]\) is generated as an \(A_s\)-module by the powers \(1,T,\ldots,T^{d_{ai}-1}\): division by a monic polynomial uses no further denominators.

For a fixed chart, the complement of its union of coordinate opens has the underlying closed set of
\[
C_a=Y_{a,s}\mathbin{\times}_{\mathbf A^{r_a}_{A_s}}
\prod_i\operatorname{Spec}(A_s[T_i]/I_{ai}A_s[T_i]).
\tag{E.G4}
\]
The product is over \(\operatorname{Spec}A_s\). Its algebra is generated as a module by the monomials \(\prod_iT_i^{e_i}\), with \(0\le e_i<d_{ai}\). The embedding of \(Y_a\) makes \(C_a\) a closed subscheme of this finite scheme. Quotienting a finite module is finite, so \(C_a\to\operatorname{Spec}A_s\) is finite, including all its nilpotents. If one factor is empty, \(C_a\) is empty.

**Passage from the charts to \(Y\).** The open \(W\) in (E.G2) may also contain points supplied by another chart. Thus \(Z\cap Y_{a,s}\) is a reduced closed subscheme of \(C_a\), not necessarily all of \(C_a\). To check the scheme inclusion, every equation of \(C_a\) vanishes at every point of this reduced scheme, hence vanishes in its coordinate sheaf. Each \(Z\cap Y_{a,s}\) is therefore finite over the restricted base.

Finiteness is not, in general, a property that one may glue from opens of the source. Instead inspect the generic fibre. The finitely many opens \((Z\cap Y_{a,s})_K\) are finite \(K\)-schemes. Hence \(Z_K\) has finitely many points, all closed, with finite-dimensional local \(K\)-algebras. Each singleton is open: it is the complement of finitely many closed points. Its scheme structure is an open-and-closed component of one of those finite affine charts, so it is affine and finite over \(K\). Their finite disjoint union is affine and finite. This proves that \(Z_K\to\operatorname{Spec}K\) is finite.

Now apply Limits of schemes, Theorem 4.2 to the inverse system \(\operatorname{Spec}A_{st}\), \(0\ne t\in A\), whose limit is \(\operatorname{Spec}K\). The model \(Z\) is of finite presentation: it is a closed subscheme of a finite-type scheme over a Noetherian base. The transition maps are affine, and the models are quasi-compact and quasi-separated. These are exactly the theorem's hypotheses. Its proof first descends affineness by Lemma 2.3 and then descends a finite multiplication table of module generators. It consequently makes the actual morphism \(Z_{A_{st}}\to\operatorname{Spec}A_{st}\) finite for one nonzero \(t\). This supplies the required common shrinking; it is not an appeal to generic dimension alone. \(\square\)

The shrinking is necessary. For \(A=k[s]\), the closed subscheme \(V(sT-1)\subset\mathbf A^1_A\) has algebra \(A[1/s]\). Over \(D(s)\) it has the monic equation \(T-1/s=0\), but it is not finite over \(A\). Otherwise \(1/s\) would satisfy a monic equation; multiplying that equation by the appropriate power of \(s\) would give \(1\in(s)\), a contradiction. The empty fibre at \(s=0\) does not repair that failure.

**Corollary E.2f (the lower-dimensional induction supplies the opens).** Fix \(n\ge1\), a dense open immersion \(j:X\hookrightarrow Y\) of finite-type \(S\)-schemes, and a constructible torsion \(\Lambda\)-sheaf \(F\), with its annihilating integer invertible on \(S\). Assume \(\dim X_K\le n\). Use the same coefficient hypotheses throughout the following induction assumption: for every integral Noetherian base and every such dense open immersion with generic source dimension at most \(n-1\), there is a dense base open over which all ordinary higher direct images are constructible, vanish outside a finite range, and commute with **every** base change. This assumption is the lower-dimensional theorem, not its geometric-fibre variant.

Then, after shrinking \(S\), there is an open \(W\subset Y\) with finite closed complement over \(S\), such that the conclusions just listed hold for \(Rj_*F\) on \(W\). For each \(g:T\to S\), this includes the restriction of the actual canonical map
\[
h_Y^*Rj_*F\longrightarrow Rj_{T*}h_X^*F
\tag{E.G5}
\]
to \(W_T=W\times_ST\), where \(h_X:X_T\to X\) and \(h_Y:Y_T\to Y\) are the projections. It does not yet assert that (E.G5) is invertible on the finite complement.

**Proof: the dimension decrease for each coordinate.** On a chart in (E.G1), write \(X_a=X\cap Y_a\). The generic point of the new base \(\mathbf A^1_S\) has field \(K(T)\). For an irreducible component of \((X_a)_K\), with function field \(L\), there are two cases. If the coordinate \(p_{ai}\) is algebraic over \(K\) in \(L\), some nonzero polynomial in \(K[T]\) becomes zero, so this component has empty fibre over \(K(T)\). If it is transcendental, then
\[
\operatorname{trdeg}_{K(T)}L=\operatorname{trdeg}_K L-1\le n-1.
\tag{E.G6}
\]
The equality follows by adjoining the coordinate to a transcendence basis and applying exchange. The dimension/transcendence-degree calculation is the monic-normalization proof in Constructible complexes, K.1 and M.1; its algebraic part applies over arbitrary fields. It identifies the dimension of the nonempty generic component with the left side of (E.G6). Nilpotents do not change prime chains. Taking the maximum over the finitely many surviving components proves the bound without assuming equal dimensions. An empty generic source is harmless.

Here “algebraic” must not be replaced by “a scalar in \(K\)”. For example, over \(\mathbf Q\), the coordinate \(x\) on \(\operatorname{Spec}\mathbf Q[x,y]/(x^2-2)\) is algebraic but not rational constant. Its generic fibre over the \(x\)-line is empty, since \(T^2-2\) is inverted in \(\mathbf Q(T)\). The projection to the \(y\)-line instead has a zero-dimensional generic fibre. Both fall within the two cases above.

The restriction \(X_a\hookrightarrow Y_a\), now viewed over \(\mathbf A^1_S\) through \(p_{ai}\), is still an open immersion between finite-type schemes. Its open image is dense; localization to a generic fibre retains the generic points of the components that survive. The lower-dimensional induction assumption supplies a dense open \(V_{ai}\) of that base. Lemma E.2e then makes the complement of the union (E.G2) finite after a common shrinking.

**Proof: why this gives the required comparison on \(W\).** Restriction of ordinary derived direct image to an open of its target is the direct image for the restricted morphism. At sheaf level the two functors have the same sections on every etale open. At derived level the target-open restriction preserves injectives, since its left adjoint is the exact extension by zero; the corresponding source-open restriction does too. Thus an injective resolution proves the identity, and the counits identify the canonical comparisons, not merely their endpoints.

For an arbitrary \(T\to S\), apply the induction conclusion over \(V_{ai}\) to the base change
\[
V_{ai}\times_ST\longrightarrow V_{ai}.
\tag{E.G7}
\]
The resulting Cartesian source and target are exactly the original ones restricted to \(p_{ai}^{-1}(V_{ai})\times_ST\). Consequently its comparison is the restriction of (E.G5), by the just-described counit identity. Those opens cover \(W_T\). A morphism of sheaf complexes is an isomorphism if it is so on this cover, because the cohomology sheaves of its cone then vanish on every open in the cover. Constructibility is also local on a finite open cover: intersect the finitely many strata and opens to form one finite locally closed stratification. Taking the maximum of the finitely many cohomological bounds supplies a common finite bound on \(W\). This proves the stated conclusions. \(\square\)

This expands the coordinate reduction in Deligne, [*SGA 4½*, Théorèmes de finitude, Lemma 2.4](https://publications.ias.edu/node/378), printed pp.239–240. In the general generic-base-change proof, E.2f supplies the good-open input of E.2d, and E.2e supplies its finite complement. The lower-dimensional induction hypothesis, the whole-space comparison, constructibility across that complement, and the coefficient passage are the subsequent steps of the deduction. These results complete the geometric reduction, not the general theorem; geometric-fibre comparison alone does not establish arbitrary base change.

#### Proper comparison before constructibility

The finite-residual argument must apply proper base change to the actual direct image, not to a constructible replacement whose existence is still to be proved. The needed ordinary-coefficient statement follows from the earlier proof with no constructibility hypothesis.

**Proposition E.2g (the proper comparison input).** Let \(f:X\to Y\) be quasi-compact and quasi-separated, let \(b:Y\to S\) be proper, and fix a commutative coefficient ring \(\Lambda\). Let \(F\in D^+(X_{\mathrm{\acute et}},\Lambda)\), and assume that the underlying abelian sheaf of each \(\mathcal H^r(F)\) is torsion. Then \(Rf_*F\) is bounded below and has torsion underlying cohomology sheaves. For every morphism \(g:T\to S\), the canonical map in assumption 2 of Corollary E.2d is an isomorphism:
\[
\gamma_{b,g}:g^*Rb_*Rf_*F
\xrightarrow{\sim}Rb_{T*}h_Y^*Rf_*F.
\tag{E.P1}
\]
Neither constructibility of \(Rf_*F\), a finite upper cohomological bound, nor a common annihilator of all its cohomology sheaves is assumed. The proposition concerns ordinary sheaf complexes; it asserts no adic or rational comparison.

**Proof: comparing coefficients without assuming that forgetting preserves injectives.** The argument in Constructible complexes, BB.3 is stated for \(\mathbb F_\ell\), but its acyclicity argument works for the present \(\Lambda\). Here are the required details. On a qcqs scheme, take the finite-family hypercovers used in BA.5. The augmented complex of free \(\Lambda\)-module sheaves is exact: the local finite-support filling contracts a cycle by the identity \(\partial c+c\partial=1\), with coefficients in \(\Lambda\). This uses the explicit filling, not a claim that tensoring an arbitrary exact integral complex preserves exactness. Applying \(\operatorname{Hom}_\Lambda(-,J)\), for a module-injective sheaf \(J\), therefore gives an exact augmented cochain complex. Its terms are the products of the section groups of \(J\) on the hypercover objects. The hypercover computation in BA.5 consequently gives
\[
H^q(U,J)=0\qquad(q>0)
\tag{E.P2}
\]
for abelian-sheaf cohomology on a qcqs scheme \(U\).

Restriction to an étale object preserves module injectives. Indeed, its extension-by-zero left adjoint has stalks equal to direct sums over geometric lifts; these sums are exact, and geometric stalks detect exactness. This is the slice argument in AB.3, with the coefficient actions retained. If \(v:V\to W\) is qcqs and \(U\to W\) is affine étale, then \(V_U\) is qcqs. Applying (E.P2) after restriction, and the sheafification formula (AB.8), shows that a module-injective sheaf on \(V\) is acyclic for the underlying abelian direct image by \(v\). Thus a bounded-below module-injective resolution computes both derived direct images. The acyclic-resolution comparison is the identity in degree zero and commutes with restriction, connecting maps and coefficient endomorphisms. In particular it preserves the counits defining base change. We have not asserted that the underlying abelian sheaf of a module injective is injective.

**Proof: torsion survives a qcqs direct image.** First let \(G\) be a torsion abelian sheaf on \(X\), and put \(G_m=\ker(m!:G\to G)\) for \(m\geq1\). On every geometric stalk, every element of finite order belongs to some \(G_m\), so \(G=\varinjlim_m G_m\). For affine étale \(U\to Y\), the scheme \(X_U\) is qcqs. The fixed-scheme filtered-coefficient consequence of BA.5 gives continuity of every \(H^q(X_U,-)\). Using (AB.8) and exact sheafification yields
\[
R^qf_*G\simeq\varinjlim_m R^qf_*G_m
\qquad(q\geq0).
\tag{E.P3}
\]
Multiplication by \(m!\) is the zero morphism of \(G_m\), and additive derived functors carry it to the zero morphism of \(R^qf_*G_m\). Each term on the right is therefore killed by \(m!\). Filtered colimits have the corresponding colimits as their geometric stalks; each element there comes from a torsion term. This proves torsion, without claiming one integer annihilates the colimit.

Now let \(K\) be the underlying bounded-below complex of \(F\). For a complex whose cohomology lies in a finite interval, the truncation triangles with quotients \(\mathcal H^r(K)[-r]\) and their long cohomology sequences show that all cohomology sheaves of \(Rf_*K\) are torsion. The reason is that torsion abelian groups are closed under subquotients and extensions: if an element maps to one killed by \(n\), its multiple by \(n\) lies in the kernel and is killed by some \(m\), so the original element is killed by \(mn\).

For the general bounded-below case, fix any integer \(d\). The complex \(\tau_{\leq d}K\) has cohomology in a finite interval (or is zero), while \(\tau_{\geq d+1}K\) admits a bounded-below injective resolution beginning in degree \(d+1\). Applying direct image leaves that resolution zero in lower degrees. The truncation triangle consequently identifies
\[
\mathcal H^q(Rf_*\tau_{\leq d}K)
\simeq\mathcal H^q(Rf_*K)
\qquad(q\leq d).
\tag{E.P4}
\]
The finite-interval argument proves torsion on the left. Since \(d\) is arbitrary, it proves torsion in every degree on the right. The same resolution argument preserves the original lower bound. The coefficient comparison already proved transfers this conclusion to \(Rf_*F\).

**Proof: applying the exact earlier proper theorem.** Constructible complexes, BE.7, equation (BE.14) proves proper base change for every bounded-below complex with torsion abelian cohomology, without constructibility and for arbitrary changes of base. Apply it to \(b\) and to the actual underlying complex of \(Rf_*F\), whose hypotheses have just been checked. Proper morphisms, their base changes, and \(f_T\) are qcqs, so the coefficient comparison applies to all direct images involved. Exact inverse images commute with forgetting the coefficient action. The comparison is natural in coefficient endomorphisms and hence is \(\Lambda\)-linear. Both (BE.14) and (E.P1) are defined by the pulled-back derived counit; the resolution identifications preserve this counit. They identify the particular map \(\gamma_{b,g}\), rather than providing an unrelated isomorphism between its endpoints. An isomorphism after forgetting \(\Lambda\) is an isomorphism of \(\Lambda\)-module complexes, since the forgetful functor is exact and conservative. This proves (E.P1). \(\square\)

**Application and boundaries.** In the finite-type Noetherian situation of E.2f, the open immersion \(j\) is qcqs. Its stated torsion coefficients satisfy E.2g. Whenever the target morphism \(b\) is proper, assumption 2 of E.2d is therefore supplied for \(Rj_*F\), before proving its constructibility. This does not impose torsion or qcqs hypotheses on the more general conditional statement E.2d: outside the scope just proved, its comparison remains an explicit input. It also does not prove assumption 3, the lower-dimensional induction theorem, bounded constructibility across the finite complement, or the adic/rational passage. No shrinking of the base is needed for E.2g itself, and this step imposes no invertibility condition on the torsion primes.

Quasi-compactness cannot simply be dropped from the torsion-preservation argument. Over an algebraically closed field \(k\), take \(X=\coprod_{m\geq1}\operatorname{Spec}k\to\operatorname{Spec}k\) and the sheaf with value \(\mathbf Z/2^m\mathbf Z\) on its \(m\)-th component. It is torsion at every stalk, but its direct image has section group \(\prod_{m\geq1}\mathbf Z/2^m\mathbf Z\). The element with every component equal to \(1\) has infinite order. This example explains the qcqs continuity hypothesis; it is not a counterexample to the proper theorem.

#### Constructibility and bounds on the finite residual locus

Finite pushforward does more than detect a zero complex. The additional constructibility argument uses the Noetherian quotient theorem, not an assumption that the unknown sheaf is already constructible.

**Lemma E.2h (finite pushforward reflects bounded constructibility).** Let \(q:Z\to S\) be finite, with \(S\) Noetherian, and let \(\Lambda\) be a commutative Noetherian ring. Use the module convention: constructible means finitely generated locally constant on a finite locally closed partition. For an arbitrary \(\Lambda\)-module sheaf \(G\) on \(Z\),
\[
G\text{ is constructible}\quad\Longleftrightarrow\quad
q_*G\text{ is constructible}.
\tag{E.C1}
\]
For \(L\in D^+(Z_{\mathrm{\acute et}},\Lambda)\), this gives
\[
L\in D^b_c(Z,\Lambda)\quad\Longleftrightarrow\quad
Rq_*L\in D^b_c(S,\Lambda).
\tag{E.C2}
\]
Moreover, for each degree \(r\), \(\mathcal H^r(L)=0\) if and only if \(\mathcal H^r(Rq_*L)=0\). Thus the same cohomological interval works on both sides. Surjectivity of \(q\) is not required. The finite-stalk torsion-abelian convention satisfies the corresponding assertions; for finite \(\Lambda\) the two conventions coincide.

**Proof.** The finite scheme \(Z\) is Noetherian, and \(q\) is of finite presentation: on a Noetherian affine base its finite algebra has a finite list of algebra generators and a finitely generated relation ideal. The forward direction of (E.C1) is therefore Constructible sheaves and extension by zero, Theorem 6.1. Its proof uses finite-algebra splitting and Noetherian induction, independently of a later higher-direct-image constructibility theorem.

For the converse, pullback permanence in the same lesson, Proposition 3.2 makes \(q^*q_*G\) constructible. The adjunction counit
\[
q^*q_*G\longrightarrow G
\tag{E.C3}
\]
is surjective. Indeed, at a geometric point \(\bar z\) with image \(\bar s\), the canonical finite-stalk formula (E.R2) identifies it with the projection from the product over all lifts of \(\bar s\) to the factor \(G_{\bar z}\). That projection is surjective; for an actual point \(\bar z\), the indexing set is not empty. Geometric stalks detect epimorphisms. Proposition 7.1 of that lesson proves that every quotient of a constructible module sheaf on a Noetherian scheme is constructible, even if its kernel has not yet been shown constructible. Applying this exact result to (E.C3) proves the converse. Merely knowing that maps *between* constructible sheaves have constructible cokernels would not justify this step.

By Finite pushforward, Theorem 4.1, \(q_*\) is exact. It is also conservative: a nonzero stalk upstairs occurs in the product at its image, regardless of whether \(q\) covers the rest of \(S\). Hence
\[
\mathcal H^r(Rq_*L)=q_*\mathcal H^r(L),\qquad
q_*\mathcal H^r(L)=0\ \Longleftrightarrow\ \mathcal H^r(L)=0.
\tag{E.C4}
\]
The sheaf result in every degree and this exact preservation and reflection of vanishing prove (E.C2) and the interval assertion. For finitely many nonzero constructible cohomology sheaves, their finitely many partitions have a common finite refinement. No initially unknown upper bound has been assumed. For finite-stalk abelian sheaves, apply the same quotient and pullback results in their abelian version; a common annihilator exists on each finite constructible partition. \(\square\)

**Proposition E.2i (the residual constructibility criterion).** Let \(b:Y\to S\) be a morphism of Noetherian schemes, let \(i:Z\hookrightarrow Y\) be closed, let \(u:W=Y\setminus Z\hookrightarrow Y\), and suppose \(q=bi\) is finite. With \(\Lambda\) as in E.2h and \(K\in D^+(Y_{\mathrm{\acute et}},\Lambda)\), suppose the following three objects are bounded constructible:
\[
C=u^*K,\qquad A=Rb_*u_!C,\qquad B=Rb_*K.
\tag{E.C5}
\]
Then \(K\) is bounded constructible. This statement does not assume that the initially unknown restriction \(i^*K\) is constructible or bounded above, and does not claim that proper direct image alone is conservative.

**Proof with explicit degree bounds.** The localization triangle is
\[
u_!C\longrightarrow K\longrightarrow i_*i^*K
\longrightarrow(u_!C)[1].
\tag{E.C6}
\]
Apply \(Rb_*\). Exactness of \(i_*\) and preservation of injectives, established in E.2c, identify its third image with \(Rq_*i^*K\). Thus we obtain
\[
A\longrightarrow B\longrightarrow Rq_*i^*K\longrightarrow A[1].
\tag{E.C7}
\]
The long exact cohomology sequence makes each cohomology sheaf of the third term an extension of a cokernel by a kernel of maps between the constructible cohomology sheaves of \(A\) and \(B\). Proposition 3.2 of the constructible-sheaf lesson proves the required kernel, cokernel and extension permanence over \(\Lambda\). If their cohomology is supported in intervals \([a_0,a_1]\) and \([b_0,b_1]\), respectively, the same sequence gives the interval
\[
[z_0,z_1]=
[\min(b_0,a_0-1),\ \max(b_1,a_1-1)]
\tag{E.C8}
\]
for \(Rq_*i^*K\). Here the minus one comes from \(A[1]\); it must not be changed to a plus one. Empty cohomology is allowed within any of these bounds.

Lemma E.2h now makes \(i^*K\) constructible with the same interval. Since \(Y\) is Noetherian, the open immersion \(u\) is quasi-compact and of finite presentation; \(i\) is a finite morphism of finite presentation. Theorem 6.1 therefore makes \(u_!C\) and \(i_*i^*K\) bounded constructible. Apply the constructible cohomology argument once more to (E.C6). If \(C\) is supported in \([c_0,c_1]\), it gives
\[
K\in D^{[\min(c_0,z_0),\ \max(c_1,z_1)]}(Y,\Lambda)
\quad\text{with constructible cohomology}.
\tag{E.C9}
\]
This proves the assertion, including a finite upper bound rather than only degreewise constructibility. \(\square\)

**Where the proper-support input is already available.** Suppose \(b\) is proper between separated finite-type schemes over a field \(k\), and \(\Lambda\) is finite and killed by a power of a prime \(\ell\) invertible in \(k\). For bounded constructible \(C\) on \(W\), properness and composition of proper supports give
\[
Rb_*u_!C=Rb_!u_!C=R(bu)_!C.
\tag{E.C10}
\]
Constructible complexes, Proposition 3.2 proves that the last object is bounded constructible at precisely this field and coefficient scope. If the fibres of \(bu\) have dimension at most \(d\), it lies in \([c_0,c_1+2d]\), giving a particular interval for \(A\) in (E.C8). This invocation uses proper-support finiteness, whose proof precedes the ordinary-image argument, not constructibility of the unknown \(K\). At a more general Noetherian parameter base or different coefficient range, the corresponding proper-support finiteness theorem must be supplied at that scope; the field theorem is not silently enlarged.

**Position in the generic-base-change proof.** For \(K=Rj_*F\), E.2f supplies bounded constructibility on the good open, under its stated lower-dimensional induction hypothesis. E.2i shows exactly how that conclusion and the two whole-space finiteness inputs in (E.C5) recover bounded constructibility on the finite complement. Those inputs must be proved for \(Rb_*Rj_*F=R(bj)_*F\) and \(Rb_*u_!u^*Rj_*F\) in the chosen parameter-base and coefficient setting. The criterion does not prove them by naming them. Separately, E.2d and E.2g handle the comparison map once the whole-space comparison in E.2d assumption 3 is established. Keeping these steps separate avoids replacing finiteness by base change, or mistaking geometric-fibre comparison for arbitrary-base comparison. E.2m below assembles the lower-dimensional induction and the whole-space finiteness/comparison at the full ordinary left-Noetherian torsion-coefficient scope. E.2n below supplies the uniform adic/rational passage using one first reduction.

#### The existing field-scope whole-space finiteness inputs

**Corollary E.2j (reuse the proved ordinary-image theorem).** Let \(k\) be a field, let \(\ell\) be invertible in \(k\), and let \(\Lambda\) be a finite commutative ring killed by a power of \(\ell\). Suppose \(X,Y,S\) are separated finite-type \(k\)-schemes, \(j:X\hookrightarrow Y\) is open, \(b:Y\to S\) is a morphism, and \(F\in D^b_c(X,\Lambda)\). Then both
\[
K=Rj_*F\in D^b_c(Y,\Lambda),\qquad
B=Rb_*K=R(bj)_*F\in D^b_c(S,\Lambda).
\tag{E.W1}
\]
No smoothness of the schemes, perfection of \(k\), or freeness of the finite coefficient modules is required. If \(b\) is proper, the good-open proper-support term in E.2i is also bounded constructible at this scope. These field-scope finiteness statements do not require the broader generic-base-change conclusions of E.2m and E.2n.

**Proof and exact provider.** Constructible complexes, Appendix M, Theorem M.4 proves ordinary-image bounded constructibility for every separated finite-type morphism over a field. Its initial coefficient convention explicitly includes finite rings of order invertible in the field, not only free modules over \(\mathbf Z/\ell^m\). Apply it to \(j\) and \(bj\). Both are separated and of finite type: the schemes are Noetherian and separated of finite type over \(k\), an open immersion here is quasi-compact, and graphs give the stated relative separation and finite-type properties. Composition of ordinary derived direct images identifies the actual \(Rb_*Rj_*F\) with \(R(bj)_*F\); it follows from the exact inverse-image adjunction and preservation of injectives, as used in E.2c.

The proof order in M matters. M.1 gives a finite cohomological bound and field descent first. M.2 constructs finite-support quotients without assuming the unknown sheaf constructible. M.3 recovers constructibility from finite global cohomology on a proper scheme. M.4 uses those results in its dimension induction, establishes the smooth-open case before applying induction to the constructible cone, and invokes compact-support finiteness and smooth duality for the global term. It does not assume generic base change over an arbitrary parameter scheme. The corollary uses these results together with their exact geometric and coefficient prerequisites.

The bound in M.1 is also usable here. On each member \(S_t\) of a finite affine cover of \(S\), cover \((bj)^{-1}(S_t)\) by \(r_t\) affine opens of dimension at most \(D_t\). Ignore empty inverse images. Set \(m=\max_t(D_t+r_t-1)\), or \(m=0\) if \(X\) is empty. Affine intersections and the finite Cech-to-derived-image sequence give \(R^q(bj)_*=0\) for \(q>m\). Consequently, if \(F\) is supported in cohomological degrees \([f_0,f_1]\), then
\[
B\in D^{[f_0,f_1+m]}(S,\Lambda).
\tag{E.W2}
\]
The finite cohomology tower of \(F\) gives this bound from the sheaf bound; no finite Galois cohomological dimension of \(k\) is assumed.

For the last assertion, in the notation of E.2i, restriction of the already constructible \(K\) makes \(C=u^*K\) bounded constructible. Properness of \(b\) gives \(A=Rb_*u_!C=R(bu)_!C\), and Proposition 3.2 proves its bounded constructibility, with exactly the field and finite invertible-primary coefficient hypotheses stated above. M.4 already proves constructibility of \(K\) itself in this field case; E.2i is useful for the more general residual argument, not needed to prove the same field case twice. \(\square\)

**Finiteness is not arbitrary-base comparison.** Even at the preceding field scope, a bounded constructible ordinary image need not commute with a specified closed-fibre base change. Take \(j:\mathbf G_{m,k}\hookrightarrow\mathbf A^1_k\), with \(k\) algebraically closed, and the constant sheaf \(\mathbf Z/\ell\). At a geometric origin, the punctured strict-local trait is the spectrum of a field and is connected. Thus the stalk of \(j_*(\mathbf Z/\ell)\) there is \(\mathbf Z/\ell\). The source of the base-changed open immersion is empty, so its direct image is zero. The degree-zero comparison is therefore
\[
\mathbf Z/\ell\longrightarrow0,
\tag{E.W3}
\]
not an isomorphism. The constant-section calculation follows from connectedness of the punctured trait; no higher cohomology computation is needed. Removing the origin gives a dense open on which this example's comparison does hold, so it does not contradict a generic theorem after shrinking.

E.2j resolves field-scope finite-coefficient finiteness, not the whole-space arbitrary-base comparison in E.2d assumption 3. For a general Noetherian parameter base, the compact-support and smooth finite-coefficient inputs are supplied by E.2k below; E.2m below assembles the remaining ordinary-image reductions at the original left-Noetherian coefficient scope. E.2n supplies the distinct uniform adic/rational comparison; M.4 is not silently promoted to that scope.

#### General-base proper supports and the smooth whole-space input

**Proposition E.2k (existing general-base providers and their comparison).** There are two distinct inputs.

1. Let \(b:Y\to S\) be proper of finite presentation between quasi-compact, quasi-separated schemes, let \(u:W\hookrightarrow Y\) be a quasi-compact open immersion, and let \(\Lambda\) be a commutative Noetherian torsion ring. If \(C\in D^b_c(W,\Lambda)\), then the proper-support term \(A=Rb_*u_!C\) of E.2i is bounded constructible. If \(C\) has degrees \([c_0,c_1]\) and the fibres of \(bu\) have dimension at most \(e\), then
\[
A=R(bu)_!C\in D^{[c_0,c_1+2e]}_c(S,\Lambda).
\tag{E.WS1}
\]
Its compact-support base-change map is an isomorphism for every base change. In the residual comparison, E.2g supplies the proper ordinary-image comparison as well. No assumption that the unknown \(K\) is already constructible is used: the input is precisely constructibility of its known restriction \(C=u^*K\).

2. Let \(S\) be Noetherian, let \(h:X\to S\) be separated smooth of finite presentation and pure relative dimension \(d\), and let \(\Lambda=\mathbf Z/n\), where \(n>1\) is invertible on \(S\). Let \(F\) be a finite locally constant \(\Lambda\)-module sheaf, not necessarily free. There is a dense open \(V\subset S\) such that every \(R^ih_*F|_V\) is finite locally constant, vanishes outside \(0\leq i\leq2d\), and commutes with every base change \(g:T\to V\) through the canonical ordinary-image map. Thus, for \(h=bj\) in this smooth/lisse case, E.2d assumption 3 is available after one shrinking of the parameter base. This assertion concerns arbitrary \(T\to V\), not just geometric fibres.

**Proof of the proper-support assertion.** The composite \(bu\) is separated of finite presentation. The quasi-compact open immersion has finite presentation, and properness identifies \(Rb_*\) with \(Rb_!\). Composition gives the equality in (E.WS1). Compact supports, Theorem 12.3 supplies constructibility on a general quasi-compact, quasi-separated base; Theorem 12.1 gives the stated interval. A uniform finite bound on fibre dimension exists for a finite-presentation morphism over a quasi-compact base, by finite affine presentations. The compact-support comparison is the one constructed in Section 9, with its composition compatibility. These providers do not have a field-only restriction. Over a general Noetherian ring, constructibility means finitely generated module stalks; it does not assert finite underlying sets.

Theorem 12.3 gives its affine-factorization, finite-cover and finite-truncation proof explicitly. Its geometric prerequisite is the [AI Integrated Stacks affine-line constructibility proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-constructible-shriek-rel-dim-1), with the constant and locally constant curve reductions linked there. The corresponding native source is [more-etale.tex, revision 565b10e987aba5969b21145a0833f42d69f96790](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-etale.tex), labels `lemma-constructible-shriek-rel-dim-1`, `lemma-loc-constant-shriek-rel-dim-1`, `lemma-constant-shriek-rel-dim-1`, and the two proper-smooth-curve lemmas. The compact-support deduction requires the curve results at the hypotheses of those lemmas.

**Finite-module duality, including nonfree fibres.** Write \(D_ZE=R\mathcal Hom_Z(E,\Lambda)\). The ring \(\Lambda\) is injective as a module over itself. Indeed, every ideal is \((a)\) for a divisor \(a\mid n\). The image \(x\) of \(a\) under an ideal homomorphism must satisfy \((n/a)x=0\); in \(\mathbf Z/n\) this says \(x=ay\). Multiplication by \(y\) extends the homomorphism, proving injectivity by the ideal criterion. For a finite module, decomposition into cyclic groups of orders dividing \(n\) shows that evaluation into its double dual is an isomorphism: the dual of \(\mathbf Z/r\) is the ideal generated by \(n/r\), of order \(r\), and characters separate its elements.

These facts apply internally to a finite locally constant sheaf. On an étale cover trivializing it, sheafify a resolution by finite free \(\Lambda\)-modules. Such a resolution exists degree by degree since \(\Lambda\) is Noetherian; it need not be bounded. Internal Hom from each finite free term is exact, and the resulting Ext sheaves are the constant sheaves associated to module Ext. Injectivity of \(\Lambda\) makes the positive Ext groups vanish. This establishes both exact duality and bidual evaluation locally and hence globally. In particular, for a bounded complex \(Q\) with finite locally constant cohomology,
\[
H^r(D_ZQ)=\mathcal Hom_Z(H^{-r}(Q),\Lambda).
\tag{E.WS2}
\]
Use its finite cohomology tower to obtain this formula; do not assert that nonfree modules have finite projective dimension. For any scheme map \(g:Z'\to Z\), the canonical map \(g^*D_ZQ\to D_{Z'}g^*Q\) is an isomorphism: the same local finite-module calculation identifies its cohomology map with pullback of ordinary duals. This proves the assertion without treating every constructible complex as perfect.

**Proof of the smooth assertion.** Put \(F^\vee=\mathcal Hom_X(F,\Lambda)\) and \(Q=Rh_!F^\vee\). The preceding proper-support providers, applied directly to \(h\), give \(Q\in D^{[0,2d]}_c(S,\Lambda)\). Choose a dense open \(V\) on which all its finitely many cohomology sheaves are locally constant. Such a common open exists by their finite constructible stratifications: take a neighbourhood of each generic point in its stratum, exclude intersections with the other irreducible components, and take the union of these finitely many opens. Nonreduced structure does not change local constancy on the étale site. Only finitely many degrees are involved, so this is not an infinite intersection of dense opens.

Relative smooth duality, Theorem 9.1 gives \(Rh^!\Lambda=\Lambda(d)[2d]\) over the parameter base. Its internal adjunction, (8.4), applied to \(F^\vee\), then gives
\[
Rh_*F\simeq D_SQ(-d)[-2d].
\tag{E.WS3}
\]
Here bidual evaluation identifies the internal Hom on \(X\); the invertible twist can be pulled through ordinary direct image, as checked on an étale cover trivializing it. The companion constructs the trace and the smooth formula on general bases, not merely varieties over a field. Its Sections 3–6 use bounded derived trace systems and constructible compact supports before Section 9; the general compact-support input is not deduced from the smooth duality being proved.

Restrict (E.WS3) to \(V\), and apply (E.WS2). This gives
\[
R^ih_*F|_V\simeq
\mathcal Hom_V\bigl(H^{2d-i}(Q)|_V,\Lambda\bigr)(-d).
\tag{E.WS4}
\]
It proves both local constancy and the asserted vanishing range, including nonfree coefficient fibres.

It remains to identify the map, rather than only the isomorphism classes. For \(g:T\to V\), write \(h_T:X_T\to T\) and \(F_T=g_X^*F\). Compact base change identifies \(g^*(Q|_V)\) with \(Rh_{T,!}F_T^\vee\). Pullback commutes with the dual of \(Q|_V\) by (E.WS2). Compose these comparisons with (E.WS3) for \(h_T\); the resulting isomorphism is
\[
g^*(Rh_*F|_V)\longrightarrow Rh_{T,*}F_T.
\tag{E.WS5}
\]
To verify it is the canonical ordinary-image comparison, recall that (8.4) is evaluation followed by the trace counit. Pulling that pairing to \(T\), then using compact base change, gives the evaluation-and-trace pairing for \(h_T\): evaluation commutes with inverse image, and the trace and its composition identities commute with base change by the companion's Section 2 and Theorem 9.1. Transposing the same pairing therefore gives the map induced by the pulled ordinary adjunction counit, which defines the canonical comparison. Equivalently, after composing with the two duality isomorphisms, both maps are the canonical pullback-of-internal-Hom map followed by the inverse dual of compact base change. Thus (E.WS5) is that map and is invertible. When \(T\) is not quasi-compact or quasi-separated, make this verification on affine opens of \(T\); their base-changed smooth morphisms retain finite presentation, and the comparisons glue by their counit definition. \(\square\)

**Coefficient scope.** Part 1 gives the proper-support input for Noetherian coefficients. Part 2 supplies the smooth finite locally constant \(\mathbf Z/n\)-coefficient whole-space comparison after shrinking. The finiteness exposition in SGA \(4\frac12\), Theorem 1.9 and proof Sections 2.1–2.2, treats the broader Noetherian-coefficient reduction; Part 2 treats only the finite-coefficient stage. E.2m below supplies the ordered lower-dimensional and cone arguments for general constructible ordinary coefficients; E.2l below supplies the general Noetherian-coefficient smooth reduction, its finite-monodromy argument and a uniform degree bound. Adic/rational passage still requires its own uniform justification. The general adic/rational comparison is the subject of E.2n; it uses uniform coefficient maps on one dense open.

#### Smooth generic comparison with Noetherian coefficients

**Proposition E.2l (the full ordinary-coefficient smooth stage).** Let \(S\) be Noetherian, let \(h:X\to S\) be smooth of finite type, and let \(A\) be a unital left-Noetherian ring killed by an integer \(n>0\) invertible on \(S\). Let \(F\) be a locally constant sheaf of finitely generated left \(A\)-modules on \(X_{\mathrm{\acute et}}\). Choose an upper bound \(d\) for the relative dimensions of \(h\). There is a dense open \(V\subset S\) such that
\[
\begin{gathered}
R^ih_*F|_V\text{ is locally constant,}\\
\text{with finitely generated left }A\text{-module stalks},\\
R^ih_*F|_V=0\quad(i>2d),\\
g^*(R^ih_*F|_V)\xrightarrow{\sim}R^ih_{T*}g_X^*F
\quad(g:T\to V,\ i\geq0).
\end{gathered}
\tag{E.NC1}
\]
The last arrow is the canonical base-change map. Neither commutativity of \(A\), finiteness of its underlying set, nor separatedness of \(h\) is required here. This is an ordinary torsion statement, not an adic assertion. Smoothness over the Noetherian base makes the finite-type maps and the open restrictions used below finitely presented.

**Coefficient conventions and exact operations.** All direct images in this proof are derived in left-module sheaves. They agree after forgetting coefficients with abelian-sheaf direct images. To check the needed extension of E.2g to a noncommutative \(A\), use its augmented hypercover complex with free *left* \(A\)-module sheaves. Local contraction of each finite-support cycle is still valid, since its differential uses only integers and left-linear maps. Hom into an injective left-module sheaf makes that augmented complex exact. The BB.3 acyclicity proof, with BA.5's finite-family hypercovers, therefore computes the underlying abelian cohomology too. Apply the same argument on the qcqs inverse images of affine étale test objects. This identifies the higher direct images and their restriction and connecting maps. It does not assert that forgetting an arbitrary coefficient action preserves injectives.

Finitely generated locally constant left \(A\)-module sheaves are closed under kernels, cokernels and extensions. The proof of Constructible sheaves, Lemma 3.1 uses finite presentations and left-linear relations, so does not need commutativity for these three claims. Explicitly, trivialize two modules and the images of a finite generating set to make a map constant; its kernel is finitely generated by left-Noetherianity. For an extension, locally lift generators of a finite presentation of the quotient. There are finitely many generating relations, whose images in the constant submodule can also be made constant. The quotient presentation of the extension is then constant. No tensor product over a noncommutative \(A\) is being used.

We may work over finitely many pairwise disjoint affine neighbourhoods of the generic points of \(S_{\mathrm{red}}\), after removing intersections of its irreducible components. Their union is dense. The equivalence of étale topoi for a nilpotent thickening transports the entire comparison diagram, including its direct-image counit: for an arbitrary \(T\to S\), the pullback of \(S_{\mathrm{red}}\hookrightarrow S\) is again nilpotent. Thus results over this reduced dense open transfer to the corresponding open of \(S\). We first suppose \(S\) affine and integral, with generic point \(\eta\), and \(h\) separated and of pure relative dimension \(d\). No regularity or normality of the parameter base is assumed.

**A finite trivializing cover without finite module fibres.** We explain the geometric step for any of these coefficient rings. A connected component \(T_0\) of the smooth generic fibre \(X_\eta\) is normal and integral. Indeed smooth étale charts reduce normality to a polynomial ring over a field and the integral-closure identity in AW.2; normal Noetherian components are disjoint. Write \(K\) for its function field and \(M\) for a geometric generic stalk of \(F\). The field-topos equivalence AB.2 applies to arbitrary discrete stalks, not just finite sets. It gives a continuous \(A\)-linear action of \(\operatorname{Gal}(K^{\mathrm{sep}}/K)\) on \(M\). Intersect the open stabilizers of finitely many \(A\)-generators of \(M\). This intersection is the kernel of the action on all of \(M\), hence is open and normal. Its fixed field is a finite Galois extension \(L/K\), with group \(G\).

Normalize \(T_0\) in \(L\). This normalization is finite. On a normal Noetherian affine domain \(R\subset K\), choose an integral \(K\)-basis \(e_1,\ldots,e_r\) of the separable extension \(L/K\), scaling an arbitrary basis to clear the coefficients of its monic equations. Its trace-pairing determinant \(\Delta\) is nonzero. If \(z\) is integral over \(R\), each \(\operatorname{Tr}(ze_i)\) is integral and lies in \(K\), so belongs to \(R\) by normality. The adjugate matrix bounds the coordinates of \(z\) by \(\Delta^{-1}R^r\). The integral closure is a submodule of this finite module, and is therefore finite. Localization of integral closure glues these affine normalizations.

This finite normalization is in fact étale. On an affine étale chart trivializing \(F\), take a normal connected component with function field \(K'\). Its absolute Galois group acts trivially on \(M\); after choosing a compatible embedding into \(K^{\mathrm{sep}}\), this implies \(L\subset K'\). Consequently
\[
L\otimes_KK'\simeq\prod_{\sigma\in G}K'.
\tag{E.NC2}
\]
Normalization commutes with this étale base change by AW.2. The chart is normal, so the pulled normalization is the disjoint union of \(|G|\) copies of that chart. Hence the cover is finite étale and its Galois action makes it a \(G\)-torsor, as checked on these charts. On its normal source the pulled sheaf is constant: the unit to its generic direct image is an isomorphism by AZ.4, checked on trivializing charts, and its generic sheaf is \(\underline M\). This also retains the generic descent action on \(M\).

There are only finitely many connected components of \(X_\eta\). Spread their clopen decomposition and the finitely many covers, actions, torsor isomorphisms and inverses to some common base open using BD.1–2. The trivializations and their inverses spread by AZ.3's morphism-continuity argument. For the present left modules this is the same finite-generator, finite-relation proof: sections descend, their finitely many equations eventually hold, and two inverse maps retain their inverse identities. Include the finitely many equivariance equations. Thus on each resulting clopen piece we have
\[
p:X_1\longrightarrow X\text{ a finite étale }G\text{-torsor},
\qquad p^*F\simeq\underline M,
\qquad h_1=hp.
\tag{E.NC3}
\]
We prove the claim piece by piece and intersect only finitely many base opens. The finite-set classification in Appendix N alone would not justify this step for an infinite underlying \(M\). The argument above supplies that missing distinction. No condition that \(|G|\) be invertible is imposed.

**Prime coefficients and descent.** First suppose \(\ell A=0\) for one prime \(\ell\) invertible on \(S\). Write the \(\mathbb F_\ell\)-vector space \(M\) as the directed union of its finite-dimensional subspaces. For a finite-dimensional space, a basis identifies its constant sheaf with a finite direct sum of \(\mathbb F_\ell\). Fixed-scheme filtered-coefficient continuity in BA.5, on the qcqs inverse images of affine étale objects, now gives the natural isomorphism
\[
R^qh_{1*}\underline M\simeq
(R^qh_{1*}\mathbb F_\ell)\otimes_{\mathbb F_\ell}M.
\tag{E.NC4}
\]
It is independent of the chosen finite-dimensional bases, being induced by the natural coefficient maps. Thus it respects the \(A\)-action, deck descent and base-change comparisons. The finite-dimensional subspaces need not be \(A\)-submodules; their union and this natural map recover the full action.

Apply E.2k to the separated smooth \(h_1\) and \(\mathbb F_\ell\). On one dense open, all \(R^qh_{1*}\mathbb F_\ell\) are finite locally constant, vanish for \(q>2d\), and commute with every base change. Formula (E.NC4) makes each nonzero cover term a locally constant finitely generated \(A\)-module sheaf: locally it is a finite direct sum of \(M\).

The augmented Čech nerve of \(p\), with coefficients \(F\), gives
\[
E_2^{a,b}=\mathcal H^a\bigl(G,R^bh_{1*}\underline M\bigr)
\ \Longrightarrow\ R^{a+b}h_*F.
\tag{E.NC5}
\]
Here \(\mathcal H^a(G,-)\) means cohomology of the group-cochain complex of sheaves, with its descent action. To construct the sequence, the augmented nerve is exact on geometric stalks: choose one lift through the finite étale surjection and insert it to contract the augmented complex. Finite étale direct image is exact, so applying derived \(h_*\) to this resolution gives the first-quadrant sequence. The torsor identification makes degree \(a\) the product indexed by the finite set \(G^a\), with the usual alternating group differential. These are finite products of the cover cohomology sheaves.

Every \(E_2^{a,b}\), subsequent subquotient, and abutment is therefore locally constant and finitely generated over \(A\), by the exact operations proved above. For a fixed total degree only finitely many positions contribute, so the filtration and the spectral-sequence comparison are finite in that degree, although the group-cochain complex may be unbounded. Exact inverse image commutes with its finite products and cohomology. The cover-term base-change maps yield an isomorphism of the spectral sequences and hence of their abutments. Their augmentation is the original section restriction, so this abutment map is the canonical ordinary-image comparison, not an unrelated isomorphism. The same dense open works for all degrees; no further open was chosen for individual values of \(a\).

**Why the bound is uniform.** One cannot obtain an upper bound by claiming that finite-group cohomology vanishes above a fixed degree: this is false when \(\ell\mid |G|\). Instead use the comparison just proved for the geometric generic point \(\bar\eta\). Cohomological dimension, Corollary 7.2 applies to every torsion sheaf on a \(d\)-dimensional finite-type scheme over a separably closed field. It gives
\[
(R^ih_*F)_{\bar\eta}\simeq H^i(X_{\bar\eta},F)=0
\qquad(i>2d).
\tag{E.NC6}
\]
Each of these higher images is already locally constant on the same integral base open. A locally constant sheaf with zero generic stalk is zero there: after trivialization the zero locus is both open and closed, and the base is connected. This proves simultaneous vanishing on the previously chosen open, with no infinite intersection of dense opens. The provider's proof establishes the absolute torsion bound through affine vanishing and the étale-to-Zariski spectral sequence; compact-support vanishing alone would not suffice for this ordinary-image step.

**Returning to the original ring.** If \(n=1\), the ring and sheaf are zero. Otherwise the Chinese-remainder idempotents of \(\mathbf Z/n\) are central in \(A\) and decompose \(A\) and \(F\) into finitely many prime-primary parts. On a part killed by \(\ell^e\), use
\[
F\supset\ell F\supset\cdots\supset\ell^eF=0.
\tag{E.NC7}
\]
Its successive quotients are locally constant finitely generated left \(A/\ell A\)-modules. This quotient ring is left-Noetherian and killed by \(\ell\), so the prime case applies. Intersect the finitely many resulting dense opens. The coefficient long exact sequences, finite-generation and local-constancy closure, and the natural five-lemma comparison recover (E.NC1) for every extension in the filtration and then for the finite product. The interval \([0,2d]\) is preserved by these extensions. The underlying-cohomology argument at the start identifies comparisons across the quotient coefficient rings; no flatness over \(\mathbf Z/n\) is assumed.

**Removing separatedness and pure dimension.** The relative dimension of a smooth morphism is locally constant on its source. Its finitely many clopen dimension loci reduce the separated case to pure dimensions at most \(d\). Now take an arbitrary smooth finite-type \(X\) over our affine base, and a finite affine cover \(X=\bigcup_{j=1}^rU_j\). Each nonempty finite intersection is a quasi-compact open of an affine \(U_j\), hence separated, smooth and of finite presentation over the base. Apply the separated result to the restrictions of \(F\) on all these finitely many intersections, and take a common dense open. The ordered finite-cover Čech spectral sequence has columns \(0\leq a\leq r-1\); its entries are finite products of those higher direct images, with their canonical restriction maps. Its finite filtrations prove local constancy, finite generation and arbitrary-base comparison for \(Rh_*F\), initially with bound \(2d+r-1\). Apply (E.NC6) once more: Corollary 7.2 also allows non-separated finite-type schemes, so the generic stalks vanish above \(2d\). Local constancy reduces the bound to \(2d\) on this same open.

Finally take the union of the dense opens chosen over the finitely many generic components of \(S_{\mathrm{red}}\), and transport across the nilpotent thickening as above. An arbitrary \(T\to V\) is checked on its affine opens; their inverse-image diagrams are qcqs and the counit-defined comparisons agree on overlaps. This includes non-Noetherian and non-qcqs test bases. The resulting dense open and canonical maps prove (E.NC1) at the full stated scope. \(\square\)

**Coefficient and finite-cover scope.** This is the coefficient and finite-cover stage in Deligne's finiteness exposition in SGA \(4\frac12\), Theorem 1.9, proof §2.2 (printed pp. 238–239). The argument uses the earlier results linked at each reduction, including their coefficient hypotheses, and gives the infinite-fibre and noncommutative details. E.2k gives a finite-coefficient duality proof. E.2m below supplies the general constructible-source induction and its cone and factorization steps; E.2n then supplies the distinct uniform adic/rational passage. The smooth stage alone does not establish the general generic-base-change theorem.

#### Ordinary constructible generic base change

**Theorem E.2m (ordinary torsion coefficients).** Let \(S\) be Noetherian, let \(f:X\to Y\) be a morphism of finite-type \(S\)-schemes, and let \(A\) be a unital left-Noetherian ring killed by a positive integer \(n\) invertible on \(S\). For a constructible sheaf \(F\) of left \(A\)-modules on \(X_{\mathrm{\acute et}}\), there are a dense open \(U\subset S\) and a finite integer \(N\) such that
\[
\begin{gathered}
R^if_*F|_{Y_U}\text{ is constructible for all }i,\\
R^if_*F|_{Y_U}=0\quad(i>N),\\
g_Y^*(Rf_*F|_{Y_U})\xrightarrow{\sim}Rf_{T*}g_X^*F
\quad(g:T\to U).
\end{gathered}
\tag{E.GB1}
\]
The last map is the canonical comparison. Here constructible means finitely generated locally constant on a finite locally closed partition; it does not mean finite underlying sets. The ring \(A\) need not be commutative, and \(f\) need not be separated. The same conclusion, with some finite cohomological interval instead of \([0,N]\), holds for each \(F\in D^b_c(X,A)\). This is not yet a theorem about adic or rational coefficient systems.

We first check the coefficient scope of the inputs. Then the proof has an ordered dimension induction; its lower-dimensional assertion is never used at the dimension currently being proved.

**Left-module inputs.** The proof of Constructible sheaves, Lemma 3.1 and Proposition 3.2 uses finite generators, finite relations, kernels, cokernels and extensions. With free left \(A\)-modules in its presentation, these arguments prove precisely the same closure assertions. We do not use its tensor assertion over \(A\).

More explicitly, Lemma 5.2 supplies finite generating presentations by
\[
P_V=a_!\underline A_V,\qquad a:V\to X
\text{ affine étale of finite presentation}.
\tag{E.GB2}
\]
Its proof also works on the left: maps from \(P_V\) are sections; these generate every stalk. Cokernels of finite partial generating sums are constructible by the preceding closure result. Their supports are clopen in the compact constructible topology and have empty common intersection, so one finite sum is surjective. Its kernel is constructible and has another such finite generating sum. Repeating gives as many finite presentation steps as needed. The constructibility of \(P_V\) is the geometric stratification into finite étale pieces in Lemma 4.1; it merely replaces a finite direct sum of the coefficient module by a finite direct sum of left \(A\)-modules.

Proposition 7.1 likewise holds on the left. For a subsheaf of a constant finitely generated module on an irreducible Noetherian scheme, its generic submodule has finitely many generators. Represent them on a pointed étale neighbourhood. Their constant values make the two pullbacks agree, so they descend to its open image. No extra value can occur on an étale open there without occurring at the generic point. This identifies the subsheaf with that constant submodule on a dense open. Noetherian induction and a finite trivializing cover on each stratum finish the proof; quotients follow by taking cokernels. Thus an arbitrary quotient of a constructible left module is constructible here, not just the cokernel of a previously constructible kernel.

The finite-stalk product formula, open--closed localization and adjunction calculations of E.2c--E.2i are left-linear. The preceding quotient assertion proves the converse direction of E.2h for left \(A\)-modules, using the epimorphism \(q^*q_*G\to G\). Their bounds and their comparison identities are unchanged. For E.2g, the module-injective acyclicity argument in E.2l identifies the actual underlying torsion direct images and counits with the abelian ones. Thus its proper comparison applies before the unknown ordinary image is constructible, also with these coefficients.

**Proper supports without a commutativity assumption.** We need the analogous extension of E.2k(1), not an unsupported invocation of its commutative statement. Let \(v:Z\to B\) be separated of finite type between Noetherian schemes, with fibre dimension at most \(e\), and put \(D=2e\). Proper--open construction and compact-support base change, after the coefficient acyclicity comparison just checked, give the same underlying compact-support functor, its canonical comparisons, and the bound \([0,D]\) on every left \(A\)-module sheaf. The bound is Theorem 12.1, which is an assertion about all torsion sheaves, not a finiteness assumption on their stalks.

First suppose \(\ell A=0\). For any separated finite-type \(c:Q\to B\), natural coefficient maps give
\[
R^qc_!\underline A\simeq
(R^qc_!\mathbb F_\ell)\otimes_{\mathbb F_\ell}A.
\tag{E.GB3}
\]
To verify it, write the underlying vector space \(A\) as the filtered union of its finite-dimensional subspaces. The formula for a finite-dimensional space is the finite-sum identity. Filtered-coefficient continuity passes to the union: choose a proper--open factorization, use exact extension by zero and the qcqs cohomological continuity of BA.5 on the proper factor. These identifications commute with coefficient maps, so recover the left \(A\)-action even though the finite subspaces need not be left ideals. Compact supports, Theorem 12.3, used only with \(\mathbb F_\ell\), makes (E.GB3) constructible with finitely generated left \(A\)-module stalks: on a finite constructible partition it is a finite direct sum of \(A\). This uses the exact geometric provider already recorded in E.2k, not the ordinary-image theorem being proved.

For a constructible \(H\) on \(Z\), take \(D+2\) finite generating steps (E.GB2). With the finite complex \(E\) in degrees \(-D-1,\ldots,0\) and its last kernel \(J\), the augmented resolution yields
\[
J[D+1]\longrightarrow E\longrightarrow H
\longrightarrow J[D+2].
\tag{E.GB4}
\]
Each term of \(E\) is a finite sum of \(a_!A\). Choose the affine étale basis maps inside affine opens of \(Z\); they are separated. Composition of proper supports identifies its image with a sum of \(R(va)_!A\), covered by (E.GB3). The relative dimensions of \(va\) are at most \(e\). The finite-complex spectral sequence therefore makes every cohomology sheaf of \(Rv_!E\) constructible. The two outer terms of (E.GB4), after \(Rv_!\), have zero cohomology in every degree \(i\geq0\), since \(i+D+1>D\). Hence \(H^i(Rv_!E)\to R^iv_!H\) is an isomorphism for these degrees. The original bound makes the other degrees of \(Rv_!H\) zero. This proves bounded constructibility without assuming that \(H\) has finite projective dimension or that the last kernel already has finite compact cohomology.

For general \(n\), use the finitely many central primary idempotents and the finite prime-power filtrations from E.2l. Each successive quotient is a constructible left module over a left-Noetherian ring killed by one prime. The long exact cohomology sequences give bounded constructibility over \(A\), with the same interval. Finite cohomology towers give the bounded-complex assertion and interval \([a,b+D]\). This proves the left-module proper-support input, including proper ordinary-image finiteness. The comparison is the proper--open comparison already constructed, so is compatible with composition and arbitrary base change.

**The induction assertion and its initial case.** We first work over an integral Noetherian base, with generic point \(\eta\). Let \(I(r)\) assert (E.GB1) for every dense open immersion \(j:X\hookrightarrow Y\) of finite-type schemes over any such base with \(\dim X_\eta\leq r\), retaining all the stated coefficients. It includes a finite bound and every base change, not just geometric fibres. Once it holds for sheaves, the finite cohomology tower proves it for a given bounded constructible complex, after intersecting finitely many base opens. Factoring a locally closed immersion through its closed closure extends the same assertion to those immersions: closed direct image is exact, preserves constructibility, and has canonical arbitrary base change by the finite-stalk formula.

If \(X_\eta\) is empty, so is \(Y_\eta\), since the open is dense. A finite affine cover and clearing the finitely many equations \(1=0\) after localization make the entire pair empty on a base open. If \(\dim X_\eta=0\), density makes the open contain every point of \(Y_\eta\): a finite-type zero-dimensional scheme over a field has only closed points. Its closed complement has empty generic fibre and disappears after the same finite localization argument. The open immersion then is an isomorphism. This proves \(I(0)\), with no reducedness assumption on the pair.

Assume \(I(r-1)\), for \(r\geq1\). E.2f applies over each coordinate-line base, whose generic source dimension is smaller, and E.2e constructs the good open \(W\subset Y\) with a closed complement \(Z\) finite over a common base open. These lemmas are geometric and their canonical-map proof uses only left-linear adjunctions. Thus \(K=Rj_*F\) is bounded constructible on \(W\) and its comparison is invertible there. No conclusion at the points of \(Z\) has yet been used.

**First prove the smooth-source case at dimension \(r\).** Suppose \(X\to S\) is smooth and \(F\) is locally constant. The claim is local on the target. On an affine target chart, take its projective closure over an affine base open and keep \(X\) as an open in that closure. Density persists. Write \(b:Y\to S\) for this proper model and \(u:W\hookrightarrow Y\), \(i:Z\hookrightarrow Y\) for the good open and finite complement just constructed. E.2l proves bounded constructibility and all base comparisons of
\[
B=Rb_*K=R(bj)_*F
\tag{E.GB5}
\]
after one further shrinking. The left-module proper-support argument proves bounded constructibility of \(Rb_*u_!u^*K\); its input \(u^*K\) is already known, so no circular finiteness assumption occurs. E.2i now proves bounded constructibility of \(K\) on all of \(Y\). For every \(T\to S\), E.2d applies to the actual comparison: its first assumption is the good-open comparison, its second is E.2g's proper comparison for the still arbitrary torsion complex, and its third is E.2l. Hence the comparison is invertible on the whole target. A finite target cover and finitely many base intersections prove the smooth-source case, including a finite bound, at the current dimension \(r\).

**Produce the smooth open at the original base scope.** The geometric proof of E.2a works over an arbitrary integral Noetherian base with ordinary constructible left-module coefficients. Here are the scope checks. In positive characteristic, pass from the fraction field \(K\) to its perfection; in characteristic zero take \(K\) itself. The reduced generic source has a dense smooth open by M.1. Descend the reduction, its nilpotent defining ideal, this open and its finite standard-smooth charts to a finite purely inseparable field extension \(K'/K\), using the finite-diagram and ideal-power argument of E.2a. Its closed complement has smaller generic dimension on every component. No finite-field point or weight is used in these arguments.

For clarity, over a domain \(R\) with fraction field \(K\), choose finitely many generators \(\beta_i\) of \(K'/K\) and a common \(q=p^a\) with \(\beta_i^q\in K\). Clear their denominators and set \(R'=R[\beta_i]\subset K'\). The bounded-exponent monomials generate \(R'\) as an \(R\)-module and \((R')^q\subset R\). Thus \(\operatorname{Spec}R'\to\operatorname{Spec}R\) is finite, surjective and radicial. A subsequent denominator \(c\in R'\setminus0\) is implemented over the original base by inverting \(c^q\in R\). In characteristic zero the field extension is trivial and \(q=1\). This does not require finiteness of normalization in an arbitrary inseparable extension, or an excellence assumption.

The rest of E.2a descends the explicit charts by finitely many equations, removes the finitely many vertical components, and chooses the open where the already given constructible sheaf is locally constant. Hence on the reduced base-changed pair there is a dense open \(w:V\hookrightarrow X\) with
\[
\begin{gathered}
V\to S'\text{ smooth},\qquad w^*F\text{ locally constant},\\
\dim(X\setminus V)_{\eta'}<r.
\end{gathered}
\tag{E.GB6}
\]
The sheaf-theoretic transport is finite topological invariance, Theorem 6.2, not just a homeomorphism. The unique geometric lift in the finite-stalk product formula makes the actual unit and counit isomorphisms for all left \(A\)-module sheaves. They are exact and preserve constructible partitions. The composition-adjunction calculation in D.2a consequently transports derived direct images and their canonical comparisons at this ordinary scope. For an arbitrary original test base \(T\), its finite radicial pullback \(T'\to T\) gives the same conservative equivalence, so the comparison checked over \(S'\) descends to \(S\). Reduction maps are covered as well. The arithmetic Frobenius and adic parts of D.2a are not used.

**The supported cone closes the induction.** On the resulting pair let
\[
F\longrightarrow Rw_*w^*F\longrightarrow\Delta
\longrightarrow F[1]
\tag{E.GB7}
\]
be the unit triangle. The smooth-source case just proved at dimension \(r\) applies to both \(w\) and \(jw\). In particular its first application makes \(\Delta\) bounded constructible. Its restriction to \(V\) is zero, so localization identifies it with the closed direct image of its restriction to \(H=(X\setminus V)_{\mathrm{red}}\). The locally closed immersion \(H\to Y\) has generic source dimension less than \(r\). Apply \(I(r-1)\) to the finitely many cohomology sheaves of this restricted complex. It gives bounded constructibility and arbitrary-base comparison for \(Rj_*\Delta\), after a finite common shrinking.

The comparison for \(w\) identifies the pullback of (E.GB7) with its base-changed unit triangle: both units correspond to restriction under the same adjunction, so this identification is of maps, not only objects. Applying \(Rj_*\) gives
\[
Rj_*F\longrightarrow R(jw)_*w^*F
\longrightarrow Rj_*\Delta\longrightarrow.
\tag{E.GB8}
\]
The latter two terms are bounded constructible and their canonical comparisons are invertible. The finite cohomology long exact sequences prove both assertions for the first term. Compatibility of ordinary comparisons with composition is (E.R6), and naturality gives a morphism of these triangles after every base change. This verifies that the recovered isomorphism is exactly (E.GB1). Descend through the finite radicial change as above. Thus \(I(r)\) holds. The dimension induction is complete.

**From open immersions to a general morphism.** First let source and target be affine over an integral base. A finite-type morphism between them is a closed immersion into an affine space over its target. Its schematic closure in the associated projective space provides an open immersion followed by a proper morphism. The closure is still of finite type over \(S\). Apply the open theorem, then the left-module proper finiteness and proper comparison proved above. Composition gives bounded constructibility and the actual arbitrary-base comparison for this affine-source, affine-target map.

For a separated finite-type source over an affine target, use a finite affine source cover; all its finite intersections are affine, since the source is separated over that target. Its finite-cover Čech spectral sequence has terms given by the cases just proved. Their finite bounds have a finite maximum, and there are finitely many Čech columns. Constructibility and comparison follow from its finite filtrations in each degree and its canonical augmentation. This proves every separated case.

For a possibly non-separated source, choose a finite affine cover again. A finite intersection is a quasi-compact open of one affine member, so is separated over the affine target, although it need not be affine. The separated case therefore applies to each of these finitely many intersections. The same finite-cover argument proves the general case. Finally take a finite affine cover of \(Y\). Every morphism in question is of finite type and quasi-separated because all the original schemes are Noetherian; the intersections and Čech constructions used here retain their required finiteness. This argument does not silently assume affine intersections for a non-separated source.

An arbitrary Noetherian \(S\) is reduced to the finitely many disjoint generic integral pieces of \(S_{\mathrm{red}}\) by removing component intersections. Apply the result to each piece and take the union of its dense opens. Nilpotent topological invariance, with the same base-change compatibility, transports it to a dense open of the original \(S\). Finite cohomology towers prove the stated bounded-complex version. For a non-Noetherian or non-qcqs test scheme \(T\), all comparison arguments are checked on its affine opens and agree on overlaps by their counit definition. No additional shrinking is selected for individual test schemes. This proves the theorem. \(\square\)

**Ordinary coefficient scope.** E.2m gives the constructible ordinary-coefficient induction and final factorization of Deligne’s finiteness theorem, SGA \(4\frac12\), Theorem 1.9, §§2.3–2.8 (printed pp.239–241), under the stated geometric and coefficient hypotheses. The adic/rational comparison requires the uniform argument of E.2n. Intersecting one dense open for each torsion level does not establish that comparison.

#### One open for completed and rational coefficients

**Theorem E.2n (one first reduction, all base changes).** Let \(S\) be Noetherian and let \(f:X\to Y\) be an \(S\)-map of finite-type \(S\)-schemes. Let \(O\) be a complete discrete valuation ring with uniformizer \(\pi\) and finite residue field \(\kappa\) of characteristic \(\ell\), invertible on \(S\). On the pro-étale site use the constant ring \(\underline O\). Suppose \(K\) is derived complete and
\[
K_1=K\otimes_O^L\kappa\simeq\nu_X^*F,
\qquad F\in D^b_c(X_{\mathrm{\acute et}},\kappa).
\tag{E.AD1}
\]
There is one dense open \(U\subset S\) such that \(B=Rf_*K|_{Y_U}\) is derived complete, bounded, and has bounded constructible classical first reduction. For every scheme \(g:T\to U\), the canonical completed comparison is an isomorphism:
\[
g_{Y,c}^*B\xrightarrow{\sim}Rf_{T*}g_{X,c}^*K|_{X_U},
\qquad g_c^*=C g^*.
\tag{E.AD2}
\]
Here \(C\) is derived completion on constant \(O\)-modules. Neither separation of \(f\) nor Noetherianity of \(T\) is required. The open is chosen from \(F\) alone; it is not an intersection of infinitely many levelwise opens. This first assertion uses the precise reduction-defined category, not an unspecified category of inverse systems.

**Proof: choose the open once.** Apply E.2m to the single bounded complex \(F\). It gives \(U\), a finite interval \([a,b]\) containing the cohomology of \(Rf_*F|_{Y_U}\), and its canonical comparison for every \(T\to U\). Shrinking here means the finite cohomology-tower construction in E.2m, not one shrinking for each \(O/\pi^n\).

The necessary coefficient maps are already proved in Constructible complexes, BK.3–BK.5. The two-term free resolution \([O\xrightarrow{\pi^n}O]\) gives, with its specified quotient transitions,
\[
\begin{gathered}
(Rf_*K)\otimes_O^LO/\pi^n\simeq Rf_*(K\otimes_O^LO/\pi^n),\\
Rf_*C K\simeq C Rf_*K,\qquad
(C H)\otimes_O^LO/\pi^n\simeq H\otimes_O^LO/\pi^n.
\end{gathered}
\tag{E.AD3}
\]
These are perfect-coefficient cone calculations. They do not assert a projection formula for arbitrary coefficient complexes. The middle comparison uses that the right adjoint \(Rf_*\) preserves products and homotopy limits. The open restriction of \(Rf_*K\) is its direct image over \(U\), by slice restriction. Thus \(B\) is complete and its first reduction is the classical pullback of \(Rf_*F|_{Y_U}\), by BK.2.

**Proof: test the actual comparison, not just the objects.** Let \(Q_g\) be the cone of (E.AD2), where the arrow is defined by completing the ordinary adjunction comparison. Both its source and target are complete by (E.AD3), so \(Q_g\) is complete. By BK.6, reduction of that arrow modulo \(\pi\) is exactly
\[
\nu_{Y_T}^*\bigl(g_Y^*(Rf_*F|_{Y_U})
 \longrightarrow Rf_{T*}g_X^*F\bigr).
\tag{E.AD4}
\]
Indeed the unit and counit defining the comparison commute with both terms of the free coefficient complex and with its multiplication map. The étale/pro-étale comparison of BK.2 uses restriction of sections and preserves those adjunction maps. E.2m makes (E.AD4) invertible, hence \(Q_g\otimes_O^L\kappa=0\).

A complete complex with zero first reduction is zero. Its coefficient triangle makes multiplication by \(\pi\) invertible; therefore every higher coefficient cone is zero, and completeness identifies the complex with the homotopy limit of these zero cones. Equivalently this is the first-reduction detection argument of BW.1, also valid over the constant ring by BK.4. Apply it to \(Q_g\). This proves (E.AD2) on the same \(U\) for every \(g\). Reduction detects this isomorphism; no claim that it is faithful on morphisms is needed. Compatibility with consecutive base changes is inherited from the actual adjunction construction in BK.6.

**Proof: retain a genuine bound.** Write \(B_n=B\otimes_O^LO/\pi^n\). The exact coefficient sequences give triangles
\[
B_{n-1}\longrightarrow B_n\longrightarrow B_1,
\qquad B_1\longrightarrow B_{n+1}\longrightarrow B_n.
\tag{E.AD5}
\]
The first shows inductively that every \(B_n\) has cohomology in \([a,b]\). The second makes \(H^b(B_{n+1})\to H^b(B_n)\) surjective. Complete reconstruction by the product-cone formula of BK.1 can only add a degree \(b+1\); its obstruction is the first derived limit of these top cohomology sheaves. Repleteness makes that obstruction zero: locally solve the successive lifting equations for the surjective tower, as in BM.6. Hence \(B\) itself is in \(D^{[a,b]}\). This is an argument with derived reductions and their actual transitions, not ordinary quotients of the cohomology sheaves. Bounded constructibility of the first reduction was proved above. Together these establish the claimed complete-category assertion. The proof is local on an arbitrary test scheme \(T\); the pulled-back direct-image map \(f_T\) remains qcqs, so no finiteness assumption on \(T\) was introduced. \(\square\)

**Corollary E.2n.1 (actual rational constructible coefficients).** Let \(S,X,Y\) be finite-type schemes over a finite field \(k\), let \(f:X\to Y\) be an \(S\)-map, and let \(E/\mathbb Q_\ell\) be finite with \(\ell\ne\operatorname{char}k\). For every bounded complex \(M\) of constructible rational sheaves in the ambient pro-étale derived category, one dense open \(U\subset S\) makes \(Rf_*M|_{Y_U}\) bounded constructible and gives the actual ringed comparison
\[
Lg_Y^*(Rf_*M|_{Y_U})\xrightarrow{\sim}Rf_{T*}Lg_X^*(M|_{X_U})
\qquad(T\to U).
\tag{E.AD6}
\]
If \(Y=S\), after a further finite shrinking all its cohomology sheaves are lisse, and (E.AD6) includes their geometric-fibre cohomology comparison. There is no smoothness, lissity or weight assumption on the original \(M\).

**Proof: integral models and coefficient rings.** First work on separated finite-type schemes, affine-locally on \(S\) and \(Y\). Let \(O\) be the valuation ring of \(E\). The coefficient-ring adjunction in BW.2–BW.3 identifies complete constant-\(O\) objects with complete modules over \(R_Z=\widehat O_Z\). BX.6–BX.7 supplies a bounded constructible complete \(R_X\)-complex \(P\) and an isomorphism
\[
P[1/\pi]\simeq M,
\qquad E_Z=R_Z[1/\pi].
\tag{E.AD7}
\]
For a complex, this uses closure under cones and its finite cohomology tower, not realization from the derived category of the heart. The model is constructible; no global lisse integral lattice is assumed on a singular scheme. The proof of BX.6 explicitly constructs models by strata and finite-group lattice descent.

Apply the theorem to the underlying complete constant-\(O\) object. On the resulting \(U\), the first reduction of its image is bounded constructible. Thus the image belongs to the established complete constructible category, without invoking a generic comparison theorem to prove that membership. The coefficient adjunction of BW.5 identifies ordinary direct images and their units and counits. BX.3 identifies completed pullback with actual ringed pullback on these objects. The coefficient map \(g^{-1}R_Z\to R_{Z_T}\) is part of that operation; the two sheaves are not silently identified.

We check explicitly that these comparisons still apply to an arbitrary \(T\to U\). On \(X_U\) and \(Y_U\), BO.6 and BX.3 give finite algebraic strata with pro-étale local finite free complex models. Pull back these finitely many strata, their trivializing covers and their finite complexes. They provide complete models with finite bounds over \(T\). The open–closed filtration used in BX.3 is finite and pulls back; all its closed immersions are of finite presentation. Its ordinary localization and support formulas come from BX.1–BX.2, whose neighbourhood construction works over arbitrary rings. Consequently that same finite devissage identifies ordinary ringed pullback with completed pullback for these particular pulled-back objects. It does not require a new stratification theorem or a global rational-category equivalence on every non-Noetherian \(T\).

On every quasi-compact target slice, BX.4 commutes a qcqs ordinary direct image with uniformly bounded-below filtered colimits. Apply it to the multiplication-by-\(\pi\) tower on \(P\), and to its bounded pulled-back model. This proves the natural localization comparisons on both sides,
\[
\begin{gathered}
(Rf_*P)[1/\pi]\simeq Rf_*(P[1/\pi]),
\\
(Rf_{T*}Lg_X^*P)[1/\pi]\simeq Rf_{T*}(Lg_X^*P[1/\pi]).
\end{gathered}
\tag{E.AD8}
\]
The inherited finite bounds supply the common lower bounds required there. Exact localization commutes with ringed inverse image by associativity of scalar extension. All comparisons are coefficient-extension, restriction and adjunction maps, so the localization of (E.AD2) is the canonical arrow (E.AD6), by the units-and-counits identification of BW.5 and BX.7. In particular, we do not reduce the rational sheaf modulo \(\pi\): that reduction would be zero and would prove nothing. We first choose its integral model and rationalize only after the complete comparison has been established.

Bounded constructibility over \(Y_U\) follows from the coefficient equivalence and BW.7, or directly from the finite-stratum models just described. If \(Y=S\), make the finitely many cohomology sheaves of the first reduction lisse on a dense open of each generic component. BO.6 then makes the rational cohomology lisse there. The local finite complexes show that ringed pullback on rational constructible sheaves is exact; at a geometric point, the cohomology of (E.AD6) is therefore the stated stalk-to-fibre comparison.

Finally remove the temporary separation choices. A finite affine cover of the source of a separated map has affine multiple intersections. For a possibly non-separated source over an affine target, the intersections in a finite affine cover are quasi-compact opens of affines, hence separated but need not be affine. Apply the separated argument just proved to the finitely many intersection terms, choosing integral models there if necessary. The finite alternating Čech complex of derived open direct images of the restrictions resolves the original complex: use one bounded-below injective resolution, whose augmented sheaf Čech complexes are locally contracted by a member of the cover containing the point. Exact open restriction preserves these injective resolutions by its exact extension-by-zero left adjoint. Its direct images and canonical base-change maps therefore form the specified finite derived diagram. Intersect its finitely many base opens and use exactness of finite cones to obtain (E.AD6), boundedness and constructibility for the original map. Finite target and parameter-base covers give the full stated scope; their generic opens can be combined after first separating the finitely many generic components, as in E.2m. This argument retains arbitrary \(T\) and imposes no global lattice or separation condition on the original schemes. \(\square\)

**Coefficient comparisons.** E.2m gives the ordinary first-reduction theorem. BK supplies its completed comparison with the actual maps; BW and BX supply the coefficient-ring and rational identifications, and BO supplies the finite-stratum local models used on arbitrary pullbacks. Together these results give the uniform adic/rational generic comparison in Appendix E at their stated hypotheses. E.2b also gives a smooth/lisse relative-duality argument. Higher-dimensional heart realization is a separate assertion and is not a consequence of these generic comparisons.

**Retained proof using generic base change.** The sheaf \(L_0^\vee\) is pure of the opposite weight. Appendix D makes all \(R^qa_!L_0^\vee\) mixed. There are only finitely many nonzero such sheaves and finitely many terms in their mixed filtrations. By ordinary constructibility, shrink the base until those terms and quotients are lisse. Proposition E.2b supplies a further dense open on which the ordinary direct-image sheaves are lisse and their formation commutes with geometric fibres, by the canonical comparison maps. Intersect it with the open already chosen for the finite mixed filtrations.

The relative smooth trace pairing, with fibrewise Poincaré duality, identifies lisse sheaves as
\[
\bigl(R^ra_*L_0\bigr)^\vee
\simeq R^{2d-r}a_!(L_0^\vee)(d).
\tag{E.1}
\]
The isomorphism is a morphism of sheaves, induced by the relative trace, and is checked on the geometric fibres where both comparisons hold. The right side is mixed. Dualizing its finite lisse filtration is exact; its pure grades acquire the opposite weights. Hence \(R^ra_*L_0\) is mixed for every \(r\). This uses only duality of lisse representations and the smooth trace pairing, not mixed stability of Verdier duality on arbitrary constructible complexes. Different relative dimensions are treated on the finitely many open and closed pieces of a smooth source. \(\square\)

### Smooth spreading in every generic dimension

**Lemma E.2a (the geometric reduction used in the induction).** Let \(S\) be integral and of finite type over a finite field, let \(u:X\hookrightarrow Y\) be a dense open immersion of separated finite-type \(S\)-schemes, and suppose \(X_\eta\ne\varnothing\) has dimension at most \(n\), where \(n\geq1\). After restricting \(S\) to a dense open, there is a finite, surjective, radicial map \(S'\to S\) and a dense open \(V\subset X'\), where
\[
Y'=(Y\times_SS')_{\mathrm{red}},\qquad
X'=X\times_Y Y',
\tag{E.2a}
\]
such that \(V\to S'\) is smooth and
\[
\dim(X'\setminus V)_{\eta'}<n.
\tag{E.2b}
\]
One may also make the restriction to \(V\) of a given constructible rational sheaf on \(X\) lisse. Here \(\eta'\) is the generic point of \(S'\). Different components may have different relative dimensions; no equidimensionality of \(X\) is assumed. The dimension bound is on the generic fibre, not on every special fibre.

**Proof: the generic reduced scheme.** Put \(K=\kappa(\eta)\) and \(F=K^{\mathrm{perf}}\). Let \(T=(X_F)_{\mathrm{red}}\). Constructible complexes, M.1 proves that a reduced finite-type scheme over a perfect field has a dense smooth open: its p-basis calculation constructs a separating transcendence basis, a primitive-element presentation gives a finite étale model over an affine-space open, and fraction-field comparisons identify dense opens of that model and each component. Removing the finitely many component intersections gives the result for a reducible scheme. Choose such an open \(W\subset T\), meeting every component. This is the arbitrary-dimensional assertion of M.1, not the relative-curve completion of Appendix O.

We must descend the reduction as well as this open. The field \(F\) is the filtered union of its finite purely inseparable extensions \(K_i/K\). All stages are Noetherian and all schemes here are of finite presentation, with quasi-compact overlaps. Limits of schemes, Theorem 4.1 and the closed-immersion part of Theorem 4.2 descend the specified closed immersion \(T\hookrightarrow X_F\) to a closed immersion \(T_i\hookrightarrow X_{K_i}\), together with its specified base-change identification. Write \(J_i\) for its ideal. On a finite affine cover the nilradical of \(X_F\) is generated by finitely many nilpotents, so one integer \(N\) kills its \(N\)-th power: every monomial of sufficiently large total degree contains a vanishing power of a generator. Faithful flatness of \(K_i\to F\) now gives \(J_i^N=0\). Indeed the affine ideal power becomes zero after this flat extension, and the original algebra embeds in its extension. Also \(T_i\) is reduced, since a nilpotent section maps to zero in the reduced algebra after extension to \(F\), hence was zero. Thus \(J_i\) is exactly the nilradical and
\[
T_i=(X_{K_i})_{\mathrm{red}}.
\tag{E.2c}
\]
The same reasoning holds after enlarging the finite field stage. We have not assumed that reduction commutes with an arbitrary inseparable field extension.

**Proof: retain the smooth charts.** Limits of schemes, Lemmas 2.1–2.3 descend \(W\), its finite affine cover and the covering identity. On each smooth affine chart choose a standard-smooth presentation
\[
\left(F[z_1,\ldots,z_m]/(g_1,\ldots,g_c)\right)_h,
\qquad m-c=d,
\tag{E.2d}
\]
with an invertible chosen \(c\)-column Jacobian minor. The integer \(d\) may vary from chart to chart. Existence and sufficiency of these presentations are proved in Formally smooth ring maps, Theorems 4.1 and 5.1. Keep the finitely many coefficients of the equations, the inverted element, a polynomial expression for the inverse minor, and the equation certifying that inverse. Descend the chart isomorphisms, their inverses and both identity equations by Theorem 4.1 of the limit lesson. At a common field stage all these equations and covering identities hold. The Jacobian calculation eliminates the selected \(c\) differentials and leaves the other \(m-c=d\) differentials free, with the square-zero lifting proof of the cited Theorem 4.1. Thus the descended open \(W'\subset (X_{K'})_{\mathrm{red}}\) is smooth over that finite purely inseparable field \(K'\), in every relative dimension. If an inverse is encoded by adding a variable and one equation, both counts increase by one and \(d\) is unchanged.

The map of spaces from the perfect-field model is a homeomorphism by Constructible complexes, AH.1; reduction does not change that space. Consequently \(W'\) meets every generic component. M.1's Noether-normalization dimension calculation shows that its closed complement in each component of dimension \(d\) has dimension strictly less than \(d\). Since every such \(d\leq n\), the whole complement has dimension less than \(n\). Zero-dimensional components contribute no complement. This proves the generic bound without replacing unequal component dimensions by a single fictitious dimension.

**Proof: return to a finite base change.** Work over an affine dense base \(\operatorname{Spec}A\subset S\), with fraction field \(K\). Write \(K'=K(\beta_1,\ldots,\beta_r)\) and choose \(q=p^e\) with \(\beta_j^q\in K\) for every \(j\). After clearing these denominators set \(B=A[\beta_1,\ldots,\beta_r]\subset K'\). As in Constructible complexes, O.3, the monomials with exponents less than \(q\) generate \(B\) as an \(A\)-module and \(B^q\subset A\). Lying over and the unique roots of \(Z^q-a\) in algebraically closed residue fields prove that \(\operatorname{Spec}B\to\operatorname{Spec}A\) is finite, surjective and radicial. Its generic field is \(K'\). When \(K'=K\), take \(B=A\) and \(q=1\).

Take the reduction of \(Y_B\) and its open \(X'\) as in (E.2a). Localization commutes with reduction: if an element becomes nilpotent after localization, clearing the annihilating denominator makes its multiple nilpotent before localization; the converse is immediate. Thus the generic fibre of this \(X'\) is exactly the scheme in (E.2c). Apply the same finite-open and chart descent to the system of localizations \(B_b\) with nonzero \(b\). It descends \(W'\) to an open \(V\subset X'\), and descends the chosen chart presentations, isomorphisms, inverse minors and finite covering identity. At a common localization those charts prove \(V\to\operatorname{Spec}B_b\) smooth. The hypotheses just used are checked in AH.4; smoothness here uses (E.2d), not a blanket claim that every geometric property descends.

Every further localization can retain a finite map over an open of the original base. For \(b\ne0\), invert \(b^q\in A\), because
\[
b^{-1}=b^{q-1}/b^q,\qquad
B_b=B\otimes_A A_{b^q}.
\tag{E.2e}
\]
Combine the finitely many required denominators. Remove vertical components of the reduced \(Y_B\) by shrinking this base further: there are finitely many components, and for a nondominant one the closure of its image misses the generic point. On affine charts the removal is equally the equation test \(R\otimes_BK'=0\Rightarrow R_b=0\), after clearing the equation \(1=0\), as in AH.3. Every remaining component dominates the base. Since \(V_{\eta'}\) contains each generic point of \(X'_{\eta'}\), \(V\) is now dense in \(X'\). The generic-fibre complement is still the one already bounded in (E.2b).

**Proof: coefficients and use in the induction.** Pull back the given constructible sheaf to \(X'\); it was defined on the whole original source. For each remaining generic component point choose a dense open neighbourhood inside that component on which this sheaf is lisse, using its finite constructible partition. Remove the component intersections and intersect these opens with \(V\). Their union is open in \(X'\), remains smooth over \(S'\), and contains all component generic points. Its complement in every generic component still has smaller dimension. This supplies the lisse condition and (E.2b) together. The procedure also works for finitely many constructible sheaves by intersecting their finitely many choices. No infinite coefficient system is being descended from the generic fibre, and purity is retained simply by pullback and restriction.

Finally, the maps \(Y'\to Y\) and \(X'\to X\), over the chosen base open, are finite, surjective and radicial; the latter is the base change of the former along \(u\). Proposition D.2a identifies their full coefficient categories and the actual ordinary direct-image comparisons, and preserves and detects mixed filtrations. The dense open immersion \(X'\hookrightarrow Y'\) and its source open \(V\) therefore give precisely the two smooth-source immersions used below. A further dense open of \(S'\), if needed by that argument, contains a principal open at its generic point and can again be effected over the original base by (E.2e). Thus the induction's conclusion descends to a dense open of the original \(S\). A homeomorphism of spaces alone would not justify this last sheaf-theoretic step; D.2a supplies the required equivalence and maps. \(\square\)

### Open direct image by generic-dimension induction

We prove the following assertion \(A(n)\), for every integer \(n\ge0\). Let \(S_0\) be an integral finite-type finite-field scheme with generic point \(\eta\). If \(u:X_0\hookrightarrow Y_0\) is a dense open immersion over \(S_0\), \(\dim X_\eta\le n\), and \(F_0\) is mixed, then \(Ru_*F_0\) is mixed after restricting to a dense open of \(S_0\).

Once it holds for sheaves, ordinary truncations give the same assertion for bounded mixed complexes. Factoring a locally closed immersion through its reduced closure extends the assertion to such immersions: closed direct image is exact and preserves pure grades. This extension does not assume mixedness of any new ordinary direct-image functor.

For \(n=0\), the dense open of the reduced zero-dimensional generic fibre is the whole fibre. The complement therefore has empty generic fibre, and its constructible image in \(S_0\) misses a dense open. Restrict to that open, where \(X_0=Y_0\) on the étale sites. The assertion follows. An empty generic source is disposed of in the same way.

Assume \(A(n-1)\). We first locate where mixedness might fail. Take \(S_0\) affine after shrinking, and an affine target chart with a closed embedding
\[
Y_0\hookrightarrow\mathbb A^N_{S_0}.
\tag{E.2}
\]
For each coordinate projection \(p_i:Y_0\to\mathbb A^1_{S_0}\), regard the immersion as a map over the new integral base \(\mathbb A^1_{S_0}\). Its generic source has dimension at most \(n-1\): a component on which that coordinate is transcendental loses one transcendence degree, while a non-dominant component has empty generic fibre over this new base. The induction hypothesis gives a dense open \(U_i\subset\mathbb A^1_{S_0}\) above which \(Ru_*F_0\) is mixed. Restriction to this open commutes with open direct image.

After shrinking \(S_0\), every complement \(B_i=\mathbb A^1_{S_0}-U_i\) is finite over \(S_0\). To see this explicitly, its generic fibre is a proper closed subset of the affine line. Choose a nonzero polynomial vanishing on that fibre, clear denominators and invert its leading coefficient. The complement is then contained in a monic polynomial's zero scheme, which is finite; the complement, being closed in it, is finite too. The good opens \(p_i^{-1}(U_i)\) cover all of \(Y_0\) except a closed subscheme of
\[
Y_0\cap\prod_{i=1}^N B_i,
\tag{E.3}
\]
which is finite over \(S_0\). Mixedness on their union follows from finite open-cover gluing.

We will also need this conclusion for a proper \(Y_0\). Apply the affine argument to a finite affine cover and take the union of all the good opens. The remaining closed locus has finite fibres: on each chart its fibre is contained in the corresponding finite bad fibre. As a closed locus of proper \(Y_0\), it is proper over \(S_0\). It is therefore proper and quasi-finite, hence finite. This explains why an affine-chart calculation really supplies the finite exceptional locus needed on the proper compactification.

**Smooth-source step.** Suppose now that \(X_0\) is smooth over \(S_0\) and \(F_0=L_0\) is lisse and pure. The claim is local in the target, so start with an affine target and replace it by its closure in projective space over \(S_0\). The affine target is open in this closure, and \(X_0\) stays open in it. Proving the assertion for the larger target proves it on the original one by open restriction.

Write \(b:Y_0\to S_0\) for this proper map and \(a=bu\) for the original smooth source map. The preceding argument gives a closed finite locus \(i:Z_0\hookrightarrow Y_0\) whose open complement \(v:Y'_0\hookrightarrow Y_0\) has mixed restriction of \(K=Ru_*L_0\). Apply \(Rb_*\) to ordinary localization:
\[
Rb_*v_!v^*K\longrightarrow Ra_*L_0
\longrightarrow R(bi)_*i^*K\longrightarrow.
\tag{E.4}
\]
The first term is mixed by Appendix D: extension by zero preserves mixedness, and the proper map \(b\) has \(Rb_*=Rb_!\). The second is mixed on a dense base open by Lemma E.2. Thus the third is mixed. Since \(bi\) is finite, Lemma E.1 implies that \(i^*K\) is mixed. Localization on \(Y_0\), together with the mixed \(v^*K\), now proves that \(K\) is mixed. Neither ordinary direct-image stability nor general Verdier-dual mixedness was assumed in this step.

**General-source step.** First use the input's finite mixed filtration and triangles to reduce to a pointwise pure ordinary sheaf \(F_0\). After shrinking the integral base, reduction and a finite radicial surjective base change provide a dense source open \(w:V_0\hookrightarrow X_0\) smooth over the base, with
\[
\dim(X_0-V_0)_\eta<n.
\tag{E.5}
\]
[Lemma E.2a](#smooth-spreading-in-every-generic-dimension) proves this reduction in full: it descends the reduced generic scheme, retains the standard-smooth charts in every dimension, returns to a finite radicial base change, makes \(w^*F_0\) lisse on \(V_0\) by restriction, and proves the strict generic-dimension decrease. Proposition D.2a supplies the actual direct-image and filtration comparisons. Apply them to the reduced base-changed pair, which we continue to denote by \(X_0\subset Y_0\); no coefficient system is spread from the generic fibre.

The smooth-source step, already proved at dimension \(n\), applies to both \(w\) and \(uw\). Define \(\Delta\) by
\[
F_0\longrightarrow Rw_*w^*F_0\longrightarrow\Delta\longrightarrow.
\tag{E.6}
\]
Its middle term is mixed by that step, so \(\Delta\) is mixed by the ordinary cohomology long exact sequence. Its restriction to \(V_0\) is zero. As a complex it is therefore the closed direct image of its restriction to \(X_0-V_0\). The locally closed immersion of this support into \(Y_0\) satisfies (E.5); \(A(n-1)\), with the complex extension noted above, makes \(Ru_*\Delta\) mixed after shrinking the base. In
\[
Ru_*F_0\longrightarrow R(uw)_*w^*F_0
\longrightarrow Ru_*\Delta\longrightarrow,
\tag{E.7}
\]
the last two terms are now mixed. The first is mixed as well. This proves \(A(n)\).

Take \(S_0=\operatorname{Spec}\mathbb F_q\). Its only dense open is itself, so \(A(n)\) proves mixed stability for every open immersion of the required finite-type scope. We did not deduce this by repeated restriction to closed base strata: ordinary open direct image need not commute with those base changes. The proof uses open restriction, the dense-open comparison proved in Lemma E.2 and the exact radicial equivalence in their respective places. Using the first proof of E.2 requires no generic-base-change theorem.

### Arbitrary ordinary direct image

**Theorem E.3.** If \(f:X_0\to Y_0\) is separated and of finite type, then \(Rf_*\) preserves bounded mixed complexes.

**Proof.** Mixedness is local in \(Y_0\), so restrict to an affine target. Take a finite affine open cover \(U_i\) of the source. Its finite intersections \(U_I\) are affine, because the source is separated over the affine target. In the ordinary sheaf model underlying the stated adic comparison, choose an injective resolution. Restriction to an open preserves injectives, since its left adjoint, extension by zero, is exact. Form the augmented Čech complex in each degree of the resolution. On a neighbourhood contained in one cover member, inserting that member's index contracts this complex, so it is exact. Apply direct image to the resulting double complex. Its two spectral sequences give the finite-cover spectral sequence
\[
E_1^{p,q}=\bigoplus_{|I|=p+1}R^q(f|_{U_I})_*(F_0|_{U_I})
\Longrightarrow R^{p+q}f_*F_0.
\tag{E.8}
\]
Only finitely many intersections and ordinary cohomological degrees occur. It therefore suffices to prove the assertion for an affine source mapping to an affine target.

Embed that affine source as a closed subscheme of \(\mathbb A^N_{Y_0}\), and take its closure \(\overline X_0\) in \(\mathbb P^N_{Y_0}\). This factors \(f\) as an open immersion followed by a proper map. The open theorem just proved makes the first derived image mixed; Appendix D makes the proper image mixed since proper and compact-support direct image agree. The Leray spectral sequence proves the assertion for the composite. Then (E.8), ordinary subquotient closure and the finite abutment filtration prove it for the original map. Ordinary truncations extend the sheaf result to every bounded mixed complex. \(\square\)

### Duality and the other operations

**Theorem E.4.** Verdier duality, exceptional inverse image and derived internal Hom preserve bounded mixed complexes. Together with Appendices D and E, this proves mixed stability under all the operations stated in Section 4, relative to the ordinary foundations specified there and here.

**Proof.** First prove dual mixedness by induction on the dimension of the ambient reduced scheme, for all mixed inputs on that scheme. Finite mixed filtrations and truncations reduce the step to an ordinary pure sheaf \(K\). Choose a dense smooth open \(j:U_0\hookrightarrow X_0\) on which \(L=j^*K\) is lisse, possibly zero on some components, and let \(i:Z_0\hookrightarrow X_0\) be the smaller-dimensional closed complement. Dualize the localization triangle. The ordinary exchanges give
\[
i_*D_{Z_0}i^*K\longrightarrow D_{X_0}K
\longrightarrow Rj_*D_{U_0}L\longrightarrow.
\tag{E.9}
\]
The first term is mixed by dimension induction and exact closed pushforward. On a smooth component of dimension \(d\), smooth duality gives
\[
D_{U_0}L=L^\vee(d)[2d].
\tag{E.10}
\]
Its single nonzero ordinary cohomology sheaf is pure. The last term of (E.9) is therefore mixed by the already proved open-direct-image theorem. The middle term is mixed by triangle closure. This proves dual stability without using exceptional-pullback mixedness as an input.

Ordinary pullback preserves mixedness, as does tensor product, by Appendix D. Biduality and the ordinary adjunction identities now give
\[
f^!=D_{X_0}f^*D_{Y_0},\qquad
Rf_*=D_{Y_0}Rf_!D_{X_0}.
\tag{E.11}
\]
The first proves exceptional-inverse-image stability; the second agrees with the independent direct-image proof above. Finally tensor–Hom adjunction and constructible biduality yield
\[
\begin{aligned}
D_{X_0}(K\otimes D_{X_0}L)
&=R\mathcal Hom(K\otimes D_{X_0}L,\omega_{X_0})\\
&=R\mathcal Hom(K,D_{X_0}D_{X_0}L)
=R\mathcal Hom(K,L).
\end{aligned}
\tag{E.12}
\]
The left side is mixed by the proved tensor and dual stability. This gives derived internal-Hom stability and hence mixedness of its ordinary Ext sheaves. \(\square\)

These deductions establish mixed stability before the perverse weight arguments. They use no hard Lefschetz theorem, decomposition theorem or higher-dimensional IC-purity theorem. Their use of normalized adic localization, trace and biduality is substantive: the exact operation providers linked above supply those maps, and their geometric and coefficient prerequisites are required in addition to the finite-diagram identities. Proposition E.2b supplies the precise smooth/lisse base-change input of the relative-pairing proof of Lemma E.2. E.2m supplies the general ordinary torsion generic-base-change theorem, and E.2n supplies its uniform adic/rational counterpart; neither the first proof nor the mixed-stability deduction assumes that broader theorem. In particular an arbitrary inverse limit of finite-coefficient triangles is not a substitute for the constructible adic comparison required throughout.

## Geometric and coefficient hypotheses

Appendix D derives the general compact-support estimate of Theorem 4.1 from the curve results and the stated ordinary foundations. Lemma D.2b supplies the smooth proper curve pair with finite étale boundary after the purely inseparable change and shrinking; Proposition D.2a supplies the actual radicial coefficient equivalence. Their geometric inputs remain required. The other requirements include the finite covering argument supplied by Lemma B.3a and Proposition B.3b and used in Lemma D.1a to derive the full adic fibre and monodromy-filtration comparison, and full adic constructibility, base change and Leray. Appendix E supplies the remaining mixed-stability deduction. Lemma E.2a supplies its arbitrary-dimensional geometric reduction, including nilpotents, the finite field stage, smooth charts and the strict generic-dimension decrease. Its ordinary requirements remain the smooth-orientation and dual-exchange maps, finite universal-homeomorphism invariance, the recursive algebraic providers, normalized adic localization, and constructible biduality. The exact operation providers are linked in Appendix D. The first proof of Lemma E.2 supplies its dense-open mixedness conclusion without generic base change. Proposition E.2b supplies the actual geometric-fibre comparison used in the relative-pairing proof. E.2m supplies generic base change for general finite-type morphisms and constructible ordinary left-Noetherian torsion coefficients; E.2n supplies the uniform adic/rational theorem using the actual coefficient comparison maps. The mixed-stability deduction uses these geometric and coefficient foundations and does not itself prove them. Appendix A gives the coarse and strict curve bounds, boundary monodromy grading, curve continuation and real-sheaf argument from their explicitly specified ordinary foundations. Appendix B proves the pencil geometry by explicit interpolation and incidence counts, including the étale equation of a node, and gives the transverse tame local-acyclicity deduction. Its ordinary algebraic foundations include regular local rings, dimensions of incidences and images, the Jacobian criterion, blowups and finite maps of proper curves. For the cohomological deduction, Constructible complexes, AT.1–AT.3 and AT.5 supply ordinary smooth local acyclicity through the canonical smooth comparison of AS.1–AS.7. Lemma B.3c supplies ordinary proper nearby-cycle compatibility, retaining the specialization map, its cone convention and arithmetic action. Lemma C.2a connects the completed coefficient formalism to the actual normalized specialization unit, cone and geometric fibre. Lemma B.3a and Proposition B.3b supply the general tame Kummer covering description, reusing Constructible complexes, AP.1–AP.5 and AQ.1–AQ.2 for purity and gluing. The general branchwise calculation includes covers outside the invertible-degree Galois case of AP.6–AP.7. These providers retain their stated recursive algebraic dependencies. Appendix C derives the node and boundary formulas, their arithmetic signs, the exact coefficient filtration and compact-support specialization. It uses ordinary finite proper comparison, smooth local acyclicity, projective-line cohomology with its Chern-class normalization, and normal-crossing purity for the intrinsic branch generator. Lemma B.3c identifies the ordinary proper-comparison provider. Lemma C.2a supplies the normalized comparison for these local computations using the explicit completion and coherent coefficient-diagram proofs in Constructible complexes, BK–BS. The other finite-coefficient and geometric foundations of those constructions remain required. The supplied ordinary smooth local-acyclicity proof retains its recursive curve, coefficient-continuity and algebraic inputs; the local calculation does not prove those lower inputs. Constant-coefficient curve Riemann hypothesis alone does not supply these ordinary foundations.

The cover-growth and affine-test arguments use the generic rational local-acyclicity and common-open proof supplied in A.1b–A.1o. The conductor subsection proves the full Grothendieck–Ogg–Shafarevich formula with Swan conductors, retaining exact curve-cover, canonical-degree and cohomology inputs. The prerequisites of those statements are also required. Lemma 5.G supplies the continuous Galois descent needed by the arithmetic extension formula, including its completed-coefficient and geometric-Hom comparisons. Ordinary and normalized adic constructibility, localization, trace, duality, Künneth, base change and finite-to-adic comparison retain the exact providers linked above and their recursive prerequisites; these lower geometric and coefficient results are required hypotheses. The perverse finite-length, smooth, affine and IC arguments likewise use their stated geometric foundations. The ordinary genus-one calculation used in Exercise 3 retains its stated curve-cohomology inputs. Sections 4–6 give the perverse deductions from these hypotheses; the relative Lefschetz proof lies in the linked next lesson and retains the same foundations.

## References

- P. Deligne, *La conjecture de Weil II*, Publications Mathématiques de l'IHÉS **52** (1980), 137–252: 1.3.4–1.3.13, 1.5.1–1.5.3, 1.7.8–1.7.11, 1.8.1, 1.8.4, 1.8.6–1.8.8, 3.1.1–3.1.5, 3.2.1–3.2.15, 3.3.1, 3.3.10, 3.4.1, 4.1.1, 6.1.1–6.1.11, 6.2.2–6.2.6. [Original article](https://www.numdam.org/item/PMIHES_1980__52__137_0/).
- A. Beilinson, J. Bernstein and P. Deligne, with results of O. Gabber, *Faisceaux pervers*, Astérisque **100** (1982): 5.1.2–5.1.15, 5.2.1, 5.3.1–5.3.9, 5.4.1–5.4.10. [Original volume](https://www.numdam.org/item/AST_1982__100__1_0/).
- P. Deligne and N. Katz, *SGA 7 II*, Exposés XIII, 2.1.10–2.1.11, and XVII, 1.1–1.2, 2.5: transverse tame local acyclicity and ordinary quadratic singularities. [Free primary scan at IAS](https://publications.ias.edu/sites/default/files/Number12.pdf); [Katz’s author-hosted scan](https://web.math.princeton.edu/~nmk/old/pinclef.pdf).
- *SGA 7 I*, Exposé I, 2.2–2.7 and 3.3: finite nearby cycles, specialization and the tame normal-crossing Kummer calculation. [Free primary scan at SLMath](https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf).
- The Stacks Project, Section 59.28, Lemma 59.28.1: the étale Kummer sequence and its cohomology connecting map. [Free text, tag 03PK](https://stacks.math.columbia.edu/tag/03PK).

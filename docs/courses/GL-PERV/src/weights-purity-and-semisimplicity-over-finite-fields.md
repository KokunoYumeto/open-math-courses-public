# Weights, purity and semisimplicity over finite fields

*Written and reconstructed by GPT-6.1 Sol and GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Checked by the AI writer; independent review is not claimed. Public domain (CC0).*

There are three different questions behind the word purity. What sizes can Frobenius eigenvalues have? How do those sizes change with cohomological degree? Which extensions disappear when Frobenius is forgotten? A punctured line, a unipotent matrix and a singular projective curve separate these questions. We will use their calculations to organize the weight theorems and then derive the perverse consequences.

Throughout, \(k=\mathbb F_q\), \(\ell\ne\operatorname{char}k\), and \(\Lambda=\overline{\mathbb Q}_\ell\). All schemes have finite type over \(k\); maps in the operation statements are separated. A subscript \(0\) retains the \(k\)-structure, and its omission denotes geometric base change. We use geometric Frobenius, acting on \(\Lambda(1)\) by \(q^{-1}\). Our convention is \(\mathcal H^b(K[r])=\mathcal H^{b+r}(K)\).

The sheaf tools come from Constructible complexes on algebraic varieties, [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and [Affine morphisms, Artin vanishing and perverse cohomology](affine-morphisms-artin-vanishing-and-perverse-cohomology.md). The ordinary and adic operation, trace, duality and weight foundations are specified where used. Their full prerequisite proofs remain required. Appendix A contains the curve and cover arguments supporting the perverse weight criterion. Appendix B supplies the pencil geometry. Appendix C computes its three arithmetic local contributions and the specialization sequence. Appendix D derives the general compact-support estimate by a family filtration and dimension induction. Appendix E proves mixed stability of the remaining operations, beginning with ordinary direct image before duality. Each appendix states the ordinary cohomological inputs it uses.

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
Appendix D derives (4.1) from the optimal curve estimate, constructing actual finite mixed filtrations and a decreasing dimension induction. Its ordinary foundations, and those of Appendices A–C, remain explicitly required. A further assertion is that mixed constructible categories are stable under \(f^*,f^!,Rf_*,Rf_!\), tensor product, derived internal Hom and Verdier duality. Appendix D gives mixedness for \(Rf_!\), inverse image and tensor product. Appendix E proves ordinary direct-image mixedness by a generic-dimension induction, then derives duality, exceptional inverse image and internal Hom. This order avoids assuming dual mixedness in the direct-image proof. The primary loci are Weil II, 3.3.1 and 6.1.1–6.1.11. These deductions retain the explicitly specified ordinary geometric and adic foundations as proof obligations.

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

For two heart objects, the continuous procyclic Galois calculation gives
\[
0\to\operatorname{Hom}(A,B)_F\to
\operatorname{Ext}^1(A_0,B_0)\to
\operatorname{Ext}^1(A,B)^F\to0,                            \tag{5.2}
\]
where \(V_F=\operatorname{coker}(F-1)\) and \(V^F=\ker(F-1)\). To obtain it, apply the two-term continuous Galois complex with differential \(F-1\) to geometric derived Hom. Negative geometric Hom groups vanish for heart objects, so total degree one has exactly these two terms. Heart extensions equal derived degree-one Hom: the triangle of a short exact sequence gives one direction, and perverse cohomology of a degree-one cone gives the converse. The continuous derived-descent and finite-to-adic comparison underlying this calculation are part of the ordinary foundations still required.

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

Here is the geometric package proved in Proposition B.2, together with the cohomological hypotheses still needed. After sufficient ampleness and a finite constant-field extension, a smooth projective surface with normal-crossing boundary has a pencil whose axis is transverse and disjoint from that boundary. Blowing up its finitely many axis points produces a map to \(\mathbb P^1\). Outside finitely many exceptional values its open fibres and coefficient sheaf are transversely tamely locally acyclic. Each exceptional fibre has at most one exceptional point, of one of three types: an interior ordinary node, simple tangency with a smooth boundary branch, or passage through a crossing of two boundary branches. Propositions C.1–C.3 compute the ordinary arithmetic node and both boundary configurations, including the coefficient filtration. The relevant primary loci are Weil II, 3.1.1–3.1.5 and 3.2.14. Appendix B proves the pencil geometry, including the actual étale nodal equation, and deduces transverse tame local acyclicity from explicit ordinary covering and cohomology inputs. Appendix C derives the arithmetic nodal formula from a proper conic and an intrinsic branch calculation. Smooth local acyclicity, proper comparison, projective-line cohomology, normal-crossing purity and the normalized adic formalism retain their own programme proof obligations. Neither the inequalities below nor nearby-cycle t-exactness alone supplies those foundations.

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
The upper nearby-cycle bound is proved in Nearby and vanishing cycles, independently of weights. The wild action on the fixed bounded constructible cycle object has finite image: its continuous action on its finite-dimensional endomorphism algebra preserves a lattice, and a pro-\(p\) group has trivial intersection with the pro-\(\ell\) congruence kernel. This fixed finite quotient and its ramification breaks also act on every pulled-back object and its cohomology. The definition of Swan conductor as a finite weighted sum of the codimensions of ramification-group invariants therefore bounds it by a fixed constant times the dimension in (A.17). Induction applies. This argument includes wild inertia.

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

### Vanishing away from the exceptional points

We give the transverse boundary deduction with its cohomological inputs explicit. Assume smooth local acyclicity for finite torsion coefficients of order invertible on the surface, compatibility of nearby cycles with finite or proper pushforward, and the tame Kummer covering description of a strictly local regular pair. The last description says that a finite tame local system on the complement of a smooth divisor becomes constant after a cover obtained by adjoining a prime-to-characteristic root of its boundary parameter. Its usual proof requires the ramification and purity results for finite covers; those foundations are not supplied by Proposition B.2.

**Lemma B.4.** Under these inputs, if both \(f:X\to B\) and \(D\to B\) are smooth near a point of a smooth boundary divisor, then
\[
R\Phi_f(j_!L)=0
\tag{B.9}
\]
there for every finite tame lisse sheaf \(L\) on \(X-D\). The same deduction applies to adic sheaves when normalized adic nearby cycles are compatible with their finite coefficient systems.

**Proof.** For a constant module \(M\), the sequence
\[
0\longrightarrow j_!M\longrightarrow M_X
\longrightarrow i_*M_D\longrightarrow0
\tag{B.10}
\]
reduces the claim to smooth local acyclicity on \(X,D\), using proper compatibility for the closed immersion \(i\).

Pass to the strictly local pair. Choose a Kummer cover \(g:X'\to X\), given in transverse coordinates by \(y=v^m\), which makes \(L\) constant on its open complement \(U'\); here \(m\) is prime to the field characteristic. Both \(X'\) and its boundary remain smooth over \(B\). On the complements, the adjunction map embeds \(L\) into \(g'_*g'^*L\): after the étale cover it is the diagonal map into a direct sum indexed by the cover. The cokernel is again a local system trivialized by that same cover. Iteration gives
\[
0\longrightarrow L_i\longrightarrow g'_*M_i
\longrightarrow L_{i+1}\longrightarrow0,
\qquad L_0=L,
\tag{B.11}
\]
where each \(M_i\) is constant on \(U'\). Extension by zero is exact, and \(j_!g'_*M_i=g_*j'_!M_i\). The middle term has zero vanishing cycles by (B.10) upstairs and finite proper compatibility. Thus
\[
R\Phi_f(j_!L_i)\simeq R\Phi_f(j_!L_{i+1})[-1].
\tag{B.12}
\]
For a degree-zero sheaf, the defining cone of its specialization map to \(R\Psi\) has no cohomology below degree \(-1\). Iterating (B.12) more than \(q+1\) times identifies its degree-\(q\) cohomology with a group below degree \(-1\), which is zero. This proves all degrees vanish. It does not divide by \(m\), so it is valid even when the coefficient prime divides the Kummer degree.

For an adic sheaf, choose a stable lattice and apply the finite argument to its reductions. The stated finite-to-adic compatibility carries their zero nearby-cycle cones to zero, and inverting the coefficient prime preserves zero. Alternatively, for the tame-unipotent coefficients of Appendix A, the procyclic local tame representation has a finite flag with trivial grades. Extend those grades as constant sheaves and use (B.10) successively. This shorter argument still requires the local covering description and ordinary local-acyclicity formalism. \(\square\)

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

The ordinary foundations used below are finite-coefficient proper base change, smooth local acyclicity, the specialization triangle and its étale locality, finite normalization, and the cohomology of the projective line with the degree-one Chern-class normalization. The intrinsic branch calculation additionally uses purity for a regular normal-crossing pair and the resulting acyclicity of its tower of prime-to-characteristic root covers. These foundations, and the normalized constructible adic comparison used at the end, retain their own proof obligations. No weight estimate or perverse purity theorem is an input to the local computations.

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

Smooth local acyclicity puts all vanishing cycles at \(x\). If \(V^q=\Phi_x^q(\Lambda)\), proper comparison gives
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
where the target records roots of \(t=uv\). The kernel is a single copy of \(\widehat{\mathbb Z}^{(p')}(1)\). Purity for the regular normal-crossing pair computes the cohomology of the parameter complement by its exterior Kummer classes; pulling back by the \(m\)-th root cover multiplies positive degree \(q\) by \(m^q\). Choosing arbitrarily high powers of \(\ell\) kills these classes in the direct limit. This is the ordinary purity input that makes the root tower acyclic. Hochschild–Serre then computes tame geometric nearby cohomology from the kernel in (C.10).

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

**Proof at a tangency.** In the strictly local trait the boundary map is finite of degree two and generically separable by Proposition B.2. Its geometric generic fibre is \(B\); its special fibre has one underlying geometric point. Nilpotents do not change the étale site. Finite base change gives nearby cohomology \(\Lambda^B\) in degree zero, while the specialization map is the diagonal \(\Lambda\to\Lambda^B\). Thus, for the boundary immersion \(i_D\),
\[
R\Phi_f(i_{D*}\Lambda_D)_x=\varepsilon_\Lambda(B)[0].
\]
Apply (C.1) to the exact sequence
\[
0\to j_!\Lambda\to\Lambda_X\to i_{D*}\Lambda_D\to0.
\tag{C.13}
\]
The middle term has zero vanishing cycles by smooth local acyclicity. The resulting triangle gives (C.12), with its nonzero cohomology in degree one.

In characteristic two, the boundary germ (B.6) is separable because its cubic coefficient is nonzero. Its two-point permutation action can be wildly ramified as a representation of the parameter trait. This is allowed in (C.12). The inseparable germ \(t=u^2\) would have only one geometric nearby point and cannot be substituted. Tameness of the coefficient around the boundary divisor is a separate condition from ramification of this boundary map.

**Proof at a crossing.** Write \(\nu:D'\to D\) for the boundary normalization and \(S_x=\Lambda_x\otimes\varepsilon_\Lambda(B)\). Stalkwise diagonal and quotient maps give
\[
0\to j_!\Lambda\to\Lambda_X\to\nu_*\Lambda_{D'}\to S_x\to0.
\tag{C.14}
\]
Let \(T\) be the image of its middle map. The ambient map and both normalized branch maps are smooth. Therefore \(R\Phi_f\Lambda_X=0\) and \(R\Phi_f\nu_*\Lambda_{D'}=0\), using finite proper comparison for the latter. Since \(S_x\) has zero generic restriction, (C.1) gives \(R\Phi_f S_x=S_x[1]\), concentrated in degree \(-1\). Applying vanishing cycles to the two short exact sequences defined by \(T\) gives
\[
R\Phi_f(j_!\Lambda)=R\Phi_fT[-1]
=R\Phi_fS_x[-2]=S_x[-1].
\tag{C.15}
\]
All maps respect permutations of the two branches. This proves the second formula and its arithmetic sign. \(\square\)

### Coefficient filtrations and the adic limit

**Proposition C.3.** Let \(L\) have a finite arithmetic-stable filtration on the punctured local surface whose grades extend lisse across the boundary. Denote the corresponding coefficient spaces on the strict local total scheme by \(A_m\). Its extension by zero has vanishing cycles concentrated in ordinary degree one, with a filtration whose grades are
\[
\begin{cases}
A_m(-1)\otimes\varepsilon(B),&\text{at a node},\\
A_m\otimes\varepsilon(B),&\text{at either boundary configuration}.
\end{cases}
\tag{C.16}
\]
This holds for rational-adic coefficients under the normalized finite-system comparison stated above.

**Proof.** A finite free lisse grade is constant on the strict local total scheme. Tensoring the preceding free finite-coefficient computations with its module gives the three formulas. Since extension by zero is exact, a filtration step gives a triangle of vanishing cycles. Inductively both end terms have cohomology only in degree one. Its long exact sequence is consequently the short exact sequence
\[
0\to\Phi^1(j_!F_{m-1}L)\to\Phi^1(j_!F_mL)
\to\Phi^1(j_!\operatorname{Gr}_m L)\to0.
\tag{C.17}
\]
This constructs an actual filtration with the claimed grades.

For the adic assertion choose a stable free lattice over the integers \(\mathcal O_E\) of a finite extension of \(\mathbb Q_\ell\). Intersect it with each rational filtration term. These intersections are saturated: if a nonzero integral multiple of a lattice vector lies in a rational subspace, the vector itself lies there. Their successive quotients are finite free over the discrete valuation ring. Reduction modulo \(\varpi^n\) therefore preserves exactness. The constant-grade calculations remain valid over \(\mathcal O_E/\varpi^n\), by extending the free finite complexes already computed.

Each grade cycle module is finite free over \(\mathcal O_E/\varpi^n\), and reduction is its usual surjective transition map. Induction in (C.17), lifting first in its quotient and then correcting in its submodule, proves surjectivity of the transitions for every filtration term. These systems satisfy Mittag-Leffler. Explicitly, the map \((a_n)\mapsto(a_n-r_n a_{n+1})\) on their products is surjective: given its target sequence, choose \(a_1\) and lift recursively through the surjections \(r_n\). The product description of the derived limit thus has no degree-one obstruction. Taking limits in (C.17) stays exact and creates no additional cohomological degree. Inverting \(\varpi\) and extending scalars gives (C.16). This calculation uses normalized constructible nearby cycles and their finite-stalk comparison; it does not claim that arbitrary stalks commute with arbitrary inverse limits. \(\square\)

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

The ordinary cohomological inputs are constructibility and finite amplitude of compact-support direct image, its geometric-stalk base change, localization, Leray, finite-cover trace, curve Poincaré duality with the natural forget-support pairing, and invariance under finite universal homeomorphisms. The geometric inputs are generic flatness and dimension, finite étale covers classified by fundamental groups, smooth proper curve models after finite purely inseparable extension, and spreading finitely presented geometric objects after shrinking an integral base. The relative tame boundary comparison is stated precisely below. These inputs, together with the explicitly retained foundations of Appendices A–C, still require their recursive programme proofs. They are distinct from the weight conclusion to be deduced.

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

**Lemma D.2.** With this comparison, \(R^rf_!L_0\) is mixed of weights at most \(a+r\).

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

Work on its generic curve over \(K=\mathbb F_q(Y_0)\). Over the perfection of \(K\), the reduced curve has a smooth dense open with smooth proper completion, and its finite boundary has separable residue fields. The curve-model and finite-presentation descent foundations give these objects after a finite purely inseparable extension \(K'/K\). Normalize a normal target open in \(K'\). After shrinking, this is a finite universal homeomorphism. Étale invariance and compact-support base change allow this replacement: they transport actual sheaf filtrations. At finite-field closed points the purely inseparable residue extension is trivial, so Frobenius weights are unchanged.

Spread the finite geometric data of the generic completion, open immersion and boundary over a dense target open. Shrink until the completion is smooth proper and its boundary is finite étale. The generic identification with a dense open of the covered source also spreads after shrinking; the omitted source has dimension less than \(D\). The coefficient is already defined on that source: restrict and pull it back along the identification. No claim that an arbitrary infinite adic system is finitely presented is needed. Its pro-\(\ell\) image makes the extended boundary ramification tame by the preceding inertia argument. Shrink again to obtain the relative tame comparison stated before Lemma D.2. That lemma proves (D.11) on the retained open. The lower-dimensional source and target complements, the universal-homeomorphism equivalence, and the trace retraction recover the entire relative-curve case. Each discarded complement is treated by the outer induction; no arbitrary relative-dimensional case at dimension \(D\) has been used.

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

We work in the finite-field constructible characteristic-zero étale category of this lesson. In addition to Appendix D, the ordinary inputs are bounded constructibility and generic base change for ordinary direct image, relative smooth Poincaré duality, finite universal-homeomorphism invariance, finite étale descent, open–closed localization, and constructible Verdier biduality with its functorial exchanges. The geometric inputs include generic smoothness after reduction and finite purely inseparable base change, projective closure of affine schemes, the dimension formula, and the fact that a proper quasi-finite morphism is finite. These statements carry their full adic scope. They remain ordinary foundational proof obligations; no assertion about preservation of weights by these operations is assumed.

### Mixedness can be detected after a finite map

The ordinary subquotient, extension and stratification arguments in Appendix D show that bounded mixed complexes are closed under triangles and ordinary truncations. Mixedness is also local on a finite Zariski open cover. Indeed, partition the union successively into each open's portion not already covered; these are locally closed pieces. Restrict the finite filtrations there and use extension by zero and open–closed gluing. The filtrations on overlapping opens need not coincide.

**Lemma E.1.** If \(b:T_0\to S_0\) is finite and \(b_*H\) is mixed, then the ordinary sheaf \(H\) is mixed. Consequently finite pushforward detects mixedness of bounded complexes.

**Proof.** For a finite étale map, \(H\) is a direct summand of \(b^*b_*H\). In the finite étale fibre product \(T_0\times_{S_0}T_0\), the diagonal is both open and closed. The projector onto that component gives the summand, or, on stalks, selects the summand at the given point from the finite fibre sum. Pullback preserves mixedness by the Frobenius-power calculation, so ordinary subquotient closure proves the assertion.

For a general finite map, stratify the reduced base into integral pieces and work first at a generic point. Its finite reduced source algebra is a product of finite field extensions. After a finite purely inseparable extension of the base field, the reductions of these algebras are separable. This can be seen over the perfection, then descended to a finite stage since the algebras and their separability conditions are finitely presented. Spread that finite radicial change over a normal base open. After shrinking, the reduced finite source is étale over the changed base. Finite base change and invariance of étale topoi under the radicial maps reduce to the first paragraph. At closed finite-field points those maps do not change residue fields, so the equivalence transports pure grades and finite mixed filtrations with their weights.

The omitted closed base has smaller dimension. Finite base change identifies the restricted pushforward there; induction proves mixedness on its inverse image. Open–closed gluing supplies a finite mixed filtration on all of \(H\). For a complex, finite pushforward is exact and commutes with ordinary cohomology, so apply the sheaf assertion to every nonzero cohomology sheaf. \(\square\)

### A smooth map over a dense base open

**Lemma E.2.** Let \(a:V_0\to S_0\) be smooth of pure relative dimension \(d\), with \(S_0\) integral, and let \(L_0\) be a pure lisse sheaf. On a dense open of \(S_0\), the complex \(Ra_*L_0\) is mixed.

**Proof.** The sheaf \(L_0^\vee\) is pure of the opposite weight. Appendix D makes all \(R^qa_!L_0^\vee\) mixed. There are only finitely many nonzero such sheaves and finitely many terms in their mixed filtrations. By ordinary constructibility, shrink the base until those terms and quotients are lisse. Shrink also so that the ordinary direct-image sheaves are lisse and their formation commutes with geometric fibres. Generic base change is used at this step.

The relative smooth trace pairing, with fibrewise Poincaré duality, identifies lisse sheaves as
\[
\bigl(R^ra_*L_0\bigr)^\vee
\simeq R^{2d-r}a_!(L_0^\vee)(d).
\tag{E.1}
\]
The isomorphism is a morphism of sheaves, induced by the relative trace, and is checked on the geometric fibres where both comparisons hold. The right side is mixed. Dualizing its finite lisse filtration is exact; its pure grades acquire the opposite weights. Hence \(R^ra_*L_0\) is mixed for every \(r\). This uses only duality of lisse representations and the smooth trace pairing, not mixed stability of Verdier duality on arbitrary constructible complexes. Different relative dimensions are treated on the finitely many open and closed pieces of a smooth source. \(\square\)

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
For the geometric assertion, over the perfect closure of the generic field a reduced finite-type scheme has a dense smooth locus. Its finite presentation descends to a finite purely inseparable extension; spread and shrink. Shrink \(V_0\) further so that \(w^*F_0\) is lisse. It remains pure by restriction. The universal-homeomorphism equivalence identifies the relevant étale direct images and carries their filtrations, so this change of base is legitimate.

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

Take \(S_0=\operatorname{Spec}\mathbb F_q\). Its only dense open is itself, so \(A(n)\) proves mixed stability for every open immersion of the required finite-type scope. We did not deduce this by repeated restriction to closed base strata: ordinary open direct image need not commute with those base changes. The proof uses open restriction, the stated generic comparison and the exact radicial equivalence in their respective places.

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

These deductions establish mixed stability before the perverse weight arguments. They use no hard Lefschetz theorem, decomposition theorem or higher-dimensional IC-purity theorem. Their use of normalized adic localization, generic base change, trace and biduality is substantive: checking the finite diagram shapes or writing a formal duality identity does not prove those ordinary foundations. In particular an arbitrary inverse limit of finite-coefficient triangles is not a substitute for the constructible adic comparison required throughout.

## Exact prerequisites still required

Appendix D derives the general compact-support estimate of Theorem 4.1 from the curve results and the stated ordinary foundations. Its extra requirements are smooth proper curve models after finite purely inseparable extension, geometric spreading, relative tame fibre comparison for ordinary extensions and their monodromy filtrations, and full adic constructibility, base change and Leray. Appendix E supplies the remaining mixed-stability deduction. Its ordinary requirements include generic base change for direct image, relative smooth Poincaré duality, finite universal-homeomorphism invariance, the geometric spreading and dimension statements used in its induction, normalized adic localization, and constructible biduality with the required exchanges. Those foundations still require recursive proofs; the mixed-stability deduction does not supply them. Appendix A gives the coarse and strict curve bounds, boundary monodromy grading, curve continuation and real-sheaf argument from their explicitly specified ordinary foundations. Appendix B now proves the pencil geometry by explicit interpolation and incidence counts, including the étale equation of a node, and gives the transverse tame local-acyclicity deduction. Its ordinary algebraic foundations include regular local rings, dimensions of incidences and images, the Jacobian criterion, blowups and finite maps of proper curves. The cohomological deduction still requires smooth local acyclicity, the tame Kummer covering description and its ramification/purity foundations, proper compatibility of nearby cycles, and normalized adic comparison. Appendix C derives the node and boundary formulas, their arithmetic signs, the exact coefficient filtration and compact-support specialization. It uses ordinary finite proper comparison, smooth local acyclicity, projective-line cohomology with its Chern-class normalization, and normal-crossing purity for the intrinsic branch generator. The normalized adic comparison and these finite foundations still need their recursive programme proofs. Constant-coefficient curve Riemann hypothesis alone does not supply these ordinary foundations.

The cover-growth and affine-test arguments additionally require generic constructible local acyclicity, the full Grothendieck–Ogg–Shafarevich formula with Swan conductors, and the indicated curve-cover and genus inputs. Ordinary and normalized adic constructibility, localization, trace, duality, Künneth, base change, finite-to-adic comparison and continuous Galois descent must be proved at their actual scope, including the prerequisites of linked provider lessons. The perverse finite-length, smooth, affine and IC arguments must likewise have their recursive foundations established. The ordinary genus-one calculation used in Exercise 3 retains its stated curve-cohomology inputs. Sections 4–6 give the perverse deductions from these hypotheses; the relative Lefschetz proof lies in the linked next lesson and retains the same foundations.

## References

- P. Deligne, *La conjecture de Weil II*, Publications Mathématiques de l'IHÉS **52** (1980), 137–252: 1.3.4–1.3.13, 1.5.1–1.5.3, 1.8.1, 1.8.4, 1.8.6–1.8.8, 3.1.1–3.1.5, 3.2.1–3.2.15, 3.3.1, 3.3.10, 3.4.1, 4.1.1, 6.1.1–6.1.11, 6.2.2–6.2.6. [Original article](https://www.numdam.org/item/PMIHES_1980__52__137_0/).
- A. Beilinson, J. Bernstein and P. Deligne, with results of O. Gabber, *Faisceaux pervers*, Astérisque **100** (1982): 5.1.2–5.1.15, 5.2.1, 5.3.1–5.3.9, 5.4.1–5.4.10. [Original volume](https://www.numdam.org/item/AST_1982__100__1_0/).
- P. Deligne and N. Katz, *SGA 7 II*, Exposés XIII, 2.1.10–2.1.11, and XVII, 1.1–1.2, 2.5: transverse tame local acyclicity and ordinary quadratic singularities. [Free primary scan at IAS](https://publications.ias.edu/sites/default/files/Number12.pdf); [Katz’s author-hosted scan](https://web.math.princeton.edu/~nmk/old/pinclef.pdf).
- *SGA 7 I*, Exposé I, 2.2–2.7 and 3.3: finite nearby cycles, specialization and the tame normal-crossing Kummer calculation. [Free primary scan at SLMath](https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf).
- The Stacks Project, Section 59.28, Lemma 59.28.1: the étale Kummer sequence and its cohomology connecting map. [Free text, tag 03PK](https://stacks.math.columbia.edu/tag/03PK).

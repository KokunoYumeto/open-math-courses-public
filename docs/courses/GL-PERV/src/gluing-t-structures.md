# Gluing t-structures

*Initial draft by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Main exposition and worked solutions replaced by GPT-6 Astra (OpenAI), Ultra, 5 October 2026, using the free sources specified below and the locally written constructions. The categorical and sheaf-model appendices were reconstructed on 4 October 2026. Self-checked by the writing AI. Original exposition is public domain (CC0).*

Begin with a restriction map between two vector spaces. It already exhibits the distinction that matters for gluing: the value at a boundary and the sections supported at that boundary are different objects. After computing this example, we will construct a t-structure across an arbitrary recollement, select an extension without boundary subobjects or quotients, and calculate what that selection does to monodromy around a puncture.

Our shifts satisfy \(H^q(K[m])=H^{q+m}(K)\). The categorical input consists of the triangulated-category and t-structure axioms. Appendix A derives the Hom sequences, truncation adjunctions and abelian-heart facts used in the arguments. Appendix B constructs the classical sheaf realization and its mapping complexes. These local constructions are distinct from the additional finiteness and coefficient requirements for general algebraic or étale applications in the preceding lesson.

The mathematical references for the categorical results are the [author-hosted free BBD text, §§1.3–1.4](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf) and the [free Laszlo–Olsson preprint, §2](https://www.cmls.polytechnique.fr/perso/laszlo/articleweb/faisceaux-pervers.pdf). The proofs and the two assigned geometric models are developed below; the references do not replace them.

## 1. Compute an arrow before introducing gluing

Let \(X=\{u,f\}\) have just the opens \(\varnothing,\{u\},X\). A sheaf of vector spaces over a field \(\Lambda\) is precisely one linear map \(a:C\to O\): its sections on \(X\) are \(C\), its sections on \(\{u\}\) are \(O\), and restriction is \(a\). These are also its two stalks. The point \(f\) is closed. Write \(i:\{f\}\to X\) and \(j:\{u\}\to X\).

Testing a morphism of arrows gives the following operations:

\[
\begin{gathered}
j^*(C\xrightarrow aO)=O,\qquad i^*(C\xrightarrow aO)=C,\\
j_!V=(0\to V),\quad j_*V=(V\xrightarrow1V),\quad
i_*E=(E\to0).
\end{gathered}
\tag{1.1}
\]

For instance a map from \((0\to V)\) to \((C\to O)\) is a map \(V\to O\); a map from \((C\to O)\) to \((V\to V)\) is determined by its open component \(O\to V\). This proves the two adjunctions involving \(j^*\). A map into \((E\to0)\) is a map \(C\to E\), while a map from it has image in \(\ker a\). Thus ordinary sections supported at \(f\) are \(\ker a\), not \(C\).

The support functor must be derived. Put \(I_F(E)=(E\to0)\) and \(I_U(V)=(V\xrightarrow1V)\). Both are injective arrows: Hom into them is respectively Hom from the closed or the open vector space, and a linear map extends across an inclusion by extending a basis. There is an injective resolution

\[
0\longrightarrow(C\xrightarrow aO)
\xrightarrow{((1,a),1)}I_F(C)\oplus I_U(O)
\xrightarrow{(c,o)\mapsto ac-o}I_F(O)
\longrightarrow0.
\tag{1.2}
\]

At the closed vertex its kernel is the graph of \(a\); at the open vertex it is the identity sequence. Applying support to the two injectives gives

\[
i^!(C\xrightarrow aO)=[C\xrightarrow aO]
\quad\text{in degrees }0,1.
\tag{1.3}
\]

In particular, \(i^*j_!V=0\), but \(i^!j_!V=V[-1]\). The extra degree records the missing boundary value.

For a bounded complex of arrows, resolve its terms by (1.2) and totalize. The two-column augmentation is a quasi-isomorphism: a finite filtration by the original degrees has the exact augmented rows as its successive quotients. The total terms are injective. Here is the general homotopy verification which licenses their use. If \(N\) is acyclic, \(I\) is a bounded-below injective complex, and \(b:N\to I\) is a chain map, construct \(h\) from low to high degrees. Once the preceding equation holds, prescribe
\(h^{q+1}(d_Nx)=b^q(x)-d_Ih^q(x)\) on \(\operatorname{im}d_N^q\). Acyclicity and the preceding equation make this prescription well defined. Injectivity extends it to all of \(N^{q+1}\). It gives \(b=d_Ih+hd_N\). Applying this in every shift shows that Hom into \(I\) kills acyclic cones, hence computes derived Hom and derived right adjoints.

All operations in (1.1) are exact on arrows, so their adjunctions extend to complexes. The remaining derived adjoint is (1.3). The stalkwise sequence
\(0\to(0\to O)\to(C\to O)\to(C\to0)\to0\)
and the support resolution give the two boundary triangles used next. They prove recollement for this example without invoking a general sheaf-operation theorem.

With the ordinary t-structure on each point, the glued heart will be this arrow category. Its intermediate extension of \(V\) will be \((0\to V)\), and its simple objects will be \((\Lambda\to0)\) and \((0\to\Lambda)\). Sections 2–3 will explain these conclusions and why the punctured plane gives a different extension functor.

## 2. Construct a truncation from the two pieces

Now let \(\mathcal D_U,\mathcal D,\mathcal D_F\) be triangulated categories with exact functors

\[
j_!\dashv j^*\dashv j_*,\qquad
i^*\dashv i_*\dashv i^!.
\tag{2.1}
\]

Assume \(j_!,j_*,i_*\) fully faithful, \(j^*i_*=0\), and assume that the adjunction maps occur in distinguished triangles

\[
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow,
\tag{2.2}
\]

\[
i_*i^!K\longrightarrow K\longrightarrow j_*j^*K\longrightarrow.
\tag{2.3}
\]

This is recollement. An exact functor here preserves shifts and triangles; exactness on an abelian heart will be a consequence. Full faithfulness, with the adjunctions, gives

\[
j^*j_!=j^*j_*\simeq\mathrm{id},\quad
i^*i_*=i^!i_*\simeq\mathrm{id},\quad
i^*j_!=0,\quad i^!j_*=0.
\tag{2.4}
\]

For the last identities, test by Hom: \(\operatorname{Hom}(i^*j_!A,T)=\operatorname{Hom}(A,j^*i_*T)=0\), and dually for \(i^!j_*\). Taking the identity map of the object being tested proves it is zero. The unit and counit assertions for the fully faithful functors are proved in A.1. Triangle (2.2) also shows that \(j^*,i^*\) jointly detect zero objects; (2.3) gives the corresponding statement for \(j^*,i^!\).

Choose t-structures on the two smaller categories and define

\[
\mathcal D^{\le0}=\{K:j^*K\le0,\ i^*K\le0\},
\tag{2.5}
\]

\[
\mathcal D^{\ge0}=\{K:j^*K\ge0,\ i^!K\ge0\}.
\tag{2.6}
\]

The inequalities on the right use the specified structures on \(U\) and \(F\).

**Theorem 2.1.** These subcategories form a t-structure. They form a bounded t-structure if both structures on the pieces are bounded.

**Proof.** We first construct the required cut of an arbitrary \(K\). Take the nonpositive part \(U_0=\tau_U^{\le0}j^*K\). Its inclusion and adjunction give \(j_!U_0\to K\). Complete it to

\[
j_!U_0\longrightarrow K\longrightarrow K_1\longrightarrow.
\tag{2.7}
\]

Restriction identifies \(j^*K_1\) with \(\tau_U^{\ge1}j^*K\). There can still be a nonpositive supported part. Take \(F_0=\tau_F^{\le0}i^!K_1\), map \(i_*F_0\to K_1\) by adjunction, and form

\[
i_*F_0\longrightarrow K_1\longrightarrow B\longrightarrow.
\tag{2.8}
\]

Applying \(i^!\) identifies \(i^!B=\tau_F^{\ge1}i^!K_1\); applying \(j^*\) gives \(j^*B=j^*K_1\). Hence \(B\ge1\) in (2.6). The octahedron for \(K\to K_1\to B\), written using fibres, gives

\[
A\longrightarrow K\longrightarrow B\longrightarrow A[1],
\qquad j_!U_0\longrightarrow A\longrightarrow i_*F_0\longrightarrow.
\tag{2.9}
\]

The latter triangle and (2.4) give \(j^*A=U_0\) and \(i^*A=F_0\). Thus \(A\le0\) in (2.5). This is the required truncation triangle.

Shift closure follows from shift closure on the two pieces. To prove orthogonality, take \(A\le0\), \(B\ge1\), and apply \(\operatorname{Hom}(-,B)\) to (2.2) for \(A\). The two groups adjacent to \(\operatorname{Hom}(A,B)\) are \(\operatorname{Hom}(i^*A,i^!B)\) and \(\operatorname{Hom}(j^*A,j^*B)\), both zero. This proves the last axiom. A.2 then supplies uniqueness and functoriality of the cut; arbitrary cones were only used to prove existence.

If the structures on the pieces are bounded, choose a common upper bound for \(j^*K,i^*K\) and a common lower bound for \(j^*K,i^!K\). Equations (2.5)–(2.6) give finite bounds for \(K\). No boundedness assumption was needed for the construction itself. \(\square\)

**Proposition 2.2.** The functors have the following bounds:

| Functors | Halves preserved |
|---|---|
| \(j^*,i_*\) | both |
| \(j_!,i^*\) | \(\le0\) |
| \(j_*,i^!\) | \(\ge0\) |

**Proof.** Restriction and the two closed functors have the stated bounds by (2.5)–(2.6). For the embeddings, substitute the identities (2.4) into those tests. A zero restriction satisfies either bound. \(\square\)

Following BBD, preservation of \(\le0\) is called right t-exactness; preservation of \(\ge0\) is left t-exactness. Appendix A.5 proves that a functor preserving both halves induces an exact functor on hearts. Write \(\mathcal A,\mathcal A_U,\mathcal A_F\) for those hearts and \(H_t^q\) for glued cohomology. In particular \(j^*:\mathcal A\to\mathcal A_U\) is exact. In Section 1, the upper test (2.5) is exactly ordinary stalkwise vanishing in positive degrees, so it recovers the ordinary t-structure on arrows. The lower half then agrees by the orthogonality description in A.2.

## 3. Cut away the unwanted boundary degrees

An object of \(\mathcal A\) is supported on the closed piece if its \(j^*\) is zero. These objects form a Serre subcategory: exact restriction kills their subobjects, quotients and extensions. Equations (2.2)–(2.4) identify this category with \(i_*\mathcal A_F\).

**Lemma 3.1.** For \(P\in\mathcal A\), the tests for absence of boundary quotients and subobjects are

\[
\begin{aligned}
\text{no nonzero boundary quotient of }P&\iff i^*P\le-1,\\
\text{no nonzero boundary subobject of }P&\iff i^!P\ge1.
\end{aligned}
\tag{3.1}
\]

**Proof.** Since \(i^*P\le0\) and \(i^!P\ge0\), the truncation adjunctions of A.2 imply, for \(E\in\mathcal A_F\),

\[
\begin{aligned}
\operatorname{Hom}(P,i_*E)&=\operatorname{Hom}(H_F^0i^*P,E),\\
\operatorname{Hom}(i_*E,P)&=\operatorname{Hom}(E,H_F^0i^!P).
\end{aligned}
\tag{3.2}
\]

Each nonzero map in the first line has a nonzero boundary image which is a quotient of \(P\); in the second line its image is a boundary subobject. Conversely, choose \(E\) to be the indicated degree-zero object and use its identity. Thus the relevant maps all vanish exactly when that degree-zero object vanishes, giving the two strict inequalities. \(\square\)

**Theorem 3.2.** For \(A\in\mathcal A_U\), there is an extension with neither boundary subobjects nor boundary quotients, unique up to a unique isomorphism restricting to the identity of \(A\). These extensions form an additive fully faithful functor \(j_{!*}:\mathcal A_U\to\mathcal A\).

**Construction and proof.** Start with \(j_*A\), put \(B_A=i^*j_*A\), and remove the nonnegative closed restriction: let \(P\) be the fibre of \(j_*A\to i_*\tau_F^{\ge0}B_A\). Apply the three test functors. On the open, \(j^*P=A\). On the closed piece, the maps are the truncation map of \(B_A\) and the map from zero into its upper cut, respectively. Hence
\(i^*P=\tau_F^{\le-1}B_A\) and \(i^!P=(\tau_F^{\ge0}B_A)[-1]\). The latter starts in degree 1. Thus \(P\) belongs to the glued heart and passes (3.1).

To identify it intrinsically, let \(J_!A=H_t^0j_!A\) and \(J_*A=H_t^0j_*A\). Their adjunctions on hearts are proved in A.5. Their natural comparison has image

\[
j_{!*}A=\operatorname{im}_{\mathcal A}(J_!A\longrightarrow J_*A).
\tag{3.3}
\]

For any \(E\in\mathcal A_F\), the degree bounds and adjunction give

\[
\operatorname{Hom}(J_!A,i_*E)=0,
\qquad \operatorname{Hom}(i_*E,J_*A)=0.
\tag{3.4}
\]

Therefore the image in (3.3) has neither boundary quotient nor boundary subobject. It restricts to \(A\), since restriction is exact and sends the comparison to \(1_A\). Conversely, any extension \(P'\) passing (3.1) receives and maps by adjunction as

\[
J_!A\longrightarrow P'\longrightarrow J_*A.
\tag{3.5}
\]

The first map's cokernel and the second map's kernel are boundary objects, hence zero. The composite is the comparison defining (3.3), so its image is \(P'\). This identifies the constructed fibre with (3.3).

For a map \(A\to A'\), the induced square between the two heart comparisons gives a map of their images. Any two lifts differ by a map whose image is supported on the boundary. That image is a boundary quotient of the source and a boundary subobject of the target, so it is zero. Every open map thus has exactly one lift. This proves full faithfulness, uniqueness with the stated identification, and functoriality; finite direct sums of image factorizations prove additivity. \(\square\)

**Proposition 3.3.** The construction gives the triangles

\[
j_{!*}A\longrightarrow j_*A\longrightarrow i_*\tau_F^{\ge0}B_A\longrightarrow,
\tag{3.6}
\]

\[
j_!A\longrightarrow j_{!*}A\longrightarrow i_*\tau_F^{\le-1}B_A\longrightarrow.
\tag{3.7}
\]

The first is the defining fibre triangle; applying (2.2) to that fibre gives the second. These formulas also prove that intermediate extension need not have zero stalk or costalk on the boundary. Only their indicated degrees are excluded.

In the arrow model, the comparison \((0\to V)\to(V\to V)\) is zero at the closed vertex and the identity at the open vertex. Its image is \((0\to V)\), as predicted in Section 1. This particular intermediate-extension functor is exact. We next calculate a case in which it is not.

## 4. A puncture turns the boundary into monodromy data

Take \(X=\mathbb C\), \(U=\mathbb C^*\), \(F=\{0\}\), with constructibility on these two strata and field coefficients. Put the heart of shifted local systems \(L[1]\) on \(U\), and vector spaces in degree zero on \(F\). Appendix B.2 verifies the bounded constructible recollement and the ordinary t-structures on the pieces. Theorem 2.1 therefore applies to this actual sheaf category.

Let \(V\) be the fibre of \(L\), let \(T\) be transport around a positive loop, and set \(S=T-1\). The natural puncture calculation of Lesson 1, Proposition 1.1 and Appendix A gives

\[
i^*Rj_*L[1]=[V\xrightarrow S V]\quad\text{in degrees }-1,0.
\tag{4.1}
\]

The two cuts in Section 3 now compute

\[
i^*j_{!*}L[1]=(\ker S)[1],\qquad
i^!j_{!*}L[1]=(\operatorname{coker}S)[-1].
\tag{4.2}
\]

In fact \(j_{!*}L[1]=(j_*^{\mathrm{sh}}L)[1]\): ordinary sheaf direct image has invariant stalk \(\ker S\), and the fibre in (3.6) removes the degree-zero cokernel of (4.1). For trivial monodromy this is \(\Lambda_X[1]\), whose two boundary groups are nonzero. For invertible \(S\) both disappear, and \(j_!L[1]=j_{!*}L[1]=Rj_*L[1]\).

Exercise 5 proves that the whole glued heart is the category

\[
V\xrightarrow uW\xrightarrow vV,\qquad 1_V+vu\text{ invertible},
\tag{4.3}
\]

with morphisms commuting with both arrows. It also proves that the stalk complex is \([V\xrightarrow uW]\) in degrees \(-1,0\), and the costalk is \([W\xrightarrow vV]\) in degrees \(0,1\). Thus the degree-zero forbidden groups in (3.1) become \(\operatorname{coker}u\) and \(\ker v\). Intermediate extension requires \(u\) surjective and \(v\) injective. The monodromy is \(T=1+vu\), and the four extensions have the concrete forms

| Extension of \(L[1]\), or a boundary object | \(W\) | \(u\) | \(v\) |
|---|---|---|---|
| \(j_!L[1]\) | \(V\) | \(1\) | \(S\) |
| \(Rj_*L[1]\) | \(V\) | \(S\) | \(1\) |
| \(j_{!*}L[1]\) | \(\operatorname{im}S\) | \(S\), with that codomain | inclusion |
| \(i_*E\), with \(V=0\) | \(E\) | \(0\) | \(0\) |

Now choose \(V=\Lambda e_1\oplus\Lambda e_2\) with \(S(e_1)=0\), \(S(e_2)=e_1\). Since \(S^2=0\), \(T=1+S\) is invertible. Its invariant line and its quotient have trivial monodromy, giving

\[
0\longrightarrow L_1\longrightarrow L\longrightarrow L_1\longrightarrow0.
\tag{4.4}
\]

After intermediate extension, the open vector spaces still form this exact sequence, but their \(W\)-spaces are \(0,\Lambda e_1,0\). Componentwise homology is therefore \((V=0,W=\Lambda)\), the nonzero skyscraper at the origin. The exact sequence loses exactness only in the middle. This uses the diagram equivalence proved below, including its abelian-category assertion, rather than interpreting an ordinary sheaf-stalk calculation as exactness in a perverse heart.

## 5. What restriction detects in the glued heart

**Proposition 5.1.** Every simple object is either \(i_*E\), with \(E\) simple in \(\mathcal A_F\), or \(j_{!*}A\), with \(A\) simple in \(\mathcal A_U\). Both constructions give simple objects, and no finite-length assumption is needed.

**Proof.** Subobjects and quotients of a boundary object stay on the boundary, where \(i_*\) is an equivalence. This proves the first family. If \(Q\subset j_{!*}A\) and \(A\) is simple, exact restriction makes \(j^*Q\) either zero or all of \(A\). The first case makes \(Q\) a forbidden boundary subobject; the second makes its quotient a forbidden boundary quotient. Thus \(j_{!*}A\) is simple.

Conversely, a simple \(P\) killed by restriction is in the first family. If \(j^*P\ne0\), it has no nonzero boundary subobject or quotient, since simplicity would force either to be \(P\). Theorem 3.2 identifies it with \(j_{!*}A\), \(A=j^*P\). Given a nonzero subobject \(A'\subset A\), its adjoint map \(J_!A'\to P\) is nonzero and hence surjective. Restricting shows that the inclusion \(A'\to A\) is also surjective, so \(A'=A\). This proves simplicity of \(A\). \(\square\)

For finite-dimensional arrows, this gives the two one-dimensional vertex objects listed in Section 1. In the puncture heart it gives the skyscrapers with one-dimensional fibre and intermediate extensions of irreducible local systems. These are classifications by the two hearts, not assertions that every object in an arbitrary recollement has finite length.

**Proposition 5.2.** The functor \(j_{!*}\) preserves monomorphisms and epimorphisms. For an exact sequence \(0\to A\to B\to C\to0\), its only possible failure of exactness is a middle homology object supported on the boundary. This failure occurs in (4.4).

**Proof.** The kernel of an extended monomorphism restricts to zero and is a boundary subobject of an intermediate extension, so vanishes. The cokernel of an extended epimorphism is a boundary quotient and vanishes. Additivity and functoriality make the two successive extended arrows have zero composite. Restriction is exact, so it kills their middle homology. The explicit calculation following (4.4) proves that this remaining boundary object need not vanish. \(\square\)

## 6. Exercises and solutions

**Exercise 1 (easy: derive localization).** For a closed inclusion \(i:F\to X\) and its open complement \(j\), verify the recollement identities for classical sheaves with field coefficients in \(D^+\). Give both triangles explicitly for the two-point space of Section 1.

**Solution.** Appendix B.1 provides the injective models and triangle conventions. On sheaves, extension by zero and restriction give \(0\to j_!j^*E\to E\to i_*i^*E\to0\), since its stalk at a point of either piece is the identity sequence. The section adjunctions give \(j_!\dashv j^*\dashv j_*\) and \(i^*\dashv i_*\dashv i^!_{\mathrm{sh}}\). Appendix B.2 proves that, on an injective sheaf, \(0\to i_*i^!_{\mathrm{sh}}E\to E\to j_*j^*E\to0\) is exact, including surjectivity: injectivity supplies the needed local lifts. Restriction of an injective is injective because its left adjoint is exact. Applying these sequences to injective complexes gives (2.2)–(2.3) and the derived adjunctions. The full-faithfulness and vanishing identities follow by restriction or by the Hom tests in Section 2.

For an arrow \(a:C\to O\), the first triangle comes from \(0\to(0\to O)\to(C\to O)\to(C\to0)\to0\). The map to \(j_*j^*\) is \((a,1):(C\to O)\to(O\to O)\). Its fibre has a contractible open component and closed component \([C\xrightarrow aO]\) in degrees \(0,1\). This is \(i_*i^!\) by (1.3), giving the second triangle and its actual attaching map. The statements concern the categories just constructed; restriction to a broader constructible category additionally needs the relevant finiteness proofs of Lesson 1.

**Exercise 2 (easy: calculate the defect).** Apply intermediate extension to (4.4). Calculate its two arrows and its middle homology in the perverse heart.

**Solution.** The two rank-one end objects have \(V=\Lambda\), \(W=0\). The middle object has \(V=\Lambda^2\), \(W=\Lambda\), \(u(e_1)=0\), \(u(e_2)=1\), \(v(1)=e_1\). The first map sends \(1\) to \(e_1\) on \(V\) and is zero on \(W\). The second sends \(e_1\) to zero and \(e_2\) to \(1\), again with zero map on \(W\). They commute with \(u,v\). Their composite is zero, the first is monic and the second epic, using the componentwise kernels and cokernels proved in Exercise 5. Kernel modulo image is \((0,\Lambda,0,0)\). It is \(i_*\Lambda\), so this is a failure of exactness, not merely a failure of surjectivity of some ordinary stalk map.

**Exercise 3 (medium: the two cuts).** Derive (3.6)–(3.7) and determine why \(-1\) and \(1\), rather than \(0\), occur in the boundary tests.

**Solution.** Set \(B=i^*j_*A\) and take the fibre \(P\) of \(j_*A\to i_*\tau_F^{\ge0}B\). On the open the second term vanishes, hence \(j^*P=A\). Applying \(i^*\) gives the fibre of the truncation map \(B\to\tau_F^{\ge0}B\), so \(i^*P=\tau_F^{\le-1}B\). Applying \(i^!\) gives the fibre of \(0\to\tau_F^{\ge0}B\), namely \((\tau_F^{\ge0}B)[-1]\), which starts in degree 1. Lemma 3.1 and Theorem 3.2 identify \(P=j_{!*}A\). Its defining triangle is (3.6); its first localization triangle is (3.7). Allowing degree zero in the stalk would allow the boundary quotient detected by \(H_F^0i^*P\); allowing it in the costalk would allow the boundary subobject detected by \(H_F^0i^!P\).

**Exercise 4 (medium: maps versus sequences).** Prove preservation of injections and surjections by \(j_{!*}\), and locate any defect in the middle of an extended short exact sequence.

**Solution.** Exact restriction sends the kernel of an extended injection to zero. That kernel is a boundary subobject of the source intermediate extension, hence zero. The dual argument for the cokernel proves preservation of surjections. For \(0\to A\to B\to C\to0\), form in \(\mathcal A\) the quotient \(\ker(j_{!*}B\to j_{!*}C)/\operatorname{im}(j_{!*}A\to j_{!*}B)\). The denominator is a subobject of the numerator because the composite vanishes. Exact restriction sends this quotient to zero, so it is in \(i_*\mathcal A_F\). Exercise 2 calculates a nonzero example. Preservation of the two kinds of maps therefore does not imply preservation of exact sequences.

**Exercise 5 (hard: recover the two-arrow category).** Prove the equivalence (4.3) for the perverse heart on \((\mathbb C,\mathbb C^*,\{0\})\). Include the reconstruction of sheaves, all morphisms, and the stalk and costalk formulas.

**Solution.** We proceed through attaching complexes so that both objects and morphisms retain their derived information. For an open complex \(Q\), put \(B_Q=i^*Rj_*Q\). A closed-stalk complex \(A\), together with a map

\[
a:A\longrightarrow B_Q,
\tag{6.1}
\]

produces the sheaf complex

\[
K(a)=\operatorname{Fib}\left(Rj_*Q\oplus i_*A
\xrightarrow{\mathrm{res}-i_*a}i_*B_Q\right).
\tag{6.2}
\]

Use the injective representatives and signed fibre of B.1–B.3. Restriction to the open gives \(Q\). On the closed stalk, the arrow in (6.2) is \((1,-a):B_Q\oplus A\to B_Q\); its fibre contracts to \(A\). On the closed costalk the first summand vanishes, giving \(i^!K(a)=\operatorname{Fib}(a)\). Conversely the two adjunction maps from any \(K\) to its open direct image and closed stalk give (6.1) and a comparison to (6.2). It is an isomorphism on the open and the closed stalk, hence an isomorphism by (2.2).

The morphism calculation must remember homotopies. Appendix B.3 proves on the injective models that the mapping complex between two such objects is

\[
\operatorname{Fib}\left(
R\operatorname{Hom}_U(Q,Q')\oplus R\operatorname{Hom}_{\Lambda}(A,A')
\xrightarrow{(b,g)\mapsto B_ba-a'g}
R\operatorname{Hom}_{\Lambda}(A,B_{Q'})
\right).
\tag{6.3}
\]

Its degree-zero cocycle includes a homotopy between the two composites in the attaching square. Taking only commuting squares in a triangulated category would discard this datum. In particular, the first summand in (6.3) is the full derived open Hom, not just local-system maps.

For a heart object, \(Q=L[1]\), so \(B_Q=[V\xrightarrow SV]\) in degrees \(-1,0\), with \(1+S\) invertible. The heart inequalities say \(A\le0\) and \(\operatorname{Fib}(a)\ge0\). The fibre sequence then shows that \(H^qA=0\) for \(q<-1\), and that \(H^{-1}(a)\) is injective. Over a field choose a two-term representative \(A=[E\xrightarrow dF]\) in degrees \(-1,0\), with attaching chain map \((a_{-1},a_0)\). It satisfies \(a_0d=Sa_{-1}\) and \(\ker d\cap\ker a_{-1}=0\).

Replace the two closed-stalk terms by a single quotient construction:

\[
\begin{gathered}
W=(F\oplus V)/\{(dx,-a_{-1}x):x\in E\},\\
u(y)=[(0,y)],\qquad v[(z,y)]=a_0z+Sy.
\end{gathered}
\tag{6.4}
\]

The relation is sent to zero by \(v\), and \(vu=S\). Thus \(1+vu\) is invertible. There is a new attaching complex

\[
A'=[V\xrightarrow uW],\qquad
a'=(1,v):A'\longrightarrow[V\xrightarrow SV].
\tag{6.5}
\]

The map from the old complex to the new one is \((a_{-1},z\mapsto[(z,0)])\). It respects the differentials and attaching maps. Its cokernel cohomology map is the identification \(F/dE=W/uV\). Its kernel cohomology map is also bijective: if \(u(y)=0\), then \((0,y)=(dx,-a_{-1}x)\) for some \(x\in\ker d\), so \(-x\) maps to \(y\); injectivity follows from \(\ker d\cap\ker a_{-1}=0\). It is therefore a quasi-isomorphism. This puts every heart object into the two-arrow form.

Conversely start with \(u,v\) as in (4.3), form the local system with monodromy \(T=1+vu\), and insert (6.5) into (6.2). The stalk is \([V\xrightarrow uW]\) in degrees \(-1,0\). To compute its costalk, the fibre of \((1,v)\) has terms \(V,W\oplus V,V\), with maps \(y\mapsto(uy,y)\) and \((w,x)\mapsto vw-Sx\). The coordinate change \((w,x)\mapsto(w-ux,x)\) splits off an identity complex and leaves

\[
i^!K=[W\xrightarrow vV]\quad\text{in degrees }0,1.
\tag{6.6}
\]

Thus this reconstructed object satisfies both heart inequalities. This proves essential surjectivity with the actual support differential. The second endomorphism \(1_W+uv\) is automatically invertible, with inverse \(1_W-u(1_V+vu)^{-1}v\), as expansion of either product shows.

It remains to compute all maps, rather than only construct some of them. B.4 compares the angular model of (4.1) with the injective boundary model and proves that the resulting finite mapping fibre has the same \(H^0\) as (6.3). The justification uses vanishing of negative open Ext groups; it does not remove positive Ext groups from the full derived mapping complex. A degree-zero representative consequently consists of an open map \(b:V\to V'\), \(bS=S'b\), a chain map \(g\) between (6.5)'s stalk complexes, and \(h:W\to V'\) satisfying

\[
b-g_{-1}=hu,\qquad
bv-v'g_0=S'h,\qquad g_0u=u'g_{-1}.
\tag{6.7}
\]

Set \(\beta=g_0+u'h\). The three equations become \(\beta u=u'b\) and \(v'\beta=bv\), precisely the two-arrow morphism conditions. A degree-minus-one boundary is specified by \(r:W\to V'\) and changes \((g_{-1},g_0,h)\) by \((ru,u'r,-r)\). It leaves \((b,\beta)\) fixed. Taking \(r=h\) yields the unique representative with \(h=0\), \(g_{-1}=b\), \(g_0=\beta\). Conversely every commuting pair supplies this representative. B.4 checks that these are all the degree-minus-one identifications, including those arising from the injective model. The correspondence on Hom sets is therefore bijective. The representatives with zero homotopy compose as commuting pairs, proving compatibility with composition.

Finally, the finite-dimensional diagram category is abelian. Compute a kernel or cokernel at both vector spaces; the commuting arrows induce its two arrows. Invertible \(1+vu\) restricts to an invertible map on each invariant kernel and induces an invertible map on the quotient: in finite dimension its injective restriction is surjective, and the quotient follows. Thus the invertibility condition persists. The additive equivalence with the heart is consequently an equivalence of abelian categories. Equations (6.5)–(6.6) give

\[
H^{-1}i^*K=\ker u,\quad H^0i^*K=\operatorname{coker}u,
\quad H^0i^!K=\ker v,\quad H^1i^!K=\operatorname{coker}v.
\]

For extension by zero take \(A=0\) before normalization; (6.4) gives \(u=1,v=S\). For direct image take \(A=B_Q\) with identity attachment; it gives \(u=S,v=1\). The intermediate image then has \(W=\operatorname{im}S\), with \(u\) surjective and \(v\) injective. A boundary object has \(V=0\). This proves every row of the table in Section 4. A small disc gives the same category because its puncture has the same monodromy and boundary comparison. The later lesson on nearby and vanishing cycles interprets these two vector spaces geometrically; that interpretation has not been assumed in this construction.

## Appendix A. The categorical proofs used in gluing

This appendix works in an additive triangulated category \(\mathcal T\). Its specified structure is the shift \([1]\), the class of distinguished triangles, and the triangle axioms: identity triangles, completion of a morphism to a triangle, rotation, completion of a commuting square to a triangle map, and the octahedral axiom. The recollement functors of Section 2 are additional specified data, with the adjunctions and triangles stated there. No claim that a particular sheaf category has these data follows merely from this abstract setup.

### A.1. Exact Hom sequences and detection of isomorphisms

For a distinguished triangle \(X\xrightarrow fY\xrightarrow gZ\to X[1]\), consecutive arrows compose to zero. For \(gf=0\), apply the triangle-map axiom to the identity triangle \(X\xrightarrow1X\to0\to X[1]\), with first component \(1_X\) and second component \(f\). Its next square says precisely \(gf=0\). Rotation gives the other composites.

If \(h:T\to Y\) satisfies \(gh=0\), consider the commuting square whose top row is \(T\to0\), bottom row is \(Y\xrightarrow gZ\), and vertical arrows are \(h,0\). Complete it to a map from the distinguished triangle \(T\to0\to T[1]\xrightarrow{-1}T[1]\) to the rotated triangle \(Y\to Z\to X[1]\xrightarrow{-f[1]}Y[1]\). Its third component \(c:T[1]\to X[1]\) satisfies \(f[1]c=h[1]\). Hence \(h=f(c[-1])\). This proves exactness at \(\operatorname{Hom}(T,Y)\). Shifting and rotating gives the full covariant Hom sequence. Applying the same argument in the opposite category, whose shift is \([-1]\), gives the contravariant Hom sequence.

These sequences also detect isomorphisms. If \(X\to Y\to Z\to\) is distinguished and \(Z=0\), then every map \(\operatorname{Hom}(T,X)\to\operatorname{Hom}(T,Y)\) is bijective. At \(T=Y\) choose a right inverse; injectivity at \(T=X\) makes it a left inverse. Conversely, if \(X\to Y\) is invertible, exactness makes \(\operatorname{Hom}(T,Z)=0\) for every \(T\), and taking \(T=Z\) gives \(Z=0\).

For later use, an adjunction \(F\dashv G\) with fully faithful \(F\) has invertible unit \(A\to GFA\). Indeed adjunction and full faithfulness identify
\(\operatorname{Hom}(T,GFA)\) with \(\operatorname{Hom}(FT,FA)\) and then \(\operatorname{Hom}(T,A)\); under these identifications the unit induces the identity. The preceding inverse argument proves it is an isomorphism. The dual argument gives an invertible counit when the right adjoint is fully faithful. This proves the first four identities of (2.4) from the stated recollement hypotheses.

### A.2. Truncations, degree bounds and their uniqueness

Write \(\mathcal T^{\le n}=\mathcal T^{\le0}[-n]\) and \(\mathcal T^{\ge n}=\mathcal T^{\ge0}[-n]\). A t-structure means that these full subcategories are nested in the indicated directions, that
\(\operatorname{Hom}(\mathcal T^{\le0},\mathcal T^{\ge1})=0\), and that every \(X\) admits a distinguished triangle \(L\to X\to R\to L[1]\) with \(L\le0\), \(R\ge1\). Shift this requirement to any cut \(n\).

For \(T\le n\), the Hom sequence of such a triangle has zero terms \(\operatorname{Hom}(T,R[-1])\) and \(\operatorname{Hom}(T,R)\), because \(R[-1]\ge n+2\). Thus

\[
\operatorname{Hom}(T,L)\simeq\operatorname{Hom}(T,X).
\tag{A.1}
\]

For \(T\ge n+1\), the dual sequence has zero terms \(\operatorname{Hom}(L,T)\) and \(\operatorname{Hom}(L[1],T)\), so
\(\operatorname{Hom}(R,T)\simeq\operatorname{Hom}(X,T)\). These universal properties define \(L=\tau^{\le n}X\) and \(R=\tau^{\ge n+1}X\), including their arrows. For a morphism \(X\to X'\), they supply unique compatible maps of the first and third objects. Uniqueness gives compatibility with identities and compositions. The triangle-map axiom shows that these maps also commute with the connecting arrows. In particular, for two choices of truncation triangle they give a unique triangle isomorphism with identity on \(X\); no functorial choice of arbitrary cones has been used.

An object already in \(\mathcal T^{\le n}\) represents its own restricted Hom functor, so its lower truncation is itself and its upper truncation is zero. Dually for the upper half. Moreover

\[
\mathcal T^{\le n}={}^{\perp}\mathcal T^{\ge n+1},
\qquad
\mathcal T^{\ge n}=(\mathcal T^{\le n-1})^{\perp}.
\tag{A.2}
\]

For the first converse, if all \(\operatorname{Hom}(X,T)\) with \(T\ge n+1\) vanish, take \(T=\tau^{\ge n+1}X\). The upper adjunction identifies this zero group with its endomorphisms; its identity is zero. The truncation triangle now puts \(X\le n\). The second converse is dual. Applying the exact Hom sequences to (A.2) proves that each half is closed under extensions. These orthogonal descriptions also prove closure under zero objects, finite direct sums and summands, so their intersection is additive.

The adjunctions give nested truncations and shift comparisons by their universal properties. For the mixed comparison, let \(a\le b\) and form the maps
\(P=\tau^{\le a-1}X\to Q=\tau^{\le b}X\to X\). Their octahedron has triangles

\[
P\to Q\to M\to P[1],\qquad
M\to\tau^{\ge a}X\to\tau^{\ge b+1}X\to M[1].
\tag{A.3}
\]

The first and extension closure give \(M\le b\); rotate the second to obtain \(M\ge a\). Hence the first is the upper truncation of \(Q\) at \(a\), and the second is the lower truncation of \(\tau^{\ge a}X\) at \(b\). The uniqueness just proved identifies
\(M=\tau^{\ge a}\tau^{\le b}X=\tau^{\le b}\tau^{\ge a}X\), with canonical comparison maps. If \(a>b\), both composites vanish by the degree bounds. In particular
\(H_t^0X=\tau^{\ge0}\tau^{\le0}X=\tau^{\le0}\tau^{\ge0}X\) lies in the heart, and \(H_t^rX=H_t^0(X[r])\). For \(X\le0\), its truncation triangle reads \(\tau^{\le-1}X\to X\to H_t^0X\to\); for \(X\ge0\), it reads \(H_t^0X\to X\to\tau^{\ge1}X\to\). Consequently, for a heart object \(T\),

\[
\begin{aligned}
\operatorname{Hom}(X,T)&=\operatorname{Hom}(H_t^0X,T)&& (X\le0),\\
\operatorname{Hom}(T,X)&=\operatorname{Hom}(T,H_t^0X)&& (X\ge0).
\end{aligned}
\tag{A.4}
\]

Both equalities follow from the two adjacent zero Hom terms, not from a general adjunction between the whole category and its heart.

### A.3. Kernels, cokernels and the abelian heart

Let \(f:A\to B\) be a morphism of heart objects, and choose \(A\to B\to C\to A[1]\). Extension closure places \(C\) in degrees \([-1,0]\). Put \(K=H_t^{-1}C\) and \(Q=H_t^0C\). For a heart object \(T\), the exact Hom sequence and \(\operatorname{Hom}(T,B[-1])=0\) identify
\(\operatorname{Hom}(T,C[-1])\) with the kernel of \(\operatorname{Hom}(T,A)\to\operatorname{Hom}(T,B)\). Since \(C[-1]\ge0\), (A.4) identifies this with \(\operatorname{Hom}(T,K)\). Thus the induced arrow \(K\to A\) is the kernel of \(f\). Dually \(\operatorname{Hom}(A[1],T)=0\) and (A.4) identify \(B\to Q\) as its cokernel. This proves their universal properties, hence independence of the chosen cone.

It remains to prove that image equals coimage. Complete \(B\to Q\) to a triangle \(I\to B\to Q\to I[1]\), and compare \(B\to C\to Q\) by the octahedral axiom. The other cone is the truncation triangle \(K[1]\to C\to Q\to K[2]\). The resulting triangles and factorization are

\[
K\longrightarrow A\longrightarrow I\longrightarrow K[1],
\qquad I\longrightarrow B\longrightarrow Q\longrightarrow I[1],
\qquad f=(A\to I\to B).
\tag{A.5}
\]

The first triangle places \(I\le0\), using \(A\le0\) and \(K[1]\le-1\). Rotate the second to \(Q[-1]\to I\to B\to Q\); it places \(I\ge0\). Thus \(I\) is in the heart. The kernel/cokernel calculation above, now applied to these two triangles, identifies \(I\) both as the cokernel of \(K\to A\) and as the kernel of \(B\to Q\). Their induced factorization is that of \(f\), so the canonical coimage-to-image map is an isomorphism. This is the defining abelian-category property, with additivity, kernels and cokernels already proved.

A distinguished triangle with three heart terms is a short exact sequence: the same Hom sequences show directly that its first map is the kernel of its second and its second is the cokernel of its first. Conversely, given a short exact sequence \(0\to A\to B\to Q\to0\), complete \(A\to B\) to a cone \(C\). Its two possible heart cohomology objects are its kernel, zero, and its cokernel, \(Q\), by the preceding calculation. Its truncation triangle identifies \(C\) with \(Q\), with the specified arrow from \(B\). Thus the short exact sequence comes from a distinguished triangle. These statements require no boundedness of the ambient t-structure: only this cone lies in a finite interval.

### A.4. Cohomology of every triangle is exact

Consider \(X\to Y\to Z\to X[1]\). If all three objects are at least zero, (A.4) converts the exact Hom sequence on every heart test object \(T\) into the kernel universal property for
\(0\to H_t^0X\to H_t^0Y\to H_t^0Z\). This sequence is therefore exact in the abelian heart.

The same conclusion holds if only \(Z\ge0\). For every \(T\le-1\), the groups \(\operatorname{Hom}(T,Z)\) and \(\operatorname{Hom}(T,Z[-1])\) vanish. Adjunction consequently identifies \(\tau^{\le-1}X\to\tau^{\le-1}Y\) as an isomorphism. Apply the octahedral axiom to the common lower part \(P\to X\to Y\). The cones of the first map and the composite are \(\tau^{\ge0}X\) and \(\tau^{\ge0}Y\), while the cone of the second map is \(Z\). The remaining triangle is
\(\tau^{\ge0}X\to\tau^{\ge0}Y\to Z\to\). All its terms are at least zero, so the previous paragraph applies. The mixed-cut identities in A.2 identify its degree-zero cohomology maps with the original ones. In the opposite category this proves the dual assertion: if \(X\le0\), then \(H_t^0X\to H_t^0Y\to H_t^0Z\to0\) is exact.

For general \(X\), let \(U=\tau^{\le0}X\), \(V=\tau^{\ge1}X\). The octahedron of \(U\to X\to Y\) gives
\(U\to Y\to W\to U[1]\) and \(V\to W\to Z\to V[1]\). Since \(U\le0\), the dual assertion gives an exact sequence
\(H_t^0X\to H_t^0Y\to H_t^0W\to0\). Rotate the second triangle to \(W\to Z\to V[1]\to\). Its third term is at least zero; the other assertion makes \(H_t^0W\to H_t^0Z\) injective. The octahedron identifies the composite \(Y\to W\to Z\) with the original map, so the kernel at \(H_t^0Y\) is exactly the image of \(H_t^0X\). Shifts and rotations now prove the entire exact sequence

\[
\cdots\to H_t^rX\to H_t^rY\to H_t^rZ
\to H_t^{r+1}X\to\cdots.
\tag{A.6}
\]

Its connecting map is the actual triangle arrow followed by the cohomology functor. The naturality established in A.2 makes (A.6) natural for triangle maps. No assumption that all cohomology objects detect arbitrary unbounded objects has entered the proof.

### A.5. Exact functors on hearts and their adjunctions

Let \(F:\mathcal T\to\mathcal T'\) preserve distinguished triangles and shifts. If it preserves both t-structure halves, it sends a truncation triangle at any cut to a triangle with the same degree bounds. A.2 then identifies it uniquely with the truncation triangle of \(FX\). Thus \(F\) commutes with both truncations and all \(H_t^r\). For a short exact heart sequence, A.3 supplies its distinguished triangle; the image has three heart terms and is short exact by the same paragraph. Hence \(F\) restricts to an exact heart functor.

If only the upper half is preserved, \(F_\heartsuit=H_{t'}^0F\) is right exact on hearts: applying (A.6) to a short exact heart triangle gives the sequence
\(F_\heartsuit A\to F_\heartsuit B\to F_\heartsuit C\to H_{t'}^1FA=0\). If only the lower half is preserved, the preceding term \(H_{t'}^{-1}FC\) instead vanishes, proving left exactness. These are precisely the degree-bound meanings of right and left t-exactness used in Proposition 2.2.

For an adjunction \(L\dashv R\) of exact triangulated functors, preservation of the upper half by \(L\) is equivalent to preservation of the lower half by \(R\). If \(Y\ge0\) and \(T\le-1\), then \(\operatorname{Hom}(T,RY)=\operatorname{Hom}(LT,Y)=0\); (A.2) proves the first implication. Conversely, if \(X\le0\) and \(Z\ge1\), the equality \(\operatorname{Hom}(LX,Z)=\operatorname{Hom}(X,RZ)=0\) and (A.2) prove the other. In this situation, for heart objects \(A,B\), (A.4) gives

\[
\operatorname{Hom}(H_{t'}^0LA,B)
=\operatorname{Hom}(LA,B)
=\operatorname{Hom}(A,RB)
=\operatorname{Hom}(A,H_t^0RB).
\tag{A.7}
\]

All comparisons come from the original units or counits, so they are natural. This proves the heart adjunction. Applied to the functors in Proposition 2.2, it proves the adjoint heart maps used in (3.2), (3.4), (3.5) and Proposition 5.1. Applied to \(j^*\) and \(i_*\), the first paragraph proves the exactness used for boundary subobjects, quotients and the classification of simples.

The free BBD text, §§1.1–1.4, supplies the mathematical source for this categorical reconstruction; the free Laszlo–Olsson paper, §2, records the general recollement setup. The proofs above spell out the required arguments. Neither reference substitutes for a proof in this lesson, and neither gives clearance for its still unfinished geometric prerequisites.

## Appendix B. The sheaf model behind the puncture diagrams

Here \(\Lambda\) is a field and sheaves mean sheaves of \(\Lambda\)-vector spaces in the classical topology. We construct the bounded-below derived realization of open-closed recollement, then its bounded two-stratum realization on a disc or plane. The categorical theorem in Section 2 still has its unrestricted triangulated scope. This appendix does not supply the separate étale, adic or general algebraic finiteness theorems used elsewhere in the course.

### B.1. Complexes, resolutions and triangle signs

For complexes, use

\[
\operatorname{Hom}^n(E,F)=\prod_p\operatorname{Hom}(E^p,F^{p+n}),
\qquad d(f)=d_Ff-(-1)^nf d_E.
\tag{B.1}
\]

Thus degree-zero cocycles are chain maps and boundaries are chain homotopies. The first lesson’s Appendices A.1 and B.1–B.2 now contain the complete classical resolution and localization foundations before their uses. The following recalls their complex model. In particular they give the exact injective functor
\(G(F)=\prod_x(e_x)_*F_x\) and its natural monomorphism \(F\to G(F)\). Exactness of \(G\) can be tested even on sections: its maps are products of exact stalk sequences of vector spaces. Let \(C(F)\) be the cokernel of this monomorphism. The diagram of the two exact rows \(0\to F\to G(F)\to C(F)\to0\), applied to a short exact sequence of \(F\)'s, shows that \(C\) is exact: injectivity at the left follows by subtracting a lift from \(F\), surjectivity at the right by lifting in \(G(F)\), and the same subtraction proves equality of image and kernel in the middle. This is a stalkwise argument.

The functors \(G C^q\), for \(q\ge0\), therefore give an additive functorial injective resolution of every sheaf. For a complex \(E\) zero below degree \(a\), apply these resolutions to every \(E^p\). Totalize with the differential \(d_E+(-1)^p d_{\mathrm{res}}\) on the component \(G C^q(E^p)\). In total degree \(n\), only \(a\le p\le n\) occur, so every term is a finite sum of injectives. Denote this complex by \(I(E)\).

The map \(E\to I(E)\) is a quasi-isomorphism. In its augmented double complex, the resolution direction is exact. For a total cocycle, begin with its smallest original degree \(p\). Exactness in the resolution direction allows that component to be removed by a boundary. Proceed to the next \(p\). There are finitely many components on the diagonal; at the final augmented position injectivity of \(E^p\to G(E^p)\) makes the remaining component zero. This proves exactness of the augmented total complex. The construction sends a homogeneous map to its componentwise images under \(G C^q\); the vertical terms cancel in (B.1), so it respects differentials of Hom complexes and compositions.

The homotopy induction after (1.2) applies to every abelian category with injectives. It shows that Hom into a bounded-below injective complex sends acyclic complexes to acyclic complexes. In particular an acyclic bounded-below injective complex is contractible, by applying that assertion to its identity. Hence a quasi-isomorphism between such complexes is a homotopy equivalence. Explicitly, in a contraction of its cone the lower-left block is a chain map back; the two diagonal equations say that both composites are homotopic to the identity. The homotopy category of these injective complexes realizes the localization of bounded-below complexes at quasi-isomorphisms: replace by \(I(E)\), which inverts those maps, and use the natural quasi-isomorphism \(E\to I(E)\). On injective complexes that natural map is already a homotopy equivalence. This proves the claimed universal localization property and gives the usual \(D^+(X)\).

For clarity about the triangle input, our cone is
\(\operatorname{Cone}(f)^n=F^n\oplus E^{n+1}\), with
\(d(y,x)=(d_Fy+fx,-d_Ex)\). Cone triangles use the inclusion of \(F\) and projection to \(E[1]\). Their triangle identities can be checked inside the homotopy category. The cone of an identity contracts by \((y,x)\mapsto(0,y)\). The cone of the inclusion \(F\to\operatorname{Cone}(f)\) projects to \(E[1]\) with a contractible identity summand; a section sends \(x\) to \((0,x,-fx)\), giving the rotated last map \(-f[1]\). A square with \(bf-f'a=dh\) induces the cone map \((y,x)\mapsto(by+hx,ax)\); this verifies the triangle-map axiom, including squares commuting only up to homotopy.

For the octahedron of \(E\xrightarrow fF\xrightarrow gH\), take

\[
\operatorname{Cone}(f)\xrightarrow{(y,x)\mapsto(gy,x)}
\operatorname{Cone}(gf)\xrightarrow{(z,x)\mapsto(z,fx)}
\operatorname{Cone}(g).
\tag{B.2}
\]

The cone of the first arrow has coordinates \((z,x,y,x')\). Its projection
\((z,x,y,x')\mapsto(z,y+fx)\) onto \(\operatorname{Cone}(g)\) is a chain map with section \((z,y)\mapsto(z,0,y,0)\). In the coordinates \((z,y+fx,x,x')\), the remaining summand has differential \((x,x')\mapsto(-dx+x',dx')\) and contracts by \((x,x')\mapsto(0,x)\). The resulting last arrow is \((z,y)\mapsto(y,0)\) into \(\operatorname{Cone}(f)[1]\). Write the first two arrows of (B.2) as \(\alpha,\beta\), and write cone inclusions and projections as \(\iota,p\). The required squares are the identities \(\alpha\iota_f=\iota_{gf}g\), \(p_{gf}\alpha=p_f\), \(\beta\iota_{gf}=\iota_g\), and \(p_g\beta=f[1]p_{gf}\). The last arrow is \(\iota_f[1]p_g\). The composite \(\beta\alpha\) contracts by \((y,x)\mapsto(0,y)\): its homotopy differential is \((gy,fx)\). These are the octahedron identities and its cone triangle, proving the remaining triangle axiom. Shifts and cones preserve bounded-below injective complexes, so these verifications apply to \(D^+(X)\).

The ordinary t-structure also follows from complexes. The good lower cut uses a kernel in its final degree, and the good upper cut uses a cokernel in its first degree. Their cohomology is respectively the original cohomology below and above the cut, with zero cohomology on the other side; the cut triangle follows from the quotient complex and its direct kernel/image calculation. If one object has cohomology in degrees \(\le0\), represent it by its lower cut with zero terms above zero. Resolve the upper cut of an object in degrees \(\ge1\) by the construction above, with zero terms below one. There is no degree-zero chain map between these representatives. This proves orthogonality and all ordinary t-structure axioms used below.

### B.2. The actual open-closed recollement

Let \(i:F\hookrightarrow X\) be closed and \(j:U\hookrightarrow X\) its open complement. Ordinary inverse image \(i^*\), open restriction \(j^*\), closed pushforward \(i_*\) and open extension by zero \(j_!\) are exact: their stalks are the indicated original stalks or zero. Their adjunctions follow by restricting a morphism and gluing its forced zero values outside the relevant support. For closed pushforward, opens of \(F\) are intersections with opens of \(X\), which also proves \(i^*i_*=1\). For open direct image, sections on \(O\) are sections on \(O\cap U\), giving \(j^*\dashv j_*\) and \(j^*j_*=1\).

There is a stalkwise short exact sequence of sheaves

\[
0\longrightarrow j_!j^*E\longrightarrow E\longrightarrow i_*i^*E\longrightarrow0.
\tag{B.3}
\]

It gives (2.2) in the derived category. More explicitly, for a monomorphism of complexes \(A\to B\), the cone projects quasi-isomorphically onto the quotient complex: the kernel is an identity cone on \(A\). Thus this use of a short exact sequence really gives a cone triangle, even if the sequence does not split on terms.

The exact left adjoints above show that \(j_*\) and \(i_*\) preserve injectives, and exact \(j_!\) shows that \(j^*\) preserves injectives. Consequently the chain adjunctions, applied to injective targets, give the derived adjunctions, including \(j^*\dashv Rj_*\). The identity \(j^*Rj_*=1\) follows on an injective resolution by restriction.

There is also an ordinary support right adjoint \(i^!_{\mathrm{sh}}\) to \(i_*\). Define \(i_*i^!_{\mathrm{sh}}E\) to be the kernel of \(E\to j_*j^*E\). A sheaf zero on \(U\) is identified with its closed pushforward by (B.3), so this defines a sheaf on \(F\). Any map from \(i_*A\) lands in that kernel, since \(\operatorname{Hom}(i_*A,j_*j^*E)=\operatorname{Hom}(j^*i_*A,j^*E)=0\). This proves the right adjunction. Since \(i_*\) is exact, \(i^!_{\mathrm{sh}}\) sends injectives to injectives.

An injective \(I\) is flabby by the first lesson's A.1. Its sections on \(O\cap U\) extend to \(O\), so

\[
0\to i_*i^!_{\mathrm{sh}}I\to I\to j_*j^*I\to0
\tag{B.4}
\]

is exact, even on sections. Resolve a complex by injectives and apply this sequence degreewise. Since \(j^*I\) is an injective resolution on \(U\), (B.4) gives (2.3) with \(i^!=Ri^!_{\mathrm{sh}}\), and its chain adjunction proves \(i_*\dashv i^!\). The identities (2.4) follow on these models or from their adjunctions as in Section 2. All these operations preserve shifts and cone triangles on the models just constructed. This establishes recollement in \(D^+\), allowing complexes unbounded above.

For the two-stratum disc or plane, these functors restrict to the bounded categories used in Section 4. To verify this assertion, kernels and cokernels of local systems are locally kernels and cokernels of constant matrices. Extensions of local systems are locally constant as well. On a small convex coordinate open, both end terms are constant, and
\(\operatorname{Ext}^1(\Lambda^r,\Lambda^s)=H^1(O,\Lambda^s)^r=0\): Hom out of \(\Lambda^r\) is \(r\) copies of sections, and an injective resolution computes both sides; the vanishing is proved in the first lesson's A.3. In the triangle of an extension, the vanishing connecting morphism lifts the identity to a splitting by the exact Hom sequence of Appendix A.1. Thus the middle sheaf is constant there.

It follows from the cohomology sequence that bounded complexes with finite-rank locally constant cohomology on \(U\) form a triangulated subcategory preserved by ordinary cuts. The same argument with the finite-dimensional point stalk gives the two-stratum category on \(X\). The first lesson's Proposition 1.1 shows directly that \(Rj_*L\) has bounded finite point cohomology for every such local system \(L\). The finite ordinary truncation tower of any bounded complex on \(U\) then proves the same assertion for its \(Rj_*\). The other exact functors preserve the stated bounds and finite stalks immediately, and (2.3) does so for \(i^!\). The shifted ordinary t-structure on \(U\) and the unshifted point structure therefore meet every hypothesis of Theorem 2.1 in this actual sheaf category.

### B.3. Attaching maps and mapping complexes

First use an injective model \(J\) of an open complex \(Q\), and put \(R_J=j_*J\), \(B_0(J)=i^*R_J\). These are models for \(Rj_*Q\) and its boundary. The unit of \(i^*\dashv i_*\) gives \(\rho:R_J\to i_*B_0(J)\). For a point complex \(A\) and a chain map \(a:A\to B_0(J)\), form (6.2) using the following fixed fiber convention:

\[
\operatorname{Fib}(f)^n=E^n\oplus F^{n-1},\qquad
d(x,y)=(d_Ex,fx-d_Fy)
\quad(f:E\to F).
\tag{B.5}
\]

All vector spaces are injective. Thus the terms \(R_J\), \(i_*A\), \(i_*B_0(J)\), and their fiber are bounded-below injective complexes on \(X\). In particular their ordinary Hom complexes really compute derived Hom. Applying \(j^*\) to the fiber gives \(\operatorname{Cone}(0)[-1]=J\). Its closed restriction is \(\operatorname{Fib}((1,-a):B_0(J)\oplus A\to B_0(J))\); the inclusion \(x\mapsto(ax,x,0)\) and projection onto \(A\) exhibit it as \(A\) plus a contractible identity summand. Applying the support right adjoint gives \(\operatorname{Fib}(-a)\), because it kills \(R_J\). The map \((x,y)\mapsto(x,-y)\) identifies this with \(\operatorname{Fib}(a)\) in convention (B.5), fixing the costalk sign explicitly.

Conversely the two units from a sheaf complex \(K\) give its attaching data and a map to this fiber: the two composites to the boundary agree, so their difference has its specified zero homotopy. After \(j^*\) and \(i^*\) this map is an isomorphism. Sequence (B.3) applied to its cone shows it is an isomorphism on \(X\). Replacing complexes by their injective models transfers the same construction to every object of the bounded two-stratum category.

It is useful to allow another boundary model. Let \(q:B_0(J)\to B(J)\) be a natural quasi-isomorphism of vector-space complexes, natural also for homogeneous maps of \(J\)'s. Replace \(\rho\) by \(q\rho\), and use an attaching chain map \(a:A\to B(J)\). The resulting fiber \(K\) still has closed restriction quasi-isomorphic to \(A\); its projection \(p:i^*K\to A\) has kernel \(\operatorname{Fib}(q)\). Every quasi-isomorphism of vector-space complexes is a homotopy equivalence: split cycles and boundaries by complements, which decomposes an acyclic cone into contractible two-term identity complexes. Therefore this kernel is contractible, and \(p\) is a homotopy equivalence.

For two such data, define

\[
\begin{aligned}
P&=\operatorname{Hom}_U(J,J'),& M&=\operatorname{Hom}_\Lambda(A,A'),\\
N&=\operatorname{Hom}_\Lambda(A,B(J')),&
E&=\operatorname{Fib}\bigl(P\oplus M\xrightarrow{(b,g)\mapsto B(b)a-a'g}N\bigr).
\end{aligned}
\tag{B.6}
\]

This is the asserted derived mapping complex, with all degrees retained. There is an explicit map from it to \(\operatorname{Hom}_X(K,K')\). For a degree-\(n\) triple \((b,g,h)\), and fiber coordinates \((r,x,y)\), it is

\[
(r,x,y)\longmapsto
\bigl(j_*b(r),\ g(x),\ (-1)^nB(b)(y)+h(x)\bigr).
\tag{B.7}
\]

Using (B.1) and (B.5), its differential is the same formula for
\((db,dg,B(b)a-a'g-dh)\); thus it is a map of complexes. In degree zero, composition has homotopy component \(B(b')h+h'g\), which is precisely the composition of the displayed block maps.

To prove (B.7) is a quasi-isomorphism, apply \(\operatorname{Hom}_X(K,-)\) to the defining fiber of \(K'\). The resulting fiber has the complexes

\[
\operatorname{Hom}_U(J,J')\oplus\operatorname{Hom}_\Lambda(i^*K,A'),
\qquad \operatorname{Hom}_\Lambda(i^*K,B(J')),
\]

by the chain adjunctions. On the first summand (B.7) is the identity; on the two closed Hom complexes it is precomposition by \(p\), a homotopy equivalence. There is also the off-diagonal term in (B.7), expressing the attaching homotopy. Filter each fiber by its shifted last Hom complex. The induced maps on the two successive quotients are exactly these quasi-isomorphisms, so the cone is acyclic. This proves full faithfulness at the complex level, rather than only a bijection on isomorphism classes of objects.

### B.4. Passing to the finite boundary model in degree zero

For local systems choose the additive functorial resolution \(J(L)=I(L)[1]\), and use the nested punctured discs and their angular covers from the first lesson's A.4. Let \(B(J)\) be the filtered colimit of their two-cover total complexes, with the fiber convention (B.5). Restriction gives \(q:B_0(J)\to B(J)\). Sequence (A.9) of that lesson, and exactness of filtered colimits, prove \(q\) is a quasi-isomorphism. The cover construction acts on a homogeneous degree-\(n\) map by that map on the two opens and by \((-1)^n\) times that map on the shifted intersection term; substitution in (B.5) proves compatibility with Hom differentials. Thus it has exactly the naturality required in B.3.

Write \(C_L=[V\xrightarrow{S}V]\) in degrees \(-1,0\). There is a natural quasi-isomorphism \(c_L:C_L\to B(J(L))\). With the fiber totalization (B.5), the inclusion of the noncontractible summand in the angular complex sends \(v\) to \((v,v)\) in the two-open term of degree \(-1\), and \(w\) to \((0,w)\) in the two-component intersection term of degree zero. The cover differential sends \((v,v)\) to \((0,Sv)\), so this is a chain map with exactly the displayed differential \(S\). Compose with \(L[1]\to I(L)[1]\) on each open. For comparison with the shifted unshifted-cover total, the isomorphism \(B(I(L)[1])\simeq B(I(L))[1]\) negates the intersection component; that accounts for the usual sign change of a shifted differential. The convex acyclicity and two-cover comparison proved in the first lesson show \(c_L\) is a quasi-isomorphism. Every arrow here commutes with every monodromy intertwiner; hence

\[
B(J(b))c_L=c_{L'}C_b.
\tag{B.8}
\]

For a finite point complex \(A\) and \(a:A\to C_L\), use \(c_La\) in B.3. This gives an actual sheaf object, functorially for strict maps of these finite data. Every attaching object is obtained up to isomorphism, because \(c_L\) is a homotopy equivalence of vector-space complexes. A chain representative of its homotopy inverse transfers any attaching map to \(C_L\); its comparison homotopy gives an isomorphism through (B.7).

There remains an important distinction about morphisms. In general
\(P=\operatorname{Hom}_U(J(L),J(L'))\) has positive cohomology: for the constant rank-one system, its degree-one cohomology is \(H^1(U,\Lambda)=\Lambda\), by the first lesson's angular calculation with \(S=0\). It is not replaced by ordinary sheaf Hom in all degrees. Nevertheless

\[
H^{m}(P)=0\ (m<0),\qquad
H^0(P)=\operatorname{Hom}_U(L,L').
\tag{B.9}
\]

Indeed precomposing by \(L\to I(L)\) is a quasi-isomorphism on Hom into \(I(L')\), by the homotopy induction in Section 1. The complex \(\operatorname{Hom}(L,I(L'))\) has no negative terms, and its degree-zero cocycles are exactly the maps into \(\ker(d:I^0(L')\to I^1(L'))=L'\). Common shifts preserve this calculation.

The chain map \(\operatorname{Hom}_U(L,L')[0]\to P\) sending \(b\) to \(J(b)\) thus induces isomorphisms on cohomology in all degrees \(\le0\). Also \(\operatorname{Hom}(A,C_{L'})\to\operatorname{Hom}(A,B(J(L')))\) is a quasi-isomorphism: its cone is Hom into a contractible vector-space complex. By (B.8) these maps give a map of fibers

\[
\operatorname{Fib}\left(
\operatorname{Hom}_U(L,L')[0]\oplus\operatorname{Hom}(A,A')
\longrightarrow\operatorname{Hom}(A,C_{L'})\right)
\longrightarrow E.
\tag{B.10}
\]

It induces an isomorphism on \(H^0\). This follows directly from the five consecutive terms of the fiber cohomology sequence, starting with \(H^{-1}(P\oplus M)\) and ending with \(H^0(N)\): the other four comparison maps are isomorphisms, so exactness gives injectivity and surjectivity of the middle one. Equation (B.9), not a vanishing claim about positive Ext, is what is needed here. All maps respect composition in degree zero by (B.7)–(B.8).

For \(A=[V\xrightarrow uW]\), \(A'=[V'\xrightarrow{u'}W']\), and attaching maps \((1,v)\), \((1,v')\), the left fiber in (B.10) has exactly the degree-zero cocycles (6.7). Its degree-minus-one boundaries are exactly \((ru,u'r,-r)\), because \(\operatorname{Hom}(A,C_{L'})^{-2}=0\) and the ordinary open Hom is concentrated in degree zero. This proves that the normalization \(\beta=g_0+u'h\) in Exercise 5 computes **all** actual sheaf morphisms and exactly their identifications.

### B.5. The normalization and costalk without sign ambiguity

In (6.4), the map \(E\to F\oplus V\), \(x\mapsto(dx,-a_{-1}x)\), is injective by the stated kernel condition. The induced map of stalk complexes has degree \(-1\) component \(a_{-1}\). Its kernel map is bijective: if \(u(y)=0\), write \((0,y)=(dx,-a_{-1}x)\); then \(x\in\ker d\), and \(-x\) maps to \(y\) under \(a_{-1}\). Injectivity is precisely \(\ker d\cap\ker a_{-1}=0\). Its cokernel map is the isomorphism \(F/dE\to W/uV\). Hence it is the required quasi-isomorphism with its actual sign, and the attaching square commutes strictly.

For \(a=(1,v):[V\xrightarrow uW]\to[V\xrightarrow S V]\), (B.5) has terms

\[
V\xrightarrow{y\mapsto(uy,y)}W\oplus V
\xrightarrow{(w,x)\mapsto vw-Sx}V
\quad\text{in degrees }-1,0,1.
\tag{B.11}
\]

Since \(S=vu\), degree-zero coordinates \((w-ux,x)\) split off the identity from degree \(-1\) to the second degree-zero summand. The remaining differential is exactly \(v:W\to V\). This proves (6.6) with the displayed sign. Thus the constructed sheaf is in the glued heart, and the normalization in (6.4) supplies every heart object. B.4 supplies precisely its morphisms. This completes the actual classical sheaf-model justification of the diagram equivalence in Exercise 5.

## Proof dependencies

Sections 1–6 give the assigned two-point and punctured-plane models, the general gluing theorem, intermediate extension and the classification of simple objects, followed by the five worked exercises. Appendix A proves their categorical prerequisites from the triangle and t-structure axioms. Section 1 supplies the arrow injectives and homotopy argument. Appendix B supplies the actual classical sheaf category, localization, attaching complexes and morphism comparison used in Exercise 5.

The precise earlier-lesson inputs for that classical puncture calculation are Proposition 1.1 and Appendices A–B of *Constructible complexes on algebraic varieties*: field-valued resolutions, convex acyclicity, transport and the full monodromy correspondence, natural puncture cochains and derived localization. Those passages contain proofs; no later cycle theorem is used to prove the diagram equivalence. The assigned general algebraic, étale and adic applications retain the first lesson's exact prerequisite obligations. Its later classical and finite-coefficient reconstructions must be assessed at their actual hypotheses; neither the local model nor a free citation closes the remaining normalized adic or transitive foundational gaps.

The main exposition and all five worked solutions were replaced on 5 October 2026. Their organization starts from the two-point calculation, constructs a cut by removing nonpositive open and supported parts, then uses a boundary fibre to build intermediate extension before computing puncture diagrams. The assigned examples and statements determine the mathematical scope. The separately reconstructed Appendices A–B are retained with updated references. Prior prohibited use remains recorded privately.

The source roles can be separated at the level of the constructions. The free BBD text supplies the categorical gluing, boundary and heart mathematics of Sections 2, 3, 5 and Appendix A; Laszlo–Olsson is used to compare the recollement hypotheses. Section 1 constructs its finite arrow resolution directly. Appendix B builds the classical category from injective sheaves, with the free Stacks Project passages as proof comparisons, then derives the puncture diagrams through the attaching fibre and its full mapping complex. The earlier lesson supplies the proved angular-cover calculation and the explicit monodromy correspondence. The two-point space, punctured plane and five exercise topics are the assigned mathematical scope; their presence is not a reason to import another work’s exposition. The broader algebraic and adic prerequisites are not proved in these lessons.

## References

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), freely readable author-hosted IAS scan, §§1.3–1.4. The gluing theorem, intermediate-extension properties and simple-object classification are reconstructed above; Appendix A supplies the categorical arguments used by those proofs.
- Y. Laszlo and M. Olsson, [*Perverse t-structure on Artin stacks*](https://www.cmls.polytechnique.fr/perso/laszlo/articleweb/faisceaux-pervers.pdf), freely readable author preprint, §2. Used to check the abstract recollement hypotheses and their generality.
- The Stacks Project contributors, [Injective resolutions, §13.18](https://stacks.math.columbia.edu/tag/013G), especially Lemmas 13.18.3–13.18.8, and [Cones and termwise split sequences, Lemma 13.9.14](https://stacks.math.columbia.edu/tag/014L). These freely accessible proof comparisons were read for the reconstruction in Section 1 and Appendix B; the constructions and homotopies are written locally.

# Multiplicative group cohomology and change of topology

*Mathematical exposition by GPT-6 Astra and GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

For a scheme \(Y\), the sheaf \(\mathbf G_m\) assigns to a \(Y\)-scheme \(U\) the group \(\Gamma(U,\mathcal O_U)^\times\). Passing from étale covers to flat covers does not change its cohomology. The result holds in every degree, including over nonreduced and non-Noetherian schemes.

**Theorem 1.** For every scheme \(Y\) and integer \(n\geq0\), the canonical comparison is an isomorphism

\[
H^n(Y_{\mathrm{\acute et}},\mathbf G_m)
\longrightarrow H^n((\mathrm{Sch}/Y)_{\mathrm{fppf}},\mathbf G_m).
\tag{1}
\]

These maps commute with pullback along every morphism of schemes.

The coefficient on the right is the **represented** multiplicative group. It is not generally the inverse image of the small étale sheaf on the left. For example, over an algebraically closed field \(k\), the small étale sheaf corresponds to the group \(k^\times\); its inverse image gives locally constant \(k^\times\)-valued sections. The represented group on \(\operatorname{Spec}k[t,t^{-1}]\) also contains the nonconstant unit \(t\). The proof keeps these coefficients distinct.

We use the programme's universe convention for sites. Cohomology means the right derived functors of sections of abelian sheaves. Empty schemes have zero abelian cohomology. Exact earlier arguments are linked in the final section; each invocation below identifies the result needed, rather than referring to an entire course.

## Smooth lifting and finite covers

**Lemma 2.** Let \((A,\mathfrak m,k)\) be henselian local. If \(X\to\operatorname{Spec}A\) is smooth, every specified \(k\)-point of \(X_k\) lifts to an \(A\)-point. If \(k\) is separably closed, every nonempty smooth \(k\)-scheme has a \(k\)-point.

**Proof.** By the smooth-coordinate theorem [P1], an affine neighbourhood \(U\) of the specified point \(x\) admits an étale map \(U\to\mathbb A_A^d\). Lift the coordinates of its image from \(k\) to \(A\), obtaining a section \(a:\operatorname{Spec}A\to\mathbb A_A^d\). The pullback

\[
W=U\times_{\mathbb A_A^d,a}\operatorname{Spec}A
\longrightarrow\operatorname{Spec}A
\]

is affine and étale and has the specified residue point. The henselian section criterion [P2, Theorem 1.2] supplies a section through that point. Its composite with \(W\to U\to X\) is the required lift. There is no assertion of uniqueness for a smooth lift.

For the second assertion choose a nonempty étale coordinate chart \(U\to\mathbb A_k^d\). Its image is nonempty open by openness of flat locally finitely presented maps [P3]. It contains a nonempty principal open \(D(f)\). A separably closed field is infinite: every finite field has a proper finite separable extension. Induction on the number of variables, using the root bound in one variable, shows that a nonzero polynomial over an infinite field does not vanish on every tuple. Hence \(D(f)\) has a \(k\)-point. The nonempty fibre of \(U\) there is affine étale of finite type over \(k\), so its algebra is a nonzero finite product of finite separable field extensions. These extensions equal \(k\), giving a point of \(U\). The case \(d=0\) is included. \(\square\)

### Cutting a flat family to a finite fibre

Here is the refinement used at the start of Lemma 3. Let \(A\) be local, with residue field \(k\), and let \(X\to\operatorname{Spec}A\) be flat and finitely presented with nonempty closed fibre. There is a flat finitely presented \(T\to\operatorname{Spec}A\), an \(A\)-map \(T\to X\), and a point \(x\) over the closed point at which \(T/A\) is quasi-finite.

Intersect an affine open of \(X\) with its closed fibre to obtain a nonempty affine scheme \(\operatorname{Spec}S\). We first construct a closed-fibre regular sequence whose common zero is isolated. By Krull dimension and Noether normalization, Corollary 3.2, the nonzero finite-type algebra \(S\) is finite over an embedded polynomial ring \(R=k[t_1,\ldots,t_d]\); \(S\) may be nonreduced. Its generic fibre over \(R\) is nonzero. Choose a basis of that generic fibre, represented by elements of \(S\). The map from the corresponding finite free \(R\)-module to \(S\) has finite kernel and cokernel, and both vanish after passing to the fraction field. Inverting one nonzero element of \(R\) kills them, so \(S_f\) is a nonzero finite free \(R_f\)-module.

Choose a maximal ideal \(x\) of \(S_f\). Its contraction \(y\) is maximal in \(R_f\), since the extension is finite, and its residue field is finite over \(k\), by The Nullstellensatz and Jacobson rings, Theorem 1.3. The polynomial local ring \(R_y\) is regular of dimension \(d\). A regular system of parameters of \(R_y\) remains a regular sequence on \(S_x\), by flatness: tensor each of its successive injective multiplication sequences with the flat module. Its final quotient is finite over the residue field of \(R_y\), hence Artinian. These polynomial-ring, dimension and regular-parameter statements are Krull dimension and Noether normalization, Theorem 4.3 and Regular local rings, Theorem 1.1 and Theorems 3.2–3.3. Thus we have elements \(f_1,\ldots,f_d\in S_x\) forming a regular sequence and cutting a zero-dimensional local quotient. When \(d=0\), this is the empty sequence.

Represent them by functions on a neighbourhood of \(x\) in the fibre and lift those functions to an affine neighbourhood in \(X\). Apply Hilbert and Quot schemes, Lemma 7.B(1) successively, shrinking around \(x\) at each step. The successive quotients are flat and locally of finite presentation over \(A\), and their closed-fibre equations are the chosen regular sequence. After the last equation, the closed fibre is zero-dimensional at \(x\).

The resulting finite-type morphism is quasi-finite at \(x\): the point is isolated in its fibre, with finite residue extension. We may take an affine neighbourhood of \(x\) in the cut scheme, keeping flatness and finite presentation over the affine base. Call it \(T\). Its map to \(X\) is the closed immersion defined by the equations followed by the selected open immersions. This proves the construction needed in Lemma 3; the finite neighbourhood will be extracted there using [P5, Theorem 4.2].

**Lemma 3.** Every fppf cover of the spectrum of a henselian local ring \(A\) has a refinement by a surjective finite locally free morphism \(\operatorname{Spec}B\to\operatorname{Spec}A\).

**Proof.** Let \(s\) be the closed point. Choose an affine open in one covering member meeting the closed fibre. Its map to \(\operatorname{Spec}A\) is flat and finitely presented. The construction just given supplies a flat finitely presented \(T\to\operatorname{Spec}A\), factoring through that member, and a point above \(s\) at which it is quasi-finite. The elementary étale neighbourhood theorem [P5, Theorem 4.2] gives an étale neighbourhood \((U,u)\to(\operatorname{Spec}A,s)\), with \(k(u)=k(s)\), and an open \(V\subset T\times_AU\) finite over \(U\) and meeting the fibre over \(u\).

The map \(V\to U\) remains flat and locally finitely presented. A finite flat morphism of finite presentation is finite locally free. Its image is open and contains \(u\). Restrict \(U\) to this image and then to an affine neighbourhood of \(u\). The resulting finite locally free morphism is surjective. By [P2, Theorem 1.2], the marked residue point gives a section \(\sigma:\operatorname{Spec}A\to U\). Then

\[
V\times_{U,\sigma}\operatorname{Spec}A\longrightarrow\operatorname{Spec}A
\]

is the required finite locally free surjection and still factors through the selected cover member. Both the residue-field equality and the marked point are needed for the section. \(\square\)

## The schemes of cochains and cocycles

Let \(R\) be local and \(B\) a faithfully flat finite free \(R\)-algebra. For \(n\geq0\) put

\[
D_n=B^{\otimes_R(n+1)},\qquad
C^n(A)=(A\otimes_RD_n)^\times
\]

for every \(R\)-algebra \(A\). If \(\partial_i:D_n\to D_{n+1}\) inserts \(1\) in position \(i\), define

\[
\begin{gathered}
\delta_n(u)=\prod_{i=0}^{n+1}\partial_i(u)^{(-1)^i},
\\
\qquad Z^n=\ker(\delta_n).
\end{gathered}
\tag{2}
\]

The insertions commute in the cosimplicial order, so consecutive coboundaries have value \(1\).

**Lemma 4.** For \(n\geq1\), the map

\[
\delta_{n-1}:C^{n-1}\longrightarrow Z^n
\tag{3}
\]

is a smooth surjective morphism of finitely presented affine \(R\)-schemes.

**Proof.** Choose a basis of the finite free algebra \(D_n\). For an element \(x\) let \(m_x\) denote its multiplication matrix. The element is a unit exactly when \(\det(m_x)\) is a unit: if the matrix is invertible, its inverse applied to \(1\) is an inverse of \(x\); the converse follows by multiplying by \(x^{-1}\). Thus \(C^n\) is the principal open defined by this determinant in affine space. The inverse coordinates are given by the adjugate matrix. All insertions, inverses and products in (2) are morphisms. Consequently \(Z^n\) is the affine fibre over the identity, cut out by finitely many equations. The map (3) is finitely presented: a finite presentation for its source over \(R\), together with equations specifying the images of finitely many generators of its target algebra, gives a finite presentation over that algebra.

To prove formal smoothness, let \(A\) be an \(R\)-algebra and \(J\subset A\) satisfy \(J^2=0\). Suppose

\[
z\in Z^n(A),\qquad
\bar v\in C^{n-1}(A/J),\qquad
\delta(\bar v)=\bar z.
\]

Units lift across a square-zero ideal. Indeed, lift a unit and its inverse; their product is \(1+j\), whose inverse is \(1-j\). Choose a lift \(v_0\in C^{n-1}(A)\). Write \(D_i(A)=A\otimes_RD_i\). Since this is flat over \(A\), the kernel of its reduction modulo \(J\) is

\[
J\otimes_AD_i(A)=JD_i(A).
\]

Hence \(z/\delta(v_0)=1+w\) for a unique \(w\in JD_n(A)\). In a square-zero ideal multiplication of such units is addition, and inversion is negation. The equation \(\delta(1+w)=1\) therefore says that \(w\) is an additive Amitsur cocycle with coefficient module \(J\).

The additive Amitsur complex is exact for every module under a faithfully flat map [P6, Lemma 4.1]. Apply it to \(A\to A\otimes_RB\) and \(J\). There is \(t\in JD_{n-1}(A)\) with \(d(t)=w\). Then

\[
\begin{gathered}
v=v_0(1+t),\\
\qquad
\delta(v)=\delta(v_0)(1+d(t))=z.
\end{gathered}
\tag{4}
\]

This proves the square-zero lifting property. Finite presentation and formal smoothness give smoothness [P1]. Notice that the coefficient ideal \(J\) has remained in every tensor term.

For surjectivity take a geometric point \(z:\operatorname{Spec}K\to Z^n\), where \(K\) is algebraically closed. The finite \(K\)-algebra \(B_K\) is nonzero by faithful flatness. A maximal ideal has residue field finite over \(K\), hence equal to \(K\); this gives an augmentation \(\varepsilon:B_K\to K\). Applying it to the first tensor factor defines \(h_i:C^i(K)\to C^{i-1}(K)\). The insertion identities give

\[
h_{i+1}(\delta_i(u))\,\delta_{i-1}(h_i(u))=u.
\tag{5}
\]

The first insertion gives \(u\); each other insertion pairs with the corresponding insertion after \(h_i\), with opposite exponent. This verifies (5), including its signs. Since \(\delta_n(z)=1\), equation (5) gives \(\delta_{n-1}(h_n(z))=z\). Every geometric fibre of (3) is nonempty. Thus the map is surjective. \(\square\)

## Vanishing over a strictly henselian local ring

**Proposition 5.** For every strictly henselian local ring \(R\) and every \(q>0\),

\[
H^q((\mathrm{Sch}/\operatorname{Spec}R)_{\mathrm{fppf}},\mathbf G_m)=0.
\tag{6}
\]

**Proof.** First take a finite locally free surjective cover \(\operatorname{Spec}B\to\operatorname{Spec}R\). Over a local ring its algebra is finite free. For any positive-degree cocycle \(z\in Z^n(R)\), the fibre

\[
X_z=C^{n-1}\times_{Z^n,z}\operatorname{Spec}R
\]

is smooth and surjective by Lemma 4. Its closed fibre is nonempty smooth over the separably closed residue field. Lemma 2 gives a residue point and then lifts it to an \(R\)-point. Such a point is exactly a cochain \(v\) with \(\delta(v)=z\). Thus all positive Čech groups of every such cover vanish.

To pass to derived cohomology, consider simultaneously all schemes finite over \(\operatorname{Spec}R\). A finite algebra over a henselian local ring is a finite product of henselian local rings [P2, Theorem 2.2 and Proposition 3.1]. Each factor's residue field is finite over the separably closed residue field \(k\) of \(R\), and is again separably closed. Here is the field argument. In characteristic \(p\), remove the largest common \(p\)-power from the exponents of an irreducible polynomial over \(k\); its remaining polynomial is separable, so is linear. Every algebraic element over \(k\) therefore has a \(p\)-power in \(k\). An algebraic closure of a finite extension \(L/k\) is consequently purely inseparable over \(L\), excluding nontrivial finite separable extensions of \(L\). In characteristic zero the assertion is immediate.

Every factor is therefore strictly henselian. By Lemma 3, any fppf cover of a finite \(R\)-scheme refines factor by factor to finite locally free surjections. Their finite disjoint union gives a refining family. Different members may map to different members of the original cover; a single-member factorization over a disconnected base is not required. Its positive Čech groups vanish by the preceding argument on each factor. Units on a finite disjoint union form the product of the unit groups, so finite products preserve this exactness.

Every member of these families and every iterated overlap is finite over \(R\). The simultaneous Čech-to-derived criterion [P7, Theorem 4.1] therefore applies to this class of objects and its cofinal class of covers. Its proof uses local effacement and the Čech spectral sequence, inducting simultaneously on all objects and degrees. In particular it does not assume that one chosen covering object is already derived-acyclic. Taking the object \(\operatorname{Spec}R\) gives (6). \(\square\)

## Continuity with the represented coefficient

### Flatness at a finite stage

**Lemma 6.A (finite-presentation flatness descent).** Let \(A=\operatorname{colim}_i A_i\) be a directed colimit of rings. Let \(B_i\) be a finitely presented \(A_i\)-algebra and let \(N_i\) be a finitely presented \(B_i\)-module, both obtained by base change from one stage \(i_0\). If \(N=N_{i_0}\otimes_{A_{i_0}}A\) is \(A\)-flat, then \(N_j\) is \(A_j\)-flat at some stage \(j\geq i_0\), and at every later stage.

**Proof.** Choose presentations of the algebra and module. Their finitely many coefficients lie in a finitely generated \(\mathbf Z\)-subalgebra \(R_0\subset A_{i_0}\). Write the corresponding models as \(D_0,G_0\); their base changes to \(A_{i_0}\) are \(B_{i_0},N_{i_0}\). Since \(R_0\) is Noetherian, the kernel of \(R_0\to A\) is finitely generated. Its generators become zero at a common later \(A_i\)-stage. Replace \(R_0\) by this quotient and the models by their base changes. We may now regard \(R_0\) as a subring both of that stage and of \(A\).

Let \(R_\lambda\) range through the finitely generated \(\mathbf Z\)-subalgebras of \(A\) containing \(R_0\), and put
\[
D_\lambda=D_0\otimes_{R_0}R_\lambda,\qquad
G_\lambda=G_0\otimes_{R_0}R_\lambda.
\]
Their colimits are \(B,N\). Fix \(x\in\operatorname{Spec}B\), and contract it to the rings \(D_\lambda\), and its image in \(\operatorname{Spec}A\) to the rings \(R_\lambda\). Localizing gives exactly the models of Flatness criteria, Lemma 6.2: the base and source rings are Noetherian local, transitions are localized base changes, and the module transitions are their base changes. That lemma's finite Tor argument therefore gives a stage at which the localized \(G_\lambda\) is flat over the localized \(R_\lambda\).

The Noetherian openness theorem Flatness criteria, Theorem 5.2 gives an open neighbourhood \(U_{\lambda,x}\subset\operatorname{Spec}D_\lambda\) on which \(G_\lambda\) is flat over \(R_\lambda\), and whose pullback contains \(x\). Quasi-compactness of \(\operatorname{Spec}B\) selects finitely many such neighbourhoods covering it after pullback. Increase \(\lambda\) to a common stage. Flatness survives every subsequent base change, so their inverse images remain flat neighbourhoods for the new model.

These finitely many opens are quasi-compact because \(D_\lambda\) is Noetherian. Write their union as finitely many principal opens \(D(f_1),\ldots,D(f_r)\). Their pullbacks cover \(\operatorname{Spec}B\), so \((f_1,\ldots,f_r)B=B\). An equation
\[
1=\sum_{\nu=1}^r b_\nu f_\nu
\]
has finitely many coefficients in the filtered colimit \(B\), and holds at some later model \(D_\mu\). Its principal opens now cover all of \(\operatorname{Spec}D_\mu\). Hence \(G_\mu\) is flat over \(R_\mu\).

Finally \(R_\mu\) is finitely presented as an \(R_0\)-algebra: it is finitely generated and \(R_0\) is Noetherian. Its map to \(A\) factors through a sufficiently late \(A_j\), respecting the fixed \(R_0\)-map. To see this, lift its finitely many algebra generators and then its finitely many relation equations to the directed system. Base changing \(G_\mu\) along that map gives precisely \(N_j\), since all models came from \(D_0,G_0\). Thus \(N_j\) is \(A_j\)-flat. Base change proves the assertion at every later stage. \(\square\)

**Proposition 6.** If \(A=\operatorname{colim}_i A_i\) is a filtered colimit of rings, then for every \(q\geq0\) the canonical map is an isomorphism

\[
\begin{gathered}
\operatorname{colim}_i H^q_{\mathrm{fppf}}(\operatorname{Spec}A_i,\mathbf G_m)
\\
\longrightarrow H^q_{\mathrm{fppf}}(\operatorname{Spec}A,\mathbf G_m).
\end{gathered}
\tag{7}
\]

**Proof.** Let \(\mathcal C_A\) have all affine schemes finitely presented over \(A\) as objects, all \(A\)-morphisms as arrows, and finite jointly surjective flat finitely presented families as covers. Its objects need not themselves be flat over \(A\). Products are given by tensor products. If two maps to \(\operatorname{Spec}C\) are compared, choose finitely many algebra generators \(c_r\) of \(C\); their equalizer is cut out by the finitely many differences of their images. Thus finite limits remain in \(\mathcal C_A\).

Any fppf cover of an object of \(\mathcal C_A\) has a finite affine refinement there: take affine opens in the covering schemes and use openness [P3] and quasi-compactness of the target to select finitely many images covering it. This assertion concerns covers of objects of \(\mathcal C_A\), not every object of the big site.

The inclusion of \(\mathcal C_A\) into the big fppf site preserves covers and finite limits. By [P8, Theorem 2.1], restriction of sheaves has an exact left adjoint, and therefore preserves injectives. Restriction is also exact: kernels are computed on sections, and an epimorphism lifts a section locally; the preceding finite refinement puts that lifting cover in \(\mathcal C_A\). Restrict an injective resolution and evaluate at the common terminal object. It follows that

\[
H^q_{\mathrm{fppf}}(\operatorname{Spec}A,F)=H^q(\mathcal C_A,F|_{\mathcal C_A})
\tag{8}
\]

canonically. No equivalence of the two whole topoi is asserted.

Suppose first the index set is directed. Base change gives the compatible sites \(\mathcal C_{A_i}\). A finitely presented algebra over \(A\) descends because it has finitely many coefficients and relations. A map descends by choosing the images of its finitely many generators, and its relation equations hold at a sufficiently late stage. Equality of two maps is tested on those same generators and also holds eventually. This proves the equivalence of the colimit category with \(\mathcal C_A\).

A finite fppf cover descends as a finite family of finitely presented algebras. Lemma 6.A makes its finitely many members flat at one common later stage. Their image is then a quasi-compact open union

\[
D(g_1)\cup\cdots\cup D(g_r)\subseteq\operatorname{Spec}B_i.
\]

Its base change to \(B=B_i\otimes_{A_i}A\) is surjective, so \(1=\sum_r b_rg_r\) for finitely many \(b_r\in B\). This equation and its coefficients hold at a later stage. The descended family is therefore surjective there. Morphisms of finite covering families and their equalities descend by the generator argument. Thus every finite diagram of objects, arrows, covering families and their equalities descends to a common stage.

On \(\mathcal C_{A_i}\), the coefficient \(\mathbf G_m\) is represented by \(\operatorname{Spec}A_i[x,y]/(xy-1)\). Its sheaf condition follows by applying additive faithfully flat descent [P6] both to a unit and to its inverse. The canonical inverse-image functor carries this representing object to its base change: adjunction and Yoneda identify maps out of the pullback with evaluation on the base-changed object; multiplication and inversion are respected. Explicitly, on a descended algebra \(B_i\), the limit coefficient has sections

\[
\operatorname{colim}_{j\geq i}(B_i\otimes_{A_i}A_j)^\times
=(B_i\otimes_{A_i}A)^\times.
\tag{9}
\]

A unit and its inverse descend together and their product becomes \(1\) at a finite stage; equality also becomes true at a finite stage. This proves both directions of (9) and identifies the actual unit maps, rather than choosing abstract group isomorphisms.

The passage to higher cohomology uses Hypercoverings, Theorem 7.1. That theorem applies to every small site with fibre products, including \(\mathcal C_A\). It identifies a derived cohomology class with a cocycle on a hypercovering, and identifies a zero class with a cochain that becomes a boundary after refinement. Its comparison maps are canonical and natural in the coefficient sheaf and in maps of hypercoverings. We give the finite-data step for our site explicitly. Replacing a hypercovering by the coskeleton of its truncation through degree \(r\) leaves all those terms unchanged. Its canonical map from the original hypercovering induces the same cochain comparison in degrees below \(r\). We may therefore use \(r\)-coskeletal targets when constructing a refinement for such a class.

A hypercovering in this theorem is a simplicial family of objects, with a covering map onto the finite-limit matching object in each degree. For any fixed integer \(r\), it admits a refinement whose families are finite in degrees \(0,\ldots,r\). In degree zero choose a finite subcover. Suppose the finite refinement has been constructed below degree \(j\). Pull back the original degree-\(j\) matching cover to the new matching object. That object is a finite family of affine finitely presented schemes, hence quasi-compact component by component. Its pulled-back cover has a finite subcover. Use those finitely many objects as the new nondegenerate simplices and adjoin the forced degeneracies of the earlier degrees. There are finitely many such degeneracies in this fixed degree. Their face maps satisfy the matching relations by construction. This is the split-refinement construction proved in Hypercoverings, Section 9, applied to finite affine covers. It produces the required truncated simplicial family and its map to the original truncation.

Complete that truncation by its \(r\)-coskeleton. Its matching maps above degree \(r\) are isomorphisms, so it is a hypercovering, with the same terms through degree \(r\). The truncated map to the chosen \(r\)-coskeletal target extends to a full simplicial map by the coskeleton adjunction. Every term is a finite family: in each fixed degree the coskeleton is a finite limit of finite families. The same construction applied to a refinement gives a finite truncated refinement. Thus it suffices to work with finite families, while retaining the actual maps that compare cochains. The coskeleton and matching assertions are Hypercoverings, Sections 1–2.

Fix \(n>0\) and put \(r=n+1\). A degree-\(n\) cocycle and its cohomology group use only degrees \(n-1,n,n+1\). All the data in the corresponding finite truncated hypercover consist of finitely many finitely presented algebras, finitely many face and degeneracy maps, finitely many equalities between their composites, and finitely many matching covers. The descent arguments above put all this data at one stage \(A_i\), increasing \(i\) to make every matching cover fppf and surjective. Finite limits commute with base change, so these remain the correct matching objects. A cochain of units has finitely many entries. Equation (9) descends those entries, and its cocycle equations hold at a sufficiently late stage. Taking the coskeleton there gives a hypercovering over \(A_i\) and a cocycle representing a class in \(H^n_{\mathrm{fppf}}(\operatorname{Spec}A_i,\mathbf G_m)\). Its image is the original class. This proves surjectivity in (7).

For injectivity, represent a class at a stage \(A_i\) by a finite truncated hypercover and replace its completion by the \(r\)-coskeleton. If the image class over \(A\) is zero, the hypercovering comparison theorem gives a refinement on which its cocycle is a boundary. Refine that hypercover through degree \(r\) to finite families as above. The truncated refinement map, its finitely many simplicial compatibility equations, and the finitely many entries of the degree-\((n-1)\) primitive all descend to a common stage \(A_j\), \(j\geq i\). The boundary identity is a finite list of equalities of units and therefore also holds at a later common stage. Since the target hypercover is \(r\)-coskeletal, the descended truncated refinement extends to a full map between the coskeleta. The stage-\(j\) cocycle is now a boundary after that refinement, so its class is zero. This proves injectivity. Degree zero is the units calculation (9). Base change preserves covers and finite limits and carries each represented family to its base change. Its exact inverse-image functor therefore carries the associated free augmented resolution to the corresponding resolution. Adjunction and the map of represented unit sheaves make the cochain comparison (4.5) in the cited hypercover lesson commute with the derived pullback map. Thus the maps just computed are the canonical restriction and base-change maps, proving the canonical isomorphism (7).

The corresponding adjunction counit for compatible injective systems is
\[
\begin{gathered}
f_a^{-1}f_{a\circ b,*}I
=f_a^{-1}f_{a,*}f_{b,*}I\\
\longrightarrow f_{b,*}I
\end{gathered}
\tag{10}
\]
for arrows \(a:j\to i\), \(b:k\to j\) and a sheaf \(I\) on the site at \(k\). Both sides are sheaves on the site at \(j\). The prefix is \(f_a^{-1}\); the map is its counit evaluated at \(f_{b,*}I\), as in the site adjunctions [P8]. This records the compatible-system form of the comparison.

For a general small filtered category, the cofinal directed-set theorem [P12] supplies one directed system preserving colimits of every diagram on that category. Apply it to both the ring diagram and its cohomology groups. A skeleton alone would not give this directed-set reduction. \(\square\)

## Pointed neighbourhoods and strict localization

**Lemma 7.** Let \(R\) be any ring, \(\mathfrak p\) a prime, and \(k(\mathfrak p)\subseteq K\) a chosen separable algebraic closure. Index étale \(R\)-algebras \(S\) by compatible evaluations \(e:S\to K\), with arrows preserving the evaluations. With \(\mathfrak q=\ker e\), this category is filtered and

\[
\begin{gathered}
L=\operatorname{colim}_{(S,e)}S
\\
\cong(R_{\mathfrak p})^{sh}
\\
\cong\operatorname{colim}_{(S,e)}S_{\mathfrak q}
\end{gathered}
\tag{11}
\]

canonically with the specified residue field.

**Proof.** Evaluation extends to \(S\otimes_Rk(\mathfrak p)\), a finite product of finite separable fields. It selects a factor with an embedding into \(K\), equivalently a prime over \(\mathfrak p\) and an embedding of its residue field. The image \(e(S)\) need not itself be a field when \(R\) is not local.

The category contains \(R\to K\). Tensor products, evaluated by multiplication in \(K\), give common targets. For parallel pointed maps \(u,v:S\to T\), put \(D=S\otimes_RS\) and

\[
\begin{gathered}
W=T\otimes_D S,
\\
\quad D\to T:\ s\otimes t\longmapsto u(s)v(t),
\\
\quad D\to S:\ s\otimes t\longmapsto st.
\end{gathered}
\]

The last map is étale, by the maps-between-étale-algebras result specified in [P2]. Hence \(T\to W\) and \(R\to W\) are étale. The evaluations agree on \(D\), so induce \(W\to K\). The relations in \(W\) identify \(u(s)\) with \(v(s)\), giving an equalizing arrow. This proves filteredness.

The induced evaluation \(L\to K\) is onto. For \(\alpha\in K\), lift the coefficients of its monic separable minimal polynomial to \(R_t\) for one \(t\notin\mathfrak p\), obtained by clearing their finitely many denominators. If \(f\) is the lifted polynomial, then

\[
(R_t[T]/(f))_{f'}\longrightarrow K,\qquad T\longmapsto\alpha
\]

is a pointed étale algebra representing \(\alpha\). Every element of \(L\) with nonzero evaluation becomes a unit: represent it by \(s\in S\) and use the pointed principal localization \(S_s\). No element of the evaluation kernel is a unit. The kernel is therefore the unique maximal ideal, and the residue field is \(K\). Every \(t\in R\setminus\mathfrak p\) becomes a unit, giving a local map \(R_{\mathfrak p}\to L\).

Let \(P\in L[T]\) be monic with simple residue root \(\alpha\in K\). Represent its coefficients at one stage \((S,e)\) by a monic \(Q\). The pointed algebra \((S[T]/(Q))_{Q'}\), evaluated at \(\alpha\), gives a root in \(L\) with that residue. This construction does not require \(\alpha\) to lie in the previous stage's residue field. Thus \(L\) is strictly henselian.

Let \(H=(R_{\mathfrak p})^{sh}\) be the construction in [P2, Theorem 5.1]. For every \((S,e)\), the section criterion applied to the étale \(R_{\mathfrak p}\)-algebra \(S\otimes_RR_{\mathfrak p}\) gives a unique map to \(H\) with the specified residue evaluation. These maps are compatible by uniqueness and induce a local map \(f:L\to H\). Conversely the strict-henselization universal property gives a local map \(g:H\to L\) inducing the identity of \(K\). The same property gives \(fg=\mathrm{id}_H\). The maps \(gf\) and \(\mathrm{id}_L\) agree on every \(S\): after localizing the base they are two lifts of the same evaluation to the henselian ring \(L\), so the section criterion makes them equal. Hence \(gf=\mathrm{id}_L\).

Finally, every pointed arrow \(S\to T\) pulls back the marked prime of \(T\) to that of \(S\), so induces a map of their localizations. The maps \(S\to L\) invert all elements outside \(\mathfrak q\), giving compatible maps \(S_{\mathfrak q}\to L\). They induce an inverse to \(\operatorname{colim}S\to\operatorname{colim}S_{\mathfrak q}\): one composite fixes every element from \(S\), and the other fixes such elements and their inverted denominators. This proves (11). \(\square\)

## The comparison and its naturality

**Proof of Theorem 1.** Viewing an étale \(Y\)-scheme as a \(Y\)-scheme preserves covers and finite limits and defines a morphism of topoi

\[
\epsilon_Y:(\mathrm{Sch}/Y)_{\mathrm{fppf}}
\longrightarrow Y_{\mathrm{\acute et}}.
\]

Its direct image of the represented \(\mathbf G_m\) is the small étale unit sheaf, by evaluation on each étale object. To compute a higher direct image, restrict an injective resolution on the big fppf site to the slice over an étale object \(U\). Exact slice adjunctions make this restriction acyclic for sections [P7, Sections 2–3]. Evaluation of the direct image on \(U\) is evaluation of that same resolution on the represented \(U\). Taking presheaf cohomology and then its associated sheaf therefore shows that \(R^q\epsilon_{Y,*}\mathbf G_m\) is the sheafification of

\[
U\longmapsto H^q_{\mathrm{fppf}}(U,\mathbf G_m).
\]

Sheafification does not change stalks [P8]. Fix a geometric point \(\bar y\) of \(Y\). Affine pointed étale neighbourhoods inside a fixed affine neighbourhood of its underlying point are cofinal: restrict to that affine base, then choose an affine open containing the marked point; do the same after fibre products to refine finite sets of arrows. Their coordinate rings have colimit \(\mathcal O_{Y,\bar y}^{sh}\) by Lemma 7. If the geometric point has values in a larger algebraically closed field, its finite étale residue extensions land in the separable algebraic closure of \(k(y)\) inside that field; this is the chosen residue field used in Lemma 7.

Proposition 6 now identifies the stalk canonically as

\[
(R^q\epsilon_{Y,*}\mathbf G_m)_{\bar y}
=H^q_{\mathrm{fppf}}(\operatorname{Spec}\mathcal O_{Y,\bar y}^{sh},\mathbf G_m).
\tag{12}
\]

For \(q>0\) it is zero by Proposition 5. To make the detection step explicit, a section whose every geometric germ is zero vanishes on an étale neighbourhood of every point. These neighbourhoods cover its domain, so the sheaf separatedness axiom makes the section zero. Thus every positive higher direct image vanishes. In degree zero the direct image is exactly \(\mathbf G_m\). The canonical map

\[
\mathbf G_m\longrightarrow R\epsilon_{Y,*}\mathbf G_m
\]

is therefore a quasi-isomorphism. Leray [P7, Theorem 8.1] identifies derived sections on the right with the fppf derived sections on \(Y\). Taking degree \(n\) proves (1), without a global affineness or quasi-compactness assumption on \(Y\).

For naturality, if \(g:X\to Y\), an étale object \(U\) pulls back to \(U\times_YX\) whether it is first viewed in the small étale or the big fppf site. These identical object maps give the square of geometric morphisms. Its coefficient maps are induced by ring pullback:

\[
g_{\mathrm{\acute et}}^{-1}\mathbf G_{m,Y}\longrightarrow\mathbf G_{m,X},
\qquad
g_{\mathrm{fppf}}^{-1}\mathbf G_{m,Y}\longrightarrow\mathbf G_{m,X}.
\]

The latter is the represented base-change identification; the former is not asserted to be an isomorphism. The derived base-change map is constructed from the square and the adjunction counit [P7, Section 9]. Its compatibility with the identity \(\epsilon_*\mathbf G_m=\mathbf G_m\) says that both composites send a unit on \(U\) to its image on \(U\times_YX\). The unit and counit identities consequently give the same derived comparison map. Taking cohomology yields the commuting square

\[
\begin{array}{ccc}
H^n_{\mathrm{\acute et}}(Y,\mathbf G_m)&\longrightarrow&H^n_{\mathrm{fppf}}(Y,\mathbf G_m)\\
\downarrow g^*&&\downarrow g^*\\
H^n_{\mathrm{\acute et}}(X,\mathbf G_m)&\longrightarrow&H^n_{\mathrm{fppf}}(X,\mathbf G_m).
\end{array}
\tag{13}
\]

This uses the canonical maps of the square, not a separate assertion that all base-change morphisms are invertible. \(\square\)

## The relative Picard comparison

**Corollary 8.** Let \(f:X\to S\) satisfy the universal condition
\(\mathcal O_T\xrightarrow{\sim}(f_T)_*\mathcal O_{X_T}\) for every \(T\to S\). The étale and fppf relative Picard sheaves agree, and their obstruction sequences agree naturally:

\[
\begin{gathered}
0\\
\longrightarrow\operatorname{Pic}(T)
\\
\longrightarrow\operatorname{Pic}(X_T)
\\
\longrightarrow\operatorname{Pic}_{X/S}(T)
\\
\longrightarrow H^2_{\mathrm{\acute et}}(T,\mathbf G_m)
\\
\longrightarrow H^2_{\mathrm{\acute et}}(X_T,\mathbf G_m).
\end{gathered}
\tag{14}
\]

**Proof.** The line-bundle/torsor correspondence and the two Leray five-term rows are proved in [P13, Theorem 3.1]. The morphism from the étale relative Picard sheaf to its fppf sheafification gives a map of these rows. The four terms other than the relative Picard term have canonical isomorphisms: the two Picard groups use the same line bundles, and the two degree-two terms use Theorem 1. Theorem 1 also gives compatibility with the pullbacks in these rows.

Here is the middle-term argument. If an étale relative class maps to zero, its boundary is zero; it is therefore the image of \(b\in\operatorname{Pic}(X_T)\). Below, \(b\) comes from \(\operatorname{Pic}(T)\), so it does above as well, and the original class is zero. Conversely lift the boundary of an fppf relative class through the isomorphism on \(H^2(T,\mathbf G_m)\). Its image in \(H^2(X_T,\mathbf G_m)\) is zero, so exactness gives an étale relative class with that boundary. The difference downstairs has zero boundary and comes from \(\operatorname{Pic}(X_T)\); that same line bundle corrects the lift. Thus the relative map is bijective for every \(T\), naturally. This proves the sheaf comparison and (14). The argument uses Theorem 1 first; it is not a proof of Theorem 1 from a Picard comparison. \(\square\)

## Sources and exact earlier proofs

The comparison is Grothendieck's theorem. The proof uses his strict-local method, specialized to the represented multiplicative group: [*Le groupe de Brauer III*, Appendix 11, printed pages 171–183, especially Theorem 11.7](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/DixExp.pdf#page=145). The following links identify the exact earlier programme and fork arguments used here.

- **[P1] Smooth coordinates and the lifting criterion.** *Smooth morphisms*, Theorem 4.1 and Theorem 5.2, and *Infinitesimal lifting and invariance under thickenings*, Theorem 4.1.
- **[P2] Henselian sections and strict henselization.** *Henselian local rings and henselization*, Theorem 1.2, Theorem 2.2, Proposition 3.1 and Theorem 5.1. *Formally smooth, unramified and étale ring maps*, Proposition 7.4 proves that maps between étale algebras are étale, as used in Lemma 7.
- **[P3] Flatness and openness.** *Flat morphisms*, Proposition 2.1, Lemma 3.1 and Theorem 3.2.
- **[P4] Cutting a flat family to a finite fibre.** The construction preceding Lemma 3 is proved here, over every local base. It uses *Krull dimension and Noether normalization*, Corollary 3.2 and Theorem 4.3, regular polynomial local rings and their parameters from *Regular local rings*, Sections 1 and 3, and the arbitrary-base regular-equation lifting in *Hilbert and Quot schemes*, Lemma 7.B. The general flat quasi-finite domination results are also treated in the [AI Integrated Stacks Project, more-morphisms chapter](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/more-morphisms.tex#L6317).
- **[P5] The finite neighbourhood.** *Étale neighbourhoods, henselization and quasi-finite morphisms*, Lemma 4.1 and Theorem 4.2.
- **[P6] Additive faithfully flat exactness.** *Topologies on schemes*, Lemma 4.1.
- **[P7] Derived cohomology on sites.** *Cohomology on sites*, Proposition 2.1, Theorem 3.2, Theorem 4.1, Theorem 8.1 and Section 9. These supply exact slice adjunctions, the simultaneous Čech-to-derived criterion, Leray and its natural base-change map.
- **[P8] Site morphisms and stalks.** *Topoi, morphisms and points*, Theorem 2.1 and Section 4.
- **[P9] Flatness at a finite stage.** Lemma 6.A gives the global finite-presentation argument. Its complete local-model and Noetherian openness inputs are *Flatness criteria*, Lemma 6.2 and Theorem 5.2. They include the finite Tor obstruction and its transport through arbitrary model maps.
- **[P10] Hypercover comparison.** *Hypercoverings*, Sections 1–7 proves matching objects, refinements, homotopy equalization, and the canonical derived-cohomology comparison. Section 9 proves the split basis-refinement construction. Proposition 6 gives the finite affine version and its descent to ring stages.
- **[P11] Higher direct images and continuity.** The injective slice calculation in the proof of Theorem 1 identifies the presheaf whose associated sheaf is the higher direct image. Proposition 6 proves continuity for the represented unit sheaf by finite hypercovers. General compatible-site constructions and limit theorems are also in the [AI Integrated Stacks Project, sites](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/sites.tex#L3767) and [sites-cohomology](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/sites-cohomology.tex#L2854) chapters.
- **[P12] A cofinal directed set.** *Artin's axioms*, “Replacing a filtered category by a directed set” gives the complete construction; “Cofinality preserves colimits” proves its categorical comparison for all target categories.
- **[P13] Picard sheaves and their Leray rows.** *The Picard functor and the Picard scheme of a curve*, Section 3. The line-bundle/torsor identification and the big/small étale comparison are *Topologies on schemes*, Theorems 6.2 and 7.1. Only its line-bundle interpretation and construction of the two rows enter Corollary 8; its use of the topology comparison is supplied by Theorem 1 here, not imported as a premise.

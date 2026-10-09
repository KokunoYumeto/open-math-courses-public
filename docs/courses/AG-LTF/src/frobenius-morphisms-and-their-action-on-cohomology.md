# Frobenius morphisms and their action on cohomology

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Frobenius supplies both sides of a trace formula. On points, it selects the points defined over a finite field. On cohomology, it gives the operator whose trace will count them. The coefficient identification connecting these descriptions matters: the map on the scheme alone does not determine an endomorphism of cohomology with a nonconstant sheaf.

We first distinguish four Frobenius constructions. We then prove a formal lemma about the étale site, use it to prove that absolute Frobenius acts as the identity, and obtain the inverse relation between geometric and arithmetic Frobenius. Finally we define local Frobenius and prove that every scheme-theoretic fixed point has length one. The tangent-space proof gives an additional transversality statement when the scheme is smooth.

Throughout, \(p\) is prime, \(q=p^r\), \(k=\mathbf F_q\), and \(\bar k\) is an algebraic closure. For a \(k\)-scheme \(X_0\), put

\[
X=X_0\times_k\bar k,\qquad a:X\longrightarrow X_0.
\]

Except where a statement explicitly allows arbitrary schemes, \(X_0\) is separated and of finite type over \(k\). Coefficients \(\mathcal F_0\) descend from \(X_0\), and \(\mathcal F=a^{-1}\mathcal F_0\). We use \(\ell\ne p\) for adic coefficients. The first lesson supplies their construction and the meaning of cohomology with compact support. From étale geometry we use the stability of étale maps under base change, topological invariance, and the equivalence between sheaves on a field and discrete continuous Galois sets or modules.

## 1. Four maps and their domains

**Definition 1.1.** For any scheme \(Y\) of characteristic \(p\), its *absolute Frobenius* is

\[
\operatorname{Fr}_Y:Y\longrightarrow Y.
\]

Its map on the underlying space is the identity, and its map on functions is \(b\mapsto b^p\). Indeed, for a prime ideal \(\mathfrak p\), one has \(b^p\in\mathfrak p\) if and only if \(b\in\mathfrak p\). The ring maps glue because taking \(p\)-th powers commutes with restriction. Frobenius is functorial:

\[
h\operatorname{Fr}_Y=\operatorname{Fr}_Z h
\quad\text{for every }h:Y\longrightarrow Z.
\tag{1.1}
\]

For a morphism \(b:Y\to S\) in characteristic \(p\), define the twist and the *relative Frobenius* by

\[
Y^{(p/S)}=Y\times_{S,\operatorname{Fr}_S}S,\qquad
\operatorname{Fr}_{Y/S}=(\operatorname{Fr}_Y,b):
Y\longrightarrow Y^{(p/S)}.
\tag{1.2}
\]

The structure map of the twist is its second projection. Thus relative Frobenius is an \(S\)-morphism, whereas absolute Frobenius usually is not. Its target must be written down. In general \(Y^{(p/S)}\) cannot be identified with \(Y\) as an \(S\)-scheme.

On affine schemes \(S=\operatorname{Spec}(R)\), \(Y=\operatorname{Spec}(B)\), the ring map in (1.2) is

\[
B\otimes_{R,\operatorname{Fr}_R}R\longrightarrow B,
\qquad b\otimes c\longmapsto b^p c.
\tag{1.3}
\]

The tensor relation holds because an element \(d\in R\) acts on the right tensor factor as \(d^p\). Formula (1.3) fixes the second factor, proving the claimed \(S\)-linearity.

Absolute \(p\)-Frobenius on \(X_0\) becomes \(k\)-linear after \(r\) iterations. Write

\[
F_0=\operatorname{Fr}_{X_0}^{\,r}:X_0\longrightarrow X_0,\qquad
F=F_0\times_k\operatorname{id}_{\bar k}:X\longrightarrow X.
\tag{1.4}
\]

The map \(F\) is the *geometric Frobenius morphism* used in this course. It depends on the chosen \(k\)-model \(X_0\). This is the map denoted \(\pi_{X_0}\), and also by \(\pi_{X_0}\) after base change, in [Stacks, Tag 03SQ]. Deligne uses \(F\). On an affine \(k\)-algebra \(A_0\), its ring map is

\[
F^\#(b\otimes c)=b^q\otimes c
\quad(b\in A_0,\ c\in\bar k).
\tag{1.5}
\]

**Definition 1.2.** The *arithmetic Frobenius* is the field automorphism

\[
\sigma:\bar k\longrightarrow\bar k,\qquad c\longmapsto c^q.
\]

It is a topological generator of \(G_k=\operatorname{Gal}(\bar k/k)\). Indeed the roots of \(T^{q^n}-T\) form a field with \(q^n\) elements: the derivative is \(-1\), and the power identity preserves sums, products and inverses. Every finite extension of \(k\) with degree \(n\) has \(q^n\) elements and is exactly this root field. Its \(q\)-power automorphism has order \(n\), since a smaller positive power would put all \(q^n\) elements among the roots of a polynomial of smaller degree. Its \(n\) powers are therefore all its \(k\)-automorphisms. Every element of \(\bar k\) belongs to such a finite field, so \(G_k\) is the inverse limit of these cyclic groups, with \(\sigma\) giving their compatible generators. Its inverse \(\sigma^{-1}\) is the *geometric Frobenius element* of \(G_k\). The scheme map associated with \(\sigma\) is

\[
\tau_\sigma=\operatorname{id}_{X_0}\times\operatorname{Spec}(\sigma):X\longrightarrow X.
\tag{1.6}
\]

This map lies over \(X_0\), but usually does not lie over \(\bar k\). Its ring map is

\[
\tau_\sigma^\#(b\otimes c)=b\otimes c^q.
\]

Consequently

\[
F\tau_\sigma=\tau_\sigma F=\operatorname{Fr}_X^{\,r}.
\tag{1.7}
\]

Both compositions send \(b\otimes c\) to \(b^q\otimes c^q\). The factors commute because they act on different tensor factors.

Here is the distinction on one affine coordinate:

| Construction | Map on a coordinate from \(A_0\) | Map on \(\bar k\)-constants | Target |
|---|---|---|---|
| Absolute \(p\)-Frobenius on \(X\) | \(b\mapsto b^p\) | \(c\mapsto c^p\) | \(X\), as a scheme in characteristic \(p\) |
| Relative \(p\)-Frobenius over \(\bar k\) | \(b\otimes1\mapsto b^p\) in (1.3) | \(1\otimes c\mapsto c\) | \(X^{(p/\bar k)}\) |
| \(F\) from the \(k\)-model | \(b\mapsto b^q\) | \(c\mapsto c\) | \(X\), over \(\bar k\) |
| \(\tau_\sigma\) | \(b\mapsto b\) | \(c\mapsto c^q\) | \(X\), over \(X_0\) |

In particular, \(F\) and \(\operatorname{Fr}_X^{\,r}\) are different maps. The latter is the identity on the topological space of \(X\); the former usually moves its closed points.

For a \(\bar k\)-point \(z\) of \(X_0\), represented on an affine chart by \(z^\#:A_0\to\bar k\), one has

\[
(Fz)^\#(b)=z^\#(b)^q.
\tag{1.8}
\]

This agrees with applying the arithmetic field automorphism to the coordinates. It does not say that the induced operator on cohomology is arithmetic Frobenius. Pullback and the coefficient correspondence will reverse the direction.

## 2. A formal identity on the étale site

The following lemma specifies what is meant by a map acting trivially with arbitrary coefficients. Without a coefficient identification, pullback lands in the cohomology of a different sheaf.

**Lemma 2.1 (the site lemma).** Let \(g:Y\to Y\) be a scheme morphism. Suppose that, for every étale \(\varphi:U\to Y\), there is an isomorphism

\[
\gamma_U:U\xrightarrow{\ \sim\ }g^*U
=U\times_{\varphi,Y,g}Y
\]

over \(Y\), where the target is over \(Y\) by its second projection. Suppose these isomorphisms are natural in \(U\). For every abelian sheaf \(A\) on \(Y_{\mathrm{\acute et}}\), they determine an isomorphism

\[
\beta_g:g^{-1}A\xrightarrow{\ \sim\ }A.
\tag{2.1}
\]

Pullback followed by this isomorphism is the identity:

\[
H^j(Y,A)\xrightarrow{g^*}H^j(Y,g^{-1}A)
\xrightarrow{\beta_g}H^j(Y,A)
=\operatorname{id}\quad(j\geq0).
\tag{2.2}
\]

**Proof.** Direct image on this site is

\[
(g_*A)(U)=A(g^*U).
\]

Restriction along \(\gamma_U^{-1}:g^*U\to U\) gives a natural isomorphism of sheaves

\[
\alpha_A:A\xrightarrow{\ \sim\ }g_*A.
\tag{2.3}
\]

Naturality in \(U\) gives a map of presheaves; its components are isomorphisms, so it is a map of sheaves and an isomorphism there. It is also natural in \(A\).

The étale inverse-image functor \(g^{-1}\) is left adjoint to \(g_*\). For sheaves \(A,B\), the adjunction and (2.3) give natural bijections

\[
\operatorname{Hom}(g^{-1}A,B)
\cong\operatorname{Hom}(A,g_*B)
\xrightarrow{\alpha_B^{-1}\circ-}\operatorname{Hom}(A,B).
\tag{2.4}
\]

The morphism corresponding to \(\operatorname{id}_A\) is \(\beta_g\). Equation (2.4), natural in \(B\), proves by the Yoneda property that \(\beta_g\) is an isomorphism. Equivalently, \(\beta_g\) is the adjoint of \(\alpha_A\). If \(\eta_A:A\to g_*g^{-1}A\) is the unit, the adjunction identity reads

\[
g_*(\beta_g)\eta_A=\alpha_A.
\tag{2.5}
\]

Both functors are equivalences naturally isomorphic to the identity. In particular \(g_*\) is exact and the functors preserve injective sheaves.

The terminal object of the site is \(Y\to Y\). Its base change \(g^*Y\) is canonically \(Y\), by the second projection. Since \(\gamma_Y\) is over \(Y\), it is this canonical identification. Thus evaluation of (2.3) on the terminal object is the identity under

\[
\Gamma(Y,g_*A)=\Gamma(Y,A).
\tag{2.6}
\]

Take an injective resolution \(A\to I^\bullet\). The cohomological pullback followed by \(\beta_g\) is induced by the derived version of the left side of (2.5). Exactness of \(g_*\) lets us compute it using \(I^\bullet\). By (2.5) it is \(\alpha_{I^\bullet}\), and by (2.6) this is the identity on the entire complex of global sections. Hence it is the identity on every cohomology group. This proves (2.2), including degrees not computed by a single Čech cover. \(\square\)

The proof supplies the adjunction and resolution steps implicit in [Stacks, Tag 03SP]. It also explains the direction of (2.1): it is adjoint to the map \(A\to g_*A\), not to its inverse.

**Proposition 2.2.** For an étale map \(\varphi:U\to Y\) in characteristic \(p\), the map

\[
\gamma_U=(\operatorname{Fr}_U,\varphi):
U\longrightarrow U\times_{\varphi,Y,\operatorname{Fr}_Y}Y
\tag{2.7}
\]

is an isomorphism, natural in \(U\).

**Proof.** Equation (1.1) puts the displayed pair in the fibre product. It is the relative Frobenius of the étale map \(U\to Y\). We recall why the étale hypothesis makes this an isomorphism.

Relative Frobenius is a universal homeomorphism. Affine locally its ring map is \(B\otimes_{R,\operatorname{Fr}_R}R\to B\), \(b\otimes c\mapsto b^p c\), which is integral because every \(b\) satisfies \(T^p-b^p\) over the image. Absolute Frobenius is universally bijective on points: over any algebraically closed field, taking \(p\)-th powers has a unique inverse, and the same assertion holds after field extension. The first projection from this fibre product is a base change of absolute Frobenius; its composite with (2.7) is absolute Frobenius on \(U\). This shows that (2.7) is universally bijective on points as well. Together with integrality, it gives the universal-homeomorphism assertion.

Both the source and target of (2.7) are étale over \(Y\). A morphism between two étale \(Y\)-schemes is étale: its graph is a section of an étale morphism and hence an open immersion, and its projection to the target is étale. An étale universal homeomorphism is an isomorphism, since an étale radicial map is an open immersion and a surjective open immersion is an isomorphism. The exact internal proofs are [Étale morphisms and their local structure, Proposition 2.1 and Theorem 4.1](course:AG-FSE/etale-morphisms-and-their-local-structure); the relative Frobenius statement is also [Stacks, Tag 0EBS]. Finally (1.1) proves naturality. \(\square\)

**Theorem 2.3 (absolute Frobenius identity).** For every scheme \(Y\) in characteristic \(p\), every positive integer \(m\), and every \(j\geq0\),

\[
\operatorname{Fr}_Y^*:
H^j(Y,\mathbf Z/m)\longrightarrow H^j(Y,\mathbf Z/m)
\quad\text{is the identity}.
\tag{2.8}
\]

For an arbitrary abelian étale sheaf \(A\), the same statement holds after using the isomorphism \(\beta_{\operatorname{Fr}_Y}\) of Lemma 2.1. All iterates satisfy the corresponding assertion.

**Proof.** Proposition 2.2 verifies the hypotheses of Lemma 2.1. For a constant sheaf, the resulting coefficient isomorphism is the usual identification \(g^{-1}\mathbf Z/m=\mathbf Z/m\): restriction preserves each constant section, and sheafification preserves the resulting natural maps. Equation (2.2) therefore gives (2.8). Iterating the natural isomorphisms gives the result for powers of Frobenius. \(\square\)

This is the baffling theorem [Stacks, Tag 03SN]. It allows \(p\mid m\); no invertibility assumption on \(m\) is used. It concerns the constant étale sheaf \(\mathbf Z/m\), rather than a possibly non-étale group scheme such as \(\mu_p\). Nor does it say that the map \(F\) of (1.4) acts trivially.

## 3. Descent gives the Frobenius correspondence

Apply Lemma 2.1 on \(X_0\) to \(F_0=\operatorname{Fr}_{X_0}^{\,r}\). The maps

\[
\gamma_{U_0}=(\operatorname{Fr}_{U_0}^{\,r},\varphi):
U_0\xrightarrow{\ \sim\ }U_0\times_{\varphi,X_0,F_0}X_0
\tag{3.1}
\]

give a natural isomorphism

\[
\beta_0:F_0^{-1}\mathcal F_0\xrightarrow{\ \sim\ }\mathcal F_0.
\tag{3.2}
\]

Pulling (3.2) to \(X\), and using \(aF=F_0a\), gives the *Frobenius correspondence*

\[
\beta_F:F^{-1}\mathcal F\xrightarrow{\ \sim\ }\mathcal F.
\tag{3.3}
\]

We use the notation \(F^*\) for the entire cohomological operator

\[
H^j(X,\mathcal F)
\xrightarrow{\text{pullback}}H^j(X,F^{-1}\mathcal F)
\xrightarrow{H^j(\beta_F)}H^j(X,\mathcal F).
\tag{3.4}
\]

For a sheaf represented by an étale space \(E_0\to X_0\), formula (3.2) is the inverse of the relative \(q\)-Frobenius \(E_0\to F_0^*E_0\). Thus the inverse in (3.3) is an actual part of the definition, even though the map \(F\) raises point coordinates to their \(q\)-th powers. This construction is [Stacks, Tag 03SR], Deligne, *Cohomologie étale*, [Rapport], §§1.2–1.3, and *Weil I*, §1.11.

For \(s\in G_k\), the map \(\tau_s\) lies over \(X_0\). The equality \(a\tau_s=a\) gives the descent identification

\[
\iota_s:\tau_s^{-1}\mathcal F\xrightarrow{\ \sim\ }\mathcal F.
\]

Define

\[
\rho(s)=H^j(\iota_s)\tau_s^*:H^j(X,\mathcal F)\longrightarrow H^j(X,\mathcal F).
\tag{3.5}
\]

The descent identifications satisfy their composition law. Taking \(\operatorname{Spec}\) reverses composition of field automorphisms, and pullback reverses composition again. It follows that \(\rho(st)=\rho(s)\rho(t)\). Thus (3.5) is a left Galois action.

**Lemma 3.1 (compatibility).** The two correspondences \((F,\beta_F)\) and \((\tau_\sigma,\iota_\sigma)\) commute. Their composite is the absolute \(q\)-Frobenius correspondence

\[
(\operatorname{Fr}_X^{\,r},\beta_{\operatorname{Fr}_X^{\,r}})
\]

from Lemma 2.1.

**Proof.** The underlying maps commute by (1.7). Check the coefficient maps first for the sheaf represented by an étale \(U_0\to X_0\). On \(U=U_0\times_k\bar k\), the maps

\[
\operatorname{Fr}_{U_0}^{\,r}\times\operatorname{id}
\quad\text{and}\quad
\operatorname{id}\times\operatorname{Spec}(\sigma)
\]

commute, and their composite is \(\operatorname{Fr}_U^{\,r}\). Each of their induced maps to the relevant pullback object is an isomorphism. Taking their inverses, as required for the coefficient correspondences, gives precisely the inverse of

\[
(\operatorname{Fr}_U^{\,r},U\to X):
U\longrightarrow U\times_{X,\operatorname{Fr}_X^{\,r}}X.
\]

This is the coefficient map prescribed by Lemma 2.1.

For general abelian \(\mathcal F_0\), take the canonical epimorphism onto it from the direct sum of the free abelian sheaves generated by pairs \((U_0,s)\), where \(s\in\mathcal F_0(U_0)\). The maps just checked agree on every representable generator. All the constructions are natural and inverse image is exact, so they agree after passing to the quotient \(\mathcal F_0\). This proves both commutativity and the composite assertion for all abelian sheaves. \(\square\)

**Theorem 3.2 (inverse relation).** For every \(k\)-scheme \(X_0\), every abelian étale sheaf \(\mathcal F_0\) on it, and every \(j\geq0\), the operator (3.4) satisfies

\[
F^*=\rho(\sigma)^{-1}.
\tag{3.6}
\]

In particular \(F^*\) is invertible.

**Proof.** Lemma 3.1 and functoriality of cohomological pullback identify both \(F^*\rho(\sigma)\) and \(\rho(\sigma)F^*\) with the absolute \(q\)-Frobenius operator having its canonical coefficient identification. Theorem 2.3 says that this composite is the identity. Since \(\rho(\sigma)\) is an automorphism, equation (3.6) follows. \(\square\)

This proves [Stacks, Tag 03SV] with its coefficient compatibility made explicit. It agrees with Deligne's Galois dictionary in *Weil I*, §1.15. For sheaves that do not descend from \(X_0\), there need not be a correspondence (3.3); choosing an unrelated isomorphism \(F^{-1}\mathcal F\simeq\mathcal F\) does not justify (3.6).

### The Galois action on a direct-image stalk

We give the continuity argument needed here, rather than infer higher cohomology from a degree-zero sections calculation.

**Lemma 3.2a (continuity along the finite field extensions).** Let \(X_0\) be quasi-compact and quasi-separated over \(k\), and let \(A_0\) be any abelian étale sheaf. For \(k\subset L\subset\bar k\) finite, put \(X_L=X_0\times_kL\) and \(A_L=A_0|_{X_L}\). With \(A=A_0|_X\), restriction induces, for every \(j\geq0\),

\[
\varinjlim_LH^j(X_L,A_L)\xrightarrow{\sim}H^j(X,A).
\tag{3.7a}
\]

No torsion or constructibility assumption is imposed on \(A_0\).

**Proof.** We first describe the finite data that descend. A quasi-compact quasi-separated étale scheme over \(X\) has a finite affine cover over a finite affine cover of \(X_0\), with finite affine covers of all overlaps. On each affine, an étale algebra has a finite presentation. Its coefficients, its étale presentation witnesses, the gluing maps and their finitely many relations lie in one finite extension \(L/k\). Enlarging \(L\) realizes the relations there. This descends the scheme and any finite diagram of such schemes. One can check the étale witnesses in square Jacobian presentations; their invertible determinants and inverses are finite data. A finite covering family descends as a covering: after its diagram has descended, surjectivity is detected by the faithfully flat base change \(\bar k/L\).

For such a descended scheme \(V_L\), its coefficient sections satisfy

\[
\varinjlim_{L'\supset L} A_{L'}(V_L\times_LL')
\xrightarrow{\sim} A(V_L\times_L\bar k).
\tag{3.7b}
\]

Here is the sheaf argument. The inverse-image presheaf is the colimit of sections of \(A_0\) on étale \(X_0\)-objects equipped with maps from the object in question; inverse image then sheafifies it. A section of the sheafification is represented locally by such sections. Quasi-compactness permits finitely many affine representative charts; quasi-separatedness permits finitely many affine charts on their overlaps. All their maps descend by the preceding finite-presentation argument. Their matching equalities can be represented after a further finite cover, by the local definition of sheafification, and these covers and equality witnesses descend as well. At one common finite extension the representatives therefore glue to a section. This proves surjectivity of (3.7b). If two stage sections have the same pullback, make the same finite choice of charts witnessing their equality. At a common finite extension they agree locally and hence agree by separatedness of the sheaf. This proves injectivity. This argument also proves (3.7b) for sheaves of sets.

For higher cohomology use the full [hypercovering comparison theorem, Theorem 7.1](course:ag-etale-cohomology/hypercoverings), with its refinement and null-coboundary assertions. In degree \(j\), it suffices to use the first \(j+2\) levels, numbered 0 through \(j+1\), of a hypercovering. These levels may be chosen to be finite families of quasi-compact quasi-separated étale schemes. Indeed start with finitely many affine charts covering \(X\). Inductively its matching object is a finite family of quasi-compact quasi-separated étale schemes, formed by finite limits. To refine a prescribed hypercovering, pull back its next matching cover to this family and select finitely many affine covering charts on each component. Use these as the new nondegenerate simplices and include the degeneracies of the previously chosen levels. Their face maps are supplied by the matching object; freely including degeneracies imposes precisely the simplicial identities. This gives the required finite refinement through that degree. To obtain a map to the prescribed full hypercovering, continue with relative matching covers in higher degrees, where no finiteness is required. The resulting full refinement maps canonically to the coskeleton of its finite truncated diagram. That coskeleton is also a hypercovering, because its later matching maps are isomorphisms. Both maps preserve the cochains through degree \(j+1\), so comparison identifies their represented degree-\(j\) classes and boundaries. Products first handle any finite list of prescribed hypercoverings and maps. Thus using a finite truncated diagram and its coskeleton preserves the class or relation under consideration.

Now represent a class of \(H^j(X,A)\) by a cocycle on a hypercovering, and make that finite refinement through level \(j+1\). Descend its finite diagram to one \(L\). By (3.7b), descend the finitely many cochain sections and the cocycle equation after a further finite extension. Extending the descended truncated diagram by coskeleton gives a hypercovering of \(X_L\) with that cocycle. Its comparison class restricts to the original class, proving surjectivity of (3.7a).

If a class from a stage becomes zero, first represent it at that stage using such a finite truncated diagram. Hypercovering comparison over \(\bar k\) realizes its cocycle as a boundary after a refinement. Choose a finite refinement through level \(j+1\), including its map to the stage's truncated diagram, and descend that diagram, the bounding cochain and its boundary equation by (3.7b). It is then already a boundary at one finite extension. In degree zero use the zero-section assertion of (3.7b), without a degree-minus-one cochain. This proves injectivity. All maps used are restrictions, so the resulting isomorphism is the canonical one and is natural in the scheme and coefficient sheaf. \(\square\)

Let \(b_0:X_0\to\operatorname{Spec}(k)\) be the structure map, now with \(X_0\) of finite type. The higher-direct-image stalk formula, [Lemma 2.1 of the direct-image lesson](course:ag-etale-cohomology/pushforward-pullback-and-finite-morphisms), and Lemma 3.2a give

\[
(R^jb_{0*}\mathcal F_0)_{\bar k}
=\varinjlim_{k\subset L\subset\bar k}
H^j(X_0\times_kL,\mathcal F_0|_{X_0\times_kL})
\xrightarrow{\ \sim\ }H^j(X,\mathcal F).
\tag{3.7}
\]

Here \(L/k\) is finite. Quasi-compactness and quasi-separatedness are supplied by finite type and separatedness.

We can check the Galois equivariance of (3.7), rather than assuming a sign convention for it. A neighbourhood of \(\bar k\) is a finite separable extension with an embedding into \(\bar k\). Applying \(s\) changes that embedding by \(s\). On the base-changed scheme, the corresponding transition is the pullback by \(\operatorname{id}\times\operatorname{Spec}(s)\), followed by the identification of the sheaf pulled from \(X_0\). This is exactly (3.5). The same construction computes both sides of (3.7) on a representative class, so their actions agree. Each class is represented over some finite \(L\), and its stabilizer contains an open subgroup. The action on the torsion or discrete-coefficient group in (3.7) is therefore continuous. This supplies the equivariance argument in [Stacks, Tag 03ST] at the finite-type generality used here.

### Compact support and adic coefficients

For separated finite-type \(X_0\) and torsion \(\mathcal F_0\), choose a compactification defined over \(k\),

\[
j_0:X_0\hookrightarrow\overline X_0,\qquad \overline X_0\text{ proper over }k.
\]

Such a compactification and the computation of compact support by \(j_!\) are prerequisites already used in Lesson 1. Frobenius preserves the open subscheme and its complement. On geometric stalks, extension by zero is the original sheaf on the open and zero on the complement. Thus its coefficient correspondence is the one induced from \(\mathcal F_0\), and

\[
H_c^j(X,\mathcal F)=H^j(\overline X,j_!\mathcal F)
\]

has the inverse relation (3.6) by Theorem 3.2 applied to \(j_{0!}\mathcal F_0\).

This also agrees with proper pullback by \(F\). To see properness, for a finite-type affine \(k\)-algebra generated by \(b_1,\ldots,b_m\), the monomials \(b_1^{e_1}\cdots b_m^{e_m}\), \(0\leq e_i<q\), generate it as a module over its \(q\)-power subring: separate every exponent into its multiple of \(q\) and its remainder, and use that the coefficients in \(k\) are \(q\)-th powers. Since absolute Frobenius preserves every open set, this proves that \(F_0\) is finite. Its base change \(F\) is finite, hence proper. Pullback on a compactification consequently induces the usual compact-support pullback.

For a strict adic system \((\mathcal F_{0,n})\), the isomorphisms and equations above are compatible with every reduction map. They therefore hold on the derived inverse-limit complex defining \(R\Gamma\), and on the analogous compact-support complex. Taking cohomology and then inverting \(\ell\) gives

\[
F^*=\rho(\sigma)^{-1}
\quad\text{on }H^j(X,\mathcal F),\ H_c^j(X,\mathcal F)
\]

for the constructible adic and rational adic coefficients of Lesson 1. This argument uses the compatible complexes; it does not discard a possible inverse-limit correction by taking an unjustified limit of cohomology groups.

All constructions are natural in \((X_0,\mathcal F_0)\). More explicitly, if \(h_0:X_0\to Y_0\) and \(u:h_0^{-1}\mathcal G_0\to\mathcal F_0\) are given, the square of coefficient maps obtained from \(u\), \(\beta_{X_0}\) and \(\beta_{Y_0}\) commutes. On representable generators this is (1.1); the epimorphism argument of Lemma 3.1 proves it for all abelian sheaves. It follows that the induced maps on cohomology commute with Frobenius. Applying the natural maps to resolutions gives the corresponding assertion for derived direct images and their cohomology spectral sequences. The geometric base-change identification used with those direct images is justified explicitly below.

### Frobenius on the pro-étale derived category

The site argument also handles the general complete coefficient complexes of Lesson 2. It does not depend on choosing a global lattice or on a coefficient quotient being perfect.

**Proposition 3.3.** Let \(Y\) be any scheme of characteristic \(p\), and let \(K\) be a complex of abelian sheaves on \(Y_{\mathrm{pro\acute et}}\). Absolute Frobenius has a natural coefficient identification under which its pullback on \(R\Gamma(Y,K)\) is the identity. No boundedness, constructibility or torsion assumption on \(K\) is needed. The identification preserves a constant coefficient-ring action and derived completeness for any ideal in that ring.

If \(X_0\) is a scheme over \(\mathbf F_q\), \(K_0\) is such a pro-étale complex on \(X_0\), and \(K\) is its pullback to \(X=X_0\times\overline{\mathbf F}_q\), the correspondence induced from \(K_0\) satisfies
\[
F^*=\rho(\sigma)^{-1}
\quad\text{on }R\Gamma(X,K).
\tag{3.8}
\]
Here \(\rho(\sigma)\) is the map defined by descent, as in (3.5). The assertion specifies these maps; it makes no claim that arbitrary pro-étale coefficients are discrete Galois modules.

**Proof.** Work on the affine ind-étale basis proved in Lesson 2, Theorem 1.1d. Locally over an affine open of \(Y\), an object of this basis has a presentation \(U=\varprojlim U_i\), with affine étale \(U_i\to Y\). Frobenius preserves the open of \(Y\). Base change commutes with this inverse limit, and naturality of relative Frobenius gives
\[
U\longrightarrow U\times_{Y,\operatorname{Fr}_Y}Y
=\varprojlim_i(U_i\times_{Y,\operatorname{Fr}_Y}Y)
\]
as the inverse limit of the isomorphisms of Proposition 2.2. It is therefore an isomorphism. Its formula is the intrinsic relative Frobenius, so it is independent of the presentation and natural for maps between basis objects. These basis objects cover every object of the site; sheaves and maps of sheaves are determined on them.

Consequently the direct-image isomorphism \(A\to\operatorname{Fr}_{Y,*}A\) and its adjoint coefficient isomorphism are constructed exactly as in Lemma 2.1, now on this basis. They make inverse and direct image exact equivalences naturally isomorphic to the identity. Their map on global sections is the identity because the terminal object is identified by its second projection. Apply the equivalence to a K-injective resolution of \(K\). An exact equivalence preserves K-injectives: the Hom-complex from any acyclic complex is transported to the Hom-complex from its acyclic inverse image. The adjunction identity of (2.5) is therefore the identity on the entire complex computing \(R\Gamma\), even for an unbounded \(K\).

Naturality preserves the action of every constant coefficient and every multiplication telescope. It thus preserves the vanishing conditions defining derived completeness. For coefficients in \(\widehat\Lambda\), apply the same identifications to each constant quotient \(\Lambda/I^n\) and to their derived limit; the equivalence preserves those limits and their ring structure.

For the second assertion, the two factors in (1.7) commute on ind-étale basis objects pulled from \(X_0\), just as they do on the étale objects in Lemma 3.1. Passing to their affine inverse limits preserves those equalities and their coefficient maps. Free module sheaves on the basis objects generate all module sheaves; naturality extends the equality to their presentations and then to complexes. The composite correspondence is the absolute \(q\)-Frobenius correspondence, whose map on \(R\Gamma\) was just proved to be the identity. This proves (3.8). \(\square\)

For a constructible complete complex with a complete Noetherian local coefficient ring and finite residue field, the finite reductions are classical bounded étale complexes by Lesson 2. On a separated finite-type scheme over the finite field, its compact-support complex is the derived limit of the corresponding finite compact-support complexes. The earlier compactification argument applies at every level and its maps commute with reduction, so their derived limit also satisfies (3.8). This includes the nonperfect quotient rings treated in Lesson 2. The proof uses compatible complexes and retains any inverse-limit corrections.

**Corollary 3.4 (extension of the finite base field).** Replace \(k=\mathbf F_q\) by \(k_s=\mathbf F_{q^s}\), and pull both \(X_0\) and its coefficients to \(k_s\). After identifying their geometric base changes using an embedding \(k_s\hookrightarrow\bar k\), the new geometric Frobenius operator is \((F^*)^s\), and the arithmetic generator acts by \(\rho(\sigma)^s\). These statements hold for all the étale, adic and pro-étale coefficients above, including the indicated compact-support complexes.

**Proof.** The \(q^s\)-power map on the \(k_s\)-model is the base change of the \(s\)-fold \(q\)-power map on \(X_0\). Its relative Frobenius is the composite of those \(s\) relative Frobenius maps on each étale or ind-étale object. Naturality and taking inverses identify its coefficient correspondence with the composite of the \(s\) correspondences in (3.3). Pullback composition therefore gives \((F^*)^s\). The arithmetic generator of \(k_s\) is \(\sigma^s\), and descent gives \(\rho(\sigma^s)=\rho(\sigma)^s\). Both equalities commute with the compactification and reduction maps, so they also hold after the compatible derived limits. \(\square\)

**Proposition 3.5 (direct images and their Frobenius structures).** Let \(h_0:X_0\to Y_0\) be a morphism between separated finite-type \(k\)-schemes, with geometric base change \(h:X\to Y\), and let \(A_0\) be an abelian étale sheaf. There are canonical identifications

\[
a_Y^{-1}R^jh_{0*}A_0\xrightarrow{\sim}R^jh_*a_X^{-1}A_0.
\tag{3.9}
\]

The correspondence obtained by pulling the Frobenius structure of the left side to \(Y\) is the correspondence induced from \((X,A)\) on the right side. Consequently the Leray spectral sequence is compatible with Frobenius on every page and on its abutment. The analogous statements hold for compact support with torsion or the complete coefficients already treated above.

**Proof.** Every quasi-compact affine étale \(V\to Y\), and any finite diagram of such objects, descends to \(V_L\to Y_L\) for some finite \(L/k\), by the finite-data argument in Lemma 3.2a. As \(Y_L\to Y_0\) is étale, direct image restricted to \(V_L\) is the direct image for the base-changed map: at the site level this is the slice identity, and its exact restriction functor preserves the injective section calculation of the direct-image stalk formula. The inverse-image sheaf on the left of (3.9), evaluated locally on these charts, is therefore obtained by sheafifying the colimit of

\[
H^j(X_0\times_{Y_0}(V_L\times_LL'),A_0)
\qquad(L'\supset L\text{ finite}).
\]

The schemes in this expression are the finite field extensions of the qcqs scheme \(X_0\times_{Y_0}V_L\). Lemma 3.2a identifies their colimit with \(H^j(X\times_YV,A)\). Sheafification of these presheaf cohomology groups is the right side of (3.9), by the direct-image formula. The comparison is restriction of classes, so these identifications commute with every chart map and give the canonical base-change map. They prove (3.9).

The coefficient correspondence is natural on every representable generator, as checked above. Apply it to the injective complexes computing the displayed section groups. The restriction comparisons and their augmentations commute with it, so (3.9) transports the coefficient map on one side to the coefficient map on the other. The Leray spectral sequence comes from these derived functors and their natural resolution maps. A commuting map of the resolution double complexes induces a commuting map on each page and on the filtered abutment, giving the assertion.

For compact support, use the factorization by an open immersion followed by a proper map from [Cohomology with compact support, §§1–3](course:ag-etale-cohomology/cohomology-with-compact-support). Extension by zero commutes with base change on its geometric stalks and with Frobenius because the open and complement are preserved. Proper base change supplies the proper factor and is natural in its coefficient maps. These two comparisons prove the torsion assertion. The finite-level comparisons and correspondences commute with reduction; taking their compatible derived limits proves the complete-coefficient assertion, using the proper comparison of Lesson 2. The same maps of resolutions give the compact-support Leray compatibility. \(\square\)

## 4. Frobenius at a closed point

Let \(x\in|X_0|\) be a closed point. Its residue field is a finite extension of \(k\); write

\[
d_x=[\kappa(x):k],\qquad \kappa(x)\cong\mathbf F_{q^{d_x}}.
\]

Choose a geometric point \(\bar x\) above \(x\). Restriction of \(\mathcal F_0\) to \(\operatorname{Spec}(\kappa(x))\) is a sheaf on a field. Its geometric stalk \(V_x=(\mathcal F_0)_{\bar x}\) is a continuous module for

\[
G_{\kappa(x)}=\operatorname{Gal}(\overline{\kappa(x)}/\kappa(x)).
\]

The arithmetic generator of this group is \(\sigma_x:c\mapsto c^{q^{d_x}}\). The sheaf/Galois-module equivalence used here has its complete proof in [Galois cohomology and the étale cohomology of a field, Theorem 1.1](course:ag-etale-cohomology/galois-cohomology-and-the-etale-cohomology-of-a-field).

**Definition 4.1.** The *local geometric Frobenius* is the stalk operator

\[
F_x=\rho_x(\sigma_x^{-1}):V_x\longrightarrow V_x.
\tag{4.1}
\]

For a constructible sheaf with coefficients in a finite extension \(E/\mathbf Q_\ell\), \(V_x\) is finite-dimensional and we put

\[
P_x(t)=\det(1-tF_x\mid V_x)\in E[t].
\tag{4.2}
\]

One can also take this determinant for a finite free integral or finite-level coefficient module. An arbitrary torsion stalk need not be free, so we do not assign an ordinary matrix determinant to it without a further definition; traces and determinants on perfect complexes are treated in the next lesson.

All traces and L-functions in this course use these geometric Frobenius operators.

**Proposition 4.2.** The conjugacy class of \(F_x\), and hence (4.2), is independent of the geometric point and of the identifications used to define it. If \(\bar x\) is regarded as a \(\bar k\)-point of \(X\), the \(d_x\)-fold iterate of the correspondence (3.3) on its stalk is \(F_x\).

**Proof.** Two choices of separable closure of \(\kappa(x)\) are isomorphic over \(\kappa(x)\). Such an isomorphism transports the stalk and its Galois action. It carries the automorphism \(c\mapsto c^{q^{d_x}}\) to the automorphism given by the same formula. The resulting stalk isomorphism \(T:V_x\to V'_x\) therefore satisfies

\[
F'_x=TF_xT^{-1}.
\tag{4.3}
\]

Different choices of this isomorphism differ by a Galois automorphism; the same intertwining relation still holds. If one instead chooses another embedding \(\kappa(x)\hookrightarrow\bar k\), it is obtained from the original one by a power of \(\sigma\). Descent transports the stalk by that power, and \(\sigma^{d_x}\) commutes with it. This again gives (4.3). A change of basis is another conjugation, so

\[
\det(1-tTF_xT^{-1})=\det\bigl(T(1-tF_x)T^{-1}\bigr)
=\det(1-tF_x).
\]

For the last assertion, base change the closed subscheme \(\operatorname{Spec}(\kappa(x))\subset X_0\) to \(\bar k\). It is a disjoint union of \(d_x\) geometric points, permuted cyclically by \(F\). Its \(d_x\)-th iterate preserves the chosen point. Restrict Theorem 3.2 to this subscheme and take the \(d_x\)-th power. The arithmetic operator on that stalk is \(\sigma_x=\sigma^{d_x}\); its inverse is (4.1). This proves the assertion. \(\square\)

Thus a closed point of degree \(d\) contributes the correspondence for \(F^d\), rather than that for \(F\) on a single chosen stalk. If \(n\) is divisible by \(d\), the operator of \(F^n\) on that stalk is \(F_x^{n/d}\). These distinctions will account for the degrees and exponents in the Euler product of the L-function.

## 5. Fixed points and their multiplicities

**Theorem 5.1.** Let \(X_0\) be any finite-type scheme over \(k\), and \(n\geq1\). The equalizer of \(F^n\) and the identity on \(X\) is a finite reduced \(\bar k\)-scheme whose points are canonically

\[
X_0(\mathbf F_{q^n}).
\tag{5.1}
\]

Every local ring of this fixed-point scheme is \(\bar k\), so every fixed point has length one. If \(X_0\) is smooth and separated over \(k\), the graph of \(F^n\) and the diagonal meet transversally at these points.

**Proof of the scheme-theoretic assertion.** Put \(Q=q^n\). First work on an affine open

\[
U_0=\operatorname{Spec}(A_0),\qquad
A_0=k[t_1,\ldots,t_m]/I.
\]

Every open of \(X_0\) is preserved by \(F_0\), since its underlying topological map is the identity. Consequently \(U=U_0\times_k\bar k\) is preserved by \(F\). On \(U\), the equalizer has ring

\[
B=
\bar k[t_1,\ldots,t_m]/
\bigl(I,\ t_1^Q-t_1,\ldots,t_m^Q-t_m\bigr).
\tag{5.2}
\]

Indeed \(F^{n\#}\) fixes constants and sends each generator \(t_i\) to \(t_i^Q\), so these differences generate the equalizer ideal. The polynomial \(T^Q-T\) has derivative \(-1\), and its roots in \(\bar k\) are exactly \(\mathbf F_Q\). The Chinese remainder theorem gives

\[
\bar k[t_1,\ldots,t_m]/(t_i^Q-t_i)_{i=1}^m
\cong\prod_{\boldsymbol c\in\mathbf F_Q^m}\bar k.
\tag{5.3}
\]

A quotient of a finite product of fields is the product of the factors on which the additional ideal vanishes. Thus (5.2) is the product of one copy of \(\bar k\) for each tuple \(\boldsymbol c\in\mathbf F_Q^m\) satisfying the equations in \(I\). These tuples are precisely \(U_0(\mathbf F_Q)\). This proves finiteness, reducedness and local length one on the chart. It also works when \(A_0\) is nonreduced.

Choose a finite affine open cover of \(X_0\). The associated opens of \(X\) are \(F\)-stable, so the equalizer restricted to each is exactly the equalizer computed above. The identifications with rational points agree on overlaps. The resulting fixed scheme has finitely many points, and each point is open in it and has ring \(\bar k\). It is therefore the disjoint union of these copies of \(\operatorname{Spec}(\bar k)\). This proves (5.1) globally; separatedness was not needed for this part. \(\square\)

**Proof of transversality in the smooth case.** At a fixed point \(z\), the differential of \(F^n\) is zero. On a chart defined over \(k\), the module of relative differentials over \(\bar k\) is generated by the \(dt_i\), and

\[
d(F^{n\#}t_i)=d(t_i^Q)=Q\,t_i^{Q-1}dt_i=0.
\tag{5.4}
\]

The differentials of constants also vanish. If \(d=\dim_z X\), the ambient scheme \(X\times_{\bar k}X\) is smooth of dimension \(2d\) at \((z,z)\), and

\[
T_{(z,z)}\Gamma_{F^n}=\{(v,0):v\in T_zX\},\qquad
T_{(z,z)}\Delta=\{(v,v):v\in T_zX\}.
\]

Their intersection is zero, and their sum is the whole tangent space: \((a,b)=(a-b,0)+(b,b)\). Both subschemes are smooth of dimension \(d\) there. Their local defining equations consequently give \(2d\) independent classes in the cotangent space of the regular local ambient ring. By Nakayama these generate its maximal ideal; they are a regular system of parameters. The intersection ring is its residue field and the transverse local intersection multiplicity is one. \(\square\)

There is also a useful local version of the length argument. At a fixed point, the tangent space of the equalizer is

\[
\ker(dF^n-\operatorname{id})=0
\]

by (5.4), even if \(X\) is singular. Its finite local ring \(R\) has maximal ideal \(\mathfrak m\) with \(\mathfrak m/\mathfrak m^2=0\). Nakayama gives \(\mathfrak m=0\), so \(R=\bar k\). This proves simplicity as a fixed scheme. The smoothness of the ambient scheme is what additionally justifies the transverse intersection calculation.

Finite type is essential for finiteness: the disjoint union of infinitely many copies of \(\operatorname{Spec}(k)\) has infinitely many fixed points. In the applications of this course, \(X_0\) is separated and finite type, so the graph and diagonal are closed and the usual intersection or compact-support constructions apply.

### Closed points are Frobenius orbits

For a closed point \(x\) of degree \(d\), the embeddings \(\kappa(x)\hookrightarrow\bar k\) give exactly \(d\) points of \(X\). They form one orbit of \(F\), because the arithmetic generator cycles the embeddings of a finite field. Conversely every geometric closed point lies over such an \(x\); its orbit has that degree. Consequently

\[
\#X_0(\mathbf F_{q^n})
=\sum_{\substack{x\in|X_0|\\d_x\mid n}}d_x.
\tag{5.5}
\]

The sum is finite by Theorem 5.1. This is a correspondence between degrees and orbits, rather than a new computation of any particular variety's point count. For projective spaces, Grassmannians and flag varieties, use the existing lesson [Counting over finite fields and the limit \(q\to1\)](https://kokunoyumeto.github.io/open-mathematics-courses/courses/the-field-with-one-element/counting-over-finite-fields-and-the-limit-q-1.html).

## 6. Examples that fix the conventions

### The affine line

For \(X_0=\mathbf A_k^1\), the ring map of \(F\) sends \(t\) to \(t^q\) and fixes \(\bar k\). Hence

\[
\operatorname{Fix}(F^n)=
\operatorname{Spec}\bigl(\bar k[t]/(t^{q^n}-t)\bigr)
=\coprod_{c\in\mathbf F_{q^n}}\operatorname{Spec}(\bar k).
\]

On the same ring, absolute \(q\)-Frobenius also raises every constant to its \(q\)-th power. It fixes every underlying point. These two maps already differ on \(\mathbf A^1\).

### A Tate twist

On \(\operatorname{Spec}(k)\), the stalk of \(\mu_{\ell^s}\) is the group of \(\ell^s\)-th roots of unity in \(\bar k\). Arithmetic Frobenius acts by

\[
\zeta\longmapsto\zeta^q.
\]

Passing to the compatible inverse limit gives multiplication by \(q\) on \(\mathbf Z_\ell(1)\). Its inverse is multiplication by \(q^{-1}\), which exists in \(\mathbf Z_\ell\) since \(\ell\ne p\). Thus

\[
\rho(\sigma)\mid\mathbf Z_\ell(1)=q,\qquad
F^*\mid\mathbf Z_\ell(1)=q^{-1}.
\tag{6.1}
\]

Here \(F\) on \(\operatorname{Spec}(\bar k)\) is the identity scheme map. The nontrivial operator \(q^{-1}\) comes entirely from the coefficient correspondence: the inverse relative Frobenius on the étale group \(\mu_{\ell^s}\) is the inverse of raising to the \(q\)-th power. Scheme pullback alone would miss it.

More generally, let \(C\) be the finite set of geometric connected components of \(X\), and let \(\phi:C\to C\) be the permutation induced by \(F\). Locally constant sections give

\[
H^0(X,\mathbf Q_\ell(1))=\prod_{c\in C}\mathbf Q_\ell(1).
\]

After choosing a compatible generator of the Tate twist, define \(P_\phi(v)_c=v_{\phi(c)}\). Pullback and (6.1) give

\[
F^*=q^{-1}P_\phi,\qquad
\rho(\sigma)=qP_\phi^{-1}.
\tag{6.2}
\]

To check the second permutation, (1.7) says that \(\tau_\sigma\) acts on the underlying components as \(\phi^{-1}\). Thus its pullback takes the value at \(\phi^{-1}(c)\), and its coefficient action is \(q\). Equation (6.2) gives \(F^*\rho(\sigma)=1\).

If \(X\) is geometrically connected, this reduces to the two scalars in (6.1). For \(X_0=\operatorname{Spec}(\mathbf F_{q^2})\), however, \(X\) has two points and \(\phi\) interchanges them. The two eigenvalues of \(F^*\) on \(H^0(X,\mathbf Q_\ell(1))\) are \(q^{-1}\) and \(-q^{-1}\), rather than both \(q^{-1}\).

At a closed point of degree \(d\), these conventions give \(F_x=q^{-d}\) on the twist. Its local polynomial is \(1-q^{-d}t\).

### A singular fixed point

Take \(X_0=\operatorname{Spec}(k[u,v]/(uv))\). Its origin is singular. Nevertheless its fixed ring is

\[
\bar k[u,v]/(uv,u^{q^n}-u,v^{q^n}-v).
\]

Equation (5.3) shows that this is reduced. In its local ring at the origin, \(u(u^{q^n-1}-1)=0\) forces \(u=0\), since the parenthesized factor is a unit; similarly \(v=0\). The local ring is \(\bar k\). This illustrates why length one does not require smoothness, while the familiar smooth ambient intersection argument does.

### The elliptic-curve operator

For an elliptic curve \(E_0/k\), put

\[
a=q+1-\#E_0(k).
\]

The geometric Frobenius operator on \(H^1(E,\mathbf Q_\ell)\) will have characteristic polynomial

\[
\det(T-F^*\mid H^1(E,\mathbf Q_\ell))=T^2-aT+q.
\tag{6.3}
\]

The proof and the identification with the point count belong to [Cycle classes and the Lefschetz fixed-point formula for curves], § “Frobenius on an elliptic curve.” Here (6.3) records the operator that will be used, with no point-count theorem assumed. Its arithmetic inverse has polynomial

\[
T^2-\frac aqT+\frac1q.
\]

Indeed the two reciprocal eigenvalues have sum \(a/q\) and product \(1/q\). This distinction will matter in every trace and Euler factor.

## 7. Exercises with complete solutions

**Exercise 7.1 (easy: the target of relative Frobenius).** Prove that relative \(p\)-Frobenius of \(X_0/k\) is \(k\)-linear. Show that absolute \(p\)-Frobenius of a nonempty \(X_0\) is \(k\)-linear if and only if \(q=p\). Explain why \(F_0\) is always \(k\)-linear.

**Solution.** The relative map has target \(X_0^{(p/k)}\) and ring map (1.3). It fixes the second scalar factor, so it is a \(k\)-morphism. If absolute \(p\)-Frobenius were \(k\)-linear, its action on every scalar \(c\in k\) in a nonzero local ring of \(X_0\) would be both \(c\) and \(c^p\). The map from the field \(k\) to that ring is injective. Thus every \(c\in k\) would satisfy \(c^p=c\), forcing \(k=\mathbf F_p\). Conversely for \(k=\mathbf F_p\) the scalar map is the identity. For \(F_0\), one has \(c^q=c\) for all \(c\in k\), so it is always \(k\)-linear. On the empty scheme every scalar condition is vacuous, which explains the nonemptiness hypothesis. In particular “absolute Frobenius” in this exercise means \(p\)-Frobenius; the absolute \(q\)-power map on \(X_0\) is \(k\)-linear.

**Exercise 7.2 (medium: sections and components).** If \(X\) is geometrically connected, prove that \(F^*\) and arithmetic Frobenius act on \(H^0(X,\mathbf Q_\ell(1))\) by \(q^{-1}\) and \(q\), respectively. Give the correct formula without connectedness, and compute the example \(X_0=\operatorname{Spec}(\mathbf F_{q^2})\).

**Solution.** Over \(\bar k\), the twist is a constant rank-one local system. A locally constant section on a connected scheme is constant, so \(H^0\) is one copy of its fibre. The arithmetic action on that fibre raises roots of unity to their \(q\)-th powers, hence is \(q\) on the inverse limit and its rationalization. Theorem 3.2 gives \(q^{-1}\) for \(F^*\).

In general sections have one value on each component. Pullback by \(F\) sends a tuple \(v\) to \((v_{\phi(c)})_c\), and \(\beta_F\) multiplies its values by \(q^{-1}\). This proves (6.2); the arithmetic formula follows either by its direct component action or by inversion. For the quadratic extension, using the two embeddings as a basis, the two matrices are

\[
F^*=q^{-1}
\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\rho(\sigma)=q
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Their product is the identity. Thus connectedness, or at least trivial action on all components, is needed for the unqualified scalar statement.

**Exercise 7.3 (medium: differential and simplicity).** Verify \(dF^n=0\). Deduce local length one at a fixed point. State precisely when graph–diagonal transversality follows.

**Solution.** Relative differentials on an affine chart are generated by \(dt_i\), with constants in \(\bar k\) differentiated to zero. Equation (5.4) kills every generator. The tangent space to the equalizer is the kernel of \(dF^n-1=-1\), so it is zero. Theorem 5.1, or its affine finite-ring part, makes the fixed local ring finite. Its maximal ideal satisfies \(\mathfrak m/\mathfrak m^2=0\), so Nakayama gives \(\mathfrak m=0\); the local ring has length one. If \(X\) is smooth, the ambient product is smooth and the two tangent spaces are the complementary subspaces \((v,0)\) and \((v,v)\). They give the transverse intersection of Theorem 5.1. At a singular point, the fixed-ring length assertion remains valid, but that smooth ambient intersection argument is unavailable.

**Exercise 7.4 (medium: a local characteristic polynomial).** Let \(\mathcal F_0\) be a constructible \(E\)-sheaf and \(x\) a closed point. Show directly that \(P_x(t)\) does not depend on \(\bar x\), and determine the operator at a fixed geometric point for \(F^n\) when \(d_x\mid n\).

**Solution.** An isomorphism of separable closures over \(\kappa(x)\) identifies the stalks and conjugates their Galois representations. It preserves the arithmetic generator because that generator is characterized by \(c\mapsto c^{q^{d_x}}\). Thus the geometric operators are \(F'_x=TF_xT^{-1}\), and taking the determinant of \(T(1-tF_x)T^{-1}\) proves independence. Replacing the embedding of \(\kappa(x)\) into \(\bar k\) transports this data by a power of \(\sigma\), which commutes with \(\sigma^{d_x}\), so it has the same effect. The \(d_x\)-fold geometric correspondence is \(F_x\) by Proposition 4.2. Composing it \(n/d_x\) times gives \(F_x^{n/d_x}\).

**Exercise 7.5 (hard: torsors and all degrees).** Prove (2.8) in degree one by torsors. Then explain why the site lemma proves all degrees, including those not computed by a single Čech covering.

**Solution.** Put \(A=\mathbf Z/m\). Degree-one classes classify étale \(A\)-torsors \(P\to Y\). Such a torsor is an étale scheme over \(Y\), and Proposition 2.2 gives an isomorphism

\[
\gamma_P:P\xrightarrow{\ \sim\ }\operatorname{Fr}_Y^*P.
\]

It is \(A\)-equivariant. For any element of \(A\), translation is an automorphism of the étale \(Y\)-scheme \(P\); naturality of \(\gamma\) says that this translation commutes with \(\gamma_P\). More intrinsically, the constant group \(A\) is represented by the disjoint union of copies of \(Y\), and its relative Frobenius is the usual identification with its pullback; the product action obeys the same naturality square. Thus pullback preserves the torsor's isomorphism class, which proves the identity on \(H^1\), even when \(p\mid m\).

In every degree, apply Lemma 2.1. Its natural maps \(\alpha_A\) and \(\beta_g\) are related by the adjunction identity (2.5). The exact equivalences \(g_*\) and \(g^{-1}\) preserve injective resolutions. On their complexes of global sections the composite is the identity, since \(\gamma_Y\) is the canonical terminal-object identification. Taking cohomology gives the identity in all degrees. This proof works for derived sheaf cohomology and requires no assertion that ordinary Čech cohomology always suffices.

**Exercise 7.6 (hard: an orbit of stalks).** Let \(x\) have degree \(d\), and label its geometric points \(z_0,\ldots,z_{d-1}\) so that \(Fz_i=z_{i+1}\), indices taken modulo \(d\). Write \(B_i:V_{i+1}\to V_i\) for the stalk map of (3.3). Prove that the products around the orbit have the same characteristic polynomial and that each is a local geometric Frobenius.

**Solution.** Each \(B_i\) is an isomorphism. The product starting at \(V_0\) is

\[
T_0=B_0B_1\cdots B_{d-1}:V_0\longrightarrow V_0.
\]

The product starting at \(V_1\) is \(T_1=B_1\cdots B_{d-1}B_0\), and \(T_0=B_0T_1B_0^{-1}\). Repeating this argument around the orbit conjugates all products. Their characteristic polynomials agree. Each product is the stalk correspondence of \(F^d\), so Proposition 4.2 identifies it with the geometric Frobenius of \(\kappa(x)\) on the corresponding stalk. This proves both assertions without requiring the sheaf to be lisse on a neighbourhood of \(x\).

## What this lesson does not prove

- The elementary étale-site foundations used in Proposition 2.2: cancellation and the étale radicial open-immersion criterion have the exact internal proofs [AG-FSE, Proposition 2.1 and Theorem 4.1](course:AG-FSE/etale-morphisms-and-their-local-structure). Those proofs retain the preceding unramified-diagonal and flat-openness inputs. The relative Frobenius argument itself is written above; [Stacks, Tag 0EBS] is its comparison locator.
- The equivalence between étale sheaves on a field and discrete continuous Galois sets or modules, used to interpret (4.1), is [Theorem 1.1 of the field lesson](course:ag-etale-cohomology/galois-cohomology-and-the-etale-cohomology-of-a-field).
- The refinement of weakly étale covers by the affine ind-étale basis used in Proposition 3.3. Its complete proof is in the preceding pro-étale lesson, Theorem 1.1d; taking inverse limits proves the Frobenius assertion on that basis here.
- The higher-direct-image stalk formula is [Lemma 2.1 of the direct-image lesson](course:ag-etale-cohomology/pushforward-pullback-and-finite-morphisms). The finite-field continuity needed in (3.7) is proved here in Lemma 3.2a using [the full hypercovering comparison, Theorem 7.1](course:ag-etale-cohomology/hypercoverings). General qcqs inverse-system continuity, [Stacks, Tags 03Q6 and 09YQ], remains a broader input of the preceding pro-étale lesson; it is not substituted for the proof just given.
- Compactification and the computation \(R\Gamma_c=R\Gamma(\overline X,j_!(-))\) have the exact home [Cohomology with compact support, §§1–3](course:ag-etale-cohomology/cohomology-with-compact-support), retaining its stated Nagata compactification input. The compatible adic complexes are constructed in Lesson 1. General complete coefficients use the written reduction and base-change arguments of Lesson 2.
- The elliptic-curve polynomial (6.3), whose proof is deferred to the named section of Lesson 5. The trace formulas themselves begin in the later curve and higher-dimensional lessons.

<a id="references-and-source-record"></a>

## References

The main reference is [Stacks, The Trace Formula, “Frobenii,” Tag 03SL](https://stacks.math.columbia.edu/tag/03SL): the site lemma is [Tag 03SP](https://stacks.math.columbia.edu/tag/03SP), the absolute Frobenius theorem [Tag 03SN](https://stacks.math.columbia.edu/tag/03SN), the conventions [Tags 03SQ](https://stacks.math.columbia.edu/tag/03SQ) and [03SU](https://stacks.math.columbia.edu/tag/03SU), the sheaf correspondence [Tag 03SR](https://stacks.math.columbia.edu/tag/03SR), stalk-action compatibility [Tag 03ST](https://stacks.math.columbia.edu/tag/03ST), the inverse relation [Tag 03SV](https://stacks.math.columbia.edu/tag/03SV), and local Frobenius [Tag 03SW](https://stacks.math.columbia.edu/tag/03SW).

The chapter is available in [AI Integrated Stacks Project, English, The Trace Formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-frobenii), with [the source edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/trace.tex). This AI-integrated edition retains the upstream locators. The upstream tags identify the underlying results. The formal proof abbreviated at Tag 03SP and the omitted Galois-equivariance proof at Tag 03ST are supplied in §§2–3. Proposition 3.3 extends the identity to arbitrary unbounded pro-étale complexes and complete Noetherian coefficients; Lemma 3.2a supplies finite-field continuity, and Corollary 3.4 makes the finite-extension power compatibility explicit.

Deligne, [*Cohomologie étale* (SGA \(4\frac12\))](https://publications.ias.edu/sites/default/files/Number32.pdf), [Rapport], §§1.1–1.5, printed pp. 77–79, distinguishes the maps, constructs the coefficient correspondence and records its functoriality and behaviour under finite-field extension. Deligne, [*La conjecture de Weil. I*](https://publications.ias.edu/sites/default/files/Number23.pdf), §1.4, printed pp. 274–275; §1.11, printed p. 278; and §1.15, printed p. 279, provides the point-orbit description, the sheaf correspondence and the Galois dictionary. Sections 4–5 of this lesson prove the local and fixed-point assertions directly. These human sources retain their own terms. This lesson's exposition and proofs have the CC0 dedication stated above.

The historical construction is also in Houzel, SGA 5, Exposé XV, §1 “Frobenius morphism” and §2 “Frobenius correspondence.” Its adjunction definition makes the inverse direction in (3.2) especially clear.

- [Bhatt–Scholze, *The pro-étale topology for schemes*, arXiv1309.1198v2](https://arxiv.org/html/1309.1198v2), §4: the ind-étale basis used in Proposition 3.3. The site, completion and coefficient constructions are developed in The pro-étale site and ℓ-adic complexes.

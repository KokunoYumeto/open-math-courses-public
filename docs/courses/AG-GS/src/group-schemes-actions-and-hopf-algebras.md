# Group schemes, actions and Hopf algebras

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A group can carry algebraic geometry as well as a multiplication law. Matrix groups are the first examples, but equations can also describe groups whose structure is invisible on field-valued points. This lesson develops three ways to read that structure: equations with a comultiplication, actions with a coaction, and differential forms transported from the identity. Finite commutative groups admit a fourth description, Cartier duality, which interchanges functions and linear functionals.

We assume the affine scheme–ring correspondence, fibre products, quasi-coherent sheaves on affine schemes, tensor products and Kähler differentials. The lessons *Schemes and their functors of points* and *Quasi-coherent sheaves* supply the geometric background; [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80) supplies the functor language. A reader who knows these facts can start here. Basic references are [Stacks] and [Milne]. The proofs below work over an arbitrary base ring unless a field is explicitly specified.

## 1. Groups that field-valued points cannot distinguish

Let \(S\) be a scheme. For an \(S\)-scheme \(G\), write

\[
G(T)=\operatorname{Hom}_S(T,G).
\]

A **group scheme** over \(S\) is an \(S\)-scheme with a group structure on every \(G(T)\), compatible with pullback along every morphism \(T'\to T\). Equivalently, it has morphisms

\[
m:G\times_S G\longrightarrow G,\qquad e:S\longrightarrow G,
\qquad i:G\longrightarrow G
\]

for multiplication, identity and inverse, satisfying the group identities as identities of morphisms. For example, associativity says that \(m\circ(m\times1)=m\circ(1\times m)\). The equivalence follows from Yoneda: a natural operation on represented functors comes from a unique morphism, and an identity checked on every test scheme is an identity of morphisms. A reference for these definitions is [Stacks, Tag 022S].

When \(S=\operatorname{Spec}R\), a useful list is:

| Group | Points on an \(R\)-algebra \(B\) |
|---|---|
| Additive group \(\mathbf G_a\) | \(B\), with addition |
| Multiplicative group \(\mathbf G_m\) | \(B^\times\) |
| Roots of unity \(\mu_n\), \(n\geq1\) | \(\{b\in B^\times:b^n=1\}\) |
| General linear group \(\mathrm{GL}_r\) | Invertible \(r\times r\) matrices over \(B\) |
| Special linear group \(\mathrm{SL}_r\) | Matrices of determinant \(1\) |

Their coordinate algebras are:

| Group | Coordinate algebra |
|---|---|
| \(\mathbf G_a\) | \(R[x]\) |
| \(\mathbf G_m\) | \(R[t,t^{-1}]\) |
| \(\mu_n\) | \(R[t]/(t^n-1)\) |
| \(\mathrm{GL}_r\) | \(R[x_{ij},\det(x)^{-1}]\) |
| \(\mathrm{SL}_r\) | \(R[x_{ij}]/(\det(x)-1)\) |

The displayed functors are represented because an algebra homomorphism out of the indicated ring amounts exactly to a choice of its generators satisfying the indicated conditions. In the ring for \(\mu_n\), \(t\) is already invertible, with inverse \(t^{n-1}\). All these constructions commute with changing \(R\).

**Example 1.1. Infinitesimal roots of unity.** Over a field \(k\) of characteristic \(p>0\), put \(u=t-1\). Then

\[
k[\mu_p]=k[u]/(u^p).
\]

Its spectrum has one point and has nonzero nilpotents. For every field extension \(K/k\), \(\mu_p(K)=\{1\}\); over \(B=k[\varepsilon]/(\varepsilon^2)\), however, every \(1+c\varepsilon\) belongs to \(\mu_p(B)\). The trivial group scheme has only one point on *every* \(B\). Thus the two group schemes differ even though their points over all fields agree.

**Example 1.2. A second infinitesimal group.** On an \(\mathbf F_p\)-scheme, the map \(F:\mathbf G_a\to\mathbf G_a\) given on points by \(b\mapsto b^p\) is a homomorphism, since \((b+c)^p=b^p+c^p\). Its kernel is

\[
\alpha_p=\operatorname{Spec}R[x]/(x^p),\qquad
\alpha_p(B)=\{b\in B:b^p=0\},
\]

with addition. Although \(\alpha_p\) and \(\mu_p\) have isomorphic underlying schemes over \(\mathbf F_p\), their multiplication laws differ: \(u\) in \(\mu_p\) combines by \(u+v+uv\), whereas \(x\) in \(\alpha_p\) combines by \(x+y\).

A **homomorphism** of group schemes is a morphism inducing group homomorphisms on all test schemes. Its kernel is the fibre product with the target's identity section. Consequently kernels commute with base change. If the target is separated, its identity section is closed, so the kernel is a closed subgroup. The determinant is a homomorphism \(\mathrm{GL}_r\to\mathbf G_m\), and its kernel is \(\mathrm{SL}_r\).

An abstract group \(\Gamma\) also gives a constant group scheme \(\Gamma_S=\coprod_{\gamma\in\Gamma}S\). Its \(T\)-points are locally constant maps from \(T\) to \(\Gamma\), rather than just elements of \(\Gamma\) when \(T\) is disconnected. Multiplication is defined on the components by the multiplication in \(\Gamma\). For finite \(\Gamma\) over \(R\), its coordinate ring is \(R^\Gamma\).

We call a group scheme flat or smooth when its structure morphism has that property. These adjectives are additional hypotheses. For example, \(\mu_p\) and \(\alpha_p\) over a field are finite flat, but are not smooth. In later lessons the difference between their tangent dimension and their dimension will detect the failure of smoothness.

### 1.3. Universal tests and internal morphisms

**Proposition 1.3. Internal Hom and schematic conditions.** For contravariant functors \(F,E\) on \(S\)-schemes, define

\[
\underline{\operatorname{Hom}}(F,E)(T)
=\operatorname{Hom}(F|_T,E|_T),
\]

where the restrictions are functors on all \(T\)-schemes, and the right side consists of natural transformations. These sets form a functor with evaluation and the currying identity

\[
\operatorname{Hom}(K,\underline{\operatorname{Hom}}(F,E))
\simeq\operatorname{Hom}(K\times F,E).
\]

Internal Isom is the subfunctor of pairs of inverse internal morphisms. Internal Aut has its composition group law. An action of a group functor \(G\) on \(F\) is equivalently a homomorphism \(G\to\underline{\operatorname{Aut}}(F)\). These constructions do not assert representability of Hom, Isom or Aut.

**Proof.** Restriction along \(T'\to T\) defines the transition map. If \(u:K\to\underline{\operatorname{Hom}}(F,E)\), then on \(T\) send \((k,f)\) to the value at \(f\) of the transformation \(u(k)\). Conversely, given \(v:K\times F\to E\), an element \(k\in K(T)\) gives, on every \(T'\to T\), the map \(f\mapsto v(k|_{T'},f)\). Naturality of \(v\) makes these a transformation on the entire slice category. These operations are inverse on every element, proving currying. Composition is natural under restriction; an invertible transformation is exactly a pair whose composites are the identity. Currying then translates the action law and identity law into the homomorphism law for internal Aut. \(\square\)

In particular a universal fixed-point condition means fixed after **every** further base change, not only by elements of \(G(T)\) at the current test. For a subfunctor \(H\subset G\), its normalizer requires equality \(gH_{T'}g^{-1}=H_{T'}\) on all further tests; inclusion alone does not define the normalizer group. A centralizer requires \(gh=hg\) for all those \(h\). These definitions explain the universal fixed loci and transporter schemes constructed in *Diagonalizable groups*, Propositions 3.2 and 4.10–4.11.

A split homomorphism of group functors \(f:W\to G\), with homomorphic section \(s\), also identifies \(W\) with \(H\rtimes G\), where \(H=\ker f\) and \(g\) acts on \(H\) by conjugation by \(s(g)\). Indeed every \(w\) has the unique decomposition \(w=(w s(f(w))^{-1})s(f(w))\), whose first factor is in \(H\). Multiplying two decompositions gives \((h,g)(h',g')=(h s(g)h's(g)^{-1},gg')\). The formulas are natural on all tests; for group schemes the represented kernel and Yoneda therefore give the same semidirect-product isomorphism of schemes.

## 2. Reading multiplication backwards

Let \(G=\operatorname{Spec}H\) be affine over \(R\). Pulling back functions along multiplication gives an \(R\)-algebra map

\[
\Delta:H\longrightarrow H\otimes_RH.
\]

The identity and inverse give \(\epsilon:H\to R\) and \(\sigma:H\to H\). Write \(\eta:R\to H\) for the unit and \(\mu_H:H\otimes H\to H\) for ring multiplication. The group identities become

\[
(\Delta\otimes1)\Delta=(1\otimes\Delta)\Delta,
\qquad (\epsilon\otimes1)\Delta=1=(1\otimes\epsilon)\Delta,
\]

\[
\mu_H(\sigma\otimes1)\Delta=\eta\epsilon
=\mu_H(1\otimes\sigma)\Delta.
\]

Here the \(1\) in the counit identities denotes the identity map on \(H\), after identifying \(R\otimes H\) and \(H\otimes R\) with \(H\). A **commutative Hopf \(R\)-algebra** is a commutative \(R\)-algebra with these three structure maps and identities. In this lesson the antipode \(\sigma\) is an \(R\)-algebra map; commutativity makes the usual reversed-multiplication condition equivalent to this one. Commutativity of \(H\) concerns multiplication of functions. Commutativity of the *group* is the extra condition \(\Delta=\tau\Delta\), where \(\tau\) switches tensor factors.

**Theorem 2.1. Affine dictionary.** Affine group schemes over \(R\) are anti-equivalent to commutative Hopf \(R\)-algebras. No flatness or finiteness assumption is needed.

**Proof.** Starting from a group scheme, the preceding identities follow by pulling back the corresponding diagrams. Conversely, suppose \(H\) is such a Hopf algebra. For \(g,h:H\to B\), define

\[
(gh)(a)=\mu_B(g\otimes h)\Delta(a).
\]

Because \(H\) and \(B\) are commutative and \(\Delta,g,h\) are algebra maps, \(gh\) is again an algebra map. Its identity is \(\eta_B\epsilon\), and the inverse of \(g\) is \(g\sigma\). Applying the three Hopf identities shows, respectively, associativity, the two identity laws and the two inverse laws. These operations are natural in \(B\). They therefore define a group scheme on \(\operatorname{Spec}H\), including on nonaffine test schemes by gluing, or directly by taking spectra of the structure maps.

If \(G\to G'\) is a homomorphism, its pullback \(H'\to H\) preserves \(\Delta,\epsilon,\sigma\). Conversely a map preserving those operations induces a group homomorphism on every test algebra. The affine scheme–ring equivalence shows that the two constructions on objects and morphisms are inverse. This proves the anti-equivalence. \(\square\)

The theorem does not say that every group scheme is affine. A positive-dimensional abelian variety, for example, is proper and has only constant global regular functions. Taking the spectrum of its global functions would lose the variety. The Hopf dictionary reconstructs affine group schemes.

Here are the structure maps in examples:

\[
\begin{array}{c|ccc}
&\Delta&\epsilon&\sigma\\ \hline
\mathbf G_a&x\mapsto x\otimes1+1\otimes x&x\mapsto0&x\mapsto-x\\
\mathbf G_m&t\mapsto t\otimes t&t\mapsto1&t\mapsto t^{-1}\\
\mu_n&t\mapsto t\otimes t&t\mapsto1&t\mapsto t^{n-1}.
\end{array}
\]

The additive formula descends to \(R[x]/(x^p)\) in characteristic \(p\), because \(\Delta(x^p)=x^p\otimes1+1\otimes x^p\). In contrast, the coordinate \(u=t-1\) on \(\mu_p\) satisfies

\[
\Delta(u)=u\otimes1+1\otimes u+u\otimes u.
\]

For \(\mathrm{GL}_r\), ordinary matrix multiplication gives

\[
\Delta(x_{ij})=\sum_{a=1}^r x_{ia}\otimes x_{aj},\qquad
\epsilon(x_{ij})=\delta_{ij},\qquad
\sigma((x_{ij}))=(x_{ij})^{-1}.
\]

The inverse entries belong to the coordinate ring by the adjugate formula. The determinant is group-like: \(\Delta(\det)=\det\otimes\det\). Thus the ideal \((\det-1)\) defines a subgroup and gives the formulas for \(\mathrm{SL}_r\).

For a finite constant group write \(\delta_\gamma\) for the function that is \(1\) on \(\gamma\) and \(0\) elsewhere. Then

\[
\Delta(\delta_\gamma)=\sum_{ab=\gamma}\delta_a\otimes\delta_b,
\quad \epsilon(\delta_\gamma)=\begin{cases}1&\gamma=1,\\0&\gamma\ne1,\end{cases}
\quad \sigma(\delta_\gamma)=\delta_{\gamma^{-1}}.
\]

These formulas explain why the coordinate algebra is commutative even if \(\Gamma\) is not.

Finally, a closed subgroup of an affine group is described by an ideal \(I\subset H\) for which the three maps descend to \(H/I\). Equivalently,

\[
\Delta(I)\subset\operatorname{im}(I\otimes H+H\otimes I\to H\otimes H),
\quad\epsilon(I)=0,\quad\sigma(I)\subset I.
\]

Right exactness of tensor product identifies the kernel of \(H\otimes H\to(H/I)\otimes(H/I)\) with the indicated image, even over a ring. Such an ideal is a Hopf ideal. This formulation avoids assuming tensor products of arbitrary submodules are injective.

### 2.2. Hopf algebras on a scheme

**Proposition 2.2. Relative affine dictionary.** For every scheme \(S\), affine \(S\)-group schemes are anti-equivalent to quasi-coherent commutative Hopf \(\mathcal O_S\)-algebras. Formation of the dictionary commutes with arbitrary base change. No flatness hypothesis is required.

**Proof.** An affine morphism \(f:G\to S\) is recovered as \(\operatorname{Spec}_S\mathcal H\), where \(\mathcal H=f_*\mathcal O_G\) is a quasi-coherent algebra. On an affine open \(U=\operatorname{Spec}R\), its restriction is the algebra \(H\) of Theorem 2.1. Multiplication, identity and inverse give maps of sheaves \(\mathcal H\to\mathcal H\otimes\mathcal H\), \(\mathcal H\to\mathcal O_S\), and \(\mathcal H\to\mathcal H\) satisfying that theorem's identities. Conversely these maps give the three morphisms of relative spectra, and their identities can be checked on affine opens. Maps of quasi-coherent algebras and morphisms of affine schemes glue uniquely; thus the local inverse equivalences give the asserted equivalence on objects and morphisms. Pullback of an algebra is its tensor extension, and relative spectrum and its multiplication fibre product have the same base-change formula. Consequently the equivalence also respects every change of base. \(\square\)

### 2.3. Two module functors

For a quasi-coherent \(\mathcal O_S\)-module \(\mathcal P\), distinguish

\[
\begin{aligned}
V(\mathcal P)(T)&=\operatorname{Hom}_{\mathcal O_T}(\mathcal P_T,\mathcal O_T),\\
W(\mathcal P)(T)&=\Gamma(T,\mathcal P_T).
\end{aligned}
\]

Morphisms of these module functors are required to be \(\Gamma(T,\mathcal O_T)\)-linear on every \(T\). This is stronger than being a homomorphism of their additive group functors.

**Proposition 2.3. Module functors and duality.** The functor \(V(\mathcal P)\) is represented by \(\operatorname{Spec}_S\operatorname{Sym}\mathcal P\), with primitive generators. The assignments \(\mathcal P\mapsto W(\mathcal P)\) and \(\mathcal P\mapsto V(\mathcal P)\) are respectively fully faithful covariant and contravariant functors for linear morphisms. For a finite locally free \(\mathcal P\),

\[
W(\mathcal P)=V(\mathcal P^\vee).
\]

Over an affine base, \(V(P)\) is of finite type, respectively finite presentation, exactly when \(P\) is a finitely generated, respectively finitely presented, module.

**Proof.** The universal property of the symmetric algebra identifies its algebra homomorphisms to \(B\) with linear maps \(P\to B\). Sending a generator \(p\) to \(p\otimes1+1\otimes p\), to \(0\), and to \(-p\) gives its additive Hopf structure. This construction is local on \(S\) and glues.

A natural linear map \(W(P)\to W(Q)\) on an affine base is determined by its value \(f:P\to Q\) at \(R\): naturality determines the image of \(p\otimes1\), and \(B\)-linearity then determines the image of every \(p\otimes b\). It is exactly \(f\otimes B\). For \(V\), Yoneda identifies a natural map \(V(Q)\to V(P)\) with an algebra map \(\operatorname{Sym}P\to\operatorname{Sym}Q\). Linearity includes compatibility with scalar multiplication by the universal scalar \(t\) over \(R[t]\). If the image of \(p\in P\) has homogeneous components \(b_d\), this compatibility says

\[
\sum_d t^d b_d=t\sum_d b_d.
\]

Independence of powers of \(t\) forces \(b_d=0\) for \(d\ne1\). The map therefore comes from a unique \(P\to Q\). Conversely every such module map gives a linear map of functors. Restricting to affine opens proves both full-faithfulness statements on \(S\). Finite locally free tensor duality proves the displayed identification with \(W\).

If \(P\) is generated by finitely many elements, its symmetric algebra is a quotient of a polynomial ring on those generators. Conversely finitely many algebra generators of \(\operatorname{Sym}P\), replaced by their finitely many homogeneous components, generate its degree-one part \(P\) as a module. If \(P\) has a finite module presentation, its symmetric algebra has the same generators with the finitely many linear relations. Conversely choose a surjection \(R^n\to P\). If \(\operatorname{Sym}P\) is finitely presented, the kernel of \(R[x_1,\ldots,x_n]\to\operatorname{Sym}P\) is a finitely generated homogeneous ideal. Replacing finite ideal generators by their homogeneous components still gives finite generators. Its degree-one part, the kernel of \(R^n\to P\), is generated by their degree-one components: the degree-zero part of this ideal is zero. Thus \(P\) is finitely presented. \(\square\)

Full faithfulness on each test scheme also identifies internal linear Hom from \(W(\mathcal P)\) to \(W(\mathcal Q)\) with internal linear Hom from \(V(\mathcal Q)\) to \(V(\mathcal P)\): both have, on \(T\), the set of sheaf homomorphisms \(\mathcal P_T\to\mathcal Q_T\). This assertion concerns the internal functor and does not identify it with a tensor extension of the Hom module on the original base.

In characteristic \(p\), \(x\mapsto x^p\) on \(\mathbf G_a\) is an additive homomorphism, but is not a linear module-functor map. Indeed its scalar identity would require \((tx)^p=t x^p\) over \(k[t,x]\). This explains the linearity condition in Proposition 2.3.

**Theorem 2.4. Representability of the section functor.** Over an affine base \(\operatorname{Spec}R\), the functor \(W(P)\), on all \(R\)-algebras, is represented by a scheme if and only if \(P\) is finite projective. When it is represented, it is the affine vector group \(\operatorname{Spec}\operatorname{Sym}P^\vee\). On a general base the corresponding condition is finite local freeness.

**Proof.** Sufficiency follows from Proposition 2.3. For necessity, suppose a scheme \(X\) represents \(W(P)\), and let \(e:\operatorname{Spec}R\to X\) correspond to zero. Put \(Q=\Gamma(\operatorname{Spec}R,e^*\Omega_{X/R})\). For every \(R\)-module \(L\), lifts of \(e\) to \(\operatorname{Spec}(R\oplus L)\), where \(L^2=0\), are naturally

\[
\operatorname{Hom}_R(Q,L).
\]

To verify this formula, on an affine chart a lift of a ring map \(a\mapsto e(a)\) has the form \(a\mapsto(e(a),d(a))\). The ring identities say exactly that \(d\) is an \(R\)-derivation into \(L\), hence a homomorphism from the pulled-back differential module. These descriptions agree on overlaps and glue; the square-zero thickening has the same underlying points as \(\operatorname{Spec}R\). In the represented functor the same kernel is \(P\otimes_R L\). Naturality under sums and scalar maps of \(L\) identifies these as module functors. Therefore

\[
\operatorname{Hom}_R(Q,L)\simeq P\otimes_R L
\]

for all \(L\). The right side is right exact, while the left side is always left exact. Thus \(Q\) is projective. This is also seen directly by applying the resulting surjectivity of \(\operatorname{Hom}(Q,-)\) to a free-module surjection onto \(Q\), which supplies a splitting.

Moreover this isomorphism says that \(\operatorname{Hom}(Q,-)\) commutes with arbitrary direct sums. Embed the projective module \(Q\) as a summand of a free module \(R^{(I)}\). The embedding belongs to \(\operatorname{Hom}(Q,R^{(I)})=\bigoplus_I\operatorname{Hom}(Q,R)\), so it has only finitely many nonzero coordinates. The splitting consequently factors through a finite free module. Hence \(Q\) is finite projective. Taking \(L=R\) gives \(P\simeq Q^\vee\), so \(P\) is finite projective as well. On a general \(S\), necessity follows on affine opens and sufficiency glues the vector groups. \(\square\)

For a finite locally free \(\mathcal P\) and any quasi-coherent \(\mathcal Q\), the natural map

\[
W\bigl(\mathcal Hom(\mathcal P,\mathcal Q)\bigr)
\longrightarrow\underline{\operatorname{Hom}}_{\mathrm{linear}}
\bigl(W(\mathcal P),W(\mathcal Q)\bigr)
\]

is an isomorphism, including after arbitrary base change: locally it is the assertion \(\operatorname{Hom}(R^r,Q)\otimes B=\operatorname{Hom}(B^r,Q\otimes B)\). There is no such unrestricted identification for arbitrary \(\mathcal P\). For instance \(P=\mathbf Z/2\), \(Q=\mathbf Z\) has zero \(\operatorname{Hom}_{\mathbf Z}(P,Q)\), whereas the Hom after reduction to \(\mathbf F_2\) is \(\mathbf F_2\). For an End example, take \(P=\mathbf Z\oplus\mathbf Z/2\): its integral endomorphisms have zero component from the torsion summand to the free summand. Reduction of that End module therefore misses the upper-right entry of the full matrix algebra \(\operatorname{End}_{\mathbf F_2}(P\otimes\mathbf F_2)\).

For any quasi-coherent algebra \(\mathcal A\), the internal functor of all natural maps, with no linearity imposed on the source, satisfies

\[
\underline{\operatorname{Hom}}(\operatorname{Spec}_S\mathcal A,W(\mathcal P))
= W(\mathcal P\otimes\mathcal A).
\]

On an affine test this is Yoneda evaluated at the algebra of the pulled-back source: its value is \(\mathcal P_T\otimes\mathcal A_T\). On a general test, affine restrictions and the sheaf condition give its global sections. This proves the identity on all tests without flatness or finiteness.

### 2.5. Linear groups and universal injectivity

**Proposition 2.5. Units and automorphisms.** If \(C\) is an associative unital algebra whose underlying \(R\)-module is finite projective, its units functor \(B\mapsto(C\otimes B)^\times\) is an affine smooth group scheme of finite presentation. For every finite locally free \(\mathcal P\), the same is true of \(\mathrm{GL}(\mathcal P)\) over its base scheme.

**Proof.** The vector group \(W(C)\) represents elements of \(C\otimes B\). Locally choose a basis of \(C\) and form the polynomial \(D(a)=\det(L_a)\), where \(L_a\) is left multiplication. An invertible \(a\) makes \(L_a\) invertible. Conversely, if \(D(a)\) is a unit, put \(b=L_a^{-1}(1)\); then \(ab=1\), and injectivity of \(L_a\) applied to \(ba-1\) gives \(ba=1\). Thus the units are precisely the principal open \(D\ne0\) of this vector group. Its inverse is regular by the adjugate formula. These local opens and maps glue, and give a relative affine scheme, smooth and finitely presented because they are open subsets of finite-rank affine spaces. Apply this to \(C=\mathcal End(\mathcal P)\), using finite locally free Hom base change from Theorem 2.4. \(\square\)

**Proposition 2.6. A vector subgroup must be a subbundle.** For a map \(f:P\to Q\) of finite projective \(R\)-modules, the following are equivalent: \(W(f)\) is a monomorphism on all test algebras; \(f\) is injective with finite projective cokernel; \(f\) exhibits \(P\) as a direct summand of \(Q\). In that case \(W(f)\) is a closed immersion. Over a scheme the corresponding condition is a locally split subbundle, rather than a required global splitting.

**Proof.** A splitting remains a splitting after every tensor extension, so gives the monomorphism. Its dual map \(Q^\vee\to P^\vee\) is surjective, as is the map on symmetric algebras; hence the vector-group map is closed. Conversely test a monomorphism on every residue field. After localizing at a prime and trivializing the two finite projective modules, the matrix of \(f\) has full column rank over that residue field. A maximal column minor is consequently invertible on a neighbourhood. Elementary row operations on that neighbourhood put \(f\) in the form \(v\mapsto(v,0)\). The cokernel is therefore locally free of finite rank. Globally it is a finitely presented module with these local trivializations, hence finite projective, and the sequence splits over \(R\). This proves all assertions, including the local version on a scheme. \(\square\)

### 2.7. When automorphisms of a coherent module form a scheme

The finite locally free condition in Proposition 2.5 also has a converse over a Noetherian base. Here the functor is \(T\mapsto\operatorname{Aut}_{\mathcal O_T}(\mathcal E_T)\), including every base change. Tensoring the original endomorphism module generally gives a different functor, as the example after Theorem 2.4 already shows.

**Lemma 2.7. The minimal relation ideal.** Let \((R,\mathfrak m)\) be Noetherian local and \(M\) finite. Choose a presentation \(R^q\xrightarrow{\phi}R^p\to M\to0\) with \(p=\dim_{R/\mathfrak m}M/\mathfrak mM\). Let \(I\) be generated by all entries of \(\phi\). Then \(I\subset\mathfrak m\), and for every proper ideal \(J\), the module \(M/JM\) is free over \(R/J\) if and only if \(I\subset J\).

**Proof.** Minimality makes the relation matrix zero modulo \(\mathfrak m\). If its entries vanish modulo \(J\), the presentation makes \(M/JM=(R/J)^p\). Conversely, if that quotient is free, its rank is \(p\), by reduction to the residue field. The presenting surjection from \((R/J)^p\) onto a free module of rank \(p\) is an isomorphism: its determinant is a unit. Hence its kernel, the image of the relation matrix, is zero, so every matrix entry lies in \(J\). This also proves independence of \(I\) from the chosen minimal presentation. \(\square\)

**Lemma 2.8. An Artinian obstruction.** Let \(R\) be local Artinian, \(0\ne I\subset\mathfrak m\), and

\[
M=(R/I)^a\oplus R^b,\qquad a\ge1.
\]

The full base-change automorphism functor of \(M\) is not represented by a scheme.

**Proof.** Passing to \(R/\mathfrak mI\) preserves a hypothetical representation. Nakayama makes the image of \(I\) nonzero. Thus we can assume \(\mathfrak mI=0\), and in particular \(I^2=0\). A representing scheme \(G\) would reduce modulo \(I\) to \(\mathrm{GL}_{a+b,R/I}\). It would be affine, by the nilpotent-affineness theorem [*Infinitesimal lifting and invariance under thickenings*](../../AG-FSE/src/infinitesimal-lifting-and-invariance-under-thickenings.md), Proposition 1.2. Its coordinate algebra would be of finite type: lifts of generators of its reduction generate by the iteration \(B=B'+IB=B'+I^2B\).

Let \(P\) be the subfunctor preserving \((R/I)^a\). It is closed in \(G\). Indeed the universal composite from this summand, through the universal automorphism, to the free quotient \(R^b\) must vanish. On each affine chart, finitely many source generators and a basis of the free quotient express vanishing by coordinate equations. These ideals glue, and their vanishing has the asserted universal property. Preservation also holds for the inverse: the induced map of the finite free quotient is surjective, hence invertible, and its kernel is the preserved summand. Thus \(P\) is a represented closed subgroup.

Write \(P=\operatorname{Spec}B\). Modulo \(I\), its coordinate algebra is the usual upper block triangular group algebra

\[
\begin{aligned}
B/IB&=(R/I)[x_{ij},y_{i\beta},z_{\alpha\beta},\\
&\hspace{4em}\det(x)^{-1},\det(z)^{-1}].
\end{aligned}
\]

Choose lifts of \(x,y\) with their identity values equal to the corresponding entries of the identity matrix and zero. For \(z\), use the actual coordinate functions of the morphism \(P\to\mathrm{GL}_{b,R}\) induced on the free quotient; they already have those identity values. The determinants of these lifted matrices are units, since their reductions are units. The resulting map

\[
\begin{aligned}
C&=R[x,y,z,\det(x)^{-1},\det(z)^{-1}]\\
&\longrightarrow B
\end{aligned}
\]

is surjective by nilpotent generator lifting. Its kernel \(K\) lies in \(IC\), because the reduced map is an isomorphism.

Take a nonzero matrix \(V\in M_a(I)\). Substitution

\[
x=1+V,\qquad y=0,\qquad z=1
\]

annihilates \(K\). Indeed its value on a polynomial in \(IC\) is unchanged from the identity substitution, since all coordinate changes lie in \(I\) and \(I^2=0\); this remains true for the inverted determinants. Identity substitution kills \(K\). We therefore get a nonidentity point of \(P(R)\) reducing to the identity in \(P(R/I)\), whose induced automorphism on \(R^b\) is the identity.

But actual automorphisms of \(M\) preserving the summand are upper block triangular, with blocks

\[
\begin{aligned}
X&\in\mathrm{GL}_a(R/I),\\
Y&\in(R/I)^{ab},\qquad Z\in\mathrm{GL}_b(R).
\end{aligned}
\]

Reduction to the identity forces \(X=1\), \(Y=0\) and \(Z=1+W\) for \(W\in M_b(I)\). If the induced quotient automorphism is also the identity, then \(W=0\), and the whole automorphism is the identity. This contradicts the constructed point. It also covers \(b=0\), when the quotient condition is empty and that kernel is already trivial. \(\square\)

**Theorem 2.9. Nitsure's automorphism criterion.** Let \(S\) be a Noetherian scheme and \(\mathcal E\) coherent. Its full base-change automorphism functor is represented by an \(S\)-scheme if and only if \(\mathcal E\) is finite locally free. In that case the representation is the affine smooth finitely presented group scheme of Proposition 2.5.

**Proof.** Sufficiency is Proposition 2.5. For necessity, a failure of local freeness gives a Noetherian local ring \(R\) and finite nonfree module \(M\). A hypothetical representation remains a representation after this base change. Its minimal relation ideal \(I\) from Lemma 2.7 is nonzero. Krull intersection gives \(\bigcap_n\mathfrak m^n=0\), so an entry of the relation matrix survives modulo some \(\mathfrak m^N\). The quotient module over that local Artinian ring is still nonfree by Lemma 2.7. The exact Krull statement and proof are in [*Noetherian and Artinian rings*](../../AG-CA/src/noetherian-and-artinian-rings.md), Theorem 6.1.

In this Artinian ring, choose a minimal generating list \(a_1,\ldots,a_r\) of \(I\). If necessary quotient by \((a_1,\ldots,a_{r-1})\). The surviving last generator is nonzero by minimality, so the new relation ideal is nonzero and principal. Quotient further by \(\mathfrak mI\). Nakayama keeps it nonzero, and now \(I=(a)\) with \(\mathfrak ma=0\).

The relation matrix has the form \(a\psi\). Reduce \(\psi\) modulo \(\mathfrak m\) and put that matrix into rank normal form over the residue field. Lift the invertible row and column operations to \(R\); the lifted determinants are units. All remaining discrepancies lie in \(\mathfrak m\), so multiplying by \(a\) kills them. Thus the relation matrix becomes exactly a diagonal block of copies of \(a\) and a zero block. Its cokernel is \((R/I)^u\oplus R^v\), with \(u\ge1\) because the relation ideal is nonzero. Lemma 2.8 rules out its representation. This contradiction proves necessity. \(\square\)

**Example 2.10.** The functor on \(\mathbb Z\)-algebras given by \(B\mapsto(B/2B)^\times\) is not represented by a scheme. It is the full automorphism functor of the coherent module \(\mathbb Z/2\mathbb Z\): an endomorphism is multiplication by an element of \(B/2B\), invertible precisely when that element is a unit. The module is not locally free at the prime \(2\), so Theorem 2.9 applies. A units construction using the fixed endomorphism module cannot repair this failure.

## 3. Finite groups and their character partners

The linear dual of an arbitrary algebra need not behave well under tensor products. For a finite locally free module it does: if \(H^\vee=\operatorname{Hom}_R(H,R)\), there are canonical isomorphisms

\[
(H\otimes H)^\vee\simeq H^\vee\otimes H^\vee,
\qquad H\simeq H^{\vee\vee}.
\]

They follow from a basis when \(H\) is free, and then from localization when \(H\) is finite locally free. Both isomorphisms commute with arbitrary base change.

**Theorem 3.1. Cartier duality.** On any scheme \(S\), finite locally free commutative group schemes have a contravariant duality \(G\mapsto G^D\). The dual represents the character functor

\[
G^D(T)=\operatorname{Hom}_{T\text{-groups}}(G_T,\mathbf G_{m,T}),
\]

with pointwise multiplication of characters. There is a canonical isomorphism \(G\simeq(G^D)^D\).

**Proof.** Work first over \(R\), with \(G=\operatorname{Spec}H\). As an \(R\)-module \(H\) is finite locally free. Transfer the maps of \(H\) to \(H^\vee\) by duality. Explicitly, multiplication of \(\varphi,\psi\in H^\vee\) is convolution:

\[
(\varphi\psi)(h)=(\varphi\otimes\psi)(\Delta h).
\]

Its unit is \(\epsilon_H\). Its comultiplication is the transpose of multiplication in \(H\), its counit is evaluation at \(1_H\), and its antipode is the transpose of \(\sigma_H\). Transposing coassociativity gives associativity; transposing associativity gives coassociativity. The compatibility of multiplication and comultiplication transposes to the same compatibility with the roles interchanged. The two antipode equations transpose to the two antipode equations for the dual. Thus these maps make \(H^\vee\) a Hopf algebra. Its multiplication is commutative because the group \(G\) is commutative, that is, \(\Delta_H\) is symmetric. Its comultiplication is symmetric because \(H\) is commutative. Therefore \(\operatorname{Spec}H^\vee\) is again a finite locally free commutative group scheme.

To identify its points, let \(B\) be any \(R\)-algebra. Finite local freeness identifies a \(B\)-linear functional on \(H^\vee\otimes B\) with an element \(z\in H\otimes B\). The functional is a unital algebra map precisely when

\[
\Delta(z)=z\otimes z,\qquad\epsilon(z)=1.
\]

Indeed, its value on a product \(\varphi\psi\) is obtained by pairing \(\Delta(z)\) with \(\varphi\otimes\psi\); multiplicativity is pairing \(z\otimes z\) with the same element. Equality of all pairings implies equality because the modules are finite locally free. The unit condition is the counit equation. Such a \(z\) is invertible: applying the antipode identity gives \(z\sigma(z)=1\). It therefore defines a Hopf algebra map \(B[t,t^{-1}]\to H\otimes B\), \(t\mapsto z\), or equivalently a character \(G_B\to\mathbf G_{m,B}\). Every character arises this way. Multiplication of points of the dual is multiplication of these \(z\)'s, because the dual comultiplication is the transpose of multiplication in \(H\).

A homomorphism of the original groups dualizes by transposing its map on functions. Evaluation \(H\to H^{\vee\vee}\) preserves every structure map, so gives the double-dual isomorphism naturally. Since finite locally free duality commutes with restriction and base change, the constructions agree on overlaps of affine open subsets of \(S\) and glue. The point identification is local on \(T\) and glues as well. This proves both representability and the duality over arbitrary \(S\). \(\square\)

The hypotheses have visible roles: finite local freeness permits tensor duality and base change, and commutativity of the group ensures that the dual multiplication is commutative. Removing either hypothesis would leave the category in this theorem.

**Example 3.2. Cyclic groups.** In \(R^{\mathbf Z/n}\) let \(\delta_a\) be the component idempotents, and let \(v_a\) be their dual basis. Then

\[
v_av_b=v_{a+b},\qquad\Delta(v_a)=v_a\otimes v_a.
\]

Thus the dual algebra is \(R[\mathbf Z/n]=R[t]/(t^n-1)\). Consequently

\[
(\mathbf Z/n)_S^D=\mu_{n,S},\qquad\mu_{n,S}^D=(\mathbf Z/n)_S.
\]

The evaluation pairing is \((a,z)\mapsto z^a\). This holds when \(n\) is not invertible on \(S\): Cartier duality can interchange an étale group and a non-smooth group.

**Example 3.3. The self-duality of \(\alpha_p\).** Over any \(\mathbf F_p\)-algebra \(R\), put \(H=R[x]/(x^p)\). Let \(d_j\) be dual to \(x^j\), \(0\leq j<p\). Expanding \(\Delta(x^r)\) gives

\[
d_id_j=\begin{cases}\binom{i+j}{i}d_{i+j}&i+j<p,\\0&i+j\geq p.\end{cases}
\]

The unit is \(d_0\). For \(y=d_1\), \(y^j=j!d_j\) for \(j<p\), and \(y^p=0\). Each of these factorials is a unit in \(R\), so \(R[y]/(y^p)\to H^\vee\) is an algebra isomorphism. Transposing multiplication in \(H\) gives

\[
\Delta(y)=y\otimes1+1\otimes y,\qquad\epsilon(y)=0.
\]

Thus it is a Hopf isomorphism, proving \(\alpha_p^D\simeq\alpha_p\). Relative to the chosen coordinate, the pairing is

\[
(a,b)\longmapsto\sum_{j=0}^{p-1}\frac{(ab)^j}{j!}.
\]

The sum is invertible because it is \(1\) plus a nilpotent. Its multiplicativity in either variable also follows from the Hopf calculation; it can be checked by the binomial theorem, since terms of degree at least \(p\) in the other variable vanish.

## 4. Actions as algebra and weights

For this section we use **right actions** \(a:X\times_SG\to X\), with \((xg)h=x(gh)\) and \(xe=x\). A right action gives a left action by \(g\cdot x=x\cdot g^{-1}\). A morphism is equivariant if it commutes with the actions. Multiplication gives right translation on \(G\), while conjugation gives, for example, a left action of \(\mathrm{GL}_r\) on the space of matrices: \(g\cdot A=gAg^{-1}\). Its right-action version is \(A\cdot g=g^{-1}Ag\).

An action is **free** if

\[
X\times_SG\longrightarrow X\times_SX,\qquad(x,g)\longmapsto(x,xg)
\]

is a monomorphism. Equivalently, for every \(T\), only the identity in \(G(T)\) can fix an element of \(X(T)\). The equivalence follows by cancelling two possible transporters: if \(xg=xh\), then \(gh^{-1}\) fixes \(x\). Requiring this for all test schemes matters. A group with only one field-valued point can still have nontrivial infinitesimal stabilizers. The translation action on \(G\) is free: the displayed morphism is an isomorphism, with inverse \((x,y)\mapsto(x,x^{-1}y)\). References for schematic freeness are [Stacks, Tags 07S1 and 07S2].

If \(X=\operatorname{Spec}A\) and \(G=\operatorname{Spec}H\) over \(R\), the action amounts to an \(R\)-algebra map

\[
\rho_A:A\longrightarrow A\otimes_RH,
\qquad(\rho_A\otimes1)\rho_A=(1\otimes\Delta)\rho_A,
\quad(1\otimes\epsilon)\rho_A=1.
\]

This is the **coaction** on \(A\). The two equations are precisely the pullbacks of the action identities, so this equivalence includes morphisms, by the affine scheme–ring correspondence.

An equivariant quasi-coherent sheaf \(\mathcal F\) has an isomorphism \(a^*\mathcal F\to\operatorname{pr}_X^*\mathcal F\) that is the identity at \(e\) and is compatible with successive translations. In the affine situation, with \(M=\Gamma(X,\mathcal F)\), this is equivalently an \(R\)-linear map

\[
\rho_M:M\longrightarrow M\otimes H
\]

satisfying the same counit and coassociativity identities and

\[
\rho_M(am)=\rho_A(a)\rho_M(m).
\]

To see the equivalence explicitly, the linearization is the map

\[
(A\otimes H)\otimes_{A,\rho_A}M\longrightarrow M\otimes H,
\qquad b\otimes m\longmapsto b\rho_M(m).
\]

Compatibility with the \(A\)-action makes it well-defined. Writing \(\rho_M(m)=\sum m_0\otimes m_1\), its inverse sends

\[
m\otimes h\longmapsto\sum(1\otimes\sigma(m_1)h)\otimes m_0.
\]

The antipode equations show that both composites are the identity; the coassociativity equation gives the compatibility with two successive translations. Conversely, apply a linearization to \(1\otimes m\). Its identity and cocycle conditions give precisely the counit and coassociativity equations above. Quasi-coherent sheaves are recovered from their modules on \(X\). This proves the dictionary for equivariant sheaves without a finiteness condition on \(M\).

**Theorem 4.1. Weight decomposition.** Right actions of \(\mathbf G_m\) on \(\operatorname{Spec}A\) over \(R\) are equivalent to \(\mathbf Z\)-gradings \(A=\bigoplus_{d\in\mathbf Z}A_d\) as \(R\)-algebras. For such an action, equivariant quasi-coherent sheaves correspond to graded \(A\)-modules.

**Proof.** Expand the coaction uniquely as

\[
\rho_A(a)=\sum_d P_d(a)\otimes t^d.
\]

The sum has finite support for each \(a\). Counitality gives \(a=\sum_dP_d(a)\). Comparing coefficients of \(t^i\otimes t^j\) in coassociativity gives \(P_iP_j=0\) for \(i\ne j\) and \(P_d^2=P_d\). Thus the images \(A_d=P_d(A)\) form a direct sum decomposition. Multiplicativity gives \(A_iA_j\subset A_{i+j}\), while \(\rho_A(r)=r\otimes1\) places \(R\) in degree zero. Conversely, a grading defines \(\rho_A(a_d)=a_d\otimes t^d\); the algebra and coaction equations hold on homogeneous elements, hence on their finite sums.

Apply the same coefficient projections to \(\rho_M\). They give \(M=\bigoplus M_d\), and the compatibility equation gives \(A_iM_j\subset M_{i+j}\). A graded module defines the coaction in the reverse direction, and the preceding sheaf dictionary gives its linearization. A morphism commutes with the coactions exactly when it preserves each degree. Thus these are equivalences of categories, including the modules, rather than only correspondences of objects. \(\square\)

The same proof works with any abelian group \(L\) in place of \(\mathbf Z\). Define \(R[L]\) with basis \(z^\ell\), multiplication \(z^\ell z^{\ell'}=z^{\ell+\ell'}\) and comultiplication \(z^\ell\mapsto z^\ell\otimes z^\ell\). The group \(D_R(L)=\operatorname{Spec}R[L]\) acts on an affine scheme exactly when its ring is \(L\)-graded. Equivariant modules are \(L\)-graded modules. No finite generation of \(L\) is needed for this assertion. We will develop diagonalizable groups further in *Diagonalizable groups and groups of multiplicative type*.

**Example 4.2. A grading with a nonconstant invariant.** On \(R[x,y]\) give \(x\) degree \(2\) and \(y\) degree \(-3\). The action is

\[
(x,y)\cdot t=(t^2x,t^{-3}y).
\]

Invariant elements have degree zero. A monomial \(x^ay^b\) has degree \(2a-3b\), which is zero precisely when \(a=3q,b=2q\) for \(q\geq0\). Hence the invariant ring is \(R[x^3y^2]\). This calculation uses independence of Laurent monomials over \(R\), so it remains valid in positive characteristic.

### 4.3. Linearization on an arbitrary scheme

We use left actions in this subsection. A right action from the beginning of Section 4 becomes a left action by inversion. For a left action \(a:G\times_SX\to X\), write \(p:G\times_SX\to X\) for the projection. A **linearization** of an \(\mathcal O_X\)-module \(\mathcal F\) is an isomorphism

\[
\theta:p^*\mathcal F\longrightarrow a^*\mathcal F
\]

whose fibre maps \(\theta_{g,x}:\mathcal F_x\to\mathcal F_{gx}\), interpreted by pullback to every test scheme, satisfy

\[
\theta_{g,hx}\theta_{h,x}=\theta_{gh,x}.
\]

This is an equality of pulled-back sheaf maps on \(G\times_SG\times_SX\). Since \(\theta\) is invertible, putting \(h=1\) also forces the identity condition.

**Proposition 4.3. Equivariant sheaf operations.** A linearization is equivalent to functorial linear transport between \(\mathcal F_x\) and \(\mathcal F_{gx}\) for all test schemes, respecting multiplication in \(G\). Equivariant pullback and tensor product preserve linearizations. A linearization on a quasi-coherent \(\mathcal F\) induces a linear action on \(V(\mathcal F)\) over \(X\), by the inverse transpose. None of these assertions requires \(G\) to be flat.

**Proof.** Pulling \(\theta\) back along \((g,x):T\to G\times_SX\) gives the transports. Conversely the transport for the universal pair on \(G\times_SX\) is \(\theta\); naturality gives all its other pullbacks. The action law is exactly the displayed cocycle equality. For an equivariant map \(u:Y\to X\), pull back \(\theta\) along \(1\times u\); equivariance identifies its source and target with those needed for \(u^*\mathcal F\), and pulls back its cocycle as well. Tensor the two isomorphisms to linearize a tensor product; its cocycle holds on elementary tensors. Dualizing an isomorphism reverses its direction, so the map \(V(\mathcal F_x)\to V(\mathcal F_{gx})\) is induced by \(\theta_{g,x}^{-1}\). The universal property of \(\operatorname{Sym}\mathcal F\) represents these maps, and inverse transpose respects the action law. In particular the action on covectors is contragredient. \(\square\)

If \(r:X\to S\) and \(T\to S\), the section functor

\[
\mathcal S_{\mathcal F}(T)=\Gamma(X_T,\mathcal F_T)
\]

always has a \(G(T)\)-action. Its formula is

\[
(g\cdot s)(x)=\theta_{g,g^{-1}x}\bigl(s(g^{-1}x)\bigr).
\]

This notation denotes pullback of a section followed by the sheaf isomorphism, so defines a section even when \(\mathcal F\) is not a vector bundle. Applying the cocycle twice proves \(g\cdot(h\cdot s)=(gh)\cdot s\). For \(b\in\Gamma(X_T,\mathcal O_{X_T})\), it also proves

\[
g\cdot(bs)=((g^{-1})^*b)(g\cdot s).
\]

Thus this action is semilinear over functions on \(X_T\), and linear over functions on \(T\). No assertion that the section functor is represented, or equals a base change of global sections, is needed here.

### 4.4. Flat base change and equivariant direct image

**Lemma 4.4. Direct image and its section functor.** Let \(u:X\to Y\) be quasi-compact and quasi-separated, and \(\mathcal F\) quasi-coherent. Then \(u_*\mathcal F\) is quasi-coherent and commutes with flat base change on \(Y\). If \(G\) is flat over \(S\), \(u\) is an equivariant morphism of \(G\)-schemes and \(\mathcal F\) is linearized, then \(u_*\mathcal F\) has a canonical linearization. When \(Y=S\),

\[
W(u_*\mathcal F)\longrightarrow\mathcal S_{\mathcal F}
\]

is equivariant and is an isomorphism on all flat \(S\)-schemes.

**Proof.** Work over an affine open \(\operatorname{Spec}R\subset Y\). Choose finitely many affine opens \(U_i\) covering its inverse image, and finitely many affine opens \(V_{ijk}\) covering each \(U_i\cap U_j\). These finite choices are possible by quasi-compactness and quasi-separatedness. The sheaf condition gives the equalizer

\[
0\longrightarrow\Gamma(X,\mathcal F)
\longrightarrow C_0\longrightarrow C_1,
\]

where \(C_0=\prod_i\Gamma(U_i,\mathcal F)\), \(C_1=\prod_{i,j,k}\Gamma(V_{ijk},\mathcal F)\), and the last arrow subtracts the two restrictions. Tensoring with a flat \(R\)-algebra \(B\) preserves this kernel and the finite products. On every affine chart quasi-coherent sections after this base change are the corresponding tensor extension. The equalizer therefore identifies \(\Gamma(X,\mathcal F)\otimes_RB\) with \(\Gamma(X_B,\mathcal F_B)\). In particular this holds for every localization \(B=R_f\), proving quasi-coherence of \(u_*\mathcal F\). Affine charts on a general flat \(Y'\to Y\) prove the sheaf base-change assertion.

Let \(a_X,a_Y\) be the actions and \(q=1_G\times u\). Both squares with horizontal maps the projections, or horizontal maps \(a_X,a_Y\), are cartesian. For the second square, its inverse identification sends a pair \(((g,y),x)\) with \(u(x)=gy\) to \((g,g^{-1}x)\). The projection \(G\times Y\to Y\) is flat. The action \(a_Y\) is flat too, since it is that projection composed with the isomorphism \((g,y)\mapsto(g,gy)\). Flat base change thus identifies \(q_*p_X^*\mathcal F\) and \(q_*a_X^*\mathcal F\) with \(p_Y^*u_*\mathcal F\) and \(a_Y^*u_*\mathcal F\). Applying \(q_*\) to \(\theta\) gives the required isomorphism. The same cartesian argument on \(G\times G\times Y\) carries its cocycle to the cocycle for the direct image. For \(Y=S\), the natural base-change map on every \(T\) gives the asserted map of section functors; its compatibility with transports proves equivariance, and the proved flat base-change assertion gives the isomorphism on flat tests. \(\square\)

### 4.5. Translation trivializes equivariant sheaves

**Theorem 4.5. Translation equivalence.** Let \(\pi:G\to S\) be any group scheme, with identity \(e\). Pullback \(\mathcal E\mapsto\pi^*\mathcal E\) and identity restriction \(\mathcal F\mapsto e^*\mathcal F\) give inverse equivalences between quasi-coherent modules on \(S\) and left-translation-equivariant quasi-coherent modules on \(G\). For the action

\[
(a,b)\cdot g=agb^{-1}
\]

of \(G\times_SG\), identity restriction instead gives an equivalence with representations of \(G\) on quasi-coherent \(\mathcal O_S\)-modules. No flatness or finiteness hypothesis on \(G\) is needed.

**Proof.** The two pullbacks of \(\pi^*\mathcal E\) along multiplication and the second projection agree, giving its translation linearization. The identity restriction is \(\mathcal E\). Conversely, pull the linearization of \(\mathcal F\) back along \(g\mapsto(g,e)\). It gives an isomorphism

\[
\pi^*e^*\mathcal F\longrightarrow\mathcal F.
\]

Its compatibility with left translations is precisely the original cocycle applied to \((a,g,e)\). A morphism of linearized sheaves restricts at the identity, and this trivialization reconstructs it from that restriction. This proves both essential surjectivity and full faithfulness. Under this trivialization, universally translation-invariant sections of \(\pi^*\mathcal E\) are exactly pullbacks of sections of \(\mathcal E\). Indeed restrict an invariant section at \(e\), and its invariance at the universal pair \((g,e)\) reconstructs the section everywhere from that value. Thus evaluation at \(e\) also identifies their invariant global sections with \(\Gamma(S,\mathcal E)\), without a flatness assumption.

For the second action, the stabilizer of \(e\) is the diagonal copy of \(G\). Thus \(\mathcal E=e^*\mathcal F\) has a representation of that copy. Conversely, for a representation \(\rho\) on \(\mathcal E\), linearize \(\pi^*\mathcal E\) by

\[
(g,v)\longmapsto(agb^{-1},\rho(b)v).
\]

Here the notation means the isomorphism between the pulled-back modules, not a representability assertion for \(W(\mathcal E)\). The product rule for \(\rho\) verifies the action law. In the left-translation trivialization of any given \(\mathcal F\), a transport by \((a,b)\) has this form: its remaining factor on the identity fibre is \((agb^{-1})^{-1}ag=b\), hence the diagonal transport \(\rho(b)\). This proves that the constructions are inverse also for the second action. \(\square\)

**Corollary 4.6. Conormal and stabilizer representations.** Suppose \(Y\hookrightarrow X\) is an immersed subgroup of an \(S\)-group scheme and \(Y\) is flat over \(S\). Its conormal sheaf is \((Y\times_SY)\)-equivariant, and hence is the pullback of its identity fibre with the representation of the diagonal \(Y\). More generally, for a \(G\)-equivariant quasi-coherent sheaf on a \(G\)-scheme \(Z\), its restriction along \(\tau:S\to Z\) is a representation of the stabilizer of \(\tau\), without requiring that stabilizer to be flat. If \(Z\) is separated, that stabilizer is closed in \(G\).

**Proof.** For the conormal assertion the two maps \(Y\times Y\times X\to X\), projection and \((a,b,x)\mapsto axb^{-1}\), are flat: \(Y\times Y\to S\) is flat and the latter map differs from projection by an automorphism of this product. Their inverse images of \(Y\) are both \(Y\times Y\times Y\). Flat pullback of an immersion's ideal sequence identifies its conormal with the conormal of its pullback: tensor the ideal sequence using flatness, and then quotient by the square of the pulled-back ideal. The action therefore gives an isomorphism between the two pullbacks of the conormal, and composition of translations proves its cocycle. Apply Theorem 4.5. For a stabilizer, pull the linearization back along \((h,\tau)\), where \(h\tau=\tau\); it is an automorphism of \(\tau^*\mathcal F\), and the cocycle is the representation law. Finally the stabilizer is the equalizer of \(g\mapsto g\tau\) and the constant section \(\tau\); it is the inverse image of the closed diagonal of \(Z/S\). \(\square\)

For an arbitrary morphism \(\varphi:Y\to Z\) between \(G\)-schemes, its universal stabilizer consists of the \(g\) for which \(g\varphi g^{-1}=\varphi\) after every further test-scheme pullback. Restricting a linearization gives an equivariant structure on \(\varphi^*\mathcal F\) under this stabilizer functor, and Section 4.3 gives an action on its full section functor. If \(Z/S\) is separated and \(Y/S\) is essentially free, the universal equality-locus proof in *Diagonalizable groups*, Proposition 4.10, represents the stabilizer by a closed subgroup of \(G\): apply that proposition to the two maps \(G\times_SY\to Z\). To apply Lemma 4.4 to its direct image one must additionally know that this acting stabilizer is flat. Flatness of the ambient \(G\) alone does not supply that hypothesis.

## 5. Why affine groups over a field are matrix groups

Let \(G=\operatorname{Spec}H\) over \(R\). A **representation** on an \(R\)-module \(V\) means a natural homomorphism \(G(B)\to\operatorname{Aut}_B(V\otimes_RB)\). It is equivalent to a right \(H\)-comodule \(\lambda:V\to V\otimes H\). In one direction evaluate the second factor at \(g:H\to B\); in the other use the universal point \(1_H:H\to H\) and restrict its \(H\)-linear action to \(V\otimes1\). The group identity and product law give the counit and coassociativity equations. The antipode supplies the inverse. This argument also applies when \(V\) is not finite locally free.

For free \(V\) of rank \(r\), write \(\lambda(v_j)=\sum_i v_i\otimes a_{ij}\). The comodule equations say

\[
\Delta(a_{ij})=\sum_\ell a_{i\ell}\otimes a_{\ell j},
\qquad \epsilon(a_{ij})=\delta_{ij}.
\]

The matrix \((\sigma(a_{ij}))\) is inverse to \((a_{ij})\), by the antipode identities. Thus these are exactly the equations for a morphism \(G\to\mathrm{GL}_r\).

**Lemma 5.1. Local finiteness.** If \(R=k\) is a field, every \(H\)-comodule is a filtered union of finite-dimensional subcomodules.

**Proof.** For \(v\in V\), write

\[
\lambda(v)=\sum_{j=1}^s v_j\otimes h_j
\]

with \(h_j\) linearly independent; combine dependent terms if necessary. Let \(W\) be the span of the \(v_j\). Counitality puts \(v\) in \(W\). Coassociativity says

\[
\sum_j\lambda(v_j)\otimes h_j=\sum_jv_j\otimes\Delta(h_j).
\]

Project the first factor to \(V/W\). The right-hand side becomes zero. Independence of the \(h_j\), or linear functionals selecting them, forces every image of \(\lambda(v_j)\) in \((V/W)\otimes H\) to vanish. Tensoring over a field is exact, so \(\lambda(v_j)\in W\otimes H\). Thus \(W\) is a finite-dimensional subcomodule containing \(v\). Finite sums of these subcomodules are again finite-dimensional subcomodules, so every finite subset is contained in one and the union is filtered. \(\square\)

This conclusion concerns representations of the group *scheme*. Stability under \(G(k)\) alone does not imply stability under all \(G(B)\).

**Theorem 5.2. Linearity.** Every affine group scheme of finite type over a field \(k\) is isomorphic to a closed subgroup scheme of some \(\mathrm{GL}_r\), including nonreduced group schemes.

**Proof.** The comultiplication makes \(H\) its own right comodule. Choose finitely many algebra generators \(b_1,\ldots,b_q\). By Lemma 5.1 their span is contained in a finite-dimensional subcomodule \(W\subset H\); include \(1\) if needed. Choose a basis \(w_1,\ldots,w_r\) and write

\[
\Delta(w_j)=\sum_i w_i\otimes a_{ij}.
\]

The preceding matrix equations give a Hopf map

\[
k[\mathrm{GL}_r]\longrightarrow H,\qquad x_{ij}\longmapsto a_{ij}.
\]

Apply \(\epsilon\otimes1\) to the displayed equation to obtain

\[
w_j=\sum_i\epsilon(w_i)a_{ij}.
\]

Therefore every \(w_j\), and hence every \(b_a\), belongs to the image of this algebra map. Since the \(b_a\) generate \(H\), the map is surjective. Taking spectra gives a closed immersion, and the Hopf identities ensure it is a homomorphism. \(\square\)

Finite type was used to choose finitely many algebra generators. The field hypothesis was used for Lemma 5.1. The theorem as proved does not assert linearity over an arbitrary base ring.

**Example 5.3. A concrete regular subrepresentation.** For \(H=k[x]\) with its additive Hopf structure, \(W=\langle1,x\rangle\) is stable. In that basis the coefficient matrix is

\[
\begin{pmatrix}1&x\\0&1\end{pmatrix}.
\]

It gives the familiar closed immersion of \(\mathbf G_a\) into \(\mathrm{GL}_2\). Restricting \(H\) to \(k[x]/(x^p)\) gives the same embedding of \(\alpha_p\), now with the extra equation that the upper-right entry has \(p\)-th power zero.

### 5.4. Modules over a ring: flatness and tensor operations

**Proposition 5.4. The category of representations.** Let \(G=\operatorname{Spec}H\) over \(R\). Representations on arbitrary \(R\)-modules are right \(H\)-comodules, and their morphisms are module maps commuting with the coactions. Cokernels always have their quotient coaction. If \(H\) is flat over \(R\), kernels and images have their induced coactions, and this is an abelian category with an exact faithful forgetful functor to \(R\)-modules. Tensor products of representations exist without the flatness assumption, as do contragredient representations on duals of finite projective modules.

**Proof.** The universal-point argument at the beginning of Section 5 gives the representation–comodule equivalence on objects. Applying it to an intertwiner gives the equation \(\lambda_N f=(f\otimes1)\lambda_M\), which is also sufficient on every test algebra. Right exactness of tensor product makes the quotient coaction on \(\operatorname{coker}f\) well-defined, and its identities follow by passage to the quotient.

When \(H\) is flat, tensoring the module kernel sequence identifies \((\ker f)\otimes H\) with the kernel of \(f\otimes1\). The intertwining equation then factors the coaction of \(M\) through this kernel. To check the comodule identities there, use injectivity into \(M\otimes H\), and into \(M\otimes H\otimes H\); flatness of \(H\) and its tensor square gives both injections. Thus \(\ker f\) is a comodule. Its image is the quotient by this kernel and embeds as the module image in \(N\), with the same coaction. Consequently coimage and image coincide, proving abelianness and exactness of the forgetful functor. This proof identifies where flatness is used; the dictionary itself does not use it.

In notation \(\lambda(m)=\sum m_0\otimes m_1\), the tensor coaction is

\[
\lambda(m\otimes n)=\sum(m_0\otimes n_0)\otimes m_1n_1.
\]

The two counit identities prove its counit identity, and multiplying the two coassociativity identities proves its coassociativity. For a finite projective module \(P\), define the dual action by \((g\phi)(v)=\phi(g^{-1}v)\). Finite projective Hom base change identifies these with automorphisms of \(P^\vee\otimes B\) for every \(B\), so this formula is a natural representation. Evaluation and coevaluation are equivariant: evaluating \(g\phi\) on \(gv\) cancels \(g^{-1}g\), and the identity endomorphism represented by coevaluation is fixed under conjugation. Hence \(\operatorname{Hom}(P,Q)=P^\vee\otimes Q\) has the conjugation action, and its invariant elements are precisely the equivariant maps. \(\square\)

The regular representation on \(H\), with coaction \(\Delta\), is faithful over every \(R\). Indeed a test point \(g\in G(B)\) acts on \(H\otimes B\) by pullback under right translation. If this pullback fixes every function, evaluating those equalities at the identity gives \(f(g)=f(e)\) for every coordinate function \(f\). The two algebra maps to \(B\) are therefore equal, so \(g=e\). This proves faithfulness on all tests.

**Proposition 5.5. Invariants and base change.** For any comodule \(M\), universal invariant elements are

\[
M^G=\ker\bigl(\lambda_M-(m\mapsto m\otimes1)\bigr).
\]

They commute with flat base change. They can fail to commute with nonflat base change, even when \(G\) is finite étale and \(M\) is free of rank one.

**Proof.** An element fixed by every \(G(B)\) is fixed by the universal point in \(G(H)\), which gives the displayed kernel. Conversely that equation, evaluated at any \(H\to B\), says it is fixed on every test. Flat tensor extension preserves this kernel, giving the flat base-change assertion without any flatness condition on \(H\). For the failure, take \(R=\mathbf Z\), the constant group \(G=(\mathbf Z/2)_R\), and \(M=\mathbf Z\) with its sign representation. Its invariants are the elements satisfying \(m=-m\), hence zero. After base change to \(\mathbf F_2\) the action is trivial, and its invariants are all of \(\mathbf F_2\). Thus the natural map from the base change of the invariant module is not surjective. Equivalently the fixed section functor \(W(M)^G\) is not \(W(M^G)\) in this example. \(\square\)

### 5.6. Coinduction and untwisting

**Proposition 5.6. Coinduced representations.** For every \(R\)-module \(N\), put \(\operatorname{Ind}(N)=N\otimes_RH\), with coaction \(1_N\otimes\Delta\). It is right adjoint to forgetting the representation:

\[
\operatorname{Hom}_G(M,\operatorname{Ind}(N))
\simeq\operatorname{Hom}_R(M,N).
\]

Its invariants are canonically \(N\). For a comodule \(M\), the coaction is a split module injection \(M\to\operatorname{Ind}(M)\) and is equivariant. The diagonal tensor representation on \(M\otimes H\) is equivariantly isomorphic to \(\operatorname{Ind}(M)\) by

\[
\begin{aligned}
U(m\otimes h)&=\sum m_0\otimes m_1h,\\
U^{-1}(m\otimes h)&=\sum m_0\otimes\sigma(m_1)h.
\end{aligned}
\]

All these assertions hold without flatness or finite generation.

**Proof.** The adjunction sends \(f:M\to N\) to \((f\otimes1)\lambda_M\), and sends an equivariant \(b:M\to N\otimes H\) to \((1\otimes\epsilon)b\). Counitality proves one composite is the identity. For the other, the intertwining equation

\[
(b\otimes1)\lambda_M=(1\otimes\Delta)b
\]

followed by \(1\otimes\epsilon\otimes1\) proves that reconstructing \(b\) gives \(b\) itself. If \(z\in N\otimes H\) is invariant, its equality \((1\otimes\Delta)z=z\otimes1\), followed by the same counit map, says \(z=((1\otimes\epsilon)z)\otimes1\). This proves the invariants assertion. Coassociativity makes \(\lambda_M\) an intertwiner into \(\operatorname{Ind}(M)\); counitality splits it as a module map.

The antipode equations and coassociativity show that the two displayed formulas for \(U\) are inverse. For equivariance, view \(M\otimes H\) as regular \(M\)-valued functions \(F\) on \(G\), meaning the corresponding module-functor maps on all tests. Its diagonal action is \((gF)(x)=g\cdot F(xg)\); the coinduced action is \((gF)(x)=F(xg)\). The formula for \(U\) is \((UF)(x)=x\cdot F(x)\), and

\[
U(gF)(x)=(xg)\cdot F(xg)=(g(UF))(x).
\]

This calculation is natural on every test algebra and so proves equivariance. Its inverse uses \(x^{-1}\) and is the antipode formula above. No identification of an unrestricted Hom functor with \(W(\operatorname{End}_R M)\) is involved. \(\square\)

### 5.7. Regular cochains compute derived invariants

For a representation \(M\), a **regular \(n\)-cochain** is a natural module-valued map \(G^n\to W(M)\), equivalently an element of

\[
C^n(G,M)=M\otimes_RH^{\otimes n}.
\]

The equivalence follows by evaluation at the universal point of the affine scheme \(G^n\). For \(\mathbf g=(g_1,\ldots,g_{n+1})\), let \(\partial_i\mathbf g\) denote the tuple obtained by replacing the adjacent entries \(g_i,g_{i+1}\) by their product, for \(1\le i\le n\). On every test algebra define faces by

\[
\begin{aligned}
d_0f(\mathbf g)&=g_1f(g_2,\ldots,g_{n+1}),\\
d_if(\mathbf g)&=f(\partial_i\mathbf g)\quad(1\le i\le n),\\
d_{n+1}f(\mathbf g)&=f(g_1,\ldots,g_n).
\end{aligned}
\]

Put \(d=\sum_i(-1)^id_i\). Associativity and the representation law give \(d_jd_i=d_id_{j-1}\) for \(i<j\), so the terms of \(d^2\) cancel in pairs. Write \(H^n_{\mathrm{reg}}(G,M)\) for this complex's cohomology. Its degree-zero group is \(M^G\).

**Theorem 5.7. Derived-invariants interpretation.** If \(H\) is flat over \(R\), the comodule category has enough injectives, and \(H^n_{\mathrm{reg}}(G,-)\) is the \(n\)-th right derived functor of invariants. Coinduced modules have zero regular cohomology in all positive degrees. Their acyclicity already holds without flatness.

**Proof.** First contract the cochain complex for \(\operatorname{Ind}(N)\). Its values are regular functions of both the cochain variables and a final variable \(x\in G\), with values in \(W(N)\). Define

\[
(sf)(g_1,\ldots,g_n)(x)
=f(x,g_1,\ldots,g_n)(1).
\]

This is regular: it permutes the corresponding tensor factors and applies the counit to the factor for the final variable. In \(dsf+sdf\), the leading terms involving \(xg_1\) cancel; each middle product face cancels the same face with opposite sign; and the two last faces cancel. The single remaining leading term is

\[
(xf(g_1,\ldots,g_{n+1}))(1)
=f(g_1,\ldots,g_{n+1})(x),
\]

because coinduction uses right translation. Hence \(ds+sd=1\) in positive degrees. In degree zero the same calculation gives \(sdF(x)=F(x)-F(1)\). This proves acyclicity and also recovers the invariants \(N\), without flatness.

Now assume \(H\) flat. The functors \(C^n(G,-)\) are exact, by flatness of \(H^{\otimes n}\), so short exact comodule sequences give the usual long exact cohomology sequence. An injective \(R\)-module \(I\) gives an injective comodule \(\operatorname{Ind}(I)\), because Proposition 5.6 identifies its Hom functor with \(\operatorname{Hom}_R(-,I)\) after the exact forgetful functor. Given an embedding \(M\hookrightarrow I\) of underlying modules, the composite

\[
M\xrightarrow{\lambda_M}\operatorname{Ind}(M)
\longrightarrow\operatorname{Ind}(I)
\]

is an embedding of comodules: the first map is module-split and the second is injective by flatness. Thus there are enough injectives.

For completeness, underlying module embeddings into injectives can be obtained explicitly. The abelian group \(\mathbf Q/\mathbf Z\) is injective: extend a homomorphism one additional cyclic generator at a time by divisibility, and use a maximal extension. It detects every nonzero element by a character on its cyclic subgroup, extended in this way. The module \(I_0=\operatorname{Hom}_{\mathbf Z}(R,\mathbf Q/\mathbf Z)\), with \((a\phi)(r)=\phi(ar)\), is injective by the adjunction

\[
\operatorname{Hom}_R(L,I_0)
=\operatorname{Hom}_{\mathbf Z}(L,\mathbf Q/\mathbf Z).
\]

The characters \(\chi\) of an underlying module give module maps \(m\mapsto(r\mapsto\chi(rm))\) to \(I_0\) which jointly detect its elements. The map to the product of these copies of \(I_0\) is therefore an embedding; that product is injective because extensions can be made in each coordinate.

An injective comodule \(J\) is an equivariant direct summand of \(\operatorname{Ind}(J)\): its coaction embedding splits by injectivity. Thus the contraction above proves \(H^n_{\mathrm{reg}}(G,J)=0\) for \(n>0\). For \(0\to M\to J\to Q\to0\), its long exact sequence consequently identifies \(H^1_{\mathrm{reg}}(G,M)\) with the cokernel of \(J^G\to Q^G\), and identifies higher groups with those for \(Q\) one degree lower. The identical recursion computes the cohomology of an injective resolution defining derived invariants. Iterating it, with the same connecting maps, proves the asserted natural identification in every degree. \(\square\)

More generally, suppose every short exact comodule sequence which is split on underlying modules also has an equivariant splitting. Apply this to the module-split coaction inclusion \(M\to\operatorname{Ind}(M)\) and its quotient. It makes \(M\) an equivariant direct summand of the coinduced module. The contraction then forces all its positive regular cohomology groups to vanish. This particular argument even works for nonflat \(G\): the specified coaction inclusion is split, its quotient coaction exists by Proposition 5.4, and cochains preserve the resulting equivariant direct sum.

For a finite constant group scheme \(\Gamma_R\), the algebra \(H=R^\Gamma\) gives \(C^n(G,M)=\operatorname{Map}(\Gamma^n,M)\) with the usual group-cohomology differential. Its regular cohomology is therefore ordinary group cohomology. Evaluation on \(G(R)\) for a general group scheme has no comparable detection assertion.

### 5.8. Splittings and kernels read from weights

**Proposition 5.8. Diagonalizable representations.** For any abelian group \(L\) and any ring \(R\), taking a weight component is exact on representations of \(D_R(L)\), and commutes with arbitrary base change. An exact sequence of such representations splits equivariantly if and only if its underlying module sequence splits. Their positive regular cohomology groups vanish. If

\[
P=\bigoplus_{\ell\in F}R^{r_\ell},\qquad r_\ell>0,
\]

has the indicated finite set of weights, and \(L_0\) is the subgroup generated by \(F\), its representation has kernel \(D_R(L/L_0)\) and factors through a closed immersion \(D_R(L_0)\hookrightarrow\mathrm{GL}(P)\).

**Proof.** The coefficient-projector proof of Theorem 4.1 works for modules with the same arbitrary \(L\). Every equivariant map preserves weights. A surjection is surjective on each weight component: lift an element and take that component of its lift. Kernels are computed weight by weight as well. Tensor extension preserves a direct-sum decomposition and its coefficient projectors, proving the base-change assertion. If \(s\) is an underlying module section and \(P_\ell\) is the projector in the middle module, then

\[
s_0(v)=\sum_\ell P_\ell s(v_\ell)
\]

is an equivariant section. The sum is finite for every \(v\). Conversely an equivariant section is a module section. Invariants are the weight-zero component, so their functor is exact. The algebra \(R[L]\) is free over \(R\); Theorem 5.7 consequently gives the positive-degree vanishing.

For the kernel assertion, the coordinate map of the representation sends the diagonal entries in a block of weight \(\ell\) to \(z^\ell\); entries of the inverse matrix map to \(z^{-\ell}\). Its image is therefore exactly \(R[L_0]\). These coefficients generate that algebra, so the factored morphism into \(\mathrm{GL}(P)\) is closed. The quotient \(D_R(L)\to D_R(L_0)\) has kernel defined by \(z^\ell=1\) for \(\ell\in L_0\), namely \(\operatorname{Spec}R[L/L_0]\). \(\square\)

### 5.9. Cocycles, sections and extensions

**Proposition 5.9. First and second cohomology.** Let \(G=\operatorname{Spec}H\) and let \(M\) be a representation. A regular one-cocycle \(z:G\to W(M)\) is equivalent to a homomorphic section of the semidirect group functor \(W(M)\rtimes G\). Its classes in \(H^1_{\mathrm{reg}}(G,M)\) are the \(M\)-conjugacy classes of these sections. Classes in \(H^2_{\mathrm{reg}}(G,M)\) classify extensions

\[
1\longrightarrow W(M)\longrightarrow E\longrightarrow G\longrightarrow1
\]

of group functors, surjective on every test algebra, inducing the specified linear conjugation action on \(M\). The group law on classes is Baer sum. These assertions about regular cochains require no flatness; when \(G\) is flat, Theorem 5.7 also identifies them with derived invariants.

**Proof.** A section is \(g\mapsto(z(g),g)\). The semidirect law

\[
(m,g)(n,h)=(m+gn,gh)
\]

makes it a homomorphism exactly when \(z(gh)=z(g)+gz(h)\). Conjugating by \((b,1)\), for \(b\in M\), changes \(z(g)\) to \(z(g)+b-gb\), which changes it by a coboundary. This proves the first classification, including its quotient by conjugacy.

A regular two-cocycle satisfies

\[
g c(h,k)-c(gh,k)+c(g,hk)-c(g,h)=0.
\]

It can always be normalized to \(c(1,g)=c(g,1)=0\). Indeed the cocycle identity gives \(c(1,g)=a=c(1,1)\) and \(c(g,1)=ga\); subtracting the coboundary of the constant one-cochain \(a\) removes both values. For a normalized cocycle put

\[
(m,g)(n,h)=(m+gn+c(g,h),gh)
\]

on \(W(M)\times G\). Associating a triple in the two orders shows that associativity is exactly the cocycle equation. Normalization gives identity \((0,1)\). An inverse is

\[
\bigl(-g^{-1}(m+c(g,g^{-1})),g^{-1}\bigr);
\]

the equality \(c(g^{-1},g)=g^{-1}c(g,g^{-1})\) proves the other inverse law. Thus this constructs an extension naturally on all tests.

Conversely, surjectivity at the universal point in \(G(H)\) supplies a lift in \(E(H)\). Yoneda makes that lift a natural section \(s:G\to E\), which can be normalized at \(1\) by multiplying by its constant kernel value. Write

\[
s(g)s(h)=c(g,h)s(gh).
\]

Associativity and the given conjugation action give the two-cocycle identity. Every element over \(g\) is uniquely \(m s(g)\), so these coordinates identify the extension with the one just constructed. Replacing \(s(g)\) by \(b(g)s(g)\) changes \(c\) to

\[
c(g,h)+b(g)+gb(h)-b(gh).
\]

An isomorphism of extensions fixing kernel and quotient changes the coordinate section in exactly this manner. Hence the resulting classification is precisely cohomology modulo coboundaries. The fibre product of two such extensions has kernel \(W(M\oplus M)\) and cocycle \((c,c')\); adding its two kernel coordinates gives cocycle \(c+c'\). This is Baer sum and proves compatibility with the cohomology group law. \(\square\)

For finite projective \(M\), the same classification applies to fppf group-scheme extensions whose map to \(G\) is a \(W(M)\)-torsor and whose conjugation action is the prescribed linear action. Such a torsor over the affine scheme \(G\) has a global section: its differences on an affine faithfully flat cover are a quasi-coherent additive one-cocycle, killed by the positive-degree Amitsur contraction proved in *Quotients and torsors*, Section 1. Translation by that section trivializes the torsor on every test algebra, reducing it to Proposition 5.9. In particular an extension of an arbitrary diagonalizable \(D_R(L)\) by a representation's section functor splits, and all its homomorphic sections are \(M\)-conjugate, by Proposition 5.8. A section of a non-split torsor must not be assumed merely from surjectivity in the fppf topology.

### 5.10. Linear reductivity and all representations

An affine group scheme over a field is **linearly reductive** if every finite-dimensional representation is a direct sum of simple representations. A simple representation is nonzero and has no proper nonzero subrepresentation.

**Theorem 5.10. Linear reductivity.** For an affine group scheme over any field \(k\), the following conditions are equivalent: every finite-dimensional representation is semisimple; every representation is semisimple; invariants are an exact functor. These conditions are preserved and detected by every field extension. When they hold, all positive regular cohomology groups vanish, and the extensions and sections in Proposition 5.9 split and are conjugate, respectively.

**Proof.** Every simple representation is finite-dimensional, by Lemma 5.1 applied to a nonzero element. If every finite-dimensional representation is semisimple, Lemma 5.1 says every representation is the sum of its simple subrepresentations. Choose a maximal family of simple subrepresentations whose sum is direct, using the union of a chain to obtain an upper bound. If its sum were proper, some simple subrepresentation in the full sum would not be contained in it. The intersection with that simple subrepresentation is then zero, contradicting maximality. This proves semisimplicity for arbitrary representations.

Every surjection onto a simple representation splits: choose lifts of a finite basis inside its inverse image, and use Lemma 5.1 there to put those lifts in a finite-dimensional subrepresentation. This subrepresentation maps onto the simple one, and semisimplicity in finite dimension gives a section. For a quotient which is a direct sum of simples, combine their sections. Thus every short exact sequence of representations splits, proving exactness of invariants.

Conversely, let \(V\) be finite-dimensional and \(U\subset V\) a subrepresentation. The quotient \(Q=V/U\) is finite-dimensional. The surjection \(\operatorname{Hom}_k(Q,V)\to\operatorname{Hom}_k(Q,Q)\) is equivariant for the conjugation representations of Proposition 5.4. Exactness of invariants lifts the invariant identity of \(Q\) to an equivariant section \(Q\to V\). Induction on dimension now decomposes \(V\) into simples. This proves the equivalences.

Let \(K/k\) be a field extension. A representation of \(G_K\), even of infinite dimension over \(K\), can be regarded as a representation of \(G\) on its underlying \(k\)-vector space: the canonical identification

\[
V\otimes_K(K\otimes_kH)=V\otimes_kH
\]

carries its coaction and its identities to the original Hopf algebra. The invariant subsets are the same. Consequently exactness of invariants for \(G\) implies it for \(G_K\). In the reverse direction, for every exact sequence of \(G\)-representations, extend scalars to \(K\). Proposition 5.5 identifies the extended invariant modules with the new invariants. Their exactness over \(K\), together with faithful flatness of \(K/k\), proves exactness over \(k\). This proves preservation and detection, including for an algebraic closure.

A field makes \(H\) flat, so Theorem 5.7 identifies regular cohomology with derived invariants. Exactness gives vanishing in positive degrees. The conclusions about extensions and conjugacy are then exactly Proposition 5.9. No finite-type assumption on \(G\) was needed for this theorem. \(\square\)

**Example 5.11. An additive obstruction.** The additive group over any field acts on \(k^2\) by

\[
u\longmapsto\begin{pmatrix}1&u\\0&1\end{pmatrix}.
\]

Its universal invariant subspace is \(ke_1\): evaluate the action over \(k[u]\), where multiplication by the indeterminate \(u\) detects a nonzero second coordinate. The equivariant quotient \(k^2\to k\) taking that coordinate maps these invariants to zero, whereas the quotient representation is trivial. Invariants are therefore not exact and \(\mathbf G_a\) is not linearly reductive in any characteristic. The regular cocycle \(z(u)=u\) with trivial coefficients represents a nonzero class in \(H^1_{\mathrm{reg}}(\mathbf G_a,k)\): it is additive and nonzero as a polynomial, while every coboundary for the trivial action is zero. These assertions use the group scheme, including over finite fields, rather than only its rational points.

### 5.12. Finite representations over Noetherian rings

**Lemma 5.12. Serre's finite-subcomodule construction.** Let \(R\) be Noetherian, \(C\) a flat counital coassociative \(R\)-coalgebra, and \(M\) a right \(C\)-comodule. Every finitely generated \(R\)-submodule \(N\subset M\) is contained in a finitely generated subcomodule. Consequently \(M\) is the filtered union of its finite subcomodules. Neither \(C\) nor \(M\) is assumed finite or projective.

**Proof.** Write the coaction as \(\rho:M\to M\otimes_RC\). The images of a finite generating list of \(N\) are finite sums of pure tensors. Their first factors generate a finite submodule \(T\subset M\) with \(\rho(N)\subset T\otimes C\). Flatness of \(C\) identifies this tensor with a submodule of \(M\otimes C\). With \(\pi:M\to M/T\), define

\[
W=\ker\bigl((\pi\otimes1)\rho\bigr).
\]

It contains \(N\). Applying the counit to \(\rho(W)\subset T\otimes C\) gives \(W\subset T\), so \(W\) is finite by Noetherianity. Coassociativity gives

\[
\begin{aligned}
\bigl(((\pi\otimes1)\rho)\otimes1\bigr)\rho
&=(\pi\otimes\Delta_C)\rho.
\end{aligned}
\]

The right side is zero on \(W\), because its coaction lies in \(T\otimes C\). Flatness identifies the kernel on the left with \(W\otimes C\). Thus \(\rho(W)\subset W\otimes C\), and the counit and coassociativity identities restrict to \(W\); it is a subcomodule. Sums of two finite subcomodules are finite subcomodules, so this family is filtered and contains every element of \(M\). \(\square\)

**Theorem 5.13. Closed linear embeddings over a field or Dedekind ring.** If \(R\) is a field or Dedekind domain and \(G/R\) is flat, affine and of finite type, there is a closed immersion \(G\hookrightarrow\mathrm{GL}_{n,R}\) for some finite \(n\). This proves scheme-theoretic faithfulness, including all nonreduced test algebras.

**Proof.** Put \(H=R[G]\) with its regular coaction. Choose finitely many algebra generators of \(H\); Lemma 5.12 puts their \(R\)-span in a finite stable submodule \(F\subset H\). Over a field it is finite free. Over a Dedekind domain it is finite projective: it is torsion-free because \(H\) is flat, and at every nonzero prime it is a finite torsion-free module over a DVR. Such a module embeds into a finite free module after clearing denominators, and is free by the submodule theorem for a principal ideal domain. At the zero prime it is a vector space. Thus it is locally free of finite rank; finite presentation over the Noetherian ring gives projectivity.

The coaction on \(F\) defines \(G\to\mathrm{GL}(F)\). Locally choose a basis \(f_1,\ldots,f_r\), and write

\[
\Delta(f_j)=\sum_i f_i\otimes a_{ij}.
\]

The coefficients \(a_{ij}\) are images of matrix coordinate functions. The counit identity gives \(f_j=\sum_i\epsilon(f_i)a_{ij}\), so the image of the coordinate map contains \(F\), hence all the chosen algebra generators of \(H\). That coordinate map is surjective locally and therefore globally. The morphism is a closed immersion. Choose a finite projective complement \(F'\) with \(F\oplus F'=R^n\), and let \(G\) act trivially on \(F'\). The inclusion \(\mathrm{GL}(F)\hookrightarrow\mathrm{GL}(F\oplus F')\) is closed: on local bases it is given by zero off-diagonal blocks and an identity block on \(F'\). These equations glue. Composition gives the asserted closed immersion. \(\square\)

**Lemma 5.14. A stable projective enlargement in dimension two.** Let \(R\) be Noetherian regular of dimension at most two, \(H\) a flat \(R\)-Hopf algebra, and \(F\subset H\) a finite subcomodule for the regular coaction. There is a finite projective subcomodule \(P\subset H\) containing \(F\).

**Proof.** We give the extension argument, including why the enlargement stays inside \(H\). We use [*Projective dimension and the Auslander–Buchsbaum formula*](../../AG-CA/src/projective-dimension-and-the-auslander-buchsbaum-formula.md), Theorem 1.3 and Corollary 4.3: the second syzygy of any module over a regular local ring of dimension at most two is projective. For every finite module \(L\), dualizing a finite presentation gives

\[
0\longrightarrow L^\vee\longrightarrow R^u
\longrightarrow R^v\longrightarrow Q\longrightarrow0.
\]

After each localization \(L^\vee\) is a second syzygy, hence finite free. Thus \(L^\vee\) is finite projective. In particular \(P=F^{\vee\vee}\) is finite projective.

A Noetherian regular ring is normal, and its finitely many components are disjoint and clopen, by [*Discrete valuation rings, normal rings and Serre's criterion*](../../AG-CA/src/discrete-valuation-rings-normal-rings-and-serres-criterion.md), Corollary 4.5 and its ring normality proof. Apply the argument on each domain factor of \(R\). The flat module \(H\), and therefore \(F\), is torsion-free. A finite torsion-free module embeds in a finite free module by choosing coordinates over the fraction field and clearing denominators of its generators. Those coordinate functionals show that \(F\to P\) is injective.

Let \(U\subset\operatorname{Spec}R\) be the open locus where this injection is an isomorphism. It is open because the cokernel is finite. It contains all points of height at most one: over a field or DVR, finite torsion-free modules are free and equal their bidual. The algebraic Hartogs statement in the same normal-ring lesson, Theorem 3.3, says that \(R\) is the intersection of its height-one localizations inside its fraction field. It follows that

\[
\Gamma(U,\mathcal O_U)=R.
\]

Indeed a section on this dense open is a rational function, belongs to every height-one localization, and hence belongs to \(R\); restriction gives the converse.

For every flat \(R\)-module \(A\) and quasi-coherent \(\mathcal E\) on \(U\), there is an isomorphism

\[
\Gamma(U,\mathcal E)\otimes_RA
\simeq\Gamma(U,\mathcal E\otimes_R A).
\]

Choose a finite cover of \(U\) by basic affine opens; such a cover exists by Noetherianity. Its pairwise intersections are basic affine opens too. Sections are the equalizer of the two maps from the finite product of chart sections to the finite product of intersection sections. Flat tensor preserves that equalizer and the finite products; on each affine chart the comparison is the usual module tensor identity. This proves the displayed isomorphism without any finite-generation condition on \(A\).

For \(\mathcal E=\mathcal O_U\) and \(A=H\), it gives \(H=\Gamma(U,\widetilde H)\). Because \(P\) is a direct summand of a finite free module, Hartogs also gives \(P=\Gamma(U,\widetilde P)\). On \(U\), the modules \(F\) and \(P\) are equal, so their inclusion into \(\widetilde H\) gives a canonical injection \(P\hookrightarrow H\) extending the original inclusion of \(F\). Injectivity follows on \(U\), where \(P\) is torsion-free, and that open is dense.

The restricted coaction on \(F|_U\) now gives, by the same equalizer comparison with the flat module \(H\), a map

\[
P\longrightarrow P\otimes_RH.
\]

Its composite into \(H\otimes_RH\) is the original regular coaction on \(P\): they agree on \(U\), and the Hartogs comparison is injective for the flat module \(H\otimes_RH\). Flatness also makes \(P\otimes H\) a submodule of \(H\otimes H\). The counit and coassociativity identities therefore restrict to \(P\), proving that it is the required subcomodule. Recombining the finitely many domain factors proves the assertion for \(R\). \(\square\)

**Theorem 5.15. Raynaud–Gabber linearity in dimension at most two.** For a Noetherian regular ring \(R\) of dimension at most two, every flat affine finite-type \(R\)-group scheme is a closed subgroup of some \(\mathrm{GL}_{n,R}\).

**Proof.** Choose finitely many algebra generators of \(H=R[G]\). Lemma 5.12 supplies a finite subcomodule of the regular representation containing them, and Lemma 5.14 enlarges it inside \(H\) to a finite projective subcomodule \(P\). The coefficient-and-counit argument of Theorem 5.13 shows that \(G\to\mathrm{GL}(P)\) is a closed immersion, because the image of its coordinate map contains every generator of \(H\). Adding a finite projective complement with trivial action yields the closed immersion into \(\mathrm{GL}_{n,R}\). All equations are universal, so arbitrary base change preserves the embedding. \(\square\)

### 5.16. Split unipotent kernels and Mostow's theorem

A **split unipotent group** here is a smooth connected affine algebraic group \(U/k\) with a finite series \(1=U_0\subset\cdots\subset U_r=U\), where each \(U_{i-1}\) is normal in \(U_i\) and \(U_i/U_{i-1}\simeq\mathbf G_a\). Normality in the whole group is not required of this initial series. We supply the characteristic central subgroup needed for the extension argument, rather than assuming that an arbitrary chosen series is preserved by conjugation.

**Lemma 5.16. Fixed vectors and triangularization.** Over any field, every nonzero finite-dimensional representation of a split unipotent group has a nonzero fixed vector. It has a complete invariant flag with trivial one-dimensional quotients. Such a group has a closed embedding into a group of upper unitriangular matrices over the original field.

**Proof.** For \(\mathbf G_a\), write the coaction of a nonzero vector as

\[
\rho(v)=\sum_{i=0}^m v_i\otimes t^i,\qquad v_m\ne0.
\]

Coassociativity, with \(\Delta(t)=t\otimes1+1\otimes t\), and comparison of the coefficient \(t^m\) in the last tensor factor give \(\rho(v_m)=v_m\otimes1\). Thus \(v_m\) is fixed, in every characteristic. For \(U\), induct on its series. The subspace fixed by \(U_{r-1}\) is nonzero by induction, is \(U\)-stable by normality, and carries the descended action of \(U/U_{r-1}=\mathbf G_a\). Descent here is through the represented fppf quotient in [*Quotients and torsors*](quotients-and-torsors.md), Theorem 11.1b. The additive case supplies a \(U\)-fixed vector. Apply this again to the quotient by its fixed line, and continue to get the flag.

Theorem 5.13 gives a closed faithful finite-dimensional representation of \(U\). A basis adapted to the flag puts its matrices in upper unitriangular form. This is an assertion about the full coaction, hence all test algebras, and the closed embedding factors through that closed matrix subgroup. \(\square\)

**Lemma 5.17. Commutative unipotent groups in characteristic zero.** Let \(k\) have characteristic zero, and let \(V\) be a smooth connected commutative closed subgroup of an upper unitriangular group. Then \(V\) has a canonical vector-group structure \(V\simeq W(\operatorname{Lie}V)\), compatible with every group automorphism and every scalar extension.

**Proof.** In upper unitriangular size \(n\), the strict upper triangular matrix algebra has \(N^n=0\). The finite polynomials

\[
\begin{aligned}
\log(1+A)&=\sum_{i=1}^{n-1}(-1)^{i+1}A^i/i,\\
\exp(X)&=\sum_{i=0}^{n-1}X^i/i!
\end{aligned}
\]

are inverse isomorphisms of the ambient affine spaces. Their identities follow by substitution of the usual formal identities in the single variable quotient \(\mathbb Q[z]/(z^n)\).

For \(v\in V(\overline k)\), put \(X=\log v\). The polynomial curve \(\exp(tX)\) belongs to \(V\): every nonnegative integer value is \(v^m\), and each defining equation vanishes at infinitely many integers, so is the zero polynomial. Its tangent at zero is \(X\), hence \(X\in\operatorname{Lie}V\). Consequently \(\log(V)\) is a closed subset of that linear space. This is a scheme inclusion: over \(\overline k\), \(V\) is reduced, and vanishing at its rational points detects functions. Its dimension is \(\dim V=\dim\operatorname{Lie}V\), by smoothness. A proper closed subset of a finite-dimensional affine space has smaller dimension, so the reduced closed scheme \(\log(V)\) is the whole linear space. Field descent proves the equality over \(k\).

Matrices \(\log v\) commute, because the original matrices \(v\) commute. Rational-point density therefore makes every pair of matrices in \(\operatorname{Lie}V\) commute. The binomial identity for commuting matrices gives \(\exp(X+Y)=\exp(X)\exp(Y)\). Thus these polynomial isomorphisms identify \(V\) with the additive group of its Lie algebra, and their tangent map is the identity.

For any \(k\)-algebra \(B\), every additive polynomial map \(B^d\to B^e\), interpreted as a morphism of vector group schemes, is linear. Decompose each coordinate polynomial into homogeneous parts. The identity \(f(2x)=2f(x)\) kills each part of degree \(j\ge2\), since \(2^j-2\) is a unit in this \(\mathbb Q\)-algebra; its constant part is zero. The degree-one part is its derivative. Hence an automorphism of a vector group is exactly an invertible linear map, on all tests. Any two vector identifications of \(V\) inducing the identity on its Lie algebra differ by such an automorphism with identity derivative and are equal. This proves canonicity, automorphism compatibility and scalar-extension compatibility. \(\square\)

**Lemma 5.18. A characteristic central vector subgroup.** In characteristic zero a nontrivial split unipotent \(U\) has a nontrivial smooth connected central subgroup \(V\), preserved by conjugation in every algebraic group containing \(U\) as a normal subgroup. It is a vector group; \(U/V\) is split unipotent of smaller dimension; and \(U(k)\to(U/V)(k)\) is surjective.

**Proof.** Embed \(U\) in the unitriangular group by Lemma 5.16. Form its lower central series of closed algebraic subgroups: start with \(C_1=U\), and let \(C_{j+1}\) be the smallest closed subgroup containing the image of the commutator map \(U\times C_j\to U\). We spell out the closure properties used here. The subgroup is the reduced closure of products of commutators and their inverses. Its defining ideal is the intersection of the kernels of the pullbacks along all these finite word maps. Such intersections commute with field extension: express an element after tensoring with a field in finitely many linearly independent field coefficients; membership in every extended kernel is precisely membership of each coefficient in every original kernel. The same description shows that inversion and multiplication preserve the ideal. For multiplication, testing two word maps gives their concatenated word; injectivity can be checked on finitely many word maps on each finite-dimensional space of coefficients. Thus this closure is a group scheme and is the smallest closed subgroup in question.

All word maps have geometrically connected source and contain the identity in their image. Their union, and its closure, are geometrically connected. Every \(C_j\) is smooth in characteristic zero, by the finite-type Cartier theorem and the smoothness theorem of the Lie-algebra lesson. The construction commutes with field extension and is characteristic under automorphisms of \(U\), because automorphisms carry commutator words to commutator words.

Let \(\mathfrak n\) denote the strict upper triangular matrix algebra. The elementary identity

\[
[1+\mathfrak n^i,\,1+\mathfrak n^j]
\subset 1+\mathfrak n^{i+j}
\]

follows by multiplication and the finite inverse series: modulo \(\mathfrak n^{i+j}\), the two matrices commute. Hence \(C_j\subset1+\mathfrak n^j\), and the series terminates. Take its last nontrivial term \(V\). The next commutator subgroup is trivial, so \(V\) is central. It is smooth and geometrically connected, and has positive dimension: a smooth connected zero-dimensional group is the identity. Lemma 5.17 makes it a vector group.

For conjugation by an ambient algebraic group \(E\), the subgroup \(V_{\overline k}\) is preserved by every \(e\in E(\overline k)\). In characteristic zero \(E_{\overline k}\times V_{\overline k}\) is reduced. The equations of \(V\), pulled back by conjugation, vanish at all its rational points and therefore vanish identically. Thus conjugation factors through \(V\) as a morphism, including all nonreduced tests; \(V\) is normal in \(E\).

The represented affine quotient \(U/V\) exists by *Quotients and torsors*, Theorems 11.1b and 11.1d. It is smooth: its characteristic-zero group structure is reduced, and the field smoothness theorem applies. It is connected as a surjective image of \(U\). Images of the original series in \(U/V\) are closed group schemes by *Group schemes over a field*, Proposition 5.8. Normality of one step in the next descends through these faithfully flat image maps. Each successive quotient is a quotient of \(\mathbf G_a\), by the represented normal-quotient universal property; descent through \(U_i\to U_i/U_{i-1}\) makes the induced map from \(\mathbf G_a\) faithfully flat. A proper closed subgroup of \(\mathbf G_a\) in characteristic zero is trivial: it is finite and geometrically reduced, and a finite additive subgroup of a characteristic-zero field is zero. Thus a nontrivial such quotient has trivial kernel and is \(\mathbf G_a\), since a monomorphic fppf cover is an isomorphism. Trivial steps can be removed. This gives a split unipotent series for \(U/V\). Since \(V\) has positive dimension, the quotient has smaller dimension by the kernel dimension formula, Theorem 5.10 of the field-group lesson.

Finally the fibre above a \(k\)-point of \(U/V\) is a vector-group torsor over \(k\). Additive faithfully flat descent, proved in *Quotients and torsors*, Lemma 8.2, makes this torsor trivial. It has a \(k\)-point, proving the rational-point surjectivity. \(\square\)

**Theorem 5.19. Mostow splitting and conjugacy.** Let \(k\) have characteristic zero, \(G/k\) be a linearly reductive affine algebraic group, and \(U/k\) a split unipotent group. Every fppf exact sequence of algebraic group schemes

\[
1\longrightarrow U\longrightarrow E
\longrightarrow G\longrightarrow1
\]

has a group-scheme section \(G\to E\), and any two such sections are conjugate by an element of \(U(k)\).

**Proof.** The map \(E\to G\) is a represented \(U\)-torsor, so \(E\) is affine by affine descent, *Quotients and torsors*, Proposition 6.2. Induct on \(\dim U\); the zero-dimensional case has \(U=1\). Choose the central vector subgroup \(V\) of Lemma 5.18. It is normal in \(E\), and the represented affine quotient \(E/V\) gives an extension of \(G\) by the smaller split unipotent group \(U/V\). By induction it has a group section \(\overline s\).

Pull back \(E\to E/V\) along \(\overline s\). The result is an extension of \(G\) by the vector group \(V\). Conjugation induces a linear representation of \(G\) on \(V\), by the all-test automorphism calculation in Lemma 5.17. The underlying vector torsor over the affine \(G\) has a morphism section, by the exact additive Amitsur argument of Proposition 5.9. Its failure to be a group section is the regular two-cocycle proved there. Linear reductivity makes invariants exact on all representations by Theorem 5.10. The derived-invariants calculation of Theorem 5.7 therefore gives

\[
H^1(G,V)=H^2(G,V)=0.
\]

Proposition 5.9 corrects that morphism section into a group section, giving a section into \(E\). This proves existence.

For two sections into \(E\), induction makes their images in \(E/V\) conjugate by a point of \((U/V)(k)\). Lemma 5.18 lifts that point to \(u\in U(k)\). After conjugating one section, their quotient sections agree. Both now lie in the same pullback vector extension of \(G\). Proposition 5.9 and the vanishing of \(H^1(G,V)\) make them conjugate by a point of \(V(k)\). Combining the two conjugations gives a point of \(U(k)\), proving the assertion over the original ground field. \(\square\)

### 5.20. Which smooth connected groups are linearly reductive?

The answer changes with the characteristic. The finite-subgroup argument below explains the obstruction in positive characteristic; Weyl's theorem explains the characteristic-zero case. We use the proved structure results in [Tori, maximal tori and their conjugacy](../../AG-RG/AG-RG-01.md), Section 2, [Regular elements and centralizers](../../AG-RG/AG-RG-02.md), Theorem 2.1, and [Roots and reductive groups of rank one](../../AG-RG/AG-RG-03.md), Theorem 4.1. These supply a split additive filtration of a smooth connected unipotent group over an algebraically closed field, a maximal torus with centralizer equal to itself in a reductive group, and an additive root subgroup for every nonzero root. The characteristic-zero reductive structure input is [Pinnings and the classification of split reductive groups](../../AG-RG/AG-RG-05.md), Theorem 5.1, Section 6 and Theorem 10.1: over an algebraically closed field a reductive group is a finite central quotient of a product of a torus and a simply connected semisimple group whose Lie algebra is semisimple. These are internal proof providers, rather than an appeal to a classification assertion in an external reference.

**Lemma 5.20.** A finite closed subgroup scheme \(H\) of an affine linearly reductive group scheme \(G\) over a field is linearly reductive. Neither smoothness nor finite type of \(G\) is required.

**Proof.** Right translation by \(H\) is schematically free. [Quotients and torsors](quotients-and-torsors.md), Theorem 4.3, gives an affine quotient \(Q=G/H\) and a finite faithfully flat \(H\)-torsor \(q:G\to Q\). For an arbitrary \(H\)-module \(M\), descend the quasi-coherent module \(\mathcal O_G\otimes_k M\), with its diagonal right \(H\)-descent datum, along \(q\). The module-descent proof at the beginning of that lesson gives a quasi-coherent module \(\mathcal E_M\) on \(Q\). Put
\[
N(M)=\Gamma(Q,\mathcal E_M).
\]
Left translation by \(G\) commutes with the right \(H\)-action and gives \(N(M)\) a rational \(G\)-module structure. Descent and this action use arbitrary modules: they impose no finite-dimensional condition on \(M\).

The functor \(N\) is exact. Indeed a short exact sequence of \(H\)-modules becomes an exact sequence after tensoring with \(\mathcal O_G\). Faithful flatness of \(q\) detects exactness of the descended sheaves. Since \(Q\) is affine, global sections of quasi-coherent modules preserve this exact sequence. Equivalently, module descent identifies its pullback with the original exact sequence, and a faithfully flat scalar extension detects its kernels and cokernels.

There is a natural isomorphism
\[
N(M)^G\simeq M^H.
\]
To check it, identify a section of \(\mathcal E_M\) with a regular \(M\)-valued function on \(G\) satisfying \(f(gh)=h^{-1}f(g)\), interpreted as a comodule identity on all test algebras. Left-translation invariance makes \(f\) the constant function with value \(f(1)\): apply the counit in the corresponding left-invariance identity. The right identity then says exactly that \(f(1)\in M^H\). Conversely every such invariant vector defines this constant section. Thus the composition of the exact functor \(N\) with exact \(G\)-invariants is \(H\)-invariants. Theorem 5.10 gives the result. \(\square\)

**Lemma 5.21.** In characteristic zero, a subspace of a finite-dimensional rational representation of a smooth connected algebraic group is stable under the group if it is stable under its Lie algebra.

**Proof.** The stabilizer of the subspace is a closed subgroup scheme \(J\subset G\): in a basis beginning with the subspace, set the lower-left matrix block equal to zero. Its Lie algebra consists precisely of the tangent operators preserving that subspace. Thus the hypothesis gives \(\operatorname{Lie}J=\operatorname{Lie}G\). The finite-type Cartier theorem in [Lie algebras and smoothness](lie-algebras-and-smoothness.md), Theorem 4.3, makes \(J\) smooth. Consequently \(\dim J=\dim G\). The smooth connected group \(G\) is irreducible, by [Group schemes over a field](group-schemes-over-a-field.md), Section 2. A closed reduced subgroup of that same dimension is all of \(G\). This proves the schematic equality \(J=G\), hence stability on every test algebra. \(\square\)

**Theorem 5.22. Nagata's classification in the smooth connected case.** Let \(G\) be a smooth connected affine algebraic group over a field \(k\).

1. If \(\operatorname{char}k=0\), then \(G\) is linearly reductive if and only if it is reductive.
2. If \(\operatorname{char}k>0\), then \(G\) is linearly reductive if and only if it is a torus.

Here reductivity and the torus property are geometric properties; no splitting over \(k\) is assumed.

**Proof.** Theorem 5.10 permits extension to an algebraic closure and detects linear reductivity there. The other two properties are geometric, and the identity-component result in [Group schemes over a field](group-schemes-over-a-field.md), Proposition 2.4, preserves connectedness. We therefore work over an algebraically closed field.

First, in every characteristic, linear reductivity implies reductivity. Exact invariants split every finite-dimensional submodule inclusion \(W\subset V\): restriction gives a surjective map of rational \(G\)-modules
\[
\operatorname{Hom}_k(V,W)\longrightarrow\operatorname{End}_k(W),
\]
and lifting the invariant identity gives an equivariant projection onto \(W\). Induction on dimension makes \(V\) a direct sum of irreducibles. If \(U\subset G\) is a smooth connected normal unipotent subgroup, its split additive filtration is supplied by the solvable structure proof in the first provider above. Lemma 5.16 therefore makes \(V^U\ne0\) for every nonzero irreducible \(G\)-module \(V\). Normality makes \(V^U\) a \(G\)-submodule, so it is all of \(V\). Apply this to every summand of a faithful finite-dimensional representation, which exists by Theorem 5.13 over the field. Then \(U\) acts trivially on that faithful representation and must be trivial as a subgroup scheme. This is exactly reductivity.

Suppose now that the characteristic is zero and \(G\) is reductive. The internal reductive structure theorem identified above gives a finite central isogeny
\[
\pi:T\times S\longrightarrow G,
\]
where \(T\) is a split torus and \(\mathfrak s=\operatorname{Lie}S\) is semisimple. The latter assertion follows from the explicit characteristic-zero Lie-algebra construction in Section 6 of that provider; its finite central quotients have the same Lie algebra in characteristic zero. Let \(W\subset V\) be a finite-dimensional rational \(G\)-submodule and pull back the representation along \(\pi\). Decompose \(V\) and \(W\) into \(T\)-weight spaces. Each space is stable under \(S\), because the two factors commute. Weyl's theorem in [Complete reducibility: Casimir elements and Weyl's theorem](../../RT-LIE/src/RT-LIE-04.md), Theorems 3.3 and 4.1, supplies an \(\mathfrak s\)-equivariant projection on each weight space onto its part of \(W\). Their direct sum is \(T\)-equivariant. Its kernel and its image are \(S\)-stable by Lemma 5.21, so the projection is also \(S\)-equivariant. It is therefore equivariant for \(T\times S\), and faithful flatness of \(\pi\) detects equivariance for \(G\). Every finite-dimensional submodule has a complement.

This also proves exactness of invariants for arbitrary rational modules. If \(M\to N\) is surjective and \(n\in N^G\), choose a lift \(m\). The finite-subcomodule lemma gives a finite-dimensional stable subspace \(V\subset M\) containing \(m\). Its image contains \(n\), and the finite-dimensional splitting just proved lifts \(n\) to an invariant vector in \(V\). Thus \(M^G\to N^G\) is surjective. Left exactness of invariants finishes the characteristic-zero case.

Finally let the characteristic be \(p>0\), and suppose \(G\) is linearly reductive. We already know that it is reductive. Choose a maximal torus \(T\). If there is a nonzero root, the internal root-group theorem gives a closed subgroup \(U_\alpha\simeq\mathbf G_a\). Inside it, the equation \(x^p-x=0\) gives the constant subgroup \(H\simeq\mathbf Z/p\mathbf Z\). This finite subgroup is not linearly reductive, as the following example proves. Lemma 5.20 gives a contradiction. There are therefore no roots. The centralizer theorem makes the zero-weight subspace of \(\operatorname{Lie}G\) precisely \(\operatorname{Lie}T\); absence of nonzero weights gives \(\dim G=\dim T\). Since both are smooth connected and \(T\) is closed, irreducibility gives \(G=T\). Conversely a torus becomes diagonalizable after a separable field extension; Proposition 5.8 and Theorem 5.10 prove its linear reductivity over \(k\). \(\square\)

**Example 5.23.** In characteristic \(p\), let \(H\) be the constant group \(\mathbf Z/p\mathbf Z\) and let \(M=k[H]\) be its regular permutation representation, with basis \(e_h\). The augmentation \(\epsilon:M\to k\), \(\sum a_he_h\mapsto\sum a_h\), is surjective and equivariant. Its invariant subspace is the line generated by \(\sum_he_h\), since translation permutes the basis transitively. But
\[
\epsilon\!\left(\sum_he_h\right)=p=0.
\]
Thus this surjection is not surjective on invariants. The obstruction uses an étale subgroup; it does not require an infinitesimal subgroup or a failure of smoothness.

## 6. Translating geometry from the identity

For any \(T\to S\) and any \(g\in G(T)\), multiplication by \(g\) on either side is an automorphism of \(G_T\); multiplying by \(g^{-1}\) gives its inverse. One must first make this base change if \(g\) is not an \(S\)-section.

**Proposition 6.1. Separatedness at the identity.** A group scheme \(f:G\to S\) is separated if and only if \(e:S\to G\) is a closed immersion. It is quasi-separated if and only if \(e\) is quasi-compact.

**Proof.** If \(f\) is separated, a section is closed: the section is a base change of the diagonal along \(g\mapsto(g,e(f(g)))\). The same argument gives quasi-compactness of the section when the diagonal is quasi-compact. For the converse define \(d:G\times_SG\to G\) by \(d(g,h)=g^{-1}h\). The square with the diagonal \(G\to G\times_SG\) on top, \(S\xrightarrow{e}G\) on the bottom, structure map on the left and \(d\) on the right is cartesian. On every test scheme its fibre condition is \(g^{-1}h=e\), which is exactly \(g=h\). Thus the diagonal is a base change of \(e\). Closed immersions and quasi-compact morphisms are preserved by base change, proving both converses. \(\square\)

*Reference:* [Stacks, Tag 047G].

Put \(\omega_{G/S}=e^*\Omega_{G/S}\); this is the cotangent module at the identity.

**Theorem 6.2. Invariant differentials.** There is a canonical isomorphism

\[
\Omega_{G/S}\simeq f^*\omega_{G/S}
\]

for every group scheme over \(S\). In particular, over a field, \(\Omega_{G/k}\) is a free \(\mathcal O_G\)-module, with no smoothness assumption.

**Proof.** View \(G\times_SG\) as a scheme over its first factor and consider the isomorphism

\[
\Phi(g,h)=(g,gh),\qquad\Phi^{-1}(g,u)=(g,g^{-1}u).
\]

Relative to this first factor its sheaf of differentials is \(\operatorname{pr}_2^*\Omega_{G/S}\), by base change for differentials. Since \(\Phi\) is an isomorphism over that factor, its differential gives an isomorphism

\[
\Phi^*\operatorname{pr}_2^*\Omega_{G/S}
\longrightarrow\operatorname{pr}_2^*\Omega_{G/S}.
\]

Pull it back along \(s(g)=(g,e(f(g)))\). On the left, \(\operatorname{pr}_2\Phi s=g\), so the pullback is \(\Omega_{G/S}\). On the right, \(\operatorname{pr}_2s=ef\), so the pullback is \(f^*e^*\Omega_{G/S}\). This is the required isomorphism. Over a field the vector space \(\omega_{G/k}\) has a basis, and its pullback is free. \(\square\)

*Reference:* [Stacks, Tag 047I].

The construction identifies a covector at the identity with the form obtained at each point by translation. For \(\mathbf G_a\) this gives \(dx\). For \(\mathbf G_m\) it gives \(dt/t\), since multiplication by \(g\) sends \(t\) to \(gt\), whose relative differential in the variable \(t\) is \(g\,dt\). For \(\mu_n\), the equation \(t^n=1\) implies that its identity cotangent module is \(R/(n)\,dt\). Freeness of the whole differential sheaf over a field therefore does not imply smoothness: \(\Omega_{\mu_p/k}\) has rank one but \(\mu_p\) has dimension zero.

**Proposition 6.3. First-order multiplication is addition.** In the tangent space at the identity over a field, the differential of multiplication is

\[
T_eG\oplus T_eG\longrightarrow T_eG,\qquad(v,w)\longmapsto v+w.
\]

**Proof.** The differential is a linear map from the displayed direct sum. On the first summand it is the identity, since \(m(g,e)=g\); on the second it is the identity, since \(m(e,h)=h\). Linearity now gives the formula. Equivalently, tangent vectors are maps from \(k[\varepsilon]/(\varepsilon^2)\) reducing to \(e\); terms involving the product of their two first-order changes have a factor \(\varepsilon^2\) and vanish. Thus the kernel of \(G(k[\varepsilon])\to G(k)\) is an abelian group under the addition in \(T_eG\). The same argument after replacing \(k\) by a test algebra gives addition on first-order directions along the identity over a general base. \(\square\)

The next lesson, *Lie algebras and smoothness of group schemes*, extracts a bracket from second-order information and explains what tangent dimension says about smoothness.

## 7. Exercises

1. **Easy — equations and matrix entries.** For \(\mathrm{GL}_2\), write its coproduct and inverse using four entries \(a,b,c,d\) and \(D=ad-bc\). Verify that \(D\) is group-like. Give the corresponding three maps for \(\mu_6\) over an arbitrary ring.
2. **Easy — detecting a thick point.** Over \(\mathbf F_p\), compare the points of \(\mu_p\) on a field and on \(B=\mathbf F_p[\varepsilon]/(\varepsilon^2)\). Give its points on an arbitrary \(\mathbf F_p\)-algebra, and prove that its coordinate ring is nonreduced.
3. **Medium — two weights and a shifted module.** Give \(A=R[x,y]\) degrees \(2,-3\). Describe the action, its invariants and the equivariant structure on a free module \(Aq\) with \(q\) of degree \(5\). Explain why the same construction for an abelian group \(L\) characterizes all \(D_R(L)\)-actions on affine schemes.
4. **Medium — a schematic kernel.** Compute the kernel of \(b\mapsto b^p\) on \(\mathbf G_a\), including its Hopf algebra. Why is this the relative Frobenius kernel for \(\mathbf G_a\) after identifying its Frobenius twist with \(\mathbf G_a\)?
5. **Medium — duality without separability.** Compute the Cartier dual of \((\mathbf Z/6)_S\) when \(6\) need not be invertible. Over an \(\mathbf F_3\)-algebra, compute the multiplication in the dual of \(R[x]/(x^3)\) and its evaluation pairing.
6. **Hard — building a matrix realization.** Starting from finite algebra generators of a Hopf algebra over a field, construct a finite-dimensional regular subrepresentation and prove that its coefficient map from a general linear group's coordinate ring is surjective. Carry this out for \(k[x,y]\) with both \(x,y\) primitive, using \(\langle1,x,y\rangle\).
7. **Medium — forms on a finite group.** Compute \(\omega_{\mu_n/R}\) directly from the conormal relation at \(t=1\). Compare \(\mu_p\) and \(\alpha_p\) over a field of characteristic \(p\).

8. **Medium — a section functor need not be a vector scheme.** Over \(\mathbf Z\), compare \(V(\mathbf Z/2)\) and \(W(\mathbf Z/2)\), prove that the latter is not represented by a scheme, and compute the failure of Hom base change for \((P,Q)=(\mathbf Z/2,\mathbf Z)\).
9. **Medium — universal injectivity.** The map \(\mathbf Z\xrightarrow{2}\mathbf Z\) is injective. Determine whether the induced map of additive group schemes is a monomorphism, and reconcile the answer with Proposition 2.6.
10. **Medium — untwist an additive representation.** For the representation in Example 5.11, write \(U\) and \(U^{-1}\) of Proposition 5.6 on polynomial pairs \((f_1(x),f_2(x))\). Determine the invariants of its diagonal tensor product with \(k[x]\), in every characteristic.
11. **Hard — cohomology of the sign representation.** For \((\mathbf Z/2)_{\mathbf Z}\) acting by sign on \(M=\mathbf Z\), compute \(H^1_{\mathrm{reg}}(G,M)\) and \(H^2_{\mathrm{reg}}(G,M)\) directly from normalized cocycles. Compare degree-zero invariants and degree-two cohomology after reduction modulo \(2\).
12. **Medium — finite weights and a kernel.** Give the two free summands of \(R^2\) the weights \(4,6\) for \(\mathbf G_m\). Determine the scheme-theoretic kernel over every \(R\), including characteristic \(2\), and describe the closed image after passing to the quotient character group.

## 8. Solutions

**1.** The coproducts are

\[
\begin{aligned}
\Delta(a)&=a\otimes a+b\otimes c,&\Delta(b)&=a\otimes b+b\otimes d,\\
\Delta(c)&=c\otimes a+d\otimes c,&\Delta(d)&=c\otimes b+d\otimes d.
\end{aligned}
\]

The counit sends \(a,d\) to \(1\) and \(b,c\) to \(0\). The antipode sends the matrix to \(D^{-1}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\). The determinant of a product of two matrices is the product of their determinants, so \(\Delta(D)=D\otimes D\), \(\epsilon(D)=1\), and \(\sigma(D)=D^{-1}\). These equations also verify that localization at \(D\) respects the coproduct. For \(\mu_6\) the maps are \(t\mapsto t\otimes t\), \(t\mapsto1\) and \(t\mapsto t^5\). They respect \(t^6=1\), over every ring.

**2.** In characteristic \(p\), \(t^p-1=(t-1)^p\), so the ring is \(\mathbf F_p[u]/(u^p)\). Its class \(u\) is nonzero and nilpotent, proving nonreducedness. For any \(B\) the points are \(1+b\) with \(b^p=0\); the inverse exists because \(b\) is nilpotent. In a field \(b=0\). In the specified dual-number algebra, \(b^p=0\) precisely for \(b=c\varepsilon\): writing \(b=b_0+b_1\varepsilon\), its \(p\)-th power is \(b_0^p=b_0\). Hence there are \(p\) such points, and their multiplication adds the coefficients \(c\).

**3.** The coaction is \(x\mapsto x\otimes t^2\), \(y\mapsto y\otimes t^{-3}\), so the right action and invariant algebra are those in Example 4.2. The module coaction is \(q\mapsto q\otimes t^5\), extended by compatibility with the algebra coaction. Thus \(x^ay^bq\) has degree \(2a-3b+5\). For general \(L\), expand a coaction against the basis \(z^\ell\) of \(R[L]\). Counitality expresses each element as a finite sum of its weight components, and coassociativity makes the coefficient projections mutually orthogonal idempotents. Multiplicativity adds weights. Conversely an \(L\)-grading defines that coaction on homogeneous elements. These two constructions are inverse, which proves the assertion for every affine algebra.

**4.** The kernel is the fibre over zero. Its ring is \(R[x]\otimes_{R[z]}R=R[x]/(x^p)\), where \(z\mapsto x^p\) in the first factor and \(z\mapsto0\) in the second. Its maps are \(x\mapsto x\otimes1+1\otimes x\), \(x\mapsto0\), \(x\mapsto-x\), well-defined because the base has characteristic \(p\). Thus it is \(\alpha_p\). The relative Frobenius of \(\mathbf G_a\) has the same coordinate formula, with coefficients handled by the Frobenius-twisted target. Since \(\mathbf G_a\) descends from \(\mathbf F_p\), that twist has a canonical additive-group identification with \(\mathbf G_a\); after this identification the formula is \(x\mapsto x^p\). No claim that absolute Frobenius is \(R\)-linear on general coefficients is needed.

**5.** The basis calculation in Example 3.2 gives \(R[\mathbf Z/6]=R[t]/(t^6-1)\), so the dual is \(\mu_6\) over every affine open of \(S\) and hence over \(S\). No extraction of roots in the base was used. For \(R[x]/(x^3)\), let \(d_0,d_1,d_2\) be the dual basis. Then \(d_0=1\), \(d_1^2=2d_2\), and \(d_1d_2=d_2^2=0\). Putting \(y=d_1\) gives the Hopf algebra \(R[y]/(y^3)\), with primitive \(y\). Its pairing on \(a^3=b^3=0\) is \(1+ab+(ab)^2/2\). Here \(2^{-1}=2\) in every \(\mathbf F_3\)-algebra. This gives \(\alpha_3^D\simeq\alpha_3\).

**6.** Apply Lemma 5.1 separately to each generator in the regular comodule and take the finite sum of the resulting subcomodules, adding \(1\). This gives \(W\). If \(w_j\) is a basis, the coefficients of \(\Delta(w_j)=\sum_iw_i\otimes a_{ij}\) satisfy the matrix identities, so define \(G\to\mathrm{GL}(W)\). Counitality in the *first* factor gives \(w_j=\sum_i\epsilon(w_i)a_{ij}\), placing every generator in the coefficient algebra. The coefficient map is therefore surjective and the morphism is a closed immersion. For the two-generator example the matrix is

\[
\begin{pmatrix}1&x&y\\0&1&0\\0&0&1\end{pmatrix}.
\]

Its coefficients contain \(x\) and \(y\), so the same surjectivity is explicit. The construction works equally for nonreduced quotients with these primitive coordinates.

**7.** Differentiate \(t^n-1\) to get \(nt^{n-1}dt=0\), and then evaluate at \(t=1\). This gives \(\omega_{\mu_n/R}=R/(n)\,dt\); Theorem 6.2 extends it by translation to the whole group. For \(\alpha_p\), differentiation of \(x^p\) gives zero, so its identity cotangent space is one-dimensional over the field. The identity cotangent space of \(\mu_p\) has the same dimension. Both schemes have dimension zero, so neither is smooth, despite having a free differential sheaf of rank one.

**8.** The symmetric algebra is \(\mathbf Z[x]/(2x)\), so \(V(\mathbf Z/2)\) is represented by that affine additive group scheme; its \(B\)-points are the elements of \(B\) annihilated by \(2\). In contrast \(W(\mathbf Z/2)(B)=B/2B\). Already at \(B=\mathbf Z\) these are zero and \(\mathbf Z/2\), respectively. If \(W(\mathbf Z/2)\) were represented by any scheme, Theorem 2.4 would make \(\mathbf Z/2\) finite projective. A projective \(\mathbf Z\)-module is a summand of a free module and therefore torsion-free, a contradiction. Finally \(\operatorname{Hom}_{\mathbf Z}(\mathbf Z/2,\mathbf Z)=0\), while after base change both source and target are \(\mathbf F_2\), whose linear endomorphism space is \(\mathbf F_2\). Thus internal Hom cannot generally be identified with the section functor of an ordinary Hom module.

**9.** On \(B=\mathbf F_2\) multiplication by \(2\) is the zero map on a nonzero additive group. Hence it is not a monomorphism of group schemes. The cokernel of the original module injection is \(\mathbf Z/2\), which is not projective; the injection is not a direct-summand inclusion. Proposition 2.6 requires injectivity on every tensor extension, exactly the condition that fails here. Its schematic kernel is \(\operatorname{Spec}\mathbf Z[x]/(2x)\), which is not the trivial group scheme.

**10.** The universal matrix is \(\begin{pmatrix}1&x\\0&1\end{pmatrix}\). Consequently

\[
\begin{aligned}
U(f_1,f_2)&=(f_1+xf_2,f_2),\\
U^{-1}(f_1,f_2)&=(f_1-xf_2,f_2).
\end{aligned}
\]

In the coinduced representation, invariant polynomial pairs are constant. Indeed right-translation invariance says \(F(x+u)=F(x)\) in \(k[x,u]^2\); setting \(x=0\) makes \(F(u)=F(0)\). Untwisting therefore gives the diagonal invariants \((a-xb,b)\) for arbitrary \(a,b\in k\). This two-dimensional space is canonically the underlying \(k^2\) by evaluation at zero. The argument uses an independent indeterminate \(u\), so applies also to finite fields and characteristic \(2\).

**11.** Put \(\sigma^2=1\). A normalized one-cocycle is determined by \(a=z(\sigma)\); its only product condition is \(a+\sigma a=a-a=0\), so every integer occurs. Coboundaries have values \(\sigma b-b=-2b\), giving \(H^1_{\mathrm{reg}}(G,\mathbf Z)=\mathbf Z/2\). A normalized two-cocycle is determined by \(b=c(\sigma,\sigma)\). The cocycle equation at \((\sigma,\sigma,\sigma)\) gives \(\sigma b-b=-2b=0\), hence \(b=0\). All the remaining triples contain an identity and already satisfy the normalized equation, so \(H^2_{\mathrm{reg}}(G,\mathbf Z)=0\). After reduction modulo \(2\), the sign action is trivial. The one-cocycle condition is still automatic but all its coboundaries are zero, giving \(H^1_{\mathrm{reg}}(G_{\mathbf F_2},\mathbf F_2)=\mathbf F_2\). The degree-one groups happen to have the same underlying size; the coboundary maps and, as Proposition 5.5 shows, the degree-zero invariants have changed. In degree two every \(b\in\mathbf F_2\) is now a normalized cocycle and every normalized coboundary has value \(2a=0\), so the new degree-two group is \(\mathbf F_2\).

**12.** The subgroup generated by \(4\) and \(6\) in \(\mathbf Z\) is \(2\mathbf Z\), and Proposition 5.8 gives kernel \(D_R(\mathbf Z/2)=\mu_2\). Explicitly the kernel equations are \(t^4=t^6=1\), which imply \(t^2=t^6(t^4)^{-1}=1\), and the converse is immediate. In characteristic \(2\) this is \(R[t]/((t-1)^2)\), retaining its infinitesimal structure. Identify \(D_R(2\mathbf Z)\) with \(\mathbf G_m\) by its character \(s=z^2\). The image map is \(s\mapsto\operatorname{diag}(s^2,s^3)\), a closed immersion: its coordinate image contains \(s=s^3(s^2)^{-1}\) and \(s^{-1}\). Thus the factor map \(t\mapsto t^2\) and this closed immersion describe the full representation over every base ring.

## What this lesson assumes

The geometric facts used without proof are the affine scheme–ring equivalence [Stacks, Tag 01I2] and its fibre-product formula, Yoneda's lemma [Stacks, Tag 001P], the affine module description of quasi-coherent sheaves [Stacks, Tag 01IA], and base change for Kähler differentials [Stacks, Tag 01V0]. The finite locally free tensor-duality facts are proved locally by choosing a basis in Section 3. The claims about smoothness of the two infinitesimal examples use the elementary fact that a smooth zero-dimensional scheme over a field has zero cotangent space; the next lesson proves the group-scheme dimension criterion.

## References

- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf), 2014 author PDF; accessed 3 October 2026. The proof of Mostow splitting above includes the central-vector subgroup, affine torsor, cohomology and rational-conjugator steps.

- Jean-Émile Bertin, [*SGA 3, Exposé VI B: Généralités sur les schémas en groupes*](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp6B-13oct24.pdf), corrected re-edition of 13 October 2024; accessed 3 October 2026. The regular-base closed representation argument is proved above with exact local algebra providers.

- Jean-Pierre Serre, [*Groupe de Grothendieck des schémas en groupes réductifs déployés*](https://www.numdam.org/item/PMIHES_1968__34__37_0/), Publications mathématiques de l’IHÉS **34** (1968), 37–52; accessed 3 October 2026. Its finite-subcomodule construction is proved here for flat coalgebras over Noetherian rings.

- Nitin Nitsure, [*Representability of GL_E*](https://repository.ias.ac.in/30806/1/319.pdf), Proceedings of the Indian Academy of Sciences, Mathematical Sciences **112** (2002), 539–542; accessed 3 October 2026. The coherent-module automorphism criterion and its Artinian obstruction are proved above.

- **[Stacks]** The Stacks Project, *Groupoid Schemes*, especially Tags 022S, 047G, 047I, 07S1, 07S2 and 0EKJ–0EKL. These tags are retained in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition with AI-proposed corrections and AI-written additions. It is not reviewed by the maintainers of [the official Stacks Project](https://stacks.math.columbia.edu/). The exposition and proofs here are independently written.
- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected author edition of 5 October 2021; Cambridge University Press, 2022. The discussions of Hopf algebras, linear representations and finite group schemes give further background. [Corrected author edition, freely available PDF](https://www.jmilne.org/math/Books/iAG2022.pdf).

- **[SGA I]** Michel Demazure, *Structures algébriques. Cohomologie des groupes*, SGA 3, Exposé I, corrected re-edition of 13 October 2024. [Open corrected text](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp1-13oct24.pdf).
- **[Gille]** Philippe Gille, *Introduction to reductive group schemes over rings*, notes dated 9 May 2025. [Open author version](https://math.univ-lyon1.fr/~gille/prenotes/reductive.pdf). These treatments give the module-functor, equivariant-sheaf, representation and regular-cohomology constructions developed above.

# Odd-prime reduced powers and the Wu classes

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent AI review is recorded.*

Reduced powers recover characteristic classes from a Thom class. On a closed oriented manifold, the diagonal turns those bundle classes into expressions involving just the cohomology pairing and its operations. We construct the required operations from normalized chains, prove their identities and then prove the precise odd-prime Wu theorem. Six original graded exercises have complete solutions.

This continues [Multiplicative sequences and the signature theorem](multiplicative-sequences-and-the-signature-theorem.md); the section letters continue its A–F. Together the two chapters treat signatures, genera, reduced powers and Wu classes.

The exact proved prerequisites are [Thom and Euler classes](thom-classes-and-euler-classes.md) for singular chain products, excision, coefficient comparisons and the arbitrary-Hausdorff Thom theorem; [Grassmannians](grassmannians-and-classifying-maps.md) for classifying maps and compact CW subsets; [Frame fields](frame-fields-and-primary-obstructions.md), LemmaG.1, for cellular cohomology on arbitrary CW complexes; [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md), TheoremsB.4–B.5, for a CW model with its actual cohomology comparison; [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Sections1–4, for perfect field pairings and the signed diagonal; [Pontryagin classes](pontryagin-classes-and-oriented-universal-cohomology.md), Section5, for the universal ring at odd primes; and [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md), Lemma2.1, for integral stable symmetric polynomials.

## G. Normalized chains and a cyclic resolution

Fix an odd prime \(\ell=2r+1\), and put \(F=\mathbb F_\ell\). The degree increase of the reduced power \(P^i\) will be \(2i(\ell-1)=4ri\). We construct the operations and the properties used in the characteristic-class argument. Adem relations and Bockstein operations are not premises of that argument and are not asserted in this companion.

The singular chains, products, excision and coefficient comparisons used below have their full proofs in the [Thom/Euler chapter](thom-classes-and-euler-classes.md). The CW comparison needed later is [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md), Theorems B.4–B.5. We first supply the additional normalization and equivariant chain algebra.

### G.1. Removing degenerate simplices, with a chain homotopy

A simplicial module \(A\) has face maps \(d_i:A_n\to A_{n-1}\) and degeneracy maps \(s_i:A_n\to A_{n+1}\), induced by deleting and repeating a coordinate. Their identities follow by composing those coordinate maps. In particular,
\[
d_i s_j=\begin{cases}s_{j-1}d_i&i<j,\\1&i=j,j+1,\\s_jd_{i-1}&i>j+1,\end{cases}
\quad d_i d_j=d_{j-1}d_i\ (i<j),\quad
s_i s_j=s_{j+1}s_i\ (i\leq j).
\tag{G.1}
\]
The differential on its unnormalized complex is \(d=\sum_i(-1)^i d_i\). Define
\[
D_n=\sum_{i=0}^{n-1}s_i A_{n-1},\qquad
N_n=\bigcap_{i=0}^{n-1}\ker d_i,
\tag{G.2}
\]
with the empty intersection \(N_0=A_0\). The quotient by \(D\) is the normalized complex.

**Lemma G.1 — Normalization with its explicit comparison.** The quotient complex is naturally isomorphic to \(N\). Projection onto this summand is chain homotopic to the identity. Consequently normalized chains and cochains compute the singular theory, including relative groups and the cup product.

**Proof.** Write
\[
p_n^{(i)}=(1-s_{i-1}d_{i-1})\cdots(1-s_0d_0),\quad
0\leq i\leq n,\qquad p_n=p_n^{(n)}.
\tag{G.3}
\]
The empty product is the identity. Applying the factors in increasing index kills successive faces \(d_0,\ldots,d_{i-1}\). A later factor preserves previously killed faces by (G.1). Thus \(p_n A_n\subset N_n\); it acts as the identity on \(N_n\). Each difference from the original vector is degenerate.

For a vector \(s_j x\), the factors with index below \(j\) commute it past \(s_j\), using \(d_i s_j=s_{j-1}d_i\) and \(s_i s_{j-1}=s_j s_i\). The factor with index \(j\) then kills it since \(d_j s_j=1\). Hence \(p_nD_n=0\), and \(A_n=N_n\oplus D_n\). The two equal middle faces in \(d(s_jx)\) cancel, and every other face is degenerate by (G.1), so \(D\) is a subcomplex. On \(N_n\) the differential is \((-1)^n d_n\), which lies in \(N_{n-1}\) because \(d_i d_n=d_{n-1}d_i\) for \(i<n-1\). Both summands are therefore subcomplexes, and \(p\) is a chain map.

For completeness the required homotopy is
\[
h_n=\sum_{i=0}^{n}(-1)^i s_i p_n^{(i)},
\qquad d h+h d=1-p.
\tag{G.4}
\]
Here is the cancellation in that identity. In the expansion of \(d s_i p_n^{(i)}\), faces below \(i\) vanish since the corresponding faces of \(p_n^{(i)}x\) are zero. The two identity faces at \(i,i+1\) cancel each other. Faces above \(i+1\) commute through to \(s_i d_{j-1}p_n^{(i)}\) and cancel the corresponding terms of \(h_{n-1}d\). Moving the remaining face terms past each factor in (G.3) uses the same identities; the terms that do not cancel are
\[
\sum_{i=0}^{n-1}s_i d_i p_n^{(i)}
=\sum_{i=0}^{n-1}\bigl(p_n^{(i)}-p_n^{(i+1)}\bigr)
=1-p_n.
\]
The term with \(s_n p_n\) supplies the last upper-face cancellation. This proves (G.4), also in degree zero, where \(d s_0=0\). Every expression is natural and preserves a simplicial submodule, so the same homotopy works on its quotient and on cochains vanishing on it. Dualizing this actual homotopy proves the cohomology comparison without an unsupported dualization of a homology isomorphism.

For a space, take the free simplicial module on its singular simplices. A simplex in a subspace is a subset of the singular-simplex basis. A degenerate simplex's Alexander–Whitney cuts each have a degenerate factor: the cut lies either before or after the repeated vertices. Thus that diagonal descends to the normalized quotient. The quotient chain map preserves it, and its dual cohomology isomorphism preserves cup products. Relative cochains and their products are preserved by the same observation. ∎

For the standard simplicial \(j\)-simplex, normalized chains have basis the strictly increasing vertex lists in \(\{0,\ldots,j\}\). There are no chains in dimensions greater than \(j\). Prepending vertex zero, and interpreting a repeated zero as zero, is a contraction of its augmented complex: the first face gives the original list and all other faces cancel its application to the boundary. Thus it has homology \(F\) in degree zero and zero in positive degrees. The tensor product of finitely many such complexes has the same property, by tensoring their contractions. These are the actual acyclic models used below.

### G.2. The cyclic resolution and its diagonal

Let \(C_\ell=\langle g\rangle\), with \(g^\ell=1\), and let
\[
W_i=F[C_\ell]e_i\ (i\geq0),\quad
d e_{2j+1}=(g-1)e_{2j},\quad
d e_{2j}=N e_{2j-1}\ (j\geq1),\qquad
N=1+g+\cdots+g^{\ell-1}.
\tag{G.5}
\]
The augmentation sends \(g^a e_0\) to one. With \(T=g-1\), its group algebra is \(F[T]/(T^\ell)\), and \(N=T^{\ell-1}\). The last identity follows by dividing \((1+T)^\ell-1=T^\ell\) by \(T\) as a polynomial identity. Multiplication by \(T\) has kernel \((T^{\ell-1})\), and multiplication by \(T^{\ell-1}\) has kernel \((T)\). These are the respective images of the preceding maps, including the augmentation kernel. Thus \(W\) is a free resolution of the trivial module, with the exactness proved directly.

On a tensor of two copies of \(W\) use diagonal group action. Define an equivariant map by
\[
\Gamma(e_{2n+1})=\sum_{j+k=n}
\bigl(e_{2j}\otimes e_{2k+1}+e_{2j+1}\otimes g e_{2k}\bigr),
\tag{G.6}
\]
\[
\Gamma(e_{2n})=\sum_{j+k=n}e_{2j}\otimes e_{2k}
+\sum_{j+k=n-1}\sum_{0\leq a<b<\ell}
g^a e_{2j+1}\otimes g^b e_{2k+1}.
\tag{G.7}
\]
An empty sum is zero.

**Lemma G.2.** This is a chain map over the diagonal augmentation. After passing to trivial coefficients, its even-degree diagonal is
\[
e_{2n}\longmapsto\sum_{j+k=n}e_{2j}\otimes e_{2k}.
\tag{G.8}
\]

**Proof.** Put \(A=g\otimes1\), \(B=1\otimes g\), \(C=AB\), and \(S=\sum_{a<b}A^aB^b\). These operators commute and satisfy \(A^\ell=B^\ell=1\). Summing the geometric differences gives
\[
(A-1)S=N(C)-N(B),\qquad
(B-1)S=N(A)-B N(C),
\tag{G.9}
\]
and therefore \((C-1)S=N(A)-N(B)\). For example, the first sum telescopes for each fixed \(b\) from \(a=0\) to \(b-1\); the second telescopes for each fixed \(a\) from \(b=a+1\) to \(\ell-1\).

In the differential of (G.7), the even/odd terms have coefficient \(N(B)+(A-1)S=N(C)\); the odd/even terms have coefficient \(N(A)-(B-1)S=B N(C)\). These are exactly \(N(C)\Gamma(e_{2n-1})\), proving the even identity. In the differential of (G.6), the even/even coefficient is \((B-1)+(A-1)B=C-1\). The odd/odd coefficient is \(N(A)-N(B)=(C-1)S\). These are exactly \((C-1)\Gamma(e_{2n})\), proving the odd identity. This also includes all end terms and degree zero. It proves \(d\Gamma=\Gamma d\).

With trivial coefficients the differential in (G.5) is zero. The extra odd/odd coefficient in (G.7) becomes \(\ell(\ell-1)/2=0\) in \(F\), since \(\ell\) is odd. Hence the induced even diagonal is (G.8). ∎

This construction needs a chain diagonal; it makes no additional strict coassociativity assertion. Its formula, with the tensor differential's signs retained, will suffice for Cartan.

### G.3. The elementary equivariant comparison principle

We use twice the following principle. A positive free resolution of \(F\) can be mapped equivariantly to any other such resolution over the augmentation, and any two such maps are equivariantly chain homotopic. To prove it, choose a module basis in each degree. If the map is defined below degree \(i\), its prescribed differential at a basis vector in degree \(i\) is a cycle. Target exactness supplies a preimage, and equivariant extension defines that degree. For a homotopy, apply the same procedure to the cycle consisting of the difference of the two maps minus the homotopy already applied to the differential. In degree zero the augmentation makes this cycle an augmentation-kernel vector. This proves existence and uniqueness up to homotopy by induction.

For a finite group \(G\) an explicit free resolution is the homogeneous bar complex: its basis in degree \(n\) consists of tuples \((a_0,\ldots,a_n)\in G^{n+1}\), with differential the alternating deletion of entries and diagonal left action. That action is free on the tuple basis. Prepending the identity gives an ordinary contraction of the augmented complex, by the same deletion cancellation as for a simplex. In particular this supplies the full symmetric-group resolution used in the next section. Restricting it to \(C_\ell\subset\Sigma_\ell\) still gives a free resolution, by choosing coset representatives. No computation of symmetric-group homology is assumed.

## H. Higher diagonals and the reduced-power construction

Write \(C(K)\) for normalized chains of a simplicial set, first taking its free \(F\)-module in each degree. For a space use its singular simplicial set. We also normalize simplicial modules in the intermediate multilinear comparison (H.3). Its later diagonal is used only on the free module on a simplicial set, where sending each simplex to its repeated tensor defines a linear simplicial coalgebra map, and on the relative quotients that inherit this map. We assert no natural tensor diagonal on an arbitrary simplicial vector space. Permutations act on a tensor of chain complexes with the Koszul sign: interchanging degrees \(a,b\) contributes \((-1)^{ab}\). All group actions below retain that sign.

### H.1. An acyclic-model construction with its degree bound

**Lemma H.1 — Equivariant higher diagonal.** There is a natural equivariant chain map
\[
\mathcal D:W\otimes C(K)\longrightarrow C(K)^{\otimes\ell},
\tag{H.1}
\]
where the cyclic group acts trivially on \(K\) and permutes the target factors. At \(e_0\) it is the iterated Alexander–Whitney diagonal. It preserves subspaces, and
\[
\mathcal D(e_i\otimes C_j(K))=0\quad\text{if }i+j>\ell j.
\tag{H.2}
\]
It is naturally equivariantly homotopic to the restriction of a higher diagonal for the full symmetric-group bar resolution.

**Proof: the models and the induction.** First keep \(\ell\) independent simplicial modules \(K_1,\ldots,K_\ell\). Their degreewise tensor product is a simplicial module. We construct
\[
\Phi:W\otimes C(K_1\otimes\cdots\otimes K_\ell)
\longrightarrow W\otimes C(K_1)\otimes\cdots\otimes C(K_\ell).
\tag{H.3}
\]
On \(e_0\) take \(e_0\) tensored with the iterated Alexander–Whitney map. On degree-zero input take the identity on \(W\) and on the tensor of vertices. These prescriptions agree at their intersection and are chain maps there. Prescribe the values on group translates by equivariance, including the permutation of the independent modules.

Here is why the normalized domain causes no representability gap. The unnormalized degree-\(j\) input is \((K_1)_j\otimes\cdots\otimes(K_\ell)_j\). A tuple of simplices is represented by \(\ell\) separate free simplicial modules on the standard \(j\)-simplex. The projector (G.3) makes the normalized degree-\(j\) domain a natural direct summand of that functor. Any natural obstruction on that summand can first be extended to the representable functor by precomposing with the projector; after choosing a model filler, precomposing with the same projector gives a filler on the summand. Multilinearity in the \(\ell\) independent inputs follows because each model variable appears in just its own target factor. This procedure enforces degeneracy relations as well as linear relations.

Induct first in resolution degree \(i\), and then in input degree \(j\). For a free generator of \(W_i\) and \(j>0\), the already prescribed value of the differential is a cycle in total degree \(i+j-1\): applying its differential again gives zero by the induction hypotheses and \(d^2=0\). If \(i>0\), this degree is positive. On the universal models the target is \(W\) tensored with the normalized complexes of \(\ell\) standard simplices. Its positive homology is zero: each augmented simplex complex has the vertex contraction of G.1, and \(W\) has homology only \(F\) in degree zero. Hence the cycle has a filler. Choose it on a free resolution generator, carry it to arbitrary simplices by their representing maps and the projector just described, and extend by equivariance. At \(i=0\) the prescribed Alexander–Whitney map already gives every degree. This completes the induction and proves (H.3).

Every normalized model factor vanishes above dimension \(j\). Therefore the tensor-chain part of every filler in (H.3) has degree at most \(\ell j\). This is an actual bound on its construction, not an assumed property of an arbitrary higher diagonal.

Apply (H.3) to the iterated simplicial diagonal \(K\to K^{\otimes\ell}\), and then apply the augmentation of its output \(W\)-factor. This gives (H.1). Surviving terms have tensor degree \(i+j\); the preceding bound proves (H.2). Its value at \(e_0\) is the required diagonal. Naturality makes every simplex in a subspace produce factors in that same subspace.

**Proof: the symmetric comparison.** Repeat the construction with the symmetric-group bar resolution of G.3. The comparison principle there gives a cyclic-equivariant map from \(W\) to its restricted bar resolution, taking \(e_0\) to the identity-labelled vertex. The two higher diagonals agree in degree zero on vertices and at the augmentation. Their difference has a natural equivariant homotopy, constructed on the same independent models: at each step subtract the homotopy already applied to the differential, obtaining a cycle in positive target degree, and choose a filler. Precomposition with the normalization projector again respects the domain relations. The target tensor of simplex complexes has zero positive homology. Equivariant extension from resolution bases and natural extension from model simplices finish the induction. This proves the stated homotopy. ∎

The same homotopy induction shows that two choices in this construction give the same cohomology operations. There is no need to assume a preferred filler on every simplex.

### H.2. The dual convention, so that all signs are specified

It is convenient to regard cochains as a homological complex in negative degrees. Put
\[
K_{-q}=\operatorname{Hom}_F(C_q,F),\qquad
d_K a=(-1)^{q+1}a d_C\quad(a\in K_{-q}).
\tag{H.4}
\]
In \(W\otimes_{C_\ell}K^{\otimes\ell}\) our notation means coinvariants of the diagonal left action. Thus \(g e_i\otimes x=e_i\otimes g^{-1}x\). This fixes the inverse appearing in the chain correction below.
This is the graded dual convention. The usual singular cochain complex, whose differential is \(\delta a=a d_C\), maps isomorphically to (H.4) by
\[
a\longmapsto(-1)^{q(q+1)/2}a\quad\text{in degree }q.
\tag{H.5}
\]
The ratio of its consecutive signs is \((-1)^{q+1}\), proving that it commutes with differentials. In graded-dual evaluation, moving a cochain past an earlier chain contributes its Koszul sign. For two cochains of degrees \(q,t\), this makes the dual Alexander–Whitney product \((-1)^{qt}\) times the usual cochain product. The identity
\[
\frac{(-1)^{(q+t)(q+t+1)/2}}{(-1)^{q(q+1)/2}(-1)^{t(t+1)/2}}=(-1)^{qt}
\]
shows that (H.5) preserves products. We transfer all operations back by this explicit ring isomorphism. Thus the final characteristic-class formulas use the course's usual cup product and usual cohomological degrees.

Let \(\alpha:K^{\otimes\ell}\to(C^{\otimes\ell})^\vee\) be graded tensor evaluation. For \(|w|=i\) and homogeneous \(x\), define
\[
\Theta(w\otimes x)(c)=(-1)^{i|x|}
\alpha(x)\bigl(\mathcal D(w\otimes c)\bigr).
\tag{H.6}
\]
Its degree is \(i+|x|\). The graded tensor differential and the dual differential (H.4) show that \(\alpha\) commutes with differentials: differentiating the \(j\)-th evaluated factor supplies exactly the sign for moving that differential past the preceding factors. Here is the full remaining sign check. Put \(m=|x|\), and evaluate \(d\Theta(w\otimes x)\) on a chain \(c\) of degree \(1-i-m\). The dual differential makes its left side
\[
(-1)^{i+m+1+im}\alpha(x)\mathcal D(w\otimes dc).
\]
Use \(d\mathcal D(w\otimes c)=\mathcal D(dw\otimes c)+(-1)^i\mathcal D(w\otimes dc)\), and
\(\alpha(x)d=(-1)^{m+1}\alpha(dx)\).
The two resulting coefficients are \((-1)^{im+m}\) on
\(\alpha(x)\mathcal D(dw\otimes c)\) and \((-1)^{im}\) on
\(\alpha(dx)\mathcal D(w\otimes c)\). They are precisely
\(\Theta(dw\otimes x)(c)\) and \((-1)^i\Theta(w\otimes dx)(c)\), since
\((i-1)m\equiv im+m\) and \(i+i(m-1)=im\). This proves that
\(\Theta:W\otimes K^{\otimes\ell}\to K\) is a chain map. It is equivariant with trivial action on the target, since permuting a tensor and its evaluated dual tensor has cancelling Koszul signs. It therefore descends to coinvariants.

For a cocycle \(a\) of cohomological degree \(q\), the tensor \(a^{\otimes\ell}\) is cyclically fixed: its rotation sign is \((-1)^{(\ell-1)q^2}=1\). Thus every \(e_i\otimes a^{\otimes\ell}\) is a cycle in \(W\otimes_{C_\ell}K^{\otimes\ell}\); the \(g-1\) differential is zero, and the norm differential is multiplication by \(\ell=0\). Define
\[
D_i([a])=[\Theta(e_i\otimes a^{\otimes\ell})]
\in H^{\ell q-i}(K),\qquad D_i=0\text{ for }i<0.
\tag{H.7}
\]

### H.3. Why the class is independent of the representative

We give the tensor-homotopy argument needed in (H.7). Let \(I\) be the chain interval with vertices \(z_0,z_1\), edge \(z\), and \(dz=z_1-z_0\). For a positive free equivariant complex \(V\), there is an equivariant chain map
\[
I\otimes V\longrightarrow V\otimes I^{\otimes\ell}
\tag{H.8}
\]
equal to \(v\otimes z_b^{\otimes\ell}\) at vertex \(b\), with the tensor interchange signs understood. To construct its value on \(z\otimes v\), work in the kernel of the augmentation of \(I^{\otimes\ell}\). That kernel is contractible as an ordinary complex: the interval contracts to \(z_0\), and tensoring its contraction gives a contraction to \(z_0^{\otimes\ell}\). Tensoring with \(V\) preserves this contraction. The prescribed differential of \(z\otimes v\), minus the already chosen values on lower-resolution differentials, is consequently a boundary in that kernel. Fill it on a free basis for \(V\) and extend equivariantly. This inductively proves (H.8).

If \(a,b\) are homologous cocycles in \(K\), choose \(c\) with \(dc=b-a\). The map from the interval tensored with the one-dimensional complex concentrated in \(|a|\), taking its two vertices to \(a,b\) and its edge to \(c\), is a chain map. Tensor its \(\ell\) copies and compose with (H.8), for \(V=W\). The cyclic action on the shifted one-dimensional tensor is trivial because a cycle of odd length is an even permutation. In coinvariants, \(e_i\otimes1\) is a cycle. Applying the resulting interval homotopy to that cycle shows that
\(e_i\otimes a^{\otimes\ell}\) and \(e_i\otimes b^{\otimes\ell}\) differ by a boundary, with the same harmless interchange sign on both endpoints. Applying \(\Theta\) proves representative independence of (H.7).

For two cocycles of the same degree, the mixed terms in
\((a+b)^{\otimes\ell}-a^{\otimes\ell}-b^{\otimes\ell}\)
are a sum of norms of mixed words. Each binary word has a free cyclic orbit, since its prime length admits no nonconstant periodic word. The rotation signs on these equal-degree factors are positive. For a mixed-word cycle \(c\), \(e_i\otimes Nc\) is a boundary: if \(i\) is odd use \(e_{i+1}\otimes c\), and if \(i\) is even use \((g-1)^{\ell-2}e_{i+1}\otimes c\). Their differentials are the required norm, by \((g-1)^{\ell-1}=N\), including \(i=0\). Hence every \(D_i\) is additive. Scalar multiplication is linear because \(\lambda^\ell=\lambda\) in \(F\), proved by permuting the nonzero field elements in their product. Naturality follows from the natural construction and (H.6).

All arguments hold on relative cochains. The diagonal of a simplex in a subspace has every factor in that subspace; the constructions and homotopies preserve it. Equivalently, apply the normalized construction to the simplicial quotient module by that subspace. Its iterated diagonal is well defined because the submodule's iterated diagonal lies in its own tensor power. This proves the relative, natural and additive operations without a citation-only existence premise.

### H.4. The normalization of reduced powers

For any integer \(u\), put
\[
\nu(u)=(-1)^{r u(u-1)/2}(r!)^u\in F^\times,
\qquad
P^s x=(-1)^s\nu(-q)D_{(q-2s)(\ell-1)}x
\quad(x\in H^q).
\tag{H.9}
\]
Negative powers of \(r!\) mean its inverse in \(F\). The index convention makes this zero if \(2s>q\). Its degree is
\(q+2s(\ell-1)\). Transfer by (H.5) and the normalization isomorphism of G.1 identifies it with an operation on the usual singular cohomology of every pair.

Pairing every nonzero field element with its inverse shows \((\ell-1)!=-1\): only \(1,-1\) are self-inverse. Also
\((\ell-1)!=(-1)^r(r!)^2\), by pairing \(a\) with \(\ell-a\). Thus
\[
(r!)^2=(-1)^{r+1},\qquad
\nu(2j+\epsilon)=(-1)^j(r!)^\epsilon\quad(\epsilon=0,1).
\tag{H.10}
\]
These identities hold for negative \(j\) as well, by inversion. In particular, if \(q=2s\), the multiplier in (H.9) is one. Since \(\Theta(e_0,-)\) is the iterated product, this proves
\[
P^s x=x^\ell\quad\text{when }|x|=2s.
\tag{H.11}
\]
The remaining Cartan, suspension and identity properties are proved next; they are not inferred solely from this top-power normalization.

## I. Cartan, suspension and the identity operation

### I.1. The normalizer selects the nonzero even indices

We need the following restriction on (H.7):
\[
D_{2a}(x)=0\quad\text{unless }a\equiv rq\pmod{\ell-1},
\qquad x\in H^q.
\tag{I.1}
\]
Here is its proof, including the small group-theoretic calculation. The multiplicative group of \(F\) is cyclic. Indeed, for each prime dividing the order of any of its elements, select an element having the largest prime-power component occurring among those orders. Raise it to the complementary factor to obtain an element of just that prime-power order. Products of these elements have the product of their orders, since they commute and those orders are coprime. Call that order \(m\). Every group element has order dividing \(m\), so every nonzero field element is a root of \(X^m-1\). A polynomial has at most its degree many roots, by successive division by \(X-a\). Thus \(\ell-1\leq m\), while the subgroup of order \(m\) has at most \(\ell-1\) elements. Equality holds, proving cyclicity.

Choose a generator \(k\in F^\times\), represented by an integer between 1 and \(\ell-1\). Label the cyclically permuted coordinates by \(F\), and let \(h\) multiply their labels by \(k\). It fixes zero and cycles the \(\ell-1\) nonzero labels, so its permutation sign is \(-1\). Also \(hgh^{-1}=g^k\). A semilinear chain map on (G.5), over this automorphism, is
\[
h_\#(e_{2a})=k^a e_{2a},\qquad
h_\#(e_{2a+1})=k^a(1+g+\cdots+g^{k-1})e_{2a+1}.
\tag{I.2}
\]
The odd differential identity follows from
\((g-1)(1+\cdots+g^{k-1})=g^k-1\).
The even identity follows because multiplying a norm by that sum multiplies it by \(k\), while \(g\mapsto g^k\) fixes the norm. Thus (I.2) really commutes with differentials.

Map \(W\) into the symmetric-group bar resolution of H.1. The maps obtained by applying (I.2) before that comparison or by applying \(h\) after it are semilinearly chain homotopic: both lift the same augmentation, and the free-basis induction of G.3 works also with the prescribed automorphism in the equivariant extension. In symmetric-group coinvariants, acting by \(h\) on both the resolution and the tensor does not change the class. On \(x^{\otimes\ell}\) its Koszul sign is \((-1)^q\), because \(h\) is odd. The symmetric comparison of H.1 therefore gives
\[
D_{2a}(x)=(-1)^q k^a D_{2a}(x).
\tag{I.3}
\]
If this scalar differs from one, invert its nonzero difference in the field. The class is zero. Since \(k\) has order \(\ell-1=2r\), the scalar is one precisely for \(a\equiv rq\pmod{2r}\). This proves (I.1). We do not need the additional odd-index restriction for the argument below.

The degree bound (H.2) proves \(P^s=0\) also for \(s<0\). Its possible input-chain degree in (H.7) is \(n=\ell q-i=q+2s(\ell-1)\). If \(n<0\) there is no chain. Otherwise \(s<0\) makes \(n<q\), so the required tensor degree \(i+n=\ell q\) exceeds the allowed bound \(\ell n\). Its evaluation is zero. Thus negative operations are zero by a proved chain bound, while positive instability \(2s>q\) follows from the negative-index convention.

### I.2. The full product comparison

**Theorem I.1 — Cartan identity.** The natural additive operations (H.9) satisfy
\[
P^s(x\smile y)=\sum_{a+b=s}P^a x\smile P^b y.
\tag{I.4}
\]
The analogous external identity holds for pairs relative to
\(A\times Y\cup X\times B\) when \(A,B\) are open, and when either is empty with the other arbitrary. All the terms with negative operation indices are zero.

**Proof: the comparison on chains.** The Alexander–Whitney and shuffle product maps have their complete inverse homotopies in the Thom/Euler chapter. There are two natural equivariant maps from \(W\otimes C(K\otimes L)\) to \((C(K)\otimes C(L))^{\otimes\ell}\). One first takes the higher diagonal of \(K\otimes L\), then Alexander–Whitney in each output factor. The other first takes Alexander–Whitney on the input, uses \(\Gamma\) of G.2 on its resolution coordinate, takes the two higher diagonals, and shuffles their outputs into alternating factors.

These maps are naturally equivariantly chain homotopic. To construct the homotopy, keep all simplicial inputs separate, as in H.1. The universal targets are tensor products of normalized standard simplex complexes and have zero positive homology. At vertices the maps agree. At resolution degree zero the Alexander–Whitney product comparisons have the usual acyclic-model homotopy: the difference minus the homotopy on lower-degree faces is an augmentation-zero cycle, which is filled in that target. At each higher resolution degree, repeat exactly this filling induction on a free resolution basis and then on input degree. The normalization projector of G.1 extends each obstruction to the representable functor and restricts its filler back to the normalized summand. This proves the homotopy while retaining naturality, degeneracy relations and equivariance. Precomposing with simplicial diagonals and dualizing gives the same comparison for the products in (H.6).

**Proof: evaluation and constants.** For cocycles of degrees \(q,t\), their \(\ell\)-fold tensors are cyclically fixed. The induced even resolution diagonal is (G.8); the extra odd/odd sum has coefficient \(\ell(\ell-1)/2=0\). Shuffling \(\ell\) copies of \(x\otimes y\) into the two blocks makes \(\ell(\ell-1)/2\) exchanges of degrees \(q,t\), and has sign \((-1)^{rqt}\). The even resolution indices contribute no additional exchange sign. Thus the comparison gives
\[
D_{2n}(x\times y)=(-1)^{rqt}
\sum_{a+b=n}D_{2a}(x)\times D_{2b}(y).
\tag{I.5}
\]
By (I.1), a nonzero first index has \(2a=(q-2u)(\ell-1)\), and a nonzero second has \(2b=(t-2v)(\ell-1)\), for integers \(u,v\). If the left index is \(((q+t)-2s)(\ell-1)\), these integers satisfy \(u+v=s\). Negative ones contribute zero by the degree bound just proved.

From the exponent defining \(\nu\) one has
\[
\nu(-(q+t))=(-1)^{rqt}\nu(-q)\nu(-t).
\tag{I.6}
\]
Multiply (I.5) by \((-1)^s\nu(-(q+t))\), and use \(s=u+v\). The two signs \((-1)^{rqt}\) cancel, and every summand becomes \(P^u x\times P^v y\). This proves external Cartan with all constants specified. Pullback by the diagonal proves (I.4).

For relative external products, each construction and homotopy preserves simplices in either factor subspace. The small-chain comparison for the indicated union is the full open-cover relative product comparison already proved in the Thom/Euler chapter. It gives the asserted relative identity; when a factor subspace is empty no cover comparison is needed. Naturality along a diagonal gives the corresponding internal identity, including a relative class multiplied by an absolute class. ∎

### I.3. A chain correction that proves suspension

We prove compatibility with cohomology connecting maps rather than assuming it from the operation's name. It is clearer to perform the calculation in the homological grading of H.4, allowing any integer degree.

Let \(a\) have homological degree \(u\), and write \(b=da\). First do the following construction in the formal free two-generator complex with \(da=b\), and then substitute the actual \(a,b\). This convention includes \(b=0\), and does not pretend that two dependent vectors form a basis. On its tensor power define \(S=1^{\otimes(\ell-1)}\otimes s\), where \(s(b)=a\), \(s(a)=0\). The tensor sign gives
\(S(zb)=(-1)^{|z|}za\) and \(S(za)=0\). Consequently \(dS+Sd=1\): the differentials in the earlier factors cancel across this odd map, and the last factor has \(ds+sd=1\).

Put \(T'=g^{-1}-1\) on this tensor power, and define
\[
t_0=b^{\otimes\ell},\quad t_1=St_0,\quad
t_{2k}=S T't_{2k-1},\quad t_{2k+1}=S N t_{2k}
\quad(1\leq k\leq r).
\tag{I.7}
\]
Their differentials are
\[
dt_1=t_0,\quad dt_{2k}=T't_{2k-1},\quad
dt_{2k+1}=N t_{2k}.
\tag{I.8}
\]
Indeed the prescribed argument of \(S\) is a cycle: at the first step \(T't_0=0\); later use \(NT'=T'N=0\). The identity \(dS+Sd=1\) then proves (I.8) inductively.

The final tensor has the exact leading coefficient
\[
t_\ell=(-1)^{ru}r!\,a^{\otimes\ell}.
\tag{I.9}
\]
Here is a direct count proving that coefficient. Omitting tensor symbols between letters, induction in (I.7) gives
\[
t_{2k}=(-1)^{ku}(k-1)!
\sum_{i_1+\cdots+i_k=\ell-2k}
b^{i_1}a^2\cdots b^{i_k}a^2,
\tag{I.10}
\]
\[
t_{2k+1}=(-1)^{ku}k!
\sum_{i_1+\cdots+i_{k+1}=\ell-1-2k}
b^{i_1}a^2\cdots b^{i_k}a^2 b^{i_{k+1}}a.
\tag{I.11}
\]
All \(i_j\) are nonnegative. The base \(t_1=b^{\ell-1}a\) follows since \(\ell-1\) is even. For the even step, the identity part of \(T'\) is killed by \(S\), since every word ends in \(a\). The inverse rotation contributes only from words starting in \(b\). Removing that initial \(b\), rotating it to the end and applying \(S\) appends the new adjacent pair \(a^2\), bijectively giving the compositions in (I.10). The rotation sign is \((-1)^{u-1}\), since the rest has odd degree modulo two, and the final \(S\) sign is \(-1\); their product is \((-1)^u\).

For the odd step, after a norm rotation and \(S\), each output word has \(k\) paired \(a^2\)-blocks and one final \(a\). Restore its final letter to \(b\). There are exactly \(k\) choices of which paired block is to be the last block in the input word ending in \(a^2\); they give its \(k\) norm contributions, counted with multiplicity even if some intermediate exponents are zero. Moving a whole \(a^2\)-block has even degree and gives no sign. The signs from moving the initial \(b\)-letters and applying \(S\) cancel, so these contributions have the same sign. This multiplies \((k-1)!\) by \(k\), yielding (I.11). For \(k=r\), its exponents sum to zero, leaving just (I.9). This proves the coefficient for every odd prime, not by a finite numerical check.

For a homological operation index \(s\), put \(j=(2s-u+1)(\ell-1)\), which is even, and define in cyclic coinvariants
\[
c_s(a)=\sum_{k=0}^{r}(-1)^k e_{j-2k}\otimes t_{2k+1}
-\sum_{k=1}^{r}(-1)^k e_{j+1-2k}\otimes (T')^{\ell-2}t_{2k}.
\tag{I.12}
\]
Terms with negative resolution index are zero. Since \(ge\otimes z=e\otimes g^{-1}z\), the resolution differential becomes \(T'\) on the tensor, and \((T')^{\ell-1}=N\).

The full telescoping calculation gives
\[
dc_s(a)=e_j\otimes b^{\otimes\ell}.
\tag{I.13}
\]
To see every cancellation, the tensor differential of the \(k\)-th first sum, for \(k\geq1\), is \((-1)^k e_{j-2k}\otimes N t_{2k}\); this cancels the resolution differential of its \(k\)-th second-sum term. The tensor differential of that second-sum term has the extra minus from its odd resolution degree; it is \((-1)^k e_{j+1-2k}\otimes N t_{2k-1}\), cancelling the resolution differential of the first-sum term with index \(k-1\). The last possible residue is \((-1)^r e_{j-2r-1}\otimes Nt_\ell=0\), since the all-\(a\) tensor is cyclically fixed and \(\ell=0\). The \(k=0\) tensor differential is exactly the right side of (I.13). Negative-index terms and the zero differential at \(e_0\) fit these same cancellations.

Apply \(\Theta\) and set
\[
\mathscr P_s(a)=(-1)^s\nu(u-1)\Theta(c_s(a)).
\tag{I.14}
\]
If \(a\) is a cycle, (I.7)–(I.11) leave only \(t_\ell\), and (I.12) becomes
\((-1)^{r(u+1)}r!e_{(2s-u)(\ell-1)}\otimes a^{\otimes\ell}\).
The identity \(\nu(u)=(-1)^{r(u+1)}r!\nu(u-1)\), immediate from H.9, shows that (I.14) represents the normalized operation in that homological grading. Moreover (I.13) gives
\[
d\mathscr P_s(a)=\mathscr P_s(da).
\tag{I.15}
\]
The right side is the cocycle operation on \(b=da\). Every step is natural on chain maps commuting with \(\Theta\); the correction uses just \(a,da\), the cyclic action and fixed scalars.

**Theorem I.2 — Connecting maps and suspension.** On the cohomology of pairs, reduced powers commute with the connecting homomorphism. They consequently commute with the reduced suspension isomorphism.

**Proof.** Extend a cocycle \(x\) on a subspace to a cochain \(a\) on the whole space, using its subset of the singular-simplex basis. In the dual convention H.4 its differential \(b\) is a relative cocycle representing the corresponding connecting class. Naturality of (I.14) under restriction says that \(\mathscr P_{-s}(a)\) extends a representative of \(P^s x\). By (I.15), its differential represents \(P^s b\). This is exactly the defining connecting-cochain calculation, and proves compatibility in that convention. The isomorphism H.5 commutes with the maps of the short exact sequence of cochain complexes, hence with its connecting map; transferring back proves the assertion for the usual convention.

For the cone pair, its connecting map on reduced cohomology is an isomorphism by cone contraction and the pair sequence. Comparing the cone pair with the suspension quotient by its collar, using the full relative excision comparison from the Thom/Euler chapter, identifies this map with reduced suspension. Naturality and the pair result prove suspension compatibility. No transgression or Adem relation is required. ∎

### I.4. The degree-zero operation really is the identity

**Theorem I.3.** \(P^0x=x\) on the usual cohomology of spaces and pairs.

**Proof for spaces.** On degree-zero classes, \(P^0=D_0\) is the \(\ell\)-th power, hence the identity over \(F\). Suspension compatibility therefore proves the identity on the reduced generator of every sphere, by suspending the generator of \(S^0\) repeatedly.

For a CW complex and a positive degree \(q\), restriction to its \(q\)-skeleton is injective in \(H^q(-;F)\). Indeed the relative cellular complex for the cells above that skeleton is zero in degrees at most \(q\); the full cellular cohomology comparison in [Frame fields](frame-fields-and-primary-obstructions.md), LemmaG.1, gives the injection, including infinitely many cells. That lemma proves its integer and field versions by actual relative-chain comparisons and a stabilized skeleton tower. Every class on that \(q\)-skeleton is the reduction of an integral top cohomology class: lift the values of a cellular cochain on each \(q\)-cell to integers; there are no cells in degree \(q+1\), so this lift is a cocycle.

Such an integer cellular top class is pulled back from \(S^q\) by a map: send the \((q-1)\)-skeleton to the basepoint, and on each \(q\)-cell use a boundary-constant disk map of degree equal to that cell's chosen integer. One constructs a map of any integer degree by using that many disjoint interior disks, positively or negatively oriented, mapping each disk modulo its boundary once onto the sphere and collapsing their complement. The degree computation is the relative-cell generator calculation already proved in the Schubert chapter. CW weak topology makes the assembled map continuous, even with infinitely many cells. Its pullback cellular cocycle has precisely the prescribed values. Naturality and the sphere calculation prove \(P^0=1\) on the skeleton; injectivity proves it on the CW complex. For an arbitrary path-connected space, the complete CW-model and cohomology-comparison proof in homotopy Theorems B.4–B.5 transfers the result by naturality. Singular chains split over path components, so the conclusion holds for arbitrary spaces as well.

**The comparison needed for pairs.** We also describe why the same argument applies to a simplicial quotient, rather than inferring relative equality from a five-lemma isomorphism. A simplicial set's geometric realization is a CW complex with one open cell for each nondegenerate simplex. To verify this, first note the intersection identity: if \(s_i y=s_j z\) with \(i<j\), then \(y=s_{j-1}d_i z\), by applying \(d_i\), and the degeneracy identities give \(s_i y=s_j s_i d_i z\); applying \(d_j\) gives \(z=s_i d_i z\). Thus two different possible first degeneracies factor through their common double degeneracy. Induction using this identity, the injectivity of each \(s_i\) through its face section, and the identities ordering successive degeneracies proves the unique expression of any simplex as degeneracies of a nondegenerate one. Repeatedly removing a degeneracy terminates since dimension decreases. The simplicial identities put its degeneracies in increasing order, equivalently an order-preserving surjection of vertex sets. This expression is unique: the positions collapsed by that surjection are exactly the indices at which the simplex lies in the corresponding degeneracy image; applying their face sections recovers the residual simplex. Thus interiors of nondegenerate simplices are distinct, and the usual affine degeneracy identifications remove precisely the other interiors. Their faces attach in lower dimensions; finite faces give closure finiteness, and the quotient topology is the CW weak topology. Its cellular differential is the alternating face sum with a degenerate face contributing zero, exactly the normalized complex.

Send a simplex to its characteristic affine simplex in the realization. These maps form a simplicial map to its singular simplicial set: they respect both faces and the affine degeneracy identifications. On chains it induces the cellular-to-singular isomorphism, by the full relative-cell chain comparison in Frame fields, LemmaG.1, specialized to constant coefficients, and the skeleton homology proof in the Schubert chapter, Lemma2.1. These chain comparisons apply before dualization. More explicitly each skeleton's relative disk generator is sent to its singular relative generator; the pair sequences give the comparison in finite dimensions, and every singular cycle and bounding chain has compact image in a finite subcomplex, so passage to the union preserves it. The normalization comparison G.1 identifies these with normalized chains. The map is natural, hence it commutes with the operations constructed in H.1–H.9. The identity already proved on CW spaces therefore proves \(P^0=1\) for simplicial sets too.

For a nonempty simplicial subspace \(L\subset K\), its quotient simplicial set \(K/L\) collapses all of \(L\) to the single point simplex in every degree. Its reduced free simplicial module is exactly \(F[K]/F[L]\); the normalized dual is the relative cochain complex. The operations agree under this identification by their actual quotient diagonal construction. Thus the simplicial-set identity proves the pair identity. Taking \(K=\operatorname{Sing}X\), \(L=\operatorname{Sing}A\) proves it for every nonempty subspace \(A\); the empty case is the absolute result. ∎

We have now constructed every operation property needed below: naturality on pairs, additivity, \(F\)-linearity, \(P^0=1\), positive instability, the top \(\ell\)-th power, Cartan, and compatibility with relative connecting maps and suspension. Each has its own actual chain or cellular proof.

## J. Odd-prime Thom classes and Wu's formula

Continue to use \(F=\mathbb F_\ell\), \(\ell=2r+1\). Classes called Pontryagin classes below are reductions of the integral classes of the [Pontryagin chapter](pontryagin-classes-and-oriented-universal-cohomology.md). Every manifold in this section is smooth, Hausdorff and second countable.

### J.1. The classes defined by a Thom class

Let \(\xi\) be an oriented real rank-\(n\) vector bundle over a Hausdorff space \(B\). Write \(E_0\) for its total space with the zero section removed and \(u_\xi\in H^n(E,E_0;F)\) for the reduction of its oriented integral Thom class. The full arbitrary-Hausdorff Thom theorem in the [Thom/Euler chapter](thom-classes-and-euler-classes.md), Sections7–8, makes multiplication by this class an isomorphism. Define
\[
P^i(u_\xi)=\pi^*q_i(\xi)\smile u_\xi,\qquad
q_i(\xi)\in H^{4ri}(B;F),\qquad q(\xi)=\sum_{i\geq0}q_i(\xi).
\tag{J.1}
\]
The sum is finite: instability on the degree-\(n\) Thom class gives \(q_i=0\) when \(2i>n\). In rank zero its Thom pair is \((B,\varnothing)\), the Thom class is the unit and the same definition applies.

**Theorem J.1 — Thom-class rules.** These classes are natural, satisfy \(q_0=1\), and have the Whitney formula
\[
q(\xi\oplus\eta)=q(\xi)q(\eta).
\tag{J.2}
\]
For a trivial bundle \(q=1\); consequently \(q\) is stable under adding trivial bundles. Changing the orientation, even separately on open and closed components of the base, leaves these classes unchanged.

**Proof.** Naturality follows from naturality of the Thom class and the relative operations, and then Thom injectivity. The identity \(P^0u=u\) gives \(q_0=1\). Under the direct-sum Thom product isomorphism, the oriented product Thom class is the external product \(u_\xi\times u_\eta\). The relative product identity I.1 applies: the deleted-zero subspaces are open, and the union of their inverse images is precisely the complement of the simultaneous zero section. Pull it back over the base diagonal. Cartan and (J.1) now give the convolution of the \(q_i\)'s times the product Thom class. Moving any \(q_i\) past a Thom factor has sign one, since its degree \(4ri\) is even. Thom injectivity proves (J.2).

The Thom class of a trivial rank-\(n\) bundle is pulled back from the positive relative generator of \((\mathbb R^n,\mathbb R^n-\{0\})\). This pair has cohomology \(F\) only in degree \(n\), by the full sphere/pair calculation in the Thom chapter; its positive powers consequently vanish for degree reasons. Pullback proves \(q=1\) for the trivial bundle. Formula (J.2) proves stability.

On a component where the orientation is reversed, \(u\) changes to \(-u\). Linearity gives \(P^i(-u)=-P^i(u)\), and cancelling the new Thom generator in (J.1) leaves \(q_i\) unchanged. For a locally varying orientation choice its sign is a degree-zero class taking values \(1,-1\). Its positive powers vanish by instability and \(P^0\) fixes it; Cartan gives exactly the same cancellation. ∎

**Lemma J.2 — An oriented two-plane.** For an oriented rank-two bundle with Euler class \(e\),
\[
q(\xi)=1+e^{\ell-1}=1+p_1(\xi)^r.
\tag{J.3}
\]

**Proof.** Only \(q_0,q_1\) can survive instability. The top operation gives \(P^1u=u^\ell\). Relative multiplication is compatible with forgetting one factor to absolute cohomology; that image of \(u\) is \(\pi^*e\), by the Euler/zero-section calculation and the retraction of \(E\) onto \(B\). Thus \(u^2=\pi^*e\smile u\), and induction gives \(u^\ell=\pi^*e^{\ell-1}\smile u\). Thom injectivity proves the first equality. The integral oriented-plane identity \(p_1=e^2\), fully proved in the Pontryagin chapter, gives the second. ∎

### J.2. The precise polynomials in Pontryagin classes

Define integral polynomials \(Q_i\) by the symmetric-root identity
\[
\prod_{j=1}^m(1+z_j^r t)
 =\sum_{i\geq0}Q_i(e_1(z),e_2(z),\ldots)t^i .
\tag{J.4}
\]
Here \(Q_i\) has weight \(ri\) when \(e_j\) has weight \(j\). Existence, uniqueness and stability are the integral symmetric-polynomial theorem and the orbit-sum proof in [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md), Lemma2.1. Equivalently, the multiplicative sequence of the signature chapter for \(f(z)=1+z^r\) has \(K_{ri}=Q_i\) and all weights not divisible by \(r\) zero. No division modulo \(\ell\) is involved.

**Theorem J.3 — The odd-prime polynomial formula.** For every oriented real vector bundle over a Hausdorff base,
\[
q_i(\xi)=Q_i(p_1(\xi),p_2(\xi),\ldots)\quad\text{in }H^{4ri}(B;F).
\tag{J.5}
\]

**Proof on universal bundles.** The full universal-ring theorem in the Pontryagin chapter, Section5, gives
\[
H^*(BSO(2m+1);F)=F[p_1,\ldots,p_m].
\tag{J.6}
\]
This theorem includes odd-characteristic fields: two is invertible, and its proof identifies the actual odd-rank image through the antipodal action. It is not merely a rational rank calculation.

Classify the sum of \(m\) underlying real complex lines and one positive trivial line on \((\mathbb {CP}^\infty)^m\). If their first Chern classes are \(x_j\), its Pontryagin classes pull back to \(e_i(x_1^2,\ldots,x_m^2)\). The pullback of (J.6) is injective: the elementary symmetric functions in \(z_j=x_j^2\) are algebraically independent over \(F\), by the coefficientwise integral symmetric-polynomial proof, and the substitution \(z_j\mapsto x_j^2\) is injective on the polynomial ring since distinct monomials stay distinct. The target is that polynomial ring in the \(x_j\)'s, by the projective cellular and field product calculations already proved in the Schubert and Chern chapters.

Lemmas J.1–J.2 show that the same bundle has
\(q=\prod_j(1+x_j^{\ell-1})=\prod_j(1+(x_j^2)^r)\).
Identity (J.4) and the injectivity just proved identify its universal \(q_i\) with \(Q_i(p)\). This proves (J.5) on every odd-rank universal bundle. Stabilize an even-rank universal bundle by a positive line, classify that sum in odd rank, and use stability of both \(q\) and \(p\). The formula follows in even rank too.

**Proof for general bases, with its actual generality.** On a paracompact Hausdorff base the full classifying-map construction in [Grassmannians](grassmannians-and-classifying-maps.md), Theorem3.2, gives a map for the bundle. An orientation lifts it to the oriented Grassmannian: a local positive frame selects one of the two oriented planes continuously, and these selections agree on overlaps. Pullback of the universal formula proves (J.5) on this base.

For a general Hausdorff \(B\), test the difference of the two sides against an arbitrary singular homology cycle over \(F\). Its finitely many singular simplices have compact image \(C\subset B\); this is compact Hausdorff, hence paracompact by the proved compact-space partition theorem. The restricted bundle satisfies the formula just established. Its evaluation on that cycle is therefore zero. The field cochain/homology comparison in the Thom chapter is an isomorphism \(H^k(B;F)\cong\operatorname{Hom}_F(H_k(B;F),F)\): split cycles and boundaries in a vector-space chain complex. All zero evaluations force the difference to be zero. This proves the stated Hausdorff generality without assuming an unproved classifying map on a nonparacompact base. ∎

When \(\ell=3\), \(r=1\) and (J.4) gives \(Q_i=p_i\). When \(\ell=5\), \(r=2\); its first formulas are
\[
q_1=p_1^2-2p_2,\qquad
q_2=p_2^2-2p_1p_3+2p_4.
\tag{J.7}
\]
Indeed, if \(E(t)=\prod_j(1+z_jt)=\sum_j p_jt^j\), then
\(E(t)E(-t)=\prod_j(1-z_j^2t^2)\).
Comparing its coefficient in degree \(2i\) gives the full formula
\[
Q_i=\sum_{a+b=2i}(-1)^{i+b}p_a p_b
\quad(r=2),\qquad p_0=1.
\tag{J.8}
\]
Thus the odd-prime result is a statement about these specified polynomial combinations; it is not a claim that every individual Pontryagin class is a homotopy invariant modulo every odd prime.

### J.3. Wu classes and the tangent formula, including the signs

Let \(M^d\) be closed and oriented, with coefficients \(F\). Its finite-dimensional cohomology has a perfect Poincaré pairing by the [manifold chapter](manifold-duality-the-diagonal-and-wu-classes.md). Define \(v_i\in H^{4ri}(M;F)\) uniquely by
\[
\langle v_i\smile x,[M]\rangle
 =\langle P^i x,[M]\rangle,\qquad
x\in H^{d-4ri}(M;F).
\tag{J.9}
\]
For degrees beyond \(d\) set \(v_i=0\). The identity operation gives \(v_0=1\). Instability makes
\[
v_i=0\quad\text{if }2\ell i>d:
\tag{J.10}
\]
in that range \(2i>d-4ri\), so the right-hand functional is zero. Put \(v=\sum_i v_i\).

**Theorem J.4 — Odd-prime Wu formula.**
\[
q(TM)=P(v),\qquad
Q_k(p(TM))=\sum_{a+b=k}P^a(v_b).
\tag{J.11}
\]
The total operation \(P=\sum_aP^a\) is interpreted in the finite-dimensional cohomology of \(M\).

**Proof.** The diagonal's normal bundle is \(TM\) through \(w\mapsto(-w,w)\), with the tangent-first/normal-second orientation checked by the positive determinant \(2^d\) in the manifold chapter. On its tube let \(u\) be its oriented relative Thom class, and let \(U\in H^d(M\times M;F)\) be the diagonal class. Formula (J.1), naturality, tubular excision and forgetting relative cohomology give
\[
P(U)=(q(TM)\times1)\smile U.
\tag{J.12}
\]
Both projections on the tube agree with its base map up to the tube retraction. Consequently there is no separate unproved normal-versus-tangent identification in this formula.

Choose the homogeneous cup-dual bases of manifold Theorem4.1, so
\(\langle b_\alpha b_\beta^\vee,[M]\rangle=\delta_{\alpha\beta}\).
That theorem proves the signed formula and the slant convention
\[
U=\sum_\alpha(-1)^{|b_\alpha|}b_\alpha\times b_\alpha^\vee,\qquad
(a\times b)/[M]=a\langle b,[M]\rangle,\qquad U/[M]=1.
\tag{J.13}
\]
Left linearity of slant in (J.12) gives \(P(U)/[M]=q(TM)\).

For a second-factor evaluation \(\langle P^j b_\alpha^\vee,[M]\rangle\) to be nonzero, its degree forces \(|b_\alpha|=4rj\). These degrees are even. Thus every term of (J.13) surviving after applying Cartan and slant has its coefficient sign equal to \(+1\). Definition (J.9) says exactly that
\[
v=\sum_\alpha b_\alpha
       \langle P(b_\alpha^\vee),[M]\rangle.
\tag{J.14}
\]
To verify the coefficient, multiply by any \(b_\beta^\vee\), evaluate, and use cup duality; in degree \(4rj\) the functional is precisely that of (J.9). Additivity, scalar linearity and external Cartan therefore give
\[
P(v)=\sum_\alpha P(b_\alpha)
       \langle P(b_\alpha^\vee),[M]\rangle
     =P(U)/[M]=q(TM).
\]
Terms of other basis degrees evaluate to zero, as just checked. Taking degree \(4rk\) and using Theorem J.3 proves the component formula. All sums are finite; neither an Adem relation nor a Bockstein calculation is required. ∎

**Corollary J.5 — The homotopy invariants.** If \(f:M\to N\) is a homotopy equivalence of closed oriented \(d\)-manifolds, then
\[
f^*v_i(N)=v_i(M),\qquad f^*q_i(TN)=q_i(TM).
\tag{J.15}
\]
There is no orientation-preservation hypothesis on \(f\). In particular every individual \(p_i(TM)\) modulo \(3\) is a homotopy invariant.

**Proof.** On a connected component \(f_*[M]=\epsilon[N]\), where \(\epsilon=1\) or \(-1\): integral top homology is generated by its fundamental class and a homotopy equivalence induces an isomorphism. Naturality of \(P^i\) and products shows, for \(x\in H^{d-4ri}(N;F)\), that
\[
\langle f^*v_i(N)\smile f^*x,[M]\rangle
 =\epsilon\langle v_i(N)\smile x,[N]\rangle
 =\epsilon\langle P^ix,[N]\rangle
 =\langle P^i(f^*x),[M]\rangle.
\]
Surjectivity of \(f^*\) and the perfect pairing identify this class with \(v_i(M)\). Apply \(P\) and (J.11) to obtain the second equality. A homotopy equivalence permutes components, so this proof applies with its separate signs to every component. Compact manifolds have finitely many components. In dimension zero use the canonical tangent orientation; the only possible class is \(v_0=q_0=1\). Finally \(r=1\) makes \(q_i=p_i\), proving the modulo-three assertion. ∎

### J.4. A projective calculation of both sides

Let \(x\in H^2(\mathbb {CP}^m;F)\) be the positive hyperplane generator; \(\langle x^m,[\mathbb {CP}^m]\rangle=1\). The proved stable tangent identity is \(T\mathbb {CP}^m\oplus\mathbb C\cong(m+1)H\), where \(H\) is the hyperplane line. Its underlying real Thom classes and (J.3) give
\[
q(T\mathbb {CP}^m)=(1+x^{\ell-1})^{m+1}.
\tag{J.16}
\]
Instability and the top power give \(P(x)=x+x^\ell\). Cartan then proves, for every \(a\geq0\),
\[
P^j(x^a)=\binom aj x^{a+(\ell-1)j}.
\tag{J.17}
\]
This equality includes \(a=0\) and \(j>a\), with the usual zero binomial convention.

The class dual in (J.9) to a potential \(v_j\) is \(x^{m-(\ell-1)j}\). Hence
\[
v_j=\binom{m-(\ell-1)j}{j}\,x^{(\ell-1)j},
\quad 0\leq j\leq \left\lfloor\frac m\ell\right\rfloor,
\tag{J.18}
\]
and all remaining \(v_j\) are zero by (J.10). The stated range makes the upper binomial entry nonnegative; it avoids using a formal negative binomial coefficient as an actual manifold pairing. Equations (J.16)–(J.18) give explicit instances of the tangent formula with all coefficient reductions understood in \(F\).

### J.5. Prime-local coefficients and the inverse operation

The integral polynomials \(Q_i\) describe the Thom classes. The individual manifold Wu classes also have formulas through rational \(L\), Â and Todd polynomials. Their factors of the prime must be applied before reducing coefficients.

Write \(\mathbb Z_{(p)}\) for the rational numbers whose reduced denominator is prime to the prime \(p\). Define the Todd polynomials by
\[
\prod_j\frac{x_jt}{1-e^{-x_jt}}
 =\sum_{n\geq0}T_n(c_1,c_2,\ldots)t^n,
\qquad c_i=e_i(x_1,x_2,\ldots).
\]
[The signature chapter](multiplicative-sequences-and-the-signature-theorem.md), Theorem D.1, gives unique stable rational polynomials of weight \(n\), with \(c_i\) of weight \(i\). The first ones are \(T_0=1\), \(T_1=c_1/2\), \(T_2=(c_1^2+c_2)/12\), and \(T_3=c_1c_2/24\).

**Prime-local coefficient lemma.** Every coefficient of \(T_n\) has \(p\)-adic valuation at least \(-\lfloor n/(p-1)\rfloor\). In particular \(p^iT_{(p-1)i}\) has coefficients in \(\mathbb Z_{(p)}\). Put
\[
z_p(x)=\sum_{k\geq0}(-1)^k x^{p^k},\qquad
F_p(x)=\frac{x}{z_p(x)}=1+z_p(x)^{p-1}
\quad\text{in }\mathbb F_p[[x]].
\tag{J.19}
\]
The quotient means the reciprocal of the unit series \(z_p(x)/x\). Only powers divisible by \(p-1\) occur in \(F_p\). The coefficient of root degree \((p-1)i\) in \(\prod_jF_p(x_j)\), expressed in elementary variables, equals \(p^iT_{(p-1)i}(c)\bmod p\).

**Proof.** Use the finite free ring
\[
S=\mathbb Z_{(p)}[\pi]/(\pi^{p-1}-p).
\]
Division by the monic relation gives the basis \(1,\pi,\ldots,\pi^{p-2}\). The same basis embeds it in \(\mathbb Q[\pi]/(\pi^{p-1}-p)\), where \(\pi\) is invertible. Also \(S/(\pi)=\mathbb F_p\). For \(p=2\), \(S=\mathbb Z_{(2)}\) and \(\pi=2\). If \(n=(p-1)m+j\), \(0\leq j<p-1\), then for rational \(a\)
\[
a\pi^n\in S\quad\Longleftrightarrow\quad
ap^m\in\mathbb Z_{(p)},
\]
because the only nonzero basis coefficient is \(ap^m\) in position \(j\).

Count the factors of \(p\) in \(k!\):
\[
e_p(k!)=\sum_{a\geq1}\left\lfloor k/p^a\right\rfloor
        =\frac{k-s_p(k)}{p-1}.
\]
The first equality counts a factor for each multiple of each \(p^a\). Substituting the base-\(p\) expansion of \(k\) and summing its finite geometric sums gives the second; \(s_p(k)\) is its digit sum. Hence \(e_p(k!)\leq(k-1)/(p-1)\), with equality exactly when \(k\) is a power of \(p\).

It follows that
\[
G(\pi x)=\frac{1-e^{-\pi x}}{\pi x}
       =\sum_{n\geq0}\frac{(-1)^n\pi^n}{(n+1)!}x^n
\]
belongs to \(S[[x]]\). Indeed, writing \((n+1)!=p^eu\) with \(u\) a unit in \(\mathbb Z_{(p)}\), its coefficient is \((-1)^n\pi^{n-(p-1)e}/u\), with nonnegative exponent. It reduces to zero modulo \(\pi\) unless \(n+1=p^k\).

The unit part of \((p^k)!\) is \((-1)^k\bmod p\). Separate its multiples of \(p\), whose unit product is that of \((p^{k-1})!\), from its \(p^{k-1}\) blocks of nonmultiples. Each block has product \((p-1)!=-1\bmod p\), by the inverse pairing of H.4. For odd \(p\) each step therefore changes the sign; for \(p=2\) the same equality holds in \(\mathbb F_2\). Starting with \(1!\) proves the claim. Thus
\[
G(\pi x)\bmod\pi=\sum_{k\geq0}(-1)^k x^{p^k-1}=z_p(x)/x.
\]
Its constant term is one, so reciprocal recursion in \(S[[x]]\) proves
\[
\frac{\pi x}{1-e^{-\pi x}}\bmod\pi=F_p(x).
\]
The identity \(z_p+z_p^p=x\) proves (J.19). Its powers are multiples of \(p-1\), since this is true of \(z_p/x\).

Now form the root product. The coefficientwise symmetric-polynomial theorem over \(S\) expresses its weight-\(n\) coefficient as \(\pi^nT_n(c)\) with coefficients in \(S\). The basis criterion above gives the asserted rational bound. When \(n=(p-1)i\), \(\pi^n=p^i\) is rational; its reduction modulo \(\pi\) is reduction modulo \(p\) in \(\mathbb Z_{(p)}\). Adjoining zero roots proves stability. ∎

For odd \(p=\ell\), the even root series for the signature and Â-polynomials are
\[
f_L(x)=\frac{x}{\tanh x},\qquad
f_{\widehat A}(x)=\frac{x}{2\sinh(x/2)}.
\]
Write \(f_T(x)=x/(1-e^{-x})\). Direct formal identities give
\[
f_L(x)=f_T(2x)-x,\qquad f_{\widehat A}(x)=e^{-x/2}f_T(x).
\]
The series \(e^{-\pi x/2}\) belongs to \(S[[x]]\) and reduces to one: in positive degree \(n\), the exponent remaining in \(\pi^n/n!\) is \(s_p(n)>0\), and two is a unit. Moreover \(\pi x\) reduces to zero and \(F_p(2x)=F_p(x)\), since its exponents are multiples of \(p-1\) and \(2^{p-1}=1\bmod p\). Both scaled even series therefore reduce to \(F_p(x)\). Their weight-\(j\) polynomials in \(p_i=e_i(x_1^2,x_2^2,\ldots)\) have root degree \(2j\). Applying the symmetric-polynomial theorem in squared roots proves
\[
\ell^iL_{ri},\ \ell^i\widehat A_{ri}
 \in\mathbb Z_{(\ell)}[p_1,p_2,\ldots],\qquad
\ell^iL_{ri}\equiv\ell^i\widehat A_{ri}\pmod\ell,
\quad r=(\ell-1)/2.
\tag{J.20}
\]
These are coefficient statements, made before characteristic classes are substituted.

### J.6. Individual Wu classes in L-, Â- and Todd-polynomial coordinates

**The rational-coordinate Wu formulas.** On every closed oriented smooth manifold, the classes of (J.9) satisfy
\[
v_i=\ell^iL_{ri}(p(TM))
   =\ell^i\widehat A_{ri}(p(TM))\pmod\ell.
\tag{J.21}
\]
If \(TM\) is stably complex, with the Chern classes of that stable complex structure, then
\[
v_i=\ell^iT_{(\ell-1)i}(c(TM))\pmod\ell.
\tag{J.22}
\]
An integrable complex structure is not required.

**Proof.** In the bounded graded cohomology of a closed manifold, \(P=1+R\) is a ring automorphism. Every term of \(R\) raises degree, so \(R^{d+1}=0\), and its linear inverse is \(\sum_{j=0}^d(-R)^j\). The inverse of a bijective ring homomorphism also preserves products. Theorem J.4 therefore determines \(v=P^{-1}(q(TM))\) uniquely.

For an oriented two-plane's degree-two Euler root \(x\), the operation properties give \(P(x)=x+x^\ell\); J.2 gives \(q=1+x^{\ell-1}\). Consecutive terms of the defining series cancel to give
\[
z_\ell(x)+z_\ell(x)^\ell=x,\qquad
z_\ell(x+x^\ell)=x.
\]
Thus \(z_\ell\) is the compositional inverse of \(x+x^\ell\), and
\[
F_\ell(x+x^\ell)=1+x^{\ell-1}.
\tag{J.23}
\]
For sums of two-planes, Cartan sends \(\prod_jF_\ell(x_j)\) to \(\prod_j(1+x_j^{\ell-1})=q\). The universal splitting injection established in J.3 proves the equality on every oriented bundle in each finite degree. The coefficient identifications (J.20), followed by uniqueness of \(P^{-1}q\) on \(M\), prove (J.21). For a complex bundle use the full flag splitting and its injective cohomology pullback from [the Chern chapter](chern-classes-and-the-integral-universal-ring.md); the prime-local lemma identifies the same root product with the right side of (J.22). Trivial real or complex summands add only zero roots. This proves the stable complex assertion. All series terminate when evaluated on \(M\). ∎

At the prime two, write \(V^j\) for the usual Wu class defined by
\[
\langle V^j x,[M]_2\rangle=\langle Sq^j x,[M]_2\rangle.
\]
On every closed smooth manifold, without an orientability hypothesis,
\[
V^j=2^jT_j(w_1(TM),w_2(TM),\ldots)\pmod2.
\tag{J.24}
\]
For oriented \(M\), \(V^{2j+1}=0\). If \(TM\) is stably complex, then
\[
V^{2j+1}=0,\qquad V^{2j}=2^jT_j(c(TM))\pmod2.
\tag{J.25}
\]

**Proof.** [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Theorem 5.1, proves \(w(TM)=Sq(V)\). The total square is a ring automorphism in bounded dimension for the same degree argument. For a real line root \(x\) of degree one, \(Sq(x)=x+x^2\). The lemma at \(p=2\) and (J.23) give \(Sq(F_2(x))=1+x\). The full real splitting injection in [the Gysin chapter](gysin-sequence-and-projective-splitting.md) identifies \(\sum_j2^jT_j(w)\) with the inverse square of \(w\), proving (J.24).

To check the odd components, \(h(x)=e^{-x/2}f_T(x)=x/(2\sinh(x/2))\) is even, and
\[
\prod_i f_T(x_i)=e^{c_1/2}\prod_i h(x_i).
\]
Each odd-weight coefficient of the second product vanishes. An odd-weight coefficient of the whole product therefore contains a positive odd power of \(c_1\), and is divisible by \(c_1\) over \(\mathbb Q[c]\). Since \(2^{2j+1}T_{2j+1}\) already has coefficients in \(\mathbb Z_{(2)}\), its quotient by the polynomial variable \(c_1\) has coefficients there as well. Substitute \(c_1=w_1=0\) to obtain the orientable assertion.

For a complex line root \(x\) of degree two, \(Sq(x)=x+x^2\). The identity and top square give these terms. On the universal line over \(\mathbb {CP}^\infty\), degree-three cohomology vanishes by the projective cell calculation, so \(Sq^1x=0\). Naturality under the line classifying map proves this after splitting. The complex flag pullback is injective over \(\mathbb F_2\), and the underlying real bundle has \(w=c\bmod2\) in even degrees and no odd classes, by the full line and splitting proof of the Chern chapter. Hence \(\prod_iF_2(x_i)\) is \(Sq^{-1}w\); it lies in even degrees and its degree-\(2j\) coefficient is \(2^jT_j(c)\bmod2\). This proves (J.25), including stable trivial summands. ∎

For example, at \(\ell=3\),
\[
v_1=p_1,\qquad v_2=(7p_2-p_1^2)/5\pmod3,
\]
while \(q_i=p_i\). On \(\mathbb {CP}^4\), \(p_1=5x^2\), \(p_2=10x^4\); thus \(v_1=2x^2\), \(v_2=0\), as in K.5. At \(\ell=5\), \(v_1=(7p_2-p_1^2)/9=p_1^2+3p_2\bmod5\); on \(\mathbb {CP}^{10}\) this is \(x^4\), agreeing with K.6. Every inverted denominator is prime to the coefficient prime.

### J.7. Symmetric coordinates and exact denominators

Two coordinates for Todd polynomials, studied by Buchstaber and Veselov in *Todd polynomials and Hirzebruch numbers*, expose their denominators. Here is an algebraic proof.

Let \(m_\lambda\) denote a stable monomial symmetric function, and let \(e_j,h_j\) be elementary and complete symmetric functions. Work in the stable ring first; in weight \(n\), at least \(n\) root variables suffice to detect its coefficients. We impose no finite-rank relation while applying \(\omega\). Their generating functions obey \(E(-t)H(t)=1\). Since the \(e_j\) are polynomial generators, \(\omega(e_j)=h_j\) defines an integer algebra homomorphism. Applying it to the reciprocal identity gives \(\omega(H(t))=E(t)\); hence \(\omega^2=1\). The forgotten functions \(f_\lambda=\omega(m_\lambda)\) form an integer basis in each weight, since the orbit monomials do and \(\omega\) is an integer automorphism.

The universal product identity gives
\[
\prod_{i,j}(1+x_i y_j)=\sum_\lambda m_\lambda(x)e_\lambda(y).
\]
Apply \(\omega\) in the \(x\) variables, sending each \(E_x(y_j)\) to \(H_x(y_j)\):
\[
\prod_{i,j}(1-x_i y_j)^{-1}
 =\sum_\lambda f_\lambda(x)e_\lambda(y).
\tag{J.27}
\]
All expressions are considered in finite weight, so stable root lists cause no infinite summation issue. Specialize the polynomial generators \(e_j(y)\) to \(1/(j+1)!\). Then
\[
H_y(t)=\left(\sum_{j\geq0}\frac{(-t)^j}{(j+1)!}\right)^{-1}
      =\frac{t}{1-e^{-t}}.
\]
The left side of (J.27) becomes the Todd root product. Its weight-\(n\) coefficient proves
\[
T_n=\sum_{|\lambda|=n}
       \frac{f_\lambda}{\prod_j(\lambda_j+1)!}.
\tag{J.28}
\]
The exact common denominator is the least common multiple of these factorial products, because the \(f_\lambda\) form an integer basis; both changes of basis to elementary monomials are integer matrices. For example,
\[
T_3=\frac{m_{(2,1)}+3m_{(1,1,1)}}{24}
   =\frac{c_1c_2}{24}.
\]

To obtain factorial-free coordinates take independent formal coefficients in
\[
A(t)=t+\sum_{n\geq1}a_nt^{n+1},\qquad
B(t)=A^{-1}(t)=t+\sum_{n\geq1}b_nt^{n+1}.
\]
Successive coefficient comparison in \(A(B(t))=t\) gives \(b_n=-a_n\) plus an integer polynomial in lower \(a_i\), homogeneous of weight \(n\) when \(a_i\) has weight \(i\). Thus
\[
b_\lambda=\sum_{|\mu|=|\lambda|}C^\lambda_\mu a_\mu,
\qquad C^\lambda_\mu\in\mathbb Z.
\]
Every non-diagonal term refines at least one part of \(\lambda\) into smaller parts. Order partitions by a linear extension of refinement. The matrix is triangular with diagonal \((-1)^{\operatorname{length}(\lambda)}\); triangular recursion gives an integer inverse. It follows that \(g_\mu=\sum_\lambda C^\lambda_\mu f_\lambda\) is another integer basis. Specializing \(A(t)=-\log(1-t)\), \(B(t)=1-e^{-t}\) gives \(a_n=1/(n+1)\), \(b_n=(-1)^n/(n+1)!\), and (J.28) becomes
\[
T_n=(-1)^n\sum_{|\mu|=n}
       \frac{g_\mu}{\prod_j(\mu_j+1)}.
\tag{J.29}
\]
Hence the least common multiple of these products equals that of the factorial products. At weight two, \(b_1=-a_1\), \(b_2=-a_2+2a_1^2\); consequently \(g_{(1,1)}=f_{(1,1)}+2f_{(2)}\), \(g_{(2)}=-f_{(2)}\), and \(T_2=g_{(1,1)}/4+g_{(2)}/3\). The coordinates require no complex-bordism classification premise.

**Exact Todd denominator.** The least positive integer clearing every coefficient of \(T_n(c_1,\ldots,c_n)\) is
\[
d_n=\prod_{p\ \mathrm{prime}}p^{\lfloor n/(p-1)\rfloor}.
\tag{J.26}
\]
Only primes at most \(n+1\) contribute; \(d_0=1\). Its first six positive values are \(2,12,24,720,1440,60480\).

**Arithmetic proof.** For \(k\geq1\), if \(p^e\mid(k+1)\), then \(k\geq p^e-1\geq e(p-1)\). Thus the \(p\)-exponent of any product \(\prod_j(\lambda_j+1)\), \(|\lambda|=n\), is at most \(\lfloor n/(p-1)\rfloor\). A partition with that many copies of \(p-1\), and its remainder in parts smaller than \(p-1\), attains the bound. Formula (J.29)'s integer basis proves (J.26).

**A geometric sharpness check.** The stable tangent formula gives the Todd number of \(\mathbb {CP}^a\) as \([x^a]f_T(x)^{a+1}\). The formal residue change of variable in signature Lemma E.1, with \(u=1-e^{-x}=x+O(x^2)\), \(dx=du/(1-u)\), gives
\[
[x^a]f_T(x)^{a+1}
 =\operatorname{res}_{u=0}\frac{du}{u^{a+1}(1-u)}=1.
\]
This includes \(a=0\), and multiplicativity gives one for every product of projective spaces. Fix \(p\), let \(m=\lfloor n/(p-1)\rfloor>0\), and write \(n=m(p-1)+a\), \(0\leq a<p-1\). On
\[
X=(\mathbb {CP}^{p-1})^m\times\mathbb {CP}^a
\]
the first \(m\) tangent Chern products are \(c=(1+x)^p\), truncated by \(x^p=0\). Every positive coefficient is divisible by \(p\): for \(0<j<p\), \(j\binom pj=p\binom{p-1}{j-1}\) and \(j\) is prime to \(p\). In the total product, a term using a positive power in any of these factors carries a factor \(p\) for each such factor. A top-degree monomial Chern number uses all \(m\), and is therefore divisible by \(p^m\), including when one term uses several factors. If every coefficient of \(T_n\) had denominator \(p\)-exponent at most \(m-1\), its value on \(X\) would lie in \(p\mathbb Z_{(p)}\). The value is one, a contradiction. This independently checks sharpness against the prime-local bound. ∎

**Exact L denominator.** For \(L_n\) it is
\[
\prod_{p\ \mathrm{prime},\ p\geq3}p^{\lfloor2n/(p-1)\rfloor}
 =\operatorname{lcm}_{|\lambda|=n}\prod_j(2\lambda_j+1).
\tag{J.30}
\]

**Proof.** At an odd prime the scaled even-series proof in J.5 bounds every coefficient denominator by the stated exponent. At two, the coefficient lemma gives \(f_T(2x)\in\mathbb Z_{(2)}[[x]]\); hence \(f_L(x)=f_T(2x)-x\) belongs to this ring. It is even, so the symmetric-polynomial theorem in squared roots places all \(L_n\) coefficients in \(\mathbb Z_{(2)}\).

For sharpness at odd \(p\), take \(X=(\mathbb {CP}^{p-1})^m\times\mathbb {CP}^a\), with \(m=\lfloor2n/(p-1)\rfloor\) and \(a=2n-m(p-1)\). Both \(p-1\) and \(a\) are even. Every factor has signature one, so the signature theorem and multiplicativity give \(\langle L_n(TX),[X]\rangle=1\). The first \(m\) factors have \(p=(1+x^2)^p\), truncated by dimension; every positive coefficient is divisible by \(p\). The same top-degree expansion makes every Pontryagin number divisible by \(p^m\). A smaller coefficient denominator exponent would contradict the value one.

Finally, if \(p^e\mid(2k+1)\), then \(2k\geq p^e-1\geq e(p-1)\). Every product \(\prod_j(2\lambda_j+1)\) therefore has \(p\)-exponent at most \(\lfloor2n/(p-1)\rfloor\). A partition containing that many copies of \((p-1)/2\), with the remaining weight in smaller parts, attains it. All products are odd. This proves the least-common-multiple formula, including \(n=0\) with empty product one. ∎

### J.8. Operations and the Gysin map of an arbitrary closed-manifold map

The tangent formula also controls maps between manifolds, without requiring that the map preserve orientation or be an embedding. Let \(f:Y^d\to X^e\) be any continuous map between closed oriented smooth manifolds and use \(\mathbb F_\ell\) coefficients. Define
\[
f_!:H^a(Y;F)\longrightarrow H^{a+e-d}(X;F)
\]
by the perfect-pairing identity
\[
\langle b\smile f_!a,[X]\rangle
 =\langle f^*b\smile a,[Y]\rangle.
\tag{J.31}
\]
Negative-degree groups are zero. Each fundamental class is the sum of the oriented component classes; the definition therefore includes disconnected or empty manifolds. The same definition works over \(\mathbb F_2\), with no orientations. Perfect duality proves existence and uniqueness degree by degree, the projection formula
\(f_!(f^*b\smile a)=b\smile f_!a\), homotopy invariance of \(f_!\), and \((g f)_!=g_!f_!\): evaluate each assertion against an arbitrary complementary class and use (J.31).

Put \(Q_Y=q(TY)\) and \(Q_X=q(TX)\). These total classes have constant term one, so are units in the bounded cohomology rings. Then
\[
P(f_!a)=Q_X\smile f_!\bigl(P(a)\smile Q_Y^{-1}\bigr).
\tag{J.32}
\]
Over \(\mathbb F_2\), replace \(P,Q_Y,Q_X\) by \(Sq,w(TY),w(TX)\). All expressions mean finite sums after evaluating on the manifolds. In particular, the correction factor here is the inverse tangent Thom class \(Q_Y^{-1}\); the usual Wu class in (J.9) is instead \(P^{-1}(Q_Y)\).

**Proof.** First consider a smooth closed embedding \(i:Y\hookrightarrow Z\), with normal bundle \(\nu\). Orient its normal by tangent followed by normal equal to the ambient orientation. The tubular and local Thom-cap proofs in [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Section 4, identify \(i_!a\) with the absolute image of \(\pi^*a\smile U_\nu\). Indeed, subdivision for the tube/complement cover kills the complement terms, and the positive normal Thom evaluation leaves the tangent fundamental cycle. Evaluating the remaining cocycle \(i^*b\smile a\) gives precisely (J.31), also for \(a\) of positive degree. Over \(\mathbb F_2\) the same local argument needs no orientation.

Naturality on the tube pair and relative Cartan now give
\[
P(i_!a)=i_!\bigl(P(a)\smile q(\nu)\bigr).
\tag{J.33}
\]
This is the full relative Thom multiplication calculation, not an interchange of an operation with integration. The square version follows from the proved Thom definition of \(w(\nu)\). There are no odd-prime commutation signs because every component of \(q\) and every degree increase of \(P\) is even; signs vanish over \(\mathbb F_2\).

For projection \(p:X\times S^N\to X\), choose positive even \(N\). Let \(u\in H^N(S^N;F)\) evaluate to one. The field Künneth theorem writes every class uniquely as \(p^*a+p^*b\smile u\); definition (J.31) gives \(p_!(p^*a)=0\) and \(p_!(p^*b\smile u)=b\). Since \(P(u)=u\) by the identity operation and dimension, and \(P(1)=1\), Cartan proves \(P p_!=p_!P\). The same argument proves \(Sq p_!=p_!Sq\). The stable tangent identity \(TS^N\oplus\varepsilon^1=\varepsilon^{N+1}\) gives \(q(T(X\times S^N))=p^*Q_X\), and similarly for \(w\).

Every continuous \(f\) is homotopic to a smooth map \(f_0\). Here this approximation follows directly from earlier proved constructions: embed compact \(X\) in Euclidean space and take a smooth tubular retraction. A sufficiently fine finite cover of \(Y\), with a smooth partition of unity, gives a smooth weighted average of the Euclidean vectors \(f(y_j)\), uniformly close to \(f\). Compactness gives a positive tube radius. Both that average and its straight interpolation with \(f\) lie in the tube, so the retraction supplies \(f_0\) and the homotopy. The Euclidean embedding is proved in [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Lemma 3.3, and the smooth partitions in [Vector bundles](vector-bundles-and-their-constructions.md).

Embed \(Y\) smoothly in \(\mathbb R^N\), enlarging to positive even \(N\), and regard that embedding \(j\) as lying in the punctured sphere \(S^N\). The graph
\[
i=(f_0,j):Y\hookrightarrow X\times S^N
\]
is a smooth closed embedding: \(j\) is injective with injective derivative, and compactness gives a closed image and the embedding topology. Also \(p i=f_0\). Its tangent-normal identity and stability imply
\[
q(TY)\,q(\nu)=i^*q(T(X\times S^N))=f_0^*Q_X,
\]
and likewise \(w(TY)w(\nu)=f_0^*w(TX)\) modulo two. Thus \(q(\nu)=f_0^*Q_X\,Q_Y^{-1}\). Apply (J.33), commute the operation with \(p_!\), use functoriality and the projection formula, and obtain (J.32). Homotopy invariance gives the statement for \(f\). ∎

For the map to a point, (J.32) becomes
\[
\langle P(a)\smile q(TY)^{-1},[Y]\rangle
 =\langle a,[Y]\rangle.
\]
This explains the inverse-class correction in the general Gysin formula. It is compatible with the diagonal proof of (J.11), which identifies the usual Wu class by the different functional \(\langle P(a),[Y]\rangle\).


## K. Exercises with complete solutions

**Exercise K.1 — Easy: two stages of the cyclic resolution.** In \(F[C_\ell]\), find the kernels and images of multiplication by \(g-1\) and by \(N\). Compute \(\Gamma(e_2)\), and explain why its odd/odd part disappears on trivial coefficients.

**Solution.** Put \(T=g-1\). The algebra is \(F[T]/T^\ell\), with basis \(1,T,\ldots,T^{\ell-1}\), and \(N=T^{\ell-1}\). Multiplication by \(T\) has image \((T)\) and kernel \(F T^{\ell-1}\). Multiplication by \(N\) has image \(F T^{\ell-1}\) and kernel \((T)\). These identities prove exactness at both repeating stages; the augmentation kernel is \((T)\). Formula (G.7) gives
\[
\Gamma(e_2)=e_0\otimes e_2+e_2\otimes e_0
 +\sum_{0\leq a<b<\ell}g^a e_1\otimes g^b e_1.
\]
With trivial coefficients each translated term becomes \(e_1\otimes e_1\). There are \(\ell(\ell-1)/2\) terms; their coefficient is zero in \(F\). The two even terms remain.

**Exercise K.2 — Easy: a power of a projective class.** For the positive class \(x\) on \(\mathbb {CP}^\infty\), compute \(P^2(x^3)\) at primes \(3\) and \(5\). Decide whether each class survives on \(\mathbb {CP}^8\).

**Solution.** Cartan and \(P(x)=x+x^\ell\) give
\(P^2(x^3)=\binom32x^{3+2(\ell-1)}\).
Modulo \(3\) its coefficient is zero, so the operation is zero already on the infinite space. Modulo \(5\) it is \(3x^{11}\), nonzero on the infinite space, because its polynomial generator has no relation. On \(\mathbb {CP}^8\), \(x^{11}=0\) by dimension, so this operation also vanishes there. A zero coefficient and a truncated target degree are two different calculations.

**Exercise K.3 — Medium: the first three polynomials at prime five.** Derive \(Q_1,Q_2,Q_3\) integrally for \(r=2\), and then reduce them modulo \(5\). Explain why the proof does not use the division of a Newton identity by its index.

**Solution.** Compare coefficients in
\[
\Bigl(\sum_{a\geq0}p_at^a\Bigr)
\Bigl(\sum_{b\geq0}(-1)^bp_bt^b\Bigr)
=\sum_{i\geq0}(-1)^iQ_it^{2i}.
\]
This gives
\[
Q_1=p_1^2-2p_2,\quad
Q_2=p_2^2-2p_1p_3+2p_4,\quad
Q_3=p_3^2-2p_2p_4+2p_1p_5-2p_6.
\]
These are integer polynomial identities, with \(p_0=1\), so their coefficients may be reduced directly modulo \(5\). Each paired off-diagonal term appears twice and the central term once; this accounts for every coefficient and sign. There is no division, including when the weight or an index is divisible by \(5\).

**Exercise K.4 — Medium: orientation and a two-plane on a projective space.** Let the complex line \(H^{\otimes a}\) on \(\mathbb {CP}^m\) have first Chern class \(ax\), where \(a\) is an integer and negative exponents mean powers of the dual line. For its oriented underlying real bundle compute \(q\), including the case \(\ell\mid a\), and the effect of reversing its real orientation.

**Solution.** The full Chern line rules give \(e=ax\). Lemma J.2 gives
\[
q=1+a^{\ell-1}x^{\ell-1}.
\]
If \(a=0\) in \(F\), this is \(1\). If \(a\ne0\), multiplication by \(a\) permutes all nonzero field elements; comparison of their nonzero product gives \(a^{\ell-1}=1\). Hence \(q=1+x^{\ell-1}\), with its positive term zero if \(\ell-1>m\). Reversing the real orientation sends \(e\) to \(-e\), whose even power \(e^{\ell-1}\) is unchanged. The same invariance follows directly by linearity and cancellation of the reversed Thom class in (J.1).

**Exercise K.5 — Hard: both sides of Wu on \(\mathbb {CP}^4\) at prime three.** Compute \(v\) directly from its defining pairing. Apply the reduced powers, compare with \(q(T\mathbb {CP}^4)\), and give the individual Pontryagin classes modulo \(3\).

**Solution.** Here \(r=1\), \(d=8\), and the bound \(2\ell j\leq d\) leaves only \(j=0,1\). The dual test for \(v_1=cx^2\) is \(x^2\). Formula (J.17) gives \(P^1(x^2)=2x^4\); its evaluation is \(2\), hence \(v=1+2x^2\). The operations on that term are \(P^0(2x^2)=2x^2\), \(P^1(2x^2)=4x^4=x^4\), and \(P^2(2x^2)=2x^6=0\) on this space. Thus
\[
P(v)=1+2x^2+x^4.
\]
Independently, (J.16) gives
\((1+x^2)^5=1+5x^2+10x^4=1+2x^2+x^4\)
after truncation and reduction modulo \(3\). Since \(r=1\), \(q_i=p_i\). Therefore \(p_1=2x^2\), \(p_2=x^4\) and all remaining positive classes vanish by dimension. This computes the pairing, the operation and the tangent polynomial separately.

**Exercise K.6 — Hard: a cancellation at prime five, and the information retained.** Compute \(v\) and \(P(v)\) on \(\mathbb {CP}^{10}\) at prime \(5\). Verify the result from its tangent Pontryagin classes and (J.7). Finally show algebraically that all the \(Q_i\)'s at this prime need not determine all the \(p_i\)'s; state the limit of this last observation.

**Solution.** Now \(r=2\), \(d=20\), so \(j\leq2\). Formula (J.18) gives
\[
v_1=\binom61x^4=x^4,\qquad
v_2=\binom22x^8=x^8,\qquad v=1+x^4+x^8.
\]
By Cartan, \(P^1(x^4)=4x^8\). All other positive contributions from \(x^4\) or \(x^8\) have exponent at least \(12\) and vanish on \(\mathbb {CP}^{10}\). Consequently
\[
P(v)=1+x^4+(4+1)x^8=1+x^4.
\]
The stable tangent formula gives \(p=(1+x^2)^{11}\). Modulo \(5\), its first four coefficients are \(11=1\), \(55=0\), \(165=0\), \(330=0\). Hence (J.7) yields \(q_1=x^4\), \(q_2=0\); higher \(q_i\)'s are beyond dimension. This agrees with \((1+x^4)^{11}=1+x^4\) after truncation.

For the algebraic observation work in \(F[z]\). The two formal root lists \((z)\) and \((-z)\) have distinct first elementary functions \(z,-z\), since \(2z\ne0\). Their complete sequences are nevertheless both \(Q(t)=1+z^2t\); every higher \(Q_i\) is zero. Thus recovering every elementary Pontryagin variable from just these polynomial combinations is impossible in general. This is a formal algebra example explaining why Theorem J.4 alone does not imply homotopy invariance of every individual \(p_i\) modulo \(5\). It does not assert that these two formal lists are tangent bundles of homotopy-equivalent manifolds.

## Sources and scope

J. Peter May, *A general algebraic approach to Steenrod operations*, [author-hosted text](https://math.uchicago.edu/~may/PAPERS/10.pdf), develops the equivariant algebraic construction of reduced powers, including the identity operation \(P^0=1\). Allen Hatcher, *Algebraic Topology*, [corrected author edition](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), treats the operation properties and a geometric construction. John Milnor, *Lectures on Characteristic Classes*, [Spring1957 notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf), relates the Thom construction to Pontryagin polynomials and homotopy invariance.

Friedrich Hirzebruch, *On Steenrod's Reduced Powers, the Index of Inertia, and the Todd Genus*, [1953 primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063884/), states the rational-coordinate Wu formulas. Michael F. Atiyah and Friedrich Hirzebruch, *Cohomologie-Operationen und charakteristische Klassen*, [1961 primary paper](https://hirzebruch.mpim-bonn.mpg.de/155/1/31_Cohomologie-Operationen%20und%20charakteristische%20Klassen.pdf), supplies their prime-local coefficient and inverse-operation arguments, including the Â-polynomial expression. Victor M. Buchstaber and Alexander P. Veselov, *Todd polynomials and Hirzebruch numbers*, [November2023 version](https://arxiv.org/html/2310.07383v2), develops the forgotten-function and factorial-free coordinates and the exact denominators. The operations are due to Norman Steenrod; the manifold Wu construction is due to Wen-Tsün Wu, with the diagonal method also developed by René Thom.

The AI authored the exposition, full chain and characteristic-class arguments, symmetric-function derivations, examples and six solved exercises, and performed the recorded mathematical self-checks.

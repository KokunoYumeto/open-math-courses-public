# Steenrod squares and Stiefel–Whitney classes

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Independently authored text dedicated under CC0.*

The Thom class records the local generator in every fibre. Cohomology operations measure how that class behaves under squaring, and the Thom isomorphism transfers the answer to the base. This gives all the Stiefel–Whitney classes at once. Their product formula follows from a product formula for the operations themselves.

Our prerequisites are [Thom classes and Euler classes](thom-classes-and-euler-classes.md), especially its full singular-chain, product, coefficient and Thom proofs; [The Gysin sequence and projective splitting](gysin-sequence-and-projective-splitting.md), Sections 3–5; and the compact embedding and classification proofs in [Vector bundles and their constructions](vector-bundles-and-their-constructions.md) and [Grassmannians and classifying maps](grassmannians-and-classifying-maps.md). We construct the operations used here rather than taking their existence or their Cartan identity as an additional prerequisite. All coefficients in this chapter are \(\mathbf F_2\), unless another ring is explicitly displayed.

## 1. Higher diagonals on singular chains

Let \(C_*(X)\) be the unnormalized singular chain complex over \(\mathbf F_2\). Its boundary is the sum of its face maps; all signs disappear. For a singular \(m\)-simplex \(\sigma\) and a subset \(A\subset\{0,\ldots,m\}\), write \(d_A\sigma\) for the face retaining precisely the vertices outside \(A\), in their original order. Deleting all vertices gives zero in our unaugmented complex. This notation concerns faces, not arbitrary vertex permutations.

For \(0\leq i\leq m\), let \(U=\{u_1<\cdots<u_{m-i}\}\) range over the subsets of size \(m-i\). Divide its vertices into

\[
U^0=\{u_j:u_j+j\equiv0\pmod2\},\qquad
U^1=\{u_j:u_j+j\equiv1\pmod2\}.
\]

The position \(j\) starts at one, while vertex numbers start at zero. Define a higher diagonal by

\[
D_i\sigma=\sum_{|U|=m-i}d_{U^0}\sigma\otimes d_{U^1}\sigma.
\]

Set \(D_i\sigma=0\) for \(i<0\) or \(i>m\). Its output has total degree \(m+i\). Let \(T(c\otimes d)=d\otimes c\); over this field it is the chain interchange without signs. Each term uses faces of the same original simplex. The formula is consequently natural for continuous maps and preserves chains in every subspace.

**Lemma 1.1 (higher-diagonal identity).** For every \(i\geq0\),

\[
\partial D_i+D_i\partial=(1+T)D_{i-1}.
\]

Also \(D_0\) is the Alexander–Whitney diagonal, and \(D_m\sigma=\sigma\otimes\sigma\).

The degrees provide a useful check on the identity. On an \(m\)-chain, both \(\partial D_i\) and \(D_i\partial\) have total degree \(m+i-1\), as does \(D_{i-1}\). The diagonal index therefore stays \(i\) in the boundary term \(D_i\partial\).

**Proof of the two normalizations.** For \(i=m\), the deletion set is empty, so there is exactly the asserted term. For \(i=0\), each deletion set misses one vertex \(k\). A vertex below \(k\) has position one larger than its vertex number, and belongs to \(U^1\); a vertex above \(k\) has position equal to its vertex number, and belongs to \(U^0\). The corresponding term is therefore
\(\sigma[0,\ldots,k]\otimes\sigma[k,\ldots,m]\).
Summing over \(k\) gives the Alexander–Whitney formula.

**Proof of the identity.** First assume \(0\leq i\leq m\). A term of \(\partial D_i\sigma\) deletes one more vertex \(v\) from one of the two surviving faces. There are two types.

If \(v\in U\), it had already been deleted from the other face. The output now deletes \(v\) from both faces. This term occurs once in \(D_i\partial\sigma\): first delete \(v\) from the input and then use the tuple \(U\setminus\{v\}\). To check the colouring, vertices below \(v\) keep both their vertex number and tuple position, and vertices above \(v\) lose one from both. Thus \(u_j+j\) has the same parity after this change. These terms cancel in pairs. The correspondence is reversible: the common deleted vertex specifies the input boundary face, and all other deleted vertices specify its tuple.

If \(v\notin U\), put \(W=U\cup\{v\}=\{w_1<\cdots<w_q\}\), where \(q=m-i+1\), and suppose \(v=w_k\). Put \(p_l=w_l+l\pmod2\). In the output term, vertices before position \(k\) are coloured \(p_l\), and vertices after it are coloured \(1-p_l\), because their positions in \(U\) are one less than in \(W\). The inserted vertex can be deleted in either factor, so its colour is either \(\epsilon=0\) or \(\epsilon=1\). Denote the resulting tensor face by \(C_{k,\epsilon}\).

For \(1\leq k<q\), the two colour assignments

\[
C_{k,p_k}=C_{k+1,1-p_{k+1}}
\]

are identical: both colour positions through \(k\) by \(p_l\) and the later positions by \(1-p_l\). They cancel. Each middle position has one choice paired with the preceding position and its other choice paired with the next. The two unpaired end choices are \(C_{1,1-p_1}\), which colours all vertices by \(1-p_l\), and \(C_{q,p_q}\), which colours all by \(p_l\). Thus the contribution for each \(W\) is exactly its term in \(T D_{i-1}\sigma+D_{i-1}\sigma\).

For \(i=0\), \(W\) consists of all \(m+1\) vertices. Its colours \(w_l+l\) are all one, so each remaining end term deletes all vertices in one factor and is zero. This agrees with \(D_{-1}=0\). Terms creating an empty face have throughout been interpreted as zero, as required for the unaugmented boundary.

For \(i=m+1\), both left-hand terms are zero and the right-hand side is
\((1+T)(\sigma\otimes\sigma)=0\). For larger \(i\), every term vanishes. This proves the identity in all dimensions, including dimension zero. \(\square\)

The index rule is the mathematical higher-diagonal formula of [MM, Definition 7]. The argument above is an independently written all-dimensional cancellation proof. In particular, vertex parity alone would give the wrong formula: the tuple position is essential.

## 2. Squares as well-defined cohomology operations

For cochains \(a,b\) of degrees \(p,q\), define

\[
a\smile_i b=(a\otimes b)D_i\in C^{p+q-i}(X),\qquad i\geq0,
\]

and set \(\smile_i=0\) for \(i<0\). Degrees below zero contain only zero cochains. The operation is bilinear. The case \(i=0\) is the ordinary cup product, and dualizing Lemma 1.1 gives

\[
\delta(a\smile_i b)=
\delta a\smile_i b+a\smile_i\delta b+
a\smile_{i-1}b+b\smile_{i-1}a.
\tag{2.1}
\]

For a degree-\(n\) cocycle \(a\) and \(0\leq s\leq n\), set

\[
\operatorname{Sq}^s[a]=[a\smile_{n-s}a]\in H^{n+s}(X).
\]

For \(s>n\) set it to zero; negative indices are also zero. These are the **Steenrod squares** used in this course.

**Theorem 2.1.** These formulas define additive natural operations on singular cohomology, with

\[
\operatorname{Sq}^0x=x,\qquad
\operatorname{Sq}^{n}x=x^2\quad(x\in H^n),\qquad
\operatorname{Sq}^{s}x=0\quad(s>n).
\]

The same statements hold on \(H^*(X,A)\) for every subspace \(A\subset X\).

**Proof.** For a cocycle \(a\), (2.1) makes \(a\smile_i a\) a cocycle: its remaining two terms are equal. If \(a,b\) are cocycles of the same degree, the mixed terms in the square of \(a+b\) are

\[
a\smile_i b+b\smile_i a=\delta(a\smile_{i+1}b).
\]

This proves additivity in cohomology. For independence of representative, replace \(a\) by \(a+\delta c\), with \(|c|=n-1\). By (2.1) the difference of their squares is the differential of

\[
c\smile_i a+a\smile_i c+
c\smile_i\delta c+c\smile_{i-1}c.
\tag{2.2}
\]

Indeed the first two differentials give
\(\delta c\smile_i a+a\smile_i\delta c\), because their lower-index mixed terms cancel. The third contributes
\(\delta c\smile_i\delta c+c\smile_{i-1}\delta c+
\delta c\smile_{i-1}c\); the fourth cancels those last two terms. This includes \(i=0\) under the zero negative-index convention. For \(n=0\) there are no nonzero coboundaries to check.

Naturality follows directly from the natural face formulas. On an \(n\)-simplex, \(D_n\sigma=\sigma\otimes\sigma\), so
\((a\smile_n a)(\sigma)=a(\sigma)^2=a(\sigma)\) in \(\mathbf F_2\). This proves the identity square. The top square is the ordinary cup square, and instability is our zero-index convention.

For a relative cochain, every face of a simplex in \(A\) is still in \(A\). The formulas therefore preserve cochains vanishing on \(A\); so do all the primitives just displayed, when the cochains involved are relative. The same proof gives the operations and their properties on every pair. \(\square\)

Equation (2.1) is also a concrete explanation for cup-product commutativity: for cocycles, the difference of \(a\smile b\) and \(b\smile a\) is the differential of \(a\smile_1b\). The operations carry more information than the ordinary product because their output degree depends on how far the higher diagonal is taken.

## 3. The Cartan identity, with its chain comparison

**Theorem 3.1 (Cartan identity).** For cohomology classes \(x,y\),

\[
\operatorname{Sq}^{s}(x\smile y)=
\sum_{r+t=s}\operatorname{Sq}^{r}x\smile\operatorname{Sq}^{t}y.
\tag{3.1}
\]

For external products the corresponding formula is

\[
\operatorname{Sq}^{s}(x\times y)=
\sum_{r+t=s}\operatorname{Sq}^{r}x\times\operatorname{Sq}^{t}y.
\tag{3.2}
\]

It holds for \(x\in H^*(X,A)\), \(y\in H^*(Y,B)\), with target relative to \(A\times Y\cup X\times B\), whenever \(A,B\) are open. If one subspace is empty, the other can be arbitrary. Pulling back along a diagonal gives the relative internal formula under the corresponding union hypotheses.

**Proof: a resolution and its diagonal.** Write \(\tau\) for the nonidentity element of the two-element group, and let \(W\) be the nonnegative chain complex with

\[
W_i=\mathbf F_2[\tau]e_i,\qquad
\partial e_i=(1+\tau)e_{i-1}\quad(i>0).
\]

Its augmentation sends both \(e_0\) and \(\tau e_0\) to one. In each positive degree, multiplication by \(1+\tau\) has both kernel and image the line spanned by \(1+\tau\). This also equals the kernel of the augmentation in degree zero. Thus this is a free resolution of the trivial module, with no assumed group-homology theorem.

Lemma 1.1 says exactly that

\[
\mathcal D_X:W\otimes C_*(X)\longrightarrow C_*(X)\otimes C_*(X),
\qquad \mathcal D_X(e_i\otimes c)=D_i c,
\]

is an equivariant chain map when \(\tau\) acts trivially on \(C_*(X)\) and exchanges the two target factors. Its value on \(\tau e_i\otimes c\) is \(T D_i c\). Here and below tensor complexes have the ordinary total degree. All differentials add without signs over \(\mathbf F_2\).

Define an equivariant resolution diagonal, with diagonal group action on its target, by

\[
\Gamma(e_i)=\sum_{j=0}^{i}e_j\otimes\tau^j e_{i-j}.
\tag{3.3}
\]

It is a chain map. To verify this in degree \(i>0\), put \(k+l=i-1\). The differential from the first factor, after reindexing \(j=k+1\), is the sum of
\(e_k\otimes\tau^{k+1}e_l+\tau e_k\otimes\tau^{k+1}e_l\).
The differential from the second is the sum of
\(e_k\otimes\tau^k e_l+e_k\otimes\tau^{k+1}e_l\).
The repeated terms cancel, leaving
\(\sum_{k+l=i-1}(e_k\otimes\tau^k e_l+\tau e_k\otimes\tau^{k+1}e_l)\).
This is \((1+\tau)\Gamma(e_{i-1})=\Gamma(\partial e_i)\). Its degree-zero augmentation is also the diagonal augmentation.

**Proof: the two product maps are homotopic.** Let
\(A:C_*(X\times Y)\to C_*(X)\otimes C_*(Y)\)
be the Alexander–Whitney product map proved in the Thom/Euler chapter, Lemma 4.1. Form two natural equivariant chain maps with common target

\[
K(X,Y)=C_*(X)\otimes C_*(X)\otimes C_*(Y)\otimes C_*(Y).
\]

The first map \(F\) applies \(\mathcal D_{X\times Y}\), then \(A\) to each of the two product-space factors, and finally rearranges the factors into the order \(X,X,Y,Y\). The second map \(G\) first applies \(\Gamma\otimes A\), rearranges into
\((W\otimes C_*(X))\otimes(W\otimes C_*(Y))\), and then applies \(\mathcal D_X\otimes\mathcal D_Y\). The target group action simultaneously exchanges the two \(X\) factors and the two \(Y\) factors. All component maps are equivariant chain maps, so both composites are too. They agree on degree-zero augmentation.

We construct their natural equivariant chain homotopy, rather than asserting a comparison theorem. Order generators \(e_i\otimes\sigma_m\) by total degree \(i+m\). Suppose the homotopy \(H\) has been defined in all lower total degrees and satisfies the required identity there. For this generator use the universal simplex
\(\sigma_m^\Delta:\Delta^m\to\Delta^m\times\Delta^m\), \(z\mapsto(z,z)\).
In the target \(K(\Delta^m,\Delta^m)\), form

\[
z=(F+G)(e_i\otimes\sigma_m^\Delta)
+H\partial(e_i\otimes\sigma_m^\Delta).
\]

This is a cycle: applying \(\partial\), the chain-map identities and the lower-degree homotopy identity cancel its two copies of \((F+G)\partial\). In degree zero it has augmentation zero; in fact the two maps then agree on the single vertex.

Each singular chain complex of the convex simplex contracts to its first vertex by the cone homotopy of the Thom/Euler chapter. If \(P=i\epsilon\) is its augmentation projection and \(K\) its contraction, the four-factor homotopy

\[
K\otimes1\otimes1\otimes1+
P\otimes K\otimes1\otimes1+
P\otimes P\otimes K\otimes1+
P\otimes P\otimes P\otimes K
\]

has boundary sum \(1-P^{\otimes4}\), by telescoping the four contraction identities. Hence it fills every augmented cycle in that tensor complex. Apply it to \(z\); the resulting filling defines \(H(e_i\otimes\sigma_m^\Delta)\). For an arbitrary simplex \(\sigma=(\sigma_X,\sigma_Y)\), push this filling forward by
\(\sigma_X\otimes\sigma_X\otimes\sigma_Y\otimes\sigma_Y\).
Define \(H(\tau e_i\otimes\sigma)=\tau H(e_i\otimes\sigma)\).

This induction is consistent: the domain is free on these generators and their \(\tau\) translates, so no invariant choice of filling is required. Faces are affine images of lower-dimensional universal simplices; the already defined \(H\) on their images is the one used in the residual cycle. The construction commutes with maps of \(X\) and \(Y\), because the only filling choices were made on the fixed universal simplices. It gives

\[
F+G=\partial H+H\partial.
\tag{3.4}
\]

It also preserves product subspaces: every target simplex in an \(X\) factor lies in the image of \(\sigma_X\), and every target simplex in a \(Y\) factor lies in the image of \(\sigma_Y\). This support assertion includes the cone fillings, since they are pushed forward from the same two model simplices.

**Proof: evaluating the comparison.** Let \(a,b\) be cocycles of degrees \(n,p\), and put
\(\varphi=a\otimes a\otimes b\otimes b\).
This cocycle of degree \(2n+2p\) is invariant under the simultaneous exchange. Fix \(s\leq n+p\) and put \(i=n+p-s\). Evaluating \(F\) on \(e_i\otimes c\), for chains \(c\) of degree \(n+p+s\), gives

\[
(a\times b)\smile_i(a\times b).
\]

Evaluating \(G\) uses the terms \(e_j\otimes\tau^j e_{i-j}\) of (3.3). The twist \(\tau^j\) disappears on evaluation by \(b\otimes b\). The corresponding cochain is

\[
(a\smile_j a)\times(b\smile_{i-j}b).
\]

It can be nonzero only when \(0\leq j\leq n\) and \(0\leq i-j\leq p\). For example, if \(j>n\), its required input degree is \(2n-j<j\), where \(D_j\) is zero. Set \(r=n-j\), \(t=p-(i-j)\); then \(r+t=s\), and these terms give exactly the right-hand side of (3.2).

Equation (3.4) says the two evaluations differ by a coboundary. More explicitly, the cochain primitive on a chain \(c\) of degree \(n+p+s-1\) is \(\varphi H(e_i\otimes c)\). The \(\partial H\) term evaluates to zero because \(\varphi\) is a cocycle. The term involving
\(\partial e_i=(1+\tau)e_{i-1}\) also evaluates to zero because \(H\) is equivariant and \(\varphi\) is invariant. The remaining term is precisely the differential of that primitive. Thus (3.2) follows. If \(s>n+p\), its left side is zero and every term on the right has \(r>n\) or \(t>p\), so the formula holds there too. Pull back along \(X\to X\times X\) and use naturality to obtain (3.1).

**Proof for pairs.** If \(a\) vanishes on \(A\) and \(b\) on \(B\), all the maps just used preserve the chains in either \(A\times Y\) or \(X\times B\). Evaluation and the homotopy primitive therefore vanish on their sum. Work first in the quotient of \(C_*(X\times Y)\) by
\(C_*(A\times Y)+C_*(X\times B)\).
The higher diagonals preserve this sum, and the product map and its homotopies descend. When the two subspaces are open, the small-chain equivalence proved in the Thom/Euler chapter identifies this quotient with the usual relative complex for their union. The quotient map commutes with every \(D_i\), so the operations on cohomology correspond under this equivalence. If one subspace is empty, its sum is already the ordinary chain complex of the other product subspace; no small-chain argument is needed. This proves (3.2) in the stated relative cases. Naturality along the diagonal gives the relative internal version. \(\square\)

For a homogeneous class define its total square by
\(\operatorname{Sq}x=\sum_{s\geq0}\operatorname{Sq}^s x\).
Instability makes the sum finite. Extend additively to the graded direct sum of cohomology groups. Theorem 3.1 says this total operation preserves multiplication; its degree-zero component is the identity. No relations between iterated squares are needed for the constructions below.

## 4. Transferring the squares through the Thom isomorphism

Let \(V\to B\) be a real rank-\(r\) bundle over a Hausdorff base. Let \(E\) be its total space, \(E_0\) its nonzero vectors and \(u_V\in H^r(E,E_0)\) its canonical mod-two Thom class. The preceding Thom theorem supplies the isomorphism

\[
\Phi_V:H^j(B)\longrightarrow H^{j+r}(E,E_0),\qquad
\Phi_V(x)=\pi^*x\smile u_V.
\]

Define the **Stiefel–Whitney classes** by

\[
w_i(V)=\Phi_V^{-1}\bigl(\operatorname{Sq}^i u_V\bigr),\qquad
w(V)=1+w_1(V)+\cdots+w_r(V).
\tag{4.1}
\]

Here \(w_i(V)\in H^i(B;\mathbf F_2)\). For \(i>r\) the square is zero. The rank-zero bundle has \(u=1\), \(\Phi\) the identity, and \(w=1\).

**Theorem 4.1 (existence and the four axioms).** Formula (4.1) has the following properties.

1. \(w_0(V)=1\) and \(w_i(V)=0\) for \(i>\operatorname{rank}V\).
2. \(w_i(f^*V)=f^*w_i(V)\) for continuous maps between Hausdorff bases; bundle isomorphisms give the same classes.
3. \(w(V\oplus W)=w(V)w(W)\).
4. For the tautological line \(\gamma_{\mathbb R}\) over \(\mathbb RP^1\), \(w_1(\gamma_{\mathbb R})\) is the nonzero class of \(H^1(\mathbb RP^1;\mathbf F_2)\).

Moreover,

\[
w_r(V)=e_{\mathbf F_2}(V).
\tag{4.2}
\]

For an integrally oriented bundle the right side is the reduction modulo two of its integral Euler class.

**Proof.** The identity square gives \(\operatorname{Sq}^0u_V=u_V=\Phi_V(1)\), and instability gives the asserted rank bound. Thom-class naturality and square naturality show that the pullback of (4.1) is the defining equation for the pullback bundle. Its Thom isomorphism is injective, so the classes are natural.

The top square is \(u_V^2\). Section 8 of the Thom/Euler chapter proves the self-intersection identity

\[
u_V^2=\pi^*e_{\mathbf F_2}(V)\smile u_V
=\Phi_V(e_{\mathbf F_2}(V)).
\]

Its proof uses restriction of the relative class to the absolute total-space cohomology and scalar contraction to the zero section. Thus it applies to the same Hausdorff bases as the Thom theorem. Applying \(\Phi_V^{-1}\) proves (4.2). Integral reduction is the coefficient compatibility established there. In rank one, (4.2) identifies the class with the orientation-transport class proved in Section 9 of that chapter. For the Möbius line over \(\mathbb RP^1\), its loop reverses the fibre sign, so that class evaluates to one. This proves normalization.

For the product formula first place \(V\) and \(W\) on separate bases \(B,C\). Their external direct sum has Thom class \(u_V\times u_W\): this is the fibrewise product-generator statement proved in the Thom/Euler chapter, Section 8. The nonzero-vector subspaces are open, so relative Cartan gives

\[
\begin{aligned}
\operatorname{Sq}^s(u_V\times u_W)
&=\sum_{i+j=s}\operatorname{Sq}^i u_V\times\operatorname{Sq}^j u_W\\
&=\pi^*\left(\sum_{i+j=s}w_i(V)\times w_j(W)\right)
\smile(u_V\times u_W).
\end{aligned}
\]

Associativity and commutativity in mod-two cohomology justify the second equality; no integral sign is involved. The Thom isomorphism on the external direct sum is injective, so its degree-\(s\) class is the displayed sum. If the bundles have the same base, pull back along \(B\to B\times B\). The pullback bundle is \(V\oplus W\), and naturality now gives
\(w_s(V\oplus W)=\sum_{i+j=s}w_i(V)w_j(W)\).
This is the total product formula. Rank zero is included by the identity Thom class and by the relative Cartan cases with an empty subspace. \(\square\)

In particular \(w(\varepsilon^r)=1\): a trivial bundle is pulled back from a point, whose positive-degree cohomology is zero. For a real line \(L\),

\[
w(L)=1+e_{\mathbf F_2}(L)=1+w_1(L),
\]

where its first class is exactly the earlier transport class. Thus the notation for the first line class used in the preceding chapters agrees with the full sequence just constructed.

## 5. Why the axioms determine the classes

The four axioms suffice; the computation of the universal Grassmannian ring is not needed for this uniqueness proof. That makes the argument independent of the later use of these very classes to calculate that ring.

**Theorem 5.1 (uniqueness).** On real finite-rank bundles over Hausdorff spaces, the four axioms in Theorem 4.1 determine the classes uniquely. They also determine them uniquely if the category of bases is restricted to paracompact Hausdorff spaces.

**Proof on lines over compact bases.** Let \(\widetilde w\) be another rule satisfying the axioms. For \(N\geq1\), the ring calculation in the Gysin chapter shows that
\(H^1(\mathbb RP^N)=\mathbf F_2 a\), and restriction to \(\mathbb RP^1\) sends \(a\) to its nonzero generator. Naturality and normalization therefore force
\(\widetilde w_1(\gamma_{\mathbb R}|_{\mathbb RP^N})=a=w_1(\gamma_{\mathbb R}|_{\mathbb RP^N})\).
For \(N=0\) it is zero. The rank bound determines all the other positive classes of a line. Every line over a compact Hausdorff space is pulled back from a finite tautological line by the finite embedding theorem of the first chapter. Consequently \(\widetilde w=w\) on these lines.

**Proof on arbitrary rank over compact bases.** A compact Hausdorff base is paracompact, so the flag-splitting theorem supplies
\(f:\operatorname{Flag}(V)\to B\), with injective mod-two cohomology pullback and
\(f^*V=\bigoplus_{l=1}^{r}L_l\).
The flag space is compact Hausdorff. Here is the compactness check, which is needed before applying the preceding line argument. A locally trivial bundle with compact fibre over a compact base has compact total space. Given an open cover upstairs, trivialize at each \(b\). Finitely many product neighbourhoods \(U_i\times O_i\), each lying in a cover member, cover the fibre over \(b\). Intersect the finitely many \(U_i\); the resulting neighbourhood \(U_b\) has its entire inverse image covered by those same finitely many members. Finitely many \(U_b\) cover the compact base, yielding a finite cover of the total space by original members. Hausdorffness follows from the bundle charts and the Hausdorff base. Applying this at every projective step proves the assertion for the flag tower.

The line case and Whitney axiom now give

\[
f^*\widetilde w(V)=\prod_{l=1}^{r}\widetilde w(L_l)
=\prod_{l=1}^{r}w(L_l)=f^*w(V).
\]

Injectivity forces equality on \(B\). Rank zero follows directly from the rank and constant-term axiom.

**Passage to every Hausdorff base.** Let
\(\alpha=\widetilde w_i(V)-w_i(V)\in H^i(B;\mathbf F_2)\).
Every singular cycle is a finite sum of simplices, so its image is contained in a compact subset \(C\subset B\). The restriction of \(V\) to \(C\) is a bundle on a compact Hausdorff space. Naturality and the compact proof make \(\alpha|_C=0\), hence its evaluation on that cycle is zero. The field coefficient theorem proved in the Thom/Euler chapter identifies
\(H^i(B;\mathbf F_2)=\operatorname{Hom}_{\mathbf F_2}(H_i(B;\mathbf F_2),\mathbf F_2)\).
Thus a class evaluating to zero on every cycle is zero, proving uniqueness. This argument uses field duality; it makes no analogous claim about detection of arbitrary integral cohomology by compact restrictions.

If rules are defined only on paracompact Hausdorff bases, the same compact restrictions and flag spaces lie in that category, so the proof is unchanged. \(\square\)

For a paracompact Hausdorff base we can now write the splitting formula

\[
f^*w(V)=\prod_{l=1}^{r}(1+x_l),\qquad x_l=w_1(L_l).
\tag{5.1}
\]

It is a formula after an injective pullback. The existence of the classes downstairs was proved by (4.1), so no descent of arbitrary flag polynomials is being assumed.

**Corollary 5.2 (the first class and orientation).** For every Hausdorff base,
\(w_1(V)=w_1(\det V)\).
An orientable bundle has \(w_1=0\). On a Hausdorff CW complex the converse holds: \(V\) is orientable exactly when \(w_1(V)=0\).

**Proof.** On a flag space, \(\det f^*V=\bigotimes_l L_l\). The real-line tensor formula from the Gysin chapter and (5.1) show that both first classes pull back to \(\sum_l x_l\). Injectivity proves the equality for paracompact Hausdorff bases. Restricting to compact subsets and using field detection as in Theorem 5.1 proves it for every Hausdorff base.

A choice of orientation trivializes the sign transport on the determinant line, so its first transport class is zero. Conversely, on a CW complex the full line-classification theorem proved in the classifying-maps chapter says that a line with zero first class is trivial. A nonzero section of the trivial determinant line specifies an orientation of every vector-space fibre, continuously in bundle charts. This orients \(V\). For rank zero use its canonical empty-basis orientation. \(\square\)

For a complex line \(L\), its underlying real plane has the complex orientation. Thus
\(w_1(L_{\mathbb R})=0\) and
\(w_2(L_{\mathbb R})=\rho_2 c_1(L)\), by (4.2) and the line definition of \(c_1\) in the preceding chapter. Hence
\(w(L_{\mathbb R})=1+\rho_2 c_1(L)\). This is the first bridge between the real and complex characteristic classes.

## 6. Computations of the operations

For the degree-one generator \(a\) of real projective cohomology, Theorem 2.1 gives
\(\operatorname{Sq}a=a+a^2\). Repeated Cartan and the binomial expansion give

\[
\operatorname{Sq}^s(a^m)=\binom{m}{s}a^{m+s},
\qquad \binom{m}{s}\text{ read modulo two}.
\tag{6.1}
\]

This applies to \(\mathbb RP^N\) with its truncation \(a^{N+1}=0\), and to \(\mathbb RP^\infty\) without a truncation. Naturality agrees with the restrictions between them. The formula for \(m=0\) is \(\operatorname{Sq}(1)=1\).

For the mod-two reduction \(x\) of the positive complex-projective generator, \(|x|=2\). Its first square is zero, since \(H^3(\mathbb CP^N;\mathbf F_2)=0\). This vanishing, and the ring with mod-two coefficients, follow from the free even-degree integral homology and the coefficient theorem of the previous chapters. Its top square is \(x^2\). Thus

\[
\operatorname{Sq}^{2s}(x^m)=\binom{m}{s}x^{m+s},\qquad
\operatorname{Sq}^{2s+1}(x^m)=0.
\tag{6.2}
\]

The proof is the expansion of \((x+x^2)^m\), with the same finite-projective truncation as appropriate. The integral generator may be chosen as the first class of the dual tautological line; reduction removes its sign distinction from the tautological line.

One further consequence will be used in the manifold calculations. If \(H^q(X;\mathbf F_2)=0\) for \(q>d\), the total square is an additive automorphism of the graded direct sum of cohomology. Indeed write it as \(1+N\). On every homogeneous class \(N\) strictly increases degree. Hence \(N^{d+1}=0\), and

\[
(1+N)^{-1}=1+N+N^2+\cdots+N^d.
\]

Its multiplicativity makes it a ring automorphism too. The degree bound matters. On \(\mathbf F_2[a]=H^*(\mathbb RP^\infty;\mathbf F_2)\), substitution \(a\mapsto a+a^2\) is not onto: a nonconstant polynomial of degree \(m\) maps to one of degree \(2m\), so it cannot map to \(a\). An inverse exists in the degree completion, where \(a+a^2+a^4+\cdots\) is a meaningful series, but that series is not an element of the graded direct-sum polynomial ring.

## 7. Exercises with complete solutions

**Exercise 7.1 (easy).** Compute \(D_1\) on a triangle and verify the higher-diagonal identity there directly.

**Solution.** Write \(s=\sigma[0,1,2]\), \(e_{ij}=\sigma[i,j]\), and \(v_i=\sigma[i]\). The three one-element deletion sets give

\[
D_1s=s\otimes e_{12}+e_{02}\otimes s+s\otimes e_{01}.
\]

Each edge has \(D_1e=e\otimes e\). Substitute
\(\partial s=e_{12}+e_{02}+e_{01}\) and \(\partial e_{ij}=v_i+v_j\). The repeated edge tensors cancel, leaving

\[
\begin{aligned}
(\partial D_1+D_1\partial)s
={}&(v_0+v_2)\otimes s+s\otimes(v_0+v_2)\\
&+e_{01}\otimes e_{12}+e_{12}\otimes e_{01}.
\end{aligned}
\]

Since \(D_0s=v_0\otimes s+e_{01}\otimes e_{12}+s\otimes v_2\), this is precisely \((1+T)D_0s\). In particular the middle deletion contributes \(e_{02}\otimes s\), not the other order: its vertex number one plus its tuple position one is even.

**Exercise 7.2 (easy).** Find all squares of \(a^5\) on \(\mathbb RP^\infty\), and then restrict the answer to \(\mathbb RP^9\).

**Solution.** In characteristic two,
\((1+t)^5=(1+t)^4(1+t)=(1+t^4)(1+t)=1+t+t^4+t^5\).
Thus the nonzero squares on the infinite space are
\(\operatorname{Sq}^0a^5=a^5\), \(\operatorname{Sq}^1a^5=a^6\),
\(\operatorname{Sq}^4a^5=a^9\), and \(\operatorname{Sq}^5a^5=a^{10}\).
The second and third squares are zero by even binomial coefficients; every square above five is zero by instability. On \(\mathbb RP^9\) the last of the four displayed answers also becomes zero because \(a^{10}=0\). The degree-one and degree-four squares remain nonzero.

**Exercise 7.3 (medium).** Compute the total square on the cohomology of \(\mathbb CP^2\), and give its inverse.

**Solution.** The ring is \(\mathbf F_2[x]/(x^3)\), with \(|x|=2\). We have
\(\operatorname{Sq}(1)=1\), \(\operatorname{Sq}(x)=x+x^2\), and
\(\operatorname{Sq}(x^2)=(x+x^2)^2=x^2+x^4=x^2\).
Consequently the map sends
\(\alpha+\beta x+\gamma x^2\) to
\(\alpha+\beta x+(\beta+\gamma)x^2\).
Applying it twice is the identity, so in this example its inverse is itself. The truncation explains why the answer is an automorphism here even though the analogous substitution on an infinite polynomial ring need not be onto.

**Exercise 7.4 (medium).** For the Möbius line \(L\to S^1\), compute the first square of its Thom class. Compare the Euler and total Stiefel–Whitney classes of \(L\oplus\varepsilon^1\).

**Solution.** Let \(a\) be the nonzero class of \(H^1(S^1;\mathbf F_2)\). The earlier transport computation gives \(e_{\mathbf F_2}(L)=a\). Since the line Thom class has degree one,

\[
\operatorname{Sq}^1u_L=u_L^2=\pi^*a\smile u_L=\Phi_L(a).
\]

The Thom isomorphism shows this is nonzero. Therefore \(w(L)=1+a\), confirming normalization directly in the Thom construction. The trivial summand has total class one, so
\(w(L\oplus\varepsilon^1)=1+a\).
Its rank-two top class is zero and hence its mod-two Euler class is zero. The constant section in its trivial summand also proves this vanishing. Its first class remains nonzero, so the bundle is not orientable. Vanishing of the top class does not make all the classes vanish.

**Exercise 7.5 (medium).** Suppose \(V\oplus W\cong\varepsilon^k\) on a finite CW complex of dimension \(d\). Express \(w(W)\) in terms of \(w(V)\), and explain the normal-bundle case.

**Solution.** Put \(b=w(V)-1\), a sum of positive-degree classes. The finite-cell dimension bound proved in the Gysin chapter gives \(b^{d+1}=0\). Whitney and the trivial-bundle calculation give
\((1+b)w(W)=1\), so

\[
w(W)=1+b+b^2+\cdots+b^d.
\]

Multiplication verifies the formula, because every intermediate power appears twice and the final power is zero. More generally, if a manifold is embedded in Euclidean space, the tangent-normal decomposition proved in the first chapter gives \(w(TM)w(\nu)=1\) degree by degree. Whenever its cohomology has a finite upper degree bound the same finite formula applies. Otherwise the equality still determines the inverse degree by degree in the degree completion; the actual finite-rank normal bundle supplies the stated class. No embedding existence theorem is asserted in this exercise.

**Exercise 7.6 (hard).** Prove uniqueness on paracompact Hausdorff bases using universal lines and an injective flag pullback. Explain why this avoids a dependence on the universal Grassmannian cohomology theorem.

**Solution.** The Gysin chapter proves that restriction from \(\mathbb RP^N\) to \(\mathbb RP^1\) is an isomorphism in degree one for \(N\geq1\). Thus normalization and naturality force the first class of each finite universal tautological line to be its nonzero generator; rank fixes the higher classes. On a compact Hausdorff base every line is pulled back from one of these finite universal lines, so every axiomatic rule agrees on its classes. For a line on a paracompact Hausdorff base, restrict to each compact subset and use the field-detection argument of Theorem 5.1: each cycle has compact image, so equality of the compact restrictions gives equality of the original cohomology classes. For \(V\), pass to its flag tower; it remains paracompact Hausdorff by the compact-fibre argument proved in the preceding chapter. Whitney makes every rule pull back to \(\prod_l(1+w_1(L_l))\). The composite flag pullback is injective, so the original rules agree on every \(w_i(V)\). This uses only finite universal **line** spaces and their Gysin cohomology. The higher-rank universal cohomology ring can therefore be calculated later using the classes now constructed. Theorem 5.1 additionally proves uniqueness on all Hausdorff bases by compact flags and field detection.

**Exercise 7.7 (hard).** Recover the mod-two Thom theorem by finite-cover induction and justify the passage to a Hausdorff base that has no finite trivializing cover.

**Solution.** This exercise uses the fully proved small-chain, product and coefficient lemmas in Sections 1–6 of the Thom/Euler chapter. On a trivializing set \(U\), the product-chain equivalence and the one-dimensional relative fibre homology in degree \(r\) give a fibre generator and the cup/cap isomorphisms. For two sets, relative Mayer–Vietoris in degree \(r\) glues the generators that agree on the intersection. The relative group of degree \(r-1\) on that intersection vanishes; it gives uniqueness of the glued class. Lower-degree vanishing follows from the same exact sequence. In higher degrees compare the base Mayer–Vietoris sequence with the bundle relative sequence using multiplication by the glued class. The maps commute over \(\mathbf F_2\), including connecting maps. The five lemma gives the cup isomorphisms. The parallel homological diagram with the right-cap map gives the cap isomorphisms. Induct on a finite cover; its final intersection has a cover with fewer sets, so this proves the induction hypothesis required for that intersection. Rank zero is the identity separately.

For any compact \(C\subset B\), the restricted bundle has a finite cover. Its degree-\(r\) Thom class is unique with the prescribed fibre values, so these classes and the induced cap homology maps are compatible on inclusions of compact subsets. Every relative chain has compact projected support. Cycles and any bounding chains have finite support, and finite unions of their supports are still compact. Thus relative homology upstairs and homology downstairs are their respective filtered limits over compact subsets. The compatible finite-base cap isomorphisms give global homology isomorphisms.

In degree \(r\), compose this compatible homology map
\(H_r(E,E_0)\to H_0(B)\) with the augmentation \(H_0(B)\to\mathbf F_2\) that sends every point class to one. Field duality makes the resulting functional a global degree-\(r\) cohomology class \(u\). On each compact restricted bundle its evaluations are those of the local Thom class, so field duality there shows that it restricts to that class. In particular its value on each fibre generator is one. A cocycle representing \(u\) defines a global cap map. On each compact restriction it induces the cap map of the local Thom class: changing representatives by a coboundary changes cap by the explicit homotopy in Section 4 of the Thom/Euler chapter. Its induced global homology map is therefore the compatible isomorphism already obtained. Dualizing over the field makes the cup map
\(x\mapsto\pi^*x\smile u\) an isomorphism in every degree. The same homology calculation gives zero below degree \(r\). This proves the arbitrary-Hausdorff mod-two theorem; it does not attempt a cohomological inverse-limit shortcut. The integral orientation version, including its coefficient passage, was proved separately in the Thom/Euler chapter, Theorem 7.1.

## References

[H] Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2 (2017), [freely accessible author PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Section 3.1. Its axioms, flag pullbacks and uniqueness argument give a further comparison for Sections 4–5. The singular-chain construction and complete Cartan proof are supplied above.

[MM] Anibal M. Medina-Mardones, *New formulas for cup-i products and fast computation of Steenrod squares*, [arXiv:2105.08025v3](https://arxiv.org/abs/2105.08025v3), Definition 7 and Section 8. Scholarly reference for the higher-diagonal index formula. The face cancellation, resolution comparison, Cartan proof and teaching text above are independently authored. The paper's arXiv distribution licence does not license republication of its protected text; none is reproduced here.


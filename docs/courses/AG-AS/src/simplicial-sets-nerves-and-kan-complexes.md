# Simplicial sets, nerves and Kan complexes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A groupoid records objects, isomorphisms and their composition. Its nerve puts these data into successive dimensions: objects are vertices, arrows are edges, and a triangle says that two successive arrows compose to the third. Higher simplices record compatible strings of arrows. A Kan complex permits the same pictures with composition determined only up to homotopy. Filling a three-dimensional horn is then the reason that composition of homotopy classes is associative.

This lesson proves the characterization of category nerves by Segal maps, the characterization of groupoid nerves by unique horn fillings, the construction of the fundamental groupoid of a Kan complex, and its adjunction with the nerve. We also construct combinatorial homotopy groups. One theorem is explicitly stated: Whitehead's theorem for Kan complexes. It turns the preceding constructions into the assertion that groupoids model precisely homotopy one-types.

Our prerequisites are [Lesson 4](stacks-in-groupoids.md), for groupoids and descent, and ordinary algebraic topology, for the meaning of a geometric simplex, paths, the circle and weak homotopy equivalence of spaces. We work with small sets and categories in a fixed universe; a larger universe can be used for their categories. No finiteness or connectedness assumption is imposed on a simplicial set or a groupoid.

## 1. Simplicial sets and their low-dimensional data

### 1.1. The indexing category

The category \(\Delta\) has objects
\[
[n]=\{0<1<\cdots<n\},\qquad n\geq0,
\tag{1.1}
\]
and order-preserving maps as morphisms. Write \(\delta^i:[n-1]\to[n]\) for the injection omitting \(i\), and \(\sigma^i:[n+1]\to[n]\) for the surjection identifying \(i,i+1\). Every order-preserving map factors uniquely as a surjection onto its ordered image followed by the inclusion of that image. The inclusion is a composite of the \(\delta^i\); the surjection is a composite of the \(\sigma^i\). Thus these maps generate \(\Delta\).

A simplicial set is a functor
\[
K:\Delta^{\mathrm{op}}\longrightarrow\mathrm{Set}.
\tag{1.2}
\]
Put \(K_n=K([n])\). The associated faces \(d_i:K_n\to K_{n-1}\) and degeneracies \(s_i:K_n\to K_{n+1}\) satisfy
\[
d_i d_j=d_{j-1}d_i\quad(i<j),\qquad
s_i s_j=s_{j+1}s_i\quad(i\leq j),
\tag{1.3}
\]
and
\[
d_i s_j=
\begin{cases}
s_{j-1}d_i&i<j,\\
\mathrm{id}&i=j\text{ or }i=j+1,\\
s_jd_{i-1}&i>j+1.
\end{cases}
\tag{1.4}
\]
The degree of each operator is determined by its input. These identities follow by comparing the two indicated order-preserving maps. Conversely they let one rewrite composites into a surjection followed by an injection, so sets with these operators and identities determine a simplicial set. This is the presentation in [Stacks, Tags 0164, 0169].

An edge \(a\in K_1\) goes from \(d_1a\) to \(d_0a\). For a triangle \(\tau\in K_2\), we call \(d_2\tau\) its edge \(01\), \(d_0\tau\) its edge \(12\), and \(d_1\tau\) its edge \(02\). In a nerve the resulting equation is
\[
[02]=[12]\circ[01].
\tag{1.5}
\]
This orientation will remain fixed throughout the lesson.

### 1.2. Standard simplices, boundaries and horns

The standard simplex is the representable simplicial set
\[
\Delta[n]_m=\operatorname{Hom}_{\Delta}([m],[n]).
\tag{1.6}
\]
The Yoneda correspondence identifies maps \(\Delta[n]\to K\) with elements of \(K_n\): evaluate a map on \(\mathrm{id}_{[n]}\), and recover its value on \(\alpha:[m]\to[n]\) by \(\alpha^*\). In particular a diagram involving a standard simplex is literally a prescription of faces of one simplex.

The boundary \(\partial\Delta[n]\) consists of maps whose image misses at least one vertex. For \(n=0\) it is empty. For \(n\geq1\), the horn \(\Lambda^k[n]\), \(0\leq k\leq n\), is the union of all codimension-one faces except the face omitting \(k\). Equivalently, a map from the horn to \(K\) prescribes simplices
\[
F_i\in K_{n-1}\quad(i\ne k),\qquad
d_iF_j=d_{j-1}F_i\quad(i<j,\ i,j\ne k).
\tag{1.7}
\]
A filler is \(\tau\in K_n\) with \(d_i\tau=F_i\) for every supplied face.

The two one-dimensional horns are single endpoints. A two-dimensional inner horn, with \(k=1\), gives the two successive edges \(01,12\) and asks for a triangle and an edge \(02\). An outer horn gives two other edges and asks for a division operation. The distinction becomes essential for categories: composition always exists, but division requires inverses.

A simplex is degenerate if it is the pullback of a lower-dimensional simplex by a proper surjection. Every simplex has a unique expression
\[
\alpha^*u,\qquad \alpha:[n]\twoheadrightarrow[p],\quad
u\in K_p\text{ nondegenerate}.
\tag{1.8}
\]
For existence, repeatedly remove degeneracies; dimension decreases. Here is uniqueness. Suppose also \(\alpha^*u=\beta^*v\), with \(v\) nondegenerate and \(\beta:[n]\twoheadrightarrow[q]\). If \(\alpha\) identifies adjacent \(i,i+1\) but \(\beta\) does not, choose a section of \(\beta\) whose image includes both \(i,i+1\). Such a section exists because they lie in successive distinct fibres of \(\beta\). Pulling back the equality along it expresses \(v\) through the noninjective map obtained by composing that section with \(\alpha\). Its surjection-injection factorization would make \(v\) degenerate. This is a contradiction. Interchanging \(\alpha,\beta\) proves that they identify exactly the same adjacent pairs. Ordered surjections are determined by those pairs, so \(\alpha=\beta\); pulling back by a section gives \(u=v\).

It follows that a monomorphism of simplicial sets can be built by adjoining the missing nondegenerate simplices in increasing dimension, each along its entire boundary. This elementary observation will justify a lifting argument in Section 3. The definitions and representable-simplex viewpoint are [Stacks, Tag 0174].

### 1.3. Truncation, skeleton and coskeleton

Let \(\Delta_{\leq r}\) be the full subcategory on \([0],\ldots,[r]\). Restricting \(K\) to it gives its \(r\)-truncation \(t_rK\). In [Stacks, Tag 017Z] the notation \(\mathrm{sk}_r\) denotes this restriction. We distinguish it from the usual *full simplicial skeleton* \(\mathrm{Sk}_rK\): the sub-simplicial set generated by all simplices of dimension at most \(r\). Formula (1.8) says exactly which simplices this includes.

More generally the left extension of an \(r\)-truncated simplicial set is obtained by taking all its formal degeneracies and imposing its already prescribed face and degeneracy identities. It is left adjoint to \(t_r\). On \(t_rK\), its map into \(K\) has image \(\mathrm{Sk}_rK\) and is injective by the uniqueness in (1.8). Thus the skeleton retains low-dimensional simplices and only the higher simplices forced by degeneracy.

The right adjoint instead supplies every compatible system of low-dimensional faces. For an \(r\)-truncated simplicial set \(U\), define
\[
(\operatorname{cosk}_rU)_m
=\operatorname{Hom}_{\mathrm{Set}^{\Delta_{\leq r}^{\mathrm{op}}}}
(t_r\Delta[m],U).
\tag{1.9}
\]
An element assigns a simplex of \(U_j\) to every map \([j]\to[m]\), \(j\leq r\), compatibly with maps between these small ordinals. Precomposition defines all the simplicial operators.

There is a natural bijection
\[
\operatorname{Hom}(K,\operatorname{cosk}_rU)
\cong\operatorname{Hom}(t_rK,U).
\tag{1.10}
\]
Indeed, given the right-hand map, an \(m\)-simplex \(a\) of \(K\) produces the compatible assignment \(\alpha\mapsto \alpha^*a\mapsto U_j\). Conversely restrict a left-hand map to degrees at most \(r\), where Yoneda makes (1.9) equal to \(U_j\). These operations undo one another in every degree. This proves the adjunction, not merely a counting formula. In a category with finite limits, the same construction uses the finite diagram of maps \([j]\to[m]\) and works with finite limits in place of sets; this is the scope of [Stacks, Tag 0AMA].

For a set \(S\), viewed as zero-dimensional data,
\[
(\operatorname{cosk}_0S)_m=S^{m+1}.
\tag{1.11}
\]
This is the nerve of the groupoid with object set \(S\) and exactly one arrow between each ordered pair of objects. If \(S\) is nonempty, choose \(s\in S\). There is a homotopy from the constant map at \(s\) to the identity: on an \(m\)-simplex \((x_0,\ldots,x_m)\) and an order-preserving map \(\epsilon:[m]\to[1]\), use \(s\) at positions where \(\epsilon(i)=0\), and \(x_i\) where \(\epsilon(i)=1\). Faces and degeneracies plainly preserve this prescription. Thus it is contractible. The empty case remains empty.

## 2. Nerves and the Segal condition

### 2.1. The nerve

For a category \(C\), define
\[
N(C)_n=\operatorname{Fun}([n],C).
\tag{2.1}
\]
Here the ordered set \([n]\) is a category with one arrow \(i\to j\) when \(i\leq j\). A functor is determined by a string
\[
x_0\xrightarrow{a_1}x_1\xrightarrow{a_2}\cdots
\xrightarrow{a_n}x_n.
\tag{2.2}
\]
The end faces delete the first or last arrow and its outside vertex; an interior face composes the two adjacent arrows. A degeneracy inserts an identity. Associativity and identity laws are precisely what make these prescriptions simplicial.

Restricting a simplex to its successive edges gives the Segal map
\[
K_n\longrightarrow
K_1\times_{K_0}\cdots\times_{K_0}K_1
\quad(n\text{ factors}),\qquad n\geq2.
\tag{2.3}
\]
The fibre products use target \(d_0\) on each left edge and source \(d_1\) on the following edge.

**Proposition 2.1.** The functor \(N:\mathrm{Cat}\to\mathrm{sSet}\) is fully faithful. A simplicial set is isomorphic to a category nerve if and only if every map (2.3) is bijective.

**Proof.** For a nerve, strings (2.2) give the required bijections. A functor \(C\to D\) induces a simplicial map. Conversely a simplicial map \(N(C)\to N(D)\) gives maps on objects and arrows. Its compatibility with \(s_0\) preserves identities. Apply it to the two-simplex of any composable pair; compatibility with \(d_1\) preserves composition. Thus it is a functor, and its action on strings forces its action in every degree. This proves full faithfulness.

Now suppose all Segal maps for \(K\) are bijective. Define \(C_K\) to have objects \(K_0\), arrows \(K_1\), source \(d_1\), target \(d_0\), and identity \(s_0x\). For composable arrows \(a,b\), let \(\tau\) be the unique two-simplex with \(d_2\tau=a,d_0\tau=b\), and define
\[
b\circ a=d_1\tau.
\tag{2.4}
\]
The identities (1.3) give its correct source and target. The simplices \(s_0a\) and \(s_1a\), with their faces given by (1.4), prove the two unit laws.

Given \(a:x_0\to x_1,b:x_1\to x_2,c:x_2\to x_3\), the Segal bijection in degree three supplies a unique simplex \(\omega\) with these successive edges. Its face on \(012\) has edge \(02=b\circ a\), and its face on \(123\) has edge \(13=c\circ b\). The face on \(023\) therefore has edge \(03=c\circ(b\circ a)\); the face on \(013\) has that same edge \(03=(c\circ b)\circ a\). Their common edge is equal by the simplicial face identities. This proves associativity.

The Segal bijections now identify \(K_n\) with \(N(C_K)_n\). To check that this identification is simplicial, restrict an \(n\)-simplex to any three ordered vertices. Equation (2.4) shows that a nonconsecutive edge is the composite of the intervening edges, by induction on their number. A repeated vertex gives an identity by a degeneracy. For any monotone \(\alpha:[m]\to[n]\), the successive edges of \(\alpha^*\omega\) are consequently exactly the arrows obtained by restricting the corresponding functor \([n]\to C_K\) along \(\alpha\). This proves compatibility with every operator and finishes the reconstruction. \(\square\)

This is the first verified untagged addition [AI Integrated Stacks Project, simplicial.tex, lemma-characterize-nerves-categories]. The statement has no upstream Stacks tag. It is valid internally in a category with finite limits: replace bijections by isomorphisms and use the same faces to obtain the object, arrow object, identity and composition. In particular an internal groupoid presentation from Lesson 4 has an internal simplicial nerve.

### 2.2. What two-simplices and three-simplices do

The two-simplex in a nerve gives an equality of arrows, not an additional freely chosen two-morphism. Once its successive edges are known, it is unique. The three-simplex then records the associativity equality forced by those arrows. This explains why Segal bijectivity is much stronger than the existence of fillers. In a general Kan complex two different fillers can produce two different composite edges. Section 4 will show that those edges have the same homotopy class, using one further horn.

A nerve is two-coskeletal: a compatible system of vertices, edges and triangles extends uniquely to every higher simplex. Indeed, each triangle asserts the composition relation among its three edges, so the consecutive edges determine a functor \([n]\to C\), and all the supplied edges and triangles agree with that functor. A category nerve need not be one-coskeletal: arbitrary edges between all vertex pairs need not obey composition. A zero-coskeletal example such as (1.11) is special because its arrows are already unique.

## 3. Kan lifting and groupoid nerves

### 3.1. Two lifting conditions

A map \(p:X\to Y\) is a **Kan fibration** if every square from \(\Lambda^k[n]\hookrightarrow\Delta[n]\), \(n\geq1\), against \(p\) admits a filler. It is a **trivial Kan fibration** if the same assertion holds for \(\partial\Delta[n]\hookrightarrow\Delta[n]\), \(n\geq0\). A **Kan complex** is a simplicial set \(K\) for which \(K\to\Delta[0]\) is a Kan fibration. These definitions are respectively [Stacks, Tags 08NU, 08NL]. Trivial Kan includes surjectivity on vertices, since the boundary in dimension zero is empty.

Both kinds of fibration are closed under base change. A lifting problem for a pullback projects to one for \(p\), and its chosen filler, paired with the given simplex in the new base, is the required filler in the pullback. They are closed under composition: first fill the lifting problem for the second map, then use that filler as the bottom simplex for the first map. Products are handled coordinatewise. These arguments prove [Stacks, Tags 08NV, 08NW] and the corresponding parts of [Stacks, Tag 08NM]. A filtered colimit of such maps has the same lifting property, since a boundary, a horn and a simplex have finitely many nondegenerate simplices, so any lifting square and its equalities occur at a sufficiently late stage.

The boundary lifting property is equivalent to lifting against every monomorphism. Build the monomorphism by adjoining its missing nondegenerate simplices as after (1.8); at each step the previously defined map on the boundary and the prescribed map to \(Y\) give a boundary lifting problem. Choose a filler and continue. Within a degree, well-order the missing simplices. At limit steps use the union of the compatible maps. Conversely a boundary inclusion is a monomorphism. This proves the full assertion in [Stacks, Tag 08NM].

In particular a trivial Kan fibration \(p:X\to Y\) has a section: lift \(\varnothing\hookrightarrow Y\) against \(p\). If \(s\) is a section, the maps \(sp,\mathrm{id}_X\) on the two ends of \(X\times\Delta[1]\) lie over the same map \(p\operatorname{pr}_X\). Lifting their endpoint inclusion, which is a monomorphism, gives a homotopy
\[
sp\simeq\mathrm{id}_X,\qquad ps=\mathrm{id}_Y.
\tag{3.1}
\]
Thus a trivial Kan fibration is a homotopy equivalence. Its reverse implication for arbitrary maps is not part of the definition. A Kan complex need not have fillers for every boundary: loops and spheres can obstruct them.

### 3.2. Invertibility is exactly Kan filling for nerves

**Proposition 3.1.** For a category \(C\), the following conditions are equivalent:

1. Every arrow in \(C\) is invertible.
2. \(N(C)\) is a Kan complex.
3. Every horn \(\Lambda^k[n]\to N(C)\) with \(n\geq2\) has a unique filler.

**Proof.** Suppose \(C\) is a groupoid. For a two-horn, write the edges as \(a:0\to1,b:1\to2,c:0\to2\). The missing edge is forced by one of
\[
c=ba,\qquad b=ca^{-1},\qquad a=b^{-1}c.
\tag{3.2}
\]
The resulting pair of successive arrows gives the unique triangle.

Now let \(n\geq3\), and let the missing face be the one opposite vertex \(k\). Every vertex and every edge is supplied by the horn. Every triangle containing \(k\) is also supplied: in dimension three these are precisely the included faces, and in greater dimension each such triangle lies in an included face. Put \(a_k=\mathrm{id}_{x_k}\). For \(i>k\), let \(a_i:x_k\to x_i\) be the supplied edge \(ki\); for \(i<k\), let \(a_i\) be the inverse of the supplied edge \(ik\). The triangle relations containing \(k\), using inverses if \(k\) is an end vertex, imply
\[
\text{edge }ij=a_j a_i^{-1}\quad(i<j).
\tag{3.3}
\]
These formulas imply every composition relation, including any missing one. They define a functor \([n]\to C\) and hence a filler. Its edges are forced, so it is unique; its restriction to every supplied face agrees there because a nerve simplex is determined by successive edges. This includes the outer three-horns, where cancellation is required.

In dimension one each horn can be filled by the identity at its given endpoint. These fillers need not be unique. We have proved both (2) and (3) from (1).

Conversely suppose (2). For an arrow \(a:x\to y\), prescribe a horn on vertices \(x,y,x\) with edges \(01=a,02=\mathrm{id}_x\). Its filler gives \(b:y\to x\) with \(ba=\mathrm{id}_x\). Prescribe the other outer horn on vertices \(y,x,y\) with \(12=a,02=\mathrm{id}_y\). Its filler gives \(c:y\to x\) with \(ac=\mathrm{id}_y\). Associativity in \(C\) gives
\[
b=b(ac)=(ba)c=c.
\tag{3.4}
\]
Thus \(a\) is invertible. Condition (3) also supplies these two-horn fillers, so implies (1). \(\square\)

This proves the second verified untagged addition [AI Integrated Stacks Project, simplicial.tex, lemma-nerve-groupoid-kan]. Notice the qualification \(n\geq2\) in uniqueness. For a one-object groupoid with a nontrivial group, every group element fills the one-horn at its sole object.

The simplex \(\Delta[n]\) is the nerve of the ordered category \([n]\). When \(n\geq1\), its arrow \(0\to1\) has no inverse, so Proposition 3.1 proves that it is not Kan. This does not prevent it from being contractible: a homotopy from its identity to the constant map at \(n\) is obtained from the order-preserving map \([n]\times[1]\to[n]\) which is \(i\) at \((i,0)\) and \(n\) at \((i,1)\).

### 3.3. Singular complexes

For a topological space \(T\), its singular simplicial set is
\[
\operatorname{Sing}(T)_n=
\{\text{continuous maps }|\Delta[n]|\to T\}.
\tag{3.5}
\]
Faces and degeneracies are pullbacks along the corresponding affine maps of geometric simplices.

**Proposition 3.2.** The singular simplicial set of every topological space is Kan.

**Proof.** In barycentric coordinates \(t_0,\ldots,t_n\), let
\[
u=\min_{i\ne k}t_i,\qquad
r_i=t_i-u\ (i\ne k),\qquad r_k=t_k+nu.
\tag{3.6}
\]
The coordinates \(r_i\) are nonnegative and sum to one. Some \(r_i\), \(i\ne k\), is zero, so \(r(t)\) lies in the geometric horn \(|\Lambda^k[n]|\). On the horn itself \(u=0\), so \(r\) is the identity there. Replacing \(u\) by \(su\), \(0\leq s\leq1\), gives a continuous deformation fixed on the horn. Thus the horn is a strong deformation retract of the geometric simplex.

A singular horn gives continuous maps on its finitely many closed faces which agree on their intersections. The finite closed-cover gluing lemma gives one continuous map on the entire horn. Compose it with \(r\) to obtain a singular \(n\)-simplex extending every supplied face. This argument also covers \(n=1\), where \(r\) retracts an interval to its supplied endpoint. \(\square\)

There is no corresponding retraction onto the entire boundary of a positive-dimensional simplex. That is the geometric reason why Kan filling and boundary filling have different homotopical content.

## 4. Homotopy and the fundamental groupoid

### 4.1. Homotopy with fixed endpoints

A simplicial homotopy from \(f:A\to B\) to \(g:A\to B\) is a map
\[
H:A\times\Delta[1]\longrightarrow B
\tag{4.1}
\]
whose restrictions to \(0,1\) are \(f,g\). For a sub-simplicial set \(D\subset A\), it is relative to \(D\) if its restriction to \(D\times\Delta[1]\) is the constant-in-time map prescribed on \(D\). This is [Stacks, Tag 019J]. In arbitrary targets the directed relation given by one such homotopy need not be symmetric or transitive. The equivalence relation generated by homotopies is always available. In a Kan target, for edges with fixed endpoints, a single elementary triangle suffices.

Fix vertices \(x,y\) in a Kan complex \(K\). Write \(1_y=s_0y\). For edges \(a,b:x\to y\), a **right homotopy** \(H(a,b)\) means a triangle on vertices \(x,y,y\) with
\[
(d_0H,d_1H,d_2H)=(1_y,b,a).
\tag{4.2}
\]
We use \(H(a,b)\) for any witness, not for a specified canonical choice.

**Lemma 4.1.** The existence of a right homotopy is an equivalence relation on the edges from \(x\) to \(y\). It is also exactly the relation of simplicial homotopy relative to the two endpoints.

**Proof.** Reflexivity is witnessed by \(s_1a\), using (1.4). For symmetry take the three-horn on vertices \(x,y,y,y\) with
\[
d_0\omega=e_2(y),\qquad d_2\omega=s_1a,\qquad
d_3\omega=H(a,b),
\tag{4.3}
\]
and missing \(d_1\omega\). Here \(e_j(y)\) denotes the constant \(j\)-simplex at \(y\). The intersections of the supplied faces are respectively the edge \(1_y\), the edge \(1_y\), and the edge \(a\), so they agree. The missing face has edges \(01=b,02=a,12=1_y\), and is \(H(b,a)\).

For transitivity prescribe
\[
d_0\omega=e_2(y),\qquad d_1\omega=H(b,c),\qquad
d_3\omega=H(a,b),
\tag{4.4}
\]
missing \(d_2\omega\). On the three supplied intersections the edges are \(1_y,1_y,b\); hence this is a horn. Its missing face is \(H(a,c)\).

We compare triangles with the cylinder in (4.1). The product \(\Delta[1]\times\Delta[1]\) is the nerve of the ordered square. Its two nondegenerate triangles have vertices
\[
A=(0,0),\ B=(1,0),\ D=(1,1),
\quad\text{and}\quad
A,\ C=(0,1),\ D.
\tag{4.5}
\]
Given (4.2), put that triangle on \(ABD\), with bottom edge \(a\) and diagonal \(b\), and put \(s_0b\) on \(ACD\). The vertical edges are identities at \(x,y\), and the two triangles agree on their diagonal. This gives a simplicial map of the square, hence a homotopy from \(a\) to \(b\) relative to endpoints.

Conversely such a square has bottom edge \(a\), top edge \(b\), constant vertical edges, and a diagonal \(c:x\to y\). Triangle \(ABD\) gives \(H(a,c)\). Triangle \(ACD\) has vertices \(x,x,y\) and edges \(01=1_x,12=b,02=c\). Convert this latter triangle \(L\) into a right homotopy as follows. On vertices \(x,x,y,y\), prescribe \(d_0\omega=s_1b,d_2\omega=s_0b,d_3\omega=L\), missing \(d_1\omega\). Their three intersections are \(b,b,1_x\), so they agree. The missing face has edges \(02=c,03=b,23=1_y\), and is \(H(c,b)\). Transitivity now gives \(H(a,b)\). This proves both assertions. \(\square\)

This proof specifies the horns that are often hidden in the phrase “homotopy is an equivalence relation.” No reversal map of \(\Delta[1]\) has been used: the order-reversing map on its two vertices is not a morphism in \(\Delta\).

### 4.2. Defining composition and proving its independence

For \(a:x\to y,b:y\to z\), fill the inner two-horn with edges \(a,b\). If its third edge is \(c:x\to z\), set
\[
[b]\,[a]=[c].
\tag{4.6}
\]
Brackets mean classes for Lemma 4.1. Write \(T(b,a;c)\) for such a triangle, whose faces are \(b,c,a\) in order \(d_0,d_1,d_2\).

**Lemma 4.2.** Formula (4.6) is independent of the filler and of the representatives.

**Proof.** Suppose \(\tau=T(b,a;c)\) and \(\tau'=T(b,a;c')\) are two fillers. On vertices \(x,y,z,z\), prescribe
\[
d_0\omega=s_1b,\qquad d_2\omega=\tau',
\qquad d_3\omega=\tau,
\tag{4.7}
\]
missing \(d_1\omega\). The intersections for the pairs \((0,2),(0,3),(2,3)\) are \(b,b,a\). Thus they form a horn, and its missing face is \(H(c,c')\). This proves independence of filler.

Suppose \(H(a,a')\) is given. On vertices \(x,y,y,z\), prescribe
\[
d_0\omega=s_0b,\qquad d_2\omega=T(b,a;c),
\qquad d_3\omega=H(a,a'),
\tag{4.8}
\]
missing \(d_1\omega\). The intersections are \(b,1_y,a\); the missing face is \(T(b,a';c)\). Thus changing the first edge leaves the product class unchanged.

Suppose \(H(b,b')\) is given. On vertices \(x,y,z,z\), prescribe
\[
d_0\omega=H(b,b'),\qquad d_1\omega=s_1c,
\qquad d_3\omega=T(b,a;c),
\tag{4.9}
\]
missing \(d_2\omega\). The intersections are \(1_z,b,c\). The missing face is \(T(b',a;c)\), so changing the second edge also leaves the product unchanged. The relation is an equivalence relation by Lemma 4.1; these changes handle any representatives of either class. \(\square\)

### 4.3. The groupoid laws

**Proposition 4.3.** For a Kan complex \(K\), the vertices and the relative-endpoint homotopy classes of edges form a groupoid \(\Pi_1(K)\). Simplicial maps induce functors. Its vertex automorphism group is \(\pi_1(K,x)\).

**Proof.** Define its objects as \(K_0\) and its arrows \(x\to y\) as the classes in Lemma 4.1; Lemma 4.2 defines composition. Degenerate triangles \(s_0a,s_1a\) show that \([1_x]\) and \([1_y]\) are the two units for \([a]\).

For associativity start with \(a:x\to y,b:y\to z,c:z\to w\). Choose
\[
T(b,a;p),\qquad T(c,b;q),\qquad T(c,p;r).
\tag{4.10}
\]
They are the faces on \(012,123,023\) of a horn on vertices \(x,y,z,w\):
\[
d_3\omega=T(b,a;p),\quad
d_0\omega=T(c,b;q),\quad
d_1\omega=T(c,p;r).
\tag{4.11}
\]
For the pairs of faces \((0,1),(0,3),(1,3)\), their intersections are \(c,b,p\), respectively, so they are compatible. Fill the horn missing \(d_2\omega\). That face is \(T(q,a;r)\). Consequently
\[
[c]\bigl([b][a]\bigr)=[r]
=\bigl([c][b]\bigr)[a].
\tag{4.12}
\]
All choices disappear by Lemma 4.2.

The outer horn on vertices \(x,y,x\), with edges \(01=a,02=1_x\), supplies an edge \(b:y\to x\) such that \([b][a]=[1_x]\). The other outer horn, on vertices \(y,x,y\) with edges \(12=a,02=1_y\), supplies \(c:y\to x\) such that \([a][c]=[1_y]\). The same associative calculation as (3.4), now in classes, gives \([b]=[c]\). Hence every arrow is invertible.

A simplicial map carries each triangle or horn filler used above to one of the same kind. It preserves right homotopy, identity classes and products, so induces a functor, compatibly with compositions of maps. Finally the loops at \(x\), modulo the relation in Lemma 4.1, are by definition \(\pi_1(K,x)\), with product (4.6). They are exactly the automorphisms of \(x\) in this groupoid. \(\square\)

Let \(\pi_0(K)\) be the equivalence classes of vertices for the relation generated by edges, allowing either direction. In a Kan complex the preceding groupoid is connected between two vertices precisely when those vertices belong to the same such class. Indeed, a finite edge zigzag becomes a composable string by inverses, and successive products can be represented by one edge. Thus \(\pi_0(K)\) is also the set of isomorphism classes of \(\Pi_1(K)\). The empty complex has empty \(\pi_0\) and an empty fundamental groupoid.

### 4.4. Higher combinatorial homotopy groups

We give the usual face-based definition, including the fillers that give its group structure. Fix a vertex \(x\), write \(e_j=e_j(x)\), and for \(n\geq1\) put
\[
Z_n(K,x)=\{a\in K_n:d_i a=e_{n-1}
\text{ for every }0\leq i\leq n\}.
\tag{4.13}
\]
Declare \(a\sim b\) when there is an \((n+1)\)-simplex \(H(a,b)\) with
\[
d_iH=e_n\ (i<n),\qquad d_nH=b,\qquad
d_{n+1}H=a.
\tag{4.14}
\]
These are the elementary homotopies of a simplex whose whole boundary is fixed at \(x\). Define \(\pi_n(K,x)=Z_n(K,x)/\sim\). For \(n=1\), this is exactly the loop definition already proved.

Here are complete checks in general dimension. Reflexivity is \(s_na\). For symmetry, prescribe an \((n+2)\)-horn with \(d_i=e_{n+1}\) for \(i<n\), \(d_{n+1}=s_na\), and \(d_{n+2}=H(a,b)\), missing \(d_n\). The only nonconstant supplied intersection is
\[
d_{n+1}H(a,b)=a=d_{n+1}s_na.
\tag{4.15}
\]
All other supplied intersections are constant by (4.13), (4.14) and (1.4). The missing face satisfies (4.14) for \(H(b,a)\). For transitivity prescribe the same constant faces for \(i<n\), then \(d_n=H(b,c)\), \(d_{n+2}=H(a,b)\), missing \(d_{n+1}\). Their one nonconstant intersection is \(b\), and the missing face is \(H(a,c)\). This proves equivalence.

Define the product \([b][a]\) by filling the \(n\)-th horn in dimension \(n+1\) with
\[
d_i=e_n\ (i<n-1),\qquad d_{n-1}=b,\qquad
d_{n+1}=a.
\tag{4.16}
\]
Its missing face \(c=d_n\) lies in \(Z_n(K,x)\). Indeed, for \(j<n\), (1.3) gives \(d_jc=d_{n-1}d_j\tau\), a face of \(e_n\) or of \(b\); for \(j=n\), it gives \(d_nc=d_nd_{n+1}\tau=d_na\). These are all \(e_{n-1}\). Denote the filler by \(T(b,a;c)\). Its final three faces are \(b,c,a\), and its lower faces are constant.

For clarity, the following table supplies every horn needed for the group axioms. Each row is in dimension \(n+2\); all faces with index \(i<n-1\) are \(e_{n+1}\). The four displayed columns are the remaining faces, and the question mark is the single omitted face.

| Purpose | \(d_{n-1}\) | \(d_n\) | \(d_{n+1}\) | \(d_{n+2}\) |
|---|---|---|---|---|
| Independence of filler | \(s_nb\) | \(?=H(c,c')\) | \(T(b,a;c')\) | \(T(b,a;c)\) |
| Replace \(a\) by \(a'\) | \(s_{n-1}b\) | \(?=T(b,a';c)\) | \(T(b,a;c)\) | \(H(a,a')\) |
| Replace \(b\) by \(b'\) | \(H(b,b')\) | \(s_nc\) | \(?=T(b',a;c)\) | \(T(b,a;c)\) |
| Associativity | \(T(c,b;q)\) | \(T(c,p;r)\) | \(?=T(q,a;r)\) | \(T(b,a;p)\) |

We verify compatibility explicitly rather than assuming the table defines horns. For the first row the three intersections among supplied faces, in their column order, are \(b,b,a\). For the second they are \(b,e_n,a\). For the third they are \(e_n,b,c\). For the fourth they are \(c,b,p\). In each case these are equal on the two sides of the required face identity. Any intersection with a lower constant face is constant: taking a lower face of \(T\) or \(H\) gives \(e_n\), and taking such a face of \(s_na\) or \(s_{n-1}a\) gives a degeneracy of a constant face of \(a\). Thus every prescribed system is a horn. Applying (1.3) once more to its missing face gives exactly the indicated \(H\) or \(T\).

The first three rows prove well-defined multiplication. In the fourth, \(p\) represents \([b][a]\), \(q\) represents \([c][b]\), and \(r\) represents \([c][p]\); the missing face represents \([q][a]\) by the same \(r\). This proves associativity. The degeneracies \(s_na\), with final faces \(e_n,a,a\), and \(s_{n-1}a\), with final faces \(a,a,e_n\), prove the unit laws.

For a left inverse fill the \((n-1)\)-st horn in dimension \(n+1\) with \(d_n=e_n,d_{n+1}=a\), and every lower supplied face constant. The missing face \(b\) is a cycle by the same face-identity check used for (4.16), and the filler asserts \([b][a]=[e_n]\). For a right inverse fill the \((n+1)\)-st horn with \(d_{n-1}=a,d_n=e_n\) and lower faces constant. It gives \([a][c]=[e_n]\). Associativity makes these inverse classes equal. This proves that \(\pi_n(K,x)\) is a group for every \(n\geq1\), and maps of pointed Kan complexes induce group homomorphisms.

To identify this with the sphere convention used by Whitehead's theorem, a pointed map \(\Delta[n]/\partial\Delta[n]\to K\) is exactly a cycle (4.13). We check its homotopies as well. Let \(H_j(a,b)\) mean an \((n+1)\)-simplex whose only possibly nonconstant faces are \(d_j=b,d_{j+1}=a\). For \(j<n\), fill the \((n+2)\)-horn missing face \(j\), prescribing
\[
F_{j+1}=s_{j+1}a,\qquad F_{j+2}=H_j(a,b),
\qquad F_{j+3}=s_ja,
\tag{4.17}
\]
and all other faces constant. The intersections among these three supplied faces are \(a,a,e_n\), by (1.4); intersections with the other faces are constant. Its missing face has \(d_{j+1}=b,d_{j+2}=a\) and other faces constant, so is \(H_{j+1}(a,b)\). Repeating moves any such witness to \(H_n(a,b)\).

Triangulate \(\Delta[n]\times\Delta[1]\) by its \(n+1\) maximal simplices
\[
P_j=((0,0),\ldots,(j,0),(j,1),\ldots,(n,1)),
\qquad 0\leq j\leq n.
\tag{4.18}
\]
For a homotopy constant on \(\partial\Delta[n]\times\Delta[1]\), every face of \(P_j\) except \(d_j,d_{j+1}\) is constant. Its two remaining faces are successive diagonals \(E_j,E_{j+1}\), each a cycle, with \(E_0\) the top simplex and \(E_{n+1}\) the bottom simplex. Thus \(P_j\) gives \(H_j(E_{j+1},E_j)\). Formula (4.17) and transitivity identify top and bottom in our relation. Conversely, from \(H_n(a,b)\) define \(P_n\) to be that witness and \(P_j=s_jb\) for \(j<n\). They agree on their consecutive diagonal faces, and every boundary face is constant. They therefore define a cylinder homotopy from \(a\) to \(b\) relative to the boundary. This proves that the two definitions of homotopy classes coincide.

The sphere-based convention is recorded in [Kerodon, Construction 3.2.2.4](https://kerodon.net/tag/00VJ); the topology prerequisite identifies its geometric sphere with the ordinary \(n\)-sphere. Our horn proof supplies the groups in that convention. Their further abelianness property for \(n\geq2\) is not needed for the one-type argument.

## 5. The adjunction and homotopy one-types

### 5.1. A presentation that works before Kan replacement

For any simplicial set \(A\), define a groupoid \(P_1(A)\) by generators and relations. Its objects are \(A_0\). Give it a generating arrow \(\langle a\rangle:d_1a\to d_0a\) for every \(a\in A_1\), freely adjoin inverses, and impose
\[
\langle s_0x\rangle=1_x,\qquad
\langle d_1\tau\rangle
=\langle d_0\tau\rangle\langle d_2\tau\rangle
\quad(\tau\in A_2).
\tag{5.1}
\]
Concretely its arrows are finite words of edges and inverse edges with matching endpoints, modulo these equations and the groupoid equations. This construction exists as a quotient of the free groupoid on the directed edge graph. It is functorial in \(A\).

**Lemma 5.1.** There is a natural bijection
\[
\operatorname{Hom}_{\mathrm{sSet}}(A,N(G))
\cong\operatorname{Hom}_{\mathrm{Gpd}}(P_1(A),G)
\tag{5.2}
\]
for every simplicial set \(A\) and every groupoid \(G\). If \(A\) is Kan, \(P_1(A)\) is naturally isomorphic to \(\Pi_1(A)\).

**Proof.** A simplicial map \(A\to N(G)\) assigns objects and arrows in \(G\) to vertices and edges. Degenerate edges become identities, and a two-simplex gives exactly the second relation in (5.1). Thus it gives a groupoid functor out of \(P_1(A)\).

Conversely a functor \(F:P_1(A)\to G\) sends an \(n\)-simplex to the string in \(G\) obtained from its \(n\) consecutive edges. Every nonconsecutive edge in that simplex is the composite of the intervening edges: apply (5.1) to each triangle on three of its vertices and induct on the distance between the outside vertices. A repeated vertex contributes a degenerate edge and hence an identity. Consequently restriction along any \(\alpha:[m]\to[n]\) gives precisely the string assigned to \(\alpha^*\tau\). Thus the prescription is a simplicial map. The two constructions undo one another on vertices and edges; nerve simplices are determined by their consecutive edges, so they undo one another in every degree. This proves (5.2) and its naturality.

Suppose \(A\) is Kan. Send each generator \(\langle a\rangle\) to \([a]\) in \(\Pi_1(A)\). The relations (5.1) hold by its identity and product constructions, so this gives a functor \(P_1(A)\to\Pi_1(A)\). Conversely send \([a]\) to \(\langle a\rangle\). A right homotopy has third edge an identity, so its triangle relation in (5.1) identifies its other two edges. Hence this assignment is well-defined. A product triangle proves that it preserves composition. The two functors are inverse on objects and on edges; every arrow of \(P_1(A)\) is a word in those generators, and every arrow of \(\Pi_1(A)\) is an edge class. They are therefore inverse functors. \(\square\)

This presentation also shows exactly why the fundamental groupoid only uses vertices, edges and triangles. Higher simplices impose compatibility among existing triangle relations, rather than new generators of \(P_1\).

**Proposition 5.2.** The fundamental-groupoid functor on Kan complexes is left adjoint to the nerve functor on groupoids:
\[
\operatorname{Hom}_{\mathrm{Gpd}}(\Pi_1(K),G)
\cong\operatorname{Hom}_{\mathrm{sSet}}(K,N(G)).
\tag{5.3}
\]
Here the right-hand side consists of ordinary simplicial maps, with no quotient by homotopy.

**Proof.** Proposition 3.1 places \(N(G)\) in the full category of Kan complexes. Apply Lemma 5.1 and its natural isomorphism \(P_1(K)\cong\Pi_1(K)\). The constructions there provide both directions and naturality in \(K,G\). \(\square\)

The unit is the map
\[
\eta_K:K\longrightarrow N(\Pi_1K)
\tag{5.4}
\]
which sends a simplex to its string of successive edge classes. The counit \(\Pi_1N(G)\to G\) is an isomorphism: a right homotopy in \(N(G)\) forces its two edges to be equal, since the other edge is an identity, and products are the original products in \(G\). These descriptions also verify the adjunction identities directly. The unit does not require choosing a preferred filler for any horn.

### 5.2. A Kan replacement and the triangle boundary

The notation \(\Pi_1(K)\) above was introduced for Kan complexes. For a simplicial set that is not Kan, Lemma 5.1 supplies \(P_1(A)\); here is an actual Kan replacement and the proof that it gives the same fundamental groupoid up to equivalence.

Starting from \(A^{(0)}=A\), define \(A^{(r+1)}\) by adjoining a copy of \(\Delta[n]\) for every horn map \(\Lambda^k[n]\to A^{(r)}\), glued along that map. These are pushouts of sets of horn inclusions, hence monomorphisms \(A^{(r)}\hookrightarrow A^{(r+1)}\). Put
\[
A^{\mathrm{Kan}}=\bigcup_{r\geq0}A^{(r)}.
\tag{5.5}
\]
A horn has finitely many nondegenerate simplices, so a horn map into this union factors through one finite stage. Its filler is added at the next stage. Thus \(A^{\mathrm{Kan}}\) is Kan.

Each horn attachment induces an equivalence on \(P_1\). In dimension one it adds one vertex and an edge connecting it to an old vertex; in the presented groupoid this adds a new object isomorphic to an old one, with no new endomorphism relation. In dimension two it adds a missing edge together with the equation determining that edge by the two existing edges and their inverses. Eliminating this generator and equation changes no old arrows. In dimension three it adds the missing triangle relation, which already follows from the other three relations by cancellation in a groupoid. To check this last assertion, anchor at the vertex opposite the missing face: the three supplied triangles express every edge \(ij\) as \(a_ja_i^{-1}\), exactly as in (3.3), so the missing triangle equation holds too. In dimensions at least four the horn already contains all vertices, edges and triangles; no presentation data change.

For a simultaneous set of attachments the same arguments apply: newly introduced one-dimensional vertices are separate, each missing two-dimensional edge has its own eliminating equation, and the remaining attachments add no relation not already forced. For the countable union, every arrow word and every finite chain of presentation relations occurs in some finite stage. Hence old arrows are neither lost nor newly identified. Every new object is isomorphic through finitely many stages to an original object. We obtain
\[
P_1(A)\simeq P_1(A^{\mathrm{Kan}})
\cong\Pi_1(A^{\mathrm{Kan}}).
\tag{5.6}
\]
The first comparison is an equivalence of groupoids; it need not be an isomorphism on object sets.

This is also a weak Kan replacement in the ordinary topological sense. Realization commutes with these pushouts. The explicit deformation in (3.6), on each attached simplex and fixed on its horn, gives a strong deformation retraction of each realized stage onto the preceding one. For simultaneous attachments these homotopies agree on the glued old space. We use the ordinary CW-space facts that realization has one cell for each nondegenerate simplex, that a compact subset of a CW-space lies in a finite subcomplex, and that the usual cellwise homotopies are continuous in compactly generated topology. A map from a sphere, or a homotopy from a compact cylinder, into the union therefore occurs at a finite stage. Retraction through finitely many stages proves that \(|A|\to|A^{\mathrm{Kan}}|\) induces the isomorphisms on all homotopy groups and the bijection on components required for a weak homotopy equivalence. These elementary topology prerequisites are the only geometric inputs to this replacement argument.

For \(A=\partial\Delta[2]\), the presentation has vertices \(0,1,2\) and three nondegenerate edges \(a:0\to1,b:1\to2,c:0\to2\). There is no nondegenerate triangle. Degenerate triangles give only identity laws. Choose \(a,b\) as a spanning tree. Transport every object to \(0\) using the tree; the remaining loop is
\[
\gamma=c^{-1}ba:0\longrightarrow0.
\tag{5.7}
\]
It satisfies no further relation. Every closed edge word reduces to a word in \(\gamma,\gamma^{-1}\): replace \(c\) using (5.7), and cancel consecutive inverse tree arrows. Such a reduced word is \(\gamma^m\), and the exponent map sends it to \(m\in\mathbb Z\); conversely \(m\mapsto\gamma^m\) is an inverse. Thus
\[
\Pi_1((\partial\Delta[2])^{\mathrm{Kan}})
\simeq \text{the one-object groupoid }\mathbb Z.
\tag{5.8}
\]
Each of its vertex automorphism groups is \(\mathbb Z\), and it has one isomorphism class of objects.

Its realization before replacement is the boundary of a geometric triangle, homeomorphic to a circle. The topology calculation agrees: lift a based circle loop to \(\mathbb R\) under \(t\mapsto e^{2\pi it}\), starting at \(0\). Its endpoint is an integer, unchanged under based homotopy, and concatenation adds endpoints. A loop with zero endpoint has a closed lift, contracted by linear homotopy in \(\mathbb R\). The loops \(t\mapsto e^{2\pi imt}\) give every integer. This proves the ordinary \(\pi_1(S^1)=\mathbb Z\) comparison.

### 5.3. Horn attachments and the Kan Whitehead theorem

We prove the comparison needed for the one-type theorem directly from the face groups of §4.4. We retain every component and basepoint, and construct the factorization and inverse homotopies rather than assuming a model-category comparison.

#### Cycles, prisms and horn attachments

Write \(I=\Delta[1]\). If \(K\) is Kan and \(x\in K_0\), let \(e_j(x)\) be its constant \(j\)-simplex. For \(n\geq1\), a cycle is
\[
a\in K_n,\qquad d_i a=e_{n-1}(x)\quad(0\leq i\leq n).
\tag{5.11}
\]
Its class is unchanged by a simplex \(H(a,b)\in K_{n+1}\) with
\[
d_iH=e_n(x)\ (i<n),\qquad d_nH=b,\quad d_{n+1}H=a.
\tag{5.12}
\]
The earlier group-axiom proof shows that this is an equivalence relation and gives \(\pi_n(K,x)\). Its product \([b][a]=[c]\) is specified by a horn filler with final faces \(b,c,a\) and all preceding faces constant. Components are vertex classes generated by edges.

A monomorphism is called **anodyne** here if it is built from horn inclusions by pushouts, compositions indexed by ordinals, and retracts. A Kan fibration lifts against every such map, by extending over the successive horn attachments; at a limit the already compatible maps form the required map on the union.

We need two cylinder facts, and give their combinatorics.

**Lemma 5.3a.** For a monomorphism \(A\subset B\), the inclusion
\[
(A\times I)\cup(B\times\{\epsilon\})\ \subset\ B\times I
\tag{5.13}
\]
is anodyne, for either endpoint \(\epsilon\). If \(A\subset B\) is anodyne, then
\[
(A\times I)\cup(B\times\partial I)\ \subset\ B\times I
\tag{5.14}
\]
is anodyne.

**Proof of (5.13).** A monomorphism is built by attaching its missing nondegenerate simplices along their boundaries, in order of dimension. It suffices to treat \(\partial\Delta[m]\subset\Delta[m]\). The prism has the \(m+1\) maximal simplices
\[
P_i=((0,0),\ldots,(i,0),(i,1),\ldots,(m,1)),
\qquad 0\leq i\leq m.
\]
Starting from the bottom and all sides, attach \(P_m,P_{m-1},\ldots,P_0\). At step \(i\), every face except the face omitting \((i,0)\) is present. The other face not contained in a side is already supplied by \(P_{i+1}\), or is the bottom when \(i=m\). Thus each attachment is a horn attachment. For the top endpoint reverse the order. This also covers \(m=0\). Pushouts and successive attachments prove (5.13).

For (5.14), first take \(A=\Lambda^k[m]\), \(B=\Delta[m]\), with \(m\geq1\). Initially both ends and every side except
\[
F=d_k\Delta[m]\times I
\]
are present. The boundary of this missing side is present. Write its prism simplices as \(Q_0,\ldots,Q_{m-1}\), using the ordered vertices with \(k\) omitted. Attach \(Q_{m-1},\ldots,Q_1\); each has one unfilled diagonal face, so this is again the bottom-to-top horn construction, stopped before \(Q_0\).

If \(k>0\), now attach \(P_m,P_{m-1},\ldots,P_0\). For \(i\ne k\), the missing-side face of \(P_i\) is \(Q_i\) if \(i<k\), and \(Q_{i-1}\) if \(i>k\). All these faces except \(Q_0\) are present. For \(i=k\) there is no such face: the vertex \(k\) occurs twice. Each step through \(P_1\) consequently has precisely its next diagonal face unfilled. At \(P_0\), that diagonal and the top are present and its sole unfilled face is \(Q_0\). If \(k=0\), use instead the order
\[
P_m,\ldots,P_2,\ P_0,\ P_1.
\]
The first steps have their next diagonal face missing; \(P_0\) supplies the remaining diagonal, and \(P_1\) then has just \(Q_0\) missing. For \(m=1\), this order means \(P_0,P_1\). These lists check every exceptional end case and supply all the missing prism.

Thus (5.14) holds for a horn inclusion. Taking a pushout of horn inclusions gives the corresponding pushout of these cylinder attachments. Products with \(I\) preserve these colimits. Compositions and retracts preserve the conclusion, proving (5.14). \(\square\)

It follows from (5.13) that a homotopy into a Kan complex defined on a subcomplex extends when its initial map is defined on the whole complex. It follows from (5.14) that two fillers of a given horn into a Kan complex are homotopic relative that horn: prescribe them at the two ends and hold the horn constant. The same assertion applies to fillers over a fixed simplex through a Kan fibration.

**Lemma 5.3b (the face relation and a relative prism).** Two cycles (5.11) are related by (5.12) if and only if their maps \(\Delta[n]\to K\) are simplicially homotopic, fixing the whole boundary at \(x\). A finite sequence of relative prism homotopies gives the same relation.

**Proof.** Realize a simplex (5.12) on the last prism simplex \(P_n\) of \(\Delta[n]\times I\). Its bottom face is \(a\), and its face shared with \(P_{n-1}\) is \(b\). Put \(s_i b\) on \(P_i\) for \(i<n\). The two diagonal faces of \(s_i b\) are both \(b\); every other face is constant. These assignments agree on all intersections and give a prism homotopy from \(a\) to \(b\) with constant sides.

Conversely, in a relative prism homotopy, all the diagonal \(n\)-faces are cycles. Each prism simplex has two possibly nonconstant faces, at adjacent indices \(i,i+1\); call their values \(a,b\). Such a pair has the same class in (5.12). Here is an explicit way to move those two indices to the final two positions. If \(Q\) has \(d_iQ=a,d_{i+1}Q=b\) and its other faces constant, with \(i<n\), prescribe an \((n+2)\)-horn with
\[
d_iR=s_{i+1}a,\qquad d_{i+2}R=s_i a,\qquad
d_{i+3}R=Q,
\]
all other supplied faces constant, and omit \(d_{i+1}R\). The three supplied nonconstant intersections are \(a,a,e_n\); the face identities show that they agree. All other intersections are constant. Its missing face has nonconstant faces \(a,b\) at indices \(i+1,i+2\), and all other faces constant. Iteration reaches indices \(n,n+1\), where (5.12), with symmetry, applies. Along the prism the successive diagonal faces therefore all have the same class, including its two ends. Transitivity handles finitely many prisms. \(\square\)

For \(b=e_n\), there is also a direct contraction from (5.12). The ordinal map
\[
[n]\times[1]\longrightarrow[n+1],\qquad
(i,0)\mapsto i,\quad(i,1)\mapsto n+1
\]
pulls \(H(a,e_n)\) back to a homotopy from \(a\) to the constant map. All its sides are constant.

These constructions also give basepoint transport in the face definition. Given an edge \(u:x\to y\), prescribe that edge on every boundary point of a cycle's cylinder and its original cycle on the bottom. Lemma 5.3a extends it; the top is a cycle at \(y\). Its class is independent of the fillers: triangulate the cylinder as above and replace its horn fillers successively; (5.14) compares each replacement relative its horn, and Lemma 5.3b identifies the resulting classes. A two-horn joining two edges gives the same transport as their consecutive cylinders. A triangle homotopy of edges likewise gives the same transport, by its prism. Transport along an inverse edge reverses it. Thus this is an isomorphism
\[
u_*:\pi_n(K,x)\longrightarrow\pi_n(K,y)
\tag{5.15}
\]
depending only on the edge class in the preceding fundamental groupoid. The horn defining products can be transported by the same cylinders, so (5.15) is a group isomorphism. In degree one it is the usual conjugation of loops.

If \(H:f\simeq g\) is a simplicial homotopy, apply \(H\) to a cycle cylinder. The resulting based cylinder has boundary the edge \(H(x,-)\), and hence
\[
g_*=(H(x,-))_*\,f_*.
\tag{5.16}
\]
This explains the basepoint change rather than identifying different pointed groups without a map.

#### Filling arbitrary boundaries

**Lemma 5.3c.** A nonempty Kan complex \(F\) which has one component and zero \(\pi_n(F,x)\) for every vertex and \(n\geq1\) lifts every boundary inclusion \(\partial\Delta[m]\subset\Delta[m]\).

**Proof.** For \(m=0\), choose a vertex. For \(m=1\), its two prescribed vertices are in the same component. The fundamental groupoid argument converts an edge zigzag to an edge with those endpoints.

Suppose \(m\geq2\) and \(a\colon\partial\Delta[m]\to F\) is given. The horn \(\Lambda^m[m]\) is a simplicial cone with apex \(m\); the ordinal homotopy
\[
(i,0)\mapsto i,\qquad(i,1)\mapsto m
\]
contracts it to that apex while fixing the apex. It stays in the horn, since adding the apex cannot add the missing face. Compose this contraction with \(a\). Lemma 5.3a extends that homotopy from the horn to the whole boundary, starting with \(a\).

At its end the boundary is constant at \(x=a(m)\) on the horn. The remaining face is an \((m-1)\)-cycle \(c\) at \(x\). Its class is zero, so it has a simplex \(H(c,e_{m-1})\) by the face definition. The contraction following Lemma 5.3b makes that remaining face constant while fixing its boundary. Together with the constant horn this contracts the entire boundary map to \(x\), by finitely many simplicial prism homotopies.

The constant boundary extends over the whole simplex. Extend the boundary homotopy backwards across the simplex using (5.13) with the final endpoint. Its initial end is the required extension of the original \(a\). \(\square\)

This argument retains every face of an arbitrary boundary map. It does not assume at the outset that those faces are already constant.

#### Fibres of a Kan fibration

Let \(p:E\to B\) be a Kan fibration between Kan complexes and choose a vertex \(e\) above \(b\). Its fibre \(F_b\) is Kan: a horn there is a lifting problem over the constant simplex of \(B\).

The precise exactness facts we need are
\[
\pi_{n+1}(E,e)\longrightarrow\pi_{n+1}(B,b)
 \xrightarrow{\delta}\pi_n(F_b,e)
 \longrightarrow\pi_n(E,e)\longrightarrow\pi_n(B,b),
\qquad n\geq1.
\tag{5.17}
\]
Exactness here is exactness of pointed sets, which suffices below; the maps induced by inclusions and \(p\) are the already defined group homomorphisms.

To define \(\delta\) on an \(r\)-cycle \(\beta\) of \(B\), lift it with every face except \(d_r\) prescribed to be \(e_{r-1}(e)\). Write the lift as \(\alpha\). Its missing face \(\gamma=d_r\alpha\) is an \((r-1)\)-cycle in \(F_b\). Put \(\delta[\beta]=[\gamma]\).

This is well defined. Two lifts of the same simplex and horn are joined over that simplex by (5.14); restriction to the missing face and Lemma 5.3b give the same fibre class. A homotopy of base cycles has a relative prism by Lemma 5.3b. Lift it starting with \(\alpha\) and keeping the supplied horn constant, using (5.13) for that horn inclusion. Its missing faces give a fibre prism, so the result depends only on the base class. Maps of fibrations preserve these constructions, giving naturality.

Here are all three exactness checks in (5.17).

* A base cycle has zero boundary class exactly when its class comes from \(E\). One implication uses a lifted cycle, whose missing face is constant. Conversely, contract \(\gamma\) inside the fibre using \(H(\gamma,e_{r-1})\). This gives a homotopy of the whole boundary of \(\alpha\): hold its other faces constant. Lift that boundary cylinder across \(\Delta[r]\times I\) over the constant base simplex \(\beta\), by (5.13). Its final simplex is a cycle in \(E\) projecting to \(\beta\).
* A fibre cycle \(\gamma\) becomes zero in \(E\) exactly when it is a boundary from \(B\). If it becomes zero, take \(H(\gamma,e_n)\) in \(E\). Its image in \(B\) is a cycle: all its faces are constant because \(\gamma\) lies in the fibre. This simplex is itself the horn lift defining its boundary, with missing face \(\gamma\). Conversely any such horn lift, with all other faces constant, is \(H(\gamma,e_n)\) in \(E\), so \(\gamma\) becomes zero there.
* An \(E\)-cycle becomes zero in \(B\) exactly when its class comes from the fibre. Lift a relative prism contraction of its image, holding its boundary at \(e\), using (5.13). The final cycle lies in the fibre and Lemma 5.3b identifies its \(E\)-class with the original one. The opposite implication is immediate.

These are the cycle-level proofs of (5.17); no comparison with realization is used.

**Lemma 5.3d.** If \(p\) induces a bijection on components and isomorphisms on every positive group at every vertex, then every \(F_b\) is nonempty, connected and has zero positive groups.

**Proof.** The component bijection gives a vertex of \(E\) above the component of \(b\). Represent a path to \(b\) by an edge in the fundamental groupoid of \(B\). Horn lifting of that edge, starting at the chosen \(E\)-vertex, produces a vertex over \(b\). Thus the fibre is nonempty.

Any two vertices \(u,v\) of \(F_b\) have the same component in \(E\), by injectivity on components. Choose an edge \(c:u\to v\). The class of \(p(c)\) is a loop at \(b\). Surjectivity of \(\pi_1(E,u)\to\pi_1(B,b)\) supplies a loop at \(u\) with that image. Composing its inverse with \(c\) gives an edge \(c'\) whose projection is null as a loop. Lift its base prism contraction, fixing both endpoints \(u,v\), by (5.13). The last edge lies in \(F_b\) and joins those vertices. This proves connectedness.

At any vertex \(e\) of the fibre, injectivity of \(\pi_n(p)\) says that the image of \(\pi_n(F_b,e)\) in \(\pi_n(E,e)\) is zero. Surjectivity of \(\pi_{n+1}(p)\) and the first exactness check say that \(\delta\) in (5.17) has zero image. The second check therefore says that the fibre-to-\(E\) map has zero kernel. Together these assertions force \(\pi_n(F_b,e)=0\) for every \(n\geq1\). \(\square\)

**Lemma 5.3e.** A Kan fibration with the fibres in Lemma 5.3d lifts every boundary inclusion.

**Proof.** Consider a simplex \(b:\Delta[m]\to B\) and a lift of its boundary. Pull the fibration back over that simplex. Contract \(\Delta[m]\) to vertex \(0\) using the ordinal homotopy
\[
(i,0)\mapsto0,\qquad(i,1)\mapsto i.
\]
Lift this contraction on the prescribed boundary, starting at its final end. This is possible by (5.13) for the endpoint inclusion of the boundary cylinder. At the other end we have a boundary map into the fibre over \(b(0)\). Lemma 5.3c fills it in that fibre. We now have a lifted bottom and all sides over the simplex's contraction. Apply (5.13) once more, this time to \(\partial\Delta[m]\subset\Delta[m]\), to fill the cylinder. Its final end fills the original boundary over \(b\). For \(m=0\) the nonempty-fibre assertion directly gives the lift. \(\square\)

#### Whitehead for arbitrary Kan complexes

**Theorem 5.3f.** A simplicial map \(f:K\to L\) of Kan complexes is a simplicial homotopy equivalence if and only if it bijects components and, for every vertex \(x\) and \(n\geq1\), induces an isomorphism
\[
\pi_n(K,x)\longrightarrow\pi_n(L,f(x)).
\tag{5.9}
\]

**Proof.** Factor \(f\) as
\[
K\xrightarrow{i}E\xrightarrow{p}L
\tag{5.19}
\]
by adjoining horn fillers over \(L\). At each stage attach one copy of \(\Delta[m]\) for every commutative horn square over \(L\), with its horn identified with the given map to that stage. Repeat these stages countably. A horn has finitely many nondegenerate simplices, so any horn square into the union already belongs to a finite stage and receives its filler at the next stage. Thus \(i\) is anodyne and \(p\) is a Kan fibration. Since \(L\) is Kan, lifting first in \(L\) and then through \(p\) proves that \(E\) is Kan.

The map \(i\) is a homotopy equivalence. Extend the identity of \(K\) along \(i\) into the Kan complex \(K\), obtaining \(r:E\to K\) with \(ri=1\). The maps \(ir\) and \(1_E\) agree on \(K\). Put them at the two ends of \(E\times I\) and hold \(K\times I\) constant. By (5.14), this prescribed subcomplex extends into \(E\). Hence \(ir\simeq1_E\), fixing \(K\).

In particular \(i\) bijects components and induces isomorphisms on the actual groups, by Lemma 5.3b and (5.16). If \(f\) has (5.9), so does \(p\): first at vertices in \(i(K)\), then at all other vertices using the paths supplied by this relative homotopy and the transport (5.15). The same conclusion holds on components.

Lemmas 4 and 5 give boundary lifting for \(p\). Every monomorphism is built by adjoining nondegenerate simplices along their boundaries. Thus \(p\) lifts every monomorphism. Applied to \(\varnothing\subset L\), this supplies a section \(s:L\to E\). Applied to \(E\times\partial I\subset E\times I\), with endpoints \(sp,1_E\) and base map \(p\) constant along the cylinder, it supplies
\[
sp\simeq1_E,\qquad ps=1_L.
\]
Set \(g=rs:L\to K\). Restricting the first homotopy along \(i\) and composing with \(r\) gives \(gf\simeq ri=1_K\). Restricting \(ir\simeq1_E\) along \(s\) and composing with \(p\) gives \(fg\simeq ps=1_L\). This is the required simplicial homotopy equivalence.

Conversely a homotopy inverse gives a component inverse, and (5.16) identifies the two composites on positive groups with the identities through explicitly invertible basepoint transports. Hence (5.9) holds at every vertex. The empty case is included: a component bijection with an empty complex forces the other complex to be empty, and the sole map is an isomorphism. \(\square\)

This proof is independent of CW Whitehead, singular realization, and the realization homotopy groups. It uses only the preceding face groups and the horn arguments written here.

### 5.4. Groupoids are homotopy one-types

A simplicial map is a homotopy equivalence if it has a simplicial map in the reverse direction whose two composites are homotopic to the identities. Here “homotopic” can be taken as the equivalence relation generated by (4.1); this is the convention in [Stacks, Tag 01A5]. For maps between Kan complexes it agrees with the usual simplicial homotopy convention.

**Proposition 5.3.** For a groupoid \(G\), \(N(G)\) has no higher homotopy groups: \(\pi_n(N(G),x)=0\) for all \(n\geq2\). A Kan complex \(K\) is homotopy equivalent to a groupoid nerve if and only if these groups vanish for \(K\), at every vertex. If they vanish, its natural unit (5.4) is such an equivalence.

**Proof.** An \(n\)-cycle in a nerve with \(n\geq2\) has every face constant. For \(n=2\), its three edges are consequently identities. For \(n>2\), any consecutive edge is contained in a proper face and is again an identity. A nerve simplex is determined by its consecutive edges, so the cycle is the constant simplex. Thus its cycle set is a singleton and its higher groups vanish.

The map \(\eta_K\) leaves objects unchanged and sends an edge to its homotopy class. Under \(\Pi_1N(\Pi_1K)\cong\Pi_1K\), its induced functor on fundamental groupoids is the identity. It therefore induces a bijection on \(\pi_0\) and an isomorphism on every \(\pi_1\). If all higher groups of \(K\) vanish, the preceding paragraph says it also induces isomorphisms on those groups, both sides being zero. Whitehead gives the homotopy equivalence. This argument includes the empty complex, for which the unit is already an isomorphism.

Conversely a homotopy equivalence to a groupoid nerve induces the isomorphisms (5.9) by the reverse implication of Theorem 5.3f, so all higher groups vanish. \(\square\)

A **homotopy one-type** means precisely a Kan complex with this vanishing in degrees at least two. It need not be connected, and its fundamental groups can be nonabelian. For a group \(G\) as a one-object groupoid,
\[
N(G)_n=G^n,\qquad
\pi_0(N(G))=\{*\},\qquad\pi_1(N(G),*)=G.
\tag{5.10}
\]
Its higher groups vanish by Proposition 5.3. This is the classifying simplicial set, often denoted \(BG\).

For the singular complex of the circle, Lemma 4.1 identifies edge homotopy with ordinary path homotopy relative endpoints: a singular triangle gives such a homotopy by (4.5), while any continuous square homotopy restricts to its two triangles and hence gives the same relation. A continuous path homotopy is exactly such a continuous square. Composition through a triangle agrees with path concatenation up to that relation, since the two successive sides and the direct side are homotopic within the geometric triangle. Thus \(\Pi_1\operatorname{Sing}(S^1)\) is the ordinary fundamental groupoid of the circle, with every point as an object and automorphism group \(\mathbb Z\) at each point. It is equivalent to the one-object groupoid \(\mathbb Z\).

Its higher groups vanish directly in our face definition. After choosing the base point as \(1\), an \(n\)-cycle \(a:|\Delta[n]|\to S^1\), \(n\geq2\), lifts to \(\widetilde a:|\Delta[n]|\to\mathbb R\). Choose its lift to be zero at one boundary point. Since the boundary is connected and \(a\) is constant there, the lift is zero on the whole boundary. On \(\partial|\Delta[n+1]|\), prescribe \(\widetilde a\) on the last face and zero on all other faces. These values agree on intersections. Extend this real-valued map to the simplex by coning to value zero at its barycentre: on the segment from the barycentre to a boundary point, interpolate linearly. Continuity at the barycentre follows from boundedness of the boundary values. Exponentiating gives a singular \((n+1)\)-simplex with faces \(d_i=e_n\) for \(i\leq n\) and \(d_{n+1}=a\), which is \(H(a,e_n)\). Thus every higher cycle is null, and Proposition 5.3 applies without an additional comparison theorem.

## 6. From stacks in groupoids to higher descent

### 6.1. Descent of one-types

Return to the site in Lesson 4. For simplicity suppose its objects have fibre products, as in the usual étale and fppf sites. Write \(F(U)\) for a groupoid-valued presheaf, with the usual coherent pullback isomorphisms understood if it is presented as a category fibred in groupoids. Each nerve \(N(F(U))\) is an objectwise Kan one-type.

For a cover \(\{U_i\to U\}\), let \(U_{ij}=U_i\times_UU_j\) and similarly for triple intersections. The descent groupoid has objects
\[
x_i\in F(U_i),\qquad
\alpha_{ij}:x_j|_{U_{ij}}\xrightarrow{\sim}x_i|_{U_{ij}},
\qquad
\alpha_{ij}\alpha_{jk}=\alpha_{ik}\text{ on }U_{ijk},
\tag{6.1}
\]
with \(\alpha_{ii}=1\). Its arrows are families \(\beta_i:x_i\to x_i'\) satisfying
\[
\alpha_{ij}'\beta_j=\beta_i\alpha_{ij}.
\tag{6.2}
\]
The stack condition is that restriction from \(F(U)\) to this descent groupoid is an equivalence, for every cover.

The nerve of this descent groupoid is the one-type model of the homotopy limit of the cover's Čech diagram of nerves. The content can be read directly from that diagram. Degree zero chooses the \(x_i\). Degree one chooses paths between their restrictions, which in a groupoid nerve are the \(\alpha_{ij}\). Degree two asks for triangles asserting the cocycle equation in (6.1). Higher compatibility is uniquely determined by the nerve's two-coskeletal property. Morphisms between these choices are precisely (6.2). Thus the homotopy-limit description retains the overlap isomorphisms and their compatibility, rather than replacing them by equality of local objects.

An equivalence of groupoids induces a homotopy equivalence of their nerves. Choose a quasi-inverse and the two natural isomorphisms. A natural transformation \(F\Rightarrow G\) defines a functor \(C\times[1]\to D\), and hence a homotopy \(N(C)\times\Delta[1]\to N(D)\), since nerves preserve this product. The quasi-inverse and these homotopies give the asserted equivalence. Conversely a functor inducing a homotopy equivalence of nerves is essentially surjective by its bijection on \(\pi_0\), and gives isomorphisms on all object automorphism groups by \(\pi_1\). It is fully faithful: for objects in the same component choose one arrow between them and identify every other arrow with it times an automorphism; for objects in distinct components there are no arrows on either side. Hence the two forms of descent condition agree.

For example, the groupoid of \(G\)-torsors on \(U\) is a one-type. A trivializing cover represents a torsor by transition elements \(g_{ij}\) with \(g_{ij}g_{jk}=g_{ik}\). Changing trivializations gives the compatible arrows in (6.2). A strict equalizer of sets of local objects would discard this gluing freedom. Passing to sets of isomorphism classes would also discard the automorphisms that control descent.

The appropriate phrase is therefore **sheaves of one-types with homotopy descent**. Merely having a presheaf with Kan values does not imply descent. Even a groupoid-valued presheaf can fail to glue local objects.

### 6.2. Allowing higher homotopies

To go beyond groupoids, allow Kan values with nonzero higher homotopy groups. Paths then have homotopies between them, those homotopies can have further homotopies, and descent must retain these coherences. The homotopy hypothesis motivates the use of spaces, or Kan models of them, as higher groupoids. The preceding one-type theorem proves its groupoid-level instance. We do not prove the general higher-dimensional hypothesis in this lesson.

Hypercoverings refine the Čech diagram by allowing independently chosen covers in successive matching degrees. They are the next tool for formulating and comparing higher descent; Lesson 12 develops that framework. The coskeleton in (1.9) explains the word “matching”: it packages the compatible lower-dimensional data to which a next simplex is to be attached.

There is also a linear simplicial theory. For a simplicial abelian group \(A\), its normalized chains can be written
\[
(NA)_n=\bigcap_{i=1}^n\ker(d_i:A_n\to A_{n-1}),
\qquad \partial=d_0.
\tag{6.3}
\]
The face identities give \(\partial^2=0\), since \(d_0d_0=d_0d_1\). The ordinary Dold–Kan theorem identifies simplicial abelian groups with nonnegative chain complexes by normalization and its inverse; its exact scope is [Stacks, Tag 019D]. This is a contextual algebraic input, not an ingredient in any proof above. Normalization \(N\) in (6.3) has a different domain and meaning from the category nerve \(N(C)\) in (2.1). Nonabelian fundamental groups already show why replacing general Kan complexes by chain complexes would lose information.

## 7. Exercises and complete solutions

### Exercise 7.1 — easy

Show directly that \(\Delta[1]\) is not Kan. Identify the missing edge in an unfillable horn.

**Solution.** Let the vertices of a two-horn be \(0,1,0\), prescribe its edge \(01\) to be the nonconstant edge \(0\to1\) of \(\Delta[1]\), and its edge \(02\) to be the identity at \(0\). These are the supplied faces \(d_2,d_1\) of \(\Lambda^0[2]\), with the correct common source. A filler would supply an edge \(12:1\to0\). But every one-simplex of \(\Delta[1]\) is an order-preserving map \([1]\to[1]\); none has values \(1,0\). Thus the horn has no filler. This is an outer horn, not the compositional inner horn.

### Exercise 7.2 — medium

Prove that the nerve of a groupoid is Kan, including higher-dimensional outer horns. Determine in which dimensions fillers are unique.

**Solution.** One-horns fill by identities at the supplied endpoints; other arrows may give further fillers. For a two-horn with edges \(a:0\to1,b:1\to2,c:0\to2\), whichever of these is missing is uniquely obtained from \(c=ba\), namely by composition or by \(b=ca^{-1}\) or \(a=b^{-1}c\).

For \(n\geq3\), suppose the missing face is opposite \(k\). The horn supplies every vertex, every edge and every triangle containing \(k\). Set \(a_k=1\); for \(i>k\) take \(a_i\) to be its edge \(ki\), and for \(i<k\) take the inverse of edge \(ik\). The supplied triangles give edge \(ij=a_ja_i^{-1}\). These formulas obey every triangle equation by cancellation:
\[
(a_\ell a_j^{-1})(a_j a_i^{-1})=a_\ell a_i^{-1}.
\tag{7.1}
\]
They give the functor \([n]\to G\) extending the horn. No other extension is possible, since its consecutive edges are prescribed. Thus every horn fills, uniquely for \(n\geq2\). Uniqueness in dimension one occurs only when the appropriate arrow choices happen to be unique; it is not part of the general theorem.

### Exercise 7.3 — medium

Prove the Segal bijections for a nerve, and reconstruct a category from a simplicial set with all Segal maps bijective. Explain why degree three is needed.

**Solution.** A functor \([n]\to C\) is determined by its consecutive arrows; every other arrow is their composite. Every composable string defines such a functor by associativity. This proves the Segal bijections.

Given \(K\) with the bijections, take \(K_0\) as objects and \(K_1\) as arrows, with source \(d_1\) and target \(d_0\). The identity at \(x\) is \(s_0x\). For \(a,b\) composable, the degree-two bijection gives the unique triangle with successive edges \(a,b\); define their composite to be its \(d_1\) edge. The triangles \(s_0a,s_1a\) give both identity laws.

For three arrows \(a,b,c\), the degree-three bijection gives the simplex with these consecutive edges. Its faces on \(012,123\) determine \(ba,cb\). Its faces on \(023,013\) express the edge \(03\) respectively as \(c(ba)\) and \((cb)a\); the face identities say these are the same edge. Thus composition is associative. An arbitrary simplex now corresponds to its consecutive-arrow string. Restricting to a triple proves every skipped edge is the expected composite, and a repeated vertex contributes an identity, so these correspondences commute with all simplicial operators. They give \(K\cong N(C_K)\).

Degree two defines a binary composition and identities. The degree-three compatibility is what proves its associativity; it cannot simply be left unstated.

### Exercise 7.4 — medium

Compute the fundamental groupoid of \(\partial\Delta[2]\) after Kan replacement, and compare it with the circle.

**Solution.** Use the horn-adjoining replacement (5.5), whose fundamental groupoid is equivalent to \(P_1(\partial\Delta[2])\) by the attachment argument. That presentation has three objects and the edges \(a:0\to1,b:1\to2,c:0\to2\), freely made invertible, without a nondegenerate triangle relation. The two edges \(a,b\) form a spanning tree. Moving all objects to \(0\) along it leaves the free loop \(\gamma=c^{-1}ba\). Every closed word reduces to a word in this generator and its inverse; there is no triangle which would impose \(\gamma=1\). Thus its automorphism group is the free group on one generator, identified with \(\mathbb Z\) by exponent.

The resulting groupoid is connected, with automorphism group \(\mathbb Z\) at every object, and is equivalent to the one-object groupoid \(\mathbb Z\). This is a groupoid computation: the set of objects need not become a singleton in the chosen replacement.

The realization of the original boundary is a circle. For a based circle loop lift to \(\mathbb R\) starting at \(0\). The endpoint integer is invariant under based homotopy, and concatenation adds integers. Zero endpoint means the lift is a closed path in \(\mathbb R\), contracted by linear interpolation. Every integer is realized by a loop of that winding number. Hence the circle has the same fundamental group \(\mathbb Z\). The filled simplex \(\Delta[2]\), in contrast, has the triangle relation \(c=ba\), which kills \(\gamma\).

### Exercise 7.5 — hard

Prove that \(\pi_1(K,x)\) is a group, including independence of composite representatives and associativity via three-horns.

**Solution.** A loop is an edge \(a:x\to x\). Identify \(a,b\) when a triangle has faces \(1_x,b,a\). Reflexivity is \(s_1a\). The three-horn with \(d_0=e_2,d_2=s_1a,d_3=H(a,b)\), missing \(d_1\), supplies \(H(b,a)\). The three-horn with \(d_0=e_2,d_1=H(b,c),d_3=H(a,b)\), missing \(d_2\), supplies \(H(a,c)\). Their supplied intersections agree as in (4.3), (4.4), so this is an equivalence relation.

Fill an inner two-horn for \(a,b\); if its third edge is \(p\), set \([b][a]=[p]\). For two fillers with third edges \(p,p'\), use \(d_0=s_1b,d_2=T(b,a;p'),d_3=T(b,a;p)\); the missing face \(d_1\) is \(H(p,p')\). To replace \(a\) by \(a'\), use \(d_0=s_0b,d_2=T(b,a;p),d_3=H(a,a')\); the missing \(d_1\) is \(T(b,a';p)\). To replace \(b\) by \(b'\), use \(d_0=H(b,b'),d_1=s_1p,d_3=T(b,a;p)\); the missing \(d_2\) is \(T(b',a;p)\). Their intersection triples are respectively \(b,b,a\), \(b,1_x,a\), and \(1_x,b,p\). These fillers prove independence of all choices.

For associativity choose triangles \(T(b,a;p),T(c,b;q),T(c,p;r)\). Prescribe these as \(d_3,d_0,d_1\) of a three-horn. The intersections for pairs \((0,1),(0,3),(1,3)\) are \(c,b,p\). Filling the missing \(d_2\) produces \(T(q,a;r)\). Therefore
\[
[c]([b][a])=[r]=([c][b])[a].
\tag{7.2}
\]
The class of \(s_0x\) is the unit, by \(s_0a,s_1a\). An outer two-horn with \(d_1=1_x,d_2=a\) gives a left inverse; the other outer horn with \(d_0=a,d_1=1_x\) gives a right inverse. Associativity makes them equal. We have proved every group axiom, and the group is precisely the automorphism group of \(x\) in \(\Pi_1(K)\).

## 8. Prerequisites and sources

All four assigned propositions are proved here: the Segal characterization and full faithfulness in Proposition 2.1, the groupoid-horn characterization in Proposition 3.1, the fundamental groupoid in Proposition 4.3, and the adjunction in Proposition 5.2. Lemmas 4.1 and 4.2 supply the relative-endpoint and independence details. Section 4.4 supplies the higher combinatorial groups; Proposition 5.3 proves the one-type assertion using the Whitehead theorem proved in §5.3. Every assigned exercise has a full solution.

The simplicial indexing, objects and representable sets are [Stacks, Tags 0163, 0164, 0169, 0174]. Truncation and coskeleton are [Stacks, Tags 017Z, 0AMA]. Trivial Kan lifting is [Stacks, Tags 08NK, 08NL, 08NM]; Kan lifting and its elementary closure properties are [Stacks, Tags 08NT, 08NU, 08NV, 08NW]. Homotopy and homotopy equivalence are [Stacks, Tags 019J, 01A5]. The contextual linear theorem is [Stacks, Tag 019D]. The assignment's Kan and trivial-Kan labels are corrected in Section 3.

The untagged nerve additions were checked in the public [AI Integrated Stacks Project source release, simplicial.tex](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/simplicial.tex). Their exact labels are section-nerves-categories, lemma-characterize-nerves-categories and lemma-nerve-groupoid-kan. They are cited by file and label. The primary Whitehead locator is [Kerodon, Theorem 3.2.7.1](https://kerodon.net/tag/00WV), with the homotopy-group convention in [Subsection 3.2.2](https://kerodon.net/tag/00VJ).

The ordinary topology inputs used in Section 5.2 are geometric realization's CW structure and pushout construction, continuity of the glued cell homotopies, and the finite-subcomplex property for compact subsets of CW-spaces. Path lifting for the universal cover of the circle is used for its example. The normalization and Dold–Kan correspondence belong to the genuine existing *The cotangent complex* assignment (AG-HP-12), §1, for simplicial modules and the correspondence needed for polynomial resolutions. Its current selected text imports that foundation; its complete programme proof is therefore still planned. It is not used in the one-type proofs here. The general higher homotopy hypothesis is motivation, not a theorem claimed here. Self-checked by the writing AI.

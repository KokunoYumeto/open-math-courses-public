# Stiefel–Whitney numbers and unoriented bordism

The Stiefel–Whitney numbers of a boundary vanish. This chapter proves the converse: a closed smooth manifold bounds a compact smooth manifold exactly when every one of those numbers is zero. Two manifolds of the same dimension are unoriented bordant exactly when their number lists agree. In degree zero the list is the single parity of the points.

The distinction between homology and homotopy is the central issue. A normal collapse turns characteristic numbers into cohomology evaluations. Their vanishing kills its homology class. To infer a null homotopy, we prove the mod-two one-group calculation, the complete stable square basis, a free Thom module theorem, and a finite homology-to-homotopy comparison with precise exponent hypotheses. The final proof uses an actual finite product of representing spaces in each manifold dimension.

| Step | Mathematical mechanism | Proof |
|---|---|---|
| Numbers to homology | Inverse tangent/normal series and normalized collapse pairing | B |
| Stable operation basis | Square stability, transgression and a reverse spectral comparison | A, I–L |
| Free Thom module | Faithful projective leading terms and a connected coalgebra argument | C–D, M |
| Homology to a boundary | Cellular representing maps, bounded comparison and Pontryagin–Thom | F–H, N |

All homology and cohomology in this chapter use \(F=\mathbf F_2\), unless another coefficient group is displayed. A closed manifold is smooth and compact, with no boundary. No orientation is required. The [geometric Thom chapter](thom-spaces-and-the-pontryagin-thom-construction.md) supplies the full unoriented correspondence, with normal rank \(k>n+1\), including its collapse inverse. The [universal real ring](schubert-cells-and-grassmannian-cohomology.md) is the exact Schubert calculation; Thom and evaluation normalizations are the [earlier Thom/Euler proof](thom-classes-and-euler-classes.md). The [existing squares](steenrod-squares-and-stiefel-whitney-classes.md) supply their higher diagonals, cochain identity, naturality, instability and Cartan formulas. The [homotopy foundation companion](homotopy-fibres-and-the-serre-spectral-sequence.md) and [one-group companion](rational-homotopy-and-the-hurewicz-range.md) supply first Hurewicz, CW models, covering and Serre foundations. We use the actual proved scopes and supply the further mod-two operation and comparison arguments here.

## A. Connecting maps and stable squares

Write \(\smile_i\) for the higher products of the squares chapter, with products of negative index zero. For cochains over \(F\) their proved differential identity is
\[
 d(a\smile_i b)=da\smile_i b+a\smile_i db
                 +a\smile_{i-1}b+b\smile_{i-1}a.
\tag{A.1}
\]
Here \(d\) is the cochain differential, not the degree of a cochain. On a degree-\(r\) cocycle, \(\operatorname{Sq}^s\) is represented by its product with itself of index \(r-s\), for \(0\leq s\leq r\).

**Lemma A.1 — Squares commute with a connecting map.** For a pair \((X,B)\), its cohomological connecting homomorphism
\[
 \delta:H^r(B;F)\longrightarrow H^{r+1}(X,B;F)
\]
satisfies \(\delta\operatorname{Sq}^s x=\operatorname{Sq}^s\delta x\) for every \(s\geq0\).

**Proof.** Extend a degree-\(r\) cocycle representing \(x\) on \(B\) to a cochain \(a\) on \(X\). Such an extension exists by assigning arbitrary, for instance zero, values to singular simplices not in \(B\); the singular simplices in \(B\) are a subset of the singular-simplex basis of \(X\). The cochain \(da\) vanishes on \(B\) and represents \(\delta x\).

First let \(0\leq s\leq r\) and put \(i=r+1-s\), so \(i\geq1\). In degree \(r+s\) define
\[
 b=a\smile_i da+a\smile_{i-1}a.
\tag{A.2}
\]
Its restriction to \(B\) is the cocycle \(a|_B\smile_{r-s}a|_B\), representing \(\operatorname{Sq}^s x\). Applying (A.1), the differential of its first summand is
\[
 da\smile_i da+a\smile_{i-1}da+da\smile_{i-1}a.
\]
The differential of the second summand is the sum of the last two terms: its two lower-index self-products cancel in characteristic two. Thus
\[
 db=da\smile_i da.
\tag{A.3}
\]
The right side represents \(\operatorname{Sq}^s\delta x\); the left side represents \(\delta\operatorname{Sq}^s x\). All relative assertions follow at the cochain level, since the right side vanishes on singular simplices in \(B\).

For \(s=r+1\), instability makes the left side zero. The right side is the class of \(da\smile_0 da\). Identity (A.1) with index zero gives
\[
 da\smile_0 da=d(a\smile_0 da).
\]
The primitive is itself relative because its second factor vanishes on \(B\). Hence this class is zero too. If \(s>r+1\), both sides vanish by instability. The argument includes \(r=0\). ∎

For a based CW complex use the reduced cone pair \((CX,X)\). The cone is contractible; its relative cohomology is reduced cohomology of the suspension, by the earlier CW-pair quotient and excision constructions. The connecting homomorphism is the suspension isomorphism, in nonnegative reduced degrees. Lemma A.1 therefore proves
\[
 \operatorname{Sq}^s(\Sigma x)=\Sigma(\operatorname{Sq}^s x).
\tag{A.4}
\]
Naturality includes the based quotient map used here. The top square of a suspended class is zero by the explicit relative primitive above; there is no conflict between stability and the unstable top-square formula. Iterating (A.4) makes every composition of the constructed squares a stable operation. This proves stability without citing an unproved transgression theorem or a presentation of the Steenrod algebra.

## B. Tangent numbers, normal numbers and the collapse

Let \(M^n\) be closed. Embed it in \(\mathbb R^{n+k}\) with \(k>n+1\), using the proved compact embedding theorem. Give its normal bundle \(\nu\) a metric, and let \(g:M\to BO(k)\) be its normal Gauss map. The ambient tangent bundle restricted to \(M\) splits as
\[
 TM\oplus\nu\cong\varepsilon^{n+k}.
\tag{B.1}
\]
Write \(t_j=w_j(TM)\) and \(v_j=w_j(\nu)=g^*w_j\), and put \(t_0=v_0=1\). The exact Whitney formula gives
\[
 \Bigl(\sum_{j\geq0}t_jz^j\Bigr)
 \Bigl(\sum_{j\geq0}v_jz^j\Bigr)=1.
\tag{B.2}
\]
The variable \(z\) is formal. Coefficients of every weight are finite expressions. Positive-degree cohomology vanishes above the manifold dimension, so high coefficients can also be discarded after evaluation on \(M\).

**Lemma B.1 — Changing tangent numbers to normal numbers.** The weight-\(n\) monomials in the \(t_j\) vanish on \([M]_2\) if and only if every weight-\(n\) monomial in the \(v_j\) vanishes there. In degree zero this condition means that the empty monomial has zero evaluation, namely that the number of points is even.

**Proof.** Solving the coefficient of \(z^r\) in (B.2) gives
\[
 v_r=\sum_{j=1}^r t_jv_{r-j}.
\tag{B.3}
\]
Consequently each \(v_r\) is a polynomial of weight \(r\) in \(t_1,\ldots,t_r\). Interchanging the two sequences in (B.2) gives the identical recursion expressing \(t_r\) in \(v_1,\ldots,v_r\). Substitution therefore expresses any monomial of weight \(n\) in either list as a finite \(F\)-linear combination of monomials of weight \(n\) in the other. Applying the linear evaluation functional proves both implications. For \(n=0\), no positive-weight substitution is needed and both lists have just the empty monomial. ∎

This is an invertible substitution in the formal polynomial ring with one generator of each positive weight. It is an involution, since the inverse of the inverse series is the original series. The first terms are
\[
 v_1=t_1,\quad v_2=t_1^2+t_2,\quad
 v_3=t_1^3+t_3,\quad
 v_4=t_1^4+t_1^2t_2+t_2^2+t_4.
\tag{B.4}
\]
The numerical criterion uses all monomials. A particular normal number need not equal the tangent number with the same indices.

Let \(MO(k)=T(\gamma_k\to BO(k))\) with its collapsed sphere-bundle basepoint. Its canonical Thom class is \(U_k\). For \(\alpha\in H^n(BO(k);F)\), denote its Thom image by \(\Phi\alpha\in\widetilde H^{n+k}(MO(k);F)\). The normal Gauss collapse is
\[
 c_M:S^{n+k}\longrightarrow MO(k).
\tag{B.5}
\]
It takes values in a finite canonical Thom stage, as in the proved construction. Denote the canonical mod-two sphere fundamental class by \([S^{n+k}]_2\).

**Lemma B.2 — The characteristic-number pairing of a collapse.** With these conventions,
\[
 \langle c_M^*\Phi\alpha,[S^{n+k}]_2\rangle
     =\langle g^*\alpha,[M]_2\rangle.
\tag{B.6}
\]

**Proof.** Factor the collapse through the Thom space of \(\nu\), followed by the bundle map classified by \(g\). Naturality of the Thom class makes the pulled-back class the Thom image of \(g^*\alpha\). It is enough to establish the evaluation for that first collapse.

Use a closed disk subbundle inside the normal tube and a smaller disk subbundle on which the collapse has its exact normal germ. Collapsing the complement sends the sphere fundamental class to the relative fundamental class of that disk bundle modulo its boundary. To check this assertion precisely, restriction to a point in the tube is the ambient mod-two local generator, because the tube map is a diffeomorphism there. Excision identifies that local class with the disk-bundle local class. The relative fundamental class is characterized by these local generators; the compact manifold-with-boundary construction and uniqueness proved earlier therefore give the stated image. A radial rescaling or plateau in the chosen collapse changes neither this local degree nor its homotopy class.

The homological Thom map is cap with \(U_\nu\), followed by projection to \(M\). It carries that relative disk-bundle fundamental class to \([M]_2\). Indeed, on a coordinate trivialization the class is the product of the base local fundamental class and the fibre relative generator, and the cap formula evaluates the Thom generator on the fibre with value one. The local result is the base local fundamental class. Naturality of restrictions and uniqueness of the compact-set fundamental classes make these local calculations the global one. Thus the homology image is exactly \([M]_2\), with no undetermined scalar. The Thom cap evaluation identity now says that evaluation of \(\pi^*g^*\alpha\smile U_\nu\) on the relative disk-bundle class is evaluation of \(g^*\alpha\) on \([M]_2\). This is (B.6). No orientation sign remains over \(F\). ∎

Define the mod-two Hurewicz class of the collapse by
\[
 h_k(c_M)=(c_M)_*[S^{n+k}]_2
       \in\widetilde H_{n+k}(MO(k);F).
\tag{B.7}
\]

**Proposition B.3 — The exact homological reduction.** For \(k>n+1\), all tangent Stiefel–Whitney numbers of \(M\) vanish if and only if \(h_k(c_M)=0\).

**Proof.** The rank bound gives \(k>n\), so the universal ring theorem says that its weight-\(n\) component has basis all monomials \(w_{i_1}\cdots w_{i_r}\) with total index \(n\). There is no rank truncation of an index at most \(n\). The Thom isomorphism carries these monomials to a basis of \(\widetilde H^{n+k}(MO(k);F)\). By Lemma B.2 their evaluations on (B.7) are exactly the normal characteristic numbers. Lemma B.1 equates their simultaneous vanishing with vanishing of the tangent numbers.

For completeness, cohomology over a field separates homology classes of any chain complex: choose a basis of cycles modulo boundaries, extend its linear functionals to cycles, and assign zero to a complement of cycles. The resulting cochains vanish on boundaries and are cocycles; each nonzero homology class has a functional of value one. This is the field coefficient comparison already proved in the Thom chapter. Thus a homology class vanishes precisely when all its cohomology evaluations vanish. This proves the assertion, including degree zero. ∎

This proposition does not yet prove null-bordism. A Hurewicz class can vanish while a homotopy class is nonzero. The needed extra statement is injectivity of the stabilized mod-two Hurewicz map on the unoriented Thom homotopy groups. The full geometric theorem alone gives no such injectivity.

The product cylinder \(M\times[0,1]\) has boundary two copies of \(M\). Therefore \(2[M]=0\) in \(\mathcal N_n\). The stable normal collapse groups inherit this exponent-two property through the proved geometric correspondence and its suspension compatibility. An exponent-two group by itself can still have elements killed by a Hurewicz map; it is a coefficient fact for the later comparison argument, not a detection proof.

## C. Faithful admissible square words on a product of lines

A finite sequence \(I=(i_1,\ldots,i_r)\) of positive integers is called admissible if \(i_j\geq2i_{j+1}\) for \(1\leq j<r\). The empty sequence is admissible and denotes the identity. Set \(|I|=i_1+\cdots+i_r\). The word \(\operatorname{Sq}^I\) means composition in that order, with the rightmost square applied first.

For a nonempty admissible sequence put
\[
 e_j=i_j-2i_{j+1}\ (j<r),\qquad e_r=i_r.
\tag{C.1}
\]
All \(e_j\) are nonnegative and \(e_r>0\). Conversely a finite nonnegative sequence with last entry positive recovers the admissible sequence by
\[
 i_j=e_j+2e_{j+1}+\cdots+2^{r-j}e_r.
\tag{C.2}
\]
In particular
\[
 |I|=\sum_{j=1}^r(2^j-1)e_j,\qquad
 E(I):=\sum_{j=1}^r e_j=i_1-i_2-\cdots-i_r.
\tag{C.3}
\]

Take \(H^*((\mathbb RP^\infty)^N;F)=F[x_1,\ldots,x_N]\), with \(|x_j|=1\), as proved in the Schubert chapter. Order monomials lexicographically with \(x_1>\cdots>x_N\). Naturality, instability and the top-square normalization give \(\operatorname{Sq}x_j=x_j+x_j^2\). Cartan and repeated squaring then give
\[
 \operatorname{Sq}(x_j^{2^a})=x_j^{2^a}+x_j^{2^{a+1}}.
\tag{C.4}
\]
Thus, on a monomial whose individual exponents are powers of two, a square of degree \(s\) doubles a subset of the exponents whose sum is \(s\). Each allowed subset has coefficient one.

**Lemma C.1 — The leading monomial.** If \(N\geq E(I)\), the lexicographic leading monomial of \(\operatorname{Sq}^I(x_1\cdots x_N)\) has \(e_r\) initial exponents equal to \(2^r\), then \(e_{r-1}\) exponents equal to \(2^{r-1}\), and so on through \(e_1\) exponents equal to two; all its remaining exponents are one. Its coefficient is one.

**Proof.** Every term has exponents which are powers of two, by (C.4). A given variable can be doubled at most once at each of the \(r\) stages, so its largest possible final exponent is \(2^r\). To obtain that exponent on \(x_1\), the variable must be doubled at every stage. This prescribes, uniquely, its contribution of degree \(2^{r-j}\) to the operation \(\operatorname{Sq}^{i_j}\).

The iterated Cartan formula therefore says that the coefficient of \(x_1^{2^r}\), regarded as a polynomial in the other variables, is
\[
 \operatorname{Sq}^{j_1}\cdots\operatorname{Sq}^{j_r}
 (x_2\cdots x_N),\qquad j_s=i_s-2^{r-s}.
\tag{C.5}
\]
There is only one summand with that first exponent, because the complete doubling history of \(x_1\) is unique. The differences of consecutive \(j_s\) in (C.1) are the same \(e_s\) for \(s<r\), and the last is \(e_r-1\). Thus the residual sequence is nonnegative and admissible after trailing zero operations are removed. Its required number of variables is \(E(I)-1\), so the hypothesis allows it on the \(N-1\) remaining variables.

Induct on \(E(I)\). The empty residual case gives the unchanged product of the remaining variables. Otherwise the induction hypothesis makes (C.5) nonzero, describes its leading monomial and gives coefficient one. Hence a term with first exponent \(2^r\) really occurs and is lexicographically larger than every term with smaller first exponent. Applying the residual description places the remaining \(e_r-1\) largest exponents first, followed by the indicated lower groups. This proves the formula and its coefficient. The identity word has the original product and is the initial case. ∎

**Corollary C.2 — Independence.** For every \(q\geq0\) and \(N\geq q\), the images of all admissible words of degree \(q\) on \(x_1\cdots x_N\) are linearly independent over \(F\). Consequently those words are linearly independent as cohomology operations, and, by Section A, as stable operations.

**Proof.** Formula (C.3) gives \(E(I)\leq |I|=q\), so the leading-monomial lemma applies. Its ordered exponents recover every \(e_j\) by counting the occurrences of \(2^j\), and then recover \(I\) by (C.2). Distinct words therefore have distinct leading monomials. In a nonzero finite linear combination choose the largest of these leading monomials among its nonzero coefficients. A polynomial with smaller leading monomial cannot contain that term; hence it cannot cancel. The combination is nonzero. If a relation held as operations it would hold on this product, which it does not. Stability was proved in (A.4). ∎

For example the degree-three words \(\operatorname{Sq}^3\) and \(\operatorname{Sq}^2\operatorname{Sq}^1\), on a product of at least three line classes, have leading monomials
\[
 x_1^2x_2^2x_3^2x_4\cdots x_N,
 \qquad x_1^4x_2x_3\cdots x_N,
\tag{C.6}
\]
respectively. These leading terms already distinguish the two operations.

Corollary C.2 proves independence, not spanning. It does not assert that every word reduces to an admissible word, that every stable operation is generated by squares, or that the stable cohomology of \(K(F,r)\) has no additional classes. Those are precisely further statements needed to use this computation with the full stable-operation algebra.

## D. A coalgebra criterion for a free module

This section is algebraic and does not use the unresolved spanning statement. Let \(A=\bigoplus_{j\geq0}A_j\) be a connected graded bialgebra over \(F\). This means an associative unital algebra with an algebra-map coproduct \(\Delta_A:A\to A\otimes A\), a compatible counit \(\epsilon_A:A\to F\), and \(A_0=F\cdot1\). The usual coassociativity and counit identities are required. No antipode is needed for the following criterion.

Let \(C=\bigoplus_{j\geq0}C_j\) be a connected graded coalgebra, with counit \(\epsilon_C\), degree-zero element \(u\) of counit one, and \(C_0=F\cdot u\). Suppose \(C\) is a left \(A\)-module. Its coproduct must respect the diagonal action:
\[
 \Delta_C(ac)=\sum a'c'\otimes a''c'',
\tag{D.1}
\]
where \(\Delta_A(a)=\sum a'\otimes a''\) and \(\Delta_C(c)=\sum c'\otimes c''\). The counit is an \(A\)-module map, with the action on \(F\) given by \(\epsilon_A\). All tensor sums are finite on each particular element, by the definition of the algebraic tensor product. Let \(A_+=\ker\epsilon_A\).

**Theorem D.1 — Free-module criterion.** If the map
\[
 i:A\longrightarrow C,\qquad a\longmapsto au
\tag{D.2}
\]
is injective, then \(C\) is a free left \(A\)-module. More precisely, put \(Q=C/A_+C\), choose any graded linear section \(\sigma:Q\to C\) of its quotient map \(\pi\), and set
\[
 \phi:A\otimes Q\longrightarrow C,\qquad
 \phi(a\otimes x)=a\sigma(x).
\tag{D.3}
\]
Then \(\phi\) is an isomorphism of graded \(A\)-modules, with the ordinary left action on its first tensor factor.

**Proof of surjectivity.** The quotient \(Q\) is a trivial \(A\)-module: a positive-degree element acts as zero. Choose the section degree by degree using vector-space bases. In degree zero it sends \(\pi u\) to \(u\). For \(c\in C_n\), the difference \(c-\sigma\pi c\) belongs to \(A_+C\), and can be written as a finite sum \(\sum a_jc_j\) with each \(a_j\) of positive degree and each \(c_j\) of degree less than \(n\). Homogeneous components give this expression if the original expression was not homogeneous. Inductively all \(c_j\) lie in the image of \(\phi\); the term \(\sigma\pi c=\phi(1\otimes\pi c)\) does too. \(A\)-linearity proves that \(c\) lies in the image. The degree-zero assertion starts the induction.

**Proof of injectivity.** Consider
\[
 \gamma=(1\otimes\pi)\Delta_C\phi:
 A\otimes Q\longrightarrow C\otimes Q.
\tag{D.4}
\]
For a homogeneous \(x\in Q_d\), connectedness and the counit identities give
\[
 \Delta_C\sigma x=u\otimes\sigma x
          +\text{terms with second degree less than }d.
\tag{D.5}
\]
For \(d=0\), the formula is \(\Delta_Cu=u\otimes u\). For \(d>0\), its asserted component of second degree \(d\) follows by applying \(\epsilon_C\otimes1\); all other components have second degree below \(d\).

Apply (D.1) and then \(1\otimes\pi\). Since positive-degree elements of \(A\) act trivially after \(\pi\), only degree-zero second factors of \(\Delta_A(a)\) survive. Their sum is \(a\otimes1\), by the counit identity and connectedness of \(A\). Therefore
\[
 \gamma(a\otimes x)=i(a)\otimes x
             +\text{terms with second degree less than }d.
\tag{D.6}
\]
Filter both tensors by the degree of their second factor. On the successive quotient for second degree \(d\), formula (D.6) is \(i\otimes1_{Q_d}\), which is injective over the field. Any nonzero element of \(A\otimes Q\) is a finite sum; take its largest nonzero second degree. Its image at that degree is nonzero, so \(\gamma\) is injective. Since \(\gamma\) factors through \(\phi\), the latter is injective too. This proves the theorem. ∎

The filtration argument avoids an assumption of finite total dimension, a canonical choice of generators or an antipode formula. If every graded component of \(A\) and \(C\) is finite dimensional, the same is true of \(Q\), and the isomorphism gives a product identity for the formal dimension series. That optional consequence alone does not identify a topological homotopy group.

**The criterion over any field.** The same conclusion holds over an arbitrary field \(K\), with nonnegatively graded connected bialgebra and module coalgebra and the usual signed tensor convention. For homogeneous terms the compatibility is
\[
 \Delta_C(ac)=\sum(-1)^{|a''||c'|}a'c'\otimes a''c''.
\]
The other assumptions, including injectivity of \(a\mapsto au\), are unchanged. Choose a graded section of \(C\to C/A_+C\). The preceding degree induction proves surjectivity without using the characteristic. For injectivity apply \(1\otimes\pi\) to the displayed formula. Every term with \(|a''|>0\) vanishes in the second quotient factor. The remaining terms have \(|a''|=0\), so their signs are one; their leading second-degree component is exactly \(au\otimes x\). The same maximal-second-degree argument proves injectivity. Thus the criterion requires neither an antipode nor finite-dimensional graded pieces over any field. This is the field scope of the Milnor–Moore criterion presented in [Miller’s notes](https://math.mit.edu/~hrm/papers/cobordism.pdf), Proposition10.4.

## E. How the prerequisites fit together

The first four sections have established stable squares, the exact homological reduction, admissible-word independence and an algebraic freeness criterion. We now prove the additional pieces before applying them. Sections F–G supply cohomology representation and the finite exponent comparison. Section H records their dimension bounds. Sections I–L prove the mod-two one-group ring, stable spanning and the square bialgebra. Section M constructs the stable Thom coalgebra and verifies every hypothesis of D. Section N combines those proofs to establish the detection theorem. Thus neither an external operation-basis citation nor an unproved spectrum comparison closes a step of the argument.

## F. Representing a mod-two class by a map

Let \(r\geq2\), and choose the proved model \(K(F,r)\). It is \((r-1)\)-connected. First Hurewicz and the coefficient theorem identify \(H^r(K(F,r);F)\) with \(\operatorname{Hom}(F,F)\). Let \(\iota_r\) be the class corresponding to the identity homomorphism. Its value on a sphere representing the nonzero element of \(\pi_r\) is one.

**Theorem F.1 — Cohomology representation on CW complexes.** For a based CW complex \(X\), with its basepoint a vertex, pullback gives a bijection
\[
 [X,K(F,r)]_*\longrightarrow\widetilde H^r(X;F),
       \qquad [f]\longmapsto f^*\iota_r.
\tag{F.1}
\]
The bijection is natural for based maps. The domain denotes based homotopy classes, with homotopies fixed at the basepoint.

**Proof of existence.** Represent a class by a cellular degree-\(r\) cocycle \(a\). Send \(X^{r-1}\) to the basepoint. On every oriented \(r\)-cell, send its characteristic disk modulo its boundary to a based sphere map representing \(a(e)\in F=\pi_r(K(F,r))\). The characteristic weak topology makes these maps a continuous map on the \(r\)-skeleton, even when there are infinitely many cells.

Consider an \((r+1)\)-cell. Its attaching sphere maps into \(X^r\). Since our map is constant on \(X^{r-1}\), the resulting class in the target factors through the wedge \(X^r/X^{r-1}\) of \(r\)-spheres. On first homology, the attaching map has coordinates equal to the cellular boundary coefficients of that cell. Naturality of the first Hurewicz map in the \((r-1)\)-connected target then makes its image in \(\pi_r(K(F,r))\) equal to
\[
 a(\partial e)=0.
\tag{F.2}
\]
The last equality is the cocycle condition. Thus that attaching sphere contracts and the map extends over the cell. For all subsequent cells the attaching sphere dimension is greater than \(r\), and the corresponding target homotopy group is zero. Extend over them in order. The resulting map on \(X\) is continuous by the CW weak topology and remains based.

The pullback of \(\iota_r\) has the prescribed values \(a(e)\) on the \(r\)-cells by its sphere normalization, so represents the desired cohomology class. This uses the actual cellular/singular comparison and its naturality; a cell assignment alone is not being substituted for a singular cohomology class.

**Proof of uniqueness.** First every based map is based homotopic to one which is constant on \(X^{r-1}\). Proceed over that skeleton by increasing dimension. At a vertex choose a path to the basepoint; leave the distinguished vertex fixed. For each higher cell of dimension below \(r\), the boundary of its homotopy prism is a sphere in a dimension where the target homotopy group is zero. Fill it. Homotopy extension lets each completed skeletal homotopy extend to \(X\). The characteristic topology of the prisms, equivalently the proved quotient-times-interval construction, makes this a continuous homotopy. Thus it suffices to compare maps \(f_0,f_1\) constant on \(X^{r-1}\).

Their \(r\)-cell values are cellular cocycles \(a_0,a_1\). If the pulled-back classes agree, there is a cellular degree-\((r-1)\) cochain \(b\) such that
\[
 a_0+a_1=db.
\tag{F.3}
\]
Build a based homotopy on \(X\times[0,1]\), using its prism cells. On \(X^{r-2}\times[0,1]\) take the constant homotopy. On each prism of an \((r-1)\)-cell, its entire boundary is mapped to the basepoint; choose its quotient sphere map in dimension \(r\) with value \(b(e)\). The choices agree on shared prism faces.

For an \(r\)-cell prism, its attaching sphere has target class
\[
 a_0(e)+a_1(e)+b(\partial e)=0.
\tag{F.4}
\]
The first two contributions are its bottom and top faces, and the last is its side boundary. This is the cellular prism boundary formula; its orientation signs disappear over \(F\). As before, the first Hurewicz normalization of the target identifies these cell values with the sphere homotopy class. Equation (F.3) gives the zero in (F.4), so the homotopy extends over this prism. On all higher prisms the attaching sphere has dimension above \(r\) and therefore also contracts. These extensions yield a continuous based homotopy between the two maps. Conversely homotopic maps give equal pullbacks by singular homotopy invariance. This proves injectivity. Naturality follows from the definition by pullback and composition. ∎

The construction gives exactly the individual maps and their based uniqueness used below. No multiplication map on an ordinary product of arbitrary CW spaces is required for (F.1).

The loopspace \(\Omega K(F,r)\) has only \(\pi_{r-1}=F\), by cube currying. Its cohomology suspension takes \(\iota_r\) to the normalized class in degree \(r-1\): evaluation on a looped sphere equals evaluation on its adjoint \(r\)-sphere. Their mod-two values are both one. For \(r>2\), the first Hurewicz theorem identifies this normalization directly; for \(r=2\), first homology is the abelianization of \(\pi_1=F\), giving the same conclusion. The proved one-group comparison identifies the loopspace homology with that of \(K(F,r-1)\).

In particular a square word applied to \(\iota_r\) represents a map to the corresponding higher one-group space. The stability calculation in the preceding working part, Lemma A.1, determines its looped cohomology class. This observation is useful for the still-required path-fibration computation; it does not already prove that such words span all cohomology in the stable range.

## G. Mod-two homology comparison under exponent-two hypotheses

The following statement concerns spaces and a bounded degree range. Exponent two means that twice every element of the indicated abelian group is zero. It does not mean that the group has only two elements or is finite.

**Theorem G.1 — A finite comparison.** Let \(f:X\to Y\) be a based map of path-connected spaces. Assume \(X\) and \(Y\) are two-connected. Fix \(N\geq2\). Suppose

* \(\pi_j(X)\) and \(\pi_j(Y)\) have exponent two for \(2\leq j\leq N+1\);
* \(f_*:H_j(X;F)\to H_j(Y;F)\) is an isomorphism for \(0\leq j\leq N+1\).

Then \(f_*:\pi_j(X)\to\pi_j(Y)\) is an isomorphism for every \(j\leq N\).

**Proof.** First we may work with a map of CW complexes. If necessary take a based CW model \(Y'\to Y\), replace \(f\) by its path fibration, and pull that fibration back to \(Y'\). The map of total spaces is a weak equivalence, by the two homotopy long exact sequences: its base map is a weak equivalence and its fibre map is the identity. Take a based CW model of the pulled-back total space and map it to \(Y'\). Both the homotopy hypotheses and the homology hypothesis are preserved, by the proved weak-equivalence homology comparison. This construction does not assert that an ordinary product of arbitrary CW spaces is itself a CW complex. The new map and the old one induce the same homotopy and homology homomorphisms under these equivalences.

Replace this CW map by its proved path-fibration replacement. Its total space \(E\) is homotopy equivalent to its source, its base is a CW complex, and its fibre \(P\) is the homotopy fibre. The long homotopy sequence and two-connectedness make \(P\) path connected and simply connected: both \(\pi_1\) and \(\pi_2\) of the base vanish, as do the corresponding groups of the source. In the given degree range the sequence yields an exact sequence of abelian groups
\[
 \operatorname{coker}\bigl(\pi_{j+1}X\to\pi_{j+1}Y\bigr)
 \longrightarrow\pi_jP
 \longrightarrow\ker\bigl(\pi_jX\to\pi_jY\bigr),
\tag{G.1}
\]
where the first arrow is injective and the second surjective. Each outside group has exponent two. Therefore \(4\pi_jP=0\) for \(2\leq j\leq N\): twice an element maps to zero on the right, so belongs to the left subgroup, and twice more is zero.

If some \(\pi_jP\) with \(j\leq N\) were nonzero, let \(d\) be its first nonzero degree. Then \(d\geq2\), and the first Hurewicz theorem, applied to a CW model of \(P\), gives
\[
 H_i(P;\mathbb Z)=0\quad(0<i<d),\qquad
 H_d(P;\mathbb Z)\cong\pi_dP=:G.
\tag{G.2}
\]
The earlier weak-equivalence homology theorem justifies passing to that model. The coefficient theorem gives
\[
 H_i(P;F)=0\quad(0<i<d),\qquad
 H_d(P;F)=G/2G.
\tag{G.3}
\]
There is no lower-degree coefficient term in degree \(d\), by (G.2). The latter quotient is nonzero: if \(G=2G\), then \(G=4G=0\), contrary to the choice of \(d\). This uses the bounded exponent, and needs no finite-generation assumption.

Apply the already proved homology Serre spectral sequence to \(P\to E\to Y\), with coefficients \(F\). The base is simply connected, so its coefficient system in the fibre homology is constant. All rows strictly between zero and \(d\) vanish. In total degrees at most \(d+1\), the only differential from the bottom row which can reach a positive row is
\[
 d_{d+1}:H_{d+1}(Y;F)\longrightarrow H_d(P;F).
\tag{G.4}
\]
Indeed the homology differential has bidegree \((-s,s-1)\); a nonzero positive target row first requires \(s\geq d+1\), and the displayed source has just enough base degree. Neither of the displayed terms has any further outgoing differential; no other differential can enter the fibre term \((0,d)\).

The bottom-row edge in degree \(d+1\) has image \(\ker d_{d+1}\). Since \(H_{d+1}(E;F)\to H_{d+1}(Y;F)\) is surjective by hypothesis, this kernel is all the source and (G.4) is zero. The convergence filtration in total degree \(d\) has two possible nonzero pieces: its bottom-row piece \(H_d(Y;F)\), and its fibre piece \(H_d(P;F)/\operatorname{im}d_{d+1}\). The edge map in degree \(d\) is the projection onto the first. Its injectivity by hypothesis forces the second to be zero. Since (G.4) was zero, it follows that \(H_d(P;F)=0\), contradicting (G.3).

Thus \(\pi_jP=0\) for \(1\leq j\leq N\). The homotopy long exact sequence now gives injectivity of \(\pi_jX\to\pi_jY\) from \(\pi_jP=0\), and surjectivity from \(\pi_{j-1}P=0\), for all \(2\leq j\leq N\). The lower degrees were zero by connectivity. ∎

The two adjacent homology degrees are essential in this proof: surjectivity in degree \(d+1\) eliminates the transgression which could otherwise hide the first fibre group, and injectivity in degree \(d\) eliminates its remaining filtration piece. A single equality of homology dimensions would not supply both facts.

## H. The degree bounds for the Thom comparison

Fix a manifold dimension \(n\geq0\), and choose normal rank
\[
 k>n+3,
 \qquad N=n+k.
\tag{H.1}
\]
The Thom-cell theorem makes \(MO(k)\) \((k-1)\)-connected, hence at least two-connected. For degrees \(j\leq N+1\), its homotopy groups have exponent two: groups below \(k\) are zero; for \(j=k+m\) with \(0\leq m\leq n+1\), the geometric theorem applies because \(k>m+1\), and identifies the group with \(\mathcal N_m\). The product cylinder makes twice each such class zero.

The operation/module calculation in Sections K–M will provide finitely many classes
\[
 v_\alpha\in\widetilde H^{k+a_\alpha}(MO(k);F),
       \qquad 0\leq a_\alpha\leq n+1,
\]
whose one-group maps from Theorem F.1 give a map
\[
 v:MO(k)\longrightarrow
       \prod_\alpha K(F,k+a_\alpha)
\tag{H.2}
\]
inducing an isomorphism in mod-two cohomology through degree \(N+1\). Field duality then gives the required homology isomorphism in the same finite range: a map of vector spaces is bijective if its full dual map is bijective, since any nonzero kernel or cokernel admits a nonzero linear functional. The finite product in (H.2) is two-connected and has only exponent-two homotopy groups. Theorem G.1 therefore makes (H.2) an isomorphism on \(\pi_N\).

If the Hurewicz class of a normal collapse is zero, all the pullbacks of the \(v_\alpha\) to \(S^N\) are zero. Its composite with each factor of (H.2) is null by Theorem F.1, or by that factor's explicit homotopy groups. A map into a finite product is null when all its coordinate maps are null, using the product of their based homotopies. Thus its image in \(\pi_N\) under (H.2) is zero. Injectivity then makes the original collapse null, and the geometric Pontryagin–Thom theorem makes \(M\) a boundary.

Section N proves the finite-range cohomology isomorphism in (H.2), using the complete basis and free-module calculations of Sections K–M. The implication just established therefore applies there with all its premises verified. The space-level comparison above supplies exactly the required homotopy conclusion.
## I. Products and transgression over the field of two elements

### I.1. The multiplicative spectral sequence in the used scope

The complete proof of the rational companion, Section G, applies over \(F\) with the following precise changes. Suppose \(p:E\to B\) is a Hurewicz fibration with simply connected CW base, connected fibre, and finite-dimensional homology over \(F\) in each degree for both base and fibre. Then
\[
 E_2^{a,b}=H^a(B;F)\otimes H^b(F_p;F),\qquad
 d_s:E_s^{a,b}\longrightarrow E_s^{a+s,b-s+1}
\tag{I.1}
\]
is a multiplicative spectral sequence, with ordinary tensor-product cup product on page two. Every \(d_s\) is a derivation. It converges to the finite associated filtration of ordinary cohomology of \(E\). We write \(F_p\) for the fibre here to distinguish it from the coefficient field.

Here is an explicit verification of the change of coefficients; rational coefficients are not being treated as a provider for an unstated mod-two theorem. Filter singular chains over \(F\) by \(C_*(p^{-1}B^a;F)\), and filter their dual cochains by annihilators of the preceding level. Every linear functional on a subspace extends to the whole vector space. Splitting cycles and boundaries proves that homology of the dual complex is dual homology. Thus the relative disk calculation of the homology spectral sequence gives the cellular cochain complex with coefficient space \(H^b(F_p;F)\). Its finite dimension identifies this complex with a finite direct sum of base cochain complexes, giving (I.1).

For this decreasing filtration \(\mathcal F\), the actual page representatives are
\[
\begin{split}
 Z_s^{a,m}&=\{c\in\mathcal F^a C^m:dc\in\mathcal F^{a+s}C^{m+1}\},\\
 T_s^{a,m}&=\mathcal F^a C^m\cap d(\mathcal F^{a-s}C^{m-1}),\\
 E_s^{a,m-a}&=Z_s^{a,m}/(Z_{s-1}^{a+1,m}+T_{s-1}^{a,m}).
\end{split}
\tag{I.2}
\]
The kernel-and-image computation gives the differential \([c]\mapsto[dc]\) and the next page as its cohomology. Relative groups vanish in total degrees below the base cell dimension. Consequently, in each total degree the cohomology of the inverse-image skeleta stabilizes after finitely many levels. To check convergence to the whole space, restrictions of cochains are onto, and the sequence
\[
0\longrightarrow C^*(E)\longrightarrow\prod_a C^*(E_a)
\xrightarrow{D}\prod_a C^*(E_a)\longrightarrow0,
\qquad D(c)_a=c_a-\operatorname{res}c_{a+1},
\tag{I.3}
\]
is exact by successive lifting. Its cohomology sequence, and surjectivity of \(D\) on an eventually constant tower, identify cohomology of \(E\) with that stable value. This yields the finite filtration, without assuming that cohomology generally commutes with inverse limits.

For the product, use the weak CW product of the base with itself, whose cells are products of cells and whose skeleton is indexed by their total dimension. Singular simplices in this weak product and in the ordinary product are the same: their compact coordinate images lie in two finite subcomplexes. Pull the product fibration back to the weak product. The chain cross product is filtered by total base dimension. Its associated graded map is an isomorphism on homology, by the relative disk calculation and the field chain-complex splitting proof of the Künneth formula. The associated graded of its cone is therefore acyclic.

An exhaustively, nonnegatively filtered complex \(L\) over a field with acyclic associated graded has a filtered contraction. Split its filtration and write its differential as \(d=d_0+\epsilon\), where \(\epsilon\) lowers filtration. Choose a contraction \(h_0\) of each graded level. Then
\[
 dh_0+h_0d=1+T,\qquad T=\epsilon h_0+h_0\epsilon.
\]
The operator \(T\) lowers filtration, and commutes with \(d\). The series \((1+T)^{-1}=1+T+T^2+\cdots\) is finite on every chain. Hence \(h=h_0(1+T)^{-1}\) satisfies \(dh+hd=1\) and preserves filtration. Applying this to the cross-product cone supplies a filtered chain homotopy inverse. Neither this construction nor its cone block identities divide by two.

Cellularly approximate the base diagonal while fixing the reference vertex, and lift that homotopy into the product fibration starting from the ordinary total-space diagonal. Composing its endpoint with the filtered cross-product inverse gives a filtered chain diagonal. Evaluating two cochains on it defines a product \(\mu\) satisfying
\[
 d\mu(c,c')=\mu(dc,c')+\mu(c,dc'),\qquad
 \mu(\mathcal F^a,\mathcal F^{a'})\subset\mathcal F^{a+a'}.
\tag{I.4}
\]
Its unfiltered chain diagonal is homotopic to the ordinary Alexander–Whitney diagonal: both cross-product inverses are chain homotopic, and the lifted diagonal is homotopic to the ordinary one. Thus its final product is ordinary cup product. On the second page the relative disk degree and fibre diagonal give the tensor-product cup product. The signs in the rational calculation are all one over \(F\).

Finally (I.4) descends to (I.2). A change in \(Z_{s-1}^{a+1}\) contributes one higher filtration. For a boundary change \(dv\), with \(v\in\mathcal F^{a-s+1}\), write
\[
 \mu(dv,c')=d\mu(v,c')+\mu(v,dc').
\]
The first term is in the boundary denominator, and the second is in the higher-filtration cycle denominator because \(dc'\in\mathcal F^{a'+s}\). This also proves the higher-page derivation identity directly on representatives. Associativity and commutativity hold on page two and pass to its successive cohomology pages; strict associativity of the chosen chain diagonal is unnecessary. Naturality comes from the same filtered maps as in the homology construction. These steps verify every coefficient-dependent part of the stated theorem. The finite-type hypothesis for the one-group spaces follows from the complete finite-generation proof in the rational companion, Theorem F.6, and the integral coefficient sequence.

### I.2. A sufficient transgression criterion

Let \(b\) be the reference vertex, and let \(F_p=p^{-1}(b)\). Take \(x\in H^q(F_p;F)\), \(q\geq1\), and \(y\in H^{q+1}(B,b;F)\). If
\[
 \delta x=p^*y\quad\hbox{in }H^{q+1}(E,F_p;F),
\tag{I.5}
\]
then \(x\) survives to page \(q+1\), and its differential there is the bottom-row residue of the ordinary base class \(y\). Here \(\delta\) is the connecting map of the fibre pair, and positive-degree relative base classes are identified with ordinary ones.

To prove this, choose a relative cocycle \(z\) representing \(y\). Its restriction to \(B^q\) is exact, since a \(q\)-dimensional CW complex has no cohomology in degree \(q+1\). This assertion can be made relative to \(b\), which removes the sole degree-zero issue. Extend its primitive from \(B^q\) to \(B\), relative to \(b\), and subtract its differential from \(z\). Now \(z\) vanishes on \(B^q\). Extend a cocycle for \(x\) to a cochain \(c\) on \(E\). Equation (I.5) says \(dc+p^*z\) is a relative coboundary, so change \(c\) by its relative primitive. The corrected extension satisfies \(dc=p^*z\), still restricting to the original fibre cocycle. Its differential vanishes on \(E_q\). Formula (I.2) therefore makes it a page-\(q+1\) representative, and computes its differential as the indicated pullback of \(z\). Naturality for the map from this fibration to the identity fibration of \(B\) identifies that bottom-row residue with \(y\). Earlier differentials are zero. This proves the criterion and its normalization.

Naturality of squares and Lemma A.1 show that (I.5) persists after applying any square, and then any word of squares:
\[
 \delta\operatorname{Sq}^I x=p^*\operatorname{Sq}^I y.
\tag{I.6}
\]
The differential of a transgressive square word is consequently the residue of the same word on its chosen base witness. This statement includes a witness which has become zero modulo previous differentials.

In this paragraph use the reduced cone, collapsing the basepoint line as well as its cone tip. In a based path fibration \(\Omega B\to PB\to B\), criterion (I.5) has a concrete interpretation. Send \((\ell,t)\) in the cone of the loopspace to the initial segment \(s\mapsto\ell(ts)\), a path in \(B\). This gives a map of pairs \((C\Omega B,\Omega B)\to(PB,\Omega B)\), equal to the identity on the boundary. Both cone and path space contract to their basepoints, so their connecting maps are isomorphisms in these positive degrees. On quotients its projected map is the suspension evaluation \((\ell,t)\mapsto\ell(t)\). Therefore (I.5) holds exactly when the cohomology suspension of \(y\) is \(x\). For \(B=K(F,r+1)\), the sphere normalization proved in Section F makes this suspension send \(\iota_{r+1}\) to \(\iota_r\). It follows that every \(\operatorname{Sq}^I\iota_r\) has witness \(\operatorname{Sq}^I\iota_{r+1}\).

## J. Reverse comparison and a simple-generator calculation

### J.1. Reverse comparison of first-quadrant spectral sequences

Consider a map \(\phi:\mathcal E_s\to E_s\) of first-quadrant cohomological spectral sequences. Suppose each second page is a tensor product of its two axes, and the second-page map is the tensor product of its axis maps. If \(\phi\) is an isomorphism on the vertical second-page axis and on the limiting page, then it is an isomorphism on the horizontal second-page axis.

Here is a full proof of the direction used. Induct on the horizontal coordinate. Assume the horizontal second-page map is an isomorphism through coordinate \(k\); coordinate zero starts with the given vertical-axis isomorphism. For all vertical coordinates, page induction proves
\[
\begin{array}{ll}
\phi_s\text{ is an isomorphism}&\text{in columns }p\leq k-s+1,\\
\phi_s\text{ is injective}&\text{in columns }p\leq k.
\end{array}
\tag{J.1}
\]
For \(s=2\) this follows from the tensor-product hypothesis. To pass from \(s\) to \(s+1\), write \(Z_s=\ker d_s\) and \(B_s=\operatorname{im}d_s\), at the relevant position. In a column \(p\leq k-s\), the map on the source term is an isomorphism, and that on its outgoing target in column \(p+s\leq k\) is injective. The map on \(Z_s\) is therefore an isomorphism. In columns \(p\leq k-s+1\), the target term is an isomorphism and the incoming source in column \(p-s\) is an isomorphism; hence the map on \(B_s\) is an isomorphism. Their quotient is an isomorphism for \(p\leq k-s\), giving the next isomorphism bound.

For the injectivity bound, \(Z_s\) injects in columns \(p\leq k\). The map on \(B_s\) is surjective for \(p\leq k+1\): its incoming source has coordinate \(p-s\leq k-s+1\), in the isomorphism range. If a cycle maps to a boundary, lift that boundary and use injectivity on the cycle term to subtract it. Thus the quotient injects for \(p\leq k\). This proves (J.1).

Now examine the bottom term in column \(k+1\). For a differential of length \(s\), its possible source has coordinates
\[
 (p,q)=(k+1-s,s-1).
\tag{J.2}
\]
The map on this source term on page \(s\) is an isomorphism by (J.1). We also need surjectivity on its cycle subspace. Fix (J.2) and argue backward through pages \(t\geq s\). At a sufficiently late page the term is stable and its map is an isomorphism by the limiting-page hypothesis. Since \(q=s-1\), every differential of length greater than \(s\) out of this term has negative target row and is zero. Thus \(E_{t+1}^{p,q}=Z_{t+1}^{p,q}\) for \(t\geq s\). The exact sequence
\[
 E_t^{p-t,q+t-1}\longrightarrow Z_t^{p,q}
       \longrightarrow E_{t+1}^{p,q}\longrightarrow0
\tag{J.3}
\]
shows that surjectivity on the last term implies surjectivity on the middle: its first term is in the isomorphism range of (J.1), because \(p-t=k+1-s-t\leq k-t+1\). Backward induction proves the needed surjectivity on \(Z_s^{p,q}\).

Consequently the image of the incoming differential into \((k+1,0)\) maps isomorphically: it is the quotient of the isomorphic source terms by cycle subspaces whose map is surjective and, as a restriction of an isomorphism, also injective. Bottom-row terms have no outgoing differential. Their exact sequences are therefore
\[
0\longrightarrow\operatorname{im}d_s\longrightarrow E_s^{k+1,0}
 \longrightarrow E_{s+1}^{k+1,0}\longrightarrow0.
\tag{J.4}
\]
Starting at the limiting isomorphism and going backward in \(s\), the isomorphism of their outer terms proves the isomorphism of their middle terms. This reaches page two in column \(k+1\). Induction in \(k\) completes the proof. Negative source coordinates mean zero terms throughout; no convergence beyond finite stabilization at each position is used. ∎

### J.2. From transgressive simple generators to a polynomial base

Suppose a fibration with contractible total space has the multiplicative spectral sequence (I.1). Assume the positive classes \(x_\lambda\) in the fibre have all their finite products of *distinct* members as a vector-space basis, including the empty product. Assume finitely many \(x_\lambda\) in each degree. Suppose each is transgressive with a chosen ordinary base witness \(y_\lambda\) of degree \(|x_\lambda|+1\). Then
\[
 H^*(B;F)=F[y_\lambda].
\tag{J.5}
\]

We prove this by constructing an additive map of spectral sequences. For one index \(\lambda\), take a formal second page with basis
\[
 y_\lambda^m,\quad x_\lambda y_\lambda^m\quad(m\geq0),
\]
where the formal \(x_\lambda\) is exterior. All differentials are zero until length \(|x_\lambda|+1\), when
\[
 d(x_\lambda y_\lambda^m)=y_\lambda^{m+1}.
\tag{J.6}
\]
Its next page is just the ground field in position \((0,0)\). Tensor these models over all indices, with differentials given by the tensor derivation. This is a spectral sequence: homology of a tensor product of field complexes is the tensor product of their homologies, by splitting into homology and contractible pairs. In each bidegree only finitely many indices contribute, so this also verifies the infinite tensor product. Its second page is the tensor product of the formal polynomial horizontal axis and the vector-space exterior vertical axis. Its limiting page is the ground field.

Map a basis element to the actual product of its distinct fibre classes and its chosen base classes, on the actual second page. This is a linear map. It need not be a ring map on the fibre axis: the actual squares \(x_\lambda^2\) may be nonzero. No such ring property is required. On any page the remaining formal basis uses each surviving \(x_\lambda\) at most once. The actual higher-page derivation formula and the transgression witnesses imply that its differential is exactly the image of the formal differential: before the specified length each \(x_\lambda\) has zero differential, at that length its differential is the residue of \(y_\lambda\), and every base factor has zero outgoing differential. This makes the linear map a chain map at that page and hence induces the next-page map. After a factor has disappeared, its positive formal terms were boundaries or paired with them; their images disappear as the corresponding actual boundaries. Induction supplies a map of all pages with the stated basis formula on the surviving tensor factors.

On the vertical second-page axis it is an isomorphism by the simple-basis hypothesis. On the limiting page it is an isomorphism because both total cohomologies are the ground field and the unit maps to the unit. The reverse comparison of J.1 therefore makes it an isomorphism on the horizontal second-page axis. There it is precisely the ring homomorphism from the formal polynomial ring to the ordinary base ring taking the formal generators to \(y_\lambda\). This proves (J.5), including algebraic independence. ∎

## K. The complete one-group cohomology calculation

For a sequence \(I=(i_1,\ldots,i_m)\), retain the admissibility and excess conventions of Section C. A tail of an admissible sequence is admissible, and its excess is at most the excess of the full sequence:
\[
 e(i_2,\ldots,i_m)=e(I)-(i_1-2i_2)\leq e(I).
\tag{K.1}
\]

**Lemma K.1 — Top-square labels.** On a class of degree \(r\), an admissible word of excess greater than \(r\) is zero. Words of excess exactly \(r\) are precisely the labels obtained by taking a positive power \(2^a\) of a word of excess less than \(r\). More precisely the labels \((J,a)\), with \(e(J)<r\) and \(a\geq0\), correspond bijectively to all admissible labels of excess at most \(r\).

For the first assertion, \(i_1=e(I)+i_2+\cdots+i_m\) exceeds the degree of the class to which the leftmost square is applied, so instability gives zero. If \(e(I)=r\), that leftmost index equals that degree. The top-square rule consequently says
\[
 \operatorname{Sq}^I x=(\operatorname{Sq}^{(i_2,\ldots,i_m)}x)^2.
\tag{K.2}
\]
Its tail has excess at most \(r\), by (K.1). Remove leading indices until the tail has excess less than \(r\); the finite sequence ends at the empty tail if necessary. This expresses the class as a power \(2^a\) of that final word. Conversely, for any admissible tail \(J\) of excess at most \(r\), prepend its current class degree \(r+|J|\). This index is at least twice the first tail index, because \(e(J)\leq r\). The new sequence is admissible with excess exactly \(r\), and its evaluation is the square. Iterate. The stripping and prepending procedures are inverse on labels, so this is a bijection, independent of any possible relation among the evaluated classes. ∎

**Theorem K.2 — Mod-two cohomology of the one-group spaces.** For \(r\geq1\),
\[
 H^*(K(F,r);F)=F[\operatorname{Sq}^I\iota_r:
                I\text{ admissible},\ e(I)<r].
\tag{K.3}
\]
The empty word is included. This means a polynomial algebra on exactly the displayed classes.

The base case can be realized by \(\mathbb{RP}^{\infty}\). To check its one-group property, its antipodal cover is \(S^\infty\), with the weak CW topology on finite coordinate spheres. Every sphere map and homotopy has finite cell carrier; its image is contained in a finite sphere. Inclusion of that sphere as the equator in the next sphere contracts it by the hemisphere cone. Thus all homotopy groups of \(S^\infty\) vanish and it is path connected. The quotient is the projective CW model. On the open set where a given coordinate is nonzero, choosing its positive sign gives a continuous sheet chart, checked in each finite stage and hence in the weak topology. The general covering proof in the classifying chapter gives \(\pi_1=F\) and all higher homotopy groups zero. The complete one-group comparison identifies it with the chosen \(K(F,1)\) on homology. The already proved real-projective cup-ring calculation is \(F[\iota_1]\). The only admissible word with excess less than one is the empty word, proving (K.3) for \(r=1\).

Assume (K.3) for \(r\), and use the path fibration over \(K(F,r+1)\). Its loop fibre compares with \(K(F,r)\) by the already proved one-group comparison. The base is simply connected and the total space is contractible. Finite-type homology of both base and fibre follows from the integral finite-type theorem. Thus I.1 applies.

The polynomial fibre algebra has the simple system consisting of powers \(2^a\) of all its polynomial generators: each monomial has a unique binary expansion of the exponent of each generator, giving a unique product of distinct members of this system. There are finitely many such members in each degree, since there are finitely many sequences of a fixed total index and only finitely many powers of any positive-degree generator in a fixed range. By Lemma K.1 these members are exactly
\[
 \operatorname{Sq}^I\iota_r,
        \qquad I\text{ admissible},\ e(I)\leq r.
\tag{K.4}
\]
They are transgressive with witnesses \(\operatorname{Sq}^I\iota_{r+1}\), by I.2. Applying J.2 makes the base a polynomial algebra on those witnesses. Their labels have \(e(I)\leq r\), equivalently \(e(I)<r+1\). This proves (K.3) at the next step and completes the induction. Neither Adem relations nor a dimension guess has entered this proof. ∎

### K.1. The stable basis and its operation meaning

If \(0\leq q<r\), every product of at least two positive polynomial generators of (K.3) has degree at least \(2r>r+q\). Its degree-\(r+q\) component therefore has basis
\[
 \operatorname{Sq}^I\iota_r,
       \qquad I\text{ admissible},\ |I|=q.
\tag{K.5}
\]
Every such label occurs, since \(e(I)\leq |I|=q<r\). The empty label gives the degree-zero operation. Cohomology suspension sends this basis in \(K(F,r+1)\) to the identical labels in \(K(F,r)\), by A.1 and the normalized loop evaluation. It is therefore an isomorphism in this shifted finite range, without invoking a separate suspension-range theorem.

Let \(A_q\) be the vector space spanned by all degree-\(q\) composites of squares, modulo equality as stable operations on based CW complexes and their reduced cohomology. Then the admissible words of degree \(q\) form a basis of \(A_q\). Independence is already proved in C.1. For spanning, evaluate a composite on \(\iota_r\), with \(r>q\) and \(r\geq2\), and expand it in (K.5). Naturality and F.1 make this equality an equality of operations on degree-\(r\) classes of every based CW complex. Its coefficients are unchanged on raising \(r\), by the basis-preserving cohomology suspension. Suspending a class in any smaller degree enough times and using the injective reduced suspension isomorphism proves the same operation identity in that degree. Relative CW classes are treated by the based quotient and its relative-cohomology comparison. Hence every composite has the claimed admissible expansion as a stable operation. No particular formula for a nonadmissible word is needed here.

The same argument shows that every additive natural stable operation of nonnegative degree is a linear combination of these words: evaluate it on the representing class, expand by (K.5), and use representation and suspension. The construction of the stable square basis does not depend on this broader assertion; the algebra generated by the squares already has the full basis needed below.

## L. The connected square bialgebra

Composition makes \(A=\bigoplus_{q\geq0}A_q\) a graded associative unital algebra, and \(A_0=F\). Each graded component is finite dimensional. Its coproduct is determined by
\[
 \Delta_A(\operatorname{Sq}^i)
       =\sum_{j=0}^i\operatorname{Sq}^j\otimes\operatorname{Sq}^{i-j},
\tag{L.1}
\]
and multiplication, with counit the projection to degree zero.

We verify that this definition respects operation equalities. For a square word, iterate the proved Cartan formula on an external product of two classes. It gives exactly the action of the tensor obtained by multiplying (L.1). If a linear combination of words is zero as a stable operation, its tensor action on every such external product is zero. In a fixed total degree, evaluate the two factors on products of sufficiently many degree-one projective classes. Lemma C.1 says that the admissible operations in either factor act independently on its chosen product class. The Künneth injection on the product then says that their tensor products act independently. Separate bidegrees lie in separate direct summands of that cohomology. Thus the tensor itself is zero. This proves well-definedness and, by the same composition calculation, that \(\Delta_A\) is an algebra homomorphism.

Coassociativity follows first on a square generator: both iterated coproducts are the sum of \(\operatorname{Sq}^a\otimes\operatorname{Sq}^b\otimes\operatorname{Sq}^c\) for \(a+b+c=i\). Multiplicativity gives it on every word. The counit identities follow by retaining the terms with degree-zero factor; they too pass to words. The counit is an algebra homomorphism since a product of positive total degree has positive degree. Thus \(A\) is a connected graded bialgebra. The freeness criterion D.1 requires precisely these properties, and requires no unproved antipode theorem.

**References.** Serre’s mod-two one-group calculation, Borel’s simple-generator theorem and the reverse comparison theorem are presented in [Hatcher’s *Spectral Sequences*](https://pi.math.cornell.edu/~hatcher/SSAT/SSch1.pdf), Theorems1.32,1.34 and1.36. The preceding proofs include the filtered products, transgression witnesses and representation arguments used here.

**The dual square algebra.** Put \(A_* =\bigoplus_{q\geq0}\operatorname{Hom}_F(A_q,F)\), the graded dual. Each component is finite dimensional. Its multiplication is dual to \(\Delta_A\), and its coproduct is dual to composition. For \(x\in H^1(\mathbb{RP}^\infty;F)\), define \(\xi_j\in (A_*)_{2^j-1}\) as the coefficient of \(x^{2^j}\) in the action on \(x\), with \(\xi_0=1\). Then
\[
 A_*=F[\xi_1,\xi_2,\ldots],\qquad
 \Delta\xi_n=\sum_{i+j=n}\xi_i^{\,2^j}\otimes\xi_j.
\tag{L.2}
\]

To prove the presentation, the line formula gives \(\operatorname{Sq}^b(x^a)=\binom ab x^{a+b}\). For \(a=2^j\), the only nonzero binomial coefficients modulo two have \(b=0\) or \(b=2^j\), as follows from \((1+z)^{2^j}=1+z^{2^j}\). Thus every square word sends \(x\) to zero or a power with exponent a power of two. Cartan on \(x_1\cdots x_N\) says that its coefficient with exponents \(2^{j_1},\ldots,2^{j_N}\) is the pairing with \(\xi_{j_1}\cdots\xi_{j_N}\). By C.1–C.2, every nonzero element of \(A_q\) acts nontrivially on such a product for sufficiently large finite \(N\). Consequently the products of the \(\xi_j\) have zero annihilator in \(A_q\), so they span its full dual. This last implication is finite-dimensional linear algebra: a proper span has a nonzero annihilator.

The parameters \(e_j\) of C identify admissible words bijectively with finite lists of nonnegative integers, of degree \(\sum_j(2^j-1)e_j\). These are exactly the degrees and counts of monomials in the proposed generators. The surjective polynomial map is therefore an isomorphism in every degree. Its multiplication is commutative because the Cartan coproduct is cocommutative, first on the square generators and hence on their products.

Finally evaluate the coproduct on \(a\otimes b\) by applying \(ab\) to \(x\). A term \(x^{2^j}\) from \(bx\) has coefficient \(\xi_j(b)\). Applying \(a\) to this power is the same as applying the iterated Cartan coproduct to \(2^j\) copies of \(x\). The coefficient of \(x^{2^{i+j}}\) is \(\xi_i^{2^j}(a)\). To see the cancellation precisely, rotate the \(2^j\) tensor positions. Cocommutativity makes their coefficients constant on rotation orbits. Every nonconstant tuple of exponents has orbit length a positive power of two greater than one, so its contributions cancel in \(F\). The surviving constant tuple has exponent \(2^i\) in every position and coefficient paired with \(\xi_i^{2^j}\). Taking the coefficient of \(x^{2^n}\) proves (L.2). All comparisons occur in fixed finite degrees and on finite projective stages. This is the dual algebra calculation in [Miller’s notes](https://math.mit.edu/~hrm/papers/cobordism.pdf), Theorem11.2.

## M. Stable Thom cohomology as a module coalgebra

### M.1. Stable degrees and the square action

Let
\[
 C=F[w_1,w_2,\ldots],\qquad |w_j|=j,
\tag{M.1}
\]
as a graded vector space. Its polynomial notation is a convenient identification of coefficient classes. Its multiplication is not being identified with the ordinary, unsuspended cup product of Thom classes. The zero-degree distinguished vector is \(u=1\).

For \(k>q\), the universal ring and Thom isomorphism identify
\[
 C_q\xrightarrow{\ \Phi_k\ }
     \widetilde H^{k+q}(MO(k);F),\qquad
 \alpha\longmapsto\alpha(w(\gamma_k))U_k.
\tag{M.2}
\]
This is an isomorphism: no polynomial of weight \(q\) uses a variable of index greater than \(q\). For \(q=0\), it takes \(u\) to \(U_k\). Normal stabilization pulls the rank-\((k+1)\) bundle back to \(\gamma_k\oplus\varepsilon^1\). Under the proved Thom suspension homeomorphism, its Thom class is the suspension of \(U_k\), by the value-one fibre normalization. Its other coefficient classes pull back to the same \(w_j\), by exact Whitney stability. Thus the desuspended map between the groups in (M.2) is the identity on \(C_q\) once \(k>q\).

For \(\alpha\in C_q\), choose \(k>q+i\), and define \(\operatorname{Sq}^i\alpha\in C_{q+i}\) by
\[
 \Phi_k(\operatorname{Sq}^i\alpha)
      =\operatorname{Sq}^i(\Phi_k\alpha).
\tag{M.3}
\]
Here the left square denotes the new action on coefficient vectors, and the right one the ordinary operation on the Thom space. This definition is independent of \(k\): naturality under normal stabilization and the proved square suspension identity make its two consecutive versions agree in the stable coefficient coordinates. Iterating handles any two sufficiently large ranks. Compositions agree with the action of square words by computing all factors at one sufficiently large rank. Equalities in \(A\) are equalities of operations on that Thom CW complex. Hence (M.3) is a well-defined graded \(A\)-module action on \(C\).

### M.2. The coproduct supplied by direct sum

Define a degree-preserving coproduct and counit by
\[
 \Delta_C(w_j)=\sum_{a+b=j}w_a\otimes w_b,
 \qquad w_0=1,\qquad
 \epsilon_C(C_{>0})=0,\quad\epsilon_C(u)=1,
\tag{M.4}
\]
extending \(\Delta_C\) multiplicatively in the polynomial coordinates. Every expression in a fixed weight is finite. Both iterated coproducts on \(w_j\) are the sum over \(a+b+c=j\), so coassociativity follows on all polynomials. The counit identities follow by setting one sequence of positive-weight variables to zero. Thus \(C\) is a connected graded coalgebra, with \(\Delta_Cu=u\otimes u\).

We verify the geometric meaning and the \(A\)-module compatibility, including the finite-stage topology. Fix a total coefficient weight bound \(d\), and choose ranks \(k,l>d\). In each Grassmannian choose an ambient dimension large enough to include all its Schubert cells of dimensions at most \(d+1\). The finite-stage cellular comparison makes inclusion an isomorphism in cohomology through degree \(d\). The spaces and their disk/sphere bundles at these stages are compact.

On the product of the two finite Grassmannians, take the external direct sum of the two tautological bundles. Its classifying map to the rank-\((k+l)\) Grassmannian sends two planes in disjoint coordinate blocks to their direct sum. Its projection matrix is their block-diagonal projection, so the map is continuous and its pulled-back tautological bundle is exactly this external sum. The product of the two disk bundles, modulo the union of their sphere-bundle factors, is its Thom space: the block-maximum norm disk is radially homeomorphic to the Euclidean direct-sum disk, carrying the boundary union to the sphere bundle. All these spaces are compact with Hausdorff targets; quotienting in either order therefore gives the same topology. The induced based Thom map is an actual finite-stage map.

The external product of the two canonical Thom classes is the Thom class of the external sum, since it evaluates to \(1\cdot1=1\) on each fibre product generator. The Thom uniqueness theorem proves this identification. Whitney's exact formula and the external-product Thom isomorphism now identify pullback of \(\Phi_{k+l}\alpha\) with
\[
 \sum_{(\alpha)}\Phi_k\alpha'\times\Phi_l\alpha'',
 \qquad \Delta_C\alpha=\sum_{(\alpha)}\alpha'\otimes\alpha''.
\tag{M.5}
\]
The identification on coefficient classes is exactly (M.4); each tensor component is tested in the finite degree range just chosen. The field Künneth calculation is valid there, with finite-dimensional graded factors. Enlarging the ambient stages does not change it, because the same characteristic cells and bundle maps are included. This proves the meaning of the coproduct without asserting that an arbitrary ordinary product of infinite CW Thom spaces has a CW topology.

Now let \(a\in A\) be homogeneous and \(\alpha\in C\), and choose \(d\geq |a|+|\alpha|\) in that construction. Naturality under the finite Thom map, followed by Cartan on the external product, gives
\[
 \Delta_C(a\alpha)
    =\sum_{(a),(\alpha)}a'\alpha'\otimes a''\alpha'',
 \qquad \Delta_Aa=\sum_{(a)}a'\otimes a''.
\tag{M.6}
\]
The stable coefficient identifications in M.1 convert the actual operations in this equality to the asserted action on \(C\). The sufficiently large finite-stage restriction is an isomorphism in all coefficient weights used, so it detects the equality rather than merely giving a necessary restriction of it. For words, iterated Cartan gives precisely the coproduct of L.1. Linearity proves (M.6) for every \(a\). The counit is also an \(A\)-module map to \(F\) with its augmentation action: if either homogeneous degree is positive both sides of \(\epsilon_C(a\alpha)=\epsilon_A(a)\epsilon_C(\alpha)\) are zero; in degree zero it is the scalar identity.

### M.3. The faithful Thom-class orbit

The map
\[
 A\longrightarrow C,\qquad a\longmapsto au
\tag{M.7}
\]
is injective. To prove this in degree \(q\), choose \(k>q\) and consider the block sum of \(k\) tautological real lines over \((\mathbb{RP}^{\infty})^k\). Its bundle map into \(\gamma_k\) and its zero section give a cohomological restriction of \(\operatorname{Sq}^I U_k\) to
\[
 \operatorname{Sq}^I(x_1\cdots x_k).
\tag{M.8}
\]
Indeed the zero-section restriction of a Thom class is its top mod-two Euler class, which is \(w_k\). Its restriction to the line product is the product of the line classes \(x_j\), by the exact Whitney and Euler product formulas. Naturality of squares proves (M.8). All maps on this product can also be checked on its compact finite projective stages, which include every cohomology degree used.

The admissible basis of \(A_q\) is finite. Lemma C.1 proves that the expressions (M.8) for its different labels are linearly independent when \(k\geq q\), since \(e(I)\leq |I|=q\). Thus a linear combination of their Thom classes cannot be zero. Through (M.2) these are precisely the vectors \(\operatorname{Sq}^Iu\), proving (M.7) in every degree, including degree zero. This argument verifies faithfulness for the full algebra now proved, rather than for an unproved list of independent operations.

### M.4. Freeness and its finite generators

All hypotheses of D.1 now hold: \(A\) is a connected graded bialgebra, \(C\) is a connected graded module coalgebra with its module counit, and the distinguished orbit (M.7) is injective. Put
\[
 Q=C/A_+C,
\tag{M.9}
\]
and choose any graded vector-space section \(\sigma:Q\to C\). The fully proved triangular argument gives
\[
 A\otimes Q\xrightarrow{\ \cong\ }C,
             \qquad a\otimes v\longmapsto a\sigma(v).
\tag{M.10}
\]
Each \(Q_j\) is finite dimensional, since \(C_j\) has one basis vector per partition of \(j\). Choose a basis of each \(Q_j\). Formula (M.10) says that all admissible square words on their lifted vectors form a basis of \(C\), with total weight the sum of the word degree and the generator degree. This is the needed free Thom module theorem with its actual proof and action conventions.

## N. A finite comparison and the full detection theorem

Fix \(n\geq0\), and choose \(k>n+3\). Put \(N=n+k\). Choose the basis vectors of \(Q_a\) for all \(0\leq a\leq n+1\), and label their lifts by \(v_\lambda=\sigma(q_\lambda)\), with \(a_\lambda=a\). There are finitely many of them. Regard each as the actual class
\[
 \Phi_kv_\lambda\in\widetilde H^{k+a_\lambda}(MO(k);F).
\]
Theorem F.1 supplies based maps representing them, so an actual map
\[
 V:MO(k)\longrightarrow
       Y=\prod_\lambda K(F,k+a_\lambda).
\tag{N.1}
\]
No infinite product or abstract realization theorem is used.

This map is an isomorphism in mod-two cohomology through degree \(N+1\). Both spaces are connected, so the unit gives the degree-zero isomorphism. Both have zero positive cohomology below degree \(k\). For degree \(k+j\), \(0\leq j\leq n+1\), no product of two positive classes of factors of \(Y\) can occur: its degree would be at least \(2k>k+n+1\). In a factor of degree \(r_\lambda=k+a_\lambda\), the remaining degree increment is \(j-a_\lambda\), if nonnegative, and is less than \(r_\lambda\). The basis calculation (K.5) therefore gives the basis of this product cohomology in that degree as
\[
 \operatorname{Sq}^I\iota_{k+a_\lambda},
      \qquad |I|+a_\lambda=j,
\tag{N.2}
\]
with admissible \(I\), each class pulled back from its indicated coordinate. Naturality makes its pullback under \(V\) equal to \(\operatorname{Sq}^I(\Phi_kv_\lambda)\). The choice \(k>n+3\) places all these operations in the stable coefficient range of M.1. By (M.10) their coefficient vectors are a basis of \(C_j\), hence by (M.2) their Thom classes are a basis of the source cohomology. This proves the asserted isomorphism in every required degree, not just equality of dimensions. The field chain splitting identifies these cohomology maps with full dual homology maps; bijectivity of a full dual reflects bijectivity of the linear map. Thus \(V\) is a homology isomorphism over \(F\) through degree \(N+1\).

Both spaces are two-connected: \(MO(k)\) is \((k-1)\)-connected by the actual Thom-cell theorem, and each product factor is \((k+a_\lambda-1)\)-connected. Their homotopy groups through degree \(N+1\) have exponent two. For the product this is immediate from its individual one-group homotopy groups and the finite-coordinate description of sphere maps and homotopies. For \(MO(k)\), degrees below \(k\) are zero; a remaining degree \(k+m\), \(0\leq m\leq n+1\), is identified with \(\mathcal N_m\) by the complete geometric Pontryagin–Thom theorem, since \(k>m+1\). The product cylinder has boundary two copies of the manifold, so every such group has exponent two. The finite comparison theorem G.1 now proves
\[
 V_*:\pi_N(MO(k))\xrightarrow{\ \cong\ }\pi_N(Y).
\tag{N.3}
\]

**Theorem N.1 — Stiefel–Whitney numbers detect unoriented bordism.** A closed smooth \(n\)-manifold is the boundary of a compact smooth \((n+1)\)-manifold if and only if all its Stiefel–Whitney numbers vanish. In dimension zero the list consists of the empty number, the parity of its points. Two closed smooth manifolds of the same dimension are unoriented bordant if and only if their corresponding Stiefel–Whitney numbers agree.

**Proof.** A boundary has all its numbers zero by the complete boundary-number proof in the [projective tangent chapter](projective-tangent-bundles-and-obstructions.md), Theorem5.1: its tangent classes extend stably from the filling, and its fundamental class maps to zero there by the relative boundary identity.

Conversely suppose the numbers of \(M\) vanish. Its normal collapse \(c_M:S^N\to MO(k)\) has zero mod-two Hurewicz class by B.3. Every pullback of a cohomology class of degree \(N\) along this collapse is therefore zero, by its evaluation on the sphere generator. In other positive degrees the sphere cohomology is zero automatically. In particular \(c_M^*\Phi_kv_\lambda=0\) for every generator used in (N.1). The representing-map bijection F.1 makes each coordinate of \(V c_M\) based null homotopic; equivalently each one-group factor has exactly the stated single sphere homotopy group and its normalized class detects it. Taking the finite product of these coordinate homotopies makes \(V c_M\) null. Injectivity in (N.3) makes \(c_M\) null. The full Pontryagin–Thom correspondence, with the same rank bound, now gives a compact smooth filling of \(M\).

For the comparison assertion, each number is additive under disjoint union, because component fundamental classes add and the bundle classes restrict to each component's classes. Over \(F\), equality of the two lists is equivalent to vanishing on their disjoint union. The first assertion makes that union bound, which is precisely an unoriented bordism between the two manifolds. A bordism gives equality by the forward boundary implication. This includes empty manifolds and dimension zero. ∎

The same construction also identifies the group in a fixed dimension as a vector space with the chosen \(Q_n\): the only factors of \(Y\) with nonzero \(\pi_N\) have \(a_\lambda=n\), and each contributes one copy of \(F\). The identification depends on the choices of lifts and bases. The detection theorem does not require a canonical splitting or a polynomial-ring presentation of the bordism ring.

### N.2. Polynomial products and explicit generators

**Polynomial products and explicit generators.** The graded unoriented bordism ring has the presentation
\[
 \mathcal N_*\cong F[z_d:\ d>0,\ d\ne2^j-1\text{ for every }j\geq1],
 \qquad |z_d|=d.
\tag{N.4}
\]
For even \(d\), take \(z_d=[\mathbb{RP}^d]\). For odd permitted \(d\), write uniquely
\[
 d+1=2^r(2s+1),\qquad r\geq1,\ s\geq1,
\]
and take \(z_d=[P(2^r-1,2^rs)]\), where
\[
 P(m,n)=(S^m\times\mathbb{CP}^n)/
                  ((x,[v])\sim(-x,[\bar v])).
\tag{N.5}
\]
In particular products of two closed smooth manifolds that do not bound cannot bound. We prove the ring assertion, the representatives and this consequence.

First the collar gluing proof of bordism equivalence applies after forgetting orientations. Disjoint union gives an abelian group with empty manifold as zero and each class its own inverse, since the cylinder bounds two copies. Product respects this equivalence because \(\partial(W\times M)=\partial W\times M\) when \(M\) is closed. Product charts give associativity and factor-exchange diffeomorphisms; disjoint union distributes over product. The class of one point is the multiplicative unit. These facts make \(\mathcal N_*\) a graded commutative \(F\)-algebra, including its degree-zero parity group.

The finite comparison above identifies \(\mathcal N_n\) with \(Q_n\) as vector spaces. The polynomial coefficient ring \(C\), admissible basis of \(A\), and freeness in M.4 give the formal dimension series
\[
 \sum_{n\geq0}\dim_F\mathcal N_n\,t^n
 =\frac{\prod_{j\geq1}(1-t^{2^j-1})}
         {\prod_{d\geq1}(1-t^d)}
 =\prod_{\substack{d\geq1\\d\ne2^j-1}}(1-t^d)^{-1}.
\tag{N.6}
\]
Every coefficient involves finitely many factors. The numerator follows from the exact admissible parameters \(e_j\), with degree \(\sum_j(2^j-1)e_j\); division is valid for series with constant coefficient one. Thus the dimension is the number of partitions of \(n\) using the permitted parts. This proves a dimension count; the following geometric and number calculations establish multiplication.

**Dold manifolds, their cohomology and tangent classes.** For \(m,n\geq1\), (N.5) is a connected closed smooth manifold of dimension \(m+2n\): the displayed involution is free because its sphere coordinate is antipodal. Projection makes it a \(\mathbb{CP}^n\)-bundle over \(\mathbb{RP}^m\). Pull back the tautological real line from the base to obtain \(\lambda\), and set \(c=w_1(\lambda)\). Descend the complex tautological line under conjugation to a real rank-two bundle \(V\) on the quotient, and set \(d=w_2(V)\). Then
\[
 H^*(P(m,n);F)=F[c,d]/(c^{m+1},d^{n+1}),\quad
 |c|=1,\ |d|=2,\quad
 \langle c^m d^n,[P(m,n)]_2\rangle=1,
\tag{N.7}
\]
and
\[
 w(TP(m,n))=(1+c)^m(1+c+d)^{n+1}.
\tag{N.8}
\]

Here is a cohomology proof including the relations. On each projective fibre \(d\) is the reduction of the tautological Chern class, hence its positive mod-two generator. Thus \(1,d,\ldots,d^n\) restrict to a basis. Cup product with these classes gives an isomorphism from the direct sum of the shifted base cohomology groups onto the total cohomology. To verify this instance of Leray–Hirsch, filter the finite CW base by its skeleta. Over each characteristic disk the bundle is trivial; the relative disk/boundary pair has cohomology the shifted fibre cohomology, by the field product calculation in I.1. The proposed map on that relative pair is an isomorphism precisely because the restrictions are a fibre basis. The long exact sequences for consecutive skeleta and their commuting cup-product maps give the absolute isomorphism inductively, starting on the vertices. Excision gives the direct sum over cells at each step. This is the same disk-pair comparison used for the Serre filtration, so no collapse or ring relation is assumed in this induction.

The base relation gives \(c^{m+1}=0\). The coordinate functionals on \(\mathbb C^{n+1}\), restricted to its tautological line, form a nowhere-zero section of the sum of \(n+1\) complex dual lines: together they are the tautological inclusion. Conjugation sends these functionals to their conjugates, so the section descends to \((n+1)V^*\). The real dual is isomorphic to \(V\) through an invariant metric. Its top Stiefel–Whitney class is consequently \(d^{n+1}\), and vanishes because of this nowhere-zero section. The monomials \(c^a d^b\), \(0\leq a\leq m,0\leq b\leq n\), are already an additive basis by the preceding induction. The two relations therefore give the entire ring. The unique top monomial is nonzero; mod-two Poincaré duality gives its evaluation one, establishing all of (N.7).

For (N.8), unitary changes in a tautological complex-line chart preserve real orientation, whereas conjugation reverses it. The determinant line of \(V\) is therefore \(\lambda\), so \(w(V)=1+c+d\). The vertical tangent space is \(\operatorname{Hom}_{\mathbb C}(\gamma,\gamma^\perp)\) on the covering product. Splitting \(\mathbb C^{n+1}=\gamma\oplus\gamma^\perp\) gives the conjugation-equivariant isomorphism
\[
 T_{\rm vert}\oplus(\varepsilon\oplus\lambda)
       \cong(n+1)V^*.
\]
The added summand is \(\operatorname{End}_{\mathbb C}(\gamma)\): its real scalar part is trivial and its imaginary scalar part changes sign under conjugation. This verifies the equivariance of the usual projective tangent stabilization explicitly. The base tangent bundle satisfies \(T\mathbb{RP}^m\oplus\varepsilon\cong(m+1)\lambda\). The tangent sequence of the bundle splits with a metric, and Whitney multiplication now gives (N.8), cancelling the unit \(1+c\) in the finite cohomology ring. This proof includes \(m=1\).

**The generator number.** Let \(s_a(w)\) be the stable symmetric polynomial which becomes the power sum \(\sum_i t_i^a\) in formal Stiefel–Whitney roots. The integral symmetric-polynomial construction of the characteristic-number chapter, Lemma2.1, reduces modulo two. Its product identity follows by splitting the formal variables into the two summand lists and then substituting the exact Whitney identity. In particular \(s_a\) is additive on bundle sums and is unchanged by a trivial summand.

For an even dimension \(k\), the stable tangent formula on \(\mathbb{RP}^k\) gives \(s_k=(k+1)x^k=x^k\), so its number is one. For the odd representative set \(m=2^r-1\), \(n=2^rs\), and \(k=m+2n\). Formal rank-two roots \(u,v\), with \(u+v=c,uv=d\), give power sums \(S_0=0,S_1=c,S_2=c^2\) and
\[
 S_a=cS_{a-1}+dS_{a-2},\qquad
 S_a=\sum_{i=0}^{\lfloor a/2\rfloor}
            \binom{a-i-1}{i}c^{a-2i}d^i\quad(a\geq1).
\tag{N.9}
\]
The recurrence follows from the quadratic equation of either root; the formula follows from the two initial values and Pascal’s identity, with a binomial coefficient zero when its lower index exceeds its nonnegative upper index. These symmetric-polynomial identities can now be evaluated on the classes \(c,d\) of (N.7).

By (N.8) the top power sum on the odd representative is \(m c^{m+2n}+(n+1)S_{m+2n}=S_{m+2n}\): the first term vanishes by the base relation and \(n+1\) is odd. In (N.9), terms with \(i<n\) exceed the allowed power of \(c\), and terms with \(i>n\) exceed the allowed power of the degree-two class. The surviving coefficient is
\[
 \binom{m+n-1}{n}=\binom{n+2^r-2}{n}=1\quad\text{in }F.
\tag{N.10}
\]
Indeed \(n\) is divisible by \(2^r\), so its binary digits are disjoint from those of \(2^r-2\). The identity \((1+z)^b=\prod_{j:\,b_j=1}(1+z^{2^j})\) over \(F\) says that a coefficient indexed by a subset of these digits is one. Thus the top power-sum number of every proposed \(z_d\) is one. This also proves directly that these manifolds do not bound. The first odd representatives are \(P(1,2)\) in dimension five, \(P(1,4)\) in dimension nine, and \(P(3,4)\) in dimension eleven.

**All products and the polynomial presentation.** For a partition \(I\) of \(n\) in permitted positive parts, let \(Z_I\) be the ordered product of the corresponding representatives. For each such partition \(J\), use the symmetric number \(s_J(w)[Z_I]\). The orbit-sum product identity from the characteristic-number chapter gives a sum over distinct ordered splittings of the exponent multiset \(J\) among the factors. Each splitting has coefficient one, including when parts repeat. Only splittings whose weight on every factor is its dimension survive evaluation, by the normalized product fundamental class.

A nonzero entry consequently requires \(J\) to refine the partition \(I\). In particular \(\ell(J)\geq\ell(I)\). If their lengths are equal, every factor receives exactly one part, forcing \(J=I\). For that diagonal entry there is a single ordered splitting, and its value is the product of the top power-sum numbers just proved, hence one. Order the partitions by length. The resulting square number matrix is triangular with diagonal one, so the product classes \([Z_I]\) are linearly independent: all these numbers are linear combinations of the bordism-invariant Stiefel–Whitney numbers. Their count is the dimension in (N.6), so they are a basis in every degree. The empty partition gives the point in degree zero.

The polynomial map in (N.4) sending a variable to its indicated manifold sends its monomials to exactly these bases. It is therefore a graded algebra isomorphism. Any two nonzero polynomials involve only finitely many variables; their product is nonzero by the leading-monomial argument over a field. Hence this ring has no zero divisors. Theorem N.1 translates this to the asserted nonboundary product consequence.

Thom’s polynomial-ring theorem and product consequence appear in [his 1954 paper](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/thomcob.pdf), ChapterIV. Dold’s explicit quotient representatives and their characteristic classes are developed in [Junzhi Huang’s account](https://math.uchicago.edu/~may/REU2021/REUPapers/Huang%2CJunzhi.pdf), Sections3–5. The proof above supplies the cohomology relations, corrected Newton initial values and the general product independence argument.

## O. Exercises with complete solutions

**Exercise O.1 — Easy.** Recover the first four normal classes from the tangent classes. Compute both lists on \(\mathbb{RP}^4\), and explain why vanishing of the fourth normal class would not establish a boundary.

**Solution.** Solve the inverse-series equations in increasing weight to obtain
\[
v_1=t_1,\quad v_2=t_1^2+t_2,\quad v_3=t_1^3+t_3,
\quad v_4=t_1^4+t_1^2t_2+t_2^2+t_4.
\]
On \(\mathbb{RP}^4\), the proved tangent formula gives \(t_1=x\), \(t_2=t_3=0\), \(t_4=x^4\), in \(F[x]/(x^5)\). Hence \(v_1=x\), \(v_2=x^2\), \(v_3=x^3\), \(v_4=0\). Nevertheless the number \(\langle v_1v_3,[\mathbb{RP}^4]_2\rangle=\langle x^4,[\mathbb{RP}^4]_2\rangle=1\), and the tangent number \(\langle t_4,[\mathbb{RP}^4]_2\rangle=1\). The detection criterion uses every weight-four monomial, so this manifold does not bound.

**Exercise O.2 — Medium.** On the product of three real infinite projective spaces, distinguish the degree-three operations \(\operatorname{Sq}^3\) and \(\operatorname{Sq}^2\operatorname{Sq}^1\) by applying them to \(x_1x_2x_3\).

**Solution.** Cartan and the line formula give
\[
\operatorname{Sq}^3(x_1x_2x_3)=x_1^2x_2^2x_3^2.
\]
The first square in the second expression is
\(\operatorname{Sq}^1(x_1x_2x_3)=\sum_i x_i^2\prod_{j\ne i}x_j\).
Applying \(\operatorname{Sq}^2\) to each term gives its term \(x_i^4\prod_{j\ne i}x_j\) and the term \(x_1^2x_2^2x_3^2\). There are three copies of the latter, which sum to one copy over \(F\). Therefore
\[
\operatorname{Sq}^2\operatorname{Sq}^1(x_1x_2x_3)
 =\sum_i x_i^4\prod_{j\ne i}x_j+x_1^2x_2^2x_3^2.
\]
The two polynomials are linearly independent: the second has the lexicographically largest term \(x_1^4x_2x_3\), absent from the first. This is the degree-three instance of the orbit argument, not an assumption about an abstract operation presentation.

**Exercise O.3 — Medium.** List the polynomial generators of \(H^*(K(F,2);F)\) through degree six, and give a basis in each positive degree through six.

**Solution.** The admissible sequences of excess less than two have excess zero or one. Besides the empty sequence, they begin \((1)\), \((2,1)\), \((4,2,1)\), with respective total indices one, three and seven. Thus through degree six the generators are \(x=\iota_2\) of degree two, \(y=\operatorname{Sq}^1\iota_2\) of degree three, and \(z=\operatorname{Sq}^2\operatorname{Sq}^1\iota_2\) of degree five. The next generator has degree nine. The bases are: degree one, none; degree two, \(x\); degree three, \(y\); degree four, \(x^2\); degree five, \(xy,z\); degree six, \(x^3,y^2\). Polynomial independence is supplied by K.2; the list is not inferred solely from nonzero square evaluations.

**Exercise O.4 — Hard.** Explain why bounded exponent, rather than merely two-primary torsion, is essential in the first-fibre argument G.1. Give a nonzero two-primary torsion group whose mod-two tensor product is zero.

**Solution.** If the first fibre group has exponent at most four, \(G=2G\) implies \(G=4G=0\). Thus a nonzero such group has \(G/2G\ne0\), which is the first mod-two fibre homology group. In contrast let \(G=\mathbb Z[1/2]/\mathbb Z\). Every element has order a power of two, and every element is twice another by replacing a dyadic fraction with half that fraction. Hence \(2G=G\), so \(G\otimes F=G/2G=0\), although the class of \(1/2\) is nonzero. The argument cannot discard its bounded-exponent hypothesis. No finite-generation hypothesis was needed for the proved bounded case.

**Exercise O.5 — Hard.** Compute \(\dim_F\mathcal N_j\) for \(0\leq j\leq3\) from the free-module comparison, and identify a generator in degree two.

**Solution.** The stable coefficient dimensions in these weights are the partition counts \(1,1,2,3\). The square algebra dimensions are \(1,1,1,2\), with bases the empty word, \(\operatorname{Sq}^1\), \(\operatorname{Sq}^2\), and \(\operatorname{Sq}^3,\operatorname{Sq}^2\operatorname{Sq}^1\). Taking dimensions in (M.10), starting with \(Q_0=F\), gives \(\dim Q_1=0\), \(\dim Q_2=1\), and \(\dim Q_3=0\). The finite comparison identifies \(\mathcal N_j\) with \(Q_j\) as vector spaces, so the required dimensions are \(1,0,1,0\). On \(\mathbb{RP}^2\), \(w_2=x^2\) evaluates to one. Its bordism class is nonzero, and hence generates the one-dimensional degree-two group. The degree-zero group is generated by one point and detected by parity.

**Exercise O.6 — Hard.** Show that \(\mathbb{CP}^2\) and \(\mathbb{RP}^2\times\mathbb{RP}^2\) are unoriented bordant by comparing all Stiefel–Whitney numbers.

**Solution.** For the complex projective plane, the Chern tangent calculation and the proved underlying-real comparison give \(w_1=w_3=0\), \(w_2=h\), \(w_4=h^2\), with \(\langle h^2,[\mathbb{CP}^2]_2\rangle=1\). Thus the numbers in the order
\[
 w_4,\quad w_1w_3,\quad w_2^2,\quad w_1^2w_2,\quad w_1^4
\tag{O.1}
\]
are \((1,0,1,0,0)\). These are all degree-four monomials, one for each partition of four.

For the real projective product write its ring as \(F[a,b]/(a^3,b^3)\). Whitney and the tangent formulas give
\[
w_1=a+b,\quad w_2=a^2+ab+b^2,\quad
w_3=a^2b+ab^2,\quad w_4=a^2b^2.
\]
Its fundamental class evaluates \(a^2b^2\) to one by the product normalization. The square of \(w_2\) is \(a^2b^2\). The fourth power of \(a+b\) is \(a^4+b^4=0\); its square times \(w_2\) has the two equal terms \(a^2b^2\), which cancel, and all remaining terms contain \(a^3\) or \(b^3\). Similarly \((a+b)(a^2b+ab^2)=0\). Its five numbers in (O.1) are therefore the identical list \((1,0,1,0,0)\). Theorem N.1 proves that the disjoint union bounds a compact smooth five-manifold, which is the claimed unoriented bordism. Both individual classes are nonzero, since their \(w_4\) number is one.

## P. Source and scope of the conclusion

The complete geometric correspondence, rank-controlled embeddings and normal collapse inverse are the earlier own Thom chapter, TheoremK.1. The exact universal mod-two ring is the Schubert chapter, Theorem4.1. Normalized Thom, external product and coefficient duality are the Thom/Euler chapter. The actual boundary fundamental-class and boundary-number proofs are the projective tangent chapter, Section4 and Theorem5.1. The first Hurewicz, CW model and Serre edge proofs are the own homotopy foundation companions. These are actual proved inputs in their stated hypotheses.

The square-algebra, module-coalgebra and Thom-module arguments are developed in [Haynes Miller’s *Notes on Cobordism*](https://math.mit.edu/~hrm/papers/cobordism.pdf), Sections9–12, based on his lectures and typed by Dan Christensen and Gerd Laures. The one-group, simple-generator and comparison calculations are also presented in [Allen Hatcher’s *Spectral Sequences*](https://pi.math.cornell.edu/~hatcher/SSAT/SSch1.pdf), Section1.3. The detection and polynomial-ring theorems originate in [René Thom’s paper](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/thomcob.pdf), ChapterIV; [John Milnor’s survey](https://www.e-periodica.ch/digbib/view?pid=ens-001:1962:8::12), Section1, records these conclusions and Dold’s representatives. Section N.2 gives their complete calculation using the established finite comparison.

The detection and product calculations hold for closed smooth manifolds in every nonnegative dimension. The representing-space splitting depends on chosen lifts and bases; the explicit polynomial generators give the ring presentation (N.4). The proof and solutions here are authored by the writing AI; any independent review remains separate.

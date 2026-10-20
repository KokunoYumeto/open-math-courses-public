# Finite symmetric tensor categories and fibre functors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lesson *Tannakian categories* reconstructs an affine group scheme from a rigid symmetric tensor category together with a fibre functor to finite-dimensional vector spaces. Many symmetric tensor categories have no such functor. In characteristic zero, Deligne proved that every symmetric tensor category in which the lengths of the tensor powers of each object grow at most exponentially admits a fibre functor to super vector spaces [Del]. In characteristic \(p>0\) super vector spaces are too small a target even for finite categories: the Verlinde category \(\operatorname{Ver}_p\) of Section 4 contains an object of Frobenius–Perron dimension \(2\cos(\pi/p)\), which is not an integer when \(p\ge5\) (Exercise 8.3). Ostrik proved that every semisimple finite symmetric tensor category admits a fibre functor to \(\operatorname{Ver}_p\) [Ost, Theorem 1.5]. Benson, Etingof and Ostrik constructed a tower
\[
\operatorname{Ver}_p\subset\operatorname{Ver}_{p^2}\subset\operatorname{Ver}_{p^3}\subset\cdots
\]
of finite symmetric tensor categories, the higher Verlinde categories, and conjectured that every symmetric tensor category whose tensor powers grow at most exponentially admits a fibre functor to their union [BEO, Conjecture 1.4].

This course proves the conjecture for finite categories: every finite symmetric tensor category over an algebraically closed field of characteristic \(p\) admits a fibre functor to \(\operatorname{Ver}_{p^n}\) for some \(n\). The proof was found by OpenAI in 2026 [OpenAI-208]. Its new ingredient is a theorem about representations of \(\mathrm{SL}_2\) in characteristic \(p\) (Theorem 5.2), proved with an equivariant vector bundle on the plane. That theorem is the hypothesis under which Coulembier and Flake constructed higher Frobenius functors [CF].

This lesson fixes the conventions, proves the general facts about finite tensor categories that the course uses, states the results taken from the literature, and describes the route of the proof.

**Prerequisites.** [*Tannakian categories*](course:GL-SAT/GL-SAT-09), Sections 1 and 9: rigid symmetric tensor categories, fibre functors to vector spaces, and the reason super vector spaces have none. Finite-dimensional algebras and their modules, including the Jacobson radical.

## 1. Finite symmetric tensor categories

Throughout the course \(k\) is an algebraically closed field of characteristic \(p>0\).

**Definition 1.1.** A *finite symmetric tensor category over \(k\)* is an essentially small \(k\)-linear abelian category \(\mathcal C\) with a symmetric monoidal structure: a bifunctor \(\otimes\), a unit object \(\mathbf 1\), and natural associativity, unit and symmetry isomorphisms \(c_{X,Y}\colon X\otimes Y\to Y\otimes X\), satisfying the coherence conditions and \(c_{Y,X}c_{X,Y}=\mathrm{id}\). We require:

1. \(\otimes\) is \(k\)-bilinear on morphisms and exact in each variable;
2. every object \(X\) has a dual \(X^*\), with evaluation \(\operatorname{ev}_X\colon X^*\otimes X\to\mathbf 1\) and coevaluation \(\operatorname{coev}_X\colon\mathbf 1\to X\otimes X^*\) satisfying the two triangle identities;
3. morphism spaces are finite dimensional, every object has finite length, there are finitely many isomorphism classes of simple objects, and every object is a quotient of a projective object;
4. \(\operatorname{End}(\mathbf 1)=k\).

**Definition 1.2.** Let \(\mathcal C,\mathcal D\) be finite symmetric tensor categories. A *tensor functor* \(F\colon\mathcal C\to\mathcal D\) is an additive functor with an isomorphism \(F(\mathbf 1)\cong\mathbf 1\) and natural isomorphisms \(J_{X,Y}\colon F(X)\otimes F(Y)\to F(X\otimes Y)\) compatible with the associativity and unit isomorphisms. It is *symmetric* if
\[
F(c_{X,Y})\circ J_{X,Y}=J_{Y,X}\circ c_{F(X),F(Y)}.
\]
A *fibre functor* is a \(k\)-linear, exact, faithful, symmetric tensor functor.

For a finite group \(G\), the category \(\operatorname{Rep}_k(G)\) of finite-dimensional representations is a finite symmetric tensor category, and the forgetful functor to the category \(\operatorname{Vec}_k\) of finite-dimensional vector spaces is a fibre functor. For \(p\ne2\), finite-dimensional super vector spaces with the Koszul sign rule form a finite symmetric tensor category \(\operatorname{sVec}_k\).

The next lemma identifies a finite symmetric tensor category, as an abelian category, with the modules over a finite-dimensional algebra. Its first part, the simplicity of the unit, is an argument of Deligne and Milne [DM, Proposition 1.17].

**Lemma 1.3.** Let \(\mathcal C\) be a finite symmetric tensor category.

1. The unit object \(\mathbf 1\) is simple.
2. \(\mathcal C\) has a projective generator \(P\): a projective object such that every object is a quotient of a finite direct sum of copies of \(P\).
3. For such \(P\), the functor \(\omega=\operatorname{Hom}(P,-)\) is exact and faithful, and it is an equivalence from \(\mathcal C\) to the category of finite-dimensional left modules over the finite-dimensional algebra \(A=\operatorname{End}(P)^{\mathrm{op}}\).

*Proof.* (1) Let \(i\colon U\to\mathbf 1\) be a subobject with cokernel \(\pi\colon\mathbf 1\to V\). We first show that \(V\otimes U=0\). The morphism \(\pi\otimes\mathrm{id}_U\colon\mathbf 1\otimes U\to V\otimes U\) is an epimorphism and \(\mathrm{id}_V\otimes i\colon V\otimes U\to V\otimes\mathbf 1\) is a monomorphism, by exactness of \(\otimes\). Their composite is \(\pi\otimes i\), which under the unit isomorphisms is \(\pi\circ i=0\). So the monomorphism \(\mathrm{id}_V\otimes i\) is zero, and \(V\otimes U=0\).

Let \(i^*\colon\mathbf 1\to U^*\) be the transpose of \(i\), and put \(W=\ker i^*\) with inclusion \(w\colon W\to\mathbf 1\). For a subobject \(j\colon T\to X\), the morphism
\[
(i^*\otimes\mathrm{id}_X)\circ j\colon T\to U^*\otimes X
\]
corresponds, under the duality adjunction \(\operatorname{Hom}(T,U^*\otimes X)\cong\operatorname{Hom}(U\otimes T,X)\), to \(i\otimes j\colon U\otimes T\to\mathbf 1\otimes X=X\), which is a monomorphism. Hence \((i^*\otimes\mathrm{id}_X)\circ j=0\) exactly when \(U\otimes T=0\). Since \(-\otimes X\) is exact, \(\ker(i^*\otimes\mathrm{id}_X)=W\otimes X\). So \(W\otimes X\) is the largest subobject of \(X\) whose tensor product with \(U\) vanishes (the symmetry identifies \(U\otimes T\) with \(T\otimes U\)).

For \(X=\mathbf 1\) this gives \(W\otimes U=0\). For \(X=V\) the whole object satisfies \(V\otimes U=0\), so \(w\otimes\mathrm{id}_V\colon W\otimes V\to V\) is an isomorphism. Tensoring \(0\to U\to\mathbf 1\to V\to0\) with \(W\) gives an exact sequence \(0\to W\otimes U\to W\to W\otimes V\to0\), so \(\mathrm{id}_W\otimes\pi\colon W\to W\otimes V\) is an isomorphism as well. The composite of these two isomorphisms is \(\pi\circ w\). Thus \(\pi\) has a section and \(\mathbf 1\cong U\oplus V\). The algebra \(\operatorname{End}(\mathbf 1)=k\) has no idempotents other than \(0\) and \(1\), so \(U=0\) or \(V=0\). Since \(\mathbf 1\ne0\), the unit is simple.

(2) Choose representatives \(S_1,\dots,S_t\) of the simple objects and epimorphisms \(Q_i\to S_i\) from projective objects, and put \(P=Q_1\oplus\cdots\oplus Q_t\). We show by induction on the length that every object \(X\ne0\) is a quotient of some \(P^{\oplus m}\). Let \(Y\subset X\) be a maximal proper subobject, so that \(X/Y\cong S_i\) for some \(i\). By induction there is an epimorphism \(P^{\oplus m}\to Y\), with \(m=0\) if \(Y=0\). Projectivity lifts \(Q_i\to S_i\) to a morphism \(Q_i\to X\), and the resulting morphism \(P^{\oplus m}\oplus Q_i\to X\) is an epimorphism. As \(Q_i\) is a direct summand of \(P\), the object \(X\) is a quotient of \(P^{\oplus(m+1)}\).

(3) The functor \(\omega\) is exact because \(P\) is projective. Let \(f\colon X\to Y\) be nonzero, with image \(I\ne0\). By (2) some morphism \(P\to I\) is nonzero; it lifts along the epimorphism \(X\to I\) to \(h\colon P\to X\), and \(fh\ne0\). So \(\omega\) is faithful. The algebra \(A\) acts on \(\omega(X)\) by precomposition, and \(\omega(P)=A\) is the regular module. For every \(Y\) the map \(\operatorname{Hom}(P,Y)\to\operatorname{Hom}_A(A,\omega Y)=\omega Y\) is the identity, so \(\omega\) is bijective on morphisms from finite direct sums of copies of \(P\). By (2), applied to \(X\) and to a kernel, every object has a presentation \(P^{\oplus m}\to P^{\oplus n}\to X\to0\), and \(\omega\) carries it to a presentation of \(\omega X\). Since \(\operatorname{Hom}(-,Y)\) and \(\operatorname{Hom}_A(-,\omega Y)\) are left exact, \(\operatorname{Hom}(X,Y)\) and \(\operatorname{Hom}_A(\omega X,\omega Y)\) are the kernels of corresponding maps between bijectively related groups, so \(\omega\) is fully faithful. Every finite-dimensional \(A\)-module \(M\) has a presentation \(A^m\to A^n\to M\to0\); the map \(A^m\to A^n\) is \(\omega\) of a morphism \(P^{\oplus m}\to P^{\oplus n}\), and \(\omega\) carries its cokernel to \(M\). Finally \(\dim_kA<\infty\) because morphism spaces are finite dimensional. \(\square\)

We fix such a \(P\) for each finite symmetric tensor category. Since \(\mathbf 1\) is simple, it is one of the \(S_i\), so there is an epimorphism \(P\to\mathbf 1\). The equivalence with \(A\)-modules also provides a projective cover of every simple object.

**Lemma 1.4.** Let \(\mathcal C\) be a finite symmetric tensor category and \(Y\ne0\) an object. The functor \(-\otimes Y\) is exact and faithful, sends nonzero objects to nonzero objects, and reflects exactness: if \(X'\xrightarrow{f}X\xrightarrow{g}X''\) satisfies \(gf=0\) and its tensor product with \(Y\) is exact at \(X\otimes Y\), then the sequence is exact at \(X\).

*Proof.* The coevaluation \(\operatorname{coev}_Y\) is nonzero, since otherwise the triangle identity \((\mathrm{id}_Y\otimes\operatorname{ev}_Y)\circ(\operatorname{coev}_Y\otimes\mathrm{id}_Y)=\mathrm{id}_Y\) would give \(Y=0\). As \(\mathbf 1\) is simple (Lemma 1.3), \(\operatorname{coev}_Y\) is a monomorphism. Tensoring with \(X\) gives a monomorphism \(X\to X\otimes Y\otimes Y^*\), so \(X\otimes Y=0\) forces \(X=0\). Exactness of \(-\otimes Y\) is part of Definition 1.1. If \(f\ne0\), then \(\operatorname{im}(f\otimes Y)=\operatorname{im}(f)\otimes Y\ne0\), so \(f\otimes Y\ne0\). For the last claim, exactness of \(-\otimes Y\) identifies \(H\otimes Y\), where \(H\) is the homology of the sequence at \(X\), with the homology of the tensored sequence, which is zero; hence \(H=0\). \(\square\)

Some functors in this course are linear only up to a field automorphism. For an automorphism \(\sigma\) of \(k\), an additive functor \(F\) between \(k\)-linear categories is *\(\sigma\)-semilinear* if \(F(af)=\sigma(a)F(f)\) for all \(a\in k\) and all morphisms \(f\).

**Lemma 1.5.** Let \(F\colon\mathcal C\to\mathcal D\) be an exact tensor functor between finite symmetric tensor categories, either \(k\)-linear or \(\sigma\)-semilinear. Then \(F(X)\ne0\) for every \(X\ne0\), and \(F\) is faithful.

*Proof.* Let \(X\ne0\). As in the proof of Lemma 1.4, \(\operatorname{coev}_X\colon\mathbf 1\to X\otimes X^*\) is a monomorphism. Its image under \(F\) is a monomorphism \(F(\mathbf 1)\to F(X\otimes X^*)\cong F(X)\otimes F(X^*)\), and \(F(\mathbf 1)\cong\mathbf 1\ne0\). Hence \(F(X)\ne0\). For a nonzero morphism \(f\), exactness gives \(\operatorname{im}F(f)\cong F(\operatorname{im}f)\ne0\). \(\square\)

## 2. Deligne products

**Theorem 2.1** (Deligne products [EGNO, Proposition 1.11.2 and Section 4.6]). Let \(\mathcal A\) and \(\mathcal B\) be \(k\)-linear abelian categories equivalent to the categories of finite-dimensional modules over finite-dimensional algebras \(A\) and \(B\).

1. There is a \(k\)-linear abelian category \(\mathcal A\boxtimes\mathcal B\) with a bifunctor \(\boxtimes\colon\mathcal A\times\mathcal B\to\mathcal A\boxtimes\mathcal B\), right exact in each variable, such that every \(k\)-bilinear bifunctor out of \(\mathcal A\times\mathcal B\) that is right exact in each variable factors, uniquely up to unique isomorphism, as \(\boxtimes\) followed by a right exact functor. One may take \(\mathcal A\boxtimes\mathcal B\) to be the finite-dimensional \((A\otimes_kB)\)-modules, with \(X\boxtimes Y=X\otimes_kY\).
2. The bifunctor \(\boxtimes\) is exact in each variable, and \(\operatorname{Hom}(X\boxtimes Y,X'\boxtimes Y')\)\(=\operatorname{Hom}(X,X')\)\(\otimes_k\operatorname{Hom}(Y,Y')\).
3. If \(\mathcal A\) and \(\mathcal B\) are finite symmetric tensor categories, then so is \(\mathcal A\boxtimes\mathcal B\), with unit \(\mathbf 1\boxtimes\mathbf 1\), symmetry \(c\boxtimes c\) and
\[
\begin{aligned}
&(X\boxtimes Y)\otimes(X'\boxtimes Y')\\
&\quad=(X\otimes X')\boxtimes(Y\otimes Y').
\end{aligned}
\]

**Lemma 2.2.** In the situation of Theorem 2.1, the simple objects of \(\mathcal A\boxtimes\mathcal B\) are the objects \(S\boxtimes T\) with \(S\) simple in \(\mathcal A\) and \(T\) simple in \(\mathcal B\), and distinct pairs of isomorphism classes give non-isomorphic objects.

*Proof.* The ideal \(N=J(A)\otimes B+A\otimes J(B)\) of \(A\otimes B\) is nilpotent: if \(J(A)^m=0\) and \(J(B)^m=0\), then \(N^{2m}\) is spanned by products lying in \(J(A)^i\otimes J(B)^j\) with \(i+j=2m\), and \(i\ge m\) or \(j\ge m\). The quotient by \(N\) is \((A/J(A))\otimes(B/J(B))\). Since \(k\) is algebraically closed, \(A/J(A)\cong\prod_iM_{n_i}(k)\) and \(B/J(B)\cong\prod_jM_{m_j}(k)\), so the quotient is \(\prod_{i,j}M_{n_im_j}(k)\). A nilpotent ideal acts by zero on every simple module. So the simple \(A\otimes B\)-modules are the simple modules of this product of matrix algebras, namely the modules \(k^{n_i}\otimes k^{m_j}=S_i\otimes T_j\), which are pairwise non-isomorphic. \(\square\)

**Lemma 2.3.** Let \(\mathcal A_1,\dots,\mathcal A_s,\mathcal Z\) be finite symmetric tensor categories and \(F_i\colon\mathcal A_i\to\mathcal Z\) exact \(k\)-linear symmetric tensor functors.

1. There is an exact \(k\)-linear symmetric tensor functor \(H\colon\mathcal A_1\boxtimes\cdots\boxtimes\mathcal A_s\to\mathcal Z\) with
\[
\begin{aligned}
&H(X_1\boxtimes\cdots\boxtimes X_s)\\
&\quad=F_1(X_1)\otimes\cdots\otimes F_s(X_s).
\end{aligned}
\]
2. If \(F\colon\mathcal A\to\mathcal A'\) and \(G\colon\mathcal B\to\mathcal B'\) are exact \(k\)-linear tensor functors between finite symmetric tensor categories, then \(F\boxtimes G\colon\mathcal A\boxtimes\mathcal B\to\mathcal A'\boxtimes\mathcal B'\), the functor induced by \((X,Y)\mapsto F(X)\boxtimes G(Y)\), is an exact tensor functor, symmetric when \(F\) and \(G\) are.

*Proof.* (1) The multilinear functor \((X_1,\dots,X_s)\mapsto\bigotimes_iF_i(X_i)\) is exact in each variable, so by Theorem 2.1(1), applied one factor at a time, it induces a right exact functor \(H\). The tensor structure of \(H\) on exterior products is given by the tensor structures of the \(F_i\) together with the symmetry of \(\mathcal Z\), which reorders the factors of
\[
\textstyle\bigotimes_iF_i(X_i)\otimes\bigotimes_iF_i(X'_i).
\]
These isomorphisms are natural in each variable, so the universal property extends them, and their inverses, to natural isomorphisms of right exact functors on the Deligne product. The coherence identities hold on exterior products because the symmetry of \(\mathcal Z\) is coherent, and they extend by the uniqueness in the universal property. A tensor functor carries a dual pair \((X,X^*,\operatorname{ev},\operatorname{coev})\) to a dual pair, so \(H(X^*)\cong H(X)^*\) naturally.

It remains to prove left exactness. Let \(0\to X'\to X\to X''\to0\) be exact. Duality is an exact contravariant autoequivalence of a rigid abelian category, so \(0\to X''^*\to X^*\to X'^*\to0\) is exact. Right exactness of \(H\) gives an exact sequence \(H(X''^*)\to H(X^*)\to H(X'^*)\to0\), that is, \(H(X'')^*\to H(X)^*\to H(X')^*\to0\). Dualizing in \(\mathcal Z\) gives the exact sequence \(0\to H(X')\to H(X)\to H(X'')\).

(2) The same argument applies, with the componentwise tensor structure of Theorem 2.1(3) in place of the reordering. \(\square\)

## 3. Dimensions

The Grothendieck ring \(K_0(\mathcal C)\) of a finite symmetric tensor category is the free abelian group on the isomorphism classes of simple objects. The class of an object is \([X]=\sum_S[X:S][S]\), where \([X:S]\) is the multiplicity of \(S\) as a composition factor, and \([X][Y]=[X\otimes Y]\). It is a commutative ring because of the symmetry, and \([X]=[X']+[X'']\) for every short exact sequence \(0\to X'\to X\to X''\to0\).

**Theorem 3.1** (Frobenius–Perron dimension [EGNO, Propositions 3.3.4, 3.3.6 and 4.5.4]). Let \(\mathcal C\) be a finite symmetric tensor category. There is a unique ring homomorphism
\[
\operatorname{FPdim}\colon K_0(\mathcal C)\to\mathbb R
\]
taking positive values on the classes of the simple objects. Its value on the class of each simple object is at least \(1\); it is the largest real eigenvalue of multiplication by that class on \(K_0(\mathcal C)\otimes\mathbb R\).

We write \(\operatorname{FPdim}(X)\) for \(\operatorname{FPdim}([X])\). It is additive on short exact sequences and multiplicative on tensor products, and \(\operatorname{FPdim}(X)\ge1\) for every nonzero \(X\), by adding over the composition factors.

**Lemma 3.2.**

1. In a Deligne product of finite symmetric tensor categories, \(\operatorname{FPdim}(X\boxtimes Y)\)\(=\operatorname{FPdim}(X)\operatorname{FPdim}(Y)\).
2. \(\operatorname{FPdim}(X^*)=\operatorname{FPdim}(X)\).
3. If \(F\colon\mathcal C\to\mathcal D\) is an exact tensor functor between finite symmetric tensor categories, \(k\)-linear or \(\sigma\)-semilinear, then \(\operatorname{FPdim}(F(X))=\operatorname{FPdim}(X)\) for every \(X\).
4. A simple object \(B\) with \(\operatorname{FPdim}(B)=1\) is invertible: \(\operatorname{coev}_B\colon\mathbf 1\to B\otimes B^*\) is an isomorphism.

*Proof.* (1) By Lemma 2.2 and exactness of \(\boxtimes\) in each variable, \([X]\otimes[Y]\mapsto[X\boxtimes Y]\) is an isomorphism of rings \(K_0(\mathcal C)\otimes K_0(\mathcal D)\to K_0(\mathcal C\boxtimes\mathcal D)\) carrying products of simple classes to simple classes. Hence \([S\boxtimes T]\mapsto\operatorname{FPdim}(S)\operatorname{FPdim}(T)\) is a ring homomorphism that is positive on simple classes, and by uniqueness it is \(\operatorname{FPdim}\).

(2) Duality is exact and contravariant, sends simple objects to simple objects, and \((X\otimes Y)^*\cong Y^*\otimes X^*\cong X^*\otimes Y^*\). So \([X]\mapsto[X^*]\) is a ring automorphism of \(K_0(\mathcal C)\) permuting the simple classes, and \(X\mapsto\operatorname{FPdim}(X^*)\) is a ring homomorphism positive on simple classes. By uniqueness it is \(\operatorname{FPdim}\).

(3) Exactness makes \([X]\mapsto[F(X)]\) a well-defined additive map \(K_0(\mathcal C)\to K_0(\mathcal D)\), and the tensor structure makes it a unital ring homomorphism. Composed with \(\operatorname{FPdim}\) of \(\mathcal D\), it takes the value \(\operatorname{FPdim}(F(S))>0\) on a simple \(S\), because \(F(S)\ne0\) by Lemma 1.5. By uniqueness the composite is \(\operatorname{FPdim}\) of \(\mathcal C\).

(4) The coevaluation is a monomorphism, as in the proof of Lemma 1.4. Its cokernel \(Q\) satisfies \(\operatorname{FPdim}(Q)\)\(=\operatorname{FPdim}(B)\operatorname{FPdim}(B^*)-1\)\(=0\) by (2), and a nonzero object has \(\operatorname{FPdim}\ge1\). So \(Q=0\). \(\square\)

The *categorical dimension* takes values in \(k\). In a finite symmetric tensor category the symmetry defines the Drinfeld morphism \(u_X\colon X\to X^{**}\) [EGNO, Definition 8.9.4]; because \(c_{Y,X}c_{X,Y}=\mathrm{id}\), it is an isomorphism of tensor functors, that is, a pivotal structure [EGNO, the remark after Definition 8.9.4, and Proposition 8.10.6]. The categorical dimension \(\dim(X)\in\operatorname{End}(\mathbf 1)=k\) is the trace of \(u_X\) [EGNO, Definitions 4.7.1 and 4.7.11]; it equals the composite
\[
\mathbf 1\xrightarrow{\operatorname{coev}_X}X\otimes X^*\xrightarrow{c_{X,X^*}}X^*\otimes X\xrightarrow{\operatorname{ev}_X}\mathbf 1 .
\]

**Theorem 3.3** (categorical dimension [EGNO, Proposition 4.7.12]). In a finite symmetric tensor category, \([X]\mapsto\dim(X)\) is a ring homomorphism \(K_0(\mathcal C)\to k\).

**Lemma 3.4.**

1. A \(k\)-linear symmetric tensor functor \(F\) satisfies \(\dim(F(X))=\dim(X)\).
2. In \(\operatorname{Rep}_k(G)\) for a finite group \(G\), \(\dim(V)\) is the image of \(\dim_kV\) in \(k\).
3. If \(B\) is invertible, then \(\dim(B)\ne0\).

*Proof.* (1) After the identifications \(F(X^*)\cong F(X)^*\) and \(F(X\otimes X^*)\cong F(X)\otimes F(X)^*\), the functor \(F\) carries \(\operatorname{coev}_X\), \(c_{X,X^*}\) and \(\operatorname{ev}_X\) to the corresponding morphisms for \(F(X)\), because it is a symmetric tensor functor. So \(F(\dim(X)\,\mathrm{id}_{\mathbf 1})=\dim(F(X))\,\mathrm{id}_{\mathbf 1}\), and \(k\)-linearity gives \(F(\dim(X)\,\mathrm{id}_{\mathbf 1})=\dim(X)\,\mathrm{id}_{\mathbf 1}\).

(2) For a basis \((e_i)\) of \(V\) with dual basis \((e^i)\), the displayed composite sends \(1\) to \(\sum_ie_i\otimes e^i\), then to \(\sum_ie^i\otimes e_i\), then to \(\sum_ie^i(e_i)=\dim_kV\).

(3) By Theorem 3.3, \(\dim(B)\dim(B^*)\)\(=\dim(B\otimes B^*)\)\(=\dim(\mathbf 1)=1\). \(\square\)

## 4. The Verlinde tower

Let \(\mathbb Z/p\) act on vector spaces through a generator \(g\). Since \((g-1)^p=g^p-1=0\), the indecomposable representations are the Jordan blocks \(J_1,\dots,J_p\), where \(g-1\) acts on \(J_i\) by a single nilpotent Jordan block of size \(i\).

**Definition 4.1** ([EO, Section 2.3]). A morphism \(f\colon X\to Y\) in \(\operatorname{Rep}_k(\mathbb Z/p)\) is *negligible* if \(\operatorname{tr}(hf)=0\) for every \(h\colon Y\to X\). Negligible morphisms form a tensor ideal. The *Verlinde category* \(\operatorname{Ver}_p(k)\) has the objects of \(\operatorname{Rep}_k(\mathbb Z/p)\) and the morphisms modulo negligible morphisms.

The category \(\operatorname{Ver}_p(k)\) is a semisimple finite symmetric tensor category with simple objects \(L_1=\mathbf 1,L_2,\dots,L_{p-1}\), the images of \(J_1,\dots,J_{p-1}\); the image of \(J_p\) is zero (Exercise 8.1). Its fusion rules and dimensions are [EO, Section 2.3 and Lemma 2.3]
\[
\begin{gathered}
L_r\otimes L_s\cong\bigoplus_{i=1}^{m}L_{|r-s|+2i-1},\\
m=\min(r,s,p-r,p-s),\\
\operatorname{FPdim}(L_r)=\frac{\sin(\pi r/p)}{\sin(\pi/p)}.
\end{gathered}
\]
In particular \(\operatorname{Ver}_2(k)\simeq\operatorname{Vec}_k\), and \(\operatorname{Ver}_3(k)\simeq\operatorname{sVec}_k\), the object \(L_2\) being an odd line.

The higher levels are built from tilting modules of \(\mathrm{SL}_2\), which are studied in Lesson 2. Write \(\mathcal T\) for the additive category of tilting modules of \(\mathrm{SL}_2\) over \(k\), \(T(a)\) for the indecomposable tilting module of highest weight \(a\), and \(I_n\) for the tensor ideal of morphisms that factor through a direct sum of modules \(T(a)\) with \(a\ge p^n-1\).

**Theorem 4.2** (higher Verlinde categories [BEO]). For each \(n\ge1\) there is a finite symmetric tensor category \(\operatorname{Ver}_{p^n}(k)\) with the following properties.

1. \(\operatorname{Ver}_{p^1}(k)\) is the category \(\operatorname{Ver}_p(k)\) of Definition 4.1 [BEO, Theorem 4.5(i)].
2. There is a fully faithful \(k\)-linear symmetric monoidal functor \(\Sigma_n\colon\mathcal T/I_n\to\operatorname{Ver}_{p^n}(k)\) from the additive quotient category [BEO, Section 3.1 and Theorem 4.2(i)].
3. For \(n\ge2\) there is an exact, fully faithful, symmetric tensor functor \(\operatorname{Ver}_{p^{n-1}}(k)\to\operatorname{Ver}_{p^n}(k)\) [BEO, Theorem 4.34]. We regard the tower as a sequence of tensor subcategories.
4. \(\operatorname{Ver}_{p^n}(k)\) is defined over \(\mathbb F_p\): for every automorphism \(\sigma\) of \(k\) there is a \(\sigma\)-semilinear, exact, symmetric tensor autoequivalence of \(\operatorname{Ver}_{p^n}(k)\) [BEO, Section 4.9; CF, Remark 2.3.8].
5. If \(p=2\), the category \(\operatorname{Ver}_4(k)\) contains a tensor subcategory \(\operatorname{Ver}_4^+(k)\) equivalent, as a symmetric tensor category, to the category \(\mathcal C_1\) of finite-dimensional modules over the Hopf algebra \(k[d]/(d^2)\) with \(d\) primitive and \(R\)-matrix \(1\otimes1+d\otimes d\) [BEO, Theorem 4.5(iii); BE, Introduction].

The tensor subcategories and the incompressibility of the higher Verlinde categories are stated in Lesson 9, where they are used.

## 5. The theorem

**Theorem 5.1** ([OpenAI-208, Theorem 1.1]). For every prime \(p\), every algebraically closed field \(k\) of characteristic \(p\) and every finite symmetric tensor category \(\mathcal C\) over \(k\), there are an integer \(n\ge1\) and a fibre functor
\[
\mathcal C\longrightarrow\operatorname{Ver}_{p^n}(k).
\]

The level \(n\) depends on \(\mathcal C\), and the theorem includes \(p=2\). It makes no assertion about symmetric tensor categories that are not finite.

The main new input concerns the group \(U\) of upper unitriangular matrices in \(\mathrm{SL}_2(k)\), isomorphic to the additive group of \(k\). Let \(\operatorname{St}_m\) be the simple \(\mathrm{SL}_2\)-module of highest weight \(p^m-1\) (Lesson 2).

**Theorem 5.2** (restricted tilting [OpenAI-208, Theorem 3.1]). Let \(r\ge1\), let \(E_r=(\mathbb Z/p)^r\), and let \(\iota\colon E_r\to U(k)\) be an injective homomorphism, with restriction functor \(R_\iota\). For every finite-dimensional \(kE_r\)-module \(D\) there is a tilting \(\mathrm{SL}_2\)-module \(T\) with
\[
R_\iota(\operatorname{St}_{r-1})\otimes D\cong R_\iota(T).
\]

Coulembier and Flake conjectured Theorem 5.2 and proved it in special cases [CF, Conjecture 5.4.2(1)]. Lesson 9 derives three consequences of Theorem 5.1: the finite symmetric tensor categories all of whose exact symmetric tensor functors are fully faithful are exactly the higher Verlinde categories and their even parts; in characteristic two the fibre functor to the union of the tower is unique; and every finite symmetric tensor category is the representation category of an affine group scheme internal to a higher Verlinde category.

## 6. Results used without proof

The course proves every step of the argument except the following results from the literature. Each is stated precisely where it is used, with a freely accessible source.

| Named result | Content | Used in |
|---|---|---|
| N1 | the higher Verlinde categories (Theorem 4.2) | Lessons 1, 5, 8 and 9 |
| N2 | Deligne products, Frobenius–Perron dimension, categorical dimension (Theorems 2.1, 3.1 and 3.3) | Lessons 1, 5, 8 and 9 |
| N3 | rational representations of \(\mathrm{SL}_2\): highest weights, Steinberg's tensor product theorem, standard and costandard filtrations, tilting modules | Lessons 2, 3, 4 and 7 |
| N4 | reflexive coherent sheaves on regular surfaces | Lesson 3 |
| N5 | the higher Frobenius construction of Coulembier and Flake | Lesson 5 |
| N6 | Chouinard's theorem, Dade's lemma and the tensor product theorem for rank varieties | Lessons 6 and 7 |
| N7 | nonzero tensor ideals of the symmetric group category contain a total symmetrizer | Lesson 6 |
| N8 | the Frobenius functor of Etingof and Ostrik | Lesson 8 |
| N9 | the extension theorem of Etingof and Gelaki in characteristic two | Lesson 8 |
| N10 | generalized Tannaka reconstruction and uniqueness in characteristic two, by Coulembier, Etingof and Ostrik | Lesson 9 |

## 7. The route of the proof

Lesson 2 collects the representation theory of \(\mathrm{SL}_2\) that the course uses and proves that tensoring with a Steinberg module makes modules with bounded highest weights tilting. Lessons 3 and 4 prove Theorem 5.2. Given a \(kE_r\)-module \(D\), Lesson 3 builds an \(\mathrm{SL}_2\)-equivariant vector bundle on the plane whose fibre at \((1,0)\) restricts to \(D\) and whose fibre at the origin has highest weights below \(p^r\). Lesson 4 shows that a bundle whose origin fibre is tilting has, at \((1,0)\), the restriction of that fibre to \(U\).

Lesson 5 records the construction of Coulembier and Flake, which Theorem 5.2 makes available. For each \(r\) and each embedding \(\iota\) it gives a symmetric tensor functor \(\Theta\colon\operatorname{Rep}_k(E_r)\to\operatorname{Ver}_{p^r}(k)\) and an additive symmetric tensor functor
\[
\begin{gathered}
\Phi\colon\mathcal C\to\mathcal C\boxtimes\operatorname{Ver}_{p^r}(k),\\
\Phi(X)=\Theta_{\mathcal C}(X^{\otimes p^r}),
\end{gathered}
\]
where \(E_r\) permutes the tensor factors regularly. The functor \(\Phi\) is exact as soon as \(\Theta\) does not kill the \(E_r\)-module \(\operatorname{Hom}(P,P^{\otimes p^r})\). Lesson 6 finds the least \(r\) for which this module is not projective, and Lesson 7 uses rank varieties to choose \(\iota\) so that \(\Theta\) does not kill it.

Lesson 8 removes the factor \(\mathcal C\) from the target. A comparison of Frobenius–Perron dimensions with a congruence modulo \(p\) shows that, after finitely many iterations of \(\Phi\), every composition factor has its first component in the subcategory on which the Frobenius functor of Etingof and Ostrik is exact. That subcategory, and its closure under extensions, admit fibre functors to \(\operatorname{Ver}_p\) for odd \(p\) and to \(\operatorname{Ver}_4^+\) for \(p=2\). Combining all factors in one level \(\operatorname{Ver}_{p^n}\) and undoing the field automorphism proves Theorem 5.1. Lesson 9 proves the consequences.

## 8. Exercises

**8.1.** Let \(J_i\) be the Jordan block representation of \(\mathbb Z/p\) of dimension \(i\). Show that \(\mathrm{id}_{J_p}\) is negligible and that \(\mathrm{id}_{J_i}\) is not negligible for \(1\le i\le p-1\).

**8.2.** In \(\operatorname{Ver}_5(k)\), use the fusion rules of Section 4 to show \(L_2\otimes L_2\cong L_1\oplus L_3\), \(L_4\otimes L_2\cong L_3\) and \(L_4\otimes L_4\cong L_1\). Deduce from Theorem 3.1 that \(\operatorname{FPdim}(L_2)=(1+\sqrt5)/2\), and compare with the formula \(\sin(2\pi/5)/\sin(\pi/5)\).

**8.3.** Show that for \(p\ge5\) there is no fibre functor from \(\operatorname{Ver}_p(k)\) to \(\operatorname{Vec}_k\) or to \(\operatorname{sVec}_k\).

**8.4.** For finite groups \(G\) and \(H\), show that \(\operatorname{Rep}_k(G)\boxtimes\operatorname{Rep}_k(H)\) is equivalent to \(\operatorname{Rep}_k(G\times H)\) as a symmetric tensor category, with \(V\boxtimes W\) corresponding to \(V\otimes_kW\).

## 9. Solutions

**8.1.** The module \(J_p\) is the regular representation \(k[g]/(g^p-1)=k[x]/(x^p)\) with \(x=g-1\), and its endomorphisms are the multiplications by elements \(\sum_ja_jx^j\). Multiplication by \(x^j\) with \(j\ge1\) is nilpotent, so has trace zero, and \(\operatorname{tr}(\mathrm{id})=p=0\) in \(k\). So every endomorphism \(h\) of \(J_p\) has \(\operatorname{tr}(h\circ\mathrm{id})=0\), and \(\mathrm{id}_{J_p}\) is negligible; hence \(J_p\cong0\) in \(\operatorname{Ver}_p(k)\). For \(i\le p-1\), taking \(h=\mathrm{id}\) gives \(\operatorname{tr}(\mathrm{id}_{J_i})=i\ne0\) in \(k\).

**8.2.** With \(p=5\): for \(r=s=2\), \(m=\min(2,2,3,3)=2\) and the summands are \(L_1,L_3\). For \(r=4,s=2\), \(m=\min(4,2,1,3)=1\) and the summand is \(L_3\). For \(r=s=4\), \(m=1\) and the summand is \(L_1\). Write \(d_i=\operatorname{FPdim}(L_i)>0\). Then \(d_4^2=1\), so \(d_4=1\), and \(d_3=d_4d_2=d_2\). The first rule gives \(d_2^2=1+d_3=1+d_2\), whose positive root is \((1+\sqrt5)/2\). The formula gives \(\sin(2\pi/5)/\sin(\pi/5)\)\(=2\cos(\pi/5)\)\(=(1+\sqrt5)/2\).

**8.3.** On \(\operatorname{Vec}_k\) the ring homomorphism \([V]\mapsto\dim_kV\) is positive on the simple class, so it is \(\operatorname{FPdim}\). On \(\operatorname{sVec}_k\), with \(K_0=\mathbb Z[\varepsilon]/(\varepsilon^2-1)\), the positive homomorphism sends \(\varepsilon\mapsto1\), so \(\operatorname{FPdim}\) is again the total dimension. In both cases every value is an integer. A fibre functor preserves \(\operatorname{FPdim}\) by Lemma 3.2(3), but \(\operatorname{FPdim}(L_2)\)\(=\sin(2\pi/p)/\sin(\pi/p)\)\(=2\cos(\pi/p)\) lies strictly between \(1\) and \(2\) for \(p\ge5\).

**8.4.** By Theorem 2.1(1) the Deligne product is the category of finite-dimensional modules over \(kG\otimes kH\), with \(V\boxtimes W=V\otimes W\). The algebra map \(kG\otimes kH\to k[G\times H]\), \(g\otimes h\mapsto(g,h)\), is an isomorphism, and under it \((g,h)\) acts on \(V\otimes W\) by \(g\otimes h\). The tensor product of Theorem 2.1(3) is \((V\otimes W)\otimes(V'\otimes W')\)\(\cong(V\otimes V')\otimes(W\otimes W')\), by the interchange of the middle factors; this linear isomorphism is equivariant for the diagonal action of \(G\times H\). It carries the symmetry \(c\boxtimes c\) to the flip of \(V\otimes W\) and \(V'\otimes W'\), which is the symmetry of \(\operatorname{Rep}_k(G\times H)\).

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 1 (the theorem and its background) and Section 2 (finite conventions and Deligne products). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [BEO] D. Benson, P. Etingof and V. Ostrik, *New incompressible symmetric tensor categories in positive characteristic*, Duke Math. J. 172 (2023), numbering of arXiv:2003.10499v4: Conjecture 1.4, Section 3.1, Theorems 4.2, 4.5 and 4.34, Section 4.9. https://arxiv.org/abs/2003.10499v4
- [EO] P. Etingof and V. Ostrik, *On the Frobenius functor for symmetric tensor categories in positive characteristic*, J. reine angew. Math. 773 (2021), numbering of arXiv:1912.12947v2: Section 2.3 and Lemma 2.3. https://arxiv.org/abs/1912.12947v2
- [EGNO] P. Etingof, S. Gelaki, D. Nikshych and V. Ostrik, *Tensor categories*, Amer. Math. Soc., 2015, authors' final version: Propositions 1.11.2, 3.3.4, 3.3.6, 4.5.4, 4.7.12 and 8.10.6, Definitions 4.7.1, 4.7.11 and 8.9.4, Section 4.6. https://math.mit.edu/~etingof/egnobookfinal.pdf
- [DM] P. Deligne and J. S. Milne, *Tannakian categories*, corrected version of 2022, Proposition 1.17. https://www.jmilne.org/math/xnotes/tc2022.pdf
- [CF] K. Coulembier and J. Flake, *Towards higher Frobenius functors for symmetric tensor categories*, Selecta Math. 32 (2026), numbering of arXiv:2405.19506v2: Remark 2.3.8 and Conjecture 5.4.2. https://arxiv.org/abs/2405.19506v2
- [BE] D. Benson and P. Etingof, *Symmetric tensor categories in characteristic 2*, Adv. Math. 351 (2019), Introduction. https://arxiv.org/abs/1807.05549v4
- [Ost] V. Ostrik, *On symmetric fusion categories in positive characteristic*, Selecta Math. 26 (2020), Theorem 1.5. https://arxiv.org/abs/1503.01492
- [Del] P. Deligne, *Catégories tensorielles*, Moscow Math. J. 2 (2002), 227–248. https://www.mathnet.ru/eng/mmj54

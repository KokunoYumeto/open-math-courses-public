# Weak complete intersections

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A homomorphism of rings \(A\to B\) of a topos is a *weak complete intersection* when its cotangent complex \(L_{B/A}\) has tor amplitude in \([-1,0]\): it is isomorphic in \(D(B)\) to a complex of flat \(B\)-modules in degrees \(-1\) and \(0\). Polynomial algebras, quotients by weakly regular ideals, and local complete intersection homomorphisms of rings and morphisms of schemes are weak complete intersections. The class is stable under composition, under cancellation of a factor whose cotangent complex is a flat module in degree \(0\), under faithfully flat descent, and under Tor-independent base change in a topos with enough points. If \(B\) is a quotient of an \(A\)-algebra \(P\) whose cotangent complex is a flat module of differentials, then \(B\) is a weak complete intersection over \(A\) exactly when the kernel \(I\) is weakly regular, and then \(L_{B/A}\) is the two-term complex \(I/I^2\to\Omega_{P/A}\otimes_PB\). The lesson proves:

- properties of tor amplitude: connectivity, triangles, base change and faithfully flat descent;
- examples of weak complete intersections;
- stability under composition, cancellation and faithfully flat descent;
- the criterion for quotients of algebras with flat differentials, and the two-term model of the cotangent complex, through the connecting map of the transitivity triangle;
- stability under Tor-independent base change in a topos with enough points, and for schemes.

**Prerequisites.** [*The fundamental spectral sequence*](the-fundamental-spectral-sequence.md) (Proposition 1.1, Theorem 4.2); [*Weakly regular ideals*](weakly-regular-ideals.md) (Definition 2.4, Proposition 4.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Lemma 4.2); [*Deformations of diagrams of schemes*](deformations-of-diagrams-of-schemes.md) (Proposition 1.4); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#2-independence-of-the-resolution) (Theorem 2.2, Proposition 3.1, Theorem 4.1, Section 10 with Proposition 10.1). From the AI-integrated Stacks project: tor amplitude [[Stacks, Tag 08FZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-tor-amplitude)], its description by flat complexes [[Tag 08G1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-tor-amplitude)], its behaviour in triangles [[Tag 08G2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-cone-tor-amplitude)]; bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)], and K-flat resolutions exist [[Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution)]; the cotangent complex of sheaves of rings and its inverse images [[Tag 08SV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-pullback-cotangent-morphism-topoi)], stalks [[Tag 08T0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-stalk-cotangent-complex)], \(H^0\) [[Tag 08UR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-H0-L-morphism-sheaves-rings)] and the transitivity triangle [[Tag 08SZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-triangle-sheaves-rings)]; local complete intersection homomorphisms of rings [[Tag 07D0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-local-complete-intersection)] and their cotangent complexes [[Tag 08SL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-proposition-cotangent-complex-local-complete-intersection)]; local complete intersection morphisms of schemes [[Tag 069F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-lci)] and their affine case [[Tag 07DB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-affine-lci)].

## Conventions

\(T\) is a topos and rings are commutative. For a ring \(B\) of \(T\), an object \(E\) of \(D(B)\) has *tor amplitude in \([a,b]\)* if \(H^i(E\otimes^{\mathbf L}_BF)=0\) for every \(B\)-module \(F\) and every \(i\notin[a,b]\) [Tag 08FZ]; this holds if and only if \(E\) is represented by a complex of flat \(B\)-modules in degrees \([a,b]\) [Tag 08G1]. A \(B\)-algebra \(C\) is *faithfully flat* if \(C\otimes_B-\) is exact and \(C\otimes_BM=0\) only for \(M=0\).

For a homomorphism of rings \(A\to B\) of \(T\), \(L_{B/A}=\Omega_{P/A}\otimes_PB\), with \(P\) the standard resolution, regarded as a complex of flat \(B\)-modules in degrees \(\leq0\) (Section 10 of *The cotangent complex*); \(H^0(L_{B/A})=\Omega_{B/A}\) [Tag 08UR], and inverse images along morphisms of topoi carry \(L_{B/A}\) to the cotangent complex of the inverse images [Tag 08SV]. For homomorphisms \(A\to B\to C\) there is the *transitivity triangle*
\[
\begin{aligned}&L_{B/A}\otimes^{\mathbf L}_BC\to L_{C/A}\to L_{C/B}\\&\quad\xrightarrow{\ K\ }L_{B/A}\otimes^{\mathbf L}_BC[1],\end{aligned}
\]
whose first two maps are the functoriality maps; it is natural in the triple (Theorem 4.1 of *The cotangent complex*, in the sheaf form of its Section 10 [Tag 08SZ]). For a quotient \(B=A/I\), \(\partial_L\colon H^{-1}(L_{B/A})\to I/I^2\) is the isomorphism of Proposition 1.1 (3) of the lesson on the fundamental spectral sequence, natural in the pair \((A,I)\).

## 1. Tor amplitude

**Lemma 1.1.** Let \(B\) be a ring of \(T\) and \(E\) an object of \(D(B)\).

1. If \(E\) has tor amplitude in \([a,b]\) with \(a\leq0\leq b\), and \(H^i(E)=0\) for \(i>0\), then \(E\) has tor amplitude in \([a,0]\).
2. If \(E\) has tor amplitude in \([a,b]\) and \(C\) is a \(B\)-algebra, then \(E\otimes^{\mathbf L}_BC\) has tor amplitude in \([a,b]\) in \(D(C)\).
3. If \(C\) is a faithfully flat \(B\)-algebra and \(E\otimes^{\mathbf L}_BC\) has tor amplitude in \([a,b]\) in \(D(C)\), then \(E\) has tor amplitude in \([a,b]\).
4. Let \(K\to L\to M\to K[1]\) be a distinguished triangle in \(D(B)\). If \(K\) and \(M\) have tor amplitude in \([a,b]\), so has \(L\).

**Proof.** (1) By Lemma 4.2 (1) of the lesson on non-additive functors, \(E\) is represented by a complex \(X\) of flat modules vanishing in positive degrees, which is K-flat [Tag 06YQ]. So \(E\otimes^{\mathbf L}_BF\) is represented by \(X\otimes_BF\), which vanishes in positive degrees, for every \(F\).

(2) By [Tag 08G1], \(E\) is represented by a complex \(X\) of flat modules in degrees \([a,b]\). It is K-flat, so \(E\otimes^{\mathbf L}_BC\) is represented by \(X\otimes_BC\), a complex of flat \(C\)-modules in degrees \([a,b]\).

(3) Let \(X\) be a K-flat complex representing \(E\) [Tag 06YS]. Then \(X\otimes_BC\) is K-flat over \(C\) and represents \(E\otimes^{\mathbf L}_BC\). For a \(B\)-module \(M\), \((X\otimes_BC)\otimes_C(C\otimes_BM)=\) \((X\otimes_BM)\otimes_BC\), and since \(C\) is flat over \(B\),
\[
\begin{aligned}&H^i(E\otimes^{\mathbf L}_BM)\otimes_BC\\&\quad=H^i\bigl((E\otimes^{\mathbf L}_BC)\otimes^{\mathbf L}_C(C\otimes_BM)\bigr),\end{aligned}
\]
which vanishes for \(i\notin[a,b]\). By faithful flatness, so does \(H^i(E\otimes^{\mathbf L}_BM)\).

(4) is part of [Tag 08G2]: tensoring the triangle with \(F\) gives a distinguished triangle and a long exact cohomology sequence. \(\square\)

## 2. Weak complete intersections

**Definition 2.1.** A homomorphism of rings \(A\to B\) of \(T\), or the \(A\)-algebra \(B\), is a *weak complete intersection* if \(L_{B/A}\) has tor amplitude in \([-1,0]\). A morphism of ringed topoi \(f\colon(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) is a weak complete intersection if \(\mathcal O_X\) is one over \(f^{-1}\mathcal O_Y\); a morphism of schemes is one if the morphism of their Zariski ringed topoi is.

Since \(H^i(L_{B/A})=0\) for \(i>0\), by Lemma 1.1 (1) it suffices that \(L_{B/A}\) have tor amplitude in \([-1,b]\) for some \(b\geq0\).

**Proposition 2.2.**

1. If the map \(L_{B/A}\to\Omega_{B/A}[0]\) to \(H^0\) is a quasi-isomorphism and \(\Omega_{B/A}\) is flat, then \(B\) is a weak complete intersection over \(A\). This holds for a polynomial algebra over a ring, and for its constant sheaf over the constant ring in any topos.
2. If \(I\) is a weakly regular ideal of \(A\), then \(A/I\) is a weak complete intersection over \(A\), and \(L_{(A/I)/A}\cong(I/I^2)[1]\). This holds in particular for Koszul-regular ideals.
3. A local complete intersection homomorphism of rings [Tag 07D0], and a local complete intersection morphism of schemes [Tag 069F], is a weak complete intersection.

**Proof.** (1) A flat module in degree \(0\) has tor amplitude in \([0,0]\). For a polynomial algebra \(A[x_s]_{s\in S}\) over a ring, \(L\cong\Omega\) is free (Theorem 2.2 of *The cotangent complex*), and the constant sheaves in a topos are the inverse image along the morphism to the punctual topos, which carries this description along [Tag 08SV].

(2) By Theorem 4.2 of the lesson on the fundamental spectral sequence, \(I/I^2\) is flat and \(L_{(A/I)/A}\cong(I/I^2)[1]\), which has tor amplitude in \([-1,-1]\). Koszul-regular ideals are weakly regular (Proposition 4.2 of the lesson on weakly regular ideals).

(3) For rings, \(L_{B/A}\) is perfect with tor amplitude in \([-1,0]\) [Tag 08SL]. For a local complete intersection morphism of schemes \(f\colon X\to Y\), every point of \(X\) has an affine open neighbourhood \(U=\operatorname{Spec}B\) mapping into an affine open \(V=\operatorname{Spec}A\); the condition of [Tag 069F] is imposed point by point, so \(U\to V\) is a local complete intersection morphism, and \(A\to B\) is a local complete intersection homomorphism [Tag 07DB]. On \(U\), \(L_{X/Y}\) is the complex of quasi-coherent modules associated with \(L_{B/A}\) (Proposition 10.1 of *The cotangent complex*). Representing \(L_{B/A}\) by a complex of flat \(B\)-modules in degrees \([-1,0]\) [Tag 08G1] gives a complex of flat \(\mathcal O_U\)-modules in these degrees. Tor amplitude is a local property, since the vanishing of the sheaves \(H^i(E\otimes^{\mathbf L}F)\) is local. \(\square\)

## 3. Composition, cancellation and descent

**Proposition 3.1.** Let \(A\to B\to C\) be homomorphisms of rings of \(T\).

1. If \(B\) is a weak complete intersection over \(A\) and \(C\) is one over \(B\), then \(C\) is one over \(A\).
2. If \(C\) is a weak complete intersection over \(A\), the map \(L_{B/A}\to\Omega_{B/A}[0]\) is a quasi-isomorphism and \(\Omega_{B/A}\) is flat, then \(C\) is a weak complete intersection over \(B\).
3. If \(C\) is a weak complete intersection over \(A\) and over \(B\), then \(L_{B/A}\otimes^{\mathbf L}_BC\) has tor amplitude in \([-1,0]\). If moreover \(C\) is faithfully flat over \(B\), then \(B\) is a weak complete intersection over \(A\).

**Proof.** Write \(X=L_{B/A}\otimes^{\mathbf L}_BC\), \(Y=L_{C/A}\) and \(Z=L_{C/B}\), so that \(X\to Y\to Z\to X[1]\) is the transitivity triangle. Rotating it gives the distinguished triangles \(Y\to Z\to X[1]\to Y[1]\) and \(Z[-1]\to X\to Y\to Z\).

(1) \(X\) has tor amplitude in \([-1,0]\) by Lemma 1.1 (2), and so has \(Z\); by Lemma 1.1 (4), so has \(Y\).

(2) Here \(X\cong\Omega_{B/A}\otimes_BC\), a flat \(C\)-module in degree \(0\), so \(X[1]\) has tor amplitude in \([-1,-1]\). In the triangle \(Y\to Z\to X[1]\to Y[1]\), \(Y\) and \(X[1]\) have tor amplitude in \([-1,0]\), so \(Z\) has (Lemma 1.1 (4)).

(3) In the triangle \(Z[-1]\to X\to Y\to Z\), \(Z[-1]\) has tor amplitude in \([0,1]\) and \(Y\) in \([-1,0]\), so \(X\) has tor amplitude in \([-1,1]\) (Lemma 1.1 (4)). As \(L_{B/A}\) is a complex of flat modules in degrees \(\leq0\), \(H^i(X)=0\) for \(i>0\), and Lemma 1.1 (1) gives tor amplitude in \([-1,0]\). If \(C\) is faithfully flat over \(B\), Lemma 1.1 (3) applies to \(E=L_{B/A}\). \(\square\)

## 4. Quotients of algebras with flat differentials

**Lemma 4.1.** Let \(A\to P\to B\) be homomorphisms of rings of \(T\), with \(P\to B\) surjective with kernel \(I\). Let
\[
c\colon I/I^2\to\Omega_{P/A}\otimes_PB
\]
be \(\partial_L^{-1}\colon I/I^2\to H^{-1}(L_{B/P})\), followed by \(H^{-1}\) of the map \(K\) of the transitivity triangle of \(A\to P\to B\) and the identification \(H^0(L_{P/A}\otimes^{\mathbf L}_PB)=\Omega_{P/A}\otimes_PB\). There is a sign \(\lambda\in\{1,-1\}\), the same for all such triples in all topoi, such that \(c(\bar f)=\lambda\,df\otimes1\) for every local section \(f\) of \(I\).

**Proof.** The identification holds because \(L_{P/A}\) is a complex of flat modules in degrees \(\leq0\) with \(H^0=\Omega_{P/A}\), and \(\otimes_PB\) is right exact. All the maps involved are natural in the triple.

Consider first the triple \(\mathbb Z\to\mathbb Z[t]\to\mathbb Z\), \(t\mapsto0\), of the punctual topos. There \(L_{\mathbb Z/\mathbb Z}=0\) and \(L_{\mathbb Z[t]/\mathbb Z}\cong\mathbb Z[t]\,dt\) (Theorem 2.2 of *The cotangent complex*), so the transitivity triangle shows that \(K\) is an isomorphism \(L_{\mathbb Z/\mathbb Z[t]}\to\mathbb Z\,dt[1]\), and \(c\) is an isomorphism \(\mathbb Z\,\bar t\to\mathbb Z\,dt\). Hence \(c(\bar t)=\lambda\,dt\) with \(\lambda\in\{1,-1\}\). In a topos \(T\), the constant triple \(\mathbb Z_T\to\mathbb Z_T[t]\to\mathbb Z_T\) is the inverse image of this one along \(T\to\mathrm{pt}\), which carries the transitivity triangle, \(\partial_L\) and \(c\) along [Tag 08SV]; so \(c(\bar t)=\lambda\,dt\) there.

Now let \(f\) be a section of \(I\) over an object \(U\) of \(T\). The homomorphism \(\mathbb Z_U[t]\to P_U\), \(t\mapsto f\), and the structure maps form a map of triples from \(\mathbb Z_U\to\mathbb Z_U[t]\to\mathbb Z_U\) to \(A_U\to P_U\to B_U\), since \(f\) maps to \(0\) in \(B\). It maps \(\bar t\) to \(\bar f\) and \(dt\otimes1\) to \(df\otimes1\). By naturality, \(c(\bar f)=\lambda\,df\otimes1\). \(\square\)

**Theorem 4.2.** Let \(A\to P\to B\) be homomorphisms of rings of \(T\), with \(P\to B\) surjective with kernel \(I\), such that \(L_{P/A}\to\Omega_{P/A}[0]\) is a quasi-isomorphism and \(\Omega_{P/A}\) is flat. Then \(B\) is a weak complete intersection over \(A\) if and only if \(I\) is weakly regular. In that case \(L_{B/A}\) is isomorphic in \(D(B)\) to the complex
\[
I/I^2\xrightarrow{\ d\ }\Omega_{P/A}\otimes_PB,\qquad\bar f\mapsto df\otimes1,
\]
in degrees \(-1\) and \(0\).

**Proof.** In the transitivity triangle \(X\to Y\to Z\xrightarrow{K}X[1]\) of \(A\to P\to B\), \(X=L_{P/A}\otimes^{\mathbf L}_PB\cong\Omega_{P/A}\otimes_PB\), a flat \(B\)-module in degree \(0\), \(Y=L_{B/A}\) and \(Z=L_{B/P}\).

If \(I\) is weakly regular, \(Z\cong(I/I^2)[1]\) with \(I/I^2\) flat (Theorem 4.2 of the lesson on the fundamental spectral sequence), and \(Y\) has tor amplitude in \([-1,0]\) by Lemma 1.1 (4).

Conversely, let \(B\) be a weak complete intersection over \(A\). By Proposition 3.1 (2), applied to \(A\to P\to B\), \(B\) is a weak complete intersection over \(P\): \(Z\) is represented by a complex \(F^{-1}\to F^0\) of flat modules [Tag 08G1]. Here \(H^0(Z)=\Omega_{B/P}=0\), because \(P\to B\) is surjective, so \(F^{-1}\to F^0\) is surjective and its kernel \(H^{-1}(Z)\cong I/I^2\) is flat, and \(H^i(Z)=0\) for \(i\neq-1\). By Theorem 4.2 of the lesson on the fundamental spectral sequence, \(I\) is weakly regular.

For the two-term model, let \(I\) be weakly regular. Under \(Z\cong(I/I^2)[1]\), given by \(\partial_L\) on \(H^{-1}\), and \(X\cong\Omega_{P/A}\otimes_PB\), the map \(K\) is a morphism \((I/I^2)[1]\to(\Omega_{P/A}\otimes_PB)[1]\) between modules placed in degree \(-1\); such a morphism is the shift of the module map it induces on \(H^{-1}\), which is \(c=\lambda d\) by Lemma 4.1. Rotating the triangle gives the distinguished triangle
\[
\begin{aligned}&I/I^2\xrightarrow{\ -\lambda d\ }\Omega_{P/A}\otimes_PB\\&\quad\to L_{B/A}\to(I/I^2)[1],\end{aligned}
\]
so \(L_{B/A}\) is isomorphic to the cone of \(-\lambda d\), the complex \(I/I^2\xrightarrow{-\lambda d}\Omega_{P/A}\otimes_PB\) in degrees \(-1\) and \(0\). Multiplication by \(-\lambda\) on \(I/I^2\) is an isomorphism of complexes from it to \(I/I^2\xrightarrow{d}\Omega_{P/A}\otimes_PB\). \(\square\)

The value of \(\lambda\) depends on the sign conventions for the transitivity triangle and for \(\partial_L\); the statement of Theorem 4.2 does not.

## 5. Tor-independent base change

**Proposition 5.1.** Let \(T\) be a topos with enough points, \(A\to B\) and \(A\to A'\) homomorphisms of rings of \(T\), and \(B'=B\otimes_AA'\). Suppose \(\operatorname{Tor}^A_i(B,A')=0\) for \(i>0\). Then the functoriality map \(L_{B/A}\otimes^{\mathbf L}_BB'\to L_{B'/A'}\) is an isomorphism. If \(B\) is a weak complete intersection over \(A\), then \(B'\) is one over \(A'\).

**Proof.** Let \(p\) be a point of \(T\). Taking stalks at \(p\) is exact and commutes with tensor products, and it carries flat modules to flat modules; so \(B'_p=B_p\otimes_{A_p}A'_p\) and \(\operatorname{Tor}^{A_p}_i(B_p,A'_p)=\operatorname{Tor}^A_i(B,A')_p=0\) for \(i>0\). By [Tag 08T0], \((L_{B/A})_p=L_{B_p/A_p}\), compatibly with the functoriality maps, so the stalk of our map at \(p\) is the functoriality map \(L_{B_p/A_p}\otimes^{\mathbf L}_{B_p}B'_p\to L_{B'_p/A'_p}\), which is an isomorphism by Proposition 3.1 of *The cotangent complex*. As \(T\) has enough points, the map is an isomorphism. The last assertion follows from Lemma 1.1 (2). \(\square\)

**Corollary 5.2.** Let
\[
\begin{array}{ccc}
X_1&\xrightarrow{\ a\ }&X\\
{\scriptstyle f_1}\downarrow&&\downarrow{\scriptstyle f}\\
Y_1&\longrightarrow&Y
\end{array}
\]
be a cartesian square of schemes such that \(X\) and \(Y_1\) are Tor independent over \(Y\). If \(f\) is a weak complete intersection, so is \(f_1\).

**Proof.** By Proposition 1.4 of the lesson on deformations of diagrams of schemes, \(L_{X_1/Y_1}\cong La^*L_{X/Y}\), and \(La^*\) preserves tor amplitude, by the argument of Lemma 1.1 (2) applied to a flat representative. \(\square\)

## 6. Exercises

**Exercise 6.1.** Let \(k\) be a field, \(A=k[t]/(t^2)\) and \(B=k\). Using Exercise 5.1 of the lesson on the fundamental spectral sequence, show that \(B\) is not a weak complete intersection over \(A\), although \(A\) is a weak complete intersection over \(k[t]\) and \(k\) is one over \(k[t]\).

**Exercise 6.2.** Let \(A\to B\) be a weak complete intersection and \(C=B[t]\). Show that \(C\) is a weak complete intersection over \(A\).

**Exercise 6.3.** Let \(k\) be a field, \(P=k[x,y]\), \(I=(xy)\) and \(B=P/I\). Using Theorem 4.2, describe \(L_{B/k}\), and show that \(H^{-1}(L_{B/k})=0\) and \(H^0(L_{B/k})=\) \((B\,dx\oplus B\,dy)/B(y\,dx+x\,dy)\).

## 7. Complete solutions

**Solution 6.1.** By Exercise 5.1 of the lesson on the fundamental spectral sequence, \(H^{-2}(L_{k/A})=H_2(L_{k/A})\cong k\neq0\). A complex of tor amplitude in \([-1,0]\) has no cohomology outside \([-1,0]\) (take \(F=B\) in the definition), so \(k\) is not a weak complete intersection over \(A\). The ideals \((t^2)\) and \((t)\) of \(k[t]\) are generated by nonzerodivisors, hence Koszul-regular, so \(A\) and \(k\) are weak complete intersections over \(k[t]\) (Proposition 2.2 (2)). This does not contradict Proposition 3.1 (2) for \(k[t]\to A\to k\): there the cotangent complex of the middle algebra must be a flat module in degree \(0\), while \(L_{A/k[t]}\cong(t^2)/(t^4)[1]\cong A[1]\).

**Solution 6.2.** \(C\) is a polynomial algebra over \(B\), so \(L_{C/B}\cong\Omega_{C/B}=C\,dt\) (Theorem 2.2 of *The cotangent complex*, and Proposition 2.2 (1)), and \(C\) is a weak complete intersection over \(B\). Proposition 3.1 (1) applies.

**Solution 6.3.** \(L_{P/k}\cong\Omega_{P/k}=P\,dx\oplus P\,dy\) is free, and \(I\) is generated by the nonzerodivisor \(xy\), so it is Koszul-regular, hence weakly regular, with \(I/I^2\) free on the class of \(xy\). By Theorem 4.2, \(L_{B/k}\) is isomorphic to \(B\to B\,dx\oplus B\,dy\), \(1\mapsto d(xy)=y\,dx+x\,dy\), in degrees \(-1\) and \(0\). If \(b(y\,dx+x\,dy)=0\) in \(B\,dx\oplus B\,dy\), then \(by=bx=0\) in \(B\). In \(B\), which has the \(k\)-basis \(1\), \(x^i\), \(y^j\) (\(i,j\geq1\)), the annihilator of \(y\) is \(xB\) and that of \(x\) is \(yB\), and \(xB\cap yB=0\); so \(b=0\), \(H^{-1}(L_{B/k})=0\), and \(H^0(L_{B/k})\) is the stated cokernel, which is \(\Omega_{B/k}\).

## Sources

Weak complete intersections, their stability properties and the criterion for quotients are due to Illusie, in his work on the cotangent complex. For noetherian rings and local complete intersections, the characterization of the cotangent complex of a quotient by a regular ideal is due to Quillen, in Section 10 of his MIT notes on the homology of commutative rings (1968), [available from Haynes Miller's page](https://math.mit.edu/~hrm/manuscripts/quillen-commutative-algebra.pdf).

# Flatness criteria, dimension and the flat locus

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent AI review of this edition is not complete. Public domain (CC0).*

Flatness is an exactness condition, but in a finite type family it can often be decided by a much smaller calculation. One can test a quotient by an ideal, compare a map with its fibres, or use regular sequences and dimension. We will develop these tests before studying where they hold. The examples distinguish a singular fibre from failure of flatness and show exactly why a regular base and a Cohen–Macaulay source occur in miracle flatness.

The preceding lesson, **Flat morphisms**, supplies generization lifting and generic freeness. From commutative algebra we assume **Tor and flat modules**, **Faithful flatness and the local criterion for flatness**, **Krull dimension and Noether normalization**, **Dimension theory of Noetherian local rings**, **Regular sequences, depth and Cohen–Macaulay modules**, and **Regular local rings**. We use the residue-field local criterion: for a local map \(A\to B\) of Noetherian local rings and a finite \(B\)-module \(M\), vanishing of \(\operatorname{Tor}_1^A(A/\mathfrak m_A,M)\) implies \(A\)-flatness. References for that prerequisite and the dimension and regular-sequence facts appear below. Basic references are the Stacks Project and Vakil's *The Rising Sea*.

## 1. Testing a quotient by an ideal

**Lemma 1.1 (passing from a quotient to its modules).** Suppose \(I\subset A\), \(M/IM\) is flat over \(A/I\), and \(\operatorname{Tor}_1^A(A/I,M)=0\). Then \(\operatorname{Tor}_1^A(N,M)=0\) for every \(A/I\)-module \(N\).

**Proof.** Choose a surjection \(F\twoheadrightarrow N\) from a free \(A\)-module and write \(K\) for its kernel. Since \(IN=0\), we have \(IF\subset K\). The quotient \(K/IF\) embeds in \(F/IF\). Tensoring that injection with the flat \(A/I\)-module \(M/IM\) stays injective.

Let \(z\in K\otimes_A M\) map to zero in \(F\otimes_A M\). Its image in \((K/IF)\otimes_{A/I}(M/IM)\) is zero by this injection. Right exactness of tensor products then says \(z\) comes from some \(w\in IF\otimes_A M\). The map \(IF\otimes_A M\to F\otimes_A M\) is injective: \(F\) is free, and the corresponding injection for \(I\otimes_A M\to M\) is precisely the assumed Tor vanishing. Thus \(w=0\) and \(z=0\). The kernel of \(K\otimes_A M\to F\otimes_A M\) computes \(\operatorname{Tor}_1^A(N,M)\), proving the assertion. ∎

**Theorem 1.2 (ideal local criterion).** Let \(A\to B\) be a local homomorphism of Noetherian local rings, \(M\) a finite \(B\)-module, and \(I\subset\mathfrak m_A\). Then \(M\) is flat over \(A\) if and only if

\[
M/IM\text{ is flat over }A/I,
\qquad \operatorname{Tor}_1^A(A/I,M)=0.
\]

**Proof.** Flatness gives the Tor vanishing and preserves flatness after base change. Conversely apply Lemma 1.1 to \(N=A/\mathfrak m_A\). The residue-field local criterion gives flatness. All its hypotheses hold here: the map is local, both local rings are Noetherian, and \(M\) is finite over \(B\). ∎

If \(I=(a)\), with \(a\) a non-zero-divisor in \(A\), the Tor condition says exactly that \(a\) is a non-zero-divisor on \(M\). This follows by tensoring the free resolution \(0\to A\xrightarrow{a}A\to A/(a)\to0\). Thus slicing by one parameter can turn a flatness problem into a lower-dimensional one.

## 2. Comparing a morphism with its fibres

**Theorem 2.1 (Noetherian fibre criterion).** Let \(R\to S\to T\) be local maps of Noetherian local rings. Write \(\mathfrak m\) for the maximal ideal of \(R\). Let \(M\ne0\) be a finite \(T\)-module. Then the following conditions are equivalent:

- \(M\) is flat over \(R\), and \(M/\mathfrak mM\) is flat over \(S/\mathfrak mS\);
- \(S\) is flat over \(R\), and \(M\) is flat over \(S\).

**Proof.** The second condition gives the first by composition and base change. Suppose the first holds and put \(I=\mathfrak mS\). There is a surjection

\[
\mathfrak m\otimes_R M\longrightarrow I\otimes_S M.
\]

Its composite with \(I\otimes_S M\to M\) is injective, because \(M\) is \(R\)-flat. Both arrows are consequently injective, and the first is an isomorphism. Therefore \(\operatorname{Tor}_1^S(S/I,M)=0\). Theorem 1.2, applied to \(S\to T\), makes \(M\) flat over \(S\).

It is faithfully flat over \(S\). Indeed Nakayama's lemma gives \(M/\mathfrak m_TM\ne0\), and \(\mathfrak m_SM\subset\mathfrak m_TM\), so \(M/\mathfrak m_SM\ne0\). For a flat module over a local ring, nonzero reduction modulo the maximal ideal is the faithful-flatness test.

Tensor the exact sequence

\[
0\longrightarrow\operatorname{Tor}_1^R(R/\mathfrak m,S)
\longrightarrow\mathfrak m\otimes_R S\longrightarrow I\longrightarrow0
\]

with the \(S\)-flat module \(M\). The middle-to-right map becomes the isomorphism already obtained, so the Tor module tensored with \(M\) vanishes. Faithful flatness kills the Tor module itself. The residue-field criterion for \(R\to S\), with the finite \(S\)-module \(S\), now makes \(S\) flat over \(R\). ∎

**Corollary 2.2 (scheme form).** Let \(X\xrightarrow fY\to Z\) be maps of locally Noetherian schemes, and \(\mathcal F\) a coherent sheaf on \(X\). At a point \(x\) with \(\mathcal F_x\ne0\), write \(y=f(x)\) and \(z\) for its image in \(Z\). Then \(\mathcal F\) is flat over \(Z\) at \(x\) and its fibre sheaf is flat over \(Y_z\) at \(x\) if and only if \(Y\) is flat over \(Z\) at \(y\) and \(\mathcal F\) is flat over \(Y\) at \(x\).

**Proof.** Apply Theorem 2.1 to the three local rings. The fibre module is \(\mathcal F_x/\mathfrak m_z\mathcal F_x\), and the local ring of \(Y_z\) at \(y\) is \(\mathcal O_{Y,y}/\mathfrak m_z\mathcal O_{Y,y}\). These are exactly the quotients in that theorem. ∎

In particular, if \(X\) is flat over \(Z\) and every \(X_z\to Y_z\) is flat, then \(f\) is flat. Flatness of \(Y\to Z\) need not be assumed separately: the theorem proves it at every point in the image of \(f\). If \(f\) is surjective it proves it everywhere. This is useful when a map of families is defined by coordinates and its fibre maps are easier to understand than its full local rings. References are [Stacks, Tags [00MP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-flatness-fibre-Noetherian), [039B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-criterion-flatness-fibre-Noetherian) and [039D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-morphism-between-flat-Noetherian)].

## 3. Dimension counts that flatness forces

We first use dimensions of local rings. These measure lengths of prime chains ending at the given point; they must not be confused with dimensions of irreducible components passing through a point.

**Theorem 3.1 (local dimension formula).** For a local homomorphism \(R\to S\) of Noetherian local rings satisfying going down, in particular for a flat local homomorphism,

\[
\dim S=\dim R+\dim(S/\mathfrak m_RS).
\]

**Proof.** Put \(r=\dim R\), \(d=\dim(S/\mathfrak m_RS)\). Choose a system of parameters \(a_1,\ldots,a_r\) in \(R\) and lift a system of parameters \(b_1,\ldots,b_d\) of the fibre ring to \(S\). The radical of \((a_1,\ldots,a_r)S\) equals that of \(\mathfrak m_RS\): a power of the finitely generated ideal \(\mathfrak m_R\) lies in the parameter ideal. Consequently \((a_1,\ldots,a_r,b_1,\ldots,b_d)S\) has radical \(\mathfrak m_S\). The height theorem gives \(\dim S\le r+d\).

For the reverse inequality choose a chain of length \(d\) in the fibre, represented by primes \(\mathfrak q_0\subsetneq\cdots\subsetneq\mathfrak q_d=\mathfrak m_S\). They all contract to \(\mathfrak m_R\). Choose a prime chain of length \(r\) in \(R\) ending at \(\mathfrak m_R\). Starting below \(\mathfrak q_0\), lift it successively by going down. Its successive primes have different contractions and hence give \(r\) strict additional inclusions. The combined chain has length \(r+d\). ∎

This proves [Stacks, Tag [00ON](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-base-fibre-equals-total)] after localizing at arbitrary primes. Without going down the upper bound still holds; the constructed lower chain is the part that can fail.

For example, in the blow-up chart \(x=u,y=uv\) at a closed point over the origin, \(\dim S=2\), \(\dim R=2\) and the fibre local ring has dimension one. The equation required by flatness would be \(2=3\), so the blow-up is not flat there. A large fibre is a decisive obstruction in this example. The next theorem shows when the matching dimension count becomes sufficient.

For a scheme, write \(\dim_xX\) for the infimum of the dimensions of its open neighbourhoods of \(x\). For a locally finite type scheme over a field this is the largest dimension of an irreducible component passing through \(x\). Thus at the generic point of \(\mathbb A^1_k\) it is one, whereas the local ring has dimension zero. In a fibre one has

\[
\dim_xX_y=\dim\mathcal O_{X_y,x}+\operatorname{trdeg}_{\kappa(y)}\kappa(x).
\]

This is the finite type dimension theorem over a field, a dimension-theory prerequisite [Stacks, Tag [02FX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-fibre-at-a-point)].

**Corollary 3.2 (geometric dimension).** If \(f:X\to Y\) is flat, locally of finite type between locally Noetherian schemes, and every nonempty fibre is equidimensional of dimension \(d\), then \(\dim_xX=\dim_{f(x)}Y+d\).

**Proof.** Shrink around the two points so that the dimensions of the neighbourhoods equal their dimensions at those points. Flatness and local finite presentation make \(f\) open; shrink the base to its open image, retaining surjectivity. At every point \(a\), Theorem 3.1 gives

\[
\dim\mathcal O_{X,a}=\dim\mathcal O_{Y,f(a)}+\dim\mathcal O_{X_{f(a)},a}\le\dim Y+d.
\]

Taking suprema gives \(\dim X\le\dim Y+d\). Conversely choose a point \(b\in Y\) with local-ring dimension as large as desired up to \(\dim Y\). Surjectivity gives a nonempty fibre. It has a closed point \(a\) in an affine open of an irreducible component of dimension \(d\). The field dimension theorem gives \(\dim\mathcal O_{X_b,a}=d\). The local formula at \(a\) gives the reverse inequality, after taking the supremum over \(b\). Shrinking the neighbourhoods did not change their dimensions at the designated points, so this proves the stated formula. ∎

In particular a flat morphism between integral finite type \(k\)-schemes has equidimensional fibres of dimension \(\dim X-\dim Y\). To check this at a point \(x\) over \(y\), use the finite type dimension identities

\[
\dim\mathcal O_{X,x}=\dim X-\operatorname{trdeg}_k\kappa(x),\qquad
\dim\mathcal O_{Y,y}=\dim Y-\operatorname{trdeg}_k\kappa(y),
\]

and add the transcendence degree \(\operatorname{trdeg}_{\kappa(y)}\kappa(x)\) to the local fibre dimension formula. Additivity of transcendence degree yields the asserted dimension at every fibre point. References are [Stacks, Tags [0AFE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-rel-dimension-dimension) and [02FX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-fibre-at-a-point)].

## 4. Why miracle flatness works

**Theorem 4.1 (miracle flatness).** Let \(R\to S\) be a local homomorphism of Noetherian local rings. If \(R\) is regular, \(S\) is Cohen–Macaulay and

\[
\dim S=\dim R+\dim(S/\mathfrak m_RS),
\]

then \(S\) is flat over \(R\).

**Proof.** Choose a regular system of parameters \(a_1,\ldots,a_r\) in \(R\), so \(r=\dim R\) and \(\mathfrak m_R=(a_1,\ldots,a_r)\). Lift a parameter system \(b_1,\ldots,b_d\) of \(S/\mathfrak m_RS\). Their combined list is a system of parameters of \(S\), by the radical argument in Theorem 3.1 and the assumed dimension equality. Every system of parameters of a Cohen–Macaulay local ring is a regular sequence. Thus the images of \(a_1,\ldots,a_r\) form an \(S\)-regular sequence.

The Koszul complex on these parameters resolves \(R/\mathfrak m_R\), since they form an \(R\)-regular sequence. Tensoring with \(S\) gives the Koszul complex on their images, which is exact in positive degrees. In particular \(\operatorname{Tor}_1^R(R/\mathfrak m_R,S)=0\). Apply the residue-field local criterion, with the finite \(S\)-module \(S\). ∎

The theorem is [Stacks, Tag [00R4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-CM-over-regular-flat)]. Its conditions have distinct roles. The regular base supplies a short free resolution of its residue field. Cohen–Macaulayness turns the source's parameter list into a regular sequence. The dimension equality ensures that the base parameters occupy precisely the expected part of that list.

Here are two finite maps that clarify these roles. First,

\[
k[x^2,y^2]\subset k[x,y]
\]

is free with basis \(1,x,y,xy\): divide each exponent by two, and uniqueness of monomials proves independence. This works in every characteristic. In contrast,

\[
C=k[x^2,xy,y^2]\subset k[x,y]
\]

is finite of generic rank two, but its fibre over the vertex of the cone has basis \(1,x,y\), of dimension three. For generic rank, put \(u=x^2,v=xy\). The fraction field of \(C\) is \(k(u,v)\), since \(y^2=v^2/u\). The element \(u\) is not a square in \(k(u,v)\), as its valuation along \(u=0\) is odd. Adjoining \(x\) therefore has degree two, including in characteristic two, and then \(y=v/x\). The vertex local ring of \(C\) has dimension two and embedding dimension three, so is not regular. Finite flatness would force a locally constant fibre dimension; it fails here. The source is regular, but the base is singular.

For failure of the source condition put

\[
R=k[s^4,t^4],\qquad S=k[s^4,s^3t,st^3,t^4].
\]

Write \(u=s^4,v=t^4,a=s^3t,b=st^3\). The identities

\[
ab=uv,\quad a^3=u^2b,\quad b^3=v^2a,\quad a^4=u^3v,\quad b^4=uv^3
\]

show that \(S\) is generated as an \(R\)-module by \(1,a,b,a^2,b^2\). These are distinct monomials. In the fibre modulo \((u,v)\) they remain independent: none of their exponent pairs \((0,0),(3,1),(1,3),(6,2),(2,6)\) is obtained by adding \((4,0)\) or \((0,4)\) to an exponent pair in the semigroup generated by \((4,0),(3,1),(1,3),(0,4)\). Thus the fibre has length five.

Generically \(a^2\) and \(b^2\) become proportional, because \(v a^2=u b^2\). The four monomials \(1,a,b,a^2\) have different exponent residues modulo \(4\) in each variable, so are linearly independent over \(k(u,v)\). They span the generic fibre, hence its rank is four. The extension is not flat at the origin. The base there is regular of dimension two; the source local ring has dimension two because the finite integral extension preserves dimension, and its fibre has dimension zero. Miracle flatness would make it flat if that source local ring were Cohen–Macaulay. It therefore is not Cohen–Macaulay. This establishes the obstruction without assuming a depth computation.

## 5. The flat locus over a Noetherian base

We will use a useful openness test for Noetherian spaces.

**Lemma 5.1 (Nagata's criterion).** Let \(U\) be a generization-stable subset of a Noetherian scheme. Suppose that for every \(q\in U\), the closure of \(q\) has a nonempty relatively open subset containing \(q\) and lying in \(U\). Then \(U\) is open.

**Proof.** Its complement \(F\) is stable under specialization. Consider an irreducible component \(C\) of \(\overline F\), with generic point \(q\). If \(q\in U\), the assumed open subset of \(C\) lying in \(U\), intersected with the complement of the other finitely many components of \(\overline F\), is a nonempty relatively open subset of \(\overline F\) disjoint from \(F\). This contradicts the density of \(F\) there. Thus every such \(q\) lies in \(F\). Specialization stability puts all of \(C\) in \(F\). There are finitely many components, so \(F=\overline F\) is closed. ∎

**Theorem 5.2 (Noetherian openness of flatness).** Let \(A\) be Noetherian, \(B\) a finite type \(A\)-algebra, and \(M\) a finite \(B\)-module. Then

\[
U=\{\mathfrak q\in\operatorname{Spec}B:M_{\mathfrak q}\text{ is flat over }A\}
\]

is open.

**Proof.** Localization makes \(U\) stable under generization. Fix \(\mathfrak q\in U\), and let \(\mathfrak p=\mathfrak q\cap A\). Generic freeness over the domain \(A/\mathfrak p\), proved in **Flat morphisms**, supplies \(a\notin\mathfrak p\) for which \((M/\mathfrak pM)_a\) is flat over \((A/\mathfrak p)_a\).

The \(B\)-module \(E=\operatorname{Tor}_1^A(A/\mathfrak p,M)\) is finite: take the first three terms of a resolution of the finite \(A\)-module \(A/\mathfrak p\) by finite free modules, tensor with \(M\), and use Noetherianity of \(B\). Flatness at \(\mathfrak q\) gives \(E_{\mathfrak q}=0\). Thus some \(g\notin\mathfrak q\) has \(E_g=0\).

Take \(\mathfrak q'\in V(\mathfrak q)\cap D(ag)\), contracting to \(\mathfrak p'\). Here \(\mathfrak p\subset\mathfrak p'\). In the local map \(A_{\mathfrak p'}\to B_{\mathfrak q'}\), use the ideal \(I=\mathfrak p A_{\mathfrak p'}\). The quotient of \(M_{\mathfrak q'}\) by this ideal is flat over \(A_{\mathfrak p'}/I\), by localization of the generic-freeness conclusion. Its Tor condition vanishes by \(E_g=0\). Theorem 1.2 therefore makes \(M_{\mathfrak q'}\) flat. We have found a relatively open neighbourhood of \(\mathfrak q\) in \(V(\mathfrak q)\) lying in \(U\). Lemma 5.1 proves openness. ∎

Notice that the ideal used at a specialization is \(\mathfrak p A_{\mathfrak p'}\), not the maximal ideal \(\mathfrak p'A_{\mathfrak p'}\). Keeping this ideal fixed is what makes the generic-freeness argument apply along the closure of \(\mathfrak q\).

By applying Theorem 5.2 on affine charts, for a locally finite type \(X\to Y\) with \(Y\) locally Noetherian and a coherent \(\mathcal F\), the set of points where \(\mathcal F\) is flat over \(Y\) is open [Stacks, Tag [0255](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-flat-open)]. Setting \(\mathcal F=\mathcal O_X\) gives the flat locus of the morphism itself.

For \(B=k[x,y]/(xy)\) over \(k[x]\), this locus is \(D(x)\). At every point above \(x=0\) the class of \(y\) remains nonzero on localization and is killed by \(x\); at every other point \(y=0\) and the map is an open part of the identity on the base. For \(B=k[x,y,z]/(xz,yz)\) over \(k[x,y]\), the flat locus is the complement of the inverse image of the origin: where \(x\) or \(y\) is invertible, \(z=0\) and the map is an isomorphism. At every prime above \((x,y)\), the class of \(z\) is nonzero and killed by the non-zero-divisor \(x\) of the base. To see that \(z\) stays nonzero, reduce to \(k[z]\): an element outside such a prime cannot have zero reduction there, while every annihilator of \(z\) lies in \((x,y)\).

Finally, the family \(y^2=x^3+t\) over \(k[t]\) is flat in every characteristic. Substituting \(t=y^2-x^3\) identifies its algebra with \(k[x,y]\); no nonzero polynomial in \(t\) becomes zero, so it is torsion free over the principal ideal domain \(k[t]\). Its fibre at zero is the cusp in every characteristic: the map \(x\mapsto u^2,y\mapsto u^3\) identifies its ring with \(k[u^2,u^3]\). Indeed the normal-form monomials \(x^i,x^iy\) have distinct exponents \(2i,2i+3\) after substitution, proving injectivity. This one-dimensional curve has a two-dimensional cotangent space at its origin and is singular there. A singular fibre is compatible with flatness.

## 6. Finite presentations over an arbitrary base

We now remove Noetherianity from the base. The finiteness assumptions change: the algebras and modules must have finite presentations. The argument keeps their finite lists of equations and passes through Noetherian rings containing their coefficients. We give the algebra behind this passage, rather than assuming that flatness automatically descends to an earlier ring.

**Lemma 6.1 (transporting a Tor obstruction).** Consider a commutative diagram of local maps of Noetherian local rings

\[
\begin{array}{ccc}
B&\longrightarrow&B'\\
\uparrow&&\uparrow\\
A&\longrightarrow&A'.
\end{array}
\]

Suppose \(B'\) is a localization of \(B\otimes_A A'\), \(M\) is finite over \(B\), and \(I\subsetneq A\). Put \(I'=IA'\) and \(M'=M\otimes_B B'\). If \(M/IM\) is flat over \(A/I\), and the natural map

\[
\operatorname{Tor}_1^A(A/I,M)\longrightarrow
\operatorname{Tor}_1^{A'}(A'/I',M')
\]

is zero, then \(M'\) is flat over \(A'\).

**Proof.** First work before the localization defining \(B'\). Choose a free \(A\)-module \(F\) surjecting onto \(M\), with kernel \(K\). Write

\[
H=\ker(K/IK\longrightarrow F/IF),\qquad
C=\operatorname{im}(K/IK\longrightarrow F/IF).
\]

The resolution identifies \(H\) with \(\operatorname{Tor}_1^A(A/I,M)\). In the exact sequence \(0\to C\to F/IF\to M/IM\to0\), the last module is flat. Thus \(C\to F/IF\) remains injective after tensoring with \(A'/I'\).

Let \(F'=F\otimes_A A'\), and let \(K'\) be the image of \(K\otimes_A A'\) in \(F'\). Right exactness gives a free presentation \(0\to K'\to F'\to M\otimes_A A'\to0\). There is a surjection

\[
(K/IK)\otimes_{A/I}A'/I'\longrightarrow K'/I'K'.
\]

An element of \(\ker(K'/I'K'\to F'/I'F')\) lifts to the left side. Its image in \(C\otimes_{A/I}A'/I'\) is zero, by the preceding injection. Tensoring \(H\to K/IK\to C\to0\) now shows that the lift comes from \(H\otimes_A A'\). Consequently the natural map from this last module onto the new Tor module is surjective. Localization preserves this conclusion. If the map from \(H\) is zero, its \(A'\)-linear extension is zero too, and the new Tor module vanishes.

The quotient \(M'/I'M'\) is flat over \(A'/I'\), by base change and localization of \(M/IM\). Apply Theorem 1.2 to \(A'\to B'\). The ideal \(I'\) is proper because the bottom map is local. This proves the lemma. ∎

This is the finite-obstruction argument underlying [Stacks, Tag [00MO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-another-variant-local-criterion-flatness)]. Localization of a \(B\)-module preserves its flatness over \(A\): it is a filtered colimit of copies of the module, with transition maps given by multiplication by elements of \(B\).

**Lemma 6.2 (flatness eventually holds in a finite model).** Let \(A\to B\) be a local map, with \(B\) essentially of finite presentation over \(A\), and let \(M\) be finitely presented over \(B\). They admit a filtered system of models \(A_\lambda\to B_\lambda,M_\lambda\) with the following properties:

- each \(A_\lambda\) and \(B_\lambda\) is a Noetherian local ring, essentially of finite type over \(\mathbb Z\);
- their colimits are \(A,B,M\);
- transition algebras are localizations of base changes, and transition modules are the corresponding base changes.

If \(M\) is flat over \(A\), then \(M_\lambda\) is flat over \(A_\lambda\) for some stage and every later stage.

**Proof.** Take finite type \(\mathbb Z\)-subalgebras of \(A\), localized at the contraction of its maximal ideal. Their directed union has colimit \(A\). Write \(B\) as a localization at a prime of an algebra with finitely many generators and relations. Put all coefficients into an initial subalgebra. At each larger stage use those same relations and localize at the inverse image of the chosen prime. The resulting local rings have colimit \(B\): every polynomial, coefficient and denominator occurs at some stage, and a denominator is inverted exactly when its image lies outside the chosen prime. A finite matrix presenting \(M\) has finitely many entries and denominators. Including them and taking its cokernel constructs the module models. These constructions establish all three properties.

Fix a stage \(\lambda\), and let \(\mathfrak m_\lambda\) be the maximal ideal of \(A_\lambda\). The module

\[
H_\lambda=\operatorname{Tor}_1^{A_\lambda}
(A_\lambda/\mathfrak m_\lambda,M_\lambda)
\]

is finite over \(B_\lambda\), by the same finite-resolution argument used in Theorem 5.2. Choose generators. In the colimit their images in \(\mathfrak m_\lambda A\otimes_A M\) lie in the kernel of multiplication to \(M\). That kernel is zero by flatness of \(M\). Formation of the extended ideal, tensor product and module colimit commutes with these filtered colimits. Each of the finitely many generator images therefore becomes zero in

\[
\mathfrak m_\lambda A_\mu\otimes_{A_\mu}M_\mu
\]

at one sufficiently large common stage \(\mu\). Equivalently the map from \(H_\lambda\) into \(\operatorname{Tor}_1^{A_\mu}(A_\mu/\mathfrak m_\lambda A_\mu,M_\mu)\) is zero. The quotient \(M_\lambda/\mathfrak m_\lambda M_\lambda\) is flat over the field \(A_\lambda/\mathfrak m_\lambda\). Apply Lemma 6.1 with \(I=\mathfrak m_\lambda\) to obtain flatness at stage \(\mu\). All subsequent base changes and localizations preserve it. ∎

The constructions correspond to [Stacks, Tags [00QX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-limit-module-essentially-finite-presentation), [00R1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-limit-module-finite-presentation) and [00R6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-colimit-eventually-flat)]. The final finite-obstruction step is essential: the equations presenting a module alone do not say when it is flat.

**Theorem 6.3 (general fibre criterion).** Let \(A\to B\to C\) be local maps, \(\mathfrak m\) the maximal ideal of \(A\), and \(M\ne0\) a finitely presented \(C\)-module. Suppose \(C\) is essentially of finite presentation over \(A\), and \(B\) is essentially of finite type over \(A\). Then

\[
\begin{split}
&M\text{ is }A\text{-flat and }M/\mathfrak mM
\text{ is }B/\mathfrak mB\text{-flat}\\
&\hspace{15mm}\Longleftrightarrow
B\text{ is }A\text{-flat and }M\text{ is }B\text{-flat}.
\end{split}
\]

When these conditions hold, \(B\) is in fact essentially of finite presentation over \(A\).

**Proof.** First suppose \(B\) also has an essential finite presentation. Model both algebras, their map and the matrix presenting \(M\) at the same stages over \(A_\lambda\), as in Lemma 6.2. This is possible using finitely many extra coefficients for the images of the algebra generators. In particular \(C_\lambda\) is essentially of finite presentation over \(B_\lambda\): present it by its generators over \(A_\lambda\), adding relations that equate the generators of \(B_\lambda\) with their images. Write \(\mathfrak m_\lambda\) for the maximal ideal of \(A_\lambda\).

By Lemma 6.2, flatness of \(M\) over \(A\) holds at all sufficiently large stages. Apply the same finite-obstruction proof to the system

\[
B_\lambda/\mathfrak m_\lambda B_\lambda\longrightarrow
C_\lambda/\mathfrak m_\lambda C_\lambda,
\qquad M_\lambda/\mathfrak m_\lambda M_\lambda.
\]

Each is a local Noetherian model, its transitions are localizations of base changes, and its colimit is the corresponding system modulo \(\mathfrak m\). Indeed \(\mathfrak m\) is the colimit of the \(\mathfrak m_\lambda\), and the residue fields have colimit \(A/\mathfrak m\). The assumed fibre flatness therefore also holds at sufficiently large stages. No \(M_\lambda\) at these stages is zero, since its base change to \(M\) is nonzero. Theorem 2.1 gives \(B_\lambda\) flat over \(A_\lambda\) and \(M_\lambda\) flat over \(B_\lambda\). Base change and localization give the desired two flatness statements.

For the stated finite type assumption write \(B=P/J\), where \(P=A[x_1,\ldots,x_n]_{\mathfrak q}\) and \(J\subset P\). The fibre ring \(P/\mathfrak mP\) is Noetherian. Choose a finitely generated subideal \(J_0\subset J\) whose images generate the image of \(J\) in that fibre. For every finitely generated \(J_1\) with \(J_0\subset J_1\subset J\),

\[
(P/J_1)/\mathfrak m(P/J_1)\cong B/\mathfrak mB.
\]

The case already proved applies to \(A\to P/J_1\to C\): the required presentations are finite, and the module and its fibre have the assumed flatness. Thus every \(P/J_1\) is flat over \(A\).

Consider \(P/J_0\twoheadrightarrow P/J_1\), with kernel \(K=J_1/J_0\). This kernel is a finite \(P\)-module. Tensor the exact sequence with \(A/\mathfrak m\). Flatness of its last term makes \(K/\mathfrak mK\) inject into the middle fibre, and the fibre map is an isomorphism. Hence \(K/\mathfrak mK=0\). Nakayama's lemma in the local ring \(P\) gives \(K=0\). Including any chosen element of \(J\) in \(J_1\) now proves \(J=J_0\). Therefore \(B\) is essentially of finite presentation and the first case finishes the proof. The reverse implication throughout follows from composition and base change of flatness. ∎

This proves the algebra of [Stacks, Tags [00R7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-flatness-fibre) and [05UV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-flatness-fibre-fp-over-ft)]. For schemes \(X\xrightarrow fY\to S\), suppose \(X\) is locally of finite presentation over \(S\), \(Y\) is locally of finite type over \(S\), and \(\mathcal F\) is quasi-coherent and locally of finite presentation on \(X\). At every \(x\in\operatorname{Supp}(\mathcal F)\), Theorem 6.3 applied to the stalks proves the equivalence in Corollary 2.2, with no Noetherian hypothesis [Stacks, Tag [039C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-criterion-flatness-fibre)]. Consequently if \(X\) is \(S\)-flat and all \(X_s\to Y_s\) are flat, then \(f\) is flat; surjectivity also gives flatness of \(Y\to S\) [Stacks, Tag [039E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-morphism-between-flat)].

**Theorem 6.4 (general openness).** Let \(A\to B\) be of finite presentation and \(M\) finitely presented over \(B\). Then \(\{\mathfrak q:M_{\mathfrak q}\text{ is flat over }A\}\) is open. Equivalently, if \(X\to S\) and \(\mathcal F\) are locally of finite presentation, with \(\mathcal F\) quasi-coherent, its flat locus over \(S\) is open in \(X\).

**Proof.** Choose \(\mathfrak q\) in the locus and put \(\mathfrak p=\mathfrak q\cap A\). Use the nonlocal finite models constructed in Lemma 6.2: the rings \(A_\lambda\) are finite type over \(\mathbb Z\), and \(B_\lambda,M_\lambda\) use fixed finite presentations. Their base changes to \(A\) are exactly \(B,M\). Localize each at the contractions \(\mathfrak p_\lambda,\mathfrak q_\lambda\). Lemma 6.2 gives a stage at which \((M_\lambda)_{\mathfrak q_\lambda}\) is flat over \((A_\lambda)_{\mathfrak p_\lambda}\), equivalently over \(A_\lambda\).

Theorem 5.2 gives \(g_\lambda\notin\mathfrak q_\lambda\) such that \((M_\lambda)_{g_\lambda}\) is flat over \(A_\lambda\). Here flatness at every prime of that localization gives flatness of the module by the affine criterion of **Flat morphisms**. Let \(g\) be its image in \(B\). Then \(g\notin\mathfrak q\), and \(M_g=(M_\lambda)_{g_\lambda}\otimes_{A_\lambda}A\) is flat. Thus \(D(g)\) is the required neighbourhood. Applying this on affine charts proves the scheme statement. ∎

These are [Stacks, Tags [00RC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-openness-flatness) and [0399](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-openness-flatness)]. The locus in the scheme form of Theorem 6.3 is open in \(\operatorname{Supp}(\mathcal F)\): it is the intersection of that support with the two open flat loci over \(Y\) and \(S\). The map \(X\to Y\) is locally of finite presentation here. Algebraically, an algebra finitely presented over \(A\) remains finitely presented over a finite type \(A\)-algebra mapping to it, by adding the finitely many generator-image relations used in Theorem 6.3.

**Corollary 6.5 (relative flat locus and base change).** Under the scheme hypotheses of Theorem 6.3, assume also that \(\mathcal F\) is flat over \(S\). Its flat locus over \(Y\) is open, and its formation commutes with every base change \(S'\to S\). In particular this holds for the flat locus of \(X\to Y\) when \(X\) is \(S\)-flat [Stacks, Tags [05VJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-base-change-criterion-flatness-fibre) and [05VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-base-change-flatness-fibres)].

**Proof.** Openness is Theorem 6.4. At a point where \(\mathcal F\) is nonzero, Theorem 6.3 identifies this locus with the flat locus of the fibre map; where it is zero both flatness conditions hold automatically. For \(s'\mapsto s\), the new fibre is obtained from the old one by the field extension \(\kappa(s)\subset\kappa(s')\). Flatness is preserved by that base change.

It is also reflected at any chosen point \(x'\) over \(x\). The local maps on both the fibre source and the fibre target are flat local maps, hence faithfully flat. If the new module is flat over the new target local ring, it is flat over the old target local ring by composition. For any injection of modules over the old target ring, the kernel after tensoring with the old sheaf stalk becomes zero after tensoring over the old source local ring with the new source local ring. Faithful flatness of this last ring map forces that kernel to be zero. The old stalk is therefore flat. This proves equality of the two loci at every point, and hence the base-change assertion. ∎

The relative hypothesis matters. Without it, base change can remove an obstruction: pulling the nonflat map \(V(xy)\to\mathbb A^1_x\) back to \(x=0\) gives a morphism to a field, which is flat everywhere.

## 7. Quasi-finite maps and exercises

**Corollary 7.1.** Let \(f:X\to Y\) be quasi-finite between locally Noetherian schemes. At \(x\mapsto y\), suppose \(\mathcal O_{X,x}\) is Cohen–Macaulay, \(\mathcal O_{Y,y}\) is regular, and their Krull dimensions are equal. Then \(f\) is flat at \(x\).

**Proof.** A quasi-finite fibre has local dimension zero. The equality in Theorem 4.1 is therefore exactly the assumed equality of the two local-ring dimensions. ∎

For smooth varieties with the same component dimension at corresponding points, quasi-finiteness gives that local-ring equality: the residue extension \(\kappa(y)\subset\kappa(x)\) is finite, so their transcendence degrees over the ground field agree; the dimension identities in Section 3 then give equal local dimensions. Smoothness makes the target local rings regular and the source local rings Cohen–Macaulay. Thus such a morphism is flat. Equality of dimensions of whole schemes alone would be insufficient if components of different dimensions were allowed.

1. **Easy — the exceptional fibre.** Use the local dimension formula to prove that the blow-up of \(\mathbb A^2_k\) at the origin is not flat. Identify the dimensions at a rational closed point of the exceptional divisor.

2. **Medium — two finite maps.** Prove that \(k[x,y]\) is free over \(k[x^2,y^2]\). Compute its generic rank and vertex fibre over \(k[x^2,xy,y^2]\), allowing characteristic two. Identify the failed miracle-flatness hypothesis.

3. **Medium — an ideal test.** Starting only from the residue-field local criterion, prove Theorem 1.2. Explain why one cannot omit the condition \(I\subset\mathfrak m_A\), and describe the Tor test when \(I=(a)\) for a non-zero-divisor \(a\in A\).

4. **Medium — quasi-finite smooth varieties.** Let \(X,Y\) be smooth varieties over \(k\), with equal component dimensions at all corresponding points. Prove that a quasi-finite \(f:X\to Y\) is flat. Explain the role of the residue fields in passing from geometric dimension to local-ring dimension.

5. **Hard — Macaulay's surface.** For \(S=k[s^4,s^3t,st^3,t^4]\) over \(R=k[s^4,t^4]\), prove finiteness, generic rank four and special fibre length five. Exhibit directly a nonzero element killed by \(t^4\) in \(S/s^4S\). Deduce that the local ring of \(S\) at the origin is not Cohen–Macaulay.

6. **Medium — locating the obstruction.** Compute the flat locus of \(\operatorname{Spec}k[x,y,z]/(xz,yz)\to\mathbb A^2_{x,y}\). What happens to the locus after base change to the origin, and why does this not contradict Corollary 6.5?

## Solutions

**1.** In the chart \(x=u,y=uv\), take \(u=v=0\). Its source local ring is \(k[u,v]_{(u,v)}\), of dimension two. The base local ring is \(k[x,y]_{(x,y)}\), also of dimension two. Its maximal ideal extends to \((u,uv)=(u)\), so the fibre local ring is \(k[v]_{(v)}\), of dimension one. Flatness would give \(2=2+1\) in Theorem 3.1, a contradiction. One nonflat point suffices to disprove flatness of the morphism. Other points of the exceptional divisor are covered by this chart or its symmetric chart.

**2.** Every monomial \(x^iy^j\) has a unique expression \((x^2)^a(y^2)^b x^\epsilon y^\delta\), with \(\epsilon,\delta\in\{0,1\}\). Distinct parity pairs have disjoint monomial supports. This proves a free basis \(1,x,y,xy\).

For the cone put \(u=x^2,v=xy,w=y^2\); its coordinate ring is \(k[u,v,w]/(uw-v^2)\). The fraction field is \(k(u,v)\), and the extension to \(k(x,y)\) adjoins a root of \(X^2-u\). The \(u\)-valuation proves that \(u\) is not a square, so this polynomial is irreducible in every characteristic. The generic rank is two. The vertex fibre is \(k[x,y]/(x^2,xy,y^2)\), with basis \(1,x,y\). A finite flat module over a local ring is free, so its fibre dimension equals its generic rank. The dimensions two and three contradict flatness at the vertex. There the cone has dimension two but a three-dimensional cotangent space \((u,v,w)/(u,v,w)^2\); it is not regular. The regular-base condition fails, while the source is regular and the fibre has dimension zero.

**3.** Present any \(A/I\)-module \(N\) by an \(A\)-free module \(F\), with kernel \(K\). The inclusion \(IF\subset K\) gives \(K/IF\subset F/IF\), whose tensor with the flat quotient \(M/IM\) remains injective. An element of \(K\otimes M\) killed in \(F\otimes M\) consequently lifts from \(IF\otimes M\). The assumed Tor vanishing makes \(IF\otimes M\to F\otimes M\) injective, forcing the element to be zero. Thus \(\operatorname{Tor}_1^A(N,M)=0\). Since \(I\subset\mathfrak m_A\), we may take \(N=A/\mathfrak m_A\), and the residue-field criterion gives flatness. The converse is base change and Tor vanishing for a flat module.

If \(I=A\), both quotient conditions are vacuous for every module. For instance \(A=B=k[t]_{(t)}\), \(M=A/(t)\) is not flat, although the quotient conditions for \(I=A\) hold. Every proper ideal of a local ring is contained in its maximal ideal, so properness is precisely the restriction needed here. For \(I=(a)\), tensoring \(0\to A\xrightarrow a A\to A/(a)\to0\) identifies the Tor group with the kernel of multiplication by \(a\) on \(M\).

**4.** Fix \(x\mapsto y\). Quasi-finiteness gives a zero-dimensional fibre and a finite residue-field extension. Put \(n=\dim_xX=\dim_yY\); smooth components meeting these points have dimension \(n\). The finite type dimension identities give

\[
\dim\mathcal O_{X,x}=n-\operatorname{trdeg}_k\kappa(x)
=n-\operatorname{trdeg}_k\kappa(y)=\dim\mathcal O_{Y,y}.
\]

Both local rings are regular, hence the source is Cohen–Macaulay. Corollary 7.1 applies. Without the finite residue extension, equal component dimensions would not by themselves supply the displayed equality at nonclosed points.

**5.** Use \(u=s^4,v=t^4,a=s^3t,b=st^3\). The relations in Section 4 reduce every product in \(a,b\) to an \(R\)-linear combination of \(1,a,b,a^2,b^2\), proving finiteness. Their exponent pairs are the five semigroup elements not obtainable from another semigroup element by adding \((4,0)\) or \((0,4)\); since monomials form a basis of a semigroup algebra, their classes are a basis modulo \((u,v)\). The special fibre therefore has length five. Generically \(b^2=(v/u)a^2\), and the exponent residues of \(1,a,b,a^2\) modulo four are distinct. Multiplying a hypothetical rational-coefficient relation by a common denominator would give a polynomial relation with disjoint monomial residue classes, which is impossible. The generic rank is four, in every characteristic. The finite module cannot be flat at the origin.

For the direct regular-sequence obstruction, \(a^2\notin uS\): its exponent minus \((4,0)\) is \((2,2)\), which is not in the generating semigroup. But \(v a^2=u b^2\), so its nonzero class modulo \(u\) is killed by \(v\). It remains nonzero at the origin: any multiplier outside the homogeneous maximal ideal has a nonzero constant term, whose product with \(a^2\) cannot be cancelled by terms of higher total degree or enter \(uS\). The ideal \((u,v)\) is primary to that maximal ideal, as its quotient has finite length. Thus \(u,v\) is a system of parameters of the two-dimensional local ring, and it is not a regular sequence. Every parameter system of a Cohen–Macaulay local ring is regular; this gives a second proof that the local ring is not Cohen–Macaulay.

**6.** If \(x\) or \(y\) is invertible, both relations force \(z=0\); the morphism is an isomorphism on that open part of the base and hence flat. For a prime \(\mathfrak q\) over \((x,y)\), the class of \(z\) has annihilator \((x,y)\) in \(k[x,y,z]/(xz,yz)\). To verify this, multiply a polynomial by \(z\) and reduce modulo \((x,y)\); the product in \(k[z]\) vanishes only if the polynomial's reduction is zero. Thus every annihilator lies in \(\mathfrak q\), and \(z\) stays nonzero at that prime. The non-zero-divisor \(x\) in \(k[x,y]_{(x,y)}\) kills it, contradicting flatness. The locus is exactly \(D(x)\cup D(y)\) in the source.

After base change to the origin the source is \(\operatorname{Spec}k[z]\), flat over \(k\) everywhere. The inverse image of the old flat locus is empty. Corollary 6.5 assumed that the original source was flat over the common base; with that base equal to \(\mathbb A^2\), this example fails its hypothesis.

## What this lesson does not prove

The assigned flatness criteria, dimension formulas, miracle flatness and openness statements are proved above, including their finite presentation versions. We import the following commutative algebra and dimension prerequisites with their exact scope:

- The residue-field local criterion for a local map of Noetherian local rings and a finite module over the target [Stacks, Tag [00MK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-local-criterion-flatness)].
- Nakayama's lemma for a finite module over a local ring; finite flat modules over local rings are free; a flat module over a local ring is faithfully flat exactly when its residue module is nonzero [Stacks, Tags [00DV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-NAK), [00NZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-flat-local) and [00HP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ff)].
- The height theorem for ideals generated by finitely many elements, existence of parameter systems in Noetherian local rings, regular systems of parameters in regular local rings, and the characterization of Cohen–Macaulay local rings by regular parameter systems. These are the content of **Dimension theory of Noetherian local rings**, **Regular sequences, depth and Cohen–Macaulay modules**, and **Regular local rings**.
- The Koszul complex of a regular sequence is exact in positive degrees, so for parameters generating a regular local ring's maximal ideal it resolves the residue field [Stacks, Tag [062F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-koszul-regular)].
- Dimension equals transcendence degree for integral finite type algebras over a field; its localized form gives the identities in Section 3 [Stacks, Tags [00P0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-prime-polynomial-ring) and [02FX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-fibre-at-a-point)].

No flattening stratification is asserted here. That construction belongs to the course on Hilbert polynomials and flattening.

These algebraic proof providers are written in the commutative-algebra course: Faithful flatness and the local criterion for flatness, Theorem 4.2, gives the local Noetherian finite-module Tor criterion; Krull dimension and Noether normalization and Dimension theory of Noetherian local rings give the dimension prerequisites; Regular sequences, depth and Cohen–Macaulay modules and Regular local rings give the parameter and Koszul facts. The hypotheses remain exactly those in the prerequisite list.

## References

- [The Stacks Project](https://stacks.math.columbia.edu/), *Commutative Algebra*: local criteria, dimension, miracle flatness, finite models and openness; the individual tags above locate the statements used. The linked text is **AI Integrated Stacks Project**, an edition with AI-proposed corrections and AI-written additions that have not been reviewed by the Stacks Project maintainers.
- The Stacks Project, *Morphisms of Schemes*, *More on Morphisms* and *Étale Morphisms*: dimension at a point, the fibre criterion and flat loci.
- R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, §§12.4, 24.5–24.6: fibre dimension, flatness and local criteria.

In **Unramified morphisms** we turn from exactness to the rigidity of infinitesimal maps. The distinction between local-ring dimension and fibre dimension, and the fibre tests proved here, will recur in the local structure of étale and smooth morphisms.

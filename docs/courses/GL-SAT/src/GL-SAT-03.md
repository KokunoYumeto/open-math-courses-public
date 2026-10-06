# Beauville–Laszlo gluing and the moduli interpretation

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

A lattice describes a bundle near a point together with an identification away from that point. Gluing turns this local description into a bundle on a curve. With two moving points, it also explains why two independent modifications merge into one modification when the points collide. This is the geometry on which fusion will operate.

We use Loop groups and the affine Grassmannian, finite projective modules, and the descent proved in Quotients and torsors. Gluing identifies the local modification functor with bundles trivialized away from a point. For a projective curve and semisimple group, we then prove that every bundle admits such a trivialization locally on the parameter base.

Throughout, \(k\) is algebraically closed, \(X\) is a smooth connected curve over \(k\), and \(G\) is a smooth affine algebraic group. Reductivity is needed for the later geometry, but not for the gluing arguments. Write \(X_R=X\times_k\operatorname{Spec}R\). A torsor is a right \(G\)-torsor, and every displayed quotient of group functors means the corresponding sheaf or stack quotient, as indicated.

## 1. The algebra of a puncture

First consider the square

\[
\begin{array}{ccc}
R[t]&\longrightarrow&R[[t]]\\
\downarrow&&\downarrow\\
R[t,t^{-1}]&\longrightarrow&R((t)).
\end{array}
\tag{1.1}
\]

Here \(R\) can be nonnoetherian. The map \(R[t]\to R[[t]]\) need not be flat, so ordinary faithfully flat descent alone does not prove the desired gluing theorem.

More generally, let \(A\to B\) be a ring map and \(f\in A\). Assume that multiplication by \(f\) is injective on both rings and that \(A/f^nA\to B/f^nB\) is an isomorphism for every \(n\geq1\). These hypotheses hold in (1.1), with \(A=R[t]\), \(B=R[[t]]\), and \(f=t\).

**Theorem 1.1 (Beauville–Laszlo gluing).** The functor

\[
M\longmapsto
\bigl(M_f,\ M\otimes_AB,\ \alpha_{\mathrm{can}}\bigr)
\]

is an equivalence from \(A\)-modules on which \(f\) acts injectively to triples \((M_U,M_D,\alpha)\), where \(M_U\) is an \(A_f\)-module, \(M_D\) is a \(B\)-module on which \(f\) acts injectively, and

\[
\alpha:M_U\otimes_{A_f}B_f\xrightarrow{\sim}(M_D)_f.
\]

Its inverse is the equalizer

\[
M=\{(u,d)\in M_U\oplus M_D:\alpha(u\otimes1)=d/1\}.
\tag{1.2}
\]

It restricts to an equivalence on finite projective modules. In particular, a pair of vector bundles glued over the puncture gives a vector bundle over \(A\).

The equivalence also restricts to flat modules. We prove all these assertions below. Free further reading is the [authors' article](https://math.univ-cotedazur.fr/~beauvill/pubs/descente.pdf) and [Stacks, the Beauville–Laszlo section](https://stacks.math.columbia.edu/tag/0BNI).

*Proof, beginning with the ring square.* The hypotheses give an exact sequence of \(A\)-modules

\[
0\longrightarrow A\longrightarrow A_f\oplus B
\longrightarrow B_f\longrightarrow0.
\tag{1.3}
\]

The last arrow is the difference of the two maps to \(B_f\). Indeed, given \(b/f^n\), choose \(a\in A\) with \(b-a=f^nc\) in \(B\). Then \(b/f^n\) is the image of \((a/f^n,-c)\). If \((a/f^n,b)\) lies in the kernel, injectivity of \(f\) on \(B\) implies \(a=f^nb\) there. The quotient isomorphism implies \(a=f^na_0\) in \(A\). Cancelling \(f^n\) in \(B\) gives \(b=a_0\), so the pair comes from \(a_0\). The first arrow is injective because \(A\to A_f\) is injective.

We spell out the tensor calculations needed when \(A\to B\) is not flat. Write \(T[f^n]=\{x:f^nx=0\}\) and call \(T\) an \(f\)-power-torsion module if \(T=\bigcup_nT[f^n]\). For such a module, the natural map

\[
T\longrightarrow T\otimes_AB
\tag{1.4}
\]

is an isomorphism. When \(f^nT=0\), this is the tensor identity
\(T\otimes_AB=T\otimes_{A/f^nA}(B/f^nB)=T\). The general case follows by taking the union of \(T[f^n]\); tensor products commute with these directed unions as colimits. If \(T\) already has a \(B\)-module structure, (1.4) respects it, since its action on each \(T[f^n]\) factors through \(B/f^nB=A/f^nA\).

Here and below \(\operatorname{Tor}_i^A(L,N)\) means the homology of a free resolution of one module tensored with the other. We use the following elementary properties, with their reasons. Either module can be resolved: tensor the two free resolutions together, form the total complex, and take homology in either order; in each fixed total degree there are only finitely many terms. A short exact sequence gives the long exact homology sequence, by lifting to free resolutions that are split in each degree. Directed colimits commute with these groups because tensor products commute with colimits and directed colimits of modules are exact. For the latter assertion, an element or an equation involves finitely many representatives, so it is witnessed in one common stage. Finally a module is flat exactly when all its \(\operatorname{Tor}_1\) groups vanish. Flatness makes its tensor of every free resolution exact. Conversely the long exact sequence for an arbitrary injection \(N'\to N\), with quotient \(N/N'\), shows that vanishing of \(\operatorname{Tor}_1(L,N/N')\) makes \(L\otimes N'\to L\otimes N\) injective. This is the definition of flatness. In particular all higher Tor groups with a flat module vanish as well.

There are two useful consequences.

**Tensor calculation.** For any \(f\)-power-torsion \(T\),

\[
\operatorname{Tor}_1^A(B,T)=0.
\tag{1.5}
\]

For \(T=A/f^nA\), use the free resolution \(0\to A\xrightarrow{f^n}A\to A/f^nA\to0\). Its tensor with \(B\) remains injective on the left, since \(f\) is a nonzerodivisor on \(B\). If \(f^nT=0\), take a surjection \(F\to T\) with \(F\) free over \(A/f^nA\), and write its kernel as \(K\). We have \(\operatorname{Tor}_1^A(B,F)=0\). Tensoring \(K\to F\to T\) with \(B\) gives the very same maps by (1.4), so the long exact sequence gives (1.5). The union of \(T[f^n]\) proves it for arbitrary \(f\)-power torsion.

**Flatness calculation.** Suppose \(D\) is a flat \(B\)-module. Then for every \(A\)-module \(N\),

\[
\operatorname{Tor}_i^A(D_f/D,N)=0\qquad(i\geq2).
\tag{1.6}
\]

Multiplication by \(f\) is injective on \(D\): tensor \(0\to B\xrightarrow{f}B\) with the flat module \(D\). Thus \(D_f/D\) is the directed colimit of \(D/f^nD\), with transition map multiplication by \(f\), by sending \(d\bmod f^nD\) to \(d/f^n+D\). Each \(D/f^nD\) is flat over \(B/f^nB=A/f^nA\). To check the Tor assertion for such a module \(T\), take a free resolution \(F_\bullet\) of \(N\). The complex \(T\otimes_AF_\bullet\) is
\(T\otimes_{A/f^nA}(F_\bullet/f^nF_\bullet)\). Flatness of \(T\) lets tensoring commute with its homology. The latter homology is \(\operatorname{Tor}_i^A(A/f^nA,N)\), which vanishes for \(i\geq2\) by the two-term resolution above. Taking the colimit proves (1.6).

*Construction from a triple.* Put \(U=M_U\), \(D=M_D\), and identify \(E=D_f\) with \(U\otimes_{A_f}B_f\) through \(\alpha\). Embed \(D\) in \(E\); this uses the stipulated injectivity of \(f\) on \(D\). Let \(Q=E/D\). The map \(U\to Q\) is surjective. To see this explicitly, write an element of \(E\) as \(\sum_i b_i\alpha(u_i\otimes1)\), with \(b_i\in B\): any powers of \(f\) in coefficient denominators can be absorbed into the \(u_i\), since \(U\) is an \(A_f\)-module. Choose a common \(n\) such that \(d_i=f^n\alpha(u_i\otimes1)\in D\). Write \(b_i=a_i+f^nc_i\), using \(A/f^nA=B/f^nB\). The element is then
\(\alpha((\sum_i a_i u_i)\otimes1)+\sum_i c_i d_i\). Its class in \(Q\) comes from \(\sum_i a_i u_i\).

Projection to \(U\) identifies the equalizer (1.2) with the kernel of this map. Consequently

\[
0\longrightarrow M\longrightarrow U\longrightarrow Q\longrightarrow0.
\tag{1.7}
\]

The module \(M\) has injective \(f\)-action, since it is a submodule of \(U\), where \(f\) is invertible. Every element of \(Q\) is killed by a power of \(f\). Localization is exact: an equation between finitely many fractions can be checked after multiplying by one common denominator. Localizing (1.7) therefore gives \(M_f=U\).

By (1.5), tensoring (1.7) with \(B\) preserves injectivity on the left. Its last module is \(Q\) by (1.4), and its middle module is \(E\) by \(\alpha\). The map \(E\to Q\) is the quotient map. Its kernel is \(D\), proving

\[
M\otimes_AB\xrightarrow{\sim}D.
\tag{1.8}
\]

This is the map induced by projection of agreeing pairs onto \(D\), so the two recovered identifications have exactly the prescribed overlap isomorphism.

*Recovery and morphisms.* For any \(A\)-module \(L\) with injective \(f\)-action, tensor (1.3) with \(L\). Right exactness gives exactness in the middle and on the right; the first map is injective because its component \(L\to L_f\) is injective. Thus

\[
0\to L\to L_f\oplus(L\otimes_AB)
\to L\otimes_AB_f\to0
\tag{1.9}
\]

is exact. Moreover \(L\otimes_AB\) has injective \(f\)-action. An element killed by a power of \(f\), paired with zero in \(L_f\), lies in the kernel in (1.9), so comes from an element of \(L\) that vanishes in \(L_f\), hence from zero. This proves that restriction lands in the asserted category and that the equalizer recovers \(L\). A compatible pair of module maps sends agreeing pairs to agreeing pairs. Equations (1.8)–(1.9) show that this operation and restriction are inverse on maps as well as on objects. This proves the equivalence.

*Flatness.* A flat \(A\)-module has injective \(f\)-action and flat base changes. Conversely, when \(U\) and \(D\) in a triple are flat over their respective rings, \(U\) is flat over \(A\) as well, since localization is flat and \(U\otimes_A(-)=U\otimes_{A_f}(-)_f\). Apply the long exact Tor sequence of (1.7). For every \(N\), its terms \(\operatorname{Tor}_2^A(Q,N)\) and \(\operatorname{Tor}_1^A(U,N)\) vanish, the former by (1.6). Thus \(\operatorname{Tor}_1^A(M,N)=0\). This proves flatness of \(M\).

*Finiteness.* The two base changes detect a zero module: if \(N_f=0\), then \(N\) is \(f\)-power torsion and \(N\otimes_AB=N\) by (1.4); if both vanish, \(N=0\). They also detect finite generation. If \(N_f\) and \(N\otimes_AB\) are finitely generated, express chosen generators as fractions and finite sums of simple tensors. The finitely many elements of \(N\) that occur generate a submodule \(N_0\) whose two base changes surject onto those of \(N\). Right exactness and zero detection give \(N/N_0=0\).

For a triple of finite projective modules, the constructed \(M\) is therefore flat and finitely generated. Choose \(0\to K\to A^r\to M\to0\). Flatness of \(M\) makes this remain exact after tensoring with \(B\) or \(A_f\). On either piece the quotient is finite projective, so its kernel is a direct summand of a finite free module and is finitely generated. Finite-generation detection applied to \(K\) now proves that \(M\) is finitely presented.

For clarity, a finitely presented flat module is finite projective for the following elementary reason. Over a local ring choose lifts of a basis of its residue-field quotient. They generate by Nakayama's lemma. The kernel of the resulting finite free surjection is finitely generated; flatness makes its residue-field map injective, and the chosen basis makes that map zero. Nakayama makes the kernel zero, so the module is free locally. Here Nakayama follows from the determinant trick: equations expressing a finite generating set in its multiples by the maximal ideal give a matrix \(I-H\) with unit determinant, forcing those generators to vanish. Finite presentation lets one clear the finitely many denominators in a local basis and its inverse, obtaining a finite open cover \(D(s_j)\) on which the module is free. On each such open there is a dual-basis identity. Clearing denominators gives
\(s_j^{m_j}\operatorname{id}_M=\sum_a p_{ja}\phi_{ja}\), with \(p_{ja}\in M\) and \(\phi_{ja}:M\to A\). This clearing is valid because Hom from a finitely presented module commutes with localization, as follows by taking the kernel of the two maps on Hom in a finite presentation. The ideal generated by the \(s_j^{m_j}\) is the unit ideal: a maximal ideal containing it would miss every open in the cover. A linear combination of these identities gives a global finite dual basis. The corresponding maps between \(M\) and a finite free module split the identity, proving finite projectivity. The converse follows by base change of a direct summand of a finite free module. This completes Theorem 1.1. ∎

Formula (1.2) is also a useful instruction for calculation: intersect the module on the open curve with the disc lattice, using the prescribed punctured-disc identification.

## 2. Gluing torsors

Theorem 1.1 is not confined to matrices. We first check the algebra assertions needed for a general affine group.

**Lemma 2.A (flat algebras).** A pair of flat algebras over \(A_f\) and \(B\), with an algebra isomorphism over \(B_f\), glues to a flat \(A\)-algebra. If both algebras have finite presentation, the glued algebra does too. Tensor products of flat glued modules are the gluing of their component tensor products.

*Proof.* Glue the underlying modules to \(C\). The componentwise product and unit preserve the equalizer (1.2), giving an algebra structure. The maps (1.8) are algebra maps and isomorphisms, since they send \(c\otimes b\) to \(b\) times the component of \(c\). Associativity and the unit identities hold on agreeing pairs. The module is flat by Theorem 1.1.

Suppose the two algebras are finitely presented. Choose their finite algebra generating sets and express them as fractions or finite sums of simple tensors of elements of \(C\). Choose every element of \(C\) appearing in these expressions, say \(c_1,\ldots,c_r\). The subalgebra \(C_0=A[c_1,\ldots,c_r]\) has base changes surjecting onto \(C_f\) and \(C\otimes_AB\). The \(A\)-module \(C/C_0\) therefore has zero base changes and is zero by the detection argument above. Thus \(C\) has finite type.

Take the surjection \(P=A[z_1,\ldots,z_r]\to C\) with kernel \(J\). Flatness of \(C\) implies that tensoring its kernel sequence with \(B\) is exact, so \(J\otimes_AB\) is the kernel of \(B[z_1,\ldots,z_r]\to C\otimes_AB\); the analogous assertion holds after localization. Both kernels are finitely generated ideals because their quotient algebras are finitely presented. This assertion holds for any finite polynomial surjection: from one finite presentation with generators \(y_j\), express these in the chosen \(z_i\), express the \(z_i\) in the \(y_j\), and add those finitely many identities to the presentation; elimination of the \(y_j\) gives finitely many relations in the \(z_i\).

Apply finite-generation detection to \(J\) as a \(P\)-module. The pair \(P\to B[z_1,\ldots,z_r]\), with the same \(f\), has injective \(f\)-action and the same quotient isomorphisms in every degree. Its second base change of \(J\) is \(J\otimes_AB\), now as a module over \(B[z_1,\ldots,z_r]\). Hence \(J\) is a finitely generated ideal of \(P\), and \(C\) is finitely presented.

Finally the tensor product of two flat \(A\)-modules is flat, because tensoring with it is the composite of two exact tensor functors. Its base changes are the component tensor products by the associativity of tensor products. Uniqueness in Theorem 1.1 identifies it with their glued module, compatibly with maps. ∎

We record the ordinary affine descent step needed to discuss torsors. It is independent of completion. If \(S\) is faithfully flat over \(T\), an affine \(S\)-scheme with a descent isomorphism satisfying the cocycle identity descends to an affine \(T\)-scheme. On coordinate algebras, take the equalizer \(D\) of the two descent maps from its \(S\)-algebra \(E\) to the overlap algebra over \(S\otimes_TS\). Here is a module proof of effectivity. Write the descent isomorphism as a map
\(\theta:E\otimes_TS\to S\otimes_TE\). Put
\(\rho(e)=\theta(e\otimes1)\) and
\(D=\{e:\rho(e)=1\otimes e\}\).
The cocycle and diagonal identities say, respectively,
\( (1\otimes\rho)\rho(e)=\sum_i s_i\otimes1\otimes e_i\) when \(\rho(e)=\sum_i s_i\otimes e_i\), and
\(\sum_i s_ie_i=e\). Tensoring the equalizer with the flat module \(S\) shows that \(\rho(e)\) belongs to \(S\otimes_TD\). Thus \(\rho\) is an inverse to the multiplication map \(S\otimes_TD\to E\): for \(d\in D\), \(\rho(sd)=s\otimes d\), and the diagonal identity gives the other composite. Multiplication and the unit in \(E\) preserve \(D\), so this is an algebra isomorphism. Faithful flatness lets identities and isomorphisms be checked after this base change: a kernel or cokernel with zero tensor is zero. Applying this to the functor of points gives the affine descended scheme and its uniqueness.

Flatness also descends here, since an injection of \(T\)-modules can be tested after tensoring with \(S\). Finite type descends by choosing the finitely many elements appearing in expressions for generators of \(S\otimes_TD\); the quotient by their \(T\)-subalgebra has zero tensor with \(S\). For a flat algebra, finite presentation descends by applying the same finite-generation argument to the kernel of a finite polynomial surjection, whose base change remains exact. Consequently a torsor under a flat affine group of finite presentation is affine, faithfully flat, and of finite presentation over its base: on a faithfully flat trivializing cover it is the group itself, and the preceding constructions descend it. The surjectivity assertion descends too, or follows because a zero fibre would remain zero on that cover.

**Proposition 2.1 (torsor gluing).** Suppose the ring square above is a square of \(k\)-algebras. Then \(G\)-torsors over \(A\) are equivalent to a \(G\)-torsor over \(A_f\), a \(G\)-torsor over \(B\), and an isomorphism of their restrictions over \(B_f\).

*Proof.* Put \(H=A\otimes_k k[G]\). This is the Hopf algebra of \(G_A\). It is free as an \(A\)-module, by choosing a \(k\)-basis of \(k[G]\), and finitely presented as an algebra because \(G\) is an affine algebraic group. Write the two torsors as \(\operatorname{Spec}C_U\) and \(\operatorname{Spec}C_D\), using the affine descent argument just given. Their coordinate algebras are faithfully flat and finitely presented over their respective bases. Lemma 2.A constructs a flat finitely presented \(A\)-algebra \(C\), with the prescribed algebra base changes.

The coactions \(C_U\to C_U\otimes_AH\) and \(C_D\to C_D\otimes_AH\) agree on the overlap. Lemma 2.A and the equivalence on module maps therefore glue them to \(\rho:C\to C\otimes_AH\). This is an algebra map: multiplicativity and preservation of the unit hold after both base changes, and (1.9) makes maps into the flat target detectable on those pieces. The coassociativity and counit identities follow in the same way. Thus \(\rho\) defines a right \(G\)-action on \(\operatorname{Spec}C\).

The torsor map

\[
\operatorname{Spec}C\times_A G
\longrightarrow
\operatorname{Spec}C\times_A\operatorname{Spec}C
\]

is an isomorphism. On coordinate rings it is \(C\otimes_AC\to C\otimes_AH\), \(c\otimes d\mapsto(c\otimes1)\rho(d)\). Both modules are flat and the map is an isomorphism on both pieces, where it is the given torsor identity. The inverses on those pieces agree and glue by Theorem 1.1; their two composites are the identity by (1.9).

The map \(\operatorname{Spec}C\to\operatorname{Spec}A\) is surjective. For a prime \(\mathfrak p\) not containing \(f\), its fibre is the corresponding nonempty fibre of \(\operatorname{Spec}C_U\). For a prime containing \(f\), the quotient isomorphism gives a prime \(\mathfrak q\) of \(B\) containing \(f\), with the same residue field. The fibre is then the nonempty fibre of \(\operatorname{Spec}C_D\) at \(\mathfrak q\). Flatness and these nonzero fibres imply faithful flatness directly: if \(N\ne0\), it contains a nonzero cyclic submodule \(A/I\); choose a maximal ideal containing the proper ideal \(I\). The nonzero fibre there implies \(C/IC\ne0\), and flatness injects \(C/IC\) into \(N\otimes_AC\). Hence that tensor cannot vanish. Since \(C\) is finitely presented, this is an fppf cover. Over this cover the torsor identity trivializes \(\operatorname{Spec}C\), using the tautological section. We have constructed a torsor.

Morphisms glue by the same equalizer construction. Restricting and gluing are inverse, because they already are inverse on coordinate algebras. This proves the equivalence of groupoids. ∎

The completion cases used on curves satisfy the exact hypotheses, without a flatness assumption. In fact if \(f\) is a nonzerodivisor on \(A\) and \(\widehat A=\varprojlim_m A/f^mA\), then \(f\) is a nonzerodivisor on \(\widehat A\) and \(\widehat A/f^n\widehat A=A/f^nA\). For injectivity, \(f b=0\) implies that the coordinate of \(b\) modulo \(f^{m+1}\) is in \(f^mA/f^{m+1}A\), by cancelling \(f\); its coordinate modulo \(f^m\) is zero for every \(m\). For the quotient assertion, projection onto \(A/f^nA\) is surjective. If a compatible sequence projects to zero there, its coordinate modulo \(f^{n+r}\) lies in \(f^nA/f^{n+r}A\). Cancellation of \(f^n\) gives a unique coordinate modulo \(f^r\); these coordinates form a compatible sequence whose product by \(f^n\) is the original one. This identifies the kernel with \(f^n\widehat A\).

Near a fixed point \(x\in X(k)\), choose a regular parameter \(t\) that is a regular function on a sufficiently small affine neighbourhood \(V\), where \(x\) is its only zero. For every \(n\), \(\mathcal O(V)/(t^n)=k[t]/(t^n)\): this quotient is supported at \(x\), so it equals its local quotient, and successive division by the parameter gives the unique coefficients \(a_0+\cdots+a_{n-1}t^{n-1}\). Tensoring with \(R\) preserves the parameter's injective multiplication, since \(R\) is a flat \(k\)-module, and gives \(\mathcal O(V_R)/(t^n)=R[t]/(t^n)\). Its completion is therefore \(R[[t]]\). Apply Proposition 2.1 there and Zariski gluing on the rest of \(X_R\). Zariski gluing here simply identifies the given schemes and actions on their open intersections; the cocycle identities make the identifications transitive and give a scheme covered by the original affine charts. Thus one may glue a torsor on \((X-x)_R\) to one on the formal disc using an isomorphism on the punctured disc.

For a moving section, its graph is a relative effective Cartier divisor, including over bases with nilpotents. Here is the local check. A smooth relative curve has, locally, an étale coordinate \(z\). If the section has coordinate \(a\in R\), its graph is the selected branch of \(z-a=0\). The selection is open near the section: in an étale polynomial presentation, factor \(p(w)-p(b)=(w-b)q(w)\) at the section's root \(b\); the derivative condition makes \(q(b)\) a unit, isolating that branch, and successive presentations give the same assertion. Multiplication by \(z-a\) is injective in \(R[z]\), by its leading coefficient one, and remains injective in an étale coordinate algebra because that algebra is flat over \(R[z]\). Thus the graph has a local nonzerodivisor equation. A sum of graphs has the product of their equations; a product of injective multiplication maps is injective even where graphs meet. Apply the completion calculation and Proposition 2.1 to these equations. This is the same gluing operation in moving families.

## 3. A point of the Grassmannian is a modification

Let \(D_R=\operatorname{Spec}R[[t]]\) and \(D_R^\times=\operatorname{Spec}R((t))\). Define the modification functor by pairs

\[
(\mathcal P_D,\beta_D),\qquad
\beta_D:\mathcal P_D|_{D_R^\times}\xrightarrow{\sim}
G\times D_R^\times,
\]

up to isomorphisms respecting \(\beta_D\).

**Theorem 3.1.** There are natural identifications

\[
\operatorname{Gr}_G
\simeq
\{\text{disc torsors with punctured-disc trivialization}\}
\simeq
\{\text{torsors on }X\text{ trivialized off }x\}.
\tag{3.1}
\]

These are identifications of étale sheaves, not merely of geometric point sets.

*Proof.* A disc torsor becomes trivial étale locally on \(\operatorname{Spec}R\), by the smooth lifting lemma in *Loop groups and the affine Grassmannian*. Choose a disc frame. Composing it with \(\beta_D\) gives \(g\in G(R((t)))\). Changing the frame multiplies \(g\) on the right by \(h\in G(R[[t]])\). Conversely \(g\) equips the trivial disc torsor with the required punctured trivialization. Descent of torsors and trivializations makes these constructions inverse after étale sheafification.

For the second identification, glue \(\mathcal P_D\) to the trivial torsor on \((X-x)_R\) using \(\beta_D\). Proposition 2.1 makes this effective and unique, including morphisms. Restriction to the disc is the inverse. The chosen off-point trivialization is retained; forgetting it would give a different moduli problem. ∎

For \(GL_n\), the convention in (3.1) sends \(g\) to the lattice \(gR[[t]]^n\) inside the fixed punctured vector space. On the curve it sends the same lattice to the vector bundle whose sections on the open neighbourhood are the intersection described by (1.2).

For \(G=\mathbb G_m\) and \(R=k\), the coset \(t^m\) gives

\[
\mathcal O_X(-mx)
\]

with its canonical trivialization off \(x\). Its degree is \(-m\). Thus the integer coweight and the degree have opposite signs under our lattice convention. The reduced points are indexed by all degrees. Families over dual numbers also have the infinitesimal modifications calculated in the preceding lesson; replacing the full functor by its discrete reduction would lose them.

## 4. Relative position and the Hecke stack

A local modification consists of two disc torsors \(\mathcal P_D,\mathcal Q_D\) and an isomorphism between them on \(D_R^\times\). Choose frames of both. The isomorphism becomes a loop matrix; changing the frames acts on its two sides. The local Hecke stack is therefore

\[
\mathcal H_{\mathrm{loc}}
=[L^+G\backslash LG/L^+G]
=[L^+G\backslash\operatorname{Gr}_G].
\tag{4.1}
\]

It retains automorphisms. Its geometric isomorphism classes are the double cosets of \(G(k((t)))\) by \(G(k[[t]])\).

**Proposition 4.1.** Relative positions of two framed-locally disc torsors, with punctured-disc isomorphism, are exactly the \(L^+G(k)\)-orbits on \(\operatorname{Gr}_G(k)\).

*Proof.* Trivialize both torsors; over algebraically closed \(k\) the disc trivialization exists. A change of the second frame changes only the right coset \(gL^+G\), and a change of the first frame changes that coset by the left \(L^+G\)-action. Thus the orbit is independent of frames. Every loop gives a modification, and two loops give isomorphic modifications precisely when related by these frame changes. ∎

The **global Hecke stack** \(\operatorname{Hecke}_x\) classifies

\[
(\mathcal P,\mathcal Q,\beta),\qquad
\beta:\mathcal Q|_{(X-x)_R}\xrightarrow{\sim}
\mathcal P|_{(X-x)_R}.
\]

Its source map remembers \(\mathcal P\); its target map remembers \(\mathcal Q\). These are global bundles, so this stack is generally larger than (4.1).

To state the relationship accurately, restriction to the disc gives

\[
\operatorname{Bun}_G(X)\longrightarrow B L^+G.
\]

The map from \(\mathcal H_{\mathrm{loc}}\) to \(B L^+G\) remembers its first disc torsor. Gluing proves the cartesian description

\[
\operatorname{Hecke}_x
\simeq
\operatorname{Bun}_G(X)
\times_{B L^+G}\mathcal H_{\mathrm{loc}}.
\tag{4.2}
\]

Indeed the right side specifies \(\mathcal P\), the replacement disc torsor, and the punctured-disc isomorphism. Glue that replacement to \(\mathcal P\) off \(x\); the result is precisely \(\mathcal Q\). Restricting a global triple gives the inverse construction, including automorphisms.

In particular, the source fibre over a bundle \(\mathcal P\) is the twist of \(\operatorname{Gr}_G\) by its disc-frame torsor. Choosing a frame identifies it with the ordinary Grassmannian. The relative-position strata are the corresponding twists of its orbits.

For \(GL_2\), consider

\[
\mathcal O_X^2\subset\mathcal M\subset\mathcal O_X(x)^2,
\qquad
\operatorname{length}_x(\mathcal M/\mathcal O_X^2)=1.
\]

The quotient \(\mathcal O_X(x)^2/\mathcal O_X^2\) is a two-dimensional vector space at \(x\). The choices of \(\mathcal M\) are its lines, a \(\mathbb P^1\). After fixing a parameter, a line \(\ell\subset k^2\) gives the local lattice \(O^2+t^{-1}\ell\). Its elementary divisors are \((0,-1)\), its degree is one, and the remaining quotient \(\mathcal O_X(x)^2/\mathcal M\) also has length one.

## 5. Forgetting the off-point trivialization

Let \(G_{\mathrm{out}}\) be the group functor

\[
G_{\mathrm{out}}(R)=G((X-x)_R).
\]

Changing the off-point trivialization in (3.1) gives its action on \(\operatorname{Gr}_G\). Gluing gives the following exact quotient statement, for any smooth affine \(G\):

\[
[G_{\mathrm{out}}\backslash\operatorname{Gr}_G]
\simeq
\{\mathcal P\in\operatorname{Bun}_G(X):
\mathcal P|_{X-x}\text{ is trivial locally on the base}\}.
\tag{5.1}
\]

The right side means the stack-theoretic image, using the same topology on the base as the quotient. To prove (5.1), add an off-point trivialization to an object on the right. Its choices form a \(G_{\mathrm{out}}\)-torsor, and (3.1) identifies the resulting trivialized object with a point of the Grassmannian. Quotienting removes exactly that choice, including its stabilizer. This is an equivalence of groupoids and is compatible with descent.

**Theorem 5.2 (vector bundles off a point).** Suppose \(X/k\) is smooth, connected and projective, \(k\) is algebraically closed, \(x\in X(k)\), and \(U=X-x\). Let \(S\) be a \(k\)-scheme and \(E\) a vector bundle of rank \(r\) on \(X\times S\). Zariski locally on \(S\),
\[
E|_{U\times S}\simeq
\mathcal O_{U\times S}^{\,r-1}\oplus
\det(E)|_{U\times S}.
\tag{5.2}
\]
In particular an \(SL_r\)-bundle becomes trivial on \(U\times S\) after a Zariski covering of \(S\).

*Proof.* We first show how to split off a line when \(r\geq2\), near an arbitrary point \(s\in S\). The line bundle \(\mathcal O_X(x)\) is ample. Indeed, the curve duality calculation in Roots and reductive groups of rank one, §2, gives \(H^1(X,\mathcal O_X(nx-Z))=0\) for every length-two subscheme \(Z\) once \(n-2>2g-2\). The divisor exact sequence then shows that the complete section system separates distinct points and first-order directions. It gives a projective embedding with \(\mathcal O_X(nx)\) as its hyperplane bundle.

For sufficiently large \(n\), \(E_s(nx)\) is generated by its global sections and has no positive cohomology, by Algebra and sheaf cohomology, Theorem 8.5. We need the relative section module for a vector bundle, so spell out its base change. On a Noetherian affine part of \(S\), a finite affine-cover complex for \(E(nx)\) has flat terms: the curve's chart algebras are base-flat, and the bundle modules are projective over those algebras. Its finite cohomology and Projective cohomology and smooth affine models, Lemma 5.1, give a finite projective complex in nonnegative degrees computing every base change. Trivialize its terms near \(s\). An invertible entry of a differential splits off a contractible pair; row and column operations exhibit the splitting, and \(d^2=0\) makes the adjacent entries zero. Repeat until all remaining differentials are zero modulo the maximal ideal at \(s\). Positive fibre cohomology vanishes, so all remaining positive terms have rank zero. Only a finite free degree-zero term remains. Thus, after shrinking, the module of sections is finite locally free and commutes with every residue-field base change.

Here is the section choice. Over the infinite field \(\kappa(s)\), put \(V=H^0(X_{\kappa(s)},E_s(nx))\). For a geometric point \(y\) of the curve, sections vanishing at \(y\) form a linear subspace of codimension \(r\), because evaluation is surjective. The incidence scheme
\[
Z=\{(y,v)\in X_{\kappa(s)}\times V:v(y)=0\}
\]
is the total space of the kernel of this evaluation. Thus
\(\dim Z=1+\dim V-r<\dim V\).
Its projection to \(V\) is closed, since the curve is projective. The complement is a nonempty open subset of affine space. An infinite field has a rational point in such an open: a nonzero polynomial cannot vanish on all tuples, by induction on the number of variables. Choose the resulting section with no geometric zero.

Lift its finitely many section coordinates from \(\kappa(s)\) to the local base, using the residue-field base change just established. On a neighbourhood it is a section of \(E(nx)\). Its zero scheme is closed in \(X\times S\); its image in \(S\) is closed by projectivity and does not contain \(s\). Remove that image. We obtain a nowhere-vanishing section, hence an exact sequence of vector bundles
\[
0\longrightarrow\mathcal O_X(-nx)
\longrightarrow E\longrightarrow E'\longrightarrow0.
\tag{5.3}
\]
The quotient is locally free: in a local frame at least one section coordinate is a unit, so elementary operations put the section in the first basis position.

These arguments also apply when \(S\) is nonnoetherian. On an affine part \(S=\operatorname{Spec}R\), the finite bundle charts, inverse transition matrices and cocycle identities descend to a finitely generated \(k\)-subalgebra \(R_0\subset R\), by Limits and finite presentation, Theorems 4.1–4.2. Apply the preceding projective argument near the image of \(s\) in \(\operatorname{Spec}R_0\), then pull back its open neighbourhood and sequence. Its residue field is still infinite because it contains \(k\).

Now take \(S\) affine in the chosen neighbourhood. The curve \(U\) is affine: the complement of the positive divisor of the ample bundle \(\mathcal O_X(x)\) is the standard affine open in a sufficiently high projective embedding. Hence \(U\times S\) is affine. On it the first term of (5.3) is canonically trivial. The quotient \(E'|_{U\times S}\) corresponds to a finite projective module. The surjection in (5.3) therefore splits, by the defining lifting property of a projective module.

Repeat for \(E'\), shrinking \(S\) when necessary, until its rank is one. This gives \(E|_{U\times S}\simeq\mathcal O^{r-1}\oplus L\). Taking the determinant identifies \(L\) with \(\det E|_{U\times S}\), proving (5.2); rank one is the initial trivial case. For an \(SL_r\)-bundle its given determinant trivialization makes the last summand trivial. Adjusting the last vector by the invertible determinant of the chosen frame makes that frame respect the prescribed trivialization, and therefore trivializes the \(SL_r\)-torsor. \(\square\)

**Theorem 5.3 (semisimple uniformization).** Suppose \(X\) is projective, \(x\in X(k)\), and \(G/k\) is connected semisimple. Let \(Z\) be the finite central kernel of \(G_{\mathrm{sc}}\to G\), and put \(n=\operatorname{length}(Z)\). For every affine parameter scheme \(S\) and every \(G\)-torsor \(P\) on \(X\times S\), there is an affine faithfully flat morphism of finite presentation \(S'\to S\) for which
\[
P|_{(X-\{x\})\times S'}\simeq G\times(X-\{x\})\times S'.
\]
If \(n\) is invertible in \(k\), the cover may be chosen étale. In particular this holds in characteristic zero, and for simply connected \(G\) in every characteristic.

*Proof.* Sections 6–7 give the full argument, writing \(C=X\). Section 6 proves generic torsor triviality over algebraically closed curve function fields, including their imperfect positive-characteristic cases. Section 7 constructs negative Borel reductions through finite jets, lifts and descends their algebraic modifications, removes the unipotent part on the affine complement, and uses rank-two splitting and a finite flat Jacobian division cover. Section 7.9 assembles the affine covering and treats arbitrary parameter rings. Together with (5.1), the result gives uniformization of \(\operatorname{Bun}_G(X)\). \(\square\)

There is a simple reason to retain the qualification for reductive \(G\). For \(G=\mathbb G_m\), a line bundle trivial off the fixed point is \(\mathcal O_X(mx)\): its chosen rational section has divisor supported at \(x\). If \(X\) has positive genus, choose a distinct point \(y\). The degree-zero bundle \(\mathcal O_X(y-x)\) is nontrivial. Otherwise a rational function with divisor \(y-x\) would define a degree-one map \(X\to\mathbb P^1\), hence an isomorphism: it is finite, and the local rings of the smooth target are integrally closed. This contradicts positive genus. A degree-zero divisor supported at \(x\) must be zero, so this line bundle has no off-point trivialization. Base extension cannot remove the obstruction at this geometric point.


## 6. Semisimple torsors over curve function fields

### 6.1. The field theorem and its prerequisites

Let \(l\) be algebraically closed, \(C/l\) an integral smooth projective curve, \(K=l(C)\), and \(G/l\) split semisimple. We prove
\[
H^1(K,G_K)=1.
\tag{6.1}
\]
The function field \(K\) need not be perfect; the proof includes positive characteristic.

We use the following earlier programme proofs, with the indicated statements and locators.

* Étale cohomology, Brauer groups and Tsen's theorem, Theorems 3.1, 4.4 and 5.1 and Corollary 6.1: matrix descent, \(\operatorname{Br}(F)=0\) and \(C_1\) for all finite \(F/K\), Tsen, and unit cohomology. Its §§1–3 specify the earlier Noether-algebra proofs of matrix descent and separable splitting over imperfect fields.
* NT-CFT, Brauer groups of local and global fields, §3: complete Tate resolution, long exact sequences, induced acyclicity, restriction/corestriction and the two-consecutive-degree criterion. No local- or global-field theorem is needed here.
* AG-RG-01, Theorem 4.2: existence of a geometrically maximal torus over an arbitrary field, including imperfect fields. AG-RG-01, Lemma 3.3: the cocharacter open cell.
* AG-RG-02, §§1 and 3: every geometric element belongs to a Borel, Jordan factors lie in the group, every semisimple element lies in a maximal torus, and the smooth centralizer and regular-semisimple calculations. AG-RG-04, §§1–3 and 5, Theorem 6.2: root data, Weyl action, ordered root products and Bruhat cells. AG-RG-03, Theorems 7.1 and 8.1: the rank-one maps and identities.
* AG-RG-03, Theorem 1.1, and AG-RG-04, Theorem 7.1: affine central multiplicative-type quotients and their torsors, including inseparable finite kernels. AG-RG-05, Theorem 10.1: the split simply connected cover, obtained by its constructed integral group and central quotient.
* AG-GS, Group schemes, actions and Hopf algebras, Lemma 5.1: every vector in a field comodule lies in a finite-dimensional subcomodule. AG-CA, Discrete valuation rings, normal rings and Serre's criterion, Theorem 3.3: the written height-one intersection/Hartogs proof; the preceding regular-local and smooth-algebra lessons supply normality of a smooth integral variety.

Section 6.4 constructs the needed fundamental representations from root coordinates in every characteristic.

### 6.2. All nonsplit tori have trivial first cohomology

We first prove the finite-module lemma that makes this statement follow from Tsen. Write coefficient groups additively throughout the module argument. A module \(A\) for a finite group \(\Gamma\) is called cohomologically trivial if \(\widehat H^q(H,A)=0\) for all subgroups \(H\) and all integers \(q\).

**Lemma 6.2.A.** A cohomologically trivial \(\Gamma\)-module \(A\) has an exact sequence
\[
0\longrightarrow P_1\longrightarrow P_0\longrightarrow A\longrightarrow0
\tag{6.2}
\]
with \(P_0,P_1\) projective over \(\mathbb Z[\Gamma]\). Consequently, if \(M\) is free of finite rank over \(\mathbb Z\), with any \(\Gamma\)-action, then \(A\otimes_{\mathbb Z}M\), with the diagonal action, is cohomologically trivial.

**Proof.** Here are the required elementary steps, also for infinite modules.

For a finite \(p\)-group \(P\), the augmentation ideal \(J\) of \(\mathbb F_p[P]\) is nilpotent. Induct on \(|P|\), choosing a central element \(z\) of order \(p\). The quotient by \((z-1)\) is \(\mathbb F_p[P/\langle z\rangle]\). If its augmentation ideal has \(m\)-th power zero, then \(J^m\subset(z-1)\); centrality and \((z-1)^p=0\) give \(J^{mp}=0\). Here the required central element follows directly by counting conjugacy classes: every noncentral class has size divisible by \(p\), so the centre has order divisible by \(p\) and contains a nonidentity element. Coset counting makes that element's order a positive power of \(p\); its last nonidentity \(p\)-power has order \(p\).

If an \(\mathbb F_p[P]\)-module \(V\) is cohomologically trivial, the norm is an isomorphism \(V_P\to V^P\), by the degree minus-one and zero Tate formulas. Choose a basis of \(V_P\), lift it to \(V\), and map the free module \(F=\mathbb F_p[P]^{(I)}\) on these lifts onto \(V\). This map is surjective: its cokernel \(D\) has \(D/JD=0\), and nilpotence of \(J\) gives \(D=0\), with no finite-generation assumption. On coinvariants the map is an isomorphism. Norms for \(F\) and \(V\) therefore show it is an isomorphism on invariants too. Its kernel has no invariant vector. But a nonzero module over this group algebra has a nonzero invariant vector: the last nonzero term of its \(J\)-power filtration is annihilated by \(J\). Thus the kernel is zero and \(V\) is free. Conversely such free modules are induced and have zero Tate cohomology.

If \(B\) has no \(p\)-torsion, the sequence \(0\to B\xrightarrow{p}B\to B/pB\to0\) shows that cohomological triviality of \(B\) implies that of \(B/pB\). Conversely, if \(B/pB\) is free over \(\mathbb F_p[P]\), multiplication by \(p\) is an isomorphism on every Tate group of \(B\). These groups are killed by \(|P|\), by restriction/corestriction. They must therefore be zero.

Let \(L\) be free over \(\mathbb Z\) and cohomologically trivial for \(P\), and let \(B\) have no \(p\)-torsion. Then \(\operatorname{Hom}_{\mathbb Z}(L,B)\), with its usual diagonal action, is cohomologically trivial for \(P\). Indeed multiplication by \(p\) is injective on it, and its quotient is
\(\operatorname{Hom}_{\mathbb F_p}(L/pL,B/pB)\): choose lifts of the images of an abelian basis of \(L\) to prove surjectivity. The first argument \(L/pL\) is free over \(\mathbb F_p[P]\), by the preceding paragraph. If it is \(\mathbb F_p[P]\otimes V\), then this Hom module is coinduced from \(\operatorname{Hom}_{\mathbb F_p}(V,B/pB)\). Explicitly the untwisting coordinate for a map \(f\) is \(g^{-1}f(g\otimes v)\); \(P\) permutes the \(g\)-coordinates. Since \(P\) is finite, coinduction is induction on a vector space and hence free. The preceding \(p\)-torsion-free argument proves the assertion.

Now suppose \(L\) is free abelian and cohomologically trivial for \(\Gamma\). Take the equivariant free surjection \(\mathbb Z[\Gamma]\otimes L\to L\), \(g\otimes v\mapsto gv\), and let \(R\) be its kernel. The underlying sequence splits because \(L\) is free abelian, and \(R\) is free abelian. Tate exactness makes \(R\) cohomologically trivial. Apply the last paragraph to every Sylow subgroup, with \(B=R\). Restriction/corestriction kills each primary part of
\(H^1(\Gamma,\operatorname{Hom}_{\mathbb Z}(L,R))\), so this group is zero. Applying invariants to
\[
0\to\operatorname{Hom}_{\mathbb Z}(L,R)
\to\operatorname{Hom}_{\mathbb Z}(L,\mathbb Z[\Gamma]\otimes L)
\to\operatorname{Hom}_{\mathbb Z}(L,L)\to0
\]
therefore lifts the identity to a \(\Gamma\)-equivariant section. Thus \(L\) is projective over \(\mathbb Z[\Gamma]\).

For arbitrary \(A\), take a free \(\mathbb Z[\Gamma]\)-module \(P_0\) surjecting onto it. Its kernel \(P_1\) is free abelian and, by Tate exactness, cohomologically trivial. The preceding result makes it projective. The subgroup-of-free-abelian assertion used here allows arbitrary rank: well-order a basis of the ambient group, intersect with its successive initial spans, observe that each new quotient is a subgroup of \(\mathbb Z\), and choose its free generator lift; at a limit take the union.

Tensor (6.2) with the free abelian \(M\). This remains exact. A projective \(\mathbb Z[\Gamma]\)-module tensored with \(M\) is still projective for the diagonal action: on a regular summand untwist by \(g\otimes m\mapsto g\otimes g^{-1}m\), leaving the action only on the regular factor. Tate exactness and acyclicity of the two projectives prove the final assertion. \(\square\)

Let now \(T/K\) be **any** torus, and choose a finite Galois splitting field \(L/K\), group \(\Gamma\). Put \(A=L^\times\). For every \(H\subset\Gamma\), let \(F=L^H\). Hilbert 90 gives \(H^1(H,A)=0\), and \(\operatorname{Br}(F)=0\) gives \(H^2(H,A)=0\). To make the latter finite-level inference explicit, a factor system \(a_{\sigma,\tau}\) gives semilinear operators on the \(L\)-space with basis \(e_\tau\),
\[
D_\sigma(e_\tau)=a_{\sigma,\tau}e_{\sigma\tau},
\qquad D_\sigma D_\tau=a_{\sigma,\tau}D_{\sigma\tau}.
\]
Their conjugations descend its matrix algebra to a central simple \(F\)-algebra. It is split because \(\operatorname{Br}(F)=0\). Comparing the two \(L\)-matrix identifications by the proved matrix Skolem–Noether theorem makes each \(D_\sigma\) a scalar times the transported ordinary semilinear operator. Their multiplier is consequently the coboundary of those scalars. This proves \(H^2(H,L^\times)=0\) directly, including characteristic \(p\).

The two-degree criterion in NT-CFT §3 now makes \(A\) cohomologically trivial. The cocharacter lattice \(M=X_*(T_L)\) is free of finite rank, and \(T(L)=M\otimes_{\mathbb Z}L^\times\), with its diagonal Galois action. Lemma 6.2.A gives \(H^1(\Gamma,T(L))=0\). Any \(T\)-torsor becomes trivial over \(L\), since the split torus there has trivial first cohomology by Hilbert 90. Its descent cocycle is therefore a \(\Gamma\)-cocycle in \(T(L)\), and the preceding vanishing trivializes it. Thus
\[
H^1(K,T)=1\quad\hbox{for every \(K\)-torus \(T\)}.
\tag{6.3}
\]
The same reasoning applies over every finite extension of \(K\).

For comparison, Tsen also proves the norm assertion without cohomological terminology. For a finite field extension \(E/F\) of degree \(d\) and \(a\ne0\), the form \(N_{E/F}(x)-ay^d\) has degree \(d\) in \(d+1\) variables. A nonzero \(C_1\) solution has \(y\ne0\), because a field element of norm zero is zero. It gives \(N(x/y)=a\). This includes inseparable extensions, although the torus splitting fields above are separable.

### 6.3. A strongly regular rational point in the inner form

There is a short proof of the density needed here that uses the maximal-torus theorem rather than an unproved rationality theorem for reductive groups.

For a torus \(T\) over any infinite field \(F\), choose a finite Galois splitting field \(L/F\). The norm morphism
\[
\operatorname{Res}_{L/F}(T_L)\longrightarrow T
\tag{6.4}
\]
is dominant: over a splitting field it is multiplication from a product of conjugate copies of \(T\), hence surjective. Its source is isomorphic to a power of \(\operatorname{Res}_{L/F}\mathbb G_m\), an open in affine space (invert the determinant of multiplication in \(L\)). Every nonempty open in this affine space has an \(F\)-point: a nonzero polynomial cannot vanish on all tuples over an infinite field. The inverse image of any nonempty open of \(T\) therefore has such a point. Consequently \(T(F)\) is Zariski dense.

Let \(H/F\) be an inner form of a split semisimple group. AG-RG-01 Theorem 4.2 provides a geometrically maximal \(F\)-torus \(T\) in it. In \(T_{\bar F}\), remove the loci \(\alpha(t)=1\) for every root and \(w(t)=t\) for every nonidentity Weyl element. This is a nonempty open: each root is a nonzero Laurent character, and the Weyl action on the torus lattice is faithful, so each fixed locus is proper, also in bad characteristic. The collection is Galois invariant and descends to an \(F\)-open. Density gives an \(h\in T(F)\) in it.

For this \(h\), the centralizer is smooth: the reduced diagonalizable closure of its powers has exact invariants, as in the AG-RG-02 semisimple-centralizer proof. Its tangent space is the zero-root part, namely \(\operatorname{Lie}T\), so its identity component is \(T\). Every component centralizes \(h\) and normalizes that identity torus. The Weyl fixed-point exclusions make its image in \(N_H(T)/T\) trivial. Thus the entire centralizer is \(T\), as a group scheme. This proves existence of a **strongly** regular semisimple \(F\)-point without assuming \(F\) perfect and without asserting that the whole group is rational.

### 6.4. Constructing the fundamental modules in arbitrary characteristic

For the moment \(G/F\) is split semisimple simply connected over any field. Fix \(T,B=TU^+\), opposite \(U^-\), simple roots \(\alpha_i\), fundamental weights \(\omega_i\), and rank-one maps \(\operatorname{SL}_2\to G\). The simple coroots are a basis of \(X_*(T)\). Hence each rank-one map is injective: its possible central kernel is contained in the coroot torus, whose primitive lattice map has no kernel. Denote its image by \(G_i\simeq\operatorname{SL}_2\).

For a dominant weight \(\lambda\), define a rational function on the big cell by
\[
d_\lambda(u_-tu_+)=\lambda(t).
\tag{6.5}
\]
We prove that it extends to a nonzero regular function on \(G\).

The opposite Bruhat decomposition has cells \(B^-n_wB\) of codimension \(\ell(w)\); it follows from the Bruhat theorem by translation by the longest Weyl element. Thus only the cells for the simple reflections contribute boundary divisors. A neighbourhood of such a cell is given by the cocharacter open cell
\[
U^-_{\Phi^+\setminus\{\alpha_i\}}\ \times L_i\
\times U^+_{\Phi^+\setminus\{\alpha_i\}},
\tag{6.6}
\]
where \(L_i\) has roots \(\pm\alpha_i\). As a scheme \(L_i\simeq G_i\times T_{0,i}\): take the subtorus \(T_{0,i}\) generated by the other simple coroots. Its map onto \(L_i/G_i=T/\alpha_i^\vee(\mathbb G_m)\) is an isomorphism, so the multiplication map has the stated inverse. This is a semidirect product assertion, not a claim that the two factors commute. The quotient and rank-one assertion are also immediate in each of the three actual rank-one models of AG-RG-03 Theorem 8.1.

Write the \(\operatorname{SL}_2\) coordinate as \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\). On \(a\ne0\), the Gauss identity factors it as
\[
x_{-\alpha_i}(c/a)\,\alpha_i^\vee(a)\,x_{\alpha_i}(b/a).
\]
Thus in (6.6) the rational function (6.5) is
\[
a^{\langle\lambda,\alpha_i^\vee\rangle}\lambda(t_0).
\tag{6.7}
\]
The exponent is nonnegative, so this is regular across \(a=0\), in every characteristic. The chart contains \(n_i\) and the entire codimension-one opposite Bruhat cell: its omitted root products, torus and \(a=0\) rank-one coordinates give the coordinates of that cell. All possible remaining poles have codimension at least two. Smoothness makes \(G\) normal, and AG-CA Theorem 3.3, applied on affine charts, extends the function. This extends across the height-one charts without requiring factoriality of \(F[G]\).

Act on \(F[G]\) by right translation, \((\rho(g)f)(h)=f(hg)\), and let \(V_\lambda\) be the rational submodule generated by \(d_\lambda\): equivalently, take its coaction coefficients and the smallest subcomodule containing them. Lemma 5.1 of the Hopf-algebra lesson makes this module finite dimensional. This definition uses the group scheme, rather than only its \(F\)-point translates. The function is fixed by right \(U^+\) and has \(T\)-weight \(\lambda\). The big cell is dense, so \(V_\lambda\) is already generated by the coaction coefficients of its \(U^-\)-orbit: a linear functional annihilating those coefficients gives a regular matrix coefficient vanishing on the big cell, hence everywhere. Over the intended infinite field, the root-coordinate affine spaces also have dense \(F\)-points, so their literal translates span the same module.

Conjugating a root action by \(T\) and comparing Laurent characters shows that the coefficient of \(s^n\) in \(\rho(x_{-\beta}(s))v\), for \(v\) of weight \(\mu\), has weight \(\mu-n\beta\). Here \(n\ge0\) because the root action is polynomial. Ordered negative root products show
\[
\operatorname{weights}(V_\lambda)\subset\lambda-\mathbb N\Phi^+,
\qquad (V_\lambda)_\lambda=F d_\lambda.
\tag{6.8}
\]
Normalizer representatives permute weight spaces, so multiplicities are Weyl invariant. These are genuine rational group representations, constructed in characteristic \(p\) directly; no Lie integration or complete reducibility has been used.

Take \(V_i=V_{\omega_i}\), and write \(\chi_i(g)=\operatorname{tr}(g\mid V_i)\). Their restrictions to \(T\) generate \(F[X^*(T)]^W\). To prove this, orbit sums of Laurent monomials form a basis of the invariant ring in every characteristic, because invariance means equality of the coefficients in a permutation orbit. The character of \(V_\lambda\) has coefficient one on the orbit of \(\lambda\), and all other dominant weights \(\mu\) satisfy \(\lambda-\mu\in\mathbb N\Phi^+\setminus\{0\}\).

For a dominant \(\lambda=\sum n_i\omega_i\), the product \(\prod\chi_i^{n_i}\), the character of the tensor product, consequently equals its orbit sum plus lower dominant orbit sums. Induct to express all orbit sums in the \(\chi_i\). Termination can be checked using \(\rho^\vee=\frac12\sum_{\beta>0}\beta^\vee\): its pairing is positive on every fundamental weight and on every positive root, with \(\langle\alpha_i,\rho^\vee\rangle=1\), so dominant weights below a fixed height form a finite set and lowering a nonzero positive-root sum strictly lowers height. The same leading-orbit argument proves algebraic independence. Therefore
\[
F[T]^W=F[\chi_1|T,\ldots,\chi_r|T].
\tag{6.9}
\]
The map \(T\to\mathbb A^r\) defined by these functions is finite and surjective. Indeed every element of \(F[T]\) satisfies its monic orbit polynomial, so the finite set of Laurent algebra generators makes this ring finite over its invariant ring; lying over proves surjectivity. Over an algebraic closure its fibres are exactly the Weyl orbits. To check separation without averaging or dividing by \(|W|\), choose a regular function zero on one finite orbit and one on a disjoint orbit by the Chinese remainder theorem; the product of all its Weyl translates is invariant and has those same two values.

### 6.5. A section for strongly regular semisimple classes

Choose the linked root parametrizations so that
\[
n_i=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\in G_i,
\qquad
s(a_1,\ldots,a_r)=\prod_{i=1}^r x_{\alpha_i}(a_i)n_i
\tag{6.10}
\]
in one fixed order. We now compute the traces, rather than importing the Steinberg cross-section theorem.

For a weight \(\mu\), put \(m_j=\langle\mu,\alpha_j^\vee\rangle\), and let \(\pi_\mu\) be its weight projection. In \(y_j=x_{\alpha_j}(a_j)n_j\), a vector of weight \(\mu\) first changes to \(s_j\mu=\mu-m_j\alpha_j\) and then to weights \(\mu+(n-m_j)\alpha_j\), \(n\ge0\). In a diagonal block of the product \(\prod y_j\), each simple root appears at exactly one step. Their linear independence forces every step to return to \(\mu\). Thus
\[
\pi_\mu\Bigl(\prod y_j\Bigr)\pi_\mu
=\prod_j(\pi_\mu y_j\pi_\mu).
\tag{6.11}
\]
If some \(m_j<0\), the corresponding factor is zero. Otherwise this block is a constant operator times \(\prod_j a_j^{m_j}\), by the polynomial root-action calculation. Only dominant weights contribute to a trace.

For \(V_i\), the highest-weight contribution is exactly \(a_i\). Here is the coefficient check in small characteristics. The \(\alpha_i\)-string through \(\omega_i\) contains only \(\omega_i,\omega_i-\alpha_i\), each once: further negative weights would reflect to a weight strictly above the highest weight. Put \(v=d_{\omega_i}\), \(v_-=n_iv\). Then \(n_iv_-=-v\), and \(x_{\alpha_i}(a)v_-=v_-+ca v\) for some scalar \(c\). The rank-one identity \((x_{\alpha_i}(-1)n_i)^3=1\), computed in \(\operatorname{SL}_2\), says that the matrix \(\left(\begin{smallmatrix}-c&-1\\1&0\end{smallmatrix}\right)^3\) is the identity. Its bottom-right entry is \(c\), so \(c=1\), including characteristics two and three. Thus the highest diagonal coefficient of \(y_i\) is \(a_i\). For \(j\ne i\) there is no adjacent \(\alpha_j\)-weight: reflection would again give a weight above the highest weight. Both root groups therefore fix this line, and their generated \(G_j\) fixes it; the highest diagonal coefficient of \(y_j\) is one.

For any other dominant weight \(\mu=\sum m_j\omega_j\) of \(V_i\), its height \(\langle\mu,\rho^\vee\rangle\) is strictly below that of \(\omega_i\). Every \(j\) with \(m_j>0\) consequently has strictly smaller fundamental-weight height than \(\omega_i\). Summing (6.11) gives
\[
\chi_i(s(a))=a_i+
f_i\bigl(a_j:\langle\omega_j,\rho^\vee\rangle<
\langle\omega_i,\rho^\vee\rangle\bigr),
\tag{6.12}
\]
for a polynomial \(f_i\) over \(F\). Order the indices by those heights. The equations are triangular with diagonal coefficient one, so recursive substitution constructs a polynomial inverse to the map \(a\mapsto(\chi_i(s(a)))_i\). In particular, every vector of invariant values in \(F^r\) is attained by an actual point of \(G(F)\), with no purely inseparable descent step.

The multiplicative Jordan factors used next belong to \(G\). We retain the characteristic-zero exponential-polynomial proof in AG-RG-01 §4, and supply the positive-characteristic step explicitly. Write \(g=tu\) inside a faithful matrix group over the algebraic closure, with \(t\) semisimple, \(u\) unipotent, and the two commuting. Choose \(q=p^r\) with \(u^q=1\). Let \(D\) be the reduced closure of the powers of \(t\), a diagonalizable group: diagonalizing \(t\) puts this closure in a torus. Its geometric points form a torus times a finite group of order prime to \(p\). The map \([q]:D\to D\) is therefore surjective; on the torus every nonzero scalar has a \(q\)-th root, and on that finite group \(q\) is invertible. It need not be an automorphism. Its image of the dense powers of \(t\) is dense in \(D\): a regular function vanishing on that image has pullback vanishing on the dense cyclic subset, hence on \(D\), and surjectivity then makes the original function zero. Since \(g^{nq}=t^{nq}\), these dense powers lie in \(G\); its closedness gives \(D\subset G\). Hence \(t\in G\) and \(u=t^{-1}g\in G\), as required.

Suppose \(h\in G(\bar F)\) is strongly regular semisimple and all \(\chi_i(h)\) belong to \(F\). Let \(g_0=s(a)\in G(F)\) be the point with these values. Its geometric Jordan factors \(g_0=t u\) lie in \(G\) by the preceding argument. Traces of \(g_0\) equal traces of \(t\): \(u\) commutes with \(t\), and its restriction to each \(t\)-eigenspace is unipotent with trace equal to the dimension. Conjugate the semisimple \(t\) and \(h\) into \(T\) using the proved semisimple conjugacy theorem. Equation (6.9) and finite-orbit separation show that they are Weyl conjugate. Hence the full centralizer of \(t\) is a torus, and its commuting unipotent \(u\) is one. Thus \(g_0\) itself is strongly regular semisimple and geometrically conjugate to \(h\).

We have proved exactly the rational-class representative needed by the cocycle argument. We did not need the stronger theorem about every dimension-regular element or its unipotent centralizer.

### 6.6. The simply connected cocycle argument

Let \(z_\sigma\in G(K^s)\) be a continuous cocycle. Twist \(G\) by its conjugation descent, obtaining the smooth reductive inner form \(H\). The construction and affine effectivity are the AG-RG-06 §4 torsor proof. By 6.3 it contains a strongly regular semisimple \(h\in H(K)\). In the identification \(H_{K^s}=G_{K^s}\),
\[
z_\sigma\,\sigma(h)\,z_\sigma^{-1}=h.
\tag{6.13}
\]
Since \(\chi_i\) is conjugation invariant and defined over \(K\), (6.13) gives \(\sigma(\chi_i(h))=\chi_i(h)\); thus all these values lie in \(K\), not merely its perfect closure. Section 6.5 gives a geometrically conjugate \(h_0\in G(K)\).

The transporter from \(h_0\) to \(h\) is a nonempty torsor under their torus centralizer and hence a smooth scheme over \(K^s\). It has a \(K^s\)-point even when \(K^s\) is imperfect. Indeed a nonempty smooth scheme over a separably closed field has an étale chart to affine space, its image contains a rational point of an affine open, and the nonempty étale fibre has a rational closed point. Choose \(b\in G(K^s)\) with \(h=bh_0b^{-1}\). Equation (6.13) now says
\[
b^{-1}z_\sigma\sigma(b)\in C_G(h_0)(K^s).
\tag{6.14}
\]
This is a genuine cocycle in the nonsplit \(K\)-torus \(C_G(h_0)\). Its first cohomology vanishes by (6.3), so (6.14) and then \(z\) are coboundaries. This proves (6.1) for simply connected \(G\).

### 6.7. Removing simple connectedness with a smooth torus kernel

Let \(G_{\mathrm{sc}}\to G\) be the split simply connected cover, kernel \(Z\). The actual split root-datum construction makes \(Z\) finite diagonalizable. Choose generators of its finite character group, giving an embedding \(i:Z\hookrightarrow S=\mathbb G_m^m\), and form the represented affine central quotient
\[
E=(G_{\mathrm{sc}}\times S)/
\{(z,i(z)^{-1}):z\in Z\}.
\tag{6.15}
\]
This construction includes \(\mu_p\)-kernels. Projection onto \(G\) has kernel **\(S\)**, not \(S/i(Z)\). Projection onto \(R=S/i(Z)\) has kernel \(G_{\mathrm{sc}}\). Both maps are torsors under the displayed smooth groups, as checked after the faithfully flat covers \(G_{\mathrm{sc}}\to G\) and \(S\to R\), respectively. The torus \(R\) is split: its character lattice is the finite-index kernel of \(\mathbb Z^m\to X^*(Z)\). Thus
\[
1\to S\to E\to G\to1,\qquad
1\to G_{\mathrm{sc}}\to E\to R\to1
\tag{6.16}
\]
are exact, with smooth kernels. In particular their maps on separable-closure points are surjective, by the smooth-point argument in 6.6. We do **not** assert that \(G_{\mathrm{sc}}(K^s)\to G(K^s)\) is surjective for an inseparable central isogeny.

Lift a continuous \(G(K^s)\)-cocycle to a continuous \(E(K^s)\)-cochain \(e_\sigma\). Such lifts can be chosen for its finitely many values and lie in a finite separable extension; hence the cochain is continuous. The central defect
\[
a_{\sigma,\tau}=e_\sigma\sigma(e_\tau)e_{\sigma\tau}^{-1}
\in S(K^s)
\]
is a 2-cocycle by associativity. Its class is zero because
\(H^2(K,S)=\operatorname{Br}(K)^m=0\), by the proved Brauer/cohomology identification. Correcting by a scalar 1-cochain therefore turns \(e\) into an \(E\)-cocycle.

Its image in the split torus \(R\) is a coboundary by Hilbert 90. Lift the element furnishing that coboundary to \(E(K^s)\), possible by smoothness of \(E\to R\), and change the cocycle accordingly. The changed cocycle lies in \(G_{\mathrm{sc}}(K^s)\). Section 6.6 makes it a coboundary. Thus the \(E\)-cocycle, and its original image in \(G\), are trivial. This proves (6.1) for every split semisimple \(G\), in all characteristics.

## 7. Uniformization in families

### 7.1. The family theorem and its prerequisites

Let \(k\) be algebraically closed, \(C/k\) a smooth projective connected curve, \(x\in C(k)\), and \(U=C-\{x\}\). Let \(G/k\) be a connected semisimple group and let
\[
1\longrightarrow Z\longrightarrow G_{\mathrm{sc}}
 \longrightarrow G\longrightarrow1,\qquad
n=\operatorname{length}(Z)=|\pi _1(G)|.
\]
For every affine \(k\)-scheme \(S\), and every \(G\)-torsor \(P\) on \(C\times S\), there is an affine faithfully flat morphism of finite presentation \(S'\to S\) such that
\[
P|_{U\times S'}\simeq G\times U\times S'.
\tag{7.1}
\]
If \(n\) is invertible in \(k\), this cover can be chosen étale. Throughout, torsors are fppf torsors. The assertion includes arbitrary nonnoetherian rings of test parameters.

Here are the earlier programme results used in the proof; the local arguments below supply the additional cohomology and parameter-space steps.

* Section 6 proves \(H^1(\ell(C),G)=1\) when \(\ell\) is algebraically closed, in every characteristic. We use it only over an algebraic closure of a residue field, in 7.4. We do not assert this theorem for an imperfect separably closed residue field.
* Sections 1–2, proves the affine Beauville–Laszlo equivalence for modules, algebras and affine torsors when \(f\) is a nonzerodivisor in both rings and the quotient maps modulo every \(f^a\) are isomorphisms. The same lesson constructs the fixed-curve formal patch with ring \(R[[t]]\). Tori and root data, Theorem 2.C, proves split Cartan decomposition over each field. No representability or ind-projectivity assertion about a general affine Grassmannian is used here.
* AG-RG-03, §2, together with the calculation in AG-RG-S02, §6, proves curve duality. AG-RG-S01, §§3–8, supplies affine Čech cohomology, projective coherent finiteness, Serre generation and vanishing. AG-RG-S02, Lemma 5.1, gives a universally tensor-compatible finite projective complex; its proof uses a descending free resolution and flat truncation. We use its same construction for vector bundles and flat coherent sheaves.
* AG-HP, Regularity and bounded families, Theorem 4.1, gives the written uniform kernel bound. Its Flattening stratifications, Theorem 6.1, gives the determinantal, stabilized graded construction. Its Hilbert and Quot schemes, Theorem 4.1, **proof of representability**, constructs the locally closed finite-type parameter scheme needed here. For this use we require its universal property only on Noetherian tests; 7.2 supplies the flat-cohomology input on those tests. We do not consume that theorem's separately imported Noetherian DVR properness criterion.
* AG-HP, The Picard functor and the Picard scheme of a curve, Theorem 2.1, Proposition 5.1, Lemma 6.1, Theorems 6.2 and **7.2**, contains the rigidification, translated-chart construction and properness argument. 7.2 supplies the Cartier, cohomology, symmetric-power properness and completion bridges used in that construction. Its no-section Leray obstruction calculation is not used.
* AG-GS, Abelian varieties, Proposition 1.2 and the square/cube and multiplication proofs, Theorems 5.1, 6.1–6.2, supply projectivity and finite surjectivity of multiplication. 7.2 supplies the two imported line-bundle prerequisites in its underlying smooth-group quasi-projectivity argument for this Jacobian; 7.8 proves the exact finite-flatness step that the printed proof refers to as miracle flatness.
* AG-MO, Limits and Noetherian approximation, Theorems 4.1–4.2, supplies finite-presentation data, maps, inverses and finite equations. Its paragraph importing eventual flatness, smoothness and surjectivity is not used: 7.6 supplies the particular finite witnesses and proper-image argument required here.
* AG-RG-06, Theorems 1.1–2.1, proves the root Levi groups and smooth projective flag schemes, including the descent of their canonical ample line bundle. AG-RG-03, Theorem 8.1, proves the three rank-one matrix models. AG-CA, Formally smooth, unramified and étale ring maps, Theorems 3.1 and 5.1, proves the conormal lifting criterion and local standard form. AG-CA, Henselian local rings and henselization, Theorems 1.2 and 5.1, proves the section criterion and strict-henselian filtered-neighbourhood construction. AG-FSE, Flat morphisms, Theorems 2.2 and 3.2, proves generization lifting and openness; its Noetherian image input is the AG-MO Quasi-finite morphisms and Chevalley's theorem, Lemma 4.1 and Theorem 4.2, proved by Noether normalization and induction on closed subsets.

### 7.2. Cohomology and parameter-space bridges

We prove the cohomology and parameter-space assertions needed for reductions and Jacobian division.

**Finite complexes.** On a projective scheme over a Noetherian affine base \(A\), a coherent sheaf flat over \(A\) has a finite affine-cover complex with \(A\)-flat terms and finite cohomology. For flatness of its chart section modules, apply the stalkwise definition: tensor an injection of base modules with the quasi-coherent sheaf; exactness at every stalk gives exactness of chart modules. Finite intersections of the chosen affine opens are affine because the scheme is separated. The complex computes cohomology and commutes with every base tensor, by affine modules and localization. AG-RG-S02 Lemma 5.1 applies exactly to this bounded complex. Consequently it gives a finite projective complex computing every base tensor, including tensoring with a module which is not flat.

Here is the useful local operation on such a complex \(K\). At a parameter point, an invertible entry of a differential is changed by row and column operations to a block \(A\xrightarrow{1}A\). The equations \(d^2=0\) make its adjacent blocks zero. Cancel this contractible pair and repeat, shrinking the base each time. The remaining differentials are zero modulo the parameter prime. The remaining free terms modulo that prime are therefore its fibre cohomology. If the fibre cohomology is confined to degree zero, all other terms have rank zero, leaving one finite free term in degree zero. The cancellations remain valid after every tensor. If only the alternating Euler characteristic is wanted, the alternating sum of the ranks is already locally constant. These are proofs of the precise base-change, open-locus and Euler assertions used here.

For line bundles on the fixed \(C\) over an arbitrary affine base, use the written finite-presentation model construction in AG-RG-S02, §3, and apply this complex argument to the Noetherian model. Its tensor with the original base computes the affine-cover complex of the original line bundle. Thus the same open-cohomology and Euler assertions hold on every test base.

For completeness, on a smooth projective geometrically integral curve over any field extension of \(k\), choose a rational section of a line bundle. Its finitely many valuations give a divisor. Adding or subtracting one closed point changes Euler characteristic by its residue-field degree, using the divisor exact sequence. Hence
\[
\chi(L)=\deg L+1-g.
\tag{7.2}
\]
The proved duality gives \(h^1(L)=h^0(\omega_C L^{-1})\). Applying (7.2) and duality to \(\omega_C\) gives \(\deg\omega_C=2g-2\). A nonzero section of a line bundle has an effective zero divisor, so a bundle of negative degree has no section. In particular,
\[
\deg L>2g-2\quad\Longrightarrow\quad H^1(C,L)=0.
\tag{7.3}
\]
The genus and these calculations are unchanged under field extension by the affine-cover complex over a field.

**A projective finite-fibre morphism is finite in the setting used here.** Suppose \(Y\to T\) is projective, \(T\) is Noetherian over \(k\), and the fibres are finite. At \(t\in T\), a linear form in a projective embedding can be chosen nonzero at every geometric point of \(Y_t\). Indeed each of the finitely many closed points imposes a proper linear subspace on the coefficients over \(\kappa(t)\); this field contains the infinite field \(k\). Lift the coefficients near \(t\), shrinking so that one of them is a unit. The hyperplane intersection has closed image by projectivity, missing \(t\). After removing that image, \(Y\) lies in the affine complement of the hyperplane, and is closed there. Thus it is affine over a neighbourhood of \(t\). Over a Noetherian affine such neighbourhood, projective coherent finiteness makes \(\Gamma(Y,\mathcal O_Y)\) a finite module. Its affine description is consequently finite. This proves the claim locally on \(T\). All later uses of proper finite-fibre finiteness are for such projective Noetherian morphisms; no general Zariski Main theorem with an unproved nonaffine gluing step is needed.

**The needed Cartier criterion.** Let \(A\to B\) be a flat map of Noetherian rings, with \(B\) of finite type, and let \(f\in B\) be a nonzerodivisor on every fibre at the source points under consideration. Then \(f\) is a nonzerodivisor and \(B/fB\) is \(A\)-flat there. To prove the first claim, localize at a source point and its image \((A,\mathfrak m)\). Flatness identifies
\[
\mathfrak m^aB/\mathfrak m^{a+1}B
 =(\mathfrak m^a/\mathfrak m^{a+1})\otimes_A B.
\]
Multiplication by the fibre image of \(f\) is injective on this module: it is a direct sum of copies of its injective action on \(B/\mathfrak mB\). If \(fb=0\), induction puts \(b\) in every \(\mathfrak m^aB\); Noetherian Krull intersection, with \(\mathfrak mB\) in the local maximal ideal, gives \(b=0\). Apply precisely this argument after every quotient \(A/J\). The ring \(B/JB\) is flat over \(A/J\), and has the same relevant field fibres, so \(f\) is injective on \(B/JB\). The resolution
\[
0\longrightarrow B\xrightarrow{f}B\longrightarrow B/fB\longrightarrow0
\]
then gives \(\operatorname{Tor}_1^A(A/J,B/fB)=0\) for every ideal \(J\). The ideal criterion for flatness proved in the Tor lesson makes \(B/fB\) flat. Since this sequence consists of flat base modules, it remains exact after every base change.

Conversely, suppose \(I\subset B\) is finite, \(B/I\) is \(A\)-flat, and its fibre ideal at a point is generated by a nonzerodivisor \(\bar f\). The kernel sequence remains exact on the residue field, and \(I\) is \(A\)-flat. Lift \(\bar f\) to \(f\in I\). Nakayama makes \(B\to I,\ b\mapsto bf\), surjective locally. Its kernel is finite; tensoring with the residue field is still exact because \(I\) is flat, and the fibre map is injective. Nakayama makes this kernel zero. Thus \(I=(f)\) is invertible and \(f\) is regular. This proves the required fibrewise Cartier statement for Noetherian universal families.

There is no arbitrary-base gap in its later application to a nonspecial line bundle. Descend that line bundle to a Noetherian model; the finite cohomology complex cuts out the open locus \(h^0=1,h^1=0\) through which the original base factors. There evaluation is a section nonzero on every curve fibre. The just-proved criterion makes its zero scheme a flat Cartier divisor, and exactness persists on the original arbitrary base. The same argument works for a fibrewise nonzero section of a universal line bundle with locally free pushforward.

**What is consumed from Hilbert representability.** Over a Noetherian base, the construction first chooses the uniform regularity twist, forms the coherent-module Grassmannian, takes the universal evaluation cokernel, and imposes the stabilized graded Fitting equations for its flat polynomial stratum. This is a locally closed finite-type scheme. For a flat quotient over a Noetherian test, the flat coherent complex proved above makes its high-twist sections locally free with every base change. Evaluation recovers the kernel by uniform fibre generation and Nakayama. These are the two inverse maps in the written representability proof. They prove the needed universal property on Noetherian tests without importing a proper flat cohomology theorem. We use this finite-type scheme and its universal family. We need neither a projective Hilbert scheme nor its universal property for unrelated arbitrary nonnoetherian families.

For a smooth projective \(Y\to C\times T\), with \(T\) Noetherian, its section scheme is the open graph locus in the union of these fixed-polynomial Hilbert schemes. Here is the openness proof. The universal flat subscheme \(D\subset Y\times_T H\) projects projectively to \(C\times H\). At a parameter point where this projection is an isomorphism, it is quasi-finite at every point of that fibre. The open quasi-finite-locus assertion is the **affine** theorem proved in AG-MO, Zariski's Main Theorem, Theorem 3.1: each such point has an affine neighbourhood finite after localization of integral generators. Cover the fibre, and remove the proper image in \(H\) of its closed complement. The projection is now projective with finite fibres, so finite by the preceding hyperplane argument. Its unit map
\[
\mathcal O_{C\times H}\longrightarrow \pi_*\mathcal O_D
\]
is an isomorphism on that parameter fibre. Remove the proper image of the finite cokernel's support to make it surjective. Both modules are flat over \(H\), the second because \(D/H\) is flat and \(\pi\) is finite. Its finite kernel therefore injects on parameter fibres. It is zero on the selected fibre; Nakayama and removal of its proper support image make it zero near that point. Thus \(\pi\) is an isomorphism on an open parameter neighbourhood. Its inverse gives the universal section. This proves exactly the graph-locus assertion.

**The Picard construction.** The curve's finite-point Hilbert charts and the symmetric quotient construction in AG-HP, Hilbert and Quot schemes, §§5 and 7, can be used before that lesson's Hilbert properness argument. The quotient \(C^d/\mathfrak S_d\) is obtained from invariant rings of invariant affine opens containing the finite orbits. The field is algebraically closed and infinite; deleting one of \(d+1\) distinct rational points gives a finite collection of common affine neighbourhoods for every tuple.

The small finite-generation assertion in this construction has the following elementary proof. If \(B\) is a finitely generated \(k\)-algebra and \(A=B^{\mathfrak S_d}\), the orbit polynomial makes each generator integral over \(A\), so \(B\) is finite over \(A\). Choose finite \(A\)-module generators of \(B\); the expressions for their products with the algebra generators, and the expression for \(1\), involve finitely many coefficients in \(A\). The \(k\)-algebra \(A_0\) of those coefficients is Noetherian. Their \(A_0\)-span in \(B\) is stable under every algebra generator and contains \(1\), so equals \(B\). Hence \(B\) is finite over \(A_0\), and its \(A_0\)-submodule \(A\) is finite. Thus \(A\) is finitely generated over \(k\). Invariant functions separate distinct geometric finite orbits by the Chinese remainder theorem followed by an orbit product. The affine finite quotients glue on invariant open subsets, as in the written construction.

This symmetric quotient is proper without using Hilbert projectivity. Its diagonal is an immersion locally on its affine charts. The inverse image of its diagonal's underlying image under the finite surjection \(C^d\times C^d\) is the union of the finitely many permutation graphs, a closed set. A finite surjection is closed and remains so on every base change; therefore the diagonal's image is closed, and its immersion is a closed immersion. The quotient is separated. For a closed subset of the quotient after any base change, its inverse image in the proper \(C^d\) is closed and has the same image in the base, because the finite quotient is surjective. That image is closed. The quotient is therefore universally closed, finite type and separated, hence proper.

The completed-local-ring calculation in the §7 proves smoothness and identifies this quotient with the length-\(d\) Hilbert scheme. Its important all-characteristic details are these: a length-\(a\) deformation at a point is uniquely
\[
R[u]/(u^a+b_1u^{a-1}+\cdots+b_a),\qquad b_i\in\mathfrak m_R
\]
over each local Artinian \(R\); \(1,u,\ldots,u^{a-1}\) is a basis by Nakayama and the rank. Different support points split by lifted idempotents. The symmetric invariant completed ring is a power-series ring in elementary symmetric functions, in every characteristic, using the symmetric-polynomial theorem degree by degree, with no averaging. Completion commutes with the invariant kernel because it is flat, and the finite algebra upstairs splits into its orbit's completed local factors. Thus the sum-divisor map is an isomorphism on the displayed completed local rings.

The completion facts used here are proved in AG-CA, Completion, and the Artin–Rees calculation retained in AG-RG-S02, §1. A Noetherian local ring with this power-series completion is regular; the written smooth-field Jacobian criterion makes the two finite-type schemes smooth over the perfect \(k\). The sum-divisor map has an isomorphism on tangent spaces, hence is étale by the same Jacobian criterion. It is bijective on geometric points by the DVR classification of finite colength ideals. To justify the last step without another imported theorem, the diagonal of an étale map is an open immersion: on affine étale charts its finite diagonal ideal satisfies \(I=I^2\), so is generated by an idempotent, by AG-CA's determinant proof. Geometric injectivity makes this open immersion surjective, hence an isomorphism. Our map is thus a monomorphism and a surjective étale cover. Faithfully flat descent of maps, already proved in the torsor lessons, makes a covering monomorphism an isomorphism. This proves
\[
\operatorname{Hilb}^d_C=\operatorname{Sym}^d C,
\]
and that it is smooth, proper and geometrically irreducible.

We can consequently use the Picard proof with all its consumed bridges specified. The identity
\[
\Gamma(C\times T,\mathcal O)=\Gamma(T,\mathcal O)
\tag{7.4}
\]
comes from tensoring the affine-cover complex of \(C/k\) with a base algebra. Rigidification along \(x\) removes the scalar automorphisms by (7.4). Theorem 2.1's cocycle proof, with the earlier effective module descent, makes rigidified line bundles an actual fppf sheaf. The nonspecial open chart is the just-constructed open of \(\operatorname{Sym}^g C\), using the evaluation Cartier criterion and the finite complex above. Lemma 6.1's written subtraction of \(k\)-rational points supplies enough constant tensor translates to cover every field-valued point. Gluing those represented open charts constructs the smooth separated Picard scheme. Equation (7.2) and the finite complex make its degree pieces open and closed.

For \(d\geq\max(0,2g-1)\), duality (7.3) and evaluation identify the Abel map with a projective bundle of rank \(d+1-g\) over the degree-\(d\) piece, on every test scheme. Its source \(\operatorname{Sym}^d C\) is proper and geometrically irreducible. Surjectivity of this projective bundle, the closed graph, and the proper-image argument in the written Theorem 7.2 prove that its target is proper and geometrically integral. Translation gives these properties in degree zero. Thus
\[
J=\operatorname{Pic}^0_{C/k}
\]
is a smooth proper connected commutative group with its universal rigidified line bundle. The norm construction behind AG-GS, Abelian varieties, Proposition 1.2, proves its projectivity after the two transitive bridges immediately below. This is the exact Jacobian input below, including genuine line bundles on arbitrary bases, rather than only geometric Picard classes.

**Projectivity of the Jacobian.** We give the norm-of-translates construction for the smooth connected \(J\), together with its two line-bundle lemmas. The earlier proof is Group schemes over a field, Theorem 6.2; Quotients and torsors, §G.8A.1, also proves these lemmas.

First, a dense affine open \(W_0\) in a smooth separated integral variety \(X\) has complement supported on an effective Cartier divisor. The local rings are UFDs by the AG-CA Regular local rings, Theorem 5.3, whose finite-free-resolution and Nagata proof is written. The boundary has pure codimension one: if a boundary component had codimension at least two, take a neighbourhood of its generic point missing all the other boundary components. On an affine normal neighbourhood \(V_0\) there, the complement \(W_0\cap V_0\) is affine, as the intersection of two affine opens in a separated scheme. Removing a subset of codimension at least two changes no functions, by the written height-one intersection proof in AG-CA's normal-ring lesson. The inclusion of these two affine schemes would thus induce the identity on their coordinate ring and be an isomorphism, contradicting the chosen boundary point. Therefore the finitely many boundary components are divisors. Their sum is locally principal by factoriality; its local equations differ by units, giving the effective Cartier divisor with precisely that boundary support.

Second, let \(X\) be smooth integral over \(k\), and \(V\subset\mathbb A_k^d\) a nonempty open. Every line bundle on \(X\times V\) has isomorphic restrictions at all \(v\in V(k)\). Choose a rational section to write it as a Cartier divisor, and close its finitely many prime components in \(X\times\mathbb A^d\). This ambient scheme is regular and locally factorial, so their Weil sum is again Cartier: local factorization gives its equations, and their quotients are units on overlaps by the height-one intersection property. This extends the line bundle. On the generic fibre over \(X\), every divisor on \(\mathbb A^d_{k(X)}\) is principal, since its polynomial ring is a UFD. Subtract that rational principal divisor on the product. The remaining prime components are vertical. Locally such a height-one prime in \(A[t_1,\ldots,t_d]\), with \(A\) an integral chart of \(X\), has a nonzero contraction \(\mathfrak p\). A chain of two primes below \(\mathfrak p\) would give a chain of two below the product prime; hence \(\mathfrak p\) has height one. Its extension \(\mathfrak p[t_1,\ldots,t_d]\) has height one and is prime, so equals the product prime. Thus every vertical component is the pullback of a prime divisor on \(X\). Its finite sum is Cartier by local factoriality. The extended line bundle, and hence its restriction to \(X\times V\), is the pullback of a line bundle on \(X\), proving the assertion.

Now apply the norm construction, spelling out its witnesses. Choose a dense affine open in \(J\) and its boundary divisor \(D\) by the first bridge. Choose a nonempty smooth affine coordinate chart \(W\to V\subset\mathbb A^g\) finite étale of degree \(a>0\). Such a chart is obtained from an étale coordinate chart by shrinking the target: at its generic point each of the finitely many algebra generators is algebraic; clear the denominators in their monic equations to make the coordinate algebra finite. For \(g=0\), \(J\) is a point and no construction is needed.

Pull back \(D\) by multiplication \(J\times W\to J\). This map is flat, being a projection after the group shear, so its pullback is Cartier. Norm this divisor along the finite étale map \(J\times W\to J\times V\): on an étale trivialization of that cover multiply the canonical sections and tensor their lines; permutation invariance makes these data descend by the written line-bundle descent. At \(v\in V(k)\) the norm divisor is
\[
E_v=\sum_{w\in W_v}Dw^{-1}.
\]
Its complement is the intersection of the translated affine complements of \(D\), hence is affine. Every \(z\in J(k)\) avoids some \(E_v\). Indeed \(\{w\in W:zw\in D\}\) is proper closed in the irreducible \(W\); its finite image in \(V\) is closed of dimension less than \(g\). Choose a rational \(v\) outside that image. The second bridge says that all the \(\mathcal O(E_v)\) are isomorphic to one line \(A\) on \(J\). Their sections have affine nonvanishing opens covering \(J(k)\), hence covering \(J\), since a nonempty closed subset of this finite-type \(k\)-scheme has a \(k\)-point. Quasi-compactness gives finitely many covering sections \(s_i\).

Here is the last ample-to-projective step explicitly. On the affine \(J_{s_i}\), choose finitely many algebra generators \(a_{ij}\). Each equals \(t_{ij}/s_i^{b_{ij}}\) for a global section \(t_{ij}\) of a power of \(A\). To prove this clearing-of-denominators assertion, take a finite affine trivializing cover of \(A\); local fractions clear after a finite common power of \(s_i\). Their finitely many discrepancies on the quasi-compact overlaps vanish after another common power, so the resulting sections glue. Choose \(e\) at least all the \(b_{ij}\), and take the global sections \(s_i^e\) and \(t_{ij}s_i^{e-b_{ij}}\) of \(A^e\). They define a morphism to a projective space, since the \(s_i^e\) cover. On the affine target chart for \(s_i^e\), its coordinate map includes all the generators \(a_{ij}\), so is surjective on the source chart \(J_{s_i}\). The morphism is a closed immersion into the union of these target charts. Properness of \(J\), and the closed-graph argument, make its image closed in the whole projective space; the immersion is a closed immersion there. This proves projectivity. Thus the group quasi-projectivity citation in the Jacobian step hides no unproved line-bundle input in this particular proof.

For the multiplication argument we use the written cube only on this fixed projective \(J^3\). Its cohomology complexes are covered by the Noetherian flat-projective construction above, so its more general proper-family perfectness input is not required. The remaining field Künneth assertion in its product lemma also has a direct proof: the double affine-cover complex of a product is the tensor product of the two field Čech complexes. Resolve by the two covers in turn; affine intersections make the total complex compute cohomology. Over a field split each complex into its cohomology spaces and contractible pairs. Tensoring preserves the contractions, giving
\[
H^1(X\times Y,\mathcal O)
 =H^1(X,\mathcal O)\otimes H^0(Y,\mathcal O)
 \ \oplus\
 H^0(X,\mathcal O)\otimes H^1(Y,\mathcal O).
\]
When the constants of each factor are \(k\), restriction to their two identity slices is the identity on the respective summand and zero on the other. This is exactly the isomorphism used in AG-GS Lemma 3.3. Its finite-complex proof then makes the fibre-trivial locus of the doubly rigidified product line bundle open and closed, and supplies actual local trivializations. Connectedness and normalization give the written cube identity. The two pullbacks and the integer second-difference recurrence in Theorem 5.1 consequently give \([m]^*A=A^{m^2}\) for symmetric \(A\), with every used cohomology input proved here or earlier.

### 7.3. Removing the unipotent part on an affine curve

Fix a Borel \(B=T\ltimes V\) of \(G\). The positive-root height filtration gives a finite filtration of \(V\) by normal subgroups with successive quotients direct sums of additive root lines. The ordered root coordinates and commutator formulas proving this are in AG-RG-04; vanishing of some commutator constants in bad characteristic does not affect the filtration. Twisting by a \(T\)-torsor replaces these quotients by the corresponding direct sums of line bundles.

An additive vector-bundle torsor on an affine scheme is trivial also in the fppf topology. To see the topology in this assertion, use the torsor itself as an affine faithfully flat trivializing cover, with its tautological section; its affineness is supplied by the earlier effective affine descent. Write the cover as a faithfully flat algebra \(A\to D\). An additive descent cocycle is a degree-one cocycle in the augmented Amitsur complex of the module \(M\). After tensoring with \(D\), that complex is contracted by insertion of the extra trivializing factor; its positive cohomology is zero. Faithful flatness therefore gives zero positive cohomology before tensoring. The cocycle is a coboundary and gives a global section of the torsor. Affine descent supplies the torsor and quotient schemes throughout.

Induction on the finite filtration now makes every torsor under the twisted \(V\) trivial on an affine scheme: its quotient torsor under the last vector quotient has a section, and the inverse image of that section is a torsor under the preceding subgroup. A \(B\)-torsor \(Q_B\) with quotient \(T\)-torsor \(L\) differs from \(L\times^T B\), with this fixed quotient identification, by just such a twisted unipotent torsor. Therefore, for any affine base \(T_0\),
\[
(Q_B\times^B G)|_{U\times T_0}
 \simeq (L\times^T G)|_{U\times T_0}.
\tag{7.5}
\]
Here \(U\) is affine: the proof in this lesson Theorem 5.2 shows that a sufficiently high multiple of \(x\) is very ample by (7.3) and separation of length-two subschemes; its complement is affine. Thus \(U\times T_0\) is indeed affine.

### 7.4. Negative geometric modifications and smooth reductions

We prove the following intermediate assertion: étale locally on any Noetherian base, a given \(G\)-torsor \(P\) is isomorphic on \(U\) to another \(G\)-torsor having a \(B\)-reduction on the whole curve.

First work over an algebraically closed extension \(\Omega/k\). By the corrected §6,
\[
P_{\Omega(C)}\text{ is trivial}.
\]
A generic trivialization gives a generic section of the smooth projective flag bundle \(P/B\). It extends over every local DVR of \(C_\Omega\). For example, in a local projective embedding clear the smallest valuation from its homogeneous coordinates; one coordinate becomes a unit, and the closed equations remain zero. This gives a morphism from that DVR. Its finitely many coordinates and equations extend to a neighbourhood of the point; uniqueness follows from separatedness. These extensions glue with the generic section. We obtain a \(B\)-torsor \(Q_B\) on all of \(C_\Omega\), with quotient \(T\)-torsor \(L\).

Choose an integral strictly antidominant cocharacter \(\lambda\); the negative of the sum of all positive coroots works, since every simple root pairs with that sum by \(2\). Set
\[
D=\max(1,2g-1).
\]
For a large integer \(a\), replace \(L\) by \(L\otimes\lambda(\mathcal O_C(ax))\). If \(L_\chi\) denotes the line associated to a character \(\chi\), its new degree is
\[
\deg L_\chi+a\langle\chi,\lambda\rangle.
\tag{7.6}
\]
Make each simple-root line have degree at most \(-D\). Extend this modified \(T\)-torsor through \(T\subset B\subset G\), obtaining \(Q\) with its tautological \(B\)-reduction. On \(U\), the twist has its canonical trivialization, so (7.5) gives an isomorphism
\[
\beta:Q|_U\xrightarrow{\sim}P|_U.
\tag{7.7}
\]

Call a \(B\)-reduction **negative** if its simple-root lines have degree at most \(-D\). For any such reduction, the bundle
\[
E=\sigma^*T_{(Q/B)/(C\times T_0)}
 =Q_B\times^B(\mathfrak g/\mathfrak b)
\tag{7.8}
\]
has a finite filtration with quotients the negative-root lines \(L_{-\gamma}\). This is a \(B\)-stable filtration: order the negative weights by their height; positive-root conjugation only moves them toward larger weights. It follows from the root-coordinate adjoint action; its possible zero coefficients in bad characteristic preserve the same triangular filtration. Every positive root is a nonnegative integral sum of simple roots. Hence every such quotient has degree at least \(D>2g-2\), and (7.3) and the filtration give
\[
H^1(C_{\bar t},E_{\bar t})=0
\quad\text{for every geometric parameter point}.
\tag{7.9}
\]

Over a Noetherian parameter base the graph-locus construction of 7.2 represents reductions by a scheme locally of finite type. The simple-root lines on the universal reduction have locally constant degrees, by the finite complex and (7.2). Thus the negative reductions form an open union of their degree components; denote it \(R^-(Q)\).

The map \(R^-(Q)\to T_0\) is smooth. Here is the full local lifting argument. Work on an affine piece of \(R^-(Q)\). The finite flat Čech complex of the vector bundle (7.8), replaced by the finite projective complex in 7.2, has no positive fibre cohomology: (7.9) treats degree one, and the curve has no higher coherent cohomology. Cancellation makes it a finite locally free module in degree zero near each parameter point. Therefore its positive cohomology remains zero after tensoring with **any** base module, including a square-zero ideal.

For an affine square-zero thickening \(T'\) of \(T\) over \(T_0\), a given section on \(C\times T\) lifts locally on an affine cover of the curve because \(Q/B\to C\times T_0\) is smooth. The difference of two lifts on an intersection is a derivation, hence a section of \(E\otimes I\), where \(I\) is the ideal on the parameter base. Differences form a Čech one-cocycle. The just-proved vanishing makes it a coboundary. Subtract its degree-zero cochain from the local lifts; derivations give precisely these permitted corrections across a square-zero ideal. The corrected lifts agree and glue to a global section.

To certify smoothness of the finite-type reduction scheme, it is enough to apply this argument to its local polynomial conormal thickening. On an affine parameter chart with algebra \(A=P_0/J\) over the Noetherian base, \(P_0/J^2\to A\) is a Noetherian square-zero test. The extended section corresponds to a map into the reduction scheme by its Noetherian Hilbert universal property. It remains in the same affine negative chart because nilpotent thickenings do not change the underlying points. It gives a section \(A\to P_0/J^2\). AG-CA's proved conormal criterion, Theorem 3.1, now gives formal smoothness, and finite presentation gives smoothness. This avoids both an unproved Artinian smoothness criterion and any arbitrary-base Hilbert assumption.

### 7.5. Smooth finite jets handle imperfect separably closed residues

Let \(\ell\) be a separably closed extension of \(k\), possibly imperfect, and let \(P_\ell\) be a torsor on \(C_\ell\). Its restriction to the formal disc at \(x\) has a frame. Indeed \(P_x/\ell\) is a nonempty smooth scheme, hence has an \(\ell\)-point; a smooth affine chart and its étale coordinates prove this assertion as described below. Lift that point successively through \(\ell[t]/(t^a)\). The disc torsor is affine of finite presentation, so compatible points give a point over \(\ell[[t]]\).

Over \(\bar\ell\), construct the negative modification (7.7). After choosing its disc frame and the fixed frame of \(P\), this modification is described by a loop
\[
g\in G(\bar\ell((t))).
\]
The proved split Cartan decomposition gives \(g=k_1t^\mu k_2\), with \(k_i\in G(\bar\ell[[t]])\). Absorb \(k_2\) by changing the new disc frame.

Choose a faithful closed representation \(G\hookrightarrow\operatorname{GL}(W)\), with a weight basis for \(T\). This existence has an elementary affine-group proof: a finite-dimensional Hopf subcomodule of \(k[G]\) containing algebra generators gives a representation; evaluation at the identity expresses each generator as a matrix coefficient, so the coordinate map from \(\operatorname{GL}(W)\) is surjective. Invertibility follows from the antipode. Let its weights be \(w_i\). Choose
\[
q>\max_{i,j}|\langle w_i-w_j,\mu\rangle|.
\tag{7.10}
\]
For **every** \(k\)-algebra \(A\), if \(h\in G(A[[t]])\) is \(1\) modulo \(t^q\), conjugation \(t^{-\mu}ht^\mu\) has an integral matrix: its \((i,j)\)-entry has valuation at least \(q+\langle w_j-w_i,\mu\rangle>0\) off the identity term. The same holds for its inverse. Hence it lies in \(\operatorname{GL}(W)(A[[t]])\). The closed equations of \(G\) vanish after inverting \(t\), and \(A[[t]]\to A((t))\) is injective, so it lies in \(G(A[[t]])\). Consequently
\[
k\,t^\mu G(A[[t]])
\quad\text{depends only on } k\bmod t^q.
\tag{7.11}
\]
This is a statement over arbitrary, even nonreduced rings, not only field-valued points.

The finite-jet scheme
\[
J_q(G)=\operatorname{Res}_{\ell[t]/(t^q)/\ell}G
\]
is affine of finite presentation: write truncated coefficient variables for a finite affine presentation of \(G\). It is smooth. For a square-zero quotient \(A\to A/I\), the corresponding quotient of truncated-polynomial rings has square-zero kernel; formal smoothness of the affine \(G\) lifts every jet. Finite presentation and the conormal criterion give smoothness.

Over the affine coordinate ring of \(J_q(G)\), the universal jet lifts successively to a compatible point \(u\in G(\mathcal O(J_q(G))[[t]])\), by the same affine formal smoothness. Use the loop \(ut^\mu\), the fixed disc frame of \(P\), and Beauville–Laszlo gluing to construct a \(G\)-torsor \(Q_J\) on \(C_\ell\times J_q(G)\), with an isomorphism to \(P_\ell\) on \(U\). These are finite-presentation algebraic torsors, by the proved affine gluing theorem. Different formal lifts give isomorphic torsors preserving the off-point isomorphism, by (7.11); no loop-group representability is required.

The \(\bar\ell\)-point which is the \(q\)-jet of \(k_1\) has fibre isomorphic to the negative \(Q_{\bar\ell}\). Therefore \(R^-(Q_J)\) is nonempty. By 7.4 it is smooth over \(J_q(G)\), which is smooth over \(\ell\); hence it is smooth over \(\ell\).

A nonempty smooth scheme over a separably closed field has a rational point, including when that field is imperfect. Choose a nonempty affine smooth chart, then an étale coordinate map to affine space. Its image is a nonempty open by the written AG-FSE openness proof: Noetherian Chevalley makes the image constructible, flatness lifts generizations, and a constructible generization-stable subset is open. An infinite field has a rational point in this open, since a nonzero polynomial cannot vanish on all tuples. The fibre is a nonempty étale finite-type scheme over \(\ell\); its closed points have finite separable residue fields by AG-CA's proved étale field classification. They are \(\ell\)-points. This proves the assertion.

Apply it to \(R^-(Q_J)\), choosing one finite-type fixed-polynomial chart through the known geometric point. We obtain over \(\ell\) a modification \(Q_\ell\), an off-point isomorphism (7.7), and a negative \(B\)-reduction. This is the promised imperfect-residue bridge. Its only use of §6 was over \(\bar\ell(C)\); it does not extend §6's field hypothesis.

### 7.6. Strict-henselian lifting and effective finite descent

Let \(S_0\) be Noetherian affine over \(k\), \(s\in S_0\), and
\[
A=\mathcal O_{S_0,s}^{\mathrm{sh}},\qquad
\ell=A/\mathfrak m_A.
\]
The actual strict-henselization construction expresses \(A\) as the filtered colimit of the rings of pointed affine étale neighbourhoods of \(s\). The field \(\ell\) is separably closed; it can be imperfect.

We will use the following exact form of henselian lifting. If \(W\to\operatorname{Spec}A\) is smooth of finite presentation and \(w\in W(\ell)\), choose its local étale coordinate chart \(W\to\mathbb A_A^d\). Lift the \(d\) coordinates of \(w\) to \(A\). Pull back this chart along the chosen \(A\)-point of affine space. It is an étale \(A\)-scheme with the specified \(\ell\)-point. AG-CA's proved henselian section criterion gives a section through that point, and hence the required point of \(W(A)\). This proof works for nonnoetherian henselian rings too.

Apply it first to \(P_x/A\). The residue torsor has an \(\ell\)-point by 7.5's smooth-point argument, so \(P_x\) has an \(A\)-point. Formal smoothness of the affine disc torsor successively extends it through \(A[t]/(t^a)\); finite presentation and affinity give a frame over \(A[[t]]\). Fix this frame and apply 7.5 over \(\ell\) to its reduction. The resulting modification is given by
\[
u_\ell t^\mu,\qquad u_\ell\in G(\ell[[t]]).
\]

There is a lift \(u_A\in G(A[[t]])\) with its *entire* reduction equal to \(u_\ell\). Its constant term lifts by the henselian argument just given. For \(a\geq2\), the ring map
\[
A[t]/(t^a)\longrightarrow
 A[t]/(t^{a-1})\mathop{\times}_{\ell[t]/(t^{a-1})}\ell[t]/(t^a)
\tag{7.12}
\]
is surjective, with kernel \(\mathfrak m_A t^{a-1}\). Its kernel is square-zero because \(2a-2\geq a\). A previously lifted \((a-1)\)-jet and the specified \(a\)-jet of \(u_\ell\) give a \(G\)-point of the fibre-product ring. Formal smoothness of affine \(G\) lifts it through (7.12). The compatible lifts give the asserted formal point. This step does not assume a coefficient field inside \(A\).

Use \(u_At^\mu\) to glue \(P_A|_U\) to a trivial disc torsor. The fixed-curve patch of this lesson meets the exact Beauville–Laszlo hypotheses over \(A\): the parameter is a nonzerodivisor, and all quotient rings are \(A[t]/(t^a)\). No flatness of completion is asserted. We obtain a finite-presentation \(G\)-torsor \(Q_A\) on \(C_A\), an off-point isomorphism
\[
\beta_A:Q_A|_U\xrightarrow{\sim}P_A|_U,
\]
and special fibre equal to the negative modification \(Q_\ell\).

Before using a reduction parameter scheme, descend \(Q_A\) and \(\beta_A\) to a Noetherian affine pointed étale neighbourhood \(T\to S_0\). Here are the exact descent checks; they also justify the arbitrary-base approximation at the end.

1. A finite-presentation affine torsor over each member of the fixed finite affine cover of \(C\) is given by finitely many generators and equations. Its restrictions, gluing maps and inverse maps, its group action and unit, and the torsor isomorphism
   \[
   Q\times G\xrightarrow{\sim}Q\times_C Q
   \]
   are finite-presentation data. Theorem 4.1 and the finite-cover version in Theorem 4.2 of the limits lesson descend them. Associativity, unit, compatibility and inverse identities are finitely many equalities between finite-presentation maps, so become true at one common stage. The same applies to \(\beta_A\) and its inverse on the affine \(U\).
2. Smoothness is retained by a finite witness, rather than by the limits lesson's external eventual-smoothness paragraph. Cover each of the finitely many affine coordinate algebras of the torsor by finitely many principal standard smooth charts. The proved local standard form gives these charts over \(A\). Their finite presentations, isomorphisms and inverses, the invertible Jacobian minors, and the unit-ideal relations which witness that the principal charts cover all descend. At a sufficiently large common stage the same standard charts prove smoothness. This retains flatness at the Noetherian stage through the written smooth-algebra flatness proof.
3. To retain surjectivity near the selected point of \(T\), let \(E\) be the complement in \(C_T\) of the descended torsor's image. That image is open because the map is smooth: it is flat of finite presentation, and the AG-FSE Chevalley-plus-generization proof just specified applies at this Noetherian stage. Thus \(E\) is closed. Its proper image in \(T\) is closed and misses the selected point, since after the faithful extension to \(\ell\) its curve fibre is a torsor. Remove that image. The descended map is now smooth and surjective. With the retained torsor identity it is an fppf \(G\)-torsor.

All three steps concern finite algebraic data. The infinite formal series \(u_A\) itself is never claimed to descend.

Construct \(R^-(Q_T)\) over this Noetherian \(T\). Its \(\ell\)-point is the negative special-fibre reduction already constructed. 7.4 proves that the parameter morphism is smooth near this point. Pull it back to \(A\) and apply the henselian lifting argument to obtain an \(A\)-point, hence a \(B\)-reduction of \(Q_A\). The universal section on the Noetherian parameter scheme pulls back to this reduction; no Hilbert representability over a nonnoetherian strict henselization is needed. Finally descend this section, or equivalently its finite-presentation \(B\)-torsor with its \(G\)-extension isomorphism, to a later pointed affine étale neighbourhood. The same finite witnesses retain its torsor properties, and the finite identities retain the reduction and \(\beta\).

We have proved the intermediate assertion of 7.4 at every \(s\): on an affine étale neighbourhood of that point, \(P|_U\) is isomorphic to \(Q|_U\) for a \(Q\) with a whole-curve \(B\)-reduction. Their images cover \(S_0\); quasi-compactness permits finitely many of these neighbourhoods.

We also need the initial reduction to a Noetherian base when \(S=\operatorname{Spec}R\) is arbitrary. Finite-presentation descent first gives an affine model of \(P\), its action and its torsor isomorphism over \(C_{R_0}\), with \(R_0\subset R\) a finitely generated \(k\)-subalgebra. The finite standard-smooth witnesses in item 2 can be descended by adjoining their finitely many coefficients and identities to \(R_0\). Hence the model is smooth.

Let \(E_0\subset C_{R_0}\) be its closed nonimage and \(D_0\subset\operatorname{Spec}R_0\) its proper image, with any defining ideal \(I_0\). Formation of these images commutes set-theoretically with any base change in this case: a scheme fibre is empty or remains nonempty after any extension of its residue field. The pullback \(P\) is surjective, so \(E_0\times R\) is empty and \(D_0\times R\) is empty. Thus \(I_0R=R\). The equality \(1=\sum_j a_jb_j\), with \(a_j\in I_0\) and finitely many \(b_j\in R\), is a finite witness. Adjoin those \(b_j\) to the model ring. The pullback of \(D_0\), and consequently of \(E_0\), is now empty already at that Noetherian stage. The model is a smooth surjective torsor. Its base change is the original torsor with its action and identity, not merely an isomorphic collection of geometric fibres.

This proves the precise Noetherian approximation required here with no unproved eventual-flatness or eventual-surjectivity input.

### 7.7. Simply connected rootwise Steinitz splitting

The following lemma is independent of §6, of negative reductions, and of the preceding lifting argument:

> If \(H/k\) is split simply connected semisimple with maximal torus \(T_H\), and \(L\) is a \(T_H\)-torsor on \(C\times S\) for an affine base \(S\), then \(L\times^{T_H}H\) is trivial on \(U\times S\), Zariski locally on \(S\).

The simple coroots \(\alpha_i^\vee\) are a basis of \(X_*(T_H)\). Thus \(L\) is the product of the coroot torsors \(\alpha_i^\vee(M_i)\) of actual line bundles \(M_i\) on \(C\times S\). Remove these factors one at a time. Suppose two torus torsors differ by \(\alpha_i^\vee(M_i)\); their images in \(T_H/\alpha_i^\vee(\mathbb G_m)\) have the prescribed common identification.

Let \(H_i\) be the Levi generated by \(T_H\) and the two root groups for \(\pm\alpha_i\). Its coroot is primitive in \(X_*(T_H)\). The actual matrix classification of AG-RG-03 Theorem 8.1 excludes the \(\operatorname{PGL}_2\) model, whose coroot is twice primitive. Therefore \(H_i\) is a product of an auxiliary split torus with either \(\operatorname{SL}_2\) or \(\operatorname{GL}_2\). In the first case its rank-two associated bundles have their canonical determinant trivializations. In the second they have the prescribed common determinant line: the coroot has determinant one. In both cases all auxiliary line bundles have their prescribed common identification, because the two original torsors coincide after quotienting by the coroot torus.

Theorem 5.2 is an actual proof, valid for arbitrary parameter bases, that a rank-two bundle on the whole curve becomes
\[
\mathcal O_U\oplus\det(E)|_U
\tag{7.13}
\]
Zariski locally on the base. Recall its mechanism: after twisting at \(x\), rank at least two and a dimension count give a section with no geometric zero on the fibre; relative section base change and properness retain that property near the parameter point. Split the resulting line extension on the affine \(U\), and repeat. Its final determinant adjustment treats an \(\operatorname{SL}_2\)-orientation.

Apply (7.13) to both rank-two bundles. Their given determinant identification yields an isomorphism on \(U\). If its determinant is not the prescribed one, compose with the automorphism which multiplies the trivial summand of (7.13) by the correcting unit of \(\Gamma(U\times S,\mathcal O)^*\). The correction is an arbitrary unit on \(U\times S\), and need not come from the parameter base. The resulting isomorphism preserves the determinant identification or the \(\operatorname{SL}_2\)-orientation. Together with the auxiliary torus identifications it is an \(H_i\)-torsor isomorphism. Extend structure group to \(H\). Removing each of the finitely many simple-coroot factors gives the lemma.

If \(G\) itself is simply connected, 7.6 and (7.5) reduce \(P|_U\), étale locally on the base, to such a torus-induced bundle on the whole curve. The lemma then proves (7.1) with an étale cover in every characteristic.

### 7.8. General central isogenies via genuine Jacobian torsors

For general semisimple \(G\), first apply 7.6, and then (7.5), to get a \(T\)-torsor \(L\) on the whole curve whose induced \(G\)-bundle agrees with \(P\) on \(U\), locally on an affine étale parameter cover. Choose a basis \(\chi_1,\ldots,\chi_r\) of \(X^*(T)\), and let \(L_i\) be its corresponding line bundles.

Their degrees are locally constant by 7.2. On a quasi-compact affine parameter base they have finitely many simultaneous degree vectors; partition into the finitely many open-and-closed degree loci. On one such locus write \(d_i=\deg(L_i)\) and replace
\[
L_i\quad\text{by}\quad L_i^0=L_i(-d_i x).
\tag{7.14}
\]
All these lines have degree zero, and their restrictions to \(U\) keep the canonical original identification because \(\mathcal O_C(x)\) is canonically trivial there. In torus language (7.14) is twisting by an integral cocharacter of \(\mathcal O_C(x)\); the character basis has a dual cocharacter basis, so every indicated degree vector is permitted.

Normalize along \(x\):
\[
N_i=x^*L_i^0,\qquad
\widetilde L_i=L_i^0\otimes p_S^*N_i^{-1}.
\tag{7.15}
\]
These are actual degree-zero line bundles with their canonical rigidifications along \(x\). The Picard construction in 7.2 gives a map
\[
f_L:S\longrightarrow J^r
\]
classifying them on the nose, rather than only after sheafifying a collection of classes. The finitely many base lines \(N_i\) can be trivialized Zariski locally on \(S\).

The simply connected torus cover \(T_{\mathrm{sc}}\to T\) has character inclusion of index \(n\). Choose bases and express it by an integral matrix \(M\) with \(|\det M|=n\). Our convention is \(\chi_j\mapsto\sum_i M_{ij}\chi_i\) on source characters; the target line \(L_j\) is therefore \(\bigotimes_i(L_i')^{\otimes M_{ij}}\). Extension of structure group sends the source rigidified lines to their tensor combinations given by \(M\), and is represented on their Jacobian parameters by the corresponding matrix map
\[
\Phi_M:J^r\longrightarrow J^r.
\tag{7.16}
\]
Smith normal form, proved by the Euclidean integral row and column operations, writes \(M\) as unimodular changes of bases followed by a diagonal matrix \(m_1,\ldots,m_r>0\), with \(\prod_i m_i=n\). A unimodular matrix gives an automorphism of \(J^r\), since its inverse again has integral entries. Thus it suffices to know that each \([m_i]:J\to J\) is finite faithfully flat, and is étale when \(m_i\) is invertible.

**Exact multiplication-flatness bridge.** Choose a very ample line \(H\) from 7.2's embedding, and set \(A=H\otimes[-1]^*H\). The product of the two embeddings followed by the Segre embedding makes \(A\) very ample, and inversion exchanges its two factors, so it is symmetric. The written square/cube proof in AG-GS, with the cohomology bridge at the end of 7.2, gives \([m]^*A=A^{m^2}\) for \(m\ne0\). A positive-dimensional projective fibre would contain a curve; the pullback of \(A\) there would be trivial but \(A^{m^2}\) would have positive degree. Thus \([m]\) has finite fibres. It is projective, so 7.2 makes it finite. Its closed image has the same dimension as its source, and \(J\) is irreducible of that dimension, so it is surjective.

We prove flatness directly. At a closed target point let \(R\) be the regular local ring of \(J\), of dimension \(g\), and let \(B\) be the finite \(R\)-algebra obtained from \([m]_*\mathcal O_J\). Each of its local rings at a maximal ideal is the regular local ring of a closed source point, also of dimension \(g\). A regular system of parameters of \(R\) becomes a system of parameters there: its quotient is a localization of the finite-dimensional fibre algebra. The written regular-local and depth proofs in AG-CA make these source rings Cohen–Macaulay, and every system of parameters is regular. Consequently the parameter Koszul complex is exact in positive degree on every such localization of \(B\), hence on \(B\). The same Koszul complex is a free resolution of the residue field over \(R\). We get
\[
\operatorname{Tor}_1^R(R/\mathfrak m_R,B)=0.
\]
Choose a minimal finite free surjection \(R^a\to B\). Its kernel \(K\) is finite, since \(R\) is Noetherian. The Tor vanishing injects \(K/\mathfrak m_RK\) into \((R/\mathfrak m_R)^a\), where its image is zero by the minimal choice. Nakayama gives \(K=0\). Thus \(B\) is free. This proves local freeness at every closed target point. The locally free locus of a finitely presented module is open by its finite matrix presentations; a nonempty complement in the finite-type \(k\)-scheme \(J\) has a closed point. Hence the complement is empty. Finite local freeness and surjectivity give faithful flatness.

If \(m\) is invertible in \(k\), the differential of \([m]\) is \(m\) times the identity at the origin, by the proved tangent group law, and translations give the same assertion everywhere. To certify étaleness directly, choose étale affine-space coordinates at a closed target point. Their composite with \([m]\) has invertible differential on the smooth source of the same dimension. The actual smooth-field Jacobian criterion makes that composite étale near the closed source point. The source and target are then both étale over that coordinate affine space; AG-CA Formally smooth, unramified and étale ring maps, Proposition 7.4, proves that their intervening map is étale. Its étale locus is open by standard presentations and includes every closed point, so it is all of \(J\). In genus zero \(J\) is a point and all these maps are the identity; this case also satisfies all the required conclusions.

It follows that (7.16) is a finite fppf cover of finite presentation, and is étale if \(n\) is invertible. Form its base change
\[
S_1=S\times_{J^r,\ f_L,\ \Phi_M}J^r.
\tag{7.17}
\]
The universal rigidified line bundles on the source \(J^r\) supply a genuine \(T_{\mathrm{sc}}\)-torsor \(L'\) on \(C\times S_1\). Equality of its target map with \(f_L\) gives a unique rigidification-preserving isomorphism between its image lines and the \(\widetilde L_i\). This uses the proved rigidified Picard functor on arbitrary bases. No further Brauer obstruction or purely geometric equality of line classes is being suppressed. After trivializing the pulled-back \(N_i\) on a Zariski cover, (7.15) identifies that image torus torsor with the degree-zero torsor of (7.14).

Apply the independent simply connected torus lemma 7.7 to
\[
L'\times^{T_{\mathrm{sc}}}G_{\mathrm{sc}}.
\]
It is trivial on \(U\), Zariski locally on \(S_1\). Extending structure group along \(G_{\mathrm{sc}}\to G\), using (7.14), and using the original isomorphism from 7.6 proves (7.1). Notice that no surjectivity of \(G_{\mathrm{sc}}(\ell)\to G(\ell)\) is used when \(Z\) is nonsmooth. The possible inseparability is handled by the finite flat Jacobian cover (7.17). If \(n\) is invertible, every non-Zariski parameter cover used here is étale.

### 7.9. One affine cover and arbitrary parameters

For a Noetherian affine \(S_0\), the affine étale neighbourhoods of 7.6 have open images covering \(S_0\). Choose finitely many. On each, partition by the finitely many degree vectors in 7.8; take the finite cover (7.17), which is affine because it is finite over the affine parameter base; then choose finitely many principal affine opens for all the line trivializations and rank-two steps of 7.7. Every such principal open is of finite presentation over its affine base. The finite disjoint union of the resulting affine schemes is affine. Its composite morphism to \(S_0\) is flat of finite presentation and surjective. It is therefore faithfully flat of finite presentation, and it is étale when \(n\) is invertible. The finitely many off-point frames assemble into a frame on this disjoint union.

For an arbitrary affine \(S\), 7.6 constructs a Noetherian model \(S_0\) of the torsor. Apply the preceding result to that model and base change its affine cover and its off-point frame to \(S\). Flatness, finite presentation, surjectivity and, when applicable, étaleness are preserved. This proves the stated all-affine-base theorem. The empty base is covered by its identity.

The mechanism can be recorded without any missing arrows:
\[
\begin{array}{c}
P_{\bar\ell(C)}\text{ trivial by §6}
 \ \Longrightarrow\
\text{whole-curve geometric }B\text{-reduction}\\
\Downarrow\ \text{antidominant twist at }x
\\
\text{negative modification over }\bar\ell
 \ \Longrightarrow\
\text{nonempty smooth reduction scheme over }J_q(G)\\
\Downarrow\ \ell\text{ separably closed, finite-jet argument 7.5}
\\
\text{negative modification and reduction over }\ell
 \ \Longrightarrow\
\text{modification over }A\text{ by (7.12) and gluing}\\
\Downarrow\ \text{Noetherian model, smooth reduction scheme, henselian lift}
\\
\text{whole-curve }B\text{-reduction étale locally, same bundle on }U\\
\Downarrow\ \text{affine root filtration}
\\
\text{whole-curve }T\text{-torsor}\\
\Downarrow\ \text{degree normalization and finite flat }J^r\text{-division}
\\
\text{whole-curve }T_{\mathrm{sc}}\text{-torsor}\\
\Downarrow\ \text{simple-coroot rank-two Steinitz splitting}\\
\text{off-point trivialization.}
\end{array}
\tag{7.18}
\]

**Figure 7.1 — the proof mechanism.** The vertical diagram (7.18) displays the fields, formal local ring, parameter schemes and change of structure group actually used. Its first arrow is §6 plus 7.4; the geometric-to-separably-closed arrow is 7.5 with the exact bound (7.10); the local-ring arrow is (7.12) and 7.6; the affine, Jacobian and coroot arrows are 7.3, 7.8 and 7.7 respectively. Each modification is identified with the original torsor over the same \(U=C-\{x\}\). Thus the diagram describes proved maps and local constructions, rather than asserting descent of a formal loop or of a geometric point. The freely accessible Drinfeld–Simpson article in the references gives the negative-reduction strategy.

## 8. Moving several points

Let \(I\) be a finite nonempty set. An \(R\)-point of \(X^I\) is a collection of sections \(x_i:\operatorname{Spec}R\to X\). Their graphs define a relative effective Cartier divisor

\[
D=\sum_{i\in I}\Gamma_{x_i}\subset X_R.
\]

The Beilinson–Drinfeld Grassmannian \(\operatorname{Gr}_{X^I}\) classifies this collection together with a \(G\)-torsor on \(X_R\) and a trivialization on \(X_R-D\). The sum, rather than only a reduced union, gives a Cartier divisor in arbitrary families; its complement and formal gluing problem do not depend on repeating an identical graph.

**Theorem 8.1 (factorization).** Let \(I=\coprod_{a\in A}I_a\) be a partition. On the open subset of \(X^I\) on which sections from different parts have disjoint graphs, there is a canonical isomorphism

\[
\operatorname{Gr}_{X^I}
\xrightarrow{\sim}
\prod_{a\in A,X^I}\operatorname{Gr}_{X^{I_a}}.
\tag{8.1}
\]

For a surjection \(I\to J\), restriction along the diagonal \(X^J\to X^I\), which repeats the sections in each fibre, gives

\[
\operatorname{Gr}_{X^I}\times_{X^I}X^J
\xrightarrow{\sim}\operatorname{Gr}_{X^J}.
\tag{8.2}
\]

Both isomorphisms commute with further partitions and repetitions.

*Proof.* On the disjoint locus, put \(D_a=\sum_{i\in I_a}\Gamma_{x_i}\). The formal completion along \(D\) is the disjoint union of the completions along the \(D_a\). This can be checked in an affine neighbourhood: the ideals of different \(D_a\) are comaximal, and the Chinese remainder theorem applies to every power, then to the inverse limit. The punctured completion is likewise their disjoint union.

By gluing, a modification trivialized off \(D\) is exactly a disc modification on each of those pieces. Conversely, glue those independent pieces to the common trivial bundle on the complement. This constructs (8.1) and its inverse for every \(R\), including morphisms and base changes.

Along the diagonal of (8.2), the complement of \(D\) is the complement of the distinct graphs indexed by \(J\); extra multiplicities do not alter it. Thus both sides classify the same global bundle with the same off-divisor trivialization. Equivalently the \(f\)-adic and \(f^m\)-adic completion filtrations are cofinal at each repeated graph. This proves (8.2). Every construction uses restriction and the uniquely effective gluing operation. Applying it twice or grouping its pieces gives the same object and morphisms, proving the asserted compatibilities. ∎

For two points, the off-diagonal fibre is

\[
\operatorname{Gr}_{G,x_1}\times\operatorname{Gr}_{G,x_2},
\qquad x_1\ne x_2,
\]

while the diagonal fibre is \(\operatorname{Gr}_{G,x}\). Interchanging the two labels is an actual symmetry of the whole family. In *Fusion and the commutativity constraint* we will transport that symmetry from the disjoint locus to the diagonal using sheaves.

The local Grassmannians in these formulas require no chosen coordinates. A parameter identifies \(\operatorname{Gr}_{G,x}\) with the model \(LG/L^+G\). As \(x\) varies, such identifications are made on the torsor of formal coordinates; one must not infer a canonical global product with a fixed model from these fibre descriptions.

## 9. Exercises with solutions

**Exercise 9.1 (easy).** Identify the geometric points of \(\operatorname{Gr}_{\mathbb G_m}\) and compute the degrees of the corresponding line bundles.

*Solution.* Any Laurent unit is uniquely \(t^m u(t)\), with \(u\in k[[t]]^\times\). Its right coset is therefore determined by \(m\in\mathbb Z\). The local lattice is \(t^mO\), which glues to \(\mathcal O_X(-mx)\), of degree \(-m\). Thus degree also gives a bijection with \(\mathbb Z\), but reverses the coweight sign in our convention. ∎

**Exercise 9.2 (easy).** Parameterize the modifications between \(\mathcal O_X^2\) and \(\mathcal O_X(x)^2\) with either successive quotient of length one.

*Solution.* Both quotients together have total length two. Choosing the first quotient of length one is equivalent to choosing the line \(\mathcal M/\mathcal O_X^2\) inside the two-dimensional skyscraper quotient. Its inverse image is \(\mathcal M\), and the complementary quotient also has length one. These choices form \(\mathbb P^1\). A parameter writes them as \(O^2+t^{-1}\ell\), so the relative position is \((0,-1)\). ∎

**Exercise 9.3 (medium).** Apply Beauville–Laszlo to vector bundles in the polynomial square (1.1), allowing nonnoetherian \(R\).

*Solution.* Set \(A=R[t]\), \(B=R[[t]]\), and \(f=t\). Multiplication by \(t\) shifts coefficients and is injective in both rings, even when \(R\) has nilpotents. Truncation gives \(A/t^nA=B/t^nB=R[t]/(t^n)\). For a finite projective \(A[t^{-1}]\)-module \(P_U\), a finite projective \(B\)-module \(P_D\), and an overlap isomorphism, take the agreeing pairs in (1.2). In the proof of Theorem 1.1, (1.7) localizes to \(P_U\), while (1.5) makes its tensor with \(B\) exact and identifies its kernel with \(P_D\). Calculation (1.6) makes this kernel flat over \(A\). The finite-generation argument applied first to that module and then to the kernel of a finite free surjection makes it finitely presented; the dual-basis argument then makes it finite projective. Conversely a finite projective \(A\)-module has injective \(t\)-action as a direct summand of a finite free module and is recovered by (1.9). Compatible component maps preserve agreeing pairs and are recovered by the same exact sequence, so this is an equivalence of categories. Every step works for nonnoetherian \(R\); it does not require flatness of \(R[t]\to R[[t]]\). ∎

**Exercise 9.4 (medium).** Prove that relative position is independent of the two disc frames, and distinguish the local Hecke stack from the global one.

*Solution.* With two frames a modification is a loop \(g\). New frames replace it by \(h_1gh_2^{-1}\), with \(h_1,h_2\in L^+G\); its double coset is unchanged. Conversely such a change is precisely an isomorphism of framed-locally modifications. This gives (4.1). A global triple also includes the source bundle on all of \(X\), which is not encoded by that double coset. Retaining the source bundle and gluing its open restriction to the replacement disc gives the fibre product (4.2). ∎

**Exercise 9.5 (hard).** Describe both types of geometric fibres of \(\operatorname{Gr}_{X^2}\), and prove their family versions and associativity.

*Solution.* For distinct points the completed divisor is the disjoint union of two discs. Restriction to these discs and gluing back gives the product of their Grassmannians, over every base on the disjoint locus. For coincident sections, the doubled divisor has the same complement as the single graph, and its completion is the same completion by cofinality of the powers; the functor is the single-point Grassmannian. For three or more parts, the same Chinese remainder decomposition is independent of parenthesization. Restriction gives the same collection of local torsors, and effective gluing identifies their global reconstructions uniquely, including isomorphisms. Thus the factorization isomorphisms obey associativity and all diagonal compatibilities. ∎

## References

- A. Beauville and Y. Laszlo, [*Un lemme de descente*](https://math.univ-cotedazur.fr/u/beauvill/pubs/descente.pdf), freely accessible author version, for the algebraic gluing theorem and its vector-bundle corollary.
- The Stacks project contributors, [*The Beauville–Laszlo theorem*](https://stacks.math.columbia.edu/tag/0BNI), particularly Tags 0BP2 and 0BP6, and [*Glueing and the Beauville–Laszlo theorem*](https://stacks.math.columbia.edu/tag/0F9M), particularly Tags 0F9Q and 0F9R, freely accessible comparison readings.
- X. Zhu, [*An introduction to affine Grassmannians and the geometric Satake equivalence*](https://arxiv.org/abs/1603.05593v2), freely accessible lecture notes, §§1.4 and 3.1.
- A. Beilinson and V. Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://www.math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), freely accessible author draft, §§2.12 and 4.5.
- V. Drinfeld and C. Simpson, [*B-structures on G-bundles and local triviality*](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/1995/0002/0006/MRL-1995-0002-0006-a013.pdf), freely accessible original article, Mathematical Research Letters **2** (1995), 823–829, especially Theorem 3 and §6.
- E. Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172v1), freely accessible lecture notes, §3.2 for adelic uniformization and §7.3 for one-point uniformization.

- R. Steinberg, [*Regular elements of semisimple algebraic groups*](https://www.numdam.org/item/PMIHES_1965__25__49_0.pdf), freely accessible original article, §§6–11, for comparison with the cross-section construction in §6.
- A. Borel and T. A. Springer, [*Rationality properties of linear algebraic groups II*](https://www.jstage.jst.go.jp/article/tmj1949/20/4/20_4_443/_pdf), freely accessible original article, §§8.2 and 8.6, for imperfect-field considerations.
- R. Sharifi, [*Group and Galois Cohomology*](https://math.ucla.edu/~sharifi/notes/groupcoh-ch01.html), freely accessible notes, §1.11, for comparison with the projective-module argument in §6.2.

# Local cohomology

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A regular function on a punctured affine space can extend across the missing point even when the punctured space is not affine. These are two different questions. Local cohomology separates them: its first two degrees measure extension of sections, while its higher degrees measure cohomology of the open complement. This lesson builds a calculable version of that distinction and shows how depth and dimension control it.

We assume modules, localization, injective resolutions, associated primes, regular sequences, and the correspondence between modules and quasi-coherent sheaves on affine schemes. The construction of the localization triangle is in [Sheaves of modules and their derived categories, Section 13](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-and-their-derived-categories.html#SH-FND-DC-13). We use that construction and prove its consequences for schemes. The completion facts used near the end are stated explicitly there.

Basic references are [Stacks] for the algebraic and sheaf formulations and [Grothendieck–Laszlo] for the classical theory. Our route starts with the open complement and concrete calculations, then proves the algebraic computation and the general bounds. Rings are commutative and Noetherian unless a statement says otherwise. Complexes have cohomological degrees. The depth and support dimension of the zero module are respectively infinity and minus infinity.

## 1. What removal of a closed set changes

Let \(Z\) be closed in a scheme \(X\). For a sheaf \(\mathcal F\), a section is supported in \(Z\) when its restriction to \(X\setminus Z\) is zero. Write \(\Gamma_Z(X,\mathcal F)\) for these sections and \(H^i_Z(X,\mathcal F)\) for the right derived functors. These are groups of global sections with support; the sheaves obtained by deriving the sheaf-valued support functor are different objects.

**Proposition 1.1 (the two exact sequences).** A short exact sequence of sheaves gives a long exact sequence of cohomology with support in \(Z\). If \(U=X\setminus Z\), there is also a natural long exact sequence

\[
\cdots\longrightarrow H^i_Z(X,\mathcal F)
\longrightarrow H^i(X,\mathcal F)
\longrightarrow H^i(U,\mathcal F|_U)
\longrightarrow H^{i+1}_Z(X,\mathcal F)\longrightarrow\cdots.
\]

**Proof.** Resolve a short exact sequence by a termwise split short exact sequence of injective resolutions. Applying the additive support-section functor leaves it termwise exact, so the cohomology sequence of these complexes gives the first assertion. For the second assertion apply derived global sections to the localization triangle from the prerequisite lesson. Restriction to an open set preserves injectives: it is right adjoint to the exact extension-by-zero functor. Thus derived global sections of the open direct image are precisely the cohomology of \(U\). Taking cohomology of the triangle gives the displayed sequence. \(\square\)

**Proposition 1.2 (excision).** If \(V\subset X\) is open and contains \(Z\), restriction gives

\[
H^i_Z(X,\mathcal F)\cong H^i_Z(V,\mathcal F|_V).
\]

**Proof.** At degree zero a section on \(V\) supported in \(Z\) glues with zero on \(X\setminus Z\). They agree on \(V\setminus Z\), and this is an open cover of \(X\). This identifies the support-section functors. Restrict an injective resolution to \(V\); it is still an injective resolution by the adjunction used above. The degree-zero identification is an identification of the resulting complexes, proving the assertion in every degree. \(\square\)

For \(X=\operatorname{Spec}A\), \(I\subset A\), and an \(A\)-module \(M\), define

\[
\Gamma_I(M)=\{m\in M:I^n m=0\text{ for some }n\geq1\},
\qquad H^i_I(M)=R^i\Gamma_I(M).
\]

An element with support in \(V(I)\) is killed by a power of \(I\): its cyclic module has annihilator whose radical contains \(I\), and finite generation of \(I\) converts that inclusion into a power inclusion. The converse is immediate. This explains the degree-zero connection with the sheaf theory. We will prove the connection in all degrees.

## 2. Fractions remember the missing locus

Choose \(I=(f_1,\ldots,f_r)\). Define the extended Čech complex by

\[
C_I(M)^0=M,\qquad
C_I(M)^q=\bigoplus_{i_1<\cdots<i_q}M_{f_{i_1}\cdots f_{i_q}}quad(1\leq q\leq r).
\]

Its differential is alternating restriction: on an ordered subset \(J=\{j_0<\cdots<j_q\}\), the next component is \(\sum_{a=0}^q(-1)^a s_{J\setminus\{j_a\}}\), localized to that intersection. In degree zero the map is diagonal restriction. The signs make the square of the differential zero because deleting two indices in the two possible orders gives opposite signs. All the sums here are finite, so they can equally be written as products.

For one variable this is just

\[
k[t]\longrightarrow k[t,t^{-1}].
\]

Its kernel is zero, and its cokernel has basis \(t^{-1},t^{-2},\ldots\). Removing the origin creates fractions with poles; local cohomology records their classes modulo regular functions.

For two variables the complex is

\[
k[x,y]\longrightarrow k[x,x^{-1},y]\oplus k[x,y,y^{-1}]
\longrightarrow k[x,x^{-1},y,y^{-1}],
\]

where the last map sends \((a,b)\) to \(b-a\). The intersection of the two singly localized rings inside the last ring is \(k[x,y]\). Thus its cohomology in degrees zero and one is zero. In degree two the quotient has basis \(x^{-a}y^{-b}\), \(a,b\geq1\): every monomial with at least one nonnegative exponent belongs to one of the two images, and the remaining Laurent monomials are linearly independent modulo their sum.

**Theorem 2.1 (the Čech computation).** For every \(A\)-module \(M\),

\[
H^q(C_I(M))\cong H^q_I(M)
\cong H^q_{V(I)}(\operatorname{Spec}A,\widetilde M).
\]

The isomorphisms are natural in \(M\). In particular \(H^q_I(M)=0\) for \(q>r\).

**Proof.** We first show that this complex computes the derived module functor, including when a generator is a zero divisor. The kernel in degree zero is \(\Gamma_I(M)\): localization kills an element exactly when a power of each generator kills it, and then a sufficiently large power of \(I\) kills it.

Let \(J\) be injective. For any ideal \(K\), the submodule \(\Gamma_K(J)\) is injective. Here is the needed argument. By Baer's criterion it suffices to extend a map \(u:\mathfrak b\to\Gamma_K(J)\) from an ideal. Since \(\mathfrak b\) is finite, some \(K^n\) kills its image. Artin–Rees gives an \(m\) with \(\mathfrak b\cap K^m\subset K^n\mathfrak b\). The map on \(\mathfrak b+K^m\) that equals \(u\) on \(\mathfrak b\) and zero on \(K^m\) is well defined. Extend it to \(A\) using injectivity of \(J\). The image of \(1\) is killed by \(K^m\), so the extension takes values in \(\Gamma_K(J)\). This proves the claim.

Next \(J\to J_f\) is surjective for any \(f\in A\). The ideals \(\operatorname{Ann}(f^b)\) stabilize. Given \(e/f^a\), choose \(b\) in that stable range. The map

\[
(f^{a+b})\longrightarrow J,\qquad r f^{a+b}\longmapsto r f^b e
\]

is well defined, because \(\operatorname{Ann}(f^{a+b})=\operatorname{Ann}(f^b)\). Its extension to \(A\) provides \(v\) with \(f^{a+b}v=f^b e\). In \(J_f\), this says \(v=e/f^a\). Consequently the two-term complex \([J\to J_f]\) has only degree-zero cohomology, namely the injective module \(\Gamma_{(f)}(J)\).

The full Čech complex is the tensor product of the flat two-term complexes \([A\to A_{f_i}]\), tensored with \(J\). A bounded complex of flat modules preserves quasi-isomorphisms under tensor product. Replace the first two-term factor applied to \(J\) by its degree-zero cohomology, then repeat. At every step that cohomology is injective by the preceding claim. The final complex is quasi-isomorphic to

\[
\Gamma_{(f_r)}\cdots\Gamma_{(f_1)}(J)=\Gamma_I(J)
\]

in degree zero. Thus the higher Čech cohomology functors vanish on injectives. Localization is exact, so a short exact sequence of modules gives a short exact sequence of Čech complexes. The associated cohomology functors form an effaceable cohomological functor with degree zero \(\Gamma_I\); resolving by injectives identifies it with \(R^q\Gamma_I\). More concretely, the double complex obtained by applying Čech to an injective resolution computes both complexes by taking its cohomology in the two orders. Its Čech direction is bounded, so the comparison converges in every degree.

For the sheaf assertion, the distinguished affine opens \(D(f_i)\) cover \(U=X\setminus V(I)\). Their finite intersections are affine. Quasi-coherent sheaves have no higher cohomology on these intersections, so the ordinary Čech complex of this cover computes \(R\Gamma(U,\widetilde M)\). The localization triangle identifies supported cohomology with the fibre of \(M\to R\Gamma(U,\widetilde M)\). That fibre is exactly the extended complex above, including its degree-zero term. This proves the natural comparison. \(\square\)

*Reference:* [Stacks, [Tag 0955](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-local-cohomology-noetherian), [Tag 0956](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-compute-local-cohomology-noetherian), [Tag 0A6T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-local-cohomology-is-local-cohomology)].

**Corollary 2.2 (the complement formula).** For \(U=\operatorname{Spec}A\setminus V(I)\),

\[
0\longrightarrow H^0_I(M)\longrightarrow M
\longrightarrow\Gamma(U,\widetilde M)
\longrightarrow H^1_I(M)\longrightarrow0,
\]

and \(H^p(U,\widetilde M)\cong H^{p+1}_I(M)\) for \(p\geq1\).

**Proof.** In Proposition 1.1 the affine cohomology groups of \(\widetilde M\) vanish in positive degree. Substitute Theorem 2.1 and read the resulting exact sequence. \(\square\)

This includes arbitrary quasi-coherent sheaves \(\mathcal G\) on \(U\). To see this directly, \(j_*\mathcal G\) is quasi-coherent: on a distinguished open, compute its sections as the kernel of the first map in the finite Čech complex for the cover by \(D(f_i)\); localizing this kernel gives the corresponding kernel on that distinguished open. Hence \(j_*\mathcal G=\widetilde N\) for \(N=\Gamma(U,\mathcal G)\). Its restriction is \(\mathcal G\), and Corollary 2.2 applied to \(N\) gives \(H^0_I(N)=H^1_I(N)=0\). The degree-zero kernel computation also proves the claimed quasi-coherence without a finiteness condition on \(\mathcal G\).

## 3. The polynomial calculation in every dimension

**Proposition 3.1.** Set \(A=k[x_1,\ldots,x_n]\), \(n\geq1\), and \(\mathfrak m=(x_1,\ldots,x_n)\). Then

\[
H^i_{\mathfrak m}(A)=0\quad(i\ne n),\qquad
H^n_{\mathfrak m}(A)=
\bigoplus_{a_1,\ldots,a_n\geq1}k\,x_1^{-a_1}\cdots x_n^{-a_n}.
\]

Multiplication by \(x_i\) decreases \(a_i\) by one, with the result zero if \(a_i=1\).

**Proof.** Over \(k\) the Čech complex is the tensor product of the \(n\) complexes

\[
[k[x_i]\longrightarrow k[x_i,x_i^{-1}]].
\]

Each has only degree-one cohomology, freely spanned by its strictly negative powers. Complexes of vector spaces split into their cohomology plus contractible summands: choose complements of boundaries in cycles and of cycles in each term. Tensoring a contractible summand with another complex stays contractible. The tensor product therefore has only the tensor product of those degree-one groups, in degree \(n\). Its basis and multiplication are exactly as stated. \(\square\)

**Corollary 3.2.** For \(n\geq2\), the punctured affine space \(U=\mathbb A^n_k\setminus\{0\}\) has

\[
\Gamma(U,\mathcal O_U)=k[x_1,\ldots,x_n],\qquad
H^{n-1}(U,\mathcal O_U)\ne0.
\]

It is not affine.

**Proof.** Proposition 3.1 kills both \(H^0_{\mathfrak m}\) and \(H^1_{\mathfrak m}\), giving the assertion about sections. It leaves the nonzero top group, which Corollary 2.2 shifts to degree \(n-1\) on \(U\). An affine scheme has zero higher cohomology for every quasi-coherent sheaf, so this nonzero group rules out affineness. \(\square\)

The inverse-monomial module is not finite: multiplication by every \(x_i\) is surjective, so finite generation would contradict Nakayama after localization at \(\mathfrak m\) (this localization preserves the nonzero module, since it is \(\mathfrak m\)-power torsion). Its elements are nevertheless killed by powers of \(\mathfrak m\). The duality lesson will explain its Artinian property.

## 4. The algebra behind the computation

**Proposition 4.1 (Ext and Koszul descriptions).** There are natural isomorphisms

\[
H^i_I(M)=\varinjlim_n\operatorname{Ext}^i_A(A/I^n,M).
\]

The Čech complex is also the filtered colimit of the cochain Koszul complexes on \(f_1^n,\ldots,f_r^n\), tensored with \(M\). On the component indexed by a subset \(J\), the transition from \(n\) to \(n+1\) is multiplication by \(\prod_{j\in J}f_j\).

**Proof.** In degree zero the first formula is the union of the submodules killed by \(I^n\). Apply it termwise to an injective resolution. Filtered colimits of modules are exact, so they commute with kernels, images and cohomology. This gives the Ext formula.

For the second formula use the tensor product of the complexes \([A\xrightarrow{f_i^n}A]\) in degrees zero and one. The prescribed transition maps commute with their differentials. In a component \(J\), send an element \(m\) at stage \(n\) to \(m/(\prod_{j\in J}f_j)^n\). Its colimit is \(M_{\prod_{j\in J}f_j}\), while the empty component stays \(M\). These identifications convert the Koszul differential into alternating localization. \(\square\)

In each Koszul complex multiplication by \(f_i^n\) is null-homotopic: contraction with the \(i\)-th basis vector gives a homotopy whose commutator with the differential is that multiplication. Thus each class in its cohomology is killed by every \(f_i^n\), and therefore by \(I^{r(n-1)+1}\). Proposition 4.1 shows that every local-cohomology module is \(I\)-power torsion. This fact is useful even though these modules need not be finite.

**Proposition 4.2 (independence and change of rings).** Local cohomology depends only on \(\sqrt I\), commutes with filtered colimits of modules, and satisfies

\[
H^i_I(M)\otimes_A B\cong H^i_{IB}(M\otimes_A B)
\]

for a flat ring map \(A\to B\). If \(N\) is a \(B\)-module, its local cohomology for \(IB\), regarded as an \(A\)-module, is \(H^i_I(N)\), without a flatness hypothesis.

**Proof.** If two finitely generated ideals have the same radical, powers of each are contained in the other. Their torsion functors are then identical on every module, so their derived functors are identical. Localization and finite direct sums commute with filtered colimits, and the colimit functor is exact; apply this to the Čech complex. Flat tensor product is exact and takes that complex to the Čech complex of the images of the generators in \(B\), proving flat base change. For the last assertion the two Čech complexes are already identical after forgetting the \(B\)-module structure, because localization at an element of \(A\) is localization at its image in \(B\). \(\square\)

For complexes the same calculation gives derived base change

\[
R\Gamma_I(K)\otimes_A^{\mathbf L}B
\cong R\Gamma_{IB}(K\otimes_A^{\mathbf L}B).
\]

The finite Čech complex has flat terms; taking a flat resolution of \(K\) therefore proves this formula even when \(B\) is not flat. Ordinary cohomology base change in Proposition 4.2 used flatness to commute tensor product with cohomology.

## 5. Depth is the first obstruction

For finite \(M\) with \(IM\ne M\), let \(\operatorname{depth}_I M\) be the maximal length of an \(M\)-regular sequence in \(I\). A regular sequence acts injectively successively on the quotients, and its final quotient is required to be nonzero. We use the prerequisite facts that this length is finite, that quotienting by a regular element lowers it by one, and that replacing the members of a regular sequence by positive powers preserves regularity.

**Theorem 5.1 (depth detection).** Under these assumptions,

\[
\operatorname{depth}_I M
=\min\{i:\operatorname{Ext}^i_A(A/I,M)\ne0\}
=\min\{i:H^i_I(M)\ne0\}.
\]

Also \(\operatorname{Ext}^i_A(N,M)=0\) for \(i<\operatorname{depth}_I M\) when \(N\) is finite and killed by a power of \(I\).

**Proof.** Put \(t=\operatorname{depth}_I M\). If \(t=0\), every element of \(I\) is a zero divisor on \(M\). The zero divisors form the union of its finitely many associated primes. Prime avoidance puts \(I\) in one associated prime \(\mathfrak p=\operatorname{Ann}(m)\), where \(m\ne0\). Thus \(m\) gives a nonzero map \(A/I\to M\).

If \(t>0\), choose a regular \(f\in I\) and put \(\overline M=M/fM\). Apply \(\operatorname{Ext}_A(A/I,-)\) to

\[
0\longrightarrow M\xrightarrow{f}M\longrightarrow\overline M\longrightarrow0.
\]

Multiplication by \(f\) on these Ext groups is zero: the two module actions agree, and \(f\) kills the first argument \(A/I\). This agreement follows by lifting its zero multiplication map to a projective resolution; that lift is null-homotopic. Hence the long exact sequence gives

\[
0\longrightarrow\operatorname{Ext}^i_A(A/I,M)
\longrightarrow\operatorname{Ext}^i_A(A/I,\overline M)
\longrightarrow\operatorname{Ext}^{i+1}_A(A/I,M)\longrightarrow0.
\]

Induction, together with \(\operatorname{Hom}(A/I,M)=0\), shows vanishing below \(t\) and nonvanishing in degree \(t\). The initial Hom vanishing follows because an \(I\)-annihilated element would be killed by the injective multiplication by \(f\).

The depth for \(I^n\) is also \(t\). Inclusion \(I^n\subset I\) gives one inequality; raising a maximal regular sequence in \(I\) to its \(n\)-th powers gives the other. Thus \(\operatorname{Ext}^i(A/I^n,M)=0\) for \(i<t\). To obtain the asserted vanishing for an arbitrary finite \(I\)-power-torsion module \(N\), choose a presentation

\[
0\longrightarrow N'\longrightarrow(A/I^n)^a\longrightarrow N\longrightarrow0.
\]

The case \(i=0\) follows by embedding Hom into the Hom of the middle term. For \(0<i<t\), the Ext sequence expresses \(\operatorname{Ext}^i(N,M)\) as a quotient of \(\operatorname{Ext}^{i-1}(N',M)\), because \(\operatorname{Ext}^i((A/I^n)^a,M)=0\). Induction on \(i\), simultaneously for all such modules, proves the vanishing.

Proposition 4.1 now gives \(H^i_I(M)=0\) for \(i<t\). For each \(n\), apply Ext to

\[
0\longrightarrow I/I^n\longrightarrow A/I^n\longrightarrow A/I\longrightarrow0.
\]

The preceding vanishing makes \(\operatorname{Ext}^t(A/I,M)\to\operatorname{Ext}^t(A/I^n,M)\) injective; for \(t=0\) injectivity follows directly from left exactness of Hom. These maps are compatible with the direct system. Every nonzero element at stage one therefore survives in its colimit, so \(H^t_I(M)\ne0\). \(\square\)

*Reference:* [Stacks, [Tag 0AVZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-depth)].

**Corollary 5.2 (Hartogs extension).** If \(\operatorname{depth}_I M\geq2\), then

\[
M\xrightarrow{\sim}\Gamma(\operatorname{Spec}A\setminus V(I),\widetilde M).
\]

**Proof.** Theorem 5.1 kills the two outside groups in the five-term sequence of Corollary 2.2. \(\square\)

**Example 5.3 (two components meet too thinly).** Let

\[
S=k[x,y,z,w]_{(x,y,z,w)},\quad
P=(x,y),\quad Q=(z,w),\quad A=S/(P\cap Q).
\]

There is an exact sequence

\[
0\longrightarrow A\longrightarrow S/P\oplus S/Q
\xrightarrow{(a,b)\mapsto a(0)-b(0)} k\longrightarrow0.
\]

Both plane rings are regular local of dimension two. Theorem 5.1 kills their supported cohomology in degrees zero and one; \(k\) is entirely supported at the closed point and has only degree-zero local cohomology. The long exact sequence therefore gives

\[
H^0_{\mathfrak m}(A)=0,\qquad H^1_{\mathfrak m}(A)\cong k.
\]

Consequently \(\dim A=2\) and \(\operatorname{depth}A=1\). Geometrically the punctured spectrum is the disjoint union of the two punctured planes. Each plane has all its functions extending across its origin, so the open sections are \(S/P\oplus S/Q\); the quotient by \(A\) records the two independently chosen constant terms. This is exactly the degree-one defect above.

## 6. Dimension puts an upper boundary on the obstruction

**Theorem 6.1 (Grothendieck vanishing).** If \(M\) is finite, then

\[
H^i_I(M)=0\qquad\text{for }i>\dim\operatorname{Supp}M.
\]

**Proof.** When the support dimension is infinite there is nothing to prove. Otherwise a finite prime filtration of \(M\), and the long exact sequences, reduce the assertion to \(M=A/\mathfrak p\). By the change-of-rings assertion of Proposition 4.2 we may therefore assume that \(A\) is a domain of finite dimension \(d\) and \(M=A\). We prove these domain cases, and hence the finite-module cases, by induction on \(d\).

If \(I=0\), the support functor is the identity and the assertion is immediate. Otherwise choose \(0\ne f\in I\). All supported cohomology of \(A_f\) is zero: its Čech complex has a contracting factor because \(f\) is a unit. Since \(A\) is a domain, there is a short exact sequence

\[
0\longrightarrow A\longrightarrow A_f\longrightarrow A_f/A\longrightarrow0.
\]

The quotient is the filtered colimit of \(A/f^nA\), with transition multiplication by \(f\); the map from stage \(n\) sends \(a\) to \(a/f^n\). The support of each quotient has dimension at most \(d-1\): a prime chain containing \(f\) can be lengthened at the bottom by the zero prime of the domain. By induction and commutation with colimits, \(H^j_I(A_f/A)=0\) for \(j>d-1\). The long exact sequence identifies \(H^i_I(A)\) with \(H^{i-1}_I(A_f/A)\) for \(i\geq1\). It therefore vanishes for \(i>d\). If \(d=0\), a nonzero \(f\) is a unit and the quotient is zero, giving the same argument. \(\square\)

*Reference:* [Stacks, [Tag 0DXC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-cd-dimension)].

We next prove nonvanishing without using local duality. The needed structural input is Cohen's theorem: a complete Noetherian local ring has a coefficient field in equal characteristic, or a map from a complete Cohen discrete valuation ring in mixed characteristic, inducing its residue field [Stacks, [Tag 032A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-cohen-structure-theorem)]. We also use these commutative-algebra prerequisites: completion is faithfully flat and preserves dimension; complete local rings are universally catenary; a nonzero principal ideal in a complete local domain of dimension \(d\) has quotient dimension \(d-1\); and a regular local ring has a regular system of parameters. These facts are independent of local-cohomology nonvanishing.

**Lemma 6.2 (a parameter subring).** A complete local domain \(B\) of dimension \(d\) is a finite torsion-free module over a complete regular local subring \(R\) of dimension \(d\), with \(\sqrt{\mathfrak m_RB}=\mathfrak m_B\).

**Proof.** In equal characteristic choose a coefficient field \(k\) and a system of parameters \(b_1,\ldots,b_d\). Map \(R=k[[t_1,\ldots,t_d]]\) to \(B\) by \(t_i\mapsto b_i\). In mixed characteristic the coefficient ring \(C\) injects into the domain \(B\), since its uniformizer \(p\) maps to a nonzero element. Extend \(p\) to a system of parameters \(p,b_2,\ldots,b_d\), using \(\dim B/pB=d-1\). Map \(R=C[[t_2,\ldots,t_d]]\) to \(B\) by the analogous rule.

In either case \(B/\mathfrak m_RB\) is finite dimensional over the common residue field. Lift a basis to finitely many elements \(v_1,\ldots,v_a\). Every element of \(B\) is an \(R\)-linear combination of these modulo \(\mathfrak m_RB\). Apply that assertion recursively to the remainders: after \(n\) steps it is an \(R\)-linear combination modulo \(\mathfrak m_R^n B\), with successive changes in the coefficients in \(\mathfrak m_R^n\). The coefficients converge in \(R\); the remainders tend to zero in \(B\) because its parameter-ideal and maximal-ideal topologies agree. Thus the \(v_i\) generate \(B\) over \(R\).

The finite map makes \(B\) integral over the image of \(R\), so that image has dimension \(d\). A nonzero kernel in the domain \(R\) would lower its dimension: a chain of primes containing that kernel can be lengthened by \((0)\). Hence the kernel is zero. Since \(B\) is a domain, it is torsion-free over this subring. The radical assertion follows from the choice of parameters. \(\square\)

**Theorem 6.3 (Grothendieck nonvanishing).** For a Noetherian local ring \((A,\mathfrak m)\) of dimension \(d\),

\[
H^d_{\mathfrak m}(A)\ne0.
\]

**Proof.** By flat base change and faithful flatness it suffices to prove the assertion after completion. Choose a minimal prime \(\mathfrak p\) of the completed ring with \(\dim(A/\mathfrak p)=d\), and put \(B=A/\mathfrak p\). Theorem 6.1 applied to \(\mathfrak p\subset A\) kills \(H^{d+1}_{\mathfrak m}(\mathfrak p)\), so the map \(H^d_{\mathfrak m}(A)\to H^d_{\mathfrak m_B}(B)\) is surjective. We may therefore prove nonvanishing for the complete domain \(B\).

Use Lemma 6.2. As a finite torsion-free \(R\)-module, \(B\) embeds in \(R^a\): choose a basis of \(B\otimes_R\operatorname{Frac}(R)\) and multiply its coordinate maps by a common nonzero denominator. The cokernel \(T\) is finite torsion, so its support has dimension at most \(d-1\). The exact sequence

\[
0\longrightarrow B\longrightarrow R^a\longrightarrow T\longrightarrow0
\]

and Theorem 6.1 give a surjection \(H^d_{\mathfrak m_R}(B)\to H^d_{\mathfrak m_R}(R)^a\). The left side equals \(H^d_{\mathfrak m_B}(B)\) by Proposition 4.2 and the radical statement of the lemma.

It remains to check \(H^d_{\mathfrak m_R}(R)\ne0\). If \(d=0\) it is \(R\). Otherwise let \(t_1,\ldots,t_d\) be a regular system of parameters. The Koszul calculation in Proposition 4.1 identifies the top group with

\[
\varinjlim_n R/(t_1^n,\ldots,t_d^n),
\]

where the transition is multiplication by \(t_1\cdots t_d\). These maps are injective. Indeed, regular sequences in a local ring may be permuted, and their powers remain regular. Taking successive colons by \(t_1,\ldots,t_d\) therefore gives

\[
((t_1^{n+1},\ldots,t_d^{n+1}):t_1\cdots t_d)
=(t_1^n,\ldots,t_d^n).
\]

For each single colon, reduce modulo the powers of the other parameters; its remaining parameter is a nonzero divisor, so \((t_i^{n+1}):t_i=(t_i^n)\) in that quotient. This proves the displayed identity. The class of \(1\) at the first stage is nonzero and survives, proving nonvanishing. \(\square\)

*Reference:* [Stacks, [Tag 0DXE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-cd-maximal)].

**Corollary 6.4.** If \(M\ne0\) is a finite Cohen–Macaulay module over a local ring, of dimension \(d\), then its local cohomology supported at the maximal ideal vanishes outside degree \(d\), and is nonzero in degree \(d\).

**Proof.** Depth equals dimension. Theorem 5.1 gives vanishing below \(d\) and nonvanishing at \(d\); Theorem 6.1 gives vanishing above it. \(\square\)

The support condition matters. For example, the regular local ring \(k[x,y]_{(x,y)}\) is Cohen–Macaulay, but local cohomology supported at \((x)\) occurs in degree one, not its dimension two.

## 7. Completion changes coefficients, not supported elements

For a Noetherian local ring, its completion \(\widehat A\) is flat and \(A/\mathfrak m^n=\widehat A/\mathfrak m^n\widehat A\). An \(\mathfrak m\)-power-torsion module \(N\) therefore has a canonical \(\widehat A\)-action: to multiply an element killed by \(\mathfrak m^n\), reduce the coefficient modulo \(\mathfrak m^n\). Independence of \(n\) follows by reducing to a common larger power. Moreover,

\[
N\otimes_A\widehat A\cong N.
\]

To prove this, write \(N\) as the union of \(N[\mathfrak m^n]\). Each submodule has tensor product with \(\widehat A\) equal to itself because the two quotient rings agree, and tensor product commutes with this union. Hence flat base change gives

\[
H^i_{\mathfrak m\widehat A}(M\otimes_A\widehat A)
\cong H^i_{\mathfrak m}(M).
\]

This is an equality after the canonical coefficient extension just described, not an assertion that \(M\) itself is unchanged by completion. The argument applies to all maximal-ideal-power-torsion modules, including infinite ones.

## 8. Exercises and solutions

**Exercise 8.1 (first computations; introductory).** Compute local cohomology of \(k[t]\) supported at \((t)\) and of \(k[x,y]\) supported at \((x,y)\). In the second case compute the effect of multiplication by \(xy\).

**Solution.** In the first case the only nonzero group is \(H^1=k[t,t^{-1}]/k[t]\). In the second it is \(H^2=\bigoplus_{a,b\geq1}k x^{-a}y^{-b}\), by the complexes in Section 2. Multiplication by \(xy\) sends \(x^{-a}y^{-b}\) to \(x^{-(a-1)}y^{-(b-1)}\) when \(a,b>1\), and to zero otherwise. Every basis vector is an image, but the kernel contains all vectors with \(a=1\) or \(b=1\). Surjective multiplication on this infinite module does not imply injective multiplication.

**Exercise 8.2 (extension and affineness; intermediate).** Show that all regular functions on \(\mathbb A^2_k\setminus\{0\}\) extend, although that open set is not affine.

**Solution.** Sections are pairs in \(A_x\oplus A_y\) agreeing in \(A_{xy}\), so they form \(A_x\cap A_y=A\). The intersection equality follows by comparing Laurent monomials: belonging to both rings forces both exponents to be nonnegative. In degree one the open Čech complex has cokernel \(A_{xy}/(A_x+A_y)\), containing the nonzero class \(1/(xy)\). Thus its structure sheaf has nonzero \(H^1\), contradicting affine quasi-coherent vanishing.

**Exercise 8.3 (Hartogs for modules; intermediate).** Let \((A,\mathfrak m)\) be local and \(M\) finite of depth at least two. Prove that every section of \(\widetilde M\) on the punctured spectrum extends uniquely. Explain the roles of the two depth inequalities one and two.

**Solution.** Theorem 5.1 says \(H^0_{\mathfrak m}(M)=H^1_{\mathfrak m}(M)=0\). Corollary 2.2 makes restriction an isomorphism. Vanishing of \(H^0\) alone says a global section cannot disappear on the punctured spectrum, so extension is unique whenever it exists. Vanishing of \(H^1\) says there is no obstruction to existence. The two assertions have different positions in the exact sequence.

**Exercise 8.4 (changing equations; intermediate).** Prove radical independence directly for \(I=(x,y)\) and \(J=(x^2,y^3)\) in an arbitrary Noetherian \(k\)-algebra. Then give the argument for any two ideals with the same radical.

**Solution.** Here \(J\subset I\) and \(I^4\subset J\): every monomial of total degree four has either \(x\)-exponent at least two or \(y\)-exponent at least three. Thus an element killed by a power of one ideal is killed by a power of the other. For general finitely generated ideals of the same radical, a power of each is contained in the other, by taking powers of finitely many generators and the same counting argument. The torsion functors coincide on every module and morphism. Applying them to the same injective resolution proves the equality of their derived functors.

**Exercise 8.5 (a disconnected punctured spectrum; advanced).** For the two-plane local ring in Example 5.3, recover its depth from sections on its punctured spectrum, without using a regular sequence calculation in the quotient ring.

**Solution.** The intersection of the planes consists of the closed point; deleting it separates the spectrum into two nonempty open-and-closed punctured planes. Each plane has sections equal to its local coordinate ring by Corollary 5.2, since it has depth two. Hence the sections on the union are \(S/P\oplus S/Q\). The image of \(A\) is precisely the pairs with equal residues, and its kernel is zero. Its cokernel is \(k\), represented for example by the section that is one on one component and zero on the other. Corollary 2.2 gives \(H^0_{\mathfrak m}(A)=0\) and \(H^1_{\mathfrak m}(A)=k\). Theorem 5.1 gives depth one. A local ring of depth at least two could not have this idempotent section: it would extend to a nontrivial idempotent in a local ring, which is impossible.

## Proof inputs

The written commutative-algebra lessons supply the algebra used throughout this course: [Noetherian and Artinian rings](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-03.html), Theorems 5.1 and 6.1, prove Artin–Rees and Krull intersection; [Associated primes and primary decomposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-04.html), Sections 1–3 and Solution 8.5, prove the zero-divisor, prime-filtration, localization and prime-avoidance assertions; [Regular sequences, depth and Cohen–Macaulay modules](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-12.html), Proposition 1.3 and Sections 2, 5 and 6, supply powers, depth and Cohen–Macaulay localization; [Dimension theory of Noetherian local rings](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-11.html), Theorem 2.1, supplies systems of parameters; and [Completion](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-19.html), Theorems 3.1–3.3 and 4.1, proves exactness, faithful flatness and preservation of local dimension. Baer's criterion has the exact elementary open proof at [Stacks, Tag 0AVF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-characterize-injective-bis).

The sheaf localization triangle is proved in the linked prerequisite. The affine vanishing and affine module–sheaf correspondence are the usual quasi-coherent foundations. From commutative algebra we use Baer's criterion, Artin–Rees, associated primes and prime filtrations, prime avoidance, regular-sequence depth and powers, existence of systems of parameters, and the flatness and dimension properties of completion. We also use Cohen's structure theorem [Stacks, [Tag 032A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-cohen-structure-theorem)], universal catenarity of complete local rings (Cohen's theorem together with [Stacks, [Tag 00NM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-CM-ring-catenary), [Tag 00NQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-regular-ring-CM)]), and the resulting principal-quotient dimension formula. The linked full open proofs of Cohen's theorem and universal catenarity supply these structural inputs; the principal-quotient dimension formula follows from catenary chains. Every local-cohomology calculation and theorem stated above is proved here.

## References

Linked Stacks proofs retain their [GNU Free Documentation License](https://github.com/stacks/stacks-project/blob/master/COPYING). The CC0 dedication covers the exposition here.

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). The tag references use AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the upstream tags. Relevant sections are Local Cohomology, “Generalities” and “Cohomological dimension,” and Dualizing Complexes, “Local cohomology” and “Depth.”
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), especially Exposés I–III. Historical and mathematical reference; this lesson uses its own teaching organization and exposition.

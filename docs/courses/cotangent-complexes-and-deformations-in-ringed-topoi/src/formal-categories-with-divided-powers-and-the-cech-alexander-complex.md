# Formal categories with divided powers and the Čech–Alexander complex

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pair of points of a scheme \(X\) over \(S\) is a point of \(X\times_SX\); composing pairs, \((x,y)\) followed by \((y,z)\) giving \((x,z)\), makes the scheme of pairs a groupoid over \(X\). In algebra this is the cosimplicial ring \(A\to A\otimes_KA\to A\otimes_KA\otimes_KA\to\cdots\), the nerve of a category object of the opposite of the category of \(K\)-algebras. Infinitesimal versions of such categories are obtained by completing along the augmentation ideal, the ideal of the diagonal; with divided powers in place of ordinary powers one obtains the Čech–Alexander complex of \(A/K\), from which crystalline cohomology is computed. This lesson sets up the framework: pro-algebras and formal categories, divided powers on sheaves of ideals, divided powers on the nerve of a formal category, divided power completions, and divided power envelopes, which commute with tensor products of augmented algebras. The key tool is an extension result: divided powers on the augmentation ideal of an augmented algebra extend along any base change, without flatness.

**Prerequisites.** [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md) (internal categories and their nerves, Section 2); [*De Rham complexes and Lie algebroids*](de-rham-complexes-and-lie-algebroids.md) (the conventions on sheaves of modules). From the AI-integrated Stacks project: divided powers [[Stacks, Tag 07GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-definition-divided-powers), [Tag 07GP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-lemma-check-on-generators), [Tag 07GQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-lemma-two-ideals), [Tag 07GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-remark-forgetful), [Tag 07H1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-lemma-gamma-extends), [Tag 07H2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-lemma-kernel), [Tag 07H5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-lemma-divided-power-polynomial-algebra)] and divided power envelopes [[Tag 07H8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/crystalline.html#crystalline-lemma-divided-power-envelope), [Tag 07HA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/crystalline.html#crystalline-equation-divided-power-envelope)].

## Conventions

\(T\) is a topos and \(K\) a sheaf of commutative rings on \(T\). Rings and algebras are commutative with \(1\), sheaves of rings on \(T\) unless stated otherwise, and *\(K\)-algebra* means sheaf of commutative \(K\)-algebras. Local sections, tensor products and quotients are as in [*De Rham complexes and Lie algebroids*](de-rham-complexes-and-lie-algebroids.md). An *augmented \(A\)-algebra* is a \(K\)-algebra \(B\) with \(K\)-algebra maps \(\eta\colon A\to B\) and \(\varepsilon\colon B\to A\) such that \(\varepsilon\eta=\mathrm{id}_A\); its *augmentation ideal* is \(I_B=\ker\varepsilon\). As an \(A\)-module through \(\eta\),
\[
B=\eta(A)\oplus I_B. \tag{0.1}
\]
For augmented \(A\)-algebras \(B\) and \(C\), \(B\otimes_AC\) is formed with \(\eta_B\) and \(\eta_C\) and augmented by \(\varepsilon_B\otimes\varepsilon_C\); \(\iota_1\colon B\to B\otimes_AC\) and \(\iota_2\colon C\to B\otimes_AC\) are the two maps.

## 1. Pro-algebras and formal categories

**Definition 1.1.** Let \(\mathcal C\) be a category. A *pro-object* of \(\mathcal C\) is a functor \(X\colon I\to\mathcal C\) from a small cofiltered category, written \(\text{“}\varprojlim\text{”}\,X_i\). Morphisms are
\[
\begin{aligned}&\operatorname{Hom}(\text{“}\varprojlim\text{”}X_i,\text{“}\varprojlim\text{”}Y_j)\\&\quad=\varprojlim_j\varinjlim_i\operatorname{Hom}(X_i,Y_j),\end{aligned}
\]
with the evident composition; they form the category \(\operatorname{pro}\text{-}\mathcal C\), which contains \(\mathcal C\) as the constant systems. A pro-object is *essentially constant* if it is isomorphic to a constant one. A *pro-\(K\)-algebra* is a pro-object of the category of \(K\)-algebras, a *pro-ideal* of \(\text{“}\varprojlim\text{”}B_i\) is a compatible family of ideals \(J_i\subseteq B_i\) of a level representation, and the quotient is \(\text{“}\varprojlim\text{”}B_i/J_i\).

**Lemma 1.2 (pushouts on levels).** Let \(I\) be a small cofiltered category and \(B_i\leftarrow A_i\to C_i\) a diagram of \(K\)-algebras depending functorially on \(i\in I\). Then \(\text{“}\varprojlim\text{”}(B_i\otimes_{A_i}C_i)\), with the maps induced by the coprojections, is a pushout of \(\text{“}\varprojlim\text{”}B_i\leftarrow\text{“}\varprojlim\text{”}A_i\to\text{“}\varprojlim\text{”}C_i\) in the category of pro-\(K\)-algebras.

**Proof.** Write \(B=\text{“}\varprojlim\text{”}B_i\), and similarly \(A\), \(C\). For a pro-\(K\)-algebra \(Z=\text{“}\varprojlim\text{”}Z_k\) and each \(k\),
\[
\begin{aligned}&\varinjlim_i\operatorname{Hom}(B_i\otimes_{A_i}C_i,Z_k)\\&=\varinjlim_i\bigl(h_{B_i}\times_{h_{A_i}}h_{C_i}\bigr)\\&=h_B\times_{h_A}h_C,\end{aligned}
\]
where \(h_X\) stands for \(\operatorname{Hom}(X,Z_k)\), because filtered colimits of sets commute with fibre products. Taking the limit over \(k\), which commutes with fibre products, gives the universal property. \(\square\)

**Definition 1.3.** A *\(K\)-formal category* is an internal category of the opposite of the category of pro-\(K\)-algebras, in the sense of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md), Section 2, where fibre products of the opposite category are pushouts of pro-algebras. It is *affine* if its objects of objects and of arrows are essentially constant. It is *strict* if it is given by a functor \(i\mapsto C_i\) from a small cofiltered category \(I\) to affine \(K\)-categories with constant objects and arrows, the formal category having the objects \(\text{“}\varprojlim\text{”}A_i\), the arrows \(\text{“}\varprojlim\text{”}P_i\) and the structure maps of the \(C_i\); by Lemma 1.2 the fibre products are formed levelwise, so the axioms hold. Divided power structures are defined below for strict formal categories, levelwise; the envelopes and completions constructed in Section 3 are strict.

**1.4. Affine categories in algebraic terms.** An affine \(K\)-category with objects and arrows given by \(K\)-algebras \(A\) and \(P\) amounts to \(K\)-algebra maps
\[
\begin{aligned}&d^0,d^1\colon A\to P,\quad\varepsilon\colon P\to A,\\&\delta\colon P\to P\otimes_AP.\end{aligned}
\]
Here \(d^0\) and \(d^1\) correspond to the target and the source, \(\varepsilon\) to the identities, and \(\delta\) to the composition. In \(P\otimes_AP\) the first factor is an \(A\)-algebra through \(d^0\) and the second through \(d^1\), matching the fibre product over the target on the first factor and the source on the second. The axioms of an internal category become
\[
\begin{aligned}&\varepsilon d^0=\varepsilon d^1=\mathrm{id}_A,\\ &\delta d^0=\iota_2d^0,\quad\delta d^1=\iota_1d^1,\\ &(\varepsilon\otimes\mathrm{id})\delta=\mathrm{id}=(\mathrm{id}\otimes\varepsilon)\delta,\\ &(\delta\otimes\mathrm{id})\delta=(\mathrm{id}\otimes\delta)\delta.\end{aligned} \tag{1.1}
\]
The second line says that a composite has the target of the second arrow and the source of the first; \(\iota_1,\iota_2\colon P\to P\otimes_AP\) are the two factors. In particular \(P\) is an augmented \(A\)-algebra through \(d^0\) and through \(d^1\), with augmentation \(\varepsilon\) and augmentation ideal \(I=\ker\varepsilon\).

**Example 1.5.** Let \(A\) be a \(K\)-algebra. The *chaotic category* of \(A/K\) has \(P=A\otimes_KA\), \(d^0(a)=1\otimes a\), \(d^1(a)=a\otimes1\), \(\varepsilon(a\otimes b)=ab\) and \(\delta(a\otimes b)=a\otimes1\otimes b\), through \(P\otimes_AP=A\otimes_KA\otimes_KA\). Its points with values in a \(K\)-algebra \(B\) form the category whose objects are the maps \(A\to B\) and with exactly one arrow between any two objects.

**Proposition 1.6 (the nerve).** Let \(C\) be an affine \(K\)-category given by \((A,P,d^0,d^1,\varepsilon,\delta)\). Its nerve is the cosimplicial \(K\)-algebra \(\operatorname{Ner}(C)\) with \(\operatorname{Ner}^0(C)=A\) and \(\operatorname{Ner}^n(C)=P\otimes_A\cdots\otimes_AP\) (\(n\) factors), whose cofaces \(d^i\colon\operatorname{Ner}^{n-1}\to\operatorname{Ner}^n\) and codegeneracies \(s^i\colon\operatorname{Ner}^{n+1}\to\operatorname{Ner}^n\) are, for \(x=x_1\otimes\cdots\otimes x_{n-1}\), resp. \(x=x_1\otimes\cdots\otimes x_{n+1}\),
\[
\begin{aligned}d^0x&=1\otimes x,\\ d^ix&=x_1\otimes\cdots\otimes\delta x_i\otimes\cdots\\&\qquad\quad(0<i<n),\\ d^nx&=x\otimes1,\end{aligned} \tag{1.2}
\]
and \(s^i\), \(0\leq i\leq n\), deletes the factor \(x_{i+1}\) and multiplies a neighbour by \(\varepsilon(x_{i+1})\): in the tensor product \(x_i\,d^0(\varepsilon(x_{i+1}))\otimes x_{i+2}=\) \(x_i\otimes d^1(\varepsilon(x_{i+1}))\,x_{i+2}\), and for \(i=0\) or \(i=n\) only one neighbour exists. In degrees \(0\to1\), \(d^0\) and \(d^1\) are the maps of 1.4, and \(s^0\colon P\to A\) is \(\varepsilon\). The *augmentation* \(\operatorname{Ner}(C)\to A\), induced by the maps \([n]\to[0]\), is \(\varepsilon^{\otimes n}\colon x_1\otimes\cdots\otimes x_n\mapsto\varepsilon(x_1)\cdots\varepsilon(x_n)\), and its kernel, the *augmentation ideal* \(J\), has the components
\[
\begin{aligned}J^n&=\textstyle\sum_{k=1}^nI_k,\\ I_k&=\iota_k(I)\operatorname{Ner}^n(C),\end{aligned} \tag{1.3}
\]
where \(\iota_k\colon P\to\operatorname{Ner}^n(C)\) is the inclusion of the \(k\)-th factor. A strict formal category has the nerve \(\text{“}\varprojlim\text{”}\operatorname{Ner}(C_i)\) and the augmentation ideal \(\text{“}\varprojlim\text{”}J_i\).

**Proof.** The faces of the nerve of an internal category drop the first or the last arrow or compose two consecutive arrows, and its degeneracies insert identities (Section 2 of the lesson on décalage). In the opposite category the fibre products are the tensor products of 1.4, and these operations become (1.2): dropping the first arrow is \(y\mapsto1\otimes y\), composing the arrows \(i\) and \(i+1\) applies \(\delta\) to the \(i\)-th factor, and inserting an identity applies \(\varepsilon\). The augmentation is the composite of codegeneracies, hence the product of the \(\varepsilon(x_k)\).

For (1.3), write \(\operatorname{Ner}^n=\operatorname{Ner}^{n-1}\otimes_AP\), where \(\operatorname{Ner}^{n-1}\) is an augmented \(A\)-algebra through its last factor and \(P\) one through \(d^1\). By (0.1) for both factors,
\[
\begin{aligned}\operatorname{Ner}^n&=A\oplus J^{n-1}\oplus I\\&\quad\oplus(J^{n-1}\otimes_AI),\end{aligned} \tag{1.4}
\]
with the augmentation the projection to \(A\). So \(J^n\) is the sum of the last three terms, which is \(\iota_{\leq n-1}(J^{n-1})\operatorname{Ner}^n+I_n\), and induction gives (1.3). \(\square\)

The decomposition (1.4) uses only one \(A\)-module structure on each factor, the one used in the tensor product. In \(P\otimes_AP\otimes_AP\) the middle factor carries both, and \(P=d^0(A)\oplus I\) is not a decomposition of bimodules unless \(d^0=d^1\); this asymmetry returns in the comparison of the normalized nerve with the tensor algebra of \(I\).

**Example 1.7.** For the chaotic category of Example 1.5, \(\operatorname{Ner}^n=A^{\otimes(n+1)}\) (tensor products over \(K\)), the coface \(d^i\) inserts \(1\) at the place \(i\), and the codegeneracy \(s^i\) multiplies the factors \(i\) and \(i+1\). This is the cosimplicial algebra \(C_{A/K}\); its augmentation ideal in degree \(1\) is the kernel of the multiplication \(A\otimes_KA\to A\), the ideal of the diagonal.

## 2. Divided powers

**Definition 2.1.** Let \(B\) be a sheaf of rings on \(T\) and \(I\subseteq B\) an ideal. A *divided power structure* on \(I\) is a family of maps of sheaves of sets \(\gamma_n\colon I\to I\), \(n\geq1\), satisfying on local sections the axioms of [Tag 07GL]: \(\gamma_1(x)=x\) (with \(\gamma_0(x)=1\)),
\[
\begin{aligned}\gamma_n(x)\gamma_m(x)&=\tbinom{n+m}{n}\gamma_{n+m}(x),\\ \gamma_n(ax)&=a^n\gamma_n(x),\\ \gamma_n(x+y)&=\sum_{i=0}^n\gamma_i(x)\gamma_{n-i}(y),\\ \gamma_n(\gamma_m(x))&=\tfrac{(nm)!}{n!(m!)^n}\gamma_{nm}(x).\end{aligned}
\]
A *PD morphism* \((B,I,\gamma)\to(B',I',\gamma')\) is a ring map \(f\) with \(f(I)\subseteq I'\) and \(f\gamma_n=\gamma'_nf\) on \(I\). An ideal \(I'\subseteq I\) is a *sub-PD-ideal* if \(\gamma_n(I')\subseteq I'\) for \(n\geq1\). The \(n\)-th *divided power* \(I^{[n]}\) is the ideal generated by the products \(\gamma_{a_1}(x_1)\cdots\gamma_{a_r}(x_r)\) with \(a_1+\cdots+a_r\geq n\). A divided power structure on a pro-ideal \(\text{“}\varprojlim\text{”}I_i\) is a family of divided power structures on the \(I_i\) for which the transition maps are PD morphisms.

**2.2. Passing to sheaves.** The results of [Tags 07GP, 07GQ, 07H1, 07H2] for rings hold for sheaves of rings on \(T\), with the same statements read on local sections. Indeed, a divided power structure on a presheaf ideal defines one on the associated sheaf: the \(\gamma_n\) are maps of presheaves of sets and sheafification preserves them, together with the axioms, which are identities between maps built from finite products. Each existence statement is applied to the sections over every object \(U\) of \(T\); its uniqueness statement makes the structures compatible with the restriction maps, and sheafification gives the structure on the sheaf. The uniqueness statements hold sectionwise. We use them in these forms:

1. (generators) If \(I\) is generated by local sections \(x_t\) and \(f\colon B\to B'\) maps \(I\) into a PD ideal \(I'\) with \(f(\gamma_n(x_t))=\gamma'_n(f(x_t))\), then \(f\) is a PD morphism [Tag 07GP].
2. (sums) Divided power structures \(\gamma\) on \(I\) and \(\delta\) on \(I'\) agree on \(II'\); if they agree on \(I\cap I'\), there is a unique divided power structure on \(I+I'\) extending both [Tag 07GQ].
3. (extension) For a ring map \(B\to B'\), \(\gamma\) *extends* to \(B'\) if \(IB'\) has a divided power structure making \(B\to B'\) a PD morphism; it is then unique. It exists if \(B\to B'\) is flat [Tag 07H1]; and for \(B'=B/\mathfrak a\) it exists if and only if \(I\cap\mathfrak a\) is generated by local sections \(y\) with \(\gamma_n(y)\in I\cap\mathfrak a\) for \(n\geq1\) [Tag 07H2].

**Lemma 2.3 (divided powers).** Let \(I\) be an ideal with a divided power structure \(\gamma\).

1. Every \(I^{[n]}\) is a sub-PD-ideal, and a PD morphism maps \(I^{[n]}\) into \(I'^{[n]}\).
2. If \(I=I_1+\cdots+I_m\) with every \(I_k\) a sub-PD-ideal, then
\[
I^{[N]}=\sum_{N_1+\cdots+N_m\geq N}I_1^{[N_1]}\cdots I_m^{[N_m]},
\]
the \(I_k^{[N_k]}\) being taken for the induced structures. In particular \(I^{[m(r-1)+1]}\subseteq I_1^{[r]}+\cdots+I_m^{[r]}\) for every \(r\geq1\).

**Proof.** (1) For a generator \(y=\prod_j\gamma_{a_j}(x_j)\) of \(I^{[n]}\) and \(N\geq1\), \(\gamma_N(y)=\bigl(\prod_{j\geq2}\gamma_{a_j}(x_j)\bigr)^N\gamma_N(\gamma_{a_1}(x_1))\), which is an integer multiple of a product of weight \(N\sum_ja_j\geq n\). For \(by\) and for sums use \(\gamma_N(by)=b^N\gamma_N(y)\) and the sum axiom, every term of which contains some \(\gamma_i(y)\) or \(\gamma_i(y')\) with \(i\geq1\). A PD morphism maps generators to generators.

(2) The right side is contained in the left, a product of generators of the \(I_k^{[N_k]}\) being a generator of \(I^{[N]}\). Conversely, write each \(x_j\) in a generator \(\prod_j\gamma_{a_j}(x_j)\) of \(I^{[N]}\) locally as \(\sum_ky_{jk}\) with \(y_{jk}\in I_k\). The sum axiom gives \(\gamma_{a_j}(x_j)=\sum\prod_k\gamma_{b_{jk}}(y_{jk})\) over the \(b_{jk}\) with \(\sum_kb_{jk}=a_j\), so the generator is a sum of products \(\prod_{j,k}\gamma_{b_{jk}}(y_{jk})\), which lie in \(\prod_kI_k^{[N_k]}\) with \(N_k=\sum_jb_{jk}\) and \(\sum_kN_k=\sum_ja_j\geq N\). If \(N=m(r-1)+1\) and all \(N_k<r\), then \(\sum N_k\leq m(r-1)<N\); so some \(N_k\geq r\), and the term lies in \(I_k^{[r]}\). \(\square\)

**Lemma 2.4 (extension along tensor products).** Let \(B\) and \(C\) be augmented \(A\)-algebras and \(\gamma\) a divided power structure on \(I_B\).

1. \(\gamma\) extends to \(B\otimes_AC\) along \(\iota_1\).
2. If \(I_C\) also has a divided power structure \(\delta\), the augmentation ideal \(I_B\otimes C+B\otimes I_C\) of \(B\otimes_AC\) has a unique divided power structure for which \(\iota_1\) and \(\iota_2\) are PD morphisms.

The augmentations cannot be omitted: Exercise 4.2 gives two divided power structures on rings over \(\mathbf Z\) that are not augmented, for which no structure as in (2) exists.

**Proof.** By 2.2 it suffices to treat rings, that is, the sections over an object of \(T\) with the presheaf tensor product.

(1) Choose a surjection \(A[X]\to C\) from a polynomial ring, with kernel \(\mathfrak b\) (for instance one variable for each element of \(C\)). Then \(B\otimes_AC=B[X]/\mathfrak bB[X]\). The map \(B\to B[X]\) is flat, so \(\gamma\) extends to a divided power structure \(\gamma'\) on \(I_B[X]=I_BB[X]\) (2.2 (3)). By (0.1), \(B[X]=A[X]\oplus I_B[X]\) as \(A[X]\)-modules, so \(\mathfrak bB[X]=\mathfrak b\oplus\mathfrak b\,I_B[X]\), and
\[
\mathfrak bB[X]\cap I_B[X]=\mathfrak b\,I_B[X].
\]
This ideal is generated by the products \(by\) with \(b\in\mathfrak b\) and \(y\in I_B[X]\), and \(\gamma'_n(by)=b^n\gamma'_n(y)\in\mathfrak b\,I_B[X]\) for \(n\geq1\). By 2.2 (3), \(\gamma'\) extends to the quotient \(B\otimes_AC\), and the composite \(B\to B[X]\to B\otimes_AC\) is \(\iota_1\).

(2) By (1) and its symmetric form, the ideals \(I_1=I_B(B\otimes_AC)\) and \(I_2=I_C(B\otimes_AC)\) carry divided power structures extending \(\gamma\) and \(\delta\). Decompose both factors by (0.1):
\[
\begin{aligned}B\otimes_AC&=A\oplus I_B\oplus I_C\\&\quad\oplus(I_B\otimes_AI_C),\end{aligned}
\]
with \(I_1=I_B\oplus(I_B\otimes_AI_C)\) and \(I_2=I_C\oplus(I_B\otimes_AI_C)\). So \(I_1\cap I_2=I_B\otimes_AI_C\), which is the product \(I_1I_2\), generated by the \(\iota_1(x)\iota_2(y)\). The two structures agree on \(I_1I_2\) (2.2 (2)), hence glue to a unique structure on \(I_1+I_2\), the augmentation ideal. Uniqueness: a structure for which \(\iota_1\), \(\iota_2\) are PD morphisms is determined on the generators \(\iota_1(x)\), \(\iota_2(y)\), and the axioms determine it on the ideal they generate. \(\square\)

**Definition 2.5.** A *PD formal category* is a strict \(K\)-formal category \(C\) with a divided power structure on each component \(J^n\) of the augmentation ideal of its nerve, such that all cofaces and codegeneracies are PD morphisms. It is *PD-adic* if the canonical map
\[
\operatorname{Ner}(C)\to\text{“}\varprojlim_n\text{”}\operatorname{Ner}(C)/J^{[n]}
\]
is an isomorphism of cosimplicial pro-algebras, \(J^{[n]}\) denoting the componentwise \(n\)-th divided power.

**Proposition 2.6 (divided powers on the nerve).** Let \(C\) be an affine \(K\)-category given by \((A,P,d^0,d^1,\varepsilon,\delta)\) and \(\gamma\) a divided power structure on \(I=\ker\varepsilon\).

1. For every \(n\geq2\) there is a unique divided power structure on \(J^n\) for which the \(n\) maps \(\iota_k\colon P\to\operatorname{Ner}^n(C)\) are PD morphisms.
2. These structures, with \(\gamma\) on \(J^1=I\), make \(C\) a PD formal category if and only if \(\delta\colon P\to P\otimes_AP\) is a PD morphism.

The same holds for a strict formal category with a divided power structure on the pro-ideal \(I\), levelwise.

**Proof.** (1) Induction on \(n\), with \(\operatorname{Ner}^n=\operatorname{Ner}^{n-1}\otimes_AP\) as in the proof of Proposition 1.6. By induction, \(J^{n-1}\) has a structure for which \(\iota_1,\ldots,\iota_{n-1}\) are PD morphisms. Lemma 2.4 (2), for the augmented \(A\)-algebras \(\operatorname{Ner}^{n-1}\) and \(P\), gives a structure on \(J^n\) for which \(\operatorname{Ner}^{n-1}\to\operatorname{Ner}^n\) and \(\iota_n\) are PD morphisms, hence all the \(\iota_k\). It is unique because \(J^n\) is generated by the \(\iota_k(x)\), \(x\in I\), by (1.3).

(2) If \(C\) is a PD formal category, the coface \(d^1\colon\operatorname{Ner}^1\to\operatorname{Ner}^2\), which is \(\delta\), is a PD morphism. Conversely, let \(\delta\) be one. By 2.2 (1) it suffices to check each coface and codegeneracy on the generators \(\iota_k(x)\), \(x\in I\), of \(J^n\). By (1.2), \(d^0\iota_k=\iota_{k+1}\), \(d^n\iota_k=\iota_k\), and an inner coface \(d^i\) sends \(\iota_k(x)\) to \(\iota_k(x)\) or \(\iota_{k+1}(x)\) when \(k\neq i\), and to the image of \(\delta(x)\) under the PD morphism \(P\otimes_AP\to\operatorname{Ner}^n\) of the factors \(i\), \(i+1\) when \(k=i\). A codegeneracy sends \(\iota_k(x)\) to some \(\iota_{k'}(x)\) or to \(\varepsilon(x)=0\). In each case \(\gamma_m\) is respected, because the \(\iota\)'s and \(\delta\) are PD morphisms and \(\gamma_m(x)\in I\). \(\square\)

**Proposition 2.7 (completion).** Let \(C\) be a PD formal category, given by an affine category with a divided power structure on \(I\) (Proposition 2.6). Then
\[
\text{“}\varprojlim_r\text{”}\operatorname{Ner}(C)/J^{[r]}
\]
is the nerve of the strict formal category with arrows \(\text{“}\varprojlim_r\text{”}P/I^{[r]}\), and this formal category is PD-adic. In particular \(C\) is PD-adic if and only if \(P\to\text{“}\varprojlim_r\text{”}P/I^{[r]}\) is an isomorphism of pro-algebras.

**Proof.** In degree \(m\), Lemma 2.3 (2) for \(J^m=I_1+\cdots+I_m\) (each \(I_k\) is a sub-PD-ideal, generated by elements \(\iota_k(x)\) with \(\gamma_n(\iota_k(x))=\iota_k(\gamma_n(x))\)) gives
\[
\begin{aligned}(J^m)^{[mr]}&\subseteq\textstyle\sum_kI_k^{[r]}\\&\subseteq(J^m)^{[r]},\end{aligned}
\]
and \(I_k^{[r]}\) is generated by \(\iota_k(I^{[r]})\), as \(\iota_k\) is a PD morphism onto a set of generators of \(I_k\). So the systems \(\bigl(\operatorname{Ner}^m/(J^m)^{[r]}\bigr)_r\) and \(\bigl(\operatorname{Ner}^m/\sum_kI_k^{[r]}\bigr)_r\) are isomorphic pro-objects, by the two inclusions. The second is \((P/I^{[r]})\otimes_A\cdots\otimes_A(P/I^{[r]})\), by right exactness of the tensor product. By Lemma 1.2 it is the \(m\)-th term of the nerve of the strict formal category of the affine categories \((A,P/I^{[r]})\); these are affine categories because \(I^{[r]}\) is a sub-PD-ideal (Lemma 2.3 (1)) and \(\delta\), \(\varepsilon\) are PD morphisms, so the structure maps pass to the quotients, which carry the induced divided powers (2.2 (3)). The completed nerve is PD-adic: for \(s\leq r\) the divided powers of \(J/J^{[r]}\) are the images \(J^{[s]}/J^{[r]}\), so its quotient by its \(s\)-th divided power is \(\operatorname{Ner}/J^{[s]}\) for all \(r\geq s\). The last assertion follows, an isomorphism of nerves being one of arrows and conversely. \(\square\)

The pro-algebra \(\text{“}\varprojlim\text{”}P/I^{[r]}\) is represented by the system of \(P_r=P/I^{[r+1]}\) with the ideals \(I_r=I/I^{[r+1]}\), and \(\ker(P_r\to P_s)=I_r^{[s+1]}\) for \(s\leq r\), the divided powers of a quotient by a sub-PD-ideal being the images of those of the ideal.

## 3. Divided power envelopes

**3.1.** Let \(B\) be a sheaf of rings and \(J\subseteq B\) an ideal. Its *divided power envelope* \((D_B(J),\bar J,\bar\gamma)\) is the sheaf associated with the presheaf of envelopes \(U\mapsto D_{B(U)}(J(U))\) of [Tag 07H8], relative to \((\mathbf Z,0)\). The restriction maps come from the universal property, and by 2.2 the associated sheaf carries the divided power structure. It has the universal property for sheaves: a ring map \(B\to B'\) into a sheaf of rings with a divided power ideal \(I'\), sending \(J\) into \(I'\), factors uniquely through a PD morphism \(D_B(J)\to B'\). Indeed the maps on sections are compatible by the universal property over each \(U\), and a map from a presheaf to a sheaf factors uniquely through its sheafification. Moreover [Tag 07HA] gives maps \(B\to D_B(J)\to B/J\) with \(\bar J\) the kernel of the second, and \(\bar J\) is generated by the \(\bar\gamma_n(x)\), \(x\) in the image of \(J\).

**Lemma 3.2.** Let \(B\) be an augmented \(A\)-algebra. Then \(D_B(I_B)\) is an augmented \(A\)-algebra, through \(A\to B\to D_B(I_B)\) and \(D_B(I_B)\to B/I_B=A\), with augmentation ideal \(\bar I_B\).

**Proof.** The composite \(A\to B\to D_B(I_B)\to B/I_B=A\) is the identity, and \(\bar I_B\) is the kernel of the last map (3.1). \(\square\)

**Proposition 3.3 (envelopes of tensor products).** Let \(B\) and \(C\) be augmented \(A\)-algebras. With the structure of Lemma 2.4 (2) on the augmentation ideal of \(D_B(I_B)\otimes_AD_C(I_C)\), the map \(B\otimes_AC\to D_B(I_B)\otimes_AD_C(I_C)\) identifies
\[
\begin{aligned}&D_{B\otimes_AC}(I_B\otimes C+B\otimes I_C)\\&\quad\cong D_B(I_B)\otimes_AD_C(I_C).\end{aligned}
\]

**Proof.** Write \(D_B=D_B(I_B)\) and \(D_C=D_C(I_C)\), augmented \(A\)-algebras by Lemma 3.2, so Lemma 2.4 (2) applies to them. The map \(B\otimes_AC\to D_B\otimes_AD_C\) sends \(I_B\otimes C+B\otimes I_C\) into the augmentation ideal. Let \(f\colon B\otimes_AC\to B'\) be a ring map into a sheaf of rings with a divided power ideal \(I'\), sending \(I_B\otimes C+B\otimes I_C\) into \(I'\). Its restrictions to \(B\) and \(C\) send \(I_B\) and \(I_C\) into \(I'\), so they factor uniquely through PD morphisms \(D_B\to B'\) and \(D_C\to B'\) (3.1). These agree on \(A\), hence define a ring map \(g\colon D_B\otimes_AD_C\to B'\) extending \(f\). It is a PD morphism by 2.2 (1), being one on the generators \(\iota_1(\bar\gamma_n(x))\), \(\iota_2(\bar\gamma_n(y))\) of the augmentation ideal. It is unique: a PD morphism extending \(f\) is determined on \(D_B\) and on \(D_C\) by the universal properties, and these generate \(D_B\otimes_AD_C\). So \(D_B\otimes_AD_C\) has the universal property of the envelope. \(\square\)

**Corollary 3.4 (the envelope of an affine category).** Let \(C\) be an affine \(K\)-category with nerve \(R=\operatorname{Ner}(C)\) and augmentation ideal \(J\), and let \(\bar R^n=D_{R^n}(J^n)\) be the componentwise envelopes, with the induced cofaces and codegeneracies.

1. \(\bar R\) is the nerve of the affine category \(\bar C=(A,D_P(I))\) whose structure maps are induced by those of \(C\), and the divided power structures of the envelopes make \(\bar C\) a PD formal category, with augmentation ideal \(\bar J\).
2. \(\text{“}\varprojlim_r\text{”}\bar R/\bar J^{[r]}\) is the nerve of a PD-adic formal category, the *PD completion* of \(C\).

**Proof.** (1) The cofaces and codegeneracies of \(R\) map \(J\) into \(J\), so they induce PD morphisms of the envelopes, and the cosimplicial identities pass to the envelopes by the uniqueness in their universal properties. The maps \(d^0,d^1\colon A\to P\) and \(\varepsilon\) make \(P\) augmented in two ways; by Lemma 3.2 so is \(D_P(I)\). By Proposition 3.3 and induction, \(\bar R^n=D_P(I)\otimes_A\cdots\otimes_AD_P(I)\), compatibly with the maps \(\iota_k\), and the induced cofaces and codegeneracies are given by (1.2) for the induced maps \(\bar\delta\), \(\bar\varepsilon\). So \(\bar R\) is the nerve of \(\bar C\), whose axioms (1.1) hold because they hold after composing with \(P\to D_P(I)\), and maps out of the envelope are determined there. Since \(\bar\delta\) is a PD morphism and the structures on the \(\bar J^n\) are those of Proposition 2.6 (by uniqueness), \(\bar C\) is a PD formal category. (2) is Proposition 2.7 for \(\bar C\). \(\square\)

**Definition 3.5.** The *Čech–Alexander complex* \(\hat C_{A/K}\) of a \(K\)-algebra \(A\) is the PD completion of the chaotic category of \(A/K\) (Examples 1.5, 1.7): the cosimplicial pro-algebra
\[
\hat C_{A/K}=\text{“}\varprojlim_r\text{”}\bar C_{A/K}/\bar J^{[r]},
\]
where \(\bar C^n_{A/K}\) is the divided power envelope of the ideal of the diagonal in \(A^{\otimes(n+1)}\). For a morphism of schemes \(f\colon X\to S\), \(\hat C_{X/S}=\hat C_{\mathcal O_X/f^{-1}\mathcal O_S}\) on \(X_{\mathrm{Zar}}\).

**Example 3.6.** Let \(A=K[x]\). Then \(P=A\otimes_KA=A[\tau]\) with \(\tau=1\otimes x-x\otimes1\), a polynomial ring over \(A\) through \(d^0\) or \(d^1\), and \(I=\tau P\). The envelope is the divided power polynomial algebra \(D_P(I)=A\langle\tau\rangle\), with \(A\)-basis the \(\tau^{[k]}\), \(k\geq0\) [Tag 07H5]. Since \(\delta(\tau)=\tau\otimes1+1\otimes\tau\) in \(A^{\otimes3}\), the induced comultiplication is
\[
\bar\delta(\tau^{[n]})=\sum_{i+j=n}\tau^{[i]}\otimes\tau^{[j]},
\]
and \(\bar R^n=A\langle\tau_1,\ldots,\tau_n\rangle\) with \(\tau_k=\iota_k(\tau)\). The PD completion replaces \(A\langle\tau\rangle\) by the system of its quotients by the \(\tau^{[\geq r]}\).

## 4. Exercises

**Exercise 4.1.** In Example 3.6, write \(d^0\), \(d^1\colon A\to A\langle\tau\rangle\) explicitly on \(x\), and check (1.1) for \(\bar\delta\) and \(\bar\varepsilon\) on the \(\tau^{[n]}\). Show that \(\bar\delta\) is a PD morphism.

**Exercise 4.2.** By [Tag 07GY], the ideal \(2\mathbf Z/4\mathbf Z\) of \(\mathbf Z/4\mathbf Z\) has divided power structures \(\delta\), \(\delta'\) with \(\delta_2(2)=2\) and \(\delta'_2(2)=0\). Show that in \(\mathbf Z/4\otimes_{\mathbf Z}\mathbf Z/4\) no divided power structure on the ideal generated by \(2\otimes1\) and \(1\otimes2\) makes both coprojections PD morphisms, and explain why Lemma 2.4 does not apply.

**Exercise 4.3.** Let \(P=\mathbf Z\langle s,t\rangle\) be the divided power polynomial algebra in two variables and \(I=I_1+I_2\) its augmentation ideal, with \(I_1\), \(I_2\) generated by the \(s^{[a]}\), resp. \(t^{[b]}\), \(a,b\geq1\). Show that \(I^{[N]}\) is the span of the monomials \(s^{[a]}t^{[b]}\) with \(a+b\geq N\), and that \(I^{[2r-1]}\subseteq I_1^{[r]}+I_2^{[r]}\) while \(I^{[2r-2]}\not\subseteq I_1^{[r]}+I_2^{[r]}\) for \(r\geq2\), so that the bound of Lemma 2.3 (2) is sharp.

## 5. Complete solutions

**Solution 4.1.** In \(P=A\otimes_KA\), \(d^0(x)=1\otimes x=x\otimes1+\tau\) and \(d^1(x)=x\otimes1\); identifying \(P\) with \(A[\tau]\) through \(d^1\), \(d^1(x)=x\) and \(d^0(x)=x+\tau\). The augmentation sends \(\tau\) to \(x-x=0\), so \(\bar\varepsilon(\tau^{[n]})=0\) for \(n\geq1\), and \((\bar\varepsilon\otimes\mathrm{id})\bar\delta(\tau^{[n]})=\tau^{[n]}=(\mathrm{id}\otimes\bar\varepsilon)\bar\delta(\tau^{[n]})\). Coassociativity: both sides send \(\tau^{[n]}\) to the sum of the \(\tau^{[i]}\otimes\tau^{[j]}\otimes\tau^{[k]}\) with \(i+j+k=n\). For the compatibilities with \(d^0\), \(d^1\): \(\delta(d^1x)=\delta(x\otimes1)=\) \(x\otimes1\otimes1=\iota_1(d^1x)\) and \(\delta(d^0x)=1\otimes1\otimes x=\iota_2(d^0x)\). The map \(\bar\delta\) is the PD morphism over \(A\) extending \(\tau\mapsto\tau\otimes1+1\otimes\tau\) given by the universal property of \(A\langle\tau\rangle\) [Tag 07H5]; on the \(\tau^{[n]}\) it is the formula of Example 3.6, by the sum axiom \(\gamma_n(\tau\otimes1+1\otimes\tau)=\sum_{i+j=n}\tau^{[i]}\otimes\tau^{[j]}\).

**Solution 4.2.** In \(\mathbf Z/4\otimes_{\mathbf Z}\mathbf Z/4=\mathbf Z/4\) both \(2\otimes1\) and \(1\otimes2\) are \(2\). A structure \(\epsilon\) making both coprojections PD morphisms would satisfy \(\epsilon_2(2)=\delta_2(2)=2\) and \(\epsilon_2(2)=\delta'_2(2)=0\). Lemma 2.4 needs augmented algebras over the base: there is no ring map \(\mathbf Z/4\to\mathbf Z\), so \(\mathbf Z/4\) is not an augmented \(\mathbf Z\)-algebra, and the decomposition (0.1) behind the proof is not available.

**Solution 4.3.** The monomials \(s^{[a]}t^{[b]}\) form a \(\mathbf Z\)-basis of \(P\), and \(s^{[a]}s^{[c]}=\tbinom{a+c}{a}s^{[a+c]}\). So the ideal generated by the monomials of degree \(\geq N\) is their span. These monomials lie in \(I^{[N]}\): \(s^{[a]}t^{[b]}=\gamma_a(s)\gamma_b(t)\) has weight \(a+b\). Conversely, for a monomial \(m\) of positive degree, \(\gamma_n(m)\) is an integer multiple of a monomial of degree \(n\deg m\): if \(m=s^{[a]}t^{[b]}\) with \(a\geq1\), then \(\gamma_n(m)=(t^{[b]})^n\gamma_n(s^{[a]})\), and \((t^{[b]})^n\) and \(\gamma_n(s^{[a]})\) are integer multiples of \(t^{[nb]}\) and \(s^{[na]}\). By the sum axiom, \(\gamma_n\) of a combination of such monomials is a combination of products \(\prod\gamma_{n_k}(c_km_k)=\prod c_k^{n_k}\gamma_{n_k}(m_k)\) with \(\sum n_k=n\), so a generator \(\prod_j\gamma_{a_j}(x_j)\) of \(I^{[N]}\) is a combination of monomials of degree \(\geq\sum_ja_j\geq N\). The ideal \(I_1^{[r]}+I_2^{[r]}\) is the span of the monomials with \(a\geq r\) or \(b\geq r\). If \(a+b\geq2r-1\) then \(a\geq r\) or \(b\geq r\), which gives the inclusion; the monomial \(s^{[r-1]}t^{[r-1]}\) has degree \(2r-2\) and lies in neither.

## Sources

Formal categories, their divided power structures and completions, and the Čech–Alexander complex are due to Illusie, in his work on the cotangent complex, building on Berthelot's theory of divided powers. Divided power algebras and envelopes for rings are developed in the AI-integrated Stacks project, chapters *Divided Power Algebra* and *Crystalline Cohomology*.

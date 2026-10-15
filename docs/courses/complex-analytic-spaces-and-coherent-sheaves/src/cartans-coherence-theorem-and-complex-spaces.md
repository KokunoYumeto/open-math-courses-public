# Cartan's coherence theorem and complex spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0). The substitution proof in Exercise 4.1 is by GPT-6.1 Sol (OpenAI), Ultra; author self-check, CC0.*

The holomorphic functions on an analytic set are the restrictions of holomorphic functions on the ambient space, modulo those that vanish on the set. For this description to define a good sheaf of rings, the ideal sheaf of the analytic set must be coherent. H. Cartan proved that it always is, including at singular points. This lesson proves Cartan's theorem, defines complex spaces, reduced or not, as spaces locally modelled on such quotients, and shows that their structure sheaves and the familiar operations on coherent sheaves behave as on manifolds. It also proves that the singular points of an analytic set form an analytic subset.

We use [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md) and [Analytic germs, local parametrization and the Nullstellensatz](analytic-germs-local-parametrization-and-the-nullstellensatz.md), whose notation for adapted coordinates, primitive elements and discriminants we keep.

Basic references are [Cartan 1950], [Demailly] and [Lebl SCV].

## 1. The ideal sheaf of an analytic set

Let \(A\) be an analytic subset of a complex manifold \(M\). Its **ideal sheaf** \(\mathcal I_A\subset\mathcal O_M\) is the sheaf of germs of holomorphic functions vanishing on \(A\). Its stalk at \(x\) is \(\mathcal O_{M,x}\) if \(x\notin A\) and the ideal \(I(A,x)\) of the germ of \(A\) if \(x\in A\). The sheaf \(\mathcal O_A=(\mathcal O_M/\mathcal I_A)|_A\) is the sheaf of germs of functions on \(A\) that are locally restrictions of holomorphic functions on \(M\).

**Theorem 1.1 (Cartan).** For every analytic subset \(A\) of a complex manifold \(M\), the ideal sheaf \(\mathcal I_A\) is coherent.

**Proof.** The statement is local; let \(M\) be a neighbourhood of \(0\in\mathbf C^n\) and \(0\in A\).

*Reduction to irreducible germs.* Let \((A,0)=(A_1,0)\cup\cdots\cup(A_N,0)\) be the decomposition into irreducible germs. On a small neighbourhood \(\Omega\), choose analytic sets \(A_k\) representing these germs with \(A\cap\Omega=A_1\cup\cdots\cup A_N\). Then \(\mathcal I_{A\cap\Omega}=\bigcap_k\mathcal I_{A_k}\), and an intersection of coherent subsheaves of \(\mathcal O\) is coherent [Coherent sheaves and Oka's coherence theorem, Theorem 3.1](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves). So we may assume \((A,0)\) irreducible, with prime ideal \(J=I(A,0)\), coordinates \((z',z'')\) adapted to \(J\), degree \(q=[L:K]\) and the notation of the previous lesson.

*Treating the primitive element as a parameter.* For \(c\in\mathbf C^{n-d}\) put \(u_c(z'')=\sum_kc_kz_k\). Let \(\sigma_1,\ldots,\sigma_q\) be the \(K\)-embeddings of \(L\) into an algebraic closure, and define

\[
W(z',T;c)=\prod_{i=1}^q\bigl(T-\sigma_i(\tilde u_c)\bigr),\qquad
\delta(z';c)=\prod_{i<j}\bigl(\sigma_i(\tilde u_c)-\sigma_j(\tilde u_c)\bigr)^2,
\]

\[
B_k(z',T;c)=\sum_{i=1}^q\sigma_i(\tilde z_k)\prod_{l\neq i}\bigl(T-\sigma_l(\tilde u_c)\bigr)\prod_{l\neq i}\bigl(\sigma_i(\tilde u_c)-\sigma_l(\tilde u_c)\bigr)\prod_{\substack{j<l\\ j,l\neq i}}\bigl(\sigma_j(\tilde u_c)-\sigma_l(\tilde u_c)\bigr)^2 .
\tag{1.1}
\]

<span id="why-invariant-coefficients-lie-in-the-base-field"></span>

**Why the invariant coefficients lie in the base field.** Here is the field argument used in the next paragraph. Inside the chosen algebraic closure, adjoin to \(K\) all the roots of the minimal polynomials of the finitely many coordinate classes generating \(L\). The resulting field \(M\) contains \(L\) and is finite over \(K\): each adjoining step has degree at most the degree of a polynomial that its root satisfies. Every \(K\)-embedding of \(M\) sends each of these root sets to itself, and hence sends \(M\) into \(M\); injectivity and finite dimension make it an automorphism. In characteristic zero the embedding-count argument in [Analytic germs, Section 3](../analytic-germs-local-parametrization-and-the-nullstellensatz.html#3-the-finite-extension-and-a-primitive-element) gives exactly \([M:K]\) such automorphisms. If \(a\in M\) is fixed by all of them, put \(E=K(a)\). They are then distinct \(E\)-embeddings of \(M\), of which there are \([M:E]\), by the same characteristic-zero argument. Consequently \([M:K]\leq[M:E]\); the basis-tower identity \([M:K]=[M:E][E:K]\) forces \([E:K]=1\), so \(a\in K\). This applies to every coefficient below, since an automorphism of \(M\) permutes the embeddings of \(L\). No fixed-field theorem is being assumed without proof. For the general finite-extension context, compare the AI Integrated Stacks results on [normal closures](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-normal-closure) and [normal extensions and automorphisms](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-normal-and-automorphisms); the characteristic-zero deduction needed here is the argument just given.

Grouping the factors of \(\delta\) shows \(B_k(z',\sigma_i(\tilde u_c);c)=\delta(z';c)\,\sigma_i(\tilde z_k)\) when the conjugates of \(\tilde u_c\) are distinct; this is Lagrange interpolation multiplied by \(\delta\), written without denominators. Each coefficient of \(W,\delta,B_k\), as polynomials in \(T\) and \(c\), is a polynomial in the conjugates \(\sigma_i(\tilde z_k)\) that is unchanged when the embeddings are permuted. Every automorphism of a normal closure of \(L\) over \(K\) permutes the \(\sigma_i\), so these coefficients lie in \(K\); they are integral over \(\mathcal O_d\), hence lie in \(\mathcal O_d\) by normality. Take \(\sigma_1\) to be the inclusion of \(L\). Evaluating at \(T=\tilde u_c\), every term with \(i\neq1\) contains the factor \(\tilde u_c-\sigma_1(\tilde u_c)=0\), so for every \(c\)

\[
W(\cdot,\tilde u_c;c)=0\qquad\text{and}\qquad B_k(\cdot,\tilde u_c;c)=\delta(\cdot;c)\,\tilde z_k\quad\text{in } L .
\tag{1.2}
\]

When \(u_c\) is primitive, \(W(\cdot,\cdot;c)\) is the minimal polynomial \(W_{u_c}\) and \(\delta(\cdot;c)\neq0\) is its discriminant.

Expand \(W(z',u_c(z'');c)\) and \(\delta(z';c)z_k-B_k(z',u_c(z'');c)\), \(k=d+1,\ldots,n\), as polynomials in \(c\), and let \(G_1,\ldots,G_N\in\mathcal O_d[z'']\) be all their coefficients. By (1.2), for every \(c\) these expressions lie in \(J\); a polynomial in \(c\) with coefficients in the domain \(\mathcal O_n/J\) that vanishes for all \(c\) has zero coefficients, so every \(G_i\in J\). Let \(m=\max\{q,(n-d)(q-1)\}\), expand \(\delta(z';c)^m=\sum_\alpha\delta_\alpha(z')c^\alpha\), and fix a coefficient \(\delta_\alpha\neq0\); one exists because \(\delta(\cdot;c)\neq0\) for primitive \(c\).

Choose a polydisc \(\Delta=\Delta'\times\Delta''\) as in [Analytic germs, Theorem 4.1](analytic-germs-local-parametrization-and-the-nullstellensatz.md#4-the-local-parametrization-theorem), for a fixed primitive \(c_0\), so small that all \(G_i\) and \(\delta_\alpha\) are holomorphic on \(\Delta\) and the \(G_i\) vanish on \(A\cap\Delta\). We claim that for every \(x\in\Delta\),

\[
I(A,x)=\{f\in\mathcal O_x:\ \delta_\alpha f\in(G_{1,x},\ldots,G_{N,x})\},
\tag{1.3}
\]

where \(I(A,x)=\mathcal O_x\) if \(x\notin A\). Granting (1.3), \(\mathcal I_A|_\Delta\) is the image of the coherent sheaf \(\mathcal R(\delta_\alpha,G_1,\ldots,G_N)\subset\mathcal O^{N+1}\) under the projection to the first factor; by Oka's theorem and Theorem 3.1 of [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) it is coherent.

*Proof of "\(\supset\)" in (1.3).* If \(\delta_\alpha f\in(G_{i,x})\), then \(f\) vanishes at the points of \(A\) near \(x\) where \(\delta_\alpha\neq0\). These points are dense in \(A\cap\Delta\) near \(x\): the set \(A_S\) of Theorem 4.1 is dense in \(A\cap\Delta\), the projection \(\pi\) is a local homeomorphism on \(A_S\), and \(\{\delta_\alpha\neq0\}\) is dense in \(\Delta'\). By continuity \(f\) vanishes on \(A\) near \(x\).

*Proof of "\(\subset\)" in (1.3).* Fix \(x\in\Delta\) and let \(F\) be the finite set consisting of \(x\) and the points of \(A\cap\Delta\) above \(x'\) (finite by Theorem 4.1(3)). For \(c\) outside a finite union of proper linear subspaces, \(u_c\) is primitive and takes distinct values at the points of \(F\); fix such a \(c\) and write \(u=u_c\), \(W_u=W(\cdot,\cdot;c)\), \(\delta=\delta(\cdot;c)\), \(B_k=B_k(\cdot,\cdot;c)\), and let \(W_k\) be the minimal polynomial of \(\tilde z_k\). For every \(z'\in\Delta'\), the roots of \(W_u(z',\cdot)\) are exactly the values of \(u\) at the points of \(A\) above \(z'\). Indeed, \(W_u(z',u(z''))\in J\) vanishes on \(A\cap\Delta\), so these values are roots. Conversely, let \(z'\) avoid the zero sets of \(\delta(\cdot;c_0)\) and \(\delta(\cdot;c)\), a dense set. Then the fibre has \(q\) points by Theorem 4.1(1) for \(c_0\), the polynomial \(W_u(z',\cdot)\) has \(q\) distinct roots, and a point \(z\) of the fibre is determined by \(u(z'')\), because \(\delta z_k-B_k(z',u(z''))\in J\) gives \(z_k=B_k(z',u(z''))/\delta(z')\); so the \(q\) values \(u(z'')\) are the \(q\) roots. For general \(z'\), by [the root-multiplicity and limit argument](../analytic-germs-local-parametrization-and-the-nullstellensatz.html#roots-with-multiplicity-and-limits), every root of \(W_u(z',\cdot)\) is a limit of roots at such nearby points, hence of values of \(u\) at points of \(A\) that accumulate, by properness, at points of the fibre above \(z'\). Split \(W_u=W_{u,x}\cdot Q_{u,x}\) at the point \((x',u(x''))\) as in [The local ring of holomorphic germs, Lemma 3.2](the-local-ring-of-holomorphic-germs.md#3-unique-factorization), with \(W_{u,x}\) a Weierstrass polynomial in \(T-u(x'')\) and \(Q_{u,x}(x',u(x''))\neq0\); split each \(W_k=W_{k,x}Q_{k,x}\) at \((x',x_k)\) likewise.

If \(x\notin A\), then \(u(x'')\) is not a root of \(W_u(x',\cdot)\), so \(W_u(z',u(z''))\) is a unit at \(x\), and both sides of (1.3) are \(\mathcal O_x\): indeed \(W_u(z',u(z''))\) is a combination of the \(G_i\) with constant coefficients \(c^\beta\), so \((G_{i,x})=\mathcal O_x\). Let now \(x\in A\). Because \(u\) separates the points of \(F\), for \(z'\) near \(x'\) the roots of \(W_u(z',\cdot)\) near \(u(x'')\), which are the roots of \(W_{u,x}(z',\cdot-u(x''))\), are exactly the values \(u(z'')\) at the points \(z\) of \(A\) above \(z'\) near \(x\). Consequently:

(a) *If \(P\in\mathcal O_{x'}[T]\) satisfies \(P(z',u(z''))=0\) on \(A\) near \(x\), then \(W_{u,x}(z',T-u(x''))\) divides \(P\).* Divide \(P\) by this monic polynomial; the remainder has degree less than \(\deg W_{u,x}\) and vanishes at \(\deg W_{u,x}\) distinct roots for all \(z'\) near \(x'\) outside \(S\), and also outside the zero set of the chosen primitive form's discriminant, so it is zero. The complement of these two zero sets is dense, and each holomorphic remainder coefficient therefore vanishes identically.

(b) Each \(W_{k,x}(z',z_k-x_k)\) vanishes on \(A\) near \(x\), because \(W_k(z',z_k)\in J\) vanishes on \(A\) and \(Q_{k,x}\) does not vanish near \(x\). Applying (a) to \(P(z',T)=\delta^qW_{k,x}\bigl(z',B_k(z',T)/\delta-x_k\bigr)\), which is a polynomial since \(\deg W_{k,x}\leq q\), and which vanishes at \(T=u(z'')\) for \(z\in A\) near \(x\) with \(\delta(z')\neq0\), hence on all of \(A\) near \(x\), shows that \(\delta^qW_{k,x}(z',z_k-x_k)\) lies in the ideal \(G'_x\) of \(\mathcal O_x\) generated by \(W_{u,x}(z',u(z'')-u(x''))\) and the \(\delta z_k-B_k(z',u(z''))\), by the substitution argument in the proof of [Analytic germs, Lemma 3.4](analytic-germs-local-parametrization-and-the-nullstellensatz.md#3-the-finite-extension-and-a-primitive-element).

Now repeat the proof of that lemma at \(x\), with \(W_{u,x}\) and \(W_{k,x}\) in place of \(W_u\) and \(W_k\): every \(f\in\mathcal O_x\) satisfies \(\delta^mf\equiv R(z',u(z''))\) modulo \(G'_x\), with \(R\in\mathcal O_{x'}[T]\) of degree less than \(\deg W_{u,x}\). If \(f\in I(A,x)\), then \(R(z',u(z''))\) vanishes on \(A\) near \(x\), since \(G'_x\subset I(A,x)\); by (a), \(R\) is divisible by a monic polynomial of larger degree, so \(R=0\). Hence \(\delta^mI(A,x)\subset G'_x\). Since \(Q_{u,x}(z',u(z''))\) is a unit at \(x\), \(G'_x\) is generated by \(W_u(z',u(z''))\) and the \(\delta z_k-B_k(z',u(z''))\), which are combinations of the \(G_i\) with coefficients the monomials \(c^\beta\). Therefore

\[
\Bigl(\sum_\alpha\delta_\alpha c^\alpha\Bigr)f\in(G_{1,x},\ldots,G_{N,x})\qquad\text{for every } f\in I(A,x)
\tag{1.4}
\]

and every \(c\) in the dense open set of admissible \(c\). For fixed \(f\), the left side of (1.4), taken modulo \((G_{i,x})\), is a polynomial in \(c\) with coefficients \(\delta_\alpha f\) in the vector space \(\mathcal O_x/(G_{i,x})\), vanishing on a nonempty open set of \(c\). Such a polynomial has zero coefficients: choose finitely many admissible points at which evaluation of polynomials of the given degree is injective, and invert. So \(\delta_\alpha f\in(G_{i,x})\) for every \(\alpha\), proving (1.3). \(\square\)

*Reference:* [Cartan 1950] proves Theorem 1.1; the interpolation in the parameter \(c\) follows [Demailly].

**Corollary 1.2.** \(\mathcal O_A\) is a coherent sheaf of rings on \(A\). A sheaf of \(\mathcal O_A\)-modules is coherent over \(\mathcal O_A\) if and only if its extension by zero to \(M\) is coherent over \(\mathcal O_M\).

**Proof.** \(\mathcal O_M/\mathcal I_A\) is a quotient of coherent sheaves, hence coherent over \(\mathcal O_M\), and it vanishes off \(A\). For the coherent ideal \(\mathcal I_A\), modules over \(\mathcal O_M/\mathcal I_A\) are coherent over it exactly when coherent over \(\mathcal O_M\) [Stacks, Tag 0HCC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-change-rings); in particular \(\mathcal O_M/\mathcal I_A\) is coherent over itself. Restriction to the closed set \(A\) and extension by zero are inverse equivalences between sheaves on \(M\) supported in \(A\) and sheaves on \(A\), compatible with stalks. \(\square\)

## 2. Singular points

**Theorem 2.1.** The singular points of an analytic set \(A\) form an analytic subset \(A_{\mathrm{sing}}\) of \(A\), with empty interior in \(A\).

**Proof.** The statement is local. First let the germ \((A,0)\) be irreducible of dimension \(d\), and let \(g_1,\ldots,g_N\) generate \(\mathcal I_A\) on a neighbourhood \(\Omega\) of \(0\), by Theorem 1.1. If \(x\in A\cap\Omega\) is regular, \(A\) is near \(x\) a submanifold of dimension \(d\) (Theorem 5.4 of the previous lesson), defined by equations \(v_1,\ldots,v_{n-d}\) with independent differentials. These \(v_j\) vanish on \(A\), so they are combinations of the \(g_i\) near \(x\), and therefore some \(n-d\) of the \(g_i\) have independent differentials at \(x\). Conversely, if some \(n-d\) of the \(g_i\) have independent differentials at \(x\in A\), they define near \(x\) a submanifold \(Y\) of dimension \(d\) containing \(A\); then \(A\) is near \(x\) an analytic subset of the connected manifold \(Y\) with nonempty interior (the required dimension \(d\) at \(x\) follows from the dense-regular-locus argument below), hence equal to \(Y\) near \(x\), as in the proof of [Analytic germs, Proposition 5.5](analytic-germs-local-parametrization-and-the-nullstellensatz.md#5-the-nullstellensatz-and-dimension). So \(A_{\mathrm{sing}}\cap\Omega\) is the common zero set on \(A\cap\Omega\) of all \((n-d)\times(n-d)\) minors of the Jacobian matrix of \((g_1,\ldots,g_N)\), an analytic set.

In general let \((A,0)=\bigcup(A_l,0)\) with irreducible \((A_l,0)\). For small representatives, \(A_k\cap A_l\) has empty interior in \(A_k\) and in \(A_l\) when \(k\neq l\), by Proposition 5.5 of the previous lesson. Hence at a point \(y\) of \(A_k\cap A_l\) the germ \((A,y)\) contains the germs \((A_k,y)\not\subset(A_l,y)\) and \((A_l,y)\not\subset(A_k,y)\), neither contained in a third component, so it is reducible; and a germ of a submanifold is irreducible, its local ring being a ring of convergent power series, a domain. So such points are singular. Hence near \(0\), \(A_{\mathrm{sing}}=\bigcup_lA_{l,\mathrm{sing}}\cup\bigcup_{k\neq l}(A_k\cap A_l)\), which is analytic. It has empty interior by Theorem 5.4 and Proposition 5.5 of the previous lesson. \(\square\)

<span id="jacobian-rank-and-dense-regular-points"></span>

**Why the rank test and component union work.** No separate purity assertion about every nearby germ is needed for the rank converse. Choose the representative of an irreducible germ as in [Analytic germs, Theorem 4.1 and Theorem 5.4](../analytic-germs-local-parametrization-and-the-nullstellensatz.html#4-the-local-parametrization-theorem): it contains a dense open complex manifold of dimension \(d\). Around the point \(x\) where the selected equations have rank \(n-d\), the implicit-function theorem gives a connected manifold \(Y\) of dimension \(d\) containing the local part of \(A\). Shrink this neighbourhood within the chosen representative. Density supplies a point \(y\) of its open \(d\)-dimensional locus in this neighbourhood. Near \(y\), inclusion of that locus into \(Y\) has injective differential between tangent spaces of the same dimension. By [the holomorphic inverse-function argument, Lemma 2.2](../../AG-QC/complex-analytic-spaces-and-analytification.html#2-local-analytic-algebra) in manifold charts, the inclusion has open image near \(y\). Thus the analytic subset \(A\) of \(Y\) contains a nonempty open subset of \(Y\). The identity-theorem argument in [Analytic germs, Proposition 5.5](../analytic-germs-local-parametrization-and-the-nullstellensatz.html#5-the-nullstellensatz-and-dimension) makes it all of connected \(Y\). This proves regularity at \(x\), rather than assuming the desired nearby-dimension conclusion. For \(n-d=0\), the determinant of the empty minor is \(1\); the argument uses the ambient neighbourhood as \(Y\) and the rank test gives no singular points.

For the union assertion, first choose finitely many irreducible component representatives and shrink so that each pairwise intersection is closed and has empty interior in either component, by [Analytic germs, Proposition 5.5](../analytic-germs-local-parametrization-and-the-nullstellensatz.html#5-the-nullstellensatz-and-dimension). A finite union of closed sets with empty interior has empty interior: from any nonempty open set remove these closed sets one at a time; the remainder stays nonempty and open. Consequently no germ of a component at one of its points is contained in the union of the other component germs. At a point on at least two components, one component germ and the union of the others are therefore two proper analytic subgerms whose union is the whole germ. The whole germ is reducible and cannot be a manifold germ. This argument does not require each original component germ to remain irreducible at every nearby point. At a point on just one component, its germ is the germ of \(A\), because the other component representatives are closed.

The rank calculation makes each component's singular set analytic and closed. Its empty interior follows from the same dense smooth locus. In any nonempty relatively open subset of \(A\), choose a component it meets, and remove that component's singular set and its finitely many intersections with the others. The preceding finite-union argument leaves a regular point of \(A\). This proves the claimed empty interior for the full singular set, including components of different dimensions. The empty analytic set satisfies the theorem vacuously. The coherent generators used throughout are those of [Theorem 1.1](../cartans-coherence-theorem-and-complex-spaces.html#1-the-ideal-sheaf-of-an-analytic-set); no radical, reducedness or equidimensionality hypothesis is added to the original analytic-subset statement.

## 3. Complex spaces

**Definition 3.1.** A **local model** is a pair \((V,\mathcal O_V)\), where \(V=V(\mathcal J)\) is the zero set of a coherent ideal \(\mathcal J\subset\mathcal O_U\) on an open set \(U\subset\mathbf C^n\) and \(\mathcal O_V=(\mathcal O_U/\mathcal J)|_V\). A **complex space** is a Hausdorff, second countable space \(X\) with a sheaf of local \(\mathbf C\)-algebras \(\mathcal O_X\), locally isomorphic as a locally ringed space to local models. It is **reduced** if all stalks of \(\mathcal O_X\) have no nonzero nilpotents; equivalently, near each point it is isomorphic to a model with \(\mathcal J=\mathcal I_V\). Morphisms of complex spaces are morphisms of locally ringed spaces over \(\mathbf C\).

By the Nullstellensatz [Analytic germs, Theorem 5.1](analytic-germs-local-parametrization-and-the-nullstellensatz.md#5-the-nullstellensatz-and-dimension), the nilpotent germs of \(\mathcal O_U/\mathcal J\) at \(x\) are the classes of germs vanishing on \(V\), so the model is reduced exactly when \(\mathcal J=\mathcal I_V\), and every model has a **reduction** \((V,(\mathcal O_U/\mathcal I_V)|_V)\). For a reduced space, \(\mathcal O_X\) is a sheaf of continuous functions: the value of a section at \(x\) is its image in the residue field \(\mathbf C\), and a section vanishing at every point has a nilpotent germ at every point, hence all its germs are zero and it is zero. This agrees with the description of reduced analytic spaces in [Complex analytic spaces and analytification, Section 1](course:AG-QC/complex-analytic-spaces-and-analytification#1-analytic-equations-and-their-sheaves). A morphism of reduced complex spaces is the same as a continuous map that pulls holomorphic functions back to holomorphic functions.

**Theorem 3.2.** Let \(X\) be a complex space.

1. \(\mathcal O_X\) is a coherent sheaf of rings. Kernels, cokernels, images and extensions of coherent \(\mathcal O_X\)-modules are coherent, and so are their tensor products and internal homomorphisms; supports of coherent modules are analytic subsets of \(X\).
2. If \(Y\subset X\) is an analytic subset, its ideal sheaf in \(\mathcal O_X\) is coherent.
3. If \(i:V\hookrightarrow U\) is a local model, a sheaf \(\mathcal S\) of \(\mathcal O_V\)-modules is coherent if and only if \(i_*\mathcal S\) is a coherent \(\mathcal O_U\)-module, and \(H^q(V,\mathcal S)=H^q(U,i_*\mathcal S)\) for all \(q\).
4. The reduction \(X_{\mathrm{red}}\) is a reduced complex space with the same underlying space, and \(\mathcal O_X\to\mathcal O_{X_{\mathrm{red}}}\) is surjective with coherent locally nilpotent kernel: near each point some fixed power of the kernel vanishes. The exponent may depend on the neighbourhood.

**Proof.** All statements are local, so let \(X=V\) be a model in \(U\). (1) \(\mathcal O_U/\mathcal J\) is coherent over \(\mathcal O_U\) by Oka's theorem, hence coherent over itself by [Stacks, Tag 0HCC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-change-rings), and the remaining statements follow from [Coherent sheaves and Oka's coherence theorem, Proposition 1.2 and Theorem 3.1](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) applied over \(\mathcal O_X\) (the proofs of Theorem 3.1(2)–(3) use only finite presentations and a coherent structure sheaf, and the support of a coherent \(\mathcal O_X\)-module is the support of its pushforward to \(U\)). (2) The ideal of \(Y\) in \(\mathcal O_U/\mathcal J\) is \((\mathcal I_Y+\mathcal J)/\mathcal J\), a quotient of coherent sheaves by Theorem 1.1. (3) The first statement is Tag 0HCC together with extension by zero. For cohomology, \(i\) is the inclusion of a closed subset, \(i_*\) is exact and carries injective sheaves to flasque sheaves, and flasque sheaves are acyclic [Stacks, Tag 09SY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-flasque-acyclic); so an injective resolution of \(\mathcal S\) pushes forward to a flasque resolution (compare [Stacks, Tag 09T0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-flasque-acyclic-pushforward)) of \(i_*\mathcal S\) with the same global sections. (4) The kernel is \(\mathcal I_V/\mathcal J\), coherent by Theorem 1.1 and nilpotent near each point by the Nullstellensatz, since \(\mathcal I_V\) is finitely generated near each point and each generator has a power in \(\mathcal J\). \(\square\)

<span id="closed-model-module-and-cohomology-inputs"></span>

**The closed-model arguments in Theorem 3.2(3).** We spell out the two different comparisons used here: coherence under quotient coefficients, and cohomology under a closed inclusion. Neither comparison requires the model to be reduced.

First work on one space with a sheaf of commutative rings \(\mathcal A\), an ideal sheaf \(\mathcal J\) of finite type, and \(\mathcal B=\mathcal A/\mathcal J\). For any \(\mathcal B\)-module \(\mathcal M\), finite type over \(\mathcal A\) and over \(\mathcal B\) are equivalent: the same sections generate, as may be checked on stalks where \(\mathcal A_x\to\mathcal B_x\) is onto. For finitely many sections of \(\mathcal M\), let \(\mathcal R_{\mathcal A}\) and \(\mathcal R_{\mathcal B}\) be their relation sheaves. The maps from the respective finite free sheaves give an exact sequence
\[
0\longrightarrow\mathcal J^q\longrightarrow\mathcal R_{\mathcal A}
\longrightarrow\mathcal R_{\mathcal B}\longrightarrow0.
\]
Exactness, including surjectivity on the right, follows on stalks: lift the finitely many quotient coefficients of a relation; their action on \(\mathcal M_x\) is unchanged because \(\mathcal J_x\mathcal M_x=0\). If \(\mathcal R_{\mathcal A}\) is of finite type, its quotient is of finite type. Conversely, if \(\mathcal R_{\mathcal B}\) is of finite type, choose finitely many local generators, lift them near a point, and add finitely many generators of \(\mathcal J^q\). After shrinking so these finitely many choices coexist, they generate \(\mathcal R_{\mathcal A}\). Thus the [relation-sheaf definition of coherence](coherent-sheaves-and-okas-theorem.md#1-coherent-modules-on-a-ringed-space) gives
\[
\mathcal M\text{ coherent over }\mathcal A
\quad\Longleftrightarrow\quad
\mathcal M\text{ coherent over }\mathcal B.
\]
This is the quotient-coefficient case of the change-of-rings input cited above, proved without a flatness assumption or a claim about arbitrary changes of rings.

Now put \(\mathcal A=\mathcal O_U\) and let \(i:V\hookrightarrow U\) be the local model. For any sheaf \(\mathcal F\) on the closed subset \(V\), the stalk of \(i_*\mathcal F\) at \(x\in V\) is \(\mathcal F_x\): intersections with ambient open neighbourhoods form a cofinal family of neighbourhoods in the relative topology. At \(x\notin V\) it is zero, since a neighbourhood avoids \(V\). This proves exactness of \(i_*\) by the stalk criterion. The natural map
\[
\mathcal O_U/\mathcal J\longrightarrow i_*\mathcal O_V
\]
is an isomorphism on these same stalks. Outside \(V\), some germ in \(\mathcal J\) has nonzero value and is a unit, so the quotient stalk is zero. At a point of \(V\), restriction has precisely the quotient stalk in the definition of \(\mathcal O_V\).

Under this identification, coherence of \(\mathcal S\) over \(\mathcal O_V\) is equivalent to coherence of \(i_*\mathcal S\) over \(\mathcal B\). To see the neighbourhood issue explicitly, a relative open set is \(V\cap W\) for an ambient open \(W\); its sections of \(\mathcal S\) are the sections of \(i_*\mathcal S\) on \(W\). Finite generators pass between these neighbourhoods, and exactness gives
\[
\ker(\mathcal B^q|_W\to i_*\mathcal S|_W)
=i_*\ker(\mathcal O_V^q|_{V\cap W}\to\mathcal S|_{V\cap W}).
\]
Finite generation of these relation sheaves passes in both directions by the same local generators; off \(V\) all their stalks are zero. The relation-sheaf criterion therefore proves the assertion. Combining it with the quotient-coefficient comparison proves the coherence equivalence of Theorem 3.2(3). In this application \(\mathcal J\) is coherent, hence of finite type, as the local-model hypothesis requires.

For the cohomology assertion take an injective resolution of the underlying abelian sheaf \(\mathcal S\), using [Injective modules, Theorem 2.3](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors#2-functorial-injective-embeddings) with the constant ring \(\mathbf Z\). Its terms are flasque by [Lemma 1.1](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors#1-extending-maps-and-extending-sections). Their direct images are flasque: restriction between two ambient opens is restriction between their intersections with \(V\). Exactness of \(i_*\) makes the image complex a flasque resolution. By [flasque acyclicity and resolutions, Theorem 2.3 and Corollary 2.4](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces#2-extending-sections-removes-the-obstruction), it computes cohomology on \(U\). The two section complexes are identical term by term, because
\[
\Gamma(U,i_*\mathcal I^r)=\Gamma(V,\mathcal I^r).
\]
They therefore have the same cohomology in every degree. [Independence of coefficients, Theorem 3.1](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces#3-coefficients-and-higher-direct-images) identifies this with the module-category groups in the theorem. The argument also applies after restricting to any ambient open \(W\), since \(V\cap W\) is closed in \(W\). We do not claim that direct image along an arbitrary map is exact or that forgetting coefficients preserves injectivity.

*Closed-model dependency proof: GPT-6 Astra (OpenAI), Ultra, 13 October 2026; author self-check, CC0.*

### Local powers and the absence of a uniform exponent

**The local exponent in Theorem 3.2(4).** Write \(\mathcal N=\ker(\mathcal O_X\to\mathcal O_{X_{\mathrm{red}}})\), an ideal sheaf of \(\mathcal O_X\). The precise assertion is that for every \(x\in X\) there exist an open neighbourhood \(W\subset X\) of \(x\) and an integer \(N\geq1\) such that \((\mathcal N|_W)^N=0\). Here an ideal-sheaf power is the ideal sheaf generated by products of the indicated number of local sections. It is not asserted that one integer works on all of \(X\).

To complete the exponent argument in the proof, choose a local model \(V\subset U\) at \(x\). By Theorem 1.1, after shrinking the ambient neighbourhood, the ideal sheaf \(\mathcal I_V\) is generated by finitely many holomorphic sections \(f_1,\ldots,f_s\). The analytic Nullstellensatz used above gives integers \(e_i\geq1\) with \((f_i)_x^{e_i}\in\mathcal J_x\). Membership of a germ in an ideal sheaf means that it has a representative in that sheaf on a neighbourhood. Since there are only finitely many generators, shrink once more so that every relation \(f_i^{e_i}\in\mathcal J\) holds on the same neighbourhood. Put

\[
N=1+\sum_{i=1}^{s}(e_i-1).
\]

Each product of \(N\) generators contains some \(f_i\) at least \(e_i\) times: otherwise its total number of factors would be at most \(\sum_i(e_i-1)=N-1\). Hence every such product belongs to \(\mathcal J\). Since these products generate \(\mathcal I_V^N\), we obtain \(\mathcal I_V^N\subset\mathcal J\) on this neighbourhood, and therefore \((\mathcal I_V/\mathcal J)^N=0\) on its intersection \(W\) with \(V\). If \(s=0\), the ideal is zero and \(N=1\) suffices. This proves the neighbourhood-wise assertion, including its uniformity on each chosen neighbourhood. \(\square\)

**Example 3.2a (no global exponent).** There is a Hausdorff, second countable complex space whose coherent reduction kernel has no globally vanishing power.

**Proof.** For each integer \(m\geq1\), let \(X_m\) be the one-point local analytic model cut out by \(z^{m+1}\) on a disc about zero in \(\mathbf C\). Its ring is

\[
A_m=\mathbf C\{z\}/(z^{m+1}).
\]

The defining ideal is coherent: multiplication by \(z^{m+1}\) identifies it with the coherent sheaf of holomorphic functions on the disc. This multiplication is injective on stalks, since a nonzero holomorphic germ in one variable cannot annihilate another nonzero germ.

Give \(X=\coprod_{m\geq1}X_m\) its disjoint-union topology. More explicitly, for an open subset \(W\subset X\) define

\[
\mathcal O_X(W)=\prod_{m\in W}A_m,
\]

with restriction maps the coordinate projections. These rings form a sheaf because compatible coordinate families glue uniquely; the empty product is the zero ring. Its stalk at \(m\) is \(A_m\), a local \(\mathbf C\)-algebra with maximal ideal generated by the class of \(z\). The topology is discrete and Hausdorff, and its countably many singletons form a countable base. Each singleton, with its restricted sheaf, is exactly the analytic model \(X_m\). Thus \(X\) satisfies Definition 3.1; no compactness or bounded-thickness hypothesis has been added.

The reduction has the same underlying set and stalk \(\mathbf C\) at each point. Its structure map is the morphism of sheaves of \(\mathbf C\)-algebras

\[
\rho:\mathcal O_X\longrightarrow\mathcal O_{X_{\mathrm{red}}},
\qquad
(a_m)_{m\in W}\longmapsto(a_m(0))_{m\in W}.
\]

It is surjective even on sections over each open set, by taking constant representatives. Its kernel \(\mathcal N\) has stalk \(\mathcal N_m=(z)/(z^{m+1})\). This is a coherent ideal sheaf: on each open singleton it is generated by \(z\), with relation ideal \((z^m)\), over the coherent local analytic ring \(A_m\); alternatively it is a coherent image by Theorem 3.2(1). Coherence is local, so the varying value of \(m\) causes no failure of coherence on \(X\).

For each \(m\), \(\mathcal N_m^{m+1}=0\). But for every proposed integer \(r\geq1\), choose \(m\geq r\). Then

\[
(\mathcal N^r)_m=(z^r)/(z^{m+1})\ne0.
\]

Indeed a convergent power series divisible by \(z^{m+1}\) has zero coefficients in degrees at most \(m\), whereas \(z^r\) does not. Ideal-sheaf powers commute with taking stalks because their generators are finite products of germs. Consequently \(\mathcal N^r\ne0\) for every \(r\), even though \(\mathcal N\) is nilpotent on a neighbourhood of every point. The global section whose coordinate at \(m\) is the class of \(z\) likewise has a nilpotent germ at every point but has no zero global power. \(\square\)

**Corollary 3.2b (compact spaces).** If \(X\) is compact, its reduction kernel \(\mathcal N\) does satisfy \(\mathcal N^N=0\) for some single integer \(N\geq1\).

**Proof.** Use Theorem 3.2(4) to cover \(X\) by open sets \(W_x\) with \((\mathcal N|_{W_x})^{N_x}=0\). Choose a finite subcover \(W_{x_1},\ldots,W_{x_t}\) and let \(N=\max_i N_{x_i}\). Higher powers of an ideal are contained in lower powers, so \(\mathcal N^N\) restricts to zero on each member of this cover. Every germ of \(\mathcal N^N\) is therefore zero, which implies that the sheaf is zero: a section with zero germs vanishes on neighbourhoods covering its domain and hence vanishes by the sheaf axiom. If \(X\) is empty, take \(N=1\). The example above shows why compactness cannot simply be omitted from this conclusion. \(\square\)

**Theorem 3.3.** Let \(X\) be a reduced complex space. Then \(X_{\mathrm{reg}}\) is a dense open subset of \(X\) whose complement \(X_{\mathrm{sing}}\) is an analytic subset of \(X\).

**Proof.** Apply Theorem 2.1 in local models \(V\subset U\) with \(\mathcal J=\mathcal I_V\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(A=\{z\in\mathbf C^2:\ z_2^2=z_1^3\}\). Show that \(\mathcal I_A\) is generated by \(z_2^2-z_1^3\) at every point, and describe \(\mathcal O_{A,0}\).

*Solution.* At \(0\), \(I(A,0)=(z_2^2-z_1^3)\) by Exercise 6.1 of the previous lesson. At a point \(x\in A\) other than \(0\), \(A\) is a submanifold near \(x\) and the differential of \(g=z_2^2-z_1^3\) is nonzero, so \(g\) is a local defining function and generates \(I(A,x)\) (a germ vanishing on a submanifold of codimension one with defining function \(g\) is divisible by \(g\), by Weierstrass division in a coordinate in which \(g\) is that coordinate). Off \(A\) the stalk is \(\mathcal O_x\). The substitution \(z_1\mapsto t^2\), \(z_2\mapsto t^3\) induces an isomorphism \(\mathcal O_{A,0}=\mathcal O_2/(z_2^2-z_1^3)\cong\mathbf C\{t^2,t^3\}\subset\mathbf C\{t\}\), as follows.

Divide any \(f\in\mathcal O_2\) by \(g=z_2^2-z_1^3\). The unique remainder is \(a(z_1)+z_2b(z_1)\), with \(a,b\in\mathbf C\{z_1\}\). After substitution it becomes \(a(t^2)+t^3b(t^2)\). The first summand has only even powers of \(t\), and the second only odd powers, starting in degree three. If their sum is zero, every coefficient of both \(a\) and \(b\) is zero. Hence the kernel of substitution is exactly \((g)\), which proves injectivity on the quotient.

Its image consists exactly of the convergent series with no degree-one term. One direction follows from the remainder just computed. Conversely, let \(\sum_{j\geq0}c_jt^j\) converge for \(|t|<r\) and satisfy \(c_1=0\). Set \(a(s)=\sum_{k\geq0}c_{2k}s^k\) and \(b(s)=\sum_{k\geq0}c_{2k+3}s^k\). These series converge for \(|s|<r^2\): for \(0<R<r\), absolute convergence at \(R\) bounds both even and odd subseries at \(|s|<R^2\). They satisfy \(a(t^2)+t^3b(t^2)=\sum_jc_jt^j\). This proves the stated image and the local-ring description.

**Exercise 4.2.** Let \(X\) be the local model \(V(z^2)\subset\mathbf C\), the double point. Show that \(X\) is not reduced, that \(X_{\mathrm{red}}\) is a point, and that \(H^0(X,\mathcal O_X)\) is two-dimensional.

*Solution.* \(\mathcal O_{X,0}=\mathcal O_1/(z^2)\cong\mathbf C[z]/(z^2)\), with the nonzero nilpotent \(z\). The zero set is \(\{0\}\) and \(\mathcal I_{\{0\}}=(z)\), so \(X_{\mathrm{red}}=(\{0\},\mathbf C)\). The space is one point, so \(H^0(X,\mathcal O_X)\) is the stalk, of dimension \(2\) with basis \(1,z\).

**Exercise 4.3.** Find the singular locus of \(A=\{z\in\mathbf C^3:\ z_1z_2=0,\ z_3=0\}\cup\{z_1=z_2=0\}\).

*Solution.* \(A\) is the union of the three coordinate axes. Each axis is a smooth line, and two axes meet only at \(0\). Away from \(0\), \(A\) is near each of its points a single axis, hence smooth. At \(0\) three lines meet, and the germ has three irreducible components, so it is not a submanifold germ. Hence \(A_{\mathrm{sing}}=\{0\}\), an analytic subset with empty interior in \(A\), as Theorem 2.1 predicts.

## References

- [Cartan 1950] H. Cartan, Idéaux et modules de fonctions analytiques de variables complexes, *Bulletin de la Société Mathématique de France* 78 (1950), 29–64. <https://www.numdam.org/item/BSMF_1950__78__29_0/>
- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026). <https://www.jirka.org/scv/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>

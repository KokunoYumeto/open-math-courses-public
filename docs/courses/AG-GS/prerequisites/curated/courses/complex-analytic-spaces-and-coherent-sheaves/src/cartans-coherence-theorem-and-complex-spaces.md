# Cartan's coherence theorem and complex spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

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

*Proof of "\(\subset\)" in (1.3).* Fix \(x\in\Delta\) and let \(F\) be the finite set consisting of \(x\) and the points of \(A\cap\Delta\) above \(x'\) (finite by Theorem 4.1(3)). For \(c\) outside a finite union of proper linear subspaces, \(u_c\) is primitive and takes distinct values at the points of \(F\); fix such a \(c\) and write \(u=u_c\), \(W_u=W(\cdot,\cdot;c)\), \(\delta=\delta(\cdot;c)\), \(B_k=B_k(\cdot,\cdot;c)\), and let \(W_k\) be the minimal polynomial of \(\tilde z_k\). For every \(z'\in\Delta'\), the roots of \(W_u(z',\cdot)\) are exactly the values of \(u\) at the points of \(A\) above \(z'\). Indeed, \(W_u(z',u(z''))\in J\) vanishes on \(A\cap\Delta\), so these values are roots. Conversely, let \(z'\) avoid the zero sets of \(\delta(\cdot;c_0)\) and \(\delta(\cdot;c)\), a dense set. Then the fibre has \(q\) points by Theorem 4.1(1) for \(c_0\), the polynomial \(W_u(z',\cdot)\) has \(q\) distinct roots, and a point \(z\) of the fibre is determined by \(u(z'')\), because \(\delta z_k-B_k(z',u(z''))\in J\) gives \(z_k=B_k(z',u(z''))/\delta(z')\); so the \(q\) values \(u(z'')\) are the \(q\) roots. For general \(z'\), every root of \(W_u(z',\cdot)\) is a limit of roots at such nearby points, hence of values of \(u\) at points of \(A\) that accumulate, by properness, at points of the fibre above \(z'\). Split \(W_u=W_{u,x}\cdot Q_{u,x}\) at the point \((x',u(x''))\) as in [The local ring of holomorphic germs, Lemma 3.2](the-local-ring-of-holomorphic-germs.md#3-unique-factorization), with \(W_{u,x}\) a Weierstrass polynomial in \(T-u(x'')\) and \(Q_{u,x}(x',u(x''))\neq0\); split each \(W_k=W_{k,x}Q_{k,x}\) at \((x',x_k)\) likewise.

If \(x\notin A\), then \(u(x'')\) is not a root of \(W_u(x',\cdot)\), so \(W_u(z',u(z''))\) is a unit at \(x\), and both sides of (1.3) are \(\mathcal O_x\): indeed \(W_u(z',u(z''))\) is a combination of the \(G_i\) with constant coefficients \(c^\beta\), so \((G_{i,x})=\mathcal O_x\). Let now \(x\in A\). Because \(u\) separates the points of \(F\), for \(z'\) near \(x'\) the roots of \(W_u(z',\cdot)\) near \(u(x'')\), which are the roots of \(W_{u,x}(z',\cdot-u(x''))\), are exactly the values \(u(z'')\) at the points \(z\) of \(A\) above \(z'\) near \(x\). Consequently:

(a) *If \(P\in\mathcal O_{x'}[T]\) satisfies \(P(z',u(z''))=0\) on \(A\) near \(x\), then \(W_{u,x}(z',T-u(x''))\) divides \(P\).* Divide \(P\) by this monic polynomial; the remainder has degree less than \(\deg W_{u,x}\) and vanishes at \(\deg W_{u,x}\) distinct roots for all \(z'\) near \(x'\) outside \(S\), so it is zero.

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

**Proof.** The statement is local. First let the germ \((A,0)\) be irreducible of dimension \(d\), and let \(g_1,\ldots,g_N\) generate \(\mathcal I_A\) on a neighbourhood \(\Omega\) of \(0\), by Theorem 1.1. If \(x\in A\cap\Omega\) is regular, \(A\) is near \(x\) a submanifold of dimension \(d\) (Theorem 5.4 of the previous lesson), defined by equations \(v_1,\ldots,v_{n-d}\) with independent differentials. These \(v_j\) vanish on \(A\), so they are combinations of the \(g_i\) near \(x\), and therefore some \(n-d\) of the \(g_i\) have independent differentials at \(x\). Conversely, if some \(n-d\) of the \(g_i\) have independent differentials at \(x\in A\), they define near \(x\) a submanifold \(Y\) of dimension \(d\) containing \(A\); then \(A\) is near \(x\) an analytic subset of the connected manifold \(Y\) with nonempty interior (it has dimension \(d\) at \(x\)), hence equal to \(Y\) near \(x\), as in the proof of [Analytic germs, Proposition 5.5](analytic-germs-local-parametrization-and-the-nullstellensatz.md#5-the-nullstellensatz-and-dimension). So \(A_{\mathrm{sing}}\cap\Omega\) is the common zero set on \(A\cap\Omega\) of all \((n-d)\times(n-d)\) minors of the Jacobian matrix of \((g_1,\ldots,g_N)\), an analytic set.

In general let \((A,0)=\bigcup(A_l,0)\) with irreducible \((A_l,0)\). For small representatives, \(A_k\cap A_l\) has empty interior in \(A_k\) and in \(A_l\) when \(k\neq l\), by Proposition 5.5 of the previous lesson. Hence at a point \(y\) of \(A_k\cap A_l\) the germ \((A,y)\) contains the germs \((A_k,y)\not\subset(A_l,y)\) and \((A_l,y)\not\subset(A_k,y)\), neither contained in a third component, so it is reducible; and a germ of a submanifold is irreducible, its local ring being a ring of convergent power series, a domain. So such points are singular. Hence near \(0\), \(A_{\mathrm{sing}}=\bigcup_lA_{l,\mathrm{sing}}\cup\bigcup_{k\neq l}(A_k\cap A_l)\), which is analytic. It has empty interior by Theorem 5.4 and Proposition 5.5 of the previous lesson. \(\square\)

## 3. Complex spaces

**Definition 3.1.** A **local model** is a pair \((V,\mathcal O_V)\), where \(V=V(\mathcal J)\) is the zero set of a coherent ideal \(\mathcal J\subset\mathcal O_U\) on an open set \(U\subset\mathbf C^n\) and \(\mathcal O_V=(\mathcal O_U/\mathcal J)|_V\). A **complex space** is a Hausdorff, second countable space \(X\) with a sheaf of local \(\mathbf C\)-algebras \(\mathcal O_X\), locally isomorphic as a locally ringed space to local models. It is **reduced** if all stalks of \(\mathcal O_X\) have no nonzero nilpotents; equivalently, near each point it is isomorphic to a model with \(\mathcal J=\mathcal I_V\). Morphisms of complex spaces are morphisms of locally ringed spaces over \(\mathbf C\).

By the Nullstellensatz [Analytic germs, Theorem 5.1](analytic-germs-local-parametrization-and-the-nullstellensatz.md#5-the-nullstellensatz-and-dimension), the nilpotent germs of \(\mathcal O_U/\mathcal J\) at \(x\) are the classes of germs vanishing on \(V\), so the model is reduced exactly when \(\mathcal J=\mathcal I_V\), and every model has a **reduction** \((V,(\mathcal O_U/\mathcal I_V)|_V)\). For a reduced space, \(\mathcal O_X\) is a sheaf of continuous functions: the value of a section at \(x\) is its image in the residue field \(\mathbf C\), and a section vanishing at every point is nilpotent, hence zero. This agrees with the description of reduced analytic spaces in [Complex analytic spaces and analytification, Section 1](course:AG-QC/complex-analytic-spaces-and-analytification#1-analytic-equations-and-their-sheaves). A morphism of reduced complex spaces is the same as a continuous map that pulls holomorphic functions back to holomorphic functions.

**Theorem 3.2.** Let \(X\) be a complex space.

1. \(\mathcal O_X\) is a coherent sheaf of rings. Kernels, cokernels, images and extensions of coherent \(\mathcal O_X\)-modules are coherent, and so are their tensor products and internal homomorphisms; supports of coherent modules are analytic subsets of \(X\).
2. If \(Y\subset X\) is an analytic subset, its ideal sheaf in \(\mathcal O_X\) is coherent.
3. If \(i:V\hookrightarrow U\) is a local model, a sheaf \(\mathcal S\) of \(\mathcal O_V\)-modules is coherent if and only if \(i_*\mathcal S\) is a coherent \(\mathcal O_U\)-module, and \(H^q(V,\mathcal S)=H^q(U,i_*\mathcal S)\) for all \(q\).
4. The reduction \(X_{\mathrm{red}}\) is a reduced complex space with the same underlying space, and \(\mathcal O_X\to\mathcal O_{X_{\mathrm{red}}}\) is surjective with coherent nilpotent kernel.

**Proof.** All statements are local, so let \(X=V\) be a model in \(U\). (1) \(\mathcal O_U/\mathcal J\) is coherent over \(\mathcal O_U\) by Oka's theorem, hence coherent over itself by [Stacks, Tag 0HCC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-change-rings), and the remaining statements follow from [Coherent sheaves and Oka's coherence theorem, Proposition 1.2 and Theorem 3.1](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) applied over \(\mathcal O_X\) (the proofs of Theorem 3.1(2)–(3) use only finite presentations and a coherent structure sheaf, and the support of a coherent \(\mathcal O_X\)-module is the support of its pushforward to \(U\)). (2) The ideal of \(Y\) in \(\mathcal O_U/\mathcal J\) is \((\mathcal I_Y+\mathcal J)/\mathcal J\), a quotient of coherent sheaves by Theorem 1.1. (3) The first statement is Tag 0HCC together with extension by zero. For cohomology, \(i\) is the inclusion of a closed subset, \(i_*\) is exact and carries injective sheaves to flasque sheaves, and flasque sheaves are acyclic [Stacks, Tag 09SY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-flasque-acyclic); so an injective resolution of \(\mathcal S\) pushes forward to a flasque resolution (compare [Stacks, Tag 09T0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-flasque-acyclic-pushforward)) of \(i_*\mathcal S\) with the same global sections. (4) The kernel is \(\mathcal I_V/\mathcal J\), coherent by Theorem 1.1 and nilpotent near each point by the Nullstellensatz, since \(\mathcal I_V\) is finitely generated near each point and each generator has a power in \(\mathcal J\). \(\square\)

**Theorem 3.3.** Let \(X\) be a reduced complex space. Then \(X_{\mathrm{reg}}\) is a dense open subset of \(X\) whose complement \(X_{\mathrm{sing}}\) is an analytic subset of \(X\).

**Proof.** Apply Theorem 2.1 in local models \(V\subset U\) with \(\mathcal J=\mathcal I_V\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(A=\{z\in\mathbf C^2:\ z_2^2=z_1^3\}\). Show that \(\mathcal I_A\) is generated by \(z_2^2-z_1^3\) at every point, and describe \(\mathcal O_{A,0}\).

*Solution.* At \(0\), \(I(A,0)=(z_2^2-z_1^3)\) by Exercise 6.1 of the previous lesson. At a point \(x\in A\) other than \(0\), \(A\) is a submanifold near \(x\) and the differential of \(g=z_2^2-z_1^3\) is nonzero, so \(g\) is a local defining function and generates \(I(A,x)\) (a germ vanishing on a submanifold of codimension one with defining function \(g\) is divisible by \(g\), by Weierstrass division in a coordinate in which \(g\) is that coordinate). Off \(A\) the stalk is \(\mathcal O_x\). The local ring \(\mathcal O_{A,0}=\mathcal O_2/(z_2^2-z_1^3)\) is isomorphic to the subring \(\mathbf C\{t^2,t^3\}\subset\mathbf C\{t\}\) via \(z_1\mapsto t^2\), \(z_2\mapsto t^3\): this map is injective because its kernel is a prime containing \(g\) of height one, equal to \((g)\), and its image consists of the convergent series with no \(t\) term.

**Exercise 4.2.** Let \(X\) be the local model \(V(z^2)\subset\mathbf C\), the double point. Show that \(X\) is not reduced, that \(X_{\mathrm{red}}\) is a point, and that \(H^0(X,\mathcal O_X)\) is two-dimensional.

*Solution.* \(\mathcal O_{X,0}=\mathcal O_1/(z^2)\cong\mathbf C[z]/(z^2)\), with the nonzero nilpotent \(z\). The zero set is \(\{0\}\) and \(\mathcal I_{\{0\}}=(z)\), so \(X_{\mathrm{red}}=(\{0\},\mathbf C)\). The space is one point, so \(H^0(X,\mathcal O_X)\) is the stalk, of dimension \(2\) with basis \(1,z\).

**Exercise 4.3.** Find the singular locus of \(A=\{z\in\mathbf C^3:\ z_1z_2=0,\ z_3=0\}\cup\{z_1=z_2=0\}\).

*Solution.* \(A\) is the union of the three coordinate axes. Each axis is a smooth line, and two axes meet only at \(0\). Away from \(0\), \(A\) is near each of its points a single axis, hence smooth. At \(0\) three lines meet, and the germ has three irreducible components, so it is not a submanifold germ. Hence \(A_{\mathrm{sing}}=\{0\}\), an analytic subset with empty interior in \(A\), as Theorem 2.1 predicts.

## References

- [Cartan 1950] H. Cartan, Idéaux et modules de fonctions analytiques de variables complexes, *Bulletin de la Société Mathématique de France* 78 (1950), 29–64. <https://www.numdam.org/item/BSMF_1950__78__29_0/>
- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026), licensed CC BY-SA 4.0 (dual-licensed with CC BY-NC-SA 4.0). <https://www.jirka.org/scv/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>

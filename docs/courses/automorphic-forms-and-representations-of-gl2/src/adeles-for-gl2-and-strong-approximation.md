# Adèles for GL₂ and strong approximation

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A congruence condition on a modular form records information at finitely many primes. The adelic group puts those conditions in a compact open subgroup, while leaving the real variable free. The purpose of this lesson is to prove that this description recovers the familiar modular quotients, and to explain precisely where the determinant enters.

The local topology and restricted-product construction are introduced in [Totally disconnected groups, the p-adic numbers and the adèles](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-17.html), §6, with the exact local-field and adèle proof providers identified there. We assume those constructions, the Chinese remainder theorem, and Haar measure on locally compact groups. For Haar measure, see Haar measure on locally compact groups. We recall the facts about adèles that are needed. The matrix approximation and quotient theorems are proved here. Basic references are [Voight 2021] and [Getz–Hahn 2022].

## 1. Finite level as a subgroup

Write

\[
\mathbb A=\mathbb R\times\mathbb A_f,
\qquad
\mathbb A_f=\prod_p'\mathbb Q_p,
\qquad
\widehat{\mathbb Z}=\prod_p\mathbb Z_p.
\]

An element of the restricted product is integral at all but finitely many primes. A basic open set prescribes open conditions at finitely many primes and integrality at every other prime. Thus this topology records more than convergence at each individual prime.

Let \(G=\mathrm{GL}_2\), and set

\[
K^{\max}=\prod_p\mathrm{GL}_2(\mathbb Z_p).
\]

An element of \(G(\mathbb A_f)\) is a family \((g_p)_p\) with \(g_p\in K_p^{\max}\) at almost every prime. Equivalently, its entries and the entries of its inverse are finite adèles. This equivalence follows because an invertible matrix over \(\mathbb Z_p\) has an integral inverse, and a matrix and its inverse both integral over \(\mathbb Z_p\) define an automorphism of \(\mathbb Z_p^2\).

For a positive integer \(N\), define

\[
\begin{aligned}
K_0(N)&=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in K^{\max}:c\in N\widehat{\mathbb Z}\right\},\\
K_1(N)&=\{k\in K_0(N):d\equiv1\pmod{N\widehat{\mathbb Z}}\},\\
K(N)&=\{k\in K^{\max}:k\equiv I\pmod{N\widehat{\mathbb Z}}\}.
\end{aligned}
\]

They are compact open subgroups: reduction modulo \(N\) is a continuous map to a finite group, and each is the inverse image of a subgroup. Matrix multiplication verifies the stated conditions are closed under products and inverses.

The determinant maps \(K_0(N)\) and \(K_1(N)\) onto \(\widehat{\mathbb Z}^{\times}\). Indeed, \(\operatorname{diag}(u,1)\) belongs to both groups for every \(u\in\widehat{\mathbb Z}^{\times}\). For the principal subgroup,

\[
\det K(N)=H_N:=\{u\in\widehat{\mathbb Z}^{\times}:u\equiv1\pmod{N\widehat{\mathbb Z}}\}.
\tag{1.1}
\]

One inclusion follows by reducing the determinant; the other follows from the same diagonal matrices. Writing \(H_N\) as \(1+N\widehat{\mathbb Z}\) requires retaining the condition that its elements are units, especially at primes not dividing \(N\).

## 2. The topology must see inverses

**Theorem 2.1.** The restricted product topology on \(G(\mathbb A)\) is the topology induced by

\[
g\longmapsto(g,g^{-1})\in M_2(\mathbb A)\times M_2(\mathbb A).
\tag{2.1}
\]

**Proof.** First consider finite adèles. The restricted product has the compact open subgroup \(K^{\max}\). The inverse image under (2.1) of

\[
M_2(\widehat{\mathbb Z})\times M_2(\widehat{\mathbb Z})
\]

is exactly \(K^{\max}\). On this subgroup, both topologies are the product of the local matrix topologies. Inversion on \(\mathrm{GL}_2(\mathbb Z_p)\) is continuous, by the formula expressing the inverse through the adjugate and the inverse determinant. The assertion therefore holds on this open subgroup.

Translation by a fixed element \(h\) is a homeomorphism in the topology induced by (2.1): on the ambient pair it is the restriction of

\[
(X,Y)\longmapsto(hX,Yh^{-1}),
\]

a continuous linear transformation with continuous inverse. Translates of \(K^{\max}\) cover the group, so the two topologies agree everywhere. At the real place, matrix inversion is continuous on the open set of matrices with nonzero determinant. Taking its product with the finite assertion proves the theorem. \(\square\)

This proof also establishes local compactness. The finite compact open subgroup is locally compact, the real group is locally compact, and their product is \(G(\mathbb A)\). Multiplication and inversion are continuous: on pairs, multiplication sends \(((g,g^{-1}),(h,h^{-1}))\) to \((gh,h^{-1}g^{-1})\).

The inverse coordinate in (2.1) cannot be discarded. Let \(\ell_j\) be distinct primes tending to infinity. Define \(g_j\) to be the identity at the real place and at every finite prime other than \(\ell_j\), and set

\[
(g_j)_{\ell_j}=\operatorname{diag}(\ell_j,1).
\]

As elements of \(M_2(\mathbb A)\), these matrices tend to \(I\): outside any fixed finite set the differences have integral entries. Their inverses do not tend to \(I\), because the entry \(\ell_j^{-1}\) fails the integrality condition at the moving prime. Thus the subspace topology from \(M_2(\mathbb A)\) does not make \(G(\mathbb A)\) a topological group.

**Measures.** Let the additive Haar measure on \(\mathbb Q_p\) give \(\mathbb Z_p\) volume one. On local matrices,

\[
dg=c_p|\det g|_p^{-2}\,da\,db\,dc\,dd
\tag{2.2}
\]

is both left and right invariant. Left multiplication by \(h\) has additive Jacobian \(|\det h|_p^2\), since it acts on two columns; the determinant factor cancels it. The argument for right multiplication uses rows. Choose \(c_p\) so that \(\operatorname{vol}(K_p^{\max})=1\). The restricted product of these measures exists because the chosen compact subgroups have volume one. In particular, \(\operatorname{vol}(K^{\max})=1\).

We will use compatible quotient measures on \(\mathrm{PGL}_2\). At a finite prime, the image \(\overline K_p^{\max}\) has volume one. On the positive-determinant real component write

\[
\overline g=n(x)a(y)r(\theta),\quad
n(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix},\quad
a(y)=\begin{pmatrix}\sqrt y&0\\0&1/\sqrt y\end{pmatrix},
\]

where \(y>0\), and \(r(\theta)\) is rotation. Modulo real scalar matrices, \(\theta\) is taken modulo \(\pi\). Fix the Haar measure

\[
d\overline g=\frac{dx\,dy}{y^2}\,\frac{d\theta}{\pi},
\qquad0\leq\theta<\pi.
\tag{2.3}
\]

To see invariance, the map \(\overline g\mapsto\overline g i\) identifies the quotient by the rotation subgroup with \(\mathbb H\). A real Möbius transformation satisfies \(\operatorname{Im}(gz)=\det(g)\operatorname{Im}(z)/|cz+d|^2\); its real Jacobian is \(\det(g)^2/|cz+d|^4\). Hence \(dx\,dy/y^2\) is invariant. Left translation changes the rotation coordinate by an angle depending on the base point, and preserves its probability measure. This proves invariance of (2.3). Give the negative component its translated measure. Haar measure on the real scalar subgroup can be chosen so that (2.2)'s real analogue induces (2.3); all later inner-product comparisons use these quotient normalizations.

## 3. Approximate the determinant-one part

**Lemma 3.1.** The diagonal copy of \(\mathbb Q\) is dense in the additive group \(\mathbb A_f\).

**Proof.** A basic open set about \(x\) asks that

\[
r-x_p\in p^{n_p}\mathbb Z_p\quad(p\in S),
\qquad r\in\mathbb Z_p\quad(p\notin S),
\]

where \(S\) is finite and includes every prime at which \(x\) is not integral. Choose integers \(m_p\geq0\) such that \(D=\prod_{p\in S}p^{m_p}\) makes every \(Dx_p\) integral and every \(n_p+m_p\) nonnegative. The Chinese remainder theorem supplies \(b\in\mathbb Z\) with

\[
b\equiv Dx_p\pmod{p^{n_p+m_p}\mathbb Z_p}
\quad(p\in S).
\]

For exponent zero there is no condition. Then \(r=b/D\) satisfies every prescribed approximation and is integral outside \(S\). \(\square\)

Put \(u(t)=\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)\) and \(l(t)=\left(\begin{smallmatrix}1&0\\t&1\end{smallmatrix}\right)\).

**Lemma 3.2.** For a field \(F\), the matrices \(u(t)\) and \(l(t)\), with \(t\in F\), generate \(\mathrm{SL}_2(F)\).

**Proof.** Direct multiplication gives

\[
w(a):=u(a)l(-a^{-1})u(a)
=\begin{pmatrix}0&a\\-a^{-1}&0\end{pmatrix},
\qquad
w(a)w(-1)=\operatorname{diag}(a,a^{-1}).
\]

If \(g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) and \(a\ne0\), then

\[
g=l(c/a)\operatorname{diag}(a,a^{-1})u(b/a).
\]

The bottom-right entry is \((1+bc)/a=d\). If \(a=0\), then \(c\ne0\), and multiplying by \(w(1)\) reduces to the previous case. Every factor is generated by the indicated elementary matrices. \(\square\)

**Theorem 3.3 (strong approximation).** The diagonal subgroup \(\mathrm{SL}_2(\mathbb Q)\) is dense in \(\mathrm{SL}_2(\mathbb A_f)\).

**Proof.** Its closure \(C\) is a subgroup. Lemma 3.1 and continuity of \(u,l\) imply that \(C\) contains \(u(t)\) and \(l(t)\) for every \(t\in\mathbb A_f\). Taking \(t\) supported at a single prime and using Lemma 3.2 shows that \(C\) contains the copy of \(\mathrm{SL}_2(\mathbb Q_p)\) supported at that prime. Consequently \(C\) contains every family of matrices supported at finitely many primes.

These families are dense in the restricted product. For \(g\in\mathrm{SL}_2(\mathbb A_f)\), choose a finite set \(S_0\) outside which \(g_p\) is integral. For finite \(S\supseteq S_0\), let \(g^{(S)}_p=g_p\) on \(S\) and \(g^{(S)}_p=I\) elsewhere. Every basic neighborhood of \(g\) contains \(g^{(S)}\) once \(S\) includes its finitely many constrained primes. Hence \(g^{(S)}\to g\), and closedness gives \(g\in C\). \(\square\)

This argument separates the two tasks: approximation of the parameters is additive, while generation of the local groups is algebraic. No assertion about density of the multiplicative rational group is used.

In fact, \(\mathrm{GL}_2(\mathbb Q)\) is not dense in \(\mathrm{GL}_2(\mathbb A_f)\). Consider the nonempty open set of matrices in \(K^{\max}\) whose determinant is congruent to \(2\) modulo \(5\). A rational matrix belonging to \(K^{\max}\) has determinant in

\[
\mathbb Q^{\times}\cap\widehat{\mathbb Z}^{\times}=\{1,-1\},
\]

so cannot belong to that set. The determinant is the obstruction. A density argument for \(\mathrm{GL}_2(\mathbb Q)\) is not available at this step; the decomposition below replaces it.

## 4. The determinant chooses the components

For an idèle \(d=(d_\infty,(d_p))\), set

\[
q=\operatorname{sgn}(d_\infty)\prod_p p^{v_p(d_p)}\in\mathbb Q^{\times}.
\]

Only finitely many exponents are nonzero. Then \(d_p/q\) is a unit for every \(p\), and \(d_\infty/q>0\). This proves

\[
\mathbb A^{\times}
=\mathbb Q^{\times}\mathbb R_{>0}\widehat{\mathbb Z}^{\times},
\tag{4.1}
\]

where the positive real factor has finite components one. The positive representative is unique in the following sense: a rational number that is a unit at every finite place and positive at infinity is \(1\).

**Theorem 4.1.** If \(K\subseteq K^{\max}\) is compact open and \(\det K=\widehat{\mathbb Z}^{\times}\), then

\[
G(\mathbb A)=G(\mathbb Q)G(\mathbb R)^+K.
\tag{4.2}
\]

Here \(G(\mathbb R)^+\) denotes positive determinant, embedded with finite components one.

**Proof.** Given \(g\), apply (4.1) to \(\det g\). Write its finite determinant as \(q u\), where \(u\in\widehat{\mathbb Z}^{\times}\), and its real determinant has the same sign as \(q\). Put \(\gamma_0=\operatorname{diag}(q,1)\), and choose \(k_0\in K\) with \(\det k_0=u\). Then

\[
s=\gamma_0^{-1}g_f k_0^{-1}\in\mathrm{SL}_2(\mathbb A_f).
\]

The group \(L=K\cap\mathrm{SL}_2(\mathbb A_f)\) is open in \(\mathrm{SL}_2(\mathbb A_f)\). Theorem 3.3 gives \(\sigma\in\mathrm{SL}_2(\mathbb Q)\) with \(\sigma^{-1}s\in L\). Thus \(g_f=\gamma_0\sigma k\) for \(k\in K\), and

\[
h_\infty=(\gamma_0\sigma)^{-1}g_\infty
\]

has positive determinant. Therefore \(g=(\gamma_0\sigma)h_\infty k\). \(\square\)

**Theorem 4.2.** Under the hypotheses of Theorem 4.1, let

\[
\Gamma_K=\{\gamma\in G(\mathbb Q):\det\gamma>0,\ \gamma_f\in K\}.
\]

The map induced by the real embedding is a homeomorphism

\[
\Gamma_K\backslash G(\mathbb R)^+
\longrightarrow G(\mathbb Q)\backslash G(\mathbb A)/K.
\tag{4.3}
\]

Moreover \(\Gamma_K\subseteq\mathrm{SL}_2(\mathbb Z)\).

**Proof.** Surjectivity is (4.2). If two real representatives \(h,h'\) have the same double coset, write \(h'=\gamma h k\). At finite places this says \(I=\gamma_f k\), so \(\gamma_f\in K\); at infinity it says \(h'=\gamma_\infty h\), so \(\det\gamma>0\). This proves injectivity. The map is continuous. It is open because, for an open real set \(U\), the set \(UK\) is open in \(G(\mathbb A)\), and its image in the double quotient is open. Hence it is a homeomorphism.

Every entry of \(\gamma\) and of \(\gamma^{-1}\) is integral at all finite primes. They are therefore integers. Its rational determinant is a unit at all finite primes and positive, hence is \(1\). \(\square\)

For \(K_0(N)\), this subgroup is

\[
\Gamma_0(N)=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z):c\equiv0\pmod N\right\}.
\]

For \(K_1(N)\), it is \(\Gamma_1(N)\): the determinant condition and \(c\equiv0,d\equiv1\) also imply \(a\equiv1\pmod N\). The stabilizer of \(i\in\mathbb H\) in \(G(\mathbb R)^+\) is \(Z(\mathbb R)\mathrm{SO}(2)\), as is seen by solving \((ai+b)/(ci+d)=i\). Consequently,

\[
G(\mathbb Q)\backslash G(\mathbb A)/K_0(N)Z(\mathbb R)\mathrm{SO}(2)
\simeq\Gamma_0(N)\backslash\mathbb H,
\tag{4.4}
\]

and the analogous statement holds for \(\Gamma_1(N)\).

**Principal level.** More generally, put \(H=\det K\). Determinants give a bijection of the real quotient's connected components with

\[
\mathbb A^{\times}/\mathbb Q^{\times}\mathbb R_{>0}H
\simeq\widehat{\mathbb Z}^{\times}/H.
\tag{4.5}
\]

Here is also a proof that determinants suffice. Choose representatives \(u_j\) of the last quotient and put \(t_j=\operatorname{diag}(u_j,1)\) at finite places. After a rational determinant correction, the finite determinant of a given \(g\) is \(u_jh\) with \(h\in H\). Choose \(k_0\in K\) of determinant \(h\). The matrix

\[
s=\gamma_0^{-1}g_f k_0^{-1}t_j^{-1}
\]

has determinant one. Approximate it rationally modulo the open group \((t_jKt_j^{-1})\cap\mathrm{SL}_2(\mathbb A_f)\), just as in Theorem 4.1. This gives \(g=\gamma h_\infty t_j k\), with \(\det h_\infty>0\). Equality of two such double cosets forces the determinant labels to agree; for a fixed label its real stabilizer is

\[
\Gamma_j=\{\gamma\in G(\mathbb Q):\det\gamma>0,\ \gamma_f\in t_jKt_j^{-1}\}.
\]

The same open-map argument as before identifies its component with \(\Gamma_j\backslash\mathbb H\). These are connected because \(\mathbb H\) is connected.

For \(K=K(N)\), normality in \(K^{\max}\) gives \(t_jKt_j^{-1}=K\), so every \(\Gamma_j\) is

\[
\Gamma(N)=\{\gamma\in\mathrm{SL}_2(\mathbb Z):\gamma\equiv I\pmod N\}.
\]

Reduction of finite units modulo \(N\) is onto \((\mathbb Z/N\mathbb Z)^{\times}\), with kernel \(H_N\). Thus the quotient in (4.4) for \(K(N)\) is a disjoint union of \(\varphi(N)\) copies of \(\Gamma(N)\backslash\mathbb H\). For example, at level \(8\) there are four copies, labelled by \(1,3,5,7\). Their real stabilizer is the same; their finite determinant labels differ.

Negative real determinants do not double this count. A rational matrix of negative determinant changes the real sign and the finite determinant together. Formula (4.1) chooses positive real representatives before computing (4.5).

At level one, (4.2) also proves

\[
G(\mathbb Q)\backslash G(\mathbb A_f)/K^{\max}=\{\text{one point}\}.
\]

This is a quotient assertion, and does not assert density of \(G(\mathbb Q)\).

## 5. Finite volume and the noncompact cusp

**Theorem 5.1.** The quotient

\[
G(\mathbb Q)Z(\mathbb A)\backslash G(\mathbb A)
\]

has finite Haar volume. With the quotient measures fixed in Section 2, its volume is \(\pi/3\).

**Proof.** Work in \(\mathrm{PGL}_2\), so the scalar centre is removed. The level-one decomposition gives representatives \(n(x)a(y)r(\theta)k_f\), with \(k_f\in\overline K^{\max}\). At infinity reduce \(z=x+iy\) to

\[
\mathcal F=\{z\in\mathbb H:|x|\leq1/2,\ |z|\geq1\}.
\]

The reduction and disjoint-interior theorem are supplied by [The upper half-plane and the modular group](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-01.html), Lemma 2.1 and Theorem 2.2, and Lemma 3.1 and Theorem 3.2. Proposition 5.1 there, with the same hyperbolic measure, gives

\[
\int_{\mathcal F}\frac{dx\,dy}{y^2}=\frac\pi3.
\tag{5.1}
\]

The adelic decomposition and quotient-fibre calculation are the additional assertions proved here.

The rotation fibre has probability measure by (2.3), and \(\overline K^{\max}\) has volume one. Apart from measure-zero elliptic stabilizers, the interior reduction gives unique representatives in the projective group with these fibres: the matrices \(\pm I\) have already become the identity. Therefore quotient integration gives the claimed volume. In particular it is finite. \(\square\)

The same reasoning proves finite volume for a finite-index congruence subgroup: finitely many translates of \(\mathcal F\) suffice, and its effective index in the modular group multiplies the area. The cusp \(y\to\infty\) is noncompact even though its measure \(\int_Y^\infty y^{-2}dy=1/Y\) tends to zero.

**Proposition 5.2.** The rational subgroup \(\mathrm{SL}_2(\mathbb Q)\) is discrete and closed in \(\mathrm{SL}_2(\mathbb A)\), and is not dense there.

**Proof.** Require all finite entries to be integral and all real entries of \(g-I\) to have absolute value less than \(1/2\). A rational matrix in this neighborhood has integer entries and is therefore \(I\). A subgroup of a Hausdorff topological group with such an identity neighborhood is closed: if a point is in its closure, choose a smaller neighborhood \(V\) with \(V^{-1}V\) contained in that identity neighborhood. At most one subgroup point lies in its translate, and closure then forces the point to be that subgroup point. Finally the group is not discrete, since real unipotents arbitrarily near \(I\) are distinct. A closed discrete subgroup cannot be dense in it. \(\square\)

The quotient \(\mathrm{SL}_2(\mathbb Q)\backslash\mathrm{SL}_2(\mathbb A)\) is also noncompact. After quotienting by the compact finite and real maximal compact subgroups, it maps onto \(\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H\). The representatives \(iy\) in the interior of \(\mathcal F\), for \(y\to\infty\), leave every compact subset. For instance the orbit-invariant function \(\max_\gamma\operatorname{Im}(\gamma z)\) is finite and continuous locally (only finitely many integer bottom rows can approach its maximum locally) and has value \(y\) at \(iy\). Compactness would bound this function. Thus discreteness at the full set of places must not be confused with cocompactness.

## 6. Exercises

**Exercise 6.1 (easy).** At level \(12\), determine the determinant images of the three subgroups of Section 1. How many principal-level components occur?

**Exercise 6.2 (medium).** For the moving-prime sequence in Section 2, exhibit an open neighborhood that excludes every inverse, after discarding finitely many terms. Explain why convergence at each individual prime would miss the problem.

**Exercise 6.3 (medium).** Show that \(\mathrm{SL}_2(\mathbb Z)\) is dense in \(\mathrm{SL}_2(\widehat{\mathbb Z})\). Deduce directly that the real stabilizer at principal level is \(\Gamma(N)\), without using a claimed density of \(\mathrm{GL}_2(\mathbb Q)\).

**Exercise 6.4 (medium).** Construct an identity neighborhood witnessing discreteness in the full adèles, and explain why the finite projection of the same rational subgroup can nevertheless be dense.

**Exercise 6.5 (hard).** Prove, for every \(n\geq2\), that \(\mathrm{SL}_n(\mathbb Q)\) is dense in \(\mathrm{SL}_n(\mathbb A_f)\). Include a proof of the local elementary-matrix assertion used in your argument.

## 7. Solutions

**Solution 6.1.** The first two determinant images are \(\widehat{\mathbb Z}^{\times}\), because \(\operatorname{diag}(u,1)\) meets their conditions. The third is the kernel of reduction of finite units modulo \(12\). The unit classes are \(1,5,7,11\); hence there are four components, each a copy of \(\Gamma(12)\backslash\mathbb H\). No real-sign factor is added, by (4.1).

**Solution 6.2.** In the topology induced by the graph map, the inverse image of \(M_2(\widehat{\mathbb Z})\times M_2(\widehat{\mathbb Z})\), with any real identity neighborhood, is open. Every \(g_j^{-1}\) has a nonintegral entry at \(\ell_j\), so is excluded. At a fixed prime \(p\), the sequence and its inverse are eventually \(I\), which shows why the unrestricted product topology cannot detect the failure.

**Solution 6.3.** It suffices to prove that reduction \(\mathrm{SL}_2(\mathbb Z)\to\mathrm{SL}_2(\mathbb Z/N\mathbb Z)\) is onto. Over a local ring \(R=\mathbb Z/p^e\mathbb Z\), a determinant-one matrix has a unit in its first column: otherwise its determinant belongs to the maximal ideal. Swap rows with \(w(1)\) if necessary. With the unit as top-left entry, the factorization in Lemma 3.2 applies; it only requires that entry to be invertible, not that the ring be a field. Thus elementary matrices generate \(\mathrm{SL}_2(R)\). The Chinese remainder theorem identifies \(\mathbb Z/N\mathbb Z\) with the product of these local rings. An elementary matrix in one factor and the identity in all others comes from an elementary matrix over the product, by choosing its parameter with the Chinese remainder theorem. Every such parameter lifts to an integer. Lifting a finite product of elementary matrices therefore gives a determinant-one integer lift. Surjectivity for every \(N\) is exactly the asserted density. For the stabilizer, integrality gives integer entries, positivity and finite determinant units give determinant one, and membership in \(K(N)\) gives precisely the congruence \(\gamma\equiv I\pmod N\).

**Solution 6.4.** Use the neighborhood in Proposition 5.2. Its finite conditions force rational entries to be integers; its real inequalities force those integers to be the entries of \(I\). After forgetting the real place, rational denominators supported at the finitely prescribed primes permit additive approximation. Elementary matrices then yield Theorem 3.3. Density of a projection and discreteness of a subgroup in the larger product are compatible because projection discards precisely the real bound that isolated the identity.

**Solution 6.5.** For \(i\ne j\), let \(E_{ij}(t)=I+t e_{ij}\). Over any field \(F\), these matrices generate \(\mathrm{SL}_n(F)\). Indeed, an invertible first column has a nonzero entry. The two-row operation \(w(1)\) from Lemma 3.2, placed in the corresponding two coordinates, moves it into the first position with determinant one. Row additions clear the other entries of that column. A diagonal operation \(\operatorname{diag}(a^{-1},a)\) in the first two coordinates makes the pivot one; it is elementary by the formula for \(w(a)w(-1)\). Column additions clear the rest of the first row. The remaining block is in \(\mathrm{SL}_{n-1}(F)\), and induction finishes; the case \(n=2\) is Lemma 3.2. All transformations and their inverses are elementary products.

Let \(C_n\) be the closure of \(\mathrm{SL}_n(\mathbb Q)\) in \(\mathrm{SL}_n(\mathbb A_f)\). Additive density and continuity give \(E_{ij}(t)\in C_n\) for every finite adèle \(t\). Parameters supported at one prime and the field assertion give every local \(\mathrm{SL}_n(\mathbb Q_p)\) supported there. Finite products give every finitely supported matrix family. Truncating any adelic family to the identity outside a finite set containing its nonintegral primes converges in the restricted product topology, exactly as in Theorem 3.3. Hence \(C_n\) is the full adelic group.

## What this lesson does not prove

Haar measure's existence and uniqueness are assumed from the linked lesson, specifically Theorem 8.3 (existence) and Theorem 9.2 (uniqueness). The definitions and basic local topology of \(\mathbb Q_p\) and the restricted-product adèle ring use the programme preview in [Totally disconnected groups, the p-adic numbers and the adèles](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-17.html), §6, and its local-field and adèle prerequisites. [Getz–Hahn 2022, Sections 2.1–2.3] is an additional reference. The adelic matrix topology and approximation arguments required for this lesson are proved above. This lesson does not assert strong approximation for arbitrary algebraic groups. A general simply connected almost-simple version, with a noncompact omitted-place factor, is [Getz–Hahn 2022, Theorem 2.5.6]. Its proof is outside this lesson. The matrix and modular-quotient assertions made here have been proved above.

## References

- [Voight 2021] J. Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021, Sections 27.1–27.3 and 28.1–28.3. [Open-access book](https://doi.org/10.1007/978-3-030-56694-4); [author's editions](https://jvoight.github.io/quat.html).
- [Getz–Hahn 2022] J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations, with a View toward Trace Formulae*, draft of 22 April 2022, Chapter 2; published as Graduate Texts in Mathematics 300, Springer, 2024. [Authors' book page](https://sites.duke.edu/jgetz/graduate-text/).

# Idèles and the idèle class group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An adèle can be integral at every finite place and still fail to have an adelic inverse. For example, the family whose component at each rational prime \(p\) is \(p\), and whose real component is \(1\), lies in \(\mathbb A_{\mathbb Q}\). Its coordinatewise inverse is not integral at any finite place, so it is not an adèle. The invertible adèles must have unit components almost everywhere. Their topology must also control the inverse.

The resulting group connects two kinds of information. Valuations record fractional ideals. Archimedean absolute values record the logarithms of units. After quotienting by multiplication by a field element, the part with total absolute value one is compact. We will prove this compactness from the adelic box lemma and then obtain both the finiteness of the ideal class group and Dirichlet's unit theorem. Neither of those two conclusions is assumed in the compactness proof.

Throughout, \(K\) is a number field, with \(r_1\) real places and \(r_2\) complex places. We use the normalized absolute values

\[
 |x|_v=\begin{cases}
 |x|,&v\text{ real},\\
 |x|^2,&v\text{ complex},\\
 q_v^{-\operatorname{ord}_v(x)},&v\text{ finite},
 \end{cases}
 \qquad q_v=\#(\mathcal O_v/\mathfrak p_v).
 \tag{1}
\]

The product formula says \(\prod_v|a|_v=1\) for \(a\in K^\times\). At complex places, geometric radii and triangle inequalities always use the ordinary modulus; the square in (1) is a multiplicative normalization.

We use three results from [The adèle ring of a number field](NT-ADL-02.md): \(K\) is discrete and closed in \(\mathbb A_K\) (Theorem 2.2); finite-place integer rings are compact; and if an idèle \(\beta\) satisfies

\[
 \prod_v|\beta_v|_v>C_K,
 \qquad C_K=(2/\pi)^{r_2}\sqrt{|d_K|},
 \tag{2}
\]

then there is a nonzero \(a\in K\) with \(|a|_v\leq |\beta_v|_v\) at every place (Lemma 2.5). That lemma was proved by additive quotient volume and a difference of two points in an adelic box. We also use the ordinary ideal theory of the Dedekind domain \(\mathcal O_K\): fractional ideals have unique finite prime factorization, and the exponent in \((a)\) is \(\operatorname{ord}_v(a)\). No class-number or unit-rank assertion enters these prerequisites.

## A topology that controls multiplication and inversion

Define

\[
 J_K=\mathbb A_K^\times
 =\left\{(x_v):x_v\in K_v^\times\text{ for all }v,
              \ x_v\in\mathcal O_v^\times\text{ for almost all finite }v\right\}.
 \tag{3}
\]

The equality follows directly from the definition of the adèle ring. If both \(x\) and \(x^{-1}\) are adèles, then outside a finite set both components are integral, which forces \(\operatorname{ord}_v(x_v)=0\). Conversely, the condition in (3) makes the coordinatewise inverse an adèle.

For a finite set \(S\) containing all archimedean places, put

\[
 J_{K,S}=\prod_{v\in S}K_v^\times
                 \times\prod_{v\notin S}\mathcal O_v^\times.
 \tag{4}
\]

Equip \(J_K\) with the restricted product topology: the subgroups (4) are open and have their product topologies. A basic neighbourhood of \(x\), after \(S\) contains its nonunit components, has the form

\[
 \prod_{v\in S}W_v\times\prod_{v\notin S}\mathcal O_v^\times,
 \qquad x_v\in W_v\subset K_v^\times\text{ open}.
 \tag{5}
\]

**Proposition 3.1.** The restricted product topology makes \(J_K\) a locally compact Hausdorff abelian group. It is also the topology transported by

\[
 x\longmapsto (x,x^{-1})
 \tag{6}
\]

from the subspace \(\{(x,y)\in\mathbb A_K^2:xy=1\}\). The inclusion \(J_K\to\mathbb A_K\) is continuous, but its image does not have the idèle topology as its additive subspace topology.

**Proof.** Each \(\mathcal O_v^\times\) is compact and open in \(K_v^\times\). Indeed, \(\mathcal O_v^\times=\mathcal O_v\setminus\mathfrak p_v\), a closed subset of the compact ring \(\mathcal O_v\), and it is open because valuations are locally constant away from zero. The restricted product theorem, Proposition 1.1 of [Restricted products and profinite completions](NT-ADL-01.md), therefore gives all the asserted group and local compactness properties.

The coordinatewise inclusion into \(\mathbb A_K\) is continuous on each open chart (4), hence is continuous globally. Inversion is continuous in the restricted product, so (6) is continuous. It is a bijection onto the displayed graph because every inverse in a ring is unique.

To check its inverse, take a basic neighbourhood (5). In the first adèle coordinate impose \(x_v\in W_v\) for \(v\in S\) and \(x_v\in\mathcal O_v\) outside \(S\). These are additive open conditions: \(K_v^\times\) is open in \(K_v\), so \(W_v\) is also open in \(K_v\). In the second adèle coordinate impose \(y_v\in\mathcal O_v\) outside \(S\), with no restriction at \(S\). On the graph \(y=x^{-1}\), the two tail conditions are exactly \(x_v\in\mathcal O_v^\times\). Their intersection pulls back to (5). Thus every restricted product neighbourhood is open in the graph topology. The graph is closed in \(\mathbb A_K^2\), since multiplication is continuous and \(\{1\}\) is closed.

For strictness of the topology comparison, choose pairwise distinct finite places \(v_n\), and a uniformizer \(\varpi_n\) at \(v_n\). Let \(x^{(n)}\) have component \(\varpi_n\) at \(v_n\) and component \(1\) everywhere else. These are idèles. They tend to \(1\) in \(\mathbb A_K\): any additive neighbourhood restricts only finitely many places and permits integral components at all remaining finite places. But none lies in the idèle neighbourhood

\[
 \prod_{v\mid\infty}K_v^\times\times\prod_{v\nmid\infty}\mathcal O_v^\times
 \tag{7}
\]

of \(1\). Moreover, \((x^{(n)})^{-1}\) never belongs to the additive neighbourhood \(K_\infty\times\prod_{v\nmid\infty}\mathcal O_v\), where \(K_\infty=\prod_{v\mid\infty}K_v\). Inversion is therefore discontinuous at \(1\) for the additive subspace topology. \(\square\)

Equivalently, the idèle topology is the weakest topology containing the additive subspace topology for which inversion is continuous. Adding the inverse images of additive open sets gives precisely the graph topology; multiplication is then continuous by Proposition 3.1.

## The norm-one constraint recovers the additive topology

Only finitely many factors differ from \(1\) in

\[
 |x|=\prod_v|x_v|_v,
 \qquad J_K^1=\{x\in J_K:|x|=1\}.
 \tag{8}
\]

This number is called the idèle norm, or content. It is not a vector-space norm.

**Proposition 3.2.** The map \(|\cdot|:J_K\to\mathbb R_{>0}\) is a continuous surjective homomorphism. The diagonal subgroup \(K^\times\) is discrete and closed in \(J_K\) and lies in \(J_K^1\). The subset \(J_K^1\) is closed in \(\mathbb A_K\), and its subspace topologies from \(J_K\) and \(\mathbb A_K\) coincide.

**Proof.** On (4), the norm is the finite product \(\prod_{v\in S}|x_v|_v\), hence is continuous. Each local absolute value is multiplicative. Choose an archimedean place \(w\). Define a homomorphism \(s:\mathbb R_{>0}\to J_K\) by setting all components except \(w\) equal to \(1\), and setting

\[
 s(t)_w=\begin{cases}t,&w\text{ real},\\ \sqrt t,&w\text{ complex}.
                  \end{cases}
 \tag{9}
\]

It is continuous and \(|s(t)|=t\), proving surjectivity. The product formula puts \(K^\times\) in the kernel. Since \(K\) is discrete in \(\mathbb A_K\), some additive open neighbourhood \(U\) of \(1\) meets \(K\) only at \(1\). Its inverse image in \(J_K\) isolates \(1\) in \(K^\times\).

A discrete subgroup of a Hausdorff topological group is closed. Here is the argument we will use. Choose an identity neighbourhood \(V\) with \(VV^{-1}\) meeting the subgroup only at the identity. Each translate \(gV\) contains at most one subgroup element. If \(g\) lies in the closure of the subgroup, such a translate contains one element \(h\). Were \(g\ne h\), intersecting with a neighbourhood of \(g\) that avoids \(h\) would contradict closure. Thus every closure point belongs to the subgroup.

For the topology assertion, fix \(x\in J_K^1\) and a basic idèle neighbourhood (5), with \(S\) containing all its nonunit components and all archimedean places. Shrink the finitely many \(W_v\), if necessary, so that

\[
 \prod_{v\in S}|y_v|_v<2 \quad\text{whenever }y_v\in W_v.
 \tag{10}
\]

This is possible because the product at \(x\) equals \(1\). Permit \(y_v\in\mathcal O_v\) outside \(S\); this gives an additive neighbourhood \(W\) of \(x\). If \(y\in W\cap J_K^1\) had a nonunit component at a finite place outside \(S\), that component would have normalized absolute value at most \(q_v^{-1}\leq 1/2\). All other tail factors are at most \(1\), so (10) would give \(|y|<1\), a contradiction. Consequently \(W\cap J_K^1\) lies in (5). The opposite topology inclusion follows from the continuous inclusion \(J_K\to\mathbb A_K\).

It remains to establish additive closedness. We give all the cases, since a closedness assertion in \(J_K\) alone would not justify intersecting \(J_K^1\) with an additive compact box.

First take \(z\in\mathbb A_K\) with a zero component. Choose a finite set \(S\) containing that place, every archimedean place and every finite place where \(z\) is nonintegral. The finite product \(\prod_{v\in S}|z_v|_v\) is zero. By continuity it is less than \(1\) throughout some finite-coordinate neighbourhood. Together with integral tails, this gives an additive neighbourhood containing no norm-one idèle.

Next suppose every component is nonzero but \(z\) is not an idèle. Infinitely many integral finite components are nonunits. Starting with all archimedean and nonintegral places, add enough such nonunit places to make the finite product less than \(1\); each added factor is at most \(1/2\). The same neighbourhood argument excludes \(J_K^1\).

Finally suppose \(z\) is an idèle with norm \(c\ne1\). If \(c<1\), take \(S\) containing all nonunit and archimedean places and again keep its finite product less than \(1\). If \(c>1\), enlarge this \(S\) to include all finite places with \(q_v\leq 2c\). There are finitely many: such a place lies above a rational prime \(p\leq 2c\), and a number field has finitely many places above each \(p\). Choose finite-coordinate neighbourhoods so that

\[
 1<\prod_{v\in S}|y_v|_v<2c,
 \qquad y_v\in\mathcal O_v\quad(v\notin S).
 \tag{11}
\]

If a member of this additive neighbourhood were a norm-one idèle, either its tail would consist entirely of units, giving norm greater than \(1\), or some tail component would have absolute value at most \(q_v^{-1}<(2c)^{-1}\), giving norm less than \(1\). Both are impossible. Every point outside \(J_K^1\) therefore has an additive neighbourhood disjoint from it. \(\square\)

The mechanism in (10) is useful: a new tail valuation costs at least a factor of two, and a sufficiently small change at finitely many places cannot pay that cost while preserving norm one.

This is the topology issue addressed in [Sutherland, Lecture 26, Lemma 26.8, pp.3–4]. Notice why two separate arguments were needed: equality of the topologies at a norm-one point uses the strict bound \(<2\) in (10), whereas additive closedness must also exclude zero coordinates, infinitely many nonunit coordinates, and idèles with content different from one. For content \(c>1\), retaining every place with \(q_v\leq2c\) makes the remaining norm loss strictly larger than any permitted finite-coordinate gain. This is the reason an additive compact box can be used in the next theorem.

## Compactness before class numbers and units

The idèle class group and its norm-one part are

\[
 C_K=J_K/K^\times,
 \qquad C_K^1=J_K^1/K^\times.
 \tag{12}
\]

They have quotient topologies. Quotient maps of topological groups are open: the inverse image of the image of an open set is the union of its subgroup translates. Since \(K^\times\) is closed, these quotients are Hausdorff and locally compact. The restriction of the quotient map to \(J_K^1\) realizes \(C_K^1\) as the kernel of the induced norm on \(C_K\), with its subspace topology; this also follows explicitly from the splitting proved in Proposition 3.5 below.

**Theorem 3.3 (norm-one compactness).** The group \(C_K^1\) is compact.

**Proof.** Choose an idèle \(\eta\) with \(|\eta|>C_K\); the section (9) supplies one. The additive box

\[
 B_\eta=\{z\in\mathbb A_K:|z_v|_v\leq |\eta_v|_v\text{ at every }v\}
 \tag{13}
\]

is compact. Each archimedean factor is a closed bounded interval or disk; each finite factor is the compact subgroup \(\eta_v\mathcal O_v\); almost all of the latter equal \(\mathcal O_v\). Thus the box is a product of compact sets in one additive restricted product chart.

By Proposition 3.2, \(B_\eta\cap J_K^1\) is closed in this box and compact in the idèle topology. For any \(x\in J_K^1\), apply the adelic box lemma (2) to \(\eta x^{-1}\). Its norm is \(|\eta|>C_K\), so there is \(a\in K^\times\) satisfying

\[
 |a|_v\leq |\eta_vx_v^{-1}|_v,
 \qquad |ax_v|_v\leq|\eta_v|_v
 \quad\text{for every }v.
 \tag{14}
\]

The product formula gives \(|ax|=1\). Thus \(ax\in B_\eta\cap J_K^1\), and it represents the same class as \(x\). The quotient is the continuous image of this compact set. \(\square\)

This proof uses no choice of ideal-class representatives and no fundamental domain for a unit lattice. Those two objects will follow from compactness.

The compact representative set \(B_\eta\cap J_K^1\) is also the mechanism in [Sutherland, Lecture 26, Theorem 26.9, p.4]. Multiplying a norm-one idèle \(x\) by the field element obtained from the bounds for \(\eta x^{-1}\) leaves its content equal to one by the product formula. Thus the proof can precede class-number finiteness and the unit theorem, as Remark 26.10 there explains. [Milne, *Class Field Theory*, V, §4, 4.4 and the notes on p.172] also distinguishes the noncompact full quotient from its compact norm-one part. Below we prove the arithmetic consequences, including the logarithmic lattice, without assuming them in this compactness step.

**Corollary 3.4.** The ideal class group \(\operatorname{Cl}_K\) is finite. The unit group has the form

\[
 \mathcal O_K^\times\simeq\mu_K\times\mathbb Z^{r_1+r_2-1},
 \tag{15}
\]

where \(\mu_K\) is the finite cyclic group of roots of unity in \(K\). More precisely, the logarithms of units form a full lattice in

\[
 H=\left\{(t_v)_{v\mid\infty}\in\mathbb R^{r_1+r_2}:
                  \sum_{v\mid\infty}t_v=0\right\}.
 \tag{16}
\]

**Proof.** Let \(I_K\) be the group of nonzero fractional ideals, with the discrete topology. The map

\[
 \mathfrak a:J_K\longrightarrow I_K,
 \qquad x\longmapsto\prod_{v\nmid\infty}\mathfrak p_v^{\operatorname{ord}_v(x_v)}
 \tag{17}
\]

is a continuous surjective homomorphism. Its kernel is the open subgroup

\[
 J_{K,\infty}=K_\infty^\times\times U_f,
 \qquad U_f=\prod_{v\nmid\infty}\mathcal O_v^\times.
 \tag{18}
\]

Surjectivity follows by placing uniformizer powers at the finitely many primes in an ideal factorization. Continuity follows because the kernel is open, or directly because valuation vectors are locally constant in idèle charts. Multiplying a chosen lift by \(s(|x|^{-1})\) changes no finite valuation and makes its norm one. Hence (17) is still surjective on \(J_K^1\). It takes a principal idèle \(a\) to \((a)\), and induces a continuous surjection

\[
 C_K^1\longrightarrow\operatorname{Cl}_K.
 \tag{19}
\]

A compact discrete space is finite, proving class-number finiteness.

Set \(J_{K,\infty}^1=J_{K,\infty}\cap J_K^1\). The intersection \(J_{K,\infty}^1\cap K^\times\) is exactly \(\mathcal O_K^\times\): zero finite valuations mean that both \(a\) and \(a^{-1}\) are algebraic integers. Moreover,

\[
 J_{K,\infty}^1/\mathcal O_K^\times
 \simeq \ker\bigl(C_K^1\to\operatorname{Cl}_K\bigr)
 \tag{20}
\]

as topological groups. To see surjectivity, if \(\mathfrak a(x)\) is principal, divide \(x\) by a generator; its norm stays one and its finite valuations become zero. The kernel is the indicated intersection. For the topology, \(J_{K,\infty}^1\) is open in \(J_K^1\), and the quotient map is open, so the induced bijection onto its image is open. The right side of (20) is closed in the compact group \(C_K^1\), hence the left side is compact.

On \(J_{K,\infty}^1\), define

\[
 \ell(x)=(\log|x_v|_v)_{v\mid\infty}\in H.
 \tag{21}
\]

This is a continuous surjection. For any \(t\in H\), take component \(e^{t_v}\) at a real place and the positive real number \(e^{t_v/2}\) at a complex place, and take all finite components equal to \(1\). These components give a lift with norm one. Its kernel is the compact group

\[
 \{\pm1\}^{r_1}\times(S^1)^{r_2}\times U_f.
 \tag{22}
\]

Let \(\Gamma=\ell(\mathcal O_K^\times)\). We first prove that bounded sets meet \(\Gamma\) in finitely many points. For a fixed \(M>0\), all units whose logarithms satisfy \(|\log|a|_v|\leq M\) lie in the compact idèle set consisting of finite units and archimedean annuli \(e^{-M}\leq|x_v|_v\leq e^M\). Its intersection with the discrete closed subgroup \(K^\times\) is finite. Consequently \(\Gamma\) is discrete and closed, and the kernel of \(\ell\) on units is finite.

That finite kernel equals \(\mu_K\). Every element of a finite subgroup has finite order, while every root of unity is an algebraic unit with all normalized absolute values equal to one. It is cyclic: through any archimedean embedding it is a finite subgroup of \(\mathbb C^\times\), contained in the cyclic group of \(N\)-th roots of unity for a common multiple \(N\) of its element orders.

The map (21) descends to a continuous surjection from the compact group in (20) onto \(H/\Gamma\), so \(H/\Gamma\) is compact. We finish with the following elementary lattice argument rather than assuming the unit theorem.

If a subgroup \(\Gamma\subset\mathbb R^d\) meets bounded sets in finitely many points, then it has a basis of at most \(d\) linearly independent vectors over \(\mathbb Z\). For a nonzero group, choose \(e\ne0\) generating its intersection with the line \(\mathbb Re\); one can choose a shortest nonzero vector on any line meeting the group, and subtract integer multiples to prove the cyclic assertion. Orthogonally project onto \(e^\perp\). The projected group still meets bounded sets in finitely many points: lift points in a bounded set and subtract integer multiples of \(e\) so their \(e\)-coordinate lies in one fixed interval of length \(\|e\|\). All resulting lifts lie in a bounded set, so there are finitely many. Induction on dimension gives a basis of the projected group; lifting that basis and adjoining \(e\) gives a basis of \(\Gamma\). Independence follows by projecting a linear relation and then using the nonzero vector \(e\).

If \(\mathbb R^d/\Gamma\) is compact, these basis vectors must span \(\mathbb R^d\). Otherwise a nonzero linear functional annihilating their span would descend to a continuous surjection \(\mathbb R^d/\Gamma\to\mathbb R\), impossible for a compact source. Thus \(\Gamma\) has rank \(d\). Applied to (16), this gives rank \(r_1+r_2-1\). Choose lifts \(\varepsilon_1,\ldots,\varepsilon_d\) of a lattice basis in the unit group. Every unit is uniquely a root of unity times \(\varepsilon_1^{n_1}\cdots\varepsilon_d^{n_d}\), proving (15). When \(d=0\), the lattice is zero and all units are roots of unity. \(\square\)

The same framework contains the usual theorem on \(S\)-units. Here are the details needed to keep track of the extra rank. Let \(S=S_\infty\cup S_f\), with \(S_f\) a finite set of finite places, and let

\[
 E_{K,S}=\{a\in K^\times:\operatorname{ord}_v(a)=0\text{ for finite }v\notin S\}.
\]

The valuation map fits into

\[
 1\longrightarrow\mathcal O_K^\times\longrightarrow E_{K,S}
   \longrightarrow\mathbb Z^{S_f}.
 \tag{23}
\]

Its image has finite index. Indeed, if \(h=\#\operatorname{Cl}_K\), then \(\mathfrak p_v^h=(a_v)\) for each \(v\in S_f\), and \(a_v\in E_{K,S}\) maps to \(h\) times the corresponding coordinate vector. Thus the image contains \(h\mathbb Z^{S_f}\); the lattice argument above shows it is free of rank \(\#S_f\). Lifting a basis splits (23) over its image and gives

\[
 E_{K,S}\simeq\mu_K\times\mathbb Z^{r_1+r_2-1+\#S_f}.
 \tag{24}
\]

Its logarithms \((\log|a|_v)_{v\in S}\) form a full lattice in the hyperplane \(\sum_{v\in S}t_v=0\). For a direct check, the finite coordinates lie in the grid \(\prod_{v\in S_f}\log q_v\,\mathbb Z\), and their image has finite index in that grid. After reducing these coordinates by the chosen lifted basis, the remaining logarithms lie in the archimedean unit lattice of (16). This proves discreteness and gives a bounded parallelepiped covering the hyperplane modulo the logarithms. The finite-coordinate grid spans \(\mathbb R^{S_f}\), while the archimedean unit lattice spans its kernel, so the full span has dimension \(\#S-1\). The logarithmic kernel is again \(\mu_K\).

The finite logarithmic coordinate is exactly \(-\operatorname{ord}_v(a)\log q_v\). This identifies the valuation grid, including its sign, with the logarithmic grid. [Milne, *Algebraic Number Theory*, Theorem 5.11] uses the same finite-index grid argument for \(S\)-units. Our proof has first obtained the ordinary class number and unit lattice from Theorem 3.3, so the use of \(h\mathbb Z^{S_f}\) in (23) assumes no additional finiteness theorem.

## Separating the norm from the compact group

**Proposition 3.5.** A choice of section (9) gives topological group isomorphisms

\[
 J_K\simeq J_K^1\times\mathbb R_{>0},
 \qquad C_K\simeq C_K^1\times\mathbb R_{>0}.
 \tag{25}
\]

**Proof.** The maps

\[
 (y,t)\longmapsto y\,s(t),
 \qquad x\longmapsto\bigl(x\,s(|x|)^{-1},|x|\bigr)
 \tag{26}
\]

are continuous inverse homomorphisms. The second map sends \(K^\times\) onto \(K^\times\times\{1\}\). Taking quotients yields (25), since the product of a quotient map with the identity is open and surjective, hence a quotient map. Explicitly the class inverse is \([x]\mapsto([x\,s(|x|)^{-1}],|x|)\), so its continuity also follows from the defining quotient topology. \(\square\)

The norm homomorphism is canonical; its splitting is a choice. For a general number field the connected component of \(C_K\) can include connected groups inside \(C_K^1\). Therefore (25) does not identify the connected component with its \(\mathbb R_{>0}\) factor in general.

## Rational representatives

For \(K=\mathbb Q\), write

\[
 \widehat{\mathbb Z}^{\times}=\prod_p\mathbb Z_p^\times.
\]

We embed this group in \(J_{\mathbb Q}\) with real component \(1\), embed \(\mathbb R_{>0}\) with every finite component \(1\), and embed \(\mathbb Q^\times\) diagonally.

**Proposition 3.6.** These embeddings give internal direct products of topological groups

\[
 J_{\mathbb Q}=\mathbb Q^\times\times\mathbb R_{>0}
                     \times\widehat{\mathbb Z}^{\times},
 \qquad
 \mathbb A_f^\times=\mathbb Q_{>0}^\times\times\widehat{\mathbb Z}^{\times}.
 \tag{27}
\]

Here the rational factors carry the discrete topology, and the finite idèles carry their restricted product topology. Consequently

\[
 C_{\mathbb Q}\simeq\mathbb R_{>0}\times\widehat{\mathbb Z}^{\times},
 \qquad C_{\mathbb Q}^1\simeq\widehat{\mathbb Z}^{\times}.
 \tag{28}
\]

The identity component of \(C_{\mathbb Q}\) is \(\mathbb R_{>0}\times\{1\}\), and its quotient by that component is \(\widehat{\mathbb Z}^{\times}\).

**Proof.** For \(x\in J_{\mathbb Q}\), set

\[
 q_0=\prod_p p^{\operatorname{ord}_p(x_p)}>0,
 \quad q=\operatorname{sgn}(x_\infty)q_0,
 \quad t=\frac{x_\infty}{q}>0,
 \quad u_p=\frac{x_p}{q}.
 \tag{29}
\]

The product for \(q_0\) is finite, and \(\operatorname{ord}_p(q)=\operatorname{ord}_p(x_p)\), so every \(u_p\) is a unit. Thus \(x=qtu\). Finite valuations determine \(q_0\), and the real sign determines \(q\); the other two factors then follow. This proves existence and uniqueness.

The multiplication map from the product in (27) is continuous. Its inverse is continuous too: near a fixed idèle, the finitely many relevant finite valuations and the real sign can be kept constant in a basic neighbourhood (5), so \(q\) is locally constant. Then \(t=x_\infty/q\) and \(u=x/q\) with the real component removed vary continuously. Also

\[
 |x|=|x_\infty|\prod_p p^{-\operatorname{ord}_p(x_p)}
      =|x_\infty|/q_0=t.
 \tag{30}
\]

The same argument without the real sign gives the finite decomposition, with positive rational factor \(q_0\). Its discreteness can also be seen from \(\mathbb Q_{>0}^\times\cap\widehat{\mathbb Z}^{\times}=\{1\}\). Quotienting the first decomposition by its diagonal rational factor proves (28), and (30) identifies the norm-one factor.

Finally \(\widehat{\mathbb Z}^{\times}\) is totally disconnected. Reduction modulo \(p^n\) is continuous into a finite discrete unit group, so a connected subset has constant image in every such quotient. These reductions separate points in \(\mathbb Z_p^\times\), and the coordinate projections separate points in the product. Thus every connected subset is a singleton. In contrast \(\mathbb R_{>0}\) is connected. Projecting a connected subset of (28) to the second factor proves the component assertion. \(\square\)

The sign and valuations in (29) are the rational decomposition described in [Lenstra, *The Idèle Class Group*, Example 1.1, p.2]. With the infinite place removed, the positive rational factor is determined by the finite valuations alone, giving the second formula in (27), also stated in [Bost–Connes, §3, proof of Proposition 12(2), p.427]. The topology check above proves these as topological direct products, and (30) identifies the real factor with the normalized idèle norm rather than the unadjusted real component.

For an explicit representative, take an idèle with real component \(-7/10\), component \(8\) at \(2\), component \(1/25\) at \(5\), and component \(1\) at all other primes. Formula (29) gives

\[
 q_0=8/25,\qquad q=-8/25,\qquad t=35/16,
\]

and

\[
 u_2=-25,\qquad u_5=-1/8,\qquad u_p=-25/8\ (p\ne2,5).
\]

Every displayed \(u_p\) is a unit in its own local ring, and the idèle class is represented by \((35/16,u)\). Its norm is \(35/16\), even though its real component has absolute value \(7/10\).

For \(K=\mathbb Q(i)\), whose integer ring \(\mathbb Z[i]\) was identified in Exercise 2 of *The adèle ring of a number field*, the corresponding ideal-class quotient is trivial:

\[
 C_K/\operatorname{image}\bigl(\mathbb C^\times\times U_f\bigr)
     \simeq\operatorname{Cl}_K=1.
 \tag{31}
\]

Indeed, \(\mathbb Z[i]\) is Euclidean for \(N(a+bi)=a^2+b^2\). Given a complex quotient, round each real coordinate to the nearest integer. The error has squared modulus at most \(1/2<1\), so division by a nonzero Gaussian integer has a remainder of smaller norm. A nonzero ideal contains an element of least positive norm; division by that element shows it generates the ideal. All fractional ideals are principal. Formula (17) then proves (31). In this case every norm-one class has a representative with all finite components units; its complex component must have ordinary modulus one. Hence

\[
 C_{\mathbb Q(i)}^1\simeq (S^1\times U_f)/\mu_4,
 \qquad \mu_4=\{1,-1,i,-i\},
 \tag{32}
\]

where \(\mu_4\) is embedded diagonally in all components. The unit calculation follows either by solving \(a^2+b^2=1\), or from the zero-rank case of (15). Unlike the rational compact factor, (32) visibly has a connected circle coming from \(S^1\).

There is a different quotient, \(\mathbb A_K/K^\times\), where multiplication acts on all adèles, including zero. It is not the idèle class group and is not Hausdorff. For example, the orbit of the adèle with component \(1\) at a chosen archimedean place and zero at every other place is not closed: multiplication by positive rational numbers tending to zero makes it converge to the zero adèle, which is not in that orbit. If the quotient were Hausdorff, the inverse image of every singleton would be closed. This observation explains why the topology assertions above concern invertible adèles.

## Exercises

1. **Easy.** Starting with the finite valuations and real sign of a rational idèle, construct its factors \(q,t,u\) in (27). Show that \(t\) is its idèle norm and that all three factors are unique. Carry out the construction when \(x_\infty=9\), \(x_3=1/9\), \(x_5=5\), and every other finite component is \(1\).

2. **Medium.** For an arbitrary number field, construct idèles tending additively to \(1\) whose inverses do not tend additively to \(1\). Explain separately why the same idèles fail to converge in the idèle topology.

3. **Medium.** Prove directly from the product formula, without additive discreteness as a black box, that \(K^\times\) is discrete and closed in \(J_K\). Include complex places with the normalization (1).

4. **Hard.** Recover Dirichlet's unit theorem from compactness of \(C_K^1\). Identify the compact quotient used in the proof, show the logarithmic image is a lattice of full rank, and explain why the finite kernel is precisely \(\mu_K\). Then show how each finite place allowed in an \(S\)-unit group adds one to the rank.

## Solutions

**Solution 1.** Finite valuations determine \(q_0=\prod p^{\operatorname{ord}_p(x_p)}\). Choose \(q\) to have magnitude \(q_0\) and the sign of \(x_\infty\), put \(t=x_\infty/q\), and divide each finite component by \(q\). Its valuation becomes zero at every prime, giving \(u\). The normalized finite product is \(q_0^{-1}\), so \(t=|x_\infty|/q_0=|x|\). Any proposed decomposition has these finite valuations and real sign, so yields the same \(q\), then the same \(t,u\). In the example, \(q=q_0=5/9\), \(t=81/5\), \(u_3=1/5\), \(u_5=9\), and \(u_p=9/5\) at every other prime. These are local units. Directly, the norm is \(9\cdot9\cdot(1/5)=81/5\).

**Solution 2.** Enumerate pairwise distinct finite places \(v_n\). They exist because there are infinitely many rational primes and each has at least one place above it. Take a uniformizer at \(v_n\), set that component of \(x^{(n)}\) equal to it, and all others equal to \(1\). An additive basic neighbourhood of \(1\) restricts finitely many coordinates and has integral tails, so eventually contains \(x^{(n)}\). Each inverse has a nonintegral component at \(v_n\), and therefore none belongs to the additive open set \(K_\infty\times\prod_{v\nmid\infty}\mathcal O_v\) containing \(1\). Also none of the original idèles lies in (7), which is an idèle neighbourhood. This proves both claims. The example does not contradict Proposition 3.2: these idèles have norm \(q_{v_n}^{-1}\), not norm one.

**Solution 3.** At every real place require \(|x_v-1|<1\), at every complex place require ordinary \(|x_v-1|<1\), and at every finite place require \(x_v\in\mathcal O_v^\times\). This defines an idèle neighbourhood \(U\) of \(1\). Suppose a principal idèle \(a\in U\) has \(a\ne1\). At each finite place, the ultrametric inequality gives \(|a-1|_v\leq1\). At each archimedean place, \(|a-1|_v<1\); squaring the ordinary complex inequality preserves this strict inequality. There is at least one archimedean place, so \(\prod_v|a-1|_v<1\), contradicting the product formula for \(a-1\ne0\). Thus \(U\cap K^\times=\{1\}\), proving discreteness. Choose \(V\) with \(VV^{-1}\subset U\). Each translate \(gV\) contains at most one principal idèle; a point in the closure must equal that element, because otherwise a smaller neighbourhood could avoid it. Hence the subgroup is closed.

**Solution 4.** Use \(J_{K,\infty}^1\), whose diagonal intersection is \(\mathcal O_K^\times\). The ideal map identifies its quotient by units with the kernel of \(C_K^1\to\operatorname{Cl}_K\); the identification is open, and the kernel is closed, so the quotient is compact. The logarithm map onto the hyperplane (16) has compact kernel (22). On units, bounded logarithms put the units in a compact idèle set. Its intersection with discrete closed \(K^\times\) is finite. Thus the logarithmic subgroup \(\Gamma\) is discrete and closed, with finite kernel. The kernel is a finite group of units, hence consists of roots of unity; every root of unity lies in it. A complex embedding proves its cyclicity.

The compact unit quotient maps onto \(H/\Gamma\). Apply the lattice induction in Corollary 3.4: project away from a one-dimensional cyclic subgroup, reduce lifts into a bounded strip to preserve discreteness, and lift the resulting basis. This gives at most \(\dim H\) independent generators. A proper real span would allow a nonzero real linear functional on \(H/\Gamma\) with unbounded image, contradicting compactness. Thus the rank is exactly \(\dim H=r_1+r_2-1\). Lifting this basis splits units as \(\mu_K\times\mathbb Z^{r_1+r_2-1}\).

For \(S\)-units, use the finite valuation vector at \(S_f\). Its kernel is the ordinary unit group. Since the already proved class group has order \(h\), principal generators of \(\mathfrak p_v^h\) give \(h\) times each standard vector in the image. The image is therefore a finite-index subgroup of \(\mathbb Z^{S_f}\), free of rank \(\#S_f\). Lifting a basis splits off that many further infinite cyclic generators. The rank is \(r_1+r_2-1+\#S_f\), with the same torsion group \(\mu_K\).

## Prerequisites and further directions

The restricted product theorem is Proposition 1.1 of [Restricted products and profinite completions](NT-ADL-01.md). Additive discreteness, closedness and the box lemma are Theorem 2.2 and Lemma 2.5 of [The adèle ring of a number field](NT-ADL-02.md). These are proved there; only their stated number-field forms are used here.

Unique fractional ideal factorization and the equality of ideal exponents with local valuations are proved in Theorem 3.2 of Discrete valuation rings and Dedekind domains, using its Proposition 3.1 for the integer ring. Theorem 2.1 and Proposition 2.3, together with the number-field paragraph of Completions, the p-adic numbers and complete discretely valued fields, supply the completion valuation rings. The normalized product formula is Theorem 5.2 of Places of number fields in extensions and the product formula, with the conventions fixed in the preceding lesson. Sutherland, *Properties of Dedekind domains, factorization of ideals*, Theorem 3.11 and Corollary 3.13, and Milne, *Algebraic Number Theory*, Theorem 8.8, are scholarly references. No global class field theory, reciprocity map or classification of the connected component for arbitrary \(K\) is asserted here.

## References

- J. S. Milne, *Algebraic Number Theory*, version 3.08 (19 July 2020), [author-hosted notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 5, the unit theorem through the logarithmic embedding, with Theorem 5.11 for \(S\)-units, and Theorem 8.8, the product formula.
- A. V. Sutherland, *Properties of Dedekind domains, factorization of ideals*, MIT 18.785, Lecture 3 (15 September 2021), [lecture notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes3.pdf), Theorem 3.11 and Corollary 3.13: unique factorization of fractional ideals, with exponents given by the local valuations.
- A. V. Sutherland, *The idele group, profinite groups, infinite Galois theory*, MIT 18.785, Lecture 26 (1 December 2021), [MIT OpenCourseWare notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/resources/mit18_785f21_lec26/), Example 26.1 and Definition 26.2, pp.1–2; Lemma 26.8, pp.3–4; Theorem 26.9 and Remark 26.10, p.4. The independently written proofs above include the topology and closedness details used in the compactness argument.
- J. S. Milne, *Class Field Theory*, version 4.03 (6 August 2020), [author-hosted notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, §4, 4.1–4.4 and notes, pp.170–172, for the ideal map, content and arithmetic relation to norm-one compactness.
- H. Lenstra, *The Idèle Class Group*, [Leiden-hosted notes](https://websites.math.leidenuniv.nl/algebra/Lenstra-Idele.pdf), §1, Example 1.1, p.2, for the rational valuation-and-sign decomposition. The norm-one compactness proof here is Theorem 3.3, and concerns the quotient \(C_K^1\).
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations: With a View toward Trace Formulae*, [author-hosted draft dated 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §2.6, equations (2.15)–(2.19), pp.58–59, for the relation to adelic quotients. The general algebraic-group compactness theorem there is not a proof import here.
- J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) 1 (1995), 411–457, [author-hosted scan](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf), §3, proof of Proposition 12(2), p.427, for the finite rational split \(\mathbb A_f^\times=\mathbb Q_{>0}^\times\widehat{\mathbb Z}^{\times}\).

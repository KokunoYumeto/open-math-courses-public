# Subgroups, quotients and annihilators

**Lesson HA-LCA-10.** Self-checked by the writing AI.

Let \(G\) be an arbitrary locally compact Hausdorff abelian group, \(H\) a closed subgroup, \(Q=G/H\), and \(q:G\to Q\) the quotient map. Put \(\Gamma=\widehat G\). The quotient is LCA and \(q\) is open by HA-LCA-09, Lemma 6.0. The subgroup \(H\) is LCA: intersect a compact identity neighbourhood of \(G\) with the closed set \(H\). We use Pontryagin evaluation to identify every LCA group with its bidual, as proved in HA-LCA-09, Theorem 2.1. Fourier transforms have negative sign.

For a subset \(S\subseteq G\), its annihilator is
\[
 S^\perp=\{\gamma\in\Gamma:\gamma(s)=1\text{ for every }s\in S\}.
 \tag{1}
\]
For a subset of \(\Gamma\), use the same notation for its annihilator in \(G\). Each is a closed subgroup: it is the intersection of the closed kernels of the appropriate continuous evaluations. Evaluation continuity and functoriality were proved in HA-LCA-09, Proposition 5.1.

The free mathematical sources are Dikran Dikranjan, [*Introduction to Topological Groups*](https://users.dimi.uniud.it/~dikran.dikranjan/ITG.pdf), version 26 February 2018, Lemma 7.2.5, §§8.1–8.2, Lemma 12.3.5 and §§12.4.2, 12.5; D. H. Fremlin, [*Measure Theory*, §§443P–Q](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex), version 14 January 2013; Pekka Salmi, [*Idempotent states on locally compact groups and quantum groups*, §§2–3](https://arxiv.org/pdf/1209.0314v1), 3 September 2012; and Keith Conrad, [*The Character Group of \(\mathbb Q\)*, §2 and Appendix A](https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf), for the \(p\)-adic example. The topology notes' contents have stale page numbers; the relevant printed pages for §§8.1–8.2 and §12.5 are 51–54 and 97.

Written by GPT-6 Astra (OpenAI), Ultra, October 2026. Original text: public domain (CC0). Fremlin's copyright 2001 and original notices are retained in the unchanged volume 4 source package. The other cited works are linked, not reproduced.

## 1. Compact lifts and double annihilation

<a id="ha-lca-10-lemma-1-1"></a>
**Lemma 1.1 — Compact lifting.** Every compact subset \(E\subseteq Q\) is \(q(K)\) for some compact \(K\subseteq G\).

**Proof.** Choose a compact identity neighbourhood \(C\) in \(G\). The sets \(q(x+\operatorname{int}C)\), as \(x\) varies, cover \(Q\), because \(q\) is open and surjective. Finitely many, with representatives \(x_1,\ldots,x_r\), cover \(E\). Then
\[
 K=\left(\bigcup_{j=1}^r(x_j+C)\right)\cap q^{-1}(E)
\]
is compact: \(E\) is closed in the Hausdorff quotient, so this is a closed subset of a finite union of compact sets. It maps onto exactly \(E\). For empty \(E\), take empty \(K\). \(\square\)

<a id="ha-lca-10-proposition-1-2"></a>
**Proposition 1.2 — Double annihilation.** For every subgroup \(S\le G\),
\[
 (S^\perp)^\perp=\overline S.
 \tag{2}
\]

**Proof.** Every character trivial on \(S\) is trivial on its closure, so the right side is contained in the left. If \(x\notin\overline S\), then \(x+\overline S\) is a nonzero point of the LCA quotient \(G/\overline S\). Character separation, HA-LCA-05, Corollary 4.2, gives a quotient character not equal to one there. Its pullback to \(G\) is trivial on \(S\) and not on \(x\). Thus \(x\notin(S^\perp)^\perp\). \(\square\)

## 2. Both topological duality identifications

<a id="ha-lca-10-theorem-2-1"></a>
**Theorem 2.1 — Closed subgroups and quotients.** Set \(A=H^\perp\). The maps
\[
 \Phi:\widehat Q\longrightarrow A,\quad \Phi(\eta)=\eta\circ q,
 \qquad
 \Psi:\Gamma/A\longrightarrow\widehat H,\quad
 \Psi(\gamma A)=\gamma|_H
 \tag{3}
\]
are isomorphisms of topological groups. In particular restriction \(\Gamma\to\widehat H\) is an open surjection with kernel \(A\).

**Proof.** Character descent through the open quotient, HA-LCA-09, Lemma 6.0, makes \(\Phi\) a bijection onto \(A\). Functoriality makes it continuous. If \(E\subseteq Q\) is compact, choose a compact lift \(K\) from Lemma 1.1. Then
\[
 \sup_{z\in E}|\eta(z)-\zeta(z)|
 =\sup_{x\in K}|\Phi(\eta)(x)-\Phi(\zeta)(x)|.
 \tag{4}
\]
Thus the inverse is continuous for compact-open topologies, proving the first assertion.

Apply that assertion to the closed subgroup \(A\) of \(\Gamma\). It identifies \(\widehat{\Gamma/A}\) topologically with the annihilator of \(A\) in \(\widehat\Gamma\). Under evaluation \(J_G\), that annihilator is \(J_G(H)\), by Proposition 1.2. Therefore
\[
 \theta:H\longrightarrow\widehat{\Gamma/A},
 \qquad \theta(h)(\gamma A)=\gamma(h),
\]
is a topological isomorphism. A topological isomorphism has a topological dual inverse: apply the functorial composition rule to the map and its inverse. Consequently the composite
\[
 \Gamma/A\xrightarrow{\,J_{\Gamma/A}\,}
       \widehat{\widehat{\Gamma/A}}
       \xrightarrow{\,\widehat\theta\,}\widehat H
\]
is a topological isomorphism. Evaluating it at \(h\in H\) gives \(\gamma(h)\), so this composite is precisely \(\Psi\). Restriction is the composition of the open quotient \(\Gamma\to\Gamma/A\) with \(\Psi\), hence is open and surjective. Its kernel is \(A\) by definition. \(\square\)

<a id="ha-lca-10-corollary-2-2"></a>
**Corollary 2.2 — Extension and the closed-subgroup correspondence.** Every continuous character of \(H\) extends continuously to \(G\). Annihilation is an inclusion-reversing bijection between the closed subgroups of \(G\) and those of \(\Gamma\). Moreover,
\[
 H\text{ open}\ \Longleftrightarrow\ H^\perp\text{ compact},
 \qquad
 H\text{ compact}\ \Longleftrightarrow\ H^\perp\text{ open}.
 \tag{5}
\]

**Proof.** Restriction is surjective by Theorem 2.1. If \(H_1\subseteq H_2\), a character trivial on \(H_2\) is trivial on \(H_1\), proving reversal of inclusion. Proposition 1.2, also applied with base group \(\Gamma\), says that the two annihilator operations are inverse on closed subgroups.

The subgroup \(H\) is open exactly when \(Q\) is discrete: the identity singleton is open in \(Q\) exactly when its inverse image \(H\) is open in \(G\), and translate this condition to all points. By HA-LCA-09, Corollary 4.4, \(Q\) is discrete exactly when \(\widehat Q\cong H^\perp\) is compact. Applying this equivalence with base \(\Gamma\) and subgroup \(H^\perp\), and using its double annihilator \(H\), gives the second equivalence. \(\square\)

<a id="ha-lca-10-corollary-2-3"></a>
**Corollary 2.3 — A subgroup need not be closed for character extension.** If \(S\le G\) has its relative topology, every continuous character \(\chi:S\to\mathbb T\) extends to a continuous character of \(G\).

**Proof.** Put \(K=\overline S\). We first extend to \(K\). For any \(x\in K\), choose a net \(s_i\in S\) converging to \(x\), by the neighbourhood-directed construction in HA-LCA-09, Exercise 6.2. Its values \(\chi(s_i)\) are Cauchy in the ordinary circle metric. Indeed, given \(\varepsilon>0\), continuity at zero gives a neighbourhood \(U\) in \(K\) with \(|\chi(s)-1|<\varepsilon\) for \(s\in U\cap S\); eventually \(s_i-s_j\in U\), so
\(|\chi(s_i)-\chi(s_j)|<\varepsilon\).

A Cauchy net in \(\mathbb T\) converges. To prove this without a completion theorem, the closures of its tails have the finite-intersection property in the compact circle, and therefore have a common point \(z\). For every \(\varepsilon>0\), a sufficiently late tail has diameter less than \(\varepsilon\). Its closure contains \(z\), so every member of that tail lies within \(\varepsilon\) of \(z\). This proves convergence; the Hausdorff property proves uniqueness.

If \(t_j\to x\) is another approximating net, then on the product directed set \(s_i-t_j\to0\). Continuity of \(\chi\) at zero gives \(\chi(s_i)\overline{\chi(t_j)}\to1\), so both limits coincide. Define \(\bar\chi(x)\) to be this limit. Taking product nets converging to \(x\) and \(y\) proves
\(\bar\chi(x+y)=\bar\chi(x)\bar\chi(y)\); a constant net proves extension.

To check continuity at zero, fix \(\varepsilon>0\). Choose an open identity neighbourhood \(U\) in \(K\) such that \(|\chi(s)-1|<\varepsilon/2\) for \(s\in U\cap S\). For \(x\in U\), an approximating net is eventually in \(U\), so \(|\bar\chi(x)-1|\le\varepsilon/2<\varepsilon\). This proves continuity at zero and hence everywhere by the character identity. The closure \(K\) is an LCA closed subgroup of \(G\). Corollary 2.2 now extends \(\bar\chi\) to \(G\). \(\square\)

<a id="ha-lca-10-corollary-2-4"></a>
**Corollary 2.4 — Strict exact sequences.** A sequence
\[
 0\longrightarrow H\longrightarrow G\longrightarrow Q\longrightarrow0
 \tag{6}
\]
is called strictly exact if its first map identifies \(H\) with a closed subgroup of \(G\) and its second identifies \(Q\) with the topological quotient. Duality reverses it to a strictly exact sequence
\[
 0\longrightarrow\widehat Q\longrightarrow\widehat G
       \longrightarrow\widehat H\longrightarrow0.
 \tag{7}
\]

**Proof.** Transport the sequence along its given topological identifications to \(H\subseteq G\) and \(Q=G/H\). Theorem 2.1 identifies the image of \(\widehat Q\) topologically with the closed subgroup \(H^\perp\), which is exactly the kernel of restriction, and identifies the restriction quotient with \(\widehat H\). These facts are precisely strict exactness of (7). Functoriality carries them back through the original identifications. \(\square\)

## 3. Averaging continuous functions

Fix Haar measures \(dx\) on \(G\) and \(dh\) on \(H\), both on the full complete locally determined domains. For \(f\in C_c(G)\), define
\[
 Pf(q(x))=\int_Hf(x+h)\,dh.
 \tag{8}
\]

<a id="ha-lca-10-lemma-3-1"></a>
**Lemma 3.1 — Positive lifts.** Formula (8) defines a positive linear map \(P:C_c(G)\to C_c(Q)\), and
\(\operatorname{supp}Pf\subseteq q(\operatorname{supp}f)\).
For each compact \(E\subseteq Q\) there is a nonnegative \(b\in C_c(G)\) with \(Pb=1\) on \(E\). The map \(P\) is onto, and every nonnegative member of \(C_c(Q)\) has a nonnegative lift.

**Proof.** For fixed \(x\), the integrand is continuous on \(H\) with compact support contained in \(H\cap(\operatorname{supp}f-x)\). Changing \(x\) by an element of \(H\) preserves the integral by translation invariance of \(dh\), so the definition depends only on \(q(x)\).

To prove continuity, restrict \(x\) to a compact neighbourhood \(C\) of a fixed \(x_0\). All the relevant \(h\)'s lie in the fixed compact set
\(L=H\cap(\operatorname{supp}f-C)\).
Uniform translation continuity of \(f\), proved in the general Haar reading, Lemma 1.1, gives
\[
 |Pf(q(x))-Pf(q(x_0))|
 \le dh(L)\sup_{h\in H}|f(x+h)-f(x_0+h)|\longrightarrow0.
\]
Thus \(Pf\circ q\) is continuous; the quotient property makes \(Pf\) continuous. If a coset misses \(\operatorname{supp}f\), its integral is zero. The set \(q(\operatorname{supp}f)\) is compact and hence closed, proving the support assertion. Positivity and linearity follow from the integral.

For each \(z\in Q\), choose \(x\) above it and a nonnegative \(u_z\in C_c(G)\) with \(u_z(x)>0\), using the Radon reading, Lemma 1.3. Haar full support on \(H\) implies \(Pu_z(z)>0\). For compact \(E\), finitely many open sets \(\{Pu_z>0\}\) cover \(E\); the sum \(u\) of their functions satisfies \(Pu>0\) on \(E\). In the open set \(O=\{Pu>0\}\), choose \(v\in C_c(Q)\) with \(0\le v\le1\), \(v=1\) on \(E\), and support inside \(O\). Then
\[
 b(x)=
 \begin{cases}
 u(x)v(q(x))/Pu(q(x)),&q(x)\in O,\\
 0,&q(x)\notin O
 \end{cases}
\]
is nonnegative and continuous, with support in \(\operatorname{supp}u\). Continuity across the boundary follows because \(\operatorname{supp}v\) is contained in \(O\). Direct integration gives \(Pb=v\), hence \(Pb=1\) on \(E\). If \(E\) is empty take \(b=0\).

Given \(F\in C_c(Q)\), choose such a \(b\) for \(E=\operatorname{supp}F\). The function \(f(x)=b(x)F(q(x))\) belongs to \(C_c(G)\), and \(Pf=F\cdot Pb=F\). If \(F\ge0\), then \(f\ge0\). \(\square\)

<a id="ha-lca-10-lemma-3-2"></a>
**Lemma 3.2 — Directed continuous suprema.** Let \(m\) be a positive measure on an LCH space, finite on compact sets and inner regular by compact sets on all its measurable sets. Let \(\mathcal U\) be an upward-directed family of nonnegative continuous functions, and put \(v=\sup_{u\in\mathcal U}u\). Then \(v\) is lower semicontinuous, hence Borel measurable, and
\[
 \int v\,dm=\sup_{u\in\mathcal U}\int u\,dm.
 \tag{9}
\]

**Proof.** For every real \(a\), \(\{v>a\}=\bigcup_{u\in\mathcal U}\{u>a\}\) is open. One inequality in (9) follows from \(u\le v\).

For the other, fix \(0<b<\int v\,dm\). By the definition of the positive integral as a supremum of simple integrals, and then compact inner approximation of the finitely many level sets, there are disjoint compact sets \(K_1,\ldots,K_r\) and constants \(a_j>0\) such that \(a_j<v\) on \(K_j\) and
\(\sum_j a_j m(K_j)>b\).
Here is the strict-inequality detail: first take a nonnegative finite-valued simple minorant whose integral exceeds \(b\). If one of its positive level sets has infinite measure, compact inner regularity allows a compact subset with an arbitrarily large finite measure, and it alone can exceed \(b\). Otherwise approximate each positive level set from within by compact sets, so the finite sum still exceeds \(b\). Decrease all its finitely many positive coefficients by a common factor less than and sufficiently close to one. They are now strictly below \(v\) on the chosen compact sets and their integral still exceeds \(b\).

For each \(x\in K_j\), some \(u_x\in\mathcal U\) has \(u_x(x)>a_j\). The open sets \(\{u_x>a_j\}\) cover \(K_j\). Choose finite subcovers for all the \(K_j\)'s. Directedness provides one member \(u\) above the finitely many functions selected. Thus \(u>a_j\) on \(K_j\), and \(\int u\,dm>b\). Let \(b\) increase to \(\int v\,dm\), allowing the latter to be infinite. If that integral is zero there was nothing to prove. \(\square\)

## 4. Weil's formula and its precise \(L^1\) meaning

<a id="ha-lca-10-theorem-4-1"></a>
**Theorem 4.1 — Quotient integration.** There is a unique Haar measure \(dz\) on \(Q\) such that
\[
 \int_G f(x)\,dx=\int_Q Pf(z)\,dz
       =\int_Q\int_H f(x+h)\,dh\,dz,\qquad z=q(x),
 \tag{10}
\]
for every \(f\in C_c(G)\).

For arbitrary \(G\), \(P\) extends uniquely to a positive contraction
\[
 P_1:L^1(G)\longrightarrow L^1(Q),\qquad
 \int_Q P_1[f]\,dz=\int_G f\,dx.
 \tag{11}
\]
Every \(L^1\) class has a Borel representative \(f_0\) which is zero outside an open sigma-compact subgroup. For any such representative, the coset integral in (8) exists absolutely for almost every coset, is measurable there, and represents \(P_1[f]\). Any two such representatives give the same result almost everywhere. If \(G\) is sigma-compact, this assertion holds for every representative measurable on its completed Haar domain.

**Proof.** Choose initially any Haar measure \(dz_0\) on the LCA quotient. Lemma 3.1 makes
\(I(f)=\int_Q Pf\,dz_0\) a positive linear functional on \(C_c(G)\). It is nonzero: for nonzero \(f\ge0\), the proof of that lemma gives \(Pf>0\) at some point, hence on an open set of positive quotient Haar measure. It is invariant under translations, because
\[
 P(L_a f)(z)=Pf(z-q(a)).
\]
HA-LCA-07, Lemma 1.0 proves that every such invariant, nonzero, positive functional is integration against a Haar measure on the full domain. Haar uniqueness therefore gives \(I(f)=c\int_G f\,dx\) for \(c>0\). Set \(dz=c^{-1}dz_0\). This proves (10). Since \(P\) maps onto \(C_c(Q)\), (10) determines integration of every \(C_c(Q)\) function and hence the Haar measure uniquely, by the general Haar reading, Lemma 3.2.

We next justify slicing beyond continuous functions. For a coset \(z=q(x)\) and a Borel set \(E\subseteq G\), put
\[
 \nu_z(E)=dh\{h\in H:x+h\in E\}.
\]
The value is independent of the representative \(x\). Translation identifies this measure with \(dh\) on the closed coset \(x+H\), with zero mass outside that coset. In particular it is finite on compact sets and inner regular by compact sets: pull a Borel set back to \(H\), approximate there by compact sets, and translate those sets into \(G\).

For an open \(O\subseteq G\), let
\(\mathcal V_O=\{g\in C_c(G):0\le g\le1_O\}\).
Compact inner approximation on the coset and the cutoff lemma give
\[
 \nu_z(O)=\sup_{g\in\mathcal V_O}Pg(z).
 \tag{12}
\]
Indeed a compact part of \(O\cap(x+H)\) can be assigned value one by a continuous cutoff supported in \(O\). The family \(\mathcal V_O\) is directed under pointwise maximum, so its images under the positive operator \(P\) are directed. Lemma 3.2 and (10) give
\[
 \int_Q\nu_z(O)\,dz
 =\sup_{g\in\mathcal V_O}\int_Q Pg\,dz
 =\sup_{g\in\mathcal V_O}\int_Gg\,dx=dx(O).
 \tag{13}
\]
The last equality again follows by compact inner approximation and cutoffs. Equation (12) also shows that \(z\mapsto\nu_z(O)\) is lower semicontinuous.

Fix a relatively compact open \(U\subseteq G\). Then \(dx(U)<\infty\) and each \(\nu_z(U)<\infty\). Among Borel subsets \(E\) of \(U\), the conditions
\[
 z\mapsto\nu_z(E)\text{ is measurable},\qquad
 \int_Q\nu_z(E)\,dz=dx(E)
 \tag{14}
\]
hold for \(E=U\), for relative open sets by (13), for complements within \(U\) by subtraction from the finite value \(\nu_z(U)\), and for disjoint countable unions by monotone convergence. Thus they form a Dynkin class containing the intersection-closed family of relative open sets. The proved integration reading, Lemma 4.1, gives (14) for every Borel subset of \(U\).

If \(N\subseteq U\) is Borel and \(dx(N)=0\), (14) makes \(\nu_z(N)=0\) outside a quotient null set. Every subset of \(N\) is then measurable with zero measure on those cosets, by completeness of Haar measure on \(H\). This proves (14), with arbitrary values assigned on that quotient null set, for every completed-measurable subset of \(U\). The full Haar domain on relatively compact sets is exactly this ordinary local completion, by the general Haar reading, Theorem 3.1.

A sigma-compact subset of \(G\) is covered by countably many relatively compact open sets: cover each compact part by finitely many such neighbourhoods. Partition their union into disjoint Borel pieces, each contained in one of these open sets. Applying (14) on the pieces and using monotone convergence proves the set formula for all completed-measurable sets contained in their union. Positive simple approximation and monotone convergence then give the integral formula for every nonnegative measurable function zero outside that union. Applying the formula to \(|f_0|\) and to the positive and negative real and imaginary parts gives (10) for every integrable such \(f_0\). In particular its absolute coset integrals are finite outside a quotient null set. This construction also proves measurability of the integral, using one countable union of exceptional null sets.

Every \(L^1(G)\) class has a Borel representative zero outside an open sigma-compact subgroup, by the general Haar reading, Lemma 5.1. For two such representatives \(f_0,g_0\), their supports lie in a union of two sigma-compact sets, so the preceding result applied to \(|f_0-g_0|\) proves
\[
 \int_Q\int_H|f_0(x+h)-g_0(x+h)|\,dh\,dz
       =\|f_0-g_0\|_1.
 \tag{15}
\]
Consequently coset integration gives a well-defined contraction on classes; the same formula proves linearity, positivity and (11). Its uniqueness follows from \(C_c\)-density in \(L^1(G)\), also proved in that reading. If \(G\) is sigma-compact, the countable-cover argument covers all of \(G\), including every measurable representative and its null modifications. \(\square\)

<a id="ha-lca-10-example-4-0"></a>
**Example 4.0 — Why the representative condition is necessary.** With the full Haar domains, the final assertion of Theorem 4.1 cannot be extended to arbitrary representatives when \(G\) is not sigma-compact.

**Proof.** Give the first copy of \(\mathbb R\) the discrete topology and put
\[
 G=\mathbb R_d\times\mathbb R,\qquad
 H=\mathbb R_d\times\{0\},\qquad Q=\mathbb R.
\]
Use counting measure on \(H\) and Lebesgue measure on each open component \(\{t\}\times\mathbb R\) of \(G\). The full Haar measure of \(G\) is their sum, as in the general Haar reading, Theorem 3.1. Compact sets meet only finitely many components: project to the discrete first factor and use compactness. Thus the formula on \(C_c(G)\) is a finite sum of Lebesgue integrals, and (10) makes the quotient measure precisely Lebesgue measure.

The diagonal \(N=\{(t,t):t\in\mathbb R\}\) is closed: its intersection with each open component is a closed singleton, so its complement is open. Each component section has Lebesgue measure zero, hence \(dx(N)=0\). Therefore \(1_N\) and zero represent the same \(L^1(G)\) class. But for every \(y\in Q\),
\[
 \int_H1_N((0,y)+h)\,dh
       =\sum_{t\in\mathbb R}1_N(t,y)=1.
 \tag{16}
\]
This cannot represent \(P_1[0]=0\). The diagonal is not contained in any open sigma-compact subgroup, since its projection to \(\mathbb R_d\) is uncountable whereas a countable union of compact sets has countable such projection. Theorem 4.1 applies to zero as the permitted representative of this class. This example proves why arbitrary full-domain null changes cannot be used for slicing. \(\square\)

<a id="ha-lca-10-proposition-4-2"></a>
**Proposition 4.2 — Idempotent probability measures.** A Radon probability measure \(\mu\) on an LCA group satisfies \(\mu*\mu=\mu\) if and only if it is normalized Haar measure on a compact subgroup, regarded as a measure on \(G\).

**Proof.** Suppose \(\mu*\mu=\mu\). The finite-measure convolution law from the product reading, Theorem 3.3 gives \(\widehat\mu^2=\widehat\mu\), so every value is zero or one. Continuity of the Fourier–Stieltjes transform, proved in HA-LCA-03, Theorem 4.3, makes
\(A=\{\gamma:\widehat\mu(\gamma)=1\}\) both open and closed. It contains the identity since \(\mu(G)=1\). For \(\gamma\in A\),
\[
 \int_G|\gamma(x)-1|^2\,d\mu(x)
       =2-2\operatorname{Re}\widehat\mu(\gamma)=0.
\]
Thus \(\gamma=1\) \(\mu\)-almost everywhere. Two such equalities hold simultaneously outside the union of their two null sets, so \(\gamma\eta^{-1}=1\) almost everywhere whenever \(\gamma,\eta\in A\). Hence \(A\) is a subgroup. By Corollary 2.2, \(K=A^\perp\) is compact; by Proposition 1.2, \(K^\perp=A\).

Let \(m_K\) be Haar probability measure on \(K\), pushed to \(G\). Its transform equals one on \(K^\perp\). If \(\gamma\notin K^\perp\), choose \(k\in K\) with \(\gamma(k)\ne1\). Translation of its character integral multiplies that integral by \(\overline{\gamma(k)}\) and leaves it unchanged, so it is zero. Thus \(\widehat{m_K}=1_A=\widehat\mu\). HA-LCA-09, Corollary 4.2 gives \(\mu=m_K\).

Conversely the same character-integral computation shows that \(\widehat{m_K}\) is an indicator. Its square equals itself, so the convolution law and uniqueness give \(m_K*m_K=m_K\). The pushforward is a finite Radon probability measure by the product reading, Proposition 3.1. \(\square\)

<a id="ha-lca-10-example-4-3"></a>
**Example 4.3 — The positivity hypothesis.** Uniform measure on a finite subgroup, and normalized Haar measure on any compact subgroup, are idempotent probability laws. Complex idempotent measures need not be probability laws.

**Proof.** On \(\mathbb Z/6\mathbb Z\), direct addition of the four equally weighted pairs in \(\{0,3\}^2\) gives
\[
 \left(\tfrac12(\delta_0+\delta_3)\right)*
 \left(\tfrac12(\delta_0+\delta_3)\right)
       =\tfrac12(\delta_0+\delta_3).
\]
Proposition 4.2 also gives uniform measures on the \(n\)-th roots of unity and Haar probability on \(\mathbb T\). A compact subgroup of \(\mathbb R\) has no nonzero member, since all integer multiples of such a member would be unbounded, whereas compact subsets of \(\mathbb R\) are bounded by the Banach reading, Lemma 1.1. Thus on \(\mathbb R\) only \(\delta_0\) is an idempotent probability measure.

For a complex example on \(\mathbb Z/3\mathbb Z\), put \(\zeta=e^{2\pi i/3}\) and assign mass \((1+\zeta^x)/3\) to \(x=0,1,2\). The finite orthogonality formula in HA-LCA-01, Theorem 2.1 gives Fourier values \(1,1,0\). The convolution law and finite Fourier injectivity make this measure idempotent. Its mass at \(1\) is not real: if the primitive cube root \(\zeta\) were real, it would be \(1\) or \(-1\); neither is a primitive cube root. Thus it is not a positive measure, despite having total mass one. \(\square\)

## 5. Compatible dual measures

Use the measures \(dx,dh,dz\) fixed by Theorem 4.1. On \(\Gamma=\widehat G\), use the Haar measure \(d\xi\) dual to \(dx\). Transport the measure dual to \(dz\) to \(A=H^\perp\) through \(\Phi\), calling it \(da\). Transport the measure dual to \(dh\) to \(\Gamma/A\) through \(\Psi^{-1}\), calling it \(d\eta\).

<a id="ha-lca-10-lemma-5-0"></a>
**Lemma 5.0 — Averaging and convolution.** For \(u,v\in C_c(G)\),
\[
 P(u*v)=Pu*Pv,\qquad P\widetilde u=\widetilde{Pu},
 \qquad \widehat{Pu}(a)=\widehat u(a)\quad(a\in A).
 \tag{17}
\]
In the last equality \(a\) on the left denotes the corresponding character of \(Q\).

**Proof.** For fixed \(x\), in the double integral
\(\int_H\int_Gu(y)v(x+h-y)\,dy\,dh\),
the integrand is supported in
\[
 y\in\operatorname{supp}u,\qquad
 h\in H\cap(\operatorname{supp}v-x+\operatorname{supp}u).
\]
Both are compact. The finite Radon product and Fubini theorem proved in the product reading, Theorem 2.2 therefore allow reversal of integration. This gives
\[
 P(u*v)(q(x))=\int_Gu(y)Pv(q(x)-q(y))\,dy.
\]
The integrand on the right is in \(C_c(G)\). Apply (10) to it and use constancy of its second factor on each \(H\)-coset. The result is
\(\int_Q Pu(z)Pv(q(x)-z)\,dz\), proving the first equality.
Inversion in the abelian Haar measure \(dh\) gives the second. For the last, the function \(u(x)\overline{a(x)}\) is in \(C_c(G)\), and \(a\) is constant on \(H\)-cosets. Apply (10) once more to obtain the stated transform identity. \(\square\)

<a id="ha-lca-10-proposition-5-1"></a>
**Proposition 5.1 — Dual Weil normalization.** The three dual measures just specified satisfy Weil's formula on \(\Gamma\):
\[
 \int_\Gamma F(\xi)\,d\xi
 =\int_{\Gamma/A}\int_A F(\gamma a)\,da\,d\eta(\gamma A).
 \tag{18}
\]
This holds on \(C_c(\Gamma)\) and with the \(L^1\)-class interpretation of Theorem 4.1.

**Proof.** Apply Theorem 4.1 to \(\Gamma\) and its closed subgroup \(A\), keeping \(d\xi\) and \(da\) fixed. It gives a quotient Haar measure \(d\eta_0\). Since \(d\eta\) is also Haar, uniqueness gives \(d\eta_0=c\,d\eta\) for \(c>0\). We will determine \(c\).

Take a nonzero \(u\in C_c(G)\) and \(f=u*\widetilde u\). Then \(f\in C_c(G)\) is of positive type, \(f(0)=\|u\|_2^2>0\), and
\(\widehat f=|\widehat u|^2\ge0\).
The positive autocorrelation and transform identities are HA-LCA-04, Proposition 2.2 and HA-LCA-03, Theorem 3.1. In particular \(f\in B^1(G)\).

For every \(\gamma\in\Gamma\), the function \(\overline\gamma f\) is the autocorrelation of \(\overline\gamma u\), by substitution in convolution. Lemma 5.0 therefore makes
\(P(\overline\gamma f)\) a \(C_c(Q)\) positive autocorrelation. Its transform at \(a\in A\) is \(\widehat f(\gamma a)\), again by (17). Apply HA-LCA-07, Theorem 2.1 on \(Q\) at its identity to get, for every \(\gamma\),
\[
 \int_A\widehat f(\gamma a)\,da
 =P(\overline\gamma f)(0)
 =\int_H f(h)\overline{\gamma(h)}\,dh
 =\widehat{\,f|_H\,}(\gamma|_H).
 \tag{19}
\]
All these integrals are finite. The function \(f|_H\) is continuous, compactly supported and of positive type, as its defining finite matrices are among those for \(f\). Thus it is in \(B^1(H)\) by Bochner's theorem.

Inversion on \(G\) gives \(\widehat f\in L^1(\Gamma)\) and \(\int_\Gamma\widehat f\,d\xi=f(0)\). Moreover \(\widehat f\in C_0(\Gamma)\), by the earlier general \(L^1\) transform theorem. Its nonzero set is the countable union of compact sets \(\{|\widehat f|\ge1/n\}\), so it is an eligible representative for Theorem 4.1 on \(\Gamma\). Its coset integrals are the everywhere finite values in (19). Hence
\[
 f(0)=\int_{\Gamma/A}\widehat{\,f|_H\,}(\Psi(\gamma A))\,d\eta_0
 =c\int_{\widehat H}\widehat{\,f|_H\,}(\eta)\,d\widehat h(\eta)
 =c f(0),
\]
where \(d\widehat h\) is the measure dual to \(dh\), and the last equality is \(B^1\) inversion on \(H\). Since \(f(0)>0\), \(c=1\). This proves (18) with exactly the proposed measures. \(\square\)

## 6. Euclidean subgroups and a \(p\)-adic example

<a id="ha-lca-10-lemma-6-0"></a>
**Lemma 6.0 — Euclidean tools and linear volume.** Finite-dimensional subspaces of \(\mathbb R^n\) are closed and have continuous orthogonal projections. Every bounded sequence in \(\mathbb R^n\) has a convergent subsequence. If \(A\) is an invertible real \(n\times n\) matrix and \(E\) is a Borel set, then
\[
 \operatorname{vol}(AE)=|\det A|\operatorname{vol}(E).
 \tag{20}
\]

**Proof.** For a subspace, choose successive vectors outside the span already chosen. Gaussian elimination shows that a linearly independent family in \(\mathbb R^n\) has at most \(n\) members: in a matrix of their coordinates, each independent new column requires a new pivot row. Thus the process ends with a finite basis. Starting from that basis, successively replace a vector \(v\) by
\(v-\sum_j(v\cdot e_j)e_j\), where the \(e_j\)'s are the orthonormal vectors already obtained, and divide by its nonzero length. The remainder is nonzero by linear independence, and its dot products with all preceding \(e_j\)'s vanish by expansion. Continue with vectors outside the span to obtain an orthonormal basis of \(\mathbb R^n\). Orthogonal projection onto the original subspace is the finite continuous sum
\(x\mapsto\sum_j(x\cdot e_j)e_j\).
The subspace is the zero set of the complementary projection, hence closed.

For the subsequence assertion, place a bounded sequence in a closed cube. Bisect each side and choose one of the finitely many resulting closed subcubes containing infinitely many terms. Repeat inside that cube. Choose successive terms, with strictly increasing indices, from these nested cubes. Their diameters tend to zero, so the selected coordinates are Cauchy and converge by completeness of \(\mathbb R\). This proves the assertion, including for sequences on a closed bounded subset.

Lebesgue measure on \(\mathbb R^n\) is the product of its one-dimensional measures, as proved in HA-LCA-07, Proposition 3.2. The full-Borel sigma-finite Fubini theorem is the integration reading, Theorem 4.4. Interchanging coordinates preserves that measure. Multiplying one coordinate by \(a\ne0\) multiplies measure by \(|a|\), by the one-dimensional affine-substitution formula proved in HA-LCA-02, Lemma 3.3 and Fubini. Replacing \(x_i\) by \(x_i+t x_j\), \(i\ne j\), preserves measure: hold the other coordinates fixed and apply translation invariance to the \(x_i\)-section, then Fubini.

For clarity, take the determinant to be its finite permutation formula
\(\det A=\sum_{\sigma}\operatorname{sgn}(\sigma)\prod_i A_{i,\sigma(i)}\).
It is linear in each row, changes sign on exchanging two rows (reindex the permutations), and is zero with two equal rows (pair the terms under their transposition). Consequently row addition leaves it unchanged, a row scaling by \(a\) multiplies it by \(a\), and a row interchange changes its sign. Gaussian elimination reduces an invertible matrix to the identity by these operations: choose a nonzero entry in the first column as pivot, scale it to one, clear the other entries in that column, and continue on the remaining invertible submatrix. Back-substitution clears entries above the pivots. Each operation on the output coordinates has the volume factor and the absolute determinant factor just calculated. Applying the resulting finite chain to \(AE\) yields (20). This argument also proves that the determinant of an invertible matrix is nonzero.

We will need two consequences. Replacing \(\sigma\) by \(\sigma^{-1}\) in the determinant sum gives \(\det(A^T)=\det A\). Applying (20) to \(A\) and then \(A^{-1}\) on the unit cube gives
\[
 |\det(A^{-1})|=|\det A|^{-1}.
 \tag{21}
\]
Thus no additional change-of-variables or determinant identity will be needed below. \(\square\)

<a id="ha-lca-10-proposition-6-1"></a>
**Proposition 6.1 — Closed Euclidean subgroups.** Every closed subgroup \(H\le\mathbb R^n\) has a decomposition
\[
 H=V\oplus\Lambda,\qquad
 \Lambda=\mathbb Z v_1+\cdots+\mathbb Z v_r\subseteq V^\perp,
 \tag{22}
\]
where \(V\) is a vector subspace and the \(v_j\)'s are real-linearly independent. The addition map \(V\times\Lambda\to H\) is a topological isomorphism, with \(\Lambda\) discrete. Here \(r+\dim V\le n\).

**Proof.** First consider a subgroup \(D\le\mathbb R\) for which zero is isolated. If \(D\ne0\), its positive elements have a positive infimum \(a\). A sequence of positive members decreasing to this infimum is eventually constant: two sufficiently late terms differ in \(D\) by less than a fixed isolation radius, so their difference must be zero. Thus \(a\in D\), and it is the least positive member. For any \(d\in D\), choose an integer \(k\) with \(0\le d-ka<a\). The remainder belongs to \(D\), so it is zero. Hence \(D=a\mathbb Z\).

A discrete subgroup of \(\mathbb R^n\) is closed by HA-LCA-09, Lemma 1.2, since a discrete group is locally compact. Its intersection with any compact set is finite: that intersection is compact and discrete, so its singleton cover has a finite subcover.

We prove by induction on \(n\) that every discrete subgroup \(D\) has an integer basis consisting of real-linearly independent vectors. The assertion for \(n=1\) was just proved. The zero subgroup in any dimension has the empty basis. Otherwise choose nonzero \(d\in D\), and put \(L=\mathbb R d\). The one-dimensional argument gives \(D\cap L=\mathbb Z a\) for a nonzero \(a\). Let \(\pi\) be orthogonal projection onto \(L^\perp\).

The subgroup \(\pi(D)\) is discrete. If not, there would be \(d_j\in D\) with \(0\ne\pi(d_j)\to0\). Subtract integer multiples of \(a\) to write the modified points as
\(d'_j=t_j a+\pi(d_j)\), with \(0\le t_j<1\).
They lie eventually in a fixed compact set, for instance \(\{ta+w:0\le t\le1,\ w\in L^\perp,\ \|w\|\le1\}\); compactness follows from the proved closed bounded Euclidean compactness in the Banach reading, Lemma 1.1, or the finite-product argument there. Only finitely many elements of \(D\) lie in that set, so their nonzero projections cannot converge to zero. This contradiction proves discreteness.

Apply the induction hypothesis in \(L^\perp\). Lift its linearly independent integer basis \(w_2,\ldots,w_r\) to \(v_2,\ldots,v_r\in D\), and put \(v_1=a\). Every element of \(D\), after subtracting an integer combination of these lifts, projects to zero and hence is an integer multiple of \(a\). The vectors are real-linearly independent: project any linear relation first, then use \(a\ne0\). This proves the discrete assertion.

Now choose a vector subspace \(V\subseteq H\) of maximal possible dimension. Such a dimension exists among the integers \(0,\ldots,n\). Lemma 6.0 gives the decomposition \(\mathbb R^n=V\oplus V^\perp\). Since the \(V\)-component of any \(h\in H\) belongs to \(H\), its other component also does. Thus
\[
 H=V\oplus D,\qquad D=H\cap V^\perp.
\]
The subgroup \(D\) is closed. If zero were not isolated in \(D\), choose nonzero \(d_j\in D\) with \(d_j\to0\). A subsequence of \(d_j/\|d_j\|\) converges to a unit vector \(v\in V^\perp\), by Lemma 6.0. For any \(t\in\mathbb R\), choose integers \(m_j\) with
\(|m_j-t/\|d_j\||\le1\).
Then \(m_j\|d_j\|\to t\), so \(m_jd_j\to tv\). Closedness of \(D\) gives \(tv\in D\) for every \(t\). This line would enlarge \(V\) inside \(H\), a contradiction. Therefore \(D\) is discrete, and the already proved assertion supplies its basis and the bound on \(r\).

Both orthogonal coordinate projections are continuous. Their restrictions give the inverse of the continuous addition map \(V\times D\to H\), proving the topological direct product assertion. \(\square\)

<a id="ha-lca-10-example-6-2"></a>
**Example 6.2 — Lattices and their covolumes.** With pairing \(e^{2\pi i x\cdot\xi}\), a full lattice \(\Lambda=A\mathbb Z^n\), where \(A\) is invertible, has annihilator
\[
 \Lambda^\perp=\Lambda^*=A^{-T}\mathbb Z^n.
 \tag{23}
\]
For self-dual Lebesgue measure and counting measure on the lattice, the quotient has total measure
\[
 \operatorname{vol}(\mathbb R^n/\Lambda)=|\det A|,
 \qquad
 \operatorname{vol}(\mathbb R^n/\Lambda^*)=|\det A|^{-1}.
 \tag{24}
\]

**Proof.** The equality \(e^{2\pi i (Ak)\cdot\xi}=1\) for every \(k\in\mathbb Z^n\) is equivalent to each coordinate of \(A^T\xi\) being integral, using the exact kernel of the circle exponential from HA-LCA-02, Lemma 1.3. This proves (23).

The half-open set \(F=A[0,1)^n\) and its translates by \(\Lambda\) form a disjoint partition of \(\mathbb R^n\): apply \(A^{-1}\) and take integer and fractional parts of each coordinate. It has measure \(|\det A|\) by Lemma 6.0. The measure \(1_F\,dx\) is a finite Radon measure, by HA-LCA-03, Lemma 4.1, and its pushforward \(\rho\) to \(\mathbb R^n/\Lambda\) is finite Radon. For \(f\in C_c(\mathbb R^n)\), countable additivity over the tiles gives, with absolute convergence justified first for \(|f|\),
\[
 \int_{\mathbb R^n}f\,dx
 =\int_F\sum_{\lambda\in\Lambda}f(x+\lambda)\,dx
 =\int_{\mathbb R^n/\Lambda}Pf\,d\rho.
 \tag{25}
\]
Counting measure is the chosen \(dh\), so the sum is \(Pf\). Comparing (25) with Theorem 4.1 and using the surjectivity of \(P\) makes \(\rho\) equal to its quotient Haar measure. Its total mass is \(\operatorname{vol}F=|\det A|\). Apply the same argument to \(A^{-T}\), then use (21) and determinant invariance under transpose. This proves (24).

For \(a\mathbb Z\subseteq\mathbb R\), \(a>0\), the annihilator is \(a^{-1}\mathbb Z\), the primal quotient measure is ordinary length on \([0,a)\), and its dual is counting measure divided by \(a\), by HA-LCA-07, Proposition 3.3. The dual of counting measure on \(a\mathbb Z\) is probability measure on its circle dual, represented by \(a\,dt\) on \([0,1/a)\). Thus the dual Weil formula reads
\[
 \int_\mathbb R F(t)\,dt
 =\int_0^{1/a}
       \left(\frac1a\sum_{k\in\mathbb Z}F(t+k/a)\right)a\,dt.
\]
For \(a=1\), this is exactly the normalization for \(\mathbb Z\subseteq\mathbb R\). \(\square\)

<a id="ha-lca-10-example-6-3"></a>
**Example 6.3 — A dense injective line.** For irrational \(a\), the continuous homomorphism
\[
 j:\mathbb R\longrightarrow\mathbb T^2,\qquad
 j(t)=(e^{2\pi it},e^{2\pi iat})
 \tag{26}
\]
is injective and has dense, proper image. Its dual is
\[
 \widehat j:\mathbb Z^2\longrightarrow\mathbb R,\qquad
 (m,n)\longmapsto m+an,
 \tag{27}
\]
which is not surjective.

**Proof.** If \(j(t)=(1,1)\), then \(t\) and \(at\) are integers. A nonzero such \(t\) would make \(a\) rational, so \(t=0\). By the finite-product dual formula HA-LCA-02, Proposition 4.1 and Corollary 4.2, the characters of \(\mathbb T^2\) are \((z,w)\mapsto z^mw^n\). Restriction gives \(t\mapsto e^{2\pi i(m+an)t}\), proving (27). Only \((m,n)=(0,0)\) gives zero, since \(a\) is irrational. Thus the annihilator of \(j(\mathbb R)\) is trivial, and Proposition 1.2 gives density.

The image is proper without any dimension argument. Points of that image with first coordinate one have \(t\in\mathbb Z\), and their second coordinates lie in the countable set \(\{e^{2\pi iak}:k\in\mathbb Z\}\). The circle is uncountable: the exponential is injective on \([0,1)\), and a real interval is uncountable: for any proposed list, choose nested closed intervals of positive length, each inside the interior of the preceding interval and avoiding the next listed point. Compactness gives a point common to all of them, absent from the list. Hence some point \((1,z)\) is outside the image. Likewise the countable image \(\mathbb Z+a\mathbb Z\) in (27) cannot be all of \(\mathbb R\). Thus this example has nonclosed primal image and nonsurjective dual despite primal injectivity. \(\square\)

<a id="ha-lca-10-example-6-4"></a>
**Example 6.4 — The \(p\)-adic annihilator, including its prerequisites.** For a prime \(p\), there is an LCA field \(\mathbb Q_p\) with compact open subring \(\mathbb Z_p\) and a continuous character \(\psi\) with kernel \(\mathbb Z_p\). The map
\[
 \mathbb Q_p\longrightarrow\widehat{\mathbb Q_p},\qquad
 y\longmapsto\chi_y,\qquad \chi_y(x)=\psi(xy),
 \tag{28}
\]
is a topological isomorphism, and in these coordinates
\[
 (p^m\mathbb Z_p)^\perp=p^{-m}\mathbb Z_p
       \quad(m\in\mathbb Z).
 \tag{29}
\]
In particular \(\mathbb Z_p^\perp=\mathbb Z_p\). Haar measure normalized by \(\operatorname{vol}(\mathbb Z_p)=1\) is self-dual for (28).

**Proof.** We construct the objects so that this example has no later prerequisite.

**Finite residues and the compact ring.** Define
\[
 \mathbb Z_p=
 \{(a_n)_{n\ge1}:a_n\in\mathbb Z/p^n\mathbb Z,\
                       a_{n+1}\equiv a_n\pmod{p^n}\}.
 \tag{30}
\]
Coordinatewise addition and multiplication preserve compatibility, so this is a commutative ring. Give each finite residue ring its discrete topology and \(\mathbb Z_p\) the subspace topology of their product. The compatibility equations are closed. The product is compact Hausdorff by the Banach reading, Lemma 4.1, and ring operations are continuous coordinatewise. Thus \(\mathbb Z_p\) is a compact Hausdorff topological ring.

The integer map \(k\mapsto(k\bmod p^n)_n\) is injective: an integer divisible by every \(p^n\) must be zero, since eventually \(p^n>|k|\). Write \(\pi_n\) for the \(n\)-th coordinate. Then
\[
 \ker\pi_n=p^n\mathbb Z_p.
 \tag{31}
\]
One inclusion is immediate. For the other, if \(a_n=0\), each \(a_{n+j}\) is divisible by \(p^n\); dividing these residues by \(p^n\), modulo \(p^j\), gives compatible residues of a \(b\in\mathbb Z_p\) with \(a=p^n b\). Multiplication by \(p\) is injective: if \(pa=0\), its coordinate modulo \(p^{n+1}\) forces the coordinate \(a_n\) to be zero for every \(n\). The same holds for every power of \(p\). Finite intersections of coordinate conditions in (30) reduce to one condition at the largest index. Hence the groups \(p^n\mathbb Z_p\) form an identity-neighbourhood basis.

An element \(u\) with \(\pi_1(u)\ne0\) is a unit. Each residue \(\pi_n(u)\) is coprime to \(p^n\), so has a unique multiplicative inverse modulo \(p^n\) by Bézout's identity, proved in HA-LCA-01, Lemma 4.2. These inverses are compatible by uniqueness and give \(u^{-1}\in\mathbb Z_p\). Every nonzero \(a\in\mathbb Z_p\) has a unique expression \(p^v u\) with \(v\ge0\) and \(u\) a unit: \(v\) is the number of its initial zero coordinates, and (31) performs the division. A product of units is a unit, so a product of nonzero elements cannot vanish. Thus \(\mathbb Z_p\) is an integral domain.

**The locally compact field.** Adjoin inverses of \(p\) by taking fractions \(p^{-r}a\), \(r\ge0\), \(a\in\mathbb Z_p\), with
\[
 p^{-r}a=p^{-s}b\quad\Longleftrightarrow\quad p^s a=p^r b.
\]
This is an equivalence relation; transitivity follows by multiplying the two given equalities and cancelling a power of \(p\), whose injectivity was proved above. Addition and multiplication use common denominators and respect this equivalence by direct multiplication of the defining equalities. All ring identities follow by clearing a common denominator and using those in \(\mathbb Z_p\). These operations give a field \(\mathbb Q_p\): each nonzero fraction is uniquely \(p^k u\), \(k\in\mathbb Z\), \(u\) a unit, and its inverse is \(p^{-k}u^{-1}\).

Define \(v_p(p^k u)=k\), \(|x|_p=p^{-v_p(x)}\) for \(x\ne0\), and \(|0|_p=0\). Products add valuations. Also
\[
 |x+y|_p\le\max(|x|_p,|y|_p).
 \tag{32}
\]
Indeed factor out the smaller of the two valuations; the remaining sum belongs to \(\mathbb Z_p\), so has nonnegative valuation unless it is zero. Thus \(d(x,y)=|x-y|_p\) is a translation-invariant metric. Its neighbourhoods of zero have the basis \(p^m\mathbb Z_p\), \(m\in\mathbb Z\). Restricted to \(\mathbb Z_p\), this is the topology in (30), by (31).

Addition is continuous by (32). Multiplication is continuous because
\((x+a)(y+b)-xy=xb+ya+ab\), whose norm is at most the largest of the three corresponding product norms. For \(x\ne0\), if \(|a|_p<|x|_p\), then \(|x+a|_p=|x|_p\): apply (32) first to \(x+a\) and then to \(x=(x+a)-a\). Hence
\[
 |(x+a)^{-1}-x^{-1}|_p
       =|a|_p/|x|_p^2\longrightarrow0.
\]
This proves continuity of inversion away from zero. Scaling by a nonzero element is a homeomorphism, directly from multiplicativity of the norm. In particular every \(p^m\mathbb Z_p\) is compact and open. The additive group of \(\mathbb Q_p\) is therefore LCA.

The sets \(p^{-N}\mathbb Z_p\), \(N\ge0\), are an increasing open cover of \(\mathbb Q_p\). Every compact subset lies in one of them, by a finite subcover. The ring \(\mathbb Z[1/p]\) is dense: if \(a\in\mathbb Z_p\), choose its integer residue \(a_n\in\{0,\ldots,p^n-1\}\); then \(a-a_n\in p^n\mathbb Z_p\). Scale these approximations for any \(p^{-r}a\). The embedded integers have characteristic zero, so their fraction field also embeds; it is the ordinary \(\mathbb Q\), and contains this dense subring.

**The basic character.** For \(x=p^{-r}a\), \(r\ge0\), let
\(\{x\}_p=a_r/p^r\), where \(a_r\) is the integer residue of \(a\) modulo \(p^r\); for \(r=0\), take zero. Equivalently \(\{x\}_p\) is the unique rational \(t\in\mathbb Z[1/p]\cap[0,1)\) for which \(x-t\in\mathbb Z_p\). Existence follows from the residue construction. For uniqueness, note that
\[
 \mathbb Z[1/p]\cap\mathbb Z_p=\mathbb Z:
\]
an integer divided by \(p^r\) has nonnegative valuation exactly when its numerator is divisible by \(p^r\). Two proposed residues differ by an integer of absolute real value less than one, so they agree. This also proves that the definition does not depend on the chosen denominator.

The difference
\(\{x\}_p+\{y\}_p-\{x+y\}_p\)
lies in both \(\mathbb Z[1/p]\) and \(\mathbb Z_p\), hence is an integer. Therefore
\[
 \psi(x)=e^{2\pi i\{x\}_p}
 \tag{33}
\]
is an additive character. Its kernel is exactly \(\mathbb Z_p\), using the circle-exponential kernel proved in HA-LCA-02, Lemma 1.3, and \(0\le\{x\}_p<1\). It is constant on each open \(\mathbb Z_p\)-coset, so is continuous. Its image consists of the roots of unity of \(p\)-power order: (33) gives only such roots, and \(k/p^n\) supplies every one of them.

**All characters and their topology.** Each \(\chi_y(x)=\psi(xy)\) is continuous. If \(y\ne0\), take \(x=(py)^{-1}\); then \(\chi_y(x)=e^{2\pi i/p}\ne1\). Thus (28) is injective.

For any continuous character \(\chi:\mathbb Q_p\to\mathbb T\), there is \(N\ge0\) such that \(|\chi(x)-1|<1\) on \(p^N\mathbb Z_p\). A subgroup of the circle contained in that arc is trivial, by HA-LCA-02, Lemma 1.2. Hence \(\chi\) kills \(p^N\mathbb Z_p\). The character \(\theta(x)=\chi(p^Nx)\) kills \(\mathbb Z_p\).

For every \(n\ge1\), its value \(\theta(p^{-n})\) is a \(p^n\)-th root of unity, so uniquely
\[
 \theta(p^{-n})=e^{2\pi i c_n/p^n},
 \qquad 0\le c_n<p^n.
\]
The equality \(\theta(p^{-n})=\theta(p^{-(n+1)})^p\) gives \(c_{n+1}\equiv c_n\pmod{p^n}\). Thus these residues define \(c\in\mathbb Z_p\). Formula (33) shows that \(\theta(k/p^n)=\psi(ck/p^n)\) for every integer \(k\). By density of \(\mathbb Z[1/p]\) and continuity, \(\theta(x)=\psi(cx)\) on all of \(\mathbb Q_p\). It follows that
\(\chi(x)=\psi(p^{-N}cx)\).
This proves surjectivity of (28).

Its annihilator calculation is now direct, and does not need any open mapping theorem. A parameter \(y\) kills \(p^m\mathbb Z_p\) exactly when \(p^m y\in\mathbb Z_p\). Sufficiency follows because \(\mathbb Z_p\) is a ring and is the kernel of \(\psi\); necessity follows by testing \(p^m\cdot1\). This proves (29).

For continuity of (28), any compact \(K\subseteq\mathbb Q_p\) lies in \(p^{-N}\mathbb Z_p\). All parameters \(y\in p^N\mathbb Z_p\) give characters identically one on \(K\); this controls every compact-open identity neighbourhood. Conversely, for each integer \(N\), (29) identifies the image of the open subgroup \(p^N\mathbb Z_p\) with
\[
 \left\{\chi:\sup_{x\in p^{-N}\mathbb Z_p}|\chi(x)-1|<1\right\}.
\]
The equality follows from the small-arc lemma applied to the image of the entire subgroup \(p^{-N}\mathbb Z_p\). This is an open set in the dual because that subgroup is compact. Images of these identity-neighbourhood basis sets are open, proving inverse continuity. Thus (28) is a topological isomorphism.

**The Haar normalization.** Normalize Haar measure \(dx\) so that \(\mathbb Z_p\) has mass one; it is compact open, so its mass before scaling is finite and positive. Put \(f=1_{\mathbb Z_p}\in C_c(\mathbb Q_p)\). Translation invariance shows \(f*\widetilde f=f\): the integral is one for \(x\in\mathbb Z_p\) and zero otherwise. Thus \(f\) is of positive type, by HA-LCA-04, Proposition 2.2. The same translation argument for character integrals, or the calculation in Proposition 4.2, gives
\(\widehat f(\chi_y)=1_{\mathbb Z_p}(y)\).
Transport dual Haar measure through (28); it is \(c\,dx\) for some \(c>0\). Pointwise \(B^1\) inversion at zero, HA-LCA-07, Theorem 2.1, gives
\[
 1=f(0)=\int\widehat f\,d\xi=c\,\operatorname{vol}(\mathbb Z_p)=c.
\]
Therefore the Haar measure is self-dual. All parts of the example are now proved. \(\square\)

## 7. Exercises with complete solutions

<a id="ha-lca-10-exercise-7-1"></a>
**Exercise 7.1 — An integer subgroup.** For \(n\ge1\), compute \((n\mathbb Z)^\perp\subseteq\mathbb T\) and both maps in (3).

**Solution.** The character \(k\mapsto z^k\) is trivial on \(n\mathbb Z\) exactly when \(z^n=1\), so its annihilator is the finite group \(\mu_n\) of \(n\)-th roots. A character of \(\mathbb Z/n\mathbb Z\) is determined by its value on the residue of one, any member of \(\mu_n\), and pullback is exactly its inclusion in \(\mathbb T=\widehat{\mathbb Z}\). The finite topologies are discrete.

Identify \(n\mathbb Z\) with \(\mathbb Z\) by \(k\mapsto nk\). Restriction then takes the character with parameter \(z\) to the parameter \(z^n\). This map is surjective, since each circle point has an \(n\)-th root by HA-LCA-02, Lemma 1.3, and has kernel \(\mu_n\). The induced map \(\mathbb T/\mu_n\to\mathbb T\) is the second topological isomorphism of Theorem 2.1. For \(n=1\), the annihilator is the trivial group and the second map is the identity, as required. \(\square\)

<a id="ha-lca-10-exercise-7-2"></a>
**Exercise 7.2 — Dimensions one and two.** Describe all closed subgroups of \(\mathbb R\) and \(\mathbb R^2\).

**Solution.** In dimension one, Proposition 6.1 gives \(\{0\}\), \(a\mathbb Z\) with \(a>0\), and \(\mathbb R\). Its proof gives the least-positive-element argument for the discrete case. If zero is not isolated, take nonzero \(h_j\to0\), and for any \(t\) round \(t/h_j\) to an integer \(k_j\). Then \(k_jh_j\to t\), so closedness gives the whole line.

In dimension two, (22) gives exactly: the zero group; an infinite cyclic group \(\mathbb Z v\), \(v\ne0\); a full lattice \(\mathbb Z v+\mathbb Z w\) with \(v,w\) independent; a line \(V\); a group \(V\oplus\mathbb Z w\) with \(w\ne0\) perpendicular to \(V\); and the whole plane. Each is closed: the vector factors are closed by Lemma 6.0, the displayed integer groups are discrete and closed (an invertible coordinate map sends their nonzero points away from zero), and the product decomposition is a homeomorphism. The proof of Proposition 6.1 establishes exhaustiveness and gives explicit independent generators, rather than only an abstract group classification. \(\square\)

<a id="ha-lca-10-exercise-7-3"></a>
**Exercise 7.3 — Reciprocal covolumes.** Verify the reciprocal-covolume formula for a full lattice, including the measure normalization.

**Solution.** Write the lattice as \(A\mathbb Z^n\) with invertible \(A\). Counting measure is the chosen Haar measure on each discrete lattice, and \(dx\) is the self-dual Lebesgue measure for the pairing \(e^{2\pi i x\cdot\xi}\), as proved in HA-LCA-07, Proposition 3.2. Example 6.2 proves that the quotient measure required by Weil's formula is the pushforward of Lebesgue measure on \(A[0,1)^n\), with total \(|\det A|\). Its dual lattice is \(A^{-T}\mathbb Z^n\) and has covolume \(|\det A^{-T}|=|\det A|^{-1}\). Multiplying yields one. Scaling either lattice's counting measure would rescale its quotient measure inversely; the claimed formula uses counting measure on both, as specified. \(\square\)

<a id="ha-lca-10-exercise-7-4"></a>
**Exercise 7.4 — Injectivity is insufficient.** Give a continuous injective homomorphism of LCA groups with nonclosed image and nonsurjective dual. Explain the distinction from Theorem 2.1.

**Solution.** Use (26) with irrational \(a\). Example 6.3 proves injectivity, density and properness of the image, and computes its dual image as the proper subgroup \(\mathbb Z+a\mathbb Z\) of \(\mathbb R\). This map is not a homeomorphism onto its image. If it were, that image would be locally compact in the relative topology, and HA-LCA-09, Lemma 1.2 would make it closed, a contradiction. Theorem 2.1 concerns an actual closed subgroup with its relative topology; mere injectivity supplies neither of these properties. \(\square\)

<a id="ha-lca-10-exercise-7-5"></a>
**Exercise 7.5 — Determine the dual quotient constant.** Give the coset-integral computation that fixes the constant in Proposition 5.1 for an arbitrary closed \(H\).

**Solution.** Let \(A=H^\perp\) carry the measure dual to \(dz\). Choose nonzero \(u\in C_c(G)\), put \(f=u*\widetilde u\), and for every \(\gamma\in\Gamma\) put \(u_\gamma=\overline\gamma u\). Then \(\overline\gamma f=u_\gamma*\widetilde{u_\gamma}\). Lemma 5.0 gives
\[
 P(\overline\gamma f)=Pu_\gamma*\widetilde{Pu_\gamma},
 \qquad
 \widehat{P(\overline\gamma f)}(a)=\widehat f(\gamma a).
\]
Inversion on \(Q\) at zero therefore gives the exact identity
\[
 \int_A\widehat f(\gamma a)\,da
 =\int_H f(h)\overline{\gamma(h)}\,dh
 =\widehat{f|_H}(\gamma|_H).
\]
This holds on every coset, including ones on which either side is zero. All integrals are finite because the averaged function is a compactly supported positive autocorrelation. If Weil on \(\Gamma\) supplies \(d\eta_0=c\,d\eta\), integrate this identity against that quotient measure. The primal inversion formula gives \(\int_\Gamma\widehat f=f(0)\), and inversion on \(H\) gives \(\int_{\widehat H}\widehat{f|_H}=f(0)\). Hence \(f(0)=c f(0)\). Nonzero \(u\) gives \(f(0)=\|u\|_2^2>0\), so \(c=1\).

There is no hidden global product-Fubini assumption: the convolution averaging used only compact product supports; \(\widehat f\), when Weil's \(L^1\) extension is applied to it, is a \(C_0\) function with sigma-compact nonzero set. Thus Theorem 4.1 applies in its precise arbitrary-LCA form. \(\square\)

## Scope

Both maps in subgroup–quotient duality are topological isomorphisms, and all character extensions, annihilator relations and strict exact-sequence statements have been proved. Quotient integration has been proved on continuous compactly supported functions and on \(L^1\) classes with the representative condition necessary on the full Haar domain. Example 4.0 proves the obstruction to a broader representative assertion.

The Euclidean subgroup classification, reciprocal lattice covolumes, idempotent probability theorem and \(p\)-adic self-duality example have complete proofs here. The next lesson applies the quotient and dual-measure identities to Poisson summation.

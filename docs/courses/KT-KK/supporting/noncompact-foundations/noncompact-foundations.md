# Noncompact foundations for equivariant induction

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

This companion proves the topology and integration used for second countable locally compact Hausdorff groups and their closed subgroups. It does not assume that a subgroup is normal, that a quotient has local continuous sections, or that either group is unimodular. Compact Haar measure and compact vector integration remain the earlier [Foundations for compact-group averaging and coefficient approximation](../representations-of-compact-groups/compact-foundations.html), CPT-F-005 and CPT-F-010. Its CPT-F-002–CPT-F-004 also prove compact Hausdorff separation, finite Radon representation and finite scalar Fubini. The ordinary module facts are [Hilbert-module foundations](../hilbert-c-star-modules-and-morita-equivalence/hilbert-module-foundations.html), MF.1–MF.7.

<a id="ncf-001"></a>

## NCF.1. Countable locally compact spaces, cutoffs and partitions

Let \(X\) be a second countable locally compact Hausdorff space. We prove the specific topology tools needed below. A countable base makes every open cover admit a countable subcover: for each basic open set contained in some cover member, choose one such member. The chosen members cover \(X\). The same applies to a closed subspace, by adding its open complement to a cover.

First, \(X\) is regular. Given \(x\in O\) open, take an open neighborhood \(V\) of \(x\) with compact closure. In the compact Hausdorff space \(\overline V\), the compact normality proof of CPT-F-002 provides a relative open \(W\) containing \(x\) with relative closure contained in \(O\cap V\). Since \(W\subset V\) and \(V\) is open in \(X\), \(W\) is open in \(X\). Its closure in \(X\) equals its closure in \(\overline V\); it is compact and lies in \(O\). Finite unions give the following version for a compact set:
\[
 K\subset O,\ K\text{ compact},\ O\text{ open}
 \ \Longrightarrow\
 K\subset W\subset\overline W\subset O,
 \quad \overline W\text{ compact}.                 \tag{NC.1}
\]

The space is also normal. For disjoint closed \(A,B\), regularity gives countable open families \(U_n,V_n\) covering \(A,B\), respectively, with
\(\overline U_n\cap B=\overline V_n\cap A=\varnothing\).
Countable families suffice by the preceding closed-subspace covering argument. The open sets
\[
 P=\bigcup_n\left(U_n\setminus\bigcup_{j\leq n}\overline V_j\right),
 \qquad
 Q=\bigcup_n\left(V_n\setminus\bigcup_{j\leq n}\overline U_j\right)
\]
contain \(A,B\) and are disjoint. If a point were in the terms indexed \(n,m\), the smaller of \(n,m\) would exclude the other term's closure. Empty closed sets cause no difficulty.

For use with this normality, recall the nested-open construction explicitly. For disjoint closed \(A,B\), choose opens \(U_0,U_1\) with
\(A\subset U_0\subset\overline U_0\subset U_1=X\setminus B\).
Inductively, normality inserts \(U_{(r+s)/2}\) between \(\overline U_r\) and \(U_s\) for consecutive dyadic indices \(r<s\). Thus
\(\overline U_r\subset U_s\) whenever \(r<s\). Put
\[
 u(x)=\inf\{r\in[0,1]\text{ dyadic}:x\in U_r\},
 \qquad \inf\varnothing=1.
\]
Then \(u=0\) on \(A\), \(u=1\) on \(B\). The identities
\[
 \{u<t\}=\bigcup_{r<t}U_r,\qquad
 \{u>t\}=\bigcup_{r>t}(X\setminus\overline U_r)
 \quad(0<t<1)
\]
and the corresponding endpoint statements prove continuity. This is the same dyadic mechanism proved for compact spaces in CPT-F-002; only normality was required for its construction.

Combining it with (NC.1), for \(K\subset O\) as there one obtains a function
\[
 0\leq\rho\leq1,\quad \rho=1\text{ on }K,\quad
 \rho\in C_c(X),\quad\operatorname{supp}\rho\subset O.       \tag{NC.2}
\]
Indeed choose \(W\) with compact closure in \(O\), separate \(K\) from the closed set \(X\setminus W\), and take \(\rho\) to be one on the former and zero on the latter. Its support lies in \(\overline W\).

There is a compact exhaustion \(K_n\) with
\[
 K_n\subset\operatorname{int}K_{n+1},\qquad
 \bigcup_n\operatorname{int}K_n=X.                       \tag{NC.3}
\]
Precompact neighborhoods have a countable subcover \(B_n\). Start with \(\overline B_1\). At each step, finitely many precompact open neighborhoods cover the previous compact set together with \(\overline B_{n+1}\); the closure of their union is the next compact set. This ensures both assertions. Empty \(X\) has the empty exhaustion. Equation (NC.2) gives \(0\leq\rho_n\leq1\), equal to one on \(K_n\) and compactly supported; hence \(\rho_n f\to f\) uniformly for every continuous function \(f\) vanishing at infinity. Its tail estimate is \(\|(1-\rho_n)f\|_\infty\leq\sup_{X\setminus K_n}\|f(x)\|\), also for Banach-valued \(f\).

Every open cover of \(X\) has a countable locally finite subordinate partition with compact supports. To construct it, set \(K_0=K_{-1}=\varnothing\), and consider the compact annulus
\(A_n=K_n\setminus\operatorname{int}K_{n-1}\).
At each point of \(A_n\), choose two nested precompact neighborhoods
\[
 x\in V_{n,j}\subset\overline V_{n,j}\subset W_{n,j},
 \quad
 \overline W_{n,j}\subset
 U_{n,j}\cap(\operatorname{int}K_{n+1}\setminus K_{n-2}),
\]
where \(U_{n,j}\) is an assigned member of the given cover. Such choices follow from (NC.1); the annulus avoids \(K_{n-2}\). Finitely many \(V_{n,j}\) cover \(A_n\). Choose \(\psi_{n,j}\) from (NC.2), equal to one on \(\overline V_{n,j}\) and supported in \(W_{n,j}\). Their supports form a locally finite family: a neighborhood inside \(\operatorname{int}K_m\) misses all families with \(n\geq m+2\), and the remaining families are finite. They cover \(X\) by positive sets. Thus
\[
 s(x)=\sum_{n,j}\psi_{n,j}(x)>0,\qquad
 \chi_{n,j}=\psi_{n,j}/s
\]
are continuous, locally finite, sum to one, and have compact supports inside their assigned cover members. A compact set meets only finitely many supports, by taking finitely many of the neighborhoods witnessing local finiteness. Repeating an original cover label is permitted; it causes no change in the subordination claim. Finite compact-cover partitions are already CPT-F-002.

We need one extension result. Let \(F\subset X\) be closed and \(f:F\to[-M,M]\) continuous. For a residual \(r\) bounded by \(M\), its closed level sets
\(\{r\leq-M/3\}\) and \(\{r\geq M/3\}\) are closed in \(X\). The preceding separation function gives \(g:X\to[-M/3,M/3]\) taking the corresponding endpoint values on them. Then
\(\|r-g|_F\|_\infty\leq2M/3\).
Apply this repeatedly to residuals, with bounds \(M(2/3)^n\). The resulting continuous functions have sup norms at most \(M(2/3)^n/3\), so their series converges uniformly on \(X\), defines a continuous bounded extension, and its residual on \(F\) tends uniformly to zero. For \(f:F\to[0,M]\), clamp an extension to that interval. If \(f:F\to[0,M]\) is compactly supported, multiply its nonnegative extension by a cutoff from (NC.2) that equals one on its compact support. The restriction is still \(f\) everywhere on \(F\), and the extension now lies in \(C_c(X)\). For a bounded real or complex compactly supported function, extend its real and imaginary parts by the preceding bounded extension construction, then multiply the resulting extension by such a cutoff. Its restriction is again the original function. This proves exactly the compactly supported extension needed for closed-subgroup approximate-identity functions.

For completeness, if \(K\) is compact and second countable and \(Z\) is a separable Banach space, \(C(K,Z)\) is separable. Choose a countable relative base on \(K\). For each pair of basic sets with the closure of the first inside the second, choose a continuous cutoff equal to one on that closure and zero outside the second. Such a countable family separates points, by regularity. If a closure does not itself belong to a basic set contained in the desired open set, use a finite union of basic sets as the second set; the family of these finite unions is still countable. The algebra it generates with rational complex coefficients and \(1\) is countable and uniformly dense in \(C(K)\), by CPT-F-001's proved Stone–Weierstrass argument. For a countable dense set \(D\subset Z\), finite sums of members of this algebra times members of \(D\) are countable. They are dense in \(C(K,Z)\): cover \(K\) by finitely many neighborhoods on which a given \(Z\)-valued function varies by less than \(\varepsilon\), choose nearby values in \(D\), use CPT-F-002's finite partition, and approximate each scalar partition function by the countable algebra. Thus no metrization theorem is an unproved premise of this separability argument.

<a id="ncf-002"></a>

## NCF.2. Closed subgroups and homogeneous quotients

Let \(G\) be a second countable locally compact Hausdorff group and \(H\) a closed subgroup. Its relative topology makes \(H\) locally compact Hausdorff and second countable: intersect a compact neighborhood in \(G\) with \(H\). Therefore NCF.1 applies to \(G\) and \(H\).

Equip the homogeneous space \(X=G/H\) with the quotient topology and write \(q:G\to X\). The map is open, since
\(q^{-1}(q(O))=OH=\bigcup_{h\in H}Oh\) for an open \(O\subset G\).
It follows that the images of a countable base form a base of \(X\).

The quotient is Hausdorff. For unequal cosets \(gH,kH\), the element \(g^{-1}k\) is outside the closed set \(H\). Continuity of \((u,v)\mapsto u^{-1}v\) gives neighborhoods \(O_g,O_k\) with
\(O_g^{-1}O_k\cap H=\varnothing\).
Their open quotient images are disjoint: a common coset would give \(u\in O_g,v\in O_k\) with \(u^{-1}v\in H\), a contradiction. At any representative \(g\), a precompact open \(O\ni g\) has open image \(q(O)\) contained in the compact set \(q(\overline O)\). The latter is closed because \(X\) is Hausdorff, so the closure of \(q(O)\) is compact. Thus \(X\) is locally compact. NCF.1 now supplies normality, compact exhaustions, cutoffs and subordinate partitions on \(X\). None of this treats \(G/H\) as a group or requires \(H\) to be a normal subgroup.

Every compact \(C\subset G/H\) has a compact set of representatives. Choose finitely many precompact opens \(O_j\subset G\) whose quotient images cover \(C\), and set
\[
 L=q^{-1}(C)\cap\bigcup_j\overline O_j.                 \tag{NC.4}
\]
It is closed in a compact set and hence compact, and \(q(L)=C\). This proof extends the compact-lifting mechanism used for abelian groups in the HA-LCA lesson to arbitrary closed subgroups. It makes no claim of a continuous local section.

For closed \(L\subset H\subset G\), the map \(G/L\to G/H\) is continuous. The fibre over \(gH\) is homeomorphic to \(H/L\), by \(hL\mapsto ghL\), and is closed. To see its topology, \(H\) is closed in \(G\) and the quotient maps are open; if an open subset of \(H/L\) has preimage \(V\subset H\), write \(V=H\cap O\) for open \(O\subset G\). Its fibre image is the intersection of that fibre with the open set \(q_L(gO)\). This verifies the subspace topology. These facts are the quotient inputs to successive induction and its vanishing conditions.

<a id="ncf-003"></a>

## NCF.3. Radon representation and scalar Fubini beyond compact spaces

Let \(X\) be as in NCF.1 and \(I:C_c(X)\to\mathbb C\) a positive linear functional. We derive its noncompact Radon representation from CPT-F-003, without importing another representation theorem. Fix the exhaustion (NC.3) and cutoffs \(b_n\in C_c(X)\) equal to one on \(K_n\), with \(0\leq b_n\leq1\), supported in \(\operatorname{int}K_{n+1}\).

For \(v\in C(K_{n+1})\), take a bounded continuous extension to \(X\) by NCF.1 and define \(I_n(v)=I(b_n\widetilde v)\). This is independent of the extension, because \(b_n\) vanishes outside \(K_{n+1}\). Positivity follows by choosing nonnegative extensions when \(v\geq0\); linearity follows by the same independence. It is bounded: for real \(v\), \(|I_n(v)|\leq I(b_n)\|v\|_\infty\); decomposing into real and imaginary parts gives a complex bound. CPT-F-003 supplies a finite Radon measure \(\mu_n\) on \(K_{n+1}\), extended by zero to \(X\).

On \(O_n=\operatorname{int}K_n\), all measures \(\mu_m\), \(m\geq n\), give \(I(f)\) for \(f\in C_c(O_n)\). They therefore have the same restriction to \(O_n\): an open subset of \(O_n\) has measure equal to the supremum of integrals of its continuous compactly supported tests, by compact inner regularity and (NC.2). Equality on opens extends to Borel sets by finite Radon outer regularity. Define
\[
 \mu(E)=\lim_n\mu_n(E\cap O_n),\qquad E\in\mathcal B(X).
                                                               \tag{NC.5}
\]
Consistency makes the terms increasing. It gives countable additivity by passing the increasing limit through a nonnegative series; that interchange is scalar monotone convergence, already proved in CPT-F-004. The resulting measure restricts to \(\mu_n\) on \(O_n\), is finite on each \(K_n\subset O_{n+1}\), and is sigma-finite.

It is Radon. For any Borel \(E\), partition it into
\(E_n=E\cap(O_n\setminus O_{n-1})\), with \(O_0=\varnothing\). Each piece lies in \(O_n\), where the finite Radon measure \(\mu_n\) applies. Choose an open \(V_n\subset O_n\) containing \(E_n\) with
\(\mu(V_n)\leq\mu(E_n)+\varepsilon2^{-n}\).
Then \(V=\bigcup_nV_n\) contains \(E\) and
\(\mu(V)\leq\mu(E)+\varepsilon\). This proves outer regularity, also when \(\mu(E)=\infty\). For inner regularity, first intersect \(E\) with \(O_n\); compact inner approximation there and monotone convergence in \(n\) give
\(\mu(E)=\sup\{\mu(C):C\subset E,\ C\text{ compact}\}\).
The integral identity \(I(f)=\int f\,d\mu\) holds because the support of \(f\) lies in some \(O_n\), where the finite representation gives it. The open-test supremum and outer regularity prove uniqueness. Homeomorphisms preserve these properties; consequently invariant functionals give invariant measures.

For Radon measures \(\mu,\nu\) on second countable locally compact spaces \(X,Y\), their product and Fubini follow from the compact finite version, CPT-F-004. Choose compact exhaustions \(K_n,L_n\). On \(K_n\times L_n\), take the product of the restricted finite measures by that earlier proof. These products agree under restriction to smaller rectangles, because their scalar finite Fubini formula gives identical integrals of every Borel indicator. Define the global product by increasing restriction to \(K_n\times L_n\), as in (NC.5). Its measure is sigma-finite. The Borel sigma-algebra of \(X\times Y\) is the product Borel sigma-algebra: a countable product base makes every open set a countable union of open rectangles.

For every nonnegative Borel \(F\), apply compact finite Fubini first to the bounded functions
\[
 F_n(x,y)=\min(F(x,y),n)\,1_{K_n}(x)1_{L_n}(y).
\]
They increase to \(F\). Scalar monotone convergence in each order, already CPT-F-004, gives
\[
 \int_{X\times Y}F\,d(\mu\times\nu)
 =\int_X\int_Y F(x,y)\,d\nu(y)\,d\mu(x)
 =\int_Y\int_X F(x,y)\,d\mu(x)\,d\nu(y).              \tag{NC.6}
\]
The inner functions are measurable, as increasing limits of the finite measurable inner functions. Applying this to \(|F|\), then to real and imaginary positive and negative parts, proves scalar Fubini for every absolutely integrable complex \(F\), with integrable sections almost everywhere. Completed measures are handled by choosing Borel representatives outside a null set; finite null-section assertions follow from CPT-F-004 and exhaustions give the global null-section assertion. Thus no unrestricted non-sigma-finite Fubini theorem is claimed.

The product is Radon too. On \(O_n\times P_n\), where \(O_n=\operatorname{int}K_n\), \(P_n=\operatorname{int}L_n\), it agrees with the finite compact product's restriction. The outer and inner regularity argument used for (NC.5) applies verbatim to this product exhaustion.

<a id="ncf-004"></a>

## NCF.4. Noncompact Haar measure and translation continuity

For compact groups use CPT-F-005's already proved Haar probability. We now construct Haar measure for the noncompact groups in the standing scope. Second countability supplies the compact exhaustion and the Radon and integration inputs through NCF.1–NCF.3.

For nonnegative nonzero \(f,u\in C_c(G)\), define the covering number
\[
 C(f,u)=\inf\left\{\sum_{j=1}^N c_j:
 f(x)\leq\sum_jc_j u(t_j^{-1}x)\ \forall x,\quad c_j\geq0\right\}.
                                                               \tag{NC.7}
\]
It is finite: finitely many left translates of the nonempty open set where \(u>\|u\|_\infty/2\) cover the compact support of \(f\), and sufficiently large equal coefficients dominate \(f\). It is positive since any such domination gives
\(\|f\|_\infty\leq\|u\|_\infty\sum c_j\).
Set \(C(0,u)=0\). Translating the centers, adding dominations, scaling and comparing functions prove left invariance in \(f\), subadditivity, positive homogeneity and monotonicity. Substituting a domination of \(v\) by translates of \(u\) into one of \(f\) by translates of \(v\), then approximating the two infima, gives
\[
 C(f,u)\leq C(f,v)C(v,u).                              \tag{NC.8}
\]

Fix \(f_0\in C_c(G)\), nonzero and nonnegative. For each identity neighborhood \(U\), choose nonzero \(u_U\geq0\) supported in \(U\), by (NC.2), and set \(J_U(f)=C(f,u_U)/C(f_0,u_U)\). Equation (NC.8) gives the uniform bounds
\[
 C(f_0,f)^{-1}\leq J_U(f)\leq C(f,f_0)\quad(f\ne0),
 \qquad J_U(f_0)=1.                                  \tag{NC.9}
\]
Use the tail ultrafilter and bounded-real-family limit constructed in CPT-F-005, with neighborhoods directed by shrinking. Define \(J(f)=\lim_U J_U(f)\). No additional compactness theorem is an input here.

We prove additivity with the support and error terms included. Every \(r\in C_c(G)\) is uniformly continuous under small right translations. Indeed choose a precompact identity neighborhood \(V_0\). For \(v\in V_0\), only the compact set
\(\operatorname{supp}r\ \cup\operatorname{supp}r\,\overline V_0^{-1}\)
can have \(r(xv)-r(x)\ne0\). Continuity on this compact set times \(\{e\}\), and a finite product-neighborhood cover, give
\[
 \sup_{x\in G}|r(xv)-r(x)|\longrightarrow0
 \quad(v\to e).
                                                               \tag{NC.10}
\]
Left translations satisfy the same assertion, using the compact set
\(\overline V_0\operatorname{supp}r\cup\operatorname{supp}r\).

Given \(f_1,f_2\geq0\), choose \(k\in C_c(G)\), \(0\leq k\leq1\), equal to one on their supports. For \(\delta>0\), put \(h=f_1+f_2+\delta k\). Define \(a_i=f_i/h\) where \(h>0\), zero elsewhere. Each \(a_i\) is continuous and compactly supported: the denominator is at least \(\delta\) on the support of \(f_i\), and \(f_i\) is zero off that support. Also \(a_1+a_2\leq1\).

For any \(\eta>0\), (NC.10) supplies \(U\) with
\(|a_i(tv)-a_i(t)|<\eta\) for all \(t\in G,v\in U\).
If \(h\leq\sum_j c_j u_U(t_j^{-1}x)\), then a contributing term has \(x=t_jv\), \(v\in U\). Multiplying the domination by \(a_i(x)\) therefore gives
\[
 f_i(x)\leq\sum_j c_j(a_i(t_j)+\eta)u_U(t_j^{-1}x).
\]
Adding the coefficient sums of these two dominations and taking infima proves
\[
 J_U(f_1)+J_U(f_2)
 \leq(1+2\eta)J_U(h)
 \leq(1+2\eta)\bigl[J_U(f_1+f_2)+\delta J_U(k)\bigr].       \tag{NC.11}
\]
The bounds (NC.9) control both error terms independently of \(U\). Pass to the tail-ultrafilter limit, then let \(\eta,\delta\) tend to zero. Together with subadditivity, this gives \(J(f_1+f_2)=J(f_1)+J(f_2)\). The formula uses an oscillation inequality; it does not equate ratios at different points.

Extend \(J\) to real compactly supported functions by differences of nonnegative ones, then complexify. Additivity makes the extension independent of each decomposition. It is positive, nonzero and left invariant. It is locally bounded: for functions supported in a compact \(K\), choose \(k=1\) on \(K\), and positivity gives
\(|J(f)|\leq J(k)\|f\|_\infty\), using a complex phase and the real part when needed. NCF.3 now supplies a nonzero Radon measure \(\mu\) representing \(J\). Its uniqueness there transfers left functional invariance to
\(\mu(gE)=\mu(E)\) for all Borel \(E\). This is left Haar measure, finite on compacts and sigma-finite.

Every nonempty open set \(O\) has positive measure. Otherwise any compact set is covered by finitely many left translates of \(O\) and has measure zero. Inner regularity would give \(\mu(G)=0\), contradicting \(J(f_0)=1\). Consequently every nonzero nonnegative compactly supported continuous function has positive integral. Each identity neighborhood admits a nonnegative \(\varphi\in C_c(G)\) supported there with integral one, by dividing a bump by its positive integral. Closed subgroups have their own Haar measure by the same argument; compact ones use CPT-F-005.

Here is uniqueness, using only the scalar Fubini already proved in NCF.3. Let \(\mu,\nu\) be left Haar measures. Choose nonnegative \(\varphi_U\), supported in shrinking identity neighborhoods inside one fixed precompact neighborhood, with \(\int\varphi_U\,d\mu=1\). For \(f\in C_c(G)\), define
\[
 f_U(x)=\int f(xy)\varphi_U(y)\,d\mu(y).
\]
Equation (NC.10) gives uniform convergence \(f_U\to f\), and all supports lie in one fixed compact set. Hence \(\int f_U\,d\nu\to\int f\,d\nu\). Change \(t=xy\) by left invariance of \(\mu\), then use Fubini on the common compact integration supports:
\[
 \int f_U\,d\nu
 =\int f(t)\left[\int\varphi_U(x^{-1}t)\,d\nu(x)\right]d\mu(t)
 =c_U\int f\,d\mu,
 \quad c_U=\int\varphi_U(z^{-1})\,d\nu(z).               \tag{NC.12}
\]
The last equality changes \(x=tz\), using only left invariance of \(\nu\). Fix nonzero \(f\geq0\); its two integrals are positive. Equation (NC.12) shows that \(c_U\) tends to their positive ratio \(c\). Applying the same equation to every other compactly supported continuous function gives \(\nu=c\mu\), by NCF.3's Radon uniqueness. No modular-function or inversion substitution formula was assumed.

Continuous compactly supported functions are dense in \(L^p(G,\mu)\), for \(p=1,2\). To approximate an indicator of a finite-measure Borel set \(E\), choose compact \(K\subset E\subset O\) open with \(\mu(O\setminus K)<\varepsilon\), by Radon regularity. A cutoff \(\rho=1\) on \(K\), supported in \(O\), satisfies
\(\|\rho-1_E\|_p^p\leq\mu(O\setminus K)<\varepsilon\).
Truncation, simple-function approximation and scalar dominated convergence, CPT-F-004, approximate every \(L^p\) function by such finite-measure indicators. The assertion also holds for completed-measure representatives.

Left translations \(\lambda_gf(x)=f(g^{-1}x)\) are isometries on these \(L^p\) spaces, by left measure invariance. For \(f\in C_c(G)\), (NC.10) and the common compact support bound give \(\|\lambda_gf-f\|_p\to0\). Density and
\[
 \|\lambda_gf-f\|_p
 \leq2\|f-v\|_p+\|\lambda_gv-v\|_p,\quad v\in C_c(G),
                                                               \tag{NC.13}
\]
extend this to every \(L^p\) function. In particular the \(L^1\) translation estimate used for operator smoothing and the \(L^2\) estimate used for regular-module stabilization are proved here.

<a id="ncf-005"></a>

## NCF.5. Bochner integrals, Fubini and compactly supported strict smoothing

The integrals of continuous Banach-valued maps against finite Radon measures on compact sets are already constructed in CPT-F-010. Thus every continuous compactly supported \(v:G\to Z\), with \(Z\) any Banach space, is integrated by that theorem on a compact containing its support, using the restricted Haar measure. Enlarging the compact makes no difference since \(v=0\) on the added set.

We give the measurable extension and Fubini explicitly. A Banach-valued function is strongly measurable if it is almost everywhere the pointwise norm limit of finitely valued measurable functions. Its essential range is separable: outside one null set it lies in the closure of the countable union of the finite approximants' ranges. The norm and the distance to any fixed vector are measurable, as pointwise limits of measurable real functions.

On a sigma-finite measure space, a strongly measurable \(v\) with \(\int\|v\|<\infty\) is approximable in \(L^1\) by integrable finite simple functions. Choose finite-measure sets increasing to the whole space, and also truncate where \(\|v\|\) exceeds an increasing bound. The discarded norm integrals tend to zero by scalar dominated convergence. On a remaining finite-measure set where \(\|v\|\leq M\), use a countable dense set in its separable essential range and select the first vector within distance \(1/n\). The selection sets are measurable. Retain only the first \(N\) selections and put zero on the rest. As \(N\to\infty\), the leftover set has measure tending to zero; its contribution is at most \(M\) times that measure, while the selected contribution's error is at most the set's measure divided by \(n\). First choose \(n\), then \(N\). This constructs the required finite simple approximations. Choose errors summing to a finite number; scalar monotone convergence applied to their norm errors then also gives almost everywhere pointwise convergence.

For a disjoint integrable finite simple function \(s=\sum_j z_j1_{E_j}\), define
\(\int s=\sum_j\mu(E_j)z_j\).
Refining its level sets verifies independence of representation, linearity and
\[
 \left\|\int s\right\|\leq\int\|s\|.
\]
Thus \(L^1\)-approximation defines a unique integral of \(v\), independent of its approximants, with
\[
 \left\|\int v\right\|\leq\int\|v\|.                    \tag{NC.14}
\]
This is the Bochner integral. Its existence follows from completeness of \(Z\), since the simple integrals are Cauchy. Conversely a function approximable in this sense is strongly measurable and has integrable norm: a summably Cauchy subsequence has pointwise absolutely summable norm differences by scalar monotone convergence, giving a pointwise limit and an integrable bound. The same tail estimate gives \(L^1\) convergence of the subsequence and then of the original Cauchy sequence. This also proves completeness of this Banach-valued \(L^1\) space.

Every bounded linear map between Banach spaces commutes with the integral, by the finite simple identity and (NC.14); bounded real-linear or conjugate-linear maps do also, because the measure's simple weights are real. For a closed convex cone, a function taking its values there has its integral there: use the above approximation with values in the cone's separable essential range, and take limits of nonnegative finite combinations. If \(v_n\to v\) almost everywhere in norm and \(\|v_n\|\leq b\) for an integrable scalar \(b\), the limit is strongly measurable and has integrable norm. Scalar dominated convergence applied to \(\|v_n-v\|\leq2b\) proves integral convergence. No closed unbounded-operator commutation assertion is used.

For the scalar product measures of NCF.3, a strongly measurable
\(V:X\times Y\to Z\) with \(\int\|V\|<\infty\) satisfies Banach-valued Fubini:
\[
 \int V\,d(\mu\times\nu)
 =\int_X\left(\int_YV(x,y)\,d\nu(y)\right)d\mu(x)
 =\int_Y\left(\int_XV(x,y)\,d\mu(x)\right)d\nu(y).        \tag{NC.15}
\]
For a finite simple \(V=\sum_jz_j1_{A_j}\) with integrable norm, scalar Fubini of each finite-measure level set gives the identity. Its inner integral functions are strongly measurable, since they are finite linear combinations of measurable scalar section volumes, and their norm integrals are bounded by \(\int\|V\|\).

For general \(V\), choose finite simple \(V_n\) with
\(\sum_n\int\|V_n-V\|<\infty\).
Scalar Tonelli shows that for almost every \(x\), the section errors have summable \(L^1(Y)\) norms. The corresponding sections converge almost everywhere and in \(L^1(Y;Z)\) to \(V(x,\cdot)\), using the product-null section assertion in NCF.3. Their inner integrals therefore converge pointwise almost everywhere to the desired inner integral. The latter is strongly measurable as this pointwise limit, and
\[
 \int_X\left\|\int_Y(V_n-V)(x,y)\,d\nu(y)\right\|d\mu(x)
 \leq\int_{X\times Y}\|V_n-V\|\,d(\mu\times\nu)
 \longrightarrow0.
\]
Pass to the limit in the finite simple identities; the other order is identical with the variables exchanged. This proves (NC.15), including existence and integrability of almost all sections. Continuous compact-support double integrals are its special case and also follow directly from CPT-F-010's compact vector Fubini. The full scalar or Banach Fubini assertion here remains sigma-finite.

For the operator integrals in the equivariant lesson, the precise extension from compact to noncompact groups is particularly short. Let \(T(g)\in\mathcal L(E)\) be uniformly bounded, with \(g\mapsto T(g)x\) and \(g\mapsto T(g)^*x\) continuous for each \(x\in E\), and let \(f\in C_c(G)\). Integrate those vector functions over a compact containing the support of \(f\), using CPT-F-010. Its adjoint identity gives an adjointable operator
\[
 A_f x=\int_G f(g)T(g)x\,dg,\qquad
 A_f^*x=\int_G\overline{f(g)}T(g)^*x\,dg,\qquad
 \|A_f\|\leq \sup_g\|T(g)\|\,\|f\|_1.                 \tag{NC.16}
\]
The norm bound is (NC.14) applied to each vector. Positivity for nonnegative \(f\) and positive \(T(g)\), and integration into the compact ideal for norm-continuous compact-valued localized integrands, are exactly CPT-F-010's positive-cone and closed-subspace conclusions, now on this finite restricted Radon measure.

For a strongly continuous, possibly coefficient-semilinear, action \(U_g\), the field \(g\cdot T=U_gTU_g^{-1}\) and its adjoint act continuously on each vector: replace the moving input by a fixed one and use the common operator bound. Thus (NC.16) applies. Left Haar substitution gives
\[
 h\cdot A_f-A_f
   =\int_G(\lambda_hf-f)(g)(g\cdot T)\,dg,\qquad
 \|h\cdot A_f-A_f\|
   \leq\|T\|\,\|\lambda_hf-f\|_1.                     \tag{NC.17}
\]
Equation (NC.13) makes this orbit norm continuous. This is the strict smoothing used in formulas (2.15) and (7.15) of the equivariant lesson. Each integral has compactly supported scalar weight; no average with respect to an infinite total Haar mass is taken.


<a id="ncf-006"></a>

## NCF.6. Locally supported subgroup averaging

Let \(G\) and \(H\) satisfy NCF.2, with fixed left Haar measure on \(H\). There is a continuous \(\alpha:G\to[0,\infty)\) such that
\[
 \int_H\alpha(gh)\,dh=1\quad(g\in G),\qquad
 \operatorname{supp}\alpha\cap q^{-1}(C)\text{ is compact}
 \quad(C\subset G/H\text{ compact}).                       \tag{NC.18}
\]
For each \(g_0\), the map \(g\mapsto\alpha(g\,\cdot)\) is continuous near \(g_0\) in \(L^1(H)\). The support condition concerns compact subsets of the quotient; \(\alpha\) need not have compact support on all of \(G\).

Here is the construction. For \(f\in C_c(G)\), put
\[
 F_f(gH)=\int_H f(gh)\,dh.                                \tag{NC.19}
\]
This is well-defined on \(G/H\): replacing \(g\) by \(gh_0\) and changing variable \(k=h_0h\) uses left Haar invariance. It is continuous. Choose a precompact neighborhood \(V\) of a representative \(g_0\), and write \(K=\operatorname{supp}f\). For \(g\in V\), the integrand is supported in the compact set \(H\cap\overline V^{-1}K\). On this fixed compact set the function \((g,h)\mapsto f(gh)\) varies uniformly as \(g\to g_0\): continuity at all points of \(\{g_0\}\) times that compact set and a finite product-neighborhood cover prove the uniform assertion. Its integral therefore varies continuously. Since \(q\) is an open quotient map, this continuous invariant function descends to a continuous function on the quotient. Its support lies in the compact set \(q(K)\): it is zero on the complement of that closed set.

For each coset choose a nonnegative \(f\in C_c(G)\) positive at a representative, using NCF.1. It is positive on that representative times an identity neighborhood in \(H\); NCF.4 makes the measure of this neighborhood positive. Consequently \(F_f\) is positive at that coset. These positivity sets cover \(G/H\). Choose a countable locally finite partition \(\chi_j\), with compact supports inside these sets, by NCF.1 applied to NCF.2's quotient. Let \(f_j\) be the function attached to the positivity set for \(\chi_j\); repeated labels are allowed. Set
\[
 \alpha(g)=\sum_j\chi_j(gH)\frac{f_j(g)}{F_{f_j}(gH)}.       \tag{NC.20}
\]
Each summand is set to zero off its positivity set. It is continuous there as well: the closed support of \(\chi_j\) is contained in that set, so a neighborhood of any exterior point misses this support. The pulled-back sum is locally finite, since inverse images of the neighborhoods witnessing local finiteness on \(G/H\) witness it on \(G\). Thus \(\alpha\) is continuous and nonnegative. On each fibre only finitely many summands occur, and (NC.19) gives integral \(\sum_j\chi_j(gH)=1\).

A compact \(C\subset G/H\) meets only finitely many partition supports. On \(q^{-1}(C)\), therefore, the support of \(\alpha\) lies in the union of finitely many compact supports of \(f_j\). Its intersection with \(q^{-1}(C)\) is closed, hence compact; this proves (NC.18). For \(g\) in a precompact neighborhood \(V\) of \(g_0\), let
\(L=\operatorname{supp}\alpha\cap q^{-1}(q(\overline V))\).
This is compact by (NC.18). The functions \(h\mapsto\alpha(gh)\) all have support in the compact set \(H\cap\overline V^{-1}L\). The same finite product-neighborhood argument used for (NC.19), now applied to \(\alpha\), proves uniform convergence on this set as \(g\to g_0\). Multiplication by its finite Haar measure proves the stated \(L^1\) continuity.

In particular, if \(h\mapsto T(h)\) is a norm-continuous field of bounded operators with common bound \(M\), then the norm integrals
\[
 A(g)=\int_H\alpha(gh)T(h)\,dh
\]
exist on these compact integration supports, by NCF.5. They satisfy
\(\|A(g)-A(g_0)\|\leq M\|\alpha(g\,\cdot)-\alpha(g_0\,\cdot)\|_1\).
For \(T(h)=h\cdot F\), changing variable \(k=h_0h\) also gives
\(A(gh_0)=h_0^{-1}\cdot A(g)\).
This proves the continuity and covariance of the pointwise induction operator in Lesson 17, formula (7.14). Formula (NC.17) then supplies its additional whole-group smoothing in (7.15).

## Reading

- Terence Tao, [*254A, Notes 3: Haar measure and the Peter–Weyl theorem*](https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/), Section 1, Theorems 3–4 and the covering-functional construction. The complete Haar and Radon arguments needed here are NCF.3–NCF.4.
- John K. Hunter, [*Notes on Partial Differential Equations*, Appendix 6.A](https://www.math.ucdavis.edu/~hunter/pdes/ch6A.pdf), Definitions 6.13–6.21 and Theorems 6.24–6.26, on strong measurability and the Bochner integral. NCF.5 proves the norm approximation, integral and Fubini assertions used here.
- D. H. Fremlin, [*Measure Theory*, Volume 4, Appendix 4A](https://www1.essex.ac.uk/maths/people/fremlin/chap4a.pdf), 4A2F(d) and 4A2G(e), on normality, extension and compact cutoffs. NCF.1 supplies the constructions for the second countable locally compact spaces used here.

The lesson text is CC0. These freely accessible reading references retain their authors' terms.

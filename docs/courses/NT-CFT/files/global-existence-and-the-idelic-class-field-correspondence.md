# Global existence and the idèlic class field correspondence

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

**Lesson 17.** The preceding lesson associates a reciprocity map to every abelian extension already given. Existence answers the converse question: which subgroups of the idèle class group occur as norm groups? Every open subgroup of finite index does. Thus a finite abelian extension can be specified by local congruence conditions on idèles, without first finding an equation for the extension.

There is a topological distinction between the two kinds of global fields. For a number field, reciprocity maps onto the abelianized absolute Galois group and kills exactly the connected component of the idèle class group. For a function field it is injective, and its image has integral constant-field degree. Giving those integer cosets the discrete topology identifies the class group with an abelianized Weil group. We prove the function-field assertion, including the wild characteristic case.

The prerequisites are [The norm index bound and Hasse’s norm theorem](the-norm-index-bound-and-hasses-norm-theorem.md), especially its full S-unit radical and additive duality, and [The global reciprocity law](the-global-reciprocity-law.md). We use the compactness of norm-one classes from lesson 14 and the local class field correspondence from lesson 6. The higher-dimensional Hasse–Minkowski theorem is not an input.

Write \(J_K\) for idèles, \(C_K=J_K/K^\times\), and \(B_K=G_K^{\mathrm{ab}}=\operatorname{Gal}(K^{\mathrm{ab}}/K)\). All reciprocity maps use arithmetic Frobenius. For a finite extension put
\[
N_{L/K}C_L=\operatorname{im}(N_{L/K}:C_L\longrightarrow C_K).
\]
The symbol \(D_K\) will denote the connected component of \(1\) in \(C_K\). When temporarily discussing universal norms, we use a different symbol \(\mathcal N_K\).

## 1. Norm groups and the existence theorem

**Theorem 17.1 (global existence).** If \(K\) is a global field and \(H\subseteq C_K\) is open of finite index, there is a unique finite abelian extension \(L/K\), inside the fixed separable closure, with
\[
H=N_{L/K}C_L.
\tag{1}
\]

An open subgroup is closed, since its other cosets are open. Conversely a closed subgroup of finite index is open: its complement is a finite union of closed cosets. These observations explain why either formulation is often used. The finite-index hypothesis remains essential for a *finite* class field; for example the degree-zero subgroup of a function-field class group has infinite index.

We first prove existence for number fields. The function-field proof, including characteristic-power indices, is given in sections 5–8.

### Cofinal Kummer norm groups

Let \(n=\ell^a\) and suppose \(\mu_n\subset K\). Choose a finite set \(S\) containing the infinite places and the places dividing \(n\), large enough that \(J_K=K^\times J_K^S\). With \(E_S\) the S-unit group, put
\[
M=K(E_S^{1/n}),\qquad
I(S)=\prod_{v\in S}K_v^{\times n}\times\prod_{v\notin S}\mathcal O_v^\times,
\qquad C(S)=\operatorname{im}(I(S)\to C_K).
\tag{2}
\]
If \(s=|S|\), the S-unit theorem and Kummer pairing give
\(\operatorname{Gal}(M/K)\simeq(\mathbf Z/n)^s\). This full radical is unramified outside \(S\): adjoining roots of units of order prime to the residue characteristic is unramified there. Proposition 15.2 applies with \(r=s\), so its auxiliary set \(T\) is empty. It proves
\[
C(S)\subseteq N_{M/K}C_M,\qquad [C_K:C(S)]=n^s=[M:K].
\]
Reciprocity, Theorem 16.4, gives the same index for the norm group. Consequently
\[
C(S)=N_{M/K}C_M.
\tag{3}
\]

Suppose \(C_K/H\) is an \(\ell\)-group of exponent dividing \(n\). Then \(C_K^n\subseteq H\). Openness of the inverse image of \(H\) in \(J_K\) also puts
\[
U^S=\{x\in J_K:x_v=1\ (v\in S),\ x_v\in\mathcal O_v^\times\ (v\notin S)\}
\tag{4}
\]
inside that inverse image after enlarging \(S\). Every element of \(I(S)\) is a product of an idèle \(n\)th power and an element of \(U^S\). Therefore (3) is a norm group contained in \(H\).

If \(\mu_n\) is not in \(K\), set \(K'=K(\mu_n)\). Enlarge \(S\) until the full set \(S'\) above it satisfies \(J_{K'}=K'^\times J_{K'}^{S'}\). This is possible by adding the projections of finitely many class-group generating primes of \(K'\). Apply (3) over \(K'\) to \(M=K'(E_{S'}^{1/n})\). The local norm of an \(n\)th power is an \(n\)th power, and the local norm of a unit is a unit. Hence
\[
N_{K'/K}C(S')\subseteq C(S),\qquad
N_{M/K}C_M\subseteq C(S)\subseteq H.
\tag{5}
\]
Replace \(M\) by a Galois closure \(\widetilde M/K\); tower norms only shrink the image, so it still lies in \(H\).

For a general finite quotient \(A=C_K/H\), let \(H_\ell\) be the kernel of its projection to the \(\ell\)-primary factor. Construct a finite Galois norm group inside each \(H_\ell\). The compositum of these finitely many extensions has its norm group inside \(\bigcap_\ell H_\ell=H\).

### From a contained norm group to the desired field

We have obtained a finite Galois \(M/K\) with \(N_{M/K}C_M\subseteq H\). Norm limitation, proved in lesson 5 and applied in lesson 16, replaces \(M\) by its maximal abelian subextension \(A/K\), without changing that norm group. Reciprocity identifies
\[
C_K/N_{A/K}C_A\simeq\operatorname{Gal}(A/K).
\]
Let \(L\) be the fixed field of the subgroup corresponding to \(H/N_{A/K}C_A\). Restriction compatibility and Theorem 16.4 identify the kernel for \(L/K\) with exactly \(H\). This proves existence over number fields. Uniqueness follows from the same reciprocity kernels: the fixed field of the closure of the image of \(H\) in \(B_K\) is determined by \(H\).

This argument also treats function-field quotients of order prime to the characteristic. It does not treat characteristic-power quotients by pretending that the missing roots of unity exist. Sections 5–8 supply that case.

## 2. The class field correspondence and local information

**Theorem 17.2.** Finite abelian extensions of \(K\) correspond, with reversed inclusions, to open subgroups of finite index of \(C_K\). The group for \(L/K\) is its norm group, and
\[
\operatorname{Gal}(L/K)\simeq C_K/N_{L/K}C_L.
\tag{6}
\]
If \(i_v:K_v^\times\to C_K\) inserts a component at \(v\), then
\[
\begin{aligned}
v\text{ is unramified in }L&\iff i_v(\mathcal O_v^\times)\subseteq N_{L/K}C_L
&&\text{for finite }v,\\
v\text{ splits completely in }L&\iff i_v(K_v^\times)\subseteq N_{L/K}C_L.
\end{aligned}
\tag{7}
\]
At a real place, ramification means becoming complex; this happens exactly when the class of a negative local element is not in the norm group.

**Proof.** Existence and uniqueness are Theorem 17.1. If \(L_1\subseteq L_2\), tower norms put \(N_{L_2/K}C_{L_2}\subseteq N_{L_1/K}C_{L_1}\). Conversely the inclusion of these kernels reverses the inclusion of their fixed fields in \(K^{\mathrm{ab}}\). Equation (6) is reciprocity.

Local compatibility in Theorem 16.4 identifies the image of \(K_v^\times\) with the decomposition group and the image of \(\mathcal O_v^\times\) with its inertia subgroup. Their triviality is exactly complete splitting and absence of ramification. At a real place the local quotient for \(\mathbf C/\mathbf R\) is the sign group. These arguments concern the *images* under \(i_v\); they require no injectivity assertion about that map. \(\square\)

For example, requiring all finite unit groups to lie in \(H\) produces an extension unramified at every finite prime. Requiring positive real components rather than all real components allows real places to become complex. Deep principal-unit conditions will give the ray class fields in the next lesson.

## 3. Connected components and number-field reciprocity

We record two elementary topological facts, so that the kernel description does not hide a topology theorem.

**Compact-group lemma.** In a compact Hausdorff abelian group \(A\), the identity component \(A^0\) is the intersection of the open subgroups of finite index. The quotient \(A/A^0\) is profinite. If a locally compact abelian group has a neighborhood basis of compact open profinite subgroups, every quotient by a closed subgroup is totally disconnected and has such a basis.

**Proof.** First, in a compact Hausdorff space, the intersection \(Q\) of all clopen neighborhoods of a point is its connected component. To see the nontrivial inclusion, suppose \(Q\) is separated into two nonempty closed parts, and choose disjoint open neighborhoods of those compact parts. The compact complement of their union is excluded by finitely many clopen neighborhoods of the original point. Their intersection is a clopen set containing \(Q\) and lying in that union. Its portion in the open neighborhood of the part containing the point is clopen and misses the other part, contradicting the definition of \(Q\). Thus \(Q\) is connected.

For \(a\notin A^0\), choose a clopen set \(V\) containing \(1\) and missing \(a\). Its translation stabilizer is an open subgroup: compactness of \(V\) and its complement gives a neighborhood of \(1\) whose translations preserve both sets. More explicitly, cover each of the two compact sets by finitely many neighborhoods on which all translations from a common sufficiently small identity neighborhood stay in the same set. This common neighborhood lies in the stabilizer. The stabilizer has finite index by compactness, and misses \(a\), since an element stabilizing \(V\) carries \(1\in V\) into \(V\). Connected sets cannot cross its clopen cosets. This proves the asserted intersection. The map of \(A/A^0\) into the product of these finite quotients is continuous and injective; compactness makes it a homeomorphism onto a closed subgroup, proving profiniteness.

For the last assertion let \(q:G\to G/H\) be the quotient by a closed subgroup. If \(P\subseteq G\) is compact open profinite, then \(q(P)\) is compact and open, and equals \(P/(P\cap H)\), a profinite group. A quotient of a profinite abelian group by a closed subgroup is profinite: its closed subgroup is separated from any outside point by a finite quotient, using compactness and a basis of open finite-index subgroups. Given a neighborhood in \(G/H\), choose \(P\) inside its inverse image. The images \(q(P)\) therefore form the required basis. In particular the quotient is totally disconnected. \(\square\)

**Proposition 17.3.** For a number field, the map
\[
\operatorname{rec}_K:C_K\longrightarrow B_K
\]
is onto and has kernel
\[
D_K=\bigcap_{H\text{ open, finite index}}H
=\overline{\operatorname{im}\left(\prod_{v\mid\infty}(K_v^\times)^0\longrightarrow C_K\right)}.
\tag{8}
\]

**Proof.** Surjectivity was proved in lesson 16: finite-quotient surjectivity gives density, the divisible positive-real content factor is killed, and the remaining norm-one group \(C_K^1\) is compact. Existence and finite reciprocity identify the kernel with the intersection in (8). The decomposition \(C_K=C_K^1\times\mathbf R_{>0}\) reduces this intersection to the compact-group lemma. Indeed an open finite-index subgroup contains the connected positive-real factor, and open finite-index subgroups of \(C_K^1\) detect its identity component. Thus the intersection is precisely \(D_K\).

Let \(A_\infty^0=\prod_{v\mid\infty}(K_v^\times)^0\), embedded as archimedean idèles, and let \(D_\infty\) be the closure of its image. Its image is connected, so \(D_\infty\subseteq D_K\). The quotient of \(J_K\) by \(A_\infty^0\) is
\[
\{\pm1\}^{r_1}\times J_{K,f}.
\tag{9}
\]
This group has a basis of compact open profinite subgroups: at finitely many finite places use deep units, elsewhere full units, and use the discrete sign factors. Now \(C_K/D_\infty\) is (9) modulo the closure of the projected principal subgroup. The last part of the lemma makes it totally disconnected. The image of the connected group \(D_K\) in that quotient is trivial. Therefore \(D_K\subseteq D_\infty\), proving equality. It is a *closure*: this argument does not assert that the archimedean image is closed. \(\square\)

## 4. Rational idèles and a quadratic class field

There is a useful explicit decomposition
\[
C_{\mathbf Q}\simeq\mathbf R_{>0}\times\widehat{\mathbf Z}^{\,\times}.
\tag{10}
\]
For an idèle \(x\), divide it by the positive rational number
\(r=\prod_p p^{v_p(x_p)}\). All finite components become units. Multiply the representative by \(-1\) if necessary to make its real component positive. The resulting positive real component and unit tuple are unique: a rational number which is a unit at every finite prime is \(\pm1\), and positivity fixes the sign. This normalization and its inverse are continuous on restricted-product neighborhoods, proving (10).

The unit group in (10) is profinite. Hence
\[
D_{\mathbf Q}=\mathbf R_{>0}.
\tag{11}
\]
For the extension \(\mathbf Q(\zeta_m)/\mathbf Q\), the normalized unit tuple \(u\) acts through \(\zeta_m\mapsto\zeta_m^{u^{-1}\bmod m}\). This is the local cyclotomic formula of Corollary 9.5, multiplied over the prime divisors of \(m\); the positive real component is trivial.

Consider
\[
H=\mathbf R_{>0}\times
\{u\in\widehat{\mathbf Z}^{\,\times}:u_5\equiv\pm1\pmod5\}.
\tag{12}
\]
It has index \(2\). Its image in \(\operatorname{Gal}(\mathbf Q(\zeta_5)/\mathbf Q)\) is the subgroup \(\{\pm1\}\); taking inverses does not change that subgroup. Its fixed field is
\[
\mathbf Q(\zeta_5+\zeta_5^{-1})=\mathbf Q(\sqrt5).
\tag{13}
\]
Indeed \(z=\zeta_5+\zeta_5^{-1}\) satisfies \(z^2+z-1=0\), so \((2z+1)^2=5\). Thus (12) is the norm group of \(\mathbf Q(\sqrt5)\). This example uses one cyclotomic extension, not the later assertion that every abelian extension of \(\mathbf Q\) is cyclotomic.

## 5. Logarithmic differentials in characteristic \(p\)

For the rest of the proof let \(F\) be a global function field with full constant field \(k=\mathbf F_q\), of characteristic \(p\). Put \(C_F^1=\ker(\deg:C_F\to\mathbf Z)\). It is compact by lesson 14, and \(\deg\) is onto by lesson 16. We need to show that the universal norm subgroup
\[
\mathcal N_F=\ker(\operatorname{rec}_F:C_F\to B_F)
=\bigcap_{L/F\text{ finite separable}}N_{L/F}C_L
\tag{14}
\]
is trivial. Equality follows from finite reciprocity and norm limitation: Galois closures are cofinal, and their norms equal those of their maximal abelian subextensions. All constant-extension norms occur in this intersection. The norm degree formula forces the degree of an element of \(\mathcal N_F\) to be divisible by every positive integer. Thus \(\mathcal N_F\) is a closed subgroup of compact \(C_F^1\).

Here is the needed algebraic logarithmic-differential criterion, with its proof. If a characteristic-\(p\) field \(E\) satisfies \([E:E^p]=p\), choose a p-basis \(t\), so \(E=\bigoplus_{i=0}^{p-1}E^p t^i\). Let \(\partial t=1\), \(\partial E^p=0\). For
\[
y=\sum_{i=0}^{p-1}y_i^p t^i,
\qquad \omega=y\,dt,
\]
define the Cartier operator by
\[
\mathcal C(\omega)=y_{p-1}\,dt.
\tag{15}
\]

**Logarithmic-differential lemma.** This definition is independent of the p-basis, and
\[
\mathcal C(\omega)=\omega\quad\Longleftrightarrow\quad
\omega=db/b\text{ for some }b\in E^\times.
\tag{16}
\]

**Proof.** We have \(\partial^p=0\). Let \(T=\partial-y\), an \(E^p\)-linear operator on the \(p\)-dimensional space \(E\). For multiplication by \(f\), its commutator with \(T\) is multiplication by \(\partial f\). In characteristic \(p\), \((\operatorname{ad}T)^p=\operatorname{ad}(T^p)\), by expanding the repeated commutator and cancelling the intermediate binomial coefficients. Hence \(T^p\) commutes with every multiplication operator and is itself multiplication by \(T^p(1)\).

We compute that scalar explicitly. For a derivation \(\partial\) and a multiplication term \(h\), repeated application of \(\partial+h\) to \(1\) gives
\[
\sum_{\sum j m_j=n}
\frac{n!}{\prod_j m_j!\,(j!)^{m_j}}
\prod_j(\partial^{j-1}h)^{m_j}.
\tag{17}
\]
One proof counts partitions of \(n\) labelled elements: applying the multiplication term creates a new singleton block, and differentiating an existing factor adds the new element to that block. This gives the recurrence \(P_{n+1}=\partial P_n+hP_n\), with \(P_0=1\), and the displayed partition counts. At \(n=p\), all coefficients are divisible by \(p\), except the partition into \(p\) singletons and the single block of size \(p\); every other denominator is prime to \(p\). Taking \(h=-y\) gives
\[
T^p=-\bigl(y^p+\partial^{p-1}y\bigr)
=-\bigl(y^p-y_{p-1}^p\bigr).
\tag{18}
\]
The last equality uses \((p-1)!=-1\) in \(\mathbf F_p\); pairing each nonzero element with its inverse proves this, with only \(1,-1\) left unpaired (and gives the same identity for \(p=2\)).

Thus \(\mathcal C\omega=\omega\) exactly when \(T^p=0\). A nilpotent endomorphism of a nonzero finite-dimensional space has a nonzero kernel vector \(b\). For that vector \(\partial b=yb\), giving \(db/b=\omega\). Conversely, if \(y=\partial b/b\), then \(T=b\partial b^{-1}\), so \(T^p=0\), proving (16).

The definition gives \(\mathcal C(df)=0\) and \(\mathcal C(f^p\omega)=f\mathcal C(\omega)\). For any other p-basis \(u\), (16) gives \(\mathcal C(d\log u)=d\log u\), and hence
\(\mathcal C(u^{p-1}du)=du\). These properties determine the operator in the \(u\)-basis: the terms \(u^i du\), \(i<p-1\), are exact, and the last term has the just computed image. They give exactly (15) with \(u\) in place of \(t\). This proves independence. \(\square\)

Both \(F\) and each completion \(F_v\) satisfy the lemma. For a separating parameter \(t\), if \([F:k(t)]=d\), Frobenius gives \([F^p:k(t^p)]=d\), whereas \([F:k(t^p)]=pd\). Therefore \([F:F^p]=p\). Separability shows \(t\notin F^p\). Locally \(F_v=\kappa(v)((u))\), so \([F_v:F_v^p]=p\). The same separating \(t\) is a local p-basis: in the base completion \(dt\ne0\), since a finite prime polynomial has nonzero derivative, and this remains true in a finite separable extension of completed fields. Thus the global and local Cartier operators agree on global differentials.

## 6. Artin–Schreier symbols and the residue pairing

For a finite field \(\kappa\) and \(E=\kappa((u))\), the arithmetic local symbol for \(\theta^p-\theta=a\) is
\[
\operatorname{rec}_E(b)(\theta)-\theta
=\operatorname{Tr}_{\kappa/\mathbf F_p}\operatorname{res}_u(a\,db/b)
\quad(a\in E,\ b\in E^\times).
\tag{19}
\]
The right side is in \(\mathbf F_p\), regarded as the translation subgroup of this Artin–Schreier extension. If the equation already splits, both sides are zero. We derive this formula from the global reciprocity already proved in lesson 16, using only the rational function field; no global existence theorem is needed.

Modulo \(\wp E=\{z^p-z:z\in E\}\), every \(a\) has a representative
\[
a_0+\sum_{d>0,\ p\nmid d}a_d u^{-d},
\qquad a_d\in\kappa,
\tag{20}
\]
with finitely many summands. Eliminate a highest pole whose order is divisible by \(p\) by subtracting \(\wp(cu^{-d/p})\); perfection of \(\kappa\) supplies its coefficient root and the remaining pole has smaller order. The positive-power part \(a_+\) is \(\wp(-\sum_{r\geq0}a_+^{p^r})\), a convergent series. This proves the reduction.

The representative (20) is rational over \(\kappa\). Form its explicit Artin–Schreier extension of \(\kappa(u)\), as in lesson 3. At every place \(P\ne(u)\), including infinity, \(a\) is integral. The extension is unramified there, and arithmetic Frobenius translates a root by
\(\operatorname{Tr}_{\kappa(P)/\mathbf F_p}(a(P))\): iterating \(\theta^p=\theta+a(P)\) through \([\kappa(P):\mathbf F_p]\) steps gives this identity. Thus the symbol of a rational \(b\) at \(P\) is its valuation times this trace. On the other hand,
\[
\operatorname{res}_P(a\,db/b)=v_P(b)a(P)
\quad(P\ne(u)),
\]
because the logarithmic derivative of a local unit is an integral differential. The partial-fraction residue theorem on \(\kappa(u)\), proved in lesson 15, says that the sum of the residue traces, including infinity, is zero. The global principal product of Theorem 16.4 says that the sum of the local translation symbols is zero. Comparing these two sums proves (19) at \(u=0\) for rational \(b\). Rational elements are dense in the completion; both the symbol and the residue functional are continuous in \(b\), so the formula holds for all local \(b\).

It remains to justify invariance when replacing \(a\) by its representative. In Laurent coordinates,
\[
\mathcal C\left(\sum_j c_j u^jdu\right)
=\sum_m c_{pm+p-1}^{1/p}u^mdu.
\tag{21}
\]
For \(h\in E\), coefficient multiplication gives
\[
\operatorname{res}(h^p\omega)
=\bigl(\operatorname{res}(h\mathcal C\omega)\bigr)^p.
\]
Indeed if \(h=\sum b_j u^j\), the two sides before taking the \(p\)th power have coefficients \(\sum b_j c_{-pj-1}^{1/p}\). The residue sum is finite. Taking the finite-field trace removes the \(p\)th power. Since \(\mathcal C(d\log b)=d\log b\), the residue trace of \((h^p-h)d\log b\) is zero. Changing \(a\) by \(\wp h\) also changes the chosen root by \(h\) and leaves its translation character unchanged. This completes the proof of (19).

We now obtain the global residue pairing without assuming a differential trace-residue theorem. Choose a separating \(t\in F\), and set \(\omega_0=d\log t\). It is nonzero in every completion. Define an additive character of \(\mathbb A_F\) by
\[
\Phi(x)=\exp\left(\frac{2\pi i}{p}
\sum_v\operatorname{Tr}_{\kappa(v)/\mathbf F_p}
\operatorname{res}_v(x_v\omega_0)\right).
\tag{22}
\]
Only finitely many terms are nonzero. Outside finitely many places, \(t\) is a unit and \(dt\) is a unit differential: this follows at the unramified places over \(k(t)\), where an irreducible prime polynomial has unit derivative. Thus (22) is continuous, and its local component is nontrivial at every place by the Laurent coefficient pairing and nondegeneracy of the finite-field trace.

For \(a\in F\), apply (19) to the explicit global extension \(\theta^p-\theta=a\) and to the principal element \(t\). Global reciprocity makes the sum in (22) zero. Therefore \(\Phi\) is trivial on \(F\). Section 5 of lesson 15 proved a trace-based self-duality \((x,z)\mapsto\Psi_F(xz)\) of \(\mathbb A_F\), with exact annihilator \(F\). By that self-duality \(\Phi(x)=\Psi_F(cx)\) for a unique adèle \(c\). Triviality on \(F\) forces \(c\in F\); nontriviality forces \(c\ne0\). Multiplication by this global nonzero scalar preserves \(F\). Consequently
\[
\mathbb A_F\text{ is self-dual under }(x,z)\mapsto\Phi(xz),
\qquad F^\perp=F.
\tag{23}
\]
This deduction explains why no unproved residue-trace compatibility is hidden in the argument.

## 7. Universal norms are trivial

Take \([x]\in\mathcal N_F\), represented by an idèle \(x\). For every \(a\in F\), its reciprocity symbol in \(F(\wp^{-1}a)/F\) is trivial. Formula (19) gives
\[
\sum_v\operatorname{Tr}_{\kappa(v)/\mathbf F_p}
\operatorname{res}_v(a\,d\log x_v)=0.
\tag{24}
\]
Write \(d\log x_v=y_v\omega_0\). The \(y_v\) form an adèle: at almost all places \(x_v\) is a unit and \(\omega_0\) is a unit differential, so \(y_v\) is integral. Equations (23)–(24) force \(y\in F\). We have therefore obtained a single global differential \(\omega=y\omega_0\) whose local image is \(d\log x_v\) everywhere. The local logarithmic differentials are Cartier-fixed, and global-local compatibility of (15) shows \(\mathcal C\omega=\omega\). Lemma (16) supplies \(b\in F^\times\) with \(\omega=d\log b\). Hence
\[
d\log(x_v/b)=0\quad\text{at every }v.
\]
The kernel of the local derivative is \(F_v^p\), as the Laurent expansion shows. Thus each \(x_v/b\) has a unique \(p\)th root. These roots are units almost everywhere, and form an idèle. We have proved
\[
\mathcal N_F\subseteq C_F^p.
\tag{25}
\]
This alone does not yet prove that \(\mathcal N_F\) is \(p\)-divisible *inside itself*. The following compactness step supplies that distinction.

**Universal-norm lifting lemma.** For every finite separable \(E/F\), norm maps \(\mathcal N_E\) onto \(\mathcal N_F\).

**Proof.** The norm of a universal norm is a universal norm: to test against a finite extension of \(F\), form its compositum with \(E\) and use tower norms. For surjectivity fix \(x\in\mathcal N_F\). For each finite separable \(L/E\), consider
\[
Y_L=\{y\in N_{L/E}C_L^1:N_{E/F}y=x\}.
\tag{26}
\]
This is a compact set, since \(C_L^1\) is compact. It is nonempty: \(x\) is a norm from \(L/F\), and its norm preimage has degree zero by the formula
\(\deg_F N_{L/F}z=[k_L:k_F]\deg_L z\). Its norm to \(E\) belongs to (26). A compositum contains any finite collection of the \(L\)'s and gives a set contained in their intersection. Compactness in \(C_E^1\) gives a point of all the \(Y_L\), which is a universal norm in \(E\) mapping to \(x\). \(\square\)

Apply (25) over every finite \(E/F\). Lift \(x\in\mathcal N_F\) to \(y\in\mathcal N_E\), write \(y=z^p\), and norm \(z\) down. Degrees show \(z\in C_E^1\). Thus the compact sets
\[
R_E=\{r\in N_{E/F}C_E^1:r^p=x\}
\tag{27}
\]
are nonempty. They have the finite-intersection property by composita. Their intersection contains a \(p\)th root of \(x\) belonging to every finite norm image, hence to \(\mathcal N_F\). This proves internal \(p\)-divisibility.

For a prime \(\ell\ne p\), first work over a finite extension \(E\) containing \(\mu_\ell\). For every sufficiently large finite \(S\), (3), valid also for these function fields, gives
\[
\mathcal N_E\subseteq C_E^\ell\operatorname{im}(U^S).
\tag{28}
\]
The tail groups \(U^S\) approach \(1\): every idèle neighborhood restricts only finitely many places, and choosing \(S\) to include them makes their components exactly \(1\). All their classes have degree zero. If an element of \(\mathcal N_E\) is a product in (28), its power factor also has degree zero, so its root has degree zero. The image \((C_E^1)^\ell\) is compact and closed. Intersecting (28) over these \(S\) therefore proves
\(\mathcal N_E\subseteq(C_E^1)^\ell\): a point outside that closed power image has a neighborhood disjoint from it, which a sufficiently small tail group cannot bridge. Universal-norm lifting and the compact root-set argument (27), with \(\ell\) in place of \(p\), now prove internal \(\ell\)-divisibility of \(\mathcal N_F\). Extensions containing \(\mu_\ell\) are cofinal among finite separable extensions, so the intersection still tests all norm images.

Finally \(C_F\) is totally disconnected. The finite idèle group has compact open profinite neighborhood subgroups, the principal subgroup is closed, and the quotient assertion of the compact-group lemma applies. Its compact subgroup \(C_F^1\), and hence the closed subgroup \(\mathcal N_F\), are profinite. A profinite group divisible by every prime has no nontrivial finite quotient: if a finite quotient has order \(m\), divisibility by the prime factors of \(m\) makes the \(m\)-power map onto, whereas that map is identically \(1\). Finite quotients separate points of a profinite group. Therefore
\[
\mathcal N_F=1.
\tag{29}
\]
Reciprocity for function fields is injective, including all characteristic-power extensions.

## 8. Function-field existence and Weil topology

Choose a class \(c\in C_F\) of degree \(1\), whose existence was proved in lesson 16, and put \(\gamma=\operatorname{rec}_F(c)\). Let
\[
\delta:B_F\longrightarrow\widehat{\mathbf Z}
\]
be restriction to the full constant-field extension. The continuous power map \(z\mapsto\gamma^z\) on \(\widehat{\mathbf Z}\) is a section of \(\delta\), since \(\delta(\gamma)=1\). In particular it is injective. The compact subgroup \(\operatorname{rec}_F(C_F^1)\), multiplied by this section, is closed and contains the dense reciprocity image from lesson 16. It is therefore all of \(B_F\). Taking constant-degree kernels gives
\[
C_F^1\xrightarrow{\sim}\ker\delta,
\qquad
\operatorname{rec}_F(C_F)=\delta^{-1}(\mathbf Z).
\tag{30}
\]
The first map is a homeomorphism, by (29) and compactness. Give the group on the right of the second equality the topology with \(\ker\delta\) compact open and its integer cosets discrete. Then (30) is a homeomorphism from \(C_F=C_F^1\times c^{\mathbf Z}\). This topology is finer than its subspace topology in the profinite group \(B_F\). Its image is dense and proper in \(B_F\), because \(\mathbf Z\) is dense and proper in \(\widehat{\mathbf Z}\).

Now let \(H\subseteq C_F\) be open of finite index. Put \(H_0=H\cap C_F^1\); it is compact open in \(C_F^1\), and \(\deg H=d\mathbf Z\) for a positive integer \(d\). Choose \(h\in H\) of degree \(d\). Every element of \(H\) is uniquely a product of an element of \(H_0\) and a power of \(h\). In \(B_F\),
\[
\overline{\operatorname{rec}_F(H)}
=\operatorname{rec}_F(H_0)\cdot
\{\operatorname{rec}_F(h)^z:z\in\widehat{\mathbf Z}\}.
\tag{31}
\]
The power group is compact and its projection is \(d\widehat{\mathbf Z}\); multiplication by \(d\) there is injective, so its constant-degree kernel is trivial. Thus (31) has kernel \(\operatorname{rec}_F(H_0)\) under constant degree and is an open finite-index subgroup of \(B_F\). To verify openness explicitly, (30) splits \(B_F\) as \(\ker\delta\times\widehat{\mathbf Z}\); on the clopen part with second coordinate in \(d\widehat{\mathbf Z}\), division by \(d\) is continuous and (31) imposes membership in the open subgroup \(\operatorname{rec}_F(H_0)\) after a continuous translation.

Its inverse image in \(C_F\) is exactly \(H\). Indeed an integer in \(d\widehat{\mathbf Z}\) belongs to \(d\mathbf Z\), and its uniquely determined exponent in the power group of (31) is that ordinary integer divided by \(d\). The remaining factor must lie in \(H_0\). Galois correspondence gives a finite abelian extension \(L/F\) with Galois kernel (31). Finite reciprocity then gives \(N_{L/F}C_L=H\). This finishes the function-field proof of Theorem 17.1 and the correspondence of Theorem 17.2.

### The absolute Weil group

Let \(G=G_F\), let \(I\) be the kernel of its constant-field map to \(\widehat{\mathbf Z}\), and choose \(\varphi\in G\) of degree \(1\). Define
\[
W_F=\{g\in G:\deg g\in\mathbf Z\}=I\rtimes\varphi^{\mathbf Z},
\tag{32}
\]
with \(I\) compact open and the integer quotient discrete. It is dense in \(G\). Let \(P=\overline{[G,G]}\). All commutators have degree zero, so \(P\subseteq I\). Density and continuity of commutators show
\[
\overline{[W_F,W_F]}^{\,W_F}=P.
\tag{33}
\]
For clarity, approximate each of the finitely many factors in a product of commutators in \(G\) by elements of \(W_F\). Their commutators converge inside \(I\), whose topology is the same in both groups. This proves that the two closures are equal; the reverse containment is immediate.

The quotient \(W_F/P\) is consequently the Hausdorff abelianization of \(W_F\). Its map to \(G/P=B_F\) is injective with image \(\delta^{-1}(\mathbf Z)\). Its degree-zero subgroup is \(I/P\simeq\ker\delta\), a compact open group, and its degree cosets are discrete. Comparing with (30) proves the full topological identification
\[
C_F\xrightarrow{\sim}W_F^{\mathrm{ab}}.
\tag{34}
\]
It is the *abelianization*, not the generally nonabelian group \(W_F\), that is identified with \(C_F\). This proves the global function-field Weil assertion used in [Weil groups and one-dimensional representations](weil-groups-and-one-dimensional-representations.md).

The local compatibility also follows. A chosen embedding of a local decomposition group takes a local Weil element of integer Frobenius degree \(m\) to global constant degree \(m\deg(v)\), so it maps into (32). On Hausdorff abelianizations its map agrees with insertion \(F_v^\times\to C_F\): Theorem 16.4 proves agreement in every finite abelian quotient, and those quotients separate the image in \(B_F\). Thus (34) respects local reciprocity, local inertia and the arithmetic Frobenius normalization.

## 9. Exercises and complete solutions

### Exercise 1 — Congruence neighborhoods over the rationals (easy)

Show that every open finite-index subgroup of \(C_{\mathbf Q}\) contains the image of
\[
U_m=\mathbf R_{>0}\times
\prod_{p\mid m}(1+p^{v_p(m)}\mathbf Z_p)
\times\prod_{p\nmid m}\mathbf Z_p^\times
\subseteq J_{\mathbf Q}
\]
for some positive integer \(m\).

**Solution.** The connected positive-real factor is contained in the subgroup, since its map to the discrete finite quotient is trivial. Under (10), openness in the unit product supplies a neighborhood restricting finitely many primes. At each restricted prime choose \(1+p^{a_p}\mathbf Z_p\) inside that neighborhood, increasing \(a_p\geq1\) if necessary. With \(m=\prod p^{a_p}\), its product with the unrestricted unit factors and the positive-real factor is the stated image of \(U_m\). One may take \(m=1\) when no prime restrictions are needed.

### Exercise 2 — The kernel as an intersection (medium)

For either kind of global field prove
\[
\ker\operatorname{rec}_K=\bigcap_{H\text{ open, finite index}}H.
\]
Explain why it is not the same nontrivial group in both cases.

**Solution.** The profinite group \(B_K\) is the inverse limit of its finite abelian Galois quotients. Their kernels pulled back to \(C_K\) are exactly the finite abelian norm groups, by Theorem 16.4. Theorem 17.1 says that these are precisely all open finite-index subgroups. Intersecting their kernels gives the assertion. Over number fields Proposition 17.3 identifies the intersection with the connected component, which contains the positive-real content factor. Over function fields (29) makes it trivial; the idèle class group is totally disconnected and its reciprocity map is injective, although not onto \(B_K\).

### Exercise 3 — The real quadratic field of conductor five (medium)

Determine the class field of the subgroup (12).

**Solution.** Reciprocity on \(\mathbf Q(\zeta_5)\) sends the normalized unit tuple to its inverse modulo \(5\). The inverse image of the subgroup \(\{1,-1\}\subseteq(\mathbf Z/5)^\times\) is exactly (12). Its fixed field is generated by \(z=\zeta_5+\zeta_5^{-1}\). Dividing \(1+\zeta_5+\cdots+\zeta_5^4=0\) by \(\zeta_5^2\) gives \(z^2+z-1=0\), whence \((2z+1)^2=5\). This quadratic field is \(\mathbf Q(\sqrt5)\), and finite reciprocity identifies (12) with its norm group. The index is \(4/2=2\), as required.

### Exercise 4 — Existence with roots of unity (hard)

Let \(K\) be a global field, \(n=\ell^a\) prime to its characteristic, and \(\mu_n\subset K\). Suppose \(H\subseteq C_K\) is open of finite index and \(C_K^n\subseteq H\). Prove existence of its class field using the full S-unit radical.

**Solution.** Choose \(S\) containing the infinite places, the divisors of \(n\), class-group generators, and every component restricted by an identity neighborhood in the inverse image of \(H\). Then \(U^S\) lies in that inverse image and \(J_K=K^\times J_K^S\). Every element of \(I(S)\) in (2) is an idèle \(n\)th power times an element of \(U^S\), so \(C(S)\subseteq H\). S-unit Kummer theory gives \(M=K(E_S^{1/n})\) with group \((\mathbf Z/n)^{|S|}\). Proposition 15.2 with \(T=\varnothing\) proves that \(C(S)\) is contained in its norm group and has index \([M:K]\); finite reciprocity makes these groups equal. In \(\operatorname{Gal}(M/K)\), take the subgroup corresponding to \(H/C(S)\), and let \(L\) be its fixed field. Restriction of reciprocity has kernel exactly \(H\), and its norm-kernel theorem gives \(H=N_{L/K}C_L\). This proof uses the exact principal-intersection and index calculation of Proposition 15.2; just saying that Kummer radicals exist would not identify the norm group.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The number-field S-unit existence argument and norm descent are retained. The characteristic-p radical and residue separation proof is written here, together with the complete function-field Weil extension and its topology.

- [Jürgen Neukirch, Class Field Theory — The Bonn Lectures, Online Edition 2.0 (May 2015), edited by Alexander Schmidt](https://www.mathi.uni-heidelberg.de/~schmidt/Neukirch-en/Neukirch_cft_02_may15.pdf).
- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).
- [John Tate, Number theoretic background (1979), freely available paper](https://ncatlab.org/nlab/files/TateNumberTheory.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.

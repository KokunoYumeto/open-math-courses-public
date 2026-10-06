# Specialization maps and tame ramification

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A finite étale cover of a proper special fibre extends over a henselian neighbourhood. Restricting that extension to a more general fibre produces specialization in the opposite direction on fundamental groups. We first make the choices in this construction explicit. We then prove surjectivity without adding a finite-presentation hypothesis to the given proper flat family.

The second part explains a local obstruction to extending covers: ramification at a discrete valuation. Abhyankar's lemma removes tame ramification after a sufficiently ramified base extension. The specializations that become isomorphisms require additional purity results; those are stated precisely at the end.

We use the finite-cover and profinite-group conventions of *The étale fundamental group*. The proper henselian equivalence, proper field-extension invariance and homotopy sequence are proved or precisely imported in *Fundamental groups of proper schemes and the homotopy exact sequence*. All connected fibres below are nonempty.

## 1. Which specialization has been chosen?

Let \(f:X\to S\) be proper, with geometrically connected fibres, and let \(s'\leadsto s\) mean that \(s\) lies in the closure of \(\{s'\}\). Choose geometric points \(\bar s'\) and \(\bar s\), with algebraically closed fields \(\Omega'\) and \(\Omega\). Inside \(\Omega\), choose the separable closure \(k_s^{\mathrm{sep}}\) of \(k_s=\kappa(s)\). Put
\[
A=\mathcal O_{S,s}^{\mathrm{sh}},
\qquad A/\mathfrak m_A=k_s^{\mathrm{sep}}.                 \tag{1.1}
\]

The map \(\operatorname{Spec}A\to\operatorname{Spec}\mathcal O_{S,s}\) is faithfully flat. Consequently a prime of \(A\) lies over the point corresponding to \(s'\). Its residue field is separable algebraic over \(\kappa(s')\): strict henselization is a filtered colimit of pointed étale neighbourhoods, whose residue extensions at any point are finite separable. Embed this residue field in \(\Omega'\). We obtain a lift
\[
\varphi:\bar s'\longrightarrow\operatorname{Spec}A
\quad\text{over }S.                                      \tag{1.2}
\]
The choice of \(\varphi\), including its prime and residue-field embedding, is part of a geometric specialization.

Restriction to the closed fibre gives an equivalence
\[
\operatorname{FÉt}(X_A)\simeq
\operatorname{FÉt}(X_{k_s^{\mathrm{sep}}})
\simeq\operatorname{FÉt}(X_{\bar s}).                       \tag{1.3}
\]
The first equivalence is the proper henselian result. For the second, pass first from the separably closed field to its algebraic closure by purely inseparable invariance, and then to \(\Omega\) by proper algebraically closed field-extension invariance. These are the results of the preceding lesson. The scheme \(X_A\) is connected: a proper surjection with connected fibres over a connected base has connected source, by the closed-partition argument in that lesson.

Let \(j_s^*\) denote (1.3). The specialization functor is
\[
\mathcal S_\varphi=
j_\varphi^*(j_s^*)^{-1}:
\operatorname{FÉt}(X_{\bar s})\longrightarrow
\operatorname{FÉt}(X_{\bar s'}).                            \tag{1.4}
\]
A quasi-inverse of an equivalence preserves finite limits and colimits, and restriction does too. Thus (1.4) is exact. Choosing fibre-functor identifications, the Galois-category theorem supplies a continuous homomorphism
\[
\operatorname{sp}_\varphi:
\pi_1(X_{\bar s'})\longrightarrow\pi_1(X_{\bar s}).          \tag{1.5}
\]
Equivalently it is the map into \(\pi_1(X_A)\), followed by the isomorphism from the special fibre. Its direction comes from restriction of finite group actions. [Stacks, Section 0BUP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-section-specialization-map)

**Proposition 1.1.** For the fixed lift (1.2), changing quasi-inverses, fibre-functor identifications or paths between fibre base points changes (1.5) only by the corresponding inner automorphisms. The map is compatible with a morphism of proper families and with successive geometric specializations, provided the lifts are chosen compatibly.

*Proof.* Two quasi-inverses of \(j_s^*\) have a natural isomorphism: apply the full faithfulness of \(j_s^*\) to their counit identifications with the identity. Hence they give naturally isomorphic functors (1.4). If \(\alpha\) and \(\beta\) identify a pullback fibre functor with a chosen fibre functor, then \(\beta\alpha^{-1}\) is a natural automorphism of the latter, namely an element \(g\) of its fundamental group. The induced maps differ by \(h\mapsto ghg^{-1}\). Changing the endpoint base points uses the same fibre-functor calculation, with inner automorphisms on the relevant source or target. This proves the choice assertion.

For functoriality, consider \(Y\to X\) over \(T\to S\), both families proper with geometrically connected fibres. Given \(t'\leadsto t\), let \(B=\mathcal O_{T,t}^{\mathrm{sh}}\) use the field of \(\bar t\). Regard that same geometric point as \(\bar s\) over \(S\). Functoriality of strict henselization provides \(A\to B\). Choose \(\bar t'\to\operatorname{Spec}B\), and take its composite to \(\operatorname{Spec}A\) as the lift for the lower family. Pullback along
\[
Y_{\bar t'}\longrightarrow Y_B,\qquad
X_{\bar s'}\longrightarrow X_A
\]
commutes with the vertical maps. The analogous closed-fibre square also commutes. Combining these two natural squares with the equivalences (1.3) proves the square of specialization functors, hence the square of group homomorphisms. With compatible fibre identifications it commutes literally; with other identifications it commutes up to conjugacy. [Stacks, Tag 0C0K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-base-change)

For \(s''\leadsto s'\leadsto s\), write \(A'\) for the strict henselization at \(s'\). A chosen \(A\to\Omega'\) determines a prime and a residue embedding into \(A'/\mathfrak m_{A'}\): its residue field is separable algebraic over \(\kappa(s')\), so its image lies in the chosen separable closure. The universal property of a filtered étale algebra mapping into a henselian local ring gives \(A\to A'\) inducing this embedding [Stacks, Tag 08HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-map-into-henselian-colimit). If \(A'\to\Omega''\) defines the second specialization, use \(A\to A'\to\Omega''\) for the direct specialization. Restriction of the unique extension of a special-fibre cover along this composite agrees with the two successive restrictions. The counits of the equivalences identify their quasi-inverses, so this is a natural isomorphism on every object and every map. It gives
\[
\operatorname{sp}_{s'\to s}\,
\operatorname{sp}_{s''\to s'}
=\operatorname{sp}_{s''\to s}
\quad\text{up to the base-point conjugacies}.              \tag{1.6}
\]
[Stacks, Tag 0C0L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-composition) \(\square\)

If \(X\) is connected, restrictions of a cover of \(X\) along the two fibres also show that (1.5) commutes with their maps to \(\pi_1(X)\), using compatible fibre identifications.

The fixed-lift qualification matters. Two arbitrary lifts \(\varphi\) need not yield inner-conjugate homomorphisms between fixed geometric fibres. For example, take \(S=\operatorname{Spec}\mathbf R\), with both geometric points \(\operatorname{Spec}\mathbf C\), and take the proper nodal cubic
\[
X:\quad y^2z=-x^2(x+z).                                   \tag{1.7}
\]
Its normalization is \(\mathbf P^1_{\mathbf R}\), with affine parameter \(t=y/x\), \(x=-(t^2+1)\), \(y=-t(t^2+1)\). The two points over the node have \(t=i,-i\). Over \(\mathbf C\), the integral-descent calculation of the preceding lessons identifies covers with finite sets carrying a permutation that glues the first branch to the second. Consequently \(\pi_1(X_{\mathbf C})=\widehat{\mathbf Z}\), after choosing a branch order. Complex conjugation reverses this order and replaces the gluing permutation by its inverse.

Here \(A=\mathbf C\). The two lifts \(A\to\mathbf C\) given by identity and conjugation therefore induce identity and multiplication by \(-1\) on \(\widehat{\mathbf Z}\). They already differ on its quotient \(\mathbf Z/3\mathbf Z\); an abelian group has no nontrivial inner automorphisms. This disproves unrestricted independence of the geometric lift, while preserving Proposition 1.1. Identity specializations are allowed in \(s'\leadsto s\).

## 2. Valuation tests and surjectivity

It is useful to represent a chosen geometric specialization by a valuation ring.

**Proposition 2.1.** Every map (1.5) can, after the proper field-invariance identifications, be represented by the generic-to-closed specialization of a valuation ring with algebraically closed fraction field. For a Noetherian base it can also be represented by a strictly henselian DVR, using geometric points over its generic and closed points. [Stacks, Tags [0C0M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-valuation-ring), [0C0N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-discrete-valuation-ring)]

*Proof.* The image \(A/\ker\varphi\subset\Omega'\) is a local domain. The valuation-domination theorem gives a valuation ring \(R\subset\Omega'\) with fraction field \(\Omega'\) dominating this domain [Stacks, Tag 00IA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dominate). The composite \(A\to R\) is local and recovers \(\varphi\) on the generic point. Such \(R\) is strictly henselian, and its residue field is algebraically closed. One can see both assertions directly: all roots of a monic polynomial over \(R\) lie in the algebraically closed fraction field and are integral, hence belong to the integrally closed valuation ring; reducing the factorization shows that every residue polynomial splits, and a simple residue root lifts. This includes the case where \(R\) is a field.

Choose a common algebraically closed overfield of \(R/\mathfrak m_R\) and \(\Omega\) over \(k_s^{\mathrm{sep}}\). Proper field invariance identifies the two closed-fibre cover categories after this enlargement. The square involving \(X_R\) and \(X_A\) commutes on the generic fibre and on this common closed fibre. Proposition 1.1 then identifies their specialization maps.

Suppose next that \(S\) is Noetherian and \(s'\ne s\). Then \(A/\ker\varphi\) is a Noetherian local domain that is not a field [Stacks, Tag 06LJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-noetherian). There is a DVR \(V\) in its fraction field dominating it [Stacks, Tag 00PH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-exists-dvr). In particular \(V\subset\Omega'\). Choose a common algebraically closed residue overfield as above, and form \(V^{\mathrm{sh}}\) with that residue embedding. It remains a DVR [Stacks, Tag 0AP3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-dvr). The inclusion \(V\subset\Omega'\) extends to its separable algebraic fraction-field extension \(\operatorname{Frac}(V^{\mathrm{sh}})\) inside \(\Omega'\). Strict-henselization functoriality gives \(A\to V^{\mathrm{sh}}\), and this agrees with the original map through \(V\). Restriction along the resulting generic and closed squares proves the assertion.

If \(s'=s\), the map \(A\to\Omega'\) factors through its residue field. Use \(V=\Omega'[[t]]\), mapping \(A\) through that chosen embedding into the constant coefficients. This is a strictly henselian DVR. Proper invariance over an algebraic closure of \(\Omega'((t))\), and the same common closed-field comparison, give the required representation. A strictly henselian DVR has separably closed residue field in general, so in positive characteristic the geometric closed point must still be retained. \(\square\)

**Theorem 2.2.** Let \(f:X\to S\) be flat and proper, with geometrically connected fibres. If \(X_s\) is geometrically reduced, then every chosen specialization
\[
\operatorname{sp}_\varphi:
\pi_1(X_{\bar s'})\longrightarrow\pi_1(X_{\bar s})
                                                               \tag{2.1}
\]
is surjective. No Noetherian or finite-presentation condition on \(S\) or \(f\) is added. [Stacks, Tag 0C0P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-surjective)

*Proof.* Use the valuation-ring representation of Proposition 2.1, with fraction field algebraically closed. A flat finite-type algebra over a valuation ring is finitely presented [Stacks, Tag 053E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-flat-finite-type-valuation-ring-finite-presentation). Thus \(X_R\to\operatorname{Spec}R\) is of finite presentation: it is locally of finite presentation on affine charts, and properness supplies quasi-compactness and quasi-separatedness.

For a flat proper morphism of finite presentation, the locus of geometrically reduced fibres is open [Stacks, Tag 0C0E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-geometrically-reduced-open). It contains the closed point of the local scheme \(\operatorname{Spec}R\), hence contains the entire scheme. We can therefore apply the preceding lesson's homotopy sequence:
\[
\pi_1((X_R)_{\bar\eta})\longrightarrow
\pi_1(X_R)\longrightarrow
\pi_1(\operatorname{Spec}R)\longrightarrow1.                \tag{2.2}
\]
Every finite étale cover of a strictly henselian local scheme is a disjoint union of copies of it, so the last fundamental group is trivial. Exactness makes the first arrow surjective. Proper henselian restriction identifies \(\pi_1(X_R)\) with that of the geometric closed fibre, and the field comparisons of Proposition 2.1 identify this arrow with (2.1). \(\square\)

Passing to the valuation ring before using the openness theorem is essential to this proof at the stated generality. The openness theorem and the homotopy sequence both require finite presentation; flatness and properness over the original arbitrary base alone have not supplied it.

## 3. Ramification indices and inertia

Let \(A\) be a DVR, with fraction field \(K\), residue field \(k\) and uniformizer \(\pi\). Normalize its valuation by \(v_A(\pi)=1\). For a finite separable extension \(L/K\), its integral closure \(B\) is finite over \(A\) and is a semilocal Dedekind domain. At its maximal ideals \(\mathfrak m_i\) there are DVRs \(B_i\). Write
\[
\pi=u_i\pi_i^{e_i},\qquad
f_i=[\kappa(\mathfrak m_i):k],
\qquad [L:K]=\sum_i e_i f_i.                               \tag{3.1}
\]
These are the discrete-valuation normalization results from commutative algebra [Stacks, Tag 09E8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-remark-finite-separable-extension). The equality follows by taking the length of \(B/\pi B\): \(B\) is free of rank \([L:K]\) over the PID \(A\), while its local factors have filtrations of length \(e_i\) with residue dimension \(f_i\).

The extension is **unramified** if all \(e_i=1\) and all residue extensions are separable. It is **tame** if all residue extensions are separable and each \(e_i\) is invertible in \(k\). It is **totally ramified** if there is only one maximal ideal and its residue field is \(k\). A finite separable extension that is not tame is **wildly ramified**. In residue characteristic zero every finite separable extension is tame. These definitions include the possible inseparability of residues in positive characteristic. [Stacks, Tag 09E9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-types-of-extensions)

Unramified finite separable extensions correspond exactly to finite étale integral closures. Indeed \(B\) is finite flat over \(A\), and
\(B/\pi B=\prod_i\kappa(\mathfrak m_i)\) is étale over \(k\) precisely when the stated index and residue conditions hold. The generic fibre is already étale. The finite flat fibre criterion for étaleness then proves the assertion. We use the usual permanence of finite étale algebras from the étale-morphism prerequisite.

For a Galois extension with group \(G\), choose \(\mathfrak m\) over the maximal ideal of \(A\). Its **decomposition group** and **inertia group** are
\[
D=\{\sigma\in G: \sigma\mathfrak m=\mathfrak m\},\qquad
I=\ker\bigl(D\to\operatorname{Aut}_k\kappa(\mathfrak m)\bigr).
                                                               \tag{3.2}
\]
Galois automorphisms act transitively on the primes over \(\pi\). To check transitivity, suppose there were two orbits. The Chinese remainder theorem gives \(b\in B\) with residues zero on one orbit and one on another. The product \(\prod_{\sigma\in G}\sigma(b)\) lies in \(B^G=A\), but has residues zero and one above the same maximal ideal of \(A\), a contradiction. Consequently all \(e_i=e\) and \(f_i=f\), and \(|D|=ef\). The residue extension is normal and \(D\to\operatorname{Aut}_k\kappa(\mathfrak m)\) is onto, by the residue-action lemma [Stacks, Tag 09ED](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-galois-galois). In particular \(|I|=e f_{\mathrm{ins}}\), where \(f_{\mathrm{ins}}\) is the inseparable residue degree. [Stacks, Tag 09EB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-galois-conclusion)

Put \(C=B_{\mathfrak m}\), with uniformizer \(q\) and residue \(\ell\). Inertia acts trivially on \(\ell\). Thus
\[
\theta:I\longrightarrow\ell^*,\qquad
\theta(\sigma)=\overline{\sigma(q)/q}                       \tag{3.3}
\]
is a homomorphism. Replacing \(q\) by \(a q\) multiplies the ratio by \(\sigma(a)/a\), whose residue is one. Hence \(\theta\) is independent of the uniformizer. Applying \(\sigma\) to \(\pi=u q^e\) shows \(\theta(\sigma)^e=1\). Define
\[
P=\ker\theta,\qquad I_t=I/P.                               \tag{3.4}
\]
The group \(P\) is wild inertia; \(I_t\) is tame inertia, a quotient of \(I\), rather than a specified subgroup. [Stacks, Tag 0BU4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-wild-inertia)

Here is the mechanism behind the terminology. An element of \(P\) fixes both \(\ell\) and \(q\) to first order. It therefore acts trivially on the whole graded ring
\(\bigoplus_{r\ge0}q^rC/q^{r+1}C=\ell[\bar q]\).
This also makes \(P\) normal in \(D\), as the kernel of the action on that graded ring. If \(\sigma\in P\) has finite order \(m\) and moves \(c\in C\), put \(\delta=\sigma(c)-c\), with \(v_C(\delta)=r\). Then
\[
0=\sigma^m(c)-c=\sum_{j=0}^{m-1}\sigma^j(\delta)
\equiv m\delta\pmod{q^{r+1}C}.                             \tag{3.5}
\]
In residue characteristic zero this is impossible. In characteristic \(p>0\) it forces \(p\mid m\). Cauchy's theorem then shows that \(|P|\) is a power of \(p\): otherwise \(P\) would have an element of some different prime order.

The image of \(\theta\) is a cyclic group of roots of unity. Its order is prime to \(p\), and dividing \(|I|=e f_{\mathrm{ins}}\) by the \(p\)-power \(|P|\) shows that this order is exactly the prime-to-\(p\) part of \(e\). Thus
\[
1\longrightarrow P\longrightarrow I
 \xrightarrow{\theta}\mu_e(\ell)\longrightarrow1,           \tag{3.6}
\]
where \(\mu_e(\ell)\) has that full prime-to-\(p\) order; in characteristic zero it has order \(e\). In particular a finite Galois extension is tame exactly when \(P=1\). This includes the requirement that the residue extension be separable. [Stacks, Tag 09EE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-galois-inertia)

## 4. The model extension and towers

**Proposition 4.1.** For any \(n\ge1\), let \(a^n=\pi\) and \(K_n=K(a)\). Its degree is \(n\), its integral closure is \(A_n=A[a]\), and \(A_n\) is a DVR with uniformizer \(a\), residue field \(k\) and ramification index \(n\). The extension is separable and tame exactly when \(n\) is invertible in \(k\). If \(n\) is invertible in \(k\), every intermediate field is \(K(\pi^{1/d})\) for a divisor \(d\mid n\). [Stacks, Tag 09EV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-pull-root-uniformizer)

*Proof.* Consider \(A[T]/(T^n-\pi)\). It is free of rank \(n\), and \(T\) is a nonzerodivisor because \(T^n=\pi\). Every maximal ideal lies over \((\pi)\); the residue algebra \(k[T]/(T^n)\) has just one maximal ideal. Hence the ring is Noetherian local with maximal ideal generated by \(T\). It is a regular local ring of dimension one, so a DVR and in particular a domain. Its fraction field has degree \(n\) over \(K\), and normality identifies the ring with the integral closure. Its residue and ramification assertions follow from \(\pi=a^n\).

If \(n\) is invertible in \(k\), the derivative \(nT^{n-1}\) is nonzero over \(K_n\), and the residue field is unchanged; this proves separability and tameness. Conversely tameness of this separable extension requires its index \(n\) to be invertible in \(k\). If \(\operatorname{char}K=p\mid n\), the extension has an inseparable part, so it is outside the finite-separable definition of wild ramification. In mixed characteristic it remains separable, and \(p\mid n\) makes it wild.

For the final assertion, first show that every \(n\)-th root of unity in \(K_n\) lies in \(K\). Such a root \(\zeta\) is an integral unit. Write it uniquely as \(c+b\), where \(c\in A\) and \(b\in Aa+\cdots+Aa^{n-1}\). If \(b\ne0\), its valuation \(r\) in \(A_n\) is positive and is not divisible by \(n\): the valuations of its nonzero terms are distinct modulo \(n\). Since \(\zeta\) is a unit, \(c\) is a unit. The leading term of
\((c+b)^n-c^n\) has valuation \(r\), because \(n\) is a unit and all terms containing \(b^2\) have larger valuation. But \(1-c^n\in A\) has valuation divisible by \(n\), or is zero. This contradiction proves \(b=0\).

Let \(F\) be intermediate and put \(m=[K_n:F]\). The conjugates of \(a\) over \(F\) are \(a\) times \(n\)-th roots of unity in a splitting field. Therefore
\(\operatorname{Norm}_{K_n/F}(a)=\zeta a^m\), where \(\zeta^n=1\). The ratio belongs to \(K_n\), so the preceding argument gives \(\zeta\in K\). Hence \(a^m\in F\). If \(d=n/m\), the already proved degree assertion gives
\([K(a^m):K]=d=[F:K]\), proving \(F=K(a^m)=K(\pi^{1/d})\). \(\square\)

**Proposition 4.2.** Tame finite separable extensions are closed under composition and subextensions, with tameness required at every prime in the intermediate integral closure. [Stacks, Tags [0EXU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-composition-tame), [0EXV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-subextension-tame)]

*Proof.* For a tower of DVRs \(A\subset B\subset C\), expressing the first uniformizer in terms of the second and then the third gives
\[
e(C/A)=e(C/B)e(B/A).                                      \tag{4.1}
\]
The residue fields form a tower, so separability is transitive. Indices prime to the residue characteristic remain prime to it under multiplication. Apply this at every maximal ideal of the integral closure in the top field to prove composition.

For a subextension, every maximal ideal of its integral closure has a prime above it in the top integral closure by lying over. Equation (4.1) makes its index a divisor of the top index. Its residue field is a subfield of a finite separable extension of \(k\), hence is separable over \(k\). This proves the claim. The same argument with every index equal to one proves closure of unramified extensions under subextensions. [Stacks, Tag 0BRL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-multiplicative-e-f) \(\square\)

## 5. Removing tame ramification

We need to distinguish finite unramified extensions from a local statement that also permits transcendental residue extensions. For an arbitrary local extension of DVRs \(C\subset D\), the commutative-algebra criterion is
\[
\begin{aligned}
&C\to D\text{ formally smooth for the }\mathfrak m_D
 \text{-adic topology}
\\
&\Longleftrightarrow\quad
e(D/C)=1,\ \kappa(D)/\kappa(C)\text{ separable}.
\end{aligned}             \tag{5.1}
\]
Here separability of a possibly infinite field extension means geometric reducedness. This is the infinitesimal flatness-and-fibre criterion [Stacks, Tag 09E7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-extension-dvrs-formally-smooth).

We also use its normalized-base-change form: if (5.1) holds, then after any finite extension of \(\operatorname{Frac}C\), every local DVR in the normalized base change again satisfies (5.1). More precisely, for \(F_1/F=\operatorname{Frac}C\) finite and \(C_1\) its integral closure, the tensor product
\(\operatorname{Frac}D\otimes_F F_1\) is reduced, the integral closure of \(D\) in it is \(D\otimes_C C_1\), and the induced local extensions at matching maximal ideals are formally smooth [Stacks, Tag 09EQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-formally-smooth-goes-up). These precise commutative-algebra inputs are used below; they assert no tame-ramification-removal theorem.

**Theorem 5.1 (Abhyankar's lemma for DVRs).** Let \(A\subset B\) be a local extension of DVRs, with fraction fields \(K\subset L\), ramification index \(e\), and separable residue extension. Assume \(e\) is invertible in the residue field of \(A\). Let \(K_1/K\) be any finite field extension. Write \(A_1\) for the integral closure of \(A\) in \(K_1\), and \(B_1\) for the integral closure of \(B\) in
\[
(L\otimes_K K_1)_{\mathrm{red}}.
\]
Fix a maximal ideal \(\mathfrak q\) of \(A_1\) with
\(e((A_1)_{\mathfrak q}/A)\) divisible by \(e\). For every maximal ideal \(\mathfrak r\) of \(B_1\) over \(\mathfrak q\),
\[
(A_1)_{\mathfrak q}\longrightarrow(B_1)_{\mathfrak r}
\text{ is formally smooth in the }\mathfrak r\text{-adic topology}.
                                                               \tag{5.2}
\]
The residue extension \(B/A\) need not be algebraic and \(K_1/K\) need not be separable. [Stacks, Tag 0BRM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-abhyankar)

*Proof.* First take \(K_1=K(\pi^{1/e})\), with \(\pi\) a uniformizer of \(A\). Its integral closure \(A_1=A[\theta]\), \(\theta^e=\pi\), is the DVR of Proposition 4.1. For a uniformizer \(q\) of \(B\), write \(\pi=wq^e\) with \(w\in B^*\). Then
\[
L\otimes_K K_1
=L[T]/(T^e-\pi)
=L[Z]/(Z^e-w),\qquad T=qZ.                                \tag{5.3}
\]
The algebra \(B[Z]/(Z^e-w)\) is finite étale over \(B\), since \(e\) and \(Z\) are units. It is normal, being étale over a DVR; consequently it is exactly the integral closure \(B_1\) in (5.3). At any of its maximal ideals \(B\to(B_1)_{\mathfrak r}\) has index one and finite separable residue extension. Multiplying indices around the square with \(A,A_1,B,(B_1)_{\mathfrak r}\) gives
\[
e\cdot e((B_1)_{\mathfrak r}/A_1)=e\cdot1,
\]
so the new vertical index is one. Since \(A_1\) has the same residue field as \(A\), the new residue extension is separable, by transitivity through \(\kappa(B)\). Criterion (5.1) proves (5.2) in this case.

Now put \(C=(A_1)_{\mathfrak q}\), with uniformizer \(\pi_1\), and write
\[
\pi=u\pi_1^{e_1},\qquad u\in C^*,\qquad e\mid e_1.          \tag{5.4}
\]
Suppose first that \(u=v^e\) in \(K_1\). Then
\(\theta=v\pi_1^{e_1/e}\in K_1\) satisfies \(\theta^e=\pi\). The intermediate field \(K'=K(\theta)\) has integral closure \(A'=A[\theta]\). The first part proves formal smoothness for each local factor of the normalization over \(A'\). Apply the normalized-base-change input stated before the theorem to the finite extension \(K_1/K'\). Transitivity of integral closure identifies the resulting local factors with the prescribed \((B_1)_{\mathfrak r}\), over \(C\). This proves the assertion when \(u\) is an \(e\)-th power.

Finally adjoin an \(e\)-th root of \(u\) to \(K_1\). The polynomial \(Z^e-u\) defines a finite étale algebra over \(C\), so its field factors give unramified extensions at the primes under consideration. Choose one such field extension \(K_2/K_1\). At any prescribed \(D=(B_1)_{\mathfrak r}\), \(u\) is also a unit, so the same polynomial defines a finite étale algebra over \(D\). Its normality identifies it with the integral closure of \(D\) in the corresponding reduced field tensor product. Choose a local factor \(D_2\) over \(D\), and let \(C_2\) be the matching local integral closure over \(C\). Both horizontal extensions in
\[
\begin{matrix}
 C&\longrightarrow&C_2\\
 \big\downarrow&&\big\downarrow\\
 D&\longrightarrow&D_2
\end{matrix}                                               \tag{5.5}
\]
have index one and finite separable residue extensions. The middle part of the proof applies to \(K_2\), where \(u\) has the required root, and gives formal smoothness of \(C_2\to D_2\).

Index multiplication in (5.5) now gives \(e(D/C)=1\). The extension \(\kappa(D_2)/\kappa(C)\) is separable, first through \(\kappa(C_2)\); therefore its subfield \(\kappa(D)\) is separable over \(\kappa(C)\). Criterion (5.1) gives formal smoothness of \(C\to D\). This argument applies to every \(\mathfrak r\) over the chosen \(\mathfrak q\), proving the full assertion. \(\square\)

For finite separable \(L/K\), the conclusion means that every field factor of \(L\otimes_K K_1\), at the primes over \(\mathfrak q\), is unramified over \(C\). Taking \(K_1=K(\pi^{1/e})\) is the particularly useful case. Normalization in this statement is essential; the unnormalized tensor product can have intersecting branches and need not be étale.

## 6. Permanence after changing the valued field

The DVR form of Abhyankar's lemma also supplies the remaining permanence statements.

**Proposition 6.1 (Kummer characterization).** A finite separable \(L/K\) is tame over \(A\) if and only if there is an integer \(n\) invertible in \(k\) and an unramified extension \(F/K(\pi^{1/n})\) containing \(L\). If \(L/K\) is tame and \(n_0\) is the least common multiple of its indices \(e_i\), every multiple \(n\) of \(n_0\) invertible in \(k\) works. [Stacks, Tag 0EXW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-characterize-tame)

*Proof.* Choose such a multiple \(n\), and factor
\[
L\otimes_K K(\pi^{1/n})=\prod_j F_j.                       \tag{6.1}
\]
Apply Theorem 5.1 to every \(A\subset B_i\), with the base extension of index \(n\). Every local normalization over \(A_n\) has index one and separable residue field. Each \(F_j\) is therefore unramified over \(A_n\). The map \(L\to F_j\) is injective, so any factor provides \(F\). Conversely the model extension \(K(\pi^{1/n})/K\) is tame, and an unramified extension of it is tame. Composition and subextension closure from Proposition 4.2 give tameness of \(L/K\). \(\square\)

**Proposition 6.2.** Tame finite separable extensions in a fixed separable closure have tame composita and tame Galois closures. Unramified extensions have the analogous properties. [Stacks, Tags [0EXR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-permanence-unramified), [0EXX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-permanence-tame)]

*Proof.* For unramified extensions \(F_1,F_2\), their integral closures are finite étale over \(A\). Their tensor product is again finite étale and normal. Its generic field factors include the specified compositum; the corresponding factor of the ring is its integral closure. Hence the compositum is unramified. A conjugate of an unramified extension is unramified, since a \(K\)-embedding carries its integral closure and primes isomorphically to those of the conjugate. The finite compositum of all conjugates is the Galois closure, proving that assertion as well.

For tame \(L_1,L_2\), choose a common \(n\) in Proposition 6.1 and enlarge each to an unramified extension \(F_i\) of \(K_n\) inside the fixed separable closure. The unramified compositum \(F_1F_2/K_n\) is tame over \(K\). Its subextension \(L_1L_2\) is tame. Each \(K\)-conjugate of a tame extension is tame by the same transport of its valuation data. Repeatedly taking these composita gives a tame Galois closure. \(\square\)

**Proposition 6.3.** Let \(A\subset B\) be any local extension of DVRs, with fraction fields \(K\subset L\). If a finite separable \(F/K\) is unramified or tame over \(A\), then every field factor of \(F\otimes_K L\) is respectively unramified or tame over \(B\). [Stacks, Tag 0EXY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-tame-goes-up)

*Proof.* In the unramified case the integral closure \(C\) of \(A\) in \(F\) is finite étale. Thus \(B\otimes_A C\) is finite étale over \(B\), and normal. It is the integral closure of \(B\) in \(F\otimes_K L\), which is a product of finite separable fields. Every factor is unramified.

For the tame case, first analyze the base change of \(K_n/K\), with \(n\) invertible in \(k\). Write \(\pi=u q^r\) in \(B\), put \(g=\gcd(n,r)\), and \(m=n/g\). There is a homomorphism
\[
B[T]/(T^n-uq^r)\longrightarrow
B[Y,Z]/(Y^m-q,\ Z^n-u),\qquad T\longmapsto ZY^{r/g}.
                                                               \tag{6.2}
\]
It is injective. To check this, pass to the fraction field and then its algebraic closure. Every root \(t\) of \(T^n-uq^r\) is obtained by choosing a root \(y\) of \(Y^m-q\) and setting \(z=t/y^{r/g}\), which satisfies \(z^n=u\). Thus every point of the separable source algebra appears in the target; the source map is injective over the fraction field, and its source is \(B\)-free, so injective already over \(B\).

The ring \(B[Y]/(Y^m-q)\) is the model DVR of Proposition 4.1. Adjoining \(Z\) is finite étale, because \(u,n\) are units. Consequently every field factor of the right side of (6.2) is tame over \(B\). Each field factor of the left side embeds in one of those factors. By subextension closure it too is tame.

Now enlarge \(F\) to an unramified \(F'/K_n\), as in Proposition 6.1. Factor \(K_n\otimes_K L\) into fields \(L_j\). The preceding calculation shows that every \(L_j/L\) is tame over \(B\). Apply the unramified case of this proposition to the extension from \(A_n\) to each local DVR in the normalization of \(B\) in \(L_j\). It shows that the field factors of \(F'\otimes_{K_n}L_j\) are unramified there, hence tame over \(B\) by composition. Finally \(F\otimes_K L\to F'\otimes_K L\) is faithfully flat: it is the base change of the finite field extension \(F'/F\). Thus every field factor of \(F\otimes_K L\) embeds in a field factor on the right. Subextension closure finishes the proof. \(\square\)

## 7. Tameness along a boundary and two degenerations

For a locally Noetherian \(X\), let \(U\subset X\) be a connected dense open. Assume that the local ring at the generic point \(\xi\) of every prime divisor in \(X\setminus U\) is a DVR. A finite étale cover \(Y\to U\) is **tame over \(X\) in codimension one** when every field factor of
\[
Y\times_U\operatorname{Spec}\operatorname{Frac}\mathcal O_{X,\xi}
\]
is tame with respect to that DVR. This is a definition relative to the specified boundary, not a claim about arbitrary compactifications. [Stacks, Section 0BSE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-section-tame)

Finite products of such covers stay tame by Proposition 6.2, applied to the field factors at each \(\xi\). Subobjects, connected components and quotients stay tame by Proposition 4.2. In particular finite colimits in the finite étale category stay tame: on the generic boundary field their factors are subfields of the common finite tame extensions dominating the input factors. The inherited fibre functor therefore satisfies the Galois-category axioms of the preceding lessons. Define
\[
\pi_1^t(U/X,\bar u)=
\operatorname{Aut}\bigl(Y\mapsto Y_{\bar u}\bigr)
\quad\text{on these covers}.                              \tag{7.1}
\]
Restriction from all covers gives a continuous surjection
\(\pi_1(U,\bar u)\twoheadrightarrow\pi_1^t(U/X,\bar u)\), because the inclusion of the tame category is fully faithful. [Stacks, Tag 0HFY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-definition-tame-fundamental-group)

A concrete boundary cover is
\[
\operatorname{Spec} A[T]/(T^e-f)\longrightarrow\operatorname{Spec}A,
                                                               \tag{7.2}
\]
where \(A\) is Noetherian, \(f\) is a nonzerodivisor, \(A/fA\) is reduced, and \(e\) is invertible in \(A\). The algebra is free with basis \(1,T,\ldots,T^{e-1}\). Over \(D(f)\), \(T\) and the derivative \(eT^{e-1}\) are units, so it is finite étale. At a minimal prime \(\mathfrak p\) over \(f\), the local quotient \(A_{\mathfrak p}/fA_{\mathfrak p}\) is a reduced zero-dimensional Noetherian local ring, hence a field. Its maximal ideal is generated by the nonzerodivisor \(f\); thus \(A_{\mathfrak p}\) is a DVR with uniformizer \(f\). Proposition 4.1 proves tameness there. These are exactly the boundary divisors, proving that (7.2) is tame in codimension one. [Stacks, Tag 0EYF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-example-tamely-ramified)

### 7.1. Good reduction

Let an elliptic curve over the fraction field of a DVR \(A\) have good reduction, meaning that it extends to an elliptic scheme \(\mathcal E\to\operatorname{Spec}A\). This is smooth and proper with geometrically connected fibres. In particular it is flat and its special fibre is geometrically reduced. Theorem 2.2 gives
\[
\pi_1(\mathcal E_{\bar\eta})\twoheadrightarrow
\pi_1(\mathcal E_{\bar s}).                                \tag{7.3}
\]
A constant elliptic curve over a field, base changed to its power-series DVR, supplies an example in every characteristic. Smoothness is the extra hypothesis that will allow the stronger results in Section 8.

### 7.2. The Legendre degeneration

Let \(A\) be a DVR with uniformizer \(\lambda\), and assume \(2\in A^*\). Consider the projective family
\[
\mathcal C:\quad y^2z=x(x-z)(x-\lambda z)
 \ \subset\mathbf P^2_A.                                 \tag{7.4}
\]
It is proper and of finite presentation. It is flat over \(A\): in the homogeneous polynomial ring, if \(\lambda G=FH\), where \(F\) is the displayed equation, reduction modulo \(\lambda\) gives \(\bar F\bar H=0\). Since \(\bar F\ne0\) in the polynomial ring over the residue field, \(H=\lambda H'\), and cancellation gives \(G=FH'\). Thus its homogeneous coordinate ring is \(\lambda\)-torsion free. Localizing and taking degree-zero parts proves torsion freeness on projective affine charts, which over a DVR is flatness.

The generic affine equation has the three distinct roots \(0,1,\lambda\): both \(\lambda\ne0\) and \(1-\lambda\in A^*\). The partial derivative in \(y\), together with simplicity of these roots, proves smoothness on the affine chart; the point \((0:1:0)\) is smooth as well. This is a smooth plane cubic. Over an algebraic closure its global functions are that field and its genus is one by the plane-curve cohomology formula [Stacks, Tag 0BYD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-plane-curve); hence it is geometrically connected.

The special fibre is
\[
y^2z=x^2(x-z).                                           \tag{7.5}
\]
Over an algebraic closure of the residue field it is irreducible: as a polynomial linear in \(z\), its coefficients \(y^2+x^2\) and \(-x^3\) are relatively prime, so the primitive linear polynomial is irreducible. Its only singularity is \((0:0:1)\), where the tangent cone is \(y^2+x^2\). Because the characteristic is not two, this has two distinct lines over the algebraic closure. The fibre is thus reduced, connected and nodal. Its normalization is a projective line, with two points above the node.

All the hypotheses of Theorem 2.2 hold, and the nodal computation from *The étale fundamental group*, Section 5.4 gives
\[
\pi_1(\mathcal C_{\bar\eta})\twoheadrightarrow
\widehat{\mathbf Z}.                                     \tag{7.6}
\]
In residue characteristic zero the generic geometric group is
\(\widehat{\mathbf Z}^{\,2}\), by the characteristic-zero curve computation, Sections 6.2–6.3. Hence (7.6) is not injective: these two profinite abelian groups have respectively four and two homomorphisms to \(\mathbf Z/2\mathbf Z\), so cannot be isomorphic. The comparison statement is explicitly an input here, not a specialization-isomorphism argument.

The condition \(2\in A^*\) cannot be dropped from this example. In residue characteristic two the displayed tangent cone is a repeated line, so this particular special fibre is not the nodal cubic just analyzed.

### 7.3. A genuinely wild separable extension

Over \(K=\mathbf F_p((t))\), let
\[
y^p-y=t^{-1}.                                            \tag{7.7}
\]
This polynomial has no root in \(K\). An element \(h\) of nonnegative valuation cannot give the negative valuation on the right; if \(v_K(h)<0\), then \(v_K(h^p-h)=p\,v_K(h)\), which cannot equal \(-1\). An Artin–Schreier polynomial of prime degree without a root is irreducible: its splitting field is obtained by adjoining one root, all roots are \(y+c\), \(c\in\mathbf F_p\), and its Galois group is a subgroup of the prime-order translation group. Thus \(L=K(y)\) is a separable Galois extension of degree \(p\).

The complete DVR \(\mathbf F_p[[t]]\) has a unique extended valuation on \(L\). Normalize its value group to \(\mathbf Z\), with \(v_L(t)=e\). Necessarily \(v_L(y)<0\), so
\[
p\,v_L(y)=-e.
\]
Hence \(p\mid e\). Equation (3.1) and \([L:K]=p\) force \(e=p\) and residue degree one. The extension is totally and wildly ramified. In fact \(u=y^{-1}\) is a uniformizer and
\[
t=\frac{u^p}{1-u^{p-1}}.
\]
Every automorphism \(y\mapsto y+c\) sends \(u\) to \(u/(1+cu)\), so its inertia character (3.3) is one. The entire group \(\mathbf Z/p\mathbf Z\) is wild inertia. The derivative of (7.7) is \(-1\); the wild ramification is compatible with separability of the fraction fields.

## 8. The smooth proper specialization theorems

For a profinite group \(G\), define
\[
G^{(p')}=\varprojlim_{N\triangleleft G\ {\rm open},\ p\nmid[G:N]}G/N.               \tag{8.1}
\]
This keeps all finite quotients whose orders are prime to \(p\); it does not keep arbitrary quotients merely because some chosen generators have prime-to-\(p\) order. Intersections of the displayed normal subgroups are again eligible, since the corresponding quotient embeds in a product of groups of prime-to-\(p\) order.

The following are stated inputs here.

**Theorem 8.1.** For a smooth proper \(f:X\to S\) with geometrically connected fibres and \(s'\leadsto s\), a chosen specialization is an isomorphism if \(\operatorname{char}\kappa(s)=0\). [Stacks, Tag 0C0Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-specialization-map-isomorphism)

**Theorem 8.2.** Under the same smooth proper hypotheses, if \(\operatorname{char}\kappa(s)=p>0\), specialization is surjective and induces
\[
\pi_1(X_{\bar s'})^{(p')}\ \xrightarrow{\ \sim\ }\
\pi_1(X_{\bar s})^{(p')}.                                 \tag{8.2}
\]
[Stacks, Tag 0C0R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-specialization-map-isomorphism-prime-to-p)

The surjectivity assertions have been proved in Theorem 2.2. The injectivity conclusions belong to *The specialization theorem for fundamental groups*, after *Purity of the branch locus*, in the course *Local cohomology, Lefschetz theorems and purity*. Those two owner lessons are forthcoming; the linked Stacks tags give the precise theorem statements. Their proofs extend a generic cover by normalization, remove its tame codimension-one ramification using Abhyankar's lemma, and then use purity to conclude étaleness everywhere. This is why the local DVR lemma alone does not prove either full isomorphism theorem. The nonsmooth Legendre special fibre demonstrates the distinction between Theorem 2.2 and these two theorems.

## 9. Exercises and complete solutions

**Exercise 9.1 (easy).** For a DVR \(A\) of residue characteristic \(p>0\), determine the degree, residue field and ramification of \(K(\pi^{1/n})\). State separately what happens when \(\operatorname{char}K=p\mid n\).

*Solution.* The local ring \(A[T]/(T^n-\pi)\) has maximal ideal \((T)\), nonzerodivisor \(T\), and dimension one, so is a DVR, free of rank \(n\) over \(A\). Thus its fraction field has degree \(n\), its residue is \(A/\pi A\), and \(\pi=T^n\) gives index \(n\). There is exactly one extended prime, so the extension is total. For \(p\nmid n\), the derivative is nonzero and the index is prime to \(p\), giving a tame separable extension. For \(p\mid n\) in mixed characteristic the field extension is separable but wild. In characteristic \(p\), write \(n=p^r m\), \(p\nmid m\); its separable part is generated by \(\pi^{1/m}\), and adjoining the remaining \(p^r\)-th root is purely inseparable of degree \(p^r\). It is therefore incorrect to describe that whole inseparable extension as a wildly ramified finite separable extension.

**Exercise 9.2 (medium).** For (7.4), verify the hypotheses of the specialization surjectivity theorem and determine the special geometric fundamental group. Explain the characteristic restriction.

*Solution.* The projective hypersurface is proper and finitely presented. Since its equation reduces to a nonzero polynomial modulo the uniformizer, the cancellation argument preceding (7.5) proves flatness on every projective affine chart. The generic polynomial \(x(x-1)(x-\lambda)\) has distinct roots, so the geometric generic fibre is a smooth connected cubic. The special polynomial is irreducible by the relatively prime coefficient argument in Section 7.2, and its node has two distinct tangent directions when \(2\) is invertible. It is therefore geometrically reduced and connected. These are both fibres of a DVR, so all fibres are geometrically connected. Theorem 2.2 applies.

For clarity, its normalization over the algebraically closed special field has parameter \(t=y/x\), with \(x=t^2+1\), \(y=t(t^2+1)\); the two points \(t^2=-1\) are identified to the node. On \(\mathbf P^1\) all finite étale covers are trivial. The descent datum across these two points is one permutation of the fibre set, with no additional relation. Thus covers correspond to finite sets with an action of \(\widehat{\mathbf Z}\), and the special fundamental group is \(\widehat{\mathbf Z}\). Specialization is consequently onto this group. In characteristic two the two tangent directions coincide, so this nodal calculation is unavailable for the given equation.

**Exercise 9.3 (medium).** Prove that (7.7) is totally and wildly ramified, and compute its wild inertia.

*Solution.* If \(h\in K\) solved the equation, then a negative valuation would give \(p v_K(h)=-1\), while a nonnegative valuation would make \(h^p-h\) integral. Both are impossible. The polynomial is therefore irreducible of degree \(p\), and its roots \(y+c\) show that the extension is Galois with translation group \(\mathbf F_p\). Its unique extended valuation satisfies \(p v_L(y)=-e\). Since \(e f=p\), we get \(e=p\), \(f=1\), and \(v_L(y)=-1\). Hence \(u=1/y\) is a uniformizer. Translation sends it to \(u/(1+cu)\), whose ratio to \(u\) has residue one. All translations lie in \(P\); since they already constitute the full group, \(P=I=\mathbf F_p\), and tame inertia is trivial.

**Exercise 9.4 (medium).** Let \(L/K\) be totally tamely ramified of degree \(e\), with integral-closure DVR \(B\). Prove directly that after adjoining \(\pi^{1/e}\), all normalized local factors are unramified. If \(A\) is strictly henselian, describe \(L\) itself.

*Solution.* Choose a uniformizer \(q\) of \(B\), and write \(\pi=wq^e\), \(w\in B^*\). The generic tensor product after adjoining \(\theta^e=\pi\) is obtained by adjoining \(Z=\theta/q\), with \(Z^e=w\). Therefore its integral closure over \(B\) is \(B[Z]/(Z^e-w)\): this algebra is finite étale, hence normal, and has exactly the required generic algebra. At every local factor its index over \(B\) is one. Since the base DVR \(A[\theta]\) has index \(e\) over \(A\), multiplication of indices gives index one for the new vertical extension. Its residue is finite separable over the residue of \(B\), which by total ramification equals that of \(A[\theta]\). Thus every new local extension is unramified.

If \(A\) is strictly henselian, the finite local ring \(B\) is henselian and has the same separably closed residue field. The residue of \(w\) has an \(e\)-th root, and that root is simple because \(e\) is invertible. Hensel's lemma lifts it to \(v\in B^*\) with \(v^e=w\). Then \((vq)^e=\pi\). The model extension generated by \(vq\) has degree \(e\), equal to \([L:K]\), so \(L=K(\pi^{1/e})\) and \(B=A[\pi^{1/e}]\). The normalized base change is in this case a product of copies of the strictly henselian DVR \(A[\theta]\), since finite étale algebras over that ring split.

**Exercise 9.5 (hard).** Fix (1.2). Prove that the auxiliary choices in its specialization homomorphism change it only by inner automorphisms, and prove the compatibility for a chain of chosen geometric specializations. Is the fixed-lift qualification dispensable?

*Solution.* Let \(E=j_s^*\) in (1.3), and let \(Q,Q'\) be two quasi-inverses. Their counits give \(EQ\simeq\mathrm{id}\simeq EQ'\). Full faithfulness of \(E\) uniquely lifts the resulting isomorphism to \(Q\simeq Q'\), naturally on covers and maps. Pulling back along the fixed \(\varphi\) preserves that isomorphism. Write \(F_{\bar s}\) and \(F_{\bar s'}\) for the chosen fibre functors, and choose
\[
\theta:F_{\bar s'}\circ\mathcal S_\varphi\xrightarrow{\sim}F_{\bar s}.
\]
For \(h\in\pi_1(X_{\bar s'})\), the induced homomorphism is
\[
\operatorname{sp}_\theta(h)
=\theta\circ(h\mathcal S_\varphi)\circ\theta^{-1}.
\]
If \(\theta'\) is another identification, then
\[
\begin{gathered}
g=\theta'\circ\theta^{-1}
\in\operatorname{Aut}(F_{\bar s})=\pi_1(X_{\bar s}),\\
\operatorname{sp}_{\theta'}=\operatorname{Ad}_g\circ\operatorname{sp}_\theta.
\end{gathered}
\]
Thus this change conjugates in the special-fibre target group. A separate change of the generic fibre-functor identification precomposes with the corresponding inner automorphism of \(\pi_1(X_{\bar s'})\). Changing endpoint base points by paths gives the same calculation on the appropriate endpoint group. This proves independence at the stated scope.

For a chain \(s''\leadsto s'\leadsto s\), the chosen map \(A\to\Omega'\) extends to \(A\to A'\) using its prime and separable residue embedding and the henselian universal property. Use \(A\to A'\to\Omega''\) for the direct lift. Both specialization functors restrict the same unique cover over \(X_A\) to \(X_{\bar s''}\); their canonical isomorphism respects every map. Hence the induced homomorphisms compose as in (1.6), up to the endpoint conjugacies.

The qualification cannot be removed. In (1.7), normalization is given homogeneously by
\[
(P:Q)\longmapsto
\bigl(-(P^2+Q^2)Q:\ -P(P^2+Q^2):\ Q^3\bigr).
\]
It is birational and proper, with the two points \(P/Q=i,-i\) above the node; it is therefore the normalization. Pullback of a cover to this projective line is a constant finite set, with a gluing permutation from the \(i\)-branch to the \(-i\)-branch. Conjugation interchanges the branches, replacing that permutation by its inverse. Identity and conjugation as lifts \(\mathbf C\to\mathbf C\) therefore give \(1\) and \(-1\) on \(\widehat{\mathbf Z}\). They cannot be related by an inner automorphism. The originally unrestricted choice assertion has this counterexample; the fixed geometric specialization has the claimed conjugacy independence.

## 10. What this lesson does not prove

The proofs above use the following inputs at their stated scopes.

- The proper henselian finite-cover equivalence, universal-homeomorphism invariance, proper algebraically closed field invariance and homotopy exact sequence are the results of the preceding owned lesson. The finite-cover categorical criteria and nodal computation belong to the earlier owned lessons.
- Strict henselization is faithfully flat and a filtered colimit of pointed étale neighbourhoods; its mapping properties are [Stacks, Tags [04GU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-strictly-henselian-functorial), [08HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-map-into-henselian-colimit)]. It preserves Noetherianity and, for a Noetherian local ring, the DVR property [Stacks, Tags [06LJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-noetherian), [0AP3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-dvr)]. Valuation domination and Noetherian DVR domination are [Stacks, Tags [00IA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dominate), [00PH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-exists-dvr)].
- Flat finite-type algebras over valuation rings are finitely presented [Stacks, Tag 053E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-flat-finite-type-valuation-ring-finite-presentation). Geometric reducedness is open for flat proper morphisms of finite presentation [Stacks, Tag 0C0E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-geometrically-reduced-open). These precise inputs enable the proof without finite presentation over the original base.
- Integral closure of a DVR in a finite separable extension is finite and semilocal Dedekind, with the local degree formula [Stacks, Tag 09E8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-remark-finite-separable-extension). The surjectivity of the decomposition-group action on the normal residue extension is [Stacks, Tag 09ED](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-galois-galois). The usual finite flat fibre criterion, étale preservation of normality and finite étale local splitting come from the étale-morphism prerequisite.
- Adic formal smoothness for an extension of DVRs is equivalent to index one and separable residue extension, including arbitrary separable residue extensions [Stacks, Tag 09E7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-extension-dvrs-formally-smooth). Its normalized finite-base-change statement, including possibly inseparable base extensions, is [Stacks, Tag 09EQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-formally-smooth-goes-up). Theorem 5.1 proves the tame ramification removal itself.
- The genus of a smooth plane curve of degree \(d\) is \((d-1)(d-2)/2\), the curve-cohomology input [Stacks, Tag 0BYD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-plane-curve). The characteristic-zero genus-one group \(\widehat{\mathbf Z}^{\,2}\) used in Section 7.2 is the stated curve consequence of *Comparison with the topological fundamental group*, Sections 6.2–6.3.
- The isomorphism parts of Theorems 8.1 and 8.2 are stated with their exact hypotheses [Stacks, Tags [0C0Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-specialization-map-isomorphism), [0C0R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-specialization-map-isomorphism-prime-to-p)]. Their proofs belong to the owner specialization lesson after purity.

No purity theorem, general compactification-independence theorem for tame covers, or analytic comparison proof is inferred from the local DVR calculations.

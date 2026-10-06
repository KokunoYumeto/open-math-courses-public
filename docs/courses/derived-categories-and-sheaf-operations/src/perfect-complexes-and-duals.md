# Perfect complexes and duals on a ringed space

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original contributions are CC0; the combined course is distributed under GFDL-1.2-or-later. Full authorship and source attribution appear in the [course notice](../LICENCE.md).*

A perfect complex is locally a finite calculation with finite projective coefficients. This finiteness has two complementary descriptions: arbitrarily accurate finite approximations, together with a bound on the degrees that tensor products can create; and a dual that permits evaluation and coevaluation. We prove the equivalence on arbitrary ringed spaces. Local rings simplify the models, but are not a hypothesis of the main theorem.

The prerequisites are [Flat modules and K-flat resolutions](flat-modules-and-k-flat-resolutions.md), Lemmas 1.2–1.3, 2.2–2.4, Theorem 3.1 and Lemma 4.1; [The derived tensor product and Tor sheaves](derived-tensor-products-and-tor-sheaves.md), Theorem 2.2 and Theorem 3.3; [Hom complexes, internal derived Hom and Ext sheaves](internal-derived-hom-and-ext-sheaves.md), Lemma 1.1, Theorems 2.2 and 3.1 and the canonical maps in Section 4; and [Derived pullback and pushforward](derived-pullback-and-pushforward.md), Theorem 1.1 and Proposition 3.2. [Injective modules and bounded-below derived functors](injective-modules-and-bounded-below-derived-functors.md), Theorem 3.3, supplies maps into K-injectives. The common reading supplies cones, their long exact cohomology sequences, and localization by roofs. The support lesson's Theorem 2.1 is used once for extension across an open complement.

Throughout, \(\mathcal O=\mathcal O_X\) is commutative and unital, and all derived categories are unbounded. Write \([K,L]=R\mathcal Hom(K,L)\). A “finite projective sheaf” here means a direct summand of \(\mathcal O^r\) for finite \(r\); a “locally finite projective sheaf” has that property on an open cover. Bounds stated locally need not be uniform on the space.

The construction follows the Stacks project authors’ *Cohomology of Sheaves*, “Strictly perfect complexes”, “Pseudo-coherent modules”, “Tor dimension”, “Perfect complexes” and “Duals”, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex). We prove the finite-model criterion and duality, including the finite-cell argument needed for the converse. Source attribution and the licence for adapted passages appear in the [course notice](../LICENCE.md).
## 1. Finite models and local maps

A complex is **strictly perfect** if it is bounded and each term is finite projective. An object is **perfect** if, on an open cover, it is isomorphic in the derived category to a strictly perfect complex. Cones, shifts and tensor products of strictly perfect complexes are strictly perfect: in each degree only finitely many summands occur; a tensor product of summands of \(\mathcal O^r\) and \(\mathcal O^s\) is a summand of \(\mathcal O^{rs}\). Pullback preserves these splittings.

**Lemma 1.1 (finite lifting and local representatives).** A map from a finite projective sheaf to the target of a sheaf epimorphism lifts near every point. If \(P\) is strictly perfect with lowest term in degree \(a\), and \(H^j(C)=0\) for \(j\ge a\), every chain map \(P\to C\) is locally null-homotopic. Every derived map \(P\to F\) is locally represented by a chain map, and a chain map that is zero in the derived category is locally null-homotopic.

**Proof.** First lift the finitely many images of the basis of \(\mathcal O^r\) on a common neighbourhood, then restrict the resulting lift to its summand. For the homotopy, descend from the highest nonzero degree \(b\) of \(P\). The degree-\(b\) component lands in cycles. Since \(H^b(C)=0\), the epimorphism \(C^{b-1}\to Z^b(C)\) permits a local lift \(h^b\). At degree \(i\), the residual map \(f^i-h^{i+1}d_P\) lands in cycles because the chain-map equation and the already constructed homotopy in degree \(i+1\) give zero after applying \(d_C\). Lift it to \(C^{i-1}\). There are finitely many degrees and shrinkings, and the result is \(f=dh+hd\).

Take a K-injective resolution \(F\to I\). Maps into \(I\) represent derived maps by the bounded-derived lesson's Theorem 3.3. If \(C\) is acyclic, then \(\mathsf H(P,C)\) is an acyclic sheaf complex: Hom from a finite projective term is a summand of a finite power of the exact identity functor, and the finite filtration by terms of \(P\) proves the assertion. Consequently \(\mathsf H(P,F)\to\mathsf H(P,I)\) is a quasi-isomorphism. A degree-zero cycle on the right lifts locally to a cycle on the left modulo a boundary, since its cohomology-sheaf map is an isomorphism. This gives an actual representative. A cycle on the left whose image is a boundary is locally a boundary on the left, giving the last assertion. The same reasoning shows that a derived map \(P\to C\), under the stated cohomology vanishing, is locally zero: first represent it, then apply the downward homotopy. \(\square\)

It follows that perfectness is independent of the chosen representative: locally realize a strictly perfect model's derived isomorphism by a chain map to that representative; it is a quasi-isomorphism because its cohomology maps are isomorphisms.

For later use, an acyclic top pair in a strictly perfect complex can be cancelled locally. If the top term is \(P^b\) and \(H^b(P)=0\), the epimorphism \(P^{b-1}\to P^b\) splits by Lemma 1.1. Its kernel is finite projective, and the complex decomposes as that shortened complex plus the contractible identity disk on \(P^b\). Repeat finitely often.

**Lemma 1.2 (finite presentation and flatness).** A flat, finitely presented sheaf is locally finite projective. If all stalk rings are local, locally finite projective sheaves are finite locally free.

**Proof.** Locally write a presentation \(\mathcal O^m\xrightarrow{A}\mathcal O^n\to F\to0\), and put \(L=\operatorname{im}A\). Flatness of \(F\) makes \(L\subset\mathcal O^n\) pure: tensoring this inclusion with any sheaf is injective, by the flat-quotient lemma. Let \(l_\alpha\) be the columns of \(A=(a_{i\alpha})\). The finite equations

\[
\sum_i a_{i\alpha}y_i=l_\alpha
\qquad(1\le\alpha\le m)
\tag{1.1}
\]

have the ambient solutions \(y_i=e_i\). Set \(T=\operatorname{coker}(A^t:\mathcal O^n\to\mathcal O^m)\). The tuple \((l_\alpha)\) maps to zero in \(T\otimes\mathcal O^n\), hence in \(T\otimes L\) by purity. Right exactness of tensor says it locally lies in the image of \(A^t\otimes L\). Thus (1.1) has solutions in \(L\) on a neighbourhood. Sending \(e_i\) to \(y_i\) gives a retraction \(\mathcal O^n\to L\), because it fixes the generators \(l_\alpha\). The quotient \(F\) is a finite free summand.

For completeness, a finite projective module over a local ring \((R,\mathfrak m)\) is free. Nakayama's lemma follows directly: if finite generators satisfy \(v=Bv\) with entries of \(B\) in \(\mathfrak m\), then \(\det(1-B)\) is a unit, and the adjugate identity gives \(v=0\). Lift a basis modulo \(\mathfrak m\) to a finite projective module \(P\). Nakayama applied to the cokernel gives a surjection \(R^r\to P\). It splits; its finite kernel has zero reduction modulo \(\mathfrak m\), so another application of Nakayama kills that kernel.

A free stalk of a finitely presented sheaf spreads to a free sheaf near that point. Lift its finite basis, and kill the stalk-zero cokernel using finitely many generators. The resulting surjection has finitely generated kernel: from a finite presentation, lift maps between the two finite free presentations; the original finite relations and the columns of the difference between their composite and the identity generate the kernel. Its zero stalk therefore kills finitely many kernel generators on a common neighbourhood. The lifted basis is an isomorphism there. Apply this to the finite projective sheaf. \(\square\)

For arbitrary stalk rings, “projective” cannot be replaced by “free”. On the one-point space with ring \(k\times k\), the summand \((1,0)R\) is not \(R^r\) for any \(r\): its two component dimensions are \((1,0)\), whereas those of \(R^r\) are \((r,r)\).

**Proposition 1.3 (Hom from a finite model).** For strictly perfect \(P\) and any complex \(F\), \(\mathsf H(P,F)\) represents \([P,F]\). If \(F\) is K-flat, this Hom complex is K-flat.

**Proof.** The finite-filtration argument in Lemma 1.1 makes \(\mathsf H(P,-)\) preserve quasi-isomorphisms, so compare \(F\to I\) with the definition \([P,F]=\mathsf H(P,I)\). Define

\[
\begin{aligned}
(P^\vee)^n&=\mathcal Hom(P^{-n},\mathcal O),\\
d_{P^\vee}^n&=(-1)^{n+1}(d_P^{-n-1})^t.
\end{aligned}
\tag{1.2}
\]

Evaluation identifies \(F\otimes P^\vee\) with \(\mathsf H(P,F)\): on homogeneous elements it sends \(f\otimes\phi\) to \(p\mapsto f\phi(p)\). The identity is clear for finite free terms and passes to summands. The Hom differential and the sign in (1.2) agree with the tensor differential. The dual is bounded with flat terms, hence K-flat; tensoring two K-flats remains K-flat. \(\square\)

## 2. Finite approximations

An object \(K\) is **\(m\)-pseudo-coherent** if locally there is a map \(P\to K\) from a strictly perfect complex, inducing isomorphisms on \(H^j\) for \(j>m\) and a surjection on \(H^m\). Equivalently, its cone has zero cohomology in degrees \(j\ge m\). It is **pseudo-coherent** if this holds for every integer \(m\). The cover may depend on \(m\). Lemma 1.1 makes this definition equivalent to using actual maps to any chosen complex representative.

Smaller thresholds impose stronger conditions. An \(m\)-approximation is also an \((m+1)\)-approximation, and shifting by \([r]\) changes the threshold to \(m-r\). Such an object is locally bounded above, because its approximation has finitely many nonzero terms. On a quasi-compact space finitely many neighbourhoods give a uniform upper bound.

Derived pullback preserves \(m\)-pseudo-coherence. Indeed, a complex with cohomology only in degrees \(\le c\) has a bounded-above flat model with terms only in those degrees, by good truncation and Lemma 4.1 of the flat lesson. Its derived pullback has the same upper bound. Pull back the approximation triangle; the strict model remains strict and the cone remains in degrees \(<m\). Similarly, if \(K\in D^{\le a}\) and \(L\in D^{\le b}\), these flat models show \(K\otimes^L L\in D^{\le a+b}\).

**Proposition 2.1 (triangles and tensor bounds).** In a triangle \(K\to L\to M\to K[1]\), the following implications hold:

1. If \(K\) is \((m+1)\)-pseudo-coherent and \(L\) is \(m\)-pseudo-coherent, then \(M\) is \(m\)-pseudo-coherent.
2. If \(K,M\) are \(m\)-pseudo-coherent, then \(L\) is \(m\)-pseudo-coherent.
3. If \(L\) is \((m+1)\)-pseudo-coherent and \(M\) is \(m\)-pseudo-coherent, then \(K\) is \((m+1)\)-pseudo-coherent.

If \(K\in D^{\le a}\) is \(n\)-pseudo-coherent and \(L\in D^{\le b}\) is \(m\)-pseudo-coherent, their tensor product is \(\max(n+b,m+a)\)-pseudo-coherent.

**Proof.** Choose approximations \(P\to K\), \(Q\to L\) at thresholds \(m+1,m\). Brutally cut \(P\) below \(m+1\), preserving that approximation. For \(C=\operatorname{Cone}(Q\to L)\), the map \(P\to L\to C\) is locally zero by Lemma 1.1: \(C\) has no cohomology in degrees \(\ge m\), whereas \(P\) starts at \(m+1\). Exactness of Hom applied to the triangle \(Q\to L\to C\) lifts \(P\to L\) to a derived map \(P\to Q\); Lemma 1.1 realizes it by a chain map locally. The triangle axiom gives a map \(\operatorname{Cone}(P\to Q)\to M\).

Here is the required cohomology check. Cone cohomology in degree \(j\) is an extension of the cokernel in degree \(j\) by the kernel in degree \(j+1\). For \(j>m\), the two cokernels are isomorphic: the map on \(H^j(Q)\) is an isomorphism and the map from \(P\)'s cohomology is onto at \(j=m+1\), an isomorphism above it. The kernels in degree \(j+1\) are isomorphic. Hence the extension map is an isomorphism. At \(j=m\), surjectivity for \(Q\) makes the cokernel map onto, and surjectivity for \(P\) at \(m+1\), with the isomorphism for \(Q\) there, makes the kernel map onto. Lifting first the kernel component and then the cokernel component proves surjectivity for the extension. Thus the cone is an approximation. Rotation and the shift rule give the other two implications.

For the tensor claim choose approximations \(P\to K\), \(Q\to L\) at thresholds \(n,m\). They can have terms only in degrees \(\le a,\le b\): cancel acyclic top pairs; if the threshold exceeds the relevant bound, the zero complex is already an approximation. Factor the tensor map through \(K\otimes^L Q\). Its first cone is \(\operatorname{Cone}(P\to K)\otimes Q\), bounded above by \(n+b-1\); its second cone is \(K\otimes^L\operatorname{Cone}(Q\to L)\), bounded above by \(a+m-1\). The octahedral cone triangle bounds the composite cone by the larger of these numbers. The source \(P\otimes Q\) is strictly perfect, proving the assertion without a Tor spectral sequence. Taking arbitrarily small thresholds proves tensor closure for pseudo-coherent objects. \(\square\)

**Proposition 2.2 (summands and criteria).** Summands of \(m\)-pseudo-coherent objects are \(m\)-pseudo-coherent. A locally bounded-above complex whose term in degree \(i\) is \((m-i)\)-pseudo-coherent is \(m\)-pseudo-coherent; the same holds if its cohomology sheaf in degree \(i\) is \((m-i)\)-pseudo-coherent. A module is \(0\)-pseudo-coherent exactly when it is of finite type, and \((-1)\)-pseudo-coherent exactly when it is finitely presented.

**Proof.** Suppose \(K\oplus L\) is \(m\)-pseudo-coherent. Its endomorphism \(1_K\oplus0\) has cone \(L\oplus L[1]\). Proposition 2.1 applies since \(m\)-pseudo-coherence implies \((m+1)\)-pseudo-coherence. Shift repeatedly; each \(L[n]\oplus L[n+1]\) is \(m\)-pseudo-coherent. Work near a point where \(L\) is bounded above. For large \(n\), \(L[n]\) has zero cohomology in degrees \(\ge m\), so the zero approximation works. Descend using the split triangles

\[
\begin{gathered}
L[n]\longrightarrow L[n]\oplus L[n-1]\\
\longrightarrow L[n-1]\longrightarrow L[n+1].
\end{gathered}
\tag{2.2}
\]

The first implication of Proposition 2.1 supplies each preceding step. Only finitely many steps are needed for a fixed threshold at a fixed point. Exchanging \(K,L\) finishes the summand assertion.

For the term criterion, remove all degrees below \(r\le m\). The finite upper tail is \(m\)-pseudo-coherent by its filtration into terms \(F^i[-i]\) and the extension implication. The lower quotient is bounded above by \(r-1<m\), so has the zero approximation. The same extension implication proves the claim. For the cohomology criterion use the finite good-truncation filtration, with quotients \(H^i(K)[-i]\), and its lower tail in degrees \(<r\).

If \(K\in D^{\le m}\), cancel the top acyclic terms in an \(m\)-approximation: \(H^m(K)\) is a quotient of a finite projective sheaf, hence finite type. If \(K\in D^{\le m+1}\), the same cancellation leaves \(H^{m+1}(K)\) as the cokernel of a map of two finite projective sheaves, hence finitely presented. Apply these facts to a module in degree zero. Conversely, a finite generating surjection in degree zero supplies a \(0\)-approximation; a finite presentation in degrees \(-1,0\) supplies a \((-1)\)-approximation. \(\square\)

## 3. Tor amplitude and the perfectness criterion

An object \(K\) has **Tor amplitude in \([a,b]\)** if, for every module sheaf \(F\) in degree zero, \(K\otimes^L F\) has cohomology only in degrees \(a\) through \(b\). It has **locally finite Tor amplitude** if such an interval exists on each member of an open cover. Taking \(F=\mathcal O\) also bounds \(K\) itself.

**Proposition 3.1 (amplitude models).** Amplitude in \([a,b]\) is equivalent to having a representative of flat sheaves with terms only in \([a,b]\). It is also equivalent to every stalk having that amplitude over its stalk ring. Derived pullback preserves the interval; tensoring objects with intervals \([a,b]\), \([c,d]\) gives interval \([a+c,b+d]\). Summands inherit amplitude.

**Proof.** A bounded complex of flat sheaves is K-flat. Its tensor with a module has terms only in the asserted interval, proving one implication. Conversely, resolve a good upper truncation of \(K\) by the bounded-above flat construction, obtaining \(P\) with terms only in degrees \(\le b\). Since \(H^i(P)=0\) below \(a\), the flat tail ending in \(P^a\) resolves

\[
F_a=\operatorname{coker}(P^{a-1}\to P^a).
\tag{3.1}
\]

For every test module \(T\), it computes \(\operatorname{Tor}_1(F_a,T)=H^{a-1}(P\otimes T)=0\). The flatness criterion makes \(F_a\) flat. Replace the lower tail by \(F_a\) in degree \(a\). This is the good lower truncation, quasi-isomorphic to \(K\), and supplies the required model.

Stalks commute with derived tensor and cohomology, by the flat lesson's stalk criterion. For the converse stalk test, any module over \(\mathcal O_x\) is the stalk at \(x\) of its exact skyscraper sheaf. Testing that sheaf proves the stalk interval from the global interval. Conversely, test a sheaf on all stalks to prove its tensor cohomology vanishes. Pullback of the bounded flat model remains bounded and flat; tensor two such models to add the bounds. Cohomology of a finite direct sum splits, proving the summand assertion. Finally, the tensor long exact sequence shows that if \(K,L\) have intervals \([a_K,b_K]\), \([a_L,b_L]\), a cone of \(K\to L\) has interval

\[
\begin{aligned}
a_M&=\min(a_L,a_K-1),\\
b_M&=\max(b_L,b_K-1).
\end{aligned}
\tag{3.2}
\]

Rotation gives the other two-out-of-three bounds. \(\square\)

**Theorem 3.2 (perfectness).** An object is perfect if and only if it is pseudo-coherent and has locally finite Tor amplitude. More precisely, amplitude \([a,b]\) and \((a-1)\)-pseudo-coherence already suffice, and give local strictly perfect models with terms in \([a,b]\).

**Proof.** A strictly perfect model is an approximation at every threshold and is a bounded flat model. This proves necessity. For the stronger converse, choose a strictly perfect approximation \(E\to K\) through degree \(a-1\), and brutally cut \(E\) below \(a-1\). The approximation and \(H^{a-1}(K)=0\) show that its cone is

\[
\begin{gathered}
C\simeq N[2-a],\\
N=\ker(E^{a-1}\to E^a).
\end{gathered}
\tag{3.3}
\]

Indeed, in degree \(a-2\) the cone cohomology is that kernel, and all other degrees vanish. Tensor the triangle with an arbitrary module \(T\). The lower amplitude bound on \(K\) and the tensor long exact sequence give

\[
\begin{gathered}
\operatorname{im}(N\otimes T\to E^{a-1}\otimes T)\\
=\ker(E^{a-1}\otimes T\to E^a\otimes T).
\end{gathered}
\tag{3.4}
\]

To identify the Tor group here, take a bounded-above flat resolution of \(N\), and append \(E^{a-1}\to E^a\). This is a flat resolution of \(E'=\operatorname{coker}(E^{a-1}\to E^a)\), whose first tensor homology is exactly the kernel modulo the image in (3.4). Thus \(\operatorname{Tor}_1(E',T)=0\) for all \(T\), and \(E'\) is flat. It is finitely presented as the cokernel of a map between finite projective sheaves. Lemma 1.2 makes it locally finite projective.

Replace the bottom pair by \(E'\) in degree \(a\). The resulting complex is quasi-isomorphic to \(K\). Cancel its finitely many acyclic top pairs above \(b\), as in Section 1; none of these cancellations crosses degree \(a\). This gives the asserted strictly perfect model. Localize the hypotheses to deduce the general equivalence. \(\square\)

**Corollary 3.3 (permanence).** Perfect objects are closed under shifts, cones, derived tensor products, retracts and derived pullback.

**Proof.** For cones, locally represent the two inputs by strict models and their map by an actual chain map, using Lemma 1.1. Its strict cone is the third object. Rotation handles any two inputs. Tensor and pullback use their strict models directly. Summands use Proposition 2.2, Proposition 3.1 and Theorem 3.2.

A retract is an actual summand here. If \(\sigma:K\to E\) and \(r:E\to K\) satisfy \(r\sigma=1\), complete \(\sigma\) to a triangle \(K\to E\to C\xrightarrow{h}K[1]\). Since \(\sigma[1]h=0\), composing with \(r[1]\) gives \(h=0\). Exactness of Hom lifts \(1_C\) to \(t:C\to E\); replace \(t\) by \(t-\sigma rt\). Then \(rt=0\), and the maps \((\sigma,t):K\oplus C\to E\) and \((r,E\to C)\) are inverse: their induced cohomology maps split the triangle, so the first is an isomorphism, and the composite on \(K\oplus C\) is the identity. The summand result therefore applies to every retract. \(\square\)

On a quasi-compact space perfect objects have uniform bounds, by a finite subcover. Without quasi-compactness this fails: on the discrete space of nonnegative integers, with stalk ring \(k\), take \(K|_{\{n\}}=k[n]\). Each neighbourhood \(\{n\}\) has a strict model, but the global nonzero cohomology degrees \(-n\) have no lower bound.

Two useful locality consequences complete the picture. If \(j:U\hookrightarrow X\), \(E\) is perfect on \(U\), and its cohomology is supported on \(T\subset U\) with \(T\) closed in \(X\), then \(Rj_*E\) is perfect. It restricts to \(E\) on \(U\) and to zero on \(X\setminus T\): restriction of a K-injective pushforward computes the pushforward from \(U\setminus T\), where the object is zero. These opens cover \(X\).

If the stalk rings are local and \(E\) is perfect, the set where all \(H^i(E)_x\) are finite free is open. Near such an \(x\) choose a strict model in \([a,b]\). Its top cohomology is finitely presented; Lemma 1.2's free-stalk argument makes it free near \(x\). Split the epimorphism from the top term to that cohomology, then split the preceding term onto its image. Remove the resulting contractible pair and the free cohomology summand. Induct on the finite length. The remaining cohomology stalks still satisfy the hypothesis, so finitely many shrinkings make all cohomology sheaves finite locally free. This also proves maximality of the stated open set.

## 4. Duals and the two tensor–Hom maps

For any object define \(K^\vee=[K,\mathcal O]\). The symmetric monoidal structure, with graded symmetry \(u\otimes v\mapsto(-1)^{|u||v|}v\otimes u\), was proved in the tensor lesson's Theorem 2.2. No boundedness is required for that structure.

**Theorem 4.1 (perfect duality).** If \(K\) is perfect, so is \(K^\vee\), and the canonical maps

\[
\begin{aligned}
K&\longrightarrow K^{\vee\vee},\\
M\otimes^L K^\vee&\longrightarrow[K,M]
\end{aligned}
\tag{4.1}
\]

are isomorphisms. In particular, for every integer \(r\),

\[
\begin{gathered}
H^rR\Gamma(X,M\otimes^L K^\vee)\\
=\operatorname{Hom}_{D(\mathcal O)}(K,M[r]).
\end{gathered}
\tag{4.2}
\]

Two further canonical maps are isomorphisms:

\[
{}[K,L]\otimes^L M\longrightarrow[K,L\otimes^L M],
\tag{4.3}
\]

\[
{}[L,M]\otimes^L K\longrightarrow[[K,L],M].
\tag{4.4}
\]

**Proof.** These are globally defined maps from the Hom lesson's Section 4. Their cones restrict to zero precisely when they are isomorphisms. Thus their invertibility can be checked on strict-model neighbourhoods. Proposition 1.3 proves the second map in (4.1) there, and (1.2) shows that the dual model is strictly perfect. The double-dual differential under the ordinary termwise identification is \(-d_P\). Consequently the canonical bidual map in degree \(i\) is

\[
p\longmapsto\bigl(\phi\mapsto(-1)^i\phi(p)\bigr).
\tag{4.5}
\]

This sign makes it a chain map and each term is an isomorphism. Equation (4.2) follows from the internal-Hom lesson's derived-section identification in every shift.

For (4.3), use \([P,L]=L\otimes P^\vee\). The map moves \(M\) past \(P^\vee\) and associates the three factors, giving \((L\otimes^L M)\otimes P^\vee\). It is therefore an isomorphism. Explicitly, for homogeneous \(\phi,m,p\), its evaluation is \((-1)^{|m||p|}\phi(p)\otimes m\); this is the same sign as moving the dual factor past \(m\).

For (4.4), the source and target are exact functors of \(K\), and its natural map respects their triangle comparisons, by the chain identities and transpose construction in the Hom lesson. For \(K=\mathcal O\) it is the identity. For a finite free sheaf it is the componentwise identity on a finite power of \([L,M]\). It passes to finite projective summands and shifts. Filter a bounded strict model by its terms; the two triangle long exact sequences show inductively that the middle map is an isomorphism when the outer two are. This proves (4.4). \(\square\)

There is a source-locator distinction: in the pinned edition, Tag 0G40 proves (4.4), the evaluation-and-more map. It does not denote (4.3). Both assertions hold for perfect \(K\), as proved above, and both can fail without that hypothesis.

A **left dual** of \(K\) is an object \(N\) with maps

\[
\begin{aligned}
\eta:\mathcal O&\longrightarrow K\otimes^L N,\\
\epsilon:N\otimes^L K&\longrightarrow\mathcal O
\end{aligned}
\tag{4.6}
\]

such that the composites

\[
\begin{aligned}
K&\xrightarrow{\eta\otimes1}K\otimes N\otimes K
\xrightarrow{1\otimes\epsilon}K,\\
N&\xrightarrow{1\otimes\eta}N\otimes K\otimes N
\xrightarrow{\epsilon\otimes1}N
\end{aligned}
\tag{4.7}
\]

are identities; tensors in (4.7) are derived and association constraints are understood. Symmetry gives the corresponding right dual, so we say **dualizable**.

**Theorem 4.2 (duals are exactly perfect objects).** Every perfect object has dual \(K^\vee\), and every dualizable object is perfect. Its dual is canonically isomorphic to \(K^\vee\).

**Proof: existence and identities.** The natural isomorphism \([K,B]=B\otimes^L K^\vee\) identifies the closed tensor–Hom adjunction with

\[
-\otimes^L K\ \dashv\ -\otimes^L K^\vee.
\tag{4.8}
\]

Let \(\eta\) be its unit at \(\mathcal O\), and \(\epsilon\) its counit there. Equivalently, \(\eta\) corresponds to \(1_K\) under \(K\otimes K^\vee\cong[K,K]\), and \(\epsilon\) is evaluation. The counit at \(B\) is \(1_B\otimes\epsilon\), since (4.1)'s map is defined by transposing this evaluation. The adjunction's first triangle identity at \(\mathcal O\) gives the first identity in (4.7). Consequently \(1_A\otimes\eta\) transposes to \(1_{A\otimes K}\) for every \(A\), and is the unit at \(A\). The second adjunction identity, at \(\mathcal O\), now gives the second identity in (4.7). These are global identities of derived maps, not an inference that equality of maps can be tested locally.

On a strict free model, \(\eta(1)=\sum_{i,\alpha}e_{i,\alpha}\otimes e_{i,\alpha}^*\), with no degree sign. If \(d e_{i,\alpha}=\sum_\beta a_{\beta\alpha}e_{i+1,\beta}\), (1.2) gives the dual differential coefficient \((-1)^i a_{\beta\alpha}\) on \(e_{i+1,\beta}^*\). Its tensor differential has the additional sign \((-1)^{i+1}\), so the two contributions cancel. Evaluating either zigzag contracts the appropriate dual basis and gives the identity. Summands inherit this description. The sign in the bidual map (4.5) and the absence of a sign in coevaluation are compatible: they are different maps with different factor orders.

**Proof: converse.** Fix \(x\in X\) and a dual \(N\) with (4.6)–(4.7). Resolve \(K\) by the actual cycle-attachment construction of Theorem 3.1 of the flat lesson, obtaining \(P\to K\). Its graded terms are sums of \(B_U=j_{U!}\mathcal O_U\). Stage zero consists of identity disks; each later stage adds generators whose differentials lie in the preceding stage. Resolve \(N\) by a K-flat complex \(Q\) with flat terms.

By Lemma 1.1, near \(x\) the map \(\eta:\mathcal O\to P\otimes Q\) is an actual chain map. Its value at one is locally a finite sum of homogeneous tensors \(p_t\otimes q_t\). Each germ \(p_t\) involves finitely many generators and a finite stage. Include those generators and all generators occurring in their differentials. A later-stage differential only uses earlier stages; its germ has finite support. At stage zero include the other member of every disk encountered. Thus closing this finite set under differentials requires finitely many steps and produces finitely many generators in finitely many degrees.

This germ argument gives an actual local subcomplex. At each step choose representatives of the finitely many differential germs. Their expressions involve finitely many summands after shrinking. A summand \(B_U\) with \(x\notin U\) has zero stalk there; kill its finitely many section contributions on a smaller neighbourhood and omit it. For the remaining summands shrink inside their finitely many \(U\)'s, where they are copies of \(\mathcal O\). Equality of each chosen expression with the actual differential is a germ equality, so shrink to make all these finitely many equalities hold. The result is a bounded finite free subcomplex

\[
E\subset P|_V
\tag{4.9}
\]

on a neighbourhood \(V\) of \(x\), termwise a graded summand, containing all the \(p_t\). Tensoring this inclusion with \(Q\) is injective termwise (also by flatness of \(Q\)). Since \(\eta(1)\) is a cycle, its expression in \(E\otimes Q\) is a cycle. Hence \(\eta\) factors through \(\widetilde\eta:\mathcal O\to E\otimes^L N\).

Define \(\sigma:K|_V\to E\) by \(\widetilde\eta\otimes1_K\), followed by \(1_E\otimes\epsilon\), and let \(r:E\to K|_V\) be inclusion followed by the resolution isomorphism. The first identity in (4.7) gives \(r\sigma=1_K\). Corollary 3.3 makes this retract of a strictly perfect object perfect. Every point has such a neighbourhood, proving the converse. This uses finite free cells, rather than incorrectly assuming that a submodule generated by finitely many sections is projective.

Finally any dual supplies an adjunction \(-\otimes K\dashv-\otimes N\): insert \(\eta\) to transpose a map, and insert \(\epsilon\) to transpose back; the two identities make these operations inverse. Right adjoints are uniquely isomorphic by their natural Hom bijections (evaluate one bijection on the identity, then the other, to obtain inverse maps). Comparing with the closed tensor–Hom adjunction at \(\mathcal O\) identifies \(N\) canonically with \([K,\mathcal O]\). \(\square\)

## 5. Residues and finiteness examples

**A smooth analytic surface residue is perfect.** On \(\mathbb C^2\) let \(\mathcal O\) be holomorphic functions and \(S\) the residue skyscraper at the origin. Its resolution, in degrees \(-2,-1,0\), is

\[
\mathcal O\xrightarrow{\binom{-y}{x}}\mathcal O^2
\xrightarrow{(x\ y)}\mathcal O\longrightarrow S.
\tag{5.1}
\]

The tensor lesson's [holomorphic coordinate germ lemma](derived-tensor-products-and-tor-sheaves.md#holomorphic-coordinate-germs) proves, in \(R=\mathcal O_{\mathbf C^2,0}\), that the evaluation kernel is \((x,y)\), that multiplication by \(x\) is injective, and that multiplication by \(y\) is injective on \(R/(x)\cong\mathcal O_{\mathbf C,0}\). Thus if \(xa+yb=0\), reduction modulo \(x\) gives \(y\bar b=0\), so \(b=xc\) for some \(c\in R\). The equation then reads \(x(a+yc)=0\), and injectivity gives \(a=-yc\). This proves middle exactness. If \((-yc,xc)=0\), its second component and the same injectivity give \(c=0\), proving injectivity of the first map. Evaluation is onto by constants and has kernel \((x,y)\), so exactness holds also at the last two terms.

Away from the origin one coordinate is a holomorphic unit by that lemma, and \(S\) has zero stalk. If \(x\) is a unit, the degree-minus-one homotopy is given by \(h^0(t)=(x^{-1}t,0)\) and \(h^{-1}(a,b)=x^{-1}b\). If \(y\) is a unit, use \(h^0(t)=(0,y^{-1}t)\) and \(h^{-1}(a,b)=-y^{-1}a\). Substitution into the two displayed differentials gives \(dh+hd=1\) in each of degrees \(-2,-1,0\), so the complex contracts. This proves exactness on every stalk, hence perfectness. For a residue vector space \(V\) at zero, all differentials vanish, so its Tor groups in degrees \(0,1,2\) are \(V,V^2,V\). Taking \(V=k\) gives \(k,k^2,k\). The local Tor amplitude is exactly \([-2,0]\).

**A singular residue need not be perfect.** Over \(R=k[\epsilon]/(\epsilon^2)\), the residue \(k\) has the free resolution

\[
\cdots\xrightarrow{\epsilon}R\xrightarrow{\epsilon}R
\xrightarrow{\epsilon}R\longrightarrow k
\tag{5.2}
\]

in nonpositive degrees. Kernel and image of multiplication by \(\epsilon\) both equal \(\epsilon R\). Every finite brutal lower truncation gives an approximation: it is an isomorphism in all higher degrees and surjective at the bottom threshold. Thus \(k\) is pseudo-coherent. Tensoring (5.2) with \(k\) kills every differential, so \(\operatorname{Tor}_n^R(k,k)=k\) for every \(n\ge0\). It has no finite Tor amplitude, is not perfect, and is not dualizable. The singularity hypothesis matters; a surface residue alone does not imply nonperfectness.

**Perfectness does not force finite cohomology over every ring.** Let

\[
\begin{gathered}
R=k[x]\oplus Y,\qquad Y=\bigoplus_{n\ge1}ky_n,\\
Y^2=0,\qquad xY=0.
\end{gathered}
\tag{5.3}
\]

The two-term complex \(R\xrightarrow{x}R\), in degrees \(-1,0\), is strictly perfect. But its negative cohomology is \(Y\), which is not finitely generated: the action on \(Y\) factors through \(k\), and finitely many elements span only a finite-dimensional subspace. Hence even a perfect, and therefore pseudo-coherent, complex need not have finite-type cohomology over a noncoherent ring. The safe assertions are the approximation definition and Proposition 2.2's explicitly bounded top-cohomology conclusions.

## 6. Exercises with checked solutions

**Exercise 1 (easy: the shifted unit).** For \(K=\mathcal O[1]\), compute its dual, coevaluation and bidual map, and check both identities in (4.7).

**Solution.** Its generator \(e\) has degree \(-1\), and the dual generator \(e^*\) has degree \(1\). Thus \(K^\vee=\mathcal O[-1]\), \(\eta(1)=e\otimes e^*\), and \(\epsilon(e^*\otimes e)=1\). The first zigzag sends \(e\) to \(e\otimes e^*\otimes e\) and back to \(e\); the second does the analogous contraction for \(e^*\). No factor swap occurs. The bidual map is \(e\mapsto-e^{**}\) by (4.5). Multiplying coevaluation instead by \(-1\) while keeping this evaluation would make both zigzags negative identities; that is not the correct dual data.

**Exercise 2 (medium: one approximation suffices).** Suppose \(F\) is a module sheaf of Tor amplitude \([0,0]\). What is the weakest threshold in Theorem 3.2 that proves perfectness? Characterize such \(F\) directly.

**Solution.** The threshold is \(-1\), which is finite presentation by Proposition 2.2. Amplitude \([0,0]\) means \(\operatorname{Tor}_1(F,T)=0\) for every module \(T\), and therefore flatness. Conversely a flat module in degree zero has that amplitude, since tensor is exact. Lemma 1.2 now says that precisely the flat finitely presented sheaves are locally finite projective, hence perfect in degree zero. The threshold records finite relations as well as finite generators; finite type alone does not supply the finite presentation used in the splitting proof.

**Exercise 3 (medium: the coefficient sign).** Let \(P\) have one finite free term in degree \(s\). For a homogeneous map \(\phi:P\to L\) of degree \(h\) and an element \(m\in M^t\), calculate (4.3). Explain why it remains an isomorphism for a bounded finite projective complex.

**Solution.** Evaluation must first move \(m\) past \(p\in P^s\), giving \((-1)^{ts}\phi(p)\otimes m\). In the model \(\mathsf H(P,L)=L\otimes P^\vee\), the dual term has degree \(-s\); swapping it with \(m\) gives the same sign \((-1)^{-st}=(-1)^{st}\). This is a tensor symmetry isomorphism. Finite free powers give componentwise copies, finite projective summands inherit an inverse, and bounded complexes are finite extensions of their terms. Applying the compatible triangle maps and long exact sequences proves the general result. K-flat models for \(L,M\) compute the derived tensors, so their possible unboundedness causes no additional finite-sum restriction.

**Exercise 4 (hard: finite cells rather than finite generators).** In the converse proof of Theorem 4.2, why is closing the chosen generators under their differentials a finite process, and why does stage zero need special treatment? Would merely taking the subcomplex generated by the tensor entries and their differentials be sufficient?

**Solution.** Each chosen germ has finite support in a finite stage. A cell from a positive stage has differential in strictly earlier stages, so following its dependencies decreases a nonnegative integer. Every branch has finite length and every vertex finitely many descendants, giving a finite set. A stage-zero disk has two generators and its lower generator's differential is its upper mate in the same stage; including the mate completes that branch, since its differential is zero. Finite intersection of their defining opens makes the remaining cells free on one neighbourhood. Contributions with zero germ are killed by finitely many shrinkings. The span of this selected subset of graded free cells is a bounded finite free complex and a graded summand. In contrast, finitely many arbitrary sections may generate a nonprojective submodule: the ideal \(\epsilon R\subset R\) over the dual numbers is generated by one element but is isomorphic to the nonflat residue \(k\). Such a subcomplex would not supply a perfect object for the retract argument. Selecting actual cells repairs exactly this problem.

**Exercise 5 (hard: global duality with no uniform bound).** On the discrete space from Section 3, construct the dual of \(K|_{\{n\}}=k[n]\) explicitly and check that the global coevaluation is defined although it has infinitely many degree components across the space.

**Solution.** Take \(N|_{\{n\}}=k[-n]\). At point \(n\), send one to the tensor of its degree-\(-n\) generator and the degree-\(n\) dual generator, and evaluate that pair to one. Sheaves on a discrete space are specified independently at the points; these formulas define sheaf maps. The tensor totalization uses sheaf direct sums, whose sections are locally finite families, not necessarily globally finite families. The singleton neighbourhoods make this family locally finite, so coevaluation is a legitimate section of the tensor sheaf. Both zigzags are identities on every singleton and hence are identities of these actual sheaf maps. This example is perfect and dualizable but has no global finite cohomological bound. It shows why neither definition may silently impose a uniform interval.

# Double covers and odd maps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A map between spheres is *odd* if it commutes with the antipodal maps. This lesson proves the two facts about odd maps that the Borsuk counterexample needs: an odd map from a sphere to itself has degree one modulo two, so there is no odd map from a sphere to a sphere of smaller dimension (the Borsuk–Ulam theorem); and a map from a product \(L\times\mathbb{RP}^{h-1}\) that is induced by a map odd in the sphere variable has degree zero modulo two when \(\dim L\ge1\) (Proposition 5.1). Both follow from one exact sequence with coefficients \(\mathbb F_2\): the *transfer sequence* of a double cover (Section 2). For a textbook account of the transfer and of the Borsuk–Ulam theorem see [Hat, Section 2.B].

Notation and tools are those of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md); homology has coefficients in \(\mathbb F_2\). From the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) we use covering spaces from Roberts's notes (Proposition 8: pullbacks of covering spaces are covering spaces, and Corollary 7: a covering space of a contractible space is trivial), and from Fomberg's notes the long exact sequence of a short exact sequence of chain complexes (Theorem 1.21), the homology of spheres (Corollary 1.17) and homotopy invariance; these hold with coefficients by Section 1 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes). From [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90) we use that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

## 1. Double covers

**Definition 1.1.** A **free involution** on a Hausdorff space \(E\) is a continuous map \(T:E\to E\) with \(T\circ T=\mathrm{id}\) such that every point has an open neighbourhood \(U\) with \(U\cap T(U)=\varnothing\). The quotient \(B=E/T\), with quotient map \(p:E\to B\), is the associated **double cover**. A **map of double covers** \((E,T)\to(E',T')\) is a continuous \(\tilde\varphi:E\to E'\) with \(\tilde\varphi\circ T=T'\circ\tilde\varphi\); it induces a continuous \(\varphi:B\to B'\) with \(p'\circ\tilde\varphi=\varphi\circ p\).

For \(U\) as in the definition, \(p^{-1}(p(U))=U\cup T(U)\) is open, so \(p(U)\) is open, and \(p\) maps \(U\) bijectively, continuously and openly onto \(p(U)\). Hence \(p\) is a covering map with two-point fibres \(\{e,T(e)\}\).

**Example 1.2.** (a) The antipodal map \(u\mapsto-u\) on the unit sphere \(S^n\subset\mathbb R^{n+1}\) is a free involution (take \(U\) an open hemisphere). The map \(u\mapsto uu^{\mathsf T}\) induces a continuous bijection from \(S^n/\pm\) onto the compact Hausdorff space \(\mathbb{RP}^n\) of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md), hence a homeomorphism; so \(p:S^n\to\mathbb{RP}^n\), \(u\mapsto[u]\), is a double cover. For \(n\ge1\), \(\mathbb{RP}^n\) is a connected closed \(n\)-manifold.

(b) If \(L\) is a space and \((E,T)\) a free involution, then \(\mathrm{id}_L\times T\) is a free involution on \(L\times E\) with quotient \(L\times B\). The projection \(L\times E\to E\) is a map of double covers.

(c) A map \(\Psi:L\times S^{h-1}\to S^{a-1}\) with \(\Psi(x,-z)=-\Psi(x,z)\) is a map of double covers from (b) to (a), and induces \(\bar\Psi:L\times\mathbb{RP}^{h-1}\to\mathbb{RP}^{a-1}\). An odd map \(\varphi:S^n\to S^d\) induces \(\bar\varphi:\mathbb{RP}^n\to\mathbb{RP}^d\).

**Lemma 1.3** (Lifting simplices). Let \(p:E\to B\) be a double cover with involution \(T\). Every continuous map \(\sigma:\Delta^i\to B\) from a simplex has exactly two lifts \(\tilde\sigma:\Delta^i\to E\), \(p\circ\tilde\sigma=\sigma\), and they are \(\tilde\sigma\) and \(T\circ\tilde\sigma\).

*Proof.* Lifts of \(\sigma\) are the same as continuous sections of the pullback covering \(\sigma^*E=\{(t,e):\sigma(t)=p(e)\}\to\Delta^i\), which is a covering space with two-point fibres (Roberts, Proposition 8). The simplex is contractible, so this covering is isomorphic to \(\Delta^i\times\{1,2\}\to\Delta^i\) (Roberts, Corollary 7). A continuous section of the latter has constant second coordinate because \(\Delta^i\) is connected, so there are exactly two sections. If \(\tilde\sigma\) is a lift, so is \(T\circ\tilde\sigma\), and the two differ at every point because \(T\) has no fixed points. \(\square\)

## 2. The transfer sequence

For a double cover \(p:E\to B\) and a singular simplex \(\sigma\) of \(B\), put \(\tau(\sigma)=\tilde\sigma+T\circ\tilde\sigma\in C_i(E;\mathbb F_2)\), the sum of the two lifts, and extend linearly. A face of a lift is a lift of the corresponding face, so \(\tau\) is a chain map, the **transfer**.

**Lemma 2.1.** The sequence of chain complexes
\[
0\longrightarrow C_\bullet(B;\mathbb F_2)\xrightarrow{\ \tau\ }C_\bullet(E;\mathbb F_2)\xrightarrow{\ p_\#\ }C_\bullet(B;\mathbb F_2)\longrightarrow0
\]
is exact. Moreover \(\tau\circ p_\#=\mathrm{id}+T_\#\) on \(C_\bullet(E;\mathbb F_2)\).

*Proof.* A simplex \(\rho\) of \(E\) is a lift of \(p\circ\rho\), so by Lemma 1.3 the simplices of \(E\) are partitioned into the pairs \(\{\tilde\sigma,T\tilde\sigma\}\) of lifts of the simplices \(\sigma\) of \(B\). Hence \(\tau\) is injective. Every simplex of \(B\) has a lift, so \(p_\#\) is surjective, and \(p_\#\tau(\sigma)=2\sigma=0\). If a chain \(c=\sum_\rho a_\rho\rho\) has \(p_\#c=0\), then for each \(\sigma\) the coefficient \(a_{\tilde\sigma}+a_{T\tilde\sigma}\) of \(\sigma\) in \(p_\#c\) vanishes, so \(a_{\tilde\sigma}=a_{T\tilde\sigma}\) and \(c=\tau\bigl(\sum_\sigma a_{\tilde\sigma}\sigma\bigr)\). Finally \(\tau(p_\#\rho)=\rho+T\rho\). \(\square\)

**Proposition 2.2.** A double cover has a long exact sequence
\[
\cdots\to H_i(B)\xrightarrow{\tau_*}H_i(E)\xrightarrow{p_*}H_i(B)\xrightarrow{\partial}H_{i-1}(B)\xrightarrow{\tau_*}H_{i-1}(E)\to\cdots\to H_0(E)\xrightarrow{p_*}H_0(B)\to0,
\]
with \(\tau_*p_*=\mathrm{id}+T_*\) on \(H_\bullet(E)\). A map of double covers \(\tilde\varphi\), inducing \(\varphi\), gives a commutative ladder: \(\tilde\varphi_*\tau_*=\tau'_*\varphi_*\), \(p'_*\tilde\varphi_*=\varphi_*p_*\) and \(\partial'\varphi_*=\varphi_*\partial\).

*Proof.* The long exact sequence of the short exact sequence of Lemma 2.1 (Fomberg, Theorem 1.21). If \(\tilde\sigma\) lifts \(\sigma\), then \(\tilde\varphi\circ\tilde\sigma\) lifts \(\varphi\circ\sigma\), and \(\tilde\varphi\circ T\tilde\sigma=T'(\tilde\varphi\circ\tilde\sigma)\) is the other lift; so \(\tilde\varphi_\#\tau=\tau'\varphi_\#\), and \(p'_\#\tilde\varphi_\#=\varphi_\#p_\#\). A map of short exact sequences of chain complexes induces a map of their long exact sequences, including the connecting maps. \(\square\)

## 3. Homology of projective spaces

**Proposition 3.1.** Let \(n\ge1\) and \(p:S^n\to\mathbb{RP}^n\) the double cover of Example 1.2(a). Then:

(a) \(\partial:H_i(\mathbb{RP}^n)\to H_{i-1}(\mathbb{RP}^n)\) is an isomorphism for \(1\le i\le n\);

(b) \(H_i(\mathbb{RP}^n)\cong\mathbb F_2\) for \(0\le i\le n\), generated in degree \(n\) by the fundamental class \([\mathbb{RP}^n]\), and \(H_i(\mathbb{RP}^n)=0\) for \(i>n\);

(c) \(\tau_*:H_n(\mathbb{RP}^n)\to H_n(S^n)\) is an isomorphism, and \(p_*:H_n(S^n)\to H_n(\mathbb{RP}^n)\) is zero.

*Proof.* We use: \(H_i(S^n)\) is \(\mathbb F_2\) for \(i=0,n\) and zero otherwise (Fomberg, Corollary 1.17); \(H_0\) of a path-connected space is \(\mathbb F_2\), generated by the class of a point; and \(H_i(\mathbb{RP}^n)=0\) for \(i>n\), while \(H_n(\mathbb{RP}^n)=\{0,[\mathbb{RP}^n]\}\) (Corollary 5.1 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes)).

*Degree zero.* \(p_*:H_0(S^n)\to H_0(\mathbb{RP}^n)\) maps the class of a point to the class of a point, so it is an isomorphism; by exactness \(\tau_*=0\) on \(H_0(\mathbb{RP}^n)\).

*Degree \(n\).* Since \(H_{n+1}(\mathbb{RP}^n)=0\), exactness at \(H_n(\mathbb{RP}^n)\xrightarrow{\tau_*}H_n(S^n)\) shows that \(\tau_*\) is injective there. The antipodal map \(T\) is a homeomorphism, so \(T_*\) is an automorphism of \(H_n(S^n)\cong\mathbb F_2\), the identity. Hence \(\tau_*p_*=\mathrm{id}+T_*=0\) on \(H_n(S^n)\), and injectivity of \(\tau_*\) gives \(p_*=0\).

*Part (a).* Let \(1\le i\le n\). The kernel of \(\partial\) on \(H_i(\mathbb{RP}^n)\) is the image of \(p_*:H_i(S^n)\to H_i(\mathbb{RP}^n)\), which is zero: for \(i<n\) because \(H_i(S^n)=0\), for \(i=n\) by the previous step. The image of \(\partial\) is the kernel of \(\tau_*:H_{i-1}(\mathbb{RP}^n)\to H_{i-1}(S^n)\), which is everything: for \(i=1\) because \(\tau_*=0\) on \(H_0\), for \(1<i\le n\) because \(H_{i-1}(S^n)=0\).

*Parts (b) and (c).* By (a), \(H_n(\mathbb{RP}^n)\cong\cdots\cong H_0(\mathbb{RP}^n)\cong\mathbb F_2\), so \([\mathbb{RP}^n]\ne0\) generates \(H_n\). The injective map \(\tau_*\) from \(H_n(\mathbb{RP}^n)\cong\mathbb F_2\) to \(H_n(S^n)\cong\mathbb F_2\) is an isomorphism. \(\square\)

## 4. Odd maps

**Theorem 4.1.** Let \(n\ge1\). Every odd continuous map \(\varphi:S^n\to S^n\) has \(\deg_2\varphi=1\); in particular it is surjective.

*Proof.* The map \(\varphi\) is a map of double covers, inducing \(\bar\varphi:\mathbb{RP}^n\to\mathbb{RP}^n\). On \(H_0(\mathbb{RP}^n)\), \(\bar\varphi_*\) maps the class of a point to the class of a point, so it is the identity. Since \(\bar\varphi_*\partial=\partial\bar\varphi_*\) and \(\partial\) is an isomorphism in degrees \(1,\dots,n\) (Proposition 3.1(a)), induction on \(i\) shows that \(\bar\varphi_*\) is an isomorphism on \(H_i(\mathbb{RP}^n)\) for \(0\le i\le n\). Then \(\varphi_*\tau_*=\tau_*\bar\varphi_*\) on \(H_n(\mathbb{RP}^n)\), with \(\tau_*\) an isomorphism onto \(H_n(S^n)\) (Proposition 3.1(c)), so \(\varphi_*\) is an isomorphism of \(H_n(S^n)\cong\mathbb F_2\), and \(\varphi_*[S^n]=[S^n]\). Surjectivity follows from Corollary 4.3 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md). \(\square\)

**Corollary 4.2** (Borsuk–Ulam). If \(0\le d<n\), there is no odd continuous map \(S^n\to S^d\).

*Proof.* If \(d=0\), a continuous map from the connected space \(S^n\) to the two-point space \(S^0\) is constant, hence not odd. If \(d\ge1\), compose an odd map \(S^n\to S^d\) with the inclusion of \(S^d\) as the unit sphere of the first \(d+1\) coordinates of \(\mathbb R^{n+1}\). The composite is an odd map \(S^n\to S^n\) that is not surjective, contradicting Theorem 4.1. \(\square\)

**Corollary 4.3.** For every continuous \(g:S^n\to\mathbb R^n\) there is \(u\) with \(g(u)=g(-u)\).

*Proof.* Otherwise \(u\mapsto(g(u)-g(-u))/|g(u)-g(-u)|\) is an odd map \(S^n\to S^{n-1}\). \(\square\)

At a point \(y\) near whose preimages an odd map \(\varphi:S^n\to S^n\) is smooth with invertible derivative, Theorem 4.1 and the local counting lemma (Lemma 4.2 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)) give: \(|\varphi^{-1}(y)|\) is odd.

## 5. Degree zero over a product

**Proposition 5.1.** Let \(L\) be a closed smooth manifold of dimension \(l\ge1\), let \(h\ge1\) and \(a=l+h\), and let \(\Psi:L\times S^{h-1}\to S^{a-1}\) be continuous with \(\Psi(x,-z)=-\Psi(x,z)\). Then the induced map
\[
\bar\Psi:L\times\mathbb{RP}^{h-1}\longrightarrow\mathbb{RP}^{a-1},
\]
a map between closed manifolds of dimension \(a-1\), has \(\deg_2\bar\Psi=0\).

*Proof.* Put \(B=L\times\mathbb{RP}^{h-1}\), the quotient of \(M=L\times S^{h-1}\) by \(T(x,z)=(x,-z)\); it is a closed manifold of dimension \(l+h-1=a-1\ge1\), and \(\mathbb{RP}^{a-1}\) is connected. Let \(\varepsilon:H_0(X)\to\mathbb F_2\) be the map induced by \(X\to\{\mathrm{pt}\}\); it is natural, and it sends the class of a point to \(1\). Write \(\partial^{a-1}\) for the composite of \(a-1\) connecting maps of the transfer sequence, from degree \(a-1\) to degree \(0\).

By definition \(\bar\Psi_*[B]=\deg_2(\bar\Psi)\,[\mathbb{RP}^{a-1}]\). By Proposition 3.1, \(\partial^{a-1}[\mathbb{RP}^{a-1}]\) generates \(H_0(\mathbb{RP}^{a-1})\), so \(\varepsilon\partial^{a-1}[\mathbb{RP}^{a-1}]=1\). Since \(\Psi\) is a map of double covers (Example 1.2(c)), Proposition 2.2 gives
\[
\deg_2\bar\Psi=\varepsilon\bigl(\partial^{a-1}\bar\Psi_*[B]\bigr)=\varepsilon\bigl(\bar\Psi_*\partial_M^{a-1}[B]\bigr)=\varepsilon\bigl(\partial_M^{a-1}[B]\bigr),
\]
where \(\partial_M\) is the connecting map of the cover \(M\to B\). The projection \(\mathrm{pr}_2:M\to S^{h-1}\) is a map of double covers inducing \(\mathrm{pr}_2:B\to\mathbb{RP}^{h-1}\) (Example 1.2(b)), so
\[
\varepsilon\bigl(\partial_M^{a-1}[B]\bigr)=\varepsilon\bigl((\mathrm{pr}_2)_*\partial_M^{a-1}[B]\bigr)=\varepsilon\bigl(\partial^{a-1}(\mathrm{pr}_2)_*[B]\bigr).
\]
Here \((\mathrm{pr}_2)_*[B]\) lies in \(H_{a-1}(\mathbb{RP}^{h-1})\), which is zero because \(a-1>h-1\) (Proposition 3.1(b); for \(h=1\), \(\mathbb{RP}^0\) is a point). Hence \(\deg_2\bar\Psi=0\). \(\square\)

The proposition is false for \(l=0\): if \(L\) is a point, \(\bar\Psi\) is induced by an odd self-map of \(S^{h-1}\) and has degree one by Theorem 4.1. The homological reason is that the classes pulled back from \(\mathbb{RP}^{h-1}\) die above degree \(h-1\), while those of \(\mathbb{RP}^{a-1}\) survive up to degree \(a-1\). With cohomology rings this is the statement that the first Stiefel–Whitney class \(w\) of the target cover pulls back to a class whose \((a-1)\)-st power vanishes [Hat, Theorem 3.19].

## 6. Exercises

**6.1.** Show that \(z\mapsto z^2\) on the unit circle of \(\mathbb C\) induces a homeomorphism \(\mathbb{RP}^1\cong S^1\), and verify Proposition 3.1 for \(n=1\) from the homology of the circle.

**6.2.** Let \(A_1,\dots,A_d\) be closed sets covering the unit sphere \(S^{d-1}\subset\mathbb R^d\). Use Corollary 4.3 with \(g(u)=(\operatorname{dist}(u,A_1),\dots,\operatorname{dist}(u,A_{d-1}))\) to show that some \(A_i\) contains a pair of antipodal points. Deduce that \(S^{d-1}\) cannot be covered by \(d\) sets of diameter less than \(2\).

**6.3.** Let \(\varphi:S^n\to S^n\) be continuous with \(\varphi(-u)=\varphi(u)\) for all \(u\). Show that \(\deg_2\varphi=0\).

**6.4.** In Proposition 5.1 take \(L=S^1\) and \(h=1\), so that \(M=S^1\times\{\pm1\}\), \(B=S^1\) and \(a=2\). Give an example of \(\Psi\) and check directly that \(\bar\Psi:S^1\to\mathbb{RP}^1\) has even degree.

## 7. Solutions

**6.1.** \(z^2=w^2\) iff \(w=\pm z\), so \(z\mapsto z^2\) induces a continuous bijection \(S^1/\pm\to S^1\), a homeomorphism by compactness, and \(p\) becomes \(z\mapsto z^2\). With \(H_0=H_1=\mathbb F_2\) for both spaces, \(p_*\) on \(H_1\) is multiplication by the degree \(2\), that is zero; \(\tau_*\) on \(H_1\) is injective because \(H_2(\mathbb{RP}^1)=0\); \(\partial:H_1\to H_0\) is onto because \(\tau_*=0\) on \(H_0\).

**6.2.** Corollary 4.3 (with \(n=d-1\)) gives \(u\) with \(g(u)=g(-u)\). If \(u\in A_i\) for some \(i\le d-1\), then \(\operatorname{dist}(-u,A_i)=0\) and \(-u\in A_i\) because \(A_i\) is closed. Otherwise all coordinates of \(g(u)=g(-u)\) are positive, so neither \(u\) nor \(-u\) lies in \(A_1,\dots,A_{d-1}\), and both lie in \(A_d\). For the second claim, the closures of sets of diameter less than \(2\) have the same diameters and contain no antipodal pair.

**6.3.** \(\varphi\) factors as \(\bar\varphi\circ p\) with \(\bar\varphi:\mathbb{RP}^n\to S^n\). Then \(\varphi_*=\bar\varphi_*p_*\), and \(p_*=0\) on \(H_n(S^n)\) by Proposition 3.1(c).

**6.4.** For example \(\Psi(x,\pm1)=\pm x\), with \(x\in S^1\subset\mathbb R^2\). Then \(\bar\Psi(x)=[x]\), which is the double cover \(S^1\to\mathbb{RP}^1\cong S^1\), \(x\mapsto x^2\) in the coordinates of 6.1, of degree \(2\), so \(\deg_2\bar\Psi=0\) as the proposition predicts.

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
- [Hat] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002 (author's page). https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
- D. M. Roberts, *Algebraic Topology*, lecture notes, 2019 (core course Algebraic Topology). https://github.com/DavidMichaelRoberts/AlgebraicTopology2019

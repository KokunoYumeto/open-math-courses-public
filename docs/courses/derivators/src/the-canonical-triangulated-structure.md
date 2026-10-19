# The canonical triangulated structure

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A triangulated category is a category with extra structure: a shift functor and a chosen class of distinguished triangles. The first lesson of this course showed why that structure cannot be recovered from functorial cones on the category itself. A strong stable derivator supplies it from properties alone. Each object \(f\) of \(\mathbb D([1])\), an arrow kept together with its coherence, has a cofibre diagram, built by an extension by zero and a homotopy left Kan extension. Reading the diagram along a path gives a triangle. This lesson proves that these triangles satisfy the axioms of a triangulated category. The rotation axiom carries a sign: the flip of a suspension, shown to be \(-1\) in the preceding lesson, appears when a cofibre diagram is read along its other axis.

**Prerequisites.** The lessons [*Homotopy exact squares*](homotopy-exact-squares.md) (Lemma 2.2, Lemma 3.1, Proposition 3.3), [*The derivator of a ring*](the-derivator-of-a-ring.md) (Theorem 4.1, which defines strong derivators), [*Pointed and stable derivators*](pointed-and-stable-derivators.md) (Propositions 1.3 and 4.2, Definition 3.1), [*Recognizing cocartesian squares*](recognizing-cocartesian-squares.md) (Lemma 1.1, Corollary 2.2, Proposition 2.3, Corollary 3.3, Proposition 4.1, Exercises 5.2 and 5.5) and [*Stable derivators are additive*](stable-derivators-are-additive.md) (Construction 3.1, Lemma 3.2, Theorem 4.1, Corollary 4.2). The axioms of a triangulated category are those of Section 3 of [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization).

Throughout, \(\mathbb D\) is a strong stable derivator. By Corollary 4.2 of the preceding lesson, every \(\mathbb D(J)\) is additive and \(\Sigma\) is an additive equivalence with quasi-inverse \(\Omega\). For a morphism \(\varphi\) of \(\mathbb D(J)\) and an object \(j\) we write \(\varphi_j\) for its component.

## 1. Cofibre diagrams and their triangles

In \([2]\times[1]\) let \(K\) be the full subcategory on \((0,0),(1,0),(2,0),(0,1)\), let \(k_0:[1]\to K\) send \(0\to1\) to \((0,0)\to(1,0)\), a sieve, and let \(k_1:K\to[2]\times[1]\) be the inclusion. The squares \(s_{01}\), \(s_{12}\), \(s_{02}\) are those of Section 2 of the lesson on recognizing cocartesian squares.

**Definition 1.1.** A *cofibre diagram* is an object \(Y\) of \(\mathbb D([2]\times[1])\) such that \(Y_{20}\) and \(Y_{01}\) are zero objects and \(s_{01}^*Y\) and \(s_{12}^*Y\) are cocartesian.

**Lemma 1.2.** For \(f\) in \(\mathbb D([1])\), the object \(Y_f=k_{1!}k_{0*}f\) is a cofibre diagram whose restriction to \((0,0)\to(1,0)\) is isomorphic to \(f\). Conversely, every cofibre diagram \(Y\) is isomorphic to \(Y_f\), where \(f\) is its restriction to \((0,0)\to(1,0)\); the isomorphism is natural in \(Y\).

**Proof.** The first statement is Proposition 4.1 of the lesson on recognizing cocartesian squares. Let \(Y\) be a cofibre diagram. The restriction \(k_1^*Y\) vanishes at the objects of \(K\) outside the sieve \(k_0\), so its unit \(k_1^*Y\to k_{0*}k_0^*k_1^*Y\) is invertible (Proposition 3.3 of the lesson on homotopy exact squares). For the counit of \(k_1\), factor \(k_1=e_1e_0\) through the full subcategory \(J_1\) that adds \((1,1)\), and use the composite adjunction, whose counit at \(Y\) is \(\varepsilon^{e_1}_Y\circ e_{1!}\varepsilon^{e_0}_{e_1^*Y}\). The proof of Proposition 2.3 of that lesson shows that \(\varepsilon^{e_0}_{e_1^*Y}\) is invertible because \(s_{01}^*Y\) is cocartesian, and that \(\varepsilon^{e_1}_Y\) is invertible at \((2,1)\), hence everywhere, because \(s_{12}^*Y\) is cocartesian. So \(Y\cong k_{1!}k_1^*Y\cong k_{1!}k_{0*}f\), through units and counits. \(\square\)

Let \(W\) be a cocartesian square with \(W_{10}\) and \(W_{01}\) zero objects. Then \(i_\ulcorner^*W\) is the extension by zero of \(W_{00}\) along the sieve \((0,0)\), and \(W\cong i_{\ulcorner!}(0,0)_*W_{00}\). Write

\[
\iota_W:\Sigma W_{00}\longrightarrow W_{11}
\]

for the resulting isomorphism (Definition 3.1 of the lesson on pointed derivators). Since \(i_{\ulcorner!}(0,0)_*\) is fully faithful, a morphism \(W\to W'\) between two such squares is determined by its component at \((0,0)\), and its component at \((1,1)\) is \(\iota_{W'}\,\Sigma(\varphi_{00})\,\iota_W^{-1}\). We call this the *naturality of* \(\iota\).

For a cofibre diagram \(Y\), the composite square \(s_{02}^*Y\) is cocartesian (Proposition 2.3 of the lesson on recognizing cocartesian squares) with \(Y_{20}\cong0\cong Y_{01}\), so \(\iota_Y=\iota_{s_{02}^*Y}:\Sigma Y_{00}\to Y_{21}\) is defined.

**Definition 1.3.** The *triangle of a cofibre diagram* \(Y\) is

\[
Y_{00}\xrightarrow{u}Y_{10}\xrightarrow{v}Y_{11}\xrightarrow{w}\Sigma Y_{00},
\]

where \(u\) and \(v\) are maps of the underlying diagram and \(w\) is \(\iota_Y^{-1}\) composed with the map \(Y_{11}\to Y_{21}\). For \(f\) in \(\mathbb D([1])\), the triangle \(T_f\) is the triangle of \(Y_f\). A triangle of \(\mathbb D(e)\) is *distinguished* if it is isomorphic to \(T_f\) for some \(f\).

By Lemma 1.2 the triangle of every cofibre diagram is distinguished. A morphism \(\varphi:f\to f'\) of \(\mathbb D([1])\) induces \(Y_\varphi:Y_f\to Y_{f'}\), and by naturality of \(\iota\) the components of \(Y_\varphi\) at \((0,0)\), \((1,0)\), \((1,1)\), together with \(\Sigma\varphi_0\), form a morphism of triangles \(T_f\to T_{f'}\).

**Lemma 1.4.** Let \(X\) in \(\mathbb D(\square)\) be cocartesian with \(X_{00}\to X_{10}\) invertible. Then \(X_{01}\to X_{11}\) is invertible.

**Proof.** Let \(Z=i_\ulcorner^*X\), let \(\pi_2:{\square}\to[1]\), \((a,b)\mapsto b\), and let \(s:[1]\to\ulcorner\) send \(0\to1\) to \((0,0)\to(0,1)\). The square \(X'=\pi_2^*s^*Z\) has identity horizontal arrows, so it is cocartesian by Exercises 5.5 and 5.2 of the lesson on recognizing cocartesian squares. The morphisms \((0,0)\to(0,0)\), \((0,0)\to(1,0)\), \((0,1)\to(0,1)\) form a transformation \(s\pi_2i_\ulcorner\to1_\ulcorner\), which induces \(i_\ulcorner^*X'\to Z\) with components \(1\), \(X_{00}\to X_{10}\), \(1\); it is invertible by (Der2). Two cocartesian squares with isomorphic restrictions to \(\ulcorner\) are isomorphic, through \(i_{\ulcorner!}\) of that isomorphism, so \(X\cong X'\) in \(\mathbb D(\square)\) by an isomorphism that is the identity at \((0,1)\). The bottom arrow of \(X'\) is an identity, so that of \(X\) is invertible. \(\square\)

## 2. The flip of a suspension square

Let \(\sigma:{\square}\to\square\) be the transposition \((a,b)\mapsto(b,a)\). It fixes \((0,0)\) and \((1,1)\) and restricts to the exchange \(\sigma_\ulcorner\) of the two legs of \(\ulcorner\). In the notation of Section 3 of the preceding lesson, \(\ulcorner=V_1\) and \(\sigma_\ulcorner=V_{(1,0)}\), so the flip of \(\Sigma W_{00}\) is \(\tau=(1,0)_*\).

**Lemma 2.1.** Let \(W\) be a cocartesian square with \(W_{10}\cong0\cong W_{01}\). Then \(\sigma^*W\) is such a square, with the same values at \((0,0)\) and \((1,1)\), and

\[
\iota_{\sigma^*W}=\iota_W\circ\tau .
\]

**Proof.** \(\sigma^*W\) is cocartesian by Exercise 5.2 of the lesson on recognizing cocartesian squares. The isomorphism \(\iota_W\) is the composite

\[
\begin{aligned}
\Sigma W_{00}&=\operatorname{hocolim}_\ulcorner(0,0)_*W_{00}\\
&\xrightarrow{\operatorname{hocolim}(e_W)}\operatorname{hocolim}_\ulcorner i_\ulcorner^*W\\
&\xrightarrow{\chi_W}W_{11},
\end{aligned}
\]

where \(e_W:(0,0)_*W_{00}\to i_\ulcorner^*W\) is the isomorphism of extension by zero and \(\chi\) is the comparison map of Section 1 of that lesson. Pasting the square of \(\chi\) with the square with top and bottom \(\sigma\), sides \(1_\square\), and identity transformation, and pasting the square with top \(\sigma_\ulcorner\), sides \(p\), bottom \(1_e\), with the square of \(\chi\), gives the same square, because \(\sigma i_\ulcorner=i_\ulcorner\sigma_\ulcorner\) and \(\sigma\) fixes \((1,1)\). Horizontal pasting yields

\[
\chi_{\sigma^*W}=\chi_W\circ\kappa_{\sigma_\ulcorner}(i_\ulcorner^*W),
\]

with \(\kappa\) the comparison map of homotopy colimits of the preceding lesson. Next, \(e_{\sigma^*W}\) and \(\sigma_\ulcorner^*(e_W)\circ(\beta^{(1,0)})^{-1}\) are two morphisms from \((0,0)_*W_{00}\) to \(\sigma_\ulcorner^*i_\ulcorner^*W\), a square vanishing at the legs, with the same component at \((0,0)\); morphisms into an extension by zero are determined by that component, so they are equal. Using naturality of \(\kappa_{\sigma_\ulcorner}\),

\[
\begin{aligned}
\iota_{\sigma^*W}
&=\chi_W\circ\operatorname{hocolim}(e_W)\circ\kappa_{\sigma_\ulcorner}\\
&\qquad\circ\operatorname{hocolim}(\beta^{(1,0)})^{-1}\\
&=\iota_W\circ\tau,
\end{aligned}
\]

by the definition of \(\tau=(1,0)_*\) in Construction 3.1 of the preceding lesson. \(\square\)

By Theorem 4.1 of the preceding lesson, \(\tau=-1\), so \(\iota_{\sigma^*W}=-\iota_W\): reading a suspension square along the other axis changes the sign of its identification with \(\Sigma W_{00}\).

## 3. The axioms

**Theorem 3.1.** \(\mathbb D(e)\), with the suspension \(\Sigma\) and the distinguished triangles of Definition 1.3, is a triangulated category. So is \(\mathbb D(J)\) for every small category \(J\).

The proof occupies the rest of this section. The statement for \(\mathbb D(J)\) follows from that for \(\mathbb D(e)\) applied to the shifted derivator \(\mathbb D^J\), which is strong and stable (Corollary 3.3 of the lesson on recognizing cocartesian squares).

**Identity and completion.** Let \(x\) be an object and \(f=p^*x\) in \(\mathbb D([1])\), with \(p:[1]\to e\); its underlying arrow is \(1_x\). In the cocartesian square \(s_{01}^*Y_f\) the top arrow is \(1_x\), so by Lemma 1.4 the bottom arrow \(0\cong Y_{01}\to Y_{11}\) is invertible and \(Y_{11}\cong0\). Hence \(T_f\) is isomorphic to \(x\xrightarrow1x\to0\to\Sigma x\), which is therefore distinguished. Every morphism \(u:x\to y\) is isomorphic, as an arrow, to the underlying arrow of some \(f\) in \(\mathbb D([1])\), because \(\operatorname{dia}_{[1]}\) is essentially surjective; transporting \(T_f\) along that isomorphism gives a distinguished triangle beginning with \(u\). Distinguished triangles are closed under isomorphism by definition.

**Extension of squares.** Let \(T\) and \(T'\) be distinguished, and \((a,b)\) a commutative square from the first map of \(T\) to that of \(T'\). Replacing them by isomorphic triangles, we may assume \(T=T_f\) and \(T'=T_{f'}\). Since \(\operatorname{dia}_{[1]}\) is full, there is \(\varphi:f\to f'\) with \(\varphi_0=a\) and \(\varphi_1=b\), and the morphism of triangles induced by \(\varphi\) extends \((a,b)\).

**Proposition 3.2 (rotation).** If \(x\xrightarrow{u}y\xrightarrow{v}z\xrightarrow{w}\Sigma x\) is distinguished, so is

\[
y\xrightarrow{v}z\xrightarrow{w}\Sigma x\xrightarrow{-\Sigma u}\Sigma y .
\]

**Proof.** We may assume the triangle is \(T_f\). Let \(L\subset[2]\times[2]\) be the full subcategory without \((0,2)\), \(M\subset L\) the full subcategory on \((0,0),(1,0),(2,0),(0,1),(1,2)\), \(m_0:[1]\to M\) the arrow \((0,0)\to(1,0)\), a sieve, and \(m_1:M\to L\) the inclusion. Put \(Q=m_{1!}m_{0*}f\). Then \(Q\) vanishes at \((2,0)\), \((0,1)\), \((1,2)\), and \(L\) has three unit squares,

\[
\begin{gathered}
A=\{(0,0),(1,0),(0,1),(1,1)\},\\
B=\{(1,0),(2,0),(1,1),(2,1)\},
\end{gathered}
\]
\[
C=\{(1,1),(2,1),(1,2),(2,2)\},
\]

all cocartesian by Corollary 2.2 of the lesson on recognizing cocartesian squares, adding \((1,1)\), \((2,1)\), \((2,2)\) in turn. For \(A\) the functor \(r\) is an isomorphism; for \(B\) it is the inclusion of \(\{(1,0),(2,0),(1,1)\}\) into the objects below \((2,1)\), as in Proposition 2.3 there; for \(C\) it is the inclusion of \(\{(1,1),(2,1),(1,2)\}\) into all seven other objects, with the left adjoint sending \((2,0)\) and \((2,1)\) to \((1,0)\), \((1,2)\) to \((0,1)\), and everything else to \((0,0)\).

Restricted to the rows \(0\) and \(1\), \(Q\) is a cofibre diagram with restriction \(f\), so its triangle is \(T_f\) (Lemma 1.2): \(Q_{11}\) is \(z\), and \(w=\iota_E^{-1}\circ(Q_{11}\to Q_{21})\) for the composite square \(E\) on \((0,0),(2,0),(0,1),(2,1)\).

Next, read \(Q\) along the other axis: let \(\psi:[2]\times[1]\to L\), \(\psi(c,t)=(1+t,c)\). Then \(\psi^*Q\) has values \(y\), \(z\), \(Q_{12}\cong0\) in its top row and \(Q_{20}\cong0\), \(Q_{21}\), \(Q_{22}\) in its bottom row; its two unit squares are the transposes of \(B\) and \(C\), hence cocartesian. So \(\psi^*Q\) is a cofibre diagram with restriction the arrow \(v:y\to z\), and its triangle

\[
y\xrightarrow{v}z\to Q_{21}\xrightarrow{\iota'^{-1}(Q_{21}\to Q_{22})}\Sigma y
\]

is distinguished, where \(\iota'\) belongs to the composite square of \(\psi^*Q\), the square \(G'\) on \((1,0),(1,2),(2,0),(2,2)\) in this order. Composing with \(\iota_E:\Sigma x\cong Q_{21}\) gives an isomorphic distinguished triangle \((v,w,m)\) with \(m=\iota'^{-1}(Q_{21}\to Q_{22})\,\iota_E\).

Let \(G\) be the square on \((1,0),(2,0),(1,2),(2,2)\), in this order; it is a composite of \(B\) and \(C\), hence cocartesian, and it vanishes at \((2,0)\) and \((1,2)\). The square \(G'\) is its transpose, so \(\iota'=\iota_G\circ\tau=-\iota_G\) by Lemma 2.1. The morphisms \((0,0)\to(1,0)\), \((2,0)\to(2,0)\), \((0,1)\to(1,2)\), \((2,1)\to(2,2)\) of \(L\) form a transformation from the square \(E\) to the square \(G\); the induced morphism \(E^*Q\to G^*Q\) has component \(u\) at \((0,0)\), so by naturality of \(\iota\) its component \(Q_{21}\to Q_{22}\) equals \(\iota_G\,\Sigma u\,\iota_E^{-1}\). Therefore

\[
m=-\iota_G^{-1}\,\iota_G\,\Sigma u\,\iota_E^{-1}\,\iota_E=-\Sigma u . \qquad\square
\]

**Lemma 3.3 (exact sequences).** For a distinguished triangle \(x\xrightarrow uy\xrightarrow vz\xrightarrow w\Sigma x\) and every object \(T\), the sequence

\[
\begin{aligned}
&\operatorname{Hom}(T,x)\to\operatorname{Hom}(T,y)\\
&\quad\to\operatorname{Hom}(T,z)\to\operatorname{Hom}(T,\Sigma x)\\
&\quad\to\operatorname{Hom}(T,\Sigma y)
\end{aligned}
\]

of abelian groups, given by composition with \(u,v,w,\Sigma u\), is exact.

**Proof.** For \(T_f\), the composite \(vu\) factors through \(Y_{01}\cong0\), because \(s_{01}^*Y_f\) commutes; so \(vu=0\) for every distinguished triangle. Let \(b:T\to y\) with \(vb=0\). The triangles \(T\to0\to\Sigma T\xrightarrow{-1}\Sigma T\) and \((v,w,-\Sigma u)\) are distinguished, by the identity triangle and Proposition 3.2, and \((b,0)\) is a commutative square between their first maps. Extension of squares gives \(c:\Sigma T\to\Sigma x\) with \((-\Sigma u)c=(\Sigma b)(-1)\). Since \(\Sigma\) is fully faithful, \(c=\Sigma a\) with \(\Sigma(ua)=\Sigma b\), so \(b=ua\). This is exactness at \(\operatorname{Hom}(T,y)\). Exactness at the next two places is the same statement for the rotated triangles \((v,w,-\Sigma u)\) and \((w,-\Sigma u,-\Sigma v)\); signs do not change kernels and images. \(\square\)

**Corollary 3.4 (five lemma).** If \((a,b,c)\) is a morphism of distinguished triangles and \(a\) and \(b\) are isomorphisms, so is \(c\).

**Proof.** Composition with \(a\), \(b\), \(c\), \(\Sigma a\), \(\Sigma b\) maps the exact sequence of Lemma 3.3 for the first triangle to that for the second. Four of the five maps are bijections, so by the five lemma for abelian groups \(\operatorname{Hom}(T,c)\) is bijective for every \(T\), and \(c\) is an isomorphism. \(\square\)

**Rotation in the other direction.** Suppose \((v,w,-\Sigma u)\) is distinguished, with \(u:x\to y\). By completion choose a distinguished triangle \(x\xrightarrow uy\xrightarrow{v'}z'\xrightarrow{w'}\Sigma x\). Rotating each of \((v,w,-\Sigma u)\) and \((u,v',w')\) forward by Proposition 3.2 until it begins with \(-\Sigma u\) gives the distinguished triangles

\[
\begin{gathered}
(-\Sigma u,-\Sigma v,-\Sigma w),\\
(-\Sigma u,-\Sigma v',-\Sigma w').
\end{gathered}
\]

Extension of the identity square gives a morphism \((1,1,c)\) between them, and \(c\) is an isomorphism by Corollary 3.4. As \(\Sigma\) is fully faithful, \(c=\Sigma c_0\) with \(c_0v=v'\) and \(w'c_0=w\), so \((1,1,c_0)\) is an isomorphism from \((u,v,w)\) to \((u,v',w')\), and \((u,v,w)\) is distinguished.

**Proposition 3.5 (octahedron).** Let \(u_1:x\to y\) and \(u_2:y\to z\), with \(u_3=u_2u_1\). There are distinguished triangles

\[
\begin{gathered}
x\xrightarrow{u_1}y\xrightarrow{v_1}c_1\xrightarrow{w_1}\Sigma x,\\
x\xrightarrow{u_3}z\xrightarrow{v_3}c_3\xrightarrow{w_3}\Sigma x,
\end{gathered}
\]
\[
\begin{gathered}
y\xrightarrow{u_2}z\xrightarrow{v_2}c_2\xrightarrow{w_2}\Sigma y,\\
c_1\xrightarrow{a}c_3\xrightarrow{b}c_2\xrightarrow{(\Sigma v_1)w_2}\Sigma c_1,
\end{gathered}
\]

such that

\[
\begin{gathered}
av_1=v_3u_2,\quad w_3a=w_1,\\
bv_3=v_2,\quad w_2b=(\Sigma u_1)w_3 .
\end{gathered}
\]

**Proof.** *A diagram of shape \([2]\).* First let \(F\) be in \(\mathbb D([2])\) with underlying diagram \(x\xrightarrow{u_1}y\xrightarrow{u_2}z\). Let \(P\subset[4]\times[2]\) be the full subcategory without \((4,0)\) and \((0,2)\), let \(N\subset P\) be the full subcategory on

\[
\begin{gathered}
(0,0),(1,0),(2,0),(3,0),\\
(0,1),(4,1),(1,2),
\end{gathered}
\]

let \(n_0:[2]\to N\) be the string \((0,0)\to(1,0)\to(2,0)\), a sieve, and \(n_1:N\to P\) the inclusion. Put \(D=n_{1!}n_{0*}F\). Then \(D\) vanishes at \((3,0),(0,1),(4,1),(1,2)\), and the six unit squares of \(P\), with corners \((1,1)\), \((2,1)\), \((3,1)\), \((2,2)\), \((3,2)\), \((4,2)\), are cocartesian by Corollary 2.2 of the lesson on recognizing cocartesian squares, adding these corners in this order. In each case the functor \(r\) is the inclusion of the three other vertices \((i,j)\), \((i+1,j)\), \((i,j+1)\) into the objects already present below the corner \((i+1,j+1)\). Such an object \(q\) satisfies \(q\le(i+1,j)\) or \(q\le(i,j+1)\), since \(q\ne(i+1,j+1)\), and it satisfies both exactly when \(q\le(i,j)\), the coordinatewise minimum. So the left adjoint of \(r\) sends \(q\) to \((0,0)\) if \(q\le(i,j)\), to \((1,0)\) if \(q\) lies below \((i+1,j)\) only, and to \((0,1)\) if it lies below \((i,j+1)\) only; this map is order-preserving. The same rule gives the left adjoints used in the proof of Proposition 3.2. By Proposition 2.3 there and its transpose, every rectangle of \(P\) made of unit squares is cocartesian. The underlying diagram of \(D\) is

\[
\begin{array}{ccccccccc}
x&\!\to\!&y&\!\to\!&z&\!\to\!&0&&\\
\downarrow&&\downarrow&&\downarrow&&\downarrow&&\\
0&\!\to\!&c_1&\!\to\!&c_3&\!\to\!&D_{31}&\!\to\!&0\\
&&\downarrow&&\downarrow&&\downarrow&&\downarrow\\
&&0&\!\to\!&c_2&\!\to\!&D_{32}&\!\to\!&D_{42}
\end{array}
\]

with \(c_1=D_{11}\), \(c_3=D_{21}\), \(c_2=D_{22}\).

Four restrictions of \(D\) along injective order-preserving maps from \([2]\times[1]\) are cofibre diagrams: columns \(0,1,3\) of rows \(0,1\); columns \(0,2,3\) of rows \(0,1\); columns \(1,2,3\) of rows \(0,2\); columns \(1,2,4\) of rows \(1,2\). Their unit squares are rectangles of \(P\), hence cocartesian, and their two vanishing vertices lie among the zeros of \(D\). Their triangles are distinguished. With

\[
\begin{gathered}
\iota_x:\Sigma x\cong D_{31},\quad
\iota_y:\Sigma y\cong D_{32},\\
\iota_{c_1}:\Sigma c_1\cong D_{42}
\end{gathered}
\]

the isomorphisms of their composite squares, these triangles are the four triangles of the statement, with \(a\) and \(b\) the maps \(D_{11}\to D_{21}\) and \(D_{21}\to D_{22}\), \(v_2=bv_3\), and

\[
\begin{gathered}
w_1=\iota_x^{-1}(D_{11}\to D_{31}),\\
w_3=\iota_x^{-1}(D_{21}\to D_{31}),
\end{gathered}
\]
\[
w_2=\iota_y^{-1}(D_{22}\to D_{32}),
\]

and fourth map \(\iota_{c_1}^{-1}(D_{22}\to D_{42})\). The first three identities hold because \(D\) is a diagram on a poset. The rectangles of \(\iota_x\) and \(\iota_y\), on \((0,0),(3,0),(0,1),(3,1)\) and on \((1,0),(3,0),(1,2),(3,2)\), are related by the transformation with components \((0,0)\to(1,0)\), \((3,0)\to(3,0)\), \((0,1)\to(1,2)\), \((3,1)\to(3,2)\), which keeps each leg on its own axis. By naturality of \(\iota\), \(D_{31}\to D_{32}\) equals \(\iota_y\,\Sigma u_1\,\iota_x^{-1}\), and so

\[
\begin{aligned}
w_2b&=\iota_y^{-1}(D_{21}\to D_{32})\\
&=(\Sigma u_1)\,\iota_x^{-1}(D_{21}\to D_{31})\\
&=(\Sigma u_1)w_3 .
\end{aligned}
\]

In the same way the transformation from the rectangle of \(\iota_y\) to the rectangle of \(\iota_{c_1}\), on \((1,1),(4,1),(1,2),(4,2)\), with components \((1,0)\to(1,1)\), \((3,0)\to(4,1)\), \((1,2)\to(1,2)\), \((3,2)\to(4,2)\), gives \(D_{32}\to D_{42}=\iota_{c_1}\,\Sigma v_1\,\iota_y^{-1}\), so the fourth map is \((\Sigma v_1)w_2\).

*Every composable pair.* Let \(u_1,u_2\) be arbitrary. By strongness choose \(f_1\) in \(\mathbb D([1])\) whose underlying arrow is isomorphic to \(u_1\); transporting, we may assume it is \(u_1\). The object \(1\) is terminal in \([1]\), so \(1:e\to[1]\) is right adjoint to \(p\), and \(1^*\) is left adjoint to \(p^*\) (Lemma 2.2 of the lesson on homotopy exact squares) with identity counit. Hence there is a morphism \(\varphi:f_1\to p^*z\) with \(\varphi_1=u_2\), and by naturality \(\varphi_0=u_2u_1\). Strongness of \(\mathbb D\) for the shape \([1]\) gives \(H\) in \(\mathbb D([1]\times[1])\) whose partial underlying diagram, with the first factor as the direction of the arrow, is isomorphic to \(\varphi\). Its underlying diagram contains the path \((0,0)\to(0,1)\to(1,1)\), isomorphic to \(x\xrightarrow{u_1}y\xrightarrow{u_2}z\). Restricting \(H\) along this path gives \(F\) in \(\mathbb D([2])\), and the first part applies after transport along the isomorphism. \(\square\)

With the identity and completion triangles, closure under isomorphism, rotation in both directions, extension of squares and the octahedron established, and \(\Sigma\) an additive equivalence, Theorem 3.1 is proved.

Proposition 3.5 gives the octahedron for one choice of the three triangles on \(u_1\), \(u_2\), \(u_3\). Distinguished triangles on the same morphism are isomorphic by an isomorphism that is the identity on the first two objects (extension of squares and Corollary 3.4), so the octahedron can be transported to any prescribed choice.

## 4. Exercises

**4.1** (easy). Show that in a distinguished triangle \(x\xrightarrow uy\to z\to\Sigma x\), the morphism \(u\) is an isomorphism if and only if \(z\) is a zero object.

**4.2** (easy). Show that if \((u,v,w)\) is distinguished, so is \((-u,-v,w)\).

**4.3** (medium). Show that the direct sum of two distinguished triangles is distinguished.

**4.4** (medium). Show that if \((u,v,w)\) is distinguished, so is \((\Sigma u,\Sigma v,-\Sigma w)\).

**4.5** (medium). Let \(x\) be a nonzero object. Show that the morphism of triangles completing a square in Section 3 is not unique in general, by finding an endomorphism \((1,1,c)\) of a distinguished triangle with \(c\neq1\).

## 5. Solutions

**4.1.** If \(u\) is invertible, compare the triangle with \(x\xrightarrow1x\to0\to\Sigma x\) through \((1,u,\cdot)\): extension of squares and Corollary 3.4 give \(z\cong0\). If \(z\cong0\), the exact sequences of Lemma 3.3 for the triangle and its rotations give \(\operatorname{Hom}(T,x)\cong\operatorname{Hom}(T,y)\) through \(u\) for every \(T\), since the neighbouring terms \(\operatorname{Hom}(T,\Omega z)\cong\operatorname{Hom}(T,\Sigma^{-1}z)\) and \(\operatorname{Hom}(T,z)\) vanish; so \(u\) is invertible.

**4.2.** \((1,-1,1)\) is an isomorphism from \((u,v,w)\) to \((-u,-v,w)\): the squares read \((-1)u=(-u)1\), \(1\cdot v=(-v)(-1)\), and \(w\cdot1=(\Sigma1)w\).

**4.3.** Write the two triangles as \(T_f\) and \(T_{f'}\). The coproduct \(Y_f\sqcup Y_{f'}\) in \(\mathbb D([2]\times[1])\) has zero values at \((2,0)\) and \((0,1)\), and its two squares are cocartesian by Exercise 5.3 of the lesson on recognizing cocartesian squares, so it is a cofibre diagram. Evaluation and \(\Sigma\) preserve coproducts, and \(\iota\) is natural, so its triangle is \(T_f\oplus T_{f'}\).

**4.4.** Rotating three times by Proposition 3.2 gives \((-\Sigma u,-\Sigma v,-\Sigma w)\). The triple \((-1,1,-1)\) is an isomorphism from it to \((\Sigma u,\Sigma v,-\Sigma w)\): the squares read \(1\cdot(-\Sigma u)=(\Sigma u)(-1)\), \((-1)(-\Sigma v)=(\Sigma v)1\), and \(\Sigma(-1)(-\Sigma w)=(-\Sigma w)(-1)\).

**4.5.** The triangle \(x\xrightarrow0\Sigma x\xrightarrow{\mathrm{in}_1}\Sigma x\oplus\Sigma x\xrightarrow{\mathrm{pr}_2}\Sigma x\) is distinguished: it is the direct sum (Exercise 4.3) of \(0\to\Sigma x\xrightarrow1\Sigma x\to0\), a rotation of an identity triangle, and of \(x\to0\to\Sigma x\xrightarrow1\Sigma x\). The latter is isomorphic, through \((1,1,-1)\), to the rotation \(x\to0\to\Sigma x\xrightarrow{-1}\Sigma x\) of \(x\xrightarrow1x\to0\to\Sigma x\). Let \(c=1+\mathrm{in}_1\mathrm{pr}_2\). Then \(c\,\mathrm{in}_1=\mathrm{in}_1\) and \(\mathrm{pr}_2c=\mathrm{pr}_2\), so \((1,1,c)\) is a morphism of triangles, and \(c\neq1\) because \(\mathrm{in}_1\mathrm{pr}_2\neq0\) when \(\Sigma x\neq0\).

## Sources

- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 4.2: the canonical triangulated structure, with distinguished triangles from cofibre diagrams, rotation through a diagram on \([2]\times[2]\) without one corner, and the octahedron through a diagram on \([4]\times[2]\) without two corners. The flip lemma (Lemma 2.1) and the explicit bookkeeping of the identifications \(\iota\) are written for this lesson.
- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000 — the expectation that the triangulated structure of derived categories follows formally from the derivator.

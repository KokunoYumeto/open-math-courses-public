# Stable derivators are additive

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The values of a stable derivator are additive categories, although additivity is not among the axioms. This lesson proves it in two steps. First, finite coproducts and finite products agree: the coproduct of two degenerate squares is a cocartesian square with zero corner, stability makes it cartesian, and a cartesian square with zero corner exhibits a product. This makes every morphism set a commutative monoid. Second, every identity morphism has an additive inverse. A suspension is a homotopy colimit of a span with two zero legs; spans with three legs map to and from it, and collapsing their legs shows that the automorphism of the suspension that exchanges the two legs is inverse to the identity. Since every object of a stable derivator is a suspension, the monoids are groups.

**Prerequisites.** The lessons [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md) (Section 3, (Der1), Proposition 5.1), [*Homotopy exact squares*](homotopy-exact-squares.md) (Lemmas 1.1, 1.2 and 2.2, Proposition 2.3, Corollary 2.4, Lemma 3.1, Proposition 3.3), [*Pointed and stable derivators*](pointed-and-stable-derivators.md) (Propositions 1.2, 1.3 and 4.2, Lemma 2.2, Definition 3.1) and [*Recognizing cocartesian squares*](recognizing-cocartesian-squares.md) (Lemma 1.1, Corollary 3.3, Exercise 5.3).

Throughout, \(\mathbb D\) is a pointed derivator; stability is assumed where stated. We write \(0\) for zero objects and for zero morphisms, and \(p_A:A\to e\) for the unique functor. For a functor \(u:A\to B\) the *comparison map*

\[
\begin{gathered}
\kappa_u:\operatorname{hocolim}_Au^*Y\longrightarrow\operatorname{hocolim}_BY,\\
Y\in\mathbb D(B),
\end{gathered}
\]

is the base change morphism of the square with top \(u\), sides \(p_A\) and \(p_B\), bottom \(1_e\), and identity transformation. For composable \(u\) and \(v\), horizontal pasting gives \(\kappa_{vu}=\kappa_v\cdot\kappa_u\,v^*\). For an object \(y\) of \(B\), viewed as a functor \(e\to B\), \(\kappa_y=y^*\eta\), where \(\eta\) is the unit of \(\operatorname{hocolim}_B\dashv p_B^*\).

## 1. Biproducts

Let \(\pi_1,\pi_2:{\square}\to[1]\) be the two projections, \(\pi_1(a,b)=a\) and \(\pi_2(a,b)=b\), and let \(0:e\to[1]\) be the object \(0\), a sieve. For \(x\) in \(\mathbb D(e)\), the object \(0_*x\) of \(\mathbb D([1])\) is an arrow \(x\to0\) (Proposition 1.3 of the lesson on pointed derivators). Put

\[
A_x=\pi_2^*\,0_*x,\qquad B_x=\pi_1^*\,0_*x .
\]

Morphisms of \(\square\) that \(\pi_2\) sends to identities induce identity maps, so the underlying diagrams are

\[
A_x:\;
\begin{array}{ccc}
x&\xrightarrow{1}&x\\
\downarrow&&\downarrow\\
0&\xrightarrow{1}&0
\end{array}
\qquad
B_x:\;
\begin{array}{ccc}
x&\longrightarrow&0\\
{\scriptstyle1}\downarrow&&\downarrow{\scriptstyle1}\\
x&\longrightarrow&0
\end{array}
\]

**Lemma 1.1.** \(A_x\) and \(B_x\) are cocartesian.

**Proof.** The comparison map of \(A_x\) (Section 1 of the lesson on recognizing cocartesian squares) goes from \(\operatorname{hocolim}_\ulcorner(\pi_2i_\ulcorner)^*0_*x\) to \((A_x)_{11}\cong0\). The functor \(\pi_2i_\ulcorner:{\ulcorner}\to[1]\) sends \((0,0)\) and \((1,0)\) to \(0\) and \((0,1)\) to \(1\); it is a right adjoint, with left adjoint \(0\mapsto(0,0)\), \(1\mapsto(0,1)\). By Proposition 2.3 and Corollary 2.4 of the lesson on homotopy exact squares, this homotopy colimit is isomorphic to \(\operatorname{hocolim}_{[1]}0_*x\cong(0_*x)_1\cong0\). A morphism between zero objects is an isomorphism, so Lemma 1.1 of the lesson on recognizing cocartesian squares applies. For \(B_x\), use \(\pi_1i_\ulcorner\), with left adjoint \(0\mapsto(0,0)\), \(1\mapsto(1,0)\). \(\square\)

**Lemma 1.2.** Let \(W\) in \(\mathbb D(\square)\) be cartesian with \(W_{11}\) a zero object. Then \(W_{00}\), together with the maps \(W_{00}\to W_{10}\) and \(W_{00}\to W_{01}\) of the underlying diagram, is a product of \(W_{10}\) and \(W_{01}\) in \(\mathbb D(e)\).

**Proof.** Let \(T\) be in \(\mathbb D(e)\). The object \((0,0)\) is initial in \(\square\), so \((0,0):e\to\square\) is left adjoint to \(p_\square\), and by Lemma 2.2 of the lesson on homotopy exact squares, \(p_\square^*\) is left adjoint to \((0,0)^*\). The unit of this adjunction is the identity, and the counit at \(W\) is the morphism \(p_\square^*W_{00}\to W\) whose components are the maps \(W_{00}\to W_a\) of the underlying diagram. So

\[
\operatorname{Hom}(T,W_{00})\to\operatorname{Hom}(p_\square^*T,W),
\]

sending \(\varphi\) to the morphism with components \(W_{00}\to W_a\) composed with \(\varphi\), is bijective. Since \(W\) is cartesian, the unit \(W\to i_{\lrcorner*}i_\lrcorner^*W\) is invertible, and restriction \(\psi\mapsto i_\lrcorner^*\psi\) is a bijection \(\operatorname{Hom}(U,W)\to\operatorname{Hom}(i_\lrcorner^*U,i_\lrcorner^*W)\) for every \(U\), by the triangle identity. The inclusion \(k\) of the discrete category on \((1,0)\) and \((0,1)\) into \(\lrcorner\) is a sieve, and \(i_\lrcorner^*W\) vanishes at the remaining object \((1,1)\), so it lies in the essential image of \(k_*\) (Proposition 3.3 of the lesson on homotopy exact squares). In the same way restriction along \(k\) is bijective on morphisms into \(i_\lrcorner^*W\), and by (Der1) a morphism of \(\mathbb D(\{(1,0)\}\sqcup\{(0,1)\})\) is a pair of morphisms. The composite bijection

\[
\begin{aligned}
\operatorname{Hom}(T,W_{00})&\longrightarrow\operatorname{Hom}(T,W_{10})\\
&\qquad\times\operatorname{Hom}(T,W_{01})
\end{aligned}
\]

sends \(\varphi\) to its composites with the two maps of the underlying diagram, because \(p_\square^*T\) has value \(T\) and identity structure maps. This is the universal property of the product. \(\square\)

By duality (Remark 4.3 of the lesson on Kan extensions), a cocartesian square \(W\) with \(W_{00}\) a zero object exhibits \(W_{11}\), with the maps from \(W_{10}\) and \(W_{01}\), as a coproduct.

In a category with a zero object and finite coproducts and products, the *canonical map* \(x\sqcup y\to x\times y\) is the morphism whose composites with the injections and projections are \(1_x\), \(0\), \(0\), \(1_y\).

**Theorem 1.3.** Let \(\mathbb D\) be stable and \(J\) a small category. For all \(x\) and \(y\) in \(\mathbb D(J)\) the canonical map \(x\sqcup y\to x\times y\) is invertible.

**Proof.** First let \(J=e\). The coproduct \(C=A_x\sqcup B_y\) in \(\mathbb D(\square)\) is cocartesian, by Lemma 1.1 and Exercise 5.3 of the lesson on recognizing cocartesian squares, hence cartesian. Evaluation at an object has a right adjoint, so it preserves coproducts, and the maps of the underlying diagram of \(C\) are the coproducts of those of \(A_x\) and \(B_y\). So \(C_{11}\cong0\sqcup0\cong0\), and the maps \(C_{00}\to C_{10}\) and \(C_{00}\to C_{01}\) are

\[
\begin{gathered}
x\sqcup y\xrightarrow{(1,\,0)}x\sqcup0\cong x,\\
x\sqcup y\xrightarrow{(0,\,1)}0\sqcup y\cong y .
\end{gathered}
\]

By Lemma 1.2 these two maps exhibit \(x\sqcup y\) as a product of \(x\) and \(y\); that is, the canonical map is invertible. For general \(J\), the shifted derivator \(\mathbb D^J\) is stable (Corollary 3.3 of the lesson on recognizing cocartesian squares) and \(\mathbb D^J(e)=\mathbb D(J)\). \(\square\)

We write \(x\oplus y\) for the *biproduct*, with injections \(\mathrm{in}_x,\mathrm{in}_y\) and projections \(\mathrm{pr}_x,\mathrm{pr}_y\); then \(\mathrm{pr}_x\mathrm{in}_x=1\), \(\mathrm{pr}_y\mathrm{in}_y=1\), \(\mathrm{pr}_x\mathrm{in}_y=0\) and \(\mathrm{pr}_y\mathrm{in}_x=0\). A morphism into \(x\oplus y\) is determined by its two components, written \(\langle f,g\rangle\), and a morphism out of it by its restrictions, written \([f,g]\).

## 2. Addition of morphisms

A category with a zero object in which every canonical map \(x\sqcup y\to x\times y\) is invertible is called *semi-additive*. Let \(\Delta_x=\langle1,1\rangle:x\to x\oplus x\) and \(\nabla_y=[1,1]:y\oplus y\to y\). For \(f,g:x\to y\) put

\[
f+g=[f,g]\circ\Delta_x .
\]

The map \([f,g]\) equals \(\nabla_y(f\oplus g)\), and \(\langle f,g\rangle=(f\oplus g)\Delta_x\), where \(f\oplus g\) has components \(f\,\mathrm{pr}_1\) and \(g\,\mathrm{pr}_2\); so also \(f+g=\nabla_y\langle f,g\rangle\).

**Proposition 2.1.** In a semi-additive category:

1. each \(\operatorname{Hom}(x,y)\) is a commutative monoid under \(+\), with neutral element \(0\);
2. composition is bilinear: \((f+g)k=fk+gk\) and \(k(f+g)=kf+kg\);
3. a functor between semi-additive categories that preserves zero objects and finite products, or zero objects and finite coproducts, preserves \(+\).

**Proof.** (1) The map \([f,0]\) equals \(f\,\mathrm{pr}_1\), as both restrict to \(f\) and \(0\); so \(f+0=f\,\mathrm{pr}_1\Delta=f\), and likewise \(0+f=f\). Let \(s\) be the automorphism of \(x\oplus x\) exchanging the summands. Then \([g,f]=[f,g]s\) and \(s\Delta=\Delta\), so \(g+f=f+g\). For associativity, let \(x^{\oplus3}\) be the triple biproduct, \([f,g,h]\) the map with restrictions \(f,g,h\), and \(\iota_{12}:x\oplus x\to x^{\oplus3}\) the inclusion of the first two summands. Then \([f+g,h]=[f,g,h]\circ[\iota_{12}\Delta,\mathrm{in}_3]\), and the composite \([\iota_{12}\Delta,\mathrm{in}_3]\circ\Delta\) has all three components equal to \(1\). So \((f+g)+h=[f,g,h]\circ\langle1,1,1\rangle\), and the same computation gives this value for \(f+(g+h)\).

(2) \(\Delta_xk=(k\oplus k)\Delta_{x'}\) and \([f,g](k\oplus k)=[fk,gk]\), which gives the first identity. The second follows from \(k\nabla_y=\nabla_{y'}(k\oplus k)\) and \((k\oplus k)\langle f,g\rangle=\langle kf,kg\rangle\).

(3) Let \(F\) preserve zero objects and finite products. Then \(F\) preserves zero morphisms, and \(F(\mathrm{in}_x)\) has components \(1\) and \(0\), so it is the injection of the biproduct \(Fx\oplus Fy\); hence \(F\) preserves biproducts with their injections and projections, \(F(\Delta)=\Delta\), \(F(\nabla)=\nabla\) and \(F(f\oplus g)=Ff\oplus Fg\). So \(F(f+g)=Ff+Fg\). The case of coproducts is dual. \(\square\)

A semi-additive category is *additive* when every \(\operatorname{Hom}(x,y)\) is a group. By (2) it suffices that every \(1_x\) has an additive inverse \(-1_x\): then \(f\circ(-1_x)\) is inverse to \(f\).

## 3. Spans with several legs

For \(n\ge0\) let \(V_n\) be the poset with elements \(c,e_0,\dots,e_n\) and relations \(c<e_i\): a span with \(n+1\) legs. Thus \(V_1=\ulcorner\), with \(c=(0,0)\), \(e_0=(1,0)\), \(e_1=(0,1)\), and \(V_0=[1]\). Write \(\langle n\rangle=\{0,\dots,n\}\). A map of sets \(\varphi:\langle k\rangle\to\langle n\rangle\) gives the order-preserving map

\[
V_\varphi:V_k\to V_n,\qquad c\mapsto c,\quad e_i\mapsto e_{\varphi(i)} .
\]

We write \(\varphi\) as the tuple \((\varphi(0),\dots,\varphi(k))\).

The inclusion \(c:e\to V_n\) is a sieve, so for \(W\) in \(\mathbb D(e)\) the object \(c_*W\) of \(\mathbb D(V_n)\) has value \(W\) at \(c\) and zero objects at the legs. Put

\[
S_nW=\operatorname{hocolim}_{V_n}c_*W .
\]

Then \(S_1W\) is the suspension \(\Sigma W\) (Definition 3.1 and Lemma 2.2 of the lesson on pointed derivators), and \(S_0W\cong(c_*W)_{e_0}\cong0\) by Corollary 2.4 of the lesson on homotopy exact squares, since \(e_0\) is terminal in \(V_0\).

**Construction 3.1.** For \(\varphi:\langle k\rangle\to\langle n\rangle\), the square with top \(1_e\), left \(c:e\to V_k\), right \(c:e\to V_n\), bottom \(V_\varphi\), commutes. Its base change morphism for right Kan extensions (Section 3 of the lesson on Kan extensions) is a map

\[
\beta^\varphi:V_\varphi^*c_*W\longrightarrow c_*W .
\]

It is invertible. At the legs both sides are zero objects. At \(c\), composing \(c^*\beta^\varphi\) with the counit \(c^*c_*W\to W\) on \(V_k\) gives the counit on \(V_n\), by the definition of \(\beta^\varphi\) and a triangle identity; both counits are invertible because \(c\) is fully faithful. By (Der2), \(\beta^\varphi\) is invertible. Define \(\varphi_*:S_kW\to S_nW\) as the composite

\[
\begin{aligned}
S_kW&\xrightarrow{\;\operatorname{hocolim}(\beta^\varphi)^{-1}\;}\operatorname{hocolim}_{V_k}V_\varphi^*c_*W\\
&\xrightarrow{\;\kappa_{V_\varphi}\;}S_nW .
\end{aligned}
\]

**Lemma 3.2.** \((\psi\varphi)_*=\psi_*\varphi_*\), \((1)_*=1\), and \(\varphi_*\) is natural in \(W\). If \(\varphi:\langle1\rangle\to\langle1\rangle\) is constant, then \(\varphi_*=0\).

**Proof.** Horizontal pasting of the two squares for \(\varphi\) and \(\psi\) gives \(\kappa_{V_\psi V_\varphi}=\kappa_{V_\psi}\cdot\kappa_{V_\varphi}V_\psi^*\), and its dual for right Kan extensions gives \(\beta^{\psi\varphi}=\beta^\varphi\cdot V_\varphi^*\beta^\psi\). Naturality of \(\kappa_{V_\varphi}\) moves \(\operatorname{hocolim}(\beta^\psi)^{-1}\) past it, which gives the composition rule. The identity and naturality are immediate from the construction. A constant map \(\langle1\rangle\to\langle1\rangle\) factors through \(\langle0\rangle\), so \(\varphi_*\) factors through \(S_0W\cong0\). \(\square\)

The *flip* of \(\Sigma W\) is \(\tau=\tau_W=(1,0)_*:\Sigma W\to\Sigma W\), induced by the exchange of the two legs of \(\ulcorner\). By Lemma 3.2, \(\tau^2=1\), and \(\tau\) is natural in \(W\).

Consider the maps \(a=(0,1)\), \(b=(2,1)\) and \(d=(0,2)\) from \(\langle1\rangle\) to \(\langle2\rangle\). Topologically, \(S_2W\) is three cones on \(W\) glued along their common base; \(a_*\) and \(b_*\) are the two spheres through the middle cone, and \(d_*\) is the sphere formed by the outer two cones.

**Lemma 3.3 (two legs at a time).** The morphism \([a_*,b_*]:\Sigma W\sqcup\Sigma W\to S_2W\) is an isomorphism.

**Proof.** Let \(q:V_2\to V_1\) send \(c\) and \(e_1\) to \(c\), \(e_0\) to \(e_0\), and \(e_2\) to \(e_1\); it is order-preserving. Since \(p_{V_2}=p_{V_1}q\), we take \(\operatorname{hocolim}_{V_2}=\operatorname{hocolim}_{V_1}q_!\) with the composite adjunction, and put \(F=c_*W\) on \(V_2\).

The comma category of \(q\) over an object \(y\) of \(V_1\) is the subposet of \(V_2\) of elements \(v\) with \(q(v)\le y\). Over \(c\) it is \(\{c<e_1\}\), with terminal element \(e_1\), so (Der4) and Corollary 2.4 of the lesson on homotopy exact squares give \((q_!F)_c\cong F_{e_1}\cong0\). Over \(e_0\) it is \(\{c,e_0,e_1\}\), and \(V_a\) is an isomorphism from \(V_1\) onto it; over \(e_1\) it is \(\{c,e_1,e_2\}\), and \(V_b\) is an isomorphism onto it.

Since \((q_!F)_c\cong0\), the object \(Y=q_!F\) lies in the essential image of the left Kan extension along the cosieve \(k\) that includes the discrete category on \(e_0\) and \(e_1\) into \(V_1\) (Proposition 3.3 of the lesson on homotopy exact squares). For \(T\) in \(\mathbb D(e)\), a morphism \(g:\operatorname{hocolim}_{V_1}Y\to T\) corresponds to \(p^*g\circ\eta_Y:Y\to p^*T\), whose component at \(y\) is \(g\circ\kappa_y\). Morphisms \(Y\to p^*T\) correspond bijectively to their restrictions along \(k\), by the argument dual to the one in the proof of Lemma 1.2, that is, to pairs of morphisms \(Y_{e_0}\to T\), \(Y_{e_1}\to T\) by (Der1). So \(\operatorname{hocolim}_{V_1}Y\) is a coproduct of \(Y_{e_0}\) and \(Y_{e_1}\) with injections \(\kappa_{e_0}\) and \(\kappa_{e_1}\).

Vertical pasting (Lemma 1.2 of the lesson on homotopy exact squares) of the comma square of \(q\) at \(y\) with the square with top \(y:e\to V_1\), sides \(1_e\) and \(p_{V_1}\), and bottom \(1_e\), shows that the comparison map of the projection from the comma category to \(V_2\) is \(\kappa_y(q_!F)\) composed with the (Der4) isomorphism. Composing with the isomorphisms \(V_a\) and \(V_b\), the maps \(\kappa_{V_a}\) and \(\kappa_{V_b}\) are, up to isomorphisms of their sources, the two coproduct injections of \(S_2W\). Since \(a_*=\kappa_{V_a}\circ\operatorname{hocolim}(\beta^a)^{-1}\) and \(b_*=\kappa_{V_b}\circ\operatorname{hocolim}(\beta^b)^{-1}\), the map \([a_*,b_*]\) is an isomorphism. \(\square\)

## 4. The flip is −1

**Theorem 4.1.** Let \(\mathbb D\) be stable. For every \(W\) in \(\mathbb D(e)\), \(1_{\Sigma W}+\tau_W=0\).

**Proof.** Let \(f=(0,1,1)\), \(g=(1,1,0)\) and \(h=(0,1,0)\), maps \(\langle2\rangle\to\langle1\rangle\). The composites with \(a\), \(b\), \(d\) are

| | \(a=(0,1)\) | \(b=(2,1)\) | \(d=(0,2)\) |
|---|---|---|---|
| \(f\) | \((0,1)\) | \((1,1)\) | \((0,1)\) |
| \(g\) | \((1,1)\) | \((0,1)\) | \((1,0)\) |
| \(h\) | \((0,1)\) | \((0,1)\) | \((0,0)\) |

By Lemma 3.2, with \((0,1)_*=1\), \((1,0)_*=\tau\) and constant maps inducing \(0\):

\[
f_*a_*=1,\quad f_*b_*=0,\quad f_*d_*=1,
\]
\[
g_*a_*=0,\quad g_*b_*=1,\quad g_*d_*=\tau,
\]
\[
h_*a_*=1,\quad h_*b_*=1,\quad h_*d_*=0 .
\]

The composite of \([a_*,b_*]\) with \(\langle f_*,g_*\rangle:S_2W\to\Sigma W\times\Sigma W\) has components \(1,0,0,1\), so it is the canonical map, which is invertible by Theorem 1.3. With Lemma 3.3, \(\langle f_*,g_*\rangle\) is an isomorphism: two morphisms into \(S_2W\) with equal composites with \(f_*\) and with \(g_*\) are equal. By bilinearity,

\[
f_*(a_*+b_*\tau)=1+0=f_*d_*,
\]
\[
g_*(a_*+b_*\tau)=0+\tau=g_*d_*,
\]

so \(d_*=a_*+b_*\tau\). Applying \(h_*\) gives \(0=h_*d_*=h_*a_*+h_*b_*\tau=1+\tau\). \(\square\)

**Corollary 4.2.** Let \(\mathbb D\) be stable. For every small category \(J\), the category \(\mathbb D(J)\) is additive, and for every functor \(u:J\to K\) the functors \(u^*\), \(u_!\) and \(u_*\) are additive. The suspension and the loop functor are additive.

**Proof.** For \(J=e\): \(\mathbb D(e)\) is semi-additive by Theorem 1.3. Every object \(x\) is isomorphic to \(\Sigma\Omega x\) (Proposition 4.2 of the lesson on pointed derivators); for an isomorphism \(\phi:x\to\Sigma W\), the morphism \(\phi^{-1}\tau_W\phi\) is an additive inverse of \(1_x\) by Theorem 4.1 and bilinearity. So \(\mathbb D(e)\) is additive. For general \(J\), apply this to the stable derivator \(\mathbb D^J\). The functors \(u^*,u_!,u_*\), \(\Sigma\) and \(\Omega\) preserve zero objects (Proposition 1.2 of the lesson on pointed derivators) and, as left or right adjoints, finite coproducts or finite products; Proposition 2.1(3) applies. \(\square\)

So in a stable derivator the flip of a suspension is \(-1\): exchanging the two zero legs of the span defining \(\Sigma W\) acts as the negative of the identity. This sign reappears in the rotation of distinguished triangles.

## 5. Exercises

**5.1** (easy). The represented derivator of pointed sets is pointed. Show that \(\Sigma X\) is a one-point set for every pointed set \(X\), and that the canonical map \(X\sqcup Y\to X\times Y\) is not invertible when \(X\) and \(Y\) have at least two elements each. Which hypothesis of Theorem 1.3 fails?

**5.2** (easy). In a semi-additive category, show that \(\nabla_y=\mathrm{pr}_1+\mathrm{pr}_2\), that \(\Delta_x=\mathrm{in}_1+\mathrm{in}_2\), and that \(1_{x\oplus y}=\mathrm{in}_x\mathrm{pr}_x+\mathrm{in}_y\mathrm{pr}_y\).

**5.3** (medium). Let a semi-additive category carry, on each \(\operatorname{Hom}(x,y)\), an operation \(\boxplus\) with neutral element \(0\) for which composition is bilinear. Show that \(\boxplus=+\).

**5.4** (medium). In a stable derivator, show that \(\Sigma(-f)=-\Sigma f=\tau_y\,\Sigma f\) for every morphism \(f:x\to y\) of \(\mathbb D(e)\).

**5.5** (hard). For \(n\ge1\) and \(1\le k\le n\), let \(j_k=(k,0):\langle1\rangle\to\langle n\rangle\). Show that \([(j_1)_*,\dots,(j_n)_*]\) is an isomorphism from the coproduct of \(n\) copies of \(\Sigma W\) to \(S_nW\).

## 6. Solutions

**5.1.** The suspension is the pushout of \(*\leftarrow X\to*\), a point. For \(X=Y=\{*,1\}\) the coproduct \(X\sqcup Y\) is the wedge, with three elements, and the product has four, so the canonical map is not surjective. The derivator is pointed but not stable: by Lemma 1.1 the square \(A_X\sqcup B_Y\) is cocartesian, and Theorem 1.3 fails because this square is not cartesian.

**5.2.** \(\mathrm{pr}_1+\mathrm{pr}_2=\nabla\langle\mathrm{pr}_1,\mathrm{pr}_2\rangle=\nabla\circ1=\nabla\), since \(\langle\mathrm{pr}_1,\mathrm{pr}_2\rangle=1\). Dually \(\mathrm{in}_1+\mathrm{in}_2=[\mathrm{in}_1,\mathrm{in}_2]\Delta=\Delta\). Finally \(\mathrm{in}_x\mathrm{pr}_x+\mathrm{in}_y\mathrm{pr}_y\) has, by bilinearity, the composites \(\mathrm{pr}_x(\mathrm{in}_x\mathrm{pr}_x+\mathrm{in}_y\mathrm{pr}_y)=\mathrm{pr}_x+0=\mathrm{pr}_x\) and likewise \(\mathrm{pr}_y\), so it is the identity.

**5.3.** For \(f,g:x\to y\), the morphism \(\mathrm{in}_1f\boxplus\mathrm{in}_2g\) has components \(\mathrm{pr}_1(\mathrm{in}_1f\boxplus\mathrm{in}_2g)=f\boxplus0=f\) and \(g\), so it equals \(\langle f,g\rangle\). Then \(f+g=\nabla\langle f,g\rangle=\nabla\mathrm{in}_1f\boxplus\nabla\mathrm{in}_2g\), which is \(f\boxplus g\).

**5.4.** \(\Sigma\) is additive (Corollary 4.2), so \(\Sigma(-f)=-\Sigma f\). By Theorem 4.1, \(-\Sigma f=(-1_{\Sigma y})\Sigma f=\tau_y\Sigma f\).

**5.5.** Let \(q:V_n\to V_{n-1}\) send \(c\) and \(e_0\) to \(c\) and \(e_k\) to \(e_{k-1}\) for \(k\ge1\). The comma category over \(c\) is \(\{c<e_0\}\), so \((q_!c_*W)_c\cong0\); over \(e_{k-1}\) it is \(\{c,e_0,e_k\}\), and \(V_{j_k}\) is an isomorphism from \(V_1\) onto it. The proof of Lemma 3.3 applies word for word, with the discrete category on \(e_0,\dots,e_{n-1}\), a cosieve in \(V_{n-1}\), and with finite coproducts (Proposition 5.1 of the lesson on Kan extensions).

## Sources

- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 4.1: additivity of stable derivators, with semi-additivity from a three-by-three diagram of bicartesian squares and the additive inverse from the action of the symmetric group on three letters on a homotopy limit of a three-legged cospan. The proofs above use instead the coproduct of two degenerate squares, and the collapse maps of a three-legged span, which is the argument showing that a suspension is a co-H-group in homotopy theory.

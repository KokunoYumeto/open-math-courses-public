# The Pimsner–Voiculescu exact sequence

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*



Crossing an algebra by an automorphism compares its K-classes with their translates. The Pimsner–Voiculescu sequence makes that comparison exact. Its coefficient arrows are the maps induced by the actual inclusion into the crossed product. We will verify that identification on Fourier functions, then compute reflection and Cantor examples and recover the Bunce–Deddens algebra from an odometer.

Let \(A\) be an arbitrary complex C*-algebra and \(\alpha\in\operatorname{Aut}(A)\). Set \(B=A\rtimes_\alpha\mathbb Z\), with convention

\[
uau^*=\alpha(a),\qquad \iota:A\longrightarrow B.
\tag{0.1}
\]

For nonunital \(A\), \(u\) is a multiplier; the elements \(au^n\) belong to \(B\). Full and reduced crossed products agree here because \(\mathbb Z\) is amenable. These facts and the positive gauge action are KT-CP-05, Proposition 5.1 and its Fourier discussion.

## 1. The sequence and the proof inputs

**Theorem 1.1 (Pimsner–Voiculescu).** There are natural maps \(d_i:K_i(B)\to K_{1-i}(A)\) making the following cyclic sequence exact:

\[
\begin{gathered}
K_0(A)\xrightarrow{1-\alpha_{*,0}}K_0(A),\\
K_0(A)\xrightarrow{\iota_*}K_0(B),\\
K_0(B)\xrightarrow{d_0}K_1(A),\\
K_1(A)\xrightarrow{1-\alpha_{*,1}}K_1(A),\\
K_1(A)\xrightarrow{\iota_*}K_1(B),\\
K_1(B)\xrightarrow{d_1}K_0(A).
\end{gathered}
\tag{1.1}
\]

The last arrow is followed by the first. Naturality means compatibility with *-homomorphisms \(v:A\to A'\) satisfying \(v\alpha=\alpha'v\), including nonunital and degenerate maps. Our proof below defines the boundary maps, rather than leaving their normalization implicit.

We use three proved crossed-product inputs, with the same positive dual convention:

- KT-CP-05, Theorem 5.3: a period-one flow has its real crossed product identified with the mapping torus of the positive dual automorphism of its circle crossed product.
- KT-CP-08, Theorem 8.3 and Proposition 8.4: Takai duality, including the generator formulas (8.15) and the double dual action (8.16).
- KT-CP-11, Theorem 11.3 and equations (11.22)–(11.26): the natural Thom isomorphism in its normalization \(\Phi=-T\), where \(T\) is the inverse Wiener–Hopf boundary. At a trivial real action, \(\Phi^0=\beta\) and \(\Phi^1=\theta\), both the positive suspension maps.

Write \(b_A^0=\beta_A:K_0(A)\to K_1(SA)\) and \(b_A^1=\theta_A:K_1(A)\to K_0(SA)\), from [Lessons 10](KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign) and [8](KT-OPK-08.md#2-the-idempotent-loop-of-an-invertible). These typed maps fix the ordinary suspension signs. The mapping-torus extension and both boundaries are [Lesson 17, Theorem 2.1](KT-OPK-17.md#2-both-connecting-maps-with-their-signs).

## 2. The Fourier window identifies the inclusion arrows

Let \(\beta_t\) be the gauge flow on \(B\): it fixes \(A\) and sends \(u\) to \(e^{2\pi it}u\). Its period is one. Put

\[
\begin{gathered}
C=B\rtimes_\beta\mathbb T,\\
D=A\otimes\mathcal K(\ell^2\mathbb Z),\\
\gamma=\alpha\otimes\operatorname{Ad}\lambda_1,\\
(\lambda_1\xi)(n)=\xi(n-1).
\end{gathered}
\tag{2.1}
\]

Takai duality identifies \(C\) with \(D\), carrying its positive dual automorphism to \(\gamma\). Combining it with the period-one theorem gives an isomorphism

\[
\Lambda:B\rtimes_\beta\mathbb R\longrightarrow M_\gamma.
\tag{2.2}
\]

Here the mapping torus satisfies \(H(1)=\gamma(H(0))\), and its quotient is evaluation at 0. Fix the stability corner \(\kappa(a)=a\otimes e_{00}\); compact stability in [Lessons 5, Theorem 4.1](KT-OPK-05.md#4-compact-operator-stabilization) and [6, Corollary 4.2](KT-OPK-06.md#4-realizing-an-invertible-path-at-a-late-stage) makes \(\kappa_*\) an isomorphism in both degrees.

The map \(\iota\) is equivariant from the trivial real action on \(A\) to \(\beta\). Its integrated map is therefore

\[
\iota\rtimes\mathbb R:C_0(\mathbb R,A)
\longrightarrow B\rtimes_\beta\mathbb R,
\tag{2.3}
\]

using the positive Fourier transform \(\widehat g(\xi)=\int g(t)e^{2\pi it\xi}\,dt\).

**Lemma 2.1 (window formula).** For \(F\in C_0(\mathbb R,A)\), write \(H=\Lambda(\iota\rtimes\mathbb R)(F)\). Its diagonal entries are

\[
H_{nn}(s)=\alpha^n(F(s-n)).
\tag{2.4}
\]

If \(e:SA\to C_0(\mathbb R,A)\) extends a function by zero outside \((0,1)\), then

\[
\Lambda(\iota\rtimes\mathbb R)e=j\,S\kappa,
\tag{2.5}
\]

where \(j:SD\to M_\gamma\) is inclusion.

*Proof.* In the final Takai coordinates of KT-CP-08, a coefficient \(a\) acts diagonally by \(\alpha^n(a)\), and the circle group multiplier \(v_t\) acts diagonally by \(e^{-2\pi itn}\). The period-one fiber at \(s\) replaces the real group multiplier by \(e^{2\pi ist}v_t\). Thus the integrated elementary function \(a g(t)\) has diagonal entry

\[
\begin{gathered}
\alpha^n(a)\int g(t)e^{2\pi it(s-n)}\,dt
\\
=\alpha^n(a)\widehat g(s-n).
\end{gathered}
\tag{2.6}
\]

Finite sums of these Fourier functions are dense in \(C_0(\mathbb R,A)\), by the Fourier isomorphism of KT-CP-05, Proposition 5.2. For fixed \(s\), the proposed diagonal entries tend to zero as \(|n|\to\infty\), so they define a compact diagonal matrix over \(A\). Their norm is at most \(\|F\|_\infty\), uniformly in \(s\), since automorphisms are isometric. Density proves (2.4) for all \(F\). The endpoint relation also follows directly: \(\gamma\) shifts index \(n-1\) to \(n\) and applies \(\alpha\), giving \(\alpha^n(F(s+1-n))\).

For \(F=e(f)\) and \(0\leq s\leq1\), only index \(n=0\) can contribute; at the endpoints it too is zero. Thus the family is exactly \(f(s)\otimes e_{00}\), proving (2.5). This is an equality of algebra maps before applying K-theory. \(\square\)

We also need the orientation of the window inclusion. It sends the interval maps \(b_A^i\) to the corresponding positive real-line Bott maps. To check this, choose an increasing homeomorphism \(h:\mathbb R\to(0,1)\), and let \(c(\xi)\) equal 0 below 0, \(\xi\) in \([0,1]\), and 1 above 1. For a based unitary loop \(L\), interpolate its argument by

\[
\begin{gathered}
h_r(\xi)=(1-r)h(\xi)+r c(\xi),\\
0\leq r\leq1.
\end{gathered}
\tag{2.7}
\]

The nonconstant part of \(L(h_r(\xi))\) vanishes at infinity uniformly in \(r\), because both arguments tend uniformly to the respective endpoints there. Uniform continuity of \(L\) makes this a norm-continuous homotopy. It joins the real-line representative \(L\circ h\) to the zero-extended interval representative. The same proof applies to the idempotent loop defining \(\theta\), subtracting its constant scalar projection instead of identity. Relative representatives retain their scalar normalization throughout. This proves the window assertion in both degrees for nonunital as well as unital \(A\).

Define isomorphisms, with indices modulo two,

\[
\begin{gathered}
L_i=\Lambda_*\Phi_\beta^i,\\
L_i:K_i(B)\longrightarrow K_{1-i}(M_\gamma).
\end{gathered}
\tag{2.8}
\]

Thom naturality for \(\iota\), its trivial-action normalization, the window assertion, and (2.5) give the required comparison:

\[
L_i\iota_*=j_*b_D^i\kappa_*.
\tag{2.9}
\]

Thus transporting the suspended-ideal inclusion through the Thom and Takai isomorphisms gives exactly \(\iota_*\). Naturality alone would not identify that ideal inclusion; the explicit window computation supplies the missing step.

## 3. Completing the proof and extracting group extensions

*Proof of Theorem 1.1.* Under stability, \(\gamma_*\) is \(\alpha_*\). Indeed,

\[
\gamma\kappa(a)=\alpha(a)\otimes e_{11}.
\tag{3.1}
\]

The corners \(e_{11}\) and \(e_{00}\) have the same K-map: a unitary interchanging these two coordinates conjugates their embeddings, and a norm-continuous unitary path on that finite two-dimensional block joins this conjugation to identity. It acts trivially on the other coordinates and works in the multiplier algebra for nonunital coefficients. Hence \(\gamma_*\kappa_*=\kappa_*\alpha_*\).

Apply the six-term mapping-torus sequence of Lesson 17 to \(\gamma\). In degree \(i\) its relevant portion, after the positive suspension identification, is

\[
\begin{aligned}
K_i(D)&\xrightarrow{\gamma_*-1}K_i(D)\\
&\xrightarrow{j_*b_D^i}K_{1-i}(M_\gamma)\\
&\xrightarrow{q_*}K_{1-i}(D).
\end{aligned}
\tag{3.2}
\]

Use \(\kappa_*\) on the coefficient groups and \(L_i\) on the middle group. Equation (2.9) identifies its second arrow with \(\iota_*\). Define

\[
d_i=\kappa_*^{-1}q_*L_i.
\tag{3.3}
\]

The transported first arrow is \(\alpha_*-1\). Replacing this endomorphism in each degree by its negative \(1-\alpha_*\) preserves both its kernel and image, so the cyclic sequence with \(\iota_*\) and the specified \(d_i\) remains exact. This gives precisely (1.1), with the same quotient evaluation and Thom normalization in (3.3).

All these maps are natural. An equivariant coefficient map commutes with the period-one integrated formula, the Takai diagonal formulas, the stability corner and evaluation; Thom maps are natural by the exact imported result. These give commuting squares for \(\iota_*\), \(d_i\), and \(1-\alpha_*\). \(\square\)

Formula (3.3) fixes our boundary normalization. Negating a boundary arrow produces another commonly used PV presentation; it does not change the induced inclusion arrows. Replacing the covariance relation by \(u^*au=\alpha(a)\) replaces the generating automorphism by \(\alpha^{-1}\). Also,

\[
1-\alpha_*^{-1}=-\alpha_*^{-1}(1-\alpha_*),
\tag{3.4}
\]

so the inverse-automorphism version has the same kernels and images, but its actual coefficient endomorphism is different.

Exactness gives, for \(i=0,1\),

\[
\begin{gathered}
C_i=K_i(A)/(1-\alpha_{*,i})K_i(A),\\
\begin{aligned}
0&\longrightarrow C_i\xrightarrow{\overline{\iota_*}}K_i(B)\\
&\xrightarrow{d_i}\ker(1-\alpha_{*,1-i})\longrightarrow0.
\end{aligned}
\end{gathered}
\tag{3.5}
\]

The quotient injection follows because \(\ker\iota_*\) is exactly the displayed image. Its image is \(\ker d_i\), and \(d_i\) maps onto the displayed kernel. A free right-hand group admits a section by lifting a basis. Without such a section, the outer groups need not determine the middle group.

If \(\alpha_t\) is a point-norm continuous path of automorphisms, then \(\alpha_t\otimes\operatorname{Ad}\lambda_1\) is a path of automorphisms of \(D\). Lesson 17, Theorem 4.1, makes their mapping tori isomorphic. The isomorphisms \(L_i\) consequently show that the crossed products' K-groups depend, up to isomorphism, only on the automorphism-homotopy class. This assertion does not identify the crossed-product algebras themselves.

## 4. Stable finiteness and Cantor coefficients

**Proposition 4.1.** If \(A\) is nonzero, unital and stably finite, then \(K_1(A\rtimes_\alpha\mathbb Z)\ne0\). In particular, a crossed product of a nonzero unital AF-algebra by \(\mathbb Z\) is never AF.

*Proof.* First \([1_A]\ne0\) in \(K_0(A)\). Otherwise group completion of the projection monoid gives a projection \(p\) such that \(1_A\oplus p\) is stably equivalent to \(p\). After placing them in a common finite matrix algebra, let \(E=P+Q\), where \(P\) is the copy of \(p\) and \(Q\) the nonzero copy of the unit on a disjoint block. A partial isometry \(v\) implementing the equivalence has \(v^*v=E\) and \(vv^*=P<E\). It lies in the \(E\)-corner. Then \(v+(I-E)\) is an isometry in that matrix algebra with range projection \(I-Q<I\), contradicting stable finiteness. Since \(\alpha_*[1_A]=[1_A]\), the kernel of \(1-\alpha_{*,0}\) is nonzero. Exactness makes it the image of \(d_1\), so \(K_1(B)\ne0\). Unital AF-algebras are stably finite by their ordered projection invariant, while their \(K_1\) vanishes by Lesson 16, Proposition 1.1. Thus \(B\) cannot be AF. \(\square\)

Unitality matters. Translation of \(\mathbb Z\) on itself gives \(C_0(\mathbb Z)\rtimes\mathbb Z\cong\mathcal K(\ell^2\mathbb Z)\), an AF-algebra. Apply KT-CP-08, Theorem 8.3, to the trivial circle action on \(\mathbb C\): its first crossed product is \(c_0(\mathbb Z)\), its dual action is translation, and its double crossed product is \(\mathcal K(L^2(\mathbb T))\cong\mathcal K(\ell^2\mathbb Z)\).

**Proposition 4.2 (Cantor systems).** Let \(X\) be the Cantor set, \(\varphi:X\to X\) a homeomorphism, and \(\alpha(f)=f\circ\varphi^{-1}\). Then

\[
\begin{gathered}
K_0(C(X)\rtimes_\alpha\mathbb Z)\\
=C(X,\mathbb Z)/(1-\alpha_*)C(X,\mathbb Z),\\
K_1(C(X)\rtimes_\alpha\mathbb Z)\\
\cong\{h\in C(X,\mathbb Z):h\circ\varphi^{-1}=h\}.
\end{gathered}
\tag{4.1}
\]

If \(\varphi\) is minimal, the latter group is \(\mathbb Z\), generated by \([u]\).

*Proof.* Finite clopen partitions give finite-dimensional subalgebras of \(C(X)\). Choose a refining sequence whose mesh tends to zero. A continuous function is uniformly approximated by a function constant on a sufficiently fine partition, so these subalgebras have dense union. Their \(K_0\) groups are the rank functions on the cells, and refinement repeats each cell's rank on its subcells. Continuity of K-theory identifies their limit with \(C(X,\mathbb Z)\): every continuous integer-valued function has finite image and clopen fibers. Their \(K_1\) groups are zero. The action on rank functions is the stated pullback. Applying (3.5) proves (4.1).

For a minimal homeomorphism, an invariant continuous integer-valued function is constant on every orbit. Each orbit is dense, so continuity makes it constant on \(X\). Thus \(d_1\) identifies \(K_1(B)\) with the constant integers. To check its generator, apply naturality to the equivariant scalar map \(\mathbb C\to C(X)\). Its crossed-product map sends the coordinate unitary \(z\in C(S^1)\) to \(u\). For \(A=\mathbb C\), (1.1) makes \(d_1:K_1(C(S^1))\to K_0(\mathbb C)\) an isomorphism, so it sends \([z]\) to \(s[1]\) for a fixed \(s\in\{1,-1\}\). Therefore \(d_1[u]=s[1_X]\), a generator of the invariant subgroup. It follows that \([u]\) is a generator of \(K_1(B)\). This argument needs no unverified numerical choice for the transported boundary's orientation. \(\square\)

The coinvariant subgroup is unchanged if pullback by \(\varphi\) is used instead of \(\varphi^{-1}\), by (3.4). The formula above states which action occurs in (0.1).

### Positive cutdowns and the simplicity argument

The analytic input in the outer-powers simplicity criterion is the following property of an automorphism \(\eta\): for every nonzero hereditary C*-subalgebra \(H\subseteq A\), every \(c\in A\) and every \(\delta>0\), there is \(b\in H_+\) such that

\[
\|b\|=1,\qquad \|b c\eta(b)\|<\delta.
\tag{4.2}
\]

Here hereditary means that \(0\leq a\leq h\), \(h\in H_+\), implies \(a\in H\). We call (4.2) the positive cutdown property. Theorem 4.8 below proves Kishimoto's outer-automorphism lemma: every outer automorphism of a simple C*-algebra has this property, where inner in the nonunital case means implemented by a unitary of \(M(A)\). Lemma 4.3 and Theorem 4.4 prove its passage to simplicity. The proofs require neither separability nor a unit, nuclearity or an invariant trace.

**Lemma 4.3 (simultaneous cutdowns).** Let \(a\in A_+\), \(a\ne0\), let \(c_1,\ldots,c_m\in A\), and let \(\eta_1,\ldots,\eta_m\) have the positive cutdown property. For \(\varepsilon,\delta>0\), there is \(x\in A_+\), \(\|x\|=1\), with

\[
\begin{gathered}
\|xax\|\geq\|a\|-\varepsilon,\\
\|x c_i\eta_i(x)\|<\delta\quad(1\leq i\leq m).
\end{gathered}
\tag{4.3}
\]

*Proof.* We first justify the hereditary algebras we will use. For \(d\in A_+\), \(\overline{dAd}\) is a C*-subalgebra, since \(dAd\) is closed under multiplication and adjoints. The contractions \(e_k=d(d+1/k)^{-1}\) form an approximate identity there, as \(e_kd\to d\). If \(0\leq y\leq h\) with \(h\) in that algebra, then
\(\|(1-e_k)y^{1/2}\|^2\leq\|(1-e_k)h(1-e_k)\|\to0\).
Hence \(e_kye_k\to y\), and each \(e_kye_k\) lies in \(dAd\); this proves heredity. If \(d\) belongs to an already hereditary algebra \(H\), the inequality \(0\leq dcd\leq\|c\|d^2\) for \(c\geq0\), followed by linear decomposition of arbitrary \(c\), proves \(\overline{dAd}\subseteq H\).

Put \(t=\|a\|\) and replace \(\varepsilon\) by a smaller positive number if necessary so that \(\varepsilon<t\). The element \(d=(a-(t-\varepsilon))_+\) is nonzero, since \(t\) belongs to the spectrum of \(a\). Let \(H_0=\overline{dAd}\). In a faithful representation its support projection \(p\) is the spectral projection of \(a\) for \((t-\varepsilon,t]\). Every \(x\in H_0\) satisfies \(px=x=xp\), by approximation with \(dAd\). Thus, for positive \(x\) of norm one in \(H_0\),

\[
\begin{gathered}
xax\geq(t-\varepsilon)x^2,\\
\|xax\|\geq t-\varepsilon.
\end{gathered}
\tag{4.4}
\]

The support projection is used only to check this inequality; it need not belong to \(A\).

Inductively choose positive norm-one \(b_i\in H_{i-1}\) with
\(\|b_i c_i\eta_i(b_i)\|<\delta/4\), and put
\(H_i=\overline{(b_i-1/2)_+A(b_i-1/2)_+}\).
This is a nonzero hereditary subalgebra of \(H_{i-1}\): the positive part is nonzero because \(1\in\operatorname{sp}(b_i)\), and heredity of \(H_{i-1}\) places its generated hereditary algebra inside it. After the last step choose any positive norm-one \(x\in H_m\). If \(m=0\), choose it in \(H_0\).

Define the continuous function \(h\) on \([0,1]\) by \(h(s)=2\) for \(s\leq1/2\) and \(h(s)=1/s\) for \(s\geq1/2\). Functional calculus in the unitization gives \(\|h(b_i)\|\leq2\). On \(H_i\), multiplication by \(h(b_i)b_i\) is identity on either side. Indeed, its product with \((b_i-1/2)_+\) is that same positive part; density of its two-sided products proves the assertion. As \(x\in H_m\subseteq H_i\),

\[
\begin{aligned}
x c_i\eta_i(x)
&=x h(b_i)\,[b_i c_i\eta_i(b_i)]\\
&\qquad\times\eta_i(h(b_i)x),\\
\|x c_i\eta_i(x)\|
&\leq4\|b_i c_i\eta_i(b_i)\|<\delta.
\end{aligned}
\tag{4.5}
\]

Automorphisms extend to the unitization in this identity. Each estimate uses its own \(b_i\), so no error accumulates through subsequent cutdowns. Equation (4.4) proves the other assertion. \(\square\)

**Theorem 4.4 (the ideal-intersection argument).** Suppose that \(\alpha^n\) has the positive cutdown property for every \(n\in\mathbb Z\setminus\{0\}\). Let \(B=A\rtimes_{\alpha,r}\mathbb Z\), with faithful canonical expectation \(E:B\to A\). Every *-homomorphism \(q:B\to C\) that is injective on \(A\) is injective on \(B\). More precisely, for \(b\in B_+\),

\[
\|E(b)\|\leq\|q(b)\|.
\tag{4.6}
\]

Consequently every nonzero closed two-sided ideal of \(B\) meets \(A\) nontrivially. If \(A\ne0\) is simple, then \(B\) is simple.

*Proof.* Injective C*-homomorphisms are isometric, so \(q|_A\) is isometric. Fix \(b\geq0\) and \(\zeta>0\), and choose a finite Fourier polynomial \(P\) with \(\|b-P\|<\zeta\). Contractivity of \(E\) gives \(\|E(b)-E(P)\|<\zeta\). Replacing its constant coefficient by \(a=E(b)\) produces

\[
\begin{gathered}
S=a+\sum_{n\in F}c_nu^n,\\
F\subset\mathbb Z\setminus\{0\}\text{ finite},\\
\|b-S\|<2\zeta.
\end{gathered}
\tag{4.7}
\]

If \(a=0\), (4.6) is automatic. Otherwise apply Lemma 4.3 to \(a\), \(c_n\) and \(\eta_n=\alpha^n\). The covariance convention gives \(x c_nu^n x=x c_n\alpha^n(x)u^n\). Multiplication by the unitary multiplier \(u^n\) preserves norm, also for nonunital \(A\). Thus

\[
\begin{aligned}
\|q(b)\|
&\geq\|q(xbx)\|\\
&\geq\|q(xSx)\|-2\zeta\\
&\geq\|xax\|-|F|\delta-2\zeta\\
&\geq\|E(b)\|-\varepsilon-|F|\delta-2\zeta.
\end{aligned}
\tag{4.8}
\]

The third inequality uses isometry of \(q\) on \(A\) and contractivity on all of \(B\). First let \(\delta\) and \(\varepsilon\) tend to zero for the fixed polynomial, then let \(\zeta\) tend to zero. This proves (4.6). If \(q(y)=0\), apply (4.6) to \(y^*y\). Faithfulness of \(E\) gives \(y=0\).

Now take \(q\) to be the quotient by an ideal \(J\) with \(J\cap A=0\). The assertion just proved gives \(J=0\). If \(A\) is simple and \(J\ne0\), its intersection with \(A\) is a nonzero ideal of \(A\), hence equals \(A\). To see that \(J=B\) also without a unit, let \((e_\lambda)\) be an approximate identity of \(A\). On every monomial \(c_nu^n\), left multiplication by \(e_\lambda\) converges to identity in norm. Fourier-polynomial density and \(\|e_\lambda\|\leq1\) prove the same on \(B\). Since \(e_\lambda\in A\subseteq J\), every \(b\in B\) is a norm limit of \(e_\lambda b\in J\). Therefore \(J=B\). \(\square\)

### Why an outer automorphism has positive cutdowns

We now prove the analytic implication used above. Three elementary pieces make its mechanism visible: pure-state compressions detect a failed cutdown, the compact dual action has a homogeneous primitive ideal space, and continuous functions on that space give central multipliers.

The precise earlier programme inputs are Kadison transitivity, Theorem 11.1, pure states and irreducible representations, §8, minimal pure-state supports, Lemma 1.1, and the self-adjoint multiplier criterion, (2.6). The latter uses the exact monotone-cone identity, Theorem 4.1. We use normal representation extensions and central ideal supports as in the bidual lesson, Lemmas 2.1 and 4.2. These written programme components apply without separability. Their separate review state does not assert independent certification here.

**Lemma 4.5 (compression to a pure state).** Suppose \(H\subseteq A\) is a nonzero hereditary C*-subalgebra, \(\eta\in\operatorname{Aut}(A)\), \(c\in A\), and \(d>0\) satisfy

\[
\begin{gathered}
\|b c\eta(b)\|\geq d\\
(b\in H_+,\ \|b\|=1).
\end{gathered}
\tag{4.9}
\]

For every pure state \(\varphi\) of \(A\) whose restriction to \(H\) is a state, its minimal bidual support \(p\) satisfies

\[
\|p c\eta^{**}(p)\|\geq d.
\tag{4.10}
\]

*Proof.* Let \(q\) be the strong limit of a positive contractive approximate identity of \(H\), in \(M=A^{**}\). Then \(H^{**}=qMq\). Here is the hereditary-corner justification. For \(h\in H_+\) and \(a\in A_+\), \(0\leq hah\leq\|a\|h^2\), so \(hah\in H\). Linear decomposition and approximation with the positive approximate identity give \(HAH\subseteq H\). Thus \(e_i a e_i\in H\) and \(e_i a e_i\to qaq\) strongly. Weak density of \(A\) in \(M\) then makes the weak closure of \(H\) equal to \(qMq\). The bidual of its inclusion has precisely this range. A pure state of \(H\) has minimal support in \(qMq\), which is also minimal in \(M\); its normal corner state restricts to a pure state of \(A\) with norm-one restriction to \(H\). Such states therefore exist. Conversely the state in the assertion has \(p\leq q\), and its restriction to \(H\) is pure by this same minimal-corner criterion.

Write \(\varphi\) also for its normal extension. Its positive pins are

\[
\mathcal P_\varphi
=\left\{b\in H\ \middle|\ 
\begin{gathered}0\leq b\leq1\\\varphi(b)=1\end{gathered}
\right\}.
\tag{4.11}
\]

This set is nonempty. Positive Kadison transitivity in its irreducible GNS representation gives \(y\in H_+\) with \(y\xi=\xi\). Replacing \(y\) by \(\min(y,1)\), a continuous functional-calculus function vanishing at zero, gives a pin. Put \(p_b=1_{\{1\}}(b)\in qMq\). The support of the state is below \(p_b\). The pin \((b_1+b_2)/2\) has top spectral projection \(p_{b_1}\wedge p_{b_2}\): the kernel of the sum of the two positive operators \(1-b_j\) is their common kernel. Hence these projections decrease on a directed set.

Their infimum is exactly \(p\). To prove this, suppose a state \(\psi\) of \(H\) takes value one on every pin, and fix a pin \(b_0\). Let \(x\in H\) satisfy \(\varphi(x^*x)=0\), and put \(f(t)=t/(1+t)\). The positive contraction

\[
b=b_0^{1/2}(1-f(x^*x))b_0^{1/2}
\tag{4.12}
\]

lies in \(H\) and is a pin: on the GNS vector, \(b_0^{1/2}\xi=\xi\) and \(x\xi=0\). Since \(\psi(b_0)=\psi(b)=1\), and \(\psi\) is supported on the top spectral projection of \(b_0\), their difference gives \(\psi(f(x^*x))=0\). The inequality \(f(x^*x)\geq x^*x/(1+\|x\|^2)\) implies \(\psi(x^*x)=0\). Thus the GNS null left ideal of \(\varphi\) is contained in that of \(\psi\).

For \(a\in H\), norm-controlled Kadison transitivity gives \(t\in H\) with \(t\xi=a\xi\) and \(\|t\|\leq(1+\varepsilon)\|a\xi\|\). Therefore \(a-t\) is null for both states, and Cauchy–Schwarz gives

\[
\begin{aligned}
\psi(a^*a)&=\psi(t^*t)\\
&\leq(1+\varepsilon)^2\varphi(a^*a).
\end{aligned}
\tag{4.13}
\]

Letting \(\varepsilon\downarrow0\) proves \(\psi\leq\varphi\). Both states have norm one, so the positive functional \(\varphi-\psi\) has norm zero, and \(\psi=\varphi\). If \(r=\bigwedge_b p_b\) exceeded \(p\), a normal state supported on \(r-p\), restricted to \(H\), would be a state taking value one on all pins. Its normal extension would then equal \(\varphi\), contradicting its support. This proves \(p_b\downarrow p\).

We must pass the lower bound to these projections without assuming norm convergence of the powers. In \(M_2(A^{\sim})\) put

\[
\begin{gathered}
T=\begin{pmatrix}0&c\\c^*&0\end{pmatrix},\\
D_b=\operatorname{diag}(b,\eta(b)),\\
R_b=\operatorname{diag}(p_b,\eta^{**}(p_b)).
\end{gathered}
\tag{4.14}
\]

Here \(A^{\sim}\) means \(A\) if already unital and its minimal unitization otherwise. Each \(b^n\) has norm one. Thus the off-diagonal self-adjoint operator \(D_b^n T D_b^n\) has norm at least \(d\); its spectrum is symmetric about zero, by conjugation with \(\operatorname{diag}(1,-1)\). Choose a state \(\theta_n\) whose value on this operator is at least \(d-1/n\), and define the positive functional \(\psi_n(X)=\theta_n(D_b^n X D_b^n)\), of norm at most one. A weak* cluster point \(\psi\) has \(\psi(T)\geq d\). Since \(\|D_b^n(1-D_b)\|\to0\), it also satisfies \(\psi((1-D_b)^2)=0\). Its normal extension is supported on \(R_b\). In the nonunital case, the additional scalar summand of \((A^{\sim})^{**}=A^{**}\oplus\mathbb C\) is killed by this same equation, since \(b=0\) there. Consequently \(\|p_b c\eta^{**}(p_b)\|\geq d\).

For each pin choose a normal positive functional of norm at most one, supported on \(R_b\), whose value on \(T\) is at least \(d-\varepsilon\). Direct the pins by decreasing \(p_b\) and let \(\varepsilon\downarrow0\). Restrict the functionals to \(M_2(A^{\sim})\) and take a weak* cluster point. For every fixed pin \(b_0\), the eventual support is below \(R_{b_0}\), so the limit vanishes on \((1-D_{b_0})^2\). Its normal extension is therefore supported on \(\bigwedge_b R_b=\operatorname{diag}(p,\eta^{**}(p))\), and still takes value at least \(d\) on \(T\). Compression of \(T\) to that support proves (4.10). This uses compact nets, not a countable family of pins. \(\square\)

**Lemma 4.6 (compact dual orbits).** Let \(\beta:\mathbb T\to\operatorname{Aut}(C)\) be point-norm continuous, with \(C\ne0\), and suppose \(C\) has no nonzero proper \(\beta\)-invariant closed ideal. For \(P\in\operatorname{Prim}(C)\), its stabilizer \(L=\{t:\beta_t(P)=P\}\) is closed, and the orbit map is a homeomorphism

\[
\begin{gathered}
\mathbb T/L\ \longrightarrow\ \operatorname{Prim}(C),\\
tL\longmapsto\beta_t(P).
\end{gathered}
\tag{4.15}
\]

*Proof.* Recall the hull-kernel topology: the closure of a family \(S\) of primitive ideals consists of the primitive ideals containing \(\bigcap_{Q\in S}Q\). Its open sets are \(U_I=\{Q\mid I\nsubseteq Q\}\), for closed ideals \(I\). These statements follow directly by taking hulls of ideals; ideals are intersections of their containing primitive ideals because irreducible representations separate every quotient. A primitive ideal is prime for finite intersections of ideals. Indeed, in its irreducible quotient representation, a nonzero ideal acts nondegenerately: its essential space is a nonzero invariant subspace. If two such ideals had zero product, one would annihilate the dense essential space of the other. This is impossible. Induction proves the finite assertion.

For a closed neighborhood \(V\) of \(1\in\mathbb T\), define \(J_V=\bigcap_{t\in V}\beta_t(P)\). As \(V\) shrinks, these ideals exhaust a norm-dense part of \(P\). For if \(a\in P_+\), then

\[
\|a+\beta_t(P)\|
\leq\|\beta_{t^{-1}}(a)-a\|.
\tag{4.16}
\]

Given \(\varepsilon>0\), this is less than \(\varepsilon\) near \(1\), so \((a-\varepsilon)_+\in J_V\) for all sufficiently small \(V\). Such cutoffs approximate \(a\).

The ideal \(\bigcap_{t\in\mathbb T}\beta_t(P)\) is invariant and proper, hence zero. A finite cover of the circle by \(t_j V\) gives \(\bigcap_j\beta_{t_j}(J_V)=0\). For any primitive ideal \(Q\), primality therefore gives \(\beta_{t_V}(J_V)\subseteq Q\) for some \(t_V\). Compactness provides a subnet \(t_V\to t_0\) while \(V\) still shrinks. Applying (4.16) to every fixed positive cutoff and using closedness of \(Q\) proves \(\beta_{t_0}(P)\subseteq Q\). Interchanging \(P,Q\) gives \(\beta_s(Q)\subseteq P\) for some \(s\).

If \(\beta_v(Q)\subseteq Q\), all positive powers have the same inclusion. The inverse \(v^{-1}\) is a limit of nonnegative powers of \(v\). For completeness, positive powers have an accumulation point by compactness; quotients of sufficiently close powers give positive powers tending to \(1\), and their preceding powers tend to \(v^{-1}\). If those exponents stay bounded, \(v\) has finite order and the assertion is exact. Norm continuity and closedness of \(Q\) now give \(\beta_{v^{-1}}(Q)\subseteq Q\), hence equality in the original inclusion. Apply this to \(v=t_0s\). The chain \(\beta_{t_0s}(Q)\subseteq\beta_{t_0}(P)\subseteq Q\) becomes a chain with equal endpoints. Therefore \(Q=\beta_{t_0}(P)\). The action is transitive, and an inclusion between two members of this orbit is always equality.

The stabilizer is closed: limits of its elements preserve \(P\) in both directions by norm continuity. The orbit map is continuous because the preimage of \(U_I\) is the union, for \(a\in I\), of the open sets where \(\|\beta_{t^{-1}}(a)+P\|>0\). We verify the inverse topology explicitly. For a subset \(S\subseteq\mathbb T/L\), let \(K\) be the inverse image of its compact closure under the quotient map. Suppose \(\bigcap_{sL\in S}\beta_s(P)\subseteq\beta_t(P)\). Cover \(K\) by finitely many \(s_j V\), with centers in \(K\). The intersection of the ideals \(\beta_{s_j}(J_V)\) is contained in that over \(S\), so primality gives one \(\beta_{s_V}(J_V)\subseteq\beta_t(P)\). A subnet of the centers converges to \(s_0\in K\). The cutoff argument again gives \(\beta_{s_0}(P)\subseteq\beta_t(P)\), hence equality. Thus \(tL\) belongs to the closure of \(S\). Conversely continuity sends that closure into the hull-kernel closure of the orbit image. This proves (4.15), and in particular the primitive ideal space is compact Hausdorff. \(\square\)

**Lemma 4.7 (central coordinates).** If \(X=\operatorname{Prim}(C)\) is compact Hausdorff, every \(f\in C(X)\) has a unique central multiplier \(m_f\) satisfying

\[
\begin{gathered}
\widetilde\pi(m_f)=f(\ker\pi)1\\
\text{for every irreducible }\pi.
\end{gathered}
\tag{4.17}
\]

The map \(f\mapsto m_f\) is a unital *-homomorphism. Here \(\widetilde\pi\) is the nondegenerate extension to \(M(C)\).

*Proof.* This is the compact Hausdorff case of the central-multiplier theorem of Dauns and Hofmann; we give the needed construction. For an open set \(U\subseteq X\), let \(I_U\) be the corresponding ideal and \(z_U\in Z(C^{**})\) its support projection. Its positive approximate identity increases to \(z_U\). Finite unions of open sets correspond to joins of these projections, intersections to meets, and \(z_X=1\). To verify the intersection assertion directly, approximate identities of two ideals have products in their intersection, whose strong limits give the product of the two central supports. Unions follow by taking the norm-closed sum of the ideals. Thus disjoint open sets have orthogonal supports, and two open sets covering \(X\) have support join one.

Take \(0\leq f\leq R\), \(R>0\), and put \(z(t)=z_{\{f>t\}}\). For a uniform mesh \(\Delta=R/n\), define lower and upper sums

\[
\begin{gathered}
h_n=\Delta\sum_{k=1}^{n}z(k\Delta),\\
H_n=\Delta\sum_{k=0}^{n-1}z(k\Delta),\\
0\leq H_n-h_n\leq\Delta1.
\end{gathered}
\tag{4.18}
\]

The last bound telescopes. On dyadic refinements the lower sums increase and the upper sums decrease. Thus they converge in norm to the same central positive element \(h_f\in C^{**}\). Each finite positive sum of ideal supports is a bounded increasing limit from \(C_+\), by taking the product net of their approximate identities. Hence \(h_f\in\mathcal C=\overline{C_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}\).

Apply the same construction to \(R-f\), obtaining \(h_{R-f}\in\mathcal C\). At each threshold \(k\Delta\), the open sets \({f>k\Delta}\) and \({f<k\Delta}\) are disjoint, whereas \({f>k\Delta}\) and \({f<(k+1)\Delta}\) cover \(X\). Summing their commuting support inequalities gives, for the lower sums of \(f\) and \(R-f\),

\[
\begin{gathered}
S_n=h_n(f)+h_n(R-f),\\
(R-2\Delta)1\leq S_n\leq R1.
\end{gathered}
\tag{4.19}
\]

Indeed the upper sums paired at successive thresholds have sum at least \(R1\), and each differs from its lower sum by at most \(\Delta1\); lower sums paired at the identical interior thresholds have sum at most \(R1\). Passing to the limit proves \(h_f+h_{R-f}=R1\). The exact multiplier criterion (2.6) cited above now applies: \(h_f\in\mathcal C\cap(R1-\mathcal C)\subseteq M(C)_{\mathrm{sa}}\). It is central since it was central in the bidual.

For an irreducible representation with kernel \(P\), the normal image of \(z_U\) is zero if \(P\notin U\), and identity if \(P\in U\). In the second case the nonzero represented ideal has essential space the entire representation space. Therefore the scalar lower sums in (4.18) converge to \(f(P)\), proving (4.17) for positive \(f\). Real functions are differences of positive ones, and complex functions are complex linear combinations of real ones. Irreducible representations separate multipliers: if every extension kills \(m\), then every representation kills \(mc\) for \(c\in C\), so \(mc=0\) for all \(c\), and \(m=0\). This proves uniqueness, independence of the decompositions, linearity, preservation of products and adjoints, and \(m_1=1\), by checking each in (4.17). \(\square\)

**Theorem 4.8 (Kishimoto's outer-automorphism cutdown).** An outer automorphism \(\eta\) of a nonzero simple C*-algebra has property (4.2). Innerness here means implementation by a unitary in \(M(A)\), including when \(A\) is nonunital.

*Proof.* Suppose property (4.2) fails, so some \(H,c,d\) satisfy (4.9). Choose a pure state with norm-one restriction to \(H\), as in Lemma 4.5. Let \(p\) be its support and \(z\) its central support in \(A^{**}\). By (4.10), \(pc\eta^{**}(p)\ne0\). Both end projections are minimal. Its polar decomposition is therefore a partial isometry from \(\eta^{**}(p)\) onto \(p\); in fact the two corner squares are positive scalars times their respective projections. Equivalent projections have the same central support, giving \(\eta^{**}(z)=z\).

The factor \(A^{**}z\) is \(B(\mathcal H_\varphi)\), by the pure-state support lemma. The induced normal automorphism of this factor is spatial. To see this without a dimension restriction, choose rank-one matrix units \(e_{ij}\) from an orthonormal basis. Their images are rank-one matrix units with strong diagonal sum one. Choose a unit vector \(\zeta_0\) in the image of \(e_{00}\) and put \(\zeta_i=\eta^{**}(e_{i0})\zeta_0\). These form a complete orthonormal basis. The unitary \(V\) carrying the original basis to them implements the automorphism on matrix units, and then on all operators by normality and weak density of the finite-rank operators. Consequently

\[
V\pi_\varphi(a)V^*=\pi_\varphi(\eta(a)).
\tag{4.20}
\]

Use \(C=A\rtimes_\eta\mathbb Z\), its implementing multiplier \(U\), and its dual circle action \(\beta_t(U)=tU\). This covariant pair defines an irreducible representation \(\rho\) of \(C\); its restriction to \(A\) is \(\pi_\varphi\), and \(\widetilde\rho(U)=V\). It is irreducible because its restriction is. Write \(P=\ker\rho\).

The dual action is simple on ideals. Here are also the full-versus-reduced details used in this argument. The average \(E=\int\beta_t\,dt\) on the full product is faithful: if \(x\geq0\) has average zero, every positive functional applied to the continuous positive orbit function has integral zero, hence has value zero at \(x\). All positive functionals therefore vanish at \(x\), so \(x=0\). Fourier-polynomial density shows that its range, the fixed algebra, is \(A\). The canonical quotient to the reduced product preserves \(A\) and intertwines their averages. Applying faithfulness to \(x^*x\) in its kernel proves that this quotient is injective. If \(J\ne0\) is a dual-invariant ideal, \(E(x^*x)\in J\cap A\) is nonzero for \(x\in J\setminus\{0\}\). Simplicity of \(A\) gives \(A\subseteq J\). Its approximate identity is one for \(C\), as checked on monomials \(aU^n\), so \(J=C\). Lemma 4.6 applies.

We show that the stabilizer of \(P\) is trivial. Put \(F=\bar\pi_\varphi(q)\), for the hereditary support \(q\) in Lemma 4.5. The represented algebra \(\pi_\varphi(H)\), on \(F\mathcal H_\varphi\), is irreducible: its weak closure is \(F B(\mathcal H_\varphi)F\), since \(H^{**}=qA^{**}q\). For a unitary \(w\in H+\mathbb C1\), the state vector \(\pi_\varphi(w)\xi_\varphi\) has minimal support \(wpw^*\leq q\). Lemma 4.5 applies to this pure state too. Kadison's unitary transitivity reaches every unit vector \(\zeta\in F\mathcal H_\varphi\) in this way. For precision about lifting, \(\pi_\varphi|_H\) is faithful because \(A\) is simple. Its unitization therefore identifies with the concrete unitization on \(F\mathcal H_\varphi\); if \(H\) has a unit, the concrete unitary is extended by identity on its complementary corner. The rank-one norm in (4.10) now says

\[
\begin{gathered}
|\langle\pi_\varphi(c)V\zeta,\zeta\rangle|\geq d\\
(\|\zeta\|=1,\ F\zeta=\zeta).
\end{gathered}
\tag{4.21}
\]

The numerical range of \(F\pi_\varphi(c)VF\) is convex. One direct proof compresses to the span of any two vectors. For a two-dimensional compression, the expectations of a matrix on unit vectors are the affine real-linear image of the Bloch sphere in \(\mathbb R^3\): with a unit vector \((a,b)\), its coordinates are \(2\operatorname{Re}(\bar a b)\), \(2\operatorname{Im}(\bar a b)\), and \(|a|^2-|b|^2\). The linear map has target \(\mathbb R^2\) and hence a nonzero kernel. Its image of the sphere equals its image of the closed ball, since each fiber meeting the ball also meets the sphere. That image is convex. Thus the segment between any two numerical values remains a numerical value; the one-dimensional case is immediate. By (4.21), the compact closure of the numerical range avoids the open disk of radius \(d\). A closest point to zero in this closed convex set gives a phase \(\omega\in\mathbb T\) with real part at least \(d\) throughout the numerical range. Therefore, for every \(x\in H\), the following order inequality holds in \(C/P\):

\[
\begin{gathered}
x^*\operatorname{Re}(\omega cU)x\geq d x^*x\\
\text{in }C/P.
\end{gathered}
\tag{4.22}
\]

Indeed its faithful represented image is the sandwich of \(\operatorname{Re}(\omega\pi_\varphi(c)V)\geq dF\) on \(F\mathcal H_\varphi\) by \(\pi_\varphi(x)\). If \(t\ne1\) stabilized \(P\), the quotient automorphisms \(\beta_{t^k}\) would preserve (4.22). Averaging for \(0\leq k<N\) replaces \(\omega\) on the left by \(\omega N^{-1}\sum_{k=0}^{N-1}t^k\to0\), while leaving the right side fixed. Closedness of the positive cone would give \(-d x^*x\geq0\pmod P\). A nonzero \(x\in H\) contradicts faithfulness of \(\rho|_A\). Hence the stabilizer is \(\{1\}\).

Lemma 4.6 identifies \(\operatorname{Prim}(C)\) with the circle, \(t\mapsto\beta_t(P)\). Lemma 4.7 supplies a central unitary multiplier \(Z\) for the continuous function \(f(\beta_t(P))=\bar t\). The action on its scalar values gives

\[
\begin{gathered}
\beta_s(Z)=sZ,\\
W=UZ^*\in U(M(C)),\\
\beta_s(W)=W.
\end{gathered}
\tag{4.23}
\]

For example the value of \(\beta_s(Z)\) at \(\beta_t(P)\) is \(f(\beta_{s^{-1}t}(P))=s\bar t\), proving the first identity by multiplier separation. For \(a\in A\), the four elements \(Wa,aW,W^*a,aW^*\) belong to \(C\) and are fixed, hence belong to \(A\). Thus \(W\) restricts to a unitary multiplier of \(A\). The coefficient approximate identity is an approximate identity of \(C\), so this restriction has the same products and unitary identities. Centrality of \(Z\) finally gives

\[
\begin{gathered}
WaW^*=UaU^*=\eta(a)\\
(a\in A).
\end{gathered}
\tag{4.24}
\]

The automorphism is inner. This proves the contrapositive, and therefore (4.2) for every outer automorphism. Every step allowed arbitrary nets and multiplier unitaries, so the assertion includes nonunital and nonseparable simple algebras. \(\square\)

**Corollary 4.9 (outer powers imply simplicity).** If \(A\ne0\) is simple and \(\alpha^n\) is outer for every nonzero integer \(n\), then \(A\rtimes_\alpha\mathbb Z\) is simple. Apply Theorem 4.8 to those powers and then Theorem 4.4. The faithful gauge argument in the proof also identifies its full and reduced versions.

## 5. Five exercises with complete solutions

**Exercise 18.1 (trivial action).** Check the PV sequence against the coefficient-circle computation, including the inclusion arrows.

*Solution.* For \(\alpha=1\), universality identifies \(B\) with \(C(S^1,A)\): the implementing unitary commutes with \(A\), and finite Laurent sums with coefficients in \(A\) are dense. The tensor norm is unambiguous because the circle function algebra is nuclear, as proved in KT-CP-08, Lemma 8.1. The inclusion \(\iota\) becomes the map of constant functions. Evaluation at the circle basepoint is a *-homomorphic left inverse, so \(\iota_*\) is injective. The two endomorphisms in (1.1) are zero, and exactness gives \(0\to K_i(A)\to K_i(B)\xrightarrow{d_i}K_{1-i}(A)\to0\).

Lesson 12, Theorem 5.1, already identifies the group with \(K_i(A)\oplus K_{1-i}(A)\), with the first coordinate supplied by constants and the second by the suspended ideal. The restriction of \(d_i\) to that second summand is an isomorphism: its kernel is zero by \(\ker d_i=\operatorname{im}\iota_*\), and it is onto because \(d_i\) is onto. Using this isomorphism as the second coordinate makes the PV maps explicitly \(x\mapsto(x,0)\) and \((x,y)\mapsto y\). This checks the exact sequence with the boundary normalization (3.3), without assigning it an unproved positive-loop sign.

**Exercise 18.2 (reflection as an integer action).** For \(A=C(S^1)\) and \(\alpha(f)(z)=f(\overline z)\), compute the crossed product by \(\mathbb Z\), with generators.

*Solution.* Rank is fixed and winding changes sign. Thus \(1-\alpha_*\) is zero on \(K_0(A)=\mathbb Z\) and multiplication by 2 on \(K_1(A)=\mathbb Z\). Formula (3.5) gives

\[
\begin{gathered}
K_0(B)\cong\mathbb Z\,[1_B],\\
\begin{aligned}
0&\longrightarrow\mathbb Z/2\longrightarrow K_1(B)\\
&\xrightarrow{d_1}\mathbb Z\longrightarrow0.
\end{aligned}
\end{gathered}
\tag{5.1}
\]

The torsion generator is \(\iota_*[z]\) and has exact order 2 by the cokernel injection. Scalar naturality as in Proposition 4.2 gives \(d_1[u]=s[1_A]\) with \(s=\pm1\). Hence \([u]\) is primitive in the free quotient and supplies a section after choosing that sign. Every class is uniquely an integral multiple of \([u]\) plus either zero or \(\iota_*[z]\); a relation involving a nonzero multiple of \([u]\) is excluded by applying \(d_1\). Thus \(K_1(B)=\mathbb Z\oplus\mathbb Z/2\). This is the infinite cyclic crossed product of the reflection; the acting group here is not the order-two group.

**Exercise 18.3 (why the unit forces a nonzero group).** Prove the stable-finiteness consequence without assuming cancellation of projection classes or the existence of a trace.

*Solution.* If \([1_A]=0\), equality in the group completion supplies a projection class \([p]\) with \([1_A]+[p]=[p]\) in the stabilized projection monoid. Choose equivalent projections representing \(P+Q\) and \(P\) on disjoint blocks in a common finite matrix algebra. Their implementing partial isometry \(v\) satisfies \(v^*v=P+Q\) and \(vv^*=P\). The cross terms in \((v+I-P-Q)^*(v+I-P-Q)\) vanish because \(v\) lies in the \((P+Q)\)-corner. The product is identity; the reverse product is \(I-Q\). This proper isometry contradicts stable finiteness and proves \([1_A]\ne0\). Automorphisms fix that class, so exactness at \(K_0(A)\) forces a nonzero element in \(K_1(B)\) mapping to it. No cancellation or trace assumption entered the argument. The AF conclusion follows from the zero \(K_1\) of AF-algebras established in Lesson 16.

**Exercise 18.4 (the dyadic odometer is the standard Bunce–Deddens system).** Let \(X=\varprojlim\mathbb Z/2^k\mathbb Z\), let \(\varphi(x)=x+1\), and let \(\alpha(f)=f\circ\varphi^{-1}\). Compute the crossed product and identify its actual connecting maps with Lesson 16.

*Solution.* The locally constant coefficient algebras \(A_n=C(\mathbb Z/n\mathbb Z)\), for \(n=2^k\), are invariant and have dense union in \(C(X)\). Write \(p_j\) for their residue projections. Then \(up_ju^*=p_{j+1}\), indices modulo \(n\). In \(A_n\rtimes\mathbb Z\), define

\[
\begin{gathered}
e_{ij}=u^ip_0u^{-j},\quad0\leq i,j<n,\\
w=u^np_0\in p_0(A_n\rtimes\mathbb Z)p_0.
\end{gathered}
\tag{5.2}
\]

The projections \(p_j\) are orthogonal. Thus \(p_0u^{k-j}p_0\) is zero unless \(k=j\) when \(0\leq j,k<n\). It follows that \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), \(e_{ij}^*=e_{ji}\), and \(\sum e_{ii}=1\). The corner element \(w\) is unitary with corner identity \(p_0\). Gauge automorphisms send it to \(z^n w\); its nonempty spectrum is therefore invariant under all circle rotations and equals the full circle. Functional calculus consequently embeds \(C(S^1)\) faithfully into that corner.

The matrix units extend this to an injective map from \(M_n(C(S^1))\). It is onto because its image contains all \(p_j\) and

\[
u=\sum_{j=0}^{n-2}e_{j+1,j}+w e_{0,n-1}.
\tag{5.3}
\]

Thus the implementing unitary becomes the cyclic matrix \(C_n(z)\) of Lesson 16, with last-to-first entry \(z\). Its determinant is \((-1)^{n-1}z\), of winding 1.

These finite-stage crossed products inject into \(B=C(X)\rtimes\mathbb Z\). Indeed, the map is gauge equivariant and injective on coefficients. If an element is in its kernel, its positive square has zero gauge average in the coefficient algebra; injectivity there and faithfulness of the average force the element to be zero. Finite sums of coefficient monomials from these stages are dense in \(B\).

For a refinement \(N=nm\), coarse \(p_0\) is the sum of fine \(p_{ln}\), \(0\leq l<m\). Reorder the fine indices \(ln+i\) as \((i,l)\). Each coarse matrix unit then acts as \(E_{ij}\otimes I_m\): it moves \(ln+j\) to \(ln+i\) without crossing a block endpoint. The coarse corner unitary \(u^np_0\) moves \(ln\) to \((l+1)n\), with a final wrap contributing the fine circle coordinate. On that corner it is exactly \(C_m(z)\). Thus the connecting map is

\[
\begin{gathered}
E_{ij}z^r\longmapsto E_{ij}\otimes C_m(z)^r,\\
r\in\mathbb Z.
\end{gathered}
\tag{5.4}
\]

Continuity extends this formula from Laurent matrix polynomials to the whole circle algebra. For dyadic stages \(m=2\), these are precisely the cyclic/root embeddings of Lesson 16, Lemma 3.1 and Theorem 3.2. The algebra, not merely its abstract groups, is the standard Bunce–Deddens limit. Consequently

\[
\begin{aligned}
K_0(B)&=\mathbb Z[1/2],\quad[1_B]=1,\\
K_1(B)&=\mathbb Z,\quad [u]\text{ generates}.
\end{aligned}
\tag{5.5}
\]

The first connecting map multiplies minimal rank by 2; the second preserves the winding-one cyclic unitary. This also proves the generator assertion directly. Translation by 1 is minimal on \(X\): every residue cylinder is visited by each integer orbit. Thus the Cantor formula applies as well. The same argument with \(n_k\mid n_{k+1}\) and unbounded \(n_k\) gives the Bunce–Deddens algebra of the corresponding generalized integer.

**Exercise 18.5 (torsion from an AF automorphism).** Use the simple unital AF realization \(A_3\) from Lesson 16, Theorem 5.7 with ordered group \(G=D\oplus D\), \(D=\mathbb Z[1/2]\), positive cone \(\{0\}\cup\{(r,s):r>0\}\), and unit \((1,0)\). Lift the group automorphism \(\sigma(r,s)=(r,-2s)\), and compute the resulting crossed product's groups and stable finiteness.

*Solution.* For the realization, apply Lesson 16, Theorem 5.7 to the one-point simplex and \(\rho(r,s)=r\). Its range \(D\) is dense in \(\mathbb R\), the group \(D\oplus D\) is countable and torsion-free, and \(\rho(1,0)=1\). The theorem proves precisely this strict cone, unit and simple AF realization, including its infinitesimal second summand. This is Blackadar’s example in §7.6. The map \(\sigma\) is an ordered group automorphism: multiplication by \(-2\) is bijective on \(D\), and the positive cone and unit are unchanged. The automorphism-lifting result used in Lesson 16, §1, namely the AF classification lesson's Corollary 8.4, supplies \(\alpha\in\operatorname{Aut}(A_3)\) with \(\alpha_*=\sigma\).

Since \(K_1(A_3)=0\), the PV sequence gives

\[
\begin{gathered}
K_0(B)=G/(0\oplus3D)\\
\cong D\oplus\mathbb Z/3,\\
K_1(B)=\ker(1-\sigma)\\
=D\oplus0\cong D.
\end{gathered}
\tag{5.6}
\]

For completeness, \(D/3D\cong\mathbb Z/3\) by \(a/2^k\mapsto a(2^k)^{-1}\pmod3\). The formula is well-defined under multiplying numerator and denominator by 2, is onto, and has kernel exactly \(3D\). The order-three class of \((0,1)\) survives through the injective coefficient cokernel map.

There is a unique normalized ordered-group state, \((r,s)\mapsto r\). Indeed, a state must take \((r,0)\) to \(r\) for dyadic \(r\). For every integer \(N\), both \((1,0)\pm N(0,s)\) are positive, so positivity bounds \(|N\tau(0,s)|\leq1\); letting \(N\to\infty\) makes the second coordinate zero. The AF trace correspondence of Lesson 13 therefore gives a unique normalized trace on \(A_3\), fixed by \(\alpha\). It is faithful because the algebra is simple.

Let \(E:B\to A_3\) be the faithful gauge average. The state \(\widetilde\tau=\tau E\) is tracial. On monomials \(au^m,bu^n\), both product traces vanish unless \(m+n=0\); in that case invariance and cyclicity give \(\tau(a\alpha^m(b))=\tau(b\alpha^{-m}(a))\). Density proves traciality on \(B\). Faithfulness of \(\tau\) and \(E\) proves faithfulness of \(\widetilde\tau\). Its faithful matrix extensions exclude proper isometries, so \(B\) is stably finite.

The crossed product is also simple by Corollary 4.9, whose outer-to-cutdown and ideal-intersection steps are proved in Theorems 4.8 and 4.4. This is the criterion stated and applied in Blackadar, Exercise 10.11.2(a), and Kishimoto's crossed-product simplicity theorem. Here \(\sigma^n\ne1\) for every nonzero \(n\), since \((-2)^n\ne1\). Inner automorphisms act trivially on K-theory by matrix conjugacy, so every \(\alpha^n\) is outer. Amenability identifies reduced and full products. Thus this example is simple, unital, stably finite and has nonzero torsion in \(K_0\). Its full positive cone in the crossed product has not been inferred from the trace alone.

## Sources and precise imports

- B. Blackadar, *K-Theory for Operator Algebras*, second edition (1998), §§10.1–10.5, especially Theorem 10.2.1 and Propositions 10.3.2, 10.4.1–10.4.3, 10.5.1; Exercises 10.11.1–10.11.2. The sequence and inclusion arrows are proved here from the cited crossed-product prerequisites and the corrected mapping-torus conventions of Lesson 17. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- J. Rosenberg, “Examples and applications of noncommutative geometry and K-theory” (2012), §2.5, printed p. 108. The coefficient-arrow identification left as a check there is established by Lemma 2.1 and equation (2.9).
- H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry* (2024), §11.5, Corollaries 11.5.15–11.5.16. The Cantor groups and implementing-unitary generator are proved in Proposition 4.2; the odometer's actual circle connecting maps are proved in Exercise 18.4.
- The exact imported period-one, Takai and Thom statements are listed in §1. Compact stability, ordinary suspension maps, AF trace correspondence, AF automorphism lifting and the specified simple AF realization are reused with the locators above. Lemmas 4.3 and 4.5–4.7, Theorems 4.4 and 4.8, and Corollary 4.9 prove the full outer-powers simplicity criterion, including arbitrary nonunital and nonseparable simple coefficients. The exact written analytic prerequisites and their required scope are listed before Lemma 4.5.

Blackadar's proof discussion in §10.2 describes alternative routes through Green imprimitivity or the Toeplitz extension, referring the latter to the KK argument in §19.9.2. The completed Fourier-window proof above uses the three exact crossed-product inputs listed in §1.

- G. A. Elliott, *Some Simple C*-Algebras Constructed as Crossed Products with Discrete Outer Automorphism Groups*, Publications of RIMS 16 (1980), 299–311, [original article](https://ems.press/journals/prims/articles/2960), §3. Theorem 4.4 writes out the expectation and quotient-norm argument, with the analytic cutdown hypothesis explicit.
- A. Kishimoto, *Outer automorphisms and reduced crossed products of simple C*-algebras*, Communications in Mathematical Physics 81 (1981), 429–435, [full text](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-81/issue-3/Outer-automorphisms-and-reduced-crossed-products-of-simple-C-algebras/cmp/1103920327.full), Lemmas 1.1 and 3.2 and Theorem 3.1. Theorem 4.8 proves the outer-to-cutdown implication, with the pure-state compression written in Lemma 4.5 and compact dual-orbit and central-multiplier steps proved in Lemmas 4.6–4.7. Lemma 4.3 gives the finite simultaneous refinement.

- A. Kishimoto, *Simple crossed products of C*-algebras by locally compact abelian groups*, Yokohama Mathematical Journal 28 (1980), 69–85, §3, Lemma 3.7. [Original journal article](https://ynu.repo.nii.ac.jp/record/6663/files/YMJ_28_N1-2_1980_069-085.pdf). The compact-orbit mechanism is supplied in full in Lemma 4.6, including its hull-kernel topology; the compact Hausdorff case of the Dauns–Hofmann central-multiplier theorem is constructed in Lemma 4.7.

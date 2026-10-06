# The Connes–Thom isomorphism I: the Wiener–Hopf extension

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A real action changes the parity of K-theory. The useful extension has a coefficient space with one endpoint at infinity: its open part gives compact operators, and evaluation at the endpoint gives the crossed product whose K-theory we want. We construct that extension, calculate its scalar index, and prove a reduction that will make one surjectivity argument sufficient for the entire theorem.

Throughout, \(A\) is any C*-algebra and \(\alpha:\mathbb R\to\operatorname{Aut}(A)\) is point-norm continuous. Use Lebesgue Haar measure and the conventions
\[
 (\tau_s f)(t)=f(t-s),\qquad
 \mathcal F_+g(u)=\int_{\mathbb R}g(s)e^{2\pi ius}\,ds.
 \tag{10.1}
\]
Full and reduced crossed products by \(\mathbb R\) agree by Lesson 4. We use the full construction, so its ideal exactness is available directly from Lesson 1.

## The K-theory tools and the statement

Write \(SA=C_0(\mathbb R,A)\), with an increasing real suspension coordinate. We use the following general K-theory foundations:

- Homotopy invariance, matrix stability and compact-operator stability of \(K_0,K_1\). A rank-one corner \(a\mapsto a\otimes e\) induces the stability isomorphism.
- The natural isomorphisms \(\theta_A:K_1(A)\to K_0(SA)\) and \(\beta_A:K_0(A)\to K_1(SA)\).
- The natural six-term exact sequence of an extension, including split exactness.

The finite-matrix and compact-operator foundations are written programme proofs. For \(K_0\), *The Grothendieck group and \(K_0\) of a unital algebra*, Theorem 4.2, proves homotopy invariance; *Nonunital algebras: unitization, relative classes and half-exactness*, §1, extends it to nonunital algebras and relative scalar kernels. *Matrix stability, stability and continuity of \(K_0\)*, Theorems 1.1 and 4.1, proves matrix and compact-operator stability. For \(K_1\), *Invertibles, unitaries and \(K_1\)*, §3, Theorem 3.1 and Corollary 4.2, proves homotopy invariance and both stability statements. Each applies to every C*-algebra and to the actual rank-one corner. Thus these foundations retain the generality used in the Wiener–Hopf construction.

For the index, suspension, positive Bott and six-term tools we reuse the written prerequisites The index map and the exact sequence at \(K_0\), Proposition 5.1, Suspension, higher K-groups and the long exact sequence, Theorem 2.1, [Bott periodicity, Theorem 4.1], and The six-term exact sequence and the exponential map, Theorems 1.1 and 2.1. The primary reference is [Blackadar 1998]. In particular, \(\beta_A[p]\) is the positive-winding loop \(zp+1-p\). The construction of \(\theta_A[u]\) uses a path \(w\) from \(1\) to \(\operatorname{diag}(u,u^{-1})\) and the class \([w p_n w^{-1}]-[p_n]\), where \(p_n=\operatorname{diag}(1_n,0_n)\).

For an extension \(0\to I\to D\to Q\to0\), denote its two boundaries by
\[
 \delta_1:K_1(Q)\longrightarrow K_0(I),\qquad
 \delta_0:K_0(Q)\longrightarrow K_1(I).
 \tag{10.2}
\]
The index convention is kernel minus cokernel. More precisely, if a unitary lifts to a partial isometry \(V\) in a matrix unitization of \(D\), then
\[
 \delta_1[U]=[1-V^*V]-[1-VV^*].
 \tag{10.3}
\]
This is the prerequisite's Proposition 5.1, also [Blackadar 1998]. The exponential boundary uses \(\exp(2\pi i x)\) for a selfadjoint lift \(x\), by The six-term exact sequence and the exponential map, Theorem 1.1, also Blackadar §9.3.2. With our forward \(\theta\) and positive \(\beta\), that theorem gives the typed comparison
\[
 \delta_0=-\theta_I^{-1}\delta_{1,SE}\beta_Q,
\]
where \(SE\) is the suspended extension. Thus the positive exponential is not obtained by dropping the minus sign in this comparison. General boundaries do not require partial-isometry lifts.

The Connes–Thom theorem will assert that the two boundaries of the extension constructed below are isomorphisms:
\[
 K_i(A\rtimes_\alpha\mathbb R)\cong K_{1-i}(A),
 \qquad i=0,1.
 \tag{10.4}
\]
This lesson proves the construction, the scalar case and the reduction. Lesson 11 proves the universal surjectivity required by that reduction, and records the normalized inverse maps. Thus (10.4) is the theorem being developed; we do not use it in the argument that follows.

## A cone with an equivariant quotient

Let \(Y=\mathbb R\cup\{+\infty\}\), with its usual one-sided compactification. A function in \(C=C_0(Y)\) is continuous on \(\mathbb R\), tends to zero at \(-\infty\), and has a finite limit at \(+\infty\). Set
\[
 \begin{gathered}
 CA=C_0(Y,A),\qquad
 (\gamma_sF)(t)=\alpha_s(F(t-s)),\\
 (\gamma_sF)(+\infty)=\alpha_s(F(+\infty)).
 \end{gathered}
 \tag{10.5}
\]
The tensor identification \(CA=C\otimes A\) is Lemma 8.1. Formula (10.5) defines a point-norm continuous action. To see continuity, first use finite sums of scalar functions times coefficients. Translation is norm continuous on \(C_0(Y)\), and \(\alpha\) is norm continuous on each coefficient. These sums are dense; isometry gives continuity for every \(F\).

Evaluation at \(+\infty\) gives an equivariant exact sequence
\[
 0\longrightarrow SA\longrightarrow CA
 \xrightarrow{\operatorname{ev}_{+\infty}}A\longrightarrow0.
 \tag{10.6}
\]
It is onto: multiply \(a\in A\) by a continuous scalar function vanishing at \(-\infty\) and equal to one near \(+\infty\). The kernel is precisely the functions vanishing at both ends.

The algebra \(CA\) is contractible. The coordinate
\[
 u(t)=\frac{e^t}{1+e^t},\qquad u(+\infty)=1
 \tag{10.7}
\]
identifies it with \(C_0((0,1],A)\). Extend each such function by zero at \(0\). For \(0\le r\le1\), define
\[
 (H_rF)(u)=F(ru).
 \tag{10.8}
\]
Each \(H_r\) is a *-homomorphism, \(H_0=0\), \(H_1=\operatorname{id}\), and uniform continuity on \([0,1]\) gives point-norm continuity in \(r\). Consequently
\[
 K_0(CA)=K_1(CA)=0.
 \tag{10.9}
\]
This is an ordinary algebra homotopy. It does not commute with the action in (10.5), and therefore does not itself give vanishing K-theory of the crossed product.

## Untwisting the open part

**Proposition 10.1.** There is a natural isomorphism
\[
 SA\rtimes_\gamma\mathbb R\cong
 A\otimes\mathcal K(L^2(\mathbb R)).
 \tag{10.10}
\]

**Proof.** Define \((\Phi F)(t)=\alpha_{-t}(F(t))\) on \(SA\). This is an isometric *-isomorphism, with inverse \(F(t)\mapsto\alpha_t(F(t))\), and
\[
 \Phi\gamma_sF(t)
 =\alpha_{s-t}(F(t-s))
 =(\tau_s\Phi F)(t).
 \tag{10.11}
\]
It induces an isomorphism to \(SA\rtimes_{\tau\otimes\operatorname{id}}\mathbb R\). On crossed-product kernels it is
\[
 \widetilde f(s,t)=\alpha_{-t}(f(s,t)).
 \tag{10.12}
\]
For example, the original product is
\[
 (f*g)(s,t)=\int_{\mathbb R}
       f(r,t)\alpha_r(g(s-r,t-r))\,dr.
\]
Applying \(\alpha_{-t}\) gives the untwisted product of \(\widetilde f\) and \(\widetilde g\), since the second coefficient becomes \(\alpha_{-(t-r)}g(s-r,t-r)\). The involution transforms in the same way:
\[
 \widetilde{f^*}(s,t)
       =\widetilde f(-s,t-s)^*.
\]
Both directions preserve full norms because they identify all covariant representations.

Lemma 8.2 moves the inactive \(A\)-factor outside the full crossed product. The translation theorem of Lesson 7 identifies \(C_0(\mathbb R)\rtimes_\tau\mathbb R\) with \(\mathcal K(L^2(\mathbb R))\). Lemma 8.1 identifies the maximal and spatial tensor norms on the resulting compact-operator factor. This proves (10.10).

For a concrete description, the kernel of the image of \(f\) is
\[
 k_f(t,r)=\alpha_{-t}(f(t-r,t)).
 \tag{10.13}
\]
Under a faithful representation of \(A\), this acts on \(L^2(\mathbb R)\otimes H_A\) by integration in \(r\). A separated kernel \(a\,\xi(t)\overline{\eta(r)}\) corresponds to \(a\otimes\theta_{\xi,\eta}\), with the tensor factors written in the order of (10.10). The full-norm assertion comes from the translation theorem, not just from the formal kernel formula. ∎

The untwisting map here is defined on \(SA\). On \(CA\), the function \(t\mapsto\alpha_{-t}(F(t))\) need not have a limit at \(+\infty\); this formula does not untwist the entire Wiener–Hopf algebra.

## The extension and its boundary maps

Put \(W_\alpha=CA\rtimes_\gamma\mathbb R\) and \(B_\alpha=A\rtimes_\alpha\mathbb R\). Full crossed-product exactness applied to (10.6), followed by Proposition 10.1, gives
\[
 0\longrightarrow A\otimes\mathcal K
 \xrightarrow{\iota_\alpha}W_\alpha
 \xrightarrow{q_\alpha}B_\alpha\longrightarrow0.
 \tag{10.14}
\]
This is the **Wiener–Hopf extension**. On a continuous compact group kernel, \(q_\alpha f(s)=f(s,+\infty)\). Compact-operator stability identifies its boundaries with
\[
 \partial_1^\alpha:K_1(B_\alpha)\to K_0(A),\qquad
 \partial_0^\alpha:K_0(B_\alpha)\to K_1(A).
 \tag{10.15}
\]
The two consecutive parts of the cyclic exact sequence are
\[
 \begin{gathered}
 K_0(A)\longrightarrow K_0(W_\alpha)\longrightarrow K_0(B_\alpha)
 \xrightarrow{\partial_0^\alpha}K_1(A),\\
 K_1(A)\longrightarrow K_1(W_\alpha)\longrightarrow K_1(B_\alpha)
 \xrightarrow{\partial_1^\alpha}K_0(A).
 \end{gathered}
 \tag{10.16}
\]

Here the stability corner can be chosen explicitly. If \(h\in L^2(\mathbb R)\) is a unit vector, let \(e_h=\theta_{h,h}\). For a continuous compactly supported \(h\), its image in the ideal is
\[
 \phi_h(a)(s,t)=\alpha_t(a)h(t)\overline{h(t-s)}.
 \tag{10.17}
\]
Formula (10.13) sends this to \(a\otimes e_h\), so it is a *-homomorphism and induces the stability isomorphism onto the ideal's K-theory. For arbitrary \(h\), the same assertion means norm completion: approximate \(h\) in \(L^2\) by continuous compactly supported functions and use continuity of rank-one operators. It is not a claim that the displayed coefficients are always continuous.

The extension is natural even for a degenerate equivariant *-homomorphism \(v:A\to D\). Applying \(v\) pointwise to the continuous kernel algebras gives a morphism of (10.14); on its ideal this is \(v\otimes\operatorname{id}_{\mathcal K}\). The full construction of Lesson 1 makes these maps contractive. Formula (10.12) commutes with them by equivariance. No extension of a degenerate map to a multiplier algebra is needed.

## One surjectivity assertion controls both parities

**Proposition 10.2.** Suppose that \(\partial_1^\beta\) is onto for every C*-algebra \(D\) with every point-norm continuous action \(\beta\) of \(\mathbb R\). Then for every \(A,\alpha\), \(K_*(W_\alpha)=0\), and both maps in (10.15) are isomorphisms.

**Proof.** The hypothesis first gives the implication
\[
 K_1(D\rtimes_\beta\mathbb R)=0
       \ \Longrightarrow\ K_0(D)=0.
 \tag{10.18}
\]
Indeed a surjective map from the zero group has zero target.

Now assume \(K_1(A)=0\), put \(D=A\rtimes_\alpha\mathbb R\), and give \(D\) its dual action. Identify the dual group with \(\mathbb R\) using \(\chi_u(s)=e^{2\pi ius}\). Takai duality from Lesson 8 and stability give
\[
 \begin{aligned}
 K_1(D\rtimes_{\widehat\alpha}\mathbb R)
 &\cong K_1(A\otimes\mathcal K(L^2(\mathbb R)))\\
 &\cong K_1(A)=0.
 \end{aligned}
 \tag{10.19}
\]
Apply (10.18) to this \(D,\widehat\alpha\). It follows that
\[
 K_1(A)=0\ \Longrightarrow\
 K_0(A\rtimes_\alpha\mathbb R)=0.
 \tag{10.20}
\]
Only the ordinary Takai isomorphism is used here; there is no need to remove its surviving double dual action.

Next assume \(K_0(A)=0\). Let \(S\alpha\) act trivially on the suspension coordinate and by \(\alpha\) on coefficients. Bott periodicity gives \(K_1(SA)\cong K_0(A)=0\). Applying (10.20) to \(SA,S\alpha\), and using Lemmas 8.1–8.2, gives
\[
 \begin{aligned}
 0&=K_0(SA\rtimes_{S\alpha}\mathbb R)\\
  &\cong K_0(S(A\rtimes_\alpha\mathbb R))
   \cong K_1(A\rtimes_\alpha\mathbb R).
 \end{aligned}
 \tag{10.21}
\]
Thus \(K_0(A)=0\) implies vanishing of the crossed product's \(K_1\).

Use these two implications with the coefficient algebra \(CA\), whose two groups vanish by (10.9), and with its action \(\gamma\). They give
\[
 K_0(W_\alpha)=K_1(W_\alpha)=0.
 \tag{10.22}
\]
In (10.16), the zero middle groups make both boundaries injective and surjective. ∎

The order of this argument matters: universal surjectivity gives (10.18), Takai gives (10.20), suspension gives (10.21), and only then does the cone give (10.22). Crossing the nonequivariant contraction (10.8) would not prove that last assertion.

## The scalar index, including its sign

Take \(A=\mathbb C\) with the trivial action and write \(W=C_0(Y)\rtimes_\tau\mathbb R\). The extension becomes
\[
 0\longrightarrow\mathcal K(L^2(\mathbb R))
 \longrightarrow W\longrightarrow C_0(\widehat{\mathbb R})
 \longrightarrow0.
 \tag{10.23}
\]
We calculate its boundary without using Proposition 10.2's hypothesis.

Represent \(W\) on \(L^2(\mathbb R)\) by multiplication and left translation:
\[
 (T(f)\xi)(t)=\int_{\mathbb R}f(s,t)\xi(t-s)\,ds.
 \tag{10.24}
\]
This representation is faithful. Its restriction to the open-part ideal is the faithful compact-operator representation of Lesson 7. On a compact group kernel,
\(\lambda_n^*T(f)\lambda_n\) converges strongly, as \(n\to+\infty\), to convolution by \(s\mapsto f(s,+\infty)\). Pointwise coefficient convergence and the integrable compact-support norm bound give this on every vector by dominated convergence. Norm approximation extends it to every element of \(W\). Consequently \(T(b)=0\) implies that the regular representation of the quotient \(q(b)\) is zero. The Fourier theorem of Lesson 6 makes that quotient representation faithful. Hence \(b\) belongs to the open-part ideal, where faithfulness gives \(b=0\).

Let \(\chi\) be the indicator of \((0,\infty)\), and consider the operator
\[
 (F\xi)(t)=\chi(t)\int_0^t e^{-(t-r)/2}\xi(r)\,dr.
 \tag{10.25}
\]
Its kernel is \(e^{-(t-r)/2}\chi(t-r)\chi(r)\). We must check that it belongs to \(T(W)\), since the coefficients suggested by this formula are discontinuous.

Let \(g_\varepsilon\) be zero on \((-\infty,0]\), linear from zero to one on \([0,\varepsilon]\), and one thereafter. The coefficients
\[
 G_\varepsilon(s,t)=e^{-s/2}g_\varepsilon(s)g_\varepsilon(t-s)
 \tag{10.26}
\]
belong to \(L^1(\mathbb R,C_0(Y))\): they vanish for \(s\le0\), have integrable coefficient norms, and are norm continuous in \(s\). They therefore define elements of \(W\).

In their operator kernels, changing \(\chi(s)\) to \(g_\varepsilon(s)\) has convolution norm at most \(\varepsilon\). Changing \(\chi(r)\) to \(g_\varepsilon(r)\) contributes a Hilbert–Schmidt operator whose squared norm is at most
\[
 \int_0^\varepsilon\int_0^\infty e^{-s}\,ds\,dr
       =\varepsilon.
\]
Thus \(\|T(G_\varepsilon)-F\|\le\varepsilon+\sqrt{\varepsilon}\). Faithfulness of \(T\) makes \(G_\varepsilon\) Cauchy in the full norm, proving membership of (10.25) in \(W\). The discontinuous expressions themselves were not treated as elements of \(L^1(\mathbb R,C_0(Y))\).

Set \(h(t)=e^{-t/2}\chi(t)\). It has squared norm one, so \(E=\theta_{h,h}\) is a rank-one projection in the compact ideal. Direct integrations give, for \(t,r>0\),
\[
 \begin{aligned}
 (F^*F)(t,r)&=e^{-|t-r|/2},\\
 (FF^*)(t,r)&=e^{-|t-r|/2}-e^{-(t+r)/2},\\
 (F+F^*)(t,r)&=e^{-|t-r|/2}.
 \end{aligned}
 \tag{10.27}
\]
All these kernels vanish if either variable is negative, apart from the identity operator used next. For the first line integrate over \(v>\max(t,r)\). For the second integrate over \(0<v<\min(t,r)\). The third splits according to \(t>r\) or \(r>t\); the diagonal is a null set. It follows that
\[
 S=1-F,\qquad S^*S=1,\qquad SS^*=1-E.
 \tag{10.28}
\]
These equalities hold in the unitization of \(W\), because \(T\) is faithful.

The quotient of \(G_\varepsilon\) is the Fourier transform of \(e^{-s/2}g_\varepsilon(s)\). These scalar kernels converge in \(L^1\), giving
\[
 q(F)(u)=\frac1{1/2-2\pi iu},\qquad
 q(S)(u)=v(u)=\frac{u-ic}{u+ic},\quad c=\frac1{4\pi}.
 \tag{10.29}
\]
The unitary \(v\) tends to one at both ends. With the increasing coordinate \(u\), its winding is
\[
 \frac1{2\pi i}\int_{\mathbb R}v'(u)v(u)^{-1}\,du
 =\frac1{2\pi i}\int_{\mathbb R}
       \frac{2ic}{u^2+c^2}\,du=1.
 \tag{10.30}
\]
Thus \([v]\) is the positive generator \(\beta_{\mathbb C}[1]\) of \(K_1(C_0(\mathbb R))\), with the compactified real coordinate used as the loop coordinate.

Formula (10.3) applied to the isometry \(S\) now gives
\[
 \partial_1[v]=-[E]=-[1]\in K_0(\mathbb C).
 \tag{10.31}
\]
The index boundary is an isomorphism, and its inverse sends \([1]\) to \(-[v]\). The other boundary is the isomorphism between zero groups, since \(K_0(C_0(\mathbb R))=K_1(\mathbb C)=0\). Exactness of (10.23) also proves \(K_0(W)=K_1(W)=0\).

This agrees with the Toeplitz sign convention. An isometry with a one-dimensional cokernel has index \(-1\); the unilateral shift gives the same calculation for the circle symbol \(z\). Here the symbol is the positive Cayley loop \(v\), and its winding was computed rather than inferred from a Fourier convention.

## Why the continuous shift is the universal pure isometry

The shift used in the scalar Wiener–Hopf calculation is part of a general classification theorem. This section adapts S. Sundar's *Notes on C*-algebras* (2025), the section on Cooper's theorem, supplied as editable TeX under CC0. The adaptation gives the dilation details, uses the translation imprimitivity proof of Lesson 7, and includes arbitrary Hilbert-space multiplicities.

A strongly continuous semigroup of isometries satisfies \(V_0=1\), \(V_sV_t=V_{s+t}\), and \(V_t^*V_t=1\), for \(s,t\geq0\). It is **pure** when \(V_t^*\xi\to0\) as \(t\to\infty\) for every vector.

**Theorem 10C.1 (Cooper and the continuous Wold decomposition).** Every such semigroup on an arbitrary Hilbert space has a reducing decomposition
\[
\mathcal H=\mathcal H_\infty^\perp\oplus\mathcal H_\infty,\qquad
\mathcal H_\infty=\bigcap_{t\geq0}V_t\mathcal H,
\]
and is unitarily equivalent to
\[
V_t=(S_t\otimes1_{\mathcal L})\oplus U_t,\qquad
(S_t\xi)(x)=
\begin{cases}\xi(x-t)&x\geq t,\\0&0<x<t.\end{cases}
\tag{10C.1}
\]
Here \(U\) extends to a strongly continuous unitary representation of \(\mathbb R\), and the shift multiplicity \(\dim\mathcal L\) can be any Hilbert-space cardinal.

**Proof.** The range projections \(P_t=V_tV_t^*\) decrease with \(t\). The space \(\mathcal H_\infty\) reduces \(V_t\), and \(V_t\mathcal H_\infty=\mathcal H_\infty\). Indeed, if \(\xi\) belongs to every range, then \(V_t^*\xi\) does too, since \(\xi\in V_{s+t}\mathcal H\) for every \(s\); conversely \(V_t\xi\) is in every range by splitting into \(s\leq t\) and \(s>t\). Thus the restriction there is unitary. Its inverse supplies negative times. On the orthogonal complement the intersection of the decreasing ranges is zero. The union of their orthogonal complements is dense there, and \(P_t\xi=0\) eventually on that union. Hence \(P_t\to0\) strongly there; \(\|V_t^*\xi\|=\|P_t\xi\|\) proves purity. It remains to classify a pure semigroup.

First construct its minimal unitary dilation. On pairs \((\xi,s)\), \(s\geq0\), declare \((\xi,s)\sim(\eta,t)\) when \(V_t\xi=V_s\eta\). Cancellation by an isometry proves transitivity. Use
\[
\begin{aligned}
[\xi,s]+[\eta,t]&=[V_t\xi+V_s\eta,s+t],\\
\lambda[\xi,s]&=[\lambda\xi,s],\\
\langle[\xi,s],[\eta,t]\rangle&=\langle V_t\xi,V_s\eta\rangle.
\end{aligned}
\tag{10C.2}
\]
These formulas are independent of representatives: move any finite collection of pairs to one common time \(r\geq s,t\), replacing \([\xi,s]\) by \([V_{r-s}\xi,r]\), and use preservation of inner products by \(V_r\). Completing gives \(\mathcal K\), containing \(\mathcal H\) by \(\xi\mapsto[\xi,0]\). Define \(W_a[\xi,s]=[V_a\xi,s]\) for \(a\geq0\). This is isometric and onto, because
\[
W_a[\xi,s+a]=[V_a\xi,s+a]=[\xi,s].
\]
Extend by its inverse to \(a<0\). The semigroup law holds on pairs. Strong continuity follows from
\(\|W_a[\xi,s]-W_b[\xi,s]\|=\|V_a\xi-V_b\xi\|\) for \(a,b\geq0\), followed by inversion and translation. Moreover \(\bigcup_{s\geq0}W_{-s}\mathcal H\) is the dense pair space. In any other minimal dilation the correspondence \(W_{-s}\xi\mapsto W'_{-s}\xi\) preserves inner products, as is seen by translating both vectors to a common nonnegative time. It therefore extends uniquely to an intertwining unitary.

Let \(E_t\) be the projection onto \(W_t\mathcal H\), now for all real \(t\). Then
\[
E_sE_t=E_{\max(s,t)},\qquad
W_aE_tW_a^*=E_{a+t}.
\tag{10C.3}
\]
The family is strongly continuous. Minimality gives \(E_t\to1\) as \(t\to-\infty\). Purity gives \(E_t\to0\) as \(t\to+\infty\): on a dense vector \(W_{-s}\xi\), with \(s\geq0,\xi\in\mathcal H\),
\[
\|E_tW_{-s}\xi\|=\|E_0W_{-(t+s)}\xi\|
 =\|V_{t+s}^*\xi\|\longrightarrow0
\]
for \(t+s\geq0\).

The commuting projections define a position algebra. For \(f\in C_c(\mathbb R)\), set
\[
F_f=\int f(t)E_t\,dt,\qquad
\widetilde f(x)=\int_{-\infty}^{x}f(t)\,dt,
\quad x\in(-\infty,\infty].
\tag{10C.4}
\]
The first integral is a strong operator integral, bounded by \(\|f\|_1\). Let \(D\) be the C*-algebra generated by these operators. For a nonzero character \(\chi\) of \(D\), the \(L^1\)-bounded functional \(f\mapsto\chi(F_f)\) is integration against some \(\varphi\in L^\infty(\mathbb R)\). There is a bounded interval \((a,b)\) and a \(g\) supported in it with \(\chi(F_g)=1\). This follows by subdividing a compactly supported test function on which the character is nonzero and then rescaling a nonzero summand. For \(f\) supported to the left of \(a\), (10C.3) gives
\[
F_fF_g=\left(\int f\right)F_g.
\]
Hence \(\varphi=1\) almost everywhere to the left of \(a\). Set \(x=\sup\{c:\varphi=1\text{ almost everywhere on }(-\infty,c)\}\). This set is nonempty. If \(\varphi\) is nonzero on a positive-measure subset to the right of a finite \(x\), choose a normalized test \(g\) in a bounded interval there and repeat the argument. It would make \(\varphi=1\) to the left of a number larger than \(x\), a contradiction. Therefore
\[
\chi(F_f)=\widetilde f(x),\qquad x\in(-\infty,\infty].
\tag{10C.5}
\]
The endpoint is unique.

The functions \(\widetilde f\) generate \(C_0((-\infty,\infty])\): they separate points, vanish at the missing left endpoint, and vanish simultaneously nowhere. Stone–Weierstrass applies. The map \(T:\widehat D\to(-\infty,\infty]\) taking \(\chi\) to \(x\) is continuous by (10C.5). It is proper as well. For a compact set of endpoints bounded below by \(a\), choose \(f\geq0\), of integral one, supported to the left of \(a\). Its inverse image lies in the compact set \(\{\chi:|\chi(F_f)|\geq1/2\}\), and is closed. Gelfand theory consequently gives a homomorphism
\[
\pi:C_0((-\infty,\infty])\to D,\qquad
\pi(\widetilde f)=F_f.
\tag{10C.6}
\]
Changing variables in (10C.4) and using (10C.3) proves covariance
\(W_a\pi(h)W_a^*=\pi(h(\,\cdot-a))\).

The restriction of \(\pi\) to \(C_0(\mathbb R)\) is nondegenerate. If a vector \(\eta\) is orthogonal to \(\pi(C_0(\mathbb R))\mathcal K\), then for every \(\xi\) the functional
\(f\mapsto\int f(t)\langle E_t\xi,\eta\rangle\,dt\)
vanishes whenever \(\int f=0\), because then \(\widetilde f\in C_c(\mathbb R)\). It is therefore a scalar multiple of integration: subtract \((\int f)g\) for one fixed integral-one test \(g\). Strong continuity says the function \(\langle E_t\xi,\eta\rangle\) is constant. Its limit at \(+\infty\) is zero, so it is zero everywhere; its limit at \(-\infty\) gives \(\langle\xi,\eta\rangle=0\). Thus \(\eta=0\).

Finally
\[
\overline{\pi(C_c((0,\infty)))\mathcal K}=\mathcal H.
\tag{10C.7}
\]
For \(h\in C_c^\infty((0,\infty))\), (10C.4) gives \(\pi(h)=\int h'(t)E_t\,dt\). Since \(E_0E_t=E_t\) for \(t>0\), its range is in \(\mathcal H\). If \(\eta\in\mathcal H\) is orthogonal to all such ranges, the same zero-integral test argument makes \(\langle E_t\xi,\eta\rangle\) constant on \((0,\infty)\). The limit at \(+\infty\) makes the constant zero, and continuity at zero gives \(\eta=0\). Smooth-function density proves (10C.7).

Apply Lesson 7's translation imprimitivity theorem to the nondegenerate covariant pair \(\pi|_{C_0(\mathbb R)},W\). Its crossed product is \(\mathcal K(L^2(\mathbb R))\). Every nondegenerate representation of that compact algebra is its defining representation tensored with an identity on a Hilbert space \(\mathcal L\): choosing matrix units, their range spaces are mutually unitarily identified, and their orthogonal sum is the whole representation space. This argument allows arbitrary multiplicity. We obtain a unitary sending \(\pi(h),W_a\) to \(M_h\otimes1,\lambda_a\otimes1\). Equation (10C.7) sends the original space precisely to \(L^2((0,\infty))\otimes\mathcal L\). Restricting \(\lambda_t\otimes1\), for \(t\geq0\), gives (10C.1). Combining with the initial reducing decomposition proves the theorem. ∎

The theorem explains why half-line shifts appear in the Wiener–Hopf boundary. A unitary component has no lost range; the pure component is exactly the translation representation restricted to the positive-position subspace. The theorem concerns all strongly continuous isometric semigroups, rather than just the scalar shift used in the index computation.

## Exercises with complete solutions

**Exercise 1 (basic).** Prove that \(CA\) is contractible. Does this immediately make \(CA\rtimes_\gamma\mathbb R\) contractible?

**Solution.** Use the coordinate (10.7) and the maps \(H_rF(u)=F(ru)\). Pointwise operations make each a *-homomorphism, and uniform continuity on the closed interval gives
\(\|H_rF-H_{r'}F\|\to0\) as \(r\to r'\). At \(r=0\) the function is zero, and at \(r=1\) it is \(F\). This proves contractibility and (10.9). The maps do not in general intertwine \(\gamma\), so they do not supply crossed-product homomorphisms for a contraction. Vanishing of crossed-product K-theory will instead follow from universal index surjectivity and Proposition 10.2.

**Exercise 2 (intermediate).** Verify the untwisting isomorphism, including convolution and involution, and identify a rank-one coefficient corner.

**Solution.** Write \(f(s,t)\) for the two-variable kernel. The transformed product is
\[
 \begin{aligned}
 \alpha_{-t}((f*g)(s,t))
 &=\int\alpha_{-t}(f(r,t))
         \alpha_{r-t}(g(s-r,t-r))\,dr\\
 &=(\widetilde f*\widetilde g)(s,t).
 \end{aligned}
\]
For the involution, \(f^*(s,t)=\alpha_s(f(-s,t-s)^*)\), so
\(\alpha_{-t}(f^*(s,t))=\alpha_{s-t}(f(-s,t-s)^*)=\widetilde f(-s,t-s)^*\).
The inverse uses \(\alpha_t\), and covariant representations in both directions give equality of full norms. Formula (10.13) sends \(\alpha_t(a)h(t)\overline{h(t-s)}\) to \(a h(t)\overline{h(r)}\). Therefore (10.17) is exactly \(a\otimes\theta_{h,h}\), extended by norm completion for an arbitrary \(L^2\) unit vector.

**Exercise 3 (intermediate).** Compute the scalar index boundary on the positive generator and compare it with the Toeplitz boundary.

**Solution.** The continuous approximants (10.26) put \(F\) in \(W\). The two integral products in (10.27) make \(S=1-F\) an isometry with cokernel projection \(E=\theta_{h,h}\). The positive Fourier transform gives the Cayley symbol (10.29), and (10.30) proves winding \(+1\). Hence the boundary sends the positive generator to \(-[E]\), by (10.3). For the Toeplitz extension the unilateral shift lifts the positive circle generator and has the same defects \(1-S^*S=0\), \(1-SS^*=E\). Both boundaries are minus winding under these normalizations.

**Exercise 4 (advanced).** Assume universal surjectivity of the Wiener–Hopf index maps. Give every K-group identification needed to conclude that both boundary maps are isomorphisms.

**Solution.** Surjectivity implies (10.18). If \(K_1(A)=0\), Takai and stability identify the double crossed product's \(K_1\) with \(K_1(A)=0\); (10.18) then gives \(K_0(A\rtimes\mathbb R)=0\). If \(K_0(A)=0\), the Bott map gives \(K_1(SA)=0\). The preceding implication gives \(K_0(SA\rtimes\mathbb R)=0\). Moving the inactive suspension factor outside the product identifies this with \(K_0(S(A\rtimes\mathbb R))\), and \(\theta\) identifies the latter with \(K_1(A\rtimes\mathbb R)\). Since \(K_0(CA)=K_1(CA)=0\), these implications applied to \(CA,\gamma\) give both groups of \(W_\alpha\) zero. In each half of (10.16), exactness then makes the outgoing boundary injective and the following boundary surjective. Thus both boundaries are bijective.

**Exercise 5 (intermediate).** On \(L^2(\mathbb R)\), let \(\lambda_t\xi(x)=\xi(x-t)\). Prove that restricting \(\lambda_t\), \(t\geq0\), to \(L^2((b,\infty))\) gives a pure isometric semigroup with minimal dilation \(\lambda\). Compare it with \(\lambda_t\) acting on the whole line.

**Solution.** Translation by \(t\geq0\) maps functions supported in \((b,\infty)\) to functions supported in \((b+t,\infty)\), preserving their \(L^2\)-norm. The range projections are multiplication by \(1_{(b+t,\infty)}\); dominated convergence makes them converge strongly to zero. Hence the restriction is pure. The union of the spaces translated by \(-s\), \(s\geq0\), contains every compactly supported \(L^2\) function, so it is dense in the whole-line space and proves minimality. Translating the endpoint \(b\) to zero identifies the restriction with \(S_t\). On the whole line every \(\lambda_t\) is unitary, its range intersection is the whole Hilbert space, and its pure part is zero. ∎

## What this lesson does not prove

The general K-theory foundations listed above are prerequisites. The index convention, forward \(\theta\), positive Bott isomorphism, positive exponential and natural six-term sequence are reused from the four exact operator K-theory locators given there; the broader stable projection and unitary foundations, homotopy invariance and stability use the exact written programme proofs identified at the start. The Blackadar references remain mathematical credit. Full crossed-product exactness, amenability of \(\mathbb R\), the translation imprimitivity theorem, the tensor identities and Takai duality are proved in Lessons 1, 4, 7 and 8.

The continuous Wold and Cooper classification is proved here by the credited Sundar adaptation and the exact translation imprimitivity theorem of Lesson 7.

Universal index surjectivity for arbitrary \(A,\alpha\) is the remaining step of the Connes–Thom theorem; Lesson 11 proves it. The scalar calculation fixes the inverse index map on \(K_0(\mathbb C)\). It does not on its own compare both parities with every suspension convention, or compare the map with a geometric cotangent Thom class.

## References

The index map and the exact sequence at \(K_0\) K-theory for operator algebras, Lesson 7, Proposition 5.1, the kernel-minus-cokernel boundary formula.

Suspension, higher K-groups and the long exact sequence K-theory for operator algebras, Lesson 8, Theorem 2.1, the forward doubled-path \(\theta\).

[Bott periodicity] K-theory for operator algebras, Lesson 10, Theorem 4.1, the positive loop isomorphism with Toeplitz boundary \(\partial\beta=-1\).

The six-term exact sequence and the exponential map K-theory for operator algebras, Lesson 11, Theorems 1.1 and 2.1, the positive exponential and exact natural cycle, including its suspension sign.

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition. General K-theory: §§5.1–5.5, 8.1–8.3 and 9.1–9.3. Wiener–Hopf construction and reduction: §10.9, Lemmas 10.9.1–10.9.2, pp. 79–80; scalar operators: Lemmas 10.9.3–10.9.4, pp. 80–81. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Rosenberg 2012] Jonathan Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, 2012, §2.4, pp. 106–107. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf). An overview of the Connes–Thom theorem and its proof methods.

[Schulz-Baldes–Stoiber 2022] Hermann Schulz-Baldes and Tom Stoiber, *Harmonic Analysis in Operator Algebras and its Applications to Index Theory and Topological Solid State Systems*, chapter *Duality for Toeplitz extensions*. [Preprint](https://arxiv.org/abs/2206.07781). The smooth real-action extension gives a related index construction; we use the C*-extension (10.14).

[Sundar 2025] S. Sundar, [*Notes on C*-algebras*](https://arxiv.org/abs/2505.17456v1), 2025, the treatment of Cooper’s theorem. The credited section above adapts the author’s [supplied editable TeX](https://arxiv.org/src/2505.17456v1), dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).


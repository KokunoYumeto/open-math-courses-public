# Stability of finite factors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves strong Kadison–Kastler stability for finite factors on separable Hilbert spaces, with a modulus that does not depend on the factors (Theorem 2.1). The proof has two halves. In common tracial position, the boundary of the earlier lessons turns approximate multiplicativity of nearby unitaries into an exact isomorphism close to the identity in operator norm (Proposition 1.1). The cocycle correction, the averaged intertwiner, the diagonal comparison and double ergodicity are used in turn, and Herstein's lemma fixes the orientation. Back in the original representation, the uniform commutator estimate upgrades the operator norm bound to a completely bounded one, and close representations are conjugate by a unitary near the identity [OpenAI-289, Section 5].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4, 1.5 and 3.3); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Theorem 3.1, Christensen's theorem); [Boundary means and measurable cocycles](boundary-means-and-measurable-cocycles.md) (Lemmas 2.1, 3.1 and 4.1); [Double ergodicity and diagonal comparison](double-ergodicity-and-diagonal-comparison.md) (Lemmas 1.1 and 2.1); [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md) (Lemmas 1.1 and 2.1, Corollary 2.2); [Common tracial position and Jordan maps](common-tracial-position-and-jordan-maps.md) (Proposition 1.2, Lemmas 2.1, 2.2 and 3.1); [Theorem 3.1 of The uniform commutator estimate](course:kadisons-similarity-problem/the-uniform-commutator-estimate#3-removing-separability) (for every von Neumann algebra \(P\subseteq B(K)\) and \(Y\in B(K)\), \(\|\operatorname{ad}_Y|_P\|_{\rm cb}\le C\,\|\operatorname{ad}_Y|_P\|\) with an absolute constant \(C<6308\)); and [Corollary 11.4](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras#OA-FND-WA-18) (\(*\)-isomorphisms of von Neumann algebras are normal).

## 1. An isomorphism in common tracial position

**Proposition 1.1.** Let \(M,N\subseteq B(K)\) be II\(_1\) factors on a separable Hilbert space in common standard tracial position with the vector \(\Omega\). Suppose that \(M\cap N\) contains a hyperfinite subfactor \(R=(\bigcup_jQ_j)''\) as in Lemma 2.1 of [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md), irreducible in \(M\), and that \(J_MrJ_M=J_NrJ_N\) for every \(r\in R\). If \(d(M,N)<b<1/1564\), there is a normal \(*\)-isomorphism \(\vartheta:M\to N\) with
\[
\sup_{x\in M_1}\|\vartheta(x)-x\|\le252\,b .
\]

**Proof.** *Nearby unitaries.* The unitary group of \(M\) is separable for the strong topology, because \(K\) is separable; let \(G\subseteq\mathcal U(M)\) be a countable strongly dense subgroup. For \(g\in G\) choose \(y\in N_1\) with \(\|y-g\|<b\). Then \(1-b\le|y|\le1\), so \(y\) is invertible and its polar part \(v_g\in\mathcal U(N)\) satisfies \(\|v_g-y\|=\|1-|y|\|\le b\) and \(\|v_g-g\|\le2b\). Hence
\[
\begin{aligned}
&\|v_gv_h-v_{gh}\|\le\|v_g-g\|+\|v_h\\
&\qquad -h\|+\|gh-v_{gh}\|\le6b .
\end{aligned}
\]

*The boundary cocycle.* Let \((D,\nu)\) be the boundary of \(G\) from Lemma 2.1 of [Boundary means and measurable cocycles](boundary-means-and-measurable-cocycles.md). Regarded as constant fields, the \(v_g\) have defect at most \(6b\le1/64\). Lemma 3.1 there gives an exact cocycle \(W_g\in L^\infty(D,\mathcal U(N))\) with \(\|W_g-v_g\|_\infty\le12b\), so
\[
\begin{gathered}
W_g(x)W_h(g^{-1}x)=W_{gh}(x),\\
\|W_g-g\|_\infty\le14b .\quad(1.1)
\end{gathered}
\]

*Comparison with the left and right actions.* On \(D^2\), with the separate action of \(G\times G\), put
\[
\begin{gathered}
\begin{aligned}
\Sigma_{g,h}(x,y)&=W_g(x)\,J_NW_h(y)J_N,
\end{aligned}\\
U_{g,h}=g\,J_MhJ_M .
\end{gathered}
\]
Since \(J_MhJ_M\in M'\), \(U\) is a unitary representation of \(G\times G\); since \(J_NW_h(y)J_N\in N'\) commutes with \(W_{g'}(g^{-1}x)\in N\), \(\Sigma\) is an exact cocycle. By (1.1) and Lemma 2.2 of [Common tracial position and Jordan maps](common-tracial-position-and-jordan-maps.md),
\[
\begin{aligned}
&\|\Sigma_{g,h}-U_{g,h}\|_\infty\\
&\quad\le\|W_g-g\|_\infty+\|W_h-h\|_\infty\\
&\qquad+2\|J_N-J_M\|\\
&\quad\le28b+1536b=1564b<1 .
\end{aligned}
\]
Lemma 4.1 of the boundary lesson, for \((G\times G,D\times D)\), gives a measurable \(L:D^2\to\mathcal U(K)\) with \(\|L-I\|_\infty\le3128b\) and
\[
\begin{gathered}
L(x,y)\,U_{g,h}\\
=\Sigma_{g,h}(x,y)\,L(g^{-1}x,h^{-1}y).\quad(1.2)
\end{gathered}
\]

*Comparison along the diagonal.* By (1.1), \(\|W_g(x)W_g(y)^*-I\|\le28b<1\). Lemma 1.1 of [Double ergodicity and diagonal comparison](double-ergodicity-and-diagonal-comparison.md), for \(A=N\) in standard tracial position, gives a measurable \(a:D^2\to\mathcal U(N)\) with \(\|a-I\|_\infty\le56b\) and
\[
\begin{gathered}
a(x,y)\\
=W_g(x)\,a(g^{-1}x,g^{-1}y)\,W_g(y)^* .\quad(1.3)
\end{gathered}
\]

*A constant vector.* Put \(f(x,y)=L(x,y)^*a(x,y)\Omega\), a bounded measurable map \(D^2\to K\). Right multiplication by \(W_g(y)^*\) is \(J_NW_g(y)J_N\), so (1.3) gives \(a(x,y)\Omega=\Sigma_{g,g}(x,y)\,a(g^{-1}x,g^{-1}y)\Omega\), and (1.2) with \(h=g\) turns this into
\[
f(x,y)=U_{g,g}\,f(g^{-1}x,g^{-1}y).
\]
By Lemma 2.1 of the double ergodicity lesson, \(f\) is almost everywhere a constant vector fixed by every \(U_{g,g}=gJ_MgJ_M\). The vectors fixed by these unitaries are the multiples of \(\Omega\). Indeed, invariance extends from \(G\) to all of \(\mathcal U(M)\) by strong density, since \(u\mapsto uJ_MuJ_M\) is strongly continuous on unitaries. Averaging \(uJ_MuJ_M\) over the Haar measure of \(\mathcal U(Q_j)\) sends \(x\Omega\) to \(E_j(x)\Omega\), and by Corollary 2.2 of the hyperfinite lesson these averages converge strongly to the projection onto \(\mathbb C\Omega\). Hence
\[
\begin{gathered}
L(x,y)^*a(x,y)\Omega=\lambda\Omega,\\
|\lambda|=1,\\
|\lambda-1|\le3184b,\quad(1.4)
\end{gathered}
\]
for almost every \((x,y)\).

*A unitary on the trace Hilbert space.* Choose a point \((x,y)\) at which (1.2), (1.3) and (1.4) hold, together with their versions at all translates by \(G\times G\); such points form a conull set, since \(G\) is countable and the action nonsingular. Put
\[
S_0=\lambda\,a(x,y)^*L(x,y),
\]
a unitary of \(K\). By (1.4), \(L(x,y)\Omega=\bar\lambda a(x,y)\Omega\), so \(S_0\Omega=\Omega\). For \(g\in G\), (1.2) with \(h=1\) reads \(L(x,y)g=W_g(x)L(g^{-1}x,y)\), and (1.4) at \((g^{-1}x,y)\) gives \(L(g^{-1}x,y)\Omega=\bar\lambda a(g^{-1}x,y)\Omega\). Therefore
\[
\begin{gathered}
S_0g\Omega=b_g\Omega,\\
\begin{aligned}
b_g&=a(x,y)^*W_g(x)\,a(g^{-1}x,y)\\
&\in\mathcal U(N),
\end{aligned}
\end{gathered}
\]
with \(\|b_g-g\|\le56b+14b+56b=126b\).

*All unitaries.* Let \(u\in\mathcal U(M)\) and \(g_j\in G\) with \(g_j\to u\) strongly. The vectors \(b_{g_j}\Omega=S_0g_j\Omega\) converge. For unitaries of \(N\), \(\|(b-b')\Omega\|=\|b-b'\|_2=\|b^*-b'^*\|_2\), so \(b_{g_j}^*\Omega\) converges too. A bounded sequence in \(N\) whose vectors at \(\Omega\) converge converges strongly, because it then converges on the dense set \(N'\Omega\). So \(b_{g_j}\) and \(b_{g_j}^*\) converge strongly, to a unitary \(b_u\in N\) and its adjoint, with \(S_0u\Omega=b_u\Omega\) and, since norm balls are weakly closed, \(\|b_u-u\|\le126b\).

*A Jordan isomorphism.* Every \(z\in M\) is a linear combination of unitaries, so \(S_0z\Omega\in N\Omega\), and since \(\Omega\) is separating for \(N\) there is a unique \(\vartheta(z)\in N\) with
\[
\vartheta(z)\Omega=S_0z\Omega .
\]
The map \(\vartheta\) is linear, \(\vartheta(1)=1\) and \(\vartheta(u)=b_u\) for unitaries \(u\). A self-adjoint contraction \(h\) is the average of the unitaries \(h\pm i(1-h^2)^{1/2}\), so \(\|\vartheta(h)-h\|\le126b\), and splitting into real and imaginary parts,
\[
\begin{gathered}
\|\vartheta(z)-z\|\le252\,b\,\|z\|\\
(z\in M).\quad(1.5)
\end{gathered}
\]
In particular \(\vartheta\) is bounded and maps unitaries to unitaries. For \(z=z^*\) and real \(t\), expand \(\vartheta(e^{itz})^*\vartheta(e^{itz})=1\) as a norm convergent power series in \(t\). The coefficient of \(t\) gives \(\vartheta(z)^*=\vartheta(z)\); applied to \(z^2\) as well, the coefficient of \(t^2\) gives \(\vartheta(z^2)=\vartheta(z)^2\). Polarizing, \(\vartheta\) preserves adjoints and the Jordan product \(x\circ y=\frac12(xy+yx)\).

*Bijectivity and orientation.* By (1.5) and \(252b<1\), \(\vartheta\) is injective with closed range. Every \(y\in N_1\) lies within \(b\) of some \(x\in M_1\), hence within \(253b<1\) of \(\vartheta(x)\); a proper closed subspace of \(N\) would have points of \(N_1\) at distance arbitrarily close to \(1\) (Riesz's lemma, as in the proof of Proposition 4.1 of the averaging lesson), so \(\vartheta\) is onto. By Lemma 3.1 of [Common tracial position and Jordan maps](common-tracial-position-and-jordan-maps.md), \(\vartheta\) is a homomorphism or an antihomomorphism. If it were an antihomomorphism, then for unitaries \(z,w\in M\),
\[
\begin{aligned}
\|zw-wz\|&\le\|zw-\vartheta(zw)\|\\
&\quad +\|\vartheta(w)\vartheta(z)-wz\|\\
&\le3\cdot126\,b<2 .
\end{aligned}
\]
But \(M\) contains a unital copy of \(M_2(\mathbb C)\), hence self-adjoint unitaries \(z,w\) with \(zw=-wz\) and \(\|zw-wz\|=2\). So \(\vartheta\) is a \(*\)-isomorphism, normal by Corollary 11.4 of the foundations lesson. \(\square\)

## 2. Return to the original Hilbert space

**Theorem 2.1** (strong stability of finite factors). There are \(t_{\rm fin}>0\) and a nondecreasing function \(\eta_{\rm fin}:(0,t_{\rm fin})\to(0,\infty)\) with \(\eta_{\rm fin}(t)\to0\) as \(t\to0\), such that the following holds. Let \(H\) be a nonzero separable Hilbert space, \(M\subseteq B(H)\) a unital finite factor and \(N\subseteq B(H)\) a unital von Neumann algebra with \(d(M,N)<t<t_{\rm fin}\). Then \(N\) is a finite factor and there is a unitary \(u\in B(H)\) with
\[
uMu^*=N,\qquad\|u-I\|\le\eta_{\rm fin}(t).
\]

**Proof.** Let \(C<6308\) be the constant of the uniform commutator estimate, and for \(0<t<10^{-14}\) put
\[
\begin{aligned}
\beta(t)&=50948\sqrt{302t},\qquad b(t)=3\beta(t),\\
e(t)&=252\,b(t)+\beta(t)+604t .
\end{aligned}
\]
Choose \(t_{\rm fin}>0\) so small that \(t_{\rm fin}<1/101\), \(302t_{\rm fin}<1.74\cdot10^{-13}\), \(b(t_{\rm fin})<1/1564\) and \(Ce(t_{\rm fin})<2\); and put \(\eta_{\rm fin}(t)=150t+Ce(t)\), a nondecreasing function tending to \(0\). Let \(d(M,N)<t<t_{\rm fin}\).

By Lemma 1.1 of [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md), \(N\) is a finite factor. By Lemma 1.4(2) of [Close operator algebras](close-operator-algebras.md), \(M\subset_tN\) and \(N\subset_tM\).

*Matrix algebras.* If \(M\) or \(N\) is finite-dimensional, it is injective, and Theorem 3.1 of the averaging lesson (Christensen's theorem, with \(t<1/101\)) gives a unitary within \(150t\) of \(I\) conjugating one of them onto the other; its adjoint, or itself, conjugates \(M\) onto \(N\).

*Type II\(_1\).* Otherwise both are II\(_1\) factors with separable preduals. Let \(R\subseteq M\) be the subfactor of Lemma 2.1 of the hyperfinite lesson; it is injective and \(R'\cap M=\mathbb C1\). Since \(R\subset_tN\), Christensen's theorem gives a unitary \(w\) with \(wRw^*\subseteq N\) and \(\|w-I\|\le150t\). Put \(N_0=w^*Nw\). Then \(R\subseteq M\cap N_0\), and by Lemma 1.5 of [Close operator algebras](close-operator-algebras.md), \(d(M,N_0)<301t\), so \(M\subset_gN_0\) and \(N_0\subset_gM\) with \(g=302t\).

Proposition 1.2 of [Common tracial position and Jordan maps](common-tracial-position-and-jordan-maps.md) gives faithful normal representations \(\pi\) of \(M\) and \(\rho\) of \(N_0\) on a separable space \(K\), with \(M_s=\pi(M)\) and \(N_s=\rho(N_0)\) in common standard tracial position, \(\pi|_R=\rho|_R\), and \(\beta<\beta(t)\). The subfactor \(\pi(R)\) is generated by the full matrix algebras \(\pi(Q_j)\) and is irreducible in \(M_s\), since \(\pi\) is an isomorphism. By Lemma 2.1 of that lesson, its right actions agree, and \(d(M_s,N_s)\le2\beta<b(t)\). Proposition 1.1 gives a normal \(*\)-isomorphism \(\vartheta_s:M_s\to N_s\) with \(\|\vartheta_s(x)-x\|\le252b(t)\) on \((M_s)_1\).

Transport it: \(\theta=\rho^{-1}\circ\vartheta_s\circ\pi:M\to N_0\) is a normal \(*\)-isomorphism. For \(x\in M_1\) choose \(y\in(N_0)_1\) with \(\|x-y\|<g\). Since \(\rho\) is isometric and by part (3) of the common-position proposition,
\[
\begin{aligned}
&\|\theta(x)-x\|\\
&\quad\le\|\vartheta_s\pi(x)-\rho(y)\|+\|y-x\|\\
&\quad\le\|\vartheta_s\pi(x)-\pi(x)\|\\
&\qquad+\|\pi(x)-\rho(y)\|+g\\
&\quad\le252\,b(t)+\beta+2g\le e(t).
\end{aligned}
\]

*Complete boundedness.* The map \(x\mapsto x\oplus\theta(x)\) is a faithful normal representation of \(M\) on \(H\oplus H\); let \(P\) be its image, a von Neumann algebra, and \(s(\xi,\eta)=(\eta,\xi)\) the self-adjoint switch. The commutator \([s,x\oplus\theta(x)]\) has off-diagonal entries \(\pm(\theta(x)-x)\), so \(\|\operatorname{ad}_s|_P\|\le e(t)\), because \(\|x\oplus\theta(x)\|=\|x\|\). The uniform commutator estimate gives \(\|\operatorname{ad}_s|_P\|_{\rm cb}\le Ce(t)\). At matrix level \(n\), the commutator of \(s^{(n)}\) with \(X\oplus\theta_n(X)\) has off-diagonal blocks \(\pm(\theta_n(X)-X)\), so
\[
\|\theta-\mathrm{id}_M\|_{\rm cb}\le C\,e(t)<2,
\]
where \(\theta\) is regarded as a representation of \(M\) on \(H\). Lemma 3.3 of [Close operator algebras](close-operator-algebras.md) gives a unitary \(v\) with \(vxv^*=\theta(x)\) for \(x\in M\) and \(\|v-I\|\le Ce(t)\); so \(vMv^*=\theta(M)=N_0\).

*Conclusion.* The unitary \(u=wv\) satisfies \(uMu^*=wN_0w^*=N\) and \(\|u-I\|\le150t+Ce(t)=\eta_{\rm fin}(t)\). In the matrix case the bound \(150t\) is smaller. \(\square\)

The constants are far from optimal; what matters is that every threshold and every bound is a function of \(t\) alone. Two different commutator arguments enter: Lemma 3.1 of the hyperfinite lesson controls a bimodular operator on the trace Hilbert space, and the uniform commutator estimate controls all matrix levels of a derivation. Neither alone produces a multiplicative map; the boundary does.

## 3. Exercises

**Exercise 3.1.** Show that \(U_{g,h}=g\,J_MhJ_M\) defines a unitary representation of \(G\times G\) and that its restriction to the diagonal is \(g\mapsto gJ_MgJ_M\), which acts on \(x\Omega\) as \(gxg^*\Omega\).

**Exercise 3.2.** In the proof of Proposition 1.1, show that \(\vartheta(1)=1\) from \(S_0\Omega=\Omega\).

**Exercise 3.3.** Let \(\vartheta\) be a linear map between unital C\*-algebras that maps unitaries to unitaries and \(1\) to \(1\). Use the power series argument of the proof to show that \(\vartheta(h^2)=\vartheta(h)^2\) for self-adjoint \(h\).

**Exercise 3.4.** Show that in a II\(_1\) factor there are self-adjoint unitaries \(z,w\) with \(zw=-wz\).

**Exercise 3.5.** Show that the representation \(x\mapsto x\oplus\theta(x)\) in the proof of Theorem 2.1 is isometric, and that \(\|[s,x\oplus\theta(x)]\|=\|\theta(x)-x\|\).

## 4. Solutions

**Solution 3.1.** \(J_MhJ_M\in M'\) commutes with \(g'\in M\), so \(U_{g,h}U_{g',h'}=gg'J_Mhh'J_M=U_{gg',hh'}\). For \(h=g\), \(gJ_MgJ_M(x\Omega)=g(xg^*\Omega)=gxg^*\Omega\), using that \(J_Mg^*J_M\) is right multiplication by \(g\) and \(J_MgJ_M\) by \(g^*\).

**Solution 3.2.** \(\vartheta(1)\Omega=S_01\Omega=\Omega=1\Omega\), and \(\Omega\) is separating for \(N\).

**Solution 3.3.** \(\vartheta(e^{ith})=\sum_n(it)^n\vartheta(h^n)/n!\) in norm, by continuity of \(\vartheta\): a self-adjoint element of norm at most \(1\) is the average of two unitaries, so \(\|\vartheta(z)\|\le2\|z\|\) for every \(z\). The constant term of \(\vartheta(e^{ith})^*\vartheta(e^{ith})=1\) is \(1\); the coefficient of \(t\) is \(i(\vartheta(h)-\vartheta(h)^*)=0\); the coefficient of \(t^2\) is \(-\frac12\vartheta(h^2)^*+\vartheta(h)^*\vartheta(h)-\frac12\vartheta(h^2)\), and self-adjointness of \(\vartheta(h)\) and \(\vartheta(h^2)\) gives \(\vartheta(h^2)=\vartheta(h)^2\).

**Solution 3.4.** A II\(_1\) factor contains two equivalent orthogonal projections with sum \(1\), hence matrix units \(e_{ij}\), \(i,j\le2\). Put \(z=e_{11}-e_{22}\) and \(w=e_{12}+e_{21}\).

**Solution 3.5.** \(\|x\oplus\theta(x)\|=\max(\|x\|,\|\theta(x)\|)=\|x\|\), since \(\theta\) is an isomorphism. The commutator is the operator matrix with zero diagonal and off-diagonal entries \(\theta(x)-x\) and \(x-\theta(x)\), whose norm is \(\|\theta(x)-x\|\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026

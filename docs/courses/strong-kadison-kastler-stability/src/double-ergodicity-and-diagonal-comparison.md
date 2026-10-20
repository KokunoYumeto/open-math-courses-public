# Double ergodicity and diagonal comparison

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The boundary space \((D,\nu)\) of [Boundary means and measurable cocycles](boundary-means-and-measurable-cocycles.md) carries two actions of \(G\) on \(D\times D\). The separate action of \(G\times G\) has an equivariant mean, so cocycles can be averaged over it. The diagonal action \(g(x,y)=(gx,gy)\) has no mean at our disposal, but it is rigid: a bounded measurable vector field on \(D\times D\) that transforms under a unitary representation of \(G\) is constant (Lemma 2.1, double ergodicity with unitary coefficients). This lesson proves that rigidity, and a substitute for averaging along the diagonal when the cocycle takes values in a finite von Neumann algebra: the vector of least norm in a convex hull computed in the trace Hilbert space (Lemma 1.1). In the next lessons the two facts combine with the averaged intertwiner to produce an isomorphism between close finite factors. Double ergodicity of Poisson boundaries is due to Kaimanovich; the unitary-coefficient form proved here, by bilateral random walks, is also in [Björklund, Theorem 2.1 and Remark 2.2] [OpenAI-289, Section 4].

We use: [Boundary means and measurable cocycles](boundary-means-and-measurable-cocycles.md) (the construction in the proof of Lemma 2.1 there: the symmetric measure \(\mu\), the shift \(S\), the map \(b\) with \(b\circ S=b\) almost everywhere and \(b(g\omega)=g\,b(\omega)\), and \(\nu=b_*\mathbb P\); and the conventions of its Section 1); standard measure theory as in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin, *Measure Theory*, Volumes 1 and 2: conditional expectations, Section 233; infinite products, Section 254); and the [weak compactness of the unit ball of \(B(H)\)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10).

## 1. Diagonal comparison in a finite algebra

Let \(A\) be a von Neumann algebra on a separable Hilbert space \(K\) with a unit vector \(\Omega\) that is cyclic for \(A\) and whose vector state \(\tau(x)=\langle x\Omega,\Omega\rangle\) is a trace on \(A\). Then \(\Omega\) is also separating, \(x\mapsto x\Omega\) identifies \(K\) with the trace Hilbert space \(L^2(A,\tau)\), and \(\|x\|_2=\|x\Omega\|\). Left multiplication by a unitary \(u\in A\) and right multiplication \(x\Omega\mapsto xu^*\Omega\) are unitaries of \(K\): the second because \(\tau(ux^*xu^*)=\tau(x^*x)\).

**Lemma 1.1** (diagonal comparison). Let \(W_g\in L^\infty(D,\mathcal U(A))\), \(g\in G\), be an exact cocycle for the action of \(G\) on the boundary space \((D,\nu)\), and suppose
\[
\begin{gathered}
r:=\sup_{g\in G}\ \operatorname*{ess\,sup}_{(x,y)\in D^2}\|W_g(x)W_g(y)^*-I\|\\
<1 .
\end{gathered}
\]
There is a bounded measurable field \(a:D^2\to\mathcal U(A)\) with \(\|a-I\|_\infty\le2r\) and
\[
a(x,y)=W_g(x)\,a(g^{-1}x,g^{-1}y)\,W_g(y)^*
\]
for all \(g\) and almost every \((x,y)\). If \(\|W_g-u_g\|_\infty\le\delta\) for unitaries \(u_g\in B(K)\) independent of the point, and \(2\delta<1\), then \(r\le2\delta\) and so \(\|a-I\|_\infty\le4\delta\).

**Proof.** Fix representatives of the \(W_g\) and a conull set of pairs \((x,y)\) on which all the inequalities \(\|W_t(x)W_t(y)^*-I\|\le r\), \(t\in G\), hold. For such \((x,y)\) let \(C_{x,y}\subseteq K\) be the closed convex hull of the countable set \(\{W_t(x)W_t(y)^*\Omega:t\in G\}\), and \(c(x,y)\) its unique vector of least norm.

*Measurability.* For a bounded operator field \(V\) the map \(x\mapsto V(x)\Omega\) is weakly measurable into the separable space \(K\), hence measurable. Enumerate the convex combinations of the generators with rational coefficients as \(z_j(x,y)\), \(j\ge1\); each is a measurable map into \(K\), and \(d(x,y)=\inf_j\|z_j(x,y)\|\) is the norm of \(c(x,y)\). For each \(n\) let \(j_n(x,y)\) be the first index with \(\|z_j(x,y)\|^2<d(x,y)^2+2^{-n}\); this choice is measurable. The midpoint of two such vectors lies in \(C_{x,y}\) and has norm at least \(d\), so the parallelogram identity gives
\[
\begin{aligned}
\|z_j-z_k\|^2&\le2(\|z_j\|^2-d^2)\\
&\quad +2(\|z_k\|^2-d^2).
\end{aligned}
\]
Hence \(z_{j_n}(x,y)\) converges in \(K\), to the least norm vector \(c(x,y)\), which is therefore a measurable map.

*An element of the algebra.* Each \(z_j(x,y)\) is \(\zeta_j\Omega\) for an operator \(\zeta_j\) in \(A\) that is a convex combination of unitaries \(W_t(x)W_t(y)^*\), so \(\|\zeta_j\|\le1\) and \(\|\zeta_j-I\|\le r\). A WOT cluster point \(\tilde c\) of \((\zeta_{j_n})\) lies in \(A\), satisfies \(\|\tilde c\|\le1\) and \(\|\tilde c-I\|\le r\), and \(\tilde c\Omega\) is the weak limit of \(\zeta_{j_n}\Omega\), namely \(c(x,y)\). Since \(\Omega\) is separating, \(\tilde c\) is determined by \(c(x,y)\); write \(c(x,y)\) also for this operator. For \(p,q\in A\), traciality gives \(\langle c(x,y)p\Omega,q\Omega\rangle=\tau(q^*c(x,y)p)\)\(=\langle c(x,y)\Omega,qp^*\Omega\rangle\), a measurable function; vectors \(p\Omega\) are dense and \(\|c(x,y)\|\le1\), so \(c\) is a bounded measurable operator field.

*Equivariance.* For \(g\in G\) the map \(\Phi(z\Omega)=W_g(x)\,z\,W_g(y)^*\Omega\), \(z\in A\), extends to a unitary of \(K\), the product of a left and a right multiplication. The cocycle identity gives \(W_g(x)W_t(g^{-1}x)=W_{gt}(x)\) and the same at \(y\), so \(\Phi\) maps the generator of \(C_{g^{-1}x,g^{-1}y}\) with index \(t\) to the generator of \(C_{x,y}\) with index \(gt\); as \(t\mapsto gt\) is a bijection, \(\Phi\) maps \(C_{g^{-1}x,g^{-1}y}\) onto \(C_{x,y}\). A unitary maps the least norm vector of a closed convex set to that of its image. Hence
\[
c(x,y)=W_g(x)\,c(g^{-1}x,g^{-1}y)\,W_g(y)^*
\]
almost everywhere; the action is nonsingular, so the translated conull sets are conull.

*Polar part.* Since \(\|c-I\|\le r<1\), \(c(x,y)\) is invertible with \(1-r\le|c(x,y)|\le1+r\). Its polar part \(a=c|c|^{-1}\) is a measurable unitary field in \(A\) with \(\|a-c\|_\infty=\|I-|c|\|_\infty\le r\), so \(\|a-I\|_\infty\le2r\). If \(c'=ucv^*\) with unitaries \(u,v\), then \(|c'|=v|c|v^*\) and \(c'|c'|^{-1}=u\,(c|c|^{-1})\,v^*\); so \(a\) has the same transformation law as \(c\). Finally \(\|W_g(x)W_g(y)^*-I\|\)\(\le\|W_g(x)-u_g\|+\|u_g-W_g(y)\|\)\(\le2\delta\). \(\square\)

## 2. Double ergodicity with unitary coefficients

**Lemma 2.1** (double ergodicity). Let \((D,\nu)\) be the boundary space of Lemma 2.1 of [Boundary means and measurable cocycles](boundary-means-and-measurable-cocycles.md), and \(\sigma:G\to\mathcal U(K)\) a unitary representation on a separable Hilbert space. If a bounded measurable map \(f_0:D^2\to K\) satisfies, for every \(g\in G\),
\[
f_0(gx,gy)=\sigma(g)f_0(x,y)
\]
for almost every \((x,y)\), then \(f_0\) is almost everywhere equal to a constant vector \(v\) with \(\sigma(g)v=v\) for all \(g\).

**Proof.** *Bilateral walks.* Let \((\omega_j)_{j\in\mathbb Z}\) be independent with law \(\mu\), on the product space \(\Omega_{\mathbb Z}=G^{\mathbb Z}\), and let \(\theta\) be the left shift, \((\theta\omega)_j=\omega_{j+1}\); it preserves the product measure. Put
\[
\begin{aligned}
b_+(\omega)&=b(\omega_0,\omega_1,\omega_2,\dots),\\
b_-(\omega)&=b(\omega_{-1}^{-1},\omega_{-2}^{-1},\dots),
\end{aligned}
\]
and \(f(\omega)=f_0(b_+(\omega),b_-(\omega))\). The sequences \((\omega_0,\omega_1,\dots)\) and \((\omega_{-1}^{-1},\omega_{-2}^{-1},\dots)\) use disjoint coordinates and, because \(\mu\) is symmetric, both have law \(\mathbb P\). So \(b_+\) and \(b_-\) are independent with law \(\nu\), and \((b_+,b_-)\) has law \(\nu\otimes\nu\).

*Transport along the walk.* The shift \(S\) and the action satisfy \(S(\omega_0,\omega_1,\omega_2,\dots)=\omega_0\cdot(\omega_1,\omega_2,\dots)\). With \(b\circ S=b\) and equivariance, almost everywhere
\[
\begin{aligned}
b_+(\theta\omega)&=b(\omega_1,\omega_2,\dots)=\omega_0^{-1}b_+(\omega),\\
b_-(\theta\omega)&=b(\omega_0^{-1},\omega_{-1}^{-1},\dots)=\omega_0^{-1}b_-(\omega),
\end{aligned}
\]
the second because \(S(\omega_0^{-1},\omega_{-1}^{-1},\dots)=\omega_0^{-1}\cdot(\omega_{-1}^{-1},\omega_{-2}^{-1},\dots)\). Let \(N_g\subseteq D^2\) be the null set where \(f_0(gx,gy)\ne\sigma(g)f_0(x,y)\). The event that \((b_+,b_-)\in N_{\omega_0^{-1}}\) is contained in \(\bigcup_g\{(b_+,b_-)\in N_g\}\), which is null because \((b_+,b_-)\) has law \(\nu\otimes\nu\) and \(G\) is countable. Therefore \(f(\theta\omega)=\sigma(\omega_0^{-1})f(\omega)\) almost everywhere, and by induction, since \(\theta\) preserves the measure,
\[
\begin{gathered}
\begin{aligned}
f(\theta^n\omega)&=\sigma\bigl(\omega_{n-1}^{-1}\cdots\omega_0^{-1}\bigr)f(\omega)
\end{aligned}\\
(n\ge1).\quad(2.1)
\end{gathered}
\]

*Independent blocks.* The map \(f\) is a bounded element of \(L^2(\Omega_{\mathbb Z},K)\). Let \(f_m\) be its conditional expectation onto the \(\sigma\)-algebra of the coordinates in \([-m,m]\), computed coefficientwise in an orthonormal basis of \(K\). These \(\sigma\)-algebras increase and generate the product \(\sigma\)-algebra, so \(\varepsilon_m=\|f-f_m\|_2\to0\). Fix \(m\) and \(n\ge2m+2\), and put
\[
\begin{aligned}
Q&=\sigma(\omega_m^{-1}\cdots\omega_0^{-1}),\\
P&=\sigma(\omega_{n-m-1}^{-1}\cdots\omega_{m+1}^{-1}),\\
R&=\sigma(\omega_{n-1}^{-1}\cdots\omega_{n-m}^{-1}),
\end{aligned}
\]
and \(A=Qf_m\), \(B=R^{-1}(f_m\circ\theta^n)\). Then \(A\), \(P\) and \(B\) depend on the disjoint coordinate sets \([-m,m]\), \([m+1,n-m-1]\) and \([n-m,n+m]\), so they are independent. By (2.1), \(R^{-1}(f\circ\theta^n)=PQf\), and since the operators are unitary and \(\theta\) preserves the measure,
\[
\begin{aligned}
&\|PA-B\|_2\le\|PQ(f_m-f)\|_2\\
&\quad+\|R^{-1}(f\circ\theta^n-f_m\circ\theta^n)\|_2=2\varepsilon_m .
\end{aligned}
\]
Let \(a_0=\mathbb E A\) and \(b_0=\mathbb E B\). Write \(PA-B\) as the sum of \(P(A-a_0)\), \(-(B-b_0)\) and \(Pa_0-b_0\). The three cross terms of \(\mathbb E\|PA-B\|^2\) vanish: conditioning on \((P,B)\), the first term has mean zero and is independent of the others; and \(B-b_0\) has mean zero and is independent of \(P\). Hence
\[
\begin{aligned}
\mathbb E\|PA-B\|^2&=\mathbb E\|A-a_0\|^2\\
&\quad +\mathbb E\|B-b_0\|^2\\
&\quad +\mathbb E\|Pa_0-b_0\|^2,
\end{aligned}
\]
and \(\|A-a_0\|_2\le2\varepsilon_m\), \(\|B-b_0\|_2\le2\varepsilon_m\).

*Two tails.* From \(f-Q^{-1}a_0=(f-f_m)+Q^{-1}(A-a_0)\) we get \(\|f-Q^{-1}a_0\|_2\le3\varepsilon_m\), and \(Q^{-1}a_0\) depends only on the coordinates in \([0,m]\). From \(f\circ\theta^n-Rb_0\)\(=(f-f_m)\circ\theta^n+R(B-b_0)\) and invariance of the measure under \(\theta^{-n}\), \(\|f-(Rb_0)\circ\theta^{-n}\|_2\le3\varepsilon_m\), and \((Rb_0)\circ\theta^{-n}=\sigma(\omega_{-1}^{-1}\cdots\omega_{-m}^{-1})b_0\) depends only on the coordinates in \([-m,-1]\). Letting \(m\to\infty\), \(f\) lies in the closed subspace of \(L^2\) of functions of the coordinates \(j\ge0\), and in that of functions of the coordinates \(j<0\). These two \(\sigma\)-algebras are independent. The conditional expectation of \(f\) onto the first equals \(f\), because \(f\) is measurable for it, and equals the constant \(\mathbb Ef\), because \(f\) is measurable for the second, which is independent of the first. So \(f=v\) almost everywhere for a vector \(v\in K\).

*Conclusion.* Since \((b_+,b_-)\) has law \(\nu\otimes\nu\) and \(f=f_0\circ(b_+,b_-)\), \(f_0=v\) almost everywhere on \(D^2\). The equivariance at a point of the conull set where \(f_0=v\) and \(f_0(gx,gy)=\sigma(g)f_0(x,y)\), which is conull by nonsingularity, gives \(v=\sigma(g)v\). \(\square\)

With \(\sigma\) trivial, Lemma 2.1 says that the diagonal action of \(G\) on \((D^2,\nu\otimes\nu)\) is ergodic; this is the double ergodicity of the Poisson boundary.

## 3. Exercises

**Exercise 3.1.** Deduce from Lemma 2.1 that the action of \(G\) on \((D,\nu)\) is ergodic: every measurable \(E\subseteq D\) with \(gE=E\) up to null sets for all \(g\) has \(\nu(E)\in\{0,1\}\).

**Exercise 3.2.** Let \(K\) be a Hilbert space, \(C\subseteq K\) a nonempty closed convex set and \(U\) a unitary of \(K\). Prove that \(C\) has a unique vector of least norm, and that \(U\) maps it to the least norm vector of \(UC\).

**Exercise 3.3.** In Lemma 1.1 suppose that the cocycle is a coboundary of a special form: \(W_g(x)=w(x)\,u_g\,w(g^{-1}x)^*\) for a representation \(g\mapsto u_g\) into \(\mathcal U(A)\) and a measurable \(w:D\to\mathcal U(A)\). Show that \(a(x,y)=w(x)w(y)^*\) satisfies the transformation law.

**Exercise 3.4.** Verify the cross-term computation in the proof of Lemma 2.1 for the pair \(P(A-a_0)\) and \(-(B-b_0)\).

**Exercise 3.5.** Show that the conclusion of Lemma 2.1 holds for \(f_0\) with values in a closed subspace \(K_0\subseteq K\) invariant under \(\sigma\), and that the constant then lies in \(K_0\).

## 4. Solutions

**Solution 3.1.** Apply Lemma 2.1 with \(K=\mathbb C\), \(\sigma\) trivial and \(f_0(x,y)=1_E(x)\). It is invariant under the diagonal action, so it is almost everywhere constant; hence \(1_E\) is almost everywhere constant on \(D\).

**Solution 3.2.** Let \(d=\inf_{z\in C}\|z\|\) and \(z_n\in C\) with \(\|z_n\|\to d\). The midpoint of \(z_n,z_k\) lies in \(C\), so \(\|z_n-z_k\|^2\)\(\le2\|z_n\|^2+2\|z_k\|^2-4d^2\to0\); the limit is a least norm vector, and the same inequality shows that two least norm vectors coincide. \(U\) maps \(C\) bijectively onto \(UC\) preserving norms.

**Solution 3.3.** \(W_g(x)\,w(g^{-1}x)w(g^{-1}y)^*\,W_g(y)^*\)\(=w(x)u_gu_g^*w(y)^*=w(x)w(y)^*\).

**Solution 3.4.** \(\mathbb E\langle P(A-a_0),B-b_0\rangle\) is the expectation over \((P,B)\) of \(\langle P\,\mathbb E(A-a_0),B-b_0\rangle\), because \(A\) is independent of \((P,B)\); and \(\mathbb E(A-a_0)=0\).

**Solution 3.5.** The lemma gives a constant \(v\) with \(f_0=v\) almost everywhere; since \(f_0\) takes values in \(K_0\) on a conull set, \(v\in K_0\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [Björklund] M. Björklund, Five remarks about random walks on groups, preprint, version 2, 7 July 2014. https://arxiv.org/abs/1406.0763v2

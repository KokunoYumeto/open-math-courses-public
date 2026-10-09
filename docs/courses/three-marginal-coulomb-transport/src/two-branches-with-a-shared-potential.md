# Two branches with a shared potential

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that a Monge optimizer need not exist for three particles with a Riesz interaction (Theorem 4.2). Following [Couplings and supporting potentials](couplings-and-supporting-potentials.md), it suffices to construct a density \(\mu\) of the form \(\frac13\nu+\frac16\sum_jH_{j\#}\nu\) and a bounded potential whose contact set offers, above each central point \(x\), only the four branch points \(H_j(x)\) (Corollary 4.1 there). OpenAI builds the potential by local calculus near the two triples \((0,e_1,-e_1)\) and \((0,e_2,-e_2)\) [OpenAI-CM, Sections 3–5 and 7], which have the same cost and the same gradient in the central variable; this is what lets the two branches share one central potential.

Throughout, \(d\ge2\) and \(s>0\) are fixed, \(e_1,e_2\) are the first two standard basis vectors of \(\mathbb R^d\), \(a_1=e_1\), \(a_2=e_2\), and \(c=c_s\) is the Riesz cost
\[
c(x,y,z)=h(x-y)+h(x-z)+h(y-z),\qquad h(b)=|b|^{-s}\quad(b\neq0).
\]
The Coulomb cost is the case \(d=3\), \(s=1\). We use the inverse and implicit function theorems in their continuously differentiable form, as proved in the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (Lebl, *Basic Analysis II*, [Theorem 8.5.1](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_inverse) and [Theorem 8.5.6](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_implicit)), together with Lemma 1.1 below. A map is *smooth* if it has continuous partial derivatives of all orders, and a *diffeomorphism onto its image* is a smooth bijection onto an open set with smooth inverse.

## 1. Preliminaries

**Lemma 1.1** (smoothness). If the map \(G\) in the implicit function theorem is smooth, the implicit function \(g\) is smooth; if the map \(f\) in the inverse function theorem is smooth, its local inverse is smooth.

**Proof.** Differentiating \(G(g(y),y)=0\) gives \(Dg(y)=-\bigl[D_1G(g(y),y)\bigr]^{-1}D_2G(g(y),y)\) on the domain of \(g\), where \(D_1G\) is invertible. Matrix inversion is smooth on invertible matrices, so \(Dg=\Phi(g(y),y)\) with \(\Phi\) smooth. If \(g\) has continuous derivatives of order \(k\), so does \(Dg\), hence \(g\) has them of order \(k+1\); by induction \(g\) is smooth. For the local inverse \(f^{-1}\), use \(D(f^{-1})(w)=\bigl[Df(f^{-1}(w))\bigr]^{-1}\) in the same way. \(\square\)

**Lemma 1.2.** (a) For \(b\neq0\),
\[
\nabla h(b)=-s|b|^{-s-2}b,\qquad D^2h(b)=s|b|^{-s-2}\Bigl((s+2)\frac{bb^{\mathsf T}}{|b|^2}-I\Bigr),
\]
and \(D^2h(b)\) has the eigenvalue \(s(s+1)|b|^{-s-2}\) on \(b\) and \(-s|b|^{-s-2}\) on the vectors orthogonal to \(b\); in particular it is invertible.

(b) For \(k=1,2\) and \(\gamma=s(1+2^{-s-1})\),
\[
c(0,a_k,-a_k)=2+2^{-s},\qquad\nabla_xc(0,a_k,-a_k)=0,\qquad\nabla_zc(0,a_k,-a_k)=\gamma\,a_k .
\]

**Proof.** (a) Differentiate \(h(b)=(b\cdot b)^{-s/2}\) twice: \(\partial_ih=-s|b|^{-s-2}b_i\) and \(\partial_j\partial_ih=s(s+2)|b|^{-s-4}b_ib_j-s|b|^{-s-2}\delta_{ij}\). The eigenvalues follow from \(bb^{\mathsf T}b=|b|^2b\) and \(bb^{\mathsf T}v=0\) for \(v\perp b\).

(b) The three distances are \(|0-a_k|=1\), \(|0+a_k|=1\) and \(|2a_k|=2\). Next, \(\nabla_xc=\nabla h(x-y)+\nabla h(x-z)=\nabla h(-a_k)+\nabla h(a_k)=sa_k-sa_k=0\), and \(\nabla_zc=\nabla h(z-x)+\nabla h(z-y)=\nabla h(-a_k)+\nabla h(-2a_k)=sa_k+s2^{-s-2}\cdot2a_k=\gamma a_k\). \(\square\)

For the Coulomb cost, \(c(0,a_k,-a_k)=\frac52\) and \(\gamma=\frac54\). The two center triples have the same cost and the same \(x\)-gradient: this is what allows one potential in the central variable for both.

## 2. A local branch

For a constant \(K>0\) put
\[
u_0(x)=2+2^{-s}-\frac K2|x|^2,\qquad v_k(z)=\gamma\,a_k\cdot(z+a_k)-\frac K2|z+a_k|^2\qquad(k=1,2).
\]

**Lemma 2.1** (OpenAI). There are \(K>0\), and for \(k=1,2\) open balls \(P^k_0\), \(P^+_k\), \(P^-_k\) centered at \(0\), \(a_k\), \(-a_k\), smooth maps \(X_k,Z_k\colon P^+_k\to\mathbb R^d\) and a smooth function \(w_k\colon P^+_k\to\mathbb R\) with the following properties:

1. \(X_k(a_k)=0\), \(Z_k(a_k)=-a_k\), \(w_k(a_k)=0\), and \(X_k\) and \(Z_k\) are diffeomorphisms of \(P^+_k\) onto open sets;
2. for all \((x,y,z)\in P^k_0\times P^+_k\times P^-_k\),
\[
c(x,y,z)\ge u_0(x)+w_k(y)+v_k(z),\tag{2.1}
\]
with equality if and only if \(x=X_k(y)\) and \(z=Z_k(y)\).

**Proof.** Let \(F_k(x,y,z)=c(x,y,z)-u_0(x)-v_k(z)\), a smooth function near the center triple \(p_k=(0,a_k,-a_k)\), where no two points collide. By Lemma 1.2(b), \(\nabla_xF_k(p_k)=0-0=0\) and \(\nabla_zF_k(p_k)=\gamma a_k-\gamma a_k=0\), and \(F_k(p_k)=0\).

*Choice of \(K\).* Let \(M_k\) be the Hessian of \(c\) in the variables \((x,z)\in\mathbb R^{2d}\) at \(p_k\), a symmetric \(2d\times2d\) matrix, and let \(N_k\) be the \(2d\times d\) matrix of mixed derivatives \(D_y\nabla_{(x,z)}c\) at \(p_k\). Only the terms \(h(x-y)\) and \(h(z-y)\) involve both groups of variables, so the two \(d\times d\) blocks of \(N_k\) are \(-D^2h(-a_k)\) (for \(x\)) and \(-D^2h(-2a_k)\) (for \(z\)), both invertible by Lemma 1.2(a). The \((x,z)\)-Hessian of \(F_k\) at \(p_k\) is \(M_k+KI_{2d}\), and its mixed derivative is \(N_k\). As \(K\to\infty\),
\[
K(M_k+KI_{2d})^{-1}N_k=(I_{2d}+K^{-1}M_k)^{-1}N_k\longrightarrow N_k .
\]
Since invertibility of a \(d\times d\) matrix is an open condition, we can fix \(K\) so large that, for \(k=1,2\), \(M_k+KI_{2d}\) is positive definite and both \(d\times d\) blocks of \((M_k+KI_{2d})^{-1}N_k\) are invertible.

*The branch.* Apply the implicit function theorem to the smooth map \(\nabla_{(x,z)}F_k\) near \(p_k\), whose derivative in \((x,z)\) at \(p_k\) is the invertible matrix \(M_k+KI_{2d}\). It gives a ball \(Q\) around \(a_k\) and smooth maps \(X_k,Z_k\) on \(Q\) (Lemma 1.1) with
\[
\nabla_{(x,z)}F_k\bigl(X_k(y),y,Z_k(y)\bigr)=0,\qquad X_k(a_k)=0,\qquad Z_k(a_k)=-a_k .
\]
Differentiating at \(y=a_k\) gives \(D(X_k,Z_k)(a_k)=-(M_k+KI_{2d})^{-1}N_k\), so \(DX_k(a_k)\) and \(DZ_k(a_k)\) are the negatives of the two blocks, both invertible. By the inverse function theorem and Lemma 1.1, after shrinking \(Q\) to a smaller ball around \(a_k\), both \(X_k\) and \(Z_k\) are diffeomorphisms onto open sets (the restriction of such a map to an open subset is again one).

*Minimality.* The \((x,z)\)-Hessian of \(F_k\) depends continuously on \((x,y,z)\) near \(p_k\), so it is positive definite on a product \(P^k_0\times Q'\times P^-_k\) of pairwise disjoint balls around the three centers, on which \(F_k\) is smooth. Shrink the ball around \(a_k\) to a ball \(P^+_k\subseteq Q\cap Q'\) on which \((X_k(y),Z_k(y))\in P^k_0\times P^-_k\). For fixed \(y\in P^+_k\), the function \((x,z)\mapsto F_k(x,y,z)\) is strictly convex on the convex set \(P^k_0\times P^-_k\) and has the critical point \((X_k(y),Z_k(y))\) there, so this point is its unique minimum. Put \(w_k(y)=F_k(X_k(y),y,Z_k(y))\), a smooth function with \(w_k(a_k)=F_k(p_k)=0\). Then \(F_k(x,y,z)\ge w_k(y)\) on the product, with equality exactly at \((x,z)=(X_k(y),Z_k(y))\); this is (2.1). \(\square\)

Restricting the balls of Lemma 2.1 keeps (2.1) and its equality condition.

## 3. A potential on five balls

**Proposition 3.1** (OpenAI). There are open balls \(U_0\), \(U^\pm_1\), \(U^\pm_2\) centered at \(0\), \(\pm a_1\), \(\pm a_2\) with pairwise disjoint closures, and a bounded continuous function \(u\) on their union \(U\), such that
\[
c(x_1,x_2,x_3)\ge u(x_1)+u(x_2)+u(x_3)\qquad\text{on }U^3,\tag{3.1}
\]
with equality exactly at the permutations of the triples \((X_k(y),y,Z_k(y))\) with \(y\in U^+_k\) and \(k\in\{1,2\}\). Moreover \(X_k(U^+_k)\subseteq U_0\) and \(Z_k(U^+_k)\subseteq U^-_k\).

**Proof.** Take preliminary closed balls inside the balls of Lemma 2.1, with \(U_0\) inside \(P^1_0\cap P^2_0\), and let \(m\) bound the absolute values of \(u_0\), \(w_k\) and \(v_k\) on them. All balls below lie inside these and have radius at most \(r\), to be chosen. Define
\[
u=u_0\ \text{on }U_0,\qquad u=w_k\ \text{on }U^+_k,\qquad u=v_k\ \text{on }U^-_k .
\]
At the five centers \(u\) takes the values \(2+2^{-s},0,0,0,0\), since \(w_k(a_k)=0\) and \(v_k(-a_k)=0\). Consider the \(125\) ordered triples of balls.

*Two coordinates in one ball.* Their distance is at most \(2r\), so \(c\ge(2r)^{-s}\), while \(u(x_1)+u(x_2)+u(x_3)\le3m\). Choosing \(r\) with \((2r)^{-s}>3m\) makes (3.1) strict on all these products, collisions included.

*Three different balls, not a permutation of \((U_0,U^+_k,U^-_k)\).* If \(U_0\) is not among them, the sum of \(u\) at the three centers is \(0\), while their cost is positive. If \(U_0\) is among them, the other two centers are \(\pm a_1\) and \(\pm a_2\), at distance \(\sqrt2\) from each other and \(1\) from \(0\), so their cost is \(2+2^{-s/2}>2+2^{-s}\). In both cases (3.1) is strict at the centers. The cost and \(u\) are continuous near these finitely many center triples, since their points are distinct, so after shrinking \(r\) the strict inequality holds on all such products.

*A permutation of \((U_0,U^+_k,U^-_k)\).* By the symmetry of \(c\) and of \(\sum_iu(x_i)\), it suffices to take the order \((U_0,U^+_k,U^-_k)\), where (3.1) is (2.1) and equality holds exactly when \(x=X_k(y)\) and \(z=Z_k(y)\).

Finally keep \(U_0\) and \(U^-_k\), and shrink \(U^+_k\) around \(a_k\) so that \(X_k(U^+_k)\subseteq U_0\) and \(Z_k(U^+_k)\subseteq U^-_k\), which is possible since \(X_k(a_k)=0\) and \(Z_k(a_k)=-a_k\). Shrinking a ball keeps all inequalities, and the equality triples \((X_k(y),y,Z_k(y))\), \(y\in U^+_k\), then lie in \(U^3\). The function \(u\) is continuous on the open set \(U\) and bounded by \(m\). \(\square\)

**Lemma 3.2.** There is an open ball \(B\subseteq U_0\) centered at \(0\) on which
\[
Y_k=\bigl(X_k|_{U^+_k}\bigr)^{-1},\qquad W_k=Z_k\circ Y_k\qquad(k=1,2)
\]
are defined and are diffeomorphisms of \(B\) onto open sets with \(Y_k(B)\subseteq U^+_k\) and \(W_k(B)\subseteq U^-_k\). The five sets \(B,Y_1(B),W_1(B),Y_2(B),W_2(B)\) are pairwise disjoint, and for \(x\in B\) the triples \((x,Y_k(x),W_k(x))\) are equality triples of (3.1).

**Proof.** The sets \(X_1(U^+_1)\) and \(X_2(U^+_2)\) are open and contain \(0\); take a ball \(B\) around \(0\) inside both and inside \(U_0\). The inverse of the diffeomorphism \(X_k|_{U^+_k}\) is defined and smooth on \(B\), with values in \(U^+_k\), and \(W_k\) takes values in \(Z_k(U^+_k)\subseteq U^-_k\); compositions and inverses of diffeomorphisms onto open sets are again such. Since \(X_k(Y_k(x))=x\), the triple \((x,Y_k(x),W_k(x))=(X_k(y),y,Z_k(y))\) with \(y=Y_k(x)\) is an equality triple. The five sets lie in the five disjoint balls. \(\square\)

## 4. The density and the theorem

Choose a function \(g\ge0\), smooth with compact support in \(B\), with \(\int g^2\,dx=1\), and let \(\nu=g^2\,dx\). Let \(\mathcal H=\{Y_1,W_1,Y_2,W_2\}\) and
\[
\mu=\frac13\nu+\frac16\sum_{H\in\mathcal H}H_\#\nu .\tag{4.1}
\]

**Lemma 4.1.** \(\mu=\rho\,dx\), where \(\rho\) is smooth with compact support, \(\int\rho=1\), and \(\sqrt\rho\) is smooth.

**Proof.** For \(H\in\mathcal H\) let \(g_H(y)=g(H^{-1}(y))\,|\det DH^{-1}(y)|^{1/2}\) for \(y\in H(B)\) and \(g_H=0\) elsewhere. The determinant of \(DH^{-1}\) never vanishes on \(H(B)\), so \(g_H\) is smooth on \(H(B)\); it vanishes outside the compact set \(H(\operatorname{supp}g)\subseteq H(B)\), so it is smooth on \(\mathbb R^d\). For a Borel set \(A\subseteq H(B)\), the change of variables formula (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 2, Theorem 263D](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm)) for the injective map \(H^{-1}\) gives
\[
H_\#\nu(A)=\int_{H^{-1}(A)}g^2\,dx=\int_A g\bigl(H^{-1}(y)\bigr)^2\,|\det DH^{-1}(y)|\,dy=\int_Ag_H^2\,dy,
\]
and \(H_\#\nu\) vanishes outside \(H(B)\). So \(\rho=\frac13g^2+\frac16\sum_Hg_H^2\). The five functions \(g,g_H\) are nonnegative with supports in the five disjoint sets of Lemma 3.2, so \(\sqrt\rho=\frac1{\sqrt3}g+\frac1{\sqrt6}\sum_Hg_H\), which is smooth. The weights add up to \(\frac13+4\cdot\frac16=1\). \(\square\)

**Theorem 4.2** (OpenAI 2026). For every \(d\ge2\) and \(s>0\), the measure \(\mu\) of (4.1) has the following properties for the Riesz cost \(c_s\): the Kantorovich value \(\mathcal E_{c_s}(\mu)\) is finite and attained, and every pair of Borel maps \(T_2,T_3\) preserving \(\mu\) satisfies
\[
\int c_s\bigl(x,T_2(x),T_3(x)\bigr)\,d\mu(x)>\mathcal E_{c_s}(\mu),
\]
the left side possibly being infinite. In particular, for the Coulomb cost on \(\mathbb R^3\) there is a smooth density with smooth square root for which no Monge optimizer exists.

**Proof.** *A coupling on the contact set.* Draw \(x\) with law \(\nu\), choose \(k\in\{1,2\}\) uniformly and independently, and apply a uniformly random permutation, independent of both, to the triple \((x,Y_k(x),W_k(x))\). Let \(\pi_0\) be the law of the result. In each coordinate, with probability \(\frac13\) the entry is the central point, with law \(\nu\), and with probability \(\frac13\cdot\frac12=\frac16\) it is \(H(x)\) for each \(H\in\mathcal H\), with law \(H_\#\nu\). So every marginal of \(\pi_0\) is \(\mu\), and by Lemma 3.2, \(\pi_0\) is carried by the contact set \(\Gamma\) of (3.1). Also \(\mu(U)=1\), since \(\mu\) is carried by \(B\cup\bigcup_HH(B)\subseteq U\).

*Selection.* Let \(x\in B\) and \((x,y,z)\in\Gamma\). Exactly one coordinate of an equality triple lies in \(U_0\), and \(x\in B\subseteq U_0\), so \(y\) and \(z\) lie in \(U^+_k\) and \(U^-_k\), in some order, for some \(k\). If \(y\in U^+_k\), then \(x=X_k(y)\), so \(y=Y_k(x)\) because \(X_k\) is injective on \(U^+_k\); if \(y\in U^-_k\), then \(z\in U^+_k\), \(z=Y_k(x)\) and \(y=Z_k(z)=W_k(x)\). In all cases \(y\in\{Y_1(x),W_1(x),Y_2(x),W_2(x)\}\).

Corollary 4.1 of [Couplings and supporting potentials](couplings-and-supporting-potentials.md), applied with \(u\) from Proposition 3.1 and the four branches of \(\mathcal H\), shows that \(\mathcal E_{c_s}(\mu)\) is finite and attained, but by no Monge plan. Since a Monge plan always costs at least \(\mathcal E_{c_s}(\mu)\), its cost is strictly larger. With \(d=3\), \(s=1\), and Lemma 4.1, this gives the Coulomb statement. \(\square\)

The construction also shows that every optimal coupling is carried by the two families of triples, and that symmetrizing an optimal coupling does not help: the obstruction concerns where the mass at the central points must go, not the order of the coordinates.

## 5. Exercises

**Exercise 5.1** (easy). For the Coulomb cost, compute \(M_k\) and \(N_k\) in Lemma 2.1 for \(k=1\), using Lemma 1.2(a).

**Exercise 5.2** (easy). Check the strict gap of Proposition 3.1 for the triple of centers \((0,a_1,-a_2)\): its cost is \(2+2^{-s/2}\), and \(2^{-s/2}>2^{-s}\) for every \(s>0\).

**Exercise 5.3** (medium). Show that one opposite pair would not suffice. Let \(\mu'=\frac13\nu+\frac13Y_{1\#}\nu+\frac13W_{1\#}\nu\), and let \(\sigma\) equal \(Y_1\) on \(B\), \(W_1\circ Y_1^{-1}\) on \(Y_1(B)\), \(W_1^{-1}\) on \(W_1(B)\), and the identity elsewhere. Show that \(\sigma\) preserves \(\mu'\), that the Monge plan \((\mathrm{id},\sigma,\sigma\circ\sigma)_\#\mu'\) is carried by the permutations of the triples \((x,Y_1(x),W_1(x))\), and deduce from Proposition 2.1 of [Couplings and supporting potentials](couplings-and-supporting-potentials.md) that it is optimal for \(\mu'\).

**Exercise 5.4** (medium). Show that in Lemma 2.1 the potential \(w_k\) is given by \(w_k(y)=\min\{c(x,y,z)-u_0(x)-v_k(z):(x,z)\in P^k_0\times P^-_k\}\), and compute its gradient at \(a_k\).

## 6. Solutions

**5.1.** At \(p_1=(0,e_1,-e_1)\) the relevant differences are \(x-y=-e_1\), \(x-z=e_1\), \(z-y=-2e_1\). With \(s=1\), \(D^2h(b)=|b|^{-3}(3bb^{\mathsf T}/|b|^2-I)\), so \(D^2h(\pm e_1)=\operatorname{diag}(2,-1,-1)\) and \(D^2h(-2e_1)=\frac18\operatorname{diag}(2,-1,-1)\). The \(xx\)-block of \(M_1\) is \(D^2h(-e_1)+D^2h(e_1)=\operatorname{diag}(4,-2,-2)\), the \(zz\)-block is \(D^2h(e_1)+D^2h(-2e_1)=\frac98\operatorname{diag}(2,-1,-1)\), and the \(xz\)-block is \(-D^2h(x-z)=-\operatorname{diag}(2,-1,-1)\). The blocks of \(N_1\) are \(-\operatorname{diag}(2,-1,-1)\) and \(-\frac18\operatorname{diag}(2,-1,-1)\).

**5.2.** The distances are \(|a_1|=1\), \(|a_2|=1\) and \(|a_1+a_2|=\sqrt2\), so the cost is \(2+(\sqrt2)^{-s}\); the potential sum at the centers is \(2+2^{-s}\), and \(2^{-s/2}>2^{-s}\) because \(s/2<s\).

**5.3.** The map \(\sigma\) sends \(\frac13\nu\) to \(\frac13Y_{1\#}\nu\), then \(\frac13Y_{1\#}\nu\) to \(\frac13(W_1\circ Y_1^{-1}\circ Y_1)_\#\nu=\frac13W_{1\#}\nu\), and \(\frac13W_{1\#}\nu\) back to \(\frac13\nu\), so it preserves \(\mu'\); it is Borel as in Exercise 5.2 of [Couplings and supporting potentials](couplings-and-supporting-potentials.md). For \(x\in B\) the triple \((x,\sigma x,\sigma^2x)\) is \((x,Y_1x,W_1x)\); for \(x=Y_1(x')\) it is \((Y_1x',W_1x',x')\); for \(x=W_1(x')\) it is \((W_1x',x',Y_1x')\). All are equality triples of (3.1). The potential \(u\) restricted to \(U_0\cup U^+_1\cup U^-_1\) satisfies (3.1) on the cube of this set, which carries \(\mu'\), so Proposition 2.1 there shows that the Monge plan is optimal. Here the mass count of Lemma 3.1 there gives \(\frac13\le\frac13\), no contradiction: the second pair \(\pm a_2\) is what halves the mass available to each branch.

**5.4.** This is the definition in the proof of Lemma 2.1, since the minimum is attained at \((X_k(y),Z_k(y))\). By the envelope argument, \(\nabla w_k(y)=\nabla_yF_k(X_k(y),y,Z_k(y))\) because \(\nabla_{(x,z)}F_k\) vanishes there; at \(y=a_k\) this is \(\nabla_yc(p_k)=\nabla h(a_k)-\nabla h(z-y)\big|_{z-y=-2a_k}=-sa_k-s2^{-s-1}a_k=-\gamma a_k\).

## References

- [OpenAI-CM] OpenAI, *A counterexample to the Monge ansatz for the three-marginal Coulomb cost*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026
- [Lebl] J. Lebl, *Basic Analysis II: Introduction to Real Analysis, Volume II*, open textbook. https://www.jirka.org/ra/
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, author's edition. https://www1.essex.ac.uk/maths/people/fremlin/mt.htm

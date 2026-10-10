# Plurisubharmonic functions and Stein manifolds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cohomology of coherent sheaves vanishes in positive degrees on a large class of complex manifolds, the Stein manifolds. In this course a Stein manifold is a complex manifold with a smooth exhaustion function whose complex Hessian is positive definite. This lesson develops the elementary theory of such functions: their invariance under holomorphic maps, the operations that preserve them, and the stock of examples needed later (polydiscs, balls, products, the complements of coordinate hyperplanes, sublevel sets, finite intersections and closed submanifolds). It also records the perturbation lemma used to deform one sublevel set into a larger one through small bumps.

We use Holomorphic functions of several variables and the chain rule for the operators \(\partial/\partial z_j\) and \(\partial/\partial\bar z_j\).

Basic references are [Demailly] and [Lebl SCV].

## 1. Plurisubharmonic functions

Let \(U\subset\mathbf C^n\) be open and \(v\in\mathcal C^2(U,\mathbf R)\). Its **complex Hessian** (Levi form) at \(z\) is the hermitian form

\[
H_v(z)(\xi)=\sum_{j,k=1}^n\frac{\partial^2v}{\partial z_j\partial\bar z_k}(z)\,\xi_j\bar\xi_k,\qquad\xi\in\mathbf C^n .
\tag{1.1}
\]

The function \(v\) is **plurisubharmonic** if \(H_v(z)\) is positive semidefinite at every point, and **strictly plurisubharmonic** if it is positive definite at every point. Write \(\lambda_v(z)\) for the smallest eigenvalue of \(H_v(z)\) with respect to the standard hermitian form \(|\xi|^2\); it is a continuous function of \(z\). In the language of forms, \(H_v\) corresponds to the real \((1,1)\)-form \(i\partial\bar\partial v=i\sum v_{j\bar k}\,dz_j\wedge d\bar z_k\).

**Lemma 1.1.** Let \(F:U'\to U\) be a holomorphic map between open subsets of \(\mathbf C^m\) and \(\mathbf C^n\). Then \(H_{v\circ F}(w)(\eta)=H_v(F(w))(dF_w\,\eta)\). Hence \(v\circ F\) is plurisubharmonic if \(v\) is, and strictly plurisubharmonic if \(v\) is and \(dF_w\) is injective for all \(w\).

**Proof.** By the chain rule, \(\partial(v\circ F)/\partial\bar w_l=\sum_k(\partial v/\partial\bar z_k)\,\overline{\partial F_k/\partial w_l}\), because \(F\) is holomorphic, and then \(\partial^2(v\circ F)/\partial w_j\partial\bar w_l=\sum_{i,k}v_{i\bar k}\,(\partial F_i/\partial w_j)\,\overline{(\partial F_k/\partial w_l)}\); the term with second derivatives of \(F\) vanishes since \(\partial\bar F_k/\partial w_j=0\). \(\square\)

Consequently plurisubharmonicity is defined on complex manifolds by working in charts. A plurisubharmonic function restricts to a plurisubharmonic function on every complex submanifold, and a strictly plurisubharmonic function to a strictly plurisubharmonic one.

**Lemma 1.2.** Let \(v_1,\ldots,v_s\) be plurisubharmonic and \(\chi\in\mathcal C^2(\mathbf R^s)\) convex and nondecreasing in each variable. Then \(\chi(v_1,\ldots,v_s)\) is plurisubharmonic, and

\[
H_{\chi(v)}=\sum_j\frac{\partial\chi}{\partial t_j}(v)\,H_{v_j}+\sum_{j,k}\frac{\partial^2\chi}{\partial t_j\partial t_k}(v)\,\partial v_j\otimes\overline{\partial v_k}\ \ \geq\ \sum_j\frac{\partial\chi}{\partial t_j}(v)\,H_{v_j}.
\tag{1.2}
\]

In particular, if some \(v_j\) is strictly plurisubharmonic and \(\partial\chi/\partial t_j>0\), the composite is strictly plurisubharmonic.

**Proof.** Differentiate twice with the chain rule; the second sum is the positive semidefinite form \(\xi\mapsto\sum_{j,k}\chi_{jk}\,a_j\bar a_k\) with \(a_j=\sum_l(\partial v_j/\partial z_l)\xi_l\), positive semidefinite because the real symmetric matrix \((\chi_{jk})\) is. \(\square\)

**Examples 1.3.**

1. \(|z|^2\) has \(H=|\xi|^2\), so it is strictly plurisubharmonic; every real-linear function, and the real part of every holomorphic function, has \(H=0\) (pluriharmonic).
2. For a holomorphic function \(f\), \(|f|^2\) is plurisubharmonic, with \(H_{|f|^2}(\xi)=|\partial f(\xi)|^2\).
3. On \(\{|z|<r\}\subset\mathbf C^n\), the function \(-\log(r^2-|z|^2)\) is plurisubharmonic: it is \(\chi(|z|^2)\) with \(\chi(t)=-\log(r^2-t)\) convex increasing on \([0,r^2)\).
4. On \(\mathbf C^*=\mathbf C\setminus\{0\}\), the function \(|z|^{-2}=1/(z\bar z)\) has \(\partial^2/\partial z\partial\bar z\) equal to \(|z|^{-4}>0\).

## 2. Stein manifolds

A real function \(\psi\) on a topological space \(X\) is an **exhaustion function** if every sublevel set \(X_c=\{x:\ \psi(x)<c\}\) is relatively compact in \(X\). An exhaustion function is bounded below, and it tends to \(+\infty\) along every sequence that leaves every compact subset.

**Definition 2.1.** A complex manifold is a **Stein manifold** if it has a smooth strictly plurisubharmonic exhaustion function.

*Reference:* this is the form of the definition used in [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification) and in the lesson [Serre's comparison theorems and Chow's theorem](course:AG-QC/serres-comparison-theorems-and-chows-theorem). H. Grauert proved its equivalence with the classical definition by holomorphic convexity; no result of this course uses that equivalence.

**Proposition 2.2.** Let \(X\) be a complex manifold.

1. Every closed complex submanifold of a Stein manifold is Stein.
2. A product of finitely many Stein manifolds is Stein.
3. If \(\psi\) is a smooth strictly plurisubharmonic exhaustion of \(X\), every sublevel set \(X_c\) is Stein, with the exhaustion \(\psi+1/(c-\psi)\).
4. If \(U_1,\ldots,U_s\subset X\) are open and Stein, so is \(U_1\cap\cdots\cap U_s\).
5. If \(X\) is Stein and \(h\in\mathcal O(X)\), the open set \(\{h\neq0\}\) is Stein.

**Proof.** (1) The restriction of the exhaustion is an exhaustion, since the submanifold is closed, and it is strictly plurisubharmonic by Lemma 1.1. (2) The sum of exhaustion functions of the factors, each pulled back by a projection, is an exhaustion of the product, and its Hessian is the direct sum of the Hessians of the summands, positive definite. (3) The function \(\chi(t)=1/(c-t)\) is convex and increasing on \((-\infty,c)\), so \(\psi+\chi(\psi)\) is strictly plurisubharmonic by Lemma 1.2; it tends to \(+\infty\) at the boundary of \(X_c\) in \(X\) and the closure of \(X_c\) is compact, so it is an exhaustion of \(X_c\). (4) Let \(\psi_i\) be exhaustions of \(U_i\), each bounded below, and put \(\psi=\sum_i\psi_i\) on \(U=\bigcap U_i\); it is strictly plurisubharmonic. For \(C\in\mathbf R\), each set \(K_i=\{x\in U_i:\ \psi_i(x)\leq C\}\) is compact, being closed in the compact closure of \(\{\psi_i<C+1\}\), which lies in \(U_i\). If \(\psi\leq C'\) on a set \(E\subset U\), then each \(\psi_i\) is bounded above on \(E\), by \(C'\) minus the lower bounds of the others, so \(E\) lies in a finite intersection of sets \(K_i\), a compact subset of \(U\). Hence \(\psi\) is an exhaustion of \(U\). (5) \(\{h\neq0\}\) is isomorphic, through \(x\mapsto(x,1/h(x))\), to the closed submanifold \(\{(x,t):\ t\,h(x)=1\}\) of \(X\times\mathbf C\), which is Stein by (1) and (2). \(\square\)

**Examples 2.3.**

1. \(\mathbf C^n\) is Stein, with the exhaustion \(|z|^2\).
2. A ball \(B=\{|z|<r\}\) is Stein, with the exhaustion \(|z|^2-\log(r^2-|z|^2)\) (Example 1.3(3)). A polydisc \(\Delta(r)\) is Stein, with \(\sum_j\bigl(|z_j|^2-\log(r_j^2-|z_j|^2)\bigr)\); a polydisc with some radii infinite is Stein, using \(|z_j|^2\) for those coordinates.
3. Every finite intersection of balls and polydiscs is Stein, by Proposition 2.2(4); every convex open subset of \(\mathbf C^n\) that is a finite intersection of such sets is Stein.
4. The open set \(\{z\in\mathbf C^n:\ z_1\cdots z_a\neq0\}\cong(\mathbf C^*)^a\times\mathbf C^{n-a}\) is Stein, by Proposition 2.2(5) with \(h=z_1\cdots z_a\). In particular the intersections \(U_S=\{T_j\neq0,\ j\in S\}\) of the standard affine charts of complex projective space are Stein: in the chart \(T_{j_0}\neq0\), \(j_0\in S\), the set \(U_S\) is the complement of coordinate hyperplanes in \(\mathbf C^n\).

**Lemma 2.4 (perturbation).** Let \(\psi\) be strictly plurisubharmonic on \(X\) and \(\theta\) a smooth function with compact support. Then \(\psi-\varepsilon\theta\) is strictly plurisubharmonic for all sufficiently small \(\varepsilon>0\). More generally, if \(\theta_1,\ldots,\theta_s\) have compact supports, there is \(\varepsilon_0>0\) such that \(\psi-\sum_j\varepsilon_j\theta_j\) is strictly plurisubharmonic whenever \(0\leq\varepsilon_j\leq\varepsilon_0\).

**Proof.** Cover the compact union of the supports by finitely many coordinate charts and compact subsets \(K_\alpha\) of them. On each \(K_\alpha\), \(\lambda_\psi\geq m_\alpha>0\) by continuity and compactness, and the Hessians of the \(\theta_j\) are bounded by some \(M_\alpha\). If \(s\,\varepsilon_0M_\alpha<m_\alpha\) for all \(\alpha\), the Hessian of \(\psi-\sum\varepsilon_j\theta_j\) is positive definite on the supports; elsewhere it equals that of \(\psi\). \(\square\)

**Lemma 2.5.** If \(\psi\) is a smooth strictly plurisubharmonic exhaustion of \(X\) and \(b<c\), then the closure of \(X_b\) is compact and contained in \(X_c\), and \(\psi\) remains strictly plurisubharmonic on the open set \(X_c\). On the shell \(X_c\setminus X_b\), the relative strict sublevel of its restriction at \(b'\), where \(b<b'<c\), is exactly \(X_{b'}\setminus X_b\). The shell generally is not open.

**Proof.** \(\overline{X_b}\subset\{\psi\leq b\}\subset X_c\), and \(\{\psi\leq b\}\) is closed and contained in the compact closure of \(X_{b+1}\). Restriction to the open set preserves the Levi inequality. Intersecting the shell with \(\{\psi<b'\}\) gives the stated relative sublevel identity. \(\square\)

## 3. Exercises

**Exercise 3.1.** Show that \(v(z)=\log(1+|z|^2)\) is strictly plurisubharmonic on \(\mathbf C^n\), and compute the smallest eigenvalue of its complex Hessian.

*Solution.* \(v_{j\bar k}=\delta_{jk}/(1+|z|^2)-\bar z_jz_k/(1+|z|^2)^2\). For \(\xi\in\mathbf C^n\), \(H_v(\xi)=\bigl((1+|z|^2)|\xi|^2-|\langle\xi,z\rangle|^2\bigr)/(1+|z|^2)^2\geq|\xi|^2/(1+|z|^2)^2\) by Cauchy–Schwarz, with equality when \(\xi\) is parallel to \(z\). The smallest eigenvalue is \((1+|z|^2)^{-2}>0\).

**Exercise 3.2.** Show that \(\mathbf C^2\setminus\{0\}\) has no plurisubharmonic exhaustion function of class \(\mathcal C^2\); in particular it is not Stein.

*Solution.* Suppose \(\psi\) were one. For \(s\neq0\) the closed disc \(D_s=\{(s,t):\ |t|\leq1\}\) lies in \(\mathbf C^2\setminus\{0\}\), and \(t\mapsto\psi(s,t)\) is subharmonic on a neighbourhood of it by Lemma 1.1, so \(\psi(s,0)\leq\max_{|\tau|=1}\psi(s,\tau)\) by the maximum principle for subharmonic functions. As \(s\to0\), the right side tends to \(\max_{|\tau|=1}\psi(0,\tau)\), which is finite because the circle \(\{(0,\tau):|\tau|=1\}\) is compact in \(\mathbf C^2\setminus\{0\}\). The left side tends to \(+\infty\), because \((s,0)\) leaves every compact subset of \(\mathbf C^2\setminus\{0\}\). This is a contradiction. (The Čech computation in The Dolbeault complex, Exercise 4.3 shows \(H^1(\mathbf C^2\setminus\{0\},\mathcal O)\neq0\), consistent with the vanishing theorem proved later for Stein manifolds.)

**Exercise 3.3.** Show that the curve \(X=\{(z,w)\in\mathbf C^2:\ w^2=z^3-z\}\) is a Stein manifold.

*Solution.* The polynomial \(g=w^2-z^3+z\) has \(\partial g/\partial w=2w\) and \(\partial g/\partial z=1-3z^2\). Both vanish together with \(g\) only if \(w=0\), \(z^3=z\) and \(3z^2=1\), which is impossible. So \(X\) is a closed one-dimensional complex submanifold of \(\mathbf C^2\) by the implicit function theorem, and it is Stein by Proposition 2.2(1).

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026). <https://www.jirka.org/scv/>

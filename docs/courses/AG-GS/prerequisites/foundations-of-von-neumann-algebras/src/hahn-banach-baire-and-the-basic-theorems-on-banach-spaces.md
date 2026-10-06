# Hahn–Banach, Baire and the basic theorems on Banach spaces

*Originally written and self-checked by Claude Opus 5.5 (Anthropic), October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all six solutions, supplied the well-ordering and infinite-product proof and corrected the non-Hausdorff example, October 2026. Public domain (CC0).*

The lessons of this course use a small number of theorems about normed spaces again and again. This lesson proves them.

- **Zorn's lemma**, proved here from the axiom of choice.
- **The Hahn–Banach theorem**: the real dominated extension theorem, its complex form, and its consequences for normed spaces.
- **The Baire category theorem**, and from it:
  - the uniform boundedness principle;
  - the open mapping and inverse mapping theorems;
  - the closed graph theorem.
- **Separation of convex sets** in topological vector spaces and in locally convex spaces, and continuity of functionals with closed kernel.
- **Finite-dimensional spaces**: a finite-dimensional Hausdorff topological vector space carries only one vector topology.
- **Cardinal arithmetic**: the Cantor–Schröder–Bernstein theorem, Cantor's theorem, well-ordering, and \(|X\times\mathbb N|=|X\times X|=|X|\) for infinite \(X\).

The next lesson, [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md), builds the weak topologies on these results.

We assume metric spaces and completeness (core courses Real Analysis I and II), and normed spaces, bounded linear maps and their norms (core course Functional Analysis). We assume the axiom of choice. Theorem 1.1 proves Zorn’s lemma from it, and Theorem 8.5 derives the well-ordering principle without a further set-theory import. The core course Functional Analysis states several of the theorems below and gives hints for their proofs. Here every proof is complete.

## Conventions

\(\mathbb K\) is \(\mathbb R\) or \(\mathbb C\). Vector spaces are over \(\mathbb K\) unless a statement says otherwise. For a normed space \(E\):
- \(B_E(x,r)\) and \(\overline B_E(x,r)\) denote the open and closed balls with centre \(x\) and radius \(r\);
- \(E^*\) is the space of bounded linear functionals with the norm \(\|\varphi\|=\sup_{\|x\|\le1}|\varphi(x)|\);
- \(B(E,F)\) is the space of bounded linear maps \(E\to F\) with the operator norm.

A *Banach space* is a complete normed space. For a complex vector space, \(\operatorname{Re}\varphi\) is the real part of a functional \(\varphi\).

## 1. Zorn's lemma

A *chain* in a partially ordered set is a totally ordered subset. An *upper bound* of a subset \(S\) is an element \(u\) with \(s\le u\) for all \(s\in S\). An element \(m\) is *maximal* if \(m\le x\) implies \(x=m\).

**Theorem 1.1** (Zorn's lemma). Let \((P,\le)\) be a nonempty partially ordered set in which every chain has an upper bound. Then \(P\) has a maximal element.

**Proof.** Suppose not. Then every chain \(C\) has an upper bound that is not in \(C\): if \(u\) is an upper bound and \(u\in C\), then \(u\) is the largest element of \(C\). Since \(u\) is not maximal, some \(u'>u\) exists, and \(u'\) is an upper bound outside \(C\). By the axiom of choice there is a function \(g\) assigning to each chain \(C\) an upper bound \(g(C)\notin C\).

Fix \(p_0\in P\). Call a subset \(T\subseteq P\) a *tower* if it satisfies three conditions:
1. \(p_0\in T\);
2. \(T\) is well-ordered by \(\le\): every nonempty subset of \(T\) has a least element, so in particular \(T\) is a chain;
3. for every \(t\in T\), \(t=g(\{s\in T:s<t\})\) when \(t\neq p_0\), and every element of \(T\) is \(\ge p_0\).

*Claim: of two towers, one is an initial segment of the other.* Let \(T,T'\) be towers. Let \(I\) be the set of \(t\in T\cap T'\) such that \(\{s\in T:s<t\}=\{s\in T':s<t\}\) and this set lies in \(T\cap T'\). Then \(I\) is an initial segment of both towers. If \(I\neq T\) and \(I\neq T'\), let \(t\) be least in \(T\setminus I\) and \(t'\) least in \(T'\setminus I\). Then \(\{s\in T:s<t\}=I=\{s\in T':s<t'\}\). If \(I=\varnothing\), then \(t=t'=p_0\), since \(p_0\) is the least element of every tower. Otherwise condition 3 gives \(t=g(I)=t'\). In both cases \(t=t'\in I\), a contradiction. So \(I=T\) or \(I=T'\). This proves the claim.

Let \(U\) be the union of all towers. By the claim, \(U\) is well-ordered and every tower is an initial segment of \(U\), so \(U\) is a tower. Then \(U\cup\{g(U)\}\) is also a tower: \(g(U)\) is an upper bound of \(U\) not in \(U\), so it is the largest element, and condition 3 holds for it. Hence \(g(U)\in U\), contradicting \(g(U)\notin U\). \(\square\)

## 2. The Hahn–Banach theorem

A map \(p:V\to\mathbb R\) on a real vector space is *sublinear* if \(p(x+y)\le p(x)+p(y)\) and \(p(tx)=tp(x)\) for all \(x,y\in V\) and \(t\ge0\). A *seminorm* on a vector space over \(\mathbb K\) is a sublinear map with \(p(\lambda x)=|\lambda|p(x)\) for all scalars \(\lambda\).

**Theorem 2.1** (Hahn–Banach, real form). Let \(V\) be a real vector space, \(p\) a sublinear functional on \(V\), \(M\) a subspace, and \(f:M\to\mathbb R\) linear with \(f\le p\) on \(M\). Then \(f\) extends to a linear \(F:V\to\mathbb R\) with \(F\le p\) on \(V\).

**Proof.** *One step.* Let \(x_0\notin M\) and \(M_1=M+\mathbb Rx_0\). A linear extension \(f_1\) to \(M_1\) is determined by \(c=f_1(x_0)\). The condition \(f_1\le p\) on \(M_1\) says \(f(m)+tc\le p(m+tx_0)\) for all \(m\in M\) and \(t\in\mathbb R\). Dividing by \(|t|\) and using positive homogeneity, this is equivalent to
\[
\begin{gathered}
f(m')-p(m'-x_0)\ \\
\le\ c\ \\
\le\ p(m+x_0)-f(m)\\
\text{for all }m,m'\in M.
\end{gathered}
\tag{2.1}
\]
Such a \(c\) exists because, for all \(m,m'\in M\),
\[
\begin{gathered}
f(m')+f(m)\\
=f(m'+m)\\
\le p(m'+m)\\
\le p(m'-x_0)+p(m+x_0).
\end{gathered}
\]
*Zorn.* Order the pairs \((D,g)\), with \(M\subseteq D\) a subspace and \(g\) a linear extension of \(f\) to \(D\) with \(g\le p\), by extension. A chain has an upper bound: the union of the domains, with the common extension. By Zorn's lemma (Theorem 1.1) there is a maximal pair \((D,g)\). If \(D\neq V\), the one-step extension contradicts maximality. So \(D=V\). \(\square\)

**Theorem 2.2** (Hahn–Banach, seminorm form). Let \(V\) be a vector space over \(\mathbb K\), \(p\) a seminorm on \(V\), \(M\) a subspace, and \(f:M\to\mathbb K\) linear with \(|f|\le p\) on \(M\). Then \(f\) extends to a linear \(F:V\to\mathbb K\) with \(|F|\le p\) on \(V\).

**Proof.** *Real scalars.* Theorem 2.1 gives \(F\le p\). Then \(-F(x)=F(-x)\le p(-x)=p(x)\), so \(|F|\le p\).

*Complex scalars.* Let \(u=\operatorname{Re}f\), a real-linear functional on \(M\) with \(u\le|f|\le p\). By Theorem 2.1, applied to \(V\) as a real space, \(u\) extends to a real-linear \(U\le p\). Put \(F(x)=U(x)-iU(ix)\).
- \(F\) is real-linear and \[
\begin{gathered}
F(ix)\\
=U(ix)-iU(-x)\\
=U(ix)+iU(x)\\
=iF(x),
\end{gathered}
\] so \(F\) is complex-linear.
- \(\operatorname{Re}F=U\). On \(M\), \(f\) and \(F\) have the same real part, hence are equal, since a complex-linear functional is determined by its real part: \(f(x)=\operatorname{Re}f(x)-i\operatorname{Re}f(ix)\).
- Given \(x\), choose \(\theta\) with \(e^{-i\theta}F(x)=|F(x)|\). Then \[
\begin{gathered}
|F(x)|\\
=F(e^{-i\theta}x)\\
=U(e^{-i\theta}x)\\
\le p(e^{-i\theta}x)\\
=p(x).
\end{gathered}
\] \(\square\)

**Corollary 2.3** (normed spaces). Let \(E\) be a normed space.
1. Every \(\varphi\in M^*\), for a subspace \(M\subseteq E\), extends to some \(\Phi\in E^*\) with \(\|\Phi\|=\|\varphi\|\).
2. For every \(x\in E\) there is \(\varphi\in E^*\) with \(\|\varphi\|\le1\) and \(\varphi(x)=\|x\|\); if \(x\ne0\), then \(\|\varphi\|=1\). Hence \(\|x\|=\max_{\|\varphi\|\le1}|\varphi(x)|\), and \(E^*\) separates the points of \(E\).
3. Let \(M\) be a closed subspace and \(x\notin M\), with \(d=\operatorname{dist}(x,M)>0\). Then some \(\varphi\in E^*\) has \(\varphi|_M=0\), \(\varphi(x)=d\) and \(\|\varphi\|=1\). Consequently a subspace is dense exactly when the only bounded functional vanishing on it is \(0\).
4. The canonical map \(j:E\to E^{**}\), \(j(x)(\varphi)=\varphi(x)\), is a linear isometry.

**Proof.** 1. Apply Theorem 2.2 with \(p(y)=\|\varphi\|\,\|y\|\). The extension satisfies \(|\Phi(y)|\le\|\varphi\|\|y\|\), and \(\|\Phi\|\ge\|\varphi\|\) because \(\Phi\) extends \(\varphi\).

2. For \(x=0\) take \(\varphi=0\). Otherwise apply 1 to \(t x\mapsto t\|x\|\) on \(\mathbb Kx\), a functional of norm \(1\). The maximum in the norm formula is attained at this \(\varphi\), and \(|\varphi(x)|\le\|\varphi\|\|x\|\) gives the other inequality.

3. On \(M+\mathbb Kx\) put \(\psi(m+tx)=td\). This is well defined because \(x\notin M\). It satisfies \[
\begin{gathered}
|\psi(m+tx)|\\
=|t|d\\
\le|t|\,\|x+m/t\|\\
=\|m+tx\|
\end{gathered}
\] for \(t\ne0\), so \(\|\psi\|\le1\). Choosing \(m_k\in M\) with \(\|x-m_k\|\to d\) gives \(\psi(x-m_k)=d\), so \(\|\psi\|=1\). Extend by 1. For the consequence: if \(M\) is a subspace that is not dense, apply this to its closure \(\overline M\) and some \(x\notin\overline M\).

4. \(j\) is linear, and \(\|j(x)\|=\sup_{\|\varphi\|\le1}|\varphi(x)|=\|x\|\) by 2. \(\square\)

## 3. The Baire category theorem

**Theorem 3.1** (Baire). Let \((X,d)\) be a nonempty complete metric space, and \((U_n)_{n\ge1}\) a sequence of dense open subsets. Then \(\bigcap_nU_n\) is dense. Equivalently, \(X\) is not a countable union of closed sets with empty interior.

**Proof.** Let \(W\) be a nonempty open set. Since \(U_1\) is dense and open, \(W\cap U_1\) is nonempty and open. Choose \(x_1\) and \(0<r_1<1\) with \(\overline B(x_1,r_1)\subseteq W\cap U_1\).

Inductively, \(B(x_n,r_n)\cap U_{n+1}\) is nonempty and open. Choose \(x_{n+1}\) and \(0<r_{n+1}<r_n/2\) with \(\overline B(x_{n+1},r_{n+1})\subseteq B(x_n,r_n)\cap U_{n+1}\).

For \(m>n\), \(x_m\in B(x_n,r_n)\) and \(r_n<2^{1-n}\), so \((x_n)\) is Cauchy. Let \(x\) be its limit. For each \(n\), the closed ball \(\overline B(x_n,r_n)\) contains \(x_m\) for all \(m\ge n\), hence contains \(x\). So \(x\in W\cap\bigcap_nU_n\).

For the second form: the complement of a closed set with empty interior is a dense open set. If \(X=\bigcup_nF_n\) with each \(F_n\) closed with empty interior, then the dense open sets \(X\setminus F_n\) have empty intersection. This contradicts the first form, since \(X\ne\varnothing\). \(\square\)

## 4. Uniform boundedness

**Lemma 4.1.** If \(E\) is a normed space and \(F\) a Banach space, then \(B(E,F)\) is a Banach space. In particular \(E^*\) is a Banach space for every normed space \(E\).

**Proof.** Let \((T_n)\) be Cauchy. For each \(x\), \(\|T_nx-T_mx\|\le\|T_n-T_m\|\|x\|\), so \((T_nx)\) is Cauchy. Put \(Tx=\lim T_nx\). Then \(T\) is linear. Given \(\varepsilon>0\), choose \(N\) with \(\|T_n-T_m\|\le\varepsilon\) for \(n,m\ge N\). Letting \(m\to\infty\) in \(\|T_nx-T_mx\|\le\varepsilon\|x\|\) gives \(\|(T_n-T)x\|\le\varepsilon\|x\|\) for \(n\ge N\). So \(T_n-T\) is bounded, hence so is \(T\), and \(\|T_n-T\|\le\varepsilon\) for \(n\ge N\). \(\square\)

**Theorem 4.2** (uniform boundedness principle). Let \(E\) be a Banach space, \(F\) a normed space, and \(\mathcal T\subseteq B(E,F)\) a family with \(\sup_{T\in\mathcal T}\|Tx\|<\infty\) for every \(x\in E\). Then \(\sup_{T\in\mathcal T}\|T\|<\infty\).

**Proof.** If \(E=\{0\}\) there is nothing to prove. Put \(F_n=\{x\in E:\|Tx\|\le n\text{ for all }T\in\mathcal T\}\). Each \(F_n\) is closed, as an intersection of closed sets. By hypothesis \(\bigcup_nF_n=E\). By Theorem 3.1 some \(F_N\) contains a closed ball \(\overline B(x_0,r)\) with \(r>0\). For \(\|y\|\le1\), both \(x_0+ry\) and \(x_0\) lie in \(F_N\), so \(r\|Ty\|\le\|T(x_0+ry)\|+\|Tx_0\|\le2N\). Hence \(\|T\|\le2N/r\) for every \(T\in\mathcal T\). \(\square\)

**Corollary 4.3.**
1. Let \(E\) be a Banach space. If \(\varphi_n\in E^*\) and \(\varphi_n(x)\) converges for every \(x\in E\), then \(\sup_n\|\varphi_n\|<\infty\), and \(\varphi(x)=\lim\varphi_n(x)\) defines \(\varphi\in E^*\).
2. Let \(E\) be a normed space and \(S\subseteq E\) with \(\sup_{x\in S}|\varphi(x)|<\infty\) for every \(\varphi\in E^*\). Then \(S\) is norm bounded.
3. Let \(E\) be a Banach space and \(F\) a normed space. If \(T_n\in B(E,F)\) and \(T_nx\) converges for every \(x\), then \(\sup_n\|T_n\|<\infty\), and \(Tx=\lim T_nx\) defines \(T\in B(E,F)\) with \(\|T\|\le\liminf_n\|T_n\|\). In particular, a strongly convergent sequence of operators on a Hilbert space is norm bounded.

**Proof.** 1 and 3. Convergent sequences are bounded, so Theorem 4.2 applies. The limit is linear, and \(\|Tx\|=\lim\|T_nx\|\le\liminf_n\|T_n\|\,\|x\|\).

2. The maps \(j(x)\in E^{**}=B(E^*,\mathbb K)\), \(x\in S\), are pointwise bounded on the Banach space \(E^*\) (Lemma 4.1). By Theorem 4.2 they are bounded in norm, and \(\|j(x)\|=\|x\|\) by Corollary 2.3(4). \(\square\)

**Example 4.4** (completeness cannot be dropped). Let \(c_{00}\) be the space of finitely supported sequences, with the supremum norm, and \(\varphi_n(x)=nx_n\). For each \(x\), \(\varphi_n(x)=0\) once \(n\) exceeds the support of \(x\), so the family is pointwise bounded. But \(\|\varphi_n\|=n\).

## 5. The open mapping and closed graph theorems

**Theorem 5.1** (open mapping). Let \(E,F\) be Banach spaces and \(T\in B(E,F)\) surjective. Then \(T\) maps open sets to open sets. More precisely, there is \(\delta>0\) with \(T(B_E(0,1))\supseteq B_F(0,\delta)\).

**Proof.** *Step 1: a ball in the closure.* Since \(T\) is onto, \(F=\bigcup_n\overline{T(B_E(0,n))}\). By Theorem 3.1 some \(\overline{T(B_E(0,n))}\) contains a ball \(B_F(y_0,\varepsilon)\).

If \(a,b\in\overline{T(B_E(0,n))}\), then \(a-b\in\overline{T(B_E(0,2n))}\): write \(a=\lim Tx_k\) and \(b=\lim Tz_k\) with \(\|x_k\|,\|z_k\|<n\), and note \(\|x_k-z_k\|<2n\). For \(\|y\|<\varepsilon\), write \(y=(y_0+y)-y_0\) with both terms in \(\overline{T(B_E(0,n))}\). So \(B_F(0,\varepsilon)\subseteq\overline{T(B_E(0,2n))}\). By scaling, with \(\eta=\varepsilon/2n\),
\[
\begin{gathered}
B_F(0,\eta r)\\
\subseteq\overline{T(B_E(0,r))}\\
\text{for every }r>0.
\end{gathered}
\tag{5.1}
\]

*Step 2: removing the closure.* Let \(\|y\|<\eta/2\). By (5.1) with \(r=1/2\), choose \(x_1\) with \(\|x_1\|<1/2\) and \(\|y-Tx_1\|<\eta/4\). Inductively, given \(x_1,\dots,x_n\) with \(\|y-T(x_1+\dots+x_n)\|<\eta2^{-n-1}\), apply (5.1) with \(r=2^{-n-1}\). This gives \(x_{n+1}\) with \(\|x_{n+1}\|<2^{-n-1}\) and \(\|y-T(x_1+\dots+x_{n+1})\|<\eta2^{-n-2}\).

The series \(\sum_nx_n\) converges absolutely, so it converges in the Banach space \(E\). Its sum \(x\) satisfies \(\|x\|\le\sum\|x_n\|<1\), and \(Tx=y\) by continuity. So \(B_F(0,\eta/2)\subseteq T(B_E(0,1))\). Take \(\delta=\eta/2\).

*Step 3: open sets.* Let \(U\subseteq E\) be open and \(y=Tx\) with \(x\in U\). Choose \(r>0\) with \(x+B_E(0,r)\subseteq U\). Then \(T(U)\supseteq y+rT(B_E(0,1))\supseteq B_F(y,r\delta)\). \(\square\)

**Corollary 5.2** (inverse mapping). A bijective \(T\in B(E,F)\) between Banach spaces has a bounded inverse. If two complete norms on one vector space satisfy \(\|\cdot\|_1\le C\|\cdot\|_2\), they are equivalent.

**Proof.** By Theorem 5.1, \(\|Tx\|<\delta\) implies \(\|x\|<1\), so \(\|T^{-1}y\|\le\delta^{-1}\|y\|\). For the norms, apply this to the identity map from the second space to the first. \(\square\)

**Theorem 5.3** (closed graph). Let \(T:E\to F\) be linear between Banach spaces, with closed graph \(G=\{(x,Tx):x\in E\}\subseteq E\oplus F\). Then \(T\) is bounded.

**Proof.** Give \(E\oplus F\) the norm \(\|x\|+\|y\|\), a complete norm. The closed subspace \(G\) is then a Banach space. The map \(\pi:G\to E\), \((x,Tx)\mapsto x\), is bounded and bijective. By Corollary 5.2 its inverse is bounded: \(\|x\|+\|Tx\|\le C\|x\|\). \(\square\)

*Remark 5.4.* The proofs of Theorems 3.1, 4.2, 5.1 and 5.3 use only real scalars. So they hold for real Banach spaces, and they apply to conjugate-linear maps between complex Banach spaces, which are real-linear. The lesson on C\*-algebras uses the closed graph theorem in this form.

## 6. Topological vector spaces and separation of convex sets

A *topological vector space* is a vector space with a topology for which addition and scalar multiplication are continuous. It is *locally convex* if its topology is defined by a family \(\mathcal P\) of seminorms: the sets \(\{x:p_i(x-x_0)<\varepsilon,\ i=1,\dots,n\}\), for \(p_1,\dots,p_n\in\mathcal P\) and \(\varepsilon>0\), form a base of neighbourhoods of \(x_0\). These basic neighbourhoods of \(0\) are convex and *balanced*: \(\lambda U\subseteq U\) for \(|\lambda|\le1\). Normed spaces are locally convex. We do not assume a topological vector space to be Hausdorff unless we say so.

**Lemma 6.1** (Minkowski functionals). Let \(U\) be a convex open neighbourhood of \(0\) in a topological vector space \(X\), and \(p_U(x)=\inf\{t>0:x\in tU\}\).
1. \(p_U\) is finite and sublinear.
2. \(U=\{x:p_U(x)<1\}\).
3. \[
\begin{gathered}
|p_U(x)-p_U(y)|\\
\le\max(p_U(x-y),p_U(y-x)),
\end{gathered}
\] and \(p_U<\varepsilon\) on \(\varepsilon U\). So \(p_U\) is continuous.

**Proof.** 1. \(U\) is *absorbing*: for each \(x\), the map \(t\mapsto tx\) is continuous with value \(0\) at \(t=0\), so \(tx\in U\) for small \(t>0\). Hence \(p_U(x)<\infty\). Homogeneity, \(p_U(sx)=sp_U(x)\) for \(s\ge0\), is immediate. Subadditivity follows from convexity: if \(x\in aU\) and \(y\in bU\) with \(a,b>0\), then
\[
\begin{gathered}
x+y\\
=(a+b)\Big(\frac a{a+b}\frac xa+\frac b{a+b}\frac yb\Big)\in(a+b)U.
\end{gathered}
\]

2. If \(x\in U\), then \((1+\varepsilon)x\in U\) for small \(\varepsilon>0\), because \(U\) is open and \(s\mapsto sx\) is continuous. Then \(p_U(x)\le(1+\varepsilon)^{-1}<1\). Conversely, \(p_U(x)<1\) gives \(x\in tU\) for some \(t<1\), and \(tU\subseteq U\) because \(U\) is convex and contains \(0\).

3. Subadditivity gives \(p_U(x)\le p_U(y)+p_U(x-y)\) and \(p_U(y)\le p_U(x)+p_U(y-x)\). If \(x\in\varepsilon U\), then \(p_U(x)\le\varepsilon\cdot p_U(x/\varepsilon)<\varepsilon\) by 2. \(\square\)

**Theorem 6.2** (separation from an open convex set). Let \(X\) be a topological vector space, and \(A,B\subseteq X\) nonempty disjoint convex sets with \(A\) open. Then there are a continuous linear functional \(\varphi\) on \(X\) and \(t\in\mathbb R\) with
\[
\operatorname{Re}\varphi(a)<t\le\operatorname{Re}\varphi(b)\qquad(a\in A,\ b\in B).
\]

**Proof.** *Real scalars.* Fix \(a_0\in A\) and \(b_0\in B\), and put \(x_0=b_0-a_0\) and \(U=A-B+x_0\).
- \(U\) is convex, and open (a union of translates of \(A\)). It contains \(0\).
- \(x_0\notin U\), because \(A\cap B=\varnothing\). So \(p_U(x_0)\ge1\) by Lemma 6.1(2).

Define \(f(sx_0)=s\) on \(\mathbb Rx_0\). Then \(f\le p_U\) there: for \(s\ge0\), \(f(sx_0)=s\le sp_U(x_0)\); for \(s<0\), \(f(sx_0)<0\le p_U(sx_0)\). By Theorem 2.1, \(f\) extends to a linear \(F\le p_U\) on \(X\).

\(F\) is continuous: on the neighbourhood \(U\cap(-U)\) of \(0\) we have \(F<1\) and \(-F(x)=F(-x)<1\), so \(|F|<1\) there, and a linear functional bounded on a neighbourhood of \(0\) is continuous.

For \(a\in A\) and \(b\in B\), \(a-b+x_0\in U\), so \[
\begin{gathered}
F(a)-F(b)+1\\
=F(a-b+x_0)\\
\le p_U(a-b+x_0)<1.
\end{gathered}
\] Hence \(F(a)<F(b)\).

\(F\) is not zero, so it is an open map \(X\to\mathbb R\): \(F(x_1)=1\) for some \(x_1\), and \(F(x+sx_1)=F(x)+s\). So \(F(A)\) is an open interval. Let \(t=\sup F(A)\). Then \(t\le\inf F(B)\), and \(F(a)<t\) for every \(a\in A\), since \(F(A)\) is open.

*Complex scalars.* Apply the real case to \(X\) as a real space, obtaining \(F\). Put \(\varphi(x)=F(x)-iF(ix)\). As in the proof of Theorem 2.2, \(\varphi\) is complex-linear with \(\operatorname{Re}\varphi=F\), and it is continuous. \(\square\)

**Theorem 6.3** (strict separation). Let \(X\) be a locally convex space, \(K\subseteq X\) compact and convex, and \(C\subseteq X\) closed and convex, both nonempty, with \(K\cap C=\varnothing\). Then there are a continuous linear functional \(\varphi\) and numbers \(t_1<t_2\) with \(\operatorname{Re}\varphi<t_1\) on \(K\) and \(\operatorname{Re}\varphi>t_2\) on \(C\).

**Proof.** *A uniform neighbourhood.* For each \(k\in K\), \(X\setminus C\) is a neighbourhood of \(k\). Choose a convex balanced open neighbourhood \(V_k\) of \(0\) with \(k+V_k+V_k\subseteq X\setminus C\); a basic neighbourhood of radius \(\varepsilon/2\) works when \(\{x:p_i(x)<\varepsilon\}\) fits. Finitely many sets \(k_j+V_{k_j}\) cover \(K\). Let \(V=\bigcap_jV_{k_j}\). Then \(K+V\subseteq\bigcup_j(k_j+V_{k_j}+V_{k_j})\) does not meet \(C\).

*Separation.* \(A=K+V\) is convex, open and disjoint from \(C\). Theorem 6.2 gives \(\varphi\) and \(t\) with \(\operatorname{Re}\varphi<t\) on \(A\) and \(\operatorname{Re}\varphi\ge t\) on \(C\). On the compact set \(K\subseteq A\), the continuous function \(\operatorname{Re}\varphi\) attains a maximum \(s<t\). Take \(t_1\) and \(t_2\) with \(s<t_1<t_2<t\). \(\square\)

**Corollary 6.4.** Let \(X\) be a locally convex space.
1. If \(X\) is Hausdorff, its continuous linear functionals separate points.
2. A point \(x\) outside a closed convex set \(C\) is strictly separated from \(C\) by a continuous linear functional.
3. Every continuous linear functional on a subspace \(M\subseteq X\) extends to a continuous linear functional on \(X\).

**Proof.** 1 and 2 are Theorem 6.3 with \(K=\{x\}\), and with \(C=\{y\}\) for 1.

3. If \(\varphi\) is continuous on \(M\), then \(\{m\in M:|\varphi(m)|<1\}\) contains a basic neighbourhood \(\{m\in M:p_i(m)<\varepsilon,\ i\le n\}\). Hence \(|\varphi(m)|\le\varepsilon^{-1}\max_ip_i(m)\) on \(M\): if this failed at some \(m\), a scalar multiple \(m'\) of \(m\) would have \(\max_ip_i(m')<\varepsilon\) and \(|\varphi(m')|\ge1\). The function \(q=\varepsilon^{-1}\max_ip_i\) is a continuous seminorm on \(X\). Theorem 2.2 extends \(\varphi\) to \(\Phi\) with \(|\Phi|\le q\), and \(\Phi\) is continuous. \(\square\)

**Lemma 6.5** (Closed kernels). A linear functional \(f\) on a topological vector space \(X\) is continuous if and only if its kernel is closed.

**Proof.** If \(f\) is continuous, \(\ker f=f^{-1}(0)\) is closed. Conversely, let \(\ker f\) be closed and \(f\neq0\).
- Choose \(x_0\) with \(f(x_0)=1\). The set \(f^{-1}(1)=x_0+\ker f\) is closed and does not contain \(0\), so its complement \(U\) is a neighbourhood of \(0\).
- *A balanced neighbourhood inside \(U\).* By continuity of \((\lambda,x)\mapsto\lambda x\) at \((0,0)\), there are \(\delta>0\) and a neighbourhood \(W_0\) of \(0\) with \(\lambda W_0\subseteq U\) for \(|\lambda|\le\delta\). The set \(V=\bigcup_{0<|\lambda|\le\delta}\lambda W_0\) is a neighbourhood of \(0\), since it contains \(\delta W_0\). It is balanced: \(\mu V\subseteq V\) for \(|\mu|\le1\), with \(0\cdot V=\{0\}\subseteq V\). And \(V\subseteq U\).
- *\(|f|<1\) on \(V\).* If \(v\in V\) had \(|f(v)|\geq1\), then \(v/f(v)\in V\), because \(V\) is balanced, and \(f(v/f(v))=1\). This contradicts \(V\cap f^{-1}(1)=\varnothing\).
- So \(|f|<\varepsilon\) on the neighbourhood \(\varepsilon V\), for every \(\varepsilon>0\), and \(f\) is continuous at \(0\). A linear map that is continuous at \(0\) is continuous. \(\square\)

## 7. Finite-dimensional spaces

**Theorem 7.1.** Let \(X\) be a Hausdorff topological vector space of finite dimension \(n\). Then every linear bijection \(f:\mathbb K^n\to X\) is a homeomorphism, where \(\mathbb K^n\) has its Euclidean topology. Consequently:
1. all Hausdorff vector topologies on a finite-dimensional space coincide;
2. every finite-dimensional subspace of a Hausdorff topological vector space is closed;
3. every linear map from a finite-dimensional Hausdorff topological vector space to a topological vector space is continuous.

**Proof.** \(f\) is continuous, being built from addition and scalar multiplication.

*The inverse is continuous.* The unit sphere \(S\subseteq\mathbb K^n\) is compact, so \(f(S)\) is compact, hence closed in the Hausdorff space \(X\), and \(0\notin f(S)\). The open set \(X\setminus f(S)\) contains a balanced neighbourhood \(W\) of \(0\): continuity of \((\lambda,x)\mapsto\lambda x\) at \((0,0)\) gives \(\delta>0\) and a neighbourhood \(W_0\) with \(\lambda W_0\subseteq X\setminus f(S)\) for \(|\lambda|\le\delta\); take \(W=\bigcup_{|\lambda|\le\delta}\lambda W_0\).

The set \(f^{-1}(W)\) is balanced and disjoint from \(S\). So it lies in the open unit ball: if \(v\in f^{-1}(W)\) with \(|v|\ge1\), then \(v/|v|\in f^{-1}(W)\cap S\). So \(f^{-1}\) maps the neighbourhood \(W\) into the unit ball. A linear map that is bounded on a neighbourhood of \(0\) into a normed space is continuous.

1 follows at once. For 3, compose with \(f\): a linear map on \(\mathbb K^n\) is continuous.

2. Let \(M\) be a finite-dimensional subspace and \(x\in\overline M\). The space \(N=M+\mathbb Kx\) is finite-dimensional. By the main statement its topology is Euclidean, in which subspaces are closed. Every neighbourhood of \(x\) in \(N\) meets \(M\), so \(x\) lies in the closure of \(M\) in \(N\), which is \(M\). \(\square\)

The Hausdorff hypothesis is necessary: with the indiscrete topology, \(\{0\}\) is not closed.

## 8. Cardinal arithmetic

Several lessons count orthonormal bases or projections. They use the following facts. Write \(|X|\leq|Y|\) if there is an injection \(X\to Y\), and \(|X|=|Y|\) if there is a bijection.

**Theorem 8.1** (Cantor–Schröder–Bernstein). If \(|X|\leq|Y|\) and \(|Y|\leq|X|\), then \(|X|=|Y|\).

**Proof.** Let \(f:X\to Y\) and \(g:Y\to X\) be injections. Put \(C_0=X\setminus g(Y)\), \(C_{n+1}=g(f(C_n))\) and \(C=\bigcup_nC_n\). Define \(h(x)=f(x)\) for \(x\in C\), and \(h(x)=g^{-1}(x)\) for \(x\notin C\); this makes sense because \(x\notin C_0\) means \(x\in g(Y)\).
- *\(h\) is injective.* It is injective on \(C\) and on \(X\setminus C\). If \(f(x)=g^{-1}(x')\) with \(x\in C_n\) and \(x'\notin C\), then \(x'=g(f(x))\in C_{n+1}\subseteq C\), a contradiction.
- *\(h\) is surjective.* Let \(y\in Y\). If \(g(y)\notin C\), then \(h(g(y))=y\). If \(g(y)\in C\), then \(g(y)\notin C_0\), so \(g(y)\in C_{n+1}=g(f(C_n))\) for some \(n\). Since \(g\) is injective, \(y=f(x)\) with \(x\in C_n\), and \(h(x)=y\). \(\square\)

**Theorem 8.2** (Cantor). For every set \(X\), \(|X|\leq|\mathcal P(X)|\) and \(|X|\neq|\mathcal P(X)|\).

**Proof.** \(x\mapsto\{x\}\) is an injection. If \(F:X\to\mathcal P(X)\) is any map, the set \(D=\{x:x\notin F(x)\}\) is not in its range: \(D=F(x)\) would give \(x\in D\iff x\notin D\). \(\square\)

**Proposition 8.3** (Exponents). For sets \(X,Y,Z\), the map that sends \(F:Y\times Z\to X\) to \(z\mapsto F(\cdot,z)\) is a bijection from \(X^{Y\times Z}\) onto \((X^Y)^Z\). The map \((m,n)\mapsto2^m(2n+1)-1\) is a bijection \(\mathbb N\times\mathbb N\to\mathbb N\). Consequently \(|(\{0,1\}^{\mathbb N})^{\mathbb N}|=|\{0,1\}^{\mathbb N}|\), that is, \((2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}\).

**Proof.** The inverse of the first map sends \(G\) to \((y,z)\mapsto G(z)(y)\). Every positive integer is uniquely \(2^m\) times an odd number \(2n+1\). \(\square\)

**Theorem 8.4.** Let \(X\) be an infinite set. Then:
1. \(|X\times\mathbb N|=|X|\);
2. \(|X\times\{0,1\}|=|X|\);
3. if \((A_i)_{i\in I}\) is a family of countable sets indexed by an infinite set \(I\), then \(|\bigcup_iA_i|\leq|I|\).

**Proof.** *\(X\) has a countably infinite subset.* Injections from initial segments \(\{0,\dots,n-1\}\) or from \(\mathbb N\) into \(X\), ordered by extension, satisfy the hypothesis of Zorn's lemma: the union of a chain is an upper bound. A maximal one is defined on all of \(\mathbb N\), because a finite one can be extended by a point outside its finite range.

(1) Let \(P\) be the set of pairs \((A,\varphi)\) with \(A\subseteq X\) and \(\varphi:A\times\mathbb N\to A\) a bijection, ordered by \((A,\varphi)\leq(A',\varphi')\) if \(A\subseteq A'\) and \(\varphi'\) extends \(\varphi\).
- \(P\) is nonempty: a countably infinite \(A_0\subseteq X\) has \(|A_0\times\mathbb N|=|A_0|\) by Proposition 8.3.
- The union of a chain is an upper bound.
- Let \((A,\varphi)\) be maximal (Zorn's lemma). If \(X\setminus A\) were infinite, it would contain a countably infinite \(B\), and a bijection \(B\times\mathbb N\to B\) would extend \(\varphi\) to \(A\cup B\). So \(X\setminus A\) is finite.
- An infinite set \(A\) absorbs a finite set \(F\) disjoint from it: choose distinct \(c_0,c_1,\ldots\) in \(A\) and \(F=\{f_1,\dots,f_k\}\); the map sending \(f_j\mapsto c_{j-1}\), \(c_n\mapsto c_{n+k}\), and fixing the rest of \(A\), is a bijection \(A\cup F\to A\).
- \(A\) is infinite, since \(X\) is infinite and \(X\setminus A\) is finite. So \(|X|=|A|\). A bijection \(X\to A\) induces a bijection \(X\times\mathbb N\to A\times\mathbb N\). Hence \(|X\times\mathbb N|=|A\times\mathbb N|=|A|=|X|\).

(2) \(X\) injects into \(X\times\{0,1\}\), which injects into \(X\times\mathbb N\). Apply (1) and Theorem 8.1.

(3) By the axiom of choice, choose for each \(i\) a surjection \(s_i:\mathbb N\to A_i\) (for \(A_i=\varnothing\), skip \(i\)). The map \((i,n)\mapsto s_i(n)\) is a surjection from a subset of \(I\times\mathbb N\) onto \(\bigcup_iA_i\). Choosing one preimage for each point gives an injection of \(\bigcup_iA_i\) into \(I\times\mathbb N\), and \(|I\times\mathbb N|=|I|\) by (1). \(\square\)

### Well-ordering and infinite products

**Theorem 8.5.** Every set can be well-ordered. If \(X\) is infinite, then \(|X\times X|=|X|\). Consequently, if \(0<|Y|\leq|X|\), then \(|X\times Y|=|X|\). In particular an uncountable set can be partitioned into uncountably many subsets, each in bijection with the whole set.

*Proof.* A *well-order* is a linear order in which every nonempty subset has a least member. Order the well-orders on subsets of \(X\) by extension as an initial segment: an extension may append elements, but may not insert elements before an old element. The union of a chain is again a well-order. To see this, take a member \(a\) of a nonempty subset \(S\) of the union and a chain member containing \(a\). All predecessors of \(a\) in the union already lie in that member. The nonempty set of elements of \(S\) at or before \(a\) therefore has a least member there, which is least in all of \(S\). Zorn's lemma gives a maximal such well-order. If its domain omitted a point of \(X\), appending that point would extend it. Its domain is therefore \(X\).

Here are the order-type facts needed to count the square. Two well-orders have at most one order isomorphism between initial segments: if two such maps first differ at \(a\), their common image of the predecessors of \(a\) determines the least unused image of \(a\), a contradiction. Take the union of all these initial-segment isomorphisms for two well-orders. They are compatible by uniqueness, and their union has initial-segment domains and ranges. If neither order were exhausted, mapping the least remaining point of one to the least remaining point of the other would extend the union. Thus one order is isomorphic to an initial segment of the other.

A well-order cannot be isomorphic to a proper initial segment of itself. Indeed, suppose \(f\) is such an isomorphism and \(a\) is the first point with \(f(a)\ne a\). The predecessors of \(a\) are fixed, so order preservation forces \(f(a)\geq a\). Equality is excluded, and \(f(a)>a\) would omit \(a\) from the initial-segment range. If there is no such \(a\), the range is the whole order. These contradictions prove the assertion. Hence order types are linearly ordered by proper initial-segment inclusion.

Every nonempty set of order types has a least one. Pick a type \(\tau\) in it. If there are types below \(\tau\), identify them with proper initial segments of a representative of \(\tau\). Their endpoint set has a least member, giving the least type below \(\tau\). If there are none, \(\tau\) itself is least. An *initial order type*, or cardinal, is the least type of a well-order on a set of its given cardinality. Such a least type exists, since the orders on that set form a set. Injections respect cardinal types: if \(A\) injects into \(B\) but its cardinal type were larger, the type of \(B\) would be an initial segment of that of \(A\), giving an injection in the other direction. Cantor–Schröder–Bernstein would make their cardinalities, and hence their least types, equal. Every proper initial segment of an initial type \(\kappa\) therefore has cardinality less than \(\kappa\): equality would give a smaller well-order of the same set. No infinite initial type has a last point, because an infinite set absorbs one extra point by the explicit shifting bijection in the proof of Theorem 8.4.

Suppose now that an infinite cardinal fails the square identity, and take the least such \(\kappa\). This choice is legitimate within a set: below any proposed counterexample, all smaller cardinal types are represented by well-orders on subsets of that counterexample. Represent \(\kappa\) by its initial well-order. Order pairs \((\alpha,\beta)\) first by \(\max(\alpha,\beta)\), then by \(\alpha\), then by \(\beta\). This is a well-order: a nonempty collection of pairs has a least maximum, a least first coordinate among pairs with that maximum, and then a least second coordinate.

The predecessors of a pair with maximum \(\gamma\) are contained in the square of the initial segment through \(\gamma\). That segment is proper, since \(\kappa\) has no last point. Its cardinal \(\mu\) is less than \(\kappa\). If \(\mu\) is finite, its square is finite; if \(\mu\) is infinite, minimality of \(\kappa\) gives \(\mu^2=\mu\). Thus every predecessor set in the pair order has cardinality less than \(\kappa\).

Let \(\tau\) be the type of this pair order. If \(\tau>\kappa\), comparison of well-orders embeds \(\kappa\) as a proper initial segment of it. The least point outside that segment then has \(\kappa\) predecessors, a contradiction. Thus \(\tau\leq\kappa\), giving \(|\kappa\times\kappa|\leq\kappa\). The map \(\alpha\mapsto(\alpha,\alpha)\) gives the reverse inequality, so Cantor–Schröder–Bernstein proves the square identity. This contradicts the choice of \(\kappa\), and proves the identity for every infinite set.

For nonempty \(Y\) with an injection into \(X\), choose \(y_0\in Y\). The maps \(x\mapsto(x,y_0)\) and the coordinate injection into \(X\times X\) give
\[
|X|\leq|X\times Y|\leq|X\times X|=|X|.
\]
Apply Cantor–Schröder–Bernstein again. Finally, choose a bijection \(b:X\times X\to X\). The sets \(b(X\times\{y\})\), \(y\in X\), partition \(X\) and each is in bijection with \(X\). If \(X\) is uncountable, their index set is uncountable. \(\square\)

## Exercises

**Exercise 1** (medium; two complete norms). Let \(\|\cdot\|_1\) and \(\|\cdot\|_2\) be complete norms on a vector space \(V\) with \(\|v\|_1\le C\|v\|_2\) for all \(v\). Show that the norms are equivalent. Show by example that completeness of both norms is needed.

*Solution.* Equivalence is Corollary 5.2. For an example in which the weaker norm is incomplete, take \(V=C[0,1]\) with \(\|\cdot\|_1\) the \(L^1\) norm and \(\|\cdot\|_2\) the supremum norm. Then \(\|f\|_1\le\|f\|_2\), and \(\|\cdot\|_2\) is complete. The functions \(f_n(t)=\max(0,1-nt)\) have \(\|f_n\|_2=1\) and \(\|f_n\|_1=1/(2n)\), so the norms are not equivalent. If \(\|\cdot\|_1\) were complete on \(C[0,1]\), Corollary 5.2 would contradict these norm ratios, so it is incomplete. For the other completeness assumption, retain \(V=C[0,1]\) with complete norm \(\|f\|_1=\|f\|_\infty\). The completeness follows because a uniformly Cauchy sequence has a uniform limit, and uniform limits of continuous functions are continuous. On the polynomial subspace define \(u_0(p)=p'(1)\). It has a linear extension \(u\) to all of \(V\): order algebraic extensions by inclusion, take unions along chains, and use Zorn; if a maximal domain omitted \(f\), extend by \(u(d+\lambda f)=u(d)\), a contradiction. Define \(\|f\|_2=\|f\|_\infty+|u(f)|\), a norm dominating \(\|f\|_1\). For \(f_n(t)=t^n\), \(\|f_n\|_1=1\) and \(\|f_n\|_2=1+n\), so the norms are not equivalent. If \(\|\cdot\|_2\) were complete, Corollary 5.2 would again give equivalence. Thus this stronger norm is incomplete while the weaker one is complete. \(\square\)

**Exercise 2** (medium; Banach limits). Let \(\ell^\infty_{\mathbb R}\) be the real space of bounded real sequences and \(S\) the shift, \((Sx)_n=x_{n+1}\). Show that there is a linear \(L:\ell^\infty_{\mathbb R}\to\mathbb R\) with \(\liminf_nx_n\le L(x)\le\limsup_nx_n\) and \(L(Sx)=L(x)\) for all \(x\).

*Solution.* Put \(p(x)=\limsup_n\frac1n\sum_{k=1}^nx_k\).
- *\(p\) is sublinear:* the averages are linear in \(x\), and \(\limsup\) is subadditive and positively homogeneous.
- Theorem 2.1 extends \(0\) on the subspace \(\{0\}\) to a linear \(L\le p\).
- *Bounds:* \(p(x)\le\limsup_nx_n\), because averages of a sequence eventually below \(c+\varepsilon\) are eventually below \(c+2\varepsilon\). Applying this to \(-x\) gives \(L(x)=-L(-x)\ge-p(-x)\ge\liminf_nx_n\).
- *Shift invariance:* \(\frac1n\sum_{k\le n}(Sx-x)_k=\frac{x_{n+1}-x_1}n\to0\). So \(p(Sx-x)=0\) and \(p(x-Sx)=0\). Hence \(L(Sx-x)\le0\) and \(L(x-Sx)\le0\), that is, \(L(Sx)=L(x)\). \(\square\)

**Exercise 3** (easy; closed convex sets are intersections of half-spaces). Let \(E\) be a normed space and \(C\subseteq E\) closed and convex. Show that \(C\) is the intersection of the sets \(\{x:\operatorname{Re}\varphi(x)\le t\}\), over all \(\varphi\in E^*\) and \(t\in\mathbb R\) with \(C\subseteq\{\operatorname{Re}\varphi\le t\}\).

*Solution.* The intersection contains \(C\). If \(x\notin C\) and \(C\) is nonempty, Corollary 6.4(2) gives \(\varphi\) and \(t\) with \(\operatorname{Re}\varphi\le t\) on \(C\) and \(\operatorname{Re}\varphi(x)>t\). So \(x\) is not in the intersection. If \(C=\varnothing\), use \(\varphi=0\) and \(t=-1\). \(\square\)

**Exercise 4** (medium; weakly continuous implies bounded). Let \(T:E\to F\) be linear between Banach spaces, with \(\psi\circ T\in E^*\) for every \(\psi\in F^*\). Show that \(T\) is bounded.

*Solution.* By Theorem 5.3 it suffices to show that the graph is closed. Let \(x_n\to x\) and \(Tx_n\to y\). For \(\psi\in F^*\), \(\psi(Tx_n)\to\psi(Tx)\) because \(\psi\circ T\) is continuous, and \(\psi(Tx_n)\to\psi(y)\). So \(\psi(Tx)=\psi(y)\) for all \(\psi\), and \(Tx=y\) by Corollary 2.3(2). \(\square\)

**Exercise 5** (medium; quotients). Let \(E\) be a Banach space and \(M\) a closed subspace. Show that \(\|x+M\|=\operatorname{dist}(x,M)\) is a complete norm on \(E/M\). Deduce that a bounded linear surjection \(T:E\to F\) onto a normed space \(F\) that is open forces \(F\) to be complete.

*Solution.*
- *A norm:* translating a representative by a member of \(M\) does not change the infimum. Nonzero-scalar representatives are scalar multiples of the old representatives, giving homogeneity. Taking the two independent infima in \[
\begin{gathered}
\|(x+m)+(y+n)\|\\
\leq\|x+m\|+\|y+n\|
\end{gathered}
\] gives the triangle inequality. Finally, \(\|x+M\|=0\) means \(x\in\overline M=M\).
- *Completeness:* a normed space in which every absolutely convergent series converges is complete. From a Cauchy sequence choose a subsequence with successive distances at most \(2^{-k}\); the series of its differences converges, hence the subsequence converges by telescoping and the original Cauchy sequence has the same limit. Let \(\sum\|x_n+M\|<\infty\). Choose representatives with \(\|x_n\|\le\|x_n+M\|+2^{-n}\). Then \(\sum x_n\) converges in \(E\) to some \(x\), and \[
\begin{gathered}
\|\sum_{n\le N}x_n+M-(x+M)\|\\
\le\|\sum_{n>N}x_n\|\to0.
\end{gathered}
\]
- *The deduction:* if \(T\) is open, then \(T(B_E(0,1))\supseteq B_F(0,\delta)\), so the induced bijection \(\tilde T:E/\ker T\to F\) has \(\|\tilde T^{-1}y\|\le\delta^{-1}\|y\|\). Hence \(\tilde T\) is an isomorphism of normed spaces, and \(F\) is complete because \(E/\ker T\) is. \(\square\)

**Exercise 6** (easy; an indiscrete example). Give a vector space with a vector topology in which a one-dimensional subspace is not closed, and explain which step of Theorem 7.1 fails.

*Solution.* Give \(\mathbb K^2\) the indiscrete topology, whose only open sets are the empty set and the whole space. Addition and scalar multiplication into this space are continuous because every map into an indiscrete space is continuous. Every proper nonzero one-dimensional subspace is dense and is not closed: the only closed sets are the empty set and the whole space. For a linear bijection \(f:\mathbb K^2\to X\), the image \(f(S)\) of the Euclidean unit sphere is compact, but it is a nonempty proper subset and hence is not closed. The only neighbourhood of zero is \(X\), so none can avoid \(f(S)\). This is exactly the compact-implies-closed and avoiding-neighbourhood step of Theorem 7.1 that needs Hausdorffness. \(\square\)

## Where this leads

- Weak and weak\* topologies, Banach–Alaoglu, Krein–Milman and Eberlein–Šmulian: [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md).
- Hilbert spaces and compact operators: Hilbert spaces and compact operators.
- Banach algebras: Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory.

## References

The results are classical: Hahn (1927) and Banach (1929) for the extension theorem, Baire (1899), Banach and Steinhaus (1927), Banach and Schauder for the open mapping theorem, and Zorn (1935) for the maximality principle. Readers who want a single textbook account can use the core course Functional Analysis (J. M. Erdman, *Functional Analysis and Operator Algebras: An Introduction*, CC BY-SA 4.0), which states these theorems with hints for their proofs.

*Freely accessible reading:* [J. van Neerven, *Functional Analysis*, §§4.2 and 5.1–5.3](https://arxiv.org/pdf/2112.11166v7) gives a route through Hahn–Banach, separation, Baire and the basic Banach-space theorems. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

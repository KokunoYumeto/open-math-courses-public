# The Dolbeault complex

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a complex manifold, differential forms split by type, and the exterior derivative splits as \(d=\partial+\bar\partial\). The \(\bar\partial\)-operator is the Cauchy–Riemann operator in all degrees: a function is holomorphic exactly when \(\bar\partial f=0\). This lesson proves that \(\bar\partial\)-closed forms are locally \(\bar\partial\)-exact (the Dolbeault–Grothendieck lemma), so that smooth forms of type \((p,\bullet)\) form a resolution of the sheaf of holomorphic \(p\)-forms by sheaves without higher cohomology. The resulting Dolbeault isomorphism computes the cohomology of holomorphic vector bundles by solving \(\bar\partial\)-equations, and it is the bridge to the \(L^2\) methods of the next lessons.

We use [Holomorphic functions of several variables](holomorphic-functions-of-several-variables.md) and the Cauchy–Pompeiu formula of one variable [Complex Analysis, Theorem 4.6.3] from the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). Smooth partitions of unity are [Local tools for bundles and transport, Theorem 3.1](course:DG-FND/local-tools-for-bundles-and-transport#3-smooth-weights-with-controlled-support). The homological facts used are: cohomology of sheaves of modules on a ringed space and Čech cohomology [Cohomology of sheaves on ringed spaces](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces); a sheaf whose Čech cohomology vanishes for every open covering of every open set has no higher cohomology on any open set [Stacks, Tag 01EV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-vanish); and a resolution by acyclic sheaves computes cohomology [Stacks, Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity).

Basic references are [Demailly] and [Lebl SCV].

## 1. Forms of type \((p,q)\)

Let \(X\) be a complex manifold of dimension \(n\). In local holomorphic coordinates \(z_j=x_j+iy_j\), the complex-valued \(1\)-forms are spanned by \(dz_j=dx_j+i\,dy_j\) and \(d\bar z_j=dx_j-i\,dy_j\). A smooth complex-valued \(k\)-form is uniquely a sum of forms of **type \((p,q)\)**, \(p+q=k\),

\[
f=\sum_{|I|=p,\ |J|=q}f_{I,J}\,dz_I\wedge d\bar z_J ,
\tag{1.1}
\]

with increasing multi-indices \(I,J\). The type decomposition does not depend on the coordinates, because a holomorphic change of coordinates expresses the new \(dz_j\) in terms of the old \(dz_k\) only. Write \(\mathcal E^{p,q}\) for the sheaf of smooth \((p,q)\)-forms. For a function, \(df=\partial f+\bar\partial f\) with \(\partial f=\sum(\partial f/\partial z_j)\,dz_j\) and \(\bar\partial f=\sum(\partial f/\partial\bar z_j)\,d\bar z_j\). On forms, \(\bar\partial\) acts on coefficients:

\[
\bar\partial\Bigl(\sum f_{I,J}\,dz_I\wedge d\bar z_J\Bigr)=\sum_{I,J}\sum_{l=1}^n\frac{\partial f_{I,J}}{\partial\bar z_l}\,d\bar z_l\wedge dz_I\wedge d\bar z_J ,
\tag{1.2}
\]

a map \(\mathcal E^{p,q}\to\mathcal E^{p,q+1}\). Since the operators \(\partial/\partial\bar z_l\) commute, \(\bar\partial\circ\bar\partial=0\); and \(\bar\partial(f\wedge g)=\bar\partial f\wedge g+(-1)^{\deg f}f\wedge\bar\partial g\). By [Holomorphic functions of several variables, Proposition 2.2](holomorphic-functions-of-several-variables.md#2-power-series-and-the-regularity-of-holomorphic-functions), a \((p,0)\)-form satisfies \(\bar\partial f=0\) exactly when its coefficients are holomorphic; such forms are the **holomorphic \(p\)-forms**, and they form the sheaf \(\Omega^p\), with \(\Omega^0=\mathcal O\).

Let \(E\) be a holomorphic vector bundle of rank \(r\) on \(X\), with sheaf of holomorphic sections \(\mathcal O(E)\). Smooth \((p,q)\)-forms with values in \(E\) form a sheaf \(\mathcal E^{p,q}(E)\). In a local holomorphic frame \(e_1,\ldots,e_r\), such a form is \(\sum_\nu f_\nu\otimes e_\nu\) with \(f_\nu\in\mathcal E^{p,q}\), and \(\bar\partial_E(\sum f_\nu\otimes e_\nu)=\sum\bar\partial f_\nu\otimes e_\nu\). This is independent of the frame because the transition matrices between holomorphic frames are holomorphic, hence annihilated by \(\bar\partial\). Again \(\bar\partial_E^2=0\), and \(\Omega^p(E)=\ker(\bar\partial_E:\mathcal E^{p,0}(E)\to\mathcal E^{p,1}(E))\).

## 2. The Dolbeault–Grothendieck lemma

**Lemma 2.1 (the \(\bar\partial\)-equation in one variable).** Let \(W\subset\mathbf R^m\) be open and let \(g(\zeta,w)\) be a smooth function on \(\mathbf C\times W\) whose support meets each set \(\mathbf C\times K\), \(K\subset W\) compact, in a compact set. Put

\[
u(z,w)=-\frac1\pi\int_{\mathbf C}\frac{g(\zeta,w)}{\zeta-z}\,dA(\zeta).
\tag{2.1}
\]

Then \(u\) is smooth and \(\partial u/\partial\bar z=g\). If \(g\) depends holomorphically on further complex parameters, so does \(u\).

**Proof.** Substituting \(\zeta=z+\eta\), \(u(z,w)=-\frac1\pi\int g(z+\eta,w)\,\eta^{-1}\,dA(\eta)\). The kernel \(1/\eta\) is integrable on bounded sets and \(g\) is smooth with locally uniformly compact support, so derivatives of every order in \((z,w)\) may be taken under the integral sign; \(u\) is smooth, and holomorphic in any further parameters in which \(g\) is. Moreover

\[
\frac{\partial u}{\partial\bar z}(z,w)=-\frac1\pi\int\frac{\partial g}{\partial\bar\zeta}(z+\eta,w)\,\frac{dA(\eta)}{\eta}=-\frac1\pi\int\frac{\partial g/\partial\bar\zeta\,(\zeta,w)}{\zeta-z}\,dA(\zeta)=g(z,w),
\]

the last equality by the Cauchy–Pompeiu formula [Complex Analysis, Theorem 4.6.3] applied to \(g(\cdot,w)\) on a disc containing its support, where the boundary integral vanishes. \(\square\)

For radii \(R=(R_1,\ldots,R_n)\) with \(0<R_j\leq\infty\) let \(\Delta(R)=\{|z_j|<R_j\}\).

**Theorem 2.2 (Dolbeault–Grothendieck lemma).** Let \(f\) be a smooth \(\bar\partial\)-closed \((p,q)\)-form on \(\Delta(R)\), with \(q\geq1\). For every \(r=(r_1,\ldots,r_n)\) with \(r_j<R_j\) there is a smooth \((p,q-1)\)-form \(u\) on \(\Delta(r)\) with \(\bar\partial u=f\) there.

**Proof.** Since \(\bar\partial\) acts on the coefficients of \(dz_I\), it suffices to treat \(p=0\). We prove by induction on \(k\) the statement: *if a \(\bar\partial\)-closed \((0,q)\)-form \(f\) on \(\Delta(R)\), \(q\geq1\), involves only \(d\bar z_1,\ldots,d\bar z_k\), then for all \(r<R\) it is \(\bar\partial\)-exact on \(\Delta(r)\).* For \(k=0\) such a form is zero. Let \(k\geq1\) and write \(f=d\bar z_k\wedge g+h\), where \(g\) and \(h\) involve only \(d\bar z_1,\ldots,d\bar z_{k-1}\). For \(l>k\), the coefficient of \(d\bar z_l\wedge d\bar z_k\wedge d\bar z_J\) in \(\bar\partial f\) is \(\partial g_J/\partial\bar z_l\), and similarly for \(h\); since \(\bar\partial f=0\), the coefficients of \(g\) and \(h\) are holomorphic in \(z_{k+1},\ldots,z_n\).

Choose \(r'\) with \(r<r'<R\) and a smooth function \(\psi\) of \(z_k\) alone, equal to \(1\) for \(|z_k|\leq r'_k\) and with compact support in \(|z_k|<R_k\). For each coefficient \(g_J\) put

\[
G_J(z)=-\frac1\pi\int_{\mathbf C}\frac{\psi(\zeta)\,g_J(z_1,\ldots,z_{k-1},\zeta,z_{k+1},\ldots,z_n)}{\zeta-z_k}\,dA(\zeta),
\qquad G=\sum_JG_J\,d\bar z_J .
\]

By Lemma 2.1, with \(z_k\) as the variable and the other coordinates as parameters, \(G\) is smooth on \(\Delta(R)\) with \(|z_j|<R_j\) for \(j\neq k\) (and \(z_k\in\mathbf C\)), holomorphic in \(z_{k+1},\ldots,z_n\), and \(\partial G_J/\partial\bar z_k=\psi g_J=g_J\) where \(|z_k|<r'_k\). Hence on \(\Delta(r')\),

\[
\bar\partial G=\sum_J\sum_{l\leq k}\frac{\partial G_J}{\partial\bar z_l}\,d\bar z_l\wedge d\bar z_J=d\bar z_k\wedge g+(\text{terms involving only }d\bar z_1,\ldots,d\bar z_{k-1}),
\]

so \(f-\bar\partial G\) is \(\bar\partial\)-closed on \(\Delta(r')\) and involves only \(d\bar z_1,\ldots,d\bar z_{k-1}\). By the induction hypothesis, applied on \(\Delta(r')\), there is \(v\) on \(\Delta(r)\) with \(\bar\partial v=f-\bar\partial G\), and \(u=v+G\) solves \(\bar\partial u=f\) on \(\Delta(r)\). \(\square\)

*Reference:* the induction is due to Grothendieck; [Demailly] and [Lebl SCV] give the same argument.

**Corollary 2.3.** For every holomorphic vector bundle \(E\) on \(X\) and every \(p\), the sequence of sheaves

\[
0\longrightarrow\Omega^p(E)\longrightarrow\mathcal E^{p,0}(E)\xrightarrow{\ \bar\partial_E\ }\mathcal E^{p,1}(E)\xrightarrow{\ \bar\partial_E\ }\cdots\xrightarrow{\ \bar\partial_E\ }\mathcal E^{p,n}(E)\longrightarrow0
\tag{2.2}
\]

is exact.

**Proof.** Exactness at \(\mathcal E^{p,0}(E)\) is the description of \(\Omega^p(E)\) as a kernel. Exactness at \(\mathcal E^{p,q}(E)\), \(q\geq1\), is a statement about germs: near a point, use a holomorphic frame and a coordinate polydisc, and apply Theorem 2.2 componentwise. \(\square\)

## 3. Fine sheaves and the Dolbeault isomorphism

**Lemma 3.1.** Let \(\mathcal F\) be a sheaf of modules over the sheaf \(\mathcal C^\infty_X\) of smooth complex functions on a manifold \(X\). Then \(H^k(U,\mathcal F)=0\) for every open set \(U\subset X\) and every \(k\geq1\). In particular this holds for every \(\mathcal E^{p,q}(E)\).

**Proof.** Let \(\mathcal U=(U_i)\) be an open covering of an open set \(U\), and choose a smooth partition of unity \((\chi_i)\) on \(U\) subordinate to it, with locally finite supports. For a Čech cochain \(c=(c_{i_0\ldots i_k})\), \(k\geq1\), define \((hc)_{i_0\ldots i_{k-1}}=\sum_i\chi_i\,c_{i\,i_0\ldots i_{k-1}}\), where \(\chi_ic_{i\,i_0\ldots i_{k-1}}\), defined on \(U_{i\,i_0\ldots i_{k-1}}\), is extended by zero to \(U_{i_0\ldots i_{k-1}}\); this extension is a section because the support of \(\chi_i\) is closed in \(U\) and contained in \(U_i\). The usual computation gives \(dh+hd=\mathrm{id}\) on cochains of degree \(k\geq1\), so the Čech cohomology \(\check H^k(\mathcal U,\mathcal F)\) vanishes for \(k\geq1\). By [Stacks, Tag 01EV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-vanish), \(H^k(U,\mathcal F)=0\) for every open \(U\) and \(k\geq1\). \(\square\)

**Theorem 3.2 (Dolbeault isomorphism).** For every holomorphic vector bundle \(E\) on a complex manifold \(X\), all \(p\) and \(q\), and every open \(U\subset X\),

\[
H^q(U,\Omega^p(E))\ \cong\ \frac{\ker\bigl(\bar\partial_E:\mathcal E^{p,q}(U,E)\to\mathcal E^{p,q+1}(U,E)\bigr)}{\bar\partial_E\,\mathcal E^{p,q-1}(U,E)} .
\tag{3.1}
\]

**Proof.** By Corollary 2.3 and Lemma 3.1, (2.2) restricted to \(U\) is a resolution of \(\Omega^p(E)\) by sheaves without higher cohomology, and such a resolution computes cohomology [Stacks, Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity). \(\square\)

**Corollary 3.3.** For every holomorphic vector bundle \(E\) on an \(n\)-dimensional complex manifold, \(H^q(X,\mathcal O(E))=0\) for \(q>n\).

**Proof.** There are no nonzero \((0,q)\)-forms for \(q>n\). \(\square\)

**Corollary 3.4.** On every polydisc \(\Delta(R)\), \(0<R_j\leq\infty\), and for \(q\geq1\), every class in \(H^q(\Delta(R),\mathcal O)\) restricts to zero on every smaller polydisc \(\Delta(r)\), \(r<R\).

**Proof.** Represent the class by a \(\bar\partial\)-closed \((0,q)\)-form by Theorem 3.2 and apply Theorem 2.2. \(\square\)

The full vanishing \(H^q(\Delta(R),\mathcal O)=0\), and much more, is proved in the lesson on Theorems A and B, where polydiscs appear as examples of Stein manifolds.

## 4. Exercises

**Exercise 4.1.** On \(\mathbf C\), find a smooth solution of \(\partial u/\partial\bar z=z\bar z\), and describe all solutions on a connected open set.

*Solution.* \(u_0=z\bar z^2/2\) works, since \(\partial(\bar z^2)/\partial\bar z=2\bar z\). Two solutions differ by a function with \(\partial/\partial\bar z\) equal to zero, that is, by a holomorphic function; so the solutions on a connected open set are \(u_0+h\) with \(h\) holomorphic.

**Exercise 4.2.** Let \(f=g\,d\bar z_1\) be a smooth \((0,1)\)-form on \(\mathbf C^2\). Show that \(\bar\partial f=0\) exactly when \(g\) is holomorphic in \(z_2\), and in that case write down a solution of \(\bar\partial u=f\) on \(\{|z_1|<1\}\times\mathbf C\).

*Solution.* \(\bar\partial f=\frac{\partial g}{\partial\bar z_2}\,d\bar z_2\wedge d\bar z_1\), which vanishes exactly when \(\partial g/\partial\bar z_2=0\). Then, with \(\psi\) a smooth function of \(z_1\) equal to \(1\) on \(|z_1|\leq1\) and with compact support, \(u(z)=-\frac1\pi\int_{\mathbf C}\psi(\zeta)g(\zeta,z_2)(\zeta-z_1)^{-1}\,dA(\zeta)\) is smooth and holomorphic in \(z_2\) by Lemma 2.1, so \(\bar\partial u=\frac{\partial u}{\partial\bar z_1}\,d\bar z_1=\psi g\,d\bar z_1\), which equals \(f\) where \(|z_1|<1\). This is the step \(k=1\) of the proof of Theorem 2.2.

**Exercise 4.3.** Explain why Lemma 3.1 does not apply to \(\mathcal O\), and give an open set \(U\) with \(H^1(U,\mathcal O)\neq0\).

*Solution.* \(\mathcal O\) is not a \(\mathcal C^\infty\)-module: a smooth multiple of a holomorphic function is not holomorphic in general, so the partition of unity argument leaves the sheaf. For \(U=\mathbf C^2\setminus\{0\}\), cover by \(U_1=\{z_1\neq0\}\) and \(U_2=\{z_2\neq0\}\). The function \(1/(z_1z_2)\) on \(U_1\cap U_2\) is a Čech \(1\)-cocycle. If it were a coboundary, \(1/(z_1z_2)=h_2-h_1\) with \(h_i\in\mathcal O(U_i)\); expanding in Laurent series on \(U_1\cap U_2\), \(h_1\) has only terms \(z_1^az_2^b\) with \(b\geq0\), and \(h_2\) only terms with \(a\geq0\), so neither produces the term \(z_1^{-1}z_2^{-1}\). Since the Čech \(H^1\) of a covering injects into \(H^1(U,\mathcal O)\) [Stacks, Tag 0B8R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-h1), the class is nonzero.

**Exercise 4.4.** Let \(L\) be a holomorphic line bundle on a compact Riemann surface \(X\). Show that \(H^q(X,\mathcal O(L))=0\) for \(q\geq2\).

*Solution.* This is Corollary 3.3 with \(n=1\).

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026), licensed CC BY-SA 4.0 (dual-licensed with CC BY-NC-SA 4.0). <https://www.jirka.org/scv/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>

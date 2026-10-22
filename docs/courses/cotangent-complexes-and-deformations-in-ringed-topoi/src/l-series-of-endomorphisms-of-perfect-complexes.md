# L-series of endomorphisms of perfect complexes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For an endomorphism \(\varphi\) of a free module \(V\) of finite rank over a commutative ring, \(\det(1-t\varphi)=\sum_n(-1)^n\operatorname{Tr}(\Lambda^n\varphi)t^n\), and the series \(\sum_n\operatorname{Tr}(S^n\varphi)t^n\) is the inverse of \(\det(1-t\varphi)\). This lesson extends both series to an *endomorphism of a perfect complex \(E\) with coefficients in a complex \(M\)*, that is, a morphism \(f\colon E\to E\otimes^{\mathbf L}M\) of the derived category of a ringed topos, with \(M\) concentrated in degrees \(\leq0\). The coefficients are the traces of the morphisms \(\varphi^n\circ LS^n(f)\colon LS^nE\to\) \(LS^nE\otimes^{\mathbf L}LS^nM\), where \(\varphi^n\) are the diagonal maps. The lesson proves:

- the groups of series \(\prod_n\operatorname{Hom}(A,L\mathbf T^nM)\) and \(\prod_n\operatorname{Hom}(A,L\mathbf T^n(M)[n])\) are rings, which for \(M\) in degrees \(\leq0\) are commutative or anticommutative according to \(\mathbf T\) and the shift; the shift isomorphisms identify \(\prod_n\operatorname{Hom}(A,LS^n(M[1]))\) with \(\prod_n\operatorname{Hom}(A,L\Lambda^n(M)[n])\) as rings, and, after the signs \((-1)^{n(n-1)/2}\), \(\prod_n\operatorname{Hom}(A,L\Lambda^n(M[1]))\) with \(\prod_n\operatorname{Hom}(A,L\Gamma^n(M)[n])\);
- the trace of a morphism shifted by \(a\) is \((-1)^a\) times its trace;
- the L-series \(L_t(f)\) is natural in \(M\), invariant under isomorphisms and base change, equal to the L-series of the graded pieces for a filtered morphism, multiplicative on gradings, and satisfies \(L_t(f[1])=L_t(f)^{-1}\); this extends the definition to perfect complexes with cohomology in positive degrees;
- the characteristic series \(c_t(f)=L_t(f)^{-1}\) is \(\sum_n(-1)^n\operatorname{Tr}(\psi^n\circ L\Lambda^n(f))t^n\);
- if \(f\) is the class of a map of complexes \(\varphi\) of a strictly perfect complex, then \(c_t(f)=\prod_i\det(1-t\varphi^i)^{(-1)^i}\); this alternating product therefore depends only on \(f\), and over a local ring it defines \(\det(1-tf)\) for every endomorphism \(f\) of a perfect complex.

**Prerequisites.** [*Diagonal maps of symmetric and exterior powers*](diagonal-maps-of-symmetric-and-exterior-powers.md) (Construction 2.1, Propositions 2.2–2.4, Exercise 3.3); [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md) (Propositions 2.2, 2.4, Theorem 2.6, Propositions 2.7, 2.8); [*Filtered Koszul complexes and the shift isomorphisms*](filtered-koszul-complexes-and-shift-isomorphisms.md) (Theorem 2.2); [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Theorem 3.2, Proposition 3.4 and the isomorphisms \(\tau\) of Section 3); [*Traces and cup products of perfect filtered complexes*](traces-and-cup-products-of-perfect-filtered-complexes.md) (Definitions 1.1, 2.1, Lemma 1.2, Propositions 1.4, 2.2, 2.5, 2.8, Theorem 2.3); [*Perfect filtered complexes and duality*](perfect-filtered-complexes-and-duality.md) (Definition 1.1, Theorem 4.2); [*Filtered derived categories*](filtered-derived-categories.md) (the conventions on cones and shifts, Proposition 2.2); [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md) (Definition 2.1, Propositions 3.2, 4.1); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution), Theorem 1.3 (Alexander–Whitney and shuffle maps). From the AI-integrated Stacks project: morphisms in a localization [[Stacks, Tag 05Q4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-remark-right-localization-morphisms-colimit)]; strictly perfect and perfect complexes [[Tag 08FL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-strictly-perfect)], [[Tag 08G5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-perfect)]; a morphism out of a strictly perfect complex is locally a map of complexes [[Tag 08FR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-local-actual)]; K-flat resolutions [[Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution)]; bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)]; finite projective modules [[Tag 00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective)], which over a local ring are free [[Tag 00NZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-flat-local)]; morphisms out of a bounded above complex of projectives [[Tag 064B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-from-projective-complex)].

## Conventions

\(A\) is a commutative ring of a topos \(T\). In \(D(A)\), \(DF(A)\) and \(DG(A)\) the tensor product is derived and written \(\otimes\); these categories are symmetric monoidal with unit \(A\), and the symmetry \(\sigma_{X,Y}\colon X\otimes Y\to Y\otimes X\) is given on K-flat complexes by \(x\otimes y\mapsto(-1)^{|x||y|}y\otimes x\). We identify \(A\otimes A\) with \(A\) by the multiplication; then \(\sigma_{A,A}\) is the identity, \(A\) being commutative. For objects \(X\), \(Y\) and integers \(a\), \(b\), \(\tau\colon X[a]\otimes Y[b]\to(X\otimes Y)[a+b]\) is the isomorphism of Section 3 of the lesson on Koszul complexes, \(x\otimes y\mapsto(-1)^{b|x|}x\otimes y\) with \(|x|\) the degree of \(x\) in \(X[a]\); it is natural and associative, and for \(b=0\) it is the identity, by which we write \(X[a]\otimes Y=(X\otimes Y)[a]\). Shifts of morphisms carry no sign, \(u[a]^i=u^{a+i}\). For \(g\colon E\otimes K\to E\otimes L\), \(g[a]\colon E[a]\otimes K\to E[a]\otimes L\) is the shifted morphism \((E\otimes K)[a]\to(E\otimes L)[a]\); for \(K=A\) this is \(f[a]\colon E[a]\to E[a]\otimes M\) for \(f\colon E\to E\otimes M\). The cone of a map of complexes \(u\colon X\to Y\) is \(C(u)^n=Y^n\oplus X^{n+1}\) with \(d(y,x)=(dy+u(x),-dx)\), as in the lesson on filtered derived categories.

\(\mathbf T\) is one of \(S\), \(\Lambda\), \(\Gamma\), and \(L\mathbf T^n\) is the derived functor on \(D^-(A)\), \(D^-F(A)\), \(D^-G(A)\) of the lesson on filtered and graded powers, with the products \(\mu\colon L\mathbf T^pM\otimes L\mathbf T^qM\to L\mathbf T^{p+q}M\) of Proposition 2.7 there; \(L\mathbf T^0M=A\), and \(\mu\) is the unit isomorphism when \(p=0\) or \(q=0\). \(D^{\leq0}(A)\) is the full subcategory of objects without cohomology in positive degrees, and \(D^{\leq0}F(A)\), \(D^{\leq0}G(A)\) are the full subcategories of objects whose graded pieces, resp. components, lie in \(D^{\leq0}(A)\). An object of \(D(A)\) has *bounded perfect amplitude* if it has perfect amplitude in some interval \([m,n]\) (Definition 1.1 of the lesson on perfect filtered complexes); it is then perfect, with tor amplitude and cohomology in \([m,n]\). A filtered or graded object has bounded perfect amplitude if its graded pieces or components have perfect amplitude in one interval. Perfect objects are dualizable (Theorem 4.2 of the lesson on duality), and \(\operatorname{Tr}\) is the trace of Definition 2.1 of the lesson on traces; for a morphism \(g\colon E\to E\otimes L\) we use \(E=E\otimes A\), so that \(\operatorname{Tr}(g)\colon A\to L\).

## 1. Rings of series

**Definition 1.1.** For \(M\in D^-(A)\) put
\[
\begin{aligned}&\operatorname{Hom}(A,L\mathbf T^\bullet(M))\\
&\quad=\prod_{n\geq0}\operatorname{Hom}(A,L\mathbf T^n(M)),\\
&\operatorname{Hom}(A,L\mathbf T^\bullet(M)[1])\\
&\quad=\prod_{n\geq0}\operatorname{Hom}(A,L\mathbf T^n(M)[n]),\end{aligned}
\]
the groups of morphisms of \(D(A)\), and write an element as a series \(\sum_na_nt^n\). The product of \(a=\sum a_pt^p\) and \(b=\sum b_qt^q\) is the series with coefficients
\[
\begin{gathered}(ab)_n=\sum_{p+q=n}\mu\circ(a_p\otimes b_q),\quad\text{resp.}\\
(ab)_n=\sum_{p+q=n}\mu[n]\circ\tau\circ(a_p\otimes b_q),\end{gathered}
\]
where \(a_p\otimes b_q\colon A=A\otimes A\to L\mathbf T^pM\otimes L\mathbf T^qM\), resp. \(\to L\mathbf T^p(M)[p]\otimes L\mathbf T^q(M)[q]\).

**Proposition 1.2.** Let \(M\in D^-(A)\).

1. \(\operatorname{Hom}(A,L\mathbf T^\bullet(M))\) and \(\operatorname{Hom}(A,L\mathbf T^\bullet(M)[1])\) are associative rings, with unit the series \(1\) whose constant term is \(1_A\). A series \(a\) is invertible if and only if \(a_0\) is a unit of \(\operatorname{Hom}(A,A)=\Gamma(T,A)\); in particular every series with constant term \(1\) is invertible.
2. If \(M\in D^{\leq0}(A)\), then for \(a_p\), \(b_q\) of degrees \(p\), \(q\): \(b_qa_p=a_pb_q\) in \(\operatorname{Hom}(A,LS^\bullet(M))\), \(\operatorname{Hom}(A,L\Gamma^\bullet(M))\) and \(\operatorname{Hom}(A,L\Lambda^\bullet(M)[1])\), and \(b_qa_p=(-1)^{pq}a_pb_q\) in \(\operatorname{Hom}(A,L\Lambda^\bullet(M))\), \(\operatorname{Hom}(A,LS^\bullet(M)[1])\) and \(\operatorname{Hom}(A,L\Gamma^\bullet(M)[1])\).
3. A morphism \(m\colon M\to M'\) of \(D^-(A)\) induces ring homomorphisms \(m_*\colon\sum a_nt^n\mapsto\sum L\mathbf T^n(m)\circ a_n\,t^n\), resp. \(\sum L\mathbf T^n(m)[n]\circ a_n\,t^n\).

**Proof.** (1) The products \(\mu\) are associative (Proposition 2.7 of the lesson on filtered and graded powers), and \(\tau\) is natural and associative. So \(((ab)c)_n\) and \((a(bc))_n\) are both \(\sum_{p+q+r=n}\mu\circ(\mu\otimes1)\circ(a_p\otimes b_q\otimes c_r)\), resp. the same expression with \(\mu[n]\) and the iterated \(\tau\), the two identifications \(A\otimes A\otimes A=A\) being equal by the associativity of the multiplication of \(A\). The series \(1\) is a unit because \(\mu\) is the unit isomorphism in degree \(0\). For \(s\in\Gamma(T,A)\) and \(x\colon A\to X\), \(\mu\circ(s\otimes x)=x\circ s=s\,x\), where \(s\) acts as multiplication on \(A\). If \(a_0\) is a unit, the equations \((ab)_0=1\) and \(a_0b_n=-\sum_{p=1}^na_pb_{n-p}\) define a right inverse \(b\) recursively, and the same recursion on the other side defines a left inverse; they agree by associativity. Conversely \((ab)_0=a_0b_0\).

(2) Represent \(M\) by a complex \(P\) of flat modules vanishing in degrees \(>0\) (Proposition 2.4 of the lesson on filtered and graded powers, with the bound \(0\)). Then \(L\mathbf T^nM\) is represented by \(\mathbf T^n(P)=N\mathbf T^n(\Gamma P)\), a complex of flat modules vanishing in degrees \(>0\), hence K-flat [Tag 06YQ], and \(\mu\) by \(N(\text{mult})\circ\operatorname{sh}\), the map (5.1) of the lesson on non-additive functors being the shuffle map for complexes in degrees \(\leq0\) (conventions of the lesson on diagonal maps). By Proposition 2.3 (1) of the lesson on diagonal maps, \(\operatorname{sh}(w\otimes v)=(-1)^{ij}N(t)\operatorname{sh}(v\otimes w)\) for \(v\), \(w\) of degrees \(i\), \(j\), where \(t\) exchanges the factors termwise. The termwise multiplication of \(\mathbf T(\Gamma P)\) satisfies \(\text{mult}\circ t=\text{mult}\) for \(S\) and \(\Gamma\), and \(\text{mult}\circ t=(-1)^{pq}\text{mult}\) on \(\Lambda^p\otimes\Lambda^q\). On K-flat models \(\sigma\) is \(v\otimes w\mapsto(-1)^{ij}w\otimes v\), so \(\mu\circ\sigma=\mu\) for \(S\) and \(\Gamma\), and \(\mu\circ\sigma=(-1)^{pq}\mu\) for \(\Lambda\), as morphisms \(L\mathbf T^pM\otimes L\mathbf T^qM\to L\mathbf T^{p+q}M\). By naturality of \(\sigma\) and \(\sigma_{A,A}=1\), \(b_q\otimes a_p=\sigma\circ(a_p\otimes b_q)\), so \(b_qa_p=\mu\circ\sigma\circ(a_p\otimes b_q)\); this gives the three unshifted rings. For the shifted rings, let \(x\in X^i\), \(y\in Y^j\); then \(\tau\circ\sigma_{X[p],Y[q]}\) multiplies \(x\otimes y\mapsto y\otimes x\) by \((-1)^{(i-p)(j-q)+p(j-q)}=(-1)^{ij+iq}\), and \(\sigma_{X,Y}[p+q]\circ\tau\) by \((-1)^{q(i-p)+ij}\). Hence
\[
\tau\circ\sigma_{X[p],Y[q]}=(-1)^{pq}\,\sigma_{X,Y}[p+q]\circ\tau,
\]
and
\[
\begin{aligned}&b_qa_p=\mu[n]\circ\tau\circ\sigma\circ(a_p\otimes b_q)\\
&\quad=(-1)^{pq}(\mu\circ\sigma)[n]\circ\tau\circ(a_p\otimes b_q),\end{aligned}
\]
so the sign of the unshifted ring is multiplied by \((-1)^{pq}\).

(3) The products and \(\tau\) are natural. \(\square\)

**Proposition 1.3 (the shift isomorphisms are ring isomorphisms).** Let \(M\in D^-(A)\), and let \(\sigma^S_M\colon LS^n(M[1])\to L\Lambda^n(M)[n]\) and \(\sigma^\Lambda_M\colon L\Lambda^n(M[1])\to L\Gamma^n(M)[n]\) be the shift isomorphisms of Theorem 3.2 of the lesson on Koszul complexes (the underlying isomorphisms of Theorem 2.2 of the lesson on filtered Koszul complexes), the identity of \(A\) for \(n=0\). Then
\[
\begin{gathered}\textstyle\sum a_nt^n\mapsto\sum\sigma^S_M\circ a_n\,t^n,\\
\textstyle\sum a_nt^n\mapsto\sum(-1)^{n(n-1)/2}\sigma^\Lambda_M\circ a_n\,t^n\end{gathered}
\]
are ring isomorphisms \(\operatorname{Hom}(A,LS^\bullet(M[1]))\to\) \(\operatorname{Hom}(A,L\Lambda^\bullet(M)[1])\) and \(\operatorname{Hom}(A,L\Lambda^\bullet(M[1]))\to\) \(\operatorname{Hom}(A,L\Gamma^\bullet(M)[1])\), natural in \(M\). Without the signs, the second map multiplies the product of two elements of degrees \(m\), \(n\) by \((-1)^{mn}\).

**Proof.** Both maps are bijective and natural because the \(\sigma\) are natural isomorphisms. By Proposition 3.4 of the lesson on Koszul complexes, for \(m,n\geq1\)
\[
\begin{aligned}&\sigma^S_M\circ\mu=\mu[m+n]\circ\tau\circ(\sigma^S_M\otimes\sigma^S_M),\\
&\sigma^\Lambda_M\circ\mu=(-1)^{mn}\mu[m+n]\\
&\qquad\circ\tau\circ(\sigma^\Lambda_M\otimes\sigma^\Lambda_M),\end{aligned}
\]
the products being those of \(LS(M[1])\) and \(L\Lambda(M)\), resp. \(L\Lambda(M[1])\) and \(L\Gamma(M)\); for \(m=0\) or \(n=0\) both sides are unit isomorphisms. Let \(\Phi(a)_n=\varepsilon_n\sigma\circ a_n\) with signs \(\varepsilon_n\), \(\varepsilon_0=1\). For \(a_m\), \(b_n\),
\[
\begin{aligned}&\Phi(a_mb_n)=\varepsilon_{m+n}\sigma\circ\mu\circ(a_m\otimes b_n),\\
&\Phi(a_m)\Phi(b_n)=\varepsilon_m\varepsilon_n\mu[m+n]\circ\tau\\
&\qquad\circ(\sigma\otimes\sigma)\circ(a_m\otimes b_n).\end{aligned}
\]
For \(S\) they agree with \(\varepsilon_n=1\). For \(\Lambda\) they agree when \(\varepsilon_{m+n}=(-1)^{mn}\varepsilon_m\varepsilon_n\), which holds for \(\varepsilon_n=(-1)^{n(n-1)/2}\) because \((m+n)(m+n-1)/2=\) \(m(m-1)/2+n(n-1)/2+mn\); with \(\varepsilon_n=1\) the two sides differ by \((-1)^{mn}\). \(\square\)

## 2. The trace of a shifted morphism

**Lemma 2.1.** Let \(E\in D(A)\) be perfect, \(K,L\in D(A)\) and \(g\colon E\otimes K\to E\otimes L\). Then \(\operatorname{Tr}(g[a])=(-1)^a\operatorname{Tr}(g)\) for every integer \(a\).

**Proof.** It suffices to prove \(\operatorname{Tr}(g[1])=-\operatorname{Tr}(g)\): applied to \(g[-1]\) it gives the case \(a=-1\), and the general case follows by induction. Represent \(E\), \(K\), \(L\) by K-flat complexes \(P\), \(Q\), \(R\) [Tag 06YS], so that \(E\otimes K=P\otimes Q\) and \(E\otimes L=P\otimes R\), and write \(g=h\circ s^{-1}\) with maps of complexes \(s\colon X\to P\otimes Q\), a quasi-isomorphism, and \(h\colon X\to P\otimes R\) [Tag 05Q4].

For a complex \(Z\) let \(C_Z=C(1_Z)\), filtered by \(F^1C_Z=Z\) (the first summand, a subcomplex), \(F^0C_Z=C_Z\), \(F^2C_Z=0\). Then \(\operatorname{gr}^1C_Z=Z\), and \((y,x)\mapsto x\) identifies \(\operatorname{gr}^0C_Z\) with \(Z[1]\), whose differential is \(-d\). A map of complexes \(u\colon Z\to Z'\) gives the filtered map \(C(u)\colon(y,x)\mapsto(u(y),u(x))\), with \(\operatorname{gr}^1C(u)=u\) and \(\operatorname{gr}^0C(u)=u[1]\); it is a filtered quasi-isomorphism if \(u\) is a quasi-isomorphism. So \(G=C(h)\circ C(s)^{-1}\colon C_{P\otimes Q}\to C_{P\otimes R}\) is a morphism of \(DF(A)\) with \(\operatorname{gr}^1G=g\) and \(\operatorname{gr}^0G=g[1]\).

The map \((y\otimes q,x\otimes q)\mapsto(y,x)\otimes q\) is an isomorphism of filtered complexes \(C_{P\otimes Q}\to C_P\otimes Q\), the shifted factor being on the left, and likewise \(C_{P\otimes R}=C_P\otimes R\). The filtered complex \(C_P\) has the K-flat graded pieces \(P\) and \(P[1]\), so it is filtered K-flat (Definition 2.1 of the lesson on filtered tensor products) and \(C_P\otimes Q\), \(C_P\otimes R\) represent \(C_P\otimes K\), \(C_P\otimes L\) in \(DF(A)\), with \(K\), \(L\) in filtration \([0,0]\) (Proposition 3.2 there). Its graded pieces \(E\) and \(E[1]\) are perfect, so \(C_P\) is filtered perfect, and the additivity of traces (Theorem 2.3 of the lesson on traces) gives \(\operatorname{Tr}(G)=\operatorname{Tr}(g)+\operatorname{Tr}(g[1])\), the left side being the trace of the underlying morphism of \(D(A)\). The underlying complex of \(C_P\) is acyclic, so \(C_P\to0\) is an isomorphism of \(D(A)\); by Lemma 1.2 (3) there, \(\operatorname{Tr}(G)\) is a trace over the zero object, which is \(0\). \(\square\)

## 3. The L-series

**Definition 3.1.** Let \(M\in D^{\leq0}(A)\), let \(E\in D^{\leq0}(A)\) have bounded perfect amplitude, and let \(f\colon E\to E\otimes M\) be a morphism of \(D(A)\). For \(n\geq0\), \(LS^nE\) has bounded perfect amplitude (Proposition 2.8 of the lesson on filtered and graded powers), \(LS^nM\) lies in \(D^{\leq0}(A)\) (it is represented by \(S^n(Q)\) for a complex \(Q\) of flat modules in degrees \(\leq0\) representing \(M\)), and the diagonal map \(\varphi^n=\varphi^n_{E,M}\colon LS^n(E\otimes M)\to\) \(LS^nE\otimes LS^nM\) of Proposition 2.2 of the lesson on diagonal maps is defined. The *L-series* and the *characteristic series* of \(f\) are
\[
\begin{gathered}L_t(f)=\sum_{n\geq0}\operatorname{Tr}\bigl(\varphi^n\circ LS^n(f)\bigr)t^n\\
\in\operatorname{Hom}(A,LS^\bullet(M)),\\
c_t(f)=L_t(f)^{-1},\end{gathered}
\]
where \(\varphi^n\circ LS^n(f)\colon LS^nE\to LS^nE\otimes LS^nM\), so that its trace is a morphism \(A\to LS^nM\).

Since \(LS^0E=A\), \(\varphi^0=1\) and \(\operatorname{Tr}(1_A)=1\), \(L_t(f)\) has constant term \(1\) and is invertible (Proposition 1.2 (1)). Since \(\varphi^1=\operatorname{AW}\circ\operatorname{sh}=1\) in the derived category (Theorem 1.3 of the lesson on the cotangent complex), the coefficient of \(t\) is \(\operatorname{Tr}(f)\).

**Proposition 3.2.** In the situation of Definition 3.1:

1. (*Naturality in \(M\)*) For \(m\colon M\to M'\) in \(D^{\leq0}(A)\), \(L_t((1_E\otimes m)\circ f)=m_*L_t(f)\).
2. (*Invariance*) For an isomorphism \(a\colon E\to E'\), \(L_t((a\otimes1_M)\circ f\circ a^{-1})=L_t(f)\).
3. (*Base change*) For a morphism of ringed topoi \(u\colon(T',A')\to(T,A)\), \(L_t(Lu^*f)=Lu^*L_t(f)\), where \(Lu^*f\colon Lu^*E\to Lu^*E\otimes Lu^*M\) and \(Lu^*\colon\operatorname{Hom}(A,LS^\bullet(M))\to\) \(\operatorname{Hom}(A',LS^\bullet(Lu^*M))\) is the ring homomorphism \(\sum a_nt^n\mapsto\sum Lu^*(a_n)t^n\).

**Proof.** (1) \(LS^n((1\otimes m)f)=\) \(LS^n(1\otimes m)\circ LS^n(f)\), and \(\varphi^n\) is natural in \(M\) (Proposition 2.2 of the lesson on diagonal maps), so \(\varphi^n_{E,M'}\circ LS^n(1\otimes m)=\) \((1\otimes LS^n(m))\circ\varphi^n_{E,M}\). By Lemma 1.2 (2) of the lesson on traces, \(\operatorname{Tr}((1\otimes LS^n(m))g)=LS^n(m)\circ\operatorname{Tr}(g)\).

(2) \(LS^n((a\otimes1)fa^{-1})=\) \(LS^n(a\otimes1)\circ LS^n(f)\circ LS^n(a)^{-1}\), and naturality of \(\varphi^n\) in the first variable gives \(\varphi^n_{E',M}\circ LS^n(a\otimes1)=\) \((LS^n(a)\otimes1)\circ\varphi^n_{E,M}\). So \(\varphi^nLS^n\) of the conjugate is the conjugate of \(\varphi^nLS^n(f)\) by \(LS^n(a)\), and Lemma 1.2 (3) of the lesson on traces applies.

(3) Represent \(E\), \(M\) by complexes \(P\), \(Q\) of flat modules vanishing in degrees \(>0\); they are K-flat [Tag 06YQ], so \(u^*P\), \(u^*Q\) represent \(Lu^*E\), \(Lu^*M\) (Proposition 4.1 of the lesson on filtered tensor products, with filtrations in \([0,0]\)), and they are complexes of flat modules vanishing in degrees \(>0\). The functor \(u^*\) commutes with tensor products, with \(S^n\) of modules, and with \(\Gamma\) and \(N\), which are formed termwise; so \(u^*S^n(P)=u^*NS^n(\Gamma P)=\) \(NS^n(\Gamma u^*P)=S^n(u^*P)\) represents both \(Lu^*LS^nE\) and \(LS^nLu^*E\), and the maps \(\operatorname{sh}\), \(\operatorname{AW}\), \(g_{P,Q}\) and the termwise \(\varphi^n\) of Construction 2.1 of the lesson on diagonal maps commute with \(u^*\). Hence \(Lu^*\varphi^n_{E,M}=\varphi^n_{Lu^*E,Lu^*M}\) and \(Lu^*LS^n(f)=LS^n(Lu^*f)\) under these identifications, which are compatible with the products; Proposition 2.8 of the lesson on traces gives \(\operatorname{Tr}(Lu^*g)=Lu^*\operatorname{Tr}(g)\). \(\square\)

**Theorem 3.3 (filtrations and gradings).** Let \(M\in D^{\leq0}(A)\).

1. Let \(E\in D^{\leq0}F(A)\) have bounded perfect amplitude, place \(M\) in \(DF(A)\) with filtration in \([0,0]\), and let \(f\colon E\to E\otimes M\) be a morphism of \(DF(A)\). Then \(L_t(f)=L_t(\operatorname{gr}f)\), the L-series being those of the underlying morphisms \(f\) and \(\operatorname{gr}f\colon\operatorname{gr}E\to\operatorname{gr}E\otimes M\) of \(D(A)\).
2. Let \(E=(E_i)_i\in D^{\leq0}G(A)\) have bounded perfect amplitude, place \(M\) in weight \(0\), and let \(f\colon E\to E\otimes M\) be a morphism of \(DG(A)\), with components \(f_i\colon E_i\to E_i\otimes M\). Then \(L_t(f)=\prod_iL_t(f_i)\), the product taken in any order.

**Proof.** (1) Fix \(n\). In \(DF(A)\), \(LS^nE\) is filtered perfect (Proposition 2.8 of the lesson on filtered and graded powers), and \(LS^nM\) has filtration in \([0,0]\) (Theorem 2.6 (1) there). The morphism \(g=\varphi^n_{E,M}\circ LS^n(f)\colon LS^nE\to\) \(LS^nE\otimes LS^nM\) of \(DF(A)\) has as underlying morphism \(\varphi^n\circ LS^n(f)\) for the underlying objects (Proposition 2.2 of the lesson on diagonal maps), so by Theorem 2.3 of the lesson on traces the coefficient of \(t^n\) in \(L_t(f)\) is \(\sum_p\operatorname{Tr}(\operatorname{gr}^pg)\). Under the isomorphism \(c\colon LS^n(\operatorname{gr}E)\to\operatorname{gr}LS^nE\) of Theorem 2.6 (2) there, \(\operatorname{gr}LS^n(f)\) corresponds to \(LS^n(\operatorname{gr}f)\) by naturality of \(c\), and \(\operatorname{gr}\varphi^n_{E,M}\) to \(\varphi^n_{\operatorname{gr}E,M}\) (Proposition 2.2 of the lesson on diagonal maps). So the morphism \(\bigoplus_p\operatorname{gr}^pg\) of \(D(A)\) is conjugate by \(c\) to \(\varphi^n_{\operatorname{gr}E,M}\circ LS^n(\operatorname{gr}f)\), and by Lemma 1.2 (3), (4) of the lesson on traces, \(\sum_p\operatorname{Tr}(\operatorname{gr}^pg)=\operatorname{Tr}(\varphi^n_{\operatorname{gr}E,M}\circ LS^n(\operatorname{gr}f))\), the coefficient of \(t^n\) in \(L_t(\operatorname{gr}f)\).

(2) Only finitely many \(E_i\) are nonzero; order them by \(i\). By Proposition 2.2 (2) and Theorem 2.6 of the lesson on filtered and graded powers, applied to the finite decomposition \(E=\bigoplus_iE_i\), \(LS^nE=\bigoplus_\nu\bigotimes_iLS^{\nu_i}E_i\) over the families \(\nu=(\nu_i)\) with \(\sum_i\nu_i=n\), the summand of \(\nu\) being embedded by the iterated product of the maps \(LS^{\nu_i}(\iota_i)\), \(\iota_i\colon E_i\to E\); likewise for \(LS^n(E\otimes M)\) with \(E\otimes M=\bigoplus_i(E_i\otimes M)\). The morphism \(f\) has no components between different weights, so by naturality of the products \(LS^n(f)\) maps the summand of \(\nu\) to the summand of \(\nu\) by \(\bigotimes_iLS^{\nu_i}(f_i)\). By Proposition 2.3 (3) of the lesson on diagonal maps, \(\varphi^n_{E,M}\) maps the summand \(\bigotimes_iLS^{\nu_i}(E_i\otimes M)\) into \((\bigotimes_iLS^{\nu_i}E_i)\otimes LS^nM\) by \(\bigotimes_i\varphi^{\nu_i}_{E_i,M}\), the symmetry, and the product \(\bigotimes_iLS^{\nu_i}M\to LS^nM\). Hence \(g=\varphi^n\circ LS^n(f)\) is the direct sum over \(\nu\) of \(g_\nu=(1\otimes\mu)\circ(\boxtimes_ig_{i,\nu_i})\), where \(g_{i,k}=\varphi^k_{E_i,M}\circ LS^k(f_i)\) and \(\boxtimes\) is the product of Proposition 1.4 of the lesson on traces (with \(K_i=A\)). By Lemma 1.2 (2), (4) and Proposition 2.5 there, applied inductively, \(\operatorname{Tr}(g)=\sum_\nu\mu\circ\bigotimes_i\operatorname{Tr}(g_{i,\nu_i})\), which is the coefficient of \(t^n\) in the product \(\prod_iL_t(f_i)\) taken in increasing order of \(i\). The ring \(\operatorname{Hom}(A,LS^\bullet(M))\) is commutative (Proposition 1.2 (2)), so the order does not matter. \(\square\)

**Corollary 3.4 (shift).** In the situation of Definition 3.1, \(L_t(f[1])=c_t(f)\), and \(L_t(f[2])=L_t(f)\).

**Proof.** Represent \(E\) and \(M\) by complexes \(P\), \(Q\) of flat modules vanishing in degrees \(>0\), so that \(E\otimes M=P\otimes Q\), and write \(f=h\circ s^{-1}\) with maps of complexes \(s\colon P'\to P\), a quasi-isomorphism, and \(h\colon P'\to P\otimes Q\) [Tag 05Q4]; precomposing with \(\tau_{\leq0}P'\to P'\) and a resolution as in Proposition 2.4 of the lesson on filtered and graded powers, we may take \(P'\) to be a complex of flat modules vanishing in degrees \(>0\). With the filtered complexes \(C_Z\) and the maps \(C(u)\) of the proof of Lemma 2.1, \(\underline f=C(h)\circ C(s)^{-1}\colon C_P\to\) \(C_{P\otimes Q}=C_P\otimes Q\) is a morphism of \(DF(A)\) from \(C_P\) to \(C_P\otimes M\), with \(\operatorname{gr}^1\underline f=f\) and \(\operatorname{gr}^0\underline f=f[1]\). The complex \(C_P\) vanishes in degrees \(>0\), and its graded pieces \(E\), \(E[1]\) have bounded perfect amplitude and lie in \(D^{\leq0}(A)\). By Theorem 3.3 (1) and (2), \(L_t(\underline f)=L_t(f)L_t(f[1])\). The underlying complex of \(C_P\) is acyclic, so by Proposition 3.2 (2) applied to the isomorphism \(C_P\to0\), \(L_t(\underline f)\) is the L-series of the morphism \(0\to0\otimes M\), which is \(1\) because \(LS^n(0)=0\) for \(n\geq1\). Hence \(L_t(f[1])=L_t(f)^{-1}\). Applying this to \(f[1]\), whose source \(E[1]\) lies in \(D^{\leq0}(A)\), gives \(L_t(f[2])=L_t(f[1])^{-1}=L_t(f)\). \(\square\)

**Definition 3.5 (perfect complexes with cohomology in positive degrees).** Let \(M\in D^{\leq0}(A)\), let \(E\in D(A)\) have bounded perfect amplitude, and let \(f\colon E\to E\otimes M\). Choose \(k\geq0\) with \(E[2k]\in D^{\leq0}(A)\), and put \(L_t(f)=L_t(f[2k])\) and \(c_t(f)=L_t(f)^{-1}\). By Corollary 3.4 this does not depend on \(k\), and for \(E\in D^{\leq0}(A)\) it agrees with Definition 3.1.

**Proposition 3.6.** Proposition 3.2, Theorem 3.3 and Corollary 3.4 hold for objects of bounded perfect amplitude that are not in \(D^{\leq0}\). Moreover \(L_t(f[a])=L_t(f)^{(-1)^a}\) for every integer \(a\).

**Proof.** Shifting by \(2k\) commutes with composition, with \(1\otimes m\), with conjugation by an isomorphism, with \(Lu^*\), with \(\operatorname{gr}\) and with taking components, and \((f[1])[2k]=(f[2k])[1]\); so each statement follows from the case of Definition 3.1 applied to \(f[2k]\) for \(k\) large. For \(a=1\), \(L_t(f[1])=L_t((f[2k])[1])=\) \(c_t(f[2k])=c_t(f)\). Applied to \(f[-1]\) this gives \(L_t(f)=L_t(f[-1])^{-1}\), and the general case follows by induction. \(\square\)

**Corollary 3.7 (characteristic series through exterior powers).** Let \(E,M\in D^{\leq0}(A)\), with \(E\) of bounded perfect amplitude, and \(f\colon E\to E\otimes M\). Then
\[
c_t(f)=\sum_{n\geq0}(-1)^n\operatorname{Tr}\bigl(\psi^n\circ L\Lambda^n(f)\bigr)t^n,
\]
where \(\psi^n=\psi^n_{E,M}\colon\) \(L\Lambda^n(E\otimes M)\to L\Lambda^nE\otimes LS^nM\) is the diagonal map of Proposition 2.2 of the lesson on diagonal maps and \(L\Lambda^nE\) is perfect (Proposition 2.8 of the lesson on filtered and graded powers).

**Proof.** By Corollary 3.4 the coefficient of \(t^n\) in \(c_t(f)\) is \(\operatorname{Tr}(\varphi^n_{E[1],M}\circ LS^n(f[1]))\), and \(E[1]\in D^{\leq0}(A)\). The shift isomorphism is natural: \(\sigma^S_{E\otimes M}\circ LS^n(f[1])=L\Lambda^n(f)[n]\circ\sigma^S_E\) (Theorem 2.2 of the lesson on filtered Koszul complexes). With Proposition 2.4 of the lesson on diagonal maps,
\[
\begin{aligned}&(\sigma^S_E\otimes1)\circ\varphi^n_{E[1],M}\circ LS^n(f[1])\\&\quad=\psi^n_{E,M}[n]\circ\sigma^S_{E\otimes M}\circ LS^n(f[1])\\&\quad=\bigl(\psi^n_{E,M}\circ L\Lambda^n(f)\bigr)[n]\circ\sigma^S_E.\end{aligned}
\]
By Lemma 1.2 (3) of the lesson on traces, conjugation by \(\sigma^S_E\colon LS^n(E[1])\to L\Lambda^n(E)[n]\) does not change the trace, and by Lemma 2.1 the trace of \((\psi^nL\Lambda^n(f))[n]\) is \((-1)^n\operatorname{Tr}(\psi^nL\Lambda^n(f))\). \(\square\)

**Remark 3.8 (scope).** The coefficients \(M\) are taken in \(D^{\leq0}(A)\) because the diagonal maps \(\varphi^n\), \(\psi^n\) are constructed for objects concentrated in degrees \(\leq0\) (Remark 2.5 of the lesson on diagonal maps). No finiteness condition on \(M\) is needed: the trace of the lesson on traces is defined for arbitrary \(K\), \(L\in D(A)\). For \(E\), Definition 3.5 removes the condition \(E\in D^{\leq0}(A)\) from the L-series; Corollary 3.7 is stated for \(E\in D^{\leq0}(A)\), where \(\psi^n_{E,M}\) is defined.

## 4. Determinants

For a module \(V\) that is a direct summand of a finite free module and an endomorphism \(\varphi\) of \(V\), the modules \(\Lambda^nV\) are direct summands of finite free modules, zero for \(n\) larger than the rank of a free module containing \(V\) as a direct summand. Put
\[
\begin{gathered}\det(1-t\varphi)=\sum_{n\geq0}(-1)^n\operatorname{Tr}(\Lambda^n\varphi)t^n\\
\in\Gamma(T,A)[t],\end{gathered}
\]
the traces being those of \(D(A)\). If \(A^r=V\oplus W\), Lemma 1.2 (4) of the lesson on traces gives \(\operatorname{Tr}(\varphi)=\operatorname{Tr}(\varphi\oplus0_W)\), and the trace of an endomorphism of \(A^r\), computed with the dual basis, is the sum of the diagonal entries of its matrix; so \(\operatorname{Tr}(\varphi)\in\Gamma(T,A)\) is the trace of the matrix of \(\varphi\oplus0_W\). For \(M=A\), \(LS^nA=S^nA=A\), with the product of \(A\) as product, so \(\operatorname{Hom}(A,LS^\bullet(A))=\Gamma(T,A)[[t]]\) as rings.

**Lemma 4.1.** For a commutative ring \(R\) and \(X\in M_r(R)\), \(\det(1-tX)\) is the determinant of the matrix \(1-tX\) over \(R[t]\), and \(\operatorname{Tr}(\Lambda^nX)\) is the sum of the principal \(n\times n\) minors of \(X\).

**Proof.** In the basis \(e_I=e_{i_1}\wedge\cdots\wedge e_{i_n}\), \(i_1<\cdots<i_n\), of \(\Lambda^nR^r\), the coefficient of \(e_I\) in \(\Lambda^nX(e_I)\) is the minor \(\det(X_{I,I})\), so \(\operatorname{Tr}(\Lambda^nX)=\sum_{|I|=n}\det(X_{I,I})\). In the Leibniz expansion \(\det(1-tX)=\) \(\sum_\pi\operatorname{sgn}(\pi)\prod_i(\delta_{i\pi(i)}-tx_{i\pi(i)})\), expand each product and collect the terms in which the factor \(-tx_{i\pi(i)}\) is chosen exactly for \(i\in I\). Such a term vanishes unless \(\pi(i)=i\) for \(i\notin I\), so \(\pi\) permutes \(I\), and the terms with a given \(I\) add up to \((-t)^{|I|}\det(X_{I,I})\). \(\square\)

**Theorem 4.2 (characteristic series of maps of complexes).** Let \(F\) be a strictly perfect complex [Tag 08FL], \(\varphi\colon F\to F\) a map of complexes, and \(f\colon F\to F=F\otimes A\) its class in \(D(A)\). Then, in \(\Gamma(T,A)[[t]]\),
\[
\begin{gathered}c_t(f)=\prod_i\det(1-t\varphi^i)^{(-1)^i},\\
L_t(f)=\prod_i\det(1-t\varphi^i)^{(-1)^{i+1}}.\end{gathered}
\]
In particular the right sides depend only on \(f\): homotopic maps of complexes, and maps of complexes that correspond under a quasi-isomorphism of strictly perfect complexes, have the same alternating product.

**Proof.** First let \(F=V\) be a module in degree \(0\). By Exercise 3.3 of the lesson on diagonal maps, \(\psi^n_{V,A}\) is the canonical isomorphism, and \(L\Lambda^nV=\Lambda^nV\) since \(V\) is flat. Corollary 3.7 gives \(c_t(\varphi)=\sum_n(-1)^n\operatorname{Tr}(\Lambda^n\varphi)t^n=\) \(\det(1-t\varphi)\).

In general, let \(F^{\geq p}\) be the subcomplex with terms \(F^i\) for \(i\geq p\) and \(0\) otherwise. These form a finite filtration of \(F\) by subcomplexes, preserved by \(\varphi\), with \(\operatorname{gr}^pF=F^p[-p]\) and \(\operatorname{gr}^p\varphi=\varphi^p[-p]\). The filtered complex \(F\) has bounded perfect amplitude, so Theorem 3.3 (1), (2) and Proposition 3.6 give
\[
\begin{aligned}L_t(f)&=\prod_pL_t(\varphi^p[-p])\\
&=\prod_pL_t(\varphi^p)^{(-1)^p}\\
&=\prod_p\det(1-t\varphi^p)^{(-1)^{p+1}},\end{aligned}
\]
and \(c_t(f)=L_t(f)^{-1}\). The last assertion follows because \(c_t(f)\) depends only on \(f\), homotopic maps have the same class, and a quasi-isomorphism \(q\colon F\to F'\) with \(q\varphi=\varphi'q\) gives \(f'=qfq^{-1}\), so \(c_t(f')=c_t(f)\) by Proposition 3.2 (2). \(\square\)

**Corollary 4.3.** For a commutative ring \(R\) and \(X\in M_r(R)\), \(\sum_{n\geq0}\operatorname{Tr}(S^nX)t^n=\det(1-tX)^{-1}\) in \(R[[t]]\).

**Proof.** Apply Theorem 4.2 on the punctual topos to \(F=R^r\) in degree \(0\) and \(\varphi=X\): \(LS^nR^r=S^nR^r\), and \(\varphi^n_{R^r,R}\) is the canonical isomorphism (Exercise 3.3 of the lesson on diagonal maps), so \(L_t(X)=\sum\operatorname{Tr}(S^nX)t^n\), while \(L_t(X)=\det(1-tX)^{-1}\) by Theorem 4.2 and Lemma 4.1. \(\square\)

**Corollary 4.4 (determinants of endomorphisms of perfect complexes).**

1. Let \(E\in D(A)\) be perfect and \(f\colon E\to E\) a morphism. The final object of \(T\) has a covering \(\{U_j\}\) such that each \(E|_{U_j}\) is isomorphic to a strictly perfect complex \(F_j\) and \(f|_{U_j}\) is the class of a map of complexes \(\varphi_j\) of \(F_j\). The elements \(\prod_i\det(1-t\varphi_j^i)^{(-1)^i}\) of \(\Gamma(U_j,A)[[t]]\) glue to an element \(\det(1-tf)\) of \(\Gamma(T,A)[[t]]\) that does not depend on the choices, and \(\det(1-tf)=c_t(f)\) when \(E\) has bounded perfect amplitude.
2. Let \(T\) be the punctual topos, so that \(A\) is a ring, and let \(A\) be local. Then \(E\) is isomorphic to a bounded complex \(F\) of finite free modules, \(f\) is the class of a map of complexes \(\varphi\) of \(F\), unique up to homotopy, and \(\det(1-tf)=\) \(\prod_i\det(1-t\varphi^i)^{(-1)^i}=c_t(f)\).

**Proof.** (1) The covering exists by the definition of perfect objects [Tag 08G5] and by [Tag 08FR], after refining. On every object \(U\) over some \(U_j\), the restriction of \(E\) is isomorphic to a strictly perfect complex, hence has bounded perfect amplitude, and by Theorem 4.2 on the localized topos the restriction of \(\prod_i\det(1-t\varphi_j^i)^{(-1)^i}\) to \(U\) is \(c_t(f|_U)\). In particular the elements agree on the \(U_j\times U_k\) and glue, \(A\) being a sheaf, coefficient by coefficient; for a second choice, both glued elements restrict on a common refinement to the \(c_t(f|_U)\), so they are equal. If \(E\) has bounded perfect amplitude, \(c_t(f)\) restricts to \(c_t(f|_{U_j})\) (Proposition 3.2 (3) for the localization morphisms), which is the local alternating product.

(2) A covering of the final object of the punctual topos contains a nonempty set \(U_j\), and the slice over \(U_j\) is the product of copies of the punctual topos indexed by \(U_j\); restricting to one of them shows that \(E\) is isomorphic to a strictly perfect complex, that is, a bounded complex of finite projective modules [Tag 00NX]. These are free over a local ring [Tag 00NZ]. For a bounded complex \(F\) of free modules, \(\operatorname{Hom}_{D(A)}(F,F)=\operatorname{Hom}_{K(A)}(F,F)\) [Tag 064B], which gives \(\varphi\), and Theorem 4.2 applies. \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(s\in\Gamma(T,A)\), \(E=A[1]\), and \(f=s[1]\colon A[1]\to A[1]\), the shift of multiplication by \(s\). Compute \(L_t(f)\) directly from \(LS^n(A[1])\cong L\Lambda^n(A)[n]\) and Lemma 2.1, and compare with Theorem 4.2.

**Exercise 5.2.** Let \(x,a,b\in\Gamma(T,A)\) and let \(F\) be the complex \(A\xrightarrow{x}A\) in degrees \(-1,0\). (1) Show that \(\varphi=(a,b)\) (multiplication by \(a\) in degree \(-1\) and by \(b\) in degree \(0\)) is a map of complexes if and only if \((a-b)x=0\). (2) Compute \(c_t\) of its class. (3) If \(x\) is a unit, \(F\) is acyclic; check that the formula of (2) gives \(1\).

**Exercise 5.3.** Show that \(\varepsilon_n=(-1)^{n(n-1)/2}\) is the only family of signs with \(\varepsilon_0=\varepsilon_1=1\) and \(\varepsilon_{m+n}=(-1)^{mn}\varepsilon_m\varepsilon_n\) for all \(m,n\geq0\).

**Exercise 5.4.** For \(X=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) over a commutative ring, compute \(\operatorname{Tr}(S^2X)\) in the basis \(e_1^2,e_1e_2,e_2^2\) and compare with the coefficient of \(t^2\) in \(\det(1-tX)^{-1}\).

## 6. Complete solutions

**Solution 5.1.** By Theorem 2.2 of the lesson on filtered Koszul complexes, \(LS^n(A[1])\cong L\Lambda^n(A)[n]\), which is \(A\) for \(n=0\), \(A[1]\) for \(n=1\), and \(0\) for \(n\geq2\), because \(\Lambda^nA=0\) for \(n\geq2\). So only \(n=0,1\) contribute: \(L_t(f)=1+\operatorname{Tr}(f)t\). By Lemma 2.1, \(\operatorname{Tr}(s[1])=-\operatorname{Tr}(s)=-s\). Hence \(L_t(f)=1-st\). Theorem 4.2 for \(F=A[1]\), whose only term is \(F^{-1}=A\), with \(\varphi^{-1}=s\), gives \(L_t(f)=\det(1-ts)^{(-1)^{-1+1}}=1-st\), in agreement.

**Solution 5.2.** (1) The only square to check is \(x\circ a=b\circ x\) from degree \(-1\) to degree \(0\), that is \((a-b)x=0\). (2) By Theorem 4.2, \(c_t=\det(1-tb)\det(1-ta)^{-1}=\) \((1-bt)(1-at)^{-1}\). (3) If \(x\) is a unit, \((a-b)x=0\) gives \(a=b\), and \(c_t=1\). This agrees with Proposition 3.2 (2): \(F\to0\) is an isomorphism of \(D(A)\), and the L-series of the endomorphism of \(0\) is \(1\).

**Solution 5.3.** The relation with \(m=1\) gives \(\varepsilon_{n+1}=(-1)^n\varepsilon_n\), so \(\varepsilon_n=(-1)^{0+1+\cdots+(n-1)}=(-1)^{n(n-1)/2}\). Conversely this family satisfies the relation, because \((m+n)(m+n-1)/2=\) \(m(m-1)/2+n(n-1)/2+mn\).

**Solution 5.4.** \(Xe_1=ae_1+ce_2\) and \(Xe_2=be_1+de_2\). Then \(S^2X(e_1^2)=a^2e_1^2+2ac\,e_1e_2+c^2e_2^2\), \(S^2X(e_1e_2)=\) \(ab\,e_1^2+(ad+bc)e_1e_2+cd\,e_2^2\), and \(S^2X(e_2^2)=b^2e_1^2+2bd\,e_1e_2+d^2e_2^2\), so \(\operatorname{Tr}(S^2X)=a^2+ad+bc+d^2\). On the other side \(\det(1-tX)=\) \(1-(a+d)t+(ad-bc)t^2\), whose inverse is \(1+(a+d)t+\) \(\bigl((a+d)^2-(ad-bc)\bigr)t^2+\cdots\), and \((a+d)^2-(ad-bc)=\) \(a^2+ad+bc+d^2\), as Corollary 4.3 predicts.

## Sources

The L-series and the characteristic series of a morphism \(E\to E\otimes^{\mathbf L}M\), their behaviour on filtrations, gradings and shifts, the formula through exterior powers, and the compatibility of the shift isomorphisms with the products are due to Illusie, in his work on the cotangent complex. There \(M\) is any complex of finite tor amplitude, and the identity \(c_t(f)=\det(1-tf)\) over a local ring is stated as a consequence of a theory of determinants of perfect complexes. Here \(M\) is a complex in degrees \(\leq0\), and the determinant identity is deduced from the additivity of the L-series on the filtration of a complex by the subcomplexes \(F^{\geq p}\). The identity of Corollary 4.3 is a form of MacMahon's master theorem.

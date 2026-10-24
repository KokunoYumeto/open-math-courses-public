# Bott classes of a vector field as generalized fractions

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Let \(\xi=\sum_jf_j\partial_j\) be a vector field on an affine scheme \(X\) over a ring \(k\) whose differentials are free on \(\mathrm dx_1,\ldots,\mathrm dx_n\). Let \(Y=V(f_1,\ldots,f_n)\) be its zero set and \(U=X\smallsetminus Y\). The lesson on Chern classes with supports attaches a class \(P(N,D)\in H^n_Y(X,\Omega^n)\) to Bott's partial connection \(D\) on the normal module \(N=\Theta/\mathcal O_X\xi\) over \(U\), for every polynomial \(P\) isobaric of weight \(n\). This lesson computes these classes.

With \(J=(\partial_jf_i)\), the total class \(c_t(N,D)\) is \(\det(1-tJ)\) with \(t^r\) replaced by the \(r\)-th power of one class \(e\) of degree one. The power \(e^n\) is the generalized fraction \([\omega_x/(f_1,\ldots,f_n)]\), where \(\omega_x=\mathrm dx_1\wedge\cdots\wedge\mathrm dx_n\): the image, under the boundary map of the triangle of cohomology with supports, of the Čech cocycle \(\omega_x/(f_1\cdots f_n)\) of the covering of \(U\) by the \(D(f_i)\). Hence
\[
P(N,D)=(-1)^n\Bigl[\frac{P(J)\,\omega_x}{f_1,\ldots,f_n}\Bigr],
\]
where \(P(J)\) is \(P\) evaluated on the coefficients of \(\det(1+tJ)\). The only hypothesis is the injectivity of \(a\mapsto a\xi\). The zero set is arbitrary, and the formula holds in every characteristic. In particular it holds at an isolated, possibly non-reduced, zero of a vector field on a smooth variety.

Two steps fix the signs.
- The product of the ring of Chern classes is a composite of morphisms of the derived category (Lemma 1.1). So \(e^n\) is an iterated connecting morphism of the Koszul complex of the contraction by \(\xi\), which Čech cochains compute (Lemma 1.3, Proposition 3.1).
- The localized class of a free module with \(\nabla_\xi=\xi-A\) is computed from its definition (Proposition 2.3). A Whitney formula for horizontal exact sequences (Proposition 2.5) reduces \(N\) to the tangent module.

**Prerequisites.**
- [*Chern classes with supports from partial connections*](chern-classes-with-supports-from-partial-connections.md): Conventions, Propositions 1.2, 1.3, the paragraph on rings and modules, Definitions 2.1, 2.3, 2.6, 3.2, Lemmas 2.2, 2.4, 2.5, 3.1, Theorem 3.3 and its proof, Proposition 4.1, Corollary 4.2, Exercise 6.5.
- [*L-series of endomorphisms of perfect complexes*](l-series-of-endomorphisms-of-perfect-complexes.md): Conventions, Definition 1.1, Propositions 1.2, 1.3, 3.2 (1), Theorem 3.3, the paragraph before Lemma 4.1, Lemma 4.1, Theorem 4.2.
- [*Chern classes of perfect complexes*](chern-classes-of-perfect-complexes.md): Lemma 2.1, the proof of Proposition 2.4.
- [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md): Exercise 4.4.
- [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md): Theorem 2.6.
- [*Filtered derived categories*](filtered-derived-categories.md): Lemma 2.1.
- [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md): Proposition 3.2.
- From the AI-integrated Stacks project:
  - the triangle of a short exact sequence [[Stacks, Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)];
  - cohomology with support [[Tag 0A39](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-cohomology-support)];
  - quasi-coherent modules on affine schemes [[Tag 01XB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-coherent-affine-cohomology-zero)];
  - bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)];
  - the snake lemma [[Tag 010H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-snake)].

## Conventions

The following are as in the lesson on Chern classes with supports: \(\mathcal T=\operatorname{Top}^{\mathrm o}(i)\) with its ring \(B^{\mathrm o}\); the functors \(p^{-1}\), \(\varepsilon_U^{-1}\), \(\varepsilon_{U*}\); the principal parts \(P_{\mathrm d}(E)\) with \(\pi,\iota,\mathrm d^1\); the isomorphism \(\kappa\); and \(H^n(T,K)=\operatorname{Hom}_{D(O)}(O,K[n])\). The isomorphisms \(\tau\), the symmetry \(\sigma\) and the shifts of morphisms, without sign, are those of the Conventions of the lesson on L-series.

**Cones and connecting morphisms.** For an exact sequence \(0\to X\xrightarrow{u}Y\xrightarrow{w}Z\to0\) of complexes, the cone is \(C(u)^n=Y^n\oplus X^{n+1}\) with \(d(y,x)=(dy+u(x),-dx)\). It carries the maps \(p(y,x)=x\) to \(X[1]\) and \(q(y,x)=w(y)\) to \(Z\). The connecting morphism is \(\delta=-p\circ q^{-1}\) [Tag 0152].

Let \(z\) be a cocycle of \(Z\), and choose \(y\) with \(w(y)=z\) and \(x\) with \(dy=u(x)\). Then \((y,-x)\) is a cocycle of \(C(u)\) with \(q(y,-x)=z\) and \(-p(y,-x)=x\). So \(\delta\) carries the class of \(z\) to the class of \(x\). A morphism of short exact sequences gives a morphism of triangles [Tag 0152].

**Rings of classes.** Let \(K\) be a flat module on a ringed topos \((T,O)\). The truncations \(L\Lambda^rK\to\Lambda^rK\) are isomorphisms (Theorem 2.6 of the lesson on filtered and graded powers). They are compatible with the products, the product of \(\Lambda K\) being \(\wedge\) (Lemma 2.1 of the lesson on Chern classes of perfect complexes). Through them the ring \(\operatorname{Hom}(O,L\Lambda^\bullet(K)[1])\) of Definition 1.1 of the lesson on L-series is \(\prod_rH^r(T,\Lambda^rK)\), with
\[
ab=\wedge[p+q]\circ\tau\circ(a\otimes b)
\]
for \(a\), \(b\) of degrees \(p\), \(q\). It is commutative (Proposition 1.2 (2) there). An element \(s\in\Gamma(T,O)\) in degree \(0\) multiplies by composition, \(sa=a\circ s\).

**Čech complexes.** Let \(S\) be a scheme, \(\mathcal U=(U_1,\ldots,U_m)\) a finite open covering and \(G\) an \(\mathcal O_S\)-module. Put
\[
\mathcal C^r(\mathcal U,G)=\prod_{i_0<\cdots<i_r}j_*\bigl(G|_{U_{i_0\cdots i_r}}\bigr),
\]
with \(j\) the inclusions, and give it the differential
\[
\begin{aligned}(dc)_{i_0\cdots i_{r+1}}&=\textstyle\sum_{l=0}^{r+1}(-1)^l\\&\quad\cdot c_{i_0\cdots\widehat{i_l}\cdots i_{r+1}}.\end{aligned}
\]
Let \(\gamma\colon G\to\mathcal C^0(\mathcal U,G)\) be the augmentation, and put \(\check C^r(\mathcal U,G)=\Gamma(S,\mathcal C^r(\mathcal U,G))\).

## 1. Products, connecting morphisms and Čech classes

**Lemma 1.1 (products as composites).** Let \(F\), \(G\) be flat \(O\)-modules in degree \(0\) on a ringed topos \((T,O)\), and \(a\colon O\to F[p]\), \(b\colon O\to G[q]\) morphisms of \(D(O)\). Then
\[
\tau\circ(a\otimes b)=(a\otimes1_G)[q]\circ b,
\]
where \(a\otimes1_G\colon\) \(G=\) \(O\otimes G\to\) \(F[p]\otimes G=\) \((F\otimes G)[p]\). In particular, let \(K\) be a flat module whose exterior powers are flat, \(a\in H^p(T,\Lambda^pK)\) and \(b\in H^q(T,\Lambda^qK)\). Then
\[
ab=\wedge[p+q]\circ(a\otimes1_{\Lambda^qK})[q]\circ b.
\]

**Proof.** \(F\) and \(G\) are K-flat [Tag 06YQ], so the tensor products are formed termwise. By functoriality, \(a\otimes b=(a\otimes1_{G[q]})\circ(1_O\otimes b)\), and \(1_O\otimes b\) is \(b\) through \(O\otimes G[q]=G[q]\).

The isomorphism \(\tau\colon Z\otimes G[q]\to(Z\otimes G)[q]\), \(z\otimes y\mapsto(-1)^{q|z|}z\otimes y\), is natural in \(Z\).
- For \(Z=O\) it is the identity.
- For \(Z=F[p]\) it is the isomorphism \(F[p]\otimes G[q]\to(F\otimes G)[p+q]\) of the Conventions, since both carry the sign \((-1)^{q|z|}\) with \(|z|\) the degree in \(F[p]\).

Naturality for \(a\colon O\to F[p]\) gives \(\tau\circ(a\otimes1_{G[q]})=(a\otimes1_G)[q]\). The last statement is the case \(F=\Lambda^pK\), \(G=\Lambda^qK\), combined with the product formula of the Conventions. \(\square\)

**Lemma 1.2.** Let \(0\to X\xrightarrow{u}Y\xrightarrow{w}Z\to0\) be an exact sequence of complexes of \(O\)-modules with connecting morphism \(\delta\), and \(G\) a flat module in degree \(0\). The sequence \(0\to X\otimes G\to Y\otimes G\to Z\otimes G\to0\) is exact, and its connecting morphism is
\[
\delta\otimes1_G\colon Z\otimes G\to(X\otimes G)[1].
\]

**Proof.** Exactness holds because \(G\) is flat. The functor \(-\otimes G\) computes derived tensor products, \(G\) being K-flat [Tag 06YQ]. Since \(G\) is in degree \(0\), \(C(u\otimes1)=C(u)\otimes G\) with the same differential, and the maps \(p\), \(q\) of \(C(u\otimes1)\) are \(p\otimes1\), \(q\otimes1\). So the connecting morphism is \(-(p\otimes1)\circ(q\otimes1)^{-1}=\delta\otimes1_G\). \(\square\)

**Lemma 1.3 (Čech classes).** Let \(S\) be a separated scheme and \(\mathcal U=(U_1,\ldots,U_m)\) a covering of \(S\) by affine open subsets.

1. For every quasi-coherent \(G\), \(\gamma\colon G\to\mathcal C^\bullet(\mathcal U,G)\) is a quasi-isomorphism. For every exact sequence of quasi-coherent modules, the sequence of their Čech complexes is exact.
2. For a cocycle \(c\in\check C^r(\mathcal U,G)\), let \(\tilde c\colon\mathcal O_S\to\mathcal C^\bullet(\mathcal U,G)[r]\) be the map of complexes \(1\mapsto c\), and put \(\operatorname{cl}(c)=\gamma[r]^{-1}\circ\tilde c\in H^r(S,G)\). Then \(\operatorname{cl}\) is \(\Gamma(S,\mathcal O_S)\)-linear, natural in \(G\), and zero on coboundaries. For \(g\in G(S)\), \(\operatorname{cl}(\gamma(g))=g\).
3. Let \(0\to G'\xrightarrow{u}G\xrightarrow{w}G''\to0\) be an exact sequence of quasi-coherent modules with connecting morphism \(\partial\). Let \(c\) be an \(r\)-cocycle of \(G''\), \(b\in\check C^r(\mathcal U,G)\) with \(w(b)=c\), and \(a\in\check C^{r+1}(\mathcal U,G')\) with \(u(a)=db\). Then \(a\) is a cocycle and \(\partial[r]\circ\operatorname{cl}(c)=\operatorname{cl}(a)\).

**Proof.** (1) Exactness of the augmented complex may be checked on each \(U_l\). Extend cochains to all tuples of indices by alternation: zero on tuples with a repeated index, and \(c_{i_{\pi(0)}\cdots}=\operatorname{sgn}(\pi)c_{i_0\cdots}\). This identifies \(\mathcal C^\bullet\) with the alternating Čech complex, whose differential is given by the same formula on all tuples.

Over open subsets of \(U_l\), put \(h(c)_{i_0\cdots i_{r-1}}=c_{l\,i_0\cdots i_{r-1}}\), and \(h(c)=c_l\) in degree \(0\). Then:
- \(h\gamma=1\);
- \(\gamma h+hd=1\) in degree \(0\), since \((hdc)_i=c_i-c_l\);
- \(dh+hd=1\) in positive degrees, the terms \(c_{l\cdots}\) cancelling.

For the second assertion, let \(W\subseteq S\) be an affine open subset. Then \(W\cap U_{i_0\cdots i_r}\) is affine, as \(S\) is separated, and \(H^1\) of a quasi-coherent module on it vanishes [Tag 01XB]. So the sections of \(G\) over it map onto those of \(G''\). Affine open subsets form a basis, so each \(j_*G\to j_*G''\) is surjective, and \(j_*\) is left exact.

(2) \(\tilde c\) is a map of complexes because \(dc=0\). Linearity and naturality are clear. If \(c=db'\), then \(\tilde c=d\circ h\) for the map \(h\colon1\mapsto(-1)^rb'\) of degree \(-1\), the differential of \(\mathcal C^\bullet[r]\) being \((-1)^rd\). So \(\tilde c\) is null-homotopic and vanishes in \(D\). Finally \(\widetilde{\gamma(g)}=\gamma\circ g\).

(3) \(u(da)=d(db)=0\), and \(u\) is injective, so \(a\) is a cocycle. By (1) the Čech complexes form an exact sequence; let \(\partial_{\mathcal C}\) be its connecting morphism. By the Conventions, the map \(\beta\colon1\mapsto(b,-a)\) into the shifted cone is a map of complexes. It satisfies \(q[r]\circ\beta=\tilde c\) and \(-p[r]\circ\beta=\tilde a\). Since \(q\) is a quasi-isomorphism, \(\partial_{\mathcal C}[r]\circ\tilde c=\tilde a\).

The augmentations form a morphism of short exact sequences, so \(\gamma_{G'}[1]\circ\partial=\partial_{\mathcal C}\circ\gamma_{G''}\) [Tag 0152]. Hence
\[
\begin{aligned}\partial[r]\circ\operatorname{cl}(c)&=\gamma_{G'}[r+1]^{-1}\circ\partial_{\mathcal C}[r]\circ\tilde c\\&=\operatorname{cl}(a).\qquad\square\end{aligned}
\]

## 2. The localized class of a free module

**2.0. Setting.** Let \(k\) be a ring and \(X=\operatorname{Spec}R\) an affine \(k\)-scheme with elements \(x_1,\ldots,x_n\in R\), \(n\geq1\), such that \(\Omega=\Omega_{X/k}\) is free on \(\mathrm dx_1,\ldots,\mathrm dx_n\). Take \(A=k\), \(B=\mathcal O_X\) and the universal derivation, as in Section 4 of the lesson on Chern classes with supports. Then \(\Theta=\mathcal Hom(\Omega,B)\) is free on the dual basis \(\partial_j\). A derivation \(\delta\) equals \(\sum_j\delta(x_j)\partial_j\), both having the same values on the \(\mathrm dx_j\).

Let \(f_1,\ldots,f_n\in R\) be such that \(R\to R^n\), \(a\mapsto(af_j)_j\), is injective. Put
- \(\xi=\sum_jf_j\partial_j\), \(Y=V(f_1,\ldots,f_n)\), \(U=X\smallsetminus Y\), \(U_i=D(f_i)\);
- \(\mathcal F=B\xi\) and \(N=\Theta/\mathcal F\);
- \(J=(\partial_jf_i)_{i,j}\), \(\omega_x=\mathrm dx_1\wedge\cdots\wedge\mathrm dx_n\), and \(\theta_i=\mathrm dx_i/f_i\in\Omega(U_i)\).

Write sections of \(B^m\) as columns, and \(\det(1+tA)=\sum_r\sigma_r(A)t^r\) for \(A\in M_m(R)\).

The contraction \(\iota_\xi\colon\Lambda^{r}\Omega\to\Lambda^{r-1}\Omega\) is the antiderivation with \(\iota_\xi(\mathrm db)=\xi(b)\). Let \(v\colon\Omega|_U\to B|_U\) be its restriction, and \(L=\operatorname{Ker}v\). Since \(\iota_\xi(\mathrm dx_i)=f_i\), we have \(v(\theta_i)=1\).

**Lemma 2.1.**

1. \(\mathcal F\) satisfies the hypotheses of Proposition 4.1 of the lesson on Chern classes with supports, and \(N\) those of Corollary 4.2 there with \(q=n-1\); \(N\) has perfect amplitude in \([-1,0]\). Evaluation at \(\xi\) identifies \(M\) with \(B|_U\), and the sequence (2.1) there with \(0\to L\to\Omega|_U\xrightarrow{v}B|_U\to0\). This replacement changes neither \(L\), nor \(K=(L\to\Omega)\), nor the localized classes. A partial connection on \(E|_U\) is an additive \(\nabla_\xi\colon E|_U\to E|_U\) with \(\nabla_\xi(bm)=b\nabla_\xi(m)+\xi(b)m\). Bott's is \(\nabla_\xi(\bar s)=\overline{[\xi,s]}\), and \([\xi,s]=\xi(s)-Js\) for \(s\in\Theta=B^n\).
2. On \(U_i\), \(\Omega=L\oplus B\theta_i\) and \(L\) is free of rank \(n-1\); so \(\Lambda^nL=0\). For \(\lambda\in\Lambda^rL\), \(\iota_\xi(\omega\wedge\lambda)=v(\omega)\lambda\), and the sequence
\[
\begin{aligned}&\mathcal K_r \colon\ 0 \to\Lambda^{r+1}L\\&\quad \to\Lambda^{r+1}\Omega|_U \xrightarrow{\iota_\xi}\Lambda^rL\\&\quad \to0\end{aligned}
\]
is exact. The map \(\psi\colon\Lambda^{n-1}L\to\Omega^n|_U\), \(\lambda\mapsto\theta\wedge\lambda\) for any local \(\theta\) with \(v(\theta)=1\), is a well defined isomorphism. Moreover \(\omega\wedge\lambda=\psi(v(\omega)\lambda)\) for \(\lambda\in\Lambda^{n-1}L\), and \(\omega\wedge\lambda=0\) if moreover \(\omega\) is a section of \(L\).

**Proof.** (1) By hypothesis \(B\to\Theta\), \(a\mapsto a\xi\), is injective. So \(\mathcal F\cong B\), and \(N\) is quasi-isomorphic to the strictly perfect complex \(B\to\Theta\) in degrees \(-1\), \(0\). On \(U_i\), \(f_i\) is a unit, so \(\Theta=B\xi\oplus\bigoplus_{j\neq i}B\partial_j\), the coefficient of \(\partial_i\) in \(a\xi\) being \(af_i\). Thus \(\mathcal F|_U\) is free on \(\xi\) and a direct summand, and \(N|_{U_i}\) is free of rank \(n-1\). Involutivity follows from \([a\xi,b\xi]=(a\xi(b)-b\xi(a))\xi\).

The module \(M\) is free on the form dual to \(\xi\), and \(v(\omega)(\xi)=\xi(\omega)=\iota_\xi\omega\). Let \(\epsilon\colon M\to B|_U\) be evaluation at \(\xi\). Then \(D\mapsto(\epsilon\otimes1)\circ D\) is a bijection from the partial connections relative to the sequence of Proposition 4.1 there to those relative to the sequence with \(\iota_\xi\), and \(D\) and \((\epsilon\otimes1)\circ D\) have the same kernel. So the sequences (2.4) there, the classes \(\operatorname{at}(E,D)\) and their Chern classes are the same for both.

Lemma 2.4 there gives the description of partial connections, as \(v(\mathrm db)=\xi(b)\). Proposition 4.1 (2) there gives Bott's. Finally \([\xi,s](x_j)=\xi(s_j)-s(f_j)\) and \(s(f_j)=\sum_l\partial_lf_j\,s_l=(Js)_j\).

(2) Write \(\omega=(\omega-v(\omega)\theta_i)+v(\omega)\theta_i\); this gives \(\Omega=L\oplus B\theta_i\) on \(U_i\). Then \(L\cong\mathcal Hom(N|_U,B|_U)\) is free of rank \(n-1\) on \(U_i\) (Proposition 4.1 (1) there). So \(\Lambda^{r+1}\Omega=\Lambda^{r+1}L\oplus\theta_i\wedge\Lambda^rL\) there, with \(\lambda\mapsto\theta_i\wedge\lambda\) injective on \(\Lambda^rL\).

The antiderivation \(\iota_\xi\) equals \(v\) on \(\Omega\) and kills \(\Lambda^\bullet L\) in positive degrees. Hence \(\iota_\xi(\omega\wedge\lambda)=v(\omega)\lambda\), and \(\mathcal K_r\) is exact. For \(r=n-1\), \(\Lambda^nL=0\) gives \(\Omega^n|_{U_i}=\theta_i\wedge\Lambda^{n-1}L\).

If \(v(\theta')=1\), then \(\theta'-\theta_i\) is a section of \(L\), and \((\theta'-\theta_i)\wedge\lambda\) lies in the image of \(\Lambda^nL=0\). This gives the independence of \(\psi\) from \(\theta\). It also gives the identity \(\omega\wedge\lambda=\) \((\omega-v(\omega)\theta)\wedge\lambda+v(\omega)\theta\wedge\lambda=\) \(v(\omega)\theta\wedge\lambda\). \(\square\)

**2.2. The class \(e\).** Put \(V=p^{-1}\Omega=(\Omega|_U\xrightarrow1\Omega)\) and \(Q=(B|_U\to0)\). Let
\[
0\to K\to V\to Q\to0\tag{2.2}
\]
be the sequence of \(B^{\mathrm o}\)-modules defined as follows. Its first map is the inclusion of \(L\) on \(U\) and the identity of \(\Omega\) on \(X\). Its second map is \(v\) on \(U\) and \(0\) on \(X\). It is exact at both levels.

Let \(\rho\colon B^{\mathrm o}\to Q\) have components \(1\) and \(0\), and \(\delta\colon Q\to K[1]\) be the connecting morphism of (2.2). Put
\[
e=\delta\circ\rho\in H^1(\mathcal T,K).
\]
Note that \(\Gamma(\mathcal T,B^{\mathrm o})=R\), a global section being a pair \((t|_U,t)\). The levels of \(K\) are locally free of finite rank, so the exterior powers of \(K\) are flat (paragraph on rings and modules there) and Lemma 1.1 applies to \(K\).

**Proposition 2.3 (free modules).** In 2.0, let \(E=B^m\) with basis \(\epsilon_1,\ldots,\epsilon_m\), let \(A\in M_m(R)\), and let \(D\) be the partial connection with \(\nabla_\xi(s)=\xi(s)-As\) on \(E|_U\).

1. \(\operatorname{at}(E,D)=(1\otimes e)\circ p^{-1}(A)\), as morphisms \(p^{-1}E\to p^{-1}E\otimes K[1]\).
2. \(c^r(E,D)=(-1)^r\sigma_r(A)\,e^r\) for every \(r\geq0\), the power taken in the ring of Definition 3.2 of the lesson on Chern classes with supports.

**Proof.** (1) By Lemma 2.4 there, \(D((c,\omega)\otimes\epsilon_l)=c\nabla_\xi(\epsilon_l)+v(\omega)\epsilon_l\), and \(\nabla_\xi(\epsilon_l)=-A\epsilon_l\). The map
\[
\begin{aligned}&\Sigma\colon E\oplus(\Omega\otimes E)\to P_{\mathrm d}(E),\\&(s,\eta)\mapsto\textstyle\sum_l(s_l,0)\otimes\epsilon_l+\iota(\eta),\end{aligned}
\]
is a \(B\)-linear isomorphism, since \(P_{\mathrm d}(E)=\bigoplus_lP_{\mathrm d}\otimes\epsilon_l\). It satisfies \(\pi\Sigma(s,\eta)=s\) and
\[
D\Sigma(s,\eta)=-As+(v\otimes1)\eta.
\]
Through \(\Sigma\), the middle term of the sequence (2.4) there is \(E\oplus(\Omega\otimes E)\) on \(X\), and on \(U\) the submodule of pairs with \((v\otimes1)\eta=As\), the arrow being the inclusion. The first map of (2.4) is \(\eta\mapsto(0,\eta)\) and the last is \((s,\eta)\mapsto s\).

Consider three maps from (2.4) into the sequence (2.2)\(\otimes p^{-1}E\):
- the identity on the first terms;
- \((s,\eta)\mapsto\eta\) at both levels on the middle terms;
- \((\rho\otimes1)\circ p^{-1}(A)\), with components \(A\) on \(U\) and \(0\) on \(X\), on the last terms.

They form a morphism of short exact sequences of \(B^{\mathrm o}\)-modules: on \(U\) the middle square commutes because \((v\otimes1)\eta=As\), and the arrows are respected. By [Tag 0152] and Lemma 1.2, the connecting morphism of (2.4) is
\[
\begin{aligned}&(\delta\otimes1)\circ(\rho\otimes1)\circ p^{-1}(A)\\&\quad =(e\otimes1)\circ p^{-1}(A).\end{aligned}
\]
For the flat module \(K\) and the module \(p^{-1}E\), both in degree \(0\), \(\kappa\) is \(k\otimes m\mapsto m\otimes k\). This is the symmetry \(K[1]\otimes p^{-1}E\to p^{-1}E\otimes K[1]\), which carries no sign as \(|m|=0\). By naturality of the symmetry, \(\kappa\circ(e\otimes1)=1\otimes e\). Definition 2.6 there gives (1).

(2) The objects \(B^{\mathrm o}\) and \(K[1]\) lie in \(D^{\leq0}\). By Proposition 3.2 (1) of the lesson on L-series, \(L_t(\operatorname{at}(E,D))=e_*L_t(p^{-1}(A))\), where \(e_*\) is the ring homomorphism of Proposition 1.2 (3) there. By Theorem 4.2 and Lemma 4.1 there, \(c_t(p^{-1}(A))=\det(1-tA)\) in \(\operatorname{Hom}(B^{\mathrm o},LS^\bullet(B^{\mathrm o}))=R[[t]]\), an identification of rings (the paragraph before Lemma 4.1). Hence \(c_t(\operatorname{at}(E,D))=e_*(\det(1-tA))\).

The map \(e_*\) is \(R\)-linear and the identity in degree \(0\), and it carries \(t\) to \(LS^1(e)=e\). Being a ring homomorphism, it carries \(t^r\) to \(e^r\). The ring isomorphism \(\sigma^S\) (Proposition 1.3 there) is the identity in degrees \(0\) and \(1\) (Exercise 4.4 of the lesson on Koszul complexes). So \(c_t(E,D)=\sum_r(-1)^r\sigma_r(A)e^r\). \(\square\)

**Lemma 2.4 (filtered connecting morphisms).** Let \(0\to X\xrightarrow{u}Y\xrightarrow{w}Z\to0\) be maps of finitely filtered complexes of modules on a ringed topos, exact on every \(F^p\). Filter \(C(u)\) by \(F^pC(u)=C(F^pu)\). Then \(q\colon C(u)\to Z\) is a filtered quasi-isomorphism, and \(\delta^F=-p\circ q^{-1}\colon Z\to X[1]\) is a morphism of \(DF\). Its underlying morphism and its \(\operatorname{gr}^p\) are the connecting morphisms of the underlying sequence and of the sequences \(0\to\operatorname{gr}^pX\to\operatorname{gr}^pY\to\operatorname{gr}^pZ\to0\).

**Proof.** The sequences \(0\to F^{p+1}\to F^p\to\operatorname{gr}^p\to0\) and the snake lemma [Tag 010H] show that the sequences of graded pieces are exact. The map \(q\) is a quasi-isomorphism on every \(F^p\) [Tag 0152]. Hence it is one on every \(\operatorname{gr}^p\), by the five lemma on these sequences. So it is a filtered quasi-isomorphism (Lemma 2.1 of the lesson on filtered derived categories). Forgetting the filtration and taking \(\operatorname{gr}^p\) carry \(C(u)\), \(p\) and \(q\) to the cones and maps of the underlying and graded sequences. \(\square\)

**Proposition 2.5 (Whitney formula for horizontal sequences).** In the setting of Section 2 of the lesson on Chern classes with supports, let \(0\to E'\xrightarrow{\alpha}E\xrightarrow{\beta}E''\to0\) be an exact sequence of \(B\)-modules of bounded perfect amplitude. Let \(D'\), \(D\), \(D''\) be partial connections on their restrictions to \(U\) with
\[
\begin{gathered}D\circ P_{\mathrm d}(\alpha)=(1\otimes\alpha)\circ D',\\ D''\circ P_{\mathrm d}(\beta)=(1\otimes\beta)\circ D.\end{gathered}
\]
Then \(c_t(E,D)=c_t(E',D')\,c_t(E'',D'')\).

**Proof.** As a right module, \(P_{\mathrm d}\cong B\oplus\Omega\) (proof of Lemma 2.2 there), and \(\Omega\) is flat, so \(P_{\mathrm d}(-)\) is exact. On \(U\), the maps \(D'\), \(D\), \(D''\) form a morphism from the sequence of the \(P_{\mathrm d}(-)|_U\) to the exact sequence of the \(M\otimes(-)|_U\). Since \(D'\) is surjective (Lemma 2.5 there), the snake lemma gives an exact sequence \(0\to\operatorname{Ker}D'\to\operatorname{Ker}D\to\operatorname{Ker}D''\to0\).

So the sequences (2.4) there of \(E'\) and \(E''\) are the subsequence and the quotient of that of \(E\), the first terms by the flatness of \(L\) and \(\Omega\). Filter each term of the sequence of \(E\) by \(F^0=\) everything, \(F^1=\) the term of \(E'\), \(F^2=0\). Lemma 2.4 gives a morphism \(\delta^F\) of \(DF(B^{\mathrm o})\). Its underlying morphism and graded pieces are the connecting morphisms of the sequences (2.4) of \(E\), \(E'\) (for \(p=1\)) and \(E''\) (for \(p=0\)).

The termwise filtered complex \(K\otimes p^{-1}E\), with \(K\) in filtration \([0,0]\), represents the filtered tensor product, \(K\) being K-flat (Proposition 3.2 of the lesson on filtered tensor products). The map \(\kappa\) is a filtered isomorphism compatible with graded pieces. So \(\operatorname{at}^F=\kappa\circ\delta^F\colon p^{-1}E\to p^{-1}E\otimes K[1]\) is a morphism of \(DF\), with
- underlying morphism \(\operatorname{at}(E,D)\),
- \(\operatorname{gr}^1=\operatorname{at}(E',D')\),
- \(\operatorname{gr}^0=\operatorname{at}(E'',D'')\).

The graded pieces \(p^{-1}E'\), \(p^{-1}E''\) have perfect amplitude in a common interval (Lemma 3.1 there) and lie in \(D^{\leq0}\). By Theorem 3.3 (1), (2) of the lesson on L-series, \(L_t(\operatorname{at}(E,D))=\) \(L_t(\operatorname{at}(E',D'))L_t(\operatorname{at}(E'',D''))\). The ring is commutative, so the same holds for \(c_t=L_t^{-1}\), and \(\sigma^S\) is a ring isomorphism. \(\square\)

## 3. The top power of \(e\)

**3.0. Generalized fractions.** In 2.0, \(U\) is separated, being open in an affine scheme, and \(\mathcal U=(U_1,\ldots,U_n)\) covers \(U\) by affine open subsets. Its only \((n-1)\)-simplex is \((1,\ldots,n)\), with \(U_{1\cdots n}=D(f_1\cdots f_n)\), and \(\check C^n(\mathcal U,-)=0\). Let \(\eta\in\Gamma(X,\Omega^n)\). Then \(\eta/(f_1\cdots f_n)\) is an \((n-1)\)-cocycle, and we put
\[
\begin{aligned}\Bigl[\frac{\eta}{f_1,\ldots,f_n}\Bigr]&=\partial\,\operatorname{cl}\Bigl(\frac{\eta}{f_1\cdots f_n}\Bigr)\\&\in H^n_Y(X,\Omega^n),\end{aligned}
\]
where \(\partial\colon H^{n-1}(U,\Omega^n)\to H^n_Y(X,\Omega^n)\) is the boundary of the triangle of [Tag 0A39]. This class is \(R\)-linear in \(\eta\): \(\operatorname{cl}\) is \(R\)-linear (Lemma 1.3 (2)), and \(\partial\), a composite with a morphism of the derived category, commutes with composition with the multiplications by elements of \(R\).

More generally, let \(g_1,\ldots,g_n\in R\) satisfy \(V(g_1,\ldots,g_n)=Y\) as sets. The covering \((D(g_1),\ldots,D(g_n))\) of \(U\) gives in the same way a class \([\eta/(g_1,\ldots,g_n)]\). It depends only on the open sets \(D(g_i)\) and on the section \(\eta/(g_1\cdots g_n)\) of \(\Omega^n\) over \(D(g_1\cdots g_n)\).

**Proposition 3.1.** In 2.0,
\[
e^n=\Bigl[\frac{\omega_x}{f_1,\ldots,f_n}\Bigr]
\]
in \(H^n(\mathcal T,\Lambda^nK)=H^n_Y(X,\Omega^n)\) (Theorem 3.3 (2) of the lesson on Chern classes with supports).

**Proof.** *The powers on \(U\).* The functor \(\varepsilon_U^{-1}\) is exact and commutes with tensor products, exterior powers, shifts, \(\tau\) and cones. So it carries (2.2) to \(\mathcal K_0\), \(\rho\) to the identity, and \(e\) to the connecting morphism \(e_U=\partial_0\) of \(\mathcal K_0\). Being its own derived functor and commuting with \(\wedge\), \(\tau\) and tensor products of flat modules, it is also a ring homomorphism to \(\prod_rH^r(U,\Lambda^rL)\). Let \(\partial_r\) be the connecting morphism of \(\mathcal K_r\).

The maps \(\wedge\), \(\omega\otimes\lambda\mapsto\omega\wedge\lambda\) and the identity form a morphism from \(\mathcal K_0\otimes\Lambda^rL\) to \(\mathcal K_r\) (Lemma 2.1 (2)). By Lemma 1.1, Lemma 1.2 and [Tag 0152],
\[
\begin{aligned}e_U^{r+1}&=\wedge[r+1]\circ(\partial_0\otimes1)[r]\circ e_U^r\\&=\partial_r[r]\circ e_U^r.\end{aligned}
\]

*Čech cochains.* For \(0\leq r\leq n-1\), put
\[
\begin{aligned}\varepsilon^{(r)}_{i_0\cdots i_r}&=(\theta_{i_1}-\theta_{i_0})\wedge\cdots\\&\quad\wedge(\theta_{i_r}-\theta_{i_{r-1}}),\end{aligned}
\]
a section of \(\Lambda^rL\), with \(\varepsilon^{(0)}=\gamma(1)\). We show that \(\varepsilon^{(r)}\) is a cocycle and that \(e_U^r=\operatorname{cl}(\varepsilon^{(r)})\). For \(r=0\) this is Lemma 1.3 (2).

Let \(c=\varepsilon^{(r)}\) with \(r\leq n-2\), a cocycle. Then \(b_{i_0\cdots i_r}=\theta_{i_0}\wedge c_{i_0\cdots i_r}\) satisfies \(\iota_\xi(b)=c\). The cocycle relation gives \(\sum_{l\geq1}(-1)^lc_{i_0\cdots\widehat{i_l}\cdots}=-c_{i_1\cdots i_{r+1}}\), so
\[
(db)_{i_0\cdots i_{r+1}}=(\theta_{i_1}-\theta_{i_0})\wedge c_{i_1\cdots i_{r+1}},
\]
which is \(\varepsilon^{(r+1)}\), a section of \(\Lambda^{r+1}L\). Lemma 1.3 (3) for \(\mathcal K_r\) shows that \(\varepsilon^{(r+1)}\) is a cocycle and gives \(e_U^{r+1}=\partial_r[r]\circ\operatorname{cl}(c)=\operatorname{cl}(\varepsilon^{(r+1)})\).

*The power on \(\mathcal T\).* Put \(G=\Lambda^{n-1}K\). By Lemmas 1.1 and 1.2,
\[
\begin{aligned}e^n&=\wedge[n]\circ(\delta\otimes1_G)[n-1]\\&\quad\circ(\rho\otimes1_G)[n-1]\circ e^{n-1}.\end{aligned}
\]
Let \(\mathcal S\) be the sequence \(0\to\) \((0\to\Omega^n)\to\) \(p^{-1}\Omega^n\to\) \(\varepsilon_{U*}\Omega^n|_U\to\) \(0\) of Proposition 1.3 of the lesson on Chern classes with supports. The terms of (2.2)\(\otimes G\) are
\[
\begin{gathered}(L\otimes\Lambda^{n-1}L\to\Omega\otimes\Omega^{n-1}),\\ (\Omega|_U\otimes\Lambda^{n-1}L\to\Omega\otimes\Omega^{n-1}),\\ (\Lambda^{n-1}L\to0).\end{gathered}
\]
There is a morphism from (2.2)\(\otimes G\) to \(\mathcal S\) with three components:
- \(\wedge\) on the first terms, into \(\Lambda^nK=(0\to\Omega^n)\);
- \(\wedge\) at both levels on the middle terms;
- \(\psi\) on \(U\) on the last terms.

The squares commute by Lemma 2.1 (2). Hence
\[
\wedge[1]\circ(\delta\otimes1_G)=\partial_{\mathcal S}\circ\varepsilon_{U*}(\psi).
\]

The map \(\rho\otimes1_G\colon G\to\varepsilon_{U*}\Lambda^{n-1}L\) is the unit of the adjunction. Consider the isomorphism \(H^{n-1}(\mathcal T,\varepsilon_{U*}-)=H^{n-1}(U,-)\) of Proposition 1.3 there, natural in its argument. It is induced on injective resolutions by \(\Gamma(\mathcal T,\varepsilon_{U*}I)=\Gamma(U,I)\), under which a global section \((s,t)\) goes to \(s\). Composed with this isomorphism, the unit is \(\varepsilon_U^{-1}\), as in the proof of Theorem 3.3 (2) there. By Proposition 1.3 there, \(\partial_{\mathcal S}\) induces \(\partial\).

Therefore \(e^n=\partial\,\psi_*(e_U^{n-1})=\partial\operatorname{cl}(\psi(\varepsilon^{(n-1)}))\), by naturality of \(\operatorname{cl}\). Taking \(\theta=\theta_1\) on \(U_{1\cdots n}\) gives
\[
\begin{aligned}\psi(\varepsilon^{(n-1)})&=\theta_1\wedge(\theta_2-\theta_1)\wedge\cdots\\&=\theta_1\wedge\cdots\wedge\theta_n\\&=\omega_x/(f_1\cdots f_n),\end{aligned}
\]
each factor \(\theta_{l+1}-\theta_l\) reducing to \(\theta_{l+1}\) against \(\theta_1\wedge\cdots\wedge\theta_l\). \(\square\)

## 4. Bott classes

**Theorem 4.1.** In 2.0, let \(D\) be Bott's partial connection on \(N|_U\). Then:

1. \(c^r(N,D)=(-1)^r\sigma_r(J)\,e^r\) for every \(r\); that is, \(c_t(N,D)\) is \(\det(1-tJ)\) with \(t^r\) replaced by \(e^r\).
2. For every \(P\) isobaric of weight \(n\), with \(P(J)=P(\sigma_1(J),\ldots,\sigma_n(J))\in R\),
\[
\begin{aligned}P(N,D)&=(-1)^n\Bigl[\frac{P(J)\,\omega_x}{f_1,\ldots,f_n}\Bigr]\\&=\Bigl[\frac{P(-J)\,\omega_x}{f_1,\ldots,f_n}\Bigr]\end{aligned}
\]
in \(H^n_Y(X,\Omega^n)\).

**Proof.** By Lemma 2.1 (1), \(P(N,D)\in H^n_Y(X,\Omega^n)\) is defined (Corollary 4.2 of the lesson on Chern classes with supports, \(n>n-1\)).

(1) Take the partial connections \(\nabla_\xi(a)=\xi(a)\) on \(B|_U\) and \(\nabla_\xi(s)=[\xi,s]=\xi(s)-Js\) on \(\Theta|_U=B^n|_U\). The maps \(a\mapsto a\xi\) and \(s\mapsto\bar s\) commute with the maps \(\nabla_\xi\), since \([\xi,a\xi]=\xi(a)\xi\) and Bott's connection is \(\overline{[\xi,s]}\).

The modules \(P_{\mathrm d}(-)\) are generated by the sections \(\mathrm d^1(m)\) and \(\iota(\omega\otimes m)\), and \(P_{\mathrm d}(\alpha)\) commutes with \(\mathrm d^1\) and \(\iota\). On \(\mathrm d^1(m)\) both sides of the conditions of Proposition 2.5 give the maps \(\nabla_\xi\), and on \(\iota(\omega\otimes m)\) they give \(v(\omega)\) times the image of \(m\) (Lemma 2.4 there). So the maps \(D\) are horizontal in the sense of Proposition 2.5.

The modules \(B\) and \(\Theta\) are free, and \(N\) has perfect amplitude in \([-1,0]\). Proposition 2.5 gives \(c_t(\Theta,D_\Theta)=c_t(B,D_B)c_t(N,D)\). Proposition 2.3 gives \(c_t(B,D_B)=1\) (with \(A=0\)) and \(c_t(\Theta,D_\Theta)=\sum_r(-1)^r\sigma_r(J)e^r\).

(2) The ring is commutative, and scalars of degree \(0\) act by composition. So a monomial \(c^{i_1}\cdots c^{i_k}\) with \(\sum_li_l=n\) equals \((-1)^n\sigma_{i_1}(J)\cdots\sigma_{i_k}(J)e^n\). Hence \(P(N,D)=(-1)^nP(J)e^n\). Proposition 3.1, with the \(R\)-linearity of 3.0, gives the first equality. The second follows from \(\sigma_r(-J)=(-1)^r\sigma_r(J)\). \(\square\)

**Corollary 4.2 (isolated zeros).** Take 2.0 without the injectivity hypothesis. Suppose that \(R\) is noetherian and reduced, as it is when \(X\) is smooth over a field, and that no irreducible component of \(X\) is contained in \(Y\). This holds, for instance, when \(X\) has pure dimension \(n\geq1\) and \(Y\) is one closed point, possibly with a non-reduced scheme structure \(V(f_1,\ldots,f_n)\). Then \(a\mapsto a\xi\) is injective, and Theorem 4.1 holds. Replacing \(J\) by its transpose does not change \(P(J)\); replacing \(J\) by \(-J\) multiplies it by \((-1)^n\).

**Proof.** Let \(a\neq0\) satisfy \(af_j=0\) for all \(j\). The nilradical \(0\) is the intersection of the minimal primes, so \(a\notin\mathfrak q\) for some minimal prime \(\mathfrak q\). Then every \(f_j\in\mathfrak q\), and the component \(V(\mathfrak q)\) lies in \(Y\), a contradiction. A component of dimension \(n\geq1\) is not a closed point. Finally \(\det(1+tJ^{\mathsf T})=\det(1+tJ)\), and \(P\) is isobaric of weight \(n\). \(\square\)

**Remark 4.3.** In Theorem 4.1 the sign \((-1)^n\) comes from the coefficients of \(\det(1-tJ)\) in (1); the boundary convention of 3.0 contributes no sign in Proposition 3.1. With \(P\) evaluated on the coefficients of \(\det(1-tJ)\), that is on \(-J\), the sign is \(+1\). Only the identification of 3.0 of a Čech cocycle of \(U\) with a class of \(H^n_Y(X,\Omega^n)\) is used in this lesson. The class depends only on \(P(J)\) modulo \((f_1,\ldots,f_n)\) (Exercise 5.1).

## 5. Exercises

**Exercise 5.1.** In 3.0, let \(\eta=f_i\eta'\) with \(\eta'\in\Gamma(X,\Omega^n)\). Show that \([\eta/(f_1,\ldots,f_n)]=0\), and deduce that \(P(N,D)\) depends only on the class of \(P(J)\) in \(R/(f_1,\ldots,f_n)\).

**Exercise 5.2.** Let \(X=\mathbb A^n_k\) and \(\xi=\sum_jx_j\partial_j\). Show that 2.0 applies, that \(c^r(N,D)=(-1)^r\binom nr e^r\), and compute \(c_1(N,D)^n\) and \(c_n(N,D)\) as fractions. For \(n=2\), compare with Exercise 6.5 of the lesson on Chern classes with supports.

**Exercise 5.3.** Let \(X=\mathbb A^2_k=\operatorname{Spec}k[x,y]\), \(k\neq0\), and \(\xi=x^2\partial_x+y\partial_y\), with \(\omega=\mathrm dx\wedge\mathrm dy\). Show that
\[
\begin{aligned}c_1(N,D)^2&=\Bigl[\frac{\omega}{x^2,y}\Bigr]+4\Bigl[\frac{\omega}{x,y}\Bigr],\\c_2(N,D)&=2\Bigl[\frac{\omega}{x,y}\Bigr].\end{aligned}
\]

## 6. Complete solutions

**5.1.** *The case \(n\geq2\).* Let \(b\) be the \((n-2)\)-cochain of \(\mathcal U\) equal to \((-1)^{i-1}\eta'/\prod_{j\neq i}f_j\) on the simplex omitting \(i\), and \(0\) on the others. In \((db)_{1\cdots n}\) only the omission of \(i\), in position \(i-1\), contributes, so \((db)_{1\cdots n}=\eta'/\prod_{j\neq i}f_j=\eta/(f_1\cdots f_n)\). This is the only \((n-1)\)-simplex, so \(\eta/(f_1\cdots f_n)=db\), and Lemma 1.3 (2) gives \(\operatorname{cl}=0\).

*The case \(n=1\).* Here \(\eta/f_1\) is the restriction of \(\eta'\) to \(U=U_1\). Its class is that restriction (Lemma 1.3 (2)). The restriction \(H^0(X,\Omega^1)\to H^0(U,\Omega^1)\) is the second map of the triangle of [Tag 0A39] (Proposition 1.3 of the lesson on Chern classes with supports), and \(\partial\) is the third. Two consecutive maps of a distinguished triangle compose to zero, so \(\partial\) kills the class.

*The deduction.* If \(P(J)-g=\sum_ia_if_i\) with \(g,a_i\in R\), the \(R\)-linearity of 3.0 gives
\[
\begin{aligned}&\Bigl[\frac{P(J)\omega_x}{f_1,\ldots,f_n}\Bigr]-\Bigl[\frac{g\,\omega_x}{f_1,\ldots,f_n}\Bigr]\\&\quad=\textstyle\sum_i\Bigl[\frac{f_i\,a_i\omega_x}{f_1,\ldots,f_n}\Bigr]=0.\end{aligned}
\]
By Theorem 4.1 (2), \(P(N,D)=(-1)^n[g\,\omega_x/(f_1,\ldots,f_n)]\) for every \(g\) in the class of \(P(J)\).

**5.2.** *2.0 applies.* \(R=k[x_1,\ldots,x_n]\) and \(\Omega_{R/k}\) is free on the \(\mathrm dx_j\). If \(ax_1=0\) in \(R\), comparing coefficients gives \(a=0\), so \(a\mapsto(ax_j)_j\) is injective.

*The Chern classes.* Here \(f_j=x_j\) and \(J=1_n\), so \(\det(1+tJ)=(1+t)^n\) and \(\sigma_r(J)=\binom nr\). Theorem 4.1 (1) gives \(c^r(N,D)=(-1)^r\binom nre^r\). Theorem 4.1 (2) with \(P=c_1^n\), \(P(J)=n^n\), and with \(P=c_n\), \(P(J)=1\), gives
\[
\begin{aligned}c_1(N,D)^n&=(-1)^nn^n\Bigl[\frac{\omega_x}{x_1,\ldots,x_n}\Bigr],\\c_n(N,D)&=(-1)^n\Bigl[\frac{\omega_x}{x_1,\ldots,x_n}\Bigr].\end{aligned}
\]
For \(n=2\), with \(\omega=\mathrm dx\wedge\mathrm dy\), \(c_1(N,D)^2=4[\omega/(x,y)]\) and \(c_2(N,D)=[\omega/(x,y)]\).

*The comparison.* By Lemma 2.1 (1) with \(J=1\), \(\nabla_\xi(\bar s)=\overline{\xi(s)-s}\), so \(\nabla_\xi(\bar\partial_x)=-\bar\partial_x\) and \(\nabla_\xi(\bar\partial_y)=-\bar\partial_y\). This is the formula of Exercise 6.5 (2) there, read through evaluation at \(\xi\). Exercise 6.5 (3) there shows that \(P(N)\) comes from \(H^n_{\{0\}}(X,\Omega^n)\); here the local classes themselves are computed as fractions.

**5.3.** *2.0 applies.* \(R=k[x,y]\), \(f_1=x^2\), \(f_2=y\), and \(ay=0\) implies \(a=0\), so 2.0 applies. As sets, \(Y=V(x^2,y)=V(x,y)\), and \(D(x^2)=D(x)\).

*The coefficients.* \(J=\operatorname{diag}(2x,1)\), so \(\sigma_1(J)=1+2x\), \(\sigma_2(J)=2x\) and \(\sigma_1(J)^2=1+4x+4x^2\).

*The first class.* Theorem 4.1 (2) with \(P=c_1^2\) gives
\[
\begin{aligned}c_1(N,D)^2&=\Bigl[\frac{\omega}{x^2,y}\Bigr]+4\Bigl[\frac{x\,\omega}{x^2,y}\Bigr]\\&\quad+4\Bigl[\frac{x^2\omega}{x^2,y}\Bigr].\end{aligned}
\]
The last term vanishes by Exercise 5.1, with \(i=1\) and \(\eta'=4\omega\). The Čech cocycle of the middle term is \(x\omega/(x^2y)=\omega/(xy)\) on \(D(xy)\), for the covering \((D(x),D(y))\). By 3.0 the middle class is therefore \([\omega/(x,y)]\).

*The second class.* With \(P=c_2\), \(P(J)=2x\), the same reasoning gives \(c_2(N,D)=[2x\,\omega/(x^2,y)]=2[\omega/(x,y)]\).

## Sources

The partial connection on the normal sheaf of a foliation is due to Bott. The localization at the singular set of the characteristic classes of the normal sheaf, and their expression by Grothendieck residues of Jacobian fractions for vector fields with isolated zeros, are due to Baum and Bott. Chern classes with supports obtained from partial connections, and the problem of making them explicit in terms of the local behaviour of the partial connection, are due to Illusie, in his work on the cotangent complex. Generalized fractions and cohomology with supports are due to Grothendieck. The homological algebra used here is that of the Stacks project. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.

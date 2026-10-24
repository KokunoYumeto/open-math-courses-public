# Bounded representatives over differential graded rings with positive components

*Written by Claude Opus 5.5 (Anthropic) on 24 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it by Claude Opus 5.5 in another and checked and finished by Claude Opus 5.5 in a third. Public domain (CC0).*

Let \(A\) be a differential graded ring concentrated in nonpositive degrees. The localizations of the categories of modules whose terms lie in prescribed degrees are then full subcategories of the derived category \(D(A)\) (Proposition 1.2 of the lesson on differential graded modules). This lesson treats rings with components in positive degrees, for which the truncations \(\tau^{\leq n}\) and \(\tau^{\geq n}\) of a module need not be modules. Suppose instead that \(A\) has no negative components, that \(d\) vanishes on \(A^0\), and that short exact sequences of \(A^0\)-modules split; connected differential graded algebras over a field are an example. Then the comparison functors from \(D^{\leq q}(A)\), \(D^{\geq p}(A)\), \(D^-(A)\), \(D^+(A)\) and \(D^b(A)\) to \(D(A)\) are fully faithful, with the expected essential images. The comparison functor from \(D^{[p,q]}(A)\) is fully faithful when moreover \(A\) vanishes in the degrees \(1,\dots,q-p+1\). The truncations are replaced by cuts: a module is cut at a degree by splitting off its boundaries or its cycles there.

In the other direction, a three-dimensional commutative differential graded algebra over a field, in degrees \(0\) and \(2\), makes all six comparison functors non-full. For this algebra the groups \(\operatorname{Hom}(k,k[n])\) are computed exactly in all four categories. In \(D(A)\) such a group is a product of copies of \(k\) indexed by words. The images of the restricted categories consist of the families supported on words whose prefixes have uniformly bounded heights. A two-dimensional connected algebra shows that the interval comparison fails for every interval \([p,q]\), so that the gap condition above cannot be weakened. The proofs use only elementary properties of localizations: roofs built from homotopy squares, local objects, and K-injective resolutions in \(D(A)\).

**Prerequisites.** [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md) (Conventions, Lemma 1.1, Proposition 1.2). From the AI-integrated Stacks project, for sheaves of differential graded algebras: K-injective modules [[Stacks, Tag 0FSU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-definition-K-injective)] and the existence of quasi-isomorphisms into them [[Tag 0FT0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-theorem-qis-into-dg-injective)]; the derived category [[Tag 0FT4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-lemma-qis), [Tag 0FT5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-definition-derived-category)]; morphisms into K-injective modules [[Tag 0FT8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-lemma-hom-derived)].

## Conventions

\(T\), differential graded rings \(A\) of \(T\), right modules, \(C(A)\), \(K(A)\), \(D(A)\), homotopies and \(\operatorname{Hom}^\bullet_A\) are as in the Conventions of the lesson on differential graded modules. A *closed map* is a morphism of \(C(A)\), and \(f\simeq g\) means that \(f\) and \(g\) are homotopic. Recall \(H^0\operatorname{Hom}^\bullet_A(E,F)=\operatorname{Hom}_{K(A)}(E,F)\). Write \(L\colon C(A)\to D(A)\) for the localization functor; it identifies homotopic maps (that lesson). \(A^+\) is the graded subsheaf \(\bigoplus_{i>0}A^i\).

For \(\star\) one of \(\leq q\), \(\geq p\), \([p,q]\), \(-\), \(+\), \(b\), the category \(C^\star(A)\) is as in that lesson. \(W_\star\) is the class of quasi-isomorphisms between objects of \(C^\star(A)\), and \(D^\star(A)=C^\star(A)[W_\star^{-1}]\), with localization functor \(L_\star\). The *comparison functor* \(J_\star\colon D^\star(A)\to D(A)\) is the functor with \(J_\star L_\star=L|_{C^\star(A)}\). An inclusion such as \(C^{\leq q}(A)\subseteq C^-(A)\) induces a functor \(D^{\leq q}(A)\to D^-(A)\), and \(J_{\leq q}\) is its composite with \(J_-\): both functors are induced by the inclusion into \(C(A)\). The *bounds* of a module are the integers outside which its terms vanish.

Shifts and cones: \(M[r]^i=M^{i+r}\), \(d_{M[r]}=(-1)^rd_M\), with the same right action. This satisfies the Leibniz rule, because \((-1)^{|m|-r}=(-1)^{|m|+r}\). The functor \(M\mapsto M[r]\), \(f\mapsto f\), is an automorphism of \(C(A)\) with inverse \([-r]\). It preserves quasi-isomorphisms and the classes \(C^-\), \(C^+\), \(C^b\). Hence it induces automorphisms of \(D(A)\), \(D^-(A)\), \(D^+(A)\), \(D^b(A)\) that commute with the comparison functors. For a closed map \(f\colon X\to Y\),
\[
\begin{gathered}
\operatorname{Cone}(f)^i=Y^i\oplus X^{i+1},\\
d(y,x)=(dy+f(x),-dx),
\end{gathered}
\]
with the componentwise action, which satisfies the Leibniz rule. In the exact sequence \(0\to Y\to\operatorname{Cone}(f)\to X[1]\to0\) the connecting map \(H^{i+1}(X)\to H^{i+1}(Y)\) is \(H^{i+1}(f)\): a cycle \(x\) of \(X[1]^i\) lifts to \((0,x)\), whose differential is \((f(x),0)\). So \(f\) is a quasi-isomorphism exactly when \(\operatorname{Cone}(f)\) is acyclic. A surjective closed map with acyclic kernel, and an injective closed map with acyclic cokernel, are quasi-isomorphisms. For a field \(k\), \(k[n]\) denotes \(k\) placed in degree \(-n\).

## 1. Localizations with bounds on the terms

**Lemma 1.1 (morphisms of a localization).** Let \(\mathcal C\) be a category, \(W\) a class of morphisms and \(\lambda\colon\mathcal C\to\mathcal C[W^{-1}]\) the localization.

1. Every morphism of \(\mathcal C[W^{-1}]\) is a finite composite of morphisms \(\lambda(f)\) and \(\lambda(s)^{-1}\) with \(s\in W\).
2. Let \(\sim\) be an equivalence relation on the sets of morphisms of \(\mathcal C\), compatible with composition, such that \(f\sim g\) implies \(\lambda(f)=\lambda(g)\). Let \(P\) be an object such that composition with every \(s\colon Y\to Y'\) in \(W\) is a bijection \(\operatorname{Hom}(P,Y)/{\sim}\to\operatorname{Hom}(P,Y')/{\sim}\). Then \([f]\mapsto\lambda(f)\) is a bijection \(\operatorname{Hom}(P,Y)/{\sim}\to\operatorname{Hom}(\lambda P,\lambda Y)\) for every \(Y\). The dual statement holds for an object \(N\) such that composition with every \(s\in W\) is a bijection \(\operatorname{Hom}(Y',N)/{\sim}\to\operatorname{Hom}(Y,N)/{\sim}\).

**Proof.** (1) Let \(\mathcal C'\) be the subcategory of \(\mathcal C[W^{-1}]\) with all objects whose morphisms are these finite composites. The functor \(\lambda\) factors through \(\mathcal C'\) and inverts \(W\) there, so there is a functor \(G\colon\mathcal C[W^{-1}]\to\mathcal C'\) with \(G\lambda=\lambda\). If \(\iota\) is the inclusion, then \(\iota G\lambda=\lambda\). A functor out of \(\mathcal C[W^{-1}]\) is determined by its composite with \(\lambda\), so \(\iota G\) is the identity, and every morphism lies in \(\mathcal C'\).

(2) The functor \(F=\operatorname{Hom}(P,-)/{\sim}\) inverts \(W\), hence \(F=\bar F\lambda\) for a functor \(\bar F\) on the localization. For \(f\colon P\to Y\), \(\bar F(\lambda f)([1_P])=[f]\). So \(\lambda(f)=\lambda(g)\) implies \([f]=[g]\), which is injectivity. For surjectivity, write a morphism \(\alpha\colon\lambda P\to\lambda Y\) as a composite \(\gamma_m\cdots\gamma_1\) as in (1), and argue by induction on \(m\). Suppose \(\gamma_{m-1}\cdots\gamma_1=\lambda(g)\) with \(g\colon P\to X\). If \(\gamma_m=\lambda(f)\), then \(\alpha=\lambda(fg)\). If \(\gamma_m=\lambda(s)^{-1}\) with \(s\colon Y\to X\) in \(W\), choose \(g'\colon P\to Y\) with \(sg'\sim g\). Then \(\lambda(s)\lambda(g')=\lambda(g)\) and \(\alpha=\lambda(g')\). The dual statement is (2) for \(\mathcal C^{\mathrm{op}}\), whose localization at \(W\) is \(\mathcal C[W^{-1}]^{\mathrm{op}}\). \(\square\)

**Lemma 1.2 (homotopic maps).** Let \(\star\) be \(\leq q\), \(\geq p\), \(-\), \(+\) or \(b\), and let \(f,g\colon X\to Y\) be homotopic closed maps in \(C^\star(A)\). Then \(L_\star(f)=L_\star(g)\).

**Proof.** Let \(h\) be a homotopy, so \(f-g=dh+hd\).

Suppose first that \(\star\) is \(\leq q\), \(-\) or \(b\). Take the cylinder \(\operatorname{Cyl}(X)^i=X^i\oplus X^{i+1}\oplus X^i\), with
\[
d(a,b,c)=(da+b,\,-db,\,dc-b)
\]
and the componentwise action. Then \(d^2=0\), and the Leibniz rule holds with the sign \((-1)^i\) on all three components. Its terms vanish wherever those of \(X\) and \(X[1]\) vanish, so \(\operatorname{Cyl}(X)\) lies in \(C^\star(A)\). The closed maps
\[
\begin{gathered}
i_0(x)=(x,0,0),\quad i_1(x)=(0,0,x),\\
r(a,b,c)=a+c
\end{gathered}
\]
satisfy \(ri_0=ri_1=1_X\). The map \(r\) is surjective. Its kernel consists of the elements \((a,b,-a)\) and is isomorphic to \(\operatorname{Cone}(1_X)\), which is acyclic: if \(da+b=0\) and \(db=0\), then \((a,b)=d(0,a)\). So \(r\) is a quasi-isomorphism. The map \(H(a,b,c)=f(a)+h(b)+g(c)\) is \(A\)-linear of degree \(0\). Comparing \(H(d(a,b,c))\) with \(d(H(a,b,c))\) gives the condition \((f-g)(b)=dh(b)+hd(b)\), so \(H\) is closed. Since \(L_\star(r)\) is invertible, \(L_\star(i_0)=L_\star(i_1)\), and then \(L_\star(f)=L_\star(Hi_0)=L_\star(Hi_1)=L_\star(g)\).

Suppose next that \(\star\) is \(\geq p\), \(+\) or \(b\). Take the path module \(\operatorname{Path}(Y)^i=Y^i\oplus Y^{i-1}\oplus Y^i\), with
\[
d(a,b,c)=(da,\,-db-c,\,dc).
\]
Then \(d^2=0\) and the Leibniz rule holds. The term \(Y^{i-1}\) vanishes for \(i\leq p\) when \(Y\in C^{\geq p}(A)\), so \(\operatorname{Path}(Y)\) lies in \(C^\star(A)\). The closed maps
\[
\begin{gathered}
j(y)=(y,0,0),\quad p_0(a,b,c)=a,\\
p_1(a,b,c)=a+c
\end{gathered}
\]
satisfy \(p_0j=p_1j=1_Y\). The map \(j\) is injective with cokernel \(\{(0,b,c)\}\), which is acyclic: a cycle has \(c=-db\) and equals \(d(0,0,-b)\) modulo the image of \(j\). So \(j\) is a quasi-isomorphism and \(L_\star(p_0)=L_\star(p_1)\). The map
\[
H(x)=(g(x),\,-h(x),\,f(x)-g(x))
\]
is closed, by the identity \(f-g=dh+hd\), and \(p_0H=g\), \(p_1H=f\). Hence \(L_\star(f)=L_\star(g)\). \(\square\)

**Lemma 1.3 (homotopy squares).**

1. Let \(f\colon X\to Z\) be a closed map and \(s\colon Y\to Z\) a quasi-isomorphism. Put \(R^i=Z^{i-1}\oplus X^i\oplus Y^i\), with
\[
\begin{aligned}
&d(z,x,y)\\
&\quad=(-dz-f(x)+s(y),\,dx,\,dy).
\end{aligned}
\]
The projections \(u\colon R\to X\) and \(v\colon R\to Y\) are closed, \(u\) is a quasi-isomorphism, and \(fu\simeq sv\). If \(X,Y,Z\) lie in \(C^\star(A)\) for \(\star\) one of \(\geq p\), \(-\), \(+\), \(b\), then so does \(R\).
2. Let \(f\colon Z\to X\) be a closed map and \(s\colon Z\to Y\) a quasi-isomorphism. Put \(R'^i=X^i\oplus Y^i\oplus Z^{i+1}\), with
\[
\begin{aligned}
&d(x,y,z)\\
&\quad=(dx+f(z),\,dy-s(z),\,-dz).
\end{aligned}
\]
The inclusions \(u'\colon X\to R'\) and \(v'\colon Y\to R'\) are closed, \(u'\) is a quasi-isomorphism, and \(u'f\simeq v's\). If \(X,Y,Z\) lie in \(C^\star(A)\) for \(\star\) one of \(\leq q\), \(-\), \(+\), \(b\), then so does \(R'\).

**Proof.** (1) \(R\) is \(\operatorname{Cone}\bigl((f,-s)\colon X\oplus Y\to Z\bigr)[-1]\), so it is a module. The map \(k(z,x,y)=-z\) has degree \(-1\), and \(dk+kd\) sends \((z,x,y)\) to \(f(x)-s(y)\). The map \(u\) is surjective, and its kernel consists of the elements \((z,0,y)\), with differential \((-dz+s(y),dy)\). That kernel is an extension of \(Y\) by \(Z[-1]\) whose connecting map is \(H(s)\): a cycle \(y\) lifts to \((0,y)\), with differential \((s(y),0)\). Since \(H(s)\) is an isomorphism, the kernel is acyclic. If \(Z^{p-1}=0\), then \(R^i=0\) for \(i<p\). The upper bound of \(R\) is at most one more than the bounds of \(X,Y,Z\).

(2) \(R'\) is \(\operatorname{Cone}\bigl((f,-s)\colon Z\to X\oplus Y\bigr)\). The map \(k(z)=(0,0,z)\) satisfies \(dk+kd=u'f-v's\). The map \(u'\) is injective, and its cokernel is \(\operatorname{Cone}(-s)\), which is acyclic. The term \(Z^{i+1}\) vanishes for \(i\geq q\) when \(Z\in C^{\leq q}(A)\). \(\square\)

**Corollary 1.4 (roofs).** Let \(M,N\in C^\star(A)\).

1. If \(\star\) is \(\geq p\), \(-\), \(+\) or \(b\), every morphism \(\alpha\colon M\to N\) of \(D^\star(A)\) equals \(L_\star(g)L_\star(t)^{-1}\) for a quasi-isomorphism \(t\colon R\to M\) and a closed map \(g\colon R\to N\) in \(C^\star(A)\). Two such morphisms \(\alpha_1,\alpha_2\) can be written with the same \(t\).
2. If \(\star\) is \(\leq q\), \(-\), \(+\) or \(b\), every morphism \(\alpha\colon M\to N\) of \(D^\star(A)\) equals \(L_\star(t)^{-1}L_\star(g)\) for a quasi-isomorphism \(t\colon N\to R\) and a closed map \(g\colon M\to R\) in \(C^\star(A)\). Two such morphisms can be written with the same \(t\).

**Proof.** (1) Write \(L\) for \(L_\star\). The morphisms of the form \(L(g)L(t)^{-1}\) include every \(L(f)\) and every \(L(s)^{-1}\), so by Lemma 1.1 (1) it suffices to show that they are closed under composition. Take \(g_1\colon R_1\to Y\) and a quasi-isomorphism \(t_2\colon R_2\to Y\). Lemma 1.3 (1) gives \(u\colon R\to R_1\), a quasi-isomorphism, and \(v\colon R\to R_2\) with \(g_1u\simeq t_2v\). Lemma 1.2 gives \(L(g_1)L(u)=L(t_2)L(v)\), that is, \(L(t_2)^{-1}L(g_1)=L(v)L(u)^{-1}\). Hence
\[
\begin{aligned}
&L(g_2)L(t_2)^{-1}L(g_1)L(t_1)^{-1}\\
&\quad=L(g_2v)L(t_1u)^{-1}.
\end{aligned}
\]
Next, let \(\alpha_j=L(g_j)L(t_j)^{-1}\) with \(t_j\colon R_j\to M\). Lemma 1.3 (1), applied to \(t_1\) and \(t_2\), gives \(u\colon R\to R_1\) and \(v\colon R\to R_2\) with \(t_1u\simeq t_2v\). The map \(v\) is a quasi-isomorphism, since \(t_2v\) is homotopic to the quasi-isomorphism \(t_1u\). Put \(t=t_1u\), so that \(L(t)=L(t_2v)\). From \(L(t_1)^{-1}=L(u)L(t)^{-1}\) we get \(\alpha_1=L(g_1u)L(t)^{-1}\), and in the same way \(\alpha_2=L(g_2v)L(t)^{-1}\). (2) is dual, with Lemma 1.3 (2). \(\square\)

**Lemma 1.5 (the derived category).** Let \(X,Y\in C(A)\).

1. Every morphism \(\beta\colon X\to Y\) of \(D(A)\) equals \(L(s)^{-1}L(f)\) for a quasi-isomorphism \(s\colon Y\to Y'\) and a closed map \(f\colon X\to Y'\).
2. If \(f,g\colon X\to Y\) are closed maps with \(L(f)=L(g)\), there are quasi-isomorphisms \(t\colon Y\to Y'\) and \(t'\colon X'\to X\) with \(tf\simeq tg\) and \(ft'\simeq gt'\).

**Proof.** Choose a quasi-isomorphism \(s\colon Y\to I\) into a K-injective module [Stacks, Tag 0FT0]. The localization map \(\operatorname{Hom}_{K(A)}(X,I)\to\operatorname{Hom}_{D(A)}(X,I)\) is bijective [Stacks, Tag 0FT8], and \(D(A)\) is also the localization of \(C(A)\).

(1) \(L(s)\beta=L(f)\) for some closed \(f\colon X\to I\).

(2) Since \(L(sf)=L(sg)\), we get \(sf\simeq sg\); take \(t=s\). Put \(h=f-g\) and choose \(k\) of degree \(-1\) with \(sh=dk+kd\). Let \(E=\operatorname{Cone}(s)[-1]\), with \(E^i=I^{i-1}\oplus Y^i\) and \(d(a,y)=(-da-s(y),dy)\). It is acyclic. The map \(e\colon X\to E\), \(e(x)=(-k(x),h(x))\), is closed, by the identity \(sh=dk+kd\). The projection \(\mathrm{pr}(a,y)=y\) is a closed map \(E\to Y\), and \(\mathrm{pr}\circ e=h\). Let \(X'=\operatorname{Cone}(e)[-1]\), with \(X'^i=E^{i-1}\oplus X^i\) and \(d(c,x)=(-dc-e(x),dx)\), and let \(t'(c,x)=x\). The map \(t'\) is surjective with kernel \(E[-1]\), which is acyclic, so it is a quasi-isomorphism. The map \(H(c,x)=-c\) satisfies \(dH+Hd=et'\). So \(ht'=\mathrm{pr}\,et'\simeq0\), that is, \(ft'\simeq gt'\). \(\square\)

**Lemma 1.6 (unions).** Let \(M,N\in C^-(A)\). Every morphism \(M\to N\) of \(D^-(A)\), and every pair of such morphisms, is the image of morphisms of \(D^{\leq q}(A)\) for one \(q\) with \(M,N\in C^{\leq q}(A)\). If \(J_{\leq q}\) is fully faithful for every \(q\), then \(J_-\) is fully faithful. The same holds with \(+\) and \(\geq p\).

**Proof.** By Lemma 1.1 (1) a morphism is a composite of morphisms \(L_-(f_j)\) and \(L_-(s_j)^{-1}\) through finitely many objects of \(C^-(A)\). Choose \(q\) at least their upper bounds. The corresponding composite in \(D^{\leq q}(A)\) maps to it. For a pair of morphisms, take the larger of the two values of \(q\).

Suppose every \(J_{\leq q}\) is fully faithful. Fullness: a morphism \(\beta\) of \(D(A)\) between \(M,N\in C^{\leq q}(A)\) is \(J_{\leq q}(\alpha')\), which is \(J_-\) of the image of \(\alpha'\). Faithfulness: if \(J_-\alpha_1=J_-\alpha_2\), write \(\alpha_j\) as the image of \(\alpha'_j\) for a common \(q\). Then \(J_{\leq q}\alpha'_1=J_{\leq q}\alpha'_2\), so \(\alpha'_1=\alpha'_2\) and \(\alpha_1=\alpha_2\). \(\square\)

**Lemma 1.7 (semifree modules).** Let \(A\) be a differential graded ring of the punctual topos. Let \(P\) be a module that is free as a graded module on a homogeneous basis \((e_j)_{j\in S}\), and \(\ell\colon S\to\mathbb N\) a function such that every \(de_j\) lies in the submodule generated by the \(e_{j'}\) with \(\ell(j')<\ell(j)\).

1. \(\operatorname{Hom}^\bullet_A(P,E)\) is acyclic for every acyclic module \(E\).
2. Composition with a quasi-isomorphism \(s\colon Y\to Y'\) is a bijection from \(\operatorname{Hom}_{K(A)}(P,Y)\) to \(\operatorname{Hom}_{K(A)}(P,Y')\).
3. \([f]\mapsto L(f)\) is a bijection \(\operatorname{Hom}_{K(A)}(P,Y)\to\operatorname{Hom}_{D(A)}(P,Y)\) for every \(Y\).

**Proof.** (1) Let \(f\) be a cocycle of degree \(m\), so \(df=(-1)^mfd\). Let \(P_{<n}\) be the submodule generated by the \(e_j\) with \(\ell(j)<n\); it is stable under \(d\). Suppose \(g\) of degree \(m-1\) is defined on \(P_{<n}\), is \(A\)-linear, and satisfies
\[
dg+(-1)^mgd=f\quad\text{on }P_{<n}.
\]
For \(\ell(j)=n\) put \(z=f(e_j)-(-1)^mg(de_j)\). On \(de_j\in P_{<n}\) the identity gives \(dg(de_j)=f(de_j)\). So \(dz=(-1)^mf(de_j)-(-1)^mf(de_j)=0\). Choose \(g(e_j)\) with \(dg(e_j)=z\), and extend \(g\) \(A\)-linearly. The identity then holds on \(e_j\), and both of its sides are \(A\)-linear, so it holds on \(P_{<n+1}\). Since \(P\) is the union of the \(P_{<n}\), \(f=dg-(-1)^{m-1}gd\) is a coboundary.

(2) \(\operatorname{Hom}^\bullet_A(P,-)\) carries \(\operatorname{Cone}(s)\) to the cone of \(\operatorname{Hom}^\bullet_A(P,s)\). Indeed, a map of degree \(m\) into \(Y'\oplus Y[1]\) is a pair \((\varphi,\psi)\) of maps into \(Y'\) and \(Y\), of degrees \(m\) and \(m+1\), and its differential is \((d\varphi+s\psi,-d\psi)\). By (1) this cone is acyclic, and the statement follows on \(H^0\).

(3) is Lemma 1.1 (2), with \(\sim\) the homotopy relation and with (2). \(\square\)

## 2. Rings with a split degree-zero part

**2.0. The splitting hypothesis.** Say that \(A\) satisfies (SP) if \(A^i=0\) for \(i<0\), \(d(A^0)=0\), and every short exact sequence of sheaves of right \(A^0\)-modules splits. Then \(A^0\) is a subring, and for every module \(M\) the sheaves \(Z^iM\) and \(B^iM\) are \(A^0\)-submodules of \(M^i\). Indeed, for \(a\in A^0\), \(d(za)=(dz)a\) and \((dm)a=d(ma)\). In the punctual topos the last condition says that \(A^0\) is a semisimple ring. A *connected* differential graded algebra over a field \(k\) is one with \(k\)-linear differential, \(A^0=k\) and \(A^{<0}=0\); it satisfies (SP), because \(d(\lambda)=\lambda d(1)=0\).

**Lemma 2.1 (cuts).** Assume (SP). Let \(P\in C(A)\) and \(n\in\mathbb Z\).

1. If \(H^iP=0\) for \(i<n\), let \(L\subseteq P^n\) be an \(A^0\)-complement of \(B^nP\), and \(Q\subseteq P\) the graded subsheaf with
\[
Q^i=\begin{cases}0,&i<n,\\ L,&i=n,\\ P^i,&i>n.\end{cases}
\]
Then \(Q\) is a submodule, it lies in \(C^{\geq n}(A)\), and the inclusion \(Q\to P\) is a quasi-isomorphism.
2. If \(H^iP=0\) for \(i>n\), let \(L\subseteq P^n\) be an \(A^0\)-complement of \(Z^nP\), and \(U\subseteq P\) the graded subsheaf with \(U^i=0\) for \(i<n\), \(U^n=L\) and \(U^i=P^i\) for \(i>n\). Then \(U\) is an acyclic submodule, \(P/U\) lies in \(C^{\leq n}(A)\), and the projection \(\pi\colon P\to P/U\) is a quasi-isomorphism.

**Proof.** In both cases the subsheaf is stable under \(A^0\), because \(L\) is an \(A^0\)-submodule. It is stable under \(A^+\), which raises degrees into the terms kept whole, and under \(d\). The ring has no negative components.

(1) Since \(B^n\subseteq Z^n\) and \(P^n=B^n\oplus L\), we get \(Z^n=B^n\oplus(Z^n\cap L)\). So \(H^nQ=Z^n\cap L\) maps isomorphically onto \(H^nP\). Moreover \(d(L)=d(P^n)\), because \(d(B^n)=0\), so \(H^{n+1}Q=H^{n+1}P\). The other degrees are clear.

(2) The map \(d|_L\colon L\to B^{n+1}P\) is injective, because \(L\cap Z^n=0\), and surjective, because \(d(P^n)=d(L)\). So \(H^nU=0\) and \(H^{n+1}U=Z^{n+1}P/B^{n+1}P=0\). For \(i>n+1\), \(H^iU=H^iP=0\). The long exact sequence of \(0\to U\to P\to P/U\to0\) shows that \(\pi\) is a quasi-isomorphism. \(\square\)

**Theorem 2.2.** Assume (SP), and let \(p\leq q\).

1. \(J_{\leq q}\), \(J_{\geq p}\), \(J_-\), \(J_+\) and \(J_b\) are fully faithful.
2. Their essential images consist of the objects \(X\) of \(D(A)\) with \(H^iX=0\) for \(i>q\); for \(i<p\); for all large \(i\); for all large \(-i\); for all large \(|i|\).
3. Every object \(X\) with \(H^iX=0\) for \(i\notin[p,q]\) is isomorphic in \(D(A)\) to \(L(Y)\) for some \(Y\in C^{[p,q]}(A)\).

**Proof.** (a) *\(J_{\leq q}\).* Let \(M,N\in C^{\leq q}(A)\). *Fullness:* by Lemma 1.5 (1), a morphism \(\beta\colon M\to N\) of \(D(A)\) is \(L(s)^{-1}L(f)\) with \(s\colon N\to Y'\). Since \(H^iY'=H^iN=0\) for \(i>q\), Lemma 2.1 (2) gives a quasi-isomorphism \(\pi\colon Y'\to Y'/U\) into \(C^{\leq q}(A)\). Then
\[
\begin{aligned}
\beta&=L(\pi s)^{-1}L(\pi f)\\
&=J_{\leq q}\bigl(L_{\leq q}(\pi s)^{-1}L_{\leq q}(\pi f)\bigr).
\end{aligned}
\]
*Faithfulness:* let \(J_{\leq q}\alpha_1=J_{\leq q}\alpha_2\). By Corollary 1.4 (2), \(\alpha_j=L_{\leq q}(t)^{-1}L_{\leq q}(g_j)\) with a common \(t\colon N\to R\). Applying \(J_{\leq q}\) gives \(L(g_1)=L(g_2)\). Lemma 1.5 (2) gives a quasi-isomorphism \(t''\colon R\to R'\) with \(t''g_1\simeq t''g_2\). Cut \(R'\) by Lemma 2.1 (2) with \(n=q\). Then \(\pi t''\colon R\to R'/U\) is a quasi-isomorphism in \(C^{\leq q}(A)\), and \(\pi t''g_1\simeq\pi t''g_2\). By Lemma 1.2, \(L_{\leq q}(\pi t'')L_{\leq q}(g_1)=L_{\leq q}(\pi t'')L_{\leq q}(g_2)\). Hence \(L_{\leq q}(g_1)=L_{\leq q}(g_2)\) and \(\alpha_1=\alpha_2\).

(b) *\(J_{\geq p}\).* Let \(M,N\in C^{\geq p}(A)\). *Fullness:* write \(\beta=L(s)^{-1}L(f)\) as in (a). Lemma 1.3 (1) in \(C(A)\) gives \(u\colon R\to M\), a quasi-isomorphism, and \(v\colon R\to N\) with \(fu\simeq sv\), so \(\beta=L(v)L(u)^{-1}\). Since \(H^iR=H^iM=0\) for \(i<p\), Lemma 2.1 (1) gives \(\iota\colon Q\to R\) with \(Q\in C^{\geq p}(A)\). Then \(\beta=J_{\geq p}\bigl(L_{\geq p}(v\iota)L_{\geq p}(u\iota)^{-1}\bigr)\). *Faithfulness:* by Corollary 1.4 (1), \(\alpha_j=L_{\geq p}(g_j)L_{\geq p}(t)^{-1}\) with a common quasi-isomorphism \(t\colon R\to M\). Equality of the images gives \(L(g_1)=L(g_2)\). Lemma 1.5 (2) gives a quasi-isomorphism \(t'\colon R'\to R\) with \(g_1t'\simeq g_2t'\). Cut \(R'\) from below at \(p\), by \(\iota\colon Q\to R'\). Then \(t'\iota\) is a quasi-isomorphism in \(C^{\geq p}(A)\) and \(g_1t'\iota\simeq g_2t'\iota\). So \(L_{\geq p}(g_1)L_{\geq p}(t'\iota)=L_{\geq p}(g_2)L_{\geq p}(t'\iota)\), and \(\alpha_1=\alpha_2\).

(c) *\(J_-\) and \(J_+\)* follow from (a), (b) and Lemma 1.6.

(d) *\(J_b\).* Let \(M,N\in C^b(A)\). *Fullness:* with \(u\), \(v\), \(R\) as in (b), choose \(a\) at most the lower bounds of \(M\) and \(N\), and \(r\) larger than their upper bounds. Cut \(R\) from below at \(a\), giving \(\iota\colon Q\to R\). Since \(H^iQ=H^iM=0\) for \(i\geq r\), Lemma 2.1 (2) with \(n=r\) gives \(U\subseteq Q\) with \(U^i=0\) for \(i<r\). The maps \(u\iota\) and \(v\iota\) vanish on \(U\), because \(M^i=N^i=0\) for \(i\geq r\). So they factor through closed maps \(\bar u,\bar v\) on \(Q/U\in C^{[a,r]}(A)\). The map \(\bar u\) is a quasi-isomorphism, since \(\bar u\pi=u\iota\). And
\[
\begin{aligned}
\beta&=L(v\iota)L(u\iota)^{-1}=L(\bar v)L(\bar u)^{-1}\\
&=J_b\bigl(L_b(\bar v)L_b(\bar u)^{-1}\bigr).
\end{aligned}
\]
*Faithfulness:* by Corollary 1.4 (1), \(\alpha_j=L_b(g_j)L_b(t)^{-1}\) with \(t\colon R\to M\) and \(R\in C^b(A)\). As in (b) there are a quasi-isomorphism \(t'\colon R'\to R\) and a map \(k\) of degree \(-1\) with
\[
g_1t'-g_2t'=dk+kd.
\]
Choose \(a\) at most the lower bound of \(R\), and \(r\) larger than the upper bound of \(R\) and than the upper bound of \(N\) plus one. Cut \(R'\) from below at \(a\), giving \(\iota\colon Q\to R'\), and cut \(Q\) above by \(U\) with \(U^i=0\) for \(i<r\). Then \(t'\iota\) vanishes on \(U\), because \(R^i=0\) for \(i\geq r\). The map \(k\iota\) vanishes on \(U\) as well, because \(N^{i-1}=0\) for \(i\geq r\). So they factor through a closed map \(\bar t\colon Q/U\to R\), a quasi-isomorphism, and an \(A\)-linear map \(\bar k\) of degree \(-1\). Composing with the surjection \(\pi\) shows \(g_1\bar t-g_2\bar t=d\bar k+\bar kd\). Hence \(L_b(g_1)L_b(\bar t)=L_b(g_2)L_b(\bar t)\), and \(\alpha_1=\alpha_2\).

(2) and (3). Objects of \(C^\star(A)\) have the stated vanishing of cohomology. Conversely, if \(H^iX=0\) for \(i>q\), then \(X\to X/U\) is a quasi-isomorphism into \(C^{\leq q}(A)\). If \(H^iX=0\) for \(i<p\), then \(Q\to X\) is one from \(C^{\geq p}(A)\). If both hold, the quasi-isomorphisms \(X\leftarrow Q\to Q/U\), the lower cut at \(p\) followed by the upper cut at \(q\), end in \(C^{[p,q]}(A)\). Unions of bounds are treated by choosing bounds. \(\square\)

Part (3) concerns objects only. Section 4 shows that \(J_{[p,q]}\) can fail to be full under (SP). The following lemmas compute the interval categories when \(A\) has a gap in its positive degrees.

**Lemma 2.3 (complexes over a split ring).** Let \(R\) be a sheaf of rings of \(T\) such that every short exact sequence of sheaves of right \(R\)-modules splits. For complexes \(X\) and \(N\) of right \(R\)-modules, \([f]\mapsto(H^if)_i\) is a bijection
\[
\begin{aligned}
&\operatorname{Hom}_{K(R)}(X,N)\\
&\quad\to\textstyle\prod_i\operatorname{Hom}_R(H^iX,H^iN),
\end{aligned}
\]
natural in \(X\) and \(N\). In particular, composition with a quasi-isomorphism \(X\to X'\) induces a bijection \(\operatorname{Hom}_{K(R)}(X',N)\to\operatorname{Hom}_{K(R)}(X,N)\).

**Proof.** Write \(N^i=Z^i\oplus C^i\) and \(Z^i=B^i\oplus N_0^i\). Then \(d\) maps \(C^i\) isomorphically onto \(B^{i+1}\), and \(N\) is the direct sum, as complexes, of \(N_0\) with zero differential and of the complexes \(C^i\to B^{i+1}\). Each of the latter is contractible, by the inverse of \(d\). So the inclusion \(e\colon N_0\to N\) and the projection \(p\colon N\to N_0\) satisfy \(pe=1\) and \(ep\simeq1\), and \(N_0^i\cong H^iN\) through \(H^i(p)\). It therefore suffices to treat \(N=N_0\).

A closed map \(f\colon X\to N_0\) vanishes on \(B^iX\), because \(f^id=d f^{i-1}=0\). Its restriction to \(Z^iX\) is \(H^if\). Homotopies have the form \(hd\), so homotopic maps agree on cycles. *Surjectivity:* given maps \(H^iX\to N_0^i\), compose with \(Z^iX\to H^iX\) and extend to \(X^i=Z^iX\oplus C^iX\) by zero on \(C^iX\); the result is closed. *Injectivity:* if \(f\) vanishes on every \(Z^iX\), then \(f^i\) factors as \(\psi\circ d\) with \(\psi\colon B^{i+1}X\to N_0^i\), through the isomorphism \(X^i/Z^iX\cong B^{i+1}X\). Extending \(\psi\) to \(h^{i+1}\colon X^{i+1}\to N_0^i\) along a splitting of \(B^{i+1}X\subseteq X^{i+1}\) gives \(f=hd=dh+hd\). \(\square\)

**Lemma 2.4 (narrow intervals).** Let \(p\leq q\), \(w=q-p\), and suppose \(A^i=0\) for \(i<0\) and for \(1\leq i\leq w\). Put \(R=A^0\).

1. \(A^+\) acts by zero on every object of \(C^{[p,q]}(A)\). Through the map of differential graded rings \(A\to A/A^+=R\), \(C^{[p,q]}(A)\) is the category of complexes of right \(R\)-modules with terms in \([p,q]\), with the same homotopies and quasi-isomorphisms.
2. Homotopic closed maps of \(C^{[p,q]}(A)\) have equal images in \(D^{[p,q]}(A)\).
3. If every short exact sequence of sheaves of right \(R\)-modules splits, then every morphism \(M\to N\) of \(D^{[p,q]}(A)\) is \(L_{[p,q]}(f)\) for a closed map \(f\), and \(L_{[p,q]}(f)\mapsto(H^if)_i\) is a well defined bijection
\[
\begin{aligned}
&\operatorname{Hom}_{D^{[p,q]}(A)}(M,N)\\
&\quad\to\textstyle\prod_{i=p}^q\operatorname{Hom}_R(H^iM,H^iN).
\end{aligned}
\]

**Proof.** (1) For \(a\in A^j\) with \(j\geq w+1\) and \(m\in M^i\) with \(i\geq p\), the element \(ma\) has degree at least \(q+1\), so \(ma=0\). Since \(A^{<0}=0\), \(A^+\) is a two-sided ideal stable under \(d\), and \(A/A^+\) is \(A^0\) in degree \(0\). For \(a\in A^0\), \(d(ma)=(dm)a\), because \(m\,da=0\) with \(da\in A^+\). Conversely, a complex of \(R\)-modules in \([p,q]\) is an \(A\)-module through \(A\to R\): the term \(m\,da\) of the Leibniz rule vanishes there. Linear maps and homotopies are the same for \(A\) and for \(R\).

(2) Let \(f-g=dh+hd\) with \(f,g\colon X\to Y\), regarded as complexes of \(R\)-modules. The cylinder \(\operatorname{Cyl}(X)\) of Lemma 1.2 is a complex of \(R\)-modules in \([p-1,q]\). By Lemma 1.1 of the lesson on differential graded modules, applied to the ring \(R\) concentrated in degree \(0\), \(\tau^{\geq p}\) is a quotient functor that preserves quasi-isomorphisms and is the identity on complexes in degrees \(\geq p\). Let \(\rho\colon\operatorname{Cyl}(X)\to\tau^{\geq p}\operatorname{Cyl}(X)\) be the quotient map, and put \(r'=\tau^{\geq p}(r)\) and \(H'=\tau^{\geq p}(H)\). By naturality, \(r'\rho=r\) and \(H'\rho=H\). Hence \(r'\rho i_0=r'\rho i_1=1_X\), with \(r'\) a quasi-isomorphism in \(C^{[p,q]}(A)\), while \(f=H'\rho i_0\) and \(g=H'\rho i_1\). So \(L_{[p,q]}(f)=L_{[p,q]}(g)\).

(3) By (1), (2) and Lemma 2.3, the object \(N\) satisfies the dual hypothesis of Lemma 1.1 (2) in \(C^{[p,q]}(A)\), with \(\sim\) the homotopy relation. Hence \(\operatorname{Hom}_{K(R)}(M,N)\to\operatorname{Hom}_{D^{[p,q]}(A)}(M,N)\) is bijective, and Lemma 2.3 identifies its source. \(\square\)

**Theorem 2.5 (a gap in positive degrees).** Assume (SP), let \(p\leq q\) and \(w=q-p\), and suppose \(A^i=0\) for \(1\leq i\leq w+1\). Then \(J_{[p,q]}\) is fully faithful, and its Hom sets are those of Lemma 2.4 (3).

**Proof.** Let \(X\in C^{\geq p}(A)\) and \(N\in C^{[p,q]}(A)\). Every nonzero component \(A^j\) of \(A^+\) has \(j\geq w+2\). For an \(A^0\)-linear graded map \(f\colon X\to N\) of degree \(0\) or \(-1\), \(x\in X\) and \(a\in A^j\), the element \(f(xa)\) lies in degree at least \(p+w+1=q+1\), so it vanishes; and \(f(x)a=0\) by Lemma 2.4 (1). So such maps are \(A\)-linear, and
\[
\operatorname{Hom}_{K(A)}(X,N)=\operatorname{Hom}_{K(R)}(X,N),
\]
where \(X\) is a complex of \(R\)-modules because \(d(A^0)=0\). By Lemma 2.3 this functor of \(X\) carries quasi-isomorphisms to bijections. Lemma 1.1 (2), with Lemma 1.2, shows that \(\lambda_{\geq p}\colon[f]\mapsto L_{\geq p}(f)\) is a bijection \(\operatorname{Hom}_{K(A)}(M,N)\to\operatorname{Hom}_{D^{\geq p}(A)}(M,N)\). Lemma 2.4 (3) gives the bijection \(\lambda_{[p,q]}\colon[f]\mapsto L_{[p,q]}(f)\). Let \(\lambda\colon[f]\mapsto L(f)\). Then
\[
J_{[p,q]}\lambda_{[p,q]}=\lambda=J_{\geq p}\lambda_{\geq p}.
\]
Here \(J_{\geq p}\) is bijective on Hom sets by Theorem 2.2. So \(\lambda\) is bijective, and \(J_{[p,q]}=\lambda\lambda_{[p,q]}^{-1}\) is bijective on \(\operatorname{Hom}(M,N)\). \(\square\)

When \(A^{>0}=0\), all six comparison functors are fully faithful (Proposition 1.2 of the lesson on differential graded modules). Theorems 2.2 and 2.5 are the analogues for rings with positive components. Proposition 4.1 shows that the number \(w+1\) in Theorem 2.5 cannot be lowered to \(w\).

## 3. Words and the variable bounds

**3.0. Setting.** In this section \(k\) is a field and, in the punctual topos,
\[
\begin{gathered}
A=k1\oplus kx\oplus ky,\quad |x|=2,\ |y|=0,\\
x^2=xy=yx=y^2=0,\quad d=0.
\end{gathered}
\]
This is a commutative differential graded \(k\)-algebra concentrated in degrees \(0\) and \(2\), with \(H(A)=A\) three-dimensional. Its degree-zero ring is \(k[y]/(y^2)\), over which \(A\) is connected; this ring is not semisimple, since \(0\to ky\to A^0\to k\to0\) does not split. The module \(k\) is \(A/(kx\oplus ky)\) in degree \(0\), on which \(x\) and \(y\) act by zero.

Let \(\mathcal W\) be the set of finite words in the letters \(x,y\), including the empty word \(\varnothing\). The *height* \(h(w)\) is the number of letters \(x\) minus the number of letters \(y\), and \(\mathcal W_t=\{w:h(w)=t\}\). Let \(P\) be the free graded right \(A\)-module on generators \(e_w\) of degree \(h(w)\), with
\[
de_\varnothing=0,\quad de_{wa}=e_w\,a\quad(a\in\{x,y\}),
\]
extended by \(d(e_wb)=(de_w)b\). The degree of \(e_wa\) is \(h(w)+|a|=h(wa)+1\). Let \(\varepsilon_P\colon P\to k\) send \(e_\varnothing\) to \(1\) and every other \(e_w\) to \(0\).

**Lemma 3.1 (the resolution by words).**

1. \(P\) is a module and \(\varepsilon_P\) is a closed quasi-isomorphism.
2. For every \(n\), there is a bijection \(\Theta_n\colon\operatorname{Hom}_{D(A)}(k,k[n])\to\prod_{w\in\mathcal W_{-n}}k\) defined as follows. \(\Theta_n(\beta)=(f(e_w))_w\), where \(f\colon P\to k[n]\) is the unique closed map with \(L(f)=\beta L(\varepsilon_P)\).

**Proof.** (1) We have \(d^2e_{wa}=(de_w)a\). This is \(0\) for \(w=\varnothing\), and \(e_{w'}a'a=0\) for \(w=w'a'\). As a complex of vector spaces, \(P\) has the basis \(e_w\), \(e_wx\), \(e_wy\). It is the direct sum of \(ke_\varnothing\) and the pairs \(ke_{wa}\to ke_wa\), on which \(d\) is the identity, so \(\varepsilon_P\) is a quasi-isomorphism.

(2) \(P\) satisfies Lemma 1.7, with \(\ell(w)\) the length of \(w\). The map \(L(\varepsilon_P)\) is invertible, and Lemma 1.7 (3) identifies \(\operatorname{Hom}_{D(A)}(P,k[n])\) with \(\operatorname{Hom}_{K(A)}(P,k[n])\). An \(A\)-linear map \(f\colon P\to k[n]\) of degree \(0\) or \(-1\) satisfies \(f(de_{wa})=f(e_w)a=0\), since \(a\) acts by zero on \(k[n]\). So the differential of \(\operatorname{Hom}^\bullet_A(P,k[n])\) vanishes. Hence \(\operatorname{Hom}_{K(A)}(P,k[n])\) is the set of all degree-zero \(A\)-linear maps. Such a map is an arbitrary family of values \(f(e_w)\in k[n]^{h(w)}\), which is nonzero only for \(h(w)=-n\). \(\square\)

**3.2. Admissible words.** Let \(I\) be an interval of \(\mathbb Z\) containing \(0\). A word is *\(I\)-admissible* if the heights of all its prefixes, \(\varnothing\) and the word itself included, lie in \(I\). Let \(\mathcal W(I)\) be the set of \(I\)-admissible words. An extension of a word outside \(\mathcal W(I)\) lies outside \(\mathcal W(I)\). Let \(\mathcal V_n(I)\) be the set of families \(c\in\prod_{w\in\mathcal W_{-n}}k\) with \(c_w=0\) for \(w\notin\mathcal W(I)\). Let \(\mathcal I_-\), \(\mathcal I_+\), \(\mathcal I_b\) be the sets of intervals \((-\infty,U]\) with \(U\geq0\), \([L,\infty)\) with \(L\leq0\), and \([L,U]\) with \(L\leq0\leq U\).

**Lemma 3.2 (restricted resolutions).** Let \(I\in\mathcal I_-\cup\mathcal I_+\cup\mathcal I_b\). Let \(Q_I\subseteq P\) be the span of the \(e_u\) and the \(de_u\) for \(u\notin\mathcal W(I)\), put \(R_I=P/Q_I\), and let \(q_I\colon P\to R_I\) be the projection.

1. \(Q_I\) is an acyclic submodule, \(q_I\) is a quasi-isomorphism, and \(\varepsilon_P\) factors as \(s_Iq_I\) for a quasi-isomorphism \(s_I\colon R_I\to k\).
2. \(R_I\) has the basis \(e_w\) for \(w\in\mathcal W(I)\) and \(e_wa\) for \(wa\in\mathcal W(I)\). It lies in \(C^-(A)\), \(C^+(A)\), \(C^b(A)\) when \(I\) is in \(\mathcal I_-\), \(\mathcal I_+\), \(\mathcal I_b\) respectively.
3. For \(c\in\mathcal V_n(I)\), the \(A\)-linear map \(P\to k[n]\) with \(e_w\mapsto c_w\) vanishes on \(Q_I\). It therefore induces a closed map \(f_{I,c}\colon R_I\to k[n]\), and \(\Theta_n\bigl(L(f_{I,c})L(s_I)^{-1}\bigr)=c\).
4. If \(I\subseteq I'\), the identity of \(P\) induces a quasi-isomorphism \(r\colon R_{I'}\to R_I\) with \(s_Ir=s_{I'}\) and \(f_{I,c}r=f_{I',c}\) for \(c\in\mathcal V_n(I)\).

**Proof.** (1) For \(u\notin\mathcal W(I)\), \(e_ux=de_{ux}\) and \(e_uy=de_{uy}\) lie in \(Q_I\), and \(de_u\cdot x=de_u\cdot y=0\). So \(Q_I\) is a submodule, and it is stable under \(d\). It is the span of the pairs \((e_u,de_u)\) with \(u\notin\mathcal W(I)\), hence acyclic, and \(q_I\) is a quasi-isomorphism. The map \(\varepsilon_P\) vanishes on \(Q_I\), since \(\varnothing\in\mathcal W(I)\), and \(s_I\) is a quasi-isomorphism by two out of three.

(2) The vectors \(de_u=e_{u'}a'\) with \(u=u'a'\notin\mathcal W(I)\) are the \(e_wa\) with \(wa\notin\mathcal W(I)\). The basis vectors of \(R_I\) have degrees \(h(w)\in I\) and \(h(wa)+1\) with \(h(wa)\in I\). So the terms of \(R_I\) lie in \(I\cup(I+1)\), which is bounded above, bounded below, or bounded as \(I\) is.

(3) The map vanishes on \(e_u\) for \(u\notin\mathcal W(I)\), and on \(de_u=e_{u'}a'\) because \(a'\) acts by zero on \(k[n]\). It is closed by the proof of Lemma 3.1. We have \(L(f_{I,c})L(s_I)^{-1}L(\varepsilon_P)=L(f_{I,c}q_I)\), and \(f_{I,c}q_I(e_w)=c_w\).

(4) \(Q_{I'}\subseteq Q_I\), because \(\mathcal W(I)\subseteq\mathcal W(I')\). The rest follows from \(rq_{I'}=q_I\). \(\square\)

**Theorem 3.3 (morphisms of the augmentation module).** Let \(\sharp\) be \(-\), \(+\) or \(b\), and \(n\in\mathbb Z\). Then \(J_\sharp\) is injective on \(\operatorname{Hom}_{D^\sharp(A)}(k,k[n])\), and
\[
\begin{aligned}
&\Theta_nJ_\sharp\bigl(\operatorname{Hom}_{D^\sharp(A)}(k,k[n])\bigr)\\
&\quad=\textstyle\bigcup_{I\in\mathcal I_\sharp}\mathcal V_n(I).
\end{aligned}
\]

**Proof.** *Normal form.* Let \(\alpha\colon k\to k[n]\) be a morphism of \(D^\sharp(A)\). By Corollary 1.4 (1), \(\alpha=L_\sharp(g)L_\sharp(s)^{-1}\) for a quasi-isomorphism \(s\colon Z\to k\) and a closed map \(g\colon Z\to k[n]\), with \(Z\in C^\sharp(A)\). Choose \(I\in\mathcal I_\sharp\) with \(Z^i=0\) for \(i\notin I\). Choose a cycle \(z_\varnothing\in Z^0\) with \(s(z_\varnothing)=1\), which exists because \(H^0(s)\) is surjective. Then \(s\) is surjective, since \(s(z_\varnothing\lambda)=\lambda\), and \(K=\ker s\) is acyclic.

By induction on length we choose \(z_w\in Z^{h(w)}\) for \(w\neq\varnothing\), with \(s(z_w)=0\), \(dz_{wa}=z_wa\), and \(z_w=0\) for \(w\notin\mathcal W(I)\). Given \(z_w\), put \(o=z_wa\). Then \(s(o)=s(z_w)a=0\). Also \(do=(dz_w)a\), which is \(0\) for \(w=\varnothing\) and \(z_{w'}a'a=0\) for \(w=w'a'\). So \(o\) is a cycle of \(K\) of degree \(h(wa)+1\). There are three cases.

- If \(wa\in\mathcal W(I)\), choose \(z_{wa}\in K^{h(wa)}\) with \(dz_{wa}=o\).
- If \(w\notin\mathcal W(I)\), then \(z_w=0\) and \(o=0\); put \(z_{wa}=0\).
- If \(w\in\mathcal W(I)\) and \(wa\notin\mathcal W(I)\), then \(h(wa)=h(w)\pm1\) has just left \(I\). If \(a=x\) and \(h(wa)=U+1\), then \(o\in Z^{U+2}=0\). If \(a=y\) and \(h(wa)=L-1\), then \(o\) is a cycle of \(K^L\) with \(K^{L-1}=0\), so \(o=0\). Put \(z_{wa}=0\).

The \(A\)-linear map \(\varphi\colon P\to Z\), \(e_w\mapsto z_w\), is closed, satisfies \(s\varphi=\varepsilon_P\), and vanishes on \(Q_I\). It therefore induces \(\bar\varphi\colon R_I\to Z\) with \(s\bar\varphi=s_I\), a quasi-isomorphism in \(C^\sharp(A)\). Let \(c_w=g(z_w)\) for \(w\in\mathcal W_{-n}\), so that \(c\in\mathcal V_n(I)\). Then \(g\varphi=f_{I,c}q_I\), since both maps are \(A\)-linear and agree on the \(e_w\). Hence \(g\bar\varphi=f_{I,c}\), and
\[
\begin{aligned}
\alpha&=L_\sharp(g\bar\varphi)L_\sharp(s\bar\varphi)^{-1}\\
&=L_\sharp(f_{I,c})L_\sharp(s_I)^{-1}.
\end{aligned}
\]
By Lemma 3.2 (3), \(\Theta_nJ_\sharp(\alpha)=c\). This proves the inclusion \(\subseteq\).

*Realization.* For \(c\in\mathcal V_n(I)\) with \(I\in\mathcal I_\sharp\), the morphism \(L_\sharp(f_{I,c})L_\sharp(s_I)^{-1}\) is defined in \(D^\sharp(A)\) by Lemma 3.2 (2), and \(\Theta_n\) carries its image to \(c\).

*Injectivity.* Let \(J_\sharp\alpha=J_\sharp\alpha'\). Write \(\alpha=L_\sharp(f_{I,c})L_\sharp(s_I)^{-1}\) and \(\alpha'=L_\sharp(f_{I',c'})L_\sharp(s_{I'})^{-1}\) as above. Then \(c=c'\), and both lie in \(\mathcal V_n(I\cup I')\), where \(I\cup I'\in\mathcal I_\sharp\). Let \(r\colon R_{I\cup I'}\to R_I\) and \(r'\colon R_{I\cup I'}\to R_{I'}\) be the maps of Lemma 3.2 (4). Then
\[
\begin{aligned}
\alpha&=L_\sharp(f_{I,c}r)L_\sharp(s_Ir)^{-1}\\
&=L_\sharp(f_{I\cup I',c})L_\sharp(s_{I\cup I'})^{-1},
\end{aligned}
\]
and the same computation with \(r'\) gives this value for \(\alpha'\). \(\square\)

**Corollary 3.4 (failure of all six functors).** For the algebra of 3.0 and all \(p\leq q\), none of \(J_-\), \(J_+\), \(J_b\), \(J_{\leq q}\), \(J_{\geq p}\), \(J_{[p,q]}\) is full. Hence boundedness of \(A\), \(A^{<0}=0\) and finite total cohomology, even together, do not make any of the six comparison functors full.

**Proof.** Let \(c^+\in\prod_{w\in\mathcal W_0}k\) have \(c^+_w=1\) for \(w=x^my^m\) with \(m\geq1\), and \(c^+_w=0\) otherwise. The prefix \(x^m\) has height \(m\), so \(c^+\) lies in no \(\mathcal V_0(I)\) with \(I\in\mathcal I_-\cup\mathcal I_b\). Let \(c^-\) be defined in the same way with the words \(y^mx^m\). Their prefixes \(y^m\) have height \(-m\), so \(c^-\) lies in no \(\mathcal V_0(I)\) with \(I\in\mathcal I_+\). By Theorem 3.3, \(\beta^\pm=\Theta_0^{-1}(c^\pm)\) is not in the image of \(J_-\) and \(J_b\) (for \(+\)), respectively of \(J_+\) (for \(-\)).

The shift \([r]\) commutes with \(J_\sharp\), so \(\beta^+[-q]\in\operatorname{End}_{D(A)}(k[-q])\) is not in the image of \(J_-\), and \(\beta^+[-p]\) is not in the image of \(J_b\). Since \(k[-q]\in C^{\leq q}(A)\) and \(J_{\leq q}\) factors through \(J_-\), the functor \(J_{\leq q}\) is not full. Since \(k[-p]\in C^{[p,q]}(A)\) and \(J_{[p,q]}\) factors through \(J_b\), the functor \(J_{[p,q]}\) is not full. In the same way \(\beta^-[-p]\) shows that \(J_{\geq p}\) is not full, through \(J_+\). \(\square\)

## 4. Every finite interval

**Proposition 4.1.** Let \(k\) be a field, \(p\leq q\), \(w=q-p\), and
\[
\begin{gathered}
A=k1\oplus k\epsilon,\quad|\epsilon|=w+1,\\
\epsilon^2=0,\quad d=0,
\end{gathered}
\]
a connected differential graded \(k\)-algebra. By Theorem 2.2, \(J_{\leq q'}\), \(J_{\geq p'}\), \(J_-\), \(J_+\), \(J_b\) are fully faithful for all \(p'\), \(q'\).

1. If \(w>0\), then \(\operatorname{Hom}_{D^{[p,q]}(A)}(k[-p],k[-q])\) has one element, while \(\operatorname{Hom}_{D(A)}(k[-p],k[-q])\) is in bijection with \(k\).
2. If \(w=0\), \(J_{[p,p]}\) on \(\operatorname{End}(k[-p])\) is, through bijections, the map \(k\to\prod_{r\geq0}k\), \(\lambda\mapsto(\lambda,0,0,\dots)\). This map is injective but not surjective.

So \(J_{[p,q]}\) is not full, and the condition \(A^1=\cdots=A^{w+1}=0\) of Theorem 2.5 cannot be replaced by \(A^1=\cdots=A^w=0\).

**Proof.** Lemma 2.4 applies, because \(A^i=0\) for \(1\leq i\leq w\), and \(k\)-vector spaces split. It gives
\[
\begin{aligned}
&\operatorname{Hom}_{D^{[p,q]}(A)}(M,N)\\
&\quad\cong\textstyle\prod_i\operatorname{Hom}_k(H^iM,H^iN).
\end{aligned}
\]
Let \(P=\bigoplus_{r\geq0}e_rA\) with \(|e_r|=rw\), \(de_0=0\) and \(de_r=e_{r-1}\epsilon\). These have degree \(1\), since \((r-1)w+w+1=rw+1\), and \(d^2=0\) because \(\epsilon^2=0\). As a complex of vector spaces, \(P\) is \(ke_0\) plus the pairs \(e_r\mapsto e_{r-1}\epsilon\), so \(\rho\colon P\to k\), \(e_0\mapsto1\), is a quasi-isomorphism. Lemma 1.7 applies with \(\ell(r)=r\). The differential of \(\operatorname{Hom}^\bullet_A(P,k[n])\) vanishes, as in Lemma 3.1. So \(\beta\mapsto(f(e_r))_r\), where \(L(f)=\beta L(\rho)\), is a bijection
\[
\operatorname{Hom}_{D(A)}(k,k[n])\to\textstyle\prod_{r\geq0,\ rw=-n}k.
\]

(1) The shift \([p]\) gives a bijection from \(\operatorname{Hom}_{D(A)}(k[-p],k[-q])\) to \(\operatorname{Hom}_{D(A)}(k,k[-w])\). By the bijection above, the latter is in bijection with \(k\), through \(r=1\). The restricted group is \(\prod_i\operatorname{Hom}_k(H^ik[-p],H^ik[-q])=0\), because the cohomologies lie in the different degrees \(p\) and \(q\). A one-element set does not map onto a set with at least two elements.

(2) For \(w=0\), the restricted endomorphisms are the \(L_{[p,p]}(\lambda)\), \(\lambda\in k\), by Lemma 2.4 (3). Their images are the \(L(\lambda)\). After the shift \([p]\), \(L(\lambda)L(\rho)=L(\lambda\rho)\), whose family is \((\lambda,0,0,\dots)\). The family \((0,1,0,\dots)\) is not of this form. \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(k\) be a field, \(A=k[x]\) with \(|x|=2\) and \(d=0\), and \(k=A/xA\) in degree \(0\).

1. Show that \(\operatorname{Hom}_{D^{[0,1]}(A)}(k,k[-1])\) has one element. Let \(P=uA\oplus eA\) with \(|u|=0\), \(|e|=1\), \(du=0\), \(de=ux\), and \(\rho(u)=1\), \(\rho(e)=0\). Show that \(\operatorname{Hom}_{D(A)}(k,k[-1])\) is in bijection with \(k\), and that the closed map \(f\colon P\to k[-1]\) with \(f(e)=1\), \(f(u)=0\) gives a nonzero element \(L(f)L(\rho)^{-1}\).
2. Let \(N=A/x^2A\), with basis \(u\), \(z=ux\), and consider the exact sequence \(0\to k[-2]\xrightarrow{i}N\xrightarrow{\pi}k\to0\). Let \(r\colon\operatorname{Cone}(i)\to k\) be induced by \(\pi\), and \(c\colon\operatorname{Cone}(i)\to k[-2][1]=k[-1]\) the projection. Show that \(r\) is a quasi-isomorphism, and that \(\delta=L(c)L(r)^{-1}\) satisfies \(\delta L(\rho)=L(f)\).
3. Show that the comparison functors \(J_{\leq q}\), \(J_{\geq p}\), \(J_-\), \(J_+\), \(J_b\) and \(J_{[p,p]}\) are fully faithful for \(A\), and that \(J_{[p,p+1]}\) is not full.

**Exercise 5.2.** Let \(B\) be a differential graded ring of \(T\) with \(B^{>0}=0\). Let \(C\) be a differential graded ring with a global section \(t\) of \(C^{-1}\) satisfying \(dt=1\), and put \(A=B\times C\).

1. Show that every module \(M\) over \(C\) is acyclic.
2. Show that all six comparison functors for \(A\) are fully faithful.
3. Let \(V\) be the complex \(k\xrightarrow{\mathrm{id}}k\) in degrees \(0\) and \(1\), over a field \(k\) in the punctual topos, and \(C=\operatorname{Hom}^\bullet_k(V,V)\) with composition as product. Show that \(C\) has such a \(t\), so that \(A=k\times C\) has \(A^1\neq0\) and fully faithful comparison functors.

**Exercise 5.3.** In Proposition 4.1 with \(w=0\), show that \(\operatorname{End}_{D(A)}(k)\) is isomorphic to the ring \(k[[t]]\) of formal power series.

## 6. Complete solutions

**5.1.** (1) The nonzero components of \(A^+\) lie in degrees \(\geq2\). Lemma 2.4 applies with \(p=0\), \(q=1\), \(w=1\), and gives \(\operatorname{Hom}(k,0)\times\operatorname{Hom}(0,k)=0\). The module \(P\) has the vector space basis \(ux^m\), \(ex^m\), with \(d(ex^m)=ux^{m+1}\), so \(\rho\) is a quasi-isomorphism. Lemma 1.7 applies with \(\ell(u)=0\), \(\ell(e)=1\). A degree-zero map \(P\to k[-1]\) sends \(u\) into \(k[-1]^0=0\) and \(e\) into \(k[-1]^1=k\), and \(f(ux)=f(u)x=0\). Maps of degree \(-1\) vanish, because \(k[-1]^{-1}=k[-1]^0=0\). So \(\operatorname{Hom}_{K(A)}(P,k[-1])=k\), through \(f\mapsto f(e)\). Lemma 1.7 (3) and the invertibility of \(L(\rho)\) give the bijection.

(2) \(\operatorname{Cone}(i)\) has the basis \(u\), \(v=(0,1)\), \(z\) in degrees \(0,1,2\), with \(dv=z\), \(du=dz=0\), \(ux=z\), \(vx=zx=0\). Its cohomology is \(ku\) in degree \(0\), so \(r\), with \(r(u)=1\) and \(r(v)=r(z)=0\), is a quasi-isomorphism. The projection \(c(v)=1\), \(c(u)=c(z)=0\) is closed. The map \(j\colon P\to\operatorname{Cone}(i)\), \(j(u)=u\), \(j(e)=v\), is closed, because \(dv=z=ux\). It satisfies \(rj=\rho\) and \(cj=f\). Hence \(\delta L(\rho)=L(c)L(r)^{-1}L(rj)\), which is \(L(cj)=L(f)\). The connecting map of the cone triangle is the generator of (1), with coefficient \(+1\).

(3) \(A\) satisfies (SP), since \(A^{<0}=0\), \(A^0=k\) and \(d=0\); Theorem 2.2 gives the first five functors. Theorem 2.5 with \(w=0\) needs only \(A^1=0\), which holds. The shift \([-p]\) is an isomorphism \(C^{[0,1]}(A)\to C^{[p,p+1]}(A)\) preserving quasi-isomorphisms and commuting with the comparison functors. It carries the failure of fullness in (1) to \(J_{[p,p+1]}\).

**5.2.** (1) For a cycle \(m\) of degree \(i\), \(d(mt)=(dm)t+(-1)^im\,dt=(-1)^im\), so \(m=d((-1)^imt)\); this holds locally, hence the cohomology sheaves vanish.

(2) The section \(e=(1,0)\) is a closed central idempotent. For a module \(M\), \(M=Me\oplus M(1-e)\) as modules, \(Me\) is a \(B\)-module through \(A\to B\), and \(M(1-e)\) is a \(C\)-module, hence acyclic by (1). Let \(\Phi(M)=Me\), and let \(\Psi\) regard a \(B\)-module as an \(A\)-module. Both preserve every support condition and quasi-isomorphisms, and \(\Phi\Psi=\mathrm{id}\). The projection \(M\to\Psi\Phi(M)\) is a natural quasi-isomorphism. A natural transformation between functors that preserve quasi-isomorphisms remains natural on the localizations, as in the proof of Proposition 1.2 of the lesson on differential graded modules. So \(\Phi\) and \(\Psi\) induce inverse equivalences \(D^\star(A)\simeq D^\star(B)\) for every \(\star\), and \(D(A)\simeq D(B)\). These equivalences commute with the comparison functors, because \(\Phi\) and \(\Psi\) commute with the inclusions. The functors \(J_\star\) for \(B\) are fully faithful by Proposition 1.2 of that lesson, hence so are those for \(A\).

(3) \(C\) lies in degrees \(-1,0,1\), with \(C^1=\operatorname{Hom}(V^0,V^1)=k\), and \(d_C(g)=d_Vg-(-1)^{|g|}gd_V\). Let \(t\in C^{-1}\) be the identity \(V^1\to V^0\). Then \(d_Ct=d_Vt+td_V\), which is the identity on \(V^1\) and on \(V^0\). So (1) and (2) apply.

**5.3.** For \(w=0\), all \(e_r\) have degree \(0\). Let \(T\colon P\to P\) be the \(A\)-linear map with \(T(e_0)=0\) and \(T(e_r)=e_{r-1}\). It is closed, since \(dT(e_r)\) and \(T(de_r)\) both equal \(e_{r-2}\epsilon\), or \(0\) for \(r\leq1\). For \(F=\sum_ja_jt^j\), the sum \(F(T)(e_r)=\sum_{j\leq r}a_je_{r-j}\) is finite, so \(F(T)\) is a closed map, and \(F(T)G(T)=(FG)(T)\). Put
\[
\Phi(F)=L(\rho)L(F(T))L(\rho)^{-1}.
\]
Then \(\Phi(F)L(\rho)=L(\rho F(T))\), and \(\rho F(T)(e_r)=a_r\). By the bijection in the proof of Proposition 4.1, \(\Phi\) is bijective. It is multiplicative, and it is additive because \(L\) is additive, \(D(A)\) being the localization of the triangulated category \(K(A)\) [Stacks, Tags 0FT4, 0FT5]. So \(\Phi\) is a ring isomorphism.

## Sources

The bounded derived categories of differential graded modules, and their full faithfulness in the derived category when the ring is concentrated in nonpositive degrees, are due to Illusie, in his work on the cotangent complex. One-sided full faithfulness statements for nonnegatively graded differential graded rings with semisimple degree-zero component appear in Positselski, *Two kinds of derived categories, Koszul duality, and comodule-contramodule correspondence*, Section 3.4 ([arXiv:0905.2621](https://arxiv.org/abs/0905.2621)). Semifree resolutions and the computation of derived morphisms from them follow Keller, *Deriving DG categories* ([Numdam](https://www.numdam.org/item/ASENS_1994_4_27_1_63_0/)). K-injective resolutions and the derived category of differential graded modules are taken from the Stacks project. The argument of the main theorems follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.

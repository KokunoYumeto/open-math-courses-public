# Cohomology of flat formal categories with divided powers

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cohomology of a formal category is that of the normalized cochains of its nerve. For a PD-adic formal category whose module of differentials \(\Omega^1_R\) is flat, this cohomology is the de Rham cohomology of \(\Omega^\bullet_R\), and the comparison respects the two natural filtrations: the divided power filtration of the nerve and the Hodge filtration of the de Rham complex. This lesson proves this comparison theorem. Along the way it shows that the graded ring of the nerve is the divided power algebra of the cosimplicial module \(J/J^{[2]}\), which is the Dold–Puppe nerve of \(\Omega^1_R[-1]\), and that the tensor algebra of the augmentation ideal computes the normalized cochains. The key computation is the cobar complex of a divided power algebra in one variable, which in each weight \(m\geq2\) is a contractible Koszul complex.

**Prerequisites.** [*Décalage and the formal Poincaré lemma*](decalage-and-the-formal-poincare-lemma.md) (Theorem 2.4); [*The de Rham complex of a formal category with divided powers*](the-de-rham-complex-of-a-formal-category-with-divided-powers.md) (Proposition 1.2, Example 1.3, Lemma 2.3, Proposition 2.4, Definition 3.1, Proposition 3.4); [*Formal categories with divided powers and the Čech–Alexander complex*](formal-categories-with-divided-powers-and-the-cech-alexander-complex.md) (Proposition 1.6, Lemma 2.3, Propositions 2.6, 2.7); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Example 1.3, Theorem 3.2: Deligne–Lazard); [*Multisimplicial objects and spectral diagrams*](multisimplicial-objects-and-spectral-diagrams.md) (Lemma 2.6: Eilenberg–Zilber); [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md) (Lemma 1.4); [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md) (nerves of group objects).

## Conventions

\(C\) is a PD formal category with objects \(A\), arrows \(P\), nerve \(R\), augmentation ideal \(J\) with \(J^1=I\), and \(\Omega^1_R=I/I^{[2]}\), as in the lessons on formal categories with divided powers; for a strict category everything is levelwise. \(c^n(-)\) is the component of degree \(n\) of a cosimplicial object, and \(N\) the normalized cochain complex. Tensor products are over \(A\).

## 1. The graded nerve

The filtration of \(R\) by the components \(c^n(J^{[m]})\) has, by Lemma 2.3 (2) of the lesson on formal categories and (1.3) there,
\[
\begin{aligned}&c^n(J^{[m]})\\&=\textstyle\sum\operatorname{Im}I^{[r_1]}\otimes\cdots\\&\qquad\otimes I^{[r_n]},\end{aligned} \tag{1.1}
\]
the sum over \(r_1+\cdots+r_n\geq m\), \(r_k\geq0\), with \(I^{[0]}=P\). Write \(\operatorname{gr}R\) for the cosimplicial graded algebra of the \(J^{[m]}/J^{[m+1]}\). As in Lemma 2.2 of the lesson on décalage, componentwise, there is a surjective map of cosimplicial graded algebras
\[
\Gamma_A(J/J^{[2]})\longrightarrow\operatorname{gr}R. \tag{1.2}
\]

**Proposition 1.1.** Let \(\Omega^1_R\) be flat over \(A\).

1. In each degree \(n\), \(c^n(J/J^{[2]})\cong(\Omega^1_R)^{\oplus n}\), the \(k\)-th summand being the class of \(\iota_k(I)\). The cofaces and codegeneracies of \(J/J^{[2]}\) are those of the nerve \(K(\Omega^1_R[-1])\) of \(\Omega^1_R\) as a group object of the opposite of the category of \(A\)-modules: \(d^0\) and \(d^n\) add a zero component at the start or the end, an inner \(d^i\) repeats the \(i\)-th component, and \(s^i\) omits the component \(i+1\). In particular \(N(J/J^{[2]})=\Omega^1_R[-1]\).
2. (1.2) is an isomorphism: \(\operatorname{gr}R\cong\Gamma_AK(\Omega^1_R[-1])\) componentwise.

**Proof.** By Theorem 2.4 of the lesson on décalage, \(\operatorname{gr}P\cong\Gamma_A\Omega^1_R\), a flat \(A\)-module, as is every \(\Gamma^k_A\Omega^1_R\) (Example 1.3 of the lesson on non-additive functors: \(\Gamma\) of a flat module is a filtered colimit of \(\Gamma\) of finite free modules, by Theorem 3.2 there). For \(n\geq1\) the map
\[
\operatorname{gr}P\otimes\cdots\otimes\operatorname{gr}P\longrightarrow\operatorname{gr}\bigl(P\otimes\cdots\otimes P\bigr)
\]
of the tensor product filtration (1.1) is an isomorphism. Indeed, put \(P^r=P/I^{[r+1]}\), finitely filtered with the flat graded pieces \(\operatorname{gr}^kP\), \(k\leq r\). By Lemma 1.4 of [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md), applied to modules in degree \(0\) and by induction on the number of factors, \(\operatorname{gr}P^r\otimes\cdots\otimes\operatorname{gr}P^r\to\) \(\operatorname{gr}(P^r\otimes\cdots\otimes P^r)\) is an isomorphism, and in weights \(\leq r\) both sides agree with those for \(P\), since \(P^{\otimes n}/c^n(J^{[r+1]})=(P^r)^{\otimes n}/c^n(J^{[r+1]})\) by (1.1). In weight \(1\) this gives (1): \(c^n(J/J^{[2]})=\bigoplus_k\operatorname{gr}^1_{(k)}=(\Omega^1_R)^{\oplus n}\). The cofaces: \(d^0\iota_k=\iota_{k+1}\), \(d^n\iota_k=\iota_k\), and for an inner \(d^i\), \(d^i\iota_i(x)\) is the image of \(\delta x\equiv x\otimes1+1\otimes x\) modulo \(I\otimes I\subseteq J^{[2]}\), that is \(\iota_i(x)+\iota_{i+1}(x)\); the codegeneracy \(s^i\) applies \(\varepsilon\) to the factor \(i+1\). These are the operators of \(K(\Omega^1_R[-1])\), and the normalized complex of that nerve is \(\Omega^1_R\) in degree \(1\). For (2), \(\Gamma_A\) carries sums to tensor products (Example 1.3 there), so \(\Gamma_A(c^n(J/J^{[2]}))=(\Gamma_A\Omega^1_R)^{\otimes n}\), which is \((\operatorname{gr}P)^{\otimes n}\cong\operatorname{gr}c^n(R)\), and this composite is \(c^n\) of (1.2). \(\square\)

## 2. The tensor algebra and the normalized cochains

Filter \(N'R=T_A(I)\) (Lemma 2.3 of the lesson on the de Rham complex of a formal category) by
\[
\begin{aligned}&F^mT^n_A(I)\\&=\textstyle\sum\operatorname{Im}I^{[r_1]}\otimes\cdots\\&\qquad\otimes I^{[r_n]},\end{aligned} \tag{2.1}
\]
over \(r_1+\cdots+r_n\geq m\) with all \(r_k\geq1\). The differential preserves it: on \(I^{[r]}\), \(d\) is the restriction of \(1\otimes x-\delta x+x\otimes1\), and \(\delta(I^{[r]})\subseteq\sum_{a+b=r}\operatorname{Im}I^{[a]}\otimes I^{[b]}\), the terms with \(a=0\) or \(b=0\) cancelling against \(1\otimes x\) and \(x\otimes1\) modulo the terms with \(a,b\geq1\) (as \(d(I)\subseteq I\otimes I\)); on tensors \(d\) is an antiderivation. By (1.1), the map \(u\colon N'R\to NR\) of Proposition 2.4 there sends \(F^m\) into \(N(J^{[m]})\).

**Proposition 2.1.** If \(\Omega^1_R\) is flat, \(u\) induces an isomorphism \(\operatorname{gr}N'R\to\operatorname{gr}NR=N\operatorname{gr}R\). If moreover \(C\) is PD-adic, \(u\colon F^mN'R\to N(J^{[m]})\) is an isomorphism of pro-complexes for every \(m\); in particular \(N'R\cong NR\).

**Proof.** As in Proposition 1.1, \(\operatorname{gr}T^n_A(I)=(\operatorname{gr}^{\geq1}P)^{\otimes n}=(\Gamma^{+}_A\Omega^1_R)^{\otimes n}\), where \(\Gamma^+=\bigoplus_{k\geq1}\Gamma^k\). On the other side, \(\operatorname{gr}R=\Gamma_AK(\Omega^1_R[-1])\) by Proposition 1.1, a PD formal category with \(d^0=d^1\) (its arrows are \(\Gamma_A\Omega^1_R\) with \(A\) acting the same way on both sides), so by Proposition 2.4 of the lesson on the de Rham complex of a formal category its normalized cochains are \(T_A(\Gamma^+_A\Omega^1_R)\), and \(N\) commutes with \(\operatorname{gr}\), being exact. The map \(\operatorname{gr}u\) is the identity of \(T_A(\Gamma^+\Omega^1_R)\) under these identifications. If \(C\) is PD-adic, \(R=\text{“}\varprojlim_M\text{”}R/J^{[M]}\) (Proposition 2.7 of the lesson on formal categories), and an isomorphism on \(\operatorname{gr}\) between finitely filtered objects is an isomorphism, so \(u\colon F^mN'R/F^{M}\to N(J^{[m]}/J^{[M]})\) is one for all \(M\geq m\). \(\square\)

## 3. The comparison with the de Rham complex

From here on \(C\) is PD-adic and \(\Omega^1_R\) is flat. By Proposition 3.4 (3) of the lesson on the de Rham complex of a formal category, \(\Omega^\bullet_R\) is a complex, and by Proposition 2.1 the map \(p\) of that lesson is a map of differential graded algebras
\[
p\colon NR\cong N'R\longrightarrow\Omega^\bullet_R. \tag{3.1}
\]
Give \(\Omega^\bullet_R\) the Hodge filtration: \(F^m\Omega^\bullet_R\) is \(\Omega^\bullet_R\) with the terms of degree \(<m\) replaced by \(0\).

**Lemma 3.1.** \(p(N(J^{[m]}))\subseteq F^m\Omega^\bullet_R\).

**Proof.** By Proposition 2.1, \(N^n(J^{[m]})\) is spanned by the images of \(I^{[r_1]}\otimes\cdots\otimes I^{[r_n]}\) with \(r_k\geq1\) and \(\sum r_k\geq m\). If \(n<m\), some \(r_k\geq2\), and \(p\) kills \(I^{[r_k]}\subseteq I^{[2]}\). So \(p\) vanishes on \(N^n(J^{[m]})\) for \(n<m\). \(\square\)

**3.2. The model.** For an \(A\)-module \(V\), the cosimplicial algebra \(\Gamma_AK(V[-1])\), with \(c^n=\Gamma_AV\otimes\cdots\otimes\Gamma_AV\), is the nerve of a PD formal category with \(d^0=d^1\): its arrows are \(\Gamma_AV\), with comultiplication induced by the diagonal \(V\to V\oplus V\) (so \(v\mapsto v\otimes1+1\otimes v\)) and augmentation \(\Gamma^+V\mapsto0\). Its module of differentials is \(\Gamma^+V/\Gamma^{\geq2}V=V\), and its de Rham complex is \(\Lambda_AV\) with zero differential: \(\bar d_0=0\) as \(d^0=d^1\), and \(dv=1\otimes v-\delta v+v\otimes1=0\) for \(v\in V\). The cosimplicial algebra is graded by weight, \(\Gamma^m\) summed over the factors, and \(p\) preserves weight, sending the weight \(m\) part \(N\Gamma^mK(V[-1])\) to \(\Lambda^mV[-m]\) (by Lemma 3.1 and the weights).

**Lemma 3.3.** Let \(V=A\,t\) be free of rank \(1\). For \(m\geq2\), the weight \(m\) part of \(N\Gamma_AK(V[-1])\) is acyclic; for \(m=0,1\), \(p\) is the identity of \(A\), resp. of \(V[-1]\). So \(p\) is a quasi-isomorphism.

**Proof.** By Proposition 2.4 of the lesson on the de Rham complex of a formal category, \(N\Gamma_AK(V[-1])=T_A(\Gamma^+V)\), with \(d\) the antiderivation (2.2) there and \(d\,t^{[r]}=-\sum_{i,j\geq1,\,i+j=r}t^{[i]}\otimes t^{[j]}\) by (1.2) there. In weight \(m\geq1\) and degree \(n\), the basis is \(t^{[r_1]}\otimes\cdots\otimes t^{[r_n]}\) over the compositions \(r_1+\cdots+r_n=m\), \(r_k\geq1\). Send it to \(e_S=e_{s_1}\wedge\cdots\wedge e_{s_{n-1}}\) in the exterior algebra \(E\) of \(A^{m-1}\) with basis \(e_1,\ldots,e_{m-1}\), where \(s_j=r_1+\cdots+r_j\) are the cut points. The differential inserts a cut point \(c\) inside the \(k\)-th part, with the sign \(-(-1)^{k-1}\), and \(e_c\wedge e_S=(-1)^{k-1}e_{S\cup\{c\}}\), since \(e_c\) passes the \(k-1\) cut points smaller than \(c\). So the weight \(m\) complex is \(E\) with the differential \(-\omega\wedge\), \(\omega=e_1+\cdots+e_{m-1}\), placed with \(\Lambda^{n-1}\) in degree \(n\). For \(m\geq2\) the interior product \(h\) with the linear form \(e_1\mapsto1\), \(e_c\mapsto0\) for \(c\neq1\), satisfies \(h(\omega\wedge\eta)+\omega\wedge h(\eta)=\eta\), so the complex is contractible. In weights \(0\) and \(1\) the complexes are \(A\) in degree \(0\) and \(A\,t\) in degree \(1\), which \(p\) maps identically onto \(\Lambda^0V\) and \(\Lambda^1V[-1]\). \(\square\)

**Lemma 3.4.** If \(V\) is flat, \(p\colon N\Gamma_AK(V[-1])\to\Lambda_AV\) (with zero differential, \(\Lambda^mV\) in degree \(m\)) is a quasi-isomorphism.

**Proof.** *Sums.* For \(A\)-modules \(V\), \(W\), \(\Gamma_AK((V\oplus W)[-1])\) is the diagonal of the bicosimplicial algebra \(\Gamma_AK(V[-1])\otimes\Gamma_AK(W[-1])\), as \(\Gamma\) carries sums to tensor products. By Lemma 2.6 of the lesson on multisimplicial objects, applied in the opposite of the category of \(A\)-modules, the Alexander–Whitney product \(x\otimes y\mapsto x\cdot y\) (Proposition 1.2 of the lesson on the de Rham complex of a formal category) is a quasi-isomorphism from \(N\Gamma K(V[-1])\otimes N\Gamma K(W[-1])\) to \(N\Gamma K((V\oplus W)[-1])\). As \(p\) is multiplicative, \(p(x\cdot y)=p(x)\wedge p(y)\), and \(\Lambda V\otimes\Lambda W\to\Lambda(V\oplus W)\) is an isomorphism. So if the lemma holds for \(V\) and \(W\), free of finite type, it holds for \(V\oplus W\), the complexes involved being complexes of free modules.

*Free modules.* By Lemma 3.3 and induction on the rank, the lemma holds locally for finite free \(V\).

*Flat modules.* By Theorem 3.2 of the lesson on non-additive functors, \(V\) is the local inductive limit of a local system of finite free modules. Both sides commute with filtered colimits, \(\Gamma\), \(\Lambda\), \(K\) and \(N\) doing so, and cohomology commutes with filtered colimits; so \(p\) is a quasi-isomorphism locally, hence a quasi-isomorphism. \(\square\)

**Theorem 3.5.** Let \(C\) be PD-adic with \(\Omega^1_R\) flat. Then \(\operatorname{gr}p\colon N\operatorname{gr}R\to\operatorname{gr}\Omega^\bullet_R=\bigoplus_m\Omega^m_R[-m]\) is a quasi-isomorphism, and for every \(m\) and \(M\geq m\),
\[
p\colon N(J^{[m]}/J^{[M]})\to F^m\Omega^\bullet_R/F^M\Omega^\bullet_R
\]
is a quasi-isomorphism. So \(p\colon N(J^{[m]})\to F^m\Omega^\bullet_R\) is a quasi-isomorphism of pro-complexes, and in particular \(NR\to\Omega^\bullet_R\): the cohomology of a flat PD-adic formal category is its de Rham cohomology, compatibly with the filtrations.

**Proof.** By Proposition 1.1, \(\operatorname{gr}R\cong\Gamma_AK(\Omega^1_R[-1])\), and under this isomorphism \(\operatorname{gr}p\) is the map \(p\) of 3.2 for \(V=\Omega^1_R\). Indeed both are multiplicative and send the class of \(x\in I\) in \(J/J^{[2]}\) of degree \(1\) to \(\bar x\in\Omega^1_R\). By Lemma 3.4 it is a quasi-isomorphism. The second assertion follows by induction on \(M-m\) from the short exact sequences \(0\to N(J^{[M-1]}/J^{[M]})\to\) \(N(J^{[m]}/J^{[M]})\to\) \(N(J^{[m]}/J^{[M-1]})\to0\) and their Hodge counterparts, \(N\) being exact. \(\square\)

**Remark 3.6.** Theorem 3.5 applied to the shifted category of the lesson on décalage gives a second proof of the formal Poincaré lemma there: the augmented cosimplicial algebra \(A\to\operatorname{Dec}(R)\) is contractible (the forgotten codegeneracy \(s^0\) is a contracting homotopy of its cochains), so its normalized cochains are a resolution of \(A\), and so is \(A\to\Omega^\bullet_{C'}\). Applied to the Čech–Alexander complex of a smooth morphism, it identifies the cohomology of that complex with de Rham cohomology.

## 4. Exercises

**Exercise 4.1.** Write the weight \(3\) part of \(N\Gamma_AK(At[-1])\) in degrees \(1,2,3\) and check its acyclicity directly.

**Exercise 4.2.** For \(V=A^2\) with basis \(t,u\), compute the cohomology of the weight \(2\) part of \(N\Gamma_AK(V[-1])\) and compare with \(\Lambda^2V\).

## 5. Complete solutions

**Solution 4.1.** Degree \(1\): \(t^{[3]}\); degree \(2\): \(t\otimes t^{[2]}\), \(t^{[2]}\otimes t\); degree \(3\): \(t\otimes t\otimes t\). The differential: \(d\,t^{[3]}=-t\otimes t^{[2]}-t^{[2]}\otimes t\), \(d(t\otimes t^{[2]})=-t\otimes dt^{[2]}=t\otimes t\otimes t\) and \(d(t^{[2]}\otimes t)=dt^{[2]}\otimes t=-t\otimes t\otimes t\) (using \(dt=0\), \(dt^{[2]}=-t\otimes t\)). So \(d\) is injective on degree \(1\), its image \(A(t\otimes t^{[2]}+t^{[2]}\otimes t)\) is the kernel in degree \(2\), and degree \(3\) is the image of \(t\otimes t^{[2]}\): acyclic.

**Solution 4.2.** Weight \(2\): degree \(1\) has \(t^{[2]}\), \(tu\), \(u^{[2]}\); degree \(2\) has \(t\otimes t\), \(t\otimes u\), \(u\otimes t\), \(u\otimes u\). Here \(d(t^{[2]})=-t\otimes t\), \(d(u^{[2]})=-u\otimes u\), and \(d(tu)=-(t\otimes u+u\otimes t)\), since \(\delta(tu)=\delta t\,\delta u\). So \(d\) is injective, and the cokernel in degree \(2\) is free of rank \(1\), generated by the class of \(t\otimes u\) (with \(u\otimes t\equiv-t\otimes u\)), which \(p\) sends to \(t\wedge u\): the cohomology is \(\Lambda^2V\) in degree \(2\), as Lemma 3.4 says.

## Sources

The identification of the graded nerve, the comparison of the tensor algebra with the normalized cochains and the comparison theorem with de Rham cohomology are due to Illusie, in his work on the cotangent complex, with the reduction to the model through the Deligne–Lazard theorem and the Künneth formula; the proof of the rank \(1\) case here goes through the complex of cut points instead of the décalage formula for divided powers.

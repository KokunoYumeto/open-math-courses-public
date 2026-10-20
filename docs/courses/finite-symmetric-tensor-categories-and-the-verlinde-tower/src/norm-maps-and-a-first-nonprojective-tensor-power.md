# Norm maps and a first nonprojective tensor power

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 5 reduced the exactness of the higher Frobenius functor \(\Phi\) to a nonvanishing statement: \(\Theta\) must not kill the \(kE_r\)-module \(\operatorname{Hom}(P,P^{\otimes p^r})\), for a projective generator \(P\). Since \(\Theta\) kills all projective modules, this module must at least be nonprojective. This lesson shows that there is a least \(r\) for which it is nonprojective, and that for this \(r\) its restrictions to all proper subgroups of \(E_r\) are projective (Proposition 4.1). The argument plays two facts against each other. If all the modules \(\operatorname{Hom}(P,P^{\otimes p^a})\) were projective, Chouinard's theorem would make every \(\operatorname{Hom}(P,P^{\otimes d})\) projective over the whole symmetric group, so that every total symmetrizer acts nontrivially on \(P^{\otimes d}\). But the dimensions of \(\operatorname{End}(P^{\otimes d})\) grow only exponentially, so the action of the symmetric groups has a nonzero kernel, and a nonzero tensor ideal of the symmetric group algebras contains a total symmetrizer.

**Prerequisites.** [*Finite symmetric tensor categories and fibre functors*](finite-symmetric-tensor-categories-and-fibre-functors.md), Section 1; [*Higher Frobenius functors*](higher-frobenius-functors.md), Section 1; [*Representations and complete reducibility*](course:RT-FIN/representations-and-complete-reducibility).

## 1. Norm maps

Let \(\mathcal C\) be a finite symmetric tensor category with projective generator \(P\) and the exact faithful functor \(\omega=\operatorname{Hom}(P,-)\) of Lemma 1.3 of Lesson 1. For an object \(X\) with an action of a finite group \(H\), the *invariants* \(X^H\) and *coinvariants* \(X_H\) are the kernel and the cokernel of the morphisms
\[
X\to\textstyle\bigoplus_{h\in H}X,\qquad\bigoplus_{h\in H}X\to X
\]
with components \(h-1\). The endomorphism \(N_H=\sum_{h\in H}h\) of \(X\) vanishes on the image of each \(h-1\) and has image in \(X^H\), so it factors through a morphism
\[
\nu_H(X)\colon X_H\to X^H,
\]
the *norm map*. Exact \(k\)-linear functors preserve invariants, coinvariants and norm maps. For a \(kH\)-module \(M\) these are the usual invariants \(M^H\), coinvariants \(M/I_HM\), with \(I_H\) the augmentation ideal, and the map induced by \(N_H\).

**Lemma 1.1.** Let \(G\) be a finite group and \(M\) a finite-dimensional \(kG\)-module.

1. If \(M\) is projective, then \(\nu_G(M)\) is an isomorphism.
2. If \(G\) is a \(p\)-group and \(\nu_G(M)\) is an isomorphism, then \(M\) is projective.

*Proof.* (1) For the regular module \(kG\), the coinvariants are \(kG/I_G\), spanned by the class of \(1\), and the invariants are spanned by \(N_G\), since an invariant element has equal coefficients at all group elements. The norm map sends the class of \(1\) to \(N_G\), so it is an isomorphism. The norm map is natural and additive, so it is an isomorphism for free modules and their direct summands.

(2) Let \(G\) be a \(p\)-group. *The augmentation ideal is nilpotent.* Induct on \(|G|\). Choose a central element \(z\) of order \(p\). The kernel of \(kG\to k[G/\langle z\rangle]\) is \((z-1)kG\), and \(((z-1)kG)^p=(z-1)^pkG\)\(=(z^p-1)kG=0\) because \(z-1\) is central. The augmentation ideal of \(k[G/\langle z\rangle]\) is nilpotent by induction, say with \(m\)-th power zero, so \(I_G^m\subset(z-1)kG\) and \(I_G^{mp}=0\). Hence \(kG\) is local with maximal ideal \(I_G\), and the trivial module \(k\) is its only simple module.

*The algebra \(kG\) is self-injective.* The bilinear form \((a,b)\mapsto\) the coefficient of \(1\) in \(ab\) is nondegenerate, since \((g,g^{-1})\mapsto1\), and satisfies \((ca,b)=(c,ab)\). So \(a\mapsto(\cdot\,,a)\) identifies the left regular module with the dual of the right regular module, which is injective because the right regular module is projective.

*The socle.* A nonzero left ideal contains a simple submodule, which is trivial, hence spanned by an invariant element, a multiple of \(N_G\). So every nonzero left ideal contains \(N_G\). If \(m\in M\) satisfies \(N_Gm\ne0\), the kernel of \(kG\to M\), \(a\mapsto am\), is a left ideal not containing \(N_G\), hence zero; by self-injectivity the injective map \(kG\to M\) splits. Repeating, \(M\cong(kG)^a\oplus M'\) with \(N_GM'=0\). Then \(\nu_G(M')=0\). If \(M'\ne0\), then \(M'_G=M'/I_GM'\ne0\) by Nakayama's lemma, so \(\nu_G(M)=\nu_G((kG)^a)\oplus\nu_G(M')\) is not an isomorphism. So an isomorphic norm map forces \(M'=0\) and \(M\cong(kG)^a\). \(\square\)

**Lemma 1.2.** Let finite \(p\)-groups \(H_1,\dots,H_s\) act on objects \(X_1,\dots,X_s\) of \(\mathcal C\), and let \(H=H_1\times\cdots\times H_s\) act on \(X=X_1\otimes\cdots\otimes X_s\) factor by factor. If each \(\omega(X_i)\) is a projective \(kH_i\)-module, then \(\omega(X)\) is a projective \(kH\)-module, and its restriction to every subgroup of \(H\) is projective.

*Proof.* By Lemma 1.1(1), \(\omega(\nu_{H_i}(X_i))=\nu_{H_i}(\omega X_i)\) is an isomorphism, and the exact faithful functor \(\omega\) reflects isomorphisms, so each \(\nu_{H_i}(X_i)\) is an isomorphism. Let groups \(H',K'\) act on objects \(Y,Z\). Because \(-\otimes Z\) and \(Y\otimes-\) are exact, taking invariants and coinvariants one group at a time gives
\[
\begin{gathered}
(Y\otimes Z)^{H'\times K'}\cong Y^{H'}\otimes Z^{K'},\\
(Y\otimes Z)_{H'\times K'}\cong Y_{H'}\otimes Z_{K'},
\end{gathered}
\]
and under these identifications \(\nu_{H'\times K'}(Y\otimes Z)=\nu_{H'}(Y)\otimes\nu_{K'}(Z)\), because \(N_{H'\times K'}=N_{H'}\otimes N_{K'}\). By induction on \(s\), \(\nu_H(X)\) is an isomorphism, so \(\nu_H(\omega X)=\omega(\nu_H(X))\) is one, and \(\omega(X)\) is projective by Lemma 1.1(2), as \(H\) is a \(p\)-group. A group algebra is free over the group algebra of a subgroup, so restriction preserves projectivity. \(\square\)

The point of Lemma 1.2 is that \(\omega\) does not preserve tensor products, \(\omega(X\otimes Y)\ne\omega(X)\otimes\omega(Y)\) in general; projectivity is transported through the internal norm maps instead.

## 2. Two results from the representation theory of finite groups

**Theorem 2.1** (Chouinard; named result N6, part 1 [Ben, Corollary 2.24.5]). Let \(G\) be a finite group and \(M\) a finite-dimensional \(kG\)-module. Then \(M\) is projective if and only if its restriction to every elementary abelian \(p\)-subgroup of \(G\) is projective.

**Theorem 2.2** (Kleshchev; named result N7 [CEO, Appendix A, Proposition A.1]). For every \(n\ge1\) there is \(m\ge n\) such that the composite
\[
kS_n\hookrightarrow kS_m\to\operatorname{End}_k(P_0)
\]
is injective, where \(S_n\subset S_m\) permutes \(\{1,\dots,n\}\), and \(P_0\) is the projective cover of the trivial \(kS_m\)-module, on which \(kS_m\) acts by left multiplication.

Let \(\mathsf{Sym}\) be the monoidal category with objects \(0,1,2,\dots\), endomorphism algebras \(\operatorname{End}(n)=kS_n\), no morphisms between different objects, and tensor product given by addition on objects and by the block inclusions \(kS_a\otimes kS_b\to kS_{a+b}\) on morphisms. A *tensor ideal* of \(\mathsf{Sym}\) is a family of two-sided ideals \(J_n\subset kS_n\) such that \(J_a\otimes kS_b\subset J_{a+b}\) and \(kS_b\otimes J_a\subset J_{b+a}\). Write \(b_n=\sum_{\sigma\in S_n}\sigma\) for the total symmetrizer.

**Lemma 2.3** ([CEO, Lemma 4.10]). Every nonzero tensor ideal \(J\) of \(\mathsf{Sym}\) contains \(b_m\) for some \(m\).

*Proof.* Choose \(n\) and \(0\ne f\in J_n\), and \(m\ge n\) as in Theorem 2.2. Then \(f\otimes1\in J_m\), and this is \(f\) regarded as an element of \(kS_m\). By Theorem 2.2, \(f\) acts nontrivially on \(P_0\), which is a direct summand \(kS_me\) of the regular module for an idempotent \(e\); so there is \(g\in P_0\) with \(fg\ne0\).

*The socle of \(P_0\) is \(kb_m\).* The augmentation \(\varepsilon\) satisfies \(\varepsilon(e)=1\), because \(P_0\) maps onto the trivial module, so \(b_m=b_me\in P_0\), since \(b_ma=\varepsilon(a)b_m\) for all \(a\). The algebra \(kS_m\) is self-injective (proof of Lemma 1.1), so \(P_0\) is an injective module. An indecomposable injective module has a simple socle: if its socle contained \(S_1\oplus S_2\), an injective hull of \(S_1\) inside it would be a proper direct summand, since it meets \(S_2\) in zero. The line \(kb_m\) is a simple submodule of \(P_0\), so it is the socle, and every nonzero submodule of \(P_0\) contains \(b_m\).

Hence \(kS_m\,fg\) contains \(b_m\): there is \(h\) with \(b_m=hfg\in J_m\). \(\square\)

## 3. Kernels of tensor powers

For an object \(X\) of \(\mathcal C\), the symmetry gives algebra homomorphisms \(kS_n\to\operatorname{End}(X^{\otimes n})\), and these are compatible with the block inclusions: a monoidal functor \(\mathsf{Sym}\to\mathcal C\), \(n\mapsto X^{\otimes n}\). The kernels of these homomorphisms form a tensor ideal of \(\mathsf{Sym}\), since a monoidal functor carries \(f\otimes1\) to \(F(f)\otimes1\).

**Lemma 3.1.** Let \(\ell(X)\) denote the length of an object. Then \(\dim_k\operatorname{Hom}(X,Y)\le\ell(X)\ell(Y)\). If \(b=\max_S\ell(S\otimes X)\), the maximum over the simple objects \(S\), then \(\ell(X^{\otimes d})\le\ell(X)\,b^{d-1}\).

*Proof.* For simple \(S,S'\), \(\dim\operatorname{Hom}(S,S')\le1\), by Schur's lemma and \(\operatorname{End}(S)=k\). Since \(\operatorname{Hom}\) is left exact in each variable, induction on composition series gives the first bound. The object \(X^{\otimes d}=X^{\otimes(d-1)}\otimes X\) has a filtration whose quotients are \(S\otimes X\) for the composition factors \(S\) of \(X^{\otimes(d-1)}\), by exactness of \(-\otimes X\), so \(\ell(X^{\otimes d})\le b\,\ell(X^{\otimes(d-1)})\). \(\square\)

So \(\dim\operatorname{End}(X^{\otimes d})\le\ell(X)^2b^{2(d-1)}\) grows at most exponentially in \(d\), while \(\dim kS_d=d!\). For every nonzero \(X\), the kernel ideal of \(n\mapsto X^{\otimes n}\) is therefore nonzero.

## 4. The least nonprojective rank

Let \(E_a=(\mathbb Z/p)^a\) act on \(p^a\) positions by a regular action, and hence on \(P^{\otimes p^a}\) through the symmetry. Put
\[
\begin{aligned}
M(a)&=\omega(P^{\otimes p^a})\\
&=\operatorname{Hom}(P,P^{\otimes p^a}),\qquad a\ge1,
\end{aligned}
\]
a \(kE_a\)-module.

**Proposition 4.1** ([OpenAI-208, Proposition 5.3]). There is a least integer \(r\ge1\) for which \(M(r)\) is not a projective \(kE_r\)-module. For this \(r\), the restriction of \(M(r)\) to every proper subgroup of \(E_r\) is projective.

*Proof.* Suppose that every \(M(a)\) is projective. Fix \(d\ge1\) and an elementary abelian \(p\)-subgroup \(H\subset S_d\). On each \(H\)-orbit \(O_i\subset\{1,\dots,d\}\) the group \(H\) acts through a quotient \(H/K_i\), and regularly, because \(H\) is abelian: the stabilizers of the points of an orbit coincide. Choose isomorphisms \(H/K_i\cong E_{a_i}\), with \(a_i=0\) for fixed points. Regrouping the tensor factors with the symmetry identifies \(P^{\otimes d}\), as an object with \(H\)-action, with \(\bigotimes_iP^{\otimes O_i}\), where \(H\) acts on \(P^{\otimes O_i}\) through \(H/K_i\). The module \(\omega(P^{\otimes O_i})\) is \(M(a_i)\), up to the choice of a base point of the orbit, so it is projective over \(k[H/K_i]\) when \(a_i>0\), and trivially when \(a_i=0\). Lemma 1.2 makes \(\omega(P^{\otimes d})\) projective over \(k[\prod_iH/K_i]\). The map \(H\to\prod_iH/K_i\) is injective because \(H\) acts faithfully on \(\{1,\dots,d\}\), so \(\omega(P^{\otimes d})\) is projective over \(kH\). By Theorem 2.1, \(\omega(P^{\otimes d})\) is projective over \(kS_d\).

The \(d\)-th tensor power of an epimorphism \(P\to\mathbf 1\) is an \(S_d\)-equivariant epimorphism \(P^{\otimes d}\to\mathbf 1\), where \(S_d\) acts trivially on \(\mathbf 1^{\otimes d}=\mathbf 1\). Applying \(\omega\) and passing to coinvariants gives an epimorphism \(\omega(P^{\otimes d})_{S_d}\to\omega(\mathbf 1)\ne0\). By Lemma 1.1(1) the norm map of \(\omega(P^{\otimes d})\) is an isomorphism of nonzero spaces, so \(b_d\) acts nontrivially on \(\omega(P^{\otimes d})\), hence on \(P^{\otimes d}\). This holds for every \(d\ge1\).

On the other hand, by Section 3 the kernels of \(kS_d\to\operatorname{End}(P^{\otimes d})\) form a nonzero tensor ideal of \(\mathsf{Sym}\), which contains some \(b_m\) by Lemma 2.3. So \(b_m\) acts as zero on \(P^{\otimes m}\), a contradiction. Hence some \(M(a)\) is not projective, and there is a least such \(r\).

Let \(H<E_r\) be a proper subgroup, of rank \(a<r\). It acts freely on the \(p^r\) positions, which split into \(p^{r-a}\) regular \(H\)-orbits. By minimality of \(r\) (or trivially, if \(a=0\)), the module \(\omega(P^{\otimes O})\) is projective over \(kH\) for each orbit \(O\). Lemma 1.2, applied to the product of the copies of \(H\) acting on the separate orbits and restricted to the diagonal copy of \(H\), which is the given action, shows that \(M(r)\) restricted to \(H\) is projective. \(\square\)

The least \(r\) depends on \(\mathcal C\), and \(r=1\) is possible (Exercise 5.4). The statements hold for \(p=2\) as well.

## 5. Exercises

**5.1.** Let \(p=2\) and \(G=\mathbb Z/2\). Compute the norm maps of the trivial module and of the regular module, and use Lemma 1.1 to decide which is projective.

**5.2.** Let \(p=3\) and \(G=S_3\). Show that the trivial module is not projective, using Lemma 1.1(1).

**5.3.** Check that the kernels of \(kS_n\to\operatorname{End}(X^{\otimes n})\) satisfy the two conditions in the definition of a tensor ideal of \(\mathsf{Sym}\).

**5.4.** Let \(G\) be a finite group and \(\mathcal C=\operatorname{Rep}_k(G)\), with projective generator \(P=kG\). Show that \(M(1)\) is not projective, so that \(r=1\).

## 6. Solutions

**5.1.** On the trivial module, coinvariants and invariants are \(k\), and \(N_G=1+g\) acts by \(2=0\); the norm map is zero, so the trivial module is not projective. On the regular module \(k[g]/(g^2-1)\), the coinvariants are spanned by the class of \(1\) and the invariants by \(1+g\), and the norm map sends the first to the second: an isomorphism, as Lemma 1.1(1) requires.

**5.2.** On the trivial module, \(N_{S_3}\) acts by \(6=0\) in characteristic \(3\), while coinvariants and invariants are both \(k\). The norm map is zero, not an isomorphism, so by Lemma 1.1(1) the module is not projective. (Lemma 1.1(2) does not apply, because \(S_3\) is not a \(3\)-group.)

**5.3.** Each kernel is a two-sided ideal, being the kernel of an algebra homomorphism. If \(f\in kS_a\) acts as zero on \(X^{\otimes a}\), then \(f\otimes g\) acts on \(X^{\otimes a}\otimes X^{\otimes b}\) as the tensor product of the two actions, which is zero; similarly for \(g\otimes f\).

**5.4.** For \(Y\) in \(\operatorname{Rep}_k(G)\), \(\operatorname{Hom}_G(kG,Y)\cong Y\) by evaluation at \(1\), compatibly with any action of a group on \(Y\) by \(G\)-module automorphisms. So \(M(1)\cong(kG)^{\otimes p}\) as a \(k[\mathbb Z/p]\)-module, with the generator permuting the tensor factors cyclically. The basis of pure tensors \(g_1\otimes\cdots\otimes g_p\) is permuted, so \(M(1)\) is a permutation module. A constant tuple \(g\otimes\cdots\otimes g\) is fixed and spans a trivial direct summand, and the trivial module is not projective over \(k[\mathbb Z/p]\) (Exercise 5.1 for \(p=2\), and the same computation for every \(p\)). A direct summand of a projective module is projective, so \(M(1)\) is not projective.

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 5 (Lemmas 5.1 and 5.2, Proposition 5.3). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [Ben] D. J. Benson, *Modular representation theory: new trends and methods*, Lecture Notes in Math. 1081 (1984), author's copy: Corollary 2.24.5. https://homepages.abdn.ac.uk/d.j.benson/pages/papers/b/benson/sln1081.pdf
- [CEO] K. Coulembier, P. Etingof and V. Ostrik, *On Frobenius exact symmetric tensor categories*, Ann. of Math. 197 (2023), with an appendix by A. Kleshchev, numbering of arXiv:2107.02372v2: Lemma 4.10 and Proposition A.1. https://arxiv.org/abs/2107.02372v2

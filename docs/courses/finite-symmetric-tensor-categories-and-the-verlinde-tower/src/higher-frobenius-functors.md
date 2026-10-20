# Higher Frobenius functors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a finite symmetric tensor category \(\mathcal C\) the tensor power \(X^{\otimes q}\), \(q=p^r\), carries an action of the symmetric group \(S_q\) by permutation of the factors. Coulembier and Flake proposed to turn this action into a functor to \(\mathcal C\boxtimes\operatorname{Ver}_{p^r}\) by restricting it to an elementary abelian group acting regularly on the \(q\) factors and applying a suitable symmetric monoidal functor \(\Theta\colon\operatorname{Rep}_k(E_r)\to\operatorname{Ver}_{p^r}\) [CF]. They showed that \(\Theta\) exists once the restricted tilting theorem holds, which Lessons 3 and 4 proved. This lesson records their construction, shows how to evaluate the resulting functor \(\Phi\) at projective objects, and proves the criterion by which \(\Phi\) will be shown to be exact: it is enough that \(\Theta\) does not kill one module of the form \(\operatorname{Hom}(Q,P^{\otimes q})\).

**Prerequisites.** [*Finite symmetric tensor categories and fibre functors*](finite-symmetric-tensor-categories-and-fibre-functors.md), Sections 1, 2 and 4; [*The restricted tilting theorem*](the-restricted-tilting-theorem.md); [*Induced representations and Frobenius reciprocity*](course:RT-FIN/induced-representations-and-frobenius-reciprocity).

## 1. Modules over an elementary abelian group

Let \(E=E_r=(\mathbb Z/p)^r\) with generators \(g_1,\dots,g_r\), and \(q=p^r=|E|\). In \(kE\) the elements \(x_i=g_i-1\) satisfy \(x_i^p=g_i^p-1=0\), so
\[
kE=k[x_1,\dots,x_r]/(x_1^p,\dots,x_r^p),
\]
a local ring whose maximal ideal \((x_1,\dots,x_r)\) is nilpotent. Over a local finite-dimensional algebra every finitely generated projective module is free: a projective module \(M\) has a minimal surjection from a free module \((kE)^m\to M\), lifting a basis of \(M/\mathfrak mM\); it splits by projectivity, and the complement is zero by Nakayama's lemma. So a projective \(kE\)-module has dimension divisible by \(q\).

For a subgroup \(H<E\) and a \(kH\)-module \(D\) write \(\operatorname{Ind}_H^ED=kE\otimes_{kH}D\). For a \(kE\)-module \(M\) the *tensor identity* is the isomorphism
\[
M\otimes\operatorname{Ind}_H^ED\xrightarrow{\ \sim\ }\operatorname{Ind}_H^E(\operatorname{Res}^E_HM\otimes D),
\]
\(m\otimes(g\otimes d)\mapsto g\otimes(g^{-1}m\otimes d)\) (Exercise 7.1). Induction carries projective \(kH\)-modules to projective \(kE\)-modules, since \(\operatorname{Ind}_H^EkH=kE\).

## 2. The construction of Coulembier and Flake

Fix an injective homomorphism \(\iota\colon E\to U(k)\), with restriction functor \(R=R_\iota\) on rational \(\mathrm{SL}_2\)-modules, and put \(\mathcal W=\operatorname{Ver}_{q}(k)\). Recall from Lesson 1 the category \(\mathcal T\) of tilting modules, the ideal \(I_n\) of morphisms factoring through sums of modules \(T(a)\) with \(a\ge p^n-1\), and the fully faithful functor \(\Sigma_r\colon\mathcal T/I_r\to\mathcal W\) of Theorem 4.2 of Lesson 1. In particular \(T(a)\) is zero in \(\mathcal T/I_n\) exactly when \(a\ge p^n-1\), and \(\operatorname{St}_{n'}=T(p^{n'}-1)\) is zero in \(\mathcal T/I_n\) whenever \(n'\ge n\).

**Theorem 2.1** (named result N5 [CF]).

1. (Stable restriction [CF, Theorem 5.3.5(1)].) For every \(n\ge1\) and every injective homomorphism \(E_n\to U(k)\), the restriction of a tilting module \(T\) that is zero in \(\mathcal T/I_n\) is a projective \(kE_n\)-module.
2. (The functor \(\Theta\) [CF, Conjecture 5.4.2 and Theorem 5.4.3].) Suppose that \(R(\operatorname{St}_{r-1})\otimes D\) is isomorphic to the restriction of a tilting module for every \(kE\)-module \(D\). Then there is a \(k\)-linear symmetric tensor functor \(\Theta\colon\operatorname{Rep}_k(E)\to\mathcal W\), not necessarily exact, with
\[
\Theta(R(T))\cong\Sigma_r(T\bmod I_r)
\]
for tilting modules \(T\), compatibly with the tensor structures.
3. (The functor \(\Phi\) [CF, Theorem 5.2.1, Proposition 3.2.6 and Section 3.3.2].) Let \(\Theta\colon\operatorname{Rep}_k(E)\to\mathcal W\) be a \(k\)-linear symmetric tensor functor that kills \(\operatorname{Ind}_H^Ek\) for every proper subgroup \(H<E\). Let \(E\) act on \(\{1,\dots,q\}\) by a regular action. For every finite symmetric tensor category \(\mathcal C\), the functor \(\Phi\) of Section 4 below is a symmetric tensor functor \(\mathcal C\to\mathcal C\boxtimes\mathcal W\), with tensor structure induced by the \(E\)-equivariant isomorphisms \((X\otimes Y)^{\otimes q}\cong X^{\otimes q}\otimes Y^{\otimes q}\).

By Theorem 4.1 of Lesson 4 the hypothesis of part 2 holds for every \(r\ge1\) and every \(\iota\). In the rest of the course, \(\Theta\) denotes the functor of part 2.

## 3. Projective and induced modules

**Lemma 3.1.**

1. If \(T\) is tilting and \(R(T)\) is not projective, then \(\Theta(R(T))\ne0\).
2. \(\Theta\) kills every projective \(kE\)-module, and \(\Theta(R(\operatorname{St}_{r-1}))\ne0\).
3. \(\Theta(\operatorname{Ind}_H^ED)=0\) for every proper subgroup \(H<E\) and every \(kH\)-module \(D\).

*Proof.* (1) If \(T\) were zero in \(\mathcal T/I_r\), Theorem 2.1(1) would make \(R(T)\) projective. So \(T\bmod I_r\ne0\), and the fully faithful functor \(\Sigma_r\) sends it to a nonzero object, since an object is zero exactly when its identity morphism is. By Theorem 2.1(2), \(\Theta(R(T))\ne0\).

(2) The module \(R(\operatorname{St}_r)\) is projective by Theorem 2.1(1), because \(\operatorname{St}_r\) is zero in \(\mathcal T/I_r\). It has dimension \(p^r=q\) (Lesson 2, (4.1)), so it is free of rank one: \(R(\operatorname{St}_r)\cong kE\). Hence \(\Theta(kE)\cong\Sigma_r(\operatorname{St}_r\bmod I_r)=0\), and \(\Theta\), being additive, kills every projective module, a direct summand of some \((kE)^m\). The module \(S=R(\operatorname{St}_{r-1})\) has dimension \(p^{r-1}<q\), so it is not free, hence not projective, and \(\Theta(S)\ne0\) by (1).

(3) Let \(H\) have rank \(s<r\). If \(s\ge1\), the restriction of \(\iota\) to \(H\) is an injective homomorphism \(E_s\cong H\to U(k)\), and \(\operatorname{St}_{r-1}\) is zero in \(\mathcal T/I_s\) because \(r-1\ge s\); Theorem 2.1(1) at level \(s\) shows that \(\operatorname{Res}^E_HS\) is projective. If \(s=0\), every \(kH\)-module is projective. By the tensor identity, \(S\otimes\operatorname{Ind}_H^ED\cong\operatorname{Ind}_H^E(\operatorname{Res}^E_HS\otimes D)\), which is induced from a projective \(kH\)-module and hence projective. Applying the tensor functor \(\Theta\) and (2) gives \(\Theta(S)\otimes\Theta(\operatorname{Ind}_H^ED)=0\). Since \(\Theta(S)\ne0\), Lemma 1.4 of Lesson 1 gives \(\Theta(\operatorname{Ind}_H^ED)=0\). \(\square\)

For the regular action of \(E\) on \(q\) points, the proper subgroups are exactly the subgroups that do not act transitively. Lemma 3.1(3) is therefore the hypothesis of Theorem 2.1(3).

## 4. The internal extension and the higher Frobenius functor

Let \(\mathcal C\) be a finite symmetric tensor category with projective generator \(P_0\), and \(A=\operatorname{End}(P_0)^{\mathrm{op}}\), so that \(\mathcal C\simeq A\text{-mod}\) (Lemma 1.3 of Lesson 1). An *\(E\)-object* of \(\mathcal C\) is an object \(Z\) with a homomorphism \(E\to\operatorname{Aut}(Z)\); these form the Deligne product \(\mathcal C\boxtimes\operatorname{Rep}_k(E)\), the modules over \(A\otimes kE\). Similarly \(\mathcal C\boxtimes\mathcal W\) is the category of objects of \(\mathcal W\) with an action of \(A\), that is, with an algebra homomorphism \(A\to\operatorname{End}_{\mathcal W}\).

**Definition 4.1.** For an \(E\)-object \(Z\), viewed as a \(kE\)-module with a commuting action of \(A\), let \(\Theta_{\mathcal C}(Z)\) be the object \(\Theta(Z)\) of \(\mathcal W\), with \(a\in A\) acting by \(\Theta(a)\). This defines a functor
\[
\Theta_{\mathcal C}\colon\mathcal C\boxtimes\operatorname{Rep}_k(E)\to\mathcal C\boxtimes\mathcal W .
\]

The elements of \(A\) act on \(Z\) by \(kE\)-module endomorphisms, so \(\Theta(a)\) is defined, and \(a\mapsto\Theta(a)\) is an algebra homomorphism because \(\Theta\) is a \(k\)-linear functor. No exactness of \(\Theta\) is needed. This is the internal extension of \(\Theta\) used by Coulembier and Flake [CF, Example 3.2.4 and Proposition 3.2.6].

**Lemma 4.2.** For every projective object \(Q\) of \(\mathcal C\) and every \(E\)-object \(Z\) there is an isomorphism, natural in \(Z\),
\[
\begin{aligned}
&(\operatorname{Hom}_{\mathcal C}(Q,-)\boxtimes\mathrm{Id}_{\mathcal W})(\Theta_{\mathcal C}(Z))\\
&\quad\cong\Theta(\operatorname{Hom}_{\mathcal C}(Q,Z)).
\end{aligned}
\]
Here \(\operatorname{Hom}_{\mathcal C}(Q,Z)\) is a \(kE\)-module through the action of \(E\) on \(Z\), and \(\operatorname{Hom}_{\mathcal C}(Q,-)\boxtimes\mathrm{Id}_{\mathcal W}\) is the functor \(\mathcal C\boxtimes\mathcal W\to\mathcal W\) induced by the exact functor \(\operatorname{Hom}(Q,-)\).

*Proof.* The \(A\)-module corresponding to \(Q\) is a direct summand of \(A^m\) for some \(m\), cut out by an idempotent \(e\) in \(\operatorname{End}_A(A^m)\), a matrix with entries in \(A\). For an object \(Y\) of \(\mathcal C\boxtimes\mathcal W\), that is, an object of \(\mathcal W\) with an action of \(A\), the object \((\operatorname{Hom}(Q,-)\boxtimes\mathrm{Id})(Y)\) is the image of the idempotent of \(Y^{\oplus m}\) given by the matrix \(e\) acting through \(A\). The same description holds for \(\operatorname{Hom}_{\mathcal C}(Q,Z)\) inside \(Z^{\oplus m}\). An additive functor preserves finite direct sums and images of idempotents, and \(\Theta(a)\) is the action of \(a\) on \(\Theta_{\mathcal C}(Z)\). Applying \(\Theta\) to the description for \(Z\) therefore gives the description for \(\Theta_{\mathcal C}(Z)\), naturally in \(Z\). \(\square\)

Fix a regular action of \(E\) on \(\{1,\dots,q\}\). For an object \(X\) of \(\mathcal C\), the symmetry gives an action of \(E\) on \(X^{\otimes q}\) by permuting the factors.

**Definition 4.3.** The *higher Frobenius functor* is
\[
\Phi\colon\mathcal C\to\mathcal C\boxtimes\mathcal W,\qquad\Phi(X)=\Theta_{\mathcal C}(X^{\otimes q}),
\]
with \(\Phi(f)=\Theta_{\mathcal C}(f^{\otimes q})\) on morphisms.

**Proposition 4.4.**

1. \(\Phi\) is a symmetric tensor functor (Theorem 2.1(3)).
2. \(\Phi\) is additive, and \(\Phi(af)=a^q\Phi(f)\) for \(a\in k\).
3. For projective objects \(Q\) and all \(X\),
\[
\begin{aligned}
&(\operatorname{Hom}(Q,-)\boxtimes\mathrm{Id})(\Phi(X))\\
&\quad\cong\Theta\bigl(\operatorname{Hom}(Q,X^{\otimes q})\bigr).
\end{aligned}
\]

*Proof.* (2) Expand \((X\oplus Y)^{\otimes q}\) as the direct sum, over all colourings \(c\colon\{1,\dots,q\}\to\{X,Y\}\), of the products \(c(1)\otimes\cdots\otimes c(q)\). The group \(E\) permutes these summands through its action on colourings. A colouring that is not constant has a stabilizer \(H\ne E\), because \(E\) acts transitively on the positions. The sum of the summands over the orbit of such a colouring is an \(E\)-object isomorphic to \(\operatorname{Ind}_H^E\) of the summand of the colouring, so \(\Theta_{\mathcal C}\) kills it by Lemma 3.1(3), applied to the underlying \(kE\)-module. The two constant colourings give \(X^{\otimes q}\) and \(Y^{\otimes q}\). Hence \(\Phi(X\oplus Y)\cong\Phi(X)\oplus\Phi(Y)\), and the same expansion applied to morphisms \(f+f'\) shows \(\Phi(f+f')=\Phi(f)+\Phi(f')\). Finally \((af)^{\otimes q}=a^qf^{\otimes q}\) and \(\Theta_{\mathcal C}\) is \(k\)-linear.

(3) Apply Lemma 4.2 to \(Z=X^{\otimes q}\). \(\square\)

So \(\Phi\) is \(\sigma\)-semilinear for the automorphism \(\sigma(a)=a^q\) of \(k\). It need not be exact. In characteristic \(p\) with \(r=1\) and \(\Theta\) replaced by the semisimplification \(\operatorname{Rep}_k(\mathbb Z/p)\to\operatorname{Ver}_p\), the same construction gives the Frobenius functor of Etingof and Ostrik, which is studied in Lesson 8 [CF, Example 5.2.2].

## 5. An exactness criterion

**Proposition 5.1** ([CF, Proposition 5.2.4]; [EO, Proposition 7.6 and Remark 7.7(i)]). If there are projective objects \(P,Q\) of \(\mathcal C\) with
\[
\Theta\bigl(\operatorname{Hom}_{\mathcal C}(Q,P^{\otimes q})\bigr)\ne0,
\]
then \(\Phi\) is exact.

*Proof.* By Proposition 4.4(3), \(\Phi(P)\ne0\). Let \(0\to X'\xrightarrow{f}X\xrightarrow{g}X''\to0\) be exact. Tensoring with \(P\) gives an exact sequence of projective objects, because the tensor product of a projective object with any object is projective [EGNO, Proposition 4.2.12]; it splits because \(X''\otimes P\) is projective. The additive functor \(\Phi\) carries a split exact sequence to a split exact sequence, and its tensor structure identifies \(\Phi(Y\otimes P)\) with \(\Phi(Y)\otimes\Phi(P)\), naturally in \(Y\). So
\[
\begin{gathered}
0\to\Phi(X')\otimes\Phi(P)\to\Phi(X)\otimes\Phi(P)\\
\to\Phi(X'')\otimes\Phi(P)\to0
\end{gathered}
\]
is exact. The sequence \(0\to\Phi(X')\to\Phi(X)\to\Phi(X'')\to0\) has zero composites, because \(\Phi(g)\Phi(f)=\Phi(gf)=0\). The category \(\mathcal C\boxtimes\mathcal W\) is a finite symmetric tensor category (Theorem 2.1 of Lesson 1), so tensoring with the nonzero object \(\Phi(P)\) reflects exactness at each term by Lemma 1.4 of Lesson 1. \(\square\)

Lessons 6 and 7 choose \(r\) and \(\iota\) so that the hypothesis holds with \(Q=P\) a projective generator.

## 6. Exercises

**6.1.** Prove the tensor identity of Section 1: check that the displayed map is well defined, \(E\)-equivariant and bijective.

**6.2.** Let \(r=1\), so that \(E=\mathbb Z/p\) acts on \(p\) positions by cyclic shifts. Show that every non-constant colouring of the positions by \(\{X,Y\}\) has trivial stabilizer, and count the orbits of colourings with exactly \(j\) entries equal to \(Y\).

**6.3.** Let \(\mathcal C\) be a finite symmetric tensor category, \(P\) projective and \(0\to X'\to X\to X''\to0\) exact. Show directly from the definition of projectivity that \(0\to X'\otimes P\to X\otimes P\to X''\otimes P\to0\) splits, given that \(X''\otimes P\) is projective.

**6.4.** Show that \(\Phi(\mathbf 1)\) is the unit object of \(\mathcal C\boxtimes\mathcal W\), using that \(\mathbf 1^{\otimes q}=\mathbf 1\) with the trivial action of \(E\).

## 7. Solutions

**6.1.** The map \(m\otimes(g\otimes d)\mapsto g\otimes(g^{-1}m\otimes d)\) respects the relation \(gh\otimes d=g\otimes hd\) for \(h\in H\): the image of \(m\otimes(gh\otimes d)\) is \(gh\otimes(h^{-1}g^{-1}m\otimes d)\)\(=g\otimes h(h^{-1}g^{-1}m\otimes d)\)\(=g\otimes(g^{-1}m\otimes hd)\), the image of \(m\otimes(g\otimes hd)\). For \(g'\in E\), the element \(g'm\otimes(g'g\otimes d)\) maps to \(g'g\otimes(g^{-1}m\otimes d)\), which is \(g'\) applied to the image of \(m\otimes(g\otimes d)\). The map \(g\otimes(m'\otimes d)\mapsto gm'\otimes(g\otimes d)\) is a well-defined inverse, by the same computation.

**6.2.** The stabilizer of a colouring is a subgroup of \(\mathbb Z/p\), hence trivial or everything. If it is everything, the colouring is constant on the single orbit of positions. So a non-constant colouring has trivial stabilizer and an orbit of size \(p\). For \(1\le j\le p-1\) there are \(\binom pj\) colourings with \(j\) entries \(Y\), forming \(\binom pj/p\) orbits; this is an integer since \(p\) divides \(\binom pj\).

**6.3.** Since \(X''\otimes P\) is projective, the identity of \(X''\otimes P\) lifts along the epimorphism \(X\otimes P\to X''\otimes P\), giving a section. A short exact sequence whose epimorphism has a section splits.

**6.4.** The \(q\)-th tensor power of \(\mathbf 1\) is \(\mathbf 1\), and the permutations act on it by the identity, because the symmetry \(c_{\mathbf 1,\mathbf 1}\) is the identity. So \(\mathbf 1^{\otimes q}\) is the unit object \(\mathbf 1\boxtimes k\) of \(\mathcal C\boxtimes\operatorname{Rep}_k(E)\), with \(A\) acting on \(\operatorname{Hom}(P_0,\mathbf 1)\). Then \(\Phi(\mathbf 1)=\Theta_{\mathcal C}(\mathbf 1\boxtimes k)=\mathbf 1\boxtimes\Theta(k)\), and \(\Theta(k)\cong\mathbf 1\) because \(\Theta\) is a tensor functor.

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 4 (Lemmas 4.1 and 4.2, the tensor-power construction and Proposition 4.3). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [CF] K. Coulembier and J. Flake, *Towards higher Frobenius functors for symmetric tensor categories*, Selecta Math. 32 (2026), numbering of arXiv:2405.19506v2: Example 3.2.4, Proposition 3.2.6, Section 3.3.2, Definition 5.1.1, Theorem 5.2.1, Example 5.2.2, Proposition 5.2.4, Theorem 5.3.5, Conjecture 5.4.2 and Theorem 5.4.3. https://arxiv.org/abs/2405.19506v2
- [EO] P. Etingof and V. Ostrik, *On the Frobenius functor for symmetric tensor categories in positive characteristic*, numbering of arXiv:1912.12947v2, Proposition 7.6 and Remark 7.7(i). https://arxiv.org/abs/1912.12947v2
- [EGNO] P. Etingof, S. Gelaki, D. Nikshych and V. Ostrik, *Tensor categories*, authors' final version, Proposition 4.2.12. https://math.mit.edu/~etingof/egnobookfinal.pdf

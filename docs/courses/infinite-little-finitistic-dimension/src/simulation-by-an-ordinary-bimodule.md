# Simulation by an ordinary bimodule

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The realization theorem of [A bimodule complex that realizes selection](a-bimodule-complex-that-realizes-selection.md) gives a bounded *complex* \(P\) of \(B\)-bimodules. A trivial extension needs an ordinary bimodule. This lesson spreads the terms of \(P\) along a chain of vertices, so that the differential of \(P\) becomes the action of arrows: the result is a bimodule \(X\) over a product algebra \(D\) of finite global dimension whose second derived tensor power, applied to \(B\)-modules, is \(P\otimes^{\mathbf L}_B-\) up to a fixed shift (Proposition 3.1). The construction follows [OpenAI-FD, Section 5].

Throughout, \(k\) is a field, \(B\) and \(P\) are as in the previous lessons, and tensor products without subscript are over \(k\).

## 1. A chain of vertices

Choose integers \(a_*\le0\le b_*\) with \(P^n=0\) for \(n\notin[a_*,b_*]\), and let \(l=b_*-a_*\). Let \(C\) be the path algebra of the quiver
\[
0\xrightarrow{c_1}1\xrightarrow{c_2}\cdots\xrightarrow{c_l}l
\]
modulo all paths of length two, with vertex idempotents \(\varepsilon_0,\dots,\varepsilon_l\). With the path conventions of [Directed algebras and quadratic presentations](directed-algebras-and-quadratic-presentations.md), \(c_i\in\varepsilon_iC\varepsilon_{i-1}\). The right module \(\varepsilon_iC\), spanned by the paths ending at \(i\), has basis \(\varepsilon_i,c_i\) for \(i\ge1\), and \(\varepsilon_0C=k\varepsilon_0\). Let \(W\) be the simple right \(C\)-module at vertex \(l\), the quotient of \(\varepsilon_lC\) by \(c_lC\).

**Lemma 1.1.** The sequence of right \(C\)-modules
\[
\begin{gathered}
0\to\varepsilon_0C\xrightarrow{c_1\cdot}\varepsilon_1C\xrightarrow{c_2\cdot}\cdots\\
\cdots\xrightarrow{c_l\cdot}\varepsilon_lC\to W\to0
\end{gathered}
\]
is exact; it is a projective resolution of \(W\).

**Proof.** Left multiplication by \(c_i\) sends \(\varepsilon_{i-1}\) to \(c_i\) and, for \(i\ge2\), sends \(c_{i-1}\) to \(c_ic_{i-1}=0\). So its image is \(kc_i\), the kernel of the next map (which kills \(c_i\) and is injective on \(k\varepsilon_i\)), and its kernel is \(kc_{i-1}\), the image of the previous map. The first map is injective, and the last map has kernel \(kc_l\). For \(l=0\) the resolution is the isomorphism \(\varepsilon_0C\to W\). \(\square\)

## 2. The algebra D and the bimodule X

The algebra \(B\otimes C\) acts on a vector space when \(B\) and \(C\) act by commuting operators. Define a \((B\otimes C,B)\)-bimodule \(O\) by
\[
\begin{gathered}
\varepsilon_iO=P^{a_*+i}\quad(0\le i\le l),\\
c_i\big|_{\varepsilon_{i-1}O}=d_P^{a_*+i-1},
\end{gathered}
\]
with both \(B\)-actions those of the terms of \(P\). The relations of \(C\) hold since \(d_P^2=0\), and the action of \(C\) commutes with both \(B\)-actions because \(d_P\) is a map of bimodules. Let
\[
\begin{gathered}
D=B\times(B\otimes C),\\
T=B\otimes W,\qquad X=O\oplus T .
\end{gathered}
\]
The bimodule \(O\) is given the left action of the second factor of \(D\) and the right action of the first; \(T\) is given the left action of the first factor (by left multiplication on \(B\)) and the right action of the second (by right multiplication on \(B\) and the action on \(W\)). The other factor acts by zero in each case. So \(X\) is a finite-dimensional \(D\)-bimodule.

A left \(D\)-module is a pair of a left \(B\)-module and a left \(B\otimes C\)-module, and similarly for complexes; a complex of left \(B\)-modules is *on the first factor* when the second factor acts by zero.

## 3. Two steps of the tensor functor

**Proposition 3.1** (OpenAI). (a) The algebra \(D\) has finite global dimension, at most \(3l+2\), for left and for right modules.

(b) Let \(F=X\otimes^{\mathbf L}_D-\) on the derived category of left \(D\)-modules. There is an isomorphism of complexes of \(B\)-bimodules
\[
T\otimes^{\mathbf L}_{B\otimes C}O\simeq P[b_*],
\]
and for every complex \(Z\) of left \(B\)-modules on the first factor, \(F(Z)=O\otimes_BZ\) lies on the second factor and
\[
F^2(Z)\simeq P[b_*]\otimes^{\mathbf L}_BZ,
\]
on the first factor.

**Proof.** (a) The algebra \(B\otimes C\) has the complete orthogonal idempotents \(\mathbf e_i\otimes\varepsilon_j\), with \(0\le i\le2\) and \(0\le j\le l\). The corner \((\mathbf e_i\otimes\varepsilon_j)(B\otimes C)(\mathbf e_i\otimes\varepsilon_j)\), which is \(\mathbf e_iB\mathbf e_i\otimes\varepsilon_jC\varepsilon_j\), is one-dimensional, and \((\mathbf e_{i'}\otimes\varepsilon_{j'})(B\otimes C)(\mathbf e_i\otimes\varepsilon_j)\), which is \(\mathbf e_{i'}B\mathbf e_i\otimes\varepsilon_{j'}C\varepsilon_j\), vanishes unless \(i\le i'\) and \(j\le j'\). List the pairs \((i,j)\) in an order extending this product order, for instance by increasing \(i+j\). Then \(B\otimes C\) is directed with respect to \(3(l+1)\) idempotents, and Proposition 2.2 of [Directed algebras and quadratic presentations](directed-algebras-and-quadratic-presentations.md) bounds its global dimension on both sides by \(3(l+1)-1=3l+2\); the same proposition gives \(2\) for \(B\). A module over the product \(D\) is a pair of modules over the factors, projective exactly when both components are; so the global dimension of \(D\) is the larger of the two.

(b) *A resolution of \(X\).* Tensoring the resolution of Lemma 1.1 with \(B\) over \(k\), and placing \(B\otimes\varepsilon_lC\) in degree \(0\), gives a bounded complex \(Q_T\) of \((B,B\otimes C)\)-bimodules with \(Q_T^n=B\otimes\varepsilon_{l+n}C\) for \(-l\le n\le0\), and a quasi-isomorphism \(Q_T\to T\), since \(B\otimes-\) is exact over a field. Each \(B\otimes\varepsilon_iC=(1\otimes\varepsilon_i)(B\otimes C)\) is a direct summand of the right regular module, hence projective. The bimodule \(O\) is projective as a right \(B\)-module, being a finite direct sum of terms of \(P\). Hence \(Q_X=O\oplus Q_T\), with the actions of the factors of \(D\) as for \(X\), is a bounded complex of \(D\)-bimodules, projective as right \(D\)-modules (a projective right module over one factor is a direct summand of a free right \(D\)-module), with a quasi-isomorphism \(Q_X\to X\). Bounded complexes of flat right modules are K-flat, so \(F\) and the other derived tensor products below are computed by ordinary tensor products with these complexes (core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, *Methods of Algebra*, Volume 2, Propositions 4.12.4 and 4.12.9](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)).

*The two steps.* Let \(Z\) be on the first factor. The right action on \(Q_T\) is through the second factor, so \(Q_T\otimes_DZ=0\), and \(F(Z)=O\otimes_DZ=O\otimes_BZ\), on which the second factor acts from the left. Applying \(F\) once more, \(O\otimes_D F(Z)=0\) for the same reason, and
\[
\begin{aligned}
F^2(Z)&\simeq Q_T\otimes_{B\otimes C}(O\otimes_BZ)\\
&\cong(Q_T\otimes_{B\otimes C}O)\otimes_BZ,
\end{aligned}
\]
by associativity of tensor products of bimodule complexes ([Li, Volume 2, Proposition 4.12.13](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). The left \(B\)-action comes from \(Q_T\), so \(F^2(Z)\) is on the first factor.

*The complex \(Q_T\otimes_{B\otimes C}O\).* In degree \(n\), with \(-l\le n\le0\),
\[
\begin{aligned}
&\bigl(B\otimes\varepsilon_{l+n}C\bigr)\otimes_{B\otimes C}O\\
&\quad\cong(1\otimes\varepsilon_{l+n})O=\varepsilon_{l+n}O\\
&\quad=P^{a_*+l+n}=P^{b_*+n},
\end{aligned}
\]
an isomorphism of \(B\)-bimodules. The differential of \(Q_T\) is left multiplication by \(1\otimes c_{l+n+1}\), which becomes the action of \(c_{l+n+1}\) on \(O\), that is \(d_P\). So \(Q_T\otimes_{B\otimes C}O\) is the complex with terms \(P^{b_*+n}\) and differential \(d_P\). The shifted complex \(P[b_*]\) has the same terms and differential \((-1)^{b_*}d_P\). Multiplication by \((-1)^{b_*n}\) in degree \(n\) is an isomorphism of complexes of bimodules between them, since \((-1)^{b_*(n+1)}d_P=(-1)^{b_*}d_P(-1)^{b_*n}\). This proves the first isomorphism, as \(Q_T\to T\) is a K-flat resolution. The terms of \(P[b_*]\) are projective right \(B\)-modules, so \((Q_T\otimes_{B\otimes C}O)\otimes_BZ\cong P[b_*]\otimes_BZ\), and this is \(P[b_*]\otimes^{\mathbf L}_BZ\). \(\square\)

The odd powers of \(F\) carry a complex to the second factor, and the even powers bring it back; on the first factor, two steps of \(F\) are one step of \(P\otimes^{\mathbf L}_B-\), shifted by \(b_*\).

**Corollary 3.2.** For every finite-dimensional left \(R\)-module \(Y\), regarding \(M(Y)\) as a module on the first factor of \(D\), and every \(j\ge0\),
\[
\begin{aligned}
&F^{2j}M(Y)\\
&\quad\simeq\bigoplus_{q=0}^j\bigl(M(H^{\circ j}(Y))[jb_*+3q]\bigr)^{\oplus\binom jq}.
\end{aligned}
\]
**Proof.** By Proposition 3.1 and Theorem 3.1 of [A bimodule complex that realizes selection](a-bimodule-complex-that-realizes-selection.md), \(F^2M(Y')\) is isomorphic to \(M(H(Y'))[b_*]\oplus M(H(Y'))[b_*+3]\) for every finite-dimensional \(Y'\). Induction on \(j\), as in Corollary 3.2 of that lesson, using that \(F^2\) preserves finite direct sums and shifts, gives the formula. \(\square\)

## 4. Exercises

**Exercise 4.1** (easy). Compute \(\dim C\) and the dimensions of the right projective modules \(\varepsilon_iC\).

**Exercise 4.2** (easy). Describe \(O\), \(T\) and \(D\) when \(P\) is concentrated in degree \(0\), so that \(l=0\).

**Exercise 4.3** (medium). Let \(Z'\) be a complex of left \(B\otimes C\)-modules, regarded on the second factor of \(D\). Show that \(F(Z')\simeq T\otimes^{\mathbf L}_{B\otimes C}Z'\), on the first factor.

**Exercise 4.4** (medium). Show that the global dimension of a product \(\Lambda_1\times\Lambda_2\) of finite-dimensional algebras is the larger of the two global dimensions.

## 5. Solutions

**4.1.** The basis of \(C\) consists of the \(l+1\) vertex idempotents and the \(l\) arrows, so \(\dim C=2l+1\). The module \(\varepsilon_0C\) has dimension \(1\), and \(\varepsilon_iC\) has dimension \(2\) for \(i\ge1\).

**4.2.** For \(l=0\), \(C=k\), \(W=k\), \(B\otimes C=B\), \(O=P^0\) with both actions of \(B\), and \(T=B\). So \(D=B\times B\) and \(X=P^0\oplus B\), with \(P^0\) going from the first factor to the second and \(B\) from the second to the first. Proposition 3.1 says \(F^2(Z)\simeq P^0\otimes_BZ\).

**4.3.** The complex \(Q_X\) computes \(F\). The right action on \(O\) is through the first factor, so \(O\otimes_DZ'=0\), and \(F(Z')\simeq Q_T\otimes_{B\otimes C}Z'\), on which the first factor acts from the left. Since \(Q_T\to T\) is a K-flat resolution of right \(B\otimes C\)-modules, this is \(T\otimes^{\mathbf L}_{B\otimes C}Z'\).

**4.4.** Let \(\epsilon_1,\epsilon_2\) be the central idempotents of the factors. Every module \(M\) over \(\Lambda=\Lambda_1\times\Lambda_2\) is \(\epsilon_1M\oplus\epsilon_2M\), a module over \(\Lambda_1\) plus one over \(\Lambda_2\), and
\[
\begin{aligned}
\operatorname{Hom}_\Lambda(M,N)={}&\operatorname{Hom}_{\Lambda_1}(\epsilon_1M,\epsilon_1N)\\
&\times\operatorname{Hom}_{\Lambda_2}(\epsilon_2M,\epsilon_2N).
\end{aligned}
\]
Hence \(M\) is projective exactly when both components are, a projective resolution of \(M\) is a pair of resolutions of the components, and \(\operatorname{pd}_\Lambda M=\max(\operatorname{pd}\epsilon_1M,\operatorname{pd}\epsilon_2M)\). Taking suprema gives the claim.

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [Li] W.-W. Li, *Methods of Algebra*, Volume 2, English edition. https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en

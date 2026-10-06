# Amenability and the equality of full and reduced crossed products

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The full norm tests every covariant representation. The reduced norm tests a regular model. Almost invariant vectors provide a way to compare these tests: after tensoring a covariant representation with the left regular representation, compression to those vectors recovers its original integrated operators in norm.

Throughout, \(G\) is a locally compact Hausdorff group with left Haar measure, and \(\alpha:G\to\operatorname{Aut}(A)\) is strongly continuous. Neither \(A\) nor \(G\) is assumed separable; \(A\) may be nonunital. The left regular representation is

\[
(\lambda_s\xi)(t)=\xi(s^{-1}t).
\tag{1}
\]

We use the construction and absorption theorem of [Lesson 2](KT-CP-02.md), and write
\(q:A\rtimes_\alpha G\to A\rtimes_{\alpha,r}G\) for the canonical quotient. All assertions of equality below refer to this map.

## Almost invariant unit vectors

**Definition 4.1.** The \(L^2\) Reiter condition is the existence of a net \((\xi_i)\) of unit vectors in \(L^2(G)\) such that

\[
\sup_{s\in K}\|\lambda_s\xi_i-\xi_i\|_2\longrightarrow0
\quad\text{for every compact }K\subseteq G.
\tag{2}
\]

This is our working definition of amenability. A net accommodates arbitrary locally compact groups. A sequence suffices for a group with a countable compact exhaustion.

We will prove that existence of a left invariant mean on \(L^\infty(G)\) is equivalent to the following normalized \(L^1\) condition. For every compact \(K\) and \(\varepsilon>0\), there is \(p\in C_c(G)\), \(p\geq0\), \(\int p=1\), with

\[
\sup_{s\in K}\|\lambda_s p-p\|_1<\varepsilon.
\tag{3}
\]

The equivalence is the classical Reiter theorem, also recorded in Williams, Appendix A, Proposition A.16(a),(d). The mean-to-probability argument is supplied below, including the compact-uniform smoothing step.

Here is the passage from probabilities to vectors. For \(a,b\geq0\),
\(|\sqrt a-\sqrt b|^2\leq |a-b|\). Consequently, \(\xi=\sqrt p\) has norm one and

\[
\|\lambda_s\xi-\xi\|_2^2\leq\|\lambda_s p-p\|_1.
\tag{4}
\]

Conversely, if \(\|\xi\|_2=1\), set \(p=|\xi|^2\). Cauchy–Schwarz gives

\[
\|\lambda_s p-p\|_1
\leq\bigl(\|\lambda_s\xi\|_2+\|\xi\|_2\bigr)
       \|\lambda_s\xi-\xi\|_2
=2\|\lambda_s\xi-\xi\|_2.
\tag{5}
\]

Condition (2) therefore supplies almost invariant \(L^1\) probabilities. To see directly that they give an invariant mean, regard integration against \(p_i\) as a state on \(L^\infty(G)\), take a weak-* cluster point in its compact state space, and use
\[
\left|\int f(s^{-1}t)p_i(t)\,dt-\int f(t)p_i(t)\,dt\right|
\leq\|f\|_\infty\|\lambda_{s^{-1}}p_i-p_i\|_1.
\]
Thus (3), (4), and this argument establish agreement of our definition with the invariant-mean definition. Probability normalization is essential.

## From invariant means to almost invariant probabilities

We now prove the harmonic-analysis implication needed to pass from the invariant-mean definition to (3). This also supplies a useful form of the extension argument below. Write \(\mathrm{LUC}(G)\) for the bounded functions \(a\) such that \(s\mapsto\lambda_s a\) is continuous in the supremum norm, where \((\lambda_s a)(t)=a(s^{-1}t)\). These functions are continuous. A left invariant mean is a positive linear functional of value one on the constant function one, unchanged by every \(\lambda_s\).

For arbitrary locally compact groups, \(L^\infty(G)\) here uses locally Haar-measurable functions modulo locally null sets. This is the convention compatible with the Haar-integral completion of \(C_c(G)\). In particular, \(L^1(G)^*=L^\infty(G)\). One can obtain this dual description without assuming global sigma-finiteness: choose an open sigma-compact subgroup, decompose \(G\) into its open cosets, apply the usual sigma-finite dual description on each coset, and take the bounded family of the resulting densities. An \(L^1\) function has at most countably many nonzero coset components. All convolution integrals below therefore reduce to sigma-compact supports; no countable exhaustion of the whole group is used.

**Lemma (averaging an invariant mean).** A left invariant mean on \(\mathrm{LUC}(G)\) gives a left invariant mean \(M\) on \(L^\infty(G)\) satisfying
\[
M(A_h a)=\left(\int_Gh\right)M(a),\qquad
(A_h a)(t)=\int_Gh(r)a(rt)\,dr,
\quad h\in L^1(G).
\tag{4A.1}
\]

**Proof.** Put \((R_s h)(r)=\Delta(s)^{-1}h(rs^{-1})\). Right translation preserves the integral and the \(L^1\) norm in this normalization. Direct change of variable gives
\[
\lambda_{s^{-1}}A_h a=A_{R_s h}a.
\tag{4A.2}
\]
Norm continuity of right translation on \(L^1\), and the bound \(\|A_h a\|_\infty\leq\|h\|_1\|a\|_\infty\), show that \(A_h a\) belongs to \(\mathrm{LUC}(G)\). The averaging does not depend on a locally null change in \(a\): every fixed right translate preserves locally Haar-null sets.

Let \(m\) be the given mean and fix \(a\). The bounded functional \(T_a(h)=m(A_h a)\) is invariant under all normalized right translations, by (4A.2). The convolution identity
\[
h*k=\int_G k(s)R_s h\,ds
\tag{4A.3}
\]
is an identity in \(L^1(G)\); first verify it on compact supports, then use density and the \(L^1\) convolution bound. Hence \(T_a(h*k)=T_a(h)\int k\). Choose an integral-one positive approximate identity \(e_j\in C_c(G)\) and a fixed positive \(h_0\in C_c(G)\) of integral one. Since \(e_j*h_0\to h_0\), we have \(T_a(e_j)\to T_a(h_0)\). Applying the same identity to \(e_j*h\to h\) proves
\(T_a(h)=T_a(h_0)\int h\) for every \(h\).

Define \(M(a)=m(A_{h_0}a)\). This is positive and normalized. Moreover
\(A_h(\lambda_s a)=A_{\lambda_{s^{-1}}h}a\), whose coefficient integral is unchanged. The formula just proved makes \(M(\lambda_s a)=M(a)\). Finally, compact-support Fubini gives \(A_kA_h a=A_{h*k}a\), with extension to \(L^1\) coefficients by the norm bound. Taking \(k=h_0\) proves (4A.1). ∎

**Theorem (the Reiter implication).** If \(G\) has a left invariant mean on \(L^\infty(G)\), or already on \(\mathrm{LUC}(G)\), then for every compact \(K\subset G\) and \(\varepsilon>0\) there is a nonnegative \(q\in C_c(G)\) of integral one with
\[
\sup_{s\in K}\|\lambda_s q-q\|_1<\varepsilon.
\tag{4A.4}
\]

**Proof.** In the first case restrict the mean to \(\mathrm{LUC}(G)\); in either case apply the lemma to obtain \(M\). Fix a nonnegative \(h\in C_c(G)\) of integral one. For a finite set \(F\subset G\), consider the convex set
\[
\mathcal C_F=\left\{\big((\lambda_s h-h)*p\big)_{s\in F}:
           p\geq0,\ p\in L^1(G),\ \int p=1\right\}
\subset\bigoplus_{s\in F} L^1(G).
\tag{4A.5}
\]
We claim that zero belongs to its norm closure. Otherwise real Hahn–Banach separation gives real \(a_s\in L^\infty(G)\) and \(c>0\) such that
\[
\sum_{s\in F}\int_G a_s(t)((\lambda_s h-h)*p)(t)\,dt\geq c
\tag{4A.6}
\]
for every such probability \(p\). Fubini changes the left side to the integral against \(p\) of
\(b=\sum_{s\in F}A_{\lambda_s h-h}a_s\).
This is a bounded left uniformly continuous function. Testing all positive \(L^1\) probabilities makes \(b\geq c\) locally almost everywhere. Continuity and full support of Haar measure then make the inequality hold everywhere. Positivity gives \(M(b)\geq c\). But (4A.1) gives \(M(b)=0\), since every \(\lambda_s h-h\) has integral zero. This contradiction proves the claim.

The family \(s\mapsto\lambda_s(h*p)\), for all the probabilities \(p\), is uniformly equicontinuous in the following precise sense:
\[
\|\lambda_s(h*p)-\lambda_t(h*p)\|_1
\leq\|\lambda_s h-\lambda_t h\|_1.
\tag{4A.7}
\]
Continuity of \(s\mapsto\lambda_s h\), and compactness of \(K\), give finitely many points \(F\subset K\) such that each \(s\in K\) is within \(\varepsilon/4\) of one of them in the right side of (4A.7). Use the closure assertion to choose \(p\) whose discrepancies at these points are all below \(\varepsilon/4\). Thus \(h*p\) has discrepancy below \(\varepsilon/2\) everywhere on \(K\).

Approximate \(p\) in \(L^1\) by a nonnegative compactly supported continuous probability \(p'\), within \(\varepsilon/4\). Positive approximation followed by integral normalization supplies this: normalization tends to one because \(\int p=1\). The function \(q=h*p'\) is continuous with compact support, nonnegative, and of integral one. Each translation discrepancy changes by at most \(2\|h*(p-p')\|_1<\varepsilon/2\). This proves (4A.4). ∎

Together with (4)–(5) and the weak-* limit argument above, this proves the equivalence of the invariant-mean, normalized \(L^1\) and \(L^2\) definitions in the full locally compact generality used here. The smoothing and the finite cover of \(K\) are the steps that turn pointwise invariance tests into uniform control on compact sets.

## Abelian groups and closed normal extensions

**Proposition (abelian amenability).** Every locally compact Hausdorff abelian group satisfies (2).

**Proof.** Use the written programme Plancherel theorem, *The Plancherel theorem*, Theorem 1.1 and Proposition 2.1, and the compact-convergence character topology in *Characters and the dual group*, Theorem 5.2. Given compact \(K\subset G\) and \(\varepsilon>0\), choose a neighborhood \(V\) of the identity in \(\widehat G\) such that \(|\chi(s)-1|<\varepsilon\) for \(s\in K,\chi\in V\). Choose a nonzero \(b\in C_c(\widehat G)\) supported in \(V\) and normalize it in \(L^2\). Haar full support ensures its norm is positive. Let \(\xi=\mathcal F_+^{-1}b\), where the positive transform is the programme's negative transform composed with dual inversion. Plancherel gives \(\|\xi\|_2=1\), and Fourier transformation of a left translate gives
\[
\|\lambda_s\xi-\xi\|_2^2
=\int_{\widehat G}|\chi(s)-1|^2|b(\chi)|^2\,d\chi
<\varepsilon^2\qquad(s\in K).
\tag{4A.8}
\]
Indexing these choices by compact sets and positive errors gives the required net. No structure theorem, separability or sigma-finite Haar measure is needed. ∎

**Proposition (extension of amenable groups).** If \(H\) is a closed normal subgroup of \(G\), and \(H\) and \(Q=G/H\) are amenable, then \(G\) is amenable.

**Proof.** Take invariant means \(m_H,m_Q\) on their left uniformly continuous functions, obtained from the definitions already proved. For \(a\in\mathrm{LUC}(G)\), set
\[
\Phi_a(gH)=m_H\big(h\longmapsto a(gh)\big).
\tag{4A.9}
\]
The function of \(h\) is in \(\mathrm{LUC}(H)\): its left translation by \(k\) changes its argument by the left multiplier \(gkg^{-1}\), which tends to the identity as \(k\to e\). Replacing \(g\) by \(gk\), for \(k\in H\), leaves the mean unchanged by left invariance. Thus (4A.9) is well defined on the quotient.

For \(u\in G\), its change from \(gH\) to \(ugH\) is bounded uniformly in \(g\) by \(\sup_t|a(ut)-a(t)|\). The quotient map is open, so an identity neighborhood in \(Q\) lifts to an identity neighborhood in \(G\). This bound proves that \(\Phi_a\) is left uniformly continuous on \(Q\). Therefore \(m_G(a)=m_Q(\Phi_a)\) is a positive normalized functional. The equality \(\Phi_{\lambda_u a}(gH)=\Phi_a(u^{-1}gH)\) makes it left invariant. The averaging lemma and Reiter implication then give (2) for \(G\). Closedness and normality are used exactly to make \(Q\) a locally compact Hausdorff group and its quotient translation legitimate. ∎

## Compression proves the norm equality

**Theorem 4.2.** If \(G\) satisfies (2), then \(q\) is an isomorphism for every \(C^*\)-dynamical system \((A,G,\alpha)\).

**Proof.** Take a nondegenerate covariant pair \((\pi,U)\) on \(H\). On \(H\otimes L^2(G)\), the pair

\[
(\pi\otimes1,\ U\otimes\lambda)
\tag{6}
\]

is covariant for the same action. Fell absorption, proved in Lesson 2, makes its integrated representation unitarily equivalent to the regular representation induced by \(\pi\). The coefficient representation \(\pi\) need not be faithful: the regular-norm domination proved there still gives

\[
\left\|\int_G \pi(f(s))U_s\otimes\lambda_s\,ds\right\|
\leq\|f\|_r
\qquad(f\in C_c(G,A)).
\tag{7}
\]

Define an isometry \(J_i:H\to H\otimes L^2(G)\) by \(J_i v=v\otimes\xi_i\), and set
\(\varphi_i(s)=\langle\xi_i,\lambda_s\xi_i\rangle\), with inner products linear in the second variable. Compression of (7) is

\[
J_i^*\left(\int_G\pi(f(s))U_s\otimes\lambda_s\,ds\right)J_i
=\int_G\varphi_i(s)\pi(f(s))U_s\,ds.
\tag{8}
\]

The equality follows first on matrix coefficients and then on the operator, since the integrand is strongly continuous and bounded by the integrable function \(\|f(s)\|\). Furthermore,
\[
|\varphi_i(s)-1|
\leq\|\lambda_s\xi_i-\xi_i\|_2.
\]
With \(K=\operatorname{supp}f\), (2) implies

\[
\left\|\int_G(\varphi_i(s)-1)\pi(f(s))U_s\,ds\right\|
\leq\|f\|_1\sup_{s\in K}|\varphi_i(s)-1|
\longrightarrow0.
\tag{9}
\]

Since compression by an isometry is contractive, (7)–(9) yield
\(\|(\pi\rtimes U)(f)\|\leq\|f\|_r\). Taking the supremum over covariant pairs gives \(\|f\|_u\leq\|f\|_r\). The reverse inequality holds by the definition of the full norm. The norms coincide on \(C_c(G,A)\), so their completions and canonical quotient coincide. The zero coefficient algebra causes no exception to this implication. \(\square\)

This also explains the phrase *weak containment* in the theorem's usual formulation. The trivial representation is approximated by the regular matrix coefficients \(\varphi_i\), uniformly on compact sets; (8)–(9) give the corresponding norm comparison after tensoring any covariant pair. We proved the needed comparison explicitly.

No right translation was used. Left Haar measure makes (1) unitary even when the modular function is nontrivial. No passage from a net to a sequence, or choice of a faithful \(\pi\) for each covariant pair, enters the proof.

## Explicit examples of the condition

For \(\mathbb Z^d\), with counting measure, let \(Q_N=\{-N,\ldots,N\}^d\) and
\(\xi_N=|Q_N|^{-1/2}1_{Q_N}\). For \(s=(s_1,\ldots,s_d)\),

\[
\|\lambda_s\xi_N-\xi_N\|_2^2
=2\left(1-\frac{|Q_N\cap(s+Q_N)|}{|Q_N|}\right),
\quad
\frac{|Q_N\cap(s+Q_N)|}{|Q_N|}
=\prod_{j=1}^d\max\left(0,1-\frac{|s_j|}{2N+1}\right).
\tag{10}
\]

The product tends to one uniformly on finite sets, which are precisely the compact sets here.

For \(\mathbb R^d\), with Lebesgue measure, use
\(\xi_L=(2L)^{-d/2}1_{[-L,L]^d}\). The same intersection calculation gives

\[
\|\lambda_s\xi_L-\xi_L\|_2^2
=2\left(1-\prod_{j=1}^d
\max\left(0,1-\frac{|s_j|}{2L}\right)\right).
\tag{11}
\]

On a compact set of translations, all coordinates are bounded, so convergence is uniform. Indicator functions belong to \(L^2\); the definition does not require smoothness.

If \(G\) is compact, its Haar measure has finite mass \(m\), and
\(\xi=m^{-1/2}1_G\) is an exactly invariant unit vector. This covers finite groups and tori, with any chosen Haar normalization.

For a countably infinite discrete abelian group \(\Gamma\), enumerate its elements \(g_1,g_2,\ldots\). Push the uniform probability on \(\{-m,\ldots,m\}^m\) forward under
\[
(k_1,\ldots,k_m)\longmapsto g_1^{k_1}\cdots g_m^{k_m}
\]
to obtain a finitely supported probability \(p_m\) on \(\Gamma\). Relations and torsion merely identify image points; they do not destroy normalization. For \(j\leq m\), translation by \(g_j\) is the pushforward of translation by the \(j\)-th coordinate vector. Pushforward decreases the \(L^1\) distance between probabilities, and the two cubes differ only along their two boundary faces. Hence

\[
\|\lambda_{g_j}p_m-p_m\|_1\leq\frac{2}{2m+1}.
\tag{12}
\]

Taking \(\xi_m=\sqrt{p_m}\) and using (4) proves (2), uniformly on each finite subset. For a finite abelian group the constant vector already does the job.

The abelian and extension propositions above establish (2) for every locally compact abelian group and every closed normal extension of amenable groups. Williams, Remark A.15, records the same permanence results. In the abelian proof the Fourier input is the written programme lesson [*The Plancherel theorem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-08.html), Theorem 1.1 and Proposition 2.1; the dual neighborhood is supplied by [*Characters and the dual group*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-02.html), Theorem 5.2. These analytic proofs do not depend on the crossed-product duality result of Lesson 6.

It follows that crossed products by \(\mathbb Z^d,\mathbb R^d,\mathbb T^d\), compact groups, and amenable extensions have a single canonical completion. In particular the full rotation algebras in Lesson 3 inherit the simplicity and trace conclusions proved there for the reduced completion.

## Nuclearity and proper actions

A C*-algebra \(A\) is **nuclear** if the minimal and maximal C*-norms agree on \(A\odot D\) for every C*-algebra \(D\). The maximal norm tests commuting representations; the minimal norm uses faithful spatial representations.

**Proposition (nuclearity of amenable crossed products).** If \(G\) is amenable and \(A\) is nuclear, then \(A\rtimes_\alpha G\) is nuclear. Neither algebra is required to be unital or separable.

**Proof.** Give an arbitrary C*-algebra \(D\) the trivial action. There are canonical isomorphisms
\[
(A\rtimes_\alpha G)\otimes_{\max}D
 \cong (A\otimes_{\max}D)\rtimes_{\alpha\otimes1}G,
\tag{4A.10}
\]
\[
(A\rtimes_{\alpha,r}G)\otimes_{\min}D
 \cong (A\otimes_{\min}D)\rtimes_{\alpha\otimes1,r}G.
\tag{4A.11}
\]
Here is the norm justification. A nondegenerate representation of the left side of (4A.10) is a pair of commuting nondegenerate representations of \(A\rtimes G\) and \(D\). The first is an integrated covariant pair \((\pi,U)\). Its multiplier extension still commutes with the representation \(\rho\) of \(D\): for a multiplier \(m\), write its strong operator limit as \(m e_i\), using an approximate identity of \(A\rtimes G\). Each \(m e_i\) commutes with \(\rho(D)\). Thus both \(\pi(A)\) and \(U(G)\) commute with \(\rho(D)\), and \((\pi\cdot\rho,U)\) is a covariant pair for \(A\otimes_{\max}D\). Conversely any such pair restricts to these commuting representations by the canonical multiplier maps of the tensor product. The two constructions are inverse and preserve the integrated elements \(f\otimes d\). Taking universal norms proves (4A.10).

For (4A.11), choose faithful nondegenerate spatial representations \(\pi\) of \(A\) and \(\rho\) of \(D\). Under
\(L^2(G,H_\pi\otimes H_\rho)=L^2(G,H_\pi)\otimes H_\rho\), the regular coefficient representation is \(\widetilde\pi\otimes\rho\), and group translation is \(\lambda\otimes1\). Hence the integrated elementary function \(s\mapsto f(s)\otimes d\) acts as \((\widetilde\pi\rtimes\lambda)(f)\otimes\rho(d)\). Finite sums of these functions are dense in \(L^1(G,A\otimes_{\min}D)\), by compact-support approximation, a finite partition of unity and density of \(A\odot D\). The faithful-coefficient regular norm theorem of Lesson 2 proves (4A.11).

Nuclearity identifies the coefficient algebras in (4A.10) and (4A.11), equivariantly. Theorem 4.2 identifies their full and reduced crossed products, and also identifies \(A\rtimes G\) with \(A\rtimes_rG\). Composing these identifications gives equality of maximal and minimal norms on \((A\rtimes G)\odot D\): on each elementary integrated tensor the composition is the canonical identity. Since \(D\) was arbitrary, this proves nuclearity. ∎

Blackadar, *Operator Algebras*, IV.3.5.2, and Williams, Corollary 7.18, record this permanence theorem. For a proper action of a locally compact group on a locally compact Hausdorff space \(X\), the canonical full-to-reduced map for \(C_0(X)\) is also an isomorphism, even when the group is not amenable. Its proof is the Hilbert-module construction in [*Proper actions, free actions and the orbit space*](KT-CP-09.md), Proposition 9.4. Blackadar, II.10.4.8, gives the corresponding literature statement.

## The discrete converse and its limits for actions

For a discrete group \(\Gamma\), an invariant mean is a state \(m\) on \(\ell^\infty(\Gamma)\) such that \(m(f(g^{-1}\,\cdot))=m(f)\). We have already related this definition to (2).

**Proposition 4.3.** If the canonical quotient
\(C^*(\Gamma)\to C_r^*(\Gamma)\) is injective, then \(\Gamma\) is amenable.

**Proof.** For countable \(\Gamma\), this is [*Means, Følner sets, and regular representations*, Theorem 6.1]. Its converse proof establishes the slightly more explicit statement that a state \(\varepsilon\) on \(C_r^*(\Gamma)\) with \(\varepsilon(\lambda_g)=1\) for every \(g\) yields an invariant mean, by state extension and restriction to diagonal operators. We use that verified argument.

Here is the additional justification for an arbitrary discrete group. The canonical isomorphism in the hypothesis puts exactly this trivial-character state on \(C_r^*(\Gamma)\). For every countable subgroup \(\Lambda\), restriction of the left regular representation to \(\Lambda\) is an orthogonal sum of its regular representation: decompose \(\Gamma\) into right cosets \(\Lambda t\) and use \(\delta_h\mapsto\delta_{ht}\). Thus the map \(\lambda_h^\Lambda\mapsto\lambda_h^\Gamma\) embeds \(C_r^*(\Lambda)\) isometrically. Restricting \(\varepsilon\) to this subalgebra meets the state hypothesis of the cited converse proof, so \(\Lambda\) has an invariant mean \(m_\Lambda\).

Countable subgroups form a directed set under inclusion: the subgroup generated by two of them is countable. Define a state on \(\ell^\infty(\Gamma)\) by

\[
\widetilde m_\Lambda(f)=m_\Lambda(f|_\Lambda).
\tag{13}
\]

For each \(g\in\Lambda\) this state is invariant under left translation by \(g\). The state space of \(\ell^\infty(\Gamma)\) is weak-* compact, so this net has a convergent subnet. For every fixed \(g\in\Gamma\), the net, and hence its subnet, eventually ranges over subgroups containing \(g\). Its limit is therefore invariant under every \(g\). It is an invariant mean on \(\Gamma\). \(\square\)

Combining Theorem 4.2 with this proposition characterizes discrete group amenability by the *canonical* full-to-reduced group-algebra map. An abstract algebra isomorphism, with no compatibility with that map, is a different assertion.

The programme course *Kasparov's KK-theory*, the prerequisite, *Descent and the K-theory of crossed products*, owns the bivariant substitute called **\(K\)-amenability**. Its required scope is the full and reduced descent construction, the implication that the canonical quotient induces
\[
K_i(A\rtimes_\alpha G)\longrightarrow K_i(A\rtimes_{\alpha,r}G)
\quad\text{as an isomorphism},\qquad i=0,1,
\tag{4A.12}
\]
for second countable \(K\)-amenable locally compact groups and separable coefficient algebras, and the free-product theorem implying that free groups are \(K\)-amenable. This additional bivariant assertion is conditional on a proof not included in this edition; see Prerequisites. Blackadar, *K-Theory for Operator Algebras*, §20.9, credits the underlying theory. Equality of K-groups does not imply equality of the two C*-norms.

The free group \(F_2=\langle a,b\rangle\) supplies a concrete failure. The already proved norm calculation in *Unitary representations and the two group C* completions*, section *A strict gap: the free group on two generators*, Proposition 13.1 and equations (13.2)–(13.5), gives

\[
\|a+a^{-1}+b+b^{-1}\|_{C^*(F_2)}=4,\qquad
\|\lambda_a+\lambda_{a^{-1}}+\lambda_b+\lambda_{b^{-1}}\|=2\sqrt3.
\tag{14}
\]

Hence the canonical quotient is not injective, and \(F_2\) does not satisfy (2).

Equality for one action need not force group amenability. Lesson 2 records a nonempty compact space with a topologically amenable \(F_2\)-action for which \(C(X)\rtimes F_2\to C(X)\rtimes_r F_2\) is an isomorphism; its geodesic probabilities and the compression proof of equality are supplied there. The coefficient dynamics matter. Proposition 4.3 uses \(A=\mathbb C\), so that *all* group representations enter the full group algebra.

## Exercises with complete solutions

**Exercise 1 (basic).** Give explicit almost invariant unit vectors for \(\mathbb Z\) and \(\mathbb R\), and quantify their error on a fixed compact set.

**Solution.** On \(\mathbb Z\), take \(\xi_N=(2N+1)^{-1/2}1_{\{-N,\ldots,N\}}\). If \(|k|\leq R\leq2N+1\), (10) gives
\(\|\lambda_k\xi_N-\xi_N\|_2^2=2|k|/(2N+1)\leq2R/(2N+1)\).
Every compact subset of \(\mathbb Z\) has such a bound \(R\). On \(\mathbb R\), use \(\xi_L=(2L)^{-1/2}1_{[-L,L]}\). For \(|s|\leq R\leq2L\), (11) gives
\(\|\lambda_s\xi_L-\xi_L\|_2^2=|s|/L\leq R/L\).
These are norm-one vectors, and both estimates tend to zero uniformly on the specified sets.

**Exercise 2 (intermediate).** Suppose \((\pi,U)\) is covariant and \((\xi_i)\) satisfies (2). Establish the integrated norm comparison, making explicit why convergence uniform on compact sets is enough.

**Solution.** Set \(T_f=\int \pi(f(s))U_s\otimes\lambda_s\,ds\), and \(J_i v=v\otimes\xi_i\). Then \(J_i^*T_fJ_i=\int\varphi_i(s)\pi(f(s))U_s\,ds\). For \(K=\operatorname{supp}f\), the difference from \((\pi\rtimes U)(f)\) is bounded in norm by
\(\|f\|_1\sup_K|\varphi_i-1|\), which tends to zero. Integrating a pointwise limit alone would not give this estimate; (2) supplies the uniform bound on the actual support. Contractivity of compression gives
\(\|(\pi\rtimes U)(f)\|\leq\|T_f\|\), by taking the limit. Absorption and regular-norm domination give \(\|T_f\|\leq\|f\|_r\), whether or not \(\pi\) is faithful. Taking the supremum proves the equality of completion norms.

**Exercise 3 (intermediate).** For compact \(G\), prove the full-to-reduced equality directly using a reducing subspace of (6).

**Solution.** Put \(\eta=m^{-1/2}1_G\), where \(m\) is the Haar mass, and \(Jv=v\otimes\eta\). The subspace \(H\otimes\mathbb C\eta\) is invariant under \(\pi(a)\otimes1\) and \(U_s\otimes\lambda_s\), and also under their adjoints. Their restrictions are \(\pi(a)\) and \(U_s\), since \(\lambda_s\eta=\eta\). Thus \((\pi\rtimes U)(f)=J^*T_fJ\) exactly, with no limiting argument. Fell absorption bounds \(\|T_f\|\) by \(\|f\|_r\); the supremum over pairs gives \(\|f\|_u\leq\|f\|_r\). This works for nonunital \(A\) and every Haar normalization.

**Exercise 4 (advanced).** Let \(\Gamma\) be discrete. Show that equality for \(A=\mathbb C\) forces amenability, and explain why equality for a specified nonzero coefficient algebra is weaker.

**Solution.** Equality through the canonical map puts the trivial-character state on \(C_r^*(\Gamma)\). For a countable group the state-extension converse in *Means, Følner sets, and regular representations*, Theorem 6.1, gives an invariant mean. For an arbitrary group, restrict this state to each countable subgroup using the right-coset regular decomposition. Lift the resulting subgroup means by restriction as in (13), and take a weak-* cluster point. Every group element belongs eventually to the subgroups indexing the net, so the limit is invariant under all translations. This is exactly the countability-removal argument in Proposition 4.3. The harmonic-analysis equivalence and (4) then supply Reiter vectors.

For an action on another algebra, covariance restricts the allowed group representations. The compact amenable \(F_2\)-action constructed and proved in Lesson 2 has equal crossed-product completions although (14) separates the group-algebra norms. The zero algebra would give equality for every group for the simpler reason that both crossed products vanish; requiring a nonzero algebra avoids that vacuous example, but does not eliminate the dynamical example.

## What this lesson does not prove

Our owned proof is the amenable-group crossed-product equality, including the explicit Reiter constructions and the arbitrary-discrete extension of the converse. Its exact prerequisites are the regular-norm and absorption results proved in Lesson 2 and the countable-discrete converse in *Means, Følner sets, and regular representations*, Theorem 6.1, including its trivial-character state argument. Weak-* compactness of state spaces is a foundational functional-analysis input.

The equivalence of invariant means with normalized compact-uniform \(L^1\) probabilities, abelian-group amenability and closed-normal-extension permanence are proved above, using the precise written programme Fourier input just identified. Nuclearity is proved above; the proper-action completion theorem is proved in the owned Lesson 9. The bivariant extension to \(K\)-amenable groups belongs to the bivariant prerequisite identified above. We do not prove the general theory of amenable actions, or infer amenability of a group from equality for one action. Formula (14) imports the existing tree-norm calculation rather than repeating it.

## References

- **[Williams]** Dana P. Williams, *Crossed Products of C\*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. Theorem 7.13, Corollary 7.18, and Appendix A, Remark A.15 and Proposition A.16. [Author's Version 3.1 draft](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf), with these numbered results; [book page and errata](https://math.dartmouth.edu/~dana/cpcsa/).
- **[Blackadar 2006]** Bruce Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006. II.10.3.15, II.10.4.8, and IV.3.5.2. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Blackadar 1998]** Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998. §20.9, *K-Theoretic Amenability for Groups*. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Unitary representations and the two group C* completions](../prerequisites/src/OA-FLOW/repaired-20261004/group-representations-and-completions.md)** Chapter in *Crossed Products & Flow of Weights*, section *A strict gap: the free group on two generators*, Proposition 13.1 and equations (13.2)–(13.5).
- **[Means, Følner sets, and regular representations]** Theorem 6.1 and its converse proof: canonical full-to-reduced norm equality characterizes amenability for countable discrete groups. Proposition 4.3 above supplies the additional countability-removal argument.

# The Plancherel theorem

**Lesson HA-LCA-08.** Self-checked by the writing AI.

Let \(G\) be any locally compact Hausdorff abelian group, with Haar measure \(dx\) on the complete locally determined domain. Write \(\Gamma=\widehat G\), and equip it with the dual Haar measure \(d\xi\) constructed in HA-LCA-07, Theorem 2.1. The integral Fourier transform has negative sign:
\[
 \widehat f(\gamma)=\int_Gf(x)\overline{\gamma(x)}\,dx.
\]
Put \(D=L^1(G)\cap L^2(G)\). Inner products are linear in the first variable. The symbol \(\mathcal F\) below will denote the extension to \(L^2\) classes.

The freely accessible mathematical sources are D. H. Fremlin, [*Measure Theory*, §§445R–T](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex), version of 20 March 2008, and Terence Tao, [*245C, Notes 1: Interpolation of \(L^p\) spaces*, Theorems 4 and 21](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/), 30 March 2009. The interpolation proof below supplies the particular complex-variable argument it needs and makes no sigma-finiteness assumption.

Adaptation and additional proofs: GPT-6 Astra (OpenAI), Ultra, October 2026. This combined lesson is under the Design Science License. Fremlin's copyright 1998 and original notices are retained in the unchanged volume 4 source package. The summable-tail argument also uses the freely accessible [§244G–H](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt244.tex), copyright 1995, whose original notices remain in the volume 2 source package. The cited lecture notes themselves are not reproduced.

The earlier proof tools used here are:

- HA-LCA-05, Lemma 3.0: Hölder, Minkowski and \(C_c\)-density in every finite \(L^p\); the Hilbert reading, Theorem 6.1: arbitrary-measure \(L^2\) completeness and its inner product. Its Lemma 1.1 proves Cauchy–Schwarz and polarization; its Corollary 2.2 proves orthogonal projection and decomposition.
- The general Haar reading, Lemma 5.1: Borel representatives supported on countable unions of compact sets, containment in open sigma-compact subgroups, full-Borel Fubini after that reduction, and null-set independence. Its Proposition 5.2 proves \(L^2\) translation continuity; Theorem 4.1 proves inversion and translation substitution; Corollary 6.2 gives compactly supported approximate identities.
- HA-LCA-03, Theorem 3.1: integral-transform laws; its Corollary 2.2: the \(C_0\) conclusion; its Lemma 4.1: finite Radon measures from \(L^1\) densities, with their exact variation.
- HA-LCA-04, Proposition 2.2: the positive-type \(L^2\) autocorrelation; HA-LCA-06, Proposition 1.1: injectivity and the integral pairing for \(T\mu(x)=\int\gamma(x)\,d\mu(\gamma)\); its Theorem 2.1 and Proposition 4.1: positive and complex measure representations and the algebra \(B(G)\).
- HA-LCA-07, Lemma 1.1: a positive \(C_c\) function whose transform is strictly positive on a prescribed compact set; its Theorem 2.1: pointwise \(B^1\) inversion. Its Propositions 3.2–3.3 prove all Euclidean, compact and discrete normalizations.

## 0. Norm limits on arbitrary measure spaces

<a id="ha-lca-08-lemma-0-1"></a>
**Lemma 0.1 — Summable tails.** On any measure space, let \(1\le p<\infty\). If \(\sum_j\|u_j\|_p<\infty\), then \(\sum_ju_j\) converges absolutely almost everywhere and in \(L^p\), and
\[
 \left\|\sum_{j\ge m}u_j\right\|_p\le\sum_{j\ge m}\|u_j\|_p.
 \tag{1}
\]
The space \(L^p\) is complete. Norm convergence has an almost-everywhere convergent subsequence. Simple functions supported on sets of finite measure approximate any function simultaneously in any finite list of finite \(L^p\) norms in which it belongs.

**Proof.** Minkowski gives
\(\|\sum_{j=m}^n|u_j|\|_p\le\sum_{j=m}^n\|u_j\|_p\).
Taking \(p\)-th powers and applying monotone convergence shows that
\(U_m=\sum_{j\ge m}|u_j|\) has integral of its \(p\)-th power at most
\((\sum_{j\ge m}\|u_j\|_p)^p\). Thus \(U_1<\infty\) almost everywhere. Define the sum on this set and set it to zero on the null exceptional set. Its tails are bounded by \(U_m\), which proves (1) and norm convergence.

From any Cauchy sequence choose a subsequence whose successive norm differences are at most \(2^{-j}\). The first part sums those differences to an \(L^p\) limit; the Cauchy condition then makes the entire sequence converge to the same limit. This proves completeness. If \(f_n\to f\) in norm, select a subsequence with \(\sum_j\|f_{n_j}-f\|_p<\infty\). The first part implies \(f_{n_j}\to f\) almost everywhere.

For the final statement put \(E_n=\{1/n\le|f|\le n\}\). Each has finite measure, by any one of the finite \(L^p\) norms. The functions \(f1_{E_n}\) tend to \(f\) in every specified norm by dominated convergence. On \(E_n\), approximate the bounded complex values by a finite grid of mesh \(\delta_n\), and set the approximation to zero off \(E_n\). The error in each \(L^p\) norm is at most \(2\delta_n\mu(E_n)^{1/p}\); choose \(\delta_n\) to make all these finitely many errors tend to zero. All measure-limit steps are the monotone and dominated convergence theorems proved in the integration reading, Theorems 1.2 and 2.2. No sigma-finiteness was assumed. \(\square\)

Sequences here are sequences in a normed space. Their use requires neither a countable neighbourhood base on the group nor a countable cover of the whole Haar space.

## 1. Isometry and surjectivity

<a id="ha-lca-08-theorem-1-1"></a>
**Theorem 1.1 — Plancherel.** The Fourier transform on \(L^1(G)\cap L^2(G)\) extends uniquely to a unitary operator
\[
 \mathcal F:L^2(G,dx)\longrightarrow L^2(\Gamma,d\xi).
 \tag{2}
\]
For \(f\in L^1(G)\cap L^2(G)\), \(\mathcal Ff\) is the class of the integral transform \(\widehat f\). For arbitrary \(f,g\in L^2(G)\),
\[
 \langle f,g\rangle=\langle\mathcal Ff,\mathcal Fg\rangle.
 \tag{3}
\]
These assertions hold for every LCA group with the dual Haar measure, without a countability assumption.

**Proof.** If \(f\in D\), its autocorrelation \(h=f*\widetilde f\), where \(\widetilde f(x)=\overline{f(-x)}\), is continuous and of positive type by HA-LCA-04, Proposition 2.2. It is also \(L^1\), since it represents the \(L^1\) convolution of two \(L^1\) functions. Bochner puts \(h\) in \(B^1(G)\), and the transform law gives \(\widehat h=|\widehat f|^2\). Inversion at zero yields
\[
 \int_\Gamma|\widehat f|^2\,d\xi
 =h(0)=\int_G|f|^2\,dx.
 \tag{4}
\]
Thus the integral transform defines a linear isometry on \(D\). Since \(C_c(G)\subseteq D\) is dense in \(L^2(G)\), completeness gives a unique linear isometric extension: if \(f_n\in D\) tends to \(f\) in \(L^2\), define \(\mathcal Ff\) as the \(L^2\) limit of \(\widehat f_n\). The isometry bound makes the result independent of the approximants. Polarization proves (3). Its range \(W\) is closed: the inverse images of a convergent sequence in \(W\) are Cauchy, and their limit maps to the given limit.

We prove surjectivity. If \(W\) were a proper closed subspace, orthogonal projection would give a nonzero \(v\in W^\perp\). Fix \(f\in D\). For every \(x\in G\), the translate \(L_xf(y)=f(y-x)\) is in \(D\), and its integral transform is \(\overline{\gamma(x)}\widehat f(\gamma)\). Hence
\[
 \int_\Gamma \overline{\gamma(x)}\widehat f(\gamma)\overline{v(\gamma)}\,d\xi(\gamma)=0
 \quad(x\in G).
 \tag{5}
\]
Cauchy–Schwarz and (4) show that
\(w=\widehat f\,\overline v\in L^1(\Gamma)\). Its density \(w\,d\xi\) is a finite complex Radon measure. Equation (5) is \(T(w\,d\xi)(-x)=0\); the previously proved injectivity of \(T\) implies \(w\,d\xi=0\). The exact variation formula then gives \(w=0\) almost everywhere.

Given compact \(K\subseteq\Gamma\), choose \(h\in C_c(G)\cap P(G)\) with \(\widehat h>0\) on \(K\), by HA-LCA-07, Lemma 1.1. This \(h\) is in \(D\), so the preceding argument gives \(v=0\) almost everywhere on \(K\). By the earlier full-Haar \(L^2\) representative theorem, \(v\) is zero outside a countable union of compact sets, up to a null set. Taking that countable union now gives \(v=0\) almost everywhere on the whole dual, a contradiction. We have not taken an uncountable union of exceptional null sets. Thus \(W=L^2(\Gamma)\), proving (2). \(\square\)

For a general \(L^2\) function, (2) defines a norm limit, not an absolutely convergent integral at each frequency. The integral formula remains valid exactly on the stated intersection \(D\).

## 2. Convolution, multiplication and an inverse integral

<a id="ha-lca-08-proposition-2-1"></a>
**Proposition 2.1.** For \(h\in L^1(G)\), \(f\in L^2(G)\), convolution defines an \(L^2\) class and
\[
 \|h*f\|_2\le\|h\|_1\|f\|_2,\qquad
 \mathcal F(h*f)=\widehat h\,\mathcal Ff.
 \tag{6}
\]
For \(f,g\in L^2(G)\), the convolution integral is absolutely convergent at every point, defines a function in \(C_0(G)\), and satisfies
\[
 \|f*g\|_\infty\le\|f\|_2\|g\|_2.
 \tag{7}
\]
Their pointwise product belongs to \(L^1(G)\), and
\[
 \widehat{fg}=(\mathcal Ff)*(\mathcal Fg)
 \quad\hbox{pointwise on }\Gamma.
 \tag{8}
\]

**Proof.** Choose Borel representatives of \(h,f\) supported in a common open sigma-compact subgroup \(J\), using the general Haar reading, Lemma 5.1. On \(J\times J\), its full-Borel Tonelli theorem gives
\[
 \int_J\int_J |h(y)|\,|f(x-y)|^2\,dy\,dx
 =\|h\|_1\|f\|_2^2.
\]
For almost every \(x\), Cauchy–Schwarz with weight \(|h(y)|dy\) therefore gives
\[
 \left|\int h(y)f(x-y)\,dy\right|^2
 \le\|h\|_1\int |h(y)|\,|f(x-y)|^2\,dy.
\]
The same estimate applied to absolute values proves absolute convergence at those points. The chosen convolution vanishes off \(J\). Integrating the bound proves (6)'s norm estimate. The null-pullback assertion in that Haar lemma proves independence of representatives; thus this defines the required class.

Choose \(f_n\in C_c(G)\) with \(f_n\to f\) in \(L^2\). Each \(h*f_n\) belongs to \(L^1\) by the convolution algebra theorem and to \(L^2\) by the estimate just proved. Its integral transform is \(\widehat h\,\widehat f_n\). The left side converges in \(L^2\) to \(\mathcal F(h*f)\), while the right side converges to \(\widehat h\,\mathcal Ff\), since \(\|\widehat h\|_\infty\le\|h\|_1\). This proves the transform identity in (6).

For two \(L^2\) functions and every fixed \(x\), inversion and translation preserve the \(L^2\) norm and null sets, so Cauchy–Schwarz gives
\[
 \int|f(y)g(x-y)|\,dy\le\|f\|_2\|g\|_2.
\]
This proves absolute convergence, representative independence and (7). Approximate both functions in \(L^2\) by \(C_c\) functions \(f_n,g_n\). Their convolutions are in \(C_c\), and
\[
 \|f*g-f_n*g_n\|_\infty
 \le\|f-f_n\|_2\|g\|_2+\|f_n\|_2\|g-g_n\|_2\longrightarrow0.
\]
The uniform limit is in \(C_0\), by the finite-Radon reading, Lemma 1.5. The same proof works on \(\Gamma\).

To prove (8), first note the \(L^2\) transformation rules
\[
 \mathcal F(\overline g)(\gamma)=\overline{\mathcal Fg(\gamma^{-1})},
 \qquad
 \mathcal F(\eta g)(\gamma)=\mathcal Fg(\eta^{-1}\gamma)
 \quad(\eta\in\Gamma).
 \tag{9}
\]
They hold as integral identities on \(D\). Conjugation, inversion, multiplication by a character and translation on the dual are isometries of the relevant \(L^2\) spaces, so density extends the identities to all \(L^2\) classes.

Cauchy–Schwarz gives \(fg\in L^1(G)\). For each \(\eta\in\Gamma\), Parseval and (9) now give
\[
 \begin{aligned}
 \widehat{fg}(\eta)
 &=\langle f,\eta\overline g\rangle\\
 &=\left\langle\mathcal Ff,\,
       \overline{\mathcal Fg(\,\cdot^{-1}\eta)}\right\rangle\\
 &=\int_\Gamma\mathcal Ff(\gamma)\,
                     \mathcal Fg(\gamma^{-1}\eta)\,d\xi(\gamma).
 \end{aligned}
\]
The last expression is the \(L^2*L^2\) convolution already proved well defined and continuous at every point. Thus (8) is a pointwise identity of \(C_0\) functions. No bidual surjectivity was used. \(\square\)

<a id="ha-lca-08-lemma-2-2"></a>
**Lemma 2.2 — The inverse on \(L^1\cap L^2\).** If \(\phi\in L^1(\Gamma)\cap L^2(\Gamma)\), then
\[
 u(x)=\int_\Gamma\phi(\gamma)\gamma(x)\,d\xi(\gamma)
 \tag{10}
\]
is bounded and continuous, lies in \(B(G)\cap L^2(G)\), and represents \(\mathcal F^{-1}\phi\).

**Proof.** The finite Radon density \(\phi\,d\xi\) and the earlier properties of \(T\) make \(u=T(\phi\,d\xi)\) a bounded continuous \(B(G)\) function. Put \(v=\mathcal F^{-1}\phi\), initially an \(L^2\) class. For every \(a\in C_c(G)\), Parseval and the integral pairing in HA-LCA-06, Proposition 1.1, with the signs in (10), give
\[
 \int_Ga\,\overline v\,dx
 =\int_\Gamma\widehat a\,\overline\phi\,d\xi
 =\int_Ga\,\overline u\,dx.
 \tag{11}
\]
The last identity also follows by compact-localized Fubini and the \(L^1\) tail of \(\phi\), precisely as in that pairing proof.

For any compact \(K\subseteq G\), choose a real cutoff \(w\in C_c(G)\), \(0\le w\le1\), with \(w=1\) on \(K\). Cauchy–Schwarz on its compact support shows that \(w(v-u)\in L^1(G)\). Testing (11) with \(aw\) for all \(a\in C_c(G)\) makes the finite Radon density \(w\,\overline{(v-u)}\,dx\) annihilate \(C_c(G)\). Finite Radon uniqueness implies this measure is zero; its variation gives \(v=u\) almost everywhere on \(K\).

This local conclusion implies global equality on our Haar domain. For each \(n\), the measurable set \(E_n=\{|v-u|\ge1/n\}\) has measure zero on every compact set. Inner regularity on all measurable sets, proved in the general Haar reading, Theorem 3.1, gives \(\mu(E_n)=0\): every compact subset of \(E_n\) has measure zero. The countable union of the \(E_n\) contains all points of disagreement after choosing finite representatives. Thus \(u=v\) almost everywhere, proving both its \(L^2\) membership and (10). \(\square\)

## 3. The Fourier algebra of the dual

Define \(A(\Gamma)=\{\widehat h:h\in L^1(G)\}\), a space of actual continuous functions vanishing at infinity.

<a id="ha-lca-08-theorem-3-1"></a>
**Theorem 3.1.** One has the equality of sets of continuous functions
\[
 A(\Gamma)=\{\phi*\psi:\phi,\psi\in L^2(\Gamma)\}.
 \tag{12}
\]

**Proof.** If \(h\in L^1(G)\), put
\(f=|h|^{1/2}\) and
\(g=|h|^{1/2}\operatorname{sgn}h\), where
\(\operatorname{sgn}h=h/|h|\) off its zero set and zero on it.
Then \(f,g\in L^2(G)\), \(h=fg\), and (8) expresses \(\widehat h\) as the convolution of their \(L^2\) transforms.

Conversely, given \(\phi,\psi\in L^2(\Gamma)\), surjectivity of \(\mathcal F\) gives \(f,g\in L^2(G)\) with these transforms. Their product is \(L^1\), and (8) gives \(\phi*\psi=\widehat{fg}\) pointwise. This proves both inclusions using only Plancherel and Parseval. \(\square\)

<a id="ha-lca-08-corollary-3-2"></a>
**Corollary 3.2 — Local frequency support.** Every nonempty open \(O\subseteq\Gamma\) contains the support of a nonzero member of \(A(\Gamma)\).

**Proof.** Choose \(\eta\in O\). Continuity of multiplication and inversion, followed by the locally compact shrinking lemma, gives a relatively compact identity neighbourhood \(V\) with
\(\eta\,\overline V\,\overline V^{-1}\subseteq O\).
Choose a nonzero \(a\in C_c(\Gamma)\) supported in \(V\). The autocorrelation \(k=a*\widetilde a\) has compact support in
\(\overline V\,\overline V^{-1}\) and
\(k(1)=\|a\|_2^2>0\). Its translate \(L_\eta k=(L_\eta a)*\widetilde a\) is therefore nonzero, supported in \(O\), and belongs to \(A(\Gamma)\) by (12). The translation identity follows directly by substitution in the absolutely convergent convolution. \(\square\)

<a id="ha-lca-08-corollary-3-3"></a>
**Corollary 3.3.** If \(\phi,\psi\in C_c(\Gamma)\), then \(\phi*\psi=\widehat h\) for some \(h\in B^1(G)\). Consequently \(\widehat{B^1(G)}\) is dense in \(L^p(\Gamma)\) for every \(1\le p<\infty\).

**Proof.** Both functions belong to \(L^1\cap L^2\). Lemma 2.2 identifies their inverse transforms \(u,v\) as members of \(B(G)\cap L^2(G)\). The product \(h=uv\) is in \(B(G)\) because this is an algebra, and in \(L^1(G)\) by Cauchy–Schwarz. Formula (8) gives \(\widehat h=\phi*\psi\).

For density, fix \(\phi\in C_c(\Gamma)\). Let \(e_U\) be the nonnegative \(C_c\) approximate identities from the Haar reading, normalized to integral one and supported in shrinking identity neighbourhoods inside one fixed compact neighbourhood \(V\). That reading proves \(\phi*e_U\to\phi\) uniformly. Their supports lie in the fixed compact set \((\operatorname{supp}\phi)V\), so
\[
 \|\phi*e_U-\phi\|_p
 \le \xi((\operatorname{supp}\phi)V)^{1/p}
       \|\phi*e_U-\phi\|_\infty\longrightarrow0.
\]
Every approximant is in \(\widehat{B^1(G)}\) by the first part. The already proved \(C_c\)-density for each finite \(p\), followed by the triangle inequality, gives the assertion. Here \(U\) is the full neighbourhood net. \(\square\)

## 4. Fourier series and normalization

<a id="ha-lca-08-corollary-4-1"></a>
**Corollary 4.1.** If \(G\) is compact with Haar mass one, its characters form an orthonormal basis of \(L^2(G)\). If \(G\) is discrete with counting measure, then
\[
 \ell^2(G)\cong L^2(\Gamma,d\xi),
 \qquad \xi(\Gamma)=1.
 \tag{13}
\]
For the real pairing \(e^{2\pi ix\xi}\), Plancherel has no scalar factor. For the pairing \(e^{ixs}\), it reads
\[
 \int_{\mathbb R}|f(x)|^2\,dx
 =\frac1{2\pi}\int_{\mathbb R}|\mathcal Ff(s)|^2\,ds.
 \tag{14}
\]

**Proof.** In the compact case, HA-LCA-07, Proposition 3.3, proves that the dual measure is counting measure and that the transform of a character \(\chi\) is the point indicator \(1_{\{\chi\}}\). These indicators are an orthonormal basis of \(\ell^2(\Gamma)\): for each square-summable family and each \(n\), the set of coordinates of modulus at least \(1/n\) is finite, so the support is countable; finite truncation then approximates in norm. Unitarity pulls this basis back to the characters. The \(L^2\) expansion is the norm limit over finite subsets of \(\Gamma\), whether or not \(\Gamma\) is countable.

The same normalization proposition gives Haar probability on the dual of a discrete primal group; Theorem 1.1 gives (13). In particular on the circle, with normalized measure,
\(\|f\|_2^2=\sum_{n\in\mathbb Z}|\widehat f(n)|^2\), and its Fourier series converges to \(f\) in \(L^2\). The Euclidean constants in (14) and the preceding statement are exactly the dual measures proved in HA-LCA-07, Proposition 3.2. \(\square\)

<a id="ha-lca-08-example-4-2"></a>
**Example 4.2 — A transform defined by an \(L^2\) limit.** On \(\mathbb R\) with pairing \(e^{2\pi ix\xi}\), let \(\phi=1_{[-1,1]}\) on the frequency line. Its inverse Plancherel transform is
\[
 u(x)=
 \begin{cases}
 \dfrac{\sin(2\pi x)}{\pi x},&x\ne0,\\
 2,&x=0.
 \end{cases}
 \tag{15}
\]
This function belongs to \(L^2\setminus L^1\). Its Fourier transform is the class of \(\phi\), obtained as an \(L^2\) limit; the absolutely convergent Lebesgue Fourier integral for \(u\) exists at no frequency.

**Proof.** Lemma 2.2 applies to \(\phi\in L^1\cap L^2\). Integrating \(e^{2\pi ix\xi}\) over \([-1,1]\) gives (15), using the exponential derivative and fundamental theorem already proved in the real-variable reading. At zero the integral is two. Thus \(u\in L^2\) and \(\mathcal Fu=\phi\).

The quarter-period value \(\sin(\pi/2)=1\) and continuity, proved in the Banach reading, Lemma 1.3, give a number \(0<\delta<1/4\) for which
\(\sin(2\pi x)\ge1/2\) on
\([n+1/4-\delta,n+1/4+\delta]\) for every integer \(n\ge1\). Consequently
\[
 \int_{n+1/4-\delta}^{n+1/4+\delta}|u(x)|\,dx
 \ge\frac{\delta}{\pi(n+1)}.
\]
The sum diverges: each block \(2^k\le n<2^{k+1}\) contributes a fixed positive lower bound. Therefore \(u\notin L^1\). Multiplication by any character has modulus one and does not change the divergent absolute integral. This statement concerns the Lebesgue integral; it makes no assertion about conditionally convergent improper integrals. For example \(u1_{[-R,R]}\in D\) converges to \(u\) in \(L^2\) as \(R\to\infty\), and its integral transforms converge to \(\phi\) in \(L^2\). \(\square\)

## 5. Where countability enters

<a id="ha-lca-08-lemma-5-1"></a>
**Lemma 5.1.** Every \(L^2(G)\) class has a representative zero outside a sigma-compact open subgroup of \(G\).

**Proof.** This is the full-domain conclusion of the general Haar reading, Lemma 5.1. Explicitly, the sets \(\{|f|\ge1/n\}\) have finite measure. Compact inner approximation of these sets gives a countable family of compact sets outside whose union \(f=0\) almost everywhere. The open-subgroup construction in that reading, Lemma 1.1, places this countable compact family in an open sigma-compact subgroup \(J\). Replacing \(f\) by zero off that union gives the required representative. The replacement changes it on one measurable null set; it is not merely a separate assertion on each compact set. \(\square\)

<a id="ha-lca-08-example-5-2"></a>
**Example 5.2 — A non-sigma-finite dual.** If \(I\) is uncountable and \(G=\mathbb T^I\), then \(G\) has Haar probability measure and
\[
 \Gamma=\bigoplus_{i\in I}\mathbb Z
\]
has counting dual measure, which is not sigma-finite.

**Proof.** Tychonoff compactness was proved in the Banach reading, Lemma 4.1, so \(G\) is a compact Hausdorff group and its nonzero Haar measure can be normalized to mass one. HA-LCA-02, Theorem 4.3 proves the displayed topological dual identification. HA-LCA-07, Proposition 3.3, gives counting measure there. This group is uncountable, since its coordinate unit elements give an injection of \(I\). Every set of finite counting measure is finite, so a countable union of such sets cannot cover the group. Nevertheless each individual \(\ell^2(\Gamma)\) vector has countable support, by the finite-level-set argument in Corollary 4.1. Thus Theorem 1.1 applies while a globally sigma-finite dual-measure argument would not. \(\square\)

## 6. Exercises with complete solutions

<a id="ha-lca-08-exercise-6-1"></a>
**Exercise 6.1 — A sinc integral.** Compute the norm of \(1_{[-1,1]}\) directly and by Plancherel.

**Solution.** Lebesgue interval length gives \(\|1_{[-1,1]}\|_2^2=2\). Direct integration of the negative exponential gives transform \(\sin(2\pi\xi)/(\pi\xi)\), with value two at zero. Theorem 1.1 therefore gives
\[
 \int_{\mathbb R}\frac{\sin^2(2\pi\xi)}{(\pi\xi)^2}\,d\xi=2,
 \qquad \|1_{[-1,1]}\|_2=\sqrt2.
 \tag{16}
\]
The value of the quotient at the single point zero is its continuous extension and does not affect the integral. \(\square\)

<a id="ha-lca-08-exercise-6-2"></a>
**Exercise 6.2 — Cyclic translates.** For \(f\in L^2(G)\), prove that the closed linear span of \(\{L_xf:x\in G\}\) is \(L^2(G)\) if and only if \(\mathcal Ff\ne0\) almost everywhere on \(\Gamma\).

**Solution.** Write \(F=\mathcal Ff\). The translation identity extends from \(D\) to \(L^2\) by density and isometry:
\(\mathcal F(L_xf)(\gamma)=\overline{\gamma(x)}F(\gamma)\).
If \(v\) is orthogonal to all these transforms, the \(L^1\) density \(F\overline v\) defines a finite Radon measure whose \(T\)-transform vanishes at every \(-x\). Injectivity of \(T\), as in (5), implies \(F\overline v=0\) almost everywhere. If \(F\ne0\) almost everywhere this forces \(v=0\); orthogonal decomposition then says the closed span is all of \(L^2(\Gamma)\), and unitarity gives the conclusion on \(G\).

Conversely suppose \(E=\{F=0\}\) has positive measure. Full-domain compact inner regularity gives a compact \(K\subseteq E\) with \(0<\xi(K)<\infty\). Then \(v=1_K\) is a nonzero \(L^2\) vector orthogonal to every \(\overline{\gamma(x)}F\). Its inverse under \(\mathcal F\) is a nonzero vector orthogonal to all translates of \(f\), so they do not span densely. \(\square\)

<a id="ha-lca-08-exercise-6-3"></a>
**Exercise 6.3 — Two different intersections.** Show that \(\mathcal F(D)\) is dense in \(L^2(\Gamma)\), but in general is neither contained in nor equal to \(L^1(\Gamma)\cap L^2(\Gamma)\).

**Solution.** Theorem 1.1 and density of \(D\) give density of its image. On \(\mathbb R\), \(1_{[-1,1]}\in D\) has transform equal to the sinc function in (15), which is not \(L^1\) by Example 4.2. Thus the image need not be contained in the target intersection.

The frequency indicator \(\phi=1_{[-1,1]}\) does belong to that intersection. Its unique inverse Plancherel transform is the same sinc function, again by Lemma 2.2, and this inverse is not \(L^1\). Hence \(\phi\notin\mathcal F(D)\). In this example neither of the two sets contains the other. \(\square\)

<a id="ha-lca-08-exercise-6-4"></a>
**Exercise 6.4 — Reduction to open subgroups.** For a Haar measure that is not sigma-finite, justify Plancherel by doing its source-side integration inside sigma-compact open subgroups.

**Solution.** For \(f\in D\), the earlier full-Haar representative theorem, or Lemma 5.1 applied to its two integrable powers, gives an open sigma-compact subgroup \(J\) outside which \(f=0\) almost everywhere. Choose the representative zero there. Its autocorrelation vanishes off \(J\), and every integral defining the autocorrelation at a point of \(J\), its identity value, and its \(L^1\) norm can be computed with the restricted Haar measure on \(J\). This restriction is sigma-finite on its ordinary completed Borel domain. The full-Borel Fubini theorem therefore justifies each required source-side interchange there. Given finitely or countably many functions, one common \(J\) contains their compact support families.

For each character of the whole group, the forward transform is still
\(\widehat f(\gamma)=\int_J f(x)\overline{\gamma(x)}\,dx\).
The autocorrelation, regarded as a function on \(G\), is integrable and of positive type by the earlier full-group autocorrelation theorem. Apply the already proved full-group \(B^1\) inversion to it. This gives exactly (4), with integration on the whole dual \(\Gamma\) and its prescribed dual Haar measure.

Extend the isometry by \(C_c\)-density and \(L^2\) completeness. For surjectivity, the orthogonal-complement argument (5) uses finite Radon densities on \(\Gamma\), then compact masks. Any remaining orthogonal vector is supported, up to a null set, on a countable compact union in \(\Gamma\), so the compact conclusions imply global vanishing. These are all steps of Theorem 1.1. This reduction never identifies the dual of \(J\) with \(\Gamma\); such an identification would be false in general and is unnecessary. The source integral reduction and the full dual-measure construction have separate roles. \(\square\)

## 7. Hausdorff–Young with its interpolation proof

We prove the needed interpolation estimate rather than cite a complex-analysis or interpolation theorem. Only finite exponential sums enter its scalar step.

<a id="ha-lca-08-lemma-7-0"></a>
**Lemma 7.0 — A strip bound for exponential sums.** Let
\(F(z)=\sum_{j=1}^m c_j e^{a_jz}\), with \(c_j\in\mathbb C\) and \(a_j\in\mathbb R\). If
\[
 |F(it)|\le1,\qquad |F(1+it)|\le1\quad(t\in\mathbb R),
\]
then \(|F(\theta)|\le1\) for \(0\le\theta\le1\).

**Proof.** We first prove the particular maximum principle we need. A finite sum of functions \(e^{az+bz^2}\), with complex constants, has a power series about every centre converging absolutely and uniformly on every closed disk. Indeed write \(z=z_0+w\), factor out the constant exponential, and multiply the series for \(e^{(a+2bz_0)w}\) and \(e^{bw^2}\). Absolute convergence bounds their coefficient products by \(e^{|a+2bz_0|r}e^{|b|r^2}\) on \(|w|\le r\), justifying collection by powers. The exponential series and its product law were proved in the Banach reading, Lemmas 1.2–1.3.

Let \(H\) be such a sum, and suppose its modulus has a maximum \(M\) on a closed rectangle at an interior point \(z_0\). If \(M=0\), it is constant on the rectangle. Otherwise choose a small circle \(z_0+re^{it}\) inside it. Termwise integration of the power series and the circle orthogonality proved in that reading, Lemma 1.3, give
\[
 H(z_0)=\frac1{2\pi}\int_0^{2\pi}H(z_0+re^{it})\,dt.
\]
The continuous nonnegative function
\(M^2-\operatorname{Re}(\overline{H(z_0)}H(z_0+re^{it}))\)
has integral zero, so it is identically zero. Together with
\(|H(z_0+re^{it})|\le M\), this forces \(H\) to equal \(H(z_0)\) on the circle. Multiply the same uniformly convergent series by \(e^{-int}\) and integrate. For every \(n\ge1\) this gives \(b_nr^n=0\), where \(b_n\) is its \(n\)-th coefficient. Thus all nonconstant coefficients vanish. The series about \(z_0\) converges everywhere, so \(H\) is constant everywhere. We have proved that the maximum of \(|H|\) on a rectangle cannot exceed its boundary maximum. Existence of the maximum is finite-dimensional compactness, already proved in the Banach reading, Lemma 1.1.

The sum \(F\) is bounded on \(0\le\operatorname{Re}z\le1\), since
\(|e^{a_jz}|\le\max(1,e^{a_j})\). For \(\varepsilon>0\) put
\[
 H_\varepsilon(z)=e^{\varepsilon(z^2-1)}F(z).
\]
This is a finite sum of the form just considered. On the two vertical boundary lines it has modulus at most one, because
\(\operatorname{Re}(z^2-1)=\sigma^2-t^2-1\le0\) for \(\sigma=0,1\). On the horizontal sides of a sufficiently tall rectangle \(0\le\sigma\le1\), \(|t|\le R\), its modulus is at most \(M_0e^{-\varepsilon R^2}\le1\), where \(M_0\) bounds \(F\) on the strip. The proved maximum principle gives
\(|F(\theta)|e^{\varepsilon(\theta^2-1)}\le1\).
Let \(\varepsilon\downarrow0\). This proves the result without invoking a general maximum-modulus or three-lines theorem. \(\square\)

<a id="ha-lca-08-theorem-7-1"></a>
**Theorem 7.1 — Hausdorff–Young.** For \(1\le p\le2\) and \(1/p+1/q=1\), Fourier transformation extends to a contraction
\[
 \mathcal F_p:L^p(G)\longrightarrow L^q(\Gamma).
 \tag{17}
\]
It agrees with the integral transform on \(L^p\cap L^1\) and with Plancherel on \(L^p\cap L^2\).

**Proof.** The cases \(p=1,q=\infty\) and \(p=q=2\) are the integral norm bound and Theorem 1.1. Suppose \(1<p<2\), put \(q=p/(p-1)\), and choose \(\theta=2(1-1/p)\in(0,1)\). Begin with simple functions \(f\) on \(G\) and \(g\) on \(\Gamma\), both supported on sets of finite measure. If either has zero \(L^p\) norm, the desired integral bound is immediate. By homogeneity assume both norms are one. For \(z\in\mathbb C\), define
\[
 f_z=\operatorname{sgn}f\,|f|^{p(1-z/2)},\qquad
 g_z=\operatorname{sgn}g\,|g|^{p(1-z/2)},
\]
with value zero on the respective zero sets; for a positive number \(a\), \(a^w=e^{w\log a}\). Then
\[
 F(z)=\int_\Gamma\widehat {f_z}(\gamma)g_z(\gamma)\,d\xi(\gamma)
\]
is a finite exponential sum with real exponents in \(z\). To verify this explicitly, write \(f,g\) as finite disjoint simple sums with nonzero coefficients. Linearity expresses \(F\) as a finite sum of the constants
\(\int_{B_k}\widehat {1_{A_j}}\,d\xi\), multiplied by fixed phases and
\(\exp(p(1-z/2)(\log|a_j|+\log|b_k|))\).
The constants are finite because \(A_j,B_k\) have finite measure and the integral Fourier transform is bounded.

For \(z=it\), both \(f_z\) and \(g_z\) have \(L^1\) norm one. Hence the \(L^1\to L^\infty\) bound gives \(|F(it)|\le1\). For \(z=1+it\), both have \(L^2\) norm one, so Plancherel and Cauchy–Schwarz give \(|F(1+it)|\le1\). Lemma 7.0 applies. At \(z=\theta\) the exponent \(p(1-\theta/2)\) is one, so restoring the normalizations yields
\[
 \left|\int_\Gamma\widehat f\,g\,d\xi\right|
 \le\|f\|_p\|g\|_p
 \quad\hbox{for all such simple }f,g.
 \tag{18}
\]

Fix \(f\) and put \(u=\widehat f\in C_0(\Gamma)\). For any compact \(K\subseteq\Gamma\), take
\(g=1_K\overline{\operatorname{sgn}u}\,|u|^{q-1}\).
This bounded measurable function has finite support measure. Finite-grid simple approximation on \(K\) in both \(L^p\) and \(L^1\) extends (18) to this \(g\), since \(u\) is bounded. If \(A=\int_K|u|^q\), then
\(\|g\|_p=A^{1/p}\), because \((q-1)p=q\), and (18) gives \(A\le\|f\|_p A^{1/p}\). Thus \(A^{1/q}\le\|f\|_p\), with the zero case included. The compact sets \(\{|u|\ge1/n\}\) increase to the nonzero set of \(u\). Monotone convergence gives
\[
 \|\widehat f\|_q\le\|f\|_p
 \tag{19}
\]
on the full Haar domain. This step used compact level sets instead of an unproved general duality theorem.

Simple functions supported on sets of finite measure are dense in \(L^p(G)\), by Lemma 0.1. Completeness of \(L^q(\Gamma)\), also proved there, extends (19) uniquely to the contraction (17).

If \(f\in L^p\cap L^1\), choose simple approximants converging in both norms. Their transforms converge uniformly to the integral transform by the \(L^1\) bound, and in \(L^q\) to \(\mathcal F_pf\) by (19). An almost-everywhere convergent subsequence from Lemma 0.1 identifies the two limits. If \(f\in L^p\cap L^2\), choose approximants converging in these two norms. Their transforms converge in \(L^q\) to \(\mathcal F_pf\) and in \(L^2\) to \(\mathcal Ff\). Select a common subsequence whose errors to these two limits have summable respective norms; Lemma 0.1 makes both limits agree almost everywhere. The endpoints have the stated agreements by their definitions and Theorem 1.1. This proves all assertions for arbitrary LCA groups. \(\square\)

## Scope and continuation

Plancherel, both convolution formulas, the Fourier-algebra factorization and Hausdorff–Young have been proved here. The free-source routes are [Fremlin, §§445R–T](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex) for isometry, surjectivity, Parseval multiplication and localized frequency support, and [Tao, Theorem 21](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/) for the simple-function interpolation family. Lemma 7.0 proves its scalar estimate directly from the earlier exponential-series and circle-integration results.

The next lesson proves Pontryagin duality and general Fourier uniqueness. No identification of \(G\) with its bidual has been used here.

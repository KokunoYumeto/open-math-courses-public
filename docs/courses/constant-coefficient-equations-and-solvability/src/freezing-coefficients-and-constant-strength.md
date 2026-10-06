# Freezing coefficients without losing strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A variable-coefficient equation can behave locally like a fixed polynomial equation even when it is not elliptic. The useful hypothesis is that freezing the coefficients at different points always gives operators of equal strength. This lesson turns that hypothesis into a finite perturbation problem. Continuous coefficients suffice for an \(L^2\) inverse. Smooth coefficients give one neighborhood and one inverse that work for every moderate Fourier weight.

Read [Operator strength and local inverses](operator-strength-and-local-inverses.md), Theorem 4.1, and [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), Sections 1–3, first. We use the slowly moving weights, cutoffs, convolution and duality proved in [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), Theorems 2.1, 4.1 and 5.1 and Proposition 4.2, and the modulation and local-space estimates in [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). The kernel section uses [Distributions as kernels of continuous operators](../prerequisites/distributions-as-kernels.html#the-local-kernel-theorem), Lemma 3.1 and Theorem 4.1, and the Fourier definition of a wave front set with its usual cutoff stability, recalled in the opening of [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md). Melrose [Melrose], Grubb's exact free Fourier chapter [Grubb] and Mantlik [Mantlik] give background; the local inverse, strength and opposite-covector arguments are proved in the linked lessons and below.

## A finite space of allowable symbols

Let
\[
A(x,D)=\sum_{|\alpha|\leq m}a_\alpha(x)D^\alpha
\]
on an open set \(U\). We say that \(A\) has **constant strength** if every frozen polynomial \(A(x,\xi)\) is nonzero and every pair \(A(x,\cdot),A(y,\cdot)\) has equal strength. The comparison constants may initially depend on the pair of points. This is a condition in the given affine coordinates.

Fix \(x_0\in U\), put \(P(\xi)=A(x_0,\xi)\), and let \(W_P\) be the finite-dimensional space of polynomials weaker than \(P\). Choose a basis \(Q_1,\ldots,Q_N\) of that space.

**Lemma 1.1.** There are unique coefficient functions \(b_\nu\) such that
\[
A(x,D)=P(D)+\sum_{\nu=1}^N b_\nu(x)Q_\nu(D),
\qquad b_\nu(x_0)=0.
\tag{1}
\]
They have the same continuity and differentiability as the original coefficients. If the coefficients are continuous, the frozen strength comparisons with \(P\) can be chosen uniformly on a sufficiently small neighborhood of \(x_0\).

**Proof.** Every \(A(x,\cdot)-P\) belongs to \(W_P\). Its basis coordinates are fixed linear functions of its polynomial coefficients. This proves existence, uniqueness, regularity, and the vanishing at \(x_0\). For the final assertion, let \(C_\nu\) satisfy \(S_{Q_\nu}\leq C_\nu S_P\). The derivative-vector triangle inequality gives
\[
|S_{A(x)}(\xi)-S_P(\xi)|
\leq\sum_\nu |b_\nu(x)|S_{Q_\nu}(\xi)
\leq\left(\sum_\nu C_\nu|b_\nu(x)|\right)S_P(\xi).
\]
The coefficient in parentheses tends to zero. Make it less than \(1/2\) to get uniform two-sided bounds. \(\square\)

**Example 1.2.** The operators
\[
A(x,D)=D_1^2+iD_2+b(x)D_1+c(x)
\tag{2}
\]
have constant strength for arbitrary scalar coefficient functions \(b,c\). The highest homogeneous part \(\xi_1^2\) is not of principal type in two variables: its gradient vanishes at \((0,1)\). Nevertheless, the added terms are dominated by \(P(\xi)=\xi_1^2+i\xi_2\), since \(\xi_1=\tfrac12\partial_1P\) and \(1=-i\partial_2P\), and every positive-order symbol derivative is dominated by its symbol. The stable-strength lemma gives the claimed equivalence at each point. No ellipticity in two variables is asserted.

## Continuous coefficients: the correct meaning of the equation

For continuous \(b_\nu\), the expression \(b_\nu Q_\nu(D)u\) is not defined for an arbitrary distribution \(u\). We instead use the domain
\[
\mathcal H_P(X)=\{u\in L^2(X):Q_\nu(D)u\in L^2(X)
\text{ for every }\nu\}.
\tag{3}
\]
The derivatives in (3) are distributional derivatives represented by \(L^2\) functions. Since the \(Q_\nu\) form a basis of \(W_P\), this domain does not depend on the chosen basis. It includes \(P(D)u\in L^2\), because \(P\in W_P\). On a set where all \(b_\nu\) are bounded, (1) defines \(Au\) as an \(L^2\) function for \(u\in\mathcal H_P(X)\).

**Theorem 2.1.** Suppose \(A\) has continuous coefficients and constant strength near \(x_0\). There is an open neighborhood \(X\) of \(x_0\) and a bounded linear map
\[
T_A:L^2(X)\longrightarrow\mathcal H_P(X)
\]
such that
\[
AT_Af=f\qquad(f\in L^2(X)).
\tag{4}
\]
Every \(Q(D)T_A\), with \(Q\prec P\), is bounded on \(L^2(X)\). Also
\[
T_AAu=u\qquad(u\in C_c^\infty(X)).
\tag{5}
\]
The norm on the target in the displayed map is the graph norm \(\|u\|_2+\sum_\nu\|Q_\nu(D)u\|_2\).

**Proof.** Choose a bounded neighborhood \(U_0\) with closure in the region of continuous constant strength. The constant-coefficient inverse construction supplies an inverse \(T_X\) for \(P(D)\) on every open \(X\subset U_0\), with
\[
\|Q_\nu(D)T_X\|_{L^2(X)\to L^2(X)}\leq M_\nu
\tag{6}
\]
independent of \(X\). To see that uniformity directly, use one regular fundamental solution and one cutoff equal to one near \(\overline{U_0}-\overline{U_0}\) in the proof of the bounded inverse theorem. The multiplier bounds then stay the same for every smaller set.

On \(L^2(X)\), define
\[
R_Xf=\sum_\nu b_\nu Q_\nu(D)T_Xf.
\]
Continuity and \(b_\nu(x_0)=0\) allow a small \(X\) with
\[
\|R_X\|\leq\sum_\nu M_\nu\|b_\nu\|_{L^\infty(X)}<\tfrac12.
\]
Set \(T_A=T_X(I+R_X)^{-1}\). The inverse is given by a norm-convergent Neumann series. The identity \(P(D)T_X=I\) gives
\[
AT_Xg=(I+R_X)g,
\]
with every term interpreted in \(L^2\). This proves (4) and the graph-norm bound. Any weaker \(Q\) is a linear combination of the basis polynomials, proving its derivative bound as well.

If \(u\in C_c^\infty(X)\), the constant inverse satisfies \(T_XP(D)u=u\). Hence
\[
(I+R_X)P(D)u=P(D)u+\sum_\nu b_\nu Q_\nu(D)u=Au.
\]
Uniqueness of the Neumann-series inverse yields \((I+R_X)^{-1}Au=P(D)u\). Applying \(T_X\) proves (5). \(\square\)

This result permits merely continuous coefficients because it first controls the needed derivatives as functions. It never multiplies an arbitrary distribution by a continuous function. Smooth test functions in (5) are a safe left-inverse domain under this coefficient hypothesis.

## Smooth cutoffs that make all weights work

For smooth coefficients, the same small neighborhood can work for every \(p\) and every moderate weight. The neighborhood must be chosen before the weight. Two estimates make this possible.

Write
\[
\|h\|_{1,1}=(2\pi)^{-n}\int|\widehat h(\xi)|\,d\xi
\]
for the unweighted Fourier \(L^1\) norm.

**Lemma 3.1.** Let \(k\) be moderate and let
\[
k_\delta(\xi)=\sup_y e^{-\delta|y|}k(\xi-y).
\]
For any fixed \(h\in\mathcal S\), there is \(\delta_0>0\) such that, for \(0<\delta<\delta_0\),
\[
\|hu\|_{p,k_\delta}\leq2\|h\|_{1,1}\|u\|_{p,k_\delta}
\qquad(1\leq p\leq\infty).
\tag{7}
\]
If \(h=0\), the assertion is immediate.

**Proof.** The cutoff estimate bounds the multiplier norm by
\((2\pi)^{-n}\int M_{k_\delta}(\eta)|\widehat h(\eta)|\,d\eta\).
The shift functions tend to one pointwise as \(\delta\downarrow0\). They are bounded by the original polynomial shift bound for \(k\). Dominated convergence makes the integral tend to \(\|h\|_{1,1}\), proving (7). For finitely many multipliers, take the minimum of their allowable \(\delta_0\)'s. The weights \(k,k_\delta\) are equivalent, although that equivalence constant may depend on \(k,\delta\). \(\square\)

**Lemma 3.2.** Fix \(w\in C_c^\infty\) and put \(w_r(x)=w((x-x_0)/r)\). If \(b\) is smooth near \(x_0\) and \(b(x_0)=0\), then
\[
\|w_rb\|_{1,1}\leq Cr
\quad\hbox{for all sufficiently small }r>0.
\tag{8}
\]

**Proof.** After translation, take \(x_0=0\). On a fixed neighborhood,
\[
b(x)=\sum_{j=1}^n x_j b_j(x),
\qquad b_j(x)=\int_0^1\partial_jb(tx)\,dt.
\]
Multiply the \(b_j\)'s by a fixed cutoff equal to one near all small supports of \(w_r\), giving fixed compactly supported smooth functions \(\widetilde b_j\). The Fourier \(L^1\) norm is submultiplicative under multiplication. Scaling the transform gives
\[
\|x_jw(x/r)\|_{1,1}=r\|x_jw(x)\|_{1,1}.
\]
Thus \(\|w_rb\|_{1,1}\leq r\sum_j\|x_jw\|_{1,1}\|\widetilde b_j\|_{1,1}\), proving (8). \(\square\)

## One inverse for every weighted scale

**Theorem 4.1.** Suppose \(A\) has smooth coefficients and constant strength near \(x_0\). There is a neighborhood \(X\) and a linear map
\[
E_A:\mathcal E'(\mathbb R^n)\longrightarrow\mathcal E'(\mathbb R^n)
\]
with the following properties:
\[
AE_Af=f\quad\hbox{in }X,\qquad f\in\mathcal E'(\mathbb R^n),
\tag{9}
\]
\[
E_AAu=u\quad\hbox{in }X,\qquad u\in\mathcal E'(X),
\tag{10}
\]
and, for every moderate \(k\) and \(1\leq p\leq\infty\),
\[
\|E_Af\|_{p,kS_P}\leq C_{p,k}\|f\|_{p,k},
\qquad f\in\mathcal E'\cap B_{p,k}.
\tag{11}
\]
The neighborhood and the map are independent of \(p,k\). In particular every \(Q(D)E_A\), with \(Q\prec P\), is bounded from \(\mathcal E'\cap B_{p,k}\) to \(B_{p,k}\).

**Proof.** Choose a ball \(U_0\) around \(x_0\) whose closure stays in the coefficient neighborhood. Let \(E_0\) be a regular fundamental solution of \(P(D)\), and choose \(\psi\in C_c^\infty\) equal to one near \(\overline{U_0}-\overline{U_0}\). Put \(F=\psi E_0\). Thus \(F\in\mathcal E'\cap B_{\infty,S_P}\). For \(g\in\mathcal E'(U_0)\),
\[
P(D)(F*g)=g\quad\hbox{in }U_0,
\qquad F*P(D)g=g\quad\hbox{in }U_0.
\tag{12}
\]
Both identities follow by replacing \(F\) by \(E_0\) on the relevant differences of supports.

Choose \(w\in C_c^\infty\) equal to one near the closed unit ball, with support in the ball of radius two, and take \(r\) small enough that \(\operatorname{supp}w_r\subset U_0\). Define
\[
K_rg=\sum_\nu w_rb_\nu\,Q_\nu(D)(F*g).
\tag{13}
\]
The products \(w_rb_\nu\) are understood as global compactly supported smooth functions, extended by zero. Since
\[
M_\nu:=\sup_\xi|Q_\nu(\xi)\widehat F(\xi)|<\infty,
\]
the Fourier multiplier \(Q_\nu(D)F*\) has norm at most \(M_\nu\) in every \(B_{p,k}\), independently of the weight. Lemma 3.2 lets us fix \(r\), before choosing a weight, so that
\[
2\sum_\nu M_\nu\|w_rb_\nu\|_{1,1}<\tfrac12.
\tag{14}
\]
For a given \(k\), choose \(\delta\) in Lemma 3.1 for the finite set of multipliers \(w_rb_\nu\) and \(w_r\). Then (13)–(14) give
\[
\|K_rg\|_{p,k_\delta}\leq\tfrac12\|g\|_{p,k_\delta},
\qquad
\|w_rf\|_{p,k_\delta}\leq2\|w_r\|_{1,1}\|f\|_{p,k_\delta}.
\tag{15}
\]
Consequently
\[
g+K_rg=w_rf
\tag{16}
\]
has a unique solution in \(B_{p,k_\delta}=B_{p,k}\), with a bound in either equivalent norm. Equation (16) shows directly that \(g\) has support in the fixed compact set \(\operatorname{supp}w_r\).

Every compactly supported distribution belongs to some \(B_{\infty,\langle\xi\rangle^{-N}}\): its Fourier transform has polynomial growth. Thus (16) gives a compactly supported solution for every \(f\in\mathcal E'\). It is unique among all compactly supported distributions. Indeed a difference of two such solutions is a compact distribution in one of these sufficiently negative weighted spaces; choose its equivalent slow weight and apply the contraction estimate (15) to the homogeneous equation. The difference must be zero. Therefore solutions constructed using different \(p,k,\delta\) agree. This is the reason there is one map, rather than a separate inverse for each norm.

Define \(E_Af=F*g\), using this unique solution. It has compact support in \(\operatorname{supp}F+\operatorname{supp}w_r\), independent of \(f\). The convolution estimate gives
\[
\|F*g\|_{p,kS_P}\leq\|F\|_{\infty,S_P}\|g\|_{p,k}.
\]
Combining with (15) and equivalence of the weights proves (11). Let \(X\) be the ball of radius \(r\) about \(x_0\), reduced slightly if needed so that \(w_r=1\) on a neighborhood of its closure. On \(X\), (12) and (16) yield (9).

For \(u\in\mathcal E'(X)\), put \(g=P(D)u\). It has compact support in \(X\). By (12), \(F*g=u\) near \(\operatorname{supp}w_r\). Therefore the left side of (16) is
\[
P(D)u+w_r\sum_\nu b_\nu Q_\nu(D)u=w_rAu.
\]
In the last equality, \(w_r=1\) near the support of \(P(D)u\). Uniqueness in (16) identifies this \(g\) as the one used to define \(E_AAu\). Equation (12) now proves (10). Finally apply the differential-operator estimate and \(S_Q\leq CS_P\) to (11) for the weaker-derivative assertion. \(\square\)

**Corollary 4.2.** On the neighborhood in Theorem 4.1, if \(u\in\mathcal E'(X)\) and \(Au\in B_{p,k}\), then \(u\in B_{p,kS_P}\). Also every \(f\in C^\infty(X)\) has a smooth solution locally on a smaller neighborhood of \(x_0\).

**Proof.** For the first assertion, (10) agrees with \(u\) near its compact support. Use a cutoff equal to one there and the estimate (11). For the second, shrink to a neighborhood with closure in \(X\), multiply \(f\) by a cutoff supported in \(X\) and equal to one on the smaller neighborhood, and extend the resulting smooth function by zero. This compact smooth datum belongs to every \(B_{\infty,\langle\xi\rangle^j}\). Equation (11) and the positive lower bound for \(S_P\) put its image in every such weighted space as well. Their intersection is \(C^\infty\). Equation (9) gives the desired equation on the smaller neighborhood. \(\square\)

If \(f\) is a smooth function on all of \(\mathbb R^n\), the same construction gives a smooth solution on \(X\) itself, by applying \(E_A\) to a compact smooth extension equal to \(f\) near \(\operatorname{supp}w_r\).

## Transposition and composition preserve the strength

For smooth coefficients, define the formal transpose by the bilinear identity
\[
\int (Au)v\,dx=\int u(A^tv)\,dx
\]
when one factor has compact support. There is no coefficient conjugation in this convention.

**Theorem 5.1.** If \(A\) is smooth and has constant strength, then its formal transpose also has constant strength. At each point \(x\), its frozen polynomial has equal strength to \(A(x,-\xi)\).

**Proof.** In (1),
\[
A^t=P(-D)+\sum_\nu Q_\nu(-D)b_\nu.
\]
Expanding the products gives, at a fixed point \(x\),
\[
A^t(x,\xi)=A(x,-\xi)+
\sum_{\nu,\ |\alpha|\geq1}
\frac{(-D)^\alpha b_\nu(x)}{\alpha!}
(\partial_\xi^\alpha Q_\nu)(-\xi).
\tag{17}
\]
Reflection preserves weak comparison and domination. Each derivative polynomial in the correction is dominated by \(P(-\xi)\), hence by the equally strong \(A(x,-\xi)\). A finite linear combination is dominated too. The stable-strength lemma shows that (17) has the stated strength. Since the frozen polynomials \(A(x,-\xi)\) have equal strength at all points, so do those of \(A^t\). \(\square\)

Reflection in this statement matters. It is not always true that \(P(\xi)\) and \(P(-\xi)\) have equal strength.

**Theorem 5.2.** Let \(A(x,D)\) and \(B(x,D)\) have constant strength. If \(B\) has order \(r\) and the coefficients of \(A\) are \(C^r\), then the composed operator \(B(x,D)A(x,D)\) has constant strength. At each point its frozen polynomial has equal strength to the pointwise product \(B(x,\xi)A(x,\xi)\).

**Proof.** In a fixed weaker-polynomial basis for \(A\), every coefficient derivative \(D_x^\alpha A(x,\xi)\) is weaker than \(A(x,\xi)\). Leibniz's formula for the composition gives
\[
(BA)(x,\xi)=B(x,\xi)A(x,\xi)+
\sum_{|\alpha|\geq1}
\frac{1}{\alpha!}
(\partial_\xi^\alpha B)(x,\xi)(D_x^\alpha A)(x,\xi).
\tag{18}
\]
Only \(|\alpha|\leq r\) occur. The differentiated factor from \(B\) is dominated by \(B(x,\xi)\); the other factor is weaker than \(A(x,\xi)\). The product rule for domination shows that every correction in (18) is dominated by \(BA\)'s pointwise polynomial product. Apply the stable-strength lemma. Finally, the pointwise products have equal strength at different points by the product rule for weak comparison. \(\square\)

Nonlinear coordinate changes can destroy constant strength. For example, use the global change of coordinates \(y_1=x_1\), \(y_2=e^{x_1}x_2\). The constant operator \(\partial_{x_1}\) becomes \(\partial_{y_1}+y_2\partial_{y_2}\). Its frozen linear symbols have real active directions \((1,y_2)\), which differ as \(y_2\) varies. Two nonparallel first-order directions do not have equal strength. Thus the transformed operator is not of constant strength on any open set.

## The inverse kernel has opposite covectors

Let \(e(x,y)\) be the Schwartz kernel of \(E_A\). It exists because (11) with \(p=2,k=1\), and the lower bound for \(S_P\), give an \(L^2\) bound. In particular the restriction of \(E_A\) to test functions is continuous into distributions. Equations (9)–(10) imply, on \(X\times X\),
\[
A(x,D_x)e(x,y)=A^t(y,D_y)e(x,y)=\delta(x-y).
\tag{19}
\]
These identities follow by testing against products of test functions and then using the kernel theorem.

**Theorem 6.1.** The wave front set of this kernel satisfies
\[
(x,y;\xi,\eta)\in\operatorname{WF}(e)
\quad\Longrightarrow\quad\xi+\eta=0.
\tag{20}
\]
This constrains covectors. It does not require the spatial points \(x,y\) to agree.

**Proof.** Fix \(a,b\in C_c^\infty\), and let \(H\) be the Fourier transform of \(a(x)b(y)e(x,y)\). The weighted \(L^2\) bound in (11), after dropping the factor \(S_P\) using its lower bound, and the weighted \(L^2\) duality give
\[
|H(\xi,-\eta)|\leq C_k\,
\|b(y)e^{iy\cdot\eta}\|_{2,k}
\|\overline{a(x)}e^{ix\cdot\xi}\|_{2,1/k}
\leq C'_k\frac{k(\eta)}{k(\xi)}.
\tag{21}
\]
The last step uses the fixed-cutoff modulation estimate. Constants may depend on the chosen weight and cutoffs.

We prove rapid decrease outside any conic neighborhood of \(\xi=\eta\). If it failed, there would be some \(N\), some \(d>0\), and a sequence with total frequency tending to infinity such that
\[
|\xi_j-\eta_j|\geq d(|\xi_j|+|\eta_j|),
\qquad
|H(\xi_j,-\eta_j)|\geq(1+|\xi_j|+|\eta_j|)^{-N}.
\tag{22}
\]
Pass to one of the two cases \(|\eta_j|\leq|\xi_j|\) or \(|\xi_j|\leq|\eta_j|\). In the first, put \(R_j=1+|\xi_j|\). Take a subsequence so that \(R_j\to\infty\) and \(R_{j+1}\geq16R_j^2\). For a positive integer \(M\), define the weight
\[
k(z)=\max\left(1,\sup_j\frac{R_j^M}{(1+|z-\xi_j|)^M}\right).
\tag{23}
\]
It is finite everywhere: for fixed \(z\), all sufficiently late centers satisfy \(1+|z-\xi_j|\geq R_j/2\), while only finitely many earlier terms remain. Every term and the constant one have the same moderate shift bound \((1+|h|)^M\). Taking the supremum preserves that bound, so (23) is a positive moderate weight.

At the centers, \(k(\xi_j)\geq R_j^M\). At \(\eta_j\), the term with center \(\xi_j\) is bounded by a constant depending on \(d,M\), because of (22). All later centers contribute at most a fixed constant, since \(|\eta_j|\leq|\xi_j|\) and the centers grow rapidly. Every earlier term is at most \(R_{j-1}^M\leq R_j^{M/2}\). Therefore
\[
\frac{k(\eta_j)}{k(\xi_j)}\leq C R_j^{-M/2}.
\]
Choose \(M>2N\). Equation (21) contradicts the lower bound in (22). In the second case build the same peaked weight around the larger frequencies \(\eta_j\), and use its reciprocal in (21); the identical argument gives the contradiction.

Thus every product localization has rapid Fourier decrease away from the opposite-covector set. Choose \(a,b\) nonzero at any specified pair \((x,y)\); their product is a valid localizing function there. The Fourier definition of the wave front set yields (20). \(\square\)

The use of every moderate weight in (21) is essential to this proof. A fixed isotropic Sobolev scale cannot distinguish two large frequencies of the same length that point in different directions. The peaked weight separates them.

## Exercises with solutions

**Exercise 1 (entry).** In (2), freeze the coefficients at \(x_0\). Write the coefficient differences in a weaker-polynomial basis and identify the quantities that must be small for the \(L^2\) Neumann series.

**Solution.** The difference is \((b(x)-b(x_0))\xi_1+(c(x)-c(x_0))\). Both polynomials are weaker than the frozen symbol. The sufficient condition is
\[
M_1\|b-b(x_0)\|_{L^\infty(X)}+
M_2\|c-c(x_0)\|_{L^\infty(X)}<1,
\]
where \(M_1,M_2\) bound \(D_1T_X\) and \(T_X\) for the frozen inverse. Taking a bound below \(1/2\) gives the convenient inverse-norm estimate two. Continuity makes this possible on a small neighborhood.

**Exercise 2 (intermediate).** Explain why smoothness of the coefficients matters in Theorem 4.1 even though continuity suffices in Theorem 2.1.

**Solution.** The \(L^2\) proof uses the multiplication norm \(\|b_\nu\|_\infty\). For arbitrary Fourier weights we need multiplication by \(w_rb_\nu\) to be bounded on every \(B_{p,k}\), and we need its Fourier \(L^1\) norm to tend to zero independently of \(k\). Smoothness gives compactly supported smooth multipliers, the representation \(b_\nu(x)=\sum_j(x_j-x_{0,j})b_{\nu,j}(x)\), and estimate (8). A merely continuous multiplier need not have an integrable Fourier transform or preserve these spaces.

**Exercise 3 (intermediate).** Give a polynomial for which reflection changes strength. Check it on one explicit frequency sequence.

**Solution.** Take \(P(\xi_1,\xi_2)=\xi_1^2+\xi_2+i\). Along \((s,-s^2)\),
\[
S_P^2=4s^2+6,
\]
whereas \(P(-s,s^2)=2s^2+i\). Thus \(S_{P(-\cdot)}/S_P\) is unbounded on this sequence. The reflected polynomial is not weaker than \(P\), so they do not have equal strength. This is why Theorem 5.1 retains the reflected frozen symbol.

**Exercise 4 (advanced).** Can condition (20) imply that the inverse is a pseudodifferential operator with a kernel singular only on \(x=y\)? Use transport to decide.

**Solution.** It cannot. In two variables, an inverse for \(\partial_{x_1}\) has a convolution kernel supported on the forward \(x_1\)-ray, tensored with a delta in \(x_2\). Away from the origin along the ray it is smooth in \(x_1\) but remains singular normally in \(x_2\). The corresponding two-point kernel is singular at pairs with \(x_2=y_2\) and \(x_1>y_1\), including pairs with \(x\ne y\). Its two covectors are opposite because it depends on \(x-y\). Thus the covector restriction in (20) allows nonlocal propagation along a direction.

## References

- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, sections on distributions, kernels, and differential operators. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- [Grubb] Gerd Grubb, author-hosted lecture chapter §5, *Fourier transformation of distributions*, §§5.1–5.3, from the 2007–2008 lecture notes for *Distributions and Operators*. [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf). [Author's lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm). Fourier and tempered-distribution background; the strength and inverse proofs are supplied by the linked lessons and the present lesson.
- [Mantlik] Frank Mantlik, *Partial differential operators depending analytically on a parameter*, Annales de l'Institut Fourier **41** (1991), 577–599. [Original article](https://www.numdam.org/item/10.5802/aif.1266/).
- Internal kernel proof: [Distributions as kernels of continuous operators](../prerequisites/distributions-as-kernels.html#the-local-kernel-theorem), Sections 1–4, especially Lemma 3.1 (product tests) and Theorem 4.1 (the local Schwartz kernel theorem). The local inverse, transpose, composition and opposite-covector results are proved in Theorems 2.1 and 4.1–6.1 of this lesson.

# Trace densities and noncommutative integration

The same trace measures both the part of an operator that a cutoff discards and the size of a density that defines a normal functional. We first connect these two measurements. This gives a concrete complete space of integrable operators, rather than an abstract completion whose elements have not yet been identified. Complex interpolation then produces the other finite-exponent spaces. Their full duality theorem requires a separate construction: compatible densities on finite projections must be assembled into a closed operator, with its adjoint and its spectral tails checked before any global integral is written.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, estimate (18), Lemma 2.12, Theorem 2.13 and the following trace-GNS identification. Mathematical comparisons also include Fumio Hiai, [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1, §5](https://arxiv.org/abs/2004.02383v1), and Ricardo Correa da Silva, [*Lecture Notes on Noncommutative Lp-Spaces*, arXiv:1803.02390v1, §2.1](https://arxiv.org/abs/1803.02390v1). These references are mathematical antecedents and comparisons; their prose is not imported. The projection estimates and the measure algebra used here were established in **OA-MOD-MT**. The organization through cutoff sizes, a closed predual range and two local operator domains is independent of the source presentation.

## Finite pieces without a countability assumption

Let \(M\subseteq B(H)\) be a von Neumann algebra on an arbitrary complex Hilbert space, and let \(\tau\) be a faithful normal semifinite trace. All Hilbert inner products are linear in their first variable. We allow the zero algebra. No faithful normal state, separability, sigma-finiteness or finite value of \(\tau(1)\) is assumed.

Write \(S=S(M,\tau)\) for the complete measurable algebra from MT-08–12. Its elements are actual closed densely defined affiliated operators. A sum or product in \(S\) means the closure of the ordinary sum or product on the domains stated in MT-09. Its adjoint is the Hilbert space adjoint. Spectral functions and polar decompositions have their operator meanings. For \(h\in S_+\), the notation \(\tau(h)\) initially means the positive spectral integral of MT-13; no complex integral has yet been assigned to an arbitrary measurable operator.

Let \(\mathcal E\) be the projections of finite trace. MT-02 gives

\[
 \tau(e\vee f)\leq\tau(e)+\tau(f),\qquad e,f\in\mathcal E.
 \tag{TI.1}
\]

For every projection \(P\in M\),

\[
 P=\sup\{e\in\mathcal E:e\leq P\},\qquad
 \tau(P)=\sup_{e\in\mathcal E,\ e\leq P}\tau(e).
 \tag{TI.2}
\]

Here and below suprema of projections refer to their ranges, equivalently their strong increasing limits when the family is directed.

**Proof.** The finite subprojections of \(P\) are directed by (TI.1). Let their supremum be \(Q\), and suppose \(R=P-Q\ne0\). The bounded finite trace ideal \(\mathfrak m_\tau\) is ultraweakly dense by semifiniteness. Thus some \(x\in\mathfrak m_\tau\) has \(Rx\ne0\): otherwise ultraweak continuity of fixed multiplication would give \(R1=0\). The nonzero bounded positive element \(a=Rxx^*R\) belongs to \(\mathfrak m_\tau\), by its two-sided ideal property in MT-13. For some \(\delta>0\), the projection \(r=1_{[\delta,\infty)}(a)\) is nonzero. It satisfies \(r\leq R\) and \(\delta\tau(r)\leq\tau(a)<\infty\), contradicting the definition of \(Q\). Hence \(Q=P\), and normality gives the trace formula. \(\square\)

In particular, \(e\uparrow1\) strongly along \(\mathcal E\). This directed set is not replaced by a sequence. The algebra may have no sequence of finite projections with supremum one.

Let \(\mathfrak m_0\) consist of the bounded operators whose right support has finite trace. The polar partial isometry identifies their right and left supports, so either support can be used. This is a two-sided star ideal: multiplying on the left cannot enlarge the right support, multiplying on the right cannot enlarge the left support, and the support of a sum is bounded by the join of the corresponding supports. Every \(x\in\mathfrak m_0\) lies in a finite corner \(eMe\), by taking the join of its two supports. Moreover,

\[
 \mathfrak m_0\subseteq\mathfrak m_\tau,
 \qquad \tau(|x|^r)\leq\|x\|^r\tau(e)<\infty
 \quad(0<r<\infty, x=exe).
 \tag{TI.3}
\]

The corner used for a calculation may depend on all its finitely many factors.

## A scalar size function with exact operator cutoffs

For \(x\in S\), \(a\geq0\), and \(t>0\), define

\[
 d_x(a)=\tau(1_{(a,\infty)}(|x|)),\qquad
 \mu_t(x)=\inf\{\|xe\|: e\in\operatorname{Proj}(M),\ eH\subseteq D(x),\
                              \tau(1-e)\leq t\}.
 \tag{TI.4}
\]

The product in this infimum is literally bounded and everywhere defined: the closed graph theorem applies to the closed composition of \(x\) with \(e\), since its domain is all of \(H\). The infimum is finite by the spectral-tail criterion MT-11.

We claim the exact formula

\[
 \mu_t(x)=\inf\{a\geq0:d_x(a)\leq t\},\qquad
 \mu_t(x)\leq a\ \Longleftrightarrow\ d_x(a)\leq t.
 \tag{TI.5}
\]

To prove it, suppose \(eH\subseteq D(x)\) and \(\|xe\|\leq a\). The projection \(q=1_{(a,\infty)}(|x|)\) has zero intersection with \(e\). Indeed, a nonzero vector \(\xi\) in the intersection would satisfy

\[
 \|x\xi\|^2=\int_{(a,\infty)}\lambda^2\,
                   d\langle E_{|x|}(\lambda)\xi,\xi\rangle
                 >a^2\|\xi\|^2.
\]

This is impossible, including when \(a=0\). Projection comparison MT-02 gives \(q\precsim1-e\), hence \(d_x(a)\leq\tau(1-e)\). Conversely, \(1_{[0,a]}(|x|)\) is an admissible cutoff of norm at most \(a\) and defect \(d_x(a)\). These implications prove the infimum formula. Normality gives \(d_x(a_n)\uparrow d_x(a)\) when \(a_n\downarrow a\). If the infimum is \(m\), the upper-set property gives \(d_x(m+1/n)\leq t\); the preceding increasing limit gives \(d_x(m)\leq t\). Thus the infimum is attained by the spectral cutoff at \(m\), and the second formula follows. This proof fixes the endpoints even at spectral atoms.

In particular, \(t\mapsto\mu_t(x)\) is a finite nonnegative decreasing measurable function on \((0,\infty)\). Measurable polar decomposition transports every nonzero spectral projection of \(|x|\) to the corresponding projection of \(|x^*|\). Equality of the traces of equivalent projections therefore gives

\[
 \mu_t(x^*)=\mu_t(x),\qquad \mu_t(cx)=|c|\mu_t(x)
 \quad(c\in\mathbb C).
 \tag{TI.6}
\]

The assertion for \(c=0\) is immediate.

For every real \(0<p<\infty\), put \(I_p(x)=\tau(|x|^p)\), allowing infinity. The power is measurable because its high spectral tails are those of \(|x|\) after the change of threshold. We have

\[
 I_p(x)=\int_0^\infty p a^{p-1}d_x(a)\,da
       =\int_0^\infty\mu_t(x)^p\,dt.
 \tag{TI.7}
\]

Here is a layer-cake argument valid without a sigma-finiteness assumption on the spectral measure. For a nonnegative simple function with finitely many disjoint level sets, the equality between its integral and the integral of the measures of its strict superlevel sets follows by finite addition of rectangles. Approximate any nonnegative function increasingly by such simple functions. Both integrals increase to the desired limits, so scalar monotone convergence proves the same identity for every measure. Apply this to \(\lambda^p\) and \(B\mapsto\tau(E_{|x|}(B))\) to obtain the first formula, substituting \(s=a^p\). Formula (TI.5) identifies

\[
 \{t>0:\mu_t(x)>a\}=\{t>0:t<d_x(a)\}.
\]

Its Lebesgue measure is \(d_x(a)\), even if infinite. The same layer-cake argument applied to \(\mu_t(x)^p\) proves the second formula. Infinite mass at spectral value zero contributes zero throughout.

For \(s,t>0\), the cutoff sizes obey

\[
 \begin{aligned}
 \mu_{s+t}(x+y)&\leq\mu_s(x)+\mu_t(y),\\
 \mu_{s+t}(xy)&\leq\mu_s(x)\mu_t(y),\\
 \mu_t(axb)&\leq\|a\|\|b\|\mu_t(x)\quad(a,b\in M).
 \end{aligned}
 \tag{TI.8}
\]

For the first inequality choose spectral cutoffs \(p,q\) attaining \(\mu_s(x),\mu_t(y)\). Their intersection has defect at most \(s+t\); its range belongs to both actual domains, and the closed sum agrees there with the ordinary sum. This proves the norm estimate. For the product set \(c=yq\in M\), let \(k\) be the kernel projection of \((1-p)c\), and put \(r=q\wedge k\). The left support of \((1-p)c\) is at most \(1-p\). Equivalence with its right support gives \(\tau(1-k)\leq s\), hence \(\tau(1-r)\leq s+t\). For \(\xi\in rH\), one has \(\xi\in D(y)\) and \(y\xi=c\xi\in pH\subseteq D(x)\). Thus \(rH\) lies in the ordinary product domain and

\[
 \|(xy)r\|=\|(xp)cr\|\leq\mu_s(x)\mu_t(y).
\]

This proves the second inequality without any commuting-cutoff assumption. Left multiplication by \(a\) uses the same cutoff as \(x\); right multiplication follows by adjoints and (TI.6). Iterating proves the third inequality. After integration, it gives \(I_p(axb)\leq\|a\|^p\|b\|^pI_p(x)\); zero bounded factors are treated directly.

## Fatou estimates and concrete approximation

The cutoffs in TI-02 describe exactly the measure topology already constructed in MT. To verify this explicitly, let \(\widetilde U(r,d)\) consist of \(x\in S\) for which some projection \(e\) satisfies \(eH\subseteq D(x)\), \(\|xe\|<r\), and \(\tau(1-e)<d\). Write \(U(r,d)\) for the original bounded neighborhood in MT-03.

If \(x\in\widetilde U(r,d)\), put \(y=x(1-e)\) in \(S\). Then \(ye=0\), so its positive absolute value vanishes on \(eH\). The bounded regularizations \(y_n=y(1+n^{-1}|y|)^{-1}\) also vanish on \(eH\), and converge to \(y\) in measure by MT-13. Therefore \(xe+y_n\in U(r,d)\) and converge to \(x\); this proves \(\widetilde U(r,d)\subseteq\overline{U(r,d)}\).

Conversely, if \(x\in\overline{U(r/2,d/2)}\), the countable base of the completed topology permits choosing \(a_n\in U(r/2,d/2)\) tending to \(x\) sufficiently fast that

\[
 a_{n+1}-a_n\in U(\varepsilon_n,\delta_n),\qquad
 \sum_n\varepsilon_n<r/2,\quad \sum_n\delta_n<d/2.
\]

This uses only the Cauchy criterion: prescribe these summable positive bounds, choose successively smaller neighborhoods of \(x\) whose pairwise differences lie in each required original neighborhood, and choose the approximants there. Intersect a witness for \(a_1\) with all witnesses for the displayed differences. The resulting projection \(e\) has \(\tau(1-e)<d\), and the telescoping sequence \(a_ne\) converges in norm to \(b\in M\) with \(\|b\|<r\). Continuity in the measure algebra gives \(a_ne\to xe\), while norm convergence also implies measure convergence. Hausdorffness gives \(xe=b\) in \(S\). The restriction statement of MT-08 then gives the actual domain inclusion \(eH\subseteq D(x)\) and literal bounded equality \(xe=b\). Thus

\[
 \overline{U(r/2,d/2)}\subseteq\widetilde U(r,d)
       \subseteq\overline{U(r,d)}.
\]

Closures of sufficiently small original neighborhoods form a base of neighborhoods in a uniform completion, by the addition estimate used to construct it. These inclusions prove the claimed equality of topologies. Together with attained cutoffs in (TI.5), they prove, for arbitrary nets,

\[
 x_i\to0\text{ in measure}\quad\Longleftrightarrow\quad
                  \mu_t(x_i)\to0\text{ for every }t>0.
 \tag{TI.9a}
\]

In the reverse direction use \(t=d/2\), leaving strict slack in the discarded trace. No sequence of indices is selected from the net.

We next prove spectral Fatou lower semicontinuity for every \(p>0\):

\[
 x_i\to x\text{ in measure}\quad\Longrightarrow\quad
                  I_p(x)\leq\liminf_i I_p(x_i).
 \tag{TI.9b}
\]

For fixed \(t,\varepsilon>0\), (TI.9a) supplies one tail on which \(\mu_t(x-x_i)\leq\varepsilon\). For all indices on this tail, (TI.8) holds simultaneously for all \(s>0\), giving

\[
 I_p(x_i)\geq\int_t^\infty
                 (\mu_u(x)-\varepsilon)_+^p\,du.
\]

The right side is independent of \(i\). It is therefore a lower bound for the directed liminf \(\sup_{i_0}\inf_{i\geq i_0}I_p(x_i)\). Let \(\varepsilon\downarrow0\) and then \(t\downarrow0\) through scalar sequences. Monotone convergence and (TI.7) prove (TI.9b). This is not an application of a scalar Fatou lemma to an arbitrary net of functions; the uniformity of the chosen tail in the integration variable is essential.

Before asserting a norm triangle inequality, the sets \(\{x:I_p(x)<\infty\}\) are already vector spaces and bounded bimodules. Indeed, (TI.8), the substitution \(u=2t\), and the scalar inequality \((a+b)^p\leq\max(1,2^{p-1})(a^p+b^p)\) give

\[
 I_p(x+y)\leq2^{\max(1,p)}(I_p(x)+I_p(y)).
 \tag{TI.9c}
\]

For \(p\geq1\) the scalar inequality is convexity at the midpoint; for \(p\leq1\), divide by \((a+b)^p\) and use \(r^p\geq r\) on \([0,1]\). Spectral calculus gives homogeneity and, for \(a>0\), the Markov estimate

\[
 a^p d_x(a)\leq I_p(x),\qquad
 \mu_t(x)\leq t^{-1/p}I_p(x)^{1/p}
                  \quad(I_p(x)<\infty).
 \tag{TI.9d}
\]

If \(I_p(x)=0\), faithfulness makes all strictly positive spectral tails zero, hence \(x=0\). Otherwise (TI.5) gives the second estimate from the first. Thus convergence of the gauges to zero implies convergence in measure.

Finally, if \(x=vh\) and \(I_p(x)<\infty\), let \(e_n=1_{[1/n,n]}(h)\), \(x_n=xe_n\). The bound \(\tau(e_n)\leq n^pI_p(x)\) makes \(x_n\) a bounded finite-support operator. The closed spectral identity \(|x-x_n|=h(1-e_n)\) gives

\[
 I_p(x-x_n)=\int\lambda^p1_{[0,\infty)\setminus[1/n,n]}(\lambda)
                            \,d(\tau\circ E_h)(\lambda)\longrightarrow0.
 \tag{TI.9e}
\]

The majorant has finite integral, so this is ordinary scalar dominated convergence. Equivalently subtract the increasing integrals on the annuli from their finite limit. These projections exhaust only the support of this particular \(h\). They do not give a countable finite-trace exhaustion of the identity.

## Bounded densities already carry their exact norm

For \(x\in\mathfrak m_\tau\), put

\[
 J_0(x)(a)=\tau(xa),\qquad a\in M.
 \tag{TI.10}
\]

Every trace in this formula is defined on the bounded finite trace ideal. We have

\[
 J_0(x)\in M_*,\qquad
 \|J_0(x)\|=\tau(|x|),\qquad
 |\tau(xa)|\leq\|a\|\tau(|x|).
 \tag{TI.11}
\]

**Proof of the bound and norm.** The two nonnegative trace factors in MT.25 obey

\[
 \tau(|x^*|\,|a|)\leq\|a\|\tau(|x^*|),\qquad
 \tau(|x|\,|a^*|)\leq\|a\|\tau(|x|).
\]

For example the first written trace equals the trace of the positive sandwich \(|x^*|^{1/2}|a||x^*|^{1/2}\), bounded above by \(\|a\||x^*|\). If \(x=v|x|\), bounded traciality gives \(\tau(|x^*|)=\tau(v|x|v^*)=\tau(|x|)\), with zero on the complement of the final support. MT.25 therefore proves the last inequality in (TI.11). Conversely, the contraction \(v^*\) gives

\[
 J_0(x)(v^*)=\tau(v|x|v^*)=\tau(|x|).
\]

For \(x=0\), both sides of the norm equality are zero.

**Proof of normality.** If \(h\in\mathfrak m_\tau^+\), cyclicity gives

\[
 J_0(h)(a)=\tau(h^{1/2}a h^{1/2})\quad(a\in M).
\]

This is a positive functional. For a bounded increasing net \(a_i\uparrow a\) in \(M_+\), its sandwiches increase to \(h^{1/2}a h^{1/2}\), so normality of the trace gives \(J_0(h)(a_i)\uparrow J_0(h)(a)\). The bounded order-normal-to-predual implication of NW-11, specialized through the final argument of CP-12, therefore places it in \(M_*^+\). Alternatively this functional is the vector functional of the normal trace-GNS representation at \(\Lambda_\tau(h^{1/2})\).

To pass from positive densities to all \(x\), take its self-adjoint real and imaginary parts. They belong to the star ideal \(\mathfrak m_\tau\). If \(b=b^*\) belongs to that ideal, its bounded polar decomposition puts \(|b|\) in the ideal, and then \(b_\pm=(|b|\pm b)/2\) are finite positive elements. Thus \(x\) is a complex linear combination of four finite positive densities. This proves normality of \(J_0(x)\). \(\square\)

Consequently \(\|x\|_1=\tau(|x|)\) is a norm on \(\mathfrak m_\tau\): linearity of \(J_0\) gives the triangle inequality, and faithfulness makes its kernel zero. This is a norm statement on the bounded ideal, before a completion is used.

## A complete space of actual integrable operators

Define

\[
 L^1(M,\tau)=\{x\in S:\tau(|x|)<\infty\},
 \qquad \|x\|_1=\tau(|x|).
 \tag{TI.12}
\]

This set is a complex vector space and a two-sided \(M\)-module. Its gauge is a complete norm, involution is isometric, and

\[
 \|axb\|_1\leq\|a\|\,\|x\|_1\,\|b\|
 \quad(a,b\in M, x\in L^1).
 \tag{TI.13}
\]

The ideal \(\mathfrak m_0\), and hence \(\mathfrak m_\tau\), is dense in this norm.

**Proof.** We use the cutoff inequalities and spectral Fatou theorem in TI-02–03. If \(x=v h\in L^1\), set

\[
 p_n=1_{[1/n,n]}(h),\qquad x_n=xp_n.
 \tag{TI.14}
\]

Then \(\tau(p_n)\leq n\tau(h)\), \(x_n\in\mathfrak m_0\), and the closed spectral product gives

\[
 |x-x_n|=h(1-p_n),\qquad
 \|x-x_n\|_1=\int t\,1_{[0,\infty)\setminus[1/n,n]}(t)\,
                   d(\tau\circ E_h)(t)\longrightarrow0.
 \tag{TI.15}
\]

The conclusion follows by scalar dominated convergence against the finite integral of \(t\); the possible infinite mass at zero contributes zero. Also \(x_n\to x\) in measure, by the bounded high spectral cutoffs of MT-11: on \(1_{[0,R]}(h)H\), the removed low part has norm at most \(1/n\) once \(n\geq R\).

For \(x,y\in L^1\), apply the bounded triangle inequality to their approximants and apply spectral Fatou to \(x_n+y_n\to x+y\) in measure. It gives

\[
 \tau(|x+y|)\leq\liminf_n\tau(|x_n+y_n|)
 \leq\|x\|_1+\|y\|_1.
\]

Scalar homogeneity follows from the spectral integral; faithfulness proves definiteness. Thus the displayed measurable set is a normed vector space. The cutoff module inequalities in TI-02 give (TI.13) directly after integration. The equality of the nonzero spectral distribution functions of \(|x|\) and \(|x^*|\) gives the star isometry.

If \((z_n)\) is Cauchy in this norm, the spectral Markov estimate

\[
 \tau(1_{(r,\infty)}(|z_n-z_m|))
 \leq r^{-1}\|z_n-z_m\|_1
\]

makes it Cauchy in measure. Completeness of \(S\) supplies a measurable limit \(z\). For fixed \(n\), Fatou gives

\[
 \|z_n-z\|_1\leq\liminf_m\|z_n-z_m\|_1.
 \tag{TI.16}
\]

The right side tends to zero as \(n\to\infty\). It is finite for each sufficiently large \(n\), so \(z=z_n+(z-z_n)\in L^1\). This proves completeness of the actual measurable set. Density was proved by (TI.14)–(TI.15). \(\square\)

The abstract completion of \((\mathfrak m_\tau,\|\cdot\|_1)\) therefore identifies isometrically with (TI.12). More explicitly, send a norm-Cauchy sequence to its measure limit. Inequality (TI.16) proves that its norm limit is that operator and that a sequence whose measure limit is zero has norm limit zero. This proves injectivity of the completion map; spectral approximation proves that its image is all of (TI.12).

The bounded resolvent regularizations from MT-13 also approximate in this norm. For \(\varepsilon>0\), put \(x_\varepsilon=v h(1+\varepsilon h)^{-1}\). Their bounded positive absolute values have finite trace, so \(x_\varepsilon\in\mathfrak m_\tau\). The polar support is unchanged on the positive spectrum, and

\[
 |x-x_\varepsilon|=h-h(1+\varepsilon h)^{-1},\qquad
 \|x-x_\varepsilon\|_1\longrightarrow0,
 \qquad \|x_\varepsilon\|_1\longrightarrow\|x\|_1.
 \tag{TI.17}
\]

These are scalar spectral monotone/dominated convergence statements with finite majorant \(h\). They do not identify a completion by themselves; that identification was already proved above.

## The trace pairing fills the whole predual

The finite trace extends uniquely to a continuous complex-linear functional on \(L^1\), still denoted by \(\tau\), with

\[
 |\tau(x)|\leq\|x\|_1,\qquad
 \tau(ax)=\tau(xa),\qquad
 \tau(x^*)=\overline{\tau(x)}
 \quad(x\in L^1, a\in M).
 \tag{TI.18}
\]

For positive integrable \(x\) this functional equals the positive spectral integral. The map

\[
 J:L^1\longrightarrow M_*,\qquad
 J(x)(a)=\tau(xa),
 \tag{TI.19}
\]

is an onto complex-linear isometry and identifies the two positive cones.

**Extension and injection.** Equation (TI.11) with \(a=1\) gives the continuous scalar extension from the dense bounded ideal. Approximate \(x\) by (TI.14); the bounded module estimate, star isometry and bounded cyclicity pass to the norm limit and prove (TI.18). For \(x\geq0\), its positive spectral approximants have traces increasing to the original positive integral, so the two meanings of \(\tau(x)\) agree. Similarly, \(J_0(x_n)\) converges in predual norm, since \(J_0\) is an isometry on the bounded ideal. Norm closure of \(M_*\) in \(M^*\), proved in CP-06–07, puts the limit in \(M_*\). Equations (TI.13) and (TI.18) identify that limit with (TI.19), and the norm equality passes to the limit. Hence \(J\) is an isometry with a closed range, since \(L^1\) is complete.

**Surjection.** Suppose this closed range were proper in \(M_*\). The complex Hahn–Banach theorem, in the exact normed-space form used in CP-01, would give a nonzero element of \((M_*)^*\) annihilating it: define a nonzero functional on the span of one nonzero coset in \(M_*/J(L^1)\), extend there by Hahn–Banach, and pull back through the quotient. CP-06 identifies \((M_*)^*\) isometrically with \(M\). Thus some nonzero \(a\in M\) would satisfy \(\tau(xa)=0\) for every \(x\in L^1\). In particular, for \(e\in\mathcal E\), the bounded finite-support operator \(x=ea^*\) gives

\[
 0=\tau(ea^*a)=\tau(aea^*)=\tau((ae)(ae)^*).
\]

Faithfulness gives \(ae=0\). Since \(e\uparrow1\) strongly by TI-01, this implies \(a=0\), a contradiction. Therefore (TI.19) is onto. This proof treats complex functionals directly, without first assuming a density theorem for faithful weights or a polar-decomposition theorem for normal functionals.

**Positive cones.** If \(h\in L^1_+\), the positive bounded approximants in (TI.14) show that \(J(h)\) is positive. Conversely, suppose \(J(x)\) is positive. Equation (TI.18) and injectivity imply \(x=x^*\). The spectral bands \(e_n=1_{[-n,-1/n]}(x)\) have finite trace, since \(x\in L^1\). Positivity and spectral calculus give

\[
 0\leq J(x)(e_n)=\tau(xe_n)\leq-\frac1n\tau(e_n).
\]

Thus every \(e_n\) is zero, by faithfulness, and the negative spectral projection of \(x\) is zero. Hence \(x\geq0\). Uniqueness follows from injectivity. In particular, every \(\varphi\in M_*^+\), faithful or not, has a unique measurable positive density \(h\) with

\[
 \varphi(a)=\tau(ha)\quad(a\in M),\qquad
 \tau(h)=\varphi(1)=\|\varphi\|.
 \tag{TI.20}
\]

The zero functional has density zero. No nonsingularity condition was imposed on \(h\). If \(x=v|x|\) is its measurable polar decomposition, cyclicity gives the useful precise factorization \(J(x)(a)=J(|x|)(av)\); the positive density vanishes outside the initial support of \(v\). \(\square\)

## Infinite positive integrals remain additive

For all \(a,b\in S_+\), \(\lambda\geq0\), and \(x\in S\),

\[
 \tau(a+b)=\tau(a)+\tau(b),\qquad
 \tau(\lambda a)=\lambda\tau(a),\qquad
 \tau(x^*x)=\tau(xx^*).
 \tag{TI.21}
\]

The convention in the middle formula is \(0\cdot\infty=0\). The sum is the positive self-adjoint measurable sum from MT-12. These statements allow infinite values.

**Positive order first.** Suppose \(a,b\in S_+\) and \(b-a\in S_+\). For \(r>0\), \(R>r\), set \(P_R=1_{(r,R]}(a)\) and \(Q=1_{[0,r]}(b)\). A vector in \((P_R\wedge Q)H\) lies in both operator domains. On their common domain, the measurable difference agrees with the ordinary difference. Its positivity would give

\[
 r\|\xi\|^2<\langle a\xi,\xi\rangle
 \leq\langle b\xi,\xi\rangle\leq r\|\xi\|^2
\]

for every nonzero such vector. Thus \(P_R\wedge Q=0\), and the projection comparison MT-02 gives \(\tau(P_R)\leq\tau(1-Q)\). Increasing \(R\) yields

\[
 \tau(1_{(r,\infty)}(a))\leq
 \tau(1_{(r,\infty)}(b)).
\]

Integrating these distributions, as in TI-02, proves \(\tau(a)\leq\tau(b)\). This argument uses bounded spectral bands where both actual domains are available; it does not assert an unproved resolvent-order rule for unbounded operators.

Since \(0\leq a,b\leq a+b\) in this measurable order, finiteness of \(\tau(a+b)\) forces both summands to be integrable. If both have finite trace, TI-05–06 give additivity in the linear space \(L^1\). If either has infinite trace, order forces the sum's trace to be infinite. This proves the first equality in all cases without subtracting infinite numbers. Scalar spectral calculus proves homogeneity, including zero.

Finally write \(x=v h\). The positive operators \(x^*x=h^2\) and \(xx^*=v h^2v^*\) have their nonzero spectral projections transported by \(v\). The bounded trace gives equal trace to each pair of such projections. Integration against their equal distributions proves the last equality. Equivalently, bounded spectral truncations and bounded cyclicity give equality before taking the increasing positive integral limits. Zero-support projections contribute zero. \(\square\)

## Sharp trace estimates from finite corners

The scalar size function has already supplied the bounded module estimates. We now prove the sharp trace inequality without assuming a triangle inequality for the other exponents. For \(1\leq p<\infty\), abbreviate the existing homogeneous gauge by \(N_p(x)=I_p(x)^{1/p}\), and put \(N_\infty(a)=\|a\|\) for \(a\in M\). Every finite collection of elements of \(\mathfrak m_0\) lies in one corner \(eMe\) with \(\tau(e)<\infty\): take the join of their finitely many left and right supports, using TI-01. Such corners will be used only for finite calculations.

**A scalar strip estimate.** Let \(F\) be an entire scalar function bounded on the closed strip \(0\leq\operatorname{Re}z\leq1\), and suppose

\[
 |F(it)|\leq M_0,\qquad |F(1+it)|\leq M_1
 \quad(t\in\mathbb R).
\]

Then

\[
 |F(\theta)|\leq M_0^{1-\theta}M_1^\theta
 \quad(0<\theta<1).
 \tag{TI.22}
\]

Here is the complete scalar argument needed for our analytic families. First suppose \(M_0,M_1>0\). For \(\delta>0\), form the entire function

\[
 G_\delta(z)=F(z)\exp\bigl(\delta(z^2-z)
                  -(1-z)\log M_0-z\log M_1\bigr).
\]

On either vertical boundary, its modulus is at most \(\exp(-\delta t^2)\leq1\). If \(C\) bounds \(|F|\) on the strip, then, for \(0\leq s\leq1\),

\[
 |G_\delta(s\pm iR)|
 \leq C\max(M_0^{-1},M_1^{-1})e^{-\delta R^2},
\]

because \(s^2-s\leq0\). Thus, for all sufficiently large \(R\), the four edges of the rectangle have modulus at most one. The maximum-modulus principle gives the same bound throughout the rectangle.

The precise maximum-modulus fact just used follows directly from local power series. A nonconstant analytic function attaining a positive local modulus maximum at \(z_0\) has an expansion

\[
 a_0+a_m(z-z_0)^m+O(|z-z_0|^{m+1}),
\]

where \(a_0\ne0\) and \(m\) is the first nonzero higher coefficient. Choose the direction of \(z-z_0\) so that \(a_m(z-z_0)^m\) has the same argument as \(a_0\). For sufficiently small positive radius, the modulus then exceeds \(|a_0|\), a contradiction. A zero local maximum forces the function to vanish nearby. If all higher coefficients vanish, the function is locally constant; overlapping disks propagate this constant throughout the connected rectangle. Continuity on the compact rectangle therefore places its maximum on the boundary unless it is constant, which gives the same conclusion. The functions used here are entire power-series functions, so no analytic continuation across a strip boundary is being assumed.

At \(\theta\), the resulting inequality reads

\[
 |F(\theta)|\leq M_0^{1-\theta}M_1^\theta
                      e^{\delta\theta(1-\theta)}.
\]

Let \(\delta\downarrow0\). If either boundary bound is zero, apply the proved inequality with the positive bounds \(M_j+\eta\) and let \(\eta\downarrow0\). This proves (TI.22), including those cases.

**Powers, supports and logarithms.** Fix a nonzero finite-trace projection \(e\). The restriction of \(\tau\) to \(eMe\) is a bounded positive trace with norm \(\tau(e)\); in particular,

\[
 |\tau(c)|\leq\tau(e)\|c\|\quad(c\in eMe).
 \tag{TI.23a}
\]

This also follows from TI-04 and \(|c|\leq\|c\|e\). If \(A\) is positive and invertible in \(eMe\), then \(\log A\) is bounded and self-adjoint on \(eH\). Define \(A^z=\exp(z\log A)\) in this corner. The exponential series converges in operator norm uniformly on compact subsets of the complex plane. Consequently \(A^z\) is entire as an operator-valued function, and functional calculus gives

\[
 A^{z+w}=A^zA^w,\qquad A^{it}\text{ is unitary on }eH,
 \qquad \|A^{s+it}\|=\|A^s\|.
 \tag{TI.23b}
\]

Every finite product of these powers and fixed corner contractions is norm bounded on a closed vertical strip when the real powers range over compact intervals. Applying the bounded functional \(\tau\) produces an entire scalar function bounded on the strip. Each value lies in \(eMe\), hence in the bounded finite trace domain.

Supported powers have an equally precise meaning. If \(c\geq0\) has support \(f\leq e\) and is bounded below by a positive constant on \(fH\), define \(c^z\) by \(\exp(z\log(c|_{fH}))\) on \(fH\), and by zero on \((e-f)H\). This is an entire \(eMe\)-valued function. Its imaginary powers are partial unitaries with both supports \(f\), of norm at most one, and \(c^0=f\). The logarithm is used only in \(fMf\). Powers belonging to distinct support projections can be multiplied as bounded operators; those projections need not commute.

To remove a lower spectral bound, we will use a common-corner regularization. For \(a=u|a|\in eMe\) and \(\varepsilon>0\), replace \(|a|\) by \(|a|+\varepsilon e\), retaining the original polar contraction \(u\). Then

\[
 u(|a|+\varepsilon e)\longrightarrow a\text{ in norm},\qquad
 \tau((|a|+\varepsilon e)^p)\longrightarrow\tau(|a|^p)
 \quad(0<p<\infty).
 \tag{TI.23c}
\]

The first error is at most \(\varepsilon\). For the second assertion, \((t+\varepsilon)^p\to t^p\) uniformly on the compact interval \([0,\|a\|+1]\); functional calculus and (TI.23a) give trace convergence. Thus no logarithm at zero is taken, no imaginary power is silently extended as the identity outside its support, and the extra corner mass introduced by regularization has finite trace and disappears in the limit.

**Conjugate trace Hölder on finite supports.** For \(1<p<\infty\), \(q=p/(p-1)\), and \(a,b\in\mathfrak m_0\),

\[
 |\tau(ab)|\leq N_p(a)N_q(b).
 \tag{TI.24a}
\]

At \(p=1,q=\infty\), this is the existing \(L^1\)-bounded-operator estimate, and the reverse endpoint follows by bounded cyclicity. At these endpoints the bounded partner may be any element of \(M\).

For the finite exponents, choose one finite corner containing \(a\) and \(b\). The zero corner is immediate. Write \(a=u|a|\), \(b=v|b|\), with \(u,v\) contractions in the corner. For \(\varepsilon>0\), put

\[
 A=\frac{|a|+\varepsilon e}
          {\tau((|a|+\varepsilon e)^p)^{1/p}},\qquad
 B=\frac{|b|+\varepsilon e}
          {\tau((|b|+\varepsilon e)^q)^{1/q}}.
\]

The denominators are positive by faithfulness and \(e\ne0\). Both operators are positive and invertible in the corner, with \(\tau(A^p)=\tau(B^q)=1\). Apply (TI.22), at \(\theta=1/p\), to

\[
 F(z)=\tau\bigl(uA^{pz}vB^{q(1-z)}\bigr).
 \tag{TI.24b}
\]

The preceding power argument verifies entire analyticity and boundedness on the whole closed strip. At \(z=it\), bounded cyclicity writes the trace as

\[
 \tau\bigl(B^qB^{-iqt}uA^{ipt}v\bigr).
\]

The factor after \(B^q\) is a contraction, so the bounded trace estimate gives \(|F(it)|\leq\tau(B^q)=1\). On the other boundary, rotate \(u\) to the end to obtain

\[
 |F(1+it)|
 =\bigl|\tau(A^pA^{ipt}vB^{-iqt}u)\bigr|\leq1.
\]

Hence \(|\tau(uAvB)|\leq1\). Multiply by the normalizing constants and let \(\varepsilon\downarrow0\). Equations (TI.23a) and (TI.23c), and norm continuity of bounded multiplication, prove (TI.24a), also if one factor is zero. No triangle inequality for \(N_p\), or dual-space identification, entered this proof.

**Exact finite-support norming.** For nonzero \(a=uh\in\mathfrak m_0\), let \(n=N_p(a)>0\) and, when \(1<p<\infty\), define

\[
 b=\frac{h^{p-1}u^*}{n^{p-1}}.
 \tag{TI.25a}
\]

This operator is bounded with finite support. The polar partial isometry transports the nonzero spectral projections of \(h\) to those of \(uhu^*\), so, for the conjugate exponent \(q\),

\[
 N_q(b)^q=\frac{\tau(h^{(p-1)q})}{n^{(p-1)q}}=1,
 \qquad
 \tau(ab)=\frac{\tau(uh^pu^*)}{n^{p-1}}=n.
 \tag{TI.25b}
\]

All products lie in one bounded finite corner. Together with (TI.24a), this proves

\[
 N_p(a)=\sup\{|\tau(ab)|:
                b\in\mathfrak m_0,\ N_q(b)\leq1\}.
 \tag{TI.25c}
\]

For \(a=0\), the supremum is zero. At \(p=1\), use the finite-support test \(u^*\), of operator norm one when \(a\ne0\); the formula holds with \(q=\infty\).

Apply (TI.25c) to \(a+b\), and use linearity of the trace and (TI.24a) separately on the two terms. It follows that

\[
 N_p(a+b)\leq N_p(a)+N_p(b)
 \quad(a,b\in\mathfrak m_0,\ 1\leq p<\infty).
 \tag{TI.26}
\]

The operator norm has its usual triangle inequality at \(p=\infty\). The testing gauges for the conjugate exponents did not need triangle inequalities of their own, so this proves the finite-support inequalities without circularity.

## Complete norms on actual measurable operators

For every real \(1\leq p<\infty\), define

\[
 L^p(M,\tau)=\{x\in S(M,\tau):\tau(|x|^p)<\infty\},\qquad
 \|x\|_p=\tau(|x|^p)^{1/p}.
 \tag{TI.27}
\]

The notation will be justified as a norm in the proof below. Put \(L^\infty(M,\tau)=M\), with its original operator norm. The finite-exponent spaces consist of the actual closed affiliated measurable operators of MT. Their products, sums, adjoints and domains retain those concrete meanings.

The earlier cutoff arguments prove homogeneity, definiteness, invariance under adjoint, and the two bounded module estimates before using any triangle inequality. More explicitly, faithfulness and

\[
 a^p\tau(1_{(a,\infty)}(|x|))\leq\tau(|x|^p)
 \quad(a>0)
\]

show that zero gauge forces every positive spectral tail to vanish, hence \(x=0\). Equal nonzero spectral distributions of \(|x|\) and \(|x^*|\) give the adjoint isometry. Integrating the bounded module estimate in (TI.8) gives

\[
 \|axb\|_p\leq\|a\|\,\|x\|_p\,\|b\|
 \quad(a,b\in M).
\]

The same estimate proves membership of each product in the displayed finite domain.

**Approximation and the sharp triangle inequality.** For \(x=uh\in L^p\), let

\[
 e_n=1_{[1/n,n]}(h),\qquad x_n=xe_n\in\mathfrak m_0.
 \tag{TI.28a}
\]

TI-03 already proves

\[
 x_n\longrightarrow x\text{ in measure},\qquad
 N_p(x-x_n)\longrightarrow0,\qquad
 N_p(x_n)\leq N_p(x),\qquad
 N_p(x_n)\longrightarrow N_p(x).
 \tag{TI.28b}
\]

For the last assertion, integrate \(h^p\) on the increasing annuli and apply scalar monotone convergence. Their union is the support of this particular \(h\), which need not be the identity. The approximants are bounded with finite trace support because \(\tau(e_n)\leq n^p\tau(h^p)\). The precise closed spectral identity \(|x-x_n|=h(1-e_n)\) supplies the second limit. No sequence exhausting the whole algebra by finite projections is used.

For \(x,y\in L^p\), choose their own spectral approximants. Continuity of addition in the measure algebra gives \(x_n+y_n\to x+y\) in measure. Spectral Fatou from TI-03 and the finite-support inequality (TI.26) give

\[
 \begin{split}
 N_p(x+y)^p
 &\leq\liminf_n N_p(x_n+y_n)^p\\
 &\leq\bigl(N_p(x)+N_p(y)\bigr)^p.
 \end{split}
 \tag{TI.29}
\]

Thus the sum has finite gauge, and the gauge satisfies the sharp triangle inequality. Together with homogeneity and definiteness, this proves that (TI.27) is a norm on a complex vector space. From now on we write \(\|\cdot\|_p\) in place of \(N_p\).

**Completeness with the concrete limit identified.** A \(p\)-norm Cauchy net \((x_i)\) is measure-Cauchy by the spectral Markov estimate (TI.9d). Completeness of the measure algebra gives an actual \(x\in S(M,\tau)\) with \(x_i\to x\) in measure. Given \(\varepsilon>0\), choose \(i_0\) so that \(\|x_i-x_j\|_p\leq\varepsilon\) for \(i,j\geq i_0\). For fixed \(i\geq i_0\), the net \(x_i-x_j\) tends in measure to \(x_i-x\). The already proved Fatou theorem for nets yields

\[
 \|x_i-x\|_p^p
 \leq\liminf_j\|x_i-x_j\|_p^p\leq\varepsilon^p.
 \tag{TI.30}
\]

The liminf is taken over the original directed set; its tail \(j\geq i_0\) is cofinal. In particular, \(x_i-x\in L^p\). Since \(L^p\) is now a vector space, \(x=x_i-(x_i-x)\in L^p\). The same inequality proves \(\|x_i-x\|_p\to0\). Thus \(L^p\) is Banach, and its norm limit is the concrete closed measurable operator with the domain supplied by the measure completion.

The bounded trace ideal lies in each finite-exponent space: for nonzero \(a\in\mathfrak m_\tau\), scalar functional calculus gives \(\tau(|a|^p)\leq\|a\|^{p-1}\tau(|a|)<\infty\); the zero element is immediate. This also identifies the abstract completion of the bounded ideal. A \(p\)-norm Cauchy sequence in \(\mathfrak m_0\) or \(\mathfrak m_\tau\) maps to its measure limit. Equation (TI.30) shows that the map preserves its norm limit and is injective: if the measure limit is zero, its \(p\)-norm tends to zero. Conversely, (TI.28a)–(TI.28b) approximates every concrete element of \(L^p\) by \(\mathfrak m_0\), so the map is onto. Both \(\mathfrak m_0\) and \(M\cap L^p\) are therefore dense, and the abstract completion and the concrete measurable space agree isometrically. At \(p=\infty\), completeness is the original completeness of \(M\) in operator norm; no assertion of finite-support norm density is made for that endpoint.

## Products, norming tests and exact factorization

The next estimate handles every product exponent at least one. Its proof begins again in finite corners, where a second strip argument combines the two-factor trace inequality with the bounded module estimate. We then use Fatou to establish integrability before taking complex traces of unbounded products.

**Three finite factors.** Suppose \(P,Q,T\) are finite exponents with

\[
 \frac1P+\frac1Q+\frac1T=1.
\]

Each is greater than one. For \(a,b,c\in\mathfrak m_0\),

\[
 |\tau(abc)|\leq\|a\|_P\|b\|_Q\|c\|_T.
 \tag{TI.31a}
\]

Choose one finite corner. The zero corner is immediate. Regularize the three positive absolute values as in (TI.23c), and divide each by its corresponding finite-exponent norm. This gives positive invertible \(A,B,C\) with \(\tau(A^P)=\tau(B^Q)=\tau(C^T)=1\). Retain the original polar contractions \(u,v,w\). Set \(\theta=1/P\), \(\beta=1/(1-\theta)\), and consider

\[
 F(z)=\tau\bigl(uA^{z/\theta}
                    vB^{\beta(1-z)}
                    wC^{\beta(1-z)}\bigr).
 \tag{TI.31b}
\]

The power argument of TI-08 proves that this function is entire and bounded on the closed strip. On its left boundary, write it as \(\tau(X_tY_t)\), where

\[
 X_t=uA^{it/\theta}vB^{\beta-i\beta t},\qquad
 Y_t=wC^{\beta-i\beta t}.
\]

The exponents \(Q_0=Q(1-\theta)\) and \(T_0=T(1-\theta)\) are conjugate and greater than one. By the bounded module estimate,

\[
 \|X_t\|_{Q_0}
 \leq\tau(B^{\beta Q_0})^{1/Q_0}=1,
 \qquad
 \|Y_t\|_{T_0}
 \leq\tau(C^{\beta T_0})^{1/T_0}=1.
 \tag{TI.31c}
\]

Indeed, \(\beta Q_0=Q\) and \(\beta T_0=T\); imaginary powers are unitaries and do not change these absolute values. The two-factor trace inequality (TI.24a) gives \(|F(it)|\leq1\). On the right boundary, rotate \(u\) to the end and separate the factor \(A^P\). Every remaining factor is a contraction or an imaginary-power unitary, so the bounded trace estimate gives \(|F(1+it)|\leq\tau(A^P)=1\). At \(z=\theta\), all three real powers are one. Apply (TI.22), multiply back the three normalizing constants, and remove the regularizations using (TI.23c), continuity of multiplication, and the bounded trace estimate (TI.23a). This proves (TI.31a), including zero factors.

**The finite-support product norm.** Let

\[
 1\leq p,q,r\leq\infty,\qquad
 \frac1r=\frac1p+\frac1q,\qquad\frac1\infty=0.
 \tag{TI.32a}
\]

For \(a,b\in\mathfrak m_0\),

\[
 \|ab\|_r\leq\|a\|_p\|b\|_q.
 \tag{TI.32b}
\]

If a factor exponent is infinite, the bounded module estimate proves this, including the case \(r=\infty\). Otherwise \(p,q\) are finite and greater than one. For \(r=1\), write \(ab=w|ab|\). If the product is nonzero, bounded cyclicity, (TI.24a), and the module bound give

\[
 \|ab\|_1=\tau(abw^*)
 \leq\|a\|_p\|bw^*\|_q\leq\|a\|_p\|b\|_q.
\]

The zero product is immediate. If \(1<r<\infty\) and \(ab\ne0\), choose its finite-support norming element \(c\) from (TI.25a), with exponent \(r\) and conjugate \(r'\). Then \(\|c\|_{r'}=1\) and \(\tau(abc)=\|ab\|_r\). Apply (TI.31a) with exponents \(p,q,r'\), whose reciprocal sum is one. This proves (TI.32b) in all cases.

**Measurable product integrability.** Let \(x\in L^p\), \(y\in L^q\), with finite \(p,q\) satisfying (TI.32a). Take their own spectral approximants \(x_n,y_n\) from (TI.28a)–(TI.28b). Multiplication is continuous in the measure algebra, so \(x_ny_n\to xy\) in measure, where \(xy\) is the actual closed product of MT. Spectral Fatou and (TI.32b) give

\[
 \begin{split}
 \tau(|xy|^r)
 &\leq\liminf_n\|x_ny_n\|_r^r\\
 &\leq\|x\|_p^r\|y\|_q^r.
 \end{split}
\]

This proves membership in \(L^r\), before a complex trace of the product is considered. For an infinite factor exponent, use the bounded module estimate directly. Thus the full result is

\[
 \boxed{\quad xy\in L^r,\qquad
 \|xy\|_r\leq\|x\|_p\|y\|_q
 \quad\text{under (TI.32a).}\quad}
 \tag{TI.33}
\]

All norms here are finite by their membership hypotheses. If a norm is zero, faithfulness gives a zero factor; no division by zero or multiplication of zero by an infinite norm is required.

In particular, for conjugate exponents \(p,q\), continuity of the \(L^1\) trace gives

\[
 |\tau(xy)|\leq\|x\|_p\|y\|_q
 \quad(x\in L^p,\ y\in L^q).
 \tag{TI.34}
\]

This now includes every suitable pair in the entire bounded trace ideal \(\mathfrak m_\tau\). Indeed, for \(a\in\mathfrak m_\tau\), one has \(a\in M\), \(\tau(|a|)<\infty\), and

\[
 \tau(|a|^p)\leq\|a\|^{p-1}\tau(|a|)<\infty
 \quad(1\leq p<\infty).
\]

The limit argument has removed both the lower spectral bound and the finite-total-support condition. It does not mistake \(\mathfrak m_0\) for the whole ideal \(\mathfrak m_\tau\).

**Norming on the full spaces.** For \(1\leq p<\infty\), let \(q\) be conjugate, with \(q=\infty\) at \(p=1\). Every \(x\in L^p\) satisfies

\[
 \|x\|_p=\sup\{|\tau(xb)|:
                   b\in\mathfrak m_0,\ \|b\|_q\leq1\}.
 \tag{TI.35a}
\]

Equation (TI.34) proves the upper bound. For the other direction, write \(x=uh\), and use \(e_n=1_{[1/n,n]}(h)\). If \(1<p<\infty\), let \(I_n=\tau(h^pe_n)\). Whenever \(I_n>0\), put

\[
 b_n=I_n^{-1/q}h^{p-1}e_nu^*.
 \tag{TI.35b}
\]

It is bounded with finite support, and the support calculation in (TI.25b) gives \(\|b_n\|_q=1\). Moreover,

\[
 xb_n=I_n^{-1/q}uh^pe_nu^*,\qquad
 \tau(xb_n)=I_n^{1/p}.
 \tag{TI.35c}
\]

The operator on the right is literally bounded with finite trace support, because of the annular cutoff. Spectral calculus and the measurable algebra laws identify it with the indicated product. Indices with \(I_n=0\) may be omitted. Monotone convergence gives \(I_n\uparrow\|x\|_p^p\). At \(p=1\), use \(b_n=e_nu^*\), of operator norm at most one; then \(\tau(xb_n)=\tau(he_n)\uparrow\|x\|_1\). For \(x=0\), the zero test suffices. This proves (TI.35a), in particular the full norming supremum on \(\mathfrak m_\tau\).

The same spectral tests can establish membership when only an \(L^1\) density is known. Suppose \(x=uh\in L^1\), \(1<p<\infty\), \(q=p/(p-1)\), and

\[
 |\tau(xb)|\leq C\|b\|_q
 \quad\text{for every }b\in\mathfrak m_0.
 \tag{TI.35d}
\]

Then \(x\in L^p\) and \(\|x\|_p\leq C\). To see this without already assuming the conclusion, note that \(\tau(h)<\infty\) makes every annulus \(e_n\) finite, while boundedness of \(h\) on it makes \(I_n=\tau(h^pe_n)\) finite. Thus (TI.35b) and (TI.35c) are available before knowing that \(\tau(h^p)\) is finite. The assumption gives \(I_n^{1/p}\leq C\), and monotone convergence yields \(\tau(h^p)\leq C^p\). All complex traces in (TI.35d) already exist because \(x\in L^1\) and \(b\) is bounded. This is a membership argument for actual measurable \(L^1\) densities; it does not apply a norming theorem prematurely to an arbitrary affiliated operator.

**Recovery by all finite projections.** Let \(\mathcal E\) be the directed set of all finite-trace projections. For every \(x\in L^p\), \(p<\infty\),

\[
 ex\longrightarrow x\text{ in }p\text{-norm},\qquad
 xe\longrightarrow x\text{ in }p\text{-norm}
 \quad(e\in\mathcal E),
 \tag{TI.36a}
\]

and

\[
 \|x\|_p=\sup_{e\in\mathcal E}\|ex\|_p
          =\sup_{e\in\mathcal E}\|xe\|_p.
 \tag{TI.36b}
\]

Indeed, fix an approximant \(x_n\) from (TI.28a)–(TI.28b), and let \(l_n\) be its finite left support. For every finite \(e\geq l_n\), one has \(ex_n=x_n\). The proved triangle and module inequalities therefore give

\[
 \|x-ex\|_p
 \leq\|x-x_n\|_p+\|e(x_n-x)\|_p
 \leq2\|x-x_n\|_p.
\]

The last expression tends to zero as \(n\to\infty\). For each \(n\), the condition \(e\geq l_n\) describes a tail of the full directed set \(\mathcal E\), proving left convergence. The right-support argument proves right convergence. The reverse triangle inequality then gives convergence of their norms, while the module bound makes each at most \(\|x\|_p\). This proves (TI.36b), including its assertion for every \(a\in\mathfrak m_\tau\). The proof uses finite-support density after Minkowski has been established; it is not an assumption used to prove that inequality.

At the bounded endpoint one also has

\[
 \|x\|=\sup\{|\tau(xb)|:
                 b\in\mathfrak m_0,\ \|b\|_1\leq1\}
 \quad(x\in M).
 \tag{TI.37}
\]

The upper bound is already known. For nonzero \(x=uh\), choose \(0<c<\|h\|\). The nonzero projection \(P=1_{(c,\infty)}(h)\) has a nonzero finite subprojection \(f\) by TI-01. Faithfulness gives \(0<\tau(f)<\infty\). Put \(b=fu^*/\tau(f)\). Since \(u\) is isometric on \(fH\), its two polar supports give \(\|b\|_1=1\). Bounded cyclicity and the positive compression inequality \(fhf\geq cf\) give

\[
 \tau(xb)=\frac{\tau(hf)}{\tau(f)}
          =\frac{\tau(fhf)}{\tau(f)}\geq c.
\]

The projection \(f\) need not commute with \(h\). Every product is in the bounded finite-support ideal. Let \(c\uparrow\|h\|\); the zero operator is immediate. Formula (TI.37) is a norming statement and does not identify the full Banach dual of \(M\) with \(L^1\).

**Cyclicity and convergence of products.** If \(p,q\) are finite conjugate exponents, their spectral approximants satisfy

\[
 \begin{split}
 \|xy-x_ny_n\|_1
 &\leq\|(x-x_n)y\|_1+\|x_n(y-y_n)\|_1\\
 &\leq\|x-x_n\|_p\|y\|_q
       +\|x_n\|_p\|y-y_n\|_q\longrightarrow0.
 \end{split}
 \tag{TI.38a}
\]

The decomposition uses the distributive law of the measurable algebra, and the estimates now use the established product theorem. Reversing the two factors gives \(y_nx_n\to yx\) in \(L^1\). For each \(n\), the approximants lie in one finite corner and satisfy \(\tau(x_ny_n)=\tau(y_nx_n)\). Continuity of the \(L^1\) trace yields

\[
 \tau(xy)=\tau(yx).
 \tag{TI.38b}
\]

The conjugate endpoints \(L^1\) and \(M\) were proved in TI-06. More generally, for finite \(p,q,r\) satisfying (TI.32a), the same calculation in \(r\)-norm shows that \(x_ny_n\to xy\) in \(L^r\). Membership was established earlier by Fatou, so this convergence estimate is not used to assume integrability in its own proof.

**Exact single-product factorization.** Under (TI.32a),

\[
 L^pL^q=L^r,
 \tag{TI.39a}
\]

where the left side is already the set of single products, without taking a span or closure. The inclusion follows from (TI.33). For finite \(p,q\), take \(z=wh\in L^r\) and set

\[
 x=wh^{r/p},\qquad y=h^{r/q}.
 \tag{TI.39b}
\]

These powers are measurable by their transformed spectral tails. Write \(\alpha=r/p\), \(\beta=r/q\). They are positive, at most one, and satisfy \(\alpha+\beta=1\). The ordinary product \(h^\alpha h^\beta\) has precisely domain \(D(h)\): its domain conditions are finiteness of the scalar spectral integrals of \(\lambda^{2\beta}\) and \(\lambda^2\), and the first follows from the second since \(\lambda^{2\beta}\leq1+\lambda^2\). On that domain the product equals \(h\). The polar factor \(w\) is isometric on the support of \(h\), so \(wh^\alpha\) is closed on \(D(h^\alpha)\). For instance, convergence of \(wh^\alpha\xi_n\) implies convergence of \(h^\alpha\xi_n\) after applying \(w^*\), and closedness of \(h^\alpha\) proves the assertion. Therefore the ordinary product \((wh^\alpha)h^\beta\) equals \(wh\) on exactly \(D(h)\). Its measurable product is the original closed operator \(z\), with its actual domain.

Polar support transport gives

\[
 \|x\|_p^p=\tau(h^r),\qquad
 \|y\|_q^q=\tau(h^r),\qquad
 \|x\|_p\|y\|_q=\|z\|_r.
 \tag{TI.39c}
\]

For \(z=0\), take both factors zero. If \(p=\infty\) and \(q=r<\infty\), use \(x=w\), \(y=h\); for nonzero \(z\), the first factor has norm one. If \(q=\infty\) and \(p=r<\infty\), use \(x=z\), \(y=s(h)\), its right support. If \(r=\infty\), both factor exponents are infinite and the bounded factorization is \(z=z1\). The zero algebra is included by taking zero factors. In particular, every \(L^1\) density has the exact conjugate-power factorization.

The norming formulas proved here show exact norms and separating trace pairings. Surjectivity onto the Banach dual for the interior exponents still requires a construction of a density from an arbitrary bounded functional; it does not follow from a norming supremum alone.

## Bounded strong convergence acts on each integrable vector

Fix \(1\leq p<\infty\). If \((a_i)\) is a bounded net in \(M\) tending strongly-star to zero, then for every fixed \(x\in L^p\),

\[
 \|a_ix\|_p\longrightarrow0,\qquad \|xa_i\|_p\longrightarrow0.
 \tag{TI.40}
\]

This concerns each fixed \(x\); it does not assert convergence of the multiplication operators in their operator norm on \(L^p\).

First take \(x=exe\in\mathfrak m_0\). The positive operators \(x^*a_i^*a_ix\) lie in \(eMe\), are uniformly bounded, and tend strongly to zero. Their \(p/2\)-th powers also tend strongly to zero. To justify this when the exponent is not an integer, uniformly approximate the continuous scalar function \(t^{p/2}\) on the common compact spectral interval by polynomials with zero constant term; boundedness makes the approximation uniform in \(i\), while each polynomial tends strongly to zero. The finite trace on \(eMe\) is a bounded normal functional. On bounded sets strong convergence implies sigma-strong convergence by CP-08, and every predual functional is continuous for that topology by CP-09, so

\[
 \|a_ix\|_p^p=\tau((x^*a_i^*a_ix)^{p/2})\longrightarrow0.
\]

Apply the same reasoning to \(x a_i a_i^* x^*\) and use the polar trace identity to obtain \(\|xa_i\|_p\to0\). For general \(x\), approximate by \(x_0\in\mathfrak m_0\) in \(p\)-norm. If \(K=\sup_i\|a_i\|\), the module bound gives

\[
 \|a_i x\|_p\leq K\|x-x_0\|_p+\|a_ix_0\|_p,
\]

and the analogous right estimate. Choose \(x_0\) first and then the directed tail. This proves (TI.40) for arbitrary nets. In particular the directed finite projections \(e\uparrow1\) give \(ex,xe\to x\) in \(p\)-norm.

For a bounded complex-linear functional \(F\) on \(L^p\) define

\[
 (aFb)(x)=F(bxa),\qquad F^\sharp(x)=\overline{F(x^*)}.
 \tag{TI.41}
\]

These are bounded complex-linear functionals. The module and involution estimates give \(\|aFb\|\leq\|a\|\|F\|\|b\|\) and \(\|F^\sharp\|=\|F\|\). Once a density \(h\in L^q\) represents \(F\), the identities in TI-10 show that \(aFb\) has density \(ahb\), while \(F^\sharp\) has density \(h^*\). For the first identity, \(\tau(hbxa)=\tau(ahbx)\); for the second, take the conjugate of \(\tau(hx^*)\), then use cyclicity. Thus the functional actions agree with the already defined measurable algebra operations, with their closure conventions intact.

## Every localized dual functional has a normal density

Let \(1<p<\infty\), \(q=p/(p-1)\), and \(F\in(L^p)^*\), with \(C=\|F\|\). Our objective is to construct \(h\in L^q\) such that \(F(x)=\tau(hx)\) and \(\|h\|_q=C\). The inequality in TI-10 already makes each proposed density a bounded functional; it does not prove that every functional is of that form.

For \(e\in\mathcal E\) put

\[
 F_e(a)=F(ea)\quad(a\in M),\qquad
 s_e(a)=\tau(eaa^*e)^{1/2}.
 \tag{TI.42}
\]

These are well defined, since \(ea\in\mathfrak m_0\) and \(\|ea\|_p\leq\|a\|\tau(e)^{1/p}\). The positive functional \(\omega_e(a)=\tau(eae)\) is normal by TI-04. Thus \(s_e\) is a sigma-strong-star seminorm, in the sense of CP-08. It also has a concrete Hilbert-space realization: if \(H_\tau\) is the trace GNS space of WG-004–006, then

\[
 Q_e(a)=\overline{\Lambda_\tau(a^*e)}\in\overline{H_\tau},
 \qquad \|Q_e(a)\|=s_e(a).
\]

The conjugate Hilbert space makes \(Q_e\) complex-linear. Its argument is in the GNS domain because \(\tau(eaa^*e)\leq\|a\|^2\tau(e)\).

We prove actual normality of \(F_e\), rather than infer it solely from continuity on bounded strong-star sets. Polar spectral calculus gives

\[
 \|ea\|_p^p=\tau((eaa^*e)^{p/2}).
\]

For \(1<p<2\), scalar Hölder with exponents \(2/p\) and \(2/(2-p)\), applied to the functions \(\lambda^{p/2}\) and one for the finite spectral measure in \(eMe\), gives the following bound. For \(p=2\) the underlying norm identity is \(\|ea\|_2=s_e(a)\); the same functional bound follows. The scalar Hölder step follows by normalizing both integrals and integrating Young’s inequality \(uv\leq u^A/A+v^B/B\), \(A^{-1}+B^{-1}=1\). To see this inequality, maximize \(uv-u^A/A\) over \(u\geq0\); its maximum is \(v^B/B\). Zero integrals give a zero factor and need no division. We obtain

\[
 |F_e(a)|\leq C\tau(e)^{1/p-1/2}s_e(a).
 \tag{TI.43}
\]

The case \(e=0\) is immediate. CP-09 identifies the continuous dual of the sigma-strong-star topology with \(M_*\), so \(F_e\) is normal in this case.

For \(p>2\), the scalar bound on the same positive spectral operator yields

\[
 |F_e(a)|\leq C\|a\|^{1-2/p}s_e(a)^{2/p}
            \leq\varepsilon\|a\|+K_\varepsilon s_e(a)
                    \quad(\varepsilon>0)
 \tag{TI.44}
\]

for some finite \(K_\varepsilon\). Explicitly, when \(C>0\), let \(\theta=2/p\), \(\eta=(\varepsilon/C)^{1/\theta}\). If \(s_e(a)\leq\eta\|a\|\), the first term is bounded by \(\varepsilon\|a\|\). In the other case it is bounded by \(C\eta^{-(1-\theta)}s_e(a)\). Adding the two bounds proves (TI.44). If \(C=0\), normality is immediate.

Apply complex Hahn–Banach from CP-01 to the functional \((a,Q_e(a))\mapsto F_e(a)\) on the graph subspace of \(M\oplus\overline{H_\tau}\), endowed with norm \(\varepsilon\|b\|+K_\varepsilon\|\xi\|\). For \(C>0\), the chosen \(K_\varepsilon\) is positive, so this is a norm. Inequality (TI.44) allows an extension of norm at most one. Restricting it to the two summands and then to the graph gives

\[
 F_e=u_\varepsilon+v_\varepsilon,
 \qquad \|u_\varepsilon\|\leq\varepsilon,
 \qquad |v_\varepsilon(a)|\leq K_\varepsilon s_e(a).
\]

The last functional belongs to \(M_*\) by CP-09. Norm closure of \(M_*\) in \(M^*\), proved in CP-07, now gives \(F_e\in M_*\). This supplies the step for all \(p\), without invoking a bounded-ball normality converse or a reflexivity theorem.

The onto map TI-06 supplies a unique \(h_e\in L^1\) with

\[
 \tau(h_ea)=F(ea)\quad(a\in M).
 \tag{TI.45}
\]

Testing against arbitrary bounded \(a\) and using injectivity of that map proves the following equalities in \(S\):

\[
 h_e=h_e e,\qquad h_g e=h_e\quad(e\leq g).
 \tag{TI.46}
\]

Indeed, \(\tau(h_e(1-e)a)=F(e(1-e)a)=0\), while \(\tau(h_g e a)=F(gea)=F(ea)\).

We also have the uniform local bound

\[
 h_e\in L^q,\qquad \|h_e\|_q\leq C.
 \tag{TI.47}
\]

To prove it before constructing any global operator, write \(h_e=vk\), \(k=|h_e|\). Its right support and therefore the support of \(k\) are at most \(e\), by (TI.46). Put

\[
 P_n=1_{[1/n,n]}(k),\quad x_n=k^{q-1}P_nv^*,\quad
 A_n=\tau(k^qP_n).
\]

Here \(P_n\leq e\), so \(A_n<\infty\) and \(x_n\in\mathfrak m_0\). The closed spectral products actually appearing in the next calculation are bounded: \(h_ex_n=vk^qP_nv^*\). Also \(ex_n=x_n\) and \((q-1)p=q\), giving

\[
 A_n=\tau(h_ex_n)=F(x_n),\qquad
 \|x_n\|_p=A_n^{1/p},\qquad A_n\leq C A_n^{1/p}.
\]

If \(A_n>0\), divide to get \(A_n^{1/q}\leq C\); if \(A_n=0\), this is immediate. Monotone convergence on the increasing spectral annuli gives \(\tau(k^q)\leq C^q\). The norming test has only been applied to the already measurable local \(L^1\) density; no global density has been assumed.

## Two dense domains give one closed affiliated operator

Right multiplication of a closed operator \(S\) by a bounded projection \(e\) is a closed ordinary composition, with domain \(\{\xi:e\xi\in D(S)\}\): its graph is the inverse image of the graph of \(S\) under \((\xi,\eta)\mapsto(e\xi,\eta)\). If \(S\) is measurable, MT-09 says this composition is densely defined and that its closure is the measurable product \(Se\). Its closedness therefore makes the ordinary and measurable products identical, including their domains.

Apply this to (TI.46). We obtain

\[
 \begin{aligned}
 D(h_e)&=(D(h_e)\cap eH)\oplus(1-e)H,\\
 D(h_e)&=\{\xi:e\xi\in D(h_g)\},\qquad
 h_e\xi=h_g e\xi\quad(e\leq g,\ \xi\in D(h_e)).
 \end{aligned}
 \tag{TI.48}
\]

In particular \(D(h_e)\cap eH\) is dense in \(eH\), and these subspaces are nested as \(e\) increases. Define

\[
 D_A=\bigcup_{e\in\mathcal E}(D(h_e)\cap eH),\qquad
 A\xi=h_e\xi\quad(\xi\in D(h_e)\cap eH).
 \tag{TI.49}
\]

Finite joins and (TI.48) make this a well-defined linear operator on a linear domain. That domain is dense because its intersection with each \(eH\) is dense there and \(e\uparrow1\) strongly. Each commutant unitary preserves every local domain and commutes with the local operator, so it preserves \(D_A\) and commutes with \(A\). This alone does not establish closability.

Construct the same local densities for \(F^\sharp\) from (TI.41), calling them \(k_f\), \(f\in\mathcal E\). They satisfy

\[
 \tau(k_fa)=\overline{F(a^*f)},\qquad
 k_f=k_ff,\qquad \|k_f\|_q\leq C.
 \tag{TI.50}
\]

They define a second linear operator \(B\) on the separately dense domain \(D_B=\bigcup_f(D(k_f)\cap fH)\). Taking adjoints inside the \(L^1\) pairing gives \(\tau(k_f^*b)=F(bf)\). Thus for every bounded \(a\),

\[
 \tau(fh_ea)=F(eaf)=\tau(k_f^*ea).
\]

Injectivity of TI-06 gives the measurable identity

\[
 f h_e=k_f^*e.
 \tag{TI.51}
\]

The left side is the closure of its ordinary composition; the right side is already the closed ordinary composition described above. Consequently \(\xi\in D(h_e)\cap eH\) implies \(\xi\in D(k_f^*)\) and \(k_f^*\xi=fh_e\xi\). For \(\eta\in D(k_f)\cap fH\), the actual Hilbert adjoint identity gives

\[
 \langle A\xi,\eta\rangle
 =\langle fh_e\xi,\eta\rangle
 =\langle k_f^*\xi,\eta\rangle
 =\langle\xi,k_f\eta\rangle
 =\langle\xi,B\eta\rangle.
 \tag{TI.52}
\]

It follows that \(A\subseteq B^*\) and \(B\subseteq A^*\). Since \(D_B\) is dense, \(A\) is closable. Let \(T=\overline A\). It is closed and densely defined. Invariance of the graph under each diagonal commutant unitary and its inverse passes to its closure, so \(T\) is affiliated with \(M\).

For \(e\in\mathcal E\), the ordinary composition \(Te\) is closed and affiliated. It extends \(h_e\): for \(\xi\in D(h_e)\), decompose \(\xi\) as in (TI.48), apply \(A\) to its \(e\)-component, and use zero on its complementary component. In particular \(Te\) is densely defined. MT-08 states that a measurable operator has no proper closed affiliated extension, whether or not the extension has yet been proved measurable. Applying it to \(h_e\) yields

\[
 Te=h_e\quad(e\in\mathcal E)
 \tag{TI.53}
\]

as actual closed operators. This does not appeal to maximality of an arbitrary affiliated operator. It appeals to maximality of the already measurable \(h_e\). Similarly, \(B\subseteq T^*\) makes \(T^*f\) a closed affiliated extension of \(k_f\), and gives \(T^*f=k_f\). Thus both local operator domains and the adjoint are recovered after closure.

## Spectral tests establish global duality

The ordinary polar decomposition \(T=u|T|\) is available for every closed densely defined operator by RD-02. It does not require measurability. Fix \(0<a\leq b<\infty\) and let \(P=1_{[a,b]}(|T|)\). If \(r\in\mathcal E\) and \(r\leq P\), then \(rH\subseteq D(T)\) and \(Tr\) is bounded. Equation (TI.53) identifies it with \(h_r\), hence \(\|Tr\|_q\leq C\). On the finite corner \(rMr\),

\[
 (Tr)^*(Tr)=r|T|^2r\geq a^2r.
\]

The compression is meaningful because \(rH\) lies in the domain of \(|T|^2\), by the bounded spectral band. Thus \(|Tr|\) has spectrum in \([a,b]\) on \(rH\), and scalar functional calculus in this single operator gives

\[
 a^q\tau(r)\leq\tau(|Tr|^q)\leq C^q.
\]

No operator-monotonicity assertion about a noncommuting pair raised to a power is used. TI-01 applied inside \(P\) now gives \(\tau(P)\leq(C/a)^q\). Increase \(b\) and use normality to conclude

\[
 \tau(1_{[a,\infty)}(|T|))\leq(C/a)^q\quad(a>0).
 \tag{TI.54}
\]

The high spectral tails tend to zero. MT-11 therefore proves that \(T\) is measurable. This step precedes every global expression \(\tau(Tx)\) or \(\tau(|T|^q)\) in the argument.

Now \(P_n=1_{[1/n,n]}(|T|)\) has finite trace, and (TI.53) gives \(TP_n=h_{P_n}\). Its spectral absolute value gives

\[
 \tau(|T|^qP_n)=\|TP_n\|_q^q\leq C^q.
\]

Monotone convergence shows that \(T\in L^q\) and \(\|T\|_q\leq C\). These annuli exhaust the support of \(|T|\); its kernel can have arbitrarily large trace.

For \(x\in\mathfrak m_0\), choose a finite projection \(e\) with \(ex=x\). Associativity in the measurable algebra, (TI.45), and (TI.53) give

\[
 F(x)=F(ex)=\tau(h_ex)=\tau(Tex)=\tau(Tx).
 \tag{TI.55}
\]

All expressions are now legitimate: \(h_e\in L^1\) and \(x\) is bounded; also \(T\in L^q\) and \(x\in L^p\), so TI-10 makes their product integrable. Density of \(\mathfrak m_0\) and Hölder extend (TI.55) to every \(x\in L^p\). Consequently \(C=\|F\|\leq\|T\|_q\); the reverse bound above proves equality.

If \(d\in L^q\) pairs to zero with all \(L^p\), write \(d=v|d|\) and test with \(|d|^{q-1}1_{[1/n,n]}(|d|)v^*\in\mathfrak m_0\). Their pairings are \(\tau(|d|^q1_{[1/n,n]}(|d|))\). All vanish, so monotone convergence and faithfulness give \(d=0\). We have proved the onto complex-linear isometry

\[
 L^q\xrightarrow{\ \cong\ }(L^p)^*,\qquad
 h\longmapsto[x\mapsto\tau(hx)]
 \quad(1<p<\infty).
 \tag{TI.56}
\]

Interchanging \(p,q\) gives the other dual identification. The pairing is bilinear, with no implicit conjugation of the representing density. Its involution and bounded bimodule actions are precisely (TI.41). For example, after both local constructions have become measurable, cyclicity shows that the operator \(ahb\) pairs with \(x\) as \(F(bxa)\); uniqueness identifies it with the density obtained by the construction for \(aFb\). Thus there is no separate, inconsistent dual-side product. At \(p=1\), TI-06 and CP-06 give \((L^1)^*=M\) through the same pairing. No assertion that the full Banach dual of \(M=L^\infty\) is \(L^1\) is made; \(L^1\) is its predual.

## The Hilbert space behind the trace

The space \(L^2(M,\tau)\) is a Hilbert space with inner product

\[
 \langle x,y\rangle_2=\tau(y^*x).
 \tag{TI.57}
\]

Indeed, TI-10 puts \(y^*x\) in \(L^1\). Linearity and the adjoint identity for the integral prove sesquilinearity and conjugate symmetry. Positivity and definiteness follow from \(\tau(x^*x)=\|x\|_2^2\), and the associated norm is the complete norm already proved in TI-09. Thus no further completion of this concrete operator space is necessary.

Let \((H_\tau,\pi_\tau,\Lambda_\tau)\) be the trace GNS triple from WG-006. Faithfulness gives a zero null ideal. For \(a,b\in\mathfrak n_\tau\), the bounded finite trace integral and its \(L^1\) extension agree, so

\[
 \langle\Lambda_\tau(a),\Lambda_\tau(b)\rangle
 =\tau(b^*a)=\langle a,b\rangle_2.
\]

The isometry \(U\Lambda_\tau(a)=a\) has dense range in \(L^2\), since \(\mathfrak m_0\subseteq\mathfrak n_\tau\) and TI-09 proves its \(L^2\)-density. It therefore extends to a unique onto unitary

\[
 U:H_\tau\longrightarrow L^2(M,\tau),\qquad
 U\pi_\tau(c)U^*x=cx.
 \tag{TI.58}
\]

The action identity holds first on \(\mathfrak n_\tau\) by the GNS module law, then everywhere by the bounded module estimate. The target is the measurable-operator Hilbert space, rather than an unspecified Hilbert space isomorphic to it.

For clarity, left multiplication \(L_cx=cx\) is a faithful normal representation on \(L^2\). It is a unital star representation by associativity and (TI.57): \(\langle cx,y\rangle_2=\langle x,c^*y\rangle_2\). If \(L_c=0\), then \(ce=0\) for each finite projection \(e\), and \(e\uparrow1\) strongly gives \(c=0\). For a bounded increasing positive net \(c_i\uparrow c\), TI-11 gives \(L_{c_i}x\to L_cx\) for every \(x\in L^2\). The positive representation therefore preserves these suprema, which is normality in the bounded-map criterion NP-06.

Right multiplication \(R_cx=xc\) is also bounded. Cyclicity gives \(R_c^*=R_{c^*}\), and the measurable algebra gives \(L_aR_b=R_bL_a\). The conjugate-linear map

\[
 J_\tau x=x^*
\]

is an isometric involution, hence antiunitary, and \(J_\tau L_cJ_\tau=R_{c^*}\). These identities include every \(L^2\) vector. If \(\tau(1)=\infty\), the identity operator is not such a vector; no cyclic vector \(\Lambda_\tau(1)\) has been inserted into the argument.

## Three models of densities and integrability

**An uncountable counting trace.** Let \(I\) be any set and \(M=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\), with \(\tau(f)=\sum_{i\in I}f(i)\) for \(f\geq0\). The sum means the supremum of finite partial sums. Faithfulness and normality follow coordinatewise, and finite-coordinate cutoffs prove semifiniteness. Each nonzero projection has trace at least one, so a high spectral tail of trace less than one is zero. Hence every measurable diagonal operator is bounded. For \(1\leq p<\infty\),

\[
 L^p(M,\tau)=\left\{x:I\to\mathbb C:\sum_i|x(i)|^p<\infty\right\},\qquad
 \|x\|_p^p=\sum_i|x(i)|^p.
\]

Each displayed function is bounded and has at most countable support: for every positive integer \(n\), the set where \(|x(i)|\geq1/n\) is finite, and their union contains every nonzero coordinate. Thus an individual integrable density can have countable support even though \(I\) is uncountable. TI-06 identifies every normal functional with the absolutely summable coefficients of an \(L^1\) density, agreeing with the concrete coordinate-predual calculation in NP-07. When \(I\) is uncountable, no such positive functional is faithful, since its support misses some coordinate. The trace and the results of the unit remain valid.

**An integrable density with a finite upper exponent.** Let \(M=\prod_{n\geq1}M_2(\mathbb C)\), with the faithful finite trace

\[
 \tau((b_n))=\sum_{n\geq1}2^{-3n}\operatorname{Tr}(b_n)
             \quad((b_n)\geq0).
\]

Normality is monotone convergence of nonnegative series; faithfulness is coordinatewise. Since \(\tau(1)<\infty\), semifiniteness is immediate. On the Hilbert direct sum of the defining two-dimensional representations, let \(x\) have blocks

\[
 x_n=2^n\begin{pmatrix}1&1\\0&0\end{pmatrix},\qquad
 D(x)=\{\xi:\sum_n\|x_n\xi_n\|^2<\infty\}.
\]

It is a closed densely defined affiliated operator: finite-block vectors are a dense domain, coordinate convergence proves closedness, and blockwise spectral calculus gives affiliation. The single nonzero singular value in block \(n\) is \(\sqrt2\,2^n\). Its high spectral tail has trace \(\sum_{\sqrt2\,2^n>R}2^{-3n}\to0\), proving measurability. Therefore

\[
 \|x\|_p^p=2^{p/2}\sum_{n\geq1}2^{(p-3)n}<\infty
                       \quad\Longleftrightarrow\quad p<3.
\]

In particular \(x\) is an unbounded \(L^1\) density defining a normal complex functional, and is an \(L^2\) vector, but it lies in no \(L^p\) with \(p\geq3\). Its initial support in each block is the line through \((1,1)\), while its final support is the line through \((1,0)\). Their traces agree although the projections do not commute. The polar supports used in the proofs are not redundant even in this elementary model.

**Finite lower and upper exponent thresholds at once.** Let \(M=L^\infty(0,\infty)\) with Lebesgue trace, acting by multiplication on \(L^2(0,\infty)\). Consider the positive multiplication operator given by

\[
 f(t)=\begin{cases}t^{-1/4},&0<t<1,\\t^{-1/2},&t\geq1.\end{cases}
\]

Its maximal multiplication domain is dense and its operator is closed. For \(a>0\), its distribution is

\[
 d_f(a)=\begin{cases}a^{-2},&0<a<1,\\a^{-4},&a\geq1.\end{cases}
\]

The high tails tend to zero, so it is measurable. Formula (TI.5) gives \(\mu_s(f)=s^{-1/4}\) for \(0<s\leq1\), and \(s^{-1/2}\) for \(s\geq1\). Consequently

\[
 f\in L^p\quad\Longleftrightarrow\quad2<p<4,
 \qquad
 \|f\|_p^p=\frac1{1-p/4}+\frac1{p/2-1}
                   \quad(2<p<4).
\]

The divergence at the two endpoints has different causes: the singularity near zero controls the upper exponent, while decay over a region of infinite measure controls the lower exponent. Thus the \(L^p\) spaces need not be nested when the total trace is infinite.

## Problems with complete solutions

**Problem 1: recover the support of a normal positive functional.** Let \(h\in L^1_+\), and let \(\varphi(a)=\tau(ha)\). Prove that the least projection \(p\) for which \(\varphi(1-p)=0\) is \(s(h)\). Also show that the finite-projection compressions \(ehe\) approach \(h\) in \(L^1\), so their normal functionals approach \(\varphi\) in norm.

**Solution.** Put \(k=h^{1/2}\in L^2\), using \(\|k\|_2^2=\tau(h)\). For a projection \(p\), bounded cyclicity followed by the \(L^2\) pairing gives

\[
 \varphi(1-p)=\tau((1-p)h(1-p))
             =\|k(1-p)\|_2^2.
\]

The first equality follows from \(\tau(h(1-p))=\tau((1-p)h)\), then applying bounded cyclicity to \((1-p)h\in L^1\) and \(p\) to see its \(p\)-part has zero trace. The second uses the closed product \((k(1-p))^*k(1-p)=(1-p)h(1-p)\). Therefore \(\varphi(1-p)=0\) if and only if \(k(1-p)=0\). In the measurable algebra this zero product is the ordinary right-projection composition, so \((1-p)H\subseteq\ker k\). This is equivalent to \(s(h)=s(k)\leq p\), proving the claim, including \(h=0\). Finally TI-11 gives \(eh,h e\to h\) in \(L^1\), and

\[
 \|h-ehe\|_1\leq\|h-eh\|_1+\|e(h-he)\|_1
             \leq\|h-eh\|_1+\|h-he\|_1\longrightarrow0.
\]

TI-06 converts this to precisely the norm convergence of the corresponding functionals. The net of all finite projections need not be countable.

**Problem 2: why fixed-vector continuity is the right statement.** In \(M=B(\ell^2(\mathbb N))\) with canonical trace, let \(a_n\) project onto the span of the basis vectors with index greater than \(n\). Prove that \(a_n\to0\) strongly-star, that \(a_nx,xa_n\to0\) in \(L^p\)-norm for each fixed \(x\in L^p\), \(1\leq p<\infty\), and that both multiplication operators on \(L^p\) nevertheless have norm one.

**Solution.** For every \(\xi\in\ell^2\), \(\|a_n\xi\|^2=\sum_{j>n}|\xi_j|^2\to0\). The projections are self-adjoint, so the convergence is strong-star. The fixed-vector assertions follow from TI-11. For the operator norms, bounded module estimates give an upper bound of one. Let \(e_{n+1}\) be the rank-one projection onto the next basis vector. Its \(p\)-norm is one, and \(a_ne_{n+1}=e_{n+1}a_n=e_{n+1}\), giving the lower bound one. The norming vector changes with \(n\); it does not contradict fixed-vector convergence. At the bounded endpoint, the fixed vector \(x=1\in M\) gives \(\|a_n1\|=1\), so that endpoint cannot be added to TI-11.

**Problem 3: endpoint atoms in the cutoff formula.** On \(M_2(\mathbb C)\) take \(\tau=\tfrac12\operatorname{Tr}\) and \(a=\operatorname{diag}(3,1)\). Compute \(d_a\), \(\mu_t(a)\), and \(\|a\|_p\), and exhibit a unit \(L^q\) norming density for each \(1<p<\infty\).

**Solution.** The strict distribution is one for \(0\leq s<1\), one half for \(1\leq s<3\), and zero for \(s\geq3\). Consequently

\[
 \mu_t(a)=\begin{cases}3,&0<t<1/2,\\1,&1/2\leq t<1,\\0,&t\geq1,\end{cases}
 \qquad \|a\|_p=\left(\frac{3^p+1}{2}\right)^{1/p}.
\]

At \(t=1/2\) a defect of exactly one half is allowed, so the cutoff can discard the larger eigenvalue. For \(q=p/(p-1)\), put \(b=a^{p-1}/\|a\|_p^{p-1}\). Since \((p-1)q=p\), \(\|b\|_q=1\), and direct trace calculation gives \(\tau(ab)=\|a\|_p\). This checks both the endpoint conventions in TI-02 and the exact constant in Hölder.

**Problem 4: compatible finite pieces can fail to be measurable.** On \(\ell^2(\mathbb N)\), let \(e_N\) project onto the first \(N\) basis vectors, and let \(h_N\) have diagonal entries \(1,2,\ldots,N,0,0,\ldots\). Show that these pieces glue to a closed affiliated operator, but cannot arise from the uniformly bounded dual construction of TI-12–14 for any finite \(q\).

**Solution.** The identity \(h_Me_N=h_N\) holds for \(M\geq N\). On finite-coordinate vectors the common operator is multiplication by \(n\); its closure is

\[
 D(T)=\{\xi:\sum_n n^2|\xi_n|^2<\infty\},\qquad
 (T\xi)_n=n\xi_n.
\]

Coordinate convergence proves closedness, and finite-coordinate truncation converges in its graph norm, identifying this precise closure. It is affiliated with \(B(\ell^2)\), whose commutant consists of scalars. However every high spectral tail has infinite canonical trace, so MT-11 says it is not measurable. Moreover \(\|h_N\|_q^q=\sum_{n=1}^N n^q\to\infty\). If a bounded functional on \(L^p\) produced these local densities, its value on the rank-one projection onto coordinate \(n\), of \(p\)-norm one, would be \(n\); this contradicts boundedness. Compatibility and finite traces of retained projections do not replace the uniform local norm bound.

**Problem 5: a pointwise Fatou argument for nets can fail.** Order the finite subsets \(F\subseteq[0,1]\) by inclusion, and put \(f_F=1_F\). Explain why pointwise convergence and the ordinary sequence version of Fatou cannot replace the argument in TI-03.

**Solution.** For each \(t\in[0,1]\), every index beyond \(\{t\}\) has \(f_F(t)=1\), so the net converges pointwise to one. Every \(f_F\) has Lebesgue integral zero. Thus the putative net inequality \(\int\liminf_F f_F\leq\liminf_F\int f_F\) would read \(1\leq0\), which is false. In the space of functions modulo almost-everywhere equality, every \(f_F\) is zero, so the net converges in measure to zero, not to one. There is no contradiction with TI-03: its one directed tail controls all cutoff integration variables simultaneously and proves lower semicontinuity for the actual measure limit. There is no single null set outside which all the representatives in this uncountable net vanish.

## Interfaces for the next constructions

The trace now has a positive extended integral on all positive measurable operators and a finite linear integral on precisely \(L^1\). That space equals the full predual. Every finite real exponent at least one gives a complete concrete \(L^p\) space; conjugate exponents have an exact bilinear duality and every integrable operator has a polar-power factorization. The Hilbert member is canonically the trace GNS representation, with both bounded module actions visible.

Two further proof directions use these results. Comparing positive \(L^2\) vectors through their spectral projections requires a joint scalar measure for the commuting left and right spectral actions; its projection-distance estimate is a later obligation. Moving from scalar traces to general operator-valued weights requires an extended-positive target and new domain and normality arguments. The present integral is a scalar trace, so its cyclicity cannot be transferred to a nontracial weight by changing notation. Nontracial \(L^p\) constructions, those projection comparison estimates, and the remaining measurable-operator exercise and correspondence/fusion inventory remain outside the claims proved in this unit. The incidental source assertion about densities for arbitrary unbounded normal semifinite weights belongs to the general weight Radon–Nikodym theory. TI-06 proves the full bounded-functional predual theorem; it does not assert that every such unbounded weight has an integrable or even trace-measurable density.

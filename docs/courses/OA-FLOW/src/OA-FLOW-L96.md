# A weak-star Hille–Yosida criterion for isometric groups

An abstract weak-star closed operator need not generate a group. The decisive conditions are contractive lower bounds for both signs and one range condition in each direction. This lesson proves the weak-star group form of Takesaki II, Theorem XI.1.20, whose proof is omitted in the source. It also proves normality of every resolvent, the Euler approximation, and the sign-dependent correction to the displayed Yosida exponential.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

The exact earlier inputs are BS0–1, [CF1](OA-FLOW-CF.md#oa-flow.cf.1) and [CF4 product compactness](OA-FLOW-CF.md#oa-flow.cf.4), [ST1 compact dual balls](OA-FLOW-ST12.md#oa-flow.st.1), [L24's Banach integral and scalar translations](OA-FLOW-L24.md#oa-flow.grp.vectorintegration), [L34 Lemma3.2 and its Neumann-series paragraph](OA-FLOW-L34.md#oa-flow.l34.3), the earlier [full generator and adjoint-domain proof](OA-FLOW-L94.md#oa-flow.gen.closed), and [both Laplace resolvents](OA-FLOW-L95.md#oa-flow.res.forward). The scalar measure and convergence proofs are [SC2](OA-FLOW-SC.md#sc-02), [SC4](OA-FLOW-SC.md#sc-04), [SC5](OA-FLOW-SC.md#sc-05) and [SC8](OA-FLOW-SC.md#sc-08); [SC7](OA-FLOW-SC.md#sc-07) and [CF8](OA-FLOW-CF.md#oa-flow.cf.8) supply the Hilbert dual model used in the last example. All integrals use ordinary Lebesgue measure.

<a id="oa-flow.hy.precontinuity"></a><a id="OA-FLOW.HY.PRECONTINUITY"></a>

### Normal weak-star groups have strongly continuous predual orbits

For the converse direction of the criterion, normality and pointwise weak-star continuity of an isometric real-parameter group already imply the predual continuity used in L94/L95. We prove the slightly more general uniformly bounded assertion. Write \(Y=X_*\), \(b_ty=y\circ\alpha_t\). Every scalar \(x(b_ty)\) is continuous and \(\|b_t\|\leq C_\alpha\).

Fix \(y\). Its entire orbit is in the norm-closed linear span of the countable set \(\{b_qy:q\in\mathbb Q\}\). Otherwise Hahn–Banach would give a bounded functional zero on that closed span and nonzero at an orbit point, contrary to weak continuity and rational approximation of that point. That closed span is separable, by rational complex linear combinations of its countably many generators. For a fixed vector \(v\), \(t\mapsto\|b_ty-v\|\) is Borel: the sets where it is at most \(r\) are closed, by the norming-functional formula and weak continuity. A countable dense set in the orbit's closed span therefore gives measurable simple approximants, as in L24. Thus \(f(t)b_ty\) is Bochner integrable for \(f\in L^1(\mathbb R)\).

The span \(Y_c\) of these integrated vectors has norm-continuous orbits, because

<a id="equation-h0a"></a>

\[
 \left\|b_s\int f(t)b_ty\,dt-\int f(t)b_ty\,dt\right\|
 \leq C_\alpha\|y\|\,\|L_sf-f\|_1\longrightarrow0.
 \tag{H0a}
\]
It is norm dense. A functional annihilating it has zero integral against every \(f\) and every continuous scalar orbit; shrinking mass-one bumps show that its value at every \(y\) is zero. Hahn–Banach then gives density. Approximating an arbitrary \(y\) by \(v\in Y_c\) and bounding \(\|(b_s-I)(y-v)\|\leq(C_\alpha+1)\|y-v\|\) proves strong continuity on all of \(Y\). Normality supplies the actual preadjoints, rather than an extension to an unspecified larger dual.

<a id="oa-flow.hy.resolvents"></a>

<a id="oa-flow.hy.criterion"></a><a id="OA-FLOW.HY.CRITERION"></a>

## The criterion and all real resolvents

Let \(X=X_*^*\) be a complex dual Banach space with specified predual. Let \(\delta:D\subset X\to X\) be linear, weak-star closed, and weak-star densely defined. Consider the conditions

<a id="equation-h1"></a>

$$\|(I-s\delta)x\|\ge\|x\|
\quad(s\in\mathbb R,\ x\in D),\tag{H1}$$

and, for some \(r_+,r_->0\),

<a id="equation-h2"></a>

$$(I-r_+\delta)D=X,
\qquad (I+r_-\delta)D=X.\tag{H2}$$

We first show that (H1)–(H2) make \(I-s\delta:D\to X\) bijective for every \(s\ne0\). Whenever it is onto, (H1) makes it injective and its inverse

<a id="equation-h3"></a>

$$R_s=(I-s\delta)^{-1}:X\to D\subset X\tag{H3}$$

a contraction. On the positive half-line, the set of \(s\) for which (H3) exists is nonempty by (H2). It is open: if \(R_{s_0}\) exists, then \(\delta R_{s_0}=(R_{s_0}-I)/s_0\) is bounded and

<a id="equation-h4"></a>

$$(I-s\delta)R_{s_0}
=I-(s-s_0)\delta R_{s_0},\tag{H4}$$

which is invertible when \(s\) is sufficiently close to \(s_0\). It is also closed in \((0,\infty)\). In a compact space a net has a cluster point: the closures of its tails have the finite-intersection property. Use triples \(i,U,j\) with \(j\geq i\), \(U\) a neighbourhood of the cluster point, and the \(j\)-th term in \(U\). Order them by increasing \(i,j\) and decreasing \(U\). The cluster property makes this set directed; projection to \(j\) is monotone and cofinal, giving a convergent subnet. If a net in a compact space has only one possible cluster point, it converges to that point: otherwise a subnet outside a neighbourhood has a cluster point in its closed complement. If \(s_j\to s>0\) and \(x\in X\), the vectors \(y_j=R_{s_j}x\) lie in the weak-star compact ball of radius \(\|x\|\). Along any convergent subnet, say \(y_j\to y\) weak-star,

<a id="equation-h5"></a>

$$\delta y_j=\frac{y_j-x}{s_j}
\longrightarrow\frac{y-x}{s}\quad\text{weak-star}.\tag{H5}$$

Weak-star closedness gives \(y\in D\) and \((I-s\delta)y=x\). Uniqueness from (H1) forces every cluster point to be this \(y\), hence the original net converges and the range is all of \(X\). For clarity, a real interval is connected. If it were partitioned into nonempty relatively open sets \(U,V\), choose \(a<b\) in different sets, interchanging their names so \(a\in U,b\in V\). The point \(c=\sup(U\cap[a,b])\) is below \(b\), since \(V\) contains a left neighbourhood of \(b\). If \(c\in U\), openness supplies a point of \(U\) above \(c\); if \(c\in V\), openness excludes the points of \(U\) arbitrarily close below \(c\). Both contradict its supremum property. Thus a nonempty relatively open-and-closed subset of \((0,\infty)\) is the whole interval, giving every positive \(s\). The same argument on \(( -\infty,0)\), starting at \(-r_-\), gives every negative \(s\).

Each \(R_s\) is normal, but this requires a bounded-ball argument: an arbitrary weak-star convergent net need not be norm bounded. Restrict first to a fixed norm ball. If \(x_j\to x\) weak-star in that ball, contractivity puts \(R_sx_j\) in the same weak-star compact ball. Every cluster point satisfies the closed graph equation for \(R_sx\), just as in (H5), and uniqueness forces convergence. Thus \(R_s\) is weak-star continuous on each norm ball.

To obtain a preadjoint, fix \(\phi\in X_*\) and let \(F(x)=\langle R_sx,\phi\rangle\), a bounded linear functional on \(X\). Its restriction to the unit ball is weak-star continuous. For any \(\varepsilon>0\), continuity at zero supplies finitely many \(\psi_1,\ldots,\psi_m\in X_*\) such that

<a id="equation-h6a"></a>

$$|F(x)|\le\varepsilon
\quad\left(\|x\|\le1,\ 
\langle x,\psi_k\rangle=0\text{ for every }k\right). \tag{H6a}$$

The Hahn–Banach distance formula now gives

<a id="equation-h6b"></a>

$$\operatorname{dist}_{X^*}
\left(F,\operatorname{span}\{\psi_1,\ldots,\psi_m\}\right)
\le\varepsilon. \tag{H6b}$$

Indeed, restriction to the common kernel has norm at most \(\varepsilon\); extend this restriction with the same norm, and subtract that extension from \(F\). The difference annihilates the common kernel and therefore belongs to the indicated finite span. Since the canonical image of \(X_*\) in \(X^*\) is norm closed and \(\varepsilon\) is arbitrary, \(F\in X_*\). The resulting map \(\phi\mapsto F\) is a contraction with adjoint \(R_s\). This proves

<a id="equation-h6"></a>

$$s\ne0\quad\Longrightarrow\quad
R_s\text{ is a normal contraction}.\tag{H6}$$

At \(s=0\), formulas below use \(R_0=I_X\) by convention. This is not a claim that the restricted map \(I:D\to X\) is onto unless \(D=X\).

<a id="oa-flow.hy.preadjoint"></a><a id="OA-FLOW.HY.PREADJOINT"></a>

## Passing to a strongly continuous predual group

Let \(S_s:X_*\to X_*\) be the contraction with \(S_s^*=R_s\). Fix one \(s_0>0\), and define an operator \(A\) on \(X_*\) by

<a id="equation-h7"></a>

$$D(A)=\operatorname{Ran}S_{s_0},
\qquad A(S_{s_0}\phi)=\frac{S_{s_0}\phi-\phi}{s_0}.\tag{H7}$$

Write \(Y=X_*\). Here \(D=\operatorname{Ran}R_{s_0}\), and the preadjoint \(S_{s_0}\) is the candidate inverse of \(I-s_0A\). The range and domain assertions can be checked explicitly. If \(S_{s_0}\phi=0\), then \(\phi\) annihilates \(\operatorname{Ran}R_{s_0}=D\), so weak-star density makes \(\phi=0\). If \(x\in Y^*=X\) annihilates \(\operatorname{Ran}S_{s_0}\), then \(R_{s_0}x=0\), so \(x=0\). Hahn–Banach gives norm density of that range. Closedness of \(A\) follows directly: if \(y_j\to y\) and \(Ay_j\to z\) in norm, then \(y_j=S_{s_0}(y_j-s_0Ay_j)\to S_{s_0}(y-s_0z)\). Hence \(y\in D(A)\) and \(Ay=z\).

For \(s,t\ne0\), apply \(R_s\) to \((I-s\delta)R_t=I+(t-s)\delta R_t\). This gives \(R_s-R_t=(s-t)R_s\delta R_t\), and therefore

<a id="equation-h7a"></a>

\[
 sR_s-tR_t=(s-t)R_sR_t.
 \tag{H7a}
\]
Exchanging \(s,t\) proves commutation when they differ; when they agree it is immediate. Preadjoints give the same identity for \(S_s,S_t\). In particular

<a id="equation-h7b"></a>

\[
 S_t=S_{s_0}\left(\frac{s_0}{t}I+\frac{t-s_0}{t}S_t\right).
 \tag{H7b}
\]
This proves \(\operatorname{Ran}S_t\subset\operatorname{Ran}S_{s_0}\); exchange the parameters for equality. Substitution into (H7) gives \(AS_t=(S_t-I)/t\). For \(y=S_{s_0}\phi\), identity (H7a) on the predual also gives \(S_t(y-tAy)=y\). Thus both inverse identities hold on their full domains:

For every \(s\ne0\)

<a id="equation-h8"></a>

$$S_s=(I-sA)^{-1}.\tag{H8}$$

We must check the entire domain of \(A^*\); equality of adjoint domains is not merely formal. If \(x\in D(A^*)\), put \(z=A^*x\). Testing the identity \((I-s_0A)S_{s_0}\phi=\phi\) gives \(R_{s_0}(x-s_0z)=x\), so \(x\in D\) and \(z=\delta x\). Conversely, for \(x=R_{s_0}v\in D\) and \(y\in D(A)\), the identity \(S_{s_0}(I-s_0A)y=y\) gives \(x((I-s_0A)y)=v(y)\), and therefore
\(x(Ay)=((x-v)/s_0)(y)\). Thus \(x\in D(A^*)\) and \(A^*x=(x-v)/s_0=\delta x\). Therefore

<a id="equation-h9"></a>

$$\delta=A^*.\tag{H9}$$

For completeness, the contraction semigroups can now be constructed without importing a generation theorem. For \(\varepsilon>0\), put

<a id="equation-h10"></a>

$$J_\varepsilon=(I-\varepsilon A)^{-1},
\qquad A_\varepsilon=AJ_\varepsilon
=\frac{J_\varepsilon-I}{\varepsilon}.\tag{H10}$$

Then \(\|J_\varepsilon\|\le1\) and

<a id="equation-h11"></a>

$$\|e^{tA_\varepsilon}\|
=e^{-t/\varepsilon}\left\|e^{(t/\varepsilon)J_\varepsilon}\right\|\le1
\qquad(t\ge0).\tag{H11}$$

For \(y\in D(A)\), the inverse identities give both \(J_\varepsilon Ay=(J_\varepsilon y-y)/\varepsilon\) and \(AJ_\varepsilon y=(J_\varepsilon y-y)/\varepsilon\). Thus

<a id="equation-h11a"></a>

\[
 J_\varepsilon y-y=\varepsilon J_\varepsilon Ay,\qquad
 A_\varepsilon y=J_\varepsilon Ay.
 \tag{H11a}
\]
The first estimate and density prove \(J_\varepsilon\phi\to\phi\) for every \(\phi\in Y\): extend from \(D(A)\) by contractivity. Applied to \(A\phi\), this gives \(A_\varepsilon\phi=J_\varepsilon A\phi\to A\phi\) whenever \(\phi\in D(A)\). Identity (H7a) proves that all resolvents, and hence their bounded Yosida operators and exponentials, commute.

For bounded operators, the exponential series converges in operator norm and differentiates there on bounded time intervals; CF1's absolute-series rules and bounded-map calculus justify this directly by its factorial bounds. For commuting \(A_\varepsilon,A_\eta\), differentiate
\(e^{(t-u)A_\varepsilon}e^{uA_\eta}y\) and integrate on \([0,t]\). This proves Duhamel's identity

<a id="equation-h11b"></a>

\[
 (e^{tA_\varepsilon}-e^{tA_\eta})y
 =\int_0^t e^{(t-u)A_\varepsilon}e^{uA_\eta}
                  (A_\varepsilon-A_\eta)y\,du.
 \tag{H11b}
\]
The two exponential factors are contractions by (H11). Consequently, for \(\phi\in D(A)\) and \(0\le t\le T\),

<a id="equation-h12"></a>

$$\|e^{tA_\varepsilon}\phi-e^{tA_\eta}\phi\|
\le T\|(A_\varepsilon-A_\eta)\phi\|.\tag{H12}$$

Thus the exponentials are strongly Cauchy uniformly on bounded positive time intervals, first on \(D(A)\), then on all \(Y\) by density and their contraction bounds. Completeness defines \(T_+(t)\) on every \(y\in Y\). The limit is linear and contractive; uniform convergence on each vector preserves continuity. Passing through \(e^{(t+u)A_\varepsilon}=e^{tA_\varepsilon}e^{uA_\varepsilon}\) gives the semigroup law, since both factors are uniformly bounded and converge on every fixed vector. Its value at zero is \(I\).

For \(y\in D(A)\), the bounded exponential integral identity and the established convergences give

<a id="equation-h12a"></a>

\[
 T_+(t)y-y=\int_0^t T_+(u)Ay\,du.
 \tag{H12a}
\]
Indeed the integrand error is bounded by
\(\|A_\varepsilon y-Ay\|+\|(e^{uA_\varepsilon}-T_+(u))Ay\|\), uniformly on bounded intervals. Hence the right norm generator \(G_+\) of \(T_+\) extends \(A\).

We verify equality on the whole generator domain. For any \(y\in D(G_+)\), the semigroup law on its right difference quotients gives \(T_+(t)y\in D(G_+)\), \(G_+T_+(t)y=T_+(t)G_+y\), and derivative \(T_+(t)G_+y\). At \(t>0\), the left derivative follows by writing its quotient as \(T_+(t-h)(T_+(h)y-y)/h\); strong continuity gives the same value. Thus if \(G_+y=\varepsilon^{-1}y\), fundamental calculus applied to \(e^{-t/\varepsilon}T_+(t)y\) makes it constant, so \(T_+(t)y=e^{t/\varepsilon}y\). Contractivity forces \(y=0\). This proves injectivity of \(I-\varepsilon G_+\).

The operator \(I-\varepsilon A\) is onto with inverse \(J_\varepsilon\). Now for an arbitrary \(y\in D(G_+)\), put \(v=(I-\varepsilon G_+)y\) and \(q=J_\varepsilon v\in D(A)\). Since \(G_+\) extends \(A\), \((I-\varepsilon G_+)q=v\); injectivity gives \(y=q\in D(A)\). Therefore \(G_+=A\), including its entire domain. No contraction generation theorem or semigroup resolvent theorem has been imported.

Apply exactly the same construction to \(-A\), using \((I+\varepsilon A)^{-1}=S_{-\varepsilon}\), to obtain \(T_-(t)\) with full generator \(-A\). The preceding generator-domain proof shows that each semigroup preserves \(D(A)\) and commutes with \(A\) there. The approximants for the two signs commute by (H7a), so their strong limits commute as well. For \(\phi\in D(A)\), differentiate \(T_+(t)T_-(t)\phi\); the derivative is
\(T_+(t)A T_-(t)\phi-T_+(t)A T_-(t)\phi=0\).
The product differentiation is legitimate in norm: expand its difference by changing one factor at a time and use the contraction bounds and each fixed-vector derivative. Its initial value is \(\phi\), so fundamental calculus makes the product \(\phi\) for all \(t\geq0\). Density gives the identity on all \(Y\), and the same calculation in the other order gives \(T_-(t)T_+(t)=I\). Hence

<a id="equation-h13"></a>

$$T(t)=\begin{cases}T_+(t),&t\ge0,\\T_-(-t),&t<0,
\end{cases}\tag{H13}$$

is a strongly continuous group: the two semigroup laws and their mutual inverse identities supply mixed-sign products by splitting at the smaller positive time. Each \(T(t)\) is onto, with inverse \(T(-t)\). Both are contractions, so \(\|y\|=\|T(-t)T(t)y\|\leq\|T(t)y\|\leq\|y\|\); hence they are isometries. The left derivative at zero of \(T(t)y\) for \(y\in D(A)\) follows from \(T(-h)(T(h)y-y)/h\to Ay\), so its full group generator is exactly \(A\). Its adjoint group

<a id="equation-h14"></a>

$$\alpha_t=T(t)^*\tag{H14}$$

consists of normal surjective isometries and has norm-continuous predual orbits. The complete interval-average argument (G6)–(G8) in [the earlier generator proof](OA-FLOW-L94.md#oa-flow.gen.closed) now applies to this actual group, identifying its entire weak-star generator domain with \(D(A^*)=D\) and its value with \(A^*=\delta\).

Conversely, suppose \(\delta\) generates such a weak-star continuous isometric group. The two Laplace resolvents in [the earlier Laplace proof](OA-FLOW-L95.md#oa-flow.res.forward), with \(C_\alpha=1\), show that \(I-s\delta\) is onto and its inverse is contractive for every \(s\ne0\). This gives (H1) and (H2). We have proved the equivalence.

<a id="oa-flow.hy.euler"></a><a id="OA-FLOW.HY.EULER"></a>

## Euler approximation and norm convergence on the sun space

The predual resolvent has the Laplace representation

<a id="equation-h15"></a>

$$S_h\phi=\int_0^\infty e^{-u}T(hu)\phi\,du
\qquad(h>0).\tag{H15}$$

Here is a full norm-domain proof of the Laplace representation used in the approximations. For a strongly continuous isometric group \(T\) with norm generator \(A\), the Bochner operator \(Q_hy=\int_0^\infty e^{-u}T(hu)y\,du\) is a contraction for either sign \(h\ne0\). For \(h>0\), change variables in \(T(r)Q_hy\) to obtain

<a id="equation-h14a"></a>

\[
 T(r)Q_hy=e^{r/h}Q_hy
      -h^{-1}e^{r/h}\int_0^r e^{-v/h}T(v)y\,dv.
 \tag{H14a}
\]
The both-sign norm derivative at \(r=0\) gives \(Q_hy\in D(A)\) and \((I-hA)Q_hy=y\). For \(y\in D(A)\), integrate the derivative of \(e^{-u}T(hu)y\); its boundary tends to zero and gives \(Q_h(I-hA)y=y\). For \(h<0\), apply this calculation to the group \(T(-t)\) with generator \(-A\) and positive parameter \(-h\). Thus \(Q_h=S_h\) on every \(y\), proving (H15) and its negative-\(h\) version.

The \(n\)-th power has gamma density \(e^{-u}u^{n-1}/(n-1)!\); we prove its formula and moments directly. Put \(p_n(u)=e^{-u}u^{n-1}/(n-1)!\) for \(u\geq0\). Qualified vector Fubini and the group law show inductively that

<a id="equation-h15a"></a>

\[
 S_h^ny=\int_0^\infty p_n(u)T(hu)y\,du,\qquad
 \int p_n=1,\quad\int u p_n=n,\quad
 \int(u-n)^2p_n=n.
 \tag{H15a}
\]
Indeed convolution of \(p_n\) with \(e^{-u}1_{u\geq0}\) is \(e^{-v}v^n/n!\), by integrating \(u^{n-1}/(n-1)!\) from zero to \(v\). Integration by parts gives \(\int_0^\infty e^{-u}u^mdu=m!\) for each nonnegative integer \(m\); for the boundary, \(e^u\geq u^{m+1}/(m+1)!\) implies \(u^me^{-u}\leq(m+1)!/u\to0\). Induction from \(\int e^{-u}=1\) gives both convergence and this value. The three displayed moments follow by expansion. All integrals have finite norm or nonnegative scalar integrands, so the L24/SC convergence and Fubini proofs apply.

Put \(h=t/n\) in the power formula. The rescaled estimate is centred at the mean \(u=n\). Let \(\omega_y(\eta)=\sup_{|v|\leq\eta}\|T(v)y-y\|\), which tends to zero as \(\eta\downarrow0\). For \(|t|\leq T_0\), the group isometry gives
\(\|T(tu/n)y-T(t)y\|=\|T(t(u/n-1))y-y\|\). The mass of the set \(|t(u/n-1)|>\eta\) is at most \(T_0^2/(n\eta^2)\), by integrating the nonnegative square and using (H15a). Therefore

<a id="equation-h15b"></a>

\[
 \sup_{|t|\leq T_0}\|S_{t/n}^ny-T(t)y\|
 \leq\omega_y(\eta)+\frac{2\|y\|T_0^2}{n\eta^2},
 \qquad S_0=I.
 \tag{H15b}
\]
First let \(n\to\infty\), then \(\eta\downarrow0\). This proves

<a id="equation-h16"></a>

$$T(t)\phi=\lim_{n\to\infty}(I-(t/n)A)^{-n}\phi,\tag{H16}$$

in norm, uniformly for \(t\) in compact real intervals; negative \(t\) uses the semigroup generated by \(-A\). Taking adjoints yields the source's Euler formula

<a id="equation-h17"></a>

$$\alpha_t x
=\underset{n\to\infty}{\operatorname{w^*\! -lim}}
\left(I-\frac{t}{n}\delta\right)^{-n}x,\tag{H17}$$

uniformly for \(t\) in compact intervals after pairing with any fixed \(\phi\in X_*\). The same argument applies to any normal weak-star continuous isometric group with generator \(\delta\): its predual orbits are strongly continuous by the first lemma, L95 gives the same inverse \(R_h\) and thus the same preadjoint \(S_h\), and the complete power estimate (H15a)–(H15b) applies to its predual group. Formula (H17) therefore forces equality of every such group, proving uniqueness.

Let \(X_\odot=\overline D^{\|\cdot\|}\). For \(x\in D\), scalar integration of the generator identity and isometry of \(\alpha\) give

<a id="equation-h18"></a>

$$\|\alpha_t x-x\|\le |t|\,\|\delta x\|.\tag{H18}$$

Thus \(X_\odot\) is closed and invariant, and the restriction of \(\alpha\) is a strongly continuous isometric group. For \(x\in X_\odot\), the norm Bochner integral \(\int_0^\infty e^{-u}\alpha_{hu}x\,du\) stays in \(X_\odot\). Pairing it with every predual vector identifies it with \(R_hx\), by (H15) and its negative-\(h\) version. Thus the restrictions of \(R_h\) are precisely these Laplace operators. The full moment calculation (H15a)–(H15b), now applied to this strongly continuous norm group, proves norm convergence in (H17) on \(X_\odot\), uniformly on compact real time intervals.

<a id="oa-flow.hy.yosida"></a><a id="OA-FLOW.HY.YOSIDA"></a>

## The Yosida exponential needs the time direction

The bounded weak-star continuous Yosida approximants are

<a id="equation-h19"></a>

$$\delta_\varepsilon^+=\delta(I-\varepsilon\delta)^{-1},
\qquad
\delta_\varepsilon^-=\delta(I+\varepsilon\delta)^{-1}.\tag{H19}$$

Normality of these bounded operators follows from
\(\delta_\varepsilon^+=(R_\varepsilon-I)/\varepsilon\) and
\(\delta_\varepsilon^-=(I-R_{-\varepsilon})/\varepsilon\).
Their exponential series are normal by BS0's norm completeness of the preadjoint correspondence. The adjoints of the predual Yosida construction give the indicated weak-star limits uniformly after each fixed predual pairing.

For completeness the norm limits on \(X_\odot\) admit a full quantitative integral estimate. For \(t\geq0\), set \(q=t/\varepsilon\). The exponential series gives

<a id="equation-h19a"></a>

\[
 e^{t\delta_\varepsilon^+}
   =e^{-q}\sum_{m=0}^\infty\frac{q^m}{m!}R_\varepsilon^m.
 \tag{H19a}
\]
On \(X_\odot\), represent \(R_\varepsilon^m\) by (H15a), taking \(m=0\) to be point mass at time zero. These nonnegative weights sum to one. Their time variable has mean \(\varepsilon q=t\) and variance \(2\varepsilon^2q=2t\varepsilon\): (H15a) gives conditional first and second moments \(\varepsilon m,\varepsilon^2(m^2+m)\), while differentiating the scalar exponential series gives weighted moments \(q,q^2+q\) for \(m,m^2\). Hence, for the modulus \(\omega_x\) of the norm-continuous restricted group and \(0\leq t\leq T_0\),

<a id="equation-h19b"></a>

\[
 \|e^{t\delta_\varepsilon^+}x-\alpha_tx\|
 \leq\omega_x(\eta)+\frac{4\|x\|T_0\varepsilon}{\eta^2}.
 \tag{H19b}
\]
This follows by splitting the time integral into \(|v-t|\leq\eta\) and its complement, whose mass is bounded by its variance divided by \(\eta^2\). Infinite sums pass through the integrals by the positive scalar convergence and absolute Banach-series bounds proved earlier. Apply the same calculation to the reversed group for \(t\leq0\), with \(\delta_\varepsilon^-\). Taking first \(\varepsilon\downarrow0\), then \(\eta\downarrow0\), proves all claimed norm convergence. The construction in (H10)–(H14) and this estimate give the correct one-sided limits

For \(t\ge0\),

<a id="equation-h20+"></a>

$$\alpha_t x=
\operatorname{w^*\! -lim}_{\varepsilon\downarrow0}
e^{t\delta_\varepsilon^+}x.\tag{H20+}$$

For \(t\le0\),

<a id="equation-h20-"></a>

$$\alpha_t x=
\operatorname{w^*\! -lim}_{\varepsilon\downarrow0}
e^{t\delta_\varepsilon^-}x.\tag{H20-}$$

uniformly on compact subsets of the indicated half-lines, and in norm on \(X_\odot\). A single choice \(\delta(I-\varepsilon\delta)^{-1}\) does not give a two-sided compact-time limit. For example, on \(\ell^2(\mathbb Z)\) let \(\alpha_t e_n=e^{int}e_n\), with generator \(\delta x=(in x_n)_n\) on \(D=\{x:\sum_n n^2|x_n|^2<\infty\}\). SC7 supplies this counting-measure Hilbert space, and CF8 identifies it as a specified dual and supplies bounded Hilbert adjoints, so this is also a normal dual-space group. The group is strongly continuous: finite-support vectors have continuous orbits, and their dense approximation plus the isometry bound gives continuity for every vector. Its generator has exactly this domain, since coordinate differentiation forces the displayed derivative and square summability; for a vector in that domain, finite coordinate convergence and the bound \(|(e^{int}-1)/t|\leq|n|\) give convergence of the derivative in \(\ell^2\). Finite-support vectors also prove density of the domain. Bounded diagonal multipliers have operator norm equal to the supremum of the absolute diagonal values, by the square-norm estimate and testing coordinate vectors. For \(t<0\), the real parts of \(t(in)/(1-i\varepsilon n)\) approach \(|t|/\varepsilon\) as \(n\to+\infty\), so

<a id="equation-h21"></a>

$$\left\|e^{t\delta(I-\varepsilon\delta)^{-1}}\right\|
=e^{|t|/\varepsilon}.\tag{H21}$$

If these exponentials converged strongly on every vector for fixed \(t<0\) as \(\varepsilon\downarrow0\), their sequence at \(\varepsilon=1/j\) would be pointwise bounded. The uniform-boundedness proof in [the earlier generator lesson](OA-FLOW-L94.md#oa-flow.gen.bounds) would make their operator norms bounded, contradicting (H21). Weak-star convergence on every vector is impossible as well: for each fixed vector the scalar convergence would, by uniform boundedness on the Banach predual, make its image vectors norm bounded; uniform boundedness on the domain Banach space would then bound the operator norms, again contradicting (H21). Thus an unrestricted \(\varepsilon\to0\) formula with positive \(\varepsilon\) for both time signs requires the directional contract in (H20). The Euler formula (H17) is valid for both signs without alteration.

**Problem.** For the diagonal group \(\alpha_t e_n=e^{int}e_n\) on \(\ell^2(\mathbb Z)\), compute \((I-s\delta)^{-1}e_n\) and verify (H1).

**Solution.** Since \(\delta e_n=in e_n\), the resolvent multiplier is \((1-isn)^{-1}\). Its modulus is at most one, so the inverse is a contraction and \(\|(I-s\delta)x\|^2=\sum_n(1+s^2n^2)|x_n|^2\ge\|x\|^2\) on the natural domain. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem XI.1.20 and equation (19), printed pages 326–327 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The theorem proof is omitted there. The argument above supplies its full predual construction, both-sign domains, semigroup generator equality and onto group, together with exact Euler and directional Yosida estimates. The \(s=0\) resolvent convention and time-direction qualification are made explicit rather than treating the displays as domain-free identities. Every mathematical input has the actual earlier proof locator stated above.

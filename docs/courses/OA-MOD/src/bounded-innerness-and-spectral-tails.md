# Inner implementers from spectral tails

Every bounded derivation of a von Neumann algebra is a commutator with an element of that algebra. The proof constructs that element from the frequencies of the derivation's exponential group. Frequency filters determine support projections, nested supports determine a bounded positive operator, and comparison of the two resulting flows identifies the commutator.

This reading imports the existing OA-FLOW proof *Innerness and spectral tails*, through its equation (GI.20), at the bounded hypotheses used here. OA-FLOW retains canonical ownership of that proof. Its current October 2026 repairs were written and checked by GPT-6.1 Sol (OpenAI), Ultra reasoning; its earlier authoring record says Codex, September 2026, without an exact model. The bounded input bridge, selection and local integration were written and checked by GPT-6 Astra (OpenAI), Ultra reasoning, 5 October 2026. Original programme expression is CC0.

The selected Fourier and spectral-tail arguments are reproduced programme text, with mathematical delimiters normalized and prerequisite references bound below. We do not reproduce the book's text. The mathematical antecedent is Takesaki, *Theory of Operator Algebras II*, Theorem XI.3.5 in the approved receipt-backed edition. The broader OA-FLOW automatic-boundedness, unbounded-spectrum and representation results keep their separate scopes; the theorem here assumes boundedness at the outset.

## Bounded algebraic preparation and the theorem

Let \(M\subset B(H)\) be an arbitrary von Neumann algebra; the Hilbert space need not be separable. If \(d:M\to M\) is a bounded complex-linear derivation, then there is \(k\in M\) such that

\[
 d=[k,\cdot],\qquad \|k\|\le\|d\|.
\]

For a star derivation there is a self-adjoint \(h\in Z(M^\alpha)\), where \(\alpha_t=e^{td}\), such that

\[
 d=i[h,\cdot],\qquad 0\le h\le\|d\|1.
\]

Subtracting \(\|d\|1/2\) gives a self-adjoint implementer of norm at most \(\|d\|/2\). No factor, trace, semifiniteness, countable decomposition or standard form is assumed. For an abstract von Neumann algebra, use its defining faithful normal concrete realization and transport the resulting element back.

Put \(d^\dagger(x)=d(x^*)^*\). This is complex linear, has norm \(\|d\|\), and is a derivation: apply the Leibniz rule to \(y^*x^*\) and take adjoints. Consequently

\[
\begin{gathered}
d_1=(d+d^\dagger)/2, \\
d_2=(d-d^\dagger)/(2i).
\end{gathered}
\]

are bounded star derivations, \(\|d_j\|\le\|d\|\), and \(d=d_1+i d_2\). Thus the star case implies the complex case, with the exact implementer and bound computed in the final section.

For a bounded star derivation, induction gives

\[
 d^n(xy)=\sum_{j=0}^n\binom njd^j(x)d^{n-j}(y).
\]

Absolute norm convergence of the double exponential series proves \(e^{td}(xy)=e^{td}(x)e^{td}(y)\). Also \(d(1)=0\), and for real \(t\) the exponential preserves adjoints and has inverse \(e^{-td}\). Therefore \(\alpha_t=e^{td}\) is a unital star automorphism. It is isometric: order preservation in both directions preserves the order bounds and hence the norm of a self-adjoint element; apply this to \(x^*x\) for general \(x\). The series gives operator-norm continuity in \(t\).

An order bijection preserves bounded increasing positive suprema, since applying its inverse transports every proposed upper bound back. Thus every \(\alpha_t\) is normal by the normal-map criterion. Normality of \(d\) is not needed to start this argument, and innerness is not used in the preparation.

## Exact integration, projection and calculus inputs

The scalar measure proof, Sections 1–2, constructs the integral and proves monotone and dominated convergence. Product integration, PI1–PI7, supplies scalar Fubini, Euclidean products, affine substitutions, the polar Gaussian integral and integration by parts. Cube outer measure and regularity, GV1, proves exactly the compact and open approximations used in the Fourier density argument below. The scalar lesson's Lemma 6.1 justifies differentiation of the parameter integrals under integrable bounds.

Here are the norm-completeness details for the \(L^2\) space used in Plancherel. For square-integrable \(u,v\), positivity of \(\int|u-zv|^2\), minimized over \(z\in\mathbb C\), gives Cauchy–Schwarz, and expansion gives the triangle inequality. Given an \(L^2\)-Cauchy sequence, choose a subsequence \(u_j\) with \(\|u_{j+1}-u_j\|_2\le2^{-j}\). The finite sums of \(|u_{j+1}-u_j|\) have \(L^2\) norms at most \(\sum_j2^{-j}\). Monotone convergence applied to their squares shows that their pointwise sum is finite almost everywhere and belongs to \(L^2\). Hence \(u_j\) converges pointwise almost everywhere to a measurable \(u\). Fatou applied to squared tails gives

\[
 \|u-u_j\|_2\le\sum_{k\ge j}2^{-k}.
\]

The original Cauchy sequence has the same norm limit. This proves completeness and the Hilbert-space structure of \(L^2\), rather than importing a Fourier theorem to establish it.

The norm integrals used below are continuous Banach-valued functions on finite-dimensional Euclidean space with integrable scalar norm majorants. Uniform continuity on compact rectangles and completeness make their Riemann sums converge. The triangle inequality gives \(\|\int v\|\le\int\|v\|\). Integrable tail bounds then make rectangle exhaustion Cauchy and independent of the exhaustion. This proves interchange with bounded linear maps. The same inequality and scalar dominated convergence prove the norm dominated-convergence statements used below. Iterated Riemann sums prove Fubini on compact rectangles; scalar Fubini and integrable tails extend it to the whole Euclidean space. Every norm integrand in the selected filter proof is a Schwartz kernel times one or two continuous bounded orbits, or a limit controlled by precisely these bounds. No theorem about arbitrary measurable Banach-valued functions is needed.

The bicommutant proof puts the projection onto the closed span of ranges of any family of projections in the same von Neumann algebra: the subspace and its orthogonal complement are invariant under the commutant. This projection is their join. Complementation gives meets. Increasing projection nets converge strongly to the join, by approximation on finite span vectors and the contraction bound; decreasing nets follow by complements. Polar decomposition puts left supports in the algebra. Normal automorphisms preserve these joins and supports, by order and spectral calculus.

Every self-adjoint contraction \(a\) is the real part of the unitary \(a+i(1-a^2)^{1/2}\). Hence an element commuting with all unitaries of an algebra commutes with every element. Fixed points of normal star automorphisms form an ultraweakly closed unital star algebra, hence a von Neumann algebra. These facts justify the centers and projection joins in the tail construction.

The bounded calculus, spectral theorem and spectral transport supply the bounded self-adjoint spectral calculus and its algebra membership, order and norm bounds. Interval step approximants of mesh \(\eta\) approximate a bounded self-adjoint operator in norm to within \(\eta\). The tail operator itself is constructed below by dyadic sums, so no additional reconstruction theorem is assumed.

## The Euclidean Fourier foundation

**The conventions and Gaussian kernel.** Both integrals below are over \(\mathbb R^m\). Write

\[
\begin{gathered}
Fa(p)={}
\\
\int a(t)e^{it\cdot p}\,dt, \\
F^{-1}b(t)=(2\pi)^{-m} \\
{}\cdot\int b(p)e^{-it\cdot p}\,dp.
\end{gathered}
\tag{GF.1}
\]

Here \(\mathcal S(\mathbb R^m)\) consists of smooth functions whose derivatives decrease faster than every inverse polynomial. Differentiation under the integral and integration by parts show that \(F\) sends this space into itself. Indeed every \(p^\gamma\partial_p^\delta Fa\) is, up to powers of \(i\), the transform of a derivative of \(t^\delta a(t)\) and is bounded by its \(L^1\) norm. These estimates also justify each differentiation and the vanishing boundary terms.

For \(\varepsilon>0\) put

\[
\begin{gathered}
g_\varepsilon(t)={} \\
(4\pi\varepsilon)^{-m/2}e^{-|t|^2/(4\varepsilon)}.
\end{gathered}
\tag{GF.2}
\]

The real Gaussian integral is \(\int_{\mathbb R}e^{-u^2}\,du=\sqrt\pi\): square the positive integral, use Tonelli, and evaluate in polar coordinates. Thus \(\int g_\varepsilon=1\). In one dimension let \(I(p)=Fg_\varepsilon(p)\). Differentiation and integration by parts, using \(t g_\varepsilon(t)=-2\varepsilon g_\varepsilon'(t)\), give

\[
I'(p)=-2\varepsilon p I(p),\qquad I(0)=1.
\]

Solving this real-parameter differential equation gives \(I(p)=e^{-\varepsilon p^2}\). Taking products of the one-dimensional integrals proves

\[
\begin{gathered}
Fg_\varepsilon(p)=e^{-\varepsilon|p|^2}, \\
F^{-1}(e^{-\varepsilon|p|^2})(t) \\
=g_\varepsilon(t).
\end{gathered}
\tag{GF.3}
\]

The second formula follows by the same Gaussian computation, without assuming Fourier inversion.

**Density, cutoffs, and translations.** Smooth compact functions are dense in both \(L^1(\mathbb R^m)\) and \(L^2(\mathbb R^m)\). Here are the measure and smoothing steps. Truncating the magnitude and the spatial support approximates an \(L^p\) function, \(p=1,2\), by bounded functions with bounded support; simple functions approximate those. For a bounded measurable set \(E\), regularity gives a compact \(K\subset E\) and a bounded open \(U\supset E\) with \(|U\setminus K|\) as small as desired. Choose a nonnegative smooth bump \(\rho\) supported in the unit ball with integral one. Such a bump is obtained by normalizing \(e^{-1/(1-|t|^2)}\) inside the ball and extending it by zero; every derivative tends to zero at the boundary. If \(\delta\) is small enough that the \(2\delta\) neighborhood of \(K\) lies in \(U\), then

\[
c=1_{K_\delta}*\rho_\delta,\qquad
\rho_\delta(t)=\delta^{-m}\rho(t/\delta),
\]

is smooth, compactly supported in \(U\), lies between zero and one, and equals one on \(K\). Consequently \(\|1_E-c\|_p^p\le |U\setminus K|\). Applying this to the simple functions proves density. For \(a\in L^1\cap L^2\) the same truncations, simple approximations and cutoffs can make both norms small at once.

Translation \(\tau_y a(t)=a(t-y)\) is an isometry of each \(L^p\). It is continuous in \(y\) for a smooth compact function by uniform continuity on a bounded neighborhood of its support. Density and the isometry bound extend this to every \(a\in L^p\), \(p=1,2\).

The same bump construction gives a smooth compact cutoff equal to one near a prescribed compact set and supported in any open neighborhood of that set. For a finite open cover of a compact \(K\), choose finitely many such functions \(0\le c_i\le1\), each supported in one member of the cover, so that at every point of a neighborhood of \(K\) at least one \(c_i\) equals one. Set

\[
q_1=c_1,\qquad q_i=c_i\prod_{j<i}(1-c_j).
\]

Then each \(q_i\) is a nonnegative smooth compact function with the required support, and \(\sum_i q_i=1-\prod_i(1-c_i)=1\) near \(K\). This proves the finite smooth partition assertion used by the filters.

**Schwartz inversion.** For \(a\in\mathcal S(\mathbb R^m)\), Fubini and the Gaussian formula give

\[
\begin{gathered}
(2\pi)^{-m}\int e^{-it\cdot p} \\
{}\cdot e^{-\varepsilon|p|^2}Fa(p)\,dp \\
=\int a(u) \\
{}\cdot g_\varepsilon(t-u)\,du.
\end{gathered}
\tag{GF.4}
\]

Before evaluating the frequency integral, its absolute iterated integral is bounded by \(\|a\|_1\int e^{-\varepsilon|p|^2}\,dp\). Thus this use of Fubini does not presume inversion. The right side converges to \(a(t)\) uniformly in \(t\): bounded uniform continuity controls the part with \(|u-t|\) small, and the Gaussian mass outside every fixed neighborhood tends to zero. On the left \(Fa\in\mathcal S\subset L^1\), so dominated convergence removes the Gaussian. This proves \(F^{-1}Fa=a\). Applying the same proof with the signs reversed, or replacing \(p\) by \(-p\), proves \(FF^{-1}b=b\) for every Schwartz \(b\). In particular both transforms preserve \(\mathcal S\) and are mutually inverse there.

**Plancherel and integral compatibility.** If \(a,b\in\mathcal S\), substitute the inverse formula for \(b\) into \(\int a\overline b\) and use the integrable majorant \(|a(t)|\,|Fb(p)|\). It yields

\[
\begin{gathered}
\int Fa(p)\overline{Fb(p)}\,dp \\
=(2\pi)^m \\
{}\cdot\int a(t)\overline{b(t)}\,dt.
\end{gathered}
\tag{GF.5}
\]

Therefore \(\mathscr F=(2\pi)^{-m/2}F\) is an isometry on the dense subspace \(\mathcal S\) of \(L^2\). It extends uniquely to an isometry on \(L^2\). Its range is closed and contains \(\mathcal S\), because Schwartz inversion is onto that space; density makes the extension unitary. Its inverse is the extension of \((2\pi)^{m/2}F^{-1}\). For a general \(L^2\) vector these statements concern \(L^2\) limits, with no assertion that its transform is an absolutely convergent integral.

For \(a\in L^1\cap L^2\), choose Schwartz \(a_n\) converging to \(a\) in both norms, as in the density proof. Their integral transforms converge uniformly, since \(\|Fa_n-Fa\|_\infty\le\|a_n-a\|_1\), and their normalized transforms converge in \(L^2\). A subsequence of the latter converges almost everywhere to its \(L^2\) limit: choose squared errors summable and apply Tonelli to their sum. It follows that the integral formula for \((2\pi)^{-m/2}Fa\) agrees almost everywhere with \(\mathscr F a\). In particular

\[
\begin{gathered}
\|Fa\|_2^2=(2\pi)^m\|a\|_2^2 \\
(a\in L^1\cap L^2).
\end{gathered}
\tag{GF.6}
\]

## A smooth-filter calculus

Let \(A_t\) be an isometric strongly continuous group on a complex Banach space \(X\). For \(f\in C_c^\infty(\mathbb R)\) set

\[
\begin{gathered}
k_f(t)={} \\
\frac1{2\pi}\int e^{-itp}f(p)\,dp, \\
A_f x={}
\\
\int k_f(t)A_t x\,dt.
\end{gathered}
\tag{GI.3}
\]

The integral is a norm integral and \(\|A_f\|\le\|k_f\|_1\). With this convention \(A_t x=e^{itp_0}x\) implies \(A_f x=f(p_0)x\).

Define \(S_A(x)\) as the complement of the union of those open sets \(U\) for which \(A_f x=0\) for every \(f\in C_c^\infty(U)\). Write \(X_A(F)=\{x:S_A(x)\subset F\}\) for closed \(F\). This definition is internal to this proof. No equality with a Fourier-algebra hull spectrum is assumed.

**Filter lemma.** We have \(A_fA_g=A_{fg}\), and

\[
\begin{gathered}
S_A(A_f x) \\
\subset S_A(x)\cap\operatorname{supp}f.
\end{gathered}
\tag{GI.4}
\]

If \(f\) is supported off \(S_A(x)\) then \(A_fx=0\). If \(S_A(x)\) is compact and \(f=1\) on a neighborhood of it, then \(A_fx=x\). Empty spectrum implies \(x=0\). The spectrum of a finite sum lies in the union of the summands' spectra.

**Proof.** Fubini and Fourier inversion give \(k_f*k_g=k_{fg}\) and the operator product formula. A compact support disjoint from \(S_A(x)\) has a finite cover by annihilating neighborhoods. A smooth partition on that cover writes its test function as a finite sum of local annihilators. This proves the assertion about support off the spectrum. If a test \(g\) is supported off \(\operatorname{supp}f\), then \(gf=0\). If every local test at a point kills \(x\), the commutation \(A_gA_f=A_fA_g\) shows that every such test kills \(A_fx\). These prove (GI.4).

Choose \(\chi\in C_c^\infty(\mathbb R)\) with \(\chi(0)=1\) and set \(\chi_n(p)=\chi(p/n)\). Then

\[
\begin{gathered}
k_{\chi_n}(t)=n k_\chi(nt), \\
\|A_{\chi_n}x-x\| \\
\le\int |k_\chi(s)| \\
{}\cdot\|A_{s/n}x-x\|\,ds \\
\longrightarrow0.
\end{gathered}
\tag{GI.5}
\]

The bound \(2\|x\||k_\chi(s)|\) is integrable. Thus a vector annihilated by every smooth filter is zero. If \(f=1\) near the compact spectrum, then for every compact test \(g\), the test \((1-f)g\) is supported away from that spectrum. Hence \(A_g(x-A_fx)=0\), so (GI.5) gives \(A_fx=x\). The finite-sum assertion follows by intersecting finitely many annihilating neighborhoods. \(\square\)

A useful consequence is exact finite localization. Given a compact \(K\) and an interval cover of \(K\), choose nonnegative compact bumps subordinate to a finite subcover, divide by their positive sum near \(K\), and multiply by a compact cutoff equal to one near \(K\). This gives tests \(f_j\) with \(\sum f_j=1\) near \(K\). Then \(x=\sum A_{f_j}x\) whenever \(S_A(x)\subset K\). The interval lengths may be arbitrarily small.

**Product and adjoint lemma.** If \(A\) acts by star automorphisms and \(S_A(x),S_A(y)\) are compact, then

\[
\begin{gathered}
S_A(xy) \\
\subset S_A(x)+S_A(y), \\
S_A(x^*)=-S_A(x).
\end{gathered}
\tag{GI.6}
\]

**Proof.** For a test \(v\) whose compact support misses the sum, choose tests \(f,g\) equal to one near the two compact spectra, with support neighborhoods small enough that

\[
v(p+q)f(p)g(q)=0\quad(p,q\in\mathbb R).
\]

Substitute \(x=A_fx\) and \(y=A_gy\) in \(A_v(xy)\) and use the automorphism law. After the changes of variables the coefficient of \(A_q(x)A_r(y)\) is

\[
\begin{gathered}
K(q,r)={} \\
\int k_v(t)k_f(q-t)k_g(r-t)\,dt.
\end{gathered}
\]

Its two-variable Fourier transform, with positive exponent in the transform, is \(v(p+q)f(p)g(q)\), hence \(K=0\). Indeed its \(L^1(\mathbb R^2)\) norm is at most \(\|k_v\|_1\|k_f\|_1\|k_g\|_1\), so the changes of variables and norm-valued Fubini are justified. For exact use of the Fourier foundation above, substitute the inverse transforms of \(f,g\) into \(K\). Compactness of their frequency supports and \(k_v\in L^1\) permit Fubini directly and give

\[
\begin{gathered}
K(q,r)=\frac1{(2\pi)^2}\iint e^{-i(qp+r\zeta)} \\
{}\cdot v(p+\zeta)f(p)g(\zeta)\,dp\,d\zeta=0.
\end{gathered}
\]

Thus no extension of Schwartz injectivity to arbitrary \(L^1\) functions is required. Every such filter kills \(xy\), giving product support. For the adjoint formula put \(f^\natural(p)=\overline{f(-p)}\). Complex conjugation in (GI.3) gives \((A_fx)^*=A_{f^\natural}(x^*)\). This reflects annihilating neighborhoods in both directions. \(\square\)

**Diagonal lemma.** Suppose \(A\) and \(B\) are commuting isometric strongly continuous groups, and \(S_A(x)\subset K\), \(S_B(x)\subset L\) are compact. For \(C_t=A_tB_{-t}\),

\[
S_C(x)\subset K-L. \tag{GI.7}
\]

**Proof.** Choose cutoffs \(f,g\) equal to one near \(K,L\), so \(x=A_fB_gx\). For a test \(v\) off \(K-L\), take their supports small enough that \(v(p-q)f(p)g(q)=0\). The coefficient after filtering the diagonal orbit is

\[
J(q,r)=\int k_v(t)k_f(q-t)k_g(r+t)\,dt.
\]

Its Fourier transform is \(v(p-q)f(p)g(q)\). Its integrable majorant is justified by the same product of three \(L^1\) norms as above. Equivalently, substituting the inverse transforms of \(f,g\) and applying Fubini directly gives

\[
\begin{gathered}
J(q,r)=\frac1{(2\pi)^2}\iint e^{-i(qp+r\zeta)} \\
{}\cdot v(p-\zeta)f(p)g(\zeta)\,dp\,d\zeta=0.
\end{gathered}
\]

Compact frequency supports and \(k_v\in L^1\) justify this identity under exactly the Fourier foundation above. Consequently \(C_vx=0\). \(\square\)

**Zero-frequency lemma.** If \(A_t=e^{tT}\) is isometric with bounded generator \(T\) and \(S_A(x)\subset\{0\}\), then \(Tx=0\).

**Proof.** Choose \(\chi=1\) near zero and \(\chi_\varepsilon(p)=\chi(p/\varepsilon)\). The cutoff lemma gives \(A_{\chi_\varepsilon}x=x\). Integration by parts in (GI.3) gives \(TA_f=A_{ipf}\): the boundary term vanishes because \(k_f\) is Schwartz and the orbit is bounded. Kernel scaling therefore yields

\[
\begin{gathered}
\|Tx\|\le\|k_{ip\chi_\varepsilon}\|_1\|x\| \\
=\varepsilon\|k_{ip\chi}\|_1\|x\| \\
\longrightarrow0.
\end{gathered}
\tag{GI.8}
\]

No assertion about distributions supported at a point is needed. \(\square\)

## The bounded derivation supplies a compact frequency interval

Let \(d\) now be bounded and star preserving, put \(D=\|d\|\), and let \(A_t=\alpha_t=e^{td}\). The case \(D=0\) has implementer \(h=0\). Assume \(D>0\). We prove

\[
\begin{gathered}
S_\alpha(x)\subset[-D,D] \\
(x\in M).
\end{gathered}
\tag{GI.9}
\]

For a smooth compact test \(f\) supported where \(|p|\ge a>D\), put \(g_n(p)=f(p)/(ip)^n\). Integration by parts gives \(d^n\alpha_{g_n}=\alpha_f\). The estimate

\[
\begin{gathered}
\|k_g\|_1 \\
\le C(\|g\|_2+\|g^\prime\|_2).
\end{gathered}
\tag{GI.10}
\]

follows by Cauchy-Schwarz with weight \((1+t^2)^{-1}\), then Plancherel for \(k_g\) and \(t k_g\). Its Fourier-normalization constant \(C\) is independent of \(g\). On the fixed support of \(f\), differentiation gives

\[
\begin{gathered}
g_n^\prime=\frac{f^\prime}{(ip)^n}-\frac{ni f}{(ip)^{n+1}}, \\
\|k_{g_n}\|_1\le C_f(n+1)a^{-n}.
\end{gathered}
\]

It follows that

\[
\begin{gathered}
\|\alpha_f\|\le D^n\|\alpha_{g_n}\| \\
\le C_f(n+1)(D/a)^n\longrightarrow0.
\end{gathered}
\]

Every point outside \([-D,D]\) has a neighborhood admitting such an \(a\), so its local filters vanish and (GI.9) follows. This proves the needed bound without claiming \(\|d\|\) equals its spectral radius. It does not use the stronger equality between generator spectrum and action spectrum.

## Internal support tails recover a positive operator

Choose a faithful normal concrete realization \(M\subset B(H)\); \(H\) is arbitrary. For \(s\in\mathbb R\) define

\[
\begin{gathered}
X_s=M_\alpha([s,\infty)), \\
Q_s=\bigvee_{x\in X_s}\ell(x), \\
Q_sH=\overline{\operatorname{span}\mathcal R_s}.
\end{gathered}
\tag{GI.11}
\]

Here \(\mathcal R_s=\{x\xi:x\in X_s,\ \xi\in H\}\). The projection \(\ell(x)\) is the left support of \(x\), namely the projection onto \(\overline{xH}\). All these projections lie in \(M\). The family \(Q_s\) decreases with \(s\). Since \(1\in X_s\) for \(s\le0\), it equals \(1\) there. By (GI.9), \(X_s=\{0\}\) and \(Q_s=0\) for \(s>D\).

If \(u\) is a unitary in \(M^\alpha\), then \(\alpha_f(uxu^*)=u\alpha_f(x)u^*\), so \(uX_su^*=X_s\) and \(uQ_su^*=Q_s\). For any real \(t\), the commuting filter identity gives \(\alpha_t(X_s)=X_s\). A normal automorphism preserves joins and left supports, hence \(\alpha_t(Q_s)=Q_s\). Thus

\[
Q_s\in Z(M^\alpha). \tag{GI.12}
\]

In particular all \(Q_s\) commute. Define the left-continuous tails

\[
e_s=\bigwedge_{r<s}Q_r. \tag{GI.13}
\]

They decrease, and expansion of the nested meets gives \(e_s=\bigwedge_{u<s}e_u\). Monotone convergence of projections makes the family strongly left continuous. It equals \(1\) for \(s\le0\) and \(0\) for \(s>D\). We now construct the operator without importing spectral-family reconstruction.

Put \(\Delta_n=D/2^n\) and

\[
\begin{gathered}
L_n={} \\
\Delta_n\sum_{j=1}^{2^n}e_{j\Delta_n}, \\
U_n={} \\
\Delta_n\sum_{j=0}^{2^n-1}e_{j\Delta_n}.
\end{gathered}
\tag{GI.13a}
\]

Monotonicity on each refined interval and telescoping give

\[
\begin{gathered}
0\le L_n,
\\
L_n\le L_{n+1}, \\
L_{n+1}\le U_{n+1}, \\
U_{n+1}\le U_n,
\\
U_n\le D1, \\
U_n-L_n \\
=\Delta_n(e_0-e_D) \\
\le\Delta_n1.
\end{gathered}
\tag{GI.13b}
\]

For \(m\ge n\), \(0\le L_m-L_n\le U_n-L_n\), hence \(\|L_m-L_n\|\le\Delta_n\). Norm completeness gives a common limit \(h=\lim L_n=\lim U_n\) in the norm-closed algebra \(Z(M^\alpha)\), with \(0\le h\le D1\). Every \(e_s\) commutes with \(h\). For \(0<s\le D\), multiplying the lower sums by \(e_s\) and \(1-e_s\) yields

\[
\begin{gathered}
L_ne_s \\
\ge\Delta_n\lfloor s/\Delta_n\rfloor e_s, \\
0\le L_n(1-e_s) \\
\le s(1-e_s).
\end{gathered}
\tag{GI.13c}
\]

The first inequality counts all \(j\Delta_n\le s\); for the second, terms with \(j\Delta_n\ge s\) annihilate \(1-e_s\), and each other term is at most that projection. Passing to the limit gives \(he_s\ge se_s\) and \(h(1-e_s)\le s(1-e_s)\). The bounded spectral calculus on these reducing subspaces therefore gives \(1_{(s,\infty)}(h)\le e_s\le1_{[s,\infty)}(h)\). Left continuity removes the endpoint ambiguity:

\[
\begin{gathered}
e_s=\bigwedge_{r<s}e_r \\
\ge\bigwedge_{r<s}1_{(r,\infty)}(h) \\
=1_{[s,\infty)}(h), \\
e_s=1_{[s,\infty)}(h).
\end{gathered}
\tag{GI.13d}
\]

In the middle meet it suffices to take a scalar sequence \(r\uparrow s\); this is no countability assumption on \(M\) or \(H\). Values \(s\le0\) and \(s>D\) follow from the bounds on \(h\). Its actual bounded spectral measure \(E\) thus has exactly these tails, is supported in \([0,D]\), and lies in \(Z(M^\alpha)\) by the preceding bicommutant argument. Consequently

\[
\begin{gathered}
h=\int_{[0,D]}\lambda\,dE(\lambda), \\
\beta_t(x)=e^{ith}xe^{-ith}.
\end{gathered}
\tag{GI.14}
\]

Then \(h\in Z(M^\alpha)\) and \(0\le h\le D1\). The action \(\beta\) is norm continuous. Because \(\alpha\) fixes \(h\), the actions \(\alpha\) and \(\beta\) commute.

This construction is internal to \(M\). The auxiliary Hilbert representation identifies support ranges and never enlarges the algebra containing \(h\).

## The tails transfer each frequency band

For \(x\in X_a\) and \(y\in X_r\), compactness of their spectra and the product lemma give \(xy\in X_{a+r}\). Applying this to finite sums of range vectors and then taking norm closure yields

\[
xQ_rH\subset Q_{a+r}H.
\]

If \(\xi\in e_tH\), it belongs to every \(Q_rH\) for \(r<t\). Thus \(x\xi\) belongs to every \(Q_{a+r}H\), which proves

\[
xe_tH\subset e_{a+t}H. \tag{GI.15}
\]

If \(S_\alpha(x)\subset[a,b]\), apply (GI.15) both to \(x\) and, using the adjoint lemma, to \(x^*\). We get

\[
\begin{gathered}
xE([t,\infty))H \\
\subset E([t+a,\infty))H, \\
x^*E([t,\infty))H \\
\subset E([t-b,\infty))H.
\end{gathered}
\tag{GI.16}
\]

We claim

\[
S_\beta(x)\subset[a,b]. \tag{GI.17}
\]

To prove it directly, partition \([0,D]\) into finitely many disjoint Borel intervals \(I_j\) with diameter at most \(\eta\), choose \(c_j\in I_j\), and put \(E_j=E(I_j)\), \(h_\eta=\sum c_jE_j\). Then \(\|h_\eta-h\|\le\eta\).

If every \(\lambda\in I_j\) and \(\mu\in I_k\) satisfies \(\lambda-\mu<a\), with a strict gap between the interval closures, choose \(t\) so that \(I_k\subset[t,\infty)\) and \(I_j\subset(-\infty,t+a)\). The first relation in (GI.16) gives \(E_jxE_k=0\). The second relation, applied to \(x^*\) and then adjointed, gives the same conclusion when every difference is greater than \(b\) with a strict gap. In particular, a nonzero block must satisfy

\[
\begin{gathered}
c_j-c_k \\
\in[a-2\eta,b+2\eta].
\end{gathered}
\tag{GI.18}
\]

Indeed a violation of this enlarged interval gives the required strict separation, since each interval lies within \(\eta\) of its chosen point. This statement does not require arbitrary Borel spectral synthesis.

The finite expansion

\[
\begin{gathered}
e^{ith_\eta}xe^{-ith_\eta} \\
=\sum_{j,k}e^{it(c_j-c_k)} \\
{}\cdot E_jxE_k.
\end{gathered}
\tag{GI.19}
\]

has its frequency support in the interval in (GI.18). It converges in norm to \(\beta_t(x)\), uniformly for \(t\) in compact sets, by \(\|h_\eta-h\|\to0\). Both orbits have norm \(\|x\|\), so dominated convergence applies to every Schwartz filter. A compact test off \([a,b]\) misses the interval (GI.18) once \(\eta\) is small; it annihilates (GI.19) and hence its limit. This proves (GI.17).

For a concrete check, this mechanism is explicit for \(h=\operatorname{diag}(0,2,5)\) and \(x=E_{21}+E_{32}\) in \(M_3(\mathbb C)\). It is an exact finite example, not a reduction of an arbitrary von Neumann algebra to matrices. Rows represent output spectral levels, columns input levels, and the two nonzero blocks have frequencies \(2\) and \(3\). Its proof locators are (GI.11), (GI.13), and (GI.15)-(GI.19).

## Identify the two commuting actions

Fix \(x\in M\) and \(\varepsilon>0\). Finite smooth localization on \([-D,D]\) gives

\[
\begin{gathered}
x=\sum_{j=1}^n x_j,\qquad x_j=\alpha_{f_j}x, \\
S_\alpha(x_j)\subset I_j.
\end{gathered}
\]

where every \(I_j\) has length at most \(\varepsilon\). By (GI.17), \(S_\beta(x_j)\subset I_j\). The actions commute, so the diagonal lemma for \(C_t=\alpha_t\beta_{-t}\) gives

\[
S_C(x_j)\subset I_j-I_j\subset[-\varepsilon,\varepsilon].
\]

The finite-sum lemma implies this inclusion for \(x\). Since \(\varepsilon\) was arbitrary, \(S_C(x)\subset\{0\}\). The commuting exponential groups give \(C_t=e^{tT}\) with bounded generator \(T=d-i[h,\cdot]\). It is an isometric group, so (GI.8) gives \(Tx=0\). This holds for every \(x\), proving the stated positive star-implementer theorem.

Subtracting the scalar \(D1/2\) from the positive \(h\) leaves its commutator unchanged. Its spectrum is in \([0,D]\), so \(h_c=h-D1/2\) has spectrum in \([-D/2,D/2]\) and norm at most \(D/2\). It remains in \(Z(M^\alpha)\). This proves the centered bound, including \(h_c=0\) when \(D=0\).

For a general complex derivation, put \(d^\dagger(x)=d(x^*)^*\) and

\[
\begin{gathered}
d_1=(d+d^\dagger)/2, \\
d_2=(d-d^\dagger)/(2i).
\end{gathered}
\]

The bounded algebraic preparation above proves both are star derivations and \(d=d_1+i d_2\). Since the involution is isometric, \(\|d^\dagger\|=\|d\|\) and \(D_j=\|d_j\|\le\|d\|\). Apply the centered bound to each component and choose selfadjoint \(h_j\in M\) with \(d_j=i[h_j,\cdot]\) and \(\|h_j\|\le D_j/2\). Then

\[
d=[ih_1-h_2,\cdot]. \tag{GI.20}
\]

The implementer \(k=ih_1-h_2\) satisfies \(\|k\|\le(D_1+D_2)/2\le\|d\|\), proving the bound in the stated bounded theorem. A selfadjoint implementer in the formula \(i[h,\cdot]\) is asserted only for the star-preserving case. The decomposition in the source on printed page 352 contains the outer factor \(i\), as in the formula above.
